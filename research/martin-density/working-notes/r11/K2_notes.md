# K2 notes (Round 11): degenerate lever systems at arbitrary base support -- items (O-c), (O-d) of ADDENDUM 10, combined with K1

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED" means: proved here, modulo the refereed results cited (X2 + X2-ref, Q1 + Q1-ref
a/b + cert0-3, Q2 + Q2-ref a, K1 + K1-ref; several links of that chain have had one referee pass, as recorded there).  This file supersedes
r11/K2_part0..3.md where they differ.  Changes made while assembling: the preparation now banks EVERY design-depth contact of U_L (so Sys-DC
needs no TU levers and no "designated" coordinates); the common-mode coefficient h is SIGNED; Proposition K2.10 of part 2 is sharpened to
Theorem K2.16; K1-ref's corrections R-6, R-7, R-8, R-10 are built in.  Numerics: r11/K2_work/ (sanity checks only).

## 0. Bottom line
(1) SYS-DC IS SETTLED.  The d-consistency system of the engineered approximant (X2 Lemma DC / Q2 Corollary 4.2) has, after a cheap
    PREPARATION of the companion (banks of mass theta_0 at the design-depth contacts, raises of thin coordinates, closing of tiny rooms), a
    column matrix whose smallest singular value is >= eps_DC, a design number times an f-constant (Theorem K2.6).  This covers Q2's (NDN2), its
    quantitative version, the exact full degeneracy of Q2-refa C.5, the "exceptional case", K1's (S)/(U)/(M) carriers in Sys-DC and K1-ref
    R-7's (P4)-type block-norm levers.  No bordering, no new rate object for c_alpha, beta_*, c'_alpha, beta'_*, Sherman-Morrison denominators
    or spreads.  The tolerance variant of Theorem UE^inf with |kappa^+-| <= s_1 is proved as well (Lemma K2.1) but is not needed.  The
    data-side bordering (R3-a) is neither proved nor needed.
