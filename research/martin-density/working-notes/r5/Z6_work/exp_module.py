"""Experiment N2/N3: forced switching profile of a single 'module' at a maximal-contact toy first row.

One block, F = {0}, z = 1 everywhere (maximal contact), strong peaks of both signs, one resonant strict
non-peak carrier l (u_l >= 0 off F) with w(k_l) = kappa*M > 0 (q_l > 0, uncompensated).
Module mate g = c (u_l - q_l L^* w), q_l = Phi_l w(k_l)/C (m = 1).
For each scale t: check p*(f +- t g) <= s(t); compute the minimal switching through l over near-optimal
two-sided decompositions (forced switching) and its maximal value (spurious switching allowed by the budget).
"""
import sys
import numpy as np
import cvxpy as cp
from toy import Model, s_of, SOLVER

rng = np.random.default_rng(1)


def build(kappa=0.5, Phi_l=2e-3, n=26, r=4, seed=1):
    rng = np.random.default_rng(seed)
    U = np.zeros((n, r))
    for j in range(n):
        U[j] = 0.15 * 2.0 ** (-0.3 * j) * rng.standard_normal(r)
    pool = list(range(1, 7))            # shared target coordinates
    sig_start = 7
    K = 6
    us, Phis = [], []
    nxt = sig_start
    targets = [  # strong peaks of both signs + module
        np.eye(n)[1] * 0.8, -np.eye(n)[2] * 0.8, np.eye(n)[3] * 0.6 + np.eye(n)[4] * 0.2,
        -np.eye(n)[5] * 0.7, np.eye(n)[6] * 0.5 - np.eye(n)[1] * 0.3,
    ]
    for k in range(K):
        S = list(range(nxt, nxt + 3)); nxt += 3
        h = np.zeros(n); h[S] = 2.0 ** (-np.arange(1, 4))
        if k < K - 1:
            y = targets[k]
            u = y + 0.15 * h
            Phis.append(0.05 * 2.0 ** (-k))
        else:
            y = np.zeros(n); y[3] = 0.3; y[4] = 0.2; y[6] = 0.1   # nonnegative off F
            u = y + 0.15 * h                                       # u(0) tuned below
            Phis.append(Phi_l)
        us.append(u)
    blocks = [dict(u=np.array(us), Phi=np.array(Phis), m=1)]
    M = Model(U, blocks)
    a = np.zeros(n); a[0] = 1.0
    a = a / M.qstar(a)
    z = np.ones(n)
    l = K - 1
    # tune u_l(0) so that u_l(xi) = kappa * threshold  (threshold: |zeta| Phi M/(m C) in u(xi) units)
    for it in range(60):
        D = M.first_row(a, z)
        b = blocks[0]
        thr = D['sigma'][0] * Phis[l] * D['M'][0] / (1 * D['C'][0])
        cur = b['u'][l] @ D['xi']
        target_val = kappa * thr
        # u_l(xi) = q0 * u_l(zhat); d u_l(zhat)/d u_l(0) = zhat[0]
        b['u'][l][0] += (target_val - cur) / (D['q0'] * D['zhat'][0])
        if abs(target_val - cur) < 1e-12:
            break
    D = M.first_row(a, z)
    return M, D, l


def module(M, D, l, c):
    b = M.blocks[0]
    wl = D['w'][0][l]
    q = b['Phi'][l] * wl / D['C'][0]
    g = c * (b['u'][l] - q * M.Lstar(D['w']))
    return g, q


def forced_switching(M, D, g, l, t, kappa_slack=0.05):
    f = D['f']; b = M.blocks[0]; w = D['w'][0]; lam = b['lam'][l]
    pp = M.pstar(f + t * g); pm = M.pstar(f - t * g)
    cap_p = pp + kappa_slack * t * t; cap_m = pm + kappa_slack * t * t
    n = M.n; K = len(b['Phi'])
    Ap, Am = cp.Variable(n), cp.Variable(n)
    Wp, Wm = cp.Variable(K), cp.Variable(K)
    cons = [cp.norm1(Ap) + cp.norm(M.U.T @ Ap) <= cap_p,
            cp.norm_inf(Wp) + cp.norm(cp.multiply(b['Phi'], Wp)) <= cap_p,
            Ap + b['u'].T @ cp.multiply(b['lam'], Wp) == f + t * g,
            cp.norm1(Am) + cp.norm(M.U.T @ Am) <= cap_m,
            cp.norm_inf(Wm) + cp.norm(cp.multiply(b['Phi'], Wm)) <= cap_m,
            Am + b['u'].T @ cp.multiply(b['lam'], Wm) == f - t * g]
    sw = (lam / t) * (Wp[l] + Wm[l] - 2 * w[l])      # Delta theta_l
    def solve(obj):
        pr = cp.Problem(obj, cons)
        try:
            pr.solve(solver=SOLVER)
        except Exception:
            try:
                pr.solve(solver=cp.SCS, eps=1e-9, max_iters=200000)
            except Exception:
                return float('nan')
        return pr.value
    mn = solve(cp.Minimize(cp.abs(sw)))
    mx = solve(cp.Maximize(sw))
    ms = solve(cp.Minimize(sw))
    return pp, pm, mn, mx, ms


if __name__ == '__main__':
    kappa = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    c = float(sys.argv[2]) if len(sys.argv) > 2 else 0.02
    Phil = float(sys.argv[3]) if len(sys.argv) > 3 else 2e-3
    M, D, l = build(kappa=kappa, Phi_l=Phil)
    b = M.blocks[0]
    print('q0=%.4f M=%.4f C=%.4f sigma=%.4f' % (D['q0'], D['M'][0], D['C'][0], D['sigma'][0]))
    print('w =', np.round(D['w'][0], 4))
    print('u_k(xi)/thr:', np.round([b['u'][k] @ D['xi'] / (D['sigma'][0] * b['Phi'][k] * D['M'][0] / D['C'][0]) for k in range(len(b['Phi']))], 3))
    g, q = module(M, D, l, c)
    print('module: c=%.3g q_l=%.3e lam_l=%.3e g(xi)=%.2e ||g||_1=%.3e' % (c, q, b['lam'][l], g @ D['xi'], np.abs(g).sum()))
    print(' t        p*(f+tg)-s(t)  p*(f-tg)-s(t)  minSwitch   maxSwitch  minSigned')
    for t in np.geomspace(3e-3, 0.5, 16):
        pp, pm, mn, mx, ms = forced_switching(M, D, g, l, t)
        print('%.2e  %+.3e  %+.3e  %.3e  %.3e  %+.3e   minSwitch/t=%.3f' % (t, pp - s_of(t), pm - s_of(t), mn, mx, ms, mn/t))
