# Referee report on `paper/martin_density_note.tex` (2678 lines)

Scope: I read the whole file and checked every proof line by line against BRIEFING.md, BRIEFING_R2.md (with both addenda),
martin_paper_summary.md, Preprint A (residual_recovery.tex), Preprint B (hmr_c0_renormings.tex), r1/A_referee, r1/C_referee,
r1/D_notes (§11), r1/G_referee (§4.7), r2/P1_referee, and (for Addendum 2) r2/P2A_referee.
I compiled the file three times with pdflatex in a scratch copy. There are no errors, no undefined references or citations, and no
multiply defined labels. There are about 15 overfull hboxes (item 27).

## Overall verdict

The mathematics in Sections 1–6 is essentially correct. I re-derived these by hand:
- Lemmas dualball, threshold, rigidity and Propositions forced, smooth, continuity, approximants, reduction, primal;
- Lemma pair, Theorem compact, Theorem lowerlimit, Corollary finite, Theorem transitivity;
- Lemmas algebra, base, block, Proposition expansion, Lemma slack, Proposition scale, Theorem transport, Corollaries lsc and check,
  Proposition shifted, Theorem shifted, Theorem joint;
- Theorem averaging and Corollaries ladder and decomposition (all constants);
- Lemma boxtails, Theorem weighted, Lemmas basetrunc and blocktrunc, Theorem carriers;
- Lemmas slice, excess, flat, overshoot, Theorem tamefibre (Steps 1–5), Theorem transfer (Steps 1–6), Remark gammaw,
  Lemma localformula (all derivatives), Proposition lowerbound (base and block suprema, including c_Q = 0), Theorem tame;
- Proposition intrinsic, Corollary linear, Lemma T, Lemma firstrow, Proposition twopiece, Theorem defect, Proposition nonrecovery,
  Proposition exact, Corollary twosided.

The referee corrections that were required are all applied:
- the coordinatewise radius (A G1);
- the hypothesis t²/C_m → 0 for infinitely many blocks (A G2, Corollary decomposition and Remark G2);
- "shifts strictly enlarge the class" is downgraded to OPEN (A G3, Remark shiftopen);
- C Prop 8.1 has its cofinite free set (K finite in Proposition lowerbound and Theorem tame);
- P1 3.5(d)/3.6 are treated as a sketch and not used (Remark resonancetypes);
- the P1 referee modification R2 of T (the set Λ(i) and the choice of s_l) is built into Lemma T, so Proposition nonrecovery is
  proved for the T that is actually constructed.

Still required, most severe first:
- an empty placeholder section, and an open problem that contradicts refereed results recorded in BRIEFING_R2 Addendum 2;
- a genuine gap in Theorem locsplit for infinitely many blocks, although the theorem is stated for "any nonempty block set";
- one false side remark (finite certificates with H = 1 are locally split);
- a wrong displayed bound in Step 1 of Theorem transfer;
- a statement/proof mismatch in Theorem transfer;
- several overclaims in the status section;
- citation numbers that do not match Preprint B;
- notation clashes, the worst of them inside a single proof.

## Required fixes (most severe first)

