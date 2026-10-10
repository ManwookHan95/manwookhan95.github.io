# Referee report on U2 (Round 8): infinite base support -- (E1)-(E5)

Refereed: r8/U2_notes.md (= U2_head + U2_part1..4 + U2_tail, identical concatenation, checked by diff) and r8/U2_work/pair_tuning_check.py
(re-run: output reproduced), against the note paper/martin_density_note.tex (def:SLD, thm:SLD, lem:twosided, lem:smallness, lem:budget,
lem:suplevel, lem:box, lem:switchbudget, lem:split, lem:peakshift, lem:flip, def:swallowed, lem:modswallow, lem:badpeaks, lem:exactswitch,
eq:hoffman, lem:windowtwopiece, lem:onesidedtransfer, lem:uniformtransfer, lem:avgfunctionals, def:SC) and the refereed Rounds 5-7:
Z5-ref (Lemma R0, R2, Theorem R1), V3 + V3-ref (Lemmas 2.1-2.3, Cor 2.4, Theorem 2.5, VP', RS', inspection items I1-I3), V1 (D_Omega, rate
scheme, Lemma S, Lemma B, Lemma DR, Lemma TU, Lemmas CO/ST/NS/RR, Prop. TR, Theorem E''), V2 (Def. 2.1-2.2, Theorem B, Def. 3.2, Theorem C1),
U4 + U4-ref (T_final, fix C1).  My part files r8/U2_ref_part1..4.md; assembled proofs r8/U2_ref_notes.md; scripts r8/U2_ref_work/
{tr_inf_joint3.py, sm_check.py}.

