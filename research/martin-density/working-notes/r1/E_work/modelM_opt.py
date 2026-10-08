import numpy as np
from modelM import solve_scale, profile_f

def nelder_mead(fun, x0, step=0.3, iters=2000, tol=1e-9):
    n = len(x0)
    pts = [np.array(x0, float)]
    for i in range(n):
        p = np.array(x0, float); p[i] += step; pts.append(p)
    vals = [fun(p) for p in pts]
    for it in range(iters):
        order = np.argsort(vals); pts = [pts[i] for i in order]; vals = [vals[i] for i in order]
        if abs(vals[-1]-vals[0]) < tol: break
        cen = np.mean(pts[:-1], axis=0)
        xr = cen + (cen - pts[-1]); fr = fun(xr)
        if fr < vals[0]:
            xe = cen + 2*(cen-pts[-1]); fe = fun(xe)
            if fe < fr: pts[-1], vals[-1] = xe, fe
            else: pts[-1], vals[-1] = xr, fr
        elif fr < vals[-2]:
            pts[-1], vals[-1] = xr, fr
        else:
            xc = cen + 0.5*(pts[-1]-cen); fc = fun(xc)
            if fc < vals[-1]: pts[-1], vals[-1] = xc, fc
            else:
                for i in range(1, n+1):
                    pts[i] = pts[0] + 0.5*(pts[i]-pts[0]); vals[i] = fun(pts[i])
    i = int(np.argmin(vals)); return pts[i], vals[i]

def sup_profile_fprime(xfree, r, A, B, M, taus, J, imin=-40):
    # xfree has J-1 entries; last frozen coordinate fixed by sum = 1
    xfr = np.append(xfree, 1.0 - np.sum(xfree))
    idx = np.arange(imin, 1); lam = r**idx.astype(float)
    eta = np.zeros_like(lam); eta[-J:] = lam[-J:]*xfr
    avail = np.ones_like(lam, dtype=bool)
    best = 0.0
    for t in taus:
        v = solve_scale(t, lam, eta, avail, 1.0, A, B, M, iters=80)[0]
        best = max(best, v)
    return best

if __name__ == "__main__":
    r = 0.5; M = 0.5
    taus = np.exp(np.linspace(np.log(r**6), np.log(r**-22), 140))
    for (A, B) in [(1.0, 0.5), (4.0, 0.5), (0.25, 0.5), (1.0, 0.1)]:
        tf, vf = profile_f(r, 1.0, A, B, M)
        gf = vf.max()
        res = []
        for J in [1, 2, 3, 5]:
            if J == 1:
                v = sup_profile_fprime(np.array([]), r, A, B, M, taus, 1)
                res.append((J, v)); continue
            x0 = np.full(J-1, 1.0/J)
            xb, vb = nelder_mead(lambda z: sup_profile_fprime(z, r, A, B, M, taus, J), x0, step=0.2, iters=400)
            res.append((J, vb, np.round(np.append(xb, 1-xb.sum()), 3)))
        print(f"A={A} B={B}: sup P_f={gf:.4f}")
        for rr in res:
            print("   J=", rr[0], " sup P_f' =", round(rr[1], 4), " ratio R =", round(rr[1]/gf, 4), rr[2] if len(rr) > 2 else "")
