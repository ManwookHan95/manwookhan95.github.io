# Z4 (Round 5): cases (O2) and (O3) of Remark rem:openZ — infinitely many swallowed signature sets and maximal contact

Setting: the note paper/martin_density_note.tex (numbering and notation as there), canonical base, finite block set I = {1,...,N} (p = p_N;
Lemma lem:martintail transfers density to Martin's norm), the signature-ladder operator of Definition def:SLD or the modified ladder SLD_G
proposed in part 2.4, first rows f with finite base support F. Parts: Z4_part1..8.md (assembled below). Script: Z4_work/maxcontact_toy.py.
No counterexample is claimed and nothing found points to one. Lemma Z and density remain OPEN for every admissible operator.

## Main results (statements in words)
**Theorem A (infinitely many swallowed signature sets; part 3, part 4).** PROVED. Use the modified ladder SLD_G (Definition def:SLD with the
window lengths and window tops inflated by a design constant G*(l), the largest Hoffman constant of the finitely many "configuration"
cones of level l; all results of Section 8 survive). Let f be a first row with finite base support, with an arbitrary (possibly infinite)
set of exactly swallowed signature sets. Assume: (H2') in every block the uniform shift can be pinned by peaks — a non-degenerate peak which
is good or swallowed with the swallowing sign, and a non-degenerate good peak or a swallowed peak of the opposite (anti) sign; (H3) every
swallowed peak of the swallowing sign is non-degenerate; (DR) the zero-cost cone admits fixed finitely supported d-repair directions with
d-sums of both signs in every block that contains a non-d-neutral swallowed strict non-peak; (W_inf) a growth condition: along a subsequence
of levels l, the quantity [(Lambda*_f(l) + M_f(l) + l)/Lambda°(l)]^2/(gamma_T(l)^2 gamma_f(l)) is o((l 2^{l^3})^6), where Lambda*_f is the room
product of the good signature sets (computed after removing the coarse swallowed targets), M_f(l) the sum of the reciprocal margins of the
swallowing-sign swallowed peaks up to level l, gamma_f(l) the least gap of the swallowed strict non-peaks up to level l, and gamma_T(l) the least
room of the free coordinates met by swallowed targets up to level l. Then f is recoverable: (f, g) lies in the closure of the norm-attaining
operators for every mate g. No resonance, no d-neutrality, no (H1) and no finiteness of the swallowed set is assumed.
For the ORIGINAL ladder the same holds without (DR) if the growth condition includes the f-dependent Hoffman constants of the actual cones
(Corollary 4.1). Theorem A and Corollary 4.1 contain Theorem thm:S — case (B_res) for SLD_G, case (B_fin) for both ladders (Corollary 4.2)
— and weaken (H2) to (H2') there. (H3) can be dropped from the window construction (Lemma 8.1, PROVED); the corresponding engineering step
is only SKETCHED (part 8, under an f-dependent steerability hypothesis).
**Mechanism (new).** (1) Scale-dependent active sets U(t) = {swallowed l <= l_* : lambda_l >= t^2}: inactive swallowed carriers cost O(l_* t)
in total, active ones satisfy lambda_l >= t^2, which turns the l_1-displacement of the projection into the coordinatewise bound needed by the
one-sided expansion. (2) The zero-cost cone depends on f only through finitely many combinatorial data on the target supports, so its
Hoffman constant is bounded by a DESIGN constant G*(l), which the super-fast ladder absorbs (T is fixed before f). (3) The uniform shift is
pinned without (H2) by BASE peaks: an anti-sign swallowed peak is pinned by the switching budget, a swallowing-sign one by its margin.
(4) d-neutrality is restored exactly by fixed repair directions (or, original ladder, by the actual Hoffman constants).

**Proposition B (far lowerings; part 1).** PROVED. p*(f^L - f) <= C_f sum_{l>L} lambda_l <= C_f c_{L+1}/2. On every scale inherited from f
through the rho-slack, the carriers made roomy by the lowering carry total switching O(t), and the coarse ones are swallowed exactly as at f;
so lower semicontinuity along far lowerings needs the same exact matching as Theorem A at f itself (far lowering localises but cannot absorb
f-dependent constants — the latter is HEURISTIC).

**Proposition C (rigidity of the d-mismatch; part 5).** PROVED. At maximal contact every two-piece data are d-neutral; in general a nonzero
d-mismatch in block m forces every far point of every peak signature set of block m to be a contact of a prescribed sign. So the option
Delta d >= 0 of Corollary cor:D1 is essentially never available on swallowed sets.

**Corollary D (maximal contact, (O3); part 5).** PROVED. At maximal contact (F finite, z = eps_0 off F) (H2') holds automatically, gamma_T = 1 and
Lambda*_f <= C Lambda°; with the design clause c_l <= (delta_l ||h_l||_1)^2, every carrier whose target does not cancel its signature lift is a
swallowing-sign peak with margin >= q_0 delta°_l/4. Hence f is recoverable under (H3), (DR) and liminf (1 + M^canc_f(l)/Lambda°(l))^2/
(gamma_f(l) (l 2^{l^3})^6) = 0 (M^canc: reciprocal margins of signature-cancelling swallowing-sign peaks). This adds to Corollary
cor:BTrecovered the maximal-contact rows that violate (BT) through infinitely many strict non-peaks or through weak/degenerate anti-sign peaks.

## What remains (precise; part 6)
(E-a) degenerate or super-weak swallowing-sign swallowed peaks (failure of (H3); margins beyond the ladder, e.g. failure of (MS) on the
swallowing side) — the degenerate part is reduced in part 8 to a steering lemma for the engineered approximants (SKETCH, needs an f-dependent
steerability hypothesis; without it OPEN); (E-b) near-threshold swallowed strict non-peaks (gaps beyond the ladder); (E-c) near-contacts met by swallowed targets;
(E-d) one-sided d-resources (failure of (DR)); (E-e) approximate swallowing of good sets ((O1)(i)). In each, the window data are exact
two-piece data only up to a first-order defect O(t) at window scale t, which neither windowed averaging nor the engineered approximants
tolerate (HEURISTIC, one-line estimates); perturbing f converts one small parameter into another of the same size (HEURISTIC). The common
open step is Problem 6.2: exact data for inexact resources, or a multi-scale engineering theorem accepting O(t) first-order defects.
(O4) (infinite F) was not treated.

## Labels
| # | Claim | Label | Where |
|---|---|---|---|
| 1 | coarse values unchanged under far lowering (Lemma 1.1) | PROVED | part 1 |
| 2 | p*(f^L - f) <= C_f c_{L+1}/2 (Prop 1.2) | PROVED | part 1 |
| 3 | band arithmetic: roomy carriers negligible on inherited scales (Prop 1.3) | PROVED | part 1 |
| 4 | zero-cost cone description and cost bound (Lemma 2.1) | PROVED | part 2 |
| 5 | configuration Hoffman constant G*(l) finite, design-computable; actual cone dominated (Lemma 2.2) | PROVED | part 2 |
| 6 | d-repair lemma (Lemma 2.3) | PROVED | part 2 |
| 7 | SLD_G admissible; all of Section 8 survives (Prop 2.4) | PROVED | part 2 |
| 8 | Theorem A = Theorem 3.1 (S_Binf) | PROVED | parts 3-4 |
| 9 | Corollary 4.1 (original ladder, f-dependent Hoffman growth) | PROVED | part 4 |
| 10 | Corollary 4.2: Theorem thm:S contained, (H2) -> (H2') | PROVED | part 4 |
| 11 | Lemma 5.0 (peaks of both signs), Prop 5.1 (d-neutral at maximal contact), Prop 5.2 ((H2') automatic) | PROVED | part 5 |
| 12 | Lemma 5.3 (signature lift; with design clause) | PROVED | part 5 |
| 13 | Corollary 5.4 / D (maximal contact) and Remark 5.5 (scope) | PROVED | part 5 |
| 14 | Prop 5.6 (general rigidity of the d-mismatch) | PROVED | part 5 |
| 15 | Lemma 6.1 (windowed averaging with window-dependent c_flat) | PROVED | part 6 |
| 16 | first-order defects O(t) cannot be averaged/engineered away; perturbations only move the smallness | HEURISTIC | parts 5, 6 |
| 17 | far lowering cannot absorb f-dependent growth | HEURISTIC | part 6 |
| 18 | (E-a)-(E-e), Problem 6.2 | OPEN | part 6 |
| 19 | finite-model check of the new pinning signs | numerical, signs only | part 7 |
| 20 | Lemma 8.1: data using degenerate peaks inwardly are exact at f; window data of Theorem 3.1 exist without (H3) | PROVED | part 8 |
| 21 | engineering (Corollary cor:D1) for data using degenerate peaks, by steering them to strict non-peaks at f', under an f-dependent steerability hypothesis | SKETCH | part 8 |
| 22 | weak peaks with intermediate margins can be neither projected nor degenerated within the window arithmetic | HEURISTIC | part 8 |
