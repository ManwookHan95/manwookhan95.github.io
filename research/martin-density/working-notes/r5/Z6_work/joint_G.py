"""Joint version of Conjecture G (Z6 notes 6.2): two module carriers l1, l2 in one uncompensated block at maximal contact.
Mate g = g1 + g2 (sum of the two modules, SAME scale range).  For each t with p*(f +- t g) <= s(t) we compute, over pairs of
decompositions with cap s(t) (the two-sided criterion), (a) min |Dtheta_l1|, (b) min |Dtheta_l2|, (c) min (|Dtheta_l1| + |Dtheta_l2|).
Joint Conjecture G predicts (c) <= C t (1/m_u(l1) + 1/m_u(l2)) for nearly neutral carriers; (c) ~ (a) + (b) means one decomposition
does both jobs.  Usage: python3 joint_G.py kappa1 kappa2 c1 c2 [Phi]"""
import sys
import numpy as np
import cvxpy as cp
from toy import Model, s_of, SOLVER


def build2(kappas, Phi_l=2e-3, n=30, r=4, seed=1):
    rng = np.random.default_rng(seed)
    U = np.zeros((n, r))
    for j in range(n):
        U[j] = 0.15 * 2.0 ** (-0.3 * j) * rng.standard_normal(r)
    E = np.eye(n)
    targets = [E[1] * 0.8, -E[2] * 0.8, E[3] * 0.6 + E[4] * 0.2, -E[5] * 0.7, E[6] * 0.5 - E[1] * 0.3]
    mod_targets = [0.3 * E[3] + 0.2 * E[4] + 0.1 * E[6], 0.25 * E[4] + 0.2 * E[6] + 0.15 * E[3]]
    us, Phis = [], []
    nxt = 7
    for k, y in enumerate(targets + mod_targets):
        S = list(range(nxt, nxt + 3)); nxt += 3
        h = np.zeros(n); h[S] = 2.0 ** (-np.arange(1, 4))
        us.append(y + 0.15 * h)
        Phis.append(0.05 * 2.0 ** (-k) if k < len(targets) else Phi_l * (1.0 if k == len(targets) else 0.7))
    blocks = [dict(u=np.array(us), Phi=np.array(Phis), m=1)]
    M = Model(U, blocks)
    a = np.zeros(n); a[0] = 1.0; a = a / M.qstar(a)
    z = np.ones(n)
    ls = [len(targets), len(targets) + 1]
    b = blocks[0]
    for it in range(80):
        D = M.first_row(a, z)
        err = 0.0
        for l, kap in zip(ls, kappas):
            thr = D['sigma'][0] * b['Phi'][l] * D['M'][0] / D['C'][0]
            cur = b['u'][l] @ D['xi']
            b['u'][l][0] += (kap * thr - cur) / (D['q0'] * D['zhat'][0])
            err = max(err, abs(kap * thr - cur))
        if err < 1e-12:
            break
    return M, M.first_row(a, z), ls


def module(M, D, l, c):
    b = M.blocks[0]
    q = b['Phi'][l] * D['w'][0][l] / D['C'][0]
    return c * (b['u'][l] - q * M.Lstar(D['w'])), q


def min_sw(M, D, g, ls, t, weights):
    f = D['f']; b = M.blocks[0]; w = D['w'][0]; n = M.n; K = len(b['Phi']); cap = s_of(t)
    Ap, Am = cp.Variable(n), cp.Variable(n); Wp, Wm = cp.Variable(K), cp.Variable(K)
    cons = [cp.norm1(Ap) + cp.norm(M.U.T @ Ap) <= cap, cp.norm_inf(Wp) + cp.norm(cp.multiply(b['Phi'], Wp)) <= cap,
            Ap + b['u'].T @ cp.multiply(b['lam'], Wp) == f + t * g,
            cp.norm1(Am) + cp.norm(M.U.T @ Am) <= cap, cp.norm_inf(Wm) + cp.norm(cp.multiply(b['Phi'], Wm)) <= cap,
            Am + b['u'].T @ cp.multiply(b['lam'], Wm) == f - t * g]
    obj = sum(wt * cp.abs((b['lam'][l] / t) * (Wp[l] + Wm[l] - 2 * w[l])) for l, wt in zip(ls, weights))
    pr = cp.Problem(cp.Minimize(obj), cons)
    try:
        pr.solve(solver=SOLVER)
    except Exception:
        try:
            pr.solve(solver=cp.SCS, eps=1e-9, max_iters=200000)
        except Exception:
            return float('nan')
    return pr.value


if __name__ == '__main__':
    k1, k2, c1, c2 = (float(x) for x in sys.argv[1:5])
    Phil = float(sys.argv[5]) if len(sys.argv) > 5 else 2e-3
    M, D, ls = build2((k1, k2), Phi_l=Phil)
    b = M.blocks[0]
    g1, q1 = module(M, D, ls[0], c1); g2, q2 = module(M, D, ls[1], c2)
    g = g1 + g2
    mus = [np.abs(b['u'][l][1:]).sum() for l in ls]
    print('w(k_l)/M = %.3f %.3f  q = %.2e %.2e  m_u = %.3f %.3f  g(xi) = %.1e' %
          (D['w'][0][ls[0]] / D['M'][0], D['w'][0][ls[1]] / D['M'][0], q1, q2, mus[0], mus[1], g @ D['xi']))
    print('   t        pp-s       pm-s     min|sw1|/t  min|sw2|/t  min(|sw1|+|sw2|)/t')
    for t in np.geomspace(3e-3, 0.5, 14):
        pp = M.pstar(D['f'] + t * g); pm = M.pstar(D['f'] - t * g)
        ok = max(pp, pm) <= s_of(t) + 1e-9
        a1 = min_sw(M, D, g, ls, t, (1, 0)) if ok else float('nan')
        a2 = min_sw(M, D, g, ls, t, (0, 1)) if ok else float('nan')
        a3 = min_sw(M, D, g, ls, t, (1, 1)) if ok else float('nan')
        print('%.2e  %+.2e  %+.2e   %.4f      %.4f      %.4f %s' % (t, pp - s_of(t), pm - s_of(t), a1 / t, a2 / t, a3 / t,
                                                                  '' if ok else 'NOT A MATE AT THIS t'), flush=True)
