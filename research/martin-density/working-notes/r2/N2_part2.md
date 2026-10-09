# N2 part 2: engineered recovery of exact two-piece mates with Delta d = 0 (rigorous)

Setting and notation of part 1. Throughout: f in S_{p*}, F = supp a finite, g in C(f) with an exact two-piece representation
(b+-, omega+-) (Def 1.1), v = b+ - b- != 0 (else g in Cert(f), Lemma 1.2(d)), a SINGLE active block m_0 (Delta omega_m = 0 for
m != m_0; so v = ell - Delta d R*_{m_0} w_{m_0}, ell := ell_{m_0}, Delta d := Delta d_{m_0}). In this part Delta d = 0, so v = ell.

## 2.1 Lemma (tuning direction). PROVED.
Put c_j := <P_{e-perp} U*v, U*e_j*> (j in N). There are j_+ in F cup K and sigma_+ in {-1, +1}, with sigma_+ = z_{j_+} if j_+ in K,
such that c_+ := sigma_+ c_{j_+} > 0.
*Proof.* v is in Y \ {0} (Lemma 1.2(b),(d)), hence not in c_00, hence not a multiple of a; U* is injective, so U*v is not a multiple
of U*a = nu e, i.e. P_{e-perp} U*v != 0. Since supp v is in F cup K and the series converges in l_1,
  sum_{j in F} v_j c_j + sum_{j in K} |v_j| z_j c_j = <P_{e-perp} U*v, U*v> = ||P_{e-perp} U*v||^2 > 0   (z_j v_j = |v_j| on K).
