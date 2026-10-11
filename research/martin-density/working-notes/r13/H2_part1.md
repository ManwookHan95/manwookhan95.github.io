# H2 part 1: precise formulation of (R1); first structural facts

Setting and notation: r12/J1_notes.md 1 and r12/J1_ref_notes.md (design T_fin^{K2} with (FC), P-TU windows, F-2 coupling),
r11/K2_notes.md 4-5 (preparation (P), Sys-A, K2.8, K2.9, K2.16), r11/K1_notes.md 2.0-2.7 (levers, pullability, (U)/(S)).
Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED" = modulo the refereed chain cited by J1.15' and J2.1.

## 1.1 What (R1) is
At a main stage L (clean sub-window w, class a), (R1) means: Step A (at the unpushed prepared row with (FC)) carries a
near-certificate y of size eps <= eps_* with phi_y > -rho_0, and NO coarse carrier is thick-type (no thick private
coordinate in S_k ∩ [1, D(L)]).  By R-G (J1-ref D): |a_s| <= 2b for s in F ∩ (s_max(L), D(L)].

FACT 1.1 (carrier kinds in (R1)).  PROVED.  In (R1):
 (a) no near coordinate of a coarse carrier is thick (near coordinates lie in (s_max(L), d(L)] ⊂ (s_max(L), D(L)]); so there are
     no (P3)/(P4) resources, no kind-(ii)/(iii) carriers (K2.16 proof of (3)), and the signed common-mode vector h vanishes;
 (b) every ZERO-DATA tuned carrier is kind (i) (its off-F/thin near coordinates are ZD after (P): two-sided composite moves);
 (c) every DATA-CARRYING tuned carrier is kind (i) (pre-placed TU lever: pullable on the TU window) or kind (iv) (= K1's (U):
     its near coordinates are S_th of the data sign sigma_l = eps_l, its TU window [x_TU, x'_max] of S_l contains no pullable
     coordinate);
 (d) every coarse peak of an UNSHIFTED block (Delta'_m = 0) is zero-data (c_k = -Delta''_m lambda_k vs_k = 0) and its near
     coordinates are off F or thin, hence ZD after (P): the block has a private two-sided peak resource (R-PK applies);
 (e) a coarse peak of a SHIFTED block carries data -Delta''_m lambda_c vs_c; its near coordinates are S_th contacts/raised
     support of the data sign; the bank there moves vs_c u_c(xhat) by -sgn(Delta''_m) per unit, so it RAISES kappa_m when
     Delta''_m < 0 and LOWERS kappa_m when Delta''_m > 0 (d kappa_m/d zeta(c) = 1 - X_m >= 3/4, (FC)); a pullable far coordinate
     of the peak gives a two-sided resource (K1 2.2 repair: TU on the peak).
Proof.  (a) R-G and the definitions (K1 2.0: N_l = first six elements of S_l beyond s_max(L), inside (s_max(L), d(L)];
d(L) <= D(L)).  (b), (c): K2.16's case list ((i) N_l contains a ZD coordinate or l has a pre-placed TU lever; (iv) every near
coordinate is S_th of the data sign) after (P) (K2 4.1(d)); a data-carrying carrier cannot have an anti-sign thin near
coordinate (K1 Lemma K1.3 case (S): |c_l| v_l(s) <= 4|a_s|/t <= 8b/t would force |c_l| <= 8bH/t < K_*^2 K t/(4D), against
Lemma K1.2), nor a free near coordinate (K1 2.1(b)).  (d), (e): K1 1.0 (peak data), (FC) / U1 Lemma 1.4(a), K2.4.  QED

FACT 1.2 (every near-certificate in (R1) is of pure type (U*)).  PROVED.  In (R1) every near-certificate y of size
eps <= eps_* satisfies ||coef_(iv)||_2 >= c_1 - C eps Design^2 |Lambda_A| and kappa_Psi <= -c_1/(8 H(L)).
Proof.  K2.16(3) with h = 0 (Fact 1.1(a)): gamma_0 = +infinity, so the first alternative is excluded; kinds (i) have
|coef| <= eps Design^2 (K2.16(2a)); ||coef_tuned||_2 >= c_1.  QED
So the one-out-of-many principle (J1.6) has no thick-type carrier to act on; (R1) is exactly the pure (U*) sign class.

## 1.2 The orientation of kind-(iv) rows
For a tuned carrier l: val_l = eps_l u_l(xhat), coef_l = eps_l y_l - zeta_m lambda_l (d kappa_m/d zeta(l)), and in route V
d kappa_m/d zeta(l) = rho_l M X/C <= C b^2 D^2 for non-peaks (U1 Lemma 1.4(c)); |zeta_m| <= Design^2.  Hence
      |coef_l - eps_l y_l| <= C Design^4 b^2 =: e_X   (tiny)                                              (1.1)
The one-sided generator of a kind-(iv) row (raise at an S_th near coordinate s, z_s = eps_l) raises val_l by eff_s v_l(s) per
unit and acts on y^T Ft by eff_s c_s(Psi), c_s(Psi) = coef_l eps_l v_l(s) - kappa theta_0 (K2.16(2c)); hence
      y_l >= -(eps Design + |kappa| theta_0) Design - e_X =: -e_1     for every kind-(iv) row l.              (1.2)
Kind-(iv) rows can only RAISE val_l by private resources (the far TU window of S_l is anti-sign support or super-thick;
z_j = -eps_l is the minimum of eps_l v_l(j) z_j).

ORIENTATION.  Every active row has a robust target ratio: rho_l >= u for active carriers (nearly neutral carriers are
exactified to zero data), so |rt_l| >= u Phi_l/(m K) >= u/Design^C.  Split the kind-(iv) rows of block m:
      K^+_m := {l : rt_l > 0},   K^-_m := {l : rt_l < 0}   (rt_l = eps-oriented target ratio, val_l = rt_l kappa_m at the target).
For l in K^-_m an OVERSHOOT (realized val_l above the target) DEcreases |r^#_l|; for l in K^+_m it INcreases |r^#_l|.
