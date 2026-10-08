import numpy as np
rng = np.random.default_rng(1)

# ---------- Block certificate exact formula ----------
# N(w) = ||w||_inf + ||D w||_2 ; W(tau) = (1 - d tau) w + tau*omega, omega off-peak.
def N(w, Phi):
    return np.max(np.abs(w)) + np.linalg.norm(Phi * w)

worst = 0.0
for trial in range(2000):
    n = 12
    Phi = 2.0 ** (-np.arange(1, n + 1)) * rng.uniform(0.5, 1.0, n)
    w = rng.uniform(-1, 1, n)
    P = rng.choice(n, size=rng.integers(1, 4), replace=False)
    w[P] = np.sign(w[P] + 1e-12)          # peak coordinates at +-1
    w = w / N(w, Phi)                     # normalise N(w)=1
    M = np.max(np.abs(w)); C = np.linalg.norm(Phi * w)
    off = [k for k in range(n) if abs(abs(w[k]) - M) > 1e-9]
    omega = np.zeros(n)
    S = rng.choice(off, size=min(3, len(off)), replace=False)
    omega[S] = rng.normal(size=len(S))
    d = np.dot(Phi * w, Phi * omega) / C
    h = Phi * omega
    hperp2 = np.dot(h, h) - d ** 2
    gap = min(M - abs(w[k]) for k in S)
    r = min(gap / (2 * np.max(np.abs(omega))), 1 / (2 * abs(d) + 1e-15), C / (2 * abs(d) * M + 1e-15))
    for tau in np.linspace(-r, r, 21):
        Wt = (1 - d * tau) * w + tau * omega
        lhs = N(Wt, Phi)
        Y = C + d * tau * M
        exact = 1 + tau ** 2 * hperp2 / (np.sqrt(Y ** 2 + tau ** 2 * hperp2) + Y)
        bound = 1 + 0.5 * tau ** 2 * (hperp2 / C) * (1 + 2 * abs(d * tau) * M / C)
        worst = max(worst, abs(lhs - exact))
        assert lhs <= bound + 1e-12, (lhs, bound)
print("block: max |N(W(tau)) - exact formula| =", worst)

# ---------- Base certificate exact formula ----------
for trial in range(2000):
    n, mH = 10, 6
    U = rng.normal(size=(n, mH))
    a = np.zeros(n); F = rng.choice(n, size=4, replace=False); a[F] = rng.normal(size=4)
    qa = np.abs(a).sum() + np.linalg.norm(U.T @ a); a /= qa
    nu = np.linalg.norm(U.T @ a); e = U.T @ a / nu
    z = rng.uniform(-0.9, 0.9, n); z[F] = np.sign(a[F])
    zhat = z + U @ e
    b = np.zeros(n); b[F] = rng.normal(size=4)
    b -= (b @ zhat) * a / (a @ zhat)       # b(zhat)=0, supp b in F
    beta = np.linalg.norm(U.T @ b)
    hb = (beta ** 2 - (U.T @ b @ e) ** 2) / nu
    delta = min(abs(a[j]) / abs(b[j]) for j in F if abs(b[j]) > 1e-14)
    r = min(delta, nu / (2 * beta))
    for tau in np.linspace(-r, r, 21):
        val = np.abs(a + tau * b).sum() + np.linalg.norm(U.T @ (a + tau * b))
        bound = 1 + 0.5 * tau ** 2 * hb * (1 + 2 * abs(tau) * beta / nu)
        lower = 1 + 0.5 * tau ** 2 * hb / (1 + abs(tau) * beta / nu)
        assert val <= bound + 1e-12 and val >= lower - 1e-12, (val, bound, lower)
print("base: expansion bounds verified")

# ---------- Monotone truncation inequality (base, with flips) ----------
worst_ratio = 0.0
for trial in range(500):
    n, mH = 30, 8
    U = rng.normal(size=(n, mH)) / 3
    a = rng.normal(size=n) * 2.0 ** (-rng.uniform(0, 8, n))
    qa = np.abs(a).sum() + np.linalg.norm(U.T @ a); a /= qa
    nu = np.linalg.norm(U.T @ a); e = U.T @ a / nu
    z = np.sign(a); zhat = z + U @ e
    b = rng.normal(size=n) * 0.3
    b -= (b @ zhat) * a                      # b(zhat)=0 since a(zhat)=1
    def qs(c):
        return np.abs(c).sum() + np.linalg.norm(U.T @ c)
    for t in [0.2, 0.05, 0.01]:
        G = np.abs(b) <= np.abs(a) / (2 * t)
        bt = np.where(G, b, 0.0)
        kappa = bt @ zhat
        ct = bt - kappa * a
        for sig in np.linspace(-0.3, 0.3, 61):
            diff = qs(a + sig * ct) - qs(a + sig * b)
            scale = sig ** 2 * (abs(kappa) * np.abs(b).sum() + np.abs(ct - b).sum()) + 1e-15
            worst_ratio = max(worst_ratio, diff / scale)
print("monotone truncation: max ratio =", worst_ratio)
