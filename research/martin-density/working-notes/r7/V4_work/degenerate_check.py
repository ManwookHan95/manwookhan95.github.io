"""Finite sanity check of Proposition 4.5 (V4 part 4): self-aligned row with an EXACTLY degenerate swallowing-type peak l_D and a
q<0 strict non-peak l_-, both tuned through F = {p,p',p'',p'''}; exact negative-d-mismatch data through l_-; perturb-and-realign.
N = 1.  Checks: (i) at f: l_D degenerate (nu = theta), l_- strict non-peak q<0, D = b^+ - b^- z-signed off F;
(ii) at f^p: l_D non-degenerate, all other carriers robust peaks, D^p z^p-signed, proxy distance small."""
import numpy as np
from scipy.optimize import brentq, fsolve

rng = np.random.default_rng(7)
L, r, n_extra = 10, 6, 40
Fc = [0, 1, 2, 3]                          # p, p', p'', p'''
extra = list(range(4, 4 + n_extra))
sig0 = 4 + n_extra
S = [list(range(sig0 + l * r, sig0 + (l + 1) * r)) for l in range(L)]
D_ = sig0 + L * r
s_diag = 0.5 ** (1 + np.arange(D_) % 5); s_diag[:4] = [0.9, 0.7, 0.8, 0.6]
def qstar(v): return np.abs(v).sum() + np.linalg.norm(s_diag * v)
l_minus, l_D = 2, 3
c = np.array([10.0 ** (-2.0 * l) for l in range(L)])
Phi = np.array([2.0 ** (-1 - (l + 1)) * c[l] for l in range(L)]); lam = Phi.copy()
h = np.zeros((L, D_))
for l in range(L):
    for i, s in enumerate(S[l]): h[l, s] = 2.0 ** (-(i + 1))
delta = np.array([min(2.0 ** (-(l + 1)), 1 / (4 * (1 + s_diag.max()) * h[l].sum())) for l in range(L)])
Y = np.zeros((L, D_))
for l in range(L):
    if l == l_minus: Y[l, 0], Y[l, 1] = 1.0, -1.0
    elif l == l_D: Y[l, 2], Y[l, 3] = 1.0, -0.8
    else:
        pool = Fc + extra + [s for ll in range(l) for s in S[ll][-2:]]
        supp = rng.choice(pool, size=4, replace=False)
        Y[l, supp] = rng.normal(size=4) + 0.3 * np.sign(rng.normal(size=4))
    Y[l] /= qstar(Y[l])
n = np.array([qstar(Y[l] + delta[l] * h[l]) for l in range(L)])
Urows = (Y + delta[:, None] * h) / n[:, None]

def build(avec, eps_ref=None, Bref=None):
    a = np.zeros(D_); a[:4] = avec
    nu = np.linalg.norm(s_diag * a); a = a / (np.abs(a).sum() + nu); nu = np.linalg.norm(s_diag * a)
    zh = {j: np.sign(a[j]) + s_diag[j] ** 2 * a[j] / nu for j in Fc}
    z = np.zeros(D_); assigned = set(Fc)
    for j in Fc: z[j] = np.sign(a[j])
    eps = np.zeros(L); flips = []
    for l in range(L):
        supp = np.nonzero(Y[l])[0]
        A = sum(Y[l, j] * (zh[j] if j in zh else z[j]) for j in supp if j in assigned)
        B = sum(abs(Y[l, j]) for j in supp if j not in assigned)
        if l in (l_minus, l_D):
            e = 1.0
        elif eps_ref is None:
            e = np.sign(A) if A != 0 else 1.0
        else:                                   # hysteresis
            e = eps_ref[l]
            if e * A <= -(B + delta[l] * h[l].sum()) / 2: e = np.sign(A); flips.append(l)
        for j in supp:
            if j not in assigned: z[j] = e * np.sign(Y[l, j]); assigned.add(j)
        for s_ in S[l]: z[s_] = e; assigned.add(s_)
        eps[l] = e
    zhat = z.copy()
    for j in Fc: zhat[j] = zh[j]
    return a, z, zhat, eps, Urows @ zhat, flips

def theta_of(zeta):
    nu_ = np.abs(zeta) / Phi ** 2
    def Psi(th):
        return np.maximum(np.abs(zeta) - th * Phi ** 2, 0).sum() ** 2 - (Phi ** 2 * np.minimum(th, nu_) ** 2).sum()
    lo, hi = 1e-12, nu_.max() * 2
    for _ in range(400):
        mid = np.sqrt(lo * hi)
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    return np.sqrt(lo * hi), nu_

# tune: unknowns (log r1, log r2) with avec = (r1, 1, r2*k, k) ; equations: n_- val_- = -eta, nu_D = theta
a0, z0, zh0, eps0, val0, _ = build(np.array([1.0, 1.0, 1.0, 1.0]))
th0, _ = theta_of(lam * val0)
eta = 0.2 * n[l_minus] * th0 * Phi[l_minus]
KK = 0.15
def F1(r1, r2):
    a, z, zh, eps, val, _ = build(np.array([r1 * KK, KK, r2, 1.0]))
    return n[l_minus] * val[l_minus] + eta
