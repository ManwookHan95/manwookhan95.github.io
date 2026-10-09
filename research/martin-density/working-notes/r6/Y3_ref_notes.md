# Y3 referee notes (Round 6): proofs of fixes and additions

Notation: the note paper/martin_density_note.tex ("the note"), r6/Y3_notes.md ("Y3"), r5/Z5_ref_notes.md ("R1", "R2" = its Theorem R1
and Lemma R2). I finite; f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu); s_j := sgn a_j on F; for a two-sided
decomposition (B_pm, Theta_pm) at scale t: f^+_j := (-s_jB_+(j) - |a_j|/t)_+, f^-_j := (s_jB_-(j) - |a_j|/t)_+, sum_F f^pm_j <= t/(4q_0)
(lem:flip, every F). P_l(c) := (c u_l, -(c/lambda_l)e_{k(l)} in block m(l)) is Y3's un-switching pair (Y3 Lemma 3.1).
Part files: r6/Y3_ref_part1..3.md. Script: r6/Y3_ref_work/critical_factor2.py. Labels: PROVED / SKETCH / HEURISTIC / OPEN / FALSE.

## 1. Small corrections (PROVED)

1.1 Lemma 4.3 holds for 0 < r <= 1/(1 + 3C_a) (not for every r > 0 as stated). Proof: Y3's argument with t := (1 + 3C_a)r <= 1, where
Lemma suplevel(e) gives |t Theta_+(k)| <= 1 + s(1) < 3 (it needs N(w + t Theta) <= s(t) <= s(1), i.e. t <= 1). Only r -> 0 is used.

1.2 Theorem 5.1, Step 4: for a general admissible T, sum_{k,m} lambda_{k,m} <= sum_{m <= N} m 2^{-m} < 2, so ||B_pm||_1 <= ||g||_1 + 6/t
(Y3 wrote 1/t, which is the SLD bound sum lambda <= 1/3). Only the existence of an f-constant A_0 matters.

1.3 Theorem 5.1, (W_M) may be weakened. In Step 1(a), for coarse peaks sigma|alpha(k)| = lambda_k mu_k gives
 sum_{coarse peaks k} lambda_k|omega_pm(k)| = sum (1/mu_k) sigma|alpha(k)||omega_pm(k)| <= (max_{coarse peaks} 1/mu_k)(t/2)
by Lemma suplevel(c). So M_f(L) can be replaced by M^max_f(L) := sum_{m in I} max{1/mu_{k,m} : (k,m) in C_L, k in P_m} <= M_f(L).

