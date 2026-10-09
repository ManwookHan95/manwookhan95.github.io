# Z2 referee, part 4: attacks tried, numerics, a relaxation that FAILS, and assessment

## 1. Attacks tried (all failed to break a PROVED claim)
1. Near-contacts vs exact contacts in the budget: the gloss "vanishes off F up to l_1-mass O(t)" breaks (part 1 §2), the inequality does not;
   no proof in Z2 uses the gloss (Theorem B± uses the phi-weighted form, Theorem S needs exact contacts and says so).
2. Sign-mixed room with a constant sign per carrier: the pinning uses phi_z(-Delta c_l v_l(s)), and the sign of -Delta c_l v_l(s) is the SAME on all
   of S_l (v_l > 0), so the min over a single sigma is the right room (theta_l). A z that is sign-mixed only on far coordinates gives tiny theta_l
   (2^{-s}-weights), which (W±) charges correctly; such f are the "super-fast room decay" class, honestly left OPEN.
3. Slaving of coarse carriers by unpinned targets (G3-referee objection): Z2 removes the touched points (S*_l) and assumes room there ((W*)).
   With B finite the removed set is finite. Correct.
4. One-sidedness of the swallowed switching: needs (H3) or B finite (cost function); the claimed K* t bound needs the unified triangular system
   (part 2 §1(b)); numerically the unified unrolling is valid (checks.py).
5. Uniform shift Delta d: G3 pinned it through ALL carriers (3.5(c)); with unpinned bad carriers this fails, and Z2 correctly replaces it by one
   pinned non-degenerate good peak (2.1, (H4)). Degenerate bad peaks with the swallowing sign are genuinely free on both sides (alpha = 0) and are
   excluded by (H5) — correct diagnosis: such usage is not two-piece data (omega must avoid peaks).
6. Size of the data: two-piece data of size ~1/t (t||b|| <= A_0'): the one-sided expansion only needs no flips on F (c_1 A_0' <= min_F|a_j|), no kinks
   (sign condition), and O(c_1) relative Hilbert error. S3 Cor D1 is applied to FIXED data for each window (no uniformity needed). Actually the
   budget shows the switching amplitude through a fixed coarse carrier is O(1) anyway.
7. Weak* vs norm: every convergence used is in norm (p*(g - g_avg) <= 2(1+||U||)K_2' T_hi/n -> 0); transfer peaks use norm density of tails.
8. Non-attained infima: optimal two-sided decompositions exist (weak* compactness, A Fact A); the Hoffman projection is onto a closed polyhedral cone.
9. c_0 vs l_inf, infinite K: V' may have infinite support on K; P2A 1.6 / S3 3.3 allow b in l_1(F cup K) with infinite K. Correct.
10. Hidden assumptions on T: the "any admissible T" lemmas (1.2, 2.1-2.3, 4.1, 4.4, 5.1-5.3) use only G3 part 2 and A Lemmas 7.1, 7.2 (Lemma B's
    conclusion); Theorems B± and S are stated for SLD only. Correct.
11. I finite vs I = N: everything is for p_N; martin-tail (G3 referee §3) transfers density. Correct.
12. RELAXATION THAT FAILS (recorded so that nobody tries it): S3 Cor D1 accepts Delta d_m >= 0, so one might hope to drop d-neutrality in (S_inf)
    when a_l >= 0 for all bad l. This is WRONG: for data with Delta d != 0 the base difference must be v = sum_m R_m*(omega_Delta,m) - sum_m Delta d_m R_m* w_m
    (P2A 1.6), and R_m* w_m carries signature mass on the ROOMY good signature sets, where it is not z-signed; so the second representation is not
    two-piece data. Theorem S's exact d-neutrality (cone constraint, or a_l = 0) is necessary for the construction, not an artefact.
13. Counterexample hunting: Z2 claims none. Prop 5.3(c) (a non-recoverable mate must be destroyed by generic perturbations of f) is a correct
    necessary condition. Nothing in Z2 suggests a counterexample; the honest open classes are listed (with the (BT) correction of part 3 §5).

## 2. Numerics (Z2ref_work/)
* checks.py: (F1)-(F4) to 1e-13; theta-split (40000 adversarial instances incl. near-contacts on V = 0 coordinates, scales 1e-3..1e3) satisfies even the
  sharper bound ||r_±|| <= ||e|| + (1/2)(sum phi_z(B_+) + phi_{-z}(B_-)) = ||e|| + t/(2q_0) (max relative violation 8e-14); alternating-sign room:
  min theta/((3/4)2^{-(s_1-s_0)}||v||) = 1.52 >= 1; unified triangular unrolling: S_1/bound <= 1/3.
* toy_signmixed.py (CLARABEL SOCP, finite model: F = {0,1}, EVERY other coordinate a contact, 2-point signatures with opposite contact signs,
  targets touching coarser signatures, all 4 carriers peaks): for 3 random mates and t in {3e-2, 1e-2, 3e-3}: switching budget <= t/q_0 with margin,
  Lemma 1.4 (sign-mixed pinning) holds to 1e-11, peak signs sigma_k omega_+ <= 0 <= sigma_k omega_- and identity (2.1.1) hold to solver tolerance/t,
  d-identity remainder |r| <= 2t/sigma_m. (Finite models are degenerate — sum|Delta c| does not scale with t there — so only signs/algebra are tested.)

## 3. Assessment
Z2 is a careful and correct piece of work. No PROVED claim is false. Fixable gaps: (i) the gloss on the switching budget near near-contacts;
(ii) the unified triangular system needed for Lemma 2.5(b) (and hence (S_inf)); (iii) a constant in 3.3(d); (iv) the status table of hard cases must
exclude (BT) points (S3 Cor D2: (BT) points with ANY contact set are in R for any admissible T), so maximal contact / super-fast room decay are open
only off (BT); (v) Prop 5.1's "no design removes swallowing" is about first-order base cost only; "signatures inside supp a do not help" is heuristic.
Real progress: Theorem B± (sign-sensitive room; cofinite contacts and geometrically decaying near-contacts) and Theorem S (finitely generated
exact resonances in the SLD space recovered with arbitrary block structure, without Lemma Z). Lemma Z remains OPEN; the remaining classes for SLD are
(F finite, not (BT)) with infinitely many non-resonant or non-d-neutral exactly swallowed sets, or super-fast room decay, or (H5)-type degenerate
bad peaks; and F infinite without room.
