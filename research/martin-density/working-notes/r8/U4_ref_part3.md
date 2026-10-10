# U4-ref part 3 — Lemma GW, the hypothesis audit, the re-verifications (VP', MT III', N-dependence)

## 3.1 Lemma GW (generic window use): CORRECT as a meta-argument (inspection standard, as labelled)
I checked the four items against the window theorems on the critical paths:
 - thm:R0 / thm:windowed: uses Lambda_f(l) <= varpi_0^{-l^2} Lambda°(l), T_hi * Lambda_f -> 0, n/K_l -> infinity; with sub-windows
   T_hi(w) <= 2^{-l^3}/(l Q(w)), Q(w) >= Design(l) >= Lambda°(l)^6, n(w) >= l 2^{l^3} Q(w): both limits hold (item (ii)).
 - V1 Proposition TR / Theorem E'' / Master Theorem II: K_w <= C_f Design u^{-4}, c_flat(w) >= c_f u(w), p*(f_j - f) <= theta_w T_lo^2:
   absorbed by Q(w) = (4 Design/u)^{omega+20} (item (ii)); fine weights below the window (item (iii)): sum_{l'>l} lambda_{l'} <=
   b(w)^2/2 <= T_lo(w)^8 for EVERY sub-window of level l (b decreasing in i).
 - Coarse weights above the window: T_hi(w) <= 1/Q(w) <= 1/Design(l) <= D(l)^{-6} <= Phi_{l''}^6 (l'' <= l): every carrier of level
   <= l is coarse on every sub-window of level l (used implicitly by every pinning lemma; contained in item (ii) since D(l) is a design
   factor).
 - Products of f-constants over the rate objects (C_f^{omega(l)}) are absorbed too: (4 Design/u)^{omega} >= C_f^{omega} once
   Design(l) >= C_f.  (U4 lists only C_f^{l^2}; this extension is harmless and makes GW cover pigeonhole arguments with per-object
   constants.)
 - Theorem RS' Step 1 (re-derived): (W*) gives Lambda*_f(l_j) = o(l_j 2^{l_j^3} Lambda°(l_j)); since Design(l) >= (l 2^{l^3}
   Lambda°)^6, Lambda*_f(l_j) <= Q(w_j) and T_hi(w_j) Lambda*_f(l_j) <= 2^{-l_j^3}/l_j -> 0; n_j = O(Lambda*_f(l_j)) = o(n(w_j)); the raise
   depth m_j ~ (2/eps)(2 n_j + log(C/(theta_j c_flat^2))) fits into n(w_j) - n_j (log(1/u) << Q(w)).
