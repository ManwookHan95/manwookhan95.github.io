# Referee report on U3 (Round 8): adversarial analysis of (C*) — explicit rows, mates, and decision

Refereed: r8/U3_notes.md (= U3_head + U3_part1..5, byte-identical, checked with diff), r8/U3_work/{nl_check.py, nl_check2.py,
vt_check.py} (re-run, outputs identical), against paper/martin_density_note.tex (def:twopiece, def:BT, prop:onesidedupper, thm:onesided,
lem:bookkeeping, lem:base, prop:rebalancing, lem:TV, lem:transferdata, lem:persistence, lem:assembly, def:engineered, lem:approxfacts,
lem:F1, lem:anchor, def:SC, lem:scrambling, thm:engineered with its full proof, lem:twosided, lem:budget, lem:suplevel, def:SLD, thm:SLD,
rem:lemmaZ(c), lem:martintail) and the refereed Round-5/6/7 results (Y1 sources and Lemmas 3.1-3.5; V1 Lemma D, Lemma S, shift cost c_pi,
Lemma TU; V2 Lemma 3.1, Def. 3.2, Theorem C1, Cor. C1.1, Master Theorem III'; V4 Construction SA / Theorem 2.2, Prop. 3.2, Lemma 5.2,
Prop. 5.3, Lemmas 3.3, 3.6, 4.1', 5.4, 5.5, Theorem 5.6 with V4-ref R3, R5, R10).  My part files: r8/U3_ref_part1..5.md; assembled notes with
all proofs of fixes: r8/U3_ref_notes.md; scripts: r8/U3_ref_work/ (vt_ref_check.py and junction_check.py are new).

## 0. Bottom line
U3 is a careful and useful piece of work.  Its structural results are right: the exact rigidity of two-piece data (Lemma S, Cor. S1,
S2, Prop. S3) and its consequence Theorem NL — the fibre map is NOT lower semicontinuous at V4's self-aligned (BT) row along (BT) rows
with one far anti-type flip, so approximants for oscillating mates must be aligned or banked — are proved; Proposition FZ (fixed-z tilts
create both kinds of robust swallowed peaks, for every admissible T) and Corollary FZ (aligned (C*) rows are isolated in their fixed-z fibre
and their tilts are in Rec) are proved; the properties of the nested-tuning rows f^infty (non-(BT), no (SC), rho^sh = 0 and c_pi = 0 at every
clean sub-window) are proved; Lemma VT (violation tolerance of a single engineered stage) is proved and I confirmed it independently in a
finite model, including the predicted failure below the threshold (VT).
Five defects must be repaired, none of which touches a PROVED structural statement:
(1) the existence induction of Theorem NT is inconsistent as written (the region of stage (iii) is empty) — repaired (F1: hysteretic owner
rule, design addition (Z0+), a one-dimensional IVT along the curve {g_i = Phi_{l_{i+1}}/4}); label stays SKETCH;
(2) Proposition NT-M(ii) is false for general Omega/Dom (target coordinates of special omega-carriers off F are not controlled) — true for
Omega = {k_-} (the oscillating mates) and, for all Omega, under (Z0+) (F2, PROVED); Corollary NT-R likewise;
(3) Lemma 3.5 needs Delta_new <= 0 (F3);
(4) Lemma QB2's accounting needs positive parts, the theta piece, and pieces of the size of the violation at banks (F4);
(5) the "(PROVED arithmetic)" scaling check of (S2a) is wrong: the window masses create a first-order theta/+- JUNCTION MISMATCH of exact
order s_1/t^2 (F6a, numerically confirmed), so K_sharp is of order t^{-2}; rebalancing it needs transfer peaks of inefficiency ~ t^2 at weight
scales that super-fast ladders do not provide (HEURISTIC).  I propose d-CONSISTENT engineered approximants (exact re-tuning of the normalized
values of the coarse omega-carriers at f' by V1-type levers; then d' = d on all switching vectors and K_sharp = O(1)) — SKETCH (F6b).
Also: U3's "OPEN sub-case" of (S2d) is not an obstruction (symmetric split, F5); Corollary FZ's Consequence (a) is overstated for general
(C*) rows; the reduction "Lemma Z (F finite) <= (S1) + (S2)" also needs RT*(c) (SKETCH).  No counterexample is claimed; nothing I checked
points to one.  Lemma Z and density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2) remain OPEN for every admissible T, including D^{V2}.

