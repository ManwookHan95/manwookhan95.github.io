# U1 part 4 — The companion: order of moves, the fine structure (gaps C*-2, C*-5), reference versus true coefficients

Setting: D^{U1} (part 3), N fixed, f with F finite, g in C(f), rho < 1; w a clean sub-window of a MAIN stage L >= l_f; an activity class a
(part 2.3) fixed, with active blocks A ⊂ I_sh(w), signs sigma_m := sgn(Delta'_m) (m in A), active coarse Omega-carriers Omega_act (sign
eps_l, class G), inactive ones (gamma = 0).  The class is ONE-SIGNED if all sigma_m (m in A) are equal: CONFIGURATION (i) if sigma = -1
(data shift Delta < 0: the blocks lack an upper source, I_up), CONFIGURATION (ii) if sigma = +1 (I_lo).  K = C_f (Design/u)^C as before.

## 4.1 The companion f^# (order of the moves)
(1a) V1's moves (C1) close class-G rooms on S^nat, (C2) close tiny target rooms, (C3) donor raise; then the realization of a Lojasiewicz
     point (u', kappa') of Gamma^#(kappa, a) (Theorem 2.3): Lemma TU (pulls and private banks on far parts of the signature sets of the
     carriers of Omega) for the values, and one push per block (Lemma 1.5: a bank at the first far coordinate of the buffer peak, or a
     move on a robust dropped strict non-peak) for kappa, solved by the intermediate value theorem up to the jumps caused by status
     changes of carriers at stages > L + R_cl (size <= C c_{L+R_cl+1}).
(1b) Absorbers: for every s in E_c(w) \ F^(1a), tune the first pair P(s) of Lemma 3.2 (block 1) to VALUE ZERO (Lemma 3.3): p_0, ..., p_R
     and the near part of S_a become support coordinates (masses >= theta_a = C_f lambda_a T_hi(w)), far part of S_a := +1.  Also tune all
     absorbers of the cluster of L to value zero (so that no cluster carrier changes status later).
(1c) Re-push kappa (one push per active block, Lemma 1.5) so that |kappa^# - kappa'| <= C c_{L+R_cl+1} (jumps of the intermediate value
     argument), then re-tune all tuned absorbers to value zero and, in configuration (ii), re-realize the values of Omega_act exactly
     (joint explicit fixed point of V1 Lemma TU: each target carrier is controlled at first order by its own masses, cross effects are
     second order in the corrections; geometric convergence).  The re-tuning moves kappa by a second-order amount << c_{L+R_cl+1}.
(2)  The FINE STRUCTURE on J_fine := N \ (F^(1b) ∪ E_c(w) ∪ (all coordinates fixed in (1a), (1b))): configuration (i): the robust
     recursion of 4.2; configuration (ii): the Schauder fixed point of 4.5.
Every move of (1a)-(1c) acts on coordinates distinct from those of the other moves (V1 3.2; absorbers' coordinates are private or in
their own signature sets).  J_fine is fixed after (1c); step (2) does not change the base part a^#, hence not e^#.

