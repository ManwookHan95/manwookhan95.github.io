# Z4 referee, part 1: Props 1.2, 1.3; Lemmas 2.1-2.3; Prop 2.4; Theorem A steps 1-9 (first pass)

## Prop 1.2 (distance of far lowerings): conclusion CORRECT, step (iv) WRONG AS WRITTEN, fixed here.
Step (iv) of the proof bounds sum_k lambda_k |w^L(k)-w(k)| by m eps_L sum_k (K_C(Phi_k+v_k) + v_k/rho_0) and then uses
"sum_k v_k <= m/(2 rho_0)". This is false: v_k = m|u_k(zhat)|/|R** zhat| does not tend to 0 (the u_k are dense in S_{q*}), so
sum_k v_k = infinity. (The bound m/(2rho_0) is a bound for sup_k v_k, or for sum_k Phi_k v_k up to a factor.) The step confuses
Phi_k|w^L(k)-w(k)| (what the clamp formula controls additively) with lambda_k|w^L(k)-w(k)| = m Phi_k |w^L(k)-w(k)|.
FIX (PROVED). For a coarse carrier k (l(k) <= L) one has u_k(zhat^L) = u_k(zhat) (Lemma 1.1), hence v^L_k = r v_k with the SAME
ratio r := |R** zhat|/|R** zhat^L| for all coarse k of the block, |r - 1| <= eps_L/rho_0. The clamp formula gives
w(k) = s_k min(M, C v_k/Phi_k), w^L(k) = s_k min(M^L, C^L r v_k/Phi_k), s_k = sign u_k(zhat). For beta > 0, x >= 0, M > 0:
|min(M, beta x) - min(M, x)| <= |beta - 1| M  (case analysis: if beta >= 1 the difference is <= (beta-1)x when x < M and 0 otherwise,
and (beta-1)x < (beta-1)M; if beta < 1, the difference is <= min(M,x) - beta min(M,x) <= (1-beta)M).
Hence for every coarse k: |w^L(k) - w(k)| <= |M^L - M| + |C^L r/C - 1| M <= K_C eps_L + (K_C eps_L + C eps_L/rho_0)/C =: K_w eps_L,
uniformly in k (sup-norm control, no summation needed), with K_C from step (iii) (which is correct: it only uses Phi-weighted sums).
Then sum_{coarse} lambda_k |w^L(k)-w(k)| <= K_w eps_L sum_k lambda_k <= K_w eps_L, and the fine part is <= 2 eps_L as written.
So q*(f^L - f) <= (1+||U||) N (K_w + 2) eps_L. The constant depends on rho_0, C_m, c_* (a fixed non-degenerate peak), i.e. on coarse data.
(Without the multiplicative structure, the clamp estimate only gives sum_k min(2Phi_k, C eps_L) ~ eps_L log(1/eps_L) or L eps_L.)
Step (iii) uses C^L -> C (root localisation window): this follows from f^L -> f, known qualitatively (Remark rem:lemmaZ(c)); not circular.

## Prop 1.3: CORRECT. (a) slack arithmetic fine (also |tau| >= 1 case). (b) box bound only needs N_m(w^L + t Theta) <= s(t), t <= 1,
which holds for two-sided decompositions of rho g at f^L at scales t >= t_L. (c) base data on S_l, supp y_l (l <= L) unchanged;
NOTE: "swallowing status" in (c) is base data only; block data of coarse carriers move by O(eps_L) (sup norm, by the fix above), so
coarse near-threshold peaks/non-peaks may change status at f^L. Harmless for the statement. The "Consequence" paragraph is interpretive.

## Lemma 2.1: CORRECT (checked: supp u_l in supp y_l ∪ S_l; S_l \ (T(U) ∪ F) infinite; phi_z(x) = 0 with |z|<1 forces x = 0).
## Configurations / G*(l): CORRECT, one fixable gap: the configuration uses U ⊂ L_N ∩ [1,l], so G*(l) depends on N and SLD_G would
depend on N, whereas Lemma martintail needs ONE operator for infinitely many N. FIX: let U range over all subsets of [1,l] (all ladder
indices); then G*(l) dominates every G*_N(l) and the design is N-independent. Also: Lemma 2.2 needs l >= max F (n = max F <= l) -- stated.
## Lemma 2.3 (d-repair): CORRECT (c_U sublinear; cost is a property of V = sum eps tau u 1_{F^c}, so zero extension keeps zero cost).
## Prop 2.4: CORRECT ((P3) inequalities hold because the inflated base >= 1). Optional clause c_l <= (delta_l ||h_l||_1)^2 cannot hold at
l = 1 with c_1 = 1 (delta_1||h_1||_1 <= 1/(4(1+||U||)) < 1); impose it for l >= 2 (recursion c_{l+1} := min{c_l/4, T_lo(l)^3,
(delta_{l+1}||h_{l+1}||_1)^2}, computable since delta_{l+1}, h_{l+1} are fixed in (D0)). Check where it is used (Lemma 5.3).
