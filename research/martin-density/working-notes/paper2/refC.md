# Referee report C on `martin_density_note_II.tex`: abstract, Section 1, Section 6, Section 7

Scope: the abstract (lines 36–66), Section 1 "Introduction" (70–307), Section 6 "Infinite base support" (7684–10070) and Section 7 "Status and open problems" (10071–10313).

Sources compared line by line:
- r5/Z5 (+ Z5_referee, Z5_ref_notes: Lemma R0, Lemma R2, Theorem R1, Lemma R3, T14/T15 corrections);
- r6/Y3 (+ Y3_referee, Y3_ref_notes: precisions 1.1–1.5, Remark 3.6(b) correction, Prop. 3.4);
- r7/V3 (+ V3_referee, V3_ref_notes: (ND′) fix, Theorem RS′ with (H3-inf) and L₀ = B_np, inspection items I1–I3, Theorem A without |b^θ|, M_inf reduction, the FALSE Remark 3.5(e));
- r8/U2 (+ U2_referee, U2_ref_notes: Lemma P, RS*, Lemma ND / ND′, Lemma W + Fix 1, RS*_inf, Fix 3–Fix 6, M-inf SKETCH);
- r8/U4 (+ U4_referee);
- ADDENDA 4–8 of BRIEFING_R2.md;
- for Section 7, also r8/U1 + U1_referee/U1_ref_notes (Lemma R-kt, the gap in MT IV) and r8/U3 + U3_referee/U3_ref_notes (F6, Theorem NL).

Part I numbering: I compiled Part I (refA_work/partI aux) and checked every `[I, …]` reference in my sections. All of them point to the intended statement. Examples: 5.8 = thm:transfer, 8.17 = thm:windowed, 8.28 = lem:flip, 8.29 = lem:boundedfree, 8.46 = rem:Binf, 1.16 = lem:pair, (15) = eq:DeltaB, (16) = eq:peakshift. The build log has no undefined references.

## 0. Verdict

**Section 6** is mathematically sound in its main lines. I re-derived the following:
- truncated canonical approximants and transfer peaks at a ∉ c₀₀;
- the flip calculus and the oscillation lemma;
- Lemma Uinf;
- bounded free switching at any F;
- un-switching;
- the raised and flip-extended engineered recovery;
- the windowed master theorem;
- the exact one-sided coefficient at arbitrary F;
- the clamped certificate and Theorems B*-inf / B-inf / B±-inf / cushion room;
- Lemma R0, exact switching at arbitrary F, the common-shift lemma and Theorem R1 (Claim 3.1 of Z5-ref in every case);
- Theorem N (all five steps);
- Lemma VP (with (ND′));
- the proof structure of Theorems RS, RS*, ND′, RSinf;
- Lemmas P, ND, Winf, DR and TR;
- Propositions Minfred and LSC.

All referee corrections of Z5, Y3, V3 and U2 are present:
- Z5-ref R1/R2;
- the (W^c) gloss;
- Y3-ref 1.2/1.3/1.5;
- V3-ref (ND′), (H3-inf), L₀ = B_np, W without |b^θ|, and Remark 3.5(e) removed (Remark RS(c));
- U2-ref r1/r2, Fix 1 (1/μ_B in (W_inf)), Fix 3 ((O6) invariant), Fix 5 (Prop. kernel), Fix 6 (tuning residual not described by (NDN) alone), and D2 ((O9) excluded).

Nothing that a referee found wrong appears as proved:
- not U1's MT IV / Cor IV.1 (Section 7 says explicitly that this conclusion is not proved);
- not U3's (S2a);
- not Y4's (UN+);
- not Z1's exposed-face consequence.

Lemma Z and density are nowhere claimed. The transport of MT III′ to infinite F is labelled a sketch.

But there are genuine defects:
- **One gap shared by three theorems (RC1).** RS, RS* and RSinf replace the sources' θ_j → 0 by a fixed θ_*. They then still claim the budget η′_j → 0, which no longer follows. Lemma Winf states its Γ bound without the budget factor.
- **A false statement inside a theorem (RC2).**
- **Circular definitions and a false intermediate bound in RSinf (RC3), and a rate Ξ_f that can vanish, which makes (W_inf) vacuous (RC15).**
- **Hypothesis mismatches (RC4, RC5).**
- **A false classification paragraph (RC6).**
- **An unlabelled heuristic (RC7).**
- **A wrong cross-reference (RC14).**

**Sections 1 and 7 and the abstract** have no mathematical errors of the kind above. They do have overclaims:
- hypotheses omitted in summaries (RC8);
- necessity claims that the paper itself disclaims (RC9);
- one ill-posed open problem (RC10);
- an "exactly when" that the sources do not support (RC11);
- a misattribution (RC12);
- an overgeneralization of Theorem NL (RC13);
- a wrong cross-reference in Section 6 (RC14).

**Number of REQUIRED fixes: 15 (RC1–RC15).**

In addition, two required fixes in my scope were already raised by referee A; I do not count them again:
- Introduction lines 176–177 (Theorem NL advertised as an established failure) = refA R2;
- Introduction line 184 (i ≥ 0 should be i ≥ 1) = refA R6.

RC9 overlaps with refB R14, which concerns the analogous sentences in Section 5.8.

Optional suggestions: 16 (OC1–OC16).

---

## 1. REQUIRED fixes

### RC1. Theorems RS, RS*, RSinf and Lemma Winf: the budget at the companion is claimed to tend to 1 but does not (lines 9119–9123, 9171–9172, 9374, 9401–9403, 9562, 9574–9575, 9671–9673)

Quotes:
- Theorem RS, Step 1: "Choose m_j ∈ ℕ minimal with C_R T_j^ε log(e/T_j) ≤ θ_* c_♭² 4^{−n_j}".
- Step 3: "p^*(f_j+tg_j) ≤ 1+(t²/2)(1+η′_j) for t ∈ [T_j 2^{−n_j}, T_j], with η′_j → 0."
- Theorem RS*, Step 1″: "x_j(n) := θ_* c_♭² T_j 4^{−n}/C_e".
- Theorem RSinf (iv): "x(n) := θ_* c_♭(l_j)² γ_B(l_j) μ_B(l_j) 2^{−2(L_j+P+n)}/(C_e(1+C_VP(l_j)))".
- Lemma Winf: hypothesis "η′ ≤ 1"; conclusion "Γ_w(b^±,ω^±) ≤ (√(1+η_Γ(η)) + C″_f K_top t)²".

