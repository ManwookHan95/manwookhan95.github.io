"""U4-ref: independent check of C1(v).  (RR_W): M^W(y) := sum{mu_s W_s : s in F, |a_s| < y W_s} = O(y^{1+eps}).
W = v_l on S_l = {2^l(2i+1)} (bounded gaps 2^{l+1}), v_l(s) = 2^{-s} (up to delta/n), |a_s| = 2^{-(1+b)s} on S_l (support swallowing,
power law; b = 1 critical).  Active set: 2^{-bs} < y.  Compare base entries 2^{-s}, 2^{-s^2-1} and an intermediate 2^{-s^{3/2}}.
Exact big-float arithmetic (mpmath); prints log M / log y at y = 2^{-L}."""
import mpmath as mp
mp.mp.prec = 200
l = 1
S = [2 ** l * (2 * i + 1) for i in range(1, 6000)]
def logM(L, b, base):
    tot = mp.mpf(0)
    for s in S:
        if b * s > L:                      # 2^{-bs} < 2^{-L}
            if base == 'exp':
                e = -2 * s
            elif base == 'mu':
                e = -(s * s + 1) - s
            else:
                e = -int(s ** 1.5) - s
            tot += mp.mpf(2) ** e
    return mp.log(tot, 2)
for b in [0.5, 1.0, 2.0, 3.0]:
    row = []
    for base in ['exp', 's^1.5', 'mu']:
        row.append((base, [float(logM(L, b, base) / (-L)) for L in [100, 200, 400]]))
    print('b = %.1f' % b, row, ' 2/b =', 2 / b)
