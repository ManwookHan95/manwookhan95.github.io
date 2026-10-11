# Referee report B on `paper3/martin_density_note_III.tex`

Scope: abstract (l.36-67), Section 1 (l.72-359), Section 4 "The operator T_fin and Master Theorem VI" (l.3174-4591),
Section 6 "Status and open problems" (l.6910-7040).  Line numbers refer to the current file (7093 lines).

Sources checked against (authoritative where they conflict with the paper): r10/Q1_notes.md, Q1_referee_a.md (+ refa_notes,
refa_part2), Q1_referee_b.md; r11/MTVI_graph.md, cert0_report.md, cert1_report.md, cert2_report.md, cert3_report.md;
r11/K1_notes.md 1.1 (Lemma K1.1) and K1_referee.md; r11/K2_notes/K2_referee (for the T^infty_fin base); BRIEFING_R2.md
ADDENDA 10-11; Part I (paper/final .aux numbering) and Part II (paper2/build .aux numbering) for every cross-reference cited in
Section 4.

## 0. Verdict

Section 4 is mathematically sound: every theorem, lemma and proposition in it is proved in the sources (Q1 with refa P1-P8 and refb
P-LIP/P-R/P-HOLD, the four certification clusters, K1.1).  All cross-references to [I] and [II] in Section 4 resolve to the intended
statements (checked against the .aux label tables), except one in the proof of Lemma partI (fix 18).  The arithmetic of Lemmas Wfin, GENfin,
interface, S2ctr and count, and of Theorems Afin, Ctr, MTVI, VI2 and Cor VI3, was re-derived (Section 3 below).

Required fixes fall into three groups:
 (A) Overclaims in the abstract, the introduction and the status section.  The two normalization options are conflated, so that
     "every N" and "the conclusion of Martin's Lemma B" are claimed for one operator.  The transport theorem is stated without
     its operator T^infty_fin.  The verification claims contradict each other.  Master Theorem VI is asserted for T^infty_fin without
     proof.  Two paraphrases of Section 5 overstate what is proved.
 (B) Statements in Section 4 that are false or unproved as written, although every conclusion survives after the fix:
     - Lemma CMtr(a): the ratios "of f^#" are not the realized ratios.
     - Lemma PM(iv): refa's precision P5 is not incorporated.
     - Lemma interface (W2) fails at stage 1.
     - The (W6) justification does not give the stated inequality.
     - The (U3) enumeration in Prop BR is incomplete.
     - The list in Lemma partI is incomplete, and one of its references is wrong.
     - The constant c_\flat (not c_flat) before Lemma CMtr is called numerical but is an f-constant.
 (C) An unresolved inconsistency between Remark later(a) (Section 6) and Lemma H1suff(i) (Section 5).

**Number of required fixes: 21** (Section 1 below).  Optional suggestions: Section 2.

## 1. Required fixes

### R1. Abstract, l.53-56: the options are conflated (Martin's Lemma B; "for every N").
Quote: "We then fix one operator $T_{\rm fin}$, independent of $N$, which satisfies the conclusion of Mart\'in's Lemma~B and can be
taken of norm less than one, and prove Master Theorem~VI: for the norms $p_N$ built with $T_{\rm fin}$, every first row with finite
base support is recoverable, for every $N\ge1$."
Problem 1: Martin's Lemma B gives a NORM-ONE injective operator (martin_paper_summary; [I, Def 1.3] (T-a) requires equality).
With norm c_1 < 1 (option (a)), T_fin does not satisfy the conclusion of Lemma B.  It satisfies it only under option (b)
(Theorem Afin(b)).
Problem 2: "for every N >= 1" holds only under option (a).  Under option (b) the case N >= 2, rho_1(f) = 1 is open (Theorem MTVI(b2),
Remark MTVIopen(b)).
Change to: "We then fix one operator $T_{\rm fin}$, independent of $N$, in two versions: with option~(a) it has norm $c_1<1$ and
satisfies all other conclusions of Mart\'in's Lemma~B, so that it defines Mart\'in-type norms; with option~(b) it has norm one and
satisfies the conclusion of Mart\'in's Lemma~B.  We prove Master Theorem~VI: with option~(a), for the norms $p_N$ built with
$T_{\rm fin}$, every first row with finite base support is recoverable, for every $N\ge1$ (with option~(b): for $N=1$, and for
$N\ge2$ at the rows with $\varrho_1(f)\ne1$)."

### R2. Abstract, l.57-58: the density equivalence also needs the option.
Quote: "Consequently, for $T_{\rm fin}$, density of $\NA((c_0,p_N),\ell_2^2)$ is equivalent to (LSC-trunc)$_N$."
Theorem VI2 holds for option (a) and every N, or for option (b) and N = 1 only.
Change to: "Consequently, for $T_{\rm fin}$ with option~(a) and every $N$ (with option~(b): for $N=1$), density of ... is equivalent
to (LSC-trunc)$_N$."

### R3. Abstract, l.58-66: the infinite-support results are stated without their operator.
Quote: "...cushion domination at deep-raised rows, and uniform solvability of the $d$-consistency system, and obtain a transport
theorem: (LSC-trunc)$_N$ holds at every triple $(f,g,\rho)$ that satisfies a joint push condition and an A-regularity condition at
infinitely many main stages."
Prop cushion, Theorem SysDC, Theorem transport and Prop residual are proved for the design T^infty_fin of Def designinf, which is T_fin
(option (a)) over the doubly exponential base mu*, with insertions.  They are not proved for T_fin.  As written, a reader combines the
transport theorem with the density criterion for T_fin, which is not justified.
Change: before "cushion domination" insert "for a variant $T^\infty_{\rm fin}$ of $T_{\rm fin}$ (option~(a), over the doubly
exponential base of Part~II, with finitely many additional design quantities per stage):".  In the last sentence of the abstract
the density statement may stay as it is.

