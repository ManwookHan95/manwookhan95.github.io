# N4: test of Lemma 11.5(b) (block truncation with exact first-order correction).
# Block dual norm N(w) = ||w||_inf + ||D w||_2, D = diag(Phi).
import numpy as np
rng = np.random.default_rng(3)
def Nn(w, Phi): return np.max(np.abs(w)) + np.linalg.norm(Phi*w)
viol_small = viol_all = tot = 0; worst = 0.0
for trial in range(3000):
    n = rng.integers(8, 40)
    Phi = rng.uniform(0.3, 0.9) ** np.arange(1, n+1)
    w = rng.uniform(-1, 1, size=n)
    npk = rng.integers(1, 4); pk = rng.choice(n, npk, replace=False)
    w[pk] = np.sign(w[pk]) * 1.0                 # peak set with |w_k| = 1 = M (before normalisation)
    w = np.clip(w, -1, 1)
    # make some near-peak coordinates (small gaps)
    near = rng.choice(n, rng.integers(0, 5), replace=False)
    for k in near:
        if k not in pk: w[k] = np.sign(w[k]) * (1 - 10.0**(-rng.uniform(1, 4)))
    w /= Nn(w, Phi)
    M = np.max(np.abs(w)); C = np.linalg.norm(Phi*w)
    peak = np.isclose(np.abs(w), M, rtol=0, atol=1e-15)
    gap = M - np.abs(w)
    # omega vanishing on the peak, small near the peak (so that v is a local mate)
    omega = rng.normal(size=n) * np.minimum(1.0, np.sqrt(gap)) ; omega[peak] = 0.0
    d = (Phi*w) @ (Phi*omega) / C
    v = omega - d*w
    # scale so that local mate inequality holds on |t|<=tau with margin
    for _ in range(60):
        ts = np.linspace(-0.3, 0.3, 61)
        ok = all(Nn(w + t*v, Phi) <= np.sqrt(1+t*t) + 1e-13 for t in ts)
        if ok: break
        omega *= 0.7; d = (Phi*w) @ (Phi*omega) / C; v = omega - d*w
    if not ok: continue
    offpk = np.where((~peak) & (np.abs(w) > 1e-3))[0]
    if len(offpk) == 0: continue
    k0 = offpk[np.argmax(gap[offpk])]; g0 = gap[k0]
    for (gam, K) in [(g0/2, n), (g0/10, n//2), (1e-3, n-1)]:
        S = np.zeros(n, bool); S[:K] = True; S &= (gap >= gam); S[k0] = True
        om2 = omega * S
        c = (Phi*w) @ (Phi*(omega - om2)) / (Phi[k0]**2 * w[k0])
        if abs(c) > 1: continue
        om2 = om2.copy(); om2[k0] += c
        v2 = om2 - d*w
        Delta = Phi*(om2 - omega)
        t0 = g0 / (4*(abs(d)*M + np.max(np.abs(omega)) + 2))
        t1 = C / (2*np.linalg.norm(Phi*(omega - d*w)) + 2)
        coef = 2*(np.linalg.norm(Phi*omega)*np.linalg.norm(Delta) + np.linalg.norm(Delta)**2)/C
        for t in np.concatenate([np.linspace(-min(t0,t1), min(t0,t1), 25), np.linspace(-3, 3, 25)]):
            if t == 0: continue
            tot += 1
            diff = Nn(w + t*v2, Phi) - Nn(w + t*v, Phi)
            if abs(t) <= min(t0, t1):
                if diff > coef*t*t + 1e-12: viol_small += 1
                if coef > 1e-14: worst = max(worst, diff/(coef*t*t))
            if diff > abs(t)*(abs(c) + np.linalg.norm(Delta)) + 1e-12: viol_all += 1
print("tests:", tot, " violations of second-order bound on |t|<=min(t0,t1):", viol_small,
      " violations of first-order bound (all t):", viol_all, " max diff/(coef t^2):", round(worst, 4))
