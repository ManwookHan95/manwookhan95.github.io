"""J2-ref: independent checks of Lemma J2.0 and Lemma J2.1 (frozen block system).
Independent implementation: the TRUE block is computed from the convex program (Martin Lemma A dual norm)
   A = max <w, zeta>  s.t. ||w||_inf + ||Phi w||_2 <= 1,  M = ||w||_inf, C = ||Phi w||_2, theta = A M / C,
cross-checked with a closed-form threshold solve; the FROZEN system is solved as the 2x2 system
   G1: A - A_f(th) = 0,  G2: A^2 - B_f(th) = 0   by Newton from the true point (not by bisection on Psi_f).
Tests: (c) consistency => truth, (d) frozen Lemma K identities and derivative formulas (finite differences, mpmath),
(e) bounds at the BOUNDARY of the hypotheses (6 b Phi_W^2 = Phi_Pf^2, 2 b Phi_W^2 = a), Step (i) of Theorem J2.1:
F(r_0) <= max rho^f_d <= (1+b)(1+6b Phi_W^2/Phi_Pf^2) with psi_d computed with sigma_rob and R_a (active Omega only)."""
import numpy as np
import mpmath as mp
import random
mp.mp.dps = 40
random.seed(7); np.random.seed(7)

def true_threshold(zeta, Phi):
    nu = [abs(z)/p**2 for z, p in zip(zeta, Phi)]
    def Psi(th):
        A = sum(max(abs(z) - th*p**2, 0) for z, p in zip(zeta, Phi))
        B = sum(p**2*min(th, n)**2 for p, n in zip(Phi, nu))
        return A*A - B
    lo, hi = mp.mpf('1e-30'), max(nu)*2
    for _ in range(300):
        mid = (lo+hi)/2
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    th = (lo+hi)/2
    A = sum(max(abs(z) - th*p**2, 0) for z, p in zip(zeta, Phi))
    return th, A

def true_convex(zeta, Phi):
    """independent: maximize <w,zeta> over ||w||_inf + ||Phi w||_2 <= 1 by parametrising M (w = clamp structure solved by
    a 1-d search over M in (0,1) with the inner problem max <w,zeta> s.t. |w_k|<=M, ||Phi w||_2 <= 1-M solved by
    a KKT water-filling: w_k = sgn(zeta_k) min(M, s |zeta_k|/Phi_k^2) with s chosen so that ||Phi w|| = 1 - M)."""
    z = np.array([float(abs(x)) for x in zeta]); P = np.array([float(x) for x in Phi])
    def inner(M):
        C = 1 - M
        # find s >= 0 with sum Phi^2 min(M, s z/Phi^2)^2 = C^2 (if even s=inf gives < C^2 then w = M everywhere)
        full = np.sum(P**2*M**2)
        if full <= C**2: return M*np.sum(z), M, np.sqrt(full)
        lo, hi = 0.0, 1.0
        while np.sum(P**2*np.minimum(M, hi*z/P**2)**2) < C**2: hi *= 2
        for _ in range(200):
            mid = (lo+hi)/2
            if np.sum(P**2*np.minimum(M, mid*z/P**2)**2) < C**2: lo = mid
            else: hi = mid
        w = np.minimum(M, hi*z/P**2)
        return np.dot(w, z), M, C
    # golden-section on M
    a, bb = 1e-9, 1-1e-9
    g = (np.sqrt(5)-1)/2
    c, d = bb - g*(bb-a), a + g*(bb-a)
    for _ in range(200):
        if inner(c)[0] > inner(d)[0]: bb = d
        else: a = c
        c, d = bb - g*(bb-a), a + g*(bb-a)
    A, M, C = inner((a+bb)/2)
    return A, M, C, A*M/C

