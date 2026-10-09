# Y2 referee, part 4: design D^Y, faces of configuration cones, Lemmas 4.1, 4.2, Proposition 4.3, Theorem M

## Design D^Y. Verdict: CORRECT (PROVED).
Recursion well defined: G**(l), H_comb(l), D(l) use only y_{l''}, v_{l''}, S_{l''}, c_{l''} for l'' <= l (c_l is fixed at stage l-1,
y_l at stage l), all N-free (subsets of [1,l], 1/Phi_{l''}, m^nat). Xi^Y >= Xi' (G** >= G*, all factors >= 1), so n^w, T_hi, c_{l+1}
are at least as favourable as for D''': (P1), (P2), (P3), allowedness and every proof that uses only lower bounds on window
lengths / upper bounds on T_hi survive (the Z6 referee's Proposition 3.3 uses nothing else). n^w_l >= (l 2^{l^3} Lambda°)^6 G**^13 D^8 l^8
H_comb^8: checked.

## Faces of configuration cones are free configurations. Verdict: CORRECT (PROVED).
A face of a polyhedral cone is obtained by turning a subset of its inequality rows into equalities; for (Z1) this adds the carrier to P,
for a (Z2) row of type +-1 it sets the type to 0. Free configurations allow every type on T(U) \ F', so every face is a free
configuration cone of the same level, and its l_1-Hoffman constant (violation: the configuration's functional with the new equalities
counted as |row|) is <= G**(l). Finite, N-free, design-computable. Precision (P-M1): the Hoffman constant depends on the
normalization of rows; G** uses Z4's weights m_l(U,n) <= 1 on (Z1), while Lemma 4.1 below must use the UNWEIGHTED rows tau_l for the
d-forced (Z1) rows (so that the face violation sum_a |r_a| is the one Lemma 4.1 bounds) and V_1 the unweighted (tau_l)_-; since
m_l <= 1, viol_{Z^0} <= V_1 and everything is consistent. Y2 does not say which normalization is used; with the unweighted one the
proof is correct.

## Lemma 4.1 (Farkas pinning of the d-forced face). Verdict: CORRECT (PROVED).
rho_A >= 0 on Z^0, = 0 on C(U); Farkas on the polyhedral cone C(U) = Z^0 ∩ ker Q gives the certificate (the LP for the least sup-norm is
feasible and its minimum attained; kappa*(U) > 0 iff A(U) != {} because rho_A is a nonzero functional). The evaluation inequality and
sum_a |r_a| = rho_A + 2 sum_a (r_a)_- are right. Numerical confirmation (referee script Y2_ref_work/farkas_face_check.py): 141 random
cones with nonempty d-forced set, 28200 random tau: max(sum_A |r_a(tau)| - (kappa*+2)V_1(tau)) = -0.034 < 0.

## Lemma 4.2 (monotonicity, repair inside the face). Verdict: CORRECT (PROVED).
(a) New rows at j in T(U') \ T(U) evaluated at E tau: j lies in no target of U, so only a signature v_l(j) (l in U, swallowed, z_j = eps_l)
can appear, giving tau_l v_l(j) >= 0; drop status is a carrier property; Q(E tau) = Q(tau). Face transport via nu_0 in ri C(U) ⊂ ri F_min(U)
(the minimal face containing a convex set C has ri C ⊂ ri F_min) and the face property x + y in F => x, y in F: correct.
(b) Q(F_min) contains Q(nu_0 +- s mu) for mu in span F_min = aff F_min: a subspace; monotone. (c) dimension stabilizes at
dim V(U_V) maximal; V(U) = V(U_V) for U ⊃ U_V; LP selection from generators of F_min(U_V); E preserves l_1 norms. Correct.

## Proposition 4.3 (face reduction). Verdict: CORRECT (PROVED).
F_min(U) = Z^0 ∩ {r_a = 0 : a in A(U)} (a face is cut out by the rows tight on it); Hoffman with G**(l) and Lemma 4.1; repair inside the
cone F_min(U) by Lemma 4.2(c); tau' := tau_1 + rho in F_min ∩ ker Q ⊂ C(U). The factor N q_max can be replaced by q_max
(||Q x||_1 <= q_max ||x||_1, each carrier in one block). Correct.

## Theorem M. Verdict: CORRECT (PROVED by modification of A'').
(DR) entered Z4 only through Lemma 2.3 in Step 5; Steps 1-3 do not use it. V_1(tau|_U): (Z1) unweighted (tau_l)_- <= ||tau - tau°||_1 <= D
(Step 3 projection into Z'), (Z2) violations <= c_U/gamma_T by (2.1), drop rows by Step 4 (margins M_f, anti-sign peaks, Theorem P's
degenerate peaks have no drop row), Q-rows by Step 5's first computation (d-identity, inactive and fine carriers): V_1 <= C'(K_1 + M_f)t.
Proposition 4.3 replaces Hoffman + (DR); constants: C_dia' <= C D(1 + K_F^rel) G**^2 (Lambda* + l + M_f)/gamma_T. Window arithmetic re-done:
K_j/c_flat <= C D^2 (1 + K_F^rel)^2 G**^4 Lambda°^2 Xi_f and n^w_l >= (l 2^{l^3} Lambda°)^6 G**^13 D^8, so condition (i) of Z4 Step 8 holds
when (1 + K_F^rel)^2 Xi_f = o((l 2^{l^3})^6) (room factor Lambda°^4 G**^9 D^6 to spare), and K_j T_hi(l) <= C (1+K_F^rel) Xi_f^{1/2}
2^{-l^3}/(l (l 2^{l^3} Lambda° G**)^5) -> 0 along the (W_M) levels (gamma_f <= 1 used). Correct.
Remark (resolves gap (G1) of part 3 for D^Y): in Theorem M the kept degenerate swallowing-type peaks of a block with no q != 0 swallowed
strict non-peak are simply d-forced (their sign rows lie in A(U)), and nothing beyond the rate K_F^rel of (W_M) is needed. When the
d-forced rows of such a block are exactly the sign rows of its degenerate peaks (e.g. resonant degenerate peaks), the certificate
-sum_D tau_l = -(1/q_min)Q_m + sum_D (q_l/q_min - 1)tau_l gives kappa* <= (1 + q_max)/q_min(D) <= C_f/Phi_min <= C_f D(l) (q >= Phi/2,
Z6-referee 3.1), so K_F^rel <= C_f there (PROVED). If target rows are d-forced as well, kappa* is a genuine rate (only bounded below as in
4.4(a)). So for D^Y the (G1) configurations are covered by Theorem M/Y with no proviso other than (W_M)/(Y4).

## Section 4.4. Verdicts.
(a) PROVED as stated (one block, all active carriers resonant strict non-peaks with q >= 0): Z^0 = orthant, C(U) = {tau >= 0: tau_l = 0 for
q_l > 0} is itself a face, A(U) = sign rows of the q > 0 carriers, certificate norm <= (1 + q_max)/q_min, lower bound |kappa_m| >= 1/q_l
from the coefficient of tau_l. The summary phrase "in one-signed blocks kappa* = Theta(1/q_min)" (Y2 Section 0 item 4 and the task
statement) is proved only in this resonant model. In general one-signed blocks: C(U) = Z^0 ∩ {tau_l = 0 : q_l > 0} is still a face, but
A(U) may contain TARGET rows vanishing on C(U); their certificates are bounded by (design Hoffman constants)/q_min (SKETCH: Hoffman on the
face C(U) gives r_a(tau) <= G** sum_{q>0} tau_l on Z^0, but turning this into a bounded Farkas multiplier needs one more design-scale
constant). Lower bound kappa* >= 1/q_{l'} - 2 for every ZERO-COST q > 0 carrier l' (test tau = e_{l'} in Lemma 4.1): PROVED. None of this is
used in Theorem M, where kappa* enters only as the rate K_F^rel.
(b) PROVED (ri-argument; compensators of both signs in U_fix give nu in ri Z^0 ∩ ker Q). "Any gaps" is correct for kappa* only; gaps of
kept q < 0 carriers still enter gamma_f.
(c) HEURISTIC as labelled.
