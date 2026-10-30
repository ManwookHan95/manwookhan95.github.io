# Referee report, key = fbl: free Banach lattices FBL[E], finite-dimensional ranges Y

This is an adversarial check of fbl_notes.md and the explorer's structured result. Real scalars throughout. Notation follows the notes: S = S_{E^*}, N(nu) = sup_{x in B_E} int_S |u(x)| d|nu|(u), F_nu, M_nu, I(nu) = supp nu^+ cap supp nu^-.

Labels:
- PROVED: full proof given here, or the notes' proof verified line by line.
- KNOWN [S]: confirmed by a web-search hit in this session (URL given).
- KNOWN [M]: from memory only.
- SKETCH, HEURISTIC, OPEN, FALSE: as usual.

Network limits (important for Section 2):
- The per-turn WebSearch budget (200 calls, shared by every agent of this turn) was already used up when this referee started. Both of my search calls were refused, so I could run no new search.
- The one extra host I tried was export.arxiv.org, arXiv's own metadata API, for a direct lookup by identifier. It does not resolve in this session; it would have to be allowed in the session's network settings. I tried no further hosts.
- Citation checks therefore rest on two sources:
  - confirmations obtained earlier in this session by the sibling referees (lipzero_referee.md, sums_tensors_referee.md, lipfree_referee.md, same folder), whose URLs are repeated below;
  - my memory, marked [M].
- I could not re-check the explorer's claims that its FBL-specific references were confirmed by search. They are listed as unverified-by-referee in Section 2.

## 0. Bottom line

1. **Verdict OPEN: confirmed.** It is neither overclaimed nor underclaimed.
   - No counterexample is claimed; one would answer Johnson-Wolfe.
   - "Always dense" is claimed only for dim E < oo, and that proof is complete (Theorem 5.2, verified in 1.5 below).
   - For infinite-dimensional E, including FBL(A) = FBL[l_1(A)] with A infinite, density is OPEN. No argument in the notes or in this report closes it.
   - EQUIVALENT_TO_JOHNSON_WOLFE is not justified, because only the trivial direction is known (JW positive => density for every FBL[E]).

2. **Every PROVED claim was re-derived. All are correct, with these exceptions.**
   - (E1) **GAP, now fixed.** Cor 4.2(b) states "NA(C(S),R) is strictly contained in NA(FBL[E],R) when dim E >= 2", but only E = l_2^2 is proved. R5 (Section 3.5) proves it for every 2 <= dim E < oo. The claim is peripheral.
   - (E2) **FALSE (a FROM MEMORY remark).** Remark 5.3(3) says Lindenstrauss property A for C[0,1] is "not settled". In fact C[0,1] fails property A.
     - This follows from the classical extreme-point argument (Lemma L in Section 3.1): ext B_{C[0,1]} = {+-1}.
     - It is also confirmed in this session: "C(K) fails property A for infinite metrizable K" (lipzero_referee.md, D8/C16, via arXiv 1306.1155).
     - The FBL analogue is new and PROVED here (R1): FBL[E] fails property A for 2 <= dim E < oo.
   - (E3) **OVERSTATEMENT in the JSON only.** The proved_here entry "Props 7.1-7.7" says "Cylindrical operators lie in the closure of NA". Prop 7.6 needs the hypothesis that Q(B_E) is closed (e.g. E reflexive). The notes state the hypothesis, and the JSON's positive_subclasses item (iii) also does.
   - (E4) **Minor points.**
     - "Non-proportional" in the JSON should read "pairwise non-positively-proportional" (Lemma 2.4). The JSON form is a stronger hypothesis, so it is still true.
     - In 7.2, y^* -> |T^*y^*|(g) is (||T|| ||g||)-Lipschitz, not ||g||-Lipschitz.
     - Prop 3.3, Step 1 needs a Borel B with 0 < rho(B) < 1. When rho is a Dirac mass no such B exists, but the conclusion of Step 2 is then immediate.
     - The citation "Gao-Lau (1990s)" is vague. I believe it is J. Gao, K.-S. Lau, J. Austral. Math. Soc. Ser. A 48 (1990) 101-112 [M]. Nothing depends on it, since Lemma 3.5 is re-proved.
     - arXiv 2505.24084 is cited without authors.
     - "Kadets, Lopez, ..." should read Kadets, Lopez-Perez, Martin, Werner.

3. **Citations.**
   - Confirmed in this session (via sibling referees):
     - Kadets-Lopez-Perez-Martin-Werner, including the sentence on C_0(L);
     - Johnson-Wolfe 1979 (the paper);
     - Schachermayer, Pacific J. Math. 1983;
     - Choi-Song (quasi-alpha => A).
   - Not re-checkable here: the FBL-specific papers (Dantas et al. 2022, Bilokopytov et al. 2025, Aviles-Rodriguez-Tradacete 2018, Oikhberg-Taylor-Tradacete-Troitsky, arXiv 2505.24084, and others).
     - Their existence and main content agree with my memory, except for 2505.24084 and arXiv 2605.12117, which I do not know.
     - I found no sign of hallucination, but I cannot certify the snippet-level details ("Conjecture 5.5", "Lemma 5.8", property (P_p)).
   - The JSON's "confirmed_by_search: true" for these should be read as "per the explorer; not re-verified by the referee".

