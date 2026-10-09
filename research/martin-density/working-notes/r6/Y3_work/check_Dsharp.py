# Lemma 1.8(b),(c): D#(t) = sup{D : D m(tD/(4C_Q)) <= t/q0 + 32 t^2}, m(y) = sum{v(s): rho(s) < y}
# model: v(s) = c0 2^{-s} on S = {1,2,...}, |a_s| = 2^{-(1+b)s}, rho(s) = |a_s|/v(s) = 2^{-b s}/c0  (monotone: C_Q = 1)
import numpy as np
c0, q0 = 0.3, 0.5
S = np.arange(1, 3000)
def m(y, b):
    rho = 2.0**(-b*S)/c0
    return (c0*2.0**(-S.astype(float)))[rho < y].sum()
def Dsharp(t, b):
    lo, hi = 0.0, 1e6
    rhs = t/q0 + 32*t*t
    if hi*m(t*hi/4, b) <= rhs: return np.inf
    for _ in range(200):
        mid = (lo+hi)/2
        if mid*m(t*mid/4, b) <= rhs: lo = mid
        else: hi = mid
    return lo
for b in [0.5, 1.0, 1.5, 2.0, 3.0]:
    vals = [(t, Dsharp(t, b)) for t in [1e-3, 1e-5, 1e-7, 1e-9, 1e-11]]
    pred = (b-1)/(b+1)
    print(f"b={b}: " + "  ".join(f"t={t:.0e}:D#={D:.3g}" for t, D in vals), f"  predicted exponent {pred:+.3f}",
          " fitted:", f"{np.polyfit(np.log([v[0] for v in vals]), np.log([v[1] for v in vals]), 1)[0]:+.3f}")
