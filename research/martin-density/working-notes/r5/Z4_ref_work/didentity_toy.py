"""Referee check (signs/algebra only, finite degenerate model as in Z4_work/maxcontact_toy.py):
 (d1) eq:didentity: Dd*M = (1/(mC)) sum_k Phi_k w_k Dtheta_k + r with |r| <= 2t/sigma   (m = 1, lam = Phi)
 (d2) referee's alternative upper bound (H2''): if every swallowed carrier has q_l >= 0, then
      Dd*M <= sum_{q>0} q_l (tau_l)_- + 2t/sigma   (here all carriers swallowed, eps = +1, q_l = Phi_l w_l / C)
      In general: Dd*M <= sum_{q>0} q (tau)_- + sum_{q<0} |q| (tau)_+ + 2t/sigma  (pure consequence of d1).
We report max |r| / (2t/sigma) and the max violation of the general bound (should be <= 0 up to solver noise)."""
import numpy as np, cvxpy as cp, warnings, sys
warnings.filterwarnings('ignore')
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 3
rng = np.random.default_rng(seed)
n, K = 14, 5
U = rng.standard_normal((n, 3)); U *= 0.15/np.linalg.norm(U, 2)
a = np.zeros(n); a[0], a[1] = 0.6, -0.3
a = a/(np.abs(a).sum() + np.linalg.norm(U.T @ a))
z = np.ones(n); z[0], z[1] = 1., -1.
sig = [[4+2*k, 5+2*k] for k in range(K)]
Y = np.zeros((K, n))
for l in range(K):
    Y[l, 2 + (l % 2)] = (1 if l % 2 == 0 else -1)*rng.uniform(.5, 1)
    Y[l, 0] = rng.uniform(-.5, .5); Y[l, 1] = rng.uniform(-.5, .5)
    if l >= 2: Y[l, sig[l-2][1]] = rng.uniform(-.05, .05)
delta = 0.3; prof = np.array([.5, .25])
u = np.zeros((K, n))
for l, S in enumerate(sig):
    v = Y[l].copy(); v[S] += delta*prof
    u[l] = v/(np.abs(v).sum() + np.linalg.norm(U.T @ v))
Phi = 0.35**(np.arange(K)+1); lam = Phi.copy()
L = (lam[:, None]*u).T
def pstar(h, ret=False):
    A = cp.Variable(n); W = cp.Variable(K); s = cp.Variable()
    cons = [A + L @ W == h, cp.norm(A, 1) + cp.norm(U.T @ A, 2) <= s, cp.norm(W, 'inf') + cp.norm(cp.multiply(Phi, W), 2) <= s]
    pr = cp.Problem(cp.Minimize(s), cons); pr.solve(solver='CLARABEL', tol_gap_abs=1e-11, tol_gap_rel=1e-11, tol_feas=1e-11)
    return (pr.value, A.value, W.value) if ret else pr.value
nu = np.linalg.norm(U.T @ a); e = U.T @ a/nu; zhat = z + U @ e
Rz = lam*(u @ zhat)
Wv = cp.Variable(K); pr = cp.Problem(cp.Maximize(Rz @ Wv), [cp.norm(Wv, 'inf') + cp.norm(cp.multiply(Phi, Wv), 2) <= 1]); pr.solve(solver='CLARABEL')
w = Wv.value; q0 = 1/(1 + pr.value); f = a + L @ w; sigma = 1 - q0
M = np.abs(w).max(); C = np.linalg.norm(Phi*w)
q = Phi*w/C           # eps = +1, m = 1
SG = np.concatenate([-np.logspace(-2.5, 1.5, 24), np.logspace(-2.5, 1.5, 24)])
def contractive(g): return max(pstar(f + s*g) - np.sqrt(1+s*s) for s in SG) <= 2e-9
def to_boundary(g0):
    lo, hi = 0., 1.
    while contractive(hi*g0): hi *= 2
    for _ in range(14):
        mid = (lo+hi)/2
        lo, hi = (mid, hi) if contractive(mid*g0) else (lo, mid)
    return lo
xi = q0*zhat
worst_r, worst_b = 0., -1.
for trial in range(3):
    g0 = rng.standard_normal(n) + 2*rng.standard_normal()*u[rng.integers(K)]
    g0 -= (g0 @ xi)/(a @ xi)*a
    g = 0.999*to_boundary(g0)*g0
    for t in [3e-2, 1e-2, 3e-3]:
        vp, Ap, Wp = pstar(f + t*g, True); vm, Am, Wm = pstar(f - t*g, True)
        Op, Om = (Wp - w)/t, (w - Wm)/t
        dth = lam*(Op - Om); tau = -dth
        dp = (1 - np.abs(w + t*Op).max()/M)/t; dm = (np.abs(w - t*Om).max()/M - 1)/t; Dd = dp - dm
        r = Dd*M - np.sum(Phi*w*dth)/C
        worst_r = max(worst_r, abs(r)/(2*t/sigma))
        bound = np.sum(np.where(q > 0, q*np.maximum(-tau, 0), 0)) + np.sum(np.where(q < 0, -q*np.maximum(tau, 0), 0)) + 2*t/sigma
        worst_b = max(worst_b, Dd*M - bound)
print(f"seed {seed}: q_l signs {np.sign(np.round(q,8))}; max |r|/(2t/sigma) = {worst_r:.3f} (<= 1 expected); "
      f"max violation of upper bound = {worst_b:.2e} (<= ~1e-6 expected)")
