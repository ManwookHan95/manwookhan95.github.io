# Referee report on Z4 (Round 5): infinitely many swallowed carriers (O2) and maximal contact (O3)

Refereed: r5/Z4_notes.md (= Z4_head + Z4_part1..8, checked to be identical up to blank lines), script r5/Z4_work/maxcontact_toy.py,
against the note paper/martin_density_note.tex (Sections 1, 7, 8). Referee part files: r5/Z4_ref_part1..6.md; proofs of all fixes and
additions: r5/Z4_ref_notes.md; scripts: r5/Z4_ref_work/clamp_lowering.py, r5/Z4_ref_work/didentity_toy.py.

## Overall verdict
The main theorem (Theorem A = Theorem 3.1, S_Binf) is CORRECT, with one fixable gap: the design SLD_G must be made independent of N
(fix given). Every step was re-derived (Steps 1-9, including the claim that c_flat ~ gamma_f/C_dia while t_1 does not depend on A_2,
gamma_B, and the window arithmetic). Corollaries 4.1, 4.2, Propositions 5.1, 5.6, Corollary 5.4, Lemmas 2.1, 2.3, 6.1, 8.1 are correct.
One PROOF ERROR: step (iv) of Proposition 1.2 sums a non-summable sequence (sum_k v_k = infinity); the conclusion is true and I give a
correct proof (sup-norm control from the common ratio of the coarse values). The SKETCH on degenerate swallowing-sign peaks (part 8) has
a gap (the averaged theta-data are outward on one side) and a false sub-claim (steering through free target coordinates is free); both are
repaired in ref notes Section 9. Several statements are slightly imprecise (listed below).
No counterexample is claimed, none is suggested by anything I checked. Lemma Z / density remain OPEN.

