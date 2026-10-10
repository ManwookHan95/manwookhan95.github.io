# K2 referee notes (Round 11): proofs of the verdicts, precisions and repairs for r11/K2_notes.md

Setting and notation of r11/K2_notes.md (design T_fin^{K2}: T_fin of Q1 over the diagonal base U k_s = mu*_s e_s, mu*_s = 2^{-2^{2^s}}, option (a),
with K1's (D-K1), K1-ref R-6/R-7/R-8 and K2's insertions (K2-a)-(K2-e); N >= 1; f in S_{p_N*} with base support F arbitrary; g in C(f); rho in (0,1);
main stage L, clean sub-window w, T := T_lo(w), b := b(w), u := u(w), D(L), H(L), U_L as in K2 1).  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Part files: r11/K2_ref_part1.md (K2.1-K2.5), part2 (preparation, K2.6, K2.7), part3 (Sys-A), part4 (bookkeeping, K2.15, gap W-1), part5 (precisions
K-7, K-8).  Scripts and outputs: r11/K2_ref_work/.  This file supersedes the part files where they differ.

## A. Verdict table
| K2 claim (K2 label) | Verdict | Items |
|---|---|---|
| Lemma K2.1 tolerance variant of UE^inf (PROVED) | correct | B.4 |
| Lemma K2.2 identity (PROVED) | correct | B.1 |
| Lemma K2.3 resource dichotomy (PROVED) | correct; the SIGNED form is what Section 5 uses | B.1 |
| Lemma K2.4 first-order actions (PROVED) | correct; sign typo in the composite move | B.2 |
| Lemma K2.5 left combinations (PROVED) | correct | B.3 |
| Preparation (P), 4.1(a)-(d) (PROVED) | correct; (R1) verified; C_+ is an f-constant at banked coordinates; doubled b in (D1) suffices (F) | C.1, F |
| Theorem K2.6 Sys-DC uniformly solvable (PROVED) | correct (PROVED mod chain); precisions P-3 (sup-norm slip), P-4 (K_DC) | C.2 |
| Corollary K2.7 (PROVED) | correct after rewording: the degeneracies are BYPASSED, not absent (square system stays degenerate) | C.3 |
| Lemma K2.8 Euler combination (PROVED) | correct; Xt_m small exactly in route V | D.1 |
| Lemma K2.9 cone realization (PROVED) | correct with two precisions: frozen coarse statuses in (c) (K-8), u-scaling of W (K-7) | D.2 |
| Theorem K2.16 structure of Step-A obstructions (PROVED) | correct; precisions K-1 (2a), K-2 (sign convention), K-3 (|a_s| at S_th) | D.3 |
| Corollary K2.17 (PROVED) | (a)-(f) correct; (g) is a reduction to (f), not a sufficient condition by itself (K-4) | D.4 |
| (O-c)(iii) not a separate obstruction (PROVED) | first part correct; the "Moreover" (far z-move breaks the certificate) is a SKETCH (K-5) | D.5 |
| Proposition K2.11 (SKETCH) | label honest | D.5 |
| Lemmas K2.12-K2.14, costs (PROVED) | correct (an apparent (K2-e) problem was checked and withdrawn, F) | F |
| Theorem K2.15 (PROVED mod chain) | correct after replacing the per-peak (H1) by the joint (H1*) (GAP W-1) and with K-7, K-8 | E, G |
| 7.3 residual class (OPEN) | "iff" must be "only if" (K-6); (W) becomes (W*) | E, G |
| Density for p_N, p (OPEN) | OPEN (agreed) | I |

