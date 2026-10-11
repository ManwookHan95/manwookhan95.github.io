# N2 (negative track): adversarial admissible T, a switching mate at all scales, and which side wins

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Part files: neg/N2_part1.md (witness calculus), N2_part2.md (the example),
N2_part3.md (what a counterexample needs).  This file is authoritative where they differ.  Scripts: neg/N2_work/pb_check4.py.
Setting: canonical base, finite block set (p_N; the example uses N = 1, which suffices for the density problem), notation of
Part I (forced data, lem:threshold block threshold, C(f), Li, Rec) and Part II (f[a', z'], Lemma T).

요약 (Korean summary for the user).  Lemma B만 쓰는 적대적 T(사적 레버/뱅크 없음, far rigidity, 근사 중복)로 "모든 작은
스케일에서 일방향(one-sided) 자원 사이를 스위칭하는" mate를 실제로 만들었습니다 (Part 2, PROVED): 접점(contact)도 strict
non-peak도 전혀 없는 행 f에서 g = gamma h 는 + 쪽에서는 음의 peak 계단만, - 쪽에서는 양의 peak 계단만으로 운반되고, Part I의
모든 내재적 회복 메커니즘 밖에 있습니다 (K(f) = {0}).  그런데 canonical truncation f_N (norm-attaining) 자체가 같은 mate
gamma h 를 자기 fibre 에 가지므로 (f, gamma h) 는 엔지니어링 없이 회복됩니다: 일방향 블록 구조가 NA 행으로 모든 스케일에서
상속됩니다.  따라서 반례가 되려면 "모든" NA 근사행에서 파괴되는 일방향 자원(무한히 많은 접점을 통한 base 공명, 또는 원거리
값을 근거리에서 상쇄하는 블록 설계)과, 모든 근사행에 대해 균일한 하한이 필요한데, 후자를 증명할 도구는 없습니다.  결론:
negative 쪽이 더 쉬운 길은 아니며, 판단은 밀도(positive) 쪽이 더 유력합니다.

## 0. Summary and answer to the question "should we approach it negatively?"

TASK.  Choose T adversarially (only Martin's Lemma B), build f and g in C(f) switching through one-sided resources at all small
scales, and try to prove non-recovery dist(rho g, C(f')) >= c for all NA f' near f; equally try to recover.

WHAT WAS DONE.
 1. (PROVED, part 1) A witness calculus for non-recovery: single-piece witnesses (Lemma 1.1), the finite-test-space form
    (Remark 1.3), an explicit upper bound for the block excess at any row by a primal splitting (Lemma 1.4: only "relevant"
    carriers -- strict non-peaks and peaks whose margin is <~ t|u_k(y)| -- contribute), base flatness on free coordinates
    (Lemma 1.5).  These are the tools any non-recovery proof must use.
 2. (PROVED, part 2) An admissible T_PB built with Lemma B only, with far rigidity (private tails <= 2^{-k} Phi(k)^2), no private
    banks/levers, no generic weights, and a first row f (F = {1}, NO contacts, NO strict non-peaks) whose fibre contains the
    segment [-gamma_0, gamma_0] h, h = e_2^* - e_3^*.  The mates gamma h switch at EVERY scale (side +: only negative peaks of a staircase
    Sigma_+ pushed inward; side -: only positive peaks of Sigma_-), and K(f) = {0}: every nonzero mate is a defect of all intrinsic
    mechanisms of Part I.  Nevertheless every canonical truncation f_N (NA) has gamma h in its OWN fibre, so (f_N, gamma h) in NA ->
    (f, gamma h): RECOVERED, with no engineering.  The one-sided structure is inherited by NA rows at all scales; far rigidity, chosen
    to kill private levers, makes inheritance easier.
 3. (PROVED ingredients + HEURISTIC synthesis, part 3) A counterexample with finite base support must use order-one one-sided
    resources at arbitrarily small scales whose usability is destroyed at EVERY NA approximant.  Block resources decided on finitely
    many coordinates are inherited (part 2), far-valued ones become exactly two-sided at the truncation (Lemma 3.2), near free
    coordinates can never be banked (Lemma 3.3), base switching must vanish off the finite window at NA rows (Lemma 3.4).  What is left:
    (A) base resonances through infinitely many contacts, (B) block "cancellation" designs whose near frozen errors cannot be
    absorbed, (C) infinite base support.  For (B), restoration of finitely many groups and crossing conversions recover every design
    except E's rigid design with an additional linear condition (LIN); for (A) the known results (Delta d = 0 recovered for every T)
    leave Delta d < 0 without (SC) and outward-moving approximate resonances, both reducing to the same transition problem.
 4. Non-recovery: NOT proved, for any T and any mate.  No claim of a counterexample.

ANSWER.  The negative approach is not easier.  A non-recovery proof needs a lower bound that is UNIFORM over all NA approximants
(a primal witness at a transition scale, Part 1); the approximant controls the values of all carriers through its normer x', at
essentially no cost for peaks, so such a bound requires a quantitative rigidity of the entire dense family (u_k) relative to xi --
E's rigid design (A1)-(A5) plus (LIN), quantified over all x' -- for which no technique exists.  The adversarial choice of T alone
does not create obstructions: in the cleanest adversarial configuration the canonical truncations recover everything.  Every
explicit adversarial mechanism examined (here and in Rounds 1-14) has an approximant family that recovers it or is not excluded.
Leaning: POSITIVE for the problem as posed.  The realistic negative target is a model-level statement (a finite "transition cell
problem" with optimal excess > 1), not a theorem about p_N.

## 1. Witness calculus (PROVED)

For f' in NA cap S_{p*} with normer x' put R_{f'}(y) := (p(x'+y)^2 - f'(x'+y)^2)^{1/2} and Delta'(y) := p(x'+y) - f'(x'+y) >= 0.

