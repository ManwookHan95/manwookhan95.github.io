# Referee report on V3 (Round 7): infinite base support, critical support swallowing, (O4)

Refereed: r7/V3_notes.md, V3_part1..4.md, V3_work/rt_check.py, against the note paper/martin_density_note.tex (lem:dualball,
lem:threshold, prop:forced, prop:approximants, rem:lemmaZ(c), lem:slack, lem:twosided, lem:smallness, lem:budget, lem:suplevel,
lem:box, def:windowcert, prop:windowcert, lem:uniformtransfer, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence,
def:twopiece, lem:switchbudget, lem:split, lem:flip, lem:peakshift, lem:modswallow, lem:badpeaks, lem:exactswitch,
lem:windowtwopiece, lem:onesidedtransfer, lem:avgfunctionals, thm:windowed, def:SLD, thm:SLD, lem:martintail) and the refereed
Round-5/6 results (Z5_ref R1/R2, Z3 Lemma 3.1 + Z3_ref, Y3 Theorem 2.1, Y3_ref 3.2-3.4). Part files r7/V3_ref_part1..4.md;
proofs of fixes r7/V3_ref_notes.md; scripts r7/V3_ref_work/rt_indep.py (independent implementation of (RT)), vp_check.py.

## Overall verdict
V3 contains a genuinely new and correct idea that removes the main infinite-support obstruction of Round 6. The raise-transfer
lemma (Lemma 2.3) is correct and elementary: a same-sign raise of the base part on its support cancels exactly against the
normalisation lam - 1, so the mate condition transfers to the raised row with only a relative factor lam and an additive error
2||U*Da|| + p*(L*(w^# - w)). With a diagonal base whose entries decay fast (design D^mu), this additive error is
super-polynomially small on deep coordinates, while the l_1-mass of the raise (~ T^2 or larger) no longer matters. Theorem 2.5
(windowed recovery through companions with this weaker decoupling) is correct. Theorem RS (Theorem R1 run at raised companions,
where R1's deep set is empty) is correct; I checked the three "inspection items" constant by constant. Hence, for the designed
norm, critical and super-critical support swallowing by finitely many bad carriers ((O4-crit) and the support part of
(O4-nd)) is resolved under (W*), (H2), (B_fin), (RR), (ND'). Gaps found are all fixable or are mislabelled side remarks:
(1) the non-degeneracy condition (ND_{L_0}) of Lemma VP is mis-stated (fails trivially when a carrier vanishes on F); fixed by
(ND'); (2) Remark 3.5(e)'s transfer of RS to Martin's p via lem:martintail is false as stated; (3) the "Consequence" of Theorem
M_inf (transport of Y1/Y2 master theorems) hides an f-dependent rate (VP constants for growing carrier sets); (4) Section 1's
"copied data lose only 9/8" ignores a first-order consistency defect (HEURISTIC). I also strengthen RS: (H3') -> (H3-inf), and
(ND), (RR) are needed only for the bad strict non-peaks. No counterexample is claimed or suggested; density remains OPEN.

## Verdicts
| # | Claim (V3 label) | Verdict | Main point |
|---|---|---|---|
| 1 | Lemma 1.1, model 1.2, Remark 1.3 (PROVED) | correct, with label fix | identity and [4/3, 3/2] computation re-derived; Remark 1.3 correct (thm:compact); "copying loses only 9/8" and "factor 2 belongs to deep assignment" are HEURISTIC (copying leaves the defect Delta B - X) |
| 2 | Lemma 2.1, 2.2 (PROVED) | correct | w = J_V(L** zhat) depends only on zhat; Z3 Lemma 3.1 applies verbatim |
| 3 | Lemma 2.3 RT (PROVED) | correct | re-derived; numerics with lam up to 3.3, with and without VP-type corrections: never violated |
| 4 | Corollary 2.4 (PROVED) | correct | phi' = (s(u)-1)/(lam^2 s(u)) |
| 5 | Theorem 2.5 E_RT (PROVED) | correct | every constant re-derived; reduces to thm:windowed / Z3 Theorem E |
| 6 | Design D^mu, Lemma 3.1 RR (PROVED) | correct | thm:SLD uses U only through q* being a norm; diagonal U allowed by the set-up |
| 7 | Lemma VP (PROVED) | correct proof, statement gap (fixed) | (ND_{L_0}) fails when some u_k|_F = 0 although nothing must be corrected; replace by (ND'): a|_F not in span{u_k|_F} |
| 8 | Theorem RS (PROVED, I1-I3) | correct with fixable gap | needs (ND') instead of (ND_B); I1-I3 verified; strengthened to (H3-inf) and L_0 = B_np, W = U_{B_np} |
| 9 | Theorem A (PROVED) | correct with fixable gap | (ND') fix; |b^theta| superfluous in W; p*(g - g_y) = O(eps_e log) |
| 10 | Cor 4.2 (LSC-trunc) (PROVED) | correct | immediate from lem:pair |
| 11 | Theorem M_inf (reduction PROVED; transport SKETCH) | reduction correct; transport plausible with a gap | VP constants for growing L_0(j) are f-dependent rates; Z4 Thm A does not fit "(B_fin)" |
| 12 | (O4-box) 4.4 (SKETCH/OPEN) | as labelled | the o(N^2) threshold is heuristic |
| 13 | Remark 3.5(e) "holds for Martin's p via lem:martintail" | FALSE as stated | martintail transfers density, not individual rows |
| 14 | Residual list 4.5, Section 6 | accurate with precisions | (E1) unavoidable for any fixed mu; (E4) (H3-inf) now covered; Theorem 3.5 not fully superseded |

## Detailed findings
F1 (Lemma 2.3, the key step). With f + lam r h = A + L*W: f^# + rh = (A + Da)/lam + L*((1 - 1/lam)w + W/lam) + L*(w^# - w);
||a + Da||_1 = ||a||_1 + ||Da||_1 gives ||Da||_1 <= lam - 1 + ||U*Da|| and q*(A + Da) <= pi + lam - 1 + 2||U*Da||. Correct for every
lam >= 1, no smallness of Da. The Round-6 negative statements (Y3 3.5(i), Y3_ref 3.3 "nested raises impossible") concern the
distance p*(f_j - f), which Theorem 2.5 no longer needs to be o(T_lo^2): they remain correct but are not obstructions.

F2 (Theorem RS). R1 used (CS_B) only through the deep set D_t (Claim 3.2(b): off D_t both side parts are <= 3|a|/t); Lemma R2
and Y3 Theorem 2.1 need only side parts. Raising |a| to >= 2C_tau T U_B on F empties D_t for all t <= T. Step 2(ii): the cone
Z_f is literally the same set at f_j because VP preserves the values of the bad strict non-peaks, whose d-coefficients are
q_l = eps_l q_0 val_l/sigma_m (lem:threshold), so each d-row is rescaled by a positive block factor; tau' = 0 on bad peaks.
(I1): the budget lemmas use only s(t) - 1 <= t^2/2 and g(xi) = 0; lem:smallness along pairs (j_n, t_n) forces j_n -> infinity.
(I2): the bounded-switching map converges in operator norm on R^B. (I3): Lemma R2 with U_* = 0 has no flips; transfer data
persist (lem:persistence). Quantifiers: design (mu, SLD) -> f -> g, rho -> windows -> T_j -> raise -> data: correct.

F3 (Lemma VP statement). For a diagonal base the value change of u depends only on u|_F. A contact-swallowed bad carrier whose
signature set and target avoid F has u_l|_F = 0, gamma_l = 0 and a zero row of Lambda: (ND_B) fails, RS does not apply, yet
the value is preserved automatically. Fix (ref notes Section 2): G maps into V_0^perp, Lambda is onto V_0^perp under (ND').
Similarly, for F finite (ND') can fail while no raise is needed; the clean statement is "(CS_{B_np}) or ((RR) and (ND'))".

F4 (strengthening, PROVED in ref notes Section 3). (H3-inf): a B_K carrier at a degenerate peak with sgn w = -eps_l may change
status at f_j (gap or margin O(eps_e)); in every case |tau_l| = O(K* t) (peak inequality, or the near-peak inequality from
lem:suplevel(f) with gap O(eps_e) = o(t^2), plus the B_K sign row), Z_f is a subcone of Z_{f_j}, and projecting onto Z_f works.

F5 (Theorem A). Correct; Y3 Theorem 2.1 already raises the b^theta support internally, so W = (sb^+)_- + (sb^-)_+ suffices.

F6 (Theorem M_inf). The reduction is a two-line consequence of Lemma 2.3 and is correct. The claimed extensions of Y1's Master
Theorem and Y2's Theorem Y to infinite F need VP at exactifying companions for carrier sets L_0(j) growing with the level; the
VP constants are f-dependent and must satisfy log C_0(j) = o(n^w_{l_j}). Not addressed; keep as SKETCH.

F7 (Remark 3.5(e)). lem:martintail: density for p_N for infinitely many N implies density for p. It does not transfer membership
of an individual f in Rec; RS is a theorem about p_N only (Sections 7-8 assume I finite).

F8 (Section 1). Lemma 1.1's remainder bound holds with constant 2/3 instead of 2; the qualifier about coarser targets is vacuous
(allowedness (a)). Copying B_pm on the deep set leaves b^+ - b^- = Delta B != X; repairing this per coordinate is what deep
assignment does, and its first-order cost at scales r << t is not accounted for in the "9/8" statement. Since Section 3 makes the
question moot, this only affects labels.

## Attacks attempted
weak* vs norm (f_j -> f in norm; forced-data continuity); uniformity in t (sub-window inside W(l_j); budget only on S_j), in the
window (n_j = o(n^w) by (W*), depth m_j ~ (2/eps)(2n_j + log(C/theta_j)) fits), in the number of active carriers (B finite),
along companions (I1-I3); simultaneous exactifications (only raise + VP; VP lives on a fixed finite F_0 disjoint from the raise);
Hoffman constants (same cone set; violations comparable); design N-independence and admissibility (thm:SLD over any U; Lemma B
density in every block untouched); non-attained infima (none used); signs (same-sign raise, |Da''| <= |a|/2 keeps sgn a = z on F);
near-contacts vs contacts (raise does not touch z, rooms or contact sets); c_0 vs l_infty (z in B_{l_infty} unchanged; f_j via
rem:lemmaZ(c)); infinite support sets (raise in l_1, possibly infinitely supported: allowed by Lemma 2.3); hidden assumptions on T
(Lemma 2.3, Theorem 2.5 any admissible T; RS: SLD-type over D^mu only); quantifier order (correct). Numerics: independent SOCP
check of (RT) and Cor 2.4 (two seeds, lam up to 3.33): no violation; VP Newton check.

## Single most valuable idea
The raise-transfer lemma: a same-sign raise of the base part on its own support is invisible to the mate condition up to the
relative factor lam and the Hilbert/normer footprint ||U*Da|| (the l_1-mass cancels against the normalisation). Choosing the base
operator diagonal with fast-decaying entries makes that footprint super-polynomially small on deep coordinates, so cushions can be
raised to dominate any bounded switching at no cost: infinite base support then behaves like finite support (no flips), and every
cushion-sparsity hypothesis of Rounds 5-6 disappears for non-mu-thin supports.

## What remains open
Density remains OPEN. At infinite F, for the designed norm: (E1) mu-thin supports (exist for every fixed mu; deleting the thin
coordinates instead of raising costs ~ y^{1+o(1)}); (E2) infinitely many bad carriers (box-size switching, scale-free raises);
(E3) non-d-neutral fixed data at raised rows ((SC) at f_y); (E4) failure of (ND') (a|_F in the span of the bad strict non-peaks
on F: second-order value drift can collapse d-neutral cones) and degenerate bad peaks with the swallowing sign; (E5) the finite-F
core (A)-(D) of ADDENDUM 6 and its transport to infinite F, where VP constants for growing carrier sets are a new f-dependent rate.
