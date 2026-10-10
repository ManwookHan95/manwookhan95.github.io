# X2 part 5 — (C_mix): mixed activity classes are recovered (given (KN) for the class, as in Master Theorem IV')

Setting: U1 part 4/5 with U1-ref's fixes (design D^{U1'}, Proposition KN, release G1), plus (D-lev) (Lemma LV) and (W_exp) (4.2).  N >= 2,
F finite, w a clean sub-window of a main stage L >= l_f, a (class, cube) set S of scales of ONE activity class a, MIXED: A_- := {m active,
sigma_m = -1} and A_+ := {m active, sigma_m = +1} both nonempty (data convention: sigma_m = sgn Delta''_m).  The class satisfies (KN_{w,a}).

## 5.1 Lemma CM (the self-aligned completion of a mixed class).  PROVED.
Let f^(1c) be the row after U1's steps (1a) [Proposition KN of U1-ref], (1b), (1c), and J_fine as in U1 4.1 with the G1 release (U1-ref
Section 5).  Define z on J_fine by the forward recursion of U1 Lemma 4.1 with STATIC ownership: own(j) := the first OWNER-CANDIDATE (in stage
order) whose vector meets j, where the owner-candidates are U1's types (a)-(c) (Omega_act, coarse peaks of active blocks, tuned absorbers) and
(d) EVERY fine carrier of an active block (its coefficient in V is -Delta''_m lambda_k w(k), Lemma 1.1(a) of U1; it may vanish, which is
harmless below); fine carriers of inactive blocks have coefficient 0 and are not candidates.  The rule at a fine candidate k, processed in
stage order with O(k) := {j in J_fine : own(j) = k} and Y_k := the part of u_k(zhat) fixed by coordinates outside O(k) (all fixed earlier):
   negative block (m(k) in A_-): varsigma_k := sgn Y_k (+1 if Y_k = 0), z_j := varsigma_k sgn u_k(j) on O(k)      [SELF-ALIGNED];
   positive block (m(k) in A_+): varsigma_k := sgn Y_k, z_j := -varsigma_k sgn u_k(j) on O(k)                     [anti-aligned, U1 Lemma 5.4];
