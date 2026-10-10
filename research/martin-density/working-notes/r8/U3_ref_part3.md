# U3-ref part 3 — Part 3 of U3: Theorem NT, Proposition NT-M, Corollary NT-R, 3.4, Lemma 3.5, Remark 3.6

Checked against: V4 Construction SA / Theorem 2.2, Lemma 1.1, Lemma 5.2, Theorem 3.5, Prop. 5.3, Lemmas 3.3, 3.6, 4.1', Prop. 4.2',
Lemmas 5.4, 5.5, Theorem 5.6 (+ V4-ref R3, R5, R10); def:SC, def:SLD (allowedness (a), (b)); V1 2.5 (c_pi), V2 Lemma 3.1, Def. 3.2.

## 1. Theorem NT, properties (b)-(e) given (a)-(c).  Verdict: CORRECT.
 (b) as V4 Theorem 2.2 Step 5.  (c) anti-owner sign with |A| < B + delta H: n val = eps(B + delta H - |A|), so z = sgn val on S_l
 (aligned, q > 0) and |w| = M nu/theta = M(1 - g_i).  (d) gap_{l_i} = M g_i < Phi_{l_{i+1}}; for Phi_{l_{i+1}} <= s <= Phi_{l_i} the carrier
 l_i enters Scr(s) with min(Phi_{l_i}, s) = s, so Scr(Upsilon s)/s >= Upsilon for all small s: (SC) fails for I_- = {1}; Q infinite: not
 (BT).  (e) I re-checked every row of V2's system (R1)-(R7) at the closed pattern for delta = 1, tau_c = lambda_c (c != l_-),
 tau_{l_-} = (1 + sum q_c lambda_c)/|q_{l_-}|: (R1) tau >= 0; (R2) only swallowing-type G-peaks, eps vs = +1; (R3) every coordinate of
 T(l) \ F is owned by a coarse carrier o; for o != l_- the owner term lambda_o eps_o u_o(j) is z_j-signed (owner rule; specials own only
 their signature sets) and dominates the later coarse terms (V4 Step 6 bounds moduli); on S_{l_-} the term tau_{l_-} v_{l_-} has
 coefficient tau_{l_-} >= 1/|q_{l_-}| >> lambda_{l_-}, so it dominates a fortiori; maximal contact: no free rows; (R4) holds exactly;
 (R5) N = 1; (R6) (L2) only: delta >= 0 is (R1) at peaks; (R7) void.  l_- is not nearly neutral at large levels (rho_{l_-} in (0, 1/2]
 fixed, b(w) -> 0), so q'_{l_-} = q_{l_-} < 0 in (R4).  c_pi: I_up = {1}, I_lo = {}, P* = the robust coarse peaks, Bf = {l_-} u
 {specials <= l}; with x = lambda on Bf the vector delta Pi + sum x eps u is the coarse part of W, z-signed where non-zero (dominance)
 and zero at coordinates owned by fine carriers (no coarse support contains them): c(1; pi) = 0.  Correct.

