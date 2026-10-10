# Q1 referee (a) — part 2: route combination, CM^tr, BR, PM (working file)

Sources re-read for this part: X2_notes 1.4, 2.1-2.3, 3.1-3.5, 4.1-4.2; X2_ref_notes 1-4; X1_notes 2.1-2.6; X1_ref_notes 3, 8; U1_notes 2.1-2.6,
3.1-3.5, 4.1; U1_ref_notes 3-8; V1_notes 4.1 (Proposition TR); note lem:martintail, prop:smooth, prop:approximants, prop:reduction, lem:pair.

## C. Verdicts on the combination claims (with re-derivations)

C1 Route decision (Q1 2.1).  CORRECT.  Route V needs from the coarse system only: (i) coarse statuses at f^# (robust peak, or strict
   non-peak with a positive gap), (ii) the kind-[3] property of near-threshold Omega carriers with the TRUE shift, (iii) exactness of
   Gamma^#(kappa, a) at the realized ratios (for the projection with error K t and the normalization onto one ray).  KN^tr supplies all
   three: (i) X1-ref 8(b); (ii) floor row (X4^0) in (T)-blocks (X1-ref 3.2-3.3), U1-ref (X4) in (KN)-blocks, vs gamma >= 0 in (U)-blocks;
   (iii) X1-ref 8(a).  KN^tr is sign-agnostic per block (part 1, A5), so it serves mixed classes.  Route V never gives an absorber a
   switching coefficient and never tunes one (X2-ref (R-abs)); the absorbers tuned by U1 are first pairs at stages > L (U1 Lemma 3.2), hence
   fine carriers of the window; earlier absorbers are ordinary coarse carriers.  Route X is not on the dependency tree of MT VI.

