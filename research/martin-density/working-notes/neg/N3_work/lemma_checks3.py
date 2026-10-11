import numpy as np, cvxpy as cp
import sqrt_mu_check as M
# Same as lemma_checks2 but with a grid restricted to t >= 1e-3, in long double post-processing, to separate
# genuine violations from solver tolerance at tiny budgets e ~ t^2/2.
m = 1e-4
a, z, xhat, w, f, psi, zeta = M.build_row(m)
sig_hat = zeta @ w; c = 1/(1+sig_hat); sigma = c*sig_hat
C = np.linalg.norm(M.Phi*w); alpha = zeta/sig_hat - M.Phi**2*w/C
n, nb = M.n, M.nb; x = xhat*c
grid = np.logspace(-3, 0.5, 30); grid = np.concatenate([grid, -grid])
g = cp.Variable(n); vars_ = {}; cons = []
for t in grid:
    A = cp.Variable(n); W = cp.Variable(nb); st = np.sqrt(1+t*t); vars_[t] = (A, W)
    cons += [A + M.Rstar @ W == f + t*g, cp.norm(A,1) + cp.norm(cp.multiply(M.mu, A),2) <= st,
             cp.norm(W,'inf') + cp.norm(cp.multiply(M.Phi, W),2) <= st]
cons += [g @ x == 0]
cp.Problem(cp.Maximize(g[1]*psi[2]-g[2]*psi[1]), cons).solve(solver=cp.CLARABEL, tol_gap_abs=1e-12, tol_gap_rel=1e-12, tol_feas=1e-12)
worst = 0
for t in [x_ for x_ in grid if x_ > 0]:
    Ap, Wp = vars_[t][0].value, vars_[t][1].value; Am, Wm = vars_[-t][0].value, vars_[-t][1].value
    res = max(np.abs(Ap + M.Rstar@Wp - f - t*g.value).max(), np.abs(Am + M.Rstar@Wm - f + t*g.value).max())
    def comp(A_, W_): return max(np.abs(A_).sum()+np.linalg.norm(M.mu*A_), np.abs(W_).max()+np.linalg.norm(M.Phi*W_))
    e = max(comp(Ap,Wp), comp(Am,Wm)) - 1
    Op = (Wp - w)/t; Om = (w - Wm)/t; s = np.sign(w)
    bnd = e/(t*sigma*np.abs(alpha))
    r = max(np.max((np.max(s*Op) - s*Op)/bnd), np.max((s*Om - np.min(s*Om))/bnd))
    worst = max(worst, r)
print("Lemma 2.2 on t in [1e-3, 3.2]: max ratio =", round(worst, 4), "(<= 1 expected)")
