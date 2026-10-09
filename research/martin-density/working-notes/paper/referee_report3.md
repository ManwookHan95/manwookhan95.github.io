# Referee report 3: the subsection "Toward Lemma Z", the abstract and the status section of martin_density_note.tex

Scope: lines 35-84 (abstract), 4631-4693 (Remark rem:lemmaZ, updated), 4695-5813 (Subsection "Toward Lemma Z"), 5815-5932 (status).
Sources: r4/Z1_notes.md (+ Z1_part1-5), Z1_referee.md, Z1_ref_notes.md (+ parts); r4/Z2_notes.md (+ parts), Z2_referee.md, Z2_ref_notes.md
(+ parts); BRIEFING_R2.md ADDENDUM 3. Only refereed results with all their corrections are used as the standard.

Compilation: copied to paper/build3/ and compiled twice with pdflatex. No errors, no undefined references or citations, 77 pages. Three
overfull boxes (2.3pt, 1.6pt, 2.6pt) at lines 2819, 3171 and 4195, all outside the new material.

## 0. Bottom line

The mathematics of the new subsection matches the refereed sources, and every correction the referees requested has been made:
- **Z2 switching budget.** The false gloss is gone. Lemma lem:switchbudget states the corrected consequences: z-signed on K up to t/(2q_0);
  t/(gamma q_0) on J_gamma; only the (1-|z|)-weighted mass off F is O(t). Remark rem:budgetgloss gives the counterexample z_j = 1-1/j.
- **Z2 Lemma 2.5(b).** It is proved through the unified triangular system (lem:modswallow, "Unified triangular system").
- **Theorem S.** The text after Definition def:swallowed says that (H2) (= Z2's (H4)) is automatic and (H3) (= Z2's (H5)) is vacuous under
  (B_res) (= Z2's (S_inf)). The bound |omega^+(k(l))| <= (3+eta)/t has been fixed. The unproved "mixture" remark is not included.
- **Z2 Prop 5.1.** Remark rem:nodesign says "first-order base cost only", and the HEURISTIC supp-a sentence is omitted.
- **(BT) points.** They are excluded from the open cases (Remark rem:Bpm(d), rem:openZ, status).
- **Z1 1.3.** The exposed-face consequence does not appear anywhere (grep for "exposed" finds nothing).
- **Z1 5.2.** The common-functional obstruction does not appear. The referee's Theorem M appears as a labelled sketch (rem:thmM).
- **Theorem B^inf.** It appears as a sketch (rem:Binf), and its unproved step (iv) is named.
- **Lemma Z per mate.** Problems prob:lemmaZ and prob:lemmaZper are per-mate statements: f' is chosen after g and rho.

I re-derived the following and found them correct:
- the phi-calculus, the split lemma, peak pinning, the flip lemma and bounded free switching;
- the sign-mixed pinning and its unrolling constant (1/q_0 + 22);
- the inclusion R_0 subset R_0^±;
- the good and bad inequalities and the unified unrolling;
- Lemma lem:badpeaks, and the Hoffman step of lem:exactswitch (cost function, cone, violation bounds);
- the d-computation d(omega^-) - d(omega^+) = sum q_l tau'_l;
- the side conditions in lem:windowtwopiece(a) and the constants in (d);
- the c_flat conditions of lem:onesidedtransfer;
- the parameter chain of Theorem thm:S, including kappa_w(rho bar D_j) <= rho^2(1+eta_0/2) <= 1.

The required fixes are about statements in the abstract, the status section and Remark rem:openZ. Some of these overstate what is proved,
some omit hypotheses, and some misdescribe an open case. Two are small errors in definitions or justifications ((O2) and (O3)).

## 1. Required fixes

**1. Abstract, lines 74-77: hypotheses of Theorem S are missing.**
> "that first rows whose signature sets are exactly swallowed by contacts are recoverable without approximating them, when the swallowing is
> finitely generated, or resonant and $d$-neutral"

Theorem thm:S needs (W*), (H2) and (H3), and the resonant case also needs (H1) (it is part of (B_res)). In the finitely generated case, (H2)
and (H3) are genuine restrictions: Remark rem:S(c) lists failure of (H3) as open, and (O1)(ii) lists failure of (H2) as open. Z2 referee
correction 4 asks for exactly these hypotheses wherever "settles G3 6.3(d)" is claimed. Suggested wording: "... are recoverable without
approximating them when the swallowing is finitely generated, or resonant and d-neutral, under a room condition on the remaining signature
sets and non-degeneracy conditions on the swallowed peak carriers".

**2. Abstract, lines 78-82: the list of open cases overstates what is proved.**
> "What remains of Lemma~Z is genuinely scale-dependent switching on approximately swallowed signature sets, lower semicontinuity along
> far-lowering approximants when infinitely many carriers are swallowed, maximal contact off block-tame points, and infinite base support
> without room."

There are three problems.
- (a) "infinite base support without room" implies that infinite base support *with* room is settled. It is not:
  - Theorem B^inf is a SKETCH (Z1 referee table #9), and the paper itself says so in rem:Binf;
  - step (iv) there is "not proved in this note";
  - Problem prob:infiniteF "remains open as stated".
- (b) "What remains ... is" claims the list is complete, but it leaves out three open cases that rem:openZ lists:
  - (O1)(ii): weak or near-threshold free carriers, bad degenerate peaks with the swallowing sign (failure of (H3)), and blocks whose
    non-degenerate peaks are all swallowed (failure of (H2));
  - infinitely many exactly swallowed carriers that are not resonant or not d-neutral, apart from maximal contact (Remark rem:S(c));
  - non-window-pinned mates.
- (c) "genuinely scale-dependent switching on approximately swallowed signature sets" is narrower than (O1), which covers near-resources on
  swallowed sets in general (Z1 referee: "(O-a): near-contact tails and weak or near-threshold free carriers on swallowed signature sets").

Suggested wording: "Among the remaining cases of Lemma Z are genuinely scale-dependent switching on swallowed signature sets (near-contact
tails, weak or near-threshold free carriers), infinitely many swallowed carriers that are not resonant and d-neutral (lower semicontinuity
along far-lowering approximants; maximal contact off block-tame points), and infinite base support (with signature room only sketched)."

**3. Status section, lines 5923-5928: the same overstatement.**
> "What remains (Remark~\ref{rem:openZ}) is genuinely scale-dependent switching on swallowed signature sets (near-contact tails, weak or
> near-threshold free carriers), lower semicontinuity along far-lowering approximants at first rows with infinitely many swallowed carriers,
> maximal contact off \textup{(BT)}, and infinite base support without room."

