"""K1 referee: independent EXACT (rational arithmetic) check of the deep assignment with trace slack (K1 1.5 (i)) and of the
contact-split bound on F_low, including boundary cases (interval degenerate to a point, x + A = 0, y - A - tr = 0, s V_c = -2A - tr).

Per coordinate (sign s, A = 2|a|/t, slack tr >= 0), flip bounds: s B+ >= -A/2 - fp, s B- <= A/2 + fm (fp, fm >= 0),
X := V_c with s X >= -2A - tr (Lemma K1.3), E := |Delta B - X|, x := s B+, y := s(B+ - X), sigma := point of [y - A - tr, x + A] closest to 0,
b1 := B+ - s sigma.  Claims: (i) |B+ - b1| <= fp + fm + E; (ii) s b1 >= -A; (iii) s (b1 - X) <= A + tr.
F_low (data-carrying lowered coordinate, s X >= 0): chi := proj_[0,1](s B+/(s X)) (0 if X = 0); claim |B+ - chi X| <= A/2 + fp + fm + E.
"""
from fractions import Fraction as Fr
import random
random.seed(3)

def rnd(lo, hi, den=97):
    return Fr(random.randint(int(lo * den), int(hi * den)), den)

viol = [0, 0, 0, 0]
N = 60000
for it in range(N):
    s = random.choice([1, -1])
    A = rnd(0, 3); tr = rnd(0, 2) * random.randint(0, 1)
    fp = rnd(0, 2) * random.randint(0, 1); fm = rnd(0, 2) * random.randint(0, 1)
    sBp = -A / 2 - fp + rnd(0, 8) * random.randint(0, 1)          # boundary case allowed (s B+ = -A/2 - fp)
    sBm = A / 2 + fm - rnd(0, 8) * random.randint(0, 1)
    Bp, Bm = s * sBp, s * sBm
    dB = Bp - Bm
    mode = random.randint(0, 3)
    if mode == 0:
        sX = -2 * A - tr                                          # extreme allowed anti-sign switching
    elif mode == 1:
        sX = s * dB
        sX = max(sX, -2 * A - tr)
    else:
        sX = max(s * dB + rnd(-5, 5), -2 * A - tr)
    X = s * sX
    E = abs(dB - X)
    x = s * Bp; y = s * (Bp - X)
    lo, hi = y - A - tr, x + A
    assert lo <= hi
    sigma = Fr(0) if lo <= 0 <= hi else (hi if hi < 0 else lo)
    b1 = Bp - s * sigma
    if abs(Bp - b1) > fp + fm + E: viol[0] += 1
    if s * b1 < -A: viol[1] += 1
    if s * (b1 - X) > A + tr: viol[2] += 1
    # F_low claim (only meaningful when s X >= 0)
    if sX >= 0:
        if sX == 0:
            chi = Fr(0)
        else:
            chi = min(max(sBp / sX, Fr(0)), Fr(1))
        if abs(Bp - chi * X) > A / 2 + fp + fm + E: viol[3] += 1
print(f"{N} exact instances: violations of (i), (ii), (iii), F_low bound = {viol}")
