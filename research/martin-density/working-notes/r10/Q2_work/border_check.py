"""Check of the bordering lemma (Q2 Proposition 3.8) and of the Woodbury determinant of Lemma DC's linearization.

(1) Bordering: for N in R^{n x n} with second-smallest singular value sigma := s_{n-1}(N) > 0, unit left singular vector y0 of
    s_n(N), and a column w:  s_min([N | w]) >= 1 / ( 1/sigma + (1 + ||w||/sigma)/|y0^T w| ).
(2) Lemma DC's linearization with S-mass common mode:  N = I - g h^T - p q^T  has
    det N = (1 - q^T p)(1 - h^T g) - (q^T g)(h^T p)   (so the Sherman-Morrison degeneracy h^T g = 1 alone is not a singularity).
(3) With h^T g = 1 exactly, the block-norm (peak) column w = -pi p restores surjectivity iff h^T p != 0, uniformly in the
    degeneracy, with the bound of (1).
"""
import numpy as np
rng = np.random.default_rng(11)

worst_ratio = np.inf
for trial in range(2000):
    n = rng.integers(2, 9)
    N = rng.standard_normal((n, n))
    # make N nearly singular with a random tiny last singular value
    U, s, Vt = np.linalg.svd(N)
    s[-1] = 10.0 ** rng.uniform(-14, 0) * s[-2]
    N = U @ np.diag(s) @ Vt
    w = rng.standard_normal(n)
    y0 = U[:, -1]
    sig = s[-2]
    bound = 1.0 / (1.0 / sig + (1.0 + np.linalg.norm(w) / sig) / abs(y0 @ w))
    smin = np.linalg.svd(np.column_stack([N, w]), compute_uv=False)[-1]
    worst_ratio = min(worst_ratio, smin / bound)
print("(1) min over trials of s_min([N|w]) / bound  (must be >= 1):", worst_ratio)

worst_det = 0.0
for trial in range(2000):
    n = rng.integers(2, 9)
    g, h, p, q = (rng.standard_normal(n) for _ in range(4))
    N = np.eye(n) - np.outer(g, h) - np.outer(p, q)
    formula = (1 - q @ p) * (1 - h @ g) - (q @ g) * (h @ p)
    worst_det = max(worst_det, abs(np.linalg.det(N) - formula) / (1 + abs(formula)))
print("(2) max relative error of the Woodbury determinant formula:", worst_det)

print("(3) exact Sherman-Morrison degeneracy h^T g = 1, peak column w = -pi p:")
for hp in [1.0, 1e-2, 1e-4, 0.0]:
    n = 6
    g = rng.standard_normal(n); h = rng.standard_normal(n); h /= (h @ g)         # h^T g = 1
    q = rng.standard_normal(n) * 0.1
    p = rng.standard_normal(n); p -= (h @ p) / (h @ h) * h; p += hp * h / (h @ h)  # prescribe h^T p
    N = np.eye(n) - np.outer(g, h) - np.outer(p, q)
    pi = 0.7
    L = np.column_stack([N, -pi * p])
    print(f"   h^T p = {h @ p:+.1e}:  s_min(N) = {np.linalg.svd(N, compute_uv=False)[-1]:.2e},  s_min([N | -pi p]) = "
          f"{np.linalg.svd(L, compute_uv=False)[-1]:.2e}")
