# Referee report on P2 (Round 15, positive track): "the common core pursued positively"

Referee: adversarial referee for task P2 (second, independent pass; an earlier unfinished pass is archived in
r15/P2_ref_prev/ and was used only as a cross-check).  Full proofs of every fix: r15/P2_ref_notes.md.  Scripts:
r15/P2_ref_work/.  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1. Overall assessment
P2 claims neither density nor non-density.  It is a structural contribution on three items: (2) the (R-S1)-with-escape
residual, (1) Problem R, (3) finite merging.  Almost every claim labelled PROVED is correct; the exceptions are one
overreach (Consequence 2.8(iii), NOT PROVED as stated), one overstatement (last sentence of Prop 3.2), one incompletely
justified smallness condition (Cor 2.5(iii), Prop 2.6'), and one hidden design modification ((D-sep) is violated by
T_fin^{K2} as it stands).  All but the overreach are repaired below.  The joint conclusion of ADDENDUM NEG is unchanged:
nothing in P2 constructs a counterexample or proves density; the open core loses only one piece -- persistent single-minor
(R-S1) at consecutive (R1) main stages is excluded (in G1's restricted model) for the (D-sep)-modified design.

## 2. Verdicts, claim by claim

### Part 2 ((R-S1) with escape)
- Theorem 2.3(A) / Lemma 2.7 (common-mode identity).  CORRECT (exact algebra).  It is Lemma III-identity (Part III eq.
  (III-identity)) with D = s_max(L) plus the support facts u_l = y_l + v_l, supp y_l in T(L), disjoint S_l, which I confirmed
  in Part III (lines 5462-5482) and Part II (h_l, delta_l in [delta^max_l/2, delta^max_l], n_l in [3/4, 5/4]).  One-line form:
  V(zhat) = kappa_V nu + sum_J V(s) z_s + sum_G C~'_l pi_l.  "Summed over a group the Hilbert terms equal the common mode" is
  exact in SIGNED form, sum_G gamma_k <U^*u_k, e> = kappa_{V^G} nu; R-ESC's h_k are absolute values that only bound it.
  Numerics: error 4e-15 (3000 random models).
- Theorem 2.3(B).  CORRECT (mod chain, G1's restricted model).  Every s in J is TS, data-carrying S_th or FR at the prepared
  row (U_L = union of ALL coarse supports, so J is in U_L at design depth; Lemma III-prep(d); G1 Def 4.1 leaves no contact or
  tiny room there), so each shared term is >= 0; Lemma 2.2 follows from H2 Fact 1.1(c) (near coordinates S_th of the data
  sign) with tail ratio <= 1/16.  G1 Prop 5.2 writes its condition (b) without the factor 1/kappa_m of the actual actions;
  P2's lambda~ = lambda/kappa_m is the correct normalization (PR-1).  The argument gives kappa_V <= -(3/4)||C~||_1/H(L), and
  per carrier kappa_V <= -(3/4) W, W = sum_G |C~_l| v_l(n_1(l)).  This is the restricted-model counterpart of Theorem
  III-Aobs (3)-(4), as P2 says.
- Corollaries 2.4-2.5.  CORRECT with fixable gaps.  (PR-3) Cor 2.5(iii) and Prop 2.6' need (mu*_{s_max(L)+1})^2 << 1/H(L),
  justified in P2 only by "mu* is doubly exponential"; since H(L) ~ 2^{L + s_max(L) + 12 * 2^L}, this needs s_max(L) >~
  log_2 L.  It holds for T_fin^{K2} because absorber targets (Def III-Tfinrounds) sit beyond max T(l-1) with length
  R(l) >= 2 log_2(1/mu_{p_0}) + 5, so s_max grows super-exponentially; a design-independent per-carrier repair is given
  (constant 5/8 instead of 1/4).  (PR-4) The "zero-data S_th/ZD" clause of Cor 2.4(i) uses P2's augmentation of G1's generator
  list by ZD moves; at a zero-data S_th coordinate outside supp V such a move acts on the minors only through the common mode,
  with coefficient ~ theta/Des, below the Step-A scale, so the clause is an artifact of the unbounded linearization.  All
  other conclusions hold in G1's own model (FR, TS, one-sided raises).  Cor 2.4(ii) (no anchor, thick support in supp V)
  and 2.4(iii): CORRECT.
- Proposition 2.6' / Corollary 2.6.  CORRECT, and stronger than stated (PR-5): the no-thick hypothesis is superfluous.
  Alignment of all coordinates s <= s_max(L), s != j, thick or not, already gives sigma M(rc) >= (3/4) W.  A free-target
  pair has a tiny minor only if some coordinate below s_max(L) is ANTI-ALIGNED.  Numerics: 2016 instances with thick
  aligned support, min sigma M/W = 2.21.
- Consequence 2.8.  (i) CORRECT.  (ii) CORRECT and valuable: R-ESC (3) stays true, but R-ESC.2's "c_k >= N_k - U_far - h_k
  >= c/H(L) (mod chain)" is unjustified, because h_k >= |u_k(s_0)| mu_{s_0}^2 |a_{s_0}|/nu can be of order mu*_{s_0} >> 1/H(L)
  (numerics: sum |gamma| h_k / sum |gamma| up to 0.51).  The escape list of R-ESC.2 must include the mate's common mode
  kappa_{V^G} < 0.  (iii) NOT PROVED as stated (overreach).  The 14b/R-ESC "escape" is a property of the MATE's switching
  coefficients gamma; Theorem 2.3 concerns the FARKAS cofactor vector C~.  Correct statement: an (R-S1)+escape residual
  needs (A) the obstruction structure of Theorem 2.3/Cor 2.4-2.5 AND (B) a mate escape from the corrected list of (ii).
  Nothing excludes G-THIN, outside switching or other strict non-peaks from (B).  Conditional link (SKETCH, referee): at a
  single-minor stage with a full-row-rank FR submatrix, Lemma 1.4(c) forces gamma|_G = c C_M + O(Des^C (t/(q_0 u) + Psi_J)).
  If outside switching Psi_J at the FR rows is negligible against the activity threshold, then sgn c = sgn lambda~ and
  kappa_{V^G} < 0, so the mate's escape IS the common mode; otherwise it is outside switching at the FR rows.  (iv)
  CORRECT but tautological.
- (D-sep) (P2: SKETCH).  SKETCH confirmed and sharpened.  (a) It is a design MODIFICATION.  T_fin^{K2} violates it because
  every pool target recurs in every block (schedule i_nu; also the fallback y^{(1)}), so singleton pseudo-minors {l}, {l'}
  have exactly equal slopes y(s)/y(s'), and single-carrier obstructions (1x1 minors) are not excluded by the slope argument.
  (b) The modification (main targets replaced by pool elements of the same support within 2^{-B}) preserves allowedness,
  (D-enum), Lemma B (Part III Theorem A_fin uses targets only through supports, q^* = 1 and density) and the field k_0.
  Absorbers carry no switching coefficient (Lemma III-CMp), so only main-carrier minors matter.  (c) The
  "identically-constant" case of P2's genericity sketch is PROVED: by multilinearity V_M'(x) = <a_0, w(x)> with
  w_j = +-V_{M''_j}, so a constant slope equals the slope of an older minor with a smaller group (numerics 3e-14).  If s is in
  the new target, the factor 1/n cancels and the slope is affine with nonzero coefficient.  (d) The quantifier point (Q) is
  resolvable (SKETCH): the next main stage's index, candidate target and signature are fixed combinatorially before the
  windows of the current main stage p, so the window condition E_p <= 2^{-p'}/(2 K_p' N_p') can be imposed.  The earlier
  pass's two-pass recursion does NOT work as stated, because absorber lengths R(l) depend on windows and change the stage
  numbering.  (e) In G1's EXACT restricted model only the qualitative clause r_M != r_M' is needed, because the slopes then
  coincide EXACTLY (PROVED).
- Theorem 2.10.  CORRECT as a conditional statement (mod (D-sep), memory Lemma H2 2.7(b), bookkeeping).  (PR-6) The range
  s, s' <= s_max(B) is automatic (disjoint groups and disjoint signature sets).  c_L -> 1 follows from the cost bounds.
  Referee remark (PROVED, exact model): for f with one pair of support coordinates whose ratio avoids the countable set of
  design slopes, no large (R1) stage is single-minor (R-S1) at all.

### Part 1 (Problem R)
- Lemma 1.1 / Corollary 1.2.  CORRECT (re-derived from N3 Def 1.1, Lemma 1.2, Lemma 2.2, N3-ref Lemmas W, S).  The
  strict-non-peak constant 7/t can be 5/t.  "Either oriented set satisfies the rate" suffices, since (i) and (ii) hold
  for either sign of Delta.  This refines N3-ref Lemma R-W.
- Proposition 1.3 / Corollary 1.4 (nested tuning).  CORRECT.  The Schauder-Tychonoff argument is complete.  (PR-7)
  Cor 1.4's bounds |N_i| = |Lambda(u 1_W)| and Lambda(e_c) use a diagonal U.  For a general compact dense-range U, choose c
  with a'(c)(UU^*a')(c) > 0 and the s_i where |Ue'| <= eps'_i.  The margin sequence need NOT be monotone: for mu_0, take i
  maximal with mu_i >= mu_0 (the earlier pass's monotonicity precision is unnecessary).  This answers N3 Section 1.6:
  non-C-tame attaining rows exist near every f, for every admissible T, in P2's one-block setting.
- Conversion lemma.  CORRECT by the intermediate value theorem, with (PR-8): the smallness of Phi_k, mu_k is RELATIVE TO
  |u_k(j)| (explicit inequality in the notes), and |z'_j| + delta_1 < 1 so that j stays free.
- Proposition 1.5 / Corollary 1.6.  CORRECT (re-derived from Part I def:certificate, lem:slack).  Constants checked on
  342,000 parameter points: p^*(g) <= r_0/(s(r_0)+1) is tight by the choice of theta; size >= 0.495 (gamma lambda)^{1/2};
  the gap term is the binding radius.  This is the lower half of the sqrt-weight law.
- Proposition 1.7.  CORRECT.  (iii) is the hypothesis set of [I, prop:scale] read backwards: valid only "if certified by the
  scale criterion".  Remark 1.8's impossibility (HEURISTIC) rests on additivity of conversion costs; if the costs did not
  add, the requirement would weaken to N >~ kappa/(gamma' lambda)^{1/2}.

### Part 3 (finite merging)
- Proposition 3.1: CORRECT (all five equivalences re-derived).
- Proposition 3.2: CORRECT except the last sentence (PR-9).  "Two mates in no common member" is unproved, since there is
  no Helly property for A(f).  Correct form: "a finite set of at least two mates outside U_NA(f) contained in no single
  member".
- Proposition 3.3: CORRECT; in (d) the conclusion is that of (b), not membership in Omega.
- Proposition 3.4: CORRECT (Mazur + Milman); (iv) is an abstract remark, correctly labelled.
- Definition 3.5 / Theorem 3.6: CORRECT, re-derived line by line; Remark 3.7(a): CORRECT.  Definition 3.5 is very
  strong, so Theorem 3.6 is close to a reformulation.  Remarks 3.7(b)-(d) and 3.8 are HEURISTIC, as labelled.

## 3. Required fixes (proofs in P2_ref_notes.md)
PR-1 G1 Prop 5.2 (b): divide each D_{m,i} by kappa_m (P2 already uses lambda~ = lambda/kappa_m).
PR-2 Thm 2.3(B): the proof gives -(3/4)||C~||_1/H(L); the per-carrier form -(3/4) W is the natural one.
PR-3 Cor 2.5(iii), Prop 2.6': replace "mu* doubly exponential" by the absorber growth of s_max(L) (for T_fin^{K2}) or by the
     per-carrier comparison (any design): sum_{TS in J} mu^2 |a||V| >= (5/8) nu^2 W once 2bH(L) + 2 mu*_{s_max+1}^2 <= nu^2/8.
PR-4 Cor 2.4(i): state the two-sided clause for TS only; drop the ZD augmentation or restrict it to generators with
     design-sized action.
PR-5 Prop 2.6': drop the no-thick hypothesis (tiny minors need ANTI-ALIGNED coordinates).
PR-6 Thm 2.10: coordinate range s, s' <= s_max(B) is automatic.
PR-7 Cor 1.4: general U (choice of c and of s_i); monotone margins unnecessary.
PR-8 Conversion lemma: smallness relative to |u_k(j)|; j stays free.
PR-9 Prop 3.2: "two mates" -> "a finite set of >= 2 mates".
Restatement (not a fix): Consequence 2.8(iii) -> "(R-S1)+escape = obstruction structure (A) AND mate escape (B)";
(D-sep) must be declared a design modification, with the window condition of (d) and the exact-model qualitative version.

## 4. What remains open (precisely)
1. Multi-minor (R-S1) stages: P2's Prop 2.9(iv) puts a|_A into the span of the p_L cofactor combinations.  This is a
   constraint only if |A| > p_L, and p_L is unbounded.  A span version of (D-sep) plus a bound on simultaneously tiny strict
   minors per stage is OPEN.
2. (R-S1) at non-consecutive or alternating stages (another residual class in between): (R-S2), (R-S3), (R-L), (R0^str),
   shifted blocks (term -kappa_m c_M in Lemma 2.1(i)).  All OPEN.
3. The mate-side escape (B) of 2.8(iii): whether an (R-S1) group's switching can escape through G-THIN or outside switching
   while its Farkas vector uses the thick common mode.  The conditional single-minor link needs: transfer of the start-row FR
   rows to the decomposition rows at the active scales, and K_*(w)^2 K >> Des^{C'}/(q_0 u).  OPEN beyond that.
4. (D-sep), quantitative form: compatibility of the window condition E_p <= 2^{-p'}/(2 K N) with the pigeonhole ladders
   (Q(w), b(w), u(w), Lemma III-count) is SKETCH; absorbers zero-data (mod chain).
5. Problem R positive: the JUNCTION problem (OPEN).  Transport of f's weak-peak staircase to approximants with exact
   first-order rebalancing, uniform D-norm control of block increments, and the constant comparison at the junction depth.
   Remark 1.8's impossibility of a slack-only junction is HEURISTIC (additivity of conversion costs).
6. Finite merging (P-II) at every f: OPEN.  Far-locality of tuned/KSB/engineered recoveries (Remarks 3.7(b)-(d)) is HEURISTIC.
7. Hence density of NA((c_0, p), l_2^2), for the designed T or any admissible T, remains OPEN, and so does the existence of
   a 2-dimensional space without Lindenstrauss property B.

## 5. Single most valuable idea
SLOPE RIGIDITY.  The exact common-mode identity forces the cofactor combination of any (R-S1) Farkas obstruction to be
EXACTLY proportional to the base on thick design-depth support (V = kappa_V a, kappa_V robustly negative).  Hence f's thick
ratios a_s/a_s' must equal DESIGN slopes V_M(s)/V_M(s') of the resonant minor.  Consecutive (R1) stages have disjoint groups
(memory), so persistence needs two different design slopes to coincide; generic target values prevent this.  In the exact
model a qualitative genericity of pool targets suffices, and for f outside a countable union of hyperplanes no single-minor
(R-S1) stage occurs at all.  This converts a residual about f-dependent near-coincidences into a statement about countably
many design numbers.  Runner-up (most robust stand-alone tool): the Schauder-Tychonoff nested tuning of Prop 1.3/Cor 1.4.
It gives attaining rows near every f, for every admissible T, with infinitely many exactly tuned deep carriers.  So a
counterexample can never prevent tuning, only the precision of available shapes relative to their weights.

## 6. Numerics (sanity checks only)
P2_ref_work/cm_check2.py: identity (2.1) and one-line form, max error 4.4e-15; Prop 2.6' with thick aligned coordinates, min
sigma M/W = 2.21 over 2016 instances; signed Hilbert sum = kappa_{V^G} nu to 8.9e-16, unsigned R-ESC sum up to 0.51 per unit
|gamma|.  P2_ref_work/dsep_multilinear.py: multilinear reduction of (D-sep), max error 2.8e-14 (2000 instances).
P2_ref_work/cor16_check.py: Cor 1.6 constant chain on 342,000 grid points (all inequalities hold; tight where designed).
