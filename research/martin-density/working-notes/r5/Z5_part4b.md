# Z5 part 4b: the obstruction for infinite F without room (support swallowing), and what can be transported

Setting: SLD operator unless stated, f arbitrary, s_j = sgn a_j on F, alpha(M) = sum_{j in F, j>M}|a_j|, v_l := delta_l h_l/n_l (the
signature part of u_l on S_l, (P1)), and for a carrier l with S_l cap F infinite the RATIO PROFILE
  varrho_l(j) := |a_j| / v_l(j)   (j in S_l cap F).

## 4.5 Support-swallowed signature sets. Definitions.
A carrier l is SUPPORT-SWALLOWED if S_l \ F is finite (so the off-support room r_l of Lemma lem:signmixed, computed on S_l \ F,
carries at most finitely many coordinates); it is CUSHION-DOMINATED if moreover inf_{j in S_l cap F} varrho_l(j) > 0, i.e.
|a_j| >= c v_l(j) on S_l cap F; it is FAST-SWALLOWED if varrho_l(j) -> 0 along S_l cap F.
(The note's Remark rem:Binf / rem:openZ case (O4) "infinite F without room" consists of first rows having support-swallowed carriers
(or carriers whose room off F decays too fast, which is case (O1)(i) with F infinite).)

## 4.6 What the base can pin for a support-swallowed carrier. PROVED (exact arithmetic of the constraint system).
The only base information on Delta theta_l available to pinning arguments (Lemmas lem:switchbudget, lem:flip, 2.7) consists of the
inequalities, for j in S_l cap F (where -Delta B(j) = Delta theta_l v_l(j) + r_l(j), r_l from finer carriers),
  (s_j Delta B(j))_- <= 2|a_j|/t + f^+_j + f^-_j,   sum_j (f^+_j + f^-_j) <= t/(2q_0).                         (4.1)
Lemma 4.6. Let l be support-swallowed, S := S_l cap F, and suppose s_j = epsilon (constant) on S (monochromatic) [resp. both signs occur
infinitely often on S (sign-mixed)]. Given t > 0 and D >= 0 put Phi_l(D, t) := sum_{j in S} (D v_l(j) - 2|a_j|/t)_+.
(a) Take r_l = 0 (no finer carriers). In the monochromatic case s_j Delta B(j) = -epsilon Delta theta_l v_l(j), so the left side of
(4.1) is (epsilon Delta theta_l)_+ v_l(j): the direction epsilon Delta theta_l > 0 (switching amplitude tau_l = -epsilon Delta theta_l < 0 in
the notation of Theorem thm:S) is constrained, the other is free. The system (4.1) is satisfied by Delta theta_l := epsilon D (D >= 0) with
f^+_j + f^-_j := (D v_l(j) - 2|a_j|/t)_+, and by no smaller choice of the f's, so it is solvable iff Phi_l(D,t) <= t/(2q_0). In the sign-mixed
case both directions are constrained, each by the sum over the coordinates of the corresponding sign class. Hence the largest amplitude in
the constrained direction compatible with (4.1) is D*_l(t) := sup{D : Phi_l(D,t) <= t/(2q_0)} (sum restricted to the sign class).
(b) If l is cushion-dominated (varrho_l >= c > 0 on S), then Phi_l(D,t) <= sum_j (D - 2c/t)_+ v_l(j) = 0 for D <= 2c/t, so
D*_l(t) >= 2c/t, which exceeds the box bound 6 lambda_l/t of Lemma lem:box as soon as c >= 3 lambda_l. The base pins nothing; the
carrier is two-sided free through the cushions (its full box range of switching is absorbed by support coordinates without flips).
(c) If varrho_l(j) = kappa v_l(j)^beta-type decay holds, e.g. v_l(j) = c_0 2^{-j}, |a_j| = 2^{-(1+beta) j} on S (beta > 0), then
D*_l(t) is of order t^{(1-beta)/(1+beta)} up to constants depending on l (for beta = 1: of order 1), so D*_l(t)/t -> infinity: the base
pins the carrier only at a scale-dependent constant K_l(t) := D*_l(t)/t -> infinity.
Proof. (a) and (b) are contained in their statements (the minimal admissible f_j at j is (D v_l(j) - 2|a_j|/t)_+; sum over j).
(c) For S = {j >= j_0}: Phi_l(D,t) = sum_j (D c_0 2^{-j} - 2^{1-(1+beta)j}/t)_+; the summand is positive iff 2^{-beta j} < D c_0 t/2, i.e.
j > J := log_2(2/(D c_0 t))/beta, and then the sum is between constant multiples of D 2^{-J} = D (D c_0 t/2)^{1/beta}. Setting this equal
to t/(2q_0) gives D^{(1+beta)/beta} ~ t^{1 - 1/beta}, i.e. D*_l(t) ~ t^{(beta-1)/(beta+1)} = t . t^{-2/(1+beta)}. QED
Remark. Lemma 4.6 is a statement about the method: pinning arguments that use only the base budget cannot give |Delta theta_l| = O(t)
uniformly in t for fast-swallowed carriers; window averaging needs a pinning constant K with n^w_l >> K on whole windows of
super-exponential length (Theorem thm:windowed), and K_l(T_lo(l)) is then astronomically large. (This is Remark 2.10 again.)

