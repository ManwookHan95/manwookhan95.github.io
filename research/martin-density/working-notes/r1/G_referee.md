# Referee report on strategy G (literature and tools survey), file `r1/G_notes.md`

Role: adversarial referee. Date: 2026-10-08.
Setting and notation are those of the briefing and of G_notes §1: canonical base q with B_q = B_{c_0} + U(B_H),
p = q + ||L·||_V, block set I nonempty (finite, or I = N).
Labels: **PROVED** (complete argument given here or verified line by line), **SKETCH**, **HEURISTIC**, **FALSE**,
**OPEN**. "CITED (excerpt)" means a literature statement that I could confirm only through search-engine excerpts.

---------------------------------------------------------------------------------------------------------

## 0. Verdict in brief

1. **Every claim the notes label PROVED that I was asked to check is correct.** I re-derived all of them; §2 lists
   what was checked and the minor slips. The quality of Part 3 is high.
2. **One conceptual error that matters for strategy.** The "free radius" use of the recentering lemma is FALSE. It
   appears in 6.3.3 "Possible use", open question (Q2), and executive summary 0.2(5)(a), which calls it one of the
   two most promising devices. The radius is pinned to ||S||: the corrected operator satisfies
   ||A − S|| ≥ ||(A − S)z_0|| = ||λa − Sz_0|| ≥ λ − ||S||. For E = ℓ_2^2 and large λ, the "corrected" operator is
   (λf/f(z_0), g − (g(z_0)/f(z_0))f). This rescales the first row by λ/f(z_0), so it is not an approximation of S.
   Moreover, for every λ the hypothesis of the lemma already forces S*ξ to attain its norm at z_0. See §3.2
   (computation plus a numerical check).
3. **The survey's main negative conclusion is correct**: no published domain-side density theorem applies. There
   are five errors on the periphery:
   - AHSP is misclassified. Every finite-dimensional space, including ℓ_2^2, *has* AHSP, and AHSP only concerns
     the domain ℓ_1 (§3.1).
   - The RSE corollary's hypothesis, which the notes call "not guaranteed", in fact always holds for Martín's space
     (§3.3).
   - Read's lifting mechanism is dismissed for a wrong reason: Prop. 3.1 does not exclude it, and Read's own space
     is a counterexample to the inference (§3.4).
   - Uhl's theorem is misquoted (§3.5).
   - The BPB remark in 4.10 is a non sequitur (§3.5).
4. **Both imports that Part 3 depends on can be eliminated.** (I3) (strict convexity of p**, unique normer, forced
   decomposition) and (I2) (two-lines property) each have a short in-house proof, valid for every nonempty I and
   needing neither the unavailable [Recovery] note nor the transfer of Martín's theorem to the canonical base
   (§4.1, §4.2).
5. **Strengthenings (all PROVED in §4).**
   - X* = (ℓ_1, p*) is *not L-embedded*. This is stronger than Prop. 3.7 and confirms the second half of
     Remark 3.7.1, which the notes leave unproved.
   - NA((c_0,p), F) is *meagre* in L((c_0,p), F) for every finite-dimensional F ≠ 0. This makes the
     CITED-conditional Remark 3.4.1 unconditional.
   - Every finite-dimensional quotient of (c_0, p) is strictly convex.
   - The NA approximants of a given f have an exact characterization (§4.7). This is the most useful item for the
     overall goal.
6. **Literature access.**
   - WebFetch to arxiv.org and to every mirror tried (ugr.es, digibug.ugr.es, fu-berlin.de) failed with DNS
     errors.
   - curl to export.arxiv.org received a proxy 403.
   - Only search excerpts were available, the same situation the notes report.
   - §5 lists what was confirmed and what was not.

---------------------------------------------------------------------------------------------------------

## 1. Method

- Read BRIEFING.md, Preprint A, Preprint B and G_notes.md in full.
- Re-derived every PROVED item line by line (§2).
- Tried to break each applicability assessment of Part 4 against the structure of p, and found four of the five
  errors listed in §0(3).
- Ran numerical experiments (scripts in `scratchpad/refG/`):
  - `recenter.py`: 6000 random instances of the recentering lemma (domain ℓ_1^n, range ℓ_2^2, minimal admissible
    radius and its multiples). There were 0 failures, and the bound ||A − S|| ≥ λ − ||S|| was asserted in every
    instance.
  - `flat.py`: exact flatness of q along far coordinates (§4.8).
  - `threshold_fast.py`: exact-KKT check of the block threshold lemma. In 60 random instances, 280 coordinates were
    above the threshold, with 0 violations of w(n) = M sign z(n).
- Searched the literature with WebSearch (§5).

---------------------------------------------------------------------------------------------------------

## 2. Claim-by-claim verdicts

