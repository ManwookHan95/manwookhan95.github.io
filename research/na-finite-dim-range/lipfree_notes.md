# key = lipfree. Lipschitz-free domains F(M), finite-dimensional ranges: is NA(F(M),Y) always dense?

## 0. Conventions, labels, bottom line

Labels: PROVED (complete proof in these notes), KNOWN (reference; [S] = confirmed by a web-search hit, URL
given; [M] = from memory only, not confirmed), SKETCH, HEURISTIC, OPEN, FALSE.

Real scalars. M is a complete pointed metric space with base point 0. Lip_0(M) = F(M)^* (isometrically);
delta: M -> F(M) is the canonical isometric embedding; for x != y the molecule is
m_{xy} = (delta_x - delta_y)/d(x,y). For a Banach space Y, every F in Lip_0(M,Y) has a unique linearization
T_F in L(F(M),Y) with T_F(delta_x) = F(x) and ||T_F|| = Lip(F); F -> T_F is an onto isometry
Lip_0(M,Y) -> L(F(M),Y). Notions of attainment:
 * NA(F(M),Y) (the object of the question, "weak" attainment): T_F attains its norm on B_{F(M)}.
 * SNA(M,Y) ("strong" attainment): ||F(x)-F(y)|| = Lip(F) d(x,y) for some x != y. Since m_{xy} lies in
   S_{F(M)}, SNA(M,Y) is contained in NA(F(M),Y) (identifying F with T_F). The inclusion is strict in
   general (Section 2.3).
 * DNA (directional attainment, defined in Section 4.2) sits between SNA and NA for Banach domains.

Background used (from the task; standard): Lindenstrauss property beta of Y gives property B; finite-dimensional
polyhedral Y have beta, so only non-polyhedral finite-dimensional Y (e.g. l_2^2) matter. The Johnson-Wolfe
question (does every finite-dimensional Y have property B?) is OPEN, even for l_2^2.

BOTTOM LINE (verdict OPEN).
 1. Nothing in the literature I could find settles "NA(F(M),Y) dense for every M and every finite-dimensional
    Y". A negative answer for one M and one Y would refute property B for Y (the Johnson-Wolfe question).
    A positive answer is implied by a positive answer to Johnson-Wolfe, but not conversely as far as I can prove.
 2. Positive classes (known plus new here): F(M) with the RNP (M purely 1-unrectifiable); F(M) = L_1(mu) (closed
    subsets of R, subsets of R-trees containing their branching points); F(M) with property alpha or
    quasi-alpha, or SNA dense; NEW (PROVED here): C^1 simple closed curves and arcs, in particular the Euclidean
    circle T. This is notable because F(T) FAILS Lindenstrauss property A (Jung-Martin-Rueda Zoca 2023);
    that failure needs infinite-dimensional ranges. Also new: stability under wedge sums (l_1-sums).
 3. Lineability criterion: holds for M a subset of R, for C^1 curves, and for bounded uniformly discrete M with
    a well-ordered distance set. It is OPEN for M = R^2 and for general uniformly discrete M.
 4. Transfer F(X) -> X (X separable): PROVED in the "directional" form (Lemma DT). If a linear T is a
    Lip-norm limit of directionally (in particular strongly) norm-attaining Lipschitz maps, then T is a limit
    of NA(X,Y). So "linear maps are approximable by SNA maps" is equivalent to "NA(X,Y) dense". The full
    transfer from NA(F(X),Y) is OPEN. The missing step is to rule out attainment at elements of F(X) that
    carry no norm direction. Such elements exist: an isometric, nowhere-differentiable copy of R in c_0
    gives an isometric copy of L_1 inside F(c_0).
 5. Martin's renormings: F(X) is a counterexample candidate at least as strong as X, in the precise
    directional sense of Corollary DT2. Nothing more can be proved here; there is no evidence of failure.
 6. Hard open test case where the linear problem is trivial: M = R^2 (equivalently X = l_2^2 as a metric space),
    Y = l_2^2. None of the standard tools applies to F(R^2).

## 1. Literature status (part (a))

### 1.1 Papers asked about
 * Kadets, Martin, Soloviova, "Norm-attaining Lipschitz functionals", Banach J. Math. Anal. 10 (2016) 621-637,
   arXiv 1601.07821. KNOWN [S]. The strongly norm-attaining Lipschitz functionals on a Banach space are
   weakly dense but NOT norm dense in Lip_0(X). The paper introduces directional attainment, and directionally
   norm-attaining functionals are dense for uniformly convex X.
   URL: https://ar5iv.labs.arxiv.org/html/1601.07821 ; https://projecteuclid.org/journals/banach-journal-of-mathematical-analysis/volume-10/issue-3/Norm-attaining-Lipschitz-functionals/10.1215/17358787-3639646.full
 * Godefroy, "On norm attaining Lipschitz maps between Banach spaces", Pure Appl. Funct. Anal. 1 (2016).
   KNOWN, but only through citing papers [S, indirect]. It contains: a moduli inequality for Lipschitz
   isomorphisms attaining their norm in a direction, and examples of pairs (X,Y) where (a weak form of)
   norm-attaining Lipschitz maps are not dense, one of them with a Kadets-Klee norm. The journal page was not
   found. Snippet source: https://ar5iv.labs.arxiv.org/html/2203.12782 . A search snippet from the CGMR circle
   of papers states: SNA(M,Y) is dense when M is compact, lip_0(M) separates points uniformly, and Y is
   finite-dimensional [S]. Attributing this to Godefroy 2016 is FROM MEMORY. Such M give F(M) a separable dual,
   hence the RNP, so the case is subsumed by (K1).
 * Cascales, Chiclana, Garcia-Lirola, Martin, Rueda Zoca, "On strongly norm attaining Lipschitz maps",
   J. Funct. Anal. 277 (2019) 1677-1717, arXiv 1807.03363. KNOWN [S]. Several linear properties of F(M) give
   property A (RNP, property alpha / quasi-alpha, a uniformly strongly exposed 1-norming set of molecules), and
   each of them gives norm density of SNA(M,Y) for EVERY Y. In particular, if F(M) has the RNP then SNA(M,Y) is
   dense for every Y [S, via Chiclana's thesis snippet].
   URL: https://ar5iv.labs.arxiv.org/html/1807.03363 ; https://www.sciencedirect.com/science/article/pii/S002212361830449X
 * Chiclana, Garcia-Lirola, Martin, Rueda Zoca, "Examples and applications of the density of strongly norm
   attaining Lipschitz maps", Rev. Mat. Iberoam. 37 (2021) 1917-1951, arXiv 1907.07698. KNOWN [S].
   SNA(T,Y) is NOT dense for ANY Banach space Y, where T is the Euclidean unit circle. There are metric spaces
   containing an isometric copy of [0,1] (so F(M) fails the RNP) for which SNA(M,Y) is dense for every Y.
   For boundedly compact M with SNA(M,R) dense, B_{F(M)} is the closed convex hull of its strongly exposed
   points. URL: https://arxiv.org/pdf/1907.07698 ; https://ems.press/journals/rmi/articles/17450
 * Chiclana, Martin, "The Bishop-Phelps-Bollobas property for Lipschitz maps", Nonlinear Anal. 188 (2019)
   158-178. KNOWN [S]. Lip-BPB (a strong-attainment notion): (M,Y) has it when M is finite and Y is
   finite-dimensional, and both finiteness assumptions are needed; uniformly Gromov concave M has it for every
   Y (also finite concave, ultrametric, and Holder spaces). Follow-up: Studia Math. 264 (2022) 121-147.
   URL: https://produccioncientifica.ugr.es/documentos/61b4fcbdff6ada1aa9a09c85?lang=en
 * G. Choi, "Norm attaining Lipschitz maps toward vectors", Proc. Amer. Math. Soc. 151 (2023) 1729-1741,
   arXiv 2203.12782. KNOWN [S]. On a large class of M (including infinite subsets of finite-dimensional
   spaces), every Lipschitz map attains its norm toward a vector iff Y is finite-dimensional. For
   finite-dimensional Y this notion is therefore trivially satisfied and irrelevant to our question.
   URL: https://doi.org/10.1090/proc/16284
 * arXiv 1907.01936 = G. Choi, Y. S. Choi, M. Martin, "Emerging notions of norm attainment for Lipschitz maps
   between Banach spaces", J. Math. Anal. Appl. 483 (2020) 123600. KNOWN [S]. It classifies the notions
   (strong, directional, derivative-type, ...) and their inclusions, and characterizes the RNP of the range Y
   by density of norm-attaining Lipschitz maps into Y; it has results for uniformly convex domains with
   finite-dimensional corollaries. Exact statements were NOT verified (full text unreachable).
   URL: https://arxiv.org/pdf/1907.01936
 * arXiv 2407.10710 = L. C. Garcia-Lirola, J. Guerrero-Viu, A. Rueda Zoca, "Projective tensor products where
   every element is norm-attaining" (2024). KNOWN [S]. It concerns norm-attaining TENSORS (elements of
   X (x)_pi Y with an optimal representation), which is a different notion. It gives new examples where X is a
   Lipschitz-free space, and density of norm-attaining tensors in L_1(mu) (x)_pi Y (any Y), or when X has the
   metric pi-property and Y is a dual with the RNP. It is not about NA(F(M),Y) for operators.
   URL: https://ui.adsabs.harvard.edu/abs/2024arXiv240710710G/abstract ; https://arxiv.org/html/2407.10710v1
 * Aliaga, Gartland, Petitjean, Prochazka, "Purely 1-unrectifiable metric spaces and locally flat Lipschitz
   functions", Trans. Amer. Math. Soc. (2022), arXiv 2103.09370. KNOWN [S]. For compact M, F(M) is a dual
   space iff M is purely 1-unrectifiable (p1u). For complete M, F(M) has the RNP (equivalently the Schur
   property) iff M is p1u [S, via later papers 2411.08369 and 2606.02918 quoting it].
   URL: https://arxiv.org/pdf/2103.09370 ; https://arxiv.org/html/2411.08369v1
 * Godard, "Tree metrics and their Lipschitz-free spaces", Proc. Amer. Math. Soc. 138 (2010) 4311-4320,
   arXiv 0904.3178. KNOWN [S]. It computes F(M) for M a subset of R. For complete M: F(M) is isometric to a
   subspace of L_1 iff M is isometric to a subset of an R-tree. If M is a subset of an R-tree containing all
   its branching points, then F(M) is isometric to some L_1(mu) [S, as summarized by a citing paper].
   URL: https://www.ams.org/proc/2010-138-12/S0002-9939-2010-10421-5/
 * Kalton, "Spaces of Lipschitz and Holder functions and their applications", Collect. Math. 55 (2004)
   171-217. KNOWN [S]. For uniformly discrete M, F(M) has the AP and the RNP (Prop. 4.4).
   URL: https://www.raco.cat/index.php/CollectaneaMathematica/article/view/56573
 * Dalet, "Free spaces over some proper metric spaces" (Mediterr. J. Math. 2015), arXiv 1404.3939. KNOWN [S].
   For countable proper M, F(M) is isometric to a dual and has the MAP; the same holds for proper
   ultrametric M. Also Dalet, "Free spaces over countable compact metric spaces" (PAMS 2015) [S].
   URL: https://ar5iv.labs.arxiv.org/html/1404.3939
 * Aliaga, Pernecka, Smith, "Convex integrals of molecules in Lipschitz-free spaces", J. Funct. Anal. (2024),
   arXiv 2302.13951. KNOWN [S]. It introduces convex integrals of molecules (de Leeuw based) and shows they
   differ in general from convex series. ALL elements of F(M) are convex series of molecules when M is
   uniformly discrete. Same authors, arXiv 2412.04312 (v2 2026): every element of F(M) is a convex series of
   elements with compact support; when F(M) has the RNP every element is a convex integral of molecules; all
   extreme points of B_{F(M)} are elementary molecules. Companion: Smith, arXiv 2412.05177.
   URL: https://arxiv.org/html/2302.13951v3 ; https://arxiv.org/abs/2412.04312v2

