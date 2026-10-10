# U4-ref part 2 — Conflicts C1-C9 (C1 and C7 are U4's new defects)

## 2.1 C1 (base 2^{-j} of V1/V2 versus mu_s = 2^{-s^2-1} of V3): CORRECT, with precisions (q3), (q4)
Where the base value enters V1.  I re-read V1 3.1-3.4.  The ONLY numerical use of the base entries s_j is the lower bound of
s_{s'}^2 v_c(s') at BANK coordinates s' = min(S_c ∩ (s_max(L), inf)) <= sigma(L) (donor banks in (C3)(b), Lemma DR(ii); private
banks in Lemma TU, Step 2: "s'^2 v' >= 8^{-sigma(L)} delta_min/2 >= Design^{-1/6}").  Pull coordinates enter only through
Lemma B with ||X_p||^2 <= sum mu_pull^2 s_j^2 <= sum mu_pull^2 (any base with s_j <= 1), and Lemma B(i)-(iii) are exact identities
for any diagonal base with positive entries.  V2 Theorem B uses Lemma TU (same banks) and V2 Step 4 pushes the buffer peak by a
bank at min(S_c ∩ (s_max(l), inf)) <= sigma(l): same bound.  V3-ref VP' uses only f-constants (F_0 finite, fixed by f).
V4's bank levers (Lemma 5.5) have f-dependent masses (mu -> 0 chosen per f; first-order own effect v s^2/nu against later carriers
of weight <= 2^{-10} lambda v by (SF*), the SAME factor s^2 mu/nu multiplying both) — base-independent; not on the critical trees.
Constants with the mu-base (re-derived):
 (a) mu_{s'}^2 v_c(s') >= mu_{sigma}^2 (4/5) delta_min 2^{-sigma} = (4/5) delta_min/B_mu(L) >= Design(L)^{-1/6}, since
     Design^{1/6} >= l 2^{l^3} B_mu/delta_min >= 2 B_mu/delta_min.
 (b) Donor bank mass: mu^D = 2 nu Lam/(lambda_c mu_s^2 v_c(s)) <= 2 (1/4) D(l) (5/4) B_mu Lam/delta_min <= Design Lam
     (nu = ||U^*a|| <= ||U|| = 1/4; lambda_c >= 1/D(l)).
 (c) Lemma B(ii) remainder: |R| <= (||U|| + mu^D mu_s^2/nu) ||X||^2/nu^2 with ||X|| = mu^D mu_s <= Design Lam: C_f Design^2 Lam^2 << Lam.
 (d) Lemma TU: Phi'(y) = sum_l m_l(y)(Delta_l + beta_l)/(v'_l Phi(y)), m_l(y) = (Delta_l y + beta_l (y - nu_p))/(s'^2 v'), so
     |Phi'| <= C |L_0| (eta + kappa)(eta + ||U||)/(s'^2 v'^2) and kappa <= C 4^G eta^2/(s'^2 v'^2) (V1-ref (p4)).  With the
     mu-base 1/(mu_{s'}^2 v'^2) <= (5/4)^2 2^{sigma} B_mu/delta_min^2 <= (25/16)(B_mu/delta_min)^2 <= Design^{1/3}: the
     contraction holds for eta <= c_T = f-constant x Design^{-1} (a fortiori for V1's c_T ~ Design^{-3}); bank masses
     m <= C eta Design^{1/6}, ||X_tune||^2 <= C (4^G + Design^{1/3}) eta^2.  Every inequality of V1 3.3-3.4 survives.
 So the fix B_mu(l) := 2^{sigma(l)}/mu_{sigma(l)}^2 in Design(l) is SUFFICIENT.  CORRECT.
(q3) "The literal V1 factor can fail."  U4 argues by "no factor is FORCED to exceed 2^{2 sigma^2}".  That is the right
 observation but not yet a failure; an explicit instance: define the dense family along the recursion, and when a new index i is
 scheduled for the first time (stage l_i), put y^(i) := normalisation of (ytilde^(i) + eps_i e_{s_i}^*) with eps_i -> 0 fixed in
 advance and s_i odd.  Every factor of V1's literal Design(l_i) except 2^{s_max} 8^{sigma} is independent of s_i (c_{l_i} by
 (W1)-(W7) does not see an odd coordinate: (W4) only involves supp y ∩ S_{l'}, (W6) only |supp y|; D, Lambda°, the Hoffman and
 pattern constants depend on the VALUE eps_i/n, not on the position s_i), so Design_V1(l_i)^{1/6} = A_i 2^{O(s_i)} while
 1/(mu_{sigma}^2 v(sigma)) >= 2^{2 s_i^2}; choosing s_i large (after A_i is known) makes the literal inequality fail at
 every l_i.  So the defect is real for suitable admissible data.  Remark: since sigma(l) >= min S_l = 3*2^l and 1/c_l grows like a
 tower in l (c_{l+1} <= b^2 <= 2^{-8 n(w)}, n(w) >= Design(l)^{20} >= c_l^{-120}), D(l) >= 1/c_l already dominates 2^{2 sigma^2}
 whenever the target supports grow slower than (roughly) the square root of the tower; the defect needs fast-growing target
 supports.  The fix costs nothing, so adopt it.
(q4) C1(v) "the mu-base is FORCED".  The computations are right (re-run, U4_ref_work/rr_check2.py): for W = v_l on S_l (bounded
 gaps) and |a_s| = 2^{-(1+b)s}, the active set at y is {s > log_2(1/y)/b}; with entries 2^{-s}, M^W(y) ~ y^{2/b} (fails (RR) for
 b >= 2); with mu_s = 2^{-s^2-1}, M^W(y) <= 2^{-(log_2(1/y)/b)^2}, super-polynomially small, (RR) for every b > 0.  What is forced is
 SUPER-EXPONENTIAL decay of the base entries (for every b > 0 one needs sum_{s > L/b} mu_s 2^{-s} = O(2^{-(1+eps)L}), i.e.
 mu_s <= 2^{-c s} for every c eventually), not the particular mu.  And "(RR) fails" means "Theorem RS does not apply", not
 "the row is not recovered" (e.g. d-neutral monochromatic super-critical swallowing with supp u_l ⊂ F is covered by Y3
 Theorem 3.5 for any base).  Wording precision only.

## 2.2 C7 ((GM) at l = 1 versus norm one): CORRECT, with precision (q5)
H_1 = 1/60, delta^max_1 = 1/2; sigma = 0 in (GM) gives g_1 <= delta_1 H_1 <= 1/120; Phi_1 = 2^{-m(1)-k(1)} c_1 <= g_1/2 forces
c_1 <= 2^{m(1)+k(1)}/240.  Since j(., m) is increasing, k(1) = 1; c_1 < 1 unless m(1) >= 7 (a ladder starting in block 7 or
later would escape, but the claim "can force" is right; for j(1,1) = 1: c_1 <= 1/60).  Then max q^*(T e) = c_1 < 1: the equality
clause of (T-a) and "norm one" fail.  FIX (GM) for l >= 2, c_1 := 1: correct.
(q5) U4's justification "V4 Lemma 3.4 concerns carriers l > log_2(2 Theta) + 1 >= 2" needs Theta >= 1.  Theta is any UPPER
bound for theta_m, so one may replace Theta by max(Theta, 1); Lemma 3.4's conclusion is then claimed only for l >=
max(2, log_2(2 Theta) + 1), which is all its uses need ("beyond an f-dependent level").  (Also V4-ref R6 lists the (GM) choice of
delta_l before y_l although the (GM) intervals depend on y_l; T_final's order target -> delta_l is the consistent one.)

## 2.3 C2-C6, C8, C9: CORRECT
C2: every condition on c_l is an UPPER bound; the only lower bounds on weights used anywhere are lambda_{l''} >= 1/D(l) and
  Phi_{l''} >= 1/D(l), with D(l) computed after c_l (checked in V1 2.4, Y1 D(l), Z6 D''', V2 Step 6 (entries 1/A_m are
  f-constants)).  Allowedness (b) is used only as the pair property 2 c_l <= 2^{-2s} c_{l'} delta_{l'} (thm:SLD (T-b),(T-c); Lemma TU(d);
  V4 Lemma 4.1'(ii) with tau), which (W4) gives.  (T-d) with allowedness (a), (c) only: re-derived in part 1.
C3: (W1)-(W7) is the minimum of every proposed bound; V2's T_lo(l,M)^3 is dominated by b(l,M)^2 <= T_lo(l,M)^8.
C4: V1 uses b(w) only through b <= T_lo^4/(l Design) and disjoint bands (checked: Lemma CO eta <= Design b, Lemma ST, Lemma D's
  fine-peak bound q_0 b^2/sigma, (R5) tiny components); V2-ref: no lower bound on b anywhere.
C5: the explosive window function and lacunary signature sets occur in none of the three trees (checked the trees of 4.2-4.3).
C6: (FD) changes the target only at k in {2^r}; for k notin K_FD all blocks still follow the same scheduled target, so even
  V2 Cor. C3.1(b) ("every index i is used at infinitely many levels of every block") holds for T_final; (FD) is used only in V4
  Prop. 5.8 (negative).
C8: RS' uses one window per level through (W*) relative to l 2^{l^3} Lambda°(l) <= n(w), the box bound and T_hi -> 0 (checked in
  part 3).
C9: j_0 = 1 is odd; S_l consists of even numbers >= 6.

## 2.4 Numerics for C1 (new; r8/U4_ref_work/)
tu_mu_hp.py (mpmath, 3000 bits): V1 Lemma TU with the ACTUAL base mu_s = 2^{-s^2-1}, banks at j' in {8, 10, 12, 14} (mu_{j'}^2 =
2^{-130} ... 2^{-394}), 1-3 tuned carriers, pulls at v(j) in [eta, 2^G eta] (coordinates up to ~460), tuning size eta = fac x reg,
reg := min_l mu_{j'}^2 v_l(j')^2.  Output tu_mu_hp.out (72 runs):
 - fac <= 0.1 (36 runs): all converge; val^# - val^(2) = x to working precision; all bank masses > 0; |Phi'| <= 0.09 with
   |Phi'| reg/eta in [2e-4, 3]; other carriers move by (0.01 ... 122) eta^2/reg (second order, constant ~ 1/reg);
   bank masses ~ eta/(mu'^2 v').
 - fac = 1: 8/12 converge (one with a non-positive bank mass); fac = 10: 4/12; fac = 100: 0/12 (|Phi'| >> 1).
 So the admissible tuning size is governed by mu_{j'}^2 v'^2 uniformly over 270 binary orders of magnitude of reg: the
 regime constant c_T of Lemma TU must be a function of the BANK factor, exactly what B_mu(l) puts into Design(l).  This tests the
 super-exponential regime that U4's tu_mu_check.py (s_j = 2^{-beta j^2}, beta ~ 0.004, banks at j' ~ 12: s'^2 ~ 0.25-0.7) did not.
rr_check2.py: exponent log M^W(y)/log y at y = 2^{-100}, 2^{-200}, 2^{-400}: base 2^{-s}: 4.01, 2.01, 1.01, 0.67 for b = 0.5, 1, 2, 3
(-> 2/b; (RR) fails for b >= 2); base 2^{-s^{3/2}}: 58.8, 21.2, 7.7, 4.2 (growing: (RR) for all b); mu-base: 1610, 405, 103, 45.
Confirms (q4): any super-exponential decay works; mu is one admissible choice.