1. **Placeholder section and an outdated open problem.**
   - Line 2539, `% PLACEHOLDER-ENGINEERED`: Section `sec:engineered` contains only one paragraph announcing content
     ("This section will treat recovery of resonant mates ..."). The text after Proposition nonrecovery (lines 2449–2451, "for instance
     by putting base mass on the contact windows (Section~\ref{sec:engineered})") points to this empty section.
   - Problem `prob:resonant` (lines 2606–2613) states as open: "Recover the switching mates of Theorem~\ref{thm:defect} along
     engineered norm-attaining approximants". BRIEFING_R2 Addendum 2 records this as PROVED and refereed:
     - P2A Thm 2.1 / N2 Thm 1: every d-neutral exact two-piece switching mate is in Ls(f), with no rate condition on T;
     - "ALL explicit defect mates of P1's example are in Ls(f)". The P2A referee finds only the trivial gap ρ ≥ 1/32 and the missing
       hypothesis g ∈ C(f), which holds here.
   - The same problem's sentence "The case ... ($d_-<d_+$) is not covered by any known argument" is also inaccurate. With
     Δd := d₋ − d₊, that case is Δd < 0, and Addendum 2 lists:
     - N2 Thm 3, recovery under (PC);
     - the N2 referee's Lemma R, which needs only (PC*);
     - "Every exact resonance with a single carrier non-peak is recovered whatever the sign of Δd".
   - Fix: either write Section 7 from P2A Thm 2.1 / N2 Thm 1, with the referee fixes (state g ∈ C(f), ρ ≥ 1/32 or the C4 fix, quantifier
     order), or delete the section. In both cases, rewrite Problem `prob:resonant` and the status paragraph (lines 2575–2584) so that
     they say the defect of Theorem `thm:defect` is a defect of the intrinsic mechanisms only. The abstract should say so too.
     Results that are conditional on (TC), (PC*) or (S) must be stated with those hypotheses, or as remarks.

2. **Gap in Theorem `thm:locsplit` for infinite I (lines 1394–1432).**
   - The statement says "Let $I$ be any nonempty block set". The proof chooses a finite I₀ depending on δ ("Choose a finite set $I_0$
     of blocks with $\|v\|\sum_{m\notin I_0}m2^{-m}<\delta$"). It then claims "a range $|t|\le\tau_5$, independent of $\delta$".
   - This claim is false when I is infinite. τ₅ is the minimum over m ∈ I₀ of the block ranges τ_{3,m} of Lemma blocktrunc. These
     satisfy τ_{3,m} ≤ t₁ = C_m/(2‖D_m(ω−dw)‖+2) ≲ C_m ≤ 2^{-m}, so τ₅ shrinks as I₀ grows.
   - The "Mate" step needs ρδ' ≤ (1−ρ²)τ₅/(3ρ), where δ' ≥ the error from dropping blocks, which is about Σ_{m∉I₀} m2^{-m}‖v_m‖. This
     can fail. D_notes Thm 11.6 has the same flaw.
   - Remark `rem:blocks` (lines 169–173: "the one place where $I=\N$ needs an extra hypothesis is Corollary~\ref{cor:decomposition}")
     is therefore also inaccurate.
   - Fix (a): restrict Theorem locsplit and Corollary `cor:splitcontractive` to finite I. This is enough for density, by Remark blocks.
   - Fix (b), a repair:
     - add to Lemma `lem:blocktrunc` the all-t bound N(w+tv'') ≤ N(w+tv) + (|ϰ|+‖Δ‖)|t|, as in D Lemma 11.5(b);
     - choose the truncation accuracy per block, δ_m ≤ ε(1−ρ²)τ_{3,m}, so that the first-order error is ≤ ερ(1−ρ²)t² beyond τ_{3,m};
     - use the local-split range τ, which does not depend on δ, in the mate step.
   - Either way, update Remark blocks.

3. **False side remark, lines 1282–1283.** "Every finite certificate direction with $H\le1$ is locally split
   (Proposition~\ref{prop:expansion})".
   - Proposition expansion only gives q*(a+tb) ≤ 1 + (t²/2)H(1+κ|t|). For H = 1 and κ > 0 this exceeds s(t) = 1 + t²/2 − t⁴/8 + ….
   - Lemma base shows that for H = 1 the true value exceeds 1 + t²/2 for one sign of t when ⟨e,h⟩ < 0.
   - Fix: replace "$H\le1$" by "$H<1$", or say "$\rho g_c$ with $\rho<1$".

4. **Wrong displayed bound in Step 1 of Theorem `thm:transfer`, lines 1768–1769.**
   - Quoted: "$\|D_m(w'_{m,N}+tv'_{m,N})\|\le C'_{m,N}+td'_{m,N}M'_{m,N}+\frac{t^2}2H'_{m,N}C'_{m,N}\theta(t)$".
   - Since ‖h_⊥‖² = H'C' and the remainder is t²‖h_⊥‖²/(2Y) with Y ≈ C', the correct term is $\frac{t^2}{2}H'_{m,N}\theta(t)$, with
     no factor C'. Step 5 (line 1876) already uses the correct form, $\frac{H'_{m,N}\theta(t)}2$.
   - Fix line 1769.

5. **Statement and proof of Theorem `thm:transfer` do not match.**
   - Statement (lines 1740–1741): "there are $g'_N\in\Cset(f'_N)$ ... with $g'_N\to\rho g$".
   - Proof: g'_N is defined in Step 1 and converges to g; the conclusion is "Hence $\rho g'_N\in\Cset(f'_N)$ and $\rho g'_N\to\rho g$"
     (line 1888).
   - Fix: rename (e.g. the mates are ρg'_N), or change the statement to "$\rho g'_N\in\Cset(f'_N)$, $g'_N\to g$".

6. **Notation clashes inside the proof of Theorem `thm:transfer` (lines 1747–1886).**
   - η is the normer for the whole of Section 5 ("In this subsection $\eta=\xi$", line 1725). It is then reused as a small number
     ("Fix ... $\eta\in(0,\frac12]$", line 1747) and as η_N := p*(g'_N − g) (line 1886).
   - L (the operator Lx = (R_m x)_m) is redefined as the level "$L:=\Gamma_w(g)/2+\eta$".
   - Λ_m is the index set {k ∉ supp ω_m : |w_m(k)| ≥ γ_m} (line 1776) and, in the same proof, the level "$\Lambda_m:=H_m/2-\tau_me_{y,m}=L$"
     (line 1809).
   - T_m clashes with the operator T and with the box tails T_m(σ;ω).
   - Fix: rename (e.g. ε₀ for the small number, ℓ_* for the level, 𝔏_m for the index set, 𝒯_m for the target).

7. **Missing hypothesis in Lemma `lem:block`(c), lines 760–762.** "(c) if $|d\sigma|\le\frac12$ and ... then
   $\|W(\sigma)\|_\infty=(1-d\sigma)M$ and equality holds in (b)".
   - The formula in (b) needs Y = C + dσM > 0, and |dσ| ≤ ½ does not imply this, because C_m ≤ 2^{-m} can be much smaller than M/2.
   - Fix: add "and $Y>0$" to (c). Part (d) is unaffected, since there Y ≥ C/2.

8. **Overclaim, lines 2602–2604.** "the approximants in Problem~\ref{prob:main} must in general depend on the mate and cannot be the
   canonical truncations".
   - Proposition nonrecovery only shows that the canonical truncations fail. Nothing shows that one engineered sequence could not
     recover the whole fibre.
   - Fix: delete "must in general depend on the mate and".

9. **Wrong logic in Problem `prob:approx`, lines 2628–2629.** "a proof of non-membership would require a sequence $f_n\to f$ with
   $g\notin\Li_n\Cset(f_n)$".
   - By Corollary lsc, such a sequence is sufficient to show g ∉ cl Cert(f). It is not necessary.
   - Fix: "one way to prove non-membership is to exhibit ...".

10. **Missing hypothesis in Remark `rem:gammaw`, lines 1914–1915.** "Thus Theorem~\ref{thm:transfer} covers every balanced shifted
    certificate whose direction lies in $S(f)$".
    - Theorem transfer needs a ∈ c₀₀.
    - Directions of finite certificates always lie in S(f), so that clause is vacuous.
    - Fix: "When $a\in c_{00}$, Theorem~\ref{thm:transfer} covers every $g_c\in\Cset(f)$ with $c$ a shifted certificate and
      $H^{\rm sh}(c)\le1$." The proof is correct; P1 referee C1 gives the stronger bound Λ ≥ Γ_w + 2q₀κ_q.

11. **Theorem `thm:defect`, lines 2355–2362, and the status section, line 2577.**
    - g_{K₁} depends on c, and g_{K₁} ∈ C(f) holds only for 0 < c ≤ c_* (Proposition twopiece). State this in the theorem.
    - Line 2577, "the defect $\Cset(f)\setminus\mathcal K(f)$ is infinite dimensional": a set difference is not a subspace. Write
      "spans an infinite-dimensional space", as Theorem defect does.

12. **Theorem `thm:carriers`, "In particular" clause (lines 1468–1472).** "In particular this holds when $\inf_i\gamma_i>0$ and
    $\|u_{k_i,m}-v\|\le K'\lambda_i$ ...". The clause must keep hypothesis (c) (H_* ≤ 1) explicitly. Fix: "... provided (c) holds".

13. **Citations that do not match the sources.**
    - Line 198, "[PrB, Lemma 5.6]": in the available Preprint B (`\newtheorem{theorem}{Theorem}[section]` with shared counters), the
      block-threshold lemma is **Lemma 6.5**. The cited lemma states only the implication; the decomposition and the off-peak formula are
      proved here, which is fine.
    - Line 2546, `\cite[Remark martin-tail]{PrB}`: a label name has leaked into the text. In Preprint B this is **Remark 6.9**.
    - Lines 529, 640 and 2552, "[PrA, Theorem 2.1/2.2]": the available Preprint A file has no `\newtheorem` lines, so the numbers cannot
      be checked. If Preprint A shares counters like Preprint B, the residual-recovery theorem is Theorem 2.4 (after Corollaries 2.2 and
      2.3). Verify, or cite by name ("Global compactness", "Residual uniform recovery").

14. **Proposition `prop:intrinsic`(b), line 2147.** "Conditions (C1), (C2) say exactly that $g_c\in S(f)$". (C1) also requires
    ‖b/a‖_∞ < ∞, which S(f) does not. Replace "say exactly that" by "imply".

15. **Clash inside the proof of Theorem `thm:joint`, lines 1044–1053.** G and G_n denote the tuple of mates and its transport, while
    the proof says "(the sets $G_n$ do not depend on $b$)", meaning the index sets G_n of Theorem transport. Rename one of them.

16. **The notation $Dg_m$ for degenerate peaks (line 1601) reads as D applied to g_m.** D_m is the diagonal operator. Use
    $\mathrm{Dg}_m$ or $\mathcal D_m$.

17. **Garbled final paragraph, lines 2640–2641.** "density into $\ell_2^{d+1}$ implies that tuples in $\Cset_d(f)/\sqrt d$ are recovered
    along a common sequence". The intended statement (A_notes l.244) is about tuples $(g_1,\dots,g_d)/\sqrt d$ with $g_i\in\Cset(f)$,
    which lie in $\Cset_d(f)$. Rewrite it that way.

18. **Unproved claims in remarks need a status label.**
    - Remark `rem:twopiece`(b), "conversely one can show that every mate is supported in $\{1\}\cup K'$ ...": this is P1 Thm 6.1,
      PROVED and refereed, but it is not proved here. Say "(proved in the companion notes; not used)" or add the proof.
    - Remark `rem:transfer`(b), "In finite-dimensional models ... the second-order coefficient can be strictly larger than $\Gamma_w$":
      label as numerical evidence (C referee §1.17).
    - Remark `rem:transfer`(c), "The same estimates performed at $\xi$ ... show": label as a sketch.
    - Remark `rem:kinks`(a), "is at most $0.296$ on both sides while $\Gamma_w=0.485$": state that this is an exact numerical
      computation in a finite analogue (C referee), not a theorem.
    - Remark `rem:kinks`(c), "they form a meagre set in the bidual face": this holds in the open part of the face with K = ∅, where
      Preprint A's residuality argument applies. Say so.

19. **Proposition `prop:approximants`, last sentence (lines 412–414).** "the coordinates of $z'_n$ outside a finite window may be chosen
    freely". The free coordinates must also avoid supp a'_n (where z'_n = sign a'_n), so the windows must contain supp a'_n. Add this.

20. **Corollary `cor:ladder`, lines 1134–1135.** "It suffices that the hypotheses hold along a geometric sequence of scales
    $t_12^{1-i}$". In the proof, t₁ is chosen depending on ρ. Write $t_*2^{1-i}$ (i ≥ 1) and take t₁ among these scales.

21. **Notation clashes in §6.2 (lines 2166–2212) with symbols in use throughout the paper.**

    | Symbol in §6.2 | Clashes with |
    |---|---|
    | α (= 1/(1+ν₁)) | α_m (threshold lemma) |
    | π_{k,m} | π_m (peak functionals, Lemma rigidity, Theorem tamefibre) |
    | ρ_l | ρ (damping factor) |
    | Λ(i) | Λ(S,Y) (Lemma localformula) |
    | κ | κ(c), κ_q |
    | h_l | h(b) |
    | K' | K (contacts) and the constants K, K' |
    | l, used both as an index and as the bijection l(n,m) | itself |

    Also Ω denotes the residual set, Ω ∈ V* in Proposition exact, and Ω_± in Corollary twosided. Rename the local symbols
    (e.g. α₁, ϖ_{k,m}, r_l, Λ_i, κ_u, h^{(l)}, ℓ(n,m)).

22. **Overloaded P^⊥ (line 685).** "where now $P^\perp$ projects onto $(D_mw_m)^\perp$", after P^⊥ was defined as the projection onto e^⊥
    (line 652). Use a separate symbol (P_m^⊥).

23. **Errors e_i versus the Hilbert vector e.** In Theorem averaging, e_i := p*(g − g_{c_i}) is used near e and e_j^*. Use ε_i or err_i.

24. **Bibliography.**
    - [Martin]: the article number "110815" cannot be checked against the sources (the summary gives only JFA 288 (2025)). Verify it.
    - [PrA] has no authors, and its date "October 2026" is unverified.
    - [PrB] has no year and no arXiv number.
    - Line 464 cites [KLMW] (arXiv:1905.08272) for the observation g(x)² ≤ p(x)² − f(x)² = 0. This is fine, but check that it is the
      intended reference (the rank-two criterion paper).

25. **Abstract (lines 52–58).**
    - "while $\Cset(f)$ is infinite dimensional": say "spans an infinite-dimensional space".
    - Add a sentence on recovery along engineered approximants (Addendum 2), or state explicitly that this question is open, consistent
      with item 1.

26. **Remark `rem:blocks` (lines 169–173).** Update it after item 2, and say explicitly that Theorem locsplit (as repaired or restricted)
    and Corollary splitcontractive are covered.

27. **Overfull hboxes, cosmetic.** Lines 1422–1432 (20.9pt), 206 (14.6pt), 509–525, 552, 685–690, 881–889, 1200, 1921–1926, 2042, 2193
    (11.2pt), 2200–2202. Break the long displays and inline formulas there.

## Points checked and found correct

These are not fixes; they are listed so the author knows what was verified.

- Global compactness: the Brezis–Lieb step, and the constant (s(t)−1)/q₀.
- Lower-limit theorem: Blaschke selection and the support-function Lipschitz bound.
- Lemma pair: the rotation argument.
- Lemma slack, constants: 2s(t) ≤ 3max(1,|t|); the window bound r_* = min(r, δ/(2κ+2), √δ).
- Theorem transport: ‖b_n/a_n‖ ≤ 2‖b/a‖ + |τ_n|, b_n(ẑ_n) = 0, liminf r ≥ r/2.
- Theorem shifted: the three-case flip/kink bound.
- Theorem averaging: (2+ρ²)/6 and the case |s| ≥ s₀.
- Corollary ladder: n ≥ 24ρ²K/(c₀(1−ρ²)).
- Corollary decomposition: H_m ≤ 1 + o(1) + O(τ²/C_m).
- Lemma basetrunc: |∂_βF_t| ≤ 2|t|³.
- Lemma blocktrunc: t₀ and t₁.
- Theorem carriers: the geometric sum ≤ 4|c|ρs.
- Theorem tamefibre: Steps 3–5, in particular δ'' = Rν_J + ζ/σ having zero peak sum.
- Theorem transfer: the bookkeeping identity via the margin identity, the sup-norm bound at k_*, Λ_b = L − η/q₀ + Σ|τ|ε₁ ≤ L.
- Lemma localformula: ∂_SΛ = M, ∂_YΛ = CY/|ζ|, ∂²_SΛ = Cc_Q/(|ζ|F₂).
- Proposition lowerbound: ‖P_{ĥ⊥}Dω̃‖² = ‖Dω‖² − d²C²/c_Q and the final identity (|ζ|/C)(‖Dω‖² − d²).
- Lemma T:
  - (T-b) and (T-c) with the constant 4/3;
  - (P3) margin 8ρ_l/5;
  - the choice of s_l;
  - every i is allowed at all large l, and i = 1 everywhere, since ρ_l < ε_* ≤ 1/72.
- Lemma firstrow: |u_{k,m}(ξ)| ≤ σ_m/m off P_m (Φ(k)|w(k)| ≤ C), and ϑ_mΦ_m(k) ≤ q₀π_{k,m}.
- Proposition twopiece: the first-order bracket sv(ẑ) = 0; c_*.
- Proposition nonrecovery: (MS) via Σ ≤ s²/c'²; strict non-peak because peaks have margin ≥ 0.
- Proposition exact and Corollary twosided.
