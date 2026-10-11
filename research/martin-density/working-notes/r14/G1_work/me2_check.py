"""G1 part 5 sanity checks.

(1) Lemma ME2 (single bilinear strict minor, two blocks):
    M(x, y) = x^T D y + E^T x + F^T y + G with design coefficients, x = block-m ratios, y = block-m' ratios.
    If all first cofactors (D y1 + E)_l, (D^T x1 + F)_k are tiny (<= b) and M(x1, y1) is tiny, then the projections
    x#, y# of x1, y1 onto A_x = {D^T x + F = 0}, A_y = {D y + E = 0} satisfy M(x#, y#) = 0 exactly, PROVIDED the constant
    value of M on A_x x A_y (a design number) is 0.  Contrast: if that constant is a tiny NON-design number g', the
    nearest zero of M is at distance ~ sqrt(g') >> b (why the design-number dichotomy matters).
(2) Strict Farkas alternative in a (U)-block, extended by two-sided FR generators (Proposition 5.2 / Corollary 5.3):
    random residual instances of the Example-4.3 type with a FREE common target coordinate j are destroyed by adding one
    FR generator at another shared free target coordinate s with det[u(j); u(s)] != 0.
"""
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(7)


def proj_affine(A, c, x):
    """Euclidean projection of x onto {z : A z + c = 0} (A z + c = 0 assumed consistent)."""
    r = A @ x + c
    return x - np.linalg.pinv(A) @ r


def check_me2(trials=500):
    worst_exact, worst_disp_ratio, worst_contrast = 0.0, 0.0, np.inf
    for _ in range(trials):
        p, q = 3, 3
        # rank-2 design matrix D (so that A_x, A_y are lines), integer entries
        U = rng.integers(-3, 4, size=(p, 2)).astype(float)
        V = rng.integers(-3, 4, size=(2, q)).astype(float)
        D = U @ V
        if np.linalg.matrix_rank(D) < 2:
            continue
        x0 = rng.integers(-2, 3, size=p).astype(float)
        y0 = rng.integers(-2, 3, size=q).astype(float)
        E = -D @ y0          # A_y = {D y + E = 0} contains y0
        F = -D.T @ x0        # A_x = {D^T x + F = 0} contains x0
        G = -(E @ x0)        # the constant value of M on A_x x A_y is E^T x0 + G = 0 (design number 0)
        M = lambda x, y: x @ D @ y + E @ x + F @ y + G
        b = 10.0 ** rng.uniform(-9, -6)
        kx = np.linalg.svd(D.T)[2][-1]; ky = np.linalg.svd(D)[2][-1]       # kernel directions
        x1 = x0 + rng.normal() * kx + b * rng.normal(size=p) / 3
        y1 = y0 + rng.normal() * ky + b * rng.normal(size=q) / 3
        cof_x = D @ y1 + E; cof_y = D.T @ x1 + F
        if max(abs(cof_x).max(), abs(cof_y).max(), abs(M(x1, y1))) > 10 * b:
            continue
        xs = proj_affine(D.T, F, x1); ys = proj_affine(D, E, y1)
        worst_exact = max(worst_exact, abs(M(xs, ys)))
        disp = np.hypot(np.linalg.norm(xs - x1), np.linalg.norm(ys - y1))
        worst_disp_ratio = max(worst_disp_ratio, disp / b)
        # contrast: constant g' (not a design number) of size b on A_x x A_y; distance to {M = 0} near (x1, y1)
        gp = b
        Mc = lambda x, y: M(x, y) + gp
        # cheap estimate of the distance to the zero set along the best bilinear direction: solve min |d| s.t. Mc(x1+dx, y1+dy) = 0
        best = np.inf
        for _ in range(200):
            dx = rng.normal(size=p); dy = rng.normal(size=q)
            # Mc(x1 + s dx, y1 + s dy) = a s^2 + bb s + cc
            a = dx @ D @ dy
            bb = dx @ (D @ y1 + E) + (x1 @ D + F) @ dy
            cc = Mc(x1, y1)
            roots = np.roots([a, bb, cc])
            for r_ in roots:
                if abs(r_.imag) < 1e-14:
                    best = min(best, abs(r_.real) * np.hypot(np.linalg.norm(dx), np.linalg.norm(dy)))
        worst_contrast = min(worst_contrast, best / b)
    return worst_exact, worst_disp_ratio, worst_contrast


def residual_LP(C, rc, P, Q, gens2, gens1):
    """Feasibility of: C (rc + d) = 0 with d = sum_P a_l e_l (a_l >= 0, oriented raises) + sum_Q b_l e_l (free)
    + sum_s c_s g_s (two-sided generators, free) + sum_s e_s h_s (one-sided generators, >= 0).  Returns True if feasible."""
    n = C.shape[1]
    cols, bounds = [], []
    for l in P:
        cols.append(np.eye(n)[l]); bounds.append((0, None))
    for l in Q:
        cols.append(np.eye(n)[l]); bounds.append((None, None))
    for g in gens2:
        cols.append(g); bounds.append((None, None))
    for h in gens1:
        cols.append(h); bounds.append((0, None))
    if not cols:
        return bool(np.allclose(C @ rc, 0))
    Gm = np.array(cols).T
    res = linprog(np.zeros(Gm.shape[1]), A_eq=C @ Gm, b_eq=-C @ rc, bounds=bounds, method="highs")
    return res.status == 0


def check_fr_generators(trials=2000):
    killed, residual_before = 0, 0
    for _ in range(trials):
        # Example-4.3 type: two oriented kind-(iv) ratios, one FREE common target coordinate j
        uj = rng.uniform(0.2, 1.0, size=2) * np.array([1, -1])     # oriented cofactors C' = (u_-(j) ..) both positive below
        C = np.array([[-uj[1], uj[0]]])                              # M = -u_-(j) r_+ + u_+(j) r_-  (oriented sign convention)
        if not (C[0, 0] > 0 and C[0, 1] > 0):
            C = -C
        rc = rng.normal(size=2)
        Mrc = (C @ rc)[0]
        if Mrc <= 0:                                                 # need the wrong sign at the start
            continue
        rc = rc * (1e-6 / Mrc)                                       # M(rc) = +1e-6 (tiny, wrong-signed)
        feas0 = residual_LP(C, rc, P=[0, 1], Q=[], gens2=[uj], gens1=[])   # own FR generator at j only
        if feas0:
            continue
        us = rng.uniform(-1.0, 1.0, size=2)                          # another shared FREE target coordinate s
        if abs(np.linalg.det(np.array([uj, us]))) < 1e-3:            # (nearly parallel target vectors: skipped)
            continue
        residual_before += 1
        feas1 = residual_LP(C, rc, P=[0, 1], Q=[], gens2=[uj, us], gens1=[])
        killed += feas1
    return residual_before, killed


if __name__ == "__main__":
    we, wd, wc = check_me2()
    print("ME2: max |M(x#, y#)| = %.2e ; max displacement / b = %.2f ; contrast (constant g' = b, not design): "
          "min distance to zero set / b = %.1f" % (we, wd, wc))
    rb, k = check_fr_generators()
    print("strict Ex.4.3-type residual instances (own FR generator at j only): %d ; destroyed by one extra generic FR generator: %d"
          % (rb, k))