Replace "infinite base support without room" with "infinite base support (with room only sketched, Remark~\ref{rem:Binf}; without room
open)". Also add the infinitely generated non-resonant or non-d-neutral exact swallowing of Remark rem:S(c), or write "includes" instead of "is".

**4. (H1) is missing wherever the resonant case of Theorem S is paraphrased.**
(B_res) is defined as "(H1) holds and every l in B is resonant and d-neutral" (line 5169). Lemma lem:modswallow(b), which gives
sum (tau_l)_- <= K_star t, needs (H1). This matches Z2's (S_inf) = "(H3) and every l resonant and d-neutral". The following paraphrases drop (H1):
- (S8), lines 5847-5852: "the signature sets that are exactly swallowed by contacts are finitely many, or all resonant and $d$-neutral, under
  the room condition (W$^\star$) on the other sets and the peak conditions (H2), (H3)". Add "(and (H1))" after "all resonant and d-neutral".
- Remark rem:S(a), lines 5625-5627: "for exact, finitely generated (or resonant and $d$-neutral) swallowing, under (W$^\star$), (H2), (H3)".
  Add "and, in the resonant case, (H1)".
- Remark rem:lemmaZ(d), lines 4679-4683: "For \emph{exact} swallowing by finitely many carriers (and for resonant, $d$-neutral swallowing) the
  combination ... is carried out ... in Theorem~\ref{thm:S}". Add "under (W*), (H2), (H3) (and (H1) in the resonant case)".
- Subsection intro, lines 4701-4704: "first rows whose signature sets are \emph{exactly} swallowed by finitely many, or by resonant and
  $d$-neutral, contact patterns are recovered". The phrase "swallowed by finitely many ... contact patterns" is also garbled; it is the number
  of swallowed *signature sets* (bad carriers) that is finite. Suggested: "first rows with finitely many exactly swallowed signature sets, or
  infinitely many whose carriers are resonant and d-neutral, are recovered under (W*), (H1)-(H3) as appropriate, without approximating the
  first row".

