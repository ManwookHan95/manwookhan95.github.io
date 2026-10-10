# Revision log: martin_density_note_II.tex (response to referee reports A, B, C)

The revised source is `paper2/martin_density_note_II.tex`. It is edited directly. The pre-revision file is saved as `paper2/orig/martin_density_note_II.prerevision.tex`.

The section files `s2.tex`–`s6.tex` and `build/parts/*` predate this revision and are stale. `build/assemble.sh` has been disabled (it now exits immediately) so that it cannot overwrite the revised file.

Build: three pdflatex passes in `paper2/build/` give:
- 144 pages;
- 0 errors;
- 0 undefined references or citations, and no LaTeX warnings;
- 4 overfull boxes, all under 10pt (largest 6.4pt).

Required items: 39 (A: 8, B: 16, C: 15). All 39 are resolved. Optional items carried out are listed at the end.

---

## Referee A (Sections 2–3)

- **A-R1 (Remark after Lemma RT: footprint of corrections).** Replaced the paragraph with a new `Remark [Raise with corrections]` (`rem:II-RTcorr`).
  - It states the hypotheses: F₀ ⊆ F∖supp Δa, |Δa''_j| ≤ |a_j|/2, D = Δa + Δa'', λ = q*(a+D) ≥ 1.
  - It notes that f^# is well defined because supports and signs are kept.
  - It gives the corrected bound with 2‖U*D‖ + 2‖Δa''‖₁, with its derivation and the extra error ≤ 2q*(Δa'')/λ.
  - The two citations in Section 6 now point to this remark.
- **A-R2 (Theorem NL overclaimed).**
  - The theorem is retitled "A criterion for the failure of lower semicontinuity along block-tame rows".
  - The paper already contains a complete realization for T_final, N = 1 (Proposition `prop:II-NLreal`, refereed OK by B). The introduction, the Section 2 overview and Remark NL now point to it.
  - Remark NL now separates the proved case (T_final, N = 1) from the general signature-ladder case. The general case is labelled "Sketch, not proved here" and its consequence is conditional ("for any such design for which the construction is granted").
- **A-R3 (G\*, H_comb, Ξ^Y undefined).**
  - G\*, H_comb and Ξ^Y are deleted from Des(l), from (K1) and from Definition II-constants(d). The sentence "recalled where they are used" is removed.
  - G\*\*(l) is now defined explicitly in Definition II-constants(d), through the box systems Z_κ(β), with G\*\* ≤ H_conf.
  - Definition II-pattern refers back to that definition.
- **A-R4 (δ_sh not a design number).**
  - New Definition II-constants(e) defines c^comb(δ; κ^sh, vs) for every enlarged shift pattern and every sign vector vs ∈ {±1}^{G_pk}. It uses no 1_{F^c}, with L evaluated on T(l)∖F′ and coef on S_{l''}∖([1,l]∪T(l)).
  - δ_sh(l) is the least positive value of c^comb_* over all pairs (κ^sh, vs), and 1 if there is none. It is a design number.
  - In Section 5 the "we read δ_sh as" paragraph is replaced. It now cites the definition and adds the identification argument: for l ≥ l_f ≥ max F and F′ = F ∩ T(l), the f-dependent cost with Π_m 1_{F^c} coincides with the design one.
- **A-R5 (norm of Lip(l)).** Lip(l) is now a Lipschitz constant for ‖·‖_∞ on ℝ^{[1,l]} on the cube, and it exists because polynomials are Lipschitz. Theorem B Step 2 now notes ‖v′−v‖_∞ ≤ ‖v′−v‖₂. This also resolves B-R5.
- **A-R6 (i ≥ 0 in the introduction).** Changed to i ≥ 1.
- **A-R7 (FD targets "removable").** The claim is deleted. Remark scope (c) now says the FD targets are also used for s_max(l) → ∞ (Lemma scales(e)) and in D^{U1′}, and that no removability is claimed.
- **A-R8 (Corollary Rkt, last assertion).** Added the uniqueness proof: G(a) = a² − (a+c₀)²R² − c₀ is strictly increasing on {a > c₀R/(1−R)} = {a > 𝗄R}. So a, 𝗄 and ϱ_k are determined by (R, Φ_P², s_Q). The proof also points to Proposition Rkt(i).

## Referee B (Sections 4–5)

- **B-R1 (Theorem B status clauses).**
  - (A2) is replaced by the precise table: kept carriers are strict non-peaks, and robust coarse peaks of f (ϱ ≥ 1+u) remain peaks with margin ≥ u/2.
  - Conclusion (a) is replaced by the full status table. Every coarse carrier with |ϱ−1| ≤ C_\*b becomes a strict non-peak, in particular every tiny-margin peak, kept or dropped. Nothing else is asserted about dropped carriers.
  - Step 4 is rewritten:
    - donor case: Lemma status (b)–(d), with the threshold rise ≥ c_fΛ ≫ C_\*b;
    - no-donor case: Lemma QB(b) applied with L = all coarse carriers of the block.
  - The paragraph after the proof and Definition II-Gamma are updated.
