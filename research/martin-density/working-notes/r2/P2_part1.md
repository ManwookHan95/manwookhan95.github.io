# P2 part 1: setting, conventions, and the engineering toolkit

Setting: canonical base q (B_q = B_{c_0} + U(B_H), U: H -> c_0 compact with dense range, U* injective), Martin's norm with a
FINITE block set I (p_N; Preprint B Remark martin-tail). Notation of A_notes §1, §4. Imports (all refereed in Round 1/2):
(T1)-(T4), A Facts A-F, A Lemmas 4.2, 4.3, 4.4, 4.7, 7.2, A Prop 4.5, A Thm 6.5, N_part1 Thm 1 (Ls(f) = C(f) for all f iff density;
g in Ls(f) iff (f, rho g) in cl NA for all rho < 1). s(t) := sqrt(1 + t^2). Only Lemma B's conclusion is used about T.
For f in S_{p*}: forced data xi, q_0, a, w = (w_m), z, e = U*a/nu, nu = ||U*a||, zhat = z + U e = xi/q_0, zeta_m = R_m** xi,
M_m, C_m, P_m, alpha_m; F := supp a; K := {j notin F : |z_j| = 1} (contacts); J_gamma := {j notin F : |z_j| <= 1 - gamma}.
For an NA point f' = grad p(x') (x' in S_p) the same notation with primes; xhat' := x'/q(x') = z' + U e' (A Fact D).
All facts of A §1 (Fact C, Lemma 4.2, Lemma 4.4, Lemma 7.2) hold at NA points with xi replaced by x' (they only use f in S_{p*}
and its normer).

## 1.1 Lemma (clamp formula). PROVED.
For f in S_{p*}, every block m and every k:
   w_m(k) = sgn(zeta_m(k)) * min( M_m , C_m r_m(k) ),     r_m(k) := |zeta_m(k)| / (Phi_m(k)^2 |zeta_m|_m) = m |u_{k,m}(xi)| / (Phi_m(k) |zeta_m|_m),
with sgn(0) = 0. In particular k is a peak iff C_m r_m(k) >= M_m, and w_m(k) depends on xi only through the ratio
u_{k,m}(xi)/|zeta_m|_m and the scalar C_m (M_m = 1 - C_m).
*Proof.* A Fact C: zeta/|zeta| = alpha + D^2 w/C with alpha supported on P, sign alpha_k = sign w(k), so for k in P,
|zeta(k)|/|zeta| = |alpha_k| + Phi_k^2 M/C >= Phi_k^2 M/C, i.e. C r(k) >= M, and sign zeta(k) = sign w(k) (both summands have
the sign of w(k) != 0). Off P: w(k) = C zeta(k)/(Phi_k^2|zeta|), so |w(k)| = C r(k) < M. If zeta(k) = 0 then k is not a peak
(peaks have |zeta(k)| > 0) and w(k) = 0. QED.

## 1.2 Lemma (convergence of block data along engineered approximants). PROVED.
Let xhat_n = z'_n + U e_n be bounded in l_infinity with xhat_n -> zhat weak* (i.e. z'_n -> z coordinatewise boundedly and
e_n -> e in H), and let a_n in c_00 cap S_{q*} with a_n(xhat_n) = 1 = q(xhat_n), a_n -> a in l_1. Put f_n := grad p(xhat_n)
= a_n + L* J_V(L xhat_n) (NA, A Fact D). Then f_n -> f in norm, w_{n,m}(k) -> w_m(k) for every (k,m), C_{n,m} -> C_m,
M_{n,m} -> M_m, |R_m xhat_n|_m -> |R_m** zhat|_m, D_m w_{n,m} -> D_m w_m in l_2, R_m* w_{n,m} -> R_m* w_m in l_1.
*Proof.* L is compact, so L xhat_n -> L** zhat in V (norm); each block R_m** zhat != 0 (T3), J_m is norm-to-weak* continuous at
nonzero points (smoothness of |.|_m), hence w_{n,m} = J_m(R_m xhat_n) -> w_m weak*; D_m, R_m* are compact (weak*-to-norm on
bounded sets). J_V is homogeneous of degree 0, so grad p(xhat_n) = grad p(xhat_n/p(xhat_n)). Norm convergence of f_n:
a_n -> a and L* J_V(L xhat_n) -> L* w. (This is G_referee 4.7 (ii) => (i), steps 1-5.) QED.
Remark. Lemma 1.2 is used in "sequential" form: all engineered approximants below come in sequences indexed by the
construction parameters, and every such sequence satisfies the hypotheses of 1.2. Any requirement of the form
"datum(f') is within eps of datum(f)" for finitely many convergent data is therefore met at a late stage of the sequence,
uniformly with respect to the other (coupled) choices made at the same stage.

