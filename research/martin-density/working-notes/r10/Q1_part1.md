# Q1 part 1 — the final design T_fin: one well-founded recursion, admissibility, N-independence, genericity, survival

Setting: note (paper/martin_density_note.tex) Sections 1, 7, 8; finite block sets I = {1..N} (p = p_N), every N >= 1 at once.
Sources combined: U4 1.1-1.3 (T_final, refereed U4-ref), U1-ref 6.2-6.4 (D^{U1'}), X1 3.1 with X1-ref 8-9 (T^tr: rate objects
of KN^tr, thresholds (D1), (D2), generic weights, fixes W1-W4), X2 6.1 with X2-ref (p-W), (p-LV1) (D^{X2}: (D-lev) with n_l,
(W_exp) after main stages only).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.1 Data fixed in advance (D0_fin)
 (i)   Base: H = l_2 with orthonormal basis (k_s); mu_s := 2^{-s^2-1}; U k_s := mu_s e_s (diagonal, compact, dense range, ||U|| = 1/4).
 (ii)  Signatures: S_l := {2^l(2i+1) : i >= 1} (l >= 1; pairwise disjoint, even, bounded gaps G_l = 2^{l+1}); Z_0 := N \ union S_l;
       h_l := sum_{s in S_l} 2^{-s} e_s^*, H_l := ||h_l||_1 (rational), delta^max_l := min{2^{-l}, (4(1 + ||U||) H_l)^{-1}}, tau_l := 2^{-l}.
 (iii) Target pool: Y_pool := {x/q^*(x) : 0 != x in c_00 with rational entries}, enumerated as (y^(i))_{i>=1} with y^(1) := e_1^*/q^*(e_1^*);
       Y_pool is dense in S_{q^*} and contains V4's (Z0)-targets.  Absorber pool: A_pool := {x/q^*(x) : x = beta e_s^* + e_{p_0}^* +
       4 sum_{r=1}^R 2^{-r} e_{p_r}^*, s >= 1, beta = +-1, R >= 1, p_0 < ... < p_R odd} (U1 (A0)).  P_Y := Y_pool ∪ A_pool (countable).
 (iv)  Schedules: a block sequence (m_r)_{r>=1} with m_1 := 2 in which every m >= 1 occurs infinitely often; a sequence (i_nu)_{nu>=1} in
       which every positive integer occurs infinitely often.
 (v)   OPTION: (a) the weight of stage 1 is generic as below (Martin-type norm, ||T|| = c_1 in [1/2, 1)); (b) c_1 := 1 ((T-a) with equality).
 (vi)  The field k_0.  For y in P_Y and l >= 1 let delta(y, l) be the (GM)-value of 1.3(S2) (delta^max_1 if l = 1), n(y, l) := q^*(y +
       delta(y, l) h_l).  k_0 := Q({y(j), delta(y, l), n(y, l) : y in P_Y, l, j >= 1}).  k_0 is countable (P_Y, N countable).
       Every (GM)-value lies in Q(y(j) : j) (it is delta^max_l or an endpoint (eps g_l - sum sigma_j y(j))/H_l of an excluded interval, and
       g_l, H_l, delta^max_l are rational), but n(y, l) may be transcendental; it is put into k_0 by definition.

