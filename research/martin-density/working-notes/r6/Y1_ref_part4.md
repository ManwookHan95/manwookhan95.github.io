# Y1 referee, part 4: transplant (Prop 5.2), Theorem E', master theorem, corollaries, sketch, residual

## 4.1 Lemma 5.1, 5.1' (fixed repair directions).  CORRECT.
(DR) carriers are exactly swallowed (class G with r^nat = 0, (C1) void on them); supp y_{l_R} \ F is finite with fixed rooms, so (C2) misses
it for l large; (C3) acts at s_m notin T(l) in the signature set of a peak; V(rho) vanishes on every (C1)-modified set (other carriers'
S^nat avoid T(l) ⊇ supp y_{l_R}); so u_{l_R}(zhat^#) = u_{l_R}(zhat), d-sums rescale exactly by A_m/A^#_m, zero cost persists.
Normalization d >= u(w)/Design(l) for l large. CORRECT.

## 4.2 Proposition 5.2 (transplant at a clean sub-window).  CORRECT (re-derived step by step).
Step 1: membership tau in Z_kappa(beta) implies V(tau) z^#-signed and supported in K^# at every j notin F: on S^nat_{l''} (l'' in G,
closed, z^# = eps), on T(l) \ F (rows), elsewhere G-vectors vanish; donors (in P) have tau = 0. Violations: (Z1) Lemma 3.2; (Z2)
(z^# L_j(tau))_- <= phi_{z_j}(Delta B(j)) + |e_0(j)| at contacts (incl. (C2)-raised ones: phi_z(x) = |x|(1+|z|) for sgn x = -sgn z), and
|L_j| <= phi/u + |e_0| at free target coordinates; (Z3) Lemmas 3.5, 3.6; (Z4) none (|tau| <= 6 lambda/t < beta). Hoffman (1952):
dist <= H(A) ||(A tau - b)_+|| for every b with nonempty polyhedron, H depends on the matrix only; the matrix of kappa^# has design entries
u_l(j); kappa^# is a generalized configuration of level l. CORRECT.
Step 2: |sum_{G,m} q tau| from eq:didentity; P-part <= l K_O t/C; q^# = (A/A^#) q + O((|T|+1) b)/A^# on kept carriers. CORRECT.
Step 3: block-diagonal exact repair; in one-signed blocks tau_0 = 0 on Sigma (in P), so sgn Q^# in {0, -sigma} under (NN_w). CORRECT.
Repairs of block m' add mass to carriers of other blocks only with zero d-sum there (exact at f^#). CORRECT.
Step 4: budget at f^#: raised (C1)/(C2) coordinates phi_{z^#} <= 2 phi_z; flipped (C1) coordinates (v-mass <= r^nat <= b) and s_m:
phi_{z^#} <= 2|x|, bounded via phicalc(b) by |Delta B| + budget; sum_flipped |Delta B| <= 6b sum lambda/t + 4b^2/t <= t^3. CORRECT.
Step 5: data; the shift trick (Z6-ref 2.1): with P := vs omega^+(k) <= 1.5 gap/t, Q := vs omega^-(k) = P + tau'/lambda (swallowing type),
vs x := (-1.5 gap^#/t - Q)_+, lambda|x| <= |tau - tau'| + lambda|Delta d| M + 1.5 lambda (gap - gap^#)_+/t (the last term O(b/t), harmless).
Size bound A_2 = 22: unshifted |omega^-| <= 4/t + 12/t + 1/t; shifted |omega^+| <= 1.5/t + 13/t. CORRECT.
(iii) kinds: (K2) gap^# >= M^# u/2 >= gamma(w); (K3) gap^# ~ M; (K1),(K4) kind [3] (Z6-ref Lemma 2.1 allows vs omega <= 1.5 gap/t on side +,
c_flat <= min(1/3, 1/(4A'))). CORRECT.
Constants: K_U <= C_f G** l D^5 Design u^{-3}, K_w <= C_f (1+G**)(K_U + K_P + 1) <= C_f Design^2 u^{-3} (Design = X^6, X >= l D G**).
The claimed Design^3 u^{-3} is a valid (weaker) bound. CORRECT.
Remark (PROVED, small improvement): the condition gap >= t^2 in kind [1] is never used in the proofs of lem:uniformtransfer /
lem:onesidedtransfer (only |omega(k)| <= 2 gap(k)/t, i.e. coordinatewise radius >= t/2, is used); it is part of the window-certificate
definition only. So "kind [1']": any gap > 0 with |omega(k)| <= 2 gap(k)/t, is admissible in Lemma U. (Used in 4.6.)

## 4.3 Theorem E' (window-dependent constants).  CORRECT.
c_flat(j) = min(c^0_flat, gamma(w_j)/(2A_2), 1/(4A')); t_1 constraints monotone in c_flat; j_0 depends only on f_j -> f (Lemma persistence);
c_flat enters Theorem E only via (A), I_r, Q = 2 rho^2 K/(c_flat n) and eps_j < theta_j rho^2 r^2/c_flat^2. Same as Y2 Theorem E'
(confirmed by the Y2 referee).

## 4.4 Master Theorem 5.4.  CORRECT (with the precisions m2, m3).
Arithmetic re-done: K_w T_hi(w) <= C_f Design^3 u^{-3} 2^{-l^3}/(l Q) = C_f u^{omega+5} 2^{-l^3}/(l Design) -> 0;
n(w) c_flat/K_w >= l 2^{l^3} Q c u/(C_f Design^3 u^{-3}) = (l 2^{l^3} Design c/C_f) u^{-omega-4} -> infinity;
eps_j <= C_f T_lo^3 log(1/T_lo) and T_lo <= 2^{-n(w)} <= 2^{-u^{-8}}, so eps_j/(c_flat^2 T_lo^2) <= C_f T_lo log(1/T_lo)/u^2 -> 0.
Every f-constant C_f is independent of l, w, t (checked: N, q_0, nu, sigma_m, C_m, M_m, theta_m, A_m, C_F, transfer data, the finitely many
donors and repair directions, l_f thresholds). Quantifiers: D_X before f; w_j and f_j = f^#_{w_j} depend on f only; data on (g, rho, t);
Corollary D1 is applied at each fixed f_j to the averaged mate. CORRECT.
Precision: "No condition is placed on any room, margin, gap, d-coefficient" is true for the growth/rate conditions; (Cmp_w) and (NN_w) are
structural conditions involving SIGNS of d-coefficients of nearly neutral carriers and the existence of repair directions.

## 4.5 Corollaries.
M1 (maximal contact): CORRECT. (C1), (C2) void; (C3) only moves donors; q^# = q A/A^# exactly for non-donor coarse carriers; (SP_w) from Z4
Lemma 5.0 (fixed non-degenerate peaks of both signs, margins >= q_0/4); donors = anti-type non-degenerate peaks with S_c ∩ F = {}.
Note: at maximal contact a block can be one-signed at infinitely many levels only if it has NO anti-type strict non-peak with w != 0
(a fixed such carrier eventually has robust rho), and then sigma = +1.
M2: CORRECT with precision (m4): the exactly swallowed anti-type peak must be NON-DEGENERATE with S_c ∩ F = {} to be a donor (a degenerate
one is still an UPPER source); and "(DR) nonzero in both signs" is genuinely stronger than Z4's (DR) (which allows the vacuous alternative;
cf. the Y2 referee's G1). Reading M2 as "Z4 Theorem A'' without (H3), (W_inf)" is accurate only with these provisos.
M3: as a statement "Theorem 5.4 needs none of the growth conditions" CORRECT; but Theorem 5.4's scope is narrower than Z6 Theorem U' in one
respect: RIGID non-one-signed blocks (Z6) are in Y1's residual (m), while U' covers them under its rate (W_U') (U' survives for D_X, Theorem
1(d)). The open core is therefore the INTERSECTION of the complements (precision m6).

## 4.6 Sketch "tiny repairs by converted anti-type peaks" (Y1 5.6 Remark (3)).  Plausible SKETCH, with two additions.
(i) The converted carrier must lie in a block that is RAISED; in a one-signed block Y1 does not raise, so a donor (or pull, 4.7) is needed
there too (harmless: Sigma carriers near threshold are dropped and their status change is handled by Step 5).
(ii) The repair member has gap^# ~ M delta ~ T_lo^3 < t^2, so it is not of kind [1] as defined; by the Remark in 4.2 (kind [1']) the
one-sided expansion only needs |omega| <= 2 gap^#/t, and |omega| <= C l(|T|+1) b D^2/t << T_lo^3/t. Zero cost at f^# (resonance) remains a
hypothesis. With (i), (ii) the bookkeeping is routine. SKETCH.

## 4.7 Residual (n) and (d) versus far pulls (Y4 referee, Round 6, C.2-C.8; not yet refereed)
Y1 writes that removing (n) "needs LOWERING a z-signed functional (impossible with banks ..., with supp a fixed only |F| - 1 Hilbert
directions)". The statement about banks is right, but lowering is NOT impossible: the far pull (a sign-flipped far contact j in S^nat_{l''}
carrying a tiny support mass, Round 2: P1 6.3, P2A, N2) lowers eps u_{l''}(zhat) by 2 v_{l''}(j) with cross effects O(mu ||U^* e_j^*||);
the Y4 referee proves Lemma U / Theorem E with pulled and banked supports (no flip from t|b(j)| <= |a(j)|) and exact two-sided per-carrier
tuning for a diagonal base U (Prop. P4). Combined with Y1 (SKETCH, my outline): at a clean w, after (C1)-(C3), tune every kept K3 carrier
of every one-signed block to val^# = 0 EXACTLY (|x| <= C_f (|T(l)|+1) b(w); pulls at j ~ log2(1/b) > sigma(l) > s_max(l), banks at
min(S_{l''} \ (F ∪ [1, s_max(l)]))); then Q^#_m(tau_0) = 0 in one-signed blocks and (NN_w) is not needed; cost o(T_lo^2) and status
perturbations O(|x|^2) << b. Design additions: bounded gaps of the S_l (2^{G_l}) and 1/s_{sigma(l)}^2 (diagonal U) in Design(l).
Likewise a weak/degenerate swallowing-type kept peak can be pushed below threshold by a pull on its own (closed) signature set, which would
replace the donor (Do_w) (Y4-ref C.8(ii); SKETCH). So (n) and (d) are residuals of Y1's move class, not intrinsic directional obstructions;
the assembly is a SKETCH pending refereeing of Y4-ref C.2-C.7 (and is proved there only for a diagonal base U).