## 4.7 Bounded (not pinned) switching through support-swallowed carriers. PROVED.
By Lemma 4.3, if all carriers outside a finite set U are pinned on a window (sum_{notin U}|Delta theta| <= K t), the switching through U is
BOUNDED by C_U(1 + K t), whatever F. Bounded switching through a support-swallowed carrier l has a well-defined flip profile:
Lemma 4.7 (flip cost of fixed data at support coordinates). Let b in l_1 and define, for each sign side, the anti-direction parts
beta^+_j := (s_j b_j)_- and beta^-_j := (s_j b_j)_+ (j in F). For r > 0,
  sum_{j in F} (|a_j + r b_j| - |a_j| - s_j r b_j) = sum_{j in F} 2(r beta^+_j - |a_j|)_+ <= 2 r sum{beta^+_j : |a_j| < r beta^+_j} =: 2r m^+(r),
and the same for r < 0 with beta^- (and |r|). In particular, if (CS) m^+(x) = o(x) as x -> 0 (cushion sparsity), the flip cost of the
data is o(r^2).
Proof. |x + y| - |x| - sgn(x) y = 2(-sgn(x) y - |x|)_+ (Lemma lem:base); the summand is positive only if |a_j| < r beta^+_j, and then
it is at most 2 r beta^+_j. QED
Examples. For the data b = -epsilon D v_l 1_S (bounded switching amplitude D through a support-swallowed l) one has
m^+(x) = D sum{v_l(j) : varrho_l(j) < x D}. With v_l(j) ~ 2^{-j}: varrho_l(j) = 1/j gives m(x) ~ 2^{-1/(Dx)} = o(x) ((CS) holds);
|a_j| = 2^{-2j} (varrho ~ 2^{-j}) gives m(x) ~ D^2 x (borderline: flip cost of exact order r^2); |a_j| = 2^{-3j} gives m(x) ~ x^{1/2}
((CS) fails: flip cost >> r^2).

Proposition 4.8 (Theorem 3.2 under cushion sparsity). In Theorem 3.2 the hypothesis (R-inf) may be replaced by
  (CS-data) for each of beta^theta_j := |b^theta_j|, beta^+_j := (s_j b^+_j)_-, beta^-_j := (s_j b^-_j)_+ (j in F):
            m(x) := sum{beta_j : j in F, |a_j| < x beta_j} = o(x) as x -> 0.
Proof. In the claim of Step 3 of Part 3 the support coordinates j in F cap [1, N_w] may now flip; using |a'_j| >= |a_j|/2 and
|1 - tau rho c| >= 1/2, the summand of Exc' at such j is at most 2(|tau| rho beta^diamond_j - |a_j|/4)_+ <= 2|tau| rho beta^diamond_j
1[|a_j| < 4 rho |tau| beta^diamond_j], so the total flip cost is <= 2 rho |tau| m(4 rho |tau|) = o(tau^2), uniformly in N_w (the sum over
F cap [1, N_w] is bounded by the sum over F). Choose T_0 so small that this is <= delta tau^2/16 for |tau| <= T_0 (for diamond = theta
the relevant range is |tau| <= s_1 <= T_0). In units of tau^2/2 this adds delta/8 to the bound of Step 5 of the note, which reads
rho^2 kappa_w + delta/8 + delta/8 + delta/8 + delta/4 = 1 - 2delta + 5delta/8; the new total 1 - 2delta + 3delta/4 is still <= 1 - delta.
Since Ghat_b must only dominate G'_b, the flip cost is simply added to Ghat_b; nothing else changes. QED

