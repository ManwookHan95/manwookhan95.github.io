# Y1 referee, part 3: the exactifying companion (Y1 part 4: donors, Lemmas 4.1-4.3)

## 3.1 Donors (Y1 4.1)
Definition and examples: correct. Existence at maximal contact: by Z4 Lemma 5.0 every block has infinitely many non-degenerate
peaks with w = -eps_0 M (margins >= q_0/4); only finitely many S_l meet F; z = eps_0 = -vs on S_c: donors. CORRECT.
IMPRECISE JUSTIFICATION, CORRECT CONCLUSION (m3). "A donor is pinned at every window: at w it is either in class R or in class G with
eps_c = -vs_c (the exceptional coordinates lie in [1,l] for l >= l_f, so outside S^nat_c)". The parenthesis is wrong: S^nat_c(l) =
S_c \ (F ∪ T(l)) does not remove [1,l], so an exceptional point (vs z > 0) may stay in S^nat_c(l) for all l. I first suspected a
counter-scenario (all non-exceptional early points of S_c covered by coarse targets, making c a class-G SWALLOWING-type peak, which would
make "(C3) after (C1)" infeasible). It is REFUTED by the tail point s_m itself. Correct proof (PROVED):
 s_m in S^nat_c(l) (s_m notin F as S_c ∩ F = {}, s_m notin T(l) as s_m > s_max(l)) and vs z_{s_m} <= 0 (l >= l_f). Room in the direction
 sigma = -vs: sum_{S^nat} v(1 - vs z) >= v_c(s_m) >= delta_c 2^{-sigma(l)}/n_c, while b(w) <= T_lo(w)^4/(l Design(l)) <= 2^{-24 sigma(l)}/l
 (Design >= 2^{6 sigma(l)}, T_lo <= 1/Design). As delta_c/n_c is fixed and sigma(l) -> infinity, v_c(s_m) > b(w) >= b(w)||v 1_{S^nat}||
 for l large. Hence at a class-G level the minimizing direction is sigma = +vs, i.e. eps_c = -vs_c (anti-type), and every exceptional
 point s_e in S^nat would contribute v(s_e)(1 + vs z_{s_e}) > v(s_e) (fixed) > b(w) to that room, so none lies in S^nat_c(l). So the donor
 is class R (pinned, 3.5(d)) or a class-G anti-type peak (pinned, 3.5(a)); (C1) sets z^# = -vs on S^nat_c(l) ∋ s_m and (C3) after (C1)
 has outward room 2 v_c(s_m). Y1's construction is correct as written; only the parenthetical reason must be replaced.

## 3.2 Companion (Y1 4.2): modified sets
(C1) on S^nat_{l''}(l) (disjoint signature sets, disjoint from T(l)); (C2) on T(l) \ F; (C3) at s_m in S_{c_m}, s_m > s_max(l), s_m notin
F (S_c ∩ F = {}). Disjoint except s_m in S^nat_c for a class-G donor, resolved by "(C3) after (C1)" (feasible by 3.1). |z^#| <= 1, z^# = sgn a on F; (a, z^#) admissible forced data
(rem:lemmaZ(c)); zhat^# - zhat = z^# - z (e unchanged since a is unchanged). CORRECT.
Checked side effects: T(l) ∩ S_{l'} = {} for l' > l (allowedness (a)), so (C2) touches fine carriers only through their targets; (C1)
may change FINE carriers' values u_{l'}(zhat) by O(1) (fine targets may meet S^nat_{l''}(l)), but their total block effect is
sum_{l'>l} lambda_{l'} |u_{l'}(Delta)| <= 3 sum_fine lambda <= b^2, and fine coordinates carry omega = 0 in the data. Harmless.

## 3.3 Lemma 4.1 (cost).  CORRECT.
Delta_m = sum_k lambda_k |u_k(Delta)|: coarse non-donors <= l(|T(l)|+1) b(w); donor = T_lo(w)^3 (by the choice of theta_m); fine <= 2b^2/3;
so max Delta_m <= 2 T_lo^3 <= c_f for l large and Z3 Lemma 3.1 (any admissible T) gives p*(f^# - f) <= C_f T_lo^3 log(1/T_lo).
Feasibility of (C3): available outward push lambda_c v_c(s_m)(1 - vs z_{s_m}) >= lambda_c delta_c 2^{-sigma(l)}/n_c (s_m <= sigma(l));
T_lo^3 <= Design^{-3} <= 2^{-18 sigma(l)}; sigma(l) -> infinity (targets dense in S_{q*}, so their supports are unbounded). CORRECT.

## 3.4 Lemma 4.2 (status table).  CORRECT.
(a) |u_{l''}(Delta)| <= r^nat + |T(l)| b <= (|T(l)|+1) b for coarse non-donors (u_{l''} vanishes on S^nat of other carriers and at s_m).
(b) non-raised blocks: T2(a) with E_m <= 2l(|T|+1)b + b^2 and C_1 f-constant (fixed non-degenerate peak k_0). Raised blocks: T2(b) at the
    donor with s = T_lo^3 and E <= E_m << A s/(8(A+theta+1)); delta_m in [c_f T_lo^3, C_f T_lo^3]. Re-derived.
(c) rho^# = rho theta/theta^# + O(N D(l)(|T|+1) b/theta^#); robust statuses preserved with u/2 margins; in raised blocks every coarse
    coordinate with |rho - 1| <= b has rho^# <= (1+b)/(1+delta) + C D(|T|+1) b <= 1 - delta/3 (b D(|T|+1) <= T_lo^4/l << delta).
(d) rooms: target coordinates are contacts or free with room >= u(w) at f^# (clean sub-window + (C2)). Contacts of f keep their signs
    except at FLIPPED (C1) coordinates (z_s eps < 0), which lie in S^nat and carry no coarse target. CORRECT.
(e) q^# = eps u(zhat^#)/A^# at strict non-peaks of f^#; converted (K4) peaks: q^# = (A/A^#) rho q + O(b)/A^# with rho in [1, 1+b]. CORRECT.
Observation: non-raised blocks may contain near-threshold coordinates that change status (peak <-> strict non-peak) between f and f^#;
all of them are DROPPED (kept near-threshold carriers force a raise), and Step 5 of Proposition 5.2 handles dropped status changes.

## 3.5 Lemma 4.3 (Z3 Lemma 1.4 revisited).  CORRECT.
u_{l''}(Delta) = sum_{S^nat} v(s)(eps - z_s) = eps r^nat; with u_{l''}(zhat) = 0 (d-neutral iff u(zhat) = 0 off P), q^# = r^nat/A^# > 0.
The remark "re-tuning the Hilbert part has |F| - 1 degrees of freedom" is the Z3 referee's; see part 5 for a further channel
(free target coordinates) that can restore exact d-neutrality in some configurations (SKETCH).
