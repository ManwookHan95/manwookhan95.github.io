# Z2 part 2: three lemmas for first rows whose signatures are swallowed (valid for any admissible T unless stated)

Standing notation as in G3 part 2: f in S_{p*}, g in C(f), eta <= eta_1 (G3 4: eta_1 = min(eta_*, min_m M_m/2)), t <= t_eta, (B_+-, Omega_+-) a
two-sided decomposition of g at scale t, omega_+- := Omega_+- + d_+- w (sup-level parametrization, G3 2.4), Delta Omega := Omega_+ - Omega_-,
Delta c_k := lambda_k Delta Omega(k) (k a carrier of block m), Delta B := B_+ - B_- = -sum_k Delta c_k u_k, Delta d_m := d_{+,m} - d_{-,m} (G3 sign).

## 2.1 Lemma (a non-degenerate peak pins the uniform shift). PROVED (any admissible T).
Let k_1 be a peak of block m with alpha_{m,k_1} != 0. Then
   |Delta d_m| M_m <= t/(sigma_m |alpha_{m,k_1}|) + |Delta c_{k_1}|/lambda_{k_1}.
Moreover, for EVERY peak k of block m (degenerate or not), with sigma_k = sign w_m(k):
   sigma_k Delta Omega(k) <= -Delta d_m M_m ... more precisely  -sigma_k Delta Omega(k) - Delta d_m M_m = |omega_+(k)| + |omega_-(k)| >= 0.   (2.1.1)
*Proof.* G3 2.4(c): sigma_k omega_+(k) <= 0 <= sigma_k omega_-(k), hence |omega_+(k)| + |omega_-(k)| = sigma_k(omega_-(k) - omega_+(k)).
Since omega_+- = Omega_+- + d_+- w and w(k) = sigma_k M: sigma_k(omega_- - omega_+)(k) = -sigma_k Delta Omega(k) + (d_- - d_+) M = -sigma_k Delta Omega(k) - Delta d M.
This is (2.1.1). G3 2.4(c) also gives sum_{k in P} |alpha_k| |omega_+-(k)| <= t/(2 sigma_m) for each sign, so at k_1:
|alpha_{k_1}| (-sigma Delta Omega(k_1) - Delta d M) <= t/sigma_m. Together with (2.1.1) >= 0:
  -|Delta Omega(k_1)| - t/(sigma_m|alpha_{k_1}|) <= Delta d M <= |Delta Omega(k_1)|.  QED.
(Compare G3 3.5(c), which bounds Delta d through the identity Delta d M = <Dw, D Delta Omega>/C + O(t) and therefore needs ALL carriers of the block
pinned. Lemma 2.1 needs only ONE non-degenerate peak pinned; a non-degenerate peak exists in every block since ||alpha_m||_1 = 1.)

## 2.2 Lemma (the d-identity). PROVED (any admissible T). (G3 3.5(c)'s computation.)
   Delta d_m M_m = (1/(m C_m)) sum_k Phi_m(k) w_m(k) Delta c_k + r_m,   |r_m| <= 2t/sigma_m.
*Proof.* G3 2.4(d): d(omega_+-) - d_+- = O(t/sigma_m) with d(Omega + d w) = <Dw, D Omega>/C + d C; subtract the two sides and use M + C = 1 and
<Dw, D Delta Omega> = sum_k Phi_k^2 w(k) Delta Omega(k) = (1/m) sum_k Phi_k w(k) Delta c_k (lambda_k = m Phi_k). QED.

## 2.3 Lemma (theta-split of a one-sided switching). PROVED (any admissible T).
Let V in l_1 be supported in the contact set K = {j notin F : |z_j| = 1} and z-signed (z_j V_j >= 0), and suppose
Delta B 1_{F^c} = V + e. Then there are theta: supp V -> [0,1] and r_+, r_- in l_1(F^c) with
   B_+ 1_{F^c} = theta V + r_+,   B_- 1_{F^c} = -(1 - theta) V + r_-,   ||r_+||_1, ||r_-||_1 <= ||e||_1 + t/q_0.
