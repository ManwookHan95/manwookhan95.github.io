# Q2 referee (a), part 1 -- Section 1 of Q2 (truncation)

Sources checked: r10/Q2_notes.md 1.1-1.4, r10/Q2_part1.md, the note (lem:dualball, prop:forced, prop:smooth, prop:continuity,
prop:approximants), r7/V3_notes.md 2.1-2.5 (raise transfer, normer change Lemma 2.2).

## 1. Lemma 1.1 (contact truncations).  VERDICT: correct (PROVED).
Re-derivation.  q*(a) = 1 (prop:forced(b)), so 1 - c_M = alpha(M) + (||U*a|| - ||U* a_{<=M}||) and the bracket has modulus
<= ||U* a_{>M}|| (for the diagonal base it is >= 0, so 1 - c_M >= alpha(M) >= 0).  (b): e^M = U* a_{<=M}/||U* a_{<=M}|| (scale invariance),
||x/|x| - y/|y| || <= |x - y|/|y| + |x| |1/|x| - 1/|y|| <= 2|x - y|/|y|; z is unchanged so zhat^M - zhat = U(e^M - e).  (c): the first row
with forced data (a^M, z) is well defined (any (a', z') with q*(a') = 1, |z'| <= 1, z' = sgn a' on supp a' gives f' := a' + L* J_V(L** q_0' zhat')
in S_{p*} with normer q_0' zhat', and by uniqueness of the forced decomposition (prop:forced(b)) its forced data are exactly (a', z')).
The convergence argument of prop:approximants (ii) => (i) uses only a'_n -> a in l_1 and bounded coordinatewise convergence of z'_n, never
z'_n in c_0, so it applies to the (non-norm-attaining) rows f^M.  (d): ||U* a_{>M}||^2 = sum_{j > M} mu_j^2 a_j^2 <= mu_{M+1}^2 alpha(M)^2.
Precision (p1.1): (a) and (b) hold for every base U; (d) needs a diagonal base with mu non-increasing (true for mu* of U2).

## 2. Lemma LT (lowering transfer).  VERDICT: correct (PROVED), including the partial-lowering form.
Re-derivation of the full form.  f^M + r h = A' + L*W + L*(w^M - w), A' := A + a^M - a = a^M + r B.  By lem:dualball and the triangle
inequality p*(f^M + r h) <= max(q*(A'), ||W||) + p*(L*(w^M - w)).  A' = (a_{<=M} + rB) + (1/c_M - 1) a_{<=M} gives
q*(A') <= q*(a_{<=M} + rB) + |1 - c_M|.  The l_1 parts of a_{<=M} + rB and A = a + rB differ only on F cap (M, inf), where the identity
      |s alpha + x| - |x| = alpha - 2 min(alpha, (-s x)_+)        (alpha >= 0, s = +-1, x real)
(three cases checked: s x >= 0; 0 < -s x <= alpha; -s x > alpha) gives ||a_{<=M} + rB||_1 = ||A||_1 - alpha(M) + 2 Lambda_M.  Hilbert part
||U*(A - a_{>M})|| <= ||U*A|| + ||U* a_{>M}||.  With Lemma 1.1(a) the alpha(M) terms cancel: q*(A') <= q*(A) + 2 Lambda_M + 2||U* a_{>M}||.
Partial form: identity |s alpha' + x| - |s alpha + x| = -(alpha - alpha') + 2 min(alpha - alpha', (y - alpha')_+), y := (-s x)_+,
0 <= alpha' <= alpha (four cases checked: s x >= 0; y <= alpha'; alpha' < y <= alpha; y > alpha), and |1 - q*(a + Delta a)| <= ||Delta a||_1 +
||U* Delta a|| (both signs of 1 - lambda' checked).  Admissibility of (a + Delta a, z) is clear (z = s_j wherever a + Delta a != 0).
Sharpness (new, PROVED): the factor 2 in front of Lambda_M in the BASE inequality q*(A') <= q*(A) + 2 Lambda_M + 2||U* a_{>M}|| (the core of the
proof) cannot be improved: h := -s_j e_j* for one j in F, j > M, 0 < r <= |a_j|, A := a + r h.  Then q*(A) = 1 - r + O(mu_j^2 r), Lambda_M = r and
q*(a^M + r h) = 1 + r + O(mu_{M+1} alpha(M)).  (For p* itself the max with ||W|| = 1 can hide part of it; the q*-level statement is what the
violation-tolerant route uses.)
Interpretation (agrees with Q2): the truncated coordinate j, a contact of f^M with sign s_j, can no longer absorb anti-sign usage; usage of
size y <= |a_j| that LOWERED |A_j| at f now RAISES the l_1 norm at f^M by the same amount: net 2y.

## 3. Normer change (Remark (2) of 1.2).  VERDICT: correct, with precision (p1.2).
V3 Lemma 2.2 (refereed) bounds p*(L*(w^# - w)) through Z3 Lemma 3.1, whose proof uses only the clamp formula for zhat and zhat^# with the SAME z;
for f^M the z is unchanged and zhat^M - zhat = U(e^M - e), so the lemma applies verbatim with eps_e = ||U|| ||e^M - e|| <= 2||U|| ||U* a_{>M}||/nu.
(p1.2) The bound p*(L*(w^M - w)) <= C'_f eps_e log(e/eps_e) needs V3's precondition max_m Delta_m <= c_f (true for M >= M_f), and C'_f, c_f depend
on f (forced data, gaps of the finitely many relevant carriers).  "Super-polynomially small in M" is then correct for the doubly exponential base
mu*_s = 2^{-2^{2^s}}: eps''_M <= C_f mu*_{M+1} alpha(M) log(e/(mu*_{M+1} alpha(M))) (alpha(M) <= 1).

## 4. Corollary 1.2 (window-local truncation).  VERDICT: correct (PROVED).
Lambda_M(r, B_r) <= |r| ||B_r 1_{(M,inf)}||_1 -> 0 for each r in the finite set S because B_r = (A_r - a)/r is in l_1.  Quantifier order: S, the
decompositions, eta are fixed first; M_0 is chosen last.  The statement says nothing about scales outside S, nor about uniformity in r on an interval:
Lambda_M(r, B_r) <= alpha(M) is the only uniform bound, i.e. (LT) is uniform in r only up to the ZEROTH-ORDER error 2 alpha(M) + eps''_M.
Precision (p1.3): for a continuum of scales one needs sup_{|r| <= r_1} ||B_r 1_{(M,inf)}||_1 |r| / r^2 -> 0 as M -> inf, i.e. tightness of the
family r^{-1}(A_r - a) 1_{(M, inf)} in l_1 uniformly in r: false in general (e.g. for a mate g with ||g 1_{(M,inf)}||_1 > 0 for every M whose
optimal decompositions place anti-sign mass on far support coordinates at scale r ~ |a_j|, the far coordinate j contributes ~ |a_j| ~ r to
Lambda_M at that scale, i.e. order r, not r^2).  This is why Q2 needs Section 2 (violation tolerance with the truncation point after s_1)
and not just Corollary 1.2.  Q2's own text (1.3 "Consequence", 1.4) says exactly this; no overclaim.

## 5. Heuristic 1.4.  HEURISTIC, correctly labelled; the argument is an explanation, not a proof.  One remark: "the normer change w' - w is nonzero for
every f' != f" is true (forced data determine f), but "the statuses of deep carriers differ at arbitrarily small scales" is not proved and need not
hold in a given block (it is not needed anywhere).

## 6. Numerics (referee's own script, Q2_refa_work/lt_adversarial.py -> .out)
Independent finite SOCP model (14 base coordinates, |F| = 11, 2 blocks x 5 carriers, CLARABEL), ADVERSARIAL directions h (anti-sign mass of size
up to 3|a_j|/|r| on the truncated support, and on partially lowered coordinates), r in {0.2, 0.05, 0.01, 0.002, -0.01}, truncation M in {5, 8}, 150
tests: max(LHS - RHS) = -2.7e-7 for (LT) (i.e. (LT) is essentially attained by adversarial h), -6.7e-4 for the partial-lowering form.  Base-level
sharpness: q*(a^M + r h) - q*(a + r h) = 2 Lambda_M to 7 digits for h = -s_j e_j*, j > M.
VERDICTS part 1: Lemma 1.1 correct; Lemma LT correct (sharp); Corollary 1.2 correct; heuristic 1.4 correctly labelled.  Precisions (p1.1)-(p1.3)
are clarifications, not errors.
