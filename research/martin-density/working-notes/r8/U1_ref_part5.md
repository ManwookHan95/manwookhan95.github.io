# U1 referee, part 5 — mixed classes, Master Theorem IV and corollaries, (C_mix), corrections

## 5.1 Lemma 5.1 (exactness in every class).  Verdict: correct ARGUMENT (Schauder on the common ray, signs not used); as a statement it
## inherits the gap of Theorem 2.3 (the Hoffman control of Proposition 2.2(b) and the statuses of the coarse carriers).  PROVED under
## (KN_{w,a}) with the G1 release.

## 5.2 Lemma 5.2 (three states of a negative fine carrier).  Verdict: CORRECT (PROVED).
Re-derived: if |w(l)| >= M/2 the coefficient |Delta''| lambda_l |w(l)| dominates on O(l) (Lemma 4.2 with M/2), admissibility forces
z_j = sgn w(l) sgn u_l(j) there (zhat = z on J_fine), v_l = Y_l + sgn(w(l)) own_l, and sgn v_l = sgn w(l) (same sign of zeta and w);
the two sign cases give (R) and (W) (the latter needs own_l > |Y_l|); otherwise |v_l| < thr_l/2 and gap > M/2 (clamp formula).

## 5.3 Lemma 5.3 ((SC) tolerating wrong branches).  Verdict: CORRECT (PROVED) with a constant precision.
Not bad => peaks have margin >= q_0 Phi^{1/2}, strict non-peaks gap >= Phi^{1/2}; contributions only from carriers with Phi_l <= X(s) :=
max((Upsilon s/q_0)^2, 2 Upsilon s/M, (Upsilon s)^{2/3}).  Precision: sum_{l >= L'} Phi_l <= (4/3) 2^{m + k(L')} Phi_{L'} (not 2 Phi_{L'}: Phi_l =
2^{-m(l)-k(l)} c_l), and all carriers l < L_i have Phi_l >= 2^{-N - L_i} Phi_{L_i - 1} > X(s_i); with Phi_{L'} <= Phi_{L'-1}^7 (true at main stages
of D^{U1'}: (W2) at L' with sub-window data at stage L'-1) the extra factor 2^{N + k(L')} is harmless.  The Remark "(R) carriers are never bad"
is correct: c_l <= b(l-1, M(l-1))^2 << (delta°_l)^8 at non-cluster stages, and at cluster stages c_{L+i} <= b(L, M(L))^2 with L + i << n(L).

## 5.4 Lemma 5.4 (mixed recursion without frustration).  Verdict: CORRECT (PROVED).
Non-frustrated positive carriers: v_l = varsigma(|Y_l| - own_l), |v_l| >= thr_l/2, coefficient sign -varsigma = sgn of the anti-aligned own
coordinates' requirement; negative carriers are (R).  Frustration (|Y| < own + thr/2) is correctly identified as the only failure of the
forward recursion.

## 5.5 Toy evidence (5.5).  HEURISTIC, correctly labelled.  (Re-run of mixed_fixedpoint_check.py / mixed_forcedW_check.py: see the referee
report, Section 4.)

## 5.6 MASTER THEOREM IV.  Verdict: NOT PROVED as stated (gap of Theorem 2.3 = status coherence; plus the fixable gaps G1, G2-(X4), the
## design defects (D1)-(D4) and the precisions of parts 2-4).  PROVED in the following corrected form.
MASTER THEOREM IV' (referee).  Design D^{U1'} (part 3), N fixed, diagonal mu-base, F finite.  Suppose that for infinitely many main stages L
some clean sub-window w of L has at least n(w)/D_cls(w) dyadic scales whose activity class a is one-signed (or has no active shift) AND
satisfies (KN_{w,a}): every active block containing an active near-threshold switching carrier contains an inactive coarse strict non-peak
with relative position >= u(w).  Then f is in Rec(p_N).
Proof: U1's proof with: classes read off the decomposition data and fixed before the companion; Theorem 2.3 replaced by the ratio-space
Lojasiewicz realization + kappa-neutral lever (part 2, 2.4); the (X4) rows of part 2 (p-b); the cofactor minors (p-c); the G1 release; the
design D^{U1'}; Lemma 4.2(ii) as repaired; Lemmas 4.1, 4.3, 4.4, 4.6, 5.x as checked.  Classes with no active shift need no kappa (the
(X3) rows read sum u gamma = 0) and are covered by V2 Theorem B.
Special cases of (KN_{w,a}) (vacuous): no active block contains an active near-threshold switching carrier (e.g. all active switching
carriers have robust relative position).  For U1's configuration (i) note that every (K4) carrier of an active negative block is FORCED to be
active ((X4): vs gamma >= lambda |Delta'| rho), so (KN) is a genuine restriction there.

## 5.7 Corollaries.
 IV.1 (N = 1, all finite-F rows in Rec(p_1)): NOT PROVED.  What is proved: f in Rec(p_1) if (KN) holds at the one-signed classes of a clean
      sub-window for infinitely many main stages (all classes are one-signed for N = 1).  The residual for N = 1 is the status-coherence
      configuration (part 2, 2.4).
 IV.2 (shape of a counterexample): as a contrapositive of IV it is not established; the correct contrapositive of IV': a finite-F
      counterexample must, at all large main stages and every clean sub-window, have all but a 1/D_cls fraction of the scales in classes
      that are mixed or violate (KN).
 IV.3: holds under (KN) (PROVED after fixes).
 IV.4 (intrinsic form): the reduction "I_up(w) = {} or I_lo(w) = {} => every class one-signed" is CORRECT (PROVED; re-derived from V1
      Lemma 3.4' halves and I_up ∩ I_lo = {}); the conclusion f in Rec needs (KN) in addition.

## 5.8 (C_mix) and its reduction to U3's (S2).  (C_mix) OPEN (as labelled).  The reduction is a plausible SKETCH: running the recursion with
frustrated positive carriers anti-aligned leaves sign violations on their own sets with l_1-mass <= C_f sum_{l > L} lambda_l own_l <= C_f c_{L+1},
all negative carriers (R).  But (i) it inherits the status-coherence gap; (ii) a violation of FIXED mass eps_j at the FIXED companion f_j can be
tolerated by Lemma VT only down to s_1 ~ 32 rho eps_j/delta, so recovery at f_j is only approximate and the uniformity along j is exactly U3's
(S2), whose sketched form has a first-order junction mismatch (U3-ref F6: K_sharp ~ t^{-2}); so "(C_mix) follows from (S2)" reduces one open
step to another open step of comparable difficulty.

## 5.9 Corrections recorded by U1 (5.8).
 * V2's near-coordinate conversion FALSE as stated: AGREE (signed sums of super-decreasing weights v(s), ratio <= 2^{-G}, G >= 4, form a
   Cantor set with gaps ~ the first weight; the discrepancy is of the order of the first converted weight).
 * "V2's two-scalar exactification is unnecessary (kappa-reduction)": DISAGREE.  Lemma 1.3 is correct (only kappa enters the exact system),
   but the second scalar returns through the statuses: by Lemma R-kt the relative positions of the switching carriers are functions of the
   ratios u/kappa, so threshold protection (theta) and exactness (kappa) still need two independent levers; with all coarse strict non-peaks in
   Omega and only peak pushes available, there is ONE lever.  This is V2-ref's (C*-3) in a sharper form, not a closure.
 * c_0(a) > 0 on unused absorbers: AGREE (needed; checked).
 * recursion_check.py vs recursion_check2.py: re-run, AGREE ((W4'') is needed for Lemma 4.2).
