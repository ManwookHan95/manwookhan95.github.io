# P3 notes (Round 15): the two falsification tests of the negative-track referees
#   (a) N2-ref: transition-cell excess for cancellation staircases / (LIN) / E's rigid design against crossing conversions
#   (b) N1-ref / R3-ref: the capacity route (R6)

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN; NUMERICAL marks model computations (sanity checks only: finite models cannot
exhibit non-density).  "PROVED (model)" means a complete proof inside Model N_RN (the separable real-norm junction model of Section 1),
not a theorem about Martin's norm.  Setting: Martin-type norm p_N with one active block (N = 1 suffices), canonical base, admissible
T = Lemma B's conclusion only, rows with finite base support, notation of Parts I-III, r1/E, r3/R3, neg/N1-N3.
This file supersedes the unfinished earlier P3 parts (P3_part0_*.md - P3_part3.md, written by a previous instance) and the drafts of
this rerun; every claim there was re-checked, corrections in Section 6.  Rerun part files: P3_part4_rerun_constants.md,
P3_part5_rerun_capacity.md, P3_part6_rerun_cell.md, P3_part7_rerun_cellnum.md, P3_part8_exact_criticality.md; scripts in
ctx/r15/P3_work/ (v2_* files, Section 8).

## 0. Answers

MAIN NEW RESULT (Section 2.5, PROVED in Model N_RN).  For an arbitrary discrete staircase (any carrier lattice, margins, multiplicities,
sparse or dense, phase-shifted types) let C(V) be the conversion capacity of a value shift V and E(V) its second-order companion
(explicit lattice sums, 2.5.0), psi = E/V^2.  Then:
 * Proposition W: f's one-sided profile is EXACTLY Q(C(W)) = (kappa - psi)/kappa^2 (kappa = C/W) along the window shift W, so
   sup_tau P_f = 1/(4 min psi);
 * Theorem EC1 / Corollary EC2: the one-type conversion with shift V = W_c := argmin psi has sup_tau P_f' = sup_tau P_f EXACTLY at
   every scale (R = 1), with three exact identities (I+), (I-), (I-b); every other placement has R > 1, with an excess of first order
   in ln V - ln W_c.  With the deep region restored over L octaves below the band: R = 1 + O(2^-L) (SKETCH + NUMERICAL).
 * Consequently all one-type "discreteness excesses" found earlier (1.0018, 1.0021, 1.0003-1.011, "about 0.2 per cent") were
   misplacements of V on a grid (correction C10); numerically R(W_c) = 1 to 1e-8 in eight layouts and to 1e-12 at the exact rational
   minimisers 7/6, 28/5, 7/5, 47/30 (e.g. one carrier per octave, margin 1: W_c = 7/6, sup P_f = 7/11).

