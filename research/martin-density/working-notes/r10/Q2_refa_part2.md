# Q2 referee (a), part 2 -- Section 2 of Q2 (finite base support in the violation-tolerant route)

Sources: Q2_notes.md 2.1-2.5; r9/X2_notes.md 1.1-1.5, 3.1-3.6, 4.1 (Theorem UE, Lemma UE-1, Theorem E^eng); r9/X2_ref_notes.md
(precisions (p-DC1)-(p-DC3), (p-UE1)-(p-UE7), (c3'), (p-E1), (p-W), (R-abs)); r7/V3_notes.md 2.3-2.5; the note (lem:bookkeeping,
lem:transferdata, lem:persistence, lem:assembly).

## 1. Lemma M2^inf.  VERDICT: correct (PROVED).
X2's proof is a compactness argument through prop:continuity (no finiteness of F: a_n -> a in l_1, e_n -> e, scalar data, D_m w_{n,m} ->
D_m w_m) and lem:persistence, whose proof uses only prop:continuity, lem:threshold at the fixed peak k_*, and dominated convergence with the
majorants lambda_k ||u_k||_1, Phi_k.  lem:transferdata uses tau_* = (pi(xi)/q_0) a - pi with a in l_1 (any F).  The removed clause
"F subset supp a'', |a''_j| >= a_min/2" has no infinite-F analogue (a_min = 0) and, in X2, is used only in (c1).  I checked the other uses of
F in X2 parts 1-4: Lemma M1 (stated for masses off/on the support of the base row f_0, not of f), Lemma DC ((SEP) refers to f_0), Lemma UE-1
(all bounds in terms of Pi and f_0's data).  None needs the clause.

## 2. Theorem UE^inf.  VERDICT: correct as a conditional theorem (PROVED as a modification of the refereed X2 Theorem UE), with
## precisions (p2.1)-(p2.4) below; none changes the conclusion.
I re-derived every new coordinate class of Step 3 (Base) at the approximant f' (data B^diamond = rho(beta^diamond - c_i a')).
 (a) j in F_0 cap [1, N_w] (support of f').  theta piece (|tau| <= s_1): |tau rho beta^theta_j| <= s_1 rho |b^theta_j| <= |A''_j|/8 by the
     definition of W_F (j notin W_F: |a_0(j)| >= 8 rho s_1 max_i |b^theta_i(j)|; j in W_F: modulus raised to that value).  +- pieces (side +
     used for tau > 0, side - for tau < 0): the anti-sign part of tau rho beta^+-_j is |tau| rho (s_j b^+_j)_- resp. |tau| rho (s_j b^-_j)_+,
     <= rho c_flat C_+ |a_0(j)| <= |a_0(j)|/8 <= |A''_j|/8 by (U3^inf) and (c1^inf).  Since |a'_j| >= |A''_j|/2 (q*(A(P*)) <= 2) and
     |tau rho c_i| <= 1/2, s_j(a'_j + tau B_j) >= |a'_j|/2 - |a'_j|/4 > 0: summand of Exc' = 0 (lem:bookkeeping(b): the summand on the support
     is 2(-sgn(a'_j)(tau B_j) - |a'_j|)_+).  Correct.
 (b) j in F_0 cap (N_w, N''] (contacts of f' of sign s_j, a'_j = 0, z'_j = s_j): beta^theta_j = 0; beta^+-_j = +- v_j/2.  The summand
     |x| - s_j x (x = tau rho beta_j) equals 0 if s_j v_j >= 0 and rho|tau||v_j| if s_j v_j < 0 (BOTH sides then use anti-sign mass |v_j|/2).
     Total <= rho |tau| tail_W <= delta s_1 |tau|/64 <= delta tau^2/64 for |tau| > s_1, and 0 in the theta regime.  Correct.
 (c) j in F_0 beyond N'' (free coordinates of f', z' = 0): summand rho|tau||v_j|/2 (+- pieces), 0 (theta): inside X2's cut-off term.  Correct.
 (d) Representation: beta^+- - beta^theta = +- v/2 on all of N (on [1,N_w] because b^+- - b^theta = +- v/2; beyond N_w by definition), so the
     three decompositions of f' + tau g'_i are decompositions of the SAME functional (X2 construction, unchanged).
 (e) Step 5 arithmetic: rho^2(1 + eta_0/2) = 1 - 2 delta; X2's budget 1 - 2delta + 4(delta/8) + delta/4 = 1 - 5delta/4; the new linear term
     rho|tau| tail_W <= (tau^2/2)(delta/32) gives 1 - 5delta/4 + delta/32 <= 1 - delta.  Step 4: the new term adds <= delta tau^2/64 <= K_sharp tau^2
     to hat G_b and hat Gamma; |eps_m| <= 6 K_sharp tau^2 is unaffected.  Correct.
 (f) Cost: q*(a' - a_0) gains q*(a_0 1_{(N_w,inf)}) <= (1 + ||U||) alpha_0(N_w) (the dropped tail) and the same bound for the normalization
     (|1 - q*(A)| contains alpha_0(N_w) + ||U* a_0 1_{(N_w,inf)}||): total 2(1 + ||U||) alpha_0(N_w).  Correct.
 (g) Order of choices.  X2's s_late ((LATE) with (p-UE5)), (VT') (the violation mass eps of the data at f_0) and K_w do not involve N_w (the
     crude mass bound ||X|| <= 4 rho s_1 mu_1 n A_0/T is N_w-free), so choosing N_w AFTER s_1 is legitimate.  Correct.
 (h) Norm attainment: a' is supported in [1, N_w] cup W cup (lever coordinates) (finite); z' = 0 beyond N''; at the finitely many truncated
     contacts |z'_j| = 1 <= 1; prop:smooth(c) applies.  Correct.
Precisions.
 (p2.1) The lever radius of Lemma DC ((p-DC1): r = 4 K_J (1 + 1/A_min)(delta_1 + T^4 s_1) + 8 K_J W_pull/A_min) must use the value move delta_1 of the
        TRUNCATED pre-row, which now contains Pi_tr = 2||U* a_0 1_{(N_w,inf)}||/nu_0 <= 2 s_1 T^4/nu_0 and the W_F raises (first-order nu-change, X2
        Lemma M1(iv), bounded by 2||U* X_F||/nu_0).  Q2's (M2) says "Pi enlarged by Pi_tr"; with r recomputed from delta_1 this is consistent: Pi <=
        K_w s_1 still holds with K_w enlarged by an f-constant.  The pull coordinates (v_l(j_p) in [r, 2^G r]) are then chosen AFTER N_w (their
        position depends on r, hence on N_w only through Pi_tr <= 2 s_1 T^4/nu_0, harmless).
 (p2.2) (S-mass) levers at THICK support coordinates (allowed in (U6) of 2.2): the lever moves A(p) by up to K r beta_p = K r nu_1/(mu_p^2 |u_l(p)|).
        The no-flip argument (a) at p needs the moved modulus >= |A_1(p)|/2, i.e. K r nu_1 <= mu_p^2 |u_l(p)| |A_1(p)|/2.  With (D-lev)
        (mu_p^2 v_l(p) >= Design(L)^{-1}) and |A_1(p)| >= u(w) this is K K_w s_1 nu Design(L) <= u(w)/2: an extra upper bound on s_1 of window type,
        compatible with (VT') under (W_exp) (eps <= C_f Design c_{L+1} <= C_f Design exp(-1/T)).  It must be added to (LATE) (or to (U6)).
 (p2.3) (W-c) of X2 (tail_W <= c_late delta T/A_0) is dropped from (i^inf); it is implied by tail_W <= T^3 for T^2 <= c_late delta/A_0.  Harmless.
 (p2.4) (U4) (H3) "b^theta = 0 at violated free coordinates j <= N_w" must be read for all j (N_w is now chosen after s_1, so the hypothesis cannot
        depend on N_w); beyond N_w the engineered data have beta^theta = 0 anyway.  Harmless.

## 3. Theorem E^{eng,RT,inf}.  VERDICT: correct (PROVED as a modification of X2 E^eng + V3 E_RT), with precision (p2.5) (statement must allow
## window-dependent C_+, hence window-dependent c_flat, because Proposition 3.2 produces C_+ <= C Design(L)/u(w)).
Re-derivation.  (B'): p*(f'_j + r g'_{j,i}) <= p*(f_j + r rho g) + p*(f'_j - f_j) + |r| p*(g'_{j,i} - rho g); hypothesis (a) and V3 Cor 2.4
((s(lambda x) - 1)/lambda <= s(x) - 1 + (lambda - 1) min(lambda^2 x^2/2, 1): phi(lambda) := (s(lambda x) - 1)/lambda has phi' = (s(u) - 1)/(lambda^2 s(u)),
u = lambda x, and (s - 1)/s <= min(u^2/2, 1); re-derived) give p*(f_j + r rho g) <= s(rho r) + (lambda_j - 1) min(lambda_j^2 rho^2 r^2/2, 1) + eps'_j.
The zeroth-order truncation cost 2(1 + ||U||) alpha_0(N_w) <= 2 theta T^2 enters exactly like eps'_j: (B') is used only for pieces with c_flat t_i < |r|,
i.e. |r| > c_flat T, where 2 theta T^2 <= 2 theta r^2/c_flat^2.  The case analysis (|r| <= r_0: max{1 + (r^2/2)(1 - delta), s(rho r) + E} + (1/n) sum_{I_r}
2 rho |r| K t_i <= s(r); |r| > r_0: all pieces by (B')) is X2's with the extra (lambda_j - 1) term <= (1 - rho^2) r^2/48 absorbed in the margin
s(r) - s(rho r) >= (1 - rho^2) r^2/3 (lem:slack(a)).  gbar_j in C(f'_j); (f'_j, gbar_j) attains its norm (prop:reduction(d)); f'_j has finite base support.
"In particular (LSC-trunc) at (f, g, rho)": immediate.  Quantifier order (f, g, rho -> base rows and windows -> s_1 -> N_w -> levers -> N'') is per mate,
which is all that density needs ((R1): density <=> (f, rho g) in cl NA for every f, g in C(f), rho < 1).
 (p2.5) As stated ("fixed A_0, A_2, gamma_B, C_+"), E^{eng,RT,inf} does not cover the output of Proposition 3.2, where C_+ = C_+(w) <= C Design(L)/u(w) is
        WINDOW-dependent; then c_flat(j) >= c_f u(w_j)/(C Design(L_j)) (by (c1^inf)) is window-dependent and the proof needs (as in X2's E^eng (E-d))
              n_j c_flat(j)/K_j -> infinity    and    theta_j / c_flat(j)^2 -> 0
        (the latter from "eps''_j <= 2 theta'_j T^2 <= 2 theta'_j r^2/c_flat^2").  Both HOLD for the design: Q(w) >= (4 Design(L)/u(w))^{omega+20},
        n(w) >= l 2^{l^3} Q(w), T_lo(w) <= 2^{-n(w)} (V1/U4/Q1 1.1), and the companion cost rate is theta_w = C_f T^2 log(1/T) (Q1 Lemma CM^tr (f)) or
        C_f Design T_lo log(1/T_lo) (V1); so n c_flat/K_w >= l 2^{l^3} Q(w) c_f u^5/(C_f Design^2) -> infinity and theta_w Design(L)^2/u(w)^2 <= C_f Design^2
        u^{-2} 2^{-Q(w)} -> 0.  Hence (p2.5) is a statement fix only: E^{eng,RT,inf} should be stated with C_+(j), c_flat(j) and the two displayed
        conditions (as X2's E^eng (E-d) already does for gamma_B(w)).

## 4. Attack log for Section 2 (all negative)
 - Scale uniformity: every new cost is either 0 (theta regime; support coordinates kept), or LINEAR in |tau| with a coefficient <= rho tail_W chosen
   after s_1 (so <= delta tau^2/64 above s_1), or zeroth order (truncation cost) <= 2 theta T^2, used only above c_flat T.  No transition-band problem:
   the transition between "transferred" (pieces finer than r, bound (B')) and "exact" (pieces with c_flat t_i >= |r|, bound (UE)) is the per-piece
   split I_r, identical to X2's.
 - Raise/truncation error accounting: the raise mass never enters (only through lambda_j, V3 RT); the truncation mass alpha_0(N_w) enters only the
   zeroth-order cost (bounded by theta T^2 by the choice of N_w), the Hilbert footprint enters Pi through Pi_tr <= 2 s_1 T^4/nu_0.  Consistent.
 - Hidden use of finite F_0 in X2's steps: checked Steps 0'-5 and UE-1(a)-(g): the only uses are (c1) [replaced], the mass set on E [replaced by W_F],
   and N_w >= max F_0 [replaced by (i^inf)].  Lemma M1(iii)'s value bound and (f)'s base-form bound are support-independent.
 - Per-mate quantifier order: correct (see 3).
