"""J2 numerics (sanity only): merged Step A in a one-block toy, started at the UNPUSHED row.
Block: robust peak p (two-sided: its |zeta| can move both ways), active WEAK PEAK k (rho in (1,1+b)) with a ONE-SIDED resource
(|zeta_k| may only increase: a bank raising eps_k val_k with eps_k = vs_k, the bad case of K1-ref R-8), active strict non-peak l
(two-sided), inactive nearly neutral carrier n held at value 0 (KN-1/P-HOLD).  Targets: ratios r''_k, r''_l with frozen status of k equal
to 1 - mu/2 (floor form with sigma = Phi_p^2, R^2 = m^2 (r_k^2 + r_l^2)), r''_l = current ratio of l.  Frozen convention (FC): P_f = {p}.
Claim tested: the frozen equations have a solution with |zeta_k| >= its initial value (one-sided resource respected) obtained by raising
the peak (kappa / threshold lever) -- no Step-0 push -- and at the solution the frozen block equals the true block (Lemma J2.1(c))."""
import numpy as np
from scipy.optimize import brentq, fsolve
rng = np.random.default_rng(11)
m = 2

def true_block(zeta, Phi):
    nu = np.abs(zeta) / Phi**2
    def Psi(th):
        A = np.maximum(np.abs(zeta) - th * Phi**2, 0).sum(); B = (Phi**2 * np.minimum(th, nu)**2).sum(); return A**2 - B
    th = brentq(Psi, 1e-14 * nu.max(), nu.max(), xtol=1e-16, rtol=1e-15, maxiter=500)
    return th, np.maximum(np.abs(zeta) - th * Phi**2, 0).sum(), nu

def frozen(zeta, Phi, Pf):
    nu = np.abs(zeta) / Phi**2
    def Psi(th):
        A = (np.abs(zeta[Pf]) - th * Phi[Pf]**2).sum(); B = th**2 * (Phi[Pf]**2).sum() + (nu[~Pf]**2 * Phi[~Pf]**2).sum(); return A**2 - B
    hi = np.abs(zeta[Pf]).sum() / (Phi[Pf]**2).sum() * (1 - 1e-13)
    th = brentq(Psi, 1e-14 * hi, hi, xtol=1e-16, rtol=1e-15, maxiter=500)
    return th, (np.abs(zeta[Pf]) - th * Phi[Pf]**2).sum(), nu

def Kf(sig, R2): return (sig + np.sqrt(sig**2 * R2 + sig * (1 - R2))) / (1 - R2)

ok = 0; worst_cons = 0.0; worst_scale = 0.0
for trial in range(300):
    b, mu = 1e-3, 0.02
    Phi = rng.uniform(0.05, 0.25, 4)            # p, k, l, n
    rho = np.array([np.nan, 1 + b * rng.uniform(0.1, 0.9), rng.uniform(0.3, 0.8), 0.0])
    # choose rho_p so that the true block with theta = 1 is consistent: a = (rho_p - 1)Phi_p^2 + (rho_k - 1)Phi_k^2 = sqrt(Phi_p^2 + Phi_k^2 + rho_l^2 Phi_l^2)
    a = np.sqrt(Phi[0]**2 + Phi[1]**2 + rho[2]**2 * Phi[2]**2)
    rho[0] = 1 + (a - (rho[1] - 1) * Phi[1]**2) / Phi[0]**2
    zeta0 = rho * Phi**2; zeta0[3] = 0.0
    Pf = np.array([True, False, False, False])
    thf, Af, nu = frozen(zeta0, Phi, Pf)
    lam = m * Phi; u0 = zeta0 / lam
    Om = np.array([False, True, True, True])
    kap0 = Af + (Af**2 - (nu[Om]**2 * Phi[Om]**2).sum()) / thf
    r0 = u0 / kap0
    # target ratios: r_l unchanged; r_k chosen so that frozen status of k = 1 - mu/2 at sigma = Phi_p^2
    sig = Phi[0]**2
    g = lambda rk: m * rk * Kf(sig, m**2 * (rk**2 + r0[2]**2)) / Phi[1] - (1 - mu / 2)
    rk_t = brentq(g, 1e-12, r0[1]); rl_t = r0[2]
    # realize: unknowns (s = scale of the peak, zeta_k, zeta_l); for each s solve the two ratio equations; then pick the smallest s with zeta_k >= zeta_k^0
    def solve_given(s):
        def F(x):
            z = np.array([zeta0[0] * s, x[0], x[1], 0.0])
            t, A, n = frozen(z, Phi, Pf)
            kap = A + (A**2 - (n[Om]**2 * Phi[Om]**2).sum()) / t
            return [z[1] / lam[1] / kap - rk_t, z[2] / lam[2] / kap - rl_t]
        x = fsolve(F, [zeta0[1], zeta0[2]], xtol=1e-14)
        return x
    # by 1-homogeneity zeta_k(s) = s * zeta_k(1): find s = zeta_k^0 / zeta_k(1) (>= 1 means a peak RAISE)
    x1 = solve_given(1.0)
    s_star = max(1.0, zeta0[1] / x1[0])
    xs = solve_given(s_star)
    z = np.array([zeta0[0] * s_star, xs[0], xs[1], 0.0])
    assert z[1] >= zeta0[1] * (1 - 1e-9), "one-sided resource violated"
    thf2, Af2, nu2 = frozen(z, Phi, Pf); th2, A2, nut = true_block(z, Phi)
    cons = (nu2[0] >= thf2) and all(nu2[i] <= thf2 for i in (1, 2, 3))
    if cons:
        ok += 1
        worst_cons = max(worst_cons, abs(thf2 - th2) / th2)
        worst_scale = max(worst_scale, s_star - 1)
        assert abs(nut[1] / th2 - (1 - mu / 2)) < 1e-6, (nut[1] / th2)
print(f"trials consistent at the realized point: {ok}/300")
print(f"max |theta_frozen - theta_true|/theta at the realized point: {worst_cons:.2e}")
print(f"max relative peak raise s* - 1 used (threshold/kappa lever): {worst_scale:.3e}  (compare mu/2 + b = {0.02/2 + 1e-3:.3e})")
print("true status of the former weak peak at the realized point = 1 - mu/2 (asserted to 1e-6)")