LEMMA 1.1 (single-piece witness).  For h in X* and y in X with x'+y != 0:  dist_{p*}(h, C(f')) >= (|h(x'+y)| - R_{f'}(y))/p(x'+y), and
dist_{p*}(h, C(f')) >= |h(x')|.
Proof.  For g' in C(f'), Part I prop:reduction(a) at x'+y gives |g'(x'+y)| <= R_{f'}(y); so |h(x'+y)| <= R_{f'}(y) + p*(h-g') p(x'+y).  Take the
infimum over g'.  For y = 0 use R_{f'}(0) = 0, p(x') = 1.  QED

REMARK 1.2.  dist_{p*}(h, C(f')) = sup_{x in B_p}(h(x) - r~_{f'}(x)) (minimax: C(f') weak*-compact convex), r~ the sublinear envelope of
(p^2 - f'^2)^{1/2}; Lemma 1.1 is the decomposition x = (x'+y) + (-x').  REMARK 1.3.  By Part I Sec. 2 (global compactness, lower-limit theorem) and lem:pair, (f, rho g) is not
in cl NA iff there are delta > 0 and a finite-dimensional E subset c_00 such that every NA f' with p*(f'-f) < delta has some x in E, p(x) <= 1,
with rho g(x) - r~_{f'}(x) >= delta.  (Restatement; PROVED.)

LEMMA 1.4 (block excess by a primal splitting).  Fix a block, zeta' := R x' != 0, w' = J(zeta'), data M', C', P', alpha', sigma' := |zeta'|.
Let eta in l_1, t > 0, eta = eta_1 + eta_2 with (i) eta_1 supported in supp alpha' and |t eta_1(k)| <= sigma'|alpha'(k)| (= lambda_k mu'_k) where
sgn eta_1(k) = -sgn alpha'(k); (ii) w'(eta_2) = (C'/M') w'(eta_1) and ||D^{-1}eta_2||_2 < infinity.  Then
      |zeta' + t eta| - w'(zeta' + t eta) <= t^2 ||D^{-1} eta_2||_2^2/(2 sigma').
Proof.  zeta' = sigma' alpha' + D beta', beta' = sigma' D w'/C', ||beta'||_2 = sigma' (Part I lem:threshold).  With x_0 := sigma' alpha' + t eta_1 and
b := beta' + t D^{-1}eta_2, |zeta' + t eta| <= max(||x_0||_1, ||b||_2) (unit ball B_{l_1} + D B_{l_2}).  By (i) there are no sign changes, so
||x_0||_1 = sigma' + t w'(eta_1)/M' (w' = M' sgn alpha' on supp alpha').  ||b||_2^2 = sigma'^2 + 2 t sigma' w'(eta_2)/C' + t^2||D^{-1}eta_2||^2, so
||b||_2 <= sigma' + t w'(eta_2)/C' + t^2||D^{-1}eta_2||^2/(2 sigma').  By (ii) both linear coefficients equal w'(eta), and w'(zeta' + t eta) =
sigma' + t w'(eta).  QED
Reading: in direction y (eta = R y, eta(k) = lambda_k u_k(y)) only strict non-peaks, degenerate peaks and peaks with margin < t|u_k(y)|
contribute, each by at most m^2 t^2 u_k(y)^2/(2 sigma'); deep carriers can be put into the l_1 part with a sign flip at first-order cost
<= 2 t lambda_k |u_k(y)|.

LEMMA 1.5 (base flatness).  If f' is NA with base data (a', z', e'), x' = c'(z' + Ue'), and y is supported in J with J cap supp a' = empty
and |z'_j| + |y_j|/c' <= 1 on J, then q(x'+y) - a'(x'+y) = 0.  Proof: z' + y/c' in B_{l_inf}, so q(x'+y) <= c' = a'(x') = a'(x'+y) <= q(x'+y).  QED

## 2. The pure block switching row (PROVED)

Single block (m = 1, lambda_k = Phi(k)).  s(t) = (1+t^2)^{1/2} >= 1 + 3t^2/8 for |t| <= 1.

2.1 DATA.  H = l_2, U e_j = mu_j e_j, mu_j := 2^{-j-10}.  abar := 1/(1+mu_1), a := abar e_1^* (q*(a) = 1, F = {1}); e = e_1, Ue = mu_1 e_1;
z := e_1 + (1/2)1_{j>=2} (not in c_0); zhat := z + Ue (zhat_1 = 1+mu_1, zhat_j = 1/2 for j >= 2).  h := e_2^* - e_3^*, e_0 := e_2^* + e_3^*
(h(zhat) = 0, e_0(zhat) = 1).  Sigma_+ := {k >= 12 : 3 | k}, Sigma_- := {k >= 13 : k = 1 mod 3}, Sigma_g := N \ ({1} u Sigma_+ u Sigma_-).
c_1 := 1, c_k := 1 on Sigma_+-, c_k := 2^{-k^2} on Sigma_g; Phi(k) := 2^{-1-k}c_k (depth ratio 1/8 inside Sigma_+ and inside Sigma_-).
Pairwise disjoint infinite S_k subset {4,5,...} with min S_k -> infinity; sigma_k := sum_{s in S_k} 2^{-s} e_s^*; delta_k := 2^{-k}Phi(k)^2.
(y^(i)) dense in c_00 cap S_{q*}, y^(1) := e_1^*/(1+mu_1); (i_n) takes every value infinitely often; i allowed at k in Sigma_g iff
supp y^(i) cap S_k = empty and 2c_k <= 2^{-2s} c_{k'} delta_{k'} for all k' != k, s in supp y^(i) cap S_{k'}; i(g_n) := i_n if allowed, else 1.
Vectors, u_k := v_k/n_k, n_k := q*(v_k), T e_k := c_k u_k:  v_1 := e_1^* + delta_1 sigma_1;  staircase v_k := h + beta_k e_0 + delta_k sigma_k
with beta_k := -8Phi(k) on Sigma_+, +8Phi(k) on Sigma_-;  generic v_k := y^(i(k)) + s_k abar e_1^* + delta_k sigma_k with s_k in [-8Phi(k), 8Phi(k)],
|y^(i(k))(zhat) + delta_k sigma_k(zhat) + s_k| >= 4Phi(k).  Bounds: staircase n_k in [1.99, 2.002]; generic n_k in [1/2, 3/2]; n_1 in
[1+mu_1-1/256, 1+mu_1+1/256].

LEMMA 2.1 (admissibility; Lemma B only).  T_PB is admissible.  Proof: (T-a) c_k <= 1 = c_1.  (T-b),(T-c): if Z := sum_k x_k c_k u_k in c_00
(x in l_1) and x_{k'} != 0, then for s in S_{k'} only the signature of k' and generic targets meet s; by allowedness, with L(s) the least
generic k whose target contains s, and sum_{k >= L, k in Sigma_g} c_k <= 2c_L:  |Z(s)| >= c_{k'}delta_{k'}2^{-s}(|x_{k'}|/3 - 2||x||_inf 2^{-s}) > 0
for large s in S_{k'}; contradiction.  (T-d): along the infinitely many k with i(k) = i, ||v_k - y^(i)||_1 <= 9Phi(k) -> 0.  QED

LEMMA 2.2 (forced data).  For zhat^# in {zhat} u {zhat_N := zhat 1_{[1,N]} : N >= 3} let f^# := f[a, z^#] (z^# = z or z 1_{[1,N]}); f := f[a,z],
f_N := f[a, z 1_{[1,N]}].  (i) f does not attain its norm, f_N attains it, f_N -> f.  (ii) 1 is a peak with w^#(1) = +M^#; k in Sigma_+ (Sigma_-)
is a non-degenerate peak with w^#(k) = -M^# (+M^#) and |u_k(zhat^#)| in [3.99Phi(k), 4.03Phi(k)].  (iii) M^# in [0.776, 0.8], C^# in [0.2, 0.224],
C^# >= M^#/4; |u_k(zhat^#)| > 2Phi(k) implies k is a non-degenerate peak of sign sgn u_k(zhat^#).  (iv) At f: F = {1}, K = empty, Q = empty.
Proof.  (i) Part II Sec. 2.1 and Part I prop:smooth(c), prop:approximants.  (ii)-(iii) zeta := R zhat^# (statuses are homogeneous); |u_k(zhat^#)| <= 1, so
|zeta| <= ||zeta||_1 <= sum Phi(k) <= 1/2.  Off P, |zeta(k)| = |zeta|Phi(k)^2|w(k)|/C <= |zeta|Phi(k), i.e. |u_k(zhat^#)| <= 1/2; u_1(zhat^#) > 0.99,
so 1 in P, w(1) = +M, C >= Phi(1)M = M/4, C <= M||Phi||_2 <= M/sqrt(12), M + C = 1.  Threshold bar-vartheta = |zeta|M/C <= 4|zeta| <= 2 (Part II
Lemma T: k in P iff |u_k(zhat^#)| >= bar-vartheta Phi(k), degenerate iff equality).  Staircase: v_k(zhat^#) = beta_k + r_k, |r_k| <= delta_k/16
(h(zhat^#) = 0, e_0(zhat^#) = 1, N >= 3), divided by n_k.  (iv) generic |u_k(zhat)| >= 4Phi(k)/n_k > 2Phi(k).  QED

PROPOSITION 2.3.  With theta := 1/5, gamma_0 := 5*10^{-5}: for f^# in {f} u {f_N : N >= 3} and |gamma| <= gamma_0, gamma h in C(f^#), and
p*(f^# + t gamma h) <= 1 + 0.32 t^2 for 0 < |t| <= t_- := 5*2^{-14}.
Proof (gamma > 0; C(f^#) is symmetric).  psi := L*w^# (||psi||_1 <= 1/2, psi(zhat^#) = |R zhat^#| >= 0).
t in (0, t_+], t_+ := 5*2^{-13}:  S(t) := {k in Sigma_+ : Phi(k) <= theta t} (largest depth >= theta t/8; sum Phi^2 <= (64/63)theta^2 t^2).  For
nu in [0,1/2]: omega := nu M/t on S(t), S_2 := sum_{S(t)} Phi^2 omega <= 0.01626 t, d := <Dw, D omega>/C = -M S_2/C (|d| <= 4S_2), Theta := omega - dw,
W := (1-td)w + t omega, B := gamma h - L*Theta.  The content c(nu) := (nu M/t)sum_{S(t)}Phi(k)/n_k has c(1/2) > 0.0048 >= gamma; fix c(nu) = gamma,
so B = -E + d psi with E := (nu M/t)sum_{S(t)}Phi(k)(beta_k e_0 + delta_k sigma_k)/n_k, ||E||_1 <= 8.1 S_2, -E(zhat^#) <= 4.03 S_2.
Block: |W(k)| <= (1-td)M everywhere (on S(t): (1-td)M - nu M); ||DW||^2 = (C + tdM)^2 + t^2(||D omega||^2 - d^2) with ||D omega||^2 <= 0.0065
and C + tdM >= C/2; so N(W) <= (1-td)M + C + tdM + t^2||D omega||^2/C <= 1 + 0.0325 t^2.
Base: |B(1)| <= 2S_2; with ||x e_1 + y|| <= x + <e_1,y> + ||y||^2/(2x) and B(zhat^#) = (1+mu_1)B(1) + sum_{j>=2} zhat^#_j B_j, |zhat^#_j| <= 1/2:
q*(a + tB) <= 1 + t B(zhat^#) + (3/2)t||B 1_{[2,inf)}||_1 + t^2 mu_1||B||_1^2/(2 abar), B(zhat^#) <= 4.03 S_2 (d < 0 <= psi(zhat^#)),
||B 1_{[2,inf)}||_1 <= 10.1 S_2; hence q*(a+tB) <= 1 + 19.2 S_2 t + tiny <= 1 + 0.32 t^2.  Part I lem:dualball gives p* <= max <= 1 + 0.32t^2.
t = -s in [-t_-, 0): same with Sigma_- (w = +M), d = +M S_2/C, f^# - s gamma h = (a - sB) + L*((1+sd)w - s omega); identical bounds.
|t| >= t_-: p*(f^# + t gamma h) <= 1 + 2.002 gamma_0|t| <= s(t) (2.002 gamma_0 <= (3/8)t_- and <= sqrt2 - 1).  QED
Numerical sanity check (finite truncated model, maximal content nu = 1/2): max (bound - 1)/t^2 = 0.119 at f and at f_3, f_10, f_50.

THEOREM 2.4.  (a) S(f) = {0}, hence the intrinsic class K(f) = {0} (Part I prop:intrinsic(b)), while C(f) contains [-gamma_0, gamma_0]h; (MS) fails
at f (margins of Sigma_+ are <= 4.03 q_0 Phi(k), so sum_{mu_k < s}Phi(k) >= s/(33 q_0)); f is not C-tame.
(b) For 0 < |gamma| <= gamma_0 and N >= 3, (f_N, gamma h) attains its norm and (f_N, gamma h) -> (f, gamma h): (f, gamma h) in cl NA((c_0,p_1), l_2^2).
(c) The decompositions switch carriers at every scale (side + only Sigma_+ pushed inward, side - only Sigma_-; on the wrong side a Sigma_+
carrier only carries negative multiples of h), the switching vector is O(t), no two-sided representation exists (S(f) = {0}); the same
holds at the NA rows f_N.
Proof.  (a) F = {1}, xi_1 != 0, Q = empty (Lemma 2.2(iv)); margins by Part II Lemma T.  (b) Lemma 2.2(i), Prop. 2.3, Part I prop:reduction(d).
(c) description of Prop. 2.3.  QED

REMARKS 2.5.  (1) Part I thm:tamefibre (C-tame => C(f) subset S(f)) is consistent: (MS) fails at f and at every f_N.  (2) Inheritance mechanism:
the staircase values are decided on {2,3} up to private tails <= Phi(k)^2 (far rigidity), the threshold is pinned by the dominant peak, and
the base part only uses |z| <= 1/2 off F -- all unchanged by truncation.  (3) Contrast with P1 (Part I Sec. 'The resonance obstruction'): there K(f) = R u_{2,1} and
the canonical truncations FAIL; here K(f) = {0} and they SUCCEED: what matters is whether the one-sided resources survive the passage to
c_0, not whether the mate is intrinsic.  (4) "At an NA row the finest scales need a single two-sided linear representation" is FALSE
for mates (true for exact data, Part II Cor. S2, and at C-tame rows).  (5) Part II's rigidity Lemma S and Thm NL constrain only mates
carrying exact two-piece data; the mates gamma h of the NA rows f_N carry none (they are carried at scale t by peaks of depth ~t).  Hence
the sandwich/profile route to non-recovery cannot work along all NA approximants: approximants violating (MS) escape it.  (6) For N >= 2
one may put near-duplicates u_{k,m} (same v_k, block-private signatures) in every block, as in Martin's construction, and use only block
1 in the decompositions; the proof goes through with changed constants (SKETCH).

## 3. What a counterexample must contain; the remaining adversarial designs

PRINCIPLE 3.1 (inheritance; HEURISTIC in general, PROVED for T_PB).  For F finite, f_N := f[a, z1_{[1,N]}]: (a) a' = a, e' = e,
zhat_N - zhat = -z1_{(N,inf)}, so carrier values change only by their pairing with the tail of z and coordinates in [1,N] keep their status
(PROVED); (b) thresholds move only through carriers with large tails (PROVED for T_PB); (c) resources decided on [1,N] up to errors
small against their margins/gaps/rooms transport at all scales (HEURISTIC).
LEMMA 3.2 (two-sidedification; PROVED).  If Ue is supported in F subset [1,N] (diagonal U) and u_k = v^near + v^far with v^near supported in
[1,N], v^near(zhat) = 0, v^far supported in (N,inf), then u_k(zhat_N) = 0 and k is a strict non-peak of f_N with w_N(k) = 0 (zeta(k) = 0 is
impossible on P because alpha(k) and Phi(k)^2 w(k)/C have the same sign and the second is nonzero).
LEMMA 3.3 (near free coordinates stay free; PROVED).  If f'_n -> f and |z_l| < 1, l notin F, then z'_n(l) -> z(l) (Part I prop:continuity), so l
is eventually free at f'_n (not in supp a'_n, where |z'| = 1): near free coordinates can never be banked along a convergent sequence.
LEMMA 3.4 (PROVED; G3 Lemma 1.4(c) at an NA row).  For every mate of an NA row f', every t > 0 and every pair of decompositions of
f' +- t g' with max-norm <= s(t): sum_{j notin F'} (1 - |z'_j|)|V_j| <= t/q'_0, V = B_+ - B_-.
CONSEQUENCE 3.5 (HEURISTIC).  A non-recovered (f, rho g) with F finite needs order-one one-sided resources at arbitrarily small scales
whose usability is destroyed at every NA approximant: (A) base resonances through infinitely many contacts; (B) block designs with far
values compensated by near parts (truncation creates robust peaks of both signs, not two-sided carriers); (C) infinite F.

DESIGN (B) (HEURISTIC).  Cancelling pairs u_{1,p}, u_{2,p} (near parts v -+ F_0 e_A, far parts +-phi_p): (i) finitely many pairs can always be
restored by far moves; infinitely many only if ||phi_p||_inf is not << phi_p(z) (adversary: spread far parts); (ii) shared far parts allow
global restoration (adversary: infinitely many independent far parts); (iii) with independent far parts, CROSSING CONVERSIONS (convert
u_{1,p} and u_{2,p'} of two pairs) cancel the near frozen error exactly; far parts are banked on far coordinates; recovered at model level;
(iv) to block (iii) the adversary needs near frozen errors in a fixed error space E_c on near free coordinates that cannot be cancelled
(no +- pairing), which by Lemma 3.3 cannot be banked and must be absorbed by block carriers: slow rates + sign rule = E's rigid design
(A1)-(A5) (r1/E_notes 7.3), with bounded conversion capacity and model-level excess R(J) - 1 > 0 (E's numerics); (v) NEW: since NA rows may
carry block switching at all scales (part 2), the approximant may also re-create one-sided structure below the transition; the
adversary must then also ensure (LIN): for small t no two families of carriers at depth >~ t that admissible moves make weak peaks of
opposite orientation have near restrictions agreeing up to O(t) modulo window vectors (base-switching constraint, Lemma 3.4).  Far
rigidity helps the adversary for (LIN) (near-duplicates cannot be separated to opposite signs without a value gap >~ Phi); (vi) the
Gordan (relative) lever lowers all peak costs at negligible cost but converts nothing; small in error-dominated designs.

DESIGN (A) (status).  Exact d-neutral resonances: recovered for every admissible T (P2A Thm 2.1 / r2 N2 Thm 1).  Delta d >= 0: (TC);
Delta d < 0: (SC) or (PC*); without (SC) and rho near 1: OPEN (Part I rem:withoutSC); the (SC)-failing carriers stay two-sided at f_N while
their tails are small, the deep ones form Part I's scrambled set; non-canonical truncations keeping finitely many of them at value 0
are available, effect OPEN.  Outward-moving approximate resonances: banks handle the base, transfer carriers are destroyed below the
window; private contact parts give inward-move levers (SKETCH); reduces to the transition problem of (B).

3.6 WHY A NON-RECOVERY PROOF IS OUT OF REACH (assessment).  By Section 1 the proof must give, uniformly over all NA f' near f, a
direction y in a fixed finite-dimensional E and a scale t with too few relevant carriers (Lemma 1.4).  The approximant sets all values
u_k(x'): reducing a peak's margin does not change its own coordinate w'(k); far coordinates are free; near ones move by o(1), which is
>> the depth of every deep carrier.  A uniform bound is a quantitative rigidity statement about the whole dense family relative to
every x' near xi ((A1)-(A5) + (LIN) for all x'), and no technique for such statements exists in the sources.  STATUS: OPEN.

## 4. Results table

| # | Result | Status |
|---|---|---|
| 1 | Lemma 1.1 single-piece witness; Remark 1.3 finite test spaces | PROVED |
| 2 | Lemma 1.4 block excess by primal splitting ("relevant carriers") | PROVED |
| 3 | Lemma 1.5 base flatness on free coordinates of an NA row | PROVED |
| 4 | Lemma 2.1 T_PB admissible (Lemma B only; far rigidity; no private levers) | PROVED |
| 5 | Lemma 2.2 forced data of f and of every canonical truncation (F={1}, K=Q=empty, staircase peaks) | PROVED |
| 6 | Prop. 2.3 gamma h in C(f) and in C(f_N) for all N >= 3, uniformly | PROVED |
| 7 | Thm 2.4 K(f) = {0}, (MS) fails, (f, gamma h) in cl NA via canonical truncations; block switching at all scales at NA rows | PROVED |
| 8 | Remark 2.5(4)-(5): "finest scales need a two-sided linear representation" false for mates; Lemma S/Thm NL route cannot cover all NA approximants | PROVED (by Thm 2.4) |
| 9 | Remark 2.5(6) N >= 2 with cross-block near-duplicates | SKETCH |
| 10 | Principle 3.1 inheritance under canonical truncation | HEURISTIC (PROVED for T_PB) |
| 11 | Lemma 3.2 two-sidedification of far-valued carriers | PROVED |
| 12 | Lemma 3.3 near free coordinates cannot be banked | PROVED |
| 13 | Lemma 3.4 base switching vanishes off the window at NA rows | PROVED (via G3) |
| 14 | Consequence 3.5 necessary structure of a counterexample (F finite) | HEURISTIC |
| 15 | Design (B): restoration, crossing conversions, reduction to E's rigid design + (LIN) | HEURISTIC |
| 16 | Design (A): status of base resonances for adversarial T | SKETCH / OPEN |
| 17 | Non-recovery of any (f, rho g) for any admissible T, any N | OPEN (not claimed) |

## 5. Next steps
 1. Formulate the finite "transition cell problem" for E's rigid design + (LIN) (self-similar staircase, one transition band, all
    lever families of Section 3 as variables) and compute its optimal excess numerically: a value <= 1 would close the negative program
    at model level; a robust value > 1 would be the first model-level evidence that survives all known approximant strategies.
 2. Positive side: prove Principle 3.1(c) for F finite, K = empty under uniform relative tails (|u_k(z 1_{(N,inf)})| <= eta_N Phi(k)
    on the carriers used, eta_N -> 0): this would settle the whole "block switching without contacts" class for every admissible T.
 3. (SC)-failing exact resonances with Delta d < 0: test non-canonical truncations that keep finitely many zero-value carriers.
 4. Write out the N >= 2 version of T_PB with Martin's cross-block near-duplicates (constants only).
