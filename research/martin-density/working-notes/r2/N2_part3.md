# N2 part 3: exact two-piece mates with Delta d != 0 (the E_referee d-coefficient issue and the C_referee kink class)

Setting of parts 1-2: single active block m_0 (drop the index), Delta d := Delta d_{m_0} != 0, v = ell - Delta d R*w, ell = R*Delta omega.
The construction of Theorem 1 (window masses, far pulls, tuning mass, target g'_n := b'_0 + sum R*(omega_theta - d'(omega_theta) w')) is
kept; what changes is the block part of the one-sided decompositions and the tuning condition.

## 3.1 Lemma (general mismatch identity). PROVED.
Let f' be any NA approximant as in Theorem 1 with supp Delta omega in Q', let theta in [0,1], c+, c- real, and put
  Omega'+- := omega+- - d'(omega+-) w' + c+- (w' - w)   (block m_0; other blocks as in Theorem 1),
  b'+- := g' - L*Omega'+-  (so that g' = b'+- + L*Omega'+- exactly). Then, with Delta d' := d'(Delta omega) = ell(x')/|R x'|:
  b'+ = b'_0 + theta v + theta (Delta d - Delta d') R*w' - (theta Delta d + c+) R*(w' - w),
  b'- = b'_0 - (1-theta) v - (1-theta)(Delta d - Delta d') R*w' + ((1-theta) Delta d - c-) R*(w' - w),
and b'+-(x') = -c+- Bx,   Bx := <w' - w, R x'> = |R x'| - <w, R x'> >= 0  (the Bregman excess of w at R x').
Moreover ell(x') - Delta d |R x'| = v(x') - Delta d Bx, so the tuning condition Delta d' = Delta d is psi~(x') := v(x') - Delta d Bx = 0.
*Proof.* Algebra: L*(omega_theta - omega+) = theta ell, d'(omega_theta) - d'(omega+) = theta Delta d', ell = v + Delta d R*w, and
R*w = R*w' - R*(w' - w); similarly for the minus side. b'+-(x') = g'(x') - <Omega'+-, L x'> with g'(x') = 0 and
<omega - d'(omega) w', R x'> = 0 (A Lemma 4.2 at f'), <w', R x'> = |R x'|. The last identity: ell(x') = v(x') + Delta d <w, R x'>. QED.
Consequences. To make both mismatch terms vanish one needs Delta d' = Delta d and c+ = -theta Delta d, c- = (1-theta) Delta d. Then
b'+ = b'_0 + theta v and b'- = b'_0 - (1-theta) v exactly as in Theorem 1, but the base first-order terms are
tau rho theta Delta d Bx (side +) and -tau rho (1-theta) Delta d Bx (side -), and the block parts contain c+-(w' - w).

## 3.2 Lemma (the block convexity mechanism works iff tau c <= 0). PROVED.
(a) If tau c <= 0 then, with s := -tau rho c in [0, 1/2], N(w' + tau rho(omega - d'w') + tau rho c (w' - w)) <= 1 + (tau^2 rho^2/(2(1-s))) H'(omega)(1 + ...)
    (Lemma 1.3 with y = w, N(w) = 1). No first-order cost at all.
(b) If s := -tau rho c < 0 and w' has a peak k outside supp omega with w(k) = -(M/M') w'(k) (a common peak with opposite sign), then
    N(W) >= 1 + 2 M |s|,  W := w' + tau rho (omega - d' w') + s (w - w').
