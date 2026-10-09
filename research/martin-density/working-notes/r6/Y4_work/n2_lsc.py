"""N2: lower semicontinuity of the mate fibre along tuned rows (finite SOCP model; degenerate, sanity only).
Maximal contact z = 1 off F = {0,1}; one block; strong peaks of both signs; a nearly neutral resonant carrier l
(u_l >= 0 off F) with u_l(xi) = kappa * threshold.  Module mate g = c (u_l - q_l L^* w).
Approximants f' (same z): (A) bank-raise a' ~ a + m*W (W = u_l, z-signed) [raises u_l(zhat)];
(B) F-tune: a' = a + s*d_F (two-sided) chosen to make u_l(zhat') = 0; (C) lower via masses at contacts j with
z_j h_W(j) < 0 (mixing base) to make u_l(zhat') = 0.  Report cost p*(f'-f), u_l(zhat'), and
dist_1(rho g, C_grid(f')) where C_grid uses a finite grid of scales (a relaxation: lower bound for the true distance).
"""
import numpy as np, cvxpy as cp, sys
from toy import Model, s_of, SOLVER

def build(kappa, n=26, r=5, seed=3, Phi_l=2e-3):
    rng = np.random.default_rng(seed)
    U = np.zeros((n, r))
    for j in range(n):
        U[j] = 0.15 * 2.0 ** (-0.3 * j) * rng.standard_normal(r)
    targets = [np.eye(n)[2] * 0.8, -np.eye(n)[3] * 0.8, np.eye(n)[4] * 0.6 + np.eye(n)[5] * 0.2,
               -np.eye(n)[6] * 0.7, np.eye(n)[7] * 0.5 - np.eye(n)[2] * 0.3]
    K = 6; us, Phis = [], []; nxt = 8
    for k in range(K):
        S = list(range(nxt, nxt + 3)); nxt += 3
        h = np.zeros(n); h[S] = 2.0 ** (-np.arange(1, 4))
        if k < K - 1:
            us.append(targets[k] + 0.15 * h); Phis.append(0.05 * 2.0 ** (-k))
        else:
            y = np.zeros(n); y[4] = 0.3; y[5] = 0.2; y[7] = 0.1
            us.append(y + 0.15 * h); Phis.append(Phi_l)
    blocks = [dict(u=np.array(us), Phi=np.array(Phis), m=1)]
    M = Model(U, blocks)
    a = np.zeros(n); a[0] = 0.7; a[1] = 0.3; a = a / M.qstar(a)
    z = np.ones(n)
    l = K - 1
    for it in range(80):
        D = M.first_row(a, z); b = blocks[0]
        thr = D['sigma'][0] * Phis[l] * D['M'][0] / D['C'][0]
        cur = b['u'][l] @ D['xi']; tv = kappa * thr
        b['u'][l][0] += (tv - cur) / (D['q0'] * D['zhat'][0])
        if abs(tv - cur) < 1e-13: break
    return M, a, z, l

def module(M, D, l, c):
    b = M.blocks[0]; q = b['Phi'][l] * D['w'][0][l] / D['C'][0]
    return c * (b['u'][l] - q * M.Lstar(D['w'])), q

def is_mate(M, f, g, ts):
    return max(M.pstar(f + t * g) - s_of(t) for t in ts)

def dist_to_fibre(M, f, target, ts, xi=None):
    n = M.n; b = M.blocks[0]; Kc = len(b['Phi'])
    h = cp.Variable(n); cons = [] if xi is None else [h @ xi == 0]
    for t in ts:
        A = cp.Variable(n); W = cp.Variable(Kc)
        cons += [A + b['u'].T @ cp.multiply(b['lam'], W) == f + t * h,
                 cp.norm1(A) + cp.norm(M.U.T @ A) <= s_of(t),
                 cp.norm_inf(W) + cp.norm(cp.multiply(b['Phi'], W)) <= s_of(t)]
    pr = cp.Problem(cp.Minimize(cp.norm1(h - target)), cons); pr.solve(solver=SOLVER)
    return pr.value