(2) SYS-A IS REDUCED TO A SIGN CLASS.  Step A is solvable whenever the needed correction lies, with a margin, in the cone of the available
    two-sided and one-sided resources with design weight (A-regularity; Lemma K2.9: Brouwer with a minimal-norm nonnegative selection; this
    also makes K1's "ratio trick" rigorous).  Theorem K2.16: every near-certificate against A-regularity has a ROBUSTLY NEGATIVE common mode,
    and then the whole thick support of the row at design depth is proportional to the certificate's combination Psi = sum coef_k u_k.
    Consequently (Corollary K2.17) the Step-A resources POSITIVELY SPAN -- Step A is solvable for every right-hand side -- at every stage with
    an anchor at depth <= D(L), or a thick and a free/zero-data coordinate private to the same coarse carrier, or a thick and a banked/raised
    data coordinate of the same sign private to the same carrier, or two thick private coordinates of one carrier with robust spread.  "KN-1
    holds in a degenerate raw direction" is not a separate obstruction (5.5).
(3) (O-d) IS SETTLED.  All new objects are design-countable, N-free and well founded (Section 6); the new (LATE) conditions hold with the s_1
    of Lemma S2c^tr; all new costs satisfy theta'/c_flat^2 -> 0 (K1-ref R-6).
(4) COMBINATION (Theorem K2.15).  (LSC-trunc)_N holds at (f, g, rho) as soon as, at infinitely many main stages, Step A is A-REGULAR and every
    active weak peak of Step 0 has a push resource (K1-ref R-8).  Remaining class (OPEN): rows for which, at all large main stages, Step A has a
    near-certificate of the form of Theorem K2.16 (types (A*), (U*)), or some active weak peak has no push resource (type (W)).  Density of
    NA((c_0, p_N), l_2^2) for any N and of NA((c_0, p), l_2^2): OPEN, reduced to this class.  No counterexample; nothing found points to one.

| # | Result | Status | Section |
|---|---|---|---|
| 1 | Lemma K2.1 (tolerance variant of Theorem UE^inf) | PROVED | 3 |
| 2 | Lemma K2.2 (exact identity), K2.3 (resource dichotomy), K2.4 (first-order actions) | PROVED | 2 |
| 3 | Lemma K2.5 (left combinations of Sys-DC) | PROVED | 4.2 |
| 4 | Theorem K2.6 (Sys-DC uniformly solvable after preparation) | PROVED | 4.3 |
| 5 | Corollary K2.7 ((O-c)(i), (ii); exceptional case; C.5; R-7 scalars not needed) | PROVED | 4.4 |
| 6 | Lemma K2.8 (Euler combination of Sys-A) | PROVED | 5.1 |
| 7 | Lemma K2.9 (cone realization of Step A) | PROVED | 5.2 |
| 8 | Theorem K2.16 (structure of Step-A obstructions: robust negative common mode, proportional thick support) | PROVED | 5.3 |
| 9 | Corollary K2.17 (positive spanning under anchor / private-thick / same-sign / robust-spread conditions; bordered and ratio-trick cases) | PROVED | 5.4 |
| 10 | (O-c)(iii): KN-1 holds in a degenerate raw direction is not a separate obstruction | PROVED | 5.5 |
| 11 | Proposition K2.11 (far pushes/pulls versus certificates; concrete form of (A*), (U*)) | SKETCH | 5.6 |
| 12 | Lemmas K2.12-K2.14, costs ((O-d) bookkeeping) | PROVED | 6 |
| 13 | Theorem K2.15 ((LSC-trunc)_N at A-regular rows with push resources) | PROVED (mod chain) | 7 |
| 14 | The residual class (A*) ∪ (U*) ∪ (W) at all large main stages | OPEN | 7.3 |
| 15 | Density of NA((c_0, p_N), l_2^2), NA((c_0, p), l_2^2) | OPEN | 8 |

## 1. Setting and notation
Design T_fin^* (Q1's T_fin over the diagonal base U k_s = mu*_s e_s, mu*_s = 2^{-2^{2^s}}, option (a)) with K1's (D-K1) and K1-ref's R-6, R-8;
the K2 insertions are listed in Section 6.  N >= 1, I the finite block set of p_N.  A ROW is f in S_{p_N*} with forced data: f = a + L^*w,
q*(a) = ||a||_1 + nu = 1, nu = ||U^*a||, e = U^*a/nu, zhat = z + U e, F = supp a (arbitrary, possibly infinite), z_s = sgn a_s on F.  Carriers
u_k (coarse: stage <= L; fine: stage > L), signature sets S_l, near coordinates N_l (the first six elements of S_l beyond s_max(L), contained in
(s_max(L), d(L)]), block weights lambda_k, block norms A_m, norming functionals w_m, block maps R_m; v_l(s) := u_l(s) on S_l.  Main stage L >=
l_f, clean sub-window w, b = b(w), u = u(w), T = T_lo(w), eta' = T^4/(L Design(L)), Step-A scale x := C Design(L) eta' (so x >= Design(L) b),
Sys-DC scale r <= C K_w s_1 (r << b).  Lever menu (P1)-(P6) of K1 2.0; carrier types (S), (U), (M) of K1 1.7 / K1-ref R-10; x'_max :=
u^2 T^3/(Design(L)^2 |Lambda|) (K1-ref R-6).
DEPTH.  H(L) := 2^{d(L)}/delta_min(L) (every near coordinate has v_l(s) >= 1/H(L)); Lambda_L := the coarse carriers;
      D(L) := the least D >= d(L) with  max_{k in Lambda_L} ||u_k 1_{(D, infinity)}||_1 <= 2^{-L^2} (|Lambda_L| H(L))^{-4};
U_L := union of supp u_k over k in Lambda_L.  Design(L) >= 2^{D(L)} D(L) H(L)/(mu*_{D(L)})^2 (Section 6), so a mass change at any s <= D(L) has
normalized efficiency mu_s^2/nu >= 1/Design(L).  "Design depth" means s <= D(L).
SYS-DC (X2 Lemma DC, Q2 Corollary 4.2): at the pre-row f_1 of Theorem UE^inf built at the companion f_0, unknowns = lever parameters P,
      F_l(P) = eps_l [u_l(xhat(P)) - (A_m(P)/A^0_m) u_l(zhat_0)],   l in Omega := all coarse strict non-peaks of f_0 (route V, no absorbers);
Q2 4.0 notation: p_l := eps_l u_l(zhat_0)/A^0_m, q_k := eps_k lambda_k w^0_m(k), g_k := eps_k <U^*u_k, e_1>, G_m := sum_k lambda_k w_m(k) <U^*u_k,
e_1>, gt := g - sum_m G_m p_m; linearization N = D - gt h^T - sum_m p_m q_m^T with D = I + X, q_m^T D^{-1} p_{m'} = delta_{mm'} q_m^T p_m, q_m^T p_m <=
1/2 (X2 2.2(3)).  SIGNED common-mode coefficient of a mass lever at p for the row l: h := eps_l a_p/(nu u_l(p)) (normalized unit step = unit
private change of eps_l val_l; this is Q2's |a|/(nu|u_l|) when eps_l a_p u_l(p) > 0).
SYS-A (K1 2.4): Step 4 of KN^tr inside Q1 Lemma CM^tr in ratio form with floating block scalars,
      Ft_l := val_l - rt_l kappa_{m(l)}   (l in Lambda_A),   val_l := eps_l u_l(xhat),   kappa_m = A_m + theta_m Phi_{P_m}^2 + S_m/theta_m (U1 Lemma 1.3),
rt_l the target ratios (Lojasiewicz/Puiseux targets r'' for active l, 0 for KN-1 holds, current ratios for holds, pushed ratios for D-pushes);
input row f_1 := the row after the deep raise, Step 0 and the preparation (P) of 4.1; |Ft(f_1)|_inf <= x.  K1's linearization (refereed by
K1-ref): J_A = [I - gtil h^T | col_c], gtil := g - (rt_l G_{m(l)})_l, col_c := -(1 - X_m) lambda_c rt^{(m)} - h_c gtil, X_m <= C c^2 D^2 (U1 Lemma
1.4(c); numerics 9: X is small only in U1's regime, not for general blocks).

## 2. Three facts valid at every row (PROVED)
LEMMA K2.2 (exact identity).  For every row and every u in l_1 put kappa_u := <U^*u, e>/nu and D_u(s) := u(s) - kappa_u a_s (s in F).  Then
      u(zhat) = kappa_u + sum_{s in F} D_u(s) sgn(a_s) + sum_{s notin F} u(s) z_s.
More generally, for every D >= 1, with c_s(u) := D_u(s) sgn(a_s) (s in F), c_s(u) := u(s) z_s (s notin F) and alpha(D) := sum_{s in F, s > D} |a_s|,
      u(zhat) = kappa_u (1 - alpha(D)) + sum_{s <= D} c_s(u) + sum_{s > D} u(s) z_s,          1 - alpha(D) >= nu.          (2.1)
Proof.  u(zhat) = u(z) + <U^*u, e> = sum_F u(s) sgn a_s + sum_{F^c} u(s) z_s + kappa_u nu and sum_F u(s) sgn a_s = kappa_u ||a||_1 + sum_F D_u(s)
sgn a_s; ||a||_1 + nu = 1.  For (2.1) write D_u(s) sgn a_s = u(s) z_s - kappa_u |a_s| for s in F, s > D; 1 - alpha(D) = ||a 1_{[1,D]}||_1 + nu.  QED
LEMMA K2.3 (resource dichotomy).  If <U^*u, e> >= 0 then for every D:  sum_{s <= D} |c_s(u)| >= <U^*u, e> - u(zhat) - ||u 1_{(D,inf)}||_1.
Proof.  (2.1) and kappa_u (1 - alpha(D)) >= kappa_u nu = <U^*u, e>.  QED
Consequence: if <U^*u,e> - u(zhat) >= theta + ||u 1_{(D,inf)}||_1, some single s <= D has |c_s(u)| >= theta/D.
LEMMA K2.4 (first-order actions; diagonal base).  At a row, for u in l_1 (remainders <= C ||U^*u|| (mu_s |dm|/nu)^2 for |dm| <= nu/(2 mu_s)):
 (i)   mass change dm at s in F (sign kept):           d u(xhat) = (mu_s^2/nu) D_u(s) dm;
 (ii)  new mass dm z_s at a contact s notin F (bank):   d u(xhat) = (mu_s^2/nu) u(s) z_s dm;
 (iii) change dz of z_s at s notin F:                  d u(xhat) = u(s) dz   (exact; e unchanged).
Proof.  U^*a changes by mu_s dm k_s; e = U^*a/||U^*a|| has derivative (mu_s dm/nu)(k_s - e_s e), e_s = mu_s a_s/nu; <U^*u, k_s - e_s e> = mu_s
D_u(s); the second derivative of x -> x/||x|| is <= 3||dx||^2/||x||^2.  (ii) is (i) with a_s = 0; (iii) xhat = z + Ue.  QED
So per unit move the action on u(xhat) is eff_s c_s(u) times the orientation of the move (eff_s = mu_s^2/nu for masses, 1 for z-moves).  A
COMPOSITE move at a zero-data contact s (bank of mass (nu/mu_s^2) P z_s for P > 0, z-move -P z_s for P <= 0) is C^{1,1} with slope u(s) z_s on
both sides (K1 2.1(a), (P1)).

## 3. LEMMA K2.1 (tolerance variant of Theorem UE^inf).  PROVED.
In Theorem UE^inf (Q2 2.4; X2 Theorem UE with the X2-ref precisions) replace "the approximant f' is d-consistent with f_0 on Omega" by
  (TOL) |mis_{i,m}| <= s_1 for every piece i and block m, mis_{i,m} := (d'_m - d_m)(Domega_{i,m}) (d-mismatch of the switching vector),
and add  (LATE-tol) C_f |Omega| A_2^2 K_w^2 s_1 <= c_late delta T^2.  Then all conclusions of Theorem UE^inf hold (K_w enlarged by an f-constant
factor): f' is norm attaining with finite base support, p*(f' + tau g'_i) <= 1 + (tau^2/2)(1 - delta) for 0 < |tau| <= c_flat t_i, and
p*(g'_i - rho g_i) <= K_w (K_w s_1 + c_fine + tail_W)/t_i.
Proof.  d-consistency enters at exactly four places.  (u1) Step 2 of thm:engineered holds without it: Omega^diamond_m = rho(omega^diamond_m -
d'_m(omega^diamond_m) w'_m) + kappa^diamond_m w'_m + rho(d^diamond_m - d^theta_m)(w'_m - w^0_m) with kappa^+-_m = -+(rho/2) mis_m, kappa^theta_m = 0.
(u2) Step 3: W_0 = (1 + tau kappa)(w' + t''(omega^diamond - d'(omega^diamond) w')), t'' = tau rho/(1 + tau kappa); |tau kappa| <= 1/16, so the
radius conditions hold with c_flat replaced by (16/15) c_flat, and lin'_m = tau kappa^diamond_m + r_m <V^an_m - w'_m, R_m x'>/sigma'_m, so |lin'_m| <=
(rho/2)|tau| s_1 + (delta/(64|I|))|tau| s_1 <= tau^2 for |tau| > s_1, while for 0 < |tau| <= s_1 the theta piece is used and lin'_m = 0 there
(kappa^theta = 0; X2 3.5 Steps 3-5 use the +- pieces only for |tau| > s_1).  Step 4 uses lin' only through |lin'_m| <= tau^2.  (u3) Lemma UE-1(c)
becomes |d'_m(omega) - d_m(omega)| <= |Omega| (A_2/t) K_w Pi and |H'_m(omega) - (C/C')H_m(omega)| <= C_f |Omega| A_2^2 K_w Pi/t^2; in Step 5 this is a
relative error <= C_f |Omega| A_2^2 K_w^2 s_1/T^2 <= delta/32 by (LATE-tol); gaps change by <= C K_w Pi <= gap/2 ((LATE)).  (u4) Lemma UE-1(g):
g''_i - g_i acquires sum_m (d_m - d'_m)(omega^theta) R_m^* w'_m, of l_1-norm <= N |Omega| A_2 K_w Pi/t_i.  Nothing else uses d-consistency.  QED
Remarks.  (TOL) is absolute in s_1 (X2 Proposition J's requirement).  |mis_{i,m}| <= (m/A'_m) ||D_m Domega||_2 ||F|_{Omega_m}||_2, so an approximate
zero |F|_inf <= c_f s_1/|Omega|^{1/2} of Sys-DC suffices; only the switching combinations matter (Q2-refa C.6).  Theorem K2.6 gives exact zeros,
so K2.1 is a robustness statement.

## 4. Sys-DC
### 4.1 Preparation (P) of the companion.  Definition and properties (PROVED).
theta_0 := b/Design(L)^{C_P}.  Inserted in Q1 Lemma CM^tr after Step 0 (deep raise beyond J(w) > D(L), V1 (C1), (C2), weak-peak pushes) and
before the Lojasiewicz step of Step A:
 (P1) every free s <= D(L), s in U_L, with tiny room (1 - |z_s| <= b) is closed to a contact (as V1 (C1), (C2));
 (P2) every contact s <= D(L), s in U_L, receives the bank mass theta_0 z_s;
 (P3) every s in F ∩ U_L, s <= D(L), with |a_s| < theta_0 is raised (same sign) to |a_s| = theta_0.
(a) Cost: p*(f^P - f^r) <= C D(L) theta_0 log(1/theta_0) + C_f p*(L^*(w^P - w^r)) <= C D(L) b log(1/b)/Design^{C_P - 1} = o(u^2 T^2) (V3 Lemma
    2.3 for raises, V1 Lemma B / Theorem E'' for banks off F, Z3 Lemma 3.1 for the normer; b <= T^4, u >= 4 (log_2(1/T))^{-1/20}).
(b) Values move by <= C D(L) theta_0 <= b (K2.4, |u_k(s)| <= 1), robust objects by <= Lip b: the clean classification survives with factor 2,
    and the Lojasiewicz step's hypothesis (D1) holds with the doubled b of (K2-e).
(c) Data: a contact of a data-carrying coarse carrier carries the exact route-V data, z-signed (K1 2.1(b), K1 part 1.3), so after (P2) it is a
    support coordinate of sign z_s with ALIGNED data -- the situation of K1's Step-A TU banks (K1 2.1(b), Proposition K1.A) -- and (U3^inf)
    constrains only anti-sign data; at raised thin coordinates K1's data are clamped/cushion dominated and a larger modulus only helps;
    zero-data coordinates are unaffected.  The theta piece of Theorem UE^inf keeps these masses >= theta_0/2 by (L-K2-1).
    [Point for a referee: that the +- pieces of the window family at banked coordinates are aligned, as at K1's TU banks (chi = 1 in V1 TR
    Step 5).  If only a split b^- = -(1 - chi) V' with chi < 1 were available, (U3^inf) there would need (1 - chi)|V'| t <= C_+ theta_0, which fails
    for t near T_hi; the alignment is what K1-ref accepted for TU banks, and nothing in the argument distinguishes a bank of mass theta_0.]
(d) TYPES.  At the companion f_0 (after Step A, 5.2) and at the pre-row f_1 of Theorem UE^inf every s <= D(L) with s in U_L, or s in F with
    |a_s| >= u/2, is of one of the types
      TS   thick support, |a_s| >= u/2 (if s notin U_L: an ANCHOR);
      S_th support with |a_s| >= theta_0/2 (banked contacts, raised thin coordinates, and Step-A raises/banks on them);
      FR   free with room >= u/2 (zero data or tolerated violations, b^theta = 0);
      ZD   zero-data coordinate, in any state (contact, free, or support of any mass);
    every other s <= D(L) is off U_L and either off F (then u(s) = 0 for every coarse u) or thin, |a_s| <= 2b.
Proof of (d).  Lemma K2.13 (clean dichotomy at depth D(L)) at f^r: s in U_L ∩ [1, D(L)] is thick, thin, a contact, free with robust room, or
free with tiny room; (P1)-(P3) turn thin coordinates, contacts and free coordinates with tiny room into S_th (zero-data ones are also
ZD).  Step A (5.2) moves TS and FR coordinates by <= Design^C x'_max << u, uses
S_th coordinates with data only through raises (one-sided generators), and may move zero-data coordinates anywhere (type ZD).  The pre-row
moves design-depth coordinates by <= K_w Pi << theta_0 ((LATE)); truncation and deep raise act beyond D(L).  QED

### 4.2 LEMMA K2.5 (left combinations of Sys-DC).  PROVED.
For y in R^Omega put beta_m := y^T p_m and Psi_y := sum_{l in Omega} y_l eps_l u_l - sum_m beta_m R_m^* w^0_m (in l_1).  Then
 (a) Psi_y(zhat_0) = 0 for every y;
 (b) for every move delta of K2.4 at f_1 (or composite of such), y^T c(delta) = l_delta(Psi_y) + err, |err| <= C |delta| ||y|| (K_w Pi + c_{L+1}),
     l_delta(u) := the first-order change of u(xhat) given by K2.4;
 (c) <U^*Psi_y, e_1> = y^T gt + O(||y|| (K_w Pi + c_{L+1})).
Proof.  (a) sum_{l in Omega_m} y_l eps_l u_l(zhat_0) = A^0_m beta_m and (R_m^* w^0_m)(zhat_0) = <w^0_m, R_m zhat_0> = A^0_m (w^0_m norms the block).
(b) dF_l = eps_l du_l - p_l dA_m and dA_m = l_delta(R_m^* w^1_m) + O(|delta|^2) (block norm smooth, Martin Lemma A(d)); so y^T c(delta) =
l_delta(Psi_y) + sum_m beta_m l_delta(R_m^*(w^0_m - w^1_m)) and ||R_m^*(w^0_m - w^1_m)||_1 <= K_w Pi + 2 c_{L+1} (X2 Lemma UE-1(d)).  (c) <U^*Psi_y,
e_1> = y^T g - sum_m beta_m G_m + (same error).  QED

### 4.3 THEOREM K2.6 (Sys-DC is uniformly solvable after preparation).  PROVED (mod the refereed machinery of X2/Q2 and Step A of 5.2).
Let L >= l_f, w clean, f_0 the prepared companion after Step A, f_1 any pre-row of Theorem UE^inf at f_0.  Let C be the column matrix of Sys-DC
at f_1 formed by
 (i)  for every l in Omega one two-sided lever: (P1) composite at a ZD near coordinate (zero-data l with an off-F or thin near coordinate);
      for a data-carrying l with an off-F or thin near coordinate, the S_th LEVER = mass change at a banked/raised near coordinate s (two-sided
      at scale r << theta_0; signed h_l = eps_l a_s/(nu v_l(s)), |h_l| <= Design^{C+1} x'_max); if N_l consists of thick coordinates: (P3) when a
      robust-spread pair exists, else (P4) at a thick near coordinate (|h_l| <= H(L)/nu).  Every l in Omega has one of these;
 (ii) one elementary column at every s <= D(L) of type TS (anchors included), S_th (mass change), FR (z-move), ZD (composite move).
Then
      s_min(C) := min_{||y||_2 = 1} ||C^T y||_2  >=  eps_DC := c_f (mu*_{D(L)})^2 / (D(L) |Omega| H(L) (1 + 8N |Omega|^{1/2}/A_min)),   c_f := nu_1/16,
so C has the right inverse R := C^T(C C^T)^{-1} with ||R||_inf <= K_DC := (number of columns)^{1/2}/eps_DC <= C_{f,N} Design(L)^{C_0}.  Consequently
Lemma DC^inf holds at f_1 with K_DC in place of K_J and WITHOUT any hypothesis on c_alpha, beta_*, c'_alpha, beta'_*, Sherman-Morrison
denominators, spreads or anchors: F has a zero P* with |P*|_inf <= K_DC r, every Omega carrier is a strict non-peak with nv = nv^0 exactly, the
coarse peaks keep their statuses, S_th masses stay >= theta_0/4, TS and FR coordinates stay robust.
Proof.  Let y be a unit vector with ||C^T y||_2 < eps; we show eps >= eps_DC.  Put gamma := y^T gt, beta_m := y^T p_m.
Step 1 (shape).  The lever of l has the column d_l e_l - h_l gt - p_{m(l)} q_l + E_l (normalized units; d_l in [1/2, 2] the diagonal of D; Q2 4.0,
Q2-refa C.1, K1 2.1, K2.4) with ||E_l|| <= eps_E := C_f Design^C (K_w Pi + c_{L+1}) <= eps_DC/8 ((LATE)).  Hence y_l = (beta_{m(l)} q_l + gamma h_l +
e'_l)/d_l with |e'_l| <= eps + eps_E.
Step 2 (gamma is robust).  Blocks are disjoint and q_m^T D^{-1} p_{m'} = delta_{mm'} q_m^T p_m, so beta_m (1 - q_m^T p_m) = gamma p_m^T D^{-1} h +
p_m^T D^{-1} e', |beta_m| <= 4(|gamma| ||h||_2 + ||e'||_2) ||p_m||_2, ||p_m||_2 <= 2|Omega|^{1/2}/A_min, ||q_m||_2 <= 1.  Therefore
      1 = ||y||_2 <= ||D^{-1}|| (sum_m |beta_m| + |gamma| ||h||_2 + ||e'||_2) <= 2 (|gamma| ||h||_2 + ||e'||_2)(1 + 8N |Omega|^{1/2}/A_min).
If ||e'||_2 >= 1/(4(1 + 8N|Omega|^{1/2}/A_min)) then eps >= eps_DC already.  Otherwise |gamma| >= gamma_min := 1/(4 ||h||_2 (1 + 8N|Omega|^{1/2}/A_min))
(and h != 0).  Replace y by -y if necessary: gamma > 0.  Note ||h||_2 <= |Omega|^{1/2} H(L)/nu_1, so gamma_min >= nu_1/(4 |Omega| H(L)(1 + 8N|Omega|^{1/2}/A_min)).
Step 3 (the combination).  By K2.5, Psi_y(zhat_0) = 0 and <U^*Psi_y, e_1> = gamma + O(K_w Pi + c_{L+1}).  Split Psi_y = Psi^c + Psi^f, Psi^f := the
fine-carrier part of -sum beta_m R_m^* w^0_m, ||Psi^f||_1 <= sum_m |beta_m| sum_{k > L} lambda_k <= C |gamma| c_{L+1}.  The coefficients of Psi^c are
<= |y_l| + sum_m |beta_m| lambda_k <= C (|gamma|/gamma_min) (unit y), so by the choice of D(L)
      ||Psi^c 1_{(D(L), inf)}||_1 <= C |Lambda_L| (|gamma|/gamma_min) 2^{-L^2} (|Lambda_L| H(L))^{-4} <= gamma/16          (L >= l_f).
At f_1: |Psi^c(xhat_1)| <= |Psi_y(zhat_0)| + ||Psi_y||_1 ||xhat_1 - zhat_0||_inf + ||Psi^f||_1 <= gamma/16 ((LATE): ||xhat_1 - zhat_0||_inf <= K_w Pi),
and <U^*Psi^c, e_1> >= (15/16) gamma.
Step 4 (a resource).  Lemma K2.3 at the row f_1 with u := Psi^c and D := D(L): some s <= D(L) has |c_s(Psi^c)| >= gamma/(2 D(L)).  If s notin U_L
then Psi^c(s) = 0, so s in F_1 and |c_s| = kappa |a_s| with kappa := <U^*Psi^c, e_1>/nu_1 <= 2 gamma/nu_1, whence |a_s| >= nu_1/(4 D(L)) >> 2b: s is TS,
an anchor (thin s notin U_L contribute <= kappa 2b each, D(L) kappa 2b << gamma/16 in total, already absorbed).  If s in U_L, s has type TS, S_th,
FR or ZD by 4.1(d).  In all cases C contains the elementary column c_s at s.
Step 5 (contradiction).  By K2.5(b) and K2.4, |y^T c_s| >= eff_s |c_s(Psi_y)| - err with |c_s(Psi_y) - c_s(Psi^c)| <= ||Psi^f||_1 + |<U^*Psi^f, e_1>|/nu_1
tiny; eff_s >= mu*_{D(L)}^2 (masses; nu <= 1) or = 1 (z-moves, composite).  So eps > |y^T c_s| >= mu*_{D(L)}^2 gamma_min/(4 D(L)) >= eps_DC
(since |c_s(Psi^c)| >= gamma/(2D(L)) >= gamma_min/(2D(L)) and the errors are << that).
Step 6 (nonlinear solve).  G(y) := F(R y) = F(0) + y + Rem(R y) on the cube |y|_inf <= r; on the face y_l = r, G_l >= r - |F(0)|_inf - C_2 ||R||^2 r^2 >=
0 when K_DC |F(0)|_inf <= r/2 and C_2 K_DC^2 r <= 1/4 (C_2 a design constant: second derivatives of K2.4 at depth <= D(L) and of the levers);
symmetric on y_l = -r; Poincare-Miranda gives a zero.  Ranges: S_th moves by <= Design(L) K_DC r <= theta_0/4 in mass ((L-K2-2)); TS, FR by << u;
ZD unlimited; (P1), (P3), (P4) as K1 2.1.  Statuses: values move by <= C_lev K_DC r << min(gap_min, margins) ((L-K2-3); Q1 Lemma PM (v)).  QED
Remarks.  (1) Steps 2-5 are a uniform dichotomy: no pigeonhole or rate object for c_alpha, beta_*, c'_alpha, beta'_*, 1 - h^T g, spreads or
anchors.  The block-norm levers (P6) (Q2 Proposition 4.1, Q2-refa C.3, K1 2.2, K1-ref R-7) are not used; a peak's near coordinates are columns
of type (ii) anyway.  (2) The resource of Step 4 is never the lever coordinate of an Omega carrier: there |c_s(Psi_y)| = |y^T(lever)|/eff + err < eps/eff
by Step 1.  (3) No TU lever is used in Sys-DC (the S_th lever replaces it), so no pull at the scale r is needed.  (4) Why preparation is needed:
without (P2) the resource of Step 4 may be a data-carrying contact, where only a bank (one-sided at every scale) is available; K1 2.2 shows that
a bank placed at the PRE-ROW cannot be made two-sided by an offset (the forced total position y^T F(0)/(y^T c) has an uncontrolled sign).  In (P2)
the offset is placed in the BASE ROW f_0, whose values ARE the targets of Sys-DC, so the forced position is theta_0 + O(K_DC r) > 0.

### 4.4 COROLLARY K2.7 (the degenerate configurations of Q2 / Q2-refa / K1 at the approximant).  PROVED.
(a) Q2 4.4(i)-(iii), Q2-refa C.5, C.6, K1 2.5(b2) and K1-ref R-7: (NDN2), its quantitative version, the exact degenerate configuration, the
    "exceptional case" (left null vector blockwise in the span of the switching vectors) and the (P4)-type block-norm degeneracy
    {c'_alpha = beta'_* = 0} do not arise after preparation: by Theorem K2.6 the prepared Sys-DC has no near-null left vector at all.  Neither
    the data-side bordering (R3-a) nor the tolerance variant is needed.
(b) Why C.5's obstruction disappears.  In C.5's configuration as stated there (no absorbers, h^T p_m = 0, u_h = kappa a_0 on F_0, c_alpha = 0),
    Lemma K2.2 gives 0 = u_h(zhat_0) = kappa + sum_{s notin F_0} u_h(s) z_s with kappa = 1/nu_0, so ||u_h 1_{F_0^c}||_1 >= 1/nu_0 >= 2 and at most 1/16
    of it lies beyond D(L): the configuration REQUIRES off-support mass of u_h at design depth.  C.5's tau_W lives exactly there (theta-masses at
    data-carrying contacts of supp u_h).  After (P2) these contacts are S_th coordinates with D_{u_h}(s) = u_h(s) - kappa theta_0 z_s != 0, so the
    prepared row is not fully degenerate and Theorem K2.6 Step 4 finds them as two-sided resources.  (By K1-ref R-11 the exact limit of an
    UNPREPARED non-regular row only gives u_h = kappa a on F_thick ∩ [1, d(L)]; the statement above concerns C.5's configuration as stated.)
(c) K1's (U), (S), (M) carriers cause no failure of Sys-DC after preparation: (U) and (M) carriers have an S_th near coordinate (a private
    two-sided lever at scale r), (S) carriers have (P4) and enter only through the direction handled by Steps 2-5.
(d) In K1's lever-regularity (LR) the Sys-DC half holds automatically; only Step A (Sys-A) and Step 0's pushes remain (Sections 5, 7).

## 5. Sys-A
### 5.1 LEMMA K2.8 (Euler combination of Sys-A).  PROVED.
For y in R^{Lambda_A} put zeta_m := sum_{l in m} y_l rt_l and
      Psi^A_y := sum_l y_l eps_l u_l - sum_m zeta_m K_m,      K_m := sum_k (d kappa_m/d zeta_m(k)) lambda_k u_k    (derivatives at the input row
of Step A, f_1 or f_1 + Pi of 5.2; all statements below are at that row).
Then (a) Psi^A_y(xhat_1) = y^T Ft(f_1) =: phi_y, |phi_y| <= x ||y||_1; (b) for every move delta of K2.4, y^T c_A(delta) = l_delta(Psi^A_y) + O(|delta|^2);
(c) <U^*Psi^A_y, e_1> = y^T gtil.
Proof.  kappa_m is a function of the block vector zeta_m = (lambda_k u_k(xhat))_k, positively homogeneous of degree 1 and C^1 while the peak set is
fixed (the clamp/threshold equations of U1 Lemma 1.2 are invariant under zeta -> c zeta, A -> cA, theta -> c theta; S_m is 2-homogeneous; non-peak
terms are smooth at zeta_k = 0).  Euler's identity gives kappa_m(f_1) = K_m(xhat_1), whence (a); (b) is the chain rule; (c) is (b) for the common
mode (G_m = <U^*K_m, e_1>).  QED  (Numerics: euler_check.py, homogeneity 4.6e-16, Euler identity 5.2e-9.)

### 5.2 A-regularity and LEMMA K2.9 (cone realization of Step A).  PROVED.
GENERATORS at the input row f_1 (normalized columns of Sys-A; by K2.8(b) each acts on y^T Ft by l_delta(Psi^A_y)):
 two-sided -- the levers (P1) (composite), (P3), (P4) of tuned carriers; TU levers whose pull AND base bank are pre-placed (the bank then moves
   both ways around its base mass, K1 2.1(b)); two-sided peak resources; one elementary move at every design-depth coordinate of type TS
   (anchors included; mass change), FR (z-move), ZD (composite);
 one-sided (allowed direction only) -- raises of S_th coordinates carrying data (in particular at the near coordinates of (U)- and
   (M)-carriers).  Every design-depth one-sided generator is a raise of |a_s|, acting on Psi(xhat) by +eff_s c_s(Psi) per unit (K2.4(i)).
PRE-PLACEMENTS Pi: discrete far moves, at most one per tuned carrier, at its smallest admissible depth in [x, x'_max]: K1's pulls (with x'_max,
K1-ref R-6) with the compensating base banks of TU, and (in 5.6 only) placements of the opposite sign ("pushes").
Let b := -Ft(f_1 + Pi), W := Design(L)^{C_A} max(x, ||b||_2), rho_0 := C_2 W^2 (C_2 the second-order constant of the generators, a design
constant; the composite moves are C^{1,1}), Q := conv(G ∪ {0}).
DEFINITION.  The stage (L, w, a) is A-REGULAR if for some Pi:  B(b, rho_0) ⊂ (W/2) Q.
A NEAR-CERTIFICATE (of size eps) is a unit y with max_{g in G}(-y^T g) <= eps; phi_y := y^T Ft(f_1 + Pi).
LEMMA K2.9.  (a) If eps_PS := min_{||y||_2 = 1} max_{g in G}(-y^T g) >= Design(L)^{-C_1} and C_A >= C_1 + 2, the stage is A-regular with Pi = {}
    (for every right-hand side).
(b) [quantitative Farkas]  If the stage is not A-regular for Pi, there is a near-certificate y of size eps < 4 Design(L)^{-C_A} with phi_y > -rho_0.
(c) If the stage is A-regular, Step A is realized: a companion f^(1a) with all conclusions of K1 Lemma K1.6(A) (exact ratios r'' on Z_kappa,
    exact KN-1 zeros, Puiseux protection, robust statuses), moves <= W, cost <= C_f Design^C W log(1/W) = o(u^2 T^2).
Proof.  (a) If some b' with ||b'|| < eps_PS were outside conv(G), a separating unit y would give y^T b' < min_g y^T g <= -eps_PS, impossible; so
B(0, eps_PS) ⊂ Q.  Every b' in B(b, rho_0) has ||b'|| <= ||b|| + rho_0 and lies in ((||b|| + rho_0)/eps_PS) Q ⊂ (W/2) Q, because ||b||/eps_PS <=
Design^{C_1} ||b|| <= W/4 and rho_0/eps_PS = C_2 W^2 Design^{C_1} <= W/4 (W <= Design^{C_A} x'_max is far below Design^{-C_1}/C_2).
(b) Pick b'' in B(b, rho_0) outside (W/2)Q and separate it from this compact convex set: a unit y with y^T b'' < (W/2) min(0, min_g y^T g).  Then
y^T b < rho_0 - (W/2) max(0, max_g(-y^T g)), so max_g(-y^T g) < 2(rho_0 + ||b||)/W <= 4 Design^{-C_A} and phi_y = -y^T b > -rho_0.
(c) For b' in cone(G) let S(b') := argmin{ ||s||_2 : G s = b', s >= 0 }; S is continuous on cone(G) (strictly convex parametric QP with the
parameter in the right-hand side; via Hoffman's bound the feasible sets depend Hausdorff-Lipschitz on b').  On K := {t >= 0 : ||t||_2 <= W} the
map T(t) := S(b - Rem(t)) is defined and continuous: ||Rem(t)|| <= C_2 ||t||^2 <= rho_0 puts b - Rem(t) in B(b, rho_0) ⊂ (W/2)Q, which also gives
||T(t)||_2 <= W/2.  Brouwer: t* = T(t*) solves Ft(f_1 + Pi) + G t* + Rem(t*) = 0 with t* >= 0.  Statuses, Puiseux margin and costs as in K1 Lemma
K1.6(A), which use only the exactness of the realized ratios and the size of the moves (<= W <= Design^C x'_max << u; R-6 for far moves).  QED
[K2.9(c) makes K1's "ratio trick" (K1 2.7 Remark (1), SKETCH there; K1-ref R-14's "degree argument on the cone of admissible bank
parameters") rigorous whenever its cone condition holds.]

### 5.3 THEOREM K2.16 (structure of Step-A obstructions).  PROVED.
NOTATION.  For a unit y write the coarse part of Psi := Psi^A_y as Psi = sum_{k coarse} coef_k u_k, i.e. coef_l = eps_l y_l - zeta_m lambda_l
(d kappa_m/d zeta(l)) for a tuned carrier l and coef_k = -zeta_m lambda_k (d kappa_m/d zeta(k)) for an untuned coarse carrier k (a peak).  For a
coordinate s in S_k beyond s_max(L) (PRIVATE to k among coarse carriers), Psi(s) = coef_k v_k(s).  gamma := <U^*Psi, e_1>, kappa := gamma/nu_1.
v_min(L) := min{|u_k(s)| : k in Lambda_L, s in supp u_k ∩ [1, D(L)]} > 0 is a design number and 1/v_min(L) <= Design(L) ((K2-b)).
Since zeta_m (1 - Xt_m) = sum_{l in m} rt_l eps_l coef_l with Xt_m := sum_{tuned l in m} rt_l eps_l lambda_l (d kappa_m/d zeta(l)) <= 1/4 (the
non-peak Euler share; U1 Lemma 1.4(c), X_m <= C c^2 D^2 -- see 9 for why this needs U1's regime), one has ||coef_tuned||_2 >= c_1 :=
1/(2 + C N |Lambda_A|^{1/2}/A_min).  h denotes the vector of signed (P4) coefficients (h_l := eps_l a_p/(nu_1 v_l(p)) at the (P4) coordinate p of
l; h_l := 0 for carriers without (P4)).
STATEMENT.  Let L >= l_f and let y be a near-certificate of size eps <= eps_* := Design(L)^{-C} (C a large absolute constant) at f_1 + Pi.  Then
 (1) [no positive common mode]  if gamma > 0 then gamma <= 2(|phi_y| + D(L) eps Design(L) + tail_D) =: small, where |phi_y| <= |Lambda_A|^{1/2}
     max(x, ||b||) and tail_D := C_f 2^{-L^2} (|Lambda_L| H(L))^{-4} + C c_{L+1};
 (2) [action of the generators]  at every design-depth coordinate s: |c_s(Psi)| <= eps Design if s carries a two-sided generator, c_s(Psi) >=
     -eps Design if it carries a one-sided one.  Hence, for every coarse carrier k:
     (2a) if S_k has a private FR or ZD coordinate in [1, D(L)], or k has a pre-placed TU lever, then |coef_k| <= eps Design^2;
     (2b) at every thick private p in S_k ∩ [1, D(L)]:  |coef_k v_k(p) - kappa a_p| <= eps Design;
     (2c) at every S_th private s' in S_k ∩ [1, D(L)] carrying data (sign z_{s'}):  coef_k z_{s'} >= -(eps Design + |kappa| theta_0) Design;
 (3) [ROBUSTLY NEGATIVE COMMON MODE]  gamma <= -c_*,   c_* := c_1 min{ 1/(4 ||h||_2), nu_1/(8 H(L)) } > 0;
 (4) [proportional thick support]  at every s <= D(L) with |a_s| >= u/2:  |Psi(s) - kappa a_s| <= eps Design, while |kappa a_s| >= c_* u/(2 nu_1);
     so Psi(s) != 0 robustly: s in U_L (NO ANCHOR), and s lies in the support of a coarse carrier whose coefficient is robust;
 (5) |Psi(s)| <= eps Design at every FR or ZD coordinate s <= D(L);
 (6) if phi_y > -rho_0 (as in K2.9(b)):  the sum of c_s(Psi) over the design-depth coordinates carrying one-sided generators is >= c_*/2.
Proof.  (1) Apply (2.1) at f_1 + Pi with u := Psi, D := D(L): phi_y = kappa(1 - alpha(D)) + sum_{s <= D} c_s(Psi) + sum_{s > D} Psi(s) z_s.  By (2)
(proved independently below) every design-depth coordinate carrying a generator has c_s >= -eps Design; the remaining design-depth
coordinates (last kind in 4.1(d)) have c_s = 0 or c_s = -kappa |a_s| >= -2|kappa| b; the deep sum is >= -tail_D (coefficients of Psi are <= C_f,
since |y| <= 1, |rt_l| <= C/A_min, |d kappa/d zeta| <= C; the fine part is <= C c_{L+1}).  If gamma > 0 then kappa(1 - alpha(D)) >= kappa nu_1 = gamma
and 2 D(L) kappa b = 2 D(L) gamma b/nu_1 <= gamma/2, whence (1).
(2) By K2.8(b) and K2.4 a generator at s acts on y^T Ft by eff_s c_s(Psi) times its orientation (composite moves: slope Psi(s) z_s on both sides);
eff_s >= 1/Design(L).  Two-sided: |eff_s c_s| <= eps; one-sided raise: eff_s c_s >= -eps.  (2a): at a private FR/ZD coordinate s', |Psi(s')| =
|coef_k| v_k(s') <= eps Design and v_k(s') >= v_min(L) >= 1/Design; a pre-placed TU bank is a two-sided private generator, same bound.  (2b): the
TS generator at p.  (2c): c_{s'} = (coef_k v_k(s') - kappa a_{s'}) z_{s'} with |a_{s'}| = theta_0 at f_1.
(3) Put gamma_0 := c_1/(4 ||h||_2) and suppose gamma > -gamma_0; by (1), |gamma| <= gamma_0 (small << gamma_0 for L >= l_f).  Every tuned carrier l is
of one of four kinds (K1-ref R-10; after (P) the off-F or thin near coordinates of zero-data carriers are ZD and those of data-carrying
carriers are S_th of the data sign sigma_l, K1 2.1(b), Lemma K1.3(S)):
  (i)   N_l contains a ZD coordinate, or l has a pre-placed TU lever: |coef_l| <= eps Design^2 by (2a);
  (ii)  S_l ∩ [1, D(L)] contains two thick private coordinates s, s' with robust spread (|1 - rho_s/rho_{s'}| >= u, rho := a/v_l): by (2b) at s and
        s', coef_l = kappa rho_s + O(eps Design^2) = kappa rho_{s'} + O(eps Design^2), so |kappa| <= 8 eps Design^3/u^2;
  (iii) otherwise, N_l contains a thick coordinate p: coef_l = kappa a_p/v_l(p) + O(eps Design^2) = eps_l gamma h_l + O(eps Design^2) by (2b);
  (iv)  otherwise every near coordinate of l is S_th of the data sign sigma_l, and coef_l sigma_l >= -(eps Design + |kappa| theta_0) Design by (2c)
        ((U)-carriers, and (P2)-carriers whose TU is not pre-placed).
 If a kind-(ii) carrier exists, kappa is tiny; this contradicts the conclusion kappa <= -c_U/2 reached below in the present case, and
 contradicts gamma <= -gamma_0 in the other case; so then NO near-certificate exists.  Otherwise ||coef_(i)||_2 + ||coef_(iii)||_2 <= |gamma| ||h||_2 +
 small' <= c_1/4 + small', hence ||coef_(iv)||_2 >= c_1/2.  At the S_th near coordinates s of a kind-(iv) carrier l (private to l),
 c_s(Psi) = coef_l sigma_l v_l(s) - kappa theta_0 >= coef_l sigma_l/H(L) - |kappa| theta_0 when coef_l sigma_l >= 0 (v_l >= 1/H(L) on N_l), and
 sum_l max(coef_l sigma_l, 0) >= ||coef_(iv)||_2 - small'' >= c_1/2 - small''.  With (2) for all other design-depth coordinates,
      sum_{s <= D(L)} c_s(Psi) >= c_1/(2 H(L)) - D(L)(eps Design^2 + 2|kappa| b) - |Lambda_A| small'' >= c_1/(4 H(L)) =: c_U.
 By (2.1), kappa(1 - alpha(D)) = phi_y - sum_{s <= D} c_s - (deep sum) <= |phi_y| - c_U + tail_D <= -c_U/2, so kappa < 0 and, as 0 < 1 - alpha(D) <= 1,
 gamma = kappa nu_1 <= -nu_1 c_U/2 = -c_1 nu_1/(8 H(L)).  In both cases gamma <= -c_*.
(4) The TS generator at s is two-sided: |c_s(Psi)| = |Psi(s) - kappa a_s| <= eps Design; |kappa| >= c_*/nu_1 by (3).  (5) FR and ZD generators are
two-sided with action Psi(s) times the orientation of z.  (6) By (2.1), sum_{s <= D} c_s(Psi) = phi_y - kappa(1 - alpha(D)) - (deep) >= -rho_0 +
|kappa| nu_1 - tail_D >= c_* - rho_0 - tail_D; two-sided coordinates contribute at most D(L) eps Design in absolute value, the last kind of 4.1(d)
at most 2 D(L) |kappa| b; the rest is the one-sided sum.  QED

### 5.4 COROLLARY K2.17 (sufficient conditions).  PROVED.
At a main stage L >= l_f (clean w, class a, after (P), Pi := the TU pre-placements of K1's Step A), the Step-A generators POSITIVELY SPAN with
eps_PS >= Design(L)^{-C} -- hence the stage is A-regular for every right-hand side (K2.9(a)) -- if one of the following holds:
 (a) every tuned carrier is privately tunable (K1 Lemma K1.5(a));
 (b) an ANCHOR: a thick s <= D(L) outside U_L (K1's (P5), now at depth D(L) >= d(L));
 (c) a coarse carrier k (tuned, or a peak) with a thick private coordinate and a private FR or ZD coordinate (or a pre-placed TU lever) in
     S_k ∩ [1, D(L)];
 (d) a coarse carrier k with a thick private coordinate p and a private S_th coordinate s' carrying data, both in S_k ∩ [1, D(L)], of the SAME
     sign (sgn a_p = z_{s'}); for an (M)-carrier: a thick near coordinate carrying the data sign;
 (e) a coarse carrier k with two thick private coordinates in S_k ∩ [1, D(L)] of robust spread (this extends K1's (P3) from N_l to S_l ∩ [1, D(L)]).
Moreover the stage is A-regular for the given right-hand side if
 (f) [K1 Lemma K1.5(b)'s setting: every tuned carrier is of kind (i) or (iii)]  |1 - h^T gtil| >= u, or |(1 - X) lambda_c h^T rt^{(m)} + h_c| >= u for
     a two-sided peak resource c (then no near-certificate exists), or phi_{y_+} >= 2 rho_0 + C Design^{-C_A} ||Ft(f_1)||_2 for the degenerate
     direction y_+ (the near-null left vector of I - gtil h^T with gamma > 0): the needed correction points DOWN along y_+;
 (g) [no (U*)-certificates; ratio trick / peak bordering, K1-ref R-13, R-14]  every block containing kind-(iv) carriers has a private two-sided
     peak resource, no kind-(iii) carrier with nonzero target, and kind-(iv) carriers with |rt_l| >= u and rt_l eps_l sigma_l of one sign; then every
     near-certificate has gamma <= -gamma_0, i.e. is of type (A*) (5.7), and (f)'s criterion applies to it.
Proof.  Suppose a near-certificate of size eps <= eps_* exists; Theorem K2.16 applies.  (a) The private two-sided columns are e_l + small and span.
(b) Psi(s) = 0 at an anchor, against (4).  (c) |coef_k| <= eps Design^2 by (2a), so Psi(p) = coef_k v_k(p) is tiny at the thick p, against (4).
(d) By (2b) and (3), coef_k v_k(p) = kappa a_p + O(eps Design) with |kappa a_p| robust and kappa < 0, so sgn(coef_k) = -sgn(a_p) and coef_k is
robust; (2c) then forces z_{s'} = sgn(coef_k) = -sgn(a_p), against sgn a_p = z_{s'}.  (e) Kind (ii) in the proof of (3): no near-certificate.  In
(a)-(e) no near-certificate of size <= eps_* exists, i.e. eps_PS > eps_*.  (f) In this setting there is no kind-(iv) carrier, so by the proof of
(3) every near-certificate has gamma <= -gamma_0; the two-sided columns form the square system I - gtil h^T (bordered by peak columns), whose
near-null left vectors are +-y_+ up to O(eps') (rank-one perturbation of I; K1 2.5(b1)); a robust bordered scalar excludes them, and +y_+ has
gamma > 0, so the only candidate is -y_+, which is an obstruction (K2.9(b)) only if phi_{-y_+} > -rho_0 up to the O(eps') deviation of the certificate from -y_+, i.e. only if
phi_{y_+} < rho_0 + C Design^{-C_A} ||Ft(f_1)||_2.
(g) In such a block coef_c = O(eps Design^2) for the peak, hence zeta_m = O(eps Design^2) (d kappa/d zeta(c) >= 3/4), so sum_{l in m} rt_l eps_l coef_l
= zeta_m(1 - Xt_m) = O(eps Design^2); kinds (i), (ii) contribute O(eps Design^2), kind (iii) nothing (zero targets), and the kind-(iv) terms
rt_l eps_l coef_l = (rt_l eps_l sigma_l)(coef_l sigma_l) have one sign up to O(eps Design^2) with |rt_l| >= u: each is O(eps Design^2/u).  So
||coef_(iv)|| is small, which in the proof of (3) excludes gamma > -gamma_0.  QED

### 5.5 (O-c)(iii): "KN-1 holds in a degenerate raw direction".  PROVED (it is not a separate obstruction).
A KN-1-held carrier l is zero data (K1 2.0).  If N_l contains an off-F or thin coordinate, it is ZD after (P) (kind (i): coef_l = O(eps Design^2)
in every near-certificate).  If N_l is thick, l is of kind (ii) (then no near-certificate exists at all) or (iii).  Its own correction is <=
4 c_{L+1}^2 << theta_0/Design.  Hence a degenerate direction in which KN-1 holds take part is either realizable or yields a near-certificate of
Theorem K2.16, i.e. it belongs to the residual (A*) of 5.7.  Moreover, if a KN-1-held carrier l of kind (iii) has a robust coefficient, every
far j in S_l off F is zero-data, and a z-move there (two-sided, efficiency v_l(j) >= x, admissible since the data vanish) breaks the
certificate; so (A*) then requires S_l ∩ {x <= v_l <= x'_max} ⊂ F with |a_j| > x'_max.  (U2 Lemma ND / Theorem ND', the cushion route, is not needed.)

### 5.6 PROPOSITION K2.11 (far moves versus certificates).  SKETCH.
Let y be a near-certificate and k a tuned carrier with robust coef_k.  A far placement at j in S_k (x <= v_k(j) <= x'_max) of support of sign
sigma acts on Psi(xhat) by coef_k v_k(j)(sigma - z_j) (+ negligible e-terms); if sgn(sigma - z_j) = -sgn(coef_k) and |sigma - z_j| >= 1/2, it
decreases y^T(values) by >= |coef_k| x/2 >> eps (per normalized unit), contradicting the certificate after pre-placement and overshoot (v_k(j) >= x
>= |phi_y|).  K1's pulls are the placements of sign -eps_k: they break the certificate when eps_k coef_k > 0 (PROVED, V1 Lemma TU / K1 2.1(b));
placements of sign +eps_k ("pushes") break it when eps_k coef_k < 0, provided pushes are admissible -- the mirror image of V1's pulls (anti-sign
data dominated by the placed mass 24 lambda_k v_k(j); costs as K1-ref R-6), not re-derived line by line.  After an overshooting pre-placement,
the stage is A-regular if +-y were the only near-certificate directions (K1.5(b)'s setting); in general one needs that no new certificate
appears (not shown).  Hence SKETCH.  Concrete reading of a residual certificate: every carrier k with robust coef_k has (S1) all thick
coordinates of S_k ∩ [1, D(L)] proportional, a_s = (coef_k/kappa) v_k(s) (tiny spreads over S_k up to depth D(L), not only on N_k), of sign
-sgn(coef_k); (S2) its data-carrying S_th coordinates of sign sgn(coef_k), its FR/ZD coordinates at depth <= D(L) absent; (S3) no far
coordinate in [x, x'_max] admitting a placement against the certificate.

### 5.7 The residual of Step A (precise).  OPEN.
A stage that is not A-regular carries a near-certificate y with (1)-(6) of Theorem K2.16 and none of Corollary K2.17 (a)-(e); it is of type
 (A*) gamma <= -gamma_0 = -c_1/(4||h||_2): the coefficients on (P4)-carriers are coef_l = eps_l gamma h_l (support-swallowed carriers whose thick
      part is proportional over S_l ∩ [1, D(L)]), possibly plus nonnegatively oriented kind-(iv) coefficients; the needed correction is against
      every generator; or
 (U*) -gamma_0 < gamma <= -c_1 nu_1/(8 H(L)): ||coef_(iv)||_2 >= c_1/2 (concentrated on (U)-type carriers, oriented coefficients >= 0), in blocks not
      of the kind of K2.17(g); the needed correction asks some kind-(iv) carriers to move against their one-sided generators, and no combination
      of kappa-rescalings and allowed moves provides it.
Both are SIGN (cone) obstructions, not rank obstructions, and both force the exact-limit structure (4) on the WHOLE thick support at depth <= D(L)
with one common kappa <= -c_*/nu_1: a|_{F_thick ∩ [1, D(L)]} = Psi_y/kappa up to eps Design/|kappa| -- an infinite-depth version of the configuration of
U2 Lemma ND / Q2 Lemma 4.3 (K1-ref R-11 had it only on F_thick ∩ [1, d(L)]) -- together with the positive one-sided mass (6).  NOT shown: that (A*)
or (U*) at ALL large main stages is impossible, nor that such rows have a non-recoverable mate.

## 6. Bookkeeping (O-d)
### 6.1 Design T_fin^{K2}.  Definition.
T_fin^* with K1's (D-K1), K1-ref R-8(ii) (enlarged (D1)), and at every stage L:
 (K2-a) [in (S5), after the carriers of stages <= L, d(L), delta_min(L) are fixed, before Design(L)] H(L), D(L), U_L as in Section 1 (D(L) exists:
        finitely many l_1 vectors).
 (K2-b) [in (S5)] Design(L) := [Design(L) of T_fin^* with (D-K1)] x (2^{D(L)} D(L) H(L) |Lambda_L|/((mu*_{D(L)})^2 v_min(L)))^{C_D2}, C_D2 absolute
        (>= 2), where v_min(L) := min{ |u_k(s)| : k in Lambda_L, s in supp u_k ∩ [1, D(L)] } > 0 (finitely many nonzero numbers).
 (K2-c) [rate scheme] add to omega(L): (R-mod') |a_s| for s in [1, D(L)]; (R-room) 1 - |z_s| for s in [1, D(L)] (= 0 on F).  2 D(L) objects.
        [No object for c_alpha, beta_*, c'_alpha, beta'_*, Sherman-Morrison denominators, spreads or anchors is needed by K2: Theorem K2.6 is
        uniform and Theorem K2.16 / Corollary K2.17 are statements about the selected stage.  K1's (R-lev) objects may stay; they are unused.]
 (K2-d) [in (S6), after b(w)] theta_0(w) := b(w)/Design(L)^{C_P}, C_P absolute, C_P >= C_D2 + 4.
 (K2-e) [in (S6)] b_X1(w) defined with 2b in place of b in (D1) and (D2) (on top of R-8(ii)'s factor Design^C/u(w)).
Construction choices (not design): J(w) > D(L) (deep raise), N_w > D(L) (truncation), pre-placements at the smallest admissible depth in
[x, x'_max] (R-6), Step 0 -> (P) -> Step A order.
### 6.2 LEMMA K2.12 (well-foundedness, positivity, N-independence, monotonicity).  PROVED.
(a) Every inserted quantity of stage L is a function of earlier quantities: D(L) of the u_k of stages <= L, d(L), delta_min(L); v_min(L) of the
u_k and D(L); Design(L) of D(L), H(L), |Lambda_L|, v_min(L); omega(L) of D(L); theta_0(w) of b(w) and Design(L); b_X1(w) of the same data as
before.  Lemma W_fin(a) persists.
(b) Finite and positive: D(L) < infinity, mu*_{D(L)} > 0, v_min(L) > 0, b(w) > 0.  (c) No rule refers to N or f; the count 2D(L) is N-free; for p_N the objects
are evaluated on the coordinates present (V1-ref p0).  (d) (K2-b), (K2-c) only enlarge Design(L), omega(L), hence Q(w) = (4 Design(L)/u(w))^{omega(L)
+ L^2 + 20} and n(w), and only lower T_lo(w), eta(w), b(w); (K2-e) only lowers b(w).  By U4 Lemma GW every window condition used by Q1, Q2, K1 is
monotone under these changes; the window count (cert3 Fix A) is unchanged in form: the M(L) = omega(L) + 1 sub-windows have pairwise disjoint
nonempty bands (u(w^+) = b(w) < u(w)).  QED
### 6.3 LEMMA K2.13 (clean dichotomy at depth D(L) along the construction).  PROVED.
At a clean w (for the enlarged scheme; exists by Q1 Theorem VI Step 1), for every s <= D(L) at f: |a_s| <= b or >= u, and 1 - |z_s| <= b or >= u.
Along f -> f^r (deep raise, J(w) > D(L): moduli change by the factor 1/lambda_r, K1-ref R-1) -> Step 0 ((C1), (C2) close rooms; weak-peak pushes
move values by <= Design^C b/u << u, R-8) -> (P) -> Step A (moves <= Design^C x'_max << u; S_th with data only raised) -> pre-row (moves <= K_w Pi
<< theta_0) -> approximant (Sys-DC moves <= Design K_DC r <= theta_0/4), every s <= D(L) keeps its class in the sense of 4.1(d).  QED
### 6.4 LEMMA K2.14 ((LATE) additions).  PROVED.
 (L-K2-1) s_1 <= theta_0 T/(8 rho A_0);   (L-K2-2) Design(L) K_DC r <= theta_0/4;   (L-K2-3) C_lev K_DC r <= min(gap_min, robust margins)/2;
 (L-K2-4) [only with K2.1] C_f |Omega| A_2^2 K_w^2 s_1 <= c_late delta T^2;   and eps_E <= eps_DC/8 (Theorem K2.6 Step 1).
All hold with Lemma S2c^tr's s_1 := max(64 rho eps^viol/delta, exp(-1/(2T))) for T small.
Proof.  b(w) is bounded below by a power of eta'(w) = T^4/(L Design(L)) with exponent and constants bounded by powers of Design(L) (b_U4 =
(eta/C_L)^{N_L/2}/(1 + Lip C_*); b_X1 via (D1), (D2), mu_kappa(h) >= c_kappa h^{beta_kappa}; R-8(ii)'s factor Design^C/u(w) with u(w) >= 4
log_2(1/T)^{-1/20}); with Design(L) <= n(w) <= log_2(1/T) (Lemma S2c^tr (i)), log(1/b) <= C log^3(1/T) and theta_0 >= exp(-C log^3(1/T)).  On the
other side r <= exp(C log^2(1/T)) s_1, K_DC <= C_{f,N} log^{C_0}(1/T), C_lev, K_w <= exp(C log^2(1/T)), and s_1 <= (1 + 32 rho/delta) exp(-1/(2T)) <=
exp(-C' log^3(1/T)) for T small.  eps_E <= C_f Design^C (K_w Pi + c_{L+1}) with Pi <= K_w s_1 and c_{L+1} <= exp(-1/T) ((W_exp)).  QED
### 6.5 Costs (theta'/c_flat^2 -> 0, K1-ref R-6).  PROVED.
With c_flat(w) >= c_f u(w) and theta' T^2 bounding all companion costs: preparation <= C D(L) b log(1/b) <= C T^4 log^3(1/T); Step A <= C_f Design^C
W log(1/W) with W <= Design^C x'_max, i.e. <= C u^2 T^3 log(1/T); pre-placements <= C Design |Lambda| x'_max log(1/T) (R-6).  Each divided by u^2 T^2
tends to 0 (u^2 >= 16 log_2(1/T)^{-1/10}).  Sys-DC moves are inside Theorem UE^inf's Pi-budget (K_J -> K_DC).
### 6.6 Audit (where each new object is used).
D(L): Theorem K2.6 Step 3, Theorem K2.16 (1) (tails), 4.1(d), J(w), N_w > D(L).  Design(L) >= 2^{D(L)}/mu*_{D(L)}^2: efficiency of every
design-depth resource >= 1/Design(L).  (R-mod'), (R-room): thin/thick and tiny/robust-room classification at depth <= D(L) (without them a
coordinate with b < |a_s| < u could be neither raised -- it is not tiny -- nor used two-sided at scale x >= Design b).  theta_0: S_th; (L-K2-1),
(L-K2-2).  Doubled b: preparation before the Lojasiewicz step.  None of the new objects enters K, D_cls, A_max or c_flat; they enter only window
constants (K_DC, ranges) and (LATE), so Lemma S2c^tr and the hypotheses (E-c)-(E-f) of Theorem E^{eng,RT,inf} are unchanged.

## 7. Combination with K1 (and K1-ref)
### 7.1 THEOREM K2.15 (transport at A-regular rows).  PROVED modulo the cited chain (X2/X2-ref, Q1/Q1-ref/cert0-3, Q2/Q2-ref a, K1/K1-ref; the
once-refereed links listed there).
Design T_fin^{K2} (6.1).  Let N >= 1, f in S_{p_N*} with base support F finite or infinite, g in C(f), rho in (0, 1).  Suppose that for infinitely
many main stages L there are a clean sub-window w of L and a class a with >= n(w)/D_cl(w) scales (K1 Lemma K1.1, Lemma-P thresholds) such that
 (H1) [K1-ref R-8, extended]  every active weak peak k of a (T)-block has a push resource: a pullable far coordinate at depth in [2b theta Phi_k/m,
      x'_max], a (P3) or (P4) resource on k, a near bank if Delta''_m > 0, or any design-depth move of K2.4 (TS, S_th raise, bank, FR, ZD)
      lowering eps_k val_k with efficiency >= 1/Design(L) and admissible for its data;
 (H2)  Step A is A-regular (5.2) after Step 0 and the preparation (P).
Then (f, rho g) lies in the closure of NA((c_0, p_N), l_2^2) along norm-attaining rows with FINITE base support; in particular (LSC-trunc)_N
holds at (f, g, rho).  If the hypothesis holds for every (g, rho), then f in Rec(p_N).
Proof.  K1 4.1 Steps 1-7 with K1-ref's R-3 (class constants), R-6 (x'_max; (E-d)'s third condition, 6.5), R-8 (Step 0 under (H1), enlarged (D1)),
and with two replacements.  Step 4 (Step A): Step 0, then (P) (4.1; costs 6.5), then the realization of Sys-A by Lemma K2.9(c) under (H2)
(exact ratios on Z_kappa, exact KN-1 zeros, Puiseux protection, robust statuses; K1 Lemma K1.6(A)'s conclusions), types of 4.1(d); the new
Step-A generators (elementary moves at design-depth TS, FR, ZD coordinates and raises of S_th coordinates) have the costs of 6.5, move robust
objects by <= Design^C W << u (K1 2.1(f)), keep support signs, and act on coordinates whose data are aligned, zero, or cushion dominated
(4.1(c)).  Step 6
(engineered approximant): Lemma DC^inf from Theorem K2.6 (uniform, no hypothesis; K_DC <= C_{f,N} Design^{C_0} plays the role of K_lev), so neither
K1's Sys-DC half of (LR) nor R-7's scalars are needed.  The remaining steps (classes, data with C_+ = 5, Theorem UE^inf, averaging by Theorem
E^{eng,RT,inf}) are K1 4.1 verbatim; the new window constants are of the form design x u^{-C} or <= exp(C log^2(1/T)) (6.4), so Lemma S2c^tr holds.
The design is one N-independent design (Lemma K2.12).  QED
### 7.2 Explicit sufficient conditions (PROVED).
(LSC-trunc)_N holds at (f, g, rho) if (H1) holds and, at infinitely many main stages, one of Corollary K2.17 (a)-(g) holds -- e.g.
 - every tuned carrier is privately tunable (K1 Corollary K1.C (a)-(c), K1-ref R-12);
 - F has a thick coordinate at depth <= D(L) outside U_L (an anchor);
 - some coarse carrier k (tuned or a peak) has, in S_k ∩ [1, D(L)] and private to k, a thick coordinate together with a free or zero-data
   coordinate, or together with a banked/raised data coordinate of the same sign, or two thick coordinates with robust spread;
 - the only non-privately-tunable carriers are (S') = (S) ∪ (M) and the needed correction in the degenerate direction points DOWN, or a
   bordered scalar is robust.
In the first three cases the Step-A resources positively span (eps_PS >= Design(L)^{-C}), so Step A is solvable for every right-hand side.
Compared with K1 Theorem 5.1 / K1-ref E, the hypothesis is weaker: the Sys-DC half of (LR) is dropped, the Sys-A half is replaced by the cone
condition (H2), and K2.17 adds the depth-D(L) criteria (b)-(e).
### 7.3 The remaining class (precise).  OPEN.
(f, g, rho) is NOT covered by Theorem K2.15 iff for all but finitely many main stages L, at every clean sub-window and admissible class,
 (W)  some active weak peak of a (T)-block has no push resource in the sense of (H1), or
 (A*)/(U*)  Step A has a near-certificate y (5.7): robustly negative common mode gamma <= -c_*, thick support at depth <= D(L) proportional to
      Psi_y with no anchor and none of Corollary K2.17 (b)-(e), positive one-sided mass >= c_*/2, and (by 5.6, SKETCH) no far move against the
      certificate.
This class is contained in the non-lever-regular class of K1 4.3 / K1-ref R-10-R-13, and strictly smaller as a class of configurations (it
excludes every configuration whose only failure is in Sys-DC, every (S')-only configuration with downward correction, and every configuration
with an anchor or a private thick coordinate of the kinds in K2.17 (b)-(e) at depth <= D(L)).  It contains no configuration known to be
realizable at ALL large main stages; it is not shown to be empty.

## 8. What remains open; main obstacle; next steps
OPEN: (LSC-trunc)_N for every f; hence density of NA((c_0, p_N), l_2^2) for any N (Theorem VI.2 of Q1: density <=> (LSC-trunc)_N) and of
NA((c_0, p), l_2^2) (Corollary VI.3: (LSC-trunc)_N for infinitely many N suffices).
MAIN OBSTACLE.  Step A's targets are RATIOS fixed by the Lojasiewicz/Puiseux step at displacement scale x >= Design(L) b, while every move that keeps
the tiny objects tiny has size <= b; so data-carrying contacts and thin coordinates give only ONE-SIDED resources at the scale x, and in a square
system the final lever positions are forced by the targets (K1 2.2).  The obstruction is the sign class (A*)/(U*) of Theorem K2.16 (and its
Step-0 analogue (W)): a combination Psi of carrier vectors with robustly negative common mode that reproduces the whole thick support at
design depth.  Preparation of the base row (the remedy for Sys-DC) cannot help Step A because Sys-A's targets are not the values of the row.
NEXT STEPS.  (1) Target freedom: if the exact set Z_kappa of the Lojasiewicz step has positive dimension at the selected point, choose the target
r'' so that y^T Ft(f_1) <= 0 for the (finitely many, by compactness) near-certificates; this would remove (A*)/(U*) without new levers
(HEURISTIC; needs the local structure of Z_kappa from Lemma QC).  (2) Prove the push lemma (mirror of V1 Lemma TU) and the overshoot argument of 5.6
in general (degree argument on the cone of pre-placements).  (3) Use the infinite-depth exact-limit structure 5.7 (a|_{F_thick} = Psi/kappa at
every large stage with kappa <= -c_*/nu) together with Q2's identity h^T F = -(kappa nu/2)||Delta e||^2 + tau_W + tau_z to look for a contradiction
or for an explicit row realizing (A*) at all stages (a counterexample would have to be checked against every alternative lever, so scepticism
is required).  (4) For (W): raising another robust peak of the same block raises theta_m and lowers rho_k (Martin block threshold equation) --
an additional push resource to be checked (HEURISTIC).
POINTS FOR A REFEREE (where this file relies on a claim not re-derived here).  (R1) 4.1(c): the +- pieces of the window family at the
theta_0-banks are aligned, as at K1's TU banks.  (R2) Theorem K2.16 uses Xt_m <= 1/4 (U1 Lemma 1.4(c)); numerics 9 show this is a property of U1's
regime, not of general blocks.  (R3) Theorem K2.6 Step 1 uses Q2 4.0's column form with D = I + X and q_m^T D^{-1} p_{m'} = delta_{mm'} q_m^T p_m <=
1/2 (Q2, Q2-refa C.1, K1-ref R-7).  (R4) Lemma K2.9(c) treats K1's TU levers as pre-placement (pull + base bank) plus a two-sided bank, as in V1
Lemma TU Step 2.  (R5) Pushes (5.6) are the mirror image of V1's pulls; only the SKETCH of 5.6 uses them.

## 9. Numerics (sanity only; r11/K2_work/)
 identity_check.py: Lemma K2.2 exact to 3.8e-14 (400 random rows); Lemma K2.3 never violated (all depths D).
 fo_check2.py (mpmath, 60 digits): Lemma K2.4 (i), (ii) relative error 1.9e-16 (fo_check.py in double precision shows cancellation at deep
   coordinates, relative 18.8; not an error of the lemma).
 psi_check.py -> psi_check.out (exact one-block Martin-type model, threshold equation, diagonal base; adapted from Q2-refa's smass_jacobian.py):
   (a) max |Psi_y(zhat_0)| = 2.8e-16 over random y; (b) 3468 elementary moves (support masses, banks, z-moves): y^T c = l_delta(Psi_y) to relative
   2.9e-5 (finite differences, step 1e-7); (c) Lemma K2.3 with u = Psi_y: no violation.
 euler_check.py -> euler_check.out: kappa = A + theta Phi_P^2 + S/theta is 1-homogeneous (4.6e-16) and satisfies Euler's identity (5.2e-9) while the
   peak set is fixed (Lemma K2.8); euler_share_probe.py: in GENERAL blocks the non-peak Euler share X reaches 1.85 (so 1 - X can vanish); K1's
   use of X_m <= C c^2 D^2 rests on U1 Lemma 1.4(c)'s regime, not on the block norm alone.
