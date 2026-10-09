# Y3 referee, part 2: Section 3 (D_sigma, Theorem 3.5, Remark 3.6(b), critical case 3.5)

## Proposition 3.3 (design D_sigma): CORRECT (PROVED).
(D1)(c) only removes allowed targets and depends only on l and the fixed sets S_l'; every finitely supported y^(i) satisfies (c)
once l >= max supp y^(i), so (T-d) holds as in thm:SLD; (T-a)-(T-c), (P1)-(P3) use only (a), (b), c_{l+1} <= c_l/4. The bounded-gap
choice S_l = {2^l(2i+1) : i >= 1} \ {j_0} is a legitimate instance of (D0) (pairwise disjoint, infinite, j_0 excluded; gap of S_l is
2^{l+1}, bounded for each l). The derived designs (SLD_G, D''', explosive D1^F) keep (D0) and allowedness and only add recursive
conditions on windows/constants computed from the actual y_l; (c) is one more condition fixed before T_hi(l). N-independence: (c)
does not involve N.

## Theorem 3.5 (super-critical support swallowing): CORRECT (PROVED), modulo the summary-table phrasing.
Checked line by line against R1 (Z5_ref_notes Section 2) and Z5 Step 2:
- Step 2: for l in B_sc, tau_l enters no row of Z_f (target rows only at j in T_0 \ F, where u_l = 0 by (i); no sign row since
  S_l \ F is empty, l in B_F; no peak row; d-row coefficient q_l = 0 by (ii)); Hoffman's right-hand side does not involve B_sc
  either, so the projection acts on the other coordinates and tau'_l := tau_l on B_sc is legitimate.
- Step 2': Z5 Lemma 5.2 (bounded free switching at any F) gives |tau_l| <= C_U(1 + K* t) for all l in B.
- Claim A: re-derived (d_j <= 0 off the finite set T_sc because s_j = eps_l and u_l = v_l >= 0 on the deep part of S_l; on T_sc,
  |d_j| <= C_tau|B| <= |a_j|/t for t <= t_sc; T_sc subset supp u_l subset F so a_j != 0 there).
- Claim B: re-derived (on S_l cap F deep, outside finitely many target coordinates of other bad carriers, s_j Xt_j = (tau'_l)_+ v_l(j) >= 0).
- (a) representation: Xt = sum_{B_np} eps_l tau~_l u_l (bad peaks have tau' = 0, B_sc subset B_np), d(omega^-) - d(omega^+) =
  sum q_l tau~_l = sum q_l tau'_l = 0.
- (d) decomposition (b^-, omega^-) = Q + sum_{B_sc} P_l(-eps_l(tau'_l)_-): base b^+ - X - sum eps(tau')_- u_l = b^+ - Xt (since
  X - Xt = -sum_{B_sc} eps(tau')_- u_l), block omega^+ + sum (eps tau'/lambda) e + sum (eps (tau')_-/lambda) e = omega^-. Correct.
- Step 5 uses Lemma 3.4(c) for each l in B_sc separately; (D1)(c) makes the remainder r(s) on S_l(deep) come only from l' > l_*.
- Step 5 uses Theorem 2.1 (no condition on |bbar^theta|): correct and necessary (|b^theta| ~ (tau'_l)_+ v_l/2 on S_l deep is not sparse).
Minor: the summary table (row 5) and Remark 3.6(a) state "with R1 the model |a_j| ~ v_l(j)^{1+b} is settled for every b except
b = 1"; this needs the qualifiers of B_sc for b > 1: supp u_l subset F (or the corrected relaxation below), w(k(l)) = 0, a
monochromatic on S_l, (QM), design D_sigma, plus (W*), (H2), (H3-inf), (B_fin). R1 (b < 1) needs none of the carrier qualifiers.

## Remark 3.6(b) (relaxing supp u_l subset F): SKETCH WITH A SIGN ERROR AND A GENUINE GAP; corrected version below.
Computation (one bad carrier l in B_sc, eps := eps_l, a target coordinate j notin F of l, no other bad carrier at j). The constrained
switching (tau_l = -D < 0) gives Delta B(j) = -eps D y_l(j)/n_l, so phi_{z_j}(Delta B(j)) = (D/n_l)(|y_l(j)| + z_j eps y_l(j)).
 (alpha) |z_j| < 1: both directions of tau_l are pinned at O(t) by the switching budget at j; the row L_j(tau) = 0 of Z_f forces
         tau'_l = 0. Harmless.
 (beta) z_j eps y_l(j) > 0: the CONSTRAINED direction is pinned (O(t)); the row z_j L_j >= 0 forces tau'_l >= 0; no un-switching needed.
 (gamma) z_j eps y_l(j) < 0: the contact j absorbs the constrained direction for free, and the FREE direction is pinned (row forces
         tau'_l <= 0). Un-switching on the - side alone (Y3's prescription) puts -eps(tau')_- y_l(j)/n_l into the - base at j; with
         R1's split b^+_j = chi_j V'(j) the - base at j becomes -chi_j eps D y_l(j)/n_l, whose z_j-component is
         chi_j D|z_j eps y_l(j)|/n_l >= 0: NOT side-- admissible unless chi_j = 0.
So Y3's case split is reversed: the case Y3 calls "un-switching admissible" (z_j eps y_l(j) < 0) is exactly the case where one-sided
un-switching is inadmissible whenever the + decomposition uses the contact (chi_j > 0).
Repair (PROVED, single target contact): in case (gamma) un-switch on BOTH sides: + pair := (R1 + pair) + P_l(eps chi_j D'), - pair :=
(+ pair) - (switching without l), D' := (tau'_l)_-. Then b^+_j = b^-_j = O(t) (set them to 0 at O(t) cost); the - pair equals
(B_-, Theta_-) + P_l(-eps(1 - chi_j)D') + O(t); Gamma costs C_un chi_j D' and C_un(1 - chi_j)D', both -> 0 on windows by Lemma 3.4(c).
On S_l(deep) both bases must take a common value in [-A_s, A_s]; projecting x_s + chi_j D v_l(s) (x_s := s B_+(s)) onto [-A_s, A_s]
costs at most f^+_s + f^-_s + |r(s)| per coordinate (because x_s >= -|a_s|/t - f^+_s and x_s <= |a_s|/t + f^-_s - D v_l(s) + |r(s)|),
i.e. O(t) in l_1. So (i) may be relaxed to: every target coordinate of l off F is shared with no other bad carrier, and at most ONE of
them is a contact of type (gamma).
Obstruction (PROVED, as a statement about exact cushion-compatible data): if l has two type-(gamma) target contacts j_1, j_2, then any
two-piece data whose l-switching coefficient K is >= 0 (necessary for (CS-side) on a non-sparse S_l, see below) must have
b^+_{j_i} = b^-_{j_i} = 0 (from z_j(b^+_j - b^-_j) = K z_j eps y_l(j)/n_l <= 0 <= z_j b^+_j - z_j b^-_j), and a + pair O(t)-close to
(B_+, Theta_+) + P_l(c) has b^+_{j_i} = (c eps - chi_{j_i} D) eps y_l(j_i)/n_l + O(t); both vanish only if |chi_{j_1} - chi_{j_2}| D = O(t).
Necessity of K >= 0: (s b^+)_- + (s b^-)_+ >= -K v_l(s) on S_l(deep), so K < 0 forces anti-sign parts >= |K| v_l(s)/2 on
{rho_l(s) < |K| t/(4C)}, which is not cushion-sparse when m_l is not o(y). Hence with several type-(gamma) contacts whose + fractions
differ by >> t/D, the un-switching method has no exact data (not a non-recovery claim).

## Section 3.5(i) ("methods fail at critical profiles"): ARITHMETIC CORRECT, LABEL OVERCLAIMED (should be HEURISTIC/arithmetic).
PROVED part: if 0 < kappa_- <= m(y)/y <= kappa_+ < infinity for small y, then D^#(t) lies between 2 sqrt(C_Q/(kappa_+ q_0)) and
2 sqrt(2C_Q(1 + 32 q_0 t)/(kappa_- q_0)) for small t (direct from the definition). This bounds what Lemma 3.4 can GUARANTEE; it does
not show that the actual constrained amplitude D(t) of any mate stays positive, nor that the listed methods fail for a given mate;
the costs quoted for raised companions (~ T_hi^2) and deep assignment are the costs of the specific constructions.
New quantitative refinement (model computation; Y3_ref_work/critical_factor2.py): in the critical model (b = 1, S = N, v = c_0 2^{-s},
|a_s| = 2^{-2s}; then m(2y) = 2m(y) exactly) the deep-assigned fixed data built at scale t pay at every scale r << t a flip excess
Fdata(r) with sup_r [Fdata(r)/r^2]/[Fdec(t)/t^2] = 2.000 at every t, where Fdec(t) = sum 2(tDv - 2|a|)_+ is the MINIMAL flip excess of
any decomposition with constrained amplitude D at scale t. Reason: at its own scale the decomposition uses the cushions |a|/t of BOTH
sides (threshold 2|a|), fixed data at a smaller scale r can only use one side's cushion |a|/r (threshold |a|). Exactly: Fdec(t) =
2 Exc_{Dv}(t/2), Fdata(r) -> Exc_{Dv}(r) for r << t, and m(2y) = 2m(y) gives Exc_{Dv}(2r) = 4 Exc_{Dv}(r), so along r = 2^{-k}t
[Fdata(r)/r^2]/[Fdec(t)/t^2] -> Exc(t)/(2 Exc(t/2)) = 2. (b = 0.5: ratio -> 0; b = 1.5: ratio unbounded.)
Consequence (HEURISTIC, worst case of a tight mate whose decomposition puts all flips on one side): the data coefficient
Gamma_w(data) + Fl(data) can exceed the budget 1 by the full flip share Phi_t = 2q_0 Fdec(t)/t^2 ~ q_0 kappa D^2, at EVERY window scale;
selecting "upper points" of the log-periodic profile (Y3 3.5(ii), worst-scale principle) cannot remove this factor 2. A fixed split
theta of the deep usage between the sides helps only if the decomposition itself splits evenly (max(c_+, c_-) <= 1 forces theta =
theta_dec = 1/2 in the self-similar model). So Y3 3.5(ii) is not merely unproved: in the exact self-similar model its premise fails.
