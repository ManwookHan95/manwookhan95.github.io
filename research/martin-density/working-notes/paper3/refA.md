# Referee report A on `martin_density_note_III.tex`: Sections 2 and 3

**Scope.** This report covers Section 2 (`sec:III-generic`, lines 360-1673, generic weights and status coherence) and Section 3 (`sec:III-UE`, lines 1674-3173, the violation-tolerant d-consistent engineered approximant).

**Sources.** Each statement was checked line by line against the following sources:
- r9/X1_notes.md and X1_referee.md; r9/X2_notes.md, X2_referee.md and X2_ref_notes.md;
- r11/cert0_report.md (cluster A), cert1_report.md (cluster B) and cert2_report.md (cluster C);
- r8/U1_referee.md;
- r11/K1_notes.md 3.1 and K1_ref_notes.md D (Lemma K1.S);
- the cited statements of Part II (paper2/martin_density_note_II.tex). Label numbers were checked against paper3/labII.txt and labI.txt.

Key identities were re-derived by hand wherever a proof was in doubt.

Line numbers refer to `paper3/martin_density_note_III.tex` as of 2026-10-11 04:33.

## 0. Verdict

**Section 2.** All the mathematics is sound, and every certification fix is present: K1, W-fix, KN-1/P-HOLD, F1, P-LIP/P-LIP+, P-SFAR, P-CY, P-CHOICE, C1-C6, D1, D2 and S-0 (see A.3 for the item-by-item check).
- The required fixes concern the following:
  - one false lemma as stated: Lemma 2.16(a) (`lem:III-Uscale`), homogeneity of the rate objects, which needs the variables removed by (X5) to be deleted;
  - one mislabelled definition: tiny/robust in Definition 2.13 must refer to moduli;
  - a quantifier-order slip: $C_*(L)$ is called a design constant but bounds $f$-dependent moves;
  - one missing threshold clause in (QC4): $\beta(b)\le\eta'/3$ is used but not implied;
  - two incorrect intermediate inequalities in the proof of Proposition 2.32 (`prop:III-KNtr`);
  - a hypothesis mismatch between Lemma 2.14(b) (`lem:III-floorrow`) and Proposition 2.32(a);
  - an uncovered case in the proof of Proposition 2.32: an inactive weak peak used as the (KN) lever;
  - an inaccurate claim that Definition 2.27 (`def:III-QCreq`) lists everything the section uses.
- None of these changes a conclusion. Required fixes R1-R8.

**Section 3.** The analytic core is correct, and the fixes of X2-ref, cert2 and K1.S are incorporated, with one exception: cert2 C2-7, the circularity of the radius, is missing (R11).
- The other required fixes concern:
  - a wrong cross-reference ([II, Theorem 5.67] for 5.68, eight times);
  - a missing hypothesis ($\Delta_1$) in Lemma 3.10;
  - the lever range of (U6)/Lemma 3.25(a);
  - the definition of $c_{\rm tiny}$;
  - a false justification in Lemma 3.20;
  - two small incorrect estimates.
- None of these changes a conclusion. Required fixes R9-R16.

**Totals.** 16 required fixes (R1-R16) and 22 optional suggestions (O1-O22).

**Overclaiming.** Neither section claims density or (LSC-trunc), and no heuristic or numerical material is presented as proof: the remarks marked "Heuristic" and "evidence only" are correctly labelled.
- Section 2 states its results for the designed operator only.
- Section 3's Theorem 3.26 is stated for $D^{U1'}$ with (D-lev) and (W$_{\exp}$) **under (KN$_{w,a}$)**, and Remark 3.29 says so.

**Numbering used in this report** (computed from the source; Section 1 has no numbered environments):
- 2.1 `lem:III-Rkt`; 2.3 `lem:III-alpha`; 2.4 `lem:III-K`; 2.6 `lem:III-floor`; 2.8 `def:III-pattern`; 2.9 `lem:III-Tblock`; 2.10 `lem:III-EC`;
- 2.11 `def:III-region`; 2.12 `lem:III-interior`; 2.13 `def:III-cone`; 2.14 `lem:III-floorrow`; 2.16 `lem:III-Uscale`; 2.17 `lem:III-weightfree`;
- 2.20 `lem:III-NLM`; 2.22 `lem:III-GEN`; 2.24 `lem:III-QC`; 2.26 `lem:III-loj`; 2.27 `def:III-QCreq`; 2.29 `lem:III-window`; 2.31 `lem:III-status`;
- 2.32 `prop:III-KNtr`; 2.34 `lem:III-drift`;
- 3.1-3.29 as in Part B below.

---

# Part A: Section 2 (generic weights and status coherence)

## A.1 Required fixes

**R1 (dependencies of the section; accuracy of a claim). Lines 440-442.**
- Quote: "the design $T_{\rm fin}$ of Section~\ref{sec:III-design} (all that is used of it is listed in Definition~\ref{def:III-QCreq})".
- Problem: this is not true. Section 2 also uses the following properties of $T_{\rm fin}$, none of which is in Definition 2.27:
  - (T-a) $\Phi_m(k)\le2^{-m-k}$ (proof of Lemma 2.4(a));
  - the weight decay $c_{l+1}\le c_l/4$, i.e. (W1) (proofs of Lemma 2.3(b) and Lemma 2.9, where $\sum_{l>L}\Phi_l^2\le c_{L+1}^2/8$);
  - (W5) $c_{L+1}\le2^{-\min S_{L+1}}$ and the signature-set geometry $s_1(l)\le L+3\cdot2^L$ (proof of Lemma 2.17(c));
  - the window properties of [II, Corollary 3.20(c)] ($\mathrm{Des}^2T_{\rm lo}\le1$; used after Lemma 2.9 and in the proof of Proposition 2.32);
  - the tuning machinery of [II, Lemmas 4.14, 4.15], with their hypotheses (T1), (T2), the bank coordinates $s'_{l''}(l)$ and the bounded gaps $2^{G(l)}\le\mathrm{Des}^{1/6}$ (Lemma 2.29, Step 4). The closing moves (C1), (C2) enter Definition 2.27 only through the constant $C_*$; see R4;
  - $s_{\rm far}(w)$ from [II, Lemma 5.50];
  - the lever construction of [II, Proposition 5.56] for blocks of kind (KN).
