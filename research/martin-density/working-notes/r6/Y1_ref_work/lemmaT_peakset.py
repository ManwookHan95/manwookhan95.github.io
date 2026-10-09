# Peak set {nu >= theta} versus the peak set of the norming functional from the dual SOCP, with solver-aware tolerances.
import numpy as np, cvxpy as cp, warnings
warnings.filterwarnings("ignore")
exec(open('lemmaT_indep.py').read().split("# ---- 1.")[0])
rng = np.random.default_rng(5)
mism = 0; tot = 0; worst = 0
for trial in range(150):
    n = int(rng.integers(6, 30))
    Phi = 2.0**(-np.arange(1, n+1)) * rng.uniform(0.2, 1.0, n)
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.0, 3.0, n)
    val, w = norming(zeta, Phi)
    th, A = theta_of(zeta, Phi)
    M = th/(th + A); C = A/(th + A)
    nu = np.abs(zeta)/Phi**2
    # predicted norming functional from Lemma T: |w(k)| = (C/A) min(theta, nu_k), sign of zeta
    wpred = np.sign(zeta)*(C/A)*np.minimum(th, nu)
    worst = max(worst, np.max(np.abs(w - wpred)))
    clear = np.abs(nu - th) > 1e-3*th
    Pw = np.abs(w) >= np.max(np.abs(w))*(1 - 1e-5)
    mism += np.sum((Pw != (nu >= th)) & clear); tot += np.sum(clear)
print("max |w_SOCP - w_LemmaT| = %.2e; peak-set mismatches on clearly separated coordinates: %d of %d" % (worst, mism, tot))
