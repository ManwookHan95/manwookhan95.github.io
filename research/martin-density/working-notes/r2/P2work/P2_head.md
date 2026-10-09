# P2 notes — engineered recovery of mates that use ONE-SIDED resources (replication–averaging–transfer)

Round 2, task P2. Setting: canonical base q, Martin's norm with a FINITE block set I (p_N; Preprint B Remark martin-tail), only Lemma B's
conclusion about T. Imports: A_notes Facts A–F, Lemmas 4.2–4.7, 7.1–7.2, Thms 4.10, 6.5 (refereed, with referee fix G1: coordinatewise
radius); N_part1 Thm 1 (density <=> Ls(f) = C(f) for all f; g in Ls(f) <=> (f, rho g) in cl NA for all rho < 1); P1 2.1–2.3, 6.1–6.2 (refereed).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Part files P2_part1..5.md (assembled below). Scripts: ctx/r2/P2work/.

## 0. Summary

**Main theorem (PROVED, Thm 2.1).** Let f in S_{p*} have finite base support F, and let g in C(f) admit one-sided linear ("two-piece")
decompositions on the two sides of t = 0 whose block parts are finitely supported strictly below the peaks and whose base parts live on
F and the contact set K with the contact signs, with EQUAL d-coefficients on the two sides (d-neutral transfer v = b+ - b-). If one block
is active (or several, under a span hypothesis (S)), then (f, rho g) is in cl NA((c_0,p), l_2^2) for every rho with rho^2 kappa < 1, and for every
rho < 1 when the decompositions are locally admissible. No assumption on K (it may be infinite), on the split of the contact mass between
the sides (non-constant splits allowed), on rates of T, or on the deep block structure of f is needed.
This makes A_referee §5.4 and P1 Prop 6.3 rigorous (Cor 2.3): all explicit defect mates of P1's example (P1 Thm 2.4) and the whole slab of
P1 6.2 lie in Ls(f). The recovering approximants are ENGINEERED (window masses on contacts, far flipped contacts with negative masses,
one raising mass, a theta-tail of the target), as they must be: P1-referee R3 shows these mates are not recovered along canonical truncations.

**Mechanism.** (1) Exact transfer: after recomputing d-coefficients at f' the one-sided decompositions of f transfer to f' with NO first-order
error (Remark 2.2(a)); (2) steering: one scalar condition per block, v_m(x') = 0, forces both sides to represent the same g' (pull by flipped
far contacts with negative masses, raise by one mass, intermediate value theorem); (3) theta-tail: beyond the window the target equals the
two-sided theta-combination, so the small-scale certificate needs masses only on finitely many contacts; (4) slack only for |t| >= T_0 (fixed).
No averaging is needed for this class; Lemma 1.5 (averaging over scales, PROVED) is required only for scale-dependent mates (part 4).

**Answers to the specific questions.**
* Mixed term delta t <P_perp U*e_j, P_perp U*B_t>/||U*a|| (3.1, PROVED): it is the first-order shift of the base part caused by a contact mass.
  For one decomposition it is absorbed by normalizing g'(x') = 0; for two pieces its difference is cancelled EXACTLY by the steering
  condition (Thm 2.1, Step 1) — not an obstruction; for finitely many pieces, finitely many steering conditions; for a continuum of
  scale-dependent pieces it is equivalent (3.2, PROVED identity) to exact replication of infinitely many relative block positions, which is
  where it becomes an obstruction (quantified by (QI), 4.4; OPEN).
* Non-zero d-mismatch (A_referee §5.5): PROVED garbage identity (3.3): the only change is E = -sum Delta d_m R_m*(w'_m - w_m), which must be
  <= eps_0 s_1 in l_1. With finitely many strict non-peaks/degenerate peaks, margin sparsity and a tuning span condition this holds (Thm 3.4,
  SKETCH with all estimates) — so A_referee's "engineering breaks when d != 0" is too pessimistic: what breaks it is infinitely many
  strict non-peaks (or dense near-threshold peaks) in the active block, where deep retuning ((QI)) is needed.
* C's "implant scale gap" (4.5): arithmetic correct; as an obstruction FALSE — Thm 2.1 is a rigorous instance with p*(f'-f) >~ s_1 >> s_1^2
  where the window (s_1, sqrt(p*(f'-f))) is covered by exact transfer. It correctly locates the difficulty for scale-dependent mates ((QI)).
* For which mates can regime (ii) be supplied (4.4(4)): base one-sided usage — always (contact masses; price: steering); off-peak carriers
  with gap — always (replicate finitely many ratios); block one-sided carriers (weak/degenerate peaks, near-threshold, coordinates pushed
  beyond their gap, deep coordinates) — degenerate peaks by one tuning move each (SKETCH); the others only through implanted gaps on
  carriers with rates ||u_k - v|| <~ Phi_k, compatible with replication only under (QI) (OPEN); components carried one-sidedly by block
  resources WITHOUT rates and without a contact representation cannot be supplied by certificates at C-tame approximants (P1-referee R1).
* Exact residual class (4.6): (R1) non-neutral two-piece data at non-tame active blocks; (R2) several active blocks without (S);
  (R3) two-piece data needing shifts (Rem 2.4, SKETCH); (R4) infinite F (near-flips); (R5) genuinely scale-dependent switching
  (approximate resonances) — reduced by the abstract scheme 4.3 to (QI) + implant compatibility, OPEN and T-dependent.
* Density of NA((c_0,p), l_2^2): still OPEN. Nothing here suggests a counterexample: every concrete defect mate known (P1) is recovered.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Clamp formula w(k) = sgn zeta(k) min(M, C r(k)) | PROVED (+numerics) | 1.1 |
| 2 | Convergence of block data along engineered approximants | PROVED | 1.2 |
| 3 | First-order identity at NA points; two-regime assembly; averaging over scales at a fixed point | PROVED | 1.3–1.5 |
| 4 | One-sided admissibility => kappa <= 1 | PROVED | 1.7 |
| 5 | **Engineered recovery of d-neutral two-piece mates** (any K, any split; one block, or (S)) | PROVED (+finite-model check) | 2.1 |
| 6 | A_referee §5.4 and P1 6.3 rigorous; slab and explicit defect mates of P1's example in Ls(f) | PROVED | 2.3 |
| 7 | Shifted two-piece data; all of C(f) at P1's example | SKETCH | 2.4 |
| 8 | Mixed term: formula; absorbed (1 piece), cancelled by steering (2 pieces) | PROVED | 3.1 |
| 9 | Consistency identity for families of transported decompositions | PROVED | 3.2 |
| 10 | Garbage identity for Delta d != 0 | PROVED | 3.3 |
| 11 | Delta d != 0 at block-tame active blocks (finite Qbar, (MS), tuning span) | SKETCH | 3.4 |
| 12 | Replication identity (exact |C'-C| and ||R*(w'-w)|| bounds) | PROVED | 4.1 |
| 13 | Retuning feasibility = restricted radius (duality) | PROVED | 4.2 |
| 14 | Abstract replication–averaging–transfer scheme | PROVED (implication) | 4.3 |
| 15 | Requirements for scale-dependent mates; (QI) | identities PROVED / necessity HEURISTIC / (QI) OPEN | 4.4 |
| 16 | C's implant-scale-gap heuristic as an obstruction | FALSE (Thm 2.1 is a counter-instance) | 4.5 |
| 17 | Residual class R1–R5 | OPEN | 4.6, 3.5 |

