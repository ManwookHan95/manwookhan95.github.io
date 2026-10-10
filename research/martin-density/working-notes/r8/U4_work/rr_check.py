"""U4 audit, conflict C1(v): raise room (RR_W): M^W(y) := sum{mu_s W_s : |a_s| < y W_s} = O(y^{1+eps}).
Profile on a signature set with bounded gaps (step G): W_s = v(s) = 2^{-s}, |a_s| = 2^{-(1+b)s} (support swallowing of
power-law type; b = 1 critical).  Compare base mu_s = 2^{-s} (V1's s_j) with mu_s = 2^{-s^2-1} (V3's D^mu).
Everything in log2 to avoid underflow; the local exponent kappa(y) := log M/log y must exceed 1 + eps for (RR)."""
import numpy as np
G = 4
S = np.arange(6, 6 + G * 4000, G).astype(float)
def log2M(log2y, b, base):
    act = S[(-(1 + b) * S) < (log2y - S)]          # |a_s| < y W_s  <=>  -(1+b)s < log2 y - s
    if base == 'exp':
        e = -act - act                              # mu_s W_s = 2^{-s} 2^{-s}
    else:
        e = -(act**2 + 1) - act                     # 2^{-s^2-1} 2^{-s}
    m = e.max()
    return m + np.log2(np.sum(2.0 ** (e - m)))
for b in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]:
    out = []
    for base in ['exp', 'mu']:
        ks = []
        for log2y in [-200.0, -400.0, -800.0]:
            ks.append(log2M(log2y, b, base) / log2y)
        out.append((base, ['%.3f' % k for k in ks]))
    print('b = %.1f:' % b, out, '  predicted exponent for base 2^{-s}: 2/b = %.3f' % (2 / b))
