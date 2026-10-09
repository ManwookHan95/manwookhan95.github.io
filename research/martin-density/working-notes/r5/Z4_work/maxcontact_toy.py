"""Z4 toy (finite, degenerate -> tests signs/algebra only): maximal contact z = +1 off F = {0,1}, one block, K carriers with
private 2-point signatures (all swallowed, eps = +1) and targets of both signs, so peaks of both signs occur.
Checks on SOCP-optimal two-sided decompositions of f +- t g, g a (near-boundary) mate:
 (c1) peak identity  vs*tau/lam - Dd*M = |om+| + |om-|   (vs = sign w(k); eps = +1)
 (c2) anti-sign peak (vs = -1):        Dd*M <= (tau)_- / lam                       [Step 3, upper bound]
 (c3) swallowing-sign peak (vs = +1):  Dd*M >= tau/lam - t/(sigma*|alpha|)        [Step 3, lower bound]
 (c4) budget sum_{j notin F} 2 (Delta B_j)_- <= t/q0.
"""
import numpy as np, cvxpy as cp, warnings, sys
warnings.filterwarnings('ignore')
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 3
rng = np.random.default_rng(seed)
n, K = 14, 5
U = rng.standard_normal((n, 3)); U *= 0.15/np.linalg.norm(U, 2)
a = np.zeros(n); a[0], a[1] = 0.6, -0.3
a = a/(np.abs(a).sum() + np.linalg.norm(U.T @ a))
z = np.ones(n); z[0], z[1] = 1., -1.
sig = [[4+2*k, 5+2*k] for k in range(K)]
Y = np.zeros((K, n))
for l in range(K):
    Y[l, 2 + (l % 2)] = (1 if l % 2 == 0 else -1)*rng.uniform(.5, 1)   # targets on shared coords 2,3 with both signs
    Y[l, 0] = rng.uniform(-.5, .5); Y[l, 1] = rng.uniform(-.5, .5)
    if l >= 2: Y[l, sig[l-2][1]] = rng.uniform(-.05, .05)             # finer targets touch a coarser signature
delta = 0.3; prof = np.array([.5, .25])
u = np.zeros((K, n))
for l, S in enumerate(sig):
    v = Y[l].copy(); v[S] += delta*prof
    u[l] = v/(np.abs(v).sum() + np.linalg.norm(U.T @ v))
Phi = 0.35**(np.arange(K)+1); lam = Phi.copy()
L = (lam[:, None]*u).T
def pstar(h, ret=False):
    A = cp.Variable(n); W = cp.Variable(K); s = cp.Variable()
    cons = [A + L @ W == h, cp.norm(A, 1) + cp.norm(U.T @ A, 2) <= s, cp.norm(W, 'inf') + cp.norm(cp.multiply(Phi, W), 2) <= s]
    pr = cp.Problem(cp.Minimize(s), cons); pr.solve(solver='CLARABEL', tol_gap_abs=1e-11, tol_gap_rel=1e-11, tol_feas=1e-11)
    return (pr.value, A.value, W.value) if ret else pr.value
nu = np.linalg.norm(U.T @ a); e = U.T @ a/nu; zhat = z + U @ e
Rz = lam*(u @ zhat)
Wv = cp.Variable(K); pr = cp.Problem(cp.Maximize(Rz @ Wv), [cp.norm(Wv, 'inf') + cp.norm(cp.multiply(Phi, Wv), 2) <= 1]); pr.solve(solver='CLARABEL')
w = Wv.value; q0 = 1/(1 + pr.value); xi = q0*zhat; f = a + L @ w; sigma = 1 - q0
M = np.abs(w).max(); C = np.linalg.norm(Phi*w); peaks = np.isclose(np.abs(w), M, atol=1e-6)
zeta = lam*(u @ xi); alpha = zeta/sigma - Phi**2*w/C
print(f"seed {seed} q0 {q0:.4f} M+C {M+C:.6f} p*(f)={pstar(f):.7f} u(zhat) {np.round(u@zhat,3)} peaks {np.where(peaks)[0]} sign {np.sign(w[peaks])} alpha {np.round(alpha[peaks],4)}")
SG = np.concatenate([-np.logspace(-2.5, 1.5, 24), np.logspace(-2.5, 1.5, 24)])
def contractive(g): return max(pstar(f + s*g) - np.sqrt(1+s*s) for s in SG) <= 2e-9
def to_boundary(g0):
    lo, hi = 0., 1.
    while contractive(hi*g0): hi *= 2
    for _ in range(16):
        mid = (lo+hi)/2
        lo, hi = (mid, hi) if contractive(mid*g0) else (lo, mid)
    return lo
notF = list(range(2, n)); worst = dict(c1=0., c2=-1., c3=-1., c4=-1.)
for trial in range(3):
    g0 = rng.standard_normal(n) + 2*rng.standard_normal()*u[rng.integers(K)]
    g0 -= (g0 @ xi)/(a @ xi)*a
    g = 0.999*to_boundary(g0)*g0
    for t in [3e-2, 1e-2, 3e-3]:
        vp, Ap, Wp = pstar(f + t*g, True); vm, Am, Wm = pstar(f - t*g, True)
        Bp, Bm = (Ap - a)/t, (a - Am)/t; Op, Om = (Wp - w)/t, (w - Wm)/t
        dB = Bp - Bm; dth = lam*(Op - Om); tau = -dth
        dp = (1 - np.abs(w + t*Op).max()/M)/t; dm = (np.abs(w - t*Om).max()/M - 1)/t; Dd = dp - dm
        omp, omm = Op + dp*w, Om + dm*w
        worst['c4'] = max(worst['c4'], sum(2*max(-dB[j], 0) for j in notF) - t/q0)
        for k in np.where(peaks)[0]:
            vs = np.sign(w[k])
            worst['c1'] = max(worst['c1'], abs(vs*tau[k]/lam[k] - Dd*M - (abs(omp[k]) + abs(omm[k]))))
            if vs < 0: worst['c2'] = max(worst['c2'], Dd*M - max(-tau[k], 0)/lam[k])
            elif abs(alpha[k]) > 1e-6: worst['c3'] = max(worst['c3'], tau[k]/lam[k] - t/(sigma*abs(alpha[k])) - Dd*M)
print("max residual c1 (should be ~0):", f"{worst['c1']:.2e}", "| max violations c2,c3,c4 (should be <= ~1e-6):",
      f"{worst['c2']:.2e} {worst['c3']:.2e} {worst['c4']:.2e}")
