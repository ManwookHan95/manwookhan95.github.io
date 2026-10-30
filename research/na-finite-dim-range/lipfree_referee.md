# Referee report, key = lipfree: Lipschitz-free domains F(M), finite-dimensional ranges Y

This is an adversarial check of lipfree_notes.md and the explorer's structured result.

Labels:
- PROVED: complete proof given here, or verified line by line.
- KNOWN [S]: confirmed by a web-search hit (URL given).
- KNOWN [M]: from memory only.
- SKETCH, HEURISTIC, OPEN, FALSE: as usual.

Real scalars are used throughout. The notation follows the notes (T_F, molecules m_xy, SNA, DNA, beta, iota).

Network limits:
- Only WebSearch was usable.
- The single other host tried, ems.press (for the CGMR 2021 PDF), does not resolve in this session. It would have to be allowed in the session's network settings.
- The session-wide web-search budget ran out before two minor items could be checked: Smith, arXiv 2412.05177, and arXiv 2606.02918. Both were only quoted by the explorer as secondary sources.

## 0. Bottom line

1. **Verdict OPEN: confirmed.** It is neither overclaimed nor underclaimed.
   - Nothing in the notes claims a counterexample, which would answer Johnson-Wolfe.
   - Nothing claims that density always holds.
   - A positive Johnson-Wolfe answer implies density for every F(M). The converse would need a transfer from F(X) to X, and that transfer is not proved: (Q-dir) is OPEN.
   - EQUIVALENT_TO_JOHNSON_WOLFE is therefore not justified. I could not prove the transfer either.

2. **Every PROVED item I re-derived is correct, with these qualifications.**
   - (E1) **GAP in remark R4.** The claim that C^1 curves give directional attainment is proved only when the attaining element has the form gamma^(nu) with ||nu||_1 = ||gamma^(nu)||. For an arbitrary element of F(gamma(I)) it is a SKETCH. The phrase "never on F(C^1 curves)" in DT2 and Section 5.2 must be restricted accordingly. The correct statement is Remark R4' (Section 3.5).
   - (E2) **OVERCLAIM.** Two heuristic statements are presented as conclusions: "F(X) is at least as good a counterexample candidate as X" (summary) and "F(XX) is not a better candidate than XX itself" (5.4). Only DT2 is proved.
     - Neither implication between "NA(X,Y) dense" and "NA(F(X),Y) dense" is known.
     - The explorer's own OQ2 contradicts the second statement. For X = l_2^2 the linear problem is trivial, NA(X,Y) = L(X,Y), yet density for F(l_2^2) = F(R^2) is OPEN. So F(X) may be strictly harder than X.
   - (E3) **NOT NEW.** Proposition N is a special case of known results. CCGMR 2019 prove that SNA(M,Y) is not dense when M is a length space [S], and every Banach space is a length space. The proof in the notes is correct.
   - (E4) **WORDING.** "Via the lineability criterion it reduces to approximating Lipschitz gradient fields ..." should read "would follow from". Lemma L is only a sufficient condition.
   - (E5) **WORDING.** In 1.1, "Such M give F(M) a separable dual" should read "make F(M) a separable dual space", since F(M) = lip_0(M)^*. The conclusion that F(M) has the RNP is unaffected.

3. **Citations.** I found no hallucinated paper. Every cited paper exists, with matching title, year and main statement, with one exception and a few unconfirmed details:
   - Misattribution: arXiv 2312.00393 is by G. Choi, M. Jung, H. J. Lee and O. Roldan (four authors). The claimed "example with no isometric c_0" is not in its abstract.
   - Statements taken from memory that I could not confirm are listed in Section 2.
   - I found one relevant reference the notes do not cite: Bachir, arXiv 2304.12611. It gives a new class of spaces with property A and applications to Lipschitz maps; I did not verify its details.

4. **New results in this report (all PROVED, Section 3).**
   - Proposition S (stars with a missing centre, bounded well-ordered inner radii) gives dense lineability. It settles the explorer's own open example, the legs [1/2,1] of an infinite star with the centre removed (2.4 CAVEAT and OQ4).
   - Lemma H gives dense lineability for finite-codimensional subspaces of L_1 cut out by finitely-valued functionals.
   - Proposition FU shows that finite disjoint unions of compacta preserve dense lineability.
   - Remark NI shows that the R^d inclusion problem (OQ2) does not depend on the norm. A positive answer would therefore settle F(E) for every finite-dimensional normed space E.
   - Remark R4' is the correct form of R4.

   By Lemma L, each dense-lineability result gives density of NA(.,Y) for every finite-dimensional Y.

## 1. Re-derivation of the PROVED claims (line by line)

### 1.1 Lemma L (lineability criterion): CORRECT
- The map y* -> ||S^* y*|| is ||S||-Lipschitz, hence continuous on the compact set B_{Y*}.
- If S != 0, its maximum is ||S|| > 0. So S^* y_0* = sum_i y_0*(y_i) psi_i is a nonzero element of V, which lies in NA(X,R).
- The approximation estimate ||T - S|| <= sum_i ||phi_i - psi_i|| ||y_i|| is right.
- This is the finite-dimensional-range case of Preprint B, Lemma densesubspace.

