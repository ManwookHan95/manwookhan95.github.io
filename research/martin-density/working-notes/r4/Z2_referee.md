# Referee report on Z2 (Round 4): Lemma Z by other routes — sign-mixed room, exact resonances, hard cases, no-go results

Setting checked: canonical base, Martin's norm with finite block set I_N (p_N; martin-tail), the SLD operator of G3 where Z2 says so, otherwise any
admissible T. I read Z2_notes.md and Z2_part1..5.md in full and re-derived every PROVED item. Supporting files: Z2_ref_part1..4.md, assembled with proofs
in Z2_ref_notes.md; scripts ctx/r4/Z2ref_work/checks.py (elementary lemmas) and toy_signmixed.py (SOCP toy model with cofinite sign-mixed contacts).

## 0. Bottom line
No PROVED claim of Z2 is false. The two main theorems are correct:
 * Theorem B± (SLD): R_0 ⊂ R_0^± ⊂ R. The sign-sensitive room theta_l = ||v_l 1_{S_l\F}|| - |<v_l 1_{S_l\F}, z>| replaces G3's (SR); cofinite contact sets with
   sign-mixed signatures and geometrically decaying near-contacts are recovered.
 * Theorem S (SLD): first rows with finitely many exactly swallowed signature sets ((H4), (H5), (W*)), or infinitely many all resonant and d-neutral ((H3), (W*)),
   are in R, with arbitrary block structure, without approximating f. This settles G3 6.3(d) for finitely generated exact resonances, under (H4), (H5), (W*).
Fixable gaps: a wrong gloss on the switching budget near near-contacts; Lemma 2.5(b) needs the unified triangular system; a constant; and the
hard-case table must exclude (BT) points (S3 Cor D2). Lemma Z remains OPEN. Nothing points to a counterexample.

## 1. Verdicts
| Claim | Z2 label | Verdict | Issues |
|---|---|---|---|
| Switching budget sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0 | PROVED | correct (gloss wrong) | Inequality re-derived (A Lemmas 7.1, 7.2 + (F1)); needs no smallness of t. The gloss "vanishes elsewhere off F up to l_1-mass O(t)" (summary, 4.1(c)) is FALSE with near-contacts: off F ∪ K only sum (1-|z_j|)|Delta B(j)| <= t/q_0 (e.g. z_j = 1 - 1/j, Delta B(j) = c_j >= 0 costs sum c_j/j). No proof uses the gloss. |
| Theorem B± | PROVED | correct | Pinning: sign(-Delta c_l v_l(s)) is constant on S_l, so the min over one sigma is the right room; triangular unrolling re-derived; G3 3.5, part 4, 5.1, 5.2 never use (SR); 5.3 along a subsequence. Example 1.3(c): "(W±) if s_1 - s_0 <= C l" is a condition on the design's S_l (G3 (D0) does not fix them). |
| Peak pinning of the shift | PROVED | correct | (2.1.1) re-derived from G3 2.4(c); d-identity re-derived. "O(t)" means O(K* t) with window constant, and needs a PINNED non-degenerate peak (SLD). |
| theta-split | PROVED | correct | Three cases re-derived; even ||r_±|| <= ||e|| + t/(2q_0) holds. 40000 adversarial instances: max relative violation 8e-14. |
| Pinning modulo swallowed carriers | PROVED | correct with fixable gap | (a) correct (removing bad-target points from S_l answers the G3-referee "slaving" objection). (b) "rho_l >= 1/Lambda* absorbed" gives only Lambda*^2 t; the stated K* t follows from the UNIFIED triangular system over good |Delta c_l| and bad (tau_l)_- (all right sides contain only later good terms). One-sidedness needs (H3) (or B finite via the cost function). |
| Theorem S | PROVED | correct with fixable gaps | Hoffman projection, cone, theta-split data, balance b^-(xi) = -sigma_m sum a_l tau'_l = 0, one-sided expansion (A Lemma 7.2 is an identity: no flips, no kinks), windowed averaging, S3 Cor D1 requirements — all checked. Fixes: unified system (for S_inf); |omega_+(k_l)| <= (3+eta)/t, not 3M/t; (H4) automatic, (H5) vacuous under S_inf; "mixture" remark unproved. |
| Contact sandwich, cushions | PROVED | correct | First-order statements; Hilbert term still constrains B on F at second order. |
| Route (b)(i) | PROVED | correct with fixable gaps | Construction of f from (a, z) re-checked (q**(zhat) = 1, uniqueness). It is a FIRST-ORDER BASE-COST statement: it does not put f outside R (Thm S, B±, S3 D2 recover many such f). "Signatures inside supp a do not help": HEURISTIC. |
| Route (b)(ii) Lemma Z_cert | PROVED | correct | C Thm 7.4 / S3 Cor D1 at f' (any T); converse for SLD via G3 Cor 6.4. |
| Route (b)(iii) Omega | PROVED | correct | Preprint A residual theorem and nonvacuity proposition checked; A_eps argument correct. |

## 2. The main points I checked
* **Theorem B±.** The only places where G3 uses (SR) are 3.2-3.4. G3 3.5(b) uses |x| + |y| <= |x - y| + phi_z(x) + phi_{-z}(y), valid for every z, so cofinite
  contacts are harmless once the switching difference is pinned. The window hypotheses of G3 5.2 hold along a subsequence by (W±).
