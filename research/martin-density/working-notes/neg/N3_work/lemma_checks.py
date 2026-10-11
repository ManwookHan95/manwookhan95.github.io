import numpy as np, cvxpy as cp
import sqrt_mu_check as M
m = 1e-4
a, z, xhat, w, f, psi, zeta = M.build_row(m)
sig_hat = zeta @ w; c = 1/(1+sig_hat); sigma = c*sig_hat
C = np.linalg.norm(M.Phi*w); alpha = zeta/sig_hat - M.Phi**2*w/C
n, nb = M.n, M.nb
# solve the max-Lambda problem and keep the decompositions
g = cp.Variable(n); vars_ = {}
cons = []
for t in M.tgrid:
    A = cp.Variable(n); W = cp.Variable(nb); st = np.sqrt(1+t*t)
    vars_[t] = (A, W)
    cons += [A + M.Rstar @ W == f + t*g, cp.norm(A,1) + cp.norm(cp.multiply(M.mu, A),2) <= st,
             cp.norm(W,'inf') + cp.norm(cp.multiply(M.Phi, W),2) <= st]
cp.Problem(cp.Maximize(g[1]*psi[2]-g[2]*psi[1]), cons).solve(solver=cp.CLARABEL)
gv = g.value
print("g(xhat') =", gv @ xhat)
F = [0, 1, 2]           # support coordinates of f' (0 and the two banks)
worst12, worst22 = 0, 0
for t in [x for x in M.tgrid if x > 0][::7]:
    Ap, Wp = vars_[t][0].value, vars_[t][1].value
    Am, Wm = vars_[-t][0].value, vars_[-t][1].value
    Bp = (Ap - a)/t; Bm = -(Am - a)/t          # A+ = a + t B+,  A- = a - t B-
    Op = (Wp - w)/t; Om = (w - Wm)/t           # W+ = w + t Om+, W- = w - t Om-
    e = np.sqrt(1+t*t) - 1
    # Lemma 1.2 (a),(b)
    lhs_a = sum((1-abs(z[j]))*abs(Bp[j]) + 2*max(-(z[j]*Bp[j]),0) for j in range(n) if j not in F) \
          + sum(2*max(-(z[j]*Bp[j] + abs(a[j])/t),0) for j in F)
    lhs_b = sum((1-abs(z[j]))*abs(Bm[j]) + 2*max(z[j]*Bm[j],0) for j in range(n) if j not in F) \
          + sum(2*max(z[j]*Bm[j] - abs(a[j])/t,0) for j in F)
    rhs = e/(c*t)
    worst12 = max(worst12, lhs_a/rhs, lhs_b/rhs)
    # Lemma 2.2 on all carriers (all are peaks here)
    s = np.sign(w)
    Lp = np.max(s*Op); Lm = np.min(s*Om)
    epsp = Lp - s*Op; epsm = s*Om - Lm
    bound = e/(t*sigma*np.abs(alpha))
    worst22 = max(worst22, np.max(epsp/bound), np.max(epsm/bound))
print("Lemma 1.2: max ratio lhs/rhs over grid =", worst12, "(must be <= 1 up to solver tolerance)")
print("Lemma 2.2: max ratio eps/bound over grid =", worst22, "(must be <= 1 up to solver tolerance)")
