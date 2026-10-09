# Z1 notes — Lemma Z for the signature-ladder design: what is proved, and the precise remaining step

Round 4, task Z1. Setting: canonical base q; Martin's norm with a FINITE block set I_N (norms p_N, every N; Remark martin-tail, proved in
G3_referee sec. 4, transfers density for all p_N to Martin's p). T = SLD operator of G3 1.2, with one harmless design adjustment (min S_l strictly
increasing, part 3 preamble; Theorems A-C of G3 unaffected). Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Part files Z1_part1..5.md
(assembled below). Numerical sanity checks of the three scalar inequalities used (1.3, 2.1, 2.4(b)): all hold (max violation <= 0).

## 0. Answer
**Lemma Z is NOT proved.** No counterexample is suggested either. What is proved:
 * Lemma Z (and density) needs to be shown only for mates that are NOT window-pinned (Theorem B*, 1.5): G3's proof of Theorem B uses the
   signature room (SR) only through its conclusion "sum_l |Delta c_l| <= K t on long windows", so every window-pinned mate at ANY f with F finite
   is recovered, whether or not f is in R_0.
 * Infinite base support is not an independent obstruction (4.1 PROVED flip lemma; 4.2 Theorem B^inf SKETCH, its only unproved ingredient is the
   import of C Thm 7.4 for a not in c_00, b in c_00 from the C referee).
 * The referee's route (lower |z| on far parts of swallowed signature sets) necessarily creates a transition band [theta, sqrt(theta)] in which
   f' must reproduce f's switching EXACTLY (3.1); a better family of approximants (lower whole FINE signature sets, keep the coarse ones; 3.2)
   reduces Lemma Z to (A) "finitely-swallowed points are in R" and (B) lower semicontinuity along those approximants (3.3), both OPEN.
 * At finitely-swallowed points the free switching is bounded (4.3, PROVED), and with exact free resources everything reduces to ONE algebraic
   obstruction (5.2, PROVED): the + and - window components cannot be made to represent the same functional because their difference is an
   unsigned O(K t) junk on the swallowed contact set; G3's averaging and S3's Theorem D both need one functional (3.4 (O-c): the naive combination
   fails by the arithmetic K t_1/n >> t_1^2 4^{-n}).
 * Tools: exposed-face lemma (1.2: no approximant f' != f can contain rho C(f) exactly), ray lemma (2.3: a decomposition is reusable at smaller
   scales iff its first-order defect Delta1 vanishes; Delta1 collects near-contacts, weak peaks, flips, wrong-signed contacts).

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | R_0-approximants exist for every f (canonical truncations, far lowerings); Lemma Z is purely a lower-semicontinuity statement | PROVED | 1.1 |
| 2 | Exposed face of B_{p*} at the normer of f is {f}; hence rho C(f) subset C(f') with f' in S_{p*} forces f' = f | PROVED | 1.2-1.3 |
| 3 | Local reduction (P2A 1.4 valid for non-NA f') | PROVED | 1.4 |
| 4 | **Theorem B*: window-pinned mates at any f with F finite are in Ls(f)** (SLD T) | PROVED (by inspection of G3) | 1.5 |
| 5 | Ray lemma: one-sided reuse of a scale-t decomposition on (0, t/2] with first-order defect Delta1(t) <= t/2 | PROVED | 2.1-2.3 |
| 6 | Dichotomy Delta1 = 0 (exact resources: reusable on the whole ray) / Delta1 > 0 (useful only near scale t); averaging needs two-sided objects | PROVED | 2.4 |
| 7 | Far lowering of a coarse swallowed set: pinning only below theta_n ~ 2^{-n}; transition band [theta_n, sqrt(theta_n)] needs exact transfer | PROVED (a,b,d) / HEURISTIC (c: size of p*(f'-f)) | 3.1 |
| 8 | Approximants f^L (lower whole fine signature sets): f^L -> f, coarse data kept, fine carriers fully roomy | PROVED | 3.2 |
| 9 | Reduction: (A) R_fin subset R and (B) lsc along R_fin approximants imply density | PROVED (A, B OPEN) | 3.3 |
| 10 | Window split Cert + Free_+- + O(Kt) at points with finitely many free carriers | SKETCH | 3.4, 5.1 |
| 11 | Window averaging + S3 Thm D cannot be combined naively (scale arithmetic) | PROVED | 3.4 (O-c) |
| 12 | Flip lemma on infinite F: near-flips pinned like contacts | PROVED | 4.1 |
| 13 | Theorem B^inf: (SR) points with infinite F are in R | SKETCH (one import) | 4.2 |
| 14 | Bounded free switching through a finite free set U* (uses Y cap c_00 = {0}, T injective) | PROVED | 4.3 |
| 15 | Common-functional obstruction: unsigned O(Kt) junk on the swallowed contact set | PROVED (algebra) | 5.2 |
| 16 | Lemma Z | OPEN | 3.4, 5.3 |

## Precise remaining step
Either of the following would finish the proof of density for the SLD T (with 1.5, 3.3, 4.2):
 (RS1) [finitely-swallowed points] For f with F finite whose non-roomy signature sets are those of a finite slaving-closed set U* of carriers,
       and every g in C(f): on a sequence of long windows, choose the two side decompositions at each window scale so that the + and - components
       (5.1) represent the same functional up to a two-sided O(K t) certificate (equivalently: the contact junk J_t of 5.2 can be made -z-signed
       modulo span{u_l 1_{K_*}}), and handle near-resources on the swallowed sets (Delta1 > 0, 3.4 (O-a)). Then the averaged object is ONE
       functional with exact two-piece data plus a two-sided certificate, recovered by S3 Theorem D (Delta d >= 0; (SC) otherwise).
 (RS2) [lower semicontinuity] Along the approximants f^L of 3.2 (or any R_fin / R_0 approximants), rho C(f) is contained in Li C(f^L): i.e. the
       switching of g through FINE swallowed carriers (amplitude <= 6 lambda_l/t at scale t, 3.2(d)) can be removed at f^L, where those
       carriers are pinned, below the slack scale sqrt(c_{L+1}).
Both are instances of the Round-2 open core O3 (scale-dependent switching), now localised to signature sets of finitely many carriers (RS1)
or to box-bounded fine carriers (RS2). Leaning: positive (density); nothing found suggests a counterexample.
