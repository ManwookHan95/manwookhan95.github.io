"""Numerical sanity check of Lemma 2.8 / Corollary 2.9 / Theorem 2.10 (G3 part 2).

Pair l+ (eps=+1), l- (eps=-1) of strict non-peaks sharing the contact j; peak carrier c with private contacts of both
orientations (unshifted block, (P1)); filler carrier.  The anti-aligned coordinate r of l- is a CONTACT, THIN support or
THICK support; its mass is tuned so that the oriented minor D = val_+ w_- + |val_-| w_+ takes a prescribed value.
For each configuration and scale t we compute  max gamma'_+  over g (g(xi)=0) and decompositions of f +- t g
(the quantity bounded in Lemma 2.8) and print it together with gamma'_+/t.
"""
import numpy as np
from scipy.optimize import brentq
from model import Row, qstar

n = 14
J, NP, NM, R, P1, P2, S0, S1 = 0, 1, 2, 3, 4, 5, 6, 7
Q1, Q2, Q3 = 8, 9, 10
mu = 0.4 * 0.7 ** np.arange(n)
SP, TP = 0.15, 0.8
PHI = np.array([0.35, 0.35, 0.15, 0.15, 0.15, 0.5])


def build(r_mass, r_type, a_r=0.0):
    """carriers: 0 = l+ (eps=+1), 1 = l- (eps=-1), 2,3,4 = peaks (2 has private contacts of both orientations), 5 = filler.
    The pair also carries a cancelling pair of THICK support coordinates S0 (+), S1 (-) so that its values are small and
    it consists of strict non-peaks (in the design strict non-peaks have values O(theta Phi_k))."""
    a = np.zeros(n)
    a[S0], a[S1] = 0.35, -0.25
    z = np.zeros(n)
    z[J], z[NP], z[NM], z[R], z[P1], z[P2], z[S0], z[S1] = 1, 1, -1, 1, 1, -1, 1, -1
    z[Q1], z[Q2], z[Q3] = 1, -1, 1
    z[11:] = [0.3, -0.2, 0.1]
    if r_type in ('thin', 'thick'):
        a[R] = a_r
    K = 6
    U = np.zeros((K, n))
    U[0, J], U[0, NP] = 0.4 * SP, 0.3 * SP
    U[0, S0] = U[0, S1] = TP
    U[1, J], U[1, NM], U[1, R] = 0.5 * SP, 0.3 * SP, r_mass * SP
    U[1, S0] = U[1, S1] = TP
    U[2, P1], U[2, P2], U[2, S0] = 0.7, 0.2, 0.1
    U[3, Q1], U[3, Q2] = 0.8, 0.1
    U[4, Q3], U[4, Q2] = 0.8, 0.1
    U[5, S1], U[5, 11:] = 0.2, [0.3, 0.2, 0.2]
    for k in range(K):
        U[k] /= qstar(U[k], mu)
    return Row(a, z, U, PHI, mu)


def Dval(row):
    eps = np.array([1, -1])
    val = eps * (row.U[:2] @ row.zhat)
    w = val - eps * row.U[:2, J] * row.zhat[J]
    return val[0] * w[1] + abs(val[1]) * w[0], val, w


def tune(target_D, r_type, a_r=0.0):
    f = lambda r: Dval(build(r, r_type, a_r))[0] - target_D
    r = brentq(f, 0.0, 6.0, xtol=1e-12)
    return build(r, r_type, a_r), r


if __name__ == '__main__':
    ts = [1e-1, 3e-2, 1e-2, 3e-3, 1e-3]
    cases = [('D>0 robust, r contact (mass 0)', None, 'contact', 0.0, 0.0),
             ('D=0, r CONTACT', 0.0, 'contact', 0.0, None),
             ('D=0, r THIN support a=1e-4', 0.0, 'thin', 1e-4, None),
             ('D=0, r THIN support a=1e-3', 0.0, 'thin', 1e-3, None),
             ('D=0, r THICK support a=0.15', 0.0, 'thick', 0.15, None),
             ('D=-0.001 (right sign), r THICK a=0.15', -0.001, 'thick', 0.15, None),
             ('D=-0.004 (right sign; l- becomes a PEAK), r THICK a=0.15', -0.004, 'thick', 0.15, None)]
    for name, Dt, rtype, a_r, rfix in cases:
        if Dt is None:
            row = build(rfix, rtype, a_r); rr = rfix
        else:
            row, rr = tune(Dt, rtype, a_r)
        D, val, w = Dval(row)
        pk = row.peaks()
        chk = row.pstar(row.f)
        print(f"\n== {name}: r_mass={rr:.4f}  D={D:.3e}  val={val.round(4)}  w={w.round(4)}  peaks={pk}  p*(f)={chk:.8f}")
        for t in ts:
            gmax, st = row.max_switch(t, 0, +1)
            print(f"   t={t:7.1e}  max gamma'_+ = {gmax:10.4e}   /t = {gmax / t:9.3f}   [{st}]")