- Fix: replace the parenthesis by: "(besides the properties of $T_{\rm final}$ and $D^{U1'}$ used through Part II, namely (T-a), (W1), (W5), the signature sets with bounded gaps, the window properties of [II, Corollary 3.20] and the tools of [II, Subsections 4.2-4.3 and 5.6], the new requirements are listed in Definition 2.27)".

**R2 (Lemma 2.16(a) is false under the convention of Definition 2.13). Lines 875-879 and 1010-1021.**
- Quotes:
  - Definition 2.13 defines Γ♭ "by the rows (X1), (X3), (X5)", and the rate objects as "the minors of the matrix of $\Gamma^\flat(\kappa,a;r)$". So the (X5) unit rows and the columns of the inactive variables are part of the matrix; Lemma 2.17(a) also lists "(X5): unit rows".
  - Lemma 2.16(a) claims: "Every minor of the matrix of $\Gamma^\flat(\kappa,a;r)$ is homogeneous of degree $0$ or $1$ in $r^{(m)}$".
- Counterexample: take a (U)-block $m$, a coordinate $j\in E_c(w)$, and $l\in\Omega_a(m)$. The $2\times2$ minor with rows $\{(\mathrm X3)_m,(\mathrm X1)_j\}$ and columns $\{\Delta'_m,\gamma_l\}$ equals $u_l(j)-r_l\tau_m(j)$, which is not homogeneous in $r^{(m)}$. This minor is a rate object, and if it is tiny at $r(f)$, the rescaling $r^{(m)}\mapsto s\,r^{(m)}$ need not preserve its vanishing. The conclusion "maps $Z_\kappa$ into itself", used in the proof of Proposition 2.32(a), then fails.
- The proof silently uses a different convention: "By (X5), $\Delta'_m=0$; deleting this variable". This is the convention of X1 2.1(U) and cert0 3.4: "(X5) removes the variable $\Delta'_m$".
- Fix:
  1. In Definition 2.13 define the matrix of Γ♭ in the **active variables only**: delete the columns of the components declared inactive by (X5) and omit the (X5) rows. The rate objects (minors and cofactor polynomials) are those of this reduced matrix. The cone, as a set in the active coordinates, and its Hoffman constant are unchanged.
  2. Adapt the list in the proof of Lemma 2.17(a): drop "(X5): unit rows".
  3. Correct the sentence in the proof of Lemma 2.16(a), "the (X1) rows contain $r$ only through $\Delta'$-columns, which for block $m$ is deleted". The (X1) rows contain no ratio at all (entries $u_l(j)$, $-\tau_m(j)$, $\alpha_l$, $-\mathrm{vs}_l\lambda_l\alpha_l$). $r$ enters only through (X3) and (X4⁰).

**R3 (tiny/robust must refer to moduli). Lines 881-882.**
- Quote: "The pattern labels each of them \emph{tiny} or \emph{robust} (its value at $r(f)$ is $\le b$, resp.\ $\ge u$)."
- Problem: minors and cofactor polynomials are signed. With signed values, a minor equal to $-1/2$ at $r(f)$ would be labelled tiny, forced to vanish on $Z_\kappa$, and could make Step 1 of Proposition 2.32 impossible. Cleanness ([II, Definition 3.18, Theorem 3.19]) concerns values in $[0,\infty]$, i.e. moduli.
- Fix: "(its modulus at $r(f)$ is $\le b$, resp.\ $\ge u$)". Likewise "every robust rate object is $\ge u/2$" (Proposition 2.32, Step 3) and "$\ge u/4$" (Proposition 2.32(a)) should say "has modulus".

**R4 (quantifier order: $C_*(L)$ is not a design constant for ratios and statuses). (QC3), lines 1345-1348.**
- Quote: "here $C_*(L)\ge1$ is a design constant such that the closing moves (C1), (C2) of the assembly ([II, Subsection 4.3]) change every ratio by at most $C_*(L)b$ and every status of a coarse carrier by at most $C_*(L)b$ ([II, Lemma 4.19])".
- What Part II provides: value bounds $|\mathrm{val}_{l''}(f_1)-\mathrm{val}_{l''}(f)|\le C_*(l)b$, with $C_*(l)=|T(l)|+2$ ([II, Definition 3.6]; (A1) of [II, Theorem 5.7]; Step 0 of the proof of [II, Proposition 5.56]). [II, Lemma 4.19] concerns the companion with the donor raise and has $f$-constants ($C_f\mathrm{Des}^{1/6}\beta_w$).
- The bounds that follow for ratios and statuses carry $f$-dependent factors:
  - ratios: $\Delta(u/\varkappa)\le\Delta u/\varkappa+|u|\,|\Delta\varkappa|/\varkappa^2$, with $\varkappa_m\ge|\hat\zeta_m(f)|$ and $|\Delta\varkappa|\le C\mathrm{Des}\,b$;
  - statuses: $\Delta\varrho\le m\Delta u/(\Phi_l\bar\vartheta_m)+\varrho|\Delta\bar\vartheta|/\bar\vartheta$.
  
  Both carry $1/|\hat\zeta_m(f)|$, $1/\bar\vartheta_m(f)$ and $1/\Phi_l\le D(L)$. A design constant cannot bound them uniformly in $f$; the design-before-$f$ order is violated as written.
- Fix: keep $C_*(L):=|T(L)|+2$ as a bound in **value units**, and add the following sentence to (QC3): "for $L\ge l_f$ the closing moves change the active ratio vector (Euclidean norm) and every coarse status by at most $C_{**}(L)b$, $C_{**}(L):=\mathrm{Des}(L)^3$." This follows from the value bound, $C_f\le\mathrm{Des}(L)$, $D(L)\le\mathrm{Des}(L)$ and $|\Omega_a|\le2L$.
- Then use $C_{**}$ in place of $C_*$ in $\beta(b)$, in $\delta_0(b)$ and in Steps 0-1 of Proposition 2.32.

**R5 ((QC4) does not imply $\beta(b)\le\eta'/3$, which the proof of Proposition 2.32 uses). Line 1356; proof lines 1501-1502, 1533-1534, 1558-1560, 1604.**
- (QC4) gives only $b\le\eta'$, $\beta(b)<1/C_L$ and (D1), $C_L\beta^{2/N_L}\le\eta'/3$.
- The proof uses more:
  - "$|r_1-r(f)|\le C_*b$" together with "$|r''-r_1|<\eta'$ and $|r''-r(f)|\le2\eta'$" (Step 3);
  - "$r_1\in\mathcal K_\kappa$ by Lemma 2.12" with $\rho_0=2\eta'$ (Step 1).
  
  Both need $C_*b\le\eta'$, in the Euclidean norm of $\mathbb R^{\Omega_a}$.
- (D1) yields $\beta\le\eta'/3$ only when $N_L\ge2$. Lemma 2.26 allows $N_L=1$, and with $N_L=1$ (D1) only gives $\beta\le(\eta'/3)^{1/2}$.
- The same gap affects the inward pushes of inactive near-threshold carriers in (U)-blocks (line 1559, "individual inward pushes by $\eta'$") and the conclusion "gap $\ge c\,\eta'M$" (Proposition 2.32(b); line 1604). A carrier with $\varrho(f_1)\le1+(1+C_*)b$ pushed by $\eta'$ in relative position keeps a positive gap only if $(1+C_*)b<\eta'$.
- Fix:
  1. Add to (QC4) the clause "$\beta(b)\le\eta'(w)/3$" (with $\beta$ built from $C_{**}$ as in R4). Alternatively, require $N_L\ge2$ in Lemma 2.26, which is always possible because $\mathrm{dist}$ is bounded on the compact set.
  2. State that $|\cdot|$ on $\mathbb R^{\Omega_a}$ is the Euclidean norm, in Lemmas 2.12, 2.24 and 2.26 and in Proposition 2.32.
  3. In Step 4 and in (b), say that the inactive near-threshold carriers of (U)- and (KN)-blocks are pushed inward **to relative position $\le1-\eta'$**, not "by $\eta'$". The gap $\ge\eta'M$ then follows, and the cost is unchanged.
- The statement of Proposition 2.32 is unaffected.

**R6 (two incorrect intermediate inequalities in the proof of Proposition 2.32). Lines 1554-1555 and 1611.**
- Quotes: "where $x$ is the vector of corrections (so $\eta_*\le C\eta'$)" and "All moves have size $\le C\mathrm{Des}\,\eta_*\le C\mathrm{Des}\,\eta'$".
- Problem: the corrections include the (U)-block rescaling $(1-s_m)r''_l\varkappa^*_m=4\mathrm{Des}\,\eta'\,r''_l\varkappa^*_m$, and generally $|r''-r_1|\varkappa^*_m\le\eta'\varkappa^*_m$ with $\varkappa^*_m\le C_f$. So only $\eta_*\le C_f\mathrm{Des}(L)\eta'$ holds, for $L\ge l_f$.
- Fix:
  - Line 1555: replace "$\eta_*\le C\eta'$" by "$\eta_*\le C_f\mathrm{Des}\,\eta'$".
  - Line 1611: replace "$\le C\mathrm{Des}\,\eta_*\le C\mathrm{Des}\,\eta'$" by "$\le2^{G(L)}\eta_*\le C_f\mathrm{Des}^{2}\eta'$".
  - With $C_T\le C_f\mathrm{Des}$ ([II, Lemma 4.15]) and $|L_0|\le2L$, the cost bound (c), $C_f\mathrm{Des}^3\eta'\log(1/\eta')$, still holds. Write this computation out; the stated conclusion stands.

