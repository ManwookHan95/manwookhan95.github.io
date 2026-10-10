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
    the levers act EXACTLY and C_m is frozen up to C_f c_{L+1} <= C_f eta' mu/8 << mu, off Omega no near-threshold carrier exists; the requirement r <= r_0 ~
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
      data (Z_kappa, F_Phi := max_{d in N_T} psi_d/Phi_d and its Lipschitz constant Lip_kappa on K_kappa, mu_kappa(h), m_0 (if Y_1 is empty;
      else m_0 := infinity), C_Y, alpha_Y (if Y_1 is nonempty; else C_Y := 0), c_kappa, beta_kappa, h_kappa; X1-ref 5-7) computed with the ACTUAL
      weights.  Under option (b) all minima/maxima over kappa in (S5)-(S6) run over the patterns with stage 1 notin N_T(kappa) only (their data
      are non-degenerate by GEN_fin; see 3.6).
      RATE OBJECTS of level l: all these objects; omega(l) := their number.
        Design(l) := [U4's Design(l)] x 4^{R_cl(l)} 2^{k(l + R_cl(l))} eta_l^{-1} (U1 (A4), main stages)
                     x max_kappa [max(1, Lip_kappa) max(1, C_Y(kappa)) max(1, 1/m_0(kappa)) max(1, 1/c_kappa) max(1, beta_kappa) max(1, 1/h_kappa)]
                       (X1-ref Q2; 1/infinity := 0)
                     x max_{l'' <= l} 2^{sigma_2(l)} n_{l''}/(mu_{sigma_2(l)}^2 delta_{l''})   ((D-lev) with n_l, X2-ref (p-LV1)).
 (S6) SUB-WINDOWS (every stage; used only at main stages).  M(l) := omega(l) + 1; for w = (l, i), 1 <= i <= M(l), with predecessor w^-:
      u(w) := 1/4 (w = (1,1)), u(w) := b(w^-) otherwise; Q(w) := max{(4 Design(l)/u(w))^{omega(l)+20}, (Design(l)/u(w))^{C_U1}} (U1 (A4):
      D_cls(w) = (J+1) 3^J (A_max/eps)^p <= C_{f,N} (Design(l)/u(w))^{C_D} with C_{f,N} an f-constant (it contains 3^N and the f-constant of A_max;
      3^{|Omega|} <= 3^l is a design factor), K = C_f (Design/u)^{C_K}; C_U1 := 2 C_D + C_K + 1 absolute; f-constants are absorbed by l 2^{l^3}
      below); n(w) := ceil(l 2^{l^3} Q(w)); T_hi(w) := min{T_lo(w^-), 2^{-l^3}/(l Q(w))}; T_lo(w) := 2^{-n(w)} T_hi(w);
      eta(w) = eta'(w) := T_lo(w)^4/(l Design(l));  b(w) := min{b_U4(w), b_X1(w)}, b_U4(w) := min{eta(w), (eta(w)/C_L(l))^{N_L(l)/2}}/(1 +
      Lip(l) C_*(l)), b_X1(w) := the largest b > 0 with (D1) C_L((1 + Lip C_*) b)^{2/N_L} <= eta'(w)/3, (D2) delta_0(b) <= min_kappa min(m_0(kappa)/2,
      (eta'(w)/(3 C_Y(kappa)))^{1/alpha_Y(kappa)}) and b <= min_kappa mu_kappa(eta'(w)/3)/8, delta_0(b) := (1 + Lip C_*) b + Lip C_L ((1 + Lip C_*)
      b)^{2/N_L} + C D(l)^2 b (conventions: m_0 = infinity or C_Y = 0 make the corresponding clause void).  [Left sides are continuous,
      increasing and -> 0 as b -> 0, right sides are positive numbers already computed, so the admissible b form an interval (0, b_X1(w)].
      The last clause uses M <= 1 in X1-ref's "M b <= mu/8".]
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

## 2. The two routes and their combination

Setting of Section 2: T_fin (option (a); under option (b) patterns with stage 1 notin N_T), N fixed, f in S_{p_N^*} with F finite, g in C(f),
rho < 1; w a clean sub-window of a main stage L >= l_f, where l_f = l_f(f, N, g, rho) is a stage beyond which every f-constant is absorbed
(companions in the r_f/2-ball of Lemma M2, T_hi(w) <= t_1 of Theorem UE, C_f^{L^2} 2^{-L^3} small, T_lo(w) below the thresholds of Lemma
S2c^tr); T := T_lo(w), n := n(w), b := b(w), u := u(w), D := D(L), eta' := T^4/(L Design(L));
an activity class a (U1 2.3, U1-ref (p-a), 4.5: read off the decomposition data and fixed before the companion), its pattern kappa, and a
(class, cube) set S of scales.  K := C_f (Design(L)/u)^C as in U1 part 2.  ROUTE X = the exact route (U1-ref's MT IV' assembly with X1's
KN^tr = X1's Master Theorem IV^tr); ROUTE V = the violation-tolerant route (X2's Theorems UE, E^eng with X2-ref's repair (R-abs)).

### 2.0 What the routes need and provide (refereed statements)
Route X: companion = (1a) Proposition KN [now KN^tr]; (1b) zero-value absorbers tuned to value EXACTLY 0 (U1 Lemma 3.3: first pairs P(s),
s in E_c(w), and the cluster of L); (1c) kappa, the exact ratios and the absorbers restored (joint fixed point); (2) fine structure (configuration
(i) recursion, configuration (ii) Schauder) with the G1 release.  Data: EXACT two-piece data at f^#; fine residues and the trace correction on
E_c cancelled EXACTLY by the absorbers' switching coefficients (U1 Proposition 3.4 = Theorem S1's RT*(c)).  Recovery: V2's Theorems E^SC/E^>=
on the subset S (U1 Lemma 2.4).  Classes: no active shift, one-signed; NOT mixed (frustrated positive carriers prevent an exact completion
with (SC) for the negative blocks: U1 5.4-5.5, U1-ref verdict on (C_mix)).
Route V: companion = (1a) Proposition KN [now KN^tr]; (1c') kappa and the exact values restored (joint fixed point), NO absorber tuned; (2') G1
release + static-ownership recursion (negative fine carriers self-aligned, positive anti-aligned, absorbers ordinary fine carriers).  Data:
U1 Proposition 2.2(e) on Omega := all coarse strict non-peaks, with tolerated violations (fine residues, trace corrections, positive-owned
coordinates) of l_1-mass O(Design c_{L+1}).  Recovery: d-consistent engineered approximant f' of f^# (Lemma DC, levers of Lemma LV(a)-(c)),
per-piece bounds (Theorem UE), averaging at f' (Theorem E^eng), threshold comparison (S2c) by (W_exp).  Classes: all.  From the coarse system
route V uses only the conclusions of Proposition KN (statuses, kind [3] rows, exactness of Gamma^#(kappa, a)).

### 2.1 Decision
| class kind | route used for Master Theorem VI | alternative | reason |
|---|---|---|---|
| no active shift | route V with KN^tr (all active blocks are (U)-blocks; KN^tr reduces to the rescaling 2.1(U) = V2 Theorem B, values only) | route X (U1-ref MT IV', first alternative: no (KN), no genericity needed) | uniform proof; route X is an independent check |
| one-signed | route V with KN^tr | route X = X1 MT IV^tr | both valid for T_fin (I3, I6, 2.7) |
| mixed | route V with KN^tr | none | route X fails (frustration); route V tolerates it |
The routes never act on the same row: for each (L, w, class) ONE companion is built.  Route V never tunes an absorber and never gives one a
switching coefficient (X2-ref 2.3: tuned absorbers cannot follow the levers of Lemma DC — their value rooms ~ their weights <= c_{L+1} are far
below the lever and theta-mass moves); route X never builds a d-consistent approximant of violated data (its data are exact).  So X1's
zero-value-absorber features (Theorem S1's RT*(c), U1 Proposition 3.4) and X2's levers never interact; what route V takes from X1 is exactly
Theorem S1(a), (b), (c) (exact cone with robust minors >= u/2, threshold protection, coupling rows (X3)) — i.e. Proposition KN^tr.

### 2.2 Lemma CM^tr (the route-V companion with KN^tr).  PROVED (modulo the refereed tools cited).
Hypotheses: as in the setting, the class a of ANY kind (no active shift, one-signed, mixed); NO hypothesis (KN_{w,a}).
Construction.  STEP A := Proposition KN^tr (X1 2.6 with X1-ref 8): formula-1 kappa with the pattern's Omega (K1); Step 0 (V1's (C1), (C2);
active weak peaks of (T)-blocks pushed to rho = 1 - b); the Lojasiewicz point r' in Z_kappa, a point r_1' of Y_1, a point r'' of Z_kappa with
|r'' - r_1| <= eta' and F(r'') <= 1 - mu_kappa(eta'/3) (Lemma QC; non-coincidence by GEN_fin); realization in ONE joint fixed point: V1 Lemma TU
sets the active values to r''_l kappa ((U)-blocks: s_m r''_l kappa, D1), HOLDS the inactive Omega values of the (T)-blocks at exactly 0 (KN-1),
(KN)-blocks receive U1-ref's lever push, D2 pushes in (U)-blocks, one peak push per block restores kappa; block-triangular Jacobian (d(u/kappa)
/d(TU) = I/kappa, dkappa/d(TU) = O(X), cross effects second order).  [For the KN-1 holds the pull of Lemma TU is taken at a contact j_p of
the carrier's own set with v_l(j_p) >= max(needed downward correction, c_{L+1}) (so j_p <= s_far(w)); the bank absorbs the rest.]  Route V
tunes no absorber, so there is no U1 step (1b) and the end of Step A IS X2-ref's step (1c').
STEP B := X2-ref Lemma CM' step (2'): the G1 release (U1-ref 5) and the static-ownership recursion on J_fine := N \ (F^A ∪ E_c(w) ∪
coordinates fixed in Step A), owner-candidates (a) Omega_act, (b) coarse peaks of active blocks, (d) every carrier at a stage > L of an active
block (absorbers included, with their forced coefficients -Delta''_m lambda_k w(k)); negative fine owners self-aligned, positive anti-aligned,
coarse owners by the sign of their coefficient, unowned coordinates z := 0.  f^# := the resulting row.
Claims.  Put mu_min(w) := min_kappa mu_kappa(eta'/3) (over the patterns of level L) and g_min(w) := (1/8) min(c_f eta', mu_min(w)).
 (a) [exactness] the active ratios at the end of Step A lie on Z_kappa; robust minors and cofactor polynomials are >= u/2; the l_1-Hoffman
     constant of Gamma^#(kappa, a) is <= C (Design/u)^C (V2 Lemma H) and A_max <= C_f (Design/u)^C (U1-ref (p-c)).
 (b) [statuses at f^#] every coarse carrier of f^# is either a peak with relative margin >= u/2 or a strict non-peak with gap^#(k) >= g_min(w);
     in a (T)-block every active near-threshold carrier d has rho^#_d <= 1 - mu_kappa(eta'/3)/4; the inactive Omega carriers of (T)-blocks
     have |value| <= 4 c_{L+1}^2.
 (c) [data] for every t in S, X2-ref CM's data — Domega(t) of U1 Proposition 2.2(e) supported in Omega := all coarse strict non-peaks of f^#,
     with the common true shift Delta''_m = Delta'^*_m kappa'_m/kappa^#_m (U1 Lemma 4.6(a); its middle term vanishes because Step B does not
     change active values), V := V(Domega(t)), V_proj := L(Delta'^*, gamma(t)) on E_c, V_fine := V - V_proj off F^#, b^+ := beta + chi V_proj +
     V_fine/2, b^- := b^+ - V, omega^- := omega^+ + Domega(t) — represent g_t with p*(g - g_t) <= K t and kappa_w <= 1 + eta_0/2, and every
     Omega carrier is of kind [1], [2] (gap >= gamma(w) := min_m M_m u/4) or [3] relative to gap^#.
 (d) [violations] eps(t) <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/T; every violated free coordinate has b^theta = 0 ((H3) of Lemma VT).
 (e) [scrambling] every carrier at a stage > L of a negative active block is an (R) peak with margin >= q^#_0 delta°_k/2, and for every negative
     active block m: Scr^#_m(x) <= C (x/q^#_0)^2 for 0 < x <= x_0(w) := c_f g_min(w) Phi_min(L).
 (f) [cost] p*(f^# - f) <= C_f Design(L) eta' log(1/eta') + C_f c_{L+1} log(1/c_{L+1}) <= theta_w T^2 with theta_w := C_f T^2 log(1/T) -> 0.
Proof.  (a) X1-ref 8(a).  (b) At the end of Step A (X1-ref 8(b)): (T)-blocks: active near-threshold rho <= 1 - mu/2 (gap = M(1 - rho) >= M mu/2),
inactive Omega values 0 (gap M); (KN)-blocks: U1-ref Proposition KN(b) with eta' (gaps >= c_f eta' M); (U)-blocks: active statuses <= 1 - eta',
inactive near-threshold carriers pushed inward by eta' (D2) (gaps >= c eta' M); every other coarse carrier keeps its robust status (relative
margin >= u - Lip eta' >= u/2, or gap >= c u).  Step B changes coarse values only through the released far parts of non-owners: for such l,
|Delta u_l(zhat)| <= 2 delta_l sum_{s > s_far} 2^{-s}/n_l <= 4 c_{L+1}^2 (2^{-s_far} <= c_{L+1}^2, U1-ref 5); it does not change a (hence not e)
and does not touch the active carriers (their sets were closed in Step A).  By X1-ref S-0 the statuses and shifts move by <= C Design(L) c_{L+1}.
Now c_{L+1} <= b(L, M(L))^2 <= b^2 ((W2); b decreases along the sub-windows of a level), b <= eta' (b_U4 <= eta) and b <= mu_min/8 ((D2)), so
C Design c_{L+1} <= C Design eta' mu_min/8 = (C T^4/L) mu_min/8 <= mu_min/16 for L large.  Hence rho^#_d <= 1 - mu/2 + mu/16 <= 1 - mu/4
(gap >= M mu/4 >= mu/8 >= g_min since M >= 1/2), and robust margins/gaps are untouched at this precision.
(c), (d), (e): X2-ref Lemma CM'(a)-(c) and its proof (X2-ref 4).  That proof uses Proposition KN only through (i) the coarse statuses
(feeding U1 Lemmas 4.1, 4.3, 4.5 and the bound x_0: coarse carriers do not enter the scrambled set below x_0 because their margins are >= u/2
and Phi gap >= Phi_min(L) g_min) — supplied by (b); (ii) the kind-[3] property of the near-threshold Omega carriers, which X2-ref takes from
U1-ref 4.1's row (X4) — in (T)-blocks it is supplied by X1's floor row (X4^0): the decomposition data satisfy (X4^0) up to K t (X1-ref 3.2;
weak peaks via eq:peakshift), and every point of the cone and every normalization increment is inward at f^# with the TRUE shift, because
lambda(|Delta'' - Delta'| + |Delta'| |rho^# - rho^0|) <= C lambda (Design c_{L+1} + c_{L+1}^2/t + D^2 c_{L+1}^2) <= 3 lambda gap^#/t (X1-ref 3.3,
S-0; Design c_{L+1} <= (T^4/L) mu/8 << gap^#); the + side: vs omega^+ <= gap(f)/t <= M b/t <= gap^#/(4t) by (D2); in (KN)-blocks U1-ref's (X4),
in (U)-blocks vs gamma >= 0 (Delta' = 0); (iii) exactness of Gamma^#(kappa, a) at the realized ratios (projection with error K t, normalization
onto one ray, U1 Proposition 2.2(b), (c)) — supplied by (a).  No other property of Proposition KN enters (U1 Lemmas 4.1, 4.2 and 4.6 use the
coarse statuses only as "robust, or strict non-peak with gap >> c_{L+1}"; U1-ref 7 covers owners inside absorber blocks; the violation count
of X2-ref CM'(c) uses cone row (X1), dominance and the trace-correction bound only).
(f) Step A: X1-ref 8(c) (V1 Lemmas CO, TU(d)), and Design(L) eta' = T^4/L; Step B: U1 Lemma 4.5 / Z3 Lemma 3.1 (coarse carriers meet J_fine only
beyond s_far(w); carriers at stages > L have total weight <= C c_{L+1}).  QED

### 2.3 Proposition BR (the KN^tr companion is a base row of Theorem UE).  PROVED.
For every t_i in S the data of CM^tr(c) form a window family at the base row f_0 := f^# satisfying X2's hypotheses (U1)-(U7) with A_0 an
f-constant, A_2 = 22, gamma_B = gamma(w) = min_m M_m u/4 (so c_flat(w) >= c_f u), C_Delta an f-constant, and window quantities
   n <= log_2(1/T), gap_min >= g_min(w), x_0 = x_0(w), C_S <= C/q_0^2, c_fine <= C_f c_{L+1}, c_tiny <= Design(L)^C c_{L+1},
   r_0 >= c g_min(w)/(C_lev Design(L)^C), C_2, C_lev, K_J <= C_f Design(L)^C (K_X = 0: no absorber in Omega).
The window conditions (W-a), (W-b) of Theorem UE hold for L >= l_f.
Proof.  (U1), (U2): CM^tr(c) (V1 TR(iii) for A_2 = 22).  (U3) at E := F^# \ F, the supports created in Step A (TU banks and pulls of KN^tr and
of the KN-1 holds, peak-push banks, (KN)-lever moves; Step B creates none): data contact-like or t|b| <= K_3 |a^#| by V1 TR(iv) — the moves of
KN^tr have the types of U1-ref's Proposition KN moves (a TU pull with mass 24 lambda v carries data <= (2A_2 + C) lambda v/t, X2-ref (c3'));
at a KN-1 hold (gamma_l = 0) the data are V_fine(j) with |V_fine(j)| <= C_f c_{L+1}, while the pull mass is >= 24 lambda_l c_{L+1} >= 24 c_{L+1}/
Design(L) and the bank mass >= c_f c_{L+1} (pull chosen with v_l(j_p) >= c_{L+1}), so t|b| <= |a^#| for t <= T_hi(w); K_3 is absorbed in (c2).
No absorber support coordinates exist ((R-abs)).  (U4): CM^tr(d).  (U5): CM^tr(e).  (U6): Lemma LV(a)-(c) (X2 2.3 with X2-ref (p-LV1), (p-LV2))
for Omega = all coarse strict non-peaks of f^#: (a) active class-G carriers: (TU) levers; (b) inactive class-G carriers, including the
KN-1-held carriers of (T)-blocks (data at the lever coordinate j(l): V_t(j) = gamma_l v_l(j) + V_fine(j) = V_fine(j)): (Z-con) levers;
(c) class-R carriers: (Z-gen) levers; lever efficiency mu_{j(l)}^2 v_l(j(l)) >= 1/Design(L) by (D-lev) with n_l.  The pull coordinates of
Lemma DC are taken among the contacts of f^# in S_l ∩ (s_max, s_far] with v_l(j_p) in [r, 2^{3G(L)} r] NOT used by Step A: Step A uses at most
two coordinates of each S_l beyond s_max (one TU pull, one bank), every window of v-values of ratio 2^{3G(L)} contains >= 3 elements of S_l
(bounded gaps G(L) = 2^{L+1}), every unused coordinate of S^nat_l is a contact with z = eps_l (V1 (C1)), and the extra factor 2^{2G(L)} <=
Design(L) enters C_2 only.  W_lev: carriers outside Omega meeting lever coordinates are at stages > L (allowedness (c): beyond s_max no coarse
target meets S_l), of total weight <= 2 c_{L+1}.  (U7): U1 Lemma 2.1.
Window quantities: T = 2^{-n} T_hi(w) <= 2^{-n}; gap_min, x_0 by CM^tr(b), (e); C_S by U1 Lemma 4.3; c_fine, c_tiny by X2-ref CM'/C_mix'
(carriers at stages > L have total weight <= C c_{L+1}, coefficients <= C_f lambda); r_0 by Lemma DC step (5) (r_0 is below the gaps of Omega
carriers and the margins of the peaks of f_0, divided by C_lev); K_J = 1 + 4/A_min since K_X = 0.
(W-a): (W_exp) and T_lo(L, M(L)) <= T give c_{L+1} <= exp(-1/T_lo(L, M(L))) <= exp(-1/T), so c_fine <= C_f exp(-1/T) <= c_late delta T/(n A_0)
for L large.  (W-b): K_J c_tiny <= C_f Design^C exp(-1/T) <= 1/4 and 2 K_J ||Y||_inf <= 2 K_J (C_f c_{L+1} + Design s_1 A_0/T) <= 1/2 for the s_1
of Lemma S2c^tr.  QED

