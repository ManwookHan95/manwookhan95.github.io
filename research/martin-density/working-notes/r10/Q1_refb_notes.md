# Q1 referee (b) — notes with proofs (design T_fin, Martin's Lemma B, genericity, weight bounds, Lemma PM, escape search)

Scope: r10/Q1_notes.md (= Q1_notes_a/b/c; part files Q1_part0..3), checked against the refereed sources it cites: U4 1.2-2.2 (T_final), U1 3.1-3.4
(D^{U1}, absorbers, Lemma 3.3), U1-ref 5-8 (G1 release, D^{U1'}, Lemma 4.2(ii) in absorber blocks, MT IV'), X1 1.1-3.1 + X1-ref 6-9 (Lemmas K, F, floor row,
NLM, GEN, QC, KN^tr, KN-1, S-0, W1-W4), X2 2.3 (Lemma LV, (D-lev)) + X2-ref 3-4 ((p-W), (p-UE5), (p-E1), Lemma CM', C_mix'), the note (def:admissible,
lem:threshold, lem:martintail, lem:pair).  Working files: r10/Q1_refb_part1..3.md.  Scripts and outputs: r10/Q1_refb_work/.
Labels: PROVED (re-derived here), PRECISION (fixable, fix given), OPEN.  Focus (as assigned): the design and the case analysis; the line-by-line
reduction "X2-ref CM' uses Proposition KN only through (i)-(iii)" is referee (a)'s and is only spot-checked here.

## 1. The recursion T_fin

### 1.1 Well-foundedness and positivity (Lemma W_fin).  PROVED (agree), with precision P-LIP.
Order at stage l: target (absorber stages: lb_l, then R(l), then y_l) -> (GM) delta_l -> n_l, u_l -> c^max_l, generic c_l -> level data and QC data with
the actual weights c_1..c_l -> Design(l) -> sub-windows w = (l, i): u(w), Q(w), n(w), T_hi, T_lo, eta', b(w) -> (next stage).
(a) Every entry of c^max_l uses only stage-(l-1) data and stage-l target data: (W7) of U4 1.3(4) is
    3 * 2^{-10} tau_{l-1} lambda_{l-1} delta_{l-1} 2^{-(m(l-1)+k(l-1)+min S_{l-1})} eta_{l-1}/(n_{l-1}(1+||U||)), target-independent.
(b) k(l + R_cl(l)) at a main stage l: the stages l+1..l+R_cl(l) are block-1 cluster stages and R_cl(l) = 2|E^ch(l)| depends on T(l) only, so
    k(l + R_cl(l)) = #{block-1 stages <= l} + R_cl(l) is known at stage l (no forward reference).
(c) (GM): g_l = delta^max_l H_l/(32 * 3^{|supp y|}); each of the 2 * 3^{|supp y|} sign pairs excludes an open delta-interval of length
    2 g_l/H_l = delta^max_l/(16 * 3^{|supp y|}); total <= delta^max_l/8 < delta^max_l/2, so the admissible subset of [delta^max_l/2, delta^max_l]
    is a nonempty finite union of closed intervals and its maximum is delta^max_l or an endpoint (eps' g_l - sum sigma_j y(j))/(eps H_l);
    H_l = 2^{-3 * 2^l}/(1 - 2^{-2^{l+1}}), delta^max_l, g_l are rational, so delta(y, l) is in Q(y(j) : j).  (Numerics: design_checks.py, item 1.)
(d) Sub-window bands are nonempty and disjoint: u(w) = b(w^-), Q(w) >= (4/u(w))^{20}, so T_hi(w) <= 2^{-l^3}/(l Q(w)) <= b(w^-)^{20} 4^{-20}
    and b(w) <= eta(w) = T_lo(w)^4/(l Design(l)) <= T_hi(w)^4 < u(w); (D1), (D2) only lower b(w).
(e) b_X1(w) > 0: the left sides of (D1), (D2) are continuous, increasing, -> 0 as b -> 0; the right sides are positive numbers (QC(a)-(c) need
    Phi notin B_kappa, guaranteed by GEN_fin since c_l was chosen transcendental BEFORE the level-l QC data are computed).
PRECISION P-LIP.  KN^tr Step 1 bounds F(r') <= F(r_1) + Lip(F)|r' - r_1| with F = max_{d in N_T} psi_d/Phi_d; its Lipschitz constant Lip_kappa on
K_kappa contains 1/Phi_d and may exceed V2's Lip(l) (constant of the determinantal polynomials).  Q1 (S6) writes delta_0(b) and (D1) with "Lip".
Fix: use Lip^*(l) := max(Lip(l), max_kappa Lip_kappa) there and in "robust statuses move by <= Lip eta'".  Lip^*(l) is a level-l design number
already dominated by Design(l) (S5); nothing else changes.

### 1.2 Upper bounds on the weights.  PROVED (complete list).
c^max_l is the minimum of: (W1) c_{l-1}/4 (cluster form min(c^cl 4^{1-i}, c_{p+i-1}/4)); (W2) b(l-1, M(l-1))^2 at PRE/MAIN, b(p, M(p))^2 inside c^cl;
(W3) (delta_l H_l)^2 at PRE/MAIN, (delta^max_{p+1} H_{p+1}/2)^2 at p+1; (W4'') (PRE/MAIN with T_lo(l-1, M(l-1))^3; clusters with T_lo(p, M(p))^3
for all s in E^ch(p)); (W5), (W7) (PRE, MAIN, and p+1 with delta^max/2); (W6) (MAIN, l >= 2); (W_exp) exp(-1/T_lo(p, M(p))) in c^cl(p).
 * (W2) at cluster stages p+i, i >= 2, is not imposed and not needed: sub-windows are used only at main stages; the only use is
   c_{L+1} <= b(L, M(L))^2 for main L.
 * (W3) at clusters p+i, i >= 2, is implied: c_{p+i} <= b(p, M(p))^2 <= T_lo(p,M(p))^8 <= 2^{-8 n(p,M(p))}, while (delta_{p+i} H_{p+i})^2 >=
   2^{-2(p+i) - 2 - 6 * 2^{p+i}}, p + i <= p + 2|E^ch(p)| <= 3p + 2 s_max(p) (|T(p)| <= s_max(p)), and n(p, M(p)) >= p 2^{p^3} Design(p) >=
   p 2^{p^3} B_mu(p)^6 >= p 2^{p^3} 2^{12 s_max(p)^2}.
 * X1's (D3) is implied (X1-ref S-0): c_{L+1} <= b(L,M(L))^2 <= b(w)^2 <= mu^2/64 and mu <= Lip_kappa eta' << 1/(C D(L)^2).
 * Implicit bounds: W_pull — a carrier other than l meeting j_p in S_l lies at a stage >= j_p (allowedness (c)), total weight <= (4/3) c_{j_p};
   W_lev — a carrier other than l meeting j > s_max(L) in S_l is at a stage > L because s_max(L) = max T(L) (by definition; Q1 2.3 attributes it
   to (c), harmless).
 * Wording: Q1 1.7 says (F10) holds "only partly ((W5), (W6), (W7) not at absorber/cluster stages)", but (S4) imposes (W5), (W7) at PRE stages and
   at p+1.  More constraints only; harmless.
Every upper bound is computed from the actual earlier weights, so c_l <= c^max_l verifies it literally.

### 1.3 Lower-bound uses of the weights.  PROVED, with precision P-R.
 * lb_l <= c_l: every entry of c^low_l is <= the corresponding entry of c^max_l (delta_l >= delta^max_l/2 in (W3), (W5); the other entries
   coincide), and >= 1/4 of it; so c_l/8 <= (1 - 2^{-l}) c^max_l/4 <= lb_l <= c_l.  Cluster: lb_{p+i} = (1 - 2^{-(p+i)}) c^max_{p+i}, exact.
 * Absorber sweep (U1 Lemma 3.3(i)): 2^{3-R} <= mu_{p_0}^2 lb_l^2/4 <= mu_{p_0}^2 c_l^2/4.
 * PRECISION P-R (I3 is incomplete): U1-ref 7 (used by route V's Step B, owners inside absorber blocks) uses the LOWER bound
   eta_k >= mu_{p_0}^2 c_k^2/64 on the absorber's least entry, i.e. an UPPER bound on R.  With R minimal for lb: 2^{4-R} > mu^2 lb^2/4 >=
   mu^2 c^2/256, and the least entry is 4 * 2^{-R}/q^*(x) >= 2^{-R}/2 (q^*(x) <= 8), so eta_k >= mu_{p_0}^2 c_k^2/2^{13} (numerics: min log_2 ratio
   = -12.55).  U1-ref 7's chain n(p'-1) >= Design(p'-1) >= (B_mu D)^6 >= (1/(eta_k lambda_k))^6 survives: B_mu(l) = 2^{2 sigma^2 + sigma + 2} with
   sigma >= p_0 >= 11 gives B_mu >= 2^{p_0}/mu_{p_0}^2 >= 2^{11}/mu_{p_0}^2, D >= 1/Phi_k, sixth power.
 * Cluster capacity: by induction from c^max_{L+i} = min(c^cl 4^{1-i}, c_{L+i-1}/4) and c_l >= (1 - 2^{-l}) c^max_l,
   c_{L+i} >= prod_{j <= i}(1 - 2^{-(L+j)}) c^cl 4^{1-i} >= (1 - sum_{n > L} 2^{-n}) c^cl 4^{1-i} >= c^cl 4^{1-i}/2 (numerics: worst 0.77).
 * Design-computed lower bounds (lambda_l >= Phi_l >= 1/D(l), Phi_min(L) >= 1/D(L)) are computed after the weights: exact.
 * s_1 = T_lo^8 c_l and (VT) c_l >= C' D T_lo: not on Master Theorem VI's tree (route V fixes s_1 by Lemma S2c^tr).

### 1.4 (W_exp) and (D-lev).  PROVED.
(W_exp) sits in c^cl(p) only, with the smallest T_lo of main stage p; for every sub-window w of p, T_lo(w) >= T_lo(p, M(p)), so
c_{p+1} <= exp(-1/T_lo(w)); later weights inherit by (W1).  b(p,M(p))^2 <= T_lo^8 >> exp(-1/T_lo): (W_exp) is the binding entry.  Absorber R of
clusters is computed from lb_{p+i}, which contains it (R larger, harmless).
(D-lev): for j <= sigma_2(l) in S_{l''}: mu_j^2 v_{l''}(j) = mu_j^2 delta_{l''} 2^{-j}/n_{l''} >= mu_{sigma_2}^2 delta_{l''} 2^{-sigma_2}/n_{l''} >= 1/Design(l);
no weight enters.  Lever-coordinate availability: inside (s_max, sigma_2(L)] Step A of CM^tr uses at most the FIRST element of each S_l (a TU
bank); its TU pulls sit at v_l(j_p) ~ the needed correction: O(eta' kappa) (active), O(b theta Phi/m) (KN-1 holds of nearly neutral carriers) or
>= c_{L+1} (Q1's floor), all << v_l(second element) >= delta_l 2^{-sigma_2}/n_l because b <= eta <= T_lo^4 <= 2^{-4 n(w)} and n(w) >= Design(L) >=
2^{6 s_max}.  So X2's lever coordinate j(l) (second element) is a free contact.  The DC pull coordinates (v ~ r) are far beyond as well.

### 1.5 Theorem A_fin (Martin's Lemma B).  PROVED (agree).
(T-a) q^*(T e_{k,m}) = c_{j(k,m)} q^*(u_{j(k,m)}) = c_{j(k,m)} <= c_1 (c_l <= c_{l-1}/4); option (a) c_1 in (1/2,1), option (b) c_1 = 1 at (1, 2).
(T-b), (T-c).  Allowedness (a) for EVERY target: main targets by (r.1); absorbers: PRE s <= p - 2|supp Y_r| - 1 <= l_r < l, cluster s <= p < l
(s in S_{l''} ∩ [1, p], or s in T(p) ∩ S_{l''} with s <= stage of its target <= p by (c), induction), and s in S_{l''} forces l'' < 3 * 2^{l''} <= s;
p_i odd lie in Z_0.  For s in S_{l'}: u_l(s) = 0 for l < l', u_{l'}(s) = delta_{l'} 2^{-s}/n_{l'}, and every later target meeting s obeys (W4).
For x in l_1(N x N) with x_{l'} != 0 and Z := T x: |Z(s)| >= c_{l'} delta_{l'} 2^{-s}(|x_{l'}|/n_{l'} - (8/9)||x||_inf 2^{-s}) > 0 for all large s in
S_{l'} (||y_l||_1 <= 1, n_l in [3/4, 5/4] since delta_l q^*(h_l) <= delta^max_l (1 + ||U||) H_l <= 1/4, sum_{l >= L(s)} c_l <= (4/3) c_{L(s)} <=
(2/3) 2^{-2s} c_{l'} delta_{l'}).  So Z in c_00 forces x = 0: injectivity and Y ∩ c_00 = {0}.
(T-d): y^(i) is allowed at round r once l_r >= max supp y + 2|supp y| ((c+): p - 2|supp y| - 1 = l_r + 2|Sigma(y)| - 2|supp y| >= max supp y; (a): s in
S_{l'} ∩ supp y gives l' < s < p); every m occurs infinitely often in (m_r), i_nu = i infinitely often, l_r -> infinity; q^*(u_l - y^(i)) <=
|1 - 1/n_l| + delta_l q^*(h_l)/n_l -> 0; Y_pool is dense in S_{q^*}.  Round 1: any candidate meeting a signature set violates (c+) (bound <= 0) or
(a), so stage 1 is the main stage of round 1, block m_1 = 2, Phi_1 = c_1/8.
Martin's proof and the note (lem:martintail, prop:reduction, lem:pair) use only ||T|| <= 1, i.e. Phi_m(k) <= 2^{-m-k} (read in the note).

### 1.6 Lemma GEN_fin.  PROVED (agree); the point that makes "weights before f" legitimate.
k_0 := Q(y(j), delta(y, l), n(y, l) : y in P_Y, l, j >= 1) is countable and fixed before any weight (every absorber outcome lies in A_pool).  It contains
every coefficient of every cone row and floor function: u_l(j) for ALL j (so the weight-dependent range E_c(w) up to s_far(w) is harmless),
mu_s, H_l, ||U||, the aggregated signature coefficients (delta_l/n_l) sum_{s' in S_l, s' <= s} 2^{-s'} for every integer s.  By X1 2.2(iv) and
2.3 (re-read), B_kappa is defined from: u_l on E_c; peak vectors and peak WEIGHTS; sigma_rob(m) = sum of Phi_p^2 over the pattern's robust peaks;
signs and combinatorial labels; the weights of (KN)-block carriers; the ratio variables r.  No continuous datum of the row f enters; f only
selects the pattern and the point r(f).  Active weak peaks of f belong to the pattern's Omega (formula-1 kappa, X1-ref K1), not to the peak
traces, so tau_m contains no N_T-weight.  Transcendence induction gives algebraic independence of (c_l)_{l >= 1} (option (a)) or (c_l)_{l >= 2}
(option (b)) over k_0, hence of any finite subfamily over k_0(any disjoint finite subfamily); X1-ref 6 (CAD over k^rc + norm of conjugates)
then excludes coincidences.

### 1.7 N-independence.  PROVED (agree).
No rule refers to N.  For p_N, carriers of blocks > N are absent; their rate objects are the constant 1; the cone of f's class equals that of the
pattern in which every block > N is inactive (inactive blocks contribute no row), which the design enumerates (enumeration over all
combinatorial data); QC data involve only (T)-blocks.  f-constants with 3^N and any N-dependent exponent of the cube count (A_max/eps)^p are
absorbed for large L because Q(w) >= (4 Design/u)^{omega(l)+20} and omega(l) -> infinity (so Q1's "C_U1 absolute" may be read as "eventually
dominated"; harmless).

## 2. Lemma PM (clamp-equation freezing).  PROVED (agree), with a new identity
2.1 Clamp equation.  lem:threshold: |w(k)| = M min(1, nu_k/theta), nu_k = |zeta_k|/Phi_k^2, theta = A M/C, C = M sqrt(S_1), M + C = 1, with
S_1 = sum Phi_k^2 min(1, nu_k/theta)^2.  With v_k := |zeta_k|/(Phi_k A): min(Phi_k M/C, v_k) = (Phi_k M/C) min(1, nu_k/theta), so
sum_k min(Phi_k (1 - C)/C, v_k)^2 = (M/C)^2 S_1 = 1.  Each term is nonincreasing in c, strictly decreasing near C for strict peaks.
2.2 alpha-mass identity (NEW, used twice).  Pairing R**xi/|R**xi| = alpha + D D^* w/C with w gives 1 = M ||alpha||_1 + C, so ||alpha||_1 = 1 (M > 0);
for k in P, |nv_k| = |alpha_k| + Phi_k^2 M/C, i.e. rho_k = 1 + |alpha_k| C/(Phi_k^2 M); hence
     sum_{k in P} (rho_k - 1) Phi_k^2 = C/M.
(Numerics: alpha_mass.py, 300 random blocks, relative error 6.5e-51.)  Consequences: every block has a strict peak (slope of the clamp equation;
Lemma PM's natural peak exists with an f-margin); and V1 Lemma D (robust coarse peak at a clean w): coarse weak peaks contribute <= b ||Phi||_2^2,
fine peaks <= sum_{fine} rho Phi^2 = sum_{fine} |zeta_k|/theta <= (1 + ||U||) sum_{fine} lambda/theta <= C_f c_{L+1}, so robust coarse peaks carry
>= C/M - b - C_f c_{L+1} > 0; thus sigma_rob(m) >= Phi_min(L)^2 > 0.
2.3 Freezing.  At f^# and f' the Omega terms coincide (nv' = nv on Omega = all coarse strict non-peaks), coarse peak terms equal Phi_k (1-c)/c for c near
C (robust margins >> lever moves), fine terms change by <= ((1-c)/c)(|nv_k| + |nv'_k|) with sum <= C_f c_{L+1}; the natural peak gives slope
>= 2 Phi_*^2 (1-c)/c^3; the intermediate value theorem gives |C' - C| <= C_f c_{L+1}.  For strict non-peaks rho_k = v_k C/(Phi_k M), so
rho'_k/rho_k = [C'/(1 - C')]/[C/(1 - C)].  In fact fine carriers with |u_k(xhat)| of order 1 are peaks (rho_k ~ m|u_k(xhat)|/(Phi_k theta)), so C moves
only through status changes of fine carriers: |C' - C| <= C sum_{fine} Phi^2.
2.4 Numerics (clamp_check.py, clamp_check2.py; independent 80-digit block solver: bisection on theta = S_2/(sqrt(S_1)(1 + sqrt(S_1))), cvxpy cross-check
of the block norm to 7e-10 and 2e-10): 10 instances, near-threshold d with rho_d = 1 - mu, mu in {1e-8, 1e-12, 1e-16}, peaks perturbed by r in
{1e-2, 1e-3}, fine carriers re-drawn arbitrarily, Omega values frozen by the fixed point in A'.  All tuned: |C' - C| <= 6e-73 (working precision),
rho'_d = rho_d to all printed digits.  CONTROL (one ROBUST strict non-peak left untuned): |C' - C| = 3.6e-8 ... 3.4e-7 and |rho'_d - rho_d| =
5e-7 ... 5e-6 >> mu.  (Leaving the nearly neutral carrier untuned moves C only by 1e-67: its clamp term is ~ 0.)

## 3. Lemma S2c^tr.  PROVED (agree).
eta'/3 = T^4/(3 L Design) >= T^5 (1/T >= 2^{n(w)} >= 3 n^2 >= 3 L Design); mu_kappa(eta'/3) >= c_kappa (eta'/3)^{beta_kappa} >= T^{5 Design}/Design
(beta <= Design, c_kappa >= 1/Design, eta'/3 <= 1/Design <= h_kappa); Design <= n(w) <= log_2(1/T): g_min >= T^{5 Design + 2} >= 2^{-6 log_2^2(1/T)},
ln(1/g_min) <= (6/ln 2) ln^2(1/T) <= 9 ln^2(1/T).  (W_exp): eps^viol <= C_f log_2(1/T) e^{-1/T} + C_f e^{-2/T}/T <= e^{-1/(2T)}/2;
s_1 := max(64 rho eps/delta, e^{-1/(2T)}) <= 2 e^{-1/(2T)} <= s_late (>= exp(-C_2 ln^2(1/T))) for T small; K_w^2 s_1 << T^2; K_w c_fine << T^2.
Robustness remark: an exponent of K_w depending on Design or on |Omega| <= L would give exp(C ln^3(1/T)), still dominated by (W_exp).

## 4. The case analysis — escape search.  RESULT: no F-finite row escapes under option (a).
E1 Every block: R_m**xi != 0 (u_{k,m} dense in S_{q^*}, xi != 0), so w_m is unique, M_m, C_m > 0, ||alpha||_1 = 1: all f-constants finite; l_f exists.
E2 A clean sub-window exists at every main stage (1.1(d), omega(L) objects, omega(L)+1 disjoint bands); the objects are numbers for EVERY pattern
   (each with its own formula-1 ratio vector), so there is no circularity with the statuses that define f's actual pattern at w.
E3 Block kinds are exhaustive: at a clean w an inactive coarse rho lies in [0, b] ∪ [u, 1 + b] ∪ [1 + u, inf) (nearly neutral / (KN) / robust peak);
   inactive blocks are (U)-blocks (their near-threshold carriers get the D2 push).
E4 sigma_rob(m) > 0 (2.2).  E5 r(f) is interior to K_kappa: from a^2 = sigma + k^2 R^2, k = a + sigma, 1 - R^2 = sigma(1 + 2a + sigma)/(a + sigma)^2 >= sigma
   because a + sigma <= ||Phi_m||_2 + ||Phi_m||_2^2 < 0.38 (a = C/M <= ||Phi_m||_2 since C = ||D w||_2 <= M ||Phi_m||_2); sigma >= sigma_rob at f; so
   R_a^2 <= 1 - sigma_rob, margin 3 sigma_rob/4 (numerics: min over 300 blocks of (1 - R^2) - sigma = 0.445).
E6 Y_1 empty cannot occur at f's own pattern (F(r') <= 1 + delta_0 <= 1 + m_0/2); |r_d| ~ Phi_d/(m K) >= 1/Design^2 >> eta': signs kept.
E7 Cross effects: rho_d = m|r_d| K(sigma, R^2)/Phi_d depends only on r_d (exact by TU), sigma (peak SET plus fine terms) and R^2 (active exact, inactive
   held), never on second-order VALUE perturbations of peaks; so the non-explicit Puiseux margin never competes with a second-order term.
   PRECISION P-HOLD: the hold must cover EVERY coarse strict non-peak of a (T)-block other than the active ones (by (T) these are exactly its
   nearly neutral coarse carriers).  Q1's "inactive Omega values of (T)-blocks" is correct with route V's convention Omega = all coarse strict
   non-peaks (Q1 2.2(c)); state it in 2.2 Step A.
E8 Under option (b), N >= 2: rows with rho_1(f) = 1, stage 1 an active near-threshold carrier of a (T)-block at clean sub-windows of infinitely many
   levels, and 2^{-3} a critical value of psi_1 on a stratum of Z_kappa — genuinely OPEN.  For a 0-dimensional stratum {r*}, psi_1(r*) is an algebraic
   function of the generic peak weights (through tau_m and sigma_rob); it equals 2^{-3} only if that function is constant, which no argument
   excludes.  Rescaling T_fin(a)/c_1 does not transfer option (a) to (b): the norm is not homogeneous in the weights.
E9 NA rows, rows whose dominant class is trivial: covered.
Conclusion: the residual risk lies in the single-pass-refereed tools (U1-ref's assembly, X1-ref's KN^tr, X2-ref's CM'/C_mix', and this round's
combination step, referee (a)), not in the design or the case analysis.

## 5. Theorem VI.2 / Corollary VI.3.  PROVED (agree).
(ii) => (i): MT VI at f' plus ||(f', g') - (f, rho g)|| <= p^*(f' - f) + p^*(g' - rho g) < 2 eps and prop:reduction(b).  (i) => (ii): lem:pair (read: density
gives NA f_n -> f with rho g in Li C(f_n)); NA rows have base part in c_00.  VI.3: lem:martintail (read: uses only |R_m x|_m <= m 2^{-m} q(x)).
