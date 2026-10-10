# U3-ref part 1 — Part 1 of U3: Lemma S, Corollaries S1, S2, Proposition S3, Theorem NL

Checked against: note def:twopiece (l. 2973), lem:rigidity (l. 294), prop:smooth(c), prop:continuity, rem:lemmaZ(c),
cor:BTrecovered, thm:onesided(c); V4 notes Construction SA / Theorem 2.2 (Steps 1-8), Proposition 3.2, Proposition 5.3
(hysteretic re-run), V4-ref (R3).  Scripts re-run: r8/U3_ref_work/nl_check2.py (copy of U3_work/nl_check2.py), output nl_check2.out.

## 1. Lemma S (sandwich of two-piece data).  Verdict: CORRECT (trivial, any admissible T, any N).
Re-derivation.  Two-piece data: g = b^+- + sum_m R_m^*(omega^+-_m - d_m(omega^+-_m) w_m), supp omega^+-_m in Q_m finite.
For j outside Sigma(omega) every R_m^* omega^+-_m vanishes at j, and R_m^*(d w_m) = d psi_m, so
g(j) = b^+-(j) - c^+-(j), c^+- := sum_m d_m(omega^+-_m) psi_m.  Side admissibility gives b^+- (j) = 0 at free j and
z_j b^+(j) >= 0 >= z_j b^-(j) at contacts.  c^+ - c^- = -sum_m Delta_m psi_m = -W_Delta (data convention).  All three items follow.
Remark: this is V2's Proposition C3 plus V4's Lemma 3.3 (D = b^+ - b^- z-signed and zero at free coordinates) read off the
omega-supports; no smallness is needed.  Fine.

## 2. Corollary S1 (one block).  Verdict: CORRECT.
Dividing the sandwich by z_j psi(j) gives: aligned contact -> pi in [-d^+, -d^-] (needs Delta = d^- - d^+ <= 0);
anti-aligned -> pi in [-d^-, -d^+] (needs Delta >= 0); free -> Delta psi(j) = 0, pi = -d^+.  The "consequently" clause needs
an aligned contact for the Delta <= 0 half; as stated.  Oscillation over aligned contacts <= |Delta|.  Checked.

## 3. Corollary S2 (F, K finite).  Verdict: CORRECT.
v = b^+ - b^- = sum_m R_m^*(omega^-_m - omega^+_m) - W_Delta = L^*((omega^- - omega^+) - (Delta_m w_m)_m) lies in Y and is supported
in F u K (finite): v = 0 by (T-c), then L^* injective (eq:Lstar) gives omega^-_m - omega^+_m = Delta_m w_m; at a peak of block m the left
side is 0 and |w_m| = M_m > 0, so Delta_m = 0.  At NA rows z' in c_0, so K is finite (prop:smooth(c)).  Correct; this is the exact
content of rem:onesided(a) for shifts.

## 4. Proposition S3 (non-constant profiles need banks or aligned maximal contact).  Verdict: CORRECT.
Re-derived: at f_n all mates have two-piece data (assumption, e.g. (BT) via thm:onesided(c)); omega-supports lie in Q_n so
Sigma(omega) is contained in Sigma_n; hypothesis (2) + Cor. S1 give Delta = 0 and pi_G constant (= -d^+) outside Sigma_n at all
coordinates with psi_n != 0, and G(s) = 0 where psi_n(s) = 0 (sandwich with c^+ = c^- = 0).  The functional
Lambda_n(h) = h(s_1) psi_n(s_2) - h(s_2) psi_n(s_1) vanishes on C(f_n) and |Lambda_n(h)| <= 2 ||psi_n||_inf ||h||_inf <= ||h||_1
(||psi_n||_inf <= sum_k lambda_k <= 1/2), so the stated l_1 bound holds (even with the better constant 1 instead of 1/2 in front of
the bracket).  psi_n -> psi in l_1 (prop:continuity).  Since p* and ||.||_1 are equivalent (||h||_1/(1 + ||L||) <= p*(h) <= q*(h)),
liminf dist > 0 holds in p* as well.  Hypothesis (1) "each s_i is free or a contact" is automatic once s_i notin F_n.

