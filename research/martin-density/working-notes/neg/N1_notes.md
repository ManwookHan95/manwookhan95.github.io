# N1 notes — Should the answer be NEGATIVE? What a non-density proof must establish, the shape of a counterexample, and an assessment

Track N1 (negative direction), after 14 rounds of positive attempts. Sources: Part I (paper/martin_density_note.tex, cited
[I, label]), Part II ([II, label]), Part III, refereed round notes (r1-r13), G3 (r14; its Section 2 and Lemma 3.1/Cor 3.2 refereed correct). Part files:
neg/N1_part1.md (formulation), neg/N1_part2.md (necessary conditions), neg/N1_part3.md (mechanisms, verdict); scripts in
neg/N1_work/. This file = summary + the three parts (authoritative) + numerics + next steps.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Proofs are complete for every item labelled PROVED here; items PROVED elsewhere
are cited.

## 0. Summary and answer to the question of the track

요약 (Korean summary for the user). 전면적인 negative 전환은 근거가 부족합니다. 14라운드 동안 만들어진 모든 적대적 후보는
새로운 회복 메커니즘으로 회복되었거나 모델 수준에 머물렀고, 어떤 행 f에서도 "모든" norm-attaining 근사열에 대한 하한
dist(rho g, C(f')) >= c 는 증명된 적이 없습니다. 반례가 되려면 모든 NA 근사열이 스스로 고르는 모든 접합(junction) 깊이에서
같은 크기로 다시 나타나는 자기유사적 불변량(유계 변환용량 + 무한으로 도망가는 오차, 또는 부호가 고정된 scrambling 비용)이
필요한데, 그런 불변량은 알려져 있지 않습니다. 다만 반례는 설계된 T_fin이 아닌 "적대적" T에서만 가능하므로, 후보 C1(음의
d-mismatch + (SC) 실패)을 대상으로, 하나의 고정 방향 x에 대한 type (I) 장애물(모든 허용 normer에서의 값싼 다중스케일 분해)을
목표로 하는 "표적형" negative 시험은 할 가치가 있습니다. 판단: 밀도(positive) 쪽이 약간 더 유력, 확신도 낮음.

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


# 1. What a proof of NON-density must establish (exact formulation, dual form)

Setting: any nonempty block set I (finite I = {1..N} gives p_N), any admissible T [I, def:admissible]. X = c_0 with p, X* = l_1 with p*,
X** = l_inf with p**. Norm equivalences: p* <= q* <= (1+||U||) ||.||_1 and ||.||_1 <= 3 p* [II, proof of Prop II-S3]; all
distances below may be taken in p* or in l_1 (constants change). S* := S_{p*}; NA_1 := NA((X,p),R) ∩ S* = grad p(S_p)
[I, prop:smooth]. s(t) := (1+t^2)^{1/2}. C(f) := {g : p*(f + t g) <= s(t) for all real t} (mate fibre), r_f := (p^2 - f^2)^{1/2}
on X, r~_f its largest sublinear minorant; C(f) = {g : g <= r~_f on X} and max_{g in C(f)} g(x) = r~_f(x) [I, prop:primal].
"[I, ...]" = Part I (paper/martin_density_note.tex), "[II, ...]" = Part II, G3 = r14/G3_notes.md.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.1 The recovered part of a fibre and the optimal obstruction functional

DEFINITION 1.1. For f in S* and h in X*:
 * Rec(f) := { g : there are f_n in NA_1 and g_n in C(f_n) with f_n -> f and g_n -> g }  (outer limit of C along NA rows);
 * U(f)   := { g : dist(g, C(f_n)) -> 0 for EVERY sequence f_n -> f in S* }            (inner limit along all rows);
 * A(f)   := the family of Hausdorff limits of sequences C(f_n), f_n in NA_1, f_n -> f;
 * Ob(f, h) := lim_{delta -> 0} inf { dist_{p*}(h, C(f')) : f' in NA_1, p*(f' - f) < delta }.

PROPOSITION 1.2 (structure of Rec(f)).  PROVED.
 (a) Rec(f) ⊆ C(f); Rec(f) is norm closed (hence compact) and balanced (lambda Rec(f) ⊆ Rec(f) for |lambda| <= 1).
 (b) Rec(f) = union of the sets A in A(f); A(f) is nonempty; every A in A(f) is compact, convex, symmetric, and
     U(f) ⊆ A ⊆ C(f).  In particular cl Cert^sh(f) ⊆ U(f) ⊆ Rec(f).
 (c) Ob(f, h) = dist_{p*}(h, Rec(f)) for every h in X*.
 (d) For g in C(f) and rho in [0,1): (f, rho g) in cl NA((X,p), l_2^2)  <=>  rho g in Rec(f)  <=>  Ob(f, rho g) = 0.
     Every g in Rec(f) satisfies (f, g) in cl NA.
 (e) NA((X,p), l_2^2) is dense  <=>  Rec(f) = C(f) for every f in S*.
Proof. (a) If g_n in C(f_n) -> g and f_n -> f then g in C(f) (global compactness / usc, [I, thm:compact]). Closedness: if h_k in
Rec(f), h_k -> h, pick f_k in NA_1 with p*(f_k - f) < 1/k and g_k in C(f_k) with p*(g_k - h_k) < 1/k; then f_k -> f, g_k -> h.
Balanced: every C(f_n) is convex and symmetric.
(b) Let g in Rec(f) via (f_n, g_n). All C(f_n) lie in the compact set C(f) ∪ (union_n C(f_n)) [I, thm:compact]; by Blaschke's
selection theorem in the hyperspace of nonempty compact subsets of this compact metric space, a subsequence C(f_{n_j})
converges in the Hausdorff metric to some A, and dist(g, A) <= p*(g - g_{n_j}) + d_H(C(f_{n_j}), A) -> 0, so g in A.
Conversely if A = lim_H C(f_n) and g in A, choose g_n in C(f_n) with p*(g_n - g) <= d_H(C(f_n), A) -> 0. NA_1 is dense in S*
(Bishop-Phelps), so sequences f_n exist, and Blaschke gives A(f) nonempty. Hausdorff limits of compact convex symmetric sets are
compact convex symmetric; A ⊆ C(f) by (a); for g in U(f), dist(g, C(f_n)) -> 0 along the defining sequence, so g in A.
cl Cert^sh(f) ⊆ U(f) is [I, prop:intrinsic(c)] (shifted transport along every sequence).
(c) Rec(f) is compact and contains 0. "<=": take g* in Rec(f) with p*(h - g*) = dist(h, Rec(f)) and (f_n, g_n) as in the
definition; dist(h, C(f_n)) <= p*(h - g_n) -> dist(h, Rec(f)). ">=": take f_n in NA_1, f_n -> f, with dist(h, C(f_n)) ->
Ob(f,h), and g_n in C(f_n) nearest to h; by [I, thm:compact] a subsequence g_n -> g*, and g* in Rec(f) by definition, so
dist(h, Rec(f)) <= p*(h - g*) = Ob(f, h).
(d) rho = 0: 0 in Rec(f) and (f,0) in cl NA by Bishop-Phelps. rho in (0,1): [I, lem:pair] says (f, rho g) in cl NA iff there are
f_n in NA_1, f_n -> f, with rho g in Li_n C(f_n); the latter is equivalent to rho g in Rec(f) (pick g_n in C(f_n) nearest to
rho g). The last equivalence is (c). Finally if g in Rec(f) via (f_n, g_n), each (f_n, g_n) attains its norm at the normer of f_n
[I, prop:reduction(d)], and (f_n, g_n) -> (f, g).
(e) "<=": [I, prop:reduction(b)] and (d). "=>": for g in C(f) and rho < 1, (d) gives rho g in Rec(f); Rec(f) is closed. QED

THEOREM 1.3 (exact non-density criterion).  PROVED.  The following are equivalent:
 (i)   NA((X,p), l_2^2) is not dense in L((X,p), l_2^2);
 (ii)  there are f in S* and g in C(f) with Ob(f, g) > 0, i.e. g notin Rec(f);
 (iii) there are f in S*, g in C(f), rho in (0,1) and theta, delta > 0 such that dist_{p*}(rho g, C(f')) >= theta for EVERY
       f' in NA_1 with p*(f' - f) < delta;
 (iv)  as (iii), and in addition there is delta' > 0 such that h'' notin Rec(f'') for every f'' in S* and h'' in C(f'') with
       p*(f'' - f) + p*(h'' - rho g) < delta' (the defect is open on the graph; cf. G3 Lemma 3.1).
Moreover Ob(f, .) = dist(., Rec(f)) is 1-Lipschitz, so Ob(f, rho g) >= Ob(f, g) - (1 - rho) p*(g): if (ii) holds with
Ob(f, g) = theta_0, then (iii) holds for every rho in (1 - theta_0/(2 p*(g)), 1) with theta = theta_0/4 and a suitable delta.
Proof. (i)<=>(ii): Prop 1.2(e). (ii)=>(iii): Ob(f, rho g) >= theta_0/2 > 0 for rho as stated; by the definition of Ob there is
delta with dist(rho g, C(f')) >= theta_0/4 for f' in NA_1 ∩ B(f, delta). (iii)=>(ii): Ob(f, rho g) >= theta > 0. (iii)=>(iv):
by Prop 1.2(d), (f, rho g) notin cl NA, so some operator ball B((f, rho g), eps) misses NA; with delta' < eps, if h'' in Rec(f'')
then (f'', h'') in cl NA lies within delta' of (f, rho g) (operator norm <= p*(f''-f) + p*(h''-rho g)), so NA meets the ball. QED

READING. The best possible "obstruction functional" is Ob itself: any functional Psi with dist(rho g, C(f')) >= c Psi(f, rho g) - o(1)
as f' -> f through NA_1 satisfies c Psi <= Ob = dist(., Rec(f)); upper bounds Ob(f, h) <= dist(h, A) (A in A(f)) <=
dist(h, U(f)) <= dist(h, cl Cert^sh(f)) are what positive results provide. A non-density proof must bound Ob from BELOW, i.e.
control dist(rho g, C(f')) simultaneously for all NA rows near f. No lower semicontinuity of f -> Ob is needed or claimed: only
the single row f matters. Since Ob(f, .) vanishes on cl Cert^sh(f), rho g must lie at positive distance from it.

## 1.2 The quantifier "every NA row near f": far freedom, uniform form

LEMMA 1.4 (far freedom, uniform form).  PROVED.  Let f in S* have forced data (a, z) [I, prop:forced]. For every delta > 0 there are
W in N and eta > 0 such that: if a' in c_00 ∩ S_{q*} with ||a' - a||_1 < eta, z' in B_{c_0} with z' = sgn a' on supp a' and
|z'_j - z_j| < eta for j <= W, then f' := grad p(y'), y' := z' + U(U^*a'/||U^*a'||), lies in NA_1 and p*(f' - f) < delta.
The coordinates z'_j, j > W, are arbitrary (subject to |z'_j| <= 1, z' in c_0, z'_j = sgn a'_j on supp a'), and supp a' may
contain coordinates beyond W (of total l_1-mass < eta). Conversely every f' in NA_1 is of this form [I, prop:smooth(c)].
Proof. f' in NA_1 by [I, prop:smooth(c)]. If the claim failed for some delta, there would be (a'_n, z'_n) satisfying the hypotheses
with W = n, eta = 1/n and p*(f'_n - f) >= delta; but then a'_n -> a in l_1 and z'_n -> z coordinatewise, so f'_n -> f by
[I, prop:approximants (ii)=>(i)]. Contradiction. QED

So in (iii) of Theorem 1.3 the adversary (the approximant) chooses: a finitely supported a' within eta of a (in particular tiny
"banks" anywhere), z' within eta of z on a window [1, W], and z' arbitrary in B_{c_0} beyond W. A non-recovery proof is a
STRATEGY assigning to each such choice a certificate of distance (Theorem 1.6 below).

PROPOSITION 1.5 (local structure of NA near (f, rho g)).  PROVED.  Let f in S*, g in C(f), rho in [0,1), and let
S in NA((X,p), l_2^2) with ||S - (f, rho g)|| < delta <= 1/4. Let S attain its norm at x_S in S_p, with y := S x_S/||S x_S||
= (cos phi, sin phi), cos phi >= 0 (replace x_S by -x_S if needed). Then:
 (a) |sin phi| <= 2 (delta/(1 - rho^2))^{1/2};
 (b) with R the rotation of l_2^2 such that R y = e_1, R S = ||S|| (f', g') where f' = grad p(x_S) in NA_1, g' in C(f'), g'(x_S) = 0;
 (c) p*(f' - f) + p*(g' - rho g) <= 2 (2 delta + pi (delta/(1 - rho^2))^{1/2})/(1 - delta).
Conversely, every c Q (f', g') with c > 0, Q a rotation, f' in NA_1 and g' in C(f') attains its norm (at the normer of f').
Proof. Put T := (f, rho g); ||T|| = 1 because p*(f) = 1 and rho g in C(f). For a unit vector u = (cos psi, sin psi),
p*(T^* u) = |cos psi| p*(f + tan psi rho g) <= |cos psi| s(rho tan psi) = (1 - (1 - rho^2) sin^2 psi)^{1/2} (and p*(rho g) <= rho if
cos psi = 0). Now p*(T^* y) >= <T x_S, y> >= <S x_S, y> - delta = ||S|| - delta >= 1 - 2 delta, so (1 - rho^2) sin^2 phi <=
1 - (1 - 2 delta)^2 <= 4 delta: (a). For (b): (R S) x_S = ||S|| e_1, so f' := (first row of RS)/||S|| satisfies f'(x_S) = 1 and
||(f', g')|| = 1 with g' := (second row)/||S||; thus p*(f') = 1 is attained at x_S, f' = grad p(x_S) [I, prop:smooth(b)], g' in C(f')
[I, prop:reduction(a)] and g'(x_S) = 0 [I, prop:reduction(c)]. (c): ||(f', g') - T|| <= (||R S - R T|| + ||R T - T|| + | ||S|| - 1 |)/||S||
<= (2 delta + ||R - I||)/(1 - delta), ||R - I|| = 2|sin(phi/2)| <= |phi| <= pi |sin phi|/2, and p*(f' - f), p*(g' - rho g) <=
||(f', g') - T||. The converse is [I, prop:reduction(d)] plus invariance of NA under rotations and scalings. QED

CONSEQUENCE (the Hahn-Banach formulation).  Near (f, rho g) the set NA is the union, over normers x' in S_p with grad p(x')
near f, of the rotated and rescaled convex fibres C(grad p(x')). It is not convex, and for small delta the ball
B((f, rho g), delta) either meets NA or misses it entirely; separation therefore has to be done FIBREWISE: (f, rho g) notin cl NA
iff there is delta > 0 such that for every x' in S_p with p*(grad p(x') - f) < delta, rho g is delta-separated from the compact
convex set C(grad p(x')) by some functional x = x(x') in X (Theorem 1.6). A functional x that works for ALL such x' at once is
exactly a convex obstruction of type (I) in Theorem 1.9. Precisely:

PROPOSITION 1.5bis (Hahn-Banach form).  PROVED.  Let f in S*, g in C(f), rho in (0,1), and for delta in (0, 1/4] put
   N_delta := { c R_phi (f', g') : f' in NA_1, p*(f' - f) < delta, g' in C(f'), |c - 1| <= delta, |phi| <= delta }  ⊆ NA,
R_phi the rotation of l_2^2 by phi (ALL mates g' of NA rows near f, not only those near rho g).
 (a) For every delta there is delta'' = delta''(delta, rho) > 0 such that every S in NA with ||S - (f, rho g)|| < delta'' lies in N_delta.
     Hence (f, rho g) in cl NA iff (f, rho g) in cl N_delta for every delta > 0.
 (b) There are a continuous linear functional Lambda on L((X,p), l_2^2) and delta > 0 with Lambda((f, rho g)) > sup Lambda(N_delta)
     iff there are x in X and theta, delta_1 > 0 with rho g(x) >= r~_{f'}(x) + theta for every f' in NA_1 ∩ B(f, delta_1)
     (a type (I) obstruction at (f, rho g), Theorem 1.9).
Proof. (a) Prop 1.5 with delta'' so small that 2(2 delta'' + pi (delta''/(1 - rho^2))^{1/2})/(1 - delta'') < delta and
pi (delta''/(1-rho^2))^{1/2} <= delta: then S = ||S|| R^{-1}(f', g') with the required bounds.
(b) "<=": Lambda(S) := <S x, e_2>. For S = c R_phi (f', g'), Lambda(S) = c (sin phi f'(x) + cos phi g'(x)); C(f') is balanced and
max_{C(f')} x = r~_{f'}(x), so sup Lambda(N_delta) <= (1 + delta)(sup_{f'} r~_{f'}(x) + delta p(x)) <= (1 + delta)(rho g(x) - theta
+ delta p(x)) < rho g(x) = Lambda((f, rho g)) for delta <= delta_1 small (note rho g(x) >= theta > 0).
"=>": S -> (S^* e_1, S^* e_2) identifies L((X,p), l_2^2) with X* x X*, so Lambda(S) = Phi_1(S^* e_1) + Phi_2(S^* e_2) with
Phi_i in X** = l_inf. Let eta := Lambda((f, rho g)) - sup Lambda(N_delta) > 0. Using c = 1, phi = 0:
Phi_1(f) + rho Phi_2(g) >= Phi_1(f') + max_{C(f')} Phi_2 + eta for f' in NA_1 ∩ B(f, delta). By upper semicontinuity of C at f
[I, thm:compact] there is delta_1 <= delta with C(f') ⊆ C(f) + eps B_{p*} for p*(f' - f) < delta_1, and we may take
delta_1 ||Phi_1|| <= eta/3. Goldstine gives x in X, p(x) <= p**(Phi_2), with |(Phi_2 - x)(k)| <= eps on a finite eps-net of the compact
set C(f) ∪ {g}; every k in C(f') is within 2 eps of a net point, so |(Phi_2 - x)(k)| <= eps + 2 eps (p**(Phi_2) + p(x)) and
|max_{C(f')} Phi_2 - r~_{f'}(x)| <= eps (1 + 4 p**(Phi_2)) for those f'; also |rho Phi_2(g) - rho g(x)| <= eps.
With eps small, rho g(x) >= r~_{f'}(x) + eta/3 on NA_1 ∩ B(f, delta_1). QED
So "Hahn-Banach separation of (f, rho g) from NA near it" is exactly a type (I) obstruction; a general non-recovery proof (type (II)
allowed) is only a FIBREWISE separation, with x depending on the approximant.

## 1.3 Dual (primal-certificate) form of the distance to a fibre

THEOREM 1.6 (dual formula; Bregman form at NA rows).  PROVED.
 (a) For f' in S* and h in X*:
       dist_{p*}(h, C(f')) = sup { h(x) - r~_{f'}(x) : x in X, p(x) <= 1 },
       dist_{l_1}(h, C(f')) = sup { h(x) - r~_{f'}(x) : x in c_00, ||x||_inf <= 1 }.
 (b) If f' = grad p(x') in NA_1 (p(x') = 1), then for y in X
       r_{f'}(y)^2 = beta_{x'}(y) (2 p(y) - beta_{x'}(y)),   beta_{x'}(y) := p(y) - grad p(x')(y) = p(y) - p(x') - grad p(x')(y - x'),
     the Bregman divergence of p at x'; beta_{x'} >= 0, it is convex and positively homogeneous, and beta_{x'}(y) = 0 iff
     y in R_+ x'.
 (c) Consequently dist_{p*}(rho g, C(f')) >= theta iff for every eta > 0 there are x in X with p(x) <= 1 and y_1, ..., y_n in X
     with sum_j y_j = x and
       sum_j ( beta_{x'}(y_j) (2 p(y_j) - beta_{x'}(y_j)) )^{1/2}  <=  rho g(x) - theta + eta.
     ("cheap decomposition": the primal certificate of non-recovery at the normer x').
Proof. (a) C := C(f') is norm compact and convex [I, thm:compact]. For a norm-compact convex C in a normed space E and h in E,
dist(h, C) = max_{phi in B_{E*}} (phi(h) - max_C phi) (Hahn-Banach separation of h from C + r B_E for r < dist(h, C), and the
trivial reverse inequality). Here E = (X*, p*), E* = (X**, p**). The map phi -> phi(h) - max_C phi is weak*-continuous on B_{p**}:
max_C phi is within eps ||phi|| of max_i phi(g_i) for a finite eps-net (g_i) of C. B_p is weak*-dense in B_{p**} (Goldstine), so
the maximum over B_{p**} equals the supremum over B_p, and max_C x = r~_{f'}(x) for x in X [I, prop:primal]. The l_1 statement is
the same with E* = l_inf and the weak*-dense set B_{c_00} ⊂ B_{l_inf}.
(b) f'(x') = 1 = p(x') and f' = grad p(x'); by positive homogeneity grad p(x')(x') = p(x'), whence the two expressions for beta.
r^2 = p^2 - f'^2 = (p - f')(p + f') = beta (2p - beta). beta >= 0 as p*(f') = 1; convexity and homogeneity are clear. If y != 0 and
beta(y) = 0, then y/p(y) is a normer of f'; p** is strictly convex [I, prop:forced(a)], so p is, and the normer is unique.
(c) dist >= theta iff for every eta there is x in B_p with rho g(x) - r~_{f'}(x) > theta - eta, and r~_{f'}(x) is the infimum of
sum_j r_{f'}(y_j) over finite decompositions sum_j y_j = x [I, prop:primal]. QED

COROLLARY 1.7 (symmetric two-point bound; curvature).  PROVED.  Let f' = grad p(x') in NA_1, v in X and tau > 0. Then
   r~_{f'}(v) <= ((1 + tau p(v))/2)^{1/2} ( beta_{x'}(x' + tau v)^{1/2} + beta_{x'}(x' - tau v)^{1/2} ) / tau.
In particular, if t -> p(x' + t v) is twice differentiable at 0 with second derivative Q(v), then |g'(v)| <= Q(v)^{1/2} for every
g' in C(f'). The same bounds hold at every f in S* (attaining or not) with x' replaced by the normer xi in S_{p**}, p by p**,
beta by beta**_xi(Y) := p**(Y) - f(Y) (Y in l_inf), and v in X.
Proof. v = y_+ + y_- with y_+ := (x' + tau v)/(2 tau), y_- := -(x' - tau v)/(2 tau). r_{f'} is even and positively homogeneous, and
r_{f'}(x' +- tau v)^2 = beta(2p - beta) <= 2 beta(x' +- tau v) p(x' +- tau v) <= 2 (1 + tau p(v)) beta(x' +- tau v). Hence
r~(v) <= r(y_+) + r(y_-) <= [ (2(1 + tau p(v)) beta_+)^{1/2} + (2(1 + tau p(v)) beta_-)^{1/2} ]/(2 tau), which is the claim. If
p(x' + t v) = 1 + t f'(v) + t^2 Q(v)/2 + o(t^2), then beta(x' +- tau v) = tau^2 Q(v)/2 + o(tau^2); let tau -> 0.
Bidual version: for g in C(f) and Y in l_inf, |g(Y)| <= r**_f(Y) := (p**(Y)^2 - f(Y)^2)^{1/2}: take a net y_a in p**(Y) B_p with
y_a -> Y weak* (Goldstine); then g(y_a) -> g(Y), f(y_a) -> f(Y) and |g(y_a)| <= (p(y_a)^2 - f(y_a)^2)^{1/2} <= (p**(Y)^2 -
f(y_a)^2)^{1/2} -> r**_f(Y). For v in X, g(v) = g(Y_+) + g(Y_-) with Y_+- := +-xi/(2 tau) + v/2 in l_inf, and the computation is
the same with p**(xi) = 1 = f(xi). QED
NUMERICAL sanity check (N1_work/twopoint_check.py; smooth norms on R^3): the LP value of max_{C(f')} v never exceeds
inf_tau of the bound; it is often strictly below the Hessian bound Q(v)^{1/2} (e.g. 0.208 vs 0.358): the large scales bind as
well; r~ is a genuinely multi-scale infimum and the two-point bound is not sharp.

READING. Mates of an NA row are bounded by the multi-scale (Bregman) curvature of p at its normer x'; mates of f by that of p**
at xi. A non-recovery proof has to show that at EVERY admissible normer x' (Lemma 1.4: x' close to xi on a window, arbitrary
far out, arbitrary tiny banks) p is FLATTER, in some direction x = x(x') and at some scale, than rho g requires.

## 1.4 Only small scales are decisive

PROPOSITION 1.8 (scale localization).  PROVED.  Let f, f' in S*, g in C(f), rho in (0,1), g' in X*, eps := p*(f' - f),
eta := p*(g' - rho g), and t_* := max( (6 eps/(1 - rho^2))^{1/2}, 6 eta/(1 - rho^2) ). If t_* <= 1, then p*(f' + t g') <= s(t) for
every |t| >= t_*. Hence g' in C(f') iff p*(f' + t g') <= s(t) for 0 < |t| < t_*.
Proof. p*(f' + t g') <= p*(f + t rho g) + eps + |t| eta <= s(rho t) + eps + |t| eta. For t_* <= |t| <= 1: eps <= (1 - rho^2)t^2/6
and |t| eta <= (1 - rho^2) t^2/6; for |t| >= 1: eps + |t| eta <= (1 - rho^2)|t|/3 (as t_* <= 1). Conclude with
s(t) - s(rho t) >= (1 - rho^2) min(t^2, |t|)/3 [I, lem:slack(a)]. QED
So in Theorem 1.3(iii) every g' at distance eta < theta from rho g must violate the mate inequality at f' at a scale
0 < |t| < t_*(eps, eta, rho) ~ max(eps^{1/2}, eta)/(1 - rho^2): the closer g' is to rho g, the smaller the violating scale.

## 1.5 Convex versus non-convex obstructions

THEOREM 1.9 (dichotomy).  PROVED.  Let f in S*.
 (a) For x in X: h_Rec(x) := sup_{g in Rec(f)} g(x) = limsup_{f' -> f, f' in NA_1} r~_{f'}(x)  (<= r~_f(x)).
 (b) The following are equivalent: (b1) cl conv Rec(f) = C(f); (b2) limsup_{NA_1 ∋ f' -> f} r~_{f'}(x) = r~_f(x) for all x in X;
     (b3) every g in C(f) that is the unique maximizer over C(f) of some x in X (an X-exposed mate) lies in Rec(f).
 (c) If g is X-exposed by x, then g in Rec(f) iff limsup_{NA_1 ∋ f' -> f} r~_{f'}(x) = r~_f(x).
 (d) NA((X,p), l_2^2) is NOT dense iff one of the following holds for some f in S*:
     (I)  [convex / uniform obstruction] there is x in X with limsup_{NA_1 ∋ f' -> f} r~_{f'}(x) < r~_f(x); equivalently some
          X-exposed mate of f is not recovered; equivalently there are g in C(f), rho < 1, theta, delta > 0 and ONE x in X with
          rho g(x) - r~_{f'}(x) >= theta for every f' in NA_1 ∩ B(f, delta);
     (II) [non-convex obstruction] cl conv Rec(f) = C(f) but Rec(f) is not convex.
Proof. (a) ">=": if g_n in C(f_n) -> g in Rec(f), then r~_{f_n}(x) >= g_n(x) -> g(x). "<=": take f_n in NA_1, f_n -> f realizing the
limsup and g_n in C(f_n) with g_n(x) = r~_{f_n}(x) [I, prop:primal]; a subsequence converges to some g* in Rec(f) [I, thm:compact] and
g*(x) = limsup.
(b) (b1)=>(b2): support functions of a set and of its closed convex hull agree; use (a) and max_{C(f)} x = r~_f(x).
(b2)=>(b1): cl conv Rec(f) is norm compact, hence weak*-compact, and convex; if some g in C(f) were outside it, a weak*-continuous
functional, i.e. some x in X = c_0, would separate them strictly, contradicting (b2) via (a). (b1)=>(b3): if g is the unique
maximizer of x on C(f) = cl conv Rec(f), the maximum of x over the compact set Rec(f) equals max_{C(f)} x and is attained at some
g* in Rec(f) ⊆ C(f); so g* = g. (b3)=>(b2): r~_f is a continuous convex function (a seminorm <= p) on the separable Banach space
X, hence Gateaux differentiable on a dense G_delta set D (Mazur's theorem). For x in D its subdifferential, which for the support
function of the weak*-compact convex set C(f) is the set of maximizers {g in C(f) : g(x) = r~_f(x)}, is a singleton {g_x}; so g_x
is X-exposed by x, g_x in Rec(f) by (b3), and h_Rec(x) >= r~_f(x). Thus (b2) holds on D, and both sides are p-Lipschitz in x
(support functions of subsets of B_{p*}), so (b2) holds everywhere.
(c) "<=" : choose f_n, g_n as in the proof of (a)"<=" for this x; the limit g* maximizes x over C(f), so g* = g, and g* in Rec(f).
"=>": (a).
(d) If density fails, Rec(f) != C(f) for some f (Prop 1.2(e)). If cl conv Rec(f) != C(f), (b) and (a) give (I). Otherwise
C(f) = cl conv Rec(f) != Rec(f), so Rec(f) is not convex: (II). Conversely (I) or (II) gives Rec(f) != C(f) (C(f) is convex).
The reformulations of (I): (b1)<=>(b3) and (c) give the exposed-mate form; for the uniform form, if limsup r~_{f'}(x) <= r~_f(x) - 3
theta, pick delta with r~_{f'}(x) <= r~_f(x) - 2 theta on NA_1 ∩ B(f, delta), g in C(f) with g(x) = r~_f(x) and rho with
(1 - rho) r~_f(x) <= theta; conversely a uniform x gives limsup r~_{f'}(x) <= rho g(x) - theta < r~_f(x). QED

REMARK 1.10 (what (I) and (II) would require).
 (I) is a statement about ONE scalar function: Phi_x(f) := r~_f(x) is upper semicontinuous on S* [I, thm:compact], continuous at every
     point of the comeager set Omega of Hausdorff-continuity points of C [I, rem:joint; G3 Cor 3.2], and (I) says that at f it has an
     "upward spike relative to NA_1": Phi_x(f) > limsup_{NA_1 ∋ f' -> f} Phi_x(f'). Since NA_1 is dense, it then also holds that
     Phi_x(f'') <= Phi_x(f) - theta for every f'' in Omega near f (continuity at f''): the fibre at f is strictly larger, in the
     fixed direction x, than the fibres of all generic and all NA rows nearby — a RIGID EXCEPTIONAL MATE. By Theorem 1.6(c) a proof of
     (I) must exhibit, at every admissible normer x' (Lemma 1.4), a cheap decomposition of the SAME x. PROVED (as a reformulation).
 (II) requires at least two recovered mates g_1, g_2 (along different NA sequences, Prop 1.2(b): different A in A(f)) whose convex
     combination is not recovered along any NA sequence. All positive results of Parts I-III are mate-specific constructions
     (engineered approximants chosen after g), so none of them excludes (II) for a general f; on the other hand no mechanism that could
     produce (II) is known, and every non-exposed mate examined in Parts I-III was recovered directly. (II) is the precise form of the
     gap noted at the end of [I, sec:status] (whether density into l_2^2 forces recovery of a whole fibre along one sequence).
     HEURISTIC/OPEN.
 Positive proofs, conversely, may split density into: (P-I) the scalar statement (b2) for all f and x [equivalently: recover every
 X-exposed mate], and (P-II) convexity of Rec(f) (a "merging lemma": two NA approximant sequences recovering g_1 and g_2 can be merged
 into one recovering both). Both are OPEN; (P-II) is new as a formulation.

# 2. The shape of a counterexample for an ARBITRARY admissible T (necessary conditions)

Setting as in part 1. A "counterexample" is (T, I, f, g, rho) with T admissible, I a block set (one finite I = {1..N} suffices
for a negative answer: (c_0, p_N) is then a Banach space X with NA(X, l_2^2) not dense), f in S*, g in C(f), rho in (0,1), and
rho g notin Rec(f) (Theorem 1.3). Throughout, "PROVED" means proved in a refereed source cited, or proved here; G3 (round 14) has been refereed
(r14/G3_referee.md): its Section 2 lemmas, Theorem CL and Lemma 3.1/Cor 3.2 are correct.

## 2.0 A global reformulation (PROVED here)

Let G := {(f, g) in S* x X* : g in C(f)} (the mate graph; closed by [I, thm:compact]) and G_NA := {(f, g) in G : f in NA_1}.
LEMMA 2.1. (a) graph(Rec) = cl G_NA (closure in S* x X*). (b) More generally, if R ⊇ NA_1 is any set of rows with
Rec(f') = C(f') for f' in R, then Rec(f) = Ls_{f' -> f, f' in R} C(f') for every f. (c) NA((X,p), l_2^2) is dense iff
G = cl G_NA, and G \ cl G_NA is relatively open in G.
Proof. (a) is the definition of Rec. (b) Rec(f) ⊆ Ls_R C is clear because NA_1 ⊆ R. Conversely, if f_n in R, g_n in C(f_n) = Rec(f_n), g_n -> g and
f_n -> f, choose by (a) (f'_n, g'_n) in G_NA with p*(f'_n - f_n) + p*(g'_n - g_n) < 1/n; then (f, g) in cl G_NA, i.e. g in Rec(f). (c) Prop 1.2(e)
and Theorem 1.3(iv). QED
So a counterexample is a point where the mate graph JUMPS UP relative to the mate graph over norm-attaining rows — equivalently,
by (b), relative to the mate graph over ANY class of rows already known to be recoverable (Omega, (BT) rows, ...). With
R = Omega (comeager, [I, rem:joint]): rho g notin Ls_{f'' -> f, f'' in Omega} C(f''): the dangerous mate is not a limit of mates
of generic rows. It is an "exceptional mate" of an exceptional row.

## 2.1 Conditions on the first row f

(F1) f is not norm attaining. [I, prop:reduction(d)]. PROVED.
(F2) f is not a point of lower semicontinuity of C. The lsc points form a comeager set Omega (Fort's theorem for the usc
     compact-valued map C [I, thm:compact]; residual uniform recovery theorem of Preprint A, [I, rem:joint]); Omega ⊆ Rec.
     So the bad rows form a MEAGRE set. PROVED.
(F3) (I finite) f does not satisfy (BT) [I, cor:BTrecovered]: either F = supp a is infinite, or some Q_m (strict non-peaks) is
     infinite, or a degenerate peak exists (Dg_m != empty), or margin sparsity (MS) fails. In particular f is not C-tame without
     degenerate peaks [I, thm:tame]. The contact set K is irrelevant for this condition (any K is allowed in (BT)). PROVED.
     Remark (V4 Prop 5.1, refereed): (BT) is meagre in every fixed-z fibre (near-threshold carriers are Baire generic), so (F3)
     is a weak restriction: violating (BT) is the generic situation, not an exceptional one.
(F4) (F = N) f does not satisfy (BD) + (SC_I) + (W_M) of [II, thm:II-N] (box-dominated support). PROVED.
(F5) Openness (Theorem 1.3(iv), G3 Lemma 3.1): there is delta' > 0 such that every (f'', h'') in G with p*(f''-f) + p*(h''-rho g)
     < delta' is again non-recovered. In particular rho g keeps distance >= delta'/2 from C(f'') for EVERY recoverable row f'' in
     B(f, delta'/2): all NA rows, all rows of Omega, all (BT) rows, and (for the designed T_fin of Part III) all rows with finite
     base support. PROVED.
(F6) f is not reached by transitivity [I, thm:transitivity]: there is no sequence of recoverable rows f_n -> f with
     liminf r~_{f_n} >= rho' r~_f (all rho' < 1) on a dense set; by Lemma 2.1(b) the sharp form is rho g notin
     Ls_{f'->f, f' in R} C(f') for every recoverable class R. PROVED.
(F7) For the designed operators: for T_fin (Part III, Master Theorem VI, two independent passes) every first row with finite base
     support is recoverable for every N, and density for p_N <=> (LSC-trunc)_N. A counterexample for T_fin must therefore have
     F INFINITE and violate (LSC-trunc)_N at (f, g, rho). For a NEGATIVE answer one should not use T_fin: one admissible T suffices,
     and an adversarial T (without signatures, ladders, generic weights or diagonal base) avoids all of Parts II-III. PROVED
     (as a consequence of Part III) / methodological remark.

## 2.2 Conditions on the mate g (any admissible T)

(M1) rho g notin U(f) ⊇ cl Cert^sh(f) (Prop 1.2(b)). This excludes, with their closures: finite certificates [I, thm:transport],
     shifted certificates [I, thm:shifted], weighted directions with H <= 1 [I, thm:weighted], locally split mates and
     split-contractive operators (I finite) [I, thm:locsplit, cor:splitcontractive], carrier mates with non-summable gaps
     [I, thm:carriers], and the ladder/averaging class [I, cor:ladder]. PROVED.
(M2) (Quantitative contrapositive of [I, cor:ladder] and [I, cor:decomposition], I finite.) For all c_0 > 0, kappa_1, K < infinity
     there are arbitrarily small t > 0 such that for NEITHER tau = t NOR tau = -t does f + tau g admit a decomposition
       f + tau g = (a + tau b_t + tau e_t) + sum_m R_m^*((1 - d_{t,m} tau) w_m + tau omega_{t,m})
     with c_t = (b_t, omega_t) a finite certificate, r(c_t) >= c_0 t, kappa(c_t) <= kappa_1, p*(e_t) <= K t and all component norms
     <= s(tau) + o(tau^2). PROVED (contrapositive; since g notin cl Cert(f) by (M1)).
     READING: at a cofinal set of small scales, on BOTH sides of t = 0, every near-optimal decomposition of f +- t g uses resources
     outside the format "finite two-sided certificate + O(t)": base mass >> t off F (contacts / near-contacts used one-sidedly),
     support coordinates used beyond their cushion (|b_j| > |a_j|/(c_0 t): near-flips), peaks used other than through the common
     shift d_m w_m, strict non-peaks used beyond their radius (near-threshold use: gap_m(k) < 2 c_0 t |omega(k)|), or an infinite
     tail of carriers of l_1-mass >> t.
(M3) If a in c_00: g notin K(f) := cl conv(Cert^sh(f) ∪ B(f)), B(f) = balanced finite certificates with Gamma_w <= 1
     [I, prop:intrinsic(c), thm:transfer]. For arbitrary F: g is not a balanced finite certificate with ||b/a||_inf < infinity
     and Gamma_w <= 1 [II, thm:II-transferinf]. PROVED.
(M4) Two-piece data. If F is finite: g carries NO two-piece data with kappa_w <= 1 and (Delta d_m >= 0 for all m [I, cor:D1], or
     I_- := {m : Delta d_m < 0} satisfying (SC) [I, thm:engineered]); no hypothesis on K, Q_m or rates of T is involved. If F is
     infinite: no such data satisfying (CS-side) [II, thm:II-raised] or rho^2 kappa^fl < 1 [II, thm:II-flipext]. Since Rec(f) is
     closed, rho g is also not a limit of such mates. PROVED.
     Hence, by [I, thm:onesided(c)] (every mate at a (BT) row has two-piece data with kappa_w <= 1), the dangerous mate must
     exploit the failure of (BT) in (F3): its one-sided decompositions need infinitely many carriers, degenerate or
     near-threshold carriers, or flips of an infinite support.
(M5) Windowed recovery through nearby rows (Theorem E family, any admissible T) [II, thm:II-E, thm:II-ERT]: g is not recovered
     through rows f_j -> f carrying (exact d-neutral two-piece, or transfer-error) window data whose transfer error is
     o(c_j^2 (T_j 2^{-n_j})^2). In words: near f there are no rows at which g has EXACT window data that are second-order close
     to f relative to the window bottom. PROVED (as the contrapositive).
(M6) Linear decompositions and exact resonances. If F ∪ K is finite, g has no two-sided decompositions linear in t on
     [-tau, tau] [I, cor:twosided]. In general, any pair of t-linear decompositions has switching vector D = B_+ - B_- in Y that is,
     off F, supported in K and z-signed [I, prop:exact]: EXACT (scale-free) switching needs infinitely many contacts (or near-flips
     of an infinite support). The explicit exact-resonance mates of [I, thm:defect] are recovered [I, cor:exampleRecovered], and
     every d-neutral exact two-piece switching mate is recovered (P2A/N2 Thm 1, Round 2, refereed; contained in [I, cor:D1]).
     PROVED. So the switching of the dangerous mate must be scale-dependent ("approximate resonance") or not of two-piece type.
(M7) Universal scale-t constraints on EVERY decomposition of EVERY mate (G3 Section 2; PROVED, G3 refereed correct): for decompositions
     f +- t g = A_+- + L^*W_+- with component norms <= s(t), B_+- := +-(A_+- - a)/t and switching vector V := B_+ - B_- in Y:
       |V(zhat)| <= t/q_0;   sum_{j notin F} (z_j V_j)_- <= t/(2 q_0);   sum_{j notin F} (1 - |z_j|)|V_j| <= t/q_0;
     and the conservation law (Theorem CL): for any T_th ⊂ F, ||V 1_{N}||_1 <= - sum_{s in T_th} zhat_s V_s + |<V 1_N, h>| + 3t/q_0
     + 4 alpha(N ∩ F)/t, N := complement of T_th. These are properties of all mates (not specific to counterexamples): they say that
     switching off F is one-signed (z-signed) up to O(t) and must be paid by the support F.
(M8) Sign rule (P1, refereed; [I, rem:resonancetypes]): exact or o(Phi)-perturbed cross-block near-duplicates (built into Lemma B's
     construction) serve the same side of t = 0 and cannot switch with each other. So Martin's built-in near-duplicates do not by
     themselves produce switching. PROVED (P1) / HEURISTIC guide (Part I).

## 2.3 Conditions on the operator T (HEURISTIC / model level; Rounds 1-3)

(T1) Rates. For "generic" T (far parts of distinct carriers quantitatively independent) the approximant can convert unboundedly
     many adjacent scales through far moves (E Cor 6.2, PROVED; E 8.3, SKETCH), and averaging then recovers (E Model N: R(J) -> 1).
     A counterexample needs an ADVERSARIAL T: error-dominated carriers (approximation errors >> Phi at the carrier's own depth),
     FAR RIGIDITY (far tails nearly collinear inside long detector groups; compatible with Lemma B: N2 4.5, SKETCH). HEURISTIC.
(T2) Non-compact errors (R3 5.1, the residual class O3*): by R3 Theorem EC (PROVED, any admissible T) every FIXED
     finite-dimensional family of O(scale) errors is carried by generic tail coordinates turned into exact zero-weight strict
     non-peaks by o(1) window moves. A counterexample needs, at every candidate boundary scale: (R1) escaping errors of critical
     size, (R2) no early generic approximants of the escaping directions, (R3) concentration on few coordinates guarded by matched
     carriers, (R4) no private handles, (R5) recursive guarding, plus (A1) near-threshold one-sided carriers of both peak types at all
     scales (a fixed point between T and f, constructed nowhere). HEURISTIC/OPEN.
(T3) Chain guards give unbounded conversion capacity except possibly for ALTERNATING types at ratio c = 1 (R3 5.2, SKETCH in a
     linear status model; referee: bounded only with constant targets). This is the most specific adversarial configuration known.
     SKETCH.

## 2.4 Self-similarity (what persists across scales)

(S1) By Lemma 1.4 the approximant chooses the window W and all far data freely; by Prop 1.8 only scales < t_*(eps, eta, rho) are
     decisive; hence the obstruction must reappear below EVERY window: it cannot be carried by finitely many coordinates or
     carriers. PROVED (as a reformulation).
(S2) For the designed T, persistent residual rows need a FRESH pinned wrong-signed resonance at every main stage (H2 Thm H2.B,
     refereed), and the persistent residual is of exact/bias type (G3 5.3, SKETCH); G3 Cor 3.2 (PROVED, refereed): a
     counterexample is a property of the PAIR (f, g) — rows with active mates near rho g force their own resonances.
     For arbitrary T the analogue is (T2)(R5). HEURISTIC for arbitrary T.

## 2.5 Summary table (arbitrary admissible T, I finite unless noted)

| # | Necessary condition on a counterexample (T, f, g, rho) | Source | Status |
|---|---|---|---|
| F1 | f not norm attaining | I prop:reduction(d) | PROVED |
| F2 | f outside the comeager set Omega of lsc points (bad rows are meagre) | Fort / PrA, I rem:joint | PROVED |
| F3 | f not (BT): F infinite, or some Q_m infinite, or degenerate peaks, or (MS) fails | I cor:BTrecovered | PROVED |
| F4 | if F = N: not (BD)+(SC_I)+(W_M) | II thm:II-N | PROVED |
| F5 | rho g uniformly far from C(f'') for all recoverable f'' near f; defect open on the graph | Thm 1.3(iv), G3 L3.1 | PROVED |
| F6 | rho g notin Ls over any recoverable class (Omega, (BT), NA) | Lemma 2.1(b) | PROVED |
| F7 | for T_fin: F infinite and (LSC-trunc)_N fails | III MT VI, Thm VI.2 | PROVED (Part III) |
| M1 | rho g notin U(f) ⊇ cl Cert^sh(f) (certificates, shifted, weighted, locally split, ladder, carriers) | I Sec 3-4 | PROVED |
| M2 | at cofinal small scales, on both sides, no "certificate + O(t)" decomposition | I cor:decomposition | PROVED |
| M3 | not in K(f) (a in c_00); not a balanced certificate with Gamma_w <= 1 (any F) | I thm:transfer, II thm:II-transferinf | PROVED |
| M4 | no two-piece data with kappa_w <= 1 and (Delta d >= 0 or (SC)); infinite F: no (CS-side)/flip-extended data | I cor:D1, thm:engineered; II raised/flipext | PROVED |
| M5 | no exact window data at second-order-close nearby rows | II thm:II-E, II-ERT | PROVED |
| M6 | switching scale-dependent (exact resonances recovered; exact switching needs infinite F ∪ K) | I prop:exact, cor:twosided, cor:exampleRecovered | PROVED |
| M7 | switching z-signed off F up to O(t); conservation law | G3 Sec 2 | PROVED (G3, refereed) |
| M8 | cross-block near-duplicates cannot switch with each other | P1 sign rule | PROVED |
| T1 | adversarial T: error-dominated carriers, far rigidity | E, N2 4.5 | HEURISTIC / SKETCH |
| T2 | escaping, concentrated, recursively guarded critical errors (O3*) at every boundary | R3 5.1 | HEURISTIC / OPEN |
| T3 | chain guards of alternating type at ratio 1 | R3 5.2 | SKETCH |
| S1 | obstruction must reappear below every window | Lemma 1.4, Prop 1.8 | PROVED (reformulation) |
| S2 | fresh resonance at every stage; obstruction is a property of the pair | H2.B (designed T), G3 3.2 | PROVED (designed) / HEURISTIC (arbitrary) |

What is NOT a necessary condition (to avoid false leads): an infinite contact set K is not required by the proved results
(F3 allows any K; rows with F ∪ K finite but infinitely many near-threshold carriers are open); infinite F is not required for an
arbitrary T (it is required only for T_fin); the d-mismatch sign is not decisive by itself (Delta d < 0 is open only without (SC)).

# 3. Can one admissible T and one row kill every recovery mechanism? Assessment

Notation as in parts 1-2. "Kill" a mechanism = choose (T, f, g) outside its hypotheses while keeping g in C(f).

## 3.1 Mechanisms, the feature each exploits, and how an adversary kills it

| # | Mechanism (any admissible T unless noted) | Feature of (f, g) exploited | Adversarial kill | Compatible with g in C(f)? |
|---|---|---|---|---|
| 1 | f attains its norm [I prop:reduction(d)] | normer in c_0 | f non-attaining | yes (trivial) |
| 2 | Omega: lsc points, comeager [PrA, I rem:joint] | genericity of f | f in the meagre discontinuity set | yes: discontinuity points exist ([I thm:defect]; [II thm:II-NL]) |
| 3 | transport of finite and shifted certificates [I thm:transport, thm:shifted] | g two-sided, finitely carried, radius >~ t | O(1) one-sided content at cofinal small scales (M2) | yes: two-piece switching mates exist ([I prop:twopiece]) |
| 4 | averaging / ladder / weighted / carriers with non-summable gaps [I Sec 4] | g = certificate + O(t) at all small scales | same as 3, quantitatively | yes |
| 5 | locally split, split-contractive [I thm:locsplit] | one two-sided decomposition for all small t | switching | yes |
| 6 | transfer peaks, K(f), Gamma_w <= 1 [I thm:transfer; II thm:II-transferinf] | balanced finite certificate, Gamma_w <= 1 | g notin S(f), or Gamma_w > 1 (needs non-(BT), [I prop:lowerbound]) | yes |
| 7 | (BT) rows: every mate has two-piece data with kappa_w <= 1 [I thm:onesided, cor:BTrecovered] | F finite, Q_m finite, no degenerate peaks, (MS) | infinitely many strict non-peaks / degenerate peaks / (MS) fails / F infinite | yes; non-(BT) is Baire-GENERIC in fixed-z fibres (V4 Prop 5.1) |
| 8 | engineered NA approximants for EXACT two-piece data [I thm:engineered, cor:D1; II thm:II-raised, II-flipext] | finitely supported, scale-INDEPENDENT one-sided data with kappa_w <= 1; Delta d >= 0 or (SC) | no exact two-piece data (scale-dependent switching through infinitely many carriers), or Delta d < 0 without (SC), or kappa_w > 1 | data-free mates: existence at all scales NOT constructed (3.2) |
| 9 | Theorem E family (windowed recovery through nearby rows) [II thm:II-E, II-ERT] | exact window data at rows second-order close to f | only approximate data at every nearby row ("exactness vs scale") | not constructed |
| 10 | error carrying (R3 Thm EC) | errors in a fixed finite-dimensional space | escaping (non-compact) errors (R3 (R1)) | not constructed |
| 11 | banks, near-contacts, far pulls, contact lemma, fresh zero-weight non-peaks (R3 4.4, II-Sec 2) | the c_0 base and Lemma 1.4 (far freedom) | CANNOT be removed by T; only made insufficient ("bounded conversion capacity") | - |
| 12 | box-dominated support [II thm:II-N] | F = N, Bx <= C_a |a|, (SC_I), (W_M) | F != N or failure of these | yes |
| 13 | all designed-T machinery (Parts I Sec 8, II, III) | signatures, ladders, generic weights, diagonal base, levers | choose a non-designed T | - |

Every hypothesis in rows 1-7 and 12-13 can be violated by a pair (f, g) with g in C(f) (the violations are even generic in the
appropriate fibres). Rows 8-10 are violated only by mates of a kind that has not been constructed (3.2). Row 11 is not a
hypothesis on (f, g) at all: it is the flexibility of NA rows, which an adversary can only out-scale.

## 3.2 What is known about killing everything at once

PROVED facts that point TOWARD the possibility of an obstruction:
 (P-a) The intrinsic mechanisms (rows 3-6) can all fail at once: for some admissible T there is a non-attaining f whose
       intrinsically recoverable mates lie on one line while C(f) is infinite dimensional [I thm:defect], and the canonical
       truncations do not recover them [I prop:nonrecovery].
 (P-b) Lower semicontinuity of the fibre map can fail along sequences of block-tame (hence recoverable) rows, even at recoverable f
       [II thm:II-NL, prop:II-NLreal]: recovery cannot be propagated along arbitrary dense sequences of good rows.
 (P-c) Every NA row near a non-attaining f differs from f in every block at infinitely many carriers: there are infinitely many common
       peaks of OPPOSITE sign (N2 Lemma 3.3, refereed). Consequently NA approximants must "scramble" every block below some depth, and for
       two-piece data with Delta d < 0 the convexity mechanism fails on one side with a first-order block cost >= 2M|tau rho c|, so the
       d-mismatch must be paid in the base (N2 Cor 3.4, refereed). This is a genuinely ONE-SIGNED effect; the opposite peaks exist at
       EVERY NA approximant, but the cost bound is proved for the transferred two-piece decompositions of N2 3.1, not for all
       decompositions at f'.
 (P-d) Exact switching requires infinitely many one-sided coordinates [I prop:exact], and exact two-piece data carry no switching at
       rows with F ∪ K finite [II cor:II-S2]; NA rows have F', K' finite. So every NA approximant must TERMINATE the switching of a
       switching mate below some scale (PROVED in the exact form; approximate form = M7).
 (P-e) Far rigidity is compatible with Lemma B (N2 4.5, SKETCH); (SC) can fail for admissible T ([I rem:withoutSC(b)], SKETCH).

PROVED facts that point AWAY from an obstruction:
 (Q-a) Every explicit candidate built so far was recovered: P1's exact resonances [I cor:exampleRecovered]; all d-neutral exact two-piece
       switching mates (Round 2, P2A/N2 Thm 1); Delta d >= 0 [I cor:D1]; E's critical cross mates (Averaging, in cl Cert); E's rigid
       design for compact errors (R3, EC; SKETCH modulo (HT-EC)); self-aligned and nested-tuning rows (II, U3); for T_fin every
       finite-support row (III MT VI).
 (Q-b) No non-recovery statement is known along ALL NA sequences at any row: (P-a), (P-b) and [II prop:II-S3] are relative to
       restricted approximant classes (canonical truncations; block-tame rows with prescribed alignment), and Prop II-S3 itself shows
       how NA rows escape (put the two test coordinates into the support of one strict non-peak: one generic carrier suffices).
 (Q-c) The bad rows form a meagre set (F2), the defect is open on the graph (F5), and the dangerous mate must stay away from the
       fibres of ALL generic rows nearby (Lemma 2.1(b)): it is an exceptional mate of an exceptional row. Exceptional mates exist
       (P-a), but none has been shown to be exceptional relative to NA rows.

NOT KNOWN (the real gap): (N-a) existence, for any admissible T, of (f, g) with g in C(f) whose switching is genuinely
scale-dependent at ALL small scales (approximate resonances through near-threshold carriers or weak peaks at every depth, no exact
two-piece data) — "a fixed point between T and f, constructed nowhere" (R3 5.1); (N-b) any lower bound for dist(rho g, C(f')) over
all NA rows f' near any f.

## 3.3 The transfer principle: where an obstruction would have to live (HEURISTIC, with PROVED ingredients)

(i) Exact finite data transfer uniformly in scale. Two-piece data use finitely many carriers and fixed base vectors; their expansion
    coefficients depend continuously on the forced data, so they transfer to every nearby row with errors that are o(t^2) uniformly for
    |t| below a fixed radius ([II lem:II-U], uniform one-sided transfer; Lemma F1 of Part I). This is why [I cor:D1] needs no rates of T.
    PROVED (the cited lemmas).
(ii) Scale-dependent data transfer only above a junction. A mate violating (M2) uses at scale t carriers in their linear (saturated)
    regime, i.e. at depths in (~t^2, ~t), with O(1) total content (the linear-regime terms sum to O(t^2) in excess, [BRIEFING (R5)]).
    By (P-c) every NA row f' agrees with f only down to some depth lambda(f') > 0 (opposite peaks below), and by Lemma 1.4 the
    approximant can make lambda(f') as small as it likes, at cost p*(f' - f) -> 0. At scales t with t^2 >> lambda(f') the linear-regime
    carriers are copied; at smaller scales f' must supply its own structure. So every NA approximant has a JUNCTION, at a depth it
    chooses. HEURISTIC (the "copying" statement is not proved for arbitrary T: threshold drift caused by the deep alterations can flip
    near-threshold carriers far above lambda when (MS) fails — the designed T protects against this with buffers, V1 Lemma DR).
(iii) Tools at the junction (all available for every T): banks (tiny support masses; total mass O(lambda log(1/lambda)) suffices to carry
    the base-converted linear-regime content of f's altered carriers at all scales between lambda and sqrt(lambda), estimate HEURISTIC),
    near-contacts (one-sided, cost eta|V| t), fresh zero-weight strict non-peaks (O(1) content at scales <= depth, O(s) content at scale s
    needs depth >~ s^2: R3 room lemma, PROVED), error carrying for compact error families (R3 Thm EC, PROVED), and the averaging theorem,
    which needs only J(rho, K) ~ K/(c_0(1 - rho^2)) adjacent scales of two-sided capacity ([I thm:averaging], PROVED).
(iv) Consequence. A counterexample must defeat these tools at EVERY junction depth, by a margin that does not shrink with the depth:
    a SELF-SIMILAR, constant-level obstruction carried by T at every depth and tied to f (fresh resonance at every stage: H2.B for the
    designed T; R3 (R5) recursive guarding for arbitrary T). At model level (E, Model N) bounded conversion capacity J gives a boundary
    excess R(J) > 1 decaying geometrically in J (R(1) ~ 1.19, R(2) ~ 1.04, R(3) ~ 1.009 in the error-dominated regime), and error
    carrying removes it for compact error directions (R3: R -> 1). So the obstruction must ALSO make the errors at every junction
    escape to infinity (non-compact). HEURISTIC/NUMERICAL (model level).

## 3.4 Concrete candidates for an adversarial (T, f, g), ranked by how much is already known

 (C1) Negative d-mismatch without scrambling control: a block in which a positive proportion of indices at every depth are exact
      zero-weight strict non-peaks ([I rem:withoutSC(b)], SKETCH), so that (SC) fails, and a mate with two-piece data, Delta d < 0 and
      kappa_w = 1 (tight). By (P-c) every NA approximant scrambles the block and pays the d-mismatch in the base on one side; the
      engineered estimate then fails for rho close to 1 ([I rem:withoutSC(a)]: recovery needs rho^2 kappa_w + rho sum |Delta d| K^scr < 1).
      OPEN whether other approximants (raised supports, banked companions, (PC*)-tuned rows: N2 Thm 3, Lemma R) avoid the cost for every
      admissible T. This is the candidate with the most PROVED one-signed structure; its weakness: the base cost is a KINK of
      Delta d R*(w' - w), and the approximant controls where R*(w' - w) lives (it can push the scrambling deep), so the obstruction needs a
      reason why the scrambling at the junction is comparable to the junction scale for EVERY approximant.
      A self-similar mechanism of exactly this kind is visible in the engineered construction (HEURISTIC reading of [I, rem:withoutSC(a)],
      K^scr = (scrambling)/s_1): to TERMINATE the switching below a scale s_1, the approximant puts window masses of size ~ s_1 |b^theta_j|
      on the window contacts; their Hilbert footprint U^*(Delta a) moves the normer by ~ s_1 sum_j |b^theta_j| ||U^* e_j^*||/nu on coarse
      coordinates, which changes the status of the carriers at depth <~ s_1 (those with Phi gap <= s_1); if a positive proportion of indices at
      every depth are zero-weight non-peaks (failure of (SC)), the scrambled mass is ~ s_1, so K^scr = O(1) at EVERY termination scale and, for
      Delta d < 0, the one-signed cost (P-c) is a constant fraction of the slack when kappa_w = 1 and rho -> 1. Escapes that an obstruction
      would have to close: (e1) footprint-free termination through BLOCK carriers (fresh zero-weight non-peaks at depth ~ s_1 carrying the
      switching two-sidedly) — this is the conversion-capacity question of (iv) again; (e2) bank efficiency (a base with ||U^* e_j^*|| tiny on
      the termination coordinates, as in the designed diagonal base) — an adversary removes it by choosing U with slowly decaying ||U^* e_j^*||
      (U is a free compact dense-range operator in the construction); (e3) raise transfer (same-sign raises on F cancel their l_1 mass against
      normalisation, [II lem:II-RT]) — applies to masses on F, not on contacts; (e4) d-consistency levers (designed T only).
 (C2) O3* (R3 5.1): error-dominated one-sided carriers of both peak types at all scales, escaping and recursively guarded critical
      errors; the chain-guard model suggests alternating types at ratio exactly 1 as the only configuration with bounded conversion
      capacity (R3 5.2, SKETCH). Nothing beyond model level.
 (C3) Type (II) of Theorem 1.9: two recoverable mates whose recovering approximants are incompatible (e.g. opposite sign requirements on
      the same far coordinates), with the midpoint not recoverable. No mechanism known; it is the only route not excluded by the fact that
      all positive constructions are mate-specific.

## 3.5 Verdict

 1. Killing all KNOWN mechanisms at once is conceivable: their hypotheses are independent, and the violations of rows 1-7 are generic.
    But killing mechanisms is not an obstruction. The approximant's freedom (row 11: far data, banks, near-contacts, fresh carriers)
    is not a finite list of tools; in fourteen rounds every adversarial feature was answered by a new mechanism (averaging, engineering,
    error carrying, convexity placement, Hoffman matching, exactification, levers), and no lower bound for dist(rho g, C(f')) over all NA
    rows has been proved anywhere. HEURISTIC (historical), PROVED in each instance cited.
 2. The present failure to prove density is a failure for ARBITRARY T of the explicit constructions, whose bottleneck is EXACTNESS
    (finite systems that must be solved exactly with one-sided levers). Lemma VT ([II lem:II-VT]) and G3 Prop 3.3 show that approximate data are tolerated
    up to violations of relative size O(1) times a small constant; so exactness is a feature of the method, and it becomes an invariant only
    if violations of relative size bounded below are forced at EVERY junction for EVERY approximant. No such invariant is known; (P-c) is the
    only approximant-independent one-signed effect proved so far, and it is first order in the scrambling, which the approximant controls.
 3. Therefore the evidence does not support switching to a negative programme wholesale. It does support a TARGETED negative test,
    because (a) a counterexample can only live at an adversarial T (for T_fin: only infinite F and failure of (LSC-trunc)); (b) for
    arbitrary T the open core is large (approximate resonances, Delta d < 0 without (SC), Gamma_w > 1, infinite F); (c) the decisive
    quantity — conversion capacity at a junction under adversarial rates, with escaping errors — is open even at model level.
 4. The missing invariant (formulated so that either answer is progress):
    (CAP+) [positive] for every admissible T, every f, g in C(f), rho < 1 and lambda_0 > 0 there is an NA row f' with a junction depth
           lambda < lambda_0 at which J(rho, K) adjacent scales of two-sided capacity carry rho g up to O(scale) (then averaging closes);
    (CAP-) [negative] an admissible T, a row f and a mate g, and a functional Psi(f', lambda) >= c > 0 for every NA row f' near f and every
           junction depth lambda, which lower-bounds the boundary excess (Model N's R - 1) and is monotone under banks, near-contacts, error
           carrying and fresh carriers. By Theorem 1.9 it is natural to aim first at a TYPE (I) obstruction: one fixed direction x in c_00 and,
           for every admissible normer x', a cheap multi-scale decomposition of x (Theorem 1.6(c)) — a purely primal object.
 Leaning: POSITIVE (density more likely), with low confidence for an arbitrary admissible T; no step of a negative proof exists.

# 4. Numerics (sanity checks only; scripts in neg/N1_work/)

No finite-dimensional model can exhibit non-density (every operator on a finite-dimensional space attains its norm); the checks
below only test inequalities used above.
 * twopoint_check.py: smooth norms on R^3 (l_4, and l_4 + 0.3||A.||_2). The support function max_{C(f')} v (LP over 2e3-1e5 sampled
   constraints |g(y)| <= r_{f'}(y), converged to 4 digits) never exceeds inf_tau of the two-point bound of Cor 1.7, and is often strictly
   below the Hessian bound (0.208 vs 0.358; 0.987 vs 1.685): r~ is a genuinely multi-scale infimum and Cor 1.7 is not sharp. Consistent.
 * angle_check.py: Prop 1.5(a) in R^3 with the l_4 norm: for 30 random (f, g, rho, delta) and perturbations of norm < delta, the norming
   direction satisfies |sin phi| <= 0.19 x 2 (delta/(1 - rho^2))^{1/2}. Consistent (random perturbations are far from the worst case).

# 5. Next steps (recommendation to the orchestrator)

 1. Do not abandon the positive programme for T_fin: a counterexample for T_fin needs infinite base support and a failure of
    (LSC-trunc)_N (F7); the negative question is a question about ADVERSARIAL admissible T.
 2. Targeted negative test, in this order:
    (a) Candidate C1 (Section 3.4), N = 1, adversarial base U (slowly decaying ||U^* e_j^*||), a positive proportion of zero-weight strict
        non-peaks at every depth, a two-piece mate with Delta d < 0 and kappa_w = 1. Sub-question: does EVERY norm-attaining approximant
        that terminates the switching at a scale s pay a scrambling mass >~ s on the wrong side (a lower bound for the termination
        footprint), or is there a footprint-free termination through block carriers (escape (e1))? Either answer is progress.
    (b) Aim any non-recovery proof at a TYPE (I) obstruction (Theorem 1.9): one fixed x in c_00 and, for every admissible normer x'
        (Lemma 1.4: window data, arbitrary far data, banks), an explicit cheap multi-scale decomposition of x (Theorem 1.6(c)). This is a
        purely primal, scalar target; it is equivalent to a convex (Hahn-Banach) separation from the local NA set (Prop 1.5bis).
    (c) Only afterwards O3* (C2): build the chain-guard design with alternating types at ratio 1 and escaping errors, and test the boundary
        excess with error carrying switched on (extend E's Model N by R3's EC and by banks).
 3. Positive counterparts that the analysis isolates (each would remove a whole class of potential counterexamples):
    (CAP+) unbounded conversion capacity at some junction for every admissible T; (P-II) a MERGING LEMMA (two NA approximant sequences
    recovering g_1 and g_2 can be merged; then Rec(f) is convex and density reduces to recovering X-exposed mates, Theorem 1.9);
    (P-I) recovery of X-exposed mates (the scalar statement limsup_{NA f' -> f} r~_{f'}(x) = r~_f(x)).
 4. Parallel track N2neg (adversarial construction) should use the necessary conditions of Section 2 as a checklist: any proposed
    (T, f, g) violating one of F1-F6, M1-M6, M8 is recovered by a refereed theorem.
