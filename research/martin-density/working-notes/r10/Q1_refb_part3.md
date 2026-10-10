# Q1 referee (b) — part 3: routes, Lemma PM, S2c^tr, C^tr, MT VI, VI.2, and the escape search (working file)

## 3.1 Route decision.  VERDICT: correct (logical bookkeeping).
One companion per (L, w, class); route V for every class; route X only as an independent proof for unshifted / one-signed classes.
Route V's use of X1 = KN^tr's conclusions (S1(a) exact cone, robust minors >= u/2; S1(b) statuses; S1(c) = identity U1 Lemma 1.3).
Absorbers in route V: the CURRENT stage's cluster (stages L+1..L+R_cl) are fine carriers (owner-candidates (d)); absorbers of EARLIER
rounds are coarse block-1 SLD carriers, treated by KN^tr like any coarse carrier (they get statuses, Omega membership, levers).  No
absorber is tuned to value 0 in route V.  Consistent.

## 3.2 Lemma PM.  VERDICT: correct; the clamp-equation argument is the clean core of the combination.
Re-derivation.  From lem:threshold: |w(k)| = M min(1, nu_k/theta), nu_k = |zeta_k|/Phi_k^2, theta = A M/C.  With v_k := |zeta_k|/(Phi_k A):
min(Phi_k M/C, v_k) = (Phi_k M/C) min(1, nu_k/theta), so sum_k min(Phi_k (1-C)/C, v_k)^2 = (M/C)^2 S_1 = 1 since C = M sqrt(S_1).  Every term is
nonincreasing in c; strict peaks give strictly decreasing terms.  EXISTENCE of a strict peak with an f-margin in EVERY block (needed for the
slope): from R**xi/|R**xi| = alpha + D D^* w/C and pairing with w, 1 = M ||alpha||_1 + C = M ||alpha||_1 + 1 - M, so ||alpha||_1 = 1 (M > 0);
alpha lives on strict peaks.  Moreover (new, used below) for k in P: |nv_k| = |alpha_k| + Phi_k^2 M/C gives rho_k = 1 + |alpha_k| C/(Phi_k^2 M),
hence the alpha-MASS IDENTITY  sum_{k in P} (rho_k - 1) Phi_k^2 = C/M = a.
Then (ii) by the intermediate value theorem (Omega terms identical, coarse peak terms identical near C, fine terms changed by at most
((1-c)/c)(|nv_k| + |nv'_k|), slope >= 2 Phi_*^2 (1-c)/c^3 from the natural peak), (iii) from rho_k = v_k C/(Phi_k M) for strict non-peaks.
Fine carriers with |u_k(xhat)| of order 1 are PEAKS (rho_k ~ m |x_k|/(Phi_k theta) -> infinity), so in practice they contribute
Phi_k^2((1-c)/c)^2 at both rows and C moves only by status changes of fine carriers: |C' - C| <= C sum_{fine} Phi^2 << C_f c_{L+1}.
Numerics (Q1_refb_work/clamp_check*.py, independent solver, 80 digits, bisection on theta = S_2/(sqrt S_1 (1 + sqrt S_1)), cvxpy cross-check):
see the final notes for the table.

## 3.3 Lemma S2c^tr.  VERDICT: correct (arithmetic re-done).
 eta'/3 = T^4/(3 L Design) >= T^5 because 1/T >= 2^{n(w)} >= 3 n^2 >= 3 L Design (n >= L 2^{L^3} Q >= L Design);
 mu_kappa(eta'/3) >= c_kappa (eta'/3)^{beta_kappa} >= Design^{-1} T^{5 Design} (beta <= Design, eta'/3 <= 1/Design <= h_kappa);
 Design <= n(w) <= log_2(1/T) gives g_min >= T^{5 Design + 2} >= 2^{-6 log_2^2(1/T)};  ln(1/g_min) <= (6/ln 2) ln^2(1/T) <= 9 ln^2(1/T).
 (W_exp): c_{L+1} <= exp(-1/T_lo(L,M(L))) <= exp(-1/T); eps^viol <= C_f log_2(1/T) e^{-1/T} + C_f e^{-2/T}/T <= e^{-1/(2T)}/2.
 s_1 := max(64 rho eps/delta, e^{-1/(2T)}) <= 2 e^{-1/(2T)} <= s_late >= exp(-C_2 ln^2(1/T)) for T small; K_w^2 s_1 <= exp(2 C_1 ln^2 - 1/(2T)) << T^2.
 Robustness (new remark): even if some window constant had a DESIGN-dependent exponent (K_w <= exp(C Design ln^2(1/T)) <= exp(C ln^3(1/T))),
 (W_exp) still wins; only an exponent of order 1/T^epsilon would break the comparison, and none occurs.
 Precision: Q1 (iii) writes "s_1 <= s_late since exp(-1/(2T)) <= exp(-C_2 log^2(1/T))" — one must also note 64 rho eps/delta <= s_late,
 which follows from eps <= e^{-1/(2T)}/2 and the f, rho-constants being absorbed for T small (Q1 says so in the proof).  Fine.

## 3.4 Theorem C^tr / MT VI / VI.2 / VI.3.  VERDICT: correct modulo the cited refereed tools and Lemma CM^tr's reduction claim (referee (a)).
 Sub-window structure re-checked: Q(w) >= (4/u(w))^{20} with u(w) = b(w^-) forces T_hi(w) <= b(w^-)^{20}/4^{20}, so b(w) <= eta(w) <= T_hi^4 <
 u(w): bands (b(w), u(w)) are nonempty and pairwise disjoint (u(w^+) = b(w)); (D1), (D2) only lower b.  Pigeonhole: omega(L) objects,
 omega(L) + 1 bands.  The objects are f-numbers computed for EVERY pattern (each with its own formula-1 ratio vector) — no circularity with
 the statuses that define f's actual pattern at w.
 (E-d) re-done: |S| c_flat/K >= c_f L 2^{L^3} Design(L)/(C_f C_{f,N}^2) -> infinity; K T_hi/|S| <= K C_{f,N}^2 2^{-L^3}/(L Q) -> 0.
 VI.2: (ii) => (i) uses MT VI at f' and closedness: ||(f', g') - (f, rho g)|| <= p^*(f' - f) + p^*(g' - rho g) < 2 eps; (i) => (ii) is lem:pair
 (read in the note: density gives NA f_n -> f with rho g in Li C(f_n); NA rows have base part in c_00).  VI.3: lem:martintail (read: uses
 only |R_m x|_m <= m 2^{-m} q(x)).  Correct.

## 3.5 Escape search (can an F-finite row avoid the case analysis?)  RESULT: no escape found under option (a); option (b) as stated.
Checked, with proofs or references:
 E1 every block has C_m in (0, 1), M_m > 0, R_m**xi != 0 (u_{k,m} dense in S_{q^*} and xi != 0), alpha-mass 1: f-constants finite/positive;
    l_f exists.
 E2 clean sub-window at every main stage (pigeonhole, 3.4).
 E3 block kinds (U)/(KN)/(T) exhaustive at a clean w: inactive coarse rho in [0,b] ∪ [u,1-u] ∪ [1-b,1+b] ∪ [1+u,inf) = [0,b] ∪ [u,1+b] ∪ [1+u,inf);
    inactive blocks are (U)-blocks (Delta' = 0), their near-threshold carriers get the D2 push.
 E4 robust peak in every block at a clean w (V1 Lemma D), re-derived from the alpha-mass identity: sum_P (rho - 1) Phi^2 = a; weak coarse peaks
    give <= b sum Phi^2, fine peaks <= (1 + ||U||) sum_{fine} lambda/theta <= C_f c_{L+1}; so robust peaks carry >= a - b - C_f c_{L+1} > 0.
    Hence sigma_rob(m) >= Phi_min(L)^2 > 0 and K_kappa is a genuine compact set.
 E5 r(f) in the interior of K_kappa: 1 - R^2 = sigma(1 + 2a + sigma)/(a + sigma)^2 >= sigma since a + sigma <= ||Phi_m||_2 + ||Phi_m||_2^2 < 0.38;
    sigma >= sigma_rob at f (P ⊇ P_rob); so R_a^2 <= R^2 <= 1 - sigma_rob, margin 3 sigma_rob/4 against the eta'-moves.
 E6 Y_1 empty cannot occur at f's pattern (F(r') <= 1 + delta_0 <= 1 + m_0/2); active near-threshold carriers keep their sign (|r_d| ~
    Phi_d/(m K) >= 1/Design^2 >> eta').
 E7 Cross effects of other blocks' moves on a (T)-block's protected statuses: rho_d = m|r_d| K(sigma, R^2)/Phi_d depends only on r_d (exact by
    TU), sigma (peak SET + fine), R^2 (active exact + inactive held at 0): second-order VALUE perturbations of peaks do not enter.  So the
    non-explicit Puiseux exponent never meets a second-order term, PROVIDED every coarse strict non-peak of a (T)-block other than the active
    ones is held (KN-1).  Precision P-HOLD: by (T) these are exactly the nearly neutral coarse carriers of the block; the hold must cover all of
    them (V2 Theorem B exactifies them to 0 as tiny objects; the joint fixed point must keep them at 0), not only those that some earlier
    convention calls "inactive Omega".  Q1's wording "inactive Omega values of (T)-blocks" is correct if Omega = all coarse strict non-peaks
    (route V's convention, Q1 2.2(c)); I recommend stating it.
 E8 Option (b), N >= 2: rows with rho_1(f) = 1, stage 1 active near-threshold in a (T)-block at clean sub-windows of infinitely many levels,
    and 2^{-3} a critical value of psi_1 on a stratum — genuinely open (2.3).  Not an escape under option (a).
 E9 Rows f in NA: trivial.  Rows whose dominant class is trivial (no active carriers): route V with trivial data (no switching): covered.
No candidate row survives; the residual risk is in the single-pass-refereed tools (U1, X1, X2 assemblies), not in the case analysis.
