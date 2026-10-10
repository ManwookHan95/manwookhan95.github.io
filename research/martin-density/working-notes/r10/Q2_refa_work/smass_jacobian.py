"""Referee (a): independent finite-difference test of Q2 4.0 (exact Jacobian with S-mass common mode) and of the bordered
column of a block-norm lever (Corollary 4.2), in a one-block Martin-type model with exact forced data (threshold equation).

Model: base coordinates 0..n-1, diagonal base mu (U* e_j* = mu_j k_j).  Carriers k = 0..K-1, block weights lambda_k = Phi_k.
Each carrier has a target on the shallow coordinates {0,1} plus a private signature set S_k.  Some support coordinates p_l lie in S_l
(THICK S-mass lever coordinates, |a(p_l)| not small).  Omega = the strict non-peaks with S-mass levers; a peak k* gets a
block-norm lever = z-move at a private contact j* of S_{k*} (off the support).
F_l(P) = eps_l [ u_l(xhat(P)) - (A(P)/A0) u_l(zhat0) ]  (l in Omega).
Predicted Jacobian (Q2 4.0):  N = I - gt h^T - p q^T,  gt = g - G p,  g_k = eps_k <U* u_k, e1>, h_l = |A1(p_l)|/(nu1 |u_l(p_l)|),
G = sum_k lambda_k w(k) <U* u_k, e1> (all carriers),  p_l = eps_l u_l(zhat0)/A0,  q_k = eps_k lambda_k w(k).
Block-norm lever column (Cor 4.2): -pi p,  pi = eps lambda_{k*} w(k*)  (unit step moves u_{k*}(xhat) by eps).
"""
import numpy as np
from scipy.optimize import brentq

rng = np.random.default_rng(11)

def block(zeta, Phi):
    nu = np.abs(zeta) / Phi**2
    def G(th):
        P = nu >= th
        A = (Phi[P]**2 * (nu[P] - th)).sum()
        return A**2 - th**2 * (Phi[P]**2).sum() - (nu[~P]**2 * Phi[~P]**2).sum()
    hi = nu.max()
    th = brentq(G, 1e-14 * hi, hi * (1 - 1e-15), xtol=1e-17 * hi, rtol=1e-15, maxiter=1000)
    P = nu >= th
    A = (Phi[P]**2 * (nu[P] - th)).sum()
    M = th / (A + th); C = A / (A + th)
    w = np.where(P, np.sign(zeta) * M, C * zeta / (Phi**2 * A))
    return w, A, M, C, th, P

class Model:
    def __init__(self, K, nsig, Phi, mu, targets, delta):
        self.K, self.nsig = K, nsig
        self.n = 2 + K * nsig
        self.Phi = np.array(Phi); self.lam = self.Phi.copy(); self.mu = np.array(mu)
        self.S = [list(range(2 + k * nsig, 2 + (k + 1) * nsig)) for k in range(K)]
        self.delta = delta
        self.hsig = []
        for k in range(K):
            hs = np.zeros(self.n)
            for i, j in enumerate(self.S[k]): hs[j] = 2.0**(-i - 1) * (1 if i % 3 else -1)
            self.hsig.append(hs)
        self.U = np.array([self.carrier(k, targets[k]) for k in range(K)])
    def carrier(self, k, tg):
        y = np.zeros(self.n); y[0], y[1] = tg
        v = y / self.qstar(y) + self.delta[k] * self.hsig[k]
        return v / self.qstar(v)
    def qstar(self, A):
        return np.abs(A).sum() + np.linalg.norm(self.mu * A)
    def forced(self, A_un, z):
        a = A_un / self.qstar(A_un)
        nu = np.linalg.norm(self.mu * a); e = self.mu * a / nu
        zhat = z + self.mu * e
        val = self.U @ zhat
        w, A, M, C, th, P = block(self.lam * val, self.Phi)
        return dict(a=a, A_un=A_un, nu=nu, e=e, zhat=zhat, val=val, w=w, A=A, M=M, C=C, th=th, P=P)
    def tune_small(self, k, A_un, z, target_val):
        """choose the shallow target (1, c) of carrier k so that u_k(zhat) = target_val"""
        a = A_un / self.qstar(A_un); nu = np.linalg.norm(self.mu * a); zhat = z + self.mu * self.mu * a / nu
        f = lambda c: self.carrier(k, (1.0, c)) @ zhat - target_val
        cs = np.linspace(-6, 6, 241); vs = [f(c) for c in cs]
        for i in range(len(cs) - 1):
            if vs[i] * vs[i + 1] < 0:
                c = brentq(f, cs[i], cs[i + 1], xtol=1e-15)
                self.U[k] = self.carrier(k, (1.0, c)); return True
        return False

