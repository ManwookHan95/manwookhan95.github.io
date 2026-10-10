# cert1: bounds for K on the W-fix region x = R_a^2 in [0, 1 - s/4], s = sigma_rob in (0, 1/12]
import numpy as np
def K(s, x): return (s + np.sqrt(s*s*x + s*(1-x)))/(1-x)
def dKdx(s, x):
    k = K(s, x); a = k - s
    return k*k/(2*(a - k*x))
out = []
for s in [1e-6, 1e-4, 1e-2, 1/12]:
    xs = np.linspace(0, 1 - s/4, 200001)
    kk = K(s, xs); dd = dKdx(s, xs)
    # finite-difference check of dK/dx
    h = 1e-9; fd = (K(s, xs[:-1] + h) - K(s, xs[:-1]))/h
    out.append('s=%.1e: max K=%.4f (formula 4(1+sqrt(5/4-s/4))=%.4f), max dK/dx=%.4e, s*max dK/dx=%.3f, min(a-kx)/s=%.4f, fd rel err=%.1e'
               % (s, kk.max(), 4*(1+np.sqrt(1.25 - s/4)), dd.max(), s*dd.max(), ((kk - s) - kk*xs).min()/s,
                  np.max(np.abs(fd - dd[:-1])/dd[:-1])))
# data region: a + sigma <= ||Phi||_2 + ||Phi||_2^2 with ||Phi||_2^2 <= 4^{-m}/3
for m in [1, 2, 3]:
    ph2 = 4.0**(-m)/3
    out.append('m=%d: ||Phi||_2 + ||Phi||_2^2 <= %.4f' % (m, np.sqrt(ph2) + ph2))
open('wfix_bounds.out', 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
