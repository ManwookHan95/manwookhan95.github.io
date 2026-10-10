# Referee report B: Sections 4 and 5 of `martin_density_note_II.tex`

Scope: Section 4 (lines 2982-4642: clean sub-windows, pinning, banks and tuning, companion
assembly, transplant, Master Theorem II) and Section 5 (lines 4643-7683: Hoffman/Lojasiewicz
exactification, Theorem B, shift dichotomy and Master Theorem III', structure of shifted data,
self-aligned rows and genericity, absorbers and Master Theorem IV', nested tuning, open problems).
Line numbers refer to the current file (10350 lines).

Sources checked line by line: r6/Y1_referee.md, Y1_ref_notes.md (m2-m5); r7/V1_referee.md,
V1_ref_notes.md, V1_notes.md (p0-p5); r7/V2_referee.md, V2_ref_notes.md, V2_notes.md (P1-P7,
F2-F6); r7/V4_referee.md, V4_ref_notes.md, V4_ref_part2.md, V4_notes.md (R3, R5, R8, R10, R11);
r8/U1_referee.md, U1_ref_notes.md, U1_ref_part3.md, U1_notes.md; r8/U3_referee.md, U3_ref_notes.md,
U3_notes.md; r6/Y4_ref_notes.md.  Key steps were re-derived independently (Theorem B Steps 1-6,
Lemma TU hypotheses, c^comb and Cor. C11(a), Prop. SAmates (iii)/(iv), Lemma zerovalue (i),
Prop. Baire, Lemma classes / Prop. ray constants, Prop. S1).

## Verdict

Most of Sections 4-5 is a faithful transcription of the refereed sources with the referee
corrections incorporated (list at the end).  Nothing that a referee found wrong is stated as
proved: Master Theorem IV and Corollary IV.1 of U1 are explicitly not claimed
(Remark `rem:II-notMTIV`, lines 7299-7312), (S2a) of U3 appears only as the sketch (S2a') inside
Remark `rem:II-openS`, Y4's directional residual and Z1's exposed-face consequence do not occur in
Sections 4-5, and density / Lemma Z are stated as open (lines 7678-7680).

However there are **16 required fixes** (R1-R16).  Five of them concern false statements or
invalid proof steps inside proved results (R1, R2, R9, R11, R12), three concern definitions
that make a proof step fail (R6, R7, R13), and the rest are wrong formulas, wrong hypotheses,
mis-citations of non-existent bounds, or necessity overclaims (R3, R4, R5, R8, R10, R14, R15,
R16).  All are fixable without changing the main architecture; none of them changes the status
(open) of density or Lemma Z.

Severity: MAJOR = R1, R2, R6, R9, R11, R12; MEDIUM = R7, R10, R13, R14, R15; MINOR (but a false
formula or citation) = R3, R4, R5, R8, R16.

---

## REQUIRED fixes

### R1 (MAJOR). Theorem B: status clauses are ill-defined and false for dropped carriers (V2-ref P2 only half incorporated)

Lines 4974-4976, 4987-4988, 5041-5044, 5087-5092, and 6707-6708.

Quoted:

- 4974-4976: `\item[(A2)] after $\mathcal M_{\rm ass}$ every carrier of $E$ has the status prescribed by $\kappa$, every peak of $\kappa$ has relative margin $\ge u(w)/2$, ...`
- 4987-4988: `\item[(a)] the pattern of $f^\#$ is $\kappa$ \textup{(}same carriers, signs, contacts on $T(l)$ and statuses\textup{)}, and $\supp a^\#$ is finite;`
- 5043-5044: `... so every coarse carrier keeps its status.`
- 5089-5090: `(A2) holds by Lemma~\ref{lem:II-status} (in blocks without a donor raise the kept carriers are robust or nearly neutral, or near-threshold, and the buffer push of Step~4 protects them).`
- 6707-6708 (Def. `def:II-Gamma`): `Let $f^\#$ be a companion of $f$ whose coarse carriers have the statuses of the closed pattern $\kappa(w)$.`

Problem.  (i) A pattern is `\kappa=(E,P,\epsilon,F',\mathrm{type})` (Definition
`def:II-constants`(a), line 2119); it records no statuses and no peaks, so "status prescribed by
kappa" and "peak of kappa" are undefined.  (ii) Under the only available reading ("status at
f"), (A2), (a) and Step 4 are false for the assembly of Section 4, which is what Theorem B is
applied to (lines 5087-5094): E contains the dropped set P, which contains anti-type tiny-margin
peaks (relative position in [1, 1+b(w)], class (P-i)).  Their margin is <= b(w) < u(w)/2, so
"every peak ... has relative margin >= u(w)/2" fails, and both the donor raise
(threshold up by >= c_f Lambda, Lemma `lem:II-status`(b)) and the buffer push (Lemma `lem:II-QB`(b)
applies to every coarse carrier of the block with v < theta + R - X, kept or not) turn them into
strict non-peaks, so "every coarse carrier keeps its status" is false.  This is exactly V2-ref
F2/P2 ("dropped anti-type near-threshold strict non-peaks and anti-type tiny-margin peaks may sit
in blocks without a donor raise ... With the d-rows of V1's transplant (kept carriers only) the
clause holds exactly and the statuses of dropped carriers enter no minor").  The paper
incorporated the second half (rows (Z4) are unit rows, lines 4956-4957) but not the first.
Note that the proof of Proposition `prop:II-ray`(a) (line 6809-6810) uses that "tiny-margin peaks
of f are strict non-peaks of f^#", i.e. the opposite of "keeps its status".

Fix.  Replace the three status clauses by the precise status table:

- (A2) first line: "after $\mathcal M_{\rm ass}$ every kept carrier ($l''\in\mathrm{Kp}$) is a
  strict non-peak, and every coarse peak of $f$ with $\varrho\ge1+u(w)$ is a peak with the same
  sign and relative margin $\ge u(w)/2$; and every kept carrier either has gap ..." (rest of (A2)
  unchanged).
- (a): "$f^\#$ has the carriers $E$, the kept set $\mathrm{Kp}$, the signs $\epsilon$ and the
  contacts on $T(l)$ of $\kappa$, and $\supp a^\#$ is finite; every kept carrier is a strict
  non-peak of $f^\#$, every coarse peak of $f$ with $\varrho\ge1+u(w)$ is a peak of $f^\#$ with the
  same sign, and every coarse carrier with $|\varrho-1|\le C_*(l)b(w)$ at $f$ (kept or dropped; in
  particular every tiny-margin peak) is a strict non-peak of $f^\#$.  Nothing else is asserted
  about dropped carriers; they enter $\Sigma^\#$ only through the unit rows (Z4)."
- Step 4, line 5043-5044: replace "so every coarse carrier keeps its status" by "so every kept
  carrier stays a strict non-peak, every coarse peak with $\varrho\ge1+u$ stays a peak with its
  sign (Lemma `lem:II-status`(c),(d)), and every coarse carrier with $|\varrho-1|\le C_*b$ is a
  strict non-peak (threshold rise $\ge c_f\Lambda\gg C_*b$)".  In the no-donor case, state that
  Lemma `lem:II-QB`(b) is applied with $L$ = all coarse carriers of block $m$ (so that tiny-margin
  peaks, kept or dropped, become strict non-peaks), and replace "every coarse peak of $\kappa$
  (relative margin $\ge u/2$)" (line 5060-5061) by "every coarse peak of $f$ with
  $\varrho\ge1+u(w)$".
- Lines 5089-5090: "(A2) holds by Lemma `lem:II-status`(c),(d) for kept carriers and robust peaks;
  the statuses of dropped carriers are not needed".
- Def. `def:II-Gamma`, lines 6707-6708: "Let $f^\#$ be the companion of Theorem `thm:II-B` for the
  closed pattern $\kappa(w)$ (statuses as in Theorem `thm:II-B`(a))".

### R2 (MAJOR). Theorem B: the buffer push of a class-R buffer peak cannot be realized by Lemma TU

Lines 4983-4985 and 5023-5030.

Quoted: 4983-4985 `in each block without donor raise, one outward push of the buffer peak $c_m$ of
Lemma~\textup{\ref{lem:II-buffer}}, all realized by one application of Lemma~\textup{\ref{lem:II-TU}}`;
5028-5030 `and, in each block without donor raise, with the additional prescribed outward push of
size $s_m$ (Step 4) at the buffer peak $c_m\notin\mathrm{Kp}$.`

Problem.  Lemma `lem:II-TU` (lines 3595-3635) has no provision for a "prescribed push" of a
carrier outside $L_0$; a carrier is moved by the lemma only if it is in $L_0$, and then
hypothesis (T1) ($z^2=\epsilon_{l''}$ on $S_{l''}\setminus[1,s_{\max}(l)]$) is required.  The
buffer peak of Lemma `lem:II-buffer` (lines 4899-4920) is any coarse peak with
$|\alpha_m(c)|\ge1/(2l)$, possibly of class R.  For a class-R peak the far room is robust and
not closed by (C1), so (T1) fails and the push cannot be produced by pulls/banks of Lemma TU.
(The remark at lines 4927-4930 "available in either direction by z-moves, banks or pulls" is
correct only with the z-move option, which is not Lemma TU.)

Fix.  Replace "all realized by one application of Lemma TU" by: "the push being realized first and
entering Lemma TU as base data: for a class-G buffer peak by a pull or bank on far coordinates
of $S_{c_m}$ (which satisfy (T1) after (C1)), for a class-R buffer peak by a z-move (or
close-and-bank) on far coordinates of its robust room as in (C3) (Lemma `lem:II-donorraise`),
with size in $[s_m,2s_m]$; followed by one application of Lemma TU with $L_0=\mathrm{Kp}$".  In
Step 3 (lines 5023-5030) say accordingly that the push masses / z-changes are part of the base
data $(A^2,z^2)$ (their coordinates lie in $S_{c_m}$, $c_m\notin\mathrm{Kp}$, so (T2) is
unaffected), and in Step 4 use $s\in[s_m,2s_m]$ (the bound $C_1(s+E)+X\le u\bar\vartheta_m/4$
still holds with the factor 2).

### R3 (MINOR). Theorem B Step 5 cites a cost bound that Lemma TU does not contain

Line 5066: `\emph{Step 5 (cost).}  The cost bound of Lemma~\ref{lem:II-TU} gives $p^*(f^\#-f_1)\le ...`

Problem.  Lemma `lem:II-TU` (a)-(d) gives exact values, side effects, mass bounds (c) and
admissibility (d); it has no cost bound (the cost item of V1's Lemma TU was not transcribed).

Fix.  "By Lemma `lem:II-TU`(c) the pull and bank masses are $\le C_f\mathrm{Des}\,2^{G(l)}\eta(w)$;
with the masses of $\mathcal M_{\rm ass}$ and of the push, Lemma `lem:II-cost` gives, exactly as
in the proof of Lemma `lem:II-compcost`(e), $p^*(f^\#-f_1)\le\dots$" (same right-hand side).

### R4 (MINOR). Theorem B Step 4: wrong lower bound for h_0

Lines 5058-5059: `$h_0\ge\min(1,\bar\vartheta_m/(2l))$ by Lemma~\ref{lem:II-buffer}`.

Problem.  Lemma `lem:II-buffer` gives $\varrho_c-1\ge A_m/(2l\Phi_c^2\bar\vartheta_m)$, hence
$\mathsf v_c-\bar\vartheta_m=\bar\vartheta_m(\varrho_c-1)\ge A_m/(2l)$; the threshold
$\bar\vartheta_m$ does not appear.

Fix.  Replace by `$h_0\ge\min(1,A_m/(2l))$`, and note that $C_1(s_m+E)<h_0$ holds for $l\ge l_f$
because $C_f\mathrm{Des}^4\eta(w)\le C_fT_{\rm lo}(w)^4\mathrm{Des}^3/l$ and $A_m$ is an
$f$-constant.

### R5 (MINOR). The norm in the definition of Lip(l) is unspecified; Theorem B Step 1 needs the sup-norm

Lines 2154-2156 (Def. `def:II-constants`(c)): `let $\mathrm{Lip}(l)\ge1$ be a common Lipschitz
constant on $[-2,2]^{[1,l]}$ of all $\pi_{\kappa,J,K}$ whose $J$ contains a value row`; used at
lines 5006-5008: `is $\mathrm{Lip}(l)$-Lipschitz on $[-2,2]^{[1,l]}$, so by (A1) it moves by at
most $\mathrm{Lip}(l)C_*(l)b$ from $f$ to $f_1$`.

Problem.  (A1) bounds each coordinate change by $C_*(l)b(w)$, i.e. the $\ell_\infty$ change; with
an $\ell_2$- (or $\ell_1$-) Lipschitz constant Step 1 loses a factor $\sqrt l$ (or $l$), and then
$\beta(w)=(1+\mathrm{Lip}C_*)b(w)$ of Proposition `prop:II-subwindows`(d) is not the right bound.
Step 2 (line 5019) uses $\|v'-v\|_2\le\eta$, which is compatible with the $\ell_\infty$ reading.

Fix.  In Def. `def:II-constants`(c) write "a common Lipschitz constant with respect to the
$\ell_\infty$-norm on $[-2,2]^{[1,l]}$"; then Step 1 is correct as written and Step 2 follows from
$\|\cdot\|_\infty\le\|\cdot\|_2$ (add these five words in Step 2).

### R6 (MAJOR). c^comb omits the dropped non-peaks, so the proof of Corollary C11(a) fails

Lines 5235-5236: `$G_{\rm np}:=E\setminus (P\cup G_{\rm pk})$`; proof lines 5281-5284:
`On $T(l)$, $|L(j)-V_j(\tau)|$ is bounded by $\max|u|$ times the (S2) defects and
$\sum_{G_{\rm np}}(\tau)_-$, ... Hence $c^{\rm comb}(\delta_{I_{\rm sh}};\kappa^{\rm sh})\le
C\mathrm{Des}\,\mathrm{viol}(\delta,\tau)$.`

Problem.  $P$ is the dropped set of the pattern (line 4937).  The row (S3) of $\Sigma^{\rm sh}$
(line 2275-2277) uses $V_j(\tau)=\sum_{l''\in E}\epsilon_{l''}\tau_{l''}u_{l''}(j)$, i.e. it
contains the dropped carriers, while $L$ contains only $G_{\rm pk}$ and $E\setminus(P\cup
G_{\rm pk})$.  Hence $L(j)-V_j(\tau)$ contains $-\sum_{l''\in P\setminus G_{\rm pk}}
\epsilon_{l''}\tau_{l''}u_{l''}(j)$, which no row of $\Sigma^{\rm sh}$ controls (dropped
non-peaks are only subject to (S1) $\tau\ge0$, possibly (S7) and (S4)), so the displayed
bound and hence (a) are not proved.  V2 used $G_{\rm np}$ = all class-G non-peaks (dropped
included), which is what the proof needs.

Fix.  Define `$G_{\rm np}:=E\setminus G_{\rm pk}$`.  With $x:=(\tau)_+$ on $G_{\rm np}$ the
displayed bound then holds verbatim, and (b) is unchanged in form (the exact resonance may use
nonnegative coefficients on dropped non-peaks).  No later statement refers to $G_{\rm np}$
(checked: the symbol occurs only at lines 5235-5282).

### R7 (MEDIUM). G_pk ("the class-G peaks of kappa") is undefined and, read literally, breaks (S2)

Line 5148: `and $G_{\rm pk}$ the class-G peaks of $\kappa$.`; line 5170-5172 (proof of Lemma
`lem:II-R17`): `at a peak of $\kappa$ (relative margin $\ge u/2$) $\mu_k\ge c_f\Phi_{l''}u\ge
c_fu/\mathrm{Des}$`.

Problem.  Patterns carry no peaks (see R1).  If $G_{\rm pk}$ is read as all class-G peaks of $f$,
it contains the tiny-margin peaks (relative margin $\le b(w)$), where $\mu_k\ge c_f\Phi u$ is false
and the (S2) defect $t/(\lambda\mu_k)$ is not $\le C_f\mathrm{Des}\,t/u$; so Lemma `lem:II-R17`
fails for (S2) at those carriers.  V2-ref P3 requires the pattern to record $G_{\rm pk}$ as a
window classification.

Fix.  Line 5148: "and $G_{\rm pk}$ the class-G coarse carriers that are peaks of $f$ with
$\varrho\ge1+u(w)$ (tiny-margin peaks belong to $E\setminus G_{\rm pk}$)".  Line 5171: replace
"at a peak of $\kappa$ (relative margin $\ge u/2$)" by "at $l''\in G_{\rm pk}$ (relative margin
$\ge u$)".  For tiny-margin peaks only the one-sided bound $\tau\ge-K_gt$ of (S1) is used, which
Lemma `lem:II-diagpin` gives (already stated at line 5166-5167).  Make the same replacement in
the (O9) bookkeeping if a definition of $G_{\rm pk}$ is given there (line 2267 only says
$G_{\rm pk}\subseteq E$).

### R8 (MINOR). Proposition constcontact is stated for "any admissible operator" but proved only for T_final

Lines 5511-5512: `Let $T$ be any admissible operator whose signature sets are pairwise disjoint
\textup{(}e.g.\ $T_{\mathrm{final}}$\textup{)}, ...`

Problem.  The conclusion speaks of clean sub-windows, sources (U2)/(L2), $\rho^{\rm sh}$, (C*)
rows and $\Rec$ via Theorem `thm:II-C1` and Theorem `thm:II-MTIII` (proof, line 5535-5536); these
objects and theorems exist only for $T_{\mathrm{final}}$ (clean sub-windows are defined from the
sub-window data of Def. `def:II-Tfinal`(6)).  V2-ref P5 states it for the design at hand.

Fix.  "Let $T=T_{\mathrm{final}}$, $N\ge1$, $f\in S_{p_N^*}$ with $F$ finite ...".  (If desired,
keep a remark that the first part of the proof, existence of carriers $l_\pm$ with
$\varrho\ge2$ and $z\equiv\epsilon_0$ on their signature sets, uses only (T-d) and disjoint
signature sets.)

### R9 (MAJOR). Proposition SAmates (iii): the normalization beta^+(xi)=0 makes g(xi) != 0, so (iii)/(iv) are false

Lines 5898-5901: `For every $\chi:F^c\to[0,1]$ and every $\beta^+$ supported in $F$ with
$\beta^+(\xi)=0$, the pairs $b^+:=\chi\Delta_\alpha\lambda_{l_-}V1_{F^c}+\beta^+$, ... are
two-piece data for $g:=b^++R_1^*(\omega^+-d(\omega^+)w_1)$.`

Problem.  $\xi=q_0\zh$ and $\zh_j=z_j$ off $F$, all coordinates off $F$ are contacts, and
$V1_{F^c}$ is $z$-signed (item (ii)).  Hence $(V1_{F^c})(\xi)=q_0\sum_{j\notin F}|V_j|>0$ and
$b^+(\xi)=q_0\Delta_\alpha\lambda_{l_-}\sum_{j\notin F}\chi_j|V_j|+\beta^+(\xi)>0$ whenever
$\chi\ne0$ and $\beta^+(\xi)=0$.  The block part satisfies $R_1^*(\omega-d(\omega)w_1)(\xi)=0$, so
$g(\xi)=b^+(\xi)\ne0$; such $g$ is not tangent at $f$, the pieces are not two-piece data, and
$cg\notin\Cset(f)$ (first-order growth of $p^*(f+rcg)$ for one sign of $r$), contradicting (iv).
V4 Prop. 3.2 normalizes $b^+(\xi)=0$, not $\beta^+(\xi)=0$.

Fix.  Replace "with $\beta^+(\xi)=0$" by "with $b^+(\xi)=0$, i.e. $\beta^+(\xi)=-q_0\Delta_\alpha
\lambda_{l_-}\sum_{j\notin F}\chi_j|V_j|$ (possible since $\xi\ne0$ on $F$)", and add to the proof
of (iii) one line: $V(\zh)=u_{l_-}(\zh)-(u_{l_-}(\zh)/A)\psi(\zh)=0$ because $\psi(\zh)=A$, hence
$b^-(\xi)=b^+(\xi)=0$.  The same normalization must be used where these mates are re-used
(Proposition `prop:II-NLreal`, line 5943, and the proof of Master Theorem IV' if it builds data
from them; see also optional item O8).

### R10 (MEDIUM). Proposition Baire: the specific choice eps_l=(Phi_{l+1}/Phi_l)^2 is not justified for "any admissible operator"

Lines 6018-6019: `With $\varepsilon_l:=(\Phi_{l+1}/\Phi_l)^2$, the row $f_a$ fails \textup{(BT)} for
every $a$ in this set.`; proof lines 6040-6043: `... or infinitely many peaks with
$\mu_l=q_0\Phi_l(\mathsf v_l-\bar\vartheta_m)/m<s_l:=q_0\Phi_{l+1}^2/(m\Phi_l)$, and
$\Phi_l/s_l\to\infty$ contradicts (MS).`

Problem.  The setting (lines 5995-5997) is "any admissible operator".  $\Phi_l/s_l=m\Phi_l^2/
(q_0\Phi_{l+1}^2)\to\infty$ requires $\Phi_{l+1}/\Phi_l\to0$, which is not part of admissibility
((T-a)-(T-d)); moreover $\Phi_{l+1}$ is ambiguous (next carrier overall, possibly of another
block, or next carrier of block $m$).  V4-ref (V4_ref_part2.md 2.1(3), V4_referee.md line 42)
records that any $\varepsilon_l\to0$ suffices and that the specific choice is not needed.

Fix.  Replace the last sentence of the statement by "If $\varepsilon_l\to0$, the row $f_a$ fails
\textup{(BT)} for every $a$ in this set", and in the proof put $s_l:=q_0\Phi_l\varepsilon_l/m$,
so that $\mu_l<s_l$ and $\Phi_l/s_l=m/(q_0\varepsilon_l)\to\infty$ contradicts (MS).

### R11 (MAJOR). Lemma zerovalue (i): the intermediate-value argument fails for theta_a of the size used later (inherited from U1 Lemma 3.3)

Lines 6641-6647 (statement) and 6665-6671 (proof):
`0\le\mathrm{Tg}-4\sum_{r=1}^R2^{-r}\sigma_r\le2^{3-R},\qquad\mathrm{Tg}:=-\big(\beta\zh_s+1+
q^*(x)\delta_ah_a(\zh)\big)`, `... $p_0$ a support coordinate with mass $m_0\in[\theta_a,
\theta_a+c_p^2]$, where $0<\theta_a\le\lambda_a$.`; proof: `At $m_0=\theta_a$ the right side lies
in $[-2^{3-R}-\epsilon,\epsilon]$ with $\epsilon=O((\mu^\star)^2\theta_a)$; raising $m_0$ by
$\Theta\in[0,c_p^2]$ raises $\zh_{p_0}$ by at least $(\mu^\star_{p_0})^2\Theta/(2\nu)$ ..., which
sweeps more than $2^{4-R}$ by the choice of $R$.  The intermediate value theorem gives
$u_a(\zh)=0$`.

Problem (re-derived).  $q^*(x)n_au_a(\zh)=-(\mathrm{Tg}-4\sum2^{-r}\sigma_r)+(\mu^\star_{p_0})^2
m_0/\nu+(\text{second-order terms of }p_r,\ S_a)$, and this is increasing in $m_0$.  The sign
choice only gives $\mathrm{Tg}-4\sum2^{-r}\sigma_r\in[0,2^{3-R}]$, while the term
$(\mu^\star_{p_0})^2\theta_a/\nu$ at the left end $m_0=\theta_a$ is not small compared with
$2^{3-R}$: by the choice of $R$ (line 6539, $2^{3-R}\approx(\mu^\star_{p_0})^2(c^{\rm low}_p)^2/4$)
the left-end value is positive as soon as $\theta_a\ge(c^{\rm low}_p)^2/4$ (roughly), and then
the increasing sweep never reaches $0$.  This happens for $\theta_a=\lambda_a$ (allowed by the
statement) and for the value $\theta_a=C_f\mathrm{Des}\,\lambda_aT_{\rm hi}$ needed for "no flips"
in Proposition `prop:II-absorb`(d) (U1-ref part 3, item (d)), because
$\lambda_a=2^{-1-k(a)}c_a\ge2^{-1-k(a)}c^{\rm low}_p$ while $(c^{\rm low}_p)^2\le c^{\rm low}_p\,
b(p-1,M(p-1))^2$ is astronomically smaller (and $T_{\rm hi}(w)\gg b(L,M(L))^2$).  The "$\epsilon=O((\mu^\star)^2\theta_a)$" in the proof is exactly this term
and is not $\le2^{4-R}$.  U1-ref (U1_ref_part3.md 3.2) checked the sweep length but not the left
endpoint, so this error is new relative to the referee reports; it is inherited from U1
Lemma 3.3 ("any theta_a works").

Fix.  Compute the target at the left endpoint.  Put
`$\mathrm{Tg}:=-\big(\beta\zh_s+\zh_{p_0}+q^*(x)\delta_ah_a(\zh)\big)$` with all $\zh$-values
evaluated at the row with $m_0=\theta_a$ (for diagonal $U$ these values, and $\nu$, do not
depend on the signs $\sigma_r$, since $\nu$ depends only on the moduli of the masses), write
$\zh_{p_r}=\sigma_r(1+e_r)$ with $0\le e_r:=(\mu^\star_{p_r})^2\theta_a/\nu$, and choose the
signs greedily for the weights $4\cdot2^{-r}(1+e_r)$ so that
$\mathrm{Tg}-\sum_r4\cdot2^{-r}(1+e_r)\sigma_r\in(0,2^{4-R}]$ (possible with error
$\le2^{2-R}(1+O(Re_1))$ around the shifted target $\mathrm{Tg}-2^{3-R}$, since $e_r\le e_1$ is
negligible: $p_1>p_0$ gives $(\mu^\star_{p_1})^2\le(\mu^\star_{p_0})^{2\cdot2^{2^{p_0}}}$; if
needed require in Def. `def:II-DU1` that $p_0$ is so large that $4e_1\le2^{-R}$).  Then the value
at $m_0=\theta_a$ lies in $[-2^{4-R},0)$, the sweep exceeds $2^{4-R}$, and the intermediate value
theorem applies.  Also check (or state) $c_p\ge c^{\rm low}_p$ for the stage of the absorber, which
the sweep bound "more than $2^{4-R}$" uses.  Statement (i) should then say "for every
$\theta_a\in(0,\lambda_a]$ there are signs $\sigma_r$ (depending on $\theta_a$) and $m_0\in[\theta_a,
\theta_a+c_p^2]$ with $u_a(\zh)=0$".  Part (ii) (simultaneous tuning) needs the same left-end
target for each absorber.

### R12 (MAJOR). Design D^{U1'} and activity classes: circular and N-dependent design factor; class constants are not of the form C_f(Des/u)^C

Lines 6575-6580 (Def. `def:II-DU1`): `At a main stage $L$ the design factor $\mathrm{Des}(L)$
additionally contains ... and the class counts $D_{\rm cls}(w)$ of Lemma~\ref{lem:II-classes}
below; ... and $Q(w)\ge D_{\rm cls}(w)^2(\mathrm{Des}(L)/u(w))^C$ for the constant $C$ of
Proposition~\ref{prop:II-ray}.`; lines 6699-6701: `$K$ denotes quantities of the form
$C_f(\mathrm{Des}(L)/u(w))^C$; the window arithmetic absorbs them (Lemma~\ref{lem:II-GW}(GW2) and
$Q(w)\ge D_{\rm cls}(w)^2(\mathrm{Des}/u)^C$).`; line 6747: `Let $J:=|\Omega|+N$, ...
$A_1:=K_*$, $A_{i+1}:=K_*A_i$`; lines 6779-6781 (Prop. `prop:II-ray`(a)): `$X(t)$
\textup{(}inactive components set to $0$\textup{)} violates \textup{(X1)}, \textup{(X3)},
\textup{(X4)} at the coefficients of $f^\#$ by at most $Kt$`; lines 6796-6798:
`$D_{\rm cls}(w):=(J+1)3^J(A_{\max}/\varepsilon)^p\le(\mathrm{Des}/u)^{C'}$`; line 7294:
`Projection moves components by $\le Kt$`.

Problems.  (a) Circularity: $\mathrm{Des}(L)$ determines $Q(w)$, $n(w)$, $T_{\rm lo}(w)$, $b(w)$ and
hence $u(w)$ of the sub-windows of level $L$, while $D_{\rm cls}(w)$ depends on $u(w)$ (through
$\varepsilon=c_f(u/\mathrm{Des})^C$ and $A_{\max}$); it cannot be a factor of $\mathrm{Des}(L)$.
(b) $D_{\rm cls}(w)$ is not a design number: it depends on $f$ ($C_f$, $c_f$, $\Delta_{\max}$ in
$A_{\max}\le C_f(\mathrm{Des}/u)^C\Delta_{\max}$) and on $N$ through $J=|\Omega|+N$, whereas
design numbers "do not depend on $N$" (line 2115) and Lemma `lem:II-DU1`(a) asserts
$N$-independence of $D^{U1'}$.  (c) The exponents grow with $L$: $A_{J+1}=K_*^{J+1}$ with
$J$ up to $2L$, and $(A_{\max}/\varepsilon)^p$ with $p$ the number of extreme rays (not bounded
by a universal constant); so "$\le(\mathrm{Des}/u)^{C'}$" and "$K$ of the form
$C_f(\mathrm{Des}/u)^C$" with fixed $C$ are false, and (GW2) (which allows only
$\mathrm{Des}^8$ and $(C/u)^{\omega+8}$ with a fixed $C$) does not absorb them.  (d) Zeroing the
inactive components costs up to $JA_{i(t)}Kt$ (Lemma `lem:II-classes`), so Prop. `prop:II-ray`(a),(b)
("at most $Kt$") and line 7294 ("Projection moves components by $\le Kt$") are false as stated;
the correct bound is $(1+C_f\mathrm{Des}\,J\,A_{i(t)})Kt$, which is what the last sentence of
Lemma `lem:II-classes` needs, and that sentence requires $K_*\ge4C_f\mathrm{Des}\,J\,H$ ($H$ the
Hoffman bound), not only "$K_*\ge2\mathrm{Des}(L)$ dominating the Hoffman constants".

Fix.  (1) Delete "and the class counts $D_{\rm cls}(w)$ of Lemma `lem:II-classes` below" from
$\mathrm{Des}(L)$.  (2) In Lemma `lem:II-classes` put $J:=|\Omega|+|I(L)|$ ($I(L)$ the blocks of
carriers $\le L$; the components $\Delta'_m$, $m\notin I(L)$, vanish by (X3)), so $J\le2L$, and
require $K_*\ge4C_f\mathrm{Des}(L)\,J\,H(L)$ with $H(L)\le C\mathrm{Des}^C/u$ the Hoffman bound of
Prop. `prop:II-ray`(b).  (3) Let $P(L)$ be a design bound for the number of extreme rays of the
cones $\Gamma^\#(a)$ of main stage $L$ (e.g. a binomial coefficient in the numbers of rows and
columns) and $\bar D(w):=(2L+1)3^{2L}(\mathrm{Des}(L)/u(w))^{C(P(L)+2L+2)}$; this is a design
number of the sub-window ($u(w)$ is one), and for $L\ge l_f$ (so that $C_f\Delta_{\max}\le
\mathrm{Des}(L)/u(w)$) it dominates $D_{\rm cls}(w)$, $K_*^{J+2}$ and all class constants.
Require $Q(w)\ge\bar D(w)^2(\mathrm{Des}(L)/u(w))^C$, either by defining $Q(w)$ for $D^{U1'}$ as the
maximum of the $T_{\mathrm{final}}$ value and this quantity, or by proving $\omega(L)+20\ge
C(P(L)+2L+3)$ (the rate scheme contains the minors of Def. `def:II-Gamma`, so $\omega(L)\ge P(L)$,
but the constant must be checked).  (4) Replace "$K$ denotes quantities of the form
$C_f(\mathrm{Des}(L)/u(w))^C$; ... (GW2) ..." by the explicit statement that all constants of
this subsection are $\le\bar D(w)^C$ and are absorbed because $T_{\rm hi}(w)\le
2^{-L^3}/(LQ(w))$ and $n(w)\ge L2^{L^3}Q(w)$.  (5) In Prop. `prop:II-ray`(a),(b) and at
line 7294 use the bound $(1+C_f\mathrm{Des}\,JA_{i(t)})Kt$ and cite the last sentence of Lemma
`lem:II-classes` for the sign/size of the active components.

### R13 (MEDIUM). Proposition S1: the definition of a free ray does not cover the case r<0

Lines 7539-7542: `whose column $\epsilon_ku_k1_{F^c}$ is a \emph{free ray} of the combinatorial
zero-cost rows \textup{(}it vanishes on $T(l)\setminus F$, or it is $z$-signed there and adding
it to any solution keeps every row satisfied\textup{)}`; lines 7544-7545: `if $r<0$ and
$x_k\ge|r|/|q_k|$, then $(\delta,x+(r/|q_k|)e_k)$ satisfies the combinatorial rows`; proof line
7551: `Adding a multiple of a free ray keeps the combinatorial rows`.

Problem.  For $r<0$ the proof subtracts $(|r|/|q_k|)$ times the column.  The second alternative
of the definition only guarantees that adding the column keeps the rows; subtracting a
$z$-signed vector can violate a sign row $\mathrm{type}(j)L(j)\ge0$ at a contact of $T(l)$.  U3's
definition (U3_notes.md lines 576-577, accepted by U3-ref) is: "its target coordinates in
$T(l)$ are contacts dominated by their owners or lie in $F$", which makes both adding and
removing harmless.

Fix.  Replace the parenthesis by "(at every $j\in T(l)\setminus F$ with $u_k(j)\ne0$, $j$ is a
contact whose row is satisfied for every value $x_k\ge0$ of the coefficient, e.g. because the
owner of $j$ dominates; in particular this holds if $u_k$ vanishes on $T(l)\setminus F$)", and in
the proof write "Changing $x_k$ within $[0,\infty)$ keeps the combinatorial rows".

### R14 (MEDIUM). Necessity claims that are only heuristic

(a) Lines 7635-7636 (Remark `rem:II-openS`, item (S1)): `(By Proposition~\ref{prop:II-Rkt} this
needs two independent levers per block, as in Remark~\ref{rem:II-openKN}.)`

(b) Line 7650: `The $d$-consistency in (S2a$'$) is necessary for this route: ...`

(c) Lines 5699-5702 (Remark `rem:II-C6`): `Subsection~\ref{subsec:II-absorb} replaces (g2) by
zero-value absorber pairs, closes (g3) in configuration (i), (g4) and (g5), and shows that (g1)
reduces to one scalar per block but requires a second, independent lever.`

Problem.  Proposition `prop:II-Rkt` proves first-order rates of change under pushes; it does not
prove that one lever per block is insufficient, and Remark `rem:II-onelever` says explicitly
"No claim is made that the conclusion of a one-lever exactification fails" (lines 6526-6527);
U1-ref likewise records no impossibility result.  The necessity of $d$-consistency in (b) is
supported only by an upper bound, finite models ("numerical evidence") and a heuristic
(U3-ref F6: HEURISTIC).  In (c), "requires a second, independent lever" is the same unproved
necessity, and "closes ... (g4) and (g5)" holds only under the hypotheses of Master Theorem IV'
(the lever (KN$_{w,a}$); for mixed classes also no frustrated positive carrier, Remark
`rem:II-openmix`).

Fix.  (a) "(Proposition `prop:II-Rkt` and Remark `rem:II-onelever` explain why a single push per
block does not obviously suffice; whether two independent levers per block are necessary is not
decided --- \emph{heuristic}.)"  (b) "The $d$-consistency in (S2a$'$) appears to be needed for this
route (\emph{heuristic}): ..." (rest unchanged; it already labels its evidence).  (c) "...
replaces (g2) by zero-value absorber pairs, and, under the hypotheses of Master Theorem IV'
(Theorem `thm:II-MTIV`), closes (g3) in configuration (i), (g4) and (g5); it reduces (g1) to one
scalar per block, which is handled there by the lever hypothesis (KN); whether a second,
independent lever is necessary is not decided (Remark `rem:II-onelever`)."  (Outside Sections
4-5, the introduction's "The lever is needed" should be aligned with this wording; flagged for
the referee of Section 1.)

### R15 (MEDIUM). Corollary B1: the coefficient bound |q^#-q| <= C eta(w) is false in donor-raised blocks

Lines 5116-5119: `the violation of (Z5) is bounded by the shift term $C_fK_dt$ (through
[I,~(17)]) plus $C\eta(w)\sum_{l''}|\tau_{l''}|\le C\eta(w)\cdot12/t\le CT_{\rm lo}(w)^3$, because
$|q^\#_{l''}-q_{l''}|\le C\eta(w)$ and $\sum_{l''}\lambda_{l''}\le1$.`

Problem.  $q^\#_{l''}=\mathrm{val}^\#_{l''}/A^\#_m$ and $q_{l''}=\mathrm{val}_{l''}/A_m$ (row (Z5),
Lemma `lem:II-status`(d)).  In a block with a donor raise the donor value moves by
$\asymp\Lambda/\lambda_{c_m}$ (Lemma `lem:II-compcost`(c)), so $|A^\#_m-A_m|\asymp\Lambda=T_{\rm lo}(w)^3
\gg\eta(w)$, hence $|q^\#-q|\asymp|\mathrm{val}|\Lambda/A_m^2$, not $O(\eta)$; the displayed bound
would only give $C\Lambda/t\le CT_{\rm lo}(w)^2$.

Fix.  Use the homogeneity of (Z5): multiply the row of block $m$ by $A^\#_m/A_m\in[\frac12,2]$
(changing its violation by a factor $\le2$).  Then the coefficients become
$\mathrm{val}^\#_{l''}/A_m=q_{l''}+x_{l''}/A_m$, i.e. $|q^\#_{l''}A^\#_m/A_m-q_{l''}|\le\eta(w)/A_m\le
C_f\eta(w)$, and the violation is $\le2\big(|\sum q_{l''}\tau_{l''}|+C_f\eta(w)\sum|\tau_{l''}|\big)
\le C_fK_dt+C_f\eta(w)\cdot12/t$, as claimed.  Replace "because $|q^\#_{l''}-q_{l''}|\le C\eta(w)$"
by this argument.

### R16 (MINOR). Overgeneralized summary after Lemma Dprime

Lines 5451-5453: `Thus in a block of a (C$^*$) row every robust coarse peak has, at every clean
sub-window of every large level, a tiny room on its natural signature set, and all of them have
one type`.

Problem.  Lemma `lem:II-Dprime` (lines 5434-5441) concerns a block without an upper (resp.
lower) source; a (C*) row has such a block at every clean sub-window (line 5420-5424), but
not every block of a (C*) row is source-deficient.

Fix.  "Thus in a source-deficient block ($m\in I_{\rm up}(w)\cup I_{\rm lo}(w)$) of a (C$^*$) row
every robust coarse peak has, at that clean sub-window, ...".

---

## Optional suggestions

O1. Remark `rem:II-onesigned`(a), lines 3520-3522: "Since $u_w/b_w\ge2^{64}$ and $u_w\to0$ ...
the rate is $<u_w$" does not follow from $u/b\ge2^{64}$ alone; use Lemma `lem:II-scales`(c)
($b\le2^{-64/u}$), i.e. $u_w/b_w\ge u_w2^{64/u_w}\to\infty$.

O2. Lemma `lem:II-sources`, (L3), lines 3329-3331: the $q>0$ carriers contribute
$\ge-(b_w/C_m)\sum6\lambda/t$, which is not included in "in total $\ge-K_gt/C_m$"; add the
term $-6b_w/(C_mt)\ge-6t^3/C_m$ (harmless).

O3. Proof of Lemma `lem:II-R17`, line 5175-5176: "the closed-pattern budget of
Lemma~\ref{lem:II-diagpin}" -- Lemma `lem:II-diagpin` contains no such budget; cite the Step 1
argument of Proposition `prop:II-transplant` (cost of the closed rooms) instead.

O4. Theorem B, lines 5087-5089: (A1) follows from Lemma `lem:II-compcost`(b) and
Lemma `lem:II-cost` (cost bound), not from Lemma `lem:II-status`; and in Step 4 state explicitly
that near-threshold kept carriers of no-donor blocks get $\gap^\#\ge\gap$ (needed later for
(X4)).