### 2.4 Lemma PM (the Puiseux margin survives the levers).  PROVED.
Let f' be the d-consistent engineered approximant of Theorem UE built at f_0 := f^# (X2 3.2: theta-masses on W, cut-off at N'', lever
parameters P* of Lemma DC with |P*|_inf <= r).  Then:
 (i)   nv'_k = nv^#_k for every k in Omega (exact; Lemma DC), in particular for every active near-threshold carrier d of a (T)-block and every
       KN-1-held carrier;
 (ii)  |C'_m - C^#_m| <= C_f c_{L+1} for every block m;
 (iii) for every k in Omega, rho'_k = rho^#_k (1 - C^#_m) C'_m/(C^#_m (1 - C'_m)); hence |rho'_k - rho^#_k| <= C_f c_{L+1}, gap'(k) >= gap^#(k)/2,
       and rho'_d <= 1 - mu_kappa(eta'/3)/8 for d in N_T;
 (iv)  the lever moves of size O(r) change the values of carriers OUTSIDE Omega only: coarse peaks of f^# (relative margin >= u/2 >> C_lev r)
       and fine carriers (total weight <= C c_{L+1});
 (v)   for every lever parameter P with |P|_inf <= r (not only at the zero P*) no Omega carrier and no coarse peak changes status.