4. **New results in this report (all PROVED, Section 3).**
   - **R1 (main sharpening).** For 2 <= dim E < oo, B_{FBL[E]} is not the closed convex hull of its extreme points. Hence FBL[E] fails Lindenstrauss property A: for every strictly convex Z isomorphic to FBL[E], NA(FBL[E],Z) is not dense.
     - Consequently FBL[E] also fails quasi-alpha. This settles the point Remark 3.9 left unexamined; quasi-alpha => A is [S] via the sibling referee.
     - Alpha, RNP and reflexivity fail as well, re-proving Props 3.7 and 3.8.
     - So Theorem 5.2 is sharp: "compact T" (or dim Y < oo) cannot be dropped. Q6, second half, is answered negatively.
   - **R2.** An abstract form of Theorem 5.2: if a Banach lattice X is lattice isomorphic to some C(K) and every positive functional on X attains its norm, then the finite-rank NA operators are dense in K(X,Y) for every Y. This isolates exactly what the proof uses.
   - **R3.** For dim E = oo, FBL[E] has no strong unit, so it is not lattice isomorphic to any C(K) and R2 cannot apply.
   - **R4.** On FBL[l_2] there is a positive functional (an explicit Gaussian one) that does not attain its norm. Even for Hilbert E, the second hypothesis of R2 fails. By contrast, every lattice homomorphism on FBL[E] attains its norm when E is reflexive.
   - **R5.** Cor 4.2(b) holds for every E with 2 <= dim E < oo.

## 1. Re-derivation of the PROVED claims

### 1.1 Section 2 (any E): all CORRECT
- **Facts (i)-(iv).** Correct.
  - For (ii), use one-element admissible families.
  - For (iii), use positive homogeneity and the test functions delta_x.
- **Lemma 2.1.** Correct. Sum over i, then over k, using that (x_i^*) is admissible.
- **Lemma 2.2.** Correct. Two continuous lattice homomorphisms that agree on delta(F) agree on the closed sublattice FBL[F]. The set where they agree is a closed vector sublattice.
- **Lemma 2.3.** Correct.
  - Auerbach step: sum_i ||x_i^*|| <= sum_k sum_i |x_i^*(x_k)| <= d.
  - Two-point interpolation: if t = -s, then g = a(delta_x)^+ + b(delta_x)^- gives g(s) = a and g(-s) = b. If s, t are independent, delta_x does it directly.
  - The lattice Stone-Weierstrass theorem applies to vector sublattices with two-point interpolation.
  - The identification FBL[E] = C_ph(E^*) is KNOWN [M] (Aviles-Rodriguez-Tradacete, ART).
- **Lemma 2.4.** Correct.
  - (a) The p_i = (u_i(x), Theta(u_i)) are nonzero and pairwise non-positively-proportional because Theta is injective. G(p) = |p_0| gamma(p/|p|) is continuous at 0, positively homogeneous, |G| <= |p_0|, and Rbar(G) lies in FBL[E].
  - (b) "<=": rescale to the admissible family (|c_i| u_i / M). ">=": use (a) and Lemma 2.1.
  - (c) h_M = (g ^ M Pt^+) - (g ^ M Pt^-) satisfies |h_M| <= g because Pt^+ ^ Pt^- = 0. Its values are sign(c_i) g(u_i) for M large. Riesz-Kantorovich applies.
  - The hypothesis "u_i nonzero, pairwise non-positively-proportional" is necessary and is used.
- **Lemma 2.5.** Correct. Merging the families uses t delta_{x^*} = delta_{t x^*} for t >= 0, and the bipolar theorem.
- **Lemma 2.6.** Correct.
  - C0 is solid by the Riesz decomposition property and absorbing in FVL[E].
  - X_p is a Banach lattice and Q agrees with q on FVL[E]. This gives ||.|| = p on FVL[E].
  - The truncation estimate is |h - h_n| = (|h| - |delta_{x_n}|)^+ <= |delta_{x - x_n}|.
  - The statement is very likely KNOWN [M] ("closed solid convex hull of delta(B_E)").
  - I use one consequence of it, proved the same way: the positive part of the ball, B_+, equals cl conv U_x [0, |delta_x|]. Take positive parts of the approximants and apply Riesz decomposition to (sum a_j g_j)^+ <= sum a_j g_j^+.
- **Lemma 2.7.** Correct.
  - (b) psi vanishes on the ideal ker delta_{x^*}. The band generated by an atom is R delta_{x^*}, a projection band because FBL[E]^* is Dedekind complete.
  - (c) |a| + |b| = max(|a+b|, |a-b|). If delta_{v_n} -> delta_u with u != 0, then eventually v_n = t_n u with t_n -> 1.

### 1.2 Section 3 (dim E = d < oo): all CORRECT, one trivial omission
- **Prop 3.1.** Correct.
  - ">=": Lusin's theorem gives g; f(tu) = t g(u)|u(x)| is continuous and positively homogeneous with |f| <= |delta_x|. The error is <= 2 eps, because |u(x)| <= 1 on S x B_E.
  - "<=": discretize, using Lemma 2.4(b) for distinct u_j in S (which are pairwise non-positively-proportional) and N(nu_eta) <= N(nu) + eta ||nu||_TV.
  - N <= TV <= dN holds via the Auerbach system.
- **Prop 3.2 (zonoid formula).** Correct.
  - K = {h_rho|_S} is compact in C(S): continuity in rho is pointwise, the family is equicontinuous (1-Lipschitz in u), and Arzela-Ascoli applies.
  - In the separation step, finiteness forces nu >= 0, and then the supremum equals sup_{S_E} F_nu = N(nu).
- **Prop 3.3.** Correct.
  - Step 1 splits rho, which needs 0 < rho(B) < 1. If rho is a Dirac mass, Step 2's conclusion holds trivially; this is the omission noted in (E4).
  - Step 2: |u(x)| = h_rho(u) for rho-a.e. x and all u in Z (countable dense subset plus continuity). Z is a nonempty open cone covered by the two closed subspaces ker delta_{x - x'} and ker delta_{x + x'}, so one of them is all of E^*.
  - Step 3: the open half-spaces H+ and H- are connected, and the bump eta |delta_{x_0}| stays inside the ball by Lemma 2.1.
- **3.4 (a)-(c) and Lemma 3.5.** Correct.
  - Admissible families for E = R are those with sum |x_i^*| <= 1.
  - In Lemma 3.5, k(t) = ||u + w(t)|| - ||u - w(t)|| goes from 2 to -2. In the second case, ||u' +- w'|| = 2/c < sqrt 2.
