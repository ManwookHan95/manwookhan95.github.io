# U4 part 2 — Hypothesis audit: every result used by Master Theorems II / III' and Theorem RS', checked for T_final

T_final, U_final as in part 1.  For each result: source and status (refereed where), the design features its proof uses (as
recorded by its author and confirmed by its referee), and the verification for T_final.  "window" below means a window of the
note's SLD; for T_final it is read as ANY sub-window w of the level (Lemma GW).

## 2.1 Lemma GW (generic window use).  PROVED (meta-argument; same as V1 Theorem 1'(d), Y1 Theorem 1(d), Y4 Lemma 1.5(c),
refereed for D_X, D^PW, D_Omega).
In every window theorem of Section 8 of the note and of Rounds 5-7 the window enters only through:
 (i) the dyadic scales of ONE window; (ii) conditions "T_hi x X_l -> 0" and "n / X_l -> infinity" along the levels used, where X_l is
 an f-dependent constant to the power <= l^2 (C_f^{l^2}), times design factors of level l, times (for pigeonhole statements) at
 most omega(l)+3 robust-rate factors u^{-1}, times (for room statements) a room product Lambda_f(l), Lambda^±_f(l) or Lambda*_f(l)
 that the hypothesis of the theorem compares with l 2^{l^3} Lambda°(l); (iii) the box bound sum_{l'>l}|Delta theta_{l'}| <=
 6 sum_{l'>l} lambda_{l'}/t <= 6t^2, which needs sum_{l'>l} lambda_{l'} <= T_lo^3 on the window; (iv) T_hi(next) <= T_lo(previous).
For T_final and any sub-window w = (l,i): (i) W(w) has n(w) dyadic scales; (ii) T_hi(w) <= 2^{-l^3}/(l Q(w)) and n(w) >= l 2^{l^3} Q(w)
with Q(w) = (4 Design(l)/u(w))^{omega(l)+20} >= Design(l) x (4/u)^{omega+3} x ... and Design(l) >= every design factor (part 1, F8),
Q(w) >= Lambda°(l); C_f^{l^2} 2^{-l^3} -> 0; (iii) sum_{l'>l} lambda_{l'} <= b(w)^2/2 <= T_lo(w)^8 (Theorem 1.5(c)); (iv) Theorem 1.5(c).
Hence each such theorem holds for T_final with "window of level l" read as "any sub-window of level l".  QED

## 2.2 Dependency tree of MASTER THEOREM II (V1 4.3) and III' (V2-ref 4b)
Legend: [any T] = valid for every admissible T and every compact dense-range U; [SLD] = uses (P1)-(P3), allowedness (a) (and (b)
only in thm:SLD), windows; [diag] = diagonal base identities; [gaps] = bounded gaps; [sub] = pigeonhole sub-windows; [rate] =
rate scheme; [Des] = design factors in Design(l).  "OK" = holds for T_final, with the reason.

