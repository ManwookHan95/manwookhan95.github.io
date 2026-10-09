# Check Lemma T2(a),(b): quantitative Lipschitz and raising bounds for the block threshold.
import numpy as np
src = open('threshold_check.py').read().split("errs = []")[0]
exec(src)
rng = np.random.default_rng(11)
viol_b = 0; viol_a = 0; viol_up = 0; nb = na = 0
for trial in range(3000):
    n = 14
    Phi = 2.0**(-np.arange(1, n+1)) * rng.uniform(0.3, 1.0, n)
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.3, 2.5, n)
    th, A = theta_eq(zeta, Phi)
    nu = np.abs(zeta)/Phi**2
    phi = np.sum(Phi**2)
    pk = [k for k in range(n) if nu[k] >= th]
    k0 = max(pk, key=lambda k: nu[k]); phi0 = Phi[k0]**2; h0 = min(1.0, nu[k0]-th)
    C1 = (1 + 2*(th+1)/A)/phi0
    # (b): raise at a random peak c by s with perturbation E elsewhere
    c = pk[rng.integers(len(pk))]
    s = A*10**rng.uniform(-6, -1)
    Emax = A*s/(8*(A+th+1))
    pert = rng.normal(size=n); pert[c] = 0
    pert *= rng.uniform(0, 1)*Emax/np.sum(np.abs(pert))
    z2 = zeta + pert; z2[c] = zeta[c] + np.sign(zeta[c])*s
    th2, A2 = theta_eq(z2, Phi)
    lb = min(1.0, A*s/(8*phi*(A+th+1)))
    nb += 1
    if th2 - th < lb*(1-1e-9): viol_b += 1
    E = np.sum(np.abs(pert))
    if C1*(s+E) < h0 and th2 - th > C1*(s+E)*(1+1e-9): viol_up += 1
    # (a): Lipschitz
    E = min(h0, th)/C1*rng.uniform(0.01, 0.99)
    pert = rng.normal(size=n); pert *= E/np.sum(np.abs(pert))
    z3 = zeta + pert
    if np.all(np.sign(z3) == np.sign(zeta)) or True:
        th3, A3 = theta_eq(z3, Phi); na += 1
        if abs(th3 - th) > C1*E*(1+1e-9): viol_a += 1
print("T2(b) lower-bound violations:", viol_b, "of", nb)
print("T2(b) upper-bound violations:", viol_up)
print("T2(a) Lipschitz violations:", viol_a, "of", na)