### R4. Introduction, l.79-81: "of norm at most one" is not Martin's Lemma B, and it is not "admissible".
Quote: "an injective operator $T$ of norm at most one given by his Lemma~B, which rests on \cite[Proposition~2.8]{KLMW20}; we call such
an operator \emph{admissible} [I,~Definition~1.3]."
Martin's Lemma B gives norm one.  [I, Def 1.3](T-a) requires $q^*(Te_{n,m})\le1$ with equality for some $(n,m)$.  An operator of
norm at most one is not admissible in general.  This precision matters here, because option (a) is exactly the departure from the
equality clause.
Change "of norm at most one" to "of norm one", and after "[I,~Definition~1.3]" add "($q^*(Te_{n,m})\le1$ with equality for some
$(n,m)$, injectivity, $Y\cap c_{00}=\{0\}$, density of the normalized vectors in every block)".

### R5. Introduction l.186-192 and Section 4 l.3186-3192: "with four changes" understates the changes to Part II's design.
Quotes: "$T_{\rm fin}$ is the design of [II,~Definition~5.48] on the ladder of [II,~Definition~3.5] with four changes: ..." (l.187-189)
and "...on the ladder of [II,~Definition~3.5], with four changes: ..." (l.3187).
Remark Tfincomp(a) (l.3359-3370) lists further changes, and some of them are material:
 - B_mu is formed at the first element beyond s_max, not the third.
 - R is computed from lb_l, and p_0 is the least odd integer (the Part II rule for p_0 is dropped).
 - Cluster weights are generic.
 - (W_exp) is put into c^cl(p).
 - b(w) = min(b_II, b_QC).
 - Above all, Dbar(w)^3 is removed from Q(w) and the exponent of Q(w) contains l^2.
The last change is why Part II's class/cube count does not transfer, and why Lemma count and Remark count are needed (cert3 Section 5).
Change "with four changes:" to "with the changes listed in Remark~\ref{rem:III-Tfincomp}, chiefly:".  In both places add as a further
item: "the window factor $Q(w)$ does not contain Part~II's $\bar D(w)^3$ and has exponent $\omega(l)+l^2+20$".

### R6. Introduction l.194-197 and Section 6 l.6916-6918: "satisfies the conclusion(s) of Martin's Lemma B" (same issue as R1).
Quotes: "and $T_{\rm fin}$ satisfies the conclusions of Mart\'in's Lemma~B; with option (a) its norm is $c_1<1$, so the norms it
defines are Mart\'in-type norms, and with option (b) it is admissible" (l.194-197).  And: "which does not depend on $N$, satisfies the
conclusion of Mart\'in's Lemma~B and, with option (a), has norm $c_1<1$ (Theorem~\ref{thm:III-Afin}): for every $N\ge1$ every first
row ..." (l.6916-6920).
Change l.194-197 to: "and $T_{\rm fin}$ satisfies (T-b)--(T-d) of [I,~Definition~1.3]; with option (b) it is admissible and satisfies
the conclusion of Mart\'in's Lemma~B; with option (a) its norm is $c_1<1$ (the only departure from Lemma~B), so the norms it defines
are Mart\'in-type norms (Theorem~\ref{thm:III-Afin})."
Change Section 6 (1) to: "For the operator $T_{\rm fin}$ of Section~\ref{sec:III-design}, which does not depend on $N$, satisfies
(T-b)--(T-d) and, with option (b), the conclusion of Mart\'in's Lemma~B, while with option (a) it has norm $c_1<1$
(Theorem~\ref{thm:III-Afin}): with option (a), for every $N\ge1$ every first row ..."

### R7. Introduction, l.241-244: the paraphrase of the sharpness of the lowering transfer is wrong.
Quote: "the factor in the lowering transfer is sharp, and the loss is linear in the truncation radius
(Remark~\ref{rem:III-LTsharp}), so the truncation must be built into the approximant rather than performed afterwards."
What Remark LTsharp proves:
 - (a): the factor 2 in front of Lambda_M is sharp.
 - (b): the cushion loss Lambda_M(r,h) = (r/r_0) alpha(M) is linear in the SCALE r, hence not O(r^2) as r -> 0.
   Truncation is therefore free only at finitely many scales fixed before M.
No "truncation radius" occurs.
Change to: "the factor $2$ in the lowering transfer is sharp, and the cushion loss can be linear in the scale $r$ rather than
quadratic (Remark~\ref{rem:III-LTsharp}), so truncation is free only at finitely many scales fixed in advance and must be built into
the approximant rather than performed afterwards."

### R8. Introduction, l.263-277: the transport theorem and its consequence are stated without the operator.
Quote (l.264-266): "\emph{Transport theorem} (Theorem~\ref{thm:III-transport}).  Let $N\ge1$, $f\in S_{p_N^*}$ with finite or infinite
base support, ..."
Quote (l.274-277): "...for instance, every first row whose base support meets no signature set beyond $s_{\max}(L)$, for infinitely
many main stages $L$, is recoverable."
Theorem transport and Cor transport are proved for T^infty_fin only, whose p_N differ from those of T_fin.  The density criterion item
directly above uses the same symbol p_N for T_fin.
Change:
 - Begin the item with "Let the design be $T^\infty_{\rm fin}$, $N\ge1$, ...".
 - Replace "is recoverable" by "lies in $\Rec(p_N)$ for the norms $p_N$ built with $T^\infty_{\rm fin}$".
Also rephrase "an activity class with at least $n(w)/D_{\rm cl}(w)$ scales at which the push condition (H1$^*$) holds and Step~A is
A-regular (H2)".  As written, (H1*) and (H2) look like conditions on scales; they are conditions on (L,w,a).  Write: "an activity
class $a$ with at least $n(w)/D_{\rm cl}(w)$ scales such that the push condition (H1$^*$) holds and Step~A is A-regular (H2) at
$(L,w,a)$".

