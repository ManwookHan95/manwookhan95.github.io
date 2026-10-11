import numpy as np, cvxpy as cp
import sqrt_mu_check as M
m = 1e-4
a, z, xhat, w, f, psi, zeta = M.build_row(m)
sig_hat = zeta @ w; c = 1/(1+sig_hat); sigma = c*sig_hat
C = np.linalg.norm(M.Phi*w); alpha = zeta/sig_hat - M.Phi**2*w/C
n, nb = M.n, M.nb
x = xhat*c   # normer x' = xhat'/p(xhat')
g = cp.Variable(n); vars_ = {}; cons = []
for t in M.tgrid:
    A = cp.Variable(n); W = cp.Variable(nb); st = np.sqrt(1+t*t)
    vars_[t] = (A, W)
    cons += [A + M.Rstar @ W == f + t*g, cp.norm(A,1) + cp.norm(cp.multiply(M.mu, A),2) <= st,
             cp.norm(W,'inf') + cp.norm(cp.multiply(M.Phi, W),2) <= st]
cons += [g @ x == 0]     # impose the exact first-order condition g(x') = 0 (true for every mate)
cp.Problem(cp.Maximize(g[1]*psi[2]-g[2]*psi[1]), cons).solve(solver=cp.CLARABEL, tol_gap_abs=1e-12, tol_gap_rel=1e-12, tol_feas=1e-12)
gv = g.value
print("g(x') =", gv @ x)
F = [0, 1, 2]
print("   t      L1.2(a)  L1.2(b)  L2.2(+)  L2.2(-)")
for t in [x_ for x_ in M.tgrid if x_ > 0][::6]:
    Ap, Wp = vars_[t][0].value, vars_[t][1].value
    Am, Wm = vars_[-t][0].value, vars_[-t][1].value
    Bp = (Ap - a)/t; Bm = -(Am - a)/t
    Op = (Wp - w)/t; Om = (w - Wm)/t
    # actual e: max of the two components at +-t
    def comp(A_, W_): return max(np.abs(A_).sum()+np.linalg.norm(M.mu*A_), np.abs(W_).max()+np.linalg.norm(M.Phi*W_))
    e = max(comp(Ap,Wp), comp(Am,Wm)) - 1
    lhs_a = sum((1-abs(z[j]))*abs(Bp[j]) + 2*max(-(z[j]*Bp[j]),0) for j in range(n) if j not in F) \
          + sum(2*max(-(z[j]*Bp[j] + abs(a[j])/t),0) for j in F)
    lhs_b = sum((1-abs(z[j]))*abs(Bm[j]) + 2*max(z[j]*Bm[j],0) for j in range(n) if j not in F) \
          + sum(2*max(z[j]*Bm[j] - abs(a[j])/t,0) for j in F)
    rhs = max(e,1e-300)/(c*t)
    s = np.sign(w); Lp = np.max(s*Op); Lm = np.min(s*Om)
    bnd = max(e,1e-300)/(t*sigma*np.abs(alpha))
    r1 = np.max((Lp - s*Op)/bnd); r2 = np.max((s*Om - Lm)/bnd)
    print(f"{t:9.2e}  {lhs_a/rhs:7.3f}  {lhs_b/rhs:7.3f}  {r1:7.3f}  {r2:7.3f}")
