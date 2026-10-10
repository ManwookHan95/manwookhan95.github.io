"""Sanity check of the bank donor (Lemma BD) in a finite model with a diagonal base.

Finite model: coordinates 0..n-1, base U = diag(s_j) (U^* e_j^* = s_j k_j), base support F = {0,1},
z in [-1,1]^n with z = sgn a on F, e = U^*a/nu, zhat_j = z_j + s_j^2 a_j/nu.
One block with carriers u_k (random finitely supported vectors, each with a private "signature"
coordinate sig[k] where u_k(sig[k]) = v_k > 0 and no other carrier lives).  zeta(k) = lam_k u_k(zhat).
Bank at the signature coordinate s of a robust peak c, with z_s = sgn(zeta(c)) (own-sign contact):
A = a + m z_s e_s.  Checks: (i) |u_c(zhat)| increases by m s_s^2 v_c/nu + O(m^2);
(ii) all other carriers change by O(m^2); (iii) theta increases, by at least the T2(b) lower bound.
"""
import numpy as np

rng = np.random.default_rng(11)


def theta_of(zeta, Phi):
    a = np.abs(zeta)
    nu = a / Phi**2

    def psi(x):
        A = np.sum(np.maximum(a - x * Phi**2, 0.0))
        B = np.sum(Phi**2 * np.minimum(x, nu) ** 2)
        return A * A - B

    lo, hi = 0.0, max(nu.max(), 1.0)
    while psi(hi) > 0:
        hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if psi(mid) > 0:
            lo = mid
        else:
            hi = mid
    th = 0.5 * (lo + hi)
    A = np.sum(np.maximum(a - th * Phi**2, 0.0))
    return th, A


fails = 0
worst_first = 0.0
worst_second = 0.0
min_raise_ratio = np.inf
T = 0
regime = [0]
for trial in range(2000):
    K = rng.integers(4, 12)          # carriers in the block
    nF = 2
    n = nF + 3 * K + 5
    s = 2.0 ** (-np.arange(1, n + 1) * rng.uniform(0.2, 0.6))
    a = np.zeros(n)
    a[:nF] = rng.normal(size=nF)
    a /= (np.abs(a).sum() + np.linalg.norm(s * a))  # q*(a) = ||a||_1 + ||U^* a|| = 1
    z = rng.uniform(-1, 1, n)
    z[:nF] = np.sign(a[:nF])
    sig = nF + np.arange(K)            # private signature coordinates
    Phi = 2.0 ** (-np.arange(1, K + 1)) * rng.uniform(0.3, 1.0, K)
    lam = Phi.copy()                   # m = 1
    Ucar = np.zeros((K, n))
    for k in range(K):
        sup = rng.choice(np.arange(nF + K, n), size=3, replace=False)
        Ucar[k, sup] = rng.normal(size=3) * 0.3
        Ucar[k, :nF] = rng.normal(size=nF) * 0.3
        Ucar[k, sig[k]] = rng.uniform(0.05, 0.3)

    def zhat_of(aa, zz):
        nu = np.linalg.norm(s * aa)
        return zz + s**2 * aa / nu

    zh = zhat_of(a, z)
    zeta = lam * (Ucar @ zh)
    th, A = theta_of(zeta, Phi)
    nu_k = np.abs(zeta) / Phi**2
    peaks = np.where(nu_k > th * (1 + 1e-6))[0]
    if len(peaks) == 0:
        continue
    c = peaks[np.argmax(nu_k[peaks] / th)]
    sc = sig[c]
    vs = np.sign(zeta[c])
    z2 = z.copy()
    z2[sc] = vs                        # close to an own-sign contact first
    zh2 = zhat_of(a, z2)
    zeta2 = lam * (Ucar @ zh2)
    th2, A2 = theta_of(zeta2, Phi)
    nuv = np.linalg.norm(s * a)
    for m in [1e-2, 3e-3, 1e-3, 3e-4]:
        a3 = a.copy()
        a3[sc] += m * vs
        zh3 = zhat_of(a3, z2)
        zeta3 = lam * (Ucar @ zh3)
        th3, A3 = theta_of(zeta3, Phi)
        dval = np.abs(Ucar[c] @ zh3) - np.abs(Ucar[c] @ zh2)
        pred = m * s[sc] ** 2 * Ucar[c, sc] / nuv
        worst_first = max(worst_first, abs(dval - pred) / m**2)
        others = [k for k in range(K) if k != c]
        dother = np.max(np.abs(Ucar[others] @ (zh3 - zh2)))
        worst_second = max(worst_second, dother / m**2)
        sraise = lam[c] * dval
        E = np.sum(np.abs(zeta3 - zeta2)) - abs(abs(zeta3[c]) - abs(zeta2[c]))
        phi = np.sum(Phi**2)
        lb = min(1.0, A2 * sraise / (8 * phi * (A2 + th2 + 1)))
        T += 1
        if E <= A2 * sraise / (8 * (A2 + th2 + 1)):
            if th3 - th2 < lb * (1 - 1e-9):
                fails += 1
            min_raise_ratio = min(min_raise_ratio, (th3 - th2) / lb)
        if m <= 0.05 * s[sc] ** 2 * Ucar[c, sc] * nuv and th3 <= th2:
            fails += 1
        if m <= 0.05 * s[sc] ** 2 * Ucar[c, sc] * nuv:
            regime[0] += 1
print("bank tests", T, "in regime m <= 0.05 s^2 v nu:", regime[0], "failures (no raise) in regime:", fails)
print("max |dval_c - m s^2 v/nu|/m^2 =", worst_first, " max other change/m^2 =", worst_second)
print("min (theta raise)/(T2(b) lower bound) =", min_raise_ratio)
