# K1 notes (Round 11): items (O-a) and (O-b) of ADDENDUM 10 -- cushion domination at deep-raised companions (Q2 Proposition 3.2) and
# the lever audit at infinite base support; Theorem 5.1 (transport of Master Theorem VI) for lever-regular rows

Setting: paper/martin_density_note.tex (Sections 1, 2, 7, 8), finite block set I = {1..N}, p = p_N, design T_fin^* (Q1's T_fin, option (a),
over the doubly exponential base mu*_s = 2^{-2^{2^s}}, Q2), first rows f with base support F = supp a ARBITRARY.  Sources: r10/Q1_notes.md
(+ Q1_referee_a/b, Q1_refa/refb_notes), r10/Q2_notes.md (+ Q2_referee_a, Q2_refa_notes), r8/U2 (Lemma P, Lemma W, DR-inf, TR-inf, Lemma ND)
with U2-ref, r7/V3 (raise transfer), r7/V1 (TU, TR, ST), r9/X1, X2 with X1-ref, X2-ref, r8/U1 with U1-ref, r5/Z5_ref_notes (Theorem R1).
Part files r11/K1_part1..4.md (reproduced below as Sections 1-4); scripts r11/K1_work/.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
"PROVED" = complete proof here, citing refereed results precisely (several of them once-refereed, as listed in Q1 3.5 and Q2).

