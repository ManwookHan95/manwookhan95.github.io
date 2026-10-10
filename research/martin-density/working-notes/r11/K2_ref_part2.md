# K2 referee, part 2: the preparation (P), Theorem K2.6, Corollary K2.7

## 1. Preparation (P) (K2 4.1).  VERDICT: correct, with three precisions.
(a) Cost.  Every (P)-move is a zeroth-order move of size <= theta_0 at <= D(L) coordinates, so the crude bound p*(f^P - f^r) <= q*(a^P - a^r) +
    C_f c(delta) (Z3 Lemma 3.1, delta = xhat^P - xhat^r, every value moving by <= C D(L) theta_0/nu) gives p*(f^P - f^r) <= C_f D(L) theta_0
    log(e/theta_0); hypothesis (a) of Theorem E^{eng,RT,inf} then holds with lambda = 1, eps' = this cost (no raise transfer is needed; V3 Lemma 2.3
    may be used for (P3) but is not necessary).  With theta_0 = b/Design^{C_P}, b <= T^4, log(1/b) <= C log^3(1/T): cost/(u T)^2 -> 0.  Correct.
(b) Values move by <= C D(L) theta_0/nu (K2.4(i),(ii), |u(s)| <= 1); tiny objects move by <= Lip D theta_0 << b, robust ones stay robust; doubling
    b in (D1), (D2) (K2-e) covers the Lojasiewicz radius.  Correct.
(c) Data at banked coordinates ((R1) of K2 8).  CHECKED.  A (P2)-banked coordinate j was a contact of f^r; the class cone at f^r carries its (X1)
    contact row (U1's cone on E_c; K1 2.1(b); K1 1.3 for tiny support in T(L)), so the switching vector V_t(j) is z_j-signed; V1 TR Step 5 treats
    support of the companion that is not support of f^r exactly as contacts ("banks need not be contacts of f", V1 Theorem E''): b^+ = chi V' + (base
    term), b^- = -(1 - chi) V' + (base term), with the base term -kappa a^#/a^#(zhat^#) of modulus <= C_f t theta_0 at j (Q2 Lemma 3.1: |kappa| <=
    C(K_U + N K_P + 1) t).  Hence the anti-sign parts are <= C_f t theta_0 <= C_f theta_0/t, i.e. (U3^inf) holds at j with C_+ = max(5, C_f), an
    f-constant (E^{eng,RT,inf} accepts it; c_flat >= c_f u is unchanged); fine-origin violations at j (<= C Design
    c_{L+1}, K1-ref Lemma K1.S) are << theta_0/T and count as support violations (Q1-refa P3).  The theta piece: (L-K2-1) gives theta_0 >= 8 rho s_1
    max_i |b^theta_i(j)|, so j is not in W_F and |tau rho b^theta_j| <= theta_0/8.  So (R1) holds; "aligned" is exact up to the base term.
