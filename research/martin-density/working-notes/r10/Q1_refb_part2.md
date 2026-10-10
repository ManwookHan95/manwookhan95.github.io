# Q1 referee (b) — part 2: Theorem A_fin, Lemma GEN_fin, options (a)/(b), N-independence (working file)

## 2.1 Theorem A_fin.  VERDICT: correct (all four items re-derived, see part 1 B3-B6)
 * round 1: any candidate with Sigma(y) != {} fails (c+) (the bound p - 2|supp y| - 1 = 2|Sigma| - 2|supp y| <= 0) or (a); so p_1 = 1
   and stage 1 is the MAIN stage of round 1 in block m_1 = 2 (Phi_1 = c_1/8).  Re-checked.
 * n_l in [3/4, 5/4]: delta_l q^*(h_l) <= delta^max_l (1 + ||U||) H_l <= 1/4.  Used in (T-b) and (T-d).
 * (T-a): ||T_fin|| = sup_l c_l = c_1 (c_l <= c_{l-1}/4); option (a) c_1 in (1/2, 1) transcendental, option (b) c_1 = 1 attained at
   (k, m) = (1, 2).  Martin's proof uses only ||T|| <= 1: v^*_{n,m} in B_Y; ||Phi_m||_1 <= 2^{-m} < 1 (Lemma A); |R_m x|_m <= m 2^{-m} q(x);
   the note's lem:martintail and prop:reduction use only Phi_m(k) <= 2^{-m-k} (checked in the note, lines 120-260).
 * Scaling remark (new): T_fin(a)/c_1 has norm one but is NOT "option (a) in disguise": the norm p is not homogeneous in the weights
   (B_{|.|_m} = B_{l_1} + D_m B_{l_2} with D_m built from the weights), so the coincidence sets B_kappa are not cones and nothing transfers
   from (a) to (b) by rescaling.  Option (b)'s exception (O2) is therefore genuine (agrees with X1-ref W1/W2).

