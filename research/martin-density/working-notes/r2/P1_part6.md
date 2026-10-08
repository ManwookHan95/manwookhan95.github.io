# P1 part 6: the whole fibre at the example, and engineered recovery of its defect

Setting of part 2 (T from 2.1, f from 2.2, u := u_{2,1}, lambda_0 := lambda_{2,1} = Phi_1(2), K' contacts, J := N \ ({1} cup K')
free coordinates (z = 0 there)). eps := s(t) - 1.

## 6.0 Lemma (margins at f). PROVED.
mu_{k,m} := |u_{k,m}(xi)| - theta_m Phi_m(k) >= q_0 psi(Phi_m(k)) for every peak, psi(phi) := min(1/4, 2 sqrt(phi)).
*Proof.* Non-exceptional k >= 2: |u(xi)| = q_0|u(zhat)| >= 1.6 q_0 rho_l (2.1(P3)), theta Phi <= q_0 pi_{k,m} <= q_0 rho_l^2 <= q_0 rho_l/26
(proof of 2.2(b)), rho_l = sqrt(2 Phi_m(k)/c_{l(1,m)}) >= sqrt(2 Phi_m(k)); so mu >= 1.5 q_0 rho_l >= 2 q_0 sqrt(Phi_m(k)).
Exceptional: |u(zhat)| > 1/2 and pi <= 1/4. k = 1: |u_{1,m}(zhat)| >= 7/9 and theta_m Phi_m(1) <= |zeta_m|/m <= q_0/2. QED.

## 6.1 Theorem (C(f) is contained in E_u). PROVED.
  E_u := { g in l_1 : supp g in {1} cup K', g(xi) = 0, theta(g) := (g_j/u_j)_{j in K'} is bounded }.
More precisely, if g in C(f), then for admissible decompositions at scales t_n -> 0+ (resp. -t_n) the carrier coefficients
mu_n := lambda_0 Omega_{t_n,1}(2) are bounded, and any limit mu+ (resp. mu-) satisfies mu+ <= g_j/u_j <= mu- for all j in K'.
*Proof.* Fix an admissible decomposition (B, Omega) at scale t > 0 (t <= t_1 small). Block m: level l_m := ||W_m||_inf, peak deviations delta_k.
(1) Peaks carry o(1): by 3.1(K1) and |alpha_k| = lambda_k mu_k/|zeta_m|, sum_P lambda_k mu_k delta_k <= eps. Split at Phi_m(k) = t^{4/3}:
    sum lambda_k delta_k <= eps/(q_0 psi(t^{4/3})) + 2 s(t) m sum_{Phi_m(k) < t^{4/3}} Phi_m(k) <= C_1 t^{4/3}
    (Phi_m(k) is decreasing in k with ratio <= 1/2, so the last sum is <= 2 t^{4/3}). Hence (1/t) sum lambda_k delta_k <= C_1 t^{1/3}.
(2) Level shifts are o(t): by the first-order balance (N_m(W_m) >= 1 + t<Omega_m, zeta_m>/|zeta_m|, q*(a+tB) >= 1 + tB(zhat), and
    q_0 B(zhat) + sum_m <Omega_m, zeta_m> = g(xi) = 0) one gets |t <Omega_m, zeta_m>| <= eps for every m. On P_m, t Omega_m(k) =
    sigma_k(l_m - M_m - delta_k); the only strict non-peak (2,1) has zeta_1(2) = 0. So
    (l_m - M_m) sum_{P_m}|zeta_m(k)| = t<Omega_m, zeta_m> + sum_P delta_k |zeta_m(k)|, and |zeta_m(k)| <= q_0 lambda_k, sum_P |zeta_m(k)| >= |zeta_m(1)| > 0:
    |l_m - M_m| <= C_2 t^{4/3}.
(3) Carrier bounded: D_1 e_2 is orthogonal to D_1 w_1 (w_1(2) = 0), so ||P-perp D_1 Omega_1|| >= Phi_1(2)|Omega_1(2)| = |mu_t|
    (m = 1), and 3.1(K2) gives mu_t^2 <= 2 s(t)^2/|zeta_1| <= 3/|zeta_1|.
(4) Decomposition of g: L*Omega = mu_t u + sum_m R_m*(Omega_m 1_{P_m}), and
    R_m*(Omega_m 1_{P_m}) = ((l_m - M_m)/(t M_m)) R_m* w_m - (1/t) sum_P lambda_k sigma_k delta_k u_k
    (w_m 1_{P_m} = w_m since w_1(2) = 0), whose l_1 norm is <= C_3 t^{1/3}. Hence ||g - B - mu_t u||_1 <= C_4 t^{1/3}.