## 2. Theorem NT, existence (nested tuning).  Verdict: SKETCH (correct label); plausible, but the written induction is
## INCONSISTENT and must be replaced (precision P3.1; corrected induction in U3_ref_notes.md, Section 3).
(P3.1) Stage (iii) puts B_{i+1} inside {g_{i+1} in (gamma_{i+1}, 2 gamma_{i+1})}; at the next stage one needs points of B_{i+1} with
g_{i+1} < Phi_{l_{i+2}}/2, where l_{i+2} > L_{i+1} and (I4) forces sum_{l > L_{i+1}} lambda_l << gamma_{i+1} theta, hence
Phi_{l_{i+2}} << gamma_{i+1}.  Since g_{i+1} > gamma_{i+1}(1 - 1/8) on B_{i+1} (up to the later threshold perturbation), the region of stage
(iii) is EMPTY.  The phrase "gamma_i to be fixed at the next stage" does not repair this (gamma_{i+1} is used to choose B_{i+1} and L_{i+1}).
Repair: the induction must NOT confine g_{i+1} away from 0; it keeps the curve {nu_{l_{i+1}} = theta} crossing the interior of B_{i+1}, and
the final confirmation g_i in (0, Phi_{l_{i+1}}/2) is made at stage i + 1 by a Poincare-Miranda argument in a curvilinear box of size
~ Phi_{l_i} Phi_{l_{i+1}} around a transversal intersection of {g_i = Phi_{l_{i+1}}/4} and {g_{i+1} = 0} (coordinates along which only one
of psi_{r_i}, psi_{r_{i+1}} varies; theta is Lipschitz, Lemma 5.2(a), and its variation over the box is O(Phi_{l_i} Phi_{l_{i+1}}), negligible
against both sign margins).  Margins of all confirmed gaps must exceed the threshold perturbation of the not-yet-fixed carriers
(choose L_{i+1} AFTER B_{i+1}).  With this, (I1)-(I4) close.  Other points that the written sketch glosses over and the corrected induction
handles: theta is not differentiable on {nu_{l_i} = theta} (B(th) has a kink), so "transversality" must be topological (sign changes),
not via gradients of theta; the finitely many owner-sign switching curves {A_l = 0}, l <= L_{i+1}, must be avoided by B_{i+1} (generic).
A cleaner variant uses a design addition (Z0+) (below), which makes every special's target supported in F: then B_{l_i} = 0 holds
automatically and specials own only their signature sets.

