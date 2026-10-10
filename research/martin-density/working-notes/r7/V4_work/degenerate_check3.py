"""Finite sanity check of Proposition 4.5 (V4 part 4), version 2.
Self-aligned row (N = 1) with two exceptional carriers tuned through F = {0,1,2,3}:
  l_- (target (e0 - e1)/q*): strict non-peak with q < 0 (n val = -eta);
  l_D (target (e2 - e3)/q*): EXACTLY degenerate swallowing-type peak (val = theta Phi, eps = +1).
Exact negative-d-mismatch data through l_- (omega at k_-).  Then perturb a and re-align with hysteresis.
Checks at f and at f^p: statuses, D = b^+ - b^- z-signed off F, Delta d sign, size of the change."""
import numpy as np
from scipy.optimize import least_squares

rng = np.random.default_rng(7)
L, r, n_extra = 10, 6, 40
Fc = [0, 1, 2, 3]
extra = list(range(4, 4 + n_extra))
sig0 = 4 + n_extra
S = [list(range(sig0 + l * r, sig0 + (l + 1) * r)) for l in range(L)]
DIM = sig0 + L * r
s_diag = 0.5 ** (1 + np.arange(DIM) % 5); s_diag[:4] = [0.9, 0.7, 0.8, 0.6]
def qstar(v): return np.abs(v).sum() + np.linalg.norm(s_diag * v)
l_minus, l_D = 2, 3
h = np.zeros((L, DIM))
for l in range(L):
    for i, s in enumerate(S[l]): h[l, s] = 2.0 ** (-(i + 1))
delta = np.array([min(2.0 ** (-(l + 1)), 1 / (4 * (1 + s_diag.max()) * h[l].sum())) for l in range(L)])
Y = np.zeros((L, DIM))
for l in range(L):
    if l == l_minus: Y[l, 0], Y[l, 1] = 1.0, -1.0
    elif l == l_D: Y[l, 2], Y[l, 3] = 1.0, -1.0
    else:
        pool = Fc + extra + [s for ll in range(l) for s in S[ll][-2:]]
        supp = rng.choice(pool, size=4, replace=False)
        Y[l, supp] = rng.normal(size=4) + 0.3 * np.sign(rng.normal(size=4))
    Y[l] /= qstar(Y[l])
n = np.array([qstar(Y[l] + delta[l] * h[l]) for l in range(L)])
Urows = (Y + delta[:, None] * h) / n[:, None]
EXC = (l_minus, l_D)
# (SF*)-type decay: c_l / c_{l-1} = 2^{-6} delta_{l-1} min(min signature weight, min |target entry|) of level l-1
c = np.zeros(L); c[0] = 1.0
for l in range(1, L):
    eta_prev = min(h[l-1][h[l-1] > 0].min(), np.abs(Y[l-1][Y[l-1] != 0]).min())
    c[l] = c[l-1] * 2.0 ** -6 * delta[l-1] * eta_prev
Phi = np.array([2.0 ** (-1 - (l + 1)) * c[l] for l in range(L)]); lam = Phi.copy()
print("c ratios:", np.array2string(c[1:] / c[:-1], precision=2))

def build(avec, eps_ref=None):
    a = np.zeros(DIM); a[:4] = avec
    nu = np.linalg.norm(s_diag * a); a = a / (np.abs(a).sum() + nu); nu = np.linalg.norm(s_diag * a)
    zh = {j: np.sign(a[j]) + s_diag[j] ** 2 * a[j] / nu for j in Fc}
    z = np.zeros(DIM); assigned = set(Fc)
    for j in Fc: z[j] = np.sign(a[j])
    eps = np.zeros(L); flips = []
    for l in range(L):
        supp = np.nonzero(Y[l])[0]
        A = sum(Y[l, j] * (zh[j] if j in zh else z[j]) for j in supp if j in assigned)
        B = sum(abs(Y[l, j]) for j in supp if j not in assigned)
        if l in EXC: e = 1.0
        elif eps_ref is None: e = np.sign(A) if A != 0 else 1.0
        else:
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
    lo, hi = 1e-200, nu_.max() * 2
    for _ in range(3000):
        mid = np.sqrt(lo * hi)
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    return np.sqrt(lo * hi), nu_

def block_data(val):
    zeta = lam * val; th, nu_ = theta_of(zeta)
    A = np.maximum(np.abs(zeta) - th * Phi ** 2, 0).sum(); C = 1 / (1 + th / A); M = 1 - C
    P = nu_ >= th * (1 - 1e-12)
    w = np.where(P, np.sign(zeta) * M, C * zeta / (Phi ** 2 * A))
    return th, nu_, A, C, M, w

a0, z0, zh0, e0, v0, _ = build(np.array([0.3, 1, 0.3, 1]))
th0 = theta_of(lam * v0)[0]
eta = 0.2 * n[l_minus] * th0 * Phi[l_minus]
def resid(x):
    a, z, zh, eps, val, _ = build(np.exp(x))
    th, nu_ = theta_of(lam * val)
    return [(n[l_minus] * val[l_minus] + eta) / eta, (val[l_D] - th * Phi[l_D]) / (th * Phi[l_D])]
best = None
for x0 in [[0.3, 1, 0.3, 1], [0.2, 1, 0.5, 1], [0.5, 1, 0.2, 1], [0.1, 1, 0.1, 1], [1, 0.3, 1, 0.3]]:
    rr = least_squares(resid, np.log(x0), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
    if best is None or np.abs(rr.fun).max() < np.abs(best.fun).max(): best = rr
avec = np.exp(best.x)
print("tuning residuals (relative):", best.fun)
a, z, zhat, eps, val, _ = build(avec)
th, nu_, Aval, C_, M_, w = block_data(val)
print("nu/theta:", np.array2string(nu_ / th, precision=8))
print("q_- sign:", np.sign(eps[l_minus] * w[l_minus]))
offF = [j for j in range(DIM) if j not in Fc]
def Dvec(w, Aval, val, dalpha=1.0):
    Rw = (lam * w) @ Urows
    Dd = dalpha * lam[l_minus] * val[l_minus] / Aval
    return dalpha * lam[l_minus] * Urows[l_minus] - Dd * Rw, Dd
def zsigned(D, z):
    return [j for j in offF if abs(D[j]) > 1e-300 and not (abs(z[j]) == 1 and z[j] * D[j] > 0)]
Dv, Dd = Dvec(w, Aval, val)
print("at f: Delta d =", Dd, "; D z-signed off F:", len(zsigned(Dv, z)) == 0)
for pp in [1e-12, 1e-11, 1e-10, 1e-9]:
    ap = avec * (1 + pp * np.array([0.3, -0.5, 0.7, -0.2]))
    a2, z2, zh2, eps2, val2, flips = build(ap, eps_ref=eps)
    th2, nu2, A2, C2, M2, w2 = block_data(val2)
    D2, Dd2 = Dvec(w2, A2, val2)
    others = [l for l in range(L) if l not in EXC]
    print(f"p={pp:.0e}: flips={flips} nu_D/theta={nu2[l_D]/th2:.9f} l_- strict non-peak={nu2[l_minus] < th2} (q<0: {np.sign(w2[l_minus]) < 0})"
          f" min others nu/theta={min(nu2[others]/th2):.3f} D^p z-signed={len(zsigned(D2, z2)) == 0} Delta d^p={Dd2:.4e}"
          f" ||R*(w^p - w)||_1={np.abs((lam*(w2-w))@Urows).sum():.2e}")
