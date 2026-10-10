# K2 part 1 (Round 11): the approximant's d-consistency system at arbitrary base support -- (O-c)(i), (ii)

Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Setting and notation: paper/martin_density_note.tex (Sections 1, 2, 7, 8); X2 = r9/X2_notes.md
with X2-ref; Q2 = r10/Q2_notes.md with Q2-refa; K1 = r11/K1_part1..4.md (this round).  Finite block set I (p = p_N), diagonal base
U k_s = mu_s e_s (mu non-increasing; T_fin^* uses mu*_s = 2^{-2^{2^s}}).  A ROW is f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu),
F = supp a arbitrary, q*(a) = ||a||_1 + nu = 1, nu = ||U^* a||, e = U^* a/nu, zhat = z + U e, z = sgn a on F.
SYS-DC = the d-consistency system of X2 Lemma DC / Q2 Corollary 4.2 at the PRE-ROW f_1 of Theorem UE^inf built at the base row f_0 (the
companion): unknowns = lever parameters, equations F_l(P) = eps_l [u_l(xhat(P)) - (A_m(P)/A^0_m) u_l(zhat_0)], l in Omega := all coarse strict
non-peaks of f_0 (route V, X = 0: no absorbers).  Q2 4.0 notation: p_l = eps_l u_l(zhat_0)/A^0_m, q_k = eps_k lambda_k w^0_m(k), g_k = eps_k <U^*u_k, e_1>,
G_m = sum_k lambda_k w_m(k) <U^*u_k, e_1>, gt = g - sum_m G_m p_m, h_l = |A_1(p_l)|/(nu_1 |u_l(p_l)|) for an S-mass lever (h_l := 0 otherwise).
SYS-A = Step A of Q1 Lemma CM^tr in K1's ratio form (K1 2.4); treated in part 2.