**R7 (hypothesis mismatch: Lemma 2.14(b) versus Proposition 2.32(a)). Lines 908-909 and 1473-1474.**
- Lemma 2.14(b) is stated for "every $r\in\mathcal K_\kappa$ with $|r-r(f)|\le2\eta'$". Proposition 2.32(a) only guarantees "$|r''-r(f)|\le5L\mathrm{Des}(L)\eta'$" for the realized ratios, because of the (U)-block rescaling.
- Section 4 applies Lemma 2.14(b) at the realized ratios (lines 3943-3945).
- The proof of Lemma 2.14(b) only uses the Lipschitz bound of $\varrho^0_l$, which depends on block $m$'s ratios alone.
- Fix:
  1. In Lemma 2.14(b) replace the hypothesis by "$|r^{(m)}-r(f)^{(m)}|\le2\eta'$" (the coordinates of block $m$).
  2. Add to Proposition 2.32(a): "in blocks of kind (T) and (KN), $|r''^{(m)}-r(f)^{(m)}|\le2\eta'$". This holds by Step 3, after R5.

**R8 (a weak-peak lever in a (KN)-block is not covered by "the proof of [II, Prop 5.56] applies verbatim"). Lines 724-725, 1555-1558 and 1596-1598.**
- Background: Definition 2.8(b) declares a block of kind (KN) if "some inactive carrier of $\Omega_m$ has $\varrho(f)\ge u$". Since $\Omega_m$ contains all weak peaks (Definition 2.8(a)), the lever $d_0$ may be an **inactive weak peak**, with $\varrho_{d_0}(f)\in[1,1+b]$. This agrees with X1 2.1(KN).
- Problem: Proposition 2.32 starts from $f_1$, which has only the closing moves; there $d_0$ is still a peak. The step "the inward lever push of the proof of [II, Prop 5.56] (Step 2), of size $s_0$" then acts on a peak, and an inward push of a peak **lowers** $\bar\vartheta$ ([II, Lemma 2.10(b)(i)]) until $d_0$ crosses the threshold.
- Its margin in $\hat\zeta$-units, $(\varrho_{d_0}-1)\bar\vartheta\Phi_{d_0}^2\le b\bar\vartheta\Phi_{d_0}^2$, need not be small compared with $s_0=C'\mathrm{Des}\,\eta'\bar\vartheta\Phi_{P}^2/(\varrho_{d_0}M)$ when $\Phi_P^2\ll\Phi_{d_0}^2$.
- [II, Proposition 5.56] is stated for $\Omega$-carriers that are strict non-peaks of the reference companion, and its proof does not treat this case.
- Fix: add to Step 4: "if the lever $d_0$ of a (KN)-block is a weak peak of $f$, it is first pushed inward to $\varrho=1-b$, as in X1 2.1(KN): the value change is $\le2b\bar\vartheta\Phi_{d_0}/m$ and the cost is $O(b)$. Thereafter it is a strict non-peak with $\varrho\ge u$, and the lever push of [II, Proposition 5.56] applies." Also check that $\bar\vartheta$ and $\varkappa$ are continuous across the crossing ([II, Lemma 2.7(a), Lemma 2.10(a)]).
- Alternative fix: prove that $s_0\ge4(1+C/(\varrho_{d_0}M))\,b\bar\vartheta\Phi_{d_0}^2$. This holds for $L\ge l_f$ if $\mathrm{Des}\ge D^2$, because $\Phi_P^2\ge D^{-2}$ and $b\le\eta'$. Then note that the net change of $\bar\vartheta$ over the whole push is still a raise of order $\varrho_{d_0}Ms_0/\Phi_P^2$.
- Either way, the present one-line citation does not cover this case.