## Verdicts
| claim | Z4 label | verdict | issue / fix |
|---|---|---|---|
| Prop 1.2 (distance of far lowerings) | PROVED | correct, proof fixed | step (iv) uses sum_k v_k <= m/(2rho_0), false (v_k bounded, not summable). Fix: for coarse k, v^L_k = r v_k with one ratio r, and abs(min(M, beta x) - min(M,x)) <= abs(beta-1) M give sup_coarse abs(w^L - w) <= K_w eps_L; then sum lambda abs(w^L - w) <= (K_w + 2) eps_L. |
| Prop 1.3 (band arithmetic) | PROVED | correct | (a)-(c) fine. The sentence "hence lsc along f^L needs the same exact matching" is interpretive (HEURISTIC). Coarse block data move by O(eps_L), so coarse near-threshold status may change (harmless). |
| Lemma 2.1 (zero-cost cone) | PROVED | correct | — |
| G*(l), Lemma 2.2 | PROVED | correct with fixable gap | configurations use U ⊂ L_N ∩ [1,l], so SLD_G depends on N, but Lemma martintail needs one T for infinitely many N. Fix: let U range over all subsets of [1,l]. |
| Lemma 2.3 (d-repair) | PROVED | correct | — |
| Prop 2.4 (SLD_G survives) | PROVED | correct with fixable gap | the N-independence fix above; the clause c_l <= (delta_l norm_1(h_l))^2 cannot hold at l = 1 (c_1 = 1); impose it for l >= 2 (only large l are used). |
| Theorem A (S_Binf) | PROVED | correct with fixable gap | N-independence of the design. Improvement (PROVED): (H2') can be weakened to (H2'') (d-identity pinning; any good peak, degenerate or not, gives the upper bound). |
| Cor 4.1 (original SLD) | PROVED | correct | conditional statement; NOTE: without (DR) the Hoffman constant H^Z_f is at least mC/c_{l'} for every one-sided zero-cost carrier l' (Lemma R, PROVED), a design-scale number, so the corollary helps only if such carriers are sparse; (W_inf^orig) can also be vacuous for some choices of the S_l. |
| Cor 4.2 (thm:S contained) | PROVED | correct | (b) needs (W*) as stated. |
| Prop 5.1 / 5.6 (rigidity of d-mismatch) | PROVED | correct | constants conservative. Valuable: Delta d_m != 0 forces peak-aligned swallowing of ALL peak signature sets of block m. Strengthened (ref notes Prop 5.6', PROVED): the same holds for every carrier with w != 0 outside the finitely many used ones, i.e. q_l has sign -sign(Delta d_m) for all but finitely many non-d-neutral carriers of block m. |
| Cor 5.4 (maximal contact) | PROVED | correct with fixable gaps | (i) a factor l^2 is dropped in the growth condition; harmless (Step 8 needs much less). (ii) "for the original SLD the same holds" is not justified: Lemma 5.3 needs the clause c_l <= (delta_l norm_1(h_l))^2, which the original recursion does not imply; state it with M_f instead of M^canc. (iii) Remark 5.5(ii) ("super-weak swallowing-sign peaks are NOT covered") is design-dependent: the condition is a liminf on M^canc/Lambda°, which may hold along a subsequence even when (MS) fails. |
| Lemma 6.1 | PROVED | correct | — |
| Lemma 8.1 (degenerate-peak usage) | PROVED | correct | d-rows must include degenerate swallowing-sign peaks (q_l = Phi M/(mC)); (DR) repairs them. |
| Engineering with degenerate peaks | SKETCH | plausible, with a gap and one false sub-claim (fixed) | GAP: for abs(tau) <= s_1 Theorem thm:engineered uses the averaged data omega^theta, which at a used degenerate peak is OUTWARD for one sign of tau; "steer to a strict non-peak" is not enough, one needs gap'(k) >= 2 rho s_1 abs(omega^theta(k)), i.e. mu'_k <= -kappa_D s_1 (gap' = M'abs(mu')/(q'_0 theta_hat' Phi_k)). FALSE sub-claim: steering through target coordinates is FREE at free coordinates (exact zero-cost data vanish there), and changes of a on F are free too (Lemma 9.2 of the ref notes, PROVED). Refined sketch under a linear hypothesis (FS) in ref notes 9.3. |

## Detailed findings
1. **Prop 1.2, step (iv) (error, fixed).** The written step multiplies the clamp estimate for Phi_k|w^L(k) - w(k)| by m and sums
"v_k", using sum_k v_k <= m/(2 rho_0). But v_k = m|u_k(zhat)|/|R** zhat| does not tend to 0 (the u_k are dense in S_{q*}), so the
sum is infinite; the clamp estimate alone gives only sum_k min(2 Phi_k, C eps_L) ~ eps_L log(1/eps_L) (or L eps_L). Correct proof
(Z4_ref_notes 1): for coarse k, u_k(zhat^L) = u_k(zhat), so v^L_k = r v_k with r = |R** zhat|/|R** zhat^L| independent of k; then
w(k) = s_k min(M, C v_k/Phi_k), w^L(k) = s_k min(M^L, C^L r v_k/Phi_k), and |min(M, beta x) - min(M, x)| <= |beta - 1| M gives
|w^L(k) - w(k)| <= |M^L - M| + |C^L r/C - 1| M = O(eps_L) uniformly in k. Numerically confirmed (clamp_lowering.py).
2. **N-independence of SLD_G (gap, fixed).** See table. With U ⊂ [1,l] arbitrary, G*(l) dominates every N-version; nothing else changes.
3. **(H2') can be weakened (addition, PROVED).** By eq:didentity, Delta d_m M_m = (good part) - sum_{l in B, m(l)=m} q_l tau_l + r_m.
If q_l >= 0 for all swallowed carriers of block m, then Delta d_m M_m <= K* t/(mC) + D/C + 12t/C + 2t/sigma (because (tau_l)_- <=
|tau_l - tau°_l| on U and inactive/fine carriers contribute O(t)); symmetrically for q_l <= 0. Also every good peak (degenerate or not)
gives Delta d M <= K* t/lambda. Hence (H2''): LOWER from a non-degenerate good or swallowing-sign swallowed peak OR all q_l <= 0; UPPER from
a good peak or an anti-sign swallowed peak OR all q_l >= 0. As every block has infinitely many non-degenerate peaks of each sign
(Lemma 5.0 holds at every f), (H2'') fails only if some block has all peaks swallowing-sign swallowed and an anti-aligned swallowed strict
non-peak, or all non-degenerate peaks anti-sign swallowed and a swallowing-sign swallowed carrier with q_l > 0.
4. **One-sided d-resources (E-d) made precise (addition).** Lemma R (PROVED): if all swallowed strict non-peaks of block m have q_l >= 0
and l' is one of them with q_{l'} > 0 and zero cost, the Hoffman constant of Z_U is >= 1/q_{l'} >= 4mC_m/c_{l'}. So without (DR) the
Hoffman constant is of design scale; Corollary 4.1 can absorb it only along windows far above l' (sparse one-sided carriers, HEURISTIC
dichotomy). Deleting one-sided switching to restore exact d-neutrality can cost O(1) in l_1 (HEURISTIC estimate). (DR) is therefore the
natural hypothesis, not a technicality.
5. **Scope (clarification).** (BT) allows any contact set. So the rows Theorem A adds to (BT) ∪ R_0^± ∪ R_S are those with infinitely
many swallowed carriers, not all resonant d-neutral, that violate (BT): through infinitely many strict non-peaks (with (DR) and gaps in the
ladder), through degenerate or weak peaks that are good or anti-sign, or through weak swallowing-sign peaks whose margins still keep
M_f(l)/Lambda°(l) within the ladder along a subsequence. (If M_f(l) <= (l 2^{l^3})^3 for ALL large l, Remark 5.5(i) -- valid at every f --
gives (MS) on the swallowing side; (W_inf) alone does not, since it bounds M_f/Lambda° only along a subsequence and Lambda°(l) may exceed
1/c_l when the S_l start far out.) A genuine but special class (at maximal contact with F finite, f depends only on finitely many numbers
a_j, so infinitely many near-threshold carriers need coincidences).
6. **6.3(d) overstated.** "Finitely swallowed rows stay open only when (H3) or (H2') fails" omits (W*) (approximate swallowing of good
sets, (O1)(i)); Corollary 4.2(b) needs (W*). The note itself says "open in case (O1)".
7. **Cor 5.4 for the original SLD**: see table (ii).
8. **Degenerate swallowing-sign peaks (Z4 part 8, refined).** Z4's sketch has a gap: Theorem thm:engineered uses the averaged data omega^theta for |tau| <= s_1 and both signs, and omega^theta(k) is outward on one side at a used degenerate peak, so the steering must be quantitative (mu'_k <= -kappa_D s_1). Z4's claim that steering through target coordinates costs (push) x (switching) is false at FREE target coordinates; free channels (z' at free coordinates, a on F) create no base excess (Lemma 9.2, PROVED). Under the linear hypothesis (FS) (e.g. a private free target coordinate for each used degenerate peak) the engineering step goes through (SKETCH 9.3), so (H3) can be dropped there; maximal contact (no free coordinates) and super-weak swallowing-sign peaks stay OPEN.
9. **Rigidity, strengthened (addition, PROVED).** Z4's Prop 5.6 extends verbatim from peaks to every carrier l of block m with
w_m(k(l)) != 0, l outside the finitely many carriers used by the data and S_l ∩ F empty: far points of S_l are contacts with
z_s = -sign(Delta d_m) sign(w_m(k(l))). So non-d-neutral two-piece data need sign-coherent far swallowing (q_l of sign -sign(Delta d_m) for
all but finitely many non-d-neutral carriers of the block) -- exactly the configurations in which Lemma 3.2 pins one side of the shift.
10. **Numerics**: maxcontact_toy.py checks signs of Step 3 only (finite degenerate model); I added didentity_toy.py (eq:didentity residual
<= 0.08 x 2t/sigma; the (H2'') bound never violated, seeds 3, 5, 11). Both are sign checks only.

## Attacks attempted (all failed to break the PROVED claims)
weak* vs norm (decompositions exist by compactness; forced data continuity used only qualitatively); uniformity in t, window and number of
active carriers (G*(l_*) covers every U ⊂ [1,l_*]; Lambda*, M_f, 1/gamma_f, 1/gamma_T monotone and evaluated at l_*; C_1..C_4, c_f, A*_0,
R_f fixed by finitely many carriers); Hoffman constants (finite for every feasible polyhedral system; weights m_l(U,n) > 0 since S_l is
infinite); signs (eq:peakshift, suplevel(c), side conditions of Lemma split, rigidity in Prop 5.6); near-contacts vs contacts (handled by
gamma_T in (2.1); exact zero cost forces |z_j| = 1 on supp V); c_0 vs l_infty (z in l_infty, f non-attaining; engineered approximants
truncate); finite vs infinite B, P, K (B infinite handled by active sets + box bounds); I finite; hidden assumptions on T (only (T-a)-(T-d),
(P1)-(P3), allowedness; SLD_G admissible); quantifier order (window data built from g, rho; engineered f' chosen inside Cor cor:D1 after the
averaged data are fixed).

## Single most valuable idea
The zero-cost cone of the swallowed switching depends on f only through finitely many combinatorial data on the finite target supports
(contact sign or free, F ∩ T(U), swallowing signs, peak status, max F); the continuous f-data are isolated in gamma_T, the margins (M_f),
the gaps (gamma_f) and the d-rows. Hence its Hoffman constant is a DESIGN constant G*(l), which a modified ladder (fixed before f) absorbs;
with the scale-dependent active sets U(t) = {lambda_l >= t^2} (converting l_1 projection errors into the coordinatewise bounds needed by the
one-sided expansion) this gives exact two-piece data on whole windows for infinitely many non-resonant swallowed carriers.

## What remains open after Z4 (for SLD_G made N-independent; F finite unless stated)
Problem prob:lemmaZper is open exactly for pairs (f,g), g not window-pinned, with f outside G ∪ R_SBinf, i.e. f with at least one of:
(E-a) a swallowing-sign swallowed peak that is degenerate (window data exist, Lemma 8.1; missing: the engineering step, SKETCH under the
linear hypothesis (FS) of ref notes 9.3, which holds when the used degenerate peaks have private free target coordinates; open at maximal contact) or weak with M_f beyond the ladder; (E-b) swallowed strict non-peaks with gaps beyond the ladder;
(E-c) near-contacts in swallowed targets with rooms beyond the ladder; (E-d) one-sided d-resources at a non-sparse set of levels (failure
of (DR); the d-row Hoffman constant is then design-scale, Lemma R); (E-e) approximate swallowing of good signature sets ((O1)(i));
failure of (H2'') (characterized in finding 3); and (O4) infinite F (untouched). Common core (Problem 6.2 of Z4): exact data for inexact
resources, or an engineering theorem tolerating first-order defects O(t) at window scale t. Lower semicontinuity along far lowerings is not
needed where Theorem A applies, and (HEURISTIC, I agree) cannot help where it fails, because the windows available above the slack threshold
of f^L carry the same coarse swallowed sets as at f. Density remains open for every admissible T, including SLD and SLD_G.