1.4 Lemma 3.4(a): the constant 32 can be 16 ((D/2)m^{>l_*}(tD/4) <= t/(2q_0) + (4/3)6t^2). Lemma 3.4(c): use D' := eta_1/2 < D^#(t_n)
(the admissible set {D' : D' m(tD'/(4C_Q)) <= ...} is an initial interval) to get the contradiction.

1.5 Theorem 2.2: the factor (1 + O(T_0 + s_1)) should be (1 + o(1)) along the construction sequence (q*(a'') -> 1, c -> 0); the extra
hypothesis rho^2 Gamma_w(b^theta, omega^theta) < 1 is implied by the main one (convexity of Gamma_w).

## 2. Relaxing supp u_l subset F in Theorem 3.5 (corrects Y3 Remark 3.6(b) and Y3_part1 Remark 1.10(c))

Setting: Theorem 3.5's hypotheses except that for l in B_sc only S_l subset F (up to finitely many points) is assumed, i.e. some target
coordinates j in supp y_l \ F are allowed. Let eps := eps_l (the sign of a on the deep part of S_l), D := (tau_l)_-, and for such j
put kappa_j := z_j eps y_l(j) (if |z_j| = 1).

2.1 Lemma (budget at a target coordinate; PROVED). Assume no other bad carrier has j in the support of its vector. Then
 phi_{z_j}(Delta B(j)) = (|tau_l|/n_l)(|y_l(j)| - sgn(tau_l) z_j eps y_l(j)) + O(e_j),  e_j := |(Delta B + Delta theta_l u_l)(j)|.
Hence: (alpha) if |z_j| < 1 both directions are pinned: (1 - |z_j|)|tau_l||y_l(j)| <= n_l(t/q_0 + e_j); (beta) if kappa_j > 0 the
constrained direction is pinned: 2(tau_l)_- kappa_j <= n_l(t/q_0 + 2e_j); (gamma) if kappa_j < 0 the free direction is pinned:
2(tau_l)_+ |kappa_j| <= n_l(t/q_0 + 2e_j), and the constrained direction is free at j.
Proof. Delta B(j) = -Delta theta_l u_l(j) + (rest) = eps tau_l y_l(j)/n_l + (rest), phi_z(x) = |x| - zx, Lemma phicalc(c) and
Lemma switchbudget (sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0). QED

2.2 Proposition (one-sided un-switching is inadmissible in case (gamma); PROVED). In case (gamma), with Y3's data (b^- := b^+ - Xt,
b^+ = chi V' off F, V' := X 1_{F^c}, Xt := X + eps(tau'_l)_- u_l), the - base at j equals -chi_j eps D' y_l(j)/n_l (D' := (tau'_l)_-),
whose z_j-component chi_j D'|kappa_j|/n_l is >= 0, so (b^-, omega^-) is side-- admissible at j only if chi_j D' = 0. In case (beta) the
- base gets a z-signed-negative term (admissible), but there D' = O(t) anyway.
Proof. With tau'_l = -D' (case (gamma) forces tau'_l <= 0 through the row z_j L_j(tau) >= 0 of Z_f), V'_j = X_j = -eps D' y_l(j)/n_l,
z_jV'_j = D'|kappa_j|/n_l > 0, Xt_j = 0, so b^-_j = b^+_j - Xt_j = chi_j V'_j = -chi_j eps D' y_l(j)/n_l. QED
So Y3's case split is reversed: one-sided un-switching is admissible exactly in case (beta), where it is not needed.

2.3 Proposition (two-sided un-switching; PROVED). Suppose every target coordinate of l in B_sc off F is shared with no other bad carrier
and at most one of them, j_*, is of type (gamma). Then Theorem 3.5 holds for f.
Proof (changes to Theorem 3.5's proof). Cases (alpha), (beta) at the other target coordinates: by 2.1 and the rows of Z_f they force
tau'_l = 0 resp. tau'_l >= 0 (Hoffman error O(K*t)); then D' = 0 and nothing changes. Case (gamma) at j_*: the row forces
tau'_l <= 0, so D' := (tau'_l)_- = (tau_l)_- + O(K*t) and Lemma 3.4(c) (which only uses S_l subset F up to finitely many points)
gives sup_{W(l_j)} D' -> 0. Let chi := chi_{j_*} in [0,1] (Lemma split) and c := eps chi D'. Data:
 + pair: R1's + pair + P_l(c), then on S_l(deep) replace the base value of s_s b^+(s) by the nearest point of [-A_s, A_s] (A_s := 2|a_s|/t),
   and put b^+_{j_*} := 0;
 - pair: the + pair minus the switching WITHOUT its l-part (so b^+ - b^- = Xt with Xt := X + eps D' u_l, which has no l-part).
(i) Closeness: P_l(c) represents 0. At j_*: B_+(j_*) = chi V'_{j_*} + e_+(j_*) and c y_l(j_*)/n_l = -chi V'_{j_*}, so setting b^+_{j_*} := 0
costs |e_+(j_*)|. On S_l(deep): x_s := s_s B_+(s) satisfies x_s >= -|a_s|/t - f^+_s and (from s_s B_-(s) <= |a_s|/t + f^-_s and
s_s Delta B(s) = -D v_l(s) - eps r(s)) x_s <= |a_s|/t + f^-_s - D v_l(s) + |r(s)|; hence x_s + chi D' v_l(s) lies within
f^+_s + f^-_s + |r(s)| + |D - D'| v_l(s) of [-A_s, A_s]. Summing: the + pair is within O(K*t) (l_1) of (B_+, Theta_+) + P_l(c).
(ii) Admissibility: b^+_{j_*} = b^-_{j_*} = 0; on S_l(deep) both bases equal a point of [-A_s, A_s] (cushion-compatible on both sides);
elsewhere R1's bounds. d-neutrality: q_l = 0 and the l-part of the switching is 0.
(iii) Gamma: + pair = (B_+, Theta_+) + P_l(c) + O(K*t); - pair = (B_-, Theta_-) + P_l(-eps(1 - chi)D') + O(K*t), because the l-part of
the true switching is (Delta B, Delta Theta)_l = P_l(-eps D) (Delta B_l = -Delta theta_l u_l = -eps D u_l, Delta Theta_l = eps D e_k/lambda_l).
By Lemma 3.1, sqrt(Gamma_w) <= sqrt(1 + eta_Gamma) + K t + C_un D' on both sides, and C_un D' -> 0 on the windows.
The rest (Lemma R2 with U_* := U_{B \ B_sc}, windows, averaging, Theorem 2.1) is unchanged. QED

2.4 Proposition (obstruction with two type-(gamma) contacts; PROVED as a statement about exact data). Let l (non-sparse: m_l(y) not
o(y)) have type-(gamma) target contacts j_1 != j_2 used by no other bad carrier. Let (b^pm, omega^pm) be two-piece data satisfying
(CS-side) whose + pair is within l_1-distance delta of (B_+, Theta_+) + P_l(c) for some c, and let K be the coefficient of u_l in
b^+ - b^-. Then K >= 0 and b^pm_{j_i} = 0, and consequently |chi_{j_1} - chi_{j_2}| D' <= n_l delta (1/|y_l(j_1)| + 1/|y_l(j_2)|).
Proof. On S_l(deep), s(b^+ - b^-)(s) = K v_l(s) + (finer targets), so (s b^+)_- + (s b^-)_+ >= -K v_l(s) - |r(s)|; if K < 0 the
anti-sign parts are >= |K|v_l(s)/2 - |r(s)| on {rho_l(s) < |K|y} for every y, contradicting (CS-side) when m_l is not o(y). At j_i,
z(b^+ - b^-)(j_i) = K z eps y_l(j_i)/n_l = K kappa_{j_i}/n_l <= 0, while side admissibility gives z b^+ >= 0 >= z b^-: so
z b^+_{j_i} = z b^-_{j_i} = 0. Finally b^+_{j_i} = B_+(j_i) + c y_l(j_i)/n_l + O(delta) = (c - eps chi_{j_i} D')y_l(j_i)/n_l + O(delta). QED
So with two type-(gamma) contacts whose + fractions differ by >> t/D', the un-switching method has no exact data. (Not a non-recovery
claim.) Corrected statement of Remark 3.6(b): (i) can be relaxed to (i') of 2.3; the general relaxation is OPEN.

## 3. The critical case: what the methods lose (HEURISTIC except where marked)

3.1 (PROVED, arithmetic) If 0 < kappa_- <= m_l(y)/y <= kappa_+ < infinity for 0 < y <= y_0, then for small t
 2 sqrt(C_Q/(kappa_+ q_0)) <= D^#(t) <= 2 sqrt(2 C_Q (1 + 16 q_0 t)/(kappa_- q_0)).
This bounds what Lemma 3.4 can guarantee; it is not a lower bound for the actual amplitude of any mate.

3.2 Cushion sharing (model computation; script critical_factor2.py). Model: S_l = N (gaps 1), v_l(s) = c_0 2^{-s}, |a_s| = 2^{-2s}
(b = 1); then m(2y) = 2m(y) exactly and Exc_{Dv}(2r) = 4 Exc_{Dv}(r). A decomposition at scale t with constrained amplitude D pays at least
 Fdec(t) := sum_s 2(tDv(s) - 2|a_s|)_+ = 2 Exc_{Dv}(t/2)
(the switching s Delta B = -Dv is absorbed by the cushions |a|/t of BOTH sides before any flip), while fixed data built at scale t by
deep assignment pay at scales r << t
 Fdata(r) = sum_{deep} 2(r(Dv - 2|a|/t) - |a|)_+ -> Exc_{Dv}(r)
(one side's cushion only). Numerically sup_{r} [Fdata(r)/r^2]/[Fdec(t)/t^2] = 2.000 for t = 1e-4, 3e-6, 1e-7 (b = 1); -> 0 for b = 0.5;
unbounded for b = 1.5. Consequence (HEURISTIC; tight mate, all flips on one side): Gamma_w(data) + Fl(data) can exceed 1 by the full
flip share Phi_t := 2q_0 Fdec(t)/t^2 ~ q_0 kappa D^2 at every window scale. With a fixed split Theta of the deep usage between the
sides and a decomposition whose + side carries the fraction p of the flips, the bounds available to the method (Gamma_w(B_+) <= 1 -
p Phi, Gamma_w(B_-) <= 1 - (1-p)Phi for a tight mate, Fl(Theta D v) = 2 Theta^2 Phi by self-similarity) certify at best
 min_Theta max(2Theta^2 - p, 2(1 - Theta)^2 - (1 - p)) Phi = (1 - 2p)^2 Phi/8   (attained at Theta = (1 + 2p)/4)
above the budget 1; this certified excess vanishes only for p = 1/2. Averaging over a window gives the same expression with the mean
share p (convexity), so it does not remove the excess. These are statements about what the method certifies, not lower bounds.
Hence the "worst-scale principle" of Y3 3.5(ii) cannot work as formulated: selecting upper points of the log-periodic profile does
not remove the factor 2 coming from cushion sharing.

3.3 Nested raises (arithmetic). Making the constrained switching cushion-compatible at scale r needs |a'_s| >~ rD v_l(s) on
{rho_l(s) < rD}; the top level r = T_0 alone costs about T_0 D m_l(T_0 D) ~ kappa D^2 T_0^2, which is of the SAME order as the slack
(1 - rho^2)T_0^2/6 of Lemma assembly. So Y3's suggested "nested family of raises with masses o(T_0^2)" is impossible for critical
profiles; it works only when kappa D^2 <~ (1 - rho^2).

3.4 Proposition (rho-threshold recovery without profile conditions; PROVED). Let f satisfy Theorem 3.5's hypotheses with (iii)
weakened to "a monochromatic on the deep part of S_l" and (iv) dropped (any profile: sparse, critical, super-critical, mixed),
for the SLD operator or any of its variants (no (D1)(c) needed). Put Lambda_un := C_un |B_sc| C_tau (C_tau: bounded free switching,
an f-constant). Then (f, rho g) in cl NA for every g in C(f) and every rho < 1/(1 + Lambda_un).
Proof. Theorem 3.5's proof uses (iv), (QM) and (D1)(c) only to make C_un sup_W sum_{B_sc}(tau_l)_- small (Step 5). Without them,
sum_{B_sc}(tau'_l)_- <= |B_sc| C_tau, so both data have sqrt(Gamma_w) <= 1 + 2kappa_0 + Lambda_un =: sqrt(G_*) on the windows.
Lemma R2 holds with "Gamma_w <= 2" replaced by "Gamma_w <= G_*" (only its constants change). The averaging step (proof of
thm:windowed) needs rho^2 (G_* + eps_tr) < 1, and Theorem 2.1 needs rho'^2 kappa_w(rho Dbar) <= rho'^2 rho^2 G_* < 1; both hold for
rho < 1/(1 + Lambda_un) after choosing kappa_0, eps_tr small. QED
Remark. This only recovers the shrunken fibre rho_* C(f); it does not give density, but it localizes the critical obstruction at the
boundary of C(f): what is missing is exactly the uniformity of the un-switching cost (C_un D -> 0), i.e. a vanishing constrained
amplitude along suitable decompositions.

## 4. Verified items (no change needed): Lemma 1.1, Lemma 1.2, Theorem 2.1, Theorem 2.2, Lemma 3.1, Proposition 3.3, Lemma 3.4,
Theorem 3.5, Theorem 4.1, Corollary 4.2, Theorem 5.1, Theorem 6.1, (LSC-trunc)(a)-(c). Details in Y3_ref_part1..3.md. The load-bearing
identities, re-derived:
4.1 (Theorem 2.1) |a''_j| = max(|a_j|, 8 rho s_1|b^theta_j|) on F cap [1,N_w], q*(a'') <= 2 at late stages, so for |tau| <= s_1:
 |tau rho b^theta_j| <= |a''_j|/8 < |a''_j|/4 <= s_j(1 - tau rho c)a'_j (no theta-flip); ||a'' - a||_1 <= alpha(N_w) + 8 rho s_1||b^theta||_1;
 z' does not depend on the raise, so (E2) is unchanged and (E1), (E3)-(E5), lem:F1, lem:scrambling hold with K_e adjusted.
4.2 (Theorem 4.1) k perp e, kappa = ||k||^2/(2q_0), k_2 = -kappa e: Z_t = eta_t - U h_t = q_0 z + t chi_c, ||Z_t||_inf <= q_0 (small t),
 ||h_t||^2 = q_0^2 + t^4 kappa^2, q**(Z + Uh) <= max(||Z||_inf, ||h||), a(eta_t) = q_0 - t^2 kappa nu, hence E_q <= t^2 nu||k||^2/(2q_0) + O(t^4);
 the block test of prop:lowerbound uses chi_2 only through q(chi_2) (overshoot) and w(t^2 delta_2) (cancels in E_m).
4.3 (Theorem 5.1) x_j := s_j b^+_{0,j} >= -(1 + 5C_a)|a_j|/t - f^+_j, y_j := s_j b^-_{0,j} <= (1 + 5C_a)|a_j|/t + f^-_j, x_j - y_j = s_j X_j >=
 -12 C_a|a_j|/t; with A_j = (6C_a + 1)|a_j|/t the nearest point sigma_j of [y_j - A_j, x_j + A_j] to 0 satisfies |sigma_j| <= f^+_j + f^-_j;
 coarse peaks: lambda_k|omega_pm(k)| <= t/(2 mu_k); inward-only block coordinates: vs_k omega^+(k) in [-4/t, 1.5 gap(k)/t].
4.4 (Theorem 3.5) X - Xt = -sum_{B_sc} eps_l(tau'_l)_- u_l, hence (b^-, omega^-) = Q + sum_{B_sc} P_l(-eps_l(tau'_l)_-); on S_l(deep),
 s_j Xt_j = (tau'_l)_+ v_l(j) >= 0 and d_j = -(tau'_l)_- v_l(j) <= 0 (monochromatic a).
