# K1 referee notes (Round 11): proofs of the corrections and precisions to r11/K1_notes.md

Setting and notation of r11/K1_notes.md (design T_fin^* of Q1 over mu*_s = 2^{-2^{2^s}}, option (a); N >= 1; f in S_{p_N*} with base support F
arbitrary; g in C(f); rho in (0,1); a clean sub-window w = (L, i) of a main stage L; T := T_lo(w), b := b(w), u := u(w), D := D(L)).  Part files:
r11/K1_ref_part1.md (Section 1 of K1), K1_ref_part2.md (Section 2), K1_ref_part3.md (Sections 3-4); scripts and outputs: r11/K1_ref_work/.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Items R-1 ... R-14 are the referee's.

## A. Verdict table
| K1 claim (K1 label) | Verdict | Item |
|---|---|---|
| Lemma K1.1: route V needs no cube (PROVED) | correct | Gamma error is K_data t (notation) |
| Remark K1.1' (HEURISTIC) | label honest | -- |
| Deep raise, J(w), (a) of E^{eng,RT,inf}, no |g_j| term (PROVED) | correct | R-1, R-2 notational |
| Lemma K1.2 (PROVED) | correct with a constant slip | R-3 |
| Lemma K1.3 (PROVED) | correct (with R-3) | -- |
| Proposition K1.A, C_+ = 5 (PROVED) | correct | R-4 notation, R-5 |
| Corollary K1.B (PROVED) | INCOMPLETE: theta'/c_flat^2 -> 0 not checked; fails with K1's x_max | R-6 (fixed) |
| Lemma K1.4 (PROVED) | correct for (P1)-(P5) | -- |
| (C2): Q2-refa C.3 bank-with-offset is one-sided (FALSE claim of Q2-refa) | K1 correct; confirmed by a nonlinear test | -- |
| Lever audit (PROVED) | correct as inventory; two omissions | R-7, R-8 |
| Sys-A, Sys-DC, definition of (LR) | Sys-A correct; Sys-DC needs R-7 for (P4)-type (P6); (LR) must include Step 0 | R-7, R-8 |
| Lemma K1.5 (PROVED) | (a), (b1), (c) correct; (b2) incomplete for (P4)-type (P6) | R-7 |
| Lemma K1.6 (PROVED) | correct up to R-6 (cost), R-8 (Step 0) | R-6, R-8 |
| Lemma K1.7 (PROVED) | (i) false as stated (type (M) missing); (ii) correct for (S') = (S) ∪ (M); (iii) overstated | R-10, R-11 |
| Lemma K1.S: Step B dispensable (PROVED) | correct | -- |
| Lemma K1.ST (PROVED) | correct (with R-8's enlarged (D1)) | -- |
| Theorem 5.1 (PROVED mod (D-K1), chain) | correct with fixable gaps R-6, R-7, R-8; PROVED after the fixes, mod (D-K1) and the chain | R-6-R-8 |
| Corollary K1.C (PROVED) | correct with precisions | R-12 |
| Characterization of non-(LR) (PROVED) | necessary condition correct after R-10; "iff" false for (U)-configurations | R-13 |
| Ratio trick (SKETCH) | SKETCH honest; needs |rt_l| >= u | R-14 |

## B. Section 1 items

R-1 (moduli under the deep raise; PROVED).  For s <= d(L) < J, a^r_s = a_s/lambda_r: the relative change is 1 - 1/lambda_r = O(2^{-J}), not O(mu*_J).
Tiny moduli stay <= b, robust ones stay >= u/lambda_r >= u/2; spreads rho_s/rho_{s'} and h = |A(s)|/(nu v_l(s)) are invariant under the common factor
(nu^r = ||U*(a + Delta a)||/lambda_r scales the same way); values and block data move by O(mu*_J) (z unchanged, ||e^r - e|| <= 16 mu*_J/nu).

R-2 (J(w); PROVED).  2^{2^{J(w) - 1}} < C log_2(1/(theta_w T^2)) + C log_2(Design(L)/(b^2 Phi_min(L))) <= C Design(L) log_2(1/T) because b is a design
power of T (b_U4 = (eta/C_L)^{N_L/2}/(1 + Lip C_*), eta = T^4/(L Design)); hence 2^{J(w)} <= max(2^{d(L)+1}, 2 log_2(C Design(L) log_2(1/T))) <= Design(L)
+ 2 log_2(C n(w)), the bound K1 uses.

R-3 (Lemma K1.2; PROVED).  Classes are read off the decomposition data x_dec (U1-ref 4.5).  For an active component, |x_dec,l| >= A_{i+1} K t = K_* A_i K t;
zeroing moves the vector by <= J A_i K t; the projection onto Gamma^#(kappa, a) (Hoffman constant H, row norms <= C) moves it by <= H(K t + C J A_i K t).
Hence |c_l - c^act_l| <= (HCJ + H + 1) A_i K t, which is <= |c^act_l|/5 if K_* >= 5(HCJ + H + 1) and <= |c_l|/5 if K_* >= 6(HCJ + H + 1).  With K1's
K_* >= 5(H J_Om + 2) the correct conclusion is the first one.  Lemma K1.3 (S) survives: |c^act_l| >= (5/6)|c_l| gives (P.2) since (5/6) 4 = 10/3 >= 16/5,
and |c_l| <= (6/5)|c^act_l| <= (3/2) C_q 2^J t/delta_min(L) < 2 C_q 2^J t/delta_min(L) <= K_*^2 K t/(4 D(L)).  Either restate K1.2 relative to |c^act_l|
or take K_* >= 6(C H J_Om + 2); nothing else changes.

R-4 (notation).  In Proposition K1.A(ii) "K t" in the l_1 bound must be K_data t (thresholds A_i <= K_*^{J+1} enter the zeroing error); the closeness bound
p*(g - g_t) <= K_data t is stated correctly.

R-5 ((P#1) at S-mass coordinates; PROVED).  Step-A S-mass steps are <= ||R|| rho_A <= Design^C eta'/u in value units, i.e. mass changes <= Design^{C+1} eta'/u
<< u <= |a_s|/2 (eta' = T^4/(L Design), T <= (u/(4 Design))^{20}); so |a^#_s| >= |a^r_s|/2 there.

R-6 (cost accounting against the window-dependent c_flat; GAP in Corollary K1.B and Theorem 5.1 Steps 4 and 7; FIX PROVED).
Requirement.  X2 Theorem E^eng (r9/X2_notes 4.1, (E-d)) and Q2-refa B.1: with c_flat = c_flat(j) depending on the window, (E-d) contains
theta'_j/c_flat(j)^2 -> 0, where theta'_j T_lo^2 bounds the companion cost plus UE's cost (the proof bounds eps''_j <= 2 theta'_j T_lo^2 <= 2 theta'_j
r^2/c_flat^2 for |r| > c_flat T_lo).  Q1 Theorem C^tr checks it (theta/c_flat^2 <= C_f T^2 log(1/T)/u^2); K1 does not.
Failure.  K1 allows pulls anywhere in Far_l(x) = {j in S_l : x <= v_l(j) <= x_max}, x_max := T^2/(L Design(L) |Lambda|), and lowers in-F pull coordinates
with |a^r_j| <= x_max.  The costs per carrier with pull depth v are: z-flip of the pull, C_f lambda_l v log(e/v) (Z3 Lemma 3.1, |u_l(delta)| = 2v);
lowering, <= 2(1 + ||U||)|a^r_j|; pull mass, 24 lambda_l v; compensating bank, mass <= 2 v nu/(mu_s^2 v_l(s)) <= 2 Design(L) nu v.  In the worst case
(only depths v ~ x_max pullable) the total is ~ C Design |Lambda| x_max log(1/T) = C T^2 log(1/T)/L.  Since log(1/T) >= n(w) >> L Design(L), this is not even
o(T^2); and for a clean sub-window with i >= 2, u = b(w^-) <= T_lo(w^-)^4/(L Design(L)), so already the lowering part alone gives theta'/c_flat^2 >=
2/(c_f^2 L Design u^2) -> infinity.  [Arithmetic illustration: K1_ref_work/ref_cost_ratio.py: log2(theta'/c_flat^2) ~ +8e3, +8e5, +8e7 at three design
scales.]
Fix (PROVED).  Put x'_max := u(w)^2 T^3/(Design(L)^2 |Lambda|) and take every pull at the smallest pullable depth in [x, x'_max].  Then the total far cost
is <= C Design(L) |Lambda| x'_max log(1/T) = C u^2 T^3 log(1/T)/Design(L) (log(e/v) <= 6 log(1/T) since v >= x_A >= T^5), so it adds <= C u^2 T log(1/T)
to theta' and theta'/c_flat^2 picks up <= C T log(1/T)/c_f^2 -> 0.  The other parts: deep raise eps'_r <= C_f T^4 log(1/T) (ratio C_f T^2 log(1/T)/(c_f u)^2
-> 0); Step-A moves <= C_f Design^C eta' log(1/eta')/u (ratio <= Design^C T^2 log(1/T)/u^3 -> 0); UE's K_w Pi log(e/Pi) <= exp(C log^2(1/T)) e^{-1/(2T)}.
Hence (E-d)'s third condition holds along the main stages.  The window stays wide: x'_max/x_A = L u^2/(C Design^3 |Lambda| T) >= 2^{6G(L)} (T <= (u/(4Design))^{20}),
and the DC window [r, 2^{3G} r] (r <= K_w s_1) lies far below.  Pullability and super-thickness are re-defined with x'_max (a window quantity: no design
change).  This only enlarges the (U)-class; no other statement of K1 is affected.

## C. Section 2 items

R-7 ((P6) by an S-mass lever on the peak; K1's "verbatim" claim FALSE; correct scalars PROVED).
Let the block-norm resource of block m* be an S-mass step at a thick near coordinate s of the robust peak k* (h0 := |A(s)|/(nu |u_{k*}(s)|) = O(Design/u),
not small).  Its column in the DC linearization is -(pi p_{m*} + h0 g) (private action on A_{m*} plus the common mode on every Omega carrier; with the
block-norm terms g is Q2's gt).  Q2-refa C.3(iv)'s rank-one perturbation argument requires h0 ||g||_inf K <= 1/2 and does not apply.
Proposition R-7.  With L(P, P_0) := D P - g h^T P - sum_m p_m q_m^T P - (pi p_{m*} + h0 g) P_0 (D = I + X, q_m^T X = 0, q_m^T p_m <= 1/2, blocks disjoint)
put c'_alpha := c_alpha + (h0/pi) q_{m*}^T D^{-1} g and beta'_* := beta_* + (h0/pi)(1 - q_{m*}^T p_{m*}) (c_alpha, beta_* of Q2 Prop. 4.1).  If
max(|c'_alpha|, |beta'_*|) >= beta_0 > 0, every b has a preimage linear in b with ||P||_inf + |P_0| <= K' ||b||_inf, K' := Q2's K with H replaced by
H + |h0|/|pi|.  If N := D - g h^T - sum p_m q_m^T is singular with one block and c'_alpha = beta'_* = 0, L is not onto.
Proof.  Seek P = D^{-1}(b + g alpha + sum_m p_m gamma_m) with alpha := h^T P + h0 P_0, gamma_m := q_m^T P (m != m*), gamma_{m*} := q_{m*}^T P + pi P_0; then
D P - g alpha - sum_m p_m gamma_m = b is exactly L(P, P_0) = b.  Consistency: for m != m*, gamma_m = [q_m^T D^{-1} b + (q_m^T D^{-1} g) alpha]/(1 - q_m^T p_m)
(as in Prop. 4.1, using q_m^T D^{-1} p_{m'} = delta_{mm'} q_m^T p_m); the m* equation gives P_0 = [(1 - q_*^T p_*) gamma_* - q_*^T D^{-1} b - (q_*^T D^{-1} g)
alpha]/pi; the h-equation h^T P = alpha - h0 P_0 becomes, after substitution, c'_alpha alpha - beta'_* gamma_* = rhs - (h0/pi) q_*^T D^{-1} b with Q2's rhs.
Choose alpha := 0 if |beta'_*| >= beta_0, gamma_* := 0 otherwise; the bounds follow as in Prop. 4.1.  Converse (one block, N singular): det N/det D =
(1 - q^T p) c_alpha - (q^T D^{-1} g) beta_* = 0 gives c'_alpha = (q^T D^{-1} g/(1 - q^T p)) beta'_*, and with both zero the scalar equation reads
0 = rhs - (h0/pi) q^T D^{-1} b, a nontrivial linear condition on b.  QED
Numerics (K1_ref_work/ref_p4_peak_scalars.py, ref_bordered.py Part B): residual of the explicit inverse 3.0e-15 (3000 multi-block instances); 2797/2797
exactly degenerate one-block systems with robust Q2 scalar (s_min[N | -pi p] >= 1.4e-2) become non-onto for the (P4)-type column at h0 = -pi beta_*/(1 - q^T p)
(median |h0| = 0.66).  Remark (PROVED): in Q2's doubly degenerate case c_alpha = beta_* = 0, a (P4) peak lever with h0 != 0 has beta'_* != 0 and borders N
(1577/1577 instances) -- but in the exact full degeneracy with kappa != 0 peaks have no thick near coordinates (Q2 Lemma 4.3(c), Q2-refa C.4(2)).
Fix: put c'_alpha, beta'_* (for the finitely many lever assignments of level L) into (R-lev) and use them in Lemma K1.5(b2) for (P4)-type (P6); private
(P6) ((P1), TU, (P3) on the peak) keep Q2's c_alpha, beta_*.

R-8 (Step 0's weak-peak pushes; GAP in the definition of (LR) and in Theorem 5.1; FIX).
In (T)-blocks Step 0 of KN^tr pushes every active weak peak k (rho in [1, 1 + b]) to rho = 1 - b, a value change <= 2b theta Phi_k/m, BEFORE the Lojasiewicz
step.  The push lowers vs_k val_k.  The peak carries data with sign eps_k = -sgn(Delta''_m) vs_k, so a near bank (which raises eps_k val_k) performs the push
iff Delta''_m > 0; for Delta''_m < 0 a pull at depth ~ 2b theta Phi/m, (P3) or (P4) is needed.  The (LR) of K1 2.4 concerns only Sys-A and Sys-DC, which are
set up after Step 0; so Theorem 5.1's hypothesis does not guarantee that Step 0 can be performed.  Moreover a (P4) push moves every value by the common
mode h * 2b theta Phi/m <= C Design b/u, hence every rate object by <= Design^C b/u, more than the radius (1 + Lip C_*) b that (D1) provides for the
Lojasiewicz step.  Fix: (i) add to (LR_{w,a}): "every active weak peak of a (T)-block has a push resource: a pullable far coordinate at depth in
[2b theta Phi/m, x'_max], (P3), (P4), or a near bank if Delta''_m > 0"; (ii) replace (D1) by C_L((1 + Lip C_*) Design(L)^C b/u(w))^{2/N_L} <= eta'(w)/3
in the definition of b_X1(w) (legitimate: u(w) = b(w^-) is fixed before b(w); left side increasing in b, so the admissible b still form an interval
(0, b_X1(w)]); robust objects survive since Design^C b/u << u (b <= T^4 << u^2).  With (i)-(ii) Lemma K1.6(A) and K1.ST hold.  Since a weak peak without
any push resource is, after a hypothetical push, a (U)-type tuned carrier, the non-lever-regular class only gains these peaks.

R-9 (= R-7, recorded in the audit table).

R-10 (Lemma K1.7(i): the missing type (M); PROVED).  A tuned carrier l without (P1), (P2), (P3) is one of: (S) N_l ⊂ F_thick with all spreads tiny; (U) data-
carrying, N_l ∩ F_thick = {} and no pullable far coordinate; (M) data-carrying, N_l contains an off-F/thin coordinate AND a thick one (no robust-spread
thick pair), no pullable far coordinate.  [Proof: if N_l contains an off-F/thin coordinate and l is zero-data, (P1) holds; if l is data-carrying with a
pullable far coordinate, (P2) holds; the rest is the case split on N_l ∩ F_thick.]  (M) has (P4) as its only two-sided resource, like (S); put (S') := (S) ∪ (M).
Lemma K1.5(b) and K1.7(ii) apply to (S') verbatim (they use only the (P4) column).  The statements of K1.7(i), 4.3 and the Characterization must read
"(U) or (S')".

R-11 (Lemma K1.7(iii): exact limit; overstated; corrected version PROVED).  A support move at s in F changes y^T(values) by (mu_s^2 A(s)/nu)[u_h(s) - kappa a_s],
kappa := <U* u_h, e>/nu.  "No usable resource" constrains only USABLE coordinates: thick s in F ∩ [1, d(L)] (thin s: effect proportional to A(s) <= b;
s > d(L): efficiency mu*_s^2 v negligible).  Exact vanishing therefore gives u_h(s) = kappa a_s for s in F_thick ∩ [1, d(L)] only; if kappa != 0 then
F_thick ∩ [1, d(L)] ⊂ supp u_h ("no anchor") and a_s = (h_l eps_l/kappa) v_l(s) on F_thick ∩ N_l.  P_F(I - e e^T)U* u_h = 0 on all of F, Q2 Lemma 4.3(b) and
U2 Lemma ND's conclusions on all of F do not follow.

## D. Sections 3-4 items

Lemma K1.S (CORRECT; re-derivation).  (U5) enters Theorem UE only via Lemma UE-1(e): S_m := ||D_m(w'_m - w^0_m)||^2 + sum_{k in A_m}(Phi_k^2 + lambda_k(|w'_m(k)
- w^0_m(k)| + (C'_m - C^0_m)_+)).  Coarse carriers are not scrambled once 2K_* Pi <= x_0(w) (margins u/2, gaps g_min at f^#, moves <= K_w Pi); fine carriers
contribute <= sum_{k > L, m(k) = m} (Phi_k + 3 m Phi_k) <= 6m c_{L+1}.  With (W_exp) and s_1 >= exp(-1/(2T)): 6m c_{L+1} <= c_late delta s_1/4 for T small.
J_fine violations <= C_f Design c_{L+1}, with b^theta = 0 at free coordinates (chi = 1/2) and violation (zV)_- at contacts.  Lemma PM and UE-1(d) do
not use fine statuses.  So Step B (G1 release, static ownership, self-aligned negative fine carriers) is redundant in route V, at finite and infinite F.

Lemma K1.1 with Step B kept (for the record; CORRECT): U1 Lemma 4.1's rules use only sigma_m, eps_l and Y_k (a function of z), and U1 Lemma 4.2 (dominance)
is stated for every Delta'' and gamma of the class (active |Delta''_m|, |gamma_l| >= A_2 K T/2).

R-12 (Corollary K1.C; precisions).  (c): read "two THICK near coordinates with spread >= u" and "an off-F OR THIN near coordinate".  Example (2): the
"point beyond which F ∩ S_l has no three consecutive elements" must be <= s_max(L) for every l <= L at infinitely many L (e.g. "beyond s_max(l)"); otherwise
the carriers l close to L are not covered.  Example (1): rho_{s'}/rho_s = 2^{G_l}(s/s')^2 >= 2^{2^{l+1} - 2} for s >= 2^{l+1}, spread >= 3/4: correct.

R-13 (Characterization; the "iff" is false for (U)-configurations).  A (U)-carrier l in block m contributes a ratio row without a two-sided private column,
but a two-sided resource of a buffer peak c of block m has the column -(1 - X) lambda_c rt^{(m)} (entries -(1 - X) lambda_c rt_l on the rows of block m) and
acts on l with efficiency (1 - X) lambda_c |rt_l|; with one (U)-carrier per block, robust |rt_l| and the other carriers private, J_A restricted to the
columns {private} ∪ {s_c} is square and block-triangular with diagonal entries 1 resp. -(1 - X)lambda_c rt_l, hence has a right inverse of norm
<= Design^C/u: (LR) holds.  So "some tuned carrier is (U)" does not imply non-(LR).  Correct statement: non-(LR) at all large stages implies the (U)/(S')
description (necessary condition); for (S')-only configurations it is also sufficient (all bordered scalars <= b and no anchor give a left vector y = h
(Sys-A) or D^{-T}(h + ...) (Sys-DC) with |y^T J| <= C b ||h||, so the minimal right inverse has norm >= 1/(C b ||h||) and rho_lev << u/Design^{C_0}).

R-14 (ratio trick; SKETCH stays).  The linear step needs |rt_l| >= u for the (U)-carriers of the block (else d kappa = kappa max(-delta_l/rt_l) is not
small), the other carriers of the block two-sided, a two-sided buffer-peak resource, a nonlinear degree argument on the cone of admissible bank
parameters, and the Sys-DC analogue (A_m through a block-norm lever in place of kappa).  Note also R-13: with one (U)-carrier per block and robust |rt_l|
no sign condition is needed at all (the peak resource is two-sided); the sign condition matters only when a block has several (U)-carriers with
different required corrections.

## E. Theorem 5.1 after the fixes (statement the referee accepts as PROVED modulo the cited chain and (D-K1) = item (O-d))
Let T_fin^* carry, in addition to K1's (D-K1) objects, the scalars c'_alpha, beta'_* of R-7 in (R-lev) and the enlarged (D1) of R-8.  Let N >= 1, f in
S_{p_N*} (F arbitrary), g in C(f), rho in (0,1).  Suppose that for infinitely many main stages L, at a clean sub-window w(L) and a class a(L) with
>= n(w)/D_cl(w) scales: (i) every active weak peak of a (T)-block has a push resource (R-8); (ii) Sys-A and Sys-DC, with pullability and super-thickness
defined with x'_max (R-6) and (P4)-type block-norm levers bordered by (c'_alpha, beta'_*) (R-7), have right inverses of norm <= Design(L)^{C_0}/u(w).
Then (f, rho g) lies in the closure of NA((c_0, p_N), l_2^2) along norm-attaining rows with finite base support; in particular (LSC-trunc)_N holds at
(f, g, rho).  Proof: K1 4.1 Steps 1-7 with R-3 (classes), R-6 (cost; (E-d) third condition checked in B), R-7 (Lemma DC^inf), R-8 (Step 0).
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2): OPEN.

## F. Numerics (sanity only; r11/K1_ref_work/)
 rerun_offset_check.out, rerun_deep_assign_check.out: K1's scripts re-run, outputs identical.
 ref_offset_nonlinear.py/.out: one-sided bank with quadratic remainder, SLSQP: min ||F||^2 >= 0.52 (y^T F_0)^2 in all 23 instances with negative forced
   position; two-sided control <= 4.5e-13.  Confirms K1's (C2).
 ref_deep_assign.py/.out: exact rational check of the deep assignment with trace slack and of the F_low split bound, 60000 instances incl. boundary cases:
   0 violations.
 ref_bordered.py/.out: Part A (Sys-A bordering, exact degeneracy 1 - h^T g~ = 0): identity h^T col = -[(1-X) lambda h^T rt + h_c] to 4e-14, explicit right
   inverse residual 1.8e-12; Part B: (P4)-type block-norm column fails in 2797/2797 degenerate instances with robust Q2 scalar (R-7).
 ref_p4_peak_scalars.py/.out: Proposition R-7's explicit inverse (residual 3e-15); doubly degenerate Q2 case bordered by a (P4) peak lever (1577/1577).
 ref_cost_ratio.py/.out: R-6 arithmetic in log2 scale.
