# P2 part 2: engineered recovery of d-neutral two-piece (switching) mates

## 2.1 Theorem (engineered recovery of d-neutral two-piece mates). PROVED.
Let f in S_{p*} with F = supp a finite, let g in C(f) carry d-NEUTRAL two-piece data (part 1, 1.6) with coefficient
kappa = kappa(data), and let rho in (0,1) with rho^2 kappa < 1. If |I_0| >= 2 assume the steering hypothesis
 (S) there are gamma > 0 and finitely many coordinates j_1, ..., j_r in J_gamma such that the vectors (v_{m,j_i})_{m in I_0}
     span H_0 := {y in R^{I_0} : sum_m y_m = 0}.
(For j notin F cup K, sum_m v_{m,j} = v_j = 0, so these vectors always lie in H_0.) Then (f, rho g) is in cl NA((c_0,p), l_2^2).
If the data are one-sided admissible (Lemma 1.7), this holds for every rho < 1, i.e. g is in Ls(f) (N_part1 Thm 1).
No condition on K (it may be infinite), on the split of the contact mass between the two sides, on the rates of T, or on the
number of strict non-peaks of f is needed.

*Proof.* If v = 0 then b+ = b- is both z-signed and (-z)-signed on K, hence vanishes on K and is supported in the finite set F;
omega+ = omega- (L* injective). So c := (b+, omega+) is a finite certificate (A Def 4.1) with g_c = g and H(c) <= kappa; rho g is in C(f)
(convexity) and H(rho c) = rho^2 kappa < 1, so rho g in Cert(f), recovered along every sequence (A Thm 4.10). Assume v != 0.
Write theta := 1/2, b^+ := b+, b^- := b-, b^theta := b_theta, and similarly omega^sigma (sigma in {+, -, theta}); all three
share d_m := d+_m = d-_m (d-neutrality), and
   g = b^sigma + sum_{m in I_0} R_m*(omega^sigma_m - d_m w_m),   b^+ = b^theta + theta v,  b^- = b^theta - (1-theta) v.   (2.1.1)

Step 0 (constants depending only on f, g, rho). delta := (1 - rho^2 kappa)/2 in (0, 1/2]; eps_0 := delta/8.
gamma_0 := min{ gap_m(k) : m in I_0, k in supp omega^sigma_m, sigma } > 0; a_min := min_{j in F} |a_j|;
beta_max := max_sigma ||b^sigma||_infinity + 1; Kc := 4 max_sigma max( ||U|| ||b^sigma||_1/nu + 1, max_m |d_m| M_m/C_m + 1 ).
Raising coordinate: v is in Y \ {0}, so v is not in R a (a in c_00, Y cap c_00 = {0}); since U* is injective, U*v is not parallel
to U*a, i.e. P_{e-perp} U*v != 0. As v is supported in F cup K and z-signed on K,
   sum_{j in F} v_j <P_{e-perp}U*v, U*e_j*> + sum_{j in K} |v_j| <P_{e-perp}U*v, z_j U*e_j*> = ||P_{e-perp}U*v||^2 > 0
(U*v = sum_j v_j U*e_j* converges in H). Hence there are j_+ and s_+ in {-1, 1} with s_+ = z_{j_+} if j_+ in K (any sign if
j_+ in F) such that gamma_+ := s_+ <P_{e-perp}U*v, U*e_{j_+}*>/nu > 0. By continuity of a'' -> <U*v, P_{e(a'')-perp}U*e_{j_+}*>/||U*a''||
(e(a'') := U*a''/||U*a''||) at a'' = a there is r_+ > 0 with s_+ <U*v, P_{e(a'')-perp}U*e_{j_+}*>/||U*a''|| >= gamma_+/2 whenever ||a'' - a||_1 <= r_+.
Choose T_0 in (0,1] with
   T_0^2 <= 3 delta,  rho T_0 beta_max <= a_min/8,  Kc T_0 <= 1,  (rho^2 kappa + delta/8)(1 + Kc T_0) <= rho^2 kappa + delta/4,
   rho T_0 <= min_sigma r_sigma/2  (r_sigma := coordinatewise radius at f of the block certificate omega^sigma, A Lemma 4.4(d) with
   referee fix G1: min over m, k of gap_m(k)/(2|omega^sigma_m(k)|), 1/(2|d_m|), C_m/(2|d_m|M_m)),
   16 rho T_0 ||U|| ||U*v|| <= nu.