## B. Lemmas K2.1-K2.5 (re-derivations)
B.1 (K2.2, K2.3).  zhat = z + Ue, so u(zhat) = sum_s u(s) z_s + <U^*u, e>, <U^*u, e> = kappa_u nu, and on F, u(s) = D_u(s) + kappa_u a_s, z_s = sgn a_s;
with ||a||_1 + nu = 1 this is the identity; for s in F, s > D, D_u(s) sgn a_s = u(s) z_s - kappa_u |a_s| gives (2.1) with 1 - alpha(D) = ||a 1_{[1,D]}||_1 + nu
>= nu.  SIGNED dichotomy (PROVED): if kappa_u >= 0 then sum_{s<=D} (c_s(u))_- >= <U^*u, e> - u(zhat) - ||u 1_{(D,inf)}||_1; if kappa_u <= 0 then
sum_{s<=D} (c_s(u))_+ >= |<U^*u, e>| + u(zhat) - ||u 1_{(D,inf)}||_1.  (Proof: (2.1), kappa_u(1 - alpha(D)) >= kappa_u nu resp. <= kappa_u nu, |z| <= 1.)
B.2 (K2.4).  d(x/||x||) = (I - e e^T) dx/||x||; <U^*u, k_s - e_s e> = mu_s D_u(s) with e_s = mu_s a_s/nu; renormalization by q* leaves e and z unchanged;
the second derivative of x/||x|| is <= 3||dx||^2/||x||^2.  Composite move at a zero-data contact: bank branch (P > 0) of mass (nu/mu_s^2) P z_s and
z-branch (P <= 0) z_s -> z_s(1 + P) [K2 writes "-P z_s": sign typo]; slope u(s) z_s on both sides.  At a ZD coordinate left by Step A with a small
mass m the two branches' first derivatives differ by <= Design(L) m (common-mode term kappa_u m/|u(s)|): harmless for m <= Design K_DC r.
B.3 (K2.5).  (a) sum_{l in Omega_m} y_l eps_l u_l(zhat_0) = A^0_m y^T p_m and (R_m^* w^0_m)(zhat_0) = <w^0_m, R_m^** zhat_0> = A^0_m (X2 Lemma DC defines
A^0_m := |R_m^** zhat_0|_m; w^0_m norms it).  (b) dF_l = eps_l du_l - p_l dA_m, dA_m = <w^1_m, R_m dxhat> + O(|delta|^2), ||R_m^*(w^0_m - w^1_m)||_1 <= K_w Pi
+ 2 c_{L+1}.  (c) <U^* R_m^* w^0_m, e_1> = G_m (with w^0) up to the same error.
B.4 (K2.1).  The four uses of d-consistency in X2's proof of Theorem UE (r9/X2_notes 3.5) and in Q2's (M1)-(M5): (u1) with diamond = +,
b^theta - b^+ = -(1/2) sum_m R_m^*(Domega_m - Delta_m w^0_m), so Omega^+_m = rho(omega^+ - d'(omega^+) w') + kappa^+ w' + rho(d^+ - d^theta)(w' - w^0) with
kappa^+ = -(rho/2) mis_m (symmetric for -; the theta pair has kappa^theta = 0 by construction of g''_i); (u2) W_0 = (1 + tau kappa)(w' + t''(omega - d'(omega) w')),
the level term tau kappa enters lin'_m, and X2's Step 4 uses lin' only through |lin'_m| <= tau^2 (the level-shift cost |tau kappa| iota, iota <= 2 eta_1, is
inside E <= 12|I| K_sharp eta_1 tau^2); (u3) |d' - d|(omega) <= |Omega| (A_2/t) K_w Pi, H' - (C/C')H = (d^2 - d'^2)/C', relative error in Step 5 <=
C_f |Omega| A_2^2 K_w^2 s_1/T^2 <= delta/32; (u4) the extra term sum_m (d_m - d'_m)(omega^theta) R_m^* w'_m in g''_i - g_i.  Nothing else uses d-consistency.
|mis| <= (m/A')||D Domega||_2 ||F||_2 (nv' - nv = lambda eps F/A'), so |F|_inf <= c_f s_1/|Omega|^{1/2} suffices.  PROVED.

## C. Preparation, Theorem K2.6, Corollary K2.7
C.1 Preparation (P).  (a) Cost: zeroth-order bound p*(f^P - f^r) <= q*(a^P - a^r) + C_f c(delta) (Z3 Lemma 3.1) <= C_f D(L) theta_0 log(e/theta_0); hypothesis
(a) of Theorem E^{eng,RT,inf} with lambda = 1.  (b) values move by <= C D(L) theta_0/nu.  (c) DATA AT BANKED COORDINATES ((R1), VERIFIED): a banked j was
a contact of f^r carrying its (X1) contact row in the class cone (U1 cone on E_c; K1 2.1(b), K1 1.3), so V_t(j) is z_j-signed; V1 TR Step 5 treats
companion support outside supp a^r as contacts (V1 Theorem E''): b^+ = chi V' + beta_j, b^- = -(1 - chi)V' + beta_j with the base term beta_j =
-kappa a^#_j/a^#(zhat^#), |beta_j| <= C_f t theta_0 (Q2 Lemma 3.1).  Hence (U3^inf) holds at j with C_+ = max(5, C_f) (an f-constant; E^{eng,RT,inf}
accepts it, c_flat >= c_f u unchanged); fine-origin violations at j are <= C Design c_{L+1} << theta_0/T; (L-K2-1) protects the theta piece.  (d) types
TS / S_th / FR (ZD a sub-label) exhaust U_L cap [1, D(L)] at f_0 and f_1.
C.2 Theorem K2.6 (re-derivation; PROVED modulo X2/Q2/K1 machinery).
 Step 1 (lever columns).  For l in Omega, dF_k/dP_l = delta_{kl} - h_l (g_k - G_{m(k)} p_k) - p_k q_l 1[m(k) = m(l)] (re-derived; = Q2 4.0) with the SIGNED
 h_l = eps_l a_s/(nu_1 v_l(s)); every l has a two-sided lever (zero-data off-F/thin near coordinate: ZD composite; data-carrying with an off-F near
 coordinate: it is a contact of the data sign (a free one forces c_l = 0, K1 2.1(b)), banked, S_th lever; thin near coordinates of data-carrying l carry
 the data sign (K1 Lemma K1.3(S)), raised, S_th lever; all near coordinates thick: (P3)/(P4)).
 Step 2.  Route V: D = I; y = sum_m beta_m q_m + gamma h + e', beta_m(1 - q_m^T p_m) = gamma h^T p_m + e'^T p_m, q_m^T p_m <= C_m <= 1/2,
 ||q_m||_2 <= 1, ||p_m||_2 <= 2|Omega|^{1/2}/A_min; hence 1 <= (|gamma| ||h||_2 + ||e'||_2)(1 + 4 sum_m ||p_m|| ||q_m||): gamma is robust unless eps is large.
 Step 3.  Psi_y(zhat_0) = 0.  PRECISION P-3: "||xhat_1 - zhat_0||_inf <= K_w Pi" is false (z_1 = z_0 1_{[1,N'']}); use instead |Psi_y(xhat_1) - Psi_y(zhat_0)| <=
 ||U^*Psi_y|| ||e_1 - e_0|| + ||Psi_y 1_{(N'',inf)}||_1 <= C(K_w Pi + t(N'')).  Tail beyond D(L) <= gamma/16 for L >= l_f by the choice of D(L).
 Step 4.  Signed dichotomy (B.1) at f_1 with u = Psi^c: sum_{s <= D(L)} |c_s| >= (13/16) gamma; off U_L only anchors (thick, |a_s| >= nu_1/(4D(L))) can carry
 gamma/(2D(L)); every s in U_L cap [1, D(L)] carries a two-sided elementary column.
 Step 5.  |y^T c_s| >= eff_s |c_s(Psi_y)| - err >= mu*_{D(L)}^2 gamma_min/(4 D(L)) = eps_DC.
 Step 6.  Poincare-Miranda with R = C^T(CC^T)^{-1}.  PRECISION P-4: ||R||_{inf->inf} <= |Omega|^{1/2}/s_min (number of ROWS).  Statuses: all moves <= K_DC r
 are far below every margin, so the block norms are C^{1,1} on the cube (unlike Sys-A, D.2).
 Interface with Theorem UE: X2's (SEP) is sufficient for the special form J = I - pq^T, not necessary; UE uses the levers only through Lemma DC's
 conclusions, the Step 3 (Base) protection (the new columns act at TS, S_th, FR, ZD coordinates: cushion dominated, aligned, zero data) and Lemma
 UE-1(b)-(d) (coarse carriers meeting the new columns keep their statuses: Bregman bound unchanged with Pi enlarged by C_lev K_DC r).
 Numerics (ref_dc_degenerate.py): six exact one-block models with an EXACTLY singular square (P4) system (s_min ~ 1e-11): Psi_y(zhat_0) ~ 1e-16, gamma =
 0.081-0.088, D_Psi = 0 at the lever coordinates, identity 1e-16, off-support sum of Psi z = -kappa; PREPARED rows: s_min(enlarged two-sided) = 0.072-0.130
 for theta_0 = 1e-2, 1e-4, 1e-6 (square part: s_min ~ theta_0); Newton solves F = 0 for perturbations of both signs along the degenerate direction, banked
 masses stay >= 0.76 theta_0.
C.3 Corollary K2.7.  (a) must read: the degeneracies may persist for the SQUARE lever system but are bypassed by the enlarged column system (numerics above).
(b) re-derived (C.5's identity holds for every setting of the ORIGINAL levers, which never act on supp u_h minus F_0): h^T p_m = 0 and c_alpha = 0 give kappa = 1/nu_0, sum_{F_0^c} u_h z = -1/nu_0, ||u_h 1_{F_0^c}||_1 >= 1/nu_0 >= 16; the explanation is heuristic,
the proof is K2.6.  (c), (d) correct.  The data-side bordering (R3-a) is not needed.

## D. Sys-A
D.1 Lemma K2.8.  1-homogeneity of A, theta (E1, E2 invariant under scaling with P fixed) and 2-homogeneity of S give Euler's identity; (b) chain rule;
(c) common mode.  Xt_m = sum_{l in m} rt_l eps_l lambda_l d kappa/d zeta(l) is tiny in route V because Lambda_A contains all coarse strict non-peaks, so
X_m <= C b^2 D^2 (U1 Lemma 1.5 final form) and d kappa/d|zeta(d)| = rho_d M X/C (U1 Lemma 1.4(c)).  Numerics: Euler 4e-10, K2.8(b) 1.5e-5 (central
differences), |Xt| <= 3.4e-6 in this regime vs 3e-2 with one coarse non-peak left out.
D.2 Lemma K2.9.  (a), (b) re-derived (separation; quantitative Farkas).  (c): the minimal-norm nonnegative selection is continuous on cone(G) (Hoffman +
continuity of the metric projection under Hausdorff convergence); antiparallel +-g are never both used; Brouwer on K.
PRECISION K-8 (frozen statuses; PROVED).  ||Rem(t)|| <= C_2 ||t||^2 needs fixed coarse statuses on K.  After Step 0 the active near-threshold carriers have
margin ~ b while points of K move values by up to W >> b; when an Omega carrier d crosses the threshold, d kappa/d|zeta(d)| jumps from rho_d M X/C (~0) to
-1 + C Phi_d^2/Phi_P^2 - X (computed from U1 Lemma 1.4(a) and cert0's formula kappa = A + theta[Phi_{P\Omega}^2 + sum_{Omega cap P}(1 - rho^2)Phi^2] +
S_f/theta); numerically (ref_kappa_jump.py) 0 -> -0.85..-0.96 while A stays C^1.  FIX: compute (A_m, theta_m) with the coarse peak set frozen at f_1 + Pi
(nonsingular smooth system, Jacobian >= Phi_P^2 >= D^{-2}); fine carriers computed truly (their status changes cost <= C c_{L+1}||t|| << rho_0).  The frozen
map is C^{1,1} on K; at the Brouwer solution the ratios are r'', the frozen rho_d = m|r''_d|K(sigma, R^2)/Phi_d <= 1 - mu/2 (Lemma K is the frozen
computation), robust statuses are kept, so the frozen (A, theta) solve the TRUE threshold equations and by uniqueness (lem:threshold) the solution is
a true one.  The same repair applies to the cube faces of K1 Lemma K1.6(A).
PRECISION K-7 (u-scaling; PROVED).  To contain K1's (LR) (right inverse <= Design^{C_0}/u, i.e. eps_PS >= u Design^{-C_0}) define A-regularity with
W := Design(L)^{C_A} u(w)^{-3} max(x, ||b||) and eps_* := u(w)^3 Design(L)^{-C}.  Costs C_f Design^C (x/u^3) log(1/x) = o(u^2 T^2), moves << u;
K2.9(a) with eps_PS >= u Design^{-C_0} and C_A >= C_0 + 2; K2.9(b) gives certificates of size <= 4u^3 Design^{-C_A}; K2.16 survives (kind (ii):
|kappa| <= 8 eps Design^3/u^2 <= 8u Design^{3-C}).  Then (LR) => (H2).
D.3 Theorem K2.16 (re-derived; PROVED).  (2) from K2.8(b) + K2.4 with eff >= 1/Design.  PRECISION K-1: in (2a) a pre-placed TU bank sits on a support
coordinate of mass m_s in [theta_0, theta_0 + Design x'_max] (base bank of the pre-placed pull), so |coef_k| <= (eps Design + |kappa| m_s) Design.  PRECISION K-2: the raise action at S_th is (coef_k v_k(s') -
kappa a_{s'}) sgn a_{s'}; "coef_k z_{s'} >= ..." presupposes v_k > 0 on S_k (SLD signatures); in general use z_{s'} sgn v_k(s'), also in kind (iv) and
K2.17(d).  (1): signed dichotomy.  (3): zeta_m(1 - Xt_m) = sum_{l in m} rt_l eps_l coef_l gives ||coef_tuned|| >= c_1; kinds (i)-(iv) exhaustive (kind
(ii) may be defined with any spread >= C eps Design^3/|kappa|); case gamma > -gamma_0 forces ||coef_(iv)|| >= c_1/2 and, by (2.1), gamma <= -c_1 nu_1/(8H(L)).
PRECISION K-3: at f_1 + Pi the S_th moduli lie in [theta_0, 2b]; the proof needs only |kappa||a_s| <= 2|kappa|b.  (4)-(6) correct ((6) under phi_y > -rho_0).
Observation (PROVED): if every (P4)-carrier has proportional thick coordinates a_s = r_l v_l(s) and meets the support only there, h^T g = (Hilbert mass of
a on these private sets)/nu^2 <= 1; so the (A*) degeneracy h^T g~ ~ 1 needs the peak terms -(h^T rt^{(m)}) G_m or cross terms through targets.
D.4 Corollary K2.17.  (a)-(e) re-derived from K2.16 (with K-2 in (d)).  (f): y ~ +-h/||h||, only -y_+ can be a certificate; phi_{y_+} >= 2rho_0 + dev
excludes it (contrapositive of K2.9(b)).  PRECISION K-4: (g) shows every near-certificate is of type (A*) with y ~ -h/||h||; A-regularity still needs (f)'s
criterion, so in 7.2 "(a)-(g)" must read "(a)-(f), or (g) together with (f)'s criterion".
D.5 (O-c)(iii) and K2.11.  KN-1 holds are zero-target, zero-data rows of Sys-A; K2.16 covers them (correct).  PRECISION K-5: a far CONTACT gives only a
one-sided z-move (two-sided after pre-placing z_j inside (-1,1)); its per-unit action |coef_l| v_l(j) <= x'_max is far below the certificate tolerance, so
"breaks the certificate" needs the range/overshoot argument of K2.11 -- SKETCH, as is the derived requirement "S_l cap {x <= v_l <= x'_max} in F, |a_j| >
x'_max".  K2.11: SKETCH honest; for a data-carrying carrier a placement of the data sign at a contact of the data sign has no effect (sigma - z_j = 0), so
pushes act only at anti-data-sign far support (flip through zero) or at zero-data carriers: the push lemma is the mirror of V1's IN-F pull.
PRECISION K-6: 7.3's "iff" is only "only if" (K2.9(b) is one-directional).

## E. GAP W-1 (Step 0 with several weak peaks) and the joint hypothesis (H1*)
Statement of the gap.  (H1) of K2.15 (= K1-ref R-8, extended) is a per-peak condition.  Step 0 must push ALL active weak peaks of (T)-blocks to rho <= 1 - b
(X1 KN^tr Step 0), making them strict non-peaks (needed for D.1's small Euler share and Lemma R-kt).  A (P4) push of weak peak k changes every value at
first order by -g_{k'} h_k per unit private change, |h_k| up to H(L)/nu (thick near coordinate, tiny v_k), so |g_{k'} h_k| may exceed 1; K2's extension
to arbitrary design-depth moves adds first-order private effects u_{k'}(s) on other weak peaks at shared coordinates.  With >= 2 such pushes the system on
the weak-peak rows is I - g_W h_W^T, singular when 1 - h_W^T g_W = 0 (Step-0 analogue of the Sherman-Morrison degeneracy): per-peak resources exist but the
joint push is impossible or needs moves >> Design^C b/u (outside R-8's enlarged (D1)).  R-8 controlled the side effects on rate objects, not this feedback.
Already for ONE weak peak: the (P4) column moves k's own value by (1 - g_k h_k) per unit, so a (P4) push of k exists only if |1 - g_k h_k| is bounded
below (the needed move scales like 1/|1 - g_k h_k|); R-8's list of push resources must carry this condition.  If the left null vector y ~ h_W of
I - g_W h_W^T has components of one sign in the inward orientation, the inequality system (I - g_W h_W^T) delta <= -tau (tau > 0) is infeasible
(apply y^T), although every peak has its own (P4) resource.
(H1*) (replacement; PROVED to suffice).  There are admissible push moves -- far pulls at depth in [2b theta Phi/m, x'_max], near banks when Delta''_m > 0,
(P3), (P4), design-depth moves of K2.4 admissible for their data -- of total size <= Design(L)^C b/u(w) after which every active weak peak of a (T)-block
has rho <= 1 - b (equivalently: the Step-0 inequality system is A-regular in the sense of K2.9 with the needed decreases as right-hand side, with the
frozen-status convention of D.2).
Sufficient conditions (PROVED).  (i) Every active weak peak has a PRIVATE push resource (far pull, near bank with Delta''_m > 0, (P3); active weak peaks carry
data, so (P1) does not occur): cross effects among weak peaks are second order (V1 Lemma B: <= C Design^2 (2b theta Phi/m)^2 in value, i.e. << b in rho),
so pushing each to rho <= 1 - 2b realizes Step 0 (overshoot is harmless: only F(r_1) <= 1 + C_* b and the (D1) radius are used afterwards).
(ii) The weak peaks pushed by (P4) or shared moves have |1 - h_W^T g_W| >= u(w): solve their rows exactly (two-sided) with ||(I - g_W h_W^T)^{-1}|| <=
1 + ||g|| ||h||/u, moves <= Design^C b/u; the remaining (private) pushes absorb the first-order cross effects one-sidedly (block triangular).
Also: (H1)'s "lowering eps_k val_k" must read "lowering vs_k val_k" (inward), i.e. raising eps_k val_k when Delta''_m > 0 (eps_k = -sgn(Delta''_m) vs_k).

## F. Bookkeeping (O-d)
K2.12 (order, finiteness, N-freeness, monotonicity via U4 Lemma GW), K2.13 (clean dichotomy at depth D(L) with the 2D(L) objects |a_s|, 1 - |z_s|) and
K2.14 ((LATE) additions; theta_0 >= exp(-C log^3(1/T)), K_DC <= C_{f,N} log^{C_0}(1/T), s_1 <= exp(-C' log^3(1/T))) re-derived: correct.  Costs 6.5:
correct.  CHECK of (K2-e) (an objection considered and WITHDRAWN): (P1) closes up to D(L) tiny rooms, but each carrier's value moves by
|sum_s u_k(s) dz_s| <= b ||u_k||_1 <= b, and (P2), (P3) move values by <= C D(L) theta_0/nu << b; rooms and moduli move by <= b each.  So the tiny
objects move by <= Lip (b + o(b)) and K2's doubled b in (D1), (D2), on top of R-8's factor Design^C/u for Step 0, is sufficient.  K1's (R-lev) objects are not needed; K2.17(e)'s
"robust spread" can be weakened to "spread >= Design^{-C}".

## G. Theorem K2.15 as accepted (PROVED modulo the cited chain: X2/X2-ref, Q1/Q1-ref a,b/cert0-3, Q2/Q2-ref a, K1/K1-ref; several links once-refereed)
Design T_fin^{K2} with (K2-e) as in F.  Let N >= 1, f in S_{p_N*} (F arbitrary), g in C(f), rho in (0,1).  Suppose that for infinitely many main stages L there
are a clean sub-window w and a class a with >= n(w)/D_cl(w) scales such that (H1*) holds (E) and Step A is A-regular after Step 0 and (P) with
W = Design^{C_A} u^{-3} max(x, ||b||) (D.2, K-7), the realization using frozen coarse statuses (K-8).  Then (f, rho g) lies in the closure of
NA((c_0, p_N), l_2^2) along norm-attaining rows with finite base support; in particular (LSC-trunc)_N holds at (f, g, rho).  Proof: K2's proof with
Step 0 under (H1*), (P) as in C.1, Step A by K2.9(c) (frozen statuses), data by K1 Proposition K1.A (banked coordinates as E-coordinates of V1 TR),
Theorem UE^inf with Lemma DC^inf from K2.6, averaging by E^{eng,RT,inf} with K1-ref's (E-d) check.  Quantifier order: design -> N -> f, g, rho -> l_f -> L ->
w -> J(w) > D(L), f^r -> Step 0 -> classes -> (P) -> Lojasiewicz targets -> Pi -> Step A -> data -> s_1 -> N_w -> N'' -> Sys-DC -> approximant.
Residual (OPEN; necessary condition for NOT being covered): at all but finitely many main stages, at every clean sub-window and admissible class,
(W*) the Step-0 push problem (H1*) fails, or (A*)/(U*) Step A has a near-certificate with the structure of K2.16 (robustly negative common mode, thick
design-depth support proportional to Psi, no anchor, none of K2.17(a)-(e), one-sided mass >= c_*/2).

## H. Numerics (sanity only; r11/K2_ref_work/)
 ref_identity.py/.out: K2.2 to 2.7e-15, (2.1) to 5.2e-15, signed K2.3 never violated (63548 tests), K2.4 incl. corrected composite: rel. error 1.2e-12 (50 digits).
 ref_blockcheck.py/.out: threshold formula = convex program for |zeta|_Phi (rel. 4e-8, solver tolerance); norming identities exact (7e-16).
 ref_dc_degenerate.py/.out: K2.5 and K2.6 at exactly singular square systems (C.2).
 ref_sysA.py, ref_sysA_central.py: K2.8 (Euler 4e-10; generator actions 1.5e-5); Xt in and out of route V's regime; 15 configurations satisfying K2.17(c)/(d)
   carry no certificate.  ref_sysA2/3.py: toy without target cross terms: no degenerate point, no certificate (evidence for the Observation in D.3 only).
 ref_kappa_jump.py/.out: d kappa/d zeta_d jumps from 0 to -0.85..-0.96 when an Omega carrier crosses the threshold; A is C^1 (K-8).
 ref_dc_adversarial_attempt.py: adversarial contact-sign iteration oscillated; no output (recorded).

## I. Most valuable idea; what remains open
Most valuable idea (K2's): put the offsets into the BASE row.  Banking every design-depth contact (and raising thin coordinates) with a tiny mass theta_0
makes the targets of the d-consistency system the values of the prepared row, so every design-depth coordinate becomes a TWO-SIDED first-order resource
at the lever scale; and the exact identity u(zhat) = kappa_u + sum_F D_u sgn a + sum_{F^c} u z turns every near-null left vector of the system (a carrier
combination Psi with Psi(zhat_0) = 0 and a robust Hilbert common mode) into a robust c_s at design depth.  The result is a uniform dichotomy with design
constants: no rate objects, no bordering, no Sherman-Morrison scalars.
OPEN: (A*)/(U*) (Step-A sign obstructions) and (W*) (joint Step-0 pushes) at all large main stages; hence (LSC-trunc)_N for every f, density of
NA((c_0, p_N), l_2^2) for any N and of NA((c_0, p), l_2^2).  Inherited: the once-refereed links of the chain.  No counterexample is suggested: every
residual is a sign/cone degeneracy of the companion construction, not a property of a mate.