TEST (b) — capacity route (R6): DEFEATED at model level.  An admissible T cannot force a Hilbert/room load above the conversion
capacity.
 * Real-norm coupling (PROVED from refereed results, Lemma B0): the first-order peak cost is 2MB x margin x depth/|t| per unit carried,
   in the SAME block excess as the Hilbert cost B x^2; models with an independent peak-cost constant (E's Model N, R3-ref scripts) are
   not real-norm models.
 * One converted band suffices EXACTLY (Corollary EC2): the load at every scale is matched by one band at the critical placement.
   Two converted bands give a factor-2 margin at the bottom (Theorem W*') and a strict first-order saving above the band even with
   destruction right below the band (Proposition FO); two-type R < 1 in every tested configuration.
 * The R3-ref deficits 1.46 / 2.07 / 1.086 / 1.09 are artefacts (peak costs 8-17 times below the real-norm value; band placement).
TEST (a) — transition cell: DEFEATED at model level, at every order.
 * E's rigid design (A1)-(A5): its own condition (O4) makes every group scalar a two-type lever: strict first-order saving (FO), EC for
   compact core errors: DEFEATED (model level).
 * Cancellation staircases (C-B1 far parts, (LIN), any near-error structure): Lemma G (PROVED) forbids balanced two-type conversion
   inside one group and the sum rule (PROVED) forbids a strict first-order saving, but the pure V-shift at W_c, with the finitely many
   groups between the band and depth V 2^-L restored (C-B1 allows it), moves every alive carrier by the same amount, creates no near
   error, needs no EC and no cross-group partner, and has cell excess exactly 0 (L = infinity) resp. O(2^-L).  So NO configuration has a
   one-sided hand-over excess bounded below uniformly in the depth (in Model N_RN).  The earlier "single-group Gordan obstruction of
   2-9 per cent" and the draft's "second-order residue of 0.2 per cent" do not exist.
 * Conjecture R6** of the draft (Gordan structure + escaping guarded errors + discreteness): its model content is FALSE (5.3).
STATUS OF THE MAIN QUESTION: OPEN.  No counterexample is claimed; nothing here is a step of a negative proof.  Both tests are defeated
at model level with proofs; the only model-level configuration with a first-order obstruction would need (R6-tie): forced destruction
right below the junction band together with the Gordan structure, for which no mechanism is known.  The remaining gap is the
real-norm transfer at exact criticality (5.3 (T)).  Leaning: density (positive answer) along this route.

## 1. Setting, the real-norm per-carrier costs, and the separable junction model

### 1.1 Setting
Martin-type norm p_N with one active block m (N = 1 suffices for both tests; other blocks are untouched spectators), canonical base,
admissible T = the conclusion of Martin's Lemma B only, rows f with finite base support.  At a row f: normer xi, q_0 = q**(xi),
forced decomposition f = a + L*w, zeta = R_m** xi, M = ||w||_inf, C = ||D_m w||_2, M + C = 1, |zeta| = 1 - q_0.  Carriers k of the
block: depth lambda_k := m Phi_m(k) (so R_m* e_k = lambda_k u_k), relative position rho_k := m u_k(xi) C/(Phi_m(k) M |zeta|).
Part I lem:threshold (Fact C): k is a peak iff |rho_k| >= 1; off the peak set w(k) = M rho_k.  A block move t Omega with coordinates
omega_k carries x_k := lambda_k omega_k units of u_k (R_m*(t omega) = t sum_k x_k u_k).  A "type" is the set of peaks of one sign:
P- (rho <= -1) can be used inward only on the side t > 0, P+ only on t < 0.  A value shift s of n_k u_k(x') moves rho_k by
s/(theta lambda_k n_k) (theta = the threshold constant); below theta lambda n_k is normalised to lambda_k ("theta = 1").

### 1.2 The three per-carrier block costs.  PROVED (restatements of refereed results).
Put B := 1/(2 m^2 C).
 (C1) Peak cost.  R3 4.7 (PROVED, refereed; equivalently N2-ref push calculus (iii) seen from the base side): for a peak with
      rho_k = sigma(1 + delta_k), delta_k > 0, alpha(k) = sigma delta_k Phi(k)^2 M/C, and an inward use at scale t has block excess
      N_m(w + t Omega) - 1 - t<Omega, zeta/|zeta|> = |t omega_k| delta_k Phi(k)^2 M/C + O(t^2) = 2 M B delta_k lambda_k |t| |x_k| + O(t^2).
      Per unit t^2: L_k (lambda_k/|t|)|x_k| with L_k := 2 M B delta_k.  Strict non-peaks: alpha(k) = 0, no first-order cost.
 (C2) Hilbert cost.  N2-ref push calculus (ii) (PROVED): N(w + t(omega - d w)) <= 1 + t^2 ||D omega||^2/(2(C + t d M)), with
      ||D omega||^2 = sum_k x_k^2/m^2 (D diagonal, disjoint coordinates: no cross terms): B sum x_k^2 per t^2 up to the factor
      C/(C + t d M) = 1 + O(t) and the projection onto (D w)^perp, which only lowers it (d = <Dw, D omega>/C = O(depth)).
 (C3) Room.  Same proof: |(1 - t d) w(k) + t omega_k| <= (1 - t d) M; a peak can be used inward only, |x_k| <= 2 M lambda_k/|t|;
      a strict non-peak w(k) = M rho_k admits t x_k in [(-M - w(k)) lambda_k, (M - w(k)) lambda_k].

### 1.3 Lemma B0 (weighted excess budget).  PROVED.
Let g be in C(f) (hence g(xi) = 0) and f + t g = A + L*W any decomposition; put E_A := q*(A) - A(xi)/q_0 >= 0 and
E_W := ||W|| - W(L** xi)/(1 - q_0) >= 0.  Then q_0 E_A + (1 - q_0) E_W = q_0 q*(A) + (1 - q_0)||W|| - 1; in particular
max(q*(A), ||W||) <= s(t) = sqrt(1 + t^2) implies q_0 E_A + (1 - q_0) E_W <= t^2/2.
Proof.  1 = (f + t g)(xi) = A(xi) + W(L** xi); A(xi) <= q*(A) q**(xi) and W(L** xi) <= ||W|| ||L** xi|| = ||W||(1 - q_0); substitute.  QED
Consequence.  For W = w + t Omega the block excess E_W is the left side of (C1) plus the Hilbert term (C2): peak cost and Hilbert
cost lie in the SAME excess with the SAME weight, so the ratio L_k/B = 2 M delta_k is an identity of the norm.  Base-side first-order
costs (near errors and core errors absorbed on free coordinates) lie in E_A (weight q_0) with a design-dependent constant A.

### 1.4 Model N_RN (definition; a MODEL whose constants are those of 1.2).
At signed scale t = sigma tau the one-sided profile of a carrier configuration is
   P(tau, sigma) = min { sum_k [ c_k |x_k| + B x_k^2 ] (+ near-error terms) : sum_k x_k = S, x_k in box_k(tau, sigma) },
   c_k = 2 M B (|rho_k| - 1)_+ lambda_k/tau + A lambda_k/tau,
boxes as in (C3).  R := sup_{tau, sigma} P_{f'} / sup P_f.  R <= 1 means no model obstruction; R > 1 in EVERY admissible approximant
would make (f, rho g) non-recoverable at model level for rho^2 > 1/R.  Near errors (cancellation designs, Section 4) add
We|E|/tau (first-order absorption) or EC at Hilbert weight Bec (R3 Theorem EC) for E = sum of the near-error vectors carried.
Accuracy (HEURISTIC, with the following PROVED ingredients).  In the deep-junction limit (all relevant depths and scales -> 0 with
their ratios fixed) the block part of the model is asymptotically exact: (C1) is exact to first order, the Hilbert term has no
cross terms, the projection/d-terms are O(depth), the sup-norm part is exact for inward pushes when another peak keeps the
sup, and the forced data (M, C, theta) of f' differ from those of f by o(1).  What the model does NOT contain: resources other
than the staircase (generic carriers carrying the switching component are excluded by the adversary's rate control, E (A5),
R3-ref 3.2), other blocks, base resources, and approximant freedoms beyond the lever families tested.

### 1.5 Diagnosis of the earlier models (PROVED from the scripts and 1.3).
 * E's Model N (r1/E 4.1) charges a0 lambda |rho| |x|/tau, proportional to |rho| = 1 + delta, with a0 independent of B; the real norm
   charges 2 M B delta lambda |x|/tau, proportional to the MARGIN.  E's "error-dominated" a0 = 0.03 (M = B = 1/2, delta = 1) is about 8
   times below the real-norm value 2 M B delta = 0.5; E's one-shift R = 2.82 and R(J) > 1 for bounded J rest on this.
 * R3-ref refwork/onetype_A.py: a0 = 0.03, B = 1: peak cost 0.06 against 2 M B delta = 1 (17 times too small); this produced the
   "bottom" deficits R = 1.463 (A = 0.5), 2.074 (A = 0.25), 1.086 (A = 1, B = 0.6).
 * R3-ref refwork/coupled_full.py: cpk = 1 with B = 1/2, M = 1/2, i.e. twice the real-norm ratio 2M; its one-shift R = 1.090 is in
   addition a band-placement artefact (Section 3.1); its two-shift R = 1.0000 is confirmed.
 * In the real norm an error-dominated regime arises only through a large core-error constant A (base side), never through a small
   peak cost; A > 0 raises P_f while EC removes it at f' (R3 Thm EC) for tau <= tau_gen, so A > 0 favours the approximant.

## 2. Capacity identities and the first-order theory of a junction (Model N_RN, A = 0)

Convex-analysis fact used throughout (envelope theorem; PROVED, standard).  For P = min { sum_k (c_k |x_k| + B x_k^2) : sum x_k = S,
x_k in [l_k, h_k] } the optimum x is unique (strict convexity) and, when some x_k is interior, so is the multiplier mu; x_k is the
projection onto [l_k, h_k] of the one-dimensional minimiser of c_k|x| + B x^2 - mu x.  Under a perturbation of the data, to first
order: lowering c_k changes P by -|x_k| dc_k; raising the bound h_k of a room-limited carrier lowers P by eta_k dh_k with
eta_k = mu - c_k - 2B x_k >= 0; giving room dh to a previously unusable carrier of cost c lowers P by (mu - c) dh when c < mu.

### 2.1 Lemma W' (window = band, arbitrary margins).  PROVED.
One type P- (rho_k = -(1 + delta_k), any delta_k > 0), A = 0, side +, y_k := lambda_k/tau, optimal x with multiplier mu > 0:
x_k = min(2 M y_k, (mu - 2MB delta_k y_k)_+/(2B)).  Window W(tau, mu) := {k : 0 < x_k < 2 M y_k}; conversion band of a value shift s:
Band(s) := {k : s/(2 + delta_k) < lambda_k < s/delta_k}.  Then W(tau, mu) = Band(mu tau/(2MB)) as sets.
Proof.  x_k > 0 iff lambda_k < mu tau/(2MB delta_k); x_k < 2 M y_k iff mu < 2MB(2 + delta_k) y_k iff lambda_k > mu tau/(2MB(2 + delta_k)).  QED
(Every margin class is matched by the SAME shift; with A > 0 every window is strictly narrower than a band.)

### 2.2 Theorem W*' (continuum Hilbert-capacity identity).  PROVED.
For a continuum configuration of one type with margin classes delta in a finite set, class delta having density D_delta per unit
of ln(lambda) at all depths, and N := sum_delta D_delta ln((2 + delta)/delta) (= the continuum size of Band(s), for every s):
   P_f(tau, +) = B S^2/N for every tau,   and the bottom value of a one-type conversion is lim_{tau -> 0} P_f'(tau, +) = B S^2/N.
With both types converted (counts N_-, N_+) the bottom value is B S^2/(N_- + N_+) <= (1/2) max_sides P_f.
Proof.  Put u := mu/(2B), a := 2 + delta.  The optimal allocation is the tent x(y) = 2My (y <= u/(Ma)), u - M delta y
(u/(Ma) <= y <= u/(M delta)), 0 beyond.  Per class: carried amount D_delta u [2/a + ln(a/delta) - 1 + delta/a] = D_delta u ln(a/delta);
cost: room-limited part 4BM^2(1 + delta) y^2 integrates to 2B(1 + delta)u^2/a^2, window part B(u^2 - M^2 delta^2 y^2) integrates to
B u^2 [ln(a/delta) - (a^2 - delta^2)/(2a^2)] = B u^2 [ln(a/delta) - 2(1 + delta)/a^2]; total D_delta B u^2 ln(a/delta).  The multiplier is
common: S = uN, P_f = B u^2 N = B S^2/N; the tent satisfies KKT, hence is optimal.  At f', as tau -> 0, Band(s) consists of strict
non-peaks with no first-order cost and room -> infinity, coarser carriers cost >= 2MB delta lambda/tau -> infinity per unit, finer
(shifted) ones cost about 2MBs/tau -> infinity: the bottom value is B S^2/N.  QED
Reading: f's one-sided Hilbert/room load at every scale is EXACTLY the bottom capacity of one converted band of its type.
NUMERICAL check (mpmath, 40 digits; v2_check_Wstar_mix.py): mixtures {(0.5, 32/oct), (2, 48/oct)}: P_f = 0.008176501-0.008176502 vs
B S^2/N = 0.00817650129; three classes: 0.0116662 vs 0.0116662; window = band as index sets at every phase.

### 2.3 Proposition FO (first-order profile change above the band).  PROVED (model level, continuum, constant margin).
Both types, density D each, margin delta, P_f = B u^2 N, u = S/N; f' obtained by a value shift V > 0 of the converted type(s);
"kd = 0": shifted carriers below the band stay alive (deep peaks); "kd = 1": all carriers below the band are dead; tau >> V;
c_1 := 2 M B u D V/tau.  Modes TWO (P- up by V, P+ down by V) and ONE (all carriers up by V).  Then
   TWO, kd = 0:  P_f'(tau, +-) = P_f - c_1 ln(a/delta) + O((V/tau)^2);   TWO, kd = 1:  P_f' = P_f - c_1 (ln(a/delta) - 2/a) + O((V/tau)^2);
   ONE, side + (converted type):  P_f' = P_f + O((V/tau)^2)  (kd = 0 and kd = 1);
   ONE, side -:  P_f' = P_f + O((V/tau)^2)  (kd = 0);   P_f' = P_f + c_1 (4/a) + O((V/tau)^2)  (kd = 1).
Proof.  Envelope theorem; for tau >> V the band and everything below it lie in the room-limited part of the tent, where
eta = mu (1 - O(V/tau)).  Contributions: (i) above the band every P- margin drops by V/lambda, i.e. its cost by 2MBV/tau per unit,
on the amount S - O(V/tau): -c_1 ln(a/delta) (ONE, side -: P+ margins rise: +c_1 ln(a/delta)).  (ii) Band (V/a, V/delta): TWO: the two
converted carriers of a depth have side-+ rooms M(1 - rho')lambda/tau and M(1 + rho')lambda/tau, total 2M lambda/tau = f's room
(room conservation), zero cost: 0.  ONE, side +: room M((2 + delta)lambda - V)/tau instead of 2M lambda/tau, total loss
(MDV/tau)(ln(a/delta) - 2/a): +c_1 (ln(a/delta) - 2/a); ONE, side -: the same amount of new free room: -c_1 (ln(a/delta) - 2/a).
(iii) Below the band f used 2MDV/(a tau) on each side at full room.  Side +: the P- carriers become P+ peaks: +c_1 (2/a); TWO kd = 0:
the P+ carriers become P- deep peaks (cost about 2MBV/tau << mu) and restore it: -c_1 (2/a).  ONE side -, kd = 0: the P- carriers
become P+ deep peaks usable on side -: -c_1 (2/a).  (iv) ONE side -, kd = 1: f's P+ carriers below the band are dead: +c_1 (2/a).
Sum each case.  ln(a/delta) > 2/a because -ln(1 - x) > x for x = 2/a in (0, 1).  QED
NUMERICAL check (v2_check_FO.py, k = 16/octave, delta = 1, coefficient of c_1 at tau/V = 8, 16, 32, 64): TWO kd 0: -0.18, -0.35, -0.67,
-0.89 (-> -1.099); TWO kd 1: -0.17, -0.29, -0.36, -0.40 (-> -0.432); ONE kd 0 (both sides), ONE kd 1 side +: |.| <= 0.0002; ONE kd 1
side -: 0.51, 0.92, 1.12, 1.22 (-> 4/3).  (A first version of the ONE kd 1 side - coefficient, 2/a, omitted term (iv); the numerics
exposed it.)

### 2.4 Proposition SR (sum rule).  PROVED (model level, first order, tau >> all shifts and dead depths).
Let f' be given by value shifts s_k and a dead set D; x^+ (P-, side +), x^- (P+, side -) f's optimal allocations, mu^+- the
multipliers.  If the GORDAN STRUCTURE holds, sum_{P-} x^+_k s_k = V S and sum_{P+} x^-_k s_k = V S with one number V, then
   [P_f'(tau,+) - P_f(tau,+)] + [P_f'(tau,-) - P_f(tau,-)] = mu^+ sum_{D cap P-} x^+_k + mu^- sum_{D cap P+} x^-_k + (second order) >= 0.
Proof.  Cost terms: -(2MB/tau) sum_{P-} x^+ s + (2MB/tau) sum_{P+} x^- s = 0.  Room terms: an alive carrier keeps total room
2M lambda/tau over the two sides (a peak: all of it on its inward side; a strict non-peak: M(1 -+ rho')lambda/tau), and for deep carriers
the box multiplier on one side equals the value of the room on the other side up to O(max|s|/tau); dead carriers lose their full
room on f's side: + mu x.  QED
Where it holds: (a) every lever combination in a cancellation design (f's side combinations are balanced; Lemma G, 4.2, makes the
pair-average shift equal to V for both types); (b) ONE mode in any design.  It FAILS for E's rigid design, whose group scalars move
P- and P+ in opposite directions (sum_{P-} x s = V_- S, sum_{P+} x s = -V_+ S): the cost terms give -(2MB/tau)(V_- + V_+)S < 0, the
strict saving of Proposition FO.  Consequence: in designs with the Gordan structure no approximant has a strict first-order saving
above the junction.  The hand-over excess is then decided beyond first order, and Theorem EC1 / Corollary EC2 (2.5) show that it is
EXACTLY ZERO for the one-type strategy at the critical placement V = W_c (with the groups below the band restored).


### 2.5 Exact discrete theory of one-type conversion (new in this rerun; part file P3_part8_exact_criticality.md)

This subsection replaces every statement of the earlier parts and of the draft versions of Sections 3-5 that one-type conversion has a positive
"discreteness" excess (R = 1.0018 / 1.0021 / "about 0.2 per cent", Conjecture R6** clause (D)).  Those numbers came from placing the
shift V on a grid (0.1 octave, later 12-24 per octave) and are the first-order cost of missing the critical placement W_c below.

#### 2.5.0 Setting (Model N_RN, separable part, no near errors)
Normalisation B = 1, M = 1/2, so the real-norm peak coefficient is cpk = 2MB = 1 (general B, M: replace lam by 2M lam and V by 2M V,
and multiply all values by B; nothing below changes).  Carriers of type P- are (lam_k, delta_k) with rho_k = -(1 + delta_k), lam_k > 0, delta_k > 0;
carriers of type P+ are (lam'_j, delta'_j) with rho = 1 + delta'_j.  Each lattice has finitely many carriers in every bounded range of depths,
sum_k lam_k < infinity over the carriers below any depth, and sum_k lam_k = infinity (unbounded above; self-similar staircases).  At scale tau write u_k = lam_k/tau.  Profile on side + (load S > 0):
   P(tau, +; S) = min sum_k [ c_k |x_k| + x_k^2 ]  subject to  sum_k x_k = S,  x_k in box_k(+),
where box_k(+) = [0, u_k], c_k = delta_k u_k for a P- carrier (|rho| >= 1 peak, inward only), box(+) = [-u, 0] for a P+ carrier, and for a
strict non-peak (|rho| < 1, w = rho/2) box(+) = [-(1 + rho)u/2, (1 - rho)u/2], c = 0.  Side - is the mirror (box(-) = -box(+)).
Homogeneity (PROVED by the substitution x = a y): P(tau/a, aS) = a^2 P(tau, S); hence P(tau, s; S) = S^2 Q_s(tau S) with Q_s(t) := P(t, s; 1).
f is the configuration with all carriers at their positions; sf_+ := sup_tau Q_+ (side + uses the P- lattice only, since P+ boxes are
[-u, 0] on side + and the multiplier is >= 0), sf_- := sup_tau Q_- (P+ lattice), sup P_f = max(sf_+, sf_-).
ONE mode with shift V > 0 (conversion of P-): every carrier's relative position becomes rho + V/lam (Section 2; all carriers alive).

Lattice functions of the P- lattice (V > 0):  band(V) = {k : V/(2 + delta_k) < lam_k < V/delta_k},  deep(V) = {k : lam_k <= V/(2 + delta_k)},
   C(V) = sum_{deep} lam_k + sum_{band} (V - delta_k lam_k)/2,
   E(V) = sum_{deep} (V - (1 + delta_k) lam_k) lam_k + sum_{band} ((V - delta_k lam_k)/2)^2,
   kappa(V) = C(V)/V,  psi(V) = E(V)/V^2.
(C(V) is the conversion capacity of N1-ref/R3-ref in exact discrete form; E is its second-order companion.)

#### 2.5.1 Lemma L (calculus of the lattice functions).  PROVED.
(i) C and E are continuous; C is nondecreasing and piecewise linear with C'(V) = (number of band carriers)/2 off the band edges;
E is continuously differentiable with E' = C.  (ii) V C(V) - E(V) = integral_0^V w dC(w) >= 0, i.e. kappa >= psi.  (iii) psi is
continuously differentiable with psi'(V) = (kappa(V) - 2 psi(V))/V.  (iv) C(V) -> 0 as V -> 0 and C(V) -> infinity as V -> infinity.
Proof.  At a lower band edge lam = V/(2 + delta): the band term (V - delta lam)/2 = lam equals the deep term of C, and ((V - delta lam)/2)^2 =
lam^2 = (V - (1 + delta) lam) lam equals the deep term of E; at an upper edge lam = V/delta both band terms vanish.  So C, E are continuous.
Termwise d/dV: deep terms of E give lam_k, band terms give (V - delta lam)/2: E' = C, continuous.  C' = (1/2) #band.  (ii) by parts:
integral_0^V w dC = V C(V) - integral_0^V C = V C(V) - E(V) (E(0) = 0).  (iii) psi' = (V E' - 2E)/V^3 = (kappa - 2 psi)/V.  (iv) on band(V) one has
(V - delta lam)/2 < lam, so C(V) <= sum_{lam_k < V/delta_k} lam_k -> 0 as V -> 0; and C(V) >= sum_{lam_k <= V/(2+delta_k)} lam_k -> sum_k lam_k =
infinity as V -> infinity (the lattice is unbounded above, as every self-similar staircase).  QED

#### 2.5.2 Lemma A (f's allocation at a given multiplier).  PROVED.
On side + at scale tau, for a multiplier nu >= 0 the minimiser of c_k x + x^2 - nu x over [0, u_k] (P- carrier) is
x_k(nu) = clip((nu - delta_k u_k)/2, 0, u_k): it equals u_k for deep(nu tau), (nu - delta_k u_k)/2 for band(nu tau), 0 otherwise.  Hence
   sum_k x_k(nu) = C(nu tau)/tau,     sum_k [c_k x_k + x_k^2] = nu sum_k x_k(nu) - E(nu tau)/tau^2.
Proof.  The 1-D minimiser is the clipped stationary point; the three cases are the definitions of deep/band.  Cost: on deep carriers
delta u^2 + u^2 = nu u - (nu - (1+delta)u) u; on band carriers with d = (nu - delta u)/2: delta u d + d^2 = nu d - d^2 (since delta u = nu - 2d).
Summing and rescaling (u = lam/tau, nu tau = W) gives the formulas.  QED

#### 2.5.3 Proposition W (exact window parametrisation of f's profile).  PROVED.
For every W > 0,   Q_+(C(W)) = Phi(W) := (kappa(W) - psi(W))/kappa(W)^2 = 1/(4 psi(W)) - (kappa(W) - 2 psi(W))^2/(4 psi(W) kappa(W)^2),
and every t > 0 equals C(W) for some W.  Consequently
   sf_+ = sup_t Q_+(t) = 1/(4 inf_W psi(W)),
attained exactly at the scales t = C(W) with W a minimiser of psi (there kappa = 2 psi).
Proof.  Fix t = C(W).  By Lemma A with tau = t and nu = W/t the allocation x(nu) is feasible for load sum x = C(W)/t = 1 and satisfies the
KKT conditions with multiplier nu (each x_k minimises its 1-D Lagrangian); the problem is strictly convex, so it is optimal, and its cost is
nu - E(W)/t^2 = W/C(W) - E(W)/C(W)^2 = Phi(W).  (If C is constant on an interval of W, W C - E is constant there by Lemma L(ii), so the value
does not depend on the choice of W.)  Surjectivity: C is continuous with limits 0 and infinity (Lemma L(iv)).  The algebraic identity
1/(4 psi) - Phi = (kappa^2 - 4 psi kappa + 4 psi^2)/(4 psi kappa^2) = (kappa - 2 psi)^2/(4 psi kappa^2) >= 0 gives Phi(W) <= 1/(4 psi(W)) <=
1/(4 inf psi); at a minimiser W_c of psi, psi'(W_c) = 0, so kappa = 2 psi by Lemma L(iii) and Phi(W_c) = 1/(4 psi(W_c)).  QED
Remark.  W is f's Hilbert-window shift (Lemma W' of Section 2: the window at scale t is the conversion band of the shift W); Proposition W
is the exact discrete form of Lemma W' + Theorem W*': f's one-sided profile at every scale is an explicit function of the conversion
capacity C and of E at the window shift.

#### 2.5.4 Theorem EC1 (exact identities for one-type conversion).  PROVED (model).
Let f' be the ONE-mode configuration with shift V > 0 (all carriers alive).  At scale tau put v = V/tau, c = C(V)/tau, e = E(V)/tau^2.  Then
 (I+)  P_f'(tau, +; 1) = (1 + c)^2 Q_+(tau (1 + c)) - v (1 + c) + e                         for every tau > 0;
 (I-)  P_f'(tau, -; 1) = (1 - c)^2 Q_-(tau (1 - c)) + v (1 - c) + e                         for tau >= C(V) (that is c <= 1);
 (I-b) P_f'(tau, -; 1) = [E(V) - E(W) - (V - W) C(W)]/tau^2, where W in [0, V] solves C(V) - C(W) = tau,   for tau <= C(V).
Proof.  Carriers of f' on side + at scale tau: a P- carrier with lam >= V/delta keeps a peak with margin delta - V/lam: box [0, u], cost
(delta u - v)x; a P- carrier in band(V) becomes a strict non-peak: with d = (v - delta u)/2 and e_k = ((2 + delta)u - v)/2 (so d + e_k = u) its side +
box is [-d, e_k], linear cost 0; a P- carrier in deep(V) becomes a peak of the other type: side + box [-u, 0]; P+ carriers: box [-u, 0].
Conjugates (mu >= 0; the optimal multiplier is >= 0 because the value is convex in S, nonnegative and 0 at S = 0): writing
g(nu) = max_{0 <= y <= u} [(nu - delta u) y - y^2] for f's conjugate of the same P- carrier, the first kind has conjugate g(mu + v); the band
kind has conjugate g(mu + v) - mu d - d^2 (substitute y = x + d in [0, u]: mu x - x^2 = (mu + v - delta u) y - y^2 - mu d - d^2); the other
kinds have conjugate 0.  For a deep carrier g(mu + v) = (mu + v - (1 + delta)u)u (saturated, since mu + v >= v >= (2 + delta)u).  Hence the
dual function of f' on side + is, for mu >= 0,
   D'(mu) = mu - sum_{P-} g(mu + v) + sum_{deep} g(mu + v) + sum_{band} (mu d + d^2) = D(mu + v) - v + mu c + e,
with D(nu) = nu - sum g(nu) the dual of f (load 1) and c = sum_deep u + sum_band d, e = sum_deep (v - (1+delta)u) u + sum_band d^2 (the lattice
functions at scale tau).  With nu = mu + v: D'(mu) = [nu (1 + c) - sum g(nu)] - v(1 + c) + e.  The bracket is the dual of f with load 1 + c,
whose maximiser nu* is >= v (by Lemma A the load C(v tau)/tau = c is carried at multiplier v, so the larger load 1 + c needs nu* >= v);
so max_{mu >= 0} D' = P_f(tau, +; 1 + c) - v(1 + c) + e, and homogeneity gives (I+).
Side -: P+ carriers have box [0, u] and cost (delta' u + v)x (conjugate g_-(mu - v), g_- = f's side - conjugate); band P- carriers have box
[-e_k, d], cost 0; deep P- carriers have box [0, u] and cost (v - (2 + delta)u)x; P- carriers with lam >= V/delta have box [-u, 0].  For
mu >= v the band and deep carriers are saturated at d and u, with conjugates mu d - d^2 and (mu - v + (1 + delta)u)u; for every mu these
values are lower bounds of the conjugates (feasible points); P- carriers with lam >= V/delta have conjugate 0 for mu >= 0.  So
D'_-(mu) <= D_-(mu - v) + v - mu c + e for all mu >= 0, with equality for mu >= v.  With nu = mu - v: the right side is [nu (1 - c) - sum g_-(nu)] + v(1 - c) + e.  If c <= 1 its maximiser over nu is >= 0, i.e.
mu >= v, where equality holds; so P_f'(tau, -; 1) = P_f(tau, -; 1 - c) + v(1 - c) + e, and homogeneity gives (I-).
(I-b): let c >= 1, W in [0, V] with C(V) - C(W) = tau, w = W/tau, mu' = v - w in [0, v].  Candidate: x = 0 on P+ carriers and on P- carriers
with lam >= V/delta; on P- carriers x_k = x_k^f(v) - x_k^f(w), where x^f(.) is f's allocation of Lemma A (so x_k = d - x_k^f(w) on band(V),
u_k - x_k^f(w) on deep(V)).  Check of the KKT conditions with multiplier mu': on P+ carriers the 1-D minimiser is clip((mu' - delta'u - v)/2, 0, u)
= 0 because mu' <= v; on band carriers it is clip(mu'/2, -e_k, d) = min((v - w)/2, (v - delta u)/2), which equals d - x^f(w) (if u < w/delta,
x^f(w) = (w - delta u)/2 and d - x^f(w) = (v - w)/2; otherwise x^f(w) = 0); on deep carriers it is clip((mu' - v + (2 + delta)u)/2, 0, u) =
clip(((2 + delta)u - w)/2, 0, u), which equals u - x^f(w) case by case (u <= w/(2+delta): 0; between: ((2+delta)u - w)/2; u >= w/delta: u).
The total is C(V)/tau - C(W)/tau = 1.  By strict convexity this is the optimum, and mu' is the multiplier.  For fixed tau the load
s(w) = C_tau(v) - C_tau(w) runs over (0, c] as w decreases from v to 0, and dP/ds = mu' = v - w; integrating,
P = integral_w^v (v - w~) dC_tau(w~) = E_tau(v) - E_tau(w) - (v - w) C_tau(w) (by parts, E' = C), which is (I-b) after rescaling.  QED

#### 2.5.5 Corollary EC2 (the critical placement).  PROVED (model).
Let p_- := min psi (P- lattice), p_+ := min psi (P+ lattice), so sf_+ = 1/(4 p_-), sf_- = 1/(4 p_+).  Assume sf_+ >= sf_- (otherwise exchange
the roles of the types and convert P+ downwards).  Let W_c be a minimiser of psi for the P- lattice.  Then the ONE-mode configuration with
shift V = W_c satisfies P_f'(tau, s) <= sup P_f for every scale tau and both sides s; hence R = sup P_f'/sup P_f = 1 exactly.
Moreover, if the P+ lattice is a dilation of the P- lattice (mirror case, sf_+ = sf_-; this covers every layout of Sections 3-4), then
R(V) > 1 for every V with psi(V) > p_-: one-type conversion is critical at W_c and strictly worse everywhere else.
Proof.  At V = W_c: kappa(V) = 2 p_-, psi(V) = p_- (Lemma L(iii)); write p = p_-, s = sf_+ = 1/(4p), so c = 2pv, e = p v^2.
(I+): P' <= s(1 + 2pv)^2 - v(1 + 2pv) + p v^2 = s + v + p v^2 - v - 2p v^2 + p v^2 = s (using 4 s p = 1).
(I-), c <= 1: P' <= sf_- (1 - 2pv)^2 + v(1 - 2pv) + p v^2 <= s(1 - 2pv)^2 + v - p v^2 = s - v + p v^2 + v - p v^2 = s.
(I-b), c >= 1: with E(V) = p V^2, C(V) = 2pV and tau = C(V) - C(W), the inequality [p V^2 - E(W) - (V - W) C(W)] <= s tau^2 is, after
multiplying by 4p and expanding, equivalent to C(W)^2 - 4p (W C(W) - E(W)) >= 0, i.e. W^2 [kappa(W)^2 - 4p (kappa(W) - psi(W))] >= 0.  Since
kappa(W) - psi(W) >= 0 (Lemma L(ii)) and p <= psi(W), the bracket is >= kappa^2 - 4 psi (kappa - psi) = (kappa - 2 psi)^2 >= 0.
Strictness away from W_c (mirror case sf_+ = sf_- = s): choose the scales tau_n -> infinity with tau_n (1 + c_n) at an argmax of Q_+
(possible since tau(1 + c) = tau + C(V) is onto); by (I+) P' = s + v_n (2 kappa s - 1) + v_n^2 (kappa^2 s - kappa + psi(V)).  If 2 kappa(V) s > 1
this exceeds s for large n; if 2 kappa s < 1 use (I-) at scales with tau (1 - c) = tau - C(V) at an argmax of Q_- (same expansion with the
sign of the linear term reversed); if 2 kappa s = 1, i.e. kappa(V) = 2p, the quadratic coefficient is psi(V) - p > 0.  QED
Remarks.  (1) The excess of a misplaced shift is first order in the placement error: R(V) - 1 = O(|ln V - ln W_c|); a grid of 10 per
octave produces the 0.1-0.3 per cent values of the earlier parts.  (2) The only carriers used below the band are the deep P- carriers
with lam >= W/(2 + delta) in (I-b); if all carriers deeper than V 2^-L are destroyed (C-B1 destruction below the restored groups), the
value changes only at scales with W < (2 + delta_max) V 2^-L, by at most the capacity lost, O(2^-L) (SKETCH; numerics in 2.5.6).
(3) Multiplicities (several carriers at the same depth, e.g. the 4-class cancellation layouts with V-only shifts) and mixed margins are
covered: the lattice functions are sums over carriers.  (4) Theorem EC1 is the exact discrete statement behind "one-type conversion is
exactly critical" (Proposition FO, continuum): the first-order coefficient 2 kappa(V) s - 1 vanishes iff kappa(V) = 1/(2s), and the
second-order coefficient psi(V) - p vanishes iff V minimises psi.

#### 2.5.6 Numerical confirmation (scripts v2_exact_check.py, v2_vscan_refined.py, v2_verify_refined.py; refined sup over tau: 96 or 64 per
octave plus bounded Brent refinement of the best points).  NUMERICAL.
 * Parametrisation Q_+(C(W)) = Phi(W): error <= 9e-16; sup P_f = 1/(4 min psi): agreement to 1e-12; identity (I+) to 3e-13; (I-b) to 2e-13;
   kappa(W_c) - 2 psi(W_c) = O(1e-9) (argmin precision), for the 8 self-similar layouts k1_d1, k1_d3, k1_d03, half_d1, half_d03, third_d1,
   mix (margins 0.3 and 3), mix2 (margins 0.2, 2, 5, P+ phase 0.25).
 * R at W_c (refined): 1 + O(1e-8) in all 8 layouts (residual = argmin precision times the kink slope); at the exact rational
   minimisers V = 7/6 (k1_d1 and the 4-class layout h = 1), 28/5 (h = 2), 7/5 (half_d1), 47/30 (k1_d03): R = 1 - 1e-12.
   Exact values: k1_d1: W_c = 7/6, sup P_f = 7/11, psi_min = 11/28; k1_d3: 11/6, 11/8; half_d1: 7/5, 21/16.
 * Kink: R(W_c (1 +- 0.001)) - 1 = 2e-4 to 1.1e-3, R(W_c (1 +- 0.01)) - 1 = 2e-3 to 1.1e-2.
 * The earlier V-only optimisers (12 or 24 tau points per octave) reported 0.9999997 / 1.0000117 / 1.00001: grid exploitation; the
   refined values at those placements are 1.000044 / 1.0000037 / 1.000000002, all consistent with min R = 1 at W_c.
 * Restoration depth (v2_restore_depth.py): with all carriers deeper than V 2^-L dead, R - 1 = 0.035, 0.0086, 0.00053 for L = 6, 8, 12
   (one carrier per octave, margin 1), i.e. about 2.2 x 2^-L; 2.5 x 2^-L (one per 2 octaves), 0.9 x 2^-L (margin 0.3).  See 3.1(vi).

## 3. Test (b): the capacity route (R6) of N1-ref / R3-ref

Question.  Can an admissible T force, at every junction of every NA approximant, a Hilbert/room load above the available two-type
conversion capacity?  (N1-ref reproduced R = 1.09 and 1.45 with one converted type and R = 1.0 with two types.)

### 3.1 Numerics (NUMERICAL, model level; exact solver v2_sep.py; tau grids 24 per octave; placements scanned over one grid period)
Modes: ONE = one absolute shift V of all carriers (one type converted); TWO = P- up and P+ down by V (both types converted in the
same band, E-type group scalar).  kd = 0: shifted carriers below the band stay alive; kd = 1: everything below the band is dead
(destruction immediately below the junction band: the hardest case for the approximant).
IMPORTANT (revision): the ONE kd = 0 values in (i)-(iv) below were obtained with V on a finite grid of placements.  By Corollary EC2
(2.5.5, PROVED) the exact optimum of ONE mode with kd = 0 is R = 1 at V = W_c (the minimiser of psi), and R(V) - 1 is of first order in
the placement error; refined computations at W_c give R = 1 + O(1e-8) in all eight self-similar layouts below (2.5.6).  The grid values
are kept only as a record of the earlier computations.
 (i) Earlier layout (2 carriers per type per octave, r = 1/2), delta = 1:
     ONE, kd = 0: grid best R = 1.0018 (narrow optimum near V = 0.582(1 + delta) = 1.164; exact: W_c = 7/6, R = 1);
     ONE, kd = 1: best R = 1.577 (every placement);  TWO, kd = 0: 0.9970;  TWO, kd = 1: 0.9978 (every placement; maxima always in the
     matched region tau = 2^12, i.e. no boundary-layer excess at all).
     The earlier "one shift R = 1.0158" (oneshift_A0.py) is a placement artefact of its 0.1-step scan (both solvers give 1.0168 at
     sc = 0.6 and 1.0039 at sc = 0.5875).
 (ii) k carriers per octave per type: ONE kd 0 (grid): delta = 1: 1.0017 (k = 4), 1.00015 (k = 8); delta = 0.3: 1.0009; delta = 3:
     1.0015 (exact optimum 1 in each case by Corollary EC2).
     TWO kd 1: delta = 1: 0.9992 (k = 4), 0.9986 (k = 8); delta = 0.3: 0.9986; delta = 3: 0.9996 — for EVERY placement.
 (iii) Self-similar sparse and mixed configurations (v2_scan3.py; best over 16 placements per period; last column: refined R at the
     critical placement W_c, v2_exact_check.py):
     | configuration | ONE kd 0 (grid) | TWO kd 1 (best / worst placement) | ONE kd 0 at W_c |
     | 1 carrier/octave, delta = 1 | 1.0111 | 0.9986 / 0.9995 | 1.000000001 (W_c = 7/6) |
     | 1 per octave, delta = 3 | 1.0003 | 0.9994 / 606 (empty band) | 1.00000003 (W_c = 11/6) |
     | 1 per octave, delta = 0.3 | 1.0013 | 0.9991 / 0.9993 | 1.000000001 (W_c = 47/30) |
     | 1 per 2 octaves, delta = 1 | 1.0021 | 0.9988 / 2858 (empty band) | 1.000000002 (W_c = 7/5) |
     | 1 per 2 octaves, delta = 0.3 | 1.0046 | 0.9994 / 0.9998 | 1.000000000005 (W_c = 1.42) |
     | 1 per 3 octaves, delta = 1 | - | 0.9999 / 8137 | 1.00000002 (W_c = 11/9) |
     | mixed margins {0.3, 3} per octave | 1.0005 | 0.9961 / 0.9963 | 1.0000000007 |
     | mixed {0.2, 2, 5}, period 2, P+ phase-shifted | 1.0070 | 0.9969 / 0.9974 | 1.000000005 |
     | 1 per octave, delta = 1, P+ phase-shifted 1/2 octave | - | 0.9988 / 0.9996 | (covered by Corollary EC2) |
     (The residuals 1e-9 - 3e-8 are the precision of the numerical argmin of psi times the kink slope; at the exact rational minimisers
     R = 1 - 1e-12.)
 (iv) Near-continuum ONE mode (k = 32, 64; v2_continuum_bl.py; placement V = 1, not W_c): the profile is monotone in tau, maximal at
     the bottom where it equals the band-count rounding ratio (k = 64, V = 1: 101.44/101 = 1.0043) and decreasing through the boundary
     layer to 1 (1.0014 at tau = V, 1.00001 at 2^8 V).  This is the misplacement effect of Corollary EC2 (in the continuum every V is
     critical, Theorem W*'), not an intrinsic discreteness excess.
 (v) Re-runs of R3-ref: onetype_A.py / coupled_full.py reproduce 1.0910, 1.4468, 1.0901 (one shift) and 0.9998 (two shifts) with
     their parameters (earlier P3 part 2.1); under the real-norm coupling and fine placement these become (i)-(iii).
 (vi) Restoration depth (v2_restore_depth.py): ONE mode at W_c with every carrier deeper than V 2^-L dead: R - 1 = 10, 1.2, 0.375, 0.158,
     0.035, 0.0086, 0.00053 for L = 1, 2, 3, 4, 6, 8, 12 (1 carrier per octave, delta = 1); about 2.5 x 2^-L (1 per 2 octaves, delta = 1) and
     0.9 x 2^-L (delta = 0.3).  So R = 1 + O(2^-L): one-type conversion needs the deep region restored over L octaves, L -> infinity.

### 3.2 Decision for test (b): DEFEATED (model level).  The defeating approximant mechanisms and their proofs (model level).
Mechanism 1 (two-type conversion; E-type designs).  At a junction of the NA approximant, restore the coarse groups, choose the
junction group's scalar so that its band is converted in BOTH types (E-type designs: opposite detector coefficients for P+/P-, E 4.3
(O4); a group scalar is then a TWO-mode lever), let everything below the band be destroyed if the adversary forces it, and carry the
compact core errors by EC (R3 Thm EC).
Proof at model level.  (1) Load: by Theorem W*' f's one-sided load at every scale equals exactly the bottom capacity of ONE band of
its type, for every margin distribution; TWO-mode conversion doubles the bottom capacity (2.2).  (2) Above the band: Proposition FO
gives a strict first-order saving -c_1 (ln(a/delta) - 2/a) < 0 on both sides even with destruction right below the band (kd = 1).
(3) The boundary layer (tau ~ V): NUMERICAL, 3.1: R < 1 for every tested configuration and the best placement, and for every
placement when the band is non-empty.
Mechanism 2 (one-type conversion at the critical placement; every design with a global shift lever).  Shift all carriers by
V = W_c (the minimiser of psi for the binding type, 2.5) and restore the groups over L octaves below the band.  Proof at model level:
Corollary EC2 (PROVED): R = 1 exactly when the deep region is alive; R = 1 + O(2^-L) with L restored octaves (3.1(vi), SKETCH +
NUMERICAL).  This mechanism needs neither two-type conversion nor EC; it fails only when destruction right below the band is forced
(R >= 1.577, Proposition FO kd = 1), and then Mechanism 1 is used.
Hence no admissible T can force a load above the conversion capacity in Model N_RN: the capacity requirement of (R6) is met EXACTLY
by one converted band at the critical placement (Proposition W and Theorem EC1 are the discrete form of Theorem W*'), and with a
factor-2 margin at the bottom and a strict first-order margin above by two converted bands.
What the R3-ref/N1-ref deficits were.  R = 1.46, 2.07, 1.086 (bottom) came from peak costs 8-17 times below the real-norm value
2 M B delta (1.5); R = 1.09 (coupled, one shift) from twice the real-norm ratio plus band placement.  One-type conversion is exactly
critical (Corollary EC2), so the earlier one-type values 1.0003-1.011 were misplacements of V; it fails (>= 1.577) only when destruction
starts right below the band (FO: first-order excess c_1 (4/a) on the non-converted side).  So two-type conversion is needed exactly
when the adversary can force destruction right below the junction band; otherwise one type suffices.
Real-norm status.  SKETCH.  The block costs of the model are the refereed real-norm first-order and Hilbert terms (1.2), asymptotically
exact in the deep-junction limit (1.4); the converted band carries the switching component two-sidedly by the push calculus (ii)
(PROVED) and EC carries compact errors (R3 Thm EC, PROVED).  Missing for a theorem: R3's transport hypothesis (HT-EC) above the
junction (matched structure of f carried over to f' up to the band), the normalisation step (R3-ref P5), and a proof that the
model's f-profile is the true cost of the mate (the model is a sufficient-condition calculator for f', not a lower bound for f).

## 4. Test (a): transition cells for cancellation staircases, (LIN), and E's rigid design

Question (N2-ref).  Compute the finite transition-cell excess for cancellation staircases with non-restorable far parts (bounded
l_1 mass, C-B1), under N2's (LIN) (no alternative staircases), and for E's rigid design (A1)-(A5) against crossing conversions:
is there a configuration whose one-sided excess at the hand-over scale is bounded below uniformly in the depth?

### 4.1 Value calculus at a junction (definitions; identities PROVED by linearity).
Cancellation design: u_k = (v + E_k + c'_k psi_{g(k)} + K lambda_k sigma_k + r_k)/n_k with v the switching direction (v(zhat) = 0), E_k
in a FIXED d-dimensional space E_c of vectors on near free coordinates, psi_g the far part of group g (sup ||psi_g||_1 < infinity,
supports leaving every finite set, F_g := psi_g(z) != 0), r_k tiny.  Near-threshold at f: n_k u_k(zhat) = rho_k theta lambda_k n_k with
|rho_k| = 1 + delta_k, i.e.  c'_k = (rho_k theta lambda_k n_k - E_k(zhat))/F_g.  Levers of an NA approximant: V := v(x' - zhat), the window
functionals E -> E(eta) (eta = o(1) window move), the group scalars Delta_g := psi_g(z') - psi_g(z).  Value shifts:
   s_k = V + E_k(eta) + c'_k Delta_g = V + E_k(eta - (Delta_g/F_g) zhat|_near) + (Delta_g/F_g) rho_k theta lambda_k n_k.
C-B1 (N2-ref, PROVED): for all but finitely many groups Delta_g = -F_g + o(1) at every NA row, and then s_k = E_k(zhat) + o(1) = O(1):
those carriers are destroyed.  (LIN) is built into every cell below: destroyed groups are dead (no alternative staircase).

### 4.2 Lemma G (Gordan invariant, precise form).  PROVED (value calculus).
A balanced set is B with weights w >= 0, sum w = 1, sum_B w_k E_k = 0.  Let B_- (P- carriers, one group g_1) and B_+ (P+ carriers,
one group g_2, possibly g_2 = g_1) be balanced, with all members converted at f', ||eta||_inf <= epsilon, and let each contain two
classes with E_k(zhat) - E_{k'}(zhat) =: e_spread > 0 (automatic for balanced sets with some E_k(zhat) != 0), and let the depths be
so small that 2(1 + delta_max) theta max_B lambda n <= e_spread/2.  Then, with ||E|| := max_k ||E_k||_1,
|Delta_{g_i}|/|F_{g_i}| <= eps_i := 2[(2 + delta_max) theta max_B lambda n + 2 epsilon ||E||]/e_spread and
   V >= theta sum_{B_-} w lambda n (delta - eps_1(1 + delta)),      V <= -theta sum_{B_+} w' lambda n (delta - eps_2(1 + delta)),
which are incompatible once eps_1, eps_2 < delta_min/(1 + delta_min) (always true as depth -> 0 and epsilon -> 0).
Proof.  Both members of a pair lie in their conversion windows, so |s_k - s_{k'}| <= (2 + delta_max) theta max lambda n.  By the
shift formula, s_k - s_{k'} = (E_k - E_{k'})(eta) - (Delta/F)(E_k - E_{k'})(zhat) + (Delta/F) theta (rho_k lambda_k n_k - rho_{k'} lambda_{k'} n_{k'}),
so |Delta/F| (e_spread - 2(1 + delta_max) theta max lambda n) <= (2 + delta_max) theta max lambda n + 2 epsilon ||E||, which gives the bound
on |Delta|/|F| under the depth condition.  Averaging the shift over
B_- with balance: sum w s = V + (Delta_1/F_1) theta sum w rho lambda n with rho = -(1 + delta); conversion needs sum w s >= theta sum w delta
lambda n; rearrange; B_+ symmetric.  QED
(The earlier statement "Psi = O(max lambda)" is the small-Delta case; the precise form also covers large group scalars, which
destroy the group.)  Exact rational check of the linear algebra: check_gordan.py (300 random designs and levers: True/True).

### 4.3 Lemma GB (cross-group balanced two-type conversion).  PROVED (value calculus).
If two controllable groups g != g' share the near-error directions (classes P-,+- with errors -+F e, P+,+- with -+F f, e(zhat) =
f(zhat) = 1, so c' = +-1 up to O(lambda)), then V = 0, eta = 0, Delta_g = s_1 > 0, Delta_{g'} = -s_2 < 0 convert P-,+ (g) and P-,- (g')
upward and P+,- (g), P+,+ (g') downward, and the sets {P-,+(g), P-,-(g')}, {P+,-(g), P+,+(g')} are balanced.  For d >= 1: the directions
of any d + 1 groups lie in the affine hyperplane {e(zhat) = 1} of E_c and are affinely dependent; with 2(d + 1) controllable groups the
signs of the Delta_g can be chosen independently for a balanced P- set and a balanced P+ set.  (No contradiction with Lemma G: the
balanced sets meet two groups.)

### 4.4 The structure of the cancellation cell: first-order criticality and the exact V-strategy.  PROVED (model level).
By Lemma G every balanced pair of a type has pair-average shift V, for EVERY lever combination; f's side combinations are balanced
(near errors cost first order at f).  Hence the Gordan structure of Proposition SR (2.4) holds for every approximant of a
cancellation design: the two sides' first-order changes above the junction add up to >= 0.  No strict first-order saving exists
(contrast: E's design, 4.6).  The pure V-shift (eta = 0, Delta_g = 0 for the restored groups) is available in EVERY cancellation
design: it shifts every alive carrier by the same V, keeps every balanced combination balanced (no near error is created, no EC is
needed) and is exactly ONE mode.  By Corollary EC2 (2.5.5) it has R = 1 EXACTLY at V = W_c when the groups below the band are restored,
and R = 1 + O(2^-L) when L octaves below the band are restored (3.1(vi)); C-B1 allows any finite number of restored groups.  So the
cancellation cell has NO excess at the model level, at any order.  (The earlier reading "the cell excess is a second-order /
discreteness quantity" was based on grid placements of V; see 4.5 and correction C10.)
Lemma BAL (the pure V-shift creates no near error).  PROVED (model).  Assume (Bal): f's optimal allocations are balanced at every
scale and side, sum_k x_k(tau) E_k = 0 (the defining property of cancellation staircases: near errors cost first order at f).  Then
every optimal allocation of the pure V-shift f' (all alive carriers shifted by V) is balanced; hence the near-error terms of Model N_RN
(We|E|/tau or EC at weight Bec) vanish at f', and Theorem EC1 / Corollary EC2 hold verbatim in the model with near errors.
Proof.  By homogeneity the optimal allocation of f at scale tau and load S is S x^f(tau S; 1), so every allocation x^f(tau, nu) of Lemma
A (the allocation of f at a multiplier nu, which is optimal for the load C(nu tau)/tau) is a nonnegative multiple of an optimal
allocation of f and therefore balanced.  The proof of Theorem EC1 identifies the optimal allocations of f': on side + it is
x^f(tau, nu*) - x^f(tau, v) on P- carriers (high: x^f(nu*); band: x^f(nu*) - d = x^f(nu*) - x^f(v); deep: 0 = u - u) and 0 on P+; on side -
it is the side - allocation of f at the multiplier mu - v on P+ carriers plus x^f(tau, v) - x^f(tau, w) on P- carriers (w = 0 in the
regime c <= 1, where the new carriers are saturated: x^f(tau, v)).  Differences and sums of balanced allocations are balanced.  QED
(If f's balance were realised only by the near-error terms of the cost and not by f's separable optimum, f's profile would include
first-order error costs; such f are not cancellation staircases in the sense of N2/N2-ref.)

### 4.5 Cell numerics (NUMERICAL, model level; exact dual solver v2_gb.py validated against cvxpy to 5e-9; deep-junction limit We = 10^6).
Layout: 4 classes per depth, depth step h octaves, delta = 1, f0 = 1; EC at Hilbert weight Bec (Bec = inf: balanced usage only,
Bec = 0: free/pooled EC); best over the scanned strategies.
 | strategy | h | EC | best R |
 | pure V at the critical placement V = W_c (one type, balanced; groups below restored) | 1 | none needed | 1 exactly (Cor. EC2; refined numerics 1 - 1e-12 at W_c = 7/6) |
 | pure V at W_c | 2 | none needed | 1 exactly (Cor. EC2; numerics 1 - 1e-12 at W_c = 28/5) |
 | pure V, placements on a grid (earlier computation) | 1 / 2 | none | 1.0018 / 1.0021 (misplacement of V) |
 | single group, global levers (V, alpha, beta) | 1 | free (Bec = 0) | 0.99990 (max in the matched region) |
 | single group, global levers | 2 | free | 0.99952 (max in the matched region) |
 | single group, local optimisation over (V, alpha, beta), balanced only (Nelder-Mead, 12 tau per octave) | 1 / 2 | none | tied optimiser (alpha = beta) converges to pure V near W_c (alpha = beta = O(2e-5) V; V = 1.16676, 5.6001); its reported 0.9999997 / 1.0000117 were tau-grid exploitation, refined 1.000044 / 1.0000037 at those V; untied runs (h = 1: beta = -0.65 V) not re-verified (C11) |
 | Lemma GB, L = 4, partner 2 groups below | 1 | Bec = 0.25 / 1 / 4 | 1.000097 / 1.000097 / 1.000108 |
 | Lemma GB, L = 4, gp = 2 | 1 | none | 1.0073 |
 | Lemma GB, L = 8, gp = 2 | 2 | Bec = 1 | 1.0000001 |
 | Lemma GB, adjacent partner (gp = 1), L = 4 | 1 | 0.25 / 1 / 4 | 1.0050 / 1.0072 / 1.0547 |
 | Lemma GB, short groups L = 2 | 1 | 1 | 1.0176 (gp = 2), 1.1037 (gp = 1) |
 | Lemma GB, delta = 3, L = 4, gp = 2 | 1 | 1 | 1.00038 |
CORRECTIONS of the earlier P3 parts.  (1) The earlier single-group numbers (R = 1.023-1.044, 1.092 in the deep limit, "Lemma G is a
genuine 9 per cent single-group obstruction") came from the family s = (V, V, 2V + u, -u), u >= 0.5V, which excludes the pure V-shift;
the pure V-shift is balanced and gives R = 1 at W_c: there is no single-group obstruction at all.  (2) The earlier cross-group
values 0.9989-1.0001 were obtained on a 3-per-octave tau grid; at the earlier placements the fine-grid value is 1.0212 (confirmed by
cvxpy at tau = 0.8409); with placements scanned over two depth steps the best is 1.0001 (L = 4), consistent in size but NOT <= 1.

### 4.6 E's rigid design (A1)-(A5) against crossing conversions.  DEFEATED (model level).
(O4) (E 4.3: one-sided far absorption of O(1) detector errors forces opposite detector coefficients for P+ and P-) makes every group
scalar a TWO-mode lever: the balanced averages of the two types move in opposite directions, the Gordan structure fails, and
Proposition FO gives a strict first-order saving; core errors in the compact E_c are carried by EC (R3 Thm EC) while f pays them
(A >= 0).  Numerically (Section 3.1) TWO mode with destruction right below the band gives R < 1 for every configuration tested.
Crossing conversions with PRIVATE far parts (N2 Design (B)(iii)) are the special case of Lemma GB with one class per group.

## 5. Decisions, defeating mechanisms, and what remains

### 5.1 Test (b) (capacity route R6): DEFEATED at model level.
No admissible T can force, at a junction, a Hilbert/room load above the conversion capacity in Model N_RN.
 * One converted band suffices EXACTLY: by Proposition W (2.5.3) f's one-sided profile at every scale is an explicit function of the
   capacity C and of E at the window shift, and by Corollary EC2 (2.5.5, PROVED in the model) the one-type shift V = W_c gives
   sup P_f' = sup P_f, with the deep region restored (R = 1 + O(2^-L) with L restored octaves, 3.1(vi)).
 * Two converted bands give a factor-2 margin at the bottom (Theorem W*') and a strict first-order saving above the band, even with
   destruction right below the band (Proposition FO); numerically R < 1 in every tested configuration (Section 3).
 * The earlier deficits are artefacts: non-real-norm peak costs (1.5, 3.1(v)) and misplacement of the shift (Corollary EC2: R(V) - 1 is
   of first order in ln V - ln W_c).
What survives of (R6) is not a capacity statement.  The only configuration of Model N_RN with a first-order excess for every
approximant would combine (i) the Gordan structure (no two-type conversion, 2.4) with (ii) FORCED destruction of the deep region
right below the junction band (one type then pays c_1 (4/a), FO).  In the model (ii) is not forced: the shift V and the depth to which
groups are kept are independent choices of the approximant (see 5.3, item (R6-tie)).

### 5.2 Test (a) (transition cell): DEFEATED at model level, at every order.
 * E's rigid design (A1)-(A5): DEFEATED (TWO mode by (O4), strict first-order saving, EC for compact core errors; 4.6).
 * Cancellation staircases with non-restorable far parts (C-B1), (LIN), any near-error structure: the pure V-shift at the critical
   placement V = W_c, with the finitely many groups between the band and depth V 2^-L restored (allowed by C-B1), moves every alive
   carrier by the same amount, creates no near error and needs no EC and no cross-group partner; by Corollary EC2 its cell excess is
   exactly 0 for L = infinity and O(2^-L) for finite L (PROVED / SKETCH + NUMERICAL, 2.5.5, 3.1(vi)).  Lemma G (4.2) and the sum rule
   (2.4) remain true but are no longer obstructions: they only exclude a strict first-order SAVING, and Corollary EC2 shows that the
   neutral strategy is exact.
 * Answer to the question "is there a configuration whose one-sided excess at the hand-over scale is bounded below uniformly in the
   depth?": NO, in Model N_RN: for every pair of carrier lattices (any margins, multiplicities, sparse or dense, phase-shifted types)
   one-type conversion at W_c has R = 1 (Corollary EC2), and R = 1 + O(2^-L) with L restored octaves; E's design is even strictly
   favourable for the approximant (FO).  The numbers 1.0018 / 1.0021 / "about 0.2 per cent" of the draft and the earlier 2-9 per cent
   "single-group Gordan obstruction" are placement artefacts (C2, C10).
 * The alternative mechanisms (pooled EC: R = 0.9999 / 0.9995; cross-group conversion with EC, Lemma GB: R <= 1.0001) are no longer
   needed; they remain as independent evidence (4.5).

### 5.3 Status of Conjecture R6** and the remaining residual (OPEN).
Conjecture R6** (draft version: a uniformly positive excess from (G) Gordan structure, (E) escaping guarded near errors, (D) discrete
staircases): its model content is FALSE.  Clause (D) produces no excess (Corollary EC2 is a proof for every discrete lattice), and
clause (E) is irrelevant for the pure V-strategy, which moves no near error.  The statement as a claim about Martin's renormings is
therefore without any known mechanism; I record it as REFUTED AT MODEL LEVEL, not as a theorem about the real norm.
What remains OPEN (precise residuals; none of them is supported by a model computation):
 (R6-tie) A design in which keeping the groups below the junction band alive is incompatible with converting the band (destruction
   forced at depth >= V/(2 + delta_max) 2^-O(1)) while the Gordan structure holds.  Only such a design gives a first-order excess
   (FO: c_1 4/a; 3.1(i): R >= 1.577) against one-type conversion, and it must also exclude two-type conversion.  In cancellation
   designs C-B1 fixes only that all but finitely many groups are destroyed; WHICH finitely many survive is the approximant's choice,
   so (R6-tie) needs a new rigidity mechanism coupling the far parts of the groups below the band to the switching value V.  No such
   mechanism is known; E's design (the only design with forced cross-type couplings) admits TWO mode.
 (T) Real-norm transfer at exact criticality.  Since the model is exactly critical (R = 1), non-density would have to come from the
   real-norm corrections to Model N_RN: other resources, base-block coupling, other blocks, the o(1) errors of the deep-junction limit
   (1.4), and the realisability of the pure V-shift by an NA row with finite base support and the restored groups.  For density one
   needs the converse: these corrections are o(1) along f'_L (junction depth -> 0, L -> infinity).  For the pure V-strategy no EC
   is used, so R3's (HT-EC) is not needed; what is needed is the transport of the matched structure of f to f' above the band (R3-ref
   P5 normalisation) and the asymptotic exactness of the block part (1.4, HEURISTIC with PROVED ingredients).
What would prove density along this route: a real-norm version of Theorem EC1 for the explicit approximants f'_L: (1) exact
decomposition of the block cost of f'_L at every scale into the separable model plus o(1) (the identities (I+), (I-), (I-b) are
algebraic consequences of the separable structure, so a real-norm analogue needs only the separable block structure of Martin's norm
at the junction, 1.2-1.4); (2) a proof that the restored groups and the shift V are realisable by NA rows with finite base support
(C-B1 and the global lever V of 4.1 suggest yes); (3) control of the base block and of the other blocks (unchanged by the V-shift up
to o(1)).
What would refute it: a design realising (R6-tie), together with a real-norm lower bound uniform over all NA rows (N2-ref Section 1
criterion) with first-order precision (the FO excess c_1 4/a is first order, so the precision required is much weaker than for the
second-order residue of the draft).

## 6. Corrections to earlier material (this rerun re-checked every claim of the unfinished earlier P3 parts 0-3 and of its own drafts)

 C1 (earlier part 2.3(b), 3.3) "One-type boundary-layer deficit R = 1.0158 (delta 1), 1.0296 (delta 3)": placement artefact of a 0.1-step
    scan and a 3-per-octave tau grid.  Finer placement grids gave 1.0018 (delta 1, 2/oct), 1.0015 (delta 3, 4/oct); the exact optimum is
    R = 1 at V = W_c (Corollary EC2, C10).  With destruction right below the band one type gives R >= 1.577 (delta 1): a first-order excess
    (Proposition FO), not a boundary-layer effect.
 C2 (earlier parts 1.3 Cor G1, 2.4(a)(c), 3.2) "Lemma G is a genuine single-group obstruction: 2.3-4.4 per cent, 9.2 per cent in the deep
    limit": FALSE as a statement about the cell.  The scanned family s = (V, V, 2V + u, -u), u >= 0.5V, excludes the balanced pure V-shift,
    which gives R = 1 at W_c.  Lemma G itself is correct (precise form 4.2): it forbids balanced TWO-type conversion inside one group.
 C3 (earlier part 2.4(b), 3.2) "Lemma GB with EC: R <= 1 up to 1e-4 (0.9989-1.0001)": not established — 3-per-octave tau grid; at the
    earlier placements the fine-grid value is 1.0212 (cvxpy-confirmed at tau = 0.8409).  With placements over two depth steps the best is
    1.0001 (L = 4), 1.0000001 (h = 2, L = 8); adjacent partners and short groups give 1.005-1.10.  (Superseded as a mechanism by
    Corollary EC2, which needs no cross-group partner.)
 C4 (earlier part 1.3) "Psi = 0 + O(max lambda)" in Lemma G: correct only for group scalars of size O(lambda); precise form 4.2.
 C5 (earlier part 1.1, 1.4) Lemma W and Theorem W*: CORRECT; generalised to arbitrary margin mixtures (Lemma W', Theorem W*') and, in
    exact discrete form, to Proposition W (2.5.3).  The peak-cost coupling cpk = 2MB: CORRECT, with the additional justification that
    both costs lie in the same block excess (Lemma B0).
 C6 (earlier part 3.1-3.3) "Two-type conversion is available at some junction in every far-rigid design class": true for E-type designs
    (opposite detector coefficients) and, via Lemma GB, for cancellation designs with a fixed finite-dimensional near-error space; but in
    cancellation designs two-type conversion is NOT strictly favourable at first order (sum rule) and depends on EC.  It is also not
    needed: one-type conversion at W_c is exact (Corollary EC2).
 C7 R3-ref / N1-ref (R6) numbers: the bottom deficits R = 1.46, 2.07, 1.086 rest on peak costs 8-17 times below the real-norm value;
    the coupled one-shift R = 1.090 on twice the real-norm ratio plus placement; their two-shift R = 1.0000 is confirmed and strengthened
    (every placement, destruction right below the band, sparse and mixed configurations).
 C8 E's Model N (r1/E 4.1-4.4, 7.1-7.4): the peak cost a0 lambda |rho| is not the real-norm law 2MB (|rho| - 1) lambda; "one shift
    R = 2.82" and "R(J) > 1 for every bounded J in the error-dominated regime" are artefacts of this law; in the real norm an
    error-dominated regime is a large core-error constant A, which favours the approximant once EC carries core errors.
 C9 (this rerun) First version of Proposition FO had the coefficient 2/a for ONE mode, side -, kd = 1; the correct value is 4/a (the
    dead P+ carriers below the band were omitted); found by the numerical check v2_check_FO.py.
 C10 (this rerun, draft Sections 0, 3-5) "One-type conversion keeps a positive discreteness excess: R = 1.0018 (h = 1), 1.0021 (h = 2),
    1.0003-1.011 (sparse/mixed), 'about 0.2 per cent'; Conjecture R6** clause (D)": FALSE.  These are misplacements of V on a finite
    grid.  The exact optimum is R = 1 at the minimiser W_c of psi (Corollary EC2, PROVED in the model), confirmed numerically to 1e-8 in
    eight layouts and to 1e-12 at the exact rational minimisers 7/6, 28/5, 7/5, 47/30.
 C11 (this rerun) Local optimisers over (V, alpha, beta) and over V alone reported R = 0.9999987, 0.9999997 (h = 1), 1.0000112,
    1.0000117 (h = 2), 1.000011 / 1.0000001 / 1.0000003 (sparse layouts).  All of them optimised V against a fixed tau grid (12 or 24
    per octave), which lets the optimiser hide maxima between grid points.  For the pure V-shift (tied optimiser, alpha = beta = 0 up to
    2e-5) a value below 1 is impossible (R >= 1 for every one-type shift: far-field expansion in the proof of Corollary EC2); refined sup
    over tau (v2_verify_refined.py): 1.000044 (h = 1), 1.0000037 (h = 2), 1.0000000022 (half_d1) at those V, and 1 at W_c.  The untied
    optimum (beta = -0.65 V, h = 1) was not re-verified with the refined sup; it is not needed.

## 7. Results table

| # | Result | Status | Where |
|---|---|---|---|
| 1 | Per-carrier block costs in carried units (peak 2MB delta lambda|x|/|t|, Hilbert B x^2, room) | PROVED (refereed sources) | 1.2 |
| 2 | Lemma B0: weighted excess budget; peak and Hilbert costs in the same block excess | PROVED | 1.3 |
| 3 | Model N_RN block part asymptotically exact in the deep-junction limit | HEURISTIC (ingredients PROVED) | 1.4 |
| 4 | Earlier models (E Model N, R3-ref scripts) use non-real-norm peak costs | PROVED (from scripts) | 1.5 |
| 5 | Lemma W': f's Hilbert window = conversion band of the shift mu tau/(2MB), any margins | PROVED (model) | 2.1 |
| 6 | Theorem W*': continuum load = one band's bottom capacity, any margin mixture | PROVED (model) | 2.2 |
| 7 | Proposition FO: first-order profile changes (TWO strictly better; ONE critical; ONE kd 1 excess 4/a) | PROVED (model, continuum) | 2.3 |
| 8 | Proposition SR: sum rule (no first-order saving under the Gordan structure) | PROVED (model) | 2.4 |
| 9 | Lemma L (lattice functions C, E: E' = C, kappa >= psi, psi' = (kappa - 2 psi)/V) | PROVED | 2.5.1 |
| 10 | Lemma A (f's allocation at a multiplier: load C/tau, cost nu S - E/tau^2) | PROVED (model) | 2.5.2 |
| 11 | Proposition W: Q(C(W)) = (kappa - psi)/kappa^2 exactly; sup P_f = 1/(4 min psi) | PROVED (model) | 2.5.3 |
| 12 | Theorem EC1: exact identities (I+), (I-), (I-b) for one-type conversion | PROVED (model) | 2.5.4 |
| 13 | Corollary EC2: one-type conversion at V = W_c has R = 1 exactly (any lattices); R(V) > 1 for psi(V) > min psi | PROVED (model) | 2.5.5 |
| 14 | Restoration depth: R = 1 + O(2^-L) with L restored octaves (constants 0.9-2.5) | SKETCH + NUMERICAL | 2.5.5 Rem. 2, 3.1(vi) |
| 15 | Numerical confirmation of 9-13 (8 layouts; identities to 3e-13; R(W_c) = 1 to 1e-8, 1e-12 at rational W_c) | NUMERICAL | 2.5.6, 3.1(iii) |
| 16 | Test (b): two-type R < 1 in all tested configurations (dense, sparse, mixed; kd = 1) | NUMERICAL | 3.1 |
| 17 | Test (b): capacity route DEFEATED at model level (one band suffices exactly; two bands with margin) | PROVED at model level (bottom, first order, and exact one-type identity); real norm SKETCH | 3.2, 5.1 |
| 18 | One-type conversion: R = 1 at W_c (deep region alive); R >= 1.577 with destruction right below the band | PROVED (model) + NUMERICAL | 2.3, 2.5.5, 3.1 |
| 19 | Lemma G (precise form, large group scalars included) | PROVED (value calculus) | 4.2 |
| 20 | Lemma GB (cross-group balanced two-type conversion; general d) | PROVED (value calculus) | 4.3 |
| 21 | Cancellation cells: no strict first-order saving (Gordan + SR), but the pure V-shift at W_c is exact: no excess at any order | PROVED (model) | 4.4, 2.5.5 |
| 21b | Lemma BAL: under (Bal) the pure V-shift's optimal allocations are balanced (no near-error cost; EC1/EC2 hold with near errors) | PROVED (model) | 4.4 |
| 22 | Cancellation cells, other strategies: R <= 1 with pooled EC; <= 1.0001 with GB + EC (long groups) | NUMERICAL | 4.5 |
| 23 | E's rigid design (A1)-(A5) defeated (TWO mode by (O4)) | PROVED at model level (first order) + NUMERICAL; real norm SKETCH | 4.6 |
| 24 | Test (a): DEFEATED at model level at every order (no configuration with uniformly positive hand-over excess) | PROVED (model) | 5.2 |
| 25 | Conjecture R6** (draft): model content refuted | FALSE (at model level) | 5.3 |
| 26 | Residuals (R6-tie) and (T) (real-norm transfer at exact criticality) | OPEN | 5.3 |
| 27 | Non-density of NA((c_0, p), l_2^2) / failure of property B for l_2^2 | NOT CLAIMED (OPEN) | 0 |
| 28 | Corrections C1-C11 | PROVED / NUMERICAL as stated | 6 |

## 8. Scripts (all in ctx/r15/P3_work/; numerics are sanity checks of the model only)
v2_sep.py (exact separable solver), v2_validate.py (vs cvxpy, 1.6e-8), v2_junction.py, v2_scan.py, v2_scan2.py, v2_scan3.py (junction
scans; outputs v2_batch*.out, v2scan*.json), v2_check_Wstar_mix.py (Theorem W*', Lemma W', mpmath), v2_check_FO.py (Proposition FO),
v2_continuum_one.py, v2_continuum_bl.py (near-continuum ONE mode), v2_gb.py (exact dual solver with near-error coupling),
v2_gb_validate.py (vs cvxpy, 5e-9), v2_gb_confirm.py (cvxpy confirmation of correction C3), v2_gb_scan.py (Lemma GB cells),
v2_cell1.py (single-group global levers), v2_cell_opt.py, v2_cell_opt_tied.py (local optimisation; outputs v2_opt*.out, see C11),
v2_one_fine.py (fine placement of ONE mode; v2_batch7.out), v2_verify_refined.py (refined sup over tau; v2_batch8.out),
v2_vscan_refined.py (R at exact rational W_c and nearby; v2_batch9*.out), v2_kappa.py (first-order criticality kappa(V) = 1/(2 sup P_f)),
v2_exact_check.py (Proposition W, Theorem EC1, Corollary EC2; v2_batch10.out), v2_profile_diff.py (profile comparison at W_c),
v2_restore_depth.py (restoration depth; v2_restore_*.out), check_gordan.py (exact rational check of Lemmas G, GB), v2_random.py
(random configurations: discarded as uninformative), v2_reconcile.py (correction C1).
Earlier instance's scripts (cell_bpc*.py, bpc_*.py, oneshift_*.py, scan_coupled.py, check_*.py) are kept; their outputs are superseded
where C1-C3 apply.

