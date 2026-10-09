# Y4 part 4 — The remaining step, relation to Round 5 / Round 6, labels

## 4.1 Why (UN+) is the right residual, and what Conjecture G_ray would have to say
 (a) PROVED (from Parts 1-2): at a clean sub-window of D^PW the only coarse objects whose tiny regime is not handled by
     closing moves, removal (Lemma 1.8), compensation by a robust ray of the opposite sign, raising (Lemma 2.6/Prop. 2.7),
     the anti-sign threshold lemma (Lemma 2.9) or Y2's threshold-raising donors, are rays of tiny POSITIVE d-sum in blocks
     whose zero-cost cone has no robust negative ray.  Exact d-neutral data then require either dropping their switching
     or lowering their d-sums.
 (b) HEURISTIC (un-switching analysis).  Rays of tiny d-sum are the EASIEST to un-switch: moving the ray component of one
     side from the base (where it is free at first order) into the block coordinates of the ray's carriers changes the
     block's uniform shift only by (amplitude) x D_r (tiny) and changes the levels at first order only by terms
     proportional to D_r.  The obstruction to un-switching is purely second order: the one-sided (base) carriage has
     quadratic cost ~ t^2 mu^2 q_0 h(V_r)/2, the two-sided (block) carriage ~ t^2 mu^2 sigma_m H_m(omega_r)/2, and a mate
     whose optimal one-sided coefficient is strictly below its balanced coefficient (Remark rem:onesided(b), gamma^+ <
     Gamma_w) genuinely prefers switching.  With slack (1 - rho^2) t^2/2 (the mate is rho g) a fraction of the switching
     can always be removed; full removal at O(t) error needs the switching amplitude through such rays to be O(t), which is
     Conjecture G_ray.  For single modules the switching is a transient band (N3, Z6 R4) because the module is a finite
     certificate at small scales; for general mates (infinite module sums, persistent gamma^+ < Gamma_w) it is OPEN.
 (c) Statement.  CONJECTURE G_ray (OPEN).  For the design D^PW, F finite, a clean sub-window w of level l and a block m
     whose zero-cost cone at level l has no ray r with d-sum <= -u(w) D_norm(r), every g in C(f) admits, at every dyadic
     scale t of w, a two-sided decomposition at scale t whose switching through the rays of d-sum in (0, b(w)] has
     l_1-size <= C(f) Design(l) t.
     Under Conjecture G_ray, these rays are pinned with design constants at clean sub-windows and the residual (UN+)
     disappears; the remaining items are then: the assembly of Theorem E + Proposition T + Theorems A''/U'/Y at tuned rows
     on clean sub-windows (SKETCH), multi-block rays (m'), Y2's aligned corner and coherent shift resonance, and (O4).

## 4.2 Relation to the other Round-5/Round-6 work
 * Z3 / Z3-referee: Proposition 1.2 and Theorem 1.6 extend the referee's band-disjointness (Prop. 4.2.1) from one rate per
   carrier to any design-countable family of rate objects (pigeonhole sub-windows).  Lemma 2.3 is the "growing-support
   Lemma U" that the Z3 referee called plausible; it removes the |F| - 1 limitation of re-tuning (Z3 4.3(iii)) in the
   raising direction, and Proposition 2.8 shows the limitation is genuine in the lowering direction for diagonal bases.
 * Z6 / Z6-referee: (UN+) is the direction-refined form of the K_nn item; N3 adds evidence for Conjecture G in a MIXED
   (ray) configuration, with the switching size independent of the d-sum over three decades.
 * Y2 (Round 6): Y2's donors (z-moves on unused signature sets) raise block thresholds and rescale d-coefficients by a
   common factor; Remark 2.8' is the base analogue (masses on donor contacts rescale all Hilbert parts by a common factor).
   Y2's Theorem M reduces item (m) to a face Farkas rate K_F^rel whose nearly-neutral part is exactly (UN+); our Lemma 1.8
   (ray removal) is the single-block special case of that reduction with an explicit constant 1/D_min, and Proposition
   2.8 explains why the nearly-neutral part cannot be removed by tuning (diagonal bases).  Y2 settles (P+) (degenerate
   swallowing-type peaks) by threshold raising, except its aligned corner.

## 4.3 Labels
| # | Statement | Label | Where |
|---|---|---|---|
| 1 | Explosive design + Cantor pairing: per-carrier rates (R types) block <= R N((2L)^{1/2}+1) windows in [1,L] | PROVED | 1.2 |
| 2 | Ray d-sums dominated by per-carrier d-coefficients in one-signed blocks (up to design factors) | PROVED | 1.3 |
| 3 | A diagonal row blocks every window of the explosive design through ray d-sums | OPEN (HEURISTIC: plausible) | 1.3 |
| 4 | D^PW admissible, N-free; all window theorems survive on sub-windows | PROVED (by inspection, as Z3-ref 4.1.1) | 1.4-1.5 |
| 5 | Clean sub-windows at every level for every f and every design-countable rate scheme | PROVED | 1.6 |
| 6 | No first row beats every window through rates (band/rate items are design artifacts modulo exactification) | PROVED (as stated) | 1.7 |
| 7 | Ray removal: dist_1(tau, C cap ker D) <= |D(tau)|/D_min | PROVED | 1.8 |
| 8 | Multi-block rays: joint d-objects | OPEN | 1.8 Limitation |
| 9 | Cost of tuned rows: p*(f^tau - f) <= C mu log(e/mu) | PROVED | 2.2 |
| 10 | Lemma U / Theorem E with banked support (contact-like data) | PROVED (by inspection) | 2.3 |
| 11 | Joint injectivity of channels on Y; design-constant version | PROVED | 2.4, 2.5 |
| 12 | Raising lemma (a + mW raises W(zhat) at rate ||P^perp U^*W||^2/nu) | PROVED (+ numerics N1) | 2.6 |
| 13 | Exact tuning under the cone condition (TC) | PROVED | 2.7 |
| 14 | Diagonal bases cannot lower z-signed functionals at first order (only |F| - 1 channels) | PROVED (+ numerics N1) | 2.8 |
| 15 | Second-order global rescaling by donor contacts | PROVED | 2.8' |
| 16 | Anti-sign threshold lemma (tau <= lambda(3 gap/t + |Delta d| M)) | PROVED | 2.9 |
| 17 | Reductions (i)-(iii) of 2.4 at clean sub-windows (rooms, anti-sign carriers, compensated/raisable d-rows) | PROVED as reductions; assembly SKETCH | 2.4 |
| 18 | Directional residual (UN+) | OPEN | 2.4(iv), 4.1 |
| 19 | Convexity in the first row; locality of Lemma Z | PROVED (elementary) | 2.5 |
| 20 | Finite-model lsc along tuned rows | numerics (trivial, degenerate) | N2 |
| 21 | Switching through a tiny positive ray independent of its d-sum | HEURISTIC (numerics N3) | N3 |
| 22 | Conjecture G_ray | OPEN | 4.1(c) |
| 23 | Un-switching analysis (second-order obstruction only) | HEURISTIC | 4.1(b) |
| 24 | Lowering channels with design conditioning for mixing bases | OPEN (HEURISTIC: plausible) | 2.4(iv) |
FALSE: nothing new.  Corrections to earlier statements: Z3 7.1 "the band defeats every window method" is false for the
pigeonhole design (and for per-carrier rates already for the explosive design, Z3-referee); the claim of the first draft of
this report that exact neutralization by masses removes K_nn is FALSE for positive d-sums with a diagonal base (Prop. 2.8),
corrected in the final text.
