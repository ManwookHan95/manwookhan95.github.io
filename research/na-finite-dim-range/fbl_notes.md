# fbl -- density of NA(FBL[E],Y) for finite-dimensional Y (free Banach lattices)

Key: fbl. Real scalars. Written 2026-10-30 by a workflow subagent.
Labels: PROVED (complete proof written here), KNOWN (reference; "confirmed" = web-search hit, URL in
Section 11; "FROM MEMORY" = not confirmed), SKETCH, HEURISTIC, OPEN, FALSE.

## 0. Summary

Verdict: OPEN for the whole class, with a complete positive answer (PROVED) for finite-dimensional E.

* Main theorem (Thm 5.2, PROVED). If dim E < oo, then for EVERY Banach space Y the norm-attaining
  finite-rank operators are dense in K(FBL[E],Y); in particular NA(FBL[E],Y) is dense in L(FBL[E],Y)
  for every finite-dimensional Y. This covers FBL(n) = FBL[l_1^n] (de Pagter-Wickstead), all n.
  The proof does NOT use any of the standard domain tools, and it cannot: for 2 <= dim E < oo the space
  FBL[E] is not reflexive, fails RNP, fails Schachermayer's property alpha (Prop 3.7), and is not an
  L_1-predual (Prop 3.6). It uses instead an exact characterization of NA(FBL[E],R) (Thm 4.1) and a
  "finite span" version of the lineability criterion (Lemma 5.1).
* Structure (PROVED): dual ball = weak*-closure of the (already absolutely convex) set of admissible
  signed point-evaluation sums; unit ball = closed solid convex hull of delta(B_E); norm of a finite
  combination of point evaluations; for dim E < oo: FBL[E] = C_ph(E^*) ~ C(S_{E^*}) with dual
  (M(S_{E^*}), N), N(nu) = sup_{x in B_E} int |u(x)| d|nu|(u), and the "zonoid formula"
  ||f|| = min{ ||rho|| : |f(u)| <= int |u(x)| d rho(x) }. FBL(1) = l_oo^2; for dim E >= 2 the norm is
  neither an M-norm nor an L-norm; FBL[E] is an L_1-predual iff dim E <= 1.
* Lineability (Section 6): spans of the lattice homomorphisms delta_{x^*} are weak*-dense but NOT
  norm-dense (dim E >= 2, PROVED). Whether NA(FBL(2),R) contains a norm-dense linear subspace is OPEN;
  a positive answer would follow from a positive answer for C(S^1), which Kadets-Lopez-Martin-Werner list
  as unknown for C_0(L). Not needed for density.
* Infinite-dimensional E (Section 7): OPEN, including FBL(A) = FBL[l_1(A)] for infinite A. Partial results
  (PROVED): exact NA criterion for operators whose adjoint takes values in finitely many point evaluations
  (any E); such operators are NA when E is reflexive and are limits of NA operators when E has property
  alpha (e.g. E = l_1(A)); a "pinning lemma" for E with property alpha reducing NA(FBL[E],Y) to a
  C(K)-type problem on one principal ideal, where the remaining obstacle is a weighted (uniform) version
  of the C(K) disjoint-support approximation; operators factoring through FBL[F] (dim F < oo) via a
  quotient with closed image of the ball are limits of NA operators. The finite-dimensional method does
  not extend directly because ||delta_u - delta_v|| >= max(||u||,||v||) for non-proportional u, v.
* Transfer / universality (Section 8): E is (1-)complemented in FBL[E] iff E is (1-)complemented in
  some Banach lattice (PROVED; KNOWN). No implication between "NA(FBL[E],Y) dense" and "NA(E,Y) dense"
  is known in either direction for infinite-dimensional E (OPEN); for every E for which we can decide
  one side, the other side is also known. Universality of the FBL class for the Johnson-Wolfe problem:
  NOT established (OPEN); only the trivial direction holds.
* Literature: no paper on plain (linear) norm-attaining operators FROM FBL[E] found; the existing work
  (Dantas-Martinez-Cervantes-Rodriguez Abellan-Rueda Zoca 2022; Bilokopytov-Garcia-Sanchez-de Hevia-
  Martinez-Cervantes-Tradacete 2025) concerns norm-attaining LATTICE HOMOMORPHISMS, a different notion
  that does fail (no Bishop-Phelps theorem for lattice homomorphisms).

## 1. Literature (task item (a))

L1. Dantas, Martinez-Cervantes, Rodriguez Abellan, Rueda Zoca, "Norm-attaining lattice homomorphisms",
 Rev. Mat. Iberoam. 38 (2022), no. 3, 981-1002; arXiv 2007.14907. KNOWN, confirmed (abstract level).
 Content (from abstract/snippets): first examples of lattice homomorphisms that do not attain their norm,
 found in free Banach lattices; NO Bishop-Phelps type theorem for lattice homomorphisms (some lattice
 homomorphisms are not norm limits of norm-attaining lattice homomorphisms); every lattice homomorphism on
 c_0, L_p, C(K), or any order continuous Banach lattice attains its norm (so no James theorem for this
 class); characterization of norm-attaining lattice homomorphisms on FBL[E] when E is l_1(A) or an
 isometric predual of l_1(A); dual of FBL(A) contains a disjoint family of cardinality 2^|A|
 (de Pagter-Wickstead question). Snippets of L2 say L1 contains "Conjecture 5.5": x^* in E^* attains its
 norm iff the induced lattice homomorphism x^*^ = delta_{x^*} on FBL[E] attains its norm, and "Lemma 5.8"
 (spaces with property (P) satisfy it).
L2. Bilokopytov, Garcia-Sanchez, de Hevia, Martinez-Cervantes, Tradacete, "Norm-attaining lattice
 homomorphisms and renormings of Banach lattices", arXiv 2502.10165 (2025), J. Funct. Anal. (ScienceDirect
 S002212362500432X). KNOWN, confirmed (abstract/snippets): every lattice homomorphism on an AM-space attains
 its norm; every infinite-dimensional C(K) has an equivalent lattice norm with a non-norm-attaining lattice
 homomorphism; a lattice with a strictly positive functional has a renorming whose only nontrivial NA
 lattice homomorphisms are coordinate functionals of atoms; the analogue of Conjecture 5.5 is FALSE for the
 free infinity-convex lattice FBL^(oo)[E]; for free p-convex lattices, p in [1,oo) (p = 1 is FBL[E]) the
 answer is unknown to the authors; there was a gap under the original definition of property (P) in L1,
 repaired via properties (P_p); c_0, l_1(Gamma), L_1(mu) (mu localizable) have (P_p).
L3. Dantas, Martinez-Cervantes, Rodriguez Abellan, Rueda Zoca, "Octahedral norms in free Banach lattices",
 RACSAM 115 (2021); arXiv 2007.05288. KNOWN, confirmed: FBL[E] has an octahedral norm for E an L_1(mu),
 a predual of a von Neumann algebra or of a JBW*-triple, the dual of an M-embedded space, the disc
 algebra, or when E^* is almost square; open whether some FBL[E] fails to be octahedral, and whether
 some FBL[E] has the Daugavet property. (Octahedrality is not related to NA-density by any known result.)
L4. Aviles, Rodriguez, Tradacete, "The free Banach lattice generated by a Banach space", J. Funct. Anal.
 274 (2018); arXiv 1706.08147. KNOWN, confirmed existence (journal data FROM MEMORY). Construction of
 FBL[E] as functions on E^* with the norm of the task; universal property; FBL(A) = FBL[l_1(A)]
 lattice isometrically; for dim E < oo, FBL[E] can be identified with C(S_{E^*}) (confirmed by a search
 summary of ART/related papers).
L5. Oikhberg, Taylor, Tradacete, Troitsky, "Free Banach lattices", J. Eur. Math. Soc. 28 (2026) 4387-4514;
 arXiv 2210.00614. KNOWN, confirmed (bibliographic; structure of FBL^(p)[E], sublattices, basic
 sequences; Theorem 9.20: E has a complemented l_1 iff l_1 is complemented in FBL[E] (snippet)).
L6. Aviles, Martinez-Cervantes, Rodriguez, Tradacete, "A Godefroy-Kalton principle for free Banach
 lattices", Israel J. Math. (2022); arXiv 2011.04639. KNOWN, confirmed: lattice-lifting property.
L7. "Complemented subspaces of Banach lattices", arXiv 2505.24084 (2025). KNOWN, confirmed snippet:
 if E is C1-isomorphic to a C2-complemented subspace of a Banach lattice then delta(E) is C1C2-complemented
 in FBL[E].
L8. Luiz, Miranda, "On norm-attaining positive operators between Banach lattices", arXiv 2409.14625,
 J. Math. Anal. Appl. 558 (2026). KNOWN, confirmed (positive operators; different notion).
L9. Garcia, Luiz, Miranda, "Norm attainment for multilinear operators and polynomials on Banach spaces and
 Banach lattices", arXiv 2605.12117 (May 2026). KNOWN, confirmed (compactness vs norm attainment;
 positive multilinear maps; different notion).