## 1.2 Rounds (D^{U1'}, U1-ref 6.2, made explicit)
Round r = 1, 2, ...; l_r := number of stages before round r (l_1 := 0).
 (r.1) Candidate: m := m_r, nu := #{r' <= r : m_{r'} = m}, y := y^(i_nu); Sigma(y) := supp y ∩ union_{l'} S_{l'}; p := l_r + 2|Sigma(y)| + 1.
       y is ALLOWED (with margin) if (a) supp y ∩ S_{l'} = {} for all l' >= p and (c+) supp y ∩ S_{l'} ⊂ [1, p - 2|supp y| - 1] for all l' < p.
       If allowed, Y_r := y; otherwise Y_r := y^(1) (supported in Z_0) and p := l_r + 1.  Put p_r := p.
 (r.2) PRE stages l_r + 1, ..., p_r - 1: for each s in Sigma(Y_r) (increasing), two consecutive block-1 stages with absorber targets for
       (s, +1) and (s, -1).
 (r.3) MAIN stage p_r: block m_r, target Y_r.
 (r.4) CLUSTER stages p_r + 1, ..., p_r + R_cl(p_r), R_cl(p) := 2|E^ch(p)|, E^ch(p) := T(p) ∪ union_{l'' <= p} (S_{l''} ∩ [1, p]),
       T(p) := union_{l'' <= p} supp y_{l''}: for each s in E^ch(p) two consecutive block-1 stages with absorber targets for (s, +-1).
       l_{r+1} := p_r + R_cl(p_r).
Every stage l has a block m(l) and k(l) := 1 + #{l' < l : m(l') = m(l)}; j(k, m) := the k-th stage of block m (strictly increasing in k,
which is all U4 1.2(i) requires of the ladder).  Round 1: Sigma = {} (no target meeting a signature set is allowed at stage 1), so stage 1
is the MAIN stage of round 1, in block m_1 = 2 (X1-ref W2).  (FD) stages are not used (U4 C6: only V4's negative Prop. 5.8 needs them).
Absorber target at a PRE or CLUSTER stage l for (s, beta): p_0 < ... < p_R the least odd integers > max(9, max T(l-1)), R = R(l) the least
integer >= 1 with 2^{3-R} <= mu_{p_0}^2 lb_l^2/4, where lb_l is the a-priori lower bound of c_l defined in (S4) (computed before y_l).

## 1.3 Stage l (any type), given everything of earlier stages
 (S1) target y_l (from 1.2); for absorber stages first lb_l (S4), then R(l), then y_l.
 (S2) delta_1 := delta^max_1; for l >= 2 ((GM), U4 1.3(2)): g_l := delta^max_l H_l/(32 * 3^{|supp y_l|}), delta_l := the largest delta in
      [delta^max_l/2, delta^max_l] with |sum_j sigma_j y_l(j) + eps delta H_l| >= g_l for all sigma in {-1,0,1}^{supp y_l}, eps = +-1.
 (S3) n_l := q^*(y_l + delta_l h_l), u_l := (y_l + delta_l h_l)/n_l, v_l := delta_l h_l/n_l, delta°_l := delta_l H_l/n_l,
      eta_l := min(1, min_{supp y_l} |y_l(j)|), Lambda°(l) := prod_{l'' <= l} (1 + 2/delta°_{l''}).
 (S4) WEIGHT.  c^max_l := the minimum of the upper bounds of D^{U1'} at stage l, computed from the ACTUAL earlier data:
       PRE and MAIN stages: (W1) c_{l-1}/4; (W2) b(l-1, M(l-1))^2; (W3) (delta_l H_l)^2; (W4'') tau_{l'} 2^{-2s} c_{l'} delta_{l'}
         T_lo(l-1, M(l-1))^3/2 (l' < l, s in supp y_l ∩ S_{l'}); (W5) c_{l-1} delta_l 2^{-min S_l - l - 10}/(1 + ||U||); (W7) as U4 1.3(4);
         MAIN stages also (W6) g_l 2^{m(l)+k(l)-l}.
       CLUSTER stage p + i (p a main stage, 1 <= i <= R_cl(p)): c^max_{p+i} := min(c^cl(p) 4^{1-i}, c_{p+i-1}/4) (X1-ref W3), where
         c^cl(p) := min{ c_p/4, b(p, M(p))^2, (delta^max_{p+1} H_{p+1}/2)^2, (W4'') at stage p+1 for every s in E^ch(p) (T_lo read at the main
         stage p, U1-ref 6.2), (W5), (W7) at stage p+1 with delta_{p+1} replaced by delta^max_{p+1}/2, and  (W_exp) exp(-1/T_lo(p, M(p))) }.
       [(W_exp) is imposed only here, i.e. on the first weight after each MAIN stage (X2-ref (p-W)); all later weights inherit it by (W1).]
       A-priori lower bounds (used for absorber targets, X1-ref W3): PRE stage l: lb_l := (1 - 2^{-l}) c^low_l, c^low_l := min{c_{l-1}/4,
         b(l-1, M(l-1))^2, (delta^max_l H_l/2)^2, (W4'') at s, (W5) with delta^max_l/2, (W7)} (independent of R; c^low_l <= c^max_l); CLUSTER
         stage p+i: lb_{p+i} := (1 - 2^{-(p+i)}) c^max_{p+i} (c^max_{p+i} does not depend on the target).
       GENERIC CHOICE: c_l := any number in [(1 - 2^{-l}) c^max_l, c^max_l] that is transcendental over k_0(c_1, ..., c_{l-1}) (l >= 2;
       under option (a) also l = 1 with c^max_1 := 1, i.e. c_1 in [1/2, 1)); option (b): c_1 := 1.  [Possible: the interval has positive
       length, the field is countable.]  Phi_l := 2^{-m(l)-k(l)} c_l, lambda_l := m(l) Phi_l.
 (S5) LEVEL DATA (U4 1.3(5) + U1 (A4) + U1-ref 4.3 + X1 3.1(i)-(ii) + X2 (D-lev)).  T(l), s_max(l), sigma(l), sigma_2(l) := max_{l'' <= l}
      (second element of S_{l''} beyond s_max(l)), m^nat, D(l), delta_min(l), G(l), B_mu(l) := 2^{sigma(l)}/mu_{sigma(l)}^2, G^*, H_comb, G^**,
      Xi^Y, the patterns, cones, rays and H_tune of V1, the shift objects of V2, the determinantal objects pi_O of V2, the minors and
      cofactor polynomials of U1-ref 4.3 (ratio variables) and of X1 2.2(iv) ((X4^0) rows in (T)-blocks, (X4) in (KN)-blocks, U-rows)
      for ALL patterns kappa and classes a of level l (over all blocks m(l''), l'' <= l: N-free), the constants Lip(l), C_L(l), N_L(l)
      (V2 Lemma L in semialgebraic form on the compact sets K_kappa, X1-ref Q3), and for every pattern kappa of level l the Lemma QC data
      (Z_kappa, F_Phi, mu_kappa(h), m_0, C_Y, alpha_Y, c_kappa, beta_kappa, h_kappa; X1-ref 5-7) computed with the ACTUAL weights.
      RATE OBJECTS of level l: all of the above objects; omega(l) := their number.
        Design(l) := [U4's Design(l)] x 4^{R_cl(l)} 2^{k(l + R_cl(l))} eta_l^{-1} (U1 (A4), at main stages)
                     x max_kappa [Lip_kappa C_Y(kappa) m_0(kappa)^{-1} c_kappa^{-1} beta_kappa h_kappa^{-1}] (X1-ref Q2)
                     x max_{l'' <= l} 2^{sigma_2(l)} n_{l''}/(mu_{sigma_2(l)}^2 delta_{l''})   ((D-lev), X2-ref (p-LV1)).
 (S6) SUB-WINDOWS (every stage; used only at main stages).  M(l) := omega(l) + 1; for w = (l, i), 1 <= i <= M(l), with predecessor w^-:
      u(w) := 1/4 (w = (1,1)), u(w) := b(w^-) otherwise; Q(w) := max{(4 Design(l)/u(w))^{omega(l)+20}, D_cls(w)^2 (Design(l)/u(w))^{C_U1}}
      (U1 (A4)); n(w) := ceil(l 2^{l^3} Q(w)); T_hi(w) := min{T_lo(w^-), 2^{-l^3}/(l Q(w))}; T_lo(w) := 2^{-n(w)} T_hi(w);
      eta(w) = eta'(w) := T_lo(w)^4/(l Design(l));
      b(w) := min{ b_U4(w), b_X1(w) },  b_U4(w) := min{eta(w), (eta(w)/C_L(l))^{N_L(l)/2}}/(1 + Lip(l) C_*(l)),
      b_X1(w) := the largest b > 0 with (D1) C_L ((1 + Lip C_*) b)^{2/N_L} <= eta'(w)/3 and (D2) delta_0(b) <= min_kappa min(m_0(kappa)/2,
      (eta'(w)/(3 C_Y(kappa)))^{1/alpha_Y(kappa)}) and b <= min_kappa mu_kappa(eta'(w)/3)/8, where delta_0(b) := (1 + Lip C_*) b +
      Lip C_L ((1 + Lip C_*) b)^{2/N_L} + C D(l)^2 b.  [Each left side is continuous, increasing, -> 0 as b -> 0 and each right side is a
      positive number already computed, so the admissible b form an interval (0, b_X1(w)]; the max of (D2)'s second clause uses M <= 1.]
 (S7) T_fin e_{k,m} := c_{j(k,m)} u_{j(k,m)}, extended linearly and continuously to l_1(N x N).

## 1.4 Lemma W_fin (well-foundedness, positivity, N-freeness).  PROVED.
(a) Every quantity of stage l is a function of (D0_fin), of quantities of earlier stages and of earlier steps of stage l.
(b) All divisors are finite and positive, every interval used for a choice is nonempty.  (c) Nothing depends on N.
Proof.  (a) (S1): the round structure uses supports of earlier targets, S_{l'}, the schedules; for absorber stages lb_l is computed from
c_{l-1}, b(l-1, M(l-1)) (stage l-1's (S6)), delta^max_l, H_l, s, (W5)/(W7)-data of stage l-1 — or, at clusters, from c^cl(p) (data of the
main stage p: c_p, b(p, M(p)), T_lo(p, M(p)), E^ch(p)) and c_{p+i-1} — then R(l), then y_l.  (S2) uses y_l; (S3) y_l, delta_l; (S4) earlier
weights, b(l-1, M(l-1)), T_lo(l-1, M(l-1)) and stage-l data, and k_0(c_1..c_{l-1}) for the generic choice; (S5) data of index <= l including
c_l (the QC data use the actual weights of carriers <= l only); (S6) Design(l), omega(l), the Lemma L and QC constants, and the predecessor
values T_lo(w^-), b(w^-).  The only "future" requirements are imposed later: (W2), (W_exp) and the (SF_tau) clause (W7) at stage l+1.
(b) As U4 Lemma W(b) for T_final's objects; c^max_l > 0 (finitely many positive bounds; (W4'') is a finite list); lb_l > 0; R(l) exists
since 2^{3-R} -> 0; QC data: mu_kappa(h) > 0 for h > 0 (Lemma QC(a), given GEN_fin below), C_Y, m_0, c_kappa, h_kappa, beta_kappa
positive finite (Lemma QC(b),(c)); b_X1(w) > 0 (right sides positive).  (c) No rule refers to N; patterns of level l range over subsets of the
finitely many carriers l'' <= l and their blocks.  For p_N, rate objects of carriers with m(l'') > N take the value 1 (V1-ref p0) and the
patterns of p_N are a subset of the patterns of level l; the design constants dominate all of them.  QED

## 1.5 Theorem A_fin (admissibility; Martin's Lemma B).  PROVED.
(a) q^*(T_fin e_{k,m}) = c_{j(k,m)} <= c_1, with c_1 in [1/2, 1) under option (a) and c_1 = 1 under option (b) (equality at (k, m) = (1, 2)).
(b) (T-b) T_fin is injective; (T-c) Y := T_fin(l_1(N x N)) satisfies Y ∩ c_00 = {0}; (T-d) for every m, {u_{j(k,m)} : k} is dense in S_{q^*}.
(c) Hence under option (b) T_fin is admissible (def:admissible) and satisfies the conclusion of Martin's Lemma B; under option (a) it
    satisfies (T-b), (T-c), (T-d) and (T-a) without the equality clause: ||T_fin|| = c_1 <= 1, which is all Martin's proof uses
    (X1-ref W1: v*_{n,m} in B_Y, ||Phi_m||_1 <= 2^{-m} < 1 in Lemma A, |R_m x|_m <= m 2^{-m} |||x|||, norm density of the normalized vectors
    in Proposition 3), so p_N and p are MARTIN-TYPE norms (Martin's construction verbatim with an operator of norm <= 1; his Remark 2).
Proof.  (a) c_l <= c_{l-1}/4 (W1) for l >= 2 (at cluster stages by c^max_{p+i} <= c_{p+i-1}/4, at PRE/MAIN stages by (W1)).
(T-b), (T-c): U4 Theorem 2.2's argument.  Let x in l_1, Z := T_fin x = sum_l x_l c_l u_l in c_00 and x_{l'} != 0.  Every target satisfies
allowedness (a): main targets by (r.1); absorber targets for (s, beta) at stage l' ' have supp = {s, p_0, ..., p_R} with p_i odd (in Z_0) and
s in Z_0 or s in S_{l''} with l'' < s <= stage (for PRE pairs, s <= p - 2|supp Y_r| - 1 < l_r + 1 by (c+); for cluster pairs of a main stage p,
s in T(p) ∩ S_{l''} forces l'' < (stage of the target containing s) <= p, and s in S_{l''} ∩ [1, p] forces l'' < s <= p).  So for s in S_{l'}:
u_l(s) = 0 for l < l', u_{l'}(s) = delta_{l'} 2^{-s}/n_{l'}, other signatures vanish on S_{l'}.  Every target meeting s in S_{l'} at a stage
l > l' satisfies (W4): c_l <= tau_{l'} 2^{-2s} c_{l'} delta_{l'}/2 ((W4'') at PRE/MAIN stages; at cluster stages c_l <= c^cl(p), which contains
(W4'') at every s in E^ch(p), and s in E^ch(p) for every cluster target).  Hence, with L(s) the least such l, sum_{l >= L(s)} c_l <=
(4/3) c_{L(s)} and |Z(s)| >= c_{l'} delta_{l'} 2^{-s} (|x_{l'}|/n_{l'} - (8/9) ||x||_inf 2^{-s}) > 0 for all large s in S_{l'}, contradicting
Z in c_00.  (T-d): fix m and i.  Block m is the main block of infinitely many rounds (every m occurs infinitely often in (m_r)); at its
nu-th such round the candidate is y^(i_nu), and i_nu = i for infinitely many nu.  The candidate y^(i) is allowed with margin at every main
stage p > p_i := 1 + max(supp y^(i)) + 2|supp y^(i)| (then (a): S_{l'} ∩ supp y^(i) != {} forces l' < min S_{l'} <= max supp y^(i) < p; (c+):
supp y^(i) ⊂ [1, p - 2|supp y^(i)| - 1]).  Main stages increase, so y_l = y^(i) at infinitely many stages l of block m, and q^*(u_l - y^(i))
<= |1/n_l - 1| + q^*(delta_l h_l)/n_l <= 4 (1 + ||U||) 2^{-l} H_l -> 0.  Density of Y_pool in S_{q^*} gives (T-d).
(c): rem:lemmaB / U4 Theorem 2.2(b): Y is a separable operator range, dense (its closure contains a dense subset of S_{q^*}), Y ∩ NA((c_0,q))
= Y ∩ c_00 = {0} (prop:smooth(c)), normalized vectors of each block dense in S_{q^*} ⊃ S_Y.  QED

## 1.6 Lemma GEN_fin (algebraic independence; all non-weight data in k_0).  PROVED.
(a) Every non-weight datum of every stage lies in k_0: y_l in P_Y always (main targets in Y_pool, absorber targets in A_pool, whatever the
integers R, p_i, s, beta are), delta_l = delta(y_l, l), n_l = n(y_l, l), u_l(j) = (y_l(j) + delta_l 2^{-j} 1_{S_l}(j))/n_l, mu_s, H_l, the
aggregated signature coefficients ||v_l 1_{S_l ∩ [1, s]}||_1 (any integer s), and all integers (m(l), k(l), stage types, s_far).
(b) Option (a): (c_l)_{l>=1} is algebraically independent over k_0; option (b): (c_l)_{l>=2} is.  Hence for every finite set D of stages
(not containing stage 1 under option (b)) the weights (Phi_d)_{d in D} are algebraically independent over k_0(Phi_l : l notin D).
Proof.  (a) Definitions (1.1(vi), 1.2, 1.3).  (b) Induction: if c_1..c_n are algebraically independent over k_0 and c_{n+1} is transcendental
over k_0(c_1..c_n), then c_1..c_{n+1} are algebraically independent over k_0.  Phi_l is a nonzero rational multiple of c_l.  QED
Consequently X1's Lemma GEN (X1-ref 6) applies to every pattern kappa of every level, except — under option (b) — patterns with stage 1
in N_T(kappa); under option (b) and N = 1 no pattern of p_1 contains stage 1 (block 2 is absent from p_1): X1-ref W2.

## 1.7 Survival audit.  PROVED (by the cited refereed audits plus the interaction checks I1-I10).
Features of T_fin: (F1)-(F9), (F11) of U4 Theorem 2.3 [SLD structure with (P1)-(P3) per sub-window, bounded gaps, allowedness (a), (c),
mu-base, private banks/pulls, pigeonhole sub-windows, rate scheme, b(w) a design power of T_lo(w), Design(l) dominating all earlier design
factors incl. B_mu (fix C1), c_{l+1} <= c_l/4, <= b(l, M(l))^2, <= (delta H)^2; N-free]; (F10) only partly ((W5), (W7), (W6) not at absorber
or cluster stages; (FD) absent); (F12) D^{U1'}'s absorbers (pre-pairs, clusters, (A0), (W4''), Lemma 3.2 under D^{U1'}, U1-ref 6.4);
(F13) X1's rate objects and thresholds (D1), (D2), Design factors; (F14) generic weights; (F15) (D-lev) with n_l; (F16) (W_exp) after main stages.
Refereed audits covering the features separately: U4 + U4-ref (T_final: Lemma GW; trees of MT II, MT III', RS'); U1-ref 6.3 (D^{U1'}: admissible,
N-free, lost features (W5), (W7), (W6) at absorber/cluster stages unused on U1's tree); X1-ref 9 (T^tr = T_final + D^{U1'} + generic weights:
W1-W4; Lemma W'); X2-ref (p-W), 6.1 (D^{X2} = D^{U1'} + (D-lev) + (W_exp): admissible, N-free, refereed results survive).
Interaction checks (the only pairs of features no single audit covered):
 I1 (F14) x upper bounds: c_l <= c^max_l, the minimum of ALL upper bounds of D^{U1'}, (W_exp), cluster rules, computed from the actual
    earlier weights.  Every upper-bound use survives verbatim.
 I2 (F14) x lower-bound uses (complete list, X1-ref W4 plus D^{U1'}): s_1 = T_lo^8 c_l and (VT) c_l >= C' D T_lo (U3-ref RT*(f), F7 — not
    on the tree of Master Theorem VI, listed for completeness); absorber capacity lambda_a >= c_{L+1}/(Design(L)) at cluster stages
    (U1 3.5(c)): c_{L+i} >= prod_{j <= i} (1 - 2^{-(L+j)}) c^cl(L) 4^{1-i} >= (1/2) c^cl(L) 4^{1-i} by induction from c^max_{L+i} = min(c^cl 4^{1-i},
    c_{L+i-1}/4); consecutive block-1 ratio >= 8 (U1-ref 7): from the upper bound (W1) and k increasing; design-computed lower bounds
    lambda_l >= 1/D(l), Phi_min(L) >= 1/D(L) (computed after c_l).  All survive with factors in [1/2, 1].
 I3 (F14) x (F12) absorber targets: R(l) is computed from lb_l <= c_l, so 2^{3-R} <= mu_{p_0}^2 lb_l^2/4 <= mu_{p_0}^2 c_l^2/4, which is the only
    property of R used (U1 Lemma 3.3(i): the sweep Theta in [0, c_p^2] covers an interval of length >= mu_{p_0}^2 c_p^2/2 >= 2^{4-R}); R is
    still fixed before c_l (X1-ref W3).
 I4 (F14) x (F16): (W_exp) is one of the upper bounds in c^cl(p) <= c^max_{p+1}; the generic weight lies below it.
 I5 (F14) x (F15): (D-lev) involves no weight.
 I6 (F16) x (F12): (W_exp) acts only on c^cl(p) (first weight after a main stage; X2-ref (p-W)); all later weights, cluster or not, are <= it
    by (W1)/cluster rule; R of cluster absorbers uses lb_{p+i}, which already contains (W_exp); D^{U1'}'s ratio c_{p+i} ~ c^cl 4^{1-i} (within
    the factor 1/2 of I2) is unchanged.
 I7 (F16) x (F13): T_lo(p, M(p)) is computed in (S6) of stage p after every b(w) of level p, (D1), (D2) included; (W_exp) is imposed at stage p+1.
 I8 (F13) x (F12): (D1), (D2) only lower b(w); Q(w) only grows (U1's D_cls enlargement is a max); Lemma GW (U4 4.1) applies: every window
    condition is monotone under enlarging Design(l) and shrinking b(w), T_lo(w) and the weights.
 I9 (F15) x everything: a lower bound on Design(L) only (Lemma GW).
 I10 genericity x non-weight data: Lemma GEN_fin(a) — the integers R(l), p_i, s, k(l) depend on weights but the data they select lie in k_0;
    thresholds b, u, T_lo, Design depend on weights but are not cone coefficients (X1-ref 6).
Conclusion: every refereed result on the dependency tree of Master Theorem VI (listed in part 3) holds for T_fin with "level" read as "main
stage", exactly as for D^{U1'} (U1 Theorem 3.1(c), U1-ref 6.3), for T^tr (X1 Lemma W'(4)) and for D^{X2} (X2 6.1).