**5. Remark rem:openZ (O1)(i), lines 5778-5781: the defect of approximate swallowing is misdescribed.**
> "By Remark~\ref{rem:budgetgloss} the switching through such carriers is $z$-signed only up to errors whose $\ell_1$-mass is not $O(t)$, so
> neither the window certificate nor Corollary~\ref{cor:D1} (which needs exact data) applies."

This sentence mixes up the two sub-cases that (O1)(i) itself lists.
- (a) **Near-contact tails** (|z_j| < 1, |z_j| -> 1). The *wrong-signed* part of Delta B is always O(t): if z_j x < 0, then
  phi_{z_j}(x) = (1+|z_j|)|x| >= |x|, so its mass is at most t/q_0 by Lemma lem:switchbudget. What need not be O(t) is the *correctly signed*
  mass carried by near-contacts off K, where the cost is only (1-|z_j|) per unit (Remark rem:budgetgloss). Two-piece data must vanish off F ∪ K
  (Definition def:twopiece), so this mass cannot be placed in side-admissible data. Trimming it forces the switching amplitude to 0 (Z1_ref_notes
  5.5(b): "the actual switching may use O(1) mass there at each scale ... It is not in P2A 1.6's format").
- (b) **Contact signs that change only far out** (|z_j| = 1 on S_l \ F, small r_l > 0). Here the switching is supported in K and is z-signed
  up to an O(t) error (first order). It fails to be *exact*, and Corollary cor:D1 needs exact data (Z2 3.5(c), Z2 referee §4(b): "the
  switching vector is z-signed only up to O(t), and S3 Cor D1 needs exact data").

Suggested replacement: "In case (a) the switching may carry mass that is not O(t) on near-contacts off K (only its (1-|z|)-weighted mass is
O(t), Remark~\ref{rem:budgetgloss}), where two-piece data must vanish. In case (b) it is supported in K and z-signed up to first-order errors.
In both cases the data are not exact, so neither the window certificate nor Corollary~\ref{cor:D1} applies."

**6. Remark rem:S(c), lines 5641-5643: align with fix 5.**
> "and \emph{approximate} swallowing ($\mathfrak r_l>0$ but too small for (W$^\pm$)), where the switching is $z$-signed only up to
> first-order errors and Corollary~\ref{cor:D1} does not apply."

This is correct only for sub-case (b) of fix 5. Add: "or, at near-contacts, is carried by coordinates off K".

**7. Remark rem:openZ (O2), lines 5790-5792: the far-lowered data are not admissible in general, and infinite F is not handled.**
> "let $f^L$ be the first row with data $(a,z^L)$, $z^L:=0$ on $\bigcup_{l>L}S_l$ and $z^L:=z$ elsewhere (Remark~\ref{rem:lemmaZ}(c))."

Remark rem:lemmaZ(c) requires z' = sgn a' on supp a'. If some S_l with l > L meets F, then z^L = 0 at a point of supp a, so (a, z^L) is not
admissible forced data.
- F finite: only finitely many S_l meet F, so the fix is to define z^L := 0 on ⋃_{l>L} S_l \ F, or to take L large.
- F infinite: by Z1 referee correction 2 ("Truncate a in the far lowerings when F is infinite") and Z1_ref_notes line 41 ("otherwise F' = F is
  infinite and f' is not in R_0"), a must also be truncated. Otherwise f^L has infinite base support and none of the proved classes applies to it.

The second question of (O2), "are all finitely swallowed first rows in Rec?", refers to Theorem S and rem:thmM, which need F finite. Either
state (O2) for F finite, or add the truncation of a. Per Z1 referee correction 4, the reduction must then cover every f, including infinite F.

**8. Remark rem:openZ (O3), lines 5802-5805: the stated reason why Theorem S fails is not the operative one.**
> "Every signature set is swallowed, and infinitely many bad carriers are not resonant (each target recurs infinitely often), so
> Theorem~\ref{thm:S} does not apply."

When z ≡ ε off F, the carrier l is resonant iff ε y_l >= 0 off F (Z2 4.2). So "infinitely many are not resonant" depends on the signs of the
recurring targets relative to ε. It fails, for example, for ε = +1 if every target is nonnegative off F. The robust reason is the following.
Every carrier is bad (S_l \ F ≠ ∅ for all l), so every non-degenerate peak carrier lies in B and (H2) fails. Moreover, B is infinite and contains
the peak carriers, which are not d-neutral, so both (B_fin) and (B_res) fail. Suggested replacement: "Every signature set is swallowed, so
every peak carrier is bad: (H2) fails, and since B is infinite and contains non-d-neutral (peak) carriers, both (B_fin) and (B_res) fail;
Theorem~\ref{thm:S} does not apply."

**9. Problem prob:lemmaZper, line 5743: the title suggests that Problem prob:lemmaZ is not per mate.**
> "\begin{problem}[Lemma Z, per mate]\label{prob:lemmaZper}"

Problem prob:lemmaZ (lines 4623-4629) is already a per-mate statement, because f' is chosen after g and rho. The new problem differs only in
its target class: G = R_0^± ∪ R_S ∪ R_BT instead of R_0. The title therefore suggests a difference that does not exist, and it hides the
difference that does. Z1 referee correction 2 asks that the paper (i) state Lemma Z per mate, and (ii) note that the uniform version is a
stronger, merely sufficient condition. The uniform version asks for one sequence f'_n with rho C(f) ⊂ Li_n C(f'_n). Fix:
- rename the problem to "Lemma Z with the enlarged target class";
- add to Problem prob:lemmaZ (or to rem:lemmaZ) the sentence: "Lemma Z is a statement per mate: f' may depend on g and rho. The uniform
  version (one sequence f'_n -> f with rho C(f) ⊂ Li_n C(f'_n)) is stronger and only sufficient."

