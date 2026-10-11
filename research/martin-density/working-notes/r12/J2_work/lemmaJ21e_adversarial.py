"""Adversarial check of Lemma J2.1(e): under 6 b Phi_W^2 <= Phi_Pf^2, 2 b Phi_W^2 <= a, rho in [1, 1+b] on W', rho <= 1 on Q_f \\ W':
   Psi_f(0+) > 0,  theta (1 - 3 b Phi_W^2/Phi_Pf^2) <= theta_f <= theta,  |A_f - A| <= 4 b theta Phi_W^2/Phi_Pf^2.
Random blocks with extreme weight ratios, many weak peaks, b up to the admissible limit."""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(5)

def frozen(zeta, Phi, Pf):
    nu = np.abs(zeta) / Phi**2
    A0 = lambda th: (np.abs(zeta[Pf]) - th * Phi[Pf]**2).sum()
    Psi = lambda th: A0(th)**2 - (th**2 * (Phi[Pf]**2).sum() + (nu[~Pf]**2 * Phi[~Pf]**2).sum())
    hi = np.abs(zeta[Pf]).sum() / (Phi[Pf]**2).sum() * (1 - 1e-13)
    psi0 = A0(0.0)**2 - (nu[~Pf]**2 * Phi[~Pf]**2).sum()
    th = brentq(Psi, 1e-15 * hi, hi, xtol=1e-17, rtol=1e-15, maxiter=1000)
    return th, A0(th), psi0

viol = 0; tested = 0; worst = 0.0; worstA = 0.0
for trial in range(20000):
    nP = rng.integers(1, 4); nW = rng.integers(1, 6); nQ = rng.integers(0, 6)
    K = nP + nW + nQ
    Phi = np.exp(rng.uniform(np.log(1e-3), np.log(0.3), K))
    b = 10**rng.uniform(-6, -1)
    rho = np.concatenate([np.full(nP, np.nan), 1 + b * rng.uniform(0, 1, nW), rng.uniform(0, 1, nQ)])
    # enforce the threshold equation with theta = 1 via the first robust peak
    P = np.zeros(K, bool); P[:nP + nW] = True
    rho[1:nP] = 1 + rng.uniform(0.1, 3.0, nP - 1)
    a = np.sqrt((Phi[P]**2).sum() + (rho[~P]**2 * Phi[~P]**2).sum())
    rest = ((rho[1:nP + nW] - 1) * Phi[1:nP + nW]**2).sum()
    rho0 = 1 + (a - rest) / Phi[0]**2
    if rho0 <= 1: continue
    rho[0] = rho0
    PhiW2 = (Phi[nP:nP + nW]**2).sum(); PhiPf2 = (Phi[:nP]**2).sum()
    if not (6 * b * PhiW2 <= PhiPf2 and 2 * b * PhiW2 <= a): continue
    zeta = rho * Phi**2
    Pf = np.zeros(K, bool); Pf[:nP] = True
    thf, Af, psi0 = frozen(zeta, Phi, Pf)
    tested += 1
    A = ((rho[P] - 1) * Phi[P]**2).sum()     # true A with theta = 1
    r1 = (1 - thf) / (b * PhiW2 / PhiPf2)
    r2 = abs(Af - A) / (b * PhiW2 / PhiPf2)
    worst = max(worst, r1); worstA = max(worstA, r2)
    if psi0 <= 0 or thf > 1 + 1e-12 or r1 > 3 + 1e-9 or r2 > 4 + 1e-9: viol += 1
print(f"tested {tested} admissible blocks; violations of Lemma J2.1(e): {viol}")
print(f"max (theta - theta_f)/(theta b Phi_W^2/Phi_Pf^2) = {worst:.4f}  (bound 3);  max |A_f - A|/(theta b Phi_W^2/Phi_Pf^2) = {worstA:.4f}  (bound 4)")