## 2.2 Lemma GEN_fin.  VERDICT: correct.
 (a) k_0 := Q(y(j), delta(y,l), n(y,l) : y in P_Y, l, j) is countable and contains every coefficient that enters a cone row or a floor
     function: u_l(j) (all j — hence the weight-dependent coordinate range E_c(w) up to s_far(w) is harmless), mu_s, H_l, ||U||, aggregated
     signature coefficients (delta_l/n_l) sum_{s' in S_l, s' <= s} 2^{-s'} for every integer s.  The (GM) value delta(y, l) lies in
     Q(y(j) : j) (part 1, B2); n(y, l) may be transcendental (lacunary Hilbert sums) and is put into k_0 by definition.  The CHOICE of the
     absorber target (R, p_0..p_R, s, beta) depends on weights, but every outcome lies in the countable pool A_pool, so k_0 is fixed before
     any weight is chosen.  Correct.
 (b) Transcendence induction: if (c_1..c_n) is algebraically independent over k_0 and c_{n+1} is transcendental over k_0(c_1..c_n), the
     family (c_1..c_{n+1}) is algebraically independent.  Standard.  A finite subfamily is algebraically independent over k_0(any disjoint
     finite subfamily).  Phi_l in Q^* c_l.  Correct.
 (c) What the X1 machinery needs (re-verified from X1 2.2(iv), 2.3, X1-ref 6): B_kappa is defined from (u_l on E_c; peak vectors and peak
     weights; sigma_rob(m) = sum of Phi_p^2 over the pattern's robust peaks; signs and combinatorial labels; weights of (KN)-block carriers;
     ratio variables r) — NO continuous datum of the row f.  The f-dependence of the companion is only through WHICH pattern occurs and the
     position of r(f).  Hence "weights chosen before f" legitimately excludes coincidences for every f.  (This is the point most likely to
     hide an error; it holds.)  Formula-1 kappa (X1-ref K1) is used only to define the variables r; the active weak peaks of f belong to the
     pattern's Omega, not to the peak traces, so tau_m contains no N_T weight.
 (d) Option (b): c_1 = 1 in k_0.  Patterns with stage 1 notin N_T are covered.  The design takes minima over these patterns only (S5).

## 2.3 Option (b), N >= 2, the residual (O2).  VERDICT: correctly labelled OPEN; precise form confirmed.
 The slice problem: with Phi_1 = 2^{-3} fixed, B_kappa ∩ {Phi_1 = 2^{-3}} has dimension < |N_T| - 1 unless, for some stratum S and some
 D ∋ 1, the critical-value set CV_{D,S} contains a (|D|-1)-dimensional piece of the rational hyperplane {Phi_1 = 2^{-3}}; for D = {1} this is
 exactly "2^{-3} is a critical value of psi_1|_S".  For a 0-dimensional stratum S = {r*}, psi_1(r*) = m|r*_1| K(sigma_rob, R_a(r*)^2) is an
 algebraic function of the generic parameters (peak weights through tau_m and sigma_rob); it equals 2^{-3} at algebraically independent
 parameters only if the function is constant.  Constancy is not excluded by any argument I know (r* may depend on the peak weights
 through tau_m in a way that compensates the strictly increasing sigma_rob-dependence of K).  So (O2) stays OPEN.  Note also that rows
 with rho_1(f) = 1 exactly, stage 1 active in a (T)-block, are a non-generic but nonempty-looking set; the theorem for option (b), N >= 2,
 is correctly restricted to rho_1(f) != 1.
 Proof of (b2) re-checked: |rho_1(f) - 1| > b(w) for all sub-windows of all levels L >= L_1 (b(w) <= T_lo(w)^4 -> 0); then stage 1 is not
 near-threshold, so 1 notin N_T(kappa) for f's pattern at every clean w of level >= L_1.  Correct.

## 2.4 N-independence.  VERDICT: correct.
 No rule of 1.1-1.3 refers to N.  For p_N: carriers of blocks > N are absent; their rate objects are the constant 1 (robust); the cone of
 f's class for p_N coincides with the cone of the pattern in which every block > N is inactive (inactive blocks contribute no rows: no
 active carriers, Delta' = 0, no peak trace), which is one of the enumerated patterns of the level (the enumeration is over all
 combinatorial data, realizable or not); QC data involve only (T)-blocks.  The f-constant C_{f,N} (3^N) and any N-dependent exponent of the
 cube count (A_max/eps)^p (p <= number of shift-ray coordinates <= N) are absorbed because Q(w) >= (4 Design(l)/u(w))^{omega(l)+20} and
 omega(l) -> infinity: for fixed N, (E-d) holds for all large L.  [Precision: Q1 1.3(S6) calls C_U1 "absolute"; if the cube exponent is
 N-dependent the clause (Design/u)^{C_U1} must be read as eventually dominated by the first term — harmless.]

## 2.5 A precision in (S6): which Lipschitz constant in delta_0(b)
 KN^tr Step 1 needs F(r') <= F(r_1) + Lip(F)|r' - r_1|, with F = F_Phi = max_d psi_d/Phi_d, whose Lipschitz constant Lip_kappa on K_kappa
 contains 1/Phi_d (d in N_T) and can exceed V2's Lip(l) (Lipschitz constant of the minors).  Q1's (S6) writes delta_0(b) with "Lip" = Lip(l).
 Fix: in (S6) put Lip^*(l) := max(Lip(l), max_kappa Lip_kappa) in delta_0 and in (D1) (and in "robust statuses move by <= Lip eta'").
 Lip^*(l) is a level-l design number (already a factor of Design(l)), so nothing else changes.  [FIXABLE PRECISION P-LIP]

## 2.6 Monotonicity / dominance of Design
 X1's new factors are maxima over the patterns of level l only.  At main stage L only the patterns of level L are used (f's pattern at
 L), so dominance of earlier levels' QC constants is never needed.  U4's part of Design(l) keeps (F9) "dominating all earlier design
 factors"; multiplying by factors >= 1 preserves it.  No issue.
