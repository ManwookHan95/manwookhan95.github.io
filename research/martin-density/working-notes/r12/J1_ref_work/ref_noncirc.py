"""J1-ref check N4 (finding F-2): size of the coupling term in J1.15's non-circularity when only the ACTIVE targets of a (U)-block are
rescaled.  Lemma K: K(sigma,R^2) = [sigma + sqrt(sigma^2 R^2 + sigma(1-R^2))]/(1-R^2), a = K - sigma, dK/dR^2 = K^2/(2(a - K R^2)).
A band of half-width beta on a robust hold k (ratio r_k, rho_k = m|r_k|K/Phi_k) changes R^2 by 2 m^2 |r_k| beta/kappa; the protected active
statuses (rho_d = m|r_d|K/Phi_d) are restored by rescaling the active targets by s with 1 - s ~ (dK/dR^2/K) * 2 m^2 |r_k| beta/kappa.
If only actives are rescaled, phi_y moves by kappa (1-s) zeta_act with zeta_act = -y_k r_k + O(eps Design) (peak resource: zeta_m ~ 0), i.e.
by (dK/dR^2/K) 2 m^2 r_k^2 beta |y_k|; the band gains only beta |y_k|/2.  ratio := 4 m^2 r_k^2 (dK/dR^2)/K = 2 rho_k^2 Phi_k^2/(K (a - K R^2))."""
import numpy as np
def K(sig, R2): return (sig + np.sqrt(sig**2*R2 + sig*(1 - R2)))/(1 - R2)
for sig in (0.02, 0.09, 0.25):
    for R2 in (0.05, 0.3):
        for Phik, rhok in ((0.3, 0.5), (0.45, 0.9), (0.1, 0.5)):
            k = K(sig, R2); a = k - sig; dK = k**2/(2*(a - k*R2))
            h = 1e-7; dKnum = (K(sig, R2 + h) - K(sig, R2 - h))/(2*h)
            ratio = 2*rhok**2*Phik**2/(k*(a - k*R2))
            print(f"sigma={sig:.2f} R2={R2:.2f} Phi_k={Phik:.2f} rho_k={rhok:.2f}: K={k:.3f} dK/dR2={dK:.3f} (num {dKnum:.3f}) ratio={ratio:.3f}"
                  f" {'(coupling term EXCEEDS band gain)' if ratio > 1 else ''}")
