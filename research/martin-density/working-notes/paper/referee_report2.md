# Referee report 2: new Sections 7 (Engineered approximants) and 8 (A designed admissible operator), updated abstract and Section 9

File checked: `ctx/paper/martin_density_note.tex` (4808 lines). The new material is lines 2659-4590. The abstract (lines 39-68) and Section 9
(lines 4591-4769) are updated. Sources used: BRIEFING_R2 (all addenda), r2/P2_notes (= P2A), P2A_referee, P2_referee (P2x part), N2_*,
r3/S3_notes + parts, S3_referee, S3_ref_notes (Lemma F1, F2-F4), r3/G3_notes + parts, G3_referee, G3_ref_notes, r3/R3_notes, R3_referee.
Compiled with pdflatex in `ctx/paper/build2/` (current file copied there): 61 pages, no errors, no undefined or multiply defined references,
11 overfull boxes (see Fix 14).

## 0. Verdict

**I re-derived every proof in Sections 7 and 8 line by line. I found no error in a theorem, lemma or proposition.** The referee corrections from
the sources are all applied:

- **S3, Lemma F1 repair.** Lemma `lem:F1` uses the monotone root equation F(c;v) = 1. The root is located with continuity (Lemma
  `lem:approxfacts`(b)), not with the rate, so the argument is not circular.
- **S3, common sequence of scales.** Definition `def:SC` builds it into (SC), and the paragraph after it explains why.
- **S3, 4.4 is heuristic.** Remark `rem:withoutSC`(b) calls it a "Sketch, not used" and states that the failure of the approximants is not
  proved.
- **S3, constant 4 in the anchor.** Lemma `lem:anchor` uses 4.
- **S3, infinite F in the open core.** This is Problem `prob:infiniteF`.
- **G3, kappa_0.** The theorem uses kappa_0 = (sqrt(1+eta_0/2)-1)/2, and the extra condition K_4 Lambda_f t <= kappa_0 is imposed.
- **G3, 6.3(b) wording.** Remark `rem:lemmaZ`(b) now says that coarser carriers can be slaved.
- **G3, 6.3(c).** Remark `rem:lemmaZ`(c) says that the mate condition is exactly the open question.
- **G3, unused hypothesis in 5.2.** The hypothesis c_1 t^(j) <= rho s_0 is dropped.
- **R3, rigid design.** It is not claimed to be recovered (Section 9, lines 4737-4742).

**The constants work for rho close to 1.** I checked Theorem `thm:engineered`, Lemma `lem:uniformtransfer`, Theorem `thm:windowed` and
Theorem `thm:R0` for rho close to 1:
- delta = (1 - rho^2 kappa_w)/2 > 0;
- eta_1, T_0, kappa_0 and n_j all depend only on delta, eta_0 or 1 - rho^2, which stay positive;
- the windows satisfy n^w_l/K_l -> infinity.

**Checked and correct.** The following are correct as written:
- Lemma `lem:bookkeeping`, Lemma `lem:TV` and Proposition `prop:rebalancing`: all inequalities re-derived, including the base algebra
  -l_b - G_b + Gamma.
- Lemma `lem:transferdata` and Lemma `lem:persistence`.
- Lemma `lem:assembly`.
- Proposition `prop:onesidedupper`.
- Theorem `thm:onesided`: Steps 1-4, including the Gram consistency <e,k_2> = -kappa_2||a||_1/nu, the identification of the dual cone of
  C_+, and Rockafellar 31.1.
- Lemma `lem:approxfacts`: (E1)-(E5).
- Lemma `lem:F1`.
- Lemma `lem:anchor`.
- Lemma `lem:scrambling`.
- Theorem `thm:engineered`: all six steps, including the exactness of the three decompositions, the kappa^sigma rewriting, the sign
  analysis of Exc', and the budget 5 delta/8 <= delta.
