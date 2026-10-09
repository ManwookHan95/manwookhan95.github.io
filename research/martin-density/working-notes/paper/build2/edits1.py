base='/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/paper/build2/'
s=open(base+'edited.tex').read()
def rep(old,new):
    global s
    assert s.count(old)==1, ('NOTFOUND or multiple', old[:80])
    s=s.replace(old,new)
# rem:blocks first sentence
rep(r"""By \cite[Remark~6.9]{PrB} (Mart\'in tails), if the set
$\NA((c_0,p_N),F)$ is dense in $\mathcal L((c_0,p_N),F)$ for arbitrarily
large $N$, then
$\NA((c_0,p),F)$ is dense for Mart\'in's $p$ ($I=\N$): one has
$p=p_N+s_N$ with $s_N\le\eta_N\,q\le\eta_Np_N$, $\eta_N\to0$, and the
lift lemma of \cite{PrB} applies.  Hence finite block sets suffice for the
density problem.""",
r"""By Lemma~\ref{lem:martintail} below (Mart\'in tails; cf.\
\cite[Remark~6.9]{PrB}), if $\NA((c_0,p_N),\mathcal F)$ is dense in
$\mathcal L((c_0,p_N),\mathcal F)$ for infinitely many $N$, then
$\NA((c_0,p),\mathcal F)$ is dense for Mart\'in's $p$ ($I=\N$).  Hence
finite block sets suffice for the density problem.""")
rep(r"""Sections~\ref{sec:second}
and~\ref{sec:resonance} assume that $I$ is finite.
\end{remark}""",
r"""Sections~\ref{sec:second}--\ref{sec:designed} assume that $I$ is finite.
\end{remark}

\begin{lemma}[Mart\'in tails]\label{lem:martintail}
Fix an admissible $T$, let $p$ be the norm with $I=\N$ and $p_N$ the norm
with $I=\{1,\dots,N\}$, and let $\mathcal F$ be a Banach space.  If
$\NA((c_0,p_N),\mathcal F)$ is dense in $\mathcal L((c_0,p_N),\mathcal F)$
for infinitely many $N$, then $\NA((c_0,p),\mathcal F)$ is dense in
$\mathcal L((c_0,p),\mathcal F)$.
\end{lemma}

\begin{proof}
Put $s_N(x):=\sum_{m>N}|R_mx|_m$, so that $p=p_N+s_N$.  Since
$|R_mx|_m\le\|R_mx\|_1\le m2^{-m}q(x)$, we have $s_N\le\eta_Nq\le\eta_Np_N$
with $\eta_N:=\sum_{m>N}m2^{-m}=(N+2)2^{-N}$, hence $\|A\|_p\le\|A\|_{p_N}\le
(1+\eta_N)\|A\|_p$ for operators $A$.  Let $S\in\NA((c_0,p_N),\mathcal F)$
with $\|S\|_{p_N}=1=\|Sx_0\|$, $p_N(x_0)=1$.  Let $J$ be a norm-one
functional on $(\bigoplus_{m>N}V_m)_{\ell_1}$ norming $(R_mx_0)_{m>N}$
($J:=0$ if this vector is $0$), and $\varphi(x):=J((R_mx)_{m>N})$; then
$\varphi\in X^*$, $|\varphi|\le s_N$ and $\varphi(x_0)=s_N(x_0)$.  Put
$S'x:=Sx+\varphi(x)Sx_0$.  Then $\|S'x\|\le p_N(x)+s_N(x)=p(x)$ and
$\|S'x_0\|=1+s_N(x_0)=p(x_0)$, so $S'\in\NA((c_0,p),\mathcal F)$, and
$\|S'-S\|_p\le\sup_x|\varphi(x)|/p(x)\le\eta_N$.  Given $A\ne0$ and
$\varepsilon>0$, density for $p_N$ gives such an $S$ with
$\|S-A/\|A\|_{p_N}\|_{p_N}<\varepsilon$; then $\|A\|_{p_N}S'$ attains its
$p$-norm and $\|\,\|A\|_{p_N}S'-A\|_p\le(1+\eta_N)\|A\|_p(\eta_N+
\varepsilon)$.  Let $\varepsilon\to0$ and $N\to\infty$ along the given
$N$.
\end{proof}""")
# rem:transfer (c)
rep(r"""(c) \emph{Sketch, not used.}  Running the same estimates at $\xi$ instead
of $x'_N$ should give
$\limsup_{t\to0}(p^*(f+tg)^2-1)/t^2\le\Gamma_w(g)$ for every balanced finite
certificate when $a\in c_{00}$; we have not written out the details and do
not use this.""",
r"""(c) For every balanced finite certificate $g$ at $f$ with $a\in c_{00}$,
$\limsup_{t\to0}2(p^*(f+tg)-1)/t^2\le\Gamma_w(g)$; this is proved in
Proposition~\ref{prop:onesidedupper}, by running the rebalancing at $\xi$
instead of $x'_N$, and Theorem~\ref{thm:onesided} identifies the exact
one-sided coefficients at \textup{(BT)} points.""")
# rem:kinks (a)
rep(r"""Whether a finite certificate with $\Gamma_2\le1<\Gamma_w$ exists at a
support with infinitely many contacts in Mart\'in's space is \emph{open};
Theorem~\ref{thm:transfer} would not recover it.""",
r"""Whether a finite certificate with $\Gamma_2\le1<\Gamma_w$ exists at a
support with infinitely many contacts in Mart\'in's space is \emph{open}.
Theorem~\ref{thm:transfer} would not recover it, but
Corollary~\ref{cor:BTrecovered} does whenever $f$ satisfies \textup{(BT)}:
by Theorem~\ref{thm:onesided} the exact one-sided coefficients are the
minima $\gamma^\pm$ of $\Gamma_w$ over side-admissible decompositions, which
re-split through contacts with the cheap sign, and the proof of the lower
bound there needs no decoupling.""")
# rem:twopiece (b),(c)
rep(r"""Conversely, every mate is
supported in $\{1\}\cup K_0$ with $g_j/u_{2,1}(j)$ bounded on $K_0$; this
is proved in the companion notes, is not proved here, and is not used.""",
r"""Conversely, every mate is
supported in $\{1\}\cup K_0$ with $g_j/u_{2,1}(j)$ bounded on $K_0$
(Corollary~\ref{cor:exampleRecovered}(b)).""")
rep(r"""(c) Since $K_0$ is infinite, $f$ is not C-tame, and
Theorem~\ref{thm:tamefibre} does not apply at $f$; the infinite contact set
is unavoidable (Proposition~\ref{prop:exact}).""",
r"""(c) Since $K_0$ is infinite, $f$ is not C-tame, and
Theorem~\ref{thm:tamefibre} does not apply at $f$; the infinite contact set
is unavoidable (Proposition~\ref{prop:exact}).  But $f$ satisfies the
block-tameness condition \textup{(BT)} of Section~\ref{sec:engineered},
which allows infinite contact sets (Corollary~\ref{cor:exampleRecovered}).""")
# paragraph after nonrecovery
rep(r"""a recovery of the switching mates must use norm-attaining approximants whose
certificate spans grow, for instance by putting base mass on the contact
windows (Remark~\ref{rem:engineered}).""",
r"""a recovery of the switching mates must use norm-attaining approximants whose
certificate spans grow, for instance by putting base mass on the contact
windows.  This is done in Section~\ref{sec:engineered}
(Remark~\ref{rem:engineered}).""")
# theorem defect sentence? keep. Replace rem:engineered
i=s.index(r"\begin{remark}[Engineered approximants; results of companion notes]\label{rem:engineered}")
j=s.index(r"\end{remark}",i)+len(r"\end{remark}")
s=s[:i]+r"""\begin{remark}[Engineered approximants]\label{rem:engineered}
Proposition~\ref{prop:approximants} shows that, outside a finite window
containing $\supp a'_n$, the base coordinates $z'_n$ of a norm-attaining
approximant are free.  Section~\ref{sec:engineered} uses this freedom:
engineered approximants put masses on finitely many contacts and truncate
$z$ far out, and transfer peaks rebalance levels between the base and the
blocks.  It is proved there that every mate of the first row $f$ of
Theorem~\ref{thm:defect} is recovered (Corollary~\ref{cor:exampleRecovered});
more generally every \textup{(BT)} point lies in $\Rec$
(Corollary~\ref{cor:BTrecovered}), and two-piece mates are recovered at
every $f$ with finite base support under the conditions of
Theorem~\ref{thm:engineered}.  Thus the defect of Theorem~\ref{thm:defect}
is a defect of the intrinsic mechanisms only, and
Proposition~\ref{prop:nonrecovery} is a statement about the canonical
truncations, not about recoverability.
\end{remark}"""+s[j:]
open(base+'edited.tex','w').write(s)
print('ok')
