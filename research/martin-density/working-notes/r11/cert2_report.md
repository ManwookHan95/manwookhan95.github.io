# cert2 report (Round 11): cluster C of the MT VI tree, re-verified from scratch

Cluster C covers the violation-tolerant, d-consistent engineered approximant and the averaging, i.e. X2's analytic core.
All paths below are relative to ctx/ = /tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx.

**Scope.** Items 12-17 and 22 (P6) of r11/MTVI_graph.md 7.1, and S2c^tr's use of item 13.
- Theorem UE, with (p-UE4)-(p-UE7) and (c3').
- Lemma UE-1, with (p-UE1)-(p-UE3), including the claim that K_w has absolute exponents.
- Theorem E^eng, with (p-E1), P6 and the subset version.
- Lemma DC, with (p-DC1)-(p-DC3).
- Lemma LV(a)-(c), with (p-LV1) and (p-LV2).
- Lemmas M1/M1' and M2, and the d-consistency identities of 1.4.

**Sources re-read line by line.**
- r9/X2_notes.md 1.1-4.2; r9/X2_ref_notes.md 0-3.
- r10/Q1_notes.md 2.3-2.6; r10/Q1_refa_notes.md (all, especially 2.1, 2.2, 2.3, 2.8); r10/Q1_refb_notes.md 1.4, 2, 3.
- Part I (paper/martin_density_note.tex): lem:threshold, prop:forced, prop:smooth, prop:continuity, prop:approximants, def:certificate, lem:algebra, lem:base, lem:block, prop:expansion, lem:slack, lem:bookkeeping, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence, lem:assembly, def:twopiece, def:engineered, lem:approxfacts, lem:F1, lem:anchor, def:SC, lem:scrambling, thm:engineered (whole proof).
- Part II (paper2/martin_density_note_II.tex): lem:II-VT with its coordinate list, lem:II-subset, thm:II-E, lem:II-cert.
- r8/U1_notes.md 4.4 and 5.3, for (U5).

**Working notes:** r11/cert2_work/progress.md.

**Scripts** (all new, in r11/cert2_work/). I wrote an independent block solver from lem:threshold (E1)/(E2), using a diagonal base.

| script | output | checks |
|---|---|---|
| dc_cert.py, dc_cert2.py | dc_cert2.out | Lemma DC: 45 instances |
| dc_fixedmove.py | dc_fixedmove.out | the fixed pull/bank term in F(0) |
| gap_cfactor.py | gap_cfactor.out | gap preservation and the factor C |
| eeng_avg2.py | eeng_avg2.out | E^eng averaging with c_flat from 1e-1 to 1e-5 |

**Labels.** Verdicts are correct / correct_with_fixable_gaps / wrong / unclear. I number new precisions C2-k; X2-ref's precisions keep their own names.

## 0. Bottom line

No result in cluster C is wrong. Every conclusion used by Master Theorem VI survives. The analytic core holds up:
- Exact d-consistency by levers (rank-one Jacobian I - pq^T with q^Tp <= C_m < 1/2, then Poincare-Miranda).
- The violation-tolerant per-piece bound with c_flat an f-constant.
- The averaging, which depends on c_flat only through n'c_flat/K and theta'/c_flat^2.

I found 12 new precisions, C2-1 to C2-12, beyond X2-ref's. Three of them correct statements that are false as written, but none affects the tree:
- **C2-5.** The gap-preservation criterion "|C - C^0| <= gap_min/4", used in Lemma DC (5) and Lemma UE-1(c), is off by the factor 1/C. There is a numerical counterexample in which the carrier becomes a peak.
- **C2-4.** X2-ref's bound on |F(0)| in (p-DC1) omits the second-order effect of the fixed TU pull/bank. Numerically this term dominates F(0).
- **C2-9.** X2-ref's bound on |c_i| in (p-UE3) is too crude to give |tau rho c_i| <= 1/2 under the stated (W-a). The Bregman identity gives a sharp bound that closes this without a new hypothesis.

All fixes are absorbed by the super-small application parameters: c_{L+1} <= e^{-1/T}, s_1 ~ e^{-1/(2T)}, and window constants <= exp(C ln^2(1/T)).

The claim that K_w has absolute exponents is **confirmed** by an explicit inventory (section 2). Design(L) enters only the base, through gap_min >= T^{5 Design + 2}, never an exponent.

| # | result | verdict | fixes |
|---|---|---|---|
| 1 | Theorem UE + (p-UE4)-(p-UE7), (c3') | correct_with_fixable_gaps | C2-5, C2-8, C2-9, C2-10, C2-11 |
| 2 | Lemma UE-1 + (p-UE1)-(p-UE3); K_w absolute exponents | correct_with_fixable_gaps; exponents CONFIRMED | C2-5 in (c), C2-10 in (g), C2-11, C2-12 |
| 3 | Theorem E^eng + (p-E1); P6 (window-dependent c_flat(j)); subset version | correct | none (read with P6 and p-E1) |
| 4 | Lemma DC + (p-DC1)-(p-DC3) | correct_with_fixable_gaps | C2-3, C2-4, C2-5, C2-6, C2-7 |
| 5 | Lemma LV(a)-(c) + (p-LV1), (p-LV2) | correct, conditional on cluster-A inputs (5.2) | none |
| 6 | Lemma M1, Cor. M1', identities 1.4 | correct | none |
| 6' | Lemma M2 (uniform ball; natural peak; transfer data) | correct_with_fixable_gaps (statement only) | C2-1, C2-2 |

## 1. Lemma M1/M1', identities 1.4, Lemma M2 (item 6; question (iv))

### Lemma M1 (correct)

Re-derived in the diagonal base, where U^* e_s^* = mu_s k_s:
- X = U^*(A - a) lies in span{k_s : s in J}, which is orthogonal to U^*a.
- Hence nu_A^2 = nu^2 + ||X||^2 and <e_A, e> = nu/nu_A.
- ||e_A - e||^2 = 2||X||^2/(nu_A(nu_A + nu)) <= ||X||^2/nu^2.
- (i): <U^*u, X> = sum_J c_s mu_s^2 u(s).
- (iii): xhat_A - zhat = (z^A - z) + U(e_A - e).
- (iv), masses on F: ||x/|x| - y/|y||| <= 2|x - y|/|y|, and the nu-change gives a first-order cross effect.

### Corollary M1' (correct)

- Crude bound: ||X|| <= sum_W m_s mu_s <= 4 rho s_1 mu_1 n A_0/T.
- Sharp bound: ||P^perp U^*b||^2 = ||P^perp U^*(b 1_F)||^2 + ||U^*(b 1_{F^c})||^2, the two pieces being orthogonal. Hence sum_{s notin F} mu_s^2 b_s^2 <= nu h(b).
- UE's mass set W also puts theta-masses on E ⊂ F_0. There M1(iv) applies (a factor 2 in ||e' - e||). This is harmless: those masses belong to the pre-row f_1 and are not lever variables.

### Identities 1.4 (correct)

Redone algebraically:
- d' = d on Omega; w' = (C'/C)w; H' = (C/C')H; kappa = 0.
- gap' = (C'/C)gap + 1 - C'/C, equivalently gap' - gap = (1 - C'/C)(1 - gap).
- The identity holds to 1e-15 in every DC instance (dc_cert2.out).

### Lemma M2 (correct proof; statement needs two clauses)

The argument (contradiction, prop:continuity, lem:persistence) is correct:
- e''_y >= 1/2, because e_y >= 1 - eta_1 >= 3/4 (lem:transferdata(d)).
- |Y|/q_0 <= sigma e_y/q_0 + Lambda_0, because mu_* <= q_0. So K_y and K_Y do not depend on eta_1.

The statement must be completed:
- **C2-1.** Say "k^nat_m is a peak of f'' with the same sign and margin >= mu^nat_m/2". The same contradiction argument gives this, since the margin is continuous. It is what Lemma PM actually uses: the clamp slope 2Phi_*^2(1-c)/c^3 must hold on the whole interval [C - x, C + x], which needs v''_* >= Phi_*(1-c)/c there.
- **C2-2.** Add |M''_m - M_m| <= gamma_0/4. Applying lem:TV at f' needs M' - gamma >= gamma_0/2, because (c5) is stated with gamma_0/8. The bound |C'' - C| <= C/8 does not imply this when gamma_0 < C/4. This also follows from the same contradiction argument.

## 2. Lemma UE-1 and the K_w exponents (items 2/13; question (ii))

### Item-by-item re-derivation

**(a)**
- Theta masses: ||.||_1 <= 4 rho s_1 n A_0/T.
- Lever masses: <= |Omega|(nu Design 2^{G+2} + 24 lambda 2^G) r.
- q*(A) <= 1 + K_w s_1.
- p*(f' - f_0) <= q*(a' - a_0) + C sum_k min(2 lambda_k, K|Du_k|). This is Z3 Lemma 3.1, in the form [II] lem:II-cost.
- The pull-meeting fine carriers move by O(1) and add + C W_pull (X2-ref p-DC2).

**(b)**
- |Du_k| <= 2Pi_X + C_2 r + t_k. The factor 2 appears when theta-masses sit on E.
- Pull-meeting carriers move by 2|u_k(j_p)|.

**(c)**
- The clamp equation, taken through the natural peak (C2-1), gives |C' - C| <= (2(1-C)/(C c_*))(1/A)(sum lambda|Du| + |DA|/A) = O(Pi), with f-constants.
- **C2-5.** The gap clause needs K_w Pi <= C_min gap_min/4, not gap_min/4 (section 4).

**(d) Bregman**
- Coarse terms contribute K_w Pi^2.
- Fine terms contribute <= 2c_fine(2Pi_X + C_2 r) + 2t(N'').
- Lever-meeting fine carriers contribute <= 2W_lev r. X2's "4 C_lev W_lev r^2" double-counts r; this is harmless.
- Pull-meeting carriers contribute 4W_pull (p-UE2).

**(e) Scrambling**
- K_* is an **f-constant**: it collects the Lipschitz constants of values, thresholds and the clamp formula. X2's "K_* := K_w" is only an upper bound.
- Omega carriers lie in S_2 by d-consistency, as soon as gap >= 2|C' - C|(1 + (M - gap)/C) (p-UE2).
- Phi-mass of A^(1) <= Scr(2K_* Pi) <= C_S(2K_* Pi)^2. This needs 2K_* Pi <= x_0 and 2K_* Pi C_S < 1.
- A^(2) ⊂ {t_k > s_1 T^4}, because Pi >= r >= 4K_J T^4 s_1.
- ||D(w' - w)||^2 <= (K Pi)^2 log_2(2/(K Pi)) + ..., using Phi_k <= 2^{-k}.
- **C2-11.** Fine carriers that meet lever (bank or Z) coordinates move by C_lev r, which can exceed K_* Pi. Add 4m·Phi(lever-meeting fine carriers) <= 8m c_{L+1} to S_m, or take K_* >= C_lev.

**(f)** All three changes are bounded by f-constants times (A_0/T)^2 Pi or A_0 tail_W/T. Correct.

**(g)** The cut-off contributes ||g_i 1_{(N'',inf)}||_1 to c_i. That term is not part of tail_W as defined.
- **C2-10.** Choose N'' last, also with max_i ||g_i 1_{(N'',inf)}||_1 <= T^4 s_1.

### K_w inventory

Every estimate in UE-1, in Lemma DC (with its constants) and in Steps 3-5 of UE is a FIXED finite product of the following quantities:
- n and A_0/T;
- 1/gap_min, 1/x_0 and C_S;
- |Omega|, entering only linearly through sums over levers;
- Design, through:
  - beta <= nu Design;
  - 2^{2G(L)} <= Design;
  - 1/Phi_min <= Design;
  - 1/r_0 <= C_lev Design^C/(g_min A_min u);
- K_J, C_2, C_lev, and m <= N;
- f-constants: 1/c_* (natural peak), 1/A_min, 1/C_min, nu, ||U||, transfer data;
- **C2-12:** add 1/u(w), which enters through the coarse-peak margins (u/2)·theta·Phi in r_0 and in the peak-status clause.

No estimate is iterated a window-dependent number of times:
- Sherman-Morrison is rank one per block.
- Poincare-Miranda involves no iteration.
- The clamp equation goes through ONE natural peak.
- Sums over Omega enter as factors |Omega|.

So K_w <= C_f (n A_0 |Omega| Design C_S/(u T gap_min x_0))^{C_abs} with C_abs absolute.

**Confirmed.** In S2c^tr (Q1 2.5):
- n, Design <= log_2(1/T);
- |Omega| <= Design;
- 1/g_min <= T^{-(5 Design + 2)} and 1/x_0 <= T^{-(5 Design + 3)}.

So ln K_w <= C ln^2(1/T). Design multiplies ln(1/T) inside the base and never becomes an exponent of K_w. Even a Design-dependent exponent (both Round-10 referees' fallback) would only give exp(C ln^3(1/T)) << e^{1/(2T)}.

## 3. Theorem UE (items 1/12; question (i))

### Re-derivation as a modification of thm:engineered and lem:II-VT

**Step 0'.** The order of choices is consistent:
- K_sharp = 4 max(1/q_0, 1/sigma_m)(1 + eta_0) + 2; then eta_1 = min(1/4, delta/(192|I|K_sharp)); then the transfer data and r_f; then t_1, c_flat and c_late.
- All of these are f-constants.
- (c1)-(c3') and (c5)-(c7) contain no window quantity. Only the last inequality of (c4) contains gamma_B.

**Step 2.** The decomposition was re-checked algebraically. The difference of the theta and ± decompositions is rho(±1/2)[v - sum_m R_m^*(Domega_m - Delta_m w^0_m)] = 0. This uses only the two representations at f_0, so it holds for violated pairs. With d' = d on Omega:
- kappa = 0;
- Omega^± = rho(omega^± - d^± w') + rho(d^± - d^theta)(w' - w^0).

### Radius conditions

**Kind [1] and kind [1'].**
- The bound is |sigma omega(k)| <= 4 rho c_flat gap^0(k). It must be <= gap'(k)/2 with gap' >= gap^0/2, so it needs rho c_flat <= 1/16.
- (c4) gives rho c_flat <= 1/(3(A_2 + 2)), which implies this only when A_2 >= 4. In Prop BR A_2 = 22, so it holds there.
- **C2-8.** Add rho c_flat <= 1/16 to (c4).
- Kind [1'] (refa P1) uses only |omega| <= 2gap^0/t and gap' >= gap^0/2, with gap_min covering it. Accepted.

**Kind [2].** The condition 2 rho c_flat A_2 <= gamma_B/4 is the last inequality of (c4). Correct.

**Kind [3].**
- The outward move is <= 3 rho c_flat gap^0 <= gap'/2.
- The inward move is <= 2 rho c_flat A_2 <= (1 - d sigma)M'.
- Together these give the conclusion of lem:block(c), and then lem:block(d)'s computation, which needs only that conclusion plus |d sigma|M/C <= 1/2.
- |d'| <= ||D omega||_2 by Cauchy-Schwarz, since ||Dw'|| = C'.
- Correct.

**Theta regime.** s_1 rho A_2/T <= gap_min/4 is contained in (LATE).

### Base claim (*), coordinate by coordinate

- **W (window contacts carrying a theta-mass).** |tau rho beta^theta| <= m_j/4 <= |a'_j|/2, using q*(A) = 1 + O(K_w s_1).
- **F.** Covered by (c1).
- **E.** Covered by (U3), with V1's K_3 absorbed in (c2). Refa P3's residues V_fine are excesses at support coordinates, <= 2(zx)_-, and are counted in eps.
- **Z-lever coordinates.** b^theta(j) = 0 there, because b^theta = beta + (chi - 1/2)V_proj and V_proj(j(l)) = 0. So (V3)/(H3) survive an inward move that frees j.
- **TU banks.** Contact-like data, plus theta-mass protection.
- **TU pulls.** |tau rho beta(j_p)| <= rho c_flat(2A_2 + C_Delta)·lambda v <= 7 lambda v, against (1 - tau rho c_i)|a'_{j_p}| ≈ 24 lambda v. This is (c3'); the margin is ample because q*(A) ≈ 1 and |tau rho c_i| << 1.
- **(N_w, N''], free coordinates, and beyond N''.** As in [II] lem:II-VT.

For |tau| > s_1 the linear terms are (1/128 + 1/32 + 1/128) delta|tau| s_1 <= delta tau^2/16.

### Steps 4-5

- These re-derive lem:TV through (c5), the error E <= delta tau^2/8 through eta_1 and (c6), and the bracket <= Gamma^{(0)} + delta/8.
- The final arithmetic is 1 - 2delta + 3delta/4 <= 1 - delta.
- Gamma_theta <= max Gamma_± by convexity, which does not need admissibility.

### (VT')

64 rho eps <= delta s_1 is stricter than [II]'s (VT), 2 rho eps <= delta s_1/16. It is used only through the linear term 2 rho|tau| eps for |tau| > s_1. Correct.

### (LATE)

The proof uses (LATE) in the following places:
- Pi <= 1/K_w;
- K_w^3 s_1 log(e/s_1) <= c delta, for Bx + S <= c_late delta s_1;
- the theta radius;
- |tau rho c_i|;
- the Step 5 bracket;
- gap' (C2-5);
- the scrambling bound 2K_* Pi <= x_0;
- the coarse-peak status clause;
- r <= r_0 and K_J C_2 r <= 1/8;
- f' lying in the M2 ball;
- q*(A) <= 2;
- K_w^2 s_1 <= K T^2 (for E^eng).

All of these are implied by s_late = c(f, delta)(T gap_min x_0/(n A_0 K_w))^C with C >= 7. X2's displayed (LATE) does not imply the second one. X2-ref's (p-UE5) is right.

### (W-a)-(W-c) and C2-9

- (W-a) must carry X2-ref's factor (1 + C_2 K_J), or use (p-UE1)'s second-order sharpening. (W-b) must also absorb C2-4's fixed-move terms.
- **C2-9.** X2-ref's (p-UE3) bounds |c_i| by ||g'' - g||_1, giving K_w(Pi + c_fine + tail_W)/t_i. That bound is valid but would need K_w c_fine <= 1/4 for |tau rho c_i| <= 1/2, which (W-a) does not give.
- The sharp bound comes from the **Bregman identity** (g''_i - g_i)(x') = -(b^theta_i 1_{(N_w,inf)})(x') - sum_m d^theta_{i,m} Bx_m. This holds because R_m^*(w^0 - w')(x') = -Bx_m. It gives

  |c_i| <= (1 + ||U||) tail_W + ||g_i 1_{(N'',inf)}||_1 + K_w(Pi + c_late delta s_1)/t_i.

- This bound has no standalone c_fine and only an f-constant in front of tail_W. So |tau rho c_i| <= 1/2 and K_A hold under (W-a) and (W-c) as stated.
- K_w c_fine enters only the conclusion p*(g' - rho g), which E^eng handles through (p-E1).

**Verdict:** correct_with_fixable_gaps. The fixes are C2-5, C2-8, C2-9 (a proof change only), C2-10 and C2-11, plus X2-ref's p-UE1 to p-UE7 and (c3').

## 4. Lemma DC (items 4/15; question (iii))

### Re-derivation

Write F_l(P) = eps_l(u_l(x_1) - u_l(z_0)) + P_l + E_l(P) - p_l(A_m(P) - A_m^0), with p_l = eps_l u_l(z_0)/A_m^0. Then:
- A_m(P) - A_m(1) = <w_m(1), R_m dx> + a Bregman term in [0, <w(P) - w(1), R dx>].
- The Jacobian is J = I - p q^T in each block, with q_k = eps_k lambda_k w^0(k).
- q^T p = sum_{Omega_m} Phi_k^2 w^0(k)^2/C_m <= C_m <= ||Phi_m||_2 < 1/2.
- Sherman-Morrison gives ||J^{-1}||_inf <= 1 + ||p||_inf ||q||_1/(1 - q^T p) <= 1 + 2/A_min, since |u(zhat)| <= q*(u) = 1. X2's 1 + 4/A_min is conservative.
- Poincare-Miranda applies with weak inequalities on the faces.

Slopes:
- A Z-move gives slope exactly 1.
- A bank gives P nu_1/nu_A = P + O(||X_lev||^2/nu^2).
- A TU lever at P = 0 has net change of second order: the flip contributes -2v(j_p), the bank contributes +2v(j_p) nu_1/nu_A, and the pull mass adds a tiny Hilbert term.
- ||X_lev||/nu <= Design 2^{G+2} r, by efficiency.

### Numerics (dc_cert2.out)

There were 45 instances, with 1-2 blocks, |Omega| from 1 to 4, TU and Z-con levers, and the pull at v in [r, 2r):
- A zero P* exists in every instance, with |P*| <= 2K_J|F(0)| (worst ratio 0.017).
- nv is exact to 1e-16.
- The statuses of all coarse carriers are kept.
- The gap identity holds to 1e-15.
- J = I - pq^T up to O(||X_lev||/nu).

### Precisions

**C2-3.** delta_1 must be a max over Omega plus weighted sums, not a max over all carriers: late carriers supported beyond N'' move by O(1). Choose N'' last, with max_{Omega} t_k(N'') <= T^4 s_1. (X2-ref p-J noted max_Omega t_k <= t(N'')/lambda_min.)

**C2-4.** F(0) also contains:
- the second-order effect of the FIXED TU pull/bank, <= C_2(2^{G+1} r)^2;
- the fixed bank part acting on fine carriers through the bank coordinate, <= 2^{G+2} r |Omega| c_tiny/A_min;
- and the linear remainder is (|Omega| c_tiny/A_min)|P|, not c_tiny|P|.

So (p-DC1)'s bound "|F(0)| <= delta_1(1 + 1/A_min) + 2W_pull/A_min" is incomplete. In the model, |F(0)| was 10-2000 times delta_1. The per-instance exponent in v(j_p) was about 2.0, dropping to 1.5-1.8 when fine carriers meet the bank or pull coordinates (dc_fixedmove.out).

The fix is to require K_J C_2 2^{2G+2} r <= 1/8 and K_J 2^{G+3} |Omega| c_tiny/A_min <= 1/8. The radius r of (p-DC1) is then unchanged.

In the application:
- C_2 <= Design^C, using 2^{2G(L)} <= Design;
- r <= exp(C ln^2(1/T)) e^{-1/(2T)};
- c_tiny <= Design^C c_{L+1}.

So both conditions hold.

**C2-5.** Gap preservation. From gap' - gap = (1 - C'/C)(1 - gap) we get |gap' - gap| = |C' - C|(1 - gap)/C. The criterion "gap(P*) >= gap^0/2 once |C(P*) - C^0| <= gap_min/4" (DC step (5), UE-1(c)) is **false as stated**.

In gap_cfactor.out (C = 0.243, gap^0 = 0.0100, nv held exact):
- |C' - C| = 0.00186 < gap/4 gives gap' = 0.00242 < gap/2;
- |C' - C| = 0.00249 < gap/4 makes the carrier **become a peak**.

The correct criterion is |C' - C| <= C gap/(2(1 - gap)). This is harmless here: at the companion |C' - C| <= C_f c_{L+1} << C g_min (Lemma PM), and UE-1(c) can take Pi <= c C_min g_min/K_w.

**C2-6.** Status along the whole cube must be measured in VALUE units:
- l in Omega stays a strict non-peak iff |u_l| < (A M/(m C)) Phi_l;
- its room is Phi_l A gap_l/(m C);
- along the cube C(P) moves at first order, by O((r + delta_1)/A_min) through the clamp equation, so gaps move by O(r/Phi_l).

Hence:
- r_0 <= c min_Omega Phi_l gap_l A_min/(m C_lev);
- r_0 <= c (coarse-peak margins (u/2)·theta·Phi_min)/C_lev.

Q1 PM(v) compares a value move "<= g_min/2" with a gap. That mixes units, but the slip is harmless: 1/Phi_min <= Design, and Q1's r_0 >= c g_min/(C_lev Design^C) already allows the factor.

**C2-7.** The apparent circularity among W_pull(j_p(r)), r and N'' is resolved by monotone bounds:
- W(j_*) with v(j_p) <= 2^{G+1} r_*;
- pulls satisfy v(j_p) >= r >= 4K_J T^4 s_1, so j_p <= J(r_min) < N''.

### Pulls as fixed O(1) moves (p-DC2)

- Carriers that meet j_p are at stages >= j_p > s_max > L, by allowedness (c).
- Hence W_pull <= (8/3) c_{j_p} <= (8/3) c_{L+1}, and W_pull/r <= C T^{-4} e^{-1/(2T)} -> 0, which is super-small.
- W_pull enters F(0), the Bregman term, S_m and the cost, each harmlessly.

**Verdict:** correct_with_fixable_gaps (C2-3 to C2-7, plus X2-ref p-DC1 to p-DC3).

## 5. Lemma LV(a)-(c) (items 5/16)

### 5.1 Internal logic

- (D-lev) arithmetic: mu_j^2 v_l(j) = mu_j^2 delta_l 2^{-j}/n_l decreases in j, so j(l) <= sigma_2(L) gives >= 1/Design. This agrees with refb 1.4.
- Bounded gaps G give an element of S_l with v in [r, 2^G r).
- (SEP)(ii) follows from allowedness (c).
- K_X = 0 after (R-abs).
- The pulls lie in S_l ∩ (s_max, s_far] ⊂ E_c (p-LV2): r >= 4K_J T^4 s_1 >> 2^{-s_far}.
- TU pull protection is (c3'), section 3.

### 5.2 Conditional on cluster A

- At Z-lever coordinates the data are ±V_fine(j)/2 with b^theta(j) = 0. This needs CM'(b)'s symmetric representation b^+ = beta + chi V_proj + V_fine/2. The condition b^theta = 0 is exactly what (H3) needs after an inward Z-move frees j.
- V1 (C1) contacts and exactness on E_c are cited, not re-derived here.

**Verdict:** correct, conditional on those cluster-A inputs.

## 6. Theorem E^eng (items 3/14, P6; question (v))

### Re-derivation

The inputs are the per-piece bounds (A) and (B), and convexity of p*. Take r_0^2 <= min(delta, 1 - rho^2); no c_flat t_1 is needed, because when I_r is empty every piece obeys (A).

**Case |r| <= r_0.**
- sum_{I_r} t < 2|r|/c_flat over dyadic scales, and this holds for ANY subset of them.
- If I_r is nonempty then |r| > c_flat T_min, so eps' <= 2theta' r^2/c_flat^2.
- The case needs 2theta'_j/c_flat(j)^2 + 4K_j/(|S_j| c_flat(j)) <= min(delta/4, (1 - rho^2)/6).
- Then 1 + r^2/2 - delta r^2/4 <= 1 + r^2/2 - r^4/8 because r^2 <= 2delta, and lem:slack(a) finishes.

**Case |r| >= r_0.** eps' + 4K T_hi|r|/|S| <= (1 - rho^2) r_0|r|/3.

**Conclusion.** gbar is in C(f'); prop:reduction(d) applies; and dist <= eps' + 4K T_hi/|S| -> 0.

theta'_j must contain UE's cost K_w Pi log(e/Pi) + C W_pull. That is <= exp(C ln^2(1/T)) e^{-1/(2T)} = o(T^2 c_flat^2), because c_flat >= c u(w) and T <= 2^{-(4/u)^20}. (p-E1) is needed so that e_{j,i} <= K t_i at the smallest scale.

### P6 (confirmed)

Only (c4)'s last inequality contains gamma_B. All the other conditions are upper bounds on c_flat, so they persist as c_flat decreases. t_1, K_sharp, eta_1, the transfer data, r_f and c_late do not depend on gamma_B.

E^eng uses c_flat only in three places, all tracked by (E-d) with c_flat(j):
- the range of (A);
- the dyadic count;
- the condition |r| > c_flat T_min.

### Subset version

- UE applies to any subfamily, since K_w is monotone in n.
- min S' >= T_lo.
- Averaging over S' works as above. This is a third pass, after X2-ref and refa G1.

### Numerics (eeng_avg2.out)

Inputs (A) and (B), averaged over random half-subsets of a 300-scale dyadic window, in stable excess arithmetic:
- The averaged bound holds iff n'c_flat/K >~ 133, **identically for c_flat = 1e-1 ... 1e-5**. The proof's sufficient threshold is 294.
- The tolerated theta'/c_flat^2 is about 1.8-7.5, against the proof's 0.0034.

So the averaging depends on c_flat only through n'c_flat/K and theta'/c_flat^2.

**Verdict:** correct, with the statement read with P6 and (p-E1).

## 7. Dependencies and remarks for other clusters

- **(U5) at companions** (CM'(a), from U1 Lemma 4.3) rests on the following facts:
  - every fine carrier of a negative block is a PEAK, as a self-aligned owner, with margin >= q_0 delta_k H_k/(2 n_k);
  - Phi_k <= (delta_k H_k)^2, by (W3).

  If infinitely many fine strict non-peaks existed, Scr would be linear, since Scr(s) >= sum_{Q, Phi <= s} Phi. So (U5) is a genuine cluster-A input (Step B ownership); it is not automatic.
- Prop BR's claims are cited, not re-derived here (cluster A):
  - A_0 is an f-constant;
  - A_2 = 22;
  - E-coordinate data obey "contact-like, or t|b| <= K_3|a^#|";
  - Phi_min(L) >= 1/Design(L) and Design(L) <= n(w) <= log_2(1/T), which are cluster D's design facts.
- c_fine <= C_f c_{L+1} needs every coarse peak to have margin >= x_0, which holds because the coarse-peak margin is >= (u/2)·theta·Phi_min >> x_0. Fine carriers meeting lever coordinates have weight <= 2c_{L+1}.

## 8. Precisions list

| id | where | statement | effect |
|---|---|---|---|
| C2-1 | Lemma M2(a) | natural peak keeps margin >= mu^nat/2 on the ball | needed by Lemma PM's slope on [C - x, C + x]; same proof |
| C2-2 | Lemma M2(a) | add \|M'' - M\| <= gamma_0/4 | needed by lem:TV at f' with (c5); same proof |
| C2-3 | Lemma DC | delta_1 := max over Omega; N'' with max_Omega t_k(N'') <= T^4 s_1 | harmless |
| C2-4 | Lemma DC, (p-DC1) | F(0) also has C_2(2^{G+1} r)^2 + 2^{G+2} r \|Omega\| c_tiny/A_min; linear remainder (\|Omega\| c_tiny/A_min)\|P\|; require K_J C_2 2^{2G+2} r <= 1/8 and K_J 2^{G+3}\|Omega\| c_tiny/A_min <= 1/8 | holds in application; numerically the dominant part of F(0) |
| C2-5 | DC (5), UE-1(c) | gap' >= gap/2 needs \|C' - C\| <= C gap/(2(1 - gap)); "gap_min/4" is FALSE (counterexample) | harmless: \|C' - C\| <= C_f c_{L+1} |
| C2-6 | DC (5), PM(v) | status radius in value units: r_0 <= c Phi_l gap_l A_min/(m C_lev) and coarse-peak margins/C_lev | covered by Q1's r_0 >= c g_min/(C_lev Design^C) |
| C2-7 | DC, 3.2 | W_pull, r, N'' ordering via monotone bounds | no circularity |
| C2-8 | UE (c4) | add rho c_flat <= 1/16 (kind [1]/[1'] radius) | implied when A_2 >= 4 (A_2 = 22) |
| C2-9 | UE-1(g), (p-UE3) | bound c_i through the Bregman identity (g'' - g)(x') = -(b^theta 1_{>N_w})(x') - sum d^theta Bx_m | removes an otherwise needed K_w c_fine <= 1/4; no new hypothesis |
| C2-10 | UE-1(g), 3.2(iv) | N'' also with max_i \|\|g_i 1_{(N'',inf)}\|\|_1 <= T^4 s_1 | harmless |
| C2-11 | UE-1(d),(e) | Bregman lever term 2W_lev r; K_* an f-constant; add 4m Phi(lever-meeting fine) to S_m | <= 8m c_{L+1}, harmless |
| C2-12 | UE-1 K_w | add 1/u(w) to K_w's argument list | absolute exponents still; u^{-1} <= log(1/T)^{O(1)} |

**None of C2-1 to C2-12 changes the hypotheses or conclusions of Lemma S2c^tr, Theorem C^tr or MT VI.** The cluster-C links can now be counted as two independent passes (X2-ref plus this certificate), with the precisions above. The subset averaging for E^eng and P6 now have three passes.