def r1_of(r2):
    lo, hi = 1e-8, 1e8
    flo = F1(lo, r2)
    for _ in range(200):
        mid = np.sqrt(lo * hi); fm = F1(mid, r2)
        if (fm > 0) == (flo > 0): lo, flo = mid, fm
        else: hi = mid
    return np.sqrt(lo * hi)
def F2(r2):
    r1 = r1_of(r2)
    a, z, zh, eps, val, _ = build(np.array([r1, 1.0, r2, 1.0]))
    th, nu_ = theta_of(lam * val)
    return np.log(nu_[l_D] / th) if nu_[l_D] > 0 else -50.0
def G(r2):
    r1 = r1_of(r2)
    a, z, zh, eps, val, _ = build(np.array([r1 * KK, KK, r2, 1.0]))
    th, nu_ = theta_of(lam * val)
    return val[l_D] - th * Phi[l_D] / 1.0      # m = 1: degenerate iff val_D = theta Phi_D (eps_D = +1)
gr = np.exp(np.linspace(np.log(1e-5), np.log(5.0), 300))
gv = [G(x) for x in gr]
k = [i for i in range(len(gr)-1) if (gv[i] > 0) != (gv[i+1] > 0)]
print('G sign changes:', [(gr[i], gr[i+1]) for i in k][:4])
lo, hi = gr[k[-1]], gr[k[-1]+1]
glo = G(lo)
for _ in range(300):
    mid = 0.5 * (lo + hi); gm = G(mid)
    if (gm > 0) == (glo > 0): lo, glo = mid, gm
    else: hi = mid
r2 = 0.5 * (lo + hi); r1 = r1_of(r2)
avec = np.array([r1 * KK, KK, r2, 1.0])
print("tuning residuals: F1/eta =", F1(r1, r2) / eta, " G/thr =", G(r2) / (theta_of(lam * build(avec)[4])[0] * Phi[l_D]))
a, z, zhat, eps, val, _ = build(avec)
zeta = lam * val; th, nu_ = theta_of(zeta)
print("nu/theta:", np.round(nu_ / th, 6))
Aval = np.maximum(np.abs(zeta) - th * Phi ** 2, 0).sum()
C_ = 1 / (1 + th / Aval); M_ = 1 - C_
P = nu_ >= th * (1 - 1e-9)
w = np.where(P, np.sign(zeta) * M_, C_ * zeta / (Phi ** 2 * Aval))
print("l_- : nu/theta =", nu_[l_minus] / th, " q_- sign:", np.sign(eps[l_minus] * w[l_minus]), "; l_D degenerate:", abs(nu_[l_D] / th - 1) < 1e-8)

def D_vec(lam, w, Aval, val, dalpha=1.0):
    Rw = (lam * w) @ Urows
    Dd = dalpha * lam[l_minus] * val[l_minus] / Aval
    return dalpha * lam[l_minus] * Urows[l_minus] - Dd * Rw, Dd
Dv, Dd = D_vec(lam, w, Aval, val)
offF = [j for j in range(D_) if j not in Fc]
bad = [j for j in offF if abs(Dv[j]) > 1e-300 and not (abs(z[j]) == 1 and z[j] * Dv[j] > 0)]
print("at f: Delta d =", Dd, " D z-signed off F:", len(bad) == 0, " #supp", sum(abs(Dv[j]) > 1e-300 for j in offF))

# perturb and realign
for pp in [1e-11, 1e-10, 1e-9, 1e-8, 1e-6]:
    ap = avec * (1 + pp * np.array([0.3, -0.5, 0.7, -0.2]))
    a2, z2, zh2, eps2, val2, flips = build(ap, eps_ref=eps)
    zeta2 = lam * val2; th2, nu2 = theta_of(zeta2)
    A2 = np.maximum(np.abs(zeta2) - th2 * Phi ** 2, 0).sum(); C2 = 1 / (1 + th2 / A2); M2 = 1 - C2
    P2 = nu2 >= th2
    w2 = np.where(P2, np.sign(zeta2) * M2, C2 * zeta2 / (Phi ** 2 * A2))
    D2, Dd2 = D_vec(lam, w2, A2, val2)
    bad2 = [j for j in offF if abs(D2[j]) > 1e-300 and not (abs(z2[j]) == 1 and z2[j] * D2[j] > 0)]
    others = [l for l in range(L) if l not in (l_minus, l_D)]
    print(f"p={pp}: flips={flips} nu_D/theta={nu2[l_D]/th2:.6f} l_- nonpeak={nu2[l_minus]<th2} min others nu/theta={min(nu2[others]/th2):.3e}"
          f" D^p z-signed={len(bad2)==0} Delta d^p={Dd2:.3e} ||R*(w2-w)||_1={np.abs((lam*(w2-w))@Urows).sum():.2e} ||z2-z||_1={np.abs(z2-z).sum():.1f}")
