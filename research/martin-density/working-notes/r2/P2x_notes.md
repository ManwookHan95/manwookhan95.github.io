# P2 notes — engineered recovery of switching mates with one-sided resources (replication–averaging–transfer)

Round 2, task P2. Setting: canonical base q, Martín's norm with a FINITE block set I (p_N, any N; Remark martin-tail of Preprint B reduces p to
these); notation of A_notes §1, §4. Only Lemma B's conclusion is used about T. Imports (refereed): (T1)-(T4), A Facts A-F, A Lemmas 4.3, 4.4, 4.7,
7.1, 7.2, A Prop 4.5, A Thm 4.10/4.17/6.8, G_referee 4.7 (parametrization of NA approximants), N_part1 Thm 1 (g in Ls(f) iff (f, rho g) in cl NA for all rho<1).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

**Provenance (important).** Two P2 agents ran concurrently and wrote to the same directory. The file P2_part1.md (toolkit) and the files
P2_part2.md, P2_part3.md (d-neutral theorem, mixed term, garbage identity) are by the OTHER instance; my files are P2x_part2..5.md. This notes
file assembles my results in full (Sections 2-5) and summarises the other instance's main theorem (Section 6, with the step I re-checked); Section 7 answers the task's specific questions.
If a later P2_notes.md from the other instance replaces this file, my results remain in P2x_part2-5.md and P2x_notes.md (identical copy).

## 0. Summary

**Answer.** The one-sided-resource mates whose decompositions near t = 0 use only ROBUST structure — base contacts (with any splitting of the
contact mass between the two sides, contacts on both sides), near-contacts, finitely many FIXED off-peak block carriers (also pushed beyond their
gap at fixed scales) — are recovered along engineered NA approximants, by a three-regime scheme in which regime (ii) is an EXACT transfer of the
one-sided decompositions of f, regime (i) is one two-sided certificate created by window masses on the contacts, and regime (iii) is the slack.
Rigorous: two-piece mates with Delta d_m >= 0 in every block under a cone tuning condition (Theorem 3.5, several blocks); d-neutral two-piece
mates without any tuning condition for one block (other instance's Theorem, pulls). The obstruction is NOT the base mixed term (it is cancelled
by finitely many scalar tunings) but the BLOCK side: x -> J_V(Lx) moves off-peak values by ~ s/Phi_k under an O(s) change of the normer, which is
harmless for fixed carriers (only a Bregman pairing, o(s), enters at first order — new Lemma 2.3) and fatal, for every mass/conversion-based scheme,
for SCALE-DEPENDENT block carriers (weak peaks, super-near-threshold carriers, deep off-peak carriers) in the band [s, sqrt(s)] (Prop 5.4). C's implant
scale gap is confirmed quantitatively (conversion cost identity 5.3) but is not an obstruction to the scheme. Density remains OPEN; no
counterexample is claimed. The exact residual class is listed in 5.6.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Three-regime theorem (abstract replication–averaging–transfer; averaging over J geometric scales with error 4 kappa t^2/(2J)) | PROVED | 1.4, 1.5, 5.1 |
| 2 | Clip formula w(k) = M clip(u_k(y)/(theta Phi_k)); Bregman identity | PROVED | 2.1, 2.2 |
| 3 | Bregman smallness: excess of w at the perturbed point is o(A) (A = normer perturbation), although sum lambda_k|w'(k) - w(k)| = Theta(A) | PROVED (+numerics) | 2.3, 2.4 |
| 4 | Base mixed term delta t <P^perp U*e_j, P^perp U*B_t>/nu: exact form; cancelled by finitely many tunings (finitely many pieces) or up to eta (any bounded family, compactness of U*); NOT an obstruction | PROVED | 2.5, 2.6 |
| 5 | Uniform Hilbert remainders; block uniformity along engineered approximants | PROVED | 3.1, 3.2 |
| 6 | Brouwer tuning lemma for positively spanning moves | PROVED | 3.3 |
| 7 | **Main theorem: two-piece switching mates (any contact split, several blocks), Delta d_m >= 0 for all m, a in c_00, cone condition (TC): (f,g) in cl NA** | PROVED | 3.5 |
| 8 | Delta d_m < 0: convexity provably fails on one side; recovery iff pinning (PIN); pinning at block-tame blocks with robust window peaks | PROVED (failure) / SKETCH (pinning) | 4.1 |
| 9 | (TC) fails: far pulls; exact tuning unnecessary (approximate tuning to eps_0 s_1 suffices: removes the j* issue of P1 6.3) | SKETCH (one block, Delta d = 0: PROVED by the other instance / N2) | 4.2, 6 |
| 10 | a not in c_00; infinitely supported carriers with near-peak decay; degenerate-peak carriers | SKETCH | 4.3, 4.4 |
| 11 | Conversion cost identity (implant scale gap): a two-sided carrier of capacity t_cap created at a peak costs >= 2|c| t_cap in f' - f (absent cancellations) | PROVED (identity) / HEURISTIC (as obstruction) | 5.3 |
| 12 | Precision obstruction: scale-dependent block carriers cannot be transferred across [s, sqrt(s/eps_0)] by any mass/conversion scheme at scale s; averaging does not help | PROVED (for transferred decompositions) / HEURISTIC (as obstruction to recovery) | 5.4 |
| 13 | Classification of where regime (i) can be supplied; exact residual class (R1)-(R4) | PROVED classification of mechanisms / OPEN residual | 5.5, 5.6 |
| 14 | d-neutral two-piece mates (one block, no tuning hypothesis; several blocks under a span hypothesis (S)) — other instance | PROVED there (key step re-checked) | 6 |
| 15 | P1's explicit defect mates (P1 2.3, 6.2): recovered | PROVED (Thm 3.5 if (TC); otherwise other instance's theorem) | 3.6(4), 6 |
| 16 | Density of NA((c_0,p_N), l_2^2) | OPEN | 5.6 |

## 1. Toolkit (from P2_part1.md, re-checked; statements only, proofs there)
1.1 Clamp formula (= 2.1 below). 1.2 Convergence of block data along engineered approximants: if xhat_n = z'_n + U e_n -> zhat weak* and a_n -> a in l_1
with a_n(xhat_n) = 1 = q(xhat_n), then f_n := grad p(xhat_n) -> f in norm, w_{n,m}(k) -> w_m(k), C_{n,m} -> C_m, M_{n,m} -> M_m, D_m w_{n,m} -> D_m w_m in l_2,
R_m* w_{n,m} -> R_m* w_m in l_1 (G_referee 4.7). 1.3 At an NA point with g'(xhat') = 0 and block parts omega - d'w' (omega off-peak), the base part B has
B(xhat') = 0 and q*(a' + tau B) = 1 + Fl' + Kink' + nu'Psi'. 1.4 Assembly: if p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta) on 0 < |tau| <= T_0 with T_0^2 <= 3delta,
p*(f' - f) <= (1-rho^2)T_0^2/6 and p*(g' - rho g) <= (1-rho^2)T_0/6, then g' in C(f') (proof: 1 + x/2 - x^2/8 <= sqrt(1+x); A Lemma 4.7 slack).
1.5 Averaging: with s_j = s_1 2^{1-j}, (i) p*(f' + t h_j) <= 1 + Qt^2/2 on |t| <= s_j, (ii) p*(f' + t gbar) <= 1 + Qt^2/2 on [s_J, T_0], (iii) p*(h_j - gbar) <= kappa s_j imply
p*(f' + t g') <= 1 + (Q + 4kappa/J)t^2/2 on |t| <= T_0 for g' = (1/J) sum h_j (convexity; sum_{s_j < |t|} s_j <= 2|t|). 1.6 Two-piece data: b+-, omega+-_m (finitely
supported, off-peak), d+-_m = <D w_m, D omega+-_m>/C_m, g = b+ + sum R_m*(omega+_m - d+_m w_m) = b- + sum R_m*(omega-_m - d-_m w_m), supp b+- in F u K,
z_j b+_j >= 0 >= z_j b-_j on K; omega_Delta := omega- - omega+, Delta d_m := d-_m - d+_m, v := b+ - b- = sum_m R_m*(omega_Delta,m - Delta d_m w_m); b+-(zhat) = 0.
1.7 One-sided admissibility (with s(tau)) implies all second-order coefficients <= 1.