### 1.2 Other relevant items (2016-2026)
 * Jung, Martin, Rueda Zoca, "Residuality in the set of norm attaining operators between Banach spaces",
   J. Funct. Anal. 284 (2023) 109746, arXiv 2203.04023. KNOWN [S]: Example 5.2 there reads "the separable space
   F(T) fails to have property A". It is deduced from the non-density of SNA(T,R) via their Corollary 5.1. The
   witnessing range is not identified in the snippet. By Proposition C below it must be infinite-dimensional.
   URL: https://arxiv.org/pdf/2203.04023
 * Aviles, Martinez-Cervantes, Rueda Zoca, Tradacete, "Infinite dimensional spaces in the set of strongly
   norm-attaining Lipschitz maps", Rev. Mat. Iberoam. (2024), arXiv 2204.12529. KNOWN [S]: for every infinite
   complete M, SNA(M,R) contains a linear subspace isomorphic to c_0 (answering Kadets-Roldan). Hence
   NA(F(M),R) is always lineable; DENSE lineability is a different and open matter (Section 3).
   URL: https://ems.press/journals/rmi/articles/10143994
 * G. Choi, M. Jung, arXiv 2312.00393 ("Embeddings of infinite-dimensional spaces in the sets of norm-attaining
   Lipschitz functions"). KNOWN [S]: pointwise norm-attainment; c_0 / l_infinity embeddings; an example where
   the norm-attaining functionals on F(M) contain no isometric copy of c_0. URL: https://arxiv.org/abs/2312.00393v1
 * G. Choi, arXiv 2410.16607 (Studia Math. 2026), "Approximations of Lipschitz maps with maximal derivatives on
   Banach spaces". KNOWN [S]: characterizes the RNP of the range through approximation by strongly norm
   attaining and maximal-derivative attaining maps, for every renorming of the range.
   URL: https://arxiv.org/html/2410.16607v1
 * Cuth, Kalenda, Kaplicky, Mathematika 63 (2017) 538-552, arXiv 1610.03966. KNOWN [S]: for a convex open domain
   Omega in a finite-dimensional normed space E, F(Omega) is canonically isometric to L_1(Omega,E) modulo the
   divergence-free fields. URL: https://arxiv.org/pdf/1610.03966
 * Background, [M]: Uhl (Pacific J. Math. 63 (1976)): NA(L_1[0,1],Y) is dense if Y has the RNP; Bourgain
   (1977): RNP implies property A; Godefroy-Kalton (Studia Math. 2003): isometric linear lifting
   iota: X -> F(X) for separable X; Aronszajn (1976) / Phelps (1978): Lipschitz maps from separable X into
   RNP spaces are Gateaux differentiable outside a Gauss-null set; Dacorogna-Marcellini (scalar differential
   inclusions).

### 1.3 Answer to (a)
Is it KNOWN whether NA(F(M),Y) is dense for every M and every finite-dimensional Y? NO. I found no paper
stating or settling it. The literature studies SNA(M,Y) (strong), directional/derivative notions, property A
of F(M) (all Y), and norm-attaining tensors. It is known (density for every finite-dimensional Y) in these cases:
 (K1) F(M) has the RNP (M p1u: uniformly discrete, countable complete, proper countable, proper ultrametric,
      snowflakes, compact M with lip_0 separating points, ...), via Bourgain or CCGMR. SNA is even dense.
 (K2) F(M) isometric to L_1(mu) (M a closed subset of R; M a subset of an R-tree containing its branching
      points), via Uhl or Section 2.
 (K3) F(M) with property alpha / quasi-alpha / a uniformly strongly exposed norming set of molecules (CCGMR);
      the CGMR examples with SNA dense (these may contain [0,1]).
 (K4) Trivially: M finite; Y polyhedral (Lindenstrauss).
NEW here: C^1 curves including T (Proposition C), wedge sums of the class (Proposition 2.5), and bounded
uniformly discrete M with a well-ordered distance set (lineability; density was already known by K1).

## 2. Reductions (part (b))

### 2.1 Lemma L (lineability criterion) -- PROVED (task background; Preprint B Lemma densesubspace)
Let X be a Banach space and V a linear subspace of X^*, norm-dense in X^*, with V contained in NA(X,R). Then
NA(X,Y) is dense in L(X,Y) for every finite-dimensional Y.
Proof. Fix a basis y_1..y_k of Y with dual functionals y_1^*..y_k^* in Y^*. Every T in L(X,Y) is
T = sum_i phi_i (x) y_i with phi_i = y_i^* o T in X^*. Given eps > 0, choose psi_i in V with
||phi_i - psi_i|| < eps/(k max_i||y_i||) and put S = sum_i psi_i (x) y_i, so ||T - S|| < eps. If S = 0 it
attains its norm. Otherwise ||S|| = ||S^*|| = sup{||S^* y^*|| : y^* in B_{Y^*}}. The map y^* -> ||S^* y^*||
is continuous on the compact set B_{Y^*}, so it attains its maximum at some y_0^*, and ||S^* y_0^*|| = ||S||.
Now S^* y_0^* = sum_i y_0^*(y_i) psi_i lies in V, which is contained in NA(X,R), and it is nonzero. Pick
x in S_X with |S^* y_0^*(x)| = ||S||; replacing x by -x we may assume y_0^*(Sx) = ||S||. Then
||Sx|| >= y_0^*(Sx) = ||S||, so S attains its norm at x. QED

### 2.2 Proposition 2.2 (every L_1(mu)) -- PROVED
For every measure space (Omega,Sigma,mu), NA(L_1(mu),R) contains a norm-dense linear subspace of L_1(mu)^*.
Hence NA(L_1(mu),Y) is dense for every finite-dimensional Y. (Uhl [M] gives more: every Y with the RNP.)
Proof. Step 1 (l_1-decomposition). Zorn's lemma gives a maximal family A of measurable sets of finite positive
measure that are pairwise almost disjoint. Let f be in L_1(mu) and S_n = {|f| > 1/n}, so mu(S_n) < infinity.
For each m, at most m*mu(S_n) members A of A satisfy mu(A cap S_n) > 1/m, because the sum of mu(A cap S_n)
over any finite subfamily is at most mu(S_n). Hence A_f = {A in A : mu(A cap {f != 0}) > 0} is countable.
Let B = {f != 0} minus the union of A_f. Then mu(B cap A) = 0 for every A in A. If mu(B) > 0, some B cap S_n
would have finite positive measure and could be added to A, contradicting maximality; so mu(B) = 0. After
disjointifying an enumeration of A_f (which changes each set by a null set) we get f = sum f 1_A in L_1 and
||f|| = sum ||f 1_A||. Thus L_1(mu) is isometric to (sum over A in A of L_1(mu|A)) in the l_1-sense, each
mu|A finite, and L_1(mu)^* is the l_infinity-sum of the spaces L_infinity(mu|A).
Step 2. Let V be the set of families h = (h_A) for which some finite set F of reals satisfies h_A in F
a.e. on A, for every A. V is linear: the values of a sum lie in F_1 + F_2, which is finite. V is dense: if
sup_A ||h_A||_inf = C, then h'_A = eps*floor(h_A/eps) takes values in the finite set eps*Z cap [-C-eps, C]
and ||h - h'|| <= eps. Each h in V, h != 0, attains its norm. Indeed ||h|| = max{|c| : c in F and
mu({h_A = c}) > 0 for some A}, a maximum over a finite set. Pick c_0 and A_0 realizing it, put
E = {h_{A_0} = c_0} (0 < mu(E) < infinity) and x = sign(c_0) 1_E / mu(E); then ||x|| = 1 and
<h,x> = |c_0| = ||h||. Lemma L concludes. QED

