"""K1 referee: arithmetic illustration of R-6 (log2 scale).  For a clean sub-window w = (L, i), i >= 2, of the design:
u = b(w^-) <= T_lo(w^-)^4/(L Design), T_hi(w) <= (u/(4 Design))^(omega+20), T = T_lo(w) = 2^{-n} T_hi, n >= L 2^{L^3} Q.
E^eng with window-dependent c_flat ~ c_f u needs theta'/c_flat^2 -> 0, theta' := (companion cost)/T^2.
K1's far moves with x_max = T^2/(L Design |Lambda|): cost >= ~ |Lambda| x_max (lowering) and ~ x_max log(1/x_max) per pull z-flip.
Referee's x'_max = u^2 T^3/(Design^2 |Lambda|): cost <= C Design |Lambda| x'_max log(1/T).
All numbers are log2; we only compare exponents.
"""
import math
for (L, logDesign, logTlo_prev, omega) in [(5, 40, -1e3, 50), (8, 200, -1e5, 300), (12, 2000, -1e7, 3000)]:
    log_u = 4 * logTlo_prev - math.log2(L) - logDesign          # u = b(w^-) <= T_lo(w^-)^4/(L Design)
    log_Thi = (omega + 20) * (log_u - 2 - logDesign)              # T_hi <= (u/(4 Design))^(omega+20)
    log_logT = math.log2(-log_Thi) + 3 * L                        # log2 log2(1/T) roughly (n >= 2^{L^3} Q dominates)
    Lam = L
    # K1: theta' ~ x_max log(1/x_max)|Lambda| / T^2 ~ log(1/T)/(L Design)
    log_theta_K1 = log_logT - math.log2(L) - logDesign
    log_ratio_K1 = log_theta_K1 - 2 * log_u                       # theta'/c_flat^2 with c_flat ~ u
    # referee: theta' ~ Design |Lambda| x'_max log(1/T) / T^2 = u^2 T log(1/T)/Design
    log_T = log_Thi                                               # T <= T_hi (only an upper bound needed)
    log_theta_ref = 2 * log_u + log_T + log_logT - logDesign
    log_ratio_ref = log_theta_ref - 2 * log_u
    print(f"L={L}: log2 u = {log_u:.3g}; log2(theta'/c_flat^2): K1 x_max -> {log_ratio_K1:.3g} (must be -> -inf), "
          f"referee x'_max -> {log_ratio_ref:.3g}")