## A.2 Optional suggestions (Section 2)

- **O1 (Lemma 2.10, proof, lines 818-821).** For an inactive shift ((U)-block) the displayed formula needs $\sum_{l\in\Omega_a(m)}r_l\gamma_l=0$; this is (X3) with $\Delta'_m=0$. Say so: "for an inactive shift the term $\Delta'_m\tau_m$ vanishes, and (X3) gives $\sum r_l\gamma_l=0$, so $\sum_l\gamma_lr_l\tau_m=0$".
- **O2 (Remark 2.2, lines 505-507).** "raises $\bar\vartheta$ at first order without moving $\varkappa$": [II, Proposition 5.46(iii)] gives the rate $\varrho_{d_0}MX/C$ for $\varkappa$, which is second order but not zero. Write "moving $\varkappa$ only at the rate $\varrho_{d_0}MX/C$".
- **O3 (Remark 2.15, line 983).** "the shift trick of [II, Subsection 2.4]": Subsection 2.4 defines the kinds [1]-[3]. The shift trick itself is in the proof of [II, Proposition 4.24(iii)]. Cite both.
- **O4 (Remark 2.25, lines 1291-1292).** "$\mu_\kappa(h)$ may be much smaller than any fixed power of $h$" literally contradicts Lemma 2.24(c). Say "may be much smaller than $h^p$ for any exponent $p$ fixed in advance (e.g. $p=4$)".
- **O5 (Remark 2.7(a), lines 688-693).** $I_m(f')$ is defined under $\Omega\subseteq Q(f')$. At $f'=f$ the set $\Omega_m$ contains the weak peaks, so the formula must use $\sigma'$ of Lemma 2.4, as the proof of Lemma 2.9 does. Say so.
- **O6 (Lemma 2.4(b), line 569).** "$a^2=\sigma'+\mathsf k^2R^2$" needs $\varkappa\ne0$ for $R$ to be defined. State the condition, or write $\sum_{\Omega}\varrho_k^2\Phi(k)^2$ in place of $\mathsf k^2R^2$.
- **O7 (Lemma 2.17(a), lines 1040-1041).** "the weights of the robust peaks of the active blocks": $\mathcal K_\kappa$ also uses $\sigma_{\rm rob}(m)$ for (U)-blocks with $\Omega_a(m)\ne\emptyset$. Write "of the blocks with an active component". This is harmless, since robust peaks are outside $\mathcal N_T$.
- **O8 (Proposition 2.32).** The symbol $r''$ denotes both the Puiseux point (Step 3) and the realized ratio vector after the (U)-rescaling (line 1582, "we call this vector $r''$ again"), and (a) refers to the latter. Use a separate symbol, e.g. $r^{(1a)}$.
- **O9 (Remark 2.28(i), line 1370).** "$\Lambda_\kappa$ and the other Lipschitz constants are $\le CL\,D(L)^9$": this is true for $\Lambda_\kappa$ and for the status functions of $\mathrm{Lip}^*_\kappa$. For the Lipschitz constants of the rate objects (minors of matrices of size up to $2L$) only finiteness is clear. Say so.
- **O10 (Lemma 2.6).** The hypothesis $\varkappa(\zeta;\Omega)\ne0$ is automatic for $\Omega\subseteq Q$, since $\varkappa=\bar\vartheta(a+\sigma)>0$.
- **O11 (Definition 2.8(b)).** Add the sentence "an inactive weak peak makes the block of kind (KN) (see R8)". This makes visible why every weak peak of a (T)-block is active, which the proof of Lemma 2.9 uses ("the inactive carriers of $\Omega_m$ are nearly neutral").
- **O12 (Proposition 2.32(b), (KN)).** $\eta'(w)$ coincides with $\eta(w)$ of Part II ([II, before Theorem 5.7]: $\eta(w)=T_{\rm lo}^4/(l\,\mathrm{Des})$), so "with $\eta'$ in place of $\eta(w)$" is an identity. Say so.

## A.3 Incorporation of the referee and certification fixes (Section 2): checked item by item

