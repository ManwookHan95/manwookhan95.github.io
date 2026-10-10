# Q1 referee (a) notes (Round 10): verification of the combined theorem (T_fin, route V with KN^tr, Master Theorem VI, Theorem VI.2)

Refereed: r10/Q1_notes.md (= Q1_notes_a + b + c; Q1_part0..3 are earlier drafts of the same text) and r10/Q1_work/ (pm_check2/3, s2c_check;
outputs re-read).  Checked against: r9 X1_referee + X1_ref_notes, X2_referee + X2_ref_notes, X1_notes 2.1-2.6, X2_notes 1.4, 2.1-2.3, 3.1-3.6,
4.1-4.2; r8 U1_ref_notes 3-8, U1_notes 2.1-2.6, 3.1-3.5, 4.1; r7 V1_notes 4.1 (Proposition TR); paper/martin_density_note.tex (def:admissible,
lem:martintail, prop:smooth, prop:approximants, prop:reduction, lem:pair).  Part files: r10/Q1_refa_part1..4.md.  Script: r10/Q1_refa_work/pm_ref.py
(+ .out).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Setting: finite block set I = {1..N}, F = supp a finite.

## 0. Bottom line
The combination is sound.  Every PROVED claim of Q1 is correct or correct after precisions; none of the gaps found is substantive, and I
fix all of them below (P1-P8).  The decisive point — that the non-explicit Puiseux margin of Proposition KN^tr survives the
violation-tolerant route — is right, and for a cleaner reason than the ratio picture: at a d-consistent approximant the relative position of
every coarse strict non-peak k is rho_k = |nv_k| C_m/(Phi_k^2 (1 - C_m)), the normalized values nv_k are frozen EXACTLY, and C_m is the root of
the clamp equation, which moves only through the fine carriers: |C' - C| <= C_f c_{L+1}, independently of the size of the engineering
perturbation.  With c_{L+1} <= b(w)^2 <= mu^2/64 and (W_exp), the margin is safe; the Puiseux exponent only inflates window constants to
exp(O(log^2(1/T))), dominated by exp(-1/T).  The one point where T_fin's definition must be amended is window bookkeeping (P8): the
exponents of the data constant K and of the class/cube count D_cls grow with L + N (class thresholds K_*^{J}) and with the number of extreme
rays p; Q1's "absolute C_U1" is wrong as stated, but Q(w)'s factor (4 Design/u)^{omega(l)+20} absorbs it once this is said (or once l^2 is added
to the exponent) and the cube pigeonhole is refined to supports of size <= N.
MASTER THEOREM VI (option (a), every N; option (b), N = 1 and rho_1(f) != 1) and Theorem VI.2 (density for p_N <=> (LSC-trunc)_N) are PROVED
modulo the cited refereed results (several of which have had one referee pass: U1-ref's assembly, X1-ref's and X2-ref's fixes).
No counterexample is claimed or suggested; nothing found points to one.  (LSC-trunc), hence density for p_N and for p, remains OPEN.

## 1. Verdicts
| Q1 claim | verdict | main point |
|---|---|---|
| T_fin, Lemma W_fin | correct, fixable gaps | P7 (patterns over the blocks of stages <= l; l_f after all blocks <= N have coarse carriers), P8 (Q(w) exponent) |
| Theorem A_fin | correct | (T-b)/(T-c) estimate and (T-d) re-derived; equality clause of (T-a) unused in arguments (grep) |
| Lemma GEN_fin | correct | only N_T weights need genericity; k_0 contains every cone coefficient |
| Survival audit I1-I10 | correct | route V uses no weight lower bound except design-computed ones; absorber items concern route X only |
| Route decision | correct | KN^tr is sign-agnostic per block, so it serves mixed classes; route X is off the tree of MT VI |
| Lemma CM^tr | correct, fixable gaps | P2 (order: class, Step A, cube, Step B), P1 (kind [1'] for D2-pushed carriers) |
| Proposition BR | correct, fixable gaps | P3 ((U3) holds up to V_fine, a tolerated violation), P4 (Step A uses a bounded number of S_l coordinates, not "two"), H |
| Lemma PM | correct | clamp-equation argument re-derived; identity rho'/rho = [C'/(1-C')]/[C/(1-C)]; independent numerics; P5 phrasing of (iv) |
| Lemma S2c^tr | correct | g_min >= T^{5 Design+2}; r_0 linear in g_min; K_w <= exp(C log^2(1/T)) |
| Theorem C^tr | correct, fixable gaps | P6 (E^eng with window-dependent gamma_B via c_flat(j)), P8 (window count) |
| Master Theorem VI | correct, fixable gaps | inherits P2, P8; quantifier order verified |
| Theorem VI.2, Cor. VI.3 | correct | (i) => (ii) for every T; (ii) => (i) by MT VI; lem:martintail needs only q^*(Te) <= 1 |

## 2. Proofs and re-derivations
2.1 (Statuses at a d-consistent approximant; Lemma PM.)  By lem:threshold, |w_m(k)| = min(M, C |zeta(k)|/(Phi_k^2 A)) and ||D w_m||_2 = C, so
    1 = sum_k min(Phi_k (1 - C)/C, v_k)^2,  v_k := |nv_k|/Phi_k,  nv_k := zeta_m(k)/A_m.           (clamp equation)
The left side is nonincreasing in C, strictly decreasing near C through any peak.  At f^# and at the d-consistent approximant f': Omega terms
are equal (nv'_k = nv^#_k, both strict non-peaks); coarse-peak terms equal Phi_k^2((1-c)/c)^2 for c near C (margins >= u/2 exceed their value
moves, which are second order — coarse peaks meet no lever coordinate by allowedness (c)); fine terms differ by <= 2((1-c)/c)|nv'_k - nv^#_k| each
(|min(a,x)^2 - min(a,y)^2| <= 2a|x - y|), in total <= 4((1-c)/c)(1 + ||U||) sum_{l > L} lambda_l/A_min <= C_f c_{L+1}.  The natural peak of
Lemma M2 gives slope >= 2 Phi_*^2 (1 - c)/c^3; the intermediate value theorem gives |C' - C^#| <= C_f c_{L+1}.  For k in Omega,
rho_k = nu_k/theta = |nv_k| C/(Phi_k^2 M), so rho'_k/rho^#_k = [C'/(1 - C')]/[C^#/(1 - C^#)].  With c_{L+1} <= b(w)^2, b(w) <= mu_min/8,
rho'_d <= 1 - mu/4 + C_f c_{L+1} <= 1 - mu/8 for the (T)-block carriers d.  (Numerics, 2.6.)
SHARPER (remark): each fine term also changes by at most a^2 = Phi_k^2 ((1-c)/c)^2 (both mins lie in [0, a]), so
|C' - C^#| <= C_f sum_{fine} Phi_k^2 <= C_f c_{L+1}^2; in particular fine carriers whose values are of size lambda_k (nu_k ~ m/Phi_k, far above
the threshold) are clamped at both rows and do not move C at all — this is what the numerics show (|C' - C| at working precision).
2.2 (Kinds of inactive Omega carriers; P1.)  In an active NEGATIVE block no inactive near-threshold carrier exists (U1-ref 4.1 exclusions:
lem:suplevel(f) / eq:peakshift give |Delta| M rho <= 3 b M/t + A_i K t/lambda against |Delta| M >= K_* A_i K t); so a (KN)-lever d_0 there is
robust (kind [2]); in positive blocks vs Domega(d_0) = Delta |w^#(d_0)| > 0 (kind [3]).  KN-1-held carriers: w^# = 0, gamma = 0, gap = M
(kind [2]).  D2-pushed carriers of (U)-blocks: Delta = 0, Domega = 0, omega^+ = V1's clamp, |omega| <= 2 gap/t: kind [1'] (gap > 0 only),
accepted by Theorem UE (its Step 3 uses |omega| <= 2 gap^0/t only).  (U2) of Theorem UE should be read with [1'].
2.3 ((U3) with fine residue; P3.)  At a support coordinate j of f_0 with z_j = sgn a_j, the base excess of a'_j + x_j is
|a'_j + x_j| - |a'_j| - z_j x_j <= 2 (z_j x_j)_-, the same expression as at a contact.  In route V the data at a Step-A bank/pull are a
contact-like (or mass-dominated) part plus +-V_fine(j)/2; the second part costs <= 2 rho |tau| |V_fine(j)| and is counted in the violation
mass eps of (U4) (sum_j |V_fine(j)| <= C_f Design c_{L+1}); the theta piece is untouched because b^theta = (chi - 1/2) V_proj.  At KN-1 hold
pulls: fine coefficients are -Delta'' lambda_k w(k) = O(lambda_k) (not O(lambda/t)), so t|V_fine(j_p)| <= t C_f c_{L+1} <= 24 lambda_l
v_l(j_p) = |a^#(j_p)| for v_l(j_p) >= c_{L+1}, t <= T_hi(w).
2.4 (Order of the companion; P2.)  Step B is built for the ray Delta'^* (owner coefficients -Delta''_m lambda_k w(k)), and Delta'^* is the corner
of the normalization cube, computed at the cone of the row after Step A.  Order: class (from the data at f) -> Step A -> cube -> Step B -> data.
2.5 (Lever coordinates; P4.)  Step A uses on each S_l a bounded number of coordinates (Step 0 push, realization pull/bank, KN-1 pull/bank,
(KN)/(D2) pushes), its banks at most the first element beyond s_max.  Lemma DC's pulls need v in [r, 2^{G} r] with r >= s_1 >= exp(-1/(2T))
>> c_{L+1}, i.e. inside S_l ∩ (s_max, s_far] ⊂ E_c; choose them among unused elements in a v-window of ratio 2^{6 G(L)} (bounded gaps), a
factor entering C_2 only.  (D-lev) with the second element of S_l beyond s_max suffices for the bank coordinate j(l) as long as Step A
banks each carrier at most at the first element (X2 LV, V1 (C3)/(C4)); if a variant of Step A needs two bank coordinates on one S_l, define
sigma_2 in (D-lev) with the third element instead (a design number; nothing else changes).
2.6 (Numerics, sanity only; Q1_refa_work/pm_ref.py, a DIFFERENT block solver: inner problem in closed form for fixed M = ||w||_inf, outer
concave maximization by bisection on the envelope derivative A'(M) = sum_clamped(|zeta_k| - Phi_k^2 M/t) - (1 - M)/t; 64-90 digits.)
10 instances (pm_ref.out; pm_ref_flip_part1.out + pm_ref_flip2.out; summary pm_ref_summary.txt), mu in {1e-6, 1e-9, 1e-12}, fine weight
W in {1e-14, 1e-20, 1e-26}, coarse perturbations r in {1e-3, 1e-2} >> mu, fine values arbitrary or moved across their own thresholds:
identity t = C/A (lem:threshold) <= 1.9e-61; after d-consistency on all of Omega, 1 - rho_d = mu exactly, rho'/rho identity <= 1.1e-54,
|C' - C| <= 4e-31 and below W^2 in every instance (the sharper bound above); CONTROL (one Omega carrier untuned): |C' - C| = 1e-7 ... 6e-5,
d becomes a peak in 6 of 10 instances.  Sanity only: finite blocks cannot exhibit infinite-dimensional failures.
2.7 (Window bookkeeping; P8, PROVED fix.)  The constant of (E-c) is K_data <= J K_*^{J+1} K (class thresholds A_{i+1} = K_* A_i, U1 2.3;
J = |Omega| + N <= L + N), and the cube count is (A_max/eps)^p (p = number of extreme rays).  Refined pigeonhole: basic representations use
<= N rays (Caratheodory); pigeonhole over the support (<= (p + 1)^N) and then over eps-cubes in [0, A_max]^J (<= (A_max/eps + 1)^N); with one
support J and corner a^max, Delta'^* := sum_J a^max_j g_j and incr(t) := sum_J (a^max_j - a_j(t)) r_j lies in the cone, ||incr(t)||_1 <= N eps.
So D_cls <= C_{f,N} 3^{2L} (p_max + 1)^N (Design/u)^{2CN}.  Put p_max(L) into Design(L) and Q(w) := (4 Design/u)^{omega(l) + l^2 + 20} (or note
omega(l) >= number of patterns >= 2^l).  For L >= l_f(f, N): D_cls^2 K_data/c_flat <= C_{f,N} (4 Design/u)^{C(L+N)} <= (4 Design/u)^{L^2 + 20}/C_{f,N},
so |S| c_flat/K_data >= L 2^{L^3}/C -> infinity and K_data T_hi/|S| -> 0.  Q only grows: Lemma GW keeps every window condition.
2.8 (Theorem E^eng with window-dependent gamma_B; P6.)  In Theorem UE only (c4) involves gamma_B; c_flat(w) = min(c^f_flat, gamma_B(w)/(8 rho A_2))
>= c_f u(w); t_1, K_sharp, c_late are f-constants ((c5) only weakens as c_flat decreases).  E^eng's proof uses c_flat(j) exactly where (E-d)
tracks it.  So "FIXED gamma_B" in its statement must read "gamma_B(j) with c_flat(j) in (E-d)", as in V1's E''.
2.9 (Quantifier order, verified.)  T_fin -> N -> f -> (g, rho) -> l_f(f, N, g, rho) -> main stage L >= l_f -> clean w(L) (rate objects of f)
-> class (data at f) -> Step A -> (support, cube) -> Step B -> data -> N_w -> s_1 := max(64 rho eps/delta, exp(-1/(2T))) -> N'' -> levers (Lemma DC)
-> f'_L and the averaged second row; L -> infinity.

## 3. What remains open (precise)
(1) (LSC-trunc)_N (infinite base support), equivalent (Theorem VI.2) to density of NA((c_0, p_N), l_2^2) for the Martin-type norm built with
    T_fin; for Martin's p (I = N) density follows from (LSC-trunc)_N for infinitely many N.  OPEN.
(2) Option (b) (norm-one T, inside def:admissible) for N >= 2 at rows with rho_1(f) = 1 (carrier 1 in N_T with the rational weight 1/8:
    a slice-coincidence question).  OPEN.
(3) Arbitrary admissible T (Martin's own Lemma B operators): MT VI is proved only for the designed T_fin.  OPEN.
(4) Robustness of the chain: the combination now has one referee pass (this report and referee (b)); U1-ref's MT IV' assembly, X1-ref's
    KN-1/S-0/W-fixes and X2-ref's (R-abs) (Lemma CM', Theorem C_mix') have had one pass each.