worst, worst_b, ntr, maxh = 0.0, 0.0, 0, 0.0
for trial in range(200):
    K, nsig = 5, 6
    Phi = sorted(rng.uniform(0.02, 0.25, K), reverse=True)
    mu = np.concatenate([[0.6, 0.5], 0.45 * rng.uniform(0.5, 1.0, K * nsig)])
    targets = [(1.0, rng.uniform(-1, 1)) for _ in range(K)]
    M_ = Model(K, nsig, Phi, mu, targets, delta=rng.uniform(0.2, 0.6, K))
    # base row: support {0,1} plus one thick lever coordinate in S_l for some carriers
    z = np.zeros(M_.n); A1 = np.zeros(M_.n)
    A1[0], A1[1] = 1.0, 0.6; z[0], z[1] = 1.0, 1.0
    for k in range(K):
        z[M_.S[k]] = rng.choice([-1.0, 1.0]) * rng.uniform(0.2, 1.0, nsig)   # mixed contacts/free
    lev = {}
    Omc = [2, 3, 4]
    for l in Omc:
        p = M_.S[l][0]
        A1[p] = rng.choice([-1.0, 1.0]) * rng.uniform(0.05, 0.3)       # thick support coordinate in S_l
        z[p] = np.sign(A1[p]); lev[l] = p
    kst = 0; jst = M_.S[kst][1]; z[jst] = 0.0                          # block-norm lever coordinate (free, zero data assumed)
    ok = True
    for it in range(3):
        D0 = M_.forced(A1, z)
        for l in Omc:
            ok = ok and M_.tune_small(l, A1, z, rng.uniform(0.2, 0.7) * D0['th'] * M_.Phi[l] * rng.choice([-1, 1]))
    if not ok:
        continue
    D0 = M_.forced(A1, z)
    Om = [l for l in Omc if not D0['P'][l] and abs(M_.U[l, lev[l]]) > 1e-3]
    peaks = [k for k in range(K) if D0['P'][k]]
    if len(Om) < 2 or kst not in peaks:
        continue
    D1 = M_.forced(A1, z)
    if any(D1['P'][l] for l in Om) or not D1['P'][kst]:
        continue
    nu1 = np.linalg.norm(M_.mu * A1)                               # nu of the unnormalized pre-row (scale cancels in values)
    e1 = D1['e']
    eps = {l: np.sign(A1[lev[l]] * M_.U[l, lev[l]]) for l in Om}
    beta = {l: nu1 / (M_.mu[lev[l]]**2 * abs(M_.U[l, lev[l]])) for l in Om}
    epsk = 1.0
    def Fmap(P, P0):
        AA = A1.copy(); zz = z.copy()
        for i, l in enumerate(Om):
            AA[lev[l]] += np.sign(A1[lev[l]]) * beta[l] * P[i]
        zz[jst] += epsk * P0 / M_.U[kst, jst]
        D = M_.forced(AA, zz)
        return np.array([eps[l] * (D['val'][l] - D['A'] / D1['A'] * D1['val'][l]) for l in Om])
    hstep = 1e-7
    n = len(Om)
    J = np.array([(Fmap(hstep * e_, 0.0) - Fmap(-hstep * e_, 0.0)) / (2 * hstep) for e_ in np.eye(n)]).T
    col = (Fmap(np.zeros(n), hstep) - Fmap(np.zeros(n), -hstep)) / (2 * hstep)
    Ustar_u_e = np.array([(M_.mu * M_.U[k]) @ e1 for k in range(K)])     # <U* u_k, e1>
    g = np.array([eps[l] * Ustar_u_e[l] for l in Om])
    h = np.array([abs(A1[lev[l]]) / (nu1 * abs(M_.U[l, lev[l]])) for l in Om])
    p = np.array([eps[l] * D1['val'][l] / D1['A'] for l in Om])
    q = np.array([eps[l] * M_.lam[l] * D1['w'][l] for l in Om])
    G = (M_.lam * D1['w'] * Ustar_u_e).sum()
    gt = g - G * p
    Nth = np.eye(n) - np.outer(gt, h) - np.outer(p, q)
    pi_ = epsk * M_.lam[kst] * D1['w'][kst]
    colth = -pi_ * p
    worst = max(worst, np.abs(J - Nth).max() / max(1, np.abs(Nth).max()))
    worst_b = max(worst_b, np.abs(col - colth).max() / max(1e-12, np.abs(colth).max()))
    maxh = max(maxh, h.max())
    ntr += 1
print(f"{ntr} trials; max rel |J_fd - N_pred| = {worst:.2e}; max rel |col_fd - (-pi p)| = {worst_b:.2e}; max h = {maxh:.2f}")
