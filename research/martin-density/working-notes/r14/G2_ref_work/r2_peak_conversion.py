"""R2 (referee): block scalar kappa(zeta; Omega) across a peak crossing (G2 Lemma 5.5).

Block norm |x| = max <w, x> s.t. ||w||_inf + ||D w||_2 <= 1, (D w)_k = Phi_k w_k.  For a split M + C = 1 the maximizer is
w_k = sgn(x_k) min(M, lam v_k), v_k = |x_k|/Phi_k^2, with sum Phi_k^2 min(M, lam v_k)^2 = C^2; theta := M/lam is the threshold
(peak iff v_k >= theta), rho_k = v_k/theta.  kappa(zeta; Omega) := (|z|(|z| + theta) - sum_{k in Omega} v_k^2 Phi_k^2)/theta
(Part III, Subsection 2.1).  We move one coordinate d through its threshold and record theta, statuses, and kappa with
(i) Omega FIXED (d in Omega throughout) and (ii) Omega switched at the crossing (d removed when it becomes a peak, as in the
proof of G2 Lemma 5.5).
"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar

def block(x, Phi):
    # threshold equation (KKT of max <w,x> s.t. ||w||_inf + ||Phi w||_2 <= 1):
    #   sum_k Phi_k^2 (v_k - theta)_+ = sqrt(sum_k Phi_k^2 min(v_k, theta)^2),  |zeta| = theta * a(theta),
    #   a(theta)^2 = sum_k Phi_k^2 min(v_k/theta, 1)^2  (Part III: a = C/M, theta = |zeta| M/C)
    v = np.abs(x) / Phi**2
    F = lambda th: np.sum(Phi**2 * np.maximum(v - th, 0.0)) - np.sqrt(np.sum(Phi**2 * np.minimum(v, th)**2))
    theta = brentq(F, 1e-300, v.max(), xtol=1e-300, rtol=1e-15, maxiter=1000)
    a = np.sqrt(np.sum(Phi**2 * np.minimum(v / theta, 1.0)**2))
    return theta * a, theta, v

rng = np.random.default_rng(7)
n = 6
Phi = 0.25 * 0.5 ** np.arange(n) * rng.uniform(0.6, 1.0, n)
x0 = np.array([10.0, 0.5, 0.4, 0.6, 0.3, 0.2]) * Phi**2   # coordinate 0 a robust peak, others non-peaks
d = 3
val, th, v = block(x0, Phi)
print("initial statuses rho:", np.round(v / th, 4))
# scan x_d through the threshold of d
Omega = [k for k in range(n) if k != 0]              # coarse non-robust-peak set (0 plays the robust peak)
rows = []
for scale in np.linspace(0.2, 12.0, 4000):
    x = x0.copy(); x[d] = x0[d] * scale
    val, th, v = block(x, Phi)
    rho = v / th
    kap_fixed = (val * (val + th) - np.sum((v**2 * Phi**2)[Omega])) / th
    Om2 = [k for k in Omega if not (k == d and rho[d] >= 1.0)]
    kap_switch = (val * (val + th) - np.sum((v**2 * Phi**2)[Om2])) / th
    a2 = np.sum(Phi**2 * np.minimum(rho, 1.0)**2)
    rows.append((rho[d], th, val, kap_fixed, kap_switch, abs(val**2 - th**2 * a2), rho[1]))
rows = np.array(rows)
i = np.argmin(np.abs(rows[:, 0] - 1.0))
print("identity |zeta|^2 = theta^2 a^2: max error %.2e" % rows[:, 5].max())
print("near crossing rho_d = %.4f: theta=%.6e |zeta|=%.6e" % (rows[i, 0], rows[i, 1], rows[i, 2]))
jf = np.max(np.abs(np.diff(rows[:, 3]))); js = np.max(np.abs(np.diff(rows[:, 4])))
print("max step of kappa along the scan: Omega fixed %.3e ; Omega switched at crossing %.3e" % (jf, js))
print("predicted jump theta*Phi_d^2 at crossing: %.3e" % (rows[i, 1] * Phi[d]**2))
print("max step of theta %.3e, of another status rho_1 %.3e (intrinsic, continuous)" %
      (np.max(np.abs(np.diff(rows[:, 1]))), np.max(np.abs(np.diff(rows[:, 6])))))
