# X2-ref part 4 — Lemma CM, Theorem C_mix, the repair (R-abs), Master Theorem V, design D^{X2}

Refereed against: U1 parts 4-5 (Lemmas 4.1-4.6, 5.1-5.4), U1-ref (Proposition KN, Sections 5-8), X2 parts 3-6, my parts 1-3.

## 4.1 Lemma CM (self-aligned completion of a mixed class).  Verdict: the RULE and the violation analysis are CORRECT and are the key
## new idea; as stated (with tuned zero-value absorbers kept in the switching data) the lemma feeds an argument that fails (part 2);
## (a)'s x_0 claim is wrong for absorbers of a negative block 1 (part 2, (A5)).
What is right (re-derived).  With static ownership and the rule "negative fine carriers self-aligned, positive fine carriers anti-aligned",
the recursion is well founded (Y_k uses only coordinates fixed before k); a negative fine carrier is an (R) peak with
|u_k(zhat)| = |Y_k| + own_k >= delta°_k (own_k >= ||u_k 1_{S_k}||_1, S_k ⊂ O(k) by allowedness (a)) and margin >= q_0 delta°_k/2 ((W3));
its coefficient -Delta''_m lambda_k varsigma_k M has the sign varsigma_k, so with U1 Lemma 4.2's dominance (valid for any owner with
|coefficient| >= (A_2 K T_lo/2) lambda M, signs not used) V(j) has the sign z_j on O(k).  For a positive fine carrier the owned set is admissible
when the carrier is not frustrated (U1 Lemma 5.4) and is otherwise violated; in every case viol(j) <= |V(j)|, so the violation mass is
<= sum_{k fine} |coef_k| ||u_k||_1 <= 2 C_Delta sum_{l > L} lambda_l.  All violated coordinates are contacts (z = +-1 on owned sets).  The
scrambling bound for negative blocks follows from U1 Lemma 4.3's argument (the only input on fine carriers is (R) and c_k <= (delta_k H_k)^2).
The decisive observation — in the violation-tolerant regime NO EXACT COMPLETION is needed, so U1's forced wrong branches (W) and frustration
(U1 5.2-5.5) never arise — is correct and is the single most valuable idea of X2.