## 3. Proposition NT-M.  Verdict: (i), (iii), (iv) CORRECT; (ii) correct for Omega = {k_-} (the case giving the oscillating
## mates), FALSE as stated for general Omega/Dom (precision P3.2: a dominance hypothesis or (Z0+) is needed).
(i): dominance at coordinates owned by o != l_- (|w(o)| >= M/2 > 2^{-5}); z psi < 0 on S_{l_-}.  (iii): prop:onesidedupper needs F finite
and side-admissible pairs, not (BT); fine.  (iv): exact.
(P3.2) In (ii) the proof treats only (a) coordinates owned by Omega-carriers and (b) coordinates outside Sigma(omega).  It omits the
coordinates of supp y_k \ F (k in Omega) owned by OTHER (earlier) carriers o: there v(j) = -Delta lambda_o w(o) u_o(j) + ... +
lambda_k Dom(k) y_k(j)/n_k, and the second term is not controlled by Delta (window data have |Dom| up to O(1/t) while |Delta| may be
tiny).  In U3's construction the special targets y^(r) have off-F support (q*(y^(r) - c/q*(c)) tiny, not 0), so such coordinates exist.
Fixes: (A) restrict to Omega = {k_-} (supp y* = F; this is the case of the dangerous oscillating mates, all claims hold), or to Dom with
|Dom(k)| <= K |Delta| for specials and the targets' off-F coefficients below the corresponding design threshold; or (B) add to the
design (Z0+): for the fixed triple F_0 = {p, p', p''} in Z_0 the target family contains c/q*(c) for a dense set of directions c in
R^{F_0}, each used infinitely often in every block (same status as (Z0); allowedness holds since Z_0 meets no signature set).  Under (Z0+)
specials have targets in F, every Omega-carrier touches F^c only on its own signature set, and (ii) holds for every Dom as stated.
The corrected stage (i) of the construction uses a target direction c close to (not on) the hyperplane c ⊥ Phi(b^(i)): its zero set
still crosses B_i, which is all that is needed.

## 4. Corollary NT-R.  Verdict: CORRECT for Omega = {k_-} (and under (Z0+) for every Omega), modulo V4 Theorem 5.6 and the
## (flagged) compatibility of V4's design conditions with D^{V2}; the genericity sentence for (H2) is unjustified (P3.3).
For Omega = {k_-}: (H1) as U3 says (|w| bounded below except nowhere; tau_k -> 0); E = supp y* \ F = {}; on S_{l_-} the coefficient
lambda_{l_-}(Dom(k_-) - Delta w(k_-)) has Dom(k_-) ~ |Delta| C/(Phi_{k_-}^2 |w(k_-)|), so it 32-dominates every later term
(|gamma_l| <= lambda_l |Delta|): E' = {}, (H2) vacuous.  Maximal contact (V4-ref R10) holds.  Theorem 5.6 applies.
(P3.3) For general Omega the sentence "on E itself D(j) = v(j) != 0 unless an exact cancellation occurs, which is removed by an
arbitrarily small change of Dom" needs an argument: the perturbation must keep z_j D(j) >= 0 at ALL zero coordinates of E' at once
(a Gordan-type alternative: possible iff no non-negative combination of the corresponding linear forms in Dom vanishes), and it
changes the mate.  Under (Z0+) E' = {} and the issue disappears.  Not needed for the explicit mates.

## 5. Section 3.4 (general mate of f^infty).  Verdict: SKETCH (correct label); route plausible; the description of what remains
## is inaccurate (P3.4).
The route of 3.4 is: exact data AT f^infty at every scale of a clean window (step 1), averaging, transplant to V4's (BT) companions
(fine re-alignment beyond L >> l + bank levers), Theorem E^SC.  For f^infty every carrier except l_- is aligned, so v = R^*Dom - Delta psi
is exactly z-signed off F as soon as Dom has the (R1) signs, Delta <= 0 and the targets of omega-carriers do not meet coarse target
coordinates of other owners (Z0+) — there are NO fine-origin violations at f^infty.  Hence this route needs neither Lemma QB2 nor Lemma
VT nor (S2); what it needs is (a) the window arithmetic of step (1) with the shift column (V1 Prop. TR with one extra column), (b) the
transplant of the finitely many window data of each window to V4's companions with L chosen after the window ((H1) fails for a datum
with Delta = 0 — such scales are d-neutral and go through Theorem E's d-neutral branch, or Delta is made slightly negative via Dom(k_-)),
(c) near-threshold specials as omega-carriers with inward moves (Z3 Lemma 5.1 / Y2 Lemma U'(ii)), and (d) (Z0+) or the dominance
hypothesis of P3.2.  U3's sentence "for f^infty step (S1) holds ... and only step (S2) is unwritten" conflates this route with Part 4's.
(Recommendation: state Section 3.4 as "SKETCH; remaining: (a)-(d)".)  Lemma Z at f^infty is therefore not proved, but it is in a
better position than the general (C*) row.

## 6. Lemma 3.5 (dead-zone bump).  Verdict: CORRECT after a precision (P3.5).
Re-derived: with Dom(k) = Delta w(k) (dead zone), the bumped coefficient is lambda_k eps_k kappa (1 - Phi_k^2 w(k)^2/C) (sign eps_k,
Phi_k^2 w(k)^2/C <= Phi_k |w(k)| < 1); on S_k the later terms are <= C 2^{-2s} c_k delta_k (allowedness (b)) against
kappa m 2^{-m-k_k} c_k delta_k 2^{-s}/2, which gives kappa_k = C_data 2^{m + k_k - min S_k} (super-exponentially small for D_Omega, where
min S_l = 2^l).  (P3.5) The d-change Delta_new - Delta = eps_k kappa Phi_k^2 w(k)/C changes v by -(Delta_new - Delta) psi EVERYWHERE, not
only on supp u_k; off Sigma(omega) v_new = -Delta_new psi is z-signed only if Delta_new <= 0.  For a swallowing-type k the bump RAISES
Delta, so the lemma needs Delta + kappa Phi_k^2 |w(k)|/C <= 0, or a compensating increase of Dom(k_-) (free ray), or Delta < 0 with
kappa <= |Delta| C/(Phi_k^2 |w(k)|).  The re-split must be done at all coordinates (clamp b^+ into [0, v_new]); the l_1 change of the
functional is still <= ||v_new - v||_1 <= 2 kappa lambda_k.  Note also that dead zones of a single shifted block with Delta < 0 arise only
from Dom(k) of the WRONG sign (eps_k Dom(k) < 0); after the (R1) correction of 3.4 they do not occur.

## 7. Remark 3.6 (N >= 2).  Verdict: CORRECT (as a remark).
