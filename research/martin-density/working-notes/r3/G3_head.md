# G3 notes — a designed admissible T for which every first row with "signature room" is recovered; reduction of density to one base-side lemma

Round 3, task G3. Setting: canonical base q; Martin's norm with a FINITE block set I_N = {1..N} (the norms p_N, every N >= 1; Preprint B
Remark martin-tail reduces density for p to density for all p_N). T is DESIGNED (only Lemma B's conclusion is required of T by Martin's
proof of algebraic triviality; our T satisfies it, 1.3). Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Part files: ctx/r3/G3_part1.md ..
G3_part6.md (assembled below). Imports (refereed, Rounds 1-2): A Facts A-F, A Lemmas 4.3, 4.4, 4.7, 7.1, 7.2, A Prop 2.1, the proof of A Thm 6.8;
C (7.2), C (7.3), C Thm 7.4 (and C Cor 7.2(c)).

## 0. Answer and summary
**The full theorem (density for some admissible T and every p_N) is reduced to ONE explicitly stated lemma about the base side (Lemma Z),
which is in fact equivalent to density for the designed T. Everything else -- in particular the four open-core items O1-O4 -- is PROVED for
the designed T at every first row f in the dense class R_0.**

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Theorem A: the "signature-ladder design" (SLD) T is admissible (norm one, injective, Ran T cap c_00 = {0}, each block dense in S_{q*}); private signatures delta_l h_l on disjoint S_l, coarse-to-fine allowedness of targets, one ladder through all blocks, super-fast weights with long windows of scales | PROVED | 1.2-1.3 |
| 2 | Class R_0 := {F = supp a finite and (SR): ||h_l 1_{S_l cap J_gamma}|| >= vartheta^l ||h_l|| for all l}; contains all NA points and all base-tame points; allows infinite contact sets, near-contacts, arbitrary blocks | PROVED (definitions/inclusions) | 1.1, 1.4 |
| 3 | Two-sided decompositions: uniform smallness, first-order terms O(t), one-sided base bounds, weighted budget Gamma_w <= 1 + o(1), sup-level parametrization of blocks | PROVED (any admissible T) | 2.1-2.5 |
| 4 | Signature pinning: delta'_l |Delta c_l| <= E_l + sum_{l'>l} kappa |Delta c_{l'}|; triangular solution; sum |Delta c| <= K_1 Lambda_f(l_*) t on window scales; contact/near-contact switching and uniform shifts pinned | PROVED | 3.1-3.5 |
| 5 | Window certificate: on every window scale a balanced finite certificate c_t with radius ~ t, ||g - g_{c_t}|| <= K_2 Lambda_f t, Gamma_w(c_t) <= 1 + o(1); one-sided excesses bounded by two-sided differences | PROVED | 4.1-4.2 |
| 6 | Uniform transfer expansion: p*(f + s g_c) <= 1 + (s^2/2)(Gamma_w(c) + eps) for |s| <= c_1 t, uniformly over window-type certificates (C Thm 7.4 at f, made uniform) | PROVED | 5.1 |
| 7 | Windowed averaging: certificates on ONE window of n >= C K dyadic scales suffice; recovery via C Thm 7.4 | PROVED | 5.2 |
| 8 | **Theorem B: for the SLD T and every N, R_0 is contained in R (every mate of every f in R_0 is recovered)** | PROVED | 5.3 |
| 9 | Corollary: for f in R_0, C(f) = closure of the Gamma_w <= 1 balanced finite certificates in C(f) (no intrinsic defect) | PROVED | 6.4 |
| 10 | **Theorem C: for the SLD T, density of NA((c_0,p_N), l_2^2) <=> Lemma Z** | PROVED | 5.4 |
| 11 | **Lemma Z: every (f, rho g) is approximated by (f', g') with f' in R_0, g' in C(f')** (base-side engineering only; approximants need not be NA) | OPEN (the single missing lemma) | 1.1, 6.3 |
| 12 | Lemma Z for mates covered by Round-2 engineering (exact two-piece mates under their hypotheses) | PROVED (by import) | 6.3(a) |
| 13 | Extension of Theorem B to infinite base support F (with (SR)) | SKETCH | 6.3(e) |
| 14 | Finitely many unpinned carriers = exact-resonance structure up to O(K t) on windows; route to Lemma Z there | HEURISTIC / OPEN | 6.3(d) |
| 15 | Density for Martin's own (unknown) T | not addressed (OPEN) | 6.1 |

Key ideas. (1) PINNING: if every block vector u_l carries a private signature delta_l h_l on coordinates where the first row has room,
then for ANY two admissible decompositions of a mate (the two sides of t = 0) the difference of the coefficient of u_l is controlled by
base mass on its signature, which costs first order and is O(t) (3.2). Contacts, near-contacts, peaks and near-threshold carriers are
one-sided resources, and every one-sided usage is bounded by a two-sided difference (2.3(b), 4.2(c)), hence pinned. (2) WINDOWS: the price
of pinning (1/delta' per level, amplified triangularly by finer targets touching coarser signatures) is a constant Lambda_f(l_*) that
depends only on the coarse levels; a super-fast ladder of weights creates windows of scales in which the finer carriers are negligible and
which contain >> Lambda_f(l_*) dyadic scales. (3) A's averaging over scales needs certificates only on one window of n dyadic scales.
(4) The budget identity controls exactly C's mass-weighted invariant Gamma_w, and transfer peaks (C Thm 7.4) realise it uniformly, so no
second-order rebalancing problem remains. (5) Since NA points lie in R_0, the remaining problem (Lemma Z) is equivalent to density and
concerns only first rows whose base one-sided resources swallow signature sets (P1's exact resonance is of this type) or whose base
support is infinite.

Leaning: positive (density). No counterexample is suggested by anything here; Theorem B removes every block-side mechanism of the open core.
