"""K1 sanity check of the deep assignment (Z5-ref Claim 3.1) with trace slack tr_j, as used in Proposition K1.A (part 1.5).

Per coordinate j of F (sign s, cushion |a| > 0, scale t):
  flip bounds of the decomposition:  s*B+ >= -|a|/t - fp,   s*B- <= |a|/t + fm,   fp, fm >= 0
  data switching X (coarse part) with NO deep set:  s*X >= -2A - tr,  A := 2|a|/t,  tr >= 0
  Delta B := B+ - B-, E := |Delta B - X|
  x := s B+, y := s (B+ - X), sigma := point of [y - A - tr, x + A] closest to 0, b1 := B+ - s*sigma
Claims: (i) |B+ - b1| <= fp + fm + E;  (ii) s*b1 >= -A;  (iii) s*(b1 - X) <= A + tr.
"""
import numpy as np
rng = np.random.default_rng(7)
N = 400000
worst = [-np.inf]*3
for _ in range(N // 1000):
    s = rng.choice([-1.0, 1.0], size=1000)
    a = np.abs(rng.exponential(1.0, size=1000)) * 10.0**rng.uniform(-6, 0, size=1000)
    t = 10.0**rng.uniform(-4, 0, size=1000)
    A = 2*a/t
    fp = rng.exponential(1.0, size=1000) * 10.0**rng.uniform(-3, 1, size=1000) * rng.integers(0, 2, size=1000)
    fm = rng.exponential(1.0, size=1000) * 10.0**rng.uniform(-3, 1, size=1000) * rng.integers(0, 2, size=1000)
    tr = rng.exponential(1.0, size=1000) * 10.0**rng.uniform(-3, 1, size=1000) * rng.integers(0, 2, size=1000)
    # sample s*B+ and s*B- consistent with the flip bounds
    sBp = -a/t - fp + rng.exponential(1.0, size=1000) * 10.0**rng.uniform(-2, 3, size=1000)
    sBm = a/t + fm - rng.exponential(1.0, size=1000) * 10.0**rng.uniform(-2, 3, size=1000)
    Bp, Bm = s*sBp, s*sBm
    dB = Bp - Bm
    # data switching: close to dB but with arbitrary error, subject to s*X >= -2A - tr
    X = dB + rng.normal(size=1000) * 10.0**rng.uniform(-3, 2, size=1000)
    sX = s*X
    sX = np.maximum(sX, -2*A - tr)          # enforce "no deep set"
    X = s*sX
    E = np.abs(dB - X)
    x = s*Bp; y = s*(Bp - X)
    lo, hi = y - A - tr, x + A
    assert np.all(lo <= hi + 1e-12)
    sigma = np.clip(0.0, lo, hi)
    b1 = Bp - s*sigma
    c1 = np.abs(Bp - b1) - (fp + fm + E)
    c2 = -A - s*b1
    c3 = s*(b1 - X) - (A + tr)
    for i, c in enumerate((c1, c2, c3)):
        worst[i] = max(worst[i], float(np.max(c / (1 + np.abs(Bp) + np.abs(X)))))
print("max normalized violations of (i), (ii), (iii) over", N, "instances:", ["%.2e" % w for w in worst])