if __name__ == '__main__':
    kappa = float(sys.argv[1]) if len(sys.argv) > 1 else 0.05
    rho = float(sys.argv[2]) if len(sys.argv) > 2 else 0.99
    M, a, z, l = build(kappa)
    D = M.first_row(a, z); f = D['f']
    ts = np.concatenate([np.geomspace(1e-5, 3, 30), -np.geomspace(1e-5, 3, 30)])
    # largest valid module coefficient on the grid
    c = 0.0
    for cc in [0.005, 0.01, 0.02, 0.03, 0.04, 0.06, 0.08]:
        g, q = module(M, D, l, cc)
        if is_mate(M, f, g, ts) <= 1e-7: c = cc
    g, q = module(M, D, l, c)
    ul = M.blocks[0]['u'][l]
    print(f"kappa={kappa}: q_l={q:.3e}, u_l(zhat)={ul @ D['zhat']:.3e}, module c={c}, mate defect={is_mate(M, f, g, ts):.2e}")
    print("dist(rho g, C(f)) =", f"{dist_to_fibre(M, f, rho * g, ts, D['xi']):.2e}")
    U = M.U; e = D['e']; nu = D['nu']; P = np.eye(U.shape[1]) - np.outer(e, e)
    W = ul.copy()                                   # z-signed off F (>= 0), any on F
    hW = U @ (P @ (U.T @ W))
    def row_from(a2):
        a2 = a2 / M.qstar(a2); return M.first_row(a2, np.where(np.arange(M.n) < 2, np.sign(a2), z))
    fams = {}
    # (A) bank-raise
    fams['A_raise'] = [a + m * W * np.where(np.arange(M.n) < 2, 1, 1) for m in [0.02, 0.01, 0.005]]
    # (B) F-tune to exact neutrality: one parameter along d_F = (1,-1) on F
    def ul_of(a2):
        Dd = row_from(a2); return ul @ Dd['zhat']
    s_lo, s_hi = -0.3, 0.3
    fl, fh = ul_of(a + s_lo * np.r_[1, -1, np.zeros(M.n - 2)]), ul_of(a + s_hi * np.r_[1, -1, np.zeros(M.n - 2)])
    if fl * fh < 0:
        for it in range(60):
            sm = 0.5 * (s_lo + s_hi); fm = ul_of(a + sm * np.r_[1, -1, np.zeros(M.n - 2)])
            if fl * fm <= 0: s_hi, fh = sm, fm
            else: s_lo, fl = sm, fm
        fams['B_Ftune'] = [a + 0.5 * (s_lo + s_hi) * np.r_[1, -1, np.zeros(M.n - 2)]]
    # (C) lower via masses at lowering contacts (z_j h_W(j) < 0, j >= 2)
    low = [j for j in range(2, M.n) if hW[j] < -1e-12]
    print('lowering contacts:', low, 'ul(zhat)=', ul @ D['zhat'])
    if low and ul @ D['zhat'] > 0:
        dirC = np.zeros(M.n); dirC[low] = 1.0
        lo, hi = 0.0, 2.0
        if ul_of(a + hi * dirC) < 0:
            for it in range(60):
                mid = 0.5 * (lo + hi)
                if ul_of(a + mid * dirC) > 0: lo = mid
                else: hi = mid
            fams['C_lower'] = [a + 0.5 * (lo + hi) * dirC]
    for name, lst in fams.items():
        for a2 in lst:
            D2 = row_from(a2); f2 = D2['f']
            cost = M.pstar(f2 - f)
            dist = dist_to_fibre(M, f2, rho * g, ts, D2['xi'])
            print(f"{name:8s}: cost p*(f'-f)={cost:.2e}  u_l(zhat')={ul @ D2['zhat']:+.2e}  dist(rho g, C(f'))={dist:.2e}"
                  f"  dist/sqrt(cost)={dist / np.sqrt(cost):.2f}")
