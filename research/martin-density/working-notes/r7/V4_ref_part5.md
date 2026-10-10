# V4 referee, part 5: full proofs of the repair R1 (weak swallowing-type peak) and of the new Proposition R5

Standing: SLD-type design with (SF*) (and (SF_tau), (b') for R5), (Z0) with p, p', p'', p''' in Z_0 and targets y* := (e_p^* - e_{p'}^*)/q*(.),
y** := (e_{p''}^* - e_{p'''}^*)/q*(.) in the family (Lemma 2.1), diagonal U, I = {1, ..., N}; owners and recursions relative to L_N (Lemma R3).
For a carrier l: n_l val_l = A_l + eps_l(B_l + delta_l H_l) when l is built by the owner step with sign eps_l (notation of Construction SA).

## R1.  Lemma (weak swallowing-type peak in self-aligned form).  PROVED.
Let m_0 <= N, F := {p, p', p'', p'''}.  For every xi in (0, 1) and every epsilon > 0 there is a first row f with supp a = F such that: every
carrier of L_N is swallowed with sign eps_l = sgn val_l (z = eps_l on S_l); l_- (a carrier of block m_0 with target y*) is a strict non-peak with
q_{l_-} < 0; l_D (a carrier of block m_0 with target y**) is a swallowing-type peak or strict non-peak whose relative margin
g := (nu_{l_D} - theta_{m_0})/theta_{m_0} satisfies |g - xi| <= epsilon; every other carrier satisfies n_l|val_l| >= (B_l + delta_l H_l)/2 and is a
non-degenerate swallowing-type peak; W-type sums are z-signed (Step 6 of Theorem 2.2) and c_*(l) = 0 in block m_0.
Proof.  (1) Parameters.  As in Proposition 5.1, a <-> b in the open positive orthant Omega of S^3 (zhat_j = 1 + s_j b_j on F).  The values of l_-
and l_D (with eps = +1 and z = +1 on their signature sets) are n_- val_- = c*(s_p b_p - s_{p'} b_{p'}) + delta_- H_- and n_D val_D =
c**(s_{p''} b_{p''} - s_{p'''} b_{p'''}) + delta_D H_D, independent of every other choice (targets supported in F).  Fix l_c (first carrier of block
m_0 other than l_-, l_D), theta_0 := lambda_{l_c} delta°_{l_c}/2, and l_1 the first carrier of block m_0 (assume l_1 = l_c; otherwise argue with l_1).
Take l_- late so that delta_- H_- + eta < c* s_{p'} and fix eta < n_- theta_0 Phi_-/(2 m_0).  The map b -> (c*(s_p b_p - s_{p'} b_{p'}), c**(s_{p''} b_{p''} -
s_{p'''} b_{p'''})) is a submersion on Omega (the two linear forms and the normal b are independent there: the forms involve disjoint pairs of
coordinates and b has all coordinates positive), so by the implicit function theorem there are an open interval J containing 0 and a
smooth curve x -> b(x) in Omega, |b'(x)| <= C_b, with n_- val_- = -eta and n_D val_D = x + x_0 along it, for a fixed base value x_0; as
delta_D H_D -> 0 when l_D -> infinity the base point may be taken in a fixed compact subset of Omega, so C_b, J do not depend on l_D (l_D late).
(2) Rows.  At x = 0 build the row by the PURE owner rule (L_N-relative) for all carriers other than l_-, l_D (eps_- = eps_D := +1).  For x in J build
it by the HYSTERETIC rule with reference signs eps^0_l from x = 0: eps_l(x) := eps^0_l unless eps^0_l A_l(x) <= -(B_l + delta_l H_l)/2, in which case
eps_l(x) := sgn A_l(x).  Every carrier other than l_-, l_D then has n_l|val_l(x)| >= (B_l + delta_l H_l)/2 with sign eps_l(x), so Step 4 of Theorem
2.2 (with |val_l| >= delta°_l/2) makes it a non-degenerate swallowing-type peak, and Steps 6-7 apply verbatim (they use only z_j = eps_o sgn u_o(j)
at owner coordinates).
(3) No coarse flip.  Let R := 4 n_D theta^max Phi_{l_D}/m_0 with theta^max := m_0(1 + ||U||)/Phi_{l_1} (an upper bound for theta_{m_0} at every row of
the family: l_1 is a peak, theta < nu_{l_1} <= m_0(1+||U||)/Phi_{l_1}).  Restrict x to |x| <= R (inside J for l_D large).  Before the first flip only
zhat_F moves, so |A_l(x) - A_l(0)| <= ||y_l 1_F||_1 max_F s_j C_b |x| <= C_1' R with C_1' := 2 max s C_b; a flip at l needs this to be >= (B_l + delta_l H_l)/2 >=
delta_l H_l/2 (at x = 0, eps^0_l A_l(0) >= 0).  For l < l_D: by (SF*) second half, c_{l_D} <= c_{l+1} <= c_l/4 <= delta_l H_l 2^{-l-12}, so
C_1' R <= C_1' 4 n_D m_0(1+||U||) c_{l_D}/(m_0 Phi_{l_1}) <= C'' 2^{-l} delta_l H_l/Phi_{l_1}; this is < delta_l H_l/2 for l > L_1 := log_2(4C''/Phi_{l_1}), and for
the finitely many l <= L_1 it holds once c_{l_D} < min_{l <= L_1} delta_l H_l Phi_{l_1}/(4 C'''), i.e. for l_D late.  Hence no carrier l < l_D flips on |x| <= R.
(4) Approximate intermediate values.  Put g(x) := (nu_D(x) - theta(x))/theta(x), nu_D(x) = m_0(x + x_0)/(n_D Phi_D) (choose x_0 so that nu_D(-R/2) <=
theta/2 and nu_D(R/2) >= 2 theta for all rows, possible since the range of nu_D over |x| <= R/2 is m_0 R/(n_D Phi_D) = 4 theta^max).  For x, x' in [-R, R]:
the carriers < l_D other than l_D have values depending continuously on x (no flips), with ||zeta^{<l_D}(x) - zeta^{<l_D}(x')||_1 <= C_2|x - x'|, and
every carrier > l_D has |val| <= 1, so ||zeta(x) - zeta(x')||_1 <= C_2|x - x'| + lambda_D|val_D(x) - val_D(x')| + 2 sum_{l > l_D} lambda_l.  By Lemma 5.2(a)
(all rows lie in one ball around the row at 0: the ball's radius is fixed and the l_1 distances are O(R) + O(sum_{l>l_D} lambda_l)),
|theta(x) - theta(x')| <= L_Theta(C_3 |x - x'| + 2 sum_{l>l_D} lambda_l).  Let x* := sup{x in [-R/2, R/2] : g(x) <= xi}.  There are x' <= x* < x'' arbitrarily
close to x* with g(x') <= xi < g(x'') (or x* = R/2, impossible since g(R/2) >= 1 > xi).  Then
   |g(x'') - g(x')| <= C_4|x'' - x'| + 3 L_Theta 2 sum_{l > l_D} lambda_l/theta_min,
theta_min := theta_0 (Theorem 2.2 Step 3 lower bound, valid at every row).  Letting x', x'' -> x* gives a row with g in [xi - epsilon', xi],
epsilon' := 6 L_Theta sum_{l > l_D} lambda_l/theta_0, which is <= epsilon for l_D late.  l_D is a swallowing-type peak if g >= 0 (val_D > 0 = sign of z on
S_D), a strict non-peak with q > 0 otherwise.  l_- keeps n_- val_- = -eta, a strict non-peak with gap >= M/2 and q < 0.  QED
Remarks.  (a) The rows are self-aligned (z = sgn val_l on S_l for every l) but not pure owner-rule rows; this is all that V4's Corollary 3.1 and
Remark 2.3(1) use.  (b) EXACT degeneracy (g = 0) is not obtained: the jump part of theta (fine flips) may skip the value; V4's OPEN label stands.
(c) The same sweep with hysteresis repairs every "move a ratio on F and run the owner rule" argument in V4 (it is the mechanism of Lemma 4.4).

## R5.  Proposition (exact all-negative data are non-generic in every fixed-z fibre).  PROVED.
Assume (SF_tau), (b') with tau_l -> 0, U diagonal, F finite with d := |F| >= 2, sigma in {-1,1}^F, z in B_{l_infty} with z = sigma on F, and A as in
Prop. 5.1.  Then the set of a in A for which SOME g in C(f_a) carries two-piece data with Delta d_m < 0 for every m in I is meagre in A.
Proof.  Work in Omega (Prop. 5.1(1)).  For a block m and a carrier l of block m let O_l be the set of b in Omega with
   (i)  2 tau_l theta_m(b) Phi_l/(m M_m(b)) < |val_l(b)| < theta_m(b) Phi_l/(2m),   and   (ii) some j in S_l \ F has z_j != sgn val_l(b).
O_l is open (val_l, theta_m, M_m are continuous in b; (ii) is open on {val_l != 0}).  CLAIM: for every m and L, V_L^m := union_{l >= L, m(l) = m} O_l
is dense.  Given b_0 and a connected open O, construct y with psi_y(b_0) = 0 and non-zero tangential gradient, and carriers l_i -> infinity of block
m with q*(u_{l_i} - y) -> 0, as in Prop. 5.1(2); for i large val_{l_i} = +-c_0/2 at points b_+-, and S_{l_i} ∩ F = {}.  If z is not constant on
S_{l_i}, (ii) holds wherever val_{l_i} != 0; if z = eps_i on S_{l_i}, (ii) holds where sgn val_{l_i} = -eps_i.  Let kappa_i(b) be the midpoint of the
window in (i) (positive, continuous, O(Phi_{l_i})); the window is non-empty once 2 tau_{l_i}/M_m < 1/2, i.e. for i large (tau -> 0, M_m >= 1/2).  On a
path in O from the point where val_{l_i} has sign eps_i... more precisely from b_{+} to b_{-} (or reversed so that the end point has sign -eps_i),
h := val_{l_i} + eps_i kappa_i changes sign for i large (|val| = c_0/2 >> kappa_i at the ends), so val_{l_i}(b) = -eps_i kappa_i(b) at some b in O, and
b in O_{l_i}.  Hence V_L^m is open and dense, and G := intersection_{m in I} intersection_L V_L^m is a dense G_delta.
Let b(a) in G and suppose g in C(f_a) carries data with Delta d_m < 0 for all m; let m* be a block with |Delta d_{m*}| = C_1.  Infinitely many carriers
l of block m* lie in O_l; all but finitely many of them are outside K_omega and have S_l ∩ (F ∪ E) = {} (K_omega, E finite, the S_l disjoint).  For
such l: by (i), l is a strict non-peak (nu_l < theta/2) with |w(l)| = M nu_l/theta in (2 tau_l, M/2), so |gamma_l| = lambda_l C_1 |w(l)| >= 2 tau_l C_1 lambda_l: l is
neither neutral nor negligible.  Take j from (ii); j in S_l \ (F ∪ E) is owned by l (L_N-relative owner, allowedness (a)).  Proposition 4.2' gives
|z_j| = 1 and z_j = sgn(gamma_l u_l(j)) = sgn(-Delta d_{m*} w(l)) = sgn val_l, contradicting (ii).  So a notin b^{-1}(G).  QED
Consequences.  (1) Theorem 5.6 and Corollary 5.7 act only on a meagre subset of every fixed-z fibre (as does (BT), Prop. 5.1).  (2) The first
alternative of V4's "structure of a counterexample" (no exact data with kappa_w <= 1 at f) is the generic one, so the decisive open problem for
F finite is the window-method residual (C*) of V2-ref, not the dead zones of exact data.  (3) tau_l -> 0 is implicitly required by V4 (Lemma 5.4
chooses L_0 with tau_{L_0} <= min_m |Delta d_m| M_m/(4 C_1)); it should be added to the definition of (SF_tau).