Problem.
- With a fixed θ_* = (1−ρ²)/(12ρ²), the choice of m_j (resp. J) gives only ε′_j ≤ θ_* c_♭² (T_j 2^{−n_j})².
- Hence, for t ∈ [T_j 2^{−n_j}, T_j], Corollary RT yields η′_j ≤ (λ_j−1)λ_j² + 2θ_* c_♭² + O(ε_e/t). The middle term is a fixed positive number, so η′_j does not tend to 0.
- With m_j minimal, the bound ε′_j ≤ C_R T_j^{2+ε} log(e/T_j) is within a factor 2^ε of θ_* c_♭² (T_j 2^{−n_j})². So nothing else forces ε′_j/t² → 0.
- The sources choose θ_j → 0:
  - V3 Step 1: "θ_j → 0";
  - V3-ref (I1): "η′_j ≤ (λ_j − 1)λ_j² + 2θ_j + O(ε_e/t) → 0";
  - U2 Step 1″: "θ_j := 1/l_j".
- The paper replaced θ_j by the fixed θ_* of its Theorem ERT. That is legitimate for hypothesis (d) of ERT (refA verified ERT), but it breaks Step 3.
- Consequence. Lemma budget(d) of Part I, run with the budget (1+η′)t²/2, gives Γ_w(B_±,Θ_±) ≤ (1+η′)(1+η_Γ(η)), not ≤ 1+η_Γ(η). So:
  - the bound "Γ_w ≤ 1+η₀/2" for the window data in RS Step 4 is not justified;
  - the same holds in RS* Step 4′ and in the conclusion of Lemma Winf (which assumes only η′ ≤ 1);
  - consequently local validity with (1+η₀) in hypothesis (b) of Theorem ERT is not justified either.
- Since c_♭ ≲ ε_tr = η₀/2, the argument might be rescued by bookkeeping, but the paper asserts η′_j → 0, which is false as written.

Change.
- (a) In RS Step 1, RS* Step 1″ and RSinf (iv), replace θ_* by θ_j := θ_*/l_j:
  - "C_R T_j^ε log(e/T_j) ≤ θ_j c_♭² 4^{−n_j}";
  - "x_j(n) := θ_j c_♭² T_j 4^{−n}/C_e";
  - "x(n) := θ_j c_♭(l_j)² … /(C_e(1+C_VP(l_j)))".

  Then hypothesis (d) of Theorem ERT still holds, because θ_j ≤ θ_*. Also ε′_j/t² ≤ θ_j c_♭² → 0 on 𝒮_j, so η′_j ≤ (λ_j−1)λ_j² + 2θ_j c_♭² + O(ε_e/t) → 0, as in V3-ref I1.

  Update the depth estimates accordingly. In RS: "m_j = O((n_j + log(l_j/(θ_* c_♭²)))/ε) = o(n(w_j))". In RS*: "2^{J_j(n)} ≤ 2 log₂(2(L_j + 2n + log₂ l_j + C))". Both are still absorbed by the window.
- (b) In Lemma Winf, either replace "η′ ≤ 1" by "η′ ≤ η′₀", with η′₀ so small that √(1+η′₀)(1+κ₀) ≤ 1 + 3κ₀/2, or keep η′ ≤ 1 and state the conclusion as

  Γ_w(b^±,ω^±) ≤ (√((1+η′)(1+η_Γ(η))) + C″_f K_top t)².

  Then in RSinf (v) add: "since η′_j → 0 by the choice of θ_j, the data satisfy Γ_w ≤ 1+η₀/2 on 𝒮_j for large j."
- (c) In RS Step 3, replace "with η′_j → 0" by "with η′_j ≤ (λ_j−1)λ_j² + 2θ_j c_♭² + O(ε_e/t) → 0 (choice of θ_j in Step 1)".

### RC2. Theorem RSinf: the last sentence of the statement is false (lines 9651–9653)

Quote: "For finite B all factors of Ξ_f other than 1+K_⋆ are f-constants, and (W_inf) reduces to (W⋆)."

Problem.
- Ξ_f(l) = (4H(l)l+3)^{l+2}(1+K_⋆(l)) C_VP(l)/(γ_B(l)μ_B(l)). For finite B the factors H, C_VP, γ_B and μ_B are f-constants for large l. The factor (4H(l)l+3)^{l+2} is not: it grows like (Cl)^{l+2}.
- (W_inf) is therefore strictly stronger than (W⋆) in general. Choose the rooms r⋆_l (which are arbitrary positive numbers determined by z on the signature sets) so that Λ⋆_f(l)/(l 2^{l³} Λ°(l)) ≍ 1/l². Then (W⋆) holds and (W_inf) fails.
- U2's Remark 2.3(b) says only that the *rates* are f-constants for finite B. Finite B is covered by Theorems RS*/ND′ under (W⋆), with thresholds indexed by |B| instead of l.

Change: replace the sentence by "For finite B the rates H, C_VP, γ_B, μ_B are f-constants for large l, and (W_inf) implies (W⋆). Finite B is covered under (W⋆) alone by Theorems RS* and ND′." The implication (W_inf) ⇒ (W⋆) uses K_⋆ ≥ Λ⋆_f together with C_VP ≥ 1 and γ_B μ_B ≤ 1. The first of these is guaranteed only after the normalization of RC15, so state the normalization before this sentence.

### RC3. Theorem RSinf, proof (iii)–(iv): a circular definition, a false intermediate bound, and an unchecked radius (lines 9665–9693)

(a) **Circularity.** Quotes:
- (iii): "some p ≤ P := (s_max(l_j)+2)(n + log₂ K_top + 2)";
- (iv): "x(n) := θ_* … 2^{−2(L_j+P+n)}/…, J°(n) := min{J : μ*_J ≤ x(n)²}, J(n) := max(J°(n), 1+max F₀)".

Here:
- K_top = K_top(l_j, J) depends on J through K₁;
- P depends on K_top;
- x depends on P;
- J(n) depends on x.

So P, x(n) and J(n) are defined in terms of each other, and the existence argument given ("the right side depends on n only through 2^{J°(n)} and log₂ K_top, which grow logarithmically") does not resolve this.

Change: define, for (n, J), the quantities K_top(J), P(n,J), x(n,J) and J°(n,J) in this order. Then take for each n the least J ≥ 1 + max F₀ with μ*_J ≤ x(n,J)². It exists, because μ*_J = 2^{−2^{2^J}} while log₂(1/x(n,J)) grows only linearly in J. Then take the least n with n ≥ A K_top(J(n))/c_♭(l_j). This is the fixed point J → K_top → n → P → x → J° of U2-ref §4.

(b) **The intermediate bound.** Quote: "Using K_top ≤ (4H(l_j)l_j+3)^{l_j+2}(K₁+K^pk)".

