# G2 referee, part 2 (working log): (R1) section -- coupled directions, H2.A', capped generators, Theorem ML, Theorem 4.9

## 2.1 Lemma 3.1' (status calculus) and Lemma 3.2 -- re-derived
- l_d(Delta) = Delta_d/rt_d + 2 kappa'_(d) m^2 sum_{k in Omega_(d)} rt_k Delta_k.  (a), (b) immediate.  (c): for d not in {l,p}:
  2 kappa'_(d) m^2 (|rt_l| 1[l in Omega] - c_lp |rt_p| 1[p in Omega]) <= 0 by the partner condition and c_lp |rt_p| >= |rt_l|;
  d = l: 1/|rt_l| + 2 kappa'_(l) m^2(|rt_l| - c_lp|rt_p|) = 1/|rt_l| - kappa'_(l)/(kappa'_* |rt_l|) = 0 when the kappa' inside c_lp is
  kappa'_(l) (G2 says so); d = p: both terms <= 0.  Size c_lp <= Des^C/u^2.  (d) (notes form, c_l = 1[l in N]/|rt_l| + 2 kappa'_max m^2|rt_l|):
  l_d(rt^{(m)}) = 1 + 2 kappa'_(d) R^2_(d) >= 1 gives l_d(v_l) <= 0.  CORRECT.  (Part-2 form with division by 1 + 2kappa' R_m^2 needs
  R^2_(d) = R^2_m; the notes' form is the right one.)
- Numerics N1 re-read: first-order max 1.1e-13; second order <= 3.6 (n1b) -- consistent.
- Lemma 3.2: the bound kappa_m(z_l - c_lp sgn(rt_p) z_p) <= Des^C u^{-3} c_MS holds for the MINIMAX element z* only (it is (1.1) applied to
  v_lp/||v_lp||_rt); "every hull element z" is FALSE in general (a hull element far from the minimizer need not pair below c_MS with D_1).
  PRECISION P-32.  The use in H2.A' is for z* only: correct.
- Partner with rt_p = 0 (KN holds at 0) is excluded by |rt_p| >= u Des^{-C_3}: correct.

