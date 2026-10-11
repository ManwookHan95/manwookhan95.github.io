"""J1 part 1 sanity checks: Lemma J1.1 (deviation identity) and Lemma J1.4 (global rigidity of Phi = a + Theta) in a finite model
with diagonal base.  Rows: a (normalized q*(a)=1), z with z = sgn a on F, |z|<=1 off F."""
import numpy as np
rng = np.random.default_rng(12)
def qstar(a, mu): return np.abs(a).sum() + np.linalg.norm(mu*a)
def row(a_un, z, mu):
    a = a_un/qstar(a_un, mu); nu = np.linalg.norm(mu*a); e = mu*a/nu
    zh = z.copy(); zh = zh + mu*e
    return a, nu, e, zh
worst1 = 0.0; worst4 = -1e9; n_viol = 0; ntest = 0
for trial in range(400):
    n = 30; mu = 0.5*0.8**np.arange(n)
    F = rng.random(n) < 0.5
    a_un = np.where(F, rng.normal(size=n), 0.0)
    z = np.where(F, np.sign(a_un), rng.uniform(-1, 1, n))
    S1 = np.where(~F)[0][:6]                     # one-sided coordinates: contacts off F
    z[S1] = rng.choice([-1, 1], len(S1))
    a, nu, e, zh = row(a_un, z, mu)
    # J1.1
    u = rng.normal(size=n)
    kap = (mu*u) @ e / nu; dev = u - kap*a
    worst1 = max(worst1, abs((mu*dev) @ e), abs(u @ zh - (kap + dev @ z)))
    # J1.4: Phi = a + Theta, Theta anti-signed on S1
    Theta = np.zeros(n); Theta[S1] = -z[S1]*rng.uniform(0, 0.3, len(S1))
    Phi = a + Theta
    base = Phi @ zh
    for k in range(50):
        # random row R' keeping S1 coordinates' sign: z' = z there, a'_s z_s >= 0 there; anything elsewhere
        a2 = a_un*np.exp(rng.normal(scale=0.5, size=n))*np.where(rng.random(n) < 0.1, -1, 1)   # sign flips allowed on F
        a2 = np.where(rng.random(n) < 0.15, 0.0, a2)
        new = (~F) & (rng.random(n) < 0.2); a2[new] = rng.normal(size=new.sum())
        a2[S1] = np.where(rng.random(len(S1)) < 0.5, 0.0, z[S1]*rng.uniform(0, 0.5, len(S1)))   # banks of the data sign or nothing
        z2 = np.where(a2 != 0, np.sign(a2), rng.uniform(-1, 1, n)); z2[S1] = z[S1]
        a2n, nu2, e2, zh2 = row(a2, z2, mu)
        bound = 1 + Theta @ z + sum(mu[s]**2*Theta[s]*a2n[s]/nu2 for s in S1)
        val = Phi @ zh2
        ntest += 1
        worst4 = max(worst4, val - bound)
        if val > bound + 1e-12: n_viol += 1
print(f"J1.1: max |<U*Dev,e>|, |u(zhat)-(kappa+Dev(z))| = {worst1:.2e}")
print(f"J1.4: {ntest} random rows, max Phi(zhat')-bound = {worst4:.3e}, violations = {n_viol}")