- Corollaries `cor:weightedengineered`, `cor:D1`, `cor:BTrecovered` and `cor:exampleRecovered`, including the (MS) verification.
- Theorem `thm:SLD`. The paper's lambda_l <= c_l/4 is sharper than G3's c_l/2 and is correct.
- Lemmas `lem:twosided` through `lem:finitebase`.
- Lemmas `lem:box`, `lem:pinning` and `lem:triangular`, and Proposition `prop:pinned`.
- Proposition `prop:windowcert`.
- Lemma `lem:uniformtransfer`.
- Theorem `thm:windowed`.
- Theorem `thm:R0`, Corollary `cor:nodefectR0` and Theorem `thm:reductionZ`.

**What still needs fixing.** The required fixes below are:
- one gap in a hypothesis, in a remark (Fix 1);
- one unjustified inequality inside a proof (Fix 2);
- an incomplete abstract and summary (Fix 3);
- a handful of serious notational clashes that make proofs ambiguous (Fixes 4-10);
- smaller wording issues and LaTeX issues.

None of them affects the truth of a theorem.

---

## 1. Required fixes (mathematics and claims)

### Fix 1 (Remark `rem:withoutSC`(a), lines 3817-3822): the sufficient condition for K^scr < infinity is not proved
Quoted text:
> "Finiteness of $K^{\rm scr}_m$ is not automatic: the truncated mass of near-threshold peaks can be of order $s\log(1/s)$ for admissible
> $T$; it holds, for instance, under \textup{(MS)} together with gaps of the strict non-peaks bounded below off a finite set."

There are two problems.

(i) The first clause is the S3 referee's Remark F4. That remark is a SKETCH (the construction of T is "built after zhat", P1 2.1 technique).
Here it is stated as a fact. It should be labelled "(sketch)".

(ii) The second clause does not follow from the stated hypotheses. Take strict non-peaks with gap_k >= g_0. They enter Scr_m(s) (and the
anchor remainder) through k with Phi_m(k) gap_m(k) <= s, i.e. Phi_m(k) <= s/g_0. Their contribution is
sum{Phi_m(k) : Phi_m(k) <= s/g_0}. Lemma B gives only Phi_m(k) <= 2^{-m-k}, and Phi_m(k) need not be monotone or geometric. The only general
bound is then sum_k min(2^{-k}, s/g_0) ~ (s/g_0) log_2(1/s), which is O(s log(1/s)), not O(s).

By S3-referee Proposition F3 (PROVED), admissible T can cluster Phi on blocks of length L_j -> infinity by column rescaling. At x = Phi(k_j)
the sum is then >= L_j x. So the "non-peak part" of K^scr can be infinite under (MS) plus gaps bounded below. The S3 referee's own F4 sentence
has the same gap, so this is not an import error. It is still an unproved claim in the paper.

Required: do one of the following.
- Add a regularity hypothesis, e.g. Phi_m(k+1) <= beta Phi_m(k) with beta < 1 (then sum_{Phi_k <= x} Phi_k <= x/(1-beta)).
- Restate the hypothesis as "sum{Phi_m(k) : k in Q_m, Phi_m(k) gap_m(k) <= s} = O(s) and (MS)".
- Label the sentence as a sketch.

Also, because the peak part needs (MS), say explicitly that K^scr < infinity is a HYPOTHESIS of the implication. The paper does this: "along a
construction sequence for which all K^scr_m are finite". Keep that.

### Fix 2 (Theorem `thm:R0`, proof, lines 4456-4477): "Gamma_w(c_t) <= 1 + eta_0/2 <= 2" needs eta_0 <= 2
Quoted text:
> "Choose $\eta_0>0$ with $\rho^2(1+\eta_0)\le(1+\rho^2)/2$ ..."
> "i.e.\ $\Gamma_w(c_t)\le1+\eta_0/2\le2$, and (C-b) holds"

The constraint rho^2(1+eta_0) <= (1+rho^2)/2 allows eta_0 up to (1-rho^2)/(2 rho^2). That is > 2 for rho < 1/sqrt(5). The inequality
1 + eta_0/2 <= 2 is needed for (C-a) of Lemma `lem:uniformtransfer` (Gamma_w(c) <= 2), and it fails for such eta_0.