## 2.2 Theorem H2.A' -- re-derived; CORRECT (mod chain, with P-32)
Free K^-: inward direction rbar_l e_l in D_1 gives kappa_m z*_l rbar_l < c_MS; with z*_l >= -e_1 (linear, inherited).  Free K^+ in (U)-blocks:
v_l in V (rt^{(m)} in V: every row is movable or in a group whose (U)-pieces are tangent by Euler's identity), R-PK for z*.  Unprotected
shifted: outward direction.  Partner: Lemma 3.2.  Case analysis uses only (1.2), Prop. 3.1(a)-(c) (all linear, inherited) and these bounds.

## 2.3 Lemma 4.2 (CAP): FIXABLE GAP G-CAP
R is defined as a BOX {sum t_g g : 0 <= t_g <= cap_g} with capacity W/2 for EVERY uncapped generator.  The Brouwer step of Lemma
III-cone(c) needs ||Rem(t)|| <= C_2 ||t||_2^2 <= rho_0 = C_2 W^2 on the domain; on the box ||t||_2 can be (W/2)|G|^{1/2}, |G| up to Des^C
(one TS/FR/ZD generator per design-depth coordinate), so ||Rem|| up to C_2 W^2 |G|/4 >> rho_0, and T(t) = S(b - Rem(t)) need not be defined.
Fix (either): (i) R := (W/2) conv(G_u ∪ {0}) + {sum_{G_c} t_g g : 0 <= t_g <= cap_g}, with sum_{G_c} cap_g <= W/2 (cap each margin lever at
W/(4|Lambda_A|), harmless since cap_min << W/Des); then ||t||_1 <= W, ||Rem|| <= rho_0; (b) reads (W/2) max_{G_u}(y^T g)_- + sum_{G_c}
cap_g (y^T g)_- < phi_y + rho_0.  (ii) keep the box and put rho_0^box := C_2 (W/2)^2 (|G_u| + 1) (still << x).  Lemma 4.3 (MS^cap) is
unchanged (only G_c enters Phi^cap; G_u enters through Y).  The selection S is continuous on R (polyhedral multifunction, Hoffman/Walkup-Wets).
N2's LP test uses the box but has no remainder, so it is unaffected.

## 2.4 Lemma 4.3 (MS^cap): CORRECT after G-CAP
Phi^cap convex in y (sum of affine and of t -> cap (t)_-), linear in Delta; Sion on compact convex sets.  (a): a CAP(b)-certificate at rt'
is a near-certificate of size < 2(||b(rt')|| + rho_0)/W, in Y by Lipschitz transport; Phi^cap(Delta*, y) = -phi_y(rt') + sum cap(y^T g)_-
+ O(Lipschitz error of capped columns) < rho_0^max + small: the threshold needs a factor 2 margin (cosmetic).

## 2.5 Lemma 4.4 (OD) and Lemma 4.5 (MV): CORRECT
OD is an identity (insert (2.2) into phi = <kappa z*, rc - rt_0>); MV(a) pairing with rt^{(m)} in V; MV(b) (JF1) at a movable row seen by all
statuses (signs re-derived: both multiplier terms have the sign of rt_l).  PRECISION P-JF1: kappa'_(d) inside Lambda.

## 2.6 Theorem ML (refined form of G2): GAPS G-MU, G-LAM, G-NAFF (fixable by hypotheses)
The proof bounds |S_res,aff| <= |mu| beta(b) with "|mu| <= Des^C/u by V2 Lemma H for robust minors".  Two problems:
(G-MU) mu solves J^T mu = (kappa z* - A^T lambda)|_G - err; its size is governed by the smallest NONZERO singular value s_J of the
  tiny-polynomial Jacobian J of the group, not by the minors of Gamma^#.  J's entries are cofactors (rate objects), but J's minors are
  NOT rate objects of the design (they are polynomials in several cofactors), so s_J may be tiny-but-nonzero (or intermediate between b and
  u) at a clean sub-window; for affine groups J does not depend on the group's ratios, so no target choice exactifies it.  Then
  S_res ~ beta(b)/s_J, and the required capacity is ~ kappa dist(rc, Z) ~ beta/s_J, not Des^C beta/u.  NUMERICS R1 (G2_ref_work/r1_mu_gap):
  one (U)-block, three pinned kind-(iv) rows, two tiny homogeneous minors J = [[1,1,1],[1,1+s,1-s]] (all cofactors robust, every 2x2
  minor O(s)), P(rc) = (0, beta), FULL target freedom on Z, capped downward levers: minimal capacity c_need = 3.33 beta/s (s = 1e-1..1e-4:
  c_need/beta = 3.3, 33, 333, 3333); certificate lower bound 1.67 beta/s; with a robust J: c_need = 0.5 beta.  All hypotheses (S), (G),
  (B) of the notes' Theorem ML hold in this model, so the PROOF is wrong as written; the statement needs a robust-Jacobian hypothesis.
(G-LAM) |mu| also involves ||A^T lambda|_G||, unbounded when Lambda_m is unbounded; MV only bounds Lambda_m in blocks whose statuses
  descend.  Lambda_m is bounded (<= Des^C/u^2) when rt^{(m)} is in V or m has a movable row of robust ratio seen by all its protected
  statuses (pair (2.2) with -rt^{(m)} or with the inward direction) -- all (U)-blocks; not in general for shifted blocks.
(G-NAFF) S_naff for non-affine kind-(i) groups: ||nu|_G|| is small only if A^T lambda|_G is small (z* small on kind-(i) rows is not enough);
  needs Lambda_m small (Lemma MV hypotheses) in blocks containing such groups.
REPAIRED STATEMENT (refined form): replace (S), (G) by
 (S+) Lemma 4.5's conclusion Lambda_m <= Des^C (eps + e_1 + e_3 + c_MS)/u^2 in every protected block whose statuses are lowered OR which
      contains a pinned group;
 (G+) every pinned group containing a kind-(iv) row has V_G = tangent space and a ROBUST Jacobian: smallest nonzero singular value
      s_J >= (u/Des)^{C_J} (affine groups included; for non-affine groups full row rank as in Lemma NL);
and put the term Des^C beta(b)/(u s_J) into cap_min.  Then the proof goes through (re-derived in ref notes).

## 2.7 REFEREE ADDITION: Theorem ML' (crude margin levers) -- PROVED (mod chain + G-CAP fix); no (S), no (G), no (K1-depth)
Statement.  At an (R1) stage put cap'_min := Des^{C_m} max(x, ||b(rt_0)||)/eff_min (>= 2x).  Call a kind-(iv) row CONTROLLED if it is free
and not locked, or it has a pullable coordinate j in S_l with v_l(j) in [cap'_min/2, x''_max] (pinned or locked rows alike; (U') bounds only
the aggregated capacity in [c_0 W, x''_max] by 4W'; superseded by G2_ref_notes C.7).  If every
block satisfies (B) (two-sided lever: all K^- or all K^+ controlled; kappa-raising only: all K^- controlled; kappa-lowering only: all K^+
controlled), Step A is realized.
Proof.  Lemma MS^cap with G_c = the margin levers (pull pre-placed with its compensating bank; capped column -eff_l e_l + small).  If not
realized, z* in conv(Y) satisfies (3.1); Delta = 0 gives sum cap_l (z*^T g_l^-)_- < phi_{z*}(rt_0) + rho_0^max <= ||b(rt_0)|| + rho_0^max,
because |phi_{z*}| = |z*^T Ft(rt_0)| <= ||z*||_2 ||b(rt_0)||_2 <= ||b(rt_0)||.  Hence (z*_l)_+ <= Des^{-C_m} + small on margin-levered rows;
z*_l >= -e_1.  Free rows: bounds of H2.A' (from D_1, no multipliers).  Per-block case analysis of H2.A' with "controlled" as above, C_m >=
C_3 + C_4 + C: |z*_l| <= c_1/(16|Lambda_A|) on all kind-(iv) rows, against Prop. 3.1(a) for z*.  Depth range: [cap'_min/2, c_0 W] is inside
the certified pre-placement range [x, x'_max] of Definition III-Areg/III-resources (cap'_min/2 >= x; c_0 W <= x'_max), nonempty when C_A >=
C_m + 6.  QED
Consequence (Theorem 4.9'): a non-realized (R1) stage has a block residual in the sense of H2.A' with "uncontrolled" = pinned or locked and
WITHOUT any pullable coordinate at depths [cap'_min/2, x''_max] (deep-swallowed over the whole certified range).  The classes (P-prot) and
(P-naff) of Theorem 4.9 are NOT needed.  G2's refined form (after (S+), (G+)) extends the swallowing range down to cap_min/2 (~ Des^{C_m -
C_A} eta') at the price of (P-prot'), (P-naff') and (K1-depth).
Note: N2's case (B) uses capacity 4(rho_0 + max|b_P|) ~ ||b||: it tests ML', not the refined cap_min.