| # | Claim (notes' label) | Verdict | Notes |
|---|---|---|---|
| 1 | L2.1 attainment criterion (PROVED) | correct | Both directions hold for every Banach F. Finite dimension is used only to get a maximizing φ (compactness of S_{F*}). For ℓ_2^2: ||(f,g)|| ≤ 1 iff p*(f+tg) ≤ (1+t²)^{1/2} for all t (put t = tan θ; the limit t → ∞ gives p*(g) ≤ 1). Hence (R1). |
| 2 | L2.6 = (R2) (PROVED) | correct | r̃_f is the largest sublinear minorant of r_f: concatenating decompositions gives subadditivity, evenness of r_f gives symmetry, and r̃_f ≥ 0. A linear g satisfies g ≤ r_f iff g ≤ r̃_f. Hahn–Banach together with r̃_f ≤ p gives continuous g with g(x) = r̃_f(x). |
| 3 | P3.1 no compact-image operators (PROVED mod (I2)) | correct | Only "NA(X) has no 2-dimensional subspace" is needed; §4.2 proves the full two-lines property in-house for every I. For a norm-one projection, P(B) = B ∩ PX. For (c), a limit of operators of rank ≤ 1 has rank ≤ 1. Caveat: Remark 3.1.1 and 4.13 overreach, see §3.4. |
| 4 | L3.2.0 asymptotic flatness (PROVED) | correct | For q the flatness is in fact *exact*: q(x+te_n) = q(x) and ∇q(x+te_n) = ∇q(x) whenever n ∉ supp ∇q(x) and \|t\| ≤ q(x)(1−\|z_n\|) (§4.8). |
| 5 | P3.2 no strongly exposed points (PROVED) | correct | Verified, including liminf p(y_n − x) ≥ δ inf_n p(e_n) > 0. |
| 6 | T3.3 fails property A (PROVED) | correct | Verified (LUR at u = Sx/λ with u_n^+ + u_n^- = 2u). It is also an immediate corollary of Lindenstrauss' Theorem 2 together with P3.2: property A plus an equivalent LUR norm forces B_X to be the closed convex hull of its strongly exposed points (CITED (excerpt), restated and sharpened in JMRZ). So "new" is overstated, but the proof is valid. The remark that the mechanism is void for finite rank is correct. |
| 7 | C3.4 ASE route closed (PROVED) | correct | ASE ≠ ∅ implies SE ≠ ∅ (verified). JMRZ converse confirmed as quoted: for X and Y* separable, NA(X,Y) residual implies ASE(X,Y) dense (CITED (excerpt)). §4.4 proves directly that NA(X,F) is meagre for every finite-dimensional F, so the conditional is unnecessary. |
| 8 | P3.6 no L/M-structure (PROVED mod (I3)) | correct | (a)–(e) verified (Kakutani; a C(K) of dimension ≥ 2 is not strictly convex). The hypothesis is proved in §4.1. |
| 9 | P3.7 not M-embedded (PROVED mod HWW) | correct | Verified: Φ ∈ X^⊥, ‖Φ‖ = 1 via χ_N, and the upper bound via the decomposition e_n* + L*w. §4.3 upgrades this to "X* is not L-embedded", which implies the claim without identifying the complementary summand. |
| 10 | T3.8 Fréchet smoothness (PROVED) | correct | Key step verified: Σ_j \|a_n(j)\|(1−\|z_j\|) → 0 with z ∈ c_0 (compactness of U) confines the ℓ_1-mass to a finite set. The block part uses w*-to-norm continuity of L*. The proof also covers q itself. I could not check novelty. |
| 11 | P3.9 continuity of forced decomposition (PROVED mod (I3)) | correct | Verified. Uses uniqueness of the normer and injectivity of R_m** (dense tails); both are proved in §4.1. |
| 12 | P3.10 asymptotic dual norm (PROVED) | correct | Verified: p*(h) = min max(q*(a), ‖w‖); asymptotic ℓ_1-additivity; ‖U*b_n‖ → 0; crossing at s = 1+βq_0. Wording: "far coordinate functionals are never mates" means that for each c > 0, c·e_n* ∉ C(f) for all n ≥ n(c). |
| 13 | 6.3 recentering and near-ball lemmas (PROVED) | correct | The symmetric-containment proof is correct and short. Numerics: 0 failures in 6000 instances. The λ = 1 reading is correct but tautological (with Tz_0 = e_1 the containment *is* ‖T‖ ≤ 1). **The "Possible use" paragraph, (Q2) and 0.2(5)(a) are FALSE; see entry 21 and §3.2.** |
| 14 | 6.1–6.2 lift and permanence (PROVED) | correct | Verified: d_p(T) ≤ η(1+η)‖T‖_p + (1+η)d_{q_η}(T). Rigidity in strictly convex F holds as stated, for lifts S + h⊗v with \|h\| ≤ s and h(z_0) = s(z_0). |
| 15 | 6.6.3 = (R4) (PROVED) | correct | (i)–(iii) and the controlled approximation verified, including p(y'_n) → 1/q_0. Upgraded to an "iff" in §4.7. |
| 16 | 4.16.1 WMP/CPP irrelevant (PROVED) | correct | Han–Kim's definitions confirmed: CPP means T+K ∈ NA whenever ‖T+K‖ > ‖T‖, and WMP implies CPP (CITED (excerpt)). T = 0 gives NA(X,F) = L(X,F), hence X reflexive by James' theorem. |
| 17 | Survey: no applicable theorem (PROVED) | correct_with_fixable_gaps | The domain-side conclusion is right. Range side: the AHSP statement is false (§3.1). Also: the RSE assessment is wrong (§3.3), the Read-mechanism justification is wrong (§3.4), Uhl is misquoted (§3.5), the BPB inference is a non sequitur (§3.5), and QNA is omitted (harmless; void for compact operators). |
| 18 | (c_0,p) fails (m_∞) (PROVED) | correct | Verified, including lim_n q(x+ce_n) = max(q(x), c). |
| 19 | (ℓ_1,q*) L-embedded (SKETCH) | correct | The computation q***(Φ) = q*(πΦ) + ‖Φ−πΦ‖ is a complete proof (§4.3). "The block term destroys this" is TRUE but unproved in the notes; Prop. 3.7 shows only non-M-embeddedness. Proof in §4.3. The slogan "compact perturbations of the dual norm preserve L-embeddedness" needs the perturbation to be ‖U*·‖ with U: H → X, so that it vanishes on X^⊥. |
| 20 | Kuratowski reduction (R3) (SKETCH) | correct | The outline is complete: Blaschke selection; w*-separation by an x ∈ c_0 of a point from a norm-compact convex set; Lipschitz extension from a dense set (r̃_f ≤ p); diagonalization. "Equivalently" in (R3) should read "restated as". It is a sufficient condition, not an equivalence with density. |
| 21 | 6.3.3 "Possible use", (Q2), 0.2(5)(a): free radius λ ≫ 1 (HEURISTIC, but promoted) | **wrong** | §3.2. The radius is pinned: ‖A−S‖ ≥ λ − ‖S‖. |
| 22 | 4.15: strict convexity of X/ker T "not guaranteed" | **wrong** | §3.3. It always holds because p* is smooth (p** strictly convex). |
| 23 | 4.13: "Prop. 3.1 excludes such norms in the relevant sense" | **wrong** (justification) | §3.4. Read's space satisfies the conclusion of Prop. 3.1 and still admits the decompositions. Whether p_N admits Read-type decompositions is OPEN. |
| 24 | 0.2(2) and table 4.20: AHSP "would settle B for ℓ_2^2", "not known for ℓ_2^2" | **wrong** | §3.1. |
| 25 | 4.10: "any positive proof … should be non-quantitative" | unclear | Non sequitur. The ACKLM example concerns another pair. BPBp for ((c_0,p), ℓ_2^2) is OPEN (and would imply density). |
| 26 | 6.6.1 (FALSE principle, SKETCH counterexample) | correct | The sketch is essentially complete. b_n = a^{(n)} + βe*_{N_n}, z_n = z on [1,n] and 1 at N_n; then y_n → ξ/q_0 weak* and ∇q(y_n) = b_n/q*(b_n), with ℓ_1-mass β/(1+β) escaping. |
| 27 | Imports (I2), (I3) for I = N | correct | Both are provable in-house in a few lines (§4.1, §4.2). |

---------------------------------------------------------------------------------------------------------

## 3. Errors and corrections

### 3.1 AHSP is misclassified (0.2(2), table 4.20). FALSE as stated.

Quoted step (0.2(2)): "Property β, quasi-β, ACK_ρ structure, AHSP and the universal BPB range property all give
density NA(X, F) *for every X*. Applied to F = ℓ_2^2 they would settle the open question … None is known for
ℓ_2^2." The table repeats this: "β, quasi-β, ACK_ρ, AHSP | range-side | not known for ℓ_2^2 | would settle B for
ℓ_2^2".

Correction (CITED (excerpt)):
- The approximate hyperplane series property characterizes the range spaces Y for which the pair (ℓ_1, Y) has the
  Bishop–Phelps–Bollobás property (Acosta–Aron–García–Maestre 2008).
- Finite-dimensional spaces, uniformly convex spaces, C(K) and L_1(μ) are standard examples of spaces with AHSP
  (excerpts from Choi–Kim–Lee–Martín and Acosta–Aron–García-Pacheco).

So ℓ_2^2 **has** AHSP. AHSP says nothing about domains other than ℓ_1 (and L_1(μ)-type domains), so it cannot settle
property B. The other four items are correctly described: β, quasi-β, ACK_ρ and the universal BPB range property
would each give property B for ℓ_2^2. β and quasi-β fail for ℓ_2^2; I re-checked quasi-β directly (any A_e
accumulating at e* must contain ±e* itself, and then nearby members of A violate ρ(e*) < 1).

### 3.2 The "free radius" recentering heuristic (6.3.3, Q2, 0.2(5)(a)). FALSE.

Quoted steps:
- 6.3.3: "choose S close to T and z_0 ∈ X such that S(B_X) is contained in a disc of radius λ (possibly λ ≫ 1)
  tangent near Sz_0. … That is a weaker requirement than f ∈ NA plus g ∈ C(f) with the same λ, because λ is free."
- (Q2): "find x′ ∈ S_p and λ ∈ [1, ∞) with … (ii) … a disc of radius λ … Then 6.3 gives an NA operator within O(ε)
  of (f, ρg)."
- 0.2(5)(a) lists this as one of the two most promising devices.

**Counter-argument (PROVED).** In the recentering lemma, Az_0 = λa, so for z_0 ∈ B_Z
  ||A − S|| ≥ ||(A − S)z_0|| = ||λa − Sz_0|| ≥ λ − ||Sz_0|| ≥ λ − ||S||.
A small correction therefore forces λ ≤ ||S|| + ||A − S||. Conversely ||A|| = λ gives λ ≥ ||S|| − ||A − S||, so
**λ = ||S|| + O(||A − S||)**: the radius is not free.

Explicitly, for E = ℓ_2^2, a = ξ = e_1 and S = (f, g):
  A = S + (f/f(z_0)) ⊗ (λe_1 − Sz_0) = ( λ f/f(z_0), g − (g(z_0)/f(z_0)) f ).
For λ ≫ 1 the first row is multiplied by λ/f(z_0). The lemma then says only that a rescaled operator attains its
norm.

For **every** λ > 0 (exact identity, from (u + λ)² + v² ≤ λ² with u = f(x) − f(z_0), v = g(x) − g(z_0)) the
hypothesis reads
  f(z_0) − f(x) ≥ [ (f(x) − f(z_0))² + (g(x) − g(z_0))² ] / (2λ)   for all x ∈ B_X.
This requires f to *attain* its maximum at z_0, with a quadratic margin of order 1/λ. In a Hilbert range ξ(a) = 1
forces ξ = a, so after a rotation this is the general case: the hypothesis always includes "S*a is norm-attaining at
z_0". The lemma therefore presupposes the very attainment that is in question for the first row. What it adds is the
rank-one correction of the remaining rows (for λ = f(z_0) = ||f||: A = (f, g − (g(z_0)/f(z_0)) f)).

Numerics (`recenter.py`): with S = ((1, 0.3, −0.2), (0, 0.9, 0.5)) on ℓ_1^3 and ||S|| = 1:

| λ | ||A − S|| |
|---|---|
| 1 | 0 |
| 2 | 1 |
| 10 | 9 |

Corrected statement. At λ = ||S|| + o(1) the lemma is a perturbative restatement of norm attainment: S(B_Z) lies in
a ball of radius λ ≈ ||S|| whose centre Sz_0 − λa is small and whose boundary passes through Sz_0. It is genuinely
useful (it is how Preprint B's transfer theorem closes, with λ_n → 1), but it is *equivalent* up to a rank-one
correction to the existence of a nearby NA operator, not a relaxation. (Q2) should be withdrawn or reformulated with
λ → ||S||.

### 3.3 RSE applicability (4.15). The hypothesis that the notes call "not guaranteed" always holds.

Quoted step: "Is p̂ strictly convex? … Strict convexity of p̂ is equivalent to smoothness of p* restricted to
span{f, g}, which is not guaranteed."

**Proposition (PROVED).** For every finite-rank T on X = (c_0, p) (any nonempty I), the quotient X/ker T is strictly
convex.

*Proof.*
1. p** is strictly convex (§4.1).
2. If Z* is strictly convex then Z is smooth. Applied to Z = (ℓ_1, p*), this shows p* is Gâteaux smooth on
   ℓ_1 \ {0}.
3. (X/ker T)* is isometric to (ker T)^⊥ = T*(F*), a finite-dimensional subspace of (ℓ_1, p*). The restriction of a
   Gâteaux-smooth norm to a subspace is Gâteaux smooth.
4. A finite-dimensional space E is strictly convex iff E* is smooth. Hence X/ker T is strictly convex. ∎

Consequence. By [CdRFJM, Cor. 2.15] (CITED (excerpt): T ∈ Fin ∩ NA with X/ker T strictly convex implies
T ∈ cl(Fin ∩ RSE)), NA(X,F) ∩ Fin ⊂ cl(RSE(X,F) ∩ Fin) for Martín's space. So density of NA and density of RSE are
equivalent for finite-dimensional F. This is a modest upgrade tool, as the notes say, but the stated obstacle does
not exist.

### 3.4 The Read mechanism is dismissed for a wrong reason (4.13; also Remark 3.1.1). FALSE inference.

Quoted step (4.13): "In Martín's space the block seminorm ||L·|| is **not** small relative to any norm with
contractive projections (Prop. 3.1 excludes such norms in the relevant sense)."

Prop. 3.1 is a statement about p alone. The Read mechanism (Preprint B) needs, for each η > 0, a decomposition
p = q_η + s_η with s_η a seminorm, s_η ≤ ηq_η, and d_{q_η}(T) → 0. One way to get the last condition is that q_η
admits contractive finite-rank projections whose adjoints converge pointwise. Then factorization happens for the
*auxiliary* norm q_η, and the lift lemma transfers to p.

**Counterexample to the inference.**
- Read's norm p_R satisfies the conclusion of Prop. 3.1: NA(p_R) contains no 2-dimensional subspace (Rmoutil; KLM).
  So any finite-rank P with P(B) closed has rank ≤ 1, by Lemma 2.3.
- Yet p_R = q_N + s_N with P_M q_N-contractive and s_N ≤ η_N q_N (Preprint B Lemma trunc).
- Preprint B obtains density of NA ∩ Fin in K exactly through this route.

So Prop. 3.1 does not obstruct Read-type decompositions.

What is actually missing (OPEN): does p_N admit decompositions p_N = q'_η + s'_η with s'_η a seminorm ≤ ηq'_η and
NA((c_0, q'_η), F) dense (for instance through contractive finite-rank projections, or through the primal transfer
theorem)? A positive answer would settle density via the permanence theorem and Remark martin-tail. The notes' 7.2
shows only that the obvious within-block truncation is not of this form. This route should stay on the list of open
directions instead of being marked excluded.

### 3.5 Minor issues

- **Uhl (4.3).** Quoted: "NA(L_1[0,1], Y) is dense iff Y has the RNP (Uhl)". The equivalence holds for *strictly
  convex* Y. Without strict convexity it fails: NA(L_1, L_1) is dense (Iwanik), although L_1 lacks the RNP
  (CITED (excerpt)). This is irrelevant to Martín's space.
- **BPB remark (4.10).** Quoted: "So any positive proof for Martín's space should be non-quantitative". The ACKLM
  example (a pair failing BPBp while density holds) concerns a different pair and implies nothing about
  ((c_0,p), ℓ_2^2). Whether this pair has BPBp is OPEN.
- **Remark 3.7.1 slogan.** "Compact perturbations of the dual norm do [preserve L-embeddedness]" is true for
  perturbations ||U*·|| with U: H → X, because their bidual extension vanishes on X^⊥ (that is what the computation
  uses). For a compact A on X* that is not an adjoint, the computation breaks.
- **QNA omission.** Every compact operator is quasi norm attaining, so QNA is void for finite-dimensional ranges.
  It is harmless but belongs in the list of void tools next to Zizler.
- **Citations not verified** (the notes flag them honestly):
  - "Question 6" numbering and the "most irritating" quote: not found. One excerpt (Martín 2014) refers to the
    Johnson–Wolfe *compact-operator* question as "Question 2".
  - KLMW item numbers: not found.

---------------------------------------------------------------------------------------------------------

## 4. Results that remove the imports or strengthen the notes

Standing facts used below, all from the briefing's setting:
- L*w = T( Σ_{m,n} w_m(n) m2^{-m-n} e_{n,m} ) ∈ Y for w ∈ V*, and T is injective, so L* is injective on V*.
- Y ∩ c_00 = {0}.
- NA(q) = c_00 (DGS lemma).
- Every tail of (u_{n,m})_n is dense in S_{q*}.
- Φ_m(n) ≤ 2^{-m-n} → 0.
- The block threshold lemma (Preprint B), which I re-proved: if w(z) = N(w)|z| with N(w) = 1, then
  z/|z| = α + D²w/C with ||α||_1 ≤ 1, w(α) = M := ||w||_∞, and C = ||Dw||_2 > 0. Hence |z(n)| > |z|(M/C)Φ(n)²
  implies w(n) = M sign z(n).

### 4.1 Strict convexity of p** and the forced decomposition, for every nonempty I. PROVED.

(Replaces the imported (I3); the [Recovery] note is not needed.)

First, p**(ξ) = q**(ξ) + ||L**ξ||_V. This holds because B_{p*} = B_{q*} + L*(B_{V*}) is w*-compact, and L**ξ ∈ V
since L is compact.

*R_m** is injective.* (R_m**ζ)(n) = mΦ_m(n) ζ(u_{n,m}). If all of these vanish, then ζ vanishes on a dense subset of
S_{q*}, so ζ = 0.

*Strict convexity.* Let p**(ξ) = p**(η) = p**((ξ+η)/2) = 1.
1. Both q** and |R_m**·|_m are seminorms, so for every m:
   |R_m**(ξ+η)|_m = |R_m**ξ|_m + |R_m**η|_m.
2. Fix m ∈ I and put z_1 = R_m**ξ, z_2 = R_m**η. Both are nonzero by injectivity.
3. Take w with N_m(w) = 1 and w(z_1 + z_2) = |z_1 + z_2|_m. Then w(z_i) = |z_i|_m for i = 1, 2, with a common
   M = ||w||_∞ > 0 and C > 0.
4. Suppose ξ, η are not positively proportional. Then some v ∈ S_{q*} has ξ(v) > 0 > η(v): if ξ, η are linearly
   independent, use surjectivity of v ↦ (ξ(v), η(v)); if η = λξ with λ < 0, take any v with ξ(v) > 0.
5. Choose n_j → ∞ with u_{n_j,m} → v. The threshold condition for z_1 at n_j reads
   m|ξ(u_{n_j,m})| > |z_1|_m (M/C) Φ_m(n_j).
   It holds for large j because Φ_m(n_j) → 0. So w(n_j) = M eventually.
6. In the same way, w(n_j) = −M eventually. This contradicts M > 0.
7. Hence η = λξ with λ > 0, and λ = 1 by normalization. ∎

*Corollary (forced decomposition).* Every f ∈ S_{p*} has a unique normer ξ ∈ S_{p**} (the normers form a convex
subset of the sphere). Take any f = a + L*w with q*(a) ≤ 1 and ||w|| ≤ 1. Then
  1 = f(ξ) = a(ξ) + w(L**ξ) ≤ q**(ξ) + ||L**ξ|| = 1,
so a(ξ) = q**(ξ) =: q_0 and w(L**ξ) = ||L**ξ||. Moreover q_0 ∈ (0,1): q_0 > 0 because ξ ≠ 0, and q_0 < 1 because
L**ξ ≠ 0. Since a(ξ) ≤ q*(a) q_0, we get q*(a) = 1.

All components R_m**ξ are nonzero and each |·|_m is smooth (N_m is strictly convex because D_m* is injective).
So w = J_V(L**ξ) is unique, and a = f − L*w. The argument also works for Martín's original base, since it uses only
(M1)–(M7). This answers the first half of the notes' (Q3) affirmatively.

### 4.2 Two-lines property for every nonempty I. PROVED.

(Replaces the imported (I2) used in P3.1.)

**Claim.** If f, g ∈ NA(p) are linearly independent and α, β ≠ 0, then αf + βg ∉ NA(p). Hence, for every
2-dimensional E ⊂ X*, NA(p) ∩ E lies in two lines.

*Proof.*
1. For a nonzero NA functional k, write k = c_k(a_k + L*w_k), where:
   - c_k = p*(k);
   - x_k ∈ S_p is a point where k attains its norm;
   - a_k = ∇q(x_k) ∈ c_00;
   - w_k = J_V(Lx_k).
2. Replacing f, g by ±f, ±g, assume α, β > 0, and suppose h = αf + βg is NA. Then
   c_h a_h − αc_f a_f − βc_g a_g = L*(αc_f w_f + βc_g w_g − c_h w_h).
   The left side lies in c_00 and the right side in Y, so both vanish. Injectivity of L* gives
   c_h w_h = αc_f w_f + βc_g w_g.
3. If x_f, x_g were dependent, say x_g = μx_f, then g/c_g = ∇p(x_g) = sign(μ)∇p(x_f) = sign(μ) f/c_f. This
   contradicts independence. So x_f, x_g are independent.
4. Hence there are v, v' ∈ S_{q*} with:
   - v(x_f) > 0 and v(x_g) > 0;
   - v'(x_f) > 0 > v'(x_g);
   - v(x_h) ≠ 0 and v'(x_h) ≠ 0.
   Each sign pattern defines a nonempty open cone, and removing the hyperplane {v(x_h) = 0} keeps it nonempty.
5. Fix m ∈ I. Along n_j with u_{n_j,m} → v, the threshold lemma applied to R_m x_k gives
   w_{k,m}(n_j) = M_k sign v(x_k) eventually, for k = f, g, h, where M_k = ||w_{k,m}||_∞ > 0.
6. Comparing coordinates n_j, and then doing the same with v', gives
   c_h M_h = αc_f M_f + βc_g M_g   and   c_h M_h = |αc_f M_f − βc_g M_g|.
   These are incompatible. ∎

### 4.3 L-embeddedness: the base dual is L-embedded, Martín's dual is not. PROVED.

*(a) (ℓ_1, q*) is L-embedded.* For Φ ∈ ℓ_1** = ℓ_∞*, let π be restriction to c_0. Since B_{q**} = B_{ℓ_∞} + U(B_H)
and U(H) ⊂ c_0,
  q***(Φ) = ||Φ||_{ℓ_∞*} + ||U*(πΦ)|| = ||πΦ||_1 + ||Φ − πΦ|| + ||U*πΦ|| = q*(πΦ) + q***(Φ − πΦ),
where the last step uses π(Φ − πΦ) = 0. So π is an L-projection.

*(b) Z := (ℓ_1, p*) is not L-embedded (for any L-projection).*

Setup:
- Let Φ ∈ Z** be a w*-cluster point of (e_n*) along a free ultrafilter 𝒰.
- ||Φ|| ≤ lim q*(e_n*) = 1.
- ||Φ|| ≥ Φ(χ_N)/p**(χ_N) → 1, where χ_N = 1_{[N,∞)} and p**(χ_N) ≤ 1 + ||L**χ_N|| → 1. So ||Φ|| = 1.
- For |t| ≤ 1 and ||w||_{V*} ≤ 1, w*-lower semicontinuity and the decomposition e_n* + L*(tw) give
  ||tL*w + Φ|| ≤ lim_𝒰 max(q*(e_n*), |t|) = 1.

Suppose Z** = Z ⊕_1 Z_s with L-projection P. Put u = PΦ. Then
  p*(u + tL*w) + ||Φ − u|| ≤ 1 = p*(u) + ||Φ − u||,
so p*(u + tL*w) ≤ p*(u) for all |t| ≤ 1 and all w ∈ B_{V*}.
- If u = 0, then L*w = 0 for all w, which is absurd.
- If u ≠ 0, let ξ_u be a normer of u. Then p*(u) ≥ p*(u + L*w) ≥ p*(u) + w(L**ξ_u) for all w ∈ B_{V*}. Hence
  L**ξ_u = 0, so ξ_u = 0 by injectivity, which is absurd. ∎

Since M-embedded spaces have L-embedded duals, this implies Prop. 3.7. It also confirms that it is precisely the
block term that destroys L-embeddedness: with L = 0 the argument fails, consistent with (a).

### 4.4 NA((c_0,p), F) is meagre in L((c_0,p), F) for every finite-dimensional F ≠ 0. PROVED.

(Unconditional replacement for Remark 3.4.1.)

1. NA(p) \ {0} ⊂ ∪_j K_j, where K_j ranges over the compact sets [1/k, k]·F_n, with
   F_n = [(S_{q*} ∩ E_n) + K] ∩ S_{p*} as in Preprint A.
2. For a compact K ⊂ X*, let A(K) = {T : ∃ φ ∈ S_{F*} with T*φ ∈ K}.
   - A(K) is closed: if T_i → T and φ_i → φ (by compactness of S_{F*}), then T*φ ∈ K.
   - A(K) has empty interior. Identify L(X,F) with (X*)^d through a basis (e_i*) of F*. Choose c > 0 with
     max_i |φ_i| ≥ c on S_{F*}. Then A(K) = ∪_i A_i(K), where A_i(K) is the closed subset of A(K) defined by
     requiring |φ_i| ≥ c.
   - If A(K) had interior, Baire's theorem would give some A_i(K) an open box U_1 × … × U_d inside it. Fix
     x_l ∈ U_l for l ≠ i. Then U_i would sit inside
     {(k − Σ_{l≠i} φ_l x_l)/φ_i : k ∈ K, φ ∈ S_{F*}, |φ_i| ≥ c},
     a compact set. That is impossible in the infinite-dimensional space X*.
3. By Lemma 2.1, NA(X,F) \ {0} ⊂ ∪_j A(K_j), a countable union of nowhere dense sets. ∎

Sanity check: meagreness is compatible with density. For instance NA(c_0, F) is meagre (NA(c_0) = c_00) and dense.
So this neither helps nor hurts the density question. It only closes every residuality route.

### 4.5 Finite-dimensional quotients are strictly convex. PROVED. See §3.3.

### 4.6 Theorem 3.3 as a corollary. PROVED mod CITED (excerpt).

Lindenstrauss' Theorem 2 (as restated in JMRZ): if X has property A and admits an equivalent LUR norm, then B_X is the
closed convex hull of its strongly exposed points. Here c_0 admits an LUR norm and B_p has no strongly exposed points
(P3.2). Hence (c_0,p) fails A.

### 4.7 Exact characterization of the NA approximants of a given f. PROVED.

(Combines the notes' P3.9 with 6.6.2 and 6.6.3.)

Let f ∈ S_{p*} have normer ξ, contact number q_0, forced decomposition f = a + L*w, and base contact
z := ξ/q_0 − U(U*a/||U*a||) ∈ B_{ℓ_∞}, so that z = sign a on supp a. For f'_n ∈ NA(p) ∩ S_{p*}, the following are
equivalent:

(i) f'_n → f in norm.

(ii) f'_n = ∇p(y'_n), where:
- y'_n = z'_n + U(U*a'_n/||U*a'_n||);
- a'_n ∈ c_00 ∩ S_{q*} and a'_n → a in ℓ_1;
- z'_n ∈ c_0, ||z'_n||_∞ ≤ 1, z'_n = sign a'_n on supp a'_n;
- z'_n → z coordinatewise.

*Proof.*

(ii) ⇒ (i):
1. y'_n → ξ/q_0 weak*, because z'_n → z boundedly coordinatewise and the U-part converges in norm.
2. p(y'_n) = 1 + ||Ly'_n|| → 1/q_0.
3. So x_n = y'_n/p(y'_n) → ξ weak*, and ∇q(x_n) = a'_n → a.
4. L*J_V(Lx_n) → L*w in norm, by compactness of L and smoothness of the V-norm at L**ξ.
5. Hence ∇p(x_n) → f.

(i) ⇒ (ii):
1. Write f'_n = ∇p(x'_n) with x'_n ∈ S_p.
2. By P3.9: a'_n := ∇q(x'_n) → a in norm, x'_n → ξ weak*, and q(x'_n) → q_0.
3. By 6.6.3(iii), y'_n := x'_n/q(x'_n) has the stated form.
4. Since y'_n → ξ/q_0 weak* and the U-part converges in norm, z'_n → z coordinatewise. ∎

Coordinatewise convergence only constrains each fixed coordinate in the limit, so for every n the coordinates of
z'_n outside a finite window W_n (with W_n ↑ N) are free, subject to |·| ≤ 1 and membership in c_0. This is the
complete list of degrees of freedom available for the (R3) program.

### 4.8 Byproduct: exact flatness of q along far coordinates. PROVED.

Let x ≠ 0 with x/q(x) = z + Uh_x, a_x = ∇q(x) ∈ c_00, n ∉ supp a_x and |t| ≤ q(x)(1 − |z_n|).
1. (x + te_n)/q(x) ∈ B_q, so q(x + te_n) ≤ q(x).
2. a_x(x + te_n) = q(x), so q(x + te_n) ≥ q(x).
3. Hence q(x + te_n) = q(x) and ∇q(x + te_n) = a_x.
4. Consequently ∇p(x + te_n) − ∇p(x) = L*(J_V(L(x+te_n)) − J_V(Lx)) → 0 in norm as n → ∞.

So far-coordinate moves of a normer change the NA functional only through the block term, by o(1). This is the
primal form of the notes' 5.3 and of the briefing's (R4) freedom. Numerically checked in `flat.py`.

---------------------------------------------------------------------------------------------------------

## 5. Literature spot-checks

Access: every WebFetch failed (DNS for arxiv.org, ugr.es, digibug.ugr.es, fu-berlin.de), and curl to
export.arxiv.org received a proxy 403. Only WebSearch excerpts and paraphrases were available, so everything below is
CITED (excerpt).

| Item in notes | Status | Source of confirmation |
|---|---|---|
| Martín 2025: no nontrivial cones; segment property; two lines in every 2-dimensional subspace; ≤ 4 points in codimension-2 quotients; base renorming via DGSR Thm 9(4) | confirmed | arXiv:2406.07273 record and abstract excerpts; v1 phrased the 2-dimensional result as "at most four points" |
| KLMW: nontrivial cone suffices for rank-two NA operators into every Y with dim ≥ 2; dense NA subspace gives finite-rank density; Hilbert-valued case in §4 (a "Prop. 4.1" mate criterion); finite-rank density holds for domains C_0(L), L_1(μ), preduals of ℓ_1 | confirmed | arXiv:1905.08272 excerpts |
| JMRZ: for X, Y* separable, NA(X,Y) residual implies ASE(X,Y) dense; ASE dense into nontrivial Y implies SE(X) dense; Lindenstrauss' Theorem 2 (A + LUR renorming) restated and sharpened | confirmed | arXiv:2203.04023 excerpts; JFA 284 (2023) 109746 |
| AHSP characterizes (ℓ_1, Y) BPBp; finite-dimensional spaces have AHSP | confirmed; **contradicts the notes** | Acosta–Aron–García-Pacheco (Banach J. Math. Anal. 2017) and Choi–Kim–Lee–Martín excerpts |
| Han–Kim: definitions of WMP and CPP; WMP ⟹ CPP | confirmed | arXiv:2402.12070 record; RACSAM 119 (2025) art. 53 |
| CdRFJM Cor. 2.15 (finite-rank NA with strictly convex X/ker T is approximable by finite-rank RSE) | confirmed | arXiv:2503.18581 excerpts |
| GMRV 2026: complex C(K) → C(S) density (complex Johnson–Wolfe) | confirmed | arXiv:2605.28466 abstract |
| Johnson–Wolfe: real C(K) domains; range L_1 (real) and L_1-preduals; NA(C(K),C(S)) dense (real) | confirmed | EuDML 218261; Martín's notes; Acosta survey excerpts |
| CGKS: Γ-flat (Asplund ⊂ Γ-flat) into ACK_ρ ranges; β spaces and uniform algebras have ACK_ρ | confirmed | arXiv:1704.01768 and arXiv:2204.01991 excerpts |
| Fovelle 2024: property B for finite-dimensional spaces open even for ℓ_2^2 | confirmed | arXiv:2402.19067 excerpt |
| Uhl: dense iff RNP | **only for strictly convex Y** | Pacific J. Math. 63 (1976); arXiv:2110.02066 excerpt |
| "Question 6", "most irritating" | not found | the only JW question number found is "Question 2" (compact operators), in Martín 2014 |

Sources (search results used):
- [arXiv:2406.07273](https://arxiv.org/abs/2406.07273), [digibug record](https://digibug.ugr.es/handle/10481/102416)
- [arXiv:1905.08272](https://arxiv.org/abs/1905.08272)
- [arXiv:2203.04023](https://arxiv.org/abs/2203.04023), [JFA version](https://www.sciencedirect.com/science/article/pii/S0022123622003664)
- [AHSP and related properties, Banach J. Math. Anal. 11(2)](https://projecteuclid.org/journals/banach-journal-of-mathematical-analysis/volume-11/issue-2/The-approximate-hyperplane-series-property-and-related-properties/10.1215/17358787-3819279.full), [Choi–Kim–Lee–Martín AHSP preprint](https://www.ugr.es/local/mmartins/Curriculum/Papers/pre2014-cklm-AHSP.pdf), [arXiv:1708.08679](https://arxiv.org/pdf/1708.08679)
- [arXiv:2402.12070](https://arxiv.org/abs/2402.12070), [RACSAM version](https://link.springer.com/article/10.1007/s13398-025-01718-z)
- [arXiv:2503.18581](https://arxiv.org/abs/2503.18581)
- [arXiv:2605.28466](https://arxiv.org/pdf/2605.28466)
- [Johnson–Wolfe, EuDML](https://eudml.org/doc/218261)
- [arXiv:1704.01768](https://arxiv.org/abs/1704.01768), [arXiv:2204.01991](https://arxiv.org/pdf/2204.01991)
- [arXiv:2402.19067](https://arxiv.org/pdf/2402.19067)
- [Uhl 1976](https://msp.org/pjm/1976/63-1/p23.xhtml), [arXiv:2110.02066](https://arxiv.org/pdf/2110.02066)
- [arXiv:1306.1155](https://arxiv.org/pdf/1306.1155)
- [Martín, 2024 Badajoz notes](https://www.ugr.es/~mmartins/Curriculum/Charlas/2024_Badajoz_notes.pdf)

---------------------------------------------------------------------------------------------------------

## 6. Single most valuable idea for the overall goal

The **norm-controlled parametrization of all NA approximants of a given f**. It is assembled from the notes' Prop. 3.9
and 6.6.2–6.6.3, and made into an equivalence in §4.7:

> f'_n ∈ NA ∩ S_{p*} tends to f **iff** f'_n = ∇p(z'_n + U(U*a'_n/||U*a'_n||)), with a'_n ∈ c_00 ∩ S_{q*} → a in ℓ_1
> and z'_n → z coordinatewise. The coordinates of z'_n outside any finite window are completely free.

Why this one:
- Combined with the Kuratowski reduction (R3), it turns the density question into a concrete primal construction
  problem. One must choose the free far coordinates of z'_n (equivalently, by §4.8, far moves of the normer) so that
  the mate fibres C(∇p(y'_n)) reach ρ r̃_f(x_i) − ε in finitely many prescribed directions.
- The survey shows, correctly (after the fixes in §3), that every off-the-shelf route is closed. This
  parametrization is therefore exactly the space in which a positive proof must live.
- The strongest new quantitative tool in the notes is Prop. 3.10, the exact asymptotic dual-norm formula. It shows
  that escaping base ℓ_1-mass costs at least βq_0 at first order. It is the natural instrument for proving that the
  free far coordinates act only through the block term.

---------------------------------------------------------------------------------------------------------

## 7. Recommendations to the author of G_notes

1. Withdraw the free-radius heuristic: rewrite 6.3.3 "Possible use", (Q2) and 0.2(5)(a) with λ = ||S|| + o(1).
2. Fix the AHSP statement; fix 4.15 (§3.3); replace the 4.13 justification with the open question in §3.4; correct
   Uhl; drop the BPB inference; add QNA to the void list.
3. Replace the imports (I2) and (I3) by §4.1–§4.2. All of Part 3 then becomes self-contained for every nonempty I,
   and the dependence on the unavailable [Recovery] note disappears.
4. Upgrade Remark 3.4.1 to §4.4 (PROVED, unconditional), Prop. 3.7 to §4.3(b), and Remark 3.7.1's sketch to §4.3(a).
5. Note that Theorem 3.3 is a direct consequence of Lindenstrauss' Theorem 2 and Prop. 3.2.
6. Use §4.7 and §4.8 as the working parametrization for the (R3) program.
