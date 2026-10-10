# U1 part 3 — The design D^{U1} (zero-value absorbers) and exact absorption on the coarse coordinates (gap C*-1)

Base design: U4's T_final (r8/U4_notes.md Section 1: D^mu base mu_s = 2^{-s^2-1}, SLD with S_l = {2^l(2i+1)}, allowedness (a), (c),
weights (W1)-(W7), sub-windows at every stage, rate objects (R1)-(R7) + V2's determinantal and shift objects).  D^{U1} changes the TARGET
schedule (step (1) of T_final), makes the ladder bijection adaptive, adds rule (c''), and modifies the weights at two kinds of stages.
Everything else of T_final is kept.  Labels PROVED / SKETCH / OPEN.  (This version supersedes an earlier draft with absorbers in every
block, whose request queue grew faster than the number of stages.)

## 3.1 Definition of D^{U1}
(A0) ABSORBER TARGETS.  For a coordinate s, a sign beta in {+1,-1} and a stage p, an absorber target is y := x/q^*(x) with
       x := beta e_s^* + e_{p_0}^* + 4 sum_{r=1}^{R} 2^{-r} e_{p_r}^*,
     p_0 < p_1 < ... < p_R FRESH odd integers (in no S_l and in no earlier target), and R = R(p) := the least integer with
     2^{3-R} <= mu_{p_0}^2 c_p^2/4.  Then |y(s)| = 1/q^*(x) in [1/8, 1].  An absorber target is allowed at p (T_final's (a): s is in Z_0 or in
     some S_{l'} with l' < p; (c): s <= p).  p_0 is the CONTINUOUS TUNING coordinate, p_1..p_R the BINARY coordinates.
(A1) MAIN STAGES and CLUSTERS.  After every main stage L, the next stages form a CLUSTER: for every coordinate s in
     E^ch(L) := T(L) ∪ union_{l'' <= L} (S_{l''} ∩ [1, L]) one BIASED PAIR of block 1 (two carriers with absorber targets for (s, +1) and
     (s, -1)), consecutive, in any order; R_cl(L) := 2|E^ch(L)|.  The ladder bijection is chosen adaptively (j(k,1) for the cluster).
(A2) DEEP PAIRS.  For every even s in some S_{l'} one biased pair of block 1 for (s, +-1) is placed at stages in [s, psi^{-1}(s)), where
     psi(p) := floor(p^{1/2}/4); and (c'') a MAIN target placed at stage p may meet S_{l'} only in [1, psi(p)] (this strengthens (c)).
(A3) SCHEDULE.  At a stage of block m: if a cluster is open, serve it (block 1); else serve the oldest pending deep request of block m (if
     m = 1 and one is due); else place T_final's main target if allowed, else an FD target (fresh odd coordinate; always allowed).
(A4) WEIGHTS.  Cluster stages: c_{L+i} := c_{L+1} 4^{1-i} (1 <= i <= R_cl), where c_{L+1} is the minimum of T_final's (W1)-(W7) at stage L+1
     taken over all coordinates s of E^ch(L) in (W4).  All other stages: T_final's rule with (W4) strengthened to
       (W4'')  c_l <= tau_{l'} 2^{-2s} c_{l'} delta_{l'} T_lo(l-1, M(l-1))^3/2   for l' < l and s in supp y_l ∩ S_{l'}.
     Design(L) at a main stage L additionally contains 4^{R_cl(L)}, 2^{k(L+R_cl)} (block-1 index), 1/eta_L and the counts D_cls(w) of
     part 2; Q(w) is enlarged so that Q(w) >= D_cls(w)^2 (Design(L)/u(w))^{C} for the constant C of part 2 (design requirement; the
     square is used by the pigeonhole of Master Theorem IV, part 5.6).
WINDOWS ARE USED ONLY AT MAIN STAGES.

## 3.2 Theorem 3.1 (admissibility, N-freeness, survival).  PROVED.
(a) T(D^{U1}) satisfies (T-a)-(T-d) of def:admissible (so the conclusion of Martin's Lemma B), (P1), and at every main stage L:
    sum_{l' > L} lambda_{l'} <= b(L, M(L))^2/2 <= T_lo(w)^8 (w of level L).
(b) D^{U1} does not depend on N (block 1 is present in every p_N).
(c) Every refereed result used in parts 1, 2, 4 (U4's dependency trees of Master Theorems II, III', V1 Lemmas B, DR, TU, CO, ST, NS, RR,
    Proposition TR, Theorem E'', V2 Lemmas H, L, QB, 2.3, Theorems B, C1, Lemma C5, Z3 Lemma 3.1, Theorem E, Lemma U, the note's lemmas)
    holds for D^{U1} with "level" read as "main stage".
Proof.  (a) (T-a): q^*(Te) = c <= 1.  (T-b), (T-c): T_final's argument (U4 Theorem 2.2) at the least stage L(s) of a target meeting
s in S_{l'} uses only allowedness (a) and (W4); absorber targets satisfy (a), cluster weights satisfy (W4) by the choice of c_{L+1}, other
stages satisfy (W4'') ⊂ (W4).  (T-d): every request is finite and the schedule (A3) serves requests in order; deep requests created up to
stage S number <= 2 psi(S) + 2 + (S^{1/2}) (coordinates s with psi^{-1}(s) <= S), so main stages are not starved: in every block,
infinitely many stages place main or FD targets; a target y^(i) touching finitely many signature coordinates is allowed at all large
stages (c'') once their deep pairs exist; hence y_l = y^(i) at infinitely many stages of each block, and density follows as in T_final.
(P1) as T_final.  (P2) at a main stage L: sum_{l'>L} c_{l'} <= c_{L+1} sum_i 4^{1-i} + (4/3) c_{L+R_cl+1} <= 2 c_{L+1} <= 2 b(L, M(L))^2 ((W2)).
(b) Requests concern block 1 and coordinates; for p_N absent carriers are omitted (as T_final).
(c) U4's Lemma GW: window arguments use one window's dyadic scales, design factors of the level, the box bound (which needs (a)), and
T_hi(next) <= T_lo(previous); all hold at main stages.  Non-window arguments use (T-a)-(T-d), (P1), (P2), allowedness (a), (b) as a
property of (y_l, c_l), (c) (implied by (c'')), bounded gaps, the mu-base, the design factors.  Absorbers are ordinary SLD carriers.  QED

## 3.3 Lemma 3.2 (first touchers).  PROVED.
Let w be a sub-window of a main stage L, s_far(w) the least s with 2^{-s} <= c_{L+1}^2 (so 2^{-s_far} <= b(w)^4), and
E_c(w) := T(L) ∪ union_{l'' <= L} (S_{l''} ∩ [1, s_far(w)]).  For every s in E_c(w), among the carriers at stages > L whose vectors meet s,
the first two form a biased absorber pair for s (a cluster pair of some main stage L' >= L with s in E^ch(L'), or the deep pair of s).
Proof.  If s in E^ch(L), the cluster of L follows L immediately.  If s in S_{l''} ∩ (L, s_far]: a target at a stage p meets s only if
s <= p ((c)) and, if it is a main target, s <= psi(p) ((c'')), i.e. p >= psi^{-1}(s), after the deep pair; FD targets meet only fresh odd
coordinates; signature vectors meet s only for l'' itself; absorber targets meet only their own s' and fresh coordinates.  So the first
carrier after L meeting s is an absorber for s (deep pair, or a cluster pair of a main stage L' with s <= L'), and pairs are
consecutive.  QED

## 3.4 Lemma 3.3 (zero-value tuning of an absorber; biased pair).  PROVED.
Let f^(1) be a companion with finite base support not containing the coordinates p_0, ..., p_R, nor S_a ∩ [1, s_far(a)] (s_far(a): least s'
with 2^{-s'} <= Phi_a^2), and with s notin F^(1).  Put z := +1 at p_0, sigma' := +1 on the near part S_a ∩ [1, s_far(a)], z := +1 on the far
part of S_a, and choose binary signs sigma_r (r >= 1) with
    0 <= Target - 4 sum_r 2^{-r} sigma_r <= 2^{3-R},   Target := -( beta zhat_s + 1 + q^*(x) delta_a h_a(zhat) )
(possible: the binary sums run through the odd multiples of 2^{2-R} in (-4, 4), and Target in [-3.5, 1.5] because zhat_s = z_s (s notin
supp a), |z_s| <= 1, and q^*(x) delta_a ||h_a||_1 <= ||x||_1 (1 + ||U||) delta_a H_a <= 7.5/5 = 1.5 by the choice of delta_a in def:SLD; round DOWN).  Put masses theta_a sigma_r at p_r (r >= 1), theta_a sigma' at the near part of S_a, and
m_0 at p_0 with m_0 in [theta_a, theta_a + c_p^2] (all become support coordinates), theta_a := C_f lambda_a T_hi (the window's T_hi; any
theta_a in (0, lambda_a] works for (i)).
(i) There is m_0 in [theta_a, theta_a + c_p^2] with u_a(zhat) = 0 EXACTLY; a is a strict non-peak with w(a) = 0 (gap M);
(ii) for finitely many absorbers tuned simultaneously, the masses m_0 can be chosen to make all values exactly 0 (contraction);
(iii) a carries no d-effect: u_a(zhat) gamma_a = 0 in (1.3), and nu_a = 0 contributes nothing to kappa (Lemma 1.3, Lemma 1.2);
(iv) cost p*(f^(2) - f^(1)) <= C (lambda_a + sum masses); the other carriers' values move by the second-order Hilbert effect
     <= C (sum masses x mu)^2 (diagonal base, Lemma B of V1), except carriers at stages > p whose targets meet the p_r or near S_a.
Proof.  (i) q^*(x) n_a u_a(zhat) = beta zhat_s + zhat_{p_0} + 4 sum 2^{-r} zhat_{p_r} + q^*(x) delta_a h_a(zhat), with zhat_{p} = z_p + mu_p^2 m_p
z_p/nu at support coordinates (diagonal base; U4 1.1) and zhat = z on S_a's far part and at s (not in the support).  With m_0 = theta_a the
bracket equals -(Target - binary sum) + O(mu^2 theta) in [-2^{3-R} - eps, eps]; raising m_0 by Theta raises zhat_{p_0} by mu_{p_0}^2 Theta/nu' (nu'
changes by a second-order amount), so Theta in [0, c_p^2] sweeps an interval of length >= mu_{p_0}^2 c_p^2/2 >= 2^{4-R} upward, which contains
the value cancelling the bracket; the intermediate value theorem gives u_a(zhat) = 0 exactly.  lem:threshold: zeta(a) = 0 < theta Phi^2, so
a is a strict non-peak with w(a) = 0.
(ii) Each absorber's value depends at first order only on its own m_0 (diagonal base: the other masses enter through nu, a second-order
effect of size <= C (sum masses mu)^2 << mu_{p_0}^2 c_p^2); the joint system is solved by the explicit fixed point of V1 Lemma TU, Step 2.
(iii) Lemma 1.3 and (E1), (E2): a strict non-peak with nu = 0 contributes 0.  (iv) Z3 Lemma 3.1 / U4.  QED
BIASED PAIR.  For a pair (a^+, a^-) and a residue r at s put gamma_{a^+} := c_0 + (-r)_+/|y_{a^+}(s)|, gamma_{a^-} := c_0 |y_{a^+}(s)|/|y_{a^-}(s)| +
r_+/|y_{a^-}(s)|, c_0 := lambda_{a^-} 2^{-s_far(a^-)}.  Then gamma_{a^+} y_{a^+}(s) + gamma_{a^-} y_{a^-}(s) = -r, both coefficients are >= c_0/4,
Lipschitz in r, and on the far parts of S_{a^+-} the absorber's own term gamma_a v_a(s') dominates every later carrier ((W4''): ratio
<= C_f 2^{s_far(a) - s'} T_lo^3 2^{1+k(a)} < 1/2), so z = +1 there is admissible whatever r is.

## 3.5 Proposition 3.4 (exact absorption on E_c).  PROVED (given parts 2 and 4).
Let w be a clean sub-window of a main stage L >= l_f and f^# the companion of part 4, at which the first pair P(s) of Lemma 3.2 is tuned
(Lemma 3.3) for every s in E_c(w) \ F^#.  Let rho(s) := V(Domega)(s) - L(Delta'', gamma)(s) - (contribution of P(s)), the RESIDUE at s
(L(Delta'', gamma): the coarse vector of part 2 with the true shift Delta'' of Lemma 4.6).  Then:
(a) rho(s) = the sum of (coefficient) u_k(s) over carriers k after P(s) (Lemma 3.2), so |rho(s)| <= C_f sum_{k after P(s)} lambda_k; on T(L)
    also the trace correction of Lemma 4.6(b) is absorbed: |(Delta'' - Delta') P(s)| <= C_f Design c_{L+1};
(b) the biased coefficients with r := rho(s) (+ trace correction) make V(Domega)(s) EXACTLY equal to L(Delta'', gamma)(s), which is
    z^#-admissible (part 2 (X1), Lemma 4.6(b));
(c) CAPACITY: |Domega(a)| = |gamma_a|/lambda_a <= A_2/t for t <= T_hi(w) (w(a) = 0), i.e. kind [2] of V1 TR(iii) (gap = M);
(d) data at the support coordinates p_r, near S_a satisfy t|b| <= m_r (no flips), and the masses cost <= C_f c_{L+1} T_hi + C c_{L+1}^2;
(e) the pairs carry no d-effect (Lemma 3.3(iii)).
Proof.  (a) Lemma 3.2 and Lemma 1.1(a); coefficients of later carriers are <= C_f lambda (Lemma 2.1: |Delta''| <= C_f) or gamma <= C_f lambda for
later absorbers.  (b) The biased pair.  (c) Cluster pairs: lambda_a >= 2^{-1-k(a)} 4^{1-R_cl} c_{L+1} >= c_{L+1}/Design(L), while
sum_{k after the cluster} lambda_k <= 2 c_{L+R_cl+1} <= 2 b(L+R_cl)^2 << c_{L+1}/Design and the trace correction is <= C_f Design c_{L+1}; so
|gamma_a|/lambda_a <= C_f Design^2 + 1 << A_2/T_hi(w) (Q(w) >= (Design/u)^C).  Deep pairs (stage p >= s): the residue comes only from
later carriers, sum lambda <= 2 c_{p+1} <= 2 b(p)^2 <= 2^{1-8 n(p)} << lambda_a = 2^{-1-k} c_p (n(p) >= Design(p) >= 2^{k+1}/c_p);
s is not in T(L) (s > L), so no trace correction.  (d) b(p_r) = (coefficient of u_a) u_a(p_r) = gamma_a 2^{1-r}/(q^*(x) n_a): t|b| <=
C_f lambda_a T_hi = theta_a <= m_r.  (e) Lemma 3.3(iii).  QED
Remark.  E_c(w) is finite; F^# stays finite; the absorbers are strict non-peaks with w = 0 (gap M): harmless for (SC) (part 4) and
for Lemma U (kind [2]).  Zero-value absorbers are what makes ONE pair per coordinate (in block 1) sufficient: a pair of a non-shifted
block would otherwise shift that block through (1.3).
