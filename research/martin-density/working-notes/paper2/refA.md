# Referee report A on `martin_density_note_II.tex`: Sections 2 and 3

Scope: Section 2, "Companions and transfer" (lines 311–1850), and Section 3, "The designed operator T_final" (lines 1852–2980). I also checked the places in the Introduction (lines 125–193) and in Sections 4–6 that describe or use these two sections.
Sources compared line by line: r5/Z3 (+ Z3_referee); r6/Y1, Y2 (+ referee reports and ref_notes), Y4-ref C.2–C.7 (banks and pulls); r7/V1, V3 (+ referees), V2-ref P1–P7 (the design D^{V2}); r8/U1, U3 (+ referees and ref_notes), U4 (+ U4_referee), and U2 (the design part, U2-ref Fix 2). I also checked Part I: I compiled `ctx/paper/martin_density_note.tex` to get its label numbering. The numbering of every `[I, ...]` reference in Sections 2–3 matches the intended label. I opened about 25 of the cited statements, including Remark 1.1, Definition 1.3, Lemmas 1.6–1.7, Propositions 1.9–1.12, Lemmas 3.3–3.4, 7.2, Proposition 7.3, Definition 7.7, Theorem 7.10, Corollary 7.22, Definition 8.1, Theorem 8.2, Lemma 8.10 and Remark 8.22, and their content matches the use. The current build log has no undefined references.

## 0. Verdict

The mathematics of Section 2 is sound. I re-derived every proof by hand:
- Lemmas T and T2, Corollary T3, and the κ-lemmas (data identity, derivatives (b)(i)–(iii), Corollary Rkt);
- the cost lemma, the raise lemmas and Corollary RT;
- Lemma U and Theorems ERT and E, including all the constant arithmetic;
- the certificate, the shift bound, the sandwich lemma, Corollaries S1 and S2, Proposition S3 and Lemma VT.

I also checked the threshold certificate and the three κ-derivatives numerically at 80 digits. The finite-difference error scales exactly with the step, as it should if the formulas are exact (script: `scratchpad/refA_work/scripts/thr_check.py`).

Every referee correction that belongs to these sections has been incorporated:
- Z3-ref: the Hoffman gloss in Lemma 1.4 and the unweighted cost term;
- Y1-ref F3 (kind [1′]), Y2 Lemma U′ (kind [3], with t₁ and j₀ uniform);
- Y4-ref P2 and V1-ref p3 (banks and pulls need not be contacts of f);
- V3 RT / E_RT;
- U1-ref Lemma R-kt (the κ-lemmas are stated only as identities; the false "one scalar suffices" claim is absent);
- U3-ref F6a: the (S2a) mismatch appears only in Remark VT(c), and its repair is labelled a sketch;
- U4-ref C1 and C7 and precisions q1, q7, q8;
- U2-ref Fix 2: B⋆ with s_t(l), and rate objects (O10)–(O12) included in ω(l).

Nothing that a referee found wrong appears as proved in these sections:
- U1 Master Theorem IV and Corollary IV.1;
- U3 (S2a);
- Y4's directional residual (UN+);
- Z1's exposed-face consequence.

Lemma Z and density are nowhere claimed.

There are **8 REQUIRED fixes**:
- **Definitional gaps that leave T_final not well defined as written (R3, R4).** G*(l) and H_comb(l) are never defined, and δ_sh(l) is not a design number as stated.
- **An unspecified norm for Lip(l) on which Section 5 silently depends (R5).**
- **Overclaims (R2, R7).** Theorem NL is stated and advertised as "the failure of lower semicontinuity", but the paper gives no instance. Remark scope (c) claims the FD targets are removable, but a Section 4 proof uses them.
- **A mis-stated error term (R1)** in the remark after Lemma RT.
- **An incomplete step in Corollary Rkt (R8).**
- **An inconsistency between the introduction and Definition II-data (R6).**

There are also 12 optional suggestions.

---

## 1. REQUIRED fixes

