# Q2 referee (a) notes (Round 10): proofs of the precisions, repairs and new observations

Refereed: r10/Q2_notes.md (and Q2_part1..4.md, Q2_work/*.py: onesided_check, prop41_check, border_check re-run with identical outputs; lt_check.out inspected).  Part files: Q2_refa_part1..4.md.  Scripts
(independent, written from scratch): Q2_refa_work/lt_adversarial.py, smass_jacobian.py, border_inverse.py, drift_check.py (+ .out / quoted output).
Setting and notation of Q2 (the note's Sections 1, 2, 7, 8; X2 Section 1-4; finite block set, p = p_N, diagonal base U k_s = mu_s e_s).
Labels: PROVED / SKETCH / HEURISTIC / OPEN / FALSE.

## A. Verdict table
| Q2 claim (Q2 label) | Verdict |
|---|---|
| Lemma 1.1 (PROVED) | correct; (p1.1) (d) needs mu non-increasing |
| Lemma LT incl. partial form (PROVED) | correct and SHARP (A.1) |
| Corollary 1.2 (PROVED) | correct; uniform in r only up to the zeroth-order term 2 alpha(M) (A.2); (p1.2) constants of the normer change are f-constants |
| Heuristic 1.4 | correctly labelled |
| Lemma M2^inf (PROVED) | correct |
| Theorem UE^inf (PROVED) | correct as a conditional theorem; (p2.1) lever radius with Pi_tr, (p2.2) S-mass range at thick coordinates, (p2.3), (p2.4) |
| Theorem E^{eng,RT,inf} (PROVED) | correct; (p2.5) must be stated with window-dependent C_+(j), c_flat(j) (B.1); holds for the design |
| Lemma 3.1 (PROVED) | correct; A_0 = 10; (p3.1) |
| Proposition 3.2 (SKETCH) | SKETCH is right |
| Lemma 3.4 (PROVED) | correct |
| 4.0 linearization (PROVED) | correct, confirmed by finite differences in an exact model (C.1) |
| Proposition 4.1 (PROVED) | correct; doubly degenerate left null vector computed (C.2) |
| Corollary 4.2 (PROVED) | correct as a conditional statement; (p3.2) Poincare-Miranda constants, (p3.3) thick S-mass range/remainder, (p3.4) zero-data hypothesis not automatic: repaired by a bank-with-offset lever (C.3) |
| Lemma 4.3 (PROVED) | (a)-(c) correct; Consequence overstated twice (C.4), repaired |
| 4.4(ii) second-order residue (PROVED) | correct when h^T D^{-1} p_m = 0 for EVERY block (p3.5); the "tolerated by UE^inf" clause is a SKETCH |
| 4.4(iii), (iv) (OPEN) | OPEN; sharpened: exact d-consistency is IMPOSSIBLE in the exact degenerate case unless an exact scalar identity holds (C.5); referee route (R3-a) (C.6, SKETCH) |
| Theorem 5.1 (SKETCH), Corollary 5.2 (SKETCH) | SKETCH is right; (p4.1) rate objects must be defined at f |
| (LSC-trunc) for every f (OPEN) | OPEN |

## B. Section 1-2 items

### A.1 Sharpness of Lemma LT (PROVED).
The base inequality proved in Lemma LT is q*(a^M + r B) <= q*(a + r B) + 2 Lambda_M(r, B) + 2||U* a_{>M}||.  The factor 2 cannot be lowered: take
j in F, j > M, B := -s_j e_j*, 0 < r <= |a_j|.  Then Lambda_M = r, ||a + rB||_1 = ||a||_1 - r and ||U*(a + rB)|| = nu - O(mu_j^2 r), so q*(a + rB) = 1 - r +
O(mu_j^2 r); and q*(a^M + rB) = q*(a^M) + r + O(mu_j r) = 1 + r + O(mu_j r).  The difference is 2r = 2 Lambda_M up to O(mu_j r + mu_{M+1} alpha(M)).
Numerically (lt_adversarial.py) the difference equals 2 Lambda_M to 7 digits; for p* with adversarial h the full (LT) is attained up to 2.7e-7.

### A.2 Non-uniformity of Corollary 1.2 in r (PROVED).
Lambda_M(r, B_r) <= min(alpha(M), |r| ||B_r 1_{(M,inf)}||_1), and nothing better holds uniformly in r.  Example: fix M, r_0 > 0 and
h := -(1/r_0) sum_{j in F, j > M} s_j |a_j| e_j*  (in l_1).  For 0 < r <= r_0 the decomposition f + r h = (a + r h) + L* w has q*(a + r h) <= 1 (the far moduli
only shrink), so p*(f + r h) <= 1, and Lambda_M(r, h) = (r/r_0) alpha(M): LINEAR in r.  At the truncated row these coordinates are contacts with z = s_j, the base
excess of r h there is sum_{j > M} (|r h_j| - s_j r h_j) = 2 r alpha(M)/r_0 (lem:bookkeeping(b)), so f^M + r h genuinely pays first order at scales r << alpha(M)/r_0.
Hence the truncation is free only at finitely many scales fixed before M (Q2's statement), never uniformly down to r = 0; this is why the violation-tolerant
route of Q2 Section 2 (N_w chosen after s_1, far usage tolerated as a violation of mass tail_W) is needed.

### B.1 Window-dependent C_+ in Theorem E^{eng,RT,inf} (PROVED).
In the proof, C_+ enters only through (c1^inf): rho c_flat C_+ <= 1/8.  With C_+ = C_+(j) one has c_flat(j) := min(c^f_flat, gamma_B/(8 rho A_2), 1/(8 rho C_+(j))),
and the proof (X2's E^eng case analysis) uses c_flat only in: (i) sum_{I_r} t_i < 2|r|/c_flat, requiring n_j c_flat(j)/K_j -> infinity; (ii) eps''_j <=
2 theta'_j T^2 <= 2 theta'_j r^2/c_flat(j)^2 for |r| > c_flat(j) T, requiring theta'_j/c_flat(j)^2 -> 0.  For the design (Q1 1.1: Q(w) >= (4 Design(L)/u(w))^{omega+20},
n(w) >= l 2^{l^3} Q(w), T_lo(w) <= 2^{-n(w)}) and Proposition 3.2's C_+(w) <= C Design(L)/u(w): c_flat(w) >= c_f u(w)/Design(L), so n c_flat/K_w >= l 2^{l^3}
Q(w) c_f u^5/(C_f Design^2) -> infinity (K_w <= C_f Design u^{-4} as in V1), and theta_w Design^2/u^2 <= C_f T^2 log(1/T) Design^2 u^{-2} -> 0 since T <= 2^{-Q(w)}.
So the theorem holds with "C_+(j), c_flat(j)" and the two displayed conditions in (E-d), (E-e').

### B.2 Lever radius and thick S-mass range in Theorem UE^inf (PROVED; (p2.1), (p2.2)).
(p2.1) X2-ref (p-DC1): r = 4 K_J (1 + 1/A_min)(delta_1 + T^4 s_1) + 8 K_J W_pull/A_min, delta_1 = max value move of the pre-row.  The truncated pre-row moves e by
||e_1 - e_0|| <= 2||U*(A_1 - a_0)||/nu_0 <= Pi_X' + Pi_tr with Pi_tr = 2||U* a_0 1_{(N_w,inf)}||/nu_0 <= 2 s_1 T^4/nu_0 and the W_F raises inside Pi_X'
(X2 Lemma M1(iv)); z is unchanged by the truncation.  Hence delta_1 <= Pi_X' + Pi_tr + (cut-off terms) and r <= K_w s_1 with K_w enlarged by an f-constant.
The pull coordinates (v_l(j_p) in [r, 2^G r]) are chosen after N_w.  Also N_w >= every S-mass lever coordinate (else the lever is truncated away).
(p2.2) An S-mass step P moves A(p) by beta_p P, beta_p = nu_1/(mu_p^2 |u_l(p)|).  Keeping |A(p)| >= |A_1(p)|/2 (needed in case (2^inf) of UE^inf's base claim
at p) for |P| <= K r is K r nu_1 <= mu_p^2 |u_l(p)| |A_1(p)|/2; with (D-lev) and |A_1(p)| >= u(w): K K_w s_1 nu Design(L) <= u(w)/2, an extra (LATE) condition,
compatible with (VT') under (W_exp).

## C. Sections 3-4 items

### C.1 Exact Jacobian of Lemma DC with thick S-mass levers (PROVED; Q2 4.0 confirmed).
Lever l of type (S-mass) at p_l in F, eps_l = sgn(A_1(p_l) u_l(p_l)), privacy p_l notin supp u_k (k in Omega, k != l).  dA(p_l) = sgn(A_1(p_l)) beta_{p_l} dP_l
gives U* dA = sgn(A_1(p_l)) beta_{p_l} mu_{p_l} k_{p_l} dP_l and de = (I - e_1 e_1^T) U* dA/nu_1, so for every carrier
      du_k(xhat) = <U* u_k, de> = sgn(A_1(p_l)) dP_l [u_k(p_l) - <U* u_k, e_1> A_1(p_l)/nu_1]/|u_l(p_l)|,
i.e. eps_k du_k = dP_l [delta_{kl} - g_k h_l], g_k = eps_k <U* u_k, e_1>, h_l = |A_1(p_l)|/(nu_1 |u_l(p_l)|) (for k notin Omega the same with eps_k dropped).
dA_m = <w_m, R_m dxhat> = sum_{all k in block m} lambda_k w_m(k) du_k = q_m^T dP - G_m h^T dP, G_m := sum_k lambda_k w_m(k) <U* u_k, e_1>.  With
p_l = eps_l u_l(zhat_0)/A_m^0: dF = dP - gt h^T dP - sum_m p_m q_m^T dP, gt = g - sum_m G_m p_m.  A block-norm lever (z-move at a private coordinate j of a peak
k*, unit step = change eps of u_{k*}(xhat)) changes no Omega value and dA_{m*} = lambda_{k*} w(k*) eps dP_0, so its column is -pi p_{m*}, pi = eps lambda_{k*} w(k*).
Numerical confirmation (smass_jacobian.py): exact one-block model (threshold equation), three strict non-peaks with thick S-mass levers (h up to 4.9), a peak
with a free private lever coordinate; finite-difference Jacobian vs formula: max relative error 9.9e-10 (194 instances); block-norm column 2.8e-9.

### C.2 The doubly degenerate bordered map (PROVED).
In Proposition 4.1, if c_alpha = beta_* = 0 then L(P, P_0) = b is solvable iff y^T b = 0 with
      y := D^{-T} ( h + sum_{m != m*} theta_m q_m ),   theta_m := h^T D^{-1} p_m / (1 - q_m^T p_m).
Proof: in the proof of Proposition 4.1 the only equation not solved for free is c_alpha alpha - beta_* gamma_{m*} = rhs, and rhs = h^T D^{-1} b + sum_{m != m*}
theta_m q_m^T D^{-1} b = y^T b; with c_alpha = beta_* = 0 solvability is rhs = 0; conversely any solution satisfies (i), (ii) with alpha := h^T P, gamma_m := q_m^T P,
which forces rhs = 0.  (border_inverse.py: rank n - 1, |y^T L| = 5e-16.)  Consequently y = D^{-T} h (Q2 4.4(ii)) iff h^T D^{-1} p_m = 0 for all m != m* -- e.g. when
block-norm levers are present in EVERY block and all their beta_*(m) vanish.  (p3.5)

### C.3 Repair of the block-norm lever when the block carries a shift (PROVED as a modification of Corollary 4.2).
Claim.  Let k* be a peak of block m* with robust margin, j in S_{k*}, j > s_max(L), j notin F_1, and suppose the window data at j are contact-like with respect to
z_1(j) (z_1(j) b^+_i(j) >= 0 >= z_1(j) b^-_i(j) for all pieces).  Then the "bank with offset" lever -- base mass m_0 := 2 K r beta_j at j with the sign of z_1(j),
lever mass m_0 + beta_j P_0 for |P_0| <= K r, beta_j := nu_1/(mu_j^2 |u_{k*}(j)|) -- satisfies the conclusions of Corollary 4.2 in place of the zero-data lever, under
the additional (LATE)-type conditions h_0 ||gt||_inf K <= 1/2, h_0 := m_0/(nu_1 |u_{k*}(j)|), and m_0 >= 8 rho s_1 max_i |b^theta_i(j)|.
Proof.  (i) Admissibility for every P_0: the mass stays in [K r beta_j, 3 K r beta_j] with the sign of z_1(j), so j is a support coordinate with z = sgn a there.
(ii) Base claim of Theorem UE^inf at j: contact-like data have zero anti-sign part on both sides, (s_j b^+_j)_- = 0 = (s_j b^-_j)_+, so (U3^inf) holds with any C_+;
the theta piece: |tau rho b^theta_j| <= s_1 rho |b^theta_j| <= m_0/8.  (iii) First-order action (X2 Lemma M1(i) at a mass off F_0): per unit P_0, u_{k*} moves by
eps (own Hilbert term beta_j mu_j^2 u_{k*}(j)/nu_1) up to the factor nu_1/nu - 1 = O(m_0^2 mu_j^2/nu^2), and every carrier k moves by the common mode
-h_0 <U* u_k, e_1> (derivative of nu/nu_A at c = m_0 is -m_0 mu_j^2/nu^2); no Omega carrier meets j (privacy).  So the bordered column is -pi p_{m*} - h_0 gt.
(iv) Writing [L | -pi p_{m*} - h_0 gt] = [L | -pi p_{m*}] + (rank one of size h_0 ||gt||), the right inverse R of Proposition 4.1 gives a right inverse
R (I + E R)^{-1} with ||E R|| <= h_0 ||gt||_inf K <= 1/2, norm <= 2K.  The rest is Corollary 4.2's proof.  (v) With (D-lev) (mu_j^2 v_{k*}(j) >= 1/Design, hence
v_{k*}(j) >= 1/Design): h_0 = 2 K r/(mu_j^2 u_{k*}(j)^2) <= 2 K r Design^2, so the condition is K^2 r Design^2 ||gt|| <= 1/4, a (LATE)-type smallness of s_1.  QED
Why needed: v = b^+ - b^- = sum_m R_m*(Domega_m - Delta_m w_m) gives every peak the coefficient -lambda_k w_m(k) Delta_m, so at j in S_{k*} beyond s_max (where among coarse
carriers only u_{k*} lives) the data are -Delta_{m*} lambda_{k*} w(k*) u_{k*}(j) + (fine): ZERO only if Delta_{m*} = 0.  If Delta_{m*} != 0, validity of the window
family forces contact-likeness at these coordinates (a free coordinate would carry the non-tolerable violation mass |Delta_{m*}| lambda_{k*} |u_{k*}(j)| summed over the
private set), which is exactly the hypothesis of the claim (this is the known "Delta d R* w z-signed on K" requirement of shifted data).

### C.4 Lemma 4.3: corrected Consequence (PROVED).
(1) If kappa = 0, then u|_F = 0; individual carriers of Lambda may meet F at shallow coordinates.  Correct statement: no carrier k in Lambda with c_k != 0 meets F
inside S_k \ [1, s_max(L)] (there u = c_k u_k by privacy).  This is what the lever argument needs.  (2) Every coarse peak k' notin Lambda has its coordinates of
S_{k'} beyond s_max(L) off F (Q2's (c), for kappa != 0); by C.3 each block with a robust-margin peak (V1 Lemma D) has a two-sided block-norm lever (zero-data
Z-gen if Delta_{m*} = 0, bank with offset otherwise).

### C.5 Exact scalar obstruction in the exact degenerate configuration (PROVED; sharpens Q2 4.4(iii)).
Setting: X = 0 (X2-ref's (R-abs) route), Lemma DC^inf with S-mass levers and block-norm levers in every block, reference row f_0 with support F_0; h fixed (the
common-mode vector at the linearization point), u_h := sum_l h_l eps_l u_l; assume h^T p_m = 0 for every block m and exact full degeneracy u_h|_{F_0} = kappa a_0|_{F_0}.
Then for EVERY lever parameter (P, P_0) (not only to first order)
      h^T F(P, P_0) = u_h(xhat(P, P_0))
                    = -(kappa nu_0/2) ||e(P, P_0) - e_0||^2 + tau_W(P, P_0) + tau_z(P, P_0),
      tau_W := sum_{s in supp a(P, P_0) \ F_0} mu_s^2 u_h(s) a(P, P_0)(s)/nu(P, P_0),     tau_z := u_h(z(P, P_0) - z_0).
Proof.  h^T F = sum_l h_l eps_l u_l(xhat) - sum_m (A_m/A_m^0) sum_{l in Omega_m} h_l eps_l u_l(zhat_0) = u_h(xhat) - sum_m A_m h^T p_m = u_h(xhat) (exact; p_l =
eps_l u_l(zhat_0)/A_m^0).  In particular u_h(zhat_0) = 0 (F = 0 at f_0).  Then u_h(xhat) = u_h(z) + <U* u_h, e> and, exactly as in Lemma 3.4 but keeping the cross
term, <U* u_h, e> = kappa nu_0 <e_0, e> + sum_{s in supp a \ F_0} mu_s^2 u_h(s) a(s)/nu, <U* u_h, e_0> = kappa nu_0, and u_h(zhat_0) = 0.  QED
Consequences.  (a) F(P, P_0) = 0 forces (kappa nu_0/2)||e - e_0||^2 = tau_W + tau_z: if kappa (tau_W + tau_z) < 0 there is NO exactly d-consistent lever setting at all.
(b) The levers of Lemma DC^inf contribute nothing to tau_W, tau_z (S-mass: support moves; Z/TU/block-norm levers: private coordinates of OTHER carriers, off supp u_h),
so tau_W = (theta-masses on W cap supp u_h) and tau_z = (cut-off beyond N''); ||e - e_0|| <= Pi_e + C r.  Hence exact solvability within the lever radius requires
|tau_W + tau_z| <= |kappa| nu_0 (Pi_e + C r)^2/2 + O(r |tau_W|): with tau_W of first order in s_1 (window coefficient C_W != 0) exact d-consistency is IMPOSSIBLE for
small s_1.  (c) The far free coordinates beyond N'' (adjustable in norm-attaining approximants) act on u_h with range <= 2 ||u_h 1_{(N'', inf)}||_1 <= C t(N'') <=
C T^4 s_1^2 (3.2(iv)): too weak for a first-order tau_W.  So a resolution must use (R3-a) below, a bank/z-move at a coordinate of supp u_h \ F_0 of usable depth, or
theta-data vanishing on W cap supp u_h (split chi = 1/2 there), or a tolerance version of UE.

### C.6 Referee route (R3-a): data-side bordering (SKETCH).
The junction mismatch of a piece is kappa^+- = -+(rho/2) sum_m sum_{k in Omega_m} Domega(k)(nv'_k - nv_k), and nv'_l - nv_l = eps_l lambda_l F_l/A_m.  Hence it suffices
to solve F(P, P_0) = lambda yhat for some scalar lambda, where yhat is any fixed vector with
      (O)  sum_{k in Omega_m} eps_k lambda_k Domega_i(k) yhat_k = 0 for every piece i and block m,   and   (Y)  y^T yhat != 0  (y the left null vector, C.2).
(Y) makes [L | -yhat] onto (the range of L is y-perp), so the Poincare-Miranda argument of Corollary 4.2 runs with the augmented right inverse; (O) gives kappa^+- = 0 for
every piece.  The residual moves the Omega values by O(lambda), |lambda| <= C (|y^T F(0)| + K^2 r^2)/|y^T yhat| = O(C_W s_1): it moves C_m, gaps and relative positions by
O(lambda) (harmless under (LATE), gap_min being in s_late), changes d'(omega^theta) by kappa_theta = O(lambda A_2/t), hence H'_m(omega^+-) by O(lambda A_2^2/t^2) (i.e.
O(lambda c_flat^2 A_2^2) on the radius |tau| <= c_flat t) and p*(g'_i - rho g_i) by O(lambda/t): all absorbed by (LATE)-type conditions; the representation identities
of UE remain exact because they involve d' - d only through Domega (check: the + piece's representation defect is (1/2)(d' - d)(Domega) sum_m R_m* w'_m).
(R3-a) fails only if, block by block, y|_{Omega_m} lies in the span of the weighted switching vectors (eps_k lambda_k Domega_i(k))_k; e.g. any S-mass carrier l with
h_l != 0 that does not switch (Domega_i(l) = 0 for all i) gives yhat := e_l.  For data on one shift ray per class (U1 Proposition 2.2), the failure set is
"h|_{Omega_m} parallel to the class ray in every block": a further degeneracy on top of (NDN2) and exact full degeneracy.  Not written line by line (status: SKETCH).

### C.7 Rate objects (PROVED; (p4.1)).
c_alpha, beta_* are evaluated at the pre-row f_1, built after the sub-window w.  Define them at f for each of the finitely many lever configurations of level L (a
design count) and include them in omega(L).  If one of them is >= u(w) at f, then at f_1 it is >= u(w)/2: f -> f_1 moves e and the values by O(mu*_J) (deep raise),
O(Design T_lo^3) (companion, V1 Lemma CO with Lam = T_lo^3) and O(K_w s_1) (pre-row), all << u(w) = b(w^-), because T_lo(w) <= 2^{-Q(w)} and
Q(w) >= u(w)^{-20}; c_alpha, beta_* are Lipschitz in these quantities with design constants.

## D. Numerics summary (sanity only)
lt_adversarial.py: (LT) max(LHS - RHS) = -2.7e-7 over 150 adversarial tests (essentially attained); partial form -6.7e-4; base-level sharpness exact.
smass_jacobian.py: 4.0 Jacobian with thick S-mass levers confirmed to 9.9e-10; block-norm column to 2.8e-9.
border_inverse.py: Proposition 4.1 right inverse residual 1.2e-13, bound ratio 3.7e-5; Woodbury determinant 4e-13; doubly degenerate left null vector of C.2 to 5e-16.
drift_check.py: Lemma 3.4 identity to 2.5e-15 (400 moves, truncations included); one-sidedness (max gain -3.3e-5 for kappa > 0); first-order action of masses on
supp u \ F.  Q2's scripts re-run: identical outputs.

## E. Most valuable idea (referee's choice)
Truncate the base support AFTER s_1: the dropped far support becomes contacts of the norm-attaining approximant whose two-sided use by the side data is a tolerated
violation of mass tail_W <= delta s_1/(64 rho), while the l_1-mass of the truncation cancels (Lemma LT / raise-transfer duality) and costs only a zeroth-order term
2(1 + ||U||) alpha_0(N_w) <= 2 theta T^2.  Hence infinite base support is NOT an obstruction of the violation-tolerant route: (LSC-trunc) at (f, g, rho) follows from
cushion-dominated window families (U3^inf) at infinite-support base rows.  The remaining infinite-F difficulty is the exactification (levers inside the support), not
the truncation.

## F. Open (referee's version)
(O-a) Proposition 3.2 for Q1's data (Lemma P projections inside the class/cube pigeonhole).  (O-b) Lever audit of Q1's construction at coordinates of S_l cap F
((L1)-(L3), Lemma DC^inf, bank-with-offset block-norm levers C.3), Step B ownership on J_fine \ F, status stability.  (O-c) Degenerate lever systems at infinitely many
levels: exact case impossible for exact d-consistency when tau_W != 0 (C.5); (R3-a) (C.6) or a tolerance variant of UE needed; quantitative near-degenerate case;
KN-1 raw holds in a degenerate raw direction.  (O-d) Bookkeeping (C.7, B.2).  (O-e) Inherited: Q1's MT VI chain (once-refereed links).
Density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2): OPEN.  No counterexample; none suggested.
