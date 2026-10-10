"""Companion to mixed_fixedpoint_check.py: frequency of FORCED wrong-branch negative carriers and dependence on the band width.
For each mixed instance (same generator) and each exact completion of the lexicographic model, classify every N-carrier with
s != 0 as R (s = sgn of its non-owned value Y_l) or W (s = -sgn Y_l, |Y_l| < own mass).  'forced W': completions exist but every
completion has a W carrier.  Also recompute 'no GOOD completion' for thinner threshold bands thr in {0.004, 0.0004, 0.00004}."""
import itertools, numpy as np
from scipy.optimize import linprog
src = open('mixed_fixedpoint_check.py').read().split("\nK = 7")[0]
ns = {}; exec(compile(src, 'mfc_head', 'exec'), ns)
instance = ns['instance']; completions = ns['completions']

def all_completions(types, U, Y0):
    K, J = U.shape; out = []
    for s in itertools.product((-1, 0, 1), repeat=K):
        s = np.array(s); zfix = np.full(J, np.nan); owner = -np.ones(J, dtype=int)
        for j in range(J):
            for l in range(K):
                if U[l, j] != 0 and s[l] != 0:
                    csign = s[l] if types[l] == 'N' else -s[l]
                    zfix[j] = csign * np.sign(U[l, j]); owner[j] = l; break
        free = np.isnan(zfix); nf = int(free.sum())
        base = Y0 + U[:, ~free] @ zfix[~free]; A = U[:, free]
        A_ub, b_ub, A_eq, b_eq = [], [], [], []
        for l in range(K):
            if s[l] == 1: A_ub.append(-A[l]); b_ub.append(base[l] - 1e-9)
            elif s[l] == -1: A_ub.append(A[l]); b_ub.append(-base[l] - 1e-9)
            else: A_eq.append(A[l]); b_eq.append(-base[l])
        if nf == 0:
            ok = all((s[l] == 1 and base[l] > 0) or (s[l] == -1 and base[l] < 0) or (s[l] == 0 and abs(base[l]) < 1e-12) for l in range(K))
            if not ok: continue
            z = zfix
        else:
            res = linprog(np.zeros(nf), A_ub=np.array(A_ub) if A_ub else None, b_ub=np.array(b_ub) if b_ub else None,
                          A_eq=np.array(A_eq) if A_eq else None, b_eq=np.array(b_eq) if b_eq else None, bounds=[(-1, 1)] * nf, method='highs')
            if res.status != 0: continue
            z = zfix.copy(); z[free] = res.x
        # classify N carriers (W status depends only on owned sets, which are fixed by s; Y_l uses non-owned coords: fixed or free)
        hasW = False
        for l in range(K):
            if types[l] == 'N' and s[l] != 0:
                nonown = [j for j in range(J) if U[l, j] != 0 and owner[j] != l]
                Y = Y0[l] + sum(U[l, j] * z[j] for j in nonown)
                if np.sign(Y) == -s[l]:
                    hasW = True
        out.append((s, hasW))
    return out

rng_state = None
K = 7; counts = dict(mixed=0, exists=0, forcedW=0); nogood = {0.004: 0, 0.0004: 0, 0.00004: 0}
for it in range(150):
    types, U, Y0 = instance(K)
    if not ('N' in types and 'P' in types): continue
    counts['mixed'] += 1
    comps = all_completions(types, U, Y0)
    if comps:
        counts['exists'] += 1
        if all(h for _, h in comps): counts['forcedW'] += 1
        for thr in nogood:
            ex, good = completions(types, U, Y0, thr, 0.5, need_good=True)
            if ex and not good: nogood[thr] += 1
print(counts); print('instances with completions but no GOOD one, by threshold:', nogood)