### R1. Remark after Lemma RT: the Hilbert footprint of the corrections is missing (lines 1074–1078)
Quote: "If, in addition, corrections $\Delta a''$ of arbitrary sign are made on a finite set disjoint from $\supp\Delta a$ with $|\Delta a''_j|\le|a_j|/2$ there, the same proof gives the bound with the additional error $2\|\Delta a''\|_1$ (because then $\|a+\Delta a+\Delta a''\|_1\ge\|a\|_1+\|\Delta a\|_1-\|\Delta a''\|_1$)."

Problem. Put D := Δa + Δa'' and λ := q*(a + D), and assume λ ≥ 1. The proof of Lemma RT gives:
- λ ≥ 1 + ‖Δa‖₁ − ‖Δa''‖₁ − ‖U*D‖, hence ‖Δa‖₁ ≤ λ − 1 + ‖Δa''‖₁ + ‖U*D‖;
- q*(A + D) ≤ π + ‖D‖₁ + ‖U*D‖ ≤ π + (λ − 1) + 2‖Δa''‖₁ + 2‖U*D‖;
- therefore p*(f^# + rh) ≤ 1 + (p*(f + λrh) − 1 + 2‖U*D‖ + 2‖Δa''‖₁)/λ + p*(L*(w^# − w)).

The footprint is that of the whole change D, not of Δa. The sentence keeps "the bound" of Lemma RT, which contains 2‖U*Δa‖, and adds only 2‖Δa''‖₁. So the term 2(‖U*D‖ − ‖U*Δa‖)/λ ≤ 2‖U*Δa''‖/λ is missing. That term is not dominated when U*Δa'' is anti-aligned with U*a, so the statement as written is not proved. The source V3 (Remark after its Lemma 2.3) has the same slip. Section 6 of this paper already uses the correct form (line 9149: ε′_j := 2‖U*D_j‖ + 2‖Δa''‖₁ + p*(L*(w_j − w))).

Change to: "If, in addition, corrections Δa'' of arbitrary sign are made on a finite set F₀ ⊆ F ∖ supp Δa with |Δa''_j| ≤ |a_j|/2 on F₀, and λ := q*(a + D) ≥ 1 with D := Δa + Δa'', then the same proof gives
p*(f^# + rh) ≤ 1 + (p*(f + λrh) − 1 + 2‖U*D‖_H + 2‖Δa''‖₁)/λ + p*(L*(w^# − w)),
because ‖a + D‖₁ ≥ ‖a‖₁ + ‖Δa‖₁ − ‖Δa''‖₁. The extra error compared with Lemma RT is therefore at most 2q*(Δa'')/λ."
The condition |Δa''_j| ≤ |a_j|/2 keeps supp(a + D) = F and the signs, so f[(a + D)/λ, z] is admissible. Say so.

### R2. Theorem NL is conditional, but it is titled and advertised as an established failure (lines 1654–1696; Introduction, lines 176–177)
Quotes:
- Title: "Failure of lower semicontinuity along block-tame rows."
- Introduction: "Section 2 also proves … the failure of lower semicontinuity of the fibre map along block-tame first rows (Theorem~\ref{thm:II-NL})."
- Remark NL: "The construction of these rows and the verification of these properties … are not reproduced here; we record only the consequence: membership in $\Rec$ cannot be propagated along an *arbitrary* dense sequence of block-tame rows …"

Problem. As proved in the paper, Theorem NL says: if f, g, s₁, s₂ and a sequence of (BT) rows f_n with the stated combinatorial properties exist, then lower semicontinuity fails along (f_n). The proof (Proposition S3 plus [I, Theorem 7.10(c), Corollary 7.22]) is correct. But the paper nowhere shows that the hypotheses can be met, because the self-aligned construction is "not reproduced". So neither the theorem title, nor the introduction, nor the "consequence" in Remark NL is established by the paper. The realization is PROVED in the source (U3 Theorem NL, Steps 1–4, refereed correct with precisions (n1) and (n2), using the hysteretic re-run). The overclaim is therefore relative to the paper's own standard ("every … theorem … is given with a complete proof"), not relative to the truth.

Change: do one of the following.
- **(a)** Add a proposition with proof that reproduces U3's construction for T_final. T_final has (SF*), (Z0) and a diagonal base by Proposition II-features (c), (e), (h), so the hypotheses of Theorem NL then hold with f a self-aligned (BT) row. Then keep the title and the introduction sentence.
- **(b)** Retitle the theorem "A criterion for the failure of lower semicontinuity along block-tame rows". In the introduction write "a criterion for the failure of lower semicontinuity … (Theorem NL); that it applies at self-aligned rows is proved in the source [U3] and is not reproduced here (Remark NL)". In Remark NL, change "we record only the consequence:" to "if this construction is granted, it follows that …".

### R3. G*(l) and H_comb(l) are never defined, so Des(l), and hence T_final, is not well defined (lines 2068–2069, 2183–2188, 2199–2201)
Quote (Definition II-constants (d)): "$G^*(l),H_{\rm comb}(l),G^{**}(l)\ge1$ are the maximal Hoffman constants of the particular configuration systems used in the pinning arguments (arbitrary contact patterns on $T(l)$ and arbitrary dropped sets); they are recalled where they are used."

Problem.
- G**(l) is defined later (Definition II-pattern, lines 3507–3513, where G** ≤ H_conf is also shown).
- G*(l) and H_comb(l) do not occur anywhere else in the paper (I searched the whole file), so they are never "recalled" and never defined.
- Ξ^Y(l) (line 2187) is defined through H_comb(l), and Ξ^Y itself is used nowhere else.
- All three are factors of Des(l) (line 2069). b(w) depends on Des(l), and c_{l+1} ≤ b(l, M(l))² by (W2). So as written the recursion in Definition II-Tfinal is not fully specified. The statements (K1), (K2), Lemma W(b) and Proposition II-bank(e) assert properties of undefined numbers.
- In U4 these factors carry Z4's G*, Z6's H_comb and Y2's Ξ^Y, so that Z4 Theorem A, Z6 U′ and Y2 Theorems M and Y survive. No such theorem is stated in this paper.

Change: either
- (i) delete G*(l), H_comb(l) and Ξ^Y(l) from the bracket of Des(l) and from (K1). Every window condition is monotone in Des (Remark GWuse), and nothing uses these factors; or
- (ii) define them explicitly in Definition II-constants (d), e.g. "G*(l) := H_comb(l) := H_conf(l)", and define G**(l) there as in lines 3507–3513 with a forward pointer. Ξ^Y is then a design number.
In either case remove the sentence "they are recalled where they are used".

### R4. δ_sh(l) is not defined in Section 3, and Section 5's definition is not a design number as stated (lines 2189–2192, used in Des(l) at line 2071; cf. lines 5233–5259)
Quote: "$\delta_{\rm sh}(l)>0$ is the least positive value of the combinatorial shift costs of the shift patterns of level $l$, computed with the design weights $2\mathfrak m^{\rm nat}_{l''}(l)$ ($\delta_{\rm sh}(l):=1$ if there is none)."

Problem.
- "Combinatorial shift cost" is not defined in Section 3.
- Section 5 (lines 5233–5259) defines c^comb, and "reads" δ_sh(l) as a minimum over *enlarged* shift patterns κ^sh. These are not the "shift patterns" π of (O6), to which Section 3 appears to refer.
- Section 5's formula uses Π_m := Σ_{l''∈G_pk} vs_{l''} λ_{l''} u_{l''} 1_{F^c}, with vs_{l''} := sgn w_{m(l'')}(k(l'')) taken from (O9)(S2). That sign depends on f, and so does the set F. The enlarged pattern (κ, N₀, R₇, I_sh, src, G_pk) does not record vs.
- So c^comb_*(κ^sh) is not "determined by the pattern" (line 5255), and δ_sh(l) as read in Section 5 is not a design number. This contradicts (K2) and Lemma W(c), and leaves Des(l) ill-defined. V2-ref (P3)/(P4) has the same omission of vs.

Change: in Definition II-constants (d), define δ_sh(l) explicitly, as follows.
1. For every enlarged shift pattern κ^sh = (κ, N₀, R₇, I_sh, src, G_pk) of level l (as in (O9)) and every sign vector vs ∈ {±1}^{G_pk}, put Π_m := Σ_{l''∈G_pk, m(l'')=m} vs_{l''} λ_{l''} u_{l''}.
2. Let c^comb(δ; κ^sh, vs) be the bracket of lines 5241–5246, with L evaluated only at j ∈ T(l) ∖ F′ and with coef_{l''} read on S_{l''} ∖ ([1, l] ∪ T(l)). No 1_{F^c} is needed.
3. Let c^comb_* be its minimum over {‖δ‖₁ = 1, the sign constraints of src}, and let δ_sh(l) := the least positive value over all pairs (κ^sh, vs), with δ_sh(l) := 1 if there is none.
4. Then in Section 5 (line 5257) replace "We read the constant … as" by a reference to this definition, and add one sentence: for l ≥ max F, with F′ = F ∩ T(l) and vs = (sgn w_m(k(l''))), the f-dependent cost of lines 5241–5246 coincides with the design one, because F ⊆ [1, l].

Also make the wording consistent ("enlarged shift patterns") in both places.

### R5. The norm for Lip(l) is not specified, and Theorem B (Section 5) needs the sup-norm (Definition II-constants (c), lines 2154–2156)
Quote: "let $\mathrm{Lip}(l)\ge1$ be a common Lipschitz constant on $[-2,2]^{[1,l]}$ of all $\pi_{\kappa,J,K}$ whose $J$ contains a value row".

Problem. Theorem B, Step 1 (lines 5006–5010) combines Lip(l) with hypothesis (A1) (line 4972). (A1) is a coordinatewise bound, |val_{l''}(f₁) − val_{l''}(f)| ≤ C_*(l) b(w) for l'' ∈ Kp. Theorem B concludes that every minor moves by at most Lip(l) C_*(l) b(w). This holds only if Lip(l) is a Lipschitz constant for the maximum norm. With the Euclidean norm, which is the default reading, one loses a factor |Kp|^{1/2} ≤ l^{1/2}. That factor is absorbed neither by C_*(l) = |T(l)| + 2 (|T(l)| can be much smaller than l) nor by β(w) = (1 + Lip C_*) b(w). The source (V2, Definition 2.1) has the same imprecision.

Change: "let Lip(l) ≥ 1 be a common Lipschitz constant, with respect to the maximum norm ‖·‖_∞ on ℝ^{[1,l]}, on [−2,2]^{[1,l]} of all π_{κ,J,K} whose J contains a value row". This also covers Step 2 of Theorem B, which uses ‖v′ − v‖₂ ≤ η(w), because ‖·‖_∞ ≤ ‖·‖₂. Polynomials are Lipschitz in every norm on a compact cube, so the constant exists.

### R6. The Introduction contradicts Definition II-data about the signature sets (line 184)
Quote: "bounded-gap signature sets $S_l=\{2^l(2i+1):i\ge0\}$ with an additional allowedness rule".

Problem. Definition II-data(i) (line 1972) takes i ≥ 1, and Section 3 uses this throughout:
- min S_l = 3·2^l (Proposition II-bank(a), Remark II-corrections(a): S₁ = {6, 10, 14, …});
- Z₀ contains the powers 2^r;
- the FD schedule K_FD = {2^r}.

With i ≥ 0 the powers 2^l would belong to S_l, which changes Z₀ and H_l.
Change: "$i\ge1$".

### R7. Remark scope (c) claims the FD targets are removable, but a Section 4 proof uses them (lines 2975–2977)
Quote: "The fresh-dominated targets serve only a negative statement (dead zones forced by positive mismatch); they can be removed from the schedule without affecting any positive statement below."

Problem.
- The lemma of Section 4 whose part (e) states s_max(l) → ∞ (lines 3074–3075) is proved through the FD targets (lines 3098–3099: "At the stages $l'=\mathfrak j(2^r,m')$ the targets are fresh-dominated …"). That fact is then used to take l_f ≥ max F (line 3105).
- The modified design D^{U1′} of Section 5 also uses FD stages (line 6554).

So the claim is contradicted by the paper's own dependencies, and its proof is missing.

Change: either delete the sentence, or replace it with: "they are used below only to see that s_max(l) → ∞, which also follows without them. The targets (y^{(i)}) are norm dense in S_{q*}, so their supports are not contained in a finite set, and every y^{(i)} is allowed and scheduled at some stage (proof of (T-d)). Removing them affects no positive statement about T_final; D^{U1′} must then be modified accordingly." If you keep the sentence, add this argument to the proof of the Section 4 lemma, part (e).

### R8. The last assertion of Corollary Rkt is not proved (lines 878–890)
Quote: "In particular, for fixed $(\Phi_P^2,s_Q)$ the relative positions of the coordinates of $\Omega$ are functions of the ratios $(\mathsf r_k)_{k\in\Omega}$ alone."

Problem. The proof establishes the identities, R < 1 and a > 𝗄R, but not that (a, 𝗄) are determined by (R, Φ_P², s_Q). The quadratic relation has two roots in general. Proposition Rkt(i) in Section 5 gives only local smooth dependence (implicit function theorem), not uniqueness.

Change: add to the proof: "Put c₀ := Φ_P² + s_Q. Then a is a root of G(a) := a² − (a + c₀)²R² − c₀. On the half-line {a > c₀R/(1 − R)}, which is equivalent to a > 𝗄R, we have G′(a) = 2(a − 𝗄R²) > 0 because a > 𝗄R ≥ 𝗄R². So G has at most one root there. Since the true a lies there, a is determined by (R, Φ_P², s_Q), and hence so are 𝗄 = a + c₀ and ϱ_k = 𝗋_k𝗄/Φ(k)." With this, the paragraph at lines 892–899 also becomes a consequence of a proved statement. You may additionally point to Proposition Rkt(ii).

---

## 2. Optional suggestions

- **O1. Remark quantifiers (lines 2790–2798).** Insert the companion into the stated order, as in V1-ref and U4-ref: "… then, for each level l, a clean sub-window w_l; then the exactifying companion f^#_{w_l} (Definition II-companionw; it depends on f and w_l only); then g and ρ; then the data at each scale t ∈ 𝒲(w_l)". The task-level requirement "companions after f" is satisfied by the construction, but it is not recorded in the remark.
- **O2. Remark resonance (b) (lines 478–484).** "must contain $-\Delta d_m\psi_m$ in $b^+-b^-$ off the supports of the block parts" is exact only for one block. In general, off Σ(ω) one has b⁺ − b⁻ = −W_Δ = −Σ_m Δd_m ψ_m (Lemma sandwich). Also state the sign condition precisely: z_j W_Δ(j) ≤ 0 at contacts and W_Δ(j) = 0 at free coordinates outside Σ(ω), instead of "where ψ_m is z-signed".
- **O3. Paragraph after Lemma shift (lines 1522–1525).** Justify "a fixed non-degenerate peak of f remains a peak" and "C^#, σ^#, M^# are close". Use Lemma cost(i), Lemma T2(a) (θ̄ is Lipschitz), and |𝗏_k(ζ̂^#) − 𝗏_k(ζ̂)| ≤ Δ_m/Φ(k)², so the strict inequality 𝗏_k > θ̄ persists. Alternatively, move the statement into a remark.
- **O4. Remark VT(b), (c) (lines 1838–1847).** Label the numerics as such, e.g. "(numerical evidence; not used)". The "order s₁/t²" of the junction mismatch is an upper bound proved in U3-ref F6a; that it is attained is generic and supported by numerics only, so say "of order up to s₁/t² (generically attained)".
- **O5. Remark cost (a) (lines 993–1003).** "cannot be replaced by a λ-weighted one" is argued only when the scalars do not move. Say "cannot in general be replaced". At a common strict non-peak the change of λ_k w_k is linear in the unweighted u_k(δ), and the scalar changes are O(Δ_m), i.e. of weighted size. Cite Z3's numerics as evidence that the unweighted term is attained.
- **O6. Introduction, lines 130–131.** "satisfies the hypotheses of [I, Theorem 8.2] verbatim" should read "satisfies (T-a)–(T-d), (P1)–(P3) of [I, Theorem 8.2] verbatim (its conclusions, which are all that [I, Section 8] uses)". This matches Lemma GW(b).
- **O7. Definition II-constants (c), Łojasiewicz constants (lines 2158–2167).** Mention the case of an empty zero set: if Z_S = ∅, then Σ_{π∈S} π² ≥ c_S > 0 on the cube, and only the alternative β ≥ 1/C can occur. Also say that 2/N_L comes from dist(·, Z_S)^N ≤ C Σπ² ≤ C|S|β².
- **O8. Lemma raise (e) (line 1020).** "with ε_e := ‖e^# − e‖_H ≤ 1" reads as a hypothesis. Say "assume ε_e ≤ 1 (true when ‖U*Δa‖ ≤ ν/2, by (b))".
- **O9. Lemma U (lines 1110 and 1126–1129).** Kind [1] uses the constant 3, where the source Y1-ref F3 uses 2 and Y2 Lemma U′ uses 3 together with gap ≥ t²/2. The paper drops the lower bound on the gap entirely, which is justified by Y1-ref F3. One sentence citing both sources would preempt doubts. The proof as written is self-contained (it uses c_♭ ≤ 1/6).
- **O10. Proposition II-bank(a) (lines 2701–2702).** Instead of the single example "s_max(10) = 9", which is admissible only for special schedules, state the general condition: the cruder bound fails whenever s_max(l) < 2^l.
- **O11. Lemma GW (GW3) (lines 2855–2856).** [I, Lemma 8.10] states |θ^±_l| ≤ 3λ_l/t. Quote it in that form and add "hence |Δθ_l| ≤ 6λ_l/t", so the reader does not look for a "6" in Part I.
- **O12. Cosmetic.** Overfull \hbox at line 2060 (the level-data display of step (5)).

---

## 3. Verification record (statement by statement)

For each statement: the source, whether it is proved in the source (after the referee fixes), whether the hypotheses match, and my check of the proof in the paper.

### Section 2
- **Subsection 2.1.**
  - f[a′,z′]: [I, Remark 8.22(c)] gives existence; uniqueness holds because f = a + L*w. [I, Proposition 1.10(c)] gives the NA criterion in both directions. OK.
  - Definition II-companion: Z3 §1 (plus V3 §2 for raises). OK.
  - Lemma II-dnormer and Corollary II-defect: Z3 Lemma 1.2 and Corollary 1.3, refereed correct. Re-derived. OK.
  - Lemma II-resonance: Z3 Lemma 1.4. Re-derived, including λ_{k,m} = mΦ_m(k). OK.
  - Remark II-resonance(a): carries the Z3-ref Hoffman fix (|R**ẑ^#|/min Re). OK.
  - Remark II-resonance(b): see O2.
- **Subsection 2.2.**
  - Lemma II-T (a)–(f): Y1 Lemma T plus Y2 (perturbed version), refereed. I re-derived (a) through (f); the constants in (f)(i′) and (f)(ii′) are exact as stated. OK.
  - Lemma II-T2: Y1 T2 with V2-ref (P1) (k₀ = c allowed; the statement does not exclude it). Re-derived both bounds in (a) and (b). OK.
  - Corollary II-T3: OK.
  - The κ-definition and Lemma II-kappa: U1 Lemma 1.3, refereed and checked to 50 digits. Re-derived. OK.
  - Lemma II-kappader: U1 Lemma 1.4. Re-derived (i)–(iii) by hand and numerically. OK.
  - Corollary II-Rkt: U1-ref Lemma R-kt. Identities OK; last sentence see **R8**.
  - Lines 892–899 agree with U1-ref F1 and Proposition Rkt(ii).
- **Subsection 2.3.**
  - Counting bound (eq:II-count). Re-derived. OK.
  - Lemma II-cost: Z3 Lemma 3.1, refereed. Re-derived (scalars, clamp formula, (ii)–(iv)). OK.
  - Remark II-cost: see O5.
  - Lemma II-raise: V3 Lemma 2.1 and 2.2. In (e), ε_e without the factor ‖U‖ is still correct, since |u(Uh)| ≤ ‖U*u‖‖h‖ ≤ ‖h‖. OK.
  - Lemma II-RT: V3 Lemma 2.3. Re-derived. OK.
  - Following remark: see **R1**.
  - Corollary II-RT: V3 Corollary 2.4. Re-derived φ′(μ). OK.
- **Subsection 2.4.**
  - Lemma II-U combines Z3 Lemma U, Y2 Lemma U′ (kind [3]; t₁ and j₀ independent of A₂ and γ_B; c_♭ ≥ c₀γ_B/A₂), Y1-ref F3 (no gap ≥ t² requirement), Y4-ref Lemma P2 (banked and pulled supports, F ⊆ F_j), and V1-ref p3 (banks need not be contacts of f).
  - Every constraint in Steps 0–4 is checked. Kind [3] at degenerate peaks: [I, Lemma 3.4] is stated for ω vanishing on P, but its parts (a) and (d) use only ‖W‖_∞ = (1 − rd)M and |rd| ≤ C/(2M). Both hold here because ω vanishes on supp α_{j,m} and the inward sign holds. [I, Lemma 7.2] needs only ‖W − w‖_∞ ≤ (M − γ)/16, not support conditions. OK.
- **Subsection 2.5.**
  - Theorem II-ERT: V3 Theorem 2.5. With fixed θ_* = (1 − ρ²)/(12ρ²) instead of θ_j → 0, the arithmetic still closes (1/48 + 1/48 + 1/24 = 1/12; least scale 2T2^{−n}). Contractivity follows from p*(f_j + rh) ≤ s(r) for all r. OK.
  - Theorem II-E: Z3 Theorem E with Y2 E′, V1 E″ and Y4-ref P2. Every hypothesis of ERT is verified. ρ²(1 + η₀/2) ≤ 1 holds. Averaging is preserved because the conditions are linear and Γ_w is convex. Kind-[3] coordinates in two-piece data are strict non-peaks. OK.
- **Subsection 2.6.**
  - Lemma II-cert: U1 Lemma 1.1. OK.
  - Lemma II-shift: U1 Lemma 2.1. Re-derived the constant 8C³/(σM²Φ_P²). OK.
  - Lemma II-sandwich and Corollaries II-S1, II-S2: U3 Lemma S, S1, S2. OK.
  - Proposition II-S3: U3 Proposition S3, using ‖ψ_n‖_∞ ≤ ½ and ‖h‖₁ ≤ 3p*(h). OK.
  - Theorem II-NL: proof correct as a conditional statement; see **R2**.
  - Remark II-NL: labelled "not proved here"; see **R2**(b).
- **Subsection 2.7.**
  - Lemma II-VT: U3 Lemma VT, refereed correct. I re-derived every coordinate case of (II-VTstar) and the final sum; δ = (1 − ρ²κ_w)/2 as in [I, Theorem 7.18, Step 0]. OK.
  - Remark II-VT(c): the U3-ref F6 repair is labelled "Sketch, not proved here". OK (precision O4).

### Section 3
- **Base.**
  - Definition II-base and Lemma II-base: U2 (μ*_s = 2^{−2^{2^s}}) and U4 §1.1. I checked ‖U‖ = 1/16, the decay identity, and part (d) (Y ≥ 1, the case J(x) = 1). OK.
  - Remark II-whybase: motivation only; consistent with U2-ref item 1 and U4-ref (q4). OK.
- **Data and recursion.**
  - Definitions II-data and II-Tfinal: U4 §1.2–1.3 with U4-ref C1 (now B⋆(l) with s_t(l), per U2-ref Fix 2) and C7 ((GM) and (W6) only for l ≥ 2). I checked H_l, S_l, Z₀ and the bounded gaps. R3, R4, R5 and R6 concern this part.
- **Design constants and rate objects.**
  - Definition II-constants: V1 2.6 (patterns), V1 1.2 (H_tune), V2 Definitions 2.1–2.2 (minors, Łojasiewicz constants via [BCR, Corollary 2.6.7]), Y1 and Y2 (Hoffman constants). Gaps: R3, R4, R5. The Łojasiewicz definition is correct (monotone in N; the constant 1 + inf C is admissible).
  - Definition II-rates: (O1)–(O7) are V1 (R1)–(R7); (O8) and (O9) are V2 with V2-ref P3; (O10)–(O12) are U2-ref Fix 2. The convention value 1 for m > N follows V1-ref p0.
  - Lemma II-ratescheme: OK (the count 3l + |T(l)|; all values in [0, ∞]).
- **Well-foundedness and admissibility.**
  - Lemma II-W: U4 Lemma W with U4-ref (q1). (GM) excludes length ≤ δ^max/8, so A_l is nonempty and compact. OK, modulo R3/R4.
  - Remark II-corrections: (a) is U4-ref C7; arithmetic re-checked (H₁ = 1/60, δ^max₁ = ½, c₁ ≤ 2^{m(1)+1}/240). (b) is U4-ref (q3), labelled "not used". OK.
  - Theorem II-lemmaB: U4 Theorem 2.2. Re-derived (T-a)–(T-d), (P1), (P2), including the 8/9 estimate. OK.
  - Remark II-blocks: correct; [I, Lemma 1.5] transfers density, not rows.
- **Window arithmetic and design features.**
  - Proposition II-subwindows: U4 Theorem 2.2(c),(d) with U4-ref (q8). Re-derived (a)–(f), including log₂(1/b) ≤ 11N_L n. OK.
  - Proposition II-features: U4 Theorem 2.3. (SF_ι) comes from (W7) plus (P2); for FD, |y_l(j_l)| ≥ 16/17 > 1/4. OK.
  - Proposition II-bank: U4-ref C1 and (q7), with U2-ref Fix 2. Re-derived (a)–(e). OK.
  - Remark II-baseindep: a meta-statement (U4-ref F2), "checked where it occurs". OK.
- **Clean sub-windows.**
  - Definition II-clean, Theorem II-clean and Corollary II-clean: Y1 Theorem 2, V1 Theorem 2′, V2 Lemma 2.1. Pigeonhole over ω(l) + 1 disjoint bands. OK.
  - Remark II-quantifiers: correct but incomplete (O1). The design is fixed before f (Lemma II-W, Lemma II-ratescheme). The companion depends on (f, w) only (Definition II-companionw, lines 3734 ff.). The data come after g, ρ and t.
- **Generic window use.**
  - Lemma II-GW: U4 Lemma GW. Re-derived (GW2) (exponent 24l³), (GW3) via [I, Lemma 8.10], and (b) against [I, Theorem 8.2] (P2)–(P3). OK.
  - Remark II-GWuse: a description of the later proofs (U4-ref: monotone in Des). OK.
  - Proposition II-RSwindow: U2 §1.1 window factor, adapted to sub-windows. Re-derived (a)–(c), including y^{1/2} − log₂y − 2 ≥ 0 for y ≥ 64. OK.
  - Remark II-scope: (a) and (b) OK; (c) see **R7**.

### Overclaiming check
- Sections 2–3 never claim Lemma Z, density, Master Theorem IV/IV.1, U3 (S2a), Y4's (UN+), or Z1's exposed-face statement.
- Sketches appear only in labelled remarks (Remark NL, Remark VT(c)).
- The only overclaims found are R2 and R7.

### Number of required fixes: 8 (R1–R8). Optional suggestions: 12 (O1–O12).
