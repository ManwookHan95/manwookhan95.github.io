# Referee report on Y2 (Round 6): peak-carrying engineering, non-rigid degenerate peaks, mixed blocks, failure of (H2'')

Refereed: r6/Y2_notes.md (and Y2_part1..6.md, Y2_work/*.py, re-run), against paper/martin_density_note.tex (Sections 1, 7, 8: Lemma
lem:threshold, Lemma lem:algebra, lem:block, Definition def:twopiece, Theorem thm:engineered, Corollary cor:D1, Definition def:SLD,
lem:uniformtransfer, lem:onesidedtransfer, lem:suplevel, eq:peakshift, eq:didentity, lem:switchbudget, lem:split, lem:windowtwopiece),
and the refereed Round-5 results (Z3 Theorem E / Lemma U; Z4 Theorem A'', SLD_G, G*, Lemma 2.3, Lemma R, ref Section 9; Z6-referee
D''', Theorem U', Theorem V, Proposition P, Lemma 2.1, Proposition R1). Referee part files: r6/Y2_ref_part1..5.md; proofs of all fixes and
extensions: r6/Y2_ref_notes.md; scripts: r6/Y2_ref_work/.

## Overall verdict
The central new mechanism is CORRECT and valuable: a COMPANION first row f_j, obtained by moving z at a few far coordinates of an unused
signature set (a donor), raises the block threshold strictly (Lemma T), leaves the values of all switching carriers unchanged, multiplies
all d-coefficients of a block by one common factor (so exact d-neutrality survives), and turns every used degenerate peak into a strict
non-peak of f_j with a tiny but fixed gap; Theorem E (Z3) with window-dependent c_flat then transfers recovery from f_j to f. This bypasses
the quantitative steering problem at engineered approximants (Z4-referee 9.1) completely. Lemma T, Lemma U', Theorem E', Proposition Q,
Corollary Q', Lemma 3.1, the face reduction (Lemmas 4.1, 4.2, Proposition 4.3) and Theorem M, Lemma 5.1, Proposition 5.2 and Theorem H
were re-derived line by line and are correct. Theorem Y and Corollary Y.1 are correct by combination. I found one genuine (fixable) GAP:
Lemma 3.2 / Theorem P(a) invoke Lemma 2.3 of Z4 "verbatim", which fails when (DR) holds through its vacuous alternative in a block that
contains kept degenerate swallowing-type peaks (G1); the gap is closed for D''' and D^Y and for finitely many such peaks, and remains for
SLD_G with infinitely many. One statement precision is needed for the later uses of Proposition Q (P-Q1: inward strict non-peaks). One
interpretive claim is not proved: that in the "aligned corner" every admissible move outside the data supports lowers the threshold
(target-coordinate moves are not covered by Lemma T(d)); I prove a target-donor lemma that narrows the residual of item (d).
No counterexample is claimed; nothing I checked points to one. Lemma Z and density remain OPEN for every admissible T.

## Verdicts
| claim | Y2 label | verdict | main point |
|---|---|---|---|
| Lemma T (threshold equation, monotonicity, perturbed version) | PROVED | correct | re-derived; independent SOCP-free primal-dual proof (ref notes 1); 60-digit adversarial test of (e): 0 violations |
| Lemma U' (inward coordinates; window-dependent A_2, gamma_B; t_1, j_0 uniform) | PROVED | correct | kind [3] only needs ||W||_inf = (1-rd)M, attained at a non-degenerate peak; all A_2, gamma_B constraints are upper bounds on c_flat, t_1-constraints monotone in c_flat |
| Theorem E' (window-dependent c_flat) | PROVED | correct | c_flat enters only via (A), I_r, Q, and the eps_j comparison |
| Proposition Q (companion transfer) | PROVED | correct (precision P-Q1) | every inward coordinate is a switching coordinate; values of switching carriers unchanged (P1, X_j); common factor |zeta|/|zeta'|; Lemma T(e) with allowedness (b) cross-effect bound re-derived. (W2) must allow inward strict non-peaks (needed by Thm P(b), Thm Y); proof extends by continuity (ref notes 2) |
| Corollary Q' (peak-carrying Cor cor:D1) | PROVED | correct | fixed data, fixed c_flat; donors outside supp b^+-; answers item (1) without (FS) |
| Lemma 3.1 (donors exist), raisability bookkeeping | PROVED | correct | Ba_j ⊂ F ∪ ∪_{Sw_j}(S_l ∪ supp y_l) |
| Lemma 3.2 (window data with inward degenerate peaks) | PROVED | gap (G1), fixable | two-case discrepancy bound and inward signs correct; Step 5 "Lemma 2.3 applies verbatim" FAILS if (DR) is vacuous in a block with kept degenerate peaks (q > 0 in its d-row, no repair direction) |
| Theorem P (a) SLD_G / D''' without (H3); (b) U' with non-rigid degenerate peaks | PROVED | (a) correct with fixable gap (G1); (b) correct with P-Q1 | (G1) fix: non-vacuous (DR), or finitely many such peaks (drop them via eq:didentity, f-constant 1/q_min), or D''' (one factor D(l) absorbed); OPEN for SLD_G with infinitely many |
| Corollary P.1 (maximal contact) | PROVED | (ii) correct; (i) correct with the (G1) proviso for SLD_G | anti-sign swallowed peaks (Lemma 5.0) are donors in every block |
| aligned corner (3.4) | OPEN | agreed open, but its description overstated | "every admissible move outside the data supports lowers the threshold" not proved: target moves change several zeta_m(k) at once; Lemma R-T (ref notes 3) shows free coordinates give donors unless the one-sided derivative vanishes both ways |
| Design D^Y; faces of configuration cones are free configurations | PROVED | correct | Xi^Y >= Xi', N-free, recursion well defined; faces = (Z1)->P, (Z2)->type 0 |
| Lemma 4.1, Lemma 4.2, Proposition 4.3 (face reduction) | PROVED | correct (normalization precision P-M1) | Farkas on C(U); ri C ⊂ ri F_min; subspace V(U) stabilizes; LP check of 4.1 on 141 cones x 200 tau: no violation |
| Theorem M (no (DR), no dichotomy; rate K_F^rel) | PROVED | correct | V_1 <= C'(K_1+M_f)t; window arithmetic re-done (surplus Lambda°^4 G**^9 D^6); also closes (G1) for D^Y |
| 4.4 (a) one-signed resonant model; (b) kappa* = 0 iff C meets ri Z^0 | PROVED | correct | "kappa* = Theta(1/q_min) in one-signed blocks" proved only in the resonant model (general: lower bound 1/q_{l'} - 2, upper bound SKETCH) |
| Lemma 5.1 (peak trace), Proposition 5.2 (shift-cost pinning), Theorem H | PROVED | correct | partial-infimum convexity, continuity, attainment on the sign sphere; I_up ∩ I_lo is always empty |
| 5.3(a) gap pinning; (b) sufficient condition for c_* > 0 | PROVED | correct inequality; gloss needs precision | O(t) pinning needs gap <= K t^2 on the window AND the design factor 1/(m_l lambda_l) for (tau)_-/lambda; (b) must hold at every large level |
| 5.3(c) coherent shift resonance | OPEN (+ observation PROVED) | open agreed; observation imprecise | constraint is on sum_{m'} Delta d_{m'} R*w_{m'} (all blocks), modulo the used carriers |
| Theorem Y (master, D^Y), Corollary Y.1 | PROVED | correct by combination (P-Q1, P-Y1, P-Y2) | (Y1) must read r*_l(l_*) > 0 for all l_* >= l; at maximal contact only M_f, gamma_f, K_F^rel remain |
| 6.2 Conjecture G | OPEN | agreed | budget computation HEURISTIC as labelled |
| 6.3 steering at f' (a),(b) | PROVED | correct | statements about the method |
| 6.4 weak peaks through companions | SKETCH | plausible SKETCH with three gaps | quantitative raise (Lemma T(e) is qualitative), first-order term alpha(k) != 0 at f, uniformity of face/repair constants at f_j |

## Main findings
1. (G1) Vacuous (DR) and kept degenerate peaks (gap, fixable; ref notes 4). Z4's (DR) allows tau^{m,+-} := 0 when block m has no
swallowed strict non-peak with q != 0. Under (M) the degenerate swallowing-type peaks (q = Phi M/(mC) > 0) join the d-row, so in such a
block the exact cone forces them to 0 and Lemma 2.3 cannot repair. The actual switching through them is pinned only at K t/q (d-identity;
the 1/q constant is essentially attained, Z6 numerics), i.e. at DESIGN scale 1/Phi_l, which SLD_G does not absorb. Repairs (PROVED):
non-vacuous (DR) in those blocks; or finitely many such peaks (drop them: sum |tau| <= C'(K_1 + M_f)t/q_min(D_m), an f-constant, and then
no donor is needed in that block); or D''' (q >= Phi/2, one factor D(l) absorbed); for D^Y Theorem M covers it with K_F^rel <= C_f in the
resonant sub-case. OPEN for SLD_G with infinitely many such peaks. Theorem Y and Corollary Y.1 (design D^Y) are NOT affected.
2. (P-Q1) Inward strict non-peaks in Proposition Q (precision; ref notes 2). Theorem P(b)/Theorem U' use kept q > 0 strict non-peaks
inwardly with arbitrarily small gap (Z6-referee Lemma 2.1). Proposition Q's (W2) allows only degenerate peaks. The extension holds: such
coordinates are switching coordinates (equal omega^+- forces both to vanish), keep their values, and stay strict non-peaks of f_j (threshold
raised in I_D; continuity elsewhere, finitely many coordinates).
3. Target donors (extension, PROVED; ref notes 3). The one-sided derivative of Psi_m along any admissible move outside
F ∪ Ba_j ∪ T_j ∪ ∪_{Sw_j} S_l is the explicit convex positively homogeneous function D_m of Lemma R-T; if it is positive for the blocks of
I_D not served by signature donors, Proposition Q holds with that companion. At a free coordinate D_m(e) + D_m(-e) >= 0, so one direction
raises the threshold unless both derivatives vanish. Hence the residual of (d) is not the whole aligned corner. Moreover (ref notes 6a)
in Theorem M/Y a degenerate peak whose sign row is d-forced has tau' = 0 and is not an inward coordinate, so (Y3) is needed only for
blocks whose degenerate peaks are actually switched (non-rigid ones), and (TD_m) may be replaced by "signature donor or target moves
with D_m > 0".
4. Precisions: normalization of rows in Lemma 4.1 (P-M1, unweighted (Z1) rows); one-signed kappa* only in the resonant model; gap-pinning
gloss; coherent-shift observation is a cross-block constraint; (Y1) with r*_l(l_*) at every level; Lambda*_f vs Lambda_g; I_up ∩ I_lo = {}.

## Attacks attempted (none broke a PROVED claim beyond (G1))
weak* vs norm (companion convergence via smoothness of |.|_m and compactness of L; f_j need not attain); uniformity in t, in the window and
along companions (t_1, j_0 from Lemma U' are independent of A_2(j), gamma_B(j); j_0 depends only on f_j -> f, which is ours; c_flat,j enters only
through (E-d'), (E-e')); uniformity in the number of active carriers (G**, H_comb over all subsets of [1,l]; R_f from dimension
stabilization; K_F a max over finitely many U); Hoffman/Farkas constants (Hoffman 1952 for every free configuration; Farkas LP minimum
attained; numerically checked); design N-independence (G**, D(l), H_comb N-free; D^Y recursion well defined); non-attained infima (c(.;l)
inner infimum not attained -- handled; c_* attained); signs and one-sidedness (inward signs in (M); eq:peakshift; suplevel(f) in 5.3(a);
Lemma T at degenerate peaks one-sided); near-contacts vs contacts (donor coordinates become free coordinates of f_j; b^+- vanish there);
c_0 vs l_infty (z + delta in l_infty; engineered approximants of f_j truncate in Cor cor:D1); finite vs infinite peak/contact/support sets
(finitely many inward coordinates per window; infinitely many degenerate peaks -> (G1)); hidden assumptions on T (only (T-a)-(T-d), (P1)-(P3),
allowedness; private signature coordinates are essential for donors -- Y2 restricts to SLD-type designs, correctly); quantifier order (window
data from (g, rho); companion and its Delta_j after the data; Lemma Z per mate).
Cross-block donors: moves in one block reach others only through targets of LATER carriers, bounded by allowedness (b) at 2^{-r} of the
own effect; the donor coordinate itself is protected by excluding X_j. Blocks outside I_D whose threshold may fall: only finitely many used
coordinates, all strict non-peaks with positive gaps: continuity.

## Numerics (r6/Y2_ref_work)
lemmaT_cert.py (primal-dual identity, 3e-14); lemmaT_e_mp.py (Lemma T(e), 60 digits, 0/1868 violations at 0.999999 of the bound);
farkas_face_check.py (Lemma 4.1, max(lhs - rhs) = -0.034 over 28200 tests); target_donor_check.py (Lemma R-T: the sign of the one-sided derivative D_m predicts the sign of the finite-difference
change of theta in 2970/2970 tests, half of them with a tuned degenerate peak; D(d) + D(-d) >= 0 in all 1500 blocks);
Y2's companion_check.py re-run (0 failures, d-ratio deviation 8e-4).

## Single most valuable idea
Status steering is free at a companion: by the closed-form threshold equation, a zeroth-order move of z at private coordinates of an
unused signature set raises the block threshold strictly while leaving every switching carrier's value untouched, so every used
degenerate peak becomes a strict non-peak and all d-coefficients of the block scale by one common factor (exact d-neutrality survives);
Theorem E then needs only p*(f_j - f) = o(T_lo^2), which is free because no quantitative size of the raise is required.

## What remains open (design D^Y, F finite, g not window-pinned)
(r) rates beyond the ladder: Lambda*_f (rooms of good signature sets; approximate swallowing), M_f (weak swallowing-type peaks; Y2 6.4 is
a SKETCH with gaps W-a..c), gamma_f (gaps of kept swallowed strict non-peaks), gamma_T, K_F^rel (nearly but not exactly d-neutral zero-cost
directions; Conjecture G open), K_sh^rel; (d') non-rigid degenerate swallowing-type peaks in blocks with neither a signature donor nor a target
move of positive derivative (Lemma R-T); (h') coherent shift resonance (c_* = 0 or beyond the ladder); (O4) infinite F. For SLD_G also:
infinitely many degenerate swallowing-type peaks in a block with vacuous (DR). Lemma Z and density of NA((c_0,p),l_2^2) remain OPEN for every
admissible T, including SLD, SLD_G, D''' and D^Y.
