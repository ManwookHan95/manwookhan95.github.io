"""Referee test: a strict FR resonance WITH an escape.  Pair l+ (eps=+1), l- (eps=-1) of strict non-peaks of an unshifted
block sharing a FREE target j (z_j = 0.3, room 0.7; strict FR row) and a shared SUPPORT target s (thick a_s = 0.3, or thin
a_s = 1e-3); private near coordinates = contacts of the data sign, far = contacts of mass 1e-4.  The FR minor
M = u_+(j) u_-(zhat) - u_-(j) u_+(zhat) is tuned by d_- = u_-(s).
Predictions: shared THICK s: order-one switching iff M ~ 0 (two-regime in |M|, Cor CL.2: |gamma||M| <~ t/(q0 eta_j));
shared THIN s: the same below the shared-cushion scale only; without the shared s (control): pinned for every M.
"""
import numpy as np, warnings
warnings.filterwarnings('ignore')
from scipy.optimize import brentq
from refmodel import MRow, qstar

n = 14
J, S, NP, FP, NM, FM, P1, P2, S0, C1, C2, C3 = range(12)
mu = 0.3 * 0.7 ** np.arange(n)


def build(dm, a_s=0.3, shared=True):
    a = np.zeros(n); z = np.zeros(n)
    a[S0] = 0.6; z[S0] = 1
    if shared:
        a[S] = a_s; z[S] = 1
    if shared == 'contact':
        a[S] = 0.0; z[S] = 1
    z[J] = 0.3
    z[NP], z[FP], z[NM], z[FM] = 1, 1, -1, -1
    z[P1], z[P2] = 1, -1
    z[C1], z[C2], z[C3] = 1, -1, 1
    z[12:] = [0.2, -0.3]
    K = 5
    U = np.zeros((K, n))
    U[0, J], U[0, NP], U[0, FP] = 0.3, 0.3, -1e-4
    U[1, J], U[1, NM], U[1, FM] = 0.3, 0.3, -1e-4
    if shared:
        U[0, S], U[1, S] = -0.2, dm
    else:
        U[0, NP] += -0.2          # same values without a shared support coordinate
        U[1, NM] += -dm
    U[2, P1], U[2, P2], U[2, S0] = 0.7, 0.2, 0.9
    U[3, C1], U[3, C2], U[3, S0] = 0.8, 0.1, 0.6
    U[4, C3], U[4, C2], U[4, 12] = 0.8, 0.1, 0.3
    for k in range(K):
        U[k] /= qstar(U[k], mu)
    Phi = np.array([0.45, 0.45, 0.12, 0.12, 0.3])
    return MRow(a, z, [U], [Phi], mu, lam_scale=[1.0])


def frminor(row):
    U = row.Us[0]; uz = U @ row.zhat
    return U[0, J] * uz[1] - U[1, J] * uz[0], uz[:2]


def maxgam(row, t):
    lam = row.lams[0]
    def obj(V):
        return lam[0] * ((row.ws[0][0] - V['Wm'][0][0]) / t - (V['Wp'][0][0] - row.ws[0][0]) / t)
    try:
        d = row.decomp(t, obj)
        return d['val'], d['status']
    except Exception:
        return float('nan'), 'fail'


if __name__ == '__main__':
    ts = [0.1, 0.03, 0.01]
    for label, a_s, shared in [('shared CONTACT s (control)', 0.0, 'contact')]:
        f0 = lambda dm: frminor(build(dm, a_s, shared))[0]
        dm0 = brentq(f0, 0.0, 3.0, xtol=1e-13)
        for Mt in [0.0, 1e-3, 1e-2]:
            dm = dm0 if Mt == 0 else brentq(lambda d: f0(d) - Mt, dm0 - 1.0, dm0 + 1.0, xtol=1e-13)
            row = build(dm, a_s, shared)
            M, uz = frminor(row)
            w = row.ws[0]; Mx = np.abs(w).max()
            P = [k for k in range(len(w)) if abs(w[k]) >= Mx - 1e-6]
            out = []
            for t in ts:
                g, st = maxgam(row, t)
                out.append(f"t={t:5.2f}: {g:7.4f} ({st[:4]})")
            print(f"[{label}] M={M: .2e} u(zhat)={np.round(uz, 3)} peaks={P}  max gamma'_+: " + "  ".join(out), flush=True)