| result (source; status) | features used | T_final |
|---|---|---|
| def:admissible, lem:dualball, lem:threshold, eq:margin, lem:rigidity, prop:forced, prop:smooth(c), prop:approximants, prop:reduction, lem:pair, thm:compact, rem:lemmaZ(c), lem:martintail (note Sec. 1-2; refereed R1-R4) | [any T] | OK (Theorem 1.5(a)) |
| lem:algebra, lem:base, lem:slack, thm:transfer, lem:bookkeeping, lem:TV, lem:transferdata, lem:persistence, def:twopiece, prop:onesidedupper, thm:onesided, def:SC, thm:engineered, cor:D1, def:BT, cor:BTrecovered (note Sec. 3-7) | [any T], I finite | OK |
| def:SLD, thm:SLD (P1)-(P3), R_0, lem:R0, thm:R0, thm:reductionZ (note Sec. 8) | [SLD] | OK: Theorem 1.5 + Lemma GW |
| lem:twosided, lem:smallness, lem:budget, lem:suplevel, lem:finitebase, lem:phicalc, lem:switchbudget, lem:split, lem:peakshift (eq:peakshift, eq:didentity), lem:flip, lem:boundedfree | [any T] | OK |
| lem:box, lem:pinning, lem:triangular, prop:pinned, def:windowcert, prop:windowcert, lem:uniformtransfer, thm:windowed, def:swallowed, lem:modswallow, lem:badpeaks, lem:exactswitch, lem:windowtwopiece, lem:onesidedtransfer, lem:avgfunctionals | [SLD] (thm:windowed, lem:uniformtransfer, lem:onesidedtransfer, lem:avgfunctionals: [any T]) | OK: (P1), (P2), allowedness (a), Lemma GW |
| Z3 Theorem E, Lemma U, Lemma 3.1, Lemma 3.2 (flipped), Prop. T step (5) with T2-T6 (R5; refereed) | [any T]; Lemma 3.1 uses only the clamp formula at zhat, zhat^# (no base parts) | OK |
| Z4 Lemma 5.0 (for M-II.3) | [any T] | OK |
| Y1 Theorem 1 (D_X), Theorem 2 (clean sub-windows), Lemmas T, T2, T3, 3.1-3.6 (constants Y1-ref m2, m5), Prop. 5.2 (structure), Theorem E', kind [1'] (Y1-ref 4), shift trick (Y1-ref (d)), donor bookkeeping (Y1-ref m3) (R6; refereed) | [sub], [rate] (R1)-(R4), [Des] D(l), G**, 2^{sigma}, |T(l)|; rooms on S^nat = S \ (F ∪ T(l)) use (P1) + allowedness (a) | OK: T_final's scheme contains (R1)-(R4); M(l) = omega(l)+1 with omega counting all objects; B_mu >= 2^{sigma}; Lemma GW |
| Y2 Lemma T(c),(d),(e), Lemma U', Theorem E', Lemma 5.1 / Prop. 5.2 (shift cost), generalized configurations, G**, Xi^Y (R6; refereed) | [any T] except Xi^Y [Des] | OK |
| Y3 D_sigma (Prop. 3.3) (R6; refereed) | [gaps], allowedness (c) | OK (F2) |
| Y4 Lemma 1.8 (ray removal; convex geometry), Lemma 2.2 (cost of tuned rows; [any T]), Lemma 2.3 (banked Lemma U / Theorem E; [any T]), Theorem 1.6 (pigeonhole; [sub]) (R6; refereed) | as stated | OK |
| Y4-ref C.1-C.7 (P1 pull effect, P2 pulled support in Lemma U, P3 data at pulls, P4 tuning) (proved by the Y4 referee; re-verified in V1, V1 refereed) | [diag], [gaps], H_tune [Des] | OK (F3, F4, F8); quantitative base factor: C1 |
| V1 Theorem 1' (D_Omega) | design | REPLACED by part 1 (T_final ⊇ D_Omega with B_mu in place of 8^{sigma}) |
| V1 Theorem 2', 2.2 classification, 2.3 pinning, Lemma D, Lemma 3.4', Lemma S, 2.6 patterns/rays (R7; refereed correct, p1-p5) | [sub], [rate] (R1)-(R7), (P2) for fine peaks (sum_{l'>l} lambda <= b^2/2), D(l) | OK |
| V1 Lemma B (3.1) | [diag] (any positive entries) | OK |
| V1 Lemma DR, Lemma TU | [diag], [gaps], s_s^2 v_c(s) >= Design^{-1/6} at bank coordinates s <= sigma(l) | OK only with B_mu(l) in Design (C1); literal V1 Design with 8^{sigma} FAILS for the mu-base (see 2.4(a)) |
| V1 Lemmas CO, ST, NS, RR, Prop. TR, Theorem E'', MASTER THEOREM II, Cor. M-II.1-3, Cor. AC | [diag], [sub], [rate], [Des]; V1-ref p0-p5 | OK |
| V2 Lemma H (Hoffman via minors), Lemma L (Lojasiewicz; BCR Cor. 2.6.7) (R7; refereed correct) | none (pure algebra) | OK |
| V2 Def. 2.1/2.2, Lemma 2.1 (design D^{V2}), Lemma 2.3 (buffer peaks; needs sum_{l'>l} lambda <= T_lo(l)^3) | [rate] determinantal objects, b(w) Lojasiewicz-adjusted, Lip, C_L, N_L, delta_comb, C_* in Design | OK (F6-F8; Theorem 1.5(d) gives V2's (2.1)) |
| V2 Theorem B (+ V2-ref P2: system of V1 Prop. TR, L_0 = Kp), Cor. B.1 | V1 Lemma TU, Lemma ST, (2.1), [diag] | OK (Lemma QB / Step 4 not needed with V1's assembly: V2-ref 3(ii)) |
| V2 Lemma 3.1, Def. 3.2 (+P3 enlarged shift patterns), Theorem C1 (+P7) | [rate] shift-pinning objects, 1/delta_sh optional | OK (F6) |
| MASTER THEOREM III' (V2-ref 4b; PROVED given V1, refereed) | all of the above | OK |

## 2.3 Dependency tree of THEOREM RS' (V3 3.4 with V3-ref Section 3)
| result (source; status) | features used | T_final |
|---|---|---|
| V3 Lemma 2.1, 2.2 (normer change via Z3 Lemma 3.1), 2.3 (raise transfer RT), Cor. 2.4, Theorem 2.5 (E_RT) (R7; refereed correct) | [any T], any F | OK |
| V3 3.1 D^mu, Lemma 3.1 (RR) | diagonal base with mu_s -> 0; (b) needs mu_s = 2^{-s^2-1} | OK (F3); with base 2^{-j}, (RR) fails for profiles |a_s| ~ v_l(s)^{1+b}, b >= 2 (C1(v), numerics part 4) |
| V3-ref Lemma VP' (ND'_{L_0}) (proved by the V3 referee; RE-VERIFIED here, 2.4(b)) | [diag] | OK |
| Z5-ref Theorem R1 Steps 1-4 (Claim 3.1, 3.2), Lemma R2, Lemma R0; Z5 Lemma 5.2 (T10, bounded switching, any F) (R5; refereed) | R1: [SLD] + windows via (W*); R2, T10: [any T] | OK: Lemma GW with (W*) relative to l 2^{l^3} Lambda°(l) <= n(w) |
| note lem:exactswitch, lem:modswallow, lem:badpeaks (+(H3-inf) by V3-ref 3(b)), lem:persistence, def:swallowed, (W*), (H2), (B_fin) | [SLD], allowedness (a) (S*_l) | OK |
| Y3 Theorem 2.1 (T8 with raised support; any admissible T, any F) (R6; refereed) | [any T] | OK |
| THEOREM RS' (V3-ref 3; PROVED "by the inspection standard of Z3 Lemma U", items I1-I3 checked by the V3 referee) | D^mu over an SLD-type design, one sub-window per level | OK.  Step 1 needs: l_j with Lambda*_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0 ((W*)), n_j = O(Lambda*_f(l_j)) = o(n(w_j)) for any sub-window w_j of level l_j, m_j + n_j <= n(w_j), T_hi(w_j) Lambda*_f(l_j) -> 0: all by Theorem 1.5(c) |

## 2.4 Items that needed more than inspection
(a) C1 is a REAL defect of the literal union "D_Omega + D^mu".  V1's Design(l) contains 8^{sigma(l)}, and V1's Lemma TU/DR need
  s_{j'}^2 v_{l''}(j') >= Design(l)^{-1/6} at the bank coordinate j' <= sigma(l).  For mu_s = 2^{-s^2-1},
  mu_{j'}^2 v(j') <= 2^{-2 j'^2 - 2} 2^{-j'}; nothing else in V1's Design is forced to be >= 2^{2 sigma(l)^2}: sigma(l) > s_max(l) is
  governed by the SUPPORTS of the coarse targets (arbitrary finitely supported vectors from a dense family, which may contain huge
  coordinates in Z_0), while the other factors (2^{s_max}, D(l) via 1/Phi, (W1)-(W7)) are at most single-exponential in s_max
  or independent of it (with rule (c), allowedness (b) only involves coordinates s <= l).  So the literal V1 factor does not dominate
  the bank factor; V1's (C3)(b) bank mass bound mu^D <= Design Lam and Lemma TU's contraction (|Phi'| <= 1/2 needs Design >> 1/(s'^2 v'))
  would fail.  FIX (adopted): B_mu(l) := 2^{sigma(l)}/mu_{sigma(l)}^2 in Design(l).  With it, every inequality of V1 3.3-3.4 holds
  verbatim (part 1, C1(iii)).  Numerics (part 4): Lemma TU with s_j = 2^{-beta j^2}: 587 tests, exact to 9e-16, other carriers move
  O(eta^2) with a constant independent of eta, bank masses scale like eta/(s'^2 v').
(b) Lemma VP' (V3-ref, single-referee) — RE-VERIFIED.  For a diagonal base, u(zhat^#) - u(zhat) = sum_{s in F} mu_s u(s)(e^# - e)_s
  depends only on u|_F.  With V_0 := {c : (sum c_k u_k)|_F = 0}, G(x)_k := <U^*u_k, e(x) - e> maps into V_0^perp.  The derivative at 0 is
  Lambda(xi)/nu, Lambda(xi)_k = sum_{s in F} mu_s^2 xi_s (u_k(s) - a_s gamma_k/nu^2), gamma_k = <U^*u_k, U^*a> (direct differentiation of
  x -> U^*(a+x)/||U^*(a+x)||).  c annihilates Lambda(l_1(F)) iff u_c|_F = kappa a|_F with kappa = sum c_k gamma_k/nu^2 (and conversely
  <U^*u_c, U^*a> = sum_{s in F} mu_s^2 u_c(s) a_s = kappa nu^2), so under (ND') the annihilator is V_0 and Lambda(l_1(F)) = V_0^perp; a finite
  F_0 suffices; Graves' theorem gives x in l_1(F_0) with G(x) = 0, ||x||_1 <= C_0 ||U^*Delta a|| (|G(0)| <= 2||U||^2... <= 2||U|| ||U^*Delta a||/nu),
  and |x_s| <= |a_s|/2 on the finite F_0 for small ||U^*Delta a||, so the signs on F are kept.  lambda >= 1 for small y because
  ||U^*Delta a|| <= (max_{active s} mu_s) ||Delta a||_1 = o(||Delta a||_1).  CONFIRMED.
(c) MASTER THEOREM III' (V2-ref 4b) — logic RE-VERIFIED.  V1's proof of Master Theorem II uses (SH_w) only through the shift bound
  |Delta d_m| M_m <= K t (Lemma S -> Step 0 of Prop. TR) and (VR_w) only in Step 3 of Prop. TR (blockwise ray removal).  Theorem C1(I)
  supplies the shift bound with K <= C_f Design^3/u^3 whenever rho^sh >= u.  Theorem B (with the transplant system of Prop. TR, P2)
  supplies a Hoffman projection tau' of tau_0 onto Sigma^# with box rows, ||tau_0 - tau'||_1 <= C_H^# sum_m |Q^#_m(tau_0)|, C_H^# <=
  C_f^l Design^2/u; Steps 4-5 of Prop. TR use only ||tau - tau'||_1, the sign rows and the box rows tau' <= 12 lambda/t (needed for
  (iv): t|b(j)| <= 12 lambda v(j) = mu/2 at pulls, and for kind [2] bounds), all of which Sigma^# contains.  The extra cost C_f Design^2
  eta log(1/eta), eta = T_lo^4/(l Design), is o(T_lo^2); V1's status table survives because the extra value moves are <= 2 eta << c_f Lam.
  CONFIRMED.  (Lemma QB and Step 4 of Theorem B are not used: in V1's assembly every block with a near-threshold kept carrier is
  donor-raised (C3), V2-ref 3(ii).)
(d) Theorem RS' over sub-windows (C8) — CONFIRMED in 2.3.
(e) Features that are NOT used by any of the three trees (and are present in T_final anyway or deliberately absent):
  - explosive window function (D1^F) of Z3-ref part 4 (and Y4-ref A.1, Y2 6.4 SKETCH): absent from T_final, used by none of the trees.
    [Y1's "explosive ladder of SUB-WINDOWS" is the pigeonhole recursion, which T_final has.]
  - lacunary signature sets (V4 Lemma 2.6): absent; used by none.
  - allowedness (c): present; used only by Y3 (Lemma 3.4, Theorem 3.5) and V3 Section 1 (superseded), not by MT II/III' or RS'.
  - (SF*), (SF_tau), (b'), (Z0), (GM), (FD), owners relative to L_N: present; used only by V4 (Theorem 2.2, 3.5, 5.6, Prop. 5.3, 5.8,
    Cor. 5.7, Lemma 3.4, 3.8, R1, R5), i.e. by additional recovered classes and by negative/realizability statements.
  - mu-base super-exponential decay: used only by RS' ((RR)); MT II/III' need only diagonality and B_mu.
(f) Hidden quantitative assumption checked: V2 Theorem B(d)'s factor (2A_max)^{-N} (N-dependent) is >= 1 since A_m <= m 2^{-m} <= 1/2
  (V2-ref attack (iv)); so C_H^# <= C_f^l Design^2/u is N-free up to the f-constant.  The only N-dependence anywhere is through
  f-constants (C_f, l_f), which are absorbed for each fixed f.

## 2.5 Verdict of the hypothesis audit.  PROVED (modulo the cited refereed results).
For T_final every result in the dependency trees of Master Theorem II, Master Theorem III' and Theorem RS' has its hypotheses
satisfied, with exactly two required changes to the literal Round-7 designs: (C1) B_mu(l) in place of 8^{sigma(l)} in Design(l);
(C7) (GM) only for l >= 2 so that c_1 = 1.  No theorem in the three trees uses the explosive design, lacunarity, or any feature that
T_final lacks.  Single-referee items on the critical paths: V1-ref p0-p5 (precisions), V2-ref P2, P3, P7 (re-checked in (c)),
V3-ref VP' and (H3-inf) (VP' re-verified in (b); (H3-inf) strengthening accepted from V3-ref 3(b); with (H3') instead of (H3-inf)
RS' is V3's own refereed statement), Y4-ref C.1-C.7 (re-verified by V1, refereed).