## Overall verdict
U2 contains one genuinely new and correct idea that settles (E1) and removes the structural part of (E2): LEMMA P.  A switching carrier
whose signature meets an UNRAISED support coordinate s of the opposite sign, deep for the data at scale t, is pinned by the mate's own
flip budget, |tau_l| <= C_q t/v_l(s) (C_q (1 + 2K*) at good-target coordinates).  Hence only coordinates beyond a depth J need raising, and
with a diagonal base whose exponent is doubly exponential (mu*_s = 2^{-2^{2^s}}) the footprint mu*_J is negligible while the pinning
constant 2^J = O(log log(1/scale)) is absorbed by the window.  I re-derived Lemma P, Theorem RS*, Lemma ND, Theorem ND', Lemma W, the
fixed points of Steps 1''/(iv), the pair/anchor tuning of Lemma TR-inf (with new 600-digit numerics) and the Sherman-Morrison structure.
Everything labelled PROVED is correct in mechanism.  Findings: one genuine gap in the constant bookkeeping of Lemma W / RS*_inf for
infinitely many bad carriers (bad-PEAK margins are an unlisted f-dependent rate, W1) -- fixable by adding 1/mu_B(l) to (W_inf); one gap in the
transport (raise depth must exceed the tuning depth d(l), G1) -- fixed; a design-statement inconsistency (B_mu* must use d(l), not sigma(l);
new rate objects must enter omega(l), s1) -- fixed; the "iff" description of the tuning residual (NDN) is FALSE (too narrow) -- corrected to
a determinantal regularity residual (G3); (E3)(c)'s transfer of (SC) along the raise is unproved (precisely located).  Two upgrades:
U2's flagged item "(R6) continuity" is RESOLVED (c_pi is exactly invariant under the raise, D1), and U2's open corner case of "RS*_inf without
(ND')" reduces to an explicit rate (and to no rate at all when the kernel signature meets F with bounded gaps) by summing Lemma P over the
kernel signature set (Fix 4.5).  No counterexample is claimed; nothing found points to one.  Density remains OPEN.

## Verdicts
| # | Claim (U2 label) | Verdict | Main point |
|---|---|---|---|
| 1 | Design SLD^star / T_final^* (PROVED) | correct for SLD^star; T_final^* statement needs fix (s1) | admissible, N-free, (P1)-(P3), recursion well founded; Step 1'' needs 2^{J(x)} = o(log(1/x)), i.e. an exponent E(J) = log_2(1/mu_J) with E(J)/2^J -> infinity (mu = 2^{-s^2-1}: no fixed point; mu = 2^{-2^s}: right side linear in n with slope >> 1, fails); the doubly exponential choice is natural; for T_final^*: B_mu*(l) must be 2^{d(l)}/(delta_min (mu*_{d(l)})^2), d(l) = sigma(l) + 2^{l+2} (TR-inf works up to d(l)), and the new rate objects (|a_s|, s <= d(l); spreads; resource determinants) must enter omega(l) |
| 2 | Lemma P (PROVED) | correct | re-derived from lem:flip + eq:DeltaB + (P1) + allowedness (a); precision: sum|r_s| <= 8t^2 needs t >= T_lo(l_*) (all uses are in the window); holds at ANY row with forced data (used in G2) |
| 3 | Theorem RS* (PROVED) | correct, precisions (r1), (r2) | thresholds, pigeonhole, Hoffman projection, empty deep set (4 cases), fixed point n_j, footprint arithmetic (C_e >= 8 C C_tau), lambda_j >= 1, J_j -> infinity all re-derived; (r1) T_B must contain the targets of ALL bad carriers (bad-peak targets were omitted from r'_s); (r2) T_0 contains the finite contact sets of B_F carriers (as in Z5) |
| 4 | Lemma ND + Theorem ND' (PROVED) | correct | exhaustive dichotomy; (H4-inf) on F \ T_B with constant max|kappa/c_k|, R0(a), R1 |
| 5 | Lemma W (PROVED) | mechanism correct; GAP W1 (fixed), precisions W2, W3 | violation of the bad-PEAK rows is <= (sum over coarse bad peaks of 1/mu_k) t, not f-constant x (1+K*) t, and bad peaks must keep their status under the raise (needs eps_e << mu_B): add 1/mu_B(l); Hoffman constant must include C_0(l_*) (~1/m_l(l_*)); B_F contact rows; t||b^+-||_1 <= 9 and A_2 = 12 confirmed |
| 6 | Theorem RS*_inf (PROVED conditional) | correct after adding 1/mu_B(l) to Xi_f (W1) | fixed point J -> K_top -> n -> P -> x -> J° exists (doubly exponential vs linear in 2^J); "t_1 >= c' gamma_B^2" is unnecessary (t_1 >= c/c_flat); VP' radius ~ C_VP^{-2} met by x_j^2; (W_inf) is satisfiable by tame infinite B |
| 7 | RS*_inf without (ND') (SKETCH) | sketch correct; upgraded to PROVED conditional on the rate 1/m^F_k(l) (Fix 4.5) | summing (P.1) over S_k ∩ F \ T_B(l_*) (proportional cushion, constant sign) pins kept kernel carriers below 3|c_k/kappa|/t; corner case = sparse F ∩ S_k beyond s_max(l); no rate if F ∩ S_k has bounded gaps |
| 8 | Lemma DR-inf (PROVED; (R6) SKETCH) | correct; (R6) upgraded to PROVED (exact invariance, D1); omission D2; gap G1 (fixed) | values move <= C mu*_J psi(J) <= C b^2 Phi_min; minors <= Lip C b^2; c_pi depends only on (F, z|_{F^c}) -> invariant; V2's rho^sh (value-dependent inf over unbounded tau) is not covered: SKETCH via bounded minimizers with robust coefficients; J must exceed d(l) or raised coordinates <= d(l) become uncontrolled (neither tiny nor robust) |
| 9 | Lemma TR-inf (PROVED) | correct, precisions T1-T3 | first-order formula and pair/anchor cancellation re-derived; NEW numerics (600 digits, 3 carriers jointly, exact to 1e-164 relative; untuned carriers move ~eta^2/(mu^2 v^2) <= Design^2 eta^2; anchor-met carriers first order ~ eta/v); (T1) e moves by eta/(mu v), not eta/v (U2's final bound stands); (T2) d(l)-design constant; (T3) first-order motion of anchor-met carriers outside L_0 is harmless because every carrier of a tiny object is in L_0 |
| 10 | (NDN) residual, "precise statement" | FALSE as an 'iff' (too narrow); corrected (G3) | thick bank coordinate + off-F pulls + tiny spreads + no anchor + tiny Sherman-Morrison denominator lacks every resource but is not in (NDN); exact residual = tiny regularity modulus of the combined first-order resource map (private, one-sided pull, single-support columns), a determinantal rate object; Sherman-Morrison determinant confirmed numerically (det(D)(1 - sum rho gamma/nu^2), 8 digits) |
| 11 | Theorem M-inf (SKETCH) | SKETCH, plausible; flagged items: (R6) resolved; Lemma ST with anchors checked; new items G1 (fixed), G2, D2, G3 | G2: V1 Prop. TR copies B_+ 1_F and uses lem:finitebase (F finite) -- must be re-run with R1's clamped base data and Lemma P at the decomposition row; at clean sub-windows (S1) of Lemma W is automatic; raise level must be 8 Bx_* (V1 box rows 12 lambda/t) |
| 12 | (E3) structure (PROVED/HEURISTIC/OPEN) | (a), (b) correct; (c) SKETCH with a precisely located gap | (SC) at f gives (SC) at f^r only on scales >= C eps_e; whether V2's construction scales stay above is the open point |
| 13 | (E4)(ii) (SKETCH) | SKETCH, correct reduction | "single unpaired support raise not admissible" re-derived (common term gamma rho_s Lam/(nu^2 lambda_c) >> b); pairs/anchors: second order <= T_lo^6 Design^4 << b |
| 14 | Numerics (evidence) | correct | pair_tuning_check.py reproduced; my tr_inf_joint3.py and sm_check.py add joint exact tuning, anchors, Sherman-Morrison, exact kernel drift sum c Delta val = -kappa nu ||e' - e||^2/2 (12 digits) |

## Main findings (proofs in U2_ref_notes.md)
F1 (Lemma P and RS* are right).  (P.1) is an exact consequence of lem:flip at the row where the decomposition lives, and (P.2) turns it into
pinning.  In RS* the pigeonhole over |B|+1 threshold intervals guarantees that kept amplitudes survive the Hoffman projection with their sign
and size, so a kept carrier can be deep neither at a raised/thick deep coordinate (cushion >= y_j v_l(j)/2) nor at a shallow one (Lemma P).
No (RR), no profile assumption.  The doubly exponential exponent is exactly what makes the fixed point n_j >= A K'(l_j, J(n_j)) solvable.
F2 (W1, the one real gap).  With infinitely many bad carriers, the rows tau_l = 0 at bad peaks are controlled only through 1/mu_k
(sigma|alpha| = lambda mu), and bad peaks must remain peaks after the raise; both are level-dependent f-rates absent from (W_inf).
F3 (G1).  The deep raise depth J must be taken above the tuning depth d(l); otherwise coordinates in [J, d(l)] carry raised moduli
4 Bx_*(s)/lambda that are neither tiny nor robust and TR-inf's case analysis does not apply.  Taking J >= d(l) + 1 costs a design factor.
F4 (G3).  The tuning residual is a regularity modulus, not (N1)&(N2)&(SM tiny).
F5 (D1, upgrade).  V1's (R6) shift costs do not depend on values at all: the raise leaves them invariant.
F6 (4.5, upgrade).  Summing Lemma P over a kernel signature set turns U2's open corner case into an explicit rate.

## Attacks attempted
weak* vs norm (raises of mass psi(J) -> 0 in l_1; f_j -> f in norm; z untouched); uniformity in t (Lemma P and lem:flip hold for every t;
the r_s bound needs t >= T_lo(l_*)); uniformity in the window (sub-window position pigeonhole: <= s_max(l)(n_j + log K_top + 2) excluded
positions); number of active carriers (B finite: f-constants; B infinite: thresholds (4H l + 3)^{l+2}, Hoffman constants with C_0(l), bad
peak margins -- W1); along companions (V3's I1-I3: budget (1 + eta')t^2/2 with eta' -> 0 on the sub-window; R2 constants persist);
simultaneous exactifications (raise + VP' on F_0 with J > max F_0; TR-inf private Jacobian, joint Newton converges numerically);
Hoffman/Farkas/minor constants (eq:hoffman normalization W2; V2's minors Lipschitz in values; rho^sh D2); design N-independence and
admissibility (base and window changes only; (T-d) untouched; recursion well founded at stage l); non-attained infima (nearest points of
closed cones; rho^sh's inf is attained on polyhedral pieces); signs and one-sidedness (kept amplitudes keep sign; pulls one-sided -> G3;
kernel drift exactly one-signed); near-contacts vs contacts (free rows on T_0 \ F with room-dependent Hoffman factor, inside H(l)); c_0 vs
l_infty (companions from forced data (a', z) with z in B_{l_infty}, rem:lemmaZ(c)); finite vs infinite peak/contact/support sets (infinite
bad peaks -> W1; infinite F in Lemma B/TU: only J ∩ supp A^0 = {} is used); hidden assumptions on T (only (P1)-(P3), allowedness (a)-(b),
bounded gaps of D_Omega for d(l)); quantifier order (design -> f -> g, rho -> levels -> sub-window position -> J -> companion ->
decompositions -> threshold pigeonhole -> data): correct.  Counterexample hunting: none of the gaps produces a non-recoverable mate; each is
a missing rate or bookkeeping item.

## Single most valuable idea
Lemma P: the mate's own flip budget pins any carrier whose switching would be deep at an unraised support coordinate of the opposite
sign (|tau_l| <= C_q t/v_l(s)); therefore cushions need to be raised only beyond a depth J, and a diagonal base with doubly exponential
exponent makes that raise free (footprint mu*_J) while the pinning constant 2^J = O(log log(1/scale)) is absorbed by any window.  This
removes (RR) (mu-thin supports), bounded switching and box domination from the infinite-support theory.

## What remains open after U2 and this report
Density of NA((c_0,p_N), l_2^2) (every N), Lemma Z, and density for Martin's p remain OPEN.  For the designed norm and infinite F:
 (i) RS-type rows (finitely many bad carriers, any profile, (W*), (H2), (H3-inf), (B_fin)): RECOVERED (PROVED; (RR) and (ND') removed).
 (ii) Infinitely many bad carriers: PROVED under (W_inf) augmented by 1/mu_B(l) (bad-peak margins) and, if (ND') fails, by the kernel rate
      1/m^F_k(l); unconditional only through the transport (iii).
 (iii) Theorem M-inf (transport of Master Theorem III' to infinite F): SKETCH; inspection items: G2 (V1's transplant at infinite F with clamped
      base data and Lemma P at the decomposition row), D2 (rho^sh under the raise), V2 Theorem B with pinned faces, joint fixed point of TR-inf;
      G1 fixed, (R6) resolved.
 (iv) Residuals specific to infinite F: the TUNING residual (tiny regularity modulus of the first-order resource map; contains U2's (NDN));
      degenerate swallowing-sign bad peaks whose donors lack resources; (SC) along the deep raise below the scale eps_e ((E3)(c)).
 (v) Shared with finite F: (C*) (near-exact coherent shift resonance; V2's gaps (C*-1)-(C*-5), in particular (C*-2) "(SC) at companions"),
      failure of (H2).
