# Y1 part 5a — Transplant: exact d-neutral two-piece data at the companion f^#_w

Setting of parts 3-4: D_X, f with F finite, g in C(f), clean sub-window w = (l,i), l >= l_f, t in W(w) dyadic, t <= min(t_eta,1),
a two-sided decomposition (B_+-, Theta_+-) of g at f at scale t, companion f^# = f^#_w.  Constants: K_g, K_d, K_P, K_O of part 3
(all <= C_f D(l)^5 u(w)^{-3}); G := class-G coarse carriers; P := the DROPPED G-carriers (Summary of part 3: anti-type G-peaks,
anti-type near-threshold G strict non-peaks, swallowing-type G-peaks with robust margin, Sigma_m(w) in one-signed blocks, donors).

**Repair directions.**  For a block m and a sign s, (DR^s_m) means (Z4 Definition (DR), one sign at a time): there is a finitely
supported rho^{m,s} in R^B_{>= 0} (B = exactly swallowed carriers of f) with zero cost at f (sum_l eps_l rho_l u_l 1_{F^c} is z-signed
and supported in K), vanishing at swallowed peaks, with d-sums sum_{m(l)=m} q_l rho_l = s and sum_{m(l)=m'} q_l rho_l = 0 (m' != m).
Block m is COMPENSATED if (DR^+_m) and (DR^-_m) hold (Z4's (DR); e.g. resonant bad strict non-peaks with q > 0 > q', Z6).
Repair directions are fixed f-dependent objects; R_f := max ||rho^{m,s}||_1; l_f is taken >= every carrier in their supports.

