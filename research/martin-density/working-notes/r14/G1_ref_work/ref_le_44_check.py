"""(1) Lemma 4.4: a move changing coarse values by c*u_k(j) changes a minor containing (X1)_j and one (X3)_m (inactive
shift, columns = gamma-columns of block m + columns where (X1)_j vanishes) only by the factor (1 - dkappa/kappa) at first
order: dM = -(dkappa/kappa) M  (zero when M = 0).  (2) Same with an extra (X4^0)-type row of block m whose entries depend on
r: the first-order change is then NOT a multiple of M (precision P-44: the lemma needs no other ratio-dependent rows).
(3) Lemma LE (b): consistency + Cramer distance for design systems with integer data (Des ~ max |cofactor|/min nonzero det).
"""
import numpy as np, itertools
rng = np.random.default_rng(3)
# (1)
worst1 = 0; worst2 = 0
for trial in range(2000):
    q = rng.integers(2, 4)          # gamma-columns of block m
    extra = rng.integers(0, 2)      # extra columns where (X1)_j vanishes
    ncol = q + extra
    uj = np.r_[rng.normal(size=q), np.zeros(extra)]           # (X1)_j restricted to M's columns
    r = rng.normal(size=q); kappa = 1 + rng.random()
    others = rng.normal(size=(ncol - 2, ncol))                # other strict rows (FR / single-variable): constant
    def M_of(rr, rows4=None):
        X3 = np.r_[-rr, np.zeros(extra)]
        A = np.vstack([X3, uj, others]) if rows4 is None else np.vstack([X3, uj, rows4(rr)])
        return np.linalg.det(A)
    c = rng.normal(); dk = rng.normal(); h = 1e-7
    dr = (c * uj[:q] - r * dk) / kappa
    dM = (M_of(r + h * dr) - M_of(r - h * dr)) / (2 * h)
    pred = -(dk / kappa) * M_of(r)
    worst1 = max(worst1, abs(dM - pred) / (1 + abs(pred)))
    # (2) replace one 'other' row by an r-dependent inward-type row (X4^0)-like: entries depend on |r_1| R^2
    if ncol - 2 >= 1:
        def rows4(rr):
            R2 = np.sum(rr ** 2)
            row = np.zeros(ncol); row[0] = 1.0; row[min(1, ncol - 1)] += abs(rr[0]) * (1 + R2)
            return np.vstack([row, others[1:]]) if ncol - 2 >= 2 else row[None, :]
        dM2 = (M_of(r + h * dr, rows4) - M_of(r - h * dr, rows4)) / (2 * h)
        pred2 = -(dk / kappa) * M_of(r, rows4)
        worst2 = max(worst2, abs(dM2 - pred2) / (1 + abs(pred2)))
print("Lemma 4.4 (only (X3)_m ratio-dependent): max rel. deviation of dM from -(dk/k)M = %.2e" % worst1)
print("with an extra ratio-dependent (X4^0)-type row: max rel. deviation = %.2e (not a multiple of M)" % worst2)
# (3) Lemma LE (b)
worst = 0; viol = 0
for trial in range(3000):
    k = rng.integers(1, 5); d = rng.integers(2, 6)
    C = rng.integers(-3, 4, size=(k, d)).astype(float)
    if np.linalg.matrix_rank(C) == 0: continue
    rho0 = rng.integers(-3, 4, size=d) / rng.integers(1, 4)
    c = -C @ rho0                                    # consistent design system
    beta = 10 ** rng.uniform(-12, -4)
    r1 = rho0 + rng.normal(size=d)
    # put r1 at residual <= beta: project then perturb within the residual budget
    P = np.linalg.pinv(C)
    r1 = r1 - P @ (C @ r1 + c)
    e = rng.uniform(-beta, beta, size=k)
    r1 = r1 + P @ e
    res = np.max(np.abs(C @ r1 + c))
    if res > beta * (1 + 1e-6): viol += 1
    # Cramer construction
    q = np.linalg.matrix_rank(C)
    found = None
    for B in itertools.combinations(range(k), q):
        for K in itertools.combinations(range(d), q):
            if abs(np.linalg.det(C[np.ix_(B, K)])) > 0.5:
                found = (B, K); break
        if found: break
    B, K = found
    ee = C @ r1 + c
    delta = np.zeros(d); delta[list(K)] = -np.linalg.solve(C[np.ix_(B, K)], ee[list(B)])
    rho = r1 + delta
    worst = max(worst, np.max(np.abs(C @ rho + c)) / beta)
print("Lemma LE(b): residual of Cramer point / beta: max %.2e (exact up to rounding); residual-budget violations: %d" % (worst, viol))
