# lipzero -- referee report on lipzero_notes.md

Key: lipzero. Adversarial referee (workflow subagent), 2026-10-30. Real scalars.
Notation as in the notes:
- P(X): NA(X,F) is dense in L(X,F) for every finite-dimensional F.
- (LL): local lineability. (DL): dense lineability.
- AA(X,F) = {S : S^*(F^*) is contained in NA(X,R)}.

Labels: PROVED / KNOWN / SKETCH / HEURISTIC / OPEN / FALSE.
Citation statuses: confirmed (search hit, URL given), not_found, misattributed_or_misstated, from_memory_plausible.

Method and limits:
- Every item labelled PROVED was re-derived by hand.
- Citations were checked with WebSearch. Only snippets were available, no full texts.
- The session's search budget ran out at the end. Two planned searches on the novelty of Thm 3.9 could not be run, so its novelty stays uncertified.

## 0. Bottom line

VERDICT: OPEN. This confirms the explorer's verdict; it is neither overclaimed nor underclaimed.
- It is unknown whether NA(Lip_0(M),Y) is dense for every M and every finite-dimensional Y, and the notes do not prove it.
- Only "JW positive => statement" is known, and it is trivial.
- No counterexample is claimed. One would refute the Johnson-Wolfe (JW) problem.

All items labelled PROVED were re-derived, and all are mathematically correct. Three results deserve special mention:
- **Thm 3.9** (the new theorem): weak*-closed finite-codimensional subspaces of L_oo(mu) have (LL). It survives a line-by-line check. The check covered:
  - the order of quantifiers: the cushions are fixed before eta, and only the level n_k is chosen after eta;
  - the case c_k = 0;
  - the null set where a cushion is infinite;
  - the passage from a.e. signs to pointwise signs through the Stone space.
- **Cor 3.10** is correct: P(Lip_0(G)) for connected metric graphs with finite first Betti number, e.g. the circle.
- **Prop 3.11** is correct: if G has a cycle, Lip_0(G)^* is not an L-space, so JW does not apply.

### Defects

None of these changes the verdict.

**D1. WRONG as stated.** Summary item (4) claims these are "the first INFINITE non-tree-like M we know of with P(Lip_0(M))".
- Counterexample: M = C_4 v [0,1], a 4-cycle wedged with a segment. It is infinite and violates the four-point condition.
- P(Lip_0(M)) follows from the notes' own Cor 3.4(ii) (see R4 in Section 6).
- Correct claim: the circle and finite graphs with a cycle are, as far as we know, the first CONNECTED non-tree-like M.

**D2. UNSUPPORTED.** (N3) says "for Lip_0([0,1]) = L_oo[0,1] density can fail for some infinite-dimensional range".
- The quoted failure of property A is for C(K) with K infinite and METRIZABLE.
- L_oo[0,1] = C(K) with K hyperstonean, which is not metrizable.
- No Lip_0(M) with M infinite is a C(K) with K metrizable, since it contains a complemented l_oo (CDW).
- The referee does not know whether L_oo[0,1], or any Lip_0(M) with M infinite, fails property A. The claim should be deleted or marked OPEN.
- "P is strictly weaker than property A" remains true: C[0,1] and c_0 have P and fail A.

**D3. MISSTATED CITATION.** The JSON says "Johnson-Wolfe 1979: norm-attaining operators are dense for real C(K) domains".
- JW's theorem is about COMPACT operators: the domain is C(K), or the range is L_1 or an L_1-predual.
- For all ranges, the JSON wording would say that C(K) has property A. The notes' own (N3) says this is false for infinite metrizable K.
- The misstatement is harmless for finite-dimensional Y.

**D4. UNCONFIRMED.** The notes quote "JW for L_1-predual DOMAINS".
- The only secondary source found puts L_1-preduals on the RANGE side, so this may be a swap of domain and range.
- The statement is not used anywhere, because Thm 3.5 is self-contained.

