# S3 referee, part 6: complete proofs of the fixes

## 6.1 Lemma F1 (|C' - C| = O(s_1) with no hypothesis; removes the circularity in Prop 4.2(a)-(b) and D2(i)). PROVED.
Setting: one block, y in l_1 \ {0}, w = J(y) (N(w) = 1, w(y) = |y|), M = ||w||_inf, C = ||Dw||, M + C = 1, P = peak set.
Clamp formula (P2A Lemma 1.1): Phi_k w(k) = sgn(y_k) min(Phi_k M, C v_k), v_k := |y_k|/(Phi_k |y|). For y = R_m x: v_k = m|u_k(x)|/|R_m x|
(scale invariant in x). Squaring and summing, C^2 = sum_k min(Phi_k M, C v_k)^2, i.e. (divide by C^2, M = 1 - C)
   F(C; v) := sum_k min(Phi_k (1-C)/C, v_k)^2 = 1.                                                    (F)
(i) F(.; v) is continuous and nonincreasing on (0,1). (ii) Since ||alpha||_1 = 1 (part 1, 1.1(iv)), some peak k_* has alpha_{k_*} != 0, i.e.
v_{k_*} > Phi_{k_*}(1-C)/C strictly (positive margin). (iii) Let v' be another datum with |v'_{k_*} - v_{k_*}| small and C' the root of F(.; v') = 1
(the C-datum of y' = R x'). There is a neighbourhood N_0 of C, independent of v' (for |v'_{k_*} - v_{k_*}| <= r_0), on which the k_*-term of
F(.; v') equals Phi_{k_*}^2((1-c)/c)^2, whose derivative is <= -c_* := -2 Phi_{k_*}^2 (1 - sup N_0)/(sup N_0)^3 < 0; the other terms are
nonincreasing. Hence F(c_1; v') - F(c_2; v') >= c_*(c_2 - c_1) for c_1 < c_2 in N_0.
(iv) |min(a, s)^2 - min(a, s')^2| <= 2a|s - s'| for a, s, s' >= 0. So |F(C; v') - F(C; v)| <= (2(1-C)/C) sum_k Phi_k |v'_k - v_k|.
(v) If C' in N_0 (true at late stages, C' -> C by P2A Lemma 1.2): F(C'; v') = 1 = F(C; v), so by (iii)-(iv)
   |C' - C| <= (2(1-C)/(C c_*)) sum_k Phi_k |v'_k - v_k|.