This is false whenever s_max(l_j) ≫ H(l_j) l_j, because the recursion K_{i+1} = 4H(K^pk + l K_i + s_max K₁) + 2K_i contains the term s_max K₁. A random test (refC_work/ktop_check.py, 2·10⁵ instances) found the stated bound violated in 39% of the cases. The correct bound, by unrolling K_{i+1} ≤ (4Hl+2)K_i + 4H(K^pk + s_max K₁), is

K_top ≤ (1+s_max(l_j))(4H(l_j)l_j+3)^{l_j+1}(K₁+K^pk).

The same test found no violation of this bound. The displayed conclusion n_j + P_j ≤ C Ξ_f Ω_K s_max log₂ n(w_j) survives, because Ω_K(l) = s_max 2^{s_max}/δ_min already contains s_max. Correct the inequality and say so.

(c) **The VP radius.** Lemma VP requires ‖U*Δa‖ ≤ c₀, where c₀ = c₀(L₀) depends on L₀ = B_np(l_j), which grows with j. The proof checks only the conditioning constant C_VP(l_j), never c₀(l_j). Change:
- add to Lemma VP the quantitative radius c₀ ≥ c_f/(1+C_VP)². It follows from the quantitative implicit function theorem: the second derivatives of G are bounded by C/ν², a right inverse of D_xG has norm ≤ C₀, and |x_s| ≤ |a_s|/2 needs C₀‖y‖ ≲ min_{F₀}|a_s|;
- note in (iv) that ‖U*Δa‖ ≤ Cμ*_{J(n)} ≤ Cx(n)² ≤ c_f/(1+C_VP)² for C_e large (U2-ref W5).

### RC4. Theorem A: Lemma Uinf is applied outside its hypothesis Γ ≤ 2 (lines 9265–9270)

Quote: "Lemma II-Uinf at f_y (U_*=0, C_+=4, …) gives p^*(f_y+rg_y) ≤ 1+(r²/2)(Γ^{(y)}_w+ε_tr)".

Problem.
- (OS1) of Lemma Uinf requires Γ^{(j)}_w(b,ω) ≤ 2.
- The data of Theorem A only satisfy Γ^{(y)}_w → Γ_w(b^±,ω^±) ≤ κ_w < 1/ρ². This exceeds 2 when ρ < 1/√2 and κ_w ∈ [2, 1/ρ²).
- The source (V3 Theorem A via Lemma R2) has the same unstated restriction.

Change (simplest): in step (2), apply Lemma Uinf to the scaled data ρ₁(b^± − κ_y a^{(y)}, ω^±). These have Γ ≤ ρ₁²(κ_w + o(1)) < 1 ≤ 2. The resulting bound p^*(f_y + rρ₁ g_y) ≤ 1 + (r²/2)(ρ₁²Γ^{(y)}_w + ε_tr) is exactly what step (3) uses. (Alternatively, state Lemma Uinf with "Γ ≤ Γ_max", the constants depending on Γ_max.)

### RC5. Lemma DR, the "Consequently" clause needs λ_r ≤ 2 (lines 9791, 9802–9805)

Quote: "λ_r := q^*(a+Δa) ∈ [1, 1+2‖Δa‖₁] … Consequently, if w is a clean sub-window of level l for f and M_f(l)‖U*Δa‖ ≤ b(w)², then every object of (O1)–(O8), (O10)–(O12) that is tiny at f has value ≤ 2b(w) at f^r, and every robust one has value ≥ u(w)/2."

Problem.
- By (a), the (O10) values at f^r are those at f divided by λ_r.
- A robust (O10) object therefore has value ≥ u(w)/λ_r, which is ≥ u(w)/2 only if λ_r ≤ 2.
- The hypothesis M_f(l)‖U*Δa‖ ≤ b² does not bound ‖Δa‖₁, since μ*_J can be tiny while ‖Δa‖₁ is large.

Change: add "and ‖Δa‖₁ ≤ 1/2" to the hypotheses of the last sentence. In the application (box-level deep raise of Lemma Winf), ‖Δa‖₁ ≤ ψ(J) → 0, so this costs nothing.

### RC6. The profile classification after Lemma "Critical profiles oscillate" is false for general signature-ladder operators (lines 7979–7983)

Quote: "For signature vectors v_l = δ_l h_l/n_l of a signature-ladder operator and |a_s| ≈ v_l(s)^{1+β₀} on S_l∩F (β₀>0), the profile of v_l 1_{S_l∩F} is sparse for β₀<1, critical for β₀=1 and super-critical for β₀>1".

Problem.
- In Part I's design (Definition 8.1) the S_l are arbitrary disjoint infinite sets. The standing conventions include that operator among the "signature-ladder operators".
- If S_l∩F is lacunary, then for β₀ = 1 the ratio m(y)/y oscillates between ≈1 (y just above v(s_i)) and ≈ v(s_{i+1})/v(s_i) → 0 (y just below v(s_i)). So liminf = 0 and the profile is neither critical nor sparse.
- For β₀ > 1, sufficiently lacunary S_l∩F (for example s_{i+1} ≥ (1+β₀)s_i) also gives liminf m(y)/y = 0, so the profile is not super-critical.
- Numerical check (refC_work/lacunary_check*.py):
  - for S = {i²} and β₀ = 1, κ just below the thresholds is ≤ 2·10⁻⁶ and tends to 0;
  - for s_{i+1} = 3s_i and β₀ = 2, log₂κ just below the thresholds is −18, −54, −162, −486;
  - with bounded gaps (S = {2i+1}, β₀ = 1), κ stays in [0.34, 1.32].
- Only the sparse case β₀ < 1 holds for every S_l.
- The Y3 model behind this paragraph assumes bounded gaps (Y3 §1: "v_l(s) = c₀2^{−s} on S_l, … (bounded gaps)").

Change: "For a signature-ladder operator whose signature sets have bounded gaps (as for T_final, S_l = {2^l(2i+1)}), and |a_s| ≈ v_l(s)^{1+β₀} on S_l∩F with S_l∖F finite, the profile is sparse for β₀ < 1 (this part holds for every S_l), critical for β₀ = 1 and super-critical for β₀ > 1; for lacunary S_l∩F the cases β₀ ≥ 1 need not be critical or super-critical."

### RC7. Remark RS(b) states a heuristic interpretation as a fact (lines 9230–9231)

Quote: "(b) At the raised row the deep set is empty, so the factor-2 loss of Remark II-R1(c), which belongs to deep assignment, does not occur."

Problem.
- The factor 2 is itself a heuristic (Remark R1(c) is labelled "Heuristic, not used").
- V3-ref §0 classifies the interpretation "factor 2 belongs to deep assignment" as HEURISTIC.
- By the paper's convention (lines 300–303), such material may appear only in a remark that says so.

