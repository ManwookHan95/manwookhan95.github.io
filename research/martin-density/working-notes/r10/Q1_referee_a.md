# Referee report (a) on Q1 (Round 10): one design T_fin, finite-support Lemma Z for every N, density <=> (LSC-trunc)

Refereed: r10/Q1_notes.md (assembled; Q1_part0..3 and Q1_notes_a/b/c are drafts/sections of the same text) and r10/Q1_work/ (pm_check2.py,
pm_check3.py, pm_check3_50.py, s2c_check.py and their outputs).  Checked against the refereed sources it cites: r9 X1_referee/X1_ref_notes,
X2_referee/X2_ref_notes, X1_notes 2.1-2.6, X2_notes 1.4, 2.1-2.3, 3.1-3.6, 4.1-4.2; r8 U1_ref_notes 3-8, U1_notes 2.1-2.6, 3.1-3.5, 4.1;
r7 V1_notes 4.1 (Proposition TR); paper/martin_density_note.tex (def:admissible, lem:martintail, prop:smooth, prop:approximants,
prop:reduction, lem:pair).  My part files: r10/Q1_refa_part1..4.md; proofs of all fixes: r10/Q1_refa_notes.md; script:
r10/Q1_refa_work/pm_ref.py, pm_ref_flip.py, pm_ref_flip2.py (outputs pm_ref.out, pm_ref_flip_part1.out, pm_ref_flip2.out; summary
pm_ref_summary.txt).  Role: adversarial referee (a), focus on the combination logic.

## 0. Bottom line
The combination is correct.  I re-derived every new step of Q1 (design recursion, admissibility, genericity, the route-V companion with
KN^tr, the base-row hypotheses of Theorem UE, the Puiseux margin against the levers, the late threshold, the averaging, the density
criterion) and found no error that invalidates a PROVED claim.  The gaps are precisions; one (P8, window bookkeeping) requires a one-line
amendment of T_fin or of the counting argument, which I supply.  With P1-P8 (proofs in Q1_refa_notes.md):
 * MASTER THEOREM VI is PROVED modulo the cited refereed results: for T_fin under option (a) (||T_fin|| = c_1 < 1, a Martin-type norm) and
   EVERY N, every f in S_{p_N^*} with finite base support is in Rec(p_N); under option (b) (T_fin admissible, norm one) for N = 1, and for
   N >= 2 at rows with rho_1(f) != 1.
 * THEOREM VI.2 is PROVED: for every N, NA((c_0, p_N), l_2^2) is dense iff (LSC-trunc)_N; Corollary VI.3 (Martin's p from (LSC-trunc)_N for
   infinitely many N) is PROVED.
 * Lemma Z at infinite base support ((LSC-trunc)), hence density for p_N and for p: OPEN.  No counterexample is claimed; nothing I checked
   points to one.
Caveat on robustness: several links of the chain have had a single referee pass (U1-ref's MT IV' assembly and Proposition KN; X1-ref's
KN-1, S-0, K1, W-fixes; X2-ref's (R-abs), Lemma CM', Theorem C_mix').  Q1 says so correctly.

## 1. Verdicts
| Claim (Q1 label) | Verdict | Main point / fix |
|---|---|---|
| T_fin, Lemma W_fin (PROVED) | correct with fixable gaps | order of stage l re-checked (lb_l -> R -> y_l -> delta_l -> c_l -> rate/QC data -> sub-windows); c^low <= c^max at PRE stages; P7: patterns must range over the blocks of stages <= l, and l_f must exceed the stage after which every block <= N has a coarse carrier; P8: Q(w) exponent (section 2) |
| Theorem A_fin (PROVED) | correct | (T-b)/(T-c): |sum_{l >= L(s)} x_l c_l y_l(s)/n_l| <= (8/9)||x||_inf 2^{-2s} c_{l'} delta_{l'} using (W4) at EVERY target meeting s (PRE, MAIN, CLUSTER); (T-d) re-derived; the equality clause of (T-a) appears in the note only in def:admissible and admissibility checks (grep: lines 144-154, 2344, 3990) |
| Lemma GEN_fin (PROVED) | correct | delta(y, l) in Q(y); n(y, l) put into k_0; absorber targets in A_pool whatever R is; only the weights of N_T need genericity (peak weights, (KN)-block weights lie in k) |
| Survival audit I1-I10 (PROVED) | correct | route V uses no lower bound on a weight except design-computed ones (lambda >= 1/D, Phi_min >= 1/D); cluster bound c_{L+i} >= c^cl 4^{1-i}/2 re-derived; absorber items matter for route X only |
| Route decision (PROVED) | correct | route V needs from the coarse system only statuses, kind-[3] rows, exactness of Gamma^#; KN^tr gives all three and is sign-agnostic per block (floor row: Lemma F for Delta' < 0, small inactive mass for Delta' > 0), hence serves mixed classes; route X is not on the tree of MT VI |
| Lemma CM^tr (PROVED) | correct with fixable gaps | P2: order must be class -> Step A -> cube -> Step B (Step B is built for the ray Delta'^*, the cube corner); P1: D2-pushed inactive carriers are kind [1'] (accepted by UE); S-0 drift C Design c_{L+1} <= (C T^4/L) mu/8 re-derived; held values end at <= 4 c_{L+1}^2, harmless (effect O(D^2 c^4) << mu) |
| Proposition BR (PROVED) | correct with fixable gaps | P3: (U3) on Step-A supports holds only up to the fine residue V_fine; it is a tolerated violation (excess at a support coordinate <= 2(z x)_-, as at a contact), counted in eps; P4: Step A uses a bounded number (not "two") of S_l coordinates; window constants K, D_cls, A_max are NOT design x u^{-C} with absolute exponents (P8) |
| Lemma PM (PROVED) | correct | clamp equation 1 = sum min(Phi_k (1-C)/C, v_k)^2 re-derived; |C' - C| <= C_f c_{L+1} independent of the perturbation size; rho'/rho = [C'/(1-C')]/[C/(1-C)] exact; P5: (iv) should say coarse PEAKS meet no lever coordinate (second-order only), Omega values move but end exactly at nv^# |
| Lemma S2c^tr (PROVED) | correct | eta'/3 >= T^5, mu >= T^{5 Design + 1}, g_min >= 2^{-6 log2^2(1/T)}; r_0 linear in g_min, other lever constants Design^C; K_w <= exp(C log^2(1/T)); s_1 = max(64 rho eps/delta, e^{-1/(2T)}) <= s_late |
| Theorem C^tr (PROVED) | correct with fixable gaps | P6: Theorem E^eng is stated "with FIXED gamma_B" but is used with gamma_B(w) -> 0; its proof uses gamma_B only via c_flat(j), tracked in (E-d) — fine, statement must say so; P8 for (E-d) |
| MASTER THEOREM VI (PROVED) | correct with fixable gaps | inherits P2, P8; quantifier order verified; (b2): |rho_1(f) - 1| > b(w) for L >= L_1 so carrier 1 is robust at clean w, not in N_T |
| Theorem VI.2, Cor. VI.3 (PROVED) | correct | (i) => (ii) holds for every T (lem:pair, prop:smooth(c)); (ii) => (i) via MT VI; lem:martintail uses only |R_m x|_m <= m 2^{-m} q(x) |