## 4.8 Where exactly the window method fails for support swallowing: deep flips. PROVED (as a statement about the construction).
Exact two-piece data (b^+, omega^+), (b^-, omega^-) must satisfy b^+ - b^- = X with X a finite block combination; and to be usable at
scale t (Lemma lem:onesidedtransfer, read at arbitrary F with the flip cost of Lemma 4.7) they must satisfy, at every support coordinate,
the one-sided cushion bounds (s_j b^+_j)_- <= A_j, (s_j b^-_j)_+ <= A_j with A_j = O(|a_j|/t) (or a (CS)-type sparsity of violations).
Lemma 4.9 (common shift). Let x, y, A be reals with A >= 0. There is sigma with x - sigma >= -A and y - sigma <= A iff x - y >= -2A, and
then one can take |sigma| <= (y - A)_+ + (-x - A)_+. [Proof: the admissible sigma form the interval [y - A, x + A].]
Consequently, given a decomposition at scale t with one-sided cushion data B_+- (Lemma 2.7) and an exact switching vector X, common
shifts on F (which keep b^+ - b^- = X) produce exact cushion bounds iff (s_j X_j)_- <= 2A_j at every j in F, at an l_1 cost
sum_j [(s_j B_-(j) - A_j)_+ + (-s_j B_+(j) - A_j)_+ + |(Delta B - X)_j|] = O(t + ||Delta B - X||_1).
(i) If X is supported, on F, in a finite set, or has bounded ratio |X_j| <= C|a_j|/t on F, the shifts exist with A_j := max(2, C)|a_j|/t:
this is the case of bad carriers whose F-parts are finitely supported or cushion-dominated (hypothesis (H4-inf) of Part 5).
(ii) If X contains bounded or box-sized switching through a fast-swallowed carrier, the condition (s_j X_j)_- <= 2A_j fails at the far
coordinates of S_l cap F (|a_j| << t v_l(j)); there the decomposition at scale t itself is "deeply flipped": by (4.1) the true switching
satisfies (s_j Delta B(j))_- <= 2|a_j|/t + f^+_j + f^-_j, so a deep violation means f^+_j + f^-_j >> |a_j|/t, i.e. the decomposition pays
flips at that coordinate at scale t. Data reproducing such a pattern at smaller scales r << t pay the flips at a first-order rate:
by Lemma 4.7 the cost at scale r is about 2 r sum{f_j : |a_j| < r f_j}, which is not o(r^2) in general (e.g. one coordinate with
f_{j_0} ~ t and |a_{j_0}| << t^2 gives cost ~ 2 r t for r in (|a_{j_0}|/t, t)). Hence fixed data cannot reproduce deep flips; the mate must
switch differently at different scales. This is precisely the "exactness vs scale" phenomenon of case (O1)(i), with the role of
near-contacts (|z_j| -> 1 off F) played by support coordinates with |a_j| -> 0.

## 4.9 The reduction question: status. 
(A) Soft reduction along truncations (contact truncations f^M of 4.1). What transfers, PROVED: pure base mates (Lemma 4.1), all finite
certificates (Theorem thm:transport: it holds along every sequence f_n -> f, in particular along truncations; its base part uses
G_n := {j in F : ...}, valid for infinite F since (C1) requires ||b/a||_inf < infinity), finitely based Gamma_w-certificates (Theorem 1.2,
along the truncated canonical approximants), every mate carrying cushion-compatible (or (CS)) two-piece data with Delta d >= 0 or (SC)
(Theorem 3.2 / Proposition 4.8: along engineered truncations with finite base support). What does NOT follow: for a general mate, the
transplanted decompositions of f at scale t cost, at f^M, the far cushion usage 2 sum_{j in F, j>M} min(|a_j|, t (anti-usage)_j) <= 2 alpha(M)
(PROVED, by the flip identity: a support coordinate turned into a contact of the same sign loses exactly its allowance), which is <= eps t^2
only for t >= (2 alpha(M)/eps)^{1/2}; below that scale the mates of f may use the far cushions symmetrically (both pieces against the
respective free directions, Lemma 2.7), which no contact sign can reproduce. A reduction "Lemma Z for finite F implies Lemma Z for all F"
along truncations is therefore EQUIVALENT to a lower-semicontinuity statement of the same type as case (O2) (lsc of mates when far
two-sided resources are made one-sided), and is OPEN.
(B) Design. No admissible design (SLD or other) can exclude support swallowing: F = supp a is arbitrary (F = N is allowed, and the
first rows with supp a = N are comeagre), and every signature vector v_l is in l_1, so for every design there are a in S_{q*} with
|a_j|/v_l(j) -> 0 on S_l, for all l simultaneously. Signatures with both signs relative to sgn a (sign-mixed) pin from both sides but with
the same scale-dependent constant (Lemma 4.6(c) applies to each sign class). So designs cannot remove (O4); they can only shape it.
(C) a in Y. For the SLD operator a in Y is possible (e.g. a = u_l, F = supp y_l cup S_l), so Lemma lem:rigidity(a) (uniqueness of data with
base parts in F cup K) fails at infinite F; but Lemma 4.3 shows that this does not affect bounded switching: the direction a is pinned at
first order (|Delta B(zhat)| <= t/q_0). The genuinely new freedom at infinite F is not a in Y but the two-sided cushions, i.e. block
combinations supported (essentially) inside F with ratios to |a| unbounded (fast swallowing).
(D) Precise obstruction. A first row f with infinite F lies outside every recoverable class proved so far only if, on all late windows,
some mate switches through carriers that are (i) not pinned off F (no or decaying room on S_l \ F, cases (O1)-(O3)), or (ii) support-
swallowed and not cushion-dominated (fast-swallowed), with switching that is not of bounded (CS)-type (Lemma 4.7, Proposition 4.8).
Case (ii) is case (O1)(i) with near-contacts replaced by small support coordinates: the cushion allowance 2|a_j|/t plays the role of the room.
