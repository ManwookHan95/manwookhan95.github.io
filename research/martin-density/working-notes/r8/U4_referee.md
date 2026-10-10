# Referee report on U4 (Round 8): consistency audit — the final operator T_final and the current master theorem

Refereed: r8/U4_notes.md (supersedes U4_part0..4.md where they differ), r8/U4_work/{tu_mu_check.py, rr_check.py} (re-run, outputs
identical), against paper/martin_density_note.tex (Sections 1, 7, 8: rem:lemmaB, def:admissible, lem:martintail, prop:smooth, lem:threshold,
lem:rigidity, def:SLD, thm:SLD, def:R0, lem:R0, lem:box, lem:pinning, lem:triangular, prop:pinned, thm:R0, thm:reductionZ) and the refereed
Rounds 5-7 (V1 1.2-4.3 with V1-ref p0-p5; V2 Theorem B, C1, Def. 2.2, Lemma 2.1 with V2-ref P1-P7 and 4b; V3 2.3, 3.1, RS with V3-ref
Sections 2-3; V4 Section 3, Lemma 3.4, 5.5 with V4-ref R6, R11; Y3 D_sigma, Theorem 3.5; Z5 referee table).
My part files: r8/U4_ref_part1..4.md; assembled proofs of all precisions: r8/U4_ref_notes.md; scripts: r8/U4_ref_work/
{tu_mu_hp.py, rr_check2.py} with outputs.

## 0. Bottom line
U4 is CORRECT in every claim it labels PROVED.  T_final is a well-founded, N-independent recursion; it satisfies the conclusion of
Martin's Lemma B (norm one, injective, dense separable operator range missing c_00, per-block density); it carries every design feature
used on the dependency trees of Master Theorem II, Master Theorem III' and Theorem RS'; and the two defects U4 found in the literal union
of the Round-7 designs are genuine and correctly fixed: C1 (V1's bank factor 8^{sigma(l)} is calibrated to the base 2^{-j}; with the
super-exponential base of V3 the bank factor mu_{sigma}^2 v(sigma) must enter Design(l), via B_mu(l) = 2^{sigma(l)}/mu_{sigma(l)}^2) and C7
((GM) at l = 1 forces c_1 < 1, contradicting norm one; impose (GM) for l >= 2).  The master theorem is a correct assembly; its residual
list is exactly the logical complement of the proved criteria.  I found eleven precisions (q1)-(q11) — one false inequality inside a
correct chain, one false side bound, two over-strong glosses, an unproved "can fail" claim that I prove, one mislabelled status flag,
weak numerics that I replace — none of which changes the definition of T_final or a statement of the master theorem.
No counterexample is claimed; nothing I checked points to one.  Lemma Z and density for p_N (every N) and for Martin's p built with
T_final remain OPEN.

