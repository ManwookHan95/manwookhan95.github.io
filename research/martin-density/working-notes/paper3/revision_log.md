# Revision log: martin_density_note_III.tex (after referee reports A, B, C)

Build: `paper3/build/` (three pdflatex passes; `build.sh` now reproduces the revised file, since
`final_parts/*.tex` were regenerated from it; the pre-revision parts are in `final_parts_orig/`,
the pre-revision tex in `martin_density_note_III.orig.tex`).
Result: 105 pages, 0 errors, 0 undefined references/citations, no overfull box > 10pt (largest 7.3pt).

Required fixes: 53 (refA 16, refB 21, refC 16), all resolved. Optional suggestions implemented: 23 (listed at the end).

## Referee A (Sections 2 and 3)

| Item | Resolution |
|---|---|
| R1 (Def. 2.27 not exhaustive) | Window paragraph of Sec. 2 now lists (T-a), (W1), (W5), bounded-gap signature sets, [II, Cor 3.20], [II, Subsec. 4.2-4.3, 5.6]; Def. QCreq lists only the new requirements. |
| R2 (Lemma Uscale(a) false) | Def. `def:III-cone`: matrix of Γ♭ formed in active variables only (inactive columns and (X5) rows deleted; cone/Hoffman constant unchanged). Proof of Lemma `weightfree`(a) no longer lists "(X5): unit rows". Proof of Lemma `Uscale`(a) corrected: (X1) rows contain no ratio; ratios enter only via (X3), (X4⁰). |
| R3 (tiny/robust signed) | Labels defined via moduli; "has modulus ≥ u/2" (Step 3) and "≥ u/4" (Prop KNtr(a), its proof, Lemma CMtr(a)). |
| R4 (C_* not a design constant for ratios/statuses) | (QC3): C_*(L):=\|T(L)\|+2 in value units ([II, Def 3.6], (A1) of [II, Thm 5.7]); new C_**(L):=Des(L)^3 bounds ratio vector (Euclidean) and coarse statuses for L ≥ l_f, derived in Step 0 of Prop KNtr; β(b), δ_0 and Steps 0-1 use C_**. |
| R5 ((QC4) lacks β ≤ η'/3) | Clause β(b) ≤ η'(w)/3 added to (QC4); Euclidean norm stated in Lemmas interior, QC, loj and Prop KNtr; Step 0/1/3 use C_** b ≤ β ≤ η'/3; inactive near-threshold carriers of (U)/(KN) blocks pushed *to* relative position ≤ 1-η' (gap ≥ η'M), push size ≤ 2η'. |
| R6 (η_* and move bounds) | η_* ≤ C_f Des η'; cost computation written out (moves ≤ C_f Des² η', ≤ 6L moves, L ≤ Des^{1/2}, counting bound [II, Subsec. 2.3], [II, Lemma 2.12(iv)]) giving C_f Des³ η' log(1/η'). |
| R7 (Lemma floorrow(b) vs Prop KNtr(a)) | Lemma floorrow(b) hypothesis now on block-m coordinates only (proof remark added); Prop KNtr(a) adds \|r''^{(m)}-r(f)^{(m)}\| ≤ 2η' in (T)/(KN) blocks; Section 4 use (proof of Lemma CMtr) cites this. |
| R8 (weak-peak lever in (KN)-block) | Step 4: a weak-peak lever d_0 is first pushed to ϱ = 1-b (value change ≤ 2bϑ̄Φ/m, cost O(b), continuity of ϑ̄, κ via [II, Lemmas 2.7(a), 2.10(a)]); then [II, Prop 5.56] applies. |
| R9 ([II, Thm 5.67] → 5.68) | All eight occurrences replaced; "the proof of [II, Thm 5.68]" where the data construction is meant. |
| R10 (Lemma DC lacks Δ_1) | Δ_1 ≤ r added to hypotheses of Lemma DC(ii); used in step (5); Lemma UE1 proof verifies Δ_1 ≤ r. |
| R11 (circular radius, cert2 C2-7) | A priori pull weight W̄_pull(r_min) defined (monotone, independent of pulls, via prescribed sets Pull_l); r defined with W̄_pull(r_min), r_min:=32K_J T⁴ s_1; actual W_pull ≤ W̄_pull; (FINE), Prop S2c, Lemma LV, Prop BR, Theorem Cmix, Lemma S2ctr use W̄_pull. |
| R12 (pull range in (U6)/Lemma LV(a)) | (U6): pulls from Pull_l for r ∈ [r_pull, r_0]; new hypothesis (PULL) r_pull ≤ 32K_J T⁴ s_1 in Thm UE, Lemma UE1, Prop S2c(ii); Lemma LV(a): Pull_l = S_l ∩ (j(l), s_far] \ F^#, window ratio 2^G with G = 6G(L), r_pull ≤ Des² c_{L+1}², existence argument (≥ 6 elements vs ≤ 5 used); Theorem Cmix records r ≥ r_pull. |
| R13 (c_tiny definition) | c_tiny now sums over (Z) and TU bank coordinates only (Lev⁰_l); pull coordinates enter via W_pull; Lemma LV(c) proof adjusted. |
| R14 (Lemma designadd justification) | Replaced by: lower-bound uses of weights (R, least entry, capacity) computed from c^low after (W_exp); Q(w) ≥ D̄(w)³ imposed after Des fixed; other window conditions monotone. |
| R15 (Lemma CMp(b) estimate) | ‖V_fine‖_1 bound includes C_f c²/t; Γ_w changes by O(c_{L+1}) (cross terms), √Γ_w by O(c_{L+1}), absorbed in the slack of the proof of [II, Thm 5.68]. |
| R16 (kind [1'] containment) | Now: contains kind [1] of [I, Lemma 8.42] (constant 2, no gap ≥ t²); not kind [1] of [II, Subsec. 2.4] (constant 3). |

## Referee B (abstract, Section 1, Section 4, Section 6)

| Item | Resolution |
|---|---|
| R1 | Abstract: two versions of T_fin (option (a) norm c_1 < 1, other Lemma-B conclusions; option (b) norm one, Lemma B); MT VI stated per option. |
| R2 | Abstract: density equivalence for option (a) every N, option (b) N = 1. |
| R3 | Abstract: cushion domination, Sys-DC and transport theorem stated for T^∞_fin. |
| R4 | Intro: "of norm one"; admissibility conditions of [I, Def 1.3] spelled out. |
| R5 | Intro and Sec. 4 opening: "changes listed in Remark Tfincomp, chiefly ..." incl. Q(w) without D̄(w)³ and exponent ω(l)+l²+20. |
| R6 | Intro and Sec. 6 item (1): (T-b)-(T-d); option (b) admissible/Lemma B; option (a) norm c_1 < 1. |
| R7 | Intro: factor 2 sharp, cushion loss linear in the scale r; truncation free only at finitely many fixed scales. |
| R8 | Intro: transport item begins "Let the design be T^∞_fin"; conclusion "lies in Rec(p_N) for p_N built with T^∞_fin"; (H1*), (H2) "at (L,w,a)". |
| R9 | Step-A constant renamed c_A (intro and all Section-5 occurrences); γ_0 = c_A/(4‖h‖_2) defined in intro. |
| R10 | Intro: approximate proportionality with error ε Des(L)/\|κ_Ψ\|. |
| R11 | Verification paragraphs (intro, Sec. 4 opening, Remark cert) rewritten: one referee each for Secs 2-3 + second verification; corrections of the second verification checked once; Prop J, Lemma noB, Cor noB, Lemma nocube one referee; proof uses Lemma nocube, alternative version described; Section 5 dependence on the μ → μ* transfer stated. |
| R12 | Section 4 opening: options inserted for MT VI and the equivalence. |
| R13 | Lemma CMtr(a): realized ratios r'' (active ratios of f^(1a)); proof notes the true shift carries the Step-B change of block scalars. |
| R14 | Lemma PM(iv) rephrased per refa P5 (Ω^# move by ≤ δ_1 + C_lev r and reach nv^#; coarse peaks second order; only fine carriers meet lever coordinates); proof adjusted. |
| R15 | Lemma interface (W2) for k ≥ 2; proof notes stage 1 is excluded and unused. |
| R16 | (W6) chain replaced by the corrected argument (σ > R(k), 2^{R} ≥ 2^{11}/(μ²c²), B_μ ≥ 2^{15}/(μ²c²), B_μ D ≥ 4(ηλ)^{-1}); D(l) := D_room(l) stated. |
| R17 | Prop BR (U3): inward pushes of inactive near-threshold carriers in (KN)/(U) blocks added, with the residue-vs-pull-mass argument. |
| R18 | Lemma partI: Def 3.1, Lemmas 3.2-3.4, 3.6, Lemma 8.27 (eq. (16)) added; sentence for Section-5-only results (Lemmas 1.6, 7.1, 8.7, 8.26, 8.28, eq. (15)) after checking their proofs; resonance example cited as [I, Section 6] and [I, Cor 7.23]. |
| R19 | Remark twodesigns: MT VI for T^∞_fin "not proved here"; base change μ → μ* enters via (B3), (W2), (W6), tuning lemma, verified for μ only. Remark infdep: sentence labelled "Sketch, not verified", final consequence conditional. |
| R20 | Lemma H1suff(i), Def H1, motivating text corrected with ε_k = vs_k sgn(e_k - Δ'_m); Remark later(a) reduced to a pointer. (Cor transport handled per refC R12.) |
| R21 | c_♭ is an f-constant (min of 1 for (U) pushes and c_f of [II, Prop 5.56(b)]). |

## Referee C (Section 5)

| Item | Resolution |
|---|---|
| R1 | Def approxinf(ii): 0 < θ_tr ≤ min(s_1T⁴, r_f(η_1)/(8(1+‖U‖)²)); (M2): ν-clause replaced by ν' ≥ ν_0 - K_wΠ (only form used), f' ∈ B_f shown, Step 4 applies. |
| R2 | (M2) and proof of Lemma deepraise cite Lemma ctrunc(b) / its elementary inequality instead of Lemma masses(ii). |
| R3 | Remark reduction(a): truncated rows satisfy (a) for all r with ε' = 2α(M)+ε''_M; the better bound only at the finitely many scales of Cor LTwin. |
| R4 | Lemma nocubeinf: K_data t (zeroing error explained). |
| R5 | Lemma deepraise(c): unchanged objects / support moduli divided by λ_r / class-cone minors unchanged / others moved by M_f(L)‖U*Δa‖; proof adds tiny ≤ b, robust ≥ u/2 since λ_r ≤ 2. |
| R6 | θ_w := T in Lemma deepraise; Lemma costs: θ_w/(c_f u)² ≤ T^{9/10}/c_f² → 0. |
| R7 | Prop cushion: new items (iv) banks off F (base term ≤ 4Kt\|a^#\| ≤ \|a^#\|/t) and (v) pulled coordinates off F; (U3^inf) on all of supp a^# with C_+ = 5; Lemma prep(c), transport Step 5, Lemma bookkeeping use the same normalization a^#_Z, \|κ\| ≤ Kt, C_+ = 5; (P^#2) describes pulled coordinates. |
| R8 | Lemma prep(a): p*(f^P - f^r) ≤ C_f Des(L) b log(1/b) (closing moves accounted); (b): values move ≤ 2b, rate objects ≤ 2 Lip·b; Lemma costs(b) and Lemma depthclean updated. |
| R9 | val notation: ε_l val_l → val_l in Lemma actions and resource list; orientation text uses vs_k u_k(x̂) = vs_k ε_k val_k. |
| R10 | c_1 → c_A (with refB R9). |
| R11 | Paragraph before Def H1 replaced by explicit statement of the Step-0 variant at arbitrary base support, why Steps 1-3 of Prop KNtr hold for it, and the real reasons (Lemma cone(c) frozen statuses; Thm Aobs \|X̃_m\| ≤ 1/4); transport Step 4 and Lemma depthclean / Def SysA refer to the variant. |
| R12 | Lemma H1suff(i): orientation-correct private resources (far pull iff ε_k = vs_k, depth ≤ Des^C b/u; near bank iff ε_k = -vs_k; (P1) if e_k = Δ'_m; (P3)); Def H1 pull window and bank condition corrected; proof rewritten (move sizes, efficiency (μ*_j)², overshoot within (I5)); Cor transport proof uses far pull or near bank according to orientation, with the depth bound. |
| R13 | Lemma H1suff(ii): Sherman-Morrison only for (P4) pushes at distinct private thick near coordinates; shared design-depth moves require a right inverse of norm ≤ Des^C/u. |
| R14 | Def H1: "Equivalently" replaced by a one-directional sufficient condition (x replaced by 2b, W ≤ Des^C b/u). |
| R15 | Def residual: single condition (A*/U*) with per-certificate type; Prop residual and its proof, intro, abstract, Section 5 opening, Section 6, Remark residual updated. |
| R16 | Remark infdep rewritten (base independence not re-verified; MT VI for T^∞_fin expected but not verified; consequence conditional); Section 5 opening states that from Subsec. cushion on the operator is T^∞_fin and the first half of the equivalence is not verified. |

## Optional suggestions implemented (23)
refA: O1 (Lemma EC proof), O3 (Remark kind3 citations), O4 (μ_κ wording), O7 (blocks with an active component), O9 (Lipschitz constants of rate objects only finite), O11 (inactive weak peak ⇒ (KN)), O15 (chain in Lemma UE1 proof), O19 (E_l remainder O((r+\|P\|)\|P\|)), O21 (pigeonhole rests on Q ≥ D̄³).
refB: O3 (D(l) := D_room), O4 (admissible operators), O5 (Remark count(A) labelled sketch, P(L) ≤ Des^{1/2}, (2L+1)9^L ≤ B), O7 (abstract qualifier), O8 (Section 6 items (3), (4), Problem Astar), O9 (Remark Tfincomp(b) tiny/robust), O10 (C_f depends on N), O12 (Lemma LV(d) in the list of false earlier statements).
refC: O4 (K_J := K_lev; (W-b) replaced by (DC); (PULL) void), O8 (2^{s_t+1} ≤ Des), O9 (bookkeeping ratio ≥ c_f n^{1/4}), O10 (approximate proportionality, which row), O13 (opening item (1)), O16 (Remark later(a) pointer).

## Unresolved / caveats
- No required item left open. The new corrections of this round were made once and have not been independently re-verified (stated in the Verification paragraphs).
- MT VI for T^∞_fin (base change μ → μ*) stays unproved; it is labelled as expected/sketch only (Remark infdep, Remark twodesigns), as the referees required.
- Two details rest on statements of the sources without a separate in-paper proof: "(1a) uses at most five elements of each S_l" (Lemma LV(a), from cert0 P4 / refB check) and the factor B*(L) of Des(L) in Part II bounding 2^{s_t(L)+1} (Lemma deepraise, per refC O8).
- Optional items not implemented: refA O2, O5, O6, O8, O10, O12, O13, O14, O16-O18, O20, O22; refB O1, O2, O6, O11, O13; refC O1-O3, O5-O7, O11, O12, O14, O15.
