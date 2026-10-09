"""Toy finite model (referee, independent of the authors' scripts): F = {0,1}, EVERY other base coordinate a contact (|z| = 1),
one block of K carriers with private 2-point signatures carrying OPPOSITE contact signs (sign-mixed room, Thm B± setting),
plus targets touching coarser signatures.  Checks on SOCP-optimal two-sided decompositions of f +- t g:
 (1) switching budget sum_{j notin F} phi_z(Delta B) <= t/q0;  (2) Lemma 1.4: theta_l|Dc_l| <= E_l + 2 sum_{l'>l} kappa|Dc_l'|;
 (3) peak signs sigma_k omega_+(k) <= 0 <= sigma_k omega_-(k) and (2.1.1); (4) d-identity of Lemma 2.2.
Finite models are degenerate (normer faces), so this tests signs/algebra only."""
import numpy as np, cvxpy as cp, warnings
warnings.filterwarnings('ignore')
rng = np.random.default_rng(7)
n, K = 14, 4
U = rng.standard_normal((n, n)); U *= 0.1/np.linalg.norm(U, 2)
a = np.zeros(n); a[0], a[1] = 0.6, -0.3
a = a/(np.abs(a).sum() + np.linalg.norm(U.T @ a))
z = np.array([1., -1.] + list(rng.choice([-1., 1.], n-2)))
sigsets = [[2+2*k, 3+2*k] for k in range(K)]           # S_l = {2+2l, 3+2l}
for S in sigsets: z[S[0]], z[S[1]] = 1., -1.             # opposite signs on each signature set
Y = np.zeros((K, n))
Y[0, 10] = 1.0; Y[1, 11] = .7; Y[1, 2] = .2; Y[2, 12] = 1.; Y[2, 4] = -.3; Y[3, 13] = .5; Y[3, 0] = .5
delta = 0.2; prof = np.array([2.**-1, 2.**-2])
u = np.zeros((K, n))
for l, S in enumerate(sigsets):
    v = Y[l].copy(); v[S] += delta*prof
    u[l] = v/(np.abs(v).sum() + np.linalg.norm(U.T @ v))
Phi = 0.4**(np.arange(K)+1); lam = Phi.copy()
L = (lam[:, None]*u).T
def pstar(phi_, ret=False):
    A = cp.Variable(n); W = cp.Variable(K); s = cp.Variable()
    cons = [A + L @ W == phi_, cp.norm(A, 1) + cp.norm(U.T @ A, 2) <= s, cp.norm(W, 'inf') + cp.norm(cp.multiply(Phi, W), 2) <= s]
    pr = cp.Problem(cp.Minimize(s), cons); pr.solve(solver='CLARABEL', tol_gap_abs=1e-11, tol_gap_rel=1e-11, tol_feas=1e-11)
    return (pr.value, A.value, W.value) if ret else pr.value
nu = np.linalg.norm(U.T @ a); e = U.T @ a/nu; zhat = z + U @ e
Rz = lam*(u @ zhat)
W = cp.Variable(K); pr = cp.Problem(cp.Maximize(Rz @ W), [cp.norm(W, 'inf') + cp.norm(cp.multiply(Phi, W), 2) <= 1]); pr.solve(solver='CLARABEL')
w = W.value; q0 = 1/(1 + pr.value); xi = q0*zhat; f = a + L @ w; sig = 1 - q0
M = np.abs(w).max(); C = np.linalg.norm(Phi*w); peaks = np.isclose(np.abs(w), M, atol=1e-7)
zeta = lam*(u @ xi); alpha = zeta/sig - Phi**2*w/C
print(f"q0 {q0:.4f} M {M:.4f} C {C:.4f} M+C {M+C:.6f} p*(f) {pstar(f):.8f} peaks {np.where(peaks)[0]} w {np.round(w,4)} alpha_peaks {np.round(alpha[peaks],4)}")
SG = np.concatenate([-np.logspace(-2.5, 1.5, 30), np.logspace(-2.5, 1.5, 30)])
def contractive(g): return max(pstar(f + s*g) - np.sqrt(1+s*s) for s in SG) <= 2e-9
def to_boundary(g0):
    lo, hi = 0., 1.
    while contractive(hi*g0): hi *= 2
    for _ in range(18):
        mid = (lo+hi)/2
        lo, hi = (mid, hi) if contractive(mid*g0) else (lo, mid)
    return lo
phi = lambda zz, x: abs(x) - zz*x
F = [0, 1]; notF = [j for j in range(n) if j not in F]
theta = np.array([min((u[l, S]*(1 + sgn*z[S])).sum() for sgn in (1, -1)) for l, S in enumerate(sigsets)])  # u_l(s)=v_l(s) on S_l (targets avoid own S_l)
kappa = np.array([[np.abs(u[lp, sigsets[l]]).sum() for l in range(K)] for lp in range(K)])   # kappa[l', l]
for trial in range(3):
    g0 = rng.standard_normal(n); g0 += 3*rng.standard_normal()*u[rng.integers(K)]
    g0 -= (g0 @ xi)/(a @ xi)*a
    c = to_boundary(g0); g = 0.999*c*g0
    for t in [3e-2, 1e-2, 3e-3]:
        vp, Ap, Wp = pstar(f + t*g, True); vm, Am, Wm = pstar(f - t*g, True)
        Bp, Bm = (Ap - a)/t, (a - Am)/t; Op, Om = (Wp - w)/t, (w - Wm)/t
        dB = Bp - Bm; dc = lam*(Op - Om)
        bud = sum(phi(z[j], dB[j]) for j in notF)
        pin = max(theta[l]*abs(dc[l]) - (sum(phi(z[s], dB[s]) for s in sigsets[l]) + 2*sum(kappa[lp, l]*abs(dc[lp]) for lp in range(l+1, K))) for l in range(K))
        dp = (1 - np.abs(Wp).max()/M)/t; dm = (np.abs(Wm).max()/M - 1)/t
        op, om = Op + dp*w, Om + dm*w; sk = np.sign(w)
        sgn_viol = max(np.max(sk[peaks]*op[peaks]), np.max(-sk[peaks]*om[peaks]))
        ident = np.max(np.abs((np.abs(op) + np.abs(om) - (-sk*(Op - Om) - (dp - dm)*M))[peaks]))
        dd = (dp - dm)*M - (Phi*w*dc).sum()/C          # Lemma 2.2 with m = 1:  Delta d M = (1/C) sum Phi w Dc + r, |r| <= 2t/sigma
        print(f"trial {trial} t={t:.0e}: p*(+)-s(t) {vp-np.sqrt(1+t*t):+.1e} budget {bud:.2e} <= t/q0 {t/q0:.2e} | pin viol {pin:+.1e} | "
              f"peak-sign viol {sgn_viol:+.1e} ident err {ident:.1e} | d-identity |r| {abs(dd):.2e} <= 2t/sig {2*t/sig:.2e} | sum|dc|/t {np.abs(dc).sum()/t:.3f}")