Proof.  (i) Definition 1.4 of X2 and the conclusion of Lemma DC.
(ii) By lem:threshold the norming functional of zeta_m satisfies |w(k)| = min(M, C |zeta(k)|/(Phi_k^2 A)) and ||D w||_2 = C; dividing C^2 =
sum_k Phi_k^2 w(k)^2 by C^2 shows that C_m is the unique root in (0, 1) of the CLAMP EQUATION
      F(c; v) := sum_k min(Phi_k (1 - c)/c, v_k)^2 = 1,     v_k := |nv_k|/Phi_k,   nv_k := zeta(k)/A.
Each term is nonincreasing in c, and the term of the natural peak k^nat_m of f (a peak with margin at every row of the ball of Lemma M2) is
Phi_*^2 ((1-c)/c)^2 near C, so F decreases with slope >= 2 Phi_*^2 (1 - c)/c^3 there.  At f^# and f' the Omega terms coincide (v'_k = v_k by
(i)); the terms of the coarse peaks of f^# equal Phi_k (1 - c)/c at both rows for c near C (their margins exceed the value moves); every
other term belongs to a fine carrier k and changes by at most min(Phi_k^2 ((1-c)/c)^2, 2 Phi_k ((1-c)/c) |v'_k - v_k|) <= 2 ((1-c)/c)
(|nv'_k| + |nv_k|), with sum_{fine} (|nv'_k| + |nv_k|) <= 2 (1 + ||U||) sum_{fine} lambda_k/A_min <= C_f c_{L+1} (|u_k(xhat)| <= ||u_k||_1
||xhat||_inf <= 1 + ||U||; sum_{l > L} lambda_l <= c_{L+1}/3 by (P2)).  The intermediate value theorem on [C - x, C + x] with x := C_f c_{L+1}
C^2/Phi_*^2 gives (ii).  (iii) For a strict non-peak rho_k = nu_k/theta = |zeta(k)| C/(Phi_k^2 A M) = v_k/(Phi_k (1 - C)/C); with v'_k = v_k this
is the formula; C and 1 - C are bounded away from 0 on the ball of Lemma M2, so |rho' - rho| <= C_f c_{L+1}.  gap = M(1 - rho) for strict
non-peaks, so gap'(k) >= gap^#(k) - C_f c_{L+1} >= gap^#(k)/2 (gap^# >= g_min(w); b <= min(eta', mu_min/8) <= 8 g_min/c_f, so C_f c_{L+1} <= C_f b^2 <= 64 C_f g_min^2/c_f^2 <= g_min/2 for L large).  For d in N_T: rho'_d <= 1 - mu/4 +
C_f c_{L+1} <= 1 - mu/8.  (iv) The levers act at private signature coordinates of Omega carriers ((SEP)); carriers meeting them are fine (2.3,
(U6)); coarse peaks have margins >= u theta Phi/(2m) >> C_lev r since r <= r_0.  (v) Lemma DC step (5): r_0 lies below every gap of an Omega
carrier and every margin of a coarse peak divided by the Lipschitz constant C_lev of the values in P; over the cube the largest value move is
<= delta_1 + C_lev r <= g_min/2.  QED
Remarks.  (1) The comparison asked for — lever moves O(r) versus the Puiseux margin mu_kappa — is: on Omega the levers act EXACTLY (no O(r) error;
only the frozen-C error C_f c_{L+1} <= C_f mu^2/64), and off Omega there is no near-threshold coarse carrier; along the continuation r <= r_0 ~
g_min(w)/C_lev is a requirement on s_1 contained in (LATE) (Lemma S2c^tr).  The Puiseux exponent enters only the WINDOW constants (K_w, r_0,
s_late), never K, D_cls, A_max or c_flat, which are of the form design x u^{-C}.  (2) Lemma PM needs the levers on ALL coarse strict non-peaks:
if one coarse strict non-peak is left untuned, C moves at first order and the margin is lost (X2-ref 1.2; numerics 4(N1) control).

