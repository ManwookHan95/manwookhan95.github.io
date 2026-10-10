# Q2 part 1 -- setting, the lowering-transfer lemma, window-local truncation

Notation of the note (paper/martin_density_note.tex, Sections 1, 2, 7, 8).  Finite block set I = {1,...,N}, p = p_N.
f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu), F = supp a INFINITE, s_j := sgn a_j (j in F),
s(t) := sqrt(1 + t^2), alpha(M) := sum_{j > M} |a_j|.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.0 The statement and what it is equivalent to

(LSC-trunc) For every f in S_{p*}, every g in C(f), every rho in (0,1) and every eps > 0 there is f' in S_{p*} whose forced base
part a' has FINITE support, with p*(f' - f) < eps and dist_{p*}(rho g, C(f')) < eps.

Facts (PROVED earlier, recalled): (i) Z5 Proposition 5.4: given Lemma Z at every finite-F row, (LSC-trunc) <=> density of
NA((c_0, p_N), l_2^2).  (ii) Part I, Lemma lem:pair: if (f, rho g) is in cl NA then (LSC-trunc) holds at (f, g, rho) (norm-attaining
rows have finite base support, Proposition prop:smooth(c)).  (iii) Conversely, if (LSC-trunc) holds at (f, g, rho') for all rho' < 1 and
every finite-F row is in Rec (finite-F Lemma Z), then (f, g) is in cl NA (transitivity, Theorem thm:transitivity, per mate).
So (LSC-trunc), per mate, is exactly "Lemma Z at infinite F with finite-support targets".  It is NOT weaker in substance:
see 1.3 for why every proof must produce EXACT local data at a finite-F row (HEURISTIC there, but it explains the architecture).

## 1.1 Contact truncations

For M with a 1_{[1,M]} != 0 put c_M := q*(a 1_{[1,M]}), a^M := a 1_{[1,M]}/c_M, and let f^M be the first row with forced data
(a^M, z) (Remark rem:lemmaZ(c) of the note): e^M := U* a^M/||U* a^M||, zhat^M := z + U e^M, q_0^M := (1 + sum_m |R_m^** zhat^M|_m)^{-1},
xi^M := q_0^M zhat^M, w^M := J_V(L^** xi^M), f^M := a^M + L* w^M.  (Admissible: z = sgn a^M on supp a^M = F cap [1,M]; |z| <= 1.)
The support coordinates j in F, j > M, become CONTACTS of f^M with sign s_j; nothing else changes in z.

Lemma 1.1 (elementary facts).  PROVED.
 (a) |1 - c_M| <= alpha(M) + ||U* a_{>M}||, where a_{>M} := a 1_{(M,inf)}.
 (b) ||e^M - e|| <= 2 ||U* a_{>M}||/nu, and zhat^M - zhat = U(e^M - e) (a vector of c_0 of sup-norm <= ||U|| ||e^M - e||).
 (c) f^M -> f in norm as M -> infinity, and all forced data of f^M converge to those of f (Proposition prop:continuity).
 (d) For the diagonal base U k_s = mu_s e_s with mu decreasing: ||U* a_{>M}|| <= mu_{M+1} alpha(M).
Proof.  (a) 1 = ||a||_1 + ||U*a|| = ||a 1_{[1,M]}||_1 + alpha(M) + ||U*a|| and c_M = ||a 1_{[1,M]}||_1 + ||U* a 1_{[1,M]}||, and
| ||U*a|| - ||U* a 1_{[1,M]}|| | <= ||U* a_{>M}||.  (b) ||x/||x|| - y/||y|| || <= 2||x - y||/||y|| with x = U* a 1_{[1,M]}, y = U*a, ||y|| = nu.
(c) Proposition prop:approximants, (ii) => (i) (valid for every f, as checked in Z5 Lemma 2.1(b)): a^M -> a in l_1 by (a), z fixed.
(d) ||U* a_{>M}||^2 = sum_{j > M} mu_j^2 a_j^2 <= mu_{M+1}^2 alpha(M)^2.  QED

## 1.2 The lowering-transfer lemma (LT).  PROVED.

Lemma LT.  Let h in X*, r in R, and let f + r h = A + L*W with q*(A) <= pi and ||W||_{V*} <= pi (e.g. pi = p*(f + r h) and the optimal
decomposition of Lemma lem:dualball).  Put B := (A - a)/r (r != 0) and define the CUSHION LOSS
      Lambda_M(r, B) := sum_{j in F, j > M} min( |a_j| , (-s_j r B_j)_+ )      (<= alpha(M), and <= |r| ||B 1_{(M,inf)}||_1).
Then
      p*(f^M + r h) <= pi + 2 Lambda_M(r, B) + 2 ||U* a_{>M}|| + p*(L*(w^M - w)).                                         (LT)
Proof.  f^M + r h = (f + r h) + (f^M - f) = [A + a^M - a] + L*W + L*(w^M - w).  Put A' := A + a^M - a = a^M + r B.  Then
p*(f^M + rh) <= p*(A' + L*W) + p*(L*(w^M - w)) <= max(q*(A'), ||W||) + p*(L*(w^M - w)) (Lemma lem:dualball), so it suffices to show
q*(A') <= q*(A) + 2 Lambda_M + 2||U* a_{>M}||.
Write a^M = a_{<=M} + (1/c_M - 1) a_{<=M} with a_{<=M} := a 1_{[1,M]}, so A' = (a_{<=M} + rB) + (1/c_M - 1) a_{<=M} and
      q*(A') <= q*(a_{<=M} + rB) + |1/c_M - 1| q*(a_{<=M}) = q*(a_{<=M} + rB) + |1 - c_M|.
l_1 part: for j <= M the coordinates of a_{<=M} + rB and of A = a + rB agree; for j > M not in F they agree (a_j = 0); for j in F,
j > M, with alpha_j := |a_j|, x := r B_j and y := (-s_j x)_+, the elementary identity
      |s_j alpha_j + x| - |x| = alpha_j - 2 min(alpha_j, y)
(case s_j x >= 0: alpha_j; case 0 < y <= alpha_j: alpha_j - 2y; case y > alpha_j: -alpha_j) gives |x| = |A_j| - |a_j| + 2 min(|a_j|, y).
Summing, ||a_{<=M} + rB||_1 = ||A||_1 - alpha(M) + 2 Lambda_M.  Hilbert part: ||U*(a_{<=M} + rB)|| <= ||U* A|| + ||U* a_{>M}||.
Hence q*(a_{<=M} + rB) <= q*(A) - alpha(M) + 2 Lambda_M + ||U* a_{>M}||, and with Lemma 1.1(a),
      q*(A') <= q*(A) - alpha(M) + 2Lambda_M + ||U* a_{>M}|| + alpha(M) + ||U* a_{>M}|| = q*(A) + 2 Lambda_M + 2||U* a_{>M}||.   QED

Remarks.  (1) The l_1-mass alpha(M) of the truncation CANCELS (exactly as the raise mass cancels in V3's raise-transfer Lemma 2.3).
What remains is (i) the cushion loss Lambda_M, which is the l_1-mass of the anti-sign part of the decomposition on the far support,
truncated at the cushion -- it vanishes when the decomposition uses the far support only in the sign direction; (ii) the Hilbert
footprint 2||U* a_{>M}|| <= 2 mu_{M+1} alpha(M); (iii) the normer change p*(L*(w^M - w)).
(2) Normer change.  By Lemma 1.1(b), zhat^M - zhat = U(e^M - e) with eps_e := ||U|| ||e^M - e|| <= 2||U|| ||U* a_{>M}||/nu; V3 Lemma 2.2
(refereed; its proof uses only the clamp formula at zhat and zhat^M, never base parts, and z is unchanged here) gives, once
max_m Delta_m <= c_f, p*(L*(w^M - w)) <= C'_f eps_e log(e/eps_e).  So the zeroth-order part of (LT),
      eps''_M := 2||U* a_{>M}|| + p*(L*(w^M - w)) <= C_f mu_{M+1} alpha(M) log(e/(mu_{M+1} alpha(M)))   (diagonal decreasing base),
is super-polynomially small in the depth M for the designed base.
(3) (LT) is the exact counterpart, for LOWERINGS, of V3's raise transfer: a raise transfers every decomposition at no l_1-cost; a
lowering transfers a decomposition at no l_1-cost exactly when the decomposition does not use the cushions of the lowered
coordinates.  General form (same proof): let Delta a be supported in F with s_j Delta a_j <= 0 and |Delta a_j| <= |a_j| (a partial
lowering; coordinates lowered to 0 become contacts of sign s_j), and let f^low be the row with forced data
((a + Delta a)/q*(a + Delta a), z) (same z: admissible, since z_j = s_j wherever a + Delta a is nonzero).  With y_j := (-s_j r B_j)_+ and alpha'_j := |a_j + Delta a_j|,
the identity |s alpha' + x| - |s alpha + x| = -|Delta a_j| + 2 min(|Delta a_j|, (y_j - alpha'_j)_+) (cases s x >= 0; y <= alpha';
alpha' < y <= alpha; y > alpha) gives
      p*(f^low + r h) <= pi + 2 sum_j min(|Delta a_j|, (y_j - alpha'_j)_+) + 2||U* Delta a|| + p*(L*(w^low - w)).
Only usage BEYOND THE NEW CUSHION alpha'_j is lost.

## 1.3 Window-local truncation.  PROVED.

Corollary 1.2.  Let S be a finite set of nonzero reals and, for r in S, decompositions f + r h_r = (a + r B_r) + L*(w + r Theta_r) with
max(q*(a + r B_r), ||w + r Theta_r||) <= pi_r.  For every eta > 0 there is M_0 such that for all M >= M_0 and r in S:
      p*(f^M + r h_r) <= pi_r + eta r^2 + eps''_M.
Proof.  Lambda_M(r, B_r) <= |r| ||B_r 1_{(M,inf)}||_1 -> 0 as M -> infinity for each of the finitely many r (B_r in l_1); choose M_0
with 2|r| ||B_r 1_{(M_0,inf)}||_1 <= eta r^2 for r in S.  QED

Consequence (the precise role of truncation).  Every window method uses decompositions at finitely many scales (a window).  For
those, the truncation point can be chosen AFTER the window and after the decompositions; then the truncated row f^M carries the same
decompositions up to eta r^2 + eps''_M.  So "far support" is never an obstruction at the level of decompositions at finitely many
scales.  What the truncation cannot give for free is the behaviour of f^M at scales BELOW sqrt(eps''_M) (and below the window): there
the local structure of f^M itself decides, and a mate of f^M must be built from EXACT local data at f^M (or at a companion).

## 1.4 Why exact local data cannot be avoided (HEURISTIC, explains the architecture)

Let f' be any row with p*(f' - f) = d > 0 (in particular any finite-F row near f).  For |r| >> sqrt(d/(1 - rho^2)) the slack of rho g
covers every transfer error, and functionals within (1 - rho^2)|r| of rho g are mates "at scale r".  For |r| << sqrt(d), the
inequality p*(f' + r g') <= s(r) is a statement about the second-order structure of p* at f' alone: every one-sided constraint of
f' (contacts, peaks, free coordinates, the levels of each block and of the base) must be met EXACTLY by a decomposition of g' at
scale r, uniformly as r -> 0.  The normer change w' - w is nonzero for every f' != f near f (Lemma 1.1(b): zhat' - zhat = U(e' - e) is a
nonzero c_0 vector, and the blocks see it through infinitely many carriers), so the block structure of f' (statuses of deep carriers,
levels, d-coefficients) differs from that of f at arbitrarily small scales.  Hence g' must carry exact local data AT f'; in all known
methods these are window data at a companion, averaged over a window (Theorem E, E_RT, E^eng).  This is why (LSC-trunc) inherits the
whole exactification problem (finite-F core + infinite-F items), and why the useful reduction is: "finite base support of the
approximant is free once exact (violation-tolerant) window data exist at some base row" (part 2).

## 1.5 Numerical sanity check (evidence only): Q2_work/lt_check.py -> lt_check.out
Finite SOCP model (16 base coordinates, |F| = 12, 2 blocks x 6 carriers, diagonal base mu_j = 0.25 * 0.5^{j^1.3}), first rows from
forced data, contact truncations at M = 7, 9, random directions h and r in {0.3, 0.1, 0.03, 0.01, -0.03}, p* by CLARABEL.  (LT) was
never violated (max of LHS - RHS = -8e-9, i.e. solver accuracy); the cushion loss Lambda_M is typically 1e-3..1e-2 while the naive
bound p*(f^M - f) is 1e-2..6e-2; the normer change p*(L*(w^M - w)) is 1e-12..1e-14 (deep coordinates have tiny mu).