Required: write "Choose eta_0 in (0, 2] with rho^2(1+eta_0) <= (1+rho^2)/2". This is harmless (eta_0 may be taken small), but the displayed
"<= 2" is otherwise unjustified. The same applies to Corollary `cor:nodefectR0`, which reuses the proof.

### Fix 3 (abstract, lines 52-57): the engineered result is stated without its standing hypotheses
Quoted text:
> "every mate with one-sided linear decompositions of weighted coefficient at most one and non-negative $d$-mismatch is recovered, for
> arbitrary contact sets and any number of blocks"

Theorem `thm:engineered` and Corollary `cor:D1` assume:
- (i) I finite (Section 7 standing assumption; Remark `rem:blocks`);
- (ii) F = supp a finite;
- (iii) the decompositions are two-piece data, i.e. omega^pm_m finitely supported in Q_m and b^pm supported in F cup K with the contact
  signs.

"any number of blocks" reads as including I = N, which is not proved (G3 referee correction 5 makes the same point for "covers O4").

Required wording, for example: "at first rows with finite base support, every mate with one-sided (two-piece) decompositions of weighted
coefficient at most one and non-negative d-mismatch is recovered, for arbitrary contact sets and any number of active blocks (for each
finite block set; infinite block sets via Lemma martintail)".

Similarly in Section 9, line 4636, "no hypothesis on the number of active blocks" is fine. Line 4606 ((S4)) correctly says "I is finite".

## 2. Required fixes (notational clashes that make a proof ambiguous)

### Fix 4 (Section 8, Theorem `thm:R0` proof, line 4466, against Definition `def:SLD`, line 3877): n_l is used for two different things
Quoted text:
> Def SLD: "$n_l:=q^*(y_l+\delta_lh_l)$" (normalising constant, n_l in [3/4, 5/4]);
> proof of Thm R0: "For a window index $l$ put $t^{(l)}:=T_{\rm hi}(l)$, $n_l:=n^w_l$ and $K_l:=\dots$"

Both meanings live in the same section, and the second one (n_l = n^w_l, a huge integer) overwrites the first. Required: drop
"n_l := n^w_l" and write n^w_l throughout the proof (it already uses n^w_l in the display), or rename it.

### Fix 5 (Section 8): c_1 denotes both the first ladder weight and the local-validity constant
Quoted text:
> Def SLD (D1): "given $c_l\in(0,1]$ ($c_1:=1$)"; Theorem SLD proof: "$q^*(Te_{k,m})=c_l\le1=c_1$";
> Lemma `lem:uniformtransfer`: "there are $c_1\in(0,\frac18]$ and $t_1>0$"; Theorem `thm:windowed`: "there are $c_1\in(0,1]$";
> Theorem R0 proof: "let $c_1,t_1$ be given by Lemma~\ref{lem:uniformtransfer}".

In the proof of Theorem R0, c_1 (the ladder weight, = 1) and c_1 (<= 1/8) coexist. Required: rename the constant of Lemma
`lem:uniformtransfer` / Theorem `thm:windowed`, e.g. c_loc or c_\flat.

### Fix 6 (Theorem `thm:engineered`, Steps 2-4): Y_m is used for two different objects in the same proof
Quoted text:
> Step 2: "If $\Delta d_m\ge0$, let $Y_m:=w_m$ ... If $\Delta d_m<0$, let $Y_m:=y_{A,m}$"
> Prop `prop:rebalancing` (applied in Step 4): "Put $Y_m:=\ip{y_m}{\zeta_m}$", and Step 0: "$|Y'^\varsigma_m|/c'\le K_Y$".