coarse owners (types (a)-(c) of U1 Lemma 4.1) set z_j := sgn(coefficient x u_own(j)(j)) on their owned sets; coordinates without owner meet no
carrier with nonzero coefficient (V(j) = 0) and get z_j := 0.  Let f^# be the resulting row.  Then for EVERY scale t in S:
 (a) every fine carrier of a negative block is a self-aligned peak with |u_k(zhat^#)| = |Y_k| + own_k >= delta°_k and margin
     mu_k >= q^#_0 delta°_k/2 (state (R) of U1 Lemma 5.2); hence the negative blocks A_- satisfy the explicit scrambling bound
     Scr^#_m(x) <= C (x/q^#_0)^2 for 0 < x <= x_0(f^#) (U1 Lemma 4.3's proof, whose only input on fine carriers is (R)), with x_0(f^#) >= c_f gap_min
     Phi_min(L) (coarse statuses from Proposition KN(b), tuned absorbers gap 3M/4);
 (b) V(Domega(t)) is z^#-admissible at every coordinate off F^# EXCEPT on the owned sets of positive fine carriers; there are no violations at
     free coordinates ((H3) of Lemma VT is vacuous); the total violation mass satisfies
         eps^{viol}(t) <= sum_{k fine, active} |coef_k| ||u_k||_1 + sum_{j owned by positive k} sum_{k' later} |coef_{k'}| |u_{k'}(j)| <= 2 C_Delta sum_{l > L} lambda_l
                       <= 4 C_Delta c_{L+1};
 (c) everything else of U1's companion is unchanged: exactness on E_c (U1 Proposition 3.4: the biased pairs cancel any residue, continuous in z),
     the coarse owned sets (U1 Lemma 4.2, whose estimates do not use the signs of the shifts), statuses of coarse carriers and absorbers (U1-ref
     Proposition KN(b), U1 Lemma 3.3), cost p*(f^# - f) <= theta_w T_lo(w)^2 (U1 Lemma 4.5), true shifts (U1 Lemma 4.6 (a)-(c)).
Proof.  (a) For a negative fine carrier k the coefficient -Delta''_m lambda_k w(k) has sign varsigma_k... precisely: by the recursion
u_k(zhat^#) = Y_k + varsigma_k sum_{O(k)} |u_k(j)| (zhat^# = z on J_fine, diagonal base), so |u_k(zhat^#)| = |Y_k| + own_k with own_k >= ||u_k 1_{S_k}||_1
= delta°_k (S_k ⊂ O(k): no earlier carrier meets S_k, allowedness (a); S_k ⊂ J_fine); the peak criterion and the margin bound are those of U1
Lemma 4.1 ((W3): theta Phi_k/m << delta°_k).  Scrambling: U1 Lemma 4.3 verbatim (coarse carriers and tuned absorbers do not contribute below
x_0; every other carrier of block m is (R)); the super-exponential decay of delta_k H_k gives sum_{k: delta_k H_k <= X} (delta_k H_k)^2 <= 2X^2.
(b) Coordinates owned by a coarse owner or by a negative fine carrier: U1 Lemma 4.2 (dominance |coef_own| |u_own(j)| >= 2 sum_{later} |coef| |u(j)|;
for a negative owner |coef_k| = |Delta''_m| lambda_k M because k is a peak), so sgn V(j) = sgn(coef_own u_own(j)) = z_j: for negative owners
coef_k = -Delta''_m lambda_k varsigma_k M with Delta''_m < 0, so sgn V(j) = varsigma_k sgn u_k(j) = z_j.  Released coordinates (G1) carry no coarse
contribution (inactive Omega carriers have gamma = 0, coarse peaks of inactive blocks have Delta''_m = 0).  Unowned coordinates: V(j) = 0.
Remaining coordinates are owned by positive fine carriers; there |V(j)| <= |coef_k u_k(j)| + sum_{later} |coef_{k'} u_{k'}(j)| and the violation at j
is at most |V(j)| (viol(j) = (z b^+)_- + (z b^-)_+ <= |b^+(j)| + |b^-(j)| = |V(j)| for the split b^+ = chi V, b^- = (chi - 1)V of U1 Prop. 2.2(e));
coefficients of fine carriers are <= C_Delta lambda (U1 Lemma 2.1; absorbers' coefficients <= C_f lambda, U1 Prop. 3.4) and ||u||_1 <= 1.
All these coordinates are contacts of f^# (z = +-1).  (c) The recursion only fixes z on J_fine; the cited statements use J_fine only through
"z is fixed on J_fine after (1c)" and dominance.  QED

## 5.2 Theorem C_mix (mixed classes are recovered).  PROVED (modulo the refereed tools of U1/U1-ref and parts 2-4 here).
Design D^{U1'} + (D-lev) + (W_exp), N fixed, F finite.  Suppose that for infinitely many main stages L some clean sub-window w of L has a
(class, cube) set S of at least n(w)/D_cls(w)^2 scales of ONE activity class a (one-signed OR mixed) satisfying (KN_{w,a}).  Then f in Rec(p_N).
Proof.  For each such (L, w): companion f^# of Lemma CM (for one-signed classes the same recursion: in configuration (i) it is U1's
recursion, in configuration (ii) it is the anti-aligned rule of Lemma 5.4 with violations only at frustrated carriers — no Schauder completion is
needed).  For every t in S the data of U1 Proposition 2.2(e) at f^# form a window family (U1)-(U7) with: (U1), (U2) from Proposition 2.2(e) and
V1 TR(iii) (kappa_w <= 1 + eta_0/2, kinds [1]-[3], A_2 = 22, A_0 an f-constant), the fine part of the data entering Gamma only through
||V_fine||_1 <= C_f c_{L+1} (contributing <= C_f c_{L+1}^2 / nu); (U3) from V1 TR(iv) and U1 Proposition 3.4(d); (U4) from Lemma CM(b) (contact
violations only, eps^{viol} <= 4 C_Delta c_{L+1}); (U5) from Lemma CM(a); (U6) from Lemma LV with (D-lev); (U7) from U1 Lemma 2.1.  (E-c) p*(g - g_t) <=
K t, K = C_f (Design/u)^C (Proposition 2.2(e)); (E-d), (E-e) as in Master Theorem IV' (U1-ref Section 8: |S| >= l 2^{l^3}(Design/u)^C >> K/c_flat,
K T_hi(w)/|S| -> 0, p*(f^# - f) <= theta_w T_lo(w)^2); the subset version of the averaging is U1 Lemma 2.4's argument applied to the proof of
Theorem E^eng (only "sum_{I_r} t_i < 2|r|/c_flat over dyadic scales" and the count |S| are used).  (E-f) is 4.2 ((W_exp)).  Theorem E^eng gives
(f, rho g) in cl NA for every rho < 1.  QED
Consequences.  (1) U1's Corollary IV.2 (shape of a counterexample) is VOID: frustration of positive carriers is harmless.  (2) The open
item (C_mix) of ADDENDUM 8 is closed (for D^{U1'} + (D-lev) + (W_exp)); the toy phenomena of U1 5.5 (forced wrong branches (W), bad carriers in
threshold bands) do not arise because the completion is never required to be exact on fine coordinates — fine-origin violations are tolerated
(Lemma VT inside Theorem UE) at the price s_1 >= 64 rho eps^{viol}/delta, which (W_exp) makes compatible with (LATE).  (3) Remaining hypothesis:
(KN_{w,a}), i.e. U1-ref's STATUS COHERENCE problem (an active block with an active near-threshold switching carrier and no inactive Omega carrier
of robust relative position) — this is the X1 task, untouched here.
