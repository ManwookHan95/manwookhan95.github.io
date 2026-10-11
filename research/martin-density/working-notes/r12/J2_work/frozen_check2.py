"""J2 numerics part 2 (double precision, sanity only):
(A) Lemma J2.0 for the FROZEN pattern: d theta_f/d|zeta_p| (p in P_f) = A_f/(Phi_Pf^2 (A_f + theta_f)), d theta_f/d|zeta_l| (l in Q_f) =
    -nu_l/(Phi_Pf^2 (A_f + theta_f)); threshold raise needed to push weak peaks by mu (small mu): first-order prediction.
(B) Smoothness: along a path moving a weak peak across the TRUE threshold, the formula-1 kappa with TRUE (A, theta) has a derivative jump
    (K2-ref K-8), while the frozen kappa_f (target pattern) is smooth; the frozen and true scalars agree on the consistent side.
(C) Lemma J2.1(d) derivatives of kappa_f: d kappa_f/d|zeta_l| = rho_l s_f/(Phi_Pf^2 (1 + a_f)) for l in Omega and 1 - a_f s_f/(Phi_Pf^2(1+a_f))
    for p in P_f (fine carriers of fixed status included in s_f)."""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(7)

def true_block(zeta, Phi):
    nu = np.abs(zeta) / Phi**2
    def Psi(th):
        A = np.maximum(np.abs(zeta) - th * Phi**2, 0).sum()
        B = (Phi**2 * np.minimum(th, nu)**2).sum()
        return A**2 - B
    th = brentq(Psi, 1e-14 * nu.max(), nu.max(), xtol=1e-16, rtol=1e-15, maxiter=500)
    A = np.maximum(np.abs(zeta) - th * Phi**2, 0).sum()
    return th, A, nu

def frozen_block(zeta, Phi, Pf):
    """coarse k in Pf peaks, others non-peaks (no fine carriers here, except an optional fine set with fixed non-peak status)."""
    nu = np.abs(zeta) / Phi**2
    Q = ~Pf
    def Psi(th):
        A = (np.abs(zeta[Pf]) - th * Phi[Pf]**2).sum()
        B = th**2 * (Phi[Pf]**2).sum() + (nu[Q]**2 * Phi[Q]**2).sum()
        return A**2 - B
    hi = (np.abs(zeta[Pf]).sum()) / (Phi[Pf]**2).sum() * (1 - 1e-13)   # A_f(hi) > 0
    th = brentq(Psi, 1e-14 * hi, hi, xtol=1e-16, rtol=1e-15, maxiter=500)
    A = (np.abs(zeta[Pf]) - th * Phi[Pf]**2).sum()
    return th, A, nu

def make_block(K=9, b=1e-3):
    Phi = rng.uniform(0.05, 0.25, K)
    rho = np.concatenate([[np.nan, rng.uniform(1.5, 3.0)], 1 + b * rng.uniform(0.05, 0.95, 2), rng.uniform(0.2, 0.9, K - 4)])
    P = np.zeros(K, bool); P[:4] = True
    a = np.sqrt((Phi[P]**2).sum() + (rho[~P]**2 * Phi[~P]**2).sum())
    rho[0] = 1 + (a - ((rho[1:4] - 1) * Phi[1:4]**2).sum()) / Phi[0]**2
    sg = rng.choice([-1.0, 1.0], K)
    return sg * rho * Phi**2, Phi, rho

