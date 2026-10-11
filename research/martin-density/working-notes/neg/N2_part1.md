# N2 (negative track) part 1: witness calculus for non-recovery

Setting and notation as in Part I (canonical base, finite block set I, admissible T).  For f' in S_{p*} attaining its norm
at x' in S_p (so f' = grad p(x')), put
   R_{f'}(y) := ( p(x'+y)^2 - f'(x'+y)^2 )^{1/2}   (y in X),   Delta'(y) := p(x'+y) - f'(x'+y) >= 0.

## Lemma 1.1 (single-piece witness).  PROVED.
Let f' in NA cap S_{p*} with normer x' and let h in X*.  Then for every y in X with x' + y != 0,
      dist_{p*}(h, C(f'))  >=  ( |h(x'+y)| - R_{f'}(y) ) / p(x'+y)      and      dist_{p*}(h, C(f'))  >=  |h(x')| .
Consequently, for h = rho g, a NA row f' is "bad" for the pair (g, rho) at level delta as soon as some y has
      rho |g(x'+y)| >= R_{f'}(y) + delta p(x'+y).
Proof.  Let g' in C(f').  By Part I prop:reduction(a) applied at the point x'+y, g'(x'+y)^2 <= p(x'+y)^2 - f'(x'+y)^2, i.e.
|g'(x'+y)| <= R_{f'}(y).  Hence |h(x'+y)| <= |g'(x'+y)| + |(h-g')(x'+y)| <= R_{f'}(y) + p*(h-g') p(x'+y).  Taking the infimum over
g' in C(f') gives the first inequality.  For the second take y = 0: R_{f'}(0) = 0 (p(x') = f'(x') = 1), p(x') = 1.  QED

Remark 1.2 (the witness is optimal up to the sublinear envelope).  By Part I prop:primal and the minimax theorem (C(f') is
weak*-compact and convex, B_p convex), dist_{p*}(h, C(f')) = sup_{x in B_p} ( h(x) - r~_{f'}(x) ), r~_{f'} the largest
sublinear minorant of r_{f'} = (p^2 - f'^2)^{1/2}.  Lemma 1.1 uses the decomposition x = (x'+y) + (-x'), for which
r_{f'}(-x') = 0; it is the natural certificate when the obstruction is a single direction at a single scale.  Multi-piece
decompositions x = sum_i (lambda_i x' + y_i) (sum lambda_i = 0) give r~_{f'}(x) <= sum_i r_{f'}(lambda_i x' + y_i), i.e. an
infimal convolution of the "+ side" and "- side" profiles; a non-recovery proof may need them when the obstruction mixes
sides.  (Not used below.)  STATUS: the identity is PROVED (standard minimax: the pairing is weak*-continuous in the
functional and affine in both variables).

Remark 1.3 (finite test spaces).  By Part I thm:compact (global compactness) and the reduction (R3) of the briefing, (f, rho g)
is NOT in cl NA iff there are delta > 0 and a finite-dimensional E subset c_00 such that every NA f' with p*(f'-f) < delta
satisfies sup_{x in E, p(x) <= 1} ( rho g(x) - r~_{f'}(x) ) >= delta.  So a non-recovery proof must produce, for EVERY NA f'
near f, a cheap primal decomposition of some x in a FIXED finite-dimensional space of finitely supported vectors.
PROVED (it is Part I lem:pair + the lower-limit theorem restated; the "if" direction is Lemma 1.1 plus Remark 1.2, the "only if" direction is
the (R3) sufficient condition read contrapositively).

## Lemma 1.4 (upper bound for the block excess by a primal splitting).  PROVED.
Fix a block (index dropped), zeta' := R x' != 0 with norming functional w' (N(w') = 1), data M', C', P', alpha' as in Part I
Lemma 1.7, sigma' := |zeta'|.  Let eta in l_1 and t > 0, and split eta = eta_1 + eta_2 with
  (i)  eta_1 supported in supp alpha' and  |t eta_1(k)| <= sigma' |alpha'(k)| = lambda_k mu'_k  whenever sgn eta_1(k) = -sgn alpha'(k),
  (ii) w'(eta_2) = (C'/M') w'(eta_1),  and  || D^{-1} eta_2 ||_2 < infinity.
Then
      |zeta' + t eta| - w'(zeta' + t eta)  <=  t^2 || D^{-1} eta_2 ||_2^2 / (2 sigma') .
Proof.  By Part I lem:threshold, zeta' = sigma' alpha' + D beta' with beta' := sigma' D w'/C', ||beta'||_2 = sigma', ||alpha'||_1 = 1, and
alpha' lives on P' with the signs of w' (so w' = M' sgn alpha' on supp alpha').  Write zeta' + t eta = x_0 + D b with x_0 :=
sigma' alpha' + t eta_1, b := beta' + t D^{-1} eta_2.  The unit ball of |.| is B_{l_1} + D(B_{l_2}), hence |zeta' + t eta| <=
max(||x_0||_1, ||b||_2).  By (i) no coordinate of x_0 changes sign relative to sigma' alpha' (coordinates off supp alpha' are 0),
so ||x_0||_1 = sigma' + t sum_k sgn(alpha'(k)) eta_1(k) = sigma' + t w'(eta_1)/M'.  Next
||b||_2^2 = sigma'^2 + 2 t sigma' <D w', D^{-1} eta_2>/C' + t^2 ||D^{-1}eta_2||^2 = sigma'^2 + 2 t sigma' w'(eta_2)/C' + t^2 ||D^{-1}eta_2||^2,
so ||b||_2 <= sigma' + t w'(eta_2)/C' + t^2 ||D^{-1}eta_2||^2/(2 sigma').  By (ii), w'(eta_1)/M' = w'(eta_2)/C' = w'(eta) (indeed
w'(eta) = w'(eta_1) + w'(eta_2) = w'(eta_1)(1 + C'/M') = w'(eta_1)/M').  Hence max(||x_0||_1, ||b||_2) <= sigma' + t w'(eta) +
t^2 ||D^{-1}eta_2||^2/(2 sigma'), and w'(zeta' + t eta) = sigma' + t w'(eta).  QED

Reading.  Peaks of f' absorb a push eta(k) = lambda_k u_k(y) (for eta = R y) up to their margins mu'_k / t; only the
unabsorbed remainder enters the l_2 part, with weight 1/Phi_k^2, i.e. with the depth-independent weight m^2 (u_k(y) - absorbed)^2.
Strict non-peaks and degenerate peaks absorb nothing.  This is the "relevant carrier" bound: at scale t in direction y only
the carriers with |u_k(x')| <~ t |u_k(y)| (and the strict non-peaks) contribute, and each contributes at most ~ m^2 t^2 u_k(y)^2 /
(2 sigma'); a deep carrier can alternatively be put into the l_1 part with a sign flip at first-order cost 2(|t eta(k)| -
lambda_k mu'_k)_+ <= 2 t lambda_k |u_k(y)| (the "linear regime").  Together with Lemma 1.5 this gives explicit upper bounds for
R_{f'}(y) = (Delta'(y)(2 + 2 f'(y) + Delta'(y)))^{1/2}.

## Lemma 1.5 (base flatness at free coordinates).  PROVED.
Let f' be NA with base data (a', z', e'), x' = c'(z' + U e'), c' = q(x').  Let y in X be supported in a set J of coordinates
with J cap supp a' = empty and |z'_j| + |y_j|/c' <= 1 for j in J.  Then q(x' + y) - a'(x' + y) = 0.
Proof.  x' + y = c'((z' + y/c') + U e') and z' + y/c' in B_{l_infty} (coordinatewise), so q(x' + y) <= c'.  Also
a'(x'+y) = a'(x') = c' because a' vanishes on J.  As q(x'+y) >= a'(x'+y) (q*(a') = 1), equality holds.  QED

Consequently, in a direction y supported on free coordinates of f' (with room), the whole excess Delta'(y) is block excess,
bounded by Lemma 1.4 for every split; this is the quantitative form of "the free-coordinate part of a mate of an NA row must
be carried by block coordinates" (r2/N2 Prop. 5.2, there for C-tame approximants only).

## What these tools can and cannot do (assessment)
A non-recovery proof must, for EVERY NA f' close to f, exhibit y (in a fixed finite-dimensional space, Remark 1.3) and a scale
with rho|g(x'+y)| > R_{f'}(y) + delta p(x'+y).  Lemmas 1.4-1.5 bound R_{f'}(y) by the "relevant carriers" of f' at that scale and
direction.  The approximant controls which carriers are relevant (values u_k(x') can be moved through x'), so the proof needs a
UNIFORM statement: no x' near xi makes enough carriers relevant in the direction y at the critical scale.  Part 2 shows by an
example that such a statement is FALSE for the most natural switching mechanism (block peaks at all depths): there the
canonical truncations keep all relevant carriers.
