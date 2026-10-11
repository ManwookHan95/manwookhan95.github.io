# N2 referee notes (full proofs of the fixes and of the referee's additions)

Setting and notation of Part I (canonical base, finite block set I, admissible T), Part II (f[a', z'], Lemma T), G3 (r14/G3_notes:
budget E_b, Lemma 1.2, Cor. 1.3, Lemma 1.4).  Part files: neg/N2_ref_part1.md ... N2_ref_part4.md.  Scripts: neg/N2_ref_work/.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1. Fix F1: the finite-test-space criterion (N2 Remark 1.3).  PROVED.
CLAIM.  For f in S_{p*}, g in C(f), rho in (0,1): (f, rho g) is NOT in cl NA((c_0,p), l_2^2) if and only if there are delta > 0 and a
finite-dimensional subspace E of c_00 such that every f' in NA cap S_{p*} with p*(f' - f) < delta satisfies
      sup { rho g(x) - r~_{f'}(x) : x in E, p(x) <= 1 } >= delta ,
where r~_{f'} is the largest sublinear minorant of (p^2 - f'^2)^{1/2} (Part I prop:primal).
Proof.  If: for g' in C(f') and x in E with p(x) <= 1, g'(x) <= r~_{f'}(x), so p*(rho g - g') >= rho g(x) - r~_{f'}(x); hence
dist(rho g, C(f')) >= delta for all NA f' within delta of f, and Part I lem:pair gives the claim.  Only if: let (x_i) in c_00 be dense
in c_0 and E_n := span{x_1, ..., x_n}.  If the condition fails for (1/n, E_n) for all n, pick NA f_n with p*(f_n - f) < 1/n and
sup_{E_n cap B_p} (rho g - r~_{f_n}) < 1/n.  By Part I thm:compact and Blaschke's theorem, along a subsequence C(f_n) -> A in the
Hausdorff metric, A compact convex, and r~_{f_n}(x) = h_{C(f_n)}(x) -> h_A(x) for x in c_0.  Hence rho g <= h_A on every E_m cap B_p,
hence on c_0 (homogeneity, p-Lipschitz continuity of both sides, density).  Separation by x in c_0 gives rho g in A, so
dist(rho g, C(f_n)) <= d_H(A, C(f_n)) -> 0 and lem:pair gives (f, rho g) in cl NA.  QED

## 2. Fix F2: the block-excess bounds (N2 Lemma 1.4 and its reading).
Fix a block, zeta' in l_1 \ {0}, w' = J(zeta'), M', C', P', alpha', sigma' := |zeta'| (Part I lem:threshold: zeta' = sigma' alpha' +
sigma' D^2 w'/C'), s_k := sgn w'(k), e := D w'/C' (unit vector of l_2), P_perp := orthogonal projection onto e^perp.
LEMMA 1.4 (N2).  PROVED (re-derived).  Note: condition (ii) is equivalent to w'(eta_1) = M' w'(eta).

LEMMA 1.4' (refined).  PROVED.  If eta = eta_1 + eta_2 satisfies (i), (ii) of Lemma 1.4, t > 0 and c := sigma' + t w'(eta) > 0, then
      |zeta' + t eta| - w'(zeta' + t eta) <= t^2 ||P_perp D^{-1} eta_2||_2^2 / (2c).
Proof.  zeta' + t eta = x_0 + D b with x_0 = sigma' alpha' + t eta_1, b = sigma' e + t D^{-1} eta_2.  By (i), ||x_0||_1 = sigma' + t w'(eta_1)/M'
= c.  Write D^{-1} eta_2 = X e + Y with X = <e, D^{-1} eta_2> = w'(eta_2)/C' = w'(eta) (by (ii)) and Y = P_perp D^{-1} eta_2; then
||b||_2^2 = c^2 + t^2 ||Y||^2, so ||b||_2 <= c + t^2||Y||^2/(2c).  Since the unit ball is B_{l_1} + D B_{l_2}, |zeta' + t eta| <=
max(||x_0||_1, ||b||_2), and w'(zeta' + t eta) = c.  QED

LEMMA 1.4'' (balanced relevant-carrier bound).  PROVED.  Let t > 0, eta in l_1, and A contained in supp alpha' with: for k in A,
s_k eta(k) >= 0 or t|eta(k)| <= sigma'|alpha'(k)|/2.  Put R := N \ A and assume ||D^{-1}(eta 1_R)||_2 < inf.  Let A_0 be a nonempty
subset of A, F_0 := sum_{A_0} Phi(k)^2, kappa := (sum_{k in R} w'(k) eta(k) - C' sum_{k in A} s_k eta(k))/F_0, and assume
t|kappa| Phi(k)^2 <= sigma'|alpha'(k)|/2 on A_0 and c := sigma' + t w'(eta) > 0.  Then
      |zeta' + t eta| - w'(zeta' + t eta) <= t^2 ( ||D^{-1}(eta 1_R)||_2 + (|kappa|/M') ||D(w' 1_{N \ A_0})||_2 )^2 / (2c).
Proof.  eta_1 := eta 1_A + kappa s 1_{A_0} Phi^2, eta_2 := eta - eta_1.  (i): eta_1 lives in A; where s_k eta_1(k) < 0,
|eta_1(k)| <= |eta(k)| 1[s_k eta(k) < 0] + |kappa| Phi(k)^2 1_{A_0}(k), so t|eta_1(k)| <= sigma'|alpha'(k)|.  (ii): w'(eta_1) = M' sum_A s_k eta(k)
+ kappa M' F_0 equals M' w'(eta) = M'(M' sum_A s_k eta(k) + sum_R w'(k) eta(k)) by the choice of kappa (M' - 1 = -C').  Finally
D^{-1} eta_2 = D^{-1}(eta 1_R) - (kappa/M') D(w' 1_{A_0}) and D(w' 1_{A_0}) = D w' - D(w' 1_{N \ A_0}), P_perp D w' = 0.  Lemma 1.4'.  QED

THE LITERAL READING IS FALSE.  N2's gloss "only strict non-peaks, degenerate peaks and peaks with margin < t|u_k(y)| contribute, each
by at most m^2 t^2 u_k(y)^2/(2 sigma')" fails: one block, Phi = (1/4, 1/8, 1/16, 1/32), zeta = (0.25, 0.1125, 0.000625, 0.025) (carrier 3 a
strict non-peak, the others robust peaks), eta = Phi(1) e_1 (a push on the robust dominant peak only): excess/t^2 -> 1.5119e-5 > 0,
equal to the exact coefficient (1/2) d_S^2 Lambda (dS)^2 = C c_Q (dS)^2/(2|zeta| F_2) of Part I lem:localformula (script
reading_counter.py).  The peak-sum change costs in proportion to the D-mass c_Q of w' on the strict non-peaks; Lemma 1.4''
captures this through the balancing term.  Numerics: Lemma 1.4' and 1.4'' hold on ~10^4 random instances up to rounding
(lemma14_check2.py, lemma14_balanced.py).

## 3. Fix F3: a multi-block admissible T_PB (Martin-type cross-block near-duplicates).  PROVED.
Data: a bijection l: N x N -> N with l(1,1) = 1, increasing in k for fixed m (so l(k,1) >= k); in every block the classes
Sigma_+ = {k >= 12, 3 | k}, Sigma_- = {k >= 13, k = 1 mod 3}, Sigma_g = rest minus {1}; weights c_{k,m} := 1 on {1} u Sigma_+-,
c_{k,m} := 2^{-l(k,m)^2} on Sigma_g; Phi_m(k) := 2^{-m-k} c_{k,m}; pairwise disjoint infinite S_{k,m} in {4,5,...} with min S_{k,m} -> inf
as l(k,m) -> inf; sigma_{k,m} := sum_{s in S_{k,m}} 2^{-s} e_s^*, delta_{k,m} := 2^{-k} Phi_m(k)^2; targets y^(i) dense in c_00 cap S_{q*},
y^(1) = e_1^*/(1+mu_1); i ALLOWED at a generic (k,m) iff supp y^(i) cap S_{k,m} = empty and 2 c_{k,m} <= 2^{-2s} c_{k',m'} delta_{k',m'} for all
(k',m') != (k,m), s in supp y^(i) cap S_{k',m'}; (i_n) takes every value infinitely often; in block m, i(g^m_n, m) := i_n if allowed,
else 1 (g^m_1 < g^m_2 < ... the generic indices).  Vectors: v_{1,m} := e_1^* + delta_{1,m} sigma_{1,m}; v_{k,m} := h + beta_k e_0 +
delta_{k,m} sigma_{k,m} on Sigma_+- with beta_k := -+8 Phi_1(k) (the SAME in all blocks); generic v_{k,m} := y^(i(k,m)) + s_{k,m} abar e_1^*
+ delta_{k,m} sigma_{k,m} with |s_{k,m}| <= 8 Phi_m(k) and |value at zhat| >= 4 Phi_m(k).  u_{k,m} := v_{k,m}/q*(v_{k,m}), T e_{k,m} := c_{k,m} u_{k,m}.
Admissibility: (T-a) c <= 1 = c_{1,1}; ||Phi_m||_1 <= 2^{-m}.  (T-d): each i is allowed at all generic (k,m) of block m with l(k,m)
large (finitely many conditions), so u_{k,m} -> y^(i) along infinitely many k in every block.  (T-b), (T-c): if T x in c_00 and
x_{k',m'} != 0, at s in S_{k',m'} only the signature of (k',m') and generic targets containing s contribute; the latter come from
(k,m) != (k',m') with 2 c_{k,m} <= 2^{-2s} c_{k',m'} delta_{k',m'}, and sum_{l(k,m) >= L} 2^{-l(k,m)^2} <= 2 * 2^{-L^2}; so
|(T x)(s)| >= c_{k',m'} delta_{k',m'} 2^{-s} (|x_{k',m'}|/3 - 2 ||x||_inf 2^{-s}) > 0 for large s in S_{k',m'}: contradiction.  QED
(The one-block construction of N2 is block 1 of this T, with 2^{-l(k,1)^2} <= 2^{-k^2}; every bound of Lemma 2.2 survives.)
The parenthetical of N2 Lemma 2.1 (literally equal vectors in every block) violates (T-b) and must be replaced by this.

## 4. Lemma R2 (unbounded block parts).  PROVED.
Let f' in S_{p*} have F' cup K' finite, normer eta, q'_0 := q**(eta), and eta_free := inf_{j notin F' cup K'} (1 - |z'_j|) > 0 (true at
every NA row).  Let g in C(f') and, for t > 0, f' +- t g = A_+- + L* W_+- with max(q*(A_+-), ||W_+-||_{V*}) <= s(t); B_+ := (A_+ - a')/t,
B_- := (a' - A_-)/t, Theta_+ := (W_+ - w')/t, Theta_- := (w' - W_-)/t.  If g is not in l_1(F' cup K') + Y (Y = range T), then
||Theta_+(t)||_{V*} -> inf and ||Theta_-(t)||_{V*} -> inf as t -> 0+.  In particular every finitely supported mate of an NA row whose
support is not contained in F' cup K' has this property.
Proof.  G3 Cor. 1.3: E_b(A_+) + E_b(A_-) <= t^2/q'_0; G3 Lemma 1.2 at j notin F' (a'_j = 0): the j-summand of E_b(A_+-) is >= (1 - |z'_j|)
t |B_+-(j)|.  So sum_{j notin F' cup K'} |B_+-(j)| <= t/(eta_free q'_0).  If ||Theta_+(t_n)|| <= R along t_n -> 0, then (weak* compactness of
the ball of V*; L* weak*-to-norm continuous on bounded sets since L is compact) Theta_+(t_n) -> Theta weak* along a subsequence and
L* Theta_+(t_n) -> L* Theta in l_1, so B_+(t_n) = g - L* Theta_+(t_n) -> b := g - L* Theta, which vanishes off F' cup K'.  Then g = b + L* Theta
in l_1(F' cup K') + Y (Part I (eq:Lstar)): contradiction.  Same for Theta_-.  If g in c_00 and g = b + y with supp b in F' cup K' and
y in Y, then y = g - b in c_00 cap Y = {0}, so supp g is contained in F' cup K'.  QED
Consequence.  At NA rows, finitely supported mates off F' cup K' (e.g. gamma h at f_N) are carried only by scale-dependent
decompositions with unbounded block parts; N2 Prop. 2.3 shows they exist.  This is the precise content of N2 Remark 2.5(4)-(5).

## 5. Push calculus.  PROVED.
One block (lambda_k = Phi(k)), any row with normer direction zhat = z + Ue, zeta^ := R zhat, w := J(zeta^), threshold vartheta^ and
margins mu^_k := |u_k(zhat)| - vartheta^ Phi(k) in zhat units, so |zeta^||alpha(k)| = lambda_k mu^_k on P (Part II Lemma T(b));
s_k := sgn w(k).  For omega in l_inf with ||D omega|| < inf, d := <D w, D omega>/C, B := g - L*(omega - d w):
 (i)   (L*(omega - d w))(zhat) = |zeta^| sum_k omega(k) alpha(k) = sum_{k in P} omega(k) s_k lambda_k mu^_k;
 (ii)  if 1 - td >= 0, C + tdM > 0 and |(1 - td) w(k) + t omega(k)| <= (1 - td) M for all k, then
       N(w + t(omega - d w)) <= 1 + t^2 ||D omega||_2^2 / (2(C + tdM));
 (iii) q*(a + tB) >= 1 + t g(zhat) - t sum_{k in P} omega(k) s_k lambda_k mu^_k.
Proof.  (i) <omega, zeta^> = |zeta^|(<omega, alpha> + d) by lem:threshold, and <w, zeta^> = |zeta^|.  (ii) With W := (1 - td) w + t omega:
||D W||^2 = (1 - td)^2 C^2 + 2t(1 - td) d C + t^2 ||D omega||^2 = (C + tdM)^2 + t^2(||D omega||^2 - d^2), so ||D W|| <= C + tdM +
t^2 ||D omega||^2/(2(C + tdM)); add ||W||_inf <= (1 - td) M and use M + C = 1.  (iii) zhat in B_{q**}, a(zhat) = 1, and B(zhat) =
g(zhat) - (i).  QED  (Checked to 60 digits on the T_PB model: push_calculus_check.py.)
Reading.  Inward pushes cost nothing at first order in the block (no margin enters (ii)); the base pays at first order exactly the
lambda-weighted margins of the pushed PEAKS, and nothing for pushed strict non-peaks.  Hence a mate carried at scale t by pushes
of size ~1/t on peaks of depth ~t with margins O(depth) costs O(t^2) -- at ANY row, attaining or not.  This is why the staircase
of Section 2 transfers to every f_N: signs, margins and the near support {2,3} are unchanged by the truncation.

## 6. N2 Remark 2.5(6) upgraded.  PROVED.
For the operator of Section 3 and the norm p_n with n >= 2 blocks: the rows f^# := f[a, z^#] (z^# in {z} u {z 1_{[1,N]} : N >= 3}) have
block-1 data identical to the one-block case (they depend only on R_1 zhat^#, and Lemma 2.2's proof uses only ||Phi_1||_1 <= 1/2,
Phi_1(1) = 1/4, ||Phi_1||_2^2 <= 1/12).  With B, W_1 of N2 Prop. 2.3 (psi := R_1* w_1), f^# + t gamma h = (a + tB) + R_1* W_1 +
sum_{m=2}^{n} R_m* w_m, and Part I lem:dualball for p_n gives p_n*(f^# + t gamma h) <= max(q*(a + tB), N_1(W_1), 1): the constants of
Prop. 2.3 are unchanged, so gamma h in C(f^#) for |gamma| <= gamma_0.  In every block m, off P_m one has |u_{k,m}(zhat)| <= |zeta_m|/m <=
2^{-m} (lem:threshold with C_m >= Phi_m(k)|w_m(k)|), so the dominant carrier is a peak, C_m >= Phi_m(1) M_m, the threshold in units of
Phi_m(k) is at most 2^{-m} * 2^{m+1} = 2, and generic carriers (|value| >= 4 Phi_m(k)/n) as well as the staircase near-duplicates
(|value| ~ 4 Phi_1(k) = 2^{m+1} Phi_m(k)) are non-degenerate peaks: Q_m = empty for all m, S(f) = {0}, K(f) = {0}; (MS) fails in block 1.
So Theorem 2.4 holds verbatim for p_n, every n >= 1.

## 7. Further corrections
 (P-c) Thm 2.4(c) at f_N: S(f_N) != {0} in general (generic carriers with far targets become strict non-peaks; observed numerically);
       "no two-sided representation" holds at f_N because gamma h is not in l_1(F) + Y (Section 4), not because S(f_N) = {0}.
 (O1)  "The canonical truncations recover everything" -> only [-gamma_0, gamma_0] h is proved to lie in C(f) and in every C(f_N);
       C(f) is not determined and f in Rec is OPEN for T_PB (f is neither (BT) nor C-tame, since (MS) fails).
 (O2)  "Principle 3.1 PROVED for T_PB" -> proved only for the mates gamma h (|gamma| <= gamma_0) of the specific row f.
 (C-B1) Design (B)(i): restoration of infinitely many cancelling pairs is impossible as soon as sup_p ||phi_p||_1 < inf (automatic for
       bounded normalisations): |phi_p(z')| <= ||phi_p||_1 sup_{supp phi_p} |z'| -> 0 for z' in c_0.  The l_inf-size ("spreading") plays no
       role; N2's "||phi_p||_inf <= F_0/delta_0 ... the adversary must spread the far parts" is incorrect (no downstream effect).
 (C-B2) Design (B)(iii): converted pairs are used two-sidedly, so their far errors must be banked on SUPPORT coordinates (tiny masses
       of a'), not on contacts (one-sided).  HEURISTIC as in N2.

## 8. Numerics (sanity checks only)
pb_ref_check.py / pb_ref_check2.py: mpmath, 60 digits, true parameters (staircase from k = 12, ratio 1/8, generic weights 2^{-k^2},
mu_j = 2^{-j-10}), 96 carriers, 1200 coordinates.  Forced data: M = 0.7999, C = 0.2001, threshold 0.80 (zhat units) at f; same at
f_3, f_10, f_60; staircase values -+3.99945 Phi(k), all peaks.  Decompositions: identity error <= 2e-61; max (bound - 1)/t^2 =
1.28e-4 (gamma = gamma_0), 0.1174 (maximal content nu = 1/2), over t in [1e-15 t_+-, t_+-], both sides, rows f, f_3, f_10, f_60.

## 9. What remains open (precise)
 1. Non-recovery of any (f, rho g) for any admissible T and any n: OPEN; there is no candidate with a proof strategy.  By Section 1 a
    proof needs, for one fixed finite-dimensional E in c_00 and delta > 0, the inequality sup_{E cap B_p}(rho g - r~_{f'}) >= delta for
    EVERY NA f' within delta of f, with upper bounds on r~_{f'} obtained from Lemma 1.4''/lem:localformula (not from per-carrier bounds).
 2. For T_PB and the row f: is C(f) contained in Li C(f_N) (i.e. f in Rec)?  Requires determining C(f) (is it [-gamma_max, gamma_max] h?).
 3. Inheritance theorem (N2's next step 2): F finite, K empty (room bounded below), mates carried by pushes on carriers whose signs and
    margins are preserved at f_N up to o(depth) (e.g. uniform relative tails) => g in Li C(f_N).  The push calculus (Section 5) gives the
    block part and the first-order base term; the change of (M, C, threshold) at f_N, the free-coordinate part of B and the first-order
    correction for g(zhat_N) != 0 remain to be controlled uniformly in t.
 4. The negative target that survives Section 2: cancellation designs whose staircases have sign-determining far parts of bounded
    l_1-mass (not restorable at any NA row, C-B1), no alternative staircase in the mate direction (a rate condition on the dense family,
    N2's (LIN)), and E's rigid design (A1)-(A5) against crossing conversions; first test = N2's finite "transition cell" computation.
 5. Base resonances with Delta d < 0 without (SC), rho -> 1 (Part I rem:withoutSC); infinite F ((LSC-trunc)).
