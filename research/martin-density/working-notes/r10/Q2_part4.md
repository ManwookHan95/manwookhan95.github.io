# Q2 part 4 -- the degenerate lever configuration (NDN) in the d-consistency system: block-norm bordering

Setting: X2 Lemma DC (r9/X2_notes.md 2.1-2.2) at a base row f_1 of ARBITRARY support, with some levers of type (S-mass) placed at THICK
support coordinates (part 3, (L3)/(L4)); diagonal base.  Labels PROVED / SKETCH / HEURISTIC / OPEN.

## 4.0 The exact linearization with S-mass common mode (PROVED; X2 Lemma M1(iv) and DC step (3'))
For a lever l of type (S-mass) at p_l in F with ratio rho_l := A_1(p_l)/u_l(p_l), a unit lever step changes A(p_l) by
sgn(A_1(p_l)) beta_{p_l}, beta_p = nu_1/(mu_p^2 |u_l(p_l)|), hence (Lemma M1(iv)) every raw value u_k(xhat) at first order by
      eps_k [ delta_{kl} - g_k h_l ],   g_k := eps_k <U* u_k, e_1>,   h_l := |A_1(p_l)|/(nu_1 |u_l(p_l)|)  (h_l := 0 for Z/TU levers).
The common mode also moves every block norm: dA_m = q_m^T dP - G_m (h^T dP), G_m := sum_{k in block m} lambda_k w^0_m(k) <U* u_k, e_1>
(all carriers of the block, peaks included).  So the Jacobian of X2's map F at P = 0 is, exactly (up to the data-replacement terms of DC (3)),
      N := D - gt h^T - sum_m p_m q_m^T,      D := I + X,      gt := g - sum_m G_m p_m,
