# U4-ref part 4 — Master Theorem (i)-(iv) and status flags

## 4.1 Master Theorem (i) [F finite]: CORRECT
- First sentence = V2-ref 4b(ii) (Master Theorem III') for T_final; its hypotheses hold by parts 1-3.
- "Equivalently f notin Rec_N implies (C*)": the negation of "infinitely many levels have SOME clean w with (SH_w) or rho^sh >= u" is
  "for all but finitely many levels EVERY clean w has not (SH_w) and rho^sh < u".  rho^sh(kappa^sh, f) and c_pi(f) are rate objects of
  level l (V2-ref P3; V1 (R6)), so at a clean w they avoid (b(w), u(w)): rho^sh < u gives rho^sh <= b; not (SH_w) gives I_up ∪ I_lo != {}
  and c_pi < u, hence c_pi <= b.  Both directions hold, so "equivalently" is right.
- Block-tame rows: cor:BTrecovered (any admissible T, I finite).  R_0, R_0^±, R_S: thm:R0, thm:Bpm, thm:S (SLD; via Lemma GW).
- Constant-sign maximal contact (z = eps_0 off F): Z4 Lemma 5.0 gives, in every block, non-degenerate coarse peaks with w = +M and
  w = -M and margins >= q_0/4; with constant swallowing sign their types are opposite, so they are sources (U2), (L2) at every clean w of
  large level (relative margin is an f-constant, >= u(w) eventually): I_up ∪ I_lo = {}, (SH_w) holds (V1 M-II.3); V2-ref 5(i) gives also
  rho^sh >= 1.  So such rows never satisfy (C*) and lie in Rec_N for every N.  (Sign-MIXED full contact is NOT covered: V2-ref P5.)
- Residual at F finite: (C*) minus ((BT) ∪ R_0 ∪ R_0^± ∪ R_S).  U4 states "(C*) and not block-tame"; adding R_0, R_0^±, R_S is cosmetic.

## 4.2 Master Theorem (ii) [F infinite]: CORRECT
RS' (part 3), R1 (Z5-ref; hypotheses (W*), (H2), (H3-inf), (B_fin), (CS_B) as in Y3 3.4), Y3 Theorem 3.5 (D_sigma), Y3 Theorem 5.1
(any admissible T), Z5 T6/T7 (refereed correct, T7 with Z5-ref's fix): all hold for T_final (Lemma GW for the window-based ones).
Per-mate results (V3 Theorem A, Y3 Theorems 2.1/6.1, (LSC-trunc)) are correctly marked as not row classes.

## 4.3 Master Theorem (iii) [residual list]: CORRECT as a logical statement; one gloss is HEURISTIC
(E1)/(E2)/(E4)/(E5) are exactly the negations of the six RS' hypotheses ((RR); (B_fin); (ND') or (H3-inf); (W*) or (H2)), so "at least
one fails" is a tautology given (ii) — correct.  The parenthetical "(E1) mu-thin supports: |a_s| below a power of mu_s on infinitely many
active coordinates" is a HEURISTIC gloss: (RR) fails iff for every eps > 0, sum{mu_s U(s) : |a_s| < y U(s)} != O(y^{1+eps}); since mu_s
is super-exponentially small this forces infinitely many active s with mu_s U(s) >~ y^{1+eps}/(their number) while |a_s| < y U(s),
i.e. roughly |a_s| <~ mu_s^{1-o(1)} U(s); the gloss should say "roughly below mu_s U(s)" (power close to 1), not "a power of mu_s".
(E3) is correctly described as an obstacle to the per-mate Theorem A only.

## 4.4 Master Theorem (iv) [density; martintail]: CORRECT
lem:martintail needs ONE admissible T (and U) for all N; T_final, U_final are N-free (Lemma W(c)).  thm:reductionZ holds for T_final
(thm:R0 via Lemma GW; lem:R0(a) any T).  Conditional form: if for infinitely many N every residual row is in Rec_N, then (with (i),
(ii)) Rec_N = S_{p_N^*}, so every (f, rho g) is in cl NA (C(f) is convex and symmetric, rho g in C(f)), density for p_N
(prop:reduction), hence density for p (lem:martintail).  No row-wise statement transfers to p: correct (V3-ref F7).

## 4.5 Status flags: CORRECT, with precision (q6)
- No SKETCH on the critical paths of (i), (ii): confirmed (MT III' = V1 MT II (refereed) + V2 Theorems B, C1 (refereed) + V2-ref P2, P3,
  P7 (single referee); RS' (inspection standard), R1, Y3 3.5, 5.1, Z5 T6/T7 (refereed)).  The SKETCH items (V2 Theorem C6, V3 M_inf
  transport, ...) appear only in residual descriptions.
- (q6) "If only double-refereed statements are wanted, RS can be stated with (H3') in place of (H3-inf)": the (ND') fix of the
  non-degeneracy condition is ITSELF a single-referee item (V3-ref Section 2).  The purely double-refereed statement is V3's original
  Theorem RS with V3's (ND_B) (Lambda : l_1(F) -> R^B onto; it implies (ND'_B), and V3-ref confirmed V3's proof under it), (RR_{U_B}) and
  (H3').  (ND') and L_0 = B_np are single-referee strengthenings.