Change: "(b) At the raised row the deep set is empty. (Heuristic: the factor-2 loss of Remark R1(c), which we attribute to deep assignment, therefore does not arise in this proof.)"

### RC8. Summaries omit essential hypotheses and conflate pairs with rows (abstract 58–63; Introduction 258–266; Section 6 introduction 7702–7711; Remark residualinf(a) 10035–10046; Section 7(c) 10096–10098)

Quotes:
- Abstract: "recovery under signature room, cushion-sparse and box-dominated support swallowing, and, for T_final, support swallowing of any profile by finitely many bad carriers and by infinitely many under a rate condition".
- Introduction: "Finitely many cushion-sparse swallowed carriers are harmless for every signature-ladder operator (Theorem R1), and box-dominated support is harmless for every admissible operator (Theorem N). … support swallowing of any profile by finitely many bad carriers is harmless (Theorems RS, RSstar and NDprime)". Section 6, lines 7702–7711, says the same.
- Remark residualinf(a): "Recovered (proved above): … window-pinned mates at any F …; finitely many cushion-sparse swallowed carriers for every signature-ladder operator (Theorem R1); … block-tame rows with cushion-sparse mates (Corollary BTinf); for T_final: finitely many bad carriers with any support profile (Theorems RSstar, NDprime), … and mates with fixed d-neutral data under (RR) (Theorem A)".
- Section 7(c): "The classes listed in Remark residualinf(a) are in Rec".

Problems.
- (i) Theorems R1, RS, RS*, ND′ need (W⋆), (H2) and (H3-inf) in addition to (B_fin). These are not side conditions. Their failures are exactly the open items (b1) and (b2) of Remark residualinf.
- (ii) Theorem N needs (SC_I) and (W_M). Remark residualinf(a) states them; the abstract, Section 1 and Section 6's introduction do not.
- (iii) Window-pinned mates (Theorem B*-inf), cushion-sparse mates of block-tame rows (Corollary BTinf; it also needs V_f with a sparse profile) and fixed-data mates (Theorem A; it needs ρ²κ_w < 1 and (ND′_{L₀})) are statements about *pairs* (f,g) or (f,ρg). They are not statements about rows. So "the classes listed … are in Rec" is false for these items.

Change:
- Abstract: "… recovery under signature room, under cushion-sparse support swallowing (with the room and peak conditions (W⋆), (H2), (H3-inf)) and for box-dominated support (with the block conditions (SC_I), (W_M)), and, for T_final, recovery of first rows whose finitely many bad carriers swallow the support with any profile (under (W⋆), (H2), (H3-inf)), and of rows with infinitely many bad carriers under a rate condition."
- Introduction lines 258–266 and Section 6 lines 7702–7711: insert "(under (W⋆), (H2), (H3-inf))" after the references to Theorems R1 and RS/RS*/ND′, and "(under (SC_I) and (W_M))" after Theorem N.
- Remark residualinf(a): add "(under (W⋆), (H2), (H3-inf))" to the items for Theorems R1, RS* and ND′, and "with V_f of sparse profile" to Corollary BTinf. Separate the list into "rows recovered" (B-inf, B±-inf, cushion room, R1, N, RS*, ND′, RSinf, Proposition kernel) and "pairs recovered" (window-pinned mates; Corollary BTinf; Theorem A with ρ²κ_w < 1 and (ND′_{L₀})).
- Section 7(c): "The rows listed in Remark residualinf(a) are in Rec and the pairs listed there are in cl NA; for each of them (LSC-trunc) holds (Proposition LSC)."

### RC9. Necessity claims that the paper's own Remark onelever disclaims (Introduction 245–248; Section 7, 10150–10154 and 10202–10206)

Quotes:
- Introduction: "The lever is needed: a donor raise moves the block scalar ϰ by the same order as the raise, and the exact shifted system depends on a block only through ratios".
- Section 7: "The first requirement is not a technicality: … so two independent levers per block are needed."
- Problem S2: "The route needs d-consistency: without it, window masses change the coarse block data at first order, which gives a mismatch of order s₁/t²".

Problem.
- What is proved (Proposition Rkt, U1-ref Lemma R-kt and §3.1) is that *peak pushes alone* cannot achieve exactness and threshold protection independently.
- Remark onelever (lines 6509–6528) states: "No claim is made that the conclusion of a one-lever exactification fails." U1-ref §3.1 likewise says "PROVED that the argument fails; no claim that the conclusion fails".
- For d-consistency: only the upper bound O(s₁/t²) is proved (U3-ref F6a). That the mismatch is attained is numerical evidence, and that it cannot be rebalanced is HEURISTIC (U3-ref F6). So the necessity of d-consistency for the route is not proved.
- refB R14 raises the same point for Section 5.8 (Remark openS and Remark C6).

Change:
- Introduction: "A lever is needed in this route: a donor raise moves ϰ by the same order as the raise, and the exact shifted system depends on a block only through ratios (Corollary Rkt, Proposition Rkt), so peak pushes alone cannot achieve exactness and threshold protection independently (Remark onelever; no claim is made that a one-lever argument cannot succeed)."
- Section 7: replace "so two independent levers per block are needed" by "so this route needs a second, ϰ-neutral lever in every such block (Remark onelever)".
- Problem S2: replace "The route needs d-consistency: without it" by "The route uses d-consistency because without it". Add "(that the mismatch cannot then be rebalanced is heuristic)".

### RC10. Problem KN is ill-posed as formulated (lines 10159–10170)

Quote: "Is there an exact completion at which d stays strictly below its threshold, with constants of the form C_f(Des/u)^C, in the case where the exact zero set of the tiny minors …, in the ratio variables and near the ratios of f, lies in {ϱ_d ≥ 1}?"

Problem.
- By Proposition Rkt (U1-ref Lemma R-kt), the relative position ϱ_d at an exact completion is a function of the ratio variables, up to fine terms O(c_{L+1}²). An exact completion near r(f) is a point of Z near r(f).
- In the case stipulated (Z near r(f) ⊆ {ϱ_d ≥ 1}), every such completion has ϱ_d ≥ 1. So the question, read with "near" as the neighbourhood reachable with constants C_f(Des/u)^C, has a trivially negative answer.
- The open problem in the sources is different. It appears in U1-ref §3.4 and §6(1), and in the paper's own Remark openKN: in this configuration, *can the row still be recovered?* The route needs either:
  - d ending as a peak whose decomposition excess |ω_+(d)| + |ω_−(d)| is O(Kt/λ_d), "which nothing proved implies"; or
  - a ϰ-neutral lever supplied by other means.