## 4.2 Theorem C_mix as written.  Verdict: GAP (not proved as written); TRUE after the repair (R-abs) below.
The proof feeds Lemma CM's companion into Theorem UE with Omega ⊃ tuned absorbers and Lemma LV(d) levers.  By part 2 (A1)-(A4), at the
radius forced by (VT') and by X2's own choice s_1 >= exp(-1/(2T)), the absorbers met by levers (and by window theta-masses on E_c
coordinates beyond the next main stage) cannot be kept at value 0 (the S-mass range is ~ m_0 mu_{p0}^2, astronomically small; the
increasing direction destroys the row), and without re-tuning they become peaks carrying nonzero switching coefficients, which costs
rho |tau| |Domega(a)| at FIRST order in the theta regime.  With X2's explicit choice s_1 >= exp(-1/(2T)) (4.2(iii)) the pull
coordinates of Lemma LV(a) lie in E_c (part 2, (p-LV2)), and their z flips alone break the tuned first pairs P(j_p) for every active
class-G carrier, whatever the violation mass.  A much smaller s_1 (below the rooms and S-mass ranges of the finitely many absorbers touched
by levers and masses — N_w is fixed before s_1) would avoid this, but (VT') forbids it as soon as eps exceeds those rooms, which is the
generic situation in mixed classes: a frustrated positive carrier at a stage L' > L violates with mass ~ C c_{L'} delta_{L'}, while the first
pairs of window coordinates s in (L', N_w] carrying theta-masses sit at stages > L' with weights << c_{L'}.  Also (U5) fails for absorbers
of a negative block 1 with X2's x_0 (part 2 (A5)).

## 4.3 The repair (R-abs).  Lemma CM' and Theorem C_mix'.  PROVED (modulo the refereed tools cited by X2; every step below is either a
## refereed statement or a one-line verification given here).
Lemma CM' (completion without absorber switching).  Design D^{X2} with (p-W); N >= 1; F finite; w a clean sub-window of a main stage L >= l_f;
a class a (one-signed or mixed) satisfying (KN_{w,a}); S a (class, cube) set.  Build f^# by
 (1a) Proposition KN of U1-ref (refereed) for the class a;
 (1c') restore kappa exactly (U1-ref Section 1: kappa is continuous, the IVT is exact) and re-realize the values of Omega_act exactly
      (joint explicit fixed point of V1 Lemma TU, block-triangular Jacobian as in U1 2.5/Prop. KN Step 2); NO absorber is tuned;
 (2') the fine structure on J_fine := N \ (F^(1a) ∪ E_c(w) ∪ coordinates fixed in (1a), (1c')), with U1-ref's G1 release, by the static-
      ownership recursion of Lemma CM with owner-candidates (a) Omega_act, (b) coarse peaks of active blocks, (d) EVERY carrier at a stage > L
      of an active block — the zero-value absorbers of D^{U1'} included, now ordinary fine carriers with their FORCED coefficients
      -Delta''_m lambda w; unowned coordinates get z = 0.
Data at t in S: Domega(t) as in U1 Proposition 2.2(e) but supported in Omega := all coarse strict non-peaks (NO absorber coefficients), with the
common true shift Delta''^* (U1 Lemma 4.6(a); its middle term vanishes since (1c') re-realizes all active values); V := V(Domega(t)),
V_proj := L(Delta'(t), gamma(t)) on E_c and 0 elsewhere, V_fine := V - V_proj off F^#;
   b^+ := beta + chi V_proj + (1/2) V_fine,     b^- := b^+ - V(Domega(t)),     omega^+ as in U1 Prop. 2.2(e),  omega^- := omega^+ + Domega(t)
(beta on F^#, chi the V1 Step-4 split on E_c contacts).  Then for every t in S:
 (a) every fine carrier of a negative active block (former absorbers included) is an (R) peak with margin >= q^#_0 delta°_k/2; for m in A_-,
     Scr_m(x) <= C (x/q^#_0)^2 for 0 < x <= x_0 := c_f gap_min Phi_min(L) (coarse carriers: Proposition KN(b); fine ones: U1 Lemma 4.3's argument,
     using c_p <= (delta^max_p H_p/2)^2 at absorber stages, U1-ref 6.2);
 (b) (b^+-, omega^+-) represent g_t (Lemma 1.1 of U1 for the two representations), p*(g - g_t) <= K t, kappa_w <= 1 + eta_0/2, kinds [1]-[3];
 (c) VIOLATIONS: at an E_c contact, z V_proj >= 0 (cone row (X1)) gives viol(j) = (z b^+)_- + (z b^-)_+ <= |V_fine(j)|; at a free coordinate off F^#,
     V_proj(j) = 0, b^+- = +-V_fine(j)/2, so b^theta(j) = 0 ((H3) of Lemma VT) and viol(j) = |V_fine(j)|; on J_fine V_proj = 0, b^+- = +-V(j)/2,
     admissible at coordinates owned by coarse owners and negative fine owners (dominance), V(j) = 0 at unowned coordinates, viol(j) <= |V(j)|
     at coordinates owned by positive fine carriers.  Hence
        eps(t) <= ||V_fine 1_{E_c}||_1 + sum_{j owned by positive fine} |V(j)| <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/T_lo(w) + 2 C_f sum_{l > L} lambda_l,
     where on E_c, V_fine = [L(Delta'', gamma) - L(Delta', gamma)] + (contributions of carriers at stages > L): the first is the trace
     correction of U1 Lemma 4.6(b) (<= C_f Design c_{L+1} in l_1; on near signature sets of coarse peaks it has the admissible sign), the second
     has l_1-norm <= C_f sum_{l>L} lambda_l (coefficients <= C_f lambda, ||u||_1 <= 1).
 (d) cost p*(f^# - f) <= theta_w T_lo(w)^2 with theta_w -> 0 (U1 Lemma 4.5 without the absorber masses), statuses as in Proposition KN(b).
Proof.  (a), (d): the cited statements; the absorbers enter only as fine carriers, which those statements already cover ((W3), (W4'') hold
at absorber stages by U1-ref 6.2, and U1-ref Section 7 gives dominance for owners inside absorber blocks).  (b): U1 Prop. 2.2(e) with the
absorber coefficients removed: g_t changes by the l_1-norm of the removed and re-split parts, <= ||V_fine||_1 + sum |gamma_a| <= C_f Design
c_{L+1} <= K t; Gamma changes by O(c_{L+1}^2) (q_0 h(y) <= ||U||^2 ||y||_1^2/nu).  (c): computed above; free coordinates of J_fine are unowned
(V = 0).  QED
Theorem C_mix' (= X2's Theorem C_mix, with Lemma CM' in place of Lemma CM).  Design D^{X2} with (p-W), N fixed, F finite.  If for infinitely
many main stages L some clean sub-window w of L has a (class, cube) set S of >= n(w)/D_cls(w)^2 scales of one class a (no active shift,
one-signed or mixed) satisfying (KN_{w,a}), then f in Rec(p_N).
Proof.  For each such (L, w): Lemma CM'.  Window family at f_0 := f^#: (U1), (U2) from (b); (U3) from V1 TR(iv) (supports of (1a); with the
constant K_3 of the bound t|b| <= K_3 |a^#| absorbed into (c2)); (U4) from (c) (contact violations, and free violations with b^theta = 0);
(U5) from (a); (U6) Lemma LV(a)-(c) for Omega = coarse strict non-peaks only (no (S-mass) lever), with (p-LV1), (p-LV2) — the data at the
lever coordinates are gamma_l v_l(j) + V_fine(j) (TU) or V_fine(j) (Z), contact-like up to V_fine, with b^theta = 0 at Z-coordinates, so they are
covered by the violation count; (U7) U1 Lemma 2.1.  Levers perturb only fine carriers besides their own (allowedness), which carry no
switching coefficient: their effect is bounded by C (c_tiny + W_lev + W_pull) <= C Design c_{L+1} in the Bregman and scrambling terms
(part 3, (p-UE1), (p-UE2)), and C Design c_{L+1} <= c delta s_1 for s_1 >= exp(-1/(2T)).  Theorem UE (part 3 precisions) at each companion with
s_1 := max(64 rho eps/delta, exp(-1/(2T))) <= s_late (by (W_exp) in c_{L+1}^low: eps <= C Design c_{L+1} <= C Design exp(-1/T)); Theorem E^eng on the
subset S ((p-E1) holds since K_w c_fine <= T^{-C'} exp(-1/T)); (E-c), (E-d), (E-e) as in U1-ref's MT IV'.  QED

## 4.4 Master Theorem V.  Verdict: the STATEMENT is PROVED (modulo the refereed tools it cites) after repair (R-abs); X2's proof of the
## mixed-class part has the gap of 4.2.  The contrapositive (F-finite residual = status coherence, i.e. (KN) failure at almost all
## scales of all clean sub-windows of all large main stages of a (C*) row) is CORRECT.
Checks: the contrapositive is the exact logical negation (for all but finitely many L, every clean w has < n/D_cls scales in classes with
(KN)); classes with no active shift satisfy (KN) vacuously (MT IV' covers them as well); (S1) (multi-block coupling rows) is part of the
exactification of Gamma^#(kappa, a), which Proposition KN performs for all blocks under (KN) — correct; RT*(c) is superseded (coarse exactness
by U1 Prop. 2.2 in the exact route; fine contributions tolerated in the violation route) — correct; U1 Cor. IV.2 (frustration as the shape of a
counterexample) is superseded — correct after (R-abs).

## 4.5 Design D^{X2}.  Verdict: CORRECT (PROVED by inspection) with (p-W) and (p-LV1).
(D-lev): computable at stage L (s_max(L), the signature sets, mu, delta_l, n_l), an additional lower bound on Design(L) — every window theorem
is monotone in Design (U4 Lemma GW).  (W_exp) imposed in c_{L+1}^low after MAIN stages L only (p-W): an extra upper bound on a weight chosen after
all sub-window data of level L; R for absorber targets is computed from c^low; (T-a)-(T-d), (P1), (P2), N-freeness unaffected (only upper
bounds on weights are added; design lower bounds lambda >= 1/D(l) are computed after c_l).  Well-founded.
