# V3 referee notes (Round 7): proofs of the fixes and improvements

Part files: r7/V3_ref_part1.md (Sections 1-2), V3_ref_part2.md (design, (RR), VP, numerics), V3_ref_part3.md (Theorem RS),
V3_ref_part4.md (Theorem A, M_inf, residuals). Scripts: r7/V3_ref_work/rt_indep.py, vp_check.py.
Notation and numbering: paper/martin_density_note.tex ("the note"), r7/V3_notes.md ("V3"), r5/Z5_ref_notes.md (R1 = Theorem R1,
R2 = Lemma R2), r6/Y3_notes.md (Theorem 2.1). I finite, p = p_N. Labels PROVED / SKETCH / HEURISTIC / OPEN / FALSE.

## 0. Verdict summary
| V3 item | Verdict |
|---|---|
| Lemma 1.1, model 1.2, Remark 1.3 | correct computations; the interpretive sentences ("copied data lose only 9/8", "factor 2 belongs to deep assignment") are HEURISTIC |
| Lemmas 2.1, 2.2, 2.3 (RT), Cor 2.4 | correct (re-derived; independent numerics) |
| Theorem 2.5 (E_RT) | correct (all constants re-derived) |
| D^mu, Lemma 3.1 (RR) | correct |
| Lemma VP | correct proof, statement gap: (ND_{L_0}) fails trivially when some u_k vanishes on F; fixed by (ND') below |
| Theorem RS | correct (inspection items checked) with the (ND') fix; strengthened below to (H3-inf) and to L_0 = B_np |
| Theorem A, Cor 4.2 | correct with the (ND') fix; |b^theta| can be dropped from W |
| Theorem M_inf | reduction correct; the transport of Y1/Y2 to infinite F is a SKETCH with an unaddressed rate issue (Section 5) |
| Remark 3.5(e) (second clause) | FALSE as stated (lem:martintail is about density, not individual rows) |

## 1. Why the main mechanism is right (summary of the re-derivation)
Lemma 2.3. If f + lam r h = A + L*W with max(q*(A), ||W||) = pi, then with B := (A - a)/(lam r), Theta := (W - w)/(lam r):
f^# + r h = (A + Da)/lam + L*((1 - 1/lam)w + W/lam) + L*(w^# - w). Same signs on F give ||a + Da||_1 = ||a||_1 + ||Da||_1, hence
||Da||_1 <= lam - 1 + ||U*Da|| and q*(A + Da) <= pi + (lam - 1) + 2||U*Da||; convexity of N_m for the block part (lam >= 1).
So p*(f^# + rh) <= 1 + (pi - 1 + 2||U*Da||)/lam + p*(L*(w^# - w)). The raise mass cancels against lam - 1; the mate condition at
f becomes, at f^#, a mate condition with quadratic coefficient lam = 1 + O(||Da||_1) plus an additive error controlled by the
Hilbert footprint ||U*Da|| (Lemma 2.2: w depends only on zhat, Z3 Lemma 3.1 applies verbatim). Theorem 2.5 needs only that
additive error to be o((T 2^{-n})^2); for D^mu and a raise at level y on the active set {|a_s| < y W_s},
||U*Da|| <= y M_mu^W(y) = O(y^{2+eps}) under (RR_W). This is what defeats the Round-6 objection "nested raises cost
~ kappa D^2 T^2": that objection concerned p*(f_j - f), which is no longer the relevant quantity.

## 2. Fix 1: the non-degeneracy condition of Lemma VP (PROVED)
For a diagonal base, u(zhat^#) - u(zhat) = <U*u, e^# - e> = sum_{s in F} mu_s^2 u_s (a^#_s/||U*a^#|| - a_s/nu): it depends only on
u|_F. Define, for a finite set L_0 of carriers,
  (ND'_{L_0})   a|_F does not belong to span{u_k|_F : k in L_0}.
(As stated in V3, (ND_{L_0}) requires Lambda : l_1(F) -> R^{L_0} onto; it fails whenever some u_k|_F = 0 or two restrictions
coincide, cases in which nothing needs to be corrected.)
Lemma VP'. Assume (ND'_{L_0}). There are a finite F_0 subset F and c_0, C_0 > 0 such that for every raise Da with
supp Da cap F_0 = {} and ||U*Da|| <= c_0 there is Da'' in l_1(F_0), ||Da''||_1 <= C_0||U*Da||, |Da''_s| <= |a_s|/2, with
u_k(zhat^#) = u_k(zhat) (k in L_0) for the row with forced data ((a + D)/q*(a + D), z), D := Da + Da''.
Proof. Let V_0 := {c in R^{L_0} : u_c|_F = 0}, u_c := sum c_k u_k. (i) For x supported in F, <U*u_c, U*x> = sum_s mu_s^2 u_c(s) x_s;
so for c in V_0 and every perturbation supported in F, c.G = <U*u_c, e(.) - e> = 0 (e(.) is a multiple of U* of a vector supported
in F, and so is e): G takes values in V_0^perp. (ii) Lambda(x)_k = sum_{s in F} mu_s^2 x_s (u_k(s) - a_s gamma_k/nu^2),
gamma_k = <U*u_k, U*a>; c annihilates Lambda(l_1(F)) iff u_c(s) = a_s (sum_k c_k gamma_k)/nu^2 for all s in F, i.e. iff
u_c|_F = kappa a|_F for some kappa (then automatically kappa = <U*u_c, U*a>/nu^2). Under (ND') this forces kappa = 0, so the
annihilator is V_0 and Lambda(l_1(F)) = V_0^perp. Pick finitely many s spanning V_0^perp: this is F_0. (iii) G(x)_k :=
<U*u_k, e(x) - e>, e(x) := U*(a + Da + x)/||U*(a + Da + x)||, x in l_1(F_0), is C^infinity on {||U*(Da + x)|| <= nu/2} with second
derivatives bounded by a constant of f; DG(x)xi = <U*u_k, P^perp_{e(x)} U*xi>/||U*(a + Da + x)||, which at (Da, x) = (0, 0) is
Lambda(xi)/nu, onto V_0^perp from l_1(F_0); by continuity in (U*Da, x) it has a right inverse of norm <= 2C_Lambda nu on a
neighbourhood. |G(0)| <= ||U|| ||e(0) - e|| <= 2||U|| ||U*Da||/nu. The quantitative surjective mapping theorem (Graves) for
G : l_1(F_0) -> V_0^perp gives x with G(x) = 0 and ||x||_1 <= C_0||U*Da||; for c_0 small, |x_s| <= |a_s|/2 on the fixed finite F_0. QED
Lemma 2.3 holds for this row with the extra error 2||Da''||_1 (V3, re-derived), and lam >= 1 for small y because the active set
leaves every finite set, so ||U*Da|| <= (max_active mu_s)||Da||_1 = o(||Da||_1).
Numerics (vp_check.py): derivative formula confirmed to 6 digits; Newton on |F_0| = 5 restores three values to 1e-17 with
||Da''||_1/||U*Da|| ~ 0.40; a carrier vanishing on F has a zero Lambda-row and zero value shift.

## 3. Theorem RS, corrected and strengthened (PROVED, by the same inspection standard as Z3 Lemma U)
Theorem RS'. Design D^mu over the SLD operator (or D_sigma, SLD_G, D''', D_X, D^PW, D^Y), every N >= 1. Let f in S_{p_N*}
(F arbitrary) satisfy R1's (W*), (H2), (H3-inf), (B_fin), and, with B_np := {l in B : k(l) is a strict non-peak of f},
  (ND'_{B_np})  and  (RR_{U_{B_np}})  M_mu^{U_{B_np}}(y) = O(y^{1+eps}).
Then f in Rec.
Proof. V3's proof (raise along U_{B_np} at level y_j = 4C_tau T_j, VP' correction for L_0 := B_np, R1's Steps 1-4 at f_j,
Lemma R2 with U_* = 0, Theorem 2.5 with Y3 Theorem 2.1 at f_j for (e)), with the following additions.
(a) Why L_0 = B_np and W = U_{B_np} suffice. The exact switching is X = sum_{l in B} eps_l tau'_l u_l with tau'_l = 0 on
B_pk, so |X| <= C_tau U_{B_np} and the raise along U_{B_np} empties R1's deep set D_t for t <= T_j. The cone Z_f involves values
only through the d-rows sum_{l in B_np, m(l) = m} q_l tau_l (q_l = eps_l q_0 val_l/sigma_m for strict non-peaks), which VP'
preserves up to a positive factor per block. Bad peaks are non-degenerate (margins move by O(eps_e)) or are handled by (b).
(b) (H3-inf) instead of (H3'). Let l in B_K sit at a degenerate peak k of block m with sgn w_m(k) = -eps_l. Keep the cone Z_f
(row tau_l = 0). Z_f is contained in Z_{f_j}: for tau in Z_f, tau_l = 0 makes the f_j-coefficient of l irrelevant, and the
other d-coefficients are proportional by VP'. At f_j, with g_j := M^{(j)}(1 - q_0^{(j)}|val^{(j)}_k|/(vartheta^{(j)}_m Phi_m(k)))_+
= O(eps_e) (because q_0|val_k| = vartheta_m Phi_m(k) at f and all quantities move by O(eps_e)):
 - if k is a peak of f_j, lem:badpeaks(c) at f_j gives tau_l <= lambda_l K_d t;
 - if k is a strict non-peak of f_j (gap g_j), put varsigma := -eps_l (= sgn w^{(j)}_m(k) for small eps_e), X := varsigma omega_+(k),
   Y := varsigma omega_-(k). lem:suplevel(f) (|d_pm t| <= 1/2) gives X <= 3g_j/(2t), Y >= -3g_j/(2t), and
   Y - X = varsigma(omega_- - omega_+)(k) = -varsigma Delta Theta_m(k) - Delta d_m (M - g_j) = -tau_l/lambda_l - Delta d_m(M - g_j)
   (Delta Theta_m(k) = Delta theta_l/lambda_l = -eps_l tau_l/lambda_l). Hence tau_l <= lambda_l(|Delta d_m|M + 3g_j/t) and
   |X| + |Y| <= (Y - X) + 6g_j/t <= |tau_l|/lambda_l + |Delta d_m| M + 6g_j/t;
 - in both cases (tau_l)_- <= c(tau)/(2 m_l) (sign row of B_K, m_l = ||v_l 1_{S_l \ (F cup T_0)}||_1 > 0) and |Delta d_m|M <= K_d t
   (lem:badpeaks(a) at f_j).
Since g_j = O(eps_e) = o(t^2) on the window, the violation of the row tau_l = 0 is O(K* t), the Hoffman projection onto Z_f
(constant of f) gives tau' in Z_{f_j} with sum|tau - tau'| <= C_f K* t, and in the data omega^pm_m(k) = 0 (the window
certificate vanishes at peaks and at coordinates of gap < t^2). The closeness estimate at k uses
lambda_k(|omega_+(k)| + |omega_-(k)|) <= |tau_l| + lambda_k(K_d t + 6g_j/t) = O(K* t). Nothing else changes. QED
Inspection items (I1)-(I3), checked: (I1) all budget lemmas use s(t) - 1 <= t^2/2 and g(xi) = 0 only; at f_j the budget is
(1 + eta'_j)t^2/2 with eta'_j <= (lam_j - 1)lam_j^2 + 2theta_j + O(eps_e/t) -> 0 on the sub-window; lem:smallness by contradiction
along pairs (j_n, t_n), where j_n -> infinity necessarily (for fixed j only t >= T_j 2^{-n_j} occur). (I2) the bounded-switching
map converges in operator norm on R^B. (I3) Lemma R2 with U_* = 0: no flips since r(sb)_- <= |a^{(j)}|/4; transfer data from f
via lem:persistence; A_0, A_2, gamma_B uniform. (W*)-data, rooms, B, eps_l, T_0, K are z/F-data and do not move.

## 4. Theorem A (PROVED with (ND'_{L_0})); simplification
W := (s b^+)_- + (s b^-)_+ suffices (drop |b^theta|): Lemma R2 uses only the side part of each pair, and Y3 Theorem 2.1 imposes
nothing on b^theta. Also p*(g - g_y) = O(eps_e log(e/eps_e)) (normer change), which is harmless. Corollary 4.2 is immediate from
lem:pair and prop:smooth(c) (NA first rows have finite base support).

## 5. Theorem M_inf: the reduction is PROVED; the transport of finite-F master theorems is a SKETCH with a gap
Reduction: Lemma 2.3 at the base row f^ex_j and p*(f^ex_j + lam r rho g) <= s(lam rho r) + p*(f^ex_j - f) give Theorem 2.5(a)
with eps'_j + p*(f^ex_j - f). Gap in the "Consequence": at exactifying companions of Y1/Y2/Y4 the set L_0(j) of carriers whose values
must be preserved grows with the level; the VP' constants C_0(j) (conditioning of Lambda on L_0(j) restricted to F) are
f-dependent rates; the raise depth then needs log C_0(j) = o(n^w_{l_j}) (and (ND'), (RR) at f^ex_j, whose support may contain
pulled/banked coordinates). This is not automatic for a fixed design: an "exactness versus scale" condition of the familiar kind.
Z4 Theorem A (infinitely many swallowed carriers) does not belong in a list "under (B_fin)".

## 6. Other corrections
(a) Remark 3.5(e), second clause: FALSE as stated. lem:martintail turns density for p_N (all first rows, infinitely many N) into
density for p; it says nothing about an individual first row of p_N versus first rows of Martin's p (Sections 7-8 of the note
assume I finite). (b) V3_part3 Remark 3.5(a): the raise mass is y m_B(y) (~ kappa y^2 critical), not "~ T_j". (c) Section 1:
copying B_pm on the deep set leaves the consistency defect Delta B - X (l_1-size O(K* t), first order at scales r << t), which the
9/8 statement ignores: HEURISTIC. (d) V3's helper block_norm (rt_check.py) computes the gauge of conv(B_1 u D B_2), not of
B_1 + D B_2; it feeds only q_0, which does not enter f, so the reported numbers stand.

## 7. What remains open after V3 and this report (design D^mu, finite I, F infinite)
(E1) mu-thin supports (relative to the fixed mu; such f exist for every mu; deleting the thin coordinates costs ~ y^{1+o(1)}, not
o(y^2)); Y3 Theorem 3.5 / Y3_ref Prop 3.4 cover only d-neutral monochromatic pieces of it.
(E2) (O4-box): infinitely many bad carriers (B infinite): bounded switching fails, the needed raise is scale-free.
(E3) non-d-neutral fixed data at raised rows ((SC) at f_y).
(E4) (ND') failure: a|_F in span{u_l|_F : l in B_np}; the value drift -kappa nu||e^# - e||^2/2 is second order but can collapse a
d-neutral block cone (so V3 Remark 3.5(d) is not routine); degenerate bad peaks with the swallowing sign (sgn w = +eps_l, and
B_F at degenerate peaks), excluded as in R1.
(E5) the finite-F core (A)-(D) of ADDENDUM 6 and its transport to infinite F (Section 5 gap: VP constants for growing L_0).
Density of NA((c_0,p),l_2^2) remains OPEN. Nothing found points to a counterexample.