Change: reformulate, e.g. "… Suppose that the exact zero set of the tiny minors, in the ratio variables and near the ratios of f, lies in {ϱ_d ≥ 1}. Is f ∈ Rec? In particular, can the window data be completed with d a peak whose excess |ω_+(d)|+|ω_−(d)| is O(Kt/λ_d), with K of the form C_f(Des/u)^C, or can a ϰ-neutral lever be supplied?"

### RC11. "Vanishes exactly when (ND′) fails" is not supported by the sources and is false in general (Problem tuning, 10271–10273; Remark Minf, 10024–10027)

Quotes:
- Problem tuning: "On proportional profiles the modulus reduces to the Sherman–Morrison denominator of Remark newrates, which vanishes exactly when (ND′) fails."
- Remark Minf: the same claim.

Problem.
- In the proportional case a = c_k v_k at the chosen coordinates s_k, the denominator is 1 − Σ_k c_k γ_k/ν².
- If (ND′) fails, then a|_F = Σ c_k u_k|_F (the c_k are forced by the values at the s_k), so Σ c_k γ_k = ν² and the denominator vanishes. This is U2-ref §8, checked numerically by sm_check.py.
- The converse fails. The denominator vanishes iff ⟨U*(Σ c_k u_k − a), U*a⟩ = 0, which is one scalar equation. It does not force Σ c_k u_k|_F = a|_F.
- The sources assert only the forward direction.

Change: "… which vanishes in particular when (ND′) fails (then a|_F = Σ c_k u_k|_F); the converse is not claimed." Make the same change in Remark Minf.

### RC12. Problem SCdeep misattributes the use of (SC) (lines 10286–10287)

Quote: "This enters only inside (C*) at infinite base support, and only for the per-mate statement Theorem A."

Problem.
- Theorem A assumes d-neutral data. Its proof applies Theorem raised at f_y with I₋ = ∅, so no (SC) is used.
- The open point (U2-ref §10 (E3)(c); V3 "Remark (OPEN)" after its Theorem A) concerns non-d-neutral data at raised rows. These arise:
  - in the transport of shifted (C*)-type data to infinite F; and
  - in a not-yet-proved extension of Theorem A to non-d-neutral fixed data.
- Remark residualinf(b5) states this correctly.

Change: "This enters only through shifted (non-d-neutral) data, i.e. inside (C*) at infinite base support (Problem Minf), and in the extension of Theorem A to non-d-neutral fixed data, which is open."

### RC13. Remark statusother overgeneralizes Theorem NL (lines 10297–10302)

Quote: "… and the failure of lower semicontinuity along block-tame rows (Theorem NL) shows that approximating first rows for a mate whose profile is not constant must put one of the two relevant coordinates into a bank, the support or the support of a strict non-peak, or be aligned with maximal contact."

Problem.
- Theorem NL assumes that the approximating rows f_n satisfy (BT). It uses this to get f_n ∈ Rec and two-piece data for every mate of f_n ([I, Theorem 7.10(c)]).
- So its contrapositive constrains only block-tame approximants. Nothing is proved about non-(BT) approximating rows, for which mates need not carry two-piece data.
- Moreover, as refA R2 notes, the paper does not establish any instance of the hypotheses of Theorem NL: the realization at self-aligned rows is "not reproduced here" (Remark NL). So "the failure of lower semicontinuity … shows" presupposes an unproved existence.

Change: "… and Theorem NL shows that *block-tame* approximating rows for a mate whose profile takes different values at two coordinates s₁, s₂ outside the data supports must put s₁ or s₂ into a bank, the support or the support of a strict non-peak, or be aligned with maximal contact. (That such mates exist at self-aligned rows is proved in the source but not reproduced here, Remark NL.)"

### RC14. Remark R1(d): wrong cross-reference (lines 8891–8893)

Quote: "For T_final both statements are contained in Theorem RSstar below, and we do not reproduce their proofs."

Problem.
- Theorem RS* assumes (ND′_{B_np}).
- The rows of Y3 Theorem 3.5 and Y3-ref Proposition 3.4 (d-neutral bad carriers with supp u_l ⊆ F and monochromatic a on S_l∩F) can fail (ND′): a|_F may lie in the span of the u_l|_F.
- Those rows are covered by Theorem ND′ (via Theorem R1), not by Theorem RS*.

Change: "For T_final both statements are contained in Theorems RSstar and NDprime below (whose hypotheses (W⋆), (H2), (H3-inf), (B_fin) are among those of the cited results)."

### RC15. The rate Ξ_f can vanish, which makes (W_inf) vacuous (lines 9634–9640; used in Theorem RSinf)

Quote: "For a level l let C_VP(l) := C₀ 2^{max F₀}/min_{s∈F₀}|a_s|, with F₀, C₀ the data of Lemma VP for L₀ := B_np(l), and Ξ_f(l) := (4H(l)l+3)^{l+2}(1+K_⋆(l)) C_VP(l)/(γ_B(l)μ_B(l))."

Problem.
- C_VP(l) enters Ξ_f multiplicatively, and it is not bounded below.
- If every carrier of B_np(l) vanishes on F, then V₀^⊥ = {0} and Lemma VP holds with F₀ = ∅. Example: all bad strict non-peaks up to level l are contact-swallowed, with signatures and targets disjoint from F. Then C_VP(l) is undefined, or 0 with the usual conventions. So Ξ_f(l) = 0, and (W_inf) holds trivially. Even when F₀ ≠ ∅, nothing prevents C₀(l), and hence Ξ_f(l), from being small along a sequence of levels.
- The theorem would then assert f ∈ Rec with no condition on the rates H(l), K_⋆(l), γ_B(l), μ_B(l). That is the unconditional infinite-B statement, which is not proved: U2-ref §11 says "unconditional only through the transport".
- The proof uses Ξ_f only as an upper bound for n_j, P_j and K_top. Those bounds ("n_j + P_j ≤ C Ξ_f Ω_K s_max log₂ n(w_j)") are false when Ξ_f is 0 or artificially small.
- Similarly, the step "2^{1+max F₀} ≤ 2C_VP(l_j)" in (iv) needs C₀ ≥ min_{F₀}|a_s|.
- The source's definition (U2-ref Fix 1) has the same gap. Proposition kernel, by contrast, uses "1 + max_k 1/m^F_k(l)".

Change: in Lemma VP take C₀ ≥ 1 without loss of generality. Define C_VP(l) := 1 if F₀ = ∅. Write (1 + C_VP(l)) in place of C_VP(l) in Ξ_f, consistently with x(n), which already contains 1 + C_VP(l_j).

