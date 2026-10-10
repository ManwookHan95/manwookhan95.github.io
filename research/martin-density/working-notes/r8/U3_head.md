# U3 notes (Round 8): adversarial and structural analysis of the residual (C*) — near-exact coherent shift resonance

Setting: paper/martin_density_note.tex (notation as there), finite block set I = {1..N}, p = p_N; design D^{V2} on V1's D_Omega with
diagonal base (plus V4's design conditions (SF*), (SF_tau), (b'), (Z0) where cited, and one harmless weight strengthening (W10) in
Part 4); F finite unless said otherwise.  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Part files: r8/U3_part1..5.md
(this file = U3_head + parts 1-5, byte-identical copies).  Scripts: r8/U3_work/{nl_check.py, nl_check2.py, vt_check.py}.
No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN (two precise steps left, Part 4.3/4.3').

## 0. Summary of the answers
(a) Construction.  The suggested route — perturb V4's self-aligned rows Baire-generically in their fixed-z fibre so that (BT) fails while
    (C*) persists — does NOT work: every tilting perturbation of a in a fixed-z fibre of an aligned row creates, in EVERY block,
    infinitely many exactly swallowed robust ANTI-type peaks (and keeps swallowing-type ones), i.e. both shift sources at every clean
    sub-window of every large level; such rows leave (C*) and are recovered by Master Theorem III' (Proposition FZ, Corollary FZ:
    PROVED).  Genuine non-(BT) (C*) rows exist nevertheless: the NESTED-TUNING rows f^infty (Theorem NT) — maximal contact, all
    carriers aligned except the q<0 carrier l_- of Construction SA, and infinitely many ALIGNED near-threshold strict non-peaks obtained
    by anti-owner signs and a nested choice of a; they fail (BT) and even (SC), and have rho^sh = 0 and c_pi = 0 at every clean
    sub-window of every large level (properties PROVED; existence SKETCH).  Their most dangerous mates — oscillating profiles on robust
    class-G peak signature sets, forced shift Delta < 0 — carry EXACT two-piece data (Proposition NT-M, PROVED; g in C(f) verified via
    Proposition prop:onesidedupper).
