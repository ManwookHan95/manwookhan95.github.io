"""Referee check of Prop 1.2 (far lowerings): one block, clamp formula Phi_k w(k) = s_k min(Phi_k M, C v_k), C root of
F(c;v) = sum_k min(Phi_k (1-c)/c, v_k)^2 = 1.  Coarse carriers k < Lc: v^L_k = r v_k (common ratio r = |R zhat|/|R zhat^L|);
fine carriers k >= Lc: v^L_k arbitrary in [0, vmax].  We compare
  S_true  = sum_k Phi_k |w^L(k) - w(k)|           (what p*(f^L - f) needs, up to the factor m)
  eps     = sum_{k >= Lc} Phi_k                      (eps_L / m)
  sup_coarse |w^L(k) - w(k)| / eps                   (the referee's multiplicative fix predicts O(1))
and the quantity the written step (iv) sums, sum_k v_k (which grows linearly in the number of carriers)."""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(0)
def solve(Phi, v):
    F = lambda c: np.sum(np.minimum(Phi*(1-c)/c, v)**2) - 1.0
    C = brentq(F, 1e-9, 1-1e-12)
    M = 1 - C
    w = np.minimum(Phi*M, C*v)/Phi
    return C, M, w
for n in [40, 80, 160]:
    k = np.arange(1, n+1)
    Phi = 0.5**k * rng.uniform(0.5, 1.0, n)          # Phi_k <= 2^{-k}
    # v_k = m|u_k(zhat)|/|R zhat|: bounded, NOT summable; scale so that C is moderate (sum Phi^2 (M/C)^2 vs sum v^2)
    v = rng.uniform(0.0, 1.0, n) * 0.6
    C, M, w = solve(Phi, v)
    for Lc in [8, 12, 16]:
        eps = Phi[Lc:].sum()
        # lowering: coarse values scaled by common ratio r, |r-1| ~ eps; fine values arbitrary
        r = 1 + eps*rng.uniform(-1, 1)
        vL = v.copy(); vL[:Lc] *= r; vL[Lc:] = rng.uniform(0, 0.6, n-Lc)
        CL, ML, wL = solve(Phi, vL)
        S_true = np.sum(Phi*np.abs(wL - w))
        supc = np.max(np.abs(wL[:Lc] - w[:Lc]))
        print(f"n={n:4d} Lc={Lc:3d} C={C:.3f} eps={eps:.2e} |C^L-C|/eps={abs(CL-C)/eps:7.3f} "
              f"sup_coarse|dw|/eps={supc/eps:7.3f} S_true/eps={S_true/eps:7.3f} sum_k v_k={v.sum():7.2f}")