### 2.5 Lemma S2c^tr (late threshold, violation masses, (W_exp)).  PROVED.
At the companion f^# of Lemma CM^tr (main stage L >= l_f, T = T_lo(w)):
 (i)   g_min(w) >= T^{5 Design(L) + 2} >= 2^{-6 log_2(1/T)^2} and x_0(w) >= T^{5 Design(L) + 3} >= 2^{-7 log_2(1/T)^2};
 (ii)  every window constant entering Theorem UE (K_w, the lever constants, C_S, 1/x_0, 1/gap_min, n, A_0/T) is <= exp(C_1 log^2(1/T)), and
       s_late(w) := c delta (T gap_min x_0/(n A_0 K_w))^{C} (X2-ref (p-UE5), C absolute and >= 3) satisfies s_late(w) >= exp(-C_2 log^2(1/T));
 (iii) eps^viol(w) <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/T <= exp(-1/(2T))/2; with s_1 := max(64 rho eps^viol/delta, exp(-1/(2T))):
       64 rho eps^viol <= delta s_1 ((VT')), s_1 <= s_late(w) ((LATE)), K_w (K_w s_1 + c_fine + tail_W) <= K T^2 (Theorem E^eng's requirement,
       X2-ref (p-E1)), s_1 >= exp(-1/(2T)) >> C Design c_{L+1}/delta (fine-carrier lever effects), and r <= r_0.
Proof.  (i) Lemma QC(c) with X1-ref Q2: mu_kappa(h) >= c_kappa h^{beta_kappa} for 0 < h <= h_kappa; here h := eta'/3 <= 1/Design(L) <= h_kappa,
c_kappa >= 1/Design(L), beta_kappa <= Design(L) ((S5)); L <= n(w), Design(L) <= n(w) (n(w) >= L 2^{L^3} Q(w) >= Design(L)) and n <= log_2(1/T),
so 3 L Design(L) <= 3 n^2 <= 1/T and eta'/3 >= T^5; hence mu_kappa(eta'/3) >= T^{5 Design(L)}/Design(L) >= T^{5 Design(L) + 1} (1/Design >= T),
c_f eta' >= T^5, and g_min >= T^{5 Design(L) + 2} for T small; the second forms use Design(L) <= log_2(1/T).  x_0 = c_f g_min Phi_min(L) with
Phi_min(L) >= 1/D(L) >= 1/Design(L) >= T.  (ii) K_w is a polynomial with absolute exponents in these quantities and in f-constants (X2 Lemma
UE-1, X2-ref (p-UE1)-(p-UE6)); the lever constants are <= C_f Design^C g_min^{-C} (2.3); everything is <= exp(C_1 log^2(1/T)) for T small (log
natural; by (i) log(1/g_min) <= 9 log^2(1/T) and log(1/x_0) <= 11 log^2(1/T)), and s_late >= exp(-C_2 log^2(1/T)) with C_2 := C (C_1 + 21).  (iii) (W_exp): c_{L+1} <= exp(-1/T), so eps^viol <= C_f T^{-1} log_2(1/T) exp(-1/T),
which is <= exp(-1/(2T))/2 and <= delta s_late/(64 rho) as soon as 1/(2T) >= C_2 log^2(1/T) + log(64 rho C_f/(delta T)), true for T small;
s_1 <= s_late since exp(-1/(2T)) <= exp(-C_2 log^2(1/T)) for T small; K_w^2 s_1 <= K T^2 because s_late contains (T/K_w)^{C} with C >= 3;
K_w c_fine <= exp(C_1 log^2(1/T)) C_f exp(-1/T) <= K T^2; tail_W is chosen <= K T^2/K_w (X2-ref (p-E1)); r <= 4 K_J (1 + 1/A_min)(Pi_X + T^4 s_1) +
8 K_J W_pull/A_min <= exp(C log^2(1/T)) s_1 + (super-small W_pull term) <= r_0, as s_late contains the factor (gap_min/K_w)^C.  QED
Comparison with X2 4.2: there gap_min >= c_f T^4/(L Design) gave K_w <= T^{-C'}; the Puiseux margin multiplies the exponents by O(Design(L)) <=
O(log(1/T)), so K_w <= exp(C log^2(1/T)) — still far below exp(1/T): (W_exp) as stated (X2-ref (p-W)) suffices and NO change of the design is
needed.  This confirms X1-ref's remark on Corollary IV^tr.2.  (Arithmetic check: 4 (N2).)

### 2.6 Theorem C^tr (every activity class is recovered; no (KN)).  PROVED (modulo the refereed tools cited).
Design T_fin (option (a); option (b) for patterns with stage 1 notin N_T), N fixed, f in S_{p_N^*} with F finite, g in C(f), rho < 1.  If for
infinitely many main stages L some clean sub-window w of L has a (class, cube) set S of at least n(w)/D_cls(w)^2 scales of ONE activity class
(of any kind) for the data of (g, rho), then (f, rho g) in cl NA((c_0, p_N), l_2^2).
Proof.  For each such (L, w) let f_L := f^# be the companion of Lemma CM^tr.  By Proposition BR the data of the scales of S form a window
family at f_L with (U1)-(U7); by Lemma PM the d-consistent engineered approximants f'_L of Theorem UE keep every status used (Omega carriers strict
non-peaks with gap' >= gap^#/2, coarse peaks peaks); by Lemma S2c^tr, (W-a), (W-b), (VT') and (LATE) hold with s_1 := max(64 rho eps^viol/delta,
exp(-1/(2T))), together with Theorem E^eng's requirement.  Hypotheses of Theorem E^eng (X2 4.1 with X2-ref (p-E1)) along main stages L_j -> infinity:
 (E-c) p*(g - g_{j,t}) <= K_j t with K_j = C_f (Design(L_j)/u(w_j))^C (CM^tr(c));
 (E-d) |S_j| >= n(w_j)/D_cls(w_j)^2 >= L_j 2^{L_j^3} (Design/u)^{C_U1 - 2 C_D}/C_{f,N}^2 (1.3(S6)), so |S_j| c_flat(w_j)/K_j >=
       c_f L_j 2^{L_j^3}/(C_f C_{f,N}^2) -> infinity (c_flat(w) >= c_f u(w), C_U1 - 2 C_D = C_K + 1); K_j T_hi(w_j)/|S_j| <= K_j C_{f,N}^2
       2^{-L_j^3}/(L_j Q(w_j)) -> 0; and theta_j/c_flat^2 <= C_f T^2 log(1/T)/u^2 -> 0 (T <= 2^{-Q(w)} <= 2^{-(4/u)^{20}});
 (E-e) eps_j = p*(f_{L_j} - f) <= theta_{w_j} T_lo(w_j)^2 (CM^tr(f)), T_lo(w_j) being the least scale of the window containing S_j;
 (E-f) Lemma S2c^tr.