## 0. Summary
(O-a) Q2's Proposition 3.2 is PROVED in a CORRECTED form (Proposition K1.A):
  * the CLASS pigeonhole is compatible with Lemma P once its thresholds dominate the Lemma-P pinning constant 8 C_q 2^{J(w)} D(L)/delta_min(L)
    (window-dependent only through 2^{J(w)} = O(Design(L) + log n(w)), absorbed by the window): active carriers then track the
    decomposition (Lemma K1.2) and are never deep at unraised shallow anti-sign coordinates (Lemma K1.3), while pinned carriers fall into the
    inactive (zero) face automatically -- this IS Q2's "projection of the switching to zero";
  * the CUBE pigeonhole (normalization to one shift ray) is NOT compatible in general (its increment has fixed size ~ eps, not ~ t; Remark
    K1.1', HEURISTIC), but it is NOT NEEDED in route V (Lemma K1.1, PROVED: no step of route V uses a common shift);
  * the "clamping" is Z5-ref's deep assignment (Claim 3.1) applied on F with the data's own switching; it costs <= (1 + eta')t/q_0 + K t in l_1
    (closeness O(K t)); the result is (U3^inf) with the ABSOLUTE constant C_+ = 5 (better than Q2's C Design/u), up to support violations of
    mass O(Design c_{L+1}) (tolerated, Q1-refa P3);
  * the deep box-level raise needs no |g_j| term (Q2's raise level 8 Bx_* + |g_j| was for copied base data).
(O-b) Line-by-line lever audit (part 2.3).  Every lever of Q1's route-V construction acts on one carrier's private near coordinates (first six
  elements of S_l beyond s_max(L)) or far (pull) coordinates; at infinite F each is replaced by one of (P1)-(P6) (Lemma K1.4).  Findings:
  * Q2-refa C.3's "bank with offset" block-norm lever is FALSE as a two-sided lever: along the degenerate direction the TOTAL lever position is
    forced to y^T F(0)/(pi y^T p_{m*}) independently of the offset (numerics: negative, i.e. infeasible for a bank, in 48.7% of random cases);
    repaired by TU on the peak (pull + bank) or (P3)/(P4) on the peak (2.2);
  * offsets never create two-sidedness; far coordinates give only one-sided private moves; two-sided private levers are: Z-con/Z-gen at a near
    off-F or thin coordinate (zero-data carriers), TU = near bank + far pull (data-carrying carriers), Hilbert pairs of thick near coordinates
    with robust spread; otherwise single thick S-mass levers with common mode (rank-one perturbation of the identity);
  * V1's donor raise (C3) is not on the tree of route V; V1's (C1), (C2) act off F as at finite F;
  * with common modes, Step A must tune the RATIOS of ALL coarse strict non-peaks (kappa may float: only ratios enter the cone, Lemma K and the
    true shift), and the linearizations become I - g~ h^T bordered by peak resources (Sys-A) resp. Q2's bordered N (Sys-DC).
  LEVER-REGULARITY is defined as a modulus condition (LR_{w,a}) on these two bordered systems (2.4); it holds automatically when every tuned
  carrier is privately tunable (K1.5(a)), and otherwise reduces to explicit bordered scalars (K1.5(b)).
Step B (static ownership) is DISPENSABLE in route V, at finite and infinite F (Lemma K1.S): with (W_exp), every fine-origin misfit is a
  tolerated violation of mass O(Design c_{L+1}) << s_1, and the scrambling hypothesis (U5) of Theorem UE is needed for COARSE carriers only
  (fine carriers contribute <= 4m C c_{L+1} to S_m).  So "Step B's ownership recursion on J_fine \ F" does not arise.  Status stability under the
  new side effects: Lemma K1.ST.
THEOREM 5.1 (transport) is PROVED for lever-regular rows (4.1), modulo the cited refereed chain and the monotone design enlargement (D-K1)
  (rate objects: near moduli, enlarged patterns, spreads and bordered scalars).  Corollary K1.C gives explicit lever-regular classes, including
  Q2 Corollary 5.2 and all rows whose support profile on each S_l is not nearly proportional to the signature profile at design depth.
THE NON-LEVER-REGULAR CLASS (4.3) is characterized exactly: at all large main stages some tuned carrier is (U) UNPULLED (data-carrying, near
  coordinates off F/thin, deep part of S_l support of the opposite sign or super-thick) or (S) SUPPORT-SWALLOWED (six near coordinates thick with
  tiny spreads, a ≈ c_l v_l there), with no anchor and all bordered scalars tiny; exact limit = Q2 Lemma 4.3 / U2 Lemma ND.  It contains Q2's
  (NDN2) and "KN-1 holds in a degenerate raw direction" and is item (O-c) (K2); the (U) case is new.
(LSC-trunc) for every f, hence density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2): still OPEN (reduced to the non-lever-regular class).
No counterexample is claimed; nothing found points to one.

## Results table
| # | Result | Status | Where |
|---|---|---|---|
| 1 | Lemma K1.1 (route V needs no cube normalization) | PROVED | 1.1 |
| 2 | Remark K1.1' (cube increment breaks cushion domination at infinite F) | HEURISTIC | 1.1 |
| 3 | Deep raise without the |g_j| term; choice of J(w), 2^{J(w)} <= Design(L) + 2 log_2(C n(w)) | PROVED | 1.2 |
| 4 | Lemma K1.2 (active coefficients track the decomposition; Lemma-P thresholds) | PROVED | 1.3 |
| 5 | Lemma K1.3 (no deep set at the raised row: deep / robust target / tiny target / shallow non-target cases) | PROVED | 1.4 |
| 6 | Proposition K1.A (= Q2 Prop. 3.2, corrected: (U3^inf) with C_+ = 5, closeness O(K t)) | PROVED | 1.5 |
| 7 | Corollary K1.B (window bookkeeping, (E-d), (E-e')) | PROVED | 1.5 |
| 8 | Lemma K1.4 (first-order action of the resources (P1)-(P6)) | PROVED (from refereed lemmas) | 2.1 |
| 9 | Q2-refa C.3 bank-with-offset is two-sided | FALSE (repaired: TU on the peak) | 2.2 |
| 10 | Line-by-line audit of Q1's levers at infinite F | PROVED | 2.3 |
| 11 | Sys-A in ratio form, Sys-DC bordered; definition of lever-regularity | definition / PROVED structure | 2.4 |
| 12 | Lemma K1.5 (sufficient conditions for (LR)) | PROVED | 2.5 |
| 13 | Lemma K1.6 (realization of Step A and Lemma DC^inf under (LR)) | PROVED | 2.6 |
| 14 | Lemma K1.7 (structure of non-(LR) configurations; exact limit) | PROVED | 2.7 |
| 15 | Lemma K1.S (Step B dispensable in route V; (U5') suffices) | PROVED | 3.1 |
| 16 | Lemma K1.ST (statuses under the new side effects; Lemma PM verbatim) | PROVED | 3.2 |
| 17 | THEOREM 5.1 (transport; (LSC-trunc) at every lever-regular (f, g, rho)) | PROVED mod (D-K1) bookkeeping and the cited chain | 4.1 |
| 18 | Corollary K1.C (explicit lever-regular rows; contains Q2 Cor. 5.2) | PROVED | 4.2 |
| 19 | Characterization of the non-lever-regular class ((U), (S)) | PROVED (as characterization) | 4.3 |
| 20 | (U)-carriers via the ratio trick under a sign condition | SKETCH | 2.7 Remark (1) |
| 21 | (LSC-trunc) at non-lever-regular rows; density for p_N and p | OPEN | 4.3, 7 |

# 1. item (O-a) -- cushion domination of route-V data at a deep-raised companion (Q2 Proposition 3.2)

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Sources: r10/Q1_notes.md (route V, Lemma CM^tr, Prop. BR, Lemma PM, Thm C^tr) with
Q1-refa P1-P8 and Q1-refb P-LIP, P-R, P-HOLD; r10/Q2_notes.md (Thm UE^inf, E^{eng,RT,inf}, Lemma 3.1) with Q2-refa precisions;
r8/U2_notes.md 1.2 (Lemma P), 2.1 (Lemma W), 3.0 (Lemma DR-inf) with U2-ref fixes (s1), G1, W1; r5/Z5_ref_notes.md Section 2 (Theorem R1,
Claim 3.1 = the "deep assignment"); r8/U1_notes.md 2.1-2.4, 4.1-4.7 with U1-ref 3-7; r9/X2_notes.md 3.1, 5.1 with X2-ref 4 (Lemma CM').

## 1.0 Setting
DESIGN.  T_fin^* := T_fin of Q1 (option (a)) over the doubly exponential diagonal base mu*_s := 2^{-2^{2^s}} (U2 1.1), with Design(L)
containing B_mu*(L) := 2^{d(L)}/(delta_min(L) (mu*_{d(L)})^2), d(L) := sigma(L) + 6 * 2^{L+1} (U2-ref (s1), enlarged to cover the six near
coordinates of part 2), and with the following objects in the
rate scheme omega(L) (bookkeeping item (O-d), assumed here and listed again in part 4):
 (R-mod) the moduli |a_s|, s in [1, d(L)] (with |a_s| := 0 for s notin F);
 (R-pat) the minors/cofactor polynomials of the ENLARGED class cones of 1.3 below (patterns in which coordinates of T(L) cap F may carry a
         contact row), for all patterns and classes of level L;
 (R-lev) the lever objects of part 2.
Every window theorem uses the base only through B_mu* (U2 Remark after 1.1, U4 Lemma GW); T_fin^* is N-free.
ROW.  N >= 1, f in S_{p_N*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu), F = supp a ARBITRARY; s_j := sgn a_j (j in F); g in C(f),
rho in (0,1); l_f = l_f(f, N, g, rho) as in Q1 3.1 (all f-constants absorbed, companions in the ball of Lemma M2^inf).
WINDOW.  L >= l_f a main stage, w a clean sub-window of L for f; T := T_lo(w), b := b(w), u := u(w), D := D(L); coarse carriers = stages <= L,
fine carriers = stages > L; T(L) := union of the supports of the coarse targets, s_max(L) := max T(L); sum_{l > L} lambda_l <= C c_{L+1} <=
C b^2 <= C T^8 ((W2) and b <= T^4).
SWITCHING VECTOR.  For route-V data with switching Domega supported in Omega (= all coarse strict non-peaks of the companion), U1 Lemma
1.1(a) gives V := V(Domega) = sum_l c_l u_l over ALL carriers, with c_l = gamma_l (l in Omega), c_k = -Delta''_m lambda_k vs_k for a coarse
peak k of block m (primed shift convention, U1 2.1), and c_k = -Delta''_m lambda_k w(k)/M for fine k.  V_c := sum_{l <= L} c_l u_l (coarse
part), V_f := V - V_c (fine part).

## 1.1 Lemma K1.1 (route V needs no shift normalization).  PROVED.
In route V (Q1 Lemma CM^tr Steps A-B, Proposition BR, Lemma PM, Lemma S2c^tr, Theorem C^tr, Master Theorem VI; X2-ref Lemma CM') the cube
pigeonhole and the normalization increment incr(t) of U1 Proposition 2.2(c)-(e) can be omitted: if for every t of a class set S the data
are built from the PROJECTED class data (Delta'(t), gamma(t)) in Gamma^#(kappa, a) (U1 2.2(a), (b), 2.3, U1-ref 4.5) without increment, then
every conclusion of Lemma CM^tr (a)-(f) and of Proposition BR holds, with (c) improved to sqrt(Gamma^#_w(b^-, omega^-)) <= sqrt(Gamma^#_w(B_-,
Theta_-)) + K t (no C_f p eps term), and Theorem C^tr holds with D_cls(w) replaced by the class count D_cl(w) := (J_Om + 1) 3^{J_Om},
J_Om := |Omega| + N (the pattern is determined by f at w and is not pigeonholed).
Proof.  We list every place where route V could use that all scales of S carry the same shift, and check that none does.
 (1) Step B (X2-ref CM' step (2'), Q1 2.2 STEP B) [moot after Lemma K1.S, which omits Step B; recorded for finite-F readers].  Owners and their
     z-assignments: (a) Omega_act carriers own their far signature sets with
     z = sgn(gamma_l v_l) = eps_l; (b) coarse peaks of active blocks with z = sgn(-Delta''_m vs u) = -sigma_m vs sgn u; (d) fine carriers by
     the recursion varsigma_k := sgn Y_k, z := varsigma_k sgn u_k (negative blocks) or -varsigma_k sgn u_k (positive blocks).  Every rule
     uses only the SIGNS sigma_m = sgn Delta''_m and eps_l, which are fixed by the class (U1 2.3: the class records the active set and the
     signs; U1-ref 4.4: sgn Delta'_m is constant on the class cone), and Y_k, which is computed from coordinates fixed before k and does not
     involve the data.  Dominance (U1 Lemma 4.2) is stated "for every Delta'' in the class (active |Delta''_m| >= A_2 K T/2, |Delta''| <= C_f)
     and every gamma(t) of the class"; U1-ref 7 (owners inside absorber blocks) uses only the least absorber entry.  The only construction
     of U1 that is built for ONE shift value is the Schauder completion of configuration (ii) (U1 Lemma 4.4, route X); route V replaces it by
     anti-alignment with tolerated violations (X2 Lemma CM, proof of Theorem C_mix: "no Schauder completion is needed").
 (2) True versus reference shift (U1 Lemma 4.6).  For each t separately, (X3) at f^# and at the realized point (u', kappa') give
     Delta''_m(t) kappa^#_m = sum_{Omega_act,m} u_l(zhat^#) gamma_l(t) and Delta'_m(t) kappa'_m = sum u'_l gamma_l(t); with u^# = u' on Omega_act
     after Step A (exact re-realization) Delta''(t) = Delta'(t) kappa'/kappa^#.  The bound |Delta'' - Delta'| <= C_f Design c_{L+R_cl+1} and the
     trace-correction estimate (U1 Lemma 4.6(b)) are per scale and unchanged; the signs and activity are kept (U1 Lemma 4.6(c)).
 (3) Kind [3] (Q1 2.2 proof of (c)(ii), X1 2.2(iii), U1-ref 4.1): "every point of the cone is inward at f^# with the true shift"; the
     increment was one more point of the cone.  Without it the data are points of the cone.
 (4) Window family (X2 3.1, Q2 2.2): (U1)-(U7) are conditions on each piece separately; (U5) concerns I_- := {m : Delta_{i,m} < 0 for some i},
     which is the set of negative active blocks of the class; (U7) is a per-piece bound.  Theorem UE (UE^inf) builds f' from the masses
     max_i |b^theta_i| and the levers on the common Omega; Theorem E^eng (E^{eng,RT,inf}) averages per-piece bounds by convexity.  No common
     shift is used.
 (5) Lemma PM, Lemma S2c^tr: independent of the data.
 (6) Counting (Theorem C^tr, Q1-refa P8): with no cubes the pigeonhole gives |S| >= n(w)/D_cl(w); every later use of |S| is a lower bound.
 The Gamma estimate: without the increment the - side differs from the decomposition's - side only by the projection and class-zeroing
 errors (U1 2.2(b), 2.3), so sqrt Gamma^#_w(b^-, omega^-) <= sqrt Gamma^#_w(B_-, Theta_-) + K t as in V1 TR Step 5 / U1 2.2(e).  QED
Remark K1.1' (why the increment must be dropped at infinite F).  HEURISTIC (no explicit row constructed).  incr(t) is a nonnegative
combination of extreme rays with coefficients up to the cube side eps = c_f (u/Design)^C (NOT proportional to t), and for class-G carriers
every ray has eps_l gamma_l >= 0 ((X2)).  At an anti-sign support coordinate j in S_l cap F below the raise depth it adds anti-sign switching
up to C p eps v_l(j), which exceeds the cushion |a_j|/t whenever |a_j| < c p eps t v_l(j); Lemma P controls only the decomposition's own
amplitude (|tau_l| v_l(j) <= (16/5)|a_j|/t or tau_l pinned), so an active carrier of small amplitude (between K_*^2 K t and ~eps) can have such
coordinates.  The resulting anti-sign mass is not O(s_1) and cannot be tolerated as a violation.  Q2's sketch ("they are sub-patterns, so
V2's minors cover them") is right for the CLASS part of the pigeonhole and wrong for the CUBE part; Lemma K1.1 removes the cube part.

## 1.2 The deep raise (U2 Lemma W (R), Q2 3.2), adapted.  PROVED.
Box function Bx_L(j) := sum_{l <= L} lambda_l |u_l(j)| (a design function; sum_j Bx_L(j) <= sum_l lambda_l <= 1).  For an integer J put
   R(J) := {j in F : j >= J, |a_j| < 8 Bx_L(j)},   Delta a := sum_{j in R(J)} s_j (8 Bx_L(j) - |a_j|) e_j^*,   lambda_r := q*(a + Delta a),
and let f^r be the row with forced data ((a + Delta a)/lambda_r, z) (V3 2.0: a same-sign raise on F; F, z, K, rooms unchanged).
 (a) raise mass <= psi_L(J) := 8 sum_{j >= J} Bx_L(j) -> 0 (J -> infinity); ||U^* Delta a|| <= mu*_J psi_L(J) <= 8 mu*_J (mu* decreasing).
 (b) (V3 Lemma 2.1, 2.2, Cor. 2.4) lambda_r >= 1, lambda_r -> 1, p*(f^r - f) -> 0, and for every r in R
        p*(f^r + r rho g) <= 1 + (s(lambda_r rho r) - 1)/lambda_r + eps'_r,   eps'_r := 2||U^*Delta a|| + p*(L^*(w^r - w)) <= C_f mu*_J log(e/mu*_J).
 (c) (U2 Lemma DR-inf, U2-ref D1) every value moves by <= C mu*_J, every rate object of level L (incl. (R-mod), (R-pat), (R-lev)) by
     <= C Design(L) mu*_J; (R6)-type shift costs are exactly invariant.
CHOICE.  J = J(w) := the least J >= d(L) + 1 with C_f mu*_J log(e/mu*_J) <= min{ theta_w T^2, b^2 Phi_min(L)/(C Design(L)) } (theta_w of
Q1 CM^tr(f)).  Since mu*_J = 2^{-2^{2^J}}, 2^{J(w)} <= max{2^{d(L)+1}, 2 log_2(8 log_2(1/T) + C_f')}, and log_2(1/T) <= 2 n(w) + log_2(1/T_hi(w))
<= 3 n(w) for L large (T_hi(w) <= T_lo(w^-) and the earlier windows are short compared with n(w)).  So 2^{J(w)} <= Design(L) + 2 log_2(C n(w)).
Then at f^r every tiny rate object of f is <= 2b and every robust one >= u/2 (clean with factor 2), the budget lemmas hold at f^r for the
mate g^r := g - (g(xi^r)/q_0^r) a^r on the window with eta' -> 0 (V3/V3-ref (I1)), and (a) of Theorem E^{eng,RT,inf} holds at f^r.
[Q2's raise level 8 Bx_* + |g_j| is not needed: the |g_j| term was for copied base data; the deep assignment of 1.5 replaces copying.]

## 1.3 Classes with Lemma-P thresholds and enlarged patterns
PATTERN ENLARGEMENT.  For j in T(L) cap F (a target coordinate in the support; at most s_max(L) of them) the clean sub-window gives
|a_j| <= b ("tiny support") or |a_j| >= u ("robust support") ((R-mod)).  The pattern kappa records this label.  In the class cone
Gamma^#(kappa, a) (U1 2.1, U1-ref 4, X1 2.2) add for every TINY support coordinate j in T(L) the CONTACT ROW
   (X1^F)   s_j L(Delta', gamma)(j) >= 0
(the (X1) row of a contact of sign s_j).  Its entries lambda_l u_l(j), lambda_k u_k(j) (peak traces) are non-weight design data, so the
weight-freeness of X1 2.2(iv), Lemmas NLM, GEN, QC and Proposition KN^tr (Step A) apply verbatim to the enlarged patterns ((R-pat)).
THRESHOLDS.  Let C_q := (8/3)(2/q_0 + 8) (Lemma P at rows in the ball, q_0^r >= q_0/2), H the Hoffman constant of the class cones
(<= C Design^C/u after exactification, U1-ref 4.3), K := C_f (Design/u)^C the projection constant of U1 2.2(a)-(b), and
   K_P(w) := 8 C_q 2^{J(w)} D(L)/delta_min(L),     K_*(w) := max{ K_*^{U1}, 5(H J_Om + 2), (K_P(w)/K)^{1/2} }.
Classes are read off the decomposition data at f^r with A_1 := K_*, A_{i+1} := K_* A_i (U1 2.3, U1-ref 4.5).
Lemma K1.2 (active coefficients track the decomposition).  PROVED.  Let t in S, c_l (l <= L) the data coefficients of 1.0 and c^act_l :=
-Delta theta_l the actual coefficients of the decomposition (B_+-, Theta_+-) at f^r (eq:DeltaB: Delta B = -sum_l Delta theta_l u_l).  Then for
every coarse l either c_l = 0, or |c_l - c^act_l| <= |c_l|/5 and |c_l| >= K_*^2 K t/(4 D(L)).
Proof.  Omega carriers: c_l = gamma_l(t), the projected component; class zeroing moves components by <= A_{i(t)} K t each, the projection onto
Gamma^#(kappa, a(t)) by <= H J_Om A_{i(t)} K t + K t (U1 2.2(a)-(b)); an active component has |gamma_l| >= A_{i(t)+1} K t = K_* A_{i(t)} K t >=
5(H J_Om + 2) A_{i(t)} K t, so the total error is <= |gamma_l|/5.  Inactive components: gamma_l(t) = 0.  Coarse peaks k of block m: c_k =
-Delta''_m(t) lambda_k vs_k and, by eq:peakshift at f^r, c^act_k = -Delta'_dec,m lambda_k vs_k + e_k with |e_k| <= C_f D t/u at peaks of
relative margin >= u/2 (U1 2.2(a)(i)); Delta''(t) = Delta'(t) kappa'/kappa^# (K1.1(2)), |Delta'(t) - Delta'_dec(t)| <= (H J_Om + 2) A_{i(t)} K t
for active shifts, Delta'(t) = Delta''(t) = 0 for inactive ones; with |Delta'(t)| >= K_*^2 K t and lambda_k >= 1/D(L), M^# >= 1/2, the same
arithmetic gives the claim (K_*^{U1} absorbs C_f D/u).  QED

## 1.4 Lemma K1.3 (no deep set at the raised row).  PROVED.
For every t in S and every j in F:
     s_j V_c(j) >= -4|a^r_j|/t - tr_j,
where tr_j := |sum_m (Delta''_m(t) - Delta'_m(t)) P_m(j)| (trace correction, nonzero only at j in T(L)) and sum_j tr_j <= C_f Design(L) c_{L+1}
+ C_f c_{L+1}^2/t.
Proof.  Coefficient bound: for coarse l, |c_l| <= C_f D(L) lambda_l.  [Omega: c_l = lambda_l(Domega(k) - Delta_m w^#(k)); by (U1) Gamma_w <= 2
and X2 Proposition J(a), ||D_m Domega||_2 <= C_f, so |Domega(k)| <= C_f/Phi_k <= C_f D(L); |Delta_m| <= C_Delta ((U7)).  Peaks: |c_k| <=
C_Delta lambda_k.]  Hence |V_c(j)| <= C_f D(L) Bx_L(j).  Four cases.
 (D) j >= J.  |a^r_j| >= 8 Bx_L(j)/lambda_r >= 4 Bx_L(j) (1.2), so 4|a^r_j|/t >= 16 Bx_L(j)/t >= |V_c(j)| for t <= T_hi(w) <= 16/(C_f D(L)).
 (Tr) j in T(L), robust: |a^r_j| = |a_j|/lambda_r >= u/2, so 4|a^r_j|/t >= 2u/T_hi(w) >= C_f D(L) >= |V_c(j)| (T_hi(w) <= u/(C Design(L))).
 (Tt) j in T(L), tiny: the data satisfy (X1^F) exactly at the reference coefficients, s_j L(Delta'(t), gamma(t))(j) >= 0; V_c(j) =
      L(Delta''(t), gamma(t))(j) = L(Delta'(t), gamma(t))(j) + sum_m (Delta''_m - Delta'_m) P_m(j) (U1 Lemma 4.6(b)); so s_j V_c(j) >= -tr_j.
      The bound on sum tr_j is U1 Lemma 4.6(a)-(b) (per scale, K1.1(2)).
 (S) j < J, j notin T(L), j in S_l for a coarse l.  Among coarse carriers only l lives at j (coarse targets lie in T(L); signature sets are
      disjoint; (P1)), so V_c(j) = c_l v_l(j).  If c_l = 0 there is nothing to prove.  Otherwise suppose s_j c_l v_l(j) < -4|a^r_j|/t.  By Lemma
      K1.2, c^act_l has the sign of c_l and |c^act_l| >= (4/5)|c_l|, so with tau_l := eps_l c^act_l (any sign convention eps_l) the coordinate is
      of the type opposite to the switching direction and |tau_l| v_l(j) > (16/5)|a^r_j|/t: (P.2) of Lemma P holds at f' := f^r (j is UNRAISED,
      j notin T(L), l <= L).  Lemma P gives |c^act_l| <= C_q t/v_l(j) <= (5/4) C_q 2^{J} t/delta_min(L) (v_l(j) = delta_l 2^{-j}/n_l, n_l <= 5/4).
      [Lemma P's term sum |r_s| <= 8t^2 needs sum_{l''>L} lambda_{l''} <= t^3, true: <= C T^8.]  Hence |c_l| <= (25/16) C_q 2^J t/delta_min(L),
      while Lemma K1.2 gives |c_l| >= K_*^2 K t/(4 D(L)) >= K_P(w) t/(4 D(L)) = 2 C_q 2^J t/delta_min(L): contradiction.
 (O) j < J, j notin T(L), j in no S_l with l <= L: no coarse carrier lives at j, V_c(j) = 0.  [A coordinate of S_l with l > L is not in T(L) by
      allowedness (a), so it falls under (O).]  QED
Remark.  (D) is the deep raise, (S) is U2's pinning-by-Lemma-P with the pinned carriers sent to the zero face by the CLASS pigeonhole (they
are inactive because their actual amplitude is below K_P t <= K_*^2 K t), (Tr)/(Tt) are the clean-sub-window dichotomy of the support moduli
of the target coordinates (U2 Lemma W (S1) and its Sigma-rows, which are automatic at clean sub-windows).  This is exactly Q2's steps (i)
"projecting the switching ... to zero" and the cushion bookkeeping, now inside Q1's class pigeonhole.

## 1.5 The deep assignment on F (Z5-ref Theorem R1, Claim 3.1) and Proposition K1.A (= Q2 Proposition 3.2).  PROVED.
Let f^# be a companion of f^r produced by Q1's Step A with the lever resources of part 2 (Step B is omitted, part 3 Lemma K1.S), and let
F_low ⊂ F be the set of support coordinates LOWERED by those resources (part 2): (i) THIN NEAR coordinates (|a^r_j| <= b, j in N_l) used
as bank or Z-con coordinates -- for a data-carrying carrier l they have s_j = eps_l and become contacts of sign eps_l (then banked: support of
sign eps_l again); for a zero-data carrier they become contacts and may be z-moved; (ii) FAR PULL coordinates (|a^r_j| <= x_max, s_j = eps_l),
which are then pulled, i.e. become support coordinates of sign -eps_l with mass 24 lambda_l v_l(j) at f^#.  Properties of f^# used (proved in part 2 / Q1): (P#1) |a^#_j| >= |a^r_j|/2 for
j in F \ F_low (q*(A^#) <= 2; S-mass levers keep |A(p)| >= |A_1(p)|/2, Q2-refa (p2.2)); (P#2) Step-A supports off F are as in Q1 Prop. BR
((U3) contact-like or t|b| <= K_3 |a^#|, up to V_fine, Q1-refa P3); (P#3) the coarse statuses of Q1 CM^tr(b).
DATA.  For t in S let (B_+-, Theta_+-) be the decomposition of g^r at f^r at scale t, V = V(Domega(t)) the route-V switching (K1.1), and
A_j := 2|a^r_j|/t (j in F).  On F \ F_low define b^+_1 by Z5-ref's deep assignment with X := V_c|_F: x_j := s_j B_+(j), y_j := s_j(B_+(j) - V_c(j)),
sigma_j := the point of [y_j - A_j - tr_j, x_j + A_j] closest to 0, b^+_1(j) := B_+(j) - s_j sigma_j (the interval is nonempty by Lemma K1.3:
x_j - y_j = s_j V_c(j) >= -2A_j - tr_j).  On F_low put b^+_1(j) := chi_j V_c(j) with chi_j in [0,1] (contact split; at a pulled
coordinate this is V1 TR(iv)'s pull data; at a coordinate of a zero-data carrier V_c(j) = 0).  Off F the + side is Q1's:
chi V_proj + V_fine/2 on contacts, Q1's data on the Step-A supports.  Then
     b^+ := b^+_1 + (off-F part) - kappa a^#/a^#(zhat^#),  kappa := (b^+_1 + off-F part)(zhat^#),   b^- := b^+ - V,   omega^+- as in Q1.
PROPOSITION K1.A.  For every t in S, (b^+-, omega^+-) represent g_t at f^# and form, together with the other scales of S, a window family at
f_0 := f^# satisfying (U1), (U2), (U4)-(U7) of Q1 Proposition BR and
 (U3^inf) with C_+ := 5:  (s_j b^+(j))_- <= 5|a^#_j|/t and (s_j b^-(j))_+ <= 5|a^#_j|/t + |V_f(j)| + tr_j for every j in F \ F_low,
 and contact-likeness up to |V_f(j)| on F_low;
the excess terms |V_f(j)| + tr_j are violations (Q1-refa P3: at a support coordinate the base excess of a'_j + x_j is <= 2(z_j x_j)_-) of total
mass <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/t, counted in eps^viol of (U4); and
     p*(g - g_t) <= K_data t,   K_data := J_Om K_*(w)^{J_Om + 1} K + C_f,
     ||B_+ 1_F - b^+_1||_1 <= (1 + eta') t/q_0^r + K t + 7 C c_{L+1}/t.
Proof.  (i) Claim 3.1 of Z5-ref, re-derived with the extra slack tr_j: from lem:flip at f^r, s_j B_+(j) >= -|a^r_j|/t - f^+_j and s_j B_-(j)
<= |a^r_j|/t + f^-_j, sum_F (f^+_j + f^-_j) <= (1 + eta')t/q_0^r.  The point of [y - A - tr, x + A] closest to 0 has modulus (-x - A)_+ +
(y - A - tr)_+ <= f^+_j + f^-_j + |(Delta B - V_c)_j| (B_+ - V_c = B_- + (Delta B - V_c)); so |B_+(j) - b^+_1(j)| <= f^+_j + f^-_j + |(Delta B -
V_c)_j|, and s_j b^+_1(j) = x_j - sigma_j >= -A_j, s_j(b^+_1 - V_c)(j) = y_j - sigma_j <= A_j + tr_j.  On F_low: |B_+(j) - chi_j V_c(j)| <=
|B_+(j)| + |V_c(j)| is bounded by A_j + f^+_j + f^-_j + |(Delta B - V_c)_j| for the choice chi_j := the projection of s_j B_+(j)/(s_j V_c(j)) onto
[0,1] when s_j V_c(j) > 0 (chi_j := 0 otherwise), because the flip bounds at f^r give -A_j/2 - f^+ <= s_j B_+(j) <= s_j V_c(j) + A_j/2 +
f^- + |(Delta B - V_c)_j| (V_c(j) = c_l v_l(j) has the sign s_j = eps_l at a lowered coordinate of a data-carrying carrier, and vanishes
at one of a zero-data carrier); sum_{F_low} A_j <= 2(|Lambda| b + |Lambda| x_max)/t <= 4T/(L Design(L)) + 2|Lambda| b/t <= K t
(|F_low| <= 2|Lambda|, x_max of part 2, b <= T^4).
At a pulled coordinate the cushion at f^# is the pull mass 24 lambda_l v_l(j) >= t|V(j)| (t <= T_hi, |c_l| <= C_f D lambda_l), as in V1 TR(iv).
(ii) ||Delta B - V_c||_{l_1(F)} <= sum_{l <= L} |c^act_l - c_l| ||u_l||_1 + ||sum_{l > L} Delta theta_l u_l||_1 <= K t + 6 sum_{l>L} lambda_l/t
(Lemma K1.2 errors are the projection/zeroing/peak errors of U1 2.2(a)-(b), 2.3, summing to <= K t; lem:box for fine carriers).  This gives
the stated l_1 bound and, with ||V_f||_1 <= C_Delta sum_{l>L} lambda_l <= C c_{L+1}, the closeness: g_t - (Q1's g_t) = b^+_1 - B_+ 1_F +
(kappa terms), so p*(g - g_t) <= (Q1's K t, with K_data of Q1-refa 2.7 for the zeroing) + (1 + ||U||)||B_+ 1_F - b^+_1||_1 <= K_data t.
(iii) Cushion.  |kappa| <= K t as in V1 TR Step 5 / Z5-ref Claim 3.2 (b^+_1 differs from B_+ 1_F by O(K t) in l_1, |B_+(zhat^r)| <= t/(2q_0^r) by
lem:budget(a), |<U^*B_+, e^# - e^r>| <= ||B_+||_1 ||e^# - e^r|| <= (C/t) Design T^3 <= t).  On F \ F_low, by (i) and (P#1):
(s_j b^+(j))_- <= A_j + |kappa| |a^#_j|/a^#(zhat^#) <= 4|a^#_j|/t + 2K t |a^#_j| <= 5|a^#_j|/t, and (s_j b^-(j))_+ = (s_j(b^+_1 - V_c - V_f)(j) -
kappa s_j a^#_j/a^#(zhat^#))_+ <= A_j + tr_j + |V_f(j)| + 2Kt|a^#_j| <= 5|a^#_j|/t + tr_j + |V_f(j)| (Kt^2 <= 1/2).  On F_low the + side is
chi_j V_c(j) and the - side -(1 - chi_j)V_c(j) - V_f(j): at a pulled coordinate t|b^+-(j)| <= t|V(j)| <= 24 lambda_l v_l(j) = |a^#_j| (the
finite-F alternative of (U3), i.e. (U3^inf) with C_+ = 1); at a lowered near coordinate of a data-carrying carrier the data are contact-like
for the sign eps_l = s_j (zero anti-sign part on both sides) up to |V_f(j)|; at a coordinate of a zero-data carrier V_c(j) = 0 and the data
are the fine residue (violation; split 1/2 at a free coordinate so that b^theta = 0).
(iv) The other hypotheses.  Only the base part on F changed; omega^+- and the off-F data are Q1's (with K1.1), so (U2), (U6), (U7) are Q1's
(with the levers of part 2), and (U5) is replaced by (U5') of Lemma K1.S(c).
(U1): t||b^+-||_1 <= t(sum_F A_j + 2||V||_1 + ...) <= 4||a^r||_1 + C_f(1 + D(L) t) <= A_0 (Claim 3.1(iv): |b^+_1(j)| <= A_j + |V_c(j)| + tr_j);
Gamma: sqrt(Gamma^#_w) is a seminorm and q_0 h(y) <= ||U||^2 ||y||_1^2/nu, so the base change of l_1-size O(K t) changes sqrt Gamma by O(K t),
absorbed as in Q1.  (U4): the violation list of Q1 CM^tr(d) plus the excesses above, all with b^theta = 0 at violated FREE coordinates
(the new violations sit at support coordinates, where (H3) is not required: P3).  QED
COROLLARY K1.B (window-constant bookkeeping).  PROVED.  With (W_exp) and the choices above: C_+ = 5 is ABSOLUTE (Q2's C Design/u is not
needed), so c_flat(w) >= c_f u(w) exactly as in Q1 (gamma_B(w) = min_m M_m u/4); K_data <= C_{f,N} (Design(L)/u)^{C(L+N)} (log n(w))^{(L+N+2)/2}
(K_*(w) <= C_f (Design/u)^C (2^{J(w)})^{1/2}, 2^{J(w)} <= Design(L) + 2 log_2(C n(w))); the class count D_cl(w) <= (L + N + 1) 3^{L+N}; and (E-d), (E-e') of Theorem E^{eng,RT,inf} hold along L -> infinity: |S| c_flat/K_data >= n(w) c_f u/(D_cl K_data) -> infinity
because n(w) >= L 2^{L^3} Q(w), Q(w) >= (4 Design/u)^{omega(L) + L^2 + 20} (Q1-refa P8) and (log n)^{L+N+2} <= n^{1/4} once log n >= L^3 >> (L+N)^2;
eps' = eps'_r + p*(f^# - f^r) <= 2 theta_w T^2 by the choice of J (1.2) and Q1 CM^tr(f).

# 2. item (O-b) -- line-by-line lever audit at infinite F; lever-regularity

Setting and notation of part 1.  "Row" = the row at which a lever acts: f_1 := f^r after Step 0 (for Step A of Q1 = KN^tr Step 4),
or the PRE-ROW f_1 of Theorem UE^inf (for Lemma DC^inf).  For a coarse carrier l: val_l := eps_l u_l(xhat_1) (eps_l the sign of l's
switching if l carries data, any fixed sign otherwise); g_l := eps_l <U^*u_l, e_1>; nu_1 := ||U^*A_1||.  x := the correction scale of
the system (x_A := C Design(L) eta' for Step A, X1-ref 8; x_DC := r, the lever radius of Lemma DC, X2-ref (p-DC1)); Lambda := the tuned
set of the system.

## 2.0 The lever menu (definitions)
NEAR COORDINATES.  N_l := the first six elements of S_l beyond s_max(L); all lie in (s_max(L), d(L)], d(L) := sigma(L) + 6 * 2^{L+1}
(bounded gaps G_l = 2^{l+1}); Design(L) contains 2^{d(L)}/(delta_min(L) (mu*_{d(L)})^2), so every near coordinate s has lever efficiency
mu*_s^2 v_l(s)/nu >= 1/Design(L) ((D-lev), X2-ref (p-LV1), U2-ref (s1)).  By (R-mod), at a clean w each near s is OFF F, THIN (|a_s| <= b) or
THICK (|a_s| >= u); by (R-lev) the SPREADS |1 - rho_s/rho_{s'}| (rho := a/v_l; s, s' thick in N_l) are tiny (<= b) or robust (>= u).
FAR COORDINATES.  Far_l(x) := {j in S_l : x <= v_l(j) <= x_max}, x_max := T^2/(L Design(L) |Lambda|) (so that zeroth-order moves of size
x_max per carrier cost o(T^2) in total).  A far j is PULLABLE for l if eps_l z_1(j) > -1/2 and j notin F, or j in F, s_j = eps_l and |a^r_j| <=
x_max (it is then lowered to a contact first).  [A far coordinate gives only ONE-sided private moves: a contact sits at the extreme of
its range, so z-moves there can only lower eps_l val_l, and a bank at a far coordinate has efficiency mu*_j^2 v_l(j), negligible.  Two-sided
private moves need a near coordinate (bank efficiency >= 1/Design) or a pull + bank pair.]
DATA STATUS.  l is ZERO-DATA if c_l(t) = 0 for all t in S (inactive Omega carriers, KN-1-held carriers, D2- and KN-pushed carriers,
coarse peaks of inactive blocks), NONZERO-DATA otherwise (active Omega carriers, coarse peaks of active blocks).
RESOURCES (all two-sided except where said):
 (P1) zero-data near lever: l zero-data and a near s in N_l that is off F, or thin (then first LOWERED to a contact of sign s_s, cost <= b):
      at a contact (Z-con of X2 2.1, with eps := z(s)): inward z-move for P <= 0, bank for P > 0; at a free coordinate: Z-gen (X2 Lemma LV(c)).
      Zero data make every state of s admissible.
 (P2) TU: l nonzero-data, a near BANK coordinate s in N_l that is off F (a contact of sign eps_l, see 2.1(b)) or thin with s_s = eps_l, and a
      PULLABLE j_p in Far_l(x) (V1 Lemma TU; U2 TR-inf (a), (a')).
 (P3) Hilbert pair: two thick s, s' in N_l with robust spread (U2 TR-inf (c)).
 (P4) single S-mass: a thick s in N_l (Q2 4.0); column e_l - h_s g, h_s := |a_1(s)|/(nu_1 v_l(s)) (normalized units).
 (P5) anchor: a thick p in F ∩ [1, d(L)] lying in supp u_k for no coarse carrier k of Lambda: column -g (plus effects on carriers meeting p,
      all outside Lambda).
 (P6) block-norm lever of block m (Sys-DC only): a two-sided resource ((P1)-(P4)) of a coarse PEAK of block m with relative margin >= u/2.
l is PRIVATELY TUNABLE if it has (P1) (zero-data) or (P2) or (P3).

## 2.1 Lemma K1.4 (first-order action of the resources).  PROVED.
(a) (P1): X2 Lemma DC (Z-con, Z-gen; refereed): slope exactly 1 on both sides (z-moves change u_l(xhat) by v_l(s) dz_s and do not change e;
    the bank has normalized slope 1 up to O(||X_lev||^2), Lemma M1(i)); the only other carriers with u_k(s) != 0 are fine (s beyond s_max(L) in
    S_l: allowedness (a), (c)), of total weight <= 2 sum_{k > L} lambda_k (W_lev, c_tiny).  The preliminary lowering of a thin s costs <= C_f b
    in p* (companion cost, Z3 Lemma 3.1) and moves e by <= 2 mu*_s b/nu (V1 Lemma B(iii)), hence every value by <= C b: a move of the size of
    (C1)/(C2), done in Step 0 BEFORE the Lojasiewicz step (so the tiny objects are re-exactified afterwards).  A far pull coordinate in F is
    lowered likewise (cost <= C_f x_max; values move by <= C mu*_j x_max << b).
(b) (P2): at a near off-F coordinate s of a NONZERO-data carrier the exact data V_t(s) = c_l v_l(s) are admissible ((X1) of the class cone on
    E_c, or the contact-row of part 1.3), so s is a contact of sign sgn(c_l) =: eps_l (a FREE near coordinate would force c_l = 0); a thin near
    coordinate of a nonzero-data carrier has s_s = eps_l (part 1, Lemma K1.3 (S): an anti-sign thin coordinate below J forces |c_l| <=
    4b/(t v_l(s)) < K_*^2 K t/(4D(L))), so after its lowering (cost <= b) it is a contact of sign eps_l whose data are contact-like.  V1 Lemma TU
    verbatim with the bank at s (a mass of sign eps_l off F^r) and the pull at j_p (if j_p in F: first lowered, cost <= C_f x_max; then the pull
    mass 24 lambda_l v_l(j_p) of sign -eps_l).  Two-sided: the pull
    shifts eps_l val_l DOWN by (1 + eps_l z_1(j_p)) v_l(j_p) >= v_l(j_p)/2 >= x/2 and the bank provides every upward correction continuously
    (V1 Lemma TU Step 2's explicit fixed point).  Cross effects: second order, C_T x^2 (V1 Lemma TU(b), X2 Lemma M1(i)).
(c) (P3): U2 Lemma TR-inf case (c) (refereed): private, two-sided, efficiency >= u/Design(L), cross effects O(Design^2 u^{-4} x^2).
(d) (P4): Q2 4.0 / Q2-refa C.1 (refereed, numerically confirmed): per unit step eps_k d val_k = delta_{kl} - g_k h_l for every carrier k with
    u_k(s) = 0 for k != l (all coarse k != l: s beyond s_max(L) in S_l); two-sided (raise unlimited; lowering by <= |a_1(s)|/2 >= u/2 >> x
    Design: Q2-refa (p2.2)).
(e) (P5): the same formula with no private part: eps_k d val_k = -g_k h_p for coarse k with u_k(p) = 0; two-sided as in (d).
(f) Every resource moves e by <= C Design(L) x (Lemma M1(iv) for support moves, V1 Lemma B for masses off F) and moves no z outside its
    own coordinates; hence robust objects of level L move by <= C Design^C x/u << u.

## 2.2 Correction to Q2-refa C.3 (bank with offset).  FALSE as stated; repaired.
Q2-refa C.3 claims that a BANK at a private contact of a peak k* of a shifted block, placed with a base mass m_0 = 2 K r beta_j and varied by
beta_j P_0 (|P_0| <= K r), is a two-sided block-norm lever satisfying the conclusions of Corollary 4.2.  This fails along the degenerate
direction.  Proof.  With N := D - gt h^T - sum_m p_m q_m^T degenerate (left null vector y, y^T p_{m*} != 0 -- the only case in which the
block-norm lever is needed), every solution of the linearized equation F(0) + N P - pi p_{m*} P_0^{tot} = 0, where P_0^{tot} := m_0/beta_j + P_0
is the lever position measured from ZERO mass (the base mass is itself a move along the lever column), satisfies
      P_0^{tot} = y^T F(0) / (pi y^T p_{m*})
(apply y^T).  So the offset does not enter the forced total; the bank requires P_0^{tot} >= 0, i.e. a SIGN condition on y^T F(0)/(pi y^T p_{m*}),
which is not controlled (F(0) is produced by the theta-masses and the pre-row moves).  Equivalently: with the base mass included in the
pre-row, |F(0)|_inf >= |pi p_{m*}| 2Kr - |F_orig(0)|, so Corollary 4.2's hypothesis K|F(0)|_inf <= r/2 fails as soon as 4K|pi p_{m*}| > 1.
[Numerics, K1_work/offset_check.py: 2000 random degenerate bordered systems; the total lever position equals y^T F(0)/(pi y^T p) to 1e-8
independently of the offset; it is negative (infeasible for a bank) in 48.7% of the instances.]
REPAIR (PROVED).  A two-sided block-norm lever of a shifted block m* is any two-sided resource of a coarse peak k* of m* with robust margin:
(P2) TU on the peak (bank at a near contact of S_{k*} + pull at a pullable far coordinate; at the pull the peak's data -Delta''_{m*} lambda_{k*}
vs v_{k*}(j_p) are anti-sign for the new support sign and are dominated by the pull mass: t|Delta''| lambda v <= C_Delta lambda v <= mu_p/24, the
peak's margin u/2 >> C_lev r), or (P3)/(P4) on the peak (its column then carries the common mode -h g as well: Q2-refa C.3(iv)'s rank-one
perturbation argument applies verbatim), or (P1) if Delta_{m*} = 0 (Q2 Corollary 4.2 as stated).

## 2.3 The audit (every lever of Q1's route-V construction; replacement at infinite F).  PROVED line by line from 2.1.
| move of Q1 (source) | carrier / data | finite-F lever | at infinite F |
|---|---|---|---|
| V1 (C1) close class-G rooms (Q1 CM^tr Step 0) | z-moves on S^nat_l = S_l \ (F ∪ T(L)) | off F | unchanged (off F by definition) |
| V1 (C2) close tiny target rooms | z-moves on T(L) \ F | off F | unchanged |
| V1 (C3) donor raise | -- | NOT on the tree of route V (U1-ref Prop. KN Step 0: "(C1), (C2) only"; X1 KN^tr Step 0) | not used |
| weak-peak push, (T)-blocks (X1 KN^tr Step 0) | active weak peak k, one-sided DOWN by <= 2b theta Phi_k/m | far pull (V1 Lemma IP) | a pullable far j of k (x := 2b theta Phi/m), or (P3)/(P4) on k (lowering direction), or (P1) if zero-data |
| TU on active values (KN^tr Step 4) | Omega_act, nonzero data | (TU) | (P2), (P3) or (P4) |
| KN-1 holds (KN^tr Step 4, Q1-refb P-HOLD) | nearly neutral Omega carriers of (T)-blocks, zero data | (TU) pull at v >= max(corr, c_{L+1}) + bank | (P1) (near Z-con/Z-gen; or TU as at finite F), (P3) or (P4) |
| D2 pushes ((U)-blocks), (KN)-block lever pushes (U1-ref Prop. KN) | inactive, zero data | TU pulls / far z-moves | (P1), (P3) or (P4) |
| peak push per block (KN^tr Step 4; U1 Lemma 1.5) | buffer peak, data iff block active | bank at first far coordinate (+ z-moves/pulls) | (P2) (active block) / (P1) (inactive), or (P3)/(P4) on the peak; in ratio form it is an optional bordering column (2.4) |
| Lemma DC levers (X2 LV (a)-(c)) | all Omega carriers | (TU) / (Z-con) / (Z-gen) at j(l) | as the corresponding Step-A row; the DC bank/Z coordinate is a near coordinate NOT used by Step A (Step A uses <= 2 near coordinates per carrier: bank, and the lowered/pull coordinate is far) |
| block-norm lever (Q2 Cor 4.2 / Q2-refa C.3) | coarse peak of block m* | zero-data lever | (P6) via 2.2's repair |
| anchors (U2 TR-inf (c')) | -- | -- | (P5) |
| Step B (G1 release, static ownership) | fine carriers, far coarse parts | z on J_fine | DISPENSABLE (part 3, Lemma K1.S) |
| theta-masses W, W_F; truncation N_w (Q2 2.3) | -- | contacts off F_0 / raised support | unchanged (Q2 Theorem UE^inf, refereed) |
Coordinate bookkeeping (PROVED).  Distinct moves act on distinct coordinates: (C1)/(C2) on S^nat and T(L) \ F; Step A uses per carrier at
most one near coordinate (bank of (P2), or the two coordinates of (P3), or one of (P4)) and one far coordinate (pull or Z-lever); Lemma DC
uses a further near coordinate (six are available: <= 2 + 2 used) and far coordinates at the scale r << x_A, disjoint from Step A's (v-windows
of ratio 2^{6G(L)} contain >= 3 elements of S_l, Q1-refa P4).  Distinct carriers have disjoint signature sets; anchors are not in any
carrier's near set of Lambda by definition.  The lowered in-F coordinates are at most 2|Lambda| per system; their total lowered mass is
<= 2|Lambda| x_max = 2 T^2/(L Design(L)) = o(T^2) (x_max := T^2/(L Design(L) |Lambda|)).

## 2.4 The linearized systems; lever-regularity
SYS-A (Step A, RATIO FORM).  Q1's Step A sets active values to r''_l kappa and restores kappa by peak pushes.  Only RATIOS enter what route V
uses: the class cone in ratio variables (U1-ref 4.3: (X3)/kappa_m reads Delta'_m = sum_l r_l gamma_l), the statuses (X1 Lemma K: rho_d =
m|r_d| K(sigma, R^2)/Phi_d; sigma depends on the peak set, R^2 on the ratios of Omega), and the true shift (with exact ratios at f^#,
Delta''_m = sum r^#_l gamma_l = Delta'_m: U1 Lemma 4.6's correction term vanishes).  So we solve
   F_A(P, s) := ( val_l/kappa_{m(l)} - rt_l )_{l in Lambda_A} = 0,   rt_l := r''_l eps_l (l in Omega_act), 0 (l in H_T),
                 val_l(f_1)/kappa_{m(l)}(f_1) (l in Hold), the pushed ratio (l in D)      [ALL rows are ratio rows],
unknowns: one resource parameter P_k per k in Lambda_A := Omega(f_1) ∪ D, where Omega(f_1) := all coarse strict non-peaks of f_1 (the
route-V Omega), H_T := its nearly neutral inactive members in (T)-blocks (held at 0: KN-1, Q1-refb P-HOLD), D := D2/KN-pushed carriers
(target = current value moved inward by eta', resp. by U1-ref Prop. KN's s_0), Hold := the remaining inactive members of Omega(f_1) (target =
their value at f_1); and optional parameters s_c (one two-sided resource of a buffer peak c per block); kappa floats.  [Holding ALL coarse
strict non-peaks is free when every resource is private (their drift is then second order, X1-ref 8 "KN-1"), and NECESSARY as soon as a
common-mode resource (P4)/(P5) is used: a common mode moves every value at FIRST order (2.1(d), (e)), which would move the (U)-block statuses
(margin eta') and R^2 in Lemma K at first order.  With Lambda_A = Omega ∪ D every coarse non-peak RATIO is exact at f^(1a), so the floating
kappa moves no status (Lemma K: rho_d = m|r_d| K(sigma, R^2)/Phi_d, R^2 a function of the Omega ratios, sigma of the peak set); common modes
then move only coarse peaks (robust margins) and fine carriers.]
Linearization (PROVED from 2.1 and U1 Lemma 1.4: d kappa_m/d|zeta_c| = 1 - X_m at peaks, = rho_d M X/C for d in Omega_m, X_m <= C b^2 D^2):
   d val = (I - g h^T) dP (+ peak columns),   d kappa_m = -G_m h^T dP + (1 - X_m) lambda_c ds_c + O(X) dP,   G_m := (1 - X_m) sum_{peaks c of m}
   lambda_c vs_c eps_c g_c,
so, after multiplying the ratio rows by kappa,
   J_A = [ I - g~ h^T | col_c ],   g~ := g - (rt_l G_{m(l)})_l,   col_c := -(1 - X) lambda_c rt^{(m(c))} - h_c g~,
up to an O(X + Design^2 x) perturbation; rt^{(m)} := the target-ratio vector restricted to block m; h_k := 0 for private resources.
SYS-DC.  Q2 4.0: L(P, P_0, P_5) = N P - sum_{m* with (P6)} pi_{m*} p_{m*} P_{0,m*} - g~~ P_5 (anchors), N := D - gt h^T - sum_m p_m q_m^T.
DEFINITION (lever-regularity).  For a level L, a clean sub-window w and a class a, put
   rho_lev(w, a) := min over the two systems of  max over admissible resource assignments  of  1/||minimal right inverse of the linearization||_inf .
(LR_{w,a}): rho_lev(w, a) >= u(w)/Design(L)^{C_0} (C_0 absolute, fixed below).  f is LEVER-REGULAR (for the mate (g, rho)) if (LR_{w(L), a(L)})
holds for infinitely many main stages L, where w(L) is the clean sub-window and a(L) the class selected by Q1's pigeonhole at L.
[rho_lev is a semialgebraic function of the level-L data of f -- near moduli (R-mod), spreads, values and block data of the coarse carriers,
signs, and the combinatorial pattern -- evaluated with the resources available at w; its arguments move by <= C Design^C (mu*_J + eta' + K_w s_1)
between f, f^r, f_1 (Lemma DR-inf, Q1 CM^tr(f), Q2-refa C.7), so it is a rate object of level L up to the availability of far resources,
which is a combinatorial property of (F, a^r) at w.]

## 2.5 Lemma K1.5 (sufficient conditions for lever-regularity).  PROVED.
(a) If every carrier of Lambda_A and of Omega (Sys-DC) is privately tunable, then (LR_{w,a}) holds with C_0 an absolute constant: J_A =
    I + O(X + Design^2 x) (block triangular in the D-columns), and J_DC is X2's J = [[I - pq^T, 0],[X, I]] (no absorbers in route V: X = 0) with
    ||J^{-1}||_inf <= 1 + 4/A_min (Sherman-Morrison, q^T p <= C_m <= 1/2).
(b) If the set Lambda_4 of carriers using (P4) is nonempty and all others are privately tunable, then the square parts are I - g~ h^T (Sys-A)
    and N (Sys-DC), with h supported in Lambda_4, and:
    (b1) Sys-A is regular with constant Design^C/beta if beta := max{ |1 - h^T g~|, max_c |(1 - X) lambda_c h^T rt^{(m(c))} + h_c|, 1[anchor] } >= u,
         the max over the two-sided peak resources c; the right inverse is Q2 Proposition 4.1's with D = I (one bordering column suffices; an
         anchor column -g~ gives y^T(-g~) = -h^T g~ = -1 on the degenerate direction y = h);
    (b2) Sys-DC is regular with constant K of Q2 Proposition 4.1 if max(|c_alpha|, |beta_*|) >= u in some block with a two-sided block-norm
         lever (P6) [Q2 Prop. 4.1, Cor. 4.2 with 2.2's repair], or an anchor exists [column -g~~ with y^T g~~ = h^T D^{-1} gt != 0 on the
         degenerate direction].
(c) In particular f is lever-regular whenever, for infinitely many main stages L, every coarse carrier of level L that is tuned in the
    selected class has an off-F or thin near coordinate and (if it carries data) a pullable far coordinate at the scales x_A and r.  This
    contains Q2 Corollary 5.2 (F ∩ (union of S_l) finite, or F meeting no S_l (l <= L) in (s_max(L), s_far(w(L))]).
Proof.  (a) 2.1(a)-(c): each column is e_k + O(Design^2 x); the D-columns affect the ratio rows through kappa only (U1 Lemma 1.4) and the
D-rows have identity diagonal; Sys-DC is X2 Lemma DC (refereed).  (b) 2.1(d)-(e) give the columns; the square part of J_A is I - g~ h^T
(the peak-mediated kappa change of a (P4) column is -G_m h_k, which in the ratio rows adds +r''_l G_m h_k); det = 1 - h^T g~; when it is
small, the left null vector is h (h^T(I - g~ h^T) = (1 - h^T g~) h^T), and h^T col_c = -(1 - X)lambda_c h^T rt^{(m(c))} - h_c h^T g~ =
-(1-X)lambda_c h^T rt^{(m)} - h_c + O(|1 - h^T g~|); Q2 Proposition 4.1's proof (choose alpha or gamma by whichever scalar is >= beta_0) applies
verbatim with D = I, giving ||R|| <= C (1 + ||g~||)(1 + ||h||)(1 + max|col|)/beta.  All entries are design-bounded: |g_k| <= ||U||, |h_k| <=
Design(L)/nu (|a| <= 1, v >= 1/Design), lambda_c, |rt| <= Design^2.  (b2) is Q2 Prop. 4.1/Cor. 4.2 (refereed) with the repaired (P6).  (c) by (a).
QED

## 2.6 Lemma K1.6 (realization under lever-regularity).  PROVED.
Assume (LR_{w,a}).  Then:
(A) Step A at f^r (KN^tr with Sys-A in ratio form) produces f^(1a) with KN^tr's conclusions (a) (active ratios exactly r'' on Z_kappa, robust
    minors >= u/2), (b) ((T)-blocks: rho_d <= 1 - mu_kappa(eta'/3)/2 for active near-threshold d, held values exactly 0; (KN)-, (U)-blocks as
    there; robust statuses kept) and (c) p*(f^(1a) - f^r) <= C_f Design(L)^{C} eta' log(1/eta') + C_f T^2/(L Design(L)) = o(T^2).
(B) Lemma DC^inf at the pre-row: F has a zero (P*, P_0*) with |(P*, P_0*)| <= K_lev r, K_lev := Design(L)^{C_0}/u(w), every Omega carrier is a
    strict non-peak with nv = nv^0 exactly, peaks keep their status, and the lever masses satisfy ||X_lev|| <= C_2 r; the window conditions
    (W-b) and (LATE) hold with K_J replaced by K_lev (S2c^tr: K_lev is a design quantity, absorbed by s_late >= exp(-C log^2(1/T))).
Proof.  (A) X1-ref 8's proof, Step 4, with the joint fixed point replaced by the Poincare-Miranda argument of Q2 Corollary 4.2 for the map
G(y) := F_A(0) + y + Rem(R_b y) on the cube |y| <= rho_A, R_b the minimal right inverse (norm <= 1/rho_lev): G_l >= rho_A - |F_A(0)| -
C_2 ||R||^2 rho_A^2 >= 0 on the faces y_l = rho_A when ||R|| |F_A(0)| <= rho_A/2 and C_2 ||R|| rho_A <= 1/4.  Here |F_A(0)| <= C Design eta' (the
Lojasiewicz displacement |r'' - r_1| <= eta' times Design, plus the KN-1/D2 targets <= C b), so rho_A := 2||R|| C Design eta' <= Design^{C}
eta'/u, and the quadratic remainder constant C_2 <= Design^C/u^C (2.1: second-order cross effects O(Design^2 u^{-4})), so C_2 ||R|| rho_A <=
Design^C u^{-C} eta' <= 1/4 because eta' = T^4/(L Design(L)) and u(w) >= T_hi(w)^{1/20} >> T (Q(w) >= (4 Design/u)^{20}).  Resource sizes are <=
||R|| rho_A in value units, i.e. masses <= Design^C eta'/u, so all the cost and status estimates of X1-ref 8 hold with eta' replaced by
Design^C eta'/u -- still << b-independent margins: robust statuses move by Design^C eta'/u << u; the Puiseux protection uses only the EXACT
ratios and the exact held values (KN-1), not the size of the moves (Q1-refa F1, Q1-refb E7).  The lowering of in-F far coordinates costs
<= 2T^2/(L Design) (2.3).  (B) Q2 Corollary 4.2's proof with R from (LR): K|F(0)|_inf <= r/2 holds for r := 4K_lev(...) as in X2-ref (p-DC1);
remainder constants are design quantities by 2.1; (S-mass) range: |P| <= K_lev r keeps |A(p)| >= |A_1(p)|/2 (Q2-refa (p2.2), (LATE)).  QED

## 2.7 Lemma K1.7 (structure of the non-lever-regular configurations).  PROVED.
If (LR_{w,a}) fails, then in at least one of the two systems the set Lambda_np of carriers that are NOT privately tunable is nonempty, and:
 (i) every l in Lambda_np is (U) UNPULLED -- nonzero-data, N_l ∩ F_thick = {} and no pullable far coordinate at the scale x -- or (S)
     SUPPORT-SWALLOWED -- N_l ⊂ F_thick with all pairwise spreads tiny;
 (ii) if Lambda_np consists of (S)-carriers only, then no anchor exists (P5), and the bordered scalars of 2.5(b) are tiny:
     |1 - h^T g~| <= u and |(1 - X)lambda_c h^T rt^{(m(c))} + h_c| <= u for every two-sided peak resource c (Sys-A), resp. |c_alpha|, |beta_*| <= u
     in every block with a two-sided block-norm lever (Sys-DC);
 (iii) EXACT LIMIT.  If (ii) holds with all tiny quantities exactly 0 for a fixed set of (S)-carriers and h^T D^{-1} p_m = 0 in every block, then
     u_h := sum_{l} h_l eps_l u_l satisfies P_F (I - e e^T) U^* u_h = 0, hence (Q2 Lemma 4.3) u_h|_F = kappa a|_F, and if kappa != 0, then
     (U2 Lemma ND) F minus the targets of these carriers lies in their signature sets with a_s = (c_l/kappa) v_l(s) there.
Proof.  (i) A carrier without (P1)-(P3): by the clean dichotomy N_l ⊂ (off F) ∪ F_thin ∪ F_thick.  If N_l meets F_thick and has no robust-spread
pair it has (P4) only (S), unless it has an off-F/thin near coordinate, in which case, being not privately tunable, it is nonzero-data
without a pullable far coordinate; if moreover N_l ∩ F_thick != {} it has (P4) and belongs to the (P4)-set of 2.5(b) -- such carriers do not
by themselves break (LR) (2.5(b) applies) -- otherwise it is (U).  A zero-data carrier with an off-F/thin near coordinate has (P1).  (ii) If only (S)-carriers lack private resources, 2.5(b) shows that (LR) can fail only if all the
listed scalars are <= u (with u = b(w^-) the next band: at a clean w they are tiny) and no anchor exists.  (iii) The left null vector of the
square part is y = h (Sys-A) resp. D^{-T}h (Sys-DC, Q2 4.4(ii)); a support move at s in F changes y^T(values) by (mu_s^2 A(s)/nu)[u_h(s) -
<U^* u_h, e> a_s/nu] (2.1(d)); its vanishing for all s in F is P_F(I - e e^T)U^* u_h = 0; Q2 Lemma 4.3 and U2 Lemma ND (both refereed).  QED
Remarks.  (1) The (U)-case is new (finite F never sees it): a data-carrying carrier whose deep signature set is support of the opposite sign
(or super-thick, |a^r_j| > x_max at every pullable depth) has only a ONE-sided private lever (its bank: eps_l val_l can only go up).
RATIO TRICK (SKETCH).  In ratio form, if block m has a two-sided buffer-peak resource and all (U)-carriers of m have target ratios rt_l of one
common sign, a correction delta of the ratios is realized with one-sided banks: if rt_l > 0 for all (U)-carriers of m, raise kappa_m by
dkappa := kappa max(0, max_U(-delta_l/rt_l)) and set the bank moves du_l := kappa delta_l + rt_l dkappa >= 0 (other carriers two-sided); if all
rt_l < 0, lower kappa_m symmetrically.  The nonlinear version needs a Brouwer argument on a cone-shaped parameter domain (not written).  Mixed
signs of the (U)-ratios inside one block are not covered.  (2) (S)-configurations at all large levels are (NDN)-type (U2 3.3, U2-ref G3) and contain Q2's (NDN2); their
exact versions have the Lemma ND structure (iii).  Both are handed over to K2 (O-c).

# 3. Step B at infinite F (it is dispensable), status stability (V1 Lemma ST) under the new side effects

Setting of parts 1-2.  f^(1a) := the row produced by Step A (Lemma K1.6(A)) at the deep-raised row f^r.  E_c(w) := T(L) ∪ union_{l <= L}
(S_l ∩ [1, s_far(w)]) minus F^(1a) (U1 2.1), s_far(w) the least s with 2^{-s} <= c_{L+1}^2; J_fine := N \ (F^(1a) ∪ E_c(w)).

## 3.1 Lemma K1.S (route V needs no Step B).  PROVED.
Put f^# := f^(1a) (no G1 release, no static-ownership recursion: z is not changed on J_fine).  For t in S let the data be those of part 1.5 on
F and of Q1 CM^tr(c) on E_c, and on J_fine put b^+(j) := chi_j V(j), b^-(j) := -(1 - chi_j) V(j) with chi_j := 1/2 at free coordinates of f^#
and chi_j in [0,1] given by lem:split at contacts (as in V1 TR Step 4).  Then:
 (a) ||V 1_{J_fine}||_1 <= C_f D(L) 2^{-s_far(w)} + C_Delta sum_{k > L} lambda_k <= C_f Design(L) c_{L+1};
 (b) the violation mass on J_fine is <= ||V 1_{J_fine}||_1, and b^theta = 0 at every violated free coordinate ((H3) of U3 Lemma VT);
 (c) (U5') every COARSE carrier of every block of f^# is a peak with relative margin >= u/2 or a strict non-peak with gap^# >= g_min(w);
 (d) Theorem UE^inf (Q2 2.4, with the precisions of Q2-refa B.2 and P3 of Q1-refa) holds with its hypothesis (U5) replaced by (U5').
Consequently Q1's Step B, and with it the question of the ownership recursion on J_fine \ F, can be omitted at finite AND at infinite F.
Proof.  (a) A coordinate j of J_fine lies in no coarse target (T(L) ⊂ E_c ∪ F^#) and in no near part S_l ∩ [1, s_far] of a coarse signature
set, so coarse carriers contribute to V(j) only through S_l ∩ (s_far, infinity): sum_{l <= L} |c_l| ||v_l 1_{(s_far, inf)}||_1 <= C_f D(L)
sum_l lambda_l (delta_l/n_l) 2^{1 - s_far} <= C_f D(L) c_{L+1}^2 (|c_l| <= C_f D(L) lambda_l, part 1.4).  Fine carriers have forced coefficients
|c_k| <= C_Delta lambda_k (U1 Lemma 1.1(a), Lemma 2.1) and ||u_k||_1 <= q*(u_k) = 1: total <= C_Delta sum_{k > L} lambda_k <= C c_{L+1}.
(b) At a free j: |b^+| + |b^-| = |V(j)|, b^theta = (b^+ + b^-)/2 = 0.  At a contact j: (z_j b^+)_- + (z_j b^-)_+ = chi (z_j V)_- + (1 - chi)(z_j V)_-
= (z_j V(j))_- <= |V(j)|.  Off F^# ∪ J_fine (i.e. on E_c) the data and their violations are Q1's (CM^tr(d)).
(c) Lemma K1.6(A) (KN^tr's (b) at f^(1a)): every coarse carrier is a peak of relative margin >= u/2 or a strict non-peak with gap >= c_f eta' M
((KN)-, (U)-blocks), >= M mu_kappa(eta'/3)/2 ((T)-blocks, active near-threshold), = M (held at 0) or robust; all >= g_min(w) (Q1 CM^tr(b)).
Without Step B there is no later drift.
(d) (U5) enters Theorem UE (X2 3.5, Q2 2.4 (M5)) only through Lemma UE-1(e): the scrambled set A_m of lem:anchor for (w^0_m, w'_m), split as in
the proof of lem:scrambling into A^(1) := {k in A_m : t_k <= Pi} and A^(2).  By (c) and Lemma UE-1(b), (c) (values and thresholds move by <=
K_w Pi), a coarse carrier with t_k <= Pi is in S_1 or S_2 of lem:anchor as soon as 2 K_* Pi <= x_0(w) := c_f g_min(w) Phi_min(L) (margins
u theta Phi/(2m) >= x_0, Phi gap >= Phi_min g_min >= x_0, gap >= g_min >= x_0); so A^(1) contains fine carriers only, whose total contribution
to S_m is <= sum_{k > L} (Phi_k^2 + lambda_k(|w' - w^0| + (C' - C)_+)) <= 4m sum_{k > L} Phi_k <= 4m C c_{L+1}; A^(2) is handled by X2 3.2(iv)
verbatim (Phi-mass <= s_1^2 T^4).  Hence
      S_m <= K_w Pi^2 log(e/Pi) + 4m (C c_{L+1} + s_1^2 T^4),
and the requirement of X2's Step 3, Bx_m + S_m <= c_late delta s_1, holds because (W_exp) and Lemma S2c^tr give c_{L+1} <= exp(-1/T) and
s_1 >= exp(-1/(2T)), so 4m C c_{L+1} <= c_late delta s_1/4 for T small; the other terms are X2's.  The violations of (a), (b) are of the
type already counted in eps^viol (Q1 CM^tr(d): eps^viol <= C_f Design c_{L+1} + C_f c_{L+1}^2/T), so (VT') and (LATE) are unchanged.  QED
Remarks.  (1) What Step B was for.  In route X (exact data, U1) every coordinate must be EXACTLY admissible; the static-ownership recursion,
self-alignment of negative fine carriers and the G1 release were needed there, and X2/Q1 inherited them.  In route V every fine-origin
misfit is a tolerated violation of mass O(Design c_{L+1}), and (W_exp) makes c_{L+1} negligible against s_1 -- including in the scrambling
term, which is the only place where the self-aligned (R)-peaks of X2 Lemma CM(a) were used.  (2) At infinite F, Step B would have needed
the signature sets S_k of fine carriers to avoid F (S_k ∩ F is not assignable and |u_k(zhat^#)| >= ||v_k 1_{S_k \ F}||_1 may be small); Lemma K1.S
removes this question.  (3) The theorem does NOT say that fine carriers are harmless in general: only their total weight c_{L+1} is used,
against s_1 >= exp(-1/(2T)); this is where (W_exp) is essential.

## 3.2 Lemma K1.ST (statuses at f^# and along the engineered approximant; new side effects).  PROVED.
At f^# = f^(1a) and at the d-consistent engineered approximant f' of Theorem UE^inf built at f^#:
 (a) every coarse strict non-peak of f^r has its RATIO exactly at its Sys-A target (Lemma K1.6(A)); every coarse peak keeps its sign and a
     relative margin >= u/2; every near-threshold active carrier d of a (T)-block has rho^#_d <= 1 - mu_kappa(eta'/3)/2 and rho'_d <= 1 -
     mu_kappa(eta'/3)/8; robust objects of level L move by <= Design^C eta'/u + C mu*_J + Design^C r/u << u between f and f';
 (b) the new side effects -- deep raise (part 1.2), lowering of far in-F coordinates (part 2.3), common modes of (P4)/(P5) and of the
     repaired block-norm levers (P6) -- change no status used by route V.
Proof.  (a) Lemma K1.6(A): Sys-A fixes all coarse non-peak ratios exactly, so by X1 Lemma K (rho_d = m|r_d| K(sigma, R^2)/Phi_d; R^2 a function
of the Omega ratios; sigma = sigma_rob + O(c_{L+1}^2) because the coarse peak set is P_rob: robust peaks move by << u, weak peaks were pushed in
Step 0) the (T)-block statuses are those of X1-ref 8 with the SAME Puiseux margin; the (U)- and (KN)-block statuses depend on the exact ratios
and on robust peaks only; robust objects move by the resource sizes (Lemma K1.6(A): <= Design^C eta'/u in value units) times design Lipschitz
constants.  At f': Lemma PM (Q1 2.4) verbatim -- its proof uses (i) nv' = nv^# on Omega (Lemma DC^inf under (LR), K1.6(B)), (ii) coarse
peaks clamped at both rows (margins >= u/2 >> the value moves K_lev r + common modes Design^C r), (iii) fine terms bounded by C sum_fine Phi^2.
None of these uses the privacy of the levers: the common modes of (P4)/(P5) move only coarse peaks and fine carriers once all Omega
normalized values are exact.  (b) Deep raise: values move by <= C mu*_J <= b^2 Phi_min/Design (part 1.2 choice of J), inside the clean
classification (U2 Lemma DR-inf).  Lowering a far coordinate j in F does not change z (a lowered support coordinate becomes a contact of the
same sign s_j) and moves e by <= 2 mu*_j x_max/nu (V1 Lemma B(iii)), hence every value by <= C mu*_j x_max << b; the subsequent pull/z-move is
the resource's own move.  Common modes: by (a), every coarse non-peak value is re-tuned exactly inside the same fixed point (Sys-A) or
Poincare-Miranda solution (Sys-DC), so only peaks (robust) and fine carriers (total weight c_{L+1}) feel them.  QED
Remark (V1 Lemma ST and Lemma NS).  V1's status table concerned the donor raise (C3) and the drift Lam = T^3; route V does not use (C3)
(part 2.3), and the closing moves (C1), (C2) act off F exactly as at finite F.  So V1 Lemma ST is replaced by (a) above; V1 Lemma NS
(no slaving) holds because every exactified object is a function of the exact ratios (Sys-A) and of the closed rooms ((C1), (C2), off F).

# 4. Theorem 5.1 (transport of Master Theorem VI to arbitrary base support) and the precise non-lever-regular class

## 4.1 THEOREM 5.1 (transport).  PROVED modulo the cited refereed results and the design bookkeeping (D-K1) below.
DESIGN (D-K1).  T_fin^* (option (a)): T_fin of Q1 over the base mu*_s = 2^{-2^{2^s}} with Design(L) >= 2^{d(L)}/(delta_min(L) mu*_{d(L)}^2),
d(L) := sigma(L) + 6 * 2^{L+1}, Q(w) := (4 Design(L)/u(w))^{omega(L) + L^2 + 20} (Q1-refa P8), and with the following objects of level L added
to the rate scheme omega(L) (each a semialgebraic function of finitely many data of f, the count a design number, N-free):
 (R-mod) |a_s| for s in [1, d(L)];  (R-pat) minors and cofactor polynomials of the class cones with the contact rows (X1^F) of part 1.3, for
 all enlarged patterns and classes of level L;  (R-lev) the spreads |1 - rho_s/rho_{s'}| of near coordinates and the bordered scalars of
 Lemma K1.5(b) (1 - h^T g~, (1 - X) lambda_c h^T rt^{(m)} + h_c, c_alpha, beta_*) for all lever assignments of level L.
[Inserting objects only enlarges omega(L), Design(L) and Q(w); by U4 Lemma GW every window condition is monotone under these changes.  The
full bookkeeping (well-foundedness, N-independence) is item (O-d) of ADDENDUM 10 (task K2).]
STATEMENT.  Let N >= 1, f in S_{p_N*} with base support F (finite or infinite), g in C(f), rho in (0,1).  Suppose f is LEVER-REGULAR for
(g, rho): for infinitely many main stages L, at the clean sub-window w(L) of L and the class a(L) selected by the class pigeonhole of part 1.3
(Lemma-P thresholds, no cube), (LR_{w(L), a(L)}) of part 2.4 holds.  Then (f, rho g) lies in the closure of NA((c_0, p_N), l_2^2), along
norm-attaining rows f'_L with FINITE base support; in particular (LSC-trunc)_N holds at (f, g, rho).  If f is lever-regular for every
(g, rho), then f is in Rec(p_N).
PROOF.  Fix N, f, g, rho and l_f = l_f(f, N, g, rho) (Q1 3.1, with Lemma M2^inf of Q2 replacing Lemma M2).  For each main stage L >= l_f of the
hypothesis, with w := w(L), T := T_lo(w):
 Step 1 (clean sub-window).  Q1 Theorem VI Step 1 with the enlarged rate scheme (D-K1): the omega(L) + 1 sub-windows have disjoint bands, so
   some w is clean for f (V1 Theorem 2', U4 Lemma GW, Q1-refb 1.1(d)).
 Step 2 (deep raise).  f -> f^r beyond J(w) (part 1.2): hypothesis (a) of Theorem E^{eng,RT,inf} at f^r with eps'_r <= theta_w T^2; the clean
   classification survives with factor 2 (U2 Lemma DR-inf); budget lemmas at f^r for g^r on the window (V3 (I1)).
 Step 3 (classes).  Two-sided decompositions of g^r at f^r at every dyadic scale of the window; class pigeonhole with thresholds A_i =
   K_*(w)^i (part 1.3): a class a = a(L) with a set S of >= n(w)/D_cl(w) scales (Lemma K1.1: no cube).  Lemma K1.2 holds on S.
 Step 4 (Step A).  Under (LR_{w,a}), Lemma K1.6(A): the companion f^# := f^(1a) with KN^tr's conclusions (exact ratios on Z_kappa, threshold
   protection with the Puiseux margin, robust statuses), p*(f^# - f^r) <= C_f Design^C eta' log(1/eta')/u + 2T^2/(L Design(L)) <= theta'_w T^2,
   theta'_w -> 0.  No Step B (Lemma K1.S).
 Step 5 (data).  Proposition K1.A: for t in S the route-V data with the deep assignment on F form a window family at f_0 := f^# with (U1), (U2),
   (U3^inf) (C_+ = 5, up to support violations of mass <= C_f Design c_{L+1} + C_f c_{L+1}^2/T), (U4), (U5') (Lemma K1.S(c)), (U6) (levers of part
   2 under (LR), Lemma K1.6(B)), (U7); p*(g - g_t) <= K_data t.
 Step 6 (engineered approximant).  Theorem UE^inf at f_0 with: (U5') in place of (U5) (Lemma K1.S(d)); support violations counted in eps (Q1-refa
   P3: at a support coordinate the base excess of a'_j + x_j is <= 2(z_j x_j)_-; the W_F raises of Q2 2.3(ii^inf) protect the theta piece on F);
   Lemma DC^inf from Lemma K1.6(B) (constant K_lev = Design^{C_0}/u in place of K_J; masses at S-mass levers keep |A(p)| >= |A_1(p)|/2 by
   (LATE), Q2-refa (p2.2)); N_w chosen after s_1 and beyond every lever coordinate (Q2 2.3(i^inf), Q2-refa B.2); s_1 := max(64 rho eps^viol/delta,
   exp(-1/(2T))) (Lemma S2c^tr: K_w <= exp(C log^2(1/T)) since every new constant -- K_lev, K_*(w) <= (Design/u)^C (log n(w))^{1/2}, C_+ = 5 --
   is at most a design power times a power of log(1/T)).  The approximant f'_L is norm attaining with finite base support (Q2 2.3), and
   p*(f'_L + tau g'_i) <= 1 + (tau^2/2)(1 - delta) for 0 < |tau| <= c_flat t_i (every piece i), p*(g'_i - rho g_i) <= K_w(K_w s_1 + c_fine + tail_W)/t_i.
   Statuses along f'_L: Lemma K1.ST (Lemma PM verbatim).
 Step 7 (averaging).  Theorem E^{eng,RT,inf} with base rows f_j := f^#(L_j), lambda_j := lambda_r(L_j), eps'_j := eps'_r + p*(f^# - f^r) <=
   (theta_w + theta'_w) T^2; (E-c) with K_j := K_data(w); (E-d), (E-e') by Corollary K1.B (|S| c_flat/K_data -> infinity, K_data T_hi/|S| -> 0,
   c_flat(w) >= c_f u(w) because C_+ = 5 is absolute, Q2-refa B.1); (E-f) by Lemma S2c^tr and (W_exp) (p-E1: K_w c_fine <= K_j T^2 4^{-n}).
   Subset averaging over S: U1 Lemma 2.4 (only the count |S| and "sum over I_r of dyadic t < 2|r|/c_flat" are used).  Conclusion: (f, rho g) in
   cl NA along the norm-attaining f'_{L_j}, which have finite base support.  QED
REMARK (what is new relative to Q2's SKETCH).  (i) Q2 Proposition 3.2 is PROVED in a corrected form (part 1): the cube normalization must be
dropped (Remark K1.1'), and is not needed (Lemma K1.1); C_+ = 5 instead of C Design/u.  (ii) Step B is dispensable (Lemma K1.S), so Q2's item
"Step B's static-ownership recursion on J_fine \ F" disappears.  (iii) The levers are audited (part 2.3); Q2-refa C.3's bank-with-offset
block-norm lever is one-sided along the degenerate direction (part 2.2, numerics) and is replaced by TU on the peak.  (iv) Lever-regularity is
defined as a modulus condition (2.4); it holds automatically when every tuned carrier is privately tunable (K1.5(a)), and otherwise reduces
to explicit bordered scalars (K1.5(b)).

## 4.2 COROLLARY K1.C (explicit lever-regular rows).  PROVED.
f is lever-regular for every (g, rho) -- hence f in Rec(p_N) -- in each of the following cases:
 (a) for infinitely many main stages L, every coarse carrier l <= L has, among the first six elements of S_l beyond s_max(L), a coordinate
     off F or with |a_s| <= b(w(L)), and (if l carries data in some class) a pullable far coordinate at the scales x_A, r of part 2;
 (b) [Q2 Corollary 5.2] F meets no S_l (l <= L) in (s_max(L), infinity) for infinitely many L -- e.g. F ∩ (union_l S_l) finite;
 (c) for infinitely many L, every coarse carrier l <= L whose first six coordinates beyond s_max(L) are all in F has two of them with spread
     |1 - rho_s/rho_{s'}| >= u(w(L)) (rho := a/v_l), and every data-carrying carrier with an off-F near coordinate has a pullable far coordinate;
 (d) any combination of (a)-(c) carrier by carrier, provided the carriers left with (P4) only satisfy the bordered condition of Lemma K1.5(b) or
     an anchor (P5) exists.
Proof.  (a), (c), (d): Lemma K1.5 (a), (b); (b) is a special case of (a) (all near and far coordinates off F; pulls at contacts of sign
eps_l closed by (C1), for support-swallowed-free carriers).  QED
Examples.  (1) If |a_s| decays polynomially on each S_l (e.g. |a_s| ~ s^{-2}), consecutive near ratios satisfy rho_{s'}/rho_s =
2^{s'-s}(s/s')^2 >= 2^{2^{l+1}-1}: robust spread, case (c) for the support-swallowed carriers.  (2) If, for every l, F ∩ S_l contains no
three consecutive elements of S_l beyond some point, then case (a) holds at every large L: the six near coordinates contain an off-F one, and
every v-window [x, x_max] (ratio >= 2^{6G(L)}) contains an off-F element of S_l, which is a contact of sign eps_l after (C1) (pullable).

## 4.3 The precise class of NON-lever-regular rows.  PROVED (as a characterization).
f is not lever-regular for (g, rho) iff for all but finitely many main stages L, at w(L) and a(L), Lemma K1.7 holds: in Sys-A or Sys-DC a
nonempty set Lambda_np(L) of tuned coarse carriers is not privately tunable, each of type
 (U) UNPULLED: carries data, no thick near coordinate, and every coordinate of S_l with x <= v_l(j) <= x_max (x = x_A or r) lies in F with
     s_j = -eps_l or |a^r_j| > x_max (deep support of the opposite sign, or super-thick at depth), or
 (S) SUPPORT-SWALLOWED: the six near coordinates are thick (|a_s| >= u) with pairwise spreads <= b (a_s ≈ c_l v_l(s) on them);
and, when Lambda_np consists of (S)-carriers only: no anchor (every thick coordinate of F ∩ [1, d(L)] lies in the support of a tuned carrier)
and all bordered scalars of Lemma K1.5(b) are <= b(w).  Exact limit (Lemma K1.7(iii)): the configuration of Q2 Lemma 4.3 / U2 Lemma ND.
This class is the infinite-F counterpart of U2's (NDN) (corrected by U2-ref G3 to a regularity modulus) and contains Q2's (NDN2) and Q2 4.4(iv)
("KN-1 holds in a degenerate raw direction").  It is item (O-c) (task K2); the sub-case (U) is new.
WHY THE CLASS IS SMALL (HEURISTIC, not used).  (S) requires a near-proportional profile a ≈ c_l v_l on six consecutive elements of S_l at
infinitely many levels together with exact cancellations of design-free scalars; (U) requires the deep part of S_l to be support of the sign
opposite to l's switching at every window.  Neither is excluded by anything proved here; no mate of such a row is shown to be non-recoverable.

# 5. Corrections and precisions to earlier rounds (recorded)
 (C1) Q2 Proposition 3.2 (SKETCH) claimed compatibility of the zero-switching faces with "Q1's class/cube pigeonhole (they are sub-patterns, so V2's
      minors cover them)".  Correct for the CLASS part (Lemma K1.2-K1.3, with thresholds enlarged by the Lemma-P constant, which depends on the
      window through 2^{J(w)}); NOT established, and HEURISTICALLY false, for the CUBE part (Remark K1.1').  Repair: drop the cube (Lemma K1.1).
      The constant is C_+ = 5, not C Design/u.
 (C2) Q2-refa C.3 ("bank with offset" block-norm lever is two-sided): FALSE (2.2).  The offset moves the base point along the lever column, so
      the degenerate direction forces the total lever position; with the base mass in the pre-row, |F(0)|_inf >= 2Kr|pi p_{m*}| - |F_orig(0)|
      violates Corollary 4.2's hypothesis K|F(0)| <= r/2 when 4K|pi p_{m*}| > 1.  Repair: TU on the peak (pull + bank), or (P3)/(P4) on the peak.
 (C3) Q1 Lemma CM^tr STEP B, X2 Lemma CM(a) (self-aligned negative fine carriers) and the G1 release: redundant in route V once (W_exp) holds
      (Lemma K1.S).  Q1 CM^tr(e) and Prop. BR's (U5) may be replaced by (U5') (coarse carriers only).  X2's (U5) hypothesis of Theorem UE is
      likewise only needed for coarse carriers when c_{L+1} << s_1.
 (C4) Q1-refa P2 ("order class -> Step A -> cube -> Step B") is moot for route V (no cube, no Step B): order class -> Step A -> data.
 (C5) U2 3.1(iv)/TR-inf's description of TU levers at infinite F needs pulls only for DATA-CARRYING carriers; zero-data carriers need one near
      off-F/thin coordinate (Z-con/Z-gen).  Far z-moves and offset banks are one-sided (2.0, 2.2).
 (C6) Q1/X1 KN^tr Step 4 restores kappa by peak pushes; only ratios are used downstream (cone in ratio form, Lemma K, true shift), so kappa may
      float, and the peak resources become optional BORDERING columns (2.4).  With common-mode resources the ratios of ALL coarse strict non-peaks
      must be tuned (first-order drift otherwise).

# 6. Numerics (sanity checks only; r11/K1_work/)
 offset_check.py -> offset_check.out: 2000 random exactly degenerate bordered systems N = I - g h^T - p q^T with a block-norm column -pi p and a
   bank offset m_0: the bordered solve has residual <= 1.2e-14; the total lever position (offset + adjustment) equals y^T F(0)/(pi y^T p) in every
   trial, independently of the offset; it is negative (infeasible for a bank) in 48.7% of the trials.  Supports (C2).
 deep_assign_check.py -> deep_assign_check.out: 4e5 random instances of the deep assignment with trace slack (part 1.5 (i)): the three claims
   |B_+ - b^+_1| <= f^+ + f^- + |Delta B - X|, s b^+_1 >= -A, s(b^+_1 - X) <= A + tr hold, maximal normalized violations -3.3e-10, 9.8e-17, 2.5e-16
   (rounding).  Supports Proposition K1.A (i).
 Finite models cannot exhibit the infinite-dimensional phenomena (deep raises, Lemma P, windows); the structural claims rest on the proofs.

# 7. What remains open (precise), and the interface with K2
 (1) The NON-LEVER-REGULAR rows (4.3): at all large main stages, at the clean sub-window and the selected class, the bordered lever systems are
     degenerate; every non-privately-tunable carrier is (U) or (S).  The (S)-part is Q2's (NDN2)/4.4(iv) (exact limit: Q2 Lemma 4.3 / U2 Lemma ND,
     a|_F proportional to a combination of signature vectors) -- item (O-c), task K2 (data-side bordering (R3-a), tolerance variant of UE^inf,
     or the cushion route).  The (U)-part is new: one-sided private levers; the ratio trick (2.7 Remark (1)) covers blocks whose (U)-ratios have
     one sign (SKETCH).
 (2) Design bookkeeping (D-K1) of the new rate objects (R-mod), (R-pat), (R-lev) -- a monotone enlargement (U4 Lemma GW), item (O-d) (K2).
 (3) Inherited: the once-refereed links of Q1's chain (U1-ref MT IV' tools, X1-ref KN^tr, X2-ref CM'/C_mix') and of Q2 (UE^inf, E^{eng,RT,inf}).
 (LSC-trunc) for every f, density of NA((c_0, p_N), l_2^2) (every N) and of NA((c_0, p), l_2^2): OPEN.  Combined with Q1 Theorem VI.2, Theorem 5.1
 gives: NA((c_0, p_N), l_2^2) is dense as soon as every (f, g, rho) with infinite base support is lever-regular or is recovered by K2's results
 in the non-lever-regular class.