# 2. first-order bookkeeping — the Bregman lemma (blocks) and the mixed term (base)

For a block m (index dropped) and y in l_infinity with R** y != 0 put zeta_y := R** y (zeta_y(k) = lambda_k u_k(y)), w_y := J(zeta_y), M_y, C_y,
  theta_y := M_y |zeta_y| / (m C_y)   (k is a peak of w_y iff |u_k(y)| >= theta_y Phi_k).
Block data are 0-homogeneous in y, so we compare y = zhat (data of f) with y' = xhat' = x'/q(x') (data of f') directly.

## 2.1 Lemma (clip formula). PROVED.
w_y(k) = M_y clip( u_k(y)/(theta_y Phi_k) ),  clip(s) := max(-1, min(1, s)).
*Proof.* P2_part1 Lemma 1.1: w(k) = sgn(zeta(k)) min(M, C r(k)), C r(k) = C m|u_k(y)|/(Phi_k|zeta|) = M|u_k(y)|/(theta Phi_k). QED.

## 2.2 Lemma (Bregman identity). PROVED.
e(y; y') := 1 - <w_y, zeta_{y'}>/|zeta_{y'}| >= 0 (excess of the old functional at the new point). Then
  |zeta_{y'}| e(y;y') + |zeta_y| e(y';y) = <w_{y'} - w_y, zeta_{y'} - zeta_y>.
Exact form: e(y;y') = sum_{k in P'} |alpha'_k| (M_y - sigma'_k w_y(k)) + (C_y C_{y'} - <D w_y, D w_{y'}>)/C_{y'} (both terms >= 0).
*Proof.* <w_y, zeta_y> = |zeta_y|, <w_{y'}, zeta_{y'}> = |zeta_{y'}|; expand. The exact form: Fact C at y', ||alpha'||_1 = 1, M + C = 1. QED.

## 2.3 Proposition (Bregman smallness). PROVED.
Let Delta_k := |u_k(y') - u_k(y)| <= A + t_k (A, t_k >= 0), Lambda := sum lambda_k, T := sum lambda_k t_k,
gamma := |M_{y'} - M_y| + M_y |theta_y/theta_{y'} - 1|, eps(s) := sum_k min(lambda_k, m s) (-> 0 as s -> 0). Then
 (a) |w_{y'}(k) - w_y(k)| <= gamma + M_y min(2, Delta_k/(theta_{y'} Phi_k)) for every k;
 (b) <w_{y'} - w_y, zeta_{y'} - zeta_y> <= gamma(A Lambda + T) + 4 M_y A eps(A/theta_{y'}) + 4 M_y T;
 (c) e(y;y') <= [gamma(A Lambda + T) + 4 M_y A eps(A/theta_{y'}) + 4 M_y T]/|zeta_{y'}|.
Hence along families with A -> 0, T = o(A), y' -> y weak* (gamma -> 0, theta_{y'} -> theta_y > 0): e(y;y') = o(A).
*Proof.* (a) clip is 1-Lipschitz and |clip(rs) - clip(s)| <= |r - 1| (r > 0). With s = u_k(y)/(theta Phi_k), s' = u_k(y')/(theta' Phi_k), s~ = u_k(y)/(theta' Phi_k):
|w'(k) - w(k)| <= |M'-M| + M(|clip(s') - clip(s~)| + |clip(s~) - clip(s)|) <= |M'-M| + M min(2, Delta_k/(theta' Phi_k)) + M|theta/theta' - 1|.
(b) The pairing is <= sum_k |w'(k) - w(k)| lambda_k Delta_k. gamma-part <= gamma(A Lambda + T). Rest: lambda_k Delta_k min(2, Delta_k/(theta' Phi_k)) <=
min(2 lambda_k Delta_k, m Delta_k^2/theta'); if t_k <= A it is <= 4A min(lambda_k, mA/theta'), else <= 4 lambda_k t_k. (c) Lemma 2.2 and e(y';y) >= 0. QED.
Remark. Only the Bregman pairing is o(A). The displacement sum_k lambda_k |w'(k) - w(k)| is in general Theta(A): each off-peak coordinate with
Phi_k >~ A moves by ~ A/Phi_k (from (a), and sharp when u_k(y') - u_k(y) ~ A). This is why d-mismatches cannot simply be put in the base
(A_referee 5.5, E_referee 3.1, N2 3.6).
Numerical check (P2work/bregman.py; one block, n = 60, Phi_k = 2^{-k}U(0.3,1), 17 off-peak coordinates, J by nested 1-D optimisation; random
|u_k(y') - u_k(y)| <= A):  A = 1e-2, 3e-3, 1e-3, 3e-4, 1e-4:  max e/A = 0.11, 0.046, 0.011, 0.0027, 0.00097 (e = O(A^2) here) while
sum lambda|dw|/A = 2.3, 3.5, 3.3, 2.6, 2.9 (Theta(A)).

## 2.4 Lemma (displacements at an engineered approximant). PROVED.
If x' = z' + U e' with z' = z on [1,N] except at finitely many window FREE coordinates j (|z_j| < 1, j notin F) moved by eta_j, and |z'| <= 1 beyond N, then
  Delta_k <= ||U|| ||e' - e|| + sum_j eta_j |u_k(j)| + 2 ||u_k 1_(N,inf)||_1;
so 2.3 applies with A := ||U|| ||e'-e|| + sum_j eta_j, t_k := 2||u_k 1_(N,inf)||_1, T = T_N := 2 sum_{k,m} lambda_{k,m} ||u_{k,m} 1_(N,inf)||_1 -> 0.
If a' = (a + Delta)/q*(a + Delta), ||U*Delta|| <= nu/2, then ||e' - e|| <= 2||U*Delta||/nu.
*Proof.* u_k(x') - u_k(zhat) = u_k(z' - z) + <U*u_k, e' - e>, ||U*u_k|| <= ||U||; ||x/||x|| - y/||y|| || <= 2||x-y||/||y||. QED.
Consequence: masses and tuning moves O(s_1), N chosen after s_1 with T_N <= s_1^2  ==>  e_m(zhat; xhat') = o(s_1) for every block.

## 2.5 Lemma (the base mixed term, exact form). PROVED.
For b in l_1 with b(zhat) = 0: b(xhat') = b(z' - z) + <U*b, e' - e>, and if a' = (a+Delta)/q*(a+Delta), ||U*Delta|| <= nu/2:
  | <U*b, e' - e> - <P_{e-perp}U*b, U*Delta>/nu | <= 6 ||U*b|| ||U*Delta||^2/nu^2.
*Proof.* h := U*Delta/nu, e' = (e+h)/||e+h||; the map h -> (e+h)/||e+h|| has derivative P_{e-perp} at 0 and second derivative <= 12 on ||h|| <= 1/2
(||e + h|| >= 1/2), so ||e' - e - P_{e-perp}h|| <= 6||h||^2. QED.
A tiny contact mass delta at j (Delta = delta z_j e_j*) thus changes the first-order coefficient of a base part b by delta z_j <P_{e-perp}U*b, U*e_j*>/nu + O(delta^2):
this is the "mixed second-order term" delta t <P^perp U*e_j, P^perp U*B_t>/||U*a|| of the task (times t from tau b(xhat')).

## 2.6 Proposition (when the base mixed term is harmless). PROVED.
Let {B_tau} (tau in a set S of scales) be the base parts to be transferred, B_tau(zhat) = 0, sup ||B_tau||_1 < inf. Use at f' the base parts
B'_tau := B_tau - b_0(xhat') a' with ONE reference b_0 (so the represented direction is unchanged). The first-order term of a' + tau B'_tau is
tau (B_tau - b_0)(xhat') = tau (B_tau - b_0)(z' - z) + tau <U*(B_tau - b_0), e' - e>, and
 (a) finitely many pieces b_0..b_r: all first-order terms vanish iff the r scalar conditions (b_i - b_0)(xhat') = 0 hold (tuning);
 (b) any bounded family: {U*(B_tau - b_0)} is relatively compact (U* compact); with E_eta finite-dimensional, dist(U*(B_tau - b_0), E_eta) <= eta, tuning
     e' - e orthogonal to E_eta (dim E_eta conditions) leaves a U-part <= eta||e'-e|||tau| = O(eta s_1|tau|) <= eps_0 tau^2 on |tau| >= s_1 if eta <= eps_0/C;
     the z-part vanishes on the window (z' = z there except at tuning coordinates not charged by the B_tau) and beyond it is a tail.
*Proof.* Linearity, compactness, Cauchy-Schwarz. QED.
**Verdict (task question).** The base mixed term is NOT an obstruction: it is the variation of first-order coefficients, linear in the masses, and is
cancelled exactly (finitely many pieces) or up to eta (compact families) by finitely many scalar tunings, provided tuning moves with two-sided
(positively spanning) effects exist (P2x_part3 3.4). For two-piece data it reduces to the single condition per active block Delta d'_m = Delta d_m,
whose residue is exactly the Bregman excess (P2x_part3 Step 3). The obstructive mismatch is on the BLOCK side (Remark after 2.3).

# 3. main theorem — engineered recovery of two-piece switching mates with Delta d_m >= 0 (several blocks)

Setting: finite I (p_N), f in S_{p*}, F = supp a FINITE; two-piece data as in P2_part1 1.6; G(s;A,B) := ||A + sB|| - ||A|| - s<A/||A||, B>.
Relation: A_referee 5.4 (SKETCH, Delta d = 0), P1 6.3 (SKETCH), N2_part2/3 (parallel, unrefereed: one active block; Delta d = 0 Thm 1; Delta d > 0
under (BR)/(TT) Thm 2), P2_part2 (concurrent P2 instance: d-neutral case). Here: several blocks, any Delta d_m >= 0, a general cone condition for
tuning, and the Bregman lemma (P2x_part2 2.3) in place of (BR)/(TT).

## 3.1 Lemma (uniform Hilbert remainders). PROVED.
Let A_0 != 0, b_* > 0, s_* := ||A_0||/(4b_*). On {||A - A_0|| <= ||A_0||/4, ||B|| <= b_*, |s| <= s_*}: ||A + sB|| >= ||A_0||/2, G is smooth, G(0) = G_s(0) = 0,
G_ss(s;A,B) = (||B||^2 - <A+sB,B>^2/||A+sB||^2)/||A+sB||, derivatives of order <= 3 bounded. Hence (a) |G(s;A,B) - G(s;A_0,B_0)| <= L s^2 (||A-A_0|| + ||B-B_0||)
(Taylor with integral remainder, Lipschitz bound on G_ss), and (b) G(-s;A,B) <= G(|s|;A,B) + c_3|s|^3 (odd part). The same holds for block Hilbert parts
||P + sQ||_2 with P = D_m w_m (||P|| = C_m > 0). QED.

## 3.2 Lemma (block uniformity). PROVED.
Fix m, omega in c_00 vanishing on P_m, gamma := min_{supp omega} gap_m > 0, d := <Dw, D omega>/C; let f'_n -> f be engineered approximants (P2_part1 1.2) and
d'_n := <Dw'_n, D omega>/C'_n, W(s) := w + s(omega - dw), W'_n(s) := w'_n + s(omega - d'_n w'_n). Put s_gamma := gamma/(8(||omega||_inf + |d| + 2)).
For every eta > 0 and tau_1 with tau_1(|d| + 1) <= 1/2 there is n_0 such that for n >= n_0:
 (a) |s| <= s_gamma: N(W'_n(s)) = 1 + G(s; P'_n, Q'_n), N(W(s)) = 1 + G(s;P,Q) (P = Dw, Q = D(omega - dw), primes at f'_n), and |difference| <= eta s^2;
 (b) s_gamma <= |s| <= tau_1: N(W'_n(s)) <= N(W(s)) + eta s^2.
*Proof.* w'_n(k) -> w(k), M'_n -> M, C'_n -> C, Dw'_n -> Dw in l_2, d'_n -> d (P2_part1 1.2). For n large |w'_n(k)| <= M'_n - gamma/2 on supp omega, |d'_n| <= |d|+1.
(a) For |s| <= s_gamma and k in supp omega: |(1 - d's)w'(k) + s omega(k)| <= (1 - d's)(M' - gamma/2) + gamma/8 <= (1 - d's)M' (1 - d's >= 1/2); off supp omega
|(1 - d's)w'(k)| <= (1 - d's)M' with equality on P' != empty. So ||W'(s)||_inf = (1 - d's)M'. Hilbert part X'(s) = ||P' + sQ'||, X'(0) = C', X'_s(0) =
(<Dw', D omega> - d'C'^2)/C' = d'M'; hence N(W'(s)) = (1 - d's)M' + C' + d'M's + G(s;P',Q') = 1 + G(s;P',Q'). Same at f; Lemma 3.1(a).
(b) ||W'(s)||_inf = max((1 - d's)M', max_{supp omega}|(1 - d's)w'(k) + s omega(k)|), same at f, so sup parts differ by <= |M'-M| + tau_1|d'-d| + max_{supp omega}|w'(k) - w(k)|;
Hilbert parts by <= |C'-C| + tau_1|d'M' - dM| + |G(s;P',Q') - G(s;P,Q)|. All -> 0 uniformly; take n_0 with total <= eta s_gamma^2. QED.

## 3.3 Lemma (Brouwer tuning). PROVED.
Let c_1..c_p positively span R^n. There are K_0 and a continuous mu: R^n -> [0,inf)^p with sum_l mu_l(y)c_l = y, |mu(y)| <= K_0|y|. If Gfun is continuous on
{mu >= 0, |mu| <= r_0} with |Gfun(mu) - Gfun(0) - sum_l mu_l c_l| <= eta|mu|, eta K_0 <= 1/2, 2K_0|Gfun(0)| <= r_0, then Gfun(mu(y)) = 0 for some |y| <= 2|Gfun(0)|.
*Proof.* Write +-e_i as nonnegative combinations beta^{+-i} of the c_l; mu(y) := sum_i ((y_i)_+ beta^{+i} + (y_i)_- beta^{-i}). Psi(y) := -Gfun(0) - [Gfun(mu(y)) - Gfun(0) - y]
maps {|y| <= 2|Gfun(0)|} continuously into itself; a Brouwer fixed point satisfies Gfun(mu(y)) = 0. QED.

## 3.4 Definition (tuning moves; condition (TC)).
I_D := {m : omega_Delta,m != 0}, V_m := R_m*(omega_Delta,m - Delta d_m w_m) (sum_m V_m = v = b+ - b-). Effect vectors in R^{I_D}:
 (M1) window free coordinate j (j notin F, |z_j| < 1), move z'_j = z_j + theta: E_j := (V_m(j))_m (two-sided);
 (M2) j in F, move a_j -> a_j + theta: E'_j := (<P_{e-perp}U*V_m, U*e_j*>/nu)_m (two-sided);
 (M3) contact j in K, extra mass theta >= 0 with sign z_j: z_j E'_j (one-sided).
(TC): the convex cone generated by {+-E_j} u {+-E'_j : j in F} u {z_j E'_j : j in K} is R^{I_D} (finitely many moves suffice).

## 3.5 Theorem (engineered recovery of two-piece switching mates). PROVED.
Let f in S_{p*} with a in c_00, g in C(f), and (b+, omega+; b-, omega-) two-piece data for g with
 (H1) for some tau_0 > 0: max(q*(a + s b+), max_m N_m(w_m + s(omega+_m - d+_m w_m))) <= s(s) on [0, tau_0], and the same for (b-, omega-) on [-tau_0, 0];
 (H2) Delta d_m := d-_m - d+_m >= 0 for every m;
 (H3) (TC).
Then (f, g) is in cl NA((c_0, p_N), l_2^2): for every rho < 1 there are NA f' -> f and g' -> g with rho g' in C(f'), f' = grad p(x'), x' obtained from zhat by
window masses 2 s_1 |b+_j| z_j on the contacts of supp b+ in [1,N], O(s_1) tuning moves, and z' := 0 beyond N.
((H2) is intrinsic: g -> -g exchanges and negates the sides and leaves each Delta d_m unchanged; moving the masses to the other side does not help — the
convexity step needs the extra block term to move toward w_m (N2 Lemma 3.2), see P2x_part4 4.1.)

*Proof.* Fix rho, delta := (1 - rho^2)/2.
Step 0. Choose tau_1 in (0, tau_0/2] with: tau_1 max_F (|b+_j| + |b-_j|)/|a_j| <= 1/4; tau_1(max|d+-_m| + 1) <= 1/2; tau_1 max_m Delta d_m <= delta/8; Lemmas 3.1/3.2
applicable on |s| <= 2tau_1 (A_0 = U*a, B_0 in {U*b+, U*b-}, all omega+-_m); T_0 := tau_1/rho with T_0^2 <= 3delta. On [0, tau_1], q*(a + s b+) = 1 + G(s;U*a,U*b+)
(supp b+ in F u K, z_j b+_j >= 0 on K, no sign change on F, b+(zhat) = 0), and on [-tau_1, 0], q*(a + s b-) = 1 + G(s;U*a,U*b-). So (H1) gives
G(s;U*a,U*b+) <= s(s) - 1 on [0,tau_1], G(s;U*a,U*b-) <= s(s) - 1 on [-tau_1,0].
Step 1 (approximants). Parameters in this order: s_1 in (0, min(tau_1, s_gamma)/2] (s_gamma of Lemma 3.2 for all omega+-_m), then N, then the tuning vector mu.
K_+ := {j in K : b+_j != 0}; Delta^0 := sum_{j in K_+ cap [1,N]} 2 s_1 |b+_j| z_j e_j* (||Delta^0||_1 <= 2 s_1 ||b+||_1); for mu >= 0 (coefficients of finitely many moves
c_l of (TC)): a'(mu) := (a + Delta^0 + Delta^tune(mu))/q*(.), z'(mu) := z on [1,N] except (M1)-moved coordinates, 0 on (N,inf); x'(mu) := z'(mu) + U e'(mu);
f'(mu) := grad p(x'(mu)): NA with q(x') = 1 = a'(x') (A Fact D; |z'| <= 1, z' = sign a' on supp a').
Step 2 (tuning). Gfun_m(mu) := (R_m*omega_Delta,m)(x'(mu)) - Delta d_m |R_m x'(mu)|_m (m in I_D). For parameters late in the sequence supp omega_Delta,m is off-peak at x'
(finitely many coordinates, gaps converge), and then Gfun_m = 0 iff Delta d'_m := <Dw'_m, D omega_Delta,m>/C'_m = Delta d_m (since d'(omega) = <omega, R x'>/|R x'| for
off-peak omega, A Lemma 4.2 at f').
 (i) |Gfun(0)| <= C_1(s_1 + T_N): by P2x_part2 2.4, Delta_k <= A + t_k with A <= C s_1, and |Gfun_m(0) - Gfun_m(zhat)| <= sum_k lambda_k(|omega_Delta,m(k)| + Delta d_m)Delta_k,
     Gfun_m(zhat) = 0 by definition of Delta d_m.
 (ii) mu -> Gfun(mu) is C^1: x'(mu) is C^1 into c_0, |R_m .|_m is Gateaux differentiable off 0 with norm-to-weak* continuous derivative J_m, so
     dGfun_m/dmu_l = (R_m*(omega_Delta,m - Delta d_m w'_m(mu)))(dx'/dmu_l), continuous; as s_1 -> 0, N -> inf, mu -> 0 we have w'_m(mu) -> w_m weak* and dx'/dmu_l -> e_j (M1)
     or -> U P_{e-perp}U*e_j*/nu (M2; times z_j for M3) in c_0, so the Jacobian -> (c_l) uniformly on |mu| <= r_0 (sequential argument, P2_part1 1.2).
 (iii) Lemma 3.3: mu* with |mu*| <= 2K_0 C_1(s_1 + T_N) and Delta d'_m = Delta d_m for all m in I_D.
 N is chosen (after s_1) with T_N <= s_1^2 and tail_N(b+) + tail_N(b-) <= s_1^2. f' := f'(mu*).
Step 3 (direction and decompositions at f'). beta := (b+ 1_[1,N])(x'), b'+ := b+ 1_[1,N] - beta a',
  g' := b'+ + sum_m R_m*(omega+_m - d'+_m w'_m),  Omega'+_m := omega+_m - d'+_m w'_m,  Omega'-_m := omega-_m - d'-_m w'_m + Delta d_m(w'_m - w_m),  b'- := g' - sum_m R_m*Omega'-_m.
 Since Delta d'_m = Delta d_m: Omega'-_m - Omega'+_m = omega_Delta,m - Delta d_m w_m, hence b'+ - b'- = v = b+ - b- and b'- = b- - b+ 1_(N,inf) - beta a'.
 First-order terms: b'+(x') = 0; g'(x') = 0 (<omega - d'w', R x'> = 0); b'-(x') = -sum_m Delta d_m <w'_m - w_m, R_m x'> = -sum_m Delta d_m |R_m x'| e_m(zhat;x') <= 0,
 and e_m = o(s_1) by P2x_part2 2.3-2.4 (A = O(s_1), T_N <= s_1^2). Also beta -> 0, g' -> g, p*(f' - f) -> 0.
Step 4 (side +, sigma in [-s_1, tau_1]). supp b'+ is in F u (K_+ cap [1,N]) in supp a'; on F no sign change; on K_+ cap [1,N], |a'_j| >= (3/2)s_1|b+_j|, z'_j = z_j = sign a'_j,
 z_j b+_j >= 0, so no sign change for sigma >= 0, and for -s_1 <= sigma < 0, |sigma b'+_j| <= s_1(|b+_j| + |beta||a'_j|) < |a'_j|. Hence
 q*(a' + sigma b'+) = 1 + sigma b'+(x') + G(sigma;U*a',U*b'+) = 1 + G(sigma;U*a',U*b'+) <= s(|sigma|) + (eta + c_3 s_1)sigma^2 (Lemma 3.1, Step 0).
 Blocks: Lemma 3.2 with omega+_m: N_m(w'_m + sigma Omega'+_m) <= s(|sigma|) + (eta + c_3 s_1)sigma^2 (for sigma < 0: 3.2(a) and 3.1(b); s_1 <= s_gamma).
Step 5 (side -, sigma in [-tau_1, -s_1/2]). b'- = b^W + t, b^W := b- 1_[1,N] - beta a', t := (b- - b+)1_(N,inf), ||t||_1 <= s_1^2. For sigma < 0 and j in K cap [1,N]:
 sigma b-_j has sign z_j = z'_j (and a'_j has that sign where a mass sits); F: no sign change. So q*(a' + sigma b^W) = 1 + sigma b^W(x') + G(sigma;U*a',U*b^W) and
   q*(a' + sigma b'-) <= 1 + G(sigma;U*a,U*b-) + eta sigma^2 + |sigma|E_1,  E_1 := sum_m Delta d_m|R_m x'|e_m + 2(1+||U||)s_1^2 = o(s_1),
 using sigma b^W(x') = sigma b'-(x') - sigma t(x') and q*(t), |t(x')| <= (1+||U||)||t||_1. For |sigma| >= s_1/2: |sigma|E_1 <= (2E_1/s_1)sigma^2 =: eta''sigma^2, eta'' -> 0.
 Blocks (convexity; Delta d_m >= 0): x := |sigma|Delta d_m <= delta/8, sigma~ := sigma/(1-x):
   w'_m + sigma Omega'-_m = (1 - x)[w'_m + sigma~(omega-_m - d'-_m w'_m)] + x w_m,
 so N_m(...) <= (1-x)N_m(w'_m + sigma~(omega-_m - d'-_m w'_m)) + x <= 1 + (1-x)(s(sigma~) - 1 + eta sigma~^2) <= 1 + (sigma^2/2)(1 + 2eta)/(1 - x)
 (Lemma 3.2 on side -, |sigma~| <= 2tau_1 <= tau_0, and (H1)).
Step 6 (assembly). sigma = rho tau. Side + covers sigma in [-s_1, tau_1], side - covers [-tau_1, -s_1/2]; for |tau| <= T_0:
   p*(f' + tau rho g') <= 1 + (rho^2 tau^2/2)(1 + 2eta + 2eta' + 2eta'')/(1 - delta/8) <= 1 + (tau^2/2)(1 - delta)
 for eta's small (rho^2 = 1 - 2delta). As T_0 is fixed and p*(f'-f), p*(rho g' - rho g) -> 0, P2_part1 Lemma 1.4 gives rho g' in C(f'); (f', rho g') is NA
 (f' attains, rho g' is a mate) and -> (f, rho g). rho -> 1: (f,g) in cl NA. QED.

## 3.6 Remarks. 
(1) No averaging is needed: one two-sided certificate (side + with window masses) on [-s_1, 0], exact one-sided decompositions on [s_1, tau_1]
    (transfer regime), slack beyond tau_1/rho.
(2) What is used about the switching part: the transfer v is carried EXACTLY at f' (fixed carriers + tuned Delta d'), the residual
    Delta d_m R_m*(w'_m - w_m) sits in the block of the side where it moves TOWARD w_m, and its first-order price in the base is the Bregman excess.
    This is the rigorous form of A_referee 5.4 (Delta d = 0) and of E_referee 3.1's repair (Delta d >= 0).
(3) The window masses move off-peak values with Phi_k >~ s_1 by ~ s_1/Phi_k (Theta(s_1) in weighted l_1), but this never enters at first order:
    the transferred decompositions use finitely many fixed carriers and d-terms computed at f'.
(4) P1's example (P1 2.3/6.2, one block, Delta d = 0, V_1 = c u_{2,1}, (M1) and (M2) void): Theorem 3.5 applies iff some contact j has
    <P_{e-perp}U*u, U*e_j*> < 0 (TC); for diagonal U it fails and far pulls are needed (N2 Thm 1; P2x_part4 4.2).

# 4. limits and extensions of Theorem 3.5 (sign of Delta d, tuning failure, a not in c_00, carriers)

Setting of P2x_part3. N2 = parallel notes ctx/r2/N2_part*.md (unrefereed); cited where they overlap.

## 4.1 Delta d_m < 0: what fails and what is needed. PROVED (failure) / conditional (recovery).
(a) Failure of the convexity mechanism (N2 Lemma 3.2(b), 3.3, Cor 3.4 — re-checked, correct): at an NA approximant f' of a non-attaining f, every
block has infinitely many common peaks k of w_m and w'_m with w'_m(k) w_m(k) < 0 (u_{k,m} close to a functional separating zhat from xhat';
(T2)). If a block part w' + s(omega - d'w') + s c (w - w')... is moved AWAY from w (s c < 0 in the notation W = w' + ... + s'(w - w'), s' < 0), the
common opposite peak k gives |W(k)| >= (1 - s d')M' + |s'|(M' + M), and Cauchy-Schwarz on the Hilbert part gives N(W) >= 1 + 2M|s'|: a first-order
excess. Since the two sides need c- - c+ = Delta d (P2x_part3 Step 3 algebra with theta-split), Delta d < 0 forces such a move on one side.
(b) Hence for Delta d_m < 0 the mismatch Delta d_m R_m*(w'_m - w_m) must be paid in the BASE on one side, at first-order price
 |sigma| |Delta d_m| Kink'(R_m*(w'_m - w_m)) (+ flips), and recovery holds as soon as (PIN) Kink-weighted ||R_m*(w'_m - w_m)||_1 = o(s_1) at the tuned
approximants (proof: Steps 3-6 of Theorem 3.5 with Omega'-_m := omega-_m - d'-_m w'_m and the extra base term; = N2 Thm 3 under its (PC)).
(c) (PIN) is a genuine requirement: P2x_part2 Remark after 2.3 — the window masses move every off-peak value with Phi_k >~ s_1 by ~ s_1/Phi_k, so
sum_k lambda_k |w'(k) - w(k)| = Theta(s_1 * #{off-peak k : Phi_k >~ s_1}) unless the off-peak values are PINNED.
(d) Pinning at block-tame robust blocks. SKETCH. Let Q_m (strict non-peaks of w_m) be finite, every peak of w_m robust in the window
(margin mu_k := |u_k(zhat)| - theta Phi_k >= C s_1 for all peaks k <= K(s_1), K(s) := min{K : sum_{k>K} lambda_k <= s^2}), no degenerate peaks.
Converse of Fact C (PROVED, elementary): if zeta'' = c''(alpha'' + D^2 w/C) with alpha'' supported on P, sign alpha''_k = sign w(k), ||alpha''||_1 = 1, then
J(zeta'') = w (w norms zeta'': <w, zeta''/c''> = M + C = 1 >= |zeta''/c''|). Apply it to zeta^# := R x' on [1,K] and c R** zhat on (K, inf): if
  (i) u_k(x') = c u_k(zhat) for k in Q_m (|Q_m| linear conditions, c > 0 free), and
  (ii) sum_{k in P, k <= K} sigma_k lambda_k (u_k(x') - c u_k(zhat)) = 0 (one more linear condition, fixing c),
then zeta^# = c|zeta|(alpha~ + D^2 w/C) with alpha~ := alpha + (zeta^# - c zeta)/(c|zeta|) supported on P, ||alpha~||_1 = 1 (by (ii)) and sign-correct (by the
margins), so J(zeta^#) = w EXACTLY. Then w'_m = J(R x') differs from J(zeta^#) only through the deep perturbation ||R x' - zeta^#||_1 = O(s_1^2);
the missing step is a Lipschitz estimate for the finitely many scalars (M', theta') of the clip formula under such perturbations (true when
the 2x2 system defining (M, theta) — C^2 = M^2 S_2(theta), theta m (1-M) = M^2 S_1(theta), S_2 := sum Phi_k^2 clip(u_k/(theta Phi_k))^2,
S_1 := sum lambda_k u_k clip(...) — is non-degenerate at f; not verified in general). Given it, w'_m - w_m = O(s_1^2) on [1,K] and
(PIN) holds with the deep part <= 2 sum_{k>K} lambda_k <= 2 s_1^2. The tuning needs (TC) for the |Q_m| conditions (i)-(ii) (effect vectors
u_k - (u_k(zhat)/pi(zhat)) pi restricted to the moves, pi := sum_P sigma_k lambda_k u_k). This agrees with N2 Prop 3.7(a) (one non-peak).
(e) Infinitely many strict non-peaks in a block with Delta d_m < 0: pinning needs ~ #{off-peak k : Phi_k >= s_1} -> infinity conditions,
solvable with O(s_1) moves only under a quantitative tail-independence property of T (N2 3.7(c)). OPEN.

## 4.2 Failure of (TC): far pulls. SKETCH (PROVED for one block with Delta d = 0 in N2 Thm 1, not re-checked line by line here).
When every available move pushes the tuned functionals the same way (P1's example with diagonal U: the only active functional is
v = c u_{2,1}, supported on F u K', and every contact mass raises v(x')), the correction must come from FAR CONTACTS used with the flipped sign:
for j in Far subset K cap (N, N''], set z'_j := -z_j and a'_j := -m_j z_j with m_j := 2 tau_1 max(|b+_j|, |b-_j|) (so that both one-sided decompositions
are LINEAR at j for |sigma| <= tau_1: the usage of side +- at j only decreases |a'_j| by at most half). The effect on the tuned functional
Gfun_m is -2 z_j V_m(j) per pulled coordinate (plus a Hilbert effect O(m_j nu_j), nu_j = ||U*e_j*|| -> 0). Order of choices: N, then s_1 small compared
with the pull reservoir sum_{K > N} |V(j)|, then Far, then N'' (window of the decompositions) so that tails beyond N'' cost <= eps_0 s_1^2.
Improvement over P1 6.3 (the partial-pull coordinate j* of P1, whose first-order cost the P1 referee flagged): exact tuning is unnecessary.
The residual (Delta d_m - Delta d'_m) R_m* w'_m can be put in the base on side - at first-order cost <= 2 |sigma| |Delta d_m - Delta d'_m| q*(R_m* w'_m), which is
<= eps_0 sigma^2 for |sigma| >= s_1 as soon as |Delta d_m - Delta d'_m| <= c eps_0 s_1; since the pull increments 2|V_m(j)| -> 0 (j -> infinity), a finite
Far realises any required correction within c eps_0 s_1 (subset sums of a null sequence with divergent... finite total: every value in
[0, sum] is within the last increment of a finite subset sum). With Delta d_m > 0 the pulls also enter the Bregman term:
<w' - w, R(z' - z) 1_Far> <= 2 sum_k lambda_k |w'(k) - w(k)| ||u_k 1_Far||_1, which must be o(s_1): a comparison between the far tails of V and of the
other block vectors (T-dependent; N2 3.5). Status: Delta d = 0 one block PROVED (N2); several blocks / Delta d > 0: SKETCH.

## 4.3 a not in c_00 (F infinite). SKETCH.
Window truncation a' := (a 1_[1,N] + Delta)/q*(...). Base parts b+- are supported in F u K with flips allowed at f (they are included in (H1)).
(i) Flip costs at f' vs f: the normalisation changes |a'_j| by a factor 1 + O(s_1 + tail_N(a)); on the flip set {j : |a_j| < 2|sigma b_j|} this changes flip costs by
<= C (s_1 + tail_N(a)) |sigma| sum_{flip set} |b_j| = o(1) s_1 |sigma|, which is <= eps_0 sigma^2 for |sigma| >= s_1 once s_1 is small (phi(sigma) := sum_{|a_j| < 2|sigma b_j|} |b_j| -> 0);
increasing |a'_j| (masses of the sign of a_j) never increases flip costs.
(ii) The two-sided small-scale regime of side + needs no flips for |sigma| <= s_1: add masses 2 s_1 |b+_j| sign(a_j) at the j in F with |a_j| < 2 s_1 |b+_j| (total o(s_1)).
(iii) Coordinates of F beyond N: tails, first-order cost <= 2|sigma| tail_N(b+-) (N after s_1).
Everything else is as in Theorem 3.5. The only new point to check in full is the uniformity of (i) on [s_1, tau_1]; I see no obstruction.

## 4.4 Carriers. SKETCH / OPEN.
(a) Infinitely supported bounded off-peak carriers omega+- with the near-peak decay of A Lemma 6.3 on BOTH sides: truncate at a level
chosen after s_1 (D Lemma 11.5(b) gives exact first-order correction and uniform second-order control on a fixed range); the discarded part changes
the transfer v by a vector of l_1-norm o(1), put in the base at first-order cost <= eps_0 s_1 |sigma|. The delicate point is that the truncated
carriers have gaps gamma(s_1) -> 0, so Lemma 3.2(a) (exact sup part for |sigma| <= s_gamma) is not available on all of [-s_1, 0]; one needs the box-tail
argument of A Thm 6.2 (coordinates with |sigma omega_k| > gap_k/2 discarded into the base at cost o(|sigma|)) AT f', i.e. uniformly along the approximants.
Plausible (the box tails are controlled by the decay, and gaps at f' converge), not written. SKETCH.
(b) Degenerate peaks (alpha_k = 0) used one-sidedly by a linear decomposition (sigma_k Omega(k) on one side of -d M): at f' such k is a peak with
alpha'_k ~ lambda_k (|u_k(x')| - theta' Phi_k)/|zeta'| or an off-peak with tiny gap; one scalar tuning per degenerate carrier keeps it at threshold
(alpha'_k = o(s_1)), after which its one-sided use costs o(s_1)|sigma|. SKETCH.
(c) Weak (non-degenerate) peaks and off-peak carriers whose DEPTH depends on the scale: not covered — part 5.

## 4.5 Summary of the two-piece / finitely-generated class.
| class (f with a in c_00 unless stated, finite I) | status |
|---|---|
| two-piece data, Delta d_m >= 0 all m, (TC) | recovered along engineered NA sequences: PROVED (Thm 3.5) |
| two-piece, one block, Delta d = 0, (TC) fails, pull reservoir | PROVED in N2 Thm 1; P2 4.2 removes the j* issue (SKETCH) |
| two-piece, Delta d > 0 with pulls | SKETCH (far-tail comparison, T-dependent) |
| two-piece, some Delta d_m < 0 | needs (PIN): block-tame robust blocks SKETCH (4.1d); infinitely many non-peaks OPEN |
| a not in c_00 | SKETCH (4.3) |
| infinitely supported carriers with near-peak decay; degenerate-peak carriers | SKETCH (4.4) |
| P1's explicit defect mates (P1 2.3, 6.2 with kappa+- <= 1) | PROVED by Thm 3.5 if some contact has <P_{e-perp}U*u, U*e_j*> < 0; otherwise N2 Thm 1 |

# 5. the general replication–averaging–transfer theorem, the scale-dependent regime, the implant scale gap, the residual class

## 5.1 Theorem (three-regime theorem, abstract form). PROVED.
Let f in S_{p*}, g in C(f), rho in (0,1), delta in (0,1]. Let f' in S_{p*}, gbar, h_1..h_J in X*, scales s_1 > s_2 > ... > s_J > 0 with s_{j+1} = s_j/2, and
Q, kappa >= 0, T_0 in (0,1] such that
 (i)   (small scales: two-sided certificates)   p*(f' + t h_j) <= 1 + Q t^2/2 for |t| <= s_j;
 (ii)  (transfer regime)                        p*(f' + t gbar) <= 1 + Q t^2/2 for s_J <= |t| <= T_0;
 (iii) (frozen errors)                           p*(h_j - gbar) <= kappa s_j;
 (iv)  (constants) Q + 4kappa/J <= 1 - delta, T_0^2 <= 3 delta;
 (v)   (slack regime) p*(f' - f) <= (1-rho^2)T_0^2/6 and p*(gbar - rho g) + 2 kappa s_1/J <= (1-rho^2)T_0/6.
Then g' := (1/J) sum_j h_j lies in C(f'); if f' is NA then (f', g') is NA and ||(f',g') - (f, rho g)|| <= p*(f'-f) + p*(gbar - rho g) + 2kappa s_1/J.
*Proof.* P2_part1 Lemma 1.5 (averaging; the sum over s_j < |t| of s_j is <= 2|t|) gives p*(f' + t g') <= 1 + (Q + 4kappa/J)t^2/2 on |t| <= T_0 and
p*(g' - gbar) <= 2kappa s_1/J; P2_part1 Lemma 1.4 (assembly) with (iv), (v). QED.
(J = 1, h_1 = gbar is the form used in P2x_part3; then (iii) is void.)

## 5.2 Where the three regimes come from, and what each costs (the bookkeeping). PROVED statements.
(a) Slack: covers |t| >= T_0 with T_0 ~ sqrt(6 eps/(1-rho^2)), eps := p*(f' - f) (Lemma 1.4). Any engineering creating two-sided structure for
    regime (i) at scale s contributes to eps (5.3), so regime (ii) must cover a band [s, ~sqrt(s)] at least.
(b) Transfer, base side: exact up to (1) flip changes O(s|t|) x (mass of the flip set), (2) window tails (choose N late), (3) the mixed term
    (P2x_part2 2.5-2.6: finitely many tunings, or compactness). None is an obstruction.
(c) Transfer, block side: the first-order block term is zero when d-coefficients are computed at f'; the price is a consistency mismatch
    sum_m (Delta d-type coefficient) R_m*(w'_m - w_m), which is Theta(s) in l_1 (P2x_part2 Remark 2.3) and is admissible only (1) in the convexity
    form (sign condition), paid by a Bregman excess o(s) (P2x_part2 2.3), or (2) after pinning (P2x_part4 4.1).
(d) Transfer of SCALE-DEPENDENT carriers (Proposition 5.4): not robust.

## 5.3 Lemma (conversion cost identity: the implant scale gap made precise). PROVED.
Let k be a peak of w_m at f and suppose at f' it is an off-peak coordinate with gap'_k = M'_m - |w'_m(k)| (an "implant" or "conversion"). To carry,
two-sidedly at scales |t| <= t_cap, a component c u_{k,m} of the direction through k alone (coefficient c/lambda_k at k), the box condition requires
|t| |c|/lambda_k <= gap'_k/2, i.e. t_cap <= lambda_k gap'_k/(2|c|). The block part of f' - f contains the term lambda_k (w'_m(k) - w_m(k)) u_{k,m}, of q*-norm
lambda_k |w'_m(k) - w_m(k)| >= lambda_k (gap'_k - |M'_m - M_m|) >= 2|c| t_cap - lambda_k |M'_m - M_m|.
So the contribution of the conversion to f' - f is at least 2|c| t_cap (up to the global level change), unless cancelled by other changes of f'.
*Proof.* |w_m(k)| = M_m at a peak; |w'(k) - w(k)| >= |w(k)| - |w'(k)| = M - M' + gap'. QED.
Consequence (HEURISTIC as an obstruction, because cancellations in f' - f are not excluded): an engineered two-sided carrier of capacity t_cap costs
eps >~ |c| t_cap, the slack then covers only |t| >~ sqrt(|c| t_cap/(1-rho^2)), and the band [t_cap, sqrt(t_cap)] must be covered by structure that f and f'
share. This is C's "implant scale gap" (C_notes 9.3), CONFIRMED in this quantitative form; it applies equally to near-threshold conversions
(E_part2 2.4): their low cost buys proportionally low capacity. The same identity holds for window masses on base contacts: a mass m_j at a contact used
with coefficient b_j gives capacity m_j/|b_j| and costs m_j in ||a' - a||_1.
C's conclusion "implants are useful only below the slack scale created by other mismatches, never as the sole support at intermediate scales" is
CORRECT but not an obstruction to the three-regime scheme: Theorem P2x_part3 3.5 covers the band by EXACT transfer of the one-sided decompositions of f.

## 5.4 Proposition (precision obstruction for scale-dependent block carriers). PROVED (as a statement about transferred decompositions).
Let f' be an engineered approximant whose normer differs from zhat by Delta_k := |u_k(xhat') - u_k(zhat)| at a block coordinate k that is off-peak at f and f'.
(a) (clip formula) |w'(k) - w(k) - (M/theta)(u_k(xhat') - u_k(zhat))/Phi_k| <= |M'/theta' - M/theta| theta' = o(1): the value moves by ~ Delta_k/Phi_k.
(b) Suppose a decomposition of f + t rho g at f uses k beyond its box, i.e. the sup norm of W = w + t Omega is attained at k: |w(k) + t Omega(k)| = ||W||_inf.
    Transferring it to f' with the same coefficient changes the sup part by w'(k) - w(k) (zero order in t); re-tuning the coefficient to
    Omega'(k) = Omega(k) - (w'(k) - w(k))/t keeps the sup part but changes the represented direction by lambda_k (w'(k) - w(k)) u_k, which must be carried by the
    base: first-order cost in the base of order |t| (lambda_k |w'(k) - w(k)|/|t|) times the kink weight = lambda_k |w'(k) - w(k)| x O(1) (zero order in t).
    Either way the error is ~ lambda_k Delta_k/Phi_k ~ m Delta_k, to be compared with eps_0 t^2.
(c) With window masses of size s (needed for regime (i) at scale s, by 5.3), Delta_k ~ s for every k (P2x_part2 2.4; generically sharp), so a carrier used at
    scale t ~ Phi_k (a scale-dependent carrier: depth tied to the scale) transfers only for t >~ sqrt(s/eps_0): the band [s, sqrt(s/eps_0)] is NOT covered.
(d) Averaging does not help: in 5.1 the transfer (ii) of gbar is needed down to the SMALLEST scale s_J, but the engineering for the largest
    certificate h_1 (scale s_1 = 2^{J-1} s_J) perturbs the normer by ~ s_1.
*Proof.* (a) P2x_part2 2.1 (off-peak: w = M u/(theta Phi)). (b),(c) are direct computations from (a) and P2x_part2 2.4. (d) Lemma 1.5's hypothesis (ii). QED.
So the only structure that crosses the band is "robust" structure: base coordinates (contacts, near-contacts, flips: P2x_part2 2.6), finitely many FIXED
block carriers with d-coefficients recomputed at f' (P2x_part3 3.2), and Bregman pairings. Pinning the ~log(1/s) values of the scale-dependent carriers
in the band would need a quantitative tail-independence of T (N2 3.7(c)): OPEN.

## 5.5 Which mates admit regime (i) (two-sided small-scale structure at an engineered f'). Classification.
Let g in C(f), a in c_00 (finite I). Regime (i) at scale s can be supplied, at cost eps = O(s), for a component of g carried at scales <= s by:
 (1) base contacts or near-contacts (window masses / small shifts of z'_j; P2x_part3 Step 4) — YES;
 (2) finitely many fixed off-peak carriers of w (already two-sided within their box) — YES;
 (3) degenerate peaks (alpha_k = 0) used one-sidedly — YES after one scalar tuning each (P2x_part4 4.4(b), SKETCH);
 (4) weak non-degenerate peaks, super-near-threshold carriers (summable gaps), off-peak carriers whose depth grows as t -> 0 — only by conversions
     (5.3), whose perturbation destroys the transfer of the other scale-dependent carriers in the band (5.4): NO with the present tools.
Regime (ii) must transfer both sides on [s, ~sqrt(s)]; by 5.4 this holds for robust decompositions.
**Answer to the task's question.** (ii)/(i) can be supplied exactly for mates which, on each side, have decompositions near 0 using only robust structure:
one-sided linear decompositions (two-piece data, arbitrary contact splitting, contacts on both sides, fixed carriers pushed beyond their gap at
fixed scales) — Theorem 3.5 with (H2) Delta d_m >= 0 and (TC), or pinning when Delta d_m < 0 (4.1). "Finitely generated" switching (carriers in a fixed finite set,
base parts varying with t) should go through the same proof with Prop 2.6(b) for the base and a per-piece convexity sign condition
sign(t)(d_t - d_ref) <= 0 (SKETCH, not written). Switching through scale-dependent BLOCK carriers on either side is not covered.

## 5.6 The exact residual class (relative to all recovery mechanisms now available). 
For f in S_{p_N*}, call g in C(f) COVERED if one of the following holds (recovery along engineered sequences depends on g, so convex combinations
of covered mates are not automatically covered — only (C1) is a closed convex set recovered along every sequence):
 (C1) g in cl Cert^sh(f) (A: transport along every sequence; includes Theorems W, L, averaging class, weighted averaging P1 4.3-4.4, C Thm 7.1/7.4);
 (C2) g is locally split (D Thm 11.6);
 (C3) g has two-piece data with finitely supported off-peak carriers, a in c_00, (H1), Delta d_m >= 0 for all m, and (TC) (P2x Thm 3.5, PROVED);
      or one active block, Delta d = 0 and a pull reservoir (N2 Thm 1, PROVED there);
 (C4) [SKETCH-level] as (C3) with a not in c_00, with bounded infinitely supported carriers with near-peak decay, with degenerate-peak carriers,
      with Delta d_m < 0 at block-tame blocks with robust window peaks (pinning), or with pulls and Delta d > 0.
RESIDUAL (not covered by any PROVED mechanism; the candidates for a counterexample live here):
 (R1) two-piece mates with some Delta d_m < 0 in a block with infinitely many strict non-peaks (pinning needs quantitative tail independence);
 (R2) two-piece mates where (TC) fails and the pull reservoir comparison fails (T-dependent);
 (R3) SCALE-DEPENDENT SWITCHING: mates with no one-sided linear (or finitely generated) decomposition near 0 on at least one side, even modulo
      cl Cert(f), whose one-sided resources at scale t include block carriers of depth -> infinity as t -> 0: weak non-degenerate peaks,
      super-near-threshold carriers with summable gaps (P1 4.4 Rem), deep off-peak carriers at generic f (Q_m infinite). Here the precision obstruction
      5.4 applies to every scheme based on window masses or conversions;
 (R4) infinitely many blocks (avoided by Remark martin-tail).
No element of (R1)-(R3) is known to exist outside cl NA; no argument here produces a counterexample (every obstruction above is an obstruction to a
METHOD: cancellations in f' - f and other decompositions are not excluded).


# 6. The other P2 instance's results (P2_part2.md, P2_part3.md): summary and what I re-checked

**6.1 Theorem (d-neutral two-piece mates; P2_part2 2.1). PROVED there.** f with F finite, g in C(f) with d-neutral two-piece data (Delta d_m = 0 for all m),
rho^2 kappa < 1; if |I_0| >= 2 a steering span hypothesis (S) on free coordinates. Then (f, rho g) in cl NA. No condition on the contact split, on K,
on rates of T or on the number of non-peaks; no tuning cone condition.
Key step re-checked (steering without (TC)): P_{e-perp}U*v != 0 (v in Y \ {0} is not a multiple of a, U* injective), and since v lives on F u K with
z_j v_j = |v_j| on K, sum_{j in F} v_j <P_{e-perp}U*v, U*e_j*> + sum_{j in K} |v_j| <P_{e-perp}U*v, z_j U*e_j*> = ||P_{e-perp}U*v||^2 > 0, so there is a "raising"
coordinate j_+ (in F with either sign, or a contact with its own sign) whose mass increases v(xhat'); far flipped contacts with negative masses
("pulls", reservoir sum_{K > N}|v_j| > 0 because v is not in c_00) decrease it by 2 sum_Far |v_j|; the intermediate value theorem gives v(xhat') = 0
exactly. Order: N, s_1 (small w.r.t. the reservoir), Far, N'' (decompositions transfer exactly on (N, N''] \ Far, and are linear on Far thanks to the
negative masses), then the raising mass; beyond N the target uses the constant-split theta-tail. I checked the sign identity, the Far
compatibility (z'_j = -z_j = sign a'_j) and the tail estimate; I did not re-derive every constant.
Combined with Theorem 3.5 above: A_referee §5.4's general form (d-neutral, any split) is PROVED (one block: always; several blocks: under (S) or (TC));
Delta d_m >= 0: PROVED under (TC) (Thm 3.5); Delta d > 0 with pulls only: SKETCH (Bregman term needs a far-tail comparison, 4.2).
**Numerics of the other instance (P2_part5.md):** clamp formula certified by SOCP duality (30 random blocks); the construction of 6.1 run in
the P1-referee finite model of P1's example (6 seeds): steering to 1e-16, constructed pair contractive up to solver offset 5e-7.
**6.2 (P2_part3 3.1-3.2).** The mixed term and the multi-piece consistency identity — agree with my 2.5-2.6 (their 3.2 identity
B'_t - B'_{t'} - rho(B_t - B_{t'}) = -rho sum_m[(Delta'_m - Delta_m)R_m*w'_m + Delta_m R_m*(w'_m - w_m)] is the multi-piece form of my Step 3 algebra).
**6.3 (P2_part3 3.4, SKETCH there).** Non-neutral two-piece data (any sign of Delta d) at block-tame active blocks with margin sparsity and a tuning
span: agrees with my 4.1(d) (pinning); both are SKETCH (uniform implicit-function / Lipschitz step for the global scalars not written in full).
For Delta d_m >= 0 my Theorem 3.5 removes all block-tameness and margin assumptions.

# 7. Answers to the specific questions of the task, and next steps

(a) **A_referee §5.4 (two-piece mates over infinite contact sets with non-constant split).** PROVED: Theorem 3.5 (several blocks, Delta d_m >= 0, (TC)) and
6.1 (d-neutral, other instance). The referee's "extra degree of freedom in the masses" is correct exactly when (TC) holds (P1's diagonal-U
objection is the failure of (TC)); otherwise pulls are needed (6.1). The referee's truncation of g is fine when N is chosen after s_1 (no pulls);
with pulls one needs the constant-split tail (P1's correction).
(b) **Switching mates.** Contacts on both sides: covered (Thm 3.5: side - contacts transfer exactly, side + contacts get masses). Off-peak carriers
pushed beyond their gap: covered when the carriers are fixed (Lemma 3.2(b): activation at fixed scales, zero-order errors -> 0); NOT covered when the
depth of the carrier grows as t -> 0 (Prop 5.4). Weak peaks: degenerate peaks (alpha = 0) SKETCH-covered by one tuning each (4.4(b)); non-degenerate weak
peaks are scale-dependent resources (usable only at scales t >~ alpha_k dev_k): residual (R3), except when intrinsic weighted averaging applies
(P1 4.3-4.4: non-summable gaps -> cl Cert(f)).
(c) **C's implant scale gap.** CONFIRMED in quantitative form (5.3: capacity t_cap costs >= 2|c| t_cap in f' - f, absent cancellations; the same
cost/capacity ratio for window masses and near-threshold conversions). It is not an obstruction to the three-regime scheme: the band
[t_cap, sqrt(t_cap)] is covered by exact transfer of robust structure (Thm 3.5). It IS an obstruction for scale-dependent carriers (5.4).
(d) **The mixed term delta t <P^perp U*e_j, P^perp U*B_t>/||U*a||.** Exact form 2.5. Not an obstruction: for one base part it is absorbed by the
a'-multiple; for finitely many pieces it is cancelled by finitely many scalar tunings (for two-piece data: the single condition Delta d'_m = Delta d_m,
whose residue is the Bregman excess, o(s_1)); for any bounded family of base parts it is cancelled up to eta by finitely many tunings (compactness of U*).
Cancellation needs tuning moves with positively spanning effects ((TC)) or pulls.
(e) **Exactly for which mates regime (i) can be supplied:** 5.5 — components carried at small scales by base contacts/near-contacts, fixed off-peak
carriers, (degenerate peaks); not for components carried at all small scales by scale-dependent block carriers.
**Next steps.** (1) Prove the pinning Lipschitz step (4.1(d)) to close Delta d < 0 at block-tame blocks. (2) "Finitely generated switching" (carriers in a
fixed finite set, base parts varying with t): write the per-piece convexity version (SKETCH in 5.5). (3) Decide (R3): either find an f with a
mate in (R3) and a uniform lower bound dist(rho g, C(f')) >= c for all NA f' near f (counterexample route — would need excluding cancellations in
f' - f, which none of the present arguments does), or a pinning scheme with ~log(1/s) conditions, i.e. a quantitative tail-independence property of T
(possibly arranged by choosing T, cf. P1 2.1). (4) Shifted two-piece data (P2_part2 2.4) to get f in R at P1's example.
