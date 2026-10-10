"""Referee check of Lemma R-kt on random blocks (50 digits):
 a := A/theta, k := kappa/theta, R^2 := m^2 sum_Omega (u_l/kappa)^2, s_f := sum_{Q\Omega} nu^2 Phi^2/theta^2:
   a^2 = Phi_P^2 + k^2 R^2 + s_f,   k = a + Phi_P^2 + s_f,   rho_l = m |u_l/kappa| k / Phi_l (l in Omega),  R < 1, a > k R."""
import mpmath as mp, random
mp.mp.dps = 50
random.seed(11)
src = open("status_rigidity.py").read().split("# ---- block:")[0]
exec(src)
worst = [mp.mpf(0)]*3; n = 0; minRgap = mp.mpf(1); minaKR = mp.mpf(10)
for trial in range(300):
    nn = random.randint(4, 9); m = random.randint(1, 3)
    Phi = [mp.mpf(2)**(-(m+k+1))*mp.mpf(random.uniform(0.2, 1)) for k in range(nn)]
    zeta = [mp.mpf(random.choice([-1,1]))*Phi[k]**2*mp.mpf(random.uniform(0.0, 3.0)) for k in range(nn)]
    A, th, M, C, nu = solve_block(zeta, Phi)
    P = [k for k in range(nn) if nu[k] >= th]; Q = [k for k in range(nn) if nu[k] < th]
    if not P or not Q: continue
    Omega = [k for k in Q if random.random() < 0.7] or [Q[0]]
    Sf = mp.fsum((nu[k]*Phi[k])**2 for k in Q if k not in Omega)
    PhiP2 = mp.fsum(Phi[k]**2 for k in P)
    kap = (A*(A+th) - mp.fsum((nu[k]*Phi[k])**2 for k in Omega))/th
    lam = [m*Phi[k] for k in range(nn)]
    r = {k: (zeta[k]/lam[k])/kap for k in Omega}
    R2 = m**2*mp.fsum(r[k]**2 for k in Omega)
    a = A/th; kk = kap/th; sf = Sf/th**2
    e1 = abs(a**2 - (PhiP2 + kk**2*R2 + sf)); e2 = abs(kk - (a + PhiP2 + sf))
    e3 = max(abs(nu[k]/th - m*abs(r[k])*kk/Phi[k]) for k in Omega)
    worst = [max(worst[0], e1), max(worst[1], e2), max(worst[2], e3)]
    minRgap = min(minRgap, 1 - mp.sqrt(R2)); minaKR = min(minaKR, a - kk*mp.sqrt(R2)); n += 1
print('blocks', n, 'max errors', [mp.nstr(x, 3) for x in worst], 'min(1-R)', mp.nstr(minRgap, 4), 'min(a-kR)', mp.nstr(minaKR, 4))
