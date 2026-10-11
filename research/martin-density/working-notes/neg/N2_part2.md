# N2 (negative track) part 2: a "pure block switching" row -- every nonzero mate is an intrinsic defect, yet the
# canonical truncations recover it with the SAME mate

Goal of this part: test the adversarial idea "switching through one-sided resources at all small scales, with NO base
one-sidedness and NO two-sided block resources at all".  Result (PROVED): such switching exists for an admissible T built
with only Lemma B's conclusion (no private banks, no generic weights, tiny private signatures = far rigidity), every nonzero
mate is outside the closure of the intrinsic classes (K(f) = {0}), and nevertheless every canonical truncation f_N (NA) has
the mate in its own fibre.  So the one-sided structure is INHERITED by NA rows at all scales; this kills the most natural
counterexample mechanism and sharpens what a counterexample must contain (part 3).

Single block I = {1} (the norm p_1; m = 1, lambda_k = Phi(k)).  s(t) = (1+t^2)^{1/2}, and s(t) >= 1 + 3t^2/8 for |t| <= 1.

## 2.1 The data and the operator T_PB

Base.  H = l_2, U e_j = mu_j e_j with mu_j := 2^{-j-10} (compact, U* injective).  q*(b) = ||b||_1 + (sum_j mu_j^2 b_j^2)^{1/2}.
Row data.  abar := 1/(1+mu_1), a := abar e_1^* (q*(a) = 1, F = {1}); e = e_1 in H, U e = mu_1 e_1;
z := e_1 + (1/2) 1_{j >= 2} (not in c_0), zhat := z + Ue, so zhat_1 = 1 + mu_1 and zhat_j = 1/2 for j >= 2.
Two vectors: h := e_2^* - e_3^*, e_0 := e_2^* + e_3^*; h(zhat) = 0, e_0(zhat) = 1.

Index classes.  Sigma_+ := {k >= 12 : k = 0 mod 3}, Sigma_- := {k >= 13 : k = 1 mod 3}, Sigma_g := N \ ({1} u Sigma_+ u Sigma_-).
Weights.  c_1 := 1, c_k := 1 (k in Sigma_+-), c_k := 2^{-k^2} (k in Sigma_g); Phi(k) := 2^{-1-k} c_k.  Inside Sigma_+ (and inside
Sigma_-) consecutive depths have ratio exactly 1/8.
Signatures.  Pairwise disjoint infinite sets S_k subset {4,5,...} (k in N) with min S_k -> infinity; sigma_k := sum_{s in S_k} 2^{-s}
e_s^* (so ||sigma_k||_1 <= 1/8 and |sigma_k(x)| <= ||x||_inf/8); delta_k := 2^{-k} Phi(k)^2 (FAR RIGIDITY: the private tail of
every carrier is <= 2^{-k} Phi(k)^2, far below the carrier's own depth).
Targets.  (y^(i))_{i>=1} dense in c_00 cap S_{q*} with y^(1) := e_1^*/(1+mu_1); (i_n) a sequence taking every value infinitely
often; Sigma_g = {g_1 < g_2 < ...}.  Index i is ALLOWED at k in Sigma_g if supp y^(i) cap S_k = empty and 2 c_k <= 2^{-2s} c_{k'} delta_{k'}
for every k' != k and s in supp y^(i) cap S_{k'} (finitely many conditions; since c_k -> 0 on Sigma_g and min S_k -> infinity,
every i is allowed at all large k in Sigma_g; i = 1 is allowed everywhere).  i(g_n) := i_n if allowed, else 1.
Vectors (n_k := q*(v_k), u_k := v_k/n_k, T e_k := c_k u_k):
 * dominant:   v_1 := e_1^* + delta_1 sigma_1;
 * staircase:  v_k := h + beta_k e_0 + delta_k sigma_k,  beta_k := -8 Phi(k) (k in Sigma_+),  beta_k := +8 Phi(k) (k in Sigma_-);
 * generic:    v_k := y + s_k abar e_1^* + delta_k sigma_k  (y := y^(i(k))), with s_k in [-8Phi(k), 8Phi(k)] chosen so that
               |y(zhat) + delta_k sigma_k(zhat) + s_k| >= 4 Phi(k)  (possible: the excluded s form an interval of length 8Phi(k)).
