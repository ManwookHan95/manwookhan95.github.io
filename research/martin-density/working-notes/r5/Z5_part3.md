# Z5 part 3: engineered recovery at arbitrary base support (Theorem thm:engineered for infinite F)

Setting: T admissible (arbitrary), I finite, f in S_{p*} with F = supp a arbitrary, s_j := sgn a_j (j in F), alpha(M) := sum_{j in F, j>M}|a_j|.
Definition def:twopiece is read verbatim for arbitrary F: a pair (b, omega) with b in l_1, omega_m in c_00(Q_m) represents g if
g = b + sum_m R_m*(omega_m - d_m(omega_m) w_m); it is side-+ (side--) admissible if b_j = 0 for j notin F cup K and z_j b_j >= 0
(<= 0) on K. No condition is imposed on F (support coordinates are two-sided for the definition).

Definition 3.1 (cushion-compatible data). Two-piece data (b^+-, omega^+-) are cushion-compatible if there is C_R < infinity with
  (R-inf)   |b^theta_j| <= C_R |a_j|,   (s_j b^+_j)_- <= C_R |a_j|,   (s_j b^-_j)_+ <= C_R |a_j|     for all j in F,
where b^theta := (b^+ + b^-)/2. Finitely based data (supp b^+- finite) are cushion-compatible. For F finite (R-inf) always holds.
In words: each piece uses a support coordinate against its sign (the direction that eventually flips) only proportionally to |a_j|.

## 3.1 Theorem E-inf. PROVED.
Theorem 3.2. Let I be finite, T admissible, f in S_{p*} with F arbitrary, g in C(f) carrying cushion-compatible two-piece data
(b^+-, omega^+-), and rho in (0,1) with rho^2 kappa_w < 1. Assume that I_- := {m : Delta d_m < 0} satisfies (SC) (no assumption if
I_- is empty). Then there are norm-attaining f'_i -> f with FINITE base supports and g'_i in C(f'_i) with g'_i -> rho g. In particular
(f, rho g) in cl NA((c_0,p), l_2^2), and if kappa_w <= 1 then (f, g) in cl NA. No hypothesis on K, Q_m (m notin I_-), or rates of T.

Corollary 3.3 (Corollary cor:D1 and cor:weightedengineered at arbitrary F). If g in C(f) carries cushion-compatible two-piece data
with Delta d_m >= 0 for all m and kappa_w <= 1 (or d-neutral data with rho^2 kappa_w < 1), then (f, g) (resp. (f, rho g)) is in cl NA.

Proof of Theorem 3.2. We run the proof of Theorem thm:engineered with the following modified approximants and list every place where
finiteness of F (through N_w >= max F, a_min = min_F |a_j|, supp a' containing F) was used.

Approximants. Parameters: window N_w, scale s_1, cut-off N'' > N_w. Put m_j := 4 rho s_1 |b^theta_j| for j in K cap [1, N_w],
  a'' := a 1_{[1,N_w]} + sum_{j in K cap [1,N_w]} m_j z_j e_j*,  a' := a''/q*(a''),  e' := U*a'/||U*a'||,
  z'_j := z_j (j <= N''),  z'_j := 0 (j > N''),  xhat' := z' + U e',  x' := xhat'/p(xhat'),  f' := grad p(x').
Then a'' in c_00, z' in c_00, |z'| <= 1, and z' = sgn a' on supp a' = (F cap [1,N_w]) cup {j in K cap [1,N_w] : b^theta_j != 0}
(on F cap [1,N_w], z'_j = z_j = s_j; on window contacts, a''_j = m_j z_j); so f' is norm attaining with forced data a', e', z',
zhat' = xhat' (Proposition prop:smooth(c)), and its base support is finite. The support coordinates j in F cap (N_w, N''] become
contacts of f' (z'_j = s_j, a'_j = 0), those beyond N'' free coordinates (z'_j = 0).
A construction sequence (N_{w,i}, s_{1,i}, N''_i) has s_{1,i} -> 0 and, chosen AFTER s_{1,i},
  (N0)  alpha(N_w) <= s_1^2,   rho sum_{j in F, j > N_w} (s_j v_j)_- <= delta s_1/32,   rho C_R s_1 <= 1/8,
and then N'' > N_w satisfying (eq:N1), (eq:N2) and rho V_{>N''} <= delta s_1/32, where v := b^+ - b^-, V_{>N''} := sum_{j>N''}|v_j|
(over all coordinates; this is (eq:N3) with delta s_1/32). Since v in l_1 and alpha(M) -> 0, (N0) holds for N_w large; so
N_{w,i} -> infinity, and N''_i -> infinity.

Lemma approxfacts. (a) holds with supp a' as above; q*(a'') <= q*(a 1_{[1,N_w]}) + (1+||U||)4 rho s_1||b^theta||_1 and
q*(a 1_{[1,N_w]}) <= 1 + ||U|| alpha(N_w), so q*(a'') <= 2 at late stages and |a'_j| >= |a_j|/2 on F cap [1,N_w], |a'_j| >= m_j/2 on
window contacts. (b) a' -> a in l_1 (alpha(N_w) -> 0, s_1 -> 0), z' -> z coordinatewise: Proposition prop:approximants.
(E1) becomes ||a'' - a||_1 <= 4 rho s_1 ||b^theta||_1 + alpha(N_w) <= 4 rho s_1||b^theta||_1 + s_1^2, so ||e' - e|| <= K_e s_1 with
K_e := 2||U||(4 rho ||b^theta||_1 + 1)/nu. (E2): xhat' - zhat = -z 1_{(N'',infinity)} + U(e' - e), as before. (E3)-(E5) and
Lemmas lem:F1, lem:anchor, lem:scrambling are consequences of (E1), (E2) and of the block structure; they hold verbatim.

