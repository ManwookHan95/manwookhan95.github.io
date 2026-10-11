# N1 part 1 — What a proof of NON-density must establish (exact formulation, dual form)

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
     gap noted at the end of [I, Section 9] (whether density into l_2^2 forces recovery of a whole fibre along one sequence).
     HEURISTIC/OPEN.
 Positive proofs, conversely, may split density into: (P-I) the scalar statement (b2) for all f and x [equivalently: recover every
 X-exposed mate], and (P-II) convexity of Rec(f) (a "merging lemma": two NA approximant sequences recovering g_1 and g_2 can be merged
 into one recovering both). Both are OPEN; (P-II) is new as a formulation.