Step 4 applies Proposition `prop:rebalancing`, whose Y_m is a scalar. Step 3 uses Y_m as an element of l_inf (the anchor). Required: rename the
anchor vector in Steps 2-3 (e.g. A_m^\natural or V^{\rm an}_m) everywhere: "Y_m:=w_m", "Y_m:=y_{A,m}", "r_mY_m", "\ip{Y_m-w'_m}{R_mx'}",
"N_m(Y_m)" and "\mathfrak g_m:=N_m(Y_m)-\ip{Y_m}{R_mx'}/\sigma'_m". Relatedly, "(1-r_m)V_m:=W_{0,m}-r_mw'_m=(1-r_m+\tau\kappa^\sigma_m)(\dots)"
(line 3595) defines V_m with a factor (1-r_m) that does not match the right side, and V_m is never used. Delete V_m and write
"W_{0,m}-r_mw'_m=(1-r_m+\tau\kappa^\sigma_m)(\dots)".

### Fix 7 (Section 7): tau denotes the tail function and the scalar parameter in the same theorem
Quoted text:
> Def `def:engineered`: "$\tau(N''):=\sum_{m\in I}\sum_k\lambda_{k,m}t_{k,m}$", (N1) "$\tau(N''_i)\le s_{1,i}^2$";
> Theorem `thm:engineered`: "$f'+\tau g'$", "$0<|\tau|\le T_1$", "$|\tau|>s_1$".

Also "tau_*" in Lemma `lem:transferdata` and Theorem `thm:transfer`. Required: rename the tail, e.g. tail(N'') or \mathfrak t(N''), in
Definition `def:engineered`, (N1), (E3)-(E5), Lemma `lem:F1`, its proof, and Lemma `lem:scrambling`.

### Fix 8 (Theorem `thm:onesided`, Steps 2-4): Psi, Phi, beta and lambda are redefined although their Section 1/3/7 meanings are in use
Quoted text:
> Step 4: "$\Psi(y):=\sup\Big\{2g(Uk+\chi_c)-\frac\nu{q_0}\|k\|^2:\dots\Big\}$"
> but Lemma `lem:base` ("$\Psi(h):=\|e+h\|-1-\ip{e}{h}$") is used in the same section (Lemma `lem:bookkeeping`(b), Prop
> `prop:onesidedupper`, Theorem `thm:engineered` Step 3 "$\nu'\Psi'(\dots)$").
> Step 2: "$\Phi(k,\chi_c):=2g(\chi)-\dots$" (Phi_m are the block weights), "$\Psi_*(\lambda)$", "$\lambda\in\R^n$" (lambda_{k,m} weights;
> lambda in Prop `prop:rebalancing`), "$n:=\sum_m(|Q_m|+1)$", and "$\beta:=g-\varphi_\lambda/2$" (beta = ||U^*b|| in Definition
> `def:certificate`).

Required: rename, e.g. Psi -> \mathcal P (value function), Phi(k,chi_c) -> \mathcal J(k,chi_c), lambda -> \mu or \pi, beta -> b_\pi,
n -> n_Q.

### Fix 9 (Definition `def:SC` and the paragraph after it, lines 3397-3409): K is the contact set
Quoted text:
> "satisfies the \emph{scrambling condition} \textup{(SC)} if for every $K\ge1$ there is a sequence $s_i\downarrow0$ ... with
> $\max_{m\in I_-}\mathrm{Scr}_m(Ks_i)/s_i\to0$"; "every block satisfies $\mathrm{Scr}_m(Ks)=o(s)$ as $s\to0$ for every $K$"

