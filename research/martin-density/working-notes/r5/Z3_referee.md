# Referee report on Z3 (Round 5): approximate swallowing and inexact free carriers, case (O1) of Remark rem:openZ

Files reviewed: ctx/r5/Z3_notes.md (= Z3_head + Z3_part1..6 + Z3_tail, identical concatenation), scripts ctx/r5/Z3_work/*.py;
checked against paper/martin_density_note.tex (Sections 1, 7, 8). My proofs, fixes and new results: ctx/r5/Z3_ref_notes.md
(parts Z3_ref_part1..4.md); scripts in ctx/r5/Z3_ref_work/. Setting: I finite, p = p_N, SLD operator where stated.

## 0. Bottom line
The notes are careful and mostly correct. The two central new tools — Theorem E (windowed recovery through nearby first rows with
scale decoupling eps_j = o(T_lo^2)) and Lemma 3.1 (cost of a companion, with the necessary UNWEIGHTED term) — are correct; I
re-derived both line by line and stress-tested Lemma 3.1 adversarially. Theorems 5.3 and 5.4 (weakened (H2)/(H3); infinitely many bad
peaks with additive inverse margins) are correct. Proposition T (transplant) is correct as a conditional statement after five fixes
(G1-G5 below; T2-T6 in the notes); for a fixed window none changes the conclusion, and Corollary 3.4 holds with the corrected
constant K^#_*. Three statements need a missing hypothesis or a corrected formulation
(Propositions 4.1(b), 4.2; the Gamma-bound of Proposition T). One claim is FALSE: that the "band" obstruction of 4.3(ii)/7.1 is
design-independent ("every design has band carriers ... no choice of design removes it"). I prove that an explosive window-length
function makes the bands of different windows pairwise disjoint, so every first row with finite base support has infinitely many
band-free windows; for that design (O1)(i) reduces to the companion-cone (Hoffman) problem for growing finite sets of nearly exactly
swallowed carriers — the same difficulty as the open part of Theorem thm:S, i.e. (O1)(i) merges into (O2). No counterexample is
claimed by the author, and nothing I found points to one.

## 1. Verdicts (claim by claim)
| Claim | Verdict | Issues |
|---|---|---|
| Lemma 1.1 effective contact set | correct | theta < 1 needed in (b) (respected) |
| Lemma 1.2 / Cor 1.3 defect identity | correct | numerically confirmed (rel. err. 2e-12); only the defect ON supp delta is converted |
| Lemma 1.4 resonance vs d-neutrality | correct | Hoffman lower bound is |R^**zhat^#|/Re(u_l), not 1/room (Re >= r_l, target part may dominate) |
| Remark 1.5 kink | correct (bounds); (c) plausible SKETCH | first-order term carries a factor 1 + O(eta_1); statements are about upper bounds only |
| Lemma U | correct | every constant traced; uniform for j >= j_0(eps_tr) |
| Theorem E | correct | re-derived; any sub-window (T_j, n_j) is allowed |
| Lemma 3.1 cost of a companion | correct | upper bound only; adversarial numerics sup L/R <= 0.24; lower bounds in 4.3 concern the method |
| Lemma 3.2 | correct after fix | "flipped" must include all j with z_j eps_l < 0, not only z_j = -eps_l |
| Proposition T | correct with fixable gaps | T2 sign of eps_l and bad-room constant; T3 Gamma bound has additive O(theta), not O(theta t); T4 factor C_0^# on vanishing rows; T5 (BS) is not implied by small rooms (target-induced costs); T6 inverse margins of bad peaks in B' grow with B' and must enter K |
| Corollary 3.4 | correct | given Theorem E + Proposition T (fixed); improvable to top sub-windows |
| Proposition 4.1 | (a) correct; (b) missing hypothesis | add r*_l > 0 for all good l; "along every subsequence" wording wrong |
| Proposition 4.2 | correct after fix | same missing hypothesis r*_l > 0 (good l <= L) |
| 4.3 limits of the companion route | partly wrong | per-window band correct; example needs ALL l in L_N plus a design growth bound; "every design / no design removes it" FALSE (explosive windows) |
| Lemma 5.1 inward moves | correct | extension to several inward coordinates verified (numerics 2e-16) |
| Identity 5.2 / Theorem 5.3 | correct | "O(t)" should read O(K_* t) |
| Theorem 5.4 | correct | K_d <= C'K_*, enters K_pk correctly |
| 5.5 (H3) failure | (i) correct; (ii) SKETCH | genericity of the tuning shift missing (vartheta_m may move either way) |
| 6.1 peak-ification | SKETCH (as labelled) | push range should be measured by sum v(1 - sigma z); genericity missing in general |
| 6.2 | correct (near-tautological) | "distance >~ c_L log(1/c_L)" is an unproved lower bound: HEURISTIC |

## 2. Errors and gaps, with fixes (details and proofs in Z3_ref_notes.md)
**(G1) Lemma 3.2 / Proposition T: definition of flipped coordinates.** For j in S_l \ F with sgn z_j = -eps_l and |z_j| < 1,
phi_{z^#}(x) = 2|x| while phi_{z_j}(x) = (1 - |z_j|)|x| for sgn x = -eps_l, so phi_{z^#} <= 2 phi_z fails. FIX: call flipped every j in
supp delta with z_j eps_l < 0. Then phi_{z_j}(eps_l tau v_l(j)) >= tau v_l(j) for tau > 0 still holds there, and the bound
S_fl = O(K_* t) of the proof goes through.
**(G2) Proposition T, step (1).** For l in A the bad inequality is (2||v_l 1_{S_l\F}|| - r_l(eps_l))(tau_l)_- <= E_l + ...; it pins
(tau_l)_- with a good constant only if eps_l MINIMIZES r_l(eps) := sum v_l(s)(1 - eps z_s). FIX: define eps_l that way; use
r*_l := ||v_l 1_{S_l\F}||_1 for l in A in Lambda*.
**(G3) Proposition T, Gamma bound (statement false as written, harmless).** ||D Theta_+-||_2 ~ 1/t, so |H^#_m(Theta) - H_m(Theta)|
<= C t^{-2}(||D(w^# - w)|| + |C^# - C|) <= C theta and |q_0^# - q_0| h(B) <= C theta: the error is an ADDITIVE O(theta). Correct form:
Gamma^#_w <= (sqrt(1 + eta_Gamma + C theta) + C(1 + C_H^#)(K_* + theta)t)^2. Corollary 3.4 assumes theta_j -> 0, so it is unaffected.
**(G4) Proposition T, vanishing rows.** Rows "L_j(tau) = 0 on T_0 \ (F u K^#)" are violated by |L_j| <= phi(L_j)/(1 - |z_j|); the factor
C_0^# = max 1/(1 - |z_j|) over that finite set (which grows with A) must enter (HF) and the growth conditions of Corollary 3.4.
**(G4') Proposition T, hidden dependence on B'.** The peak rows are violated by |tau_l| <= t/mu_{k(l)} + lambda_l K_d t; summed over
the non-degenerate peak carriers of B' this is t sum 1/mu + K_d t, which grows with B' (Z3 tracks it correctly in Theorem 5.4 but hides
it in "C depending only on f" in Proposition T). Same for the cost-conversion constants 1/m_l. FIX: replace K_* by
K^#_* := K_* + sum_{B' nondeg. peaks} 1/mu + C_0^# in the conclusion and in the growth conditions of Corollary 3.4.
**(G5) (BS) vs small rooms; 4.3(i) "(with lambda-weighted targets ignored)" is unjustified.** c(delta) contains
min(lambda_{l''}, |y_{l''}(delta)|) for every carrier whose target meets a raised set; the only control is |delta_s| <= r_l n_l 2^s/delta_l,
so these terms can be ~sqrt(c_l r_l) >> r_l. Sufficient: max_A r_l <= theta T_lo^2 delta_min 2^{-s_max}/C (design quantities); the
status/gap parts of (BS) remain hypotheses.
**(G6) Propositions 4.1(b) and 4.2: missing hypothesis.** (W*) needs r*_l > 0 for EVERY good l; r_l > 0 does not imply it (S*_l removes
target coordinates of later bad carriers). Add it; then both proofs are correct. Also: failure of (W+-) with all r_l > 0 implies
liminf (r_l/delta°_l)^{1/l} = 0, not decay "along every subsequence".
**(G7) 4.3(ii): the band example and design-independence.**
 * "r_l = 2^{-l^4} delta°_l for infinitely many l in one block" is NOT a band example: for a sparse set (L_{i+1} >= L_i^2) the windows
   l_* in [2L_i^{4/3}, L_{i+1}) are pinnable and (W+-) holds along them. Correct version: rooms at ALL l in L_N, plus (G1') gaps of
   L_N are O(l^{1/2}) and (G2') delta°_l >= 2^{-l^2} (n^w contains Lambda°(l_*), whose factors from blocks m > N do not appear in
   Lambda^+-; if those delta° are tiny the windows outrun 2^{sum l^4}). Under (G1'), (G2') I verified the arithmetic: the example blocks
   every window of the original design.
 * "Every design has band carriers ... no choice of design removes it" (and 7.1 "defeats every window method"): FALSE — see Section 3.
**(G8) Minor.** Lemma 1.4's Hoffman gloss (1/Re, not 1/room); Remark 1.5(a) first-order term has a factor 1 + O(eta_1); Theorem 5.3
"O(t)" means O(K_* t); 6.1 push range; 6.2 lower-bound remark is HEURISTIC; 4.3(iii) re-tuning: with supp a^# = F kept (needed for
Lemma U) the vector e^# has only |F| - 1 degrees of freedom, so at most |F| - 1 d-neutral approximately resonant carriers per window
can be re-tuned without adding base coordinates (the SKETCH's "tiny masses on unused contacts" needs a version of Lemma U with
growing supports — plausible, not written).

## 3. New result: the band is a design artifact (explosive windows). PROVED (Z3_ref_notes part 4)
Replace l 2^{l^3} in (D1) by a recursively chosen F(l) with F(l+1) >= max{F(l)^2, (l+1)2^{(l+1)^3}, b(l)^{-4(l+1)}}, where
b(l) := 4^{-2n^w_l} T_hi(l)^4 delta_min(l) 2^{-s_max(l)}/l, u(l) := F(l)^{-1/(4l)}, n^w_l := ceil(F(l)Lambda°(l)),
T_hi(l) := min{T_lo(l-1), 1/(F(l)Lambda°(l))}.
 (i) Theorem thm:SLD and all of Section 8 and of Z3 survive with F(l) in place of l 2^{l^3} (the factor only absorbs f-dependent
     C_f^{l^2}).
 (ii) The bands (b(l), u(l)) are pairwise disjoint; for any numbers rho_l (l in L_N) at most |L_N cap [1,L]| windows in [1,L] are
     blocked (contain some coarse rho_l in their band); since {l : m(l) > N} is infinite, infinitely many windows are unblocked —
     for EVERY first row.
 (iii) At an unblocked window, with rho_l = r_l/delta°_l, the coarse carriers split into pinned P (rho >= u) and exactified E (rho <= b):
     K_* <= C_f^{l_*} F^{1/4} Lambda°(l_*) (given the slaving condition r*_l >= r_l/2 on P), and c(delta) + Delta <= theta T_lo^2 with
     theta -> 0. Hence f in Rec whenever, along infinitely many unblocked windows, (H1)-(H3) for E u B, status stability (BS), and (HF)
     with C^#_H <= F^{1/2} hold (Theorem E + Proposition T + Corollary 3.4).
Consequence: for this design (O1)(i) is no longer a "band" problem; it is exactly the Hoffman/companion-cone problem for growing finite
sets of nearly exactly swallowed carriers (Remark rem:S(c)), including the Lemma 1.4 obstruction (d-neutral approximately resonant
carriers make the cone at f^# degenerate). This does NOT settle (O1)(i): Hoffman constants are f-dependent and cannot be dominated by a
design function fixed before f.
Secondary improvement (PROVED): Theorem E accepts any sub-window, so Corollary 3.4 holds with the top sub-window
[2^{-n_j}T_hi(l_j), T_hi(l_j)], n_j ~ psi_j(1 + C_H)K_*, and exactification threshold theta 4^{-n_j}T_hi^2 — the form the notes' own
"tower gap" gloss requires.

## 4. What remains open after Z3 (+ this report)
 (a) (O1)(i), original design: band carriers (rooms without tower gaps, e.g. 2^{-l^4}delta°_l on all of L_N under (G1'),(G2'));
     equivalently lower semicontinuity dist(rho g, C(f^L)) -> 0 along far lowerings (Proposition 4.2, with (G6)).
 (b) (O1)(i), explosive design: (HF) with C_H <= F^{1/2}, (BS)-status, slaving (r*_l >= r_l/2, (H1)) and (H2)/(H3) for the growing sets
     E_j; in particular d-neutral approximately resonant E-carriers (Lemma 1.4: re-tuning e with only |F| - 1 degrees of freedom, or
     new base coordinates with a growing-support Lemma U).
 (c) (O1)(ii): (H3) failure with bad strict non-peaks of weight q < 0 (tuning companions, 5.5(ii): genericity of the threshold shift
     unproved); infinitely many non-d-neutral bad strict non-peaks; (H2)-failing blocks with non-d-neutral switching (exact two-piece
     data impossible; shifted, infinitely supported data needed); weak bad peaks with non-summable inverse margins ((W*_pk) fails).
 (d) SKETCHes not upgraded: Remark 1.5(c), 4.3(iii) re-tuning, 5.5(ii), 6.1 (exact degeneracy/genericity), (D*) construction.
 (e) (O2)-(O4) of Remark rem:openZ unchanged. Density of NA((c_0,p),l_2^2) remains OPEN.
