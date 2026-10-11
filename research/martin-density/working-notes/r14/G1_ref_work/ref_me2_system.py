"""Gap G-S2: Lemma 5.1 (one two-(X3) minor in isolation) does not give a joint exact point when the same blocks carry
single-(X3) tiny strict minors.  Abstract bilinear model (active-shift blocks, so affine terms are present):
  M1(x)  = x1 - x2            (single-(X3) tiny strict minor of block m;  A_m = {x1 = x2})
  M1'(y) = y1 - y2            (single-(X3) tiny strict minor of block m'; A_m' = {y1 = y2})
  M(x,y) = x1 y1 + x2 y2 + (x1 - x2)/2 + (y1 - y2)/2      (two-(X3) minor; design coefficients)
On A_m x A_m': M = 2 s t.  Start: s = t = sigma, 2 sigma^2 = b (all tiny minors <= b), deviations from A of size b.
All FIRST cofactors dM/dx_l, dM/dy_k are ~ +-1/2 (robust), so Lemma 5.1 (i) applies to M alone -- but its move breaks M1.
The joint zero set {M1 = M1' = M = 0} is at distance ~ sigma = sqrt(b/2) >> Des^C b.
"""
import numpy as np
from scipy.optimize import minimize
for b in [1e-4, 1e-6, 1e-8, 1e-10]:
    sig = np.sqrt(b / 2)
    x = np.array([sig + b / 3, sig]); y = np.array([sig, sig - b / 3])
    M1 = x[0] - x[1]; M1p = y[0] - y[1]
    M = x @ y + (x[0] - x[1]) / 2 + (y[0] - y[1]) / 2
    cof = [y[0] + 0.5, y[1] - 0.5, x[0] + 0.5, x[1] - 0.5]
    # Lemma 5.1 (i): move x1 alone
    x1new = x[0] - M / cof[0]
    M1_after = x1new - x[1]
    # nearest joint zero: on A, M = 2 s t, zero set s = 0 or t = 0; min over both branches of distance (s,t)-> exact
    def joint_dist(z):
        x1, x2, y1, y2 = z
        return np.sum((z - np.r_[x, y]) ** 2)
    best = np.inf
    for branch in range(2):
        cons = [{'type': 'eq', 'fun': lambda z: z[0] - z[1]}, {'type': 'eq', 'fun': lambda z: z[2] - z[3]},
                {'type': 'eq', 'fun': lambda z: z[0] * z[2] + z[1] * z[3] + (z[0] - z[1]) / 2 + (z[2] - z[3]) / 2}]
        z0 = np.r_[x, y].copy()
        if branch == 0: z0[:2] = 0
        else: z0[2:] = 0
        r = minimize(joint_dist, z0, constraints=cons, method='SLSQP', options={'ftol': 1e-30, 'maxiter': 500})
        best = min(best, np.sqrt(r.fun))
    print("b=%.0e |M1|=%.1e |M1'|=%.1e |M|=%.2e first cofactors=%s  Lemma5.1(i) leaves |M1|=%.2e  joint dist=%.3e (=%.2f sqrt(b), =%.1e b)"
          % (b, abs(M1), abs(M1p), abs(M), np.round(cof, 3), abs(M1_after), best, best / np.sqrt(b), best / b))
