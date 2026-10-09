# G3 referee, part 3: attempts to break Theorem B; side results; remaining items

## 3.1 Attacks tried on Theorem B (none succeeded)
1. Kink re-splitting (C referee's finite analogue, Gamma_2 = 0.296 < Gamma_w = 0.485). At f in R_0 the minus side can represent a contact
   component e_j* only through carriers u_l ~ e_j*/q*(e_j*), whose signature delta_l h_l must then be carried by base mass on S_l cap J_gamma
   (first-order price gamma t per unit) or cancelled by finer targets (whose own signatures must be cancelled, ...; the regress is cut in
   a window by the box bound on carriers l > l_*). So the re-splitting amplitude is O(Lambda_f t) and its second-order gain O(t^3).
   No contradiction: C's finite analogue has no signatures (it is "outside R_0").
2. Cross-block duplicates (same target in several blocks): u_l - u_{l'} = (delta_l h_l - delta_{l'} h_{l'})/n on disjoint signature sets,
   so trading coefficients between duplicates is pinned exactly like a contact switch. Correct.
3. Degenerate / weak peaks (alpha_k = 0 or tiny): 2.3(c) gives no control, but 2.4(c) one-sidedness (sigma omega_+ <= 0 <= sigma omega_-)
   holds for EVERY peak, and 4.2(c) uses only that. Correct.
4. Huge internal coefficients (|omega^c(k)| up to 2 gap/t, |d_+| up to O(1/t)): no step needs bounded coefficients; 5.1 needs only
   |s| |omega(k)| <= 2 c_1 gap and |s d| <= 2 c_1; C Thm 7.4 is applied to a FIXED averaged certificate. Correct.
5. Uniformity in t: t_eta (2.2) depends on (f, g, eta) only; window constants K_l, n_l depend on l only through Lambda_f(l); c_1, t_1
   (5.1) depend on (f, eps_tr, A_0) with A_0 = K_b + 1 depending on f only. Order of choices in 5.3 is consistent. Correct.
6. c_0 vs l_inf: z in l_inf (non-attaining f), contacts may be infinite; C Thm 7.1's canonical truncation z^N := z 1_{F cup [1,N]} works for
   any z; the only place F finite is needed is 2.5 and the base expansion in 5.1. Correct.
7. Coarse carriers with tiny weight inside a window (c_{l_*} can be < T_hi(l_*)): harmless, pinning is only an upper bound.
8. Fine targets touching coarse signatures: enter the triangular system with total weight (4/3) * 6 t^2. Correct.
9. Finite-model numerics (part 2): consistent.

## 3.2 Remark martin-tail is valid (one-step tail lift) -- PROVED here
G3 works with p_N. For completeness: density of NA((c_0,p_N),F) for infinitely many N implies density for p. Let
s_N(x) := sum_{m>N} |R_m x|_m <= eta_N q(x) <= eta_N p(x) (eta_N = sum_{m>N} m 2^{-m}). Let S in NA((c_0,p_N),F) with ||S||_{p_N} = 1
attained at x_0 (p_N(x_0) = 1, ||S x_0|| = 1). Choose phi in c_0* with |phi(x)| <= s_N(x) for all x and phi(x_0) = s_N(x_0)
(phi = J o L_{>N}, J a norming functional of L_{>N} x_0 in V_{>N}). Put S' := S + (S x_0) (x) phi. Then
||S' x|| <= ||S x|| + |phi(x)| <= p_N(x) + s_N(x) = p(x) and ||S' x_0|| = 1 + s_N(x_0) = p(x_0): S' attains its p-norm 1 at x_0, and
||S' - S||_{L((c_0,p),F)} <= sup s_N/p <= eta_N. Since ||A||_p <= ||A||_{p_N} <= (1 + eta_N)||A||_p, approximating T/||T||_{p_N} by such S
gives dist_p(T, NA_p) <= ||T||_{p_N}(eps + eta_N) -> 0. (Mere closeness p_N <= p <= (1 + eta_N) p_N is not by itself a known mechanism
for transferring NA-density; what makes it work is that the tail s_N is a seminorm whose derivative at x_0 can be added as a rank-one lift.)
So G3's restriction to p_N loses nothing for the final question (density for p).

## 3.3 Imprecisions in part 6 (not affecting Thms A-C)
* 6.3(b) "Only these carriers lose their pinning; all others stay pinned" is inaccurate: if delta'_{l_0} = 0, every COARSER carrier l < l_0
  with kappa_{l_0,l} > 0 (target y_{l_0} touching S_l) is contaminated: its pinning inequality contains kappa_{l_0,l}|Delta c_{l_0}|, so its
  coefficient is slaved to the free one (determined up to O(t)/delta'_l by it), not pinned. The structural picture of 6.3(d) (finitely many
  free coefficients + slaved ones + O(K t)) survives; the sentence in (b) should be corrected. Also, failure of (SR) can come from room ratios
  decaying faster than any vartheta^l along a sequence of l, which weakens pinning gradually rather than removing it.
* 6.3(c) "any f' with finite base support and room ... will do" means "is an admissible approximant in Lemma Z"; it must not be read as
  saying that lowering z on sparse far subsets of signature sets gives dist(rho g, C(f')) < eps -- that is exactly Lemma Z (OPEN).
  Construction of such f' in S_{p*} is legitimate: given (a', z') with q*(a') = 1, z' in B_{l_inf}, z' = sign a' on supp a', put
  zhat' = z' + U e', q_0' = 1/(1 + sum_m |R_m** zhat'|_m), xi' = q_0' zhat', w'_m = J_m(R_m** xi'), f' = a' + L* w'; then f'(xi') = 1 = p**(xi'),
  p*(f') = 1; f' -> f if a' -> a in l_1 and z' -> z coordinatewise (compactness of R_m), so the lowering must be done on FAR coordinates
  (fine: (SR) only needs a vartheta^l fraction, and h_l's mass is 2^{-s}-weighted, so vartheta must then be small).
* 1.1 / Thm B text "covers O1-O4": O4 also listed infinite block sets; G3 covers several blocks for each p_N, and infinite block sets only
  through martin-tail (valid, 3.2 above).

## 3.4 Lemma Z for Round-2 classes
Correct but trivial: P2A Thm 2.1, N2 Thms 1-3, N2-ref Thm 3*, P2x Thm 3.5 already put those mates in Ls(f) for any admissible T (hence
for SLD T), and NA approximants are in R_0. Conditional exactly as the imports are: N2 Thm 3 / N2-ref Thm 3* are PROVED modulo the tuning
hypothesis; P2A Thm 2.1 has the referee's trivial fix (rho >= 1/32 in Step 1). Nothing new is gained from Theorem B here.

## 3.5 Theorem B with infinite F (SKETCH) -- plausible; what must be written
(i) 2.5 has no analogue (U* on l_1(F) is not bounded below), so B_+ 1_F may be unbounded; the clamp replaces it. On F the + side is free
in the direction sign(a_j) (no flip); the excess e_j := (B_+(j) sign a_j - 2|a_j|/t)_+ satisfies e_j <= |Delta B(j)| + f_j, where
f_j := (B_-(j) sign a_j - |a_j|/t)_+ is the minus-side flip excess, sum_j f_j <= t/(4 q_0) (flip cost 2t f_j in E_q, q_0 E_q <= t^2/2);
the other direction is a + side flip, also O(t). (ii) 5.1 must be redone with (C-a'): |b_j| <= 2|a_j|/t (so ||b||_1 <= 2||a||_1/t is
unbounded): no sign flips for |s| <= c_1 t, c_1 <= 1/4, and the Hilbert part has relative perturbation O(c_1 ||U|| ||a||_1/nu), absorbed
by c_1 small. (iii) Truncation to F_t with sum_{F \ F_t}|a_j| <= t^2 costs 2t; rebalance kappa_t. (iv) Final recovery: C Thm 7.4 with
a not in c_00, b in c_00 (C referee: Remark 7.1' extends to b != 0) -- several blocks as in C's remark. No obstruction found.
