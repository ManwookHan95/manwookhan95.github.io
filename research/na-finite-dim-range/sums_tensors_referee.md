# sums_tensors -- ADVERSARIAL REFEREE REPORT

Key: sums_tensors. Referee pass of 2026-10-30. Real scalars. Object of the report: the explorer's notes
`sums_tensors_notes.md` (sections 0-11) and its structured result (verdict EQUIVALENT_TO_JOHNSON_WOLFE).
Labels as in the task: PROVED (full proof here or full proof in the notes re-derived here), KNOWN (with
reference; "confirmed" = search hit with URL; "FROM MEMORY" otherwise), SKETCH, HEURISTIC, OPEN, FALSE.
Notation as in the notes: P(X) means NA(X,F) dense in L(X,F) for every finite-dimensional F; AA(X,Y) is
the set of S with S*y* in NA(X,R) for every y* in Y*.

Network: only WebSearch worked. arXiv full texts are blocked in this session. The single other host I
tried (ojs.utlib.ee, to read Kirme 2026 on absolute sums) failed with a DNS error, so no further hosts
were tried; ojs.utlib.ee would have to be allowed in the session's network settings to read it.

## 0. Referee summary

0.1 Verdict. corrected_verdict = EQUIVALENT_TO_JOHNSON_WOLFE (I agree with the explorer). The verdict is
neither overclaimed nor underclaimed: the notes claim no counterexample and no "always dense" theorem;
they prove that for the listed classes "NA(W,Y) dense for all W in the class" is equivalent to "Y has
property B", which is exactly the open Johnson-Wolfe (JW) question for Y. Remark: for the classes of ALL
sums or ALL tensor products this equivalence is trivial (X = X (+)_a {0} = X (x)_pi R); the content of
Theorem 4 lies in the non-degenerate classes (diagonal sums X (+)_a X, fixed n >= 2 in l_1^n / l_oo^n,
fixed infinite E, fixed atomless mu, dim >= 2 factors). The notes do state the diagonal and dim >= 2
versions, so this is a presentational point, not an error.