**Hypotheses at w.**
 (SP_w)  shift sources (part 3);   (Do_w)  donors for the blocks that need a raise (part 4);
 (Cmp_w) every block is COMPENSATED AT w ((Rep^+_m) and (Rep^-_m), Definition in Y1_part5c / notes 5.1') or sigma-one-signed
         at w (Lemma 3.6) for some sigma = sigma_m;
 (NN_w)  in every sigma-one-signed block m: no KEPT carrier (type (K3)) has sigma q^#_{l''} > 0, and if some kept carrier has
         sigma q^#_{l''} < 0, then (Rep^sigma_m) holds at w.  (q^# = d-coefficient at f^#, Lemma 4.2(e).)
 (Fixed directions: (DR^s_m) at f implies (Rep^s_m) at every clean w of large level, Lemma 5.1'.)

**Lemma 5.1 (repair carriers are untouched by the companion).  PROVED.**  For l >= l_f: every carrier l_R in the support of a
repair direction satisfies u_{l_R}(zhat^#) = u_{l_R}(zhat), hence q^#_{l_R} = q_{l_R} A_m/A^#_m EXACTLY, and every repair direction has
zero cost at f^#; its d-sums at f^# are s A_m/A^#_m in block m and 0 in every other block.
Proof.  l_R is exactly swallowed, so (C1) does nothing on S^nat_{l_R}.  The near-contacts in supp u_{l_R} \ F are finitely many
coordinates with FIXED rooms > 0; for l >= l_f these rooms exceed u(w) (u(w) -> 0), so (C2) does not touch them.  (C3) acts on
s_m notin T(l) in the signature set of a donor (a peak, hence not in the support of a repair direction, which vanishes at peaks).
So u_{l_R}(Delta) = 0, and q^# = eps u(zhat^#)/A^# (Lemma 4.2(e)).  Zero cost at f^#: contacts of f keep their signs at f^#, and at
non-contacts of f the vector of the direction vanishes (zero cost at f).  QED

**Proposition 5.2 (transplant at a clean sub-window).  PROVED (by modification of Z3 Proposition T, Z4 Steps 2-6 and Z6
Theorem U' (5)-(6); every departure is listed).**  Assume (SP_w), (Do_w), (Cmp_w), (NN_w).  Then there is a functional g_t carrying
d-neutral two-piece data (b^+-, omega^+-) AT f^# (Definition def:twopiece at f^#) such that
 (i)   b^+-(xi^#) = 0, t||b^+-||_1 <= A_0 (an f-constant), Gamma^#_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta) + C theta_w) + K_w t)^2;
 (ii)  p*(g - g_t) <= K_w t,  with K_w <= C_f Design(l)^3 u(w)^{-3} (Y1_part5c 5c.2);
 (iii) every k in supp omega^+-_m satisfies, at f^#, one of [1] gap^#(k) >= t^2, |omega(k)| <= 2gap^#(k)/t; [2] gap^#(k) >= gamma(w) :=
       min_m M_m u(w)/4 and |omega(k)| <= A_2/t; [3] k a strict non-peak of f^# with the INWARD sign for the side (vs omega^+(k) <= 0
       <= vs omega^-(k), up to 1.5 gap^#(k)/t) and |omega(k)| <= A_2/t;  A_2 := 22.
Proof.
Step 1 (zero-cost projection; combinatorial).  Let tau := (tau_{l''})_{l'' in G} (tau = -eps Delta theta).  Let kappa^# be the generalized
configuration of level l with U := G, P as above, eps, F' := F ∩ T(l), type(j) := sgn z^#_j if |z^#_j| = 1 and 0 otherwise
(j in T(l) \ F), and box radii beta_{l''} := 12 lambda_{l''}/t.  For tau' in Z_{kappa^#}(beta), V(tau') := sum_G eps tau'_{l''} u_{l''} 1_{F^c}
is z^#-signed and supported in K^#: on S^nat_{l''} only u_{l''} among G-vectors lives (no coarse target there) and z^# = eps_{l''}
(Lemma 4.2(d)), tau' >= 0; on T(l) \ F the rows (Z2); elsewhere the G-vectors vanish (supp u_{l''} \ F is in S^nat_{l''} ∪ T(l)).
Violations by the actual tau (Lemmas 3.2-3.6, 4.2(d); Delta B 1_{F^c} = V(tau) + e_0):
 (Z1): sum (tau)_- <= K_g t;  (Z2) at contacts of f^#: (z^#_j L_j(tau))_- <= (z^#_j Delta B(j))_- + |e_0(j)| and (z^#_j Delta B(j))_- <=
 phi_{z_j}(Delta B(j)) (if z_j = z^#_j = +-1, or z^#_j = sgn z_j with |z_j| < 1: phi_z(x) = |x|(1 + |z|) when sgn x = -sgn z); at
 free coordinates of f^# (room >= u(w)): |L_j(tau)| <= phi_{z_j}(Delta B(j))/u(w) + |e_0(j)|; sum <= (t/q_0)(1 + 1/u(w)) + 2||e_0||;
 (Z3): sum_P |tau| <= l K_O t (Lemmas 3.5, 3.6);  (Z4): |tau| <= 6 lambda/t (Lemma lem:box): no violation.
Hoffman (definition of G**(l)): tau_0 in Z_{kappa^#}(beta) with ||tau - tau_0||_1 <= G**(l) V_w, V_w := C_f l D^5 u(w)^{-3} t.
Step 2 (d-rows at f^#).  Q^#_m(tau') := sum_{l'' in G\P, m(l'')=m} q^#_{l''} tau'_{l''}.  By eq:didentity at f and Lemmas 3.1, 3.5, 3.6:
|sum_{G, m} q tau| <= (K_d + (K_g+1)/C_m + 2/sigma_m) t and |sum_{P,m} q tau| <= l K_O t/C_m.  For kept l'': |q^# - q A/A^#| <=
(b(w) |q| + (|T(l)|+1) b(w))/A^#_m (Lemma 4.2(e); for converted (K4) peaks q = eps vs Phi M/(mC) and |u(zhat)| = rho Phi theta/m with
|rho - 1| <= b), and |tau_0| <= 12 lambda/t; so |Q^#_m(tau_0)| <= K_Q t with K_Q := C_f(K_d + K_g + l K_O + G** V_w/t) + C l(|T(l)|+1)b/t^2,
and b/t^2 <= t^2.
Step 3 (exact d-repair).  Let rho^{m,s} be the directions of (Rep^s_m) at w (d-sums s d_{m,s} in block m, d_{m,s} >= u(w)/Design(l),
0 in the other blocks, all computed at f^#).  Compensated block m: c_m := |Q^#_m(tau_0)|/d_{m,-sgn Q}, add c_m rho^{m, -sgn Q^#_m(tau_0)}.
sigma-one-signed block m: the kept carriers are of type (K3) only; if all have q^# = 0 then Q^#_m(tau_0) = 0; otherwise by (NN_w) all
nonzero q^# of kept carriers have sign -sigma, so sgn Q^#_m(tau_0) in {0, -sigma}, and we add (|Q^#_m(tau_0)|/d_{m,sigma}) rho^{m,sigma}.
Call the result tau'.  The d-sums of the added directions are block-diagonal at f^#, so Q^#_m(tau') = 0 for every m, and
||tau' - tau_0||_1 <= N K_Q t Design(l)/u(w).  Sums of zero-cost vectors with nonnegative coefficients have zero cost (Z4 Lemma 2.3: phi_z is
subadditive and positively homogeneous), so V' := V(tau') is z^#-signed in K^#, and
  ||Delta B 1_{F^c} - V'||_1 <= ||e_0||_1 + ||tau - tau'||_1 <= K_U t,  K_U := K_g + 1 + G** V_w/t + N K_Q Design(l)/u(w).
(Carriers of the repair directions may lie in P; they receive only amounts <= K_Q t Design/u(w); they are strict non-peaks of f^#,
with gap^# >= M u(w)/4 where q^# < 0 (definition of (Rep)).)
Step 4 (split at f^#).  Lemma lem:split at f^# needs sum_{j notin F} [phi_{z^#_j}(B_+(j)) + phi_{-z^#_j}(B_-(j))] = O(t): off the modified
coordinates phi_{z^#} = phi_z; at (C2) coordinates (raises, same sign) phi_{z^#}(x) <= 2 phi_{z}(x) (Z3 Lemma 3.2); at (C1) coordinates with
z_s eps >= 0 likewise; at the remaining modified coordinates (flipped (C1) coordinates, z_s eps < 0, the referee's definition, and the
(C3) coordinates) phi_{z^#}(x) <= 2|x|, and by Lemma lem:phicalc(b), |B_+(j)| + |B_-(j)| <= |Delta B(j)| + phi_{z_j}(B_+(j)) + phi_{-z_j}(B_-(j)),
so these coordinates cost at most 2 sum_j |Delta B(j)| + t/q_0.  On S^nat_{l''}, Delta B(s) = eps tau v(s) - r(s) and the flipped v-mass is
<= r^nat_{l''} <= b(w), so sum_{flipped} |Delta B| <= (6/t) b(w) sum lambda + 2t^7 <= t^2; at s_m only the donor (pinned, |Delta theta_c| <= K_P t)
and fine carriers live: |Delta B(s_m)| <= K_P t + t^7.  So chi, frak e_+- exist with ||frak e_+-||_1 <= K_U t + 2N K_P t + 3t/q_0.
Step 5 (data and estimates).  Define, AT f^#, omega^+_m := clamp of omega_{+,m} with gap^# (Definition def:windowcert) at the coarse
strict non-peaks of f^# carrying no kept switching, 0 at peaks of f^#, omega^+_m(k(l'')) := omega_{+,m}(k(l'')) at kept carriers and at the
repair carriers; omega^-_m := omega^+_m + sum_{l''} (eps tau'_{l''}/lambda_{l''}) e_{k(l'')}; b^+ := B_+ 1_F + chi V' - kappa^# a with
kappa^# := (B_+1_F + chi V')(zhat^#); b^- := b^+ - sum eps tau'_{l''} u_{l''}; g_t := b^+ + sum_m R_m^*(omega^+_m - d^#_m(omega^+_m) w^#_m).
At kept coordinates of types (K1), (K4) (q > 0) apply the shift of Theorem C Step 5 (Z6 referee Section 2): move omega^+-(k) by the
same x with vs x := (-1.5 gap^#/t - vs omega^-(k))_+, lambda_k |x| <= |tau_k - tau'_k| + lambda_k |Delta d| M; it leaves
omega^- - omega^+, Delta d^# and V' unchanged.  Then: two-piece admissibility at f^# and the second representation are those of
Lemma lem:windowtwopiece(a) (b^+ 1_{F^c} = chi V' z^#-signed, b^- 1_{F^c} = -(1-chi)V'); d-neutrality: d^#(omega^-) - d^#(omega^+) =
sum q^# tau' = Q^#_m(tau') = 0 (Step 3).  Estimates: as in Z3 Proposition T step (5) with K^#_* replaced by K_U: replacing (d, w, gap)
by (d^#, w^#, gap^#) costs C_f(t^{-1} + t^{-2} t) c(Delta) <= C theta_w t (Lemma 4.1), re-clamping costs (2/t) sum lambda|gap^# - gap| <=
C theta_w t; at dropped coordinates: pinned (Lemmas 3.1, 3.5, 3.6), and if the status changes between f and f^# the datum 0 is used
with error <= |tau| + lambda|Delta d| M (peak of f) or <= 2 lambda gap/t + |tau| + lambda |Delta d| M with gap <= b(w) (strict non-peak of
f, by the claim in the proof of Proposition prop:windowcert(c)); at (K4) coordinates omega^+ = omega_+ (no error) and the shift error;
Gamma: fix T3 of the Z3 referee.  This gives (i), (ii) with K_w <= C_f (1 + G**) (K_U + 1).  (iii): clamped coordinates are of kind [1];
(K2) have gap^# >= M^# u(w)/2 (Lemma 4.2(c)) and (K3) gap^# >= M^#/2, repair carriers fixed gaps: kind [2]; (K1), (K4) after the
shift: kind [3] (Z6 referee Lemma 2.1 / Y2 Lemma U'); |omega^+| <= 4/t, |tau_0|/lambda <= 12/t, and the repair amounts give
<= K_Q t Design(l) D(l)/u(w) <= 1/t (t in W(w), l large), so A_2 := 22.  QED
