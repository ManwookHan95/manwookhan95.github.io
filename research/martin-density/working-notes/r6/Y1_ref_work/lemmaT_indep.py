# Independent checks of Lemma T (threshold equation) and Lemma T2 (Lipschitz / raising bounds) of Y1 part 2.
# Dual SOCP: the norming functional w of zeta maximizes <w,zeta> subject to ||w||_inf + ||Phi w||_2 <= 1.
import numpy as np, cvxpy as cp

rng = np.random.default_rng(2026)

def norming(zeta, Phi):
    n = len(zeta); w = cp.Variable(n); s = cp.Variable(); c = cp.Variable()
    cons = [cp.abs(w) <= s, cp.norm2(cp.multiply(Phi, w)) <= c, s + c <= 1]
    prob = cp.Problem(cp.Maximize(zeta @ w), cons)
    prob.solve(solver=cp.CLARABEL, tol_gap_abs=1e-13, tol_gap_rel=1e-13, tol_feas=1e-13)
    return prob.value, w.value

def Psi(x, a, Phi):
    A = np.sum(np.maximum(a - x*Phi**2, 0.0)); B = np.sum(np.minimum(x*Phi, a/Phi)**2)
    return A*A - B

def theta_of(zeta, Phi):
    a = np.abs(zeta); lo, hi = 0.0, 1.0
    while Psi(hi, a, Phi) > 0: hi *= 2
    for _ in range(300):
        mid = 0.5*(lo+hi)
        if Psi(mid, a, Phi) > 0: lo = mid
        else: hi = mid
    th = 0.5*(lo+hi)
    return th, np.sum(np.maximum(a - th*Phi**2, 0.0))

# ---- 1. Lemma T against the dual SOCP
err_norm = 0; err_theta = 0; err_P = 0
for trial in range(150):
    n = int(rng.integers(6, 30))
    Phi = 2.0**(-np.arange(1, n+1)) * rng.uniform(0.2, 1.0, n)
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.0, 3.0, n)
    val, w = norming(zeta, Phi)
    M = np.max(np.abs(w)); C = np.linalg.norm(Phi*w)
    th, A = theta_of(zeta, Phi)
    err_norm = max(err_norm, abs(val - A)/A)
    err_theta = max(err_theta, abs(val*M/C - th)/th)
    nu = np.abs(zeta)/Phi**2
    # peak set from w versus {nu >= theta}: compare on coordinates with |nu - th| > 1e-6 th
    clear = np.abs(nu - th) > 1e-6*th
    Pw = np.abs(w) >= M*(1 - 1e-7)
    err_P += np.sum((Pw != (nu >= th)) & clear)
print("Lemma T vs dual SOCP: max rel err norm %.2e, theta %.2e, peak-set mismatches %d" % (err_norm, err_theta, err_P))

# ---- 2. Lemma T2(b), adversarial: degenerate peak c, perturbation concentrated on near-threshold coordinates
def make_degenerate(zeta, Phi, c):
    # adjust |zeta(c)| so that nu_c = theta(zeta) exactly (bisection on the value)
    sgn = np.sign(zeta[c]) if zeta[c] != 0 else 1.0
    def g(v):
        z = zeta.copy(); z[c] = sgn*v; th, _ = theta_of(z, Phi); return v/Phi[c]**2 - th
    lo, hi = 0.0, 1.0
    while g(hi) < 0: hi *= 2
    for _ in range(200):
        mid = 0.5*(lo+hi)
        if g(mid) < 0: lo = mid
        else: hi = mid
    z = zeta.copy(); z[c] = sgn*0.5*(lo+hi); return z

viol_lb = viol_ub = viol_a = 0; nb = na = 0; worst_ratio = np.inf
for trial in range(2500):
    n = int(rng.integers(6, 24))
    Phi = 2.0**(-np.arange(1, n+1)) * rng.uniform(0.2, 1.0, n)
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.0, 3.0, n)
    th, A = theta_of(zeta, Phi); nu = np.abs(zeta)/Phi**2
    if trial % 2 == 0:
        npk = [k for k in range(n) if nu[k] < th]
        if npk:
            c = npk[rng.integers(len(npk))]; zeta = make_degenerate(zeta, Phi, c)
            th, A = theta_of(zeta, Phi); nu = np.abs(zeta)/Phi**2
        else:
            continue
    else:
        pk = [k for k in range(n) if nu[k] >= th]; c = pk[rng.integers(len(pk))]
    phi = np.sum(Phi**2)
    pk = [k for k in range(n) if nu[k] >= th*(1 + 1e-9)]
    if not pk: continue
    k0 = max(pk, key=lambda k: nu[k]); phi0 = Phi[k0]**2; h0 = min(1.0, nu[k0] - th)
    C1 = (1 + 2*(th + 1)/A)/phi0
    s = A*10**rng.uniform(-7, -1)
    Emax = A*s/(8*(A + th + 1))
    # adversarial direction: lower the other peaks and push strict non-peaks outward (both lower the threshold)
    pert = np.zeros(n)
    for k in range(n):
        if k == c: continue
        pert[k] = -np.sign(zeta[k]) if nu[k] >= th else np.sign(zeta[k])
    wts = 1.0/(np.abs(nu - th) + 1e-12); pert *= wts
    if np.sum(np.abs(pert)) == 0: continue
    pert *= Emax*rng.uniform(0.5, 1.0)/np.sum(np.abs(pert))
    z2 = zeta + pert; z2[c] = zeta[c] + np.sign(zeta[c])*s
    th2, _ = theta_of(z2, Phi); nb += 1
    lb = min(1.0, A*s/(8*phi*(A + th + 1)))
    worst_ratio = min(worst_ratio, (th2 - th)/lb)
    if th2 - th < lb*(1 - 1e-9): viol_lb += 1
    E = np.sum(np.abs(pert))
    if C1*(s + E) < h0 and th2 - th > C1*(s + E)*(1 + 1e-9): viol_ub += 1
    # T2(a) Lipschitz with adversarial direction
    E = min(h0, th)/C1*rng.uniform(0.01, 0.99)
    p3 = pert/np.sum(np.abs(pert))*E if np.sum(np.abs(pert)) > 0 else 0
    th3, _ = theta_of(zeta + p3, Phi); na += 1
    if abs(th3 - th) > C1*E*(1 + 1e-9): viol_a += 1
print("T2(b) lower-bound violations %d / %d (worst ratio actual/bound %.3f); upper-bound violations %d" % (viol_lb, nb, worst_ratio, viol_ub))
print("T2(a) Lipschitz violations %d / %d" % (viol_a, na))
