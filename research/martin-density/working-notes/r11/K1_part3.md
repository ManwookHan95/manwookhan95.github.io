# K1 part 3 (Round 11): Step B at infinite F (it is dispensable), status stability (V1 Lemma ST) under the new side effects

Setting of parts 1-2.  f^(1a) := the row produced by Step A (Lemma K1.6(A)) at the deep-raised row f^r.  E_c(w) := T(L) ∪ union_{l <= L}
(S_l ∩ [1, s_far(w)]) minus F^(1a) (U1 2.1), s_far(w) the least s with 2^{-s} <= c_{L+1}^2; J_fine := N \ (F^(1a) ∪ E_c(w)).

## 3.1 Lemma K1.S (route V needs no Step B).  PROVED.
Put f^# := f^(1a) (no G1 release, no static-ownership recursion: z is not changed on J_fine).  For t in S let the data be those of part 1.5 on
F and of Q1 CM^tr(c) on E_c, and on J_fine put b^+(j) := chi_j V(j), b^-(j) := -(1 - chi_j) V(j) with chi_j := 1/2 at free coordinates of f^#
and chi_j in [0,1] given by lem:split at contacts (as in V1 TR Step 4).  Then:
 (a) ||V 1_{J_fine}||_1 <= C_f D(L) 2^{-s_far(w)} + C_Delta sum_{k > L} lambda_k <= C_f Design(L) c_{L+1};
 (b) the violation mass on J_fine is <= ||V 1_{J_fine}||_1, and b^theta = 0 at every violated free coordinate ((H3) of U3 Lemma VT);
 (c) (U5') every COARSE carrier of every block of f^# is a peak with relative margin >= u/2 or a strict non-peak with gap^# >= g_min(w);
 (d) Theorem UE^inf (Q2 2.4, with the precisions of Q2-refa B.2 and P3 of Q1-refa) holds with its hypothesis (U5) replaced by (U5').
Consequently Q1's Step B, and with it the question of the ownership recursion on J_fine \ F, can be omitted at finite AND at infinite F.
Proof.  (a) A coordinate j of J_fine lies in no coarse target (T(L) ⊂ E_c ∪ F^#) and in no near part S_l ∩ [1, s_far] of a coarse signature
set, so coarse carriers contribute to V(j) only through S_l ∩ (s_far, infinity): sum_{l <= L} |c_l| ||v_l 1_{(s_far, inf)}||_1 <= C_f D(L)
sum_l lambda_l (delta_l/n_l) 2^{1 - s_far} <= C_f D(L) c_{L+1}^2 (|c_l| <= C_f D(L) lambda_l, part 1.4).  Fine carriers have forced coefficients
|c_k| <= C_Delta lambda_k (U1 Lemma 1.1(a), Lemma 2.1) and ||u_k||_1 <= q*(u_k) = 1: total <= C_Delta sum_{k > L} lambda_k <= C c_{L+1}.
(b) At a free j: |b^+| + |b^-| = |V(j)|, b^theta = (b^+ + b^-)/2 = 0.  At a contact j: (z_j b^+)_- + (z_j b^-)_+ = chi (z_j V)_- + (1 - chi)(z_j V)_-
= (z_j V(j))_- <= |V(j)|.  Off F^# ∪ J_fine (i.e. on E_c) the data and their violations are Q1's (CM^tr(d)).
(c) Lemma K1.6(A) (KN^tr's (b) at f^(1a)): every coarse carrier is a peak of relative margin >= u/2 or a strict non-peak with gap >= c_f eta' M
((KN)-, (U)-blocks), >= M mu_kappa(eta'/3)/2 ((T)-blocks, active near-threshold), = M (held at 0) or robust; all >= g_min(w) (Q1 CM^tr(b)).
Without Step B there is no later drift.
(d) (U5) enters Theorem UE (X2 3.5, Q2 2.4 (M5)) only through Lemma UE-1(e): the scrambled set A_m of lem:anchor for (w^0_m, w'_m), split as in
the proof of lem:scrambling into A^(1) := {k in A_m : t_k <= Pi} and A^(2).  By (c) and Lemma UE-1(b), (c) (values and thresholds move by <=
K_w Pi), a coarse carrier with t_k <= Pi is in S_1 or S_2 of lem:anchor as soon as 2 K_* Pi <= x_0(w) := c_f g_min(w) Phi_min(L) (margins
u theta Phi/(2m) >= x_0, Phi gap >= Phi_min g_min >= x_0, gap >= g_min >= x_0); so A^(1) contains fine carriers only, whose total contribution
to S_m is <= sum_{k > L} (Phi_k^2 + lambda_k(|w' - w^0| + (C' - C)_+)) <= 4m sum_{k > L} Phi_k <= 4m C c_{L+1}; A^(2) is handled by X2 3.2(iv)
verbatim (Phi-mass <= s_1^2 T^4).  Hence
      S_m <= K_w Pi^2 log(e/Pi) + 4m (C c_{L+1} + s_1^2 T^4),
and the requirement of X2's Step 3, Bx_m + S_m <= c_late delta s_1, holds because (W_exp) and Lemma S2c^tr give c_{L+1} <= exp(-1/T) and
s_1 >= exp(-1/(2T)), so 4m C c_{L+1} <= c_late delta s_1/4 for T small; the other terms are X2's.  The violations of (a), (b) are of the
type already counted in eps^viol (Q1 CM^tr(d): eps^viol <= C_f Design c_{L+1} + C_f c_{L+1}^2/T), so (VT') and (LATE) are unchanged.  QED
Remarks.  (1) What Step B was for.  In route X (exact data, U1) every coordinate must be EXACTLY admissible; the static-ownership recursion,
self-alignment of negative fine carriers and the G1 release were needed there, and X2/Q1 inherited them.  In route V every fine-origin
misfit is a tolerated violation of mass O(Design c_{L+1}), and (W_exp) makes c_{L+1} negligible against s_1 -- including in the scrambling
term, which is the only place where the self-aligned (R)-peaks of X2 Lemma CM(a) were used.  (2) At infinite F, Step B would have needed
the signature sets S_k of fine carriers to avoid F (S_k ∩ F is not assignable and |u_k(zhat^#)| >= ||v_k 1_{S_k \ F}||_1 may be small); Lemma K1.S
removes this question.  (3) The theorem does NOT say that fine carriers are harmless in general: only their total weight c_{L+1} is used,
against s_1 >= exp(-1/(2T)); this is where (W_exp) is essential.

## 3.2 Lemma K1.ST (statuses at f^# and along the engineered approximant; new side effects).  PROVED.
At f^# = f^(1a) and at the d-consistent engineered approximant f' of Theorem UE^inf built at f^#:
 (a) every coarse strict non-peak of f^r has its RATIO exactly at its Sys-A target (Lemma K1.6(A)); every coarse peak keeps its sign and a
     relative margin >= u/2; every near-threshold active carrier d of a (T)-block has rho^#_d <= 1 - mu_kappa(eta'/3)/2 and rho'_d <= 1 -
     mu_kappa(eta'/3)/8; robust objects of level L move by <= Design^C eta'/u + C mu*_J + Design^C r/u << u between f and f';
 (b) the new side effects -- deep raise (part 1.2), lowering of far in-F coordinates (part 2.3), common modes of (P4)/(P5) and of the
     repaired block-norm levers (P6) -- change no status used by route V.
Proof.  (a) Lemma K1.6(A): Sys-A fixes all coarse non-peak ratios exactly, so by X1 Lemma K (rho_d = m|r_d| K(sigma, R^2)/Phi_d; R^2 a function
of the Omega ratios; sigma = sigma_rob + O(c_{L+1}^2) because the coarse peak set is P_rob: robust peaks move by << u, weak peaks were pushed in
Step 0) the (T)-block statuses are those of X1-ref 8 with the SAME Puiseux margin; the (U)- and (KN)-block statuses depend on the exact ratios
and on robust peaks only; robust objects move by the resource sizes (Lemma K1.6(A): <= Design^C eta'/u in value units) times design Lipschitz
constants.  At f': Lemma PM (Q1 2.4) verbatim -- its proof uses (i) nv' = nv^# on Omega (Lemma DC^inf under (LR), K1.6(B)), (ii) coarse
peaks clamped at both rows (margins >= u/2 >> the value moves K_lev r + common modes Design^C r), (iii) fine terms bounded by C sum_fine Phi^2.
None of these uses the privacy of the levers: the common modes of (P4)/(P5) move only coarse peaks and fine carriers once all Omega
normalized values are exact.  (b) Deep raise: values move by <= C mu*_J <= b^2 Phi_min/Design (part 1.2 choice of J), inside the clean
classification (U2 Lemma DR-inf).  Lowering a far coordinate j in F does not change z (a lowered support coordinate becomes a contact of the
same sign s_j) and moves e by <= 2 mu*_j x_max/nu (V1 Lemma B(iii)), hence every value by <= C mu*_j x_max << b; the subsequent pull/z-move is
the resource's own move.  Common modes: by (a), every coarse non-peak value is re-tuned exactly inside the same fixed point (Sys-A) or
Poincare-Miranda solution (Sys-DC), so only peaks (robust) and fine carriers (total weight c_{L+1}) feel them.  QED
Remark (V1 Lemma ST and Lemma NS).  V1's status table concerned the donor raise (C3) and the drift Lam = T^3; route V does not use (C3)
(part 2.3), and the closing moves (C1), (C2) act off F exactly as at finite F.  So V1 Lemma ST is replaced by (a) above; V1 Lemma NS
(no slaving) holds because every exactified object is a function of the exact ratios (Sys-A) and of the closed rooms ((C1), (C2), off F).
