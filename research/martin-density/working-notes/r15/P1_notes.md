# P1 notes (round 15) — Problem R as a NEGATIVE target: free-coordinate oscillation carried by small-margin peaks

Task: find admissible T, N, a row f, g in C(f), rho < 1 and free coordinates j, j' of f whose oscillation is carried only by
small-margin peaks of f, and prove dist(rho g, C(f')) >= c > 0 for ALL norm-attaining f' near f (or find the approximant
family that breaks it). Setting throughout: one block (N = 1). Sources: BRIEFING_R2 (Addenda 13, 14a/b, NEG), neg/N1-N3
(+ referee notes), Part I. Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Part files: P1_part1.md ... P1_part5.md
(reproduced below); scripts: P1_work/ (anchored_model.py, mf_model.py, run*.py, mf_run*.py).

## 0. Answer

요약 (Korean). Problem R의 negative 목표는 달성되지 않았다. 대신 (1) 모든 행(row)에서 성립하는 새로운 엄밀한 도구를
증명했다: 지지집합 밖에서는 base를 대칭적으로(양쪽 같은 부호로) 쓸 수 없다는 Lemma SYM, 척도 간 일관성 Lemma P, 그리고
strict non-peak/degenerate peak의 진동 용량이 무게가 아니라 "개수"(진동 프로파일의 l_2 노름)로 정해진다는 용량 정리 C2와
따름정리 C3. (2) 이로부터 회복하는 NA 근사열은 Z를 보는 깊은 strict non-peak를 반드시 가져야 함을 증명했다(명제 N).
(3) 그리고 Problem R을 깨는 근사열 족을 정확히 기술했다: KSB(keep-shift-bank) — f의 staircase를 깊이 L까지 유지하고,
Z 위의 공통 이동으로 깊이 ~L의 carrier 하나를 deep-kernel strict non-peak로 만들고, 그 접촉좌표에 작은 은행을 두어
깨끗한 대칭 carrier로 만든다. 하나의 strict non-peak가 그보다 작은 모든 척도를 한꺼번에 덮으므로, N3 심판이 예상한
"무한히 많은 near-threshold carrier의 nested tuning"이 필요 없다. 유한 SOCP 모형에서 KSB는 rho g를 회복하고(거리가 L과
함께 0으로 감소) 단순 절단은 실패한다. 따라서 sqrt-무게 용량 법칙은 근사열을 따라 균일하지 않을 것으로 보인다(모형 수준의 증거, 엄밀한 반증은 아님).
남은 negative 경로는 접합 척도에서의 용량 상수 비교뿐이며, 모든 시험 모형에서 근사열이 이긴다. 판단: positive 쪽.

ANSWER (English).
 1. NEGATIVE TARGET NOT ACHIEVED. No (T, f, g, rho) with a non-recovery proof. Every obstruction mechanism examined
    (contact-anchored staircases, misaligned multi-family staircases, Diophantine schedules, dimension counting against
    combinations) reduces to a capacity comparison at a single junction depth, which the approximant wins in all models.
 2. NEW PROVED TOOLS (valid at EVERY row, NA or not; no tameness):
    - Lemma SYM: off the support F', same-sign ("symmetric") base usage on the two sides of a scale-t pair has total
      l_1 mass <= e/(c't) = O(t); Corollary SYM': a block combination used identically on both sides must reproduce the mate
      up to O(t) on all coordinates off F' (contacts included).
    - Lemma P: block parts at two scales agree on free coordinates up to (t_1 + t_2)/(2c') (room-weighted).
    - Theorem C2 (l_2-count capacity bound): the Z-oscillation of every mate is bounded at each scale t by a base term O(t),
      a peak term sum_{P°} min(t/(2mu_k), 5Phi_k/t)|ell_k|, an l_2 term (kappa_2 + E°)(C'^2/C'^2_{P°}) ||ell 1_{N', Phi >= st}||_2
      over strict non-peaks and degenerate peaks, and a deep tail; kappa_2 = (0.434/sigma')^{1/2}.
    - Corollary C3: at rows margin-sparse at Z, every mate's oscillation is <= const * ||ell 1_{N'}||_2 (COUNT, not weight).
      Generalizes N3-ref Cor 2.4' (which needed N' to see nothing).
    - Proposition N: recovering margin-sparse NA approximants must contain strict non-peaks/degenerate peaks seeing Z with
      l_2-mass of oscillation profiles bounded below; in the Problem-R situation their depth tends to infinity.
 3. BREAKING FAMILY (positive mechanism for Problem R; SKETCH + model evidence): KSB approximants (Sec. 5.3). One clean
    deep-kernel strict non-peak per approximant (made from f's own near-threshold carrier by a common shift of z' on Z,
    contact parts banked) covers all scales below the junction; above, the kept staircase works as at f.
    Consequently the "sqrt-weight capacity law" is expected NOT to be uniform along NA sequences (the KSB strict non-peak
    has weight -> 0 but O(1) capacity; the law's rate term degenerates with the kept staircase). HEURISTIC (model-level;
    the mechanism is explicit; not a rigorous disproof).
 4. Leaning: POSITIVE (density more likely), low-to-moderate confidence. Problem R is not a source of non-density in the
    designs examined; the decisive open point for a negative proof would be a design forcing a junction-capacity deficiency
    (R2 of Sec. 5.4), for which there is no candidate.

| # | Result | Status | Where |
|---|---|---|---|
| 1 | Lemma SYM (no symmetric base usage off F'), Cor SYM' | PROVED | 4.1 |
| 2 | Lemma P (cross-scale consistency on J') | PROVED | 4.2 (1.3) |
| 3 | Theorem C2 (l_2-count capacity bound, every row) | PROVED | 4.3 |
| 4 | Corollary C3 (count capacity at margin-sparse rows) | PROVED | 4.3 |
| 5 | Proposition N (recovering approximants need deep carriers seeing Z) | PROVED | 5.1 |
| 6 | Single-scale capacity bounds cannot certify non-recovery against deep strict non-peaks | HEURISTIC (reading of Prop N/C3: capacity is a count, not a weight) | 5.1 |
| 7 | Cleanliness of usable deep carriers (hand-over at scale ~Phi) | SKETCH | 5.2, 2.2(f) |
| 8 | Anchored design D_anch: f's mates exist (staircase through contacts) | HEURISTIC (model: yes; sign convention forced) | 2.1, 3.1 |
| 9 | KSB approximants recover rho g in D_anch (1 and 2 misaligned families) | HEURISTIC (model) | 3.2, 5.3 |
| 10 | Uniform sqrt-weight capacity law along NA sequences | HEURISTIC: expected FALSE (KSB mechanism explicit; model evidence; not disproved rigorously) | 5.3 |
| 11 | Dimension count against clean combinations of non-anchored carriers | HEURISTIC | 2.2(e) |
| 12 | Junction-capacity deficiency (route R2 to non-density) | OPEN; contradicted by all models | 5.4 |
| 13 | Problem R (negative) | OPEN; no candidate survives | 5.4 |
| 14 | Non-margin-sparse NA approximants (staircases at f') need near-duplicate families on a cofinite set | HEURISTIC | 2.3 R-iii |

---

# P1 part 4 — rigorous tools: symmetric usage, cross-scale consistency, l_2-count capacity bound

Setting: one block (I = {1}, the norm p_1), T admissible, lambda_k = Phi_k = 2^{-1-k} q*(Te_k) <= 2^{-1-k}, so
||Phi||_2^2 <= 1/12. A "row" is any f' in S_{p*} (norm attaining or not) with forced data (Part I prop:forced): normer
theta' (an element of the bidual ball; for NA rows the normer x'), c' := q**(theta') = q_0', a', F' = supp a', z', w', M', C',
sigma' = |zeta'| with zeta' = R** theta', alpha', P' (peaks), Q' (strict non-peaks), margins mu'_k (k in P'),
Dg' = {k in P' : mu'_k = 0} (degenerate peaks), P° := P' \ Dg', N' := Q' u Dg', psi' := L* w'. J' := {j notin F' : |z'_j| < 1},
room r_j := 1 - |z'_j|. g' in C(f'), t in (0,1], e := s(t) - 1 <= t^2/2. A scale-t pair is (B+, Omega+; B-, Omega-) with
f' + t g' = (a' + tB+) + L*(w' + t Omega+), f' - t g' = (a' - tB-) + L*(w' - t Omega-), all four norms <= 1 + e
(exists: N3 Def 1.1, PROVED). Notation: for x real, x_+ = max(x,0), x_- = max(-x,0).

Facts used (all refereed): N3 Lemma 1.2 (switching budget) in the form
 (a) sum_{j notin F'} [ (1-|z'_j|)|B+_j| + 2 (z'_j B+_j)_- ] + sum_{F'} 2 (z'_j B+_j + |a'_j|/t)_-  <=  e/(c' t),
 (b) sum_{j notin F'} [ (1-|z'_j|)|B-_j| + 2 (z'_j B-_j)_+ ] + sum_{F'} 2 (z'_j B-_j - |a'_j|/t)_+  <=  e/(c' t),
 and the inequality c' G_b + sigma' G(W) <= e (N3 proof of Lemma 1.2) for W = w' + t Omega+ (and W = w' - t Omega-), where
 G(W) := N(W) - 1 - <zeta'/sigma', W - w'> >= 0; N3 Lemma 2.2 (collective motion): L+ := sup_{P'} s_k Omega+(k)
 (s_k := sgn w'(k)) satisfies |L+| <= (2+e)/t and Omega+(k) = s_k (L+ - eps_k) on P' with 0 <= eps_k <= e/(t sigma'|alpha'(k)|)
 for alpha'(k) != 0; eq. (margin): sigma'|alpha'(k)| = Phi_k mu'_k.

## 4.1 LEMMA SYM (no symmetric base usage off the support).  PROVED.
For every row f', g' in C(f'), t > 0 and scale-t pair:
      sum_{ j notin F' : B+_j B-_j >= 0 }  min(|B+_j|, |B-_j|)  <=  e/(c' t)  (<= t/(2c')).
Proof. Fix j notin F' with B+_j B-_j >= 0 and put m := min(|B+_j|, |B-_j|), x := |z'_j| in [0,1]. Its contribution to the
sum of the left sides of (a) and (b) is at least (1-x)(|B+_j| + |B-_j|) + 2(z'_j B+_j)_- + 2(z'_j B-_j)_+. If z'_j = 0 this
is >= 2m. Otherwise B+_j and B-_j have a common sign sigma (or one of them vanishes, then m = 0); if sigma = sgn z'_j then
(z'_j B-_j)_+ = x|B-_j| >= x m, and if sigma = -sgn z'_j then (z'_j B+_j)_- = x|B+_j| >= x m. In both cases the contribution
is >= 2(1-x)m + 2x m = 2m. Adding (a) and (b) gives sum 2m <= 2e/(c' t).  QED
READING. Off F' (in particular on contacts, near-contacts and free coordinates) the base can only be used in a SWITCHING
way (opposite signs on the two sides); same-sign usage has total l_1-mass O(t). Two-sided usage is possible only on F'
(support, banks), within the anti-sign allowance |a'_j|/t.
COROLLARY SYM' (symmetric block usage pins the carriers to the mate). If at a coordinate j notin F' the block parts of the
two sides agree, (L*Omega+)(j) = (L*Omega-)(j) =: X_j, then B+_j = B-_j = g'_j - X_j, and summing over such j:
      sum_{ j notin F' : (L*Omega+)(j) = (L*Omega-)(j) } |g'_j - X_j|  <=  e/(c' t).
So a carrier combination used identically on both sides (strict non-peaks used "symmetrically") must reproduce g' up to
O(t) in l_1 on all coordinates off F' — contacts included. PROVED (immediate from Lemma SYM).

## 4.2 LEMMA P (cross-scale consistency on free coordinates).  PROVED.
For every row f', g' in C(f'), 0 < t_1, t_2 <= 1 and scale-t_i pairs (B^{+-}_i, Omega^{+-}_i):
      sum_{j in J'} (1-|z'_j|) |(L*Omega^{s}_1)(j) - (L*Omega^{s'}_2)(j)|  <=  (t_1 + t_2)/(2c')     (s, s' in {+,-}).
Proof. g' = B^s_i + L*Omega^s_i, so the difference of block parts equals B^{s'}_2 - B^s_1 coordinatewise; by (a), (b),
sum_{J'} (1-|z'_j|)|B^s_i(j)| <= e_i/(c' t_i) <= t_i/(2c'). Triangle inequality.  QED

## 4.3 THEOREM C2 (l_2-count capacity bound at every row).  PROVED.
Let Z = {j, j'} subset J', Lambda'(h) := h_j psi'_{j'} - h_{j'} psi'_j (so Lambda'(psi') = 0), ell_k := Lambda'(u_k).
For k in P° put m_k(t) := min{ t/(2 mu'_k), 5 Phi_k / t }, and E°(t) := (sum_{P°} m_k(t)^2)^{1/2} (possibly infinite).
Let C'_{P°} := ||D w' 1_{P°}||_2 = M' ||Phi 1_{P°}||_2 (> 0 since ||alpha'||_1 = 1 forces P° != empty) and
kappa_2 := (0.434/sigma')^{1/2}. Then for every g' in C(f'), t in (0,1] and s in (0,1]:
 |Lambda'(g')| <= (t/(2c')) (|psi'_{j'}|/r_j + |psi'_j|/r_{j'}) + sum_{k in P°} m_k(t) |ell_k|
                 + (kappa_2 + E°(t)) (C'^2 / C'^2_{P°}) ( sum_{k in N', Phi_k >= s t} ell_k^2 )^{1/2}
                 + (5/t) sum_{k in N', Phi_k < s t} Phi_k |ell_k|.
Proof. Step 1 (base on Z). g'_i = B+_i + (L*Omega+)(i) for i in Z. By (a), |B+_i| <= t/(2c' r_i), hence
 |Lambda'(B+)| <= (t/(2c'))(|psi'_{j'}|/r_j + |psi'_j|/r_{j'}).
Step 2 (block identity). Put Theta := Omega+ - (L+/M') w'. Then L*Omega+ = (L+/M') psi' + L*Theta and
 Lambda'(L*Omega+) = Lambda'(L*Theta) = sum_k Phi_k Theta(k) ell_k (absolutely convergent: |Theta(k)| <= 5/t below and
 sum Phi_k |ell_k| < infinity). On P': Theta(k) = s_k(L+ - eps_k) - (L+/M') s_k M' = -s_k eps_k, with eps_k >= 0 and
 eps_k <= ||Omega+||_inf + |L+| <= 2(2+e)/t <= 5/t (||Omega+||_inf <= (||w' + tOmega+||_inf + ||w'||_inf)/t <= (2+e)/t).
 On Q': |Theta(k)| <= ||Omega+||_inf + |L+| |w'(k)|/M' <= 5/t. For k in P°: Phi_k eps_k <= e/(t mu'_k) <= t/(2 mu'_k)
 (collective motion + margin identity) and Phi_k eps_k <= 5 Phi_k/t; so Phi_k eps_k <= m_k(t).
Step 3 (l_2 control). With W = w' + t Omega+: G(W) = [||W||_inf - <alpha', W>] + [||DW||_2 - <Dw'/C', DW>] since
 <zeta'/sigma', W> = <alpha', W> + <Dw'/C', DW> and <zeta'/sigma', w'> = 1 (Part I lem:threshold). Both brackets are >= 0;
 for the second, with e_w := Dw'/C' (unit) and X := DW: ||X|| - <e_w, X> = ||P_perp X||^2/(||X|| + <e_w,X>) >= ||P_perp X||^2/(2||X||),
 P_perp the projection onto e_w^perp, and P_perp X = t P_perp D Omega+. Moreover ||X|| <= ||Phi||_2 ||W||_inf <= (1+e)/sqrt(12) <= 0.434.
 With sigma' G(W) <= e <= t^2/2 this gives ||P_perp D Omega+||_2^2 <= 0.434/sigma' = kappa_2^2.
Step 4 (strict non-peaks and degenerate peaks). D Theta = D Omega+ - (L+/M') D w', so P_perp D Theta = P_perp D Omega+.
 Split D Theta = Y + Y° with Y := (D Theta) 1_{N'} and Y° := (D Theta) 1_{P°} = -D(s eps) 1_{P°}; ||Y°||_2 <= E°(t).
 Hence ||P_perp Y||_2 <= kappa_2 + E°(t). Write Y = P_perp Y + <Y, e_w> e_w; restricting to N' (Y lives on N') and pairing with
 e_w 1_{N'}: <Y, e_w>(1 - ||e_w 1_{N'}||^2) = <P_perp Y, e_w 1_{N'}>, so |<Y, e_w>| <= ||P_perp Y|| ||e_w 1_{N'}|| / (1 - ||e_w 1_{N'}||^2)
 and ||Y|| <= ||P_perp Y|| / (1 - ||e_w 1_{N'}||^2). Since ||e_w 1_{N'}||^2 = 1 - C'^2_{P°}/C'^2 (the D-mass of w' splits over
 N' and P°), ||Y||_2 <= (kappa_2 + E°(t)) C'^2/C'^2_{P°}.
Step 5 (assembly). Lambda'(L*Theta) = -sum_{P°} Phi_k s_k eps_k ell_k + sum_{N', Phi_k >= st} Y_k ell_k + sum_{N', Phi_k < st} Phi_k Theta(k) ell_k;
 bound the first by sum m_k(t)|ell_k|, the second by Cauchy-Schwarz, the third by (5/t) sum Phi_k |ell_k|. Add Step 1.  QED

COROLLARY C3 (small-scale capacity of a row).  PROVED.  Suppose t_n -> 0 with sum_{P°} m_k(t_n)|ell_k| -> 0 and E°(t_n)
bounded by E_inf. Then every g' in C(f') satisfies
      |Lambda'(g')| <= (kappa_2 + E_inf) (C'^2/C'^2_{P°}) ( sum_{k in N'} ell_k^2 )^{1/2}.
In particular (N' sees no oscillation, i.e. ell_k = 0 on N'): g' is proportional to psi' on Z.
Proof. Apply C2 with t = t_n and s_n := 1/log_2^2(1/t_n). Since Phi_k <= 2^{-1-k},
 sum_{Phi_k < s t} Phi_k <= sum_k min(2^{-1-k}, st) <= st (log_2(1/(st)) + 1), so the last term is
 <= 5 s_n (log_2(1/(s_n t_n)) + 1) max_k |ell_k| -> 0; the base term -> 0; the l_2 sums increase to sum_{N'} ell_k^2.  QED
Remarks. (i) The hypothesis on P° is a margin-sparsity condition at Z. SKETCH: it holds under N3-ref's log^2 rate (same
 choice of mu_0 = mu_0(t) as in the proof of Cor 2.4', splitting P° at margin mu_0; not written out), and it fails when
 small-margin peaks seeing Z occur at almost all depths (staircases). It is never automatic: by N3-ref Lemma R-V(c)
 every row has infinitely many near-kernel carriers seeing Z, so it is a sparse-visit property of T relative to the
 normer (for the KSB rows of 5.3 it is an assumption on T, compatible with Lemma B; cf. N3-ref Cor 2.4' Remark (ii)).
 (ii) Unlike N3 Thm 2.3' (strict non-peaks counted by weight/t), strict non-peaks and degenerate peaks enter C3 by COUNT
 (l_2-norm of their oscillation profiles), independent of their weights: a single deep strict non-peak seeing Z can carry
 oscillation of order kappa_2 |ell_k| at all small scales — which is what NA approximants exploit (part 5).
 (iii) C2 is single-scale; combined with Lemma SYM and Lemma P it controls which carriers can be used at different scales.

---

# P1 part 5 — what recovering approximants must contain, and the breaking family for Problem R

## 5.1 Necessary condition (PROVED, from C3 + status continuity)
PROPOSITION N. Let f in S_{p*} (one block), g in C(f), rho in (0,1), Z = {j, j'} subset J(f), Lambda(g) := g_j psi_{j'} - g_{j'} psi_j
!= 0. Let f'_n -> f be NA rows and g'_n in C(f'_n) with g'_n -> rho g. Suppose every f'_n satisfies the hypothesis of
Corollary C3 (small-margin peak capacity at Z vanishing along some t -> 0, with E° bounded by E_inf, uniformly in n).
Then for all large n
      ( sum_{k in N'_n} Lambda'_n(u_k)^2 )^{1/2}  >=  rho |Lambda(g)| / ( 2 (kappa_2(f'_n) + E_inf) C_n'^2 / C'^2_{n,P°} ),
i.e. the approximants must carry strict non-peaks or degenerate peaks seeing Z with l_2-mass of oscillation profiles
bounded below. If moreover no strict non-peak or degenerate peak of f sees Z (the Problem-R situation), these carriers
have depth -> infinity (for every finite set Lambda of carriers, N'_n n Lambda contains no carrier seeing Z for large n).
Proof. Lambda'_n(g'_n) -> rho Lambda(g) (psi'_n -> psi in l_1 by Part I prop:continuity, g'_n -> rho g), so
|Lambda'_n(g'_n)| >= rho|Lambda(g)|/2 for large n; apply C3 to g'_n at f'_n. The depth statement is status continuity
(N3-ref Sec. 5): a fixed carrier that is a peak with positive margin at f is a peak with positive margin at f'_n for large n.
(kappa_2(f'_n) = (0.434/sigma'_n)^{1/2} -> (0.434/sigma)^{1/2} and C'_{n,P°} is bounded below along the sequence because
the shallow robust peaks of f stay robust peaks.)  QED
READING. Unlike N3 Thm 2.3' (weights) this is a COUNT condition: one deep carrier per approximant suffices for the
necessary condition. Hence no single-scale capacity bound can certify non-recovery against approximants that can create
deep strict non-peaks seeing Z; a negative proof must exploit cross-scale consistency (Lemma P) and the impossibility of
symmetric base usage off F' (Lemma SYM), i.e. CLEANLINESS of the deep carriers.

## 5.2 Cleanliness (SKETCH)
A strict non-peak k used at all scales t <= t_k (t_k ~ Phi_k gamma_k / c_k, c_k = its coefficient) with the same coefficient on
both sides contributes c_k u_k to the block parts of both sides; by Corollary SYM' its whole vector off F' must be reproduced
by g' up to O(t), and by Lemma P its J'-profile must be reproduced, at the hand-over scale ~ t_k, by the carriers used above
t_k, up to O(t_k) (room-weighted). Since the slack covers only |t| >= 6 eta/(1-rho^2) (N1 Prop 1.8, eta = p*(g' - rho g)),
the hand-over cannot be pushed to the slack unless the pollution is O(t_k). So deep carriers usable for rho g are
(i) strict non-peaks (or combinations) whose off-F' parts are O(Phi)-close to what the large-scale structure produces,
with their contact parts on F' (banks). Approximants can make such carriers from f's own near-threshold carriers:

## 5.3 The breaking family KSB (keep-shift-bank). Precise description; recovery: model-level evidence (HEURISTIC),
## general statement OPEN.
Data: f with a family A of near-threshold peaks carrying the Z-oscillation, pairwise near-duplicates on J(f) (forced by
Lemma P at f), each with off-J part on contacts K(f) and support F(f) (forced by Lemma SYM at f: off F the base absorbs
only switching usage, so the carriers' off-J parts must sit where f's base absorbs them, i.e. on K u F).
Approximant f'_{L,delta} := grad p(y'), y' = z' + U(U*a'/||U*a'||), with
 (K) z' = z on a window containing Z, F(f) and the contact parts of all carriers of A of depth < L (kept staircase);
 (S) a common shift of z' on Z of size delta = O(Phi_{k_0}) chosen so that one carrier k_0 in A of depth ~ L has
     u_{k_0}(y') = 0 (deep-kernel strict non-peak). Possible because all carriers of A see Z with a common profile;
 (B) banks of tiny mass (>= c Phi_{k_0}) on the (finitely many, up to an l_1-tail << Phi_{k_0}) contact coordinates of
     u_{k_0}, with the contact signs (so u_{k_0}(y') is unchanged and its off-J part lies on F', where two-sided base usage
     is allowed below the bank capacity scale (N3 Prop 1.8)); a' -> a in l_1;
 (D) z' := 0 (or any c_0 choice) beyond the window: deeper carriers of A are destroyed (robust).
Then f'_{L,delta} -> f as L -> infinity (Part I prop:approximants). Mechanism: above depth L the kept staircase carries
rho g in switching mode as at f (scales >= ~Phi_L); below, the clean symmetric strict non-peak k_0 carries it at all scales
<= ~Phi_{k_0} (Corollary C3 count capacity kappa_2 |ell_{k_0}|; Lemma SYM satisfied since its off-J part is on banks).
Model evidence (P1_part3, run7, mf_run2): distance_{l1}(rho g_f, C(f'_KSB)) for rho = 0.9 decreases with L
 (one family: 0.093, 0.030, 0.012 at L = 4, 6, 8; two misaligned families: 0.162, 0.062, 0.003), while canonical-type
 truncations stay far (0.275, 0.225 / 0.336, 0.146) until boundary effects; a single banked band strict non-peak has
 per-scale capacity >= f's staircase in every tested parameter set (ratios 1.03-1.18; K = 1.5..5, tau = 0.25..1).

## 5.4 Status of Problem R (negative target)
 * No admissible T, f, g, rho with a proof of non-recovery was found. Every candidate obstruction met here reduces to a
   junction capacity comparison at the depth of the approximant's conversion (one or a few clean strict non-peaks vs. the
   kept staircase), which the approximant wins in all tested models.
 * What a negative proof would have to show (precise residual, OPEN): for some design, at EVERY NA row near f, either
   (R1) no clean strict non-peak seeing Z can be created near any junction depth — impossible for staircase-carried
        oscillations by 5.3 (S),(B) as long as the carriers' off-J parts are bankable (always true up to small tails), or
   (R2) the junction capacity is uniformly deficient by a factor < rho — contradicted by the models (a single clean strict
        non-peak already matches the staircase), and the "duality" (small margins <=> wide shift band, many conversions)
        suggests it fails generally (HEURISTIC), or
   (R3) the oscillation is carried at f by structure that is not a near-duplicate family on J (impossible by Lemma P at f
        when it is carried by small-margin peaks at all scales in switching mode: HEURISTIC, needs a proof that switching
        through non-duplicates leaks).
 * Leaning: positive (Problem R is not a source of non-density in the designs examined; the KSB family is the
   positive mechanism the N3 referee anticipated — "re-create weak-peak freedom at free coordinates at every scale below the
   slack scale" — realised not by nested tuning of infinitely many near-threshold carriers but by ONE clean deep-kernel
   strict non-peak per approximant, which covers all smaller scales at once).

---

# P1 part 1 — context digest and first structural observations (Problem R, negative target)

Setting: one block (N = 1), lambda_k = Phi(k) <= 2^{-1-k}, u_k = T e_k / q*(T e_k), psi := R* w. Notation of Part I / N3.
Z = {j, j'} free coordinates of f (|z_j|, |z_j'| < 1). Oscillation functional of h in X*:
  Lambda_Z(h) := h_j psi_j' - h_j' psi_j  (N3-ref Prop X uses this).

## 1.1 What the tools say (digest; all cited results refereed)
(a) N3 Thm 2.3' (margin-classified profile bound, PROVED at EVERY row): for g' in C(f'), t in (0,1], mu_0 in (0,1]:
    Osc_Z(g';psi') <= t [A_0 + 2(rho_S+1) l(t)/mu_0] + 15 H'(mu_0)/t,  H'(mu_0) = weighted mass of near-kernel carriers
    (strict non-peaks + peaks with margin < mu_0) seeing Z.
(b) N3-ref Lemma R-F (Fatou): liminf_{f'->f} H_{f'}(mu_0) >= H_f(mu_0) for fixed mu_0. Hence every FIXED-threshold bound is
    inherited from f and can never certify non-density.
(c) N1 Prop 1.8 (scale localization): with eps = p*(f'-f), eta = p*(g'-rho g), the mate inequality of g' at f' holds
    automatically for |t| >= t_* = max((6 eps/(1-rho^2))^{1/2}, 6 eta/(1-rho^2)). Only scales t < t_* decide.
(d) N3 Lemma 1.2 at an NA row f' (switching budget): for every scale-t pair, sum_{J'} (1-|z'_i|)(|B+_i| + |B-_i|) <= t/c'.
(e) N3 Thm 1.4 (de-switching): at an NA row, bounded-coefficient switching dies out as t -> 0.
(f) N2 Thm 2.4: the staircase design T_PB (near-threshold peaks u_k ~ h + beta_k e_0, beta_k = -+8 Phi(k), far-rigid) gives
    mates gamma h oscillating on free coordinates {2,3}, carried ONLY by small-margin peaks (Q = empty, no degenerate peaks,
    (MS) fails) — i.e. a Problem-R configuration — and EVERY canonical truncation f_N recovers them exactly (gamma h in C(f_N)).
    Mechanism: the staircase values are decided on the window {2,3} (far rigidity), so truncation preserves the structure.

## 1.2 Consequence for the design of a negative example (HEURISTIC, used as a guide)
A Problem-R counterexample must make f's small-margin peak structure NON-PRESERVABLE by c_0 normers: the near-threshold
carriers of f must take their values from the non-c_0 part of xi (anchoring). Two kinds of anchoring:
 (A-free) on FREE coordinates of f: a carrier used with O(1) coefficient at some scale puts its whole vector into the active
     block part R*Omega_t; by (d) at f itself the active parts at different scales must agree on J up to O(t) (room-weighted).
     So all near-threshold carriers used by g must share their J-profile up to O(Phi): a COMMON far part P. One common
     parameter P(x') can be restored at a c_0 normer (move finitely many far free coordinates): the structure is preserved
     (like T_PB). Not an obstruction.
 (A-contact) on CONTACTS of f: carrier-dependent far parts on K (infinite). At f they are absorbed by one-sided base usage
     on K, which forces SWITCHING use (side + and side - use the carrier differently): one-sided absorption cannot absorb a
     symmetric use (B+ = B- on a contact forces B ~ 0 there). At an NA row only finitely many of these contact blocks can be
     kept (K' finite), so beyond some depth l_0 the anchored carriers are destroyed or become polluting.

## 1.3 The pollution principle at NA rows (PROVED as stated; elementary from (d))
LEMMA P (cross-scale consistency on free coordinates). Let f' be NA, g' in C(f'), 0 < t_1 < t_2 <= 1, and scale-t_i pairs
(B+-_i, Omega+-_i). Then for each sign
   sum_{i in J'} (1 - |z'_i|) |(L*Omega^+_1)(i) - (L*Omega^+_2)(i)| <= (t_1 + t_2)/c'      (and likewise for -, and +/-).
Proof. g' = B^+_1 + L*Omega^+_1 = B^+_2 + L*Omega^+_2, so L*(Omega^+_1 - Omega^+_2) = B^+_2 - B^+_1 on every coordinate;
by (d), sum_{J'}(1-|z'_i|)|B^+_s(i)| <= t_s/c' (half of the budget of (d) is enough). Triangle inequality. QED
READING. At an NA row the block parts used at two scales agree on all free coordinates of f' (a cofinite set) up to
O(max scale). A carrier that is used with an O(1) coefficient at small scales but not at large ones must have (up to
O(scale)) the same J'-profile as the carriers used at the large scales. Carriers whose far parts sit on coordinates that
are free at f' (destroyed contact blocks of f, far free coordinates) are unusable unless all scales use them.

## 1.4 Approximant strategies identified so far (to be tested)
 S1 (preserve-and-convert). Keep z' = z on [1, W_2] (preserving f's anchored carriers up to depth l_0), convert one or a few
    anchored carriers at the junction depth into deep-kernel strict non-peaks by a common window shift of size ~Phi_{l_0}
    (cost eps ~ Phi_{l_0}); a deep-kernel strict non-peak has capacity ~ sqrt(C) |osc| at ALL scales below ~Phi.
    Issue: capacity of finitely many strict non-peaks is bounded by sqrt(C n) |osc| (l_2 cost), while f may carry more per
    scale; and the converted carrier's far part sits on a kept contact (switching only), see 1.2 (A-contact).
    [RESOLVED later: banking the contact makes the converted carrier a clean symmetric carrier (Lemma SYM), and in all
    models ONE such strict non-peak already matches the staircase capacity (part 3, part 5.3).]
 S2 (nested tuning). Re-create near-threshold structure below l_0 with other carriers: requires near-duplicates of the
    J-profile of f's carriers at rate O(Phi) (Lemma P), which the designer can forbid (separation rule).
 S3 (exact far restoration). If the anchoring parameter is common (A-free), restore it (T_PB-type preservation).

---

# P1 part 2 — an anchored candidate design and the approximant's moves (analysis; labels per item)

One block (N = 1), lambda_k = Phi_k. Diagonal U with super-fast decaying entries (U-part levers negligible).

## 2.1 Candidate design D_anch (HEURISTIC design; admissibility to be checked as in N2 Lemma 2.1)
Coordinates: 1 = support (a = abar e_1*), Z = {2,3} free with zhat_2 = zhat_3 = 1/2, 4 = staircase coordinate (free,
zhat_4 != 0), contacts b_k (one private far coordinate per anchored carrier), private signature sets S_k (tiny), generic
coordinates. Oscillation vector h := e_2* - e_3* + (tau/zhat_1) e_1*, so h(zhat) = tau > 0 and h - (tau/zhat_1)e_1* = e_2* - e_3*.
Anchored carriers k in Sigma_+ u Sigma_- (geometric weights inside each family, ratio r):
     u_k = (h + beta_k e_4* + tau s_k e_{b_k}* + delta_k sigma_k) / n_k,   z_{b_k} = -s_k (contact of f),
so u_k(zhat) = (beta_k zhat_4 + small)/n_k: choose beta_k so that |u_k(zhat)| = K vartheta Phi_k (near-threshold peak,
margin (K-1) vartheta Phi_k, sign -s_k as in T_PB). On J (free coordinates of f) all anchored carriers have the SAME profile
h + O(Phi) (near-duplicates on J): f's mates gamma (e_2* - e_3*) are carried by switching staircases as in N2 Prop 2.3, the
contact parts tau s_k e_{b_k}* being absorbed one-sidedly on the contacts b_k (sign condition z_{b_k} = -s_k), and the F-part
(tau/zhat_1)e_1* by the base on F (two-sided). (Mate existence: SKETCH — N2 Prop 2.3 with contacts; to be checked numerically.)
Non-anchored carriers: window errors in GENERIC directions of size >= K_k Phi_k (K_k -> infinity), concentrated far parts
(few coordinates, sizes bounded below), Diophantine schedule of targets relative to xi (values at xi avoid the strict
non-peak band by >= K_k Phi_k for every bank-sign choice), no near-duplicate families modulo finite sets.

## 2.2 What NA approximants can and cannot do (analysis)
 (a) Keeping. Only finitely many contacts b_k can be kept (z' in c_0): f's staircase is preserved down to a finite depth L'.
     Destroyed anchored carriers have value ~ h(zhat')c'/n ~ tau/n: robust; they cannot be used (their contact part sits on a
     free coordinate of f': pollution tau on J', Lemma P).
 (b) Symmetric use needs strict non-peaks (peaks used symmetrically overshoot on one side; LEMMA SYM below). A symmetric
     carrier's whole vector enters g' up to the base: on contacts and near-contacts one-sided base usage cannot absorb a
     symmetric component (LEMMA SYM), on banks it can (below bank capacity, N3 Prop 1.8), on free coordinates only at
     first-order cost (room).
 (c) Inward contact moves (near-contacts) tune anchored carriers individually, but a near-contact is one-sided: symmetric use
     then costs t * room * c tau ~ t * c * (shift) at first order, so these carriers are usable only down to a positive scale.
 (d) The only continuous lever acting on all kept anchored carriers is the common shift delta = h(zhat') - h(zhat) (window
     perturbation); it puts the anchored carriers with Phi_k in (delta/((K+1)vartheta), delta/((K-1)vartheta)) into the strict
     non-peak band (one family). Banking their contacts makes them CLEAN symmetric strict non-peaks (J'-profile h + O(Phi)).
     Their number n_band <= 1 + log((K+1)/(K-1))/log(1/r) (design constant; = 1 for K >= 3, r <= 1/2).
 (e) Window levers orthogonal to h and e_4 tune non-anchored carriers individually (cost ~ shift), far parts give discrete
     (bank-sign) tuning only. Clean symmetric combinations of non-anchored carriers must cancel their generic window errors
     to precision O(Phi) on all free window coordinates: m >= W' + 1 carriers, but tuning m values needs m <= W' - 2 + (far
     tuning coordinates), and each unbanked far tuning coordinate adds one cancellation equation. DIMENSION COUNT: impossible
     for generic data (HEURISTIC; exact/approximate version with precision O(Phi) not proved).
 (f) Why precision O(Phi) and not o(1): the slack covers only |t| >= t_* >= 6 eta/(1-rho^2) (N1 Prop 1.8), and the
     pollution of a symmetric carrier is part of eta = p*(g' - rho g); a symmetric strict non-peak at depth k covers only
     t <~ Phi_k gamma_k / c_k, so a hand-over (to the kept staircase or to the slack) happens at scale ~ Phi_k, where Lemma P
     forces agreement on J' up to O(Phi_k). (Lemma P is PROVED; the hand-over accounting is SKETCH.)
 (g) Cost cancellation (compensating a status change by sign flips of deep near-copies) can make eps << lambda_k gamma_k,
     but it does not lower t_* below 6 eta/(1-rho^2); irrelevant at tiny scales.

## 2.3 Residual of the candidate (what a negative proof would still need)
 R-i  (rigidity) a proof of the dimension count (e) in the approximate form required by (f), for EVERY NA row near f,
      including combinations mixing anchored, banked, near-contact and non-anchored carriers;
 R-ii (constants) at tiny scales the mate of f' must be carried by <= n_band clean strict non-peaks (l_2-pooled capacity
      ~ sqrt(C'/sigma') ||ell_band||_2), while f's switching staircase pools ~ n_eff = (1+r)/(1-r) carriers per side but
      pays margin, range and leakage costs. Non-recovery would follow if  rho^2 * (capacity of f)^2 > (band capacity)^2.
      This is a finite self-similar optimisation (checked numerically in part 3).
      RESULT (part 3): contradicted in every tested model — the best band strict non-peak has capacity >= f's staircase.
 R-iii (non-margin-sparse approximants) excluded only heuristically (they need near-duplicate families on a cofinite set).

---

# P1 part 3 — model numerics for D_anch (finite SOCP; sanity checks only, NOT statements about Martin's space)

Script: P1_work/anchored_model.py (+ run2..run7.py). One block; base coordinates 0 (support), 1,2 (Z, free, z = 1/2),
3 (staircase coordinate), 4, contacts b_k; dominant robust carrier D ~ e_0 + 0.15(e_1 + e_2) + 0.3 e_4 (so psi|_Z is NOT
proportional to (1,-1) and the oscillation e_1 - e_2 is a genuine Problem-R oscillation); anchored carriers
u_k ~ e_1 - e_2 + s_k (tau/zhat_0) e_0 + beta_k e_3 + tau s_k e_{b_k}, all contacts z_{b_k} = -1 (this sign convention is
forced: side + pushes Sigma_+ inward and the base must absorb -tau s_k e_{b_k} with sign z, side - likewise for Sigma_-;
the opposite convention kills the staircase: Osc ~ 1e-3), |u_k(zhat)| = K vartheta Phi_k (near-threshold peaks), Phi
geometric 2^{-3-i}, families alternating. Mate condition imposed on a symmetric log grid of scales.

## 3.1 Anchoring does not destroy f's capacity (f tested on t in [1e-3, 2])
 tau = 0 (T_PB-like): Osc_max = 0.205;  tau = 0.5, correct contact signs: 0.174;  wrong signs: 0.0013.

## 3.2 Plain truncations fail, keep + common shift + bank recovers
 f'_trunc(L): contacts kept for anchored index < L, deeper contacts set to 0 (destroyed).
 f'_band(L, i): same + common shift delta = z'_1 - z'_2 putting anchored carrier i into the strict non-peak band
   (value ~ 0.01 vartheta Phi_i), its contact banked (bank mass 1e-3, sign z_{b_i}).
 Max oscillation, grid [1e-3, 2] (nA = 10, K = 3, tau = 0.5): f 0.174; trunc(L=6) 0.040; band(6,5) 0.147; band(6,4) 0.172;
   band(6,3) 0.134.
 Parameter sweep (best band(6, i) / f): K = 1.5: 1.09; K = 2: 1.03; K = 5: 1.18; tau = 0.25: 1.06; tau = 1: 1.08.
 Recoverability of rho g_f (g_f = f's maximizing mate on its grid [5e-4, 2], ||g_f||_1 = 0.32), distance in l_1 to C(f')
 on the finer grid [5e-5, 2], rho = 0.9 (nA = 12):
     L = 4: band 0.093 / trunc 0.275;   L = 6: band 0.030 / trunc 0.225;   L = 8: band 0.012 / trunc 0.041 (boundary effects).
 Reading: in the single-family anchored design the approximant family "keep down to L + common shift + banked band strict
 non-peak at depth ~ L" recovers rho g (distance decreasing with L), while canonical-type truncations do not. A single clean
 symmetric strict non-peak has at least the per-scale capacity of f's whole switching staircase (ratios 1.03-1.18).
 Solver statuses partly "optimal_inaccurate" (CLARABEL); trends are stable across runs.

## 3.3 Misaligned multi-family staircases (P1_work/mf_model.py, mf_run1.py, mf_run2.py)
 F families of anchored staircases with the same Z-profile and staircase coordinate, weights offset by r^{f/F} (so a common
 shift cannot align all families), K = 3, tau = 0.5, carriers fixed by the design at f (T fixed for all rows).
 Max oscillation on [1e-3, 2]: f 0.156 / 0.140 / 0.118 for F = 1 / 2 / 3; best keep-shift-bank row 0.182 / 0.214 / 0.261
 (the common shift typically converts one carrier in several families at once: SNP sets (2,10), (4,14), (7,17), ...).
 Recoverability (F = 2, nA = 10, rho = 0.9, ||g_f||_1 = 0.41; f-grid [5e-4,2], approximant grid [5e-5,2]):
     L = 4: KSB 0.162 / trunc 0.336;  L = 6: KSB 0.062 / trunc 0.146;  L = 8: KSB 0.0033 / trunc 0.014 (boundary effects).
 Reading: misalignment does not create a deficiency in the models; KSB distances decrease roughly like ||f' - f||.

---

# P1 part 6 — robustness of KSB, open points, next steps

## 6.1 Robustness of the KSB mechanism across anchoring types (HEURISTIC)
 * Anchoring on exact contacts of f: KSB as in 5.3 (banks on the contacts of the converted carrier).
 * Anchoring on near-contacts of f (|z_{b_k}| = 1 - r_k, r_k -> 0; Round-4 "approximate swallowing"): at f the base absorbs
   at first-order cost r_k |B| t, so the design needs r_k <~ Phi_k; at an approximant with window tolerance eta, every
   near-contact with r_k < eta (in particular the junction carrier's) can be turned into a bank with the same sign:
   KSB unchanged.
 * Anchoring on free coordinates with room bounded below: by Lemma P at f the anchored parts must then be common to the
   carriers used at different scales (up to O(t) room-weighted), i.e. one common far part, restorable by finitely many far
   moves (T_PB-type inheritance, N2 Thm 2.4). Not an obstruction.
 * Oscillation carried at f by combinations (several carriers per scale): the shift lever is (at least) two-dimensional
   (both coordinates of Z, plus other free window coordinates in the supports), so finitely many members can be converted
   simultaneously for generic data (HEURISTIC).

## 6.2 What remains OPEN
 (O-R1) A complete proof that KSB approximants recover rho g in one explicit design (e.g. D_anch with one family): needs
   (a) existence of the switching mate g at f with explicit constants (N2 Prop 2.3 with contacts; the contact sign
   convention z_{b_k} = -1 for both families is forced, model-checked), (b) the mate at f'_{L,delta}: f's decomposition above
   the junction (with the shift delta = O(Phi_L) and the destroyed deep part as perturbations), the banked strict non-peak
   below, and the junction scales (model: favourable constants). This would settle Problem R positively for that design.
 (O-R2) The junction capacity comparison in general (one clean strict non-peak, or a band of them, vs the kept staircase).
   Heuristic duality: small margins (large staircase capacity per scale) <=> wide shift band (many conversions).
 (O-R3) Non-margin-sparse NA approximants (staircases inside f') — another positive mechanism (T_PB truncations), not
   needed by KSB; C3 does not cover them.
 (O-R4) A two-scale version of C2 that encodes cleanliness rigorously (Sec. 5.2) — the only route by which a negative
   proof could discount deep "polluting" carriers.

## 6.3 Suggested next steps
 1. Prove (O-R1) for D_anch with one family (finite bookkeeping as in N2 Prop 2.3; the shift and the bank are the only new
    ingredients; Lemma SYM shows why the bank is necessary).
 2. Turn 5.2 into a theorem: for NA f', g' in C(f'), a strict non-peak k used with coefficient c at scales below t_k must
    have its off-F' part reproduced by g' (SYM') and its J'-profile reproduced by the large-scale carriers up to O(t_k)
    (Lemma P) — a "cleanliness inequality" with explicit constants.
 3. Negative side: the shape "off-J parts not bankable near any junction" does not survive either (HEURISTIC check):
    if the converted carrier's contact part tau sigma_{k_0} is spread over infinitely many contacts of f, bank it on a
    finite set [1, n] with ||sigma_{k_0} 1_{(n,inf)}||_1 <= c Phi_{k_0} (exists since the tail tends to 0); the bank masses
    needed are ~ Phi_{k_0} gamma tau sigma_{k_0}(i) (total O(Phi_{k_0})), banks keep z' = z there (no effect on other
    carriers), and the remaining tail pollutes g' by O(c tau Phi_{k_0}), within the hand-over tolerance of 5.2.
    So no candidate shape for a Problem-R counterexample survives this round's analysis; a negative programme would
    need an obstruction that is not of "capacity at free coordinates" type.