### R9. Introduction, l.298-300 (and Section 5): "c_1" has two meanings.
Quote: "$-\gamma_0<\gamma\le-c_1\nu_1/(8H(L))$, the coefficients of the carriers whose near coordinates are all thick carrying
$\ell_2$-mass at least $c_1/2$."
Earlier in the introduction (l.195), and throughout Section 4, c_1 is the weight of stage 1 (= ||T_fin|| under option (a)).  Here c_1 is the
Step-A constant c_1 := 1/(2 + CN|Lambda_A|^{1/2}/A_min) of Theorem Aobs (l.6224).  gamma_0 is not defined in the introduction either.
Change: rename the Step-A constant to $c_{\rm A}$ wherever it occurs:
 - introduction l.298, 300;
 - Section 5 l.6224, 6252, 6295, 6313-6325, 6802, 6810, 6836, 6851 (coordinate with the Section-5 referee).
In the introduction write "with the constant $\gamma_0=c_{\rm A}/(4\|h\|_2)$ of Definition~\ref{def:III-residual}".

### R10. Introduction, l.302-304: exact proportionality is claimed, but only approximate proportionality is proved.
Quote: "In the cases (A$^*$) and (U$^*$) the thick part of the base support at design depth is proportional to the carrier combination
of the certificate, with a robustly negative common factor."
Prop residual(i) gives only
   |a_s - Psi_y(s)/kappa_Psi| <= eps Des(L)/|kappa_Psi|   for s <= dbar(L) with |a_s| >= u/2,
where eps < 4u^3 Des(L)^{-C_A} is the size of the certificate and kappa_Psi <= -c_*/nu_1.
Change "is proportional to the carrier combination of the certificate" to "agrees, up to an error $\varepsilon\,\mathrm{Des}(L)/
|\varkappa_\Psi|$ ($\varepsilon$ the size of the certificate), with a fixed multiple $\Psi_y/\varkappa_\Psi$ of the carrier
combination of the certificate (Proposition~\ref{prop:III-residual}(i))".

### R11. The verification claims (l.315-324, l.3204-3206, l.4533-4539, l.4583-4587) overstate and contradict each other.
Quotes:
 (a) l.315-318: "The material of Sections~\ref{sec:III-generic}--\ref{sec:III-MTVI} was checked by two independent referees, and every
     result on which Master Theorem~VI rests that had been checked only once was re-derived in a second, independent verification".
 (b) l.3204-3206: "Every link of the argument has been checked in two independent verifications; the corrections found there are
     incorporated, and they are listed in Remark~\ref{rem:III-cert}."
 (c) l.4533-4535: "The argument of this section was checked by two independent referees, and every result on which it rests that had
     been checked only once was re-derived in a second, independent verification".
 (d) l.4583-4587: "Lemma~\ref{lem:III-nocube} was checked by one referee. ... that version was checked twice, so
     Theorem~\ref{thm:III-MTVI} does not depend on Lemma~\ref{lem:III-nocube}."
Facts (MTVI_graph Sections 0-3, 7; cert0-cert3; K1_referee):
 - Sections 2-3 come from X1/X2 (Round 9, ONE referee each).  The Round-10 combination (Q1) had two referees.  The certification
   re-derived the once-checked links on the tree of MT VI.
 - Results checked by one referee only: Prop J (X2-ref only; not on the tree, not re-derived); Lemma noB and Cor noB (= K1.S,
   K1-ref only); Lemma nocube (= K1.1, K1-ref only).
 - The proof of MT VI as written uses Lemma nocube:
   - Lemma count(c): "by Lemma~\ref{lem:III-nocube} a class set needs no further pigeonhole";
   - proof of Thm Ctr: "with the pieces of Lemma~\ref{lem:III-nocube}".
   So (b) contradicts (d).
 - The corrections made in the certification were each derived and checked by one certifier:
   - Lemma window (cert0 F1);
   - Lemma interface and Prop transfer, which cert3 Sections 1-2 wrote out for the first time (MTVI_graph I-1, I-5: before that the
     transfer was asserted "by inspection");
   - the s-free coefficients (cert1 P-SFAR);
   - the gap criterion, the |F(0)| bound and the Bregman bound (cert2 C2-5, C2-4, C2-9).
   Only the count correction (A) has two checks (refa P8, cert3 5.3).
Change:
 - (b): replace the first sentence by "The verification status of the argument is recorded in Remark~\ref{rem:III-cert}."
 - (a) and (c): rewrite as "The results of Sections~2 and~3 on which Master Theorem~VI rests were checked by one referee each and then
   re-derived in a second, independent verification organized in four clusters (...); the combination in this section was checked by
   two referees and re-derived in the same verification.  The corrections introduced in the second verification (the common pull
   window, the transfer interface of Lemma~\ref{lem:III-interface} and Proposition~\ref{prop:III-transfer}, the $s$-free coefficients,
   the gap criterion of Lemma~\ref{lem:III-dcons}(a), the bounds of Lemmas~\ref{lem:III-DC} and~\ref{lem:III-UE1}(g)) were each made
   and checked once.  Proposition~\ref{prop:III-J}, Lemma~\ref{lem:III-noB}, Corollary~\ref{cor:III-noB} and
   Lemma~\ref{lem:III-nocube} were checked by one referee."
 - (d): write "The proof given here uses Lemma~\ref{lem:III-nocube}.  Without it ... and the count of Remark~\ref{rem:III-count}(A),
   which is only sketched here; that version was verified twice in the sources (the count by refa P8 and cert3; the order class,
   Step~A, cube, Step~B by refa P2 and cert0), so MT VI does not depend on Lemma~\ref{lem:III-nocube}."
 - Make l.322-324 consistent with this.

### R12. Section 4 opening, l.3177-3184: the option is missing.
Quote: "We define a single operator $T_{\rm fin}$, independent of the number $N$ of blocks, and prove that for the norms $p_N$ built
with it every first row with finite base support is recoverable, for every $N$ (Theorem~\ref{thm:III-MTVI}).  By the reduction of
[I,~Section~1] and [II,~Proposition~6.48] the density of $\NA((c_0,p_N),\ell_2^2)$ is then \emph{equivalent} to ..."
Change: after "for every $N$" insert "when $T_{\rm fin}$ is taken with option~(a) of Definition~\ref{def:III-Tfindata} (with
option~(b): for $N=1$, and for $N\ge2$ at the rows with $\varrho_1(f)\ne1$)".  After "\emph{equivalent}" insert "(option~(a), every
$N$; option~(b), $N=1$)".

