base='/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/paper/'
s=open(base+'build2/edited.tex').read()
i=s.index(r"\section{Status of the density problem}\label{sec:status}")
j=s.index(r"\begin{thebibliography}")
s=s[:i]+open(base+'newparts/S.tex').read()+s[j:]
a=s.index(r"\begin{abstract}"); b=s.index(r"\end{abstract}")
newabs=r"""\begin{abstract}
For Mart\'in's renormings $p$ of $c_0$ (canonical base, finitely or
infinitely many blocks) we study the density of norm-attaining operators
into $\ell_2^2$ through the mate fibres
$\Cset(f)=\{g:\ (f,g)\text{ is contractive}\}$.  Density is equivalent to the
statement that every pair $(f,\rho g)$ with $g\in\Cset(f)$ and $\rho<1$ is a
limit of norm-attaining pairs, and we reduce this to lower limits of the
fibres along norm-attaining approximants; finitely many blocks suffice.  We
introduce finite certificates with coordinatewise radii, prove that the
closed set they generate is transported along \emph{every} sequence
$f_n\to f$, and prove an averaging theorem over scales which covers weighted
directions, locally split mates and cross mates carried by off-peak
coordinates with non-summable gaps.  At tame supports we identify the sharp
second-order invariant, the mass-weighted coefficient $\Gamma_w$, and
realize it along canonical truncations by means of transfer peaks.  We then
construct an admissible operator $T$ and a non-attaining first row at which
all intrinsically recoverable mates lie on one line while $\Cset(f)$ spans an
infinite-dimensional space (the resonance obstruction); the canonical
truncations do not recover these mates.

This is a defect of the intrinsic mechanisms only.  Rebalancing through
transfer peaks at first order makes \emph{engineered} norm-attaining
approximants work without any steering: every mate with one-sided linear
decompositions of weighted coefficient at most one and non-negative
$d$-mismatch is recovered, for arbitrary contact sets and any number of
blocks, and the case of negative mismatch is reduced to a scrambling
condition.  By Fenchel duality we compute the exact one-sided second-order
coefficients at block-tame first rows, and deduce that every block-tame
first row is recoverable, whatever its contact set; in particular every mate
of the resonant example is recovered.  Finally we design an admissible
operator (private signatures, coarse-to-fine targets, a super-fast ladder
of weights) for which every first row with finite base support and
signature room is recoverable, and for which density is equivalent to a
single approximation statement, Lemma~Z.  The density problem itself
remains open; we formulate precisely what remains.
"""
s=s[:a]+newabs+s[b:]
open(base+'build2/edited.tex','w').write(s)
print('ok')