(5) Free coordinates: by 3.1(B1) with z = 0 on J, ||B 1_J||_1 <= eps/(q_0 t) <= t/(2 q_0); u vanishes on J. So ||g 1_J||_1 <= C_5 t^{1/3},
    and letting t -> 0: g = 0 on J, i.e. supp g in {1} cup K'.
(6) Contacts (z = 1 on K'): the paid usage is sum_{K'} (B_j)_- <= eps/(2 q_0 t) (3.1(B1)), so sum_{K'} (g_j - mu_t u_j)_- <= C_6 t^{1/3}.
    Along t_n -> 0 with mu_{t_n} -> mu+: g_j >= mu+ u_j for all j in K'. The side t < 0 is symmetric (cheap sign of B_j is now
    negative): g_j <= mu- u_j. Since u_j > 0 on K', g_j/u_j in [mu+, mu-]. QED.
So C(f) lies in the infinite-dimensional space E_u, while cl Cert^sh(f) lies in the line R u (Theorem 2.4).

## 6.2 Proposition (a large slab of E_u consists of mates). PROVED.
There is theta_* > 0 such that every g in E_u with ||theta(g)||_inf <= theta_* lies in C(f).
*Proof.* As 2.3, with mu+ := inf theta(g), mu- := sup theta(g): side + f + t g = (a + t(g - mu+ u)) + L*(w + t(mu+/lambda_0) e_2), where
g - mu+ u is supported on {1} cup K', >= 0 on K' (cheap for t > 0), and (g - mu+ u)(zhat) = g(zhat) = 0; side - with mu- (<= 0 on K').
The base costs are Hilbert terms O(t^2 ||theta||^2), the block cost is t^2 (mu+-)^2/(2 C_1), the e_1*-coefficient stays positive;
the crude bound handles |t| >= 1. QED.
Consequently Def(f) contains { g in E_u : ||theta(g)||_inf <= theta_*, theta(g) not constant } (infinite dimensional).

## 6.3 Proposition (engineered recovery of the explicit switching mates). SKETCH (all estimates indicated).
Let g in E_u, theta := theta(g), mu+ := inf theta, mu- := sup theta, and let kappa+- := max( h(g - mu+- u), (mu+-)^2/C_1 ) be the
second-order coefficients of the explicit side decompositions of 6.2 (h = base Hilbert coefficient, A Def 4.1). If rho^2 max(kappa+, kappa-) < 1,
then (f, rho g) is in cl NA((c_0,p), l_2^2).
Construction (parameters: window N, mass scale t_m, a finite far set Far, cut-off N'', and mu_inf in [mu+, mu-]):
 * target: g' := g 1_{{1} cup (K' cap [1,N])} + mu_inf u 1_{K' cap (N, infinity)} + (multiple of a' making g'(x') = 0); ||g' - g|| <= 2||theta||_inf sum_{K'>N} u_j + o(1);
 * base: a' := normalization of a + sum_{j in K', j <= N} m_j e_j* + (tuning masses at contacts) - sum_{j in Far} m'_j e_j*, with window masses
   m_j := 2 t_m |theta_j - mu_inf| u_j + t_m u_j > 0 and far masses m'_j := 2 T_0 (|mu+| + |mu-| + |mu_inf|) u_j;
 * contact vector: z' := 1 on {1} cup ((K' cap [1, N'']) \ Far), z' := -1 on Far, z' := 0 elsewhere (z' in c_0, z' -> z coordinatewise);
   here Far is a finite subset of K' cap (N, N''] whose u-mass sum_{Far} u_j is of order t_m (needed in (i));
 * order of choices: N (window), then t_m <= c tau_N with tau_N := sum_{K' > N} u_j (so that Far fits into K' cap (N, infinity)),
   then Far and the tuning masses (by continuity, (i)), then N'' >= max Far so large that sum_{K' > N''} u_j <= (1 - rho^2) t_m/(48 S),
   S := |mu+| + |mu-| + |mu_inf|;
 * x' := z' + U e', e' := U*a'/||U*a'||, f' := grad p(x'/p(x')) = a' + L* J_V(L x') (A Fact D): NA.
(i) Exact carrier. u(x') = <U*u, e' - e> - sum_{K'} u_j (1 - z'_j) (using u(zhat) = 0). Positive tuning masses at a contact j_+ with
  <P_e-perp U*u, U*e_{j_+}*> > 0 raise the first term (j_+ exists: sum_{K'} u_j <P_e-perp U*u, U*e_j*> = ||P_e-perp U*u||^2 > 0, and the
  coordinate 1 contributes 0); the far coordinates (z' = -1) lower the second term by 2 sum_{Far} u_j ("free pulls"); a continuous parameter
  (a partial value of z' on one far coordinate) gives u(x') = 0 exactly (the far masses' own effect on the first term is
  O(T_0 S sum_{Far} u_j nu_j) with nu_j = ||U*e_j*|| -> 0, negligible against the pull 2 sum_{Far} u_j once N is large). Then zeta'_1(2) = 0, w'_1(2) = 0, k = 2 is again a strict
  non-peak of block 1 (gap M'_1), and R_1*((mu/lambda_0) e_2) = mu u is carried by block 1 at cost M'_1 + sqrt(C'^2 + t^2 mu^2) for every mu.
(ii) Small scales |t| <= t_m: f' + t rho g' = (a' + t rho (g' - mu_inf u)) + L*(w' + t rho (mu_inf/lambda_0) e_2). The base part
  g' - mu_inf u = (theta - mu_inf) u on the window, 0 on K' beyond N (this is why the tail of g' is mu_inf u), plus a multiple of a':
  it is supported in supp a' and the window masses exceed |t rho (theta_j - mu_inf) u_j|: no flips, no kinks, first-order term
  rho t (g' - mu_inf u)(x̂') = 0. Its coefficient is max(h'(g' - mu_inf u), mu_inf^2/C'_1) -> max(h(g - mu_inf u), mu_inf^2/C_1) <= max(kappa+, kappa-)
  by convexity of mu -> max(h(g - mu u), mu^2/C_1) on [mu+, mu-]. A two-sided finite certificate at f' with coefficient < 1/rho^2 (approximately).
(iii) Intermediate scales t_m <= |t| <= T_0: side + uses mu+, side - uses mu-. Base part g' - mu+- u: on the window (theta - mu+-)u has the cheap
  sign (window contacts with masses); on K' cap (N, N''] the entries (mu_inf - mu+-)u_j have the cheap sign at the contacts z' = 1; on Far
  they are absorbed by the far masses (|t| |mu_inf - mu+-| u_j <= m'_j: |A_j| - z'_j A_j = 0); beyond N'' (z' = 0) the first-order cost is
  <= |t| |mu_inf - mu+-| sum_{K' > N''} u_j <= (1 - rho^2) t^2/24 for |t| >= t_m, once N'' is chosen large AFTER t_m. Second-order terms -> kappa+-.
(iv) Large scales |t| >= T_0: slack (A Lemma 4.7): p*(f' - f) -> 0 (a' -> a in l_1, z' -> z coordinatewise, A Fact E / G Prop 6.6.3) and
  ||rho g' - rho g|| -> 0 as N -> infinity, t_m -> 0, Far -> infinity.
Hence for suitable parameters (f', rho g') is contractive and attains its norm at x'/p(x'), and (f', rho g') -> (f, rho g).
(The bookkeeping of the second-order terms at f' versus f is the same as in C Thm 7.1 / D Lemmas 11.3-11.4: finitely many changed
coordinates in each Hilbert term and e' -> e.)
Remark (correction to A_referee §5.4). The referee enforces u(x'') = 0 "by one extra degree of freedom in the masses". When every
available positive-mass direction RAISES u(x'') (e.g. U diagonal: <U*u, e'' - e> = sum_{K'} u_j sigma_j^2 m_j/nu + O(m^2) >= 0), the deficit
must be compensated by pulling contacts inward, which costs |t| x O(t_m) at first order on one side, comparable to the slack exactly
at the scale t_m where the masses are needed, with a constant that blows up as rho -> 1. The far NEGATIVE masses (sign-flipped far
contacts: allowed, because z' only has to converge coordinatewise) remove this obstruction. Also the referee's truncation of g must be
replaced by the constant tail mu_inf u (otherwise the carrier's tail costs first order at the smallest scales).
Remark (what is missing for f in R). By 6.1 every mate g lies in E_u, but 6.3 needs rho^2 max(kappa+, kappa-) < 1 for the EXPLICIT side
decompositions. For g in C(f) the actual optimal decompositions may be cheaper (second-order rebalancing through shifts, A §4.5); recovery
of all of C(f) would follow if the explicit decompositions, possibly shifted along R_m* w_m (shifts transport, A Thm 4.17), were
asymptotically optimal. Not proved (HEURISTIC: by the proof of 6.1, peaks, level shifts and free coordinates contribute only o(1) in
g-units, but they may contribute O(t^2) to the costs).