### Required fixes in my scope already raised by other referees (not counted again)
- **Introduction lines 176–177** advertise Theorem NL as "the failure of lower semicontinuity …". The theorem is a conditional criterion whose realization is not reproduced (refA R2). RC13 is the Section 7 counterpart.
- **Introduction line 184**: "S_l = {2^l(2i+1) : i ≥ 0}" should read "i ≥ 1" (refA R6).
- refB R14 (necessity claims in Section 5.8) is the Section 5 counterpart of RC9.
- refB R8 (Proposition constcontact stated for any admissible T) and refB R11/R12 (Lemma zerovalue; Des(L) of D^{U1′}) affect claims that Sections 1 and 7 quote:
  - line 228: "it does not occur at constant-sign maximal contact";
  - lines 238–244 (Master Theorem IV′);
  - Remark statusfin(c): "now proved by the zero-value absorber pairs".

  Once refB's fixes are made, these quotations must be checked against the corrected statements.

---

## 2. Optional suggestions

- **OC1. Theorem R1, Step 3(e) (line 8841).** γ_𝓑 is used here without definition; it is defined only at line 9510, in another context. Add "γ_𝓑 := min(min_m M_m, min{gap_{m(l)}(k(l)) : l ∈ B_np}) > 0 as in [I, Lemma 8.41]".
- **OC2. Remark RS(a) (line 9226).** "it is never o(T_j²)" is false for sparse profiles, where the mass y_j m(y_j) = o(y_j²). Write "for critical and super-critical profiles it is not o(T_j²)" (cf. V3-ref §6(b)).
- **OC3. Theorem A, proof (1) (line 9264).** "p^*(g−g_y) = O(ε_e)" should be O(ε_e log(e/ε_e)) because of the normer change (V3-ref §4). This is harmless.
- **OC4. Theorem RS, Step 2 (lines 9143–9146).** Lemma raise(b), (d), (e) is cited for D_j = Δa + Δa″, which is not a raise. Add: "the proofs of Lemma raise(b), (c), (e) use only that z is fixed; (d) follows from ‖D_j‖₁ → 0 and λ_j → 1".
- **OC5. Theorem RS, Step 2(ii) (line 9164).** "with the same Hoffman constant" should read "with Hoffman constants within a factor → 1". The d-rows are rescaled by the block factors q₀^{(j)}σ_m/(q₀σ_{j,m}) → 1; the cone is the same set.
- **OC6. Lemma Winf, step (3).** Lemma P is applied with T_B(l_*) (the coarse bad targets) in place of T_B (all bad targets). Add one sentence: targets of fine bad carriers l″ > l_* that contain s are part of r_s, so Lemma P holds with T_B(l_*) for coarse l (cf. U2-ref r1).
- **OC7. Proposition kernel, proof (line 9743).** "We use Lemma Winf with f′ = f": Lemma Winf assumes (ND′_{B_np(l_*)}), which fails here. Write "We run the proof of Lemma Winf with R = ∅ and D = 0 (its hypothesis (ND′) is used only for the correction Δa″)".
- **OC8. Theorem RSinf, hypothesis "r⋆_l > 0 for every good l".** The rooms of Lemma Winf depend on the level l_* (the targets of B(l_*) are removed). State "r⋆_l(l_*) > 0 for all good l ≤ l_* and all l_*".
- **OC9. Proposition LSC, last statement (lines 9953–9958).** For Theorems raised and A only the triples with ρ²κ_w < 1 are covered, so write "for every (f, g, ρ) covered". The proof can simply cite [I, Lemma 1.16] (with [I, Proposition 1.10(c)]): (f, ρg) ∈ cl NA gives norm-attaining f_n → f with ρg ∈ Li 𝒞(f_n).
- **OC10. Introduction lines 162–164.** "The uniform one-sided transfer expansion (Lemma U) holds along every sequence of first rows f_j → f": Lemma U assumes F and F_j finite with F ⊆ F_j. The version for arbitrary supports is Lemma Uinf under (OS2′); mention it.
- **OC11. Abstract lines 44–46 and Introduction lines 165–169.** Theorem ERT's hypothesis is on the transfer error ε′_j, not on p^*(f_j−f). For raise companions p^*(f_j−f) is not o(T_lo²) (Remark RS(a)). Rephrase, e.g. "… whose transfer error (for raise companions: the Hilbert footprint of the raise and the normer change) is below a fixed multiple of the square of the bottom of the window".
- **OC12. Remark residualinf(d) (lines 10064–10068).** The sentence "every infinite-support mechanism examined is either harmless after a deep raise …" is an interpretation; label it as in Remark evidence. Note also that "box-size switching" is harmless only under (W_inf).
- **OC13. Section 7(b) (lines 10092–10094).** (C*) rows are defined for T_final (Definition Cstar). For D^{U1′} write "for the norm built with D^{U1′}, the rows with finite base support covered by Master Theorem IV′ are in Rec".
- **OC14. Problem mix (lines 10172–10178).** The parenthesis reports finite models in which every exact completion is bad. Reformulate the problem as "are the rows of mixed classes in Rec?", with the good completion as one route, as in RC10.
- **OC15. Remark cushionroom (lines 8626–8629).** "If z is constant on S_l∖F_{≤M₀}" should say "constant of modulus 1" (contacts and support of one sign), as the parenthesis intends.
- **OC16. Remark transferinf(c) and Remark R1(d).** Both state results without proof that are proved in the sources: pure base mates along every truncation (Z5 Lemma 5.1, refereed correct); Y3 Theorem 3.5 and Y3-ref Proposition 3.4. Cite the sources there, in line with the convention of lines 300–303.

---

## 3. Verification record

For each statement: its source, its status in the source after the referee fixes, and my check of the paper's proof.

### Section 6.1 (transfer peaks outside c₀₀; source Z5 T1, T2)
- **Definition/Lemma trunc.** Source: Z5 Lemma 2.1, PROVED. I re-derived (a)–(c), including ‖a_{N′}‖₁ + ν_{N′} = 1, a_{N′}(x̃_{N′}) = 1 and c_{N′} = 1/p(x̃_{N′}) → q₀. OK.
- **Theorem transferinf.** Source: Z5 Theorem 2.2, PROVED. I re-derived:
  - the no-flip radius r_b = min(1, 1/(4‖b/a‖_∞)), uniform in N′;
  - the base expansion with factor 1 + 2|t|‖U*b′‖/ν;
  - h_{N′} → H_b;
  - Step 4 (e_{m,N′} → e_{∞,m}).

  The hypotheses match Part I Theorem 5.8 with a ∈ ℓ₁ and ‖b/a‖_∞ < ∞. OK.
- **Corollary windowedinf** (Z5 Cor. 2.3). OK.
- **Remark transferinf** (Z5 T9). Correct; see OC16.

