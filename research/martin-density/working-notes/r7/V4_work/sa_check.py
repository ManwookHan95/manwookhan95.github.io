"""Finite sanity check of Construction SA (V4 part 2) for N = 1.

Model: one block, L carriers, coordinates = Z0 = {0,1} (p, p'), extra non-signature coordinates, and signature sets S_l.
Diagonal base U: U^* e_j = s_j kappa_j.  q*(a) = ||a||_1 + ||U^* a||.
Carrier l: u_l = (y_l + delta_l h_l)/n_l, Phi_l = 2^{-1-k} c_l (m = 1), lambda_l = Phi_l.
Construction: F = {0,1}, a > 0 on F tuned so that n_- val_- = -eta; owner-rule recursion for z.
Checks: (a) sgn val_l = eps_l, |val_l| >= delta_l H_l/n_l; (b) peaks via threshold equation; (c) l_- strict non-peak with q < 0;
(d) W = sum lambda_l eps_l u_l 1_{F^c} z-signed; (e) block norm via SOCP equals A(theta).
"""
import numpy as np
import cvxpy as cp

rng = np.random.default_rng(1)
L = 9            # carriers
r = 6            # signature size per carrier
n_extra = 30     # extra non-signature coordinates
Z0 = [0, 1]
extra = list(range(2, 2 + n_extra))
sig_start = 2 + n_extra
S = [list(range(sig_start + l * r, sig_start + (l + 1) * r)) for l in range(L)]
D = sig_start + L * r
s_diag = 0.5 ** (1 + np.arange(D) % 7)          # diagonal base entries
s_diag[0] = 0.8; s_diag[1] = 0.6

def qstar(v):
    return np.abs(v).sum() + np.linalg.norm(s_diag * v)

l_minus = 5
c = np.array([10.0 ** (-2.5 * l) for l in range(L)])     # fast decay (stand-in for (SF*))
Phi = np.array([2.0 ** (-1 - (l + 1)) * c[l] for l in range(L)])
lam = Phi.copy()                                          # m = 1
# signatures (index weights instead of 2^{-s} to avoid underflow)
h = np.zeros((L, D))
for l in range(L):
    for i, s in enumerate(S[l]):
        h[l, s] = 2.0 ** (-(i + 1))
delta = np.array([min(2.0 ** (-(l + 1)), 1 / (4 * (1 + s_diag.max()) * h[l].sum())) for l in range(L)])
# targets: random sparse on Z0 ∪ extra ∪ earlier signature sets (allowedness (a)); l_minus gets y*
Y = np.zeros((L, D))
for l in range(L):
    if l == l_minus:
        Y[l, 0], Y[l, 1] = 1.0, -1.0
    else:
        pool = Z0 + extra + [s for ll in range(l) for s in S[ll][-2:]]   # late coords of earlier sets
        supp = rng.choice(pool, size=4, replace=False)
        Y[l, supp] = rng.normal(size=4) + 0.3 * np.sign(rng.normal(size=4))
    Y[l] /= qstar(Y[l])
n = np.array([qstar(Y[l] + delta[l] * h[l]) for l in range(L)])
U_rows = (Y + delta[:, None] * h) / n[:, None]   # u_l

def build(ratio, eta_target=None):
    a = np.zeros(D); a[0], a[1] = ratio, 1.0
    nu = np.linalg.norm(s_diag * a); a = a / (np.abs(a).sum() + nu); nu = np.linalg.norm(s_diag * a)
    zhat_F = {j: np.sign(a[j]) + s_diag[j] ** 2 * a[j] / nu for j in Z0}
    z = np.zeros(D); assigned = set(Z0)
    for j in Z0: z[j] = np.sign(a[j])
    eps = np.zeros(L)
    for l in range(L):
        supp = np.nonzero(Y[l])[0]
        A = sum(Y[l, j] * (zhat_F[j] if j in zhat_F else z[j]) for j in supp if j in assigned)
        if l == l_minus:
            e = 1.0
        else:
            e = np.sign(A) if A != 0 else 1.0
        for j in supp:
            if j not in assigned:
                z[j] = e * np.sign(Y[l, j]); assigned.add(j)
        for s_ in S[l]:
            z[s_] = e; assigned.add(s_)
        eps[l] = e
    zhat = z.copy()
    for j in Z0: zhat[j] = zhat_F[j]
    val = U_rows @ zhat
    return a, z, zhat, eps, val

def theta_of(zeta):
    nu_ = np.abs(zeta) / Phi ** 2
    def Psi(th):
        A = np.maximum(np.abs(zeta) - th * Phi ** 2, 0).sum()
        B = (Phi ** 2 * np.minimum(th, nu_) ** 2).sum()
        return A * A - B
    lo, hi = 1e-300, nu_.max() * 2
    for _ in range(3000):
        mid = np.sqrt(lo * hi) if hi / lo > 4 else 0.5 * (lo + hi)
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi), nu_

