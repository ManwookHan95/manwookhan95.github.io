# N1 notes — Should the answer be NEGATIVE? What a non-density proof must establish, the shape of a counterexample, and an assessment

Track N1 (negative direction), after 14 rounds of positive attempts. Sources: Part I (paper/martin_density_note.tex, cited
[I, label]), Part II ([II, label]), Part III, refereed round notes (r1-r13), G3 (r14; its Section 2 and Lemma 3.1/Cor 3.2 refereed correct). Part files:
neg/N1_part1.md (formulation), neg/N1_part2.md (necessary conditions), neg/N1_part3.md (mechanisms, verdict); scripts in
neg/N1_work/. This file = summary + the three parts (authoritative) + numerics + next steps.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Proofs are complete for every item labelled PROVED here; items PROVED elsewhere
are cited.

## 0. Summary and answer to the question of the track

QUESTION (user): "After this much effort without a proof, shouldn't we approach the problem negatively?"

ANSWER. Not wholesale. The evidence still (weakly) favours density, and the failure so far is a failure of the explicit
constructions for an ARBITRARY admissible T (their bottleneck is exactness of finite systems solved with one-sided levers), not a
sign of an obstruction: no lower bound for dist(rho g, C(f')) over all norm-attaining rows f' near any f has ever been proved, and
every adversarial configuration built in 14 rounds was recovered by a new mechanism or stayed at model level. A TARGETED negative
test is nevertheless worthwhile, but only with an ADVERSARIAL admissible T (never the designed T_fin, for which a counterexample
would need infinite base support and a failure of (LSC-trunc)), aimed first at a type (I) obstruction (one fixed direction x and,
at every admissible normer x', a cheap multi-scale decomposition of x). Precisely:

(1) Exact target (PROVED, Section 1). With Rec(f) := outer limit of the fibres C(f') along norm-attaining rows f' -> f:
    * Rec(f) is a compact balanced union of compact convex sets, each containing U(f) ⊇ cl Cert^sh(f); the optimal obstruction
      functional is Ob(f, h) := liminf_{NA f' -> f} dist(h, C(f')) = dist(h, Rec(f)); density <=> Rec(f) = C(f) for all f <=> the mate
      graph equals the closure of its part over norm-attaining rows (Prop 1.2, Thm 1.3, Lemma 2.1).
    * A non-density proof must give (f, g in C(f), rho < 1, theta, delta) with dist(rho g, C(f')) >= theta for EVERY norm-attaining f'
      in B(f, delta); such f' are exactly grad p(z' + U(U*a'/||U*a'||)) with (a', z') close to (a, z) on a fixed window and
      ARBITRARY beyond it, with arbitrary tiny "banks" in a' (Lemma 1.4). The defect is then open on the graph (Thm 1.3(iv)).
    * Dual form: dist(h, C(f')) = sup_{p(x) <= 1} (h(x) - r~_{f'}(x)), and at f' = grad p(x') the cost of a decomposition is
      sum_j (beta(y_j)(2p(y_j) - beta(y_j)))^{1/2} with beta the Bregman divergence of p at x' (Thm 1.6): a non-recovery certificate is a
      CHEAP multi-scale decomposition of some x at every admissible normer (p must be flatter at x' than rho g requires).
    * Near (f, rho g), NA is the union over normers x' of the rotated and rescaled convex fibres C(grad p(x')) (Prop 1.5); a
      Hahn-Banach separation of (f, rho g) from (the fattened local part of) NA exists iff there is a TYPE (I) obstruction: one x with
      rho g(x) >= r~_{f'}(x) + theta for all NA f' near f (Prop 1.5bis).
    * Dichotomy (Thm 1.9): non-density <=> (I) some x-exposed mate is unrecovered (a scalar "upward spike" of f -> r~_f(x) relative
      to NA rows, hence relative to all generic rows) or (II) cl conv Rec(f) = C(f) but Rec(f) is not convex (incompatible recovering
      sequences). Mazur's theorem is the key tool. Only scales |t| < t_*(eps, eta, rho) ~ max(eps^{1/2}, eta)/(1 - rho^2) are decisive
      (Prop 1.8).
(2) Shape of a counterexample for an arbitrary admissible T (Section 2, all PROVED from cited refereed results unless marked):
    f non-attaining, outside the comeager set of lsc points, not (BT) (F infinite, or infinitely many strict non-peaks, or degenerate
    peaks, or (MS) fails), not box-dominated; rho g outside U(f) ⊇ cl Cert^sh(f); at cofinal small scales and on BOTH sides no
    "certificate + O(t)" decomposition (contrapositive of [I, cor:decomposition]); no two-piece data with kappa_w <= 1 and Delta d >= 0 or
    (SC); no exact window data at second-order-close rows; switching genuinely scale-dependent (exact resonances are recovered); rho g
    uniformly far from the fibres of ALL recoverable rows nearby (NA, generic, (BT), ...). HEURISTIC (Rounds 1-3): adversarial T with
    error-dominated carriers, far rigidity, escaping and recursively guarded errors (R3's class O3*).
(3) Can one T and one row kill every mechanism (Section 3)? The hypotheses of all PROVED mechanisms can be violated simultaneously
    by pairs (f, g) with g in C(f) (violations are even generic) EXCEPT that mates whose switching is scale-dependent at ALL scales have
    never been constructed. But killing mechanisms is not an obstruction: the approximant's freedom (far data, banks, near-contacts,
    fresh zero-weight carriers, error carrying) is a generator, every NA approximant has a junction at a depth of its own choosing, and
    a counterexample needs a SELF-SIMILAR invariant (bounded conversion capacity with escaping errors, or a one-signed scrambling cost)
    forced at EVERY junction for EVERY approximant. The only approximant-independent one-signed effect proved so far — unavoidable
    common peaks of opposite sign at every NA row, which make the d-mismatch of Delta d < 0 data cost first order on one side (N2 Lemma
    3.3, Cor 3.4) — is first order in a scrambling that the approximant controls. No such invariant is known (missing piece: (CAP+-),
    Section 3.5).

Leaning: POSITIVE (density more likely), low confidence for arbitrary admissible T. Nothing found here is a step toward a
counterexample; nothing found here proves density either.

| # | Result | Status | Where |
|---|---|---|---|
| 1 | Structure of Rec(f); Ob(f,h) = dist(h, Rec(f)); density <=> Rec = C | PROVED | Prop 1.2 |
| 2 | Exact non-density criterion; Ob 1-Lipschitz; openness on the graph | PROVED | Thm 1.3 |
| 3 | Far freedom, uniform form (window + arbitrary far data + banks) | PROVED | Lemma 1.4 |
| 4 | Local structure of NA near (f, rho g) (rotation angle <= 2(delta/(1-rho^2))^{1/2}) | PROVED (+numerics) | Prop 1.5 |
| 5 | Hahn-Banach form: convex separation from the local NA set <=> type (I) | PROVED | Prop 1.5bis |
| 6 | Dual formula; Bregman form of r_{f'}; primal certificate of non-recovery | PROVED | Thm 1.6 |
| 7 | Symmetric two-point curvature bound (also at the bidual normer) | PROVED (+numerics) | Cor 1.7 |
| 8 | Scale localization | PROVED | Prop 1.8 |
| 9 | Convex / non-convex dichotomy; exposed mates; scalar spike form | PROVED | Thm 1.9, Rem 1.10 |
| 10 | graph(Rec) = cl G_NA; Rec(f) = outer limit along ANY recoverable class | PROVED | Lemma 2.1 |
| 11 | Necessary conditions F1-F7, M1-M6, M8 (arbitrary T) | PROVED (cited) | Sec 2 |
| 12 | M7 universal switching constraints / conservation law | PROVED (G3, refereed) | Sec 2 |
| 13 | T1-T3, S2 adversarial requirements on T | HEURISTIC / SKETCH | Sec 2.3-2.4 |
| 14 | Mechanism table; simultaneous violation of all PROVED hypotheses | HEURISTIC (each entry cited) | Sec 3.1-3.2 |
| 15 | Transfer principle: every NA approximant has a junction; obstruction must be self-similar | HEURISTIC (PROVED ingredients) | Sec 3.3 |
| 16 | Candidates C1 (Delta d < 0 without (SC)), C2 (O3*), C3 (type II) | OPEN | Sec 3.4 |
| 17 | Merging lemma (convexity of Rec(f)) as a positive target; (CAP+) / (CAP-) | OPEN | Rem 1.10, Sec 3.5 |
| 18 | Existence of a counterexample; density for any p_N or p | OPEN | - |

