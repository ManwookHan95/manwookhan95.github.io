"""K1 referee: checks of the bordered lever systems of K1 2.4-2.5 and of the (P6)-via-(P4) claim of K1 2.2.

Part A (Sys-A, K1 Lemma K1.5(b1)).  J = [I - gt h^T | col_c], col_c = -(1-X) lam_c rt^(m) - h_c gt.
  * with 1 - h^T gt = 0 exactly, the left null vector of the square part is h, and h^T col_c = -[(1-X) lam_c h^T rt^(m) + h_c] (exact
    identity when h^T gt = 1);
  * explicit right inverse: P = b + gt*alpha - col_c*P0 with (1 - h^T gt) alpha + (h^T col_c) P0 = h^T b; bound
    ||P|| <= ||b|| (1 + (||gt|| + ||col_c||) ||h||_1 / beta).
Part B (Sys-DC with a block-norm lever whose resource is an S-mass lever (P4) on the peak).
  Q2 Prop 4.1 handles the column -pi p_{m*}; K1 2.2 asserts that a (P4) lever on the peak, whose column is -pi p_{m*} - h0 gt with h0 = O(Design/u)
  NOT small, is covered "verbatim" by Q2-refa C.3(iv)'s rank-one perturbation argument (which needs h0 ||gt|| K <= 1/2).
  We exhibit exactly degenerate N = I - gt h^T - p q^T with Q2's scalar beta_* = h^T p ROBUST (so the pure column -pi p borders N onto), but
  y^T(-pi p - h0 gt) = 0 for an h0 of moderate size: the (P4)-type bordered system is NOT onto.  So the (P4) block-norm lever needs its own
  bordered scalar  y^T(pi p_{m*} + h0 gt)  (a new rate object), contrary to "verbatim".
"""
import numpy as np
rng = np.random.default_rng(11)

# ---------------- Part A ----------------
worstA_id, worstA_res, worstA_ratio = 0.0, 0.0, 0.0
for trial in range(3000):
    n = int(rng.integers(3, 9))
    h = np.abs(rng.normal(size=n)) * rng.integers(0, 2, size=n)   # h supported on the (P4) set
    if h.sum() == 0:
        h[0] = 1.0
    g0 = rng.normal(size=n)
    gt = g0 / (h @ g0)            # exact degeneracy: h^T gt = 1
    rt = rng.normal(size=n)
    block = rng.integers(0, 2, size=n).astype(bool)   # block m(c)
    rtm = rt * block
    X = rng.uniform(0, 0.25); lam_c = rng.uniform(0.1, 1.0); h_c = rng.normal() * rng.integers(0, 2)
    col = -(1 - X) * lam_c * rtm - h_c * gt
    S = np.eye(n) - np.outer(gt, h)
    # identity check
    lhs = h @ col
    rhs = -((1 - X) * lam_c * (h @ rtm) + h_c)
    worstA_id = max(worstA_id, abs(lhs - rhs))
    beta = abs(h @ col)
    if beta < 1e-3:
        continue
    b = rng.normal(size=n)
    P0 = (h @ b) / (h @ col)          # alpha := 0 branch (since 1 - h^T gt = 0)
    P = b - col * P0
    res = np.linalg.norm(S @ P + col * P0 - b, np.inf)
    worstA_res = max(worstA_res, res)
    bound = np.abs(b).max() * (1 + (np.abs(gt).max() + np.abs(col).max()) * np.abs(h).sum() / beta)
    worstA_ratio = max(worstA_ratio, (np.abs(P).max() + abs(P0)) / (bound * (1 + 1 / 1)))
print("Part A: max |h^T col - (-(1-X)lam h^T rt - h_c)| =", f"{worstA_id:.2e}",
      "; max residual of explicit right inverse =", f"{worstA_res:.2e}",
      "; max (|P|+|P0|)/(2*bound) =", f"{worstA_ratio:.3f}")

# ---------------- Part B ----------------
count, found, worst_q2 = 0, 0, []
for trial in range(4000):
    n = int(rng.integers(3, 8))
    p = rng.normal(size=n)
    q = rng.normal(size=n) * 0.2
    if q @ p > 0.4:
        continue
    h = rng.normal(size=n)
    A = np.eye(n) - np.outer(p, q)
    g0 = rng.normal(size=n)
    c = h @ np.linalg.solve(A, g0)
    if abs(c) < 0.3:
        continue
    gt = g0 / c
    N = A - np.outer(gt, h)
    u_, s_, vt_ = np.linalg.svd(N.T)
    y = vt_[-1]                       # left null vector of N
    if s_[-1] > 1e-10:
        continue
    pi = rng.uniform(0.2, 1.0)
    # Q2's pure block-norm column -pi p: onto iff y^T p != 0
    ytp = y @ p
    ytg = y @ gt
    if abs(ytp) < 0.05 or abs(ytg) < 0.05:
        continue
    count += 1
    # S-mass (P4) peak lever: column -pi p - h0 gt; it fails exactly for h0* = -pi y^T p / y^T gt
    h0_star = -pi * ytp / ytg
    col2 = -pi * p - h0_star * gt
    s_bord = np.linalg.svd(np.hstack([N, col2[:, None]]), compute_uv=False)[-1]
    s_bord_pure = np.linalg.svd(np.hstack([N, (-pi * p)[:, None]]), compute_uv=False)[-1]
    if s_bord < 1e-10 and s_bord_pure > 1e-3:
        found += 1
        worst_q2.append((abs(h0_star), s_bord_pure, abs(h @ p)))
worst_q2 = np.array(worst_q2)
print(f"Part B: {count} exactly degenerate one-block systems with robust y^T p; in {found} of them the (P4)-type column "
      f"-pi p - h0 gt with h0 = -pi y^T p / y^T gt makes [N | column] NOT onto (s_min < 1e-10) although [N | -pi p] has s_min >= 1e-3.")
print("   median |h0*| = %.3f, 10%%-quantile |h0*| = %.3f, 90%%-quantile |h0*| = %.3f;  min s_min of the pure bordering = %.3e" %
      (np.median(worst_q2[:, 0]), np.quantile(worst_q2[:, 0], 0.1), np.quantile(worst_q2[:, 0], 0.9), worst_q2[:, 1].min()))
print("   (|h0*| is O(1): within the range Design/u of thick S-mass common modes, so no smallness condition excludes it.)")
