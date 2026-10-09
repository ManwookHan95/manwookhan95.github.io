# Lemma 4.3: c -> (P_perp U^T sum c_k u_k, (sum c_k u_k)(zhat)) is injective even when a = u_1 (a in Y)
import numpy as np
rng = np.random.default_rng(3)
n, d, k = 50, 10, 6
U = rng.standard_normal((n, d)) * (0.6 ** (np.arange(n)/5))[:, None]
qs = lambda x: np.abs(x).sum() + np.linalg.norm(U.T @ x)
us = [rng.standard_normal(n) * 0.8 ** np.arange(n) for _ in range(k)]
us = [u / qs(u) for u in us]
a = us[0].copy()                       # a in Y: a is one of the carrier vectors
nu = np.linalg.norm(U.T @ a); e = U.T @ a / nu
zhat = np.sign(a) + U @ e
P = np.eye(d) - np.outer(e, e)
A_only_hilbert = np.column_stack([P @ U.T @ u for u in us])            # map used in the note (needs a in c_00)
A_full = np.vstack([A_only_hilbert, np.array([[u @ zhat for u in us]])])  # with the first-order coordinate
print("rank of Hilbert-only map:", np.linalg.matrix_rank(A_only_hilbert, 1e-10), "of", k, " (kernel contains the a-direction)")
print("rank with first-order term:", np.linalg.matrix_rank(A_full, 1e-10), "of", k)
print("smallest singular value with first-order term:", np.linalg.svd(A_full, compute_uv=False)[-1])