## 5. Theorem NL (lsc of the fibre map fails at f_SA along (BT) rows).  Verdict: CORRECT.
Checked step by step.
 Step 1.  In def:SLD every target y^(i) is used in every block at infinitely many carriers (the index i occurs infinitely often in
 (i_r) and y^(i) is allowed at all large l); with (Z0), y* is in the family, so carriers o_n -> infinity of block m_0 with target y*
 exist; delta_{o_n} H_{o_n} -> 0.  Since supp y* = F is assigned from the start, B_{o_n} = 0 and A_{o_n} = y*(zhat_F) =
 -(eta + delta_{l_-} H_{l_-}) (from n_{l_-} val_{l_-} = y*(zhat_F) + delta_{l_-} H_{l_-} = -eta).  Targets of carriers < o_n avoid S_{o_n}
 (allowedness (a)); o_n owns only S_{o_n}.  So z^(n) -> z coordinatewise, a^(n) = a, f_n -> f by rem:lemmaZ(c).
 Step 2.  n val^(n)_{o_n} <= -(eta + delta_{l_-}H_{l_-})/2 with z = +1 on S_{o_n}: anti-type; nu_{o_n} -> infinity relative to the
 bounded thresholds, margin >= q_0 eta/4 (|val| >= 2 eta/5).  The hysteretic re-run gives every re-run carrier n|val| >= (B + delta H)/2
 with the sign eps_l (kept: eps n val = eps A + B + dH > (B + dH)/2; flipped: >= B + dH); V4 Theorem 2.2 Step 4 survives the factor 2
 (Phi_l/Phi_k <= (5/4) delta°_l 2^{-l-10}/(1 + ||U||) <= |val_l| 2^{-l-8}/(1 + ||U||)).  ||zeta^(n) - zeta||_1 <= 2(1 + ||U||) sum_{l >= o_n}
 lambda_l -> 0, so the two non-robust carriers (first carrier, l_-) keep their statuses.  Q^(n) = {k_-}, no degenerate peak, (MS):
 (BT).  Checked.
 Step 3.  psi_n(s) for s in S_c is lambda_c w(c) v_c(s) + later terms; V4 Step 6 bounds the MODULI of the later terms
 (coefficients |w| <= 1), so the owner term dominates (|w(c)| = M >= 1/2 at peaks); S_c aligned for swallowing-type c, S_{o_n}
 anti-aligned, both outside Sigma_n = F u S_{l_-}.  Checked (target coordinates of owners are also aligned, not needed).
 Step 4.  V4 Prop. 3.2 with a coordinatewise split chi: b^+ = chi Delta_alpha lambda V 1_{F^c} + beta^+ is z-signed (chi >= 0) and
 b^- = (chi - 1)(...) + (beta^+ - Delta_alpha lambda V 1_F) is (-z)-signed off F; both in l_1 (chi bounded).  At s in S_l, l != l_-,
 u_{l_-}(s) = 0, R^* omega^+(s) = alpha lambda u_{l_-}(s) = 0, V(s) = (|val_{l_-}|/|zeta^|) psi(s), giving the exact profile formula.
 c g in C(f) for small c: from prop:onesidedupper (limsup form, gives p*(f + r g) <= 1 + (r^2/2)(kappa_w + 1) on |r| <= r_0) and
 s(t) - 1 >= min(t^2, |t|)/3; the needed smallness is c^2(kappa_w + 1) <= 2/3 and c r_0 (kappa_w + 1) <= 2/3.  Checked.
Comment on the reading.  The theorem is a genuine and useful NEGATIVE structural fact: membership in Rec cannot be propagated by
an arbitrary dense sequence of (BT) rows, and approximants for oscillating mates must be aligned or banked (Remark (b)).  It does
NOT bear on density (f_SA is (BT), hence in Rec).

## 6. Numerics (re-run, identical output)
nl_check2.py: f and f_n have P = {0,1,3}, Q = {2}; z V >= 0 off F (min 3e-7); profile (2.35e-4, 0, 1.17e-4); max_t [p*(f + t g) -
s(t)] = -5.1e-7 on the grid; gamma^+ at f_n INFEASIBLE, gamma^- = 8.6e-4; p*(f_n - f) = 8.3e-7; max oscillation over two-piece data
1.60e-2 at f versus 2.4e-8 at f_n.
Two precisions on the reading of the output (no effect on any claim):
 (n1) The grid values printed under "At f_n: p*(f_n + t c g) - s(t)" are all NEGATIVE down to |t| = 1e-3: the linear excess of c g at
     f_n (side + violation on S_o of size ~6e-7 per unit t) only beats the quadratic slack below |t| ~ 1e-6, which double-precision
     SOCPs cannot resolve.  The docstring item (2) of nl_check2.py ("> 0 for small |t|") is therefore NOT what the run shows; the
     reliable test is the infeasibility of the side-+ SOCP (item (3)), as U3 Part 5 says.
 (n2) The residual 2.4e-8 at f_n is solver tolerance, not "the difference psi_n - psi" (the script uses psi_n at f_n, where the
     theoretical value is exactly 0 by Proposition S3).
