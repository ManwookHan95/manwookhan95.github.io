# U1 notes (Round 8): the finite-F residual (C*) of Master Theorem III — exact shifted data at companions

Setting: paper/martin_density_note.tex (notation as there), finite block set I = {1..N}, p = p_N, first rows f with FINITE base support F,
diagonal base.  Design: V2's D^{V2} on V1's D_Omega, rebuilt on U4's T_final and enlarged to D^{U1} (part 3).  Labels PROVED / SKETCH /
HEURISTIC / FALSE / OPEN; "PROVED" means: complete proof here, using only results that were refereed in earlier rounds (listed in 5.6).
This file = U1_head.md + U1_part1.md ... U1_part5.md (byte-identical copies).  Numerics: r8/U1_work/.

## 0. Summary
Task: complete V2's Theorem C6 by closing (C*-1) exact absorption of fine residues on coarse free coordinates, (C*-2) (SC) at companions
for blocks with Delta d < 0, (C*-3) exactification of the block scalars, (C*-4) one shift direction along a window, (C*-5) the joint
completion/absorption fixed point; deliver MASTER THEOREM IV or the precise remaining step.

What is proved.
 (1) STRUCTURE (part 1).  Exact two-piece data at a first row f' exist iff the single certificate V(Domega) = sum_m R_m^*(Domega_m -
     d'_m(Domega_m) w'_m) is z'-admissible off F' (Lemma 1.1).  Every carrier outside the switching support enters V with the FORCED coefficient
     -Delta_m lambda_l w'(l); the shift of a block is tied to the switching values by the DATA IDENTITY
         Delta'_m kappa'_m = sum_{l in Omega_m} u_l(zhat') gamma_l,   kappa' = A' + theta' Phi_P^2 + (1/theta') sum_{Q \ Omega} nu'^2 Phi^2   (Lemma 1.3),
     so ONE scalar per block (kappa) enters, not the two scalars (theta, A) of V2's gap (C*-3); kappa is tuned by one push of a buffer peak
     with derivative 1 - X >= 3/4 (Lemmas 1.4, 1.5).  Numerically verified to 1e-15 (identities) and 1e-32 (derivatives, 60 digits).
 (2) (C*-3), (C*-4) (part 2).  Data shifts are bounded (Lemma 2.1); scales are sorted into finitely many ACTIVITY CLASSES (2.3); inside a
     class the data are projected onto the shifted exact cone Gamma^# (Hoffman via V2 Lemma H) and NORMALIZED to one common shift ray by
     increments added to the minus side only (Proposition 2.2: the represented functional is untouched, sqrt(Gamma) grows by O(epsilon));
     the cone is exactified by V2's Lojasiewicz Lemma L in the variables (u_Omega, kappa) and realized by V1's Lemma TU plus one kappa-push
     per block (Theorem 2.3); averaging over a SUBSET of the scales of a window is allowed (Lemma 2.4).
 (3) (C*-1) (part 3).  The design D^{U1} adds ZERO-VALUE ABSORBERS: biased pairs of block-1 carriers whose targets carry fresh binary
     tuning coordinates, placed in a cluster right after every main stage and as deep pairs before any main target can reach a signature
     coordinate (rule (c'')).  The first two carriers meeting any coarse coordinate after the main stage form such a pair (Lemma 3.2); tuned
     to value EXACTLY zero (Lemma 3.3) they carry no d-effect and no kappa-effect, and their switching coefficients cancel the fine residue at
     every coarse coordinate exactly (Proposition 3.4).  D^{U1} is admissible, N-free, and every refereed tool survives (Theorem 3.1).
 (4) (C*-2), (C*-5) for ONE-SIGNED classes (part 4).  Moves are ordered so that nothing feeds back: coarse realization, absorber tuning,
     re-push, then the fine structure on J_fine.  Configuration (i) (all active shifts negative): an ownership recursion makes every fine
     carrier of an active block a robust SELF-ALIGNED peak (Lemma 4.1); the first carrier with a nonzero coefficient dominates V at each
     coordinate (Lemma 4.2, using the weight rule (W4''), numerically necessary); hence V is admissible for every shift vector of the class
     and (SC) holds at the companion with any sequence (Lemma 4.3).  Configuration (ii) (all positive): Schauder-Tychonoff completion
     (Lemma 4.4, V2 Lemma C5).  Reference versus true shifts are reconciled exactly (Lemma 4.6); costs are o(T_lo^2) (Lemma 4.5).
 (5) Mixed classes (part 5).  Exactness holds in EVERY class (Lemma 5.1); only (SC) for the negative blocks can fail.  At any exact
     completion a negative fine carrier is in one of three states (Z') small value, (R) self-aligned robust peak, (W) wrong branch (Lemma
     5.2), and (SC) holds unless some (W) carrier has its value in a threshold band of width ~Phi^{1/2} (Lemma 5.3).  The forward recursion
     survives mixing unless a positive carrier is FRUSTRATED (|Y| < own mass) (Lemma 5.4); frustration forces zero cascades that can force
     (W) (toy model, 5.5).

MASTER THEOREM IV (5.6).  PROVED.  D^{U1}, N fixed, F finite.  If for infinitely many main stages L some clean sub-window w of L has at
least n(w)/D_cls(w) scales in ONE-SIGNED activity classes, then f in Rec(p_N).
 Corollary IV.1.  For N = 1 every class is one-signed: EVERY f with finite F is in Rec(p_1) (finite-F Lemma Z for p_1).
 Corollary IV.4 (intrinsic).  If for infinitely many main stages some clean sub-window has I_up(w) = {} or I_lo(w) = {}, then f in Rec(p_N).
 Corollary IV.2.  A finite-F counterexample for p_N (N >= 2) must have, at every large main stage and every clean sub-window, both
 source deficiencies (I_up, I_lo nonempty) actively shifted at all but a 1/D_cls fraction of the scales, with frustrated positive carriers.

THE PRECISE REMAINING STEP (C_mix) (5.7).  OPEN.  In a mixed class, find an exact completion (exists, Lemma 5.1) at which no negative fine
carrier has its value in its threshold band B_l = (thr_l (1 - Phi_l^{1/2}/M), thr_l + Phi_l^{1/2}).  Bad carriers need the coincidence
own_l - |Y_l| in B_l (measure ~Phi_l^{1/2}); toy data: forced wrong branches occur (3/115), bad ones only with artificially thick bands.
(C_mix) follows from U3's open uniformity step (S2) (violation tolerance), SKETCH of the reduction in 5.7(c).
Not claimed: transfer to Martin's p (the one-signed hypothesis is not N-independent); infinite F (U2's items).

Corrections recorded (5.8): V2's near-coordinate conversion is FALSE as stated (Cantor-set obstruction); V2's two-scalar exactification
is unnecessary (kappa-reduction); this round's part 4 needed c_0(a) > 0 on unused tuned absorbers; a first numerical toy violated (W4'').

## Results table
| # | Result | Status | Where |
|---|---|---|---|
| 1 | Lemma 1.1 exactness certificate V(Domega) | PROVED | 1.1 |
| 2 | Lemma 1.2 threshold identities (E1), (E2) | PROVED (+ numerics) | 1.2 |
| 3 | Lemma 1.3 data identity, kappa-reduction | PROVED (+ numerics) | 1.3 |
| 4 | Lemma 1.4 derivatives of kappa | PROVED (+ 60-digit numerics) | 1.4 |
| 5 | Lemma 1.5 kappa tunable by one buffer-peak push (final form) | PROVED | 1.5 |
| 6 | Lemma 2.1 shift bound | PROVED (+ numerics) | 2.2 |
| 7 | Activity classes | PROVED | 2.3 |
| 8 | Proposition 2.2 projection and normalization to one ray (C*-4) | PROVED (modulo V1 TR, refereed) | 2.4 |
| 9 | Theorem 2.3 exactification with one scalar per block (C*-3) | PROVED | 2.5 |
| 10 | Lemma 2.4 subset averaging | PROVED | 2.6 |
| 11 | Theorem 3.1 D^{U1} admissible, N-free, tools survive | PROVED | 3.2 |
| 12 | Lemma 3.2 first touchers are absorber pairs | PROVED | 3.3 |
| 13 | Lemma 3.3 zero-value tuning, biased pairs | PROVED | 3.4 |
| 14 | Proposition 3.4 exact absorption on coarse coordinates (C*-1) | PROVED | 3.5 |
| 15 | Lemma 4.1 robust self-aligned recursion (configuration (i)) | PROVED (+ numerics) | 4.2 |
| 16 | Lemma 4.2 owner dominance under (W4'') | PROVED (+ numerics) | 4.3 |
| 17 | Lemma 4.3 (SC) at the companion, configuration (i) (C*-2) | PROVED | 4.4 |
| 18 | Lemma 4.4 Schauder completion, configuration (ii) | PROVED | 4.5 |
| 19 | Lemma 4.5 cost and statuses | PROVED | 4.6 |
| 20 | Lemma 4.6 reference versus true shift; move order (C*-5) | PROVED | 4.1, 4.7 |
| 21 | Lemma 5.1 exactness in mixed classes | PROVED | 5.1 |
| 22 | Lemma 5.2 three states of a negative carrier | PROVED | 5.2 |
| 23 | Lemma 5.3 (SC) criterion tolerating wrong branches | PROVED | 5.3 |
| 24 | Lemma 5.4 mixed recursion without frustration | PROVED | 5.4 |
| 25 | Toy evidence on mixed classes | HEURISTIC | 5.5 |
| 26 | MASTER THEOREM IV (one-signed classes) | PROVED | 5.6 |
| 27 | Corollary IV.1 (N = 1: all finite-F rows recovered) | PROVED | 5.6 |
| 28 | Corollary IV.2 (shape of a counterexample) | PROVED | 5.6 |
| 29 | Corollary IV.3 (mixed without frustration) | PROVED | 5.6 |
| 30 | Corollary IV.4 (intrinsic: one source type deficient) | PROVED (modulo V1 Lemma 3.4', refereed) | 5.6 |
| 31 | (C_mix): mixed classes, (SC) at an exact completion | OPEN | 5.7 |
| 32 | (C_mix) follows from U3's (S2) | SKETCH | 5.7(c) |
| 33 | V2's near-coordinate conversion | FALSE as stated | 5.8 |

## Numerics (r8/U1_work/)
 kappa_check.py (+ kappa_lib.py): 307 random blocks; (E1) 8.5e-16, (E2) 7.8e-16, two forms of kappa 3.1e-16, identity (1.3) 3.0e-15,
   duality 2.2e-16 (finite-difference derivative checks 3e-4 / 2e-2 are step-size noise, superseded by kappa_check2).
 kappa_check2.py (mpmath, 60 digits, central differences h = 1e-30): Lemma 1.4 (a), (b), (c) on 211 / 127 / 117 tests, max relative
   errors 2.1e-32, 6.5e-33, 6.4e-33.
 shift_bound_check.py: Lemma 2.1 on 5220 tests, max d^2/bound = 1.0000000000000007 (rounding), equality attained at x = w 1_Omega;
   min (1 - chi)/(M^2 Phi_P^2/C^2) = 0.9999999999999992 (>= 1 up to rounding; equality when Omega = Q).
 recursion_check.py (first toy; later targets ignore (W4'')): admissibility FAILS — the toy, not the lemma, was wrong.
 recursion_check2.py: with (W4'') enforced, 200 instances x 50 shift vectors: all carriers robust self-aligned peaks, V z-signed at every
   coordinate; with (W4'') violated, 27% of the instances fail.
 mixed_fixedpoint_check.py, mixed_forcedW_check.py, mixed_bad_inspect.py: lexicographic model of mixed classes (5.5).