(vi) Along the approximants of S3 3.3: |v'_k - v_k| <= (m/|R xhat'|)|u_k(xhat' - zhat)| + m |u_k(zhat)| | 1/|R xhat'| - 1/|R** zhat| |
<= K(s_1 + t_k) by (E2) and the convexity sandwich of (E4) (which does not use C'). Hence
   |C' - C| <= K'(s_1 sum_k Phi_k + sum_k Phi_k t_k) = O(s_1) + (a quantity -> 0 as N'' -> infinity, made <= s_1^2). QED.
Consequence (Lipschitz bound, Prop 4.2(a), D2(i)): if sgn u_k(xhat') = sgn u_k(zhat),
|Phi_k w'(k) - Phi_k w(k)| <= Phi_k|M' - M| + |C' - C| v_k + C'|v'_k - v_k| <= K(s_1 + t_k); if the signs differ, both |u_k| are <= |u_k(xhat') - u_k(zhat)|
and |Phi_k w'(k) - Phi_k w(k)| <= C' v'_k + C v_k <= K(s_1 + t_k). The constant is uniform in k. This is the input that Prop 4.2(a),(c),(d) and
D2(i),(ii) need; no circularity remains.

## 6.2 Remark F2 (common scales; a logical gap, not a counterexample).
Scr_m(s) is nondecreasing in s. If Scr_m(K s_i) <= eps_i s_i with eps_i -> 0, then Scr_m(K s) <= 2 eps_i s on [s_i/2, s_i]; nothing more follows
from monotonicity. So two nondecreasing functions can each be o(s) along some sequence while their "good" scale sets are disjoint
(e.g. one is small near s = 2^{-j^2}, the other near 2^{-j^2-j}, each increasing steeply in between). Theorem D with several Delta d < 0
blocks needs (SC_m) along ONE sequence of s_1; hence Prop 4.2's "Consequently" is a non sequitur as stated, and must assume a common sequence
(or Scr_m(Ks) = o(s) as s -> 0 in all but one such block). Whether actual blocks of an admissible T can realise disjoint good scales is
irrelevant for the correction.

## 6.3 Proposition F3 (Phi need not be regular for admissible T). PROVED.
If T is admissible and 0 < c_{n,m} <= 1 with c_{n,m} = 1 for some (n,m) with q*(T e_{n,m}) = 1 (or sup c_{n,m} q*(T e_{n,m}) = 1), then
T' := T Diag(c) is admissible: ||T'|| = sup c q*(Te) = 1; T' injective (c > 0); Ran T' is contained in Ran T, so Ran T' cap c_00 = {0} and Ran T' is in Y;
T'e/q*(T'e) = Te/q*(Te), so every tail is still dense. Given any admissible T and any increasing k_0 < k_1 < ..., choosing
c_{k,m} := Phi_m(k_j)/Phi_m(k) for k_{j-1} < k <= k_j gives Phi'_m(k) = Phi_m(k_j) on the j-th cluster (c <= 1 since Phi_m decreases along
k... if not monotone, use min over the cluster). With cluster lengths L_j -> infinity: sum_{Phi'_k < x} sqrt(Phi'_k) >= L_j sqrt(Phi_m(k_j)) at
x slightly above Phi_m(k_j), so sup_x (sum_{Phi' < x} sqrt(Phi'))/sqrt(x) = infinity, and the box tail of A Cor 6.10(a) for |c_k| = K sqrt(Phi'_k)
is not O(sigma) along those scales. So S3 4.5's "O(sigma) box tails when |c_k| <= K sqrt(Phi_k)" needs a regularity hypothesis on Phi
(e.g. Phi_m(k+1) <= beta Phi_m(k), beta < 1), which Lemma B does not supply.
(Remark: the l_1-mass bound used in D2(i), ||D(w'-w)||^2 = O(s_1^2 log(1/s_1)), only uses Phi_m(k) <= 2^{-m-k} and is unaffected.)

## 6.4 Remark F4 (K^scr can be infinite; scope of S3 4.3). SKETCH.
The peak part of Scr_m(s) is sum{min(Phi_k, s) : k in P_m, mu_k <= s} <= s #{k : Phi_k >= s} + sum_{Phi_k < s} Phi_k = O(s log(1/s)) and no better
in general: if mu_k <= 4^{-k} for a set of peaks of positive log-density (e.g. all k outside a sparse subsequence carrying the density of the
u_{k,m}; T built after zhat as in P1 2.1, with |u_{k,m}(zhat)| - theta Phi_m(k) prescribed), then for small s about (1/2)log_2(1/s) peaks with
Phi_k >= s have mu_k <= s and Scr_m(s) >~ (s/2) log_2(1/s). Then K^scr = +infinity is possible and 4.3 gives no threshold. (MS) in the block
excludes this. So 4.3's "rho-defect only" holds under (MS) (+ non-peak gaps bounded below off a finite set), not in general.

## 6.5 Numerical evidence produced by the referee (scripts in ctx/r3/S3ref_work/)
 * thmB_check.py / thmB_small.py: finite analogue of Theorem B confirmed for the C-referee certificate AND for random g with g(xi) = 0
   (both sides, values 1.10419 / 1.75850 matched to 4-5 digits below the onset radius; infeasible sides blow up like 1/|t|). Independent
   SOCP evaluation of p* (Clarabel, tol 1e-14), not the ellipsoid method used by the C referee.
 * rplus_indep.py: Lemma R+ on 17076 random/adversarial blocks, max violation 0.0.