**10. Remark rem:thmM, lines 5692-5693: one constraint bound is mis-cited.**
> "by $O(Kt)$ (Lemma~\ref{lem:switchbudget}, and \eqref{eq:didentity} together with Lemma~\ref{lem:budget}(a))"

The cone's d-constraints are sum_{l in U, m(l)=m} x_l u_l(xi) = 0. Their violation is controlled by the first-order identity
sum_k Delta theta_{k,m} u_{k,m}(xi) = (R_m^* Delta Theta_m)(xi), which is proportional to <Delta Theta_m, zeta_m>. That pairing lies in [-t, t]
by Lemma lem:budget(a), and the pinned carriers contribute O(Kt) (Z1 referee §2.2, third fact; correction 5).

The identity eq:didentity concerns Delta d_m, which is a different quantity, and it is not needed here. Replace the citation with "Lemma
lem:budget(a) applied to the first-order identity for (R_m^* Delta Theta_m)(xi)". Optionally add that for strict non-peaks (by (E1)),
u_l(xi) is a positive multiple of epsilon_l q_l, so this cone uses the same d-neutrality as Lemma lem:exactswitch.

**11. Remark rem:lemmaZ(e), line 4690, is inconsistent with Remark rem:Binf.**
> "adapting Lemma~\ref{lem:uniformtransfer} to $|b_j|\le2|a_j|/t$"

After truncation and rebalancing, the base part satisfies |b_t(j)| <= 3|a_j|/t: see rem:Binf (i)-(ii), and Z1 4.2 (C-a'), "|b_j| <= 3|a_j|/t".
The bound 2|a_j|/t holds only for the clamp before balancing. Change the bound to 3|a_j|/t. Since (e) now duplicates rem:Binf, it would be
better to shorten (e) to one sentence that points to rem:Binf.

**12. Remark rem:openZ, lines 5767-5768: imprecise description of "f not in G".**
> "If $F$ is finite, $f\notin\mathcal G$ means that \textup{(W$^\pm$)} fails and that ..."

Membership in R_0^± also requires r_l > 0 for all l, and (W^±) as displayed (line 5030) is only the liminf condition. Write "f ∉ R_0^± (some
r_l = 0, or (W^±) fails), f fails (BT), and ...". The failure of (BT) is said one sentence earlier, but it belongs in this characterization too.

**13. Remark rem:Binf, lines 5654-5655: the definition does not cover the claim.**
> "more generally Theorem~\ref{thm:Bstar} should hold for window-pinned mates at first rows with arbitrary $F$."

Definition def:windowpinned (line 4938) assumes that F is finite, so "window-pinned at f with F infinite" is undefined. Add "(with
Definition~\ref{def:windowpinned} read verbatim for infinite $F$)".