## 1. Verdicts
| Claim (U4 label) | Verdict | Main point / fix |
|---|---|---|
| Definition of T_final, U_final, Lemma W (PROVED) | correct, precisions (q1), (q7) | every stage-l quantity traced to earlier data; (W1)-(W7) positive, finite; N-free; (q1) V4-ref R6 lists delta_l before y_l although the (GM) intervals depend on y_l: U4's order is the only consistent one; (q7) "sigma(l) <= s_max + 2^{l+1}" is false when s_max < 2^l (correct: max(3*2^l, s_max + 2^{l+1})), unused |
| Theorem 2.2 (admissibility; Lemma B; (P1)-(P3); V2's (2.1)) (PROVED) | correct, precision (q8) | (T-b),(T-c) via (W4) = allowedness (b); (T-d) with (a),(c) only; ||T|| = c_1 = 1; Y dense, Y ∩ c_00 = {0}; b(w) <= 2^{-64/u} < u; (q8) the chain "eta <= T_lo^4 <= 2^{-4l^3} < 1/Design" has a false middle step (Design >= 2^{6 l^3}); eta = T_lo^4/(l Design) < 1/Design <= 1/C_L directly; "l large" unnecessary |
| Theorem 2.3 (features F1-F11) (PROVED) | correct, precisions (q2), (q11) | (SF_tau) re-derived exactly from (W7) + (P2); (FD) inequality 4/5 > 1/4; (q11) "every feature used by the refereed results" must be restricted to the three trees and V4's positive results (explosive and lacunary designs are deliberately absent, as C5 says) |
| C1: defect of D_Omega + D^mu and the fix B_mu (PROVED) | correct, precision (q3) | the base enters V1/V2 only through s'^2 v' at bank coordinates s' <= sigma(l); with B_mu every inequality of V1 3.3-3.4 holds (mu^D <= Design Lam; remainder C Design^2 Lam^2; contraction needs 1/(s'^2 v'^2) <= Design^{1/3}); (q3) "can fail" was argued only as "no factor is forced to exceed 2^{2 sigma^2}"; I give an explicit admissible instance (pure fresh targets e_{s_i}^* at first scheduling) where it fails at infinitely many levels |
| C1(v): the mu-base is forced (PROVED) | computations correct; statement too strong, (q4) | base 2^{-s}: M^W(y) ~ y^{2/b}, (RR) fails for b >= 2 (re-run: 4.01, 2.01, 1.01, 0.67 -> 2/b); what is forced is SUPER-EXPONENTIAL decay (2^{-s^{3/2}} also works); "(RR) fails" = "RS does not apply", not "not recovered" |
| C7: (GM) at l = 1 (PROVED) | correct, precision (q5) | H_1 = 1/60, delta^max_1 = 1/2, c_1 <= 2^{m(1)+k(1)}/240 (= 1/60 if j(1,1) = 1); fix (GM) for l >= 2; V4 Lemma 3.4's range l > log_2(2 Theta) + 1 >= 2 needs Theta >= 1, harmless (Theta is any upper bound) |
| C2-C6, C8, C9 (PROVED) | correct | only upper bounds on c_l are imposed and only design-computed lower bounds (lambda >= 1/D(l)) are used; minimum of all c-bounds; V2's smaller b (no lower bound on b used); explosive/lacunary absent from the trees; (FD) harmless (even V2 Cor. C3.1(b) survives); RS' on sub-windows; j_0 = 1 odd |
| Lemma GW (PROVED, inspection) | correct | checked against thm:R0, Prop. TR / Theorem E'' / MT II and RS' Step 1; every window condition is monotone under enlarging Design(l); GW also absorbs per-object products C_f^{omega(l)} ((4 Design/u)^{omega} >= C_f^{omega}) |
| Hypothesis audit of MT II, MT III', RS' (PROVED) | correct | spot-checked every entry carrying a design feature; Prop. TR's N-dependence (2N D max A K_Q t/u, C(1 + N K_P)) is an f-constant for p_N |
| Re-verification: VP', MT III' logic, N-dependence (PROVED) | correct | VP' re-derived independently (annihilator = {c : u_c|_F in R a|_F} = V_0 under (ND'); Graves; lam >= 1; RT error + 2||Delta a''||_1); MT III': V1 never uses tau' <= tau_0 after Step 3, Sigma^# contains every row Steps 4-5 use; (2A_max)^{-N} >= 1 sits in the LOWER bound of nonzero minors |
| Master Theorem (i) F finite (PROVED) | correct | "equivalently (C*)" is a correct contrapositive at clean sub-windows (rho^sh, c_pi are rate objects); constant-sign maximal contact via Z4 Lemma 5.0 / V1 M-II.3 / V2-ref 5(i); sign-mixed full contact is NOT covered (V2-ref P5) |
| Master Theorem (ii) F infinite (PROVED) | correct | RS', R1, Y3 3.5, Y3 5.1, Z5 T6/T7 hold for T_final |
| Master Theorem (iii) residual list (PROVED, logical) | correct, precision (q9) | (E1)/(E2)/(E4)/(E5) are the negations of the six RS' hypotheses; the gloss "|a_s| below a power of mu_s" is HEURISTIC (roughly |a_s| <~ mu_s^{1-o(1)} U(s)) |
| Master Theorem (iv), martintail (PROVED/OPEN as labelled) | correct | T_final, U_final N-free; conditional form valid; no row-wise transfer to p |
| Status flags (PROVED) | correct, precision (q6) | no SKETCH on the critical paths; but the purely double-refereed RS is V3's statement with (ND_B) (not (ND')) and (H3'): the (ND') fix is itself single-referee |
| Numerics (evidence) | correct but weak, (q10) | tu_mu_check.py never reaches the super-exponential regime (s'^2 in [0.25, 0.7]); replaced by a 3000-bit test with the actual mu-base (below) |

## 2. Main findings (proofs in U4_ref_notes.md)
F1 (T_final is right).  I traced every quantity of stage l: (1) supports of earlier targets, S_{l'}, schedule; (2) y_l, H_l; (3) y_l,
delta_l; (4) c_{l-1}, b(l-1, M(l-1)), lambda_{l-1}, delta_{l-1}, eta_{l-1}, n_{l-1}, delta_l, g_l, y_l; (5) data of index <= l incl. c_l (through
Phi_l in D(l)); (6) Design(l), omega(l), C_L, N_L, Lip, C_*, predecessor values.  No forward reference; all divisors positive; N-free.
(T-a)-(T-d) and Lemma B's conclusion re-derived; (P1)-(P3) hold on every sub-window; V2's (2.1) holds.
F2 (C1 is real, the fix suffices).  The only numerical use of the base anywhere on the trees is the lower bound of s'^2 v_c(s') at BANK
coordinates s' = min(S_c ∩ (s_max(l), inf)) <= sigma(l) (V1 Lemma DR(ii), Lemma TU Step 2; V2 Theorem B Steps 3-4).  With mu_s = 2^{-s^2-1}:
mu_{s'}^2 v_c(s') >= (4/5) delta_min/B_mu(l) >= Design(l)^{-1/6}; the donor bank mass is <= Design Lam; Lemma B's remainder is C Design^2 Lam^2;
Lemma TU's contraction constant ~ 1/(s'^2 v'^2) <= Design^{1/3} (V1-ref p4).  Pulls, Lemma B identities, VP', V4's bank levers are base-free
or have f-dependent constants.  (q3): explicit admissible data where V1's literal 8^{sigma} fails at infinitely many levels.
F3 (C7 is real).  At l = 1, (GM) with sigma = 0 gives g_1 <= delta_1 H_1 <= 1/120 and Phi_1 <= g_1/2 forces c_1 <= 2^{m(1)+k(1)}/240.
F4 (master theorem).  A correct assembly: (i) = MT III' + cor:BTrecovered + thm:R0/Bpm/S + M-II.3; (ii) = RS', R1, Y3 3.5/5.1, Z5;
(iii) = logical complement; (iv) = thm:reductionZ + prop:reduction + lem:martintail with the N-free T_final.
F5 (numerics, new).  tu_mu_hp.py runs V1 Lemma TU at 3000 bits with the actual base and banks at j' = 8 ... 14 (mu_{j'}^2 = 2^{-130} ...
2^{-394}): for eta <= 0.1 reg (reg := min mu_{j'}^2 v'^2) 36/36 runs are exact to working precision with positive bank masses
~ eta/(mu'^2 v'), |Phi'| <= 0.09, other carriers moving by (0.01 ... 122) eta^2/reg; at eta = reg 8/12, at 10 reg 4/12, at 100 reg 0/12
converge.  The admissible tuning size scales with mu_{j'}^2 v'^2 over 270 binary orders of magnitude: exactly the quantity B_mu(l) bounds.

## 3. Attacks attempted (none broke a PROVED claim)
weak* vs norm (Theorem 2.2 density in q^*-norm; companions in p^*); uniformity in t (window conditions monotone in Design; sub-window
box bound for every t >= T_lo(w)); in the window (first sub-window of a level: u = b(l-1, M(l-1)) is not << 1/Design(l), never needed);
in the number of active carriers (patterns over subsets of [1,l]; C_f^{omega} absorbed); along companions (bank masses <= Design Lam,
tuning <= C_T eta, costs theta_w T_lo^2 with theta_w -> 0 because T_lo <= 2^{-Design^{20}}); simultaneous exactifications (banks at
distinct far coordinates, second-order cross effects ~ eta^2/reg, checked numerically); Hoffman/Lojasiewicz/minor constants (Lemma W(b);
Theorem 2.2(d); direct-sum structure in (q3)); design N-independence (Lemma W(c); Prop. TR's N is an f-constant; (2A_max)^{-N} >= 1 helps);
admissibility (Lemma B in every block, including the FD stages); well-foundedness ((GM) needs y_l first: (q1)); non-attained infima ((GM)
maximum exists: compact admissible set of positive measure; rho^sh an LP minimum); signs and one-sidedness (bank signs, pull signs, VP'
keeps sgn a on F_0); near-contacts vs contacts and c_0 vs l_infty (not touched by the audit); finite vs infinite supports (VP' needs a FINITE
F_0; RS raises live where mu is tiny); hidden assumptions on T (only (T-a)-(T-d), (P1)-(P3), allowedness (a)-(c), bounded gaps, diagonal
mu-base, V4's upper bounds; Martin's Y is defined as the range of T, which is all Steps 2-10 need); quantifier order (data (D0_final) ->
T_final -> N -> f -> levels/clean w -> companion -> g, rho -> data at each t).
Suspected problems examined and refuted: (i) a factor of Design(l) depending on c_{l+1} (none); (ii) results needing a lower bound on b(w)
or an upper bound on n(w) (none); (iii) the B_mu enlargement breaking an estimate that needs Design small (none: every condition is
"window parameter small relative to Design"); (iv) N-dependence through Prop. TR's ray-removal constants (f-constants for p_N);
(v) (FD) destroying V2 Cor. C3.1(b) (no: every scheduled index still recurs in every block).

## 4. Numerics (sanity checks only; r8/U4_ref_work/)
tu_mu_hp.py / .out: Section 2, F5.  rr_check2.py / .out: (RR) exponents for bases 2^{-s}, 2^{-s^{3/2}}, mu (q4).  U4's tu_mu_check.py and
rr_check.py re-run: identical outputs.

## 5. Single most valuable idea
In the whole refereed machinery of Rounds 5-7 the base operator enters a DESIGN constant at exactly one place: the bank factor
mu_{s'}^2 v(s') at the first far signature coordinate, which fixes the admissible size of every first-order bank move (donor raises and
exact two-sided tuning).  Calibrating Design(l) to it (B_mu(l) = 2^{sigma(l)}/mu_{sigma(l)}^2) makes the diagonal bank/pull machinery
base-agnostic, so one diagonal base with super-exponentially decaying entries serves both the exact-tuning companions (finite F) and the
raise-transfer companions (infinite F): a single N-independent admissible T_final carries all refereed results at once.  The
high-precision test confirms that the admissible tuning size is governed by exactly this factor.

## 6. What remains open after U4 (+ this report), T_final, U_final, finite I = {1..N}
F finite: the rows satisfying (C*) that are not block-tame and not in R_0 ∪ R_0^± ∪ R_S (near-exact coherent shift resonance at every
clean sub-window of all large levels; includes sign-mixed full contact); the sketched route (V2 Theorem C6) needs C*-1 exact absorption of
fine-peak residues on coarse free coordinates, C*-2 (SC) at companions in configuration (i), C*-3 exactification of theta_m, A_m, C*-4 a
shift direction constant along a window with >= 2 shifted blocks, C*-5 a joint completion/absorption fixed point.
F infinite: (E1) (RR) fails (roughly mu-thin supports); (E2) infinitely many bad carriers ((O4-box)); (E4) (ND') or (H3-inf) fails;
(E5) (W*) or (H2) fails (finite-F core at infinite F; VP' constants for growing carrier sets need log C_0(j) = o(n(w_j))); (E3) only for the
per-mate Theorem A.
Lemma Z, density of NA((c_0,p_N), l_2^2) for every N, and density of NA((c_0,p), l_2^2) for Martin's p built with T_final: OPEN.
The audit itself leaves nothing open: T_final is admissible and every proved criterion applies to it.