- **Prop 3.6 (Hlawka).** Correct.
  - The four-case check in R is right.
  - The norms are nu(1,1) = c0 for x, y, z and x+y+z, and nu(2,0) = nu(0,2) = 2 for the pairwise sums.
  - So 4 c0 >= 6 would be needed, which is false since c0 <= sqrt 2.
  - The argument works for every E with dim E >= 2, including infinite dimensions.
- **Prop 3.7 (alpha fails).** Correct.
  - Alpha-points are exposed: x_l^*(y_n) <= |a_l| + r(1 - |a_l|), and the sign is forced, so a_l -> 1.
  - For phi = delta_u - delta_v: sup_{C0} phi <= ||u - v|| < ||u + v|| = ||phi||.
  - Section 3.1 strengthens this.
- **Prop 3.8.** Correct. ||iotabar g|| >= sup_{B_{F^*}} |g| >= ||g||/2 by Hahn-Banach and Lemma 2.3. It holds for every E with dim E >= 2.

### 1.3 Section 4: Theorem 4.1 CORRECT; Cor 4.2 (a), (c) CORRECT; (b) GAP (fixed by R5)

**Theorem 4.1, sufficiency.**
- A \ Z0 and B \ Z0 are disjoint, because A cap B = I(nu) is contained in Z0. They are relatively closed in the metric space S \ Z0, so Urysohn gives g.
- Put f(tu) = t g(u) |u(x_0)| off the cone over Z0, and f = 0 on that cone.
- f is continuous because |f(v)| <= |v(x_0)|. Lemma 2.1 gives ||f|| <= 1.
- Then int f dnu = F_nu(x_0) = N(nu).

**Theorem 4.1, necessity.**
- The chain is N(nu) = int f dnu <= int |f| d|nu| <= int h_rho d|nu| = int F_nu drho <= N(nu), using Fubini.
- Equality gives:
  - f = h_rho nu^+-a.e. and f = -h_rho nu^- -a.e.;
  - supp rho is contained in M_nu.
- The set {f = h_rho} is closed and has full nu^+-measure, so it contains supp nu^+. Similarly f = -h_rho on supp nu^-.
- Hence h_rho = 0 on I(nu). This makes every u in I(nu) vanish on supp rho, and any x_0 in supp rho (nonempty) works.

**Cor 4.2.**
- (a) For nu = sum a_l mu_l with mu_l carried by disjoint compact sets K_l: supp nu^+ is contained in the union of K_l over a_l > 0, and supp nu^- in the union over a_l < 0. These are disjoint.
- (c) The fat Cantor set C is chosen with lambda(C cap U) > 0 for every open U meeting C. Then I = C, which contains two independent points of the square's boundary, and no x_0 != 0 is annihilated by both.
  - The JSON labels the statement "NA(FBL(2),R) is a linear subspace" FALSE. That is consistent: the notes disprove it.
- (b) The example nu = lambda|_(0,pi/2) - lambda|_(pi/2,pi) on l_2^2 is correct: F_nu is identically 2, and x_0 = e_1 annihilates I(nu) = {pi/2}.
  - The claim "when dim E >= 2" is not proved for other E. See R5.

### 1.4 Lemma 5.1: CORRECT
- On the finite-dimensional W, the weak* and norm topologies coincide. So y^* -> ||S^* y^*|| is weak*-continuous on the weak*-compact B_{Y^*}.
- This is the localized form of Preprint B, Lemma densesubspace / KLMW. It is valid for every Y.

### 1.5 Theorem 5.2 (main): CORRECT, complete proof
Every step checks:
- T^* is compact, and N <= TV <= dN.
- T^* y_i^* = h_i mu with |h_i| <= 1.
- The partition into cubes of side < eps' gives oscillation < eps' on each A_l.
- Inner regularity gives mu(J) < eps.
- y_l := T^{**} 1_{K_l} lies in Y by Gantmacher. Here nu -> nu(K_l) is a bounded functional on (M(S), N), because |nu(K_l)| <= d N(nu).
- S^* y^* = E(T^* y^*), and E is a TV-contraction (sum_l |nu(K_l)| <= |nu|(S)).
- W = span{mu|_{K_l}} lies in NA by Cor 4.2(a), so Lemma 5.1 applies.
- The estimate is ||T - S|| <= (3 + d) eps.

Remarks:
- The FBL-specific input is exactly the pair "N is equivalent to TV" and "every positive nu attains its norm, at |delta_{x_0}|". R2 states this abstractly.
- Remark 5.3(3) is FALSE as a background statement (E2). Moreover R1 shows that non-compact T into infinite-dimensional Y can fail for FBL[E] itself.

### 1.6 Section 6: CORRECT
- **Prop 6.1.**
  - Weak*-density is equivalent to the span having trivial pre-annihilator.
  - For non-density, the test elements are f = Rbar(G) with:
    - G = 0 on the rays through the finitely many points P;
    - G = |v_1| + |v_2| off small angular sets;
    - ||f|| <= ||z_1|| + ||z_2||.
  - This gives a distance >= 4/(pi C) > 0, independent of psi.
  - Point evaluations f -> f(Q^* v) are continuous in v, so phi is well defined.
