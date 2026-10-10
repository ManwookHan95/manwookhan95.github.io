# X2 part 3a — (S2a') Uniform per-piece engineered bounds at a d-consistent engineered approximant: statement, construction, estimates

Setting of parts 1-2.  Throughout, f in S_{p*} (F finite) is the TARGET row, rho in (0,1), eta_0 in (0,2] with rho^2 (1 + eta_0) <=
(1 + rho^2)/2, A_0, A_2 >= 1, gamma_B in (0,1]; delta := (1 - rho^2(1 + eta_0/2))/2 >= (1 - rho^2)/8 > 0, so rho^2 kappa <= 1 - 2 delta for every
kappa <= 1 + eta_0/2.  "f-constant" = a number depending only on (f, N, rho, eta_0, A_0, A_2, gamma_B); by Lemma M2 all f-constants are
valid at every row in the ball B_f := {f'' : p*(f'' - f) <= r_f(eta_1)}.

## 3.1 Data at a base row (hypotheses (U1)-(U7)).
A BASE ROW is f_0 in S_{p*} with p*(f_0 - f) <= r_f/2, F_0 = supp a_0 finite, F ⊂ F_0, E := F_0 \ F.  A WINDOW FAMILY at f_0 consists of
pieces i = 1..n at scales t_i in [T, t_1] (t_1 an f-constant fixed in 3.4) with pairs (b^+-_i, omega^+-_i) representing g_i at f_0
(g_i(xi_0) = 0), all pieces sharing a finite set Omega = union_m Omega_m of strict non-peaks of f_0, such that:
 (U1) t_i ||b^+-_i||_1 <= A_0 and Gamma^{(0)}_w(b^+-_i, omega^+-_i) <= 1 + eta_0/2;
 (U2) supp omega^+-_{i,m} ⊂ Omega_m, and every k in supp omega_{i,m} is of kind [1] (gap^0(k) >= t_i^2, |omega_i(k)| <= 2 gap^0(k)/t_i),
      [2] (gap^0(k) >= gamma_B, |omega_i(k)| <= A_2/t_i) or [3] (|omega_i(k)| <= A_2/t_i and inward-signed: vs_k omega^+_i(k) <= 1.5 gap^0(k)/t_i,
      vs_k omega^-_i(k) >= -1.5 gap^0(k)/t_i, vs_k := sgn w^0_m(k)), as in V1 Proposition TR(iii);
 (U3) on E: at every j in E the data are contact-like (z_0(j) b^+_i(j) >= 0 >= z_0(j) b^-_i(j)) or t_i |b^+-_i(j)| <= |a_0(j)|;
 (U4) violations: (H3) of Lemma VT (b^theta_i(j) = 0 at violated free coordinates j <= N_w), total violation mass eps_i <= eps;
 (U5) explicit scrambling for the negative blocks I_- := {m : Delta_{i,m} < 0 for some i}: Scr^{(0)}_m(x) <= C_S x^2 for 0 < x <= x_0;
 (U6) Omega carries levers with (SEP) at f_0 (Lemma DC constants r_0, C_2, K_J, C_lev, c_tiny), and the first-order cross effects of
      lever coordinates on carriers outside Omega have total weight W_lev := sum_{k notin Omega, Lev ∩ supp u_k != {}} lambda_k (|dz|-
      weighted, per unit r) — fine carriers only;
 (U7) |Delta_{i,m}| <= C_Delta (an f-constant: U1 Lemma 2.1 gives C_Delta^2 = 8 max_m C_m^3/(sigma_m M_m^2 Phi_{P_m}^2) up to the factor 2
      between f_0 and f, since Gamma <= 2).
Window quantities: n, T, the lever constants, x_0, C_S, gap_min := min_{k in Omega} gap^0(k), and c_fine := sum over carriers that are
fine (not in Omega, not peaks of f_0 with margin >= x_0) of lambda_k.