### Section 6.2 (cushions, flip profiles; sources Y3 §1, Z5 Lemma 1.1, Z5 T10, Y3 Lemma 3.1, Z5-ref R2)
- **Lemma flipcalc (a)–(d)** (Y3 Lemma 1.1, refereed correct). Re-derived, including the converse in (d): Fl(2r) ≥ 2r·m(r). OK.
- **Lemma oscillate** (Y3 Lemma 1.2). Re-derived (R_i ≥ 2R_{i+1}). OK. The paragraph after it: RC6.
- **Lemma cushion** (Z5 Lemma 1.1). OK.
- **Lemma Uinf.** This merges the paper's Lemma U with Z5-ref Lemma R2 (sparse flips) and V3-ref I3 (along f_j, U_* = 0).
  - Checked: a positive flip summand forces |a_j(i)| < 2C_* r U_*(i) and is ≤ 3rC_*U_*(i); Fl_* = 3C_* r·m̄(2C_* r) = o(r²) uniformly in j; and q₀^{(j)}Fl_* ≤ (r²/2)(ε_tr/10).
  - The conditions on c_♭ and t₁ involve only f, ε_tr, A₀, C₊, C_*, m̄; j₀ also depends on (f_j). Transfer data, [I, Lemma 7.1(b)], [I, Lemma 7.2] and [I, Proposition 7.3] hold at every F.

  OK. Note RC4: (OS1) requires Γ ≤ 2.
- **Lemma boundedfree** (Z5 T10; corrects Part I Lemma 8.29 and the Round-4 referee). (a) is [I, (15)] with Lemma 8.7(a). (b): Φ is injective because the a-direction is pinned by the ẑ-coordinate. Constants checked. OK.
- **Lemma unswitch** (Y3 Lemma 3.1). Re-derived C_un(l)² = q₀‖U‖²/ν + σ_m/(m²C_m) using λ = mΦ. OK.

### Section 6.3 (engineered recovery at arbitrary F; source Y3 §2, §4, §6 + Y3-ref)
- **Definition twopieceinf, Theorem raised** (Y3 Theorem 2.1).
  - Checked: the raise |a″_j| = max(|a_j|, 8ρs₁|b^θ_j|); (E1) with 12 (8 would suffice — harmless); (E2) unchanged; s_j x ≥ |a″_j|/4.
  - No θ-flips; ±-flips cost ≤ 2ρ|τ| m(4ρ|τ|).
  - The coordinates in F ∩ (N_w, N″] become contacts and cost ρ|τ|(s_j v_j)₋.
  - Budget: 1 − 2δ + 6δ/8 ≤ 1 − δ.

  OK.
- **Theorem flipext** (Y3 Theorem 2.2 with Y3-ref 1.5: factor (1+o(1)); θ-hypothesis dropped). Checked Fl(τ) ≤ Fl_β(ρ|τ|(1+ε)) and c′ → q₀. OK.
- **Theorem masterinf** (Y3 Theorem 6.1).
  - Averaging uses [I, Lemma 8.43].
  - The (CS-side) of the averages follows from Lemma flipcalc(b): m_{C₊|a|/T′}(2x) = 0 for x < T′/(2C₊).
  - (SC) is hereditary.

  OK.
- **Theorem onesidedinf** (Y3 Theorem 4.1).
  - Test points: Z_t = q₀z + tχ_c, ‖h_t‖² = q₀² + t⁴κ², a(η_t − ξ) = −t²κν.
  - Fenchel duality has no F-constraint.
  - (c): G_b = Fl_{(sb)₋} + νΨ.

  OK.
- **Corollary BTinf** (Y3 Corollary 4.2). |b^± − g| ≤ C V_f; block-tame ⇒ (SC) for every set of blocks. OK.

### Section 6.4 (room; source Z5 §3)
- **Proposition clamped** (Z5 Proposition 3.1). Re-derived K_κ, |κ_t| ≤ 2K_κ t, |b_t| ≤ 3|a|/t and (c). OK.
- **Theorem Bstarinf** (Z5 T5). Checked (PIN_K) with K = K_j + 6, the use of Lemma Uinf (A₀ = 4, kind [1]) and Corollary windowedinf (finite supp b_t). OK.
- **Theorems Binf, Bpminf, cushionroom** (Z5 T6, T7a, T7b).
  - Checked Σ_l E^c_l ≤ (2/q₀ + 4)t, the constant (2/q₀ + 26), and the monotonicity of M(·).
  - The Z5-ref 1.1 correction of the (W^c) gloss is in Remark cushionroom.

  OK.

### Section 6.5 (cushion sparsity; source Z5-ref R0, R1)
- **Definition badinf.** Matches Z5-ref: q_l, S⋆_l, Λ⋆ over good carriers only; the paper notes the difference from Part I's Λ⋆ at finite F.
- **Lemma R0, Lemma exactswitchinf.** These are Z5-ref Lemma R0 and R1 Steps 1–2: T₀ includes S_l∖F for l ∈ B_F, there is no sign row for B_F, and the cost formula is c(τ) = Σ_{B_K} 2(τ_l)₋𝔪_l + Σ_{T₀∖F} φ. OK.
- **Lemma commonshift** (Z5-ref Claim 3.1). Both cases re-derived. OK.
- **Theorem R1** (Z5-ref Theorem R1). Steps 1–5 re-derived:
  - |τ′_l| ≤ C_τ;
  - ‖ΔB − X‖₁ ≤ (C_f+1)K_⋆ t;
  - the deep-set bounds and t‖b^±‖₁ ≤ 3 + 3C_τ|B|;
  - A₂ = 4 + C_τ/λ_B;
  - the use of Lemma Uinf (U_* = U_B, C_* = C_τ) and of Theorem masterinf (β = C_τ U_B).

  OK (OC1).
- **Remark R1.**
  - (a): correct for every infinite S_l∩F, since only sparsity is claimed "iff β₀ < 1".
  - (b): Z5-ref §5(b), correct.
  - (c): labelled heuristic.
  - (d): RC14.

### Section 6.6 (box domination; source Y3 Theorem 5.1 + Y3-ref 1.2, 1.3)
- **Theorem N.** Steps 1–5 re-derived:
  - E_± ≤ (t/2)M_f(L) + 4t² (Y3-ref 1.3 with the max over coarse peaks);
  - |(b⁰_± − B_±)_j| ≤ 5Bx(j)/t;
  - |X_j| ≤ 12Bx(j)/t;
  - common shift |σ_j| ≤ 𝔣⁺_j + 𝔣⁻_j;
  - K = (1+‖U‖)²/q₀;
  - ‖B_±‖₁ ≤ ‖g‖₁ + 6/t (Y3-ref 1.2);
  - the kind [1]/[3] classification (A₂ = 4);
  - the fixed window length n₀.

  OK.