## 1.3 Lemma (first-order identity at an NA point). PROVED.
Let f' = grad p(x') be NA with data (a', w', z', e', nu', xhat'), g' in X* with g'(xhat') = 0, and suppose
g' = B + sum_m R_m*(omega_m - d'_m w'_m) with omega_m finitely supported and vanishing on the peak set P'_m,
d'_m := <D w'_m, D omega_m>/C'_m. Then B(xhat') = 0, and for every real tau
   q*(a' + tau B) = 1 + Fl'_B(tau) + Kink'(tau B) + nu' Psi'(tau U*B/nu'),
where Kink'(y) := sum_{j notin supp a'} (|y_j| - z'_j y_j) >= 0, Fl' and Psi' are those of A Lemma 4.3/7.2 at f' (Psi' with e').
*Proof.* A Lemma 4.2 at f': <omega_m - d'_m w'_m, R_m x'> = 0. Hence B(x') = g'(x') = 0 and B(xhat') = 0. The identity is A
Lemma 7.2 at f' (E_q(a' + tau B) = q*(a' + tau B) - (a' + tau B)(xhat') and a'(xhat') = 1). QED.

## 1.4 Lemma (assembly in two regimes). PROVED.
Let f, f' in S_{p*}, g in C(f), rho in (0,1), g' in X*, and 0 < T_0 <= 1. Suppose
 (i) p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta) for 0 < |tau| <= T_0, where 0 < delta <= 1 and T_0^2 <= 3 delta;
 (ii) p*(f' - f) <= (1 - rho^2) T_0^2/6 and p*(g' - rho g) <= (1 - rho^2) T_0/6.
Then g' in C(f'). If moreover f' is NA, then (f', g') in NA((X,p), l_2^2) and ||(f',g') - (f, rho g)|| <= p*(f'-f) + p*(g'-rho g).
*Proof.* For |tau| <= T_0: 1 + (tau^2/2)(1 - delta) <= 1 + tau^2/2 - tau^4/8 <= s(tau), since tau^2 delta/2 >= tau^4/8 iff
tau^2 <= 4 delta, and sqrt(1+x) >= 1 + x/2 - x^2/8. For |tau| >= T_0: p*(f' + tau g') <= p*(f + tau rho g) + p*(f'-f) + |tau| p*(g' - rho g)
<= s(rho tau) + (1-rho^2)(T_0^2 + |tau| T_0)/6 <= s(tau) by A Lemma 4.7 (s(tau) - s(rho tau) >= (1-rho^2) min(tau^2,|tau|)/3) as in the
proof of A Prop 4.8. NA: KLMW (A Lemma 1.2 of N_part1). QED.

## 1.5 Lemma (averaging over scales at a fixed point; E_part2 §2.1). PROVED.
Let f' in S_{p*}, gbar, h_1, ..., h_J in X*, s_j := s_1 2^{1-j}, Q, kappa >= 0 and 0 < s_1 <= T_0 with
 (i) p*(f' + t h_j) <= 1 + Q t^2/2 for |t| <= s_j;  (ii) p*(f' + t gbar) <= 1 + Q t^2/2 for s_J <= |t| <= T_0;
 (iii) p*(h_j - gbar) <= kappa s_j.
Then g' := (1/J) sum_j h_j satisfies p*(f' + t g') <= 1 + (Q + 4 kappa/J) t^2/2 for |t| <= T_0, and p*(g' - gbar) <= 2 kappa s_1/J.
*Proof.* Convexity: p*(f' + t g') <= (1/J) sum_j p*(f' + t h_j). For s_j >= |t| use (i); for s_j < |t| (then |t| >= s_J) use
p*(f' + t h_j) <= p*(f' + t gbar) + |t| kappa s_j and (ii). Since sum_{s_j < |t|} s_j <= 2|t|, the extra term is <= 2 kappa t^2/J. QED.
(Lemma 1.5 is only needed for scale-dependent mates, part 4; the main theorem of part 2 needs no averaging.)

## 1.6 Notation for one-sided linear decompositions ("two-piece data").
Let f in S_{p*} with F finite. Two-piece data for g in X* consist of a finite set I_0 of blocks and
  (b+, omega+), (b-, omega-):  b+- in l_1, omega+-_m in c_00 (m in I_0), supp omega+-_m cap P_m = empty,
  d+-_m := <D_m w_m, D_m omega+-_m>/C_m,
  g = b+ + sum_{m in I_0} R_m*(omega+_m - d+_m w_m) = b- + sum_{m in I_0} R_m*(omega-_m - d-_m w_m),
  supp b+- in F cup K,  z_j b+_j >= 0 and z_j b-_j <= 0 for j in K.
Derived objects: omega_Delta,m := omega-_m - omega+_m, Delta d_m := d-_m - d+_m = <D w_m, D omega_Delta,m>/C_m,
  v_m := R_m* omega_Delta,m (in Y),  v := b+ - b- = sum_m v_m - sum_m Delta d_m R_m* w_m  (in Y cap l_1(F cup K), z-signed on K).
The data are d-NEUTRAL if Delta d_m = 0 for all m (then v = sum_m v_m). For theta in [0,1]:
  b_theta := (1-theta) b+ + theta b- = b+ - theta v,  omega_theta := (1-theta) omega+ + theta omega-,  d_theta = (1-theta)d+ + theta d-.
Coefficients: h(b) := ||P_{e-perp} U*b||^2/nu (A Def 4.1), H_m(omega) := (||D_m omega||^2 - <D_m w_m, D_m omega>^2/C_m^2)/C_m,
  kappa(data) := max( h(b+), h(b-), max_{m in I_0} H_m(omega+_m), max_m H_m(omega-_m) ).
Since h and H_m are positive semidefinite quadratic forms (convex), h(b_theta) <= max(h(b+),h(b-)) and H_m(omega_theta) <= max(H_m(omega+),H_m(omega-)).
Automatic facts (PROVED): b+-(zhat) = 0 (from g(xi) = 0 and A Lemma 4.2: <omega - d w, zeta_m> = 0); v(zhat) = 0; if v = 0 then
omega_Delta = 0 (L* injective) and b+ = b-, so g has a two-sided linear decomposition.

## 1.7 Lemma (one-sided admissibility gives kappa <= 1). PROVED.
If, in addition, for some tau_0 > 0: q*(a + tau b+) <= s(tau) and N_m(w_m + tau(omega+_m - d+_m w_m)) <= s(tau) for 0 <= tau <= tau_0,
and the same with (b-, omega-) for -tau_0 <= tau <= 0, then kappa(data) <= 1.
*Proof.* Base, side +: by A Lemma 7.2 with first-order term b+(zhat) = 0 and nonnegative flip and kink terms,
q*(a + tau b+) >= 1 + nu Psi(tau U*b+/nu) >= 1 + (tau^2/2) h(b+)/(1 + tau ||U*b+||/nu) (A Lemma 4.3, valid when tau||U*b+|| <= nu/2);
comparing with s(tau) <= 1 + tau^2/2 and letting tau -> 0+ gives h(b+) <= 1. Blocks, side +: A Lemma 4.4(b) (valid for small tau >= 0:
1 - d tau > 0, Y > 0) gives 1 + tau^2||h_perp||^2/(sqrt(Y^2 + tau^2||h_perp||^2) + Y) <= s(tau), and tau -> 0+ (Y -> C) gives
||h_perp||^2 <= C, i.e. H_m(omega+_m) <= 1. Side - symmetric. QED.
