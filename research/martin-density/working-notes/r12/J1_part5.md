# J1 part 5: target sets instead of target points; rescaling coupling in (U)-blocks; the refined residual

## 5.1 Lemma J1.13 (what Step A must realize exactly).  PROVED (inspection of the chain, as in 4.2 and 3.3).
Let Tgt := Z_kappa ∩ B(r_1, eta') ∩ {F_st <= 1 - 3mu/4} be the Lojasiewicz/Puiseux target SET (ratios of the ACTIVE Omega carriers), and call
an active ratio r_l FREE if no tiny minor and no tiny cofactor polynomial of Gamma^#(kappa, a) (written as in X1 2.2(iv)) depends on r_l.
Then the downstream construction (class data, Theorem UE^inf, E^{eng,RT,inf}) needs from Step A only:
 (i) the realized active ratio vector r^# lies in Z_kappa, every robust minor is >= u/4 at r^#, and r^# is within eta' + Design^C beta_*/kappa
     of r_1;
 (ii) the statuses: (T)-blocks rho_d(r^#) <= 1 - mu/2 for d in N_T, (U)-blocks rho <= 1 - eta'/2, (KN)-blocks U1-ref Prop. KN(b), robust
     statuses robust; KN-1 values with m^2 sum r^2 <= mu/(C D^C) in (T)-blocks;
 (iii) exact realization of NOTHING else: the class data are projected onto Gamma^#(kappa, a) evaluated at the REALIZED ratios r^# (Lemma H
     with the robust minors >= u/4 and the tiny ones exactly 0 gives the same Hoffman bound C_f^l Design^2/u as at r''), and the true shift
     at the companion is then the cone shift (X3 at r^#).
Proof.  The class data of a class are produced per scale by projecting the decomposition data (violations <= K t) onto the cone; nothing
forces this projection to be done before the realization: performing it at r^# uses only (i) (Lemma H, V2) and gives exact cone points at
the companion's own ratios, so U1 Lemma 4.6's correction term vanishes as with exact targets.  The remaining uses of the ratios are the
statuses (ii) (Lemma K, Lemma PM, X1 2.2(iii): the floor row needs rho - rho^0 <= C gap/t, weaker than (ii)) and the size of the moves
(costs, robust objects), covered by (i).  Inactive values enter only through (ii) (K1 2.4; cert0 3.2).  QED
Consequence.  In Step A every FREE active ratio and every inactive value may be realized within a band, provided (i)-(ii) hold for every
point of the band; only the PINNED active ratios (those occurring in a tiny minor/cofactor) must be realized on Z_kappa exactly.

## 5.2 Lemma J1.14 (rescaling coupling in unshifted blocks).  PROVED.
Let m be a (U)-block (Delta'_m = 0 in the class; this includes blocks with no active carrier) and suppose some inactive rows of block m and
some FREE active rows of block m are realized within bands of half-widths beta_l (value units).  Replace the (U)-block targets s r'^{(m)} of
X1 2.1(U) by s_m r'^{(m)} with s_m := the largest s <= 1 - C Lip eta' such that every active status of block m, computed with the realized
values, is <= 1 - eta'/2 (and the D2-pushed carriers' pushes enlarged likewise).  Then (a) Z_kappa is preserved (minors of a (U)-block are
homogeneous in r^{(m)}, cert0 3.4 D1); (b) s_m depends continuously on the realized values and 1 - s_m <= C(Lip eta' + D^C sum_l (|r_l| beta_l/kappa_m
+ beta_l^2/kappa_m^2)); (c) the coupled system (Step A with the bands and s_m as a function of the realized values) has a solution by
Brouwer whenever the band-A-regularity of Lemma J1.8 holds uniformly over the range of s_m.
Proof.  (a) cert0 3.4 D1 (homogeneity of the minors in r^{(m)}; vanishing preserved; robust minors scale by >= s^n >= 1/2).  (b) Lemma K: every
active status of block m equals m|r_d| K(sigma, R^2)/Phi_d; scaling r^{(m)} by s multiplies |r_d| by s and lowers K (K increasing in R^2), while
the bands change R^2 by <= m^2 sum (2|r_l| beta_l/kappa + beta_l^2/kappa^2); dK/dR^2 <= C D^C on the compact region (X1 1.1).  (c) the unknowns
(t, sigma) of J1.8(a) and the scalar s_m: the map (t, sigma, s) -> (minimal-norm solution for the right-hand side b(s) - Rem(t), s_m(realized
values)) is continuous on a compact convex set; J1.8(a) applied for each s in the range gives the selection.  QED
[For (KN)-blocks the same coupling with the KN-lever push of U1-ref Prop. KN (push amount as a continuous function of the realized values)
is expected to work: SKETCH (the lever's margin bookkeeping was not re-derived).]

## 5.3 Theorem J1.15 (Step A at rows with one relievable thick-type carrier).  PROVED modulo the cited chain (+ J2's (FC)).
Design T_fin^{K2}.  At a stage (L, w, a), Step A is realized (and Theorem K2.15 / J2's Theorem J2.1 apply at this stage) if there is no
near-certificate of size <= eps_*, or if SOME thick-type coarse carrier k satisfies one of:
 (J-a) a helpful coordinate in its far window FW_k (Theorem J1.7);
 (J-b) a private two-sided design-depth resource, two thick private coordinates of robust spread, or a thick and a same-orientation S_th
       private coordinate (K2.17(c)-(e));
 (J-c) k is a zero-data strict non-peak, of robust or tiny status (not D2-pushed), of a (U)-block or of a block with no active carrier, and
       the block has a private two-sided peak resource (Lemmas J1.13, J1.14, Theorem J1.9);
 (J-d) k is an ACTIVE strict non-peak of a (U)-block whose ratio is FREE, the block having a private two-sided peak resource (J1.13, J1.14,
       J1.9);
 (J-e) k is zero-data in a (T)-block (KN-1) and mu_kappa(eta'/3) >= C D^C (beta_*/kappa)^2 m^2 (always true if Proposition J1.11 holds);
 (J-f) k is active in a shifted block satisfying the mismatch-tolerance conditions (MT1)-(MT3) of J1.12 with delta_0 >= beta_*/kappa_m, or k is
       active with a FREE ratio in a shifted block in which no protected status is R^2-sensitive at the scale beta_* (J1.13 with (ii)).
Proof.  (J-a): J1.7.  (J-b): K2.17.  (J-c), (J-d): by J1.13 the row of k may be realized in a band of half-width beta_*, all other
requirements (i)-(ii) being restored by the rescaling coupling J1.14 (and, for (J-d), by projecting the class data at the realized ratios);
k's own status: robust or tiny margin >> beta_* m K/(kappa Phi_k) for (J-c); for (J-d) it is one of the active statuses restored by s_m.
NON-CIRCULARITY: the coupling changes the targets of block m by (s_m - 1) r'^{(m)}, which changes phi_y by kappa_m (s_m - 1) zeta_m(r'), and
|zeta_m| <= 2 eps Design for every near-certificate because block m has a private two-sided peak resource (y^T col_c = -(1 - X) lambda_c
zeta_m); since 1 - s_m <= C D^C beta_* m K/(kappa Phi_min) this is <= C Design^C eps beta_* << c_* u beta_*/(32 nu_1) (eps <= 4 Design^{-C_A}).
So the band must absorb only the coupling-independent part of phi_y.  Then Theorem J1.9 (every near-certificate has |y_k| >= c_* u/(8 nu_1)
by J1.6(a)) and J1.8(a), applied uniformly over the compact range of s_m (J1.14(c)).  (J-e): (B2) of J1.10 holds with the stated
inequality.  (J-f): J1.12 resp. J1.13.  QED
In particular (LSC-trunc)_N holds at (f, g, rho) whenever, at infinitely many main stages, Step A carries no near-certificate or one of
(J-a)-(J-f) holds for some thick-type carrier (J2's Theorem J2.1 removes (H1*)).

## 5.4 The remaining class after J1 (precise).  OPEN.
(f, g, rho) is not covered by Theorem J1.15 (with J2) only if, for all but finitely many main stages L, at every clean sub-window and every
admissible class, Step A carries a near-certificate y (structure: K2.16 and J1.3 -- kappa_y <= -c_*/nu_1, Psi_y = kappa_y (a + Theta_y) + E_y with
anti-signed one-sided "hole" mass sum_{S_1} |Theta_y| >= 1 - small; by J1.5 no companion keeping the one-sided coordinates' signs realizes the
targets) AND
 (R0) [all thick-type carriers rigid at once] every thick-type coarse carrier k has a frozen far window (z_j = tau_k(j) or super-thick on FW_k),
      no private two-sided design-depth resource, spreads <= Design^{2 - C_A} on its thick private coordinates, and is of one of the types
      (R-pin) active with a PINNED ratio (it occurs in a tiny minor/cofactor of the class cone), in any block;
      (R-T)   zero-data in a (T)-block (KN-1 carrier) with mu_kappa(eta'/3) < C D^C m^2 (beta_*/kappa)^2 [empty if Proposition J1.11 holds];
      (R-Ts)  active with a free ratio in a shifted block with an R^2-sensitive protected status, failing (MT1)-(MT3);
      (R-KN)  zero-data in a (KN)-block [covered if the KN-lever coupling of 5.2 is carried out];
      (R-D2)  zero-data, near threshold and D2-pushed in a (U)-block (its own margin is only ~eta'; a one-sided inward band helps only when
              the certificate's needed direction is inward);
      (R-np)  zero-data or free-active in a (U)-block that has NO private two-sided peak resource (the rescaling coupling may then be circular);
      (R-pk)  a peak (no row) whose block has no private two-sided peak resource;
 or
 (R1) there is NO thick-type carrier: all thick design-depth support of a lies on coarse TARGET coordinates T(L), and every near-certificate
      is of pure type (U*): its robust coefficients sit on active kind-(iv) carriers (data-carrying, all design-depth private coordinates S_th of
      the data sign, far window swallowed by anti-data-sign support), with the one-sided hole mass >= 1 - small on their S_th coordinates.
In the stable case (the thick-type carriers and their proportionality constants rho_k fixed for all large L) the near-relations become exact
identities at f: a = sum_{K_0} rho_k u_k on the thick part of F and every per-block frozen value Phi_0^{(m)}(zhat_f) vanishes, so Phi_0 :=
sum_{K_0} rho_k u_k is a FLAT, block-representable direction at f (4.5(d)): the residual is a resonance in which the base vector a itself is
block-representable as a mate direction.  Not shown: that such rows have a non-recoverable mate (no counterexample is suggested), nor that
(R0)/(R1) can hold at all large stages for some row.
