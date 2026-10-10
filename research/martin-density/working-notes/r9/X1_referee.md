# Referee report on X1 (Round 9): kappa-neutral levers, status coherence without (KN), exact coupling (S1), RT*(c)

Refereed: r9/X1_notes.md (the assembled version; the part files X1_part1..4.md are earlier drafts of the same material and differ only in
wording and in the order of 2.5-2.7), r9/X1_work/{lemmaK_check.py, floor_check.py, sard_toy2.py} (sard_toy2 re-run: output identical),
against paper/martin_density_note.tex (def:admissible, rem:lemmaB, lem:threshold, lem:suplevel, eq:peakshift, def:twopiece) and the refereed
Rounds 5-8 (U1 Lemmas 1.1-1.5, 2.1-2.4, 3.x, 4.1-4.6 with U1-ref 1-8 (Lemma R-kt, Proposition KN, (X4), G1, D^{U1'}, Master Theorem IV');
U3-ref (S1), RT*(c); U4 T_final with U4-ref; V1 Prop. TR(iii), Lemmas TU, B, CO, ST; V2 Lemmas H, L, Theorem B; Y1 Prop. 5.2(iii)).
My part files: r9/X1_ref_part1..4.md; assembled proofs of all fixes: r9/X1_ref_notes.md; scripts r9/X1_ref_work/ (indep_block.py,
cvx_check2.py, floor_ref.py, weakpeak_ref.py, sard_toy2_rerun.out).

## 0. Bottom line
X1's central idea is correct and, to my mind, is the decisive new step for the finite-F residual: after rewriting U1-ref's inward row at the
FLOOR, (X4^0) "vs_l gamma_l + Delta'_m m^2 |r_l| K(sigma_rob, R_a^2) >= 0", the exact zero set Z of the tiny minors (ratio space) and the
floor functions psi_d(r) = m |r_d| K(sigma_rob, R_a^2) contain NO weight of the active near-threshold carriers d; these weights enter only
as denominators of the floor statuses psi_d/Phi_d.  Choosing all weights algebraically independent over the countable field of non-weight
design data (possible inside T_final's weight intervals), the semialgebraic Sard theorem shows that the threshold value 1 is never a
local-minimum value of max_d psi_d/Phi_d on any Z (Lemmas NLM, GEN), and compactness / Lojasiewicz / Puiseux turn this into status
coherence with design constants (Lemma QC, Proposition KN^tr).  This replaces U1-ref's hypothesis (KN) — which, as X1's Lemma F shows
rigorously, is a property of f (robust inactive k-mass) that no design-supplied lever can create.  I re-derived Lemma K, Lemma F, the
inward identity, NLM, GEN, QC and the chain of KN^tr, and checked the identities with an independent block solver (60 digits) cross-checked
against a direct convex computation of the dual norm.
I found no error that invalidates a PROVED claim, but several gaps that must be repaired (all fixed below, proofs in X1_ref_notes.md):
 (G1, KN-1) the (T)-block margin mu(eta'/3) ~ c (eta')^beta has a NON-EXPLICIT Puiseux exponent; inactive Omega carriers that are "pushed to
     0" once and then left alone are moved back by second-order cross effects (~ Design^2 eta'^2) whose effect on the statuses is NOT
     dominated by mu when beta > 4.  Fix: hold them at value exactly 0 inside the joint fixed point (as U1 does for absorbers).
 (G2, W-fix) the compact region K_kappa of Lemma NLM contains the N_T-weights (|r_l| <= 2 Phi_l/(m k_min)), so "Z independent of Phi" is
     literally false; harmless (drop these bounds; eps_K := sigma_rob/4 suffices, or note F >= 2 on that face).
 (G3, D2) inactive near-threshold carriers of UNSHIFTED blocks are not treated (must be pushed inward individually, U1-ref Prop. KN(b)).
 (G4, S-0) X1's weight bound (D3) does not address the drift C Design c_{L+1} of U1-ref's later companion steps; it is dominated anyway by
     (W2) + (D2) (c_{L+1} <= b(w)^2 <= mu^2/64 and mu <= Lip eta' << 1/Design).
 (G5, K1) convention: the ratios must be computed with U1's formula-1 kappa and the PATTERN's Omega (containing the active weak peaks of f);
     in the "peak convention" the block ratios change by a relative O(Phi_l^2/k) (numerically 0.7%-7%), and 2.1(T)/2.2(ii) would fail.
 (G6, W3) absorber sizes R and cluster weights of D^{U1'} use exact weight values; with perturbed weights R must be computed from the
     lower end (1 - 2^{-p}) c_p^low and cluster maxima read with (W1) applied to the actual predecessor.
 (G7, W1) under option (a) T^tr is NOT admissible in the note's sense ((T-a) demands equality for some (n,m)); the norm is a Martin-type
     norm (Martin's proof uses only ||T|| <= 1, re-checked).  I give a fix inside the note's class for N = 1 (W2): put the norm-one carrier
     in block 2 (ladder/round sequence with m(1) = 2); then for p_1 every relevant weight is generic and Corollary IV^tr.1 holds for an
     admissible T^tr(b) without exception.
With these repairs: Proposition KN^tr, Theorem S1, Master Theorem IV^tr and Corollary IV^tr.1 are PROVED modulo the refereed tools — in
particular modulo U1-ref's assembly of Master Theorem IV', which has had one referee pass.  Corollary IV^tr.1 = finite-F Lemma Z for p_1 (for
T^tr).  Corollary IV^tr.2 (all N) is correctly labelled SKETCH (X2 unrefereed).  Lemma Z and density for p_N (every N, including N = 1,
because of infinite F) and for Martin's p remain OPEN.  No counterexample is claimed; nothing I checked points to one.

## 1. Verdicts
| Claim (X1 label) | Verdict | Main point / fix |
|---|---|---|
| Lemma K (PROVED) | correct | re-derived (root selection, monotonicity via dk/dR^2 = k^2/(2(a - kR^2))); new independent solver: 3.0e-61; precision K1 on the kappa convention when Omega meets P |
| Lemma F (PROVED) | correct | elementary from K's monotonicity; "(up to fine terms)" superfluous; numerics: 400 blocks, floor attained to 8.5e-41; nearly neutral inactive mass only O(b^2) |
| Remark 1.3 (facts PROVED, conclusion HEURISTIC) | as labelled | not used anywhere; the negative answer to "design-supplied levers" is rigorous only in the sense of Lemma F |
| Lemma EC (PROVED) | correct | precisions: in (U)-blocks (X3) is a constraint, not an elimination; weight-freeness concerns (X1)-(X3), (X5) — (X4) of U1-ref has 1/lambda |
| 2.1 three kinds of blocks (PROVED) | correct with fixable gaps | D1 (cofactor polynomials scale by s^e, e <= n, not "factor in [s,1]"), D2 (inactive near-threshold carriers of (U)-blocks), D3 (deviation O(b) needs formula-1 convention) |
| 2.2 floor-form row (X4^0) (PROVED) | correct with fixable gaps | identity verified to 7.5e-62; data satisfy it up to K t (incl. weak peaks via eq:peakshift); kind [3] at f^#; weight-freeness true after W-fix |
| Lemma NLM (PROVED) | correct with fixable gap (W-fix) | Sard argument re-derived; conclusion unaffected by the weight-dependent face of K_kappa |
| Lemma GEN (PROVED) | correct | cleaner proof via "dim < n => contained in a hypersurface over k^rc" + norms; all non-weight data of T_final/D^{U1'} lie in a countable pool independent of the weights |
| Lemma QC (PROVED) | correct | (a)-(c) re-derived; precisions Q1 (mu(h) <= Lip h), Q2 (Design >= 1/h_kappa), Q3 (Lemma L for semialgebraic functions on K_kappa) |
| Proposition KN^tr (PROVED mod tools) | correct with fixable gaps | KN-1 (exact hold of inactive values: needed because beta is non-explicit), D2, S-0 (D3 replaced by (W2) + (D2)), Q2 |
| Design T^tr, Lemma W' (PROVED) | correct with fixable gaps | W1 (option (a) outside the note's class), W3 (absorber R, cluster maxima), W4 (lower-bound uses of weights: complete list confirmed) |
| Theorem S1 (PROVED mod assembly) | correct (given KN^tr's fixes) | (c) is the identity U1 Lemma 1.3; the content is the Hoffman control of the full cone with all rows (X3); RT*(c) independent of the configuration; S1-a: no claim on mixed fine structure |
| Master Theorem IV^tr (PROVED mod tools) | correct with fixable gaps (inherits) | U1-ref's proof uses (KN) only via Prop. KN, (X4) and Lemma 4.3's positive gaps; all supplied; true-vs-reference shift (U1 4.6) compatible with the margin |
| Corollary IV^tr.1 (PROVED) | correct with fixable gaps | holds for T^tr(a) (relaxed (T-a)); with W2 (m(1) = 2) also for an admissible T^tr(b); finite-F only |
| Corollary IV^tr.2 (SKETCH) | unclear (label appropriate) | substitution of the polynomial gap into X2's K_w is consistent with (W_exp); correctness of X2 itself pending |

## 2. Main findings (proofs in X1_ref_notes.md)
F1 (the idea is right).  Weight-freeness: every row of Gamma^#(kappa, a) after the substitution — (X1) entries u_l(j) and Delta'_m tau_m(j)
(peak weights only), aggregated signature rows (row scaling irrelevant), (X2), (X5), (X3)/kappa with entries r_l, (X4^0) with vs_l and
m^2 |r_l| K(sigma_rob, R_a^2), (U)-rows, (KN)-rows with 1/lambda of (KN)-block carriers — and every cofactor polynomial is free of the N_T
weights.  NLM: a witness of a coincidence must be a critical point of Psi_{D,S} on its stratum, so the coincidence set lies in a finite union
of CV_{D,S} x R^{N_T \ D} of dimension < |N_T|.  GEN: such a set lies in a hypersurface defined over the real closure of k; algebraically
independent weights avoid it.  QC: usc + compactness gives mu(h) > 0; Lojasiewicz and Puiseux give design constants.  The chain of KN^tr
(Lojasiewicz point r', nearby point r_1' of {F <= 1}, nearby point r'' with F <= 1 - mu) uses only Lemma F's inequality rho^0 <= rho for
the starting bound F(r_1) <= 1 + Cb, so the (T)-hypothesis is needed only for 2.2(ii) (data satisfy (X4^0)), and there only for positive
blocks.  Lemma F also explains precisely why U1-ref's (KN) worked and why it cannot be manufactured.
F2 (KN-1).  The margin mu(eta'/3) may be ~ eta'^beta with beta > 4 (non-explicit).  Every quantity that separates the true companion status
from psi_d(r'')/Phi_d must therefore be dominated by mu, not by a power of eta'.  Active ratios: realized exactly (joint TU fixed point);
sigma: depends on the peak SET only; fine terms: <= C c_{L+1}^2 <= C b^4 << mu by (W2), (D2); inactive Omega values: must be HELD at exactly
0 in the joint fixed point — otherwise second-order cross effects of the other blocks' moves (V1 Lemma B remainder ~ Design^2 eta'^2) give a
contribution ~ D^2 Design^4 eta'^4 to the statuses, which is not << c (eta'/3)^beta for beta > 4.
F3 (S-0).  U1-ref's steps (1b), (1c), (2) and the true-versus-reference shift (U1 Lemma 4.6) move statuses and shifts by <= C Design c_{L+1};
since c_{L+1} <= b(L, M(L))^2 <= b(w)^2 and (D2) gives b(w) <= mu/(8M), this is <= C Design mu^2 << mu (mu <= Lip eta' << 1/Design).
F4 (K1).  Lemma K with Omega ∩ P non-empty (formula-1 kappa): a^2 = sigma' + k^2 R^2, k = a + sigma', sigma' = Phi_{P \ Omega}^2 + sum_{Omega ∩ P}
(1 - rho^2) Phi^2 + s_f.  Numerically (weakpeak_ref.py) the active statuses differ from the floor by 0.54 b in this convention, while the two
conventions differ by 0.7%-7% in kappa.  The rate objects and the Step-0 push must use formula 1 with the pattern's Omega (U1's definition).
F5 (W2: N = 1 inside the note's class).  Under option (b) only carrier 1 has a rational weight.  Nothing on the dependency trees requires
m(1) = 1; with m(1) = 2 (D^{U1'}: start the block sequence of the rounds with block 2; round 1 has no PRE stages because no target meeting a
signature set is allowed at stage 1) no rational weight occurs in any pattern of p_1, so Corollary IV^tr.1 holds for an operator satisfying
(T-a) with equality.  For N >= m(1) the carrier-1 exception (X1 4.3 (R1)) remains OPEN; a slice version of NLM works whenever the rational
value is a regular value of psi_1 on every stratum.
F6 (W1).  Option (a) changes the class of operators: def:admissible demands equality in (T-a), Martin's Lemma B gives a norm-one T.  The
relaxation is harmless for Martin's theorem (only ||T|| <= 1 is used) and X1 says so, but statements "for T^tr (option (a))" are statements
about a Martin-type norm outside the note's class; F5 removes the issue for N = 1.

## 3. Attacks attempted
Uniformity in t (kind [3] needs vs Domega >= -3 gap^#/t and vs omega^+ <= 1.5 gap^#/t: the first improves as t decreases, the second follows
from gap(f) <= M b <= gap^#/4 for all t; the shift trick's cost is O(K t) because |rho^# - rho(f)| <= Lip eta' + C D^2 b); in the window
(D_cls, Q(w), Hoffman constants contain no 1/gap^#; b(w) only shrinks, u(w^+) = b(w), Q(w) adapts); in the number of carriers (finitely many
patterns per level; F is a max over N_T of all (T)-blocks jointly); along companions (one per (class, cube), realized exactly; FOUND KN-1);
simultaneous exactifications/levers ((T)-, (KN)-, (U)-blocks treated in one joint fixed point; each block's statuses depend only on its own
ratios, sigma and R^2; cross effects second order — FOUND that this matters for (T)-blocks, KN-1); two-lever count of Lemma R-kt (in a (T)-block
the second lever is the position of the exact point on Z; when Z is locally a point, F(r_0) != 1 generically and F(r_0) > 1 contradicts f's
own statuses through m_0 / C_Y, which b(w) absorbs); Hoffman/minor constants (all minors and cofactor polynomials are rate objects;
semialgebraic Lojasiewicz, Q3); design N-independence (no block count used); admissibility (FOUND W1; fix W2 for N = 1); well-foundedness
(pattern constants of level L before b(w), b(w) before c_{L+1}; E_c's dependence on s_far(w), hence on c_{L+1}, is only through aggregated
sign/zero rows whose existence is combinatorial; FOUND W3); genericity (k_0 countable and weight-independent: (GM) depends on y_l and l
only, absorber R integer, FD/absorber targets fresh with binary values; thresholds b, u, T_lo may depend on weights but are not cone
coefficients); signs and one-sidedness (vs_l = sgn r_l; identity checked; Delta' > 0 vs < 0 in (X4^0) analysed; weak peaks via eq:peakshift);
non-strict minima (included in B_kappa); empty Y_1 (excluded by m_0); quantifier order (design -> f -> clean w (rate objects of f for every
pattern and class) -> g, rho -> class, pattern -> companion -> data).
Suspected problems examined and REFUTED: (i) the coincidence set could be full-dimensional when Z is degenerate (no: Sard covers dim S < |D|);
(ii) mu(h) could exceed what the ratio displacement allows (no: mu(h) <= Lip h, Q1); (iii) the (U)-rescaling could break exactness of cofactor
polynomials (no: multi-homogeneous, D1); (iv) the perturbed weights could break T_final's admissibility (no: only upper bounds and
design-computed lower bounds are used; W3 for D^{U1'}); (v) the floor-form row could be violated by data in positive blocks with inactive
mass (only in (KN)-blocks, where U1-ref's row is kept).

## 4. Numerics (sanity checks; r9/X1_ref_work/)
indep_block.py / .out: NEW solver (bisection on the threshold equation from (E1), (E2), 60 digits).  Lemma K and rho = m|r|k/Phi on 99
blocks: 3.0e-61; a^2 = E: 5.5e-61; minus root <= sigma always; K increasing; inward identity lambda vs Domega = vs gamma + Delta' m^2 |r| k:
7.5e-62.  cvx_check2.py / .out: the solver against cvxpy/CLARABEL (dual norm maximisation): A to 1e-11, M, C to 1e-8, off-peak w to 1e-5.
floor_ref.py / .out: Lemma F on 400 blocks (inactive masses of all kinds): rho >= floor always, equality case 8.5e-41; nearly neutral inactive
carriers move statuses by O(b^2); (U)-rescaling lowers statuses by a factor <= s.  weakpeak_ref.py / .out: K1 (formula-1 convention: deviation
0.54 b; conventions differ by 0.7%-7% in kappa).  sard_toy2 (X1) re-run: identical.

## 5. Single most valuable idea
The weights of the switching carriers are themselves the missing second lever: once the inward rows are written at the floor, the exact
zero set of the tiny minors and the floor functions psi_d are weight-free, so the threshold enters only through psi_d(r)/Phi_d.  Choosing
all ladder weights algebraically independent over the countable field of the non-weight design data (a free choice inside T_final's
weight intervals) makes "1 is a local-minimum value of max_d psi_d/Phi_d on Z" impossible for every pattern at every level (semialgebraic
Sard), and compactness / Lojasiewicz / Puiseux convert this into status coherence with design constants that b(w) can absorb.
(Complement from this report: because the resulting margin has a non-explicit Puiseux exponent, every other perturbation of a (T)-block —
notably the inactive Omega values — must be held EXACTLY in the joint fixed point, not merely made small.)

## 6. What remains open (design T^tr with the fixes; finite block set I = {1..N})
(1) Option (b) (norm-one carrier with rational weight) for N >= m(1): rows whose weight-one carrier is an active near-threshold carrier of a
    (T)-block (forces rho_1(f) = 1 exactly) with a coincidence on the slice Phi_1 = 2^{-m(1)-1}.  [For N = 1: removed by m(1) = 2.]
(2) Mixed activity classes for N >= 2: X2's Theorem C_mix (to be refereed) + Corollary IV^tr.2.
(3) Infinite base support: (E1)-(E5) and U2's items; status coherence at infinite F (Lemmas F, NLM, GEN, QC should transfer since patterns
    are finite per level — not checked).
(4) Martin's p: needs Lemma Z at infinite F for infinitely many N (lem:martintail).
Lemma Z and density of NA((c_0, p_N), l_2^2) for every N (including N = 1) and of NA((c_0, p), l_2^2): OPEN.  The finite-F part of Lemma Z for
p_1 is now PROVED for T^tr (modulo the refereed programme, in particular U1-ref's Master Theorem IV' assembly).
