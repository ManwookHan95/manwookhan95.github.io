# V3 part 3: support swallowing of ANY profile through raised companions (resolves (O4-crit) and the support part of (O4-nd))

## 3.1 The designed base (design D^mu). PROVED.
Fix mu_s in (0, 1/2] with mu_s -> 0 (recommended: mu_s := 2^{-s^2-1}). H := l_2 with orthonormal basis (k_s), U k_s := mu_s e_s. U is compact
(diagonal, entries -> 0), has dense range (it contains c_00), ||U|| <= 1/2, U* e_s* = mu_s k_s, q*(a) = ||a||_1 + (sum_s mu_s^2 a_s^2)^{1/2}.
Every SLD-type design (SLD, SLD_G, D_sigma, D''', D_X, D^PW, D^Y) built over this base is admissible and N-free: those constructions use U
only through delta_l := min{2^{-l}, (4(1+||U||)||h_l||_1)^{-1}} and through "U compact with dense range"; Y4's results that need a diagonal
base (Lemma P1 diagonal case, Prop. P4, Cor. P5) apply. We call such a design D^mu.

## 3.2 Raise room
For a weight W in l_1, W >= 0, put M_mu^W(y) := sum{ mu_s W_s : s in F, |a_s| < y W_s } (mu-weighted active mass) and
  (RR_W)  M_mu^W(y) = O(y^{1+eps}) as y -> 0, for some eps > 0.
Lemma 3.1 (PROVED). (a) If |a_s| >= c_a mu_s^{1/(1+eps)} for all s in F (condition (RR_a)), then (RR_W) holds for every W in l_1.
(b) For mu_s = 2^{-s^2-1} and W = U_B (bad-carrier profile, U_B(s) := sum_{l in B}|u_l(s)|), (RR_W) holds as soon as
    log(U_B(s)/|a_s|) <= (1 - eps')s^2 for all large s in F cap supp U_B; in particular for every power-law profile |a_s| ~ v_l(s)^{1+b}
    (b > 0) on swallowed signature sets, sparse, critical (b = 1), super-critical or mixed.
Proof. (a) |a_s| < yW_s forces c_a mu_s^{1/(1+eps)} < y||W||_inf, i.e. mu_s < (y||W||_inf/c_a)^{1+eps}; sum <= ||W||_1 (y||W||_inf/c_a)^{1+eps}.
(b) Active s (|a_s| < y U_B(s)) satisfy 2^{-(1-eps')s^2} < y, so mu_s <= y^{1/(1-eps')}; M <= ||U_B||_1 y^{1+eps''}. For |a_s| ~ v_l(s)^{1+b}
with v_l(s) = delta_l 2^{-s}/n_l: log(v_l(s)/|a_s|) = O(s) = o(s^2). QED
Remark. (RR_W) is NOT a cushion condition: it compares the support values with the (designed) base entries mu_s, not with the signatures.
Compare (CS_W): m_W(y) := sum{W_s : |a_s| < yW_s} = o(y), which fails for critical and super-critical profiles. (RR) fails only for
"mu-thin" supports (|a_s| below a power of mu_s on infinitely many active coordinates), e.g. |a_s| = 2^{-2s^2}.

## 3.3 Lemma VP (value-preserving raises). PROVED.
Let L_0 be a finite set of carriers, gamma_k := <U*u_k, U*a> (k in L_0), and assume
  (ND_{L_0})  the linear map Lambda: l_1(F) -> R^{L_0}, Lambda(x)_k := sum_{s in F} mu_s^2 x_s (u_k(s) - a_s gamma_k/nu^2), is onto.
Then there are a finite F_0 subset F and c_0, C_0 > 0 such that for every raise Delta a with supp Delta a cap F_0 = {} and ||U*Delta a|| <= c_0
there is Delta a'' in l_1(F_0) with ||Delta a''||_1 <= C_0 ||U*Delta a||, |Delta a''_s| <= |a_s|/2, such that the first row f^# with forced data
((a + Delta)/q*(a + Delta), z), Delta := Delta a + Delta a'', satisfies u_k(zhat^#) = u_k(zhat) for every k in L_0. Lemma 2.3 holds for this
f^# with the extra error 2||Delta a''||_1 (and lambda >= 1 once C_0 ||U*Delta a|| <= ||Delta a||_1 / 2... in general add a tiny extra raise).
Proof. Lambda(e_s), s in F, span R^{L_0}; pick finitely many (F_0). For x in l_1(F_0) put e(x) := U*(a + Delta a + x)/||U*(a + Delta a + x)|| and
G(x)_k := <U*u_k, e(x) - e>. G is C^infinity on {||U*(Delta a + x)|| <= nu/2}, with uniformly bounded second derivatives, and
DG(x) xi = <U*u_k, P^perp_{e(x)} U* xi>/||U*(a + Delta a + x)||; at Delta a = 0, x = 0 this is Lambda(xi)_k/nu (diagonal U:
<U*u_k, U*xi> = sum mu_s^2 u_k(s) xi_s and <U*xi, e> = sum mu_s^2 a_s xi_s/nu), onto on l_1(F_0); by continuity DG(x) has a right inverse of
norm <= 2 C_Lambda for ||U*Delta a||, ||x|| small. |G(0)| <= ||U||·2||U*Delta a||/nu (Lemma 2.1(b),(c)). Graves' (quantitative surjective
implicit function) theorem gives x with G(x) = 0, ||x||_1 <= C_0 ||U*Delta a||. Since F_0 is finite and fixed, |x_s| <= |a_s|/2 for c_0 small.
The extra error in Lemma 2.3: ||a + Delta||_1 >= 1 - ||U*a|| + ||Delta a||_1 - ||Delta a''||_1 and q*(a + Delta + lambda r B) <= q*(A) +
||Delta a||_1 + ||Delta a''||_1 + ||U*Delta||. QED
Remark. (ND_{L_0}) fails iff a nontrivial combination u := sum c_k u_k satisfies u|_F = kappa a|_F for a constant kappa (then sum c_k val_k
moves by -kappa nu ||e^# - e||^2/2 under every move on F: second order, but nonzero). On the deep part of a signature set S_l cap F this
forces |a_s| proportional to v_l(s), i.e. a cushion-dominated (sparse) profile there; (ND) is generic.

## 3.4 Theorem RS (support swallowing of any profile). PROVED (modulo the inspection items (I1)-(I3), which are of the same kind as
Lemma U / Lemma P2 of earlier rounds).
Design: D^mu over the SLD operator (or D_sigma); N >= 1, p = p_N. Let f in S_{p*} (F arbitrary) satisfy R1's (W*), (H2), (B_fin), and
 (H3') no bad carrier sits at a degenerate peak;
 (ND_B) Lemma VP's surjectivity for L_0 := B;
 (RR_B) M_mu^{U_B}(y) = O(y^{1+eps}) for some eps > 0.
Then f in Rec. [Compared with Theorem R1 (Z5_ref), (CS_B) is replaced by (RR_B); compared with Y3 Theorem 3.5 / Y3_ref Prop. 3.4, no
d-neutrality, no supp u_l subset F, no monochromatic sign, no (QM), no super-criticality, no rho-threshold.]
Proof. Fix g in C(f), rho in (0,1), eta_0, kappa_0, eps_tr, eta as in R1. Let C_tau, K*, K_j := (1 + ||U||)K^R_2(l_j), c_flat, t_1 be R1's
constants AT f (Step 2' and Step 4 of R1), with a factor 2 of room.
Step 1 (windows). By (W*) pick window indices l_j -> infinity with Lambda*_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0. Put
n_j := ceil(48 rho^2 K_j/(c_flat(1 - rho^2))) and choose the top T_j of a sub-window S_j := {T_j 2^{1-i} : i <= n_j} inside W(l_j) with
  C (C_tau T_j)^{eps} log(1/T_j) <= theta_j 4^{-n_j},  theta_j -> 0
(possible: n_j = O(Lambda*_f(l_j)) = o(n^w_{l_j}), so T_j := T_hi(l_j) 2^{-ceil((2/eps)(2 n_j + log(C/theta_j)))} still has T_j 2^{-n_j} >= T_lo(l_j)).
Step 2 (companion). y_j := 4 C_tau T_j. Raise along W := U_B at level y_j: Delta a_s := s_s(y_j U_B(s) - |a_s|)_+ (s in F); then add the
correction of Lemma VP for L_0 := B; f_j := the resulting row. By Lemma 2.1, 2.2, 3.1, 3.3: lambda_j - 1 <= 2 y_j ||U_B||_1 -> 0,
||U*Delta|| <= y_j M(y_j) + ..., eps'_j := 2||U*Delta|| + 2||Delta a''||_1 + p*(L*(w_j - w)) = O(y_j^{2+eps} log(1/y_j)) <= theta_j (T_j 2^{-n_j})^2 (Step 1),
p*(f_j - f) -> 0, and
  (i) |a^{(j)}_s| >= y_j U_B(s)/lambda_j >= 2 C_tau T_j U_B(s) on F (the cushions dominate the bad profile at all scales t <= T_j);
  (ii) val_l = u_l(zhat) is unchanged for l in B, all block scalars move by O(eps_e), z, F, K, J, rooms, B, eps_l are unchanged;
       hence the cone Z_f of Lemma lem:exactswitch (rows: tau_l >= 0 for l in B_K, target rows on T_0, peak rows, d-rows
       sum_{m(l)=m} eps_l val_l tau_l = 0 -- recall q_l = eps_l q_0 val_l/sigma_m) is the same at f_j, with the same Hoffman constant;
       statuses of the bad carriers (strict non-peaks with gaps >= gamma_B, non-degenerate peaks: (H3')) and of the (H2) peaks are unchanged
       for j large (their margins/gaps are f-constants, the scalars move by O(eps_e)).
Step 3 (approximate decompositions at f_j). g_j := g - (g(xi_j)/q_0^{(j)}) a^{(j)}; |g(xi_j)| <= ||g||_1 ||xi_j - xi||_inf = O(eps_e). By Corollary 2.4,
p*(f_j + t g_j) <= 1 + (t^2/2)(1 + eta'_j) for t in [T_j 2^{-n_j}, T_j], eta'_j -> 0, and g_j(xi_j) = 0. Lemma lem:twosided at f_j gives exact
decompositions with this budget; Lemmas lem:smallness, lem:budget, lem:suplevel, lem:box, lem:switchbudget, lem:modswallow, lem:badpeaks
hold at f_j with s(t) - 1 replaced by (1 + eta'_j)t^2/2 (constants multiplied by at most 2) [(I1): these lemmas use the budget only through
s(t) - 1 <= t^2/2 and g(xi) = 0; lem:smallness by compactness along f_j -> f].
Step 4 (exact window data at f_j). Run R1's Steps 1-3 at f_j. By (ii) the exact switching tau' lies in Z_{f_j} = Z_f with
sum|tau - tau'| <= C_f K* t, and |tau'_l| <= C_tau [(I2): Z5 Lemma 5.2's injectivity modulus is continuous in (e, zhat)]. On F,
|X_s| <= C_tau U_B(s) <= 2A^{(j)}_s := 4|a^{(j)}_s|/t for t <= T_j by (i); so R1's deep set D_t is EMPTY, and Claim 3.2 gives d-neutral two-piece
data (b^pm, omega^pm) AT f_j for g_{j,t} with (s b^+)_- <= 3|a^{(j)}|/t, (s b^-)_+ <= 3|a^{(j)}|/t, |b^theta| <= 4|a^{(j)}|/t on F,
p*(g_j - g_{j,t}) <= K_j t, Gamma_w <= (1 + 2kappa_0)^2 = 1 + eta_0/2, and the block size conditions of Lemma R2.
Step 5 (pieces). Lemma R2 at f_j with U_* = 0 (no sparse part): p*(f_j + r g_{j,t}) <= 1 + (r^2/2)(1 + eta_0) for 0 < |r| <= c_flat t on the
respective sides, with c_flat, t_1 independent of j [(I3): Lemma R2's constants depend on f_j only through nu, q_0, sigma_m, C_m, M_m, the transfer
data (Lemma lem:persistence) and the cushion bound, all uniform along f_j -> f]. Hence (b) of Theorem 2.5 (pieces of rho g_{j,t}).
Step 6. Theorem 2.5: (a) is Corollary 2.4 (with g, and p*(g - g_j) = O(eps_e) absorbed into eps'_j and K_j), (c), (d) by Steps 1-2, and (e):
the averaged data are d-neutral two-piece data at f_j for gbar_j with kappa_w <= 1 + eta_0/2 and (s bbar^+)_-, (s bbar^-)_+, |bbar^theta| <=
4|a^{(j)}|/T_lo, so (CS-side) holds at f_j (m(x) = 0 for x < T_lo/4); Theorem 2.1 (Y3) at f_j with I_- empty gives (f_j, rho' rho gbar_j) in cl NA
for all rho' < 1, hence (f_j, rho gbar_j) in cl NA. So (f, rho g) in cl NA; let rho -> 1. QED
Remarks 3.5. (a) The mechanism: in the critical case the decomposition at scale t flips on {v_l(s) <~ tD} with mass ~ D^2 t; at f_j these
coordinates carry cushions >= C_tau T_j v_l(s) >= the whole switching, at the cost of a raise of l_1-mass ~ T_j (FIRST order), which is
harmless because a same-sign raise on F commutes with the triangle inequality (Lemma 2.3) and its Hilbert/normer footprint is
||U*Delta a|| <= max_{active} mu_s ||Delta a||_1, super-polynomially small for D^mu. Y3's "nested raises cost ~ kappa D^2 T_0^2 = order of
the slack" and Y3_ref 3.3 are correct for the decoupling requirement p*(f_j - f) = o(T_lo^2) of Z3 Theorem E, but that requirement is
replaced by eps'_j = o(T_lo^2) in Theorem 2.5. (b) The referee's factor 2 (cushion sharing) is a property of R1's deep assignment; at f_j
there is no deep set at all. (c) (H3') can presumably be relaxed to R1's (H3-inf) (B_K carriers at degenerate peaks with sign -eps_l): their
status at f_j may change by O(eps_e), but Lemma lem:badpeaks(c) uses only the box inequality at k(l), which survives a gap or margin of
size O(eps_e) << t^2 (SKETCH). (d) (ND_B) can be dropped if the degenerate second-order drift is handled by Hoffman stability (SKETCH).
