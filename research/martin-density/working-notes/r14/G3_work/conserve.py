r"""Numerical check of Theorem CL (global conservation law for the switching vector), G3 notes.

For decompositions f + t g = A_+ + R^T W_+, f - t g = A_- + R^T W_- with norms <= s(t) and g(xi) = 0:
   V := B_+ - B_- = (A_+ + A_- - 2a)/t,
   |V(zhat)| <= 2(s(t)-1)/(q0 t)                                                     (CL0)
   sum_{s notin T} |z_s||V_s| <= |<V 1_T, zhat>| + |<V 1_{F\T}, h>| + 2(s-1)/(q0 t) + 2*sum_{s notin T} err_s     (|z|-weighted form of CL2)
with err_s = (e_s^+ + e_s^-)/(2t) off F and (2|a_s| + (e_s^+ + e_s^-)/2)/t on F.  We also print the crude form
   RHS_crude = |<V1_T, zhat>| + |<V1_{F\T}, h>| + 2t/q0 + 4 alpha(F\T)/t.
"""
import numpy as np
import cvxpy as cp
from model import Row, SOLVER
from selfpin import build, tune


def solve_switch(row, t, k, sign=+1):
    n, K = row.n, row.K
    st = np.sqrt(1 + t * t)
    g = cp.Variable(n)
    Ap, Am = cp.Variable(n), cp.Variable(n)
    Wp, Wm = cp.Variable(K), cp.Variable(K)
    cons = [row.f + t * g == Ap + cp.multiply(row.lam, Wp) @ row.U,
            row.f - t * g == Am + cp.multiply(row.lam, Wm) @ row.U,
            row.xi @ g == 0]
    for A in (Ap, Am):
        cons.append(cp.norm(A, 1) + cp.norm(cp.multiply(row.mu, A), 2) <= st)
    for W in (Wp, Wm):
        cons.append(cp.norm(W, 'inf') + cp.norm(cp.multiply(row.Phi, W), 2) <= st)
    gam = row.lam[k] * ((row.w[k] - Wm[k]) / t - (Wp[k] - row.w[k]) / t)
    prob = cp.Problem(cp.Maximize(sign * gam), cons)
    prob.solve(**SOLVER)
    return prob.value, prob.status, Ap.value, Am.value, Wp.value, Wm.value


def check(row, t, thick_thr=0.05):
    val, st, Ap, Am, Wp, Wm = solve_switch(row, t, 0, +1)
    a, z, zhat = row.a, row.z, row.zhat
    F = np.abs(a) > 1e-14
    T = np.abs(a) > thick_thr
    N = ~T
    h = np.where(F, zhat - z, 0.0)
    V = (Ap + Am - 2 * a) / t
    s1 = np.sqrt(1 + t * t) - 1
    ep = np.abs(Ap) - z * Ap
    em = np.abs(Am) - z * Am
    err = np.where(F, (2 * np.abs(a) + (ep + em) / 2) / t, (ep + em) / (2 * t))
    lhs = np.sum(np.abs(z[N]) * np.abs(V[N]))
    thick = abs(V[T] @ zhat[T])
    hterm = abs(V[F & N] @ h[F & N])
    rhs = thick + hterm + 2 * s1 / (row.q0 * t) + 2 * err[N].sum()
    crude = thick + hterm + 2 * t / row.q0 + 4 * np.abs(a[F & N]).sum() / t
    Vz = V @ zhat
    gam = row.lam * ((row.w - Wm) / t - (Wp - row.w) / t)
    Vrec = gam @ row.U          # V = L^*(Theta_- - Theta_+) should equal B_+ - B_-
    return dict(st=st, gmax=val, Vz=Vz, Vz_bd=2 * s1 / (row.q0 * t), lhs=lhs, rhs=rhs, crude=crude, thick=thick,
                Vrec_err=np.abs(Vrec - V).max(), gam=gam)


if __name__ == '__main__':
    cases = [('D=0, r CONTACT', lambda: (build(0.0, 'contact'), 0.05)),
             ('D=0, r THIN 1e-3', lambda: (tune(0.0, 'thin', 1e-3)[0], 0.05)),
             ('D=0, r THICK 0.15', lambda: (tune(0.0, 'thick', 0.15)[0], 0.05)),
             ('D=-0.001, r THICK 0.15', lambda: (tune(-0.001, 'thick', 0.15)[0], 0.05)),
             ('D=-0.004, r THICK 0.15 (l- is a peak here)', lambda: (tune(-0.004, 'thick', 0.15)[0], 0.05))]
    for name, mk in cases:
        row, thr = mk()
        print(f"\n== {name}  q0={row.q0:.4f}  a={np.round(row.a, 4)}")
        for t in [1e-1, 3e-2, 1e-2]:
            r = check(row, t, thr)
            print(f"  t={t:6.0e} [{r['st']}] gamma'_+max={r['gmax']:.4f}  |V(zhat)|={abs(r['Vz']):.2e} <= {r['Vz_bd']:.2e}"
                  f"   LHS={r['lhs']:.4f} <= RHS={r['rhs']:.4f} (crude {r['crude']:.4f}; thick part {r['thick']:.4f})"
                  f"   |V - L*dTheta|={r['Vrec_err']:.1e}")