C2 Kinds of the inactive Omega carriers (my item B1).  RESOLVED (no gap).  In an ACTIVE NEGATIVE block an inactive near-threshold carrier
   cannot exist: at a strict non-peak lem:suplevel(f) gives vs Domega_dec >= -3 gap/t, with gamma below the class threshold A_i K t this
   forces |Delta| M rho <= 3 b M/t + A_i K t/lambda, contradicting |Delta| M >= K_* A_i K t (K_* >= 2 D(L) x Hoffman, U1-ref 4.5); at weak
   peaks eq:peakshift gives the same.  (This is U1-ref 4.1 "Exclusions".)  Hence (KN)-levers d_0 of negative blocks are robust (kind [2]);
   in positive blocks vs Domega(d_0) = Delta |w^#(d_0)| > 0 is inward (kind [3] after the shift trick).  KN-1-held carriers have w^# = 0 and
   gamma = 0, so Domega = 0 and gap = M: kind [2].  D2-pushed inactive carriers of (U)-blocks: Delta = 0, Domega = 0, omega^+ = the clamp of
   V1 Step 5: kind [1'] (gap > 0, |omega| <= 2 gap/t), which Theorem UE accepts (its Step 3 uses only |omega| <= 2 gap^0/t for kind [1]; the
   clause gap >= t^2 is never used there; V1's E'' states [1'] explicitly).  PRECISION P1: (U2) of Theorem UE should read [1'].

C3 Lemma CM^tr.  CORRECT with precisions.
   (b) statuses: re-derived.  c_{L+1} <= b(L, M(L))^2 <= b(w)^2 and b(w) <= min(eta'(w), mu_min/8) give
       C Design c_{L+1} <= C Design eta' mu_min/8 = C (T^4/L) mu_min/8 <= mu_min/16.  The S-0 drift (fine status changes enter C_m only
       through the clamp equation, values of non-owners by <= 4 c_{L+1}^2) is therefore << mu.  Inactive (T)-block values end at
       |u| <= 4 c_{L+1}^2 after the G1 release: their effect on the active statuses is O(D^2 c_{L+1}^4) << mu (KN-1 needs "<< mu", not "= 0";
       the exact hold is needed only against the Design^2 eta'^2 cross effects inside Step A, and it is realized there).
   ORDER (precision P2): Step B (fine structure) is built for the RAY Delta'^* (owner coefficients -Delta''_m lambda_k w(k)), and Delta'^*
   is the corner of the normalization CUBE.  So the order is: class a (read off the data at f) -> Step A -> cube (normalization at the
   cone of f^(A)) -> Step B -> data.  Q1 3.1 Step 2 says "Lemma CM^tr builds its companion; pigeonhole over cubes ..."; it must say
   "Step A of CM^tr; cube; Step B".  (U1-ref 4.5 and 8 have the right order.)  No change of substance.
   (c) the representation and kinds: X2-ref CM'(b) with C2 above.  (d), (e), (f): as X2-ref CM'.

C4 Proposition BR.  CORRECT with precisions.
   (U3) on E (supports created in Step A): in route V the data at a bank/pull of Step A are (contact-like part) + (+-V_fine(j)/2), so
   "contact-like" holds only UP TO the fine residue.  PRECISION P3: at a support coordinate j with sign z_j = sgn a^#_j the base excess of
   a'_j + x_j is |a'_j + x_j| - |a'_j| - z_j x_j <= 2 (z_j x_j)_-, the same as at a contact; so the residue is a tolerated violation of mass
   |V_fine(j)| (cost <= 2 rho |tau| |V_fine(j)|, counted in eps of (U4)); the theta piece is unaffected because b^theta = (chi - 1/2) V_proj
   (V_fine cancels).  X2-ref's C_mix' proof makes the same tacit step ("(U3) at the supports of (1a) by V1 TR(iv)").  KN-1 hold supports:
   |V_fine(j_p)| <= C_f c_{L+1} (fine coefficients are -Delta'' lambda_k w(k), O(lambda), NOT O(lambda/t)), pull mass 24 lambda_l v_l(j_p)
   >= 24 c_{L+1}/Design: t|b| <= |a^#| for t <= T_hi(w).  CORRECT.
   (U6) lever coordinates: Lemma DC's pull coordinates need v in [r, 2^{G} r] with r >= s_1 >= exp(-1/(2T)) >> c_{L+1}; they lie in
   S_l ∩ (s_max, s_far] (2^{-s_far} <= c_{L+1}^2) — inside E_c, as X2-ref (p-LV2) says — and must avoid the coordinates used in Step A
   (Step 0 weak-peak pushes, TU pull/bank of the realization, KN-1 pull/bank, (KN)/(D2) pushes: a BOUNDED number per carrier, not "at most
   two" as Q1 2.3 says).  PRECISION P4: take the lever pull among unused elements of S_l in a v-window of ratio 2^{6 G(L)} (bounded gaps give
   >= 6 elements); the factor enters C_2 only.  The bank coordinate j(l) <= sigma_2(L) because Step A's banks use at most the first element
   of S_l beyond s_max (X2 LV, V1 (C3)/(C4)); (D-lev) as defined (second element) suffices.
   (W-a), (W-b): X2-ref (p-UE6) adds the factor (1 + C_2 K_J) and W_pull <= c delta s_1: both hold since c_{L+1} <= exp(-1/T) and
   W_pull <= C c_{L+1}.  CORRECT.

C5 Lemma PM.  CORRECT (the key new quantitative claim; re-derived).
   (ii) clamp equation 1 = sum_k min(Phi_k (1 - C)/C, v_k)^2 (v_k = |nv_k|/Phi_k): Omega terms identical (d-consistency), coarse-peak terms
   equal Phi_k^2 ((1-c)/c)^2 at both rows near C (clamped: margins >> value moves), fine terms change by <= 2((1-c)/c)(|nv'_k| + |nv_k|),
   sum over fine <= 4 (1 + ||U||) sum_{l > L} lambda_l / A_min <= C_f c_{L+1}; slope >= 2 Phi_*^2 (1 - c)/c^3 from the natural peak (Lemma M2).
   This is INDEPENDENT of the perturbation size Pi (sharper in form than X2-ref 1.2's K (c_fine Pi + W_pull) bound, which it implies).
   (iii) rho_k = |nv_k| C/(Phi_k^2 (1 - C)) for strict non-peaks, so rho'_k/rho^#_k = [C'/(1-C')]/[C^#/(1-C^#)]: exact identity.
   (iv) PHRASING (precision P5): the levers do move Omega values (that is their purpose) — they end EXACTLY at nv^#; what is true is that
   coarse PEAKS meet no lever coordinate (allowedness (c)) and move only at second order through the Hilbert part, and the only
   first-order side effects are on fine carriers (total weight <= 2 c_{L+1}).
   (v) along the cube |P| <= r: Omega values move by <= delta_1 + C_lev r and C(P) by O(r); with r <= r_0 ~ c g_min Phi_min A_min/(m C_lev)
   no status changes (Lemma DC step (5)).  r <= r_0 is implied by s_1 <= s_late (s_late contains gap_min^C).
   Remark: the Puiseux margin enters only gap_min (theta-regime radius s_1 <= T gap_min/(4 rho A_2), Lemma DC radius r_0, (LATE)); it never
   enters c_flat, K_sharp, K, D_cls or A_max.  CONFIRMED against Theorem UE's proof (kind [3] uses only gap' >= gap^0/2).

C6 Lemma S2c^tr.  CORRECT (arithmetic re-derived; see part 3 for the window count).
