# J1 part 3: the one-out-of-many principle; band relaxation of inactive rows; what can and cannot be relaxed

Notation of parts 1-2.  ||b|| := ||Ft(R_1)||_2 (right-hand side of Step A), beta_* below in value units (the units of Ft).

## 3.1 Lemma J1.8 (band version of K2.9).  PROVED.
Split the rows of Sys-A into EQUALITY rows E and BAND rows B with half-widths beta_l > 0 (l in B): the relaxed Step A asks for a row R'
with Ft_l(R') = 0 (l in E) and |Ft_l(R')| <= beta_l (l in B).  Put Box := sum_{l in B} [-beta_l/2, beta_l/2] e_l.
 (a) If B(b, rho_0) ⊂ (W/2) conv(G ∪ {0}) + Box, the relaxed Step A is realized as in K2.9(c) (frozen statuses K-8 / J2's (FC)), with moves
     <= W and the same cost bound.
 (b) If (a) fails, there is a unit y with max_{g in G}(-y^T g) < 2(rho_0 + ||b||)/W (<= 4 Design^{-C_A}) and
      phi_y := y^T Ft(R_1) > (1/2) sum_{l in B} |y_l| beta_l - rho_0.
Proof.  (a) K2.9(c)'s Brouwer argument with the unknowns (t, sigma), t >= 0, sigma in Box, the map (t, sigma) -> the minimal-norm solution
(t', sigma') of G t' - sigma' = b - Rem(t) (a strictly convex parametric QP whose feasible set depends Hausdorff-Lipschitz on the right side,
Hoffman), defined on {||t|| <= W} x Box; a fixed point gives Ft(R_1) + G t + Rem(t) = sigma with sigma in Box.  (b) Pick b'' in B(b, rho_0)
outside the compact convex set (W/2)Q + Box and separate: a unit y with y^T b'' < min over (W/2)Q + Box of y^T(.) = (W/2) min(0, min_g y^T g) -
(1/2) sum_B |y_l| beta_l.  As in K2.9(b): (W/2) max(0, max_g(-y^T g)) < -y^T b'' <= ||b|| + rho_0, and y^T b < rho_0 - (1/2) sum_B |y_l| beta_l, i.e.
phi_y = -y^T b > (1/2) sum_B |y_l| beta_l - rho_0.  QED

## 3.2 Theorem J1.9 (one-out-of-many).  PROVED (modulo the cited chain).
Let k be a thick-type coarse carrier that is a strict non-peak of R_1 (so k in Lambda_A has a row).  If the row of k is relaxed to a band of
half-width
      beta_k >= beta_* := 16 nu_1 (||b|| + 2 rho_0)/(c_* u)
(and all other rows are kept), the relaxed Step A is realized (Lemma J1.8(a)).
Proof.  Otherwise Lemma J1.8(b) gives a near-certificate y of size < 4 Design^{-C_A} <= eps_* with phi_y > |y_k| beta_k/2 - rho_0.  By J1.6(a),
|coef^y_k| >= c_* u/(4 nu_1); and y_k = eps_k (coef^y_k + zeta_m lambda_k d kappa_m/d zeta(k)) with |zeta_m| <= C/A_min and d kappa_m/d zeta(k) =
rho_k M X_m/C <= C b^2 D^2 (U1 Lemma 1.4(c); route V: every coarse strict non-peak is in Omega), so |y_k| >= c_* u/(8 nu_1).  Hence phi_y >
c_* u beta_k/(16 nu_1) - rho_0 >= ||b|| + rho_0.  But |phi_y| = |y^T Ft(R_1)| <= ||b||.  Contradiction.  QED
Remarks.  (1) Since EVERY near-certificate has a robust, fixed-sign coefficient on EVERY thick-type carrier (J1.6(a)), relieving ONE thick-type
carrier -- by a band (J1.9), a helpful far placement (J1.7), a private two-sided resource (K2.17(a),(c),(e)) -- removes ALL obstructions.  The
residual must therefore be "rigid at every thick-type carrier simultaneously".  (2) beta_* is of the size of the needed corrections times
nu_1/(c_* u): for Step A, ||b|| <= C |Lambda_A|^{1/2} max(kappa eta', b) (Lojasiewicz/Puiseux displacement <= eta', KN-1 values <= C b, D-pushes
<= eta'), so beta_* <= C_f Design(L)^C eta'/u.

## 3.3 Proposition J1.10 (legitimate bands).  PROVED for (a)-(c); (d) is a precise negative statement.
Which rows of Sys-A may be relaxed to bands, and how wide?  The exact targets of the inactive rows (holds, KN-1 zeros, D-pushes) are used
downstream ONLY through statuses: Lemma K (rho_d = m|r_d| K(sigma, R^2)/Phi_d, R^2 = m^2 sum_{Omega} r_l^2), the (U)-block rescaling margin eta',
the (KN)-lever margin, the Puiseux margin mu = mu_kappa(eta'/3) of the active near-threshold carriers of (T)-blocks, and the robust margins
(K1 2.4 bracket; cert0 3.2; X1-ref 8).  Neither the class cone Gamma^#(kappa, a) (its ratio-dependent rows (X3), (X4^0) involve ACTIVE ratios
only), nor Sys-DC (whose targets are the values of the companion, K2 4.1), nor Theorem UE^inf / E^{eng,RT,inf} use the values of inactive
Omega carriers.  Hence a band of half-width beta on an inactive row l of block m is legitimate if
 (B1) l keeps its status class: |Delta rho_l| <= C_K beta/(kappa_m Phi_l) <= (margin of l)/4;
 (B2) the induced change of R^2 of block m, |Delta R^2| <= m^2 (2 |r_l| beta/kappa_m + (beta/kappa_m)^2), moves the protected statuses of block m by
      less than a quarter of their margin: (T)-block: C D^C |Delta R^2| <= mu/4; (U)-block: C D^C |Delta R^2| <= eta'/4 (the rescaling 1 - s_m =
      C Lip eta' of X1 2.1(U), cert0 3.4 D1, can absorb it after enlarging C); (KN)-block: within U1-ref Prop. KN(b)'s margin (enlarge C').
Consequences:
 (a) NEARLY NEUTRAL inactive rows (|r_l| <= C b) of (U)- and (KN)-blocks admit bands of half-width beta_* (B2: m^2(2Cb beta_* + beta_*^2)/kappa^2
     <= C Design^C (b eta'/u + eta'^2/u^2) << eta', since b <= mu/8 << eta' by (D2) and eta' << u^2).  [PROVED]
 (b) ROBUST-status inactive rows of blocks without protected statuses (no active carrier at all, i.e. inactive blocks; or blocks whose
     actives all have robust statuses) admit bands of half-width min(beta_*, c u kappa Phi) -- i.e. beta_* (beta_* << u).  [PROVED]
 (c) Hence (Theorem J1.9): if some THICK-TYPE carrier is (a) or (b), the relaxed Step A is realized.  [PROVED]
 (d) NOT legitimate in general (precise reasons): (i) KN-1 rows of (T)-blocks: B2 needs (beta_*/kappa)^2 m^2 C D^C <= mu/4, i.e. mu >> Design^C
     eta'^2/u^2, which fails when the Puiseux exponent beta_kappa of Lemma QC exceeds 2 (not excluded: cert0 3.2 records mu << (Design eta')^4 as
     possible); (ii) robust holds of (U)-blocks with active carriers: B2 needs 2 m^2 |r_l| beta_* << eta' while beta_* ~ Design^C eta'/u -- off by the
     factor Design^C/u, and enlarging the rescaling enlarges ||b|| and beta_* proportionally (circular); (iii) active rows: their ratios enter (X3)
     and Z_kappa (part 4).
Proof of (a)-(c): (B1), (B2) by Lemma K's Lipschitz bounds (X1 1.1: dk/dR^2 = k^2/(2(a - kR^2)), bounded by C D^C on the compact region of X1
2.3) and the listed margins; then Theorem J1.9.  (d) is the computation in the statement.  QED

## 3.4 Summary of what parts 2-3 remove (PROVED).
At a stage (L, w, a) Step A is realized (A-regular or band-A-regular) if SOME thick-type coarse carrier k
 - has a helpful far coordinate in FW_k (J1.7), or
 - is an inactive nearly-neutral strict non-peak of a (U)- or (KN)-block (J1.10(a)), or
 - is an inactive robust strict non-peak of a block without protected statuses (J1.10(b)), or
 - has a private two-sided design-depth resource (FR/ZD/TU; K2.17(c)) or two thick private coordinates of robust spread (K2.17(e)) or a thick
   and a same-orientation S_th private coordinate (K2.17(d)).
So the residual requires EVERY thick-type carrier to be rigid in all these senses at once.  Rows without thick-type carriers (all thick
design-depth support of a on coarse TARGET coordinates T(L)) are not touched by parts 2-3; there the certificates are of pure (U*) type
on the kind-(iv) carriers plus target-coordinate combinations (part 5).
