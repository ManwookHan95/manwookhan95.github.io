# Q2 notes (round 10) -- (LSC-trunc) for Martin's norm p_N with a designed T

Task: for f in S_{p_N*} with INFINITE base support, g in C(f), rho < 1, eps > 0, find f' with FINITE base support, p_N*(f' - f) < eps and
dist(rho g, C(f')) < eps.  With task Q1 (finite-F Lemma Z for T_fin, Master Theorem VI, Theorem VI.2) this is equivalent to density of
NA((c_0, p_N), l_2^2), and for infinitely many N it gives density for Martin's p (Corollary VI.3, lem:martintail).
Design: T_fin^* := T_fin (ADDENDUM 9 / Q1 Section 1, option (a)) over the doubly exponential diagonal base mu*_s = 2^{-2^{2^s}} (U2 1.1,
U2-ref (s1)), with the new rate objects of Sections 3-4 added to omega(L).  Every window theorem is base-independent (U2 Remark after 1.1;
U4 Lemma GW).  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Parts: Q2_part1.md ... Q2_part4.md; scripts and outputs: Q2_work/.

VERDICT.  (LSC-trunc) is NOT proved for every f.  Proved: (i) truncation of the base support is free at the level of decompositions at
finitely many scales (Lemma LT); (ii) finite base support of the approximant is free in the violation-tolerant route at ARBITRARY F, so
(f, rho g) in cl NA -- in particular (LSC-trunc) at (f, g, rho) -- follows from window families with SIDE CUSHION DOMINATION (U3^inf) at base
rows of arbitrary support (Theorems UE^inf, E^{eng,RT,inf}); (iii) lem:finitebase is not needed (Lemma 3.1); (iv) the exact one-sided
structure of the degenerate lever configuration (Lemma 3.4); (v) the degenerate configuration does not obstruct exact d-consistency once
one block-norm lever is added, except on a codimension-two set (Proposition 4.1, Corollary 4.2, Lemma 4.3).  The remaining step is a
line-by-line transport of Q1's per-window construction to an infinite-F, deep-raised base row (Section 5.3).

| # | statement | status | where |
|---|-----------|--------|-------|
| 1 | Lemma 1.1 (contact truncations: elementary facts) | PROVED | 1.1 |
| 2 | Lemma LT (lowering transfer; truncation mass cancels; partial-lowering form) | PROVED | 1.2 |
| 3 | Corollary 1.2 (window-local truncation at finitely many scales) | PROVED | 1.3 |
| 4 | Exact local data at the approximant are unavoidable | HEURISTIC | 1.4 |
| 5 | Lemma M2^inf (uniform neighborhoods at arbitrary F) | PROVED | 2.1 |
| 6 | Theorem UE^inf (engineered bound at base rows of arbitrary support, (U3^inf)) | PROVED (modification of refereed X2 Thm UE) | 2.4 |
| 7 | Theorem E^{eng,RT,inf} (cl NA along norm-attaining, finite-support approximants) | PROVED (modification of X2 E^eng + V3 E_RT) | 2.5 |
| 8 | Lemma 3.1 (V1 TR(i) without lem:finitebase, A_0 = 10) | PROVED | 3.1 |
| 9 | Proposition 3.2 (cushion domination of transplanted data at a deep-raised companion) | SKETCH | 3.2 |
| 10 | Lemma 3.4 (exact drift identity in the (ND)-failure configuration) and consequences | PROVED | 3.4 |
| 11 | Proposition 4.1 (block-norm bordering: explicit right inverse uniform in the Sherman-Morrison denominator) | PROVED | 4.1 |
| 12 | Corollary 4.2 (Lemma DC^inf: exact d-consistency with thick S-mass levers) | PROVED (modification of X2 Lemma DC) | 4.2 |
| 13 | Lemma 4.3 (structure of exact full degeneracy at infinite F; peaks keep off-support levers) | PROVED | 4.3 |
| 14 | Theorem 5.1 (transport: (LSC-trunc) at every lever-regular row) | SKETCH | 5.1 |
| 15 | Corollary 5.2 (rows whose support avoids the lever coordinates) | SKETCH | 5.2 |
| 16 | (LSC-trunc) for every f with infinite base support | OPEN | 5.3 |

## 0. Setting
Notation of paper/martin_density_note.tex (Sections 1, 2, 7, 8).  p = p_N = q + ||L .||_V, q*(A) = ||A||_1 + ||U* A||; a first row f in S_{p*}
has forced data (xi, q_0, a, w, F, z, zhat, e, nu): f = a + L* w, F = supp a, z = sgn a on F, |z| <= 1, e = U* a/nu, nu = ||U* a||,
zhat = z + U e, xi = q_0 zhat, w = J_V(L^** xi).  Diagonal base U k_s = mu_s e_s (mu decreasing).  s(t) := sqrt(1 + t^2);
C(f) := {g : p*(f + t g) <= s(t) for all t}.  s_j := sgn a_j (j in F); alpha(M) := sum_{j > M} |a_j|; a_{>M} := a 1_{(M, inf)}.
Dual ball (lem:dualball): p*(h) = min { max(q*(A), ||W||_{V*}) : h = A + L* W }.
Equivalences (recalled, PROVED earlier): Z5 Proposition 5.4 / Q1 Theorem VI.2: given finite-F Lemma Z (Q1 Corollary VI.1), (LSC-trunc)
for every (f, g, rho) <=> density.  Per mate: if (f, rho' g) in cl NA for all rho' < 1 then (LSC-trunc) holds at (f, g, rho) (norm-attaining
rows have finite base support, prop:smooth(c)); conversely (LSC-trunc) at (f, g, rho) with finite-F Lemma Z gives (f, rho g) in cl NA
(transitivity, thm:transitivity).

## 1. Truncation

### 1.1 Contact truncations; Lemma 1.1.  PROVED.
For M with a 1_{[1,M]} != 0 let c_M := q*(a 1_{[1,M]}), a^M := a 1_{[1,M]}/c_M, and f^M the first row with forced data (a^M, z) (admissible:
z = sgn a^M on supp a^M).  The coordinates j in F, j > M, become CONTACTS of f^M of sign s_j; z is unchanged.
 (a) |1 - c_M| <= alpha(M) + ||U* a_{>M}||.  (b) ||e^M - e|| <= 2||U* a_{>M}||/nu and zhat^M - zhat = U(e^M - e).
 (c) f^M -> f and all forced data converge (prop:continuity).  (d) ||U* a_{>M}|| <= mu_{M+1} alpha(M).
Proof.  (a) 1 = ||a 1_{[1,M]}||_1 + alpha(M) + ||U* a||, c_M = ||a 1_{[1,M]}||_1 + ||U* a 1_{[1,M]}||, and the two Hilbert norms differ by at most
||U* a_{>M}||.  (b) ||x/||x|| - y/||y|| || <= 2||x - y||/||y|| with x = U* a 1_{[1,M]}, y = U* a; zhat^M - zhat = U(e^M - e) as z is fixed.
(c) prop:approximants (ii) => (i) (valid for every F, Z5 Lemma 2.1(b)): a^M -> a in l_1 by (a).  (d) sum_{j > M} mu_j^2 a_j^2 <= mu_{M+1}^2
alpha(M)^2.  QED

### 1.2 Lemma LT (lowering transfer).  PROVED.
Let h in X*, r != 0, f + r h = A + L* W with q*(A) <= pi, ||W||_{V*} <= pi.  Put B := (A - a)/r and
      Lambda_M(r, B) := sum_{j in F, j > M} min( |a_j| , (-s_j r B_j)_+ )    (<= alpha(M) and <= |r| ||B 1_{(M,inf)}||_1).
Then  p*(f^M + r h) <= pi + 2 Lambda_M(r, B) + 2||U* a_{>M}|| + p*(L*(w^M - w)).
Proof.  f^M + r h = A' + L* W + L*(w^M - w) with A' := A + a^M - a = a^M + r B, so by lem:dualball and the triangle inequality it suffices to
prove q*(A') <= q*(A) + 2 Lambda_M + 2||U* a_{>M}||.  With a_{<=M} := a 1_{[1,M]}, A' = (a_{<=M} + rB) + (1/c_M - 1) a_{<=M}, hence
q*(A') <= q*(a_{<=M} + rB) + |1 - c_M|.  l_1 part: coordinates j <= M and j notin F of a_{<=M} + rB and of A agree.  For j in F, j > M, with
alpha := |a_j|, x := r B_j, y := (-s_j x)_+ the identity |s_j alpha + x| - |x| = alpha - 2 min(alpha, y) (cases s_j x >= 0; 0 < y <= alpha;
y > alpha) gives |x| = |A_j| - |a_j| + 2 min(|a_j|, y).  Summing: ||a_{<=M} + rB||_1 = ||A||_1 - alpha(M) + 2 Lambda_M.  Hilbert part:
||U*(a_{<=M} + rB)|| = ||U*(A - a_{>M})|| <= ||U* A|| + ||U* a_{>M}||.  With Lemma 1.1(a):
q*(A') <= q*(A) - alpha(M) + 2Lambda_M + ||U* a_{>M}|| + alpha(M) + ||U* a_{>M}||.  QED
Remarks.  (1) The l_1-mass alpha(M) cancels (as the raise mass in V3's raise transfer, Lemma 2.3).  What remains: the cushion loss Lambda_M
(anti-sign usage of the decomposition on the far support, capped at the cushion), the Hilbert footprint 2||U* a_{>M}|| <= 2mu_{M+1} alpha(M),
and the normer change p*(L*(w^M - w)) <= C'_f eps_e log(e/eps_e), eps_e := ||U|| ||e^M - e|| (V3 Lemma 2.2: its proof uses only the clamp
formula at zhat, zhat^M).  (2) Partial-lowering form (same proof): for Delta a supported in F with s_j Delta a_j <= 0, |Delta a_j| <= |a_j|, and
f^low the row with data ((a + Delta a)/q*(a + Delta a), z), with y_j := (-s_j r B_j)_+, alpha'_j := |a_j + Delta a_j|, the identity
|s alpha' + x| - |s alpha + x| = -|Delta a_j| + 2 min(|Delta a_j|, (y_j - alpha'_j)_+) gives
      p*(f^low + r h) <= pi + 2 sum_j min(|Delta a_j|, (y_j - alpha'_j)_+) + 2||U* Delta a|| + p*(L*(w^low - w)):
only usage BEYOND THE NEW CUSHION is lost.

### 1.3 Corollary 1.2 (window-local truncation).  PROVED.
Let S be a finite set of nonzero reals and f + r h_r = (a + r B_r) + L*(w + r Theta_r) with max(q*(.), ||.||) <= pi_r (r in S).  For every
eta > 0 there is M_0 with p*(f^M + r h_r) <= pi_r + eta r^2 + eps''_M for all M >= M_0 and r in S, eps''_M := 2||U* a_{>M}|| + p*(L*(w^M - w)).
Proof.  Lambda_M(r, B_r) <= |r| ||B_r 1_{(M,inf)}||_1 -> 0 for each of the finitely many r (B_r in l_1).  QED
So the far support is never an obstruction for decompositions at finitely many scales chosen BEFORE the truncation point.

### 1.4 Exact local data at the approximant (HEURISTIC; explains the architecture)
For f' near f with p*(f' - f) = d > 0, scales |r| >> sqrt(d/(1 - rho^2)) are covered by the slack of rho g; for |r| << sqrt(d) the inequality
p*(f' + r g') <= s(r) is a statement about the second-order structure of p* at f' alone.  The normer change w' - w is nonzero for every f' != f
(Lemma 1.1(b)), so statuses and levels of deep carriers at f' differ from those at f at arbitrarily small scales; g' must carry exact local
data at f'.  Hence (LSC-trunc) inherits the exactification problem, and the useful reduction is Section 2.  (Numerics, Q2_work/lt_check.py:
(LT) never violated, max LHS - RHS = -8e-9; cushion loss 1e-3..1e-2 versus the naive p*(f^M - f) = 1e-2..6e-2; normer change 1e-12..1e-14.)

## 2. Finite base support is free in the violation-tolerant route

References: X2 = r9/X2_notes.md with X2-ref precisions (p-UE1)-(p-UE7), (c3'), (p-E1), (p-W); V3 = r7/V3_notes.md (Lemma 2.3 RT,
Corollary 2.4, Theorem 2.5 E_RT); Y3 = r6/Y3_notes.md (Theorem 2.1).

### 2.1 Lemma M2^inf.  PROVED.
Fix at f (F arbitrary) in every block gamma_m in (M_m/2, M_m) with |w_m(k)| != gamma_m for all k, transfer data (gamma_m, k^vs_{*,m},
Lambda^vs_m) for eta_1 in (0, 1/4] (lem:transferdata), and a peak k^nat_m with alpha_m(k^nat_m) != 0.  There is r_f(eta_1) > 0 such that every
f'' with p*(f'' - f) <= r_f(eta_1) satisfies X2 Lemma M2 (a) without its clause "F subset supp a'', |a''_j| >= a_min/2 on F", and M2 (b).
Proof.  X2's compactness argument: if it failed for every r there would be f_n -> f violating it; prop:continuity (valid for every F: a_n -> a
in l_1, scalar data converge, w_{n,m} -> w_m coordinatewise, D_m w_{n,m} -> D_m w_m) and lem:persistence (whose proof uses only prop:continuity,
the threshold lemma and dominated convergence in the blocks) contradict this.  The removed clause is the only reference to F.  QED

### 2.2 Window families at a base row of arbitrary support (definition)
Fix rho in (0,1), eta_0 in (0,2] with rho^2(1 + eta_0) <= (1 + rho^2)/2, constants A_0, A_2 >= 1, gamma_B in (0,1], C_+ >= 1, and
delta := (1 - rho^2(1 + eta_0/2))/2.  A BASE ROW is f_0 in S_{p*} with forced data (xi_0, q_0^0, a_0, w^0, F_0, z_0, zhat_0, e_0, nu_0), F_0
arbitrary, p*(f_0 - f) <= r_f/2.  A WINDOW FAMILY at f_0 is as in X2 3.1 (pieces i = 1..n at scales t_i in [T, t_1], pairs (b^+-_i, omega^+-_i)
representing g_i at f_0 with g_i(xi_0) = 0, a common finite set Omega of strict non-peaks) satisfying X2's (U1), (U2), (U4)-(U7) (with
(p-UE1)-(p-UE7), (c3')) and, instead of (U3):
 (U3^inf) SIDE CUSHION DOMINATION: for every i and j in F_0, (s_j b^+_i(j))_- <= C_+ |a_0(j)|/t_i and (s_j b^-_i(j))_+ <= C_+ |a_0(j)|/t_i.
(Contact-like data on F_0 satisfy it with any C_+; X2's alternative "t_i |b^+-_i(j)| <= |a_0(j)|" gives C_+ = 1.  Nothing is required of
the sign-direction usage or of b^theta.)  In (U6), (SEP)(i) reads "disjoint from F_0 except for (S-mass) levers".

### 2.3 The construction (X2 3.2 with three changes)
Order: f -> f-constants -> window family at f_0 -> s_1 -> N_w -> N'' -> levers.
 (i^inf) N_w is chosen AFTER s_1 with tail_W := max_i (||b^+-_i 1_{(N_w,inf)}||_1 + ||v_i 1_{(N_w,inf)}||_1) <= min{T^3, delta s_1/(64 rho),
   K T^2/K_w}, alpha_0(N_w) := sum_{j > N_w} |a_0(j)| <= theta T^2/(1 + ||U||), ||U* a_0 1_{(N_w,inf)}|| <= s_1 T^4.  The pre-row uses
   a_0 1_{[1,N_w]}: f_1 := (a_0 1_{[1,N_w]} + masses, z_0 1_{[1,N'']}) normalized by q*.  F_0 cap (N_w, N''] become contacts of sign s_j.
 (ii^inf) masses: X2's W together with W_F := {j in F_0 cap [1, N_w] : |a_0(j)| < 8 rho s_1 max_i |b^theta_i(j)|}, where a_0(j) is RAISED
   (same sign) to modulus 8 rho s_1 max_i |b^theta_i(j)| (Y3 Theorem 2.1's raised support).
 (iii)-(vi) as in X2 3.2 with beta^theta := b^theta 1_{[1,N_w]}, beta^+- := b^+- 1_{[1,N_w]} +- (1/2) v 1_{(N_w,inf)}.
The resulting f' is norm attaining: a' is supported in a finite set and z' = 0 beyond N'' (prop:smooth(c)).

### 2.4 Theorem UE^inf.  PROVED (line-by-line modification of X2's refereed Theorem UE; modifications listed in full).
Let f be arbitrary, f_0 a base row, and a window family (U1), (U2), (U3^inf), (U4)-(U7) at f_0.  Define c^f_flat by X2 Step 0' with (c1)
replaced by (c1^inf) rho c_flat C_+ <= 1/8 ((c2)-(c7), (c3') unchanged), c_flat := min(c^f_flat, gamma_B/(8 rho A_2)).  Under X2's window
conditions (W-a), (W-b) (with (p-UE6)), (VT'), (LATE) (with (p-UE5)) and N_w as in (i^inf), the engineered approximant f' is norm attaining,
      p*(f' - f_0) <= K_w Pi log(e/Pi) + 2(1 + ||U||) alpha_0(N_w),  Pi := Pi_X + Pi_tr + r + t(N'')^{1/2},  Pi_tr := 2||U* a_0 1_{(N_w,inf)}||/nu_0,
and for every piece i:  p*(f' + tau g'_i) <= 1 + (tau^2/2)(1 - delta) for 0 < |tau| <= c_flat t_i,  p*(g'_i - rho g_i) <= K_w(K_w s_1 + c_fine + tail_W)/t_i.
Proof (X2's Steps 0'-5 and Lemma UE-1 verbatim except):
 (M1) Lemma M2^inf replaces M2; the removed clause was used only in (c1), replaced by (c1^inf).
 (M2) Lemma UE-1(a)-(c), (g) with Pi enlarged by Pi_tr: truncating a_0 beyond N_w moves e by <= Pi_tr (Lemma 1.1(b)) and z nowhere, so every
      carrier value moves by <= Pi_tr more (u(Uh) = <U* u, h>, ||U* u_k|| <= 1) and the block scalars by K_w Pi_tr more (UE-1(c) uses only value
      changes); normalization changes no value (e is scale invariant).  W_F masses are same-sign raises on F_0: by X2 Lemma M1(iv)
      ||e_A - e|| <= 2||U*(A - a)||/nu, so they enter Pi_X through 2||U* X_F||/nu_0, ||U* X_F|| <= 8 rho s_1 mu_1 n A_0/T.  In p*(f' - f_0) the
      truncation adds q*(a_0 1_{(N_w,inf)}) <= (1 + ||U||) alpha_0(N_w), twice (normalization included).
 (M3) Step 3, new coordinate classes (others verbatim):
   (2^inf) j in F_0 cap [1, N_w]: A''_j := a_0(j) or its raised value, |a'_j| >= |A''_j|/2 (q* <= 2 at late stages).  theta-piece (|tau| <= s_1):
     |tau rho beta^theta_j| <= s_1 rho |b^theta_j| <= |A''_j|/8 (definition of W_F).  +- pieces (s_1 < |tau| <= c_flat t_i, sgn tau the side):
     the anti-sign part of tau rho beta^+-_j is <= rho c_flat t_i C_+ |a_0(j)|/t_i <= |A''_j|/8 <= |a'_j|/4 by (U3^inf), (c1^inf).  Since
     a'_j + tau B^diamond_j = (1 - tau rho c_i) a'_j + tau rho beta^diamond_j with |tau rho c_i| <= 1/2 (UE-1(g), (LATE)), the sign of a'_j
     is kept: summand 0 of Exc'.  [Replaces X2's (2) "F: no flip by (c1)".]
   (2'^inf) j in F_0 cap (N_w, N''] (contacts of sign s_j): beta^theta_j = 0, beta^+-_j = +-(1/2) v_j, summand of Exc' <= rho|tau||v_j|; total
     <= rho|tau| tail_W <= delta s_1 |tau|/64 <= delta tau^2/64 for |tau| > s_1, and 0 for |tau| <= s_1 (a TOLERATED violation).
   (2''^inf) j in F_0 beyond N'': inside X2's cut-off term (1/2) rho |tau| V_{>N''}.
   Hence Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} + 2 rho |tau| eps + rho |tau| tail_W.
 (M4) Step 5: X2 ends with rho^2(1 + eta_0/2) + delta/8 + delta/8 + delta/8 + delta/4 + delta/8 = 1 - delta - delta/4; adding delta/32 keeps
      it <= 1 - delta.
 (M5) Steps 1, 2, 4 and UE-1(d)-(f) verbatim (they use the base only through q*(B^diamond) <= 2(1 + ||U||) rho A_0/t_i + |c_i|, the base form
      (f) -- whose proof uses ||beta^diamond - b^diamond||_1 <= tail_W -- and Lemma M1 with e computed at the truncated pre-row).  QED

### 2.5 Theorem E^{eng,RT,inf}.  PROVED (X2 Theorem E^eng with UE^inf and V3 Theorem 2.5's accounting).
Let f in S_{p*} (F arbitrary), g in C(f), rho, eta_0, delta as in 2.2.  Suppose base rows f_j (arbitrary support), p*(f_j - f) -> 0, lambda_j >= 1,
lambda_j -> 1, eps'_j >= 0, windows S_j = {T_j 2^{1-i} : 1 <= i <= n_j} carrying window families at f_j with fixed A_0, A_2, gamma_B, C_+ and
 (a)   p*(f_j + r rho g) <= 1 + (s(lambda_j rho r) - 1)/lambda_j + eps'_j for all r;
 (E-c) p*(g - g_{j,t}) <= K_j t (t in S_j);  (E-d) K_j T_j -> 0, n_j c_flat/K_j -> infinity;  (E-e') eps'_j <= theta_j (T_j 2^{-n_j})^2, theta_j -> 0;
 (E-f) the window conditions of 2.4 at f_j, 64 rho eps^viol_j <= delta s_late(j), (p-E1) K_w c_fine <= K_j T_j^2 4^{-n_j}.
Then (f, rho g) in cl NA((c_0, p_N), l_2^2) along norm-attaining rows f'_j with FINITE base support; in particular (LSC-trunc) holds at (f, g, rho).
Proof.  X2's proof with Theorem UE^inf, s_1 := s_late(j) (keeping (VT')), N_w by (i^inf) with theta := theta_j, and the bound
 (B')  p*(f'_j + r g'_{j,i}) <= p*(f_j + r rho g) + p*(f'_j - f_j) + |r| p*(g'_{j,i} - rho g)
                            <= s(rho r) + (lambda_j - 1) min(lambda_j^2 rho^2 r^2/2, 1) + eps''_j + 2 rho |r| K_j t_i,
 eps''_j := eps'_j + K_w Pi log(e/Pi) + 2(1 + ||U||) alpha_0(N_w) <= 2 theta'_j (T_j 2^{-n_j})^2, theta'_j -> 0, using V3 Corollary 2.4
 ((s(lambda x) - 1)/lambda <= s(x) - 1 + (lambda - 1) min(lambda^2 x^2/2, 1)).  In X2's case analysis (B) enters only as "s(rho r) + eps' +
 2 rho |r| K t_i"; the extra term is <= (1 - rho^2) r^2/48 (|r| <= 1) and <= (1 - rho^2) r_0 |r|/48 (|r| > r_0) once (lambda_j - 1)(1 + lambda_j^2)
 <= (1 - rho^2) r_0^2/48, absorbed by X2's margins (1 - rho^2) r^2/6, (1 - rho^2) r_0 |r|/3.  So gbar_j := (1/n_j) sum_i g'_{j,i} is in C(f'_j),
 (f'_j, gbar_j) attains its norm (prop:reduction(d)), and ||(f'_j, gbar_j) - (f, rho g)|| <= p*(f_j - f) + eps''_j + 4 K_j T_j/n_j -> 0.  QED
Remarks.  (1) lambda_j = 1, eps'_j = p*(f_j - f): X2's E^eng at arbitrary F.  (2) Raised base rows (V3 Lemma 2.3) satisfy (a) with
eps'_j = 2||U* Delta a_j|| + p*(L*(w^{(j)} - w)); lowered rows (Lemma LT) with lambda_j = 1, eps'_j = 2 max_r Lambda(r) + eps''_M.
(3) The far support of an infinite-F base row becomes contacts inside the engineered approximant; its two-sided use by the side data is a
violation of mass tail_W <= delta s_1/(64 rho).  (4) Consequently (LSC-trunc) at (f, g, rho) follows from the EXISTENCE of window families with
(U1), (U2), (U3^inf), (U4)-(U7) at base rows f_j satisfying (a), (E-c)-(E-f).  Producing them is the infinite-F exactification problem.

## 3. Producing cushion-dominated window families at infinite F

### 3.0 Inventory: where the finite-F production (Q1 Master Theorem VI: U1 companions, X1 KN^tr, X2 CM'/DC/LV, V1 TR) uses |F| < infinity
 (alpha) no flip on F via a_min = min_F |a_j| (X2 M2, UE (c1); V1 TR): REMOVED by Section 2 ((U3^inf) suffices).
 (beta)  lem:finitebase in V1 TR(i): REMOVED by Lemma 3.1.
 (gamma) flips on F (copied base data B_+- 1_F use the support beyond its cushion): Proposition 3.2 (SKETCH).
 (delta) levers (z-moves, banks, pulls at coordinates of S_l beyond s_max) assumed OFF the support: at infinite F they may lie in F;
         replacements (L1)-(L4) (3.3) and Section 4.
 (eps)   new rate objects (moduli |a_s| at design depth, spreads, Sherman-Morrison denominators, beta_*, c_alpha of Section 4) must enter
         omega(L) (bookkeeping as in U4/U2 for T_final^*).

### 3.1 Lemma 3.1 (TR(i) without lem:finitebase).  PROVED.
In V1 Proposition TR (and every transplant copying B_+ 1_F) t ||b^+-||_1 <= A_0 := 10 holds at arbitrary F for t <= min(t_eta, t_1), eta <= 1.
Proof.  b^+ = B_+ 1_F + chi V' - kappa a/a(zhat^#), b^- = b^+ - sum_{Kp} eps tau' u (TR Step 5).  lem:smallness holds at arbitrary F (Z5
Section 1: bounded coordinatewise convergence with limsup ||A_n||_1 <= ||a||_1 forces ||A_n - a||_1 -> 0 for every a in l_1), so t||B_+||_1 <=
eta <= 1.  ||V'||_1 <= sum tau' <= 4/t (TR Step 3), |kappa| <= C(K_U + N K_P + 1) t (TR (ii)), ||a||_1 <= 1, a(zhat^#) >= 1/2.  Hence
t||b^+||_1 <= 1 + 4 + 2C(...) t^2 <= 6 for t small, and t||b^-||_1 <= t||b^+||_1 + t sum tau' <= 10 (||u||_1 <= q*(u) = 1).  QED
(lem:finitebase served only to bound ||B_+ 1_F||_1; U2-ref's inspection item G2 thereby reduces to (gamma).)

### 3.2 Proposition 3.2 (cushion domination at a deep-raised companion).  SKETCH.
Let w be a clean sub-window of a main stage L, f^r the deep box-level raise of f beyond depth J (U2 Lemma DR-inf with the raise mass
augmented by |g_j|: Delta a_j := s_j (8 Bx_*(j) + |g_j| - |a_j|)_+ for j >= J; footprint <= mu*_J (8 sum_{j >= J} Bx_* + ||g||_1)), and f^# the
companion of f^r built by Q1's construction with the lever replacements of 3.3/Section 4.  Then the transplanted window data satisfy (U3^inf)
at f^# with C_+ <= C Design(L)/u(w), after (i) projecting the switching of every carrier that is deep at an unraised shallow THIN coordinate to
zero (Lemma P of U2: such amplitudes are <= C_q t/v_l(s); the projection is a face of the pattern cone, Hoffman constant a design minor, V2
Lemma H) and (ii) clamping the then one-sided, switching-free data at those coordinates to 0 (cost <= |a_s|/t + phi_s per coordinate).
Coordinatewise: deep (raised): |usage| <= |g_j| + 12 Bx_*(j)/t <= 2|a^r_j|/t; shallow robust (|a_j| >= u): |usage| <= (Design/u)|a_j|/t;
shallow thin (|a_j| <= b): Lemma P + (i)-(ii).  For the RS/MT III' data this is U2's Lemma W (PROVED, refereed, fix W1).  Not written line by
line: compatibility of the zero-switching faces in (i) with Q1's class/cube pigeonhole (they are sub-patterns, so V2's minors cover them).
The window-dependent C_+ makes c_flat(w) >= c_f u(w)/Design(L), which E^eng accepts because n(w) >> Design(L)/u(w).

### 3.3 Levers at infinite F
For a carrier l needing a two-sided value lever at a clean sub-window take the first two coordinates s < s' of S_l beyond s_max(L) (design
depth, (D-lev): mu*_s^2 v_l(s) >= Design(L)^{-1}).  Exactly one of:
 (L1) one of them is OFF the support: the finite-F lever there (X2 Lemma LV: Z-gen, Z-con, TU), verbatim;
 (L2) one is in F and THIN (|a| <= b(w)): lower it to a contact of the same sign (cost <= 2|a|, Lemma LT partial form; switching-free after
      Proposition 3.2(i)), then (L1)  [U2 TR-inf (a')];
 (L3) both in F, THICK (|a| >= u(w)), ROBUST spread |1 - rho_{s'}/rho_s| >= u(w) (rho := a/v_l): the Hilbert pair (s, s') with
      Delta' = -(alpha_s/alpha_{s'}) Delta, alpha := mu*^2 a/nu^2, cancels the common nu-term at first order: a private two-sided lever of
      efficiency >= Design(L)^{-1} u(w)  [U2 TR-inf (c), PROVED];
 (L4) both thick with TINY spread: single (S-mass) levers whose common mode is not small; treated in Section 4.
(At a clean sub-window thin/thick and tiny/robust are exhaustive: the moduli, spreads and denominators are rate objects of level L.)

### 3.4 Lemma 3.4 (exact drift identity in the (ND)-failure configuration).  PROVED.
Diagonal base.  Let f° be a row (data a°, z°, F°, nu°, e°) and u = sum_k c_k u_k a finite combination of carrier vectors with u|_{F°} =
kappa a°|_{F°}, kappa != 0.  Let f^1 be any row with forced data (a^1, z^1) such that z^1 = z° on supp u and (supp a^1 \ F°) cap supp u is
empty.  [Allowed: arbitrary raises and lowerings on F°, truncation to contacts of the same sign, masses and z-moves outside supp u.]  Then
      sum_k c_k u_k(zhat^1) - sum_k c_k u_k(zhat°) = -(kappa nu°/2) ||e^1 - e°||^2.
Proof.  sum_k c_k u_k(zhat) = u(z) + <U* u, e>, and u(z^1) = u(z°).  U* u = kappa U*(a° 1_{F°}) + U*(u 1_{F° c}) = kappa nu° e° +
sum_{s notin F°} mu_s u(s) k_s, while e^1 = sum_{s in supp a^1} mu_s a^1(s) k_s/nu^1; the cross term sum_{s in supp a^1 \ F°} mu_s^2 u(s) a^1(s)/nu^1
vanishes by hypothesis, and <U*u, e°> = kappa nu° likewise.  So the difference is kappa nu° (<e°, e^1> - 1) = -(kappa nu°/2)||e^1 - e°||^2.  QED
Consequences (PROVED).  (a) Over all rows reachable by such moves the RAW combination sum c u(zhat) attains a strict one-sided extremum at f°:
it only decreases if kappa > 0 (only increases if kappa < 0), with equality iff e^1 = e°.  (b) Its only two-sided first-order resources are
z-moves, banks and pulls on supp u \ F° and sign changes on F° cap supp u (cost |a_s| in the transfer error).  (c) A "de-proportionalizing"
pair (relative raise at one thick coordinate of S_l cap F, compensating lowering at another) creates first-order efficiency at the new row,
but the raw combination never exceeds its value at f°: a target ABOVE that value is unreachable by support moves.  (This corrects the guess
that a small de-proportionalizing raise removes the degeneracy for raw-value targets; for NORMALIZED targets see Section 4.)
Numerics (Q2_work/onesided_check.py): identity exact to 1.7e-15 over 200 random admissible moves (n = 40, |F| = 25); a bank on supp u \ F
changes the combination at first order (+1.4e-14, +1.5e-13, +1.5e-12 for masses 1e-4, 1e-3, 1e-2).

## 4. The degenerate lever configuration in the d-consistency system

### 4.0 The exact Jacobian with S-mass common mode.  PROVED (X2 Lemma M1(iv), Lemma DC step (3')).
For an (S-mass) lever l at p_l in F (ratio rho_l := A_1(p_l)/u_l(p_l), unit step = change of A(p_l) by sgn(A_1(p_l)) beta_{p_l},
beta_p := nu_1/(mu_p^2 |u_l(p_l)|)), every raw value moves at first order by eps_k (delta_{kl} - g_k h_l), g_k := eps_k <U* u_k, e_1>,
h_l := |A_1(p_l)|/(nu_1 |u_l(p_l)|) (h_l := 0 for Z/TU levers); every block norm by dA_m = q_m^T dP - G_m (h^T dP), G_m := sum_{k in block m}
lambda_k w^0_m(k) <U* u_k, e_1> (all carriers, peaks included).  Hence the Jacobian of X2's map F (F_l = eps_l [u_l(xhat) - (A_m/A^0_m) u_l(zhat_0)])
is, up to the data-replacement terms of DC (3),
      N = D - gt h^T - sum_m p_m q_m^T,   D := I + X,   gt := g - sum_m G_m p_m,
with X2's p_m (p_l = eps_l u_l(zhat_0)/A^0_m), q_m (q_k = eps_k lambda_k w^0_m(k)), q_m^T p_m <= C_m <= 1/2, and the absorber matrix X (rows of
absorbers, columns of Omega^0: X^2 = 0, D^{-1} = I - X, q_m^T X = 0).  h^T g = sum_l rho_l gamma_l/nu_1^2 (gamma_l := <U* u_l, U* A_1>): 1 - h^T g is the
Sherman-Morrison denominator of (L4).  X2 required K_J ||g h^T|| <= 1/2, false for thick |A_1(p_l)|.  By the capacitance formula the matrix
I - [h q_1 .. q_M]^T D^{-1} [gt p_1 .. p_M] has diagonal entries 1 - q_m^T p_m >= 1/2 in its last M places, so N has at most ONE degenerate
direction; for one block det N/det D = (1 - q^T p)(1 - h^T D^{-1} gt) - (q^T D^{-1} gt)(h^T D^{-1} p): the Sherman-Morrison degeneracy alone is
NOT a singularity of the d-consistency system (numerically: det = -7.25 at 1 - h^T D^{-1} g = 1e-16, Q2_work/prop41_check.out).

### 4.1 Proposition 4.1 (block-norm bordering).  PROVED.
Let D = I + X, g, h in R^Omega, p_m, q_m supported in disjoint Omega_m with q_m^T p_m <= 1/2 and q_m^T X = 0, m* a block, pi != 0, and
      L(P, P_0) := D P - g (h^T P) - sum_m p_m (q_m^T P) - pi p_{m*} P_0.
Put K_D := 1 + ||X||_inf, Q := sum_m ||q_m||_1, pbar := max_m ||p_m||_inf, H := ||h||_1,
      c_alpha := 1 - h^T D^{-1} g - sum_{m != m*} (h^T D^{-1} p_m)(q_m^T D^{-1} g)/(1 - q_m^T p_m),     beta_* := h^T D^{-1} p_{m*}.
If max(|c_alpha|, |beta_*|) >= beta_0 > 0, then every b has a preimage (P, P_0), linear in b, with ||P||_inf + |P_0| <= K ||b||_inf,
      K := 4 (1 + 1/|pi|) K_D^4 (1 + pbar)^2 (1 + Q)^3 (1 + H)(1 + ||g||_inf)(1 + 1/beta_0),
independent of 1 - h^T g and of det N.
Proof.  q_m^T D^{-1} p_{m'} = q_m^T p_{m'} - q_m^T X p_{m'} = delta_{mm'} q_m^T p_m.  Seek P = D^{-1}(b + g alpha + sum_m p_m gamma_m) with
(i) h^T P = alpha, (ii) q_m^T P = gamma_m (m != m*), (iii) P_0 := (gamma_{m*} - q_{m*}^T P)/pi; then D P = b + g(h^T P) + sum_{m != m*} p_m (q_m^T P)
+ p_{m*}(q_{m*}^T P + pi P_0), i.e. L(P, P_0) = b.  (ii) <=> gamma_m = [q_m^T D^{-1} b + (q_m^T D^{-1} g) alpha]/(1 - q_m^T p_m).  Substituting,
(i) <=> c_alpha alpha - beta_* gamma_{m*} = rhs := h^T D^{-1} b + sum_{m != m*} (h^T D^{-1} p_m)(q_m^T D^{-1} b)/(1 - q_m^T p_m).  If |beta_*| >= beta_0
take alpha := 0, gamma_{m*} := -rhs/beta_*; if |c_alpha| >= beta_0 take gamma_{m*} := 0, alpha := rhs/c_alpha.  Bounds (B := ||b||_inf):
|rhs| <= H K_D (1 + 2 pbar Q K_D) B =: beta_0 R; |alpha|, |gamma_{m*}| <= R; |gamma_m| <= 2||q_m||_1 K_D (B + ||g|| R);
||P||_inf <= K_D [(1 + 2 pbar Q K_D) B + (||g|| + pbar + 2 pbar Q K_D ||g||) R] <= K_0 B with K_0 := 4 K_D^4 (1+pbar)^2 (1+Q)^2 (1+H)(1+||g||)(1+1/beta_0)
(using 1 + 2pbar Q K_D <= 2K_D(1+pbar)(1+Q), ||g|| + pbar + 2pbar Q K_D ||g|| <= 2K_D(1+||g||)(1+pbar)(1+Q), 1 + xH/beta_0 <= x(1+H)(1+1/beta_0)
for x >= 1); |P_0| <= (R + Q ||P||)/|pi| <= (1 + Q) K_0 B/|pi|.  QED
Remarks.  (a) X2's square system (P_0 = 0) needs a codimension-ONE non-degeneracy (det); with one block-norm lever the degenerate set is
{c_alpha = 0 and beta_* = 0} (codimension TWO), with such levers in several blocks codimension 1 + (their number).  (b) General bordering
(PROVED): if s_{n-1}(N) >= sigma > 0, y_0 a unit left singular vector of s_n(N), then s_min([N | w]) >= 1/(1/sigma + (1 + ||w||/sigma)/|y_0^T w|)
(y = t y_0 + y_perp, ||y^T N|| >= sigma ||y_perp||, |y^T w| >= |t||y_0^T w| - ||y_perp|| ||w||).
Numerics: Q2_work/prop41_check.py (3 blocks, absorbers, exact c_alpha = 0 or beta_* = 0): residual <= 2.5e-12, (||P|| + |P_0|)/(K||b||) <= 6.7e-6;
Q2_work/border_check.py: bound (b) holds with min ratio 1.027 over 2000 trials.

### 4.2 Corollary 4.2 (Lemma DC^inf).  PROVED (as a modification of X2 Lemma DC).
Let f_1 be a pre-row of arbitrary support, Omega and levers as in X2 2.1 except that (S-mass) levers may sit at thick support coordinates
(no smallness of the common mode), and let there be a BLOCK-NORM LEVER for a block m*: a coordinate j off supp A_1, in the signature set of a
peak k* of block m*, beyond s_max, in no supp u_k (k in Omega), carrying only fine data V_fine(j) (zero-data lever of X2 Lemma LV(c)),
normalized so that a unit step moves u_{k*}(xhat) by eps; then dF = -pi p_{m*} dP_0 with pi := eps lambda_{k*} w^0_{m*}(k*), |pi| = lambda_{k*} M_{m*}.
If max(|c_alpha|, |beta_*|) >= beta_0 (with g := gt), the conclusion of Lemma DC holds with K_J replaced by K of Proposition 4.1: F has a zero
(P*, P_0*), |(P*, P_0*)| <= K r; peaks (k* included, moved by <= K r) remain peaks; nv_l = nv_l^0 exactly on Omega.
Proof.  DC steps (1), (2), (5) verbatim (the new lever changes z at one coordinate of S_{k*}, hence no Omega value, and A_{m*} at first order
through k*; fine carriers meeting j enter c_tiny).  Step (3): the Jacobian is L of Proposition 4.1 with the remainder bounds of DC (3')
(masses enter smoothly with lever-data constants).  Step (4): with the linear right inverse R_b of 4.1 put (P, P_0) := R_b y and G(y) :=
F(0) + y + Rem(R_b y); on |y|_inf <= r, G_l >= r - |F(0)|_inf - C_2 K^2 r^2 - c_tiny K r >= 0 on {y_l = r} (<= 0 on {y_l = -r}) when
K|F(0)|_inf <= r/2, K C_2 r <= 1/4, K c_tiny <= 1/4; Poincare-Miranda gives a zero.  QED

### 4.3 Lemma 4.3 (exact full degeneracy at infinite F).  PROVED.
Let u = sum_{k in Lambda} c_k u_k (coarse carriers of level <= L) satisfy P_F (I - e e^T) U* u = 0 (no support move changes the combination at
first order; P_F := projection onto span{k_s : s in F}).  Then (a) u|_F = kappa a|_F with kappa = <U* u, U* a>/nu^2; (b) if kappa != 0, F is
contained in supp u (finitely many carrier supports); (c) under the design's privacy (supp u_k cap S_{k'} subset [1, s_max(L)] for coarse
k != k', X2 Lemma LV (SEP)(ii)) the coordinates of S_{k'} beyond s_max(L) are OFF F for every coarse k' notin Lambda, in particular for every peak.
Proof.  (a) P_F U* u = U*(u 1_F), P_F e = e, so U*(u 1_F) = (<U*u, e>/nu) U* a, and mu_s > 0.  (b) u(s) = kappa a_s != 0 on F.  (c) such a
coordinate lies in no supp u_k (k in Lambda), hence not in supp u, hence not in F.  QED
So in the exact full-degenerate configuration every block has peak zero-data levers, and Corollary 4.2 applies as soon as max(|c_alpha|,
|beta_*|) >= beta_0 for one block; if kappa = 0 the carriers of Lambda do not meet F (their levers are of type (L1)).

### 4.4 What remains of the degenerate configuration
 (i) PROVED: with block-norm levers, d-consistency degenerates only on (NDN2): c_alpha ~ 0 AND beta_* ~ 0 in every block having such a
     lever, where (absorber entries of h being <= C_f c_{L+1}) beta_* ~ sum_{l in Omega_{m*}} rho_l u_l(zhat_0)/(nu_1 A^0_{m*}) (the rho-weighted
     base value of the S-mass carriers) and c_alpha ~ 1 - sum_l rho_l gamma_l/nu_1^2 - (block-norm terms).
 (ii) PROVED (Lemma 3.4 + 4.0): in the EXACT version of (NDN2) with exact full degeneracy, the left null vector of N is D^{-T} h and the
     corresponding combination of the d-consistency equations moves under support moves only at SECOND order (raw part -(kappa nu/2)||Delta e||^2,
     normalized part sum_m (Delta A_m) h^T D^{-1} p_m = 0 at first order), plus tau := the first-order effect of moves on supp u \ F (window
     theta-masses on W cap supp u; the cut-off beyond N'', a tail <= sum_{j > N''} |u(j)|).  A second-order residue is tolerated by Theorem
     UE^inf (it needs |kappa^+-| <= c delta s_1; Pi^2 <= c delta s_1 for s_1 small after the window).
 (iii) OPEN: whether tau_W (first order in s_1 with a window-dependent constant) is compatible with that tolerance, and the quantitative
     version of (NDN2) (both objects tiny but nonzero) when not separated by the pigeonhole.  (NDN2) is non-generic: codimension two in the
     level-L data at every level where it is needed.
 (iv) OPEN: KN-1 holds of Q1's Step A (raw values held at exactly 0) whose own-set levers are thick support coordinates: the raw system has
     Jacobian D - g h^T, degenerate when 1 - h^T D^{-1} g ~ 0, and the bordering helps only if one of the per-block kappa restorations (peak
     pushes) can be traded for the degenerate direction, which depends on the pattern's ratio system Z_kappa (not checked).

## 5. Assembly and the precise remaining step

### 5.1 Theorem 5.1 (transport of Master Theorem VI to infinite F).  SKETCH.
Let T_fin^* (option (a)), N >= 1, f in S_{p_N*} with infinite base support.  Call f LEVER-REGULAR if for infinitely many main stages L the clean
sub-window w(L) (rate objects of 3.0(eps) included in omega(L)) satisfies: in every value-tuning system of the companion construction at the
deep-raised row (Q1 Lemma CM^tr Step A: TU settings, KN-1 holds, peak pushes; X2 Lemma DC at the pre-row) every carrier needing a lever is in
case (L1), (L2) or (L3) of 3.3, or the (S-mass) levers of case (L4) satisfy max(|c_alpha|, |beta_*|) >= u(w) in some block with a block-norm
lever (Corollary 4.2), and no KN-1 hold lies in a degenerate direction of its raw system.  Then f is in Rec_N; in particular (LSC-trunc) holds
at f for every mate.
Route, per clean sub-window w(L): (1) deep raise f -> f^r beyond J (U2 DR-inf: the clean classification is preserved; V3 RT gives hypothesis
(a) of Theorem E^{eng,RT,inf} with eps' = Hilbert footprint + normer change, <= mu*_J(...) log); (2) Q1's companion (Lemma CM^tr) at f^r with
levers replaced as in 3.3 / Corollary 4.2; (3) transplanted window data with Lemma 3.1 and Proposition 3.2 ((U3^inf), C_+ <= C Design/u);
(4) Theorem UE^inf at the companion and Theorem E^{eng,RT,inf} along the windows (Z3 Lemma 3.1 for the companion moves, eps' = o(T_lo^2)); the
engineered approximants are norm attaining with finite base support.
Why SKETCH: Proposition 3.2 for Q1's data; Step B's static-ownership recursion when J_fine meets F (coordinates of F cannot be assigned a
sign freely); status stability (V1 Lemma ST) under the side effects of (L2), (L3) and S-mass levers (second order, harmless by Lemma RR, not
re-checked line by line); bookkeeping of the new rate objects.

### 5.2 Corollary 5.2 (rows avoiding the lever ranges).  SKETCH.
If F cap (union of the signature sets S_l) is finite -- more generally, if for infinitely many main stages L the support F meets no S_l
(l of level <= L) inside the lever range (s_max(L), s_far(w(L))] -- then every lever of Q1's construction is of type (L1) (verbatim finite-F
levers), f is lever-regular, and f is in Rec_N modulo Proposition 3.2 and the Step B audit.  (For F cap (union S_l) finite the condition holds
for every L with s_max(L) > max(F cap union S_l).)

### 5.3 THE PRECISE REMAINING STEP for (LSC-trunc) (given Q1)
 (R1) Proposition 3.2 for Q1's data (U1 (class, cube) sets, KN^tr, Lemma CM'): compatibility of Lemma P's zero-switching faces with the
      class/cube pigeonhole.
 (R2) Line-by-line replacement of every lever of Q1's construction (KN^tr's TU levers, KN-1 holds and peak pushes; Lemma DC's levers; V1's
      donors and pulls) at coordinates of S_l cap F by (L1)-(L3) or the bordering of Corollary 4.2; Step B's ownership recursion on J_fine \ F;
      V1 Lemma ST under the new side effects.
 (R3) The degenerate configurations: (NDN2) for d-consistency (4.4(iii): exact case with tau_W != 0, and the quantitative near-degenerate
      case) and KN-1 holds in a degenerate direction (4.4(iv)).  Candidate resolutions (not carried out): data-side freedom (choose the
      switching data with Domega^T rtilde = 0 for the uncontrollable direction rtilde, so that the residue does not enter kappa^+-); window
      masses placed off supp u; targets defined at a de-proportionalized base row (Lemma 3.4(c) caps raw targets only).
 (R4) Bookkeeping: add the moduli |a_s| at design depth, spreads, Sherman-Morrison denominators, beta_*, c_alpha to omega(L) (as U4/U2 did for
      T_final^*).
(R1), (R2), (R4) are audits of existing constructions; (R3) needs a new argument, or a proof that the degeneracy at all large stages is
incompatible with the structure that requires exact tuning.  Rows that are lever-regular need only (R1), (R2), (R4).

## 6. Numerics (evidence only; Q2_work/)
 lt_check.py -> lt_check.out: finite SOCP model (16 base coordinates, |F| = 12, 2 blocks x 6 carriers, mu_j = 0.25 * 0.5^{j^1.3}, CLARABEL):
   (LT) never violated (max LHS - RHS = -8.0e-9); cushion loss 1e-3..1e-2 vs naive p*(f^M - f) 1e-2..6e-2; normer change 1e-12..1e-14.
 onesided_check.py -> onesided_check.out: Lemma 3.4 identity exact to 1.7e-15 (200 random admissible moves); banks on supp u \ F act at
   first order (1.4e-14, 1.5e-13, 1.5e-12, linear in the mass).
 border_check.py -> border_check.out: general bordering bound (min ratio 1.027); Woodbury determinant formula (error 1e-14); exact SM
   degeneracy with peak column: s_min([N | -pi p]) = 0.26 for h^T p = 1, degrading only as h^T p -> 0.
 prop41_check.py -> prop41_check.out: explicit right inverse of Proposition 4.1 (3 blocks, absorbers, exact c_alpha = 0 or beta_* = 0):
   residual <= 2.5e-12, bound ratio <= 6.7e-6; one block with 1 - h^T D^{-1} g = 1e-16: square determinant -7.25 = formula.

## 7. Assessment
Leaning POSITIVE that (LSC-trunc) holds for T_fin^* (hence density for p_N, and for Martin's p via Corollary VI.3): truncation costs
nothing at finitely many scales (Lemma LT), finite base support of the approximant is free in the violation-tolerant route (Section 2), and
every infinite-F obstruction found is either an audit of an existing construction or a degeneracy of a lever system of codimension >= 2 at
infinitely many levels (Section 4).  No mechanism for a counterexample was found: a bad row would need, at all large stages, the
codimension-two degeneracy (NDN2) or a degenerate KN-1 direction, together with the failure of every candidate in (R3).
Negative claims made here (all precise and limited): Lemma 3.4(c) (support moves cannot push a degenerate RAW combination above its value
at the proportional row) and the heuristic 1.4; neither excludes (LSC-trunc).
