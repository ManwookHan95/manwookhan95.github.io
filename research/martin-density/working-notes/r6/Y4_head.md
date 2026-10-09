# Y4 notes (Round 6): "exactness vs scale" — diagonal first rows, tuning channels, and the directional residual

Setting and notation: paper/martin_density_note.tex (Sections 1, 7, 8) and the refereed Round-5 reports (Z3 Theorem E,
Lemma U, Lemma 3.1, Proposition T with the Z3-referee fixes and the explosive design (D1^F); Z4 Theorem A with (H2'');
Z6-referee design D''' and Theorem U'; Z6 2.4, Conjecture G).  Finite block set I = {1..N}, p = p_N, F = supp a finite
unless said otherwise.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Part files: Y4_part1.md (task (a)),
Y4_part2.md (task (b)), Y4_part3.md (task (c)); scripts in Y4_work/.  No counterexample is claimed; nothing found points to
one.  Lemma Z and density remain OPEN for every admissible T.

## 0. Summary

**(a) Can a diagonal first row beat every window?**
* Explosive design (Z3_ref (D1^F)) with the Cantor pairing as ladder bijection: NO through PER-CARRIER rates.  For any
  first row and any values of R per-carrier rate types (rooms, target rooms, threshold distances = relative margins/gaps,
  relative d-coefficients), at most R N((2L)^{1/2} + 1) windows in [1,L] are blocked (Proposition 1.2, PROVED).
* JOINT rate objects (d-sums of zero-cost rays in MIXED blocks; Farkas/Hoffman data of finite systems) are exponentially
  many per level and the counting fails (Observation 1.3).  In one-signed blocks ray d-sums are dominated by per-carrier
  rates (PROVED).  Whether a diagonal row can block every window of (D1^F) through ray d-sums is OPEN (HEURISTIC: plausible;
  a nested intervals construction in the |F| - 1 base parameters is the natural attempt).
* Pigeonhole design D^PW (Definition 1.4): every level l has M(l) = omega(l) + 1 sub-windows with globally disjoint
  bands, omega(l) a design bound for the number of rate objects of level <= l.  D^PW is admissible, N-free, and every
  window theorem of the note and of Round 5 survives (Lemma 1.5, PROVED).  Every first row has, at EVERY level, a clean
  sub-window at which every rate object is robust (>= u) or tiny (<= b), with robust products absorbed and tiny objects
  exactifiable at cost theta T_lo^2, theta -> 0 (Theorem 1.6, Corollary 1.7, PROVED).  So no first row can beat every
  window through rates: the BAND obstruction and item (r) are design artifacts — modulo the exactification of the tiny
  objects, which is where the real difficulty moves (below).
* d-rows are controlled by ray rates without any compensator: removal of a fraction of the rays of the sign of the
  mismatch costs |mismatch|/D_min (Lemma 1.8, PROVED; single-block rays; multi-block rays need joint objects, OPEN (m')).
* Diagonal candidates: mixed blocks with "ray modules" switching through rays of tiny d-sum; not recovered by any proved
  mechanism for (D1^F); for D^PW they reduce to the directional residual (UN+) below (1.6, HEURISTIC description).

**(b) Non-window tools.**
* Tuned rows (banked companions): masses at contacts, changes of a on F, z-moves at free coordinates; cost
  C_f mu log(e/mu) (Lemma 2.2); Z3 Lemma U and Theorem E hold with banked (growing) support for contact-like data (Lemma
  2.3) — this removes the |F| - 1 limitation of Z3 4.3(iii); channels are jointly injective on Y (Lemma 2.4) with
  design-constant conditioning (Lemma 2.5); the RAISING LEMMA (Lemma 2.6): adding mW to a raises W(zhat) at the rate
  ||P^perp U^*W||^2/nu for every z-signed W; exact tuning under a cone condition (Proposition 2.7).  All PROVED.
* DIRECTIONAL OBSTRUCTION (Proposition 2.8, PROVED): masses at contacts can always raise a z-signed functional; with a
  diagonal base they can never lower it to first order, so lowering is limited to the |F| - 1 two-sided channels on F (and
  one global second-order rescaling, Remark 2.8').  Generic bases do have first-order lowering channels (numerics N1).
* Anti-sign threshold lemma (Lemma 2.9, PROVED): swallowed q < 0 strict non-peaks of tiny gap are pinned like anti-sign
  peaks; the gap rate gamma_B is harmless in both regimes.
* Consequently exactification has a favourable direction (close rooms and target rooms; raise negative tiny d-sums; drop
  anti-sign threshold carriers; raise thresholds — Y2's donors) and an unfavourable one: LOWER a tiny POSITIVE d-sum.
  The sharp residual is
     (UN+) a block whose zero-cost cone has no robust ray of negative d-sum, while the mate switches persistently through
           rays of tiny positive d-sum (nearly neutral, positively d-coupled directions),
  which is Z6's K_nn and the nearly-neutral part of Y2's face Farkas rate K_F^rel, now identified as a DIRECTION problem.
* Non-window viewpoints: convexity of {h : (h, rho g) contractive} (PROVED, not usable directly because the forced-data map
  is not affine); locality (PROVED: Lemma Z is local at f' on the scales |r| <~ p*(f' - f)^{1/2}); Baire (nothing new);
  multi-level companions need no compatibility between levels (Theorem E builds the approximants directly).

**(c) Numerics.**  N1: diagonal bases never lower (0 of 300 x 38 contacts), mixing/random bases lower at ~half of the
contacts; raising derivative confirmed to 2e-8.  N2: lower semicontinuity along tuned rows is trivial in finite models
(dist ~ 7e-4 x cost), as expected (degenerate).  N3: in a finite (UN+) model the forced switching through a ray of tiny
positive d-sum is a transient band of height ~1.4e-2 t that does NOT grow as the d-sum decreases over three decades
(1.54e-2, 1.45e-2, 1.38e-2, 1.37e-2): evidence for a RAY version of Z6's Conjecture G, i.e. that (UN+) is an artifact of
the 1/D pinning bound rather than of the geometry (HEURISTIC).

**Bottom line.**  The "exactness vs scale" obstruction is NOT intrinsic as a RATE phenomenon: a pigeonhole window design
gives every first row clean sub-windows at every level.  What remains for the companion/window route is DIRECTIONAL:
exactification sometimes requires lowering z-signed functionals, which cheap moves cannot do (diagonal bases), and the
corresponding mates must then be shown to need no switching through those directions (Conjecture G_ray).

**Precise remaining step.**  Prove Conjecture G_ray: in a block whose zero-cost cone at level l (of a clean sub-window) has
no robust ray of negative d-sum, at every scale t of the sub-window some two-sided decomposition of g switches through the
rays of tiny positive d-sum by at most C Design(l) t.  Together with Theorem 1.6, Parts 1-2, Y2 (donors, Theorems P, M, H)
and Round 5 (Theorem E, Proposition T, Theorems A'', U') this would leave only the assembly (SKETCH), the aligned corner and
the coherent shift resonance of Y2, multi-block rays (m'), and (O4) infinite F.  Alternative route: a mixing base with
lowering channels of design-bounded conditioning (transversality; OPEN).
