ERRATUM (see G3_notes.md, authoritative): Lemma 1.4(a) also holds at FREE coordinates (|x| - z x >= 2(z x)_- for |z| <= 1); the
statement of Cor. 1.8 is restated cleanly in the notes (-C_f t/U_N <= gamma'_+ <= C_f t/max(|Mj|, U_far)); Lemma 1.7(i) reads
S_0(t) = t/q_0 + (sigma/q_0) eta_P (1 + M Phi_P^2/C) + r_Q (same quantity).  The notes add Theorem CL (conservation law).

# G3 part 1 (Round 14, adversarial): norm-level pinning lemmas at an arbitrary first row

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Setting: finite block set I, p = p_N, any admissible T (nothing about the
design is used in this part).  f in S_{p*} has forced data (xi, q_0, a, w, F, z, zhat, e, nu) [I, Prop. 1.9]: f = a + L^*w,
q*(a) = ||a||_1 + nu = 1, nu = ||U^*a||, e = U^*a/nu, zhat = z + U e, xi = q_0 zhat, F = supp a, z = sgn a on F, ||z||_inf <= 1.
zeta_m := R_m^** xi, sigma_m := |zeta_m|_m, and q_0 + sum_m sigma_m = p^**(xi) = 1.  lambda_k := m Phi_m(k) (block m understood), so that
R_m^* Theta = sum_k lambda_k Theta(k) u_{k,m}.  s(t) := (1 + t^2)^{1/2}.  Excess functions [I, Sec. 7.1]:
   G_b(A) := q*(A) - A(zhat) >= 0,      G_m(W) := N_m(W) - <W, zeta_m>/sigma_m >= 0     (sigma_m > 0).
A coordinate j is a CONTACT if j notin F and |z_j| = 1, FREE if j notin F and |z_j| < 1.

Purpose.  The residuals (R0)/(R1) of Addendum 13 are statements about the companion construction.  Before constructing rows at
which they persist, we record what the corresponding resonances force on EVERY mate of f, independently of any construction.
All statements below are about exact decompositions of f +- t g at a single scale t, which exist for every g in C(f).

## 1.1 The weighted excess budget

LEMMA 1.1 (weighted excess budget).  PROVED.  Let h in X^* with h(xi) = 0 and f + h = A + sum_m R_m^* W_m with
max(q*(A), max_m N_m(W_m)) <= pi.  Then
      q_0 G_b(A) + sum_m sigma_m G_m(W_m) <= pi - 1.
Proof.  Since xi = q_0 zhat and (R_m^* W_m)(xi) = <W_m, R_m^** xi> = <W_m, zeta_m>,
   q_0 G_b(A) + sum_m sigma_m G_m(W_m) = q_0 q*(A) + sum_m sigma_m N_m(W_m) - (A + sum_m R_m^* W_m)(xi)
                                      <= pi (q_0 + sum_m sigma_m) - (f + h)(xi) = pi - f(xi) - h(xi) = pi - 1.   QED

LEMMA 1.2 (coordinate form of the base excess).  PROVED.  For A in l_1,
      G_b(A) >= E_b(A) := sum_j (|A_j| - z_j A_j),   every summand >= 0,
and the summand at j equals 2 (z_j A_j)_- at a contact, 2(-s_j A_j)_+ at j in F (s_j := sgn a_j = z_j), and is >= (1 - |z_j|)|A_j| at a
free coordinate.
Proof.  A(zhat) = A(z) + <U^*A, e>, so G_b(A) = (||A||_1 - A(z)) + (||U^*A|| - <U^*A, e>) and the second bracket is >= 0 (||e|| = 1).
||A||_1 - A(z) = sum_j (|A_j| - z_j A_j) with |z_j| <= 1.  At a contact |x| - z_j x = 2(z_j x)_-; at j in F, z_j = s_j and
|x| - s_j x = 2(s_j x)_- = 2(-s_j x)_+; at a free coordinate |x| - z_j x >= (1 - |z_j|)|x|.  QED

COROLLARY 1.3 (two-sided budget at scale t).  PROVED.  Let g in C(f) and t > 0.  There are decompositions
      f + t g = A_+ + L^* W_+,      f - t g = A_- + L^* W_-,      max(q*(A_+-), max_m N_m(W_{+-,m})) <= s(t),
and every such pair satisfies E_b(A_+) + E_b(A_-) <= 2(s(t) - 1)/q_0 <= t^2/q_0.
Proof.  p*(f +- t g) <= s(t) because g in C(f) (equivalently p*(cos(th) f + sin(th) g) <= 1 for all th).  The infimum defining
p*(h) = inf{max(q*(A), ||W||_{V*}) : h = A + L^*W} is attained: the sublevel sets {W : ||W||_{V*} <= c} are weak*-compact, L^* is
weak*-to-weak* continuous, and A = h - L^*W -> q*(A) is weak*-lsc (q* is a dual norm on l_1 = c_0^*).  Apply Lemma 1.1 with h = +-tg
(h(xi) = 0 because the normer xi of f satisfies g(xi) = 0 for every mate) and drop the nonnegative block excesses; then Lemma 1.2.  QED

NOTATION.  For a pair as in 1.3 put B_+ := (A_+ - a)/t, B_- := (a - A_-)/t, Theta_+ := (W_+ - w)/t, Theta_- := (w - W_-)/t.  Then
      g = B_+ + L^*Theta_+ = B_- + L^*Theta_-,       V := B_+ - B_- = L^*(Theta_- - Theta_+)        (the SWITCHING VECTOR at scale t),
and for a carrier k of block m, gamma_k := lambda_k (Theta_{-,m}(k) - Theta_{+,m}(k)) (its SWITCHING AMPLITUDE at scale t), so that
V = sum_{m,k} gamma_k u_{k,m}.  Let e_j^+- denote the summand of E_b(A_+-) at j.

## 1.2 Sign constraints on the switching vector

LEMMA 1.4 (pointwise switching constraints).  PROVED.  With the notation above, at every coordinate j:
 (a) contact:   z_j V_j >= -(e_j^+ + e_j^-)/(2t);
 (b) j in F:    s_j V_j >= -(2|a_j| + (e_j^+ + e_j^-)/2)/t;
 (c) free:      |V_j| <= (e_j^+ + e_j^-)/(t (1 - |z_j|)).
Consequently, for every set E of contacts and support coordinates,
      sum_{j in E} (o_j V_j)_- <= 2 alpha(E)/t + t/(2 q_0),       o_j := z_j (= s_j on F),  alpha(E) := sum_{j in E ∩ F} |a_j|.   (1.1)
Proof.  At a contact, A_+(j) = t B_+(j) and A_-(j) = -t B_-(j), so e_j^+ = 2t (z_j B_+(j))_- and e_j^- = 2t (z_j B_-(j))_+; hence
z_j V_j = z_j B_+(j) - z_j B_-(j) >= -(z_j B_+(j))_- - (z_j B_-(j))_+ = -(e_j^+ + e_j^-)/(2t).  At j in F, A_+(j) = a_j + t B_+(j), so
e_j^+ = 2(-s_j t B_+(j) - |a_j|)_+ and (-s_j B_+(j))_+ <= (|a_j| + e_j^+/2)/t; likewise A_-(j) = a_j - t B_-(j) gives
(s_j B_-(j))_+ <= (|a_j| + e_j^-/2)/t; and s_j V_j >= -(-s_j B_+(j))_+ - (s_j B_-(j))_+.  At a free coordinate
e_j^+- >= (1 - |z_j|) t |B_+-(j)|.  For (1.1) sum (a), (b) over E and use sum_j (e_j^+ + e_j^-) <= t^2/q_0 (Corollary 1.3).  QED

So at every scale the switching vector is z-signed on contacts and s-signed on the support up to an l_1-error 2 alpha(E)/t + t/(2q_0):
cushions |a_j| enter only through alpha(E)/t, and everything else is O(t).  This is the scale-t form of side admissibility of
two-piece data [I, Def. 7.7], valid for every mate at every row, with no exactness assumption.

## 1.3 Pinning of a carrier by private coordinates of both orientations

LEMMA 1.5 (private pinning).  PROVED.  Let k be a carrier of block m and E a set of contacts and support coordinates (no free
coordinate).  Write V_j = gamma_k u_k(j) + psi_j (psi collects the other carriers), orient j by o_j := sgn(z_j u_k(j)) (z_j = s_j on F),
and put E^+- := {j in E : o_j = +-1}, U^+- := sum_{E^+-} |u_k(j)|, alpha^+- := alpha(E^+-), Psi^+- := sum_{E^+-} |psi_j|.  Then
   -(2 alpha^+/t + t/(2 q_0) + Psi^+)/U^+  <=  gamma_k  <=  (2 alpha^-/t + t/(2 q_0) + Psi^-)/U^-          (1.2)
(a side is void if U^+- = 0).
Proof.  For j in E^+, z_j V_j = gamma_k |u_k(j)| + z_j psi_j; summing Lemma 1.4 over E^+ gives gamma_k U^+ >= -(2 alpha^+/t + t/(2q_0)) - Psi^+.
For j in E^-, z_j V_j = -gamma_k |u_k(j)| + z_j psi_j, giving gamma_k U^- <= 2 alpha^-/t + t/(2q_0) + Psi^-.  QED

COROLLARY 1.6 (kind-(iv)-type carriers are pinned at f, on both sides).  PROVED.  Let l be a carrier whose coordinates in a set N
are contacts or support coordinates of the sign eps_l (z_j u_l(j) has the sign eps_l there: "data-sign near coordinates") and whose
coordinates in a set E_far are contacts or support coordinates of the opposite orientation ("anti-sign far coordinates"), both
private up to psi.  Then for every mate g and every scale t
   -(2 alpha(N)/t + t/(2q_0) + Psi_N)/U_N  <=  eps_l gamma_l  <=  (2 alpha(E_far)/t + t/(2q_0) + Psi_far)/U_far.
In particular, if alpha(N) + alpha(E_far) <= t^2 (thin cushions), then
      |gamma_l| <= [ (2 + 1/(2q_0)) t + Psi_N + Psi_far ] / min(U_N, U_far).
Proof.  Lemma 1.5 with E^{sgn eps_l} = N and E^{-sgn eps_l} = E_far, multiplied by eps_l.  QED
Reading.  For the kind-(iv) carriers of (R1) (near coordinates S_th of the data sign; pull ranges anti-sign super-thin support or
anti-sign contacts, H2 Thm H2.B(i)), the switching amplitude at f is <= C t/min(U_N, U_far) at every scale t >= (alpha/1)^{1/2}:
the carrier can switch with amplitude of order one only at scales t >~ min(U_N, U_far), i.e. above the mass of its anti-sign far
part.  (This is the norm-level content of "kind (iv) is one-sided": the data sign is the only switching direction that is not
pinned by the near coordinates, and the anti-sign far mass pins that direction too below its own scale.)

## 1.4 Pinning of a pair by a contact minor

LEMMA 1.7 (pair pinning by a wrong-signed contact minor).  PROVED (under the stated hypotheses; any admissible T).  Fix a block m
(index dropped), a scale t and decompositions as in 1.3; Delta Theta := Theta_- - Theta_+.  Assume
 (P1) [unshifted: peak switching pinned]  |Delta Theta(k)| <= eta_P for every peak k in P;
 (P2) [two switching carriers]  for the strict non-peaks Q, gamma_k = lambda_k Delta Theta(k) satisfies
      |sum_{k in Q \ {k_1,k_2}} u_k(zhat) gamma_k| <= r_Q;
 (P3) j is a contact, and V_j = gamma_1 u_1(j) + gamma_2 u_2(j) + psi_j  (u_i := u_{k_i}, gamma_i := gamma_{k_i}; psi_j collects the other
      carriers, including the peaks).
Put Mj := u_1(j) u_2(zhat) - u_2(j) u_1(zhat) and S := u_1(zhat) gamma_1 + u_2(zhat) gamma_2.  Then
 (i)  |S| <= S_0(t) := (sigma/q_0) [ t max(1, 1/sigma) + eta_P (1 + M Phi_P^2/C) ] + r_Q,     Phi_P^2 := sum_{k in P} Phi(k)^2;
 (ii) z_j gamma_1 Mj/u_2(zhat) >= -[ (e_j^+ + e_j^-)/(2t) + |psi_j| + |u_2(j)/u_2(zhat)| S_0(t) ]   (if u_2(zhat) != 0).
Hence, if the orientation of gamma_1 is forced (e.g. by Corollary 1.6) and z_j sgn(gamma_1) Mj/u_2(zhat) < 0 (WRONG SIGN), then
      |gamma_1| <= |u_2(zhat)| [ t/(2 q_0) + |psi_j| + |u_2(j)/u_2(zhat)| S_0(t) ] / |Mj|.
Proof.  Put L(Theta) := <Theta, zeta>/sigma.  By the threshold structure [I, block-threshold lemma] zeta/sigma = alpha + D^2 w/C with
alpha supported on P, sgn alpha = sgn w there, ||alpha||_1 = 1, C = ||Dw||_2, M = ||w||_inf, M + C = 1; hence
L(Theta) = sum_P |alpha(k)| sgn(w(k)) Theta(k) + <D Theta, D w>/C.
Step 1 (levels).  From q*(a + tB) = 1 + t B(zhat) + G_b(a + tB) and N(w + t Theta) = 1 + t L(Theta) + G(w + t Theta) (both excesses
>= 0), the bounds q*(A_+), N(W_+) <= s(t) give t B_+(zhat) <= s(t) - 1 and t L_m(Theta_{+,m}) <= s(t) - 1 for every block, and the
first-order identity (A_+ - a)(xi) + sum_m <W_{+,m} - w_m, zeta_m> = t g(xi) = 0 reads q_0 B_+(zhat) + sum_m sigma_m L_m(Theta_{+,m}) = 0.
A family of reals x_i with sum 0 and x_i <= c_i (s(t)-1), sum_i c_i = 1, satisfies x_i >= -(s(t) - 1); with x = sigma_m t L_m this gives
|L_m(Theta_{+,m})| <= max(1, 1/sigma_m) (s(t) - 1)/t <= max(1, 1/sigma_m) t/2.  The minus side is identical (f - tg = A_- + L^*W_-,
A_- = a - t B_-, W_- = w - t Theta_-).  So |L(Delta Theta)| <= max(1, 1/sigma) t.
Step 2 (the d-row).  By (P1) the peak part of L(Delta Theta) is at most eta_P in modulus.  Split <D Delta Theta, D w>/C into the
peak sum, of modulus <= eta_P M Phi_P^2/C, and the non-peak sum.  Off P, Phi(k)^2 w(k) = C zeta(k)/sigma = C lambda_k q_0 u_k(zhat)/sigma,
so the non-peak sum equals (q_0/sigma) sum_{k in Q} u_k(zhat) gamma_k.  Therefore
(q_0/sigma) |sum_Q u_k(zhat) gamma_k| <= max(1, 1/sigma) t + eta_P (1 + M Phi_P^2/C), and (P2) gives (i).
Step 3.  gamma_2 = (S - u_1(zhat) gamma_1)/u_2(zhat), so V_j = gamma_1 Mj/u_2(zhat) + u_2(j) S/u_2(zhat) + psi_j; Lemma 1.4(a) gives (ii);
(ii) with sum_j (e_j^+ + e_j^-) <= t^2/q_0 gives the last bound.  QED

Remarks.  (1) (P1) is the norm-level form of "unshifted block".  Lemma 1.1 at the peaks gives sgn(w(k)) Theta_+(k) within
t/(2 sigma |alpha(k)|) of max_P sgn(w) Theta_+ on supp alpha, and symmetrically for Theta_-; the common value is then pinned (to
O(t)) by any peak carrier with private coordinates of both orientations (Lemma 1.5) -- the norm-level form of "a two-sided peak
resource / both sources".  (2) Lemma 1.7 is the norm-level form of H2's Example 4.3, of Z6's Farkas pinning (Prop. P) and of
U3's Lemma R-pin: a nonzero oriented minor of the wrong sign pins the needed switching with the f-DEPENDENT constant 1/|Mj|; a
vanishing minor does not pin.  It constrains every mate at every row, with no reference to any construction.

## 1.5 Consequence: the two-regime profile of a dangerous mate at a residual stage

COROLLARY 1.8.  PROVED (from 1.6, 1.7).  Let (l_+, l_-) be a pair of data-sign carriers (Corollary 1.6) of an unshifted block that
share a contact j with an oriented minor Mj of the wrong sign (the configuration of H2 Example 4.3), with anti-sign far masses
U_far(l_+-) and near masses U_N(l_+-), thin cushions (alpha <= t^2) and negligible psi, eta_P, r_Q.  Then for every mate g and every
scale t the data-sign switching amplitude of l_+ satisfies
      |gamma_{l_+}(t)| <= C_f t min( 1/|Mj|, 1/U_far(l_+), 1/U_N(l_+)^{...} )   --   precisely the minimum of the bounds of 1.6 and 1.7,
with C_f depending only on q_0, sigma, u_2(zhat), u_2(j) (and the constants of 1.6).  So the pair switches with amplitude of order one
only at scales t >~ max(|Mj|, U_far)/C_f (the FREE regime); below, its switching is pinned with the f-dependent constant
C_f/max(|Mj|, U_far).  In particular, if a mate is active on l_+ with amplitude >= c_0 at a scale t_a, then
      |Mj| <= C_f t_a/c_0       and       U_far(l_+) <= C_f t_a/c_0.                                                   (1.3)
Proof.  Take the minimum of the upper bounds of Corollary 1.6 (data-sign direction) and Lemma 1.7 (wrong-signed minor).  QED

Reading for the residual.  A wrong-signed resonance |Mj| in (delta_Z, C b] (H2-ref F-NE) constrains only the switching at scales
t <~ |Mj|; a mate active on the pair with ORDER-ONE amplitude down to the bottom s_a of its activity class forces |Mj| <= C_f s_a/c_0.
So the window method's difficulty is not that f is far from Z_kappa relative to the scales at which the pair actually switches, but
(i) its near-exactness tolerance delta_Z is tied to the WINDOW bottom s_1 (<= s_a) with design-factor losses, and (ii) the
preparation (P2) pushes the minor by >= c theta_0/Design^C >> s_1 (H2 Lemma 5.2).  Part 3 analyses this.  If the pair's activity
is only of RELATIVE size (|gamma| >= K_* t, the class thresholds of K1 Lemma K1.2), (1.3) gives only |Mj| <= C_f/K_*, which is not
informative: then the pair is "pinned with a window constant", and the residual concerns the size of that constant.
