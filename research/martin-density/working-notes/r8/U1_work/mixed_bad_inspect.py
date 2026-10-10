"""Re-run mixed_fixedpoint_check.py's instance stream, stop at the first instance with exact completions but no GOOD one,
and list ALL its exact completions (lexicographic model) with the carriers' values."""
import itertools, numpy as np
from scipy.optimize import linprog
import importlib.util, sys
spec = importlib.util.spec_from_file_location('mfc', 'mixed_fixedpoint_check.py')
src = open('mixed_fixedpoint_check.py').read().split("\nK = 7")[0]
ns = {}
exec(compile(src, 'mfc_head', 'exec'), ns)
rng = ns['rng']; instance = ns['instance']; completions = ns['completions']; recursion_possible = ns['recursion_possible']
K = 7; thr, eps = 0.004, 0.5
for it in range(150):
    types, U, Y0 = instance(K)
    if not ('N' in types and 'P' in types):
        continue
    recursion_possible(types, U, Y0)
    ex, good = completions(types, U, Y0, thr, eps, need_good=True)
    if ex and not good:
        break
np.set_printoptions(precision=4, suppress=True, linewidth=160)
print('types', types); print('Y0', Y0); print('U'); print(U)
J = U.shape[1]
for s in itertools.product((-1, 0, 1), repeat=K):
    s = np.array(s); zfix = np.full(J, np.nan)
    for j in range(J):
        for l in range(K):
            if U[l, j] != 0 and s[l] != 0:
                csign = s[l] if types[l] == 'N' else -s[l]
                zfix[j] = csign * np.sign(U[l, j]); break
    free = np.isnan(zfix); nf = int(free.sum())
    base = Y0 + U[:, ~free] @ zfix[~free]; A = U[:, free]
    A_ub, b_ub, A_eq, b_eq = [], [], [], []
    for l in range(K):
        if s[l] == 1: A_ub.append(-A[l]); b_ub.append(base[l] - 1e-9)
        elif s[l] == -1: A_ub.append(A[l]); b_ub.append(-base[l] - 1e-9)
        else: A_eq.append(A[l]); b_eq.append(-base[l])
    if nf == 0:
        v = base
        ok = all((s[l] == 1 and v[l] > 0) or (s[l] == -1 and v[l] < 0) or (s[l] == 0 and abs(v[l]) < 1e-12) for l in range(K))
        if ok: print('completion s=', s, 'v=', v, 'z=', zfix)
        continue
    # maximize distance of N-values from band: just report one feasible point and the range of each N-carrier value
    res = linprog(np.zeros(nf), A_ub=np.array(A_ub) if A_ub else None, b_ub=np.array(b_ub) if b_ub else None,
                  A_eq=np.array(A_eq) if A_eq else None, b_eq=np.array(b_eq) if b_eq else None, bounds=[(-1, 1)] * nf, method='highs')
    if res.status == 0:
        z = zfix.copy(); z[free] = res.x
        v = Y0 + U @ z
        rngs = []
        for l in range(K):
            if types[l] == 'N' and s[l] != 0:
                lo = linprog(A[l], A_ub=np.array(A_ub) if A_ub else None, b_ub=np.array(b_ub) if b_ub else None,
                             A_eq=np.array(A_eq) if A_eq else None, b_eq=np.array(b_eq) if b_eq else None, bounds=[(-1, 1)] * nf, method='highs')
                hi = linprog(-A[l], A_ub=np.array(A_ub) if A_ub else None, b_ub=np.array(b_ub) if b_ub else None,
                             A_eq=np.array(A_eq) if A_eq else None, b_eq=np.array(b_eq) if b_eq else None, bounds=[(-1, 1)] * nf, method='highs')
                rngs.append((l, base[l] + lo.fun, base[l] - hi.fun))
        print('completion s=', s, 'free coords', np.nonzero(free)[0], 'v=', v, 'N-value ranges', rngs)