O5. "absorbed by (GW2)" (lines 5122-5123, 5227-5228, 6700): (GW2) allows only
$\mathrm{Des}(l)^8$ and $(C/u)^{\omega+8}$ with fixed $C$; factors $C_f\mathrm{Des}^Cu^{-C}$ with
$C\le\omega(l)+20$ are absorbed directly by $Q(w)$ ($T_{\rm hi}\le2^{-l^3}/(lQ(w))$,
$n(w)\ge l2^{l^3}Q(w)$).  Cite that, or extend (GW2) to $\mathrm{Des}(l)^{C}$.

O6. Theorem `thm:II-C1` and Lemma `lem:II-R17`: add "$t\le\min(t_\eta,1)$" to the scales, as in
Proposition `prop:II-transplant` (line 4151), since [I, Lemma 8.5] decompositions are used.

O7. Proposition SAmates (ii), line 5919: "for $l_-$ late" is unnecessary ($c_1\ge\frac12$ and
$2^{-5}c_2\lambda_{l_-}\le\frac1{32}$ always); harmless.

O8. Proof of Master Theorem IV', lines 7248-7252: say explicitly that $\beta$ (supported in
$F^\#$) is chosen with $b^+(\xi^\#)=0$ (cf. R9); otherwise the data are not tangent.

