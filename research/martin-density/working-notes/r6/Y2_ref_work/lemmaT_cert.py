"""Referee check of Lemma T by an independent primal-dual certificate (no SOCP):
given theta = root of Psi, build x_k = sgn(z_k)(|z_k| - theta Phi_k^2)_+, beta_k = (z_k - x_k)/Phi_k,
w_k = sgn(z_k) min(theta, nu_k) * C/|z|, with |z| := A(theta), C chosen so that ||w||_inf + ||Phi w||_2 = 1.
Primal: ||x||_1 = A, ||beta||_2 = sqrt(B) -> |z| <= max(A, sqrt B) = A.  Dual: N(w)=1, <w,z> = A.
Also adversarial test of the perturbed raising bound Lemma T(e)."""
import numpy as np
rng = np.random.default_rng(12345)

def root(a, Phi):
    def Psi(th):
        A = np.sum(np.maximum(a - th*Phi**2, 0)); B = np.sum(Phi**2*np.minimum(th, a/Phi**2)**2)
        return A*A - B
    lo, hi = 0.0, 1.0
    while Psi(hi) > 0: hi *= 2
    for _ in range(300):
        mid = 0.5*(lo+hi)
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)

worst = 0.0
for trial in range(3000):
    n = rng.integers(2, 30)
    Phi = rng.uniform(0.001, 1, n)*2.0**(-rng.uniform(0, 1)*np.arange(n)); Phi *= rng.uniform(0.05, 0.99)/Phi.sum()
    z = rng.normal(size=n)*rng.uniform(0, 1, n)**3
    if np.all(z == 0): continue
    a = np.abs(z); th = root(a, Phi)
    A = np.sum(np.maximum(a - th*Phi**2, 0)); B = np.sum(Phi**2*np.minimum(th, a/Phi**2)**2)
    x = np.sign(z)*np.maximum(a - th*Phi**2, 0); beta = (z - x)/Phi
    nu = a/Phi**2
    v = np.sign(z)*np.minimum(th, nu)          # w proportional to v
    Minf = np.max(np.abs(v)); Cl = np.linalg.norm(Phi*v)
    w = v/(Minf + Cl)                            # N(w) = 1
    dual = w @ z; primal = max(np.sum(np.abs(x)), np.linalg.norm(beta))
    worst = max(worst, abs(primal - dual)/dual, abs(A - np.sqrt(B))/A)
    # M/C ratio must equal theta/|z|
    M = np.max(np.abs(w)); C = np.linalg.norm(Phi*w)
    worst = max(worst, abs(M/C - th/A)*A/th)
print("primal-dual gap / identity residual (max rel):", worst)

# Lemma T(e): random perturbations satisfying the hypothesis must raise theta
viol = 0; tests = 0; tight = np.inf
for trial in range(20000):
    n = rng.integers(2, 20)
    Phi = rng.uniform(0.001, 1, n)*2.0**(-rng.uniform(0, 1)*np.arange(n)); Phi *= rng.uniform(0.05, 0.99)/Phi.sum()
    z = np.abs(rng.normal(size=n))*rng.uniform(0, 1, n)**2 + 1e-12
    a = z; th = root(a, Phi); A = np.sum(np.maximum(a - th*Phi**2, 0)); nu = a/Phi**2
    kp = rng.integers(n)
    z2 = z.copy()
    if nu[kp] >= th and rng.random() < 0.5:   # (i') increase at a peak
        D = z[kp]*rng.uniform(1e-3, 0.5); z2[kp] += D; bound = A*D/(A+th)
    else:
        if nu[kp] > th:  # make it a strict non-peak case only
            continue
        D = z[kp]*rng.uniform(1e-3, 0.99); z2[kp] -= D; bound = nu[kp]*D/(2*(A+th))
    # adversarial perturbation of the other coordinates of total size E < bound (push to lower theta)
    others = [k for k in range(n) if k != kp]
    if not others: continue
    E = bound*rng.uniform(0.0, 0.999)
    wts = rng.dirichlet(np.ones(len(others)))
    for k, wt in zip(others, wts):
        # lowering moves: decrease at peaks, increase at non-peaks
        if nu[k] >= th: z2[k] = max(z2[k] - wt*E, 0)
        else: z2[k] += wt*E
    th2 = root(z2, Phi); tests += 1
    if th2 <= th*(1+1e-12): viol += 1
    tight = min(tight, (th2 - th)/th)
print("Lemma T(e) tests:", tests, "violations:", viol, "min rel increase:", tight)