K is the contact set (Section 1, line 352). It appears in the same section (Definition `def:twopiece`, Theorem `thm:engineered`, "(SC) for
$K:=2K_*$"). Required: use another letter (e.g. A or \Upsilon) for the multiplier in Definition `def:SC`, Lemma `lem:scrambling`, the
remark after Definition `def:SC`, Theorem `thm:engineered` ("Construction"), and Corollary `cor:BTrecovered`. Likewise "K_0" is the
constant of Theorem `thm:engineered` Step 0 and also the contact set K_0 = S_{l_0} of Section 6, used in Corollary `cor:exampleRecovered`
twenty lines later. Rename the constant (e.g. K_\sharp).

### Fix 10 (Sections 7-8): iota and vartheta_0 clash with established symbols
Quoted text:
> Prop `prop:rebalancing`: "the \emph{inefficiency} $\iota_m:=\dots$"; Def `def:SLD` (D0): "Fix a bijection $\iota:\N\times\N\to\N$";
> Def `def:windowcert`: "$\iota(k,m)\le l_*$".
> Def `def:R0`: "there are $\gamma\in(0,1)$ and $\vartheta_0\in(0,1]$" (vartheta_m is the threshold constant, line 266; vartheta and
> vartheta' are used in Lemmas `lem:transferdata` and `lem:scrambling`).

Required: rename the ladder bijection (e.g. \ell, as in Section 6, or \mathfrak j) and the room constant (e.g. \varpi_0 or r_0). The
paragraph in Section 8 (lines 3847-3849) lists symbols "local to this section", but iota and vartheta_0 are not among them, and they clash
with Section 7 and Section 1.

### Fix 11 (Sections 7-8): further overloaded symbols (lower priority, but required for readability)

**(a) sigma: label versus weight.** In Theorem `thm:engineered`, sigma is both a label in {+,-,theta} and the block weight sigma_m:
> "$d^\sigma_m:=d_m(\omega^\sigma_m)$ for $\sigma\in\{+,-,\theta\}$" ... "$c'h'(\beta^\sigma)+\sum_m\sigma'_mH'_m(\omega^\sigma_m)$"

Use another label letter, e.g. \diamond in {+,-,theta}.

**(b) s: variable versus the function s(t) = sqrt(1+t^2).** In the proof of Theorem `thm:windowed`, s is the variable and s(.) is the
function of line 76:
> "$p^*(f+s\rho g_{c_{t_i}})\le p^*(f+s\rho g)+\rho|s|Kt_i\le s(\rho s)+\rho|s|Kt_i$", "$1+\frac{s^2}2-\frac{s^4}8\le s(s)$"

Lemma `lem:uniformtransfer` and conditions (i)-(iii) of Theorem `thm:windowed` also use s as the variable, and s is also a coordinate
s in S_l in Section 8. Use tau or r as the variable.

**(c) rho: radius versus scaling.** Proposition `prop:windowcert`(c) has "Let $\rho_k:=|\omega_+(k)-\omega^c(k)|$", but rho in (0,1) is
the scaling throughout. Use \varrho_k or e'_k.

**(d) m_j: mass versus block index.** Definition `def:engineered` has "$m_j:=4\rho s_1|b^\theta_j|$", but m is the block index and
lambda_{k,m} = m Phi_m(k) appears in the same lemmas. Use \mathsf m_j or \mu_j.

**(e) N: window versus block count.** Definition `def:engineered` has "For a \emph{window} $N\ge\max F$", but in Sections 1 and 8, N is the
number of blocks (p_N, I = {1,...,N}), and in Section 6 it indexes the canonical truncations f'_N. Use N_w or W for the window, and N''
remains the cut-off.

**(f) kappa: six meanings.** kappa is used for:
- kappa(c) (Definition `def:certificate`);
- kappa_w (Definition `def:twopiece`);
- kappa_2 (Theorem `thm:onesided`);
- kappa^sigma_m (Theorem `thm:engineered`);
- kappa_{l',l} (Lemma `lem:pinning`);
- kappa_t (Definition `def:windowcert`);
- kappa_0 (Theorem `thm:R0`).

At least kappa_t (a scalar base coefficient) and kappa_{l',l} should be renamed, because both appear in Section 8 next to kappa_0.

**(g) c: five meanings in Section 8.** c is used for:
- c_l (weights);
- c^pm_l (block coefficients);
- c_t (certificate);
- c_1 (Fix 5);
- c' (= q(x'), Section 7).

At least the coefficients c^pm_l / Delta c_l should get their own letter, e.g. theta^pm_l, so that "Delta c_l" is not read as a difference
of weights.

## 3. Required fixes (unproved or imprecise wording)

### Fix 12 (Remark `rem:onesided`(b), lines 3188-3192): the strict inequality is provable and should be proved, not attributed to numerics
Quoted text:
> "When $K$ is infinite, $\gamma^\pm(g)$ can be smaller than $\Gamma_w$ of a balanced finite certificate representing $g$ ... This is the
> phenomenon observed numerically in finite models ... (numerical evidence only)."

As written, an existence claim about Mart\'in's space rests on finite-model numerics. A two-line proof is available at the example of
Section 6.

Take g := c u_{2,1}. It has the certificate data (0, (c/lambda_0)e_2), with Gamma_w(g) = sigma_1 c^2/C_1 =: B. For theta in [0,1] the pair
(theta c u_{2,1}, (1-theta)(c/lambda_0)e_2) is side-+ admissible: u_{2,1} > 0 on K_0, and z = 1 there (Lemma T (P1)). Its weighted
coefficient is theta^2 A + (1-theta)^2 B with A := q_0 h(c u_{2,1}). A > 0 because U^*u_{2,1} is not a multiple of U^*e_1^* (U^* is
injective, and supp u_{2,1} meets K_0). Hence

  gamma^+(g) <= AB/(A+B) < B = Gamma_w(g).

On side -, only theta <= 0 is admissible, so gamma^-(g) = Gamma_w(g).

Required: replace the sentence by this argument, or by "can be smaller (e.g. gamma^+ < Gamma_w for g = c u_{2,1} at the first row of
Lemma firstrow)". State explicitly that whether max(gamma^+, gamma^-) < Gamma_w can occur is the open question of Remark `rem:kinks`(a).

### Fix 13 (various): imprecise or unsupported wording
(a) Lemma `lem:R0`(c), line 3974: "$\mathcal R_0$ contains first rows with infinite contact sets and with near-contacts, with arbitrary block
structure."
The proof says nothing about the block structure. The block data are determined by zhat and T, and cannot be prescribed. Replace with "and
(SR) imposes no condition on the block data".

(b) Remark `rem:lemmaZ`(b), line 4546: "for all $\gamma,\vartheta_0$, some signature set satisfies ..." should say "some signature set
$S_l$, $l\in\mathcal L_N$, satisfies ...". Also, "$\delta'_{l_0}=0$" depends on gamma. Say "for every gamma".

(c) Section 9, lines 4738-4742: "operators $T$ have been proposed whose near-threshold peak carriers are one-sided with bounded conversion
capacity; for them no recovery argument is known (the available arguments leave a capacity requirement that does not improve as
$\rho\to1$)".
This is unreferenced, and the phrase "does not improve as rho -> 1" is not what R3_referee found. R3_referee found a rho-INDEPENDENT
Hilbert/room-capacity requirement on the converted carriers, which does not disappear when the error-driven part is removed. Suggested:
"... leave a Hilbert (room) capacity requirement on the converted carriers that is independent of rho and of the error terms". Either give a
citation (companion note) or say "one can design operators T ... (we do not include this construction)".

(d) Line 3727: "the engineered recovery of $d$-neutral two-piece mates of the companion notes" cites "companion notes" that are not in the
bibliography. Cite them, or delete the clause.

(e) Line 3760: "Corollary~\ref{cor:BTrecovered} contains Theorem~\ref{thm:tame} (which needed $K$ finite)". Theorem `thm:tame` also asserts
recovery along the canonical truncations, which Corollary `cor:BTrecovered` does not. Say "contains the conclusion $f\in\Rec$ of Theorem
tame". The same applies to (S4), line 4609.

(f) Line 3051: "The last sentence proves the statement left as a sketch in Remark~\ref{rem:transfer}(c)". Remark `rem:transfer`(c) has
already been rewritten to say "this is proved in Proposition onesidedupper". Delete the sentence at line 3051, or make Remark
`rem:transfer`(c) a plain forward reference.

(g) Definition `def:twopiece`, lines 2979-2981: "A pair with $b$ supported in $F$ is admissible on both sides; it is then a balanced finite
certificate". Being a balanced finite certificate (Definition `def:tame`) requires b(xi) = 0, i.e. g(xi) = 0. Add "if $g(\xi)=0$".

(h) Lemma `lem:approxfacts`(c), line 3236: "and at late stages for the bounds involving $|R_m\hat x'|_m$". Only (E4) uses a lower bound on
|R_m x̂'|_m. (E3) holds at every stage. Move the qualifier to (E4).

## 4. Required fixes (LaTeX)

### Fix 14: overfull boxes in the new sections
The build in `build2/` reports these overfull boxes. All except the first are in the new material.

| Lines | Width over | Where |
|---|---|---|
| 2805-2808 | 2.3pt | proof of Proposition `prop:rebalancing` |
| 3610 | 16.5pt | display "$G'_m(W^\natural_m)\le\hat G_m:=\dots,\ \mathfrak g_m:=\dots$" |
| 3885 | 19.3pt, in alignment | Definition `def:SLD` (D1), gather line with $T_{\rm hi}$, $n^w_l$ |
| 3933-3941 | 14.4pt | injectivity proof in Theorem `thm:SLD` |
| 4058-4062 | 13.9pt | Lemma `lem:budget`(b) |
| 4114-4117 | 2.6pt | Lemma `lem:suplevel`(f) |
| 4196-4205 | 5.6pt | proof of Lemma `lem:triangular` |
| 4275-4281 | 9.0pt | proof of Proposition `prop:windowcert`(b) |
| 4546-4556 | 8.5pt | Remark `rem:lemmaZ`(b) |
| 4671-4676 | 15.3pt | Section 9 paragraph after Problem `prob:main` |

Required fixes:
- Break the displays at 3610 and 3885 into two lines (`multline`/`split`, or separate `gather` rows).
- Rewrite the inline formulas at 3936, 4060, 4200 and 4278 as displays.
- Check the rest with `\sloppy` locally or by rephrasing.

### Fix 15: minor LaTeX and markup points
(a) Line 4333: "\]  The first term is at most" begins a paragraph-continuation line directly after a display. Add a line break or `%` for
clean source. This is cosmetic.

(b) Theorem `thm:engineered`, Step 0, lines 3494-3499: "the conditions marked $(T_1)$ below". The marks "(condition $(T_1)$: ...)" appear
only twice, and "(condition $(T_0)$ ...)" several times. Consider listing all (T_0)/(T_1) conditions in one display in Step 0. The proof is
correct, but the reader must collect seven scattered conditions to see that the order of choices (T_1, K_0 -> eta_1 -> transfer data ->
T_0 -> s_1 -> N'') is consistent. I checked that it is.

## 5. Points checked in detail (no change needed; for the record)

**Theorem `thm:engineered` Step 2.**
- Identities: beta^pm - beta^theta = pm v/2; Omega^pm - Omega^theta = mp(rho/2)((omega^- - omega^+) - Delta d w).
- With v = sum_m R_m^*((omega^-_m - omega^+_m) - Delta d_m w_m), all three decompositions represent g' exactly.
- The kappa^sigma rewriting is an identity.
- tau rho (d^sigma - d^theta) = -r_m sgn(Delta d_m) holds on both sides.
- In the anchor case W^natural = W_0 - r w' + r y_A, by w' - w = (y_A - w') + Z_A.

**Theorem `thm:engineered` Step 3.**
- The sign analysis of Exc'(tau B^sigma) covers every coordinate class: F, window contacts with and without mass, contacts in (N, N''],
  contacts beyond N'', and free coordinates.
- Exc' = 0 for the theta-piece needs |tau rho beta^theta_j| <= m_j/4 <= |a'_j|/2. This holds because |tau| <= s_1.

**Theorem `thm:engineered` Steps 4-5.**
- |eps_m| <= 6 K_0 tau^2.
- The transfer-vector radius conditions hold. Here gamma_m > M_m/2 is what makes eta <= gamma/2.
- E <= delta tau^2/8.
- Final budget: rho^2 kappa_w + 5 delta/8 <= 1 - delta.

**Lemma `lem:F1`.** The k-natural term gives a uniform negative slope on [C-r, C+r]; |min(x,s)^2 - min(x,s')^2| <= 2x|s-s'|; the D-norm
bound O(s_1^2 log(1/s_1)) uses only Phi_m(k) <= 2^{-m-k}. Correct, and not circular.

**Lemma `lem:anchor`.** Every line checked, including the disjoint-support bound X_0 <= 3||D(w'-w)||^2 + 2 sum_A Phi^2 <= X.

**Theorem `thm:onesided`.**
- Z_{t,j} = (q_0 + t^2 kappa_2) z_j on F.
- ||h_t|| = q_0 + t^2 kappa_2 + O(t^3).
- b(chi_c) <= 0 for side-+ pairs.
- Every linear form on R x R^{Q_m} is V = omega + (c/M)w, and it is of the form 2v iff <V, zeta_m> = 0.
- -Psi_* splits into q_0 h(beta) plus the indicator of side-+ admissibility.
- Rockafellar 31.1 applies: Q is finite on R^n, Psi is proper concave, and the minimum is attained.

**Section 8.**
- Pinning: the triangular unrolling uses 1/delta'_l <= 1 + 2/delta'_l and sum_l kappa_{l',l} <= 4/3.
- Fine tail: sum_{l>l_*} |Delta c_l| <= 6 T_lo(l_*)^3/t <= 6t^2.
- Proposition `prop:pinned`(c) uses Phi^2 Delta Theta = Phi Delta c/m.
- Window certificate: the three cases at k in Q (inside the clamp, beyond the clamp with gap >= t^2, gap < t^2), and the peak case.
- Uniform transfer: the radius is >= min(t/4, C_m t/2), and the order eta_1 -> c_1 -> t_1 is consistent.
- Windowed averaging: Q <= (1-rho^2)/12 gives 1 - (1-rho^2)/3, and s^2 <= 1 - rho^2 gives the quartic term.
- Theorem R0: Lambda_f(l) T_hi(l) <= vartheta_0^{-l^2} 2^{-l^3}/l -> 0, and n^w_l/K_l -> infinity.

**Corollary `cor:exampleRecovered`.**
- Margins: mu_{1,m} >= q_0(7/9 - 1/2), mu >= q_0(1/2 - varpi) and mu >= q_0 r_l.
- (MS): sum Phi <= s^2/q_0^2.
- (b): mu^+ <= g_j/u_{2,1}(j) <= mu^- follows from b^+ >= 0 >= b^- on K_0.

**Remark `rem:lemmaZ`(c)** (construction of f' from (a', z')) is correct, including q^{**}(zhat') = a'(zhat') = 1.

## 6. Summary of required changes
1. Remark withoutSC(a): the condition for K^scr < infinity is unproved without Phi-regularity, and the F4 claim should be labelled a sketch.
2. Theorem R0: add eta_0 <= 2.
3. Abstract: add I finite, F finite and two-piece data, and say "active blocks".
4.-11. Notational clashes:
   - n_l;
   - c_1;
   - Y_m (and the stray V_m);
   - tau(N'');
   - Psi/Phi/beta/lambda/n in Theorem onesided;
   - K in (SC) and the constant K_0;
   - iota and vartheta_0;
   - sigma-labels, s(s), rho_k, m_j, the window N, kappa, c.
12. Remark onesided(b): replace the numerics attribution by the 2-line proof at g = c u_{2,1} (gamma^+ < Gamma_w = gamma^-).
13. Wording items (a)-(h).
14.-15. Overfull boxes and LaTeX cosmetics.
No theorem needs to be weakened, and no referee correction from S3/G3/R3 is missing.