## 2. Main findings
F1 (the combination holds; PM is the heart).  In route V nothing about the ratios r = u/kappa is needed at the approximant: for a coarse
   strict non-peak, rho_k = |nv_k| C_m/(Phi_k^2 (1 - C_m)); d-consistency freezes nv_k on ALL coarse strict non-peaks exactly; coarse peaks enter
   the clamp equation only through Phi_k (they stay clamped); so C_m moves only through the fine carriers, by <= C_f c_{L+1}.  Hence the only
   comparison the Puiseux margin mu = mu_kappa(eta'/3) must win is mu >> C_f c_{L+1}, which (W2) + (D2) (c_{L+1} <= b^2 <= mu^2/64) and (W_exp)
   give with room.  The lever size r never meets mu on Omega; it meets g_min only through Lemma DC's status radius r_0 ~ g_min/C_lev and the
   theta-regime radius s_1 <= T gap_min/(4 rho A_2), both contained in (LATE).  Re-derived; independent numerics (section 4).
F2 (KN^tr in route V).  The three things route V takes from the coarse system (statuses; kind [3] of near-threshold Omega carriers with the
   TRUE shift; exactness of Gamma^#(kappa, a)) are exactly KN^tr's conclusions (a), (b) and the floor row (X4^0).  KN^tr never uses the signs
   of other blocks, so mixed classes are covered.  In active negative blocks inactive near-threshold carriers cannot exist (U1-ref 4.1
   exclusions), so the kinds of all inactive Omega carriers are as in X2-ref's assembly (P1).  KN-1 needs "<< mu", and the exact hold inside
   Step A is what protects against the Design^2 eta'^2 cross effects; the later G1 release (4 c_{L+1}^2) is harmless.
F3 (P8: exponents are not absolute).  The class thresholds A_{i+1} = K_* A_i (U1 2.3) make the data constant K_data <= J K_*^{J+1} K with
   J = |Omega| + N <= L + N, and the cube count (A_max/eps)^p carries the number p of extreme rays.  Q1's "D_cls <= C_{f,N}(Design/u)^{C_D},
   K = C_f(Design/u)^{C_K}, C_U1 = 2C_D + C_K + 1 absolute" is therefore unjustified (inherited from U1/U1-ref).  Fix: (a) pigeonhole first
   over the support (size <= N, Caratheodory) of the basic representation, then over cubes, so D_cls <= C_{f,N} 3^{2L} (p_max+1)^N
   (Design/u)^{2CN}; (b) put p_max(L) into Design(L) and use Q(w) := (4 Design/u)^{omega(l) + l^2 + 20} (or prove omega(l) >= 2^l).  Then
   (E-d) holds for L >= l_f(f, N).  Q only grows, so Lemma GW keeps all window conditions.  Proof: Q1_refa_notes 2.7.
F4 (P3: (U3) with residue).  X2-ref's C_mix' proof and Q1's Proposition BR cite V1 TR(iv) for (U3) at the supports created in step (1a), but
   V1 TR(iv) concerns exact data; in route V the data there are contact-like only up to +-V_fine/2.  Harmless: at a support coordinate the
   base excess of a'_j + x_j is <= 2(z_j x_j)_- (same as a contact), so the residue is a tolerated violation (cost <= 2 rho|tau||V_fine(j)|),
   to be counted in eps of (U4); b^theta = (chi - 1/2)V_proj is residue-free.
F5 (P2, P4, P5, P6, P7).  Order of the companion; bounded number of Step-A coordinates on S_l and choice of Lemma DC's pull coordinates in
   a v-window of ratio 2^{6G(L)} inside S_l ∩ (s_max, s_far]; phrasing of PM(iv); E^eng with window-dependent gamma_B; patterns over the
   blocks of stages <= l.  All proved in Q1_refa_notes.

## 3. Attacks attempted
Uniformity in t (kind [3] needs no gap lower bound in c_flat; theta regime radius in (LATE)); in the window (exponents of K, D_cls — FOUND P8);
number of carriers (|Omega| <= L, J <= L + N, patterns finite, omega(l) >= 2^l); along companions and approximants (Lemma M2 ball; clamp
equation); simultaneous levers (Lemma DC pulls vs Step-A pulls/banks vs KN-1 holds — FOUND P4, harmless); KN-1 vs G1 release (harmless);
signs (negative-block exclusions; floor row for both signs of Delta'); Hoffman/minor constants (Design^C, J-dependence absorbed); design
well-foundedness (QC data after c_l; b_X1 after Design; (W_exp) after T_lo(p, M(p))); N-independence (FOUND P7, presentational); genericity
(only N_T; option (b) slice); admissibility ((T-a) equality unused); quantifier order (verified, Q1_refa_notes 2.9); counterexample search
(none: every defect found is bookkeeping).

## 4. Numerics (sanity; r10/Q1_refa_work/pm_ref.py, independent block solver)
Inner problem for fixed M = ||w||_inf in closed form, outer concave maximization by bisection on A'(M) (envelope theorem), 64-90 digits
(a different algorithm from Q1's bisection on theta).  Identity t = C/A of lem:threshold: <= 1.9e-61.  Worst cases for PM: coarse peaks moved
by a relative r in {1e-3, 1e-2}, FINE values replaced by arbitrary values of size <= 2 lambda_k (pm_ref.out, 4 instances) or half of them placed
near THEIR thresholds and moved across (pm_ref_flip_part1.out + pm_ref_flip2.out, 6 instances, 0-5 fine status flips), mu in {1e-6, 1e-9,
1e-12}, fine weight W in {1e-14, 1e-20, 1e-26}; d-consistency on all of Omega by a fixed point.  Results (pm_ref_summary.txt): 1 - rho_d = mu
EXACTLY in all 10 instances; rho'/rho = [C'/(1-C')]/[C/(1-C)] to <= 1.1e-54; |C' - C| <= 3e-56 when the fine carriers stay clamped (C exactly
frozen) and <= 4.0e-31, each value below W^2, with flips — i.e. the SHARPER bound |C' - C| <= C_f sum_fine Phi_k^2 <= C_f c_{L+1}^2 (each fine
clamp term moves by at most Phi_k^2((1-c)/c)^2), well inside Q1's C_f c_{L+1}.  CONTROL (one Omega carrier untuned): |C' - C| = 1e-7 ... 6e-5
and d becomes a peak in 6 of 10 instances (otherwise rho_d moves by 7.6e-6 ... 1.4e-4 >> mu).  Q1's pm_check3 (80 digits, 12 instances) and
s2c_check (log-scale arithmetic) were re-read: outputs consistent with the claims.

## 5. Single most valuable idea
At a d-consistent engineered approximant the switching statuses are functions of frozen normalized values and ONE block scalar C_m, the root
of the clamp equation sum_k min(Phi_k (1 - C)/C, v_k)^2 = 1, which only the fine carriers can move.  This decouples the non-explicit Puiseux
margin of the generic-weight design (X1) from every engineering perturbation of the violation-tolerant route (X2): the margin only has to
beat the fine weight c_{L+1}, and the Puiseux exponent costs only exp(O(log^2(1/T))) in window constants, which the super-exponential weight
decay (W_exp) absorbs.

## 6. What remains open
(1) (LSC-trunc)_N (infinite base support) — by Theorem VI.2 EQUIVALENT to density of NA((c_0, p_N), l_2^2) for the Martin-type norm built
    with T_fin; density for Martin's p follows from (LSC-trunc)_N for infinitely many N.  (2) Option (b) (norm one, inside def:admissible), N >= 2,
    rows with rho_1(f) = 1 (slice coincidence for the rational weight).  (3) Martin's own operators (arbitrary admissible T).  (4) A second
    pass on the single-pass links (U1-ref MT IV', X1-ref KN-1/S-0, X2-ref (R-abs)).
Density of NA((c_0, p_N), l_2^2) (any N) and of NA((c_0, p), l_2^2): OPEN.