L10. Kadets, Lopez, Martin, Werner, "Norm attaining operators of finite rank", arXiv 1905.08272 (in "The
 Mathematical Legacy of Victor Lomonosov", De Gruyter 2020). KNOWN, confirmed: lineability criterion;
 quote from a search snippet: "For C_0(L), we do not know whether it is actually true that NA(C_0(L))
 contains a dense linear subspace."
L11. Johnson, Wolfe, "Norm attaining operators", Studia Math. 65 (1979) 7-19. KNOWN, confirmed
 (bibliographic + snippet: NA dense in L(C(K),C(S)) in the real case). The L_1-predual statement for
 compact operators quoted in the task: FROM MEMORY / task background.
L12. Schachermayer, "Norm attaining operators on some classical Banach spaces", Pacific J. Math. 105
 (1983) 427-438. KNOWN, confirmed: weakly compact operators from C(K) to any X are norm limits of NA
 operators; C[0,1] fails property B; an operator L_1[0,1] -> C[0,1] not approximable.
L13. Gao-Lau constant g(X) = inf{max(||x+y||,||x-y||): x,y in S_X} <= sqrt 2 for all X, dim >= 2.
 KNOWN, confirmed by snippet (e.g. arXiv 2407.14475). An elementary proof of what we need is in Lemma 3.5.
Searches for "free Banach lattice" together with "norm attaining operators", "property A", "property B",
"Lindenstrauss", 2023-2026, returned nothing on plain (linear) operators FROM FBL[E]. Conclusion:
density of NA(FBL[E],Y) for finite-dimensional Y is, to our search, NOT addressed in the literature,
not even for FBL(n). Everything in Sections 3-8 below is new as far as we can tell, except where marked.

## 2. Setting and basic facts for an arbitrary Banach space E

2.0 Definitions. H[E] = positively homogeneous f: E^* -> R. A finite family (x_i^*)_{i<=n} in E^* is
ADMISSIBLE if sup_{x in B_E} sum_i |x_i^*(x)| <= 1 (equivalently max over signs ||sum_i s_i x_i^*|| <= 1).
||f|| = sup{ sum_i |f(x_i^*)| : (x_i^*) admissible }. FBL[E] = closure (in this norm) of the vector
sublattice of H_0[E] = {||f|| < oo} generated by {delta_x : x in E}, delta_x(x^*) = x^*(x). Imported from
[L4] (KNOWN): ||delta_x|| = ||x||; universal property: for every Banach lattice X and T in L(E,X) there is a
unique lattice homomorphism T^: FBL[E] -> X with T^ delta_x = Tx, and ||T^|| = ||T||.
Elementary facts (PROVED, immediate from the definition): (i) |f| <= |g| pointwise implies ||f|| <= ||g||
(lattice norm); (ii) sup_{x^* in B_{E^*}} |f(x^*)| <= ||f|| (one-element families are admissible);
(iii) for x^* in E^*, delta_{x^*}: f -> f(x^*) is a lattice homomorphism FBL[E] -> R of norm ||x^*||
(<= by (ii) and homogeneity, >= by testing on delta_x); (iv) t delta_{x^*} = delta_{t x^*} for t >= 0
(positive homogeneity), but delta_{-x^*} != -delta_{x^*}.

Lemma 2.1 (domination; PROVED). If f in FBL[E], x_1..x_m in E and |f| <= sum_k |delta_{x_k}| pointwise on
E^*, then ||f|| <= sum_k ||x_k||.
Proof. For an admissible family, sum_i |f(x_i^*)| <= sum_k sum_i |x_i^*(x_k)| <= sum_k ||x_k||, because
sum_i |x_i^*(x_k)| = ||x_k|| sum_i |x_i^*(x_k/||x_k||)| <= ||x_k|| when x_k != 0. QED

Lemma 2.2 (induced homomorphisms; PROVED). For R in L(F,E) put Rbar := (delta_E o R)^ : FBL[F] -> FBL[E].
Then Rbar(g)(x^*) = g(R^* x^*) for g in FBL[F], x^* in E^*, and ||Rbar|| = ||R||.
Proof. ||Rbar|| = ||delta_E o R|| = ||R|| by the universal property. For fixed x^*, both g -> Rbar(g)(x^*)
and g -> g(R^*x^*) are continuous lattice homomorphisms FBL[F] -> R (by (iii)); on delta_y both give
x^*(Ry) = (R^*x^*)(y). Two continuous lattice homomorphisms that agree on delta(F) agree on the closed
sublattice generated by delta(F), which is FBL[F]. QED

Lemma 2.3 (finite-dimensional E; PROVED). Let d = dim E < oo, S := S_{E^*}. Then FBL[E] equals the space
C_ph(E^*) of all continuous positively homogeneous functions on E^*, and sup_S|f| <= ||f|| <= d sup_S|f|.
So f -> f|_S is a lattice isomorphism of FBL[E] onto C(S) (not isometric when d >= 2, see 3.4).
Proof. (a) delta_x is continuous and ph; lattice operations and linear combinations preserve this; by (ii)
FBL-limits are uniform limits on S, so FBL[E] is contained in C_ph(E^*). (b) Let (x_k, x_k^*)_{k<=d} be
an Auerbach system (||x_k|| = ||x_k^*|| = 1, x_k^*(x_l) = [k=l]). For u in E^*, u = sum_k u(x_k) x_k^*,
so ||u|| <= sum_k |u(x_k)|. For an admissible family, sum_i ||x_i^*|| <= sum_k sum_i |x_i^*(x_k)| <= d, and
sum_i |f(x_i^*)| = sum_i ||x_i^*|| |f(x_i^*/||x_i^*||)| <= d sup_S|f|. (c) Let L be the set of restrictions
to S of the vector lattice generated by the delta_x; L is a vector sublattice of C(S). Two-point
interpolation: let s != t in S and a, b real. If s, t are linearly independent there is x with s(x) = a,
t(x) = b, and delta_x works. Otherwise t = -s; take x with s(x) = 1 and g = a (delta_x)^+ + b (delta_x)^-:
g(s) = a, g(-s) = b. By the lattice (Kakutani-Krein) form of the Stone-Weierstrass theorem L is dense in
(C(S), sup). By (b), for g in C_ph(E^*) and g_n in the generated lattice with sup_S|g_n - g| -> 0 we get
||g_n - g|| <= d sup_S |g_n - g| -> 0, so g in FBL[E]. QED

Lemma 2.4 (finite combinations of point evaluations; any E; PROVED). Let u_1..u_n in E^* \ {0} be pairwise
non-positively-proportional (u_i != t u_j for t > 0, i != j) and c in R^n.
(a) For every x in E there is f in FBL[E] with |f| <= |delta_x| on E^* and f(u_i) = sign(c_i)|u_i(x)|.
(b) ||sum_i c_i delta_{u_i}|| = sup_{x in B_E} sum_i |c_i| |u_i(x)|.
(c) In the dual Banach lattice, |sum_i c_i delta_{u_i}| = sum_i |c_i| delta_{u_i}.
Proof. (a) W = span{u_i} is finite-dimensional; the map E -> W^*, z -> (w -> w(z)) is onto (otherwise a
nonzero w in W would vanish on E), so there are z_1..z_m in E (m = dim W) such that
Theta: W -> R^m, w -> (w(z_1),..,w(z_m)) is a linear bijection. Put p_i = (u_i(x), Theta(u_i)) in R^{1+m}.
The p_i are nonzero and pairwise non-positively-proportional (Theta is injective and linear). Let
q_i = p_i/|p_i| (Euclidean), distinct points of the sphere S^m; choose gamma in C(S^m) with |gamma| <= 1 and
gamma(q_i) = sign(c_i) (finitely many points; e.g. disjoint bumps). Define G(p) = |p_0| gamma(p/|p|) for
p != 0 (p_0 the first coordinate), G(0) = 0: G is continuous, ph, |G(p)| <= |p_0|, and
G(p_i) = |u_i(x)| sign(c_i). Let R: l_1^{1+m} -> E, R e_0 = x, R e_k = z_k. By Lemma 2.3 G lies in
FBL[l_1^{1+m}], and by Lemma 2.2 f := Rbar(G) lies in FBL[E] with f(x^*) = G(x^*(x), x^*(z_1),..,x^*(z_m)).
Hence |f(x^*)| <= |x^*(x)| and f(u_i) = G(p_i).
(b) "<=": for f in FBL[E], with M = sup_{x in B_E} sum|c_i||u_i(x)| > 0, the family (|c_i|u_i/M) is
admissible, so sum c_i f(u_i) <= sum |f(|c_i|u_i)| <= M ||f||. ">=": for x in B_E take f from (a);
||f|| <= ||x|| <= 1 by Lemma 2.1 and sum c_i f(u_i) = sum |c_i||u_i(x)|.
(c) Write phi = sum c_i delta_{u_i}. For g >= 0 in FBL[E], |phi|(g) = sup{phi(h): |h| <= g} <=
sum |c_i| g(u_i). For equality: as in (a) (with the same z_k) choose a ph continuous P on R^m with
P(Theta(u_i)) = sign(c_i) |Theta(u_i)| (Euclidean norm) and put Pt := Zbar(P) in FBL[E], Z: e_k -> z_k, so
Pt(u_i) = sign(c_i)|Theta(u_i)|; let h_M = (g ^ M Pt^+) - (g ^ M Pt^-). Since Pt^+ ^ Pt^- = 0, at every point
at most one term is nonzero, so |h_M| <= g; and h_M(u_i) = sign(c_i) min(g(u_i), M|Theta(u_i)|) =
sign(c_i) g(u_i) for M large. So |phi|(g) >= sum |c_i| g(u_i). QED

Lemma 2.5 (dual ball; PROVED). D := {sum_i s_i delta_{x_i^*}: (x_i^*) admissible, s_i = +-1} is absolutely
convex, ||f|| = sup_{phi in D} phi(f), and B_{FBL[E]^*} = weak*-closure of D (no convex hull needed).
Proof. By (iv), lambda sum s_i delta_{x_i^*} + (1-lambda) sum s'_j delta_{y_j^*} =
sum s_i delta_{lambda x_i^*} + sum s'_j delta_{(1-lambda) y_j^*}, and the merged family is admissible since
sup_x [lambda sum|x_i^*(x)| + (1-lambda) sum |y_j^*(x)|] <= 1. D is symmetric, contains 0 (empty family) and
t D subset D for t in [0,1]. The norm formula is the definition (choose s_i = sign f(x_i^*)). So D° = B_{FBL[E]},
and by the bipolar theorem B_{FBL[E]^*} = D°° = weak*-closed absolutely convex hull of D = weak*-cl(D). QED

Lemma 2.6 (unit ball; PROVED; very likely KNOWN, cf. [L4],[L5]). B_{FBL[E]} = cl conv U_{x in B_E}
[-|delta_x|, |delta_x|] (closed solid convex hull of delta(B_E)). Consequently ||phi|| =
sup_{x in B_E} |phi|(|delta_x|) for every phi in FBL[E]^*. If moreover B_E = cl absconv(G), then
||phi|| = sup_{x in G} |phi|(|delta_x|) and B_{FBL[E]} = cl conv U_{x in G} [-|delta_x|, |delta_x|].
Proof. Let C0 = conv U_{x in B_E}[-|delta_x|,|delta_x|] inside the free vector lattice FVL[E] generated by
delta(E) (intersected with FVL[E]), and p its Minkowski functional on FVL[E]. C0 is solid (Riesz
decomposition: if |h| <= sum lambda_k g_k with |g_k| <= |delta_{x_k}|, then h = sum h_k with
|h_k| <= lambda_k |delta_{x_k}|), convex, absorbing in FVL[E] (each element is dominated by a multiple of a
finite sum of |delta_x|), so p is a lattice seminorm with p(delta_x) <= ||x||. Let X_p be the completion of
FVL[E]/ker p (a Banach lattice) and q the quotient map; q o delta: E -> X_p has norm <= 1. By the universal
property there is a lattice homomorphism Q: FBL[E] -> X_p of norm <= 1 with Q delta_x = q delta_x; Q and q
agree on FVL[E] (lattice homomorphisms agreeing on generators). Hence p(h) = ||q h|| = ||Q h|| <= ||h|| on
FVL[E]. Conversely C0 is contained in B_{FBL[E]} (lattice norm, convexity), so ||h|| <= p(h). Thus
||.|| = p on FVL[E]; B_{FBL[E]} is the closure of {h in FVL[E]: ||h|| < 1}, contained in cl C0, contained in
B_{FBL[E]}. For phi: sup over [-|delta_x|,|delta_x|] of phi is |phi|(|delta_x|) (Riesz-Kantorovich), and
sup over a closed convex hull equals sup over the generating set. If B_E = cl absconv(G): x -> |phi|(|delta_x|)
is a continuous seminorm (|delta_{x+y}| <= |delta_x| + |delta_y|, evenness, bound ||phi|| ||x||), so its
supremum over B_E is its supremum over G; for the ball, if x = sum a_g g (finite, sum|a_g| <= 1) then
|delta_x| <= sum|a_g||delta_g| and Riesz decomposition gives [-|delta_x|,|delta_x|] inside
conv(U_g [-|delta_g|,|delta_g|]); for x = lim x_n of such points and |h| <= |delta_x|, the truncations
h_n = (h ^ |delta_{x_n}|) v (-|delta_{x_n}|) satisfy |h - h_n| <= |delta_{x - x_n}|, so ||h - h_n|| <= ||x - x_n||. QED

Lemma 2.7 (real lattice homomorphisms; PROVED; (a) KNOWN [L1],[L4]). (a) Every lattice homomorphism
phi: FBL[E] -> R equals delta_{x^*} with x^* = phi o delta (two lattice homomorphisms agreeing on delta(E)).
(b) delta_{x^*} is an atom of FBL[E]^*: if 0 <= psi <= delta_{x^*} then psi = t delta_{x^*}. Hence every phi in
FBL[E]^* splits as phi = t delta_{x^*} + phi' with phi' disjoint from delta_{x^*}, and
|phi + s delta_{x^*}| = |t + s| delta_{x^*} + |phi'| for all real s.
(c) For u, v non-positively-proportional: ||delta_u - delta_v|| = max(||u+v||, ||u-v||) >= max(||u||,||v||).
Hence delta_u is a norm limit of norm-attaining lattice homomorphisms iff delta_u itself attains its norm.
Proof. (b) N := ker delta_{x^*} is an ideal (lattice homomorphism). psi(f) <= delta_{x^*}(f) = 0 for f >= 0 in N,
so psi vanishes on N_+ and hence on N (f in N implies f^+, f^- in N). FBL[E]/N is at most one-dimensional,
so psi = t delta_{x^*}. FBL[E]^* is Dedekind complete; the band generated by the atom delta_{x^*} is
R delta_{x^*} and is a projection band; phi' := phi - P phi is disjoint from delta_{x^*}; the modulus of a sum of
disjoint elements is the sum of the moduli. (c) Lemma 2.4(b) with c = (1,-1):
sup_x (|u(x)| + |v(x)|) = sup_x max(|(u+v)(x)|, |(u-v)(x)|). If delta_{v_n} -> delta_u (u != 0) then eventually
v_n = t_n u with t_n > 0, t_n -> 1, and delta_{v_n} = t_n delta_u; norm attainment is invariant under positive
scaling. QED

## 3. Structure (task item (b))

Throughout 3.1-3.3 and 3.7: d = dim E < oo, S = S_{E^*}, FBL[E] = C_ph(E^*) (Lemma 2.3), and measures on S
act on ph functions by integration of their restrictions to S.

Prop 3.1 (dual of FBL[E], dim E < oo; PROVED). Every phi in FBL[E]^* is phi(f) = int_S f dnu for a unique
nu in M(S); the dual order is the order of measures (so |phi| <-> |nu|), and
  ||phi|| = N(nu) := sup_{x in B_E} int_S |u(x)| d|nu|(u),   N(nu) <= ||nu||_TV <= d N(nu).
In particular B_{FBL[E]^*} = {nu : N(nu) <= 1}.
Proof. Lemma 2.3 and the Riesz representation theorem give the identification as vector lattices.
">=": fix x in B_E, eps > 0, sigma = dnu/d|nu| (|sigma| = 1). By Lusin's theorem there is g in C(S),
|g| <= 1, with |nu|({g != sigma}) < eps. Let f(tu) = t g(u)|u(x)| (t >= 0, u in S). Then f in C_ph(E^*),
|f| <= |delta_x|, so ||f|| <= 1 (Lemma 2.1), and int f dnu = int g sigma |u(x)| d|nu| >= int|u(x)|d|nu| - 2 eps.
"<=": for nu = sum c_j delta_{u_j} with distinct u_j in S this is Lemma 2.4(b). For general nu, partition S
into Borel sets A_j of diameter < eta, pick u_j in A_j, nu_eta = sum_j nu(A_j) delta_{u_j}. For f in C(S),
int f dnu_eta -> int f dnu (uniform continuity), and N(nu_eta) <= sup_x sum_j int_{A_j} (|u(x)| + eta) d|nu|
<= N(nu) + eta ||nu||_TV, since |u_j(x) - u(x)| <= eta for u in A_j, x in B_E. Hence
int f dnu <= limsup N(nu_eta) ||f|| <= N(nu) ||f||. Finally |u(x)| <= 1 gives N <= TV, and with an Auerbach
system sum_k |u(x_k)| >= ||u|| = 1 on S, so ||nu||_TV <= sum_k int |u(x_k)| d|nu| <= d N(nu). QED

Prop 3.2 (zonoid formula; PROVED). For dim E < oo and f in FBL[E]:
  ||f|| = min{ ||rho|| : rho positive Radon measure on S_E, |f(u)| <= h_rho(u) := int_{S_E} |u(x)| drho(x) for all u in E^* }.
(h_rho is the support function of the zonoid int [-x,x] drho(x); so ||f|| is the least "mass" of a zonoid
whose support function dominates |f|.)
Proof. If |f| <= h_rho and (x_i^*) is admissible: sum_i |f(x_i^*)| <= int sum_i |x_i^*(x)| drho(x) <= ||rho||.
Conversely let ||f|| <= 1. K := {h_rho|_S : rho >= 0, ||rho|| <= 1} is convex and compact in C(S): rho -> h_rho is
continuous from the weak*-compact set of such rho into (C(S), sup), because h_rho(u) is weak*-continuous in rho
for each u and the family {h_rho} is uniformly bounded and 1-Lipschitz in u (Arzela-Ascoli). The set
K - C(S)_+ is convex and closed. If |f| were not in it, Hahn-Banach would give nu in M(S) and c with
int |f| dnu > c >= sup{int (k - g) dnu : k in K, g >= 0}. Finiteness of the sup over g >= 0 forces nu >= 0, and
then the sup equals sup_{rho} int int |u(x)| drho(x) dnu(u) = sup_{x in S_E} int |u(x)| dnu(u) = N(nu). But
int |f| dnu <= || |f| || N(nu) = ||f|| N(nu) <= N(nu) by Prop 3.1, a contradiction. So |f| <= h_rho for some
rho with ||rho|| <= 1; scaling gives the min (attained by compactness). QED

Prop 3.3 (extreme points; PROVED). If 1 <= dim E < oo, every extreme point of B_{FBL[E]} belongs to
{ +-delta_x, +-|delta_x| : x in S_E }.
Proof. Let f be extreme; ||f|| = 1. Take rho from Prop 3.2: ||rho|| = 1, |f| <= h_rho.
Step 1. Let B be Borel with 0 < rho(B) < 1, rho_1 = rho|_B, rho_2 = rho|_{S_E \ B}; h_rho = h_{rho_1} + h_{rho_2}.
Put f_i = f h_{rho_i}/h_rho on {h_rho > 0}, f_i = 0 elsewhere. f_i is continuous (|f_i| <= |f| <= h_rho near
zeros of h_rho) and ph, so f_i in FBL[E], |f_i| <= h_{rho_i}, ||f_i|| <= rho_i(S_E) (Prop 3.2, easy half).
f = rho(B) (f_1/rho(B)) + (1-rho(B)) (f_2/(1-rho(B))) is a convex combination of points of the ball, so
f_1 = rho(B) f, i.e. h_{rho_1} = rho(B) h_rho on Z := {f != 0} (an open cone, nonempty).
Step 2. For u in Z the measure B -> int_B |u(x)| drho(x) equals rho(B) h_rho(u) for all B, so |u(x)| = h_rho(u)
for rho-a.e. x. Using a countable dense subset of Z and continuity, for rho-a.e. x: |u(x)| = h_rho(u) for all
u in Z. If x, x' are two such points, Z is covered by the closed sets {u: u(x) = u(x')} and
{u: u(x) = -u(x')}; by Baire one has interior, so it is all of E^*, i.e. x' = +-x. Hence rho is carried by
{x_0, -x_0} for some x_0 in S_E, h_rho = |delta_{x_0}| and |f| <= |delta_{x_0}|.
Step 3. On H+ = {u(x_0) > 0} and H- = {u(x_0) < 0}, f = g |delta_{x_0}| with g continuous, |g| <= 1. If
|g(u_1)| < 1 at some u_1 in H+ U H-, a small continuous ph bump eta |delta_{x_0}| (0 <= eta <= 1 - |g| near u_1,
eta(u_1) > 0, eta supported in a small cone around u_1) gives f +- eta|delta_{x_0}| in B_{FBL[E]} (Lemma 2.1)
with midpoint f: contradiction. So |g| = 1 on H+ U H-; H+ and H- are convex hence connected, so g is a
constant e+ on H+ and e- on H-, and f = e+ (delta_{x_0})^+ + e- (delta_{x_0})^-, which is one of
|delta_{x_0}|, delta_{x_0}, -delta_{x_0}, -|delta_{x_0}|. QED

3.4 FBL(1), M-norms, L-norms (PROVED).
(a) FBL(1) = FBL[R] is lattice isometric to l_oo^2 via f -> (f(1), f(-1)). Indeed H[R] is 2-dimensional
(f(t) = t f(1) for t >= 0, f(t) = |t| f(-1) for t < 0), all of it lies in FBL[R] (Lemma 2.3), lattice operations
are pointwise, and for an admissible family (sum_i |x_i^*| <= 1) sum_i |f(x_i^*)| =
sum_{x_i^*>0} x_i^* |f(1)| + sum_{x_i^*<0} |x_i^*| |f(-1)| <= max(|f(1)|,|f(-1)|), with equality for the one-point
families {1} or {-1}.
(b) Never an L-norm (E != 0): (delta_x)^+ and (delta_x)^- are disjoint, each of norm ||x|| (>= by testing at a
norming functional, <= since both are <= |delta_x|), but ||(delta_x)^+ + (delta_x)^-|| = || |delta_x| || = ||x||.
(c) An M-norm iff dim E <= 1. For E = l_1^2 (FBL(2)): || |delta_{e_1}| v |delta_{e_2}| || = 2 (the family
{e_1^*, e_2^*} is admissible for l_1^2, giving >= 2; |delta_{e_1}| + |delta_{e_2}| dominates, giving <= 2),
while || |delta_{e_i}| || = 1. For general E with dim E >= 2: take u, w as in Lemma 3.5 (unit,
max ||u +- w|| <= sqrt 2); then {u/sqrt2, w/sqrt2} is admissible; for x, y in S_E with u(x), w(y) > 1 - eps,
|| |delta_x| v |delta_y| || >= (|u(x)| + |w(y)|)/sqrt 2 > (2 - 2eps)/sqrt 2 > 1.

Lemma 3.5 (elementary, PROVED; the bound is KNOWN [L13]). Every normed space G with dim G >= 2 contains
linearly independent u, w in S_G with max(||u+w||, ||u-w||) <= sqrt 2.
Proof. Fix u in S_G and v in S_G independent of u; w(t) = (cos t u + sin t v)/||cos t u + sin t v||,
t in [0,pi], is a continuous path in S_G from u to -u, and k(t) = ||u + w(t)|| - ||u - w(t)|| goes from 2 to -2.
Pick t0 in (0,pi) with k(t0) = 0 and put w0 = w(t0) (independent of u since sin t0 > 0),
c = ||u + w0|| = ||u - w0|| in (0, 2]. If c <= sqrt 2 take (u, w0). Otherwise take u' = (u + w0)/c and
w' = (u - w0)/c: unit, independent, u' + w' = 2u/c, u' - w' = 2w0/c, so ||u' +- w'|| = 2/c < sqrt 2. QED

Prop 3.6 (L_1-preduals; PROVED). FBL[E] is an L_1-predual iff dim E <= 1. If dim E >= 2, FBL[E]^* contains a
3-dimensional subspace that violates Hlawka's inequality, so FBL[E]^* is not isometric to a subspace of
any L_1(mu). (The Johnson-Wolfe L_1-predual tool is therefore never available for dim E >= 2.)
Proof. dim E <= 1: FBL[E] is {0} or l_oo^2 = C({-1,1}). Hlawka in L_1: for reals a, b, c,
|a|+|b|+|c|+|a+b+c| >= |a+b|+|b+c|+|c+a|. (If a, b, c have a common sign both sides equal 2(|a|+|b|+|c|).
Otherwise, by symmetry and a global sign change, a, b >= 0 > c = -t; the claim becomes
t + |a+b-t| >= |b-t| + |a-t|; check the cases t >= a+b (equality), max(a,b) <= t < a+b (a+b >= 2t-a-b),
min(a,b) <= t < max(a,b) (a+b >= max-min), t < min(a,b) (a+b >= a+b-2t).) Integrating, Hlawka holds in every
L_1(mu) and hence in all its subspaces. Now let dim E >= 2 and choose u, w in S_{E^*} by Lemma 3.5 applied to
G = E^*, c0 := max(||u+w||,||u-w||) <= sqrt 2. The functionals u, -u, w are pairwise non-positively-
proportional, so by Lemma 2.4(b) the element a delta_u + b delta_{-u} + c delta_w has norm
nu(|a|+|b|, |c|), nu(s,t) := sup_{y in B_E} (s|u(y)| + t|w(y)|), with nu(2,0) = nu(0,2) = 2 and
nu(1,1) = sup_y max(|(u+w)(y)|,|(u-w)(y)|) = c0. Take x = delta_u + delta_w, z = -delta_u + delta_w,
y = delta_{-u} - delta_w. Then ||x|| = ||y|| = ||z|| = ||x+y+z|| = nu(1,1) = c0 (x+y+z = delta_{-u} + delta_w),
x+y = delta_u + delta_{-u}, y+z = -delta_u + delta_{-u} have norm nu(2,0) = 2, and z+x = 2 delta_w has norm 2.
Hlawka would require 4 c0 >= 6, i.e. c0 >= 3/2 > sqrt 2. QED
(Numerical cross-check, fbl_scripts/l1embed.py: Hlawka and negative type fail in (R^3, nu(|a|+|b|,|c|)) for
nu = l_2, l_4, l_oo and hold for nu = l_1.)

Prop 3.7 (property alpha; PROVED). If 2 <= dim E < oo, FBL[E] fails Schachermayer's property alpha.
(FBL[R] = l_oo^2 has it.)
Proof. Property alpha gives B = cl absconv{x_l} with x_l^*(x_l) = 1 = ||x_l^*|| and |x_m^*(x_l)| <= r < 1 (l != m).
Each x_l is exposed by x_l^*: if y in B, x_l^*(y) = 1, approximate y by y_n = sum_m a_m x_m (sum|a_m| <= 1);
x_l^*(y_n) <= |a_l| + r(1 - |a_l|) -> 1 forces a_l -> 1 and ||y_n - a_l x_l|| <= 1 - |a_l| -> 0, so y = x_l.
Exposed points are extreme, so by Prop 3.3, B_{FBL[E]} = cl absconv{x_l} is contained in
C0 := cl conv{+-delta_x, +-|delta_x| : x in S_E}. Take u, v in S_{E^*} independent with ||u - v|| < ||u + v||
(v close to u). For phi = delta_u - delta_v and x in S_E: phi(+-delta_x) = +-(u - v)(x) and
phi(+-|delta_x|) = +-(|u(x)| - |v(x)|), both of modulus <= |(u-v)(x)|; so sup_{C0} phi <= ||u - v||. But by
Lemma 2.4(b) ||phi|| = max(||u+v||,||u-v||) = ||u + v|| > ||u - v||, so sup over the ball exceeds sup over C0,
contradicting B_{FBL[E]} subset C0. QED

Prop 3.8 (reflexivity, RNP; PROVED). If dim E >= 2, FBL[E] contains a subspace isomorphic to C(S^1), hence
c_0; so FBL[E] is not reflexive and fails RNP (and the Schur property). If dim E <= 1 it is finite-dimensional.
Proof. Let F be a 2-dimensional subspace, iota: F -> E. iotabar: FBL[F] -> FBL[E] (Lemma 2.2) has norm 1 and
||iotabar g|| >= sup_{x^* in B_{E^*}} |g(x^*|_F)| = sup_{B_{F^*}} |g| >= ||g||/2 (Hahn-Banach and Lemma 2.3, d = 2).
FBL[F] is isomorphic to C(S_{F^*}) and S_{F^*} is homeomorphic to the circle. QED
Remark 3.9. So for 2 <= dim E < oo none of the standard domain tools of the task (Lindenstrauss reflexive,
Bourgain RNP, Schachermayer alpha, Johnson-Wolfe L_1-predual) applies; quasi-alpha (Choi-Song) was not
examined. For infinite-dimensional E, property alpha of FBL[E] was not decided.

## 4. Norm-attaining functionals on FBL[E], dim E < oo

Notation: for nu in M(S), F_nu(x) := int_S |u(x)| d|nu|(u) (a continuous seminorm on E), so N(nu) = max_{B_E} F_nu,
attained on the compact set M_nu := {x in S_E : F_nu(x) = N(nu)} (F_nu is ph, so maxima lie on S_E if nu != 0).
I(nu) := supp nu^+ cap supp nu^- (closed supports of the Jordan parts).

Theorem 4.1 (characterization; PROVED). nu in M(S) attains its FBL[E]^*-norm iff there is x_0 in M_nu with
u(x_0) = 0 for every u in I(nu). In words: nu^+ and nu^- may "touch" only on the great sphere annihilating one
maximizer of F_nu. (For C(S) the criterion is I(nu) = empty.)
Proof. Sufficiency. Let x_0 be as stated, A = supp nu^+, B = supp nu^-, Z0 = {u in S : u(x_0) = 0}. A \ Z0 and
B \ Z0 are disjoint and relatively closed in the open set S \ Z0 (their closures meet only in I(nu), which
lies in Z0). By Tietze (metric space) there is g continuous on S \ Z0, |g| <= 1, g = 1 on A \ Z0, g = -1 on
B \ Z0. Put f(tu) = t g(u)|u(x_0)| for u in S \ Z0, t >= 0, and f = 0 on the cone over Z0. f is continuous
(|f| <= |delta_{x_0}|) and ph, so f in FBL[E] and ||f|| <= 1 (Lemma 2.1). Then int f dnu =
int_A |u(x_0)| dnu^+ + int_B |u(x_0)| dnu^- = F_nu(x_0) = N(nu) (on Z0 the integrand vanishes anyway).
Necessity. Let int f dnu = N(nu) with ||f|| = 1, and take rho (Prop 3.2): ||rho|| = 1, |f| <= h_rho. Then
N(nu) = int f dnu <= int |f| d|nu| <= int h_rho d|nu| = int_{S_E} F_nu drho <= N(nu). Equalities give:
(i) f >= 0 nu^+-a.e., f <= 0 nu^- -a.e.; (ii) |f| = h_rho |nu|-a.e.; (iii) F_nu = N(nu) rho-a.e., so
supp rho is contained in the closed set M_nu. By (i),(ii) and continuity f = h_rho on supp nu^+ and f = -h_rho
on supp nu^-, so h_rho = 0 on I(nu). For u in I(nu), 0 = h_rho(u) = int |u(x)| drho(x) gives u = 0 on supp rho.
Any x_0 in supp rho works. QED

Corollary 4.2 (PROVED). (a) If supp nu^+ cap supp nu^- = empty, nu attains its norm (at g|delta_{x_0}|, g an
Urysohn function, x_0 any maximizer of F_nu). In particular positive measures, finitely supported measures,
and every element of span{mu_1,..,mu_m} with mu_l >= 0 carried by pairwise disjoint compact sets K_l, attain
their norms. (b) NA(C(S),R) is strictly contained in NA(FBL[E],R) (as sets of measures) when dim E >= 2:
for E = l_2^2, nu = lambda|_{(0,pi/2)} - lambda|_{(pi/2,pi)} (arc length, angles) has I(nu) = {angle pi/2},
F_nu is constant (int_0^pi |cos(t - s)| dt = 2 for all s), so x_0 = e_1 is a maximizer annihilating I(nu).
(c) NA(FBL(2),R) is not a linear subspace: with lambda the normalized length measure on S (boundary of the
square, E = l_1^2) and C a fat Cantor subset of S (closed, nowhere dense, lambda(C cap U) > 0 for every open
U meeting C), nu_1 = lambda and nu_2 = -2 lambda|_C attain their norms (one sign each), but
nu_1 + nu_2 = lambda|_{S\C} - lambda|_C has I = C, which contains two linearly independent u, u'; no
x_0 != 0 is annihilated by both.

## 5. Main theorem: density for finite-dimensional E (task item (d))

Lemma 5.1 (finite-span criterion; PROVED; a localized form of the lineability lemma of [L10] /
Preprint B Lemma densesubspace). Let X, Y be Banach spaces, W a finite-dimensional subspace of X^* with
W subset NA(X,R), and S in L(X,Y) with S^*(Y^*) subset W. Then S in NA(X,Y).
Proof. S^* is weak*-to-weak* continuous with values in W, on which weak* and norm topologies coincide; so
y^* -> ||S^* y^*|| is weak*-continuous on the weak*-compact B_{Y^*} and attains its maximum ||S^*|| = ||S|| at
some y_0^*. S^* y_0^* in W attains its norm at some x_0 in S_X, and ||S x_0|| >= y_0^*(S x_0) =
(S^* y_0^*)(x_0) = ||S||. QED
Consequence. If for all phi_1..phi_k in X^* and eps > 0 there are psi_j with ||phi_j - psi_j|| < eps and
span{psi_j} subset NA(X,R), then finite-rank NA operators are dense in the finite-rank operators F(X,Y) for
every Y (approximate sum phi_j (x) y_j by sum psi_j (x) y_j); in particular NA(X,Y) is dense for dim Y < oo.

Theorem 5.2 (PROVED). Let dim E = d < oo and let Y be any Banach space. Every compact T: FBL[E] -> Y is a norm
limit of finite-rank operators S in NA(FBL[E],Y) whose adjoints take values in span{mu|_{K_1},..,mu|_{K_m}}
(mu >= 0, K_l pairwise disjoint compact). In particular NA(FBL[E],Y) is dense in L(FBL[E],Y) for every
finite-dimensional Y. This includes FBL(n) = FBL[l_1^n] for every n, and FBL(1) = l_oo^2 trivially.
Proof. Let eps > 0. T^* : Y^* -> (M(S), N) is compact; choose y_1^*,..,y_n^* in B_{Y^*} with
T^*(B_{Y^*}) inside the union of the N-balls of radius eps around T^* y_i^*. Put mu = sum_i |T^* y_i^*| (if
mu = 0 then ||T|| <= eps and S = 0 will do) and write T^* y_i^* = h_i mu with Borel |h_i| <= 1. Let
eps' = eps/(1 + mu(S)). Partition [-1,1]^n into finitely many Borel cubes of side < eps' and let A_1..A_m be the
nonempty preimages under (h_1,..,h_n): a Borel partition of S on each piece of which every h_i oscillates
by < eps'. By inner regularity choose compact K_l subset A_l with mu(A_l \ K_l) < eps/m; let
L = {l : mu(K_l) > 0} and J = S \ U_{l in L} K_l, so mu(J) < eps. Since T is compact, T^{**} maps FBL[E]^{**}
into Y (Gantmacher); with 1_{K_l} in M(S)^* = FBL[E]^{**} (nu -> nu(K_l)) put y_l := T^{**}(1_{K_l}) in Y, so
y^*(y_l) = (T^* y^*)(K_l). Define the finite-rank operator
   S f := sum_{l in L} ( int_{K_l} f dmu / mu(K_l) ) y_l .
Then S^* y^* = E(T^* y^*), where E nu := sum_{l in L} (nu(K_l)/mu(K_l)) mu|_{K_l}. E is a contraction for the
total variation norm. S^*(Y^*) lies in W = span{mu|_{K_l}: l in L}, and every element of W attains its norm
(Cor 4.2(a)), so S in NA(FBL[E],Y) by Lemma 5.1.
Estimate. E(h_i mu) = sum_l hbar_{i,l} mu|_{K_l} with hbar_{i,l} an average of h_i over K_l, so
|h_i - hbar_{i,l}| < eps' on K_l, and ||h_i mu - E(h_i mu)||_TV <= eps' mu(S) + mu(J) < 2 eps. For y^* in
B_{Y^*} pick i with N(T^* y^* - T^* y_i^*) < eps; using N <= TV <= d N (Prop 3.1) and ||E||_TV <= 1:
N(T^* y^* - S^* y^*) <= N(T^*y^* - T^*y_i^*) + ||T^*y_i^* - E T^* y_i^*||_TV + ||E(T^*y_i^* - T^*y^*)||_TV
<= eps + 2 eps + d eps. Hence ||T - S|| <= (3 + d) eps. QED
Remarks 5.3. (1) The proof is the C(K) argument for compact operators (cf. Johnson-Wolfe [L11],
Schachermayer [L12]) transplanted to the FBL norm; the only FBL-specific inputs are Prop 3.1 (dual norm
equivalent to total variation) and Cor 4.2(a) (disjointly signed measures attain the FBL-dual norm, which
uses compactness of B_E). (2) For finite-dimensional E nothing about E (polyhedral or not) matters.
(3) Not proved here: density in L(FBL[E],Y) for non-compact T and infinite-dimensional Y (for C[0,1]
itself Lindenstrauss property A is, to our knowledge, not settled; FROM MEMORY, not searched).

## 6. Lineability (task item (c))

Prop 6.1 (PROVED). For every E, span{delta_{x^*} : x^* in E^*} is weak*-dense in FBL[E]^*. If dim E >= 2 it is
NOT norm-dense; in fact there is phi in FBL[E]^* with dist(phi, span{delta_{x^*}}) > 0.
Proof. Weak*-density: if f in FBL[E] is annihilated by all delta_{x^*}, then f = 0 as a function on E^*.
Non-density: pick x_1^*, x_2^* independent in E^*, Q = (x_1^*, x_2^*): E -> R^2 (onto), z_1, z_2 in E with
x_j^*(z_k) = [j=k], lambda = normalized length measure on the Euclidean unit circle S_2 of R^2 = (R^2)^*, and
phi(f) := int_{S_2} f(Q^* v) dlambda(v) (bounded: |phi(f)| <= sup_{S_2} |f o Q^*| <= ||Q|| ||f||, by fact (ii)).
Let psi = sum_{i<=n} c_i delta_{y_i^*} be any finite combination. Let P = {(y_i^*(z_1), y_i^*(z_2))} (finitely
many points of R^2) and let G be continuous ph on R^2 with 0 <= G <= |v_1| + |v_2|, G = 0 on the rays through
P, and G = |v_1| + |v_2| outside angular neighbourhoods of these rays of total length < eta. Put f(x^*) :=
G(x^*(z_1), x^*(z_2)) = Rbar(G)(x^*), R: e_k -> z_k (Lemmas 2.2, 2.3). Then f(y_i^*) = 0, and since
|f| <= |delta_{z_1}| + |delta_{z_2}|, ||f|| <= ||z_1|| + ||z_2|| =: C (Lemma 2.1). Also f(Q^* v) = G(v), so
phi(f) >= int_{S_2} (|v_1| + |v_2|) dlambda - 2 eta = 4/pi - 2 eta. Hence ||phi - psi|| >= (4/pi - 2 eta)/C,
a bound independent of psi. QED
For dim E < oo: span{delta_u} is contained in NA(FBL[E],R) (Cor 4.2(a)) and its norm closure is the space of
purely atomic measures, a proper subspace of M(S) when dim E >= 2; the norm closure of NA is everything
(Bishop-Phelps) but NA itself is not a linear subspace (Cor 4.2(c)).

Prop 6.2 (PROVED, a one-way comparison). Let dim E < oo. If NA(C(S_{E^*}),R) contains a norm-dense linear
subspace V of M(S_{E^*}), then V is a norm-dense linear subspace of FBL[E]^* contained in NA(FBL[E],R).
Proof. On C(K) a measure attains its norm iff supp nu^+ cap supp nu^- is empty (if int f dnu = ||nu||_TV with
|f| <= 1 then f = 1 on supp nu^+ and f = -1 on supp nu^-; conversely Urysohn). Such measures are in
NA(FBL[E],R) by Cor 4.2(a), and N is equivalent to TV (Prop 3.1). QED
Status of the lineability question for FBL(2): OPEN. By Prop 6.2 it would follow from a positive answer for
C(S^1); Kadets-Lopez-Martin-Werner [L10] state that they do not know whether NA(C_0(L)) contains a dense linear
subspace (confirmed snippet). The converse of Prop 6.2 is unclear (NA(FBL[E],R) is strictly larger than the set
of disjointly signed measures, Cor 4.2(b), but only by "touching on one great sphere"). The question is moot for
density: Theorem 5.2 uses only the finite-span criterion (Lemma 5.1), which is always available here.
Natural linear subspaces inside NA(FBL(2),R) (PROVED by Cor 4.2(a)): span{delta_u}; for a fixed positive mu
carried by a compact zero-dimensional Z subset S, {g mu : g locally constant on Z} (each g takes finitely many
values on clopen pieces, so its positive and negative parts are carried by disjoint compact sets). Neither is
norm-dense; sums of such subspaces for different (Z, mu) can leave NA (Cor 4.2(c) is of this kind).

## 7. Infinite-dimensional E (including FBL(A), A infinite): partial results; the general case is OPEN

7.1 Finitely atomic operators. Call T in L(FBL[E],Y) (Y finite-dimensional) finitely atomic if
T f = sum_{i<=n} f(u_i) c_i with u_i in E^* \ {0} pairwise non-positively-proportional and c_i in Y \ {0}.
Then T^* y^* = sum_i y^*(c_i) delta_{u_i}. Put R_T := (u_1,..,u_n): E -> R^n and give R^n the norm
||a||_{Z_T} := sup_{y^* in B_{Y^*}} sum_i |y^*(c_i)| |a_i| (a norm, absolute in the coordinates).
Prop 7.1 (PROVED). ||T|| = ||R_T||_{E -> Z_T}, and if R_T attains its norm then T attains its norm.
Proof. By Lemma 2.4(b), ||T^*y^*|| = sup_{x in B_E} sum_i |y^*(c_i)||u_i(x)|; take sup over y^*. If
||R_T x_0||_{Z_T} = ||T|| with x_0 in S_E, choose y_0^* in B_{Y^*} attaining the sup defining ||R_T x_0||_{Z_T}
(compactness), and f from Lemma 2.4(a) for x = x_0 and the coefficients y_0^*(c_i): ||f|| <= 1 and
y_0^*(Tf) = sum_i |y_0^*(c_i)||u_i(x_0)| = ||T||, so ||Tf|| >= ||T||. QED
The converse (T in NA implies R_T in NA) contains, for n = 1, Conjecture 5.5 of [L1] (delta_{x^*} attains
its norm on FBL[E] iff x^* attains its norm on E), which is open for FBL[E] in general per [L2] and known for
E with property (P_p) (c_0, l_1(Gamma), L_1(mu) localizable) [L1],[L2]. So the converse is OPEN in general.
Corollary 7.2 (PROVED). (a) If E is reflexive, every finitely atomic T is norm-attaining (R_T has finite rank,
so x -> ||R_T x|| is weakly continuous on the weakly compact B_E). (b) For any E and any finite-dimensional
Banach lattice Y = (R^k, absolute norm, coordinatewise order), if S in NA(E,Y) then the lattice homomorphism
S^ (S^ f = (f(S^* e_j^*))_j) attains its norm, at delta_{x_0} if S attains at x_0 (||S^ delta_{x_0}|| =
||S x_0|| = ||S|| = ||S^||). (c) For the reverse kind of approximation note Lemma 2.7(c): lattice homomorphisms
at different points are far apart, so S^ is NOT approximated by (S_n)^ when S_n -> S, S_n != S.

7.2 Pinning for E with property alpha (e.g. E = l_1(A)). Let B_E = cl absconv{x_l : l in Lambda} with
x_l^* in S_{E^*}, x_l^*(x_l) = 1, |x_m^*(x_l)| <= r < 1 (l != m). For T in L(FBL[E],Y), dim Y < oo, put
Psi_T(l) := max_{y^* in B_{Y^*}} |T^*y^*|(|delta_{x_l}|) (the max exists: y^* -> |T^*y^*|(g) is ||g||-Lipschitz).
By Lemma 2.6, ||T|| = sup_l Psi_T(l).
Lemma 7.3 (pinning; PROVED). For every eps > 0 there are l_0 in Lambda and y_1 in S_Y such that
T' := T + eps delta_{x_{l_0}^*} (x) y_1 (i.e. T'f = Tf + eps f(x_{l_0}^*) y_1) satisfies ||T' - T|| = eps and
Psi_{T'}(l_0) >= Psi_{T'}(l) + eps(1-r)/2 for all l != l_0; hence ||T'|| = Psi_{T'}(l_0).
Proof. Choose l_0 with Psi_T(l_0) > sup Psi_T - eps(1-r)/2, y_0^* in S_{Y^*} with Psi_T(l_0) = |T^*y_0^*|(F),
F := |delta_{x_{l_0}}|. Write p = x_{l_0}^* and T^*y_0^* = t delta_p + phi' with phi' disjoint from delta_p
(Lemma 2.7(b)). Choose y_1 in S_Y with y_0^*(y_1) = 1, replaced by -y_1 if t < 0. Then
|T'^*y_0^*| = (|t| + eps) delta_p + |phi'|, and since delta_p(F) = |p(x_{l_0})| = 1,
Psi_{T'}(l_0) >= |T^*y_0^*|(F) + eps = Psi_T(l_0) + eps. For l != l_0 and any y^*, |T'^*y^*| <=
|T^*y^*| + eps|y^*(y_1)| delta_p, so Psi_{T'}(l) <= Psi_T(l) + eps |p(x_l)| <= Psi_T(l) + eps r. Subtract. QED
Prop 7.4 (AM-ideal reduction; PROVED). Let T' be as in Lemma 7.3, F = |delta_{x_{l_0}}|, I_F the principal ideal
generated by F with the order-unit norm ||g||_F = inf{c: |g| <= cF} (an AM-space with unit, i.e. C(K_F) by
Kakutani; ||g|| <= ||g||_F). Then ||T'|| = ||T'|_{I_F}||_{(I_F,||.||_F) -> Y}, and T' in NA(FBL[E],Y) iff
T'|_{I_F} in NA((I_F,||.||_F),Y).
Proof. For phi in FBL[E]^*, sup{phi(g): ||g||_F <= 1} = |phi|(F); so ||T'|_{I_F}|| = max_{y^*}|T'^*y^*|(F) =
Psi_{T'}(l_0) = ||T'||. If T'|_{I_F} attains at g, ||g||_F = 1, then ||g|| <= 1 and ||T'g|| = ||T'||.
Conversely let ||T'f|| = ||T'||, ||f|| = 1, y^* in S_{Y^*} with y^*(T'f) = ||T'||, phi = T'^*y^*; then
phi(f) = ||T'|| >= ||phi||. By Lemma 2.6 f = lim h_n, h_n = sum_l a_{l,n} g_{l,n} (finite convex combinations,
|g_{l,n}| <= |delta_{x_l}|). phi(g_{l,n}) <= |phi|(|delta_{x_l}|) <= Psi_{T'}(l) <= ||T'|| - eps(1-r)/2 for
l != l_0, so phi(h_n) -> ||T'|| forces a_{l_0,n} -> 1; then ||h_n - a_{l_0,n} g_{l_0,n}|| <= 1 - a_{l_0,n} -> 0,
g_{l_0,n} -> f, and f lies in the norm-closed interval [-F,F]: ||f||_F <= 1 and T'|_{I_F} attains at f. QED
Corollary 7.5 (PROVED). If E has property alpha (e.g. E = l_1(A), x_a = e_a, x_a^* = e_a^*, r = 0), every
finitely atomic T: FBL[E] -> Y is a norm limit of norm-attaining operators; in particular every lattice
homomorphism S^: FBL(A) -> Y (Y a finite-dimensional Banach lattice) is.
Proof. T' (Lemma 7.3) is finitely atomic (if x_{l_0}^* is a positive multiple of some u_i, merge the atoms).
x -> ||R_{T'} x||_{Z_{T'}} = sup_{y^*} |T'^*y^*|(|delta_x|) (Lemma 2.4(b),(c)) is a continuous even convex function,
so its sup over B_E is its sup over {x_l}, i.e. sup_l Psi_{T'}(l) = Psi_{T'}(l_0), attained at x_{l_0}.
Prop 7.1 gives T' in NA, and ||T' - T|| = eps. QED
Remaining obstacle for FBL(A) (precise). By Prop 7.4, density of NA(FBL[E],Y) for E with property alpha is
EQUIVALENT to: every pinned T' can be approximated by pinned T'' whose restriction to the AM-space I_F is
norm-attaining on C(K_F). The C(K) machinery (Theorem 5.2's construction) produces approximants on C(K_F)
that are small in the order-unit dual norm (total variation on K_F), but the perturbation must be small in
the FBL[E]^*-norm, which on functionals carried by I_F is the WEIGHTED quantity sup_l |rho|(|delta_{x_l}|):
directions in K_F where some other coordinate dominates the pinned one carry large weight. The needed step is
a uniform (over l) inner-regularity / junk-removal statement. OPEN.

7.3 Cylindrical operators. Prop 7.6 (PROVED). Let Q: E -> F be a linear surjection onto a finite-dimensional
F such that K := Q(B_E) is closed (automatic if E is reflexive; true if Q factors through a finite-dimensional
quotient of a norm-one projection; false e.g. for E = c_0, Q = u in l_1 \ c_00, where Q(B_E) is open). Let Y be
a Banach space and S in K(FBL[F],Y). Then S o Qbar is a norm limit of operators in NA(FBL[E],Y).
Proof. Let F_Q be F normed by the gauge of K (a symmetric convex body: bounded, closed, and absorbing by the
open mapping theorem). FBL[F_Q] is the same lattice C_ph(F^*) as FBL[F], with an equivalent norm, and Qbar
(g -> g o Q^*) has norm ||Q||_{E -> F_Q} <= 1 into FBL[F_Q]. Claim: ||R o Qbar|| = ||R||_{FBL[F_Q] -> Y} for every
R. "<=" is clear. ">=": by Lemma 2.6 (applied to F_Q) ||R|| = sup{||Rg|| : |g| <= |delta_y|, y in K}. For such
g (y != 0) write y = Qx with x in B_E and choose a linear J: F -> E with QJ = id_F and Jy = x (extend {y} to a
basis). Then f := Jbar g satisfies |f| = Jbar|g| <= Jbar|delta_y| = |delta_x| (Jbar is a positive lattice
homomorphism), so ||f|| <= 1, and Qbar f = (QJ)bar g = g; hence ||R Qbar|| >= ||Rg||. Now apply Theorem 5.2 to
S on FBL[F_Q]: S_n -> S with S_n in NA, and (proof of Thm 5.2 + Lemma 5.1 + Cor 4.2(a)) S_n attains its norm
at some g_n = theta_n |delta_{y_n}| with y_n in S_{F_Q} subset K. Lifting g_n as above gives f_n with
||f_n|| <= 1 and ||S_n Qbar f_n|| = ||S_n g_n|| = ||S_n|| = ||S_n Qbar||; and ||S_n Qbar - S Qbar|| <=
||S_n - S||_{F_Q} -> 0. QED

7.4 The finite-dimensional method does not extend directly. Prop 7.7 (PROVED). (a) Finitely atomic
functionals are not norm-dense (Prop 6.1). (b) The cylindrical functionals {Qbar^* nu : Q: E -> F of finite
rank, nu in FBL[F]^*} are not norm-dense in FBL(N)^* = FBL[l_1]^*: phi_oo := sum_i delta_{e_i^*} is a norm-one
functional (finite subfamilies of (e_i^*) are admissible for l_1, so sum_i |f(e_i^*)| <= ||f||; and
phi_oo(|delta_{e_1}|) = 1) at distance >= 1 from every cylindrical functional. phi_oo attains its norm.
Proof of (b). Let psi = Qbar^* nu. For n != k, f_{n,k} := (|delta_{e_n}| - |delta_{e_k}|)^+ satisfies
0 <= f_{n,k} <= |delta_{e_n}|, so ||f_{n,k}|| <= 1, and phi_oo(f_{n,k}) = sum_i (|e_i^*(e_n)| - |e_i^*(e_k)|)^+ = 1.
Qbar is a lattice homomorphism with Qbar delta_x = delta_{Qx}, so Qbar f_{n,k} = (|delta_{Qe_n}| - |delta_{Qe_k}|)^+,
which is dominated by |delta_{Q(e_n - e_k)}|; hence |psi(f_{n,k})| <= ||nu|| ||Q(e_n - e_k)||. (Q e_n) is bounded
in the finite-dimensional range of Q, so for every eta > 0 there are n != k with ||Q(e_n - e_k)|| < eta. Thus
||phi_oo - psi|| >= 1 - ||nu|| eta for all eta. QED
(c) Perturbing the "E-side" of a functional is not norm-continuous: Lemma 2.7(c). So one cannot reduce to
finite-dimensional E by approximating the E-part (Lindenstrauss/Bourgain/Schachermayer for E do not transfer
by composition).
Example 7.8 (PROVED; plain NA functionals near a non-NA lattice homomorphism). E = c_0, u in l_1 with
infinite support, u_1 > 0. For n with tau := ||u - P_n u||_1 <= u_1/2 put v := P_n u + 2 tau e_1 (in c_00) and
phi := delta_u - delta_{v-u}. Then ||phi - delta_u|| = ||v - u||_1 <= 3 tau -> 0, and (Lemma 2.4(b) with
|a| + |b| = max(|a+b|,|a-b|)) ||phi|| = max(||v||_1, ||2u - v||_1) = max(||u||_1 + tau, ||u||_1 - tau) =
||v||_1, attained by the convex function x -> |u(x)| + |(v-u)(x)| at x_0 = sum_{i<=n} sign(v_i) e_i in B_{c_0}.
By Prop 7.1 (n = 2 atoms, Y = R) phi attains its norm. (delta_u itself does not, by [L1],[L2]: c_0 has (P_p).)

7.5 Heuristics on the general case (HEURISTIC, not proofs).
(H1) A general phi in FBL[E]^* can be written phi(f) = int h V^(f) dmu with V: E -> L_1(mu) (the AL-space of
|phi|), V^ its lattice-homomorphic extension, |h| <= 1 (PROVED-level standard facts, not used above). Then
||T|| = sup_{x in B_E} ||H(.) V x(.)||_{L_1(mu) (x)_eps Y} for T = (phi_j) with common mu, H = (h_j): the
E-direction is a norm-attainment problem for an operator from E into L_1(mu) (x)_eps Y, coupled with a C(K)-type
sign-separation problem; only TV-type (multiplicative, restriction) perturbations of h and mu are cheap.
(H2) For FBL(N) one can build functionals with infinitely many sign-interlaced "clusters" all visible from the
pinned coordinate e_0 (atoms near s_b e_0^* + r e_b^* + t e_{gamma_b}^*, sum s_b = 1, r = 1/2). Junk removal
cluster by cluster costs ~ r in coordinate b (not small), yet a UNIFORM choice of compact sets in the
cluster parameter costs only r*eps (clusters are copies of each other), and spread atoms can be separated by
elements sum_k eps_k (F ^ M_k |delta_{z_k}|) with sum_k M_k ||z_k|| < oo (computed for
v_k = s_k e_0^* + r e_{b_k}^*: f = sum_k eps_k (F ^ (s_k/r)|delta_{e_{b_k}}|) separates all atoms). This
suggests a dichotomy (close atoms: cheap truncation; spread atoms: cheap separation) that might prove density
for FBL(A); not carried out.
(H3) Nothing found suggests a counterexample; by the Johnson-Wolfe background none is expected, and a
counterexample would have to use infinite-dimensional E (Theorem 5.2).
(In (H2) the separating element is to be truncated to [-F,F]; truncation does not change its values at the atoms.)

## 8. Transfer and universality (task item (e))

Prop 8.1 (complementation; PROVED; KNOWN in this form [L7], confirmed snippet). Let C >= 1. delta(E) is
C-complemented in FBL[E] iff E is isometric to a C-complemented subspace of some Banach lattice. In particular
delta(E) is 1-complemented when E is a Banach lattice (c_0, l_p, L_p, C(K), l_1(A), ...), with the projection
delta o (id_E)^ ; and delta(E) is not complemented at all when E is not isomorphic to a complemented subspace of
a Banach lattice (e.g. spaces failing Gordon-Lewis local unconditional structure such as the Schatten classes
S_p, p != 2: FROM MEMORY, not searched).
Proof. If J: E -> X is an isometric embedding into a Banach lattice and P: X -> J(E) a projection with
||P|| <= C, then J^ : FBL[E] -> X has norm 1 and Pi := delta o J^{-1} o P o J^ satisfies Pi delta_x = delta_x,
||Pi|| <= C. Conversely FBL[E] is a Banach lattice containing delta(E) isometrically. QED

Prop 8.2 (what transfers; PROVED). (a) If every finite-dimensional Y has Lindenstrauss property B (positive
Johnson-Wolfe answer), then NA(FBL[E],Y) is dense for all E and all finite-dimensional Y (trivial).
(b) For dim E < oo both NA(E,Y) (E reflexive) and NA(FBL[E],Y) (Theorem 5.2) are dense, for all f.d. Y.
(c) S in NA(E,Y) implies S^ in NA(FBL[E],Y) for every finite-dimensional Banach lattice Y (Cor 7.2(b)).
Prop 8.3 (why the standard transfer routes fail; PROVED statements, conclusions OPEN).
(i) Subspaces. delta(E) is an isometric copy of E in FBL[E], but density of NA cannot pass to subspaces in
general unless Johnson-Wolfe is solved: every X embeds isometrically into C(B_{X^*}), and NA(C(K),Y) is dense for
f.d. Y (compact operators, [L11],[L12] or the proof of Thm 5.2 with N replaced by TV).
(ii) 1-complemented subspaces. For a Banach lattice E the decomposition FBL[E] = delta(E) + ker (id_E)^ is not
an absolute (or lattice) sum, so summand-inheritance results for absolute/lattice sums (sibling notes
"sums_tensors", Theorem 2) do not apply. Example E = R: FBL[R] = l_oo^2 (coordinates (f(1), f(-1))),
delta(R) = {(t,-t)}, ker (id_R)^ = {f: f(1) = 0} = {(0,s)}; ||(1,-1) + (0,1)|| = 1 but ||(1,-1) + (0,-1)|| = 2
although the summands have the same norms. Whether NA-density for finite-dimensional ranges passes to
1-complemented subspaces in general is not known to us (not searched).
(iii) Quotients. Every Banach lattice X is a lattice quotient of FBL[X] ((id_X)^ is onto); no general
argument transfers NA-density to quotients.
(iv) Lattice-homomorphism extension. S -> S^ is an isometry L(E,Y) -> L(FBL[E],Y) for Banach lattices Y, but
NA operators near S^ are typically not lattice homomorphisms (Example 7.8), and their restrictions to
delta(E) need not attain their norm; norm-attaining lattice homomorphisms are not dense [L1] (Lemma 2.7(c)).
Conclusions. "NA(FBL[E],Y) dense => NA(E,Y) dense": OPEN (no argument; no possible test case, since no E
with NA(E,Y) non-dense is known for f.d. Y). "NA(E,.) dense for all f.d. ranges => NA(FBL[E],.) dense": OPEN
for infinite-dimensional E; it fails to follow even for E = l_1(A), c_0, l_2 by our methods (Section 7).
Universality of the FBL class for Johnson-Wolfe (JW <=> density for all FBL[E]): only "=>" is known
(Prop 8.2(a)); "<=" is NOT established (OPEN). By Theorem 5.2, any counterexample to JW inside the FBL class
must have dim E = oo.

## 9. Different notions that do fail (reported separately; they do NOT concern NA(FBL[E],Y))

* Norm-attaining LATTICE HOMOMORPHISMS: no Bishop-Phelps theorem [L1] (KNOWN, confirmed). Mechanism
  (PROVED here, Lemma 2.7): real lattice homomorphisms on FBL[E] are the delta_u, and
  ||delta_u - delta_v|| = max(||u+v||,||u-v||) >= max(||u||,||v||) for non-proportional u, v, so delta_u is a
  limit of norm-attaining lattice homomorphisms only if it attains its norm itself; for E = c_0 and
  u in l_1 \ c_00, delta_u does not attain its norm [L1],[L2] (KNOWN, snippet level). But delta_u IS a norm limit
  of plain norm-attaining functionals (Example 7.8), consistent with Bishop-Phelps.
* Renormings: every infinite-dimensional C(K) has an equivalent LATTICE norm with a non-norm-attaining lattice
  homomorphism; the analogue of Conjecture 5.5 fails for FBL^(oo)[E] [L2] (KNOWN, confirmed).
* Bishop-Phelps-Bollobas properties for positive operators/functionals (Acosta, Soleimani-Mourchehkhorti and
  others) and norm attainment of positive operators [L8], positive multilinear maps [L9]: different notions.
* The other failing notions listed in the task (strongly norm-attaining Lipschitz maps, bilinear forms) are not
  specific to free Banach lattices; nothing found connecting them to FBL[E].

## 10. Open questions (precise)

Q1. dim E = oo: is NA(FBL[E],Y) dense for every finite-dimensional Y? Test cases: E = l_1(N) (FBL(N)), c_0, l_2.
    A negative answer for some E and some f.d. Y would answer Johnson-Wolfe negatively.
Q2. (Reduction for property-alpha E, Prop 7.4.) Can every pinned operator be approximated, in the FBL[E]^*-
    weighted sense, by pinned operators whose restriction to the principal AM-ideal I_F is norm-attaining on
    C(K_F)? Equivalently a uniform-in-l version of inner regularity for the weights |delta_{x_l}| on K_F.
Q3. Does NA(FBL(2),R) contain a norm-dense linear subspace? (Implied by a positive answer for C(S^1) [L10].)
Q4. Vector version of [L1, Conj. 5.5]: for finitely atomic T, does T in NA force R_T in NA (Prop 7.1)?
Q5. Any implication between density for FBL[E] and density for E (Section 8).
Q6. Property alpha / quasi-alpha for FBL[E], dim E = oo (not decided here).

## 11. Sources (URLs of confirming search hits)

L1: https://arxiv.org/abs/2007.14907 ; https://ems.press/journals/rmi/articles/2040295 ;
    https://produccioncientifica.ugr.es/documentos/63bcb8def8c8215fcce543a4
L2: https://arxiv.org/pdf/2502.10165 ; https://www.sciencedirect.com/science/article/pii/S002212362500432X
L3: https://arxiv.org/pdf/2007.05288 ; https://link.springer.com/10.1007/s13398-020-00940-1
L4: https://arxiv.org/pdf/1706.08147
L5: https://ems.press/doi/10.4171/jems/1552 ; https://arxiv.org/pdf/2210.00614
L6: https://arxiv.org/pdf/2011.04639
L7: https://arxiv.org/pdf/2505.24084
L8: https://arxiv.org/pdf/2409.14625
L9: https://arxiv.org/pdf/2605.12117
L10: https://arxiv.org/pdf/1905.08272
L11: https://eudml.org/doc/218261
L12: https://msp.org/pjm/1983/105-2/pjm-v105-n2-p13-s.pdf
L13: https://arxiv.org/pdf/2407.14475
Other hits consulted: survey "Free objects in Banach space theory" https://arxiv.org/pdf/2302.10807 ;
Bandyopadhyay-Godefroy (J. Convex Anal. 13) https://www.heldermann.de/JCA/JCA13/JCA133/jca13042.htm ;
Dantas-Falco-Jung-Rodriguez-Vidanes https://arxiv.org/pdf/2311.17426 ; Acosta-Soleimani-Mourchehkhorti
https://arxiv.org/pdf/2106.05935 .
Network note: ems.press could not be fetched (host not allowed in this session); only WebSearch was used.
Scripts: /tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/fbl_scripts/l1embed.py

## 12. Numerical sanity checks (not proofs)
fbl_scripts/zonoid_check.py (same scratchpad folder as l1embed.py): (1) zonoid-formula LP on grids gives
|| max(|u_1|,|u_2|) || = 2.0000 in FBL(2) = FBL[l_1^2] (matches 3.4(c)) and 1.4142 in FBL[l_2^2];
(2) for random discrete nu on FBL[l_2^2], the LP value sup_{||f||<=1} int f dnu equals N(nu) to 5 digits
(Prop 3.1 / Lemma 2.4(b)); (3) F_nu is constant (= 2) for |nu| = arc length on a half circle (Cor 4.2(b)).
l1embed.py: Hlawka and negative type fail in (R^3, nu(|a|+|b|,|c|)) for nu = l_2, l_4, l_oo; hold for l_1.