O9. Lemma `lem:II-domfine`(i), line 7054: "$T_{\rm lo}(k-1)\le T_{\rm lo}(w)$" holds only for
carriers $k$ at stages $>L$; for coarse owners (types (a), (b)) restrict to $j>s_{\rm far}(w)$ or
give the separate (easier) bound.

O10. Lemma `lem:II-recursion`, line 7018: "$O(k)\supseteq S_k$" fails on $S_k\cap F^\#$
($J_{\rm fine}\cap F^\#=\emptyset$); write $O(k)\supseteq S_k\cap J_{\rm fine}$.

O11. Lemma `lem:II-QB2` proof: the lower bound $|a^b_j|\ge m_j/(1+\mathsf m)$ should read
$m_j/(1+(1+\|U\|)\mathsf m)$ (normalization by $q^*$); constants only.

O12. Lemma `lem:II-classes`: note that class-R $\Omega$-carriers are always inactive ((X1) at
free coordinates forces $\gamma=0$, proof of Prop. `prop:II-ray`(c)), which simplifies the count.

O13. Proposition `prop:II-transplant`(ii), lines 4391-4393: "$K_U+NK_{\rm pin}+1$" should be
"$K_U+lK_{\rm pin}+1$" (the coarse sum has $l$ terms); both are $\le C_fG^{**}(l)l^3D_{\rm r}^4
u^{-4}$, so harmless (and the $N$ would otherwise suggest an $N$-dependent constant).

---

## Verified correct (no change required beyond the items above)

Section 4: Lemma `lem:II-scales`(a)-(e); Lemma diagpin (incl. $e_0$ bound via
$\sum_{l'>l}\lambda\le b^2/3$); peakrel; sources (with O2); donorpeak; shiftpin; pinned (Y1-ref m2
hypothesis $|\Delta d|M\le K't$ incorporated); bankformula; Lemma TU ($c_T=c_f\mathrm{Des}^{-1}$,
$C_T=C_f\mathrm{Des}$, V1-ref p4 incorporated); companion moves (C1)-(C4), donorraise, compcost,
status, exactrobust, IP (re-derived); Proposition transplant (V1 Prop. TR, with O13);
Master Theorem II, Corollaries N1, AC, residual list, Remark master2.  V1-ref p0-p5 and Y1-ref
m2, m5 are incorporated; Y1-ref m3 is not applicable (bank donors).

Section 5: Lemmas hoffman, loj, raycomp, QB (with $k_0=c$), buffer; Theorem B Steps 1, 2, 6 and
the Hoffman bound $C_f^l\mathrm{Des}^2/u$ (subject to R1-R5); Corollary B1 (subject to R15);
Lemma R17 (subject to R7, O3); Theorem C1 (dichotomy), Theorem Eshift, Lemma subset, MT III',
Definition Cstar, Corollary Cstarnec; Lemma Dprime, Proposition C3 and Remark C3 (heuristic
correctly labelled), Proposition C4, C5, Remark C5, Corollary A, Remark C6 (subject to R14);
Theorem SA (Steps 1-8 re-derived), Corollary SArec, Proposition NLreal, Proposition FZ, Corollary
FZ, Remark FZ, dom, align, R5, BTdense; Proposition Rkt, Remark onelever; Lemma DU1,
firsttouch, Proposition absorb, (X4) corrected form, G1 release, (KN), Lemma recursion,
domfine (with O9, O10), Master Theorem IV' cases ($\alpha$), ($\beta$), ($\gamma$) (= U1 Cor.
IV.2-IV.4 with (KN), as U1-ref requires), Remark notMTIV; alignedres, Theorem NT (conditional on
existence, existence only as Remark NTexist sketch), NTM (both alternatives, U3-ref F2), NTR,
QB2 (U3-ref F4 incorporated), Rpin, VT; Remarks openKN, openmix, openmisc; the closing
statement that density and Lemma Z remain open (lines 7678-7680).

Quantifier order: design before $f$ is respected everywhere except Def. `def:II-DU1` (R12);
companions after $f$, data after $g$, $\rho$, $t$ are respected (MT II, MT III', MT IV' proofs).

Count: **16 required fixes (R1-R16)**, 13 optional suggestions (O1-O13).
