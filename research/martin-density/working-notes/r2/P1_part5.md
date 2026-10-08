# P1 part 5: the dual (support-function) route

## 5.1 Proposition (support-function criterion; reduction to c_0-exposed mates). PROVED.
Let A subset B be norm-compact convex symmetric subsets of l_1 = c_0* (e.g. A = cl Cert^sh(f), B = C(f), both norm compact:
A Thm 3.1). Then
 (a) A = B iff h_A(x) = h_B(x) for all x in a dense subset of c_0 (h_K(x) := max_{k in K} k(x));
 (b) A != B iff some c_0-EXPOSED point of B (the unique maximizer over B of some x in c_0) lies outside A; the set
     {x in c_0 : h_A(x) < h_B(x)} is then open and nonempty, and it contains a dense G_delta subset of exposing vectors.
*Proof.* (a) |h_K(x) - h_K(y)| <= (sup_K ||k||_1) ||x - y||_inf, and weak*-compact convex sets are separated by elements of c_0.
(b) If b in B \ A, separation gives x_0 with b(x_0) > h_A(x_0), hence h_B > h_A on a ball V around x_0. By Mazur's theorem (c_0
separable) the continuous convex function h_B is Gateaux differentiable on a dense G_delta G; for x in G its subdifferential, which
is the face argmax_B x (weak*-compactness of B), is a singleton {b_x}; for x in V cap G, b_x(x) = h_B(x) > h_A(x), so b_x is not in A. QED.

## 5.2 Proposition (scale-by-scale formula). PROVED.
C(f) = intersection over t != 0 of C_t := {g : p*(f + t g) <= s(t)} = (s(t) B_{p*} - f)/t, with
  h_{C_t}(x) = (s(t) p(x) - sign(t) f(x))/|t|,   min_{t != 0} h_{C_t}(y) = r_f(y) = sqrt(p(y)^2 - f(y)^2),
and r~_f(x) = h_{C(f)}(x) = inf { sum_i h_{C_{t_i}}(x_i) : sum_i x_i = x } (finite families), which is (R2).
*Proof.* The C_t are weak*-compact convex and contain 0; the support function of an intersection of such sets is the
weak*-lsc closure of the inf-convolution of their support functions, here a finite continuous sublinear function, hence equal to
it. The one-scale minimum: with t = tan(theta), h = (P - F cos theta)/sin theta (P = p(y), F = |f(y)|) is minimized at cos theta = F/P
with value sqrt(P^2 - F^2). QED.
Reading. The one-scale sets C_t are DECOMPOSITION-BLIND: they only see p*. Certificates, in contrast, are defined through the
forced decomposition and require one TWO-SIDED linear structure valid on a whole window of scales |tau| <= r(c). The variational
characterization therefore gives no handle on which decompositions realize the optimal mate: the maximizer g_x of a given x
over C(f) is only characterized by complementary slackness with the active scales/pieces of a minimizing family in 5.2, and
nothing in that characterization produces two-sided structure.

## 5.3 Proposition (explicit failure of "certificates achieve r~_f"). PROVED.
At the first row f of part 2 take j_1, j_2 in K' (j_1 != j_2) and x_* := e_{j_1} - (u(j_1)/u(j_2)) e_{j_2} in c_00 (u := u_{2,1}). Then
  h_{cl Cert^sh(f)}(x_*) = 0 < c u(j_1) <= r~_f(x_*),
and by 5.1(b) there is an open set of x near x_* whose exposed mates lie in Def(f).
*Proof.* cl Cert^sh(f) is contained in R u (Thm 2.4) and u(x_*) = 0. The mate g := g_{K_1} of Prop 2.3 with j_1 in K_1, j_2 notin K_1
satisfies g(x_*) = c u(j_1) - beta a(x_*) = c u(j_1) > 0 (a(x_*) = 0 since 1 notin {j_1, j_2}). QED.

## 5.4 Conclusion for the dual route (PROVED statements / HEURISTIC reading).
 * (PROVED) The defect is detectable from c_0: Def(f) != empty iff h_{cl Cert^sh(f)} < r~_f somewhere on c_0, iff some c_0-exposed
   mate is outside cl Cert^sh(f) (5.1). So it suffices, in any future positive attempt, to treat EXPOSED mates.
 * (PROVED) A scale-by-scale variational argument cannot show h_{cl Cert^sh(f)} = r~_f in general (5.3); the gap is produced
   exactly by the exact resonance (part 2/4.1): in the minimizing families of 5.2 for x_*, the active pieces live at both signs of
   t and the optimal mate uses the contact set K_1 on one side and the carrier plus K_2 on the other.
 * (HEURISTIC) In positive situations (no resonances, part 3.6(1)) the right dual statement would be: for every exposed mate g_x,
   the optimal pieces at scale t can be chosen "window + O(t)" on one side; by Thm 6.8 this would give g_x in cl Cert(f). The
   shift problem (Thm 3.7, second piece) remains: the window parts are only controlled in the weighted sense Gamma_w <= 1 + o(1)
   (C_notes Prop 8.1), not in the max sense H <= 1, unless the blocks' first-order coefficients vanish.