## 1.1 Lemma K2.1 (tolerance variant of Theorem UE^inf).  PROVED.
Statement.  In Theorem UE^inf (Q2 2.4; X2 Theorem UE with X2-ref precisions) replace "the engineered approximant f' is d-consistent with f_0 on
Omega" by:
  (TOL)  for every piece i and block m:  |X_{i,m}| <= s_1,   X_{i,m} := (d'_m - d_m)(Domega_{i,m})   (the d-mismatch of the switching vector),
and add to (LATE) the condition  (LATE-tol)  C_f |Omega| A_2^2 K_w^2 s_1 <= c_late delta T^2 .
Then all conclusions of Theorem UE^inf hold (K_w enlarged by an f-constant factor): f' is norm attaining with finite base support,
p*(f' + tau g'_i) <= 1 + (tau^2/2)(1 - delta) for 0 < |tau| <= c_flat t_i, and p*(g'_i - rho g_i) <= K_w(K_w s_1 + c_fine + tail_W)/t_i.
Proof.  d-consistency enters X2's proof (and Q2's modification) at exactly four places; we list them with the replacement.
 (u1) Step 2.  The general form of thm:engineered Step 2 holds without d-consistency:
        Omega^diamond_m = rho(omega^diamond_m - d'_m(omega^diamond_m) w'_m) + kappa^diamond_m w'_m + rho(d^diamond_m - d^theta_m)(w'_m - w^0_m),
      kappa^+-_m = rho(d'_m - d_m)(omega^+- - omega^theta) = -+(rho/2) X_m, kappa^theta_m = 0.  (Identities of thm:engineered Step 2; they use
      only the two representations at f_0.)
 (u2) Step 3, blocks.  W_0 := w' + tau rho(omega^diamond - d'(omega^diamond) w') + tau kappa^diamond w' = (1 + tau kappa)(w' + t''(omega^diamond -
      d'(omega^diamond) w')), t'' := tau rho/(1 + tau kappa); since |tau kappa| <= (rho/2) c_flat t s_1 <= 1/16, every radius condition of X2 Step 3
      (kinds [1]-[3], (c4)) holds with c_flat replaced by (16/15) c_flat (absorbed into (c4)), and
        lin'_m(W^natural_m) = tau kappa^diamond_m + r_m <V^an_m - w'_m, R_m x'>/sigma'_m          (thm:engineered Step 3).
      So |lin'_m| <= (rho/2)|tau| s_1 + (delta/(64|I|))|tau| s_1 <= |tau| s_1 <= tau^2 for |tau| > s_1 (rho < 1), and lin'_m = 0 on the theta piece.
      X2 Step 4 uses lin' only through |lin'_m| <= tau^2 (in |eps_m| <= 6 K_sharp tau^2), so Step 4 and its error E <= (delta/8) tau^2 are unchanged.
 (u3) Lemma UE-1(c) "d'(omega) = d(omega), H'(omega) = (C/C')H(omega) for omega supported in Omega" is replaced by the bounds
        |d'_m(omega) - d_m(omega)| <= sum_k |omega(k)| |nv'_k - nv^0_k| <= |Omega| (A_2/t) K_w Pi,          (|omega^diamond(k)| <= A_2/t, UE-1(b),(c))
        |H'_m(omega) - (C/C') H_m(omega)| = |d(omega)^2 - d'(omega)^2|/C' <= C_f |Omega| A_2^2 K_w Pi/t^2        (|d(omega)| <= ||D omega||_2 <= A_2/t).
      In Step 5 the bracket c'h' + sum sigma' H' then acquires the relative error C_f |Omega| A_2^2 K_w Pi/T^2 <= C_f |Omega| A_2^2 K_w^2 s_1/T^2
      <= delta/32 by (LATE-tol) (Pi <= K_w s_1); X2's chain 1 - delta - delta/4 + delta/32 (Q2 (M4)) becomes <= 1 - delta - delta/4 + delta/16 <= 1 - delta.
      gap'(k) >= gap^0(k) - C K_w Pi >= gap^0(k)/2 by (LATE) (gap_min is a factor of s_late), so the statuses of Omega are kept.
 (u4) Lemma UE-1(g): g''_i - g_i acquires sum_m (d_m(omega^theta) - d'_m(omega^theta)) R_m^* w'_m, of l_1-norm <= N |Omega| A_2 K_w Pi/t_i; hence
      p*(g'_i - rho g_i) <= K_w (K_w s_1 + c_fine + tail_W)/t_i after enlarging K_w by an f-constant factor.
Nothing else in X2's proof (Steps 0'-5, Lemma UE-1(a),(b),(d)-(f)) or in Q2's modifications (M1)-(M5) uses d-consistency.  QED
Remarks.  (1) The tolerance is ABSOLUTE in s_1 (an f-constant multiple), not window-dependent: this is exactly what X2 Proposition J says is
needed.  (2) |X_{i,m}| <= (m/A'_m) ||D_m Domega_{i,m}||_2 ||F|_{Omega_m}||_2 (Cauchy-Schwarz with lambda_k = m Phi_k and nv'_k - nv_k =
lambda_k eps_k F_k/A'_m) and ||D_m Domega||_2 <= C_Delta' (U1 Lemma 2.1, Gamma <= 2), so (TOL) holds as soon as |F(P*)|_inf <= c_f s_1/|Omega|^{1/2}:
an approximate zero of Sys-DC suffices.  (3) (TOL) involves only the SWITCHING combinations (Q2-refa C.6's observation): the non-switching
components of F enter only (u3), (u4), which are (LATE)-absorbed.  Lemma K2.1 is not needed for the main results below (Theorem K2.6 gives
exact zeros) but makes them robust.

## 1.2 Lemma K2.2 (exact identity for an arbitrary combination).  PROVED.
For every row and every u in l_1 put kappa_u := <U^* u, e>/nu and D_u(s) := u(s) - kappa_u a_s (s in F).  Then (any bounded U, not only diagonal)
      u(zhat) = kappa_u + sum_{s in F} D_u(s) sgn(a_s) + sum_{s notin F} u(s) z_s .
Proof.  u(zhat) = u(z) + <U^*u, e> = sum_F u(s) sgn(a_s) + sum_{F^c} u(s) z_s + kappa_u nu, and sum_F u(s) sgn(a_s) = kappa_u ||a||_1 + sum_F D_u(s) sgn(a_s).
Since ||a||_1 + nu = q*(a) = 1 the claim follows.  QED
(Q2 Lemma 3.4 and Q2-refa C.5 are the special case D_u = 0 on F; numerics: identity_check.py, error 3.8e-14.)

## 1.3 Lemma K2.3 (resource dichotomy).  PROVED.
For every row, u in l_1 with <U^*u, e> >= 0, and every D >= 1:
      sum_{s in F, s <= D} |D_u(s)| + sum_{s notin F, s <= D} |u(s)|  >=  <U^*u, e> - u(zhat) - ||u 1_{(D, infinity)}||_1 .
Proof.  By K2.2, splitting at D and using D_u(s) sgn a_s = u(s) sgn a_s - kappa_u |a_s| for s in F, s > D:
  u(zhat) = kappa_u (1 - alpha(D)) + S_sh + R_sh + sum_{s > D} u(s) z_s,   alpha(D) := sum_{s in F, s > D} |a_s|,
with S_sh, R_sh the two sums on the left.  1 - alpha(D) = ||a 1_{[1,D]}||_1 + nu >= nu and kappa_u >= 0, so kappa_u(1 - alpha(D)) >= kappa_u nu =
<U^*u, e>; the last sum is >= -||u 1_{(D,inf)}||_1.  Rearrange.  QED
Consequence.  If <U^*u, e> - u(zhat) >= theta + ||u 1_{(D,inf)}||_1 with theta > 0, some s <= D has |D_u(s)| >= theta/D (s in F) or |u(s)| >= theta/D
(s notin F): a SINGLE coordinate of depth <= D carries a robust share.  (numerics: identity_check.py, no violation in 400 random rows.)

## 1.4 Lemma K2.4 (first-order action of elementary moves).  PROVED.
Diagonal base.  At a row, for u in l_1, the value u(xhat) changes as follows (R denotes a remainder with |R| <= C ||U^*u|| (mu_s |dm|/nu)^2 for
|dm| <= nu/(2 mu_s)):
 (i)   mass change dm at s in F (sign of a_s kept):          d u(xhat) = (mu_s^2/nu) D_u(s) dm + R;
 (ii)  new mass dm z_s at s notin F with |z_s| = 1 (bank):   d u(xhat) = (mu_s^2/nu) u(s) z_s dm + R;
 (iii) change dz of z at s notin F (|z_s + dz| <= 1):        d u(xhat) = u(s) dz  (exactly; e unchanged).
Proof.  U^*A changes by mu_s dm k_s, and e = U^*A/||U^*A|| has derivative (mu_s dm/nu)(k_s - e_s e), e_s = <e, k_s> = mu_s a_s/nu; the second
derivative of x -> x/||x|| is <= 3||dx||^2/||x||^2.  <U^*u, k_s - e_s e> = mu_s u(s) - (mu_s a_s/nu) kappa_u nu = mu_s D_u(s).  (ii) is (i) with a_s = 0.
(iii): xhat = z + Ue.  QED  (numerics: fo_check2.py, 60 digits, relative error 2e-16.)
Note: (i) with u = u_k reproduces Q2 4.0's column eps_k(delta_{kl} - g_k h_l) for an S-mass lever (Q2-refa C.1).

## 1.5 Lemma K2.5 (the combination seen by a left vector).  PROVED.
Sys-DC at the pre-row f_1 of the base row f_0.  For y in R^Omega put beta_m := y^T p_m and
      Psi_y := sum_{l in Omega} y_l eps_l u_l - sum_m beta_m R_m^* w^0_m   in l_1     (w^0_m: the norming functionals of f_0).
 (a) Psi_y(zhat_0) = 0 for EVERY y.
 (b) For every elementary move delta of 1.4 at f_1 (or any lever composed of such moves), the column c(delta) := dF(delta) satisfies
      y^T c(delta) = l_delta(Psi_y) + err,   |err| <= C |delta| ||y|| (K_w Pi + c_{L+1}),
     where l_delta(u) is the first-order change of u(xhat) given by 1.4 (linear in u).
 (c) <U^*Psi_y, e_1> = y^T gt + O(||y|| (K_w Pi + c_{L+1})).
Proof.  (a) eps_l u_l(zhat_0) = A^0_m p_l, so sum_{l in Omega_m} y_l eps_l u_l(zhat_0) = A^0_m beta_m; and (R_m^* w^0_m)(zhat_0) = <w^0_m, R_m^{**} zhat_0> =
A^0_m because w^0_m norms zeta^0_m = R_m^{**} zhat_0 (forced decomposition, |w^0_m|_m^* = 1).  Subtract.
(b) dF_l = eps_l du_l - (dA_m/A^0_m) eps_l^2 u_l(zhat_0) ... = eps_l du_l - p_l dA_m (eps_l^2 = 1); du_l = l_delta(u_l); A_m = |R_m xhat|_m is smooth
(Martin Lemma A(d)) with derivative <w^1_m, R_m dxhat> at f_1, i.e. dA_m = l_delta(R_m^* w^1_m) + O(|delta|^2).  So y^T c(delta) = l_delta(Psi_y) +
sum_m beta_m l_delta(R_m^*(w^0_m - w^1_m)), and ||R_m^*(w^0 - w^1)||_1 <= sum_k lambda_k |w^0(k) - w^1(k)| <= K_w Pi + 2 c_{L+1} (X2 Lemma UE-1(d)).
(c) <U^*Psi_y, e_1> = sum y_l eps_l <U^*u_l, e_1> - sum beta_m <U^* R_m^* w^0_m, e_1> = y^T g - sum_m beta_m G_m + (same error) = y^T gt.  QED
Meaning.  Every possible degenerate direction of Sys-DC is a combination Psi of carrier vectors whose VALUE at the base row vanishes, while its
Hilbert projection <U^*Psi, e> is the common-mode coefficient y^T gt.  Lemma K2.3 then locates a resource.

## 1.6 Definition (prepared companion).
Level L, clean sub-window w, b := b(w), u := u(w), T := T_lo(w).  D(L) := the least D >= d(L) (K1's near depth) with
      max_{k carrier of stage <= L} ||u_k 1_{(D, infinity)}||_1 <= 2^{-L^2} H(L)^{-4},   H(L) := 2^{d(L)}/delta_min(L)
(a design number of stage L: the vectors u_k of stages <= L are fixed at stage L; H(L) does not involve Design(L)).  U_L := union of supp u_k over
coarse carriers k (stages <= L).  theta_0 := b/Design(L)^{C_P}.
PREPARATION (P), inserted in Q1 Lemma CM^tr after Step 0 (V1 (C1), (C2)) and the deep raise (J(w) > D(L)), before Step A's Lojasiewicz step:
 (P1) every s <= D(L), s in U_L, free with tiny room (1 - |z_s| <= b; a rate object, see part 3) is closed to a contact (as V1 (C1), (C2));
 (P2) every contact s <= D(L), s in U_L, that is not one of Step A's or Sys-DC's designated lever coordinates (K1 2.3 bookkeeping) receives the bank
      mass theta_0 z_s; in the class cones these coordinates keep their contact rows (data z-signed);
 (P3) every s <= D(L) in F cap U_L with |a_s| < theta_0 is raised (same sign) to |a_s| = theta_0.
PROPERTIES (PROVED).  (a) Cost: p*(f^P - f^r) <= C D(L) theta_0 log(1/theta_0) + C_f p*(L^*(w^P - w^r)) <= b log(1/b) = o(T^2) (V3 Lemma 2.3 /
Corollary 2.4 for (P3); V1 Lemma B / Theorem E'' for banks off F; Z3 Lemma 3.1 for the normer change).  (b) Values move by <= C D(L) theta_0 <= b
(K2.4, |u_k(s)| <= 1), statuses and robust objects by <= Lip b: the clean classification survives with factor 2, and (D1) of X1 2.6 holds after
doubling b in its definition (a design adjustment, part 3).  (c) Data: at banked coordinates the transplanted data are contact-like (cone rows kept;
V1 TR Step 5: b^+ = chi V', b^- = -(1-chi)V' there), so (U3^inf) holds with any C_+; at raised thin coordinates K1's data are clamped/cushion-
dominated (K1 part 1) and a larger modulus only helps; the theta piece is protected at banked/raised coordinates once s_1 <= theta_0 T/(8 rho A_0)
(a (LATE) condition).  (d) TYPES at the companion f_0 (after Step A): every s <= D(L), s in U_L, is
   S_theta: support with |a_s| >= theta_0 (thick, banked, raised, or a Step A TU bank -- whose final mass is >= beta x/4 by the pull overshoot,
            K1 2.1(b));
   FR:      free with room >= u (zero data, or tolerated violations with b^theta = 0);
   ZD:      a zero-data coordinate (Step A's (P1) levers, K1 2.0), contact or free.
 Proof of (d): design-depth coordinates of U_L are contacts, free or support; (P1)-(P3) and Step A leave exactly these types; Step A's pull
 coordinates have v ~ x_A, hence depth > D(L) (T <= 2^{-Q(w)}, D(L) a design depth).

## 1.7 Theorem K2.6 (Sys-DC is uniformly solvable after preparation).  PROVED (modulo the refereed machinery of X2/Q2 and K1's Step A).
Let L >= l_f, w a clean sub-window, f_0 the prepared companion of 1.6 after Step A (Q1 CM^tr / K1 Lemma K1.6(A)), and f_1 any pre-row of Theorem
UE^inf at f_0.  Let C be the column matrix of Sys-DC at f_1 formed by (i) the lever of every l in Omega (K1 2.3: (P1)-(P4)), (ii) one elementary
resource at every s <= D(L), s in U_L (S_theta: mass change; FR, ZD: z-move), and (iii) a mass change at every thick s <= D(L) in F_1 \ U_L
(K1's anchors (P5)).  Then
      s_min(C) := min_{||y||_2 = 1} ||C^T y||_2  >=  eps_DC := c_f mu*_{D(L)}^2 / (D(L) H(L)^2 (1 + 4N/A_min)) ,
a design number times an f-constant; hence C has a right inverse R with ||R||_inf <= K_DC := (number of columns)^{1/2}/eps_DC <= Design(L)^{C_0}
(Design(L) >= 2^{D(L)}/mu*_{D(L)}^2, part 3).  Consequently Lemma DC^inf holds at f_1 with K_J replaced by K_DC and WITHOUT any hypothesis on
c_alpha, beta_*, Sherman-Morrison denominators, spreads or anchors: F has a zero P*, |P*|_inf <= K_DC r, every Omega carrier is a strict non-peak
with nv = nv^0 exactly, the coarse peaks keep their statuses, and the moved masses keep |a| >= theta_0/2 at S_theta coordinates.
Proof.  Suppose ||C^T y||_2 < eps for a unit y; we show eps >= eps_DC.  Write gamma := y^T gt, beta_m := y^T p_m.
Step 1 (shape of y).  Every l in Omega has a column of the form  c_l = e_l - h_l gt - p_{m(l)} q_l + E_l  in normalized units (unit step = unit
change of eps_l val_l at first order), with h_l = |a(p_l)|/(nu v_l(p_l)) <= H(L)/nu for an S-mass lever (P4), and h_l <= C theta_0 H(L) or
h_l <= eta' Design^C (banked, TU-bank: masses <= beta x) or h_l = 0 (Z-levers, Hilbert pairs) otherwise, ||E_l|| <= C Design^C (x + K_w Pi) (Q2 4.0,
K1 2.1(a)-(d), K2.4).  Hence, from |y^T c_l| < eps:
      y_l = beta_{m(l)} q_l + gamma h_l + e_l',   |e_l'| <= eps + C Design^C (x + theta_0) |gamma|.
Step 2 (gamma is robust).  beta_m = y^T p_m = beta_m q_m^T p_m + gamma h^T p_m + O(e'), and 1 - q_m^T p_m >= 1/2 (q_m^T p_m <= C_m <= 1/2, X2 2.2(3)),
so |beta_m| <= 2(|gamma| ||h||_2 ||p_m||_2 + ||e'||_2 ||p_m||).  With ||q_m||_2 <= 1, ||p_m||_2 <= 2|Omega|^{1/2}/A_min:
      1 = ||y||_2 <= |gamma| ||h||_2 (1 + 4N |Omega|^{1/2}/A_min) + C N |Omega| ||e'||/A_min,
so |gamma| >= 1/(2 ||h||_2 (1 + 4N|Omega|^{1/2}/A_min)) =: gamma_min > 0 once eps <= c/(N |Omega|/A_min) (otherwise eps >= eps_DC already).
In particular h != 0: if every Omega carrier is privately tunable, Sys-DC is uniformly regular (K1 Lemma K1.5(a)).  Replace y by -y if needed:
gamma > 0.
Step 3 (the combination).  By K2.5, Psi_y(zhat_0) = 0 and <U^*Psi_y, e_1> = gamma + O(K_w Pi + c_{L+1}).  Split Psi_y = Psi^c + Psi^f, Psi^f := the
fine-carrier part of -sum beta_m R_m^* w^0_m, ||Psi^f||_1 <= sum_m |beta_m| sum_{k > L} lambda_k <= C |gamma| ||h|| c_{L+1}.  The coefficients of Psi^c
are bounded by |y_l| + sum_m |beta_m| lambda_k <= C |gamma| H(L) |Omega| N/(nu A_min), so by the choice of D(L),
      ||Psi^c 1_{(D(L), inf)}||_1 <= C |gamma| H(L) |Omega| N/(nu A_min) * 2^{-L^2} H(L)^{-4} <= gamma/16      (L >= l_f).
At f_1: Psi^c(xhat_1) = Psi_y(zhat_0) + (Psi_y(xhat_1) - Psi_y(zhat_0)) - Psi^f(xhat_1) = O(||Psi_y||_1 delta_1 + |gamma| ||h|| c_{L+1}) <= gamma/16
(delta_1 <= K_w Pi, (LATE)); <U^*Psi^c, e_1> >= gamma - gamma/16.
Step 4 (resource).  Lemma K2.3 at the row f_1 with u := Psi^c, D := D(L): some s <= D(L) has
      |D_{Psi^c}(s)| >= gamma/(2 D(L))  (s in F_1)      or      |Psi^c(s)| >= gamma/(2 D(L))  (s notin F_1).
If s notin U_L then Psi^c(s) = 0, so s is in F_1 with |D_{Psi^c}(s)| = kappa |a_s|, kappa = <U^*Psi^c, e_1>/nu_1 <= 2 gamma/nu_1, whence |a_s| >=
nu_1/(4 D(L)) >> b: s is THICK (clean dichotomy of the moduli, part 3), i.e. an anchor (iii).  (Thin s <= D(L) in F_1 \ U_L contribute at most
kappa b each to Lemma K2.3's left side, D(L) kappa b in total, which is absorbed in gamma/16.)  If s in U_L: at f_1 design-depth coordinates
have the types of f_0 (theta-masses sit at contacts deeper than D(L), because all design-depth contacts of U_L are banked or designated;
truncation acts beyond N_w > D(L)), so s is S_theta, FR or ZD by 1.6(d).
Step 5 (contradiction).  By K2.5(b) and K2.4 the elementary column c_s at s satisfies
      |y^T c_s| >= (mu_s^2/nu)|D_{Psi_y}(s)| - err >= mu*_{D(L)}^2 gamma/(4 D(L) nu)        (S_theta or anchor, unit mass),
      |y^T c_s| >= |Psi_y(s)| - err >= gamma/(4 D(L))                                        (FR, ZD, unit z),
(Psi_y - Psi^c has |.(s)| <= ||Psi^f||_1 tiny).  Hence eps > |y^T c_s| >= mu*_{D(L)}^2 gamma_min/(4 D(L) nu) >= eps_DC.  This proves the singular value
bound; R := C^T (C C^T)^{-1}.
Step 6 (nonlinear solve).  X2 Lemma DC step (4) / Q2 Corollary 4.2 with the right inverse: G(y) := F(R y) = F(0) + y + Rem(R y) on the cube
|y|_inf <= r; on the face y_l = r, G_l >= r - |F(0)|_inf - C_2 ||R||^2 r^2 >= 0 when K_DC |F(0)|_inf <= r/2 and C_2 K_DC^2 r <= 1/4; symmetric on y_l = -r;
Poincare-Miranda gives a zero.  C_2 is a design constant (second derivatives of K2.4 at depth <= D(L) and of the levers, K1 2.1).  Ranges: every
resource moves by <= K_DC r in its own units; S_theta needs K_DC r beta <= theta_0/2 (beta <= Design/nu), FR needs K_DC r/u <= room/2, the levers
of K1 2.3 as there -- all contained in (LATE) because r <= C K_w s_1 and s_1 <= s_late with s_late containing (theta_0 u/(K_w Design))^C (part 3).
Statuses: values move by <= C_lev K_DC r << min(gap_min, robust margins) (Q1 Lemma PM (v), (LATE)).  Exactness on Omega is F(P*) = 0.  QED
Remarks.  (1) No pigeonhole/rate object is used for c_alpha, beta_*, 1 - h^T g, spreads or anchors: Steps 2-5 are a UNIFORM dichotomy.  The block-norm
levers (P6) of K1 and the bordering of Q2 Proposition 4.1 are not needed (they may be added as further columns).  (2) The resource found in Step 4
is never an S-mass lever coordinate p_l itself: there D_{Psi_y}(p_l) = (y^T c_l)(nu v_l(p_l)/mu^2...) is small by Step 1.  (3) Why preparation is
needed: without (P2) the resource could be a data-carrying contact, where only a bank (one direction) is available; K1 2.2 shows that a bank placed
at the PRE-ROW cannot be made two-sided by an offset (the forced total position y^T F(0)/(y^T c) has an uncontrolled sign).  In (P2) the offset is
part of the BASE ROW f_0, whose values are the targets of Sys-DC, so the forced position is theta_0 + O(K_DC r) > 0.

## 1.8 Corollary K2.7 (the degenerate configurations of Q2 / Q2-refa / K1 at the approximant).  PROVED.
(a) Q2 4.4(i)-(iii) and Q2-refa C.5, C.6: (NDN2), its quantitative version, and the exact degenerate configuration are covered by Theorem K2.6:
    after preparation Sys-DC has an exact zero with design constants.  Neither the data-side bordering (R3-a) nor the tolerance variant is needed;
    the "exceptional case" (left null vector blockwise in the span of the switching vectors) needs no separate treatment.
(b) Why C.5's obstruction disappears.  At an UNPREPARED base row in C.5's configuration (X = 0; h^T p_m = 0 for all m; exact full degeneracy
    u_h|_{F_0} = kappa a_0|_{F_0}; c_alpha = 1 - h^T g = 0), Lemma K2.2 gives 0 = u_h(zhat_0) = kappa + 0 + sum_{s notin F_0} u_h(s) z_s with kappa =
    <U^*u_h, e_0>/nu_0 = 1/nu_0, hence ||u_h 1_{F_0^c}||_1 >= 1/nu_0 >= 2 (nu_0 <= ||U|| <= 1/2), and its part beyond D(L) is <= 1/16: the configuration
    REQUIRES off-support mass of u_h at design depth.  C.5's tau_W lives exactly there (theta-masses at data-carrying contacts of supp u_h).  After
    (P2) those contacts are S_theta coordinates with D_{u_h}(s) = u_h(s) - kappa theta_0 z_s != 0, so the prepared row is NOT exactly fully degenerate,
    C.5's identity does not apply, and K2.6 Step 4 finds them as resources.
(c) K1's (U) and (S) carriers (K1 2.7) cause no failure of Sys-DC after preparation: (U)-carriers have a near S_theta (banked) coordinate, i.e. a
    private two-sided lever relative to f_0; (S)-carriers produce at most the degenerate direction handled by Steps 2-5.
(d) The tolerance variant K2.1 shows moreover that an approximate zero with |F|_inf <= c_f s_1/|Omega|^{1/2} would suffice.
Consequence for K1.  In K1's lever-regularity (LR_{w,a}) (K1 2.4) the Sys-DC half holds automatically (after (P)); only Sys-A remains (part 2).

## 1.9 Numerics (sanity only; K2_work/)
 identity_check.py: Lemma K2.2 exact to 3.8e-14 (400 random rows); Lemma K2.3 never violated (all depths D).
 fo_check2.py (mpmath, 60 digits): Lemma K2.4 (i), (ii) relative error 1.9e-16.
 psi_check.py -> psi_check.out (exact one-block Martin-type model, threshold equation, diagonal base; adapted from Q2-refa's smass_jacobian.py):
   (a) max |Psi_y(zhat_0)| = 2.8e-16 over random y;  (b) for 3468 elementary moves (support masses, banks, z-moves) the finite-difference
   column satisfies y^T c = l_delta(Psi_y) to relative 2.9e-5 (step 1e-7);  (c) Lemma K2.3 with u = Psi_y: no violation.
