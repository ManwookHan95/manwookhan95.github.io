# Q1 notes (Round 10): the combined theorem — ONE N-independent design T_fin; every first row with finite base support is recovered, for every N

Setting: paper/martin_density_note.tex (Sections 1, 2, 7, 8; notation there), finite block sets I = {1..N} (p = p_N), every N >= 1, first rows
f in S_{p_N^*} with FINITE base support F = supp a.  Rec(p_N) := {f : (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f)}.
Sources combined (all refereed, read referee reports first): U4 + U4-ref (T_final), U1 + U1-ref (D^{U1'}, Lemma R-kt, Proposition KN, Master
Theorem IV' assembly, G1 release), X1 + X1-ref (Lemmas K, F, EC, floor row (X4^0), NLM, GEN, QC, Proposition KN^tr, T^tr, fixes KN-1, D2, S-0,
K1, Q1-Q3, W-fix, W1-W4), X2 + X2-ref (Lemmas M1, M2, DC, LV, UE-1, Theorems UE, E^eng, (S2c), (D-lev), (W_exp), repair (R-abs): Lemma CM',
Theorem C_mix'), Z5 Proposition 5.4.  Part files: r10/Q1_part0..3.md (this file supersedes them where they differ).  Scripts: r10/Q1_work/.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED" = complete proof here, citing refereed results precisely; the combination
argument of this round is itself unrefereed, and several cited links have had a single referee pass (listed in 3.5).
No counterexample is claimed; nothing found points to one.

## 0. Summary (answers to the three task items)
(1) DESIGN.  T_fin := D^{U1'} on U4's T_final, with X1's rate objects and thresholds (D1), (D2), generic transcendental weights (fixes W1-W3),
    X2's (D-lev) with n_l and (W_exp) imposed only on the first weight after each MAIN stage (p-W) — written as ONE recursion (Section 1).
    Lemma W_fin (well-founded, N-free), Theorem A_fin (Martin's Lemma B: (T-b), (T-c), (T-d); (T-a) with ||T|| = c_1), Lemma GEN_fin
    (weights algebraically independent over a countable field k_0 containing every non-weight datum) and the interaction checks I1-I10
    (generic weights vs every upper bound, every lower-bound use, absorber R and cluster weights, (W_exp), (D-lev)): PROVED.
    NORMALIZATION (the task's "say which"): the theorem for EVERY N is proved for OPTION (a): ||T_fin|| = c_1 in [1/2, 1) (a Martin-type norm,
    Martin's construction verbatim with an operator of norm <= 1, his Remark 2; (T-a) holds without its equality clause).  With norm one
    (option (b), X1-ref W2: the norm-one carrier is stage 1 in block 2) the theorem holds for N = 1, and for N >= 2 at every F-finite row
    with rho_1(f) != 1; the case rho_1(f) = 1 is OPEN (a slice-coincidence question, 3.6).
(2) ROUTES.  Route V (violation-tolerant, X2 + X2-ref (R-abs)) with step (1a) := Proposition KN^tr is used for EVERY activity class (no active
    shift, one-signed, mixed).  Route X (exact data, zero-value absorbers, X1's MT IV^tr) remains valid for T_fin as an independent proof for
    classes without active shift or one-signed (double coverage), not for mixed classes.  The two routes never act on the same row: route V
    never tunes an absorber (absorbers are ordinary fine carriers there), route X never builds a d-consistent approximant of violated data.
    PROVED: Lemma CM^tr (X1's companion as the companion of route V, with KN-1's exact hold built into the joint fixed point (1c') and
    X1-ref's S-0 drift bound for the fine-structure step), Proposition BR (it is a base row of Theorem UE: (U1)-(U7), (W-a), (W-b), all
    constants of the form design x u^{-C} except the window constants), Lemma PM (the Puiseux margin mu_kappa survives the levers: on Omega
    the levers act EXACTLY and C_m is frozen up to C_f c_{L+1} << mu^2, off Omega no near-threshold carrier exists; the requirement r <= r_0 ~
    g_min/C_lev is part of the late threshold), Lemma S2c^tr (the Puiseux exponent multiplies the exponents of the window constants by
    O(Design(L)) <= O(log(1/T)), so K_w <= exp(C log^2(1/T)) and s_late >= exp(-C log^2(1/T)); (W_exp) c_{L+1} <= exp(-1/T) still wins:
    threshold comparison and Theorem E^eng's requirement hold with NO change of the design), Theorem C^tr.
(3) MASTER THEOREM VI (PROVED): for T_fin (option (a)), every N >= 1 and every f in S_{p_N^*} with finite base support, f in Rec(p_N).
    THEOREM VI.2 (PROVED): for every N, NA((c_0, p_N), l_2^2) is dense <=> (LSC-trunc)_N.  COROLLARY VI.3: (LSC-trunc)_N for infinitely many
    N => density for the Martin-type norm p (I = N) built with T_fin.  So the density problem for these Martin-type norms is reduced EXACTLY
    to (LSC-trunc), the infinite-base-support half of Lemma Z, which remains OPEN.

## Results table
| # | Result | Status | Where |
|---|---|---|---|
| 1 | Definition of T_fin (one recursion) | definition | 1.1-1.3 |
| 2 | Lemma W_fin (well-founded, positive, N-free) | PROVED | 1.4 |
| 3 | Theorem A_fin ((T-b), (T-c), (T-d); (T-a) with ||T|| = c_1; Martin-type norm under option (a)) | PROVED | 1.5 |
| 4 | Lemma GEN_fin (all non-weight data in k_0; weights algebraically independent) | PROVED | 1.6 |
| 5 | Interaction checks I1-I10; survival of every refereed result used | PROVED | 1.7 |
| 6 | Route decision per activity class | PROVED (via 7-11) | 2.1 |
| 7 | Lemma CM^tr (route-V companion with KN^tr; KN-1 hold in (1c'); S-0 drifts) | PROVED mod refereed tools | 2.2 |
| 8 | Proposition BR (KN^tr companion is a base row of Theorem UE) | PROVED mod refereed tools | 2.3 |
| 9 | Lemma PM (Puiseux margin vs levers; C frozen; status preservation along the continuation) | PROVED (+ numerics) | 2.4 |
| 10 | Lemma S2c^tr (late threshold, violation masses, (W_exp)) | PROVED (+ arithmetic check) | 2.5 |
| 11 | Theorem C^tr (every activity class recovered, no (KN)) | PROVED mod refereed tools | 2.6 |
| 12 | Route X alternative for unshifted / one-signed classes on T_fin | PROVED mod refereed tools | 2.7 |
| 13 | MASTER THEOREM VI (option (a): every N; option (b): N = 1, and N >= 2 with rho_1(f) != 1) | PROVED mod refereed tools | 3.1 |
| 14 | Corollary VI.1 (finite-F Lemma Z, f' := f) | PROVED | 3.2 |
| 15 | Theorem VI.2 (density <=> (LSC-trunc)_N, every N) and Corollary VI.3 (Martin's p) | PROVED | 3.3 |
| 16 | Option (b), N >= 2, rows with rho_1(f) = 1 | OPEN | 3.6 |
| 17 | (LSC-trunc)_N (infinite F), density for p_N and p | OPEN | 3.6 |

## 1. The final design T_fin

### 1.1 Data fixed in advance (D0_fin)
 (i)   Base: H = l_2 with orthonormal basis (k_s); mu_s := 2^{-s^2-1}; U k_s := mu_s e_s (diagonal, compact, dense range, ||U|| = 1/4);
       q^*(a) = ||a||_1 + (sum_s mu_s^2 a_s^2)^{1/2}.
 (ii)  Signatures: S_l := {2^l(2i+1) : i >= 1} (l >= 1; pairwise disjoint, even, bounded gaps G_l = 2^{l+1}); Z_0 := N \ union S_l;
       h_l := sum_{s in S_l} 2^{-s} e_s^*, H_l := ||h_l||_1 (rational), delta^max_l := min{2^{-l}, (4(1 + ||U||) H_l)^{-1}}, tau_l := 2^{-l}.
 (iii) Target pool Y_pool := {x/q^*(x) : 0 != x in c_00 with rational entries}, enumerated as (y^(i))_{i>=1} with y^(1) := e_1^*/q^*(e_1^*);
       Y_pool is dense in S_{q^*} (rational finitely supported vectors are dense in l_1, q^* is equivalent to ||.||_1, normalization is
       continuous) and contains V4's (Z0)-targets.  Absorber pool A_pool := {x/q^*(x) : x = beta e_s^* + e_{p_0}^* + 4 sum_{r=1}^R 2^{-r}
       e_{p_r}^*, s >= 1, beta = +-1, R >= 1, p_0 < ... < p_R odd} (U1 (A0)).  P_Y := Y_pool ∪ A_pool, countable.
 (iv)  Schedules: a block sequence (m_r)_{r>=1} with m_1 := 2 in which every m >= 1 occurs infinitely often; a sequence (i_nu)_{nu>=1} in which
       every positive integer occurs infinitely often.
 (v)   OPTION (a): the weight of stage 1 is chosen generically like all others (c_1 in [1/2, 1)); OPTION (b): c_1 := 1.
 (vi)  The field k_0: for y in P_Y and l >= 1 let delta(y, l) be the (GM)-value of 1.3(S2) (delta^max_1 if l = 1) and n(y, l) := q^*(y +
       delta(y, l) h_l); k_0 := Q({y(j), delta(y, l), n(y, l) : y in P_Y, l, j >= 1}), a countable field.  (delta(y, l) is delta^max_l or an
       endpoint (eps g_l - sum_j sigma_j y(j))/H_l of an excluded interval, so it lies in Q(y(j) : j); n(y, l) may be transcendental and is
       included by definition.)

### 1.2 Rounds (D^{U1'} of U1-ref 6.2, made explicit)
Round r = 1, 2, ...; l_r := number of stages before round r (l_1 := 0).
 (r.1) Candidate: m := m_r, nu := #{r' <= r : m_{r'} = m}, y := y^(i_nu); Sigma(y) := supp y ∩ union_{l'} S_{l'}; p := l_r + 2|Sigma(y)| + 1.
       y is ALLOWED (with margin) if (a) supp y ∩ S_{l'} = {} for all l' >= p and (c+) supp y ∩ S_{l'} ⊂ [1, p - 2|supp y| - 1] for all l' < p.
       If allowed, Y_r := y; otherwise Y_r := y^(1) (supported in Z_0) and p := l_r + 1.  Put p_r := p (the MAIN stage of round r).
 (r.2) PRE stages l_r + 1, ..., p_r - 1: for each s in Sigma(Y_r) (in increasing order) two consecutive block-1 stages carrying absorber
       targets for (s, +1) and (s, -1).
 (r.3) MAIN stage p_r: block m_r, target Y_r.
 (r.4) CLUSTER stages p_r + 1, ..., p_r + R_cl(p_r), R_cl(p) := 2|E^ch(p)|, E^ch(p) := T(p) ∪ union_{l'' <= p} (S_{l''} ∩ [1, p]), T(p) :=
       union_{l'' <= p} supp y_{l''}: for each s in E^ch(p) two consecutive block-1 stages with absorber targets for (s, +1), (s, -1).
       l_{r+1} := p_r + R_cl(p_r).
Every stage l has a block m(l) and k(l) := 1 + #{l' < l : m(l') = m(l)}; j(k, m) := the k-th stage of block m (strictly increasing in k,
all that U4 1.2(i) requires).  Round 1: no candidate meeting a signature set is allowed at stage 1, so Sigma = {} and stage 1 is the MAIN
stage of round 1, in block m_1 = 2 (X1-ref W2).  (FD) stages are not used (U4 C6: only V4's negative Proposition 5.8 needs them).
Absorber target at a PRE or CLUSTER stage l for (s, beta): p_0 < ... < p_R := the least odd integers > max(9, max T(l-1)); R = R(l) := the
least integer >= 1 with 2^{3-R} <= mu_{p_0}^2 lb_l^2/4, where lb_l is the a-priori lower bound of c_l of 1.3(S4) (computed before y_l).

### 1.3 Stage l (any type), given everything of the earlier stages
 (S1) Target y_l from 1.2 (for absorber stages: first lb_l, then R(l), then y_l).
 (S2) delta_1 := delta^max_1; for l >= 2 ((GM), U4 1.3(2)): g_l := delta^max_l H_l/(32 * 3^{|supp y_l|}), delta_l := the largest delta in
      [delta^max_l/2, delta^max_l] with |sum_j sigma_j y_l(j) + eps delta H_l| >= g_l for all sigma in {-1,0,1}^{supp y_l}, eps = +-1.
 (S3) n_l := q^*(y_l + delta_l h_l), u_l := (y_l + delta_l h_l)/n_l, v_l := delta_l h_l/n_l, delta°_l := delta_l H_l/n_l,
      eta_l := min(1, min_{j in supp y_l} |y_l(j)|), Lambda°(l) := prod_{l'' <= l}(1 + 2/delta°_{l''}).
 (S4) WEIGHT.  c^max_l := the minimum of the upper bounds of D^{U1'} at stage l, computed from the ACTUAL earlier data:
      PRE and MAIN stages: (W1) c_{l-1}/4; (W2) b(l-1, M(l-1))^2; (W3) (delta_l H_l)^2; (W4'') tau_{l'} 2^{-2s} c_{l'} delta_{l'} T_lo(l-1,
        M(l-1))^3/2 for l' < l and s in supp y_l ∩ S_{l'}; (W5) c_{l-1} delta_l 2^{-min S_l - l - 10}/(1 + ||U||); (W7) as in U4 1.3(4);
        MAIN stages also (W6) g_l 2^{m(l)+k(l)-l}.
      CLUSTER stage p + i (p a main stage, 1 <= i <= R_cl(p)): c^max_{p+i} := min(c^cl(p) 4^{1-i}, c_{p+i-1}/4) (X1-ref W3), where
        c^cl(p) := min{ c_p/4, b(p, M(p))^2, (delta^max_{p+1} H_{p+1}/2)^2, (W4'') for every s in E^ch(p) (T_lo read at the main stage p,
        U1-ref 6.2), (W5) and (W7) at stage p+1 with delta_{p+1} replaced by delta^max_{p+1}/2, and (W_exp) exp(-1/T_lo(p, M(p))) }.
        [(W_exp) is imposed only here, on the first weight after each MAIN stage (X2-ref (p-W)); all later weights inherit it.]
      A-priori lower bounds: PRE stage l: lb_l := (1 - 2^{-l}) c^low_l, c^low_l := min{c_{l-1}/4, b(l-1, M(l-1))^2, (delta^max_l H_l/2)^2,
        (W4'') at s, (W5) with delta^max_l/2, (W7)} <= c^max_l (independent of R); CLUSTER stage p+i: lb_{p+i} := (1 - 2^{-(p+i)}) c^max_{p+i}
        (c^max_{p+i} does not depend on the target).
      GENERIC CHOICE: c_l := a number in [(1 - 2^{-l}) c^max_l, c^max_l] transcendental over k_0(c_1, ..., c_{l-1}) (l >= 2; under option (a)
      also l = 1, with c^max_1 := 1, i.e. c_1 in [1/2, 1)); option (b): c_1 := 1.  [Possible: the interval has positive length and the field
      is countable.]  Phi_l := 2^{-m(l)-k(l)} c_l, lambda_l := m(l) Phi_l.
 (S5) LEVEL DATA.  T(l), s_max(l), sigma(l), sigma_2(l) := max_{l'' <= l} (second element of S_{l''} beyond s_max(l)), m^nat, D(l), delta_min(l),
      G(l), B_mu(l) := 2^{sigma(l)}/mu_{sigma(l)}^2, G^*, H_comb, G^**, Xi^Y, V1's patterns, cones, rays, H_tune, V2's shift and determinantal
      objects, the minors and cofactor polynomials of the exact shifted cones Gamma^#(kappa, a) in ratio variables (U1-ref 4.3) and in X1's form
      ((X4^0) rows in (T)-blocks, (X4) in (KN)-blocks, U-rows; X1 2.2(iv)) for ALL patterns kappa and classes a of level l (patterns range over the
      finitely many carriers l'' <= l and their blocks: N-free); Lip(l), C_L(l), N_L(l) (V2 Lemma L in semialgebraic form on the compact sets
      K_kappa := {r : R(m)^2 <= 1 - sigma_rob(m)/4 for the active blocks m}, X1-ref W-fix, Q3); for every pattern kappa of level l the Lemma QC
      data (Z_kappa, F_Phi := max_{d in N_T} psi_d/Phi_d, mu_kappa(h), m_0 (if Y_1 is empty; else m_0 := infinity), C_Y, alpha_Y (if Y_1 is
      nonempty), c_kappa, beta_kappa, h_kappa; X1-ref 5-7) computed with the ACTUAL weights.  Under option (b) all minima/maxima over kappa in
      (S5)-(S6) run over the patterns with stage 1 notin N_T(kappa) only (their data are non-degenerate by GEN_fin; see 3.6).
      RATE OBJECTS of level l: all these objects; omega(l) := their number.
        Design(l) := [U4's Design(l)] x 4^{R_cl(l)} 2^{k(l + R_cl(l))} eta_l^{-1} (U1 (A4), main stages)
                     x max_kappa [Lip_kappa C_Y(kappa) m_0(kappa)^{-1} c_kappa^{-1} beta_kappa h_kappa^{-1}] (X1-ref Q2)
                     x max_{l'' <= l} 2^{sigma_2(l)} n_{l''}/(mu_{sigma_2(l)}^2 delta_{l''})   ((D-lev) with n_l, X2-ref (p-LV1)).
 (S6) SUB-WINDOWS (every stage; used only at main stages).  M(l) := omega(l) + 1; for w = (l, i), 1 <= i <= M(l), with predecessor w^-:
      u(w) := 1/4 (w = (1,1)), u(w) := b(w^-) otherwise; Q(w) := max{(4 Design(l)/u(w))^{omega(l)+20}, D_cls(w)^2 (Design(l)/u(w))^{C_U1}}
      (U1 (A4)); n(w) := ceil(l 2^{l^3} Q(w)); T_hi(w) := min{T_lo(w^-), 2^{-l^3}/(l Q(w))}; T_lo(w) := 2^{-n(w)} T_hi(w);
      eta(w) = eta'(w) := T_lo(w)^4/(l Design(l));  b(w) := min{b_U4(w), b_X1(w)}, b_U4(w) := min{eta(w), (eta(w)/C_L(l))^{N_L(l)/2}}/(1 +
      Lip(l) C_*(l)), b_X1(w) := the largest b > 0 with (D1) C_L((1 + Lip C_*) b)^{2/N_L} <= eta'(w)/3, (D2) delta_0(b) <= min_kappa min(m_0(kappa)/2,
      (eta'(w)/(3 C_Y(kappa)))^{1/alpha_Y(kappa)}) and b <= min_kappa mu_kappa(eta'(w)/3)/8, delta_0(b) := (1 + Lip C_*) b + Lip C_L ((1 + Lip C_*)
      b)^{2/N_L} + C D(l)^2 b.  [Left sides are continuous, increasing and -> 0 as b -> 0, right sides are positive numbers already computed,
      so the admissible b form an interval (0, b_X1(w)].  The second clause of (D2) uses M <= 1 in X1-ref's "M b <= mu/8".]
 (S7) T_fin e_{k,m} := c_{j(k,m)} u_{j(k,m)}, extended linearly and continuously to l_1(N x N).

### 1.4 Lemma W_fin (well-foundedness, positivity, N-freeness).  PROVED.
(a) Every quantity of stage l is a function of (D0_fin), of quantities of earlier stages and of earlier steps of stage l.  (b) All divisors
are finite and positive and every interval used for a choice is nonempty.  (c) Nothing depends on N.
Proof.  (a) (S1): the round structure uses supports of earlier targets, the S_{l'} and the schedules; for absorber stages lb_l uses c_{l-1},
b(l-1, M(l-1)) (step (S6) of stage l-1), delta^max_l, H_l, s and the (W5)/(W7)-data of stage l-1, or at clusters c^cl(p) (data of the main
stage p: c_p, b(p, M(p)), T_lo(p, M(p)), E^ch(p)) and c_{p+i-1}; then R(l), then y_l.  (S2) uses y_l; (S3) y_l, delta_l; (S4) earlier weights,
b(l-1, M(l-1)), T_lo(l-1, M(l-1)), stage-l data and the field k_0(c_1..c_{l-1}); (S5) data of index <= l including c_l (QC data use the actual
weights of carriers <= l only); (S6) Design(l), omega(l), the Lemma L and QC data, and the predecessor values T_lo(w^-), b(w^-).  Requirements
about the future are imposed later: (W2), (W7) and (W_exp) at stage l+1.  (b) As U4 Lemma W(b) for T_final's objects; c^max_l > 0 (finitely many
positive bounds; (W4'') is a finite list); lb_l > 0 and R(l) exists (2^{3-R} -> 0); the QC data are positive and finite (Lemma QC(a)-(c),
applicable by GEN_fin to every pattern used); b_X1(w) > 0.  (c) No rule refers to N.  For p_N the rate objects of carriers with m(l'') > N
take the value 1 (V1-ref p0) and the patterns of p_N at level l are among those of level l, so the design constants dominate all of them.  QED

### 1.5 Theorem A_fin (admissibility; Martin's Lemma B).  PROVED.
(a) q^*(T_fin e_{k,m}) = c_{j(k,m)} <= c_1, with c_1 in [1/2, 1) under option (a) and c_1 = 1 under option (b) (attained at (k, m) = (1, 2)).
(b) (T-b) T_fin is injective; (T-c) Y := T_fin(l_1(N x N)) satisfies Y ∩ c_00 = {0}; (T-d) for every m, {u_{j(k,m)} : k >= 1} is dense in S_{q^*}.
(c) Under option (b) T_fin is admissible (def:admissible) and satisfies the conclusion of Martin's Lemma B.  Under option (a) it satisfies
    (T-b), (T-c), (T-d) and (T-a) without the equality clause, with ||T_fin|| = c_1 <= 1, which is all Martin's proof uses (X1-ref W1:
    v*_{n,m} in B_Y, ||Phi_m||_1 <= 2^{-m} < 1 in Lemma A, |R_m x|_m <= m 2^{-m} |||x|||, norm density of the normalized vectors in
    Proposition 3); p_N and p are then MARTIN-TYPE norms (Martin's construction verbatim with an operator of norm <= 1; his Remark 2).
Proof.  (a) c_l <= c_{l-1}/4 for l >= 2 (PRE/MAIN: (W1); clusters: c^max_{p+i} <= c_{p+i-1}/4).
(T-b), (T-c) (U4 Theorem 2.2's argument).  Every target satisfies allowedness (a): main targets by (r.1); an absorber target for (s, beta)
at stage l has support {s, p_0, ..., p_R} with p_i odd (in Z_0), and s is in Z_0 or s in S_{l''} with l'' < s and s < l: for PRE pairs
s <= p - 2|supp Y_r| - 1 <= l_r < l by (c+); for cluster pairs of a main stage p < l, s in S_{l''} ∩ [1, p] gives l'' < s <= p, and s in T(p) ∩
S_{l''} gives l'' < (stage of the target containing s) <= p, by allowedness (a) of that target.  Hence, for s in S_{l'}: u_l(s) = 0 for l < l',
u_{l'}(s) = delta_{l'} 2^{-s}/n_{l'}, and other signature vectors vanish on S_{l'}.  Every target meeting s in S_{l'} at a stage l > l'
satisfies (W4): c_l <= tau_{l'} 2^{-2s} c_{l'} delta_{l'}/2 ((W4'') at PRE/MAIN stages; at a cluster stage p+i, c_{p+i} <= c^cl(p), which
contains (W4'') for every s in E^ch(p), and the cluster target's s lies in E^ch(p)).  Let x in l_1(N x N) (indexed by stages), Z := T_fin x
= sum_l x_l c_l u_l in c_00, and x_{l'} != 0.  For s in S_{l'}, Z(s) = x_{l'} c_{l'} delta_{l'} 2^{-s}/n_{l'} + sum_{l > l', s in supp y_l}
x_l c_l y_l(s)/n_l; if the sum is nonempty with least index L(s), then sum_{l >= L(s)} c_l <= (4/3) c_{L(s)} <= (2/3) 2^{-2s} c_{l'} delta_{l'},
so |Z(s)| >= c_{l'} delta_{l'} 2^{-s} (|x_{l'}|/n_{l'} - (8/9) ||x||_inf 2^{-s}) > 0 for all large s in S_{l'} (n_l in [3/4, 5/4]), contradicting
Z in c_00.  So x = 0: (T-b), and (T-c) since Y ∩ c_00 = T_fin(x) ∩ c_00.
(T-d): fix m and i.  Block m is the main block of infinitely many rounds; at its nu-th such round the candidate is y^(i_nu), and i_nu = i for
infinitely many nu.  y^(i) is allowed with margin at every main stage p > 1 + max supp y^(i) + 2|supp y^(i)| ((a): S_{l'} ∩ supp y^(i) != {}
forces l' < min S_{l'} <= max supp y^(i) < p; (c+): supp y^(i) ⊂ [1, p - 2|supp y^(i)| - 1]).  Main stages increase, so y_l = y^(i) at
infinitely many stages l of block m, and q^*(u_l - y^(i)) <= |1/n_l - 1| + q^*(delta_l h_l)/n_l <= 4(1 + ||U||) 2^{-l} H_l -> 0.  Density of
Y_pool in S_{q^*} gives (T-d).  (c): rem:lemmaB / U4 Theorem 2.2(b): Y is a separable operator range, dense, Y ∩ NA((c_0, q)) = Y ∩ c_00 = {0}
(prop:smooth(c)), and the normalized vectors of each block are dense in S_{q^*} ⊃ S_Y.  QED

### 1.6 Lemma GEN_fin (algebraic independence; non-weight data in k_0).  PROVED.
(a) Every non-weight datum of every stage lies in k_0: y_l in P_Y always (main targets in Y_pool, absorber targets in A_pool, whatever the
integers R, p_i, s, beta are), delta_l = delta(y_l, l), n_l = n(y_l, l), u_l(j) = (y_l(j) + delta_l 2^{-j} 1_{S_l}(j))/n_l, mu_s, H_l, the
aggregated signature coefficients ||v_l 1_{S_l ∩ [1, s]}||_1 (any integer s, e.g. s = s_far(w)), and all integers (m(l), k(l), stage types).
(b) Option (a): (c_l)_{l >= 1} is algebraically independent over k_0; option (b): (c_l)_{l >= 2} is.  Hence for every finite set D of stages
(not containing stage 1 under option (b)) the weights (Phi_d)_{d in D} are algebraically independent over k_0(Phi_l : l notin D).
Proof.  (a) By the definitions in 1.1(vi), 1.2, 1.3.  (b) Induction: if c_1, ..., c_n are algebraically independent over k_0 and c_{n+1} is
transcendental over k_0(c_1, ..., c_n), then c_1, ..., c_{n+1} are algebraically independent over k_0.  Phi_l is a nonzero rational multiple
of c_l.  QED
Consequently X1's Lemma GEN (X1-ref 6: B_kappa is semialgebraic of dimension < |N_T|, defined over k := k_0(weights of the carriers of kappa
outside N_T)) gives (Phi_d)_{d in N_T(kappa)} notin B_kappa for EVERY pattern kappa of every level (option (a)), resp. for every pattern with
stage 1 notin N_T(kappa) (option (b)); thresholds b, u, T_lo, Design depend on weights but are not cone coefficients.

### 1.7 Survival audit and interaction checks.  PROVED (by the cited refereed audits and I1-I10).
Features: (F1)-(F9), (F11) of U4 Theorem 2.3 [SLD structure, (P1)-(P3) per sub-window, bounded gaps, allowedness (a), (c), mu-base, private
banks/pulls, pigeonhole sub-windows, rate scheme, b(w) a design power of T_lo(w), Design(l) dominating all earlier design factors incl.
B_mu (fix C1), c_{l+1} <= c_l/4, <= b(l, M(l))^2, <= (delta H)^2; N-free]; (F10) only partly ((W5), (W6), (W7) not at absorber/cluster stages,
(FD) absent); (F12) D^{U1'} (pre-pairs, clusters, (A0), (W4''); Lemma 3.2 under D^{U1'}, U1-ref 6.4); (F13) X1's rate objects, (D1), (D2),
Design factors; (F14) generic weights; (F15) (D-lev) with n_l; (F16) (W_exp) after main stages.
Audits covering features separately: U4 + U4-ref (T_final; Lemma GW; trees of MT II, MT III', RS'); U1-ref 6.3 (D^{U1'}: admissible, N-free,
lost features unused on U1's tree); X1-ref 9 (T^tr = T_final + D^{U1'} + generic weights, W1-W4, Lemma W'); X2-ref (p-W), 6.1 (D^{X2} =
D^{U1'} + (D-lev) + (W_exp)).  The pairs no single audit covered:
 I1 (F14) x upper bounds: c_l <= c^max_l, the minimum of ALL upper bounds (D^{U1'}, cluster rule, (W_exp)), computed from the actual earlier
    weights; every upper-bound use survives verbatim.
 I2 (F14) x lower-bound uses (complete list, X1-ref W4 plus D^{U1'}): absorber capacity lambda_a >= c_{L+1}/Design(L) at cluster stages (U1 3.5(c)):
    c_{L+i} >= prod_{j<=i}(1 - 2^{-(L+j)}) c^cl(L) 4^{1-i} >= (1/2) c^cl(L) 4^{1-i} by induction from c^max_{L+i} = min(c^cl 4^{1-i}, c_{L+i-1}/4);
    consecutive block-1 ratio >= 8 (U1-ref 7): from (W1) and k increasing; design-computed lower bounds lambda_l >= 1/D(l), Phi_min(L) >= 1/D(L)
    (computed after the weights); s_1 = T_lo^8 c_l and (VT) c_l >= C' D T_lo (U3-ref RT*(f), F7) — not on the tree of Master Theorem VI.
    All survive with factors in [1/2, 1].
 I3 (F14) x (F12): R(l) is computed from lb_l <= c_l, so 2^{3-R} <= mu_{p_0}^2 c_l^2/4, the only property of R used (U1 Lemma 3.3(i): the
    sweep Theta in [0, c_p^2] covers an interval of length >= mu_{p_0}^2 c_p^2/2 >= 2^{4-R}); R is fixed before c_l (X1-ref W3).
 I4 (F14) x (F16): (W_exp) is one of the bounds in c^cl(p) <= c^max_{p+1}; generic weights lie below it.
 I5 (F14) x (F15): (D-lev) involves no weight.
 I6 (F16) x (F12): (W_exp) acts only on c^cl(p) (X2-ref (p-W)); all later weights, cluster or not, are below it ((W1)/cluster rule); R of
    cluster absorbers uses lb_{p+i}, which already contains (W_exp); D^{U1'}'s ratio c_{p+i} ~ c^cl 4^{1-i} holds within the factor of I2.
 I7 (F16) x (F13): T_lo(p, M(p)) is computed in (S6) of stage p after every b(w) of level p, (D1), (D2) included; (W_exp) is imposed at p+1.
 I8 (F13) x (F12): (D1), (D2) only lower b(w); Q(w) only grows; U4 Lemma GW: every window condition is monotone under enlarging Design(l)
    and shrinking b(w), T_lo(w) and the weights.
 I9 (F15): a lower bound on Design(L) only (Lemma GW).
 I10 genericity x non-weight data: GEN_fin(a).
Conclusion: every refereed result on the dependency tree of Master Theorem VI (3.5) holds for T_fin with "level" read as "main stage",
exactly as for D^{U1'} (U1 Theorem 3.1(c), U1-ref 6.3), T^tr (X1 Lemma W'(4)) and D^{X2} (X2 6.1).