- **Remark N.** (b) checked. (c) is a statement about the method (Y3-ref F7: "checked").

### Section 6.7 (raise transfer at T_final; sources V3 + V3-ref, U2 + U2-ref)
- **Lemma VP** (V3-ref VP′ with (ND′)). Re-derived (i)–(iii), including D_xG(0,0) = Λ/ν and the invariance of V₀^⊥. OK; for the quantitative radius see RC3(c).
- **Raise room (RR_W).** Example and remarks correct.
- **Theorem RS** (V3-ref Theorem RS′). Steps 1–6 checked: bounded switching, an empty deep set, the cone at f_j equal to the cone at f, and the B_K degenerate anti-sign peaks (V3-ref §3(b)). One gap: RC1 (θ_*); see also OC4, OC5.
- **Remark RS.** (a): OC2. (b): RC7. (c): the V3-ref §6(a) fix is present.
- **Theorem A** (V3 Theorem 4.1 + V3-ref §4). Correct apart from RC4 and OC3.
- **Lemma P** (U2 Lemma P + U2-ref r1). Re-derived (P.1)/(P.2): Σ|r_s| ≤ 8t² for t ≥ T_lo(l_*), and C_q is a valid (larger) constant. OK.
- **Theorem RS*** (U2 §1.3 + U2-ref r1, r2). Checked:
  - the thresholds K_i and the pigeonhole;
  - kept amplitudes keep sign and satisfy (3/4)|τ| ≤ |τ′| ≤ (5/4)|τ|;
  - the four cases of the empty-deep-set claim;
  - the footprint ε′_j ≤ 2C x y_j and the fixed point n_j.

  OK apart from RC1.
- **Lemma ND, Theorem NDprime** (U2 Lemma ND / Theorem ND′, U2-ref §3). Checked (H4-inf) with constant max|κ/c_k|. OK.
- **Lemma Winf** (U2 Lemma W + U2-ref Fix 1, W2–W5). Steps (1)–(4) checked:
  - |τ_l| ≤ 2t/μ_B + λK_d t at bad peaks;
  - the Σ-rows;
  - "thick" coordinates satisfy 2|a′|/t ≥ (K^pk + K_top/4)t;
  - t‖b^±‖₁ ≤ 9 and A₂ = 12.

  Defect: the Γ conclusion (RC1(b)); see also OC6.
- **Theorem RSinf** (U2 RS*_inf + Fix 1). See RC1, RC2, RC3, RC15, OC8.
- **Remark RSinf.** OK.
- **Proposition kernel** (U2-ref Fix 5). Checked the summation of (P.1) over Ŝ_k, the allowedness bound 5·2^{−2j}δ_k/t, and that kept kernel carriers have s_s X′_s > −4|a_s|/t. OK (OC7).

### Section 6.8 (deep raises; sources U2 DR-inf, TR-inf, U2-ref Fixes 3, 4, 6; V3 M_inf)
- **Lemma DR.**
  - (a): (O1), (O2), (O6), (O11) are unchanged and (O10) is divided by λ_r, because J > s_t(l) and the first three coordinates beyond s_max(l) are ≤ s_t(l) (line 2677).
  - (b): Lipschitz bounds; (O12) has λ_r cancel.
  - (O9) is excluded (U2-ref D2).

  OK apart from RC5.
- **Lemma TR.** Re-derived (a) (first-order formula and remainder), (b) (pair cancellation and the private effect) and (c). OK. The paragraph after it agrees with U2-ref §7 and (E4)(ii) ("single unpaired support raise not admissible").
- **Proposition Minfred** (V3-ref §5, reduction PROVED). OK.
- **Proposition LSC** (Z5 Proposition 5.4; V3 Corollary 4.2). The equivalence and its proof are correct; OC9.
- **Remark trunc.** Labelled an interpretation (Y3-ref F9). OK.
- **Remark Minf.** Labelled sketch. Its item list matches U2-ref §9 (G2, D2, pinned faces, joint fixed point, 8Bx_*). RC11 applies.
- **Remark residualinf.** RC8, OC12.

### Abstract and Section 1
- All `[I, …]` references verified: 3.8, 4.1, 6.6, 7.18, 7.21, 7.22, 8.1, 8.2, 8.3, 8.18, 8.20, 8.21, 8.31, 8.35, 8.44, 1.3, 1.5, 1.9, 1.13, 1.15, 9 (Section 9 of Part I).
- Lemma Z is stated per mate (f′ chosen after g and ρ).
- Density and Lemma Z are stated as open for every N, including N = 1, and for Martín's p.
- The p_N vs. p disclaimer is present (line 145).
- MT IV′ is quoted with (KN) and the frustration condition, matching Theorem MTIV.
- The (C*) characterization matches Definition Cstar and Corollary Cstarnec.
- Defects: RC8, RC9 (line 245); refA R2 and R6 (lines 176, 184); OC10, OC11.
- The conventions paragraph (lines 300–306) is honoured in my sections, except RC7 and the unlabelled interpretation in Remark residualinf(d) (OC12).

### Section 7
- (a) and (b) are consistent with the body (OC13).
- **Problems Z, LSC and p** are correctly posed. The reduction "Problem Cstar ⇒ Lemma Z at finite F" via Corollary Cstarnec, [I, Lemma 1.16] and [I, Lemma 8.4(a)] is correct.
- **"Route through absorbers and levers".** It correctly says that the donor-raise exactification (U1's MT IV / Cor IV.1) "is not proved and is not used"; the necessity wording is RC9.
- **Problem KN:** RC10. **Problem mix:** OC14. **Problem S1:** OK. **Problem S2:** RC9.
- **Remark statusfin.** Its claims match U1/U1-ref (C*-1, C*-2 in configuration (i), C*-4, C*-5). It depends on refB R11 (Lemma zerovalue).
- **Problems Minf, Winf, H2:** consistent with U2-ref §11. **Problem tuning:** RC11. **Problem SCdeep:** RC12.
- **Remark statusother:** RC13. **Remark evidence:** properly labelled.

### Quantifier order (checked in Theorems RS, RS*, RSinf, A, R1, N, B*-inf)
- The design (T_final, μ*, sub-windows) is fixed before f.
- Levels, windows, raise depths and companions depend on f and ρ (and, in Theorem A, on the fixed data of g, which is allowed because the statement is per mate). They are chosen before the scale.
- Two-sided decompositions and window data are taken after g, ρ and t.
- Theorem ERT's quantifiers are used correctly.
- I found no order violation. RC1 and RC3(a) are defects in the choice of depths, not in the order.

### Required-fix count: 15 (RC1–RC15). Optional: 16 (OC1–OC16).
