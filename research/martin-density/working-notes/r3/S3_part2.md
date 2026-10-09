# S3 part 2: the exact one-sided second-order invariant (O2, second half) and complete recovery at P1's example

Setting and notation of part 1 (finite I, admissible T). Lemma 1.1 of part 1 holds verbatim at ANY f in S_{p*} with normer xi in place of x'
(replace c' by q_0, sigma'_m by sigma_m): its proof only uses A Fact C at the normer.

## 2.1 Definition (block-tame with arbitrary contacts: hypothesis (BT)).
f in S_{p*} satisfies (BT) if: F = supp a is finite; every Q_m (strict non-peaks of w_m) is finite; no block has degenerate peaks
(every peak k has margin mu_{k,m} := |u_{k,m}(xi)| - theta_m Phi_m(k) > 0, theta_m := M_m sigma_m/(m C_m)); and margin sparsity holds in every block:
   (MS)  sum{ Phi_m(k) : k in P_m, mu_{k,m} < s } = o(s)  as s -> 0+.
NO assumption is made on the contact set K = {j notin F : |z_j| = 1} (it may be infinite, even cofinite) or on z off F cup K.
(C-tame points (C_notes Def 6.0 with Dg = empty) are the (BT) points with K finite; P1's example (P1 2.2) is (BT) with K infinite, see 2.6.)

## 2.2 Definition (side-admissible decompositions; the one-sided invariant).
Let f satisfy (BT) and g in X* = l_1 with g(xi) = 0. For omega = (omega_m)_{m in I}, omega_m in R^{Q_m} (extended by 0), put d_m := d_m(omega_m) =
<D_m w_m, D_m omega_m>/C_m and b(omega) := g - sum_m R_m*(omega_m - d_m w_m) in l_1. The decomposition omega is SIDE-+ (resp. SIDE--) ADMISSIBLE if
   b(omega)_j = 0 for every j notin F cup K,   and  z_j b(omega)_j >= 0 (resp. <= 0) for every j in K.
Note b(omega)(zhat) = g(zhat) - sum_m <omega_m - d_m w_m, zeta_m>/q_0 = 0 automatically (A Lemma 4.2: <omega - d w, zeta_m> = 0).
The ONE-SIDED INVARIANTS are
   gamma^+(g) := inf{ Gamma_w(b(omega), omega) : omega side-+ admissible },  gamma^-(g) := inf{ ... side-- admissible }   (inf of the empty set = +infinity).
Two-piece data in the sense of P2A 1.6 are exactly pairs (omega+ side-+ admissible, omega- side-- admissible); kappa_w of part 1 is
max(Gamma_w(+), Gamma_w(-)), so min over two-piece data of kappa_w equals max(gamma^+, gamma^-) when both infima are attained.

## 2.3 Theorem B (exact one-sided second-order coefficient). PROVED.
Let f satisfy (BT) and g in l_1 with g(xi) = 0. Then
  (a) lim_{t -> 0+} 2(p*(f + t g) - 1)/t^2 = gamma^+(g)  and  lim_{t -> 0-} 2(p*(f + t g) - 1)/t^2 = gamma^-(g)   (in [0, +infinity]);
  (b) if gamma^+-(g) < infinity the infimum defining it is attained;
  (c) consequently every g in C(f) satisfies gamma^+(g) <= 1 and gamma^-(g) <= 1, and therefore carries two-piece data (P2A 1.6: b+- in l_1(F cup K),
      z-signed resp. (-z)-signed on K; omega+-_m finitely supported in Q_m) with kappa_w <= 1.
Remarks. (i) For K finite (C-tame), (c) recovers P1 3.8 (b(omega)_K must be both z- and (-z)-signed, so 0) and C Prop 8.1 with the referee's
missing hypothesis removed differently: the lower bound no longer needs decoupling. (ii) The C_referee counter-phenomenon (1.20: Gamma_2 < Gamma_w
at supports with many kinks) is exactly gamma^+- < Gamma_w(certificate): the optimal side decompositions re-split the certificate through
contacts with the cheap sign. Numerical confirmation in 2.7.

*Proof of the upper bound (limsup <= gamma^+).* Let omega be side-+ admissible with Gamma := Gamma_w(b, omega) < infinity, b := b(omega).
Base: for 0 < t < min_F|a_j|/(||b||_inf + 1) no coordinate of F changes sign, b vanishes off F cup K and z_j b_j = |b_j| on K, F and K are disjoint, so
||a + t b||_1 = ||a||_1 + t sum_F sign(a_j) b_j + t sum_K z_j b_j = ||a||_1 + t b(z). By (C 7.2), ||U*(a + t b)|| <= nu + t <e, U*b> + t^2 ||P_perp U*b||^2/(2(nu - t||U*b||)).
Adding and using b(z) + <e, U*b> = b(zhat) = 0: q*(a + t b) <= 1 + (t^2/2) h(b) nu/(nu - t||U*b||).
Blocks: V_m := w_m + t(omega_m - d_m w_m) satisfies N_m(V_m) <= 1 + (t^2/2) H_m(omega_m) C_m/(C_m - t||D_m(omega_m - d_m w_m)||) for small t (C Thm 7.1 Step 4
with N = infinity; omega_m is supported on finitely many strict non-peaks). Now f + t g = (a + t b) + sum_m R_m* V_m. Apply Lemma 1.1 (at f) with the transfer
data of Lemma 1.2 (Omega_m := Q_m) and eps_m := t_m t^2, the t_m solving the equalisation system of 1.4 for (h(b), H_m(omega_m)); exactly as in the
proof of Theorem A (with f' = f, no engineering), all pieces are <= 1 + (t^2/2)(Gamma + eta) + O(|t|^3) for any prescribed eta > 0 (eta controls the
inefficiency eta_1 of the transfer peaks). By A Fact A, limsup_{t->0+} 2(p*(f + t g) - 1)/t^2 <= Gamma + eta. Take the infimum over omega and eta -> 0.
(This is C Cor 7.2(c) for side-admissible rather than F-supported base parts.) Side - is symmetric (t < 0, (-z)-signed).

*Proof of the lower bound (liminf >= gamma^+).* Step 1 (test points). Let C_+ := { nu_c in c_00 : nu_c = 0 on F, z_j nu_{c,j} <= 0 for j in K } (inward moves of
contacts, arbitrary finitely supported moves of the other coordinates off F), and let k in H with <k, e> = 0. Put nu := U k + nu_c (in c_0),
kappa_2 := nu ||k||^2/(2 q_0) [here nu = ||U*a||], and choose k_2 in H with <U*e_j*, k_2> = -kappa_2 sign(a_j) (j in F) and <e, k_2> = kappa_2 - ||k||^2/(2q_0):
k_2 := kappa'_2 e + k_{2,perp}, kappa'_2 := -kappa_2 ||a||_1/nu, k_{2,perp} in E_F := span{U*e_j* : j in F} solving the Gram system
<k_{2,perp}, U*e_j*> = -kappa_2 sign(a_j) - kappa'_2 (Ue)_j (j in F) (U* injective, so the Gram matrix is invertible); it is orthogonal to e because
sum_F a_j(-kappa_2 sign a_j - kappa'_2 (Ue)_j) = -kappa_2 ||a||_1 - kappa'_2 nu = 0; and then ||k||^2/(2q_0) + <e,k_2> = ||k||^2/(2q_0) - kappa_2||a||_1/nu = kappa_2 because
||a||_1 + nu = q*(a) = 1. (This is C Prop 8.1 (i), re-derived by C_referee 1.20, with k no longer restricted to E_F.) For t > 0 put
   H_t := q_0 e + t k + t^2 k_2,   nu_2 := (U k_2) 1_{N \ F},   eta_t := xi + t nu + t^2 nu_2,   Z_t := eta_t - U H_t.
Coordinates: for j in F, Z_{t,j} = q_0 sign(a_j) + t^2 kappa_2 sign(a_j); for j notin F, Z_{t,j} = q_0 z_j + t nu_{c,j}. Since nu_c is finitely supported, inward on K
(where |z_j| = 1) and |z_j| < 1 on its support off F cup K, for 0 < t <= t_0(nu_c): |Z_{t,j}| <= q_0 for j notin F. Also ||H_t|| = q_0 + t^2 kappa_2 + O(t^3) (k orthogonal to e).
As B_{q**} = B_{l_inf} + U(B_H), q**(eta_t) <= max(||Z_t||_inf, ||H_t||) <= q_0 + t^2 kappa_2 + O(t^3). Since a is supported on F, a(nu_c) = 0, a(nu_2) = 0, and
a(U k) = <U*a, k> = 0, we get a(eta_t - xi) = 0 and the base excess E_q(eta_t - xi) := q**(eta_t) - q_0 - a(eta_t - xi) <= (t^2/2) (nu/q_0)||k||^2 + O(t^3).
Step 2 (blocks). With delta_1 := R_m nu, delta_2 := R_m nu_2 (both in l_1, nu, nu_2 in c_0), C Prop 8.1 (ii) (general Lemma 5.1(a) with overshoot; Q_m finite;
no degenerate peaks; (MS); re-derived by C_referee 1.20) gives E_m(t delta_1 + t^2 delta_2) <= (t^2/2) Hb_m(delta_1) + o(t^2), where Hb_m is the block quadratic
form of C Lemma 5.1(iii) (with the degenerate case z_Q = 0 as in C Prop 8.1 (v)). Hb_m(delta) depends on delta only through the finitely many numbers
ell_m(nu) := ( (u_{k,m}(nu))_{k in Q_m}, pi_m(nu) ), pi_m := R_m*(sign(w_m) 1_{P_m}) in l_1 (delta_Q = (m Phi_m(k) u_{k,m}(nu))_Q and S_P(delta) = pi_m(nu)).
Write Hb_m(R_m nu) = Qf_m(ell_m(nu)) with Qf_m a positive semidefinite quadratic form on R^{|Q_m|+1}.
Step 3 (the test inequality). C (8.1): since g(xi) = 0 and p** = f + Delta with Delta(eta) = E_q(eta - xi) + sum_m E_m(R_m**(eta - xi)) (C Lemma 6.1; exact),
p*(f + t g) >= (f + t g)(eta_t)/p**(eta_t) = 1 + t^2 g(nu) - Delta(eta_t) + O(t^3). Hence, for every admissible test pair (k, nu_c),
   liminf_{t->0+} 2(p*(f + t g) - 1)/t^2 >= Phi(k, nu_c) := 2 g(U k + nu_c) - (nu/q_0)||k||^2 - sum_m Qf_m(ell_m(U k + nu_c)).
Step 4 (Fenchel duality). Let ell := (ell_m)_m : c_0 -> R^n (n := sum_m (|Q_m| + 1)), Qf := sum_m Qf_m on R^n, and define on R^n the concave function
   Psi(y) := sup{ 2 g(U k + nu_c) - (nu/q_0)||k||^2 : k perp e, nu_c in C_+, ell(U k + nu_c) = y }  (sup of the empty set = -infinity).
Psi is concave (the constraint set is convex, the objective jointly concave), Psi(0) >= 0. If Psi(y_0) = +infinity for some y_0 then sup Phi = +infinity and
the lower bound holds trivially. Otherwise Psi is a proper concave function and Qf is finite and convex on all of R^n, so ri(dom Qf) meets ri(dom Psi);
by Fenchel's duality theorem (Rockafellar, Convex Analysis, Thm 31.1)
   sup_y [Psi(y) - Qf(y)] = min_{lambda in R^n} [ Qf^*(lambda) - Psi_*(lambda) ],
with Qf^*(lambda) := sup_y [<lambda, y> - Qf(y)], Psi_*(lambda) := inf_y [<lambda, y> - Psi(y)], and the minimum attained. Clearly sup_{k,nu_c} Phi = sup_y [Psi - Qf].
Compute both conjugates. Write phi_lambda := sum_i lambda_i ell_i in l_1 (ell_i ranging over the u_{k,m}, k in Q_m, and pi_m), so <lambda, ell(nu)> = phi_lambda(nu).
 * -Psi_*(lambda) = sup_{k perp e, nu_c in C_+} [ 2(g - phi_lambda/2)(U k + nu_c) - (nu/q_0)||k||^2 ] =: Bconj(g - phi_lambda/2). For beta in l_1:
   sup over k perp e of 2<U*beta, k> - (nu/q_0)||k||^2 equals (q_0/nu)||P_perp U*beta||^2 = q_0 h(beta); sup over nu_c in the cone C_+ of 2 beta(nu_c) is 0 if
   beta(nu_c) <= 0 on C_+, i.e. beta_j = 0 for j notin F cup K and z_j beta_j >= 0 on K, and +infinity otherwise. So Bconj(beta) = q_0 h(beta) on side-+ admissible beta,
   +infinity otherwise.
 * Qf^*(lambda) = sum_m sup_{y_m} [<lambda_m, y_m> - Qf_m(y_m)]. Block m: every linear functional of the block data (delta_Q, S_P(delta)) is
   delta -> 2 v(delta) with v = R_m*(omega~ + c w_m)-type, i.e. v(delta) = <omega~, delta> + c w_m(delta) restricted, omega~ on Q_m; C Prop 8.1 (v) (re-derived by the
   C referee, including the degenerate case) shows sup_delta [2 v(delta) - Hb_m(delta)] = sigma_m H_m(omega~) if v is BALANCED (v(zeta_m) = 0, i.e. c = -d_m(omega~)),
   and +infinity otherwise (Hb_m vanishes on the radial direction delta = zeta_m, along which 2v(delta) = 2 s v(zeta_m) is unbounded). Hence
   Qf^*(lambda) = sum_m sigma_m H_m(omega_m) if phi_lambda/2 = sum_m R_m*(omega_m - d_m(omega_m) w_m) for some omega_m in R^{Q_m}, and +infinity otherwise
   (phi_lambda determines the omega_m: T injective and Q_m is not all of N).
Therefore min_lambda [Qf^* - Psi_*] = min over omega with g - sum_m R_m*(omega_m - d_m w_m) side-+ admissible of [q_0 h(b(omega)) + sum_m sigma_m H_m(omega_m)] = gamma^+(g),
and the minimum is attained. With Step 3: liminf_{t->0+} 2(p*(f+tg) - 1)/t^2 >= sup Phi = gamma^+(g). Side -: replace C_+ by C_- (z_j nu_{c,j} >= 0) and t by -t
(the test points eta_t := xi + t nu + t^2 nu_2 with t < 0 move the contacts inward iff z_j nu_{c,j} >= 0). This proves (a) and (b).
(c): g in C(f) gives p*(f + t g) <= s(t) = 1 + t^2/2 + O(t^4), so both one-sided limits are <= 1. QED.

Comment on rigor. The only imported steps are C Prop 8.1 (i), (ii), (v) and C Lemma 6.1, (8.1), all re-derived by the C referee (1.20 lists them as
correct); the referee's gap was step (iii) (decoupling), which is replaced by Step 4 here. The weak-duality direction of Step 4 is elementary:
for side-+ admissible omega and any test pair, 2g(nu) = 2b(nu) + sum_m 2 v_m(nu) with 2b(nu) <= 2<U*b,k> (b(nu_c) <= 0) <= q_0 h(b) + (nu/q_0)||k||^2 and
2 v_m(nu) <= sigma_m H_m(omega_m) + Qf_m(ell_m(nu)).

## 2.4 Corollary B1 (structure of the fibre at (BT) points). PROVED.
If f satisfies (BT), then every g in C(f) satisfies g(xi) = 0, gamma^+(g) <= 1 and gamma^-(g) <= 1, and has two-piece data with kappa_w <= 1 whose
two sides are OPTIMAL side decompositions. (Conversely, if g(xi) = 0 and gamma^+-(g) < 1, then p*(f + t g) <= s(t) for all small |t|; membership in C(f)
then only depends on the large-|t| behaviour.) For P1's example this is P1 Thm 6.1 (C(f) in E_u) with the exact second-order constraint added.

## 2.5 Theorem C (recovery at (BT) points). PROVED under the stated alternatives.
Let f satisfy (BT), g in C(f), and let (omega+, omega-) be optimal side decompositions (2.3(b)); write Delta d_m := d_m(omega-_m) - d_m(omega+_m) and let I_0 be the
set of blocks where omega+_m or omega-_m is nonzero. Then g is in Ls(f) (i.e. (f, rho g) in cl NA for every rho < 1) in each of the cases
 (C1) Delta d_m = 0 for all m and |I_0| <= 1, or |I_0| >= 2 with the steering condition (S) of P2A 2.1;  [part 1, Theorem A]
 (C2) |I_0| = 1, Delta d > 0, and (TT) or (BR) of N2 Thm 2;                                                   [part 1, Cor A' + N2 Thm 2]
 (C3) |I_0| = 1, Delta d < 0, |Q_{m_0}| = 1 and (TT);                                                          [part 1, Cor A' + N2-referee Cor R]
 (C4) Delta d_m >= 0 for all m and the tuning-cone condition (TC) of P2x Thm 3.5.                              [part 1, Cor A' + P2x Thm 3.5]
Proof. By 2.3(c) the optimal data have kappa_w = max(gamma^+, gamma^-) <= 1, so rho^2 kappa_w < 1 for every rho < 1. Apply Theorem A / Corollary A'. QED.
(SUPERSEDED by part 3, Corollary D2: at (BT) points none of (S), (TT)/(BR), |Q_{m_0}| = 1, (TC) is needed; every mate is recovered.)

## 2.6 Corollary B2 (P1's example: every mate is recovered). PROVED.
Let T, f be as in P1 2.1-2.2 (any finite I containing 1). Then (f, rho g) is in cl NA((c_0,p), l_2^2) for EVERY g in C(f) and every rho < 1; i.e. f is in the
recoverable set R, and all of P1's "defect" is recovered by rebalanced engineered approximants.
*Proof.* (BT): F = {1}; Q_1 = {2}, Q_m = empty (m != 1) (P1 2.2(b)); every peak has margin mu_{k,m} >= q_0 psi(Phi_m(k)) > 0 with psi(phi) = min(1/4, 2 sqrt phi)
(P1 6.0), so there are no degenerate peaks, and for s < q_0/4: mu_{k,m} < s forces Phi_m(k) < s^2/(4 q_0^2), whence sum{Phi_m(k) : mu_{k,m} < s} <= 2 s^2/(4q_0^2) = o(s)
(Phi_m(k+1) <= Phi_m(k)/2: Phi_m(k) = 2^{-m-k} c_{l(k,m)} with c_l decreasing along k). (MS) holds. K = K' (infinite) is allowed.
Side decompositions: omega_1 = (mu/lambda_0) e_2 (mu real), all other omega_m = 0; d_1 = <D_1 w_1, D_1 omega_1>/C_1 = Phi_1(2)^2 w_1(2) mu/(lambda_0 C_1) = 0 since w_1(2) = 0; so
R_1*(omega_1 - d_1 w_1) = mu u (u = u_{2,1}), H_1(omega_1) = (Phi_1(2) mu/lambda_0)^2/C_1 = mu^2/C_1 (lambda_0 = Phi_1(2), m = 1), b = g - mu u. Side-+ admissibility:
supp(g - mu u) in {1} cup K' and g_j - mu u_j >= 0 on K' (z = 1 there; u_j > 0), i.e. g in E_u-type support and mu <= inf theta(g), theta_j := g_j/u_j. Hence
   gamma^+(g) = min_{mu <= inf theta(g)} Phi_g(mu),  gamma^-(g) = min_{mu >= sup theta(g)} Phi_g(mu),  Phi_g(mu) := q_0 h(g - mu u) + sigma_1 mu^2/C_1,
(Phi_g is a strictly convex quadratic in mu, so the minima are attained). For g in C(f), 2.3(c) gives gamma^+-(g) <= 1. The optimal data
(b+- = g - mu+- u, omega+- = (mu+-/lambda_0) e_2) are two-piece data with a single active block, Delta d = 0 (d = 0 on both sides), kappa_w <= 1. Theorem A
gives (f, rho g) in cl NA for every rho < 1. QED.
This answers the question "is every g in C(f) recovered at P1's example?": YES (PROVED). It upgrades P2A 2.4 (SKETCH, via shifts) to a proof and shows
that the shifted transport of A Thm 4.17 is not needed: the transfer-peak rebalancing (C Thm 7.4) is the exact mechanism, and the exact invariant is the
weighted coefficient minimised over side-admissible carriers mu (not the max-form kappa+- of P1 6.3).

## 2.7 Numerical confirmation (S3_work/gamma_side.py). 
Finite model of the C referee (C_work/Cref_work model.py, seed 21: n = 6, d = 3, F = {3,4,5}, one block with 5 coordinates + a non-peak transfer
coordinate, pure block certificate on k_0 = 1). gamma+- computed by a convex QP over omega in R^Q with the side constraints of 2.2:
| model | Gamma_w(certificate) | gamma^+ (QP) | referee's exact coefficient t>0 | gamma^- (QP) | referee's exact t<0 |
|---|---|---|---|---|---|
| free coordinates J = {0,1,2} | 0.29824 | 0.29824 | 0.29814 (t=1e-3) | 0.29824 | 0.29834 (t=-1e-3) |
| all off-support coordinates kinks (J empty) | 0.48511 | 0.29567 | 0.29567 (3e-4), 0.29568 (1e-4) | 0.28325 | 0.28325 (-3e-4), 0.28324 (-1e-4) |
The one-sided invariant reproduces the referee's exact one-sided coefficients to 5 digits, including the asymmetry between the two sides. (In a
finite model the upper bound needs a transfer coordinate, which the referee's model supplies; the lower bound of 2.3 holds in any finite model.)
