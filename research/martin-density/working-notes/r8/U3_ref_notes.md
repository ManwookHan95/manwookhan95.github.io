# U3 referee notes (Round 8): verification of U3 and proofs of the fixes

Refereed: r8/U3_notes.md (= U3_head + U3_part1..5, byte-identical, checked with diff) and r8/U3_work/*.py, against
paper/martin_density_note.tex (Sections 1, 7, 8) and the refereed Round-5/6/7 results (V1, V2, V3, V4 and their referee notes).
This file = U3_ref_head + U3_ref_part1..5 (part 1: U3 Part 1; part 2: U3 Part 2; part 3: U3 Part 3; part 4: U3 Part 4 and numerics;
part 5: proofs of the fixes F1-F7).  Scripts: r8/U3_ref_work/ (nl_check2.py and vt_check.py re-run; vt_ref_check.py and
junction_check.py new).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Setting: p = p_N, N finite (mostly N = 1), F finite.

## Summary of the verification
 * CORRECT as PROVED: Lemma S, Corollaries S1, S2, Proposition S3, Theorem NL (lsc of the fibre map fails at f_SA along (BT) rows),
   Lemma D', Proposition FZ (any admissible T), Corollary FZ (for the stated aligned class), Lemma A (statement precision P2.2),
   Theorem NT properties (b)-(e) incl. rho^sh = 0 and c_pi = 0, Proposition NT-M (i), (iii), (iv), Lemma 3.5 (after the sign precision
   F3), Lemma QB2 as an inequality (accounting precisions F4), Lemma VT (single stage; confirmed numerically), Proposition RT*(a),(b),(d),
   (f) (bookkeeping F7), (S1) for one shifted block with a free-ray q < 0 carrier, Lemma R-pin.
 * SKETCH, correctly labelled but with defects: Theorem NT existence — the written induction is INCONSISTENT (the stage region is empty),
   repaired in F1; Section 3.4 (all mates of f^infty) — plausible, but what remains is not (S2) (P3.4); RT*(c), (e); (S2b).
 * Wrong or overstated: Proposition NT-M(ii) for general Omega/Dom (fails when a special omega-carrier has a wrongly signed off-F target
   coordinate and eps Dom is large; correct for Omega = {k_-} and under the design addition (Z0+), F2); Corollary NT-R's genericity
   sentence for (H2) (F2); Corollary FZ Consequence (a) for general (C*) rows (P2.1); the "(PROVED arithmetic)" scaling check of (S2a):
   K_sharp is NOT O(1) — the window masses create a first-order theta/+- junction mismatch of order s_1/t^2 (F6; numerically exact
   scaling, junction_check.py), which for super-fast ladders cannot be rebalanced with the available transfer peaks (HEURISTIC); repair by
   d-consistent engineered approximants (SKETCH).
 * Not an obstruction after all: U3's "OPEN sub-case" of (S2d) (free in-window violations with b^+ b^- > 0): the symmetric split gives (H3)
   at an l_1 cost <= the violation mass (F5).
 * No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN for every admissible T.
# U3-ref part 1 — Part 1 of U3: Lemma S, Corollaries S1, S2, Proposition S3, Theorem NL

Checked against: note def:twopiece (l. 2973), lem:rigidity (l. 294), prop:smooth(c), prop:continuity, rem:lemmaZ(c),
cor:BTrecovered, thm:onesided(c); V4 notes Construction SA / Theorem 2.2 (Steps 1-8), Proposition 3.2, Proposition 5.3
(hysteretic re-run), V4-ref (R3).  Scripts re-run: r8/U3_ref_work/nl_check2.py (copy of U3_work/nl_check2.py), output nl_check2.out.

## 1. Lemma S (sandwich of two-piece data).  Verdict: CORRECT (trivial, any admissible T, any N).
Re-derivation.  Two-piece data: g = b^+- + sum_m R_m^*(omega^+-_m - d_m(omega^+-_m) w_m), supp omega^+-_m in Q_m finite.
For j outside Sigma(omega) every R_m^* omega^+-_m vanishes at j, and R_m^*(d w_m) = d psi_m, so
g(j) = b^+-(j) - c^+-(j), c^+- := sum_m d_m(omega^+-_m) psi_m.  Side admissibility gives b^+- (j) = 0 at free j and
z_j b^+(j) >= 0 >= z_j b^-(j) at contacts.  c^+ - c^- = -sum_m Delta_m psi_m = -W_Delta (data convention).  All three items follow.
Remark: this is V2's Proposition C3 plus V4's Lemma 3.3 (D = b^+ - b^- z-signed and zero at free coordinates) read off the
omega-supports; no smallness is needed.  Fine.

## 2. Corollary S1 (one block).  Verdict: CORRECT.
Dividing the sandwich by z_j psi(j) gives: aligned contact -> pi in [-d^+, -d^-] (needs Delta = d^- - d^+ <= 0);
anti-aligned -> pi in [-d^-, -d^+] (needs Delta >= 0); free -> Delta psi(j) = 0, pi = -d^+.  The "consequently" clause needs
an aligned contact for the Delta <= 0 half; as stated.  Oscillation over aligned contacts <= |Delta|.  Checked.

## 3. Corollary S2 (F, K finite).  Verdict: CORRECT.
v = b^+ - b^- = sum_m R_m^*(omega^-_m - omega^+_m) - W_Delta = L^*((omega^- - omega^+) - (Delta_m w_m)_m) lies in Y and is supported
in F u K (finite): v = 0 by (T-c), then L^* injective (eq:Lstar) gives omega^-_m - omega^+_m = Delta_m w_m; at a peak of block m the left
side is 0 and |w_m| = M_m > 0, so Delta_m = 0.  At NA rows z' in c_0, so K is finite (prop:smooth(c)).  Correct; this is the exact
content of rem:onesided(a) for shifts.

## 4. Proposition S3 (non-constant profiles need banks or aligned maximal contact).  Verdict: CORRECT.
Re-derived: at f_n all mates have two-piece data (assumption, e.g. (BT) via thm:onesided(c)); omega-supports lie in Q_n so
Sigma(omega) is contained in Sigma_n; hypothesis (2) + Cor. S1 give Delta = 0 and pi_G constant (= -d^+) outside Sigma_n at all
coordinates with psi_n != 0, and G(s) = 0 where psi_n(s) = 0 (sandwich with c^+ = c^- = 0).  The functional
Lambda_n(h) = h(s_1) psi_n(s_2) - h(s_2) psi_n(s_1) vanishes on C(f_n) and |Lambda_n(h)| <= 2 ||psi_n||_inf ||h||_inf <= ||h||_1
(||psi_n||_inf <= sum_k lambda_k <= 1/2), so the stated l_1 bound holds (even with the better constant 1 instead of 1/2 in front of
the bracket).  psi_n -> psi in l_1 (prop:continuity).  Since p* and ||.||_1 are equivalent (||h||_1/(1 + ||L||) <= p*(h) <= q*(h)),
liminf dist > 0 holds in p* as well.  Hypothesis (1) "each s_i is free or a contact" is automatic once s_i notin F_n.

## 5. Theorem NL (lsc of the fibre map fails at f_SA along (BT) rows).  Verdict: CORRECT.
Checked step by step.
 Step 1.  In def:SLD every target y^(i) is used in every block at infinitely many carriers (the index i occurs infinitely often in
 (i_r) and y^(i) is allowed at all large l); with (Z0), y* is in the family, so carriers o_n -> infinity of block m_0 with target y*
 exist; delta_{o_n} H_{o_n} -> 0.  Since supp y* = F is assigned from the start, B_{o_n} = 0 and A_{o_n} = y*(zhat_F) =
 -(eta + delta_{l_-} H_{l_-}) (from n_{l_-} val_{l_-} = y*(zhat_F) + delta_{l_-} H_{l_-} = -eta).  Targets of carriers < o_n avoid S_{o_n}
 (allowedness (a)); o_n owns only S_{o_n}.  So z^(n) -> z coordinatewise, a^(n) = a, f_n -> f by rem:lemmaZ(c).
 Step 2.  n val^(n)_{o_n} <= -(eta + delta_{l_-}H_{l_-})/2 with z = +1 on S_{o_n}: anti-type; nu_{o_n} -> infinity relative to the
 bounded thresholds, margin >= q_0 eta/4 (|val| >= 2 eta/5).  The hysteretic re-run gives every re-run carrier n|val| >= (B + delta H)/2
 with the sign eps_l (kept: eps n val = eps A + B + dH > (B + dH)/2; flipped: >= B + dH); V4 Theorem 2.2 Step 4 survives the factor 2
 (Phi_l/Phi_k <= (5/4) delta°_l 2^{-l-10}/(1 + ||U||) <= |val_l| 2^{-l-8}/(1 + ||U||)).  ||zeta^(n) - zeta||_1 <= 2(1 + ||U||) sum_{l >= o_n}
 lambda_l -> 0, so the two non-robust carriers (first carrier, l_-) keep their statuses.  Q^(n) = {k_-}, no degenerate peak, (MS):
 (BT).  Checked.
 Step 3.  psi_n(s) for s in S_c is lambda_c w(c) v_c(s) + later terms; V4 Step 6 bounds the MODULI of the later terms
 (coefficients |w| <= 1), so the owner term dominates (|w(c)| = M >= 1/2 at peaks); S_c aligned for swallowing-type c, S_{o_n}
 anti-aligned, both outside Sigma_n = F u S_{l_-}.  Checked (target coordinates of owners are also aligned, not needed).
 Step 4.  V4 Prop. 3.2 with a coordinatewise split chi: b^+ = chi Delta_alpha lambda V 1_{F^c} + beta^+ is z-signed (chi >= 0) and
 b^- = (chi - 1)(...) + (beta^+ - Delta_alpha lambda V 1_F) is (-z)-signed off F; both in l_1 (chi bounded).  At s in S_l, l != l_-,
 u_{l_-}(s) = 0, R^* omega^+(s) = alpha lambda u_{l_-}(s) = 0, V(s) = (|val_{l_-}|/|zeta^|) psi(s), giving the exact profile formula.
 c g in C(f) for small c: from prop:onesidedupper (limsup form, gives p*(f + r g) <= 1 + (r^2/2)(kappa_w + 1) on |r| <= r_0) and
 s(t) - 1 >= min(t^2, |t|)/3; the needed smallness is c^2(kappa_w + 1) <= 2/3 and c r_0 (kappa_w + 1) <= 2/3.  Checked.
Comment on the reading.  The theorem is a genuine and useful NEGATIVE structural fact: membership in Rec cannot be propagated by
an arbitrary dense sequence of (BT) rows, and approximants for oscillating mates must be aligned or banked (Remark (b)).  It does
NOT bear on density (f_SA is (BT), hence in Rec).

## 6. Numerics (re-run, identical output)
nl_check2.py: f and f_n have P = {0,1,3}, Q = {2}; z V >= 0 off F (min 3e-7); profile (2.35e-4, 0, 1.17e-4); max_t [p*(f + t g) -
s(t)] = -5.1e-7 on the grid; gamma^+ at f_n INFEASIBLE, gamma^- = 8.6e-4; p*(f_n - f) = 8.3e-7; max oscillation over two-piece data
1.60e-2 at f versus 2.4e-8 at f_n.
Two precisions on the reading of the output (no effect on any claim):
 (n1) The grid values printed under "At f_n: p*(f_n + t c g) - s(t)" are all NEGATIVE down to |t| = 1e-3: the linear excess of c g at
     f_n (side + violation on S_o of size ~6e-7 per unit t) only beats the quadratic slack below |t| ~ 1e-6, which double-precision
     SOCPs cannot resolve.  The docstring item (2) of nl_check2.py ("> 0 for small |t|") is therefore NOT what the run shows; the
     reliable test is the infeasibility of the side-+ SOCP (item (3)), as U3 Part 5 says.
 (n2) The residual 2.4e-8 at f_n is solver tolerance, not "the difference psi_n - psi" (the script uses psi_n at f_n, where the
     theoretical value is exactly 0 by Proposition S3).
# U3-ref part 2 — Part 2 of U3: Lemma D', Proposition FZ, Corollary FZ, Lemma A

Checked against: Y1 notes (classification R/G, Lemmas 3.1-3.5, source definitions (U1)-(U3), (L1)-(L3)), V1 Lemma D, Lemma S(a),
shift patterns and c_pi (V1 2.5), V2 Lemma 3.1, Def. 3.2, Theorem C1, Master Theorem III' (V2-ref), def:SLD, (T-d), V4 Prop. 5.1.

## 1. Lemma D'.  Verdict: CORRECT (immediate).
At a clean w every coarse carrier is in class R or class G (pigeonhole).  A class-R peak is (U1) (and (L1) if rho >= 1 + u), a
class-G anti-type peak is (U2), a class-G swallowing-type peak with rho >= 1 + u is (L2).  So "no upper source" forces every coarse
peak to be class-G swallowing type (all of them, not only those with rho >= 1 + u), and "no lower source" forces every coarse peak with
rho >= 1 + u to be class-G anti-type; existence of such a peak is V1 Lemma D.  Correct.

## 2. Proposition FZ.  Verdict: CORRECT (any admissible T, any diagonal U).
Re-derived.  For diagonal U, (Ue)_j = s_j^2 a_j/nu, so zhat = Phi(a) on F and = z off F; Phi(a)_j = sigma_j(1 + s_j|b_j|) lies in the open
sigma-orthant, so <Phi(a_0), Phi(a_1)> > 0.  Two non-zero vectors that are not positively proportional are strictly separated by a
linear functional (independent: dual basis; dependent: they would be opposite, impossible here).  y(zhat(a)) = <y, Phi(a)> for y
supported in F; |u(zhat) - y(zhat)| <= q*(u - y) since q**(zhat) <= 1; (T-d) gives carriers of every block, arbitrarily far out, in
any q*-ball.  The four inequalities defining eta are strict.  Correct.
The parenthetical remark is even better than stated: Phi(a_1) = lam Phi(a_0) together with ||b(a_1)||_2 = 1 is a quadratic equation
in lam with the root lam = 1, so at most ONE a_1 != a_0 has Phi(a_1) positively proportional to Phi(a_0).

## 3. Corollary FZ.  Verdict: CORRECT for the stated class (aligned rows); Consequence (a) OVERSTATED (precision P2.1).
Proof re-derived: the flipping carriers k_i (val(a_0) >= eta/2, val(a_1) <= -eta/2) are, for large i, exactly swallowed with z = +1 on
S_{k_i} (hypothesis), hence class G (room 0) anti-type peaks at f_{a_1} with nu -> infinity (Phi_{k_i} -> 0, threshold of f_{a_1}
fixed), margin ~ q_0 eta/2: (U2) at every clean w of every level >= k_i; the non-flipping carriers give (L2).  So (SP_w) at every
clean w of large level, I_sh = {}, (R5) forces delta = 0, viol >= ||delta||_1, rho^sh >= 1 (V2-ref: "(SP_w) => rho^sh >= 1"), and
Master Theorem III' (V2-ref) gives f_{a_1} in Rec (F finite).  Correct.
(P2.1) Consequence (a) says "(C*) is NOT open in any fixed-z fibre".  What is proved is this for (C*) rows satisfying the hypothesis of
the corollary (all but finitely many carriers of EVERY block exactly swallowed with the sign of their value).  For a general (C*) row the
argument shows only that the SOURCE-DEFICIENT blocks acquire both sources at f_{a_1}: by Lemma D' every robust coarse peak of a deficient
block is class G of one type, so the flipping family turns into the other type at f_{a_1} (and a carrier whose room is robust at the
clean sub-windows of f_{a_1} is class R, a source of both kinds).  Blocks that HAVE both sources at f_{a_0} through carriers of both
types may lose one type at f_{a_1} (their flipping family can consist of anti-type carriers and their non-flipping family of
swallowing-type ones; then f_{a_1} has only (L2) from these families), so (C*) could reappear with another deficient block.  Read (a)
as "aligned (C*) rows are isolated in their fixed-z fibre (up to at most one other point)".  No other statement depends on (a).
Consequence (b) is correctly labelled (PROVED only for (BT) rows of the fibre, HEURISTIC otherwise).

## 4. Lemma A (one block: shifted exact data <=> Omega-coherence).  Verdict: CORRECT, with a precision of statement (P2.2).
Necessity = Lemma S.  Sufficiency re-derived: d is linear, d(e_k) = Phi_k^2 w(k)/C, so d(gamma) = Delta is solvable on Omega iff some
k in Omega has w(k) != 0; with v := R^*gamma - Delta psi, b^+ := chi v 1_K + beta, b^- := b^+ - v, side admissibility at a contact j holds
for EVERY chi_j in [0,1] iff z_j v_j >= 0 (chi_j = 0 or 1 included), and at a free j off F iff v_j = 0.  Both pairs represent
h = b^+ + R^*(omega^+ - d(omega^+) w) (direct computation).  Correct.
(P2.2) The hypothesis "omega-differences chosen so that psi-terms on Sigma(omega) are z-signed" should read: "v = R^*gamma - Delta psi
is z-signed at the contacts and vanishes at the free coordinates of Sigma(omega) \ F".  In the Reading, "psi is z-signed at every
coordinate whose owner has w != 0" needs the owner to be NON-NEGLIGIBLE in V4's sense (|w(o)| >= 2 tau_o, V4 Lemma 4.1' /
Prop. 4.2'); for nearly neutral owners dominance can fail (these are V4's dead zones).  The Reading is informal and not used later.
The multi-block remark (coordinates owned by carriers of UNSHIFTED blocks are dead zones for the shifted blocks) is correct and is the
structural core of the multi-block part of (S1).
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
# U3-ref part 4 — Part 4 of U3: Lemma QB2, Lemma VT, Proposition RT*, (S1), (S2), Lemma R-pin; numerics

Checked against: note lem:bookkeeping, lem:base, prop:rebalancing, lem:TV, lem:transferdata, lem:persistence, lem:assembly,
def:engineered, lem:approxfacts (E1)-(E5), lem:F1, lem:anchor, def:SC, lem:scrambling, thm:engineered (full proof, Steps 0-6),
lem:twosided, lem:budget, lem:suplevel; V2 Cor. C1.1(a), Lemma 3.1, Def. 3.2; Z3 Lemma 3.1 (companion cost); def:SLD, (P2).
Scripts: U3_ref_work/vt_check.py (re-run, identical), U3_ref_work/vt_ref_check.py (new, independent check of Lemma VT).

## 1. Lemma QB2 (quadratic bank repair).  Verdict: the displayed inequality is CORRECT (trivial); the accounting that makes it
## useful needs four precisions (P4.1)-(P4.4); with them the "quadratic law" stands.
Re-derived: at j in E, z_j = sgn a^b_j, the summand of Exc^b is 2(x - |a^b_j|)_+ with x := -sgn(a^b_j) t B_j, and
2(x - m)_+ <= x^2/(2m) since x^2/(2m) - 2(x - m) = (x - 2m)^2/(2m).  E ⊂ F^b, so b on E is unconstrained.  Correct.
(P4.1) Positive parts.  The sharp bound is 2(x - m)_+ <= (x_+)^2/(2m): at a bank coordinate only the side whose datum is VIOLATED
(z_j b^+_j < 0 for side +, z_j b^-_j > 0 for side -) pays.  With U3's Gamma^E (full b_j^2 on every piece) the non-violated side would be
charged b^-_j^2/|a^b_j|, which is huge when |b^-_j| >> |e_j|; use Gamma^{E,+-} := Gamma_w(b^+-, omega^+-) + q^b_0 sum_E ((z_j b^+-_j)_-+)^2/|a^b_j|.
(P4.2) The theta piece.  In thm:engineered the theta-decomposition is used for 0 < |tau| <= s_1 with BOTH signs of tau; at a bank
coordinate (now in F^b, no window mass) it flips as soon as |tau rho b^theta_j| > |a'_j|, and pays (tau^2 rho^2/2)(b^theta_j)^2/|a'_j|.  So
Gamma_theta acquires q_0 sum_E (b^theta_j)^2/|a^b_j| as well.  Both (P4.1) and (P4.2) are harmless exactly when ALL pieces are of the
size of the violation at the bank coordinates: |b^+-_j| <= C|v_j| with |v_j| the (fine-origin) mismatch there.  For the fine-origin
violations of Proposition RT*(d) this can always be arranged (v_j = -sum_m Delta_m psi_m(j) is a sum over fine/medium carriers, and the
split b^+_j = chi_j v_j with chi_j in [0,1] gives |b^+-_j| <= |v_j|); this hypothesis must be stated.
(P4.3) Cost.  "p*(f^b - f) <= C_f sum_E m_j" should read <= C_f m log(e/m), m := sum_E m_j (Z3 Lemma 3.1: zhat moves only on E at first
order — diagonal base — and the w-change carries the Delta log(e/Delta) term when carriers touch E).  Still o(T_lo^2).
(P4.4) Uniformity.  Imposing (T_1) on F only is legitimate (the flip part on E is bounded for ALL tau by the quadratic term), but the
other (T_0)/(T_1) conditions are evaluated at f^b; they depend continuously on the masses, so uniformity in small masses holds.
Numerics (vt_check.py re-run, identical): m_min/eps^2 = 0.83, 0.79, 0.75, 0.71 (grid ratio 10^{1/8}); the trend is consistent with the
precise prediction m_min = q_0 rho^2 eps^2/(1 - rho^2 kappa_w) = 0.67 eps^2 (maximize 2 q_0 (t rho eps - m) - (t^2/2)(1 - rho^2 kappa_w) over t;
the quadratic bound is tight at the optimum); U3's 0.81 omits q_0 = 0.796 and the slack factor — a constant, not the law.

## 2. Lemma VT (violation tolerance at a single stage).  Verdict: CORRECT (PROVED) as a conditional single-stage statement;
## confirmed numerically (vt_ref_check.py).
I re-derived (*) case by case from Step 3 (Base) of the proof of thm:engineered:
 on supp a', summand = 2(-x - A)_+ <= 2 x_- with A = (1 - tau rho c)|a'_j| > 0, x = z'_j tau rho beta_j; F: no flip by (T_1); window contact
 with mass, theta: |x| <= m_j/4 <= A (lem:approxfacts(a)); +: 2 rho|tau|(z b^+)_-; -: 2 rho|tau|(z b^-)_+; window contact without mass:
 b^theta_j = 0 forces beta^theta_j = 0, the +- summands are 2 rho|tau| times the violation; free j <= N_w: (H3) or viol = 0 gives beta^theta_j = 0,
 +-: <= 2 rho|tau||b^+-_j|; contacts in (N_w, N'']: rho|tau|(z_j v_j)_- <= rho|tau| viol(j) since z v >= -(z b^+)_- - (z b^-)_+; free j > N_w:
 |v_j| <= viol(j) (also for j > N'' where z'_j = 0); contacts j > N'': (1/2) rho|tau||v_j| (the V_{>N''} term).  Free coordinates never carry
 masses.  Steps 0-2 use only the REPRESENTATIONS (Gamma_w convex without admissibility; v = sum R^*((omega^- - omega^+) - Delta d w) holds
 for any two representations), Step 3 (Blocks) only supp omega in Q, lem:approxfacts only ||b^theta||_1 and the masses; Step 5 gains
 delta tau^2/16; total (tau^2/2)(1 - 2 delta + 3 delta/4) <= (tau^2/2)(1 - delta).  Correct.  The VT statement correctly excludes Step 6.
Numerical confirmation (new script vt_ref_check.py: N = 1 model with a dead-zone contact j0 violated on side + by eps, the full engineered
approximant built from the violated data, true p* computed by SOCP, kappa_w = 0.048, delta = 0.48):
   eps = 2e-3: s_1 = 32 rho eps/delta = 0.12 -> max_tau [p*(f' + tau g') - 1 - tau^2(1-delta)/2] = -8.6e-9 (holds);  s_1 = 4 rho eps/delta
   -> -2.1e-8 (holds);  s_1 = eps/20 -> +7.8e-6, failing for tau in [5.6e-4, 1.0e-2] (the predicted linear-cost window (m_j0/(rho eps), ~4 rho eps/delta)).
   eps = 5e-4: same pattern (holds, holds, fails on [1.8e-4, 2.4e-3]).
So the threshold (VT) is real (the constant 32 is not sharp; 4 suffices here) and the failure mode below it is the linear flip cost.
Limitation (correctly stated by U3, Remark 4.2(c)): (VT) bounds s_1 from BELOW, "late" bounds it from ABOVE; for fixed violated data
(VT) fails at all late stages.  VT is useful only where eps is small compared with the late threshold of the row (= (S2c)).

## 3. Proposition RT*.  Verdicts: (a) CORRECT; (b) CORRECT (= Lemma A / Lemma S, with the Sigma(omega) clause of P2.2);
## (c) SKETCH (plausible); (d) CORRECT given (c), with a bookkeeping precision (P4.5); (e) SKETCH; (f) CORRECT arithmetic (P4.6).
(a) V2 Cor. C1.1(a): c^comb is a polyhedral function of finitely many variables (T(l), G finite), its minimum over x >= 0 is an attained
LP value, the sign sphere is compact; in case (II) c^comb_* = 0 is ATTAINED: an exact combinatorial resonance exists.  Correct.
(c) I checked the structure: on T(l) the data v^# differ from the combinatorial L by (i) class-R strict non-peaks of shifted blocks (they
must be put into Omega with net coefficient 0 — Lemma R-pin controls the size), (ii) G strict non-peaks of shifted blocks outside the
resonance (same neutralization), (iii) medium/fine contributions.  Plausible; this item is a genuine part of the reduction and is
NOT covered by (S1), (S2): the sentence "Assuming them [(S1), (S2)], every F-finite (C*) row is in Rec" must read "assuming (S1), (S2)
and RT*(c)" (P4.7).
(P4.5) |Delta| is not O(1) at window scales: Delta = d(omega^-) - d(omega^+) with |omega| up to O(1/t) (box bound), so |Delta| <= C D(l)/t and
the fine-origin mass is eps <= C D(l) sum_{c > l} lambda_c / t <= C D(l) T_lo(l)^3/t <= C D(l) T_lo(l)^2 (without (W10)).  The bank cost
eps^2/beta stays o(T_lo^2); the (VT) arithmetic of (f) survives because of (W10) (below).
(P4.6) (f) re-checked with |Delta| <= C/t: free-coordinate mass <= C T_lo(l)^{10}/T_lo(l) = C T_lo(l)^9; s_1 := T_lo(l)^8 c_l satisfies
32 rho eps/delta <= s_1 iff c_l >= C' T_lo(l), true since log(1/c_l) ~ 10 log(1/T_lo(l-1)) << log(1/T_lo(l)) ~ n^w_l; and s_1 <= T_lo(l)^3 times
the least coarse weight.  Correct.  (W10) is an upper bound on weights chosen at stage l before Design(l) and the window of level l; all
window results use weights through upper bounds ((P2)) — compatible, same status as V4's design conditions (not checked line by line
against every constant of D_Omega / D^{V2}).

## 4. (S1) for a single shifted block with a free-ray q<0 carrier.  Verdict: CORRECT (PROVED).
After Hoffman projection onto the combinatorial cone (pattern-only, design constant), the coupling residual r = delta + sum q x is
removed by moving x_k of the free-ray carrier (q_k < 0) by r/|q_k| (r > 0) or decreasing it (r < 0, if x_k >= |r|/|q_k|; otherwise set x_k = 0
and the remaining residual forces delta = O(K t), i.e. the pinned case).  |q_k| = Phi_k |w(k)|/(m C) >= Phi_k M u(w)/(m C) at a clean
sub-window (rho_k robust, not nearly neutral), so the constant is design x u^{-1}.  Correct.  Note that this also gives rho^sh = 0 exactly
at f whenever (a) and a free-ray q<0 carrier hold.  General (S1): OPEN, as labelled.

## 5. (S2a)-(S2d).  Verdicts: (S2a) SKETCH, but the "scaling check (PROVED arithmetic)" is WRONG as written (P4.8); (S2b) SKETCH
## (plausible given a corrected (S2a)); (S2c) HEURISTIC (as labelled); (S2d) SKETCH, and its "OPEN sub-case" is avoidable (P4.9).
(P4.8) K_sharp is NOT O(1) uniformly in t — the theta/+- JUNCTION MISMATCH.  K_sharp bounds |lin'_m|/(|tau| s_1); for diamond = +-,
lin'_m = tau kappa^diamond_m + r_m <V^an - w', R x'>/sigma' with kappa^diamond_m = rho (d'_m - d_m)(omega^diamond - omega^theta).  By the proof of
(E4), (d'_m - d_m)(omega) = omega(R xhat')/|R xhat'| - omega(R zhat)/|R zhat|, so |(d' - d)(omega)| <= C ||lambda omega||_1 (K_e s_1 + t(N''));
for window data ||lambda(omega^- - omega^+)||_1 is up to O(1/t) (box bound; O(1) for fixed switching) and K_e = 8 rho ||U|| ||b^theta||_1/nu =
O(1/t) (size condition t||b||_1 <= A_0).  Hence |lin'_m| ~ |tau| s_1/t^2 — the mass-induced change of the block data (first order, of size
s_1 ||b^theta||_1 ~ s_1/t) acting on switching of size 1/t.  At the junction |tau| ~ s_1 this is tau^2/t^2, a factor t^{-2} above the
quadratic terms; the theta-piece cannot be extended (its masses would grow in proportion, the ratio is scale invariant), so the
mismatch must be removed by rebalancing with inefficiency eta_1 <~ delta t^2 and Lambda <~ t^{-2} (Lemma TV(a) needs |eps_m| Lambda <= gamma/2).
Such transfer peaks need a carrier of block m at weight Phi(k_*) in the range [~|tau| s_1/t^2, ~eta_1] approximating the f-dependent
transfer target T/ell to precision ~eta_1 (lem:transferdata: the peak condition forces Phi(k_*) <~ delta_0 ~ eta_1, and Lambda = ell/lambda_{k_*}).
For super-fast ladders (D_Omega: about one weight per window level, c_{l+1} <= T_lo(l)^{10}) only O(1) carriers have weights in that range and
their targets are fixed by the design: in general NO such transfer peak exists.  So U3's scaling check ("K_sharp = O(1) because Gamma_w <= 2
bounds the quadratic terms") overlooks the first-order part of K_sharp, and (S2a) as written is NOT established.
Suggested repair (SKETCH; Section 5 of U3_ref_notes.md): D-CONSISTENT engineered approximants.  Since d'_m(omega) = d_m(omega) for every omega
supported on a set S of strict non-peaks as soon as the normalized block values agree on S ((R_m xhat')(k)/|R_m xhat'| = (R_m zhat)(k)/|R_m zhat|,
k in S), re-tune at f' the normalized values of the finitely many coarse omega-carriers exactly back to their values at the row (V1
Lemma TU: pulls and private banks at far signature coordinates, diagonal base, explicit fixed point; the levers keep f' norm attaining).
Then kappa^diamond_m = 0 for ALL pieces at once, lin'_m reduces to the anchor/Bregman part r_m g_m = |tau| O(|Delta d| (Bx + S_m)) (fine
carriers only, <= |tau| s_1 T_lo^3/t^2 after the tuning), K_sharp = O(1) is restored, fixed transfer data suffice, and the remaining
conditions of Step 0 hold for |tau| <= c_flat t (K_W, K_A, K_h, K_H = O(1/t)), as U3 computed.  Requirements: s_1 <= c delta t^3-type bounds for the
residual terms (met by (f)'s s_1 = T_lo^8 c_l), and the tuning cost (second order plus far lever masses) below the scale-decoupling budget.
(S2b): one stage late for all pieces with masses 4 rho s_1 max_i |b^theta_{i,j}|; K_e ~ 1/T_lo for every piece; with the d-consistent
tuning (one tuning serves all pieces, since it fixes d' = d on all omega supported on the tuned set) the (A^eng)/(B'') averaging is
Theorem E's; plausible.  Without the tuning, (S2b) inherits the junction problem.
(P4.9) (S2d): the pair at a violated in-window free coordinate is determined only up to adding the same number to b^+_j and b^-_j (which
changes the represented functional by that number at j).  Choosing the symmetric split b^+_j = -b^-_j = v_j/2 gives b^theta_j = 0, i.e.
(H3), and b^+_j b^-_j <= 0, at an l_1 cost |b^theta_j| (fine-origin, since exact data at the row have b^+-_j = 0 there).  So the "OPEN sub-case
b^+(j) b^-(j) > 0" is not an obstruction.

## 6. Lemma R-pin.  Verdict: CORRECT (PROVED), consequences (i) correct, (ii) plausible as labelled.
lem:suplevel(f): varsigma omega_+(k) <= (1 - d_+ t) gap/t, varsigma omega_-(k) >= -(1 + d_- t) gap/t, |d t| <= 1/2 gives
varsigma(omega_+ - omega_-)(k) <= 3 gap/t; omega_+ - omega_- = Delta Theta + Delta d w.  Exact.

## 7. Section 4.4(5) (former gaps (C*-1), (C*-2), (C*-4), (C*-5) "not a gap any more").  Verdict: SKETCH-level claims, correctly
## flagged as resting on (S2) — and on RT*(c) (P4.7).
# U3-ref part 5 — Proofs of the fixes (F1)-(F7) and of the new finding (F6)

Conventions as in U3 (data convention Delta := d(omega^-) - d(omega^+); N = 1 in F1-F3; design with (SF*), (SF_tau), (b'), (Z0),
diagonal U; "aligned" carrier: z = sgn(val) on its signature set).

## F1. Corrected nested-tuning induction for Theorem NT (existence).  SKETCH (complete outline; every step is a one-dimensional
## intermediate value argument or a finite Lipschitz estimate).  Replaces U3 3.1 stages (i)-(iii).
Ingredients.  (a) Parameter b in the open positive orthant Omega_+ of S^2; for y supported in F, y(zhat) = <y, Phi(b)>, Phi(b) = (1 + s_j b_j)_j.
(b) HYSTERETIC owner rule for non-special carriers (V4 Prop. 5.3): reference sign eps_l fixed at the stage where l is first assigned,
kept as long as eps_l A_l(b) > -(B_l + delta_l H_l)/2; then n_l|val_l| >= (B_l + delta_l H_l)/2 with sign eps_l (aligned, robust peak by
V4 Theorem 2.2 Step 4 with |val| >= delta°/2).  For D_Omega-type ladders delta_l H_l ~ 2^{-l - 2^l} decreases super-exponentially, so the
hysteresis margin of every carrier l' < l exceeds C delta_l H_l by a huge factor.  (c) theta^{(L)}(b) := threshold of the block vector of
the carriers <= L; any completion changes it by at most eta_L := L_Theta (1 + ||U||) sum_{l > L} lambda_l (V4 Lemma 5.2(a), uniform on the
compact closure of B_0, every block vector there having the first carrier as a robust peak).  (d) A design addition (Z0+): for the fixed
triple F_0 = {p, p', p''} in Z_0 the target family contains c/q*(c) for a countable dense set of directions c in R^{F_0}, each used infinitely
often in every block (same status as (Z0)).  Then a special with target c/q*(c) has B = 0 and A(b) = <c, Phi(b)>/q*(c).
Induction data at stage i >= 1: closed ball B_i, level L_i >= l_i, specials l_1 < ... < l_i, numbers eps_j > 0 (j < i), kappa_i > 0 with
 (J1) all assignments of carriers <= L_i are constant on B_i (hysteresis; specials and l_- have eps = +1);
 (J2) for j < i: g_j^{(L_i)} := 1 - nu_{l_j}/theta^{(L_i)} lies in [eps_j, Phi_{l_{j+1}}/2 - eps_j] on B_i, and 2 eta_{L_i}/theta_min < eps_j;
 (J3) n val_{l_-} in (-eta, -eta/2) with margin on B_i; 0 < -A_{l_j} < delta_{l_j} H_{l_j} on B_i (j <= i);
 (J4) G_i := g_i^{(L_i)} takes the values >= kappa_i and <= -kappa_i in int B_i, 2 eta_{L_i}/theta_min < kappa_i.
Step i -> i + 1.  Pick b^0 in int B_i with G_i(b^0) = 0 (IVT on a path between the two points of (J4)).  Pick c_{i+1} in the dense family
with <c_{i+1}, Phi(b^0)> close to 0 and tangential gradient independent of that of <c_i, Phi> at b^0; near b^0, x_1 := <c_i, Phi(b)>,
x_2 := <c_{i+1}, Phi(b)> are coordinates.  nu_{l_i} depends on x_1 only (slope ~ m/(n Phi_{l_i} q*)), nu_l for a carrier l with target
c_{i+1}/q* on x_2 only (slope ~ m/(n Phi_l q*)), theta is Lipschitz in (x_1, x_2) with an O(1) constant.  For such a carrier l > L_i (late),
the curve Gamma_l := {G_i = Phi_l/4} is a graph x_1 = phi_l(x_2) with |phi_l'| <= C Phi_{l_i}; along it, G^l := 1 - nu_l/theta equals 1 where
x_2 = -delta_l H_l q*(c_{i+1}) (val_l = 0) and is very negative a distance ~ delta_l H_l further: by the IVT there is b^# on Gamma_l with
G^l(b^#) = 0 and val_l(b^#) > 0, at distance O(delta_l H_l) from b^0 (inside int B_i for l large).  On this path only carriers in (L_i, l) can
switch; by (b) their hysteresis margins exceed the path's O(delta_l H_l) variation, so none switches.  Put l_{i+1} := l, choose
r := c Phi_{l_i} Phi_l and B_{i+1} := closed ball of radius r around b^#: G_i in [Phi_l/8, 3 Phi_l/8] on B_{i+1} (slope ~1/Phi_{l_i}, theta
variation O(r)), and G^l takes values +-kappa_{i+1}, kappa_{i+1} ~ c' Phi_{l_i}, in int B_{i+1} (slope ~1/Phi_l).  Then choose L_{i+1} >= l_{i+1}
with 2 eta_{L_{i+1}}/theta_min < min(Phi_l/16, kappa_{i+1}, eps_j (j < i)) and shrink nothing (hysteresis keeps (J1) on B_{i+1} for the new
carriers in (l, L_{i+1}] if B_{i+1} is small compared with their margins; otherwise shrink B_{i+1} around b^# keeping a crossing of G^l,
possible because the margins exceed C r).  (J1)-(J4) hold at stage i + 1 with eps_i := Phi_l/16.
Limit.  b^infty := intersection of the B_i; z := the (constant) assignments.  By (J2) and (c), every l_i has relative gap in
(0, Phi_{l_{i+1}}/2) at the final row; l_- and the robust peaks are as in V4; (a) of Theorem NT holds with "owner sign" replaced by
"aligned with n|val| >= (B + delta H)/2" (all that (b)-(e) use).  Why U3's version fails: it confines g_{i+1} to (gamma_{i+1}, 2 gamma_{i+1})
on B_{i+1}, so the next stage (which needs g_{i+1} < Phi_{l_{i+2}}/2 << gamma_{i+1}) has an empty region.

## F2. (Z0+) and Proposition NT-M(ii)'.  PROVED.
Assume (Z0+) and that every special has a target c/q*(c) supported in F (F1 produces such rows).  Then for every finite Omega in Q
containing k_-, every omega^+ supported in Omega, every Dom supported in Omega with eps_k Dom(k) >= 0 (k in Omega \ {k_-}),
Delta := d(Dom) < 0 and Dom(k_-) > Delta w(k_-), every chi : F^c -> [0,1] and every beta supported in F with (beta + chi v 1_{F^c})(zhat) = 0,
the pairs of U3 3.2(ii) are two-piece data.
Proof.  v = R^* Dom - Delta psi.  Omega-carriers (l_- and specials) have targets in F, hence touch F^c only on their own (pairwise
disjoint) signature sets.  (1) j in S_k, k in Omega: v(j) = lambda_k (Dom(k) - Delta w(k)) v_k(j) - Delta sum_{l > k} lambda_l w(l) u_l(j).  For a
special, eps_k w(k) > 0 and eps_k Dom(k) >= 0 give eps_k (Dom(k) - Delta w(k)) >= |Delta||w(k)| >= |Delta| M/2; for k_-, d(Dom) = Delta forces
Dom(k_-) >= |Delta| C/(Phi_{k_-}^2 |w(k_-)|) >> |Delta| (U3 3.2).  The later terms have moduli <= |Delta| 2^{-5} lambda_k v_k(j) (V4 Theorem 2.2
Step 6; coefficients |w| <= 1).  So z_j v(j) >= (1/4 - 2^{-5}) |Delta| lambda_k v_k(j) > 0 (z = eps_k on S_k).  (2) j notin F u union_{k in Omega} S_k:
R^* Dom(j) = 0 and v(j) = -Delta psi(j) is z_j-signed and non-zero by U3 3.2(i) (j notin S_{l_-}).  Hence v is z-signed and non-zero off F;
b^+ = chi v 1_{F^c} + beta is z-signed, b^- = (chi - 1) v 1_{F^c} + (beta - v 1_F) is (-z)-signed off F; there are no free coordinates.  Both pairs
represent g (b^+ - b^- = v = R^*(omega^- - omega^+) - Delta psi) and g(xi) = q_0 b^+(zhat) = 0.  QED
Corollary NT-R'.  Under (Z0+), every mate of f^infty with such data, kappa_w <= 1, Delta < 0, is in cl NA (V4 Theorem 5.6): (H1) as in U3;
E = union_{k in Omega} supp y_k \ F = {}; on S_k (k in Omega) the coefficient satisfies |gamma_k| >= lambda_k |Delta|/4 >= tau_k C_1 lambda_k once
tau_k <= 1/4, so V4 Lemma 4.1' gives 32-dominance there; on the finitely many remaining coordinates of E', D = v is non-zero by (1).
Without (Z0+) the statement holds for Omega = {k_-} (supp y* = F) by the same proof.

## F3. Lemma 3.5' (dead-zone bump).  PROVED.
Add the hypothesis Delta_new := Delta + eps_k kappa Phi_k^2 w(k)/C <= 0 (automatic for anti-type k, or for kappa <= |Delta| C/(Phi_k^2|w(k)|);
otherwise raise Dom(k_-) accordingly).  Then: the new coefficient of u_k is lambda_k eps_k kappa (1 - Phi_k^2 w(k)^2/C) (sign eps_k);
v_new = v + eps_k kappa lambda_k u_k - (Delta_new - Delta) psi is z-signed off F (on S_k by the allowedness-(b) estimate for kappa >= kappa_k,
elsewhere because v_new = -Delta_new psi + (unchanged Omega terms) with Delta_new <= 0); re-split by clamping b^+_new(j) := projection of
b^+(j) onto [0, v_new(j)] (z-oriented) at every j; then ||g' - g||_1 <= ||v_new - v||_1 <= kappa lambda_k + kappa Phi_k^2 |w(k)| ||psi||_1/C <= 2 kappa lambda_k.

## F4. Lemma QB2' (sharp bank accounting).  PROVED.
Let (b^+-, omega^+-) represent g at f (F finite), be side-admissible off a finite set E of contacts, and let f^b be the banked row.  In the
bounds of prop:onesidedupper / Lemma U / thm:engineered at f^b, the flip summand at j in E is at most
   (t^2/2) ((z_j b^+_j)_-)^2/|a^b_j|  (side +, t > 0),   (t^2/2) ((z_j b^-_j)_+)^2/|a^b_j|  (side -, t < 0),   (t^2/2) (b^theta_j)^2/|a^b_j|  (theta piece),
since the summand is 2(x - m)_+ with x = -sgn(a^b_j) t B_j, which vanishes for x <= 0 and is <= x_+^2/(2m).  Consequently, if at every j in E all
three pieces are bounded by the violation, max(|b^+_j|, |b^-_j|, |b^theta_j|) <= C_E e_j with e_j := (z_j b^+_j)_- + (z_j b^-_j)_+ (true for
fine-origin violations with the clamped split |b^+-_j| <= |v_j|), masses m_j := (C_E^2 q_0 epsilon/beta) e_j (epsilon := sum_E e_j) add at most
beta (1 + o(1)) to each Gamma_diamond, and p*(f^b - f) <= C_f m log(e/m), m := sum_E m_j = C_E^2 q_0 epsilon^2/beta.

## F5. (H3) by the symmetric split.  PROVED.
Given pairs representing g with v = b^+ - b^-, and a finite set J' of free coordinates in the window, put b~^+-_j := +-v_j/2 (j in J'),
b~^+- := b^+- elsewhere, and g~ := g - sum_{j in J'} b^theta_j e_j^* + c a (c chosen with g~(xi) = 0).  Then (b~^+-, omega^+-) represent g~,
b~^theta = 0 on J' (so (H3) of Lemma VT holds), b~^+_j b~^-_j <= 0 (U3's conversion criterion holds), viol~(j) = |v_j| <= |b^+_j| + |b^-_j| = viol(j),
and, since c = sum_{J'} b^theta_j zhat_j with |zhat_j| = |z_j| < 1 off F (diagonal U: e is supported in F) and ||a||_1 <= 1,
||g~ - g||_1 <= 2 sum_{J'} |b^theta_j| <= sum_{J'} viol(j) (|b^theta_j| <= (|b^+_j| + |b^-_j|)/2).  The pairs absorb c a on F (admissible there).
So the "OPEN sub-case" of U3 (S2d) is not an obstruction.

## F6. The theta/+- junction mismatch, and d-consistent engineered approximants.
(F6a) Estimate (PROVED from the proof of thm:engineered).  For diamond = +-, lin'_m = tau kappa^diamond_m + r_m <V^an_m - w'_m, R_m x'>/sigma'_m with
kappa^diamond_m = rho (d'_m - d_m)(omega^diamond_m - omega^theta_m) and, for omega vanishing on P_m u P'_m (proof of (E4)),
   (d'_m - d_m)(omega) = sum_k omega(k) [ (R_m xhat')(k)/|R_m xhat'|_m - (R^{**}_m zhat)(k)/|R^{**}_m zhat|_m ].
With the diagonal base the window masses change (R_m xhat')(k) at first order by lambda_k sum_{j in W} u_k(j) s_j^2 m_j z_j/nu'' (m_j = 4 rho s_1 |b^theta_j|),
so for window data (||b^theta||_1 ~ A_0/t, switching ||lambda(omega^- - omega^+)||_1 up to A_2/t) the bracket is of order s_1/t and
|kappa^diamond_m| ~ s_1/t^2, generically with equality up to constants.  Hence the constant K_sharp of Step 0 (which must dominate |lin'_m|/(|tau| s_1))
is of order t^{-2}, not O(1).  (Numerical check junction_check.py, N = 1 model, datum of vt_check scaled by 1/t, exact forced data of the
engineered approximant: kappa t^2/s_1 = 4.8203e-8 to five digits for t in {1, 0.3, 0.1, 0.03} and s_1 in {1e-4, 1e-5}; the small constant
reflects the model's tiny s_j^2 at the switching carrier's signature coordinates, the scaling is exact.)  At the junction |tau| = s_1 the
mismatch is ~ tau^2/t^2; enlarging the theta-regime enlarges the masses in
proportion (scale invariance), so the mismatch must be paid by rebalancing: cost iota |eps_m| with |eps_m| ~ |lin'_m|, i.e. iota <~ delta t^2, and
Lemma TV(a) needs |eps_m| Lambda <= gamma/2.  By lem:transferdata a transfer peak of inefficiency iota needs Phi(k_*) <~ iota (peak condition) and
Lambda = ell/lambda_{k_*}; at |tau| ~ s_1 one needs Phi(k_*) in [~ s_1^2/t^2, ~ delta t^2] with u_{k_*} within ~ t^2 of the f-dependent vector T/ell.
HEURISTIC consequence: for D_Omega-type ladders (one weight per window level) only O(1) carriers have weights in that range, with fixed
targets, so in general no such transfer peak exists and the bound of Lemma VT cannot hold uniformly with T_0 >= c_flat t.
Scope: F6a does NOT affect the refereed Theorem E (Z3), E^SC (V2), E'' (V1) or thm:engineered itself: they apply thm:engineered at a
FIXED row to FIXED exact data (non-uniformly; mate property at the row from Lemma U, where f' = f and there is no mismatch).  It affects
only routes that need the engineered bound uniformly in the window scale, i.e. U3's (S2) with violated data.
(F6b) Repair (SKETCH): d-consistent engineered approximants.  After placing the window masses, re-tune at f' the normalized values
(R_m xhat')(k)/|R_m xhat'|_m of the finitely many coarse omega-carriers k (all pieces of the window) exactly back to their values at the row, by
V1 Lemma TU levers (pulls and private banks at far signature coordinates of k; with the diagonal base each lever acts at first order only on
its own carrier; explicit contraction fixed point; the lever coordinates carry clamped data with one side zero and a theta-mass, so they cost
nothing at first order).  Then (d'_m - d_m)(omega) = 0 for EVERY omega supported on the tuned set, kappa^diamond_m = 0 for all pieces, lin'_m
reduces to r_m g_m = |tau| O(|Delta d_m| (Bx_m + S_m)) = |tau| O(s_1 T_lo^3/t^2 + s_1^2/t^3), K_sharp = O(1) with FIXED transfer data, and
U3's remaining scaling arithmetic (K_W, K_A, K_h, K_H = O(1/t), T_0 >= c_flat t) goes through under s_1 <= c delta t^3 (met by U3 (f):
s_1 = T_lo^8 c_l).  Not written line by line: the lever sizes against the data at lever coordinates, and the scrambled-set bound S_m <= c delta t s_1.

## F7. Bookkeeping of Proposition RT*(d),(f) with the true size of Delta.  PROVED (arithmetic).
At window scales |Delta| <= C D(l)/t (box bound |omega| <= 6/t, coarse Phi >= 1/D(l)).  Hence fine-origin mass eps <= C D(l) sum_{c>l} lambda_c/t:
<= C D(l) T_lo(l)^2 under (P2), <= C D(l) T_lo(l)^9 under (W10).  Bank cost eps^2/beta = o(T_lo^2) in both cases; (VT) with s_1 = T_lo(l)^8 c_l
needs c_l >= C' D(l) T_lo(l), true since log(1/c_l) ~ 10 log(1/T_lo(l-1)) << n^w_l <= log(1/T_lo(l)) (D(l) is fixed before n^w_l).