Step 0. Replace the condition of (T_1) "rho T_0 (||b^+||_inf + ||b^-||_inf) <= a_min/8" by "rho T_0 C_R <= 1/8". All other choices
(T_1, K_sharp, eta_1, transfer data, T_0, s_{1,i}, N''_i) are as in the note; N_{w,i} is chosen after s_{1,i} by (N0).

Step 1 (target) and Step 2 (three exact decompositions): verbatim, with beta^theta := b^theta 1_{[1,N_w]},
beta^+- := b^+- 1_{[1,N_w]} +- (1/2) v 1_{(N_w,infinity)}; the identities beta^+- - beta^theta = +-(1/2)v and
v = sum_m R_m*((omega^-_m - omega^+_m) - Delta d_m w_m) (both pairs represent g) do not involve F; g'' - g =
-b^theta 1_{(N_w,infinity)} + (block terms) -> 0.

Step 3, base: the claim becomes
  Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} + rho |tau| sum_{j in F, j > N_w} (s_j v_j)_-,  and = 0 for diamond = theta.
Proof of the claim. On supp a' write a'_j + tau B^diamond_j = (1 - tau rho c) a'_j + tau rho beta^diamond_j with |tau rho c| <= 1/2.
 * j in F cap [1, N_w]: |a'_j| >= |a_j|/2 and s_j(1 - tau rho c)a'_j >= |a_j|/4. For diamond = theta (|tau| <= s_1),
   |tau rho beta^theta_j| <= s_1 rho C_R |a_j| <= |a_j|/8. For diamond = + (tau > 0), s_j tau rho beta^+_j >= -tau rho (s_j b^+_j)_- >=
   -T_0 rho C_R |a_j| >= -|a_j|/8. For diamond = - (tau < 0), s_j tau rho beta^-_j = -|tau| rho s_j b^-_j >= -T_0 rho C_R |a_j| >= -|a_j|/8.
   In all cases s_j(a'_j + tau B^diamond_j) > 0: no flip, and the summand of Exc' vanishes.
 * window contacts with mass, and contacts j in K: verbatim as in the note (they use only the side conditions on K).
 * j in F cap (N_w, N'']: here z'_j = s_j, a'_j = 0, beta^theta_j = 0 and beta^+-_j = +-(1/2)v_j; the summand is
   |tau rho beta^diamond_j| - s_j tau rho beta^diamond_j = 2(s_j tau rho beta^diamond_j)_-, which is 0 for theta and equals
   |tau| rho (s_j v_j)_- for diamond = sgn tau (for tau > 0: 2 tau rho ((1/2) s_j v_j)_-; for tau < 0: 2(|tau| rho (1/2) s_j v_j)_-).
 * j in F, j > N'': z'_j = 0 and the summand is |tau rho beta^diamond_j| <= (1/2) rho |tau| |v_j| (0 for theta), counted in V_{>N''}.
 * j notin F cup K: b^+-, v vanish. QED claim.
The Hilbert part is unchanged (P'^perp U*a' = 0, h'(beta^diamond) -> h(b^diamond) since beta^diamond -> b^diamond in l_1), and K_A
(the bound of (|q*(A_tau) - 1| + q*(A_tau - a'))/|tau|) is finite because ||beta^diamond||_1 <= ||b^+||_1 + ||b^-||_1.

Step 4: verbatim. Step 5: the first-order base costs are (1/2) rho|tau| V_{>N''} + rho |tau| sum_{F, j>N_w}(s_j v_j)_-
+ |tau| o(s_1) <= |tau| delta s_1/64 + |tau| delta s_1/32 + |tau| delta s_1/64 = |tau| delta s_1/16 <= delta tau^2/16 for |tau| > s_1
(at late stages, the o(s_1) term being the anchor remainder 2||Z||_1 of the note), and they are absent for diamond = theta; this is
exactly the bound "the last two terms are at most delta tau^2/16" used in Step 5 of the note. Step 6: verbatim (Lemma lem:assembly).
Hence g'_i := g' in C(f'_i) at late stages, g'_i -> rho g, f'_i norm attaining with finite base support. QED

Remark 3.4. (a) Under (R-inf) the second condition of (N0) is automatic once alpha(N_w) <= s_1^2: (s_j v_j)_- <= (s_j b^+_j)_- +
(s_j b^-_j)_+ <= 2C_R|a_j|, so sum_{F, j > N_w}(s_j v_j)_- <= 2 C_R s_1^2.
(b) Only the anti-sign directions enter (R-inf): a support coordinate used by the + piece in the direction of sgn a_j (or by the - piece in
the opposite direction) never flips, however large the usage. This is the exact one-sided structure of cushions (Lemma 2.7).
(c) The approximants keep the cushions F cap [1, N_w] and turn the far support into contacts with the same signs; the far switching is
charged at first order, which is affordable because it is o(s_1) by (N0). This is the mechanism a reduction "infinite F -> finite F"
must use: support coordinates beyond the window are contacts at the approximant, so only switching that is s-signed up to an
allowance proportional to |a_j| (cushion-compatible) can be transported.