### 2.3 Proposition 2.3 (closed subsets of R; explicit form of Godard) -- PROVED
Let M be a nonempty closed subset of R with base point x_0 in M. Let C = conv(M), an interval, and let G be
the family of gaps, i.e. the bounded components (a,b) of C minus M (so a, b lie in M). Let
W = {u in L_1(C) : u is a.e. constant on each gap}. Then:
 (i) every g in Lip_0(M) has a unique extension g~ to C that is affine on each gap; Lip(g~) = Lip(g), and
     Lip(g) = ||g~'||_{L_infinity(C)};
 (ii) the formula <g, Phi(u)> = integral_C g~' u defines an onto linear isometry Phi: W -> F(M);
 (iii) W is isometric to L_1(mu_M), where mu_M = lambda restricted to M plus the sum over gaps G of
       lambda(G) delta_G (each gap collapsed to an atom of mass equal to its length);
 (iv) V_R = {g : g~' is a.e. finitely valued} is a dense linear subspace of Lip_0(M) contained in
      NA(F(M),R). Hence NA(F(M),Y) is dense for every finite-dimensional Y.
(M non-closed: F(M) = F(closure of M). Changing the base point gives an isometric free space.)
Proof. (i) Define g~ by linear interpolation on each gap. Let x < y in C. If x and y lie in the closure of
one gap (a,b), the slope is |g(b)-g(a)|/(b-a) <= L := Lip(g). Otherwise let b_1 be the right endpoint of
x's gap (b_1 = x if x is in M) and a_2 the left endpoint of y's gap (a_2 = y if y is in M). Then
x <= b_1 <= a_2 <= y with b_1, a_2 in M, and
|g~(y)-g~(x)| <= |g~(y)-g~(a_2)| + |g(a_2)-g(b_1)| + |g~(b_1)-g~(x)| <= L(y-a_2) + L(a_2-b_1) + L(b_1-x) = L(y-x).
So Lip(g~) <= Lip(g), and the reverse inequality holds because g~ extends g. On an interval, a Lipschitz
function is absolutely continuous and Lip = ||derivative||_infinity. Uniqueness is clear.
(ii) On W_0 = span{1_[x,y] : x < y in M} put Phi(1_[x,y]) = delta_y - delta_x. Every gap lies either inside
[x,y] or outside it, so W_0 is contained in W. For u in W_0 we have <g, Phi(u)> = integral g~' u, since
integral_x^y g~' = g(y) - g(x). This shows that Phi is well defined (if u = 0 a.e., Phi(u) pairs to 0 with
all of Lip_0(M), hence is 0) and that ||Phi(u)|| <= ||u||_1. Moreover W_0 is dense in W. Simple functions are
dense in W, so it suffices to approximate 1_G for a gap G = (a,b) (which equals 1_[a,b] a.e.) and 1_E for
E contained in M with lambda(E) finite. Given eps, take an open set U containing E with lambda(U minus E) < eps,
and finitely many of its component intervals I_k = (s_k, t_k) with lambda(U minus union I_k) < eps. Drop
those with I_k cap M empty, and let s'_k = inf(M cap [s_k,t_k]), t'_k = sup(M cap [s_k,t_k]); both lie in M.
Since E is contained in M, E cap I_k lies in [s'_k, t'_k]. For u = sum_k 1_[s'_k,t'_k], which is in W_0,
|u - 1_E| <= 1_{(U minus E) union finite set} + 1_{E minus union I_k}, so ||u - 1_E||_1 < 2 eps. So Phi
extends to a contraction W -> F(M) with the same formula. It is isometric: for u in W, h = sign(u) is
constant on gaps; g(x) = integral_{x_0}^x h for x in M satisfies g~ = integral h (affine on gaps),
Lip(g) <= 1 and <g, Phi(u)> = ||u||_1. The range is closed (W is complete) and contains every
delta_x - delta_{x_0}, whose span is dense in F(M); so Phi is onto.
(iii) Send u to (u restricted to M, (value of u on G)_G); then ||u||_1 = integral_M |u| + sum_G |c_G| lambda(G).
(iv) V_R is linear. It is dense: with h = eps*floor(g~'/eps) (constant on gaps, finitely valued because
g~' is bounded), let g_1(x) = integral_{x_0}^x h on M; by (i), Lip(g - g_1) = ||g~' - h||_inf <= eps.
Each g in V_R, g != 0, attains its norm. L = Lip(g) = max{|c| : lambda{g~' = c} > 0}, so pick such c.
Choose x_1 < x_2 in M with lambda(E) > 0 where E = {g~' = c} cap [x_1,x_2]; gaps lie inside or outside
[x_1,x_2], so u = sign(c) 1_E / lambda(E) is in W. Then ||Phi(u)|| = 1 and <g, Phi(u)> = L. Lemma L applies.
QED
Remark (KNOWN, also PROVED by (iv)): NA(F([0,1]),R) strictly contains SNA([0,1],R). Take g~' = 1 on a fat
Cantor set and -1/2 elsewhere: g attains its norm on F([0,1]) but at no molecule, since every interval meets
the complement of the Cantor set in positive measure.

### 2.4 R-trees (Godard) -- KNOWN [S] + PROVED corollary
Godard: if M is a closed subset of an R-tree containing all branching points of the subtree it spans, then
F(M) is isometric to L_1(mu) (length measure on the hull, with gaps collapsed as in 2.3). By Proposition 2.2,
NA(F(M),Y) is dense for every finite-dimensional Y, and NA(F(M),R) contains a dense linear subspace.
CAVEAT (OPEN here): for subsets of R-trees MISSING branching points, F(M) is only isometric to a SUBSPACE of
L_1 (codimension 1 in the simplest examples). Density of NA is not inherited by subspaces. Example: the
legs [1/2,1] of an infinite star with the center removed. With finitely many legs a direct 1D argument (as in
Proposition C) works, but infinitely many legs bring back the "slopes at infinity" issue of Section 3.3.

### 2.5 Proposition 2.5 (wedge sums) -- PROVED
Let (M_i,d_i,0_i), i in I, be pointed metric spaces. The wedge M = wedge of the M_i is their disjoint union
with all base points identified to 0, and d(x,y) = d_i(x,y) on M_i, d(x,y) = d_i(x,0) + d_j(0,y) for x in
M_i, y in M_j, i != j. (This is a metric, complete if every M_i is complete.) Let iota_i: F(M_i) -> F(M) be
the linearization of the pointed isometric inclusion. Then Psi((mu_i)) = sum_i iota_i(mu_i) is an onto
isometry from the l_1-sum of the F(M_i) to F(M).
Proof. (1) R: f -> (f|M_i) maps Lip_0(M) isometrically ONTO the l_infinity-sum of the Lip_0(M_i). Clearly
sup_i Lip(f|M_i) <= Lip(f). Conversely, given (f_i) with sup Lip(f_i) = L, define f = f_i on M_i
(consistent at 0). For x in M_i, y in M_j with i != j,
|f(x)-f(y)| <= |f_i(x)| + |f_j(y)| <= L d_i(x,0) + L d_j(0,y) = L d(x,y).
(2) For finitely many nonzero mu_i: ||Psi((mu_i))|| = sup_{Lip f <= 1} sum_i <f|M_i, mu_i>. By (1) the
restrictions f|M_i range independently over the unit balls, so the supremum is sum_i ||mu_i||. Hence Psi
extends to an isometry. Its range is closed and contains every delta_x, so Psi is onto. QED

### 2.6 Proposition 2.6 (l_1-sums, fixed Y) -- PROVED
Let X be the l_1-sum of Banach spaces X_i, i in I, and Y a Banach space. Then NA(X,Y) is dense iff NA(X_i,Y)
is dense for every i. Combined with 2.5: for every Y, NA(F(wedge of the M_i),Y) is dense iff every
NA(F(M_i),Y) is dense. So the class of M with "NA(F(M),Y) dense for all finite-dimensional Y" is closed
under arbitrary wedge sums.
Proof. Write T_i = T o J_i, where J_i is the inclusion of X_i; then ||T|| = sup_i ||T_i||.
(<=) Let T != 0 and 0 < eps < ||T||/2. Pick i_0 with ||T_{i_0}|| > ||T|| - eps and S_0 in NA(X_{i_0},Y)
with ||S_0 - T_{i_0}|| < eps; then ||T|| - 2eps < ||S_0|| < ||T|| + eps. Put S_0' = (||T||/||S_0||) S_0,
which is norm attaining with ||S_0'|| = ||T|| and ||S_0' - S_0|| <= 2 eps. Let S agree with T on X_i for
i != i_0 and equal S_0' on X_{i_0}. Then ||S|| = ||T||, S attains its norm at J_{i_0} x_0 (where S_0'
attains), and ||S - T|| <= 3 eps.
(=>) Fix i_0 and T_0 != 0 in L(X_{i_0},Y), and let T = T_0 o P_{i_0} (P_{i_0} the coordinate projection).
For eps < ||T_0||/3 take S in NA(X,Y) with ||S - T|| < eps, attaining its norm at x = (x_i) with
sum ||x_i|| = 1. Then ||S J_i|| < eps for i != i_0 and ||S J_{i_0}|| > ||T_0|| - eps > 2 eps, so
||S|| = ||S J_{i_0}||. Also ||S|| = ||Sx|| <= ||S J_{i_0}|| a + eps (1 - a) with a = ||x_{i_0}||. This
forces a = 1, and then ||S J_{i_0} x_{i_0}|| = ||S J_{i_0}||. So S J_{i_0} is norm attaining and
eps-close to T_0. QED

### 2.7 RNP cases -- KNOWN [S] + PROVED deduction
(a) For complete M: F(M) has the RNP iff M is p1u (APGP [S]). Then Bourgain [M] gives property A, so
NA(F(M),Y) is dense for EVERY Y; moreover SNA(M,Y) is dense for every Y (CCGMR [S]).
(b) PROVED (from the KNOWN representation theorems of APS [S]): if every element of F(M) is a convex
integral of molecules -- which holds when F(M) has the RNP (APS 2412.04312) and when M is uniformly
discrete (convex series, APS 2302.13951) -- then NA(F(M),Y) = SNA(M,Y) for EVERY Banach space Y.
Proof. Suppose T_F attains its norm at mu in S_{F(M)}. By Hahn-Banach pick y^* in S_{Y^*} with
y^*(T_F mu) = Lip(F), and let phi = y^* o F. Then Lip(phi) <= Lip(F) = phi(mu) <= Lip(phi), so
phi(mu) = Lip(phi). Write mu = integral m_{xy} dpi(x,y) with pi >= 0 on the set of pairs and
pi(total) = ||mu|| = 1, in the sense that <f,mu> = integral f(m_{xy}) dpi for all f in Lip_0(M). Then
Lip(phi) = integral phi(m_{xy}) dpi <= Lip(phi), with equality only if phi(m_{xy}) = Lip(phi) for pi-a.e.
pair, in particular for some x != y. Hence ||F(x)-F(y)|| >= y^*(F(x)-F(y)) = Lip(F) d(x,y). QED

## 3. Lineability tests (part (c)): does NA(F(M),R) contain a dense linear subspace of Lip_0(M)?

### 3.1 M a subset of R: YES (Proposition 2.3(iv)); R-trees containing branching points: YES (2.4).

### 3.2 Proposition C (C^1 simple curves; the circle T) -- PROVED (new as far as I know)
Let Z be a Banach space, l > 0, and gamma: R -> Z a C^1 map with ||gamma'(t)|| = 1 for all t. Either
(closed case) gamma is l-periodic and injective on [0,l), or (arc case) gamma is injective on [0,l].
Let M = gamma([0,l]) with the metric of Z and base point gamma(0). Then
V_C = {f in Lip_0(M) : (f o gamma)' is a.e. finitely valued on [0,l]} is a norm-dense linear subspace of
Lip_0(M) contained in NA(F(M),R). Hence NA(F(M),Y) is dense for every finite-dimensional Y.
This applies to the Euclidean unit circle T (gamma(t) = (cos t, sin t), l = 2 pi).
Notation: dd(s,t) = |s-t| (arc case), dd(s,t) = min_k |s-t-kl| (closed case).
Step 0 (geometry). (a) ||gamma(s)-gamma(t)|| <= dd(s,t): gamma is 1-Lipschitz, and in the closed case we use
periodicity to pick representatives. (b) Let w(delta) = sup{||gamma'(r)-gamma'(r')|| : |r-r'| <= delta};
w(delta) -> 0 by uniform continuity. Writing gamma(t)-gamma(s) = (t-s)gamma'(s) + integral_s^t
(gamma'(r)-gamma'(s)) dr gives ||gamma(t)-gamma(s)|| >= |t-s|(1 - w(|t-s|)). (c) (chord-arc) There is
c in (0,1] with ||gamma(t)-gamma(s)|| >= c dd(s,t). Proof: pick delta_0 with w(delta_0) <= 1/2. For
dd <= delta_0, (b) gives the bound with c = 1/2. On the compact set {dd(s,t) >= delta_0} (in [0,l]^2 or the
torus) injectivity gives a positive minimum m_0 of ||gamma(t)-gamma(s)||, and dd <= l; take
c = min(1/2, m_0/l). For T: c = 2/pi, because 2 sin(a/2) >= 2a/pi on [0,pi].
Step 1. For f in Lip_0(M), g = f o gamma is Lipschitz with |g'| <= Lip(f) a.e. (by (a)), l-periodic in the
closed case, and g(t) - g(s) = integral_s^t g'.
Step 2. V_C is a linear subspace (finitely valued functions form a vector space).
Step 3 (V_C lies in NA). Let f in V_C, L = Lip(f) > 0, and D(s,t) = (g(t)-g(s))/||gamma(t)-gamma(s)||.
Since D(t,s) = -D(s,t), L = sup D.
 Case A: the supremum is attained at a pair. Then f is in SNA(M,R), which is contained in NA.
 Case B: it is not attained. Take (s_n,t_n) with D -> L and, by compactness, (s_n,t_n) -> (s*,t*). If
 dd(s*,t*) > 0, D is continuous at (s*,t*) (denominator >= c dd > 0) and D(s*,t*) = L, contradiction. So
 dd(s_n,t_n) -> 0. With representatives |t_n - s_n| = dd(s_n,t_n), Steps 0(b) and 1 give
 D(s_n,t_n) <= ||g'||_inf / (1 - w(|t_n-s_n|)), which tends to ||g'||_inf. Hence L <= ||g'||_inf <= L.
 Because g' is finitely valued, some value c_0 with |c_0| = L is taken on a set E in [0,l) with
 lambda(E) > 0. Let gamma^: F([0,l]) -> F(M) be the linearization of the pointed 1-Lipschitz map
 gamma|[0,l]; then ||gamma^|| <= 1 and <k, gamma^(nu)> = <k o gamma, nu>. Use F([0,l]) = L_1[0,l]
 (Proposition 2.3 with no gaps; <h,u> = integral h'u), and put mu = gamma^(sign(c_0) 1_E / lambda(E)).
 Then ||mu|| <= 1 and f(mu) = integral_E g' sign(c_0)/lambda(E) = L. So f attains its norm at mu.
Step 4 (density). Given f and eps, let g = f o gamma and h = eps*floor(g'/eps) (finitely valued,
||g' - h|| <= eps). In the closed case integral_0^l g' = 0, so kappa = (1/l) integral_0^l h has
|kappa| <= eps; put h_1 = h - kappa (mean zero, ||g' - h_1|| <= 2eps), extended l-periodically. In the arc
case h_1 = h. Let G(t) = integral_0^t h_1 (l-periodic in the closed case) and f_1(gamma(t)) = G(t), which is
well defined by injectivity. For any s,t, integrate over the shorter arc (allowed since the mean is 0):
|G(t)-G(s)| <= ||h_1|| dd(s,t) <= (||h_1||/c) ||gamma(t)-gamma(s)||. So f_1 is in V_C, and
|(g-G)(t) - (g-G)(s)| <= 2 eps dd(s,t) <= (2eps/c) ||gamma(t)-gamma(s)||, i.e. Lip(f - f_1) <= 2eps/c.
Step 5. Lemma L. QED
COROLLARY C1 (PROVED from Proposition C + KNOWN [S]). F(T) fails property A (JMR 2023, Ex. 5.2), and
SNA(T,Y) is dense for no Y (CGMR 2021). Nevertheless NA(F(T),Y) is dense for every finite-dimensional Y, and
NA(F(T),R) is densely lineable. So the range witnessing the failure of property A for F(T) must be
infinite-dimensional. F(T) fails the RNP (it contains F(arc), which is isomorphic to L_1).
REMARK (OPEN): curves with corners (e.g. the boundary of a square in l_2^2). Step 3 fails there: chord slopes
across a corner can approach a supremum larger than ||g'||_inf without attaining it when g' switches values
infinitely often near the corner. Same for infinitely many legs in 2.4.

### 3.3 Uniformly discrete M
PROPOSITION U1 -- PROVED. Let M be bounded and uniformly discrete (theta = inf of distances > 0), with
well-ordered distance set D(M) = {d(x,y) : x != y} (every nonempty subset has a minimum; e.g. D(M) finite).
Then the finitely valued functions form a dense linear subspace of Lip_0(M) contained in SNA(M,R), which is
contained in NA(F(M),R).
Proof. Attainment: let f have finite value set F. For a > b in F, the set of distances d(x,y) with f(x) = a,
f(y) = b is a subset of D(M), so it has a minimum delta_ab, realized by a pair. Hence
Lip(f) = max over a > b in F of (a-b)/delta_ab, a maximum over a finite set, attained at a pair. Density:
f is bounded (|f(x)| <= Lip(f) diam M); f_eps = eps*floor(f/eps) is finitely valued with f_eps(0) = 0, and
|(f-f_eps)(x) - (f-f_eps)(y)| < eps <= (eps/theta) d(x,y). QED
(For such M, density of NA was already known via the RNP; the point is the linear structure.)
EXAMPLE U2 -- PROVED. M = {0} union {x_n} union {y_n} with d(x_n,y_m) = 1 + 1/(n+m), all other distances
between distinct points equal to 2. This is a metric: all distances lie in [1,2]. Let f = 1 on {x_n} and 0
elsewhere. Then Lip(f) = sup 1/(1+1/(n+m)) = 1 is not attained at any pair. Since every element of F(M) is a
convex series of molecules (APS [S]), Proposition 2.7(b) gives NA(F(M),R) = SNA(M,R), so f is not in
NA(F(M),R). Thus finitely valued functions do NOT lie in NA here. Whether SOME dense linear subspace does:
OPEN. Elements of such a subspace near f need "tilts" of order 1/(n+m) that beat the distance excess at
finite pairs, coherently along every 2-dimensional section. I could neither build such a family (natural
linear tilt operators fail: a near-identity tilt operator is onto, so its image contains non-attaining
elements) nor rule it out. HEURISTIC: an obstruction, if any, would come from the planar cluster-set /
convex-hull analysis of pairs of elements, in the spirit of Rmoutil's argument.
For ALL uniformly discrete M, density of NA(F(M),Y) for every Y is KNOWN (Kalton RNP + Bourgain).

### 3.4 M = R^2 (Euclidean)
LEMMA R1 -- PROVED. Let d >= 1 and R^d be Euclidean. For u in L_1(R^d;R^d), the functional
Lambda_u(g) = integral grad g . u lies in F(R^d), with ||Lambda_u|| <= ||u||_1. Consequently:
 * if f in Lip_0(R^d) satisfies |grad f| = Lip(f) on a set of positive measure, then f is in NA(F(R^d),R);
 * if G in Lip_0(R^d,Y) and y^* in S_{Y^*} satisfy Lip(y^* o G) = Lip(G) and |grad(y^* o G)| = Lip(G) on a set
   of positive measure, then T_G is in NA(F(R^d),Y).
Proof. Rademacher gives |grad g| <= Lip(g) a.e., so |Lambda_u(g)| <= Lip(g) ||u||_1. By Banach-Dieudonne /
Krein-Smulian, it suffices that Lambda_u is weak*-continuous on bounded sets. On bounded subsets of Lip_0 the
weak* topology is the topology of pointwise convergence (KNOWN, standard [M]). Let g_a -> g pointwise with
Lip(g_a) <= C. Equicontinuity makes the convergence uniform on compact sets. For v in C_c^infinity,
integral grad g_a . v = -integral g_a div v -> -integral g div v = integral grad g . v. For general u pick v
with ||u - v||_1 < eta; then the error is at most 2 C eta. For the attainment claims, take S in
{|grad f| = L} bounded with 0 < lambda(S) < infinity and u = 1_S grad f / (L lambda(S)): ||u||_1 = 1 and
Lambda_u(f) = L. The vector case follows from phi = y^* o G: ||T_G Lambda_u|| >= phi(Lambda_u) = Lip(G). QED
Hence V_fin = {f in Lip_0(R^2) : grad f is a.e. finitely valued} is a linear subspace contained in
NA(F(R^2),R). Is V_fin dense? Since Lip(f - g) = ||grad f - grad g||_inf on R^d, this is exactly the question:
can every gradient field be approximated in L_infinity by finitely valued gradient fields? It is a
differential inclusion grad g(x) in K cap B(grad f(x), eps) with a MEASURABLE target. Status: OPEN.
Test cases:
 (i) laminates f = h(<x,v>): round h'. PROVED (trivial).
 (ii) grad f bounded and uniformly continuous: SKETCH, YES. Take the piecewise affine interpolant on a fine
     regular triangulation (error <= C w(delta)). On each triangle tau with gradient a_tau, add w_tau in
     W_0^{1,inf}(tau) with a_tau + grad w_tau in K cap B(a_tau, eps/2), where K is an eps/8-net. This uses
     the scalar pyramid construction: for xi in int conv{a_1..a_N},
     u(x) = xi.x + 1 + min_i (a_i - xi).x on P' = {max_i (xi - a_i).x <= 1} has grad u in {a_i} and
     u = xi.x on the boundary of P'. Then a Vitali covering of tau by scaled copies of P' finishes.
 (iii) radially wild f = h(|x|) with h' = 1 on a fat Cantor set E and -1 on its complement: SKETCH, YES.
     On the fat set {|x| in E} put g = N(x) + c(|x|), where N(x) = max_j <x,e_j> is a fine polygonal gauge and
     c(r) = -2 lambda([r_0,r] minus E). The approximate gradient there is e_j (in K) because c' = 0 a.e. on E.
     On each gap annulus, intersected with each angular sector, solve the scalar inclusion with target near
     -e_j and boundary datum N(x) + c(a_i) - 2(|x| - a_i), whose gradient lies in the interior of the
     convex hull of the target (pyramids + Vitali, as in (ii)). The pieces glue continuously, the result is
     Lipschitz, grad g is finitely valued, and ||grad g - grad f||_inf <= eps.
 General f: OPEN. Standard convex-integration existence theorems need targets that are constant or
 continuous in x [M]; here the target is only measurable.
Consequently NA(F(R^2),l_2^2) density is OPEN (not addressed in the literature I found). None of the standard
tools applies: F(R^2) contains L_1 (so no RNP); it has the Daugavet property [M], hence no strongly exposed
points, so property alpha / quasi-alpha fail; it is not isometric to a subspace of L_1 (Godard [S]); its dual
is not an L_1-space; and SNA(R^2,Y) is not dense (Proposition N below). The LINEAR problem for X = l_2^2 is
trivial, so F(R^2) isolates a purely "nonlinear" difficulty.
DIRECT CONSTRUCTIONS (HEURISTIC, failed). Boosting the slope along a line forces a boost on a neighborhood
(by Lipschitz extension), which collides with maximal-slope points of the wild gradient nearby. A radial
damping G = F - delta chi (F - F(x_0)) with chi = |x - x_0|/R keeps Lip(G) <= Lip(F) and is delta-close to F
(PROVED: ||DG|| <= (1 - delta chi) L + delta |F - F(x_0)| |grad chi| <= L), but by itself it creates no exact
attainment.

### 3.5 General M: OPEN
NA(F(M),R) always contains SNA(M,R), which contains a copy of c_0 for infinite M (Aviles et al. [S]), so it is
always lineable. Dense lineability is known only in the cases above. The lineability criterion is only
sufficient. RNP spaces (e.g. Example U2) show density without (known) dense lineability.

## 4. Transfer F(X) -> X and universality (part (d))

Setting: X a separable Banach space with base point 0. beta: F(X) -> X is the barycentre (linearization of
id_X), ||beta|| = 1. iota: X -> F(X) is the Godefroy-Kalton isometric linear lifting with beta iota = id_X
(KNOWN [M]), so P = iota beta is a norm-one projection and X is isometric to a 1-complemented subspace of F(X).
Facts (PROVED, elementary):
 (F1) For linear T, the linearization of T (as a Lipschitz map) is T beta.
 (F2) If A in NA(X,Y) attains its norm at u, then A beta attains its norm at the molecule m_{u,0}. So
      NA(X,Y) dense implies that every T beta is a limit of NA(F(X),Y). The converse is the transfer question.
 (F3) For G in Lip_0(X,Y): ||T_G iota - T|| <= Lip(G - T), since T_G - T_T = T_{G-T},
      T_T iota = T beta iota = T, and ||iota|| = 1. The "averaged derivative" T_G iota is close to T but has
      no reason to attain its norm (it averages derivatives; HEURISTIC).

### 4.1 Proposition N -- PROVED (Y = R: KMS 2016 [S]; general Y probably known, not confirmed)
For every Banach space X != 0 and Y != 0, SNA(X,Y) is NOT dense in Lip_0(X,Y). Hence the hypothesis
"SNA(X,Y) dense" of any implication "SNA(X,Y) dense => NA(X,Y) dense" is never satisfied for Banach domains.
Proof. Let E be a measurable subset of R with 0 < lambda(E cap I) < lambda(I) for every nondegenerate interval
I (classical [M]: inductively place disjoint nowhere dense fat Cantor sets inside every rational interval).
Let h(t) = integral_0^t (1_E - 1_{R minus E}), so Lip(h) = 1 and h' takes both values +-1 on positive-measure
subsets of every interval. Fix x^* in S_{X^*} and y_0 in S_Y, and let F(x) = h(x^*(x)) y_0. Then Lip(F) = 1:
the bound <= 1 is clear; for >=, take x_0 in S_X with x^*(x_0) > 1 - delta and a density point s of E with
h'(s) = 1 to get slopes > (1-delta)^2. Suppose G is in SNA with Lip(G - F) < 1/4, attaining at (a,b). Then
Lip(G) >= 3/4. Pick y^* in S_{Y^*} with y^*(G(a)-G(b)) = Lip(G)||a-b||, and let u = (a-b)/||a-b||,
s_0 = ||a-b||. For 0 <= s < s' <= s_0 we get y^*(G(b+s'u) - G(b+su)) = Lip(G)(s'-s): the inequality <= is
the Lipschitz bound, and >= follows by subtracting the bounds on [0,s] and [s',s_0] from the total. Hence
y^*(F(b+s'u) - F(b+su)) >= (3/4 - 1/4)(s'-s), i.e.
y^*(y_0) [h(x^*(b) + s' x^*(u)) - h(x^*(b) + s x^*(u))] >= (s'-s)/2.
Since |h(p) - h(q)| <= |p-q|, we get |y^*(y_0)| |x^*(u)| >= 1/2. So k(r) = y^*(y_0) h(x^*(b) + r) is strictly
monotone on the nondegenerate interval between 0 and s_0 x^*(u), with derivative of one fixed sign and
modulus >= 1/2 a.e. But k' = +-y^*(y_0) takes BOTH signs on positive-measure subsets of that interval.
Contradiction; so the Lip-distance from F to SNA(X,Y) is >= 1/4. QED

### 4.2 Directional attainment
DEFINITION. G in Lip_0(X,Y) is directionally norm attaining (G in DNA(X,Y)) if there are u in S_X,
y^* in S_{Y^*}, z_k in X and h_k > 0 with y^*(G(z_k + h_k u) - G(z_k))/h_k -> Lip(G).
REMARKS (PROVED).
 (R1) SNA is contained in DNA: take z_k = b and h_k = ||a-b|| constant.
 (R2) Y finite-dimensional: if pairs (x_k,w_k) have slopes ||G(x_k)-G(w_k)||/||x_k-w_k|| -> L = Lip(G) and
      directions (x_k-w_k)/||x_k-w_k|| -> u in norm (the KMS-type directional notion), then G is in DNA.
      Take norming y^*_k, pass to y^*_k -> y^* (compactness), and put z_k = w_k, h_k = ||x_k-w_k||. Then
      y^*(G(w_k+h_k u) - G(w_k)) >= y^*_k(G(x_k)-G(w_k)) - ||y^*_k - y^*|| L h_k
      - L h_k ||u - (x_k-w_k)/h_k|| = h_k (L - o(1)).
 (R3) If T_G attains its norm at an element of F(sigma), where sigma = {z+su : s in [0,a]} is a segment (an
      isometric copy of [0,a], so F(sigma) = L_1[0,a] is isometrically a subspace of F(X)), then G is in DNA.
      With phi = y^* o G norming, the attaining element is k in L_1 with ||k|| = 1 and
      integral (phi(z+su))' k(s) ds = L, which forces (phi(z+su))' = L sign k(s) a.e. on {k != 0}. At such
      an interior point s_0, the directional slope in direction +-u tends to L.
 (R4) The same holds for elements of F(gamma(I)) with gamma a C^1 curve: at a point where (phi o gamma)' = L,
      the direction gamma'(s_0) works, because gamma(s_0+h) = gamma(s_0) + h gamma'(s_0) + o(h).

### 4.3 Lemma DT (directional transfer) -- PROVED
Let X be separable, Y finite-dimensional, T in L(X,Y), eps >= 0, and G in DNA(X,Y) with Lip(G - T) <= eps and
L = Lip(G) > 0. Then there is A in NA(X,Y) with ||A|| = L and ||A - T|| <= eps.
Proof. Let u, y^*, z_k, h_k be as in the definition, with
y^*(G(z_k + h_k u) - G(z_k)) >= (L - eta_k) h_k, eta_k -> 0.
Step 0 (KNOWN differentiability). Y has the RNP and X is separable, so G is Gateaux differentiable outside a
Borel set N' that is null for every nondegenerate Gaussian measure on X (Aronszajn 1976, Phelps 1978;
Benyamini-Lindenstrauss Ch. 6 [M]). Fix a centered nondegenerate Gaussian measure g on X: the law of
sum_j 2^{-j} xi_j x_j with (x_j) dense in B_X and xi_j i.i.d. N(0,1). Its support is X, so g(B(0,1)) > 0.
Translates and dilates of g are again nondegenerate Gaussian measures.
Step 1 (good parallel segment). Let sigma_k = eta_k + 1/k and t_k = sigma_k h_k. For each fixed s, the law of
z_k + t_k w + s u (w distributed as g) is a nondegenerate Gaussian, so it gives N' measure 0. By Fubini on
g x Lebesgue([0,h_k]), for g-a.e. w the set {s : z_k + t_k w + s u in N'} is Lebesgue-null. Pick such w_k
with ||w_k|| < 1, and put v_k = t_k w_k, so ||v_k|| <= sigma_k h_k.
Step 2 (integrate). s -> G(z_k + v_k + su) is Lipschitz into finite-dimensional Y, hence absolutely continuous,
and for a.e. s its derivative is DG(p_s)u with p_s = z_k + v_k + su outside N'. Therefore
integral_0^{h_k} y^*(DG(p_s)u) ds = y^*(G(z_k+v_k+h_k u) - G(z_k+v_k))
>= (L - eta_k) h_k - 2 L ||v_k|| >= (L - eta_k - 2 L sigma_k) h_k.
So some s_k with p_k := p_{s_k} outside N' has y^*(DG(p_k)u) >= L - eta_k - 2 L sigma_k.
Step 3. At every Gateaux point p: ||DG(p)|| <= L, and since G - T has Gateaux derivative DG(p) - T at p and
Lip(G - T) <= eps, ||DG(p) - T|| <= eps.
Step 4 (limit). A_k = DG(p_k) satisfies ||A_k|| <= L. By a diagonal argument over a countable dense D in X
(bounded sets in finite-dimensional Y are relatively compact), A_{k_j} x converges for x in D, hence for all x
by equicontinuity. Ax = lim A_{k_j} x is linear, with ||A|| <= L and ||A - T|| <= eps, and
y^*(Au) = lim y^*(A_{k_j} u) >= L. Hence L <= y^*(Au) <= ||Au|| <= ||A|| <= L, so A attains its norm at u
and ||A|| = L. QED
Remark: the same proof works for reflexive Y: use WOT-compactness of bounded subsets of L(X,Y) and
WOT-lower semicontinuity of the norm.

### 4.4 Corollaries -- PROVED
DT1. Let X be separable, Y finite-dimensional and T in L(X,Y). The following are equivalent:
(a) T is in the closure of NA(X,Y); (b) T is in the Lip-closure of SNA(X,Y); (c) T is in the Lip-closure of
DNA(X,Y). [(a)=>(b): linear NA operators are in SNA. (b)=>(c): R1. (c)=>(a): Lemma DT.] In particular,
NA(X,Y) is dense iff every linear operator is a Lip-limit of strongly norm attaining Lipschitz maps. This is
the meaningful form of "SNA dense => NA dense" (cf. Proposition N). It is probably known in some form (cf.
Godefroy 2016, Choi-Choi-Martin 2020); not confirmed (full texts unreachable).
DT2. (F(X) as a counterexample candidate.) If NA(X,Y) is not dense, pick T outside its closure. Then T beta
(that is, T viewed as a Lipschitz map) is at positive Lip-distance from DNA(X,Y). So any approximants of
T beta from NA(F(X),Y) must attain their norm only at elements of F(X) that carry no norm direction: never at
molecules, never on F(segments), never on F(C^1 curves) (R1-R4).

### 4.5 What blocks the full transfer -- OPEN
(Q-dir) For X separable and Y finite-dimensional: does T_G in NA(F(X),Y) imply G in DNA(X,Y)?
A positive answer to (Q-dir), even only for G Lip-close to linear maps, gives the full transfer by Lemma DT, and
then the universality statement: "NA(F(X),Y) dense for all separable X" is equivalent to the Johnson-Wolfe
question restricted to separable domains.
SKETCH (de Leeuw formulation): if every mu in F(X) has an optimal de Leeuw representation (Aliaga-Pernecka-
Smith) charging the Borel set of points of the compactified pair space whose direction converges in norm
(a G_delta, since S_X is Polish), then (Q-dir) holds. The norming function phi equals Lip a.e. for the
representing measure; a charged norm-direction point gives pairs with slopes -> Lip and directions -> u,
then apply R2. Not written in detail (the APS framework is not verified here).
Evidence:
 (+) SKETCH: McShane-type extensions are in DNA. For phi_-(x) = inf_s [phi(s) + ||x - s||] at x off the set
     with an attained infimum at s^*, moving toward s^* along the finitely many maximal coordinates (in c_0),
     or along a norming direction of x - s^*, gives slope exactly 1.
 (-) Example Gamma -- PROVED. gamma(t) = (t, (2^{-n} sin(2^n t))_{n>=2}) is an ISOMETRIC embedding of R into
     c_0, and it is norm-differentiable NOWHERE. Isometry: ||gamma(t)-gamma(s)|| =
     max(|t-s|, sup_n 2^{-n}|sin 2^n t - sin 2^n s|) = |t-s|. Nowhere differentiable: a norm derivative would
     be the coordinatewise limit (1, cos(2^n t))_n, but if |cos 2^n t| < 1/2 then cos 2^{n+1} t <= -1/2, so the
     coordinates do not tend to 0 and the limit is not in c_0. Hence F(gamma(R)) is an isometric copy of
     L_1(R) inside F(c_0), made of "integrals of derivations along gamma" whose directions gamma'(t) lie in
     l_infinity minus c_0. The norm-one elements gamma^(1_E)/lambda(E) are attained exactly by the 1-Lipschitz
     phi with (phi o gamma)' = 1 a.e. on E. Example: phi = e_1^*, which IS in DNA (direction e_1). Whether
     some non-DNA phi attains there is OPEN. So (Q-dir) cannot be proved by reading directions off
     representations; one would need to show that attaining functionals can always be "redirected", which
     McShane-type arguments do for scalar functions but not near a prescribed linear map.
Other routes tried (HEURISTIC, failed): the G-K averaged derivative (F3) does not attain; rank-one corrections
need exact information that weak attainment does not provide. A quantitative (BPB-type) version cannot be
universal: Aron-Choi-Kim-Lee-Martin (Trans. AMS 2015) show that BPB-type versions of property B are strictly
stronger than property B, and [M] there is X such that (X,Y) fails the BPBp for every strictly convex Y of
dimension >= 2 (not confirmed by search).

### 4.6 Status of (d)
 * PROVED: directional transfer (Lemma DT, Corollaries DT1/DT2). "SNA(X,Y) dense => NA dense" holds in the
   meaningful local form DT1; global density of SNA never holds for Banach X (Proposition N).
 * OPEN: the full transfer NA(F(X),Y) dense => NA(X,Y) dense, hence also whether the Lipschitz-free class is
   universal for the Johnson-Wolfe question. Missing ingredient: (Q-dir). Obstruction: Example Gamma.
 * Also OPEN: a full positive theorem for the class. It would require settling M = R^2 (Section 3.4),
   where the linear problem is trivial.

## 5. F(X) with X = a Martin renorming of c_0 (part (e))

Let XX = (c_0, p) be Martin's space (Preprint B, Section subsec:space; JFA 2025, arXiv 2406.07273). Facts used
(from Preprint B / BRIEFING; not re-verified here): XX is smooth (M7) and p** is strictly convex, so XX is
strictly convex; NA(XX,R) cap E is contained in two lines for every 2-dimensional E in XX^*; density of
NA(XX,l_2^2) is OPEN.

5.1 Structure of F(XX) (PROVED unless marked). XX is separable, so XX is isometric to a 1-complemented subspace
of F(XX) (Godefroy-Kalton [M]). F(XX) contains F(segment) = L_1 isometrically, so it fails the RNP. It has the
Daugavet property [M: free spaces of length spaces], so its unit ball has no strongly exposed points.
NA(F(XX),R) contains SNA(XX,R), which contains a copy of c_0 (Aviles et al. [S]). So, in contrast with
NA(XX,R) (algebraically thin), the norm-attaining functionals on F(XX) are lineable. SNA(XX,Y) is not dense
for any Y != 0 (Proposition N).

5.2 NA cones at molecules -- PROVED. Let x != y in XX, u = (x-y)/||x-y||, m = m_{xy}, and
C_m = {f in Lip_0(XX) : f(m) = Lip(f)}.
 (i) f is in C_m iff f(y+su) = f(y) + s Lip(f) for 0 <= s <= ||x-y||. (Lipschitz bound on [0,s] and on
     [s,||x-y||], with equality of the total.)
 (ii) C_m cap XX^* is the ray R_+ J(u), where J(u) is the unique norming functional of u (XX is smooth). For
      linear x^*, x^*(m) = x^*(u) = ||x^*|| iff x^* = ||x^*|| J(u).
 (iii) If f is in C_m and is Gateaux differentiable at z in the open segment, then Df(z) = Lip(f) J(u):
       Df(z)(u) = Lip(f) by (i), ||Df(z)|| <= Lip(f), and smoothness.
 (iv) If G in Lip_0(XX,Y) attains its norm at m with norming y^*, then y^* o DG(z) = Lip(G) J(u) at every
      Gateaux point z of the open segment.
So the molecule cones, read through derivatives, reproduce EXACTLY the rays of NA(XX,R). The "two lines"
phenomenon of Preprint B constrains derivative pairs (Dg_1(z), Dg_2(z)) of maps into l_2^2 exactly as it
constrains linear operators. Lemma DT turns any directional attainment into a linear norm-attaining operator
next to T. Thus molecules, segments and C^1 curves give NOTHING beyond the linear theory of XX.

5.3 Where F(XX) could differ from XX. Only through attainment at elements without norm directions (Section
4.5). Such elements exist structurally: XX fails the RNP, and the curve gamma of Example Gamma is bi-Lipschitz
into XX (the identity c_0 -> XX is an isomorphism) and nowhere differentiable. Since XX is strictly convex,
its metric segments are straight, so gamma is not geodesic in XX. Whether elements gamma^(1_E) can be norming
for Lipschitz maps near a linear T is OPEN (it requires "infinitesimally geodesic" behaviour of gamma on E).

5.4 Verdict for (e).
 * PROVED (DT2): if NA(XX,l_2^2) is not dense, then no linear T outside its closure is a Lip-limit of
   directionally (in particular strongly) norm attaining maps XX -> l_2^2. F(XX) is therefore a counterexample
   candidate AT LEAST as strong as XX, in this directional sense.
 * PROVED (Corollary DT3 below): any density proof for F(XX) that uses directionally attaining approximants
   (for instance a dense linear subspace of DNA functionals in Lip_0(XX)) would also prove density of
   NA(XX,Y) for all finite-dimensional Y, i.e. solve Martin's problem positively.
 * No mechanism of failure is visible. Elements without norm directions could only RESCUE density, never
   destroy it. So F(XX) is not a better candidate than XX itself, and a negative answer for F(XX) would refute
   property B of l_2^2 in any case.
COROLLARY DT3 -- PROVED. Let X be separable. If Lip_0(X) contains a norm-dense linear subspace V contained in
DNA(X,R), then NA(X,Y) is dense for every finite-dimensional Y.
Proof. Let T in L(X,Y) and eps > 0. Approximate the coordinate functionals of T (as in Lemma L) by psi_i in V;
the Lipschitz map S = sum psi_i y_i has Lip(S - T) < eps. The function y^* -> Lip(y^* o S) is continuous on
the compact B_{Y^*}, and Lip(S) = max over y^* of Lip(y^* o S). Choose y_0^* realizing the maximum (norm 1
if S != 0). Then phi = y_0^* o S = sum y_0^*(y_i) psi_i is in V, hence in DNA, with Lip(phi) = Lip(S). So S is
in DNA(X,Y) (same u, z_k, h_k, with y^* = y_0^*). Lemma DT gives A in NA(X,Y) with ||A - T|| <= eps. QED

## 6. Open questions and status table

OPEN QUESTIONS
 OQ1. Is NA(F(M),Y) dense for every complete pointed M and every finite-dimensional Y? (A negative answer
      refutes property B of Y; a positive answer follows from a positive Johnson-Wolfe answer.)
 OQ2. M = R^2 Euclidean, Y = l_2^2. Sub-question: is V_fin (finitely valued gradients) dense in Lip_0(R^2),
      i.e. can every Lipschitz gradient field be approximated in L_infinity by finitely valued gradient fields?
      Test cases (laminated, C^1, radially wild) all work (SKETCH for the last two).
 OQ3. (Q-dir) / full transfer: for separable X, does T_G in NA(F(X),Y) force G in DNA? Even only for G close to
      linear maps? Obstruction to naive proofs: Example Gamma (F(c_0) contains an isometric L_1 made of
      direction-free derivations).
 OQ4. Dense lineability of NA(F(M),R) for general uniformly discrete M (Example U2), for curves with corners,
      and for subsets of R-trees missing branching points.
 OQ5. Is density of NA(.,Y) for all finite-dimensional Y inherited by 1-complemented subspaces, or by
      F(N) for N a 1-Lipschitz retract of M?

STATUS TABLE
 Lemma L (lineability criterion) ........................................... PROVED
 Prop 2.2 (every L_1(mu): dense lineability) ............................... PROVED
 Prop 2.3 (M subset of R: F(M) = L_1(mu_M) explicitly; dense lineability) .. PROVED (explicit form of Godard)
 2.4 R-trees with branching points .......................................... KNOWN [S] + PROVED corollary
 Prop 2.5 (wedge sum -> l_1-sum, isometric) ................................ PROVED
 Prop 2.6 (l_1-sums: NA density iff for each summand) ....................... PROVED
 2.7(a) RNP iff p1u, property A, SNA dense ................................. KNOWN [S]
 2.7(b) NA(F(M),Y) = SNA(M,Y) when elements are convex integrals of molecules . PROVED given KNOWN APS theorem
 Prop C (C^1 simple curves, circle T: dense lineability) .................... PROVED
 Cor C1 (F(T) fails property A but NA(F(T),Y) dense for finite-dim Y) ....... PROVED + KNOWN [S]
 Prop U1 (bounded unif. discrete, well-ordered distances) ................... PROVED
 Example U2 (finitely valued functions not NA) .............................. PROVED; dense lineability OPEN
 Lemma R1 (|grad f| = Lip on positive measure => NA on F(R^d)) .............. PROVED
 V_fin dense in Lip_0(R^2) ................................................. OPEN (SKETCH in test cases)
 NA(F(R^2),l_2^2) dense ..................................................... OPEN
 Prop N (SNA(X,Y) never dense for Banach X != 0) ............................ PROVED (Y = R: KNOWN [S])
 Lemma DT (directional transfer), Cor DT1, DT2, DT3 .......................... PROVED
 Full transfer / universality ............................................... OPEN
 de Leeuw route to (Q-dir) .................................................. SKETCH (conditional)
 Example Gamma (isometric nowhere-differentiable R in c_0) ................... PROVED
 5.2 NA cones at molecules of XX ............................................. PROVED
 F(XX) as a counterexample candidate ....................................... as strong as XX (DT2); no evidence of failure
 Overall question .......................................................... OPEN
