# X2-ref part 3 — Lemma UE-1, Theorem UE, Theorem E^eng, (S2c)

Refereed against: thm:engineered (Steps 0-5, constants (T_1), (T_0)), lem:approxfacts, lem:F1, lem:anchor, lem:scrambling, lem:TV,
prop:rebalancing, lem:transferdata, lem:persistence, lem:assembly, lem:slack, prop:reduction; U3 Lemma VT (as verified by U3-ref); Z3 Lemma
3.1; U1 Lemma 2.4; X2 parts 1-2 with my parts 1-2.

## 3.1 Lemma UE-1.  Verdict: CORRECT (PROVED) after precisions (p-UE1)-(p-UE4); none changes a conclusion.
(a) sizes: correct (Corollary M1' crude bound; Lemma DC; Z3 Lemma 3.1 with delta = xhat' - zhat_0: d-consistent Omega carriers move by
    <= K Pi, carriers meeting pull coordinates contribute <= W_pull (p-DC2), the cut-off <= t(N'')).
(b) values: correct for carriers not meeting lever coordinates; (p-UE1) for carriers meeting a PULL coordinate the move is 2|u_k(j_p)|, not
    <= C_lev r (p-DC2); with the diagonal base the lever MASSES affect carriers not meeting their coordinates only at second order (Lemma M1(i)),
    so the bound Pi_X + C_2 r + t_k can even be sharpened to Pi_X + C(||X|| + ||X_lev||)^2/nu^2 + t_k.
(c) block data: correct (lem:F1 monotonicity through the fixed natural peak; norm Lipschitz).  By my part 1 (referee addition),
    |C' - C| <= K sum_{Q \ Omega} Phi_k |v'_k - v_k| <= K (c_fine Pi + W_pull) at a d-consistent row, much better than K_w Pi.
