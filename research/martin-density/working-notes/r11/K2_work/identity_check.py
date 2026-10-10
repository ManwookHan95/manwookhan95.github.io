"""K2 sanity checks (numerics only; finite models).
(1) Exact identity (Lemma K2.ID): for any row (a, z) with q*(a) = 1 and any u in l_1,
      u(zhat) = kappa_u + sum_{s in F} D_u(s) sgn(a_s) + sum_{s notin F} u(s) z_s,
    kappa_u := <U*u, e>/nu, D_u(s) := u(s) - kappa_u a_s, e := U*a/nu, zhat := z + U e (diagonal U).
(2) Resource bound (Lemma K2.RD): sum_{F, s<=D}|D_u| + sum_{F^c, s<=D}|u| >= <U*u,e> - u(zhat) - ||u 1_(D,inf)||_1  (if <U*u,e> >= 0).
(3) First-order formulas (Lemma K2.FO): mass dm at s in F: d u(xhat) = (mu_s^2/nu) D_u(s) dm; z-move at s notin F: u(s) dz;
    bank dm at contact s notin F (sign z_s): (mu_s^2/nu) u(s) z_s dm.   (normalization by q* does not change e or z.)
"""
import numpy as np
rng = np.random.default_rng(11)

def forced(a, z, mu):
    Ua = mu * a
    nu = np.linalg.norm(Ua)
    e = Ua / nu
    zhat = z + mu * e
    return nu, e, zhat

def qstar(a, mu):
    return np.abs(a).sum() + np.linalg.norm(mu * a)

maxerr1 = maxviol2 = 0.0; maxerr3 = 0.0
for trial in range(400):
    n = rng.integers(20, 60)
    mu = 0.5 * 0.7 ** np.arange(n) * rng.uniform(0.5, 1.0, n)
    F = rng.random(n) < 0.5
    F[0] = True
    a = np.where(F, rng.normal(size=n) * rng.uniform(0.01, 1, n), 0.0)
    a /= qstar(a, mu)
    z = np.where(F, np.sign(a), rng.uniform(-1, 1, n))
    contacts = (~F) & (rng.random(n) < 0.4)
    z[contacts] = np.sign(rng.normal(size=contacts.sum()))
    nu, e, zhat = forced(a, z, mu)
    u = rng.normal(size=n) * 0.8 ** np.arange(n)
    kap = np.dot(mu * u, e) / nu
    Du = u - kap * a
    lhs = np.dot(u, zhat)
    rhs = kap * qstar(a, mu) + np.sum(Du[F] * np.sign(a[F])) + np.sum(u[~F] * z[~F])
    maxerr1 = max(maxerr1, abs(lhs - rhs))
    # (2)
    if np.dot(mu * u, e) >= 0:
        for D in range(1, n):
            res = np.sum(np.abs(Du[:D][F[:D]])) + np.sum(np.abs(u[:D][~F[:D]]))
            bound = np.dot(mu * u, e) - lhs - np.sum(np.abs(u[D:]))
            maxviol2 = max(maxviol2, bound - res)
    # (3) first-order: support mass at s in F
    s = rng.choice(np.where(F)[0]); dm = 1e-7 * np.sign(a[s])
    a2 = a.copy(); a2[s] += dm
    nu2, e2, zhat2 = forced(a2, z, mu)   # z unchanged (same sign); e is scale invariant
    pred = (mu[s] ** 2 / nu) * Du[s] * dm
    act = np.dot(u, zhat2) - lhs
    maxerr3 = max(maxerr3, abs(act - pred) / (abs(pred) + 1e-30) if abs(pred) > 1e-14 else 0)
    # bank at a contact
    cs = np.where(contacts)[0]
    if len(cs):
        s = rng.choice(cs); dm = 1e-7
        a3 = a.copy(); a3[s] = z[s] * dm
        nu3, e3, zhat3 = forced(a3, z, mu)
        pred = (mu[s] ** 2 / nu) * u[s] * z[s] * dm
        act = np.dot(u, zhat3) - lhs
        if abs(pred) > 1e-14:
            maxerr3 = max(maxerr3, abs(act - pred) / abs(pred))
print("(1) identity max error:", maxerr1)
print("(2) resource bound max violation (should be <= 0):", maxviol2)
print("(3) first-order formulas max relative error:", maxerr3)
