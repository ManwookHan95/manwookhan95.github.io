# X2 part 1 — Setting, mass bookkeeping with the diagonal base, the true size of the junction mismatch, uniform neighborhoods

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; notation as there), I = {1..N} finite, p = p_N, design T_final / D^{U1'}
(U4, U1-ref Section 6) with the diagonal base U k_s = mu_s e_s, U^* e_s^* = mu_s k_s (mu_s = 2^{-s^2-1}; only "diagonal with positive
entries" is used in this part).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.0 Objects
A ROW is f_0 in S_{p*} with forced data (xi_0, q_0, a, w, F, z, zhat, e, nu) (prop:forced), F := supp a finite, zhat = z + Ue, so
(Ue)_s = mu_s^2 a_s / nu, i.e. zhat_s = z_s for s notin F.  zeta_m := R_m^** zhat, A_m := |zeta_m|_m (= sigma_m/q_0), and for a strict
non-peak k of block m the NORMALIZED VALUE nv_k := zeta_m(k)/A_m = lambda_k u_k(zhat)/A_m; by lem:threshold, nv_k = Phi_k^2 w_m(k)/C_m, and
for omega vanishing on the peak set P_m:  d_m(omega) = <D_m w_m, D_m omega>/C_m = sum_k omega(k) nv_k.                          (1.0)
A PIECE at scale t in (0,1] is a functional g with g(xi_0) = 0 together with two pairs (b^+-, omega^+-) REPRESENTING g at f_0
(def:twopiece: g = b^+- + sum_m R_m^*(omega^+-_m - d_m(omega^+-_m) w_m), omega^+-_m in c_00 supported in Q_m), NOT necessarily
side-admissible; Domega := omega^- - omega^+, Delta_m := d_m(Domega_m), v := b^+ - b^- = sum_m R_m^*(Domega_m - Delta_m w_m),
b^theta := (b^+ + b^-)/2, omega^theta := (omega^+ + omega^-)/2.  Violations viol(j), eps := sum_{j notin F} viol(j) as in U3 Lemma VT.

## 1.1 Lemma M1 (masses off the support, diagonal base).  PROVED.
Let J be a finite set disjoint from F, c in R^J, A := a + sum_{s in J} c_s e_s^*, X := sum_{s in J} c_s mu_s k_s, nu_A := ||U^*A||,
e_A := U^*A/nu_A.  Then X ⊥ U^*a, nu_A = (nu^2 + ||X||^2)^{1/2}, and for every u in l_1:
 (i)   <U^*u, e_A - e> = sum_{s in J} c_s mu_s^2 u(s)/nu_A + (nu/nu_A - 1) <U^*u, e>;
 (ii)  ||e_A - e|| <= ||X||/nu,  |<U^*u, e_A - e>| <= ||U^*u|| ||X||/nu,  and 0 <= nu_A - nu <= ||X||^2/(2nu);
 (iii) if z^A is any sign vector admissible with A (|z^A| <= 1, z^A = sgn A on supp A) and xhat_A := z^A + U e_A, then
       |u(xhat_A) - u(zhat)| <= ||U^*u|| ||X||/nu + sum_s |u(s)| |z^A_s - z_s|   (for s in F, z^A_s = z_s = sgn a_s).
Proof.  U^*a = sum_{s in F} a_s mu_s k_s and X lies in span{k_s : s in J}, J ∩ F = {}: orthogonal.  (i) e_A = (nu e + X)/nu_A and
<U^*u, X> = sum_J c_s mu_s <U^*u, k_s> = sum_J c_s mu_s^2 u(s).  (ii) <e_A, e> = nu/nu_A, so ||e_A - e||^2 = 2(1 - nu/nu_A) =
2(nu_A - nu)/nu_A <= ||X||^2/nu^2 because nu_A - nu = ||X||^2/(nu_A + nu) <= ||X||^2/(2nu); Cauchy-Schwarz.  (iii) xhat_A - zhat =
(z^A - z) + U(e_A - e) and u(U h) = <U^*u, h>.  QED
For a carrier, ||U^*u_k|| <= q*(u_k) = 1.  So every value moves by at most ||X||/nu plus its own sign changes.
(iv) If masses are also put on support coordinates (J ∩ F != {}, same signs), X is no longer orthogonal to U^*a and nu_A - nu is of FIRST
order; the general bound ||e_A - e|| <= 2||U^*(A - a)||/nu (||x/|x| - y/|y||| <= 2|x - y|/|y|) replaces (ii), and a mass c at p in F changes
EVERY value at first order through the term (nu/nu_A - 1)<U^*u, e> = -c mu_p^2 a_p <U^*u, e>/nu^2 + O(c^2): a cross effect of relative size
|a_p|/nu compared with the own effect c mu_p^2 u(p)/nu on a carrier with u(p) != 0.  (PROVED, same computation.)

## 1.2 Corollary M1' (masses of an engineered approximant).  PROVED.
Let pieces i = 1..n at scales t_i >= T > 0 satisfy t_i ||b^+-_i||_1 <= A_0, and let the mass set be W (finite, disjoint from F) with
masses m_s := 4 rho s_1 max_i |b^theta_i(s)| (s in W).  Then ||X|| <= sum_W m_s mu_s <= 4 rho s_1 mu_1 n A_0 / T  (crude bound), and
for s notin F the sharper bound sum_{s notin F} mu_s^2 b(s)^2 <= nu h(b) (h of def:certificate; diagonal base: U^*(b 1_{F^c}) ⊥ span
{k_s : s in F} ∋ e) gives ||X||^2 <= 16 rho^2 s_1^2 nu sum_i h(b^theta_i) <= 16 rho^2 s_1^2 nu n Gamma_max/q_0 when W ∩ F = {}.
Proof.  ||X|| <= sum m_s mu_s and max_i |.| <= sum_i |.|; h is a positive semidefinite quadratic form, so h(b^theta) <= (h(b^+) + h(b^-))/2
<= Gamma_w/q_0.  QED
(Only the crude bound is used below: every requirement on s_1 will be "s_1 small compared with window quantities", and the masses
enter only through ||X||.)

## 1.3 Proposition J (the junction mismatch for VALID data).  PROVED (upper bound); the lower-bound statement is HEURISTIC.
Notation of thm:engineered, at the engineered approximant f' of f_0 built from ONE piece (no re-tuning), late stage.  Suppose the piece
has Gamma_w(b^+-, omega^+-) <= Gamma_max and supp omega^+-_m ⊂ Omega_m ⊂ Q_m.  Then for every block
 (a) ||D_m Domega_m||_2^2 = Delta_m^2 + C_m H_m(Domega_m) <= (4 Gamma_max/sigma_m) (C_m + C_m^3/(M_m^2 Phi_{P_m}^2))   [U1 Lemma 2.1];
 (b) |kappa^+-_m| = (rho/2) |(d'_m - d_m)(Domega_m)|
         <= (rho m/2) ||D_m Domega_m||_2 |Omega_m|^{1/2} max_{k in Omega_m} |u_k(xhat') - u_k(zhat)|/A'_m  +  (rho/2)|Delta_m| |A'_m - A_m|/A'_m;
     consequently |kappa^+-_m| <= C_f |Omega_m|^{1/2} (||X|| + t(N'')), C_f depending only on the block constants of f_0, Gamma_max, rho.
Proof.  (a) D Domega = (Delta/C) D w + y with y ⊥ D w, ||y||^2 = C H (def:certificate); Lemma 2.1 of U1 (re-derived by U1-ref) bounds
Delta^2 <= H C^3/(M^2 Phi_P^2) since Domega is supported in Q; and H(Domega) <= 2H(omega^+) + 2H(omega^-) <= 4 Gamma_max/sigma.
(b) kappa^+- = rho (d' - d)(omega^+- - omega^theta) = -+ (rho/2)(d' - d)(Domega) (proof of thm:engineered, Step 2).  By (1.0) at f_0 and
at f' (Omega carriers stay strict non-peaks at late stages), (d' - d)(Domega) = sum_k Domega(k)(nv'_k - nv_k), and nv'_k - nv_k =
lambda_k (u_k(xhat')/A' - u_k(zhat)/A); split as lambda_k (u_k(xhat') - u_k(zhat))/A' + lambda_k u_k(zhat)(1/A' - 1/A); the second part sums
to Delta (A - A')/A' by (1.0); Cauchy-Schwarz with lambda_k = m Phi_k on the first.  Lemma M1(iii): |u_k(xhat') - u_k(zhat)| <= ||X||/nu + t_k
(the cut-off changes z only beyond N''); |A' - A| <= sum_k lambda_k |u_k(xhat' - zhat)| <= ||X||/nu + t(N'').  QED
Consequence.  The mismatch is uniform in the scale t of the piece (U3-ref's estimate kappa ~ s_1/t^2 used a datum scaled by 1/t, whose
Gamma_w grows like t^{-2}; with Gamma_w <= 2 the 1/t-sized parts of b^theta and Domega are forced onto coordinates/directions where they
cost nothing in Gamma, and (a) shows ||D Domega||_2 = O(1)).  But it is NOT uniform in the WINDOW: |Omega_m| and ||X|| (which carries the
masses of all n pieces of the window) grow with the window, while the rebalancing in Step 4 of thm:engineered absorbs a first-order
level shift kappa only at cost |tau kappa| iota with a FIXED inefficiency iota ~ eta_1 (transfer data of f; eta_1 cannot be made
window-dependent without f-dependent rates: Lemma TV(a) needs |eps| Lambda <= gamma/2 with Lambda = Lambda(eta_1) unbounded).  At |tau| = s_1
the ratio (cost)/(budget delta tau^2) is ~ eta_1 C_f |Omega|^{1/2} ||X||/(delta s_1), unbounded along the windows (HEURISTIC: it is attained
in general; the proof below does not need the lower bound).  Hence an exact cancellation is the robust remedy: d-CONSISTENCY.

## 1.4 Definition (d-consistent approximant).
A first row f' (with forced data primed) is d-CONSISTENT with f_0 on a finite set Omega = union_m Omega_m of strict non-peaks of f_0 if
every k in Omega_m is a strict non-peak of f' and nv'_k = nv_k (equivalently u_k(xhat') = (A'_m/A_m) u_k(zhat)).  Then, by (1.0) at both
rows, d'_m(omega) = d_m(omega) for EVERY omega supported in Omega_m, w'_m(k) = (C'_m/C_m) w_m(k) and
    gap'_m(k) = (C'_m/C_m) gap_m(k) + (1 - C'_m/C_m)          (k in Omega_m),                                                   (1.1)
since gap' = M' - (C'/C)|w| = (1 - C') - (C'/C)(1 - C - gap).  In particular kappa^+- = 0 for every piece supported in Omega and
H'_m(omega) = (C_m/C'_m) H_m(omega) for every such omega (H'(omega) = (||D omega||^2 - d'(omega)^2)/C').  (Elementary; PROVED.)

## 1.5 Lemma M2 (uniform neighborhoods).  PROVED.
Let f in S_{p*} have F finite.  Fix, at f, in every block: gamma_m in (M_m/2, M_m) with |w_m(k)| != gamma_m for all k, and, for a given
eta_1 in (0, 1/4], transfer data (gamma_m, k^vs_{*,m}, Lambda^vs_m) (lem:transferdata), and a peak k^nat_m with alpha_m(k^nat_m) != 0.  Then
there is r_f(eta_1) > 0 such that every f'' in S_{p*} with p*(f'' - f) <= r_f(eta_1) satisfies (double primes = data of f''):
 (a) |C''_m - C_m| <= C_m/8, |sigma''_m - sigma_m| <= sigma_m/8, |q''_0 - q_0| <= q_0/8, |nu'' - nu| <= nu/8, F ⊂ supp a'' and
     |a''_j| >= a_min/2 on F (a_min := min_F |a_j|), and the peak k^nat_m of f is a peak of f'' with the same sign;
 (b) the transfer data persist: k^vs_{*,m} is a peak of f'' with w''_m = M''_m and positive margin, P''_m ⊂ L''_m, e''^vs_{y,m} >= 1/2,
     iota''^vs_m <= 2 eta_1, ||D_m y''^vs_m||_2 <= K_y, |Y''^vs_m|/q''_0 <= K_Y, with K_y, K_Y independent of eta_1 (lem:transferdata(b),(d)).
Proof.  If (a) or (b) failed for every r > 0, there would be f_n -> f violating it; Proposition prop:continuity (a_n -> a in l_1, scalar
data converge, w_{n,m} -> w_m coordinatewise, k^nat a peak with positive margin persists as in the proof of lem:persistence) and Lemma
lem:persistence contradict this for n large.  QED
All constants called "f-constants" below are computed from the data of f and are valid on the ball p*(f'' - f) <= r_f; companions
f_j -> f and their engineered approximants eventually lie in that ball, so these constants are uniform along every window sequence.