The subset version of the averaging (U1 Lemma 2.4 applied to the proof of E^eng: only "sum over I_r of dyadic t < 2|r|/c_flat" and the count
|S| are used) gives (f, rho g) in cl NA.  QED

### 2.7 The route-X alternative (for the record)
(a) For classes with no active shift or one-signed, X1's Master Theorem IV^tr (X1-ref 10: U1-ref's MT IV' assembly with KN^tr) applies to T_fin:
T_fin = T^tr + (D-lev) + (W_exp); (D-lev) only enlarges Design; (W_exp) only shrinks c_{L+1}; route X uses c_{L+1} only as an upper bound and in
the absorber capacity ratio lambda_a/c_{L+1} >= 1/(2 Design(L)) (I2, I3, I6).  PROVED mod refereed tools.  One-signed classes are covered twice.
(b) For N = 1 every class is one-signed or has no active shift, so Corollary IV^tr.1 gives Master Theorem VI for p_1 by route X alone,
independently of X2, for option (a) and (stage 1 lies in block 2, absent from p_1; X1-ref W2) for option (b).
(c) Route X cannot replace route V for mixed classes (frustration; U1 5.4-5.5); route V must not use the absorbers (X2-ref 2.3).

## 3. Master Theorem VI and the density criterion

### 3.1 MASTER THEOREM VI.  PROVED (modulo the refereed results listed in 3.5; the combination argument of this round is unrefereed).
Let T_fin be the design of Section 1 and p_N the corresponding norm on c_0 (I = {1, ..., N}).
 (a) OPTION (a) (Martin-type norm, ||T_fin|| = c_1 < 1): for EVERY N >= 1 and every f in S_{p_N^*} whose base support F = supp a is finite,
     f is in Rec(p_N): (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f).
 (b) OPTION (b) (T_fin admissible with (T-a) holding with equality at stage 1, which lies in block 2):
     (b1) for N = 1 every f in S_{p_1^*} with finite base support is in Rec(p_1);
     (b2) for N >= 2 every f in S_{p_N^*} with finite base support and rho_1(f) != 1 is in Rec(p_N), where rho_1(f) is the relative position
          (lem:threshold) at f of the norm-one carrier (stage 1, block 2).  The case rho_1(f) = 1 is OPEN (3.6).