(d) Types (4.1(d)).  Correct: after (P1)-(P3) every design-depth coordinate of U_L is TS, S_th (support with |a| >= theta_0/2) or FR, with ZD as
    a sub-label; at f_1 the only contacts of U_L at depth <= D(L) are ZD coordinates moved there by Step A (data zero, composite move two-sided);
    the deep raise, the pulls and the truncation act beyond D(L) (J(w), N_w > D(L); pull depths v in [x, x'_max] are far beyond the design
    depth because x <= T^4 and v_k(s) >= v_min(L) >= 1/Design(L) on [1, D(L)]).
Precision (P-1).  4.1(d)'s phrase "S_th with data only raised" must be read at the scale of Step A: S_th masses can move by <= theta_0/2 both
ways, which is negligible at the scale x; K2 uses exactly this.  Precision (P-2): K2.4's composite at a ZD coordinate left by Step A with a small
mass m has a slope mismatch <= Design m between its two branches (part 1, 3); harmless if m <= Design K_DC r, otherwise use the mass branch.

## 2. Theorem K2.6.  VERDICT: correct (PROVED modulo the cited machinery), with precisions.
Re-derivation of the six steps.
Step 1.  For l in Omega the normalized lever column is e_l - h_l gt - p_{m(l)} q_l + E_l: own part from K2.4 (private coordinate beyond s_max(L),
  allowedness (c)), common mode -g_k h_l with the SIGNED h_l = eps_l a_s/(nu_1 v_l(s)), block-norm part -p_k dA_m with dA_m = q_l - G_m h_l (all
  carriers of the block in G_m); I re-derived dF_k/dP_l = delta_{kl} - h_l (g_k - G_{m(k)} p_k) - p_k q_l 1[m(k) = m(l)] (= Q2 4.0).  E_l collects
  f_1-versus-f_0 data (K_w Pi) and fine carriers (c_{L+1}).  Every l in Omega has such a lever: zero-data l with an off-F/thin near coordinate:
  ZD composite (h = 0 or <= theta_0 H/nu); data-carrying l with an off-F near coordinate: that coordinate is a contact of the data sign (a free
  one would force c_l = 0, K1 2.1(b)) and is banked, S_th lever; thin near coordinates of data-carrying l carry the data sign (K1 Lemma K1.3(S))
  and are raised, S_th lever; all near coordinates thick: (P3)/(P4).  Exhaustive.
Step 2.  In route V, D = I.  y = sum_m beta_m q_m + gamma h + e', beta_m(1 - q_m^T p_m) = gamma h^T p_m + e'^T p_m (blocks disjoint), q_m^T p_m <= C_m
  <= 1/2 (sum over Omega_m of Phi^2 w^2/C <= C), ||q_m||_2 <= 1, ||p_m||_2 <= 2|Omega|^{1/2}/A_min: 1 <= (|gamma| ||h|| + ||e'||)(1 + 4 sum_m ||p_m||
  ||q_m||).  So gamma is robust unless e' is (then eps is already large).  Correct (K2's constants are conservative).
Step 3.  Psi_y(zhat_0) = 0 exactly (K2.5(a)).  PRECISION (P-3): the inequality "||xhat_1 - zhat_0||_inf <= K_w Pi" is false as written: the
  pre-row has z_1 = z_0 1_{[1,N'']}, so xhat_1 - zhat_0 has sup norm up to 1 beyond N''.  The quantity actually needed is
     |Psi_y(xhat_1) - Psi_y(zhat_0)| <= ||U^* Psi_y|| ||e_1 - e_0|| + ||Psi_y 1_{(N'',inf)}||_1 <= C (K_w Pi + t(N'')),
  which is what K2 uses (Psi_y is a finite combination of coarse carriers plus a fine part of mass <= C c_{L+1}; N'' > N_w > D(L)).  The tail
  estimate beyond D(L) follows from the definition of D(L) and gamma >= gamma_min for L >= l_f.  Correct after this rewording.
Step 4.  K2.3 at f_1 with u = Psi^c (kappa >= 0): sum_{s <= D} |c_s| >= (13/16) gamma.  Off U_L: c_s = 0 (s notin F_1) or -kappa |a_1(s)|; thin ones
  total <= 2 D kappa b << gamma/16; a coordinate with |c_s| >= gamma/(2D) off U_L has |a_1(s)| >= nu_1/(4D) >> 2b, so it is thick (an anchor) by the
  depth-D(L) clean dichotomy (Lemma K2.13).  In U_L every design-depth coordinate carries a two-sided elementary column (1(d)).  Correct.
Step 5.  |y^T c_s| >= eff_s |c_s(Psi_y)| - err (K2.5(b) + K2.4; for z-moves |Psi(s)| >= |c_s|), eff_s >= mu*_{D(L)}^2.  Correct.
Step 6.  Poincare-Miranda on the cube in the y-variables with the minimal-norm right inverse R = C^T(CC^T)^{-1}.  PRECISION (P-4):
  ||R||_{inf->inf} <= |Omega|^{1/2}/s_min(C) (number of ROWS); K2 writes (number of columns)^{1/2} -- also an upper bound since #columns >= #rows.
  The remainder constant C_2 is a design constant (second derivatives at depth <= D(L)); ranges via (L-K2-2), (L-K2-3).  Correct.