No window theorem on the three trees uses an UPPER bound on the window length n or a LOWER bound on T_lo; all window conditions are
monotone in the right direction under enlarging Design(l) (which is how C1's B_mu enters).  CORRECT.

## 3.2 The dependency tables (U4 4.2, 4.3): CORRECT
I spot-checked the entries that carry design features: Y1 rooms on S^nat (P1 + allowedness (a)); V1 Lemma D (needs sum_{l'>l} lambda
<= b^2/2: holds on every sub-window); V1 Lemma DR/TU (base: C1); V2 Lemma 2.3 (sum lambda <= T_lo(l)^3: holds); V2 Theorem B (Lemma TU
+ (2.1): Theorem 2.2(d)); Y3 Prop. 3.3 (D_sigma = bounded gaps + rule (c): both present); Y4 Theorem 1.6 (D^PW: Design >= 2^{s_max}/
delta_min, Q(w): present); Z4 SLD_G (G^*(l) in Design); Z6 D''' (D(l), H_comb in Design); Y2 D^Y (Xi^Y in Design).  Also V2 Cor. C3.1(b)
(not on the trees) survives the (FD) stages (each scheduled index is used infinitely often in every block).
Proposition TR uses N (number of blocks) in its constants (||tau_0 - tau'||_1 <= 2 N D max A K_Q t/u, C_S <= C(1 + N K_P)): for p_N these
are f-constants (f in S_{p_N^*}), so the theorem is per N; no design constant depends on N.  CORRECT.

## 3.3 V3-ref Lemma VP' under (ND'_{L_0}): CORRECT (independently re-derived)
(i) Diagonal base: for x supported in F, U^*x = sum_{s in F} mu_s x_s k_s; e, e(x) lie in span{k_s : s in F}; so for every carrier u,
u(zhat^#) - u(zhat) = <U^*u, e^# - e> = sum_{s in F} mu_s u(s)(e^# - e)_s depends only on u|_F (z is unchanged since the raise keeps
the signs on F).  (ii) G(x)_k := <U^*u_k, e(x) - e> lies in V_0^perp, V_0 := {c : (sum c_k u_k)|_F = 0}.  (iii) DG at (Delta a, x) = (0,0) in
direction xi (supp xi ⊂ F): (1/nu) sum_{s in F} mu_s^2 xi_s (u_k(s) - a_s gamma_k/nu^2), gamma_k = <U^*u_k, U^*a> (derivative of
X -> X/||X|| is P^perp_X/||X||).  (iv) c annihilates the range iff u_c|_F = kappa a|_F with kappa = sum c_k gamma_k/nu^2; conversely such c
has <U^*u_c, U^*a> = kappa' nu^2 when u_c|_F = kappa' a|_F (a supported on F), so the condition is "u_c|_F in R a|_F".  Under (ND') the
multiple must be 0: annihilator = V_0, range = V_0^perp (finite dimension); a finite F_0 ⊂ F gives columns spanning V_0^perp.
(v) On l_1(F_0), DG(Delta a, x) depends continuously on (U^*Delta a, x) (entries involve a_s + x_s on F_0, gamma'_k, nu', all continuous in
U^*(a + Delta a + x)); Graves gives x with G(x) = 0, ||x||_1 <= C_0 |G(0)| <= C_0' ||U^*Delta a|| (|G(0)_k| <= ||U|| ||u_k||_1 2||U^*Delta a||/nu).
(vi) Signs on F_0 kept for ||U^*Delta a|| <= c_0 (finite F_0, |x_s| <= |a_s|/2).  (vii) lam := q^*(a + Delta a + x) >= 1 + ||Delta a||_1 -
(1 + (1 + ||U||) C_0') ||U^*Delta a|| >= 1 when the raise lives where mu_s is small (RS raises at depth y -> 0: the active set leaves
every finite set).  The raise-transfer Lemma 2.3 then holds with the extra additive error 2||Delta a''||_1 (sign change on F_0 breaks
||a + Delta||_1 = ||a||_1 + ||Delta||_1 by at most 2||x||_1), still O(||U^*Delta a||).  CORRECT; no gap found.

## 3.4 Master Theorem III' (V2-ref 4b) logic: CORRECT
Re-read V1 Proposition TR Steps 0-5.  (SH_w) enters only in Step 0 (|Delta d_m| M_m <= K t, Lemma S); (VR_w) only in Step 3 (ray removal).
Replacements: Theorem C1(I) gives Step 0's bound with K <= C_f Design^3/u^3 when rho^sh >= u; V2 Theorem B (system of V2-ref 3: (Z1),
(Z2), (Z3), (Z4'), (Z5), (box), L_0 = Kp) gives a Hoffman projection tau' of tau_0 with ||tau_0 - tau'||_1 <= C_H^# sum_m |Q^#_m(tau_0)| <=
C_f^l Design^2 N K_Q t/u.  Steps 4-5 use tau' only through: ||tau - tau'||_1 (estimates (ii)), tau' >= 0 on kept and = 0 on dropped
carriers and the cone rows (zero cost, z^#-signedness), the box tau' <= 12 lambda/t ((iv) at pulls: t|b(j)| <= 12 lambda v(j) = mu/2;
||V'||_1 <= 4/t; kind [2] bound tau'/lambda <= 12/t) and Q^#_m(tau') = 0 (d-neutrality).  V1's extra property tau' <= tau_0 is never
used after Step 3.  All are rows of Sigma^#.  Constants: K_U, K_w gain the factor C_f^l Design^5/u^4 at most, absorbed by Q(w).
(V2-ref 3(ii): blocks without a donor raise hold only robust or nearly neutral kept carriers, so V2's Step 4/Lemma QB is not needed.)

## 3.5 N-dependence: CORRECT
V2 Theorem B Step 6: minors containing (Z5)-rows are (prod of factors 1/A^#_m) x pi_O(val), with 1/A^#_m >= 1/(2 A_max) >= 1 because
A_m = |R_m^** zhat|_m <= sum_k lambda_{k,m} |u_{k,m}(zhat)| <= m 2^{-m} <= 1/2; so nonzero minors have modulus >= u/2 (the factor
(2A_max)^{-N} >= 1 sits in the DENOMINATOR's lower bound and helps); C_H^# <= max(1,||A||)^{l-1}(rows cols)/min(delta_comb, u/2), with
||A|| <= C (1 + 1/A_min) an f-constant.  Elsewhere N enters only through f-constants (Prop. TR above).  The design is N-free.
