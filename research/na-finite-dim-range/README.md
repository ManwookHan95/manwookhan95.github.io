# Density of NA(X, Y) for finite-dimensional Y on "complicated" domains

Question: for X a Lipschitz-free space F(M), Lip_0(M), a free Banach lattice FBL[E], a tensor product or a direct sum,
and Y finite-dimensional, is NA(X, Y) always dense in L(X, Y)?

Working notes (one explorer + one adversarial referee per class; AI-written and AI-refereed, not human-verified;
citations checked only through search snippets because arxiv.org was not reachable):
- `sums_tensors_notes.md`, `sums_tensors_referee.md`
- `lipfree_notes.md`, `lipfree_referee.md`
- `lipzero_notes.md`, `lipzero_referee.md`
- `fbl_notes.md`, `fbl_referee.md`

Verdicts (P(X) means: NA(X, Y) is dense for every finite-dimensional Y):
- Polyhedral finite-dimensional Y: always dense for every X (Lindenstrauss, property beta).
- Direct sums and tensor products: "always dense" is EQUIVALENT to the Johnson-Wolfe question (every finite-dimensional
  space has property B). Density passes from l_1-sums to summands and back (T1), to every absolute or lattice summand
  (T2), and from L_1(mu, X) to X (Theorem 10); X (x)_pi l_1^n = l_1^n(X), X (x)_eps l_oo^n = l_oo^n(X), etc.
- F(M): OPEN. New: P(F(M)) for C^1 simple closed curves and arcs (e.g. the circle; F(T) fails property A), wedges.
- Lip_0(M): OPEN. New: weak*-closed finite-codimensional subspaces of L_oo(mu) are locally lineable (Theorem 3.9),
  hence P(Lip_0(G)) for connected metric graphs with finite first Betti number; C(K, E) for finite-dimensional E.
- FBL[E]: OPEN for dim E = infinity. New: for dim E < infinity, norm-attaining finite-rank operators are dense in
  K(FBL[E], Y) for every Y (Theorem 5.2), while FBL[E] fails property A when dim E >= 2.
No counterexample is known in any class; one would answer the Johnson-Wolfe question negatively.
