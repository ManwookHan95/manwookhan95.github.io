# Finite-model sanity check of P2 Theorem 2.1 (engineered recovery of d-neutral two-piece mates).
# Model: P1-referee's finite model of P1's example (refP1/model.py): base coordinate 0 (supp a), contacts 1..nK (z=1),
# free coordinates (z=0); one block, special block coordinate 1 with u(zhat)=0 (w(1)=0).
import sys, numpy as np
sys.path.insert(0, '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r2/refP1')
from model import build, first_row, pstar, qstar

def s(t): return np.sqrt(1+t*t)

def run(seed, rho=0.9, Nw=5, s1=0.02, nFar=0, Ncut=None, steer=True, verbose=False):
    M = build(seed=seed, nK=12, nJ=10, K=7)
    n, nK, sig, a, z, zhat, u = M['n'], M['nK'], M['sig'], M['a'], M['z'], M['zhat'], M['u']
    lam = M['lam']; Phi = M['Phi']
    f, w, _ = first_row(M, zhat)
    assert abs(w[1]) < 1e-6, w
    rng = np.random.default_rng(100+seed)
    K1 = np.arange(1, 1+nK)
    th = 0.15*rng.uniform(0, 1, nK)          # theta(g) on contacts: non-constant split
    g = np.zeros(n); g[K1] = th*u[K1]
    g[0] = -(g @ zhat)/zhat[0]
    # mate check at f (finite model)
    ts = np.concatenate([-np.geomspace(1e-3, 20, 25), np.geomspace(1e-3, 20, 25)])
    viol_f = max(pstar(M, f + t*g) - s(t) for t in ts)
    mup, mum = th.min(), th.max(); theta = 0.5
    v = (mum - mup)*u                         # transfer v = b+ - b- = R*(omega- - omega+) (lambda_1 omega = mu)
    bth = g - (mup + theta*(mum - mup))*u     # b_theta = g - mu_theta u
    # construction
    Ncut = nK if Ncut is None else Ncut       # contacts beyond Ncut get z' = 0 (finite stand-in for N'')
    win = np.arange(1, 1+Nw); far = np.arange(1+Nw, 1+Nw+nFar)
    jfar, jstar = nK-1, nK          # far contact (full flip + negative mass), last contact (partial move, "beyond N''")
    def approx(phi):
        # phi >= 0: raise mass phi at contact 1; -1 <= phi < 0: partial pull z'_{jstar} = 1 + 2 phi;
        # -2 <= phi < -1: jfar fully flipped (with negative mass) and partial pull at jstar with 1 + 2(phi+1)
        app = a.copy()
        for j in win: app[j] += 4*rho*s1*abs(bth[j])          # window masses (z_j = 1)
        zp = z.copy()
        if phi >= 0: app[1] += phi
        elif phi >= -1: zp[jstar] = 1 + 2*phi
        else:
            zp[jfar] = -1; app[jfar] -= 4*rho*1.0*abs(v[jfar]); zp[jstar] = 1 + 2*(phi+1)
        ap = app/qstar(app, sig)
        ep = sig*ap; ep = ep/np.linalg.norm(ep)
        xh = zp + sig*ep
        return ap, xh
    if steer:
        lo, hi = -2.0, 2.0
        for _ in range(80):
            mid = 0.5*(lo+hi); _, xh = approx(mid)
            if u @ xh < 0: lo = mid
            else: hi = mid
        mu = 0.5*(lo+hi)
    else:
        mu = 0.0
    ap, xh = approx(mu)
    assert abs(qstar(ap, sig) - 1) < 1e-12 and abs(ap @ xh - 1) < 1e-9
    fp, wp, _ = first_row(M, xh)
    Cp = np.linalg.norm(Phi*wp)
    om_th = np.zeros(M['K']); om_th[1] = (mup + theta*(mum-mup))/lam[1]
    dp = (Phi**2*wp) @ om_th / Cp
    gpp = np.zeros(n); gpp[:1+Nw] = bth[:1+Nw]; gpp[0] = bth[0]
    gpp = gpp + (lam*(om_th - dp*wp)) @ M['Us']
    c = gpp @ xh
    gp = rho*(gpp - c*ap)
    viol = max(pstar(M, fp + t*gp) - s(t) for t in ts)
    small = [ (pstar(M, fp + t*gp) - 1)/t**2 for t in [-0.03, -0.01, 0.01, 0.03]]
    if verbose: print(seed, 'u(xhat\')=%.2e mu=%.3e dp=%.2e |f\'-f|=%.3f |g\'-rho g|=%.3f' % (u@xh, mu, dp, np.abs(fp-f).sum(), np.abs(gp-rho*g).sum()))
    return viol_f, viol, small, u @ xh

if __name__ == '__main__':
    for seed in range(6):
        vf, vs, sm, ux = run(seed, steer=True, verbose=True)
        vf2, vn, sm2, ux2 = run(seed, steer=False)
        print('seed %d: g mate at f: max(p*-s)=%.1e | steered: max(p*-s)=%.1e, (p*-1)/t^2 at t=-.03,-.01,.01,.03: %s | unsteered u(x)=%.2e: max(p*-s)=%.1e, small-t ratios %s'
              % (seed, vf, vs, np.round(sm, 3), ux2, vn, np.round(sm2, 2)))
