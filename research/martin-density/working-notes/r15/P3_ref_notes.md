# P3 referee notes (Round 15): transition-cell excess and the capacity route -- full checks, proofs of fixes, referee additions

Read in full: r15/P3_notes.md (= P3_final_s0..s6), P3_part0-8, P3_work scripts (v2_*.py, check_gordan.py), BRIEFING_R2 Addenda 13, 14a,
14b, NEG; neg/N1, N2, N3 referee reports and ref notes (push calculus, C-B1, Lemma 1.4'', E-2); r3/R3_referee.md and r3/refwork,
r3/work/modelN.py; r1/E_notes 4.1-4.4, 7.3-7.5.  Referee scripts: r15/P3_ref_work/ (independent solver sep_ref.py written from
scratch; ec_fast.py, ec_vec.py, ec_vec2.py exact/tabulated identities validated against it; check_ec.py, check_sr.py, check_bal.py,
bal_vec*.py, cap_shift*.py, cap_exact.py, nonsimplex*.py, qosc.py, check_foa*.py).  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN;
NUMERICAL = model sanity checks only.  "Model" = P3's Model N_RN (separable real-norm junction model, Section 1.4 of P3).

## Summary of findings
 1. Every model-level identity of P3 Section 2 re-derived and confirmed: Lemma B0, the constants (C1)-(C3), Lemma W', Theorem W*',
    Proposition FO (all six coefficients), Lemma L, Lemma A, Proposition W, Theorem EC1, Corollary EC2 (independent solver: identities
    to 12 digits, R(W_c) = 1 to 3e-8, kink slopes 0.56 / 1.15 per per cent of misplacement).
 2. Proposition SR is FALSE as stated for discrete lattices: the sum of the first-order changes equals (C(V)/tau)(mu^+ - mu^-) and can be
    negative (both sides decrease at first order at some scales).  Correct in the continuum.  Harmless for P3's conclusions.
 3. MAIN GAP.  Lemma BAL's hypothesis (Bal) is NOT the defining property of cancellation staircases.  For error classes at different
    depths (the generic case in Martin's norm) the pure V-shift FAILS: R >= 1.074 (two classes +-e, half-octave phase), R unbounded
    (sparse antiphase classes, empty bands).  So test (a) is not defeated by P3's mechanism.
 4. REPAIR (referee, PROVED at model level): Bregman form of one-type conversion and THEOREM KKT.  f's profile is H(t)/t^2 with H the
    balanced infimal convolution of the A_c = int C_c^{-1}; class shifts equal to the KKT multipliers (V, eta) of f's balancing problem
    at the critical scale (global shift + window functional) give R = 1 exactly for EVERY cancellation cell with a fixed
    finite-dimensional near-error space (numerically 1 to 1e-11).  Test (a)'s conclusion is thereby established at A = 0, with no EC,
    no cross-group partner and no two-type conversion.
 5. Restoration depth upgraded from SKETCH to PROVED (model): R <= 1 + K 2^-L.
 6. Scope: all model theorems are at A = 0 (no first-order base costs at f').  With persistent base costs (EC unavailable) ONE-mode
    conversion has a first-order excess c_1(ln(a/delta) - l_A) (FO-A, PROVED in the continuum, numerically confirmed); TWO mode with
    kd = 1 has c_1(2/a - l_A).  New residual (R6-A): what survives of clause (E) of the draft Conjecture R6** is escaping CORE errors.
 7. No claim of non-density; no admissible T or mate is constructed; the main question stays OPEN.

# P3 referee, part 1: Section 1 (constants, Lemma B0, Model N_RN) and Section 2.1-2.4 (W', W*', FO, SR)

Sources re-read: P3_notes.md (all), P3_part2/4/5/8, neg/N2_referee.md, N2_ref_notes.md (push calculus, C-B1, Lemma 1.4''),
r3/R3_referee.md (main finding R6), r3/refwork/coupled_full.py and r3/work/modelN.py (Model N code), r1/E_notes 4.1-4.4, 7.3-7.5.

## 1.1 Per-carrier block costs (C1)-(C3).  CORRECT (re-derived).
Block m, forced data (w, M, C, zeta), lem:threshold zeta/|zeta| = alpha + D^2 w/C.  With rho_k := m u_k(xi) C/(Phi(k) M |zeta|) one gets
zeta(k)/|zeta| = rho_k Phi(k)^2 M/C, hence on the peak set alpha(k) = (rho_k - s_k) Phi(k)^2 M/C = s_k delta_k Phi(k)^2 M/C for rho_k =
s_k(1 + delta_k).  For W = w + t(omega - d w) (push calculus form) <omega - d w, zeta/|zeta|> = <omega, alpha>, so the block excess
E_W = N(W) - 1 - t<Omega, zeta/|zeta|> equals [N(W) - 1] + t sum_P |omega_k||alpha(k)| for inward pushes.  With x_k = lambda_k omega_k,
lambda_k = m Phi(k): t|omega_k||alpha_k| = |t||x_k| delta_k lambda_k M/(m^2 C) = 2MB delta_k lambda_k |t||x_k| (B = 1/(2 m^2 C)).  Exact
Hilbert term (no sup-norm change, another peak keeps the sup): N(W) - 1 = sqrt((C + tdM)^2 + t^2(||D omega||^2 - d^2)) - (C + tdM)
<= t^2 ||D omega||^2/(2(C + tdM)), ||D omega||^2 = sum x_k^2/m^2, i.e. B sum x_k^2 up to 1 + O(depth).  Room (C3) from
|(1 - td) w(k) + t omega(k)| <= (1 - td) M.  All three agree with P3 1.2.

## 1.2 Lemma B0.  CORRECT (PROVED; it is G3 Lemma 1.1-1.3 in weighted form).
g in C(f) forces g(xi) = 0 (since (f + tg)(xi) = 1 + t g(xi) <= sqrt(1 + t^2) for all t); 1 = A(xi) + W(L** xi), A(xi) <= q_0 q*(A),
W(L**xi) <= (1 - q_0)||W||: the identity q_0 E_A + (1 - q_0) E_W = q_0 q*(A) + (1 - q_0)||W|| - 1 is exact and <= s(t) - 1 <= t^2/2.
Referee precision (B0-a).  B0 is a NECESSARY condition (the max-structure max(q*(A), ||W||) <= s(t) implies the weighted one).  The
model objective of P3 is exactly E_W/t^2 (peak part 2MB delta lambda|x|/tau + Hilbert B x^2) = (weighted budget)/(1 - q_0) - (base
part).  That the weighted budget is also asymptotically SUFFICIENT needs fair block-to-base rebalancing (move O(t^2) block norm along a
fixed V' with L*V' approximating a direction supported in supp a', where q* is differentiable with derivative xi'/q_0'; the naive
direction V' = w' is unfair by the far l_1-mass of f' - a' on free coordinates).  This is the "quadratic rebalancing" of r1/A and is
not re-proved in P3; it belongs to the transfer item (T).  It does not affect any model-level statement.
Precision (B0-b).  "Peak cost and Hilbert cost lie in the same excess with the same weight" is true for E_W.  In the push-calculus
decomposition the block NORM N(W) contains only the Hilbert term and the first-order peak cost sits in q*(A) (N2-ref push calculus
(iii)); the two views agree because (1 - q_0)|alpha(k)| = q_0 lambda_k mu^_k (zhat units).  The coupling L_k/B = 2 M delta_k is an
identity of the norm: CORRECT.

## 1.3 Diagnosis of the earlier models (1.5).  CORRECT.
Checked in the code: r3/work/modelN.py charges a0 lam |rho| |x|/tau on peaks; refwork/coupled_full.py sets a0 = cpk delta/(1 + delta),
so with cpk = 1, B = M = 1/2 the peak cost at f is 1 x delta lam/tau, twice the real-norm 2MB delta = delta/2.  onetype_A.py with
a0 = 0.03, B = 1, M = 1/2, delta = 1: 0.06 lam/tau against 2MB delta = 1: 17 times too small.  E's own justification of a0 (E 4.1:
"alpha_i ~ lambda_i Phi_i |rho_i|") is a rough estimate of the BLOCK peak cost; the exact coefficient is proportional to the margin.
So the R3-ref "bottom deficits" (R = 1.46, 2.07, 1.086) do rest on a non-real-norm peak/Hilbert ratio.  Caveat recorded below (1.6).

## 1.4 Lemma W'.  CORRECT (PROVED, model).
Re-derived: x_k = clip((mu - 2MB delta_k y_k)/(2B), 0, 2M y_k); x_k > 0 iff lambda_k < mu tau/(2MB delta_k); x_k < 2M y_k iff
lambda_k > mu tau/(2MB(2 + delta_k)); and a value shift s makes a P- peak a strict non-peak iff s/(2 + delta_k) < lambda_k < s/delta_k.
Precision (W'-a, fixable).  "theta lambda_k n_k normalised to lambda_k" hides a real point: if the switching direction enters u_k with
coefficient c_k/n_k (n_k = q*(T e_k)-normalisation, c_k the v-coefficient; both vary by O(1) in cancellation designs), work in
v-units y_k = c_k x_k/n_k and shift-depth Lambda_k := lambda_k n_k/c_k.  Then cost 2MB delta_k Lambda_k |y_k|/tau + B w_k^{-1} y_k^2 with
room w_k 2M Lambda_k/tau, w_k := (c_k/n_k)^2, and the window is still EXACTLY the band {s/(2 + delta_k) < Lambda_k < s/delta_k} (the
weight cancels in both inequalities).  So W' holds verbatim in Lambda; all capacities acquire the weights w_k (see part 2).

## 1.5 Theorem W*'.  CORRECT (PROVED, model, continuum).
Re-derived every integral: per class (a = 2 + delta, u = mu/(2B)) carried amount D[2u/a + u ln(a/delta) - u(1 - delta/a)] = D u ln(a/delta);
room-limited cost 4BM^2(1 + delta) int_0^{u/(Ma)} y dy = 2B(1 + delta)u^2/a^2; window cost B int (u^2 - M^2 delta^2 y^2) dy/y =
B u^2 [ln(a/delta) - 2(1 + delta)/a^2] (uses a^2 - delta^2 = 4(1 + delta)); total D B u^2 ln(a/delta).  KKT with a common multiplier
gives P_f = B S^2/N.  Bottom of f': band carriers are strict non-peaks with zero linear cost and room -> infinity, all other carriers
have linear cost -> infinity: B S^2/N.  Two converted types: B S^2/(N_- + N_+) <= (1/2) B S^2/min(N_-, N_+).

## 1.6 Proposition FO.  CORRECT (PROVED, model, continuum, constant margin; remainder estimate routine).
Re-derived all six coefficients by the envelope theorem (room multiplier eta = mu(1 - O(V/tau)) on saturated carriers):
 side +, any mode: margin drop above the band: -(2MBV/tau) S = -c_1 ln(a/delta).
 ONE side +: band room loss mu M D V(ln(a/delta) - 2/a)/tau = +c_1(ln(a/delta) - 2/a); below-band P- become P+ peaks: +c_1 (2/a).  Sum 0.
 ONE side -: margins rise +c_1 ln(a/delta); new free band room -c_1(ln(a/delta) - 2/a); deep P- -> usable P+ deep peaks -c_1(2/a) (kd 0);
   kd 1: no deep gain and f's own P+ carriers below the band dead (+c_1 2/a): total c_1(4/a).
 TWO: band room conserved (M(1 - rho') + M(1 + rho') = 2M per depth), so -c_1 ln(a/delta) (kd 0) and -c_1(ln(a/delta) - 2/a) (kd 1).
ln(a/delta) > 2/a: yes.  The remainder O((V/tau)^2) follows from strong convexity (2B) of the separable QP: perturbing linear costs/
boxes by O(V/tau) on the carried mass moves the optimum by O(V/tau), so the envelope error is quadratic.  Correction C9 (4/a, not 2/a)
confirmed.
Referee observation (FO-A, new, model level): with a first-order base cost A lambda/tau per unit at f AND at f' (core errors NOT
removed by EC at the scale tau), the window is narrower than a band and ONE mode is no longer critical above the band: carried
amount S = u D l_A with l_A := ln((2MB a + A)/(2MB delta + A)) < ln(a/delta), and the first-order changes become
   ONE, side +:  + c_1 (ln(a/delta) - l_A) > 0,      ONE, side -:  - c_1 (ln(a/delta) - l_A)   (kd 0).
So with A > 0 one-type conversion has a first-order EXCESS on the converted side at every scale where f' still pays the A-costs.
Harmless for P3's conclusions only because R3 Thm EC removes A-costs at f' below tau_gen and the excess at tau > tau_gen is
O(V/tau_gen) -> 0; but it shows that "A > 0 favours the approximant" (P3 1.5) is a statement that depends on EC at all scales
<= tau_gen >> V, not a model theorem.  (Derivation: Appendix A.2 below.)

## 1.7 Proposition SR (sum rule).  GAP: correct in the continuum (or when mu^+(tau) = mu^-(tau)); FALSE as stated for general
discrete lattices.
The cost terms cancel exactly (Gordan structure).  The room-term step "for deep carriers the box multiplier on one side equals the
value of the room on the other side up to O(max|s|/tau)" requires mu^+(tau) = mu^-(tau).  Counter-computation from P3's own exact
identities (I+), (I-) (ONE mode is Gordan with every V): expanding for v = V/tau -> 0,
   [P_f'(tau,+) - P_f(tau,+)] + [P_f'(tau,-) - P_f(tau,-)] = (C(V)/tau) (mu^+(tau) - mu^-(tau)) + O(v^2),
because d/dS[S^2 Q(tau S)] at S = 1 equals 2Q(tau) + tau Q'(tau) = mu(tau).  For phase-shifted discrete lattices mu^+(tau) != mu^-(tau)
at most tau, so the first-order sum is nonzero, of either sign (numerical confirmation: Appendix A.1).  Consequences: (i) the sentence "in
designs with the Gordan structure no approximant has a strict first-order saving" is proved only for the continuum / equal-multiplier
case; (ii) nothing in the defeat of the tests depends on SR (it is an adversary-favourable statement and Corollary EC2 is exact), so
the gap is harmless for P3's conclusions.  Fix: state SR with the hypothesis mu^+(tau) = mu^-(tau) (true in the continuum and for
mirror lattices with equal depths), and add the term (C(V)/tau)(mu^+ - mu^-) in general.