Interface with Theorem UE (r9/X2_notes 3.4-3.5).  X2's (U6)/(SEP) is a sufficient condition for the special form J = I - pq^T; the proof of
Theorem UE uses the levers only through (i) Lemma DC's conclusions (exact zero, sizes <= C_2 r, statuses), (ii) Step 3 (Base) protection of lever
coordinates and (iii) Lemma UE-1(b)-(d).  With K2's columns: (ii) the elementary columns act at coordinates whose data are cushion dominated
(TS, anchors), aligned (S_th) or zero (FR, ZD), so the base claim of UE^inf holds there (class (2^inf) of Q2 2.4 for support, X2's free/contact
classes otherwise); (iii) coarse carriers meeting the new columns keep their statuses, so UE-1(d)'s Bregman bound keeps its form with Pi
enlarged by C_lev K_DC r.  So Theorem UE^inf holds with K_DC in place of K_J.  Correct.
Numerics (K2_ref_work/ref_dc_degenerate.py, one-block exact Martin model, six models with an EXACTLY singular square (P4) lever system,
s_min(square) ~ 1e-11):  Psi_y(zhat_0) ~ 1e-16, gamma = 0.081..0.088 (robust), D_Psi = 0 at the lever coordinates (exact full degeneracy on F),
identity error 1e-16, the off-support sum of Psi z equals -kappa (the forced off-support mass); K2.5(b) on finite-difference columns to 5e-8.
PREPARED rows (all contacts of the carriers' supports banked): s_min(enlarged two-sided matrix) = 0.072..0.130 for theta_0 = 1e-2, 1e-4, 1e-6
(no degradation as theta_0 -> 0; the square part has s_min ~ theta_0), proof bound eps_DC ~ 7e-8; Newton with the minimal-norm right inverse
solves F = 0 from perturbations of BOTH signs along the degenerate direction (residual 1e-16, two iterations) and every banked mass stays >=
0.76 theta_0.  In these random models the unprepared banks had mixed signs (one-sided correction possible); an adversarial sign iteration
oscillated (ref_dc_adversarial_attempt.py) -- the unprepared obstruction itself rests on Q2-refa C.5 and K1-ref's nonlinear test.

## 3. Corollary K2.7.  VERDICT: correct after rewording (a).
(a) PRECISION (P-5): "(NDN2), its quantitative version, the exact full degeneracy, the exceptional case and R-7's (P4)-type degeneracy do not
    arise after preparation" must read: "they may still occur for the SQUARE lever system, but they are irrelevant: the enlarged two-sided
    column system of Theorem K2.6 has a right inverse with design constants".  (Numerics: at prepared rows the square system has s_min ~ theta_0.)
(b) Re-derived: in C.5's configuration h^T p_m = 0 gives c_alpha = 1 - h^T g = 1 - kappa nu_0, so c_alpha = 0 iff kappa = 1/nu_0; K2.2 then gives
    sum_{F_0^c} u_h z = -1/nu_0 and ||u_h 1_{F_0^c}||_1 >= 1/nu_0 >= 16 (||U|| = mu*_1 = 1/16); the part beyond D(L) is <= ||h||_1 2^{-L^2}
    (|Lambda_L| H(L))^{-4}.  After (P2) the design-depth contacts carrying this mass are support coordinates with two-sided mass changes, and
    Q2-refa C.5's identity (whose hypotheses exclude moves at supp u_h \ F_0) does not constrain the enlarged system.  Correct; the explanation
    is heuristic, the proof is Theorem K2.6.
(c), (d) Correct.  The data-side bordering (R3-a) is indeed not needed.