- **B-R2 (buffer push not realizable by Lemma TU).** Step 3 is rewritten:
  - the push of size s ∈ [s_m, 2s_m] is realized first: by a pull or bank (class G, after (C1)) or by a z-move or close-and-bank (class R, as in (C3));
  - it then enters Lemma TU as base data, with L₀ = Kp; (T2) is unaffected.
  - s_m is fixed from a priori bounds X̄, Ē, so there is no circularity.
  - Step 4 uses s ∈ [s_m, 2s_m], and Step 5 is updated.
  - The paragraph after Lemma buffer is corrected.
- **B-R3 (cost bound not in Lemma TU).** Step 5 now uses Lemma TU(c) mass bounds plus Lemma cost, as in Lemma compcost(e).
- **B-R4 (h₀ bound).** Changed to h₀ ≥ min(1, A_m/(2l)), with the reason, and C₁(s+E) < h₀ is checked for l ≥ l_f.
- **B-R5 (Lip norm).** See A-R5.
- **B-R6 (G_np excluded dropped non-peaks).** G_np := E∖G_pk, so dropped carriers are included. This is done in Definition constants(e) and in Section 5.
- **B-R7 (G_pk undefined).**
  - G_pk is now the class-G coarse carriers that are peaks of f with ϱ ≥ 1+u(w). Tiny-margin peaks are in E∖G_pk, and cleanness shows there are only these two kinds.
  - The proof of Lemma R17 uses "l″ ∈ G_pk (relative margin ≥ u)".
- **B-R8 (Proposition constcontact).** It is now stated for T = T_final. A new Remark `rem:II-constcontact` records that the first part of the proof works for any admissible operator with disjoint signature sets.
- **B-R9 (SAmates normalization).**
  - "β⁺(ξ) = 0" is replaced by "b⁺(ξ) = 0", i.e. β⁺(ξ) = −q₀Δ_αλΣχ_j|V_j|.
  - A tangency paragraph is added to the proof: ẑ = z off F; V(ẑ) = 0 because ψ(ẑ) = A; and g(ξ) = 0.
  - The same normalization is required in the proof of MT IV′ (also B-O8).
- **B-R10 (Baire, ε_l).** The statement now reads "if ε_l → 0", and the proof uses s_l := q₀Φ_lε_l/m.
- **B-R11 (Lemma zerovalue left endpoint).** Statement and proof are rewritten.
  - Statement: for every θ_a ∈ (0, λ_a] there are signs σ_r, depending on θ_a, and m₀ ∈ [θ_a, θ_a + c_p²] with u_a(ẑ) = 0.
  - Proof, left endpoint:
    - Tg is evaluated at m₀ = θ_a, and is independent of σ because ν depends only on the moduli;
    - ẑ_{p_r} = σ_r(1+e_r), with e_r ≤ e := (μ\*_{p₀})^{2^{2^{p₀}}−1} < 2^{−R};
    - the signs are chosen around the shifted target Tg − 2^{3−R}, so Ψ(θ_a) ∈ [−2^{4−R}, 0).
  - Proof, sweep:
    - the ν-mediated changes are explicitly bounded;
    - c_p ≥ c^low_p is proved;
    - the sweep is at least 2^{7−R}.
  - Definition D^{U1′}:
    - p₀ is chosen so that (μ\*_{p₀})^{2^{2^{p₀}}−1} < 2^{−R} (well founded);
    - c^low reads (W5) with δ^max/2.
  - Part (ii) uses the same left-end rule.
  - The lemma states that it is used for absorbers of late stages, which is f-dependent and is how it is applied.
- **B-R12 (D^{U1′} circular and N-dependent design factor).**
  - D_cls is deleted from Des(L).
  - Definition DU1 introduces design numbers:
    - R_Γ(L) = 2|T(L)| + 11L;
    - P(L) = 2^{R_Γ(L)};
    - D̄(w) = (2L+1)3^{2L}(Des(L)/u(w))^{C_Γ(P(L)+2L+2)}.
  - At main stages Q(w) := max{Q(w), D̄(w)³}. The Section 3–5 window arguments use only lower bounds on Q.
  - Lemma classes:
    - J ≤ 2L, because N ≤ L for L ≥ l_f;
    - K_\* ≥ max{2Des, 4C_f Des·J·H(L)}, with K_\* ≤ (Des/u)^C;
    - the zeroing cost (1 + C_f Des J A_i)Kt is proved;
    - the bounds by D̄ are proved.
  - Proposition ray (a), (b) use the bound (1 + C_f Des J A_{i(t)})Kt. In (d), D_cls ≤ D̄ is proved, with p ≤ P(L).
  - The "K" convention paragraph is rewritten so that constants are absorbed directly through Q ≥ D̄³.
  - MT IV′ (statement and proof) and Corollary MTIVintr now use D̄(w) and the corrected projection bound.
