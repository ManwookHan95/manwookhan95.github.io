"""J2-ref: is literal K-8 ("coarse peak set frozen at the input row") defective in a (U)-block, and does (FC) fix it?
One block: robust peak p (rho ~ 2..3), active WEAK PEAK k (rho = 1 + b s), active strict non-peaks l1, l2, inactive non-peak n, fine carriers.
(U)-block realization: the active carriers' ratios are set to s_m r_0 (r_0 := current frozen ratios, s_m = 1 - c eta') with kappa floating
(peak value fixed), by a fixed-point iteration on the active values (two-sided value levers).  Two frozen conventions:
  (FC)  P_f = {p}: k frozen as a non-peak;           (K8)  P_f = {p, k}: k frozen as a peak (literal K-8 at the unpushed input row).
At the realized point we compute the TRUE block scalars (threshold equation) and the TRUE ratios u_l / kappa_true (U1's kappa, Omega = all
coarse non-peaks at the realized point) and compare with the targets.  Exactness on Z_kappa requires error 0."""
import mpmath as mp, random
mp.mp.dps = 40
random.seed(5)

def scal(zeta, Phi, Pf, fine):
    """frozen scalars (theta_f, A_f) with coarse pattern Pf (coarse non-Pf are non-peaks), fine carriers true.
    If Pf is None: TRUE scalars."""
    n = len(zeta); nu = [abs(z)/p**2 for z, p in zip(zeta, Phi)]
    def AB(th):
        A = 0; B = 0
        for k in range(n):
            if Pf is None or k in fine:
                A += max(abs(zeta[k]) - th*Phi[k]**2, 0); B += Phi[k]**2*min(th, nu[k])**2
            elif k in Pf:
                A += abs(zeta[k]) - th*Phi[k]**2; B += th**2*Phi[k]**2
            else:
                B += nu[k]**2*Phi[k]**2
        return A, B
    lo, hi = mp.mpf('1e-30'), max(nu)*3
    while AB(hi)[0] <= 0: hi *= mp.mpf('0.999')
    for _ in range(250):
        mid = (lo+hi)/2
        A, B = AB(mid)
        if A*A - B > 0: lo = mid
        else: hi = mid
    th = (lo+hi)/2
    return th, AB(th)[0], nu

def kappa_of(zeta, Phi, Pf, fine, Om):
    th, A, nu = scal(zeta, Phi, Pf, fine)
    S = sum(nu[k]**2*Phi[k]**2 for k in Om)
    return A + (A*A - S)/th, th, nu

m = 2
res = {'FC': [], 'K8': []}
stat = []
for trial in range(60):
    eta = mp.mpf(10)**random.uniform(-3, -2); b = eta*mp.mpf(10)**random.uniform(-4, -2)
    # carriers: 0 = p (robust peak), 1 = k (weak peak), 2,3 = l1,l2 (active non-peaks), 4 = n (inactive non-peak), 5,6 = fine
    Phi = [mp.mpf(random.uniform(0.08, 0.3)) for _ in range(5)] + [mp.mpf(random.uniform(1e-4, 1e-3)) for _ in range(2)]
    rho = [None, 1 + b*mp.mpf(random.uniform(0.1, 1)), mp.mpf(random.uniform(0.5, 0.95)), mp.mpf(random.uniform(1 - float(b), 1 - float(b)/10)),
           mp.mpf(random.uniform(0.05, 0.5)), mp.mpf(random.uniform(0, 0.8)), mp.mpf(random.uniform(0, 0.8))]
    P = [0, 1]
    a = mp.sqrt(sum(Phi[k]**2 for k in P) + sum(rho[k]**2*Phi[k]**2 for k in range(7) if k not in P))
    rho[0] = 1 + (a - (rho[1] - 1)*Phi[1]**2)/Phi[0]**2
    if rho[0] < 1.3: continue
    sg = [random.choice([-1, 1]) for _ in range(7)]
    zeta0 = [sg[k]*rho[k]*Phi[k]**2 for k in range(7)]
    fine = {5, 6}; act = [1, 2, 3]; Om = [1, 2, 3, 4]   # route-V Omega: all coarse non-robust-peak carriers
    lam = [m*p for p in Phi]
    for conv, Pf in (('FC', {0}), ('K8', {0, 1})):
        kap0, _, _ = kappa_of(zeta0, Phi, Pf, fine, Om)
        r0 = {j: (zeta0[j]/lam[j])/kap0 for j in act}
        s_m = 1 - 3*eta            # (U)-block rescaling of the targets
        tgt = {j: s_m*r0[j] for j in act}
        z = list(zeta0)
        for it in range(200):       # fixed point: |zeta_j| = lam_j |tgt_j| kappa_f(z)
            kap, _, _ = kappa_of(z, Phi, Pf, fine, Om)
            znew = list(z)
            for j in act: znew[j] = lam[j]*tgt[j]*kap
            if max(abs(znew[j] - z[j]) for j in act) < mp.mpf('1e-35'): z = znew; break
            z = znew
        # true scalars and true ratios at the realized point
        tht, At, nut = scal(z, Phi, None, fine)
        Pt = [k for k in range(5) if nut[k] >= tht]
        Omt = [k for k in range(5) if k not in Pt]
        St = sum(nut[k]**2*Phi[k]**2 for k in Omt)
        kt = At + (At*At - St)/tht
        err = max(abs((z[j]/lam[j])/kt - tgt[j])/abs(tgt[j]) for j in act)
        res[conv].append(err)
        if conv == 'FC':
            stat.append((nut[1]/tht, Pt))
        if conv == 'K8':
            # size comparison: eta' * Phi_k^2 scale
            res.setdefault('K8scale', []).append(err/(eta*Phi[1]**2))
print('(U)-block realization from the UNPUSHED row, 60 random blocks:')
print('  true status of the former weak peak at the (FC)-realized point: max = %.6f (must be < 1)' % max(float(s[0]) for s in stat))
print('  true coarse peak set at the (FC)-realized point is {p} in %d/%d cases' % (sum(1 for s in stat if s[1] == [0]), len(stat)))
print('  K8 error / (eta Phi_k^2): min = %.3f, max = %.3f' % (float(min(res['K8scale'])), float(max(res['K8scale']))))
for conv in ('FC', 'K8'):
    v = res[conv]
    print('  %-3s: max relative error |true ratio - target| = %.3e, min = %.3e' % (conv, float(max(v)), float(min(v))))