**D5. LABEL.** The "Consequence" of Prop 3.2 (Lindenstrauss' biadjoint theorem "does not decide P") is not a theorem.
- It is a remark about one proof strategy and should be labelled HEURISTIC.
- The equivalence "T** = T o pi <=> T weak*-continuous" is correct and PROVED.

**D6. MISSING CITATION.** Example 3.6(b) ("the dual of l_oo(H) is not an L-space") needs Grothendieck's theorem: 1-complemented subspaces of L_1 spaces are L_1 spaces. The complemented copy is H^*, which happens to be isometric to H.

**D7. REMOVABLE HYPOTHESES.** The following can be dropped (see R2 in Section 6):
- sigma-finiteness in Thm 3.9;
- "countable edge set" and "d assumed to be a metric" in Cor 3.10.

**D8. CITATION DETAIL.** arXiv 2110.02066 exists (Dantas-Falco-Jung, on group-invariant operators), but the referee could not see the quoted sentence in it.
- The statement "C(K) fails property A for infinite metrizable K" is confirmed through arXiv 1306.1155 instead.
- The attribution to Lindenstrauss is not confirmed.

### New results added by the referee

All are PROVED in Section 6.
- **R1.** C(K,E) has (LL) for every compact Hausdorff K and every finite-dimensional E.
  - This upgrades "infinite wedge of copies of one finite pointed metric space" from SKETCH (in the notes) to PROVED.
  - It covers the infinite wedge of equilateral triangles, where Lip_0 = l_oo(H) and JW does not apply.
- **R2.** Thm 3.9 holds for arbitrary measures. Cor 3.10 holds for every connected metric graph with finite first Betti number.
- **R3 (corona reduction).** l_oo(Gamma; X_gamma) has (LL) if and only if every X_gamma has (LL) and the corona l_oo/c_0 has (LL).
  - Every infinite bouquet of circles with the wedge metric has Lip_0 isometric to l_oo(Gamma; X_1), where X_1 = {h in L_oo[0,1] : int h = 0}, whatever the lengths. This includes the Hawaiian earring with its intrinsic metric.
  - So (LL) for all countable bouquets is one question about one corona space.
- **R4.** The explicit counterexample to D1.

## 1. Section 1 of the notes

**Lemma 1.1 (adjoint criterion): correct.**
- Both directions checked. T = 0 is trivial.
- Maximizers of y^* -> ||T^* y^*|| exist because S_{Y^*} is compact.

**Lemma 1.2: correct.**
- (a) is trivial.
- (b) "=>": S^* y^* = sum_i y^*(y_i) psi_i lies in span{psi_i}.
- (b) "<=": take F = l_oo^d. Since ||e_i^*||_{l_1^d} = 1, we get ||psi_i - phi_i|| <= ||S - T||, and span{psi_i} = S^*(F^*).
- (c): a maximizer y_0^* of ||S^* y^*|| on S_{F^*} has ||S^* y_0^*|| = ||S||; then apply Lemma 1.1.
- Linear dependence among the phi_i does no harm.

**Remark 1.3: correct, modulo two KNOWN inputs.**
- Small perturbations of independent phi_1, phi_2 stay independent. So (LL) with d = 2 would put a 2-dimensional subspace inside NA(R,R), contradicting Rmoutil (confirmed).
- P(R) follows from Preprint B, Theorem read-finite-density: the closure of the norm-attaining finite-rank operators is K(R,F). For finite-dimensional F, L(R,F) = K(R,F).
- Checked against the provided tex: the abstract and the theorem statement match.

**Remark 1.4: correct.** NA(c_0,R) = c_00 is a dense subspace of l_1.

## 2. Sections 3.1-3.4 of the notes

**Prop 3.1: correct.**
- (a) B_X is weak*-compact and x -> ||Sx|| is weak*-continuous. A maximizer of norm < 1 can be rescaled when S != 0.
- (b) S = sum phi_i (x) y_i is weak*-to-norm continuous iff each phi_i is weak*-continuous, iff phi_i is in J_Z(Z).
- (c) W is norm closed because J_Z(Z) is. If W = L(X,Y), rank-one operators phi (x) y force Z** = J_Z(Z).
- (d) For finite M, F(M) is finite-dimensional. For infinite M, CDW (confirmed) gives a complemented copy of l_1 in F(M), so F(M) is not reflexive.

**Prop 3.2: the equivalence is correct; the "Consequence" is HEURISTIC (D5).**
- Checked: T**(Xi) = sum_i Xi(phi_i) y_i.
- If phi_i = J_Z z_i, then phi_i(pi Xi) = Xi(J_Z z_i).
- Conversely, Xi in (J_Z Z)^perp gives pi Xi = 0, hence Xi(phi_i) = 0. By Hahn-Banach, phi_i lies in the norm closure of J_Z Z, which is J_Z Z.
- Why the consequence is not a theorem: a T whose biadjoint attains its norm at some Xi may still attain its own norm elsewhere, and nothing in the argument excludes this.
- Suggested wording: "the direct transfer of Lindenstrauss' theorem works only for weak*-continuous T".

**Prop 3.3 (wedge): correct.**
- The triangle inequality was checked in all five placements of x, y, z:
  - all three points in one piece;
  - two points in one piece and the middle point elsewhere;
  - end points in different pieces;
  - all three in different pieces.
- R is isometric (cross pairs go through 0) and onto (by gluing).
- R is a homeomorphism for pointwise convergence on bounded sets. The l_1-sum of the F(M_i) is therefore the predual (Krein-Smulian / Banach-Dieudonne).

**Cor 3.4: (i), (ii) correct; (iii) not re-checked; (iv) correctly OPEN.**
- (i) Re-derived:
  - ||S_W|| <= ||S - T|| < eps, because T(0,w) = 0.
  - c = ||x_1|| >= 1 - eps/||S|| > (1-2eps)/(1-eps) >= 2/3 for eps < 1/4.
  - ||Eu|| <= ||u||/c and E(x_1/c) = x/c, so R = S o E attains its norm at x_1/c.
  - ||R - S_1|| <= ||S_W||/c, hence ||R - T_1|| < eps/c + eps < 3 eps.
  - The argument works for ANY second summand W.
- (ii) (X_1 (+)_oo X_2)^* = X_1^* (+)_1 X_2^*. A functional whose two components attain at z_1 and z_2 attains at (z_1, z_2).
- (iii) is an internal reference (sums_tensors Prop 6) and was not re-checked here.
- (iv) is correctly labelled OPEN.

**Lemma 3.5a: correct (standard).** It uses three facts:
- the complement of the support of a Radon measure is null (inner regularity on open sets);
- Urysohn's lemma;
- {f = 1} is closed and has full mu^+-measure.

**Theorem 3.5 (C(K) has (LL)): correct.**
- rho = sum |mu_i| is a finite Radon measure, and |h_i| <= 1.
- A common partition is used. Inner regularity of finite Radon measures on Borel sets follows from outer regularity.
- The approximation bound holds:
  sum_i ||psi_i - mu_i|| <= sum_i int |h_i - sum_j c_ij 1_{A_j}| drho + sum_{i,j} |c_ij| rho(A_j \ K_j) < 2 eps.
- The nu_j have disjoint supports, so ||sum_j a_j nu_j|| = sum_j |a_j| rho(K_j).
- sign(a_j) on the disjoint compacta extends by Tietze (truncated to [-1,1]).
- No metrizability is used.
- Remark 3.5b is correct once the nu_j = 0 are discarded.

**Example 3.6: correct; the tested claim is FALSE.**
- The unit ball {|x|, |y|, |x - y| <= 2} has the six listed vertices. A hexagon is not a parallelogram, so Lip_0(M) is not l_oo^2.
- Hence F(M) is not l_1^2, the only 2-dimensional L_1(mu).
- M is ultrametric, so this is also an instance of DKP.
- Consequence (b) needs the fix D6:
  - X = l_oo(H) contains H^* 1-complemented in X^*: P_1^* is an isometric embedding with left inverse iota_1^*.
  - If X^* were an L_1(nu), Grothendieck's theorem would make H^* an L_1-space, i.e. l_1^2. But H^* is hexagonal.
  - The hexagon is affinely regular: v_1 = (2,2), v_2 = (2,0), v_3 = (0,-2) satisfy v_2 = v_1 + v_3. So H^* is isometric to H, and the notes' "contains H" is also right.
- The SKETCH "P(l_oo(H))" is now PROVED (R1).

**Prop 3.7: correct, modulo KNOWN results.**
- (a) L_1(mu) is an AL-space for every mu. Its dual is an AM-space with unit e(x) = ||x^+|| - ||x^-|| (linear because the norm is additive on the positive cone). Then Kakutani's theorem.
- (b) The canonical map F(M) -> F(M)** = Lip_0(M)^* is isometric.
- Godard's characterization covers non-sigma-finite nu. DKP state it for subspaces of SOME L_1(mu): "M is 0-hyperbolic iff F(M) is isometric to a subspace of some L_1(mu)" (snippet).

**Prop 3.8 (closed M in R): correct.**
- Interpolation keeps the Lipschitz constant; the three-piece estimate was checked.
- ||Phi f||_{L_oo(nu)} = max(ess sup_M |F'|, sup_g |slope_g|) = ess sup_R |F'| = L(f). Unbounded gaps contribute 0.
- Onto: take H constant on gaps and F(x) = int_0^x H.
- The point masses p_g lie outside M, so L_oo(nu) = L_oo(lambda|_M) (+)_oo l_oo(G).
- The degenerate cases are covered: M discrete, lambda(M) = 0, and M = R.

## 3. Sections 3.5-3.6 of the notes (the new results)

**Facts K1, K2 and C1-C3: correct.**
- C1 uses only that J is an injective unital algebra homomorphism.
- C3:
  - ||m_g|| = ||g||_1 by L_1-L_oo duality.
  - m_g << lambda: first for bounded g >= 0 (positivity of J^{-1}), then in general because the lambda-continuous measures form a norm-closed set.
  - m_{1_A} = 1_{A~} lambda.
  - Indicators of clopen sets are dense in L_1(lambda) because K is zero-dimensional: a compact C inside an open U is covered by a clopen D with C in D in U.

**Theorem 3.9: CORRECT.** Step-by-step re-derivation:
- **Step 0.** mu' = w_0 mu has the same null sets, and int h g dmu = int h (g/w_0) dmu' with g/w_0 in L_1(mu'). Removing dependent g_l does not change X.
- **Step 0'.**
  - X = (span{m_{g_l}})_perp.
  - Its annihilator is the weak*-closure of a finite-dimensional space, i.e. span{m_{g_l}} itself.
  - Hahn-Banach gives ||Psi|_X|| = dist(Psi, X^perp), and the distance is attained (finite dimension).
- **Steps 1-2.**
  - Lebesgue decomposition of the Radon measures Phi_i with respect to lambda; C3 identifies the absolutely continuous parts with m_{a_i}.
  - One lambda-null Borel set N (the union of the N_i) carries all sigma_i.
  - The partition sets are intersected with N before compacta are taken. Hence K_k lies inside N, lambda(K_k) = 0, and m_w(K_k) = 0 (since m_w << lambda).
- **Step 3.**
  - In a compact zero-dimensional space, disjoint compacta have disjoint clopen neighbourhoods (induction on k).
  - Outer regularity of the positive Radon measure m_w gives nested clopen D_k^(n) with m_w(D_k^(n)) <= 8^-n.
  - A -> A~ is a Boolean isomorphism, so after removing a null set the E_k^(n) are exactly nested in n and disjoint in k.
  - mu(intersection over n of E_k^(n)) <= int_{E_k^(n)} w <= 8^-n (as w >= 1). So the set where chi_k = +oo is null, chi_k is in L_1, and ||chi_k||_1 <= theta sum_n 4^-n = theta/3.
- **Step 5.** ||Psi_i - Phi_i|| <= sum_k |d_ik| theta/3 + ||sigma_i - sum_k d_ik nu_k||, and restriction to X is contractive. Correct.
- **Step 6 (the heart).** Quantifiers: the cushions are fixed BEFORE eta; only the level n_k is chosen after eta and after the minimizer t*.
  - (6a) The norms add: m_{u - sum t g} is lambda-continuous, and sum_k c_k nu_k lives on the lambda-null union of the disjoint K_k. Coercivity uses the independence of the g_l.
  - (6b) Since mu is finite, L_1^* = L_oo, and dist(u,G) in L_1 is a maximum over the weak*-compact set B_{G^perp}. The maximizer h_0 lies in B_X, and int r h_0 = int u h_0 = ||r||_1 forces h_0 = sign r a.e. on {r != 0}.
  - (6c) On E_k^(n) the other cushions vanish: E_k^(n) lies inside D_k^(0) = O_k, which is disjoint from O_k' for k' != k.
    - By the choice of w: |a_eta| <= |eta|_oo w and |sum_l t*_l g_l| <= |t*|_oo w.
    - On E_k^(n): chi_k >= theta 2^n w.
    - Take n_k with |c_k| theta 2^{n_k} > |eta|_oo + |t*|_oo. Since w >= 1 > 0, the strict inequality holds pointwise, so sign r = sign c_k a.e. on E_k^(n_k), hence h_0 = sign c_k a.e. there.
    - C1 then gives J h_0 = sign c_k on the clopen set D_k^(n_k), which contains K_k.
    - For c_k = 0 nothing is needed.
  - (6d) psi_eta(h_0) = int u h_0 + sum_k c_k int J h_0 dnu_k = ||r||_1 + sum_k |c_k| ||nu_k|| = ||psi_eta||. If psi_eta != 0, this forces ||h_0|| = 1.
- No gap was found.
- What the proof really uses, correctly identified in Remark 3.9a(iii):
  - the finite dimension of span{g_l}, which gives the attained minimum and the pointwise domination by w;
  - the Stone representation, which turns a.e. sign information on E_k^(n) into pointwise information on a clopen neighbourhood of the singular support.

**Remark 3.9a: correct.** Item (ii) recomputed with lambda(A) = 3/5:
- min_t [(3/5)|5/3 - t| + (2/5)|t|] = 2/3, attained at t = 5/3. So ||psi|| = 2/3 + 1 = 5/3.
- For h in B_X: (5/3) int_A h = -(5/3) int_{A^c} h <= 2/3, with equality only if h = -1 a.e. on A^c.
- In that case C1 gives nu(h) = -1. So psi(h) < 5/3 for every h in B_X, and psi does not attain its norm.

**Cor 3.10: correct; the hypotheses can be weakened (R2).**
- s -> f(e(s)) is L(f)-Lipschitz because d(e(s), e(s')) <= |s - s'|. Edges need not be isometric; loops and multiple edges are fine.
- The fundamental theorem of calculus holds along edge paths.
- int_Z h = 0 on the fundamental cycles implies int_gamma h = 0 for every closed edge path, whose chain is an integer combination of fundamental cycles.
- So f is well defined, and taking the infimum over paths gives L(f) <= ||h||_oo.
- Phi(f) = h by differentiation along edges. Phi is an onto linear isometry.

**Prop 3.11: correct, modulo KNOWN results** (the four-point characterization of subsets of R-trees, confirmed; Godard).
- The shortest simple cycle Z is isometrically a circle. For a path gamma from x to y, c = [gamma] + [beta] (mod 2) is a Z_2-cycle:
  - If c != 0, its support contains a simple cycle of length >= L_0. Hence length(gamma) + length(beta) >= L_0 = length(alpha) + length(beta).
  - If c = 0, gamma covers beta.
- Four points at arc distance L_0/4 give pair sums L_0/2, L_0/2, L_0, so the four-point condition fails.

**Prop 3.12: (a), (b) correct; (c), (d) correctly labelled HEURISTIC/OPEN.**
- "No known tool applies" in (c) is a negative literature statement, not a theorem.
- (b) P f(x) = f(x_1 e_1) has norm one because |x_1 - y_1| <= |x - y|_2. Its range is isometric to Lip_0(R) = L_oo(R).

## 4. Sections 4-6 of the notes

**Prop 4.1: correct.** F(M) consists of weak*-continuous functionals; apply Prop 3.1.

**Lemma 4.2: correct.**
- |a_0| + |b_0| = 1 rho-a.e.
- R(x) is nonempty by compactness of the l_1-circle D.
- (A) Two distinct points of D are never positive multiples of each other, so a separating (s,t) exists. Then x lies in both supp m^+ and supp m^-, contradicting Lemma 3.5a.
- (B) Continuity follows from a finite cover of D \ W.
- (C) The countable-base argument with inner regularity gives (a_0,b_0)(y) in R(y) off a null set.
- (D) supp m^+ = cl P, because every nonempty relatively open subset of S = supp rho has positive measure.

**Cor 4.3: correct.**
- (i) ab = 0 a.e., hence everywhere on S by continuity. The sets {a != 0} and {b != 0} are clopen in S.
- (ii) The sets W_q are:
  - nonempty and open in S;
  - pairwise disjoint: r takes values in {q,-q} on W_q, and no two points of an arc of angular length < pi are equal or antipodal.
  - This gives uncountably many disjoint sets of positive measure, which is impossible.
- (iii) follows from (ii).

**Prop 4.4: correct, modulo a KNOWN fact.** Regular measures on scattered compacta are purely atomic (Rudin 1957 / Pelczynski-Semadeni 1959). Rudin's paper was confirmed to exist; the measure statement is FROM MEMORY.

**Prop 4.5: correct.**
- Both inequalities int g h <= ||g||_1 and s sigma(h) <= |s| ||sigma|| must be equalities.
- g != 0 a.e. pins h = sign g.
- s = 1 and s = -1 give sigma(sign g) = ||sigma|| = -sigma(sign g).

**4.6: correct.** A complemented l_oo inside Lip_0(M) prevents K from being scattered: C(K) with K scattered is Asplund, and Asplund spaces do not contain l_1.

**4.7.**
- (a) The PROVED part is Cor 4.3(i). "Cannot in general be merged" is HEURISTIC.
- (c) The fat Cantor argument is correct:
  - An optimal representation g = sum a_k 1_{I_k}/|I_k| with sum |a_k| = ||g||_1 forces pointwise equality in the triangle inequality, so |g| >= |a_k|/|I_k| a.e. on I_k.
  - No nondegenerate interval lies a.e. inside a nowhere dense set.
  - So the kernel of the quotient map l_1(M~) -> F([0,1]) is not proximinal.
- The de Leeuw description of Lip_0(M) as Gamma^perp was re-checked: u(x,y) d(x,y) = f(x) - f(y) follows from the three-point relation with z = 0.

**Prop 5.1: correct** (the classical Lindenstrauss argument).
- Invariance gives additivity of Pf.
- Boundedness gives R-linearity.
- Linear f are fixed.

**Example 5.2: correct.**
- ||w + 1||_oo = 2 - alpha and ||w - 1||_oo = 1 + alpha, which differ when alpha != 1/2.
- The existence of A with phi(1_A) != 1/2 is correctly derived from non-atomicity.

**Prop 5.3: correct** (classical: the standard extension to l_oo, then Phillips).

**Prop 5.4: correct but tautological.** Both "=>" directions only use that the universal objects l_oo(Gamma) and l_1(Gamma) have P.

**5.5: correctly labelled OPEN.** The reference to Preprint B, Thm finite-blocks(b) (strict convexity of (c_0,p_J)**) matches the provided tex.

**6.1 Status table: correct, with two updates.**
- Row "tree-like M without branching points ... infinite wedge of one fixed finite piece -- SKETCH": upgrade to PROVED (R1).
- Row "graphs with infinitely many cycles (Hawaiian earring)": the metric must be specified.
  - With the intrinsic metric, the Hawaiian earring is a wedge of circles (R3).
  - With the Euclidean metric of R^2, it is a different space.

**6.2 Notions that fail.**
- (N1) Confirmed. KMS covers geodesic M. For length spaces: Cascales-Chiclana-Garcia-Lirola-Martin-Rueda Zoca, J. Funct. Anal. 277 (2019) (snippet).
- (N2) Correct.
- (N3) See D2.
- (N4) Correct.
- Addition (snippet only; the source paper was not pinned down): a search result states that F(S^1), the predual of Lip_0(S^1), fails Lindenstrauss property A.
  - This is a different notion: the predual as domain, with all ranges.
  - It is consistent with Cor 3.10.

## 5. Citation check

All checks below are from WebSearch snippets; URLs are given.

**C1. Lindenstrauss, Israel J. Math. 1 (1963) 139-148. Confirmed.**
- Record: DOI 10.1007/BF02759700 (scilit.net). "Reflexive => property A" appears in snippets of arXiv 1306.1155.
- The biadjoint theorem and "beta => B" are well known but were not visible in the snippets: from_memory_plausible.

**C2. Johnson-Wolfe, Studia Math. 65 (1979) 7-19. Paper confirmed; JSON wording misstated (D3).**
- Paper: https://eudml.org/doc/218261.
- Content, per an arXiv 1306.1155 snippet: compact operators are approximable by norm-attaining operators when the DOMAIN is C(K), or the RANGE is L_1 (real case) or an L_1-predual.
- The JSON wording "NA dense for real C(K) domains" misstates this.

**C3. "JW for L_1-predual domains". Not confirmed (D4).** The secondary source puts L_1-preduals on the range side.

**C4. Schachermayer, Pacific J. Math. 105 (1983) 427-438. Confirmed.** Abstract at https://msp.org/pjm/1983/105-2/pjm-v105-n2-p13-s.pdf:
- weakly compact operators from C(K) are approximable by norm-attaining operators;
- NA(C(K),L_1[0,1]) and NA(C(K),l_2) are dense;
- NA(L_1[0,1],C[0,1]) is not dense.

**C5. BPBp papers. Confirmed.**
- Kim-Lee, arXiv 1407.7872: BPBp for (C(K),Y) with Y uniformly convex. The journal data (JMAA 2015) were not shown by the search.
- Kim-Lee-Lin, J. Nonlinear Convex Anal. 17 (2016) 243-249, any measure space: https://digitalcommons.memphis.edu/facpubs/5836.
- Acosta, Banach J. Math. Anal. 10 (2016) 307-319.

**C6. KLMW. Confirmed.**
- "Norm attaining operators of finite rank", in The Mathematical Legacy of Victor Lomonosov (De Gruyter 2020) 157-188; arXiv 1905.08272.
- Confirmed details: the sentence "For C_0(L), we do not know whether ... NA(C_0(L)) contains a dense linear subspace", and the result for isometric preduals of l_1.

**C7. Rmoutil, J. Funct. Anal. 272 (2017) 918-928. Confirmed.**

**C8. Godard, Proc. AMS 138 (2010) 4311-4320. Confirmed.**
- https://www.ams.org/proc/2010-138-12/S0002-9939-2010-10421-5/
- Confirmed: F(M) is isometric to a subspace of L_1 iff M embeds into an R-tree.
- The branching-point result (F(M) = L_1(mu) when M contains the branching points) is confirmed through a citing snippet.

**C9. Dalet-Kaufmann-Prochazka, Bull. Belg. Math. Soc. 23 (2016) 391-400. Confirmed.**
- Confirmed: ultrametric spaces never give l_1(Gamma); negligibility and 0-hyperbolicity are necessary.
- The exact "iff" with branching points: from_memory_plausible.

**C10. Godefroy-Kalton, Studia Math. 159 (2003) 121-141. Confirmed.**
- Confirmed: for separable X, a Lipschitz right inverse yields a linear right inverse.
- The isometric version, used for the norm-one weak*-continuous projection: from_memory_plausible.

**C11. Lindenstrauss, Michigan Math. J. 11 (1964) 263-287. Paper confirmed.** The complementation statement was not visible (from_memory_plausible). The notes' own proof (Prop 5.1) is correct.

**C12. Cuth-Kalenda-Kaplicky, Mathematika 63 (2017) 538-552. Confirmed.**

**C13. Free-space structure papers. Confirmed.**
- Cuth-Doucha-Wojtaszczyk, Proc. AMS 144 (2016) 3833-3846: complemented l_1 in F(M) for infinite M.
- Aliaga-Medina, arXiv 2601.03131, "Lipschitz extension and Lipschitz-free spaces over nets in normed spaces" (Jan 2026).

**C14. Naor-Schechtman, SIAM J. Comput. 37 (2007) 804-826. Confirmed.** The free-space corollary is from_memory_plausible.

**C15. Kadets-Martin-Soloviova, Banach J. Math. Anal. 10 (2016) 621-637. Confirmed.** Secondary sources attribute the geodesic case to KMS.

**C16. arXiv 2110.02066. Exists, but the quoted sentence was not seen (D8).**
- It is Dantas-Falco-Jung, Results Math. 2023.
- The statement itself is confirmed via arXiv 1306.1155.

**C17. Confirmed:**
- Martin, RACSAM 110 (2016) 269-284 (arXiv 1502.07084);
- Uhl, Pacific J. Math. 63 (1976) 293-300;
- Bourgain, Israel J. Math. 28 (1977).

**C18. Confirmed:**
- Aliaga-Petitjean-Prochazka, J. Funct. Anal. 280 (2021) 108916;
- Kalton, Collect. Math. 55 (2004) 171-217;
- Chiclana-Garcia-Lirola-Martin-Rueda Zoca, arXiv 1907.07698.

**C19. Textbook facts.**
- Confirmed: Grothendieck's theorem on 1-complemented subspaces of L_1 (arXiv 2412.14808 snippet) and the four-point theorem (arXiv 2303.07920, Thm 6.4).
- from_memory_plausible: Kakutani, Stone, Phillips, Rudin / Pelczynski-Semadeni.

**C20. Preprint B. Quoted correctly** (checked against the tex): Lemma densesubspace, Theorem read-finite-density, Thm finite-blocks(b).

**Summary.** No hallucinated reference was found. There are two misstatements (C2 wording, C3) and one unconfirmed attribution (C16).

## 6. New results by the referee (all PROVED here)

### R1. C(K,E) has (LL)

**Theorem R1.** Let K be compact Hausdorff and let E be a finite-dimensional real normed space. Then C(K,E) (sup norm) has (LL). Hence:
- P(C(K,E)) holds;
- P(l_oo(Gamma,E)) holds, because l_oo(Gamma,E) is isometric to C(beta Gamma, E).

**Proof.** Fix a basis e_1..e_m of E with dual basis e_1^*..e_m^*, and put C_E := max_k ||e_k^*||_{E^*}. For F in C(K,E) write F_k := e_k^* o F in C(K); then ||F_k||_oo <= C_E ||F||.

(1) Representation.
- Let phi_1..phi_d in C(K,E)^* and eps > 0.
- For each i,k the map f -> phi_i(f e_k) is in C(K)^*. Riesz gives a Radon measure mu_ik with phi_i(f e_k) = int f dmu_ik.
- Since F = sum_k F_k e_k, we get phi_i(F) = sum_k int F_k dmu_ik.

(2) Approximation.
- Let rho := sum_{i,k} |mu_ik|, a finite Radon measure, and write mu_ik = h_ik rho with |h_ik| <= 1.
- Choose a finite Borel partition A_1..A_n and reals c_ijk with
  sum_{i,k} int |h_ik - sum_j c_ijk 1_{A_j}| drho < eps.
- By inner regularity choose compacta K_j inside A_j with sum_{i,j,k} |c_ijk| rho(A_j \ K_j) < eps.
- Put nu_j := rho restricted to K_j, and
  psi_i(F) := sum_j sum_k c_ijk int F_k dnu_j.
- For ||F|| <= 1:
  |phi_i(F) - psi_i(F)| <= sum_k ||F_k||_oo ||mu_ik - sum_j c_ijk nu_j|| <= C_E sum_k int |h_ik - sum_j c_ijk 1_{K_j}| drho.
- Sum over i and split 1_{K_j} = 1_{A_j} - 1_{A_j \ K_j}. This gives sum_i ||phi_i - psi_i|| < 2 C_E eps.

(3) Attainment.
- Let eta in R^d and put u_j := sum_k (sum_i eta_i c_ijk) e_k^* in E^*. Then psi_eta := sum_i eta_i psi_i satisfies
  psi_eta(F) = sum_j int_{K_j} <u_j, F(x)> drho(x).
- Hence |psi_eta(F)| <= sum_j ||u_j|| rho(K_j) whenever ||F|| <= 1.
- Pick v_j in B_E with <u_j, v_j> = ||u_j||; this exists because B_E is compact.
- The K_j are pairwise disjoint compact sets, so G_0 := v_j on K_j is continuous on their union.
- Extend each coordinate e_k^* o G_0 by Tietze. This gives a continuous G: K -> E with G = v_j on K_j.
- Let r(v) := v / max(1, ||v||). It is a continuous radial retraction onto B_E and the identity on B_E. Put F := r o G.
- Then F is in C(K,E), ||F|| <= 1, F = v_j on K_j, and psi_eta(F) = sum_j ||u_j|| rho(K_j) >= ||psi_eta||.
- So psi_eta attains its norm at F (and ||F|| = 1 if psi_eta != 0).
- Thus span{psi_i} lies in NA(C(K,E),R). QED

**Isometry l_oo(Gamma,E) = C(beta Gamma,E).** A bounded x: Gamma -> E takes values in a compact ball, so it extends continuously to beta Gamma. The sup norm is unchanged because Gamma is dense. Restriction is the inverse.

**Corollary R1'.** Let M_0 be a finite pointed metric space, and let M be the wedge of any family (M_gamma)_{gamma in Gamma} of copies of M_0.
- Lip_0(M) = l_oo(Gamma, Lip_0(M_0)) by Prop 3.3. So Lip_0(M) has (LL), and P(Lip_0(M)) holds.
- More generally, by Cor 3.4(ii), any finite wedge of such spaces, of Godard-class spaces and of finite-Betti metric graphs has (LL).
- Example: the infinite wedge of equilateral triangles, where Lip_0 = l_oo(H) and JW does not apply (Ex 3.6(b)).
- This upgrades the SKETCH (sums_tensors Prop 12(b)) quoted in the notes.
- Novelty is not claimed: R1 is the Johnson-Wolfe argument with vector values.

### R2. Removing sigma-finiteness and countability

**(a) Theorem 3.9 holds for an arbitrary measure space (Omega, Sigma, mu).**
- Each g_l vanishes off a sigma-finite set. Let Omega_0 be the union of these sets.
- Restriction gives an isometry L_oo(mu) = L_oo(mu|Omega_0) (+)_oo L_oo(mu|Omega_0^c). Under it, X = X_0 (+)_oo L_oo(mu|Omega_0^c), where X_0 is the constrained space over the sigma-finite set Omega_0.
- X_0 has (LL) by Thm 3.9.
- L_oo(mu|Omega_0^c) is an AM-space with unit 1, hence a C(K) (Kakutani, KNOWN). It has (LL) by Thm 3.5.
- Cor 3.4(ii) concludes.

**(b) Cor 3.10 holds for every connected metric graph G with finite first Betti number b.** No countability or local finiteness is needed.
- (i) d is a metric and G is geodesic. Fix a spanning tree T and subdivide at the two given points.
  - A simple edge path is determined by the ordered list of non-tree edges it uses and their orientations; between them it follows the unique tree path.
  - So there are at most sum_{k<=b} 2^k b!/(b-k)! simple paths between two points.
  - Every walk contains a simple path (loop erasure), so d(x,y) is the minimum of their lengths, which is > 0 for x != y.
- (ii) The edges lying on some cycle form a finite set E_0, since every cycle is a mod-2 sum of the b fundamental cycles.
  - The proof of the isometry in Cor 3.10 never used countability.
  - The cycle constraints g_c vanish off E_0. Hence Lip_0(G) = X_{E_0} (+)_oo L_oo(lambda restricted to the edges not in E_0).
  - X_{E_0} has (LL) by Thm 3.9 (finitely many edges). The second summand has (LL) by R2(a) / Thm 3.5.
  - Cor 3.4(ii) concludes.

### R3. Corona reduction for l_oo-sums

**Setting.** Let (X_gamma)_{gamma in Gamma} be Banach spaces, X := l_oo(Gamma; X_gamma), c_0 := c_0(Gamma; X_gamma), and Q := X/c_0 with quotient map pi.

**Lemma R3.1 (L-decomposition).** Every phi in X^* is uniquely a + s, where:
- a(x) = sum_gamma a_gamma(x_gamma) with (a_gamma) in l_1(Gamma; X_gamma^*);
- s lies in c_0^perp;
- ||phi|| = sum_gamma ||a_gamma|| + ||s||.

**Proof.**
- Let a be the extension of phi|c_0 = (a_gamma) in l_1(X_gamma^*) given by the absolutely convergent sum, and s := phi - a, which vanishes on c_0.
- Given eps, choose:
  - a finite set F with sum_{gamma not in F} ||a_gamma|| < eps;
  - unit vectors x_gamma (gamma in F) with a_gamma(x_gamma) > ||a_gamma|| - eps/|F|;
  - y in B_X with s(y) > ||s|| - eps.
- Let z agree with x_gamma on F and with y off F. Then z - y is in c_0, ||z|| <= 1, and phi(z) >= ||a|| + ||s|| - 3 eps.
- Uniqueness: a is determined by phi|c_0. QED

**Lemma R3.2 (closed balls).** pi(B_X) = B_Q.
**Proof.** ||pi x|| = limsup_gamma ||x_gamma|| along the cofinite filter. If this is <= 1, then x'_gamma := x_gamma / max(1, ||x_gamma||) gives ||x'|| <= 1 and x - x' in c_0. QED

**Theorem R3.** X has (LL) iff every X_gamma has (LL) and Q has (LL).

**Proof.**
- **"=>" for the summands.**
  - Write X = X_gamma (+)_oo W. Given phi_i in X_gamma^*, apply (LL) in X to phi_i o P_gamma.
  - If psi = (psi^gamma, psi^W) attains its norm at (x,w), then psi^gamma(x) = ||psi^gamma|| and psi^W(w) = ||psi^W||, since both inequalities must be equalities.
  - So the restrictions psi_i^gamma have span inside NA(X_gamma), and ||psi_i^gamma - phi_i|| <= ||psi_i - phi_i o P_gamma||.
- **"=>" for the corona.**
  - Given sbar_i in Q^*, apply (LL) in X to s_i := sbar_i o pi. This gives psi_i with span in NA(X). Split psi_i = a'_i + s'_i by R3.1.
  - The L-decomposition gives ||s'_i - s_i|| <= ||psi_i - s_i||.
  - If sum eta_i psi_i attains at x, then sum eta_i s'_i attains at x, by the same equality argument.
  - So the induced functionals on Q attain at pi(x) with the same norm, because pi^* is isometric.
- **"<="**
  - Given phi_i = a_i + s_i and eps, choose a finite F with sum_i sum_{gamma not in F} ||a_{i,gamma}|| < eps. Write X = X_F (+)_oo X^F (coordinates in F / off F).
  - s_i vanishes on X_F, which lies inside c_0. So phi_i^F := (a_i restricted to F) (+) (s_i restricted to X^F) satisfies ||phi_i - phi_i^F|| = sum_{gamma not in F} ||a_{i,gamma}||.
  - X_F has (LL): it is a finite l_oo-sum of (LL) spaces (Cor 3.4(ii)).
  - X^F / c_0(Gamma \ F) = Q isometrically. So (LL) of Q, together with R3.2 applied to X^F, gives functionals t_i on X^F that vanish on c_0, are eps-close to s_i|X^F, and whose combinations all attain on B_{X^F}.
  - Combine the two families as in Cor 3.4(ii). QED

**Corollary R3'.**
- (a) Let C_gamma (gamma in an infinite set Gamma) be circles of lengths L_gamma > 0, and let B be their wedge with the wedge metric. With L_n = 2 pi/n this is exactly the intrinsic (path) metric of the Hawaiian earring. Then, isometrically and independently of the lengths,
  Lip_0(B) = l_oo(Gamma; X_1), where X_1 := {h in L_oo[0,1] : int h = 0}.
  Proof:
  - Cor 3.10 with b = 1 gives Lip_0(C_gamma) = {h in L_oo[0,L_gamma] : int h = 0}.
  - h -> h(L_gamma .) is an onto isometry from this space to X_1.
  - Then apply Prop 3.3.
- (b) X_1 has (LL) by Thm 3.9. So for countable Gamma, Lip_0(B) has (LL) iff the single space Q_1 := l_oo(N; X_1)/c_0(N; X_1) has (LL).
- (c) Likewise, for an infinite wedge of finite metric spaces with varying Lip_0(M_n) = E_n: (LL) holds iff it holds for l_oo(E_n)/c_0(E_n).
- Status of (b) and (c): OPEN.

**HEURISTIC remark on (c) when dim E_n <= m.**
- After a John-position normalization, l_oo(E_n)/c_0(E_n) is the space of continuous R^m-valued functions on N* = beta N \ N with a continuously varying norm nu_p.
- The proof of R1 goes through when every nu_p is strictly convex: norming vectors then depend continuously on p.
- It fails in general, because the face map p -> {v : nu_p(v) = 1, <u,v> = nu_p^*(u)} need not admit continuous selections (rotating polygons).

### R4. Counterexample to "first infinite non-tree-like M" (D1)

- Let C_4 = {0,a,b,c} with d(0,a) = d(a,b) = d(b,c) = d(c,0) = 1 and d(0,b) = d(a,c) = 2. Let M := C_4 v [0,1], wedged at 0.
- M is not tree-like: the pair sums of the quadruple 0,a,b,c are 2, 2, 4, so the four-point condition fails. Also Lip_0(M)^* is not an L-space (Prop 3.7(b)).
- Lip_0(M) = Lip_0(C_4) (+)_oo L_oo[0,1] by Props 3.3 and 3.8.
  - A finite-dimensional space has (LL) trivially: every functional attains its norm.
  - L_oo[0,1] has (LL) by Thm 3.5.
- So Cor 3.4(ii) gives (LL), hence P(Lip_0(M)).
- Corrected claim: Cor 3.10 gives, as far as we know, the first CONNECTED non-tree-like M with P(Lip_0(M)).

## 7. What remains open; required fixes

### Open

These were correctly identified by the explorer; some are sharpened here.
- **O1.** P(Lip_0(M)) for all M (the question itself): OPEN. It follows from a positive JW answer, and a counterexample would refute JW. No reduction of JW to this class is known: P is not known to pass to 1-complemented subspaces, and passing to subspaces or exact quotients is equivalent to JW (Prop 5.4).
- **O2.** Lip_0(R^n), n >= 2 (any norm), and (LL) for it: OPEN. No known tool applies.
- **O3.** Graphs with infinitely many independent cycles: OPEN.
  - For the Z^2 grid nothing new is known.
  - For bouquets of circles, including the intrinsic Hawaiian earring, (LL) is now equivalent to (LL) of the single corona Q_1 = l_oo(X_1)/c_0(X_1) (R3').
- **O4.** l_oo(E_n) with varying finite-dimensional E_n (infinite wedges of varying finite pieces): OPEN.
  - In terms of (LL), it is equivalent to the corona question R3'(c).
  - Strictly convex E_n of bounded dimension look tractable by the R1 argument (HEURISTIC).
- **O5.** (DL) for C(K) with K not scattered (KLMW), e.g. L_oo[0,1] and l_oo: OPEN.
- **O6.** OPEN:
  - Is P inherited by 1-complemented subspaces?
  - Does P(Z**) imply P(Z)?
  - Do P(X_1) and P(X_2) imply P(X_1 (+)_oo X_2)?
- **O7.** "Lip_0(M) is an L_1-predual => F(M) = L_1(mu)" (the notes' Q8): OPEN, not settled here.
- **O8.** Novelty of Thm 3.9: not certified; the search budget was exhausted.

### Required fixes to the notes and JSON

- **F1.** Replace "first INFINITE non-tree-like M" by "first CONNECTED non-tree-like M" (R4).
- **F2.** Delete the property-A claim for L_oo[0,1] in (N3), or mark it OPEN (D2).
- **F3.** Johnson-Wolfe:
  - state the compact-operator form: domain C(K), or range L_1 / an L_1-predual (D3);
  - drop or flag the domain-side L_1-predual version (D4).
- **F4.** Relabel the "Consequence" of Prop 3.2 as HEURISTIC (D5).
- **F5.** Cite Grothendieck in Ex 3.6(b) (D6).
- **F6.** Remove sigma-finiteness (Thm 3.9) and countability / local finiteness (Cor 3.10), or cite R2 (D7).
- **F7.** Upgrade "infinite wedge of one fixed finite piece" from SKETCH to PROVED (R1).
- **F8.** For "C(K) fails property A for infinite metrizable K", cite the confirmed source arXiv 1306.1155 (Martin, J. Funct. Anal. 2014) rather than arXiv 2110.02066 (D8).
- **F9.** Specify the metric whenever the Hawaiian earring is named. The intrinsic metric gives a wedge of circles (R3').

End of report.