If c_j != 0 for some j in F take j_+ := j, sigma_+ := sign c_j. Otherwise the first sum vanishes and some j in K has z_j c_j > 0. QED.
(Example: in P1's example F = {1}, U*e_1* = nu_1 e, so c_1 = 0 and only contact directions exist; for diagonal U all
contact directions have z_j c_j >= 0: masses alone can only RAISE v(x'), which is why far pulls are needed.)

## 2.2 Lemma (two elementary continuity facts). PROVED.
(a) For A in l_1 with U*A != 0 let E(A) := U*A/||U*A||. If ||U*(A - a)|| <= nu/2 then ||E(A) - e|| <= 2||U*(A - a)||/nu.
(b) There is delta_1 > 0 such that for all A with ||A - a||_1 <= delta_1 and all real mu with |mu| <= delta_1:
    d/dmu <U*v, E(A + mu sigma_+ e*_{j_+})> >= c_+/(2 nu).
*Proof.* (a) ||x/||x|| - y/||y|| || <= ||x - y||/||y|| + | ||y|| - ||x|| |/||y|| <= 2||x - y||/||y|| with y = U*a, ||y|| = nu.
(b) The derivative equals sigma_+ <P_{E(A_mu)-perp} U*v, U*e*_{j_+}>/||U*A_mu||, A_mu := A + mu sigma_+ e*_{j_+}, a continuous function of
(A, mu) near (a, 0) in l_1 x R, with value c_+/nu at (a, 0). QED.

## 2.3 Theorem 1 (engineered recovery, Delta d = 0). PROVED.
Let f in S_{p*} with F = supp a finite, and let g in C(f) have an exact two-piece representation with a single active block and
Delta d = 0. Then g is in Ls(f): for every rho in (0,1) there are norm-attaining f'_n in S_{p*} and g'_n in C(f'_n)/rho with
(f'_n, rho g'_n) in NA((c_0,p), l_2^2) and (f'_n, rho g'_n) -> (f, rho g). Hence (f, rho g) is in cl NA for all rho < 1.
The approximants are engineered (window masses on the contacts, far sign-flipped contacts carrying negative masses, one
tuning mass fixed by the intermediate value theorem, a constant-theta tail); theta in [0,1] is arbitrary.

### Proof.
**Step 0 (constants; chosen from f and the representation only).** Fix rho, theta. Let eta_0 > 0 with rho^2 (1+eta_0)^3 <= (1+rho^2)/2.
Gamma := 1 + max(||b+||_1, ||b-||_1, ||v||_1); a_min := min_F |a_j|; gamma_min := min over m and k in supp omega+_m cup supp omega-_m of
gap_m(k) (> 0); W_max := max_{m,+-} ||omega+-_m||_inf; d_max := 1 + max_{m,+-} |d_m(omega+-_m)|; C_min := min_m C_m.
Choose T_0 in (0,1] with: T_0^2 <= (1 - rho^2)/2; 2 T_0 rho W_max <= gamma_min/4; 8 T_0 rho d_max (1 + 1/C_min) <= eta_0;
4 T_0 rho Gamma ||U||/nu <= eta_0/(1+eta_0) (Hilbert factor); 4 T_0 rho Gamma <= a_min/4; and T_0 K_c <= eta_0, where
K_c := 16 Gamma ||U||/nu + 8 d_max/C_min bounds the kappa of all certificates used below (A Def 4.1) once the data of f'
are within a factor 2 of those of f. Let j_+, sigma_+, c_+ be as in 2.1 and delta_1 as in 2.2(b).

**Step 1 (parameters for step n).** Write mx(N) := max{|v_j| : j in K, j > N} (> 0: supp v cap K is infinite, Lemma 1.2(d)).
 (i) Window: N_n -> infinity, N_n > max(F cup {j_+}), and 8 T_0 rho ||U*v|| max_{j > N_n} nu_j <= nu (nu_j := ||U*e_j*|| -> 0).
 (ii) D_n := mx(N_n) -> 0 and t_n := nu D_n/(16 ||U*v|| (||U|| + 1) Gamma) -> 0.
 (iii) Far_n := the shortest initial segment (in increasing order) of {j in K : j > N_n, v_j != 0} with sum_{Far_n} |v_j| >= D_n;
      then D_n <= sum_{Far_n} |v_j| <= 2 D_n (the last element added is <= mx(N_n) = D_n).
 (iv) N''_n > max Far_n with rho ||v 1_{K cap (N''_n, infinity)}||_1 <= 3(1 - rho^2) t_n/16 and ||v 1_{K cap (N''_n, infinity)}||_1 <= D_n.
 (v) Masses: m_{n,j} := 4 t_n |b_theta,j| for j in K cap [1, N_n]; far masses m'_{n,j} := 2 T_0 rho |v_j| for j in Far_n. For mu >= 0:
      A_n(mu) := a + sum_{j in K cap [1,N_n]} m_{n,j} z_j e_j* + mu sigma_+ e*_{j_+} - sum_{j in Far_n} m'_{n,j} z_j e_j*,
      a'_n(mu) := A_n(mu)/q*(A_n(mu));  z'_n := z on [1, N''_n] \ Far_n, -z on Far_n, 0 on (N''_n, infinity);
      x'_n(mu) := z'_n + U E(A_n(mu)).
For mu small, a'_n(mu) has the sign of a on F, z'_n is in c_00, |z'_n| <= 1, and z'_n = sign a'_n(mu) on supp a'_n(mu)
(F: z = sign a; window masses and a mass at j_+ in K carry sign z_j; far masses carry sign -z_j = z'_j). So by Fact D,
a'_n(mu)(x'_n(mu)) = q*(a'_n(mu)) = 1 = q(x'_n(mu)), and f'_n(mu) := grad p(x'_n(mu)) is norm attaining, with base data
(a'_n(mu), z'_n, E(A_n(mu))) and base contact xhat' = x'_n(mu).

**Step 2 (exact tuning by the intermediate value theorem).** Let psi_n(mu) := v(x'_n(mu)). Since v(zhat) = 0, supp v in F cup K, z'_n = z on F:
  psi_n(mu) = <U*v, E(A_n(mu)) - e> - 2 sum_{Far_n} |v_j| - ||v 1_{K cap (N''_n, inf)}||_1.          (2.3.1)
By 2.2(a) (||U*(A_n - a)|| <= nu/2 for n large; ||U*e_j*|| <= ||U||) and Step 1(i),(ii):
|<U*v, E(A_n(0)) - e>| <= (2||U*v||/nu)(4 ||U|| t_n Gamma + sum_{Far} m'_{n,j} nu_j) <= D_n ||U||/(2(||U||+1)) + (1/2) sum_{Far} |v_j|
<= D_n/2 + (1/2) sum_{Far} |v_j|. Hence, by (iii),(iv): psi_n(0) <= D_n/2 - (3/2) D_n < 0 and psi_n(0) >= -D_n/2 - 5 D_n - D_n >= -7 D_n.
Put mubar_n := 14 nu D_n/c_+ -> 0. For n large, ||A_n(mu) - a||_1 <= 4 t_n Gamma + mubar_n + 4 T_0 rho D_n <= delta_1 for mu in [0, mubar_n],
so by 2.2(b) psi_n(mubar_n) >= psi_n(0) + mubar_n c_+/(2 nu) >= 0. psi_n is continuous; choose mu_n in (0, mubar_n] with psi_n(mu_n) = 0.
From now on a'_n := a'_n(mu_n), x'_n := x'_n(mu_n), f'_n := grad p(x'_n), and all data of f'_n are primed.

**Step 3 (convergence).** ||A_n(mu_n) - a||_1 -> 0, so a'_n -> a in l_1; z'_n -> z coordinatewise (z'_n = z on [1, N_n], N_n -> infinity).
By Lemma 1.5, f'_n -> f, and for n large: supp omega+-_m is contained in Q'_{n,m} with gaps' >= gamma_min/2, C'_{n,m} >= C_m/2,
nu'_n >= nu/2, |a'_{n,j}| >= a_min/2 on F, |d'_{n,m}(omega+-_m)| <= d_max, q*(A_n(mu_n)) <= 4/3, and the block coefficients
H'_{n,m}(omega) -> H_m(omega) for omega in {omega+_m, omega-_m, omega_theta,m}. Moreover d'_{n,m_0}(Delta omega) = ell(x'_n)/|R_{m_0} x'_n| (Lemma 1.2(c),
homogeneity) = psi_n(mu_n)/|R_{m_0} x'_n| = 0 (ell = v as Delta d = 0); for m != m_0, Delta omega_m = 0. So Delta d'_{n,m} = 0 for all m.

**Step 4 (the target and its three decompositions).** s_n := -(b_theta 1_{[1,N_n]})(x'_n); since z'_n = z on [1, N_n],
(b_theta 1_{[1,N_n]})(x'_n) = (b_theta 1_{[1,N_n]})(zhat) + <U*(b_theta 1_{[1,N_n]}), E_n - e> -> b_theta(zhat) = 0 (Lemma 1.2(a),(f)); so s_n -> 0.
  b'_{0} := b_theta 1_{[1,N_n]} + s_n a'_n,   g'_n := b'_0 + sum_m R_m*( omega_theta,m - d'_{n,m}(omega_theta,m) w'_{n,m} ).
Then g'_n - g = -b_theta 1_{(N_n, inf)} + s_n a'_n + sum_m R_m*( d_m(omega_theta,m) w_m - d'_{n,m}(omega_theta,m) w'_{n,m} ) -> 0 in l_1.
Since Delta d'_{n,m} = 0, d'(omega_theta) = d'(omega+) = d'(omega-) blockwise, and with v = ell = R*_{m_0} Delta omega:
  g'_n = b'+ + sum_m R_m*(omega+_m - d'(omega+_m) w'_m),   b'+ := b'_0 + theta v = b+ 1_{[1,N_n]} + theta v 1_{(N_n,inf)} + s_n a'_n;
  g'_n = b'- + sum_m R_m*(omega-_m - d'(omega-_m) w'_m),   b'- := b'_0 - (1-theta) v = b- 1_{[1,N_n]} - (1-theta) v 1_{(N_n,inf)} + s_n a'_n.
Also b'_0(x'_n) = 0 and b'+-(x'_n) = +- (theta or 1-theta) psi_n(mu_n) = 0.
Coordinate structure (n large): on J (free coordinates) b'_0, b'+, b'- vanish; on supp a'_n they are dominated as described below;
on contacts in (N_n, N''_n] \ Far_n the entries theta v_j (resp. -(1-theta) v_j) are z-signed (resp. anti-z-signed); beyond N''_n they
are theta v_j (resp. -(1-theta)v_j) at coordinates with z'_n = 0.

**Step 5 (small scales |tau| <= min(2 t_n/rho, T_0): a two-sided finite certificate at f'_n).** c' := (b'_0, omega_theta) is a finite
certificate at f'_n (A Def 4.1): supp b'_0 in supp a'_n (F, the window contacts with b_theta,j != 0 carry masses, a'_n-multiple);
b'_0(x'_n) = 0; omega_theta,m in c_00(Q'_{n,m}). Ratios: on F, |b'_{0,j}|/|a'_{n,j}| <= 2 Gamma/a_min + |s_n|; on window mass coordinates
|b_theta,j| q*(A_n)/m_{n,j} + |s_n| <= 1/(3 t_n) + |s_n| (q*(A_n) <= 4/3); elsewhere on supp a'_n only |s_n|. So
1/||b'_0/a'_n||_inf >= 1/(1/(3t_n) + |s_n| + 2Gamma/a_min) >= 2 t_n for n large, and r(c') >= 2 t_n (the Hilbert and block radii are
bounded below independently of n). g_{c'} = g'_n. H(c') = max(h'(b_theta 1_{[1,N_n]}), H'_m(omega_theta,m)) ->
max(h(b_theta), H_m(omega_theta,m)) <= kappa <= 1 (Lemma 1.2(f); h' ignores multiples of a'_n), so H(c') <= 1 + eta_0 for n large; kappa(c') <= K_c.
A Prop 4.5 at f'_n for rho c' (H(rho c') = rho^2 H(c'), r(rho c') = r(c')/rho, kappa(rho c') <= kappa(c')): for |tau| <= min(2t_n/rho, T_0),
  p*(f'_n + tau rho g'_n) <= 1 + (tau^2/2) rho^2 (1+eta_0)(1 + K_c T_0) <= 1 + tau^2 rho^2 (1+eta_0)^2/2 <= 1 + tau^2 (1/2 - (1-rho^2)/4) <= s(tau),
using s(tau) >= 1 + tau^2/2 - tau^4/8 >= 1 + tau^2/2 - (1-rho^2) tau^2/16 for tau^2 <= (1-rho^2)/2.

**Step 6 (intermediate scales t_n <= |tau| <= T_0: one-sided decompositions).** Let 0 < tau <= T_0 (tau < 0 is symmetric with b'-, omega-):
  f'_n + tau rho g'_n = (a'_n + tau rho b'+) + sum_m R_m*( w'_m + tau rho (omega+_m - d'(omega+_m) w'_m) ).
Base (Lemma 1.4 with B := rho b'+, B(x'_n) = 0): no sign changes on supp a'_n: on F, |tau rho b'+_j| <= T_0 rho (Gamma + 1) <= a_min/2 <= |a'_{n,j}|;
on window mass coordinates tau b+_j has the sign z_j of a'_{n,j} (the s_n a'_n part only rescales a'_{n,j} by 1 + tau rho s_n > 0); on Far_n,
|a'_{n,j}| = m'_{n,j}/q*(A_n) >= (3/2) T_0 rho |v_j| >= (3/2)|tau rho theta v_j| (q*(A_n) <= 4/3), and the s_n a'_n part only rescales
a'_{n,j} by 1 + tau rho s_n >= 9/10, so no sign change; at j_+ in K the entry is z-signed. Kinks:
zero on J (entries 0), on contacts with z'_n = z (z-signed entries, tau > 0), and the only contribution is beyond N''_n:
kink'_tau(rho b'+) <= tau rho theta ||v 1_{K cap (N''_n,inf)}||_1 <= 3(1 - rho^2) tau t_n/16 <= 3(1-rho^2) tau^2/16 (tau >= t_n).
Hilbert: tau rho ||U*b'+|| <= T_0 rho Gamma ||U|| (1 + o(1)) <= nu'/2 and h'(b'+) -> h(b+) <= 1 (||b'+ - b+||_1 <= ||b+ 1_{(N_n,inf)}|| +
||v 1_{(N_n,inf)}|| + |s_n| -> 0; h'_n -> h uniformly on bounded sets since e'_n -> e, nu'_n -> nu), so for n large
  q*(a'_n + tau rho b'+) <= 1 + 3(1-rho^2) tau^2/16 + tau^2 rho^2 (1+eta_0)^2/2.
Blocks (A Lemma 4.4(d) at f'_n; |tau rho omega+_m(k)| <= gap'(k)/2 and the d-radii hold by the choice of T_0):
  N_m(w'_m + tau rho(omega+_m - d' w'_m)) <= 1 + (tau^2 rho^2/2) H'_m(omega+_m)(1 + eta_0) <= 1 + tau^2 rho^2 (1+eta_0)^2/2  (n large).
By Fact A, p*(f'_n + tau rho g'_n) <= 1 + tau^2 [rho^2(1+eta_0)^2/2 + 3(1-rho^2)/16] <= 1 + tau^2 [1/2 - (1-rho^2)/16] <= s(tau).
(The certificate of Step 5 covers |tau| <= t_n, so there is no gap between Steps 5 and 6.)

**Step 7 (large scales |tau| >= T_0: slack).** eps_n := p*(f'_n - f) -> 0, eta_n := p*(g'_n - g) -> 0 (Steps 3, 4; p* <= ||.||_1).
For n large, eps_n <= (1-rho^2) T_0^2/6 and rho eta_n <= (1-rho^2) T_0/6. Then for |tau| >= T_0, with A Lemma 4.7,
p*(f'_n + tau rho g'_n) <= p*(f + tau rho g) + eps_n + |tau| rho eta_n <= s(rho tau) + (1-rho^2) min(tau^2, |tau|)/3 <= s(tau)
(for T_0 <= |tau| <= 1: eps_n <= (1-rho^2)tau^2/6, |tau| rho eta_n <= (1-rho^2) tau^2/6; for |tau| >= 1 both are <= (1-rho^2)|tau|/6).

**Step 8 (conclusion).** For n large, p*(f'_n + tau rho g'_n) <= s(tau) for all real tau, i.e. rho g'_n in C(f'_n). By N_part1 Lemma 1.2(a),
(f'_n, rho g'_n) is a norm-one operator attaining its norm (at the normer of f'_n). It converges to (f, rho g). So (f, rho g) in cl NA for
every rho in (0,1), and g in Ls(f) (N_part1 Thm 1(iii)). QED.

Quantifier order (referee gap G3): rho, theta -> eta_0 -> T_0 (from f-data only) -> for each n: N_n -> D_n, t_n -> Far_n -> N''_n ->
mu_n (IVT, depends on all previous choices) -> f'_n, g'_n; then "n large" for the convergence statements of Steps 3-7.

## 2.4 What was fixed relative to P1 6.3 / referee report (C4)
 * (G1) g in C(f) is a hypothesis (used only in Step 7).
 * (G2) No coordinate with fractional value of z' is used: the exact zero psi_n(mu_n) = 0 is obtained from a continuous MASS parameter
   (IVT on mu), not from a partial pull z'_{j*} in (-1,1); the only first-order cost is the v-tail beyond N''_n, chosen after t_n.
 * (G3) Order of quantifiers as above. Also: the far pulls need no a-priori relation "t_m <= c tau_N": D_n := mx(N_n) automatically
   guarantees a far set with pull in [D_n, 2D_n].
 * The tuning direction always exists (Lemma 2.1); if c_j != 0 for some j in F, the tuning mass works in both directions and the
   far pulls can be dropped (Far_n := empty, mu in [-mubar_n, mubar_n]).

## 2.5 Corollary (P1's example; rigorous version of P1 6.3). PROVED.
Let T, f be as in P1 §2 (any finite I containing 1), u := u_{2,1}, lambda_0 := Phi_1(2). Every g in C(f) for which there are
mu+ <= inf_{j in K'} g_j/u_j and mu- >= sup_{j in K'} g_j/u_j with max( h(g - mu+- u), (mu+-)^2/C_1 ) <= 1 lies in Ls(f). In
particular this holds for the whole slab of P1 6.2 and for every two-piece mate g_{K_1} of P1 2.3 (0 < c <= c_*), i.e. the explicit
defect of P1 Thm 2.4 is recovered along engineered NA sequences.
*Proof.* By P1 6.1, g is in E_u. The representation b+- := g - mu+- u, omega+- := (mu+-/lambda_0) e_2 (block 1) satisfies (E1)
(supp in {1} cup K'; z_j(g_j - mu+ u_j) = u_j(g_j/u_j - mu+) >= 0 and similarly <= 0 for mu-), (E2) (Q_1 = {2}), (E3) (R_1*(e_2/lambda_0) =
u and d_1(e_2) = Phi_1(2)^2 w_1(2)/C_1 = 0), (E4) by hypothesis (H_1((mu/lambda_0) e_2) = (Phi_1(2) mu/lambda_0)^2/C_1 = mu^2/C_1 because
D_1 e_2 is orthogonal to D_1 w_1). Single active block, Delta d = 0. Apply Theorem 1. For the slab: P1 6.2's proof gives the
coefficients O(||theta||^2) small. For g_{K_1}: mu+ = 0, mu- = c, and P1 2.3's bounds give the coefficients <= 1 for c <= c_*. QED.
Remark. Whether ALL of C(f) at P1's example is recovered is not settled here: for g in C(f) whose explicit decompositions have
coefficient > 1, the actual decompositions rebalance at second order (peak/level shifts, transfer peaks); Theorem 1 would have to be
combined with a shifted / transfer-peak version at the engineered approximants (C_notes Thm 7.4). OPEN (plausible).

## 2.6 Remark (several active blocks). SKETCH.
If |I_act| >= 2 (all Delta d_m = 0), Step 2 must achieve ell_m(x'_n) = 0 for every active m. Since sum_m ell_m = v vanishes on J, the
v-condition is tuned as above (it is insensitive to free coordinates), and the remaining |I_act| - 1 conditions can be tuned by
o(1) moves of finitely many near free coordinates (which do not change v(x'_n)) PROVIDED the restrictions {ell_m|_J} have rank
|I_act| - 1 (no second resonance inside span{ell_m}). Under this rank condition the proof goes through verbatim (the tuning of the free
coordinates is a linear system with a fixed invertible matrix, solved after mu_n; its effect on v(x'_n) is nil).