## 1. Verdicts
| Claim | U3 label | Verdict | Main point |
|---|---|---|---|
| Lemma S (sandwich) | PROVED | correct | V2 Prop. C3 + V4 Lemma 3.3 read off the omega-supports; no smallness needed |
| Corollary S1 | PROVED | correct | division of the sandwich by z psi |
| Corollary S2 (F, K finite: no switching, no shift) | PROVED | correct | (T-c) + injectivity of L^*; P_m non-empty |
| Proposition S3 | PROVED | correct | Lambda_n vanishes on C(f_n); |Lambda_n(h)| <= ||h||_1 (better constant); l_1 and p* equivalent |
| Theorem NL | PROVED | correct | Steps 1-4 re-derived (targets used infinitely often in def:SLD; hysteretic re-run gives (BT); dominance of psi_n); numerics re-run; two reading precisions (n1), (n2) |
| Lemma D' | PROVED | correct | definitions of sources + V1 Lemma D |
| Proposition FZ | PROVED | correct | any admissible T, diagonal U; at most ONE a_1 != a_0 has Phi(a_1) proportional to Phi(a_0) |
| Corollary FZ | PROVED mod MT III' | correct for the stated aligned class; Consequence (a) overstated (P2.1) | non-deficient blocks of a general (C*) row may lose a source type under a tilt |
| Lemma A | PROVED | correct, statement precision (P2.2) | Sigma(omega) clause; "owner w != 0" must be "non-negligible owner" |
| Theorem NT (existence) | SKETCH | SKETCH, written induction INCONSISTENT; repaired (F1) | stage (iii) region empty; theta not differentiable on {nu = theta}; owner switching curves |
| Theorem NT (properties (b)-(e)) | PROVED | correct | (R1)-(R7) and c(1; pi) re-checked row by row |
| Proposition NT-M | PROVED | (i), (iii), (iv) correct; (ii) FALSE as stated for general Omega/Dom; correct for Omega = {k_-} and under (Z0+) (F2) | target coordinates of special omega-carriers owned by other carriers |
| Corollary NT-R | PROVED mod V4 5.6 | correct for Omega = {k_-}; under (Z0+) for all Omega (F2); genericity sentence for (H2) unjustified | E = {}, 32-dominance via V4 Lemma 4.1' |
| Recovery of all mates of f^infty (3.4) | SKETCH | SKETCH, plausible; remaining steps misdescribed (P3.4) | route via V4 companions needs no VT/(S2): window arithmetic with shift column, window-data transplant (Delta = 0 scales), inward moves of near-threshold specials, (Z0+) |
| Lemma 3.5 (dead-zone bump) | PROVED | correct after precision (F3) | needs Delta_new <= 0; re-split everywhere; ||g' - g|| <= 2 kappa lambda_k |
| Lemma QB2 | PROVED | inequality correct; accounting needs (P4.1)-(P4.4) (F4) | positive parts; theta piece; pieces O(violation) at banks; cost m log(e/m); numerics consistent with q_0 rho^2 eps^2 |
| Lemma VT | PROVED | correct (single stage); numerically confirmed | every case of Step 3 (Base) re-derived; threshold real, constant 32 not sharp |
| Prop. RT*(a), (b), (d) | PROVED | correct; bookkeeping (P4.5): |Delta| <= C D(l)/t | c^comb minimum attained; fine-origin mass <= C D T_lo^2 (P2), <= C D T_lo^9 (W10) |
| Prop. RT*(c), (e) | SKETCH | SKETCH, plausible; (c) is a separate ingredient of the reduction (P4.7) | class-R and unused G strict non-peaks must be neutralized as omega-carriers |
| RT*(f) scale bookkeeping | PROVED | correct (also with |Delta| ~ 1/t) | s_1 = T_lo^8 c_l meets (VT) and the scrambling bound; (W10) compatible (upper bound on weights) |
| (S1) single shifted block, free-ray q<0 carrier | PROVED | correct | Hoffman constant 1/|q_k| <= design/u at a clean sub-window |
| (S2a) | SKETCH | SKETCH, but the scaling check is WRONG (F6a) | K_sharp ~ t^{-2} from kappa ~ s_1/t^2; repair = d-consistent approximants (F6b, SKETCH) |
| (S2b) | SKETCH | SKETCH; inherits (S2a)'s problem; plausible after F6b | one d-tuning serves all pieces |
| (S2c) | HEURISTIC | HEURISTIC (as labelled) | — |
| (S2d) | SKETCH | SKETCH; its OPEN sub-case is not an obstruction (F5) | symmetric split: (H3) at l_1 cost <= violation |
| Lemma R-pin | PROVED | correct | lem:suplevel(f) |
| Numerics (Part 5) | sanity | reproduced; two reading precisions | see Section 4 |

