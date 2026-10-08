# P1 notes — Is the defect empty? (matching at scale, resonances, and an explicit nonempty defect)

Round 2, task P1. Setting: canonical base q (B_q = B_{c_0} + U(B_H), U compact with dense range), Martin's norm with a FINITE block
set I (p_N; by Preprint B Remark martin-tail this suffices; everything also holds for I = N given (T4) there), notation of
A_notes §1, §4 and BRIEFING. Imported as in Round 1: (T4) strict convexity of p** (unique normers, forced decomposition),
A_notes Facts A-F, Lemmas 4.3-4.7, Prop 4.5, Thm 4.10, 4.17, 6.2, 6.5, 6.8, Lemmas 7.1-7.2 (all refereed); in 3.8 also C_notes
Thm 6.4, Prop 6.5, Lemma 5.2 (Round 1, unrefereed; re-checked where used). Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Def(f) := C(f) \ (closure of all mates known to be recoverable by intrinsic means: finite, shifted, weighted certificates,
locally admissible linear decompositions = locally split mates, the averaging class of A Thm 6.8, C Thm 7.1, the constant-split
two-piece mates of A_referee §5.1). Part files: P1_part1.md ... P1_part6.md (this file assembles them). Script:
scripts/check_twopiece.py (numerical check of the two-piece decompositions, 200 random truncated models: max excess over
s(t) on |t| <= 1 is 2e-16).

## 0. Answer and summary

**The defect is NOT empty in general.** For a suitable admissible T (constructed in 2.1; Lemma B's conclusion only) there is a
non-attaining first row f in S_{p_N*} (any N >= 1) such that every mate obtained by any known intrinsic mechanism lies on ONE
line R u (u := u_{2,1}), while C(f) contains an infinite-dimensional family of "two-piece" switching mates, e.g. the finitely
supported mate c u(j)(e_j* - zhat_j alpha e_1*) for any contact j (Theorem 2.4). The mechanism is an EXACT RESONANCE: the block
vector u of an off-peak coordinate with w = 0 is, as a base functional, supported on supp a plus an infinite contact set K'
with the contact signs, and u(zhat) = 0; splitting the contact set between the two sides of t = 0 produces mates that use
contacts K_1 for t > 0 and the block carrier plus contacts K_2 for t < 0.

"Matching at scale" holds, but it is AUTOMATIC (it is the identity B+ + L*Omega+ = g = B- + L*Omega-) and does not force the
one-sided parts to be small: the two sides' one-sided usages have opposite signs and ADD UP in the transfer (D, Omega_D) =
(B+ - B-, Omega- - Omega+), which is a cheap zero-direction decomposition of f (3.4-3.6). So a defect mate exists only through
RESONANCES = cheap transfers with large one-sided mass. Exact resonances need infinitely many one-sided base coordinates
(contacts or near-flips; 4.1), so none exist at NA points or when a is in c_00 and K is finite; approximate resonances run
through near-threshold block carriers (cross-block near-duplicates switch only if their perturbation is >~ Phi in the xi-direction
with opposite signs, 4.2), and when the gaps of the carriers are not summable the mate is in cl Cert(f) anyway (weighted
averaging, 4.3-4.4). Exact description of the defect: at block-tame f (finitely many strict non-peaks, finite supp a)
Def(f) = (C(f) \ S(f)) union {g_c in C(f): Hhat(c) > 1} with S(f) the finite-dimensional certificate span (3.7); at C-tame f the
first piece is empty (3.8). The dual route reduces everything to c_0-exposed mates but cannot close the gap (5.1-5.3).
The explicit defect of Theorem 2.4 is nevertheless recoverable by ENGINEERED NA approximants (6.3, SKETCH), after correcting
the referee's scheme (far NEGATIVE masses and a constant tail). So it is not a counterexample to density; it shows that
density cannot be proved by intrinsic (sequence-independent) recovery alone.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | All known intrinsic recoverable classes lie in cl S(f), S(f) := span of certificate directions; hence C(f) \ cl S(f) is in Def(f) | PROVED | 1.2-1.3 |
| 2 | Construction of an admissible T with prescribed special vectors and a "badly approximable" zhat (all coordinates but one are peaks) | PROVED | 2.1 |
| 3 | The first row f: non-attaining, contact set infinite, Q_1 = {2}, Q_m empty otherwise | PROVED (T4) | 2.2 |
| 4 | Two-piece mates g_{K_1} in C(f) (explicit decompositions on both sides) | PROVED (+numerics) | 2.3 |
| 5 | **Def(f) != empty**: cl Cert^sh(f) in R u, g_{K_1} not in R u for empty != K_1 != K' | PROVED | 2.4 |
| 6 | Single-scale resource bounds and capacities (window / one-sided / remainder) | PROVED | 3.1-3.3 |
| 7 | Transfer identity; sign opposition; matching at scale is automatic; one-sided parts bounded by the transfer's one-sided mass | PROVED | 3.4-3.6 |
| 8 | Block-tame f: Def(f) = (C(f) \ S(f)) disjoint union {Hhat > 1}; cl Cert^sh = Cert^sh | PROVED | 3.7 |
| 9 | C-tame f: C(f) in S(f), only the second-order defect can survive | PROVED mod C Thm 6.4/Prop 6.5 | 3.8 |
| 10 | Exact resonances force infinitely many one-sided base coordinates (none at NA points) | PROVED | 4.1 |
| 11 | Sign rule; Martin's near-duplicates serve the same side unless perturbed by >~ Phi | PROVED | 4.2 |
| 12 | Weighted averaging theorem; near-threshold carriers with sum of gaps = infinity give mates in cl Cert(f) | PROVED | 4.3-4.4 |
| 13 | Switching through super-near-threshold carriers (summable gaps) or weak peaks: in cl Cert(f)? | OPEN | 4.4 Rem |
| 14 | Support-function criterion; reduction to c_0-exposed mates; explicit support-function gap | PROVED | 5.1-5.3 |
| 15 | At the example, C(f) is contained in E_u (explicit infinite-dimensional space) and contains a slab of it | PROVED | 6.1-6.2 |
| 16 | Engineered recovery of the explicit switching mates at the example (corrected referee scheme) | SKETCH | 6.3 |
| 17 | Second-order defect {Hhat > 1} nonempty somewhere? | OPEN | 3.7 Rem |
| 18 | For EVERY admissible T, some f has Def(f) != empty? | OPEN (true for the constructed T) | 7 |
| 19 | Conjecture A 7.5 (scale separation => empty defect) | FALSE as stated (exact resonances need no rates) | 7 |

