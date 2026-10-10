# Referee report on V2 (Round 7): multi-block rays (B) and coherent shift resonance (C)

Refereed: r7/V2_notes.md (= V2_head + V2_part1..4 + V2_tail, byte-identical, checked with diff), V2_work/* (re-run), against
paper/martin_density_note.tex (Sections 1, 7, 8: lem:threshold, eq:margin, def:twopiece, def:SC, lem:scrambling, thm:engineered,
cor:D1, def:SLD, thm:SLD, lem:phicalc, lem:switchbudget, lem:peakshift / eq:didentity), Round 5 (Z3 Theorem E, Lemma U, Lemmas 3.1,
3.2, 5.1, Prop. T with (HF), (BS); Z4 Lemma 5.0, Z4-ref Prop. 5.6'), Round 6 (Y1 Lemmas T, T2, T3, 3.1-3.6, Cor. M1 + Y1-ref;
Y4-ref C.1-C.8) and Round 7's V1 (unified design, assembly, Master Theorem II) with its referee report r7/V1_referee.md (V1 correct
in all PROVED claims).  My part files: r7/V2_ref_part1..4.md; assembled proofs of all fixes: r7/V2_ref_notes.md; scripts:
r7/V2_ref_work/{qb_jac_check.py, jac_check2.py, tworay_tau.py, thmB_toy.py}.

## 0. Bottom line
Every claim V2 labels PROVED is CORRECT, up to seven precisions (P1)-(P7) that change no conclusion; the two SKETCHES are plausible
but have two further gaps (g4), (g5) beyond the three V2 lists.  The central result, Theorem B, is right and important: the
d-row (and the whole exact-cone) Hoffman constant at a clean sub-window can be made a DESIGN/u constant for EVERY configuration,
because (i) by Lemma H only NONZERO minors matter, (ii) the minors are multi-affine polynomials in the carrier VALUES (row factors
1/A_m aside), and (iii) by the Lojasiewicz inequality all tiny minors of one pattern have an EXACT common zero within a design power of
their size, which two-sided per-carrier tuning (pulls + private banks, diagonal base) realizes at cost o(T_lo^2).  I re-derived each
step, checked that the minors capture V1's ray components and the multi-block obstruction (a 4x4 minor equals the 2x2 ray
d-determinant; a degree-3 cyclic three-block example with NO small 2x2 minor), and confirmed numerically that exactification drops the
true Hoffman ratio from ~1/beta to O(1).  Combined with V1 (now refereed correct), item (B) of ADDENDUM 6 (multi-block rays) and
the d-row part of (m) are no longer residuals for D^{V2}, F finite.  Theorem C1 is also correct: making the shift-pinning rate rho^sh
itself a rate object turns item (C) into the dichotomy "pinned with a design x u^{-3} constant" / "near-exact coherent shift
resonance (rho^sh <= b)"; its case (I) contains Y1's (SP_w) (then rho^sh >= 1), and it is an independent alternative to V1's
shift-cost criterion (SH_w) (neither implies the other as far as I can prove: precision (P7)).  Hence Master Theorem III (PROVED,
given V1), sharpened to III': for D^{V2}, diagonal U, F finite, f is in Rec unless at all but finitely many levels every clean
sub-window has rho^sh <= b(w) AND V1's shift cost c_pi(w) <= b(w).
That residual (C*) is OPEN; V2's Part 4 describes it correctly (rigidity of shifted data, oscillating profiles force shifts,
fine-tail completion) and I add two obstacles to its sketched route.  No counterexample is claimed; nothing I checked points to one.
Lemma Z and density of NA((c_0,p_N), l_2^2) remain OPEN for every admissible T, including D^{V2}.

## 1. Verdicts
| Claim | V2 label | Verdict | Main point / fix |
|---|---|---|---|
| Lemma H (Hoffman via independent row sets and minors) | PROVED | correct | projection + normal cone + conic Caratheodory; Cauchy-Binet; equalities as two rows; numerics re-run |
| Lemma L (simultaneous exactification, Lojasiewicz) | PROVED | correct (wording precision) | BCR 2.6.7 with g = dist(., Z_S) (semialgebraic); alternative (i) means NO consistency hypothesis is needed. Remark (c)'s example is not a polynomial system: use pi = v_1^2 |
| Lemma QB (threshold buffer at a peak) | PROVED | correct, precision (P1) | k_0 = c must be ALLOWED in C_1, h_0 (a block may have no other non-degenerate peak); T2(b)'s upper bound holds with k_0 = c (proof in ref notes 1). 3000 random blocks, 0 violations of (a), (b), (c) |
| Two-ray example; component exactification insufficient | PROVED | correct | re-embedded in tau-coordinates: 4x4 minor = delta = v_1 v_4 - v_2 v_3, true l_1 Hoffman ratio exactly 4/delta, 1 at delta = 0 |
| Design D^{V2}, Lemma 2.1 | PROVED | correct | admissible (only window parameters change), N-free (objects of level <= l touch <= l blocks), recursion order fine; no lower bound on b(w) is used anywhere; (2.1) re-derived |
| Lemma 2.3 (buffer peaks) | PROVED | correct | alpha-mass count; the stated relative margin is valid (a sharper one holds); the parenthesis "exceeds u by any design factor" is false at the first sub-window of a level but never used |
| Theorem B (multi-block exactification) | PROVED | correct, precision (P2) | Lojasiewicz point + one Lemma TU solve + buffer/donor; minors = (row factors) x pi_O(values); Hoffman <= C_f^l Design^2/u. (P2): the d-rows (hence L_0 and the objects) must be those of the transplant actually used — KEPT strict non-peaks (V1 Prop. TR); then (A2)'s no-donor clause matches V1 and dropped carriers' statuses are irrelevant |
| Corollary B.1 | PROVED | correct (given V1) | Hoffman projection onto Sigma^# (with box rows) replaces V1's ray removal; V1's later steps use only the l_1 distance of tau and tau', the sign rows and the box (checked) |
| Lemma 3.1, Def. 3.2 (shift-extended system, rho^sh) | PROVED | correct, precision (P3) | (R1)-(R7) re-derived from Y1 3.1-3.4 / eq:peakshift / eq:didentity, none assuming a shift bound; infimum is an attained LP minimum. (P3): the pattern must include the window classifications (nearly neutral set, (R7)-set, I_sh and source types, G_pk/G_np, F ∩ T(l)) for rho^sh to be a rate object |
| Theorem C1 (dichotomy) | PROVED | correct, precision (P7) | homogeneity; all blocks pinned at once; (SP_w) => rho^sh >= 1. (P7): rho^sh >= u and V1's c_pi >= u are INDEPENDENT pinning criteria (rho^sh has no box on tau; c_pi charges tiny rooms) — use both (Master Theorem III') |
| Corollary C1.1 | PROVED | correct, precision (P4) | c^comb <= C Design viol re-derived; (P4): weight m^nat depends on F (use the design mass on S \ ([1,l] ∪ T(l))) and the sign-sphere needs a Lipschitz projection |
| Theorems E^>=, E^SC | PROVED | correct | Theorem E uses d-neutrality only in averaging and in cor:D1 (Lemma U is one side at a time); E^SC via thm:engineered at f_j; (SC) passes to subsets |
| Proposition C3, Cor. C3.1(a),(b) | PROVED | correct | trivial subtraction; far-swallowing; target density per block (same (i_r) in every block) |
| Cor. C3.1(c) (maximal contact) | PROVED | correct only for z = eps_0 constant off F — precision (P5) | for full SIGN-MIXED contact the identities are void but (SP_w) can fail (self-aligned signature signs make all coarse peaks swallowing type); case (II) not excluded there |
| Cor. C3.1(b) reading | HEURISTIC | correctly labelled | — |
| Proposition C4 + Example | PROVED | correct | sandwich re-derived; scope = rows keeping l a peak (cheap companions do); example's side-- condition should read phi <= c z R_m^* w_m (finer targets) |
| Lemma C5 (fine-tail completion) | PROVED | correct, limitation (P6) | Schauder-Tychonoff on [-1,1]^{J_fine}; continuity via dominated convergence and weak* continuity of J_m; coarse values exactly unchanged. (P6): completes ONE ray of shift vectors only |
| Near-coordinate conversion | SKETCH | plausible | — |
| Theorem C6 (stable shifted resonance) | SKETCH | plausible sketch, incomplete | V2's gaps (g1) block scalars, (g2) conversion, (g3) (SC) at companions, plus NEW (g4) scale-dependent shift DIRECTIONS with >= 2 shifted blocks vs one-ray completion (P6), (g5) completion and coarse absorption must be a joint fixed point |
| Remark 4.5 (Jacobian of (theta, A)) | PROVED | correct | re-derived from Lemma T; central differences on 1169 blocks: entries to 4.7e-7, det ratio 1.000000 |
| Master Theorem III | PROVED mod V1 | correct (V1 now refereed correct); sharpened to III' | (SH_w) used only via K_d (Theorem C1(I) supplies it); (VR_w) only in ray removal (Theorem B replaces it); smaller b and tuning eta <= T_lo^4/(l Design) keep all V1 estimates. III': f in Rec if infinitely many levels have a clean w with rho^sh >= u OR (SH_w) |
| Residual (C*), item (E) | OPEN | correct statement, sharpened | f notin Rec only if rho^sh(kappa(w), f) <= b(w) AND c_pi(w) <= b(w) at every clean w of all large levels |

## 2. Main findings (proofs in V2_ref_notes.md)
**F1 (Theorem B is right, and the determinantal obstruction is genuinely beyond linear tuning).**  Every V1 ray component is (design
number) x (a minor of A_kappa(v)): for an extreme ray r cut out by n-1 tight independent rows A_{J'}, det[A_{J'}; (Z5)_m] = +-||c||_1
D_{r,m}(v)/A^#_m with c the cofactor vector (without the row factor 1/A^#_m: +-||c||_1 D_{r,m}(v)).  So Theorem B contains V1's (C4).  It also contains obstructions with no small component
and no small 2x2 minor: in the cyclic three-block example (thmB_toy.py) the only tiny minor is a degree-3 polynomial (the 3x3 ray
d-determinant); the Lojasiewicz move (here of size ~beta) zeroes it, robust minors stay >= 0.3, and the l_1 Hoffman ratio drops from
4e2 ... 3e5 (beta = 1e-2 ... 1e-5) to 1.3-1.6.
**F2 (P2: which system).**  Theorem B's (A2) no-donor clause is not satisfied by V1's assembly if L_0 is read as "all class-G strict
non-peaks" (dropped anti-type near-threshold strict non-peaks and anti-type tiny-margin peaks may sit in blocks without a donor raise).
With the d-rows of V1's transplant (kept carriers only) the clause holds exactly and the statuses of dropped carriers enter no minor.
**F3 (P3, P4: rate-object bookkeeping).**  rho^sh(kappa, f) is a function of f only once kappa records the window classifications;
c^comb must use an F-free weight.  Both are bookkeeping.
**F4 (P5: maximal contact).**  C3.1(c) needs constant contact sign.
**F5 (P7: two pinning criteria).**  rho^sh >= u (Theorem C1) and V1's c_pi >= u (Lemma S) are independent sufficient conditions
for shift pinning (rho^sh has no box on tau, c_pi charges tiny rooms and ignores the d-identity); with Theorem B both work without
(VR_w), giving Master Theorem III' and a smaller residual (C*): rho^sh <= b AND c_pi <= b at every clean w of all large levels.
**F6 (gaps of the (C*) route).**  (g4): in case (II) the shift is unpinned, its direction can change from scale to scale inside a window,
but Theorem E averages all scales at ONE companion and Lemma C5 completes one shift ray only; (g5): completion and coarse absorption
interact.  A route for (g3) ((SC) at companions by a level-by-level fine-tail regularization) is sketched in the ref notes.

## 3. Attacks attempted (none broke a PROVED claim)
weak* vs norm (Lemma C5 continuity in the product topology; costs in norm via Z3 Lemma 3.1); uniformity in t (Lemma 3.1 errors and
Theorem B's companion are scale-independent within W(w)); in the window (all new constants design x u^{-k} x C_f^l, Q(w) absorbs;
note u(w) need not be << 1/Design(l) at the first sub-window, and nothing needs it); in the number of active carriers (objects over
all subsets of [1,l]); along companions (one companion per window; C_f from convergent forced data); simultaneous exactifications
(values of L_0 set EXACTLY by one solve after all other moves; tiny values go to exactly 0, never change sign; robust objects move by
Lip eta << u); Hoffman/Farkas constants (RHS-independent; 0 feasible; box rows +-e_l; row factors 1/A_m with A_m <= 1/2); design
N-independence (objects touch <= l blocks; p_N simply omits patterns with absent carriers); Lemma B density (only window parameters
changed); non-attained infima (rho^sh is an LP minimum; Lojasiewicz nearest zero exists; Hoffman projections exist); signs and
one-sidedness (data vs decomposition conventions of Delta d: Delta^{data} = -Delta d^{dec} up to M; configurations (i)/(ii)); near-contacts
vs contacts (free coordinates of kappa have robust room; tiny target rooms closed exactly); c_0 vs l_infty (companions, completed rows
have z in l_infty, allowed by Theorem E); finite vs infinite (F finite; infinite peak sets via alpha-mass; Sigma_Omega never cofinite);
hidden assumptions on T (diagonal U and bounded gaps are design choices); quantifier order (objects and b(w) before f; companion after
f and w; data after g, rho, t).  Suspected problems examined: (i) Lojasiewicz point flipping the type of a strict non-peak (impossible:
only tiny values can flip and they are sent to exactly 0); (ii) buffer peak not swallowed (push by z-moves, banks or pulls on its far
signature coordinates in either direction); (iii) Theorem C1 circular (no: (R1)-(R7) use no shift bound); (iv) Hoffman bound depending
on N through (2A_max)^{-N} (A_m <= m 2^{-m} <= 1/2, so these factors are >= 1).

## 4. Numerics (r7/V2_ref_work; sanity checks only)
qb_jac_check.py: Lemma QB on 3000 random blocks (k_0 = c allowed): 0 violations ((a) 3000, (b) 4434, (c) 891 + 6629 tests).
jac_check2.py: Remark 4.5 Jacobian, 1169 blocks: max relative entry error 4.7e-7, det ratio 1.000000.
tworay_tau.py: two-ray example in tau-coordinates: minor = delta, Hoffman ratio 4/delta, Lemma H bound ~22/delta, ratio 1 at delta = 0.
thmB_toy.py: cyclic three-block degree-3 obstruction removed by exactification (Hoffman ratio ~1/beta -> 1.3-1.6).
V2_work/hoffman_minors_check.py re-run: identical to V2's report.

## 5. Single most valuable idea
Hoffman constants through NONZERO minors (Lemma H) + Lojasiewicz exactification of all TINY minors at once (Lemma L), with the
non-explicit Lojasiewicz exponent absorbed by the design (b(w) a design power of T_lo(w)): any finite polyhedral system whose
coefficients are polynomials in tunable carrier values becomes, at a cheap companion, a system whose minors are either exactly zero or
robust, so its Hoffman constant is design/u for EVERY configuration.  This disposes of all f-dependent d-row Hoffman constants
(multi-block rays, mixed/uncompensated blocks) in one stroke.  (Runner-up: making the shift-pinning rate rho^sh itself a pigeonhole
rate object, which reduces (C) to near-exact coherent resonance.)

## 6. What remains open after V2 (+ this report), design D^{V2} (on V1's D_Omega), diagonal U, finite I
(C*) F finite, at all but finitely many levels every clean sub-window has rho^sh(kappa(w), f) <= b(w) and V1's shift cost c_pi(w) <= b(w)
(by (P7) both are necessary for f notin Rec): a block lacking a shift source whose
peak shift traces are compensated (near-)exactly by zero-cost switching obeying the d-identity.  Recovery of mates using such resonances
needs shifted two-piece data (Prop. C4), i.e. (C*-1) EXACT absorption of the fine-peak residues -sum_m Delta_m M_m sum_{fine peaks} vs
lambda u on the finitely many coarse free coordinates (fine tails are completable, Lemma C5); (C*-2) (SC) at the companions in
configuration (i) (Delta^{data} < 0); (C*-3) exactification of the block scalars theta_m, A_m entering the shifted system; (C*-4) with two
or more shifted blocks, a shift DIRECTION that is constant along the scales of a window (or per-block fine admissibility); (C*-5) joint
completion/absorption.  At constant-sign maximal contact (C*) does not occur; at sign-mixed full contact it is not excluded.
(E) infinite F: (O4-crit), (O4-nd), (O4-box) and the finite-F core at infinite F (Theorem B and Theorem C1 are local in the level and
should transfer to Y3's framework — not checked).
Lemma Z and density of NA((c_0,p_N), l_2^2) and of NA((c_0,p), l_2^2) remain OPEN for every admissible T, including D^{V2}.