### R13. Lemma CMtr(a), l.3851-3855 and proof l.3910-3911: the ratios "of f^#" are not the realized ratios.
Quote: "\item[(a)] \textup{(Exactness.)}  The active ratios of $f^\#$ lie in $Z_\kappa$; every robust rate object is $\ge u/4$ there;
the $\ell_1$-Hoffman constant of the cone $\Gamma^\#(\kappa,a)$ at these ratios is ..."
Proof quote: "(a) is Proposition~\ref{prop:III-KNtr}(a) (with the robust bound $u/4$), and Step~B does not change the active values".
Problem: a ratio is r_l = u_l(zhat)/kappa_m.  Step B leaves the active values unchanged, but it moves kappa_m by up to C_f c_{L+1}.
The paper's own proof of (b) says so (l.3927: "and $\varkappa$ moves by $\le C_fc_{L+1}$").  So the active ratios of f^# are the
realized ratios r'' of Step A, rescaled block by block by kappa'_m/kappa^#_m.  Invariance of Z_kappa under such a rescaling is
proved only for blocks of kind (U) (Lemma Uscale(a), where the Delta'_m-column is deleted).  For a (T)-block, the row (X4^0)
contains m^2|r_l| K(sigma_rob, R_a(r)^2), which is not homogeneous in the block's ratios, and no invariance is proved for (T)- or
(KN)-blocks.  So "the active ratios of f^# lie in Z_kappa" is not proved.  It is also not what is used.  Prop KNtr(a) gives, and the proof of (c) item (iii), Lemma nocube and the true shift Delta'' = Delta' kappa'/kappa^#
use, exactness at the realized ratios r''.  Q1 CM^tr(a) says correctly "the active ratios at the end of Step A lie on Z_kappa".
Change (a) to: "The realized active ratios $r''$ (the active ratios of $f^{(1a)}$, i.e.\ $u_l(\zh^\#)/\varkappa'_m$ with the block
scalars $\varkappa'_m$ of $f^{(1a)}$) lie in $Z_\kappa$; every robust rate object is $\ge u/4$ at $r''$; the $\ell_1$-Hoffman constant
of $\Gamma^\#(\kappa,a)$ at $r''$ is ...".
In the proof, after "does not change the active values" add: "; the change of the block scalars in Step~B is carried by the true
shift $\Delta''_m=\Delta'_m\varkappa'_m/\varkappa^\#_m$ in (c)".

### R14. Lemma PM(iv), l.4127-4130: refa precision P5 is not incorporated; the clause as written is false.
Quote: "for every lever parameter $P$ with $|P|_\infty\le r$ \textup{(}not only at $P^*$\textup{)} no carrier of $\Omega^\#$ and no
coarse peak of $f^\#$ changes status; the lever moves change the values only of carriers outside $\Omega^\#$ that meet lever
coordinates, and these are fine."
Problem: the levers exist to move the values of the carriers of Omega^#.  Along the cube those values move by up to
delta_1 + C_lev r (Lemma DC), and they end exactly at nv^# at P* (part (i)).  In addition, every value moves at second order through
the Hilbert normalization.  The proof of (iv) itself says "the carriers of $\Omega^\#$ move by at most the moves bounded there".
refa required this rephrasing (Q1_refa_part2 C5(iv), precision P5): "the levers do move Omega values ...; coarse PEAKS meet no
lever coordinate and move only at second order ...; the only first-order side effects are on fine carriers".
Change the second clause to: "along the cube the carriers of $\Omega^\#$ move by at most $\delta_1+C_{\rm lev}r$ and reach
$\mathrm{nv}^\#$ at $P^*$; coarse peaks of $f^\#$ meet no lever coordinate and move only at second order, by less than their margins;
among the carriers outside $\Omega^\#$, only fine carriers (stages $>L$, total weight $\le c_{L+1}/3$) meet lever coordinates."

### R15. Lemma interface (W2), l.3641: the statement is false at stage 1.
Quote: "\item[(W2)] $\Phi_k\le c_k\le(\delta_kH_k)^2$ for every stage $k$."
At stage 1, (S4) sets c^max_1 := 1 (option (a); c_1 in [1/2,1)) or c_1 := 1 (option (b)), and (W3) is not imposed.  But
S_1 = {6,10,14,...}, H_1 = 2^{-6}/(1-2^{-4}) = 1/60 and delta_1 = delta^max_1 = min{1/2, (4(5/4)H_1)^{-1}} = 1/2.
So (delta_1 H_1)^2 = 1/14400 < 1/2 <= c_1.  The proof's "At PRE and MAIN stages by (W3) of [II]" does not apply at the main stage 1.
Change "for every stage $k$" to "for every stage $k\ge2$", and in the proof "At PRE and MAIN stages $k\ge2$".  (W2) is used only for
fine carriers k > L >= l_f (Lemma CMtr(e); [II, Lemmas 5.60, 5.62]), so nothing else changes.

### R16. Lemma interface, proof of (W6), l.3701-3705: the stated justification does not give the stated inequality.
Quote: "The chain of [II,~Lemma~5.61(ii)], $n(p'-1)\ge\mathrm{Des}(p'-1)\ge(B_\mu(p'-1)D(p'-1))^6\ge(\eta_k\lambda_k)^{-6}$ for the
first stage $p'$ after the absorber sequence, survives the factor $2^{13}$, because $\sigma(p'-1)>p_0$ gives $B_\mu(p'-1)\ge
2^{p_0}/\mu_{p_0}^2\ge2^{11}/\mu_{p_0}^2$ and $D\ge1/\Phi_k$."
Problem: the two quoted bounds give only
   B_mu D >= 2^{11}/(mu_{p_0}^2 Phi_k),
while eta_k >= mu_{p_0}^2 c_k^2/2^{13} and lambda_k >= Phi_k give only
   (eta_k lambda_k)^{-1} <= 2^{13}/(mu_{p_0}^2 c_k^2 Phi_k).
The factor 1/c_k^2 (c_k <= 1, in fact tiny) is not covered.  The same gap is in U1-ref 7 and in cert3 W6(ii).
Corrected argument:
 - sigma(p'-1) > s_max(p'-1) >= p_R(k) = p_0 + 2R(k) > R(k).
 - The definition of R(k) gives 2^{R(k)} >= 32/(mu_{p_0}^2 lb_k^2) >= 2^{11}/(mu_{p_0}^2 c_k^2), since lb_k >= c_k/8.
 - Hence, with 1/mu_sigma^2 >= 16, B_mu(p'-1) = 2^{sigma}/mu_sigma^2 >= 2^{15}/(mu_{p_0}^2 c_k^2).
 - Therefore B_mu(p'-1) D(p'-1) >= 2^{15}/(mu_{p_0}^2 c_k^2 Phi_k) >= 4 (eta_k lambda_k)^{-1}.
Replace the "because ..." clause by this argument.  Optionally add that [II, Lemma 5.61(ii)] needs only
n(p'-1) >= log_2(4C_f/(T_lo eta_k lambda_k)), so the margin is enormous.

### R17. Proposition BR, proof of (U3), l.4047-4050: the list of supports created in Step A is incomplete.
Quote: "The coordinates of $E:=F^\#\setminus F$ are created in Step~A (tuning banks and pulls of active carriers and of held carriers,
peak-push banks, lever moves in blocks of kind (KN)); Step~B creates none, and no absorber coordinate is a support coordinate."
Step 4 of Prop KNtr (l.1556-1560) also makes "the individual inward pushes by $\eta'$" of the inactive near-threshold carriers in
blocks of kind (KN) and (U).  These are realized by pulls in the common window (cert0 F1: "all pulls of the joint fixed point
(actives, holds, peak pushes, lever and D2 pushes realized by pulls)").  They create support coordinates whose (U3) bound is not
verified in the text.
Change:
 - Add "inward pushes of the inactive near-threshold carriers in blocks of kind (KN) and (U)" to the list.
 - After the sentence on held carriers add: "The same argument applies at the pulls of these inward pushes.  The pushed carriers are
   inactive in the class ($\gamma_l=0$, Lemma~\ref{lem:III-LV}(b)), so the data there are the residue $\le C_fc_{L+1}$, while the pull
   mass is $\ge24\lambda_lc_{L+1}$."

### R18. Lemma partI, l.3600-3607 and its proof l.3616-3619: the list is incomplete and one reference is wrong.
Quote: "...in particular for $T_{\rm fin}$ under both options: Propositions~1.9--1.13, Lemmas~1.5--1.7 and~1.16, the results of
Section~7 used in Section~\ref{sec:III-UE} (7.13--7.17, Theorem~7.18 and the lemmas used in its proof), and Lemmas~8.8 and~8.10."
Proof quote: "...and in the resonance example of [I, Section~8]".
Problem (i): results of [I] that the paper uses for an operator of norm c_1 < 1 but that are not on the list:
 - on the tree of MT VI:
   - [I, Def 3.1, Lemmas 3.2, 3.3, 3.4(c),(d), 3.6(a)], in Lemma masses and in the proofs of Theorems UE and Eeng;
   - [I, (16)] = eq:peakshift, i.e. Lemma 8.27, in Lemma floorrow (l.942) and in the proof of Lemma CMtr (l.3967).
 - in Section 5, where T^infty_fin is also option (a): [I, Lemmas 1.6, 7.1(b), 8.7(a), 8.26, 8.27, 8.28] and [I, (15)].
cert3 Section 7 read lem:base, lem:block, lem:slack, prop:expansion and the Section-7 lemmas.  It did not read lem:budget (8.7),
lem:split (8.26), lem:peakshift (8.27) or lem:flip (8.28).
Problem (ii): the resonance example is in [I, Section 6] (Lemmas lem:T and lem:firstrow, Theorem 6.6), revisited in [I, Corollary 7.23].
[I, Section 8] is the designed operator.
Change:
 - Add "Definition~3.1, Lemmas~3.2--3.4 and~3.6, Lemma~8.27 (equation (16))" to the list (covered by cert3 Section 7 and by the
   operator-free proof of Lemma 8.27 from Lemma 8.8).
 - Add a sentence covering the [I]-results used only in Section 5 (Lemmas 1.6, 7.1, 8.7, 8.26, 8.28, equation (15)), after checking
   that their proofs use $T$ only through (T-b)--(T-d) and $q^*(Te_{k,m})\le1$.
 - Replace "the resonance example of [I, Section~8]" by "the resonance example of [I, Section~6] and [I, Corollary~7.23]".

### R19. Section 6, Remark twodesigns, l.7001-7008: an unproved claim (MT VI for T^infty_fin) is reported as established, with a
wrong description of its support.
Quote: "Remark~\ref{rem:III-infdep} states that Master Theorem~VI, and hence the density criterion, also hold for
$T^\infty_{\rm fin}$.  This rests on the monotonicity of the window conditions under the insertions (Lemma~\ref{lem:III-designinf}(d))
and on the fact that the window theorems use the base only through the design factor; this transfer between the two bases is argued
in Remark~\ref{rem:III-infdep} and was not part of the four-cluster verification of Section~\ref{sec:III-MTVI}."
Problems:
 (i) Remark infdep (l.6900-6903: "Theorem~\ref{thm:III-MTVI} holds for $T^\infty_{\rm fin}$ as well, because its proof uses the design
     only through conditions that are monotone under the insertions") argues only monotonicity under (I1)-(I5).  It does not address
     the change of base mu -> mu*.
 (ii) The base enters the proof of MT VI outside the window theorems:
     - (B3) of Lemma interface (computed with B_mu at the first element beyond s_max);
     - (W2) at cluster stages (via B_mu^6 >= 2^{12 sigma^2});
     - (W6) (mu_{p_0}, the rule for R, and the chain of R16);
     - the mu-base tuning lemma behind Prop transfer (cert3 Section 4: "the only refereed source of Lemma TU / bank efficiency for
       T_fin's base").
     For mu*, Part II's [II, Lemma 4.15] is available, but it is formed with B* at the third element, while T_fin's Des uses the first.
     None of this was written out for mu*.
 (iii) So "MT VI holds for T^infty_fin" is a theorem-level claim without proof, stated as fact in a remark that does not say it is a
     sketch.  This is contrary to the convention announced at l.357-359.
Change Remark twodesigns to: "Whether Master Theorem~VI, and hence the density criterion, hold for $T^\infty_{\rm fin}$ is not proved
here.  The monotonicity argument of Remark~\ref{rem:III-infdep} covers the insertions (I1)--(I5).  It does not cover the change of base
from $\mu$ to $\mu^\star$, which enters the proof of Theorem~\ref{thm:III-MTVI} through (B3), (W2), (W6) of
Lemma~\ref{lem:III-interface} and the tuning lemma behind Proposition~\ref{prop:III-transfer}, all verified for $\mu$ only.  We expect
the transfer, since each item has a $\mu^\star$-analogue with $B_{\mu^\star}$, but it has not been written out or verified."
For coordination with the Section-5 referee:
 - Remark infdep must label its sentence on MT VI for T^infty_fin "(sketch, not verified)" and make its final sentence conditional
   on it.
 - Theorem transport itself uses the route-V companion and the window count of Section 4 for T^infty_fin (Remark infdep,
   l.6896-6900), i.e. the same unwritten transfer to mu* (K1/K2 assumed it: K1_notes 1.0 "Every window theorem uses the base only
   through B_mu*").  Say so in the verification paragraph l.325-327.

### R20. Section 6, Remark later(a), l.7015-7025, versus Lemma H1suff(i) (Section 5): a stated lemma is left contradicted.
Quote: "By [I,~Lemma~8.27] the data of an active weak peak $k$ have sign $\epsilon_k=\mathrm{vs}_k\sgn(e_k-\Delta'_m)$ with $e_k\ge0$;
the formula $\epsilon_k=-\sgn(\Delta''_m)\mathrm{vs}_k$ ... can fail at a weak peak when $\Delta'_m>0$ and $e_k>\Delta'_m$. ... the
private resource ``near bank with $\Delta''_m>0$'' in Lemma~\ref{lem:III-H1suff}(i) should then be read with the correct sign of the
data."
The sign formula follows from the refereed [I, Lemma 8.27]: -varsigma_k Delta Theta(k) = Delta d M + e_k, with the sign convention
fixed by the robust case e_k ~ 0.  A near bank raises eps_k val_k.  It therefore pushes the weak peak inward iff eps_k = -vs_k, i.e.
iff e_k < Delta'_m.  When 0 < Delta'_m < e_k, a near bank with Delta''_m > 0 pushes OUTWARD.  Hence:
 - Lemma H1suff(i) (l.6640-6642: "a near bank with $\Delta''_m>0$") is false as stated in that sub-case;
 - the motivating text l.6611-6613 ("the peak carries data of sign $\epsilon_k=-\sgn(\Delta''_m)\mathrm{vs}_k$, so a near bank ...
   performs the push only if $\Delta''_m>0$") is wrong at weak peaks.
A remark labelled "not verified and not used" cannot leave a stated lemma in this state.  The rule is: nothing found wrong appears as
proved.
Change (coordinate with the Section-5 referee):
 - In Lemma H1suff(i) and in the discussion l.6611-6613, replace "near bank (of a peak) with $\Delta''_m>0$" by "near bank of a weak
   peak $k$ whose data sign is $\epsilon_k=-\mathrm{vs}_k$ (by [I,~Lemma~8.27], $\epsilon_k=\mathrm{vs}_k\sgn(e_k-\Delta'_m)$, so this
   holds iff $e_k<\Delta'_m$)".  The proof of H1suff(i) is unchanged.
 - In Definition H1 (l.6619) the list only enumerates admissible moves, and (H1*) requires the end statuses, so the definition stays
   correct.  Make the same rewording there for consistency.
 - Corollary transport uses only private far pulls and is unaffected; say so.
 - Shorten Remark later(a) to a pointer to this corrected formulation.

### R21. Standing notation before Lemma CMtr, l.3825-3826: the constant c_\flat is called "numerical", but it is an f-constant.
Quote: "where $c_\flat\in(0,1]$ is a numerical constant such that the gaps produced in blocks of kind (KN) and (U) by
Proposition~\ref{prop:III-KNtr}(b) are $\ge c_\flat\eta'M_m$."
For blocks of kind (KN), Prop KNtr(b) refers to [II, Prop 5.56(b)] with eta' in place of eta(w).  That result gives
"every inactive near-threshold $\Omega$-carrier is a strict non-peak with gap $\ge c_f\eta(w)M$" (Part II l.7121-7123), with c_f an
f-constant.  No numerical constant works in general.  Q1 2.2 also writes "gaps >= c_f eta' M".
Change "is a numerical constant" to "is a constant depending only on $f$ (the minimum of the numerical constant for the inward pushes
in (U)-blocks and the $f$-constant $c_f$ of [II,~Proposition~5.56(b)] for the inactive near-threshold carriers of (KN)-blocks)".
Nothing else changes:
 - in Lemma S2ctr(i), $c_\flat\eta'\ge c_\flat T^5\ge T^6$ holds for $T\le c_\flat$, i.e. for $L\ge l_f$;
 - in Lemma PM(iii), $C_fc_\flat^{-2}$ is again an $f$-constant.

## 2. Optional suggestions

O1. Lemma S2ctr(i), proof l.4221.  "Finally $x_0=c_fg_{\min}\Phi_{\min}(L)$ and $\Phi_{\min}(L)\ge1/\mathrm{Des}(L)\ge T$" gives only
    $x_0\ge c_fT^{5\mathrm{Des}+3}$.  To obtain the stated $x_0\ge T^{5\mathrm{Des}+3}$, use the intermediate bound
    $g_{\min}\ge\frac18T^{5\mathrm{Des}+1}$ and $T\le c_f/8$.
O2. Remark routeX, l.3781-3786.  The precise failing comparison is cert3 Section 8: $e_1<2^{-R}$ needs
    $|\text{residue}(s)|\lesssim\nu2^{8p_0}c_{L+1}^2/T_{\rm hi}$, while the residue contains the true-shift correction, of size up to
    $C_f\mathrm{Des}\,c_{L+1}$.  "Not small compared with $c_{L+1}$" understates the gap.  State the comparison.
O3. Notation $D(L)$.  It is used in (QC3), in Lemma interface (W6) ("$\lambda_l\ge1/D(l)$") and in Lemma CMtr.  Section 5 (l.5176)
    calls it "the design quantity of [II, Subsection 5.6]", but Part II has no symbol $D(L)$; it has $D_{\rm room}(l)$.  The proof of
    Lemma Wfin(f) verifies (QC3) through $D_{\rm room}$.  Define $D(l):=D_{\rm room}(l)$ once in (S5), or say which quantity is meant.
O4. Introduction, l.280-282: "and for every other admissible operator".  $T_{\rm fin}$ with option (a) and $T^\infty_{\rm fin}$ are not
    admissible.  Write "and for every admissible operator, in particular for the operators of Mart\'in's Lemma~B".
O5. Remark count(A).
    - Add the bound $P(L)\le\mathrm{Des}(L)^{1/2}$ (cert3 5.1(c)), which is used in $D_{\rm cls}\le B^{1+N(2C+3)}$.
    - Note that $(2L+1)9^L\le B$ because $\mathrm{Des}\ge2^{6L^3}$.
    - Label (A) as a sketch whose details are in the sources (refa notes 2.7, cert3 5.3).
    - The same remark shows that Lemma count(a) can be sharpened to $D_{\rm cl}(w)\le B$.
O6. Proposition transfer.  [II, Lemma 4.1] (lem:II-scales) is used: parts (c), (d), (e) are invoked through (D1), (B3), (S2) and in
    item (iii) of the proof.  List it with (B3, S2, D1).
O7. Abstract, l.50-52: "per-piece bounds have radius proportional to the scale with window-independent constants".
    $c_{\rm flat}=\min(c^f_{\rm flat},\gamma_B/(8\rho A_2))$ is window independent only for fixed $\gamma_B$; in the application
    $\gamma_B=\gamma(w)\to0$ (handled by Theorem Eeng).  Add "for fixed $\gamma_B$".
O8. Section 6.
    - Item (4): add "at a clean sub-window and a class with at least $n(w)/D_{\rm cl}(w)$ scales", and "(checked by one referee)".
    - Problem Astar: "together with a positive answer to Problem~\ref{prob:III-Wstar}".
    - Item (3) "Tools valid beyond $T_{\rm fin}$": Prop KNtr needs the QC requirements of a design; say "for every design satisfying
      the QC requirements".
O9. Remark Tfincomp(b), "zero sets and tiny labels agree".  The row scalings are $\le1$.  So scheme-tiny implies cone-tiny, and
    scheme-robust ($\ge u$) implies cone-robust $\ge u/2$ (the minors involve at most $R_\Gamma(L)$ scaled rows and
    $(1-2^{1+L-9\cdot2^L})^{R_\Gamma(L)}\ge\frac12$).  Say this instead of "agree".
O10. Introduction, l.354-356: "Constants written $C_f$ depend on the first row (and on the mate where said)".  Sections 2 and 4 let them
    depend on $N$ as well (l.457-458; $l_f=l_f(f,N,g,\rho)$); add "and on $N$".
O11. Proof of Theorem VI2, l.4486-4487: "($\Cset(f')$ is closed)" is not needed.  $\dist<\varepsilon$ already provides $g'$.
O12. Introduction, l.327-335 (statements of earlier drafts found false): add "levers for tuned zero-value absorbers (an earlier
    Lemma LV(d))", which Remarks routedecision and abs explain.
O13. Proof of MT VI, Step 2 (option (b), $N\ge2$): add that once $b(w)<|\varrho_1(f)-1|$, cleanness gives
    $|\varrho_1(f)-1|\ge u(w)$, so stage 1 is a robust carrier at $w(L)$.

## 3. What was checked and found correct (no change needed)

- Definitions Tfindata, Tfinrounds, Tfinstage against Q1 1.1-1.3.  Incorporated: P7 (patterns over the blocks of stages <= l), P8
  (here: Q(w) exponent with l^2 and the class-only count), P-LIP and P-LIP+ (Lip* in b_II and in (QC4)), P-R, P-SFAR (s-free
  alpha_{l''}), (W_exp) only in c^cl(p), R from lb_l, generic weights in [(1-2^{-l})c^max_l, c^max_l].
- Lemma GENfin(a),(b).  Agrees with Lemma GEN's hypotheses (k_0 contains all u_l(j) and alpha_l; k = k_0(Phi_l, l notin N_T)).
- Lemma Wfin(a)-(f), each item re-derived:
  - order of a stage; k(l + R_cl(l)) known at stage l;
  - the excluded (GM) set has measure <= delta^max/8;
  - lambda_l <= c_l/4 and sum_{l>L} lambda_l <= c_{L+1}/3;
  - c_{L+1} <= b(L,M(L))^2 <= b(w)^2 <= T_lo(w)^8;
  - T_lo decreases along sub-windows, which gives (W_exp) at every sub-window;
  - lb_l bounds; the cluster lower bound via prod(1-2^{-(L+j)}) >= 1/2;
  - (QC1)-(QC5) and (D-lev).
- Theorem Afin.  Re-derived:
  - allowedness of PRE and cluster absorber targets (s <= l_r < l via (c+));
  - the injectivity estimate with the factor 8/9;
  - (T-d) once p > 1 + max supp y + 2|supp y|, with q*(u_l - y) <= (8/3) delta (1+||U||) H;
  - n_l in [3/4, 5/4];
  - attainment at (1,2).
  Statement (b)/(c) correctly separates the options.
- Lemma partI.  Content agrees with cert3 Section 7, apart from R18.
- Lemma interface, re-derived:
  - (B3): all three inequalities from Des^{1/6} >= 2 B_mu/delta_min;
  - (W2) at p+1 and at p+i, i >= 2 (8n >= 2(p+i) + 4 + 6*2^{p+i} via B_mu^6 >= 2^{12 sigma^2});
  - (W6) least entry 4*2^{-R}/q*(x) >= mu^2 c^2/2^{13} (R >= 2, q*(x) <= 8);
  - (S2); (D2) band disjointness; (A1) (p_0 > max T(l-1) >= s, so no other absorber of the cluster meets s).
  Apart from R15, R16.
- Proposition transfer.  Every number [II, x.y] cited in Section 4 resolves to the intended Part II label (build/*.aux): 2.9 kappa,
  2.10 kappader, 2.11 cor:Rkt, 2.12 cost, 2.22 cert, 2.23 shift, 2.30 VT, 3.5 Tfinal, 3.6/3.7 constants/rates, 3.10 W, 3.12 lemmaB,
  3.14 subwindows, 3.16 bank, 3.18/3.19/3.20 clean, 3.22 GW, 4.7 donorpeak, 4.14 bankformula, 4.15 TU, 4.16 companionw,
  4.17-4.19 donorraise/compcost/status, 4.24 transplant, 5.1 hoffman, 5.3 loj, 5.7 thm:B, 5.14 subset, 5.46 prop:Rkt, 5.48 DU1,
  5.50 firsttouch, 5.51 zerovalue, 5.52 Gamma, 5.53 classes, 5.54 ray, 5.56 KN, 5.57 compclass, 5.58 trueshift, 5.59 absorb,
  5.60 recursion, 5.61 domfine, 5.62 SCi, 5.63 schauder, 5.64 coststat, 5.68 MTIV, 5.70 notMTIV, 6.48 LSC.  The interface items named
  per result match cert3's table.  Every [I, x.y] cited in Sections 1 and 4 resolves correctly (final/*.aux), except the "Section 8"
  of R18.
- Remark routeX.  Agrees with cert3 Section 8 (off tree; not used).
- Lemma CMtr, re-derived:
  - (b): Step B drift (released far parts <= 4c^2 since 2^{-s_far} <= c^2; clamp equation; Lemma drift; gap >= M mu/4 >= mu/8 >=
    g_min; robust and (KN)/(U) margins move by <= C_f Des b^2 << c_\flat b/8 <= g_min);
  - the kind-[3] display and the + side gap(f) <= Mb <= M mu/8 <= 1.5 gap^# (cert0 C6);
  - (f) cost: Des^3 eta' log(1/eta') <= C_f T^3 log(1/T) since Des^2 T <= Des^{-18};
  - Step A = Prop KNtr with exact holds of ALL non-active nearly-neutral carriers (P-HOLD) and the common window (cert0 F1).
- Proposition BR, re-derived:
  - (U3) at held pulls (t C_f c <= K_3 24 lambda c);
  - (U6): j(l) <= second element; v_l(second) >= 1/Des by (D-lev); the window of ratio 2^{6G(L)} holds >= 6 elements of S_l
    while Step A uses <= 5; r >= s_1 T^4 >> c_{L+1} >= 2^{-s_far/2}, so lever pulls lie below s_far;
  - c_flat >= c_f u.
- Lemma PM(i)-(iii).  Clamp equation; rho = |nv| C/(Phi^2(1-C)); gap criterion of cert2 C2-5, with b <= 8 g_min/c_\flat and
  C_f b^2 <= C^# g_min/4; rho_d(f') <= 1 - mu/8.
- Lemma S2ctr, re-derived:
  - eta'/3 >= T^5 from 1/T >= 2^{n} >= 3n^2 >= 3L Des;
  - mu >= Des^{-1}(eta'/3)^{Des} >= T^{5 Des + 1};
  - g_min >= T^{5Des+2} >= 2^{-6 log_2^2(1/T)};
  - natural-log bounds 9 log^2 and 11 log^2;
  - (W-b);
  - order of choices C_0 (absolute) -> T_* -> l_f, with no circularity.
- Lemma nocube.  Matches K1.1 (K1-ref: correct); items (1)-(6) as in K1_notes 1.1.
- Lemma count.  (a)-(c) re-derived: K_data <= B^{C_*(2L+2)+C_K+2}, C_1 = 2C_* + C_K + 6, n(w) >= L 2^{L^3} B^{omega+L^2+20},
  K_data T_hi <= 2^{-L^3}/L.  Remark count agrees with cert3 5.2-5.5 (Q1's original count wrong as written; fixes A and B).
- Theorem Ctr.  (E-c)-(E-f) checked against Theorem Eeng (l.2645-2673): K_j T_j -> 0; n'_j c_flat/K_j -> infinity;
  theta_j = C_f T' log(1/T') + e^{-1/(3T')} T'^{-2}; theta_j/c_flat^2 <= C_f theta_j log_2^2(1/T') -> 0.
- Theorem MTVI.  Step 1 pigeonhole over omega(L)+1 disjoint bands; option (b): stage 1 = (1,2) is absent from p_1, and
  b(w) <= 2^{-4L^3} < |rho_1(f) - 1|; the quantifier order matches refa 2.9.
- Theorem VI2 and Cor VI3: [I, Lemma 1.16], [I, Props 1.10(c), 1.12, 1.13], [I, Remark 1.4, Lemma 1.5] (|R_m x|_m <= m 2^{-m} q(x)).
- Remark cert, lists (1)-(5).  Every fix of refa (P1-P8), refb (P-LIP, P-R, P-HOLD, alpha-mass), cert0 (F1, C1-C7), cert1 (P-LIP+,
  P-SFAR, P-CY), cert2 (C2-1, C2-2, C2-4, C2-5, C2-9; the others are Section-3 precisions) and cert3 (F1-F6) appears in the text,
  except refa P5 (R14).
- Section 6.  Problems LSC, optb, other and B, and Remarks MTVIopen and evidence, are consistent with Section 4 and make no
  overclaim, apart from R6, R19 and R20.