- **B-R13 (free ray for r < 0).** The definition now requires each affected row in T(l)∖F to be satisfied for every x_k ≥ 0. The proof says "changing x_k within [0, ∞)".
- **B-R14 (necessity claims).**
  - Remark openS (S1) and (S2a′) are relabelled "heuristic", with no claim of necessity.
  - Remark C6 now says that, under the hypotheses of MT IV′, (g3) in configuration (i), (g4) and (g5) are closed, and that whether a second lever is necessary is not decided.
  - The introduction and Section 7 are aligned (see C-RC9).
- **B-R15 (Corollary B1 coefficient bound).** Replaced by the homogeneity argument: rescale the (Z5) row by A^#_m/A_m ∈ [½, 2]. This gives |q^# A^#/A − q| ≤ C_f η. The false bound is noted.
- **B-R16 (summary after Lemma Dprime).** Restricted to source-deficient blocks at that clean sub-window.

## Referee C (abstract, Sections 1, 6, 7)

- **C-RC1 (θ_\* fixed, η′ ↛ 0).**
  - θ_j := θ_\*/l_j is used in RS Step 1, RS\* Step 1″ and RSinf (iv). Hypothesis (d) of ERT still holds because θ_j ≤ θ_\*.
  - The depth estimates are updated.
  - RS Step 3 now gives η′_j ≤ (λ_j−1)λ_j² + 2θ_j c_♭² + O(ε_e/t) → 0, with the reason.
  - RS Step 4 and RS\* explain how (1+η′_j) enters [I, Lemma 8.7(d)], so Γ_w ≤ 1+η₀/2 holds for large j.
  - Lemma Winf's conclusion is now Γ ≤ (√((1+η′)(1+η_Γ)) + C″K_top t)², and the proof says how this is obtained.
  - RSinf (v) adds that η′_j → 0 gives Γ ≤ 1+η₀/2.
- **C-RC2 (RSinf last sentence false).** Replaced. For finite B the rates are f-constants and (W_inf) implies (W⋆), because Ξ_f ≥ 1+K_\* ≥ Λ⋆_f. Finite B is covered by RS\* and ND′ under (W⋆).
- **C-RC3 (RSinf circularity, K_top bound, VP radius).**
  - (a) K_top(J), P(n,J), x(n,J) and J(n) are now defined in order. J(n) is the least J ≥ 1 + max F₀ with μ\*_J ≤ x(n,J)², which exists by double-exponential versus linear growth. n_j is then the fixed point.
  - (b) The bound is corrected to K_top ≤ (1+s_max)(4Hl+3)^{l+1}(K₁+K^pk), with the unrolling argument. The final estimate survives via (1+s_max)2^{s_max}/δ_min ≤ 2Ω_K.
  - (c) Lemma VP now states C₀ ≥ 1 and a quantitative radius c₀ ≥ c_f min{1, min|a_s|}/(1+C₀)², with c_f depending only on ν. A new proof step (iv) gives a contraction argument. RSinf (iv) checks that the footprint is ≤ c_f/(1+C_VP)².
- **C-RC4 (Theorem A: Lemma Uinf needs Γ ≤ 2).** ρ₁ is fixed first, and Lemma Uinf is applied to the scaled data ρ₁(b^± − κ_y a, ω^±), whose Γ is < 1. Step (3) is adjusted. Also, per OC3, p\*(g−g_y) = O(ε_e log(e/ε_e)).
- **C-RC5 (Lemma DR, λ_r ≤ 2).** Added the hypothesis ‖Δa‖₁ ≤ ½ to the "Consequently" clause, with the reason in the proof. The application notes that ‖Δa‖₁ ≤ ψ(J) ≤ ½.
- **C-RC6 (profile classification).** Now restricted to bounded-gap signature sets with S_l∖F finite. The sparse case is noted to hold for every S_l, and lacunary sets are noted as possible counterexamples for β₀ ≥ 1.
- **C-RC7 (Remark RS(b)).** The interpretation is now labelled "Heuristic". (Also OC2: "for these profiles it is not o(T_j²)".)
- **C-RC8 (missing hypotheses; rows versus pairs).**
  - The abstract, the introduction and the Section 6 introduction now add (W⋆), (H2), (H3-inf) for R1/RS/RS\*/ND′ and (SC_I), (W_M) for Theorem N.
  - Remark residualinf(a) is split into "Rows" and "Pairs", with all hypotheses, including V_f of sparse profile and ρ²κ_w < 1, (ND′_{L₀}).
  - Section 7(c) now says "rows … in Rec and pairs … in cl NA".