with X2's p_m (p_l = eps_l u_l(zhat_0)/A^0_m on Omega_m), q_m (q_k = eps_k lambda_k w^0_m(k) on Omega_m), and the absorber matrix X
(X_{ak} != 0 only for a absorber, k in Omega^0; so X^2 = 0, D^{-1} = I - X, and q_m^T X = 0 since q_m vanishes on absorbers).  X2 required
K_J ||Y|| <= 1/2 for the rank-one term Y = -g h^T; at infinite F with thick |A_1(p_l)| this fails.  Note h^T g = sum_l rho_l gamma_l/nu_1^2
(gamma_l = <U* u_l, U* A_1>): 1 - h^T g is the Sherman-Morrison denominator of part 3 (L4).  By the capacitance (Woodbury) formula
      det N = det D * det C,  C = I - [h q_1 ... q_M]^T D^{-1} [g p_1 ... p_M],  C_{mm'} = delta_{mm'}(1 - q_m^T p_m) (m, m' >= 1),
and q_m^T p_m <= C_m <= 1/2 (X2 DC step (3)), so N has AT MOST ONE degenerate direction; for one block det N = (1 - q^T p)(1 - h^T g) -
(q^T g)(h^T p) (checked numerically, Q2_work/border_check.py).  In particular (NDN) in the sense of part 3 (h^T g = 1) is NOT by itself a
singularity of the d-consistency system: the block-norm coupling q^T g h^T p enters.

## 4.1 Proposition 4.1 (block-norm bordering).  PROVED.
Let D = I + X as above, g, h in R^Omega, p_m, q_m supported in the disjoint sets Omega_m (m = 1..M) with q_m^T p_m <= 1/2 and q_m^T X = 0,
and let m* be a block and pi != 0.  Consider the bordered linear map (P in R^Omega, P_0 in R)
      L(P, P_0) := D P - g (h^T P) - sum_m p_m (q_m^T P) - pi p_{m*} P_0.
Put K_D := 1 + ||X||_inf, Q := sum_m ||q_m||_1, pbar := max_m ||p_m||_inf, H := ||h||_1, and
      c_alpha := 1 - h^T D^{-1} g - sum_{m != m*} (h^T D^{-1} p_m)(q_m^T D^{-1} g)/(1 - q_m^T p_m),      beta_* := h^T D^{-1} p_{m*}.
If max(|c_alpha|, |beta_*|) >= beta_0 > 0, then for every b in R^Omega there is (P, P_0) with L(P, P_0) = b, depending linearly on b, and
      ||P||_inf + |P_0| <= K ||b||_inf,   K := 4 (1 + 1/|pi|) K_D^4 (1 + pbar)^2 (1 + Q)^3 (1 + H) (1 + ||g||_inf) (1 + 1/beta_0),
a bound INDEPENDENT of the Sherman-Morrison denominator 1 - h^T g and of det N.  (Applied below with g := gt of 4.0.)
Proof.  Note q_m^T D^{-1} p_{m'} = q_m^T p_{m'} - q_m^T X p_{m'} = delta_{mm'} q_m^T p_m.  We look for P = D^{-1}(b + g alpha + sum_m p_m gamma_m) with
scalars alpha, gamma_m and require (i) h^T P = alpha, (ii) q_m^T P = gamma_m for m != m*, (iii) P_0 := (gamma_{m*} - q_{m*}^T P)/pi.  Then
D P = b + g (h^T P) + sum_{m != m*} p_m (q_m^T P) + p_{m*}(q_{m*}^T P + pi P_0), i.e. L(P, P_0) = b.  Condition (ii) reads
gamma_m (1 - q_m^T p_m) = q_m^T D^{-1} b + (q_m^T D^{-1} g) alpha, so gamma_m := [q_m^T D^{-1} b + (q_m^T D^{-1} g) alpha]/(1 - q_m^T p_m)
(denominator >= 1/2).  Substituting, (i) becomes the single scalar equation
      c_alpha alpha - beta_* gamma_{m*} = h^T D^{-1} b + sum_{m != m*} (h^T D^{-1} p_m)(q_m^T D^{-1} b)/(1 - q_m^T p_m) =: rhs.
Case |beta_*| >= beta_0: take alpha := 0, gamma_{m*} := -rhs/beta_*.  Case |c_alpha| >= beta_0: take gamma_{m*} := 0, alpha := rhs/c_alpha.
Bounds (B := ||b||_inf): ||D^{-1}||_inf <= K_D; |rhs| <= H K_D (1 + 2 pbar Q K_D) B; R := |rhs|/beta_0 bounds |alpha| and |gamma_{m*}| in
both cases; |gamma_m| <= 2 ||q_m||_1 K_D (B + ||g||_inf R) (m != m*); hence
||P||_inf <= K_D (B + ||g|| R + pbar sum_m |gamma_m|) <= K_D [(1 + 2 pbar Q K_D) B + (||g|| + pbar + 2 pbar Q K_D ||g||) R]
         <= 2K_D^2 (1+pbar)(1+Q) B [1 + 2 K_D^2 (1+||g||)(1+pbar)(1+Q) H/beta_0] <= K_0 B,  K_0 := 4K_D^4 (1+pbar)^2 (1+Q)^2 (1+H)(1+||g||)(1+1/beta_0),
and |P_0| <= (R + Q ||P||_inf)/|pi| <= (1 + Q) K_0 B/|pi|; so ||P||_inf + |P_0| <= (1 + Q)(1 + 1/|pi|) K_0 B = K B.  QED
Remarks.  (a) Without the bordering column (X2's square system, P_0 = 0) the condition is |det C| >= beta_0, i.e. a codimension-ONE
non-degeneracy; with one block-norm lever the degenerate set is {c_alpha = 0 and beta_* = 0}: codimension TWO, and with block-norm levers in
several blocks m*, codimension 1 + (number of such blocks).  (b) General bordering (also PROVED, elementary): if s_{n-1}(N) >= sigma > 0 and
y_0 is a unit left singular vector of s_n(N), then s_min([N | w]) >= 1/(1/sigma + (1 + ||w||/sigma)/|y_0^T w|) (write y = t y_0 + y_perp;
||y^T N|| >= sigma ||y_perp||; |y^T w| >= |t| |y_0^T w| - ||y_perp|| ||w||).  Checked numerically (border_check.py: ratio >= 1.027 over 2000 trials).

## 4.2 Corollary 4.2 (Lemma DC^inf: exact d-consistency with thick S-mass levers).  PROVED as a modification of X2 Lemma DC.
Let f_1 be a pre-row of arbitrary support, Omega, levers as in X2 2.1 except that (S-mass) levers may sit at thick support coordinates (no
smallness of Y), and suppose in addition a BLOCK-NORM LEVER for one block m*: a coordinate j off supp A_1 in the signature set S_{k*} of a peak
k* of block m*, beyond s_max, lying in no supp u_k (k in Omega, k != k*) and carrying data V_fine(j) only (zero-data lever (Z-gen) of X2
Lemma LV(c)), normalized so that a unit step moves u_{k*}(xhat) by eps (sign chosen); then dF = -p_{m*} pi dP_0 with
pi := eps lambda_{k*} w^0_{m*}(k*), |pi| = lambda_{k*} M_{m*} (k* is a peak).  If max(|c_alpha|, |beta_*|) >= beta_0 at f_1
(rate objects of the level), then the conclusion of Lemma DC holds with K_J replaced by the K of Proposition 4.1: F has a zero (P*, P_0*)
with |(P*, P_0*)| <= K r, the peaks remain peaks (k* moves by <= K r, below its margin for r <= r_0), and exact d-consistency nv_l = nv_l^0
holds on Omega.
Proof.  X2 DC steps (1), (2), (5) verbatim (the block-norm lever moves z at one coordinate of S_{k*}; it changes no Omega value since
j notin supp u_k, and A_{m*} at first order by pi |A^0| per unit through k*, the fine carriers meeting j entering c_tiny).  Step (3): the
Jacobian is the bordered map L of Proposition 4.1 (with the remainder bounds of DC (3'), unchanged: masses enter smoothly with constants of the
lever data).  Step (4): let R_b be the linear right inverse of Proposition 4.1, ||R_b|| <= K; put (P, P_0) := R_b y and G(y) := F(0) + y +
Rem(R_b y); on the cube |y|_inf <= r, G_l >= r - |F(0)| - C_2 K^2 r^2 - c_tiny K r >= 0 on y_l = r (and <= 0 on y_l = -r) under
K|F(0)|_inf <= r/2, K C_2 r <= 1/4, K c_tiny <= 1/4: Poincare-Miranda gives G(y*) = 0.  QED

## 4.3 Lemma 4.3 (structure of exact full degeneracy at infinite F).  PROVED.
Let u = sum_{k in Lambda} c_k u_k be a finite combination of coarse carriers of level <= L such that the first-order effect of EVERY support
move vanishes on the combination, i.e. P_F (I - e e^T) U* u = 0 (P_F := orthogonal projection onto span{k_s : s in F}).  Then
 (a) u|_F = kappa a|_F with kappa = <U* u, U* a>/nu^2 (the hypothesis of Lemma 3.4);
 (b) if kappa != 0 then F is contained in supp u, a union of finitely many carrier supports;
 (c) if moreover the design's privacy holds (supp u_k cap S_{k'} subset [1, s_max(L)] for coarse k != k', X2 Lemma LV (SEP)(ii)), then for
     every coarse carrier k' notin Lambda -- in particular every peak -- the coordinates of S_{k'} beyond s_max(L) are OFF the support F.
Proof.  (a) P_F U* u = U*(u 1_F) (diagonal base) and P_F e = e, so the hypothesis is U*(u 1_F) = <U* u, e> e = (<U*u, e>/nu) U* a, and U* is
injective coordinatewise (mu_s > 0).  (b) For s in F, u(s) = kappa a_s != 0.  (c) Such s lies in no supp u_k, k in Lambda (privacy, k != k'),
hence not in supp u, hence not in F by (b).  QED
Consequence.  In the EXACT full-degenerate configuration every block has peak zero-data levers (Corollary 4.2 applies whenever
max(|c_alpha|, |beta_*|) >= beta_0 for some block), and if kappa = 0 the carriers of Lambda do not meet F at all (no S-mass levers needed).

## 4.4 What remains of (NDN) for d-consistency (refines part 3, Remark 3.5)
(i) PROVED: with a block-norm lever in some block, the d-consistency system degenerates only on the codimension-two set
     (NDN2):  c_alpha ~ 0  AND  beta_* = h^T D^{-1} p_{m*} ~ 0,
where, up to the absorber correction X (whose h-entries are <= C_f c_{L+1}), beta_* ~ sum_{l in Omega_{m*}} rho_l u_l(zhat_0)/(nu_1 A^0_{m*})
(the rho-weighted base value of the S-mass carriers of block m*) and c_alpha ~ 1 - sum rho_l gamma_l/nu^2 - (block-norm terms).
(ii) PROVED (Lemma 3.4 + 4.0): in the EXACT version of (NDN2) with exact full degeneracy, the degenerate combination of the d-consistency
equations is moved by support moves only at SECOND order (raw part: -(kappa nu/2)||Delta e||^2; normalized part: sum_m (Delta A_m/A_m^0)
h^T p_m A^0_m = 0 at first order), plus tau := the first-order effect of moves at coordinates of supp u minus F (window theta-masses on
W cap supp u, the cut-off beyond N''; the latter is a tail, <= sum_{j > N''} |u(j)|).
(iii) OPEN: whether tau_W (window masses on W cap supp u, first order in s_1 with a window-dependent constant) is compatible with the tolerance
|kappa^+-| <= c delta s_1 of Theorem UE^inf in the exact (NDN2) configuration, and the quantitative (near-degenerate) version of (NDN2) when it
is not separated by the design pigeonhole.  (NDN2) is non-generic (codimension two in the level-L data; destroyed by an arbitrarily small
raise of a on the lever coordinates, V3 RT, but a raise moves the base row and the drift identity of Lemma 3.4 caps what such a raise buys).
(iv) The same bordering would apply to the KN-1 holds of Q1's Step A (raw zeros, values r''_l kappa) if one of the per-block kappa
restorations (peak pushes) can be traded for the degenerate direction; whether the pattern's ratio system Z_kappa admits this is NOT
checked (OPEN).  In route V's KN^tr the holds use TU levers at contacts of the carrier's own set; at infinite F these are S-mass levers only when
the first two coordinates of S_l beyond s_max are thick support coordinates.

## 4.5 Numerics (evidence only)
Q2_work/border_check.py: bordering bound of Remark (b) holds (min ratio 1.027 over 2000 random near-singular N); Woodbury determinant formula
exact to 1e-14.  Q2_work/prop41_check.py: the explicit right inverse of Proposition 4.1 (3 blocks, absorber matrix X, exact c_alpha = 0 or
exact beta_* = 0 in 2/3 of the 3000 trials) solves L(P, P_0) = b to 2.5e-12, and (||P|| + |P_0|)/(K ||b||) <= 6.7e-6 (K is crude); with one
block and EXACT Sherman-Morrison degeneracy 1 - h^T D^{-1} g = 1e-16, X2's square determinant is -7.25, equal to the formula: the
block-norm coupling alone keeps the d-consistency system regular.