(d) Bregman: correct, plus <= 4 W_pull for carriers meeting pull coordinates (|w' - w| <= 2, |Delta u| <= 2).
(e) scrambling: correct for the carriers it treats; (p-UE2) two additions: carriers meeting pull coordinates add <= 4m W_pull to the sum
    over A_m and 4 W_pull^2 to ||D(w' - w)||^2; and the d-consistent Omega carriers are in S_2 whatever their Phi_k gap_k (w'(k) = (C'/C) w(k),
    gap' >= gap/2), so (U5) is needed only for carriers OUTSIDE Omega — this matters for zero-value absorbers in a negative block 1, whose
    Phi_a gap_a is tiny (part 2, (A5)).
(f) base form: correct.
(g) targets: (p-UE3) |c_i| <= K_w (Pi + c_fine + tail_W)/t_i (the term 2 c_fine from ||R_m^*(w^0 - w')||_1 is missing in the first bound and
    present in the second); harmless.
(p-UE4) The radius of Lemma DC must be r := 4 K_J (1 + 1/A_min)(delta_1 + T^4 s_1) (p-DC1).

## 3.2 Theorem UE.  Verdict: CORRECT (PROVED) as a conditional theorem after the precisions below; the substance (exact d-consistency
## removes the only first-order term that is not uniformly small, so K_sharp and c_flat are f-constants) is right.
Checked line by line against thm:engineered:
 * Step 0' (order f -> K_sharp -> eta_1 -> transfer data, r_f -> c_flat (first-order conditions) -> t_1 (quadratic conditions) -> window ->
   N_w -> s_1 -> N'' -> levers): consistent; every condition (c1)-(c7) involves only quantities fixed before it.  K_sharp is an f-constant.
   (If A_0 is window-dependent, A_0 = C_f (Design/u)^C as in V1 TR, then c_flat >= c_f (u/Design)^C; harmless under Q(w).)
 * Step 1-2: the three decompositions are exact for violated pairs (only the two representations at f_0 and v = V(Domega) are used); with
   d' = d on Omega, Omega^+- = rho(omega^+- - d^+- w') + rho(d^+- - d^theta)(w' - w^0) and kappa = 0 (re-derived).
 * Step 3 (Blocks): lin'_m = r_m <V^an - w', R x'>/sigma' exactly (lem:algebra at f'; re-derived both anchor cases); radius conditions for
   kinds [1]-[3] in the +- regimes ((c4): 4 rho c_flat <= 1/4 follows from rho c_flat (A_2 + 2) <= 1/3 and A_2 >= 1) and in the theta regime
   ((LATE): s_1 <= t gap'/(2 rho A_2)); r_m <= 1/16 by (c5) (c_flat C_Delta <= C_min/(4 C_W)).
 * Step 3 (Base): claim (*) re-derived at every new coordinate type of f': F, E (U3), masses, Z-type lever coordinates (zero data — or, after
   repair R-abs, fine-residue data with chi = 1/2, cost <= 2 rho |tau| |residue|, counted in eps), TU banks (contact-like data, theta-mass if
   in the window), TU pulls (no flip: at j_p in E_c the data are b^+- = (chi, chi - 1) V(j_p) with V(j_p) = gamma_l v_l(j_p) (+ a fine residue after R-abs,
   super-small against lambda_l v_l(j_p)), |gamma_l| <= lambda_l (2 A_2/t + C_Delta) because |Domega| <= 2 A_2/t; so |tau rho b(j_p)| <=
   rho c_flat (2 A_2 + C_Delta)(1 + o(1)) lambda_l v_l(j_p) <= mu_p/3 = 8 lambda_l v_l(j_p) needs (c3') rho c_flat (2 A_2 + C_Delta) <= 7 instead
   of X2's (c3) rho c_flat (A_2 + C_Delta + 1) <= 8; a constant), contacts and free coordinates beyond the window as in Lemma VT.
 * Step 4 (rebalancing), Step 5 (levels): identical to thm:engineered with T_0 = c_flat t_i; every cubic/quartic error is (const) c_flat tau^2
   because the data enter as K/t (re-derived: K_W/t, K_A/t, K_H/t, K_h/t).
Precisions.
 (p-UE5) (LATE) as displayed, s_1 <= c_late delta min{T^3 gap_min/(n A_0 K_w)^2, x_0 T/(n A_0 K_w)}, does NOT imply the inequalities actually
   used in Step 3 (K_w^3 s_1 log(e/s_1) <= c delta for the Bregman/scrambling terms; K_J (C_2 + C) r <= 1/4 and r <= r_0 for Lemma DC; Pi <= 1/K_w;
   K_w^2 s_1 log(e/s_1) <= theta T^2 in Theorem E^eng).  Since K_w is a polynomial in window quantities, the correct s_late is an explicit
   window quantity of the form c delta (T gap_min x_0/(n A_0 K_w))^C; in the application it is still >= T^{C''} (part 4.2 below), so nothing
   downstream changes.
 (p-UE6) (W-a) must carry the lever factor (or use the sharpened (b)): c_fine <= c_late delta T/(n A_0 (1 + C_2 K_J)), and W_pull <= c delta s_1 must
   be added; both are automatic at U1's companions (super-small weights).
 (p-UE7) The statement "lever coordinates carry zero or contact-like data" holds at U1's companions only with the zero-value absorbers in
   place — which is exactly what fails (part 2); with repair R-abs they carry zero/contact-like data up to fine residues, tolerated as
   violations.

## 3.3 Theorem E^eng.  Verdict: CORRECT (PROVED) as a conditional theorem; one missing hypothesis (p-E1).
Re-derived: (A^eng) from Theorem UE; (B) from g in C(f) and the triangle inequality; the two cases |r| <= r_0 (I_r empty: Assembly-type
inequality 1 + (r^2/2)(1 - delta) <= 1 + r^2/2 - r^4/8 <= s(r) for r^2 <= delta; I_r nonempty: |r| > c_flat T gives eps' <= 2 theta' r^2/c_flat^2,
sum_{I_r} t_i < 2|r|/c_flat for dyadic scales) and |r| >= r_0 (lem:slack(a), min(r^2,|r|) >= r_0|r|); gbar_j in C(f'_j) by convexity;
prop:reduction(d).  The subset version (U1 Lemma 2.4) applies verbatim (only "dyadic" and the count are used).
(p-E1) The proof needs K_w (K_w s_1 + c_fine + tail_W) <= K T^2; the c_fine part is NOT implied by (W-a) (c_fine <= c T/(n A_0) while K_w can be
T^{-C'}); add "K_w c_fine <= K_j T_j^2 2^{-2 n_j}" to (E-f), and choose N_w with tail_W <= K T^2/K_w (not only <= T^3) — free choices, both true
at U1's companions under (W_exp).
Remark: E^eng is a genuinely new averaging scheme (averaging AT the norm-attaining approximant, per-piece bounds, no exactness of the
averaged data, no final call of cor:D1); it is what makes violated data usable along windows.  Correct.

## 3.4 (S2c) threshold comparison and (W_exp).  Verdict: arithmetic CORRECT for the window constants of the COARSE levers; the claim
## "lever constants <= Design(L)^C" is FALSE for X2's absorber (S-mass) levers (part 2, (A3)); after repair R-abs it is correct.
 (i) n <= log_2(1/T), Design <= n, gap_min >= c_f T^4/(L Design) (Prop KN(b)), x_0 >= c_f gap_min Phi_min(L) (coarse carriers only — tuned
     absorbers would violate it, part 2 (A5)), C_S <= C/q_0^2, coarse lever constants <= Design^C ((D-lev) with n_l): K_w <= T^{-C'},
     s_late >= T^{C''} (with the corrected s_late of (p-UE5)).  The intermediate "exp(C log^2(1/T))" is loose but its conclusion holds.
 (ii) fine weights: c_fine, c_tiny, W_pull <= C_f c_{L+1} (W_pull far smaller); violation mass <= C_f Design c_{L+1} after R-abs.
 (iii) with (W_exp) c_{L+1} <= exp(-1/T_lo(L, M(L))) <= exp(-1/T): all comparisons hold for large L, and s_1 := max(64 rho eps/delta,
     exp(-1/(2T))) is admissible; it also dominates C c_{L+1}/delta, which the lever perturbations of fine carriers need (part 4).
 (p-W) Placement of (W_exp).  As written ("at every stage l+1") it contradicts D^{U1'}'s cluster rule c_{p+i} := c_{p+1}^low 4^{1-i} (at the
     cluster stage p+2 the bound exp(-1/T_lo(p+1, M(p+1))) is far below c_{p+1}^low/4, sub-window data being defined at every stage).  Only
     c_{L+1} after MAIN stages L is used; impose (W_exp) in c_{L+1}^low for main stages L (equivalently read T_lo of the last main stage).  Then it
     is compatible with D^{U1'} (R is chosen from c^low; only upper bounds are added) and admissibility/N-freeness are unaffected.
 "(W10) does not suffice": not checked (irrelevant, a design choice is made).
