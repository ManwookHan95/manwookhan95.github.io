# Y4 referee, part 3 — reductions at clean sub-windows, Part 4 of Y4, non-window viewpoints, numerics, hunt

## 3.1 One more gap in D^PW: what Q(w) must absorb (G-PW3)
Cor. 1.7 asserts K T_hi(w) <= C_f^{l^2}/(l 2^{l^3}) with K the window constant.  That needs K <= C_f^{l^2} Q(w).  But the
window constants of Prop. T / Thm U' / Thm E are PRODUCTS of several rate-dependent factors: Prop. T gives
p*(g - g_t) <= C(1 + C_H^#)(K_* + theta)t, where K_* carries the room product (<= Design (4/u)^omega at a clean
sub-window) and C_H^# the d-row Hoffman constant (Lemma 1.8: <= Design/u(w)); Thm U' has K_U = C Lambda_g (1 + K_P + K_R)
H_comb D^2.  So K can reach C_f^{l^2} Design(l)^3 (4/u(w))^{omega(l)+1} > C_f^{l^2} Q(w).  FIX (design): put
Q(w) := (4 Design(l)/u(w))^{omega(l)+3}; all statements of Lemma 1.5 and Thm 1.6 remain true (the product bound
prod (1 + 3/rho) <= (4/u)^omega <= Q(w)/Design(l) is unchanged), and every polynomial combination of Design(l), 1/u(w) and
the room product of degree <= 3 is absorbed.  Similarly n(w) must dominate 1/c_flat ~ Design/(u Phi) (robust gaps) --
covered by the same Q.

## 3.2 Y4 2.4 (reductions at clean sub-windows). VERDICT: SKETCH (as labelled), with corrections.
 (i) Tiny rooms / target rooms closed: correct direction, cost by Z3 Lemma 3.1 with the target-induced term (needs
     (G-PW1)); "PROVED as a reduction (given the transplant)" -- acceptable as a reduction.  NOTE: closing a room RAISES
     eps_l u_l(zhat) by Re(u_l) (Z3 Lemma 1.4) and so can destroy exact d-neutrality; Y4 regards re-lowering as impossible
     beyond |F| - 1 dims; with pulls (my 2.2) it is available per carrier.
 (ii) Anti-sign tiny-gap carriers dropped: PROVED (Lemma 2.9 + claim in Prop. windowcert(c)).
 (iii) Compensated blocks: ADDING a robust ray of the opposite sign neutralizes a mismatch e at cost e/u, independently of
     tiny rays -- correct.  Raising tiny negative rays: Lemma 2.6 for one ray; several: (TC) -- with pulls + private banks
     (diagonal base, Prop. P4) unconditional.
 (iv) (UN+) "OPEN, the genuinely directional residual": NOT A RESIDUAL for a diagonal base and single-block rays (Cor. P5,
     with the sign-constrained Hoffman solve for near-threshold q > 0 carriers); (P+) also handled by pulls.  The parenthetical "Y2's donors settle (P+) except the aligned corner": in the
     aligned corner (Y2 3.4) threshold steering is impossible, but per-carrier pulls lower the value of the degenerate
     swallowing-type peak itself (it becomes a q > 0 strict non-peak with tiny gap, which needs no gap by the inward-only
     expansion); exact d-neutrality must then be re-imposed at the companion (Prop. P4 / Hoffman projection with
     design-controlled d-row).  Plausible: SKETCH, not checked against all of Y2's bookkeeping.
 "Assembly with Thm E, Prop. T, Thms A''/U'/Y at tuned rows": SKETCH -- agreed.  Additional items the assembly must
 include: the transplant at a row with changed a and e (Hilbert-part comparison: |h^#(b) - h(b)| <= C ||e^# - e||/t^2 x
 t^2-normalization = additive O(theta), as in Z3_ref G3), the sign-constrained exact solve of Cor. P5 (always feasible,
 design-conditioned), the order "first push tiny-margin swallowing-type peaks below threshold, then recompute the pattern and
 neutralize its tiny rays", and the closure of the exactified set under slaving (part 1, 1.4).

## 3.3 Y4 Part 4. VERDICT: 4.1(a) overclaimed; 4.1(b),(c) correctly labelled.
 4.1(a) is labelled PROVED, but it depends on (TC) (conditional), Y2's donors (open in the aligned corner), the transplant
 assembly (SKETCH), and -- decisively -- on the restricted move class: with pulls, single-block rays of tiny POSITIVE d-sum
 ARE handled by exactification.  Correct label: SKETCH, and the residual it names is not a residual (diagonal base).
 4.1(b) (un-switching heuristic) HEURISTIC: fine.  4.1(c) Conjecture G_ray OPEN: fine, but NOT needed for the companion
 route at clean sub-windows (diagonal base, single block, (ST)); it would still be needed if one insists on recovery at f
 itself (no companions).
 4.2 relations: "Prop. 2.8 explains why the nearly-neutral part cannot be removed by tuning (diagonal bases)" -- FALSE
 with pulls.  "Lemma 1.8 is the single-block special case of Y2's Theorem M with explicit constant 1/D_min" -- plausible.
 4.3 table: items 14 (the "only |F| - 1 channels" consequence), 17 (assembly), 18 (UN+ as residual) need relabelling as
 above; the "FALSE: nothing new ... exact neutralization by masses removes K_nn is FALSE for positive d-sums with a
 diagonal base" correction is itself only half right: by MASSES alone, yes; by masses + pulls, exact neutralization is
 possible.

