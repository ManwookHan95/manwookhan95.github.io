# J1 scratch 0 (working notes, not final)
Key reformulation (to be proved in part1):
- Delta := Psi - kappa_Psi a satisfies <U^*Delta, e> = 0 and Psi(zhat) = kappa_Psi + Delta(z)  [a(zhat) = 1].
- All first-order generator actions are in terms of Delta: z-move Delta(s) dz; mass (mu^2/nu) Delta(s) dm; bank (mu^2/nu) Delta(s) z_s dm.
- phi_y = y^T Ft(f_1+Pi) = Psi(zhat_1) (Euler) and, when all targets equal current ratios, phi_y = 0.  So the obstruction is
  purely the sign of the TARGET DISPLACEMENT projected on y:  phi_y = -sum_l y_l kappa_m (rt_l - current ratio_l) (+ KN-1, D, Pi terms).
- In (A*) with y = gamma h: Psi = (gamma/nu) (sum_{K0} rho_l u_l) =: (gamma/nu) Phi_0, rho_l = a_p/v_l(p).
  Exact proportional swallowing a = sum_{K0} rho_l u_l - Theta on F (Theta off F): Phi_0(zhat) = 1 + Theta(z) and this is the MAXIMUM
  of Phi_0(zhat(row)) over rows with the same z off F (Cauchy-Schwarz + sign rigidity).  Banks at anti-sign-data contacts lower it at
  first order, mass moves lower it at second order.  So "frozen combination": achievable = {Phi_0 <= current}.
- Residual (A*) with tiny peak-bordered scalars <=> per block rho-combination of ratios ~ 0 (h^T rt^{(m)} ~ 0).
- Far moves: pulls/pushes/far z-moves break certificates unless z_j = sigma_k := -sgn(coef_k) sgn v_k(j) on the far window
  (or super-thick).  Need bounded-range cone realization.
Routes: (1) target freedom (choose r'' with rho-combination not increased); (3) far moves rigorous; (2) cushion; (4) design.

## status before final assembly
part1: J1.1 deviation identity, J1.2 target form (peak columns depend on targets), J1.3 normal form, J1.4 global rigidity, J1.5 infeasibility.
part2: J1.6(a) orientation (every near-cert has coef_k ~ kappa_y a_p/v_k(p) on EVERY thick-type carrier), J1.6(b) placements,
       J1.7 one helpful far coordinate of one thick-type carrier => A-regular; frozen-window residual.
part3: J1.8 band version of K2.9; J1.9 one-out-of-many (band of width beta_* on one thick-type row => realized); J1.10 legitimate bands:
       nearly-neutral zero-data rows of (U)-blocks; robust holds of unprotected blocks; NOT: KN-1 of (T)-blocks unless Puiseux exp = 1;
       robust holds of protected blocks (factor Design^C/u circular); active rows.
part4: J1.11 first-order Puiseux margin (SKETCH: GEN gives regularity at every level point; uniformity gap in curve selection);
       J1.12 mismatch tolerance (conditional); gauge (identity, admissibility, curvature dichotomy PROVED; use SKETCH); target freedom char.
numerics: check_part1 (J1.1, J1.4: 0 violations / 20000), check_resonant2 (near-certificates at resonance: sign ok, coef/(kappa rho)=1,
       pull lowers y^T Ft exactly as predicted), check_orient (random configs: no exact certificates -- codimension one).
NOTE downstream: X1 2.2(iii) floor/kind[3] needs rho - rho^0 <= C gap/t at (T)-blocks -- weaker than the status margin; OK.