*Proof.* Fix j notin F; x := B_+(j), y := B_-(j), so x - y = V_j + e_j. G3 2.3(b) gives sum_{j notin F} phi_{z_j}(x) <= t/(2q_0) and
sum phi_{-z_j}(y) <= t/(2q_0) (phi as in part 1).
 * V_j = 0: put theta_j := 0, r_+(j) := x, r_-(j) := y. Then |x| + |y| <= |x - y| + phi_z(x) + phi_{-z}(y) = |e_j| + phi_z(x) + phi_{-z}(y).
 * V_j != 0 (so |z_j| = 1): X := z_j x, Y := z_j y, v := |V_j| = z_j V_j > 0, X - Y = v + z_j e_j; phi_z(x) = 2X_-, phi_{-z}(y) = 2Y_+.
   theta_j := clamp(X/v, 0, 1), r_+(j) := z_j(X - theta_j v), r_-(j) := z_j(Y + (1 - theta_j) v).
   |r_+(j)| = dist(X, [0, v]) <= X_- + (X - v)_+ <= X_- + Y_+ + |e_j| (as X - v = Y + z_j e_j).
   |r_-(j)|: if 0 < theta_j < 1, = |Y + v - X| = |e_j|; if theta_j = 0 (X <= 0), = |X - z_j e_j| <= X_- + |e_j|;
   if theta_j = 1 (X >= v), = |Y| = |X - v - z_j e_j| and Y >= -|e_j| (X - v >= 0), so |Y| <= Y_+ + |e_j|.
Summing: ||r_+-|| <= ||e|| + sum_j (X_- + Y_+ + phi-terms on V_j = 0) <= ||e|| + t/q_0. QED.
Meaning: when the switching difference is (up to e) a z-signed contact vector V, the + side carries a fraction theta of V and the - side the
complementary fraction (with opposite sign), coordinatewise. ("Two-piece" structure with a general split theta, not only theta in {0,1}.)

