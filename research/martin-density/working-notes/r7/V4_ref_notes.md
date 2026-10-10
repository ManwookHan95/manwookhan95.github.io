# V4 referee notes (Round 7): proofs of all fixes and additions

Refereed: r7/V4_notes.md (+ V4_part1..5, V4_work/*.py).  Part files of this referee: r7/V4_ref_part1..5.md; scripts:
r7/V4_ref_work/{sa_check_mp.py (mpmath version, not runnable here), sa_check_dec.py + decimalmp.py (120-digit decimal re-run)}.
Setting: paper/martin_density_note.tex (Sections 1, 7, 8), finite I = {1, ..., N}, p = p_N; refereed Rounds 5-7 (Z3 Lemma U, Lemma 3.1;
Y4-ref Lemma P2; V1/V2 referee reports).  "SLD-type design" as in V4.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 0. Summary of fixes and additions
| # | object | status after fix |
|---|---|---|
| R1 | Remark 2.3(1): weak swallowing-type peak in self-aligned form (proof gap: coarse switches along the sweep) | PROVED (hysteretic sweep + approximate IVT) |
| R2 | Proposition 2.4 literally false (earlier entries uncontrolled) | PROVED with i(j) := first non-zero index |
| R3 | owners/recursions for p_N must be relative to L_N (absent carriers would act as neutral owners) | PROVED; all of V4 holds for every N |
| R4 | Lemma 1.3, second bound omits the q > 0 swallowed non-peaks | PROVED corrected bound |
| R5 | NEW: exact all-negative two-piece data are meagre in every fixed-z fibre | PROVED |
| R6 | Lemma 2.1: order of choices in the modified recursion | PROVED |
| R7 | Lemma 3.8: nonincreasing majorant; common sequence | PROVED (single block); ladder version stated |
| R8 | Lemma 3.6 with banks: rebalance with a 1_F | PROVED |
| R9 | Corollary 5.7 for N >= 2 | PROVED with Delta d_m < 0 in every block |
| R10 | Theorem 5.6 forces maximal contact | PROVED (scope lemma) |
| R11 | tau_l -> 0 must be part of (SF_tau) | design precision |

## R1. Weak swallowing-type peak (repairs Remark 2.3(1)).  PROVED.
Setting: design with (SF*), (Z0) containing p, p', p'', p''' and targets y* = (e_p^* - e_{p'}^*)/q*, y** = (e_{p''}^* - e_{p'''}^*)/q*; diagonal U; block
m_0 <= N; carriers l_- (target y*), l_D (target y**) of block m_0; F = {p, p', p'', p'''}.
Lemma R1.  For every xi in (0, 1) and epsilon > 0 there is a first row with supp a = F in which every carrier of L_N is swallowed with its own
sign (z = sgn val_l on S_l), l_- is a strict non-peak with q < 0, l_D has relative margin g = (nu_D - theta)/theta in [xi - epsilon, xi], and every
other carrier is a non-degenerate swallowing-type peak with n_l|val_l| >= (B_l + delta_l H_l)/2; Steps 6-7 of Theorem 2.2 hold (W-sums
z-signed, c_*(l) = 0 in block m_0).
Proof.  (1) b in Omega (open positive orthant of S^3), zhat_j = 1 + s_j b_j on F.  n_- val_- = c*(s_p b_p - s_{p'} b_{p'}) + delta_- H_- and n_D val_D =
c**(s_{p''} b_{p''} - s_{p'''} b_{p'''}) + delta_D H_D (eps = +1 on S_-, S_D).  The two linear forms are independent on the tangent space of S^3 at
every b in Omega (a relation alpha L_1 + beta L_2 + gamma b = 0 forces gamma(b_p/s_p + b_{p'}/s_{p'}) = 0, hence gamma = alpha = beta = 0), so there is
a smooth curve x -> b(x), |b'| <= C_b, along which n_- val_- = -eta (eta < n_- theta_0 Phi_-/(2m_0), theta_0 := lambda_{l_c} delta°_{l_c}/2) and
n_D val_D = x_0 + x; the base point lies in a fixed compact subset of Omega as l_D -> infinity (delta_D H_D -> 0), so C_b does not depend on l_D.
(2) At x = 0 build the row by the pure owner rule over L_N (eps_- = eps_D = +1); for x != 0 by the hysteretic rule with reference signs from
x = 0 (flip eps_l only if eps^0_l A_l(x) <= -(B_l + delta_l H_l)/2, then eps_l := sgn A_l(x)).  Every carrier other than l_-, l_D has
n_l|val_l| >= (B_l + delta_l H_l)/2 with sign eps_l, so Step 4 of Theorem 2.2 (with delta°_l/2) makes it a non-degenerate swallowing-type peak,
and Steps 6-7 apply (they only use z_j = eps_o sgn u_o(j) at owner coordinates).
(3) No flip below l_D.  Let theta^max := m_0(1 + ||U||)/Phi_{l_1} (l_1 the first carrier of block m_0, a peak, so theta < nu_{l_1}) and R :=
4 n_D theta^max Phi_D/m_0.  For l < l_D, A_l depends on x only through zhat_F (its other coordinates are owned by carriers < l, none of which flips
— induction), |A_l(x) - A_l(0)| <= 2 max s C_b |x|, and a flip needs >= delta_l H_l/2.  By (SF*) second half, c_{l_D} <= c_l/4 <= delta_l H_l 2^{-l-12}
(l >= 2), so 2 max s C_b R <= C'' 2^{-l} delta_l H_l/Phi_{l_1} < delta_l H_l/2 for l > L_1 := log_2(2C''/Phi_{l_1}); for the finitely many l <= L_1 the
same holds once c_{l_D} is small, i.e. l_D late.  So no carrier l < l_D flips for |x| <= R.
(4) Approximate IVT.  g(x) := nu_D(x)/theta(x) - 1 with nu_D = m_0(x_0 + x)/(n_D Phi_D); choose x_0 with nu_D(-R/2) <= theta/2, nu_D(R/2) >= 2 theta at
all rows of the family (theta varies by a relative amount -> 0 over |x| <= R).  For |x|, |x'| <= R: carriers < l_D (other than l_D) have values
continuous in x, carriers > l_D have |val| <= 1, so ||zeta(x) - zeta(x')||_1 <= C_3|x - x'| + 2 sum_{l > l_D} lambda_l, and by Lemma 5.2(a)
|theta(x) - theta(x')| <= L_Theta(C_3|x - x'| + 2 sum_{l>l_D} lambda_l).  Let x* := sup{x in [-R/2, R/2] : g(x) <= xi} (< R/2 since g(R/2) >= 1); pick
x' <= x* < x'' arbitrarily close to x* with g(x') <= xi < g(x'').  Since nu_D(x')/theta(x') <= 2,
|g(x'') - g(x')| <= C_4|x'' - x'| + 2|theta(x'') - theta(x')|/theta_0 -> <= 4 L_Theta sum_{l > l_D} lambda_l/theta_0 =: epsilon'.  So g(x') in [xi - epsilon', xi] for
x' close to x*; epsilon' <= epsilon for l_D late.  val_D > 0 throughout, so l_D is swallowing type (peak iff g >= 0).  QED
(Exact degeneracy g = 0 is not obtained: the jump part of theta may skip it.  V4's OPEN label stands.)

## R2. Single-vector principle (corrects Proposition 2.4).  PROVED.
Literal statement is false: V_1(j) = 10, V_2(j) = -1, V_i(j) = 0 (i >= 3); i(j) = 2 satisfies the hypothesis, z_j := -1, but (V_1 + V_2)(j) = 9.
Correct statement: let F be finite and V_i in l_1; for j notin F let i(j) be the FIRST index with V_i(j) != 0 and assume |V_{i(j)}(j)| >
sum_{i > i(j)} |V_i(j)| whenever i(j) exists.  Put z_j := sgn V_{i(j)}(j) (any value in [-1,1] if no V_i(j) != 0).  Then every partial sum
sum_{i <= n} V_i, and every sum sum_i rho_i V_i with rho_i in [1/2, 1] if the factor 1 is replaced by 2, is z-signed off F.
Proof: at j, terms with i < i(j) vanish; for n >= i(j) the sum has the sign of its first term, which dominates the rest; for n < i(j) it is 0.

## R3. Owners relative to L_N.  PROVED.
For p_N put L_N := {l : m(l) <= N} and o_N(j) := min{l in L_N : u_l(j) != 0}.  Every coordinate has o_N(j) (Lemma 1.2(b) applied to block 1).
Run Construction SA, the fine re-alignment (Theorem 3.5), the hysteretic re-runs (Prop. 5.3, Lemma 4.4, Lemma 5.5) over L_N only.
Claim: every statement of V4 holds for every N with o_N in place of o.  Proof: (i) a present carrier's signature set is unassigned at its own
step (allowedness (a) and disjointness), so every present carrier is swallowed with its own sign; (ii) a coordinate j with o_N(j) = o is either
in S_o or in supp y_o \ S_o (the latter covers j in Z_0 and j in S_l with l absent); in the second case it is unassigned at step o (no earlier
present carrier contains it), so z_j = eps_o sgn y_o(j); (iii) all dominance estimates (Step 6 of Theorem 2.2, Lemma 4.1') bound the later
contributions by sums over ALL later carriers ((SF*), (SF_tau)) or by allowedness (b), (b'), hence a fortiori over present ones; case (iii) of
Lemma 4.1' needs only |y_o(j)| >= eta_o; (iv) Steps 3-5, 8 of Theorem 2.2 involve only block-m carriers.  Why it is needed: with the all-carrier
recursion a coordinate owned by an absent carrier o receives z_j = eps_o, while every quantity of p_N (the vector of c_*(l), the d-row
D = sum_{k in L_N} gamma_k u_k) is dominated at j by o_N(j), whose sign eps_{o_N} sgn y_{o_N}(j) is unrelated to eps_o; Theorem 2.2(e) and the
(T2) verification of Lemma 5.4 would fail there.  The design itself stays N-independent; only the row construction depends on N.

## R4. Lemma 1.3, corrected second bound.  PROVED.
In the setting of lem:peakshift at t in W(l_*), t <= min(t_eta, 1), with good pinning bound K* t, for every block m:
 Delta d_m M_m (1 + sum_{l in Pk} q_l lambda_l) <= sum_{l in B, l <= l_*, q_l < 0} |q_l|(tau_l)_+ + sum_{l in B, l <= l_*, q_l > 0, l notin Pk} q_l (tau_l)_-
                                                + (K* t + 6t^2)/(m C_m) + 2t/sigma_m,
and consequently, using |q_l| <= Phi_l M_m/(m C_m) and (tau_l)_+-, <= |Delta theta_l| <= 6 lambda_l/t (lem:box),
 Delta d_m M_m <= (6 M_m/(C_m t)) sum_{l in B ∩ [1, l_*], m(l) = m, l notin Pk} Phi_l^2 + (K* t + 6t^2)/(m C_m) + 2t/sigma_m.
Under (H1) of def:swallowed, lem:modswallow(b) gives sum (tau_l)_- <= K* t and the q > 0 part is <= K* t/(m C_m); only then is the shift "fed only by
negative d-weights".  (Proof: V4's, plus the two displayed bounds.)

## R5. Exact all-negative data are non-generic.  PROVED (new).
Assume (SF_tau), (b'), tau_l -> 0 (R11), U diagonal, F finite with d = |F| >= 2, sigma, z with z = sigma on F, A as in Prop. 5.1.
Proposition R5.  The set of a in A for which some g in C(f_a) carries two-piece data with Delta d_m < 0 for every m in I is meagre in A.
Proof.  In Omega, for a carrier l of block m let O_l := {b : 2 tau_l theta_m Phi_l/(m M_m) < |val_l(b)| < theta_m Phi_l/(2m), and some j in S_l \ F has
z_j != sgn val_l(b)} (open).  Density of V^m_L := union_{l >= L, m(l) = m} O_l: given b_0 and a connected open O, take y and carriers l_i as in
Prop. 5.1(2) (val_{l_i} = +-c_0/2 at b_+- in O, S_{l_i} ∩ F = {}).  Let eps_i := the constant value of z on S_{l_i} if z is constant there, eps_i := 1
otherwise; kappa_i(b) := midpoint of the window (positive, continuous, O(Phi_{l_i})); the window is non-empty for i large (2 tau_{l_i}/M_m < 1/2).
h := val_{l_i} + eps_i kappa_i has sign eps_i at the end where val = eps_i c_0/2 and sign -eps_i at the other end (kappa_i < c_0/2), so h(b) = 0 at some
b in O: val_{l_i}(b) = -eps_i kappa_i(b) lies in the window with sign -eps_i, and (ii) holds; b in O_{l_i}.  G := intersection_m intersection_L V^m_L is a
dense G_delta.  If b(a) in G and data with all Delta d_m < 0 exist, let |Delta d_{m*}| = C_1; pick l of block m* with b in O_l, l notin K_omega,
S_l ∩ (F ∪ E) = {} (all but finitely many).  Then nu_l < theta/2 (strict non-peak) and |w(l)| = M nu_l/theta > 2 tau_l, so |gamma_l| = lambda_l C_1|w(l)| >=
2 tau_l C_1 lambda_l (not neutral, not negligible); for j from (ii), o_N(j) = l, and Prop. 4.2' gives z_j = sgn(gamma_l v_l(j)) = sgn(-Delta d_{m*} w(l)) =
sgn val_l, contradicting (ii).  QED
Consequences: Theorem 5.6 / Corollary 5.7 act on a meagre subset of each fibre (like (BT), Prop. 5.1); the GENERIC row has no exact
all-negative data, so its mates must be handled by window data — the residual there is V2-ref's (C*), not the dead zones of Section 12.

## R6. Lemma 2.1: the modified recursion.  PROVED.
Stage l (after all data of levels < l): (1) S_l (fixed in advance, inside N \ Z_0); (2) delta_l in [delta^max_l/2, delta^max_l] avoiding the
finitely many (GM)-intervals (g_l small); (3) y_l := the scheduled target if it satisfies allowedness (a), else y^(1); the (FD) targets
(e_j^* + r)/q*(.) with j in Z_0 fresh and r supported in Z_0 are interleaved at infinitely many stages of every block, keeping every scheduled
target infinitely often in every block; (4) n_l, u_l, eta_l, g_l; (5) c_l := minimum of: the design's own bound (e.g. c_{l-1}/4, T_lo(l-1)^3,
Design-dependent bounds), allowedness (b), (b'), (SF*) second half, Phi_l <= g_l 2^{-l}, and the (SF*)/(SF_tau) first-half bound imposed by level
l-1 (an upper bound on c_l in terms of level-(l-1) data via sum_{l'' >= l} lambda_{l''} <= c_l/3); (6) the level-l window and Design constants.
Every condition is an upper bound on c_l by a positive number computable at that point; (T-a)-(T-d) and (P1)-(P3) are proved as in thm:SLD
(allowedness (b) now always holds, so (T-d) is easier); no result of Section 8 or Rounds 5-7 uses a lower bound on c_l.

## R7. Lemma 3.8 with a monotone majorant.  PROVED (single block).
Replace eps_k by a NONINCREASING summable majorant of (Phi_m(k+1)/Phi_m(k))^{1/2}; under (SF*), Phi_m(k+1)/Phi_m(k) <= c_{l+1}/(2c_l) <= 2^{-2l-14}
(l = j(k,m); delta_{l+1} <= 2^{-l-1}, min S >= 1), so eps_k := 2^{-j(k,m)-7} works.  Then the proof is V4's: carriers k <= L with |nu_k - theta| <=
eps_L/kappa satisfy |nu_k - theta| <= eps_k/kappa, finitely many by hypothesis, each with nu_k != theta (no degenerate peak), so none for L large.
For several blocks one needs a common sequence (def:SC); the ladder version (scales between consecutive ladder weights, with the same
majorant) is a routine extension, not needed by V4 since Theorem 5.6 uses (BT).

## R8. Lemma 3.6 with banks: rebalancing.  PROVED.
Rebalance b^+-_# by adding c a 1_F (not c a^#): a 1_F(xi^#) = q_0^# a(zhat^#_F) -> q_0 a(zhat_F) = q_0 != 0, so |c| -> 0, the difference b^+_# - b^-_# = D^# is
unchanged, and the bank coordinates keep the contact-like split z b^+ >= 0 >= z b^- required by Y4-ref Lemma P2.

## R9. Corollary 5.7 for N >= 2.  PROVED.
Read "Delta d < 0" as Delta d_m < 0 for EVERY m (otherwise a block with Delta d_m = 0 has only neutral carriers outside K_omega and (H1) fails), and
read the non-negligibility hypothesis as |Delta d_{m(k)}||w(k)| >= 2 tau_k C_1 for exceptional strict non-peaks not carrying omega.  Then the proof
is V4's (E = {}, factor >= 64 > 32 from Step 6, so E' = {}).
Existence caveat: the clause "including exactly degenerate swallowing-type peaks, if present" is conditional.  Rows that are (hysteretic)
owner-rule above some level and carry an EXACTLY degenerate swallowing-type peak are not known to exist: the threshold has a jump part from
fine flips that may skip the degenerate value, and freezing the fine signs lets fine values cross zero, which destroys exact data (Prop.
4.2').  Prop. 5.1(c) gives exact degeneracy only at fixed z on all levels, where fine carriers are not robust.  OPEN, and immaterial for
D_Omega (V1 Corollary AC).

## R10. Scope of Theorem 5.6.  PROVED.
Lemma.  If two-piece data with all Delta d_m < 0 satisfy (H1) and (H2), then |z_j| = 1 for every j notin F.
Proof.  For j notin F: if j in E' then D(j) != 0 by (H2); if o_N(j) notin K_omega ∪ Neg and j notin E, then o_N(j) is neither neutral (H1) nor negligible,
so D(j) != 0 by Prop. 4.2'; if o_N(j) in K_omega ∪ Neg and j notin E', the owner term exceeds 32 times the rest, so D(j) != 0.  Lemma 3.3: D vanishes
at free coordinates.  QED
So Theorem 5.6 concerns maximal-contact (typically sign-mixed) first rows; there it complements V2-ref's Master Theorem III' (whose residual
(C*) is not excluded at sign-mixed full contact).

## R11. Design precision.
(SF_tau) must include tau_l -> 0 (used in Lemma 5.4: tau_{L_0} <= min_m |Delta d_m| M_m/(4 C_1) for an f-dependent right side; and in R5).

## 12. Verified without change (proof re-derived)
Lemmas 1.1, 1.2, 3.3, 3.4, 4.1', 4.4, 4.5, 5.2, 5.4, 5.5; Propositions 3.2, 4.2', 4.6, 5.1, 5.3, 5.8; Theorems 2.2 (with R3), 3.5, 3.7, 5.6 (with R3,
R8, R10); Lemma 2.6; Corollary 3.1.  Numerics: sa_check.py and degenerate_check4.py re-run with V4's outputs; sa_check_dec.py (120 digits,
(SF*)-type weights) confirms Theorem 2.2 and Proposition 3.2 away from round-off (n_- val_- = -4.2e-60 = target; nu_-/theta = 0.25; q_- < 0; all other
nu/theta in [5, 8e124]; W, V z-signed; Delta d/Delta alpha = -5.4e-118; N(w) - 1 = 1e-117).
