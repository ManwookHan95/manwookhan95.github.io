"""Referee (b) for Q1, independent check of Lemma PM (ii)-(iii): with the normalized values nv = zeta/A of ALL coarse strict
non-peaks frozen and coarse peaks kept clamped, C_m (hence every relative position) moves only through the fine carriers.
Block model (note, lem:threshold): zeta_k = lambda_k x_k, lambda_k = m Phi_k, x_k = u_k(xhat) in [-1.25, 1.25].
Norming functional: |w_k| = M min(1, nu_k/theta), nu_k = |zeta_k|/Phi_k^2, theta solves
    theta = S2(theta)/(sqrt(S1(theta)) (1 + sqrt(S1(theta)))),  S1 = sum Phi^2 min(1,nu/theta)^2, S2 = sum |zeta| min(1,nu/theta),
M = 1/(1 + sqrt S1), C = M sqrt S1, A = M S2.  Cross-checked once against cvxpy (dual-norm maximization).
"""
import mpmath as mp, random, sys
mp.mp.dps = 80
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 3)

def solve(Phi, zeta):
    nu = [abs(z)/p**2 for z, p in zip(zeta, Phi)]
    def G(th):
        S1 = mp.fsum(p**2*min(1, n/th)**2 for p, n in zip(Phi, nu))
        S2 = mp.fsum(abs(z)*min(1, n/th) for z, n in zip(zeta, nu))
        return th - S2/(mp.sqrt(S1)*(1 + mp.sqrt(S1))), S1, S2
    # G is increasing in theta (bracket: tiny theta -> negative, huge theta -> positive)
    lo, hi = mp.mpf(10)**-60, max(nu)*10
    assert G(lo)[0] < 0 < G(hi)[0]
    th = mp.findroot(lambda t: G(t)[0], (lo, hi), solver='anderson') if False else None
    for _ in range(600):
        mid = mp.sqrt(lo*hi) if hi/lo > 4 else (lo+hi)/2
        if G(mid)[0] < 0: lo = mid
        else: hi = mid
    th = (lo+hi)/2
    _, S1, S2 = G(th)
    M = 1/(1 + mp.sqrt(S1)); C = M*mp.sqrt(S1); A = M*S2
    rho = [n/th for n in nu]
    return dict(theta=th, M=M, C=C, A=A, rho=rho)

def build(m, cw, fine_n, fine_scale, mu):
    # coarse carriers: indices 0,1 peaks; 2 near-threshold d; 3,4 robust non-peaks; 5 nearly neutral
    Phi = [mp.mpf(2)**(-m-k-1)*c for k, c in enumerate(cw)]
    Phi += [mp.mpf(2)**(-m-6-k)*fine_scale*mp.mpf(random.uniform(0.2, 1))*mp.mpf(4)**(-k) for k in range(fine_n)]
    lam = [m*p for p in Phi]
    x = [mp.mpf(1.2), mp.mpf(-1.1), mp.mpf(0.5), mp.mpf(0.3), mp.mpf(-0.2), mp.mpf(0)]
    x += [mp.mpf(random.uniform(-1.2, 1.2)) for _ in range(fine_n)]
    # tune x[2] so that rho_d = 1 - mu, x[3], x[4] so that rho in [0.3, 0.6], x[5] so rho ~ 1e-30 (fixed point)
    targets = {2: 1 - mu, 3: mp.mpf('0.45'), 4: mp.mpf('0.35'), 5: mp.mpf('1e-30')}
    for it in range(200):
        z = [l*xx for l, xx in zip(lam, x)]
        s = solve(Phi, z)
        for k, tg in targets.items():
            x[k] = x[k]/abs(x[k])*tg*s['theta']*Phi[k]**2/lam[k] if x[k] != 0 else tg*s['theta']*Phi[k]**2/lam[k]
    z = [l*xx for l, xx in zip(lam, x)]
    return Phi, lam, x, z

def perturb_and_measure(Phi, lam, x, z, s0, r, omega, tune_all=True):
    # peaks 0,1: relative perturbation r (stay peaks); fine carriers (>= 6): arbitrary new x in [-1.2, 1.2];
    # Omega carriers: zeta'_k = (A'/A) zeta_k (frozen nv) — fixed point in A'
    xp = list(x)
    xp[0] = x[0]*(1 + r); xp[1] = x[1]*(1 - r)
    for k in range(6, len(x)): xp[k] = mp.mpf(random.uniform(-1.2, 1.2))
    om = omega if tune_all else [k for k in omega if k != 3]
    sc = mp.mpf(1)
    for it in range(400):
        zp = [l*xx for l, xx in zip(lam, xp)]
        for k in om: zp[k] = sc*z[k]
        s1 = solve(Phi, zp)
        sc_new = s1['A']/s0['A']
        if abs(sc_new - sc) < mp.mpf(10)**-70: break
        sc = sc_new
    return s1

m = 2
res = []
for inst in range(4):
    cw = [mp.mpf(random.uniform(0.3, 1)) for _ in range(6)]
    mu = mp.mpf(10)**(-random.choice([8, 12, 16]))
    fine_scale = mu**2          # fine total weight ~ c_{L+1} <= b^2 <= mu^2/64
    Phi, lam, x, z = build(m, cw, 30, fine_scale, mu)
    s0 = solve(Phi, z)
    omega = [2, 3, 4, 5]
    assert s0['rho'][0] > 1 and s0['rho'][1] > 1 and all(s0['rho'][k] < 1 for k in omega)
    r = mp.mpf(random.choice(['1e-3', '1e-4', '1e-2']))
    s1 = perturb_and_measure(Phi, lam, x, z, s0, r, omega, True)
    s2 = perturb_and_measure(Phi, lam, x, z, s0, r, omega, False)
    fine_lam = mp.fsum(lam[6:])
    res.append((inst, mu, r, s0['rho'][2], s1['rho'][2], abs(s1['C'] - s0['C']), fine_lam, abs(s2['C'] - s0['C']), s2['rho'][2]))
    print(f"inst {inst}: mu={mp.nstr(mu,2)} r={mp.nstr(r,2)} rho_d={mp.nstr(s0['rho'][2],22)} | all-tuned: rho'_d={mp.nstr(s1['rho'][2],22)} "
          f"|C'-C|={mp.nstr(abs(s1['C']-s0['C']),3)} (fine lambda sum {mp.nstr(fine_lam,3)}) | one untuned: |C'-C|={mp.nstr(abs(s2['C']-s0['C']),3)} rho'_d={mp.nstr(s2['rho'][2],22)}")

# cvxpy cross-check of the block solver on one small instance (double precision)
try:
    import cvxpy as cp, numpy as np
    Phi = [2.0**(-3-k)*random.uniform(0.3,1) for k in range(8)]
    zeta = [random.uniform(-1, 1)*2*p for p in Phi]
    s = solve([mp.mpf(p) for p in Phi], [mp.mpf(v) for v in zeta])
    w = cp.Variable(8)
    prob = cp.Problem(cp.Maximize(np.array(zeta) @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(np.array(Phi), w), 2) <= 1])
    prob.solve()
    print("cvxpy cross-check: A(solver) =", mp.nstr(s['A'], 12), " A(cvx) =", prob.value, " rel diff", abs(float(s['A']) - prob.value)/prob.value)
except Exception as e:
    print("cvxpy unavailable:", e)