- **C-RC9 (necessity claims).**
  - Introduction: "A lever is needed in this route … (Remark onelever; no claim that a one-lever argument cannot succeed)".
  - Section 7: "this route needs a second, ϰ-neutral lever".
  - Problem S2: "uses d-consistency because …; that the mismatch cannot be rebalanced is heuristic".
- **C-RC10 (Problem KN ill posed).** Reformulated as "Is f ∈ Rec?", with the two routes: a peak with excess O(Kt/λ_d), or a ϰ-neutral lever. A parenthesis explains why d cannot be kept below threshold.
- **C-RC11 ("exactly when (ND′) fails").** Changed in Problem tuning and Remark Minf to "vanishes in particular when (ND′) fails; the converse is not claimed".
- **C-RC12 (Problem SCdeep).** Re-attributed to shifted (non-d-neutral) data, inside (C\*) at infinite F and in the open extension of Theorem A. Theorem A itself uses no (SC).
- **C-RC13 (Remark statusother).** Restricted to *block-tame* approximating rows, with nothing proved for other rows, and pointed to Proposition NLreal for the existence of such mates.
- **C-RC14 (Remark R1(d) cross-reference).** Now cites Theorems RS\* and ND′, with the hypotheses and the reason (failure of ND′). It is labelled "proved in our sources, not reproduced here" (also OC16).
- **C-RC15 (Ξ_f can vanish).**
  - C₀ ≥ 1 is taken; C_VP(l) := 1 if F₀ = ∅; so C_VP ≥ 2^{max F₀} ≥ 1.
  - γ_B and μ_B are capped at 1.
  - Ξ_f now uses (1 + C_VP).

## Optional suggestions also carried out

- **Referee A:**
  - O1: companion in Remark quantifiers.
  - O2: Remark resonance(b), with the exact sign conditions.
  - O4: Remark VT numerics labelled "numerical evidence", and "order up to".
  - O5: Remark cost "cannot in general", with the evidence labelled.
  - O6: introduction, "(T-a)–(T-d), (P1)–(P3)".
  - O7: Łojasiewicz case with empty zero set.
  - O8: Lemma raise(e) phrased as an assumption.
  - O10: Proposition bank(a), general condition s_max(l) < 2^l.
  - O11: (GW3) quotes |θ^±| ≤ 3λ/t.
  - O12: overfull box at the level-data display.
- **Referee B:**
  - O1: Remark onesigned, via Lemma scales.
  - O3: Lemma R17 cites Step 1 of Proposition transplant.
  - O4: (A1) from compcost(b) plus Lemma cost; gap^# ≥ gap stated in Step 4.
  - O7: SAmates (ii) without "l₋ late".
  - O8: β normalization in the proof of MT IV′.
  - O13: K_U + lK_pin.
- **Referee C:**
  - OC2, OC3 (with RC4 and RC7).
  - OC4: D_j not a raise, in RS Step 2.
  - OC5: Hoffman constants within a factor tending to 1.
  - OC7: Proposition kernel runs the proof of Winf.
  - OC10, OC11: introduction and abstract.
  - OC12: Remark residualinf(d) labelled an interpretation.
  - OC13: Section 7(b) for D^{U1′}.
  - OC14: Problem mix reformulated.
  - OC15: "constant of modulus 1".
  - OC16 (part): Remark R1(d).

The remaining optional items are not done. They are A-O3, A-O9, B-O2, B-O5, B-O6, B-O9–O12, C-OC1, C-OC6, C-OC8, C-OC9, and the rest of C-OC16 (Remark transferinf(c)).

## Unresolved or to note

- No required item is left unresolved.
- Points where a check would be useful:
  - **B-R11.** The new Lemma zerovalue is stated for absorbers of late stages, which is an f-dependent condition (2μ\*_{p₀} ≤ ν₍₁₎/4 and 160λ_a² ≤ ν₍₁₎²/2). This is how Proposition absorb and MT IV′ use it, but those proofs were not re-read line by line for this point.
  - **B-R12.** Replacing Q(w) by max{Q, D̄³} at the main stages of D^{U1′} relies on the claim that the window arguments of Sections 3–5 use only lower bounds on Q(w). This holds for the instances checked: Lemma scales(b), the subwindow arithmetic and GW. It was not re-verified for every occurrence.
  - **A-R2.** The fix rests on the existing Proposition NLreal (T_final, N = 1). The general signature-ladder realization stays a labelled sketch.