0.2 Proofs. I re-derived every item labelled PROVED, line by line (Section 1 below): Lemmas 1.1, 1.2,
1.3, 1.4, Theorem 1 (T1), Lemma 3.1 and Theorem 2 (T2), Theorem 4, Propositions 5, 6, 7(a)-(d), 8(i)-(iii),
9, Theorem 10 (called "T3" in the verdict text), Propositions 11, 13, 14, 15, the l_4^2 check, and the two
FALSE items (P7(e), F-bil). All are CORRECT. I found no hidden hypothesis, no wrong isometry, no
quantifier or sign error. The degenerate cases are handled: x_1 = 0 is excluded by Step 1 of T2;
r = 0 and beta = 0 are harmless in Prop 6; infinite and uncountable index sets are fine (countable
supports in l_1-sums; ideal property for lattice sums); nothing uses separability (T10 uses a lifting
exactly to avoid it). Four facts used FROM MEMORY by the explorer are now confirmed by search (Singer's
representation of C(K,X)*; scattered K iff all Radon measures are atomic; L_1(mu,X)* = L_oo(mu,X*) iff
X* has RNP for sigma-finite mu; Maharam's lifting theorem). Prop 12(b) is correctly labelled SKETCH; its
steps are standard and I found no gap (1.12).

0.3 Literature. Most references exist and say what is claimed (Section 2). Errors or unsupported claims:
 (L1) MISSTATED: "C_0(L) fails property A for infinite L" -- the sources found say "C(K) for infinite
      METRIZABLE K" / "C_0(L) for infinite metrizable L". Consequently the claim "l_oo = C(beta N) fails A"
      (notes 5.5 and the field different_notions_that_fail) is UNSUPPORTED: beta N is not metrizable, and I
      found no source; the statement "for infinite-dimensional ranges the converse FAILS for infinite
      l_oo-sums" must be withdrawn or marked OPEN. The c_0- and L_1[0,1]-examples remain correct.
 (L2) MISSTATED (minor): KLMW prove approximability for FINITE-CODIMENSIONAL proximinal subspaces of c_0
      and of K(l_2) (and for c_0-sums of reflexive spaces); "finite-codimensional" was dropped.
 (L3) MISATTRIBUTED (minor, notes 8 (F2), FROM MEMORY there): density of norm-attaining multilinear FORMS
      under RNP is credited to Aron-Finet-Werner (1995); Choi-Kim (J. London Math. Soc. 54 (1996)) treat
      polynomials / multilinear mappings (secondary source, see Section 2).
 (L4) PARTLY UNCONFIRMED: Acosta-Aguirre-Paya, Israel J. Math. 93 (1996) 221-227 is confirmed and does
      show that NA bilinear forms on X x X need not be dense; that the space is "G x G for a Gowers-type
      space G" is not confirmed by any snippet (keep as FROM MEMORY).
 (L5) UNCONFIRMED attribution: the fixed-Y l_1-sum lemma "in Paya-Saleh 2000" (notes Sec 2) was not found;
      the property-A form (ACKLM: "stable under arbitrary l_1-sums [12]") is confirmed.
 (L6) Literature on T2: confirmed that Choi-Dantas-Jung-Martin (Mediterr. J. Math. 16 (2019)) state the
      DOMAIN-side BPBp inheritance only for absolute summands of type 1 or oo, with density analogues (one
      snippet: type 1). Type 1 means that (1,0) is a vertex of the unit ball of the absolute norm (definition
      seen in Choi-Choi-Jung-Martin, RACSAM 2022, arXiv 2004.11025). So T2 (all absolute norms, all lattice
      sums, any Y) goes beyond what the snippets show; novelty remains unverified (full text not readable).
      Related recent work missed by the explorer: J. Kirme, "Stability of properties alpha and beta under
      absolute sums of Banach spaces", Acta Comment. Univ. Tartu. Math. 30(1) (2026) (abstract only seen).

0.4 New results added by the referee (Section 4; full proofs):
 R1 (PROVED) AA(C(K),Y) is dense in L(C(K),Y) for EVERY compact Hausdorff K and every finite-dimensional
    Y (lineability of NA(C(K),R) is NOT needed and is not claimed for perfect K).
 R2 (PROVED) The class AAD := {X : AA(X,Y) dense for every finite-dimensional Y} contains all reflexive
    spaces, all spaces with a dense linear subspace inside NA(X,R), and all C(K); it is stable under finite
    absolute and lattice sums, c_0-sums, l_p-sums (1<p<oo), and X -> C(K,X) when X* has RNP.
 R3 (PROVED, with the explorer's Prop 6) P(X) <=> P(X (+)_a Z) for every Z in AAD and every absolute a; in
    particular P(X) <=> P(X (+)_a C(K)) for EVERY compact K (e.g. Martin's space (+)_oo C[0,1]).
 R4 (PROVED) AAD is strictly smaller than the class of P-spaces: Read's space has P (Preprint B) and is not
    in AAD (Rmoutil). Hence Prop 6 cannot settle Q1 even for known P-spaces; P(R (+)_oo R) for Read's
    space R is a concrete instance of Q1 not covered by any result found (OPEN as far as I know).
 R5 (PROVED) Fixed-factor universality: X (x)_pi (Z_1 (+)_1 Z_2) = (X (x)_pi Z_1) (+)_1 (X (x)_pi Z_2) and
    X (x)_eps (Z_1 (+)_oo Z_2) = (X (x)_eps Z_1) (+)_oo (X (x)_eps Z_2) isometrically; hence for every
    fixed Z with a one-dimensional L-summand, NA(X (x)_pi Z, Y) dense => NA(X,Y) dense, and for every
    fixed Z with a one-dimensional M-summand, NA(X (x)_eps Z, Y) dense => NA(X,Y) dense, for ANY Y.
 R6 (PROVED) Wedge sums of metric spaces: F(M_1 v M_2) = F(M_1) (+)_1 F(M_2) and Lip_0(M_1 v M_2) =
    Lip_0(M_1) (+)_oo Lip_0(M_2) isometrically; so T1/T2 transfer to free spaces and Lip_0 of wedges.
 R7 (HEURISTIC) Why T10 is special to L_1: the analogous inheritance for L_p([0,1],X), 1<p<oo, and for
    C(K,X) with K perfect, is OPEN; the lifting proof breaks exactly at "||S_t|| <= ||S|| for every t".

0.5 Required corrections (numbered).
 C1. Replace "C_0(L) fails A for infinite L" by "for infinite metrizable L"; withdraw "l_oo fails A" and
     the derived claim about infinite l_oo-sums (mark OPEN / unsupported) [notes 5.5; field
     different_notions_that_fail].
 C2. KLMW: add "finite-codimensional" [known_results item 4].
 C3. RNP => dense NA multilinear forms: cite Aron-Finet-Werner 1995 (FROM MEMORY + secondary source);
     Choi-Kim 1996 for polynomials [notes 8 (F2)].
 C4. AAP 1996: keep the confirmed statement (some X with NA bilinear forms on X x X not dense); mark the
     identification "G x G, G Gowers-type" as FROM MEMORY [known_results item 6, notes 8 (F1)].
 C5. Label consistency: the verdict text calls the L_1(mu,X) inheritance "T3"; proved_here calls it T10.
 C6. positive_subclasses (1): "l_1(X) ... whenever X* has RNP" -- the RNP hypothesis is not needed for
     l_1(X) (Theorem 1); it is needed only for L_1(mu,X) with mu non-atomic (Prop 11).
 C7. Theorem 4 (C1) and (C3) with n = 1: say explicitly that the classes with a degenerate summand/factor
     are trivially universal and that the content is in the non-degenerate classes.
 C8. Corollary 6.1 / positive_subclasses (2): add C(K) (any compact K) to the admissible "other summands"
     (R1, R3); add Kirme 2026 to the literature on absolute sums.

## 1. Line-by-line re-derivation of the PROVED items

1.1 Lemma 1.1 (adjoint criterion) -- CORRECT. (=>) If ||Tx|| = ||T||, x in S_X, take y* in S_{Y*} with
y*(Tx) = ||Tx||; then (T*y*)(x) = ||T|| >= ||T*y*||, so equality and T*y* attains at x. (<=) If
|(T*y*)(x)| = ||T*y*|| = ||T|| with x in S_X, then ||Tx|| >= |y*(Tx)| = ||T||. T = 0 is trivial. For
dim Y < oo, y* -> ||T*y*|| is continuous on the compact S_{Y*} with maximum ||T||.

1.2 Absolute norms and Lemma 1.2 -- CORRECT. Monotonicity: s = lam s' + (1-lam)(-s') with
lam = (1 + s/s')/2 in [1/2,1] is right (lam s' - (1-lam)s' = (2 lam - 1)s' = s); evenness + convexity
give g(s) <= g(s'). max(|s|,|t|) <= a(s,t) <= |s|+|t|. Dual norm: the maximum of alpha s + beta t over the
sign-symmetric compact ball equals the maximum of |alpha| s + |beta| t over its positive part, attained
at a point with a(s,t) = 1 if (alpha,beta) != 0. ||f|| = a*(||f_1||,||f_2||): upper bound by the
definition of a*, lower bound by x = (s z_1, t z_2). If both f_i attain, f(x) = ||f|| exactly. (If one
f_i = 0, any unit z_i works.)

1.3 Banach sequence lattices, completeness of E(X_i) -- CORRECT. The Cauchy property of d^{n,m} in E uses
(L1) with the dominating sequence (||x^m_i - x^k_i||)_i, whose E-norm is ||x^m - x^k||; coordinatewise
convergence follows from |b_i| <= ||b||_E (L1 + L2). E(X_i) is a vector space by (L1).

1.4 AA operators -- CORRECT. (a) maximizer y* exists and S*y* attains. (b) reflexive. (c) KLMW criterion:
S*y* = sum_k y*(y_k) psi_k lies in V; ||S - T|| <= sum_k ||psi_k - phi_k|| ||y_k||. (d) uses Lemma 1.2
(and its finite-lattice analogue: the dual norm of an absolute normalized norm on R^n is attained at a
nonnegative norm-one vector s, and x = (s_i z_i)).

1.5 Theorem 1 (l_1-sums, any Y, any index set) -- CORRECT.
"<=": i0 with ||T_{i0}|| > 1 - eps, S_0 in NA with ||S_0 - T_{i0}|| < eps, S_0' = S_0/||S_0||,
||S_0' - T_{i0}|| <= |1 - ||S_0||| + eps < 3 eps; gluing (Lemma 2.1(b)) gives ||S|| = max(1, sup_{i!=i0}
||T_i||) = 1, attained at J_{i0} z, and ||S - T|| = ||S_0' - T_{i0}|| (Lemma 2.1(a)). Needs eps < 1/2 only
for ||S_0|| > 0; eps < 1/4 is harmless.
"=>": sum_i (||S|| - ||S_i||) ||x_i|| = 0 with nonnegative terms forces ||S_i|| = ||S|| on supp x; for
i != i0, ||S_i|| = ||(S - T)J_i|| < eps < 1 - eps < ||S||, so x = J_{i0}x_{i0}; then S_{i0} attains and
||S_{i0} - T_0|| < eps. Remark 2.2 (approximant attains at one coordinate) is correct.

1.6 Lemma 3.1 and Theorem 2 (condition (AD)) -- CORRECT, for ANY Y (finite dimension is never used).
(AD) for absolute sums: ||(u, lam w)|| = a(||u||, |lam| ||w||) <= a(||x_1||, ||w||) by monotonicity.
For E(X_i): the norm sequence of u + lam w is dominated coordinatewise by that of x_1 + w; apply (L1).
C(K,X) with k0 isolated: f -> (f(k0), f|K\{k0}) is onto because K\{k0} is clopen; sup norms give (+)_oo.
L_1(mu,X) with an atom A: strongly measurable functions are a.e. constant on an atom, so L_1(mu|A,X) = X.
Proof of T2: ||T|| = 1 (||P|| <= 1 and T = T_1 on X_1). ||S_W|| < eps since T vanishes on W; ||w|| <= 1
from (AD) with u = 0, lam = 1. Step 1: ||S|| <= ||S_1|| c + ||S_W|| ||w|| <= ||S|| c + eps gives
c >= 1 - eps/||S|| > (1 - 2eps)/(1 - eps) > 0 (so x_1 = 0 cannot occur). Step 3: for ||u|| <= 1,
E u = c^{-1}(cu + phi(u) w) with ||cu|| <= ||x_1|| and |phi(u)| <= 1, so ||Eu|| <= c^{-1}||x_1 + w|| = 1/c.
Step 4: E(x_1/c) = (x_1 + w)/c, so ||R(x_1/c)|| = ||S||/c >= ||R||. Step 5: ||R - S_1|| <= ||Sw||/c <=
eps/c and eps/c + eps < eps(1-eps)/(1-2eps) + eps < 2.5 eps < 3 eps for eps < 1/4. Since Y is arbitrary,
T2 also shows: property A passes to every absolute summand and every lattice summand of a domain space.

1.7 Theorem 4 -- CORRECT (the reductions are exactly T1, T2, T10 and the isometries of Prop 9; (C5)
contains X (x)_pi l_1^2 = X (+)_1 X and X (x)_eps l_oo^2 = X (+)_oo X). See 0.1 for the triviality remark.
Corollary 4.1 and 4.2 are correct (4.2 uses Prop 11 with X* isomorphic to l_1, which has RNP; RNP is an
isomorphic invariant).

1.8 Proposition 5 -- CORRECT. X* = l_1(X_i*) (c_0-sums) and l_q(X_i*) (l_p-sums), for arbitrary index
sets; ||phi - phi P_F|| is the tail norm, which tends to 0 along finite F; T P_F = T_F pi_F; S := S_F pi_F
has ||S|| = ||S_F||, attains at the inclusion of z, and ||S - T|| <= ||S_F - T_F|| + ||T - TP_F||. The
remarks on p = 1 (tails need not be small, e.g. (1,1,...) in l_oo) and infinite l_oo-sums are correct.

1.9 Proposition 6 -- CORRECT. Checks: AA(X_2,Y) and its density do not depend on the norm of Y (S*(Y*)
is norm-independent). Step 0: ||(0, S_2 - T_2)|| <= ||S_2 - T_2|| because ||x_2|| <= a(||x_1||,||x_2||);
AA is a cone. Step 1: ||(R_1,S_2')|| <= 1 iff ||R_1*y*|| <= phi(h_2(y*)) for all y*; h_2 <= ||S_2'||
<= ||T'|| = 1 so phi is evaluated on [0,1]; a*(., beta) is continuous, nondecreasing on [0,oo), equals
beta at 0 and tends to oo, so the sublevel set is [0, phi(beta)] and a*(phi(beta),beta) = 1. Step 2 fine.
Step 3: phi nonincreasing (a* monotone), concave (hypograph of the convex set {a* <= 1} in the positive
quadrant), phi(0) = 1, phi(beta) >= 1 - beta > 0 on [0,1) (a* <= sum), continuous on [0, r_2] (interior
continuity plus the chord bound at 0); D is a closed convex symmetric body with phi(r_2) B_Y in D in B_Y.
R_1(B) in D iff ||R_1||_{X_1 -> (Y,p_D)} <= 1 (D closed). Step 4: if ||T_1'||_D = r < 1, then
a*(h_1,h_2) <= a*(r phi(beta), beta) <= r + (1-r) beta <= r + (1-r) r_2 < 1, a contradiction (r = 0
included). Steps 5-6: the contact functional exists by compactness of S_{Y*} and continuity of psi; v != 0.
Step 7: ||S*y*|| = a*(phi(beta),beta) = 1 >= ||S|| and S*y* attains by Lemma 1.2 (beta = 0 trivial);
Lemma 1.1 gives S in NA. Step 8: ||S - T'|| = ||S_1' - T_1'|| <= ||S_1' - T_1'||_D since ||.|| <= p_D.
The mechanism is the Minkowski-difference body of Preprint B's Transfer Theorem, applied to an absolute
sum; Remark 6.2 (no conflict with Preprint B) is correct. Corollary 6.1(a)-(c) correct (induction uses
associativity of l_p and l_oo sums and 1.4(d); infinite c_0/l_p sums via Prop 5).

1.10 Proposition 7 -- (a)-(d) CORRECT; (e) correctly labelled FALSE. (c): with c = (sum ||f_i||^q)^{-1/p},
||x||_p^p = c^p sum ||f_i||^{(q-1)p} = 1 and f(x) = c sum ||f_i||^q = ||f||_q. (d): |m| purely atomic on a
scattered compactum (Pelczynski-Semadeni / Rudin; confirmed), m = sum_t delta_t (x) m({t}) because
||m(B)|| <= |m|(B); Urysohn functions with disjoint supports give f with ||f|| <= 1 and m(f) = ||m||.
(e): f = (1 - 1/i) in l_oo = l_1* does not attain; for l_1 itself the finitely-valued sequences form a
dense linear subspace of norm-attaining functionals (sums of finitely-valued sequences are
finitely-valued). The question for l_1(X_i) with infinite-dimensional X_i is genuinely different:
finitely-valued sequences are not dense in l_oo(l_2) ((e_i) has distance >= 1 from them).

1.11 Proposition 8 -- (i)-(iii) CORRECT; (iv),(v) correctly labelled HEURISTIC. For (iii) "c_0-stability
contains (C_oo)": X_1 (+)_oo X_2 is an l_oo-summand of c_0(X_1, X_2, X_2, ...), so T2 applies (no zero
spaces needed).

1.12 Proposition 9 -- CORRECT. (i)-(v) as written; (vi): the L_1(mu,X)-norm is a subcross norm, hence
<= pi; equality on simple tensors over disjoint sets, then by pi-continuity. Sigma-finiteness is not
needed for (vi). Proposition 12(a) CORRECT. Prop 12(b) SKETCH: the steps are standard (Bochner densities
by RNP of X*; common Borel partition shrunk to disjoint compact sets by inner regularity of the Radon
measure lambda; Q maps the closed ball onto the closed ball via Urysohn functions equal to 1 on C_j with
disjoint supports; R' o Q attains where R' does). I found no gap; the SKETCH label is appropriate.

1.13 Theorem 10 (L_1(mu,X) => X, Y finite-dimensional, atomless mu allowed) -- CORRECT (modulo the
lifting theorem, confirmed: von Neumann 1931, Maharam 1958, Ionescu Tulcea 1969). Key points checked:
(1) T1 "=>" reduces to a complete probability nu (completion does not change L_1(nu,X)). (2) Densities:
||H_x(t)|| <= ||S|| ||x|| a.e. by the dense-sequence argument (strict inequality of the integral on a
set of positive measure). (3) The lifting acts on a.e.-classes, so x -> S_t x is linear for EVERY t, and
positivity of rho gives y_k*(S_t x) <= ||S|| ||x|| for EVERY t, hence ||S_t|| <= ||S|| everywhere.
(4) Sf = int S_t f(t) dnu: first for simple f, then via f_n = g_n 1_{||g_n|| <= 2||f||} (which converges
a.e. to f, also where f = 0), domination 2||S|| ||f(t)||, completeness for measurability. (5) For
T = T_0 Phi: (S - T)_t = S_t - T_0 for every t since rho(1) = 1; so ||S_t - T_0|| <= ||S - T|| for every t.
(6) Equality in ||S|| = int y*(S_t f(t)) <= ||S|| ||f||_1 gives a t0 with f(t0) != 0 and S_{t0} attaining.
Remark (1) (separable X without lifting) is correct. The proof is genuinely specific to L_1: see R7.

1.14 Proposition 11 (X* RNP, P(X) => P(L_1(mu,X))) -- CORRECT, modulo L_1(nu,X)* = L_oo(nu,X*) (confirmed
for sigma-finite nu). G = sum_j g_j (x) b_j is essentially separably valued; A_k := {||G - R_k|| < eps}
minus earlier ones is a measurable partition of a full-measure set; ||S - S'|| <= eps; S' = R o Psi with
||Psi|| <= 1; T1 + Remark 2.2 give R' attaining at J_{k0} z; f_0 = 1_{A_{k0}} z / nu(A_{k0}) gives
Psi f_0 = J_{k0} z and S'' = R' Psi attains. This is the operator analogue of Dantas-Garcia-Maestre-Martin
(Canad. J. Math. 70 (2018)), who reduce the compact-operator BPBp for L_1(mu,X) to l_1(X) under the same
hypothesis "X* has RNP" (confirmed snippet).

1.15 Proposition 13 (property alpha stable under (x)_pi) -- CORRECT. |phi_ij(u_kl)| = |x_i*(x_k)||z_j*(z_l)|
is <= lambda_X if k != i and <= lambda_Z if k = i, l != j; the projective ball is the closed absolutely
convex hull of B_X (x) B_Z, and x (x) z is a limit of absolutely convex combinations of the u_ij.
1.16 Proposition 14 (K(H) lineable) -- CORRECT (tr(KS) = sum_n s_n <K f_n, e_n>; equality forces
K f_n = e_n; an infinite-rank S would make K non-compact; finite-rank S are dense in S_1(H)).
1.17 Proposition 15 -- CORRECT (the factorization through F = R^n / ker M gives S*phi in V; S*phi0 attains
at x0; A x0 lies in W and attains at z0; closure of V (x) W = approximable operators; the examples use
Pitt's theorem and the AP of l_1, l_q). 1.18 The l_4^2 computation in Sec 8 -- CORRECT (unique norming
functionals in the smooth space l_4^2 force A e_2 = (b,d) with b z_1^3 + d z_2^3 = 0, and the s^2 term
forces b = 0 and d = 0 when z_1 z_2 != 0, so A = e_1* (x) z has rank one and ||A - I|| >= 1).
1.19 F-bil (FALSE) -- correctly refuted: NA(X (x)_pi Z, R) is always dense (Bishop-Phelps), NA bilinear
forms are not (AAP 1996; Choi 1997).

## 2. Citation check (WebSearch, standard mode unless noted; full texts not readable)

2.1 Aron-Choi-Kim-Lee-Martin, "The Bishop-Phelps-Bollobas version of Lindenstrauss properties A and B",
Trans. AMS 367 (2015) 6085-6101, arXiv 1305.6420. CONFIRMED (https://www.ams.org/journals/tran/2015-367-09/S0002-9947-2015-06551-9 ;
https://arxiv.org/pdf/1305.6420). Snippets: "Lindenstrauss property A is stable under arbitrary l1-sums [12]"
and "Lindenstrauss property B is stable under arbitrary c0-sums [4, Proposition 3]". Identity of [12] as
Choi-Song not seen (plausible). Both statements are easy (T1 with arbitrary Y; for B: perturb the
dominant coordinate so that it is strictly largest).

2.2 Choi-Dantas-Jung-Martin, "The Bishop-Phelps-Bollobas property and absolute sums", Mediterr. J. Math.
16 (2019) no. 3, paper 73, DOI 10.1007/s00009-019-1346-6, arXiv 1806.09366. CONFIRMED
(https://oasis.postech.ac.kr/handle/2014.oak/100835 ; https://arxiv.org/pdf/1806.09366). Abstract: range
side for every absolute summand; domain side for absolute summands of type 1 or oo; "analogous results
for ... the density of norm-attaining operators"; one snippet: the density results "also hold for type 1
absolute norms". Type 1 = (1,0) is a vertex of the unit ball (Choi-Choi-Jung-Martin, "On quasi norm
attaining operators between Banach spaces", RACSAM 2022, arXiv 2004.11025, https://arxiv.org/pdf/2004.11025).
The explorer's description is accurate; T2's full generality is not visible in any snippet.

2.3 Choi-Song, "Property (quasi-alpha) and the denseness of norm attaining mappings", Math. Nachr. 281
(2008). CONFIRMED (https://oasis.postech.ac.kr/handle/2014.oak/22500): quasi-alpha implies A; if X_k
(1 <= k <= n-1) have quasi-alpha and X_n has A, then X_1 (x)_pi ... (x)_pi X_n has A. Matches the notes.

2.4 Kadets-Lopez-Perez-Martin-Werner, "Norm attaining operators of finite rank", in: The Mathematical
Legacy of Victor Lomonosov, De Gruyter 2020, 157-188, arXiv 1905.08272. CONFIRMED
(https://arxiv.org/pdf/1905.08272): dense linear subspace of NA functionals => density of NA finite-rank
operators; finite-rank operators approximable for FINITE-CODIMENSIONAL proximinal subspaces of c_0 or of
K(l_2) and for c_0-sums of reflexive spaces; K(l_2) and c_0-sums of reflexive spaces listed among spaces
whose NA functionals form a vector space. Status: misstated in a minor way (C2).

2.5 Acosta-Aguirre-Paya, "There is no bilinear Bishop-Phelps theorem", Israel J. Math. 93 (1996) 221-227,
DOI 10.1007/BF02761104. CONFIRMED that NA bilinear forms on X x X are not dense for some X
(https://link.springer.com/article/10.1007/BF02761104). "X = G, a Gowers-type space": not confirmed
(the 1992 Acta Univ. Carolin. paper of the same authors uses Gowers' space for NA(G,l_p) not dense;
https://www.dml.cz/bitstream/handle/10338.dmlcz/701970/ActaCarolinae_033-1992-2_2.pdf). See C4.

2.6 Y.S. Choi, "Norm attaining bilinear forms on L1[0,1]", J. Math. Anal. Appl. 211 (1997) 295-300,
DOI 10.1006/jmaa.1997.5461. CONFIRMED (https://remotecenter.postech.ac.kr/handle/2014.oak/20923). Related:
Y. Saleh, IJMMS 23 (2000) 833-837: NA bilinear forms on L_1(mu) dense iff mu purely atomic
(https://emis.univie.ac.at/journals/HOA/IJMMS/Volume23_12/421296.abs.html).

2.7 Finet-Paya, Israel J. Math. 108 (1998) 139-143 (DOI 10.1007/BF02783045) and Paya-Saleh, Arch. Math. 75
(2000) 380-388 (DOI 10.1007/s000130050519). CONFIRMED (https://link.springer.com/article/10.1007/s000130050519):
NA(L_1(mu), L_oo(nu)) dense for arbitrary mu and localizable nu. The "l_1-sum lemma in Paya-Saleh"
(notes Sec 2, FROM MEMORY) was NOT found (C-L5).

2.8 Property A failures. CONFIRMED with a qualifier: c_0, non-atomic L_1(mu), and C(K) for infinite
METRIZABLE K (C_0(L) for infinite metrizable L) fail A; L_1(mu) has A iff mu is purely atomic
(Martin's 2016 lecture notes https://www.ugr.es/local/mmartins/material/2016-Korea-ILJU-school-NOTES.pdf ;
ACKLM 2015). MISSTATED in the notes: "infinite L" without "metrizable", and "l_oo = C(beta N) fails A"
is not supported by any source found (C1).

2.9 Ryan, Introduction to Tensor Products of Banach Spaces (2002), Thm 5.33: (X (x)_eps Y)* = X* (x)_pi Y*
when X* or Y* has RNP and X* or Y* has AP. CONFIRMED indirectly: arXiv 2404.03322 cites "[6, Theorem 5.33]"
with exactly this statement (https://arxiv.org/pdf/2404.03322); identity of [6] not seen. Reflexivity of
l_p (x)_pi l_q iff 1/p + 1/q < 1: CONFIRMED (https://arxiv.org/pdf/2202.00371 states the iff;
https://arxiv.org/pdf/2409.20220 the "if" via Pitt).

2.10 Norm-attaining TENSORS. CONFIRMED: Dantas-Jung-Roldan-Rueda Zoca, Mediterr. J. Math. 19 (2022),
DOI 10.1007/s00009-021-01949-5 (https://arxiv.org/abs/2006.09871v3); Rueda Zoca, Mediterr. J. Math. 20
(2023) 208 (https://arxiv.org/pdf/2209.02947); Garcia-Lirola, Guerrero-Viu, Rueda Zoca, "Projective tensor
products where every element is norm-attaining", Banach J. Math. Anal. 19 (2025) (https://arxiv.org/abs/2407.10710);
arXiv 2607.28054 exists, title "Projective norm-attainments and their implications"
(https://arxiv.org/pdf/2607.28054); content not read.

2.11 Dantas-Garcia-Maestre-Martin, "The Bishop-Phelps-Bollobas property for compact operators", Canad. J.
Math. 70 (2018) 53-73, arXiv 1604.00618. CONFIRMED (https://dcmpx.remotevs.com/org/arxiv/PL/pdf/1604.00618):
if X* has RNP and (l_1(X),Y) has the BPBp for compact operators, so does (L_1(mu,X),Y).

2.12 Johnson-Wolfe, "Norm attaining operators", Studia Math. 65 (1979) 7-19, DOI 10.4064/sm-65-1-7-19.
CONFIRMED (https://eudml.org/doc/218261). The L_1-predual statement itself was not visible in snippets
(given as background in the task). Schachermayer, Pacific J. Math. 105 (1983): an operator L_1[0,1] ->
C[0,1] not approximable, so C[0,1] fails B (https://msp.org/pjm/1983/105-2/pjm-v105-n2-p13-s.pdf).

2.13 Items marked FROM MEMORY by the explorer, now checked:
 - Lifting theorem (von Neumann 1931, Maharam 1958; Ionescu Tulcea, Topics in the Theory of Lifting,
   Springer 1969): CONFIRMED (https://en.wikipedia.org/wiki/Lifting_theory).
 - L_1(mu,X)* = L_oo(mu,X*) iff X* has RNP (w.r.t. mu), mu sigma-finite (Diestel-Uhl IV.1): CONFIRMED by
   secondary sources (e.g. https://arxiv.org/pdf/2109.15001); the theorem number IV.1.1 not seen.
 - Singer's representation C(K,X)* = rcabv(K,X*): CONFIRMED (Hensgen, "A simple proof of Singer's
   representation theorem", PAMS 1996, https://www.ams.org/proc/1996-124-10/S0002-9939-96-03493-4/).
 - Scattered K iff every Radon measure is atomic (Pelczynski-Semadeni, Rudin): CONFIRMED (snippets).
 - Schachermayer (alpha => A), Israel J. Math. 44 (1983), DOI 10.1007/bf02760971: CONFIRMED via
   secondary sources.
 - Choi-Kim 1996 "RNP => dense NA multilinear forms": MISATTRIBUTED (C3): a 2024 Filomat paper credits
   forms to Aron-Finet-Werner and polynomials to Choi-Kim (J. London Math. Soc. 54 (1996) 135-147,
   https://remotecenter.postech.ac.kr/handle/2014.oak/21498).
 - Rmoutil (Read's space has no 2-dimensional subspace in NA): CONFIRMED, J. Funct. Anal. 272 (2017)
   918-928, arXiv 1503.06112 (https://arxiv.org/pdf/1503.06112).
 - Ruess-Stegall (injective tensor product of Asplund spaces is Asplund): not checked (side remark).

2.14 Missed related literature: J. Kirme, "Stability of properties alpha and beta under absolute sums of
Banach spaces", Acta Comment. Univ. Tartu. Math. 30(1) (2026), DOI 10.12697/ACUTM.2026.30.12
(https://ojs.utlib.ee/index.php/ACUTM/article/view/26686): hereditary results for l_1-sums and forward
stability of alpha under polygonal absolute sums (abstract only). It concerns alpha/beta, not P.

## 3. Verdict check

3.1 No overclaim: no counterexample is claimed (any would solve JW); no "always dense" is claimed.
Theorem 4 is exactly an equivalence with property B of the fixed Y, with complete proofs. The positive
subclasses are each backed by a PROVED item or a confirmed known theorem, except Prop 12(b) (SKETCH,
correctly labelled) and the l_oo context claim (C1).
3.2 No underclaim found: Q1-Q6 are, to my knowledge, not settled in the literature found; my R1-R5 extend
the positive side but do not touch Q1 for pairs of non-AA spaces (R4).
3.3 corrected_verdict: EQUIVALENT_TO_JOHNSON_WOLFE.

## 4. New results by the referee (complete proofs)

Definition. AAD := {X : AA(X,Y) is dense in L(X,Y) for every finite-dimensional Y}.
Reformulation (PROVED). X is in AAD iff for every d >= 1, every (phi_1..phi_d) in (X*)^d and every eta > 0
there are psi_j with ||psi_j - phi_j|| < eta and span{psi_1..psi_d} contained in NA(X,R).
Proof: for S = sum_j psi_j (x) e_j in L(X,R^d), S*y* = sum_j y*(e_j) psi_j, so S is in AA iff the span of
the psi_j lies in NA(X,R). If U : Y -> R^d is a linear isomorphism, (US)* = S*U* with U* onto, so S is in
AA(X,Y) iff US is in AA(X,R^d), and U preserves density. QED. By 1.4(a), AAD is contained in P.

### R1 (PROVED). For every compact Hausdorff K and finite-dimensional Y, AA(C(K),Y) is dense. So C(K) is in AAD.
Proof. Let b_1..b_d be a basis of Y, b_j* the dual basis, T in L(C(K),Y), m_j := T*b_j* in M(K) (Riesz),
so T f = sum_j m_j(f) b_j. Put lambda := sum_j |m_j| (finite positive regular Borel measure). If lambda = 0,
T = 0. Otherwise m_j = h_j lambda with h_j in L_1(lambda) (Radon-Nikodym; |m_j| <= lambda). Let eta > 0.
Choose a finite Borel partition B_1..B_n of K and reals c_jk with sum_j ||h_j - sum_k c_jk 1_{B_k}||_1 <
eta (common refinement for the d functions). Inner regularity: for each k there is a compact C_k in B_k
with lambda(B_k \ C_k) as small as we like [take an open U containing K \ B_k with lambda(U \ (K\B_k))
small, by outer regularity, and C_k := K \ U]; choose them with sum_{j,k} |c_jk| lambda(B_k \ C_k) < eta.
Set m_j' := (sum_k c_jk 1_{C_k}) lambda and S := sum_j m_j' (x) b_j. Then sum_j ||m_j - m_j'|| < 2 eta and
||S - T|| <= 2 eta max_j ||b_j||. For y* in Y*: S*y* = sum_k a_k lambda|_{C_k} with a_k := sum_j y*(b_j)
c_jk. The C_k are pairwise disjoint, so ||S*y*|| = sum_k |a_k| lambda(C_k). The sets P := union{C_k :
a_k > 0} and N := union{C_k : a_k < 0} are disjoint and compact; K is normal, so there is a continuous
f : K -> [-1,1] with f = 1 on P and f = -1 on N (f = +-1 constant if one of them is empty). Then
<S*y*, f> = sum_k a_k int_{C_k} f dlambda = sum_k |a_k| lambda(C_k) = ||S*y*||, ||f|| <= 1. So S*y* is in
NA(C(K),R) for every y*, i.e. S is in AA(C(K),Y). QED.
Remarks. (i) This is the mechanism behind the Johnson-Wolfe theorem for C(K) (attribution FROM MEMORY).
(ii) Lineability of NA(C(K),R) for perfect K is NOT claimed and NOT needed: AA-density is built
operator by operator. (iii) For L_1(mu) (sigma-finite) the simple functions form a dense linear subspace
of L_oo(mu) inside NA(L_1(mu),R) (finitely many values, so the ess sup is attained on a set of positive,
and by sigma-finiteness positive finite, measure); so L_1(mu) is lineable, already covered by the notes.

### R2 (PROVED). Stability of AAD.
(a) Reflexive spaces, spaces X with a dense linear subspace of X* inside NA(X,R), and all C(K) are in AAD
(notes 1.4(b),(c); R1). (b) Finite absolute sums and finite lattice sums of AAD-spaces are in AAD (notes
1.4(d), re-checked in 1.4 above). (c) c_0(X_i) and l_p(X_i), 1 < p < oo, are in AAD if every X_i is.
(d) If X is in AAD and X* has RNP, then C(K,X) is in AAD for every compact Hausdorff K.
Proof of (c). X* = l_1(X_i*) (resp. l_q(X_i*)). Given phi_1..phi_d and eta, choose a finite F with
sum_j ||phi_j - phi_j 1_F|| < eta. For i in F apply the reformulation in X_i to (phi_{1,i},..,phi_{d,i})
with tolerance eta/|F|, getting psi_{j,i} whose span lies in NA(X_i,R); put psi_j := (psi_{j,i})_{i in F},
extended by 0. Then ||psi_j - phi_j|| < 2 eta. For c in R^d, f := sum_j c_j psi_j has components
f_i = sum_j c_j psi_{j,i} in NA(X_i,R) for i in F and 0 elsewhere; it attains its norm by the formulas of
Prop 7(b),(c) (x = sum_{i in F} J_i z_i for c_0; x = c sum ||f_i||^{q-1} J_i z_i for l_p). QED.
Proof of (d). WLOG Y = R^d. Let phi_1..phi_d in C(K,X)* = rcabv(K,X*) (Singer), lambda := sum_j |phi_j|.
X* has RNP and phi_j << lambda has bounded variation, so phi_j = g_j lambda with g_j in L_1(lambda,X*)
(Bochner), <phi_j, f> = int <g_j(t), f(t)> dlambda, ||phi_j|| = int ||g_j|| dlambda. Choose a common Borel
partition B_1..B_n and x*_jk in X* with sum_j ||g_j - sum_k 1_{B_k} x*_jk||_{L_1(lambda,X*)} < eta, then
compact C_k in B_k with sum_{j,k} ||x*_jk|| lambda(B_k \ C_k) < eta (inner regularity as in R1). For each k
apply X in AAD to (x*_1k,..,x*_dk) with tolerance eta/(1 + lambda(K)), getting w*_jk with
span_j{w*_jk} in NA(X,R). Put psi_j := (sum_k 1_{C_k} w*_jk) lambda (a regular X*-valued measure); then
||psi_j - phi_j|| < 3 eta (sum over j). For c in R^d, psi := sum_j c_j psi_j = (sum_k 1_{C_k} v_k) lambda with
v_k := sum_j c_j w*_jk in NA(X,R) and ||psi|| = sum_k lambda(C_k) ||v_k||. Pick z_k in S_X with v_k(z_k) =
||v_k||, disjoint open U_k containing C_k, Urysohn u_k : K -> [0,1] with u_k = 1 on C_k, supp u_k in U_k,
and f := sum_k u_k z_k. Then ||f|| <= 1, f = z_k on C_k, and <psi, f> = sum_k lambda(C_k) v_k(z_k) = ||psi||.
So span{psi_j} lies in NA(C(K,X),R). QED.
Consequence. Prop 12(b) of the notes (SKETCH) is now PROVED, in the stronger AA form, for X reflexive or
finite-dimensional (both are in AAD with X* RNP), every compact K; also for X = c_0 and X = K(l_2)
(lineable, separable duals), e.g. C([0,1],c_0) and C([0,1],K(l_2)) are in AAD, hence have P.

### R3 (PROVED). If Z is in AAD and a is any absolute normalized norm, then P(X) <=> P(X (+)_a Z).
"<=": T2. "=>": Prop 6 with X_1 = X ((H1) is P(X) applied to the norm p_D) and X_2 = Z ((H2)). As in
Cor 6.1(b), the same holds for finite l_p/l_oo sums, and (Prop 5) c_0- and l_p-sums (1<p<oo), in which one
summand has P and all others are in AAD. Examples (new w.r.t. the notes): P(X) <=> P(X (+)_a C(K)) for
every compact K; P(Martin's space (+)_oo C[0,1]) <=> P(Martin's space); P(R (+)_a C[0,1]) holds for Read's
space R (P(R) by Preprint B).

### R4 (PROVED). AAD is strictly smaller than the class of P-spaces.
Read's space R (Read's renorming of c_0, as in Preprint B) has P: Preprint B proves NA(R,F) dense for
every reflexive F (KNOWN from Preprint B, not re-checked here). R is not in AAD: by Rmoutil (confirmed)
NA(R,R) contains no 2-dimensional subspace. Take phi_1, phi_2 in R* independent, delta := dist(phi_2,
R phi_1) > 0. If ||psi_j - phi_j|| < eta < ||phi_1||/2 with span{psi_1,psi_2} in NA, the span is not
2-dimensional, so psi_2 = c psi_1 with |c| <= (||phi_2|| + eta)/(||phi_1|| - eta) =: C', and
delta <= ||phi_2 - c phi_1|| < (1 + C') eta, impossible for small eta. The same argument applies to the
smooth Read space (same NA set, Preprint B Lemma smoothing) and to Martin's space (Preprint B: NA meets
every 2-dimensional subspace of the dual in at most two lines). QED.
Consequence (HEURISTIC/OPEN). Prop 6 and R3 cannot decide Q1 for pairs of non-AAD spaces. A concrete open
instance: does R (+)_oo R (R = Read's space) have P? Both summands have P; neither is AAD; the lift lemma of
Preprint B needs a norm of the form q + s and does not directly apply to max(p(x), p(y)). I found no result
covering it. (A negative answer would refute JW by Prop 8(ii), so it is not expected.)

### R5 (PROVED). Fixed-factor universality for tensor products.
(a) X (x)_pi (Z_1 (+)_1 Z_2) = (X (x)_pi Z_1) (+)_1 (X (x)_pi Z_2) isometrically.
(b) X (x)_eps (Z_1 (+)_oo Z_2) = (X (x)_eps Z_1) (+)_oo (X (x)_eps Z_2) isometrically.
(c) If Z = R (+)_1 Z' for some Z' (Z has a one-dimensional L-summand), then NA(X (x)_pi Z, Y) dense implies
NA(X,Y) dense, for EVERY Banach space Y. (d) If Z = R (+)_oo Z' (one-dimensional M-summand), then
NA(X (x)_eps Z, Y) dense implies NA(X,Y) dense, for every Y. Hence, for each such fixed Z, the class
{X (x)_pi Z : X Banach} (resp. {X (x)_eps Z}) is universal: "NA dense on the whole class for this Y" iff
"Y has property B", for every Y, finite-dimensional or not.
Proof. (a) Let P_j, iota_j be the coordinate projections/injections of Z_1 (+)_1 Z_2 and, on the
algebraic tensor product, J u := (u_1, u_2) with u_j := (I (x) P_j) u. For any representation
u = sum_k x_k (x) (z_k^1, z_k^2): pi(u_1) + pi(u_2) <= sum_k ||x_k|| (||z_k^1|| + ||z_k^2||) = sum_k
||x_k|| ||(z_k^1,z_k^2)||_1; taking the infimum, ||Ju|| <= pi(u). Conversely u = (I (x) iota_1)u_1 +
(I (x) iota_2)u_2 and the metric mapping property gives pi(u) <= pi(u_1) + pi(u_2). So J is isometric; it
extends to the completions, its range is closed and contains the dense algebraic part, hence onto.
(b) (Z_1 (+)_oo Z_2)* = Z_1* (+)_1 Z_2*. For x* in B_{X*} and z* = (z_1*, z_2*) with ||z_1*|| + ||z_2*|| <= 1:
(x* (x) z*)(u) = (x* (x) z_1*)(u_1) + (x* (x) z_2*)(u_2), of modulus <= max(eps(u_1), eps(u_2)); the
choices z* = (z_1*, 0), (0, z_2*) give the reverse inequality. So eps(u) = max(eps(u_1), eps(u_2)); extend
as in (a). (c) X (x)_pi R = X, so X (x)_pi Z = X (+)_1 (X (x)_pi Z'); apply Theorem 1 ("=>"). (d) Same with
X (x)_eps R = X and Theorem 2 (condition (AD) holds for (+)_oo). QED.
Examples: (c) Z = l_1(Gamma), l_1^n (n >= 2), L_1(mu) with an atom; (d) Z = c_0(Gamma), l_oo, l_oo^n,
C(K) with K having an isolated point. This contains the notes' classes (C3) (atomic case) and (C4). For
atomless L_1(mu) the notes' Theorem 10 is needed and gives the result only for finite-dimensional Y.

### R6 (PROVED). Wedge sums: a bridge to the Lipschitz-free classes.
For pointed metric spaces (M_1,0), (M_2,0) let M = M_1 v M_2 be the disjoint union with the base points
identified and d(x,y) := d_1(x,0) + d_2(0,y) for x in M_1, y in M_2 (a metric: the triangle inequality
follows from d(x,y) >= d_1(x,0) and d(x,y) >= d_2(0,y)). Then (i) Lip_0(M) = Lip_0(M_1) (+)_oo Lip_0(M_2)
and (ii) F(M) = F(M_1) (+)_1 F(M_2), isometrically.
Proof. (i) f -> (f|M_1, f|M_2) is a linear bijection (pairs vanishing at 0 glue). Lip(f) >= max(Lip f_1,
Lip f_2) trivially; for x in M_1, y in M_2: |f(x) - f(y)| <= |f_1(x) - f_1(0)| + |f_2(0) - f_2(y)| <=
max(L_1,L_2)(d_1(x,0) + d_2(0,y)). (ii) Let iota_j : F(M_j) -> F(M) be the linearizations of the isometric
inclusions and Phi(mu_1,mu_2) := iota_1 mu_1 + iota_2 mu_2. By (i), ||Phi(mu_1,mu_2)|| = sup{<f_1,mu_1> +
<f_2,mu_2> : max(Lip f_1, Lip f_2) <= 1} = ||mu_1|| + ||mu_2||. The range is closed and contains delta(M),
whose span is dense; so Phi is onto. QED. (Standard; FROM MEMORY that it is in the literature, e.g. work of
Kaufmann on products of free spaces.)
Consequence: for every Y, NA(F(M_1 v M_2), Y) is dense iff NA(F(M_1),Y) and NA(F(M_2),Y) are dense
(Theorem 1), and NA(Lip_0(M_1 v M_2), Y) dense implies NA(Lip_0(M_i), Y) dense (Theorem 2). So, inside the
Lipschitz-free class, gluing metric spaces at a point can neither create nor destroy a counterexample.

### R7 (HEURISTIC; the limits of Theorem 10).
Write S in L(L_p(nu,X),Y) (1 < p < oo) or in L(C(K,X),Y) through densities t -> S_t as in Theorem 10. In
both cases ||S*y*|| is an AVERAGE over t of ||S_t*y*|| (an L_{p'}-norm, resp. an integral against a control
measure), not an essential supremum. Norm attainment of S at f then gives, for a.e. t in supp f, that
S_t*y* attains its norm at f(t)/||f(t)||, but not that y* maximizes ||S_t*z*|| over z*; so S_t is only
NEAR-attaining, and passing from near- to exact attainment is a Bishop-Phelps-Bollobas-type step that is
not available for general X. For p = 1 the dual norm is an ess sup, which yields ||S_t|| <= ||S|| =
||S_t*y*|| at a.e. t of supp f; this is exactly where Theorem 10 works. Hence the inheritance
"NA(L_p([0,1],X),Y) dense => NA(X,Y) dense" (1 < p < oo) and "NA(C(K,X),Y) dense => NA(X,Y) dense" for
perfect K remain OPEN; the notes claim neither (they claim l_p(X) and C(K,X) with an isolated point only).

## 5. Status of the open questions after this referee pass

Q1 ((C_a): P(X_1), P(X_2) => P(X_1 (+)_a X_2)). OPEN. Now known when one summand has P and the other is in
AAD (Prop 6 + R1/R2: reflexive, lineable, C(K), c_0- and l_p-sums of such, C(K, reflexive)). Concrete
undecided instances: R (+)_oo R and R (+)_oo (Martin's space), R = Read's space (R4). A failure would refute
JW (Prop 8(ii), correct).
Q2 (P(X) => P(L_1([0,1],X)) without RNP of X*). OPEN. The direct "replace S_t near t0" approach needs a
set of positive measure on which t -> S_t is nearly constant in operator norm, which fails for
weak*-densities (Rademacher-type densities in l_oo = l_1*); in that example P holds for other reasons
(L_1([0,1],l_1) = l_1(L_1[0,1]), Theorem 1 + Uhl).
Q3 (C(K,X), K perfect). Inheritance C(K,X) => X: OPEN (R7). P(X) => P(C(K,X)): PROVED for X in AAD with X*
RNP (R2(d)); for non-AAD X with X* RNP it reduces (Prop 12(b), SKETCH) to P(l_oo^m(X)), i.e. to Q1.
Q4 (l_oo(X_i) infinite; lineability of l_1(X_i), l_oo(X_i), general (x)_eps): OPEN; note the obstruction
in 1.10 for the naive approach in l_1(l_2).
Q5 (general finite lattice sums in Prop 6): SKETCH in the notes; not re-proved here (the two-summand absolute
case suffices for all statements above).
Q6 (property A under finite (+)_oo or (+)_p sums, infinite-dimensional ranges): OPEN as far as found.
Context (C1): whether l_oo has property A is not settled by any source found.
New: inheritance from L_p([0,1],X) (1<p<oo) and from C(K,X) (K perfect) to X: OPEN (R7).

## 6. Final status table (referee)

T1 PROVED/correct. T2 PROVED/correct (any Y; also gives domain inheritance of property A). T4 PROVED/correct
(trivial for degenerate classes). P5 PROVED/correct. P6 PROVED/correct. P7(a)-(d) PROVED/correct;
P7(e) FALSE/correct. P8(i)-(iii) PROVED/correct; (iv),(v) HEURISTIC. P9 PROVED/correct. T10 PROVED/correct
(lifting confirmed). P11 PROVED/correct (duality confirmed). P12(a) PROVED/correct; P12(b) SKETCH, now PROVED
for X in AAD with X* RNP (R2(d)). P13, P14, P15 PROVED/correct. F-bil FALSE/correct.
Known-results list: 2 misstatements (C1 metrizability and l_oo; C2 finite codimension), 1 misattribution
(C3), 2 partly unconfirmed attributions (C4, L5); everything else confirmed.
Verdict: EQUIVALENT_TO_JOHNSON_WOLFE (confirmed).