Normalisations: staircase n_k in [1.99, 2.002] (||h + beta e_0||_1 = 2 for |beta| < 1; Hilbert part <= 2^{-10}; signature
<= delta_k/8); generic n_k in [1 - 10Phi(k), 1 + 10Phi(k)] subset [1/2, 3/2]; n_1 in [1+mu_1-1/256, 1+mu_1+1/256].

LEMMA 2.1 (admissibility).  PROVED.  T_PB is admissible (Part I def:admissible: (T-a)-(T-d)); it uses only Lemma B's conclusion.
Proof.  (T-a): q*(T e_k) = c_k <= 1 = c_1.  (T-b), (T-c): let x in l_1(N) with Z := sum_k x_k c_k u_k in c_00, and suppose x_{k'} != 0.
For s in S_{k'}: h, e_0, e_1^* vanish at s >= 4, signatures of k != k' vanish on S_{k'}, and the only other contributions come
from generic k with s in supp y^(i(k)); for these k != k' (supp y^(i(k)) cap S_k = empty) and allowedness gives 2c_k <=
2^{-2s} c_{k'} delta_{k'}.  With L(s) the least such k and sum_{k >= L, k in Sigma_g} c_k <= 2 c_L (c_{k+1} <= c_k/2 on Sigma_g),
||y^(i)||_inf <= 1 and n_k >= 1/2:
   |Z(s)| >= |x_{k'}| c_{k'} delta_{k'} 2^{-s}/n_{k'} - 4 ||x||_inf c_{L(s)} >= c_{k'} delta_{k'} 2^{-s} ( |x_{k'}|/3 - 2 ||x||_inf 2^{-s} ),
which is > 0 for all large s in S_{k'} (n_{k'} <= 3).  S_{k'} is infinite, so Z is not in c_00: contradiction.  Hence x = 0;
this gives (T-c) and, with Z = 0, (T-b).  (T-d): for each i, i(k) = i for infinitely many k in Sigma_g, and along them
||v_k - y^(i)||_1 <= 9Phi(k) -> 0 and n_k -> 1, so u_k -> y^(i); the y^(i) are dense in S_{q*}.  QED
(Martin's cross-block near-duplicates: for p_N with N >= 2 one may use the same vectors u_k in every block m with weights
2^{-m-k} c_k; nothing below changes except constants.  We stay with N = 1, which suffices for the density problem: one N.)

## 2.2 The first rows f and f_N

For z^# in {z} u {z 1_{[1,N]} : N >= 3} let f^# := f[a, z^#] be the first row with forced base data (a, z^#) (Part II
Sec. 2.1, exists and is unique), zhat^# := z^# + Ue, i.e. zhat^# = zhat or zhat_N := zhat 1_{[1,N]}.  Write f := f[a,z],
f_N := f[a, z 1_{[1,N]}], and w^#, M^#, C^#, P^#, Q^# for the block data (norming functional of R zhat^#).

LEMMA 2.2 (forced data).  PROVED.
 (i) f in S_{p*} does not attain its norm; every f_N attains its norm (at zhat_N/p(zhat_N)); f_N -> f in norm.
 (ii) For every zhat^#: 1 is a peak with w^#(1) = +M^#; every k in Sigma_+ is a non-degenerate peak with w^#(k) = -M^# and
      u_k(zhat^#) in [-4.03Phi(k), -3.99Phi(k)]; every k in Sigma_- is a non-degenerate peak with w^#(k) = +M^# and
      u_k(zhat^#) in [3.99Phi(k), 4.03Phi(k)].
 (iii) M^# in [0.776, 0.8], C^# = 1 - M^# in [0.2, 0.224], C^# >= M^#/4, and the threshold in zhat-units is <= 2:
      |u_k(zhat^#)| > 2 Phi(k) implies that k is a non-degenerate peak of sign sgn u_k(zhat^#).
 (iv) At f: F = {1}, K = empty (|z_j| = 1/2 for j >= 2), and every carrier is a non-degenerate peak (Q = empty).
Proof.  (i) a in c_00, z^# = sgn a on F; f[a, z^#] attains its norm iff a in c_00 and z^# in c_0 (Part II Sec. 2.1, Part I Prop.
1.10(c)); convergence: Part I prop:approximants (z 1_{[1,N]} -> z coordinatewise).  (ii)-(iii): put zeta := R zhat^# (statuses are
positively homogeneous, so the normalisation xi^# = q_0^# zhat^# is irrelevant).  zhat^# in B_{q**} and a(zhat^#) = 1, so
|u_k(zhat^#)| <= 1 and |zeta| <= ||zeta||_1 = sum_k Phi(k)|u_k(zhat^#)| <= sum_k Phi(k) <= 1/2.  Off P, Part I lem:threshold gives
|zeta(k)| = |zeta| Phi(k)^2 |w(k)|/C <= |zeta| Phi(k) (as C >= Phi(k)|w(k)|), i.e. |u_k(zhat^#)| <= 1/2.  Now
u_1(zhat^#) = (1 + mu_1 + delta_1 sigma_1(zhat^#))/n_1 >= (1 + mu_1 - 1/256)/(1 + mu_1 + 1/256) > 0.99, so 1 in P and w(1) = +M.
Hence C = ||D w||_2 >= Phi(1) M = M/4, and C <= M ||Phi||_2 <= M (sum_k 4^{-1-k})^{1/2} = M/sqrt(12); with M + C = 1 this gives (iii)'s
bounds on M, C.  The threshold constant is bar-vartheta = |zeta| M/C <= 4|zeta| <= 2, and by Part I lem:threshold / Part II Lemma T,
|zeta(k)| > |zeta| Phi(k)^2 M/C, i.e. |u_k(zhat^#)| > bar-vartheta Phi(k), forces k in P with w(k) = M sgn zeta(k) and positive
margin.  Staircase values: v_k(zhat^#) = h(zhat^#) + beta_k e_0(zhat^#) + delta_k sigma_k(zhat^#) = beta_k + r_k with |r_k| <=
delta_k/16 <= Phi(k)^2 (h(zhat^#) = zhat^#_2 - zhat^#_3 = 0 and e_0(zhat^#) = 1 for N >= 3), so u_k(zhat^#) = (beta_k + r_k)/n_k lies in
the stated intervals (Phi(k) <= 2^{-13}); these exceed 2Phi(k) in modulus.  (iv) Generic carriers at zhat: |v_k(zhat)| =
|y(zhat) + s_k + delta_k sigma_k(zhat)| >= 4Phi(k) ((s_k abar e_1^*)(zhat) = s_k), so |u_k(zhat)| >= 4Phi(k)/n_k >= (8/3)Phi(k) > 2Phi(k).  QED
(At f_N the generic carriers may change status; nothing below uses them.)

## 2.3 The mates gamma h, uniformly at f and at all f_N

PROPOSITION 2.3.  PROVED.  Let theta := 1/5 and gamma_0 := 5*10^{-5}.  For every f^# in {f} u {f_N : N >= 3} and |gamma| <= gamma_0,
gamma h in C(f^#); explicitly p*(f^# + t gamma h) <= 1 + 0.32 t^2 for 0 < |t| <= min(t_-, 1), t_- := Phi(13)/theta = 5*2^{-14}, and
p*(f^# + t gamma h) <= s(t) for all t.
Proof.  C(f^#) is symmetric, so let 0 < gamma <= gamma_0.  Drop # from M, C, w, psi := L* w = sum_k Phi(k) w(k) u_k (note
||psi||_1 <= 1/2 and psi(zhat^#) = <w, R zhat^#> = |R zhat^#| >= 0).
Case 0 < t <= t_+ := Phi(12)/theta.  Let S(t) := {k in Sigma_+ : Phi(k) <= theta t} (nonempty; its largest depth is >= theta t/8, and
sum_{S(t)} Phi(k)^2 <= (64/63)(theta t)^2).  For nu in [0, 1/2] put omega(k) := nu M/t on S(t) (0 elsewhere), S_2 := sum_{S(t)}
Phi(k)^2 omega(k), d := <D w, D omega>/C = -M S_2/C (w = -M on S(t)), Theta := omega - d w, W := w + t Theta = (1-td) w + t omega,
and A := a + t B with B := gamma h - L* Theta.  The "content" c(nu) := (nu M/t) sum_{S(t)} Phi(k)/n_k is continuous, c(0) = 0, and
c(1/2) >= (0.776/(2t))(theta t/8)/2.002 > 0.0048 >= gamma; fix nu with c(nu) = gamma.  Then
   L* Theta = c(nu) h + E - d psi,   E := (nu M/t) sum_{S(t)} Phi(k)(beta_k e_0 + delta_k sigma_k)/n_k,   B = -E + d psi.
Numbers: S_2 <= (nu M/t)(64/63) theta^2 t^2 <= 0.01626 t; |d| <= 4 S_2; ||E||_1 <= 8.1 S_2; -E(zhat^#) <= 4.03 S_2 (beta_k = -8Phi(k));
||D omega||_2^2 = (nu M/t)^2 sum Phi(k)^2 <= 0.0065.
Block: on S(t), W(k) = -(1-td)M + nu M has modulus <= (1-td)M (d < 0, 0 <= nu <= 1/2); elsewhere |W(k)| = (1-td)|w(k)| <= (1-td)M.
With <Dw, D omega> = dC, ||D W||_2^2 = ((1-td)C + td)^2 + t^2(||D omega||^2 - d^2) <= (C + tdM)^2 + t^2 ||D omega||^2, and C + tdM >= C/2
(t|d|M <= 0.052 t^2 <= 0.1).  Hence N(W) <= (1-td)M + C + tdM + t^2 ||D omega||^2/(2(C + tdM)) = 1 + t^2||D omega||^2/(2(C+tdM)) <= 1 + 0.0325 t^2.
Base: |B(1)| <= |d| |psi(1)| <= 2 S_2, so abar + tB(1) > 0, and with ||x e_1 + y||_H <= x + <e_1, y> + ||y||^2/(2x),
   q*(A) <= 1 + t(1+mu_1) B(1) + t ||B 1_{[2,inf)}||_1 + t^2 mu_1 ||B||_1^2/(2 abar).
Since B(zhat^#) = (1+mu_1) B(1) + sum_{j>=2} zhat^#_j B_j and |zhat^#_j| <= 1/2 for j >= 2,
   q*(A) <= 1 + t B(zhat^#) + (3/2) t ||B 1_{[2,inf)}||_1 + t^2 mu_1 ||B||_1^2/(2 abar).
Here B(zhat^#) = -E(zhat^#) + d psi(zhat^#) <= 4.03 S_2 (d < 0, psi(zhat^#) >= 0) and ||B 1_{[2,inf)}||_1 <= ||E||_1 + |d| ||psi||_1 <= 10.1 S_2,
so q*(A) <= 1 + 19.2 S_2 t + 2^{-11} (12.1 S_2)^2 t^2 <= 1 + 0.32 t^2.  By Part I lem:dualball, p*(f^# + t gamma h) <= max(q*(A), N(W)) <= 1 + 0.32t^2.
Case 0 < s := -t <= t_-.  Same with Sigma_- (w = +M there), omega := nu M/s on {k in Sigma_- : Phi(k) <= theta s}, d := <Dw, D omega>/C =
+M S_2/C, f^# - s gamma h = (a - sB) + L*((1+sd) w - s omega), B := gamma h - L*(omega - d w) = -E' + d psi with E' as E (beta_k > 0).
On Sigma_-: (1+sd)M - nu M in [0, (1+sd)M]; ||D((1+sd)w - s omega)||^2 = ((1+sd)C - sd)^2 + s^2(||D omega||^2 - d^2), giving
N <= 1 + s^2||D omega||^2/(2(C - sdM)); and -B(zhat^#) = E'(zhat^#) - d psi(zhat^#) <= 4.03 S_2.  The bounds are identical.
Large |t|.  For t_- <= |t| <= 1: p*(f^# + t gamma h) <= 1 + |t| gamma q*(h) <= 1 + 2.002 gamma_0 |t| <= 1 + (3/8) t_- |t| <= 1 + 3t^2/8 <= s(t)
(2.002 gamma_0 = 1.0e-4 <= (3/8) t_- = 1.14e-4).  For |t| >= 1: 2.002 gamma_0 <= sqrt(2) - 1 <= (s(t) - 1)/|t|.  Since 0.32 < 3/8, all cases
give p*(f^# + t gamma h) <= s(t).  QED
(Numerical sanity check of the explicit decompositions in a finite truncated model: N2_work/pb_check4.py; observed
max (bound - 1)/t^2 = 0.119 at f and at f_N, N = 3, 10, 50, with the maximal content nu = 1/2; claimed bound 0.32.)

## 2.4 Consequences

THEOREM 2.4.  PROVED.  For T_PB and the rows above:
 (a) the certificate span S(f) = (l_1(F) cap xi^perp) + span{y_k : k in Q} is {0}; hence the intrinsic class K(f) of Part I Sec. 'The resonance obstruction'
     (closed convex hull of shifted certificates and of the C-tame class) is {0} (Part I prop:intrinsic(b)), while C(f) contains the
     segment [-gamma_0, gamma_0] h.  Every nonzero mate gamma h is an "intrinsic defect", and f is not C-tame: (MS) fails;
 (b) for 0 < |gamma| <= gamma_0 and every N >= 3, the operator (f_N, gamma h) : (c_0, p_1) -> l_2^2 attains its norm (Part I Prop.
     1.13(d)), and (f_N, gamma h) -> (f, gamma h); hence (f, gamma h) is in cl NA((c_0, p_1), l_2^2) -- recovered by the canonical
     truncations, with the SAME second row, and without engineering;
 (c) the decompositions of Prop. 2.3 switch carriers between the two sides at every scale (side + only peaks of Sigma_+ pushed
     inward, side - only peaks of Sigma_-; on the wrong side a carrier of Sigma_+ can only carry negative multiples of h), the
     switching vector V(t) = B_+ - B_- is O(t) (it lives in the e_0, sigma_k and psi directions), and NO two-sided representation
     exists (S(f) = {0}).  The same holds at the NA rows f_N: NA rows can carry one-sided block switching at ALL scales.
Proof.  (a) F = {1}, xi_1 = q_0(1 + mu_1) != 0 and Q = empty (Lemma 2.2(iv)).  (MS) fails: by Part II Lemma T, the margin of
k in Sigma_+ is mu_k = q_0 Phi(k)(|u_k(zhat)|/Phi(k) - bar-vartheta) <= 4.03 q_0 Phi(k), so sum_{k in P, mu_k < s} Phi(k) >=
sum_{k in Sigma_+, Phi(k) < s/(4.03 q_0)} Phi(k) >= s/(33 q_0) for small s.  (b) Lemma 2.2(i), Prop. 2.3, Part I prop:reduction(d).
(c) is a description of the decompositions of Prop. 2.3 (and of Part I thm:tamefibre which would force C(f) subset S(f) = {0}
if (MS) held).  QED

Remarks 2.5.
 (1) Consistency: Part I thm:tamefibre (C-tame rows have C(f) subset S(f)) is not contradicted: neither f nor any f_N satisfies (MS).  The
     example shows that (MS)-failure (non-degenerate peaks whose margins are comparable to their depths, at all depths) is a
     genuine one-sided resource, available at NA rows as well.
 (2) Why the truncation inherits everything: the staircase values u_k(zhat^#) are fixed by the coordinates {2,3} (where
     z 1_{[1,N]} = z) up to the private tails delta_k sigma_k, which are <= Phi(k)^2 (far rigidity -- the adversarial choice) and
     hence negligible against margins of order Phi(k); the threshold is pinned (<= 2Phi(k)) by the dominant peak; the base part
     of every decomposition only uses that the free coordinates have |z| <= 1/2 (true at f and at f_N).  Far rigidity, chosen to
     destroy the positive side's private levers, makes inheritance EASIER, not harder.
 (3) Comparison with Part I Sec. 'The resonance obstruction' (P1's exact resonance): there K(f) = R u_{2,1} and the canonical truncations FAIL (Prop. 6.6);
     here K(f) = {0} and they SUCCEED.  The difference is where the one-sided resources live: P1 uses infinitely many base
     contacts (not available at any NA row), here the resources are block peaks whose statuses are decided on finitely many
     coordinates.
 (4) The heuristic "at an NA row the finest scales need a single two-sided linear representation" (E notes, part 2.2) is FALSE
     for mates in general (it is true for exact data, Part II Cor. S2, and for C-tame rows); what is true at NA rows is that BASE
     switching must vanish off the finite set F' u K' (G3 Lemma 1.4(c)).