# P3 referee, part 2: Section 2.5 (Lemma L, Lemma A, Proposition W, Theorem EC1, Corollary EC2, restoration depth)

Independent solver: P3_ref_work/sep_ref.py (exact bisection on the multiplier; written from scratch, not from P3's v2_sep.py);
checks: P3_ref_work/check_ec.py (output reproduced below), check_sr.py.

## 2.1 Lemma L.  CORRECT (PROVED).
Per carrier c_k(V) = clip((V - delta_k lam_k)/2, 0, lam_k) and e_k(V) = int_0^V c_k (deep: (V - (1 + delta)lam)lam, band:
((V - delta lam)/2)^2, 0 above); continuity at both band edges checked; E' = C termwise (locally finitely many band carriers,
deep part dominated by sum lam); V C - E = int_0^V w dC >= 0 by parts; psi' = (V E' - 2E)/V^3 = (kappa - 2 psi)/V.
Precisions: (L-a) (iv) needs sum_{lam_k < x} lam_k -> 0 as x -> 0 and delta_k bounded below (else infinitely many coarse
carriers can sit in band(V)); both hold for the staircases considered.  (L-b) With the weights w_k of part 1 (W'-a), C, E are
sums of w_k c_k, w_k e_k and every item of Lemma L holds verbatim.

## 2.2 Lemma A.  CORRECT.  x_k(nu) = clip((nu - delta_k u_k)/2, 0, u_k) = c_k(nu tau)/tau; cost identities checked
(deep: (1 + delta)u^2 = nu u - (nu - (1 + delta)u)u; band: delta u d + d^2 = nu d - d^2).

## 2.3 Proposition W.  CORRECT (PROVED), with one hypothesis to add.
Q_+(C(W)) = W/C(W) - E(W)/C(W)^2 = (kappa - psi)/kappa^2 and 1/(4 psi) - Phi = (kappa - 2 psi)^2/(4 psi kappa^2): verified.
Precision (W-a, fixable): "sup_t Q_+ = 1/(4 inf psi), attained at C(W_c)" needs inf psi to be ATTAINED (true for log-periodic psi,
i.e. self-similar staircases).  If the infimum is only approached (W -> 0 or infinity) one gets sup Q_+ <= 1/(4 inf psi), and equality
needs kappa - 2 psi -> 0 along the minimising sequence, which is not automatic.  State the hypothesis.
Numerics (referee solver, one carrier per octave, delta = 1): min psi = 0.392857142857 = 11/28 at W_c = 1.16666666 = 7/6;
1/(4 min psi) = 0.636363636364 = 7/11; Q_+(C(W)) = (kappa - psi)/kappa^2 to 13 digits at W = 0.9, 1.1, 7/6, 1.5, 1.9.

## 2.4 Theorem EC1.  CORRECT (PROVED, model).  Every conjugate re-derived.
(I+): first-kind conjugate g(mu + v); band conjugate g(mu + v) - mu d - d^2 via y = x + d (uses 2d = v - delta u); deep and P+
conjugates 0 for mu >= 0; deep g(mu + v) saturated because mu + v - delta u >= 2u; optimal multiplier >= 0 because the value function
is convex, 0 at load 0 and >= 0; nu* >= v because load(v) = c < 1 + c.  (I-): conjugates for mu >= v exact, lower bounds for mu < v;
maximiser of the right side at nu* >= 0 when c <= 1.  (I-b): KKT check of x = x^f(v) - x^f(w) on band and deep carriers
(all three depth cases), zero on P+ (mu' <= v) and on P- above the band; total load (C(V) - C(W))/tau; integration of dP/ds = v - w
by parts.  Consistency at c = 1 (both give E(V)/tau^2) checked.
Numerics (referee solver): at V = W_c and V = 1.3 W_c and tau/C(V) in {0.05, 0.4, 0.9, 1.5, 7.3, 60}, the solver values of
P'(tau, +) and P'(tau, -) agree with (I+), (I-), (I-b) to 12 digits (check_ec.py output, e.g. V = W_c, tau = 0.4 C: 0.504132230774 /
0.627840910654 both ways).

## 2.5 Corollary EC2.  CORRECT (PROVED, model), with the hypotheses (W-a) and "mirror" for strictness.
Re-derived: at V = W_c, kappa = 2p, psi = p, 4sp = 1: (I+) <= s(1 + 2pv)^2 - v(1 + 2pv) + pv^2 = s; (I-) <= s(1 - 2pv)^2 + v(1 - 2pv) + pv^2
= s; (I-b) reduces to C(W)^2 - 4p(W C(W) - E(W)) >= 0, i.e. kappa^2 - 4p(kappa - psi) >= (kappa - 2 psi)^2 >= 0.  Strictness away from
W_c in the mirror case: far-field expansion s + v(2 kappa s - 1) + v^2(kappa^2 s - kappa + psi) on the side chosen by the sign of
2 kappa s - 1; at 2 kappa s = 1 the quadratic coefficient is psi(V) - p.  So in the mirror case R(V) >= 1 for EVERY one-type shift,
with equality iff psi(V) = min psi.
Numerics (referee solver, sup over tau in [2^-14 V, 2^14 V], 96 points per octave, both sides): R(W_c) = 1.00000003 (residual =
argmin precision 2e-9 times kink slope plus grid sup of P_f); R(1.01 W_c) = 1.0056, R(0.99 W_c) = 1.0115, R(1.1 W_c) = 1.073,
R(0.9 W_c) = 1.222.  The kink is steep and asymmetric (about 0.56 and 1.15 per per cent of misplacement), which explains why
grid placements produced the spurious "discreteness excesses" (correction C10 confirmed).
Precision (EC2-a): EC2 is an upper bound for f' at every scale; the claim "R = 1 exactly" (rather than <= 1) uses the far field
(tau -> infinity at argmax phases), fine.

## 2.6 Restoration depth.  Upgraded: PROVED (model) for lattices with Lambda(x) := sum_{lam_k < x} lam_k <= K_1 x (both types).
Claim: if every carrier with lam < V 2^-L is dead, then R <= 1 + K 2^-L.
Proof (referee).  Side +: dead carriers lie in deep(V) (L >= log2(2 + delta_max)) or are P+ carriers; on side + both kinds have box
[-u, 0] and conjugate 0 for mu >= 0, so (I+) holds unchanged and side + <= s.  Side -: let x* be the optimal allocation of the
alive configuration (load 1), l(tau) := sum over dead carriers of x*_k >= 0.  (a) For tau <= C(V) - C((2 + delta_max) V 2^-L) the
(I-b) allocation uses only carriers with lam > W/(2 + delta) >= V 2^-L, so l = 0 and nothing changes.  (b) Otherwise tau >= C(V)/2
(L large), and l <= Lambda(V 2^-L)/tau <= 2 K_1 2^-L/kappa(V).  By convexity of the value function in the load, P_dead(tau; 1) <=
P_dead(tau; 1 - l) + l mu_dead(tau; 1) <= P_alive(tau; 1) + l mu_dead(tau; 1) (x* restricted to the alive carriers is feasible at load
1 - l).  mu_dead(tau; 1) is bounded on tau >= C(V)/2 (compactness on bounded ranges; as tau -> infinity it tends to f's side -
multiplier, bounded for self-similar lattices).  Hence side - <= s + K_0 K_1 2^-L/kappa(V).  QED
The constants 0.9-2.5 of P3's numerics are consistent with this (non-sharp) bound.  Status in the table: SKETCH -> PROVED (model).

## 2.7 Weighted lattices (W'-a continued).  PROVED (model).
With per-carrier weights w_k > 0 (v-coefficient c_k, normalisation n_k, w_k = (c_k/n_k)^2, shift-depth Lambda_k = lam_k n_k/c_k),
each carrier's problem in v-units is w_k times the unweighted one in the variable z_k = y_k/w_k (cost w_k(delta U z + z^2), box
z in [0, U], load sum w_k z_k; the 1-D minimiser at multiplier mu is the unweighted clip((mu - delta U)/2, 0, U)), and all of Lemma L, Lemma A,
Proposition W, Theorem EC1, Corollary EC2 and 2.6 hold with C = sum w_k c_k, E = sum w_k e_k.  P3's remark (3) (multiplicities)
is the integer case.  This matters because in cancellation designs n_k = q*(v + E_k + c'_k psi_g + ...) varies by O(1).

# P3 referee, part 3: Section 4 (value calculus, Lemma G, Lemma GB, Lemma BAL, cancellation cells) and Section 3 (test (b))

## 3.1 Value calculus 4.1.  CORRECT.
n_k u_k(x') - n_k u_k(zhat) = V + E_k(eta) + c'_k Delta_g with c'_k = (rho_k theta lambda_k n_k - E_k(zhat))/F_g re-derived from the
near-threshold condition; C-B1 consequence s_k = V + E_k(eta + zhat|near) + o(1) for destroyed groups re-derived.
Remark (new, harmless): if E_k(zhat) = 0 on a group, "destruction" (Delta_g = -F_g) sends every carrier of the group to
rho' = (V + E_k(eta))/(theta lambda_k n_k), i.e. it CONVERTS the group instead of destroying it; adversarial designs therefore need
E_k(zhat) != 0, which is exactly the e_spread > 0 hypothesis of Lemma G.

## 3.2 Lemma G.  CORRECT (PROVED, value calculus) under its stated hypotheses (e_spread > 0, depth condition).
Re-derived the bound |Delta/F| <= eps_i and the two averaged inequalities V >= theta sum w lambda n (delta - eps(1 + delta)),
V <= -theta sum w' lambda n (delta - eps(1 + delta)).  Scope precision (G-a): Lemma G forbids converting a balanced P- set AND a
balanced P+ set of one group.  It does NOT forbid "crossed" class conversion: error class A (+e) shifted up, class B (-e) shifted
down; then {converted P- of A, converted P+ of B} is a balanced set of two-sided carriers usable on BOTH sides.  This lever is
outside the families tested by P3 (see 3.5).

## 3.3 Lemma GB.  CORRECT (value calculus) for d = 1; for general d the stated count needs a precise argument (fixable).
d = 1: classes P-,+-(g) with errors -+F e convert under Delta_g = +-s; the two balanced sets are as stated.  General d: the error
vectors e_g (normalised e_g(zhat) = 1) lie in a (d - 1)-dimensional affine hyperplane; Radon's theorem gives, among any d + 1 of them,
a partition G_+ u G_- with intersecting convex hulls, which is exactly a balanced P- conversion (signs of Delta_g by the partition).
The P+ classes of the same groups convert with the SAME partition, so independent choices need disjoint group sets: 2(d + 1)
groups suffice (each set's other-type conversions are simply not used).  With this wording: PROVED.

## 3.4 Lemma BAL.  The implication is CORRECT (PROVED); the parenthetical claim that (Bal) is "the defining property of cancellation
staircases" is FALSE.
Proof check: f's allocation at a multiplier is a positive multiple of an optimal allocation (homogeneity), hence balanced under
(Bal); f''s optimal allocations are differences/sums of such allocations (EC1 proof); so balanced.  Fine.
Why (Bal) is not automatic.  In a cancellation design the balance of f's allocations is ENFORCED by the first-order cost of near
errors (We |E|/tau, We -> infinity in the deep-junction limit; near free coordinates cannot be banked, N2 Lemma 3.3).  The separable
optimum is balanced only for symmetric layouts (each balanced set consists of carriers with identical depth/margin data, as in P3's
"4 classes per depth").  In Martin's norm every carrier has its own depth lambda_k = m 2^{-m-k} q*(T e_k); cancelling partners at
different depths are the generic case.  Then the exact model is
   P_f(tau, s) = min { sum_c P_c(tau, s; S_c) : S_c >= 0 (class loads), sum_c S_c = 1, sum_c S_c e^(c) = 0 },
which for two classes (errors +e, -e) is P_A(tau; 1/2) + P_B(tau; 1/2), and the same holds at f' (no EC).

## 3.5 NEW: the asymmetric cancellation cell (referee computation; NUMERICAL, model level, exact identities).
Layout: two error classes A (+e) and B (-e); each class has P- and mirror P+ carriers, one per `step' octaves, margin delta; class B
is class A dilated by 2^phi.  Exact balance at f and at f' (no EC).  By EC1 applied per class at load 1/2 (and its mirror for downward
shifts), every profile is an explicit function of the lattice functions; evaluator ec_vec.py/ec_vec2.py validated against the
brute-force solver (|difference| <= 6e-8 for step 1, <= 6e-6 for step 2-3).  Results (R = sup P_f'/sup P_f, min over the lever):
 | layout | sup P_f | pure V-shift (P3's mechanism) | class shifts V_A, V_B > 0 (window lever e(eta) or group scalars) |
 | step 1, delta 1, phi 0 (symmetric) | 7/22 | 1.00004 (grid; = 1 at W_c) | 1.0000000 (V_A = V_B = 7/6) |
 | step 1, delta 1, phi 1/4 | 0.3176763 | 1.00055 | 1.0000365 |
 | step 1, delta 1, phi 1/2 | 0.3162321 | 1.0743 | 1.0001433 (V_A = 1.3817, V_B = 1.4985) |
 | step 2, delta 3, phi 1 | 1.4843750 (= 95/64) | 2278 (one class always has an empty band) | 1 (exact: 0.999999999995 at the KKT shift, part 4) |
 | step 3, delta 1, phi 3/2 | 1.0725334 | 5.237 | 1 (grid optimiser 1.0004; KKT shift 1.0001, grid-limited) |
 (The grid optimiser's small residuals 1e-5 - 4e-4 are artefacts of tabulation/placement; the exact computation at the KKT shift of
 part 4 gives 1 to 1e-11 in the two layouts checked at high precision.  Warning for future numerics: the tabulated identities lose
 all accuracy for tau << V (cancellation of terms of size (C(V)/tau)^2); use the QP solver there, as in cap_shift2.py.)
Upper bound for class-critical placement: R <= (sum_c S_c^2 sup Q_c)/sup_tau F(tau) =: M_R (misalignment ratio), which is
1.0062 (step 1), 1.074 (step 2, delta 3), 1.122 (step 3, delta 1), 1.258 (step 4, delta 1) for antiphase classes (qosc.py).
Conclusions.
 (i) The pure V-shift does NOT defeat cancellation designs whose error classes sit at different depths: R >= 1.074 for every V in
     the half-octave layout, and R is unbounded (empty bands) in sparse layouts.  P3's statement "cancellation staircases ... any
     near-error structure ... are defeated by the pure V-shift at W_c (Corollary EC2 + Lemma BAL)" is FALSE; P3's proof of "NO
     configuration has a one-sided hand-over excess bounded below uniformly in the depth" therefore has a gap for asymmetric layouts.
     The CONCLUSION (and "no EC, no cross-group partner, no two-type conversion") is nevertheless TRUE at A = 0: Theorem KKT (part 4).
 (ii) Class-dependent shifts (available through the window functional e(eta) or the group scalars, P3 4.1) remove the excess
     EXACTLY, provided the class shifts are chosen as the KKT multipliers of f's balancing problem at the critical scale (Theorem KKT,
     part 4, PROVED at model level; per-class critical placements V_c = W_c^(c) are NOT the right choice and leave an excess up to the
     misalignment ratio M_R).
 (iii) Pooled EC (Bec -> 0) also wins (pooled sup 0.3157196 < balanced sup 0.3162321), but for O(1)-relative near errors the EC
     Hilbert weight is not small in general (implant scale gap, R3-ref; E's (A5)); Theorem KKT makes EC unnecessary for near errors.
 (iv) Crossed class shifts (class A up, class B down, equal |V|) give 1.186; crossed with free |V_A|, |V_B|: 1.0061 (half-octave);
     both dominated by the KKT shift.

# P3 referee, part 4: the Bregman form of one-type conversion and the KKT class-shift theorem (referee's repair of test (a))

All statements in Model N_RN, separable part, normalisation B = 1, 2MB = 1, peak room lam/tau, no first-order base costs (A = 0),
all carriers alive (kd = 0; with L restored octaves add O(2^-L) as in part 2, 2.6).

## 4.1 The Bregman (translation) form.  PROVED (model).
For one carrier family (one error class) with P- lattice capacity C_-(V) and P+ lattice capacity C_+(V) (P3 2.5.0; weights allowed),
let Gamma be the odd-extended generalised inverse: Gamma(y) = C_-^{-1}(y) for y > 0, Gamma(y) = -C_+^{-1}(-y) for y < 0, and
A(x) := int_0^x Gamma(y) dy (convex, A(0) = 0, A >= 0).  A ONE-mode shift is parametrised by its capacity Y: Y = C_-(V) > 0 for the
P- type shifted up by V, Y = -C_+(V) < 0 for the P+ type shifted down by V; then V = |Gamma(Y)|.
 (T1) f's profile:  P_f(tau, +-; S) = A(+-S tau)/tau^2.
 (T2) shifted f':   P_f'(tau, +-; S) = D_A(Y +- S tau, Y)/tau^2,  D_A(x, Y) := A(x) - A(Y) - Gamma(Y)(x - Y)  (Bregman divergence).
Proof.  The inverse-function identity int_0^{C(W)} C^{-1} = W C(W) - E(W) (E = int C) turns Proposition W into (T1)
(P(tau; S) = S^2 Q(S tau) and Q(C(W)) = (W C(W) - E(W))/C(W)^2).  For (T2) insert the same identity into EC1: (I+) with
T := S tau + C(V) gives (S + c)^2 Q(tau(S + c)) = A(Y + S tau)/tau^2, and -v(S + c) + e = [-V(Y + S tau) + E(V)]/tau^2 with
E(V) = VY - A(Y); (I-b) is the same computation on [Y - S tau, Y] inside (0, infinity); (I-) is the case where [Y - S tau, Y]
crosses 0, where Gamma on negative arguments is the P+ lattice: int_{-u}^{Y} (V - Gamma) = V(Y + u) + A(-u) - A(Y) reproduces
(S - c)^2 Q_-(tau(S - c)) + v(S - c) + e term by term.  QED  (Numerically: identical to the brute-force QP at all tested points.)

## 4.2 Corollary EC2 in one line.  PROVED (model).
Let s := sup_{x != 0} A(x)/x^2, attained at x* (self-similar lattices).  At a maximiser A is differentiable (left and right
derivatives of A(x)/x^2 force A'_-(x*) >= 2 s x* >= A'_+(x*), and A'_- <= A'_+ by convexity), A(x*) = s x*^2, Gamma(x*) = 2 s x*,
so the parabola s x^2 is tangent to A at x* and D_A(x* + h, x*) <= s(x* + h)^2 - s x*^2 - 2 s x* h = s h^2 for every real h.
Hence the shift with capacity Y = x* (i.e. V = Gamma(x*) = W_c of P3) has P_f'(tau, +-; S) <= s S^2 = sup P_f(.; S): R = 1.
This is P3's Corollary EC2 (x* = C(W_c)), with a proof that does not need the case analysis (I+)/(I-)/(I-b), and it shows
what EC2 really is: f's profile is A(t)/t^2, f''s profile is the Bregman divergence of A at Y, and a translation is free exactly at
the tangency points of the supporting parabola.

## 4.3 THEOREM KKT (class shifts for cancellation cells).  PROVED (model).
Setting: error classes c = 1..K (carriers with the same near-error vector E^(c) in the fixed finite-dimensional space E_c), each with
its own lattices of both types (any depths, phases, margins, weights) and its function A_c as in 4.1.  At f and at f' (no EC) the
carried near error must vanish on each side: class loads S_c (real, any sign) with sum_c S_c = 1, sum_c S_c E^(c) = 0.  Put
   H(x) := min { sum_c A_c(y_c) : sum_c y_c = x, sum_c y_c E^(c) = 0 }   (convex in x, H(0) = 0),
so that P_f(tau, +-) = H(+-tau)/tau^2 and s := sup_{x != 0} H(x)/x^2 = sup P_f.  Let Z* be a maximiser of H(x)/x^2, Y = (Y_c) an
optimal allocation for H(Z*), and (V, eta) Lagrange multipliers of the two constraints at (Z*, Y) (they exist: linear constraints,
finite convex objective), so that Gamma_c(Y_c) = V + <eta, E^(c)> for every class (subgradient form) and V in dH(Z*).
Claim: the approximant f' that shifts class c by V_c := V + <eta, E^(c)> (capacity translation Y_c), i.e. the GLOBAL shift V plus
the WINDOW functional eta (value calculus 4.1: s_k = V + E_k(eta) for E_k = E^(c)), satisfies sup P_f' = sup P_f.
Proof.  For side + and any balanced y with sum y_c = tau, by (T2) per class:
   sum_c D_{A_c}(Y_c + y_c, Y_c) = sum_c A_c(Y_c + y_c) - H(Z*) - sum_c (V + <eta, E^(c)>) y_c = sum_c A_c(Y_c + y_c) - H(Z*) - V tau,
because sum_c y_c E^(c) = 0.  As y ranges over the balanced allocations of total tau (no sign constraints), Y + y ranges over ALL
balanced allocations of total Z* + tau; hence tau^2 P_f'(tau, +) = H(Z* + tau) - H(Z*) - V tau = D_H(Z* + tau, Z*).  Side - gives
D_H(Z* - tau, Z*).  H is convex with H(x) <= s x^2 and tangency at Z* (4.2 applied to H), so D_H(Z* +- tau, Z*) <= s tau^2.  QED
Remarks.  (a) For one class this is 4.2; for symmetric layouts ((Bal)) eta = 0 and the shift is P3's pure V-shift; in general the
required class shifts differ, and they are EXACTLY the dual variables of f's balancing problem at the critical scale -- so the
approximant's lever family {global shift, window functionals} is always sufficient.  (b) No EC, no cross-group partner, no two-type
conversion is used; eta = O(junction depth) = o(1).  (c) Realising eta by a window move needs the restrictions of E_c to the near
free coordinates to be linearly independent (true for the designs of N2/P3; otherwise replace E_c by its quotient).  (d) Numerics
(exact lattice functions + brute-force QP): two classes +-e, half-octave phase: R = 1.000000000025 (pure V-shift: R >= 1.0743);
sparse antiphase (one carrier per 2 octaves, delta = 3): R = 0.999999999995 (pure V-shift: R >= 2278, empty bands); three classes
+1, -1, +2 at phases 0, 1/3, 2/3 (NON-simplex, one free load parameter): KKT shifts lie in the lever family up to 7e-6 and R = 1 + 4e-5
(grid-limited).  Scripts: P3_ref_work/cap_exact.py, nonsimplex3.py, bal_vec*.py, check_bal.py.

## 4.4 Consequences for P3's claims.
 * Lemma BAL: the implication is correct, but (Bal) is NOT the defining property of cancellation staircases (it holds only for
   symmetric layouts); without (Bal) the pure V-shift fails (R >= 1.074 in the half-octave layout, unbounded in sparse layouts).
 * Test (a): P3's CONCLUSION (no model-level cell excess, no EC, no cross-group partner) is TRUE for all cancellation cells with a
   fixed finite-dimensional near-error space -- but by Theorem KKT, not by the pure V-shift + Lemma BAL, whose proof covers only
   symmetric layouts.  Verdict: correct with a fixable gap (the gap is real; the fix is 4.3).
 * The (R6-tie) residual is unchanged: 4.3 uses ONE mode per class and needs the deep region alive (kd = 0); with forced destruction
   right below every class band one is back to Proposition FO's c_1 4/a excess per class.
 * With first-order base costs A > 0 that EC does not remove at the relevant scales, ONE-mode conversion (hence also 4.3) has the
   first-order excess c_1 (ln(a/delta) - l_A) of part 1 (FO-A), and TWO-mode with kd = 1 has c_1 (2/a - l_A) > 0 once l_A < 2/a
   (error-dominated regime).  So for E's rigid design (error-dominated by definition) the model-level defeat rests on EC (R3 Thm EC
   + (HT-EC)), not on a model theorem.

# P3 referee, part 5: test (b), E's rigid design, first-order base costs, and the remaining residual

## 5.1 Test (b) (capacity route R6).  CORRECT at model level for A = 0; scope precision for A > 0.
 * "No admissible T can force a junction load above the conversion capacity" (Model N_RN, A = 0): CORRECT -- Proposition W + EC2
   (re-proved in Bregman form, part 4) give R = 1 for every lattice pair; Theorem KKT extends this to balanced multi-class cells.
 * "Two bands give a factor-2 bottom margin and a strict first-order saving": CORRECT at A = 0 (W*', FO), including kd = 1.
 * "R3-ref deficits 1.46 / 2.07 / 1.086 are artefacts": CORRECT (peak/Hilbert ratio 17 times / 8 times too small; checked in
   r3/refwork/onetype_A.py and r3/work/modelN.py).  "1.09 (coupled) = twice the ratio + placement": PLAUSIBLE and consistent (with
   cpk = 4MB the window ratio 1 + 4MB/(cpk delta) is smaller than the band ratio 1 + 2/delta, so one-type conversion is not critical);
   not re-run by the referee.
 * Precision (b-A).  P3's sentence "A > 0 favours the approximant" holds only THROUGH EC.  If a first-order base cost A lambda/tau per
   unit persists at f' at the junction scales (EC unavailable), then (FO-A, part 1, numerically confirmed by check_foa.py:
   coefficients +0.4045/+0.4055 predicted for A = 1, +0.7592/+0.7621 for A = 4 at tau/V = 128) ONE-mode conversion has a FIRST-ORDER
   EXCESS c_1(ln(a/delta) - l_A) on the converted side, l_A = ln((2MB a + A)/(2MB delta + A)), uniformly in the depth; TWO-mode
   conversion keeps a saving -c_1 l_A for kd = 0 but has the excess c_1(2/a - l_A) for kd = 1 once l_A < 2/a.  So "the R3-ref deficits
   are artefacts" is right for their A = 0 content and for A > 0 only modulo EC.
 * Real-norm status: SKETCH (P3 says so; agreed).

## 5.2 E's rigid design (A1)-(A5).  P3's label SKETCH is honest; one sub-claim needs a scope restriction.
(O4) (opposite detector coefficients) does make each group scalar a TWO-mode lever (balanced averages of P+ and P- move oppositely,
Gordan structure fails), and at A = 0 Proposition FO gives the strict first-order saving.  But (A1) makes the design ERROR-DOMINATED
(large core-error constant): at A > 0 the saving survives only for kd = 0 (-c_1 l_A); with destruction right below the band (kd = 1) the
first-order coefficient is c_1(2/a - l_A), positive in the error-dominated regime.  Hence for E's design the model-level defeat rests on
EC removing the core-error costs at f' at all scales up to tau_gen >> V (R3 Thm EC, PROVED, plus (HT-EC), OPEN), or on keeping the deep
region alive (kd = 0).  "E's rigid design is strictly favourable for the approximant" is PROVED only at A = 0 or with EC.

## 5.3 Check of Lemma B for T and of g in C(f).
P3 constructs no operator T and claims no non-density; all its statements are model-level (Model N_RN) or value calculus on design
formulas (cancellation designs of N2 Design (B), E's (A1)-(A5)).  Admissibility (Martin's Lemma B) of these designs is NOT verified
anywhere (E 7.3 already flags it); P3 does not rely on it for any PROVED claim.  The mates are model mates (load S at every scale); no
g in C(f) is exhibited.  Nothing to check beyond this; the model's status as a calculator (upper bound for f', not a lower bound for f)
is stated correctly in P3 3.2.

## 5.4 Residual after this referee report (model level and real norm)
 (R6-tie) [P3] forced destruction right below every junction band + Gordan structure: Proposition FO's excess c_1 4/a (per class) --
   OPEN, no mechanism known.
 (R6-A) [NEW, referee] persistent first-order base costs at the junction (core errors that EC cannot carry, e.g. directions escaping
   every fixed finite-dimensional space or not approximable at the required rates, E's (A5)) + Gordan structure (no two-type
   conversion at the junction): ONE-mode / KKT conversion has the first-order excess c_1(ln(a/delta) - l_A) > 0 uniformly in the depth
   (FO-A).  This is what survives of the draft Conjecture R6** clause (E): not "escaping near errors" (irrelevant by Theorem KKT) but
   escaping CORE errors.  OPEN at model level (cross-group two-type conversion, partial EC, other levers not analysed).
 (T) [P3] real-norm transfer: (i) the model's f-profile must be a LOWER bound for the true cost of the mate at f (transport of
   matched structure, R3-ref P5); (ii) fair block-to-base rebalancing so that the weighted budget of Lemma B0 is also sufficient at f'
   (r1/A quadratic rebalancing); (iii) realisability of the shifts (V, eta) and of the restored groups by NA rows with finite base
   support; (iv) control of base block and other blocks.  OPEN.
 Main question (density of NA((c_0, p), l_2^2)): OPEN.  No counterexample, no step of a negative proof; the model-level evidence
 (both tests defeated at A = 0, now for all cancellation cells) continues to favour density.

# P3 referee, part 6: derivations referred to above, and the results table

## A.1 The sum-rule formula for ONE mode (proof of the SR counter-statement, part 1, 1.7).  PROVED (model).
Mirror-free setting, any lattices, f's multipliers mu^+-(tau) at load 1 (mu = d/dS [S^2 Q(tau S)] at S = 1 = 2Q(tau) + tau Q'(tau)).
For the ONE-mode shift V, (I+) and (I-) give, with c = C(V)/tau, v = V/tau, e = E(V)/tau^2 and tau >= C(V):
   P'(+) = (1 + c)^2 Q_+(tau + C(V)) - v(1 + c) + e = Q_+(tau) + c mu^+(tau) - v + O(v^2),
   P'(-) = (1 - c)^2 Q_-(tau - C(V)) + v(1 - c) + e = Q_-(tau) - c mu^-(tau) + v + O(v^2),
(expand (1 +- c)^2 Q(tau +- C(V)) = Q +- c(2Q + tau Q') + O(c^2)), hence
   [P'(+) - P_f(+)] + [P'(-) - P_f(-)] = (C(V)/tau)(mu^+(tau) - mu^-(tau)) + O(v^2).
ONE mode has the Gordan structure (all shifts equal V), so P3's SR would require this to be >= 0 (= 0 without dead carriers).
Numerically (check_sr.py, one carrier per octave, delta = 1, V = 1e-3): P+ lattice in phase: sum = O(v^2) (1.5e-8); P+ phase 1/4
octave, tau = 3.6: dP(+) = -9.50e-6, dP(-) = -1.55e-6, sum = -1.105e-5, predicted -1.104e-5; phase 1/2, tau = 4.4: sum = -1.618e-5,
predicted -1.617e-5.  So at some scales BOTH profiles decrease at first order under the Gordan structure.  (For R this does not
matter: in the mirror case Corollary EC2 still gives R(V) >= 1 for every ONE-mode shift.)

## A.2 (FO-A): first-order changes with a persistent base cost.  PROVED (model, continuum, constant margin, tau >> V).
Each carrier pays, in addition to the block costs, A y per unit (y = lambda/tau), at f and at f' (EC not used).  f's tent:
x(y) = min(2My, (mu - c y)/(2B))_+ with c = 2MB delta + A; saturation below y_s = mu/(2MB a + A), zero above y_0 = mu/c.  Carried
amount per class (density D per ln lambda): D u ln((2MB a + A)/(2MB delta + A)) =: D u l_A (u = mu/(2B)).  Envelope theorem (room
value mu(1 - O(V/tau)) on saturated carriers, band and below inside the saturated region for tau >> V):
 ONE, side +: margins above the band drop: -(2MB V/tau) S = -c_1 l_A; band room loss + lost deep P- room: + c_1 ln(a/delta)
   (exactly as at A = 0, the room terms do not involve A): total + c_1 (ln(a/delta) - l_A) > 0  (l_A < ln(a/delta) for A > 0).
 ONE, side -: margins of P+ rise: + c_1 l_A; new band room and deep P+ peaks: - c_1 ln(a/delta): total - c_1 (ln(a/delta) - l_A) (kd 0).
 TWO, side +: - c_1 l_A + 0 (room conservation) + c_1(2/a) - c_1(2/a) (kd 0)  = - c_1 l_A;  kd 1: c_1 (2/a - l_A).
(c_1 = 2MB u D V/tau.)  Numerically (check_foa.py, check_foa2.py, 16 carriers per octave, delta = 1, tau/V = 128): ONE side +:
+0.4045 (A = 1; predicted 0.4055), +0.7592 (A = 4; 0.7621); TWO kd 1: -0.0181 (A = 1; -0.0265), +0.3323 (A = 4; +0.3302); A = 0
reproduces P3's coefficients.

## A.3 Weighted lattices.  PROVED (model).  See part 2, 2.7: with w_k = (c_k/n_k)^2 and Lambda_k = lam_k n_k/c_k every identity of
P3 2.5 holds with C = sum w_k c_k(V), E = sum w_k e_k(V); Lemma W' holds verbatim in Lambda.

## A.4 Results table (referee)
| # | P3 claim | P3 label | Referee verdict |
|---|---|---|---|
| 1 | Lemma B0 (weighted budget; peak and Hilbert costs in one excess, L_k/B = 2M delta_k) | PROVED | CORRECT (necessary direction; sufficiency = fair rebalancing, part of (T)) |
| 2 | (C1)-(C3) constants, Model N_RN | PROVED / HEURISTIC | CORRECT as stated (model accuracy HEURISTIC, as labelled) |
| 3 | Diagnosis of E's Model N / R3-ref scripts | PROVED | CORRECT (checked in the code) |
| 4 | Lemma W' (window = band) | PROVED | CORRECT; precision: in shift-depth Lambda when normalisations vary |
| 5 | Theorem W*' | PROVED | CORRECT (all integrals re-derived) |
| 6 | Proposition FO | PROVED (A = 0) | CORRECT; addition FO-A for A > 0 |
| 7 | Proposition SR | PROVED | GAP: correct only if mu^+(tau) = mu^-(tau) (continuum); general formula A.1; harmless |
| 8 | Lemma L, Lemma A | PROVED | CORRECT (add: delta bounded below; weights) |
| 9 | Proposition W | PROVED | CORRECT (add: inf psi attained) |
| 10 | Theorem EC1 | PROVED | CORRECT (every conjugate re-derived; 12-digit numerics) |
| 11 | Corollary EC2 | PROVED | CORRECT (one-line Bregman proof, part 4) |
| 12 | Restoration depth R = 1 + O(2^-L) | SKETCH | PROVED by the referee (part 2, 2.6) |
| 13 | Test (b) defeated at model level | PROVED (model) | CORRECT at A = 0; with A > 0 only via EC (FO-A) |
| 14 | Lemma G | PROVED | CORRECT (scope: balanced P- and P+ sets of one group) |
| 15 | Lemma GB | PROVED | CORRECT (general d via Radon, disjoint group sets) |
| 16 | Lemma BAL | PROVED | implication CORRECT; "(Bal) is the defining property of cancellation staircases" FALSE |
| 17 | Test (a): pure V-shift defeats every cancellation design | PROVED (model) | FALSE for asymmetric layouts (R >= 1.074 / unbounded) |
| 18 | Test (a): no configuration has a uniform excess; no EC / partner / two-type needed | PROVED (model) | TRUE at A = 0 by the referee's Theorem KKT; P3's proof incomplete |
| 19 | E's rigid design defeated (TWO mode by (O4), saving, EC) | SKETCH | label correct; "strict saving" needs A = 0, kd = 0 or EC |
| 20 | Conjecture R6** model content FALSE | FALSE (model) | FALSE at A = 0 (clauses (D), near-error (E)); a core-error version survives as (R6-A) |
| 21 | Residuals (R6-tie), (T) | OPEN | agreed; add (R6-A) |
