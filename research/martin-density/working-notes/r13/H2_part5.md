# H2 part 5: can exactness be relaxed?  Near-exactness (NE), the preparation bias, and what drives the residual

Setting of H2_part1-4.  s_1 = the theta-threshold of Theorem UE^inf at the stage (s_1 <= s_late(w), X2 3.2 (LATE)); Lemma VT (U3 4.2):
violations of l_1-mass eps are tolerated when 64 rho eps <= delta s_1 (VT'); r = Sys-DC lever radius (r >= K_DC |F(0)|, F(0) ~ K_w Pi,
Pi <= K_w s_1 (X2 3.2(a)), so r >> s_1); theta_0 = bank mass of the preparation (P2) with theta_0 >= 4 Design K_DC r (K2 4.3 Step 6).

## 5.1 Proposition NE (near-exactness suffices for the class data).  SKETCH (audit of J1.13's list; no line-by-line re-proof).
Claim.  In J1.13 the requirement "pinned ratios realized EXACTLY on Z_kappa" may be replaced by: the realized ratios r^# lie within
delta_Z of a point r^flat of Z_kappa at which every robust minor is >= u/4, provided
      C_f Design(L)^C delta_Z <= delta s_1/(64 rho).                                                          (NE)
Argument.  Project the class data at r^flat (Lemma H at r^flat: same Hoffman bound; the data's distance to the cone at r^flat is O(K t) +
O(Design^C (eta' + delta_Z)) as before).  At f^# the true shift is Delta''_m = sum r^#_l gamma_l (X3), the cone shift sum r^flat_l gamma_l; they differ
by <= C_f D delta_Z (|gamma_l| <= C_f D lambda_l, K1.3).  This mismatch enters (i) the peak traces -Delta'' lambda_c vs_c u_c on E_c and T(L)
(U1 Lemma 4.6(b)), (ii) the tau_m-terms of the (X1) contact rows (Lemma EC), (iii) the inactive switching Delta'' w(l) of shifted blocks (J1-ref B.5),
(iv) the (X4^0) floor rows.  (i)-(ii) are contact/support violations of total mass <= C_f Design delta_Z, tolerated by (VT') [free coordinates:
split 1/2-1/2 so that b^theta = 0, as in K1.S]; (iii)-(iv) move kinds and floor rows by C Design delta_Z << gap^#/t (gap^# >= eta'/(3 Design),
H1 Prop. J1.11) and << the curvature slack.  The other uses of ratios (statuses by Lemma K, Sys-DC targets, Lemma PM, homogeneity of
(U)-block minors) use the realized ratios and need no exactness.  What is NOT checked line by line: every place downstream where
"the data lie in Gamma^#(kappa, a) at the realized point" is used with zero tolerance (U1 Lemma 4.6(c) for INACTIVE shifts: a (U)-block acquires
a true shift of size <= C_f D delta_Z; its peaks acquire tiny data -- handled as violations above).

## 5.2 The preparation bias.  PROVED.
LEMMA 5.2.  At an (R1) stage, the preparation (P2)/(P3) raises the value of every kind-(iv) carrier l: val_l(R_1) - val_l(f^r) >=
eff_s v_l(s) theta_0 - C D b theta_0 > 0 for each banked near contact s of l; and theta_0 >= 4 Design K_DC r >> Design^C s_1.  Consequently
(NE) can never absorb the bias: for a tiny minor M that is a nonnegative form in the oriented kind-(iv) ratios of a block (Prop. 4.1),
M(r_1) >= M(r(f^r)) + c theta_0/Design^C with c > 0 whenever the form charges a banked kind-(iv) row, and c theta_0/Design^C >> delta_Z
for every delta_Z allowed by (NE).
Proof.  K2.4(ii): the bank changes u_l(xhat) by (mu_s^2/nu) u_l(s) z_s dm with z_s = eps_l, u_l(s) = v_l(s) > 0 (s private to l; K2 4.1(c));
eff_s = mu_s^2/nu >= 1/Design; common-mode terms of (P3) raises at thin coordinates are <= C D b theta_0.  theta_0 >= 4 Design K_DC r: K2 4.3
Step 6 (S_th masses must stay >= theta_0/4 while the Sys-DC levers move by <= Design K_DC r).  r >> s_1: X2 3.2 (r >= 4 K_J Pi_X, Pi_X ~ s_1
A_0/T up to f-constants).  QED
So the two sources of a one-signed resonance at the start row are: (a) f itself lies on the wrong side (M(r(f)) > 0), and (b) the
preparation's upward bias when f lies on the right side by less than c theta_0/Design^C.  (b) is an artefact of K2's preparation:
kind-(iv) carriers receive a bank only because Sys-DC (Theorem K2.6) wants a two-sided lever at scale r for every Omega carrier.

## 5.3 A bias-free preparation for kind-(iv) carriers (SKETCH).
If a kind-(iv) carrier l has, at the Sys-DC scale, a pullable set J_r(l) ⊂ S_l with total pull capacity >= 4 K_DC r (coordinates with
v_l(j) in [c r, c_0 W]: BELOW the Step-A pull window, where (U') says nothing), replace its (P2) bank by a pre-placed TU pair at scale r
(pull of capacity ~4 K_DC r + compensating bank): net change of val_l is ZERO at first order (V1 Lemma TU, K1 2.1(b)), the lever is
two-sided at scale r (K2 4.3 (i) is satisfied by the TU column), and Step A sees no bias.  Combined with 5.1 this would remove the
bias source (b): a pinned one-signed resonance would then obstruct only when f itself is on the wrong side by more than delta_Z.
Remaining honest residual under 5.1 + 5.3: kind-(iv) carriers whose signature sets are anti-sign at EVERY depth from W down to r
("fully swallowed"), or rows with a wrong-sided resonance of f.  Not proved: (NE) in full; the Sys-DC re-check with TU columns at
scale r for (U')-carriers (P-TU-type range conditions at scale r).

## 5.4 Under (NE): which blocks still obstruct.  SKETCH (conditional on 5.1).
Under (NE) with b(w) so small that C_L((1 + Lip C_*) b)^{2/N_L} <= delta_Z (a design clause on b(w); b only appears as an upper threshold),
the start row is near-exact, and the Lojasiewicz displacement of pinned ratios is unnecessary.  Then:
 (a) (U)-blocks: realize s r_1 on all rows (s = 1 - C Lip eta'): values of kind-(iv) rows UNCHANGED, kappa^# := kappa/s via the two-sided
     peak resource (Fact 1.1(d)), statuses scaled down (Lemma K), near-exactness kept (homogeneity).  No obstruction (up to the bias (b)).
 (b) shifted blocks without active near-threshold carriers and (KN)-blocks: no status displacement of kind-(iv) rows is needed (robust
     statuses; the KN lever lowers statuses through R^2 of an inactive two-sided carrier).  No obstruction (up to the bias).
 (c) (T)-blocks with active near-threshold carriers: the Puiseux descent (H1 Lemmas 1.1-1.2) must move along Z_kappa; it is blocked iff
     every descent direction at the contact point decreases the value of some K^+ kind-(iv) row (or of a K^- row's |ratio| upward...).
     Simplest instance: a single active near-threshold K^+ kind-(iv) carrier d in a (T)-block (then Delta'_m = rt_d |gamma_d| > 0, the peak
     lever LOWERS kappa, and rho_d = m|r_d| K(sigma_rob, m^2 r_d^2)/Phi_d cannot decrease).  This "inward-locked near-threshold carrier" is the
     irreducible core of (R1) under (NE): its inward direction is downward for its value, it has no private downward resource
     (Lemma 2.5), and no block lever helps.  By Lemma 2.6 the same carrier cannot play this role at two consecutive (R1) stages.
