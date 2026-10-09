# Referee report on Y1 (Round 6): unified design D_X and the companion rate dichotomy

Refereed: r6/Y1_notes.md (= Y1_part0..4, 5a, 5c, 5b; checked against the part files) and r6/Y1_work/*.py, against
paper/martin_density_note.tex (Sections 1, 7, 8: def:SLD, thm:SLD, lem:threshold, eq:margin, lem:block, def:twopiece, cor:D1, lem:twosided,
lem:budget, lem:suplevel, lem:box, lem:pinning, lem:phicalc, lem:switchbudget, lem:split, lem:peakshift (eq:didentity), lem:signmixed,
def:swallowed, lem:modswallow, lem:badpeaks, lem:exactswitch, lem:windowtwopiece, lem:onesidedtransfer, thm:windowed, thm:S, rem:openZ)
and the refereed Round-5 results (Z3 Theorem E, Lemma U, Lemma 3.1, Prop. T; Z4 Theorem A'', Lemma 5.0, (DR), Cor. 5.4; Z5 T1-T12, R1;
Z6-ref D''', Lemma 2.1, Theorem U', Prop. P), and the parallel Round-6 referee reports Y2_referee.md, Y4_referee.md.
My part files: r6/Y1_ref_part1..5.md; assembled proofs: r6/Y1_ref_notes.md; scripts: r6/Y1_ref_work/.

## 0. Bottom line
Y1 is CORRECT in all its PROVED claims. I re-derived every step of Theorems 1 and 2, Lemmas T, T2, T3, 3.1-3.6, 4.1-4.3, 5.1, 5.1',
Proposition 5.2, Theorem E' and the master theorem, including all constant arithmetic and the order of quantifiers, and audited every
f-dependent quantity entering the window constants: each is a fixed f-constant or one of the omega(l) rate objects (no hidden rate).
I found six precisions (m1-m6), none of which changes a statement's conclusion or a construction. The most substantive is (m3): the stated
reason why a donor is pinned and raisable is wrong (S^nat does not exclude [1,l]); I first suspected a counter-scenario (a class-G
SWALLOWING-type donor making "(C3) after (C1)" infeasible), and refuted it: the tail point s_m itself carries room >= delta_c 2^{-sigma(l)}/n_c
>> b(w), which forces eps_c = -vs_c. The master theorem therefore removes every growth/rate condition of the Round-5 core (r) within its
structural hypotheses (SP_w), (Do_w), (Cmp_w), (NN_w). The sketch on tiny repairs is plausible with two additions. The residuals (n) and (d)
are residuals of Y1's move class, not intrinsic: the Round-2 far pull, re-proved on companions by the Y4 referee, lowers single carriers
and would remove both (SKETCH of the assembly). No counterexample is claimed; nothing I checked points to one. Lemma Z and density remain OPEN.

## 1. Verdicts
| Claim | Y1 label | Verdict | Main point |
|---|---|---|---|
| Theorem 1 (design D_X: admissible, N-free, disjoint bands, survival) | PROVED | correct (precision m1) | recursion, bands (b(w) <= 2^{-4u^{-8}} < u(w), u(w^+) = b(w)), fine weights <= b^2/3, N-freeness, survival re-derived. (m1) Z4 Cor. 5.4 survives in the Z4 referee's M_f form; its M^canc form needs the clause c_l <= (delta_l ||h_l||_1)^2 (addable to c_{l+1}) |
| Theorem 2 (clean sub-windows at every level) | PROVED | correct | omega(l) = 3l + |T(l)| objects, omega+1 disjoint open bands, pigeonhole |
| Lemma T, T2, T3 (threshold equation) | PROVED | correct | re-derived by hand (incl. the c-term of Bh at level theta+h); exact norming certificate to 2e-16; 2493 adversarial T2 tests incl. constructed degenerate peaks, 0 violations |
| Lemmas 3.1-3.6 (pinning at a clean sub-window) | PROVED | correct (precisions m2, m5) | diagonal pinning on S^nat = S \ (F ∪ T(l)) (no slaving, no products); 3.5(b) correct and useful; 3.6 tacitly uses (SP_w) through K_d; constant 4b^2/t in 3.1. Added: one-signed blocks automatically have one shift source |
| Lemmas 4.1-4.3 (companion f^#_w) | PROVED | correct (precision m3) | cost o(T_lo^2), status table, common d-rescaling, forced q^# = r^nat/A^# re-derived; donor claim true but for a different reason (tail point s_m has room >> b(w)) |
| Proposition 5.2 (transplant) | PROVED | correct | zero cost of Z_kappa(beta) checked coordinatewise; violations (Z1)-(Z4); Hoffman RHS-independence; block-diagonal repair; split at f^#; shift trick; A_2 = 22; even K_w <= C_f Design^2 u^{-3} |
| Theorem E' | PROVED | correct | c_flat enters only via (A), I_r, Q and the eps-comparison; t_1, j_0 uniform (agrees with the Y2 referee) |
| MASTER THEOREM 5.4 | PROVED | correct | window arithmetic re-done (K_w T_hi -> 0, n c_flat/K_w -> infinity, eps_j = o(c_flat^2 T_lo^2)); C_f uniform in l, w, t; quantifiers in order |
| Corollary M1 (maximal contact) | PROVED | correct | (C1),(C2) void; (SP_w) and donors from Z4 Lemma 5.0; one-signedness at infinitely many levels forces no anti-type strict non-peak with w != 0 |
| Corollary M2 | PROVED | correct (precision m4) | anti-type peak non-degenerate with S_c ∩ F = {}; "nonzero (DR^pm)" stronger than Z4's (DR) |
| Corollary M3 | PROVED | correct as a statement on hypotheses (precision m6) | rigid non-one-signed blocks are covered by Z6 U' (under a rate), not by 5.4; open core = intersection of complements |
| Tiny repairs by converted anti-type peaks (5.6(3)) | SKETCH | plausible SKETCH, two additions | (i) raise also in one-signed blocks; (ii) the member's gap ~ T_lo^3 < t^2 is admissible since gap >= t^2 of kind [1] is never used in Lemma U (PROVED: kind [1']) |
| Residual list (n), (m), (d), (h), (O4) | OPEN | logically correct complement of 5.4; (n), (d) not intrinsic | far pulls lower single carriers (Y4-ref C.2-C.7): (NN_w) and (Do_w) removable by exact per-carrier tuning (SKETCH, diagonal U) |

## 2. Main findings (proofs in Y1_ref_notes.md)
**F1 (m3, donors; reason corrected, conclusion confirmed).** Y1 asserts a donor is class R or a class-G anti-type peak at every clean
window "because the exceptional coordinates lie in [1,l], outside S^nat_c" — false as stated (S^nat_c(l) = S_c \ (F ∪ T(l))). Correct proof:
s_m in S^nat_c(l) with vs z_{s_m} <= 0 gives room >= v_c(s_m) >= delta_c 2^{-sigma(l)}/n_c in the -vs direction, while b(w) <=
2^{-24 sigma(l)}/l (Design >= 2^{6 sigma(l)}); so class G forces eps_c = -vs_c, and then no exceptional point can lie in S^nat_c(l).
Hence "(C3) after (C1)" always has outward room 2 v_c(s_m), and Lemma 4.1's feasibility holds as written.
**F2 (m2).** Lemma 3.6's constant uses K_d (Lemma 3.4 under (SP_w)); state (SP_w). Addition: +1-one-signed blocks satisfy (U3), -1-one-signed
blocks satisfy (L3).
**F3 (kind [1'], PROVED addition).** In Lemma U a first-kind coordinate needs only |omega(k)| <= 2 gap(k)/t (radius >= t/4 in
lem:block(d)); gap >= t^2 is a window-certificate convention. Needed by the tiny-repair sketch and by any repair through carriers with
gap ~ T_lo^3.
**F4 (residuals (n), (d) vs far pulls).** Y1 states that (n) needs LOWERING a z-signed functional, "impossible with banks ...; with supp a
fixed only |F| - 1 Hilbert directions". True for that move class; but the Round-2 far pull (sign-flipped far contact with a tiny support
mass) lowers ONE carrier's value by 2 v(j) at first order, and the Y4 referee re-proves it on companions together with Lemma U / Theorem E
for pulled and banked supports and exact two-sided per-carrier tuning (diagonal base U). Plugged into Y1 (outline in Y1_ref_notes 7): tune
every kept nearly neutral carrier of every one-signed block to exact d-neutrality at cost O(Design b log(1/b)) = o(T_lo^2), so (NN_w) is
not needed; pulling a kept weak/degenerate swallowing-type peak below threshold on its own closed signature set replaces (Do_w).
Status: SKETCH (assembly), pending refereeing of Y4-ref C.2-C.7; needs bounded gaps of the S_l and 1/s_{sigma(l)}^2 (diagonal U) in Design.
**F5 (precisions).** (m1) survival of Z4 Cor. 5.4 in its M_f form; (m4) M2's donor non-degenerate, S_c ∩ F = {}; (m5) Lemma 3.1 constant;
(m6) scope vs Z6 U'; Lemma 4.2's thresholds l_f also exceed the donors' exceptional points (implicit in Y1).

## 3. What is genuinely new and valuable in Y1
(a) Excluding ALL coarse target coordinates from the pinning and closing sets (S^nat_{l''}(l) = S_{l''} \ (F ∪ T(l))): pinning becomes
diagonal (no slaving, no room products), closing costs carry no target-induced terms for coarse carriers (the Z3-ref G5 / Y4-ref G-PW1
factor disappears), and after closing the zero-cost cone is a generalized configuration on T(l), whose Hoffman constant G**(l) is a design
constant. (b) The pigeonhole over omega(l) + 1 sub-windows with disjoint bands (as in Y4) makes every rate tiny or robust at EVERY level.
(c) Lemma 3.5(b): anti-type near-threshold strict non-peaks are pinned, so their tiny gaps are not rates. (d) The donor threshold raise
(as in Y2) made quantitative (Lemma T2) and window-uniform, converting weak and degenerate swallowing-type peaks into kind-[3] coordinates.

## 4. Attacks attempted (none broke a PROVED claim)
weak* vs norm; uniformity in t (only via b(w) <= T_lo^4/(l Design) and fine weights <= b^2/3), in the window (design x u^{-k} x f-constants;
Q(w) dominates), in the number of active carriers (G** over all subsets of [1,l]), along companions (Lemma U', supp a fixed); Hoffman/Farkas
(RHS independence, feasibility via 0, the one-signed d-row certificate); N-independence; non-attained infima (polyhedral projections, root of
a strictly monotone Psi, exact norming certificates); signs and one-sidedness (peakshift, suplevel(c),(f), shift trick, donor direction,
forced q^#, signs of w^# at kept carriers); near-contacts vs contacts ((C2), free target rooms >= u, flipped v-mass <= b); c_0 vs l_infty
(non-attaining companions, Corollary D1 at each f_j); finite vs infinite sets (F finite; G, T(l) finite per level); hidden assumptions on T
(only (T-a)-(T-d), (P1)-(P3), allowedness and the explicit recursion); quantifier order (D_X before f; companions depend on f only).
Suspected counter-scenario (swallowing-type class-G donor): refuted (F1).

## 5. Numerics (r6/Y1_ref_work; sanity checks only)
lemmaT_cert2.py: exact norming certificate from Lemma T (N(w) = 1 to 2.2e-16, <w,zeta> = A to 5.4e-16, primal SOCP to 2.5e-9) on 150 random
blocks. lemmaT_indep.py: 2493 adversarial Lemma T2 tests (half with constructed degenerate peaks, perturbations in the threshold-lowering
direction): 0 violations, minimal ratio actual/bound 8.45. lemmaT_peakset.py documents a dual-SOCP indeterminacy at negligible weights
(solver behaviour). Y1's scripts (threshold_check.py, t2_check.py) are consistent with these.

## 6. Single most valuable idea
Pin and close on S^nat_{l''}(l) = S_{l''} \ (F ∪ T(l)) — the signature set minus ALL coarse target coordinates — and let the pigeonhole over
omega(l) + 1 disjoint bands decide, at every level, which rates are robust (pinned diagonally with design x 1/u constants) and which are tiny
(closed exactly at cost o(T_lo^2)); after closing, the zero-cost cone is a generalized configuration on the finite set T(l), so its Hoffman
constant G**(l) is a design constant. Every f-dependent RATE becomes a structural datum; only directional/structural obstructions remain.

## 7. What remains open after Y1 (+ this report), D_X, F finite, g not window-pinned
f such that at all but finitely many levels every clean sub-window violates (SP_w), (Do_w), (Cmp_w) or (NN_w), and f outside the surviving
classes (R_0^pm, R_S, R_BT, Z4 Theorem A'', Z6 Theorem U'):
 (n) wrong-sign nearly neutral kept carriers in one-signed blocks (incl. Z3 Lemma 1.4 carriers) — removable by far pulls + banks (SKETCH);
 (m) mixed blocks neither compensated nor one-signed — rigid ones under Z6 U' (rate K_R); single-block tiny rays by pulls (Y4-ref Cor. P5,
     SKETCH); multi-block rays OPEN;
 (d) aligned corner (no donor) — target donors (Y2-ref), pulls on the peak (SKETCH);
 (h) failure of (SP_w) — Y2 Theorem H; coherent shift resonance OPEN;
 (O4) infinite F.
Most useful next step: WRITE the assembly "master theorem + far pulls + banks" (diagonal U); it would reduce the open core for D_X to
multi-block rays, coherent shift resonance and infinite F. Lemma Z and density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2) remain
OPEN for every admissible T, including D_X.