## 2. Main findings (proofs in U3_ref_notes.md, part 5)
F1 (Theorem NT existence).  U3's stage (iii) confines g_{i+1} to (gamma_{i+1}, 2 gamma_{i+1}) on B_{i+1}, while the next stage needs
g_{i+1} < Phi_{l_{i+2}}/2 << gamma_{i+1}: empty.  Repair: keep the curve {g_{i+1} = 0} crossing int B_{i+1}; at stage i+1 move along the curve
{g_i = Phi_{l_{i+1}}/4} (a Lipschitz graph in coordinates (x_1, x_2) = (<c_i, Phi>, <c_{i+1}, Phi>)) and use the IVT for g_{i+1}; take a ball of
radius ~ Phi_{l_i} Phi_{l_{i+1}}; use the HYSTERETIC owner rule so that no carrier in (L_i, l_{i+1}) switches (margins ~ delta H decay
super-exponentially); choose L_{i+1} after B_{i+1}.  With (Z0+) (dense F_0-supported targets) specials have B = 0 automatically.
F2 (NT-M(ii)).  At j in supp y_k \ F owned by another carrier o, v(j) = -Delta lambda_o w(o) u_o(j) + lambda_k Dom(k) y_k(j)/n_k + ...: with
eps Dom(k) large and d(Dom) fixed (adjust Dom(k_-)), the second term wins with the sign of y_k(j); a wrongly signed coordinate breaks
admissibility.  Under (Z0+) Omega-carriers touch F^c only on their own signature sets and (ii) holds for every Dom (proof in F2).
F3-F5 as in the verdict table.
F6 (junction mismatch).  (E4)'s identity (d'_m - d_m)(omega) = sum_k omega(k)[(R xhat')(k)/|R xhat'| - (R zhat)(k)/|R zhat|] and the first-order
effect of the window masses m_j = 4 rho s_1 |b^theta_j| (||b^theta||_1 ~ 1/t) on the coarse values give kappa^diamond ~ s_1/t^2 for window data
with switching of size 1/t; junction_check.py shows kappa t^2/s_1 constant to five digits over t in [0.03, 1].  At |tau| = s_1 the mismatch is
tau^2/t^2 and is scale invariant (enlarging the theta-regime enlarges the masses).  Rebalancing needs inefficiency ~ t^2 and Lambda <~ t^{-2},
i.e. a carrier of weight in [~ s_1^2/t^2, ~ t^2] within ~ t^2 of an f-dependent transfer target; D_Omega-type ladders have O(1) carriers in
that weight range, with fixed targets (HEURISTIC obstruction for U3's (S2a) as written).  F6 does NOT affect thm:engineered,
Theorem E (Z3), E^SC (V2) or E'' (V1): they use thm:engineered non-uniformly, at a fixed row with fixed exact data whose mate property at
that row comes from Lemma U (no engineered approximant, no mismatch).  Repair (SKETCH): re-tune at f' the normalized values
of the finitely many coarse omega-carriers exactly (V1 Lemma TU levers; diagonal base makes each lever act on its own carrier at first
order); then (d' - d) vanishes on every switching vector of every piece, lin' reduces to the anchor/Bregman part, K_sharp = O(1) with fixed
transfer data, and U3's remaining scaling arithmetic holds for |tau| <= c_flat t under s_1 <= c delta t^3 (met by RT*(f)).
F7 (|Delta| at window scales).  |Delta| <= C D(l)/t; the fine-origin mass is <= C D T_lo^2 without (W10) and <= C D T_lo^9 with it; (VT) with
s_1 = T_lo^8 c_l needs c_l >= C' D T_lo, true.

## 3. Attacks attempted
weak* vs norm (f_n -> f via rem:lemmaZ(c); psi_n -> psi in l_1; engineered approximants converge in p*); uniformity in t (Lemma VT is single
stage; (S2a) uniformity fails as written — F6); in the window (RT*(f) re-done with |Delta| ~ 1/t); in the number of active carriers (Omega
finite; f^infty has infinite Q, handled by the nest and margins); along companions (Theorem NL: lsc fails along non-aligned (BT) rows;
V4's hysteretic re-alignment is aligned); simultaneous exactifications (masses + banks + d-tuning: a joint fixed point, SKETCH); Hoffman
constants ((S1) single block: 1/|q_k| <= design/u since rho_k robust at clean w); design N-independence ((W10), (Z0+) are ladder/target
conditions, N-free); admissibility ((Z0+) keeps the family dense and allowed; (W10) only lowers weights; well-founded: c_l uses
T_lo(l-1)); non-attained infima (rho^sh = 0 and c_pi = 0 attained by explicit vectors; c^comb_* an attained LP minimum); signs and
one-sidedness (data vs decomposition conventions in R-pin and NT(e); bank flips only on violated sides, F4; Lemma 3.5's d-change raises Delta
for swallowing-type carriers, F3); near-contacts vs contacts (Cor. FZ needs exact or tiny-room swallowing; Consequence (a) overstated);
c_0 vs l_infty (rows with z in l_infty are allowed by rem:lemmaZ(c) and thm:engineered); finite vs infinite (Q infinite at f^infty; Sigma_n
finite at (BT) rows); hidden assumptions on T ((Z0), (SF*), (SF_tau), (b') from V4; (W10) and, in my fixes, (Z0+) — all explicit design
choices; compatibility with D^{V2} not checked line by line, as in V4-ref); quantifier order (design -> f -> g, rho -> window -> companion ->
stage -> data; in F1 the special targets are chosen during the row construction, after the design).  Counterexample search: Theorem NL's
mechanism only shows that SOME approximating sequences fail; along aligned/banked approximants nothing obstructs recovery (Prop. S3).

## 4. Numerics (sanity checks only; double precision, CLARABEL)
nl_check2.py re-run: identical to U3 Part 5.  Precisions: (n1) its grid values at f_n are all NEGATIVE down to |t| = 1e-3 (the linear excess
of c g at f_n beats the quadratic slack only below |t| ~ 1e-6, unresolvable); the reliable evidence is the INFEASIBLE side-+ SOCP;
(n2) the residual 2.4e-8 at f_n is solver tolerance (theoretical value 0).
vt_check.py re-run: identical (m_min/eps^2 = 0.83 ... 0.71, consistent with the exact prediction q_0 rho^2/(1 - rho^2 kappa_w) = 0.67 up to the mass grid; U3's 0.81 omits q_0 and the slack factor).
vt_ref_check.py (new): full engineered approximant from violated data (dead-zone contact violated by eps on side +), true p* by SOCP:
s_1 = 32 rho eps/delta and s_1 = 4 rho eps/delta: bound p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta) holds on the whole grid; s_1 = eps/20: fails
for tau in [5.6e-4, 1.0e-2] (eps = 2e-3) and [1.8e-4, 2.4e-3] (eps = 5e-4) — exactly the linear-flip window predicted by Lemma VT.
junction_check.py (new): kappa t^2/s_1 = 4.8203e-8 for t in {1, 0.3, 0.1, 0.03}, s_1 in {1e-4, 1e-5}: the junction mismatch scales as s_1/t^2.

## 5. Single most valuable idea
Violation tolerance of engineered approximants (Lemma VT): in the proof of thm:engineered the sign conditions of two-piece data enter ONLY
the base-excess claim, and a violation of l_1-mass epsilon costs at most 2 rho |tau| epsilon in the +- regimes and nothing in the
theta-regime (the window masses protect every contact, whatever the sign of b^theta); hence near-exact data suffice at a stage with
2 rho epsilon <= delta s_1/16.  Together with Theorem NL (approximants must be aligned or banked) this pins down what a recovery of (C*)
rows must look like.  The referee's complement: to use VT uniformly across the scales of a window the engineered approximant must be
d-CONSISTENT (normalized values of the coarse switching carriers re-tuned exactly), since otherwise the window masses produce a theta/+-
junction mismatch of order s_1/t^2 that super-fast ladders cannot rebalance.

## 6. What remains open after U3 (+ this report), design D^{V2} on D_Omega with diagonal base, F finite
(1) (S1) in general: exact coupling rows Delta_m = d^#_m(omega^-) - d^#_m(omega^+) inside the exact combinatorial cone with design x u^{-O(1)}
    constants when no free-ray q<0 carrier exists or >= 2 blocks are shifted (V2's (C*-3)); single shifted block with a free-ray q<0 carrier:
    PROVED.
(2) (S2), sharpened: (S2a') d-consistent engineered approximants with uniform per-piece bounds T_0 >= c_flat t (lever sizes against the data
    at lever coordinates; scrambled-set bound S_m <= c delta t s_1); (S2b) averaging at the norm-attaining approximant; (S2c) threshold
    comparison epsilon_w <= delta s_late/(32 rho) (HEURISTIC).
(3) RT*(c): coarse exactness at V1's companion modulo coupling rows and medium/fine contributions (SKETCH).
(4) The explicit non-(BT) (C*) rows f^infty: existence SKETCH (F1); Lemma Z at f^infty: exact-data mates PROVED (Omega = {k_-}; all Omega
    under (Z0+)), general mates SKETCH via V4 companions (window arithmetic with a shift column, transplant of window data, inward moves).
(5) Infinite F: (E1)-(E5) of ADDENDUM 7, unchanged.
Lemma Z, and density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2), remain OPEN for every admissible T, including D^{V2}.
No counterexample; nothing points to one.
