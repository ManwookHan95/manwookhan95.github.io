# Check of Lemma 1.1 (clamp formula) on random blocks, exact J via SOCP.
import numpy as np, cvxpy as cp
rng = np.random.default_rng(1); worst = 0
for trial in range(40):
    K = 14; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5,1,K)
    zeta = rng.normal(size=K)*Phi
    idx = rng.choice(K, 4, replace=False); zeta[idx] *= 1e-2*Phi[idx]   # some near-zero entries -> strict non-peaks
    w = cp.Variable(K)
    pr = cp.Problem(cp.Maximize(zeta@w), [cp.norm(w,'inf') + cp.norm(cp.multiply(Phi,w),2) <= 1]); pr.solve(solver=cp.CLARABEL, tol_gap_abs=1e-11, tol_gap_rel=1e-11)
    w = w.value; nz = pr.value; M = np.abs(w).max(); C = np.linalg.norm(Phi*w)
    r = np.abs(zeta)/(Phi**2*nz)
    wc = np.sign(zeta)*np.minimum(M, C*r)
    worst = max(worst, np.abs(w-wc).max())
print("max |w - clamp| over 40 random blocks:", worst)
