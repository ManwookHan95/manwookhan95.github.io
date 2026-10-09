"""N3: the (UN+) configuration in a finite model: two carriers l1 (q1 > 0) and l2 (q2 < 0), each NOT z-signed alone,
whose combinations mu1 u1 + mu2 u2 are z-signed exactly for mu2/mu1 in [1/2, 2] (shared coordinates 9, 10).
Extreme rays A (mu2 = mu1/2) and B (mu2 = 2 mu1); d-sums D_A = q1 + q2/2 (robust > 0), D_B = q1 + 2 q2 = eps (tiny > 0):
no ray of negative d-sum (uncompensated), one tiny positive ray.  Maximal contact z = 1 off F = {0}.
Mate: ray module g = c (V_B - D_B-correction), V_B = u1 + 2 u2 (in lambda-normalized block units).
Measure the minimal switching (|tau1| + |tau2|)/t over two-sided decompositions with the true cap s(t)."""
import sys, numpy as np, cvxpy as cp
from toy import Model, s_of, SOLVER

def build(eps_rel, n=30, r=5, seed=5):
    rng = np.random.default_rng(seed)
    U = np.zeros((n, r))
    for j in range(n):
        U[j] = 0.15 * 2.0 ** (-0.3 * j) * rng.standard_normal(r)
    E = np.eye(n)
    peaks = [E[1] * 0.8, -E[2] * 0.8, E[3] * 0.6 + E[4] * 0.2, -E[5] * 0.7, E[6] * 0.5 - E[1] * 0.3]
    y1 = 0.3 * E[4] + 0.2 * E[7] + 0.2 * E[10] - 0.15 * E[9]
    y2 = 0.3 * E[9] + 0.1 * E[8] - 0.1 * E[10]
    us, Phis, nxt = [], [], 11
    for k, y in enumerate(peaks + [y1, y2]):
        S = list(range(nxt, nxt + 2)); nxt += 2
        h = np.zeros(n); h[S] = 2.0 ** (-np.arange(1, 3))
        us.append(y + 0.15 * h)
        Phis.append(0.05 * 2.0 ** (-k) if k < 5 else 2e-3)
    b = dict(u=np.array(us), Phi=np.array(Phis), m=1)
    M = Model(U, [b])
    a = np.zeros(n); a[0] = 1.0; a /= M.qstar(a); z = np.ones(n)
    l1, l2 = 5, 6
    # tune F-entries: q2 = -0.3 * thr-scale (robust negative), and q1 + 2 q2 = eps_rel * |q2|
    for it in range(100):
        D = M.first_row(a, z)
        C, Mm, sig = D['C'][0], D['M'][0], D['sigma'][0]
        q = lambda l: b['Phi'][l] * D['w'][0][l] / C
        thr2 = sig * b['Phi'][l2] * Mm / C           # threshold in u(xi) units
        t2 = -0.3 * thr2                              # u2(xi) target (non-peak, q2 < 0)
        cur2 = b['u'][l2] @ D['xi']
        b['u'][l2][0] += (t2 - cur2) / (D['q0'] * D['zhat'][0])
        q2 = q(l2)
        q1_target = -2 * q2 + eps_rel * abs(q2)
        # q1 = Phi1 w1/C, off-peak w1 = C zeta1/(Phi1^2 sigma) -> q1 = zeta1/(Phi1 sigma) = u1(xi)/sigma (m=1)
        cur1 = b['u'][l1] @ D['xi']; t1 = q1_target * sig
        b['u'][l1][0] += (t1 - cur1) / (D['q0'] * D['zhat'][0])
        if abs(t1 - cur1) + abs(t2 - cur2) < 1e-14: break
    D = M.first_row(a, z)
    return M, D, l1, l2

def ray_module(M, D, l1, l2, c):
    b = M.blocks[0]; C = D['C'][0]
    om = np.zeros(len(b['Phi'])); om[l1] = c / b['lam'][l1]; om[l2] = 2 * c / b['lam'][l2]
    d = (b['Phi'] ** 2 * D['w'][0]) @ om / C
    return M.Lstar([om - d * D['w'][0]]), om

def min_switch(M, D, g, l1, l2, t):
    f = D['f']; b = M.blocks[0]; w = D['w'][0]; n = M.n; K = len(b['Phi'])
    Ap, Am, Wp, Wm = cp.Variable(n), cp.Variable(n), cp.Variable(K), cp.Variable(K)
    cap = s_of(t)
    cons = [cp.norm1(Ap) + cp.norm(M.U.T @ Ap) <= cap, cp.norm_inf(Wp) + cp.norm(cp.multiply(b['Phi'], Wp)) <= cap,
            Ap + b['u'].T @ cp.multiply(b['lam'], Wp) == f + t * g,
            cp.norm1(Am) + cp.norm(M.U.T @ Am) <= cap, cp.norm_inf(Wm) + cp.norm(cp.multiply(b['Phi'], Wm)) <= cap,
            Am + b['u'].T @ cp.multiply(b['lam'], Wm) == f - t * g]
    sw = [(b['lam'][l] / t) * (Wp[l] + Wm[l] - 2 * w[l]) for l in (l1, l2)]
    pr = cp.Problem(cp.Minimize(cp.abs(sw[0]) + cp.abs(sw[1])), cons)
    pr.solve(solver=SOLVER)
    return pr.value, pr.status

if __name__ == '__main__':
    eps_rel = float(sys.argv[1]); c = float(sys.argv[2])
    M, D, l1, l2 = build(eps_rel)
    b = M.blocks[0]; C = D['C'][0]; q = lambda l: b['Phi'][l] * D['w'][0][l] / C
    print(f"eps_rel={eps_rel}: q1={q(l1):+.3e} q2={q(l2):+.3e} D_A={q(l1) + q(l2) / 2:+.3e} D_B={q(l1) + 2 * q(l2):+.3e}"
          f" gaps: {D['M'][0] - abs(D['w'][0][l1]):.3f} {D['M'][0] - abs(D['w'][0][l2]):.3f}")
    g, om = ray_module(M, D, l1, l2, c)
    ts = np.geomspace(3e-3, 1.0, 14)
    worst = max(max(M.pstar(D['f'] + t * g), M.pstar(D['f'] - t * g)) - s_of(t) for t in ts)
    print(f"  c={c}: mate defect on grid = {worst:+.2e}  (<= 0 means mate)")
    if worst <= 1e-7:
        for t in ts:
            v, st = min_switch(M, D, g, l1, l2, t)
            print(f"  t={t:.2e}  min (|tau1|+|tau2|)/t = {v:.3e}  [{st}]")