*Proof of (b).* At k: sigma' W(k) = (1 - tau rho d' - s) M' + s sigma' w(k) = (1 - tau rho d') M' + |s| (M' + M). By Cauchy-Schwarz
||D W|| >= <D W, D w'>/C' = (1 - tau rho d' - s) C' + tau rho d' + s <Dw, Dw'>/C' >= (1 - tau rho d') C' + tau rho d' + |s| C' - |s| C
(<Dw, Dw'> <= C C'). Adding: N(W) >= |W(k)| + ||DW|| >= (1 - tau rho d')(M' + C') + tau rho d' + |s|(M' + M + C' - C) = 1 + |s|(1 + M - C) = 1 + 2M|s|. QED.

## 3.3 Lemma (common peaks of opposite sign are unavoidable). PROVED.
Let f in S_{p*} be NOT norm attaining and f' in S_{p*} norm attaining (normer in c_0). Then in every block m there are infinitely many k
which are peaks of both w_m and w'_m, with w'_m(k) w_m(k) < 0.
*Proof.* zhat is not in c_0 and xhat' is in c_0 \ {0}, so they are linearly independent elements of l_inf = (l_1)*; hence y -> (y(zhat), y(xhat'))
maps l_1 onto R^2, and there is y in S_{q*} with y(zhat) =: 2 delta > 0 > -2 delta' := y(xhat'). By (T2) the tail of (u_{k,m})_k is dense in
S_{q*}: infinitely many k satisfy q*(u_{k,m} - y) < min(delta, delta'), so u_{k,m}(zhat) > delta and u_{k,m}(xhat') < -delta' (q**(zhat) = 1 =
q(xhat')). By Fact C (k is a peak as soon as |u_{k,m}(xi)| > theta_m Phi_m(k), theta_m := M_m |zeta_m|/(m C_m), and Phi_m(k) -> 0), all but finitely
many of these k are peaks of w_m with sign + and of w'_m with sign -. QED.

## 3.4 Corollary (Delta d < 0: one side cannot use the convexity mechanism). PROVED.
If Delta d < 0, no choice of theta in [0,1] makes both c+ = -theta Delta d <= 0 and c- = (1 - theta) Delta d >= 0. For any choice, on the
side where tau c > 0 the block part of the exact-mismatch-free decomposition of 3.1 has N(W) >= 1 + 2M |tau| rho |c| (3.2(b), 3.3: the
common opposite peaks are fine coordinates, outside supp omega), a first-order excess that exceeds the slack s(tau) - s(rho tau) <= (1-rho^2)tau^2/2
for all |tau| < 4M|c|/(1-rho^2)... i.e. at every small scale. Hence for Delta d < 0 the mismatch Delta d R*(w' - w) must be put into the base on
at least one side (theta = 0: side -, c- := 0), where it costs the KINK of Delta d R*(w' - w) at f' (Lemma 1.4).
This makes precise why E_referee's repair covers exactly Delta d >= 0.

## 3.5 Theorem 2 (Delta d > 0). PROVED under (BR); (BR) PROVED under two-sided mass tuning.
Let f, g be as in Theorem 1 but with Delta d > 0. Suppose
 (BR) the engineered approximants of Theorem 1 can be chosen with Bx_n := |R x'_n| - <w, R x'_n> = o(t_n) (t_n the window-mass scale).
Then g is in Ls(f). (BR) holds in particular under
 (TT) two-sided mass tuning: c_j != 0 for some j in F, or z_j c_j takes both signs on K (c_j := <P_{e-perp} U*v, U*e_j*>).
*Proof.* Use Lemma 3.1 with c+ = -theta Delta d, c- = (1-theta) Delta d and tune psi~ = v - Delta d Bx to 0 (Step 2 of Theorem 1 with psi_n
replaced by psi~_n; this is possible because d/dmu Bx(x'_n(mu)) = <J(R x'_n(mu)) - w, R U dE/dmu> -> 0 uniformly for mu in [0, mubar_n] (J is
norm-to-weak* continuous at R**zhat, dE/dmu ranges in a norm-compact set), so psi~_n still has derivative >= c_+/(4 nu), and Bx_n(0) -> 0).
Then b'+ = b'_0 + theta v, b'- = b'_0 - (1-theta) v, and the base first-order terms are rho |tau| (theta or 1-theta) Delta d Bx_n, which by
(BR) is <= (1-rho^2) tau^2/32 for |tau| >= t_n, n large. Block parts: Lemma 3.2(a) (tau c+- <= 0 on both sides; s <= T_0 rho Delta d <= 1/2 by
the choice of T_0). Everything else is Steps 3-8 of Theorem 1 verbatim (Lemma 1.4 with B(xhat') != 0 adds tau B(xhat') to the bound).
(TT) => (BR): with (TT) the tuning mass can move psi~ in both directions, so Far_n := empty (Remark 2.4) and the only far modification is
z'_n = 0 beyond N''_n. Then, by convexity of |.| (|R**zhat| >= |R x'| + <w', R**zhat - R x'>),
  Bx_n <= <w'_n - w, R(x'_n - zhat)> <= ||U|| ||E_n - e|| sum_k lambda_k |w'_n(k) - w(k)| + 2 theta_{N''_n},
θ_N := sum_k lambda_k ||u_k 1_{(N,inf)}||_1. Here ||E_n - e|| = O(t_n + mu_n) = O(t_n) (deficit O(t_n), no pulls), sum_k lambda_k |w'_n(k) - w(k)| -> 0
(dominated convergence, Lemma 1.5), and N''_n is chosen after t_n with theta_{N''_n} <= t_n^2. So Bx_n = o(t_n). QED.
Without (TT) the far pulls contribute <w' - w, R(z'_n - z) 1_{Far_n}> to Bx_n, i.e. at most 2 sum_k lambda_k |w'_n(k) - w(k)| |u_k|(Far_n), to be
compared with t_n ~ sum_{Far_n} |v_j|: a comparison between the far tails of v and of the other block vectors (T-dependent; it holds e.g.
for P1-type T, where the only block vectors with mass on K' far out are v-multiples and very fine targets). Status: SKETCH.

## 3.6 Theorem 3 (Delta d < 0). PROVED conditionally on (PC).
Let f, g be as in Theorem 1 but with Delta d < 0. Take theta := 0 and c+ = c- := 0; tune psi~ = v + |Delta d| Bx to 0 (as in 3.5). Then
side + is the certificate itself (b'+ = b'_0), and side - is b'- = b'_0 - v + E'_n with E'_n := Delta d R*(w'_n - w) and b'-(x'_n) = 0.
Suppose
 (PC) sum_{j in G_n} |E'_{n,j}| = o(t_n), where G_n := (complement of supp a'_n) cup {j in supp a'_n : 2 T_0 rho |E'_{n,j}| > |a'_{n,j}|}.
Then g is in Ls(f).
*Proof.* As Theorem 1; on side - (tau < 0) Lemma 1.4 gives the extra first-order term kink'_tau(rho E'_n) <= 2 |tau| rho sum_{G_n} |E'_{n,j}|
(on supp a'_n \ G_n there is no sign change), which is <= (1-rho^2) tau^2/32 for |tau| >= t_n, n large; h'(b'-) -> h(b-) since ||E'_n||_1 -> 0
(Lemma 1.5: R*w'_n -> R*w). QED.
Remarks. (1) Absorbing masses. One may add to a'_n masses of sign z'_j on any contact and on far free coordinates (setting z'_j = +-1 there,
which is allowed beyond a level N_0 -> infinity): then G_n shrinks to the NEAR FREE coordinates J cap [1, N_0] plus the tail beyond N''_n, but
E'_n depends on these masses (they move e'). So (PC) is a genuine fixed-point/pinning requirement: the approximants must keep
R*(w'_n - w) small on the near free coordinates at the precision o(t_n), where t_n is the very scale of the window masses that perturb e'.
(2) Why the requirement is scale-invariant (and therefore not automatic): the window masses move e' by ~ t_n, hence R x' by ~ t_n near the
coarse coordinates, hence w' at off-peak coordinates with Phi >= t_n by ~ t_n/Phi, hence R*(w' - w) by ~ t_n per off-peak coordinate of
scale >= t_n (A_referee 5.5, E_referee 2.7). Enlarging the masses enlarges t_n and the perturbation in the same proportion.

## 3.7 Proposition (cases where (PC) holds). SKETCH.
(a) Block-tame carrier block with robust peaks. Suppose Q_{m_0} = {k_0} (only one strict non-peak in the carrier block), no degenerate peaks,
margin sparsity (MS): sum{lambda_k : k in P_{m_0}, mu_k < s} = o(s), and (TT). Then for block m_0 the "pinning conditions" reduce to the single
tuned scalar: writing R*w = lambda_0 w(k_0) u_{k_0} + M pi, pi := sum_{k in P} sigma_k lambda_k u_k, one has
  v(x') = Delta d M pi(zhat) [ u_{k_0}(x')/u_{k_0}(zhat) - pi(x')/pi(zhat) ]   (exact; uses v(zhat) = 0, u_{k_0}(zhat) != 0 since Delta d != 0),
and, by the converse of Fact C (zeta' = c'(alpha' + D^2 w/C) with alpha' >= 0 on P, ||alpha'||_1 = 1 implies J(zeta') = w), the conditions
"ratio at k_0 = ratio of the peak sum" and "every peak of w stays above the old threshold at x'" give w'_{m_0} = w_{m_0} EXACTLY. So after
tuning v(x'_n) ~ 0, w'_n - w is generated only by the coordinates whose threshold condition fails: near perturbations of size O(t_n) flip
only peaks with margin O(t_n) (total lambda-mass o(t_n) by (MS)), the far modification beyond N''_n flips a lambda-mass that tends to 0
as N''_n -> infinity (no degenerate peaks) and can be made o(t_n). A perturbation estimate for J (the global data M', C', zeta'(k_0) react to
the flipped coordinates only through quantities bounded by their lambda-mass) then gives ||E'_n||_1 = o(t_n), hence (PC).
The perturbation estimate for J at flipped coordinates is the step not written in full (hence SKETCH).
(b) Without (TT) the far pulls flip peaks with ||u_k 1_{Far_n}|| >~ mu_k; (PC) then needs sum{lambda_k : mu_k <= 2 ||u_k 1_{Far_n}||_1} = o(sum_{Far_n} |v_j|),
a comparison of far tails (T-dependent; true for P1-type T).
(c) Infinitely many strict non-peaks in the carrier block (the generic case of Preprint A): pinning needs ~ log(1/t_n) conditions (one per
off-peak coordinate of scale >= t_n) solved by tuning variables with condition numbers that must be o(1/t_n) relative to t_n: a
QUANTITATIVE TAIL-INDEPENDENCE property of T at f. Neither proved nor refuted. OPEN.

## 3.8 Existence of Delta d < 0 mates (so 3.6 is not vacuous). SKETCH.
In P1's construction (P1 2.1) replace the special vector by u_{2,1} := (h - kappa' pi)/n, where h is supported on {1} cup K', z-signed on K',
h(zhat) = 0, pi := sum_{(k,1) != (2,1)} sigma_k lambda_{k,1} u_{k,1} (signs sigma fixed by the robust-peak design, which does not involve u_{2,1}),
and kappa' is small. With all block-1 coordinates except (2,1) peaks, R_1*w_1 = lambda_0 w_1(2) u + M_1 pi, and a direct computation gives
for c u: v = c u - (c u(xi)/|zeta_1|) R_1*w_1 = (c M_1 pi(xi)/(n |zeta_1|)) h (the pi-coefficient is -(c M_1/(n |zeta_1|)) h(xi) = 0), so v is
supported on {1} cup K', z-signed: an exact resonance with Delta d = c u(xi)/|zeta_1| = -c kappa' pi(xi)/(n |zeta_1|), negative for c kappa' > 0.
(2,1) stays a strict non-peak for kappa' small (|u(xi)| below the threshold). Injectivity / Y cap c_00 = {0} follow as in P1 2.1 (h carries a
signature on S_{l_0}). The two-piece mates g_{K_1} are then constructed as in P1 2.3 (second-order coefficients small for c small).

## 3.9 The kink class of C_referee 1.20 (infinitely many kinks). PROVED identification + consequences.
By 1.6, a one-sided first-order re-split through kinks is an exact two-piece representation with Delta d = -(s+ - s-) c'/M. Hence:
 * if the re-splitting block vector v'' has c' < 0 (Delta d > 0): recovered by Theorem 2 under (TT) (or (BR));
 * if c' > 0 (Delta d < 0): recovered by Theorem 3 under (PC); in the C_referee configuration J is FINITE (K cofinite), so the near free
   coordinates form a fixed finite set and (PC) is a finite set of pinning conditions (|J| scalars) plus absorbing masses on contacts:
   SKETCH-level plausible, not proved;
 * if c' = 0 (no peak component; Delta d = 0): recovered by Theorem 1.
In all cases the mate must ALSO satisfy kappa <= 1 for its re-split decompositions (that is how it is a mate when Gamma_w > 1).
So "supports with infinitely many kinks" do not create a new mechanism: they are exact resonances, and the open part is exactly the
Delta d < 0 pinning problem.

## 3.10 Summary for exact resonances
| class | status |
|---|---|
| exact two-piece, Delta d = 0, one active block | recovered along engineered NA sequences: PROVED (Thm 1) |
| several active blocks, all Delta d_m = 0 | PROVED under a rank condition (Remark 2.6, SKETCH of the tuning step) |
| Delta d > 0, two-sided mass tuning (TT) | PROVED (Thm 2) |
| Delta d > 0 without (TT) | PROVED under (BR); (BR) is a far-tail comparison (SKETCH, T-dependent) |
| Delta d < 0 | PROVED under (PC) (Thm 3); the convexity mechanism provably fails on one side (3.4); (PC) SKETCH in block-tame robust cases (3.7a), OPEN in general (needs quantitative tail independence, 3.7c) |
| C_referee kinks | = exact resonances with Delta d = -(s+ - s-)c'/M (3.9): covered by the rows above |