## 3.4 Non-window viewpoints (Y4 2.5). VERDICT: correct, elementary, (b) not new.
 (a) D(rho g) = {h : h(y)^2 <= p(y)^2 - rho^2 g(y)^2 for all y} = intersection of the slabs {|h(y)| <= c(y)},
     c(y) := (p(y)^2 - rho^2 g(y)^2)^{1/2} >= 0 (|g| <= p since p*(g) <= 1): convex, symmetric, weak* closed and bounded.
     PROVED.  "Not usable" is a HEURISTIC assessment.  Also correct: the forced-data map is not affine.
 (b) p*(f' + r rho g) <= s(rho r) + eps and s(r) - s(rho r) >= (1 - rho^2) min(r^2,|r|)/3 (Lemma lem:slack(a)) give
     p*(f' + r rho g) <= s(r) for (6 eps/(1-rho^2))^{1/2} <= |r|, provided eps <= (1 - rho^2)/3.  PROVED; this is the
     remark after Prop. prop:scale of the note ("the slack alone certifies the scales |t| >~ sqrt(eps/(1-rho^2))").
 (c) Baire: Remark rem:meagre(c).  Nothing new: agreed.
 (d) Multi-level companions: consistent with Thm E (f_j depends on j; no transitivity needed).  Agreed.

## 3.5 Numerics. VERDICT: N1 reproduced; N3 MISLABELLED (factor 1/t).
 N1 (re-run): diag min z_j h_W(j) = -0.000; mix 46%, rand 48% lowering contacts; raising derivative rel. err. <= 2e-8.
 N3 (re-run, Y4_ref_work/n3_check.py): the objective of min_switch is sum_l (lambda_l/t)(W_+ + W_- - 2w)(l) =
 sum_l lambda_l Delta Theta_l = |Delta theta_1| + |Delta theta_2| (ABSOLUTE switching), not switching/t.  The reported
 "band of height ~1.4e-2 t" is therefore wrong by a factor 1/t: relative switching sum|Delta theta|/t is 0.47 / 0.36 /
 0.36 / 0.22 at t = 1.5e-2 ... 7.1e-2 for eps_rel = 1, and 0.04 / 0.10 for eps_rel = 0.01.  The qualitative reading
 (forced switching O(t), transient, not growing as D_B -> 0; in fact smaller for smaller D_B here) is unaffected.
 Validity of the mate is tested only on a 14-point grid; finite models are degenerate (Y4 says so).  HEURISTIC.
 N2: not re-run (sanity, degenerate; correctly labelled as trivial).
 New (pull_check.py): see part 2 -- pulls lower exactly the pulled carrier by 2 v(j), cost O(v(j) + mu).

## 3.6 Counterexample hunt
Y4 claims no counterexample; its "diagonal candidates" (1.6) are descriptions of what would have to fail.  Attempts:
 * (UN+) as a counterexample mechanism: dead for diagonal bases (pulls); the value-side status issue (a q > 0
   near-threshold carrier inside a tiny ray must only be lowered) is solved by the sign-constrained system R x = -V,
   x_NT <= 0 (feasible because x = -v works; Hoffman gives a small solution; part 2, Cor. P5).  What is left is the
   block-threshold drift O(Delta) common to ALL exactification moves = the status part of Z3's (BS) (bookkeeping, not a
   counterexample mechanism: a buffer of size C_f Phi Delta suffices).  A counterexample would have to
   live in multi-block rays (m') (determinantal, not linear, exactification), in the coherent shift resonance (Y2 item
   (h)), in non-diagonal bases if one insists on them, or at infinite F.
 * Rates: impossible for D^PW (Thm 1.6), as Y4 says.
 * Weak* vs norm, c_0 vs l_infty: pulled and banked rows have finite support and z in l_infty (not c_0) -- they are NOT
   norm-attaining, which is allowed (Thm E applies Cor. D1 at f_j).  Quantifier order: f_j is built after g, rho and the
   window (Thm E); the design (D^PW, (G), (G-PW1), (G-PW3)) is fixed before f.  N-freeness: all added design quantities
   (2^{G_l}, ||R^+|| over patterns, 1/(s_{j'}^2 v(j'))) are N-free.  Uniformity in t: the pull masses mu_j are fixed per
   window; the no-flip bound t|b(j)| <= 12 lambda v(j) holds at every scale of the window.
 Nothing found points to a counterexample.
