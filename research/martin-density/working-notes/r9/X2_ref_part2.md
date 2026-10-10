# X2-ref part 2 — Lemma DC (exact d-consistency by levers) and Lemma LV (levers at U1's companions)

Refereed against: X2 part 2; U1 parts 3-4 (A0 absorber targets, Lemma 3.2, Lemma 3.3, Proposition 3.4, Lemmas 4.1, 4.2, 4.6), U1-ref
Sections 5-6 (G1 release, D^{U1'}), V1 Lemma TU as quoted, lem:F1 (clamp formula), Lemma M1.  Scripts: X2's dc_jacobian.py, dcons_check*.py
(re-run: outputs identical), my absorber_check.py (+ .out).

## 2.1 Lemma DC as an abstract statement.  Verdict: CORRECT (PROVED) after three precisions (p-DC1)-(p-DC3).
Re-derived.  (i) Levers have exact first-order slope 1 in eps_l u_l: z-moves by construction (z(j) - z_1(j) = eps_l P/v_l(j), u_l(j) = v_l(j)
— this presupposes v_l > 0 on S_l, true for SLD signatures delta_l h_l with h_l >= 0; otherwise replace v_l(j) by |v_l(j)| and adjust signs);
banks/S-masses through Lemma M1(i): a mass c at s changes u_l(xhat) by c mu_s^2 u_l(s)/nu + O(c^2) when s notin supp A_1, so beta_s = nu/(mu_s^2 v_l(s))
gives slope 1; masses at s in supp A_1 add the first-order nu-effect Y of (3') (correctly bounded).  (ii) The derivative of the block norm
A_m at the current point is <w_m, R_m dxhat> (smooth norm), and a lever of carrier k changes only u_k at first order (diagonal base;
(SEP)(ii)), so dA_m/dP_k = eps_k lambda_k w_m(k): the Jacobian of F is I - p q^T blockwise with p_l = eps_l u_l(zhat_0)/A_m^0,
q_k = eps_k lambda_k w_m^0(k).  (iii) q^T p = sum_{Omega_m} w_m^0(k) nv_k = sum_{Omega_m} Phi_k^2 w_m^0(k)^2/C_m in [0, C_m], C_m <= 2^{-m} <= 1/2, so
(Sherman-Morrison) ||(I - p q^T)^{-1}||_inf <= 1 + ||p||_inf ||q||_1/(1 - q^T p) <= 1 + 2/A_min (|u(zhat_0)| <= q*(u) q**(zhat_0) = 1).  (iv) Poincare-
Miranda on the cube with the face estimates is correct.  The rank-one remark (no second lever needed for d-CONSISTENCY, in contrast
with U1-ref Lemma R-kt, which concerns moving statuses at fixed ratios) is correct.  X2's numerics re-run: J_fd = I - p q^T to 2.1e-10.
(p-DC1) Radius.  |F(0)|_inf <= delta_1 (1 + 1/A_min) (|A_m(1) - A_m^0| <= sum_k lambda_k |Delta u_k| <= delta_1), so the hypothesis K_J |F(0)| <= r/2
is met by r := 4 K_J (1 + 1/A_min)(delta_1 + ...), not by X2's r := 4 K_J (Pi_X + T^4 s_1) (3.2(iii)); harmless (a window constant).
(p-DC2) TU pulls are FIXED O(1) moves (z(j_p) flips by 2), not "per unit r": a carrier k != l meeting j_p moves by 2|u_k(j_p)|, not by C_lev r.
The correct accounting: let W_pull := sum of lambda_k over carriers k != l whose vectors meet a pull coordinate.  These carriers are at stages
>= j_p (allowedness (c): supp y_k ∩ S_l ⊂ [1, k]) and j_p ~ log_2(1/r), so W_pull <= 2 m c_{stage j_p}, super-small against every window
quantity (weights decay super-exponentially).  Their effect on the block norms (<= 2 W_pull) enters F(0) and must satisfy
2 K_J W_pull <= r/4; their effect on the Bregman term and the scrambled set is <= C W_pull (Theorem UE, part 3).  All harmless; but the
statements "every carrier value moves by at most delta_1 + C_lev r" and Lemma UE-1(b) "carriers meeting lever coordinates move by
<= C_lev r" are false for carriers meeting pull coordinates.
(p-DC3) "the peaks of f_0 of every block remain peaks": only peaks whose margin exceeds the value moves (in particular all coarse
peaks); fine peaks with tiny margins may change status (harmless: they carry no switching coefficient).

## 2.2 Lemma LV (levers at U1's companions).  Verdict: (a)-(c) CORRECT for the coarse carriers (with (p-LV1), (p-LV2));
## (d) FALSE IN THE APPLICATION — the zero-value absorbers cannot be re-tuned at the engineered approximant.
(p-LV1) (D-lev) gives mu_{j(l)}^2 delta_l 2^{-j(l)} >= Design^{-1}; with v_l(s) = delta_l 2^{-s}/n_l this is mu^2 v_l >= 1/(n_l Design): add n_l to
Design (a design number of level L).
(p-LV2) The pull coordinates j_p with v_l(j_p) in [r, 2^G r] lie in E_c(w) (not in J_fine) whenever r >= 2^{-s_far(w)}-scale, which is the case
for X2's parameters (s_1 >= exp(-1/(2T)) >> c_{L+1}^2 >= 2^{-s_far}): they are coarse contacts closed by (C1) with z = eps_l, and their data are
contact-like by EXACTNESS ON E_c (U1 Prop. 3.4), not by ownership/dominance as written.  Conclusion of (a) unchanged.
THE ABSORBER GAP (main finding).  Lemma DC is applied with Omega ⊃ the tuned absorbers (first pairs P(s), s in E_c(w), and the cluster of
L), each re-tuned to value exactly 0 at f' by an (S-mass) lever at its tuning coordinate p_0.  This fails:
 (A1) Size of the needed correction.  Every lever of a coarse carrier acts at coordinates of E_c: the bank / inward z-move at j(l) and the
      pull at j_p (both in S_l ∩ (s_max, s_far]).  Each such coordinate s has its own first absorber pair P(s), and |u_a(s)| = |y_a(s)|/n_a >=
      1/(8 n_a) (U1 (A0)).  A z-move of size Delta z at s changes u_a by |u_a(s)| Delta z: the pull flip (Delta z = 2) changes it by >= 1/(4 n_a);
      the Z/bank lever by |u_a(s)| r/v_l(s) >= r/(8 n_a Design).  Window theta-masses at s change it by m_s mu_s^2 |u_a(s)|/nu.
 (A2) Room.  An absorber a is a strict non-peak iff m |u_a(xhat)| < theta Phi_a (lem:threshold), i.e. its value room is theta Phi_a/m ~
      lambda_a (theta = A M/C an f-constant).  Absorbers for s in S_l ∩ (L, s_far] are pre-pairs / later cluster pairs, at stages > L with
      lambda_a <= c_{L+1}, and for s in (L, N_w] typically at stages ~ s or later (weights super-exponentially small in s).
 (A3) Range of the S-mass lever.  Changing m_0 by Delta m changes u_a by Delta m mu_{p0}^2 u_a(p_0)/nu, and m_0 >= 0 must hold (sign of
      the support coordinate, and t|b_t(p_0)| <= m_0 for no flips): in the decreasing direction the range is <= m_0 mu_{p0}^2/nu ~ lambda_a T_hi
      mu_{p0}^2 (p_0 fresh, beyond every earlier coordinate); in the increasing direction the needed mass is Delta u nu/(mu_{p0}^2 |u_a(p0)|),
      which for Delta u >= r/(8 n_a Design) is astronomically larger than 1 and destroys the row (q*(a') >> 1).  These are NOT design
      quantities of level L: the "Consequence" of Lemma LV (r_0, C_2, K_J <= f-constant x Design(L)^C) is false for (d).
 (A4) Consequence.  For the radius r >= 4 K_J T^4 s_1 forced by (VT') and X2's choice s_1 >= exp(-1/(2T)) (part 4.2), r >> lambda_a for every
      absorber of the window: the S-mass levers cannot restore u_a = 0; Lemma DC's hypothesis r <= r_0 fails.  Without re-tuning, every
      absorber met by a lever becomes a PEAK of f' (value change >> room), and since its switching coefficient Domega(a) = gamma_a/lambda_a is
      nonzero (biased pairs: gamma_a >= c_0/4 > 0; used pairs: |Domega(a)| up to C_f Design^2), the block expansion acquires the FIRST-ORDER
      term |sigma omega^diamond(a)| (lem:block(c) fails at a peak with omega(a) != 0): in the theta regime this is rho|tau||Domega(a)|/2, not O(tau^2).
 Numerical illustration (absorber_check.py; one block; carrier l with signature on {3,4,5}, absorber a with Phi_a = 1e-7 on {s = 4, p0, p1},
 mu_{p0} = 1e-3, tuned to value 0 by m_0 = 1.6e-2): an inward lever move of l at s lowering u_l by P = 1e-6 moves u_a to 7.4e-6 resp. 1.4e-5
 (beta = +1 / -1), 90-170 times its room theta Phi_a = 8.3e-8; the absorber becomes a peak; restoring u_a = 0 by the S-mass needs a NEGATIVE
 mass (beta = -1: none in [0, 1e14 m_0]) or a mass 10^3 m_0 = 17 (beta = +1), i.e. the row's base part is replaced; for P = 1e-3 no admissible
 S-mass exists for either sign.
 (A5) The same obstruction hits Lemma UE-1(e)/(U5) as used in Lemma CM(a): a tuned absorber of a negative block 1 is a strict non-peak with
      Phi_a gap ~ Phi_a M, so it contributes Phi_a to Scr_1(x) for every x >= Phi_a M, and Scr_1(x) <= C_S x^2 fails for x ~ Phi_a; X2's claim
      x_0(f^#) >= c_f gap_min Phi_min(L) "(tuned absorbers gap 3M/4)" confuses the gap (robust) with Phi x gap (tiny).  (With exact
      d-consistency the absorbers are in S_2 and not scrambled, so this point alone would only need a re-reading of Lemma UE-1(e); but
      d-consistency of absorbers is exactly what fails.)
REPAIR (R-abs) (PROVED in part 4): in the violation-tolerant route the absorbers are not needed at all.  Give them NO switching coefficients
(they become ordinary fine carriers of block 1, owner-candidates of type (d) when block 1 is active) and tolerate the fine residues on E_c and
the trace corrections of U1 Lemma 4.6(b) as contact/free violations of total mass <= C_f Design c_{L+1} (with the symmetric split chi = 1/2 of
the fine part at free coordinates, so that (H3) holds).  Then Omega = coarse strict non-peaks only, every lever of Lemma LV (a)-(c) has
design-quantity constants, Lemma DC needs no absorber block and no (S-mass) lever, and the levers' perturbations of fine carriers
(former absorbers included) cost only C x (their total weight) <= C c_{L+1} in the Bregman and scrambling terms.  The zero-data property
of (b), (c) becomes "data = fine residue at j(l)", a tolerated violation (counted in eps).  See part 4.