* **Theorem S.** For B finite the cost of a bad switching is a finite sum of convex piecewise-linear functions (T_0 = U_B supp y_l is finite), so the zero-cost
  switching set is a polyhedral cone, and Hoffman's bound (constant H(f)) projects the actual switching onto it at cost O(H K* t). d-neutrality is forced up to
  O(K* t) by ONE pinned non-degenerate peak (2.1 + (H4)), so the cone can include exact d-neutrality. The theta-split then gives EXACT P2A data on every
  window scale; the + side is exact at the bad coordinates, the - side differs by the switching. I verified the second representation (needs d(omega^-) =
  d(omega^+)), the balance of both sides, the Gamma_w bounds by seminorm comparison with the actual decompositions (G3 2.3(d) on both sides), and the
  one-sided expansion for data of size ~1/t. S3 Cor D1 needs exactly: b^± in l_1(F ∪ K) with the sign conditions, omega^± in c_00 off the peaks,
  g in C(f), F finite, Delta d >= 0, kappa_w < 1/rho^2 — all satisfied; it is applied to fixed data for each window, so no uniformity is needed.
* **Failed relaxation (recorded).** S3 Cor D1 allows Delta d_m >= 0, so one may hope to drop d-neutrality. This fails: data with Delta d != 0 need
  -Delta d R_m* w_m inside v = b^+ - b^-, and R_m* w_m has signature mass on roomy good signature sets (good peaks), where it is not z-signed.
* **Numerics.** checks.py: (F1)-(F4), theta-split (sharp form), alternating-room bound (ratio >= 1.52), unified unrolling. toy_signmixed.py: in a model where every
  off-F coordinate is a contact and each 2-point signature carries both contact signs, the budget, Lemma 1.4, the peak sign conditions, (2.1.1) and
  the d-identity hold to solver tolerance (finite models are degenerate, so this tests signs and algebra only).

## 3. Corrections requested
1. Replace "z-signed on contacts and vanishes elsewhere off F, up to l_1-mass O(t)" by "z-signed on K up to l_1-mass t/(2q_0); l_1-mass <= t/(gamma q_0) on J_gamma;
   in general only the (1-|z_j|)-weighted mass off F ∪ K is O(t)" (summary row 1, 4.1(c)).
2. Lemma 2.5(b): prove the K* t bound by the unified triangular system (one paragraph; part 2 §1 of my notes).
3. 3.3(d): |omega_+(k_l)| <= (3 + eta)/t; note that the budget even gives Phi(k_l)|Omega_±(k_l)| = O(1) at d-neutral bad carriers.
4. Theorem S: state that (H4) is automatic and (H5) vacuous under (S_inf); state "settles G3 6.3(d)" with the hypotheses (H4), (H5), (W*); mark the mixture
   remark of 3.1 as unproved.
5. Prop 5.1: say "first-order base cost"; label the supp-a sentence HEURISTIC.
6. **Hard-case table (4.5, 6): exclude (BT) points.** S3 Cor D2 (refereed) puts every (BT) point — F finite, all Q_m finite, no degenerate peaks, (MS) — in R
   for ANY admissible T and ANY contact set. So maximal contact and super-fast room decay are open only OFF (BT). The Hoffman-constant obstruction of 4.2
   is an obstruction to the METHOD of Theorem S, not to recovery. Theorems B± and S are new exactly where (BT) fails (infinitely many strict non-peaks,
   degenerate peaks, failure of (MS)); S_inf with B infinite always concerns non-(BT) points.
7. Example 1.3(c): add that the gap condition s_1 - s_0 <= C l is a design condition on the S_l.

## 4. Assessment
Z2 enlarges the recovered class for the SLD space in two directions that G3 left open. First, room is sign-sensitive: contact sets may be cofinite as
long as the contact signs are mixed on the signature sets. Second, exactly swallowed signature sets are harmless when the free switching is finitely
generated (or infinitely generated but resonant and d-neutral). The Baire reformulation is correct and honest about its limits.
What remains for SLD, after this report: F finite, NOT (BT), and one of (a) infinitely many exactly swallowed sets with non-resonant or non-d-neutral
carriers (maximal contact off (BT) is the model case), (b) approximate swallowing with super-fast room decay, (c) a bad degenerate peak with the
swallowing sign; and F infinite without room. In (b) the switching vector is z-signed only up to O(t), and S3 Cor D1 needs exact data. This "exactness
versus scale" tension is the real remaining obstacle. Nothing suggests a counterexample.

## 5. Most valuable idea
Do not drop the unpinned switching; make it exact. At first rows whose signatures are exactly swallowed, the free switching lives in a polyhedral
zero-cost cone. On each window, Hoffman's bound projects the actual two-sided switching onto that cone at cost O(t). One pinned non-degenerate peak pins
the uniform shift, so the cone can be taken exactly d-neutral. The theta-split then divides the projected switching coordinatewise between the two sides.
The result is EXACT two-piece data at every window scale. A whole window of such data is averaged (G3 5.2), and S3 Cor D1 recovers the average, whatever
the contact set and the block structure. This connects G3's signature pinning with S3's engineering.
Natural next step: an "approximately two-piece" version of S3 Cor D1 that tolerates a first-order defect (sign errors of l_1-mass O(scale) on
near-contacts). It would cover approximate swallowing.