Proof of (a).  Fix N, f, g in C(f) and rho < 1.  Let l_f be the stage beyond which all f-constants are absorbed (as in U1-ref's MT IV' and X2's
Theorem UE: companions in the r_f/2-ball of Lemma M2, T_hi(w) <= t_1, C_f^{L^2} 2^{-L^3} small, T below the thresholds T_0(f, rho) of
Lemma S2c^tr).
Step 1 (a clean sub-window at every main stage).  For a main stage L the rate objects of level L evaluated at f are omega(L) real numbers: the
relative positions and margins (V1 (R1)-(R7)), V2's determinantal and shift objects, and the minors and cofactor polynomials of Gamma^#(kappa, a)
for every pattern kappa and class a of level L evaluated at the ratios r(f) (formula-1 kappa with the pattern's Omega: U1-ref 4.3, X1 2.2(iv),
X1-ref K1).  The M(L) = omega(L) + 1 sub-windows of L have pairwise disjoint bands (b(w), u(w)) (U4 Theorem 2.2(c): u(w^+) = b(w) < u(w); adding
(D1), (D2) only lowers b), and each object lies in at most one band; so some sub-window w(L) is CLEAN: every object is <= b(w) or >= u(w)
(V1 Theorem 2', U4 Lemma GW).
Step 2 (a large class set).  For the given (g, rho) each dyadic scale t of W(w(L)) has exactly one activity class (U1 2.3, U1-ref (p-a), 4.5),
and the class is of one of the three exhaustive kinds (no active shift, one-signed, mixed).  Pigeonhole over the <= (J+1) 3^J classes gives a
class a with >= n(w)/((J+1) 3^J) scales; Lemma CM^tr builds its companion; pigeonhole over the (A_max/eps)^p cubes of the normalization (U1
Proposition 2.2(c), (d), eps := c_f (u/Design)^C) gives a (class, cube) set S with |S| >= n(w)/D_cls(w) >= n(w)/D_cls(w)^2.
Step 3.  The hypothesis of Theorem C^tr holds at w(L) for EVERY main stage L >= l_f; hence (f, rho g) in cl NA.  As rho < 1 and g in C(f) are
arbitrary and cl NA is closed, f in Rec(p_N).  N was arbitrary and T_fin does not depend on N.  QED
Proof of (b).  (b1): stage 1 lies in block m_1 = 2, absent from p_1, so no pattern of p_1 contains it; by GEN_fin(b) the weights of all
carriers of p_1 are algebraically independent over k_0, and the proof of (a) applies verbatim (X1-ref W2); alternatively 2.7(b) (route X alone).
(b2): rho_1(f) != 1 and b(w) <= T_lo(w)^4 -> 0 give L_1 such that |rho_1(f) - 1| > b(w) for every sub-window w of every level L >= L_1; then stage 1
is not near-threshold at f, so stage 1 notin N_T(kappa) for the pattern kappa of f at any clean w of level L >= L_1; for these patterns GEN_fin(b)
applies and the design constants of (S5)-(S6) (restricted as stated there) are positive; the proof of (a) applies for L >= max(l_f, L_1).  QED

### 3.2 Corollary VI.1 (finite-F Lemma Z).  PROVED.
For T_fin (option (a), or option (b) with N = 1) and every N: Lemma Z holds at every first row with finite base support in the strong form
f' := f (no approximation of f is needed).  Proof: Master Theorem VI.

### 3.3 Theorem VI.2 (density <=> (LSC-trunc)) and Corollary VI.3.  PROVED.
Let T_fin be as above with option (a) (or option (b) and N = 1).  For every N >= 1 the following are equivalent:
 (i)  NA((c_0, p_N), l_2^2) is norm dense in L((c_0, p_N), l_2^2);
 (ii) (LSC-trunc)_N: for every f in S_{p_N^*}, g in C(f), rho < 1 and eps > 0 there is f' in S_{p_N^*} with FINITE base support such that
      p_N^*(f' - f) < eps and dist_{p_N^*}(rho g, C(f')) < eps.
