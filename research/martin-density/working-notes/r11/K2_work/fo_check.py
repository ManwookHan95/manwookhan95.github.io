import numpy as np
rng = np.random.default_rng(5)
def forced(a, z, mu):
    Ua = mu*a; nu = np.linalg.norm(Ua); e = Ua/nu; return nu, e, z + mu*e
def qstar(a, mu): return np.abs(a).sum() + np.linalg.norm(mu*a)
worst = 0.0
for trial in range(2000):
    n = rng.integers(10, 40)
    mu = 0.5*0.7**np.arange(n)*rng.uniform(0.5,1,n)
    F = rng.random(n) < 0.5; F[0] = True
    a = np.where(F, rng.normal(size=n)*rng.uniform(0.01,1,n), 0.0); a /= qstar(a, mu)
    z = np.where(F, np.sign(a), rng.uniform(-1,1,n))
    nu, e, zh = forced(a, z, mu)
    u = rng.normal(size=n)*0.8**np.arange(n)
    kap = np.dot(mu*u, e)/nu; Du = u - kap*a
    s = rng.choice(np.where(F)[0]); dm = 1e-6*np.sign(a[s])
    a2 = a.copy(); a2[s] += dm
    nu2, e2, zh2 = forced(a2, z, mu)
    pred = (mu[s]**2/nu)*Du[s]*dm
    act = np.dot(u, zh2) - np.dot(u, zh)
    scale = (mu[s]**2/nu)*(abs(u[s]) + abs(kap*a[s]))*abs(dm)
    worst = max(worst, abs(act-pred)/scale)
print("first-order support-mass formula: max |act-pred|/scale =", worst)
