# Finite-model sanity check of N2 Theorem 1 (engineered recovery of an exact two-piece mate, Delta d = 0).
# Uses the referee's finite model of P1's example (refP1/model.py): one block, diagonal U, contacts K' = 1..nK,
# special block vector u = Us[1] with u(zhat) = 0 and supp u = {0} cup K'.
# Construction (finite emulation): window = first NW contacts (masses 4 t |b_theta,j| with sign z_j = +1),
# Far = next nF contacts (z' = -1, negative masses 2 T0 rho |v_j|), middle contacts unchanged, last nT contacts z' = 0
# ("beyond N''"), tuning mass mu at a window contact chosen by bisection so that u(x') = 0 (Delta d' = 0).
import numpy as np, sys, warnings, cvxpy as cp
warnings.filterwarnings("ignore")
sys.path.insert(0, '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r2/refP1')
from model import *

def first_row_a(M, ap, x):
    zeta = Rmap(M, x); w, nrm = block_J(M, zeta)
    return ap + (M['lam'] * w) @ M['Us'], w, nrm

def run(seed, c=0.15, theta=0.5, rho=0.9, t=0.02, T0=0.3, NW=5, nF=2, nT=2):
    M = build(seed, nK=12, nJ=10)
    n, nK, sig, u, zhat, a = M['n'], M['nK'], M['sig'], M['u'], M['zhat'], M['a']
    f, w, _ = first_row(M, zhat)
    rng = np.random.default_rng(200 + seed)
    K1 = np.zeros(n, bool); K1[1:1+nK] = rng.random(nK) < 0.5
    v1 = np.where(K1, c*u, 0.0); beta = v1 @ zhat; g = v1 - beta*a          # two-piece mate g_{K1}
    lam1 = M['lam'][1]
    # representation: b+ = g, omega+ = 0;  b- = g - c u, omega- = (c/lam1) e_1  (Delta d = 0 since w(1) = 0)
    bp, bm = g.copy(), g - c*u; v = bp - bm
    btheta = bp - theta*v
    win = np.arange(1, 1+NW); far = np.array([], int); tail = np.array([1+nK-1]) if USE_TAIL else np.array([], int)
    def build_x(mu, jplus=1, far=None):
        far = FAR if far is None else far
        A = a.copy()
        A[win] += 4*t*np.abs(btheta[win])                                    # window masses, sign z_j = +1
        A[far] -= 2*T0*rho*np.abs(v[far])                                    # far negative masses
        A[jplus] += mu                                                       # tuning mass (z_{j+} = +1)
        ap = A/qstar(A, sig)
        zp = M['z'].copy(); zp[far] = -1.0; zp[tail] = 0.0
        ep = sig*ap; ep = ep/np.linalg.norm(ep)
        return ap, zp + sig*ep
    # choose Far greedily among the finest contacts (excluding the tail) until the pull exceeds the deficit
    FAR = np.array([], int)
    cand = [j for j in range(nK-1, NW, -1) if abs(v[j]) > 0]
    for j in cand:
        if build_x(0.0, far=FAR)[1] @ u <= 0: break
        FAR = np.append(FAR, j)
    # bisection on mu for u(x') = 0
    lo, hi = 0.0, 1e-3
    if build_x(lo)[1] @ u > 0: return None
    while build_x(hi)[1] @ u < 0: hi *= 2
    for _ in range(80):
        mid = 0.5*(lo+hi)
        if build_x(mid)[1] @ u < 0: lo = mid
        else: hi = mid
    mu = 0.5*(lo+hi); ap, xp = build_x(mu)
    fp, wp, _ = first_row_a(M, ap, xp)
    Cp = np.linalg.norm(M['Phi']*wp)
    def dprime(om): return (M['Phi']**2 * wp) @ om / Cp
    om_theta = np.zeros(M['K']); om_theta[1] = theta*c/lam1
    sN = -((btheta*np.isin(np.arange(n), np.concatenate([[0], win]))) @ xp)
    b0 = btheta*np.isin(np.arange(n), np.concatenate([[0], win])) + sN*ap
    gp = b0 + (M['lam']*(om_theta - dprime(om_theta)*wp)) @ M['Us']
    ts = np.concatenate([-np.logspace(-4, 1, 21)[::-1], np.logspace(-4, 1, 21)])
    exc = [pstar(M, fp + tt*rho*gp) - np.sqrt(1+tt*tt) for tt in ts]
    return dict(seed=seed, nFar=len(FAR), mu=mu, u_xp=u@xp, wp1=wp[1], f_dist=np.abs(fp-f).sum(), g_dist=np.abs(gp-g).sum(),
                gp_xp=gp@xp, worst=max(exc), argworst=ts[int(np.argmax(exc))])

for USE_TAIL in [False]:
  print("USE_TAIL", USE_TAIL)
  for seed in range(4):
    r = run(seed, t=0.05)
    print(r if r is None else {k: (float('%.3e' % v) if isinstance(v, (float, np.floating)) else v) for k, v in r.items()})