## 4.2 Lemma 4.1 (ownership; the robust recursion, configuration (i)).  PROVED.
A carrier k is an OWNER-CANDIDATE if its coefficient in V (Lemma 1.1(a)) is nonzero with a sign known in advance: (a) l in Omega_act (sign
eps_l); (b) coarse peaks of active blocks (coefficient -Delta''_m vs lambda: sign -sigma_m vs); (c) ALL TUNED absorbers: the used pairs
P(s) (biased coefficients >= c_0/4 > 0) and every other tuned absorber a, which gets the constant switching coefficient gamma_a := c_0(a) =
lambda_a 2^{-s_far(a)} > 0 [CORRECTION made in the final check: with gamma_a := 0 the far part of S_a, fixed at z = +1 in (1b), would carry
only later contributions of uncontrolled sign; with gamma_a = c_0(a) > 0 the absorber's own term dominates there by the biased-pair estimate
of 3.4, so z = +1 is admissible; its contribution at its own target coordinate s' lies on a support coordinate (s' in F^(1a)) or is part
of the residue absorbed by the first pair P(s') (Prop 3.4(a)); value zero keeps it free of d-effects (Lemma 3.3(iii))]; (d) fine carriers k (stages > L) of
active blocks other than tuned absorbers (coefficient -Delta''_m lambda_k w(k); sign -sigma_m varsigma_k, varsigma_k := sgn w(k), to be chosen).  For j in J_fine let own(j) := the least owner-candidate (in stage order) whose vector meets j.
Every j in J_fine either has an owner or meets no carrier with a nonzero coefficient; in the latter case V(Domega)(j) = 0 and z_j may
be chosen freely in [-1, 1] (admissible).  (By V2 Cor. C3.1(b) every coordinate meets carriers of every block at infinitely many stages,
so in fact owners exist whenever some block is active; the argument does not need this.)  Define recursively, along the stages k > L of class (d):
    O(k) := {j in J_fine : own(j) = k} (contains S_k ∩ J_fine = S_k: no earlier carrier meets S_k, allowedness (a));
    Y_k := u_k(zhat) computed with the coordinates of supp u_k \ O(k) (all fixed earlier, or owned by earlier candidates);
    varsigma_k := sgn Y_k (:= +1 if Y_k = 0);   z_j := sgn(-sigma_m varsigma_k u_k(j)) for j in O(k),
and for owners of types (a)-(c) put z_j := sgn(coefficient x u_own(j)(j)) on their owned sets (fixed already in (1a)-(1b) for (a), (c)).
In configuration (i) (sigma = -1) this gives z_j = varsigma_k sgn u_k(j) on O(k) (SELF-ALIGNED) and
    |u_k(zhat^#)| = |Y_k| + sum_{j in O(k)} |u_k(j)| >= ||v_k||_1 = delta_k H_k/n_k,                                        (4.1)
so k is a peak of f^# with sign varsigma_k and margin mu_k >= q^#_0 (delta_k H_k/n_k - theta^#_m Phi_k/m) >= q^#_0 delta_k H_k/(2 n_k).
Proof.  The recursion is well founded: Y_k uses only coordinates whose z is fixed before k is processed.  zhat^#_j = z_j on J_fine (j notin
F^#, diagonal base: (Ue)_j = mu_j^2 a^#_j/nu = 0).  With sigma = -1, z_j u_k(j) = varsigma_k |u_k(j)| on O(k), so u_k(zhat^#) = Y_k + varsigma_k
sum_{O(k)} |u_k(j)| has sign varsigma_k and modulus (4.1).  Peak criterion lem:threshold (V1 1.3): rho_k = |u_k| m/(Phi_k theta) >= 1; by (W3)
Phi_k <= c_k <= (delta_k H_k)^2, so theta Phi_k/m <= theta (delta_k H_k)^2 << delta_k H_k/n_k for stages > L >= l_f (theta^# <= C_f).  QED

## 4.3 Lemma 4.2 (dominance: the owner fixes the sign of V).  PROVED.
In the situation of 4.2 (configuration (i)), or for the fixed owners (a)-(c) in configuration (ii), for every j in J_fine owned by k:
    |coefficient_k| |u_k(j)| >= 2 sum_{k' later than k, u_{k'}(j) != 0} |coefficient_{k'}| |u_{k'}(j)|,
hence sgn V(Domega)(j) = sgn(coefficient_k u_k(j)) and z_j V(j) > 0: V is z^#-admissible at every coordinate of J_fine (all of them are
contacts of f^#).  The bound holds for every Delta'' in the class (active |Delta''_m| >= A_2 K T_lo(w)/2, |Delta''| <= C_f) and every
gamma(t) of the class (active |gamma_l| >= A_2 K T_lo(w)/2).
Proof.  Coefficients of carriers k' later than k are <= C_f lambda_{k'} (Lemma 2.1; absorbers' gamma <= C_f lambda_a, part 3.5(c)).
(i) j in S_k (signature coordinate of the owner): carriers k' > k meet j only through targets, allowed only if c_{k'} <= tau_k 2^{-2j} c_k
delta_k T_lo(k-1)^2/2 ((W4')); their total weight is <= (4/3) of the largest, so the right side is <= C_f tau_k 2^{-2j} c_k delta_k T_lo(k-1)^2,
while the left side is >= |coefficient_k| delta_k 2^{-j}/n_k with |coefficient_k| >= (A_2 K T_lo(w)/2) lambda_k M^#/... for type (d), >= A_2 K
T_lo(w)/2 for (a), >= c_0/4 for (c), >= (A_2 K T_lo(w)/2) lambda_k for (b).  Since T_lo(k-1) <= T_lo(w) (k - 1 >= L) and lambda_k = m 2^{-m-k(k)}
c_k with 2^{m + k(k) - j} <= 2^{m - k} (j >= 3 * 2^k), the ratio is <= C_f T_lo(w) 2^{m}/(A_2 K) < 1/2 for types (a), (b), (d); for (c):
j > s_far(a) and c_0 = lambda_a 2^{-s_far(a)} give ratio <= C_f 2^{m + k - (j - s_far(a))} T_lo^2 < 1/2.  For (a), (b) the owned signature
coordinates are the far ones (j > s_far(w)), where 2^{-j} <= b(w)^2 makes the ratio even smaller.
(ii) j a target coordinate of k (j in supp y_k, Z_0 or a coarser signature set): the left side is >= |coefficient_k| eta_k/n_k
(eta_k := least nonzero |y_k(j)|), the right side <= C_f sum_{k'>k} lambda_{k'} <= C_f c_{k+1} <= C_f b(k, M(k))^2 <= C_f 2^{-8 n(k)}, and
n(k) >= Design(k) >= 1/(eta_k lambda_k) (Design contains 1/eta and 1/Phi): ratio <= C_f 2^{-8 n(k)} T_lo(w)^{-1} << 1 (T_lo(w) >= T_lo(k)).
Owners of type (a), (b) have no target coordinates in J_fine (their targets lie in T(L) ⊂ E_c).  QED

## 4.4 Lemma 4.3 ((SC) at f^# for the negative blocks).  PROVED.
In configuration (i), the set I_- := A (all active blocks, Delta''_m < 0) satisfies the scrambling condition (SC) of def:SC at f^#, with
ANY sequence s_i -> 0.
Proof.  Fix m in A and Upsilon >= 1.  Carriers of block m at f^#: (1) coarse (stages <= L): finitely many; peaks have relative margin >=
u/2 (V2 (A2), V1 Lemma ST(c)), strict non-peaks have gap^# >= c_f Lam M^# or robust gaps (V1 Lemma ST(c)), no degenerate peaks; so for s
below a positive bound s_0(f^#) none of them contributes to Scr_m(Upsilon s).  (2) tuned absorbers: finitely many strict non-peaks with
gap >= 3M/4 (Lemma 3.3): no contribution for s < s_0.  (3) all other carriers of block m at stages > L: peaks with margin mu_k >=
q^#_0 delta_k H_k/(2 n_k) (Lemma 4.1).  A carrier of (3) contributes only if mu_k <= Upsilon s, i.e. delta_k H_k <= 2 n_k Upsilon s/q^#_0 =: X(s),
and then contributes min(Phi_k, Upsilon s) <= Phi_k <= c_k <= (delta_k H_k)^2 ((W3)).  The numbers a_k := delta_k H_k decrease super-
exponentially in k (delta_k <= 2^{-k}, H_k <= 2^{1 - 3 * 2^k}), so sum_{k : a_k <= X} a_k^2 <= 2 X a_{k(X)} <= 2 X^2, where k(X) is the least such
k.  Hence Scr_m(Upsilon s) <= C (Upsilon s/q_0)^2 = o(s) for s < s_0.  The sequence may be common to all m in A.  QED
Consequently thm:engineered applies at f^# to data with Delta_m < 0 exactly on A (I finite, F^# finite).

## 4.5 Lemma 4.4 (configuration (ii): exact completion by a fixed point, with the class fixed).  PROVED.
Let the class be of configuration (ii) and let all scales of the class carry the COMMON reference shift Delta'^* (part 2.4(c)).  Put
J_free := J_fine minus the owned sets of the fixed owners (a)-(c) (their signs are fixed by Lemma 4.2).  For z' in [-1,1]^{J_free}
let f(z') be the row with these coordinates replaced, and define the TRUE common shift Delta''(z') by (X3) at f(z') with the class's
gamma(t) (Lemma 4.6: Delta'' does not depend on t after (1c)) and the absorbers' coefficients gamma_abs(z') (part 3.5, continuous in the
residues, which are continuous in z').  Then the map
    Psi(z')_j := clamp_{[-1,1]}( z'_j + V(z')(j) ),   j in J_free,
V(z') := the fine part of V(Domega) at f(z') with shift Delta''(z') (coefficients -Delta''_m lambda_k w_m(z')(k) of the fine carriers of
active blocks), has a fixed point z'^*, and at f^# := f(z'^*) the vector V(Domega) is z^#-admissible on J_fine.
Proof.  As V2 Lemma C5 (refereed): [-1,1]^{J_free} with the product topology is compact convex metrizable; zhat(z') depends coordinatewise
continuously on z'; R_m^** zhat(z') is l_1-continuous by dominated convergence; the duality maps J_m are norm-to-weak* continuous (Lemma
A(d)), so w_m(z')(k) is continuous; V(z')(j) is a dominated series; Delta''(z') is continuous (kappa^#(z') is a continuous function of the
block data, which are continuous; the absorbers' coefficients are Lipschitz in the residues, Lemma 3.3).  Schauder-Tychonoff gives
z'^*; clamp(z_j + V_j) = z_j means V_j = 0 if |z_j| < 1 and z_j V_j >= 0 if |z_j| = 1.  On the owned sets of (a)-(c), Lemma 4.2.  QED
No (SC) is needed in configuration (ii): Delta_m >= 0 for all m, and cor:D1 applies at f^#.

## 4.6 Lemma 4.5 (cost and statuses of f^#).  PROVED.
p*(f^# - f) <= C_f Design T_lo^3 log(1/T_lo) + C_f T_lo^4 log(1/T_lo) + C_f c_{L+1} log(1/c_{L+1}) =: theta_w T_lo(w)^2 with theta_w -> 0;
the block data move by the same order; every coarse carrier keeps its status class (V1 Lemma ST), every robust minor of Gamma^# stays
>= u/(2 Design^C) (Theorem 2.3), and the statuses of the coarse carriers in Omega and of the coarse peaks are those used in Gamma^#.
Proof.  (1a): V1 Lemma CO (refereed) and Theorem 2.3 (moves <= T_lo^4).  (1b), (1c): the absorbers' values move by O(1), cost <= C sum
lambda_a <= C c_{L+1}; masses <= C_f c_{L+1} T_hi.  (2): Z3 Lemma 3.1 with delta = zhat^# - zhat^(1b) supported in J_fine: coarse carriers
meet J_fine only in the far parts of their signature sets (2^{-s} <= 2^{-s_far(w)}), so |u_{l''}(delta)| <= 4 delta_{l''} 2^{-s_far(w)}; carriers at
stages > L contribute <= sum lambda <= c_{L+1}.  c_{L+1} <= b(L, M(L))^2 <= T_lo(w)^8.  Statuses: V1 Lemma ST with the extra drift
C c_{L+1} << Lam.  QED

## 4.7 Lemma 4.6 (reference versus true coefficients; the true shift).  PROVED.
Let (Delta'(t), gamma(t)) in Gamma^#(u', kappa', a) be the reference coarse data of a scale t (projected, and normalized in configuration
(ii)).  The data at f^# with switching gamma(t) on Omega_act (0 on inactive members of Omega, c_0(a) on the other tuned absorbers, the biased
coefficients on the used pairs) have TRUE shift Delta''(t) given by (X3) at f^#:
    Delta''_m(t) kappa^#_m = sum_{l in Omega_act, m(l) = m} u_l(zhat^#) gamma_l(t)        (absorbers contribute 0: value zero, Lemma 3.3(iii)).
Then
(a) |Delta''_m(t) - Delta'_m(t)| <= C_f ( |kappa^#_m - kappa'_m| + ||u^# - u'||_{Omega_act} ||gamma(t)||_1 ) <= C_f Design c_{L+R_cl+1} + C_f c_{L+1}^2/t;
    in configuration (ii) the middle term vanishes (step (1c)), so Delta''(t) = Delta'^* kappa'/kappa^# =: Delta''^* is the SAME for all t of
    the class;
(b) L(Delta''(t), gamma(t)) differs from the admissible L(Delta'(t), gamma(t)) by sum_m (Delta''_m - Delta'_m) P_m, P_m := the coarse peak traces
    of block m restricted to E_c; on the near signature sets of the coarse peaks the total coarse value is the peak's own trace
    -Delta''_m vs lambda v_l(s), of the same sign as -Delta'_m vs (|Delta'' - Delta'| < |Delta'|/2), hence admissible; on T(L) the difference is
    absorbed by the cluster pairs (Proposition 3.4, cluster capacity >= c_{L+1}/(Design T_hi(w)) against a correction <= C_f Design c_{L+1});
(c) the signs and activity of Delta''(t) are those of Delta'(t) (active |Delta'_m| >= A_{i+1} K t/2 >> the bound in (a), since c_{L+1} <= T_lo^8).
Proof.  (a) Subtract (X3) at (u', kappa') from (X3) at (u^#, kappa^#) and divide by kappa^# >= A^# >= c_f.  |kappa^# - kappa'|: after (1c),
<= C c_{L+R_cl+1} (jumps: only carriers at stages > L + R_cl can change status under the push, since the cluster carriers are tuned to value
zero with gap M and the coarse carriers have robust margins/gaps); step (2) changes the block data by <= C (sum_{stages > L+R_cl} lambda +
2^{-s_far(w)}) <= C c_{L+R_cl+1} (Lemma 4.5; coarse carriers meet J_fine only beyond s_far, 2^{-s_far} <= c_{L+1}^2... and cluster carriers do
not meet J_fine except in their far signature parts, fixed at +1 or owned with gamma = 0); kappa is Lipschitz in the block data with
constant <= Design/u (Lemma 1.2: (A, theta) solve (E1), (E2), a nonsingular system at f^# with Jacobian bounded below by Phi_P^2 >= D(L)^{-2}).
||u^# - u'||_{Omega_act}: exact after (1a); (1b), (1c) second-order Hilbert effects <= C (sum masses x mu)^2 <= C c_{L+1}^2; step (2) does not
change u_l (l in Omega_act): their vectors meet J_fine only in their own far signature parts, owned by l with the sign eps_l fixed since
(C1).  In configuration (ii), (1c) re-realizes u^# = u' exactly; kappa^# is common to all scales.
(b) L is linear in Delta'; coarse peaks are the only coarse carriers whose coefficient depends on the shift; on S^nat of a peak only the
peak lives among coarse carriers ((P1), allowedness (a)).  (c) The gaps of the thresholds (2.3).  QED
