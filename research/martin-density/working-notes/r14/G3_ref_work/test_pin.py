"""Referee test (G3 Cor 2.11 sharpened; Interpretation (b)): which cushions relieve the pinning of a pair of strict
non-peaks in an unshifted block?

Pair l+ (eps=+1), l- (eps=-1) sharing ONE coordinate j; private NEAR coordinates of the data sign (aligned for the data
direction), private FAR coordinates of the anti sign with small mass (deep-swallowed type: far mass << near mass).
Variants:
  (i)   j contact,       near = THIN data-sign support (a = 1e-3)      -> data-direction switching pinned at all t (claim)
  (ii)  j contact,       near = contacts                                -> pinned
  (iii) j THIN support a_j = 1e-3 (sign z_j), near = contacts           -> relieved below the shared-cushion scale
  (iv)  j FREE (z_j = 0.3), near = THIN support                          -> pinned (free shared coordinate is no escape)
For each: max gamma'_+ (data direction) and max (-gamma'_+) (anti-data direction) at several t.
"""
import numpy as np, warnings
warnings.filterwarnings('ignore')
from refmodel import MRow, qstar

n = 14
J, NP, FP, NM, FM, P1, P2, S0, C1, C2, C3 = range(11)
mu = 0.3 * 0.7 ** np.arange(n)


def build(variant, cj=(-0.24, 0.36), far=1e-4):
    a = np.zeros(n); z = np.zeros(n)
    a[S0] = 0.6; z[S0] = 1
    z[P1], z[P2] = 1, -1
    z[C1], z[C2], z[C3] = 1, -1, 1
    z[11:] = [0.2, -0.3, 0.1]
    # pair coordinates
    z[NP], z[FP] = 1, 1          # l+: u(NP) > 0 aligned, u(FP) < 0 anti-aligned
    z[NM], z[FM] = -1, -1        # l-: u(NM) > 0 -> z u < 0 -> aligned for eps=-1; u(FM) < 0 -> anti-aligned
    if variant in ('i', 'iv'):
        a[NP], a[NM] = 1e-3, -1e-3
    if variant in ('i', 'ii'):
        z[J] = 1
    elif variant == 'iii':
        z[J] = 1; a[J] = 1e-3
    elif variant == 'iv':
        z[J] = 0.3
    K = 5
    U = np.zeros((K, n))
    U[0, J], U[0, NP], U[0, FP] = cj[0], 0.3, -far
    U[1, J], U[1, NM], U[1, FM] = cj[1], 0.3, -far
    U[2, P1], U[2, P2], U[2, S0] = 0.7, 0.2, 0.6   # peak carrier with private contacts of both orientations
    U[3, C1], U[3, C2], U[3, S0] = 0.8, 0.1, 0.4
    U[4, C3], U[4, C2], U[4, 11] = 0.8, 0.1, 0.3
    for k in range(K):
        U[k] /= qstar(U[k], mu)
    Phi = np.array([0.4, 0.4, 0.15, 0.15, 0.3])
    return MRow(a, z, [U], [Phi], mu, lam_scale=[1.0])


def info(row):
    w = row.ws[0]; M = np.abs(w).max()
    P = [k for k in range(len(w)) if abs(w[k]) >= M - 1e-6]
    uz = row.Us[0] @ row.zhat
    eps = np.array([1, -1])
    val = eps * uz[:2]
    return P, val, w


def maxgam(row, t, k, sgn):
    lam = row.lams[0]
    def obj(V):
        return sgn * lam[k] * ((row.ws[0][k] - V['Wm'][0][k]) / t - (V['Wp'][0][k] - row.ws[0][k]) / t)
    d = row.decomp(t, obj)
    return d['val'], d['status']


if __name__ == '__main__':
    ts = [0.1, 0.03, 0.01, 0.003]
    for var in ['ii', 'i', 'iii', 'iv']:
        row = build(var)
        P, val, w = info(row)
        print(f"\n== variant ({var})  peaks={P}  val(oriented)={np.round(val, 4)}  w={np.round(w, 4)}  q0={row.q0:.3f}"
              f"  p*(f)={row.pstar(row.f):.7f}")
        for t in ts:
            gp, s1 = maxgam(row, t, 0, +1)
            gm, s2 = maxgam(row, t, 0, -1)
            print(f"   t={t:6.3f}  max gamma'_+ = {gp:8.4f} (/t {gp/t:8.2f}) [{s1}]   max -gamma'_+ = {gm:8.4f} (/t {gm/t:8.2f}) [{s2}]")