- **Prop 6.2.** Correct. NA(C(K),R) consists of exactly the measures with I(nu) = empty, and N is equivalent to TV.
- **Q3 (lineability) status.** The quoted KLMW sentence ("For C_0(L), we do not know whether ... NA(C_0(L)) contains a dense linear subspace") is confirmed [S] in this session (lipzero_referee.md C6; https://arxiv.org/pdf/1905.08272).

### 1.7 Section 7: CORRECT (one JSON overstatement, E3)
- **Prop 7.1.** Correct. The supremum over B_{Y^*} is attained because Y is finite-dimensional.
- **Cor 7.2.** Correct.
  - (a) R_T has finite rank and is weakly continuous on the weakly compact B_E.
  - (b) ||S^ delta_{x_0}|| = ||S x_0||.
- **Lemma 7.3 (pinning).** Correct, including the sign choice of y_1 that makes |t +- eps| = |t| + eps. The final inequality is Psi_T'(l) <= Psi_T'(l_0) - eps(1 - r)/2. The Lipschitz constant typo is noted in (E4).
- **Prop 7.4.** Correct.
  - sup{phi(g) : ||g||_F <= 1} = |phi|(F).
  - The convex-combination argument forces a_{l_0,n} -> 1, so f lies in the norm-closed interval [-F, F].
- **Cor 7.5.** Correct.
  - Merging an atom positively proportional to p is allowed; drop it if its coefficient becomes 0.
  - x -> ||R_T' x|| is an even continuous convex function. Its supremum over B_E = cl absconv{x_l} is attained at x_{l_0}.
- **Prop 7.6.** Correct under the stated hypothesis that K = Q(B_E) is closed.
  - The lifting uses J with QJ = id_F and Jy = x; then |Jbar g| <= |delta_x|.
  - The attainment points g_n = theta_n |delta_{y_n}| come from the proofs of Thm 5.2 and Cor 4.2(a).
  - Without closedness (e.g. E = c_0, Q = u in l_1 \ c_00) the proof does not apply, and the claim is unproved; see (E3).
- **Prop 7.7.**
  - (b) is correct: f_{n,k} = (|delta_{e_n}| - |delta_{e_k}|)^+ gives phi_oo(f_{n,k}) = 1, and Qbar f_{n,k} <= |delta_{Q(e_n - e_k)}|.
  - Addition (PROVED, same argument): the Gaussian functional phi_V of R4 is also at positive distance from all cylindrical functionals on FBL[l_2].
    - Take f = (|delta_{e_n}| - |delta_{e_k}|)^+ with ||Q(e_n - e_k)|| small.
    - phi_V(f) = E(|d_n g_n| - |d_k g_k|)^+, which stays bounded below as n, k -> oo.
- **Example 7.8.** Correct.
  - v - u has the tail -(u - P_n u), so it is not a positive multiple of u.
  - ||phi|| = max(||v||_1, ||2u - v||_1) = ||u||_1 + tau, attained at x_0 = sum_{i<=n} sign(v_i) e_i.
- **7.5 HEURISTIC.** Labelled correctly.
  - The representation (H1), phi = int h V^(.) dmu with V: E -> L_1(mu) and |h| = 1, is right. Proof: take the AL-space completion of FBL[E] / ker |phi|(|.|) and the lattice-homomorphism quotient q = V^.
  - It is also right that ||T|| = sup_{x in B_E} sup_{y^*} int |y^*(H)| |Vx| dmu.

### 1.8 Section 8: CORRECT
- **Prop 8.1.** Correct. Pi = delta o J^{-1} o P o J^ fixes delta(E) and has norm <= C.
  - That complemented subspaces of Banach lattices have Gordon-Lewis l.u.st. is KNOWN [M].
  - That S_p (p != 2) fails it is KNOWN [M].
- **Prop 8.2.** Correct.
- **Prop 8.3.**
  - (i) Every X embeds in C(B_{X^*}), and compact operators from C(K) are approximable (Johnson-Wolfe; domain C(K) [S] via lipzero_referee.md C2).
  - (ii) The example in l_oo^2 is correct: ||(1,0)|| = 1 but ||(1,-2)|| = 2.
  - (iii) and (iv) are correct.
- **"Universality not established".** Correct. Only "JW positive => FBL density" is available.

### 1.9 Section 9 (different notions): CORRECT as a classification
- The mechanism in Lemma 2.7(c) is PROVED.
- Non-attainment of delta_u on FBL[c_0] for u in l_1 \ c_00 rests on Dantas-Martinez-Cervantes-Rodriguez Abellan-Rueda Zoca (DMRR), which characterizes this for (preduals of) l_1. This is [M] here; the search budget was exhausted.
- Example 7.8 is a correct illustration that this failure concerns lattice homomorphisms only.

## 2. Citation check

Statuses:
- [S]: confirmed in this session, by a sibling referee's search hit.
- [M]: plausible from my memory; NOT re-verified by me.
- [U]: unverified, no memory.

| # | Reference (as cited) | Status | Notes |
|---|---|---|---|
| L1 | Dantas, Martinez-Cervantes, Rodriguez Abellan, Rueda Zoca, "Norm-attaining lattice homomorphisms", Rev. Mat. Iberoam. 38 (2022) 981-1002, arXiv 2007.14907 | [M] | My memory of the abstract matches the notes: a disjoint family of size 2^|A| in FBL(A)^* (de Pagter-Wickstead question); every lattice homomorphism on c_0, L_p, C(K) attains; first non-NA lattice homomorphisms, on FBL[E]; no Bishop-Phelps theorem. The numbering "Conjecture 5.5" and "Lemma 5.8" was not checked. |
| L2 | Bilokopytov, Garcia-Sanchez, de Hevia, Martinez-Cervantes, Tradacete, arXiv 2502.10165, J. Funct. Anal. (2025) | [M] (weak) | Existence and theme are plausible. The specific claims (AM-spaces; renormings of C(K); failure for FBL^(oo); unknown for p in [1,oo); the (P) gap and (P_p)) were not checked. |
| L3 | DMRR, "Octahedral norms in free Banach lattices", RACSAM 115 (2021), arXiv 2007.05288 | [M] | Peripheral. |
| L4 | Aviles, Rodriguez, Tradacete, "The free Banach lattice generated by a Banach space", J. Funct. Anal. 274 (2018), arXiv 1706.08147 | [M] (strong) | Construction, universal property, FBL(A) = FBL[l_1(A)], and the finite-dimensional C(S_{E^*}) identification. |
| L5 | Oikhberg, Taylor, Tradacete, Troitsky, "Free Banach lattices", arXiv 2210.00614; JEMS | [M] | The paper exists. The JEMS volume and pages and "Theorem 9.20" were not checked. |
| L6 | Aviles, Martinez-Cervantes, Rodriguez, Tradacete, "A Godefroy-Kalton principle for free Banach lattices", Israel J. Math. (2022), arXiv 2011.04639 | [M] | Not used in any proof. |
| L7 | "Complemented subspaces of Banach lattices", arXiv 2505.24084 | [U] | Authors missing. Nothing depends on it: Prop 8.1 is elementary and verified. |
| L8, L9 | Luiz-Miranda arXiv 2409.14625; Garcia-Luiz-Miranda arXiv 2605.12117 | [U] | Different notions; not used. |
| L10 | Kadets, Lopez-Perez, Martin, Werner, "Norm attaining operators of finite rank", in The Mathematical Legacy of Victor Lomonosov (De Gruyter 2020) 157-188, arXiv 1905.08272 | [S] | lipzero_referee.md C6 and sums_tensors_referee.md 2.4 (https://arxiv.org/pdf/1905.08272). The C_0(L) sentence is confirmed. The notes misspell the name as "Lopez". |
| L11 | Johnson, Wolfe, Studia Math. 65 (1979) 7-19 | [S] (paper) | https://eudml.org/doc/218261 (lipzero_referee.md C2). Per a snippet, compact operators are approximable when the domain is C(K), or the range is L_1 (real case) or an L_1-predual. "NA dense in L(C(K),C(S)), real case" is [M]. The "L_1-predual DOMAIN" version used in the task background was not confirmed (lipzero_referee.md D4); this is harmless, because FBL[E] is not an L_1-predual anyway (Prop 3.6). |
| L12 | Schachermayer, Pacific J. Math. 105 (1983) 427-438 | [S] | https://msp.org/pjm/1983/105-2/pjm-v105-n2-p13-s.pdf (lipzero_referee.md C4). |
| L13 | Gao-Lau constant, arXiv 2407.14475 | [M] | Needs a precise reference (see E4). Lemma 3.5 is re-proved and verified. |
| extra | Choi-Song, "Property (quasi-alpha) and the denseness of norm attaining mappings", Math. Nachr. 281 (2008) | [S] | https://oasis.postech.ac.kr/handle/2014.oak/22500 (sums_tensors_referee.md 2.3): quasi-alpha => property A. Used in R1. |
| extra | "C(K) fails property A for infinite metrizable K" | [S] | Via arXiv 1306.1155 (Martin, J. Funct. Anal. 2014), per lipzero_referee.md D8/C16. This contradicts Remark 5.3(3) (E2). |
| extra | Lindenstrauss 1963 (reflexive => A); Bourgain 1977 (RNP => A); Schachermayer 1983 (alpha => A) | [S] | lipzero_referee.md C1, C17; sums_tensors_referee.md line 305. |

Conclusion of Section 2:
- I found no hallucinated reference, but the FBL-specific literature (L1-L9) could not be re-verified in this turn.
- No proof in the notes depends on L1-L9. They are used only for:
  - context;
  - the "different notions" section;
  - the open status of Conjecture 5.5.

## 3. New results (all PROVED here)

### 3.1 R1: FBL[E] fails Lindenstrauss property A for 2 <= dim E < oo

**Lemma L (PROVED).** This is the classical extreme-point argument of Lindenstrauss 1963 [M].

*Statement.* Let X, Z be Banach spaces with Z strictly convex, and let J: X -> Z be an onto isomorphism. Suppose some x^* in S_{X^*} has
  kappa := sup{|x^*(e)| : e in ext B_X} < 1.
Then NA(X,Z) is not dense in L(X,Z). Equivalently: if NA(X,Z) is dense, then B_X = cl conv(ext B_X).

*Proof.*

Step 0 (injective operators attain at extreme points).
- Let T != 0 be injective and attain its norm at x_1 in S_X.
- Suppose x_1 = (y + y')/2 with y, y' in B_X. Then |Ty|, |Ty'| <= ||T|| = |(Ty + Ty')/2|.
- If Ty != Ty', strict convexity (when both norms equal ||T||) or the triangle inequality (otherwise) gives |(Ty + Ty')/2| < ||T||, a contradiction.
- So Ty = Ty', and injectivity gives y = y' = x_1. Thus x_1 is in ext B_X.

Step 1 (the test operator).
- Fix z_0 in S_Z and put w_0 = J^{-1} z_0.
- For delta > 0 with delta != -x^*(w_0), let T_0 := delta J + x^* (x) z_0 = delta J (I + delta^{-1} x^* (x) w_0).
- T_0 is an onto isomorphism: the second factor has inverse I - (delta + x^*(w_0))^{-1} x^* (x) w_0.
- Put m_0 := 1/||T_0^{-1}|| > 0. Then ||T_0|| >= sup_{B_X} (|x^*| - delta ||J||) = 1 - delta ||J||.

Step 2 (no norm-attaining operator near T_0).
- Choose delta so small that 1 - 2 delta (1 + ||J||) > kappa, and let r := min(m_0, delta).
- Suppose T is in NA(X,Z) with ||T - T_0|| < r. Then |Tx| >= (m_0 - r)||x||, so T is injective and nonzero.
- Let T attain its norm at x_1. By Step 0, x_1 is in ext B_X.
- Then
  |x^*(x_1)| >= |T_0 x_1| - delta ||J|| >= ||T|| - r - delta ||J|| >= ||T_0|| - 2r - delta ||J|| >= 1 - 2 delta (1 + ||J||) > kappa.
- This contradicts the definition of kappa.

Equivalence: the norming form follows from Hahn-Banach, since ext B_X is symmetric. QED

**Theorem PA (PROVED).** Let 2 <= dim E < oo and X = FBL[E].

(a) B_X != cl conv(ext B_X). Precisely, take u, v in S_{E^*} independent with ||u - v|| < ||u + v||, and phi = delta_u - delta_v. Then
  sup_{ext B_X} |phi| <= ||u - v|| < ||u + v|| = ||phi||.

(b) X has an equivalent strictly convex norm. For every strictly convex Z isomorphic to X, NA(X,Z) is not dense. So FBL[E] fails Lindenstrauss property A, while Theorem 5.2 shows that it has property A for compact operators.

(c) Each of the following implies property A, so FBL[E] has none of them: reflexivity (Lindenstrauss), RNP (Bourgain), property alpha (Schachermayer), quasi-alpha (Choi-Song). These implications are [S] via the sibling referees (Section 2).
- The criterion "B_X is the closed convex hull of a set of uniformly strongly exposed points" also fails, directly by (a): exposed points are extreme.
- Item (c) re-proves Props 3.7 and 3.8 and settles the quasi-alpha question that Remark 3.9 left open.

*Proof.*

(a)
- Prop 3.3 (verified) gives ext B_X contained in {+-delta_x, +-|delta_x| : x in S_E}.
- For x in S_E: |phi(+-delta_x)| = |(u - v)(x)| and |phi(+-|delta_x|)| = ||u(x)| - |v(x)|| <= |(u - v)(x)|.
- Lemma 2.7(c) gives ||phi|| = max(||u + v||, ||u - v||).
- Such u, v exist: take any u and an independent w, and set v = (u + tw)/||u + tw|| with t > 0 small.

(b)
- X is separable, since it is isomorphic to C(S_{E^*}) (Lemma 2.3).
- Let (phi_n) in B_{X^*} separate points, and put |f| := ||f|| + q(f) with q(f) = (sum_n 2^{-n} phi_n(f)^2)^{1/2} <= ||f||.
- q is the norm of an injective operator into l_2, hence Hilbertian.
- If |a| = |b| = |(a + b)/2| = 1, then q(a + b) = q(a) + q(b). So b = ta with t >= 0, and |b| = t|a| forces t = 1. Thus |.| is strictly convex.
- Apply Lemma L with x^* = phi/||phi|| and kappa <= ||u - v||/||u + v|| < 1.

(c) Immediate from (b). QED

**Remarks on R1.**
- The same proof shows that C(K) fails property A whenever K is a connected infinite compact metric space, since then ext B_{C(K)} = {+-1}. In particular C[0,1] fails A, so Remark 5.3(3) is wrong (E2).
- R1 answers the second half of Q6 negatively. For dim E < oo, NA(FBL[E],Y) can fail to be dense for non-compact operators into infinite-dimensional Y.
- So FBL(n), n >= 2, is a natural space with "property A for compact operators" (Theorem 5.2) but without property A.
- R1 has no bearing on finite-dimensional Y, and Johnson-Wolfe is untouched.
- For dim E = oo (with E separable), it is OPEN whether B_{FBL[E]} = cl conv(ext B_{FBL[E]}). If the equality fails, Lemma L gives failure of property A.
  - Prop 3.3 does not extend as it stands: in infinite dimensions the bump of Step 3 cannot be localized in norm by finitely many coordinates.

### 3.2 R2: abstract form of Theorem 5.2

**Proposition G (PROVED).**
- Hypotheses:
  - X is a Banach lattice and Phi: X -> C(K) is a lattice isomorphism onto, with a ||Phi x||_oo <= ||x|| <= b ||Phi x||_oo;
  - every positive functional on X attains its norm.
- Conclusion: for every Banach space Y, every compact T: X -> Y is a norm limit of finite-rank operators in NA(X,Y).

*Proof.*

Setup.
- Identify X^* with M(K) via nu -> nu o Phi, a lattice isomorphism.
- Put N(nu) := ||nu o Phi||. Then ||nu||_TV / b <= N(nu) <= ||nu||_TV / a, because Phi(B_X) contains the sup-ball of radius 1/b and lies in the sup-ball of radius 1/a.

(i) Disjointly supported elements attain their norm.
- Let mu_l >= 0 be carried by pairwise disjoint compact sets K_l, and nu = sum_l c_l mu_l.
- The positive functional |nu| o Phi = |nu o Phi| attains its norm at some x_0 in B_X. We may take x_0 >= 0: replacing x_0 by |x_0| does not decrease the value.
- Let g = Phi x_0 >= 0. Let sigma in C(K) satisfy |sigma| <= 1 and sigma = sign(c_l) on K_l (Urysohn).
- Put h := Phi^{-1}(sigma g). Since |h| = Phi^{-1}(|sigma| g) <= x_0, we have ||h|| <= 1.
- Then
  nu(Phi h) = sum_l |c_l| int g dmu_l = |nu|(g) = || |nu| o Phi || = ||nu o Phi||.
  The last equality holds because the dual norm is a lattice norm.

(ii) The approximation.
- Repeat the proof of Theorem 5.2 verbatim, with N in place of the FBL dual norm.
- S^* y^* = E(T^* y^*) lies in span{mu|_{K_l}}, which is contained in NA by (i). Lemma 5.1 then gives S in NA.
- The estimate becomes ||T - S|| <= eps + 2 eps/a + b eps/a. QED

**Application to FBL[E], dim E = d.**
- Here Phi = restriction to S, with a = 1 and b = d (Lemma 2.3).
- A positive nu attains its norm at |delta_{x_0}|, where x_0 maximizes F_nu.
- So Theorem 5.2 is exactly the case X = FBL[E].
- The second hypothesis is not automatic for equivalent lattice norms on C(K). Lattice homomorphisms are positive, and Bilokopytov et al. [M] renorm every infinite-dimensional C(K) so that some lattice homomorphism does not attain its norm.

### 3.3 R3: for dim E = oo, FBL[E] has no strong unit

**Proposition SU (PROVED).** If dim E = oo, no e >= 0 in FBL[E] satisfies FBL[E] = U_n [-ne, ne]. Hence FBL[E] is not lattice isomorphic to any C(K), and Proposition G cannot apply.

*Proof.*

Step 1 (equivalence of norms).
- Suppose e is a strong unit, and let ||f||_e := inf{c : |f| <= ce}.
- ||.||_e is complete:
  - ||f|| <= ||e|| ||f||_e, so an ||.||_e-Cauchy sequence f_n converges in norm to some f;
  - letting m -> oo in |f_n - f_m| <= eps e gives |f_n - f| <= eps e, because order intervals are norm-closed.
- By the open mapping theorem, ||f||_e <= C ||f||.

Step 2 (a lower bound for e).
- From |delta_x| <= C ||x|| e pointwise on E^*, we get |u(x)| <= C ||x|| e(u).
- Taking the sup over x in B_E gives ||u|| <= C e(u) for every u in E^*.

Step 3 (contradiction).
- Every element of FBL[E] is weak*-continuous on B_{E^*}:
  - this holds for delta_x;
  - it is preserved by lattice-linear operations;
  - it passes to FBL-norm limits, which are uniform on B_{E^*} by fact (ii).
- Since dim E = oo, each basic weak*-neighbourhood {u : |u(x_j)| < eta, j <= m} contains the nonzero subspace intersect_j ker delta_{x_j} of E^*, hence a point of S_{E^*}.
- So some net u_alpha in S_{E^*} tends weak* to 0, and e(u_alpha) -> e(0) = 0. This contradicts e(u_alpha) >= 1/C.

Last claim: a lattice isomorphism onto C(K) maps the preimage of 1 to a strong unit. QED

### 3.4 R4: a positive functional on FBL[l_2] that does not attain its norm

**Proposition PF (PROVED).**

*Setup.*
- E = l_2. (g_n) are i.i.d. N(0,1) on (Omega, P). d_n = 1 - 1/(n+1), D = diag(d_n), and c = E|g_1| = sqrt(2/pi).
- Vx := sum_n d_n x_n g_n, with the series converging in L_2(P). Since Vx ~ N(0, ||Dx||_2^2), we have ||Vx||_{L_1} = c ||Dx||_2.
- V^ : FBL[l_2] -> L_1(P) is the lattice homomorphism extending V, from the universal property.
- phi := E o V^.

*Claim.* phi >= 0 and ||phi|| = c, and phi attains its norm at no f in B_{FBL[l_2]}.

*Proof.*

Step 1 (the norm).
- phi(|delta_x|) = E|Vx| = c ||Dx||_2.
- By Lemma 2.6, ||phi|| = sup_{x in B_E} phi(|delta_x|) = c sup_n d_n = c.

Step 2 (reduction to an approximating sequence).
- Let ||f|| <= 1 with phi(f) = c. Since phi(|f|) >= phi(f), we may assume f >= 0.
- By the positive form of Lemma 2.6 (see 1.1), there are h_n = sum_j a_{j,n} g_{j,n} -> f in norm, where:
  - a_{j,n} >= 0 and sum_j a_{j,n} = 1;
  - 0 <= g_{j,n} <= |delta_{x_{j,n}}| with ||x_{j,n}|| <= 1.
- phi(h_n) <= c sum_j a_{j,n} ||D x_{j,n}||, and phi(h_n) -> c. Hence
  eps_n := sum_j a_{j,n} (1 - ||D x_{j,n}||) -> 0.

Step 3 (norming points escape to infinity).
- For ||x|| <= 1 and every N:
  ||Dx||^2 <= d_N^2 ||P_N x||^2 + ||x - P_N x||^2 <= 1 - (1 - d_N^2) ||P_N x||^2.
- Hence ||P_N x||^2 <= 2(1 - ||Dx||)/(1 - d_N^2).

Step 4 (f vanishes everywhere).
- Fix u in l_2 = E^*. Point evaluation is continuous (fact (ii)), so f(u) = lim h_n(u).
- By Jensen's inequality,
  0 <= h_n(u) <= sum_j a_{j,n} |<x_{j,n}, u>| <= ||u - P_N u|| + ||u|| (2/(1 - d_N^2))^{1/2} eps_n^{1/2}.
- Let n -> oo, then N -> oo: f(u) = 0.
- So f = 0, contradicting phi(f) = c > 0. QED

**Remarks on R4.**
- For reflexive E, every lattice homomorphism delta_{x^*} attains its norm: if x^* attains at x_0, then delta_{x^*} attains at delta_{x_0}. R4 shows that the positive cone of the dual behaves differently.
- The automatic step "|nu| attains its norm" in Cor 4.2(a) and Prop G therefore fails for infinite-dimensional reflexive E.
- Any extension of Theorem 5.2 must choose its positive components carefully. Perturbing V itself is useless, by the same mechanism as Lemma 2.7(c).
- A possible repair (HEURISTIC): let phi_A := E[1_A V^(.)].
  - PROVED part: ||phi - phi_A|| = sup_x E[1_{A^c} |Vx|] <= P(A^c)^{1/2}.
  - HEURISTIC part: a two-dimensional Gaussian computation suggests that A^c = {|g_N| <= 2/(N+1)} makes phi_A attain its norm at |delta_{e_N}|. This was not checked in detail.
- Whether such mass removal works uniformly for several functionals at once is exactly the open problem Q1.

### 3.5 R5: Cor 4.2(b) holds for every E with 2 <= dim E < oo

**Classical planar facts used, KNOWN [M].**
- (Z1) Every centrally symmetric planar convex body Z is a zonoid: h_Z(p) = int |<theta, p>| dtau(theta) for an even positive measure tau.
- (Z2) For such Z, 4 tau, rotated by pi/2, equals the length measure of the boundary of Z indexed by outer normal angle. This follows from h'' + h = S_Z together with (|cos|)'' + |cos| = 2(delta_{pi/2} + delta_{-pi/2}).

**Proposition (PROVED modulo Z1-Z2).** For every E with 2 <= dim E < oo there is nu in M(S_{E^*}) such that:
- I(nu) != empty, so nu does not attain its C(S)^*-norm;
- nu attains its FBL[E]^*-norm.

*Proof.*

Step 1 (choice of x_0, w, u_0, D).
- Let x_0 be an exposed point of B_E, exposed by w in S_{E^*}; exposed points exist in finite dimensions. So w(x) = 1 with x in B_E forces x = x_0.
- Take u_0 in S_{E^*} with u_0(x_0) = 0, and let G = span{w, u_0}.
- Use coordinates z = s w + t u_0 on G, with the Euclidean structure that makes (w, u_0) orthonormal.
- Put D = B_{E^*} cap G.

Step 2 (D is smooth at w).
- Every functional on G is z -> z(y) for some y in E, and sup_D z(y) = ||Qy||, where Q: E -> E/G_perp is the quotient map and Q(B_E) is closed.
- Suppose z -> z(y) supports D at w, i.e. w(y) = ||Qy||. Pick y' with Qy' = Qy and ||y'|| = ||Qy||. Then w attains its norm at y'/||y'||, which must be x_0.
- So the support line at w is unique: it is {s = 1}, the line for evaluation at x_0.
- Consequently, near w the boundary of D is the graph s = 1 - phi_D(t), with phi_D convex, phi_D >= 0, phi_D(0) = 0 and phi_D'(0) = 0.

Step 3 (the body Z).
- Let Z := D cap {|s| <= 1 - gamma t^2} with gamma > 0. Both sets are convex and symmetric, w lies on the boundary of Z, and Z is contained in D.
- Near w, the boundary of Z is s = 1 - psi(t), with psi = max(phi_D, gamma t^2). Here psi(0) = psi'(0) = 0 and psi(t) > 0 for t != 0.
- So the outer normal angle arctan psi'(t) is > 0 for t > 0 and < 0 for t < 0, and tends to 0 as t -> 0.
- Hence, for every eta > 0, the boundary length of Z charges normal angles in (0, eta) and in (-eta, 0).

Step 4 (the measure nu).
- By (Z1) and (Z2), h_Z(y) := max_{z in Z} z(y) = int |theta(y)| dtau(theta), and tau charges directions on both sides of u_0 (angle pi/2) in every neighbourhood.
- Push tau radially onto the sphere S_{E^*} cap G, with density ||theta||. Fold it onto the angles (0, pi], using evenness. This gives tau' >= 0 with int |u(y)| dtau'(u) = h_Z(y).
- Put nu := tau'|_(0, pi/2] - tau'|_(pi/2, pi].
- Then supp nu^+ lies in the arc [0, pi/2] and supp nu^- in the arc [pi/2, pi]. The endpoints 0 and pi correspond to the distinct points w and -w. So I(nu) = {u_0}.

Step 5 (norm attainment).
- |nu| = tau', so F_nu = h_Z <= max_{z in D} z(.) <= ||.||, i.e. N(nu) <= 1.
- F_nu(x_0) >= w(x_0) = 1, so x_0 is in M_nu, and u_0(x_0) = 0.
- Theorem 4.1 applies. QED

## 4. Verdict, required fixes, remaining open problems

**Corrected verdict: OPEN.** It agrees with the explorer.

What is settled:
- PROVED (verified): NA(FBL[E],Y) is dense for every finite-dimensional Y when dim E < oo. In fact finite-rank norm-attaining operators are dense in K(FBL[E],Y) for every Y.
- New (R1): this cannot be extended to all operators. For 2 <= dim E < oo, FBL[E] fails property A.

What is open:
- For dim E = oo, density for finite-dimensional Y is OPEN.
- No transfer to Johnson-Wolfe is known in either direction beyond the trivial one, so EQUIVALENT_TO_JOHNSON_WOLFE is not justified.
- No counterexample is claimed, and none should be expected.

**Required fixes to the notes and JSON.**
1. Cor 4.2(b): add R5, or restrict the claim to l_2^2.
2. Remark 5.3(3): delete "not settled". C[0,1] fails A (classical; [S] via the sibling referee). Add R1.
3. JSON "Props 7.1-7.7": add "Q(B_E) closed" to the claim about cylindrical operators.
4. Remark 3.9 and Q6: quasi-alpha fails, and property A fails (R1). Q6 for non-compact T is answered negatively.
5. Citations:
   - give the authors of arXiv 2505.24084;
   - correct the spelling Lopez-Perez;
   - give the Gao-Lau journal reference;
   - mark the FBL-specific "confirmed_by_search" entries as not re-verified by the referee.
6. Cosmetic: Lipschitz constant ||T|| ||g|| in 7.2; the Dirac case in Prop 3.3; the wording "non-positively-proportional" in the JSON.

**Remaining open problems (sharpened).**
- Q1. Is NA(FBL[E],Y) dense for finite-dimensional Y when dim E = oo? Test cases: FBL(N), FBL[c_0], FBL[l_2].
  - By R3, Prop G cannot be used, since there is no strong unit.
  - By R4, even for E = l_2 the positive components must be chosen carefully.
  - By Lemma 2.7(c) and 1.7, only multiplicative (TV-type) perturbations of the AL-representation (H1) are cheap.
- Q1'. For separable infinite-dimensional E with dim E >= 2: is B_{FBL[E]} = cl conv(ext B_{FBL[E]})? If not, FBL[E] fails property A by Lemma L.
- Q3. Lineability for FBL(2): open. Prop 6.2 reduces it to C(S^1), and that case is open per KLMW [S].
- Q4. The vector form of Conjecture 5.5: open (not checked further).
- Q5. Transfer and universality: open.