## 2.4 Definition (resonant carriers). For the SLD operator and f with F finite:
 * B(f) := {l : m(l) <= N, theta_l(f) = 0} (exactly swallowed signature sets: z == sigma_l on S_l \ F for a sign sigma_l; part 1, 1.3(c)).
 * l in B(f) is RESONANT if (Res_l): z_j sigma_l u_l(j) = |u_l(j)| for every j notin F (the whole off-support part of sigma_l u_l is a z-signed
   contact vector; in particular u_l vanishes on non-contacts outside F). Put ũ_l := sigma_l u_l 1_{F^c} (z-signed, supported in K).
 * The resonant carrier l (block m = m(l), coordinate k_l = k(l)) is d-NEUTRAL if w_m(k_l) = 0, equivalently u_l(xi) = 0 (block-threshold lemma:
   off the peak set w_m(k) = C zeta_m(k)/(Phi_m(k)^2 sigma_m), zeta_m(k) = lambda_k u_k(xi); and w(k) = 0 forces k notin P_m since M_m > 0).
 * "Room off bad targets": for l notin B(f), theta*_l(f) := min_{sigma} sum_{s in S*_l} v_l(s)(1 + sigma z_s), S*_l := S_l \ (F cup U_{l' in B(f), l' > l} supp y_{l'});
   Lambda*_f(l) := prod_{l' <= l, m(l') <= N} (1 + 3/rho_{l'}), with rho_{l'} := theta*_{l'} for l' notin B(f) and rho_{l'} := 2||v_{l'} 1_{S_{l'} \ F}||_1 for l' in B(f).
 * Condition (W*): rho_l > 0 for all l, and liminf_l Lambda*_f(l)/(l 2^{l^3} Lambda°(l)) = 0.
 * Condition (H3) (bad targets avoid bad signatures): supp y_{l'} cap S_l = empty for all l < l' in B(f). (For l >= l' this is automatic by
   allowedness (a).)

## 2.5 Lemma (pinning modulo resonant switching). PROVED (SLD T).
Let f have F finite, every l in B(f) resonant, (H3) and (W*). Let l_* be a window index (Cset = {l <= l_*}), t in W(l_*), t <= min(t_eta, 1).
For l in B(f) put tau_l := -sigma_l Delta c_l. Then, with K* := (1/q_0 + 22) Lambda*_f(l_*):
 (a) sum_{l notin B(f)} |Delta c_l| <= K* t;
 (b) tau_l >= -K* t/... more precisely sum_{l in B(f) cap Cset} (tau_l)_- <= K* t;
 (c) Delta B 1_{F^c} = V + e with V := sum_{l in B(f) cap Cset} (tau_l)_+ ũ_l (z-signed, supported in K) and ||e||_1 <= 4 K* t + 6 t^2.
*Proof.* Pinning inequalities. (i) l notin B: on S*_l the vector -Delta B equals Delta c_l v_l + sum_{l' > l, l' notin B} Delta c_{l'} y_{l'}/n_{l'} (signature
privacy, allowedness (a) for coarser indices, and the definition of S*_l for finer bad indices); exactly as in 1.4,
  theta*_l |Delta c_l| <= E_l + 2 sum_{l' > l, l' notin B} kappa_{l',l} |Delta c_{l'}|,  E_l := sum_{s in S_l \ F} phi_{z_s}(Delta B(s)).
(ii) l in B: on S_l \ F, -Delta B = Delta c_l v_l + sum_{l' > l} Delta c_{l'} y_{l'}/n_{l'}, and by (H3) only l' notin B occur. z == sigma_l there, so by (F2), (F3)
of part 1, |Delta c_l| (1 + sigma_l sign Delta c_l) ||v_l 1_{S_l\F}|| <= E_l + 2 sum_{l'>l, l' notin B} kappa |Delta c_{l'}|, i.e.
  rho_l (tau_l)_- = 2 ||v_l 1_{S_l \ F}|| (sigma_l Delta c_l)_+ <= E_l + 2 sum_{l' > l, l' notin B} kappa_{l',l} |Delta c_{l'}|.
Solve the triangular system (i) over Cset \ B exactly as in 1.5 (the bad indices do not enter it): sum_{Cset \ B} |Delta c_l| <=
Lambda*(l_*)[sum E + (8/3) sum_{Fset} |Delta c|]; fine indices (both kinds): sum_{l > l_*} |Delta c_l| <= 6 t^2 (box bound, (P2)); sum_l E_l <= t/q_0 (1.2.1).
This gives (a) and then (b) from (ii) (rho_l >= 1/Lambda* is absorbed in Lambda*). (c): Delta B = -sum_l Delta c_l u_l; on F^c,
-sum_{l in B cap Cset} Delta c_l u_l = sum (tau_l) ũ_l = V - sum (tau_l)_- ũ_l, and the remaining terms (good carriers, fine carriers) have l_1-norm
<= K* t + 6 t^2 (||u_l||_1 <= 1). QED.

## 2.6 Lemma (resonant switching is d-neutral up to O(K* t); non-neutral switching through non-degenerate or wrongly signed peaks is pinned). PROVED (SLD T).
Same hypotheses. Fix a block m and a peak k_1 of w_m with alpha_{m,k_1} != 0 and iota(k_1, m) <= l_* (exists for l_* large). Then
 (a) |Delta d_m| M_m <= t/(sigma_m |alpha_{k_1}|) + K* t/lambda_{k_1} =: K_d* t;
 (b) | sum_{l in B cap Cset, m(l) = m} sigma_l Phi_m(k_l) w_m(k_l) tau_l | <= m C_m (K_d* + K* + 2/sigma_m) t;
 (c) if l in B cap Cset and k_l is a peak with alpha_{k_l} != 0, then |tau_l| <= lambda_l (t/(sigma_m |alpha_{k_l}|) + K_d* t);
     if k_l is a peak with sign w(k_l) = -sigma_l (degenerate or not), then tau_l <= lambda_l K_d* t.
*Proof.* (a) Lemma 2.1 with |Delta c_{k_1}| <= K* t (k_1 is a good carrier: B consists of exactly swallowed carriers... if k_1 happens to be in B, use (c)'s
first bound for it, which is self-contained). (b) Lemma 2.2: (1/(mC)) sum_k Phi_k w(k) Delta c_k = Delta d M - r; split the sum into good carriers
(<= (1/(mC)) K* t since Phi_k |w(k)| <= 1), fine carriers (<= 6t^2/(mC)) and bad coarse carriers, where Delta c_l = -sigma_l tau_l.
(c) (2.1.1) at k = k_l: |omega_+(k_l)| + |omega_-(k_l)| = -sigma_k Delta Omega(k_l) - Delta d M = sigma_k sigma_l tau_l/lambda_l - Delta d M >= 0, and if alpha_{k_l} != 0 the
left side is <= t/(sigma_m|alpha_{k_l}|) (G3 2.4(c)). If sigma_k sigma_l = -1 the nonnegativity gives tau_l <= -lambda_l Delta d M <= lambda_l K_d* t. QED.
Consequences. Resonant carriers sitting at a non-degenerate peak, or at a peak whose sign is opposite to sigma_l, are PINNED (their switching amplitude is
O(t)), and with one bad carrier per block, or with all bad carriers of a block having sigma_l w(k_l) of one sign, every non-d-neutral resonant
carrier is pinned (b). The only genuinely free switching is through strict non-peaks (or degenerate peaks with sign w = sigma_l) whose weighted
d-contributions cancel, in particular through d-NEUTRAL resonant non-peaks.
