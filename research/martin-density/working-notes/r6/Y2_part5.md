# Y2 part 5: mixed blocks without (DR) -- face reduction of the d-row Hoffman constant (item (m))

Framework: Z4 Theorem A'' (Steps 1-9, active sets U = U(t) = {l in B ∩ [1,l_*] : lambda_l >= t^2} ⊃ U_fix), configurations kappa =
(U, P, eps, F', type, n) and their cones Z'_kappa (rows (Z1),(Z2)) and Z^0_kappa (rows (Z1)-(Z3)) of Z4 part 2; q_l, Q_m(tau) :=
sum_{l in U, m(l)=m} q_l tau_l (all bad carriers, peaks included: q = varsigma eps Phi M/(mC) for peaks).

## 5.1 The enlarged configuration constant and the design D^Y
In Z4 a configuration has type(s) = eps_{l'} forced on S_{l'} ∩ T(U) (l' in U).  Call a *free configuration* the same object with
type : T(U) \ F' -> {+1, -1, 0} arbitrary.  Put G**(l) := max(1, max over free configurations of level <= l of the l_1-Hoffman
constants of the systems (Z1),(Z2) and (Z1)-(Z3)) -- finite (finitely many free configurations of each level, Hoffman 1952), N-free if U
ranges over all subsets of [1,l] (Z4 referee Section 2), and computable from the design data of the carriers l' <= l.
**Design D^Y**: Definition D''' of the Z6 referee (T(l), m^nat, D(l) := 1 + sum_{l''<=l}(1/m^nat_{l''}(l) + 1/Phi_{l''}), H_comb(l) as
there) with Xi'(l) replaced by
   Xi^Y(l) := [l H_comb(l) G**(l) D(l)]^8 (l 2^{l^3} Lambda°(l) G**(l))^5,
n^w_l := ceil(l 2^{l^3} Lambda°(l) Xi^Y(l)), T_hi(l) := min{T_lo(l-1), 2^{-l^3}/(l Lambda°(l) Xi^Y(l))}, T_lo(l) := 2^{-n^w_l} T_hi(l),
c_{l+1} := min{c_l/4, T_lo(l)^3}.  PROVED: D^Y is admissible and N-free, and every result proved for D''' (all of Section 8 of the
note, Theorems C, U', V, Z4 Theorem A'') holds for D^Y: the recursion is well defined (every ingredient has index <= l), Xi^Y >= Xi' >= 1
gives (P1), (P2) and the (P3) used by D''' (the Z6 referee's Proposition 3.3 uses only that the inserted factor dominates the factors
it needs, is >= 1, computable at stage l and N-free).
**Faces are free configurations (PROVED).**  Every face of Z^0_kappa is Z^0_kappa' for a free configuration kappa': a face is obtained by
turning some inequality rows into equalities; for a row of (Z1) this enlarges P, for a row of (Z2) at j it sets type'(j) := 0.  Hence the
Hoffman constant of every face of every configuration cone of level <= l is at most G**(l).

## 5.2 The d-forced face and its Farkas constant
Fix f (F finite) and a finite U ⊃ U_fix, U ⊂ B.  Let Z^0 := Z^0_{kappa(f,U)} (zero cost, drop rows tau_l = 0 at the peaks that are
dropped; in the setting of Theorem P the kept degenerate swallowing-type peaks have no drop row), C(U) := Z^0 ∩ ker Q (Q = (Q_m)_m), and
F_min(U) the minimal face of Z^0 containing C(U).  Let A(U) be the set of inequality rows r_a of Z^0 that vanish on F_min(U) but not on
all of Z^0 (the *d-forced rows*), and rho_A := sum_{a in A(U)} r_a (rho_A := 0 if A(U) = {}).
**Lemma 5.1 (Farkas pinning of the d-forced face).  PROVED.**  If A(U) != {}, there are y_b >= 0 (inequality rows of Z^0), y'_e in R
(equality rows) and kappa_m in R with -rho_A = sum_b y_b r_b + sum_e y'_e r_e + sum_m kappa_m Q_m.  Let kappa*(U) be the least
sup-norm of such a certificate (an LP; kappa*(U) := 0 if A(U) = {}).  Then for every tau in R^U
   sum_{a in A(U)} |r_a(tau)| <= (kappa*(U) + 2) V_1(tau),   V_1(tau) := sum_b (r_b(tau))_- + sum_e |r_e(tau)| + sum_m |Q_m(tau)|.
*Proof.* rho_A >= 0 on Z^0 and rho_A = 0 on C(U) = Z^0 ∩ ker Q, so -rho_A >= 0 on the polyhedral cone Z^0 ∩ ker Q; Farkas' lemma gives
the certificate.  Evaluating at tau and bounding -y_b r_b(tau) <= y_b (r_b(tau))_-, |y'_e r_e(tau)|, |kappa_m Q_m(tau)|:
rho_A(tau) <= kappa*(U) V_1(tau).  Finally sum_a |r_a(tau)| = rho_A(tau) + 2 sum_a (r_a(tau))_- <= rho_A(tau) + 2 V_1(tau).  QED
**Lemma 5.2 (monotonicity and repair inside the face).  PROVED.**  (a) For U ⊂ U' (finite, ⊃ U_fix) the extension by zero E maps Z^0(U)
into Z^0(U'), C(U) into C(U'), and F_min(U) into F_min(U').  (b) V(U) := Q(F_min(U)) is a linear subspace of R^N, and V(U) ⊂ V(U').
(c) There are a finite set U_V ⊂ B and R_f < infinity (depending only on f) such that for every finite U ⊃ U_V ∪ U_fix and every
v in V(U) there is rho in F_min(U) with Q(rho) = v and ||rho||_1 <= R_f ||v||_1.
*Proof.* (a) Rows of Z^0(U') at coordinates of T(U) and the sign/drop rows of carriers of U are those of Z^0(U) (drop status of a carrier
does not depend on U); a new row at j in T(U') \ T(U) evaluated at E tau reads sum_{l in U} eps_l tau_l u_l(j): j lies in no target of U,
so either j in S_l for one l in U, where the row is eps_l tau_l v_l(j) with type(j) = z_j = eps_l (l swallowed), i.e. tau_l v_l(j) >= 0,
true on Z^0(U); or the value is 0.  New sign/drop rows of carriers of U' \ U vanish at E tau.  Q(E tau) = Q(tau).  So E(Z^0(U)) ⊂ Z^0(U'),
E(C(U)) ⊂ C(U').  Let nu_0 in C(U) ∩ ri F_min(U).  For mu in F_min(U), nu_0 - s mu in F_min(U) for small s > 0, hence E(nu_0) = s E(mu) +
E(nu_0 - s mu) with both summands in Z^0(U'); E(nu_0) lies in C(U') ⊂ F_min(U'), a face, so E(mu) in F_min(U').
(b) Q is linear on the cone F_min(U), so Q(F_min(U)) is a convex cone; it contains a neighbourhood of 0 = Q(nu_0) in Q(span F_min(U))
because nu_0 is a relative interior point; hence it equals the subspace Q(span F_min(U)).  Monotone by (a) and Q∘E = Q.
(c) The subspaces V(U) ⊂ R^N increase along inclusions; take U_V with dim V(U_V) maximal; then V(U) = V(U_V) =: V_inf for U ⊃ U_V.
F_min(U_V) is a finitely generated cone with Q(F_min(U_V)) = V_inf; choose generators rho_1..rho_p and, for a basis of V_inf and its
negatives, nonnegative combinations of the generators; this gives a linear-programming selection v -> rho(v) in F_min(U_V) with
||rho(v)||_1 <= R_f ||v||_1.  For U ⊃ U_V, E rho(v) in F_min(U) by (a).  QED
**Proposition 5.3 (face reduction).  PROVED.**  For U ⊃ U_V ∪ U_fix and every tau in R^U there is tau' in C(U) with
   ||tau - tau'||_1 <= [G**(l)(kappa*(U) + 3) + R_f (1 + N q_max G**(l)(kappa*(U) + 3))] V_1(tau)      (l := max U, q_max := max |q_l| <= 1/C_min).
*Proof.* F_min(U) = Z^0 ∩ {r_a = 0 : a in A(U)} (a face is cut out by the rows tight on it; rows tight on all of Z^0 are rows of Z^0
already), a free configuration cone of level l (5.1).  Hoffman: tau_1 in F_min(U) with ||tau - tau_1||_1 <= G**(l)(viol_{Z^0}(tau) +
sum_a |r_a(tau)|) <= G**(l)(kappa* + 3) V_1(tau) (Lemma 5.1).  Then Q(tau_1) in V(U) (Lemma 5.2(b)); let rho := rho(-Q(tau_1)) (Lemma 5.2(c))
and tau' := tau_1 + rho in F_min(U) (convex cone) with Q(tau') = 0, i.e. tau' in C(U).  ||rho||_1 <= R_f ||Q(tau_1)||_1 <=
R_f(||Q(tau)||_1 + N q_max ||tau - tau_1||_1).  QED
Reading.  The f-dependence of the d-row Hoffman constant is isolated in ONE linear program per active set, kappa*(U), plus a fixed
repair constant R_f; the combinatorial part is the design constant G**.  kappa*(U) = 0 whenever the d-neutral zero-cost cone C(U) meets
the relative interior of the zero-cost cone Z^0 (no d-forced rows): then mixed blocks cost nothing beyond R_f.

## 5.3 Theorem M
Rates: K_F(l) := max{kappa*(U) : U finite, U_V ∪ U_fix ⊂ U ⊂ B ∩ [1,l]} (nondecreasing in l) and its relative version
K_F^rel(l) := K_F(l)/D(l) (D(l) the design factor of D^Y; by 5.4(a) design-scale parts 1/Phi of kappa* are absorbed by D(l)).
**Theorem M.  PROVED (by modification of Z4 Theorem A'' / Theorem P).**  Design D^Y, N >= 1, f with F finite satisfying (H2'') [or the
shift-cost condition of part 6], (H3) or the donor condition of Theorem P, and
   (W_M)  liminf_l (1 + K_F^rel(l))^2 Xi_f(l) / (l 2^{l^3})^6 = 0     (Xi_f as in Z4 3.1).
Then f in Rec.  No (DR), no compensated/rigid dichotomy, no resonance is assumed: mixed blocks are allowed.
*Proof.* Z4 Steps 1-3 unchanged (they give c_U(tau) <= (1/q_0 + 2K_0)t, the projection bound for the zero-cost rows via Lemma 2.2 of Z4
with gamma_T, and |Delta d_m| M_m <= K_d t).  Step 4 of Z4 bounds the violations of (Z1)-(Z3) by C_2(K_1 + M_f)t; Step 5's first computation
bounds |Q_m(tau|_U)| <= K_q t <= C K_1 t (inactive and fine carriers included).  So V_1(tau|_U) <= C'(K_1 + M_f) t.  Replace the
Hoffman-plus-(DR) argument of Steps 4-5 by Proposition 5.3 (U ⊃ U_V for t small): tau' in C(U) -- zero cost, tau' = 0 at the dropped peaks,
exact d-rows -- with ||tau|_U - tau'||_1 <= C_dia' t, C_dia' := C'' G**(l_*)(1 + K_F(l_*))(K_1 + M_f), C'' an f-constant.  Steps 6-9 (or
Lemma 4.2 + Proposition Q in the setting of Theorem P) are unchanged with C_dia' in place of C_dia; since C_dia' <= C D(l)(1 + K_F^rel)
G**^2 (Lambda* + l + M_f)/gamma_T, Z4 Step 8 needs K_j/c_flat <= C D^2 (1 + K_F^rel)^2 G**^4 Lambda°^2 Xi_f <= n^w_l and K_j T_hi(l) -> 0;
D^Y gives n^w_l >= (l 2^{l^3} Lambda°)^6 G**^{13} D^8 and T_hi(l) <= its inverse, so both hold along the levels given by (W_M).  QED

## 5.4 What K_F measures, and what remains of (m)
(a) PROVED: one block, all its carriers in U resonant strict non-peaks with q_l >= 0: Z^0 is the orthant, C(U) = {tau >= 0 : tau_l = 0
where q_l > 0}, the d-forced rows are the sign rows of the q > 0 carriers, and with q_min := min{q_l > 0}, q_max := max q_l the
certificate -sum_{q_l>0} tau_l = -(1/q_min) Q_m + sum_{q_l>0} (q_l/q_min - 1) tau_l gives 1/q_min <= kappa*(U) <= (1 + q_max)/q_min (the
lower bound: the coefficient kappa of Q_m must satisfy kappa q_l <= -1 for every l with q_l > 0).  So K_F is design scale (q_l >= Phi_l/2
when gap <= M/2, Z6 referee 3.1) times the relative rate K_nn of nearly neutral carriers -- the Z4 referee's Lemma R (lower bound) and
Theorem U' (upper bound) in one formula.
(b) PROVED: K_F(l) = 0 iff A(U) = {} for all U, iff C(U) meets the relative interior of Z^0 (the minimal face containing C(U) is Z^0).
This holds in particular if every block containing a carrier of B with q != 0 has resonant strict non-peaks l^+_m, l^-_m in U_fix with
q_{l^+_m} > 0 > q_{l^-_m} (compensated blocks, NO gap condition needed for this step): take nu_0 in ri Z^0; e_{l^+-_m} in Z^0 (resonance),
so nu := nu_0 + sum_m (x^+_m e_{l^+_m} + x^-_m e_{l^-_m}) in ri Z^0 for x >= 0, and x can be chosen with Q(nu) = 0.  More generally
K_F = 0 whenever some d-neutral zero-cost combination is strictly positive on every non-implicit row of Z^0 ("two-sided mixed blocks").
(c) In general kappa*(U) is the reciprocal of the smallest relative d-coefficient of a zero-cost direction leaving the d-forced face:
by LP duality, kappa*(U) = sup{ rho_A(mu) : mu with V_1-row violations <= 1 and |Q(mu)| <= 1 ... } (HEURISTIC reading, not used).  It is
large exactly when zero-cost switching directions exist that are NEARLY but not exactly d-neutral (generalized K_nn).  This is a genuine
f-rate (the q_l depend continuously on f), and the exact-data method cannot avoid it: the actual switching may run along such a
direction with amplitude up to |Q|-pinning/|Q(direction)|, and no exact d-neutral datum is close to it (the direction is not contained in
any d-neutral zero-cost element).  REMAINING STEP for (m): either a design that bounds kappa*(U) (impossible for one-signed blocks by
Lemma R, so only relative versions K_F/D(l) can be design-bounded), or a joint transient bound of Conjecture G type for nearly neutral
directions (part 7).