### 1.2 Proposition 2.2 (every L_1(mu)): CORRECT
- Step 1 is correct also for mu that is not sigma-finite:
  - A_f is countable, because the sets in the family are pairwise almost disjoint, so every finite sum of mu(A cap S_n) is at most mu(S_n).
  - Maximality of the family forces mu(B) = 0.
  - L_1(mu) is isometric to the l_1-sum of the spaces L_1(mu|A), and its dual is the l_infinity-sum of the spaces L_infinity(mu|A).
- Step 2 is correct: V is linear, V is dense (floor rounding), and every nonzero element attains its norm at sign(c_0) 1_E / mu(E).
- The content is classical (Uhl; finite-dimensional Y has the RNP), but the proof is complete.

### 1.3 Proposition 2.3 (closed M in R): CORRECT
- (i) Gaps are automatically bounded, because the finite endpoints of conv(M) lie in M. The three-piece estimate x <= b_1 <= a_2 <= y covers all cases: x or y in M, x or y in a gap, or both in the closure of one gap.
- (ii) W_0 is contained in W, because for x, y in M every gap lies either inside or outside [x,y]. The approximation of 1_E (E contained in M, finite measure) by sum_k 1_[s'_k,t'_k] has error below 2 eps, since these intervals overlap only at endpoints. Isometry follows from h = sign(u), and the map is onto because its range is closed and dense.
- (iii) is clear.
- (iv) V_R is linear and dense, and it lies in NA because E = {g~' = c} cap [x_1,x_2] with x_i in M is a union of whole gaps and a subset of M.
- The fat Cantor example (NA strictly larger than SNA on F([0,1])) is correct.

### 1.4 Section 2.4 (R-trees containing their branching points)
- Godard's theorem: KNOWN [S]. The corollary drawn from it is correct.
- The CAVEAT example (infinite star with the centre removed) is RESOLVED POSITIVELY by Proposition S (Section 3.1).

### 1.5 Propositions 2.5 and 2.6 (wedge sums, l_1-sums): CORRECT
- Completeness of the wedge: a Cauchy sequence that visits infinitely many branches converges to the base point.
- In 2.6, direction (=>): the strict inequality ||S J_{i_0}|| > ||S - T|| >= sup_{i != i_0} ||S J_i|| forces a = 1.
- This is probably known (stability of density of NA under l_1-sums of domains [M]).
- Addendum: dense LINEABILITY passes to FINITE wedge sums, because the maximum over finitely many pieces is attained. For infinite wedge sums it is not proved.

### 1.6 Section 2.7(b) (NA = SNA when every element is a convex integral of molecules): CORRECT
- This rests on two APS results, both confirmed [S]:
  - every element of F(M) is a convex series of molecules when M is uniformly discrete;
  - every element is a convex integral of molecules when F(M) has the RNP.
- Alternative proof in the RNP case:
  - The norming face of B_F(M) is closed, bounded and convex.
  - The RNP gives the Krein-Milman property, so the face has an extreme point.
  - That point is extreme in B_F(M), hence an elementary molecule (APS 2412.04312 [S]).

### 1.7 Proposition C (C^1 simple curves, the circle T): CORRECT
I re-derived every step.
- Step 0:
  - (a) The 1-Lipschitz bound uses periodic representatives.
  - (b) w(delta) -> 0 by uniform continuity of gamma' on [0,l], or by periodicity in the closed case.
  - (c) The chord-arc constant comes from compactness of {dd >= delta_0} and injectivity.
- Step 3, Case B:
  - A limit pair (s*,t*) off the diagonal would be attained, because D is continuous there. So the pairs collapse onto the diagonal.
  - Hence L = ||g'||_inf. A finitely valued g' takes the value +-L on a set of positive measure.
  - The attaining element gamma^(sign(c_0) 1_E / lambda(E)) has norm at most 1, because ||gamma^|| <= 1.
- Step 4: the mean-zero correction keeps G periodic, and the Lipschitz estimate integrates over the shorter arc.
- There are no hidden hypotheses. "C^1" is meant in the Frechet sense, with unit speed in the ambient norm; any regular C^1 curve can be reparametrized this way.
- The deduction "F(T) fails property A (JMR, confirmed [S]) only through infinite-dimensional ranges" is valid.
- I found no prior occurrence of Proposition C in the literature I checked.

### 1.8 Proposition U1 and Example U2: CORRECT
- U1: the value set is finite, minima exist because D(M) is well ordered, and floor rounding gives density.
- U2:
  - All distances lie in [1,2].
  - Lip(f) = 1 is approached along the pairs (x_n, y_m) but is not attained.
  - APS (convex series [S]) together with 2.7(b) shows f is not in NA.
  - So the well-ordering hypothesis of U1 cannot be dropped.

### 1.9 Lemma R1: CORRECT
- The proof uses, in order:
  - Krein-Smulian (Banach-Dieudonne);
  - bounded weak* convergence equals pointwise convergence;
  - equicontinuous nets converge locally uniformly;
  - integration by parts against C_c^infinity;
  - L_1-approximation.
- V_fin is linear and lies in NA.

V_fin test cases:
- (i) Laminates: PROVED (trivial).
- (ii) Uniformly continuous gradient: SKETCH, credible.
  - The pyramid u(x) = xi.x + 1 - max_i (xi - a_i).x has gradient in {a_i} a.e. and equals xi.x on the boundary of P'.
  - P' is bounded if and only if xi lies in int conv{a_i}.
  - Shape-regular P1 interpolation has gradient error at most C w(delta).
  - A Vitali covering finishes the argument (standard Dacorogna-Marcellini technique [M]).
- (iii) Radially wild example: SKETCH, not checked in detail.

### 1.10 Proposition N: CORRECT, but NOT NEW
- The key step is correct: exact attainment on [b,a] forces slope Lip(G) on every subsegment.
- Non-density of SNA(M,.) for length spaces M is in CCGMR 2019 [S], and Banach spaces are length spaces. KMS 2016 already covers Y = R for Banach spaces.

### 1.11 Remarks R1-R4 (Section 4.2)
- R1, R2, R3: CORRECT.
  - In R2, compactness of B_{Y*} gives y*_k -> y* with ||y*|| = 1.
  - In R3, F(segment) = L_1 isometrically.
- R4: GAP.
  - The argument shows: if T_G attains its norm at gamma^(nu) with ||nu||_1 = 1, then G is in DNA.
  - For a general mu in F(gamma(I)) one can have ||nu||_1 > ||mu||. This happens, for example, for molecules of far-apart points of a closed curve, or for mixtures. In that case phi(mu) = L does not force (phi o gamma)' = L on a set of positive measure.
  - Status for general elements: SKETCH. It would follow from the existence of optimal "local + molecular" decompositions.
  - Corrected statement: Remark R4' (Section 3.5).

### 1.12 Lemma DT (directional transfer): CORRECT
I checked each step.
- Gateaux differentiability off a Gauss-null Borel set, for Lipschitz maps from separable X into Y with the RNP: Aronszajn, Phelps [M], standard.
- The measure g is nondegenerate: for x* != 0, x*(sum_j 2^{-j} xi_j x_j) has variance sum_j 4^{-j} x*(x_j)^2 > 0.
- g(B(0,1)) > 0, for example because P(|xi_j| < j/4 for all j) > 0.
- Fubini on g x Lebesgue.
- The 2L||v_k|| loss estimate.
- At Gateaux points, ||DG(p)|| <= L and ||DG(p) - T|| <= eps.
- The diagonal limit A attains its norm at u.

The reflexive-Y remark is fine, using WOT-convergent subnets. Novelty: plausibly folklore around Godefroy's "maximal derivative attainment" (Godefroy 2016 and Choi 2026 [S]); I could not settle it either way.

### 1.13 Corollaries DT1, DT2, DT3: CORRECT, except DT2's parenthetical
- DT3:
  - Lip(S) = max over y* of Lip(y* o S), and y* -> Lip(y* o S) is Lip(S)-Lipschitz.
  - If S != 0, the maximizer has norm 1.
- DT2's parenthetical "never on F(C^1 curves)" must be restricted as in R4'.

### 1.14 Example Gamma: CORRECT
- Isometry: 2^{-n}|sin 2^n t - sin 2^n s| <= |t - s|.
- Nowhere differentiable: if |cos a| < 1/2 then cos 2a < -1/2, so the coordinatewise limit (1, cos 2^n t) is not in c_0. The map is not even weakly differentiable.
- This is a standard example (Benyamini-Lindenstrauss [M]).
- Side remark: for X = c_0 itself, the finitely supported functionals form a dense subspace of NA(c_0,R). So NA(c_0,Y) is dense by Lemma L, and Gamma is purely structural.

### 1.15 Section 5.2 (molecule cones in Martin's space XX): CORRECT
- (i) follows from the subsegment argument of Proposition N.
- (ii) and (iii) follow from smoothness of XX: the norming functional of u is unique.

### 1.16 The labels SKETCH and HEURISTIC are used correctly
- de Leeuw route: SKETCH.
- Direct R^2 boosts: HEURISTIC. The damping estimate ||DG|| <= L is correct but gives no margin.

### 1.17 Summary statements comparing F(X) and X: OVERCLAIM (E2)
- What is proved (DT2): if T is at distance d > 0 from NA(X,Y), then every R in NA(F(X),Y) with ||R - T beta|| < d is the linearization of a map that is not in DNA. In particular R does not attain its norm at molecules, or at isometric-curve densities.
- What is not proved, in either direction:
  - "NA(X,Y) not dense => NA(F(X),Y) not dense";
  - "NA(X,Y) dense => NA(F(X),Y) dense". For X = l_2^2 the second is exactly the open OQ2.
- So "F(XX) is not a better candidate than XX" is unjustified. F(XX) has many more operators to approximate (all Lipschitz maps) as well as more attaining elements.

## 2. Citation check

Status codes:
- C: confirmed by a search hit.
- MIS: misattributed or misstated.
- M: from memory, plausible, not confirmed.
- NC: not checked (the session's search budget was exhausted).

| # | Reference (as cited) | Status | Note |
|---|---|---|---|
| 1 | Kadets-Martin-Soloviova, Banach J. Math. Anal. 10 (2016) 621-637 | C | SNA is weakly but not norm dense; directional notion dense for uniformly convex X. [Project Euclid](https://projecteuclid.org/journals/banach-journal-of-mathematical-analysis/volume-10/issue-3/Norm-attaining-Lipschitz-functionals/10.1215/17358787-3639646.full) |
| 2 | Cascales-Chiclana-Garcia-Lirola-Martin-Rueda Zoca, JFA 277 (2019) 1677-1717 | C | F(M) with the RNP gives SNA dense for every Y. The table of contents has property alpha and quasi-alpha. SNA is not dense for length spaces. [ar5iv](https://ar5iv.labs.arxiv.org/html/1807.03363) |
| 3 | Chiclana-Garcia-Lirola-Martin-Rueda Zoca, Rev. Mat. Iberoam. 37 (2021) 1917-1951 | C | SNA(T,Y) is not dense for any Y. Some M containing [0,1] have SNA dense. [arXiv](https://arxiv.org/pdf/1907.07698) |
| 4 | Jung-Martin-Rueda Zoca, JFA 284 (2023) 109746, Ex. 5.2 | C | F(T) is separable and fails property A. [arXiv](https://arxiv.org/pdf/2203.04023) |
| 5 | Aliaga-Gartland-Petitjean-Prochazka, Trans. AMS (2022) | C | Purely 1-unrectifiable characterization. "RNP iff p1u" confirmed through secondary sources. [arXiv](https://arxiv.org/pdf/2103.09370) |
| 6 | Godard, PAMS 138 (2010) 4311-4320 | C | Isometric embedding into L_1 iff M is a subset of an R-tree. Isometric to L_1(mu) if M contains its branching points. [AMS](https://www.ams.org/proc/2010-138-12/S0002-9939-2010-10421-5/) |
| 7 | Kalton, Collect. Math. 55 (2004), Prop. 4.4 | C | Uniformly discrete M gives F(M) the RNP and the AP (secondary source: Lancien's commentary). [RACO](https://www.raco.cat/index.php/CollectaneaMathematica/article/view/56573) |
| 8 | Dalet, Mediterr. J. Math. 12 (2015) 973-986 | C | Countable proper M, and proper ultrametric M: F(M) is a dual with the MAP. [arXiv](https://arxiv.org/pdf/1404.3939) |
| 9 | Aliaga-Pernecka-Smith, JFA 2024 (arXiv 2302.13951) | C | Every element is a convex series of molecules when M is uniformly discrete. [arXiv](https://arxiv.org/html/2302.13951v3) |
| 10 | Aliaga-Pernecka-Smith, arXiv 2412.04312 | C | Title: "A solution to the extreme point problem and other applications of Choquet theory to Lipschitz-free spaces". RNP gives convex integrals of molecules; extreme points are elementary molecules. [arXiv](https://arxiv.org/abs/2412.04312v2) |
| 11 | Aviles-Martinez-Cervantes-Rueda Zoca-Tradacete, Rev. Mat. Iberoam. 40 (2024) 189-200 | C | SNA(M) contains an isomorphic copy of c_0 for infinite complete M. [EMS](https://ems.press/journals/rmi/articles/10143994) |
| 12 | G. Choi-Y.S. Choi-Martin, JMAA 483 (2020) 123600 | C | Der(R,Y) dense iff Y has the RNP; classification of the notions. [ar5iv](https://ar5iv.arxiv.org/html/1907.01936) |
| 13 | Garcia-Lirola-Guerrero-Viu-Rueda Zoca, arXiv 2407.10710 | C | Concerns norm-attaining tensors. Published in Banach J. Math. Anal. 19 (2025). [arXiv](https://arxiv.org/abs/2407.10710) |
| 14 | G. Choi, PAMS 151 (2023) 1729-1741 | C | Attainment "toward vectors" is automatic iff Y is finite-dimensional. [DOI](https://doi.org/10.1090/proc/16284) |
| 15 | Chiclana-Martin, Nonlinear Anal. 188 (2019) 158-178 | C | Lip-BPB holds for finite M with finite-dimensional Y, and both conditions are needed. [UGR](https://produccioncientifica.ugr.es/documentos/61b4fcbdff6ada1aa9a09c85?lang=en) |
| 16 | Cuth-Kalenda-Kaplicky, Mathematika 63 (2017) 538-552 | C | F(Omega) is L_1(Omega,E) modulo divergence-free fields. [arXiv](https://arxiv.org/pdf/1610.03966) |
| 17 | Godefroy, Pure Appl. Funct. Anal. 1 (2016) 39-46 | C / M | The paper is confirmed indirectly (cited by Dalet-Lancien and by Choi): a moduli inequality and a weak notion of attainment with non-density examples. The attribution to it of "SNA dense for compact M with lip_0 separating points and finite-dimensional Y" is M. |
| 18 | "G. Choi-M. Jung", arXiv 2312.00393 | MIS | The authors are G. Choi, M. Jung, H. J. Lee and O. Roldan. The abstract has pointwise attainment, isometric c_0 / l_infinity copies, and isometric c_0 in SNA for R-trees containing their branching points. The claim "an example with no isometric c_0" is not confirmed. [arXiv](https://arxiv.org/abs/2312.00393v1) |
| 19 | G. Choi, arXiv 2410.16607 | C | Published in Studia Math. 287 (2026) 3-20; characterizes the RNP of the range. [arXiv](https://arxiv.org/html/2410.16607v1) |
| 20 | Aron-Choi-Kim-Lee-Martin, Trans. AMS 367 (2015) 6085-6101 | C / M | The paper is confirmed. The claim "there is X with (X,Y) failing the BPBp for every strictly convex Y" is NOT confirmed. [AMS](https://www.ams.org/journals/tran/2015-367-09/S0002-9947-2015-06551-9) |
| 21 | Bachir, arXiv 2304.12611 (not cited in the notes) | C (existence) | New class of spaces with property A; sigma-porosity; applications to Lipschitz maps. Its relevance to F(M) was not checked. [arXiv](https://arxiv.org/pdf/2304.12611) |
| 22 | Classical results: Lindenstrauss 1963, Bourgain 1977, Uhl 1976, Godefroy-Kalton 2003, Aronszajn 1976 / Phelps 1978, Dacorogna-Marcellini, Daugavet property of F(length space) | M | Standard; not searched. |
| 23 | Smith, arXiv 2412.05177; arXiv 2606.02918 | NC | Search budget exhausted. Both are used only as secondary sources. |

## 3. New results (referee)

### 3.1 Proposition S (stars with a missing centre): PROVED

**Setting.**
- Let I be an index set with |I| >= 2, and let (delta_i)_{i in I} be positive reals.
- Assume their value set Delta = {delta_i} is well ordered (every nonempty subset has a least element) and bounded above. Put delta_* = min Delta > 0 and delta^* = sup Delta < infinity.
- For each i, let M_i be a closed subset of [delta_i, infinity) that contains delta_i. The legs may be unbounded.
- Let M be the disjoint union of the M_i, with metric:
  - d(x,y) = |x - y| for x, y in the same M_i;
  - d(x,y) = x + y for x in M_i, y in M_j, i != j.
- Equivalently, M is the closed set of all s e_i with s in M_i, inside the R-tree star with rays e_i, and the centre c is removed.
- For |I| >= 3, c is a branching point of the hull that is missing from M, so Godard's theorem does not apply.
- Base point: delta_{i_1} for a fixed index i_1.
- For g in Lip_0(M), let g~_i be the gap-affine extension of g|M_i to conv(M_i) (Proposition 2.3), and put p_i = g(delta_i).

**Claim.** Let V be the set of g in Lip_0(M) for which there are finite sets S, P in R such that, for every i, g~_i' lies in S almost everywhere on conv(M_i) and p_i lies in P. Then V is a norm-dense linear subspace of Lip_0(M) contained in NA(F(M),R). Consequently, by Lemma L, NA(F(M),Y) is dense for every finite-dimensional Y.

**Proof.**

(a) M is a complete metric space. It is a subset of the star R-tree, and every cross distance is at least 2 delta_*. So a Cauchy sequence eventually stays in a single closed M_i.

(b) V is linear. If the values lie in S_1, P_1 for one function and in S_2, P_2 for another, the sum has values in the finite sets S_1 + S_2 and P_1 + P_2. The gap-affine extension is linear in g.

(c) A formula for Lip(g), valid for every g. Put A = sup_i Lip(g|M_i) and D = sup over i != j of (p_i - p_j)/(delta_i + delta_j).
- Lip(g) >= A clearly.
- Lip(g) >= D, because d(delta_i, delta_j) = delta_i + delta_j.
- Now take x in M_i and y in M_j with i != j. Since d(x, delta_i) = x - delta_i and d(y, delta_j) = y - delta_j,
  g(x) - g(y) <= (p_i - p_j) + A(x - delta_i) + A(y - delta_j) = A(x+y) + beta,
  where beta = (p_i - p_j) - A(delta_i + delta_j).
- Divide by x + y, which is at least delta_i + delta_j.
  - If beta <= 0, the quotient is at most A.
  - If beta > 0, the quotient is at most A + beta/(delta_i + delta_j) = (p_i - p_j)/(delta_i + delta_j) <= D.
- The same bound holds for g(y) - g(x). Pairs inside one leg have slope at most A.
- Hence Lip(g) = max(A, D).

(d) Every g in V, g != 0, attains its norm.
- Case Lip(g) = D > A.
  - For a value Q in P that is taken by some leg, let m(Q) = min{delta_i : p_i = Q}. It exists because Delta is well ordered.
  - Then D is the maximum, over the finitely many pairs Q_1 > Q_2 of values in P, of (Q_1 - Q_2)/(m(Q_1) + m(Q_2)).
  - Choose legs i, j realizing the maximum. Then i != j, because Q_1 != Q_2.
  - We get g(delta_i) - g(delta_j) = D d(delta_i, delta_j). So g is in SNA, which is contained in NA.
- Case Lip(g) = A >= D.
  - For each i, Lip(g|M_i) = ||g~_i'||_inf (Proposition 2.3(i)), and this belongs to the finite set {|s| : s in S}.
  - So A is a maximum over a finite set, attained at some leg i_0.
  - Proposition 2.3(iv), applied to M_{i_0} with base point delta_{i_0} and to the function g|M_{i_0} - p_{i_0}, gives mu in F(M_{i_0}) with ||mu|| = 1 and <g, mu> = A.
  - F(M_{i_0}) sits isometrically in F(M) (McShane extension), and constants vanish on it. So g attains its norm.

(e) Density. Let g be in Lip_0(M), L = Lip(g), and eps > 0.
- The values p_i are bounded: |p_i - p_{i_1}| <= L(delta_i + delta_{i_1}) <= 2 L delta^*. So q_i = eps*floor(p_i/eps) takes finitely many values.
- Put h_i = eps*floor(g~_i'/eps). Its values lie in the finite set eps*Z cap [-L-eps, L], and h_i is constant on the gaps of M_i.
- Define g_1(x) = q_i + integral from delta_i to x of h_i, for x in M_i. Then g_1~_i' = h_i and g_1(delta_i) = q_i, so g_1 - g_1(delta_{i_1}) lies in V.
- Inside one leg: Lip((g - g_1)|M_i) = ||g~_i' - h_i||_inf <= eps, by Proposition 2.3(i).
- Across legs i != j:
  |(g-g_1)(x) - (g-g_1)(y)| <= |p_i - q_i| + eps(x - delta_i) + |p_j - q_j| + eps(y - delta_j) <= 2 eps + eps(x+y) <= eps(1 + 1/delta_*)(x+y).
- Hence Lip(g - g_1) <= eps(1 + 1/delta_*). QED

**Remarks.**

1. The explorer's open example in 2.4 CAVEAT and OQ4 is the case delta_i = 1/2 and M_i = [1/2,1] for infinitely many i. It is now settled: NA(F(M),R) is densely lineable, and NA(F(M),Y) is dense for every finite-dimensional Y.

2. The well-ordering hypothesis cannot simply be dropped for this V. Take degenerate legs M_i = {delta_i} with delta_1 = 1 and delta_j = 1/2 + 1/j for j >= 2, and let g(delta_1) = 1 and g = 0 elsewhere.
   - Then Lip(g) = sup_j 1/(3/2 + 1/j) = 2/3, and this supremum is not attained.
   - M is uniformly discrete, so APS together with 2.7(b) shows that g is not in NA.
   - Density of NA(F(M),Y) still holds there, by the RNP.
   - For strictly decreasing inner radii with non-degenerate legs, dense lineability is OPEN.

3. Boundedness of Delta is used only for density; attainment needs only well-ordering. An example covered by the proposition: delta_i = 1 - 1/(i+1).

### 3.2 Lemma H (finite-codimensional subspaces of L_1): PROVED

**Statement.**
- Let (Omega, Sigma, nu) be sigma-finite, and let w_1, ..., w_k in L_inf(nu) be finitely valued.
- Put H = {u in L_1(nu) : integral of w_j u dnu = 0 for j = 1..k}.
- For h in L_inf(nu), let phi_h be the functional u -> integral of h u, restricted to H.

Then {phi_h : h finitely valued} is a norm-dense linear subspace of H^* contained in NA(H,R). Hence NA(H,Y) is dense for every finite-dimensional Y.

**Proof.**
- Linearity is clear.
- Density.
  - Let psi be in H^*. By Hahn-Banach, psi extends to L_1(nu) with the same norm. By sigma-finiteness the extension is given by some h in L_inf(nu).
  - Choose a finitely valued h' with ||h - h'||_inf <= eps. Then ||psi - phi_{h'}||_{H^*} <= eps.
- Attainment.
  - The map Theta = (h, w_1, ..., w_k) from Omega to R^{k+1} takes values in a finite set V. Let P_v = Theta^{-1}(v) for v in V.
  - Let V_+ be the set of v with nu(P_v) > 0. For each such v choose Q_v contained in P_v with 0 < nu(Q_v) < infinity.
  - Let K be the set of c in R^{V_+} with sum_v |c_v| <= 1 and sum_v (w_j)_v c_v = 0 for all j. K is a compact polytope.
  - Upper bound. For u in B_H put c_v = integral of u over P_v. Then:
    - sum_v |c_v| <= ||u||_1 <= 1;
    - sum_v (w_j)_v c_v = integral of w_j u = 0, so c lies in K;
    - phi_h(u) = sum_v h_v c_v.
    Hence ||phi_h|| <= max over c in K of sum_v h_v c_v.
  - Lower bound. For c in K put u_c = sum_v c_v 1_{Q_v} / nu(Q_v). Then:
    - ||u_c||_1 = sum_v |c_v| <= 1;
    - integral of w_j u_c = sum_v (w_j)_v c_v = 0, so u_c lies in B_H;
    - phi_h(u_c) = sum_v h_v c_v.
  - So ||phi_h|| equals the maximum of a linear function over the compact set K. It is attained at u_{c*} for a maximizer c*. QED

**Application to R-trees (SKETCH; it relies on the explicit derivative form of Godard's isometry, [M]).**
- Let M be a closed subset of an R-tree.
- Suppose the set B of branching points of conv(M) that are not in M is finite, and each b in B has finitely many adjacent gaps in M cup B.
- Then F(M) = {mu in F(M cup B) : <1_b, mu> = 0 for all b in B}:
  - the annihilator of F(M) in Lip_0(M cup B) is spanned by the indicators 1_b, which are Lipschitz because B is finite and M is closed;
  - F(M cup B) is isometric to L_1(nu) by Godard.
- Under the derivative representation, 1_b corresponds to the finitely valued function equal to +-1/length on the gaps adjacent to b.
- Lemma H then gives dense lineability. Proposition S covers stars without using Godard.

### 3.3 Proposition FU (finite disjoint unions of compacta): PROVED

**Statement.**
- Let M = M_1 cup ... cup M_n, with the M_i compact and pairwise disjoint. Fix o_i in M_i.
- Suppose each NA(F(M_i),R) contains a norm-dense linear subspace V_i of Lip_0(M_i, o_i).

Then V = {f in Lip_0(M) : f|M_i - f(o_i) lies in V_i for all i} is a dense linear subspace of Lip_0(M) contained in NA(F(M),R).

**Proof.**
- Linearity is clear.
- Attainment.
  - Lip(f) is the larger of max_i Lip(f|M_i) and the cross suprema sup over x in M_i, y in M_j of |f(x) - f(y)|/d(x,y), for i != j.
  - Each cross supremum is the maximum of a continuous function on the compact set M_i x M_j, since distances there are at least delta = min over i != j of dist(M_i, M_j) > 0. If it is the largest term, f attains its norm at a molecule.
  - Otherwise Lip(f) = Lip(f|M_i) for some i. Then f|M_i - f(o_i) lies in V_i, so it attains its norm at some mu in S_{F(M_i)}, which is contained in F(M). Constants vanish on F(M_i), so f attains its norm at mu.
- Density.
  - Given f and eps, choose v_i in V_i with Lip(f|M_i - f(o_i) - v_i) <= eps, and put f_1 = f(o_i) + v_i on M_i.
  - On M_i, |(f - f_1)(x)| <= eps diam(M_i).
  - For x in M_i, y in M_j, i != j: |(f - f_1)(x) - (f - f_1)(y)| <= eps(diam M_i + diam M_j) <= (2 eps D/delta) d(x,y), where D is the largest diameter.
  - So Lip(f - f_1) <= eps max(1, 2D/delta). Subtract the constant f_1(base point) to land in Lip_0(M). QED

**Examples.** Finite disjoint unions of C^1 simple arcs and closed curves (Proposition C), and of compact subsets of R (Proposition 2.3). Countable unions are not covered: Example U2 is a countable union of points.

### 3.4 Remark NI (the R^d inclusion problem does not depend on the norm): PROVED

Let N be any norm on R^d, with dual norm N^*.

(a) **Lip_N(f) = ess sup N^*(grad f) for Lipschitz f on R^d.**
- Lower bound: at a differentiability point p, Lip_N(f) >= |grad f(p) . v| / N(v) for every v, so Lip_N(f) >= N^*(grad f(p)).
- Upper bound: fix x != y. For almost every z, the function t -> f(x + z + t(y - x)) has derivative grad f . (y - x) at almost every t (Rademacher and Fubini). Hence |f(y+z) - f(x+z)| <= (ess sup N^*(grad f)) N(y - x). Let z -> 0 and use continuity.

(b) **V_fin is contained in NA(F(R^d,N),R).**
- If grad f takes finitely many values, pick a value a with N^*(a) = Lip_N(f) that is taken on a set S with 0 < lambda(S) < infinity.
- Pick J with N(J) = 1 and a . J = N^*(a). Let u = 1_S J / lambda(S).
- Lambda_u lies in F(R^d,N): the weak*-continuity argument of Lemma R1 does not use the norm.
- ||Lambda_u|| <= integral of N(u) = 1, and Lambda_u(f) = N^*(a) = Lip_N(f).

(c) **Density of V_fin in Lip_0(R^d,N) does not depend on N.** If c|x| <= N(x) <= C|x|, then for every Lipschitz h: (1/C) Lip_|.|(h) <= Lip_N(h) <= (1/c) Lip_|.|(h). QED

**Consequence.** A positive answer to OQ2 in dimension d would give density of NA(F(E),Y) for every d-dimensional normed space E and every finite-dimensional Y, via Lemma L. This includes polyhedral E such as l_1^2 and l_inf^2, whose free spaces also contain L_1.

### 3.5 Remark R4' (correct form of R4): PROVED

**Statement.**
- Let gamma: [0,l] -> X be C^1 with ||gamma'|| = 1 everywhere.
- Let gamma^ : F([0,l]) = L_1[0,l] -> F(X) be its linearization.
- Suppose T_G attains its norm at gamma^(nu) with ||nu||_1 = ||gamma^(nu)|| = 1. Let y* be norming and phi = y* o G.

Then G is in DNA(X,Y).

**Proof.**
- We have integral of (phi o gamma)' nu = L and |(phi o gamma)'| <= L. Together these force (phi o gamma)' = L sign(nu) almost everywhere on {nu != 0}.
- Suppose {(phi o gamma)' = L} has positive measure (otherwise use -gamma'). Let s_0 be a density point of it.
- The difference quotient (phi o gamma(s_0 + h) - phi o gamma(s_0))/h tends to L.
- Since gamma(s_0 + h) = gamma(s_0) + h gamma'(s_0) + o(h) and phi is L-Lipschitz, (phi(gamma(s_0) + h gamma'(s_0)) - phi(gamma(s_0)))/h also tends to L.
- So G is in DNA with direction gamma'(s_0) and functional y*. QED

**Scope.** This covers segments and isometric curves, where every element of F(gamma([0,l])) has such a representation. It does not cover arbitrary elements of F(gamma(I)) when gamma is curved.

## 4. What remains open after this report

- **OQ1 (main question): OPEN.** Is NA(F(M),Y) dense for every complete pointed M and every finite-dimensional Y?
  - A negative answer refutes property B of Y, which answers Johnson-Wolfe.
  - A positive Johnson-Wolfe answer implies a positive answer here.
  - The converse is open, because the transfer below is open.
- **OQ2: OPEN.** Is V_fin (functions with finitely valued gradients) dense in Lip_0(R^2)?
  - By Remark NI the question does not depend on the norm, and a positive answer would settle F(E) for every 2-dimensional normed space E.
  - Test cases: laminates are proved; the uniformly continuous gradient case (ii) is a credible SKETCH; general measurable gradients are open.
- **OQ3: OPEN.** Does T_G in NA(F(X),Y) force G to be in DNA (question Q-dir)? Is there a full transfer from F(X) to X?
  - Added by the referee: no implication between density for X and density for F(X) is known, in either direction.
  - In particular "NA(X,Y) dense => NA(F(X),Y) dense" is open even for X = l_2^2 (this is OQ2).
- **OQ4.**
  - SETTLED by Proposition S: infinite stars with the centre removed and with bounded, well-ordered inner radii, including the explorer's example (legs [1/2,1]).
  - SETTLED by Proposition FU: finite disjoint unions of compacta that each have dense lineability.
  - Still open:
    - stars whose inner radii strictly decrease, with non-degenerate legs;
    - R-trees missing infinitely many branching points, or a branching point with infinitely many distinct adjacent gap lengths;
    - curves with corners, for example the boundary of the square in l_2^2, or an L-shaped arc. For an L-shaped arc in l_2^2, F(M) contains L_1 and M is not a subset of an R-tree. Moreover the finitely-valued-derivative subspace is not contained in NA, because cross slopes at the corner can approach the supremum without attaining it. This is the simplest compact case where every tool in the notes fails;
    - general uniformly discrete M (Example U2): dense lineability is open, although density is known;
    - countable unions.
- **OQ5 and OQ6: OPEN.** OQ5 asks about inheritance by 1-complemented subspaces and by 1-Lipschitz retracts. OQ6 asks for dense directional-attaining subspaces for Martin's space.

## 5. Corrected verdict

**OPEN.** The explorer's verdict stands.

There is no counterexample. Density for all F(M) is not proved. Equivalence with Johnson-Wolfe is not proved, because it would need the transfer (Q-dir), which remains open.

## 6. Required edits to the notes

1. In R4, DT2 and 5.2, restrict "F(C^1 curves)" to attaining elements gamma^(nu) with ||nu||_1 = ||gamma^(nu)||, as in Remark R4'.
2. In the summary and 5.4, replace "F(X) is at least as good a counterexample candidate as X" and "F(XX) is not a better candidate than XX" by the precise statement of DT2. Add that neither implication between density for X and density for F(X) is known (compare X = l_2^2).
3. Credit Proposition N to CCGMR 2019 (non-density of SNA for length spaces) and KMS 2016 (Y = R).
4. In 3.4, change "reduces to" to "would follow from".
5. In 1.1, change "give F(M) a separable dual" to "make F(M) a separable dual space".
6. In 1.2, correct the author list of arXiv 2312.00393 (Choi, Jung, Lee, Roldan) and drop the unverified "no isometric c_0" sentence.
7. In 2.4 CAVEAT and OQ4, mark the infinite-star example as settled (Proposition S).
8. In 2.6, note that dense lineability is preserved only by FINITE wedge sums, as far as proved.
9. Add Bachir, arXiv 2304.12611, as a possibly relevant reference, with details unverified.

<!-- END -->