Proof.  For S = (h_1, h_2) : (c_0, p_N) -> l_2^2, ||S|| <= p_N^*(h_1) + p_N^*(h_2).
(ii) => (i): given f in S_{p_N^*}, g in C(f), rho < 1, eps > 0, (LSC-trunc)_N gives f' with finite base support and g' in C(f') with
p^*(f' - f) < eps and p^*(g' - rho g) < eps; f' in Rec(p_N) by Master Theorem VI, so (f', g') in cl NA and ||(f', g') - (f, rho g)|| < 2 eps.
Hence (f, rho g) in cl NA for all f, g, rho, and prop:reduction(b) (every norm-one operator into l_2^2 is, after a rotation of l_2^2, of the form
(f, g) with g in C(f), and density holds iff all (f, rho g), rho < 1, lie in cl NA) gives (i).
(i) => (ii): lem:pair gives norm-attaining f_n -> f with rho g in Li_n C(f_n); every norm-attaining f_n in S_{p_N^*} equals nabla p_N(x_n) and
has its base part in c_00 (prop:smooth(c), prop:approximants), i.e. finite base support.  QED
This is Z5's Proposition 5.4 (T13a; refereed as a correct reformulation), whose first condition (Lemma Z at every f with finite base support) is
now PROVED for T_fin; the proof uses only prop:reduction(b), lem:pair, prop:smooth, prop:approximants (all [any T] in U4 4.2) and Master
Theorem VI (with Rec in place of R_0; NA ∩ S ⊂ Rec trivially: if f attains its norm at x_0 and g in C(f), then g(x_0) = 0 and (f, g) attains
its norm at x_0).  These results use (T-a) only as q^*(Te) <= 1 (through Phi_m(k) <= 2^{-m-k}); in the note the equality clause appears only in
def:admissible and in the verifications of admissibility (lines 144-154, 2344, 3990 of martin_density_note.tex), never in an argument.  Hence
Theorem VI.2 holds for the Martin-type norm of option (a).
COROLLARY VI.3 (Martin's p).  If (LSC-trunc)_N holds for infinitely many N, then NA((c_0, p), l_2^2) is dense for the Martin-type norm p (I = N)
built with T_fin.  Proof: Theorem VI.2 and lem:martintail (its proof uses only |R_m x|_m <= m 2^{-m} q(x), valid for ||T|| <= 1; T_fin is
N-independent).

### 3.4 The answers in one paragraph
For the single N-independent operator T_fin (option (a)), every first row with finite base support of every finite-block norm p_N is
recovered: all its mates are limits of norm-attaining operators (Master Theorem VI).  The two routes are compatible because they are used on
different rows and the only things route V takes from route X are the conclusions of Proposition KN^tr (exact cone, threshold protection,
coupling rows); KN-1's exact hold lives in the companion's joint fixed point, d-consistency transports it exactly to the engineered approximant,
and the Puiseux margin is protected there by the freezing of C_m (Lemma PM).  The non-explicit Puiseux exponent costs only a factor
O(log(1/T)) in the exponents of the window constants, which (W_exp) absorbs (Lemma S2c^tr).  Consequently density of NA((c_0, p_N), l_2^2)
is EQUIVALENT to (LSC-trunc)_N for every N (Theorem VI.2), and (LSC-trunc)_N for infinitely many N gives density for p (Corollary VI.3).

### 3.5 Dependency tree and status flags
Unrefereed (this round): T_fin and Lemma W_fin, Theorem A_fin, Lemma GEN_fin, checks I1-I10 (Section 1); Lemma CM^tr, Proposition BR, Lemma PM,
Lemma S2c^tr, Theorem C^tr (Section 2); Master Theorem VI, Corollary VI.1, Theorem VI.2, Corollary VI.3 (Section 3).
Refereed tools used (with the round's referee fixes):
 * note: lem:threshold, lem:F1 (clamp formula), lem:suplevel, eq:peakshift, def:twopiece, def:engineered and thm:engineered (proof), lem:block,
   lem:base, lem:bookkeeping, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence, lem:approxfacts, lem:anchor, def:SC, lem:scrambling,
   lem:slack, prop:reduction, lem:pair, prop:smooth, prop:approximants, prop:continuity, lem:martintail.
 * U4 + U4-ref: T_final, Lemma GW, Theorem 2.2; V1 (Theorem 2', Lemmas D, TU, CO, ST, moves (C1), (C2), Proposition TR(iii)-(iv)); V2 (Lemmas H,
   L, Theorem B); Z3 Lemma 3.1; U3 Lemma VT (U3-ref F6).
 * U1 + U1-ref (single pass; several statements proved BY the referee): Lemmas 1.1-1.5, 2.1, 2.4, classes 2.3 (p-a), Proposition 2.2 ((p-b)-(p-d)),
   Lemma 3.2 under D^{U1'} (6.4), Lemmas 4.1-4.3, 4.5, 4.6, Lemma R-kt, Proposition KN (for (KN)-blocks), rows 4.1-4.5, G1 release, D^{U1'}, Lemma
   4.2(ii) repair.
 * X1 + X1-ref (single pass; fixes proved by the referee): Lemmas K, F, EC, the floor row (X4^0) and weight-freeness, Lemmas NLM, GEN, QC,
   Proposition KN^tr (KN-1, D2, S-0, K1, Q1-Q3, W-fix), Lemma W' (W1-W4).
 * X2 + X2-ref (single pass; (R-abs), Lemma CM', Theorem C_mix' proved BY the referee and re-derived here as Lemma CM^tr / Theorem C^tr):
   Lemmas M1, M1', M2, identities 1.4 with the referee addition 1.2, Lemma DC ((p-DC1)-(p-DC3)), Lemma LV(a)-(c) ((p-LV1), (p-LV2)), Lemma UE-1
   and Theorem UE ((p-UE1)-(p-UE7), (c3')), Theorem E^eng ((p-E1)), (S2c) with (W_exp) ((p-W)), design D^{X2}.
 * Z5 Proposition 5.4 (refereed), re-proved in 3.3.
NOT used: Master Theorems II, III' and V4's results (the class pigeonhole covers every F-finite row directly); (W5), (W6), (W7) at absorber or
cluster stages, (FD); Theorem S1's RT*(c) and the zero-value absorbers (route X, an alternative only).

### 3.6 What remains open (precise)
 (O1) (LSC-trunc)_N for some/every N — by Theorem VI.2 EQUIVALENT to density for p_N built with T_fin.  It is the infinite-base-support half of
      Lemma Z (Z5 T13; U4's (E1)-(E5) and U2's items: transport of the finite-F master theorems to infinite F (M-inf, SKETCH), tuning regularity
      modulus, (W_inf), (SC) along deep raises, status coherence at infinite F).  Nothing here bears on it.
 (O2) Option (b), N >= 2: rows with rho_1(f) = 1 exactly at which stage 1 is an active near-threshold carrier of a (T)-block at clean
      sub-windows of infinitely many levels, with a coincidence on the slice Phi_1 = 2^{-3} (Phi_1 rational, so Lemma GEN does not apply).
      Precisely: whether 2^{-3} can be a critical value of psi_1 restricted to a stratum of Z_kappa for all values of the generic parameters
      (X1-ref W2 slice remark; if 2^{-3} is a regular value of psi_1 on every stratum, the slice version of Lemma NLM settles it).  Under option
      (a) this does not arise; option (b) for N = 1 is settled (3.1(b1)).
 (O3) Arbitrary admissible T (Martin's own Lemma B operators): Master Theorem VI is proved for the designed T_fin only.
 (O4) Martin's p (I = N): by Corollary VI.3 density follows from (LSC-trunc)_N for infinitely many N; row-wise statements do not transfer.
No counterexample is claimed; nothing found points to one.  Density of NA((c_0, p_N), l_2^2) (every N) and of NA((c_0, p), l_2^2) remain OPEN,
now reduced EXACTLY to (LSC-trunc) for the Martin-type norms built with T_fin.

## 4. Numerics (sanity checks only; r10/Q1_work/)
 (N1) pm_check2.py (+ pm_check2.out: 12 instances, 50 digits), pm_check3.py (80 digits, 520 bisection steps; pm_check3_80full.out: all 12
      instances; pm_check3.out: the first 7) and pm_check3_50.py (+ pm_check3_50.out: the same 12 instances at 50 digits): an independent
      block model (mpmath) solving the threshold equations (E1), (E2); robust peaks, one near-threshold strict non-peak d tuned to rho_d = 1 - mu
      with mu in {1e-8, 1e-12, 1e-16, 1e-20}, fine carriers of total weight mu^2 (as c_{L+1} <= b^2 <= mu^2/64), every value perturbed by a
      relative amount r in {1e-3, 1e-4, 1e-2, 1e-5} >> mu.  Untuned, the perturbation moves rho_d by ~r and makes d a PEAK in 7 of 12 instances;
      after imposing d-consistency on ALL coarse strict non-peaks (fixed point in A'), rho_d = 1 - mu to all printed digits in all 12 instances
      (mu down to 1e-20) and |C' - C| <= 1.6e-73 (working precision at 80 digits); the clamp-equation bound of Lemma PM(ii) holds.  CONTROL:
      with one coarse strict non-peak left untuned, |C' - C| ranges over 3e-9 ... 1.3e-4 and d becomes a PEAK in 6 of 12 instances (Lemma PM needs
      the levers on all of Omega, X2-ref 1.2).  [pm_check.py, a full row model with masses, was too slow and was replaced; the row-level lever
      mechanism is X2's Lemma DC, checked numerically by X2 and X2-ref.]  At 50 digits (pm_check3_50.out) |C' - C| reaches 1e-27 ... 1e-19 for
      mu = 1e-16, 1e-20: a bisection-resolution artefact (bracket [0, max nu] with nu ~ 1/Phi_fine up to 1e40), absent at 80 digits.
 (N2) s2c_check.py (+ .out): log_2-scale arithmetic of Lemma S2c^tr with the worst case Design(L) = n(w) and absolute exponents C in {3, 10, 30},
      f-constants up to 1e12: the threshold comparison 64 rho eps/delta <= s_late and exp(-1/(2T)) <= s_late hold for all n >= 16 ... 23 (T = 2^{-n});
      at n = 60, log_2 s_late ~ -4e5 ... -3.4e7 against log_2(64 rho eps/delta) ~ -1.7e18.  (In T_fin, n(w) >= L 2^{L^3} Q(w) is astronomically larger.)
These checks cannot exhibit infinite-dimensional failures; they confirm the two quantitative mechanisms new in this round.

## 5. Points for the referee
 * Lemma CM^tr's proof claims that X2-ref's CM' uses Proposition KN only through (i) statuses, (ii) kind-[3] rows, (iii) exactness; check
   X2-ref 4 ((a)-(d)) line by line against this claim, in particular the dominance (U1 Lemma 4.2) and the trace-correction bound with the
   TRUE shift in (T)-blocks (X1-ref S-0).
 * The KN-1 hold is realized INSIDE Step A's joint fixed point; Step B's G1 release moves the held values by <= 4 c_{L+1}^2 — check that
   X1-ref's S-0 indeed covers the G1 release in route V (no absorber tuning in between).
 * Lemma PM(ii): the clamp-equation argument requires that the coarse peaks stay clamped and that the natural peak gives a slope bound on the
   ball of Lemma M2; fine status changes are covered by the min(...) bound.
 * Lemma S2c^tr: K_w is polynomial in 1/gap_min, 1/x_0 with ABSOLUTE exponents (X2 Lemma UE-1, X2-ref (p-UE1)-(p-UE6)); if some exponent were
   design-dependent the bound exp(C log^2(1/T)) would become exp(C Design log^2(1/T)) <= exp(C log^3(1/T)), still dominated by (W_exp).
 * The pull coordinates of Lemma DC are chosen unused by Step A (2.3); the extra factor 2^{2G(L)} enters only C_2.
 * Option (a) leaves the note's class only through the equality clause of (T-a), which no argument uses (3.3).
