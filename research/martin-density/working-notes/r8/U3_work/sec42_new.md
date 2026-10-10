## 4.2 Lemma VT (violation tolerance of the engineered approximants, single stage).  PROVED (line-by-line modification of the
## proof of Theorem thm:engineered in the note; nothing else is used).
Setting.  I finite, f in S_{p*} with F finite, rho in (0,1), g in X^* with g(xi) = 0.  Let (b^+, omega^+), (b^-, omega^-) be pairs that
REPRESENT g in the sense of Definition def:twopiece (g = b^+- + sum_m R_m^*(omega^+-_m - d_m(omega^+-_m) w_m), omega^+-_m in c_00,
supp omega^+-_m in Q_m), but are NOT assumed side-admissible.  For j notin F put
   viol(j) := (z_j b^+_j)_- + (z_j b^-_j)_+   if j in K (contact),      viol(j) := |b^+_j| + |b^-_j|   if j notin F u K (free),
and epsilon := sum_{j notin F} viol(j) (<= ||b^+||_1 + ||b^-||_1).  Two-piece data are exactly the case epsilon = 0.  Hypotheses:
 (H1) rho^2 kappa_w < 1, kappa_w := max(Gamma_w(b^+, omega^+), Gamma_w(b^-, omega^-)) (the formula of def:twopiece);
 (H2) I_- := {m : Delta d_m < 0} satisfies (SC) (no assumption if I_- is empty);
 (H3) (theta-exactness at free coordinates of the window) b^+_j + b^-_j = 0, i.e. b^theta_j = 0, at every free coordinate
      j <= N_w with viol(j) > 0 (for instance: at every violated free coordinate).
Statement.  Choose delta, T_1, K_sharp, eta_1, the transfer data and T_0 exactly as in Step 0 of the proof of thm:engineered for the data
(f, b^+-, omega^+-, rho), except that K_sharp is replaced by K_sharp + 1.  Let (N_w, s_1, N'') be a stage of the construction sequence of
that proof which is late in the sense of that proof (all statements there marked "at late stages" hold at it) and at which (H3) and
     (VT)   2 rho epsilon <= delta s_1 / 16
hold.  Then the engineered approximant f' (Definition def:engineered; norm-attaining) and g' := rho(g'' - c a') of Step 1 satisfy
     p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta)      for 0 < |tau| <= T_0.
Proof.  (1) Where admissibility is used.  Step 0 uses the data only through kappa_w (Gamma_theta <= kappa_w by convexity; (H1)) and
through the finitely many constants listed there; Step 1 and Step 2 use only the two representations (g'' - g -> 0, g'(x-hat') = 0,
the identities beta^+- - beta^theta = +-(1/2)v, v = b^+ - b^- = sum_m R_m^*((omega^-_m - omega^+_m) - Delta d_m w_m)); Step 3 (Blocks)
uses only supp omega^diamond_m in Q_m and the radius conditions; Lemma lem:approxfacts uses b^theta only through the masses
m_j = 4 rho s_1 |b^theta_j| and ||b^theta||_1.  The sign conditions on b^+- enter ONLY the claim of Step 3 (Base),
Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} (and = 0 for diamond = theta).  We replace it by
     Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} + 2 rho |tau| epsilon   (diamond = +-, s_1 < |tau| <= T_0),
     Exc'(tau B^theta) = 0                                                (0 < |tau| <= s_1).                          (*)
