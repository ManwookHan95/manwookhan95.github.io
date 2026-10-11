# N2 referee, part 2: Lemma 2.1 (admissibility of T_PB) and Lemma 2.2 (forced data)

Scripts: neg/N2_ref_work/pbmodel.py (high-precision model with the TRUE parameters: staircase from k = 12, depth ratio 1/8,
generic weights 2^{-k^2}, mu_j = 2^{-j-10}, private signatures delta_k = 2^{-k} Phi(k)^2), pb_ref_check.py (forced data),
pb_ref_check2.py (decompositions, part 3).  mpmath with 60 digits, carriers k <= 96, coordinates j <= 1200.

## 2.1 Lemma 2.1 (admissibility) -- CORRECT for one block (PROVED); the multi-block parenthetical is WRONG as written (fix F3)

Re-derived.  (T-a): q*(T e_k) = c_k <= 1 = c_1.  (T-b)/(T-c): let x in l_1 with Z := T x in c_00 and x_{k'} != 0.  At s in S_{k'}
(a subset of {4,5,...}) the vectors h, e_0, e_1^* vanish, the signatures sigma_k (k != k') vanish (disjointness), and a generic
target y^(i(k)) can be nonzero at s only if k != k' (allowedness forbids supp y^(i(k)) cap S_k != empty; i = 1 is supported
on {1}).  For such k allowedness gives 2 c_k <= 2^{-2s} c_{k'} delta_{k'}; with L(s) the least such k, sum_{k >= L, k in Sigma_g}
c_k <= 2 c_L (c = 2^{-k^2} on Sigma_g), ||y^(i)||_inf <= 1 and n_k >= 1/2, the generic contributions are at most
4 ||x||_inf c_{L(s)} <= 2 ||x||_inf 2^{-2s} c_{k'} delta_{k'}, while the signature of k' contributes x_{k'} c_{k'} delta_{k'} 2^{-s}/n_{k'}
with n_{k'} <= 3.  Hence |Z(s)| >= c_{k'} delta_{k'} 2^{-s} (|x_{k'}|/3 - 2||x||_inf 2^{-s}) > 0 for all large s in the infinite set
S_{k'}: contradiction.  (T-d): every i is allowed at all large k in Sigma_g (finitely many conditions; c_k -> 0; min S_k -> inf),
so i(k) = i for infinitely many k, and ||v_k - y^(i)||_1 <= 8 Phi(k) abar + delta_k/8 -> 0, n_k -> 1.  Also ||Phi||_1 <= 1/2 < 1
(Lemma A applies).  The norm-one condition of Lemma B is (T-a) with equality at k = 1.

Precisions.
 (P-a) n_k >= 2 exactly on the staircase (||h + beta e_0||_1 = 2 for |beta| < 1, plus the disjoint signature), so the stated
       interval [1.99, 2.002] is correct (numerically n_k in [2.000273, 2.000273]).
 (P-b) Lemma 2.1 constructs a ONE-block operator T: l_1(N) -> l_1.  For the norm p_1 only block 1 enters, and every Part I
       statement used (rigidity, forced decomposition, dual ball, approximants, reduction) uses only (T-a)-(T-d) of the blocks
       present, so this suffices for the density problem for p_1 (a negative answer for p_1 alone would already give a
       two-dimensional Hilbert space without property B).  To obtain an operator on l_1(N x N) in the literal sense of
       def:admissible one needs further blocks; see F3.
 (F3)  The parenthetical "for p_N with N >= 2 one may use the SAME vectors u_k in every block m with weights 2^{-m-k} c_k" is
       wrong as written: T e_{k,m} = c_k u_k for all m makes T(e_{k,1} - e_{k,2}) = 0, so (T-b) fails.  CORRECTION (PROVED):
       take a bijection l: N x N -> N with l(1,1) = 1, pairwise disjoint infinite signature sets S_{k,m} in {4,5,...} with
       min S_{k,m} -> inf, delta_{k,m} := 2^{-k} Phi_m(k)^2, generic weights c_{k,m} := 2^{-l(k,m)^2}, staircase and dominant weights 1,
       u_{k,m} := (v_k^{(m)} + delta_{k,m} sigma_{k,m})/n_{k,m} where v_k^{(m)} is the block-1 recipe (dominant e_1^*; staircase
       h + beta_k e_0 with beta_k = -+8 Phi_1(k); generic y^(i(k,m)) + s_{k,m} abar e_1^* with |value at zhat| >= 4 Phi_m(k)), and
       allowedness of i at a generic (k,m) relative to ALL signature sets S_{k',m'}.  The proof above goes through verbatim with
       (k,m) in place of k (the generic weights are summable in the order of l with sum_{l(k,m) >= L} c_{k,m} <= 2 c_L).  These are
       exactly Martin-type cross-block near-duplicates: u_{k,m} and u_{k,1} differ only by private tails.

## 2.2 Lemma 2.2 (forced data) -- CORRECT (PROVED)

Re-derived.  zhat^# in B_{q**} gives |u_k(zhat^#)| <= 1 and |zeta| <= ||zeta||_1 <= ||Phi||_1 <= 1/2.  Off P, |zeta(k)| = |zeta| Phi(k)^2
|w(k)|/C <= |zeta| Phi(k) since C = ||Dw||_2 >= Phi(k)|w(k)|; so |u_k(zhat^#)| > 1/2 forces k in P.  u_1(zhat^#) >= (1+mu_1)/n_1 > 0.99
(sigma_1(zhat^#) >= 0), so 1 in P, w(1) = M, C >= M/4, C <= M ||Phi||_2 <= M/sqrt(12); M + C = 1 gives M in [0.7760, 0.8].  By Part II
Lemma T, k in P iff |u_k(zhat^#)| >= bar-vartheta Phi(k) with bar-vartheta = |zeta| M/C <= 4 |zeta| <= 2.  Staircase values:
v_k(zhat^#) = beta_k + delta_k sigma_k(zhat^#) with 0 <= sigma_k(zhat^#) <= 1/16 (h(zhat^#) = 0, e_0(zhat^#) = 1 need N >= 3: both
coordinates 2, 3 lie in [1, N] and (U e)_2 = (U e)_3 = 0), so u_k(zhat^#) lies in [-4 Phi(k), -3.996 Phi(k)] on Sigma_+ and in
[3.996 Phi(k), 4 Phi(k)] on Sigma_- (inside the stated intervals).  Generic carriers at zhat: |v_k(zhat)| >= 4 Phi(k) by the choice
of s_k ((abar e_1^*)(zhat) = 1), so |u_k(zhat)| >= 4 Phi(k)/(1 + 9 Phi(k)) > 2 Phi(k): Q = empty at f.  K = empty since |z_j| = 1/2 off
F = {1}.  (i): f[a, z^#] attains its norm iff a in c_00 and z^# in c_0 (Part II Sec. 2.1, Part I prop:smooth(c)); f_N -> f because
z 1_{[1,N]} -> z coordinatewise (Part II Sec. 2.1).

Numerical confirmation (pb_ref_check.py, true parameters):
   f:    M = 0.799922, C = 0.200078, threshold (zhat units) = 0.8048, |zeta| = 0.2013; staircase u_k/Phi = -+3.99945; Q = empty;
   f_3, f_10:  M = 0.8, C = 0.2, threshold 0.8001; staircase u_k/Phi = -+3.99945, all peaks; generic carriers with targets
         beyond N become strict non-peaks (expected; N2 says "the generic carriers may change status; nothing below uses them").
   f_60: same as f.
So the threshold is about 0.80 (the bound 2 holds with room), and the staircase margins are about 3.2 Phi(k) q_0.

## Verdict on part 2
Lemma 2.1: CORRECT (one block); the N >= 2 parenthetical is wrong as written (F3), corrected above.  Lemma 2.2: CORRECT.
The listed features of T_PB (dominant carrier; staircases with vectors (h -+ 8 Phi(k) e_0)/n up to tails; generic carriers hitting
the dense targets; private tails <= 2^{-k} Phi(k)^2; no private banks or levers in the sense that every private resource moves a
carrier's value by at most delta_k/8 << Phi(k); generic weights 2^{-k^2}, i.e. no "generic-weight" (transcendental) design) are
accurate.  T_PB uses only the conclusion of Lemma B (via def:admissible).