**14. Remark rem:openZ (O1)(ii), lines 5782-5784: the parenthetical does not match its examples.**
> "such as weak peaks or near-threshold strict non-peaks (failure of (E1) in Remark~\ref{rem:thmM})"

(E1) says "every l ∈ U is a strict non-peak", so a near-threshold strict non-peak satisfies it. Its difficulty is quantitative: gaps that are
not bounded below are what make its usage inexact. The Z1 referee groups these carriers together loosely ("weak or near-threshold (E1 fails)").
For accuracy, write "(weak peaks violate (E1); near-threshold strict non-peaks satisfy (E1) but their gaps are not bounded below)".

## 2. Optional suggestions (not required)

- **rem:thmM, line 5696** ("close in spirit to Theorem S").
  - A first row in the class of rem:thmM is in R_S (case B_fin) whenever r*_l > 0 for the good carriers in U: slaving closure gives
    S*_l = S_l \ F for good l ∉ U, so (W*) follows from (SR). (H2) holds and (H3) is vacuous by (E1).
  - So the sketch adds something only when a good carrier in U loses all its room to the targets of bad carriers.
  - Saying this would show how small the gap between the sketch and the proved theorem is.
- **Lemma lem:switchbudget**: say explicitly that no smallness of t is needed, which the Z2 referee confirmed. The proof says "for every t > 0",
  but the lemma does not.
- **Z2 referee correction 3, second half.** At d-neutral bad carriers the budget also gives Phi(k_l)|Omega_±(k_l)| = O(1). This could be added
  after lem:windowtwopiece(d). It is not needed.
- **rem:Bpm(c)**: the sufficient condition sum_{l'<=l}(s_1-s_0)(l') = o(l^3) along a subsequence is correct, since the alternating bound gives
  Lambda^±/Lambda° <= C^l 2^{sum of gaps}. It is a condition on the design and on F, and F affects only finitely many l. Saying "(a condition on
  the sets S_l of the design)" would match the Z2 referee's correction 7, which is otherwise already met.

## 3. Items checked and found correct (no action)

- Lemma lem:phicalc (a)-(d); Lemma lem:switchbudget, with the corrected consequences; Remark rem:budgetgloss (correct form of the Z2 gloss).
- Lemma lem:split: the three cases re-derived, and the bound |e_±(j)| <= |e(j)| + phi_z(B_+(j)) + phi_{-z}(B_-(j)) checked.
- Lemma lem:peakshift and eq:didentity, against Z2 2.1-2.2 and the sup-level lemma.
- Lemma lem:flip, against Z1 4.1 (the constants t/(4q_0) and t/(2q_0) re-derived).
- Lemma lem:boundedfree, against Z1 4.3: injectivity uses Y ∩ c_00 = {0} and the injectivity of T; F finite is stated.
- Definition def:windowpinned and Theorem thm:Bstar, against Z1 1.5: (SR) enters only through Prop pinned(a); K = K_j + 6 <= 7K_j.
  Remark rem:Bstar.
- Definition def:R0pm, Lemma lem:signmixed (unrolling constant 1/q_0 + 22), Theorem thm:Bpm (including R_0 ⊂ R_0^± via
  1 + 3/(gamma delta') <= (3/(2gamma))(1 + 2/delta')), Remark rem:Bpm(a)-(d).
- Definition def:swallowed, with the naming map: Z2's (H3), (H4), (H5) are the paper's (H1), (H2), (H3). The remark that (H2) is automatic and
  (H3) vacuous under (B_res) is correct: bad carriers are then strict non-peaks, and every block has a non-degenerate peak because ||alpha||_1 = 1.
- Lemma lem:modswallow: the unified triangular system, as the Z2 referee requested.
- Lemmas lem:badpeaks, lem:exactswitch (Hoffman, cost function, violation bounds), lem:windowtwopiece (a)-(d) (including the corrected
  (3+eta)/t <= 4/t and A_2), lem:onesidedtransfer, lem:avgfunctionals.
- Theorem thm:S: the chain Gamma <= (1+2kappa_0)^2 = 1 + eta_0/2, kappa_w(rho bar D_j) <= rho^2(1 + eta_0/2) <= 1, then Cor D1.
- Remark rem:nodesign (first-order base cost only, as corrected). Remark rem:meagre (a)-(c), against Z2 5.3.
- No exposed-face consequence and no common-functional obstruction appear. Theorem M and Theorem B^inf appear only as sketches.
