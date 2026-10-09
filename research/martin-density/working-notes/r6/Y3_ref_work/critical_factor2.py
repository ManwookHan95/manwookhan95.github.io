# Critical support swallowing, model of Z5 7.1 / Y3 3.5: S = {1,2,...} (gaps 1), v(s) = c0 2^{-s}, |a_s| = 2^{-(1+b)s}.
# At scale t a decomposition with constrained switching D (s Delta B = -D v on S) pays, at minimum, the flip excess
#    Fdec(t) = sum_s 2 (t D v(s) - 2|a_s|)_+     (cushion |a|/t of BOTH sides used; all flips on one side)
# Fixed data built at scale t by deep assignment (R1): on the deep set {D v > 4|a|/t}: (s b^-)_+ = D v - 2|a|/t,
# elsewhere (s b^-)_+ <= 3|a|/t (no flips for r <= t/3). At scale r the data pay
#    Fdata(r) = sum_{deep} 2 ( r (D v - 2|a|/t) - |a| )_+ .
# Symmetric split theta on the deep set: each side carries theta D v resp. (1-theta) D v.
import numpy as np
c0, D = 0.3, 1.0
S = np.arange(1, 400).astype(float)
v = c0 * 2.0**(-S)
def run(b):
    a = 2.0**(-(1+b)*S)
    out = []
    for t in [1e-4, 3e-6, 1e-7]:
        Fdec = np.sum(2*np.maximum(t*D*v - 2*a, 0))
        deep = D*v > 4*a/t
        beta = np.where(deep, D*v - 2*a/t, 0.0)
        ratios = []
        for r in t * 2.0**(-np.arange(2, 40)):
            Fdata = np.sum(2*np.maximum(r*beta - a, 0))
            ratios.append((Fdata/r**2) / (Fdec/t**2) if Fdec > 0 else np.nan)
        out.append((t, np.nanmin(ratios), np.nanmax(ratios)))
    return out
for b in [0.5, 1.0, 1.5]:
    for t, lo, hi in run(b):
        print(f"b={b} t={t:.0e}: [Fdata(r)/r^2]/[Fdec(t)/t^2] over r = t/4 ... t/2^39 : min {lo:.3f}  max {hi:.3f}")
# exact self-similarity at b = 1: m(2y) = 2 m(y)
b = 1.0; a = 2.0**(-2*S)
def m(y): return v[a < y*v].sum()
for y in [1e-3, 3e-4, 1e-5]:
    print(f"b=1: m(2y)/m(y) at y={y:.0e}: {m(2*y)/m(y):.6f}")