(2) Proof of (*).  By Lemma lem:bookkeeping(b) at f', Exc'(B) = sum_j (|a'_j + B_j| - |a'_j| - z'_j B_j); on supp a' the summand is
2(-sgn(a'_j) B_j - |a'_j|)_+, off supp a' it is |B_j| - z'_j B_j.  With B = tau B^diamond = tau rho(beta^diamond - c a'):
 on supp a', a'_j + tau B_j = (1 - tau rho c) a'_j + tau rho beta^diamond_j with 1 - tau rho c >= 1/2, so the summand equals
 2(-x - (1 - tau rho c)|a'_j|)_+ <= 2 (x)_- with x := z'_j tau rho beta^diamond_j.
 * j in F: no flip by (T_1), summand 0 (unchanged).
 * window contact with mass (j in K, j <= N_w, b^theta_j != 0; z'_j = z_j): diamond = theta: |tau rho b^theta_j| <= m_j/4 <= |a'_j|/2,
   summand 0 (for either sign of b^theta_j).  diamond = +: tau > 0, x = tau rho z_j b^+_j, summand <= 2 rho |tau| (z_j b^+_j)_-.
   diamond = -: tau < 0, x = -|tau| rho z_j b^-_j, summand <= 2 rho |tau| (z_j b^-_j)_+.  In both cases <= 2 rho |tau| viol(j).
 * window contact without mass (b^theta_j = 0, so beta^theta_j = 0 and b^+_j = -b^-_j): off supp a'; diamond = theta: 0;
   diamond = +: |tau rho b^+_j| - z_j tau rho b^+_j = 2 rho |tau| (z_j b^+_j)_-; diamond = -: = 2 rho |tau| (z_j b^-_j)_+; <= 2 rho |tau| viol(j).
 * free j <= N_w: off supp a', |z_j| <= 1; diamond = theta: beta^theta_j = b^theta_j = 0 if viol(j) > 0 by (H3), and b^+-_j = 0 if viol(j) = 0;
   summand 0.  diamond = +-: summand <= 2 rho |tau| |b^diamond_j| <= 2 rho |tau| viol(j).
 * contact j in (N_w, N'']: beta^theta_j = 0; beta^+-_j = +-(1/2) v_j, so for diamond = sgn tau, tau beta^diamond_j = (1/2)|tau| v_j and the
   summand is rho |tau| (z_j v_j)_-.  Since z_j v_j = z_j b^+_j - z_j b^-_j >= -(z_j b^+_j)_- - (z_j b^-_j)_+, (z_j v_j)_- <= viol(j).
 * free j > N_w: beta^theta_j = 0; |beta^+-_j| = |v_j|/2 <= viol(j)/2; summand <= 2 rho |tau| |v_j|/2 <= rho |tau| viol(j).
 * contact j > N'': z'_j = 0, summand rho |tau| |v_j|/2 (diamond = +-) and 0 (theta): this is the term (1/2) rho |tau| V_{>N''} (unchanged).
 Summing gives (*).  (Free coordinates are never in supp a' = F u {window contacts with b^theta != 0}.)
(3) Constants.  For |tau| > s_1, (VT) gives 2 rho |tau| epsilon <= delta |tau| s_1/16 <= delta tau^2/16 <= tau^2/32, so the bound
hat G_b <= K_sharp tau^2 of Step 0 holds with K_sharp + 1, and Step 4 (rebalancing, |varepsilon_m| <= 6 K_sharp tau^2, error E <= delta tau^2/8 by
the choice of eta_1 with the new K_sharp and the (T_0) conditions) is unchanged.  K_A (bound for (|q*(A_tau) - 1| + q*(A_tau - a'))/|tau|) is
finite since beta^diamond in l_1; it is chosen before T_0 as in the note.
(4) Step 5.  hat Gamma = c' hat G_b + sum_m sigma'_m hat G_m gains at most c' 2 rho |tau| epsilon <= delta tau^2/16 (c' = 1/p(x-hat') <= 1) in the
+- regimes and nothing in the theta-regime.  Hence, for 0 < |tau| <= T_0,
     p*(f' + tau g') <= 1 + (tau^2/2)(rho^2 kappa_w + delta/8 + delta/8 + delta/8 + delta/4 + delta/8) = 1 + (tau^2/2)(1 - 2 delta + 3 delta/4)
                     <= 1 + (tau^2/2)(1 - delta).   QED
Remarks.  (a) In-window CONTACT violations need no bank when (VT) holds: their cost is the same linear 2 rho |tau| viol(j), paid only
for |tau| > s_1 (in the theta-regime the masses m_j protect every window contact, whatever the sign of b^theta_j).  Banks (Lemma QB2)
are needed only for violations whose mass is NOT <= delta s_1/(32 rho) at an admissible s_1.
(b) Free violations inside the window with b^theta_j != 0 are NOT tolerated: they cost 2 rho |tau| |b^theta_j| for |tau| <= s_1, which is
not O(tau^2); free coordinates cannot carry masses (that would change z'_j from |z_j| < 1 to +-1, an O(1) move of x-hat').  This is the
reason for (H3).
(c) What the lemma does NOT give.  Step 6 (Lemma lem:assembly) needs a pair (f_0, g_0) with g_0 in C(f_0) and p*(f' - f_0) <=
(1 - rho^2) T_0^2/6, p*(g' - rho g_0) <= (1 - rho^2) T_0/6.  A functional with violated data is in general NOT a mate of f (U3_work/
vt_check.py: positive excess at f), so in applications the assembly is made relative to the ORIGINAL pair (f_0, g_0) = (f, g) of the
(C*) row, which needs T_0 (of the violated data at the companion) to be large compared with sqrt(p*(f' - f_0)): a uniformity statement.
Moreover (VT) bounds s_1 from below, while "late" means s_1 below a threshold s_late(data) (Bx_m = o(s_1), (E4) convergence, scrambling):
the lemma is useful iff epsilon <= delta s_late/(32 rho).  Both points belong to (S2), see 4.3 and 4.3'.