## 3.2 Construction of the d-consistent engineered approximant f' = f'(N_w, s_1, N'').
 (i)   N_w >= max F_0 with tail_W := max_i (||b^+-_i 1_{(N_w, inf)}||_1 + ||v_i 1_{(N_w, inf)}||_1) <= T^3;
 (ii)  s_1 in (0, 1]; MASS SET W := {j in [1, N_w] \ F_0 : j a contact of f_0, max_i |b^theta_i(j)| > 0} ∪ {j in E : the data are contact-like
       at j}; masses m_j := 4 rho s_1 max_i |b^theta_i(j)| with sign z_0(j) (added to a_0(j) on E);
 (iii) Pi_X := ||X||/nu_0 with X the mass vector (Lemma M1); r := 4 K_J (Pi_X + T^4 s_1) (radius of the levers); pull coordinates of the (TU)
       levers with v_l(j_p) in [r, 2^{G} r];
 (iv)  N'' > N_w larger than every lever coordinate, with t(N'') := sum_{m,k} lambda_k ||u_k 1_{(N'', inf)}||_1 <= T^4 s_1^2,
       sum_m sum_k Phi_k 1[t_k > s_1 T^4] <= s_1^2 T^4 (cf. (N2)), and rho V_{>N''} <= delta s_1/64 for every piece;
       (A (TU) pull coordinate inside the window that carries a theta-mass gets the total mass -eps_l(mu_p + m_j), i.e. the theta-mass takes the
       sign of z'_j = -eps_l; this only enlarges |a'_j| and is part of the fixed pull configuration of Lemma DC.)
 (v)   the pre-row f_1 := (a_0 + masses, z_0 1_{[1,N'']}) and the lever parameters P* of Lemma DC at f_1 (its hypotheses are checked in 3.3);
       f' := nabla p(x'), x' := xhat'/p(xhat'), xhat' := z' + U e', where (a', z') are the forced data of f(P*) normalized
       (a' := A(P*)/q*(A(P*)); z' = z_0 on [1, N''] except at lever coordinates, z' = 0 beyond N'').
 (vi)  For each piece: g''_i := b^theta_i 1_{[1,N_w]} + sum_m R_m^*(omega^theta_{i,m} - d'_m(omega^theta_{i,m}) w'_m), c_i := g''_i(xhat'),
       g'_i := rho (g''_i - c_i a').
f' is norm attaining (z' in c_00, a' in c_00, Proposition prop:smooth(c)), and d-consistent with f_0 on Omega (Lemma DC).

## 3.3 Lemma UE-1 (explicit estimates at f').  PROVED.
Put Pi := Pi_X + r + t(N'')^{1/2} (the PERTURBATION SIZE).  There is a window constant K_w (a polynomial in n, A_0/T, 1/gap_min, 1/x_0,
C_S, the lever constants and f-constants) such that, if Pi <= 1/K_w, then:
 (a) [sizes] Pi_X <= 4 rho mu_1 n A_0 s_1/(T nu_0); r <= 8 K_J Pi_X; the masses and lever moves satisfy q*(a'' - a_0) + q*(A(P*) - a'') <=
     K_w s_1; p*(f' - f_0) <= K_w (s_1 log(1/s_1) + tail(N_w-independent)) — precisely p*(f' - f_0) <= K_w Pi log(e/Pi);
 (b) [values] every carrier k with Lev ∩ supp u_k = {} has |u_k(xhat') - u_k(zhat_0)| <= Pi_X + C_2 r + t_k(N''); Omega carriers satisfy
     nv'_k = nv^0_k exactly; carriers meeting lever coordinates (fine, total weight <= W_lev r) move by <= C_lev r;
 (c) [block data] |C'_m - C^0_m| + |M'_m - M^0_m| + |A'_m - A^0_m| + |c' - q^0_0| + |nu' - nu_0| + ||e' - e_0|| <= K_w Pi; every peak of f_0 with margin
     > K_w Pi stays a peak with the same sign; every k in Omega has gap'(k) >= gap^0(k)/2; d'_m(omega) = d_m(omega) and
     H'_m(omega) = (C^0_m/C'_m) H_m(omega) for omega supported in Omega_m (Definition 1.4);
 (d) [Bregman] 0 <= Bx_m := <w'_m - w^0_m, R_m xhat'> <= K_w Pi^2 + 4 Pi_X c_fine + 4 C_lev r W_lev r + 2 t(N'');
 (e) [scrambling, m in I_-] the quantity S_m := ||D_m(w'_m - w^0_m)||_2^2 + sum_{k in A_m} (Phi_k^2 + lambda_k(|w'_m(k) - w^0_m(k)| + (C'_m - C^0_m)_+))
     of lem:scrambling (A_m the scrambled set of lem:anchor for (w^0_m, w'_m)) satisfies S_m <= K_w Pi^2 log(e/Pi) + 4m (C_S (K_w Pi)^2 + s_1^2 T^4);
 (f) [base form] for every piece and diamond in {+, -, theta}, with beta^theta := b^theta 1_{[1,N_w]}, beta^+- := b^+- 1_{[1,N_w]} +- (1/2) v 1_{(N_w,inf)}:
     |c' h'(beta^diamond) - q^0_0 h^0(b^diamond)| <= K_w (Pi/T^2 + tail_W/T), where h'(beta) := ||P'^perp U^* beta||^2/nu';
 (g) [targets] |c_i| <= K_w (Pi + tail_W)/t_i and p*(g'_i - rho g_i) <= K_w (Pi + c_fine + tail_W)/t_i.
Proof.  (a) Corollary M1' (crude bound) with t_i >= T and ||b^theta_i||_1 <= A_0/t_i; Lemma DC: |P*| <= r and lever masses <= beta 2^{G+2} r with
beta = nu/(mu_j^2 v_l(j)) a lever constant; z-moves <= r/v.  For p*(f' - f_0): Z3 Lemma 3.1 (companion cost, refereed: p*(f'' - f_0) <=
q*(a'' - a_0) + C_f c(delta), c(delta) = sum_m [Delta_m log(e/Delta_m) + sum_k min(lambda_k, |u_k(delta)|)]) with delta := xhat' - zhat_0, whose
carrier values are bounded by (b); the cut-off contributes t(N'').  (b) Lemma M1(iii) (base f_0, masses and lever masses J := W ∪ Lev,
||X_tot|| <= ||X|| + C_2 r) and Lemma DC.  (c) |A'_m - A^0_m| <= sum_k lambda_k |u_k(xhat') - u_k(zhat_0)| (norm Lipschitz, sum lambda <= 1);
the threshold equation of Y1 Lemma T (theta, A solve (E1), (E2) of U1 Lemma 1.2, a nonsingular system at f_0 with Jacobian bounded below by
Phi_P^2 >= Phi_{k^nat}^2) gives |C' - C| <= K_w max-change, exactly as in the proof of lem:F1 (strict monotonicity of F(c; v) through the fixed
peak k^nat_m of Lemma M2, Lipschitz bound sum_k Phi_k |v'_k - v_k|); q_0 = 1/(1 + sum_m A_m); nu', e': Lemma M1(ii) with q*-normalization.
Peaks: the margin is a Lipschitz function of the value and of theta (lem:threshold).  Omega: (1.1) and |C' - C| <= gap_min/4 for Pi <= 1/K_w.
(d) (E5) of lem:approxfacts: 0 <= Bx_m <= <w'_m - w^0_m, R_m(xhat' - zhat_0)> = sum_k lambda_k (w'_m(k) - w^0_m(k)) u_k(xhat' - zhat_0).  Coarse
carriers (peaks of f_0 with margin > K_w Pi, and Omega): |w' - w^0| <= |C' - C| (peaks: |M' - M|; Omega: (C'/C - 1)|w^0|) <= K_w Pi, values
<= Pi: total <= K_w Pi^2.  Remaining carriers: |w' - w^0| <= 2; those not meeting lever coordinates contribute <= 2 sum lambda_k (Pi_X + t_k)
<= 2 Pi_X c_fine + 2 t(N''); those meeting lever coordinates <= 2 C_lev r * (their weight) <= 2 C_lev W_lev r^2.  (e) Proof of lem:scrambling
read with the perturbation size Pi in place of s_1: by (b), (c), a peak of f_0 with margin > K_* Pi (K_* := K_w) is in S_1, a strict non-peak
with Phi gap and gap > K_* Pi is in S_2 (the margin/gap arguments of lem:scrambling use only |u_k(xhat') - u_k(zhat_0)|, |theta' - theta|,
|C' - C| and lem:F1-type Lipschitz bounds, all <= K_w Pi here); so A_m ∩ {t_k <= Pi} ⊂ {mu_k <= 2K_*Pi or Phi gap <= 2K_*Pi or gap <= 2K_*Pi},
whose Phi-mass is <= Scr^{(0)}_m(2 K_* Pi) <= C_S (2K_*Pi)^2 by (U5) (2K_*Pi <= x_0); {t_k > s_1 T^4} has Phi-mass <= s_1^2 T^4 by (iv); with
|w' - w| <= 2, (C'-C)_+ <= 1, Phi <= 1, lambda = m Phi, the sum over A_m is <= 4m(...).  ||D(w' - w^0)||^2 <= K_w Pi^2 log(e/Pi): the last
display of the proof of lem:F1 with K_F s_1 replaced by K_w Pi (Phi_k |w'(k) - w(k)| <= K_w(Pi + t_k) from the clamp formula).  (f) Three
changes: (1) beta^diamond - b^diamond has l_1-norm <= tail_W, and |h(y) - h(y')| <= ||U||^2 (||y||_1 + ||y'||_1)||y - y'||_1/nu with ||b||_1 <=
A_0/T; (2) ||P'^perp y||^2 - ||P^perp y||^2 = <y, e>^2 - <y, e'>^2, of modulus <= 2 ||y||^2 ||e' - e|| <= 2 ||U||^2 (2A_0/T)^2 K_w Pi;
(3) |c'/nu' - q_0/nu_0| <= K_w Pi.  (g) c_i = (g''_i - g_i)(xhat') + g_i(xhat' - zhat_0) (g_i(zhat_0) = 0 since g_i(xi_0) = 0);
g''_i - g_i = -b^theta_i 1_{(N_w,inf)} + sum_m d^theta_{i,m} R_m^*(w^0_m - w'_m) by d-consistency (d'(omega^theta) = d(omega^theta)), with
|d^theta_{i,m}| <= ||D_m omega^theta||_2 <= A_2 ||Phi_m||_2/t_i ... <= K_w/t_i and ||R_m^*(w^0 - w')||_1 <= sum_k lambda_k |w^0(k) - w'(k)| <= K_w Pi + 2 c_fine;
|g_i(xhat' - zhat_0)| <= |<U^* g_i, e' - e_0>| + sum_{lever, cut-off} |g_i(j)| |z' - z_0|(j) <= ||g_i||_1 (K_w Pi) with ||g_i||_1 <= K_w/t_i; and
p*(.) <= (1 + ||U||) ||.||_1.  QED