def frozen(zeta, Phi, Pf, fine, th0, A0):
    """Newton on (A, th) for G1 = A - A_f(th), G2 = A^2 - B_f(th) starting at (A0, th0)."""
    nu = [abs(z)/p**2 for z, p in zip(zeta, Phi)]
    n = len(zeta)
    def Af(th): return sum((abs(zeta[k]) - th*Phi[k]**2) if k in Pf else (max(abs(zeta[k]) - th*Phi[k]**2, 0) if k in fine else 0) for k in range(n))
    def Bf(th): return sum(th**2*Phi[k]**2 if k in Pf else (Phi[k]**2*min(th, nu[k])**2 if k in fine else nu[k]**2*Phi[k]**2) for k in range(n))
    A, th = mp.mpf(A0), mp.mpf(th0)
    for _ in range(60):
        h = th*mp.mpf('1e-25')
        G1, G2 = A - Af(th), A*A - Bf(th)
        d1 = (Af(th+h) - Af(th-h))/(2*h); d2 = (Bf(th+h) - Bf(th-h))/(2*h)
        J = mp.matrix([[1, -d1], [2*A, -d2]])
        dx = mp.lu_solve(J, mp.matrix([-G1, -G2]))
        A += dx[0]; th += dx[1]
    assert Af(th) > 0
    return th, A, nu

def Kfun(sig, R2): return (sig + mp.sqrt(sig**2*R2 + sig*(1 - R2)))/(1 - R2)

def make(nrob, nweak, nnon, nfine, b, wmin=0.02, wmax=0.3, rob=(1.3, 3.0)):
    """block with theta := 1 by construction: choose rho's, solve rho of robust peak 0 from the alpha-mass identity"""
    n = nrob + nweak + nnon + nfine
    Phi = [mp.mpf(random.uniform(wmin, wmax)) for _ in range(nrob+nweak+nnon)] + [mp.mpf(random.uniform(1e-5, 1e-3)) for _ in range(nfine)]
    rho = [None] + [mp.mpf(random.uniform(*rob)) for _ in range(nrob-1)] + \
          [1 + b*mp.mpf(random.uniform(0.0, 1.0)) for _ in range(nweak)] + \
          [mp.mpf(random.uniform(0.0, 0.99)) for _ in range(nnon)] + [mp.mpf(random.uniform(0, 1.5)) for _ in range(nfine)]
    P = list(range(nrob+nweak)) + [k for k in range(nrob+nweak+nnon, n) if rho[k] >= 1]
    PhiP2 = sum(Phi[k]**2 for k in P)
    SQ = sum(rho[k]**2*Phi[k]**2 for k in range(n) if k not in P)
    a = mp.sqrt(PhiP2 + SQ)
    rest = sum((rho[k]-1)*Phi[k]**2 for k in P if k != 0)
    rho[0] = 1 + (a - rest)/Phi[0]**2
    if rho[0] < rob[0]: return None
    sg = [random.choice([-1, 1]) for _ in range(n)]
    zeta = [sg[k]*rho[k]*Phi[k]**2 for k in range(n)]
    return zeta, Phi, rho, n

m = 2
W = {}
def upd(k, v):
    W[k] = max(W.get(k, mp.mpf(-1e9)), v)