(b) Recovery.  The exact-data mates of f^infty are recovered (Corollary NT-R: PROVED modulo V4 Theorem 5.6, refereed, and the
    assumed design compatibility of V4's conditions with D^{V2}).  The general mate of f^infty, and every (C*) row, reduce to two
    precise steps (S1) coupling exactness and (S2) uniform composition of violation-tolerant engineered approximants (Part 4); for
    f^infty and for every single-shifted-
    block (C*) row with a free-ray q<0 carrier, (S1) holds (PROVED), so only (S2) remains.  The new mechanism that removes V2-ref's
    gaps (C*-1), (C*-4), (C*-5) is QUADRATIC BANK REPAIR (Lemma QB2, PROVED): a sign violation of l_1-mass epsilon at contacts is
    converted into a second-order cost by banks of total mass ~ epsilon^2/beta, so fine-origin violations (mass <= C T_lo^3, and
    <= C T_lo^{10} under (W10)) cost o(T_lo^6) — no exact absorption and no Slater condition are needed; the tail, including free
    coordinates, is handled by VIOLATION TOLERANCE of the engineered approximants (Lemma VT, PROVED at a single stage by a line-by-line
    modification of the proof of Theorem thm:engineered: a violation of l_1-mass epsilon costs at most 2 rho |tau| epsilon, only in the
    regimes |tau| > s_1, and is absorbed when 2 rho epsilon <= delta s_1/16).  What remains of (S2) is UNIFORMITY of the engineered
    construction along companions, made precise as (S2a)-(S2d) in Part 4.3'.
    Lower semicontinuity: along SOME (BT) sequences (V4's aligned re-alignments) the exact-data mates of f^infty are recovered, but
    lower semicontinuity of the fibre map FAILS along other (BT) sequences, even at a (BT) row: Theorem NL (PROVED) gives (BT) rows
    f_n -> f_SA (one far carrier flipped to an anti-type peak) with liminf dist(rho g, C(f_n)) > 0 for every oscillating mate g.  The
    mechanism is an exact rigidity of two-piece data (Lemma S, Corollary S1, Proposition S3: PROVED): with one block, a single
    anti-aligned contact or free coordinate outside the omega-supports forces Delta = 0 and a CONSTANT profile for every mate.
(c) The quantitative property.  Non-recovery of (C*) would require one of: (i) failure of (S1): the coupling rows Delta_m =
    d_m(omega^-) - d_m(omega^+) cannot be made exact inside the (exact, by V2 Cor. C1.1(a)) combinatorial resonance cone with a
    design-controlled constant — only possible with >= 2 shifted blocks or without a free-ray q<0 carrier; (ii) failure of (S2):
    non-uniformity of the engineered construction along the companions — the late-stage threshold s_late(f^#_w) falling below
    32 rho epsilon_w/delta (epsilon_w = fine-origin violation mass), or T_0 not scaling like the piece radius c_flat t — or in-window free
    violations with b^+(j) b^-(j) > 0.  The violation cost itself is harmless at every single stage obeying 2 rho epsilon <= delta s_1/16
    (Lemma VT, PROVED); the tail term (1/2) rho |tau| V_{>N''} of thm:engineered is absorbed the same way.  Finite SOCP models confirm the exact
    rigidity (oscillating part of the local fibre collapses from 1.6e-2 to 2.4e-8 under a far anti-type flip of norm 8.3e-7) and the
    quadratic bank law (least repairing bank mass / epsilon^2 = 0.83, 0.79, 0.75, 0.71 vs predicted rho^2 = 0.81); the window mass that
    Lemma VT places at a violated contact, 4 rho s_1 |b^theta_j| with s_1 >= 32 rho epsilon/delta, obeys the same quadratic law.

## 1. Results and labels
| # | Result | Label | Part |
|---|---|---|---|
| 1 | Lemma S (exact rigidity/sandwich of two-piece data, any coordinate outside the omega-supports) | PROVED | 1.1 |
| 2 | Corollary S1 (one block: profile constant unless shifted; anti-aligned/free coordinate forces Delta = 0) | PROVED | 1.2 |
| 3 | Corollary S2 (F, K finite, e.g. NA rows: no switching, no shift) | PROVED | 1.3 |
| 4 | Proposition S3 (necessary condition for following a non-constant profile along rows with exact data) | PROVED | 1.4 |
| 5 | Theorem NL (fibre map not lsc at f_SA along (BT) rows; oscillating mates lost) | PROVED (uses V4 Thm 2.2, Prop 3.2, Prop 5.3, refereed) | 1.5 |
| 6 | Lemma D' (shape of source-deficient blocks) | PROVED (V1 Lemma D, Lemma S(a)) | 2.1 |
| 7 | Proposition FZ (fixed-z tilts create anti-type and swallowing-type robust swallowed peaks in every block) | PROVED (any admissible T) | 2.2 |
| 8 | Corollary FZ (fixed-z tilts of aligned rows leave (C*) and are in Rec) | PROVED mod Master Theorem III' | 2.3 |
| 9 | Lemma A (one block: existence of shifted exact data = Omega-coherence of psi) | PROVED | 2.4 |
| 10 | Theorem NT (non-(BT), non-(SC) rows in (C*)): existence | SKETCH | 3.1 |
| 11 | Theorem NT: properties (b)-(e) given (a)-(c) incl. rho^sh = 0, c_pi = 0 | PROVED | 3.1 |
| 12 | Proposition NT-M (explicit oscillating coherent-shift mates of f^infty, exact data, c g in C(f)) | PROVED | 3.2 |
| 13 | Corollary NT-R (these mates are recovered) | PROVED mod V4 Thm 5.6 + design compatibility | 3.3 |
| 14 | Recovery of all mates of f^infty | SKETCH (only the uniform composition (S2) remains) | 3.4, 4.3, 4.3' |
| 15 | Lemma 3.5 (dead-zone bump) | PROVED | 3.5 |
| 16 | Lemma QB2 (quadratic bank repair; uniform flip bound) | PROVED | 4.1 |
| 17 | Lemma VT (violation tolerance of engineered approximants, single stage) | PROVED (modification of the proof of thm:engineered) | 4.2 |
| 18 | Proposition RT* (a),(b),(d),(f) / (c),(e) | PROVED / SKETCH | 4.3 |
| 19 | (S1) for a single shifted block with a free-ray q<0 carrier | PROVED | 4.3 |
| 20 | (S2a) uniform per-piece engineered bounds, (S2b) averaging at the engineered approximant, (S2d) free violations | SKETCH | 4.3' |
| 20' | (S2c) threshold comparison s_late(f^#_w) >= 32 rho epsilon_w/delta under (W_k) | HEURISTIC | 4.3' |
| 20'' | (S1) in general; (S2) as a whole (uniform composition) | OPEN (precise) | 4.3, 4.3' |
| 21 | Numerics (rigidity collapse; quadratic bank law) | sanity checks | 5 |

## 2. What is used
Note: Sections 1, 7, 8 (lem:threshold, lem:bookkeeping, lem:base, def:twopiece, prop:onesidedupper, thm:onesided, def:BT, def:SC,
thm:engineered and its proof, cor:D1, cor:BTrecovered, lem:switchbudget, lem:suplevel, lem:peakshift, rem:lemmaZ(c), def:SLD,
lem:rigidity).  Refereed: V4 Construction SA / Theorem 2.2 (with R3), Proposition 3.2, Proposition 5.3 (hysteretic re-run), Lemma 5.2,
Theorem 5.6 with Lemmas 5.4, 5.5; V1 Lemma D, Lemma S(a), Lemma 3.4', donor raise and assembly; V2 Theorem C1, Corollary C1.1(a),
Lemma 3.1, Theorem E^SC; Z3 Theorem E, Lemma U; Y1 Lemmas 3.2-3.5 and the source definitions.  New design input: (W10)
c_{l+1} <= T_lo(l)^{10} (an upper bound on weights; admissible as in V4 Lemma 2.1) — used only in Part 4.3(f).
