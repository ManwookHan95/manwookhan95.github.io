"""Independent elementary checks for Z2 (referee). phi-calculus, theta-split (Lemma 2.3, with the sharper t/(2q0) form),
alternating-sign room bound (1.3(c)), unified triangular system (Lemma 2.5(a)-(b))."""
import numpy as np
rng = np.random.default_rng(12345)
phi = lambda z, x: np.abs(x) - z*x

# (F1)-(F4)
w1 = w2 = w3 = w4 = -np.inf
for _ in range(100000):
    z = rng.uniform(-1, 1) if rng.random() < .7 else rng.choice([-1., 1.])
    x, y, r = rng.standard_normal(3)*10**rng.uniform(-3, 3, 3)
    w1 = max(w1, phi(z, x-y) - phi(z, x) - phi(-z, y))
    w2 = max(w2, abs(phi(z, x+r) - phi(z, x)) - 2*abs(r))
    v = abs(x); c = y
    w3 = max(w3, abs(phi(z, -c*v) - abs(c)*v*(1 + z*np.sign(c))))
for _ in range(2000):
    n = 20; v = rng.exponential(size=n); z = rng.uniform(-1, 1, n)
    lhs = min((v*(1+z)).sum(), (v*(1-z)).sum()); rhs = v.sum() - abs(v @ z)
    w4 = max(w4, abs(lhs - rhs))
print(f"F1 viol {w1:.1e}  F2 viol {w2:.1e}  F3 err {w3:.1e}  F4 err {w4:.1e}")

# theta-split (Lemma 2.3): adversarial random instances, check ||r_pm|| <= ||e|| + budget/2 (budget = sum phi_z(B+) + phi_-z(B-)),
# which is the sharper form (t/(2q0) instead of t/q0).
worst = -np.inf; worst_full = -np.inf
for it in range(40000):
    n = rng.integers(1, 40)
    contact = rng.random(n) < rng.uniform(0, 1)
    z = np.where(contact, rng.choice([-1., 1.], n), rng.uniform(-1, 1, n))
    Vabs = np.where(contact & (rng.random(n) < .7), rng.exponential(size=n)*10**rng.uniform(-2, 2), 0.)
    V = z*Vabs
    scale = 10**rng.uniform(-3, 3)
    e = rng.standard_normal(n)*scale*rng.choice([0, 1e-3, 1, 10])
    Bm = rng.standard_normal(n)*10**rng.uniform(-2, 2)
    if rng.random() < .3:  # make B- nearly (-z)-signed (cheap) to stress the bound
        Bm = -z*np.abs(Bm)
    Bp = Bm + V + e
    budget = phi(z, Bp).sum() + phi(-z, Bm).sum()
    theta = np.zeros(n); rp = Bp.copy(); rm = Bm.copy()
    m = Vabs > 0
    X = z*Bp; Y = z*Bm
    theta[m] = np.clip(X[m]/Vabs[m], 0, 1)
    rp[m] = z[m]*(X[m] - theta[m]*Vabs[m]); rm[m] = z[m]*(Y[m] + (1-theta[m])*Vabs[m])
    assert np.allclose(Bp, theta*V + rp) and np.allclose(Bm, -(1-theta)*V + rm)
    nr = max(np.abs(rp).sum(), np.abs(rm).sum())
    worst = max(worst, (nr - np.abs(e).sum() - budget/2)/(1 + np.abs(e).sum() + budget))
    worst_full = max(worst_full, (nr - np.abs(e).sum() - budget)/(1 + np.abs(e).sum() + budget))
print(f"theta-split: max rel. violation of ||r|| <= ||e|| + budget/2 : {worst:.1e};  of ||r|| <= ||e|| + budget : {worst_full:.1e}")

# 1.3(c): alternating z along S \ F: theta >= (3/4) 2^{-(s1-s0)} ||v||
wa = np.inf
for _ in range(20000):
    k = rng.integers(2, 30)
    gaps = rng.integers(1, 12, size=k)
    s = np.cumsum(gaps) + rng.integers(0, 20)
    v = 2.0**(-s.astype(float))
    z = np.array([(-1)**i for i in range(k)], float)*rng.choice([-1, 1])
    th = v.sum() - abs(v @ z)
    wa = min(wa, th/((3/4)*2.0**(-(s[1]-s[0]))*v.sum()))
print(f"alternating room: min theta/((3/4)2^-(s1-s0)||v||) = {wa:.4f} (must be >= 1)")

# unified triangular system (Lemma 2.5(a)-(b)): x_l <= (X_l + (8/3) S_{l+1})/rho_l  =>  S_1 <= prod(1+3/rho) sum X
wt = -np.inf
for _ in range(20000):
    L = rng.integers(1, 12)
    rho = 10**rng.uniform(-4, 0, L)
    X = rng.exponential(size=L)*10**rng.uniform(-3, 1, L)
    x = np.zeros(L); S = 0.
    for l in range(L-1, -1, -1):      # worst case: equality
        x[l] = (X[l] + (8/3)*S)/rho[l]; S += x[l]
    bound = np.prod(1 + 3/rho)*X.sum()
    wt = max(wt, S/bound - 1)
print(f"unified triangular unrolling: max (S_1/bound - 1) = {wt:.2e} (must be <= 0)")