cnt = 0
for trial in range(400):
    nrob, nweak, nnon, nfine = random.randint(1, 3), random.randint(1, 4), random.randint(0, 5), random.randint(0, 3)
    b = mp.mpf(10)**random.uniform(-5, -1.3)
    out = make(nrob, nweak, nnon, nfine, b)
    if out is None: continue
    zeta, Phi, rho, n = out
    th, A = true_threshold(zeta, Phi)
    # independent convex-program check of the true block
    Ac, Mc, Cc, thc = true_convex(zeta, Phi)
    upd('true: |A_threshold - A_convex|/A', abs(float(A) - Ac)/Ac)
    upd('true: |theta_threshold - theta_convex|/theta', abs(float(th) - thc)/thc)
    Pf = set(range(nrob)); fine = set(range(nrob+nweak+nnon, n))
    Wp = list(range(nrob, nrob+nweak))
    PhiW2 = sum(Phi[k]**2 for k in Wp); PhiPf2 = sum(Phi[k]**2 for k in Pf)
    a = A/th
    hyp = (6*b*PhiW2 <= PhiPf2) and (2*b*PhiW2 <= a)
    thf, Af, nu = frozen(zeta, Phi, Pf, fine, th, A)
    x = b*PhiW2/PhiPf2
    if hyp:
        cnt += 1
        upd('(e) theta_f - theta (must be <= 0)', (thf - th)/th)
        upd('(e) (theta - theta_f)/(3 b theta PhiW2/PhiPf2) (<= 1)', (th - thf)/(3*th*x))
        upd('(e) |A_f - A|/(4 b theta PhiW2/PhiPf2) (<= 1)', abs(Af - A)/(4*th*x))
        for k in range(n):
            upd('(e) rho^f_k/(rho_k (1+6x)) (<= 1)', (nu[k]/thf)/((nu[k]/th)*(1 + 6*x)))
        # kappa_f vs formula-1 kappa(Omega) with Omega = all coarse non-Pf (pattern's Omega incl. weak peaks)
        Om = [k for k in range(nrob+nweak+nnon) if k not in Pf]
        SOm = sum(nu[k]**2*Phi[k]**2 for k in Om)
        kf = Af + (Af**2 - SOm)/thf; k1 = A + (A**2 - SOm)/th
        upd('(e) |kappa_f - kappa(Omega)|/(b theta PhiW2/PhiPf2) (constant C)', abs(kf - k1)/(th*x))
        # (d) frozen Lemma K identities
        lam = [m*p for p in Phi]; uv = [z/l for z, l in zip(zeta, lam)]
        r = {k: uv[k]/kf for k in Om}
        R2 = m**2*sum(r[k]**2 for k in Om)
        af, kk = Af/thf, kf/thf; sig = (Af**2 - SOm)/thf**2
        upd('(d) |a^2 - sigma - k^2R^2|', abs(af**2 - sig - kk**2*R2))
        upd('(d) |k - K(sigma,R^2)|', abs(kk - Kfun(sig, R2)))
        upd('(d) R^2 - 1 (must be < 0)', R2 - 1)
        upd('(d) sigma_rob/2 - (1 - R^2) (must be <= 0: W-fix region)', PhiPf2/2 - (1 - R2))
        # Step (i): floor function at r_0 with sigma_rob and R_a (active Omega: weak peaks + nonpeaks with rho > 1/2, say)
        act = [k for k in Om if (nu[k]/th) > 0.5]
        Ra2 = m**2*sum(r[k]**2 for k in act)
        for d in Wp:
            psi = m*abs(r[d])*Kfun(PhiPf2, Ra2)/Phi[d]
            upd('Step(i): psi_d(r_0)/Phi_d - rho^f_d (must be <= 0)', psi - nu[d]/thf)
            upd('Step(i): (rho^f_d - 1)/((1+b)(1+6x) - 1) (<= 1)', (nu[d]/thf - 1)/((1 + b)*(1 + 6*x) - 1))
        # (d) derivative formulas by finite differences (fixed statuses)
        s_f = (sig - PhiPf2 - sum(Phi[k]**2 for k in fine if nu[k] > thf))
        Phi2p = PhiPf2 + sum(Phi[k]**2 for k in fine if nu[k] > thf)
        for j in list(Om)[:3] + list(Pf)[:1]:
            h = abs(zeta[j])*mp.mpf('1e-15') if zeta[j] != 0 else mp.mpf('1e-20')
            zp = list(zeta); zm = list(zeta)
            sgn = 1 if zeta[j] >= 0 else -1
            zp[j] = zeta[j] + sgn*h; zm[j] = zeta[j] - sgn*h
            def kap(z):
                t, Aa, nn = frozen(z, Phi, Pf, fine, thf, Af)
                S = sum(nn[k]**2*Phi[k]**2 for k in Om)
                return Aa + (Aa**2 - S)/t
            fd = (kap(zp) - kap(zm))/(2*h)
            if j in Om:
                pred = (nu[j]/thf)*s_f/(Phi2p*(1 + af))
            else:
                pred = 1 - af*s_f/(Phi2p*(1 + af))
            upd('(d) |d kappa_f/d|zeta_j| fd - formula|', abs(fd - pred))
print('admissible blocks tested:', cnt)
for k, v in W.items():
    print('%-80s max = %.4g' % (k, float(v)))