**Present and correct:**
- K1, formula-1 $\varkappa$ with the pattern's $\Omega$: Definition 2.8(a), Lemma 2.4(b), Remark 2.5, Lemma 2.17(b).
- W-fix, region defined by robust peak weights only: Definition 2.11, Remark 2.21.
- KN-1 / P-HOLD, exact holds: Proposition 2.32 Step 4 and (b), Remark 2.33.
- cert0 F1, common pull window: Lemma 2.29, Remark 2.30, Step 4.
- P-LIP and P-LIP+, $\mathrm{Lip}^*_\kappa$ including $\Lambda_\kappa$ and the actual statuses: Definition 2.27.
- P-SFAR, $s$-free $\alpha_l$: Definition 2.13, Lemma 2.17(c), Remark 2.18.
- P-CY: Lemma 2.24(b), Remark 2.25, (D2).
- P-CHOICE: Remark 2.25.
- Q2 ($\eta'/3\le1/\mathrm{Des}\le h_\kappa$): Remark 2.28(iii).
- Q3 (Łojasiewicz on $\mathcal K_\kappa$): Lemma 2.26.
- cert0 C1 ($F\le1-\tfrac34\mu$): Lemma 2.24(a).
- C2: Remark 2.25.
- C3 (Step-0 weak-peak push dropped; bound through Lemma 2.9): Step 0.
- C4 (cost with $\mathrm{Des}^3$): Proposition 2.32(c), see R6.
- C5 (robust $\ge u/4$): Proposition 2.32(a).
- C6 ($\gap(f)\le\frac32\gap^\#$, not "$Mb\le\gap^\#/4$"): Remark 2.15.
- D1 (degree $e\le n$, factor $s^n$): Lemma 2.16, see R2.
- D2 (inactive near-threshold carriers of (U)-blocks pushed): Proposition 2.32(b), see R5.
- S-0 ($c_{L+1}\le b^2$ replaces (D3)): (QC5), Lemma 2.34.
- Puiseux reference (van den Dries, Ch. 7): Lemma 2.24(c).
- GEN in the norm form: Lemma 2.22.
- Option (b) exception stated as open, with no claim about the slice version: Remark 2.35(iii).
- U1-ref Lemma R-kt as Lemma 2.1; (X4) of U1-ref (F4) kept in (KN)-blocks: Definition 2.13.

**Re-derived independently in this pass:**
- Lemma 2.1(b); Lemma 2.3; Lemma 2.4(a)-(e), including the explicit bounds of (e): $K\le10/s_0$, $\partial_sK\le16/s_0^2$, $\partial_xK\le1000/s_0^4$.
- Lemma 2.6; Lemma 2.9 (constants $C\sigma^{-5}$, $C\sigma^{-6}$); Lemma 2.12; Lemma 2.14(a),(c); Lemma 2.17(c) arithmetic.
- Lemmas 2.20, 2.22, 2.24 and 2.26; Lemma 2.31; Lemma 2.34.

**Part II citations checked:** [II, Lemma 2.6], [II, Corollary 2.11], [II, Proposition 5.46], [II, Remark 5.47], [II, Definitions 5.52, 5.55], [II, Proposition 5.56], [II, Lemma 4.15], [II, Corollary 3.20]. They say what is attributed to them, except as noted in R4 and O3.

---

# Part B: Section 3 (the violation-tolerant $d$-consistent engineered approximant)

**Numbering:**
- 3.1 `def:III-pieces`; 3.2 `lem:III-masses`; 3.3 `def:III-dcons`; 3.4 `lem:III-dcons`; 3.6 `lem:III-ball`; 3.7 `prop:III-J`;
- 3.9 `def:III-levers`; 3.10 `lem:III-DC`; 3.12 `def:III-window`; 3.13 `def:III-approx`; 3.14 `lem:III-UE1`;
- 3.15 `thm:III-UE`; 3.17 `thm:III-Eeng`; 3.19 `def:III-designadd`; 3.20 `lem:III-designadd`; 3.21 `prop:III-S2c`;
- 3.23 `lem:III-noB`; 3.24 `lem:III-CMp`; 3.25 `lem:III-LV`; 3.26 `thm:III-Cmix`; 3.27 `cor:III-noB`.

**Verdict.**
- The analytic core is correct and every certification fix is in place: d-consistency, Sherman–Morrison/Poincaré–Miranda, the violation-tolerant per-piece bound with $c_{\rm flat}$ an $f$-constant, the averaging at the norm-attaining approximant, (R-abs) and Lemma K1.S. The item-by-item check is in B.3.
- The required fixes concern:
  - a wrong cross-reference repeated eight times;
  - one missing hypothesis in the abstract Lemma 3.10;
  - a circular definition in Definition 3.13(iii) (cert2 C2-7 not incorporated);
  - an inconsistency between the lever range claimed in (U6)/Lemma 3.25(a) and the pull coordinates actually available;
  - the definition of $c_{\rm tiny}$ versus the bound of Lemma 3.25(c);
  - a false justification in the proof of Lemma 3.20;
  - two small incorrect estimates (Lemma 3.24(b); the remark after Definition 3.12).
- None of these changes a conclusion of Section 3.

## B.1 Required fixes

**R9 (wrong cross-reference, eight occurrences). Lines 2905, 2923, 2935, 2968, 2973, 3066, 3070, 3101: "[II, Theorem 5.67]".**
- In Part II, 5.67 is `lem:II-mixed` ("The recursion in a mixed class"); Master Theorem IV′ is `thm:II-MTIV` = Theorem 5.68 (labII.txt). The Introduction (line 132) and lines 334, 3207, 3787, 4342 correctly cite 5.68.
- Fix: replace "[II, Theorem 5.67]" by "[II, Theorem 5.68]" at all eight places. Where the intended object is the data construction inside its proof, say "the proof of [II, Theorem 5.68]".

**R10 (Lemma 3.10 lacks a hypothesis on $\Delta_1$). Lines 2055-2059 and proof step (5), lines 2133-2140.**
- Step (5) says that along the cube "$C_m$, $\bar\vartheta_m$ move by $O((r+\delta_1+\Delta_1)/A_{\min})$" and concludes "no status changes along the cube". Step (2) relies on this.
- But the hypotheses of (ii) bound only $\delta_1$ (which, since the C2-3 fix, is a max over $\Omega$ only), $|F(0)|$ and $r$. $\Delta_1$ (the $\lambda$-weighted change of all values in the pre-row) is not controlled. A small $|F(0)|$ does not bound $\Delta_1$, because of cancellations in $A_m(0)-A_m(f_0)$. So the abstract lemma, as stated, does not imply that statuses are preserved.
- In the application Lemma 3.14 gives $\Delta_1\le\Pi_X+T^4s_1\le r$, so nothing downstream breaks.
- Fix: add "$\Delta_1\le r$" to the hypotheses of (ii), next to "$\delta_1\le r\le r_0$". Alternatively, replace the hypothesis "$K_J|F(0)|_\infty\le r/2$" by "$K_J$ times the right side of (i) is $\le r/2$", which implies $\Delta_1\le A_{\min}r/(2K_J)$. Then use this in step (5).

**R11 (circular definition of the radius $r$; cert2 C2-7 not incorporated). Definition 3.13(iii), lines 2238-2242.**
- Quote: "$r:=16K_J(1+1/A_{\min})(\Pi_X+2T^4s_1)+32K_JW_{\rm pull}/A_{\min}$, and pull coordinates with $v_l(j_p)\in[r,2^Gr]$". Here $W_{\rm pull}$ (Subsection 3.3) is the weight of the carriers meeting the pull coordinates $j_p$, which are chosen in terms of $r$.
- Fix (as in cert2 C2-7):
  1. Define $W_{\rm pull}$ by a monotone a priori bound, independent of the actual pulls. Take $\overline W_{\rm pull}$ := total weight of the carriers $k\ne l$ that meet some $j\in S_l$ with $v_l(j)\ge r_{\min}:=32K_JT^4s_1$, $l\in\Omega$. In the application this is $\le C_f\mathrm{Des}^Cc_{L+1}$, by allowedness (c): such carriers sit at stages beyond $s_{\max}$.
  2. Define $r$ with $\overline W_{\rm pull}$.
  3. Note that the pulls chosen afterwards have $v_l(j_p)\ge r\ge r_{\min}$, so their actual $W_{\rm pull}$ is $\le\overline W_{\rm pull}$.
- The same symbol is used in (FINE), Lemma 3.14 and Proposition 3.21; replace it there as well.

**R12 (the pull range claimed in (U6) and Lemma 3.25(a) is not available). Lines 2200-2201, 3006-3011 and 3036-3042.**
- (U6) requires "for every $r\in(0,r_0]$ every TU lever has a pull coordinate with $v_l(j_p)\in[r,2^Gr]$". Lemma 3.25(a) claims "pull coordinates in $S_l\cap(j(l),s_{\rm far}(w)]$, all contacts of $f^\#$ with $z^\#=\epsilon_l$ … and for every $r\le r_0$ there is a pull coordinate with $v_l(j_p)\in[r,2^{G(L)}r]$".
- Two problems:
  1. Inside $(j(l),s_{\rm far}(w)]$ the values satisfy $v_l\ge v_l(s_{\rm far}(w))\approx\delta_l2^{-s_{\rm far}}/n_l$. So for $r<2^{-G(L)}v_l(s_{\rm far}(w))$ (i.e. $r\lesssim c_{L+1}^2$) no such coordinate exists. Without step (2) (Corollary 3.27) the far part beyond $s_{\rm far}$ is not owned by $l$, so it cannot serve as a pull coordinate.
  2. Statement (a) says "pull coordinates in $S_l\cap(j(l),s_{\rm far}(w)]$, all contacts of $f^\#$ with $z^\#=\epsilon_l$", whereas the proof (lines 3036-3038) correctly says "$S_l\cap(s_{\max}(L),s_{\rm far}(w)]\setminus F^\#$". The realization, hold and lever pulls of (1a) ([II, Lemma 4.15], Proposition 2.32, [II, Proposition 5.56]) sit in $S_l\cap(j(l),s_{\rm far}(w)]$ and carry pull masses of sign $-\epsilon_l$. They are support coordinates of $f^\#$, not contacts with $z^\#=\epsilon_l$ (cert0 P4: per $S_l$ at most a bounded number of elements are used). Removing them also affects the bounded-gap claim "$v_l(j_p)\in[r,2^{G(L)}r]$".
- Fix:
  - In (U6) and Lemma 3.25(a), replace "for every $r\in(0,r_0]$" by "for every $r\in[r_{\min}(w),r_0]$, $r_{\min}(w):=2^{2G(L)}\max_{l}v_l(s_{\rm far}(w))\le C\,c_{L+1}^2$".
  - Write the pull range as $S_l\cap(j(l),s_{\rm far}(w)]\setminus F^\#$ in the statement, as in the proof. Enlarge the window ratio to $2^{CG(L)}$ (cert0 P4 uses $2^{6G}$) so that an element outside $F^\#$ exists in every window, and use this $G$ in (U6), in Definition 3.13(iii) and in $\Lambda_{\rm lev}$.
  - In Theorem 3.26 and Proposition 3.21 record that $r\ge16K_JT^4s_1\ge r_{\min}(w)$, since $s_1=e^{-1/(2T)}\gg c_{L+1}^2$.

**R13 ($c_{\rm tiny}$: definition versus the bound of Lemma 3.25(c)). Lines 2030-2031 and 3020-3021, 3045-3047.**
- $c_{\rm tiny}$ is defined as $\max_{l\in\Omega}\sum_{k\notin\Omega}\lambda_k\sum_{s\in\mathrm{Lev}_l}|u_k(s)|/v_l(s)$, the sum running over **all** lever coordinates, TU pull coordinates included.
- At a pull coordinate $v_l(j_p)\approx r$, so its term is $\approx|u_k(j_p)|/r$. The proof of Lemma 3.25(c) only uses "$1/v_l(j(l))\le\mathrm{Des}(L)$", which concerns the bank/Z coordinate $j(l)$. So the bound "$c_{\rm tiny}\le C_f\mathrm{Des}(L)^Cc_{L+1}$" is not proved for the quantity as defined.
- In Lemma 3.10 only the $P$-dependent coordinates matter: in (i) and (2) the term describes the bank at $j'$ and the (Z) moves. The TU pull is a fixed move, accounted for by $W_{\rm pull}$.
- Fix: define $c_{\rm tiny}$ with $s$ ranging over the (Z) coordinates and the TU **bank** coordinates only. Equivalently, keep the definition, replace the bound of Lemma 3.25(c) by $c_{\rm tiny}\le C_f\mathrm{Des}^Cc_{L+1}/r$, and check (W-b) via $c_{L+1}/r\le e^{-1/(2T)}T^{-4}$.

**R14 (Lemma 3.20: the justification is false as stated). Lines 2777-2781.**
- Quotes: "the absorber lengths are computed from $c^{\rm low}$, so the absorber targets are unchanged" and "The results of Part II use weights only through upper bounds and $\mathrm{Des}$ only through lower bounds, and use windows only through the properties of [II, Lemma 3.22]".
- Problems:
  - Part II's absorber construction ([II, Definition 5.48, Lemma 5.51]) uses weights through **lower** bounds: $R$ is computed from $c^{\rm low}_p$, together with the least entry and the cluster capacity (cert3 item 2a: "'weights enter only through upper bounds' is false as stated").
  - (W$_{\exp}$) lowers $c^{\rm low}_{L+1}$ itself, so the cluster after $L$ gets new $R$'s. The targets are not "unchanged"; they are produced by the same rule.
  - The class/cube pigeonhole is not covered by [II, Lemma 3.22] (cert3 items 2d, 5). Part II handles it through $Q(w)\ge\bar D(w)^3$ in [II, Definition 5.48].
- Fix: replace the two sentences by: "Lower-bound uses of weights in Part II (absorber length $R$, least absorber entry, cluster capacity) are computed from $c^{\rm low}$ after (W$_{\exp}$) is imposed, so they hold for the modified weights. Enlarging $\mathrm{Des}$ enlarges $\bar D(w)$, and $Q(w)\ge\bar D(w)^3$ is imposed after $\mathrm{Des}(L)$ is fixed. Every other window condition is monotone ([II, Lemma 3.22])."

**R15 (incorrect estimate in the proof of Lemma 3.24(b)). Lines 2969-2972.**
- Quote: "this changes $g_t$ by at most $\|\mathcal V_{\rm fine}\|_1+\sum_a|\gamma_a|\le C_f\mathrm{Des}\,c_{L+1}\le Kt$, and $\Gamma_w$ by $O(c_{L+1}^2)$".
- Two corrections:
  1. By (c) of the same lemma, $\|\mathcal V_{\rm fine}\|_1\le C_f\mathrm{Des}\,c_{L+1}+C_fc_{L+1}^2/t$; the second term is missing (it is still $\le Kt$).
  2. A perturbation $y$ of the data with $h(y)$, $H(y)=O(c^2)$ changes $\Gamma_w$ through the cross term $2\langle\cdot,\cdot\rangle$ by $O(c_{L+1})$, not $O(c_{L+1}^2)$.
- Fix: write "$\sqrt{\Gamma_w}$ (a seminorm) changes by $O(c_{L+1})$", and absorb this in the slack of [II, Theorem 5.68]'s proof, which bounds $\sqrt{\Gamma^\#_w}$ by $\sqrt{\Gamma_w(B_-,\Theta_-)}+Kt+C_fp\varepsilon$ (cert0 CM′(b)).

**R16 (false containment claim). Lines 2222-2223.**
- Quote: "Kind [1$'$] contains kind [1] of [II, Theorem 2.20] ($\gap\ge t^2$ is not required)".
- Problem: kind [1] of [II, Subsection 2.4], which is what [II, Theorem 2.20] uses, is $|\omega(k)|\le3\gap(k)/t$. Kind [1′] requires $|\omega(k)|\le2\gap^0(k)/t$. So [1′] does not contain it. The constant 2 is used: kind [1′] needs $4\rho c_{\rm flat}\gap^0\le\gap'/2$ in Step 3 of Theorem 3.15.
- Fix: "Kind [1′] contains kind [1] of [I, Lemma 8.42] (constant 2, without the condition $\gap\ge t^2$)". Alternatively, define [1′] with the constant 3 and strengthen (c4) to $\rho c_{\rm flat}\le1/24$.

## B.2 Optional suggestions (Section 3)

- **O13 (Proposition 3.7(c), proof, line 1963).** Lemma 3.2(iii) gives $|\delta u_k|\le\Pi_e+2t_k$, because $|z'-z_0|\le2$, not $\Pi_e+t_k$. The constant is absorbed in $C$; correct the line.
- **O14 (Remark 3.8, line 1969).** "$\Pi_e=O(s_1(n\nu/q_0)^{1/2})$": Lemma 3.2(iv) gives $\|X\|=O(s_1(n\nu/q_0)^{1/2})$ and hence $\Pi_e\le2\|X\|/\nu=O(s_1(n/(\nu q_0))^{1/2})$. This is heuristic context only.
- **O15 (Lemma 3.14, proof, lines 2318-2319).** The two linear terms of (i) contribute $K_J(1+1/A_{\min})(\Pi_X+T^4s_1)+2K_JW_{\rm pull}/A_{\min}\le r/16+r/16$. So the chain should read $r/8+r/8+r/16\le r/2$, not $r/16+r/8+r/16$. The conclusion is unchanged.
- **O16 (Theorem 3.15, Step 0, order of choices).** The pre-row $f_1=f[A_1,z_01_{[1,N'']}]$ depends on $N''$, which is chosen after $r$. Write the order as "$s_1\to$ masses of the pre-row and $\Pi_X\to r\to$ pulls $\to N''$ (cut-off of the pre-row) $\to P^*$".
- **O17 (Lemma 3.14(e) and Lemma 3.23).** Carriers meeting lever or pull coordinates also contribute up to $4\sum\lambda_k$ to $\|D_m(w'_m-w^0_m)\|_2^2$, not only to the sum over $A_m$. The displayed bounds should carry $8(W_{\rm lev}+W_{\rm pull})$, or $4$ in each part. This is harmless under (FINE).
- **O18 (Lemma 3.23).** By the definition after (U7), "every peak of $f_0$ that is not fine has margin $\ge x_0$" is a tautology: low-margin coarse-stage peaks count as fine. The real requirement is the smallness of $c_{\rm fine}$, which then includes such peaks. Likewise, the $\Omega$ clause is redundant for $d$-consistent carriers (X2-ref p-UE2). Say so, and point to Corollary 3.27's proof, where the margin clause is verified so that $c_{\rm fine}$ consists of stages $>L$ only.
- **O19 (Lemma 3.10, proof step (2)).** "$|E_l(P)-(YP)_l|\le C'_2|P|^2$": the bank slope is $\nu_1/\nu_A=1-O(r^2)$, so the remainder is $O((r+|P|)|P|)$. This is what step (3) actually uses ($C_2(|P|+\delta_1+r)|P|$); align the two statements.
- **O20 (Lemma 3.24).** "$\Delta\omega(t)$ … $0$ on the inactive $\Omega$-carriers": in the data convention of [II, Subsection 5.6] the inactive components are the $\gamma_l$ ((X5)), i.e. $\Delta\omega(l)=\Delta''_mw^\#_m(k(l))$. Say which is meant.
- **O21 (Theorem 3.26).** Recall explicitly that the pigeonhole bound $|\mathcal S|\ge n(w)/\bar D(w)^2$ rests on $Q(w)\ge\bar D(w)^3$ of [II, Definition 5.48] (cert3 item 5, Part II mechanism), not on [II, Lemma 3.22].
- **O22 (Section 2, Remark 2.18).** "Hoffman and Łojasiewicz constants within a factor 2": row scalings by $t_l\in[\frac12,1]$ change the Hoffman constant by at most a factor 2. The Łojasiewicz inequality $\mathrm{dist}^{N}\le C\,\Pi_S$ changes its constant $C$ by up to a factor 4, since $\Pi_S$ is quadratic in the rate objects, so the displacement bound changes by up to $4^{1/N_L}$. Say "within a fixed factor".

## B.3 Incorporation of the referee and certification fixes (Section 3): checked item by item

**Present and correct:**
- X2-ref p-J: cut-off term $\max_\Omega t_k$ (Proposition 3.7). Referee addition F3: Remark 3.5, Lemma 3.4(c).
- p-DC1 (radius with $(1+1/A_{\min})$ and $W_{\rm pull}$): Definition 3.13(iii), but see R11. p-DC2 (pulls are fixed moves; $W_{\rm pull}$): Lemma 3.10(i), Remark 3.11(a). p-DC3: Lemma 3.10(ii).
- p-LV1 ($n_l$ in (D-lev)): Definition 3.19. p-LV2 (pulls in $E_c$): Lemma 3.25(a), but see R12. LV(d) false, hence (R-abs): Definition 3.9 last sentence, Remark 3.28, Lemma 3.24.
- p-UE1/p-UE2 ($W_{\rm pull}$ terms; $\Omega\subseteq S_2$): Lemma 3.14(b),(e). p-UE3 is superseded by C2-9: Lemma 3.14(g). p-UE4 = p-DC1. p-UE5 ($s_{\rm late}$ with exponent 7): Theorem 3.15. p-UE6 ((W-a) with $(1+C_2K_J)$; $W_{\rm pull}$ condition, i.e. (FINE)): Theorem 3.15. p-UE7 (residues as violations): (U6).
- (c3′): (c3) of Theorem 3.15 is stronger. p-E1: (E-f) of Theorem 3.17 and the tail condition in Definition 3.13(i). p-W ((W$_{\exp}$) at main stages only): Definition 3.19, but see R14.
- cert2 C2-1/C2-2 (margin of $k^\natural$; $|M''-M|\le\gamma_0/4$): Lemma 3.6(a). C2-3 ($\delta_1$ over $\Omega$, plus $\Delta_1$): Lemma 3.10, but see R10. C2-4: Lemma 3.10(i), (W-b). C2-5 (correct gap criterion): Lemma 3.4(a), Lemma 3.10(iii), Remark 3.11(b), Lemma 3.14(c).
- C2-6 (value units for $r_0$): Lemma 3.10 step (5), Lemma 3.25 proof. C2-7: **not incorporated** (R11). C2-8: (c4). C2-9 (Bregman identity for $c_i$): Lemma 3.14(g). C2-10 ($\|g_i1_{(N'',\infty)}\|_1$): Definition 3.13(iv). C2-11 ($W_{\rm lev}$ in $\mathfrak S_m$; $K_*$ an $f$-constant): Lemma 3.14(e). C2-12 ($1/u$ via $1/r_0\in\Lambda_{\rm lev}$): Lemma 3.14.
- cert2 P6 (window-dependent $c_{\rm flat}(j)$): Theorem 3.17, Remark 3.18(c). Subset averaging: Remark 3.18(b).
- refa P1 (kind [1′]): Definition 3.12, but see R16. refa P3 (support residues): (U3), (U4).
- K1.S (Step B dispensable, (U5′), the bound $4c_{\rm fine}$, the role of (W$_{\exp}$)): Lemma 3.23, Corollary 3.27 and the paragraph after Lemma 3.23.
- cert0 CM′(a)-(d) at the companion without absorbers: Lemma 3.24 (stated for the (KN) companion of Part II, which is the setting of X2-ref).

**Re-derived independently in this pass:**
- Lemma 3.2; Lemma 3.4 (gap identity, junction terms, clamp slope bound); Proposition 3.7.
- Lemma 3.10 steps (1)-(4): the Jacobian $I-pq^T$, $q^Tp\le C_m<\tfrac12$, $\|J^{-1}\|\le1+2/A_{\min}$, Poincaré–Miranda arithmetic.
- The decomposition identity of Theorem 3.15 Step 2 for violated pairs, the radius conditions of kinds [1′]/[2]/[3], the base claim, the arithmetic of Steps 4-5 ($1-2\delta+11\delta/16\le1-\delta$).
- Theorem 3.17 (both cases); Proposition 3.21; Corollary 3.27.