out = {}
def rec(k, v): out[k] = max(out.get(k, 0.0), abs(v))
for trial in range(200):
    zeta, Phi, rho = make_block()
    K = len(zeta)
    Pf = np.zeros(K, bool); Pf[:2] = True
    thf, Af, nu = frozen_block(zeta, Phi, Pf)
    PhiPf2 = (Phi[Pf]**2).sum()
    # (A) frozen Lemma J2.0
    for j in range(K):
        h = 1e-7 * abs(zeta[j]); z = zeta.copy(); z[j] += np.sign(zeta[j]) * h
        th2, _, _ = frozen_block(z, Phi, Pf)
        z[j] = zeta[j] - np.sign(zeta[j]) * h; th1, _, _ = frozen_block(z, Phi, Pf)
        fd = (th2 - th1) / (2 * h)
        form = (Af if Pf[j] else -nu[j]) / (PhiPf2 * (Af + thf))
        rec('(A) frozen d theta_f/d|zeta_j|: rel err', (fd - form) / abs(form))
    # (A') small push by threshold raise: needed relative raise of |zeta_0| for d log rho_k = -eps (k = weak peaks), eps = 1e-6
    eps = 1e-6
    af = Af / thf
    pred = eps * thf * PhiPf2 * (1 + af) / af          # dZ predicted
    z = zeta.copy(); target = np.log(nu[2] / thf) - eps
    f = lambda s: np.log(nu[2] / frozen_block(np.where(np.arange(K) == 0, zeta * (1 + s), zeta), Phi, Pf)[0]) - target
    s = brentq(f, 0.0, 1.0, xtol=1e-18)
    rec("(A') threshold raise dZ / first-order prediction - 1 (eps=1e-6)", abs(zeta[0]) * s / pred - 1)
    # (C) derivatives of kappa_f, Omega = all non-Pf coarse carriers EXCEPT one carrier kept outside Omega (to make s_f > 0)
    Om = ~Pf.copy(); Om[K - 1] = False
    def kap(zz):
        t, A, n = frozen_block(zz, Phi, Pf)
        SOm = (n[Om]**2 * Phi[Om]**2).sum()
        return A + (A**2 - SOm) / t, t, A, n
    k0, t0, A0, n0 = kap(zeta)
    s_f = (n0[(~Pf) & (~Om)]**2 * Phi[(~Pf) & (~Om)]**2).sum() / t0**2
    a0 = A0 / t0
    for j in range(K):
        h = 1e-7 * abs(zeta[j]); zp = zeta.copy(); zp[j] += np.sign(zeta[j]) * h; zm = zeta.copy(); zm[j] -= np.sign(zeta[j]) * h
        fd = (kap(zp)[0] - kap(zm)[0]) / (2 * h)
        if Pf[j]: form = 1 - a0 * s_f / (PhiPf2 * (1 + a0))
        elif Om[j]: form = (n0[j] / t0) * s_f / (PhiPf2 * (1 + a0))
        else: continue
        rec('(C) d kappa_f/d|zeta_j| abs err', fd - form)
    # (B) path across the true threshold for weak peak 2: rho_2 from 1 + 1e-3 down to 1 - 1e-3 (true statuses)
    def gap(sv):
        zz = zeta.copy(); zz[2] = np.sign(zeta[2]) * sv; t, A, n = true_block(zz, Phi); return n[2] - t
    s0 = brentq(gap, 0.5 * abs(zeta[2]), 2 * abs(zeta[2]), xtol=1e-16)   # crossing point
    OmT = ~Pf.copy()
    def kap_true(sv):
        zz = zeta.copy(); zz[2] = np.sign(zeta[2]) * sv
        t, A, n = true_block(zz, Phi)
        return A + (A**2 - (n[OmT]**2 * Phi[OmT]**2).sum()) / t
    def kap_froz(sv):
        zz = zeta.copy(); zz[2] = np.sign(zeta[2]) * sv
        t, A, n = frozen_block(zz, Phi, Pf)
        return A + (A**2 - (n[OmT]**2 * Phi[OmT]**2).sum()) / t
    h = 1e-6 * s0
    dT_below = (kap_true(s0 - h) - kap_true(s0 - 2 * h)) / h; dT_above = (kap_true(s0 + 2 * h) - kap_true(s0 + h)) / h
    dF_below = (kap_froz(s0 - h) - kap_froz(s0 - 2 * h)) / h; dF_above = (kap_froz(s0 + 2 * h) - kap_froz(s0 + h)) / h
    rec('(B) |jump of d kappa_true/d|zeta_2|| across the true threshold (expected O(1))', dT_above - dT_below)
    rec('(B) |jump of d kappa_frozen/d|zeta_2||  (expected ~ h * C)', dF_above - dF_below)
    # on the side where the weak peak is a true strict non-peak and peak 3 too: does frozen = true?  (peak 3 is still a true weak peak, so
    # make it a non-peak as well first)
    zz = zeta.copy(); zz[2] = np.sign(zeta[2]) * s0 * 0.99; zz[3] = zeta[3] * 0.98
    t1, A1, n1 = true_block(zz, Phi); t2, A2, n2 = frozen_block(zz, Phi, Pf)
    if all(n1[k] < t1 for k in range(K) if not Pf[k]):
        rec('(B) consistent side: |theta_f - theta| / theta', (t2 - t1) / t1)
for k, v in out.items():
    print(f"{k:85s} max = {v:.3e}")