# tune ratio so that n_- val_- = -eta
eta = None
def g(ratio):
    a, z, zhat, eps, val = build(ratio)
    return n[l_minus] * val[l_minus]
# first build to get theta_0 scale
a, z, zhat, eps, val = build(1.0)
th, nu_ = theta_of(lam * val)
eta = 0.25 * n[l_minus] * th * Phi[l_minus]   # well below threshold
target = -eta
lo, hi = 1e-6, 1e6
for _ in range(200):
    mid = np.sqrt(lo * hi)
    if g(mid) > target: hi = mid
    else: lo = mid
ratio = np.sqrt(lo * hi)
a, z, zhat, eps, val = build(ratio)
zeta = lam * val
th, nu_ = theta_of(zeta)
print("n_- val_- =", n[l_minus] * val[l_minus], " target", target)
print("theta =", th)
for l in range(L):
    status = "peak" if nu_[l] >= th else "non-peak"
    print(f"l={l} eps={eps[l]:+.0f} val={val[l]:+.3e} |val|>=dH/n:{abs(val[l]) >= delta[l]*h[l].sum()/n[l]*(1-1e-12) or l==l_minus}"
          f" nu/theta={nu_[l]/th:.3e} {status} sign_ok={np.sign(val[l])==eps[l] or l==l_minus}")
# q of l_minus
M = None
# norming functional w via Lemma T: off P w = C zeta/(Phi^2 |zeta|), on P w = sgn * M
Pset = nu_ >= th
Aval = np.maximum(np.abs(zeta) - th * Phi ** 2, 0).sum()   # = |zeta|
# M, C: M + C = 1, M = C theta/|zeta|
C_ = 1.0 / (1.0 + th / Aval); M_ = 1 - C_
w = np.where(Pset, np.sign(zeta) * M_, C_ * zeta / (Phi ** 2 * Aval))
q_minus = eps[l_minus] * Phi[l_minus] * w[l_minus] / (1 * C_)
print("w(l_-) =", w[l_minus], " q_- =", q_minus, " (expect < 0)")
print("check N(w) = ||w||_inf + ||Phi w||_2 =", np.abs(w).max() + np.linalg.norm(Phi * w), "; <w,zeta> - |zeta| =", w @ zeta - Aval)
# SOCP for |zeta|_Phi
gam = cp.Variable(L)
prob = cp.Problem(cp.Minimize(cp.maximum(cp.norm1(zeta - cp.multiply(Phi, gam)), cp.norm(gam, 2))))
prob.solve()
print("SOCP |zeta| =", prob.value, " A(theta) =", Aval, " rel.err", abs(prob.value - Aval) / Aval)
# W z-signed off F
W = (lam * eps) @ U_rows
offF = [j for j in range(D) if j not in Z0]
bad = [j for j in offF if abs(W[j]) > 0 and not (abs(z[j]) == 1 and z[j] * W[j] > 0)]
print("W z-signed off F:", len(bad) == 0, " #coords with W!=0:", sum(abs(W[j]) > 0 for j in offF), " bad:", bad[:10])

# ---- Proposition 3.2 check: V = u_- - (val_-/|zeta|) R^* w is z-signed off F; Delta d < 0
Rstar_w = (lam * w) @ U_rows                 # R^* w = sum_k lambda_k w(k) u_k
V = U_rows[l_minus] - (val[l_minus] / Aval) * Rstar_w
badV = [j for j in offF if abs(V[j]) > 1e-300 and not (abs(z[j]) == 1 and z[j] * V[j] > 0)]
print("V z-signed off F:", len(badV) == 0, " #coords V!=0 off F:", sum(abs(V[j]) > 1e-300 for j in offF), " bad:", badV[:10])
dalpha = 1.0
Delta_d = dalpha * lam[l_minus] * val[l_minus] / Aval
print("Delta d =", Delta_d, "(expect < 0)")
# exact identity check: R^*(omega^- - omega^+) - Delta d R^* w == Delta_alpha lambda_- V
lhs = dalpha * lam[l_minus] * U_rows[l_minus] - Delta_d * Rstar_w
print("identity residual:", np.abs(lhs - dalpha * lam[l_minus] * V).max())
# d(omega) via the definition <D w, D omega>/C at k_-:
d_e = Phi[l_minus] ** 2 * w[l_minus] / C_
print("d(e_k-) =", d_e, " zeta(k-)/|zeta| =", zeta[l_minus] / Aval)
