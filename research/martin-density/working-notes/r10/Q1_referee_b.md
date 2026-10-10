# Referee report (b) on Q1 (Round 10): one design T_fin, finite-support Lemma Z for every N

Refereed: r10/Q1_notes.md (with Q1_notes_a/b/c, Q1_part0..3) and r10/Q1_work/ (pm_check2/3, s2c_check outputs read).  Checked against: U4 1.2-2.2
(T_final), U1 3.1-3.4 (D^{U1}, absorbers, Lemma 3.3), U1-ref 5-8, X1 1.1-3.1 with X1-ref 6-9, X2 2.3 with X2-ref 3-4, and the note (def:admissible,
lem:threshold, lem:martintail, lem:pair; lines 120-260, 562-600).  Assigned focus: the design (well-foundedness with generic transcendental weights;
Martin's Lemma B; N-independence; every weight bound, (W_exp), (D-lev), cluster/absorber weights) and whether ANY F-finite first row escapes the
case analysis.  My working files: r10/Q1_refb_part1..3.md; proofs: r10/Q1_refb_notes.md; scripts/outputs: r10/Q1_refb_work/ (design_checks,
clamp_check, clamp_check2, alpha_mass).

## 0. Bottom line
The design part of Q1 is correct.  T_fin is one well-founded, N-independent recursion; every quantity of a stage depends only on earlier data;
the generic choice of c_l happens BEFORE the level-l QC data are computed, which is exactly what makes those data positive (non-coincidence).
Theorem A_fin (Martin's Lemma B: injectivity, Y ∩ c_00 = {0}, per-block density, ||T|| = c_1) and Lemma GEN_fin are correct.  I re-derived each
item.  The key point for "weights chosen before f" also holds: the coincidence sets B_kappa contain no continuous datum of f.  f only selects the
pattern and the point r(f), and every coefficient of every cone row and floor function lies in k_0(weights outside N_T).  All upper bounds on the
weights are verified literally, because c^max_l is computed from the actual earlier weights.  Every lower-bound use survives within a fixed
factor; one use is not on Q1's list (P-R), and it survives too.  (W_exp), (D-lev) and the cluster and absorber weights are compatible.  Lemma PM
(the clamp equation freezes C_m once all coarse strict non-peaks are tuned exactly) is correct and is the clean core of the combination.  My
independent 80-digit solver confirms it, including the control.  Lemma S2c^tr's arithmetic is right.  Theorem VI.2 and Corollary VI.3 follow
formally.  Escape search: no F-finite row escapes the case analysis under option (a).  The option-(b) exception (rho_1(f) = 1, N >= 2) is
genuine and correctly labelled OPEN.  I found no error that invalidates a PROVED claim.  I found four fixable precisions (P-LIP, P-R, P-HOLD,
wording), all fixed in Q1_refb_notes.md.  The proof of Master Theorem VI remains "modulo" the single-pass-refereed assemblies (U1-ref,
X1-ref, X2-ref) and the reduction claim of Lemma CM^tr, which referee (a) audits line by line.  Density of NA((c_0, p_N), l_2^2) and
NA((c_0, p), l_2^2) is reduced to (LSC-trunc), which is OPEN.  No counterexample is claimed, and nothing I checked points to one.

## 1. Verdicts
| Claim | Verdict | Main point |
|---|---|---|
| T_fin, Lemma W_fin | correct with fixable gaps | order of a stage re-derived; (W7) target-independent (so lb_l <= c_l); k(l + R_cl(l)) known at stage l; (GM) max exists and is in Q(y); bands nonempty and disjoint; P-LIP: the Lipschitz constant in delta_0, (D1) must dominate Lip_kappa of F_Phi |
| Theorem A_fin | correct | (T-b), (T-c) via (W4) + allowedness (a) for every target incl. absorbers; (T-d) once l_r >= max supp y + 2|supp y|; round 1 forces stage 1 = main stage in block 2; n_l in [3/4, 5/4] |
| Lemma GEN_fin | correct | k_0 fixed before weights; contains u_l(j) for ALL j and all aggregated coefficients; B_kappa has no f-datum |
| Survival audit I1-I10 | correct with fixable gaps | complete upper-bound list verified; P-R: U1-ref 7 also uses an UPPER bound on R (least absorber entry), constant 64 -> 2^13, survives; (W3) at clusters p+i, i >= 2, implied (arithmetic re-done) |
| Route decision | correct | one companion per (L, w, class); absorbers of the current cluster are fine carriers, those of earlier rounds coarse SLD carriers |
| Lemma CM^tr | correct with fixable gaps | arithmetic of (b) re-done; P-HOLD: hold ALL nearly-neutral coarse carriers of (T)-blocks (= inactive Omega with Omega = all coarse strict non-peaks); reduction (i)-(iii) spot-checked only (referee (a)) |
| Proposition BR | correct | lever coordinate j(l) (second element beyond s_max) is free: Step A's pulls sit far beyond sigma_2(L), at most the first element is a bank; W_lev by definition of s_max; KN-1 hold supports satisfy (U3) |
| Lemma PM | correct | clamp equation re-derived; alpha-mass identity gives the natural peak; numerics: frozen to 6e-73, control moves rho_d by 5e-7..5e-6 >> mu |
| Lemma S2c^tr | correct | g_min >= T^{5 Design + 2}, (W_exp) dominates even exp(C ln^3(1/T)) |
| Theorem C^tr | correct (modulo refereed tools) | (E-c)-(E-f) arithmetic re-done |
| Master Theorem VI | correct (modulo refereed tools and CM^tr's reduction) | case analysis exhaustive (Section 3); option (b) N >= 2 exception exact |
| Theorem VI.2, Corollary VI.3 | correct | formal; lem:pair and lem:martintail read in the note |

## 2. Findings
F1 (genericity is legitimate).  The only way a generic-weight argument fails is if the bad set depends on the row.  Re-reading X1 2.2(iv)/2.3:
   B_kappa is built from u_l|E_c, peak vectors and peak weights, sigma_rob (pattern's robust peaks), signs and labels, (KN)-block weights and the
   ratio variables.  The weight-dependent range E_c(w) (up to s_far(w)) is harmless because k_0 contains u_l(j) for every j and every aggregated
   coefficient.  Formula-1 kappa puts the active weak peaks into Omega, so tau_m has no N_T-weight.  PROVED.
F2 (alpha-mass identity, new).  sum_{k in P}(rho_k - 1) Phi_k^2 = C/M in every block (from ||alpha||_1 = 1 and |nv_k| = |alpha_k| + Phi_k^2 M/C).  It gives
   at once the natural peak needed for Lemma PM's slope and a two-line proof of V1 Lemma D: robust coarse peaks carry >= C/M - b - C_f c_{L+1} > 0.
   Hence sigma_rob > 0.  Together with 1 - R^2 = sigma(1 + 2a + sigma)/(a + sigma)^2 >= sigma (a + sigma < 0.38), r(f) is interior to K_kappa.  PROVED
   (numerics 6.5e-51 and margin 0.445).
F3 (P-LIP).  KN^tr Step 1 needs Lip(F_Phi) = Lip_kappa (it contains 1/Phi_d) in delta_0(b) and (D1).  Q1's (S6) uses Lip(l) of the minors.  Fix:
   Lip^*(l) := max(Lip(l), max_kappa Lip_kappa), already a factor of Design(l).
F4 (P-R).  I3 says the sweep bound is the only use of R.  U1-ref 7 also needs the least absorber entry eta_k >= c mu_{p_0}^2 c_k^2, i.e. R not too
   large.  With R from lb_l >= c_l/8 one gets eta_k >= mu^2 c^2/2^{13}; U1-ref 7's sixth-power slack absorbs it.
F5 (P-HOLD).  The non-explicit Puiseux margin survives only because rho_d = m|r_d|K(sigma, R^2)/Phi_d involves no second-order VALUE perturbation of
   peaks (sigma depends on the peak SET).  The only other term, the inactive part of R^2, must be held EXACTLY.  By (T) that part is exactly the
   nearly-neutral coarse carriers of the block; all of them must be held.  This is Q1's statement when Omega = all coarse strict non-peaks.
F6 (wording).  (W5), (W7) are imposed at PRE stages and at p+1, contrary to 1.7's "(F10) only partly".  W_lev holds by definition of s_max(L) =
   max T(L) (Q1 cites (c)).  "C_U1 absolute" should read "eventually dominated by (4 Design/u)^{omega+20}" if the cube exponent depends on N.  All harmless.
F7 (no rescaling shortcut for option (b)).  T_fin(a)/c_1 has norm one, but the norm is not homogeneous in the weights: B_{|.|_m} = B_{l_1} + D_m B_{l_2}.
   So B_kappa is not a cone and nothing transfers from (a) to (b).  The residual (O2) is genuine.

## 3. Escape search (assigned): can an F-finite first row avoid the case analysis?
I tried each structural route by which a row could escape:
 * f-constants infinite: excluded (R_m**xi != 0 by density, unique w_m, M, C > 0, ||alpha||_1 = 1).
 * No clean sub-window: excluded (omega(L) objects, omega(L)+1 nonempty disjoint bands).
 * Circularity between objects and statuses: excluded (objects for every pattern).
 * A block of no kind: excluded (inactive coarse rho in [0,b] ∪ [u,1+b] ∪ [1+u,inf)).
 * sigma_rob = 0, or r(f) outside K_kappa: excluded by F2.
 * Y_1 empty at f's pattern: excluded (F(r') <= 1 + m_0/2).
 * Sign flips of r_d: excluded (|r_d| >= 1/Design^2 >> eta').
 * Second-order cross effects beating the Puiseux margin: excluded under P-HOLD.
 * Fine near-threshold carriers: tolerated violations, C moves by <= C sum_fine Phi^2.
 * Dominant class trivial, or f in NA: covered.
The only surviving candidates are option-(b) rows with rho_1(f) = 1 exactly, stage 1 active near-threshold in a (T)-block, with 2^{-3} a critical
value of psi_1 on a stratum of Z_kappa (a property of the design that no argument excludes).  Under option (a) no row escapes.

## 4. Attacks attempted
 * Well-foundedness: forward references (k(l + R_cl), s_far(w) in E_c, (W_exp) at p+1) all resolved.
 * Genericity: "weights before f" with f-dependent bad sets — refuted (F1).
 * Option (a)-to-(b) transfer by rescaling — refuted (F7).
 * Upper bounds: all of (W1)-(W7), (W4'') in cluster form, (W_exp), (D3), W_pull, W_lev.
 * Lower bounds: the complete list plus P-R.
 * Lever coordinates: Step A cannot occupy the second element of S_l beyond s_max (pull sizes << v_l(second element)).
 * Lemma PM: what if a coarse non-peak is left untuned (control: margin destroyed) or if fine carriers change status (bounded by sum Phi_fine^2).
 * Slack in S2c^tr: tested against design-dependent exponents (still fine).
 * N-dependence: patterns of p_N are enumerated patterns; N-dependent exponents absorbed by omega(l) -> infinity.
 * Martin's Lemma B: the injectivity estimate with absorbers.

## 5. Numerics (sanity checks; r10/Q1_refb_work/)
design_checks.py/.out: (GM) on 60 rational targets (max exists, rational; excluded length 1/8 of delta^max); 1 - R^2 identity (7e-51); cluster
capacity worst ratio 0.77 >= 1/2; absorber least entry >= mu^2 c^2 2^{-12.55}.  alpha_mass.py/.out: alpha-mass identity on 300 random blocks
(6.5e-51), min (1 - R^2) - sigma = 0.445.  clamp_check.py/.out, clamp_check2.py/.out: an independent 80-digit block solver (cvxpy cross-check of
the block norm to 2e-10) over 10 instances with mu down to 1e-16.  With all coarse strict non-peaks frozen, |C' - C| <= 6e-73 and rho_d is unchanged
to all digits.  Control (one robust non-peak untuned): |C' - C| ~ 1e-7 and rho_d moves by 5e-7..5e-6 >> mu.

## 6. Single most valuable idea
The generic-weight threshold protection has a margin of non-explicit size.  It is usable because it never has to beat a perturbation.
 * The bad sets B_kappa contain no datum of f, so transcendental weights fixed in advance avoid them for every row.
 * At the engineered approximant, freezing the normalized values of ALL coarse strict non-peaks (d-consistency) and keeping the coarse peaks
   clamped fixes C_m through the clamp equation sum_k min(Phi_k(1-c)/c, v_k)^2 = 1, hence every relative position.
 * The only residual is the fine mass c_{L+1} <= b^2 <= mu^2/64.
 * The non-explicit Puiseux exponent costs only polylog factors in the window constants, which (W_exp) absorbs.
(My complement: the alpha-mass identity sum_P (rho - 1) Phi^2 = C/M, which supplies the clamp slope and sigma_rob > 0 in one line.)

## 7. What remains open
 (1) (LSC-trunc)_N (infinite base support), equivalently (Theorem VI.2) density of NA((c_0, p_N), l_2^2) for T_fin.  Density for Martin-type p
     needs it for infinitely many N (Corollary VI.3).  Its sub-items are M-inf transport, tuning regularity modulus, (W_inf), (SC) along deep raises,
     and status coherence at infinite F.
 (2) Option (b) (norm-one T in the note's class), N >= 2: rows with rho_1(f) = 1, i.e. whether 2^{-3} can be a critical value of psi_1 on a stratum of
     Z_kappa identically in the generic parameters.
 (3) Martin's own operators (arbitrary admissible T): nothing here applies.
 (4) Certification: Master Theorem VI rests on single-pass-refereed assemblies (U1-ref MT IV' tools, X1-ref KN^tr, X2-ref CM'/C_mix') and on this
     round's reduction claim in Lemma CM^tr (X2-ref CM' uses Proposition KN only through statuses, kind-[3] rows and exactness).  Referee (a)'s
     line-by-line check of that claim is the remaining verification.
Density of NA((c_0, p_N), l_2^2) (every N) and of NA((c_0, p), l_2^2): OPEN.
