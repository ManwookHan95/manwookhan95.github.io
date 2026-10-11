# Referee check of H2 Corollary 4.2 (U-block, linear tiny minors M_i(x, y) = C'_P x + C'_Q y, x = oriented pinned kind-(iv) ratios
# (one-sided: x >= rc, after the free positive rescaling is absorbed), y = pinned two-sided ratios (free)).
# Cor 4.2 claims: NOT residual if (A) every tiny minor containing a kind-(iv) ratio has a nonzero cofactor on some two-sided row,
# or (B) in every such minor the kind-(iv) cofactors take both signs.  We exhibit counterexamples with several minors.
import numpy as np
from scipy.optimize import linprog

def primal_feasible(Cp, Cq, c):
    nP = Cp.shape[1]; nQ = Cq.shape[1]
    A = np.hstack([Cp, Cq]); b = np.zeros(Cp.shape[0])
    bounds = [(c[i], None) for i in range(nP)] + [(None, None)] * nQ
    res = linprog(np.zeros(nP + nQ), A_eq=A, b_eq=b, bounds=bounds, method='highs')
    return res.status == 0

# (A): x = (x1, x2, x3): x2 in K+ (rt>0), x3 in K- (rt<0); one two-sided y.
# M1 = x1 + y ; M2 = x1 + 2 x2 + 3 x3 + y.  Combination M2 - M1 = 2 x2 + 3 x3 has nonnegative kind-(iv) coefficients, Q-part 0.
Cp = np.array([[1.0, 0.0, 0.0], [1.0, 2.0, 3.0]]); Cq = np.array([[1.0], [1.0]])
for eps in [-1e-4, 1e-4]:
    # start ratios: x1 arbitrary, x2 = 0.3, x3 = -(0.6 - eps)/3 so that 2x2 + 3x3 = eps; y0 chosen so that M1 = 0 at start
    rc = np.array([0.5, 0.3, -(0.6 - eps) / 3.0])
    print("(A) lambda^T M(rc) = %+.1e  feasible:" % eps, primal_feasible(Cp, Cq, rc),
          " every minor has a two-sided cofactor:", bool(np.all(Cq != 0)))
# (B): mixed-sign kind-(iv) cofactors in EVERY minor, no two-sided rows.
# M1 = x1 - x2 ; M2 = x2 - x1 + x3 + x4 ; M1 + M2 = x3 + x4 (x3 in K+, x4 in K-).
Cp = np.array([[1.0, -1.0, 0.0, 0.0], [-1.0, 1.0, 1.0, 1.0]]); Cq = np.zeros((2, 0))
for eps in [-1e-4, 1e-4]:
    rc = np.array([0.4, 0.4, 0.25, -0.25 + eps])
    print("(B) lambda^T M(rc) = %+.1e  feasible:" % eps, primal_feasible(Cp, Cq, rc),
          " each minor mixed-sign:", [bool((r > 0).any() and (r < 0).any()) for r in Cp])
# Correct sufficient condition: C'_Q of full row rank => (lambda^T C')_Q = 0 forces lambda = 0 => never residual.
rng = np.random.default_rng(3); bad = 0; N = 2000
for _ in range(N):
    k = rng.integers(1, 4); nP = rng.integers(1, 5); nQ = rng.integers(k, k + 3)
    Cp = rng.normal(size=(k, nP)); Cq = rng.normal(size=(k, nQ))
    if np.linalg.matrix_rank(Cq) < k: continue
    rc = rng.normal(size=nP)
    bad += (not primal_feasible(Cp, Cq, rc))
print("full-row-rank C'_Q: infeasible instances =", bad, "of", N)
