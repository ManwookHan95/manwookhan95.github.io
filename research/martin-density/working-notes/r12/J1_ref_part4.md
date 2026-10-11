# J1 referee, part 4: the gauge (7.3), target freedom and the stable exact case (7.4), the residual (8)

## 4.1 The gauge (J1 7.3 / part4 4.4).  Verdict: (a), (b), (c) CORRECT; (d) main statement CORRECT, its "in particular" UNJUSTIFIED (P-G);
## (e) SKETCH (label honest).
(a) Tautology: a piece is (b, omega) with g = b + sum_m R_m^*(omega_m - d_m(omega_m) w_m), d_m linear, so (b - s B(rhot), omega + s rhot) represents
    the same g.  (b) sum_m R_m^* rhot_m = sum_{K_0} lambda_k (rho_k/lambda_k) u_k = Phi_0; d_m(rhot_m) = <D w_m, D rhot_m>/C_m and, by the block
    threshold lemma (off the peak set w_m(k) = C_m (R_m xi)(k)/(Phi_m(k)^2 |R_m xi|)), <D w_m, D rhot_m> = (C_m/A_m) Phi_0^{(m)}(xi); hence
    d_m(rhot_m) = Phi_0^{(m)}(xi)/A_m (xi = q_0 zhat).  Re-derived.  (c) Coordinatewise rules re-derived (TS: -s a_j is anti-sign for s > 0 and needs
    s|a_j| <= C_+ |a_j|/t, i.e. |s| <= C_+/t; contacts: sign rows; free E_c coordinates: exact zero needed).
(d) The parabola argument is correct: {s_+ - s_-} contains every value between 0 and 2(s^*(P^+) - s^*(P^-)) = 2 s_0^Gamma.  P-G: "if the switching
    through K_0 is EXACTLY along rhot (single thick-type carrier, or Domega|_{K_0} proportional to rhot), s_0 = s_0^Gamma" needs Q(G^perp, G) = 0, which
    does not follow from a support condition: Q (= q_0 H_b + sum sigma_m H_m) couples K_0 with the other carriers of the block (through d_m and C_m)
    and with the base part.  Two-dimensional example: Q = [[2, 1], [1, 2]], G = (1, 0), switching s_0 G + (0, 1): s_0^Gamma = s_0 + 1/2.  Replace by:
    "s_0 = s_0^Gamma whenever the Q-orthogonal decomposition of the switching along G has G-coefficient s_0".

## 4.2 Target freedom (7.4(a)-(b)).  Verdict: CORRECT as a restatement (with P-1).
(a) is K2.9's definition rewritten; note that C_ach itself depends on the targets through zeta_m(.; rt) (part 1, P-1), so "target freedom" is a
fixed-point condition, not a condition on a fixed cone.  (b) The fuzz statement is correct; Remark R-W (part 2) shows the fuzz is a window
quantity (it can be lowered to O(Design^C x/x_TU)), but it stays >> eta', so the conclusion of (b) is unchanged.

## 4.3 Stable exact case (7.4(c)/(d), part4 4.5(d)).  Verdict: CORRECT only under two unstated hypotheses (P-S); the flatness computation is
## correct.
P-S.  The two claims "a = Phi_0 on the thick part of F" and "Phi_0^{(m)}(zhat_f) = 0 for every block" are derived from the near-certificate
relations.  K2.16(4) gives Psi(s) = kappa a_s + O(eps Design) at EVERY thick s <= D(L); on a thick TARGET coordinate s in T(L), Psi(s) = sum_k coef_k u_k(s)
includes non-thick-type carriers (kind (iv), peaks), so a_s = Phi_0(s) needs that these coefficients be negligible.  The per-block vanishing needs
zeta_m ~ 0 (private peak resource) AND no robust kind-(iv) coefficient in the block (then sum_{l in m} y_l val_l = kappa_y Phi_0^{(m)}(zhat_1) + small).
Correct statement (PROVED, via Lemma R-PB): if at all large residual stages (H-pure) the robust coefficients of the near-certificates lie on
thick-type NON-peaks only, and (H-pk) every block meeting K_0 has a private two-sided peak resource, then at each such stage
|Phi_0^{(m)}(zhat_1)| <= kappa_m (tau_* + C Design max|rt - rc|) for every block and |a_s - Phi_0(s)| <= eps Design/|kappa| at every thick s <= D(L);
if moreover K_0 and the rho_k stabilize, the relations are exact at f in the limit (tau_*, eps Design, eta' -> 0 and zhat_1 -> zhat_f
coordinatewise with Phi_0 in l_1).  Flatness re-derived: for K_0 strict non-peaks, ||w_m + t rhot_m||_inf = M for |t| small, and
||D(w_m + t rhot_m)||_2 = C + t <Dw, D rhot>/C + O(t^2) = C + t Phi_0^{(m)}(xi)/A_m + O(t^2), so N_m(w_m + t rhot_m) = 1 + O(t^2) when Phi_0^{(m)}(xi) = 0,
and p*(f + t Phi_0) <= max(q*(a), max_m N_m(w_m + t rhot_m)) (B_{p*} = B_{q*} + L^*B_{V*}).  At a residual stage (not in the limit) the same
computation gives p*(f + t Phi_0) <= 1 + C' t tau' + C t^2: approximately flat at scales t >> tau'.

## 4.4 The residual (J1 8).  Verdict: correct as a NECESSARY condition after the following corrections (none makes it larger than stated
## except P-TU's window convention, which enlarges the (U)-class exactly as K1-ref R-6 did).
 (1) (R-np) must exclude nearly-neutral zero-data carriers (covered by J1.10(a) without coupling or peak resource).
 (2) (R-D2)/(R-np)/(J-c): with F-2 the coupling rescales all targets of the block; P-D2 for inactive blocks.
 (3) NEW necessary condition (Lemma R-PB): every block m with a private two-sided peak resource meeting K_0 and whose tuned carriers are thick-type,
     privately tunable, or kind (iv) of the opposite orientation, has |S_m| <= tau_*, i.e. |Phi_0^{(m)}(zhat_1)| <= kappa_m (tau_* + C Design eta'').
 (4) (R1) precision: robust coefficients may also sit on non-thick-type peaks of blocks without a private peak resource, and "unpulled" means:
     no pullable coordinate in the TU window (anti-data-sign support, or data-sign support with |a_j| > x'_max).
 (5) Observation R-G (PROVED; K2 4.1(d), K2.16(4), K2.17(b)): at a stage of type (R1) every s in F ∩ (s_max(L), D(L)] is THIN (|a_s| <= 2b(w)):
     a thick s there lies in U_L (no anchor) and beyond the targets, hence in a coarse signature set, so its carrier would be thick-type.  So (R1)
     at all large main stages forces a to be b(w(L))-thin (super-exponentially small) on the long intervals (s_max(L), D(L)] beyond the coarse
     targets.  At a stage of type (R0) every coarse carrier k has all thick private coordinates in S_k ∩ [1, D(L)] proportional to v_k up to the
     tiny spread of J1.6(a) (else K2.17(e) applies).  Both are strong non-generic conditions on f; neither is shown to be impossible at all large
     stages, and nothing suggests a non-recoverable mate.
Status of the goal: (LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and of NA((c_0, p), l_2^2): OPEN.
