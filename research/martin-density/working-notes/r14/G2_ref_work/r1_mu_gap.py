"""R1 (referee): the |mu| bound in G2's refined Theorem ML needs a ROBUST Jacobian of the tiny polynomials.

Restricted linear model of one (U)-block (as in G2's N2): three pinned kind-(iv) rows P (one-sided upward generators e_l,
capacity W/2), the two-sided peak resource +-rt (block scaling, column = current target vector), two tiny HOMOGENEOUS linear
minors J r = 0 with J = [[1,1,1],[1,1+s,1-s]] (all cofactors robust, every 2x2 minor of J is O(s): tiny-but-nonzero
singular value s).  Start row rc with tiny-polynomial values P(rc) = J rc = (0, beta).  Targets: ANY rt on Z = ker J
(full target freedom along the tangent space).  Capped downward margin levers -e_l of capacity cap on every P row.
Exact realizability of b(rt) = kappa (rt - rc) for SOME rt in Z is equivalent (eliminating the bilinear peak term) to
min over omega of max_l (kappa rc_l + omega k_l) <= cap   (k spans ker J).
We compute the minimal capacity c_need by LP and compare with beta (G2's bound would give c_need <= C * beta with C
independent of s, since |mu| <= Des^C/u was claimed and P(rc) <= beta).
"""
import numpy as np
from scipy.optimize import linprog

kappa = 1.0
def c_need(s, beta):
    J = np.array([[1.0, 1.0, 1.0], [1.0, 1.0 + s, 1.0 - s]])
    k = np.cross(J[0], J[1]); k /= np.linalg.norm(k)
    # rc with J rc = (0, beta): least-norm solution plus a generic kernel component
    rc = np.linalg.lstsq(J, np.array([0.0, beta]), rcond=None)[0] + 0.3 * k
    # LP: minimize c subject to kappa rc_l + omega k_l <= c for all l  (variables omega, c)
    A = np.column_stack([k, -np.ones(3)])
    res = linprog([0.0, 1.0], A_ub=A, b_ub=-kappa * rc, bounds=[(None, None), (None, None)], method="highs")
    cneed = res.x[1]
    # certificate bound: y = J^T mu/||J^T mu|| with mu = (-1/s + 2, 1/s): y = (2,3,1)/sqrt(14) >= 0, y.k = 0
    mu = np.array([-1.0 / s + 2.0, 1.0 / s]); y = J.T @ mu; ny = np.linalg.norm(y); y /= ny
    lower = kappa * (mu @ (J @ rc)) / ny / np.sum(y)        # phi_y / sum(y_+)
    dist = np.linalg.norm(np.linalg.pinv(J) @ (J @ rc))       # dist(rc, Z)
    return cneed, lower, dist, np.linalg.svd(J, compute_uv=False)[-1]

print(" s        beta      c_need     cert.lower   c_need/beta   dist(rc,Z)   sigma_min(J)")
for beta in [1e-6]:
    for s in [1e-1, 1e-2, 1e-3, 1e-4]:
        cn, lo, d, sm = c_need(s, beta)
        print("%.0e  %.0e  %.3e  %.3e   %.3e    %.3e    %.3e" % (s, beta, cn, lo, cn / beta, d, sm))
# with a robust Jacobian (rows far from parallel) the needed capacity is O(beta):
J2 = np.array([[1.0, 1.0, 1.0], [1.0, 2.0, 0.5]])
k2 = np.cross(J2[0], J2[1]); k2 /= np.linalg.norm(k2)
rc2 = np.linalg.lstsq(J2, np.array([0.0, 1e-6]), rcond=None)[0] + 0.3 * k2
res = linprog([0.0, 1.0], A_ub=np.column_stack([k2, -np.ones(3)]), b_ub=-kappa * rc2, bounds=[(None, None)] * 2, method="highs")
print("robust J: c_need/beta = %.3f" % (res.x[1] / 1e-6))