(Kc bounds, at late stages, both 2||U*B^sigma||/nu' and 2 rho|d'_m|M'_m/C'_m; Kc T_0 <= 1 also gives |tau| ||U*B^sigma|| <= nu'/2.)
Put A_0 := 8 rho ||U|| ||U*v|| ||b^theta||_1/nu + 1.

Construction (parameters chosen in the order N, s_1, Far, N'', mu, p; each later choice may depend on the earlier ones):
 (C1) Window N >= max(F cup {j_+} cup {j_1,...,j_r}). Put tau_N := sum_{j in K, j > N} |v_j| > 0 (v is not in c_00 and lives on
      F cup K with F inside [1,N]) and eps_N := sup_{j > N} |v_j|.
 (C2) Small scale s_1 in (0, T_0] with 4 A_0 s_1 <= tau_N.
 (C3) Window masses m_j := 4 rho s_1 |b^theta_j| for j in K cap [1,N].
      Far set: Far := K cap (N, N_2] with N_2 minimal such that V_Far := sum_{j in Far} |v_j| >= 2 A_0 s_1 (exists by (C2));
      then V_Far <= 2 A_0 s_1 + eps_N. Far masses m'_j := 4 rho T_0 |v_j| (j in Far).
 (C4) Cut-off N'' > N_2 with V_{>N''} := sum_{j in K, j > N''} |v_j| <= eps_0 s_1/rho.
 (C5) For mu >= 0 and p in [-gamma, gamma]^r:
        a''(mu) := a + sum_{j in K cap [1,N]} m_j z_j e_j* - sum_{j in Far} m'_j z_j e_j* + mu s_+ e_{j_+}*,   a' := a''/q*(a''),
        z'_j := z_j on [1,N''] \ (Far cup {j_1..j_r}),  z'_j := -z_j on Far,  z'_{j_i} := z_{j_i} + p_i,  z'_j := 0 for j > N'',
        e' := U*a'/||U*a'||,  xhat' := z' + U e',  x' := xhat'/p(xhat'),  f' := grad p(x') = a' + sum_m R_m* w'_m  (NA).
      Compatibility (A Fact D): z' is in c_00, ||z'||_inf <= 1, and z' = sign a' on supp a' = F cup {window contacts with m_j > 0}
      cup Far (cup {j_+} if mu > 0): on F, z = sign a and the mass at j_+ in F keeps the sign if mu <= |a_{j_+}|/2; on window contacts
      z'_j = z_j = sign(m_j z_j); on Far z'_j = -z_j = sign(-m'_j z_j); j_+ in K gets mass of sign z_{j_+} = z'_{j_+}. Hence
      q(xhat') = a'(xhat') = 1 and f' is norm attaining.

Step 1 (steering: exact carriers). Psi(mu) := v(xhat'(mu, p)) does not depend on p (v_j = 0 at the free coordinates j_i).
Since v(zhat) = 0:  v(xhat') = v(z' - z) + <U*v, e' - e>, and, because z_j v_j = |v_j| on K, v_j = 0 off F cup K, F in [1,N]:
   v(z' - z) = -2 V_Far - V_{>N''}.
Lipschitz bound ||e(a'') - e|| <= 2||U|| ||a'' - a||_1/nu (from ||x/|x| - y/|y||| <= 2|x - y|/|y| and ||U*y|| <= ||U|| ||y||_1):
   |<U*v, e(a''(0)) - e>| <= (2||U|| ||U*v||/nu)(4 rho s_1 ||b^theta||_1 + 4 rho T_0 V_Far) <= A_0 s_1 + V_Far/2 <= V_Far
(by the choice of T_0 and V_Far >= 2A_0 s_1). Hence Psi(0) <= -2V_Far + V_Far = -V_Far < 0 and |Psi(0)| <= 4 V_Far.
Let mu_max := 8 V_Far/gamma_+. At late stages (s_1, eps_N small) ||a''(mu) - a||_1 <= r_+ and mu_max <= |a_{j_+}|/2 (if j_+ in F) for
mu in [0, mu_max]; then by the mean value theorem Psi(mu_max) >= Psi(0) + mu_max gamma_+/2 >= 0. Psi is continuous, so there is
mu_* in [0, mu_max] with Psi(mu_*) = v(xhat') = 0. Fix mu := mu_*.
If |I_0| >= 2: y := (v_m(xhat'(mu_*, 0)))_{m in I_0} lies in H_0 (its sum is v(xhat') = 0, d-neutrality). Let A: R^r -> H_0,
A p := sum_i p_i (v_{m,j_i})_m (onto by (S)) with a fixed linear right inverse A^+. Since v_m(zhat) = <omega_Delta,m, zeta_m>/q_0 =
|zeta_m| Delta d_m/q_0 = 0 (A Fact C), and xhat' -> zhat weak* along the construction (Step 3), y -> 0; at late stages
p := -A^+ y has |p_i| <= gamma, and then v_m(xhat') = y_m + (A p)_m = 0 for every m in I_0 (changing z' at the j_i is affine and does
not change e' or v(xhat')). Result: v_m(xhat') = 0 for all m in I_0.

Step 2 (the target and its three decompositions). d'^sigma_m := <D w'_m, D omega^sigma_m>/C'_m. At late stages supp omega^sigma_m
avoids P'_m (Step 3), so by Lemma 1.1 at f' (w'(k) = C' lambda_k u_k(x')/(Phi_k^2 |zeta'_m|) off P'):
   <D w'_m, D omega_Delta,m> = (C'_m/|zeta'_m|) v_m(x') = 0,  hence d'^+_m = d'^-_m = d'^theta_m =: d'_m.
Define g'' := b^theta 1_{[1,N]} + sum_{m in I_0} R_m*(omega^theta_m - d'_m w'_m), c := g''(xhat'), g' := rho (g'' - c a'), so g'(xhat') = 0.
For sigma in {+, -, theta} put B^sigma := g' - rho sum_m R_m*(omega^sigma_m - d'_m w'_m). Since omega^theta - omega^+ = theta omega_Delta,
omega^theta - omega^- = -(1-theta) omega_Delta and the d'-terms coincide:
   B^theta = rho(b^theta 1_{[1,N]} - c a'),  B^+ = B^theta + rho theta v,  B^- = B^theta - rho(1-theta) v.   (2.1.2)
Write B^sigma = rho(beta^sigma - c a') with beta^theta = b^theta 1_{[1,N]}, beta^+ = b^+ 1_{[1,N]} + theta v 1_{(N,inf)},
beta^- = b^- 1_{[1,N]} - (1-theta) v 1_{(N,inf)} (by (2.1.1)). Then f' + tau g' = (a' + tau B^sigma) + sum_m R_m*(w'_m + tau rho(omega^sigma_m - d'_m w'_m))
for every sigma and tau, so by A Fact A
   p*(f' + tau g') <= max( q*(a' + tau B^sigma), max_{m in I_0} N_m(w'_m + tau rho(omega^sigma_m - d'_m w'_m)) ).   (2.1.3)

Step 3 (convergence along the construction). Along any sequence of constructions with N -> infinity (hence s_1, V_Far, mu_*, |p| -> 0):
the total mass ||a'' - a||_1 <= 4 rho s_1 ||b^theta||_1 + 4 rho T_0 (2A_0 s_1 + eps_N) + mu_max -> 0, so a' -> a, e' -> e; z' -> z coordinatewise
(z' = z on [1,N] except at the fixed j_i, where |p_i| -> 0; Far lies beyond N). Lemma 1.2: f' -> f, w'_m(k) -> w_m(k), M', C', |zeta'| converge.
Consequences at late stages: gap'_m(k) >= gamma_0/2 on supp omega^sigma (so these coordinates are off-peak at f'); d'_m -> d_m;
H'_m(omega^sigma_m) -> H_m(omega^sigma_m); g'' -> g in l_1 (g'' - g = -b^theta 1_{(N,inf)} + sum_m R_m*(d_m w_m - d'_m w'_m)); c = (g'' - g)(xhat') + g(xhat') -> g(zhat) = 0;
g' -> rho g; beta^sigma -> b^sigma in l_1 (beta^+ - b^+ = -b^theta 1_{(N,inf)}, similarly for -), so B^sigma -> rho b^sigma; nu' -> nu and
h'(B^sigma) := ||P_{e'-perp} U*B^sigma||^2/nu' -> rho^2 h(b^sigma).

Step 4 (cost of the block parts). A Lemma 4.4(c),(d) at f' (coordinatewise radius, referee fix G1) for the certificate rho omega^sigma_m:
for |tau| <= T_0 (<= r_sigma/(2 rho) <= coordinatewise radius at f' at late stages),
   N_m(w'_m + tau rho(omega^sigma_m - d'_m w'_m)) <= 1 + (rho^2 tau^2/2) H'_m(omega^sigma_m)(1 + 2 rho |tau d'_m| M'_m/C'_m).
Blocks m notin I_0 contribute N_m(w'_m) = 1.

Step 5 (cost of the base parts). Lemma 1.3 applies (g'(xhat') = 0, supp omega^sigma off P'): q*(a' + tau B^sigma) = 1 + Fl' + Kink' + nu' Psi'.
Use sigma = theta for |tau| <= s_1 and sigma = sign(tau) for s_1 <= |tau| <= T_0. Late stages: |tau rho c| <= 1/2 and 1/2 <= q*(a'') <= 2.
 (a) No sign flips. On supp a', a'_j + tau B^sigma_j = (1 - tau rho c) a'_j + tau rho beta^sigma_j. j in F: |a'_j| >= a_min/4 (also at j_+ in F, as
     mu <= |a_{j_+}|/2) and |tau rho beta^sigma_j| <= rho T_0 beta_max <= a_min/8. Window contacts with mass: for sigma = theta, |tau| <= s_1:
     |tau rho beta^theta_j| <= s_1 rho |b^theta_j| = m_j/4 <= |a'_j|/2; for sigma = +, tau > 0: beta^+_j = b+_j has z_j b+_j >= 0, so tau beta^+_j has
     the sign z_j = sign a'_j; sigma = -, tau < 0: beta^-_j = b-_j, z_j b-_j <= 0, same conclusion. j_+ in K: as for window contacts
     (its mass has sign z_{j_+}). Far: |a'_j| >= m'_j/2 = 2 rho T_0 |v_j| >= 2|tau rho beta^sigma_j| (|beta^sigma_j| <= |v_j| there, beta^theta_j = 0).
     Hence Fl' = 0 in all cases.
 (b) Kinks (j notin supp a'). Non-contacts j in J := N \ (F cup K) (including the j_i): beta^sigma_j = 0 (b+-, v vanish there), so 0.
     Window contacts without mass (b^theta_j = 0): beta^+_j = theta v_j, beta^-_j = -(1-theta)v_j, beta^theta_j = 0, z'_j = z_j, z_j v_j >= 0: on
     the designated side tau beta^sigma_j has the sign z_j, so |tau B_j| - z'_j tau B_j = 0. Contacts in (N, N''] \ Far: same computation.
     Contacts beyond N'' (z'_j = 0): kink |tau rho beta^sigma_j| <= rho |tau| |v_j| for sigma = +-, and 0 for sigma = theta (beta^theta = 0 beyond N).
     Total: Kink' <= rho |tau| V_{>N''} <= eps_0 s_1 |tau| <= eps_0 tau^2 for |tau| >= s_1 (sigma = +-), and Kink' = 0 for sigma = theta.
 (c) Hilbert term (A Lemma 4.3 at f'): nu' Psi'(tau U*B^sigma/nu') <= (tau^2/2) h'(B^sigma)(1 + 2|tau| ||U*B^sigma||/nu') when |tau| ||U*B^sigma|| <= nu'/2.

Step 6 (conclusion). At late stages h'(B^sigma) <= rho^2 kappa + delta/8 and rho^2 H'_m(omega^sigma_m) <= rho^2 kappa + delta/8 (Step 3, and h(b^sigma),
H_m(omega^sigma) <= kappa by convexity, 1.6), and the factors in Steps 4-5(c) are <= 1 + Kc T_0. By (2.1.3), for 0 < |tau| <= T_0,
   p*(f' + tau g') <= 1 + (tau^2/2)(rho^2 kappa + delta/4) + eps_0 tau^2 = 1 + (tau^2/2)(rho^2 kappa + delta/2) <= 1 + (tau^2/2)(1 - delta)
(rho^2 kappa = 1 - 2 delta). With T_0^2 <= 3 delta and, at late stages, p*(f' - f) <= (1-rho^2)T_0^2/6 and p*(g' - rho g) <= (1-rho^2)T_0/6, Lemma 1.4
gives g' in C(f'); (f', g') attains its norm and converges to (f, rho g). QED.

## 2.2 Remarks on the proof. (PROVED statements.)
 (a) No "transfer error" occurs: the one-sided decompositions of f transfer EXACTLY to f' after (i) recomputing the d-coefficients at f'
     (which kills every first-order Hilbert mismatch in the blocks: the first-order block term at f' is <D omega, D w'>/C' - d' = 0),
     (ii) the steering conditions v_m(xhat') = 0 (equivalently d'^+_m = d'^-_m), which make the two side decompositions represent the SAME g',
     and (iii) replacing the tail of g beyond the window by the theta-tail sum_m R_m* omega^theta_m-part (the base part of g' beyond N is 0),
     which turns the non-constant split into a constant split beyond N (A_referee 5.1) while the window part is made two-sided by masses.
 (b) Order of choices: N, then s_1 (<= tau_N/(4A_0)), then Far (pull of size ~ s_1 at costless coordinates: flipped far contacts carrying
     negative masses), then N'' (tail cost <= eps_0 s_1 |tau|), then mu (raise by a mass at j_+, intermediate value theorem), then p.
     No step requires a rate, a tail-independence radius, or any information about the deep block structure of f.
 (c) The mixed second-order/first-order term created by the masses (part 3, 3.1) is exactly cancelled by Step 1: it is the first-order
     difference between the two sides, <U*v, e' - e>, and Step 1 makes v(xhat') = 0.

## 2.3 Corollaries. PROVED.
 (a) (A_referee §5.2/§5.4 made rigorous.) The two-piece mates g = v 1_{K_1} - (v 1_{K_1})(zhat) a, v = c u_{k_0,m}, over an infinite contact set
     with ARBITRARY (non-constant) split K' = K_1 + K_2, are recovered: data b+ = g, omega+ = 0; b- = g - v, omega- = (c/lambda_{k_0,m}) e_{k_0};
     w_m(k_0) = 0 gives d+ = d- = 0 (d-neutral); single block. Lemma 1.7 applies (P1 Prop 2.3 shows one-sided admissibility for small c).
     Hence g in Ls(f). (The "extra degree of freedom in the masses" of A_referee §5.4 is replaced by Step 1: P1's correction is confirmed and
     generalized.)
 (b) (P1 Prop 6.3 made rigorous, with P1-referee's sharpening.) At P1's example (T of P1 2.1, f of P1 2.2): every g in E_u (P1 6.1) with
     mu+ <= inf theta(g), mu- >= sup theta(g) and rho^2 max( h(g - mu+- u), (mu+-)^2/C_1 ) < 1 has (f, rho g) in cl NA. In particular the
     whole slab {g in E_u : ||theta(g)||_inf <= theta_*} (P1 6.2), including all the explicit defect mates of P1 Thm 2.4, lies in Ls(f).
 (c) (Every one-sided-linear exact resonance with one active block is harmless.) If f has F finite and g in C(f) has one-sided admissible
     two-piece data with a single active block and Delta d = 0, then g in Ls(f). This is the complete class of "exact-resonance" switching
     mates of P1 4.1 with finitely supported block carriers whose transfer does not involve R_m* w_m.

## 2.4 Remark (shifted two-piece data; the full fibre at P1's example). SKETCH.
For g in C(f) at P1's example, optimal decompositions at scale t carry, besides g - mu_t u on the base and mu_t u on the carrier, O(t^2)
first-order masses (shifts, A §4.5 / A §9(f)); the limits mu+- of mu_t along t -> 0+- satisfy only SHIFTED second-order bounds
H^sh <= 1, not kappa <= 1. Theorem 2.1 extends verbatim to two-piece data with quadratic shifts tau^2 theta^sigma_m w_m (A Def 4.15) on each
side, the shift kink costs being transported as in the proof of A Thm 4.17 (limsup of kappa_q at f' <= kappa_q at f, by domination) and
the theta-certificate at small scales using the shift theta^theta := (1-theta)theta^+ + theta theta^- (H^sh is convex). Combined with P1 6.1
(every g in C(f) lies in E_u with such limit decompositions) this would give f in R (every mate recovered) at P1's example. The shifted
transport of A Thm 4.17 has non-explicit o(tau^2) remainders, which are harmless here because Theorem 2.1 needs only a FIXED range
|tau| <= T_0 and uniform convergence along the construction. Not written out in full; status SKETCH.

