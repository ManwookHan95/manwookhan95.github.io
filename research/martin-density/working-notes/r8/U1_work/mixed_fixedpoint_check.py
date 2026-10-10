"""Exploration of MIXED activity classes (U1 part 5): exact fine completions in a lexicographic toy model.

Model (limit of super-decreasing weights): carriers l = 0..K-1 in stage order, type N (negative block, coefficient sign +s_l)
or P (positive block, coefficient sign -s_l), where s_l in {-1, 0, +1} is the sign of w(l) (0 = zero value).  At a coordinate j
the sign of V_j is fixed by the FIRST carrier meeting j with s != 0 (dominance); if no such carrier meets j, V_j = 0 and z_j is
free in [-1, 1].  Exact completion (= admissibility of V): z_j = sgn V_j at every j met by a nonzero carrier, and for every
carrier: sgn(v_l) = s_l, where v_l = Y0_l + sum_j u_l(j) z_j (Y0_l = value of the coarse, already fixed coordinates).
GOOD completion: every N-carrier with s != 0 has |v_l| outside the threshold band (thr(1-eps), thr(1+eps)) (the SC criterion of
Lemma 5.3; zero / tiny values are harmless, values far above threshold are robust peaks).
Each carrier owns two signature coordinates (weights 0.7a, 0.3a, a = own mass), later carriers' targets meet earlier signature
coordinates with O(1) coefficients, and the coarse offsets Y0 are often 0 or small (frustration).
For every instance we enumerate all 3^K sign patterns, solve the LP in the free coordinates, and record whether exact
completions exist, whether a GOOD one exists, and whether the configuration-(i) recursion (all N self-aligned) would be possible."""
import itertools
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(2024)


def instance(K):
    types = rng.choice(['N', 'P'], size=K)
    J = 2 * K
    U = np.zeros((K, J))
    a = 0.05
    for l in range(K):
        U[l, 2 * l] = 0.7 * a
        U[l, 2 * l + 1] = 0.3 * a
        for l2 in range(l):
            if rng.random() < 0.35:
                j = 2 * l2 + rng.integers(0, 2)
                U[l, j] = rng.choice([-1, 1]) * rng.uniform(0.2, 1.0) * 0.1
    Y0 = np.where(rng.random(K) < 0.4, 0.0, rng.uniform(-0.12, 0.12, size=K))
    return types, U, Y0


def completions(types, U, Y0, thr, eps, need_good):
    K, J = U.shape
    found_any = False
    found_good = False
    for s in itertools.product((-1, 0, 1), repeat=K):
        s = np.array(s)
        zfix = np.full(J, np.nan)
        for j in range(J):
            for l in range(K):
                if U[l, j] != 0 and s[l] != 0:
                    csign = s[l] if types[l] == 'N' else -s[l]
                    zfix[j] = csign * np.sign(U[l, j])
                    break
        free = np.isnan(zfix)
        nf = int(free.sum())
        base = Y0 + U[:, ~free] @ zfix[~free]
        A = U[:, free]
        # constraints: s=+1: v >= 1e-9 ; s=-1: v <= -1e-9 ; s=0: v = 0
        A_ub, b_ub, A_eq, b_eq = [], [], [], []
        for l in range(K):
            if s[l] == 1:
                A_ub.append(-A[l]); b_ub.append(base[l] - 1e-9)
            elif s[l] == -1:
                A_ub.append(A[l]); b_ub.append(-base[l] - 1e-9)
            else:
                A_eq.append(A[l]); b_eq.append(-base[l])
        def solve(extra_ub=(), extra_b=()):
            Au = list(A_ub) + list(extra_ub); bu = list(b_ub) + list(extra_b)
            if nf == 0:
                v = base
                ok = all(np.dot(r, np.zeros(0)) <= bb + 1e-12 for r, bb in zip(Au, bu)) if Au else True
                ok = ok and all(abs(base[l]) < 1e-12 for l in range(K) if s[l] == 0)
                return ok
            res = linprog(np.zeros(nf), A_ub=np.array(Au) if Au else None, b_ub=np.array(bu) if bu else None,
                          A_eq=np.array(A_eq) if A_eq else None, b_eq=np.array(b_eq) if b_eq else None,
                          bounds=[(-1, 1)] * nf, method='highs')
            return res.status == 0
        if not solve():
            continue
        found_any = True
        if not need_good:
            return True, None
        # GOOD: for each N-carrier with s != 0 choose |v| >= thr(1+eps) or |v| <= thr(1-eps)
        Nnz = [l for l in range(K) if types[l] == 'N' and s[l] != 0]
        for choice in itertools.product((0, 1), repeat=len(Nnz)):
            eu, eb = [], []
            for l, c in zip(Nnz, choice):
                # s_l v_l = |v_l| = s_l (base + A z)
                if c == 0:   # |v| >= thr(1+eps):  -s(base + Az) <= -thr(1+eps)
                    eu.append(-s[l] * A[l]); eb.append(s[l] * base[l] - thr * (1 + eps))
                else:        # |v| <= thr(1-eps)
                    eu.append(s[l] * A[l]); eb.append(-s[l] * base[l] + thr * (1 - eps))
            if solve(eu, eb):
                found_good = True
                return True, True
    return found_any, (found_good if found_any else None)


def recursion_possible(types, U, Y0):
    """Configuration-(i)-type forward recursion: N self-aligned with sgn Y; P anti-aligned if |Y| > own mass, else FRUSTRATED."""
    K, J = U.shape
    z = np.full(J, np.nan)
    for l in range(K):
        own = [j for j in range(J) if U[l, j] != 0 and np.isnan(z[j])]
        nonown = [j for j in range(J) if U[l, j] != 0 and not np.isnan(z[j])]
        Y = Y0[l] + sum(U[l, j] * z[j] for j in nonown)
        ownmass = sum(abs(U[l, j]) for j in own)
        if types[l] == 'N':
            sg = np.sign(Y) if Y != 0 else 1.0
            for j in own:
                z[j] = sg * np.sign(U[l, j])
        else:
            if abs(Y) <= ownmass:
                return False
            sg = np.sign(Y)
            for j in own:
                z[j] = -sg * np.sign(U[l, j])
    return True


K = 7
thr, eps = 0.004, 0.5
stats = dict(n=0, mixed=0, exists=0, good=0, frustrated=0, exists_but_no_good=0)
bad_examples = []
for it in range(150):
    types, U, Y0 = instance(K)
    if not ('N' in types and 'P' in types):
        continue
    stats['mixed'] += 1
    rec = recursion_possible(types, U, Y0)
    if not rec:
        stats['frustrated'] += 1
    ex, good = completions(types, U, Y0, thr, eps, need_good=True)
    stats['exists'] += int(ex)
    if ex:
        stats['good'] += int(bool(good))
        if not good:
            stats['exists_but_no_good'] += 1
            bad_examples.append((types, U, Y0))
print(stats)
print('instances where exact completions exist but none is GOOD:', len(bad_examples))
