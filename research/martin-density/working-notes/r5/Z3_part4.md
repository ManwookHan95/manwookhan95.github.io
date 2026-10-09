# Z3 part 4 — consequences for (O1)(i): approximate swallowing

SLD operator, N >= 1, F finite throughout. Rooms r_l (sign-mixed rooms of Theorem thm:Bpm), r*_l (Definition def:swallowed).

## 4.1 Proposition ((O1)(i) is an infinitely-many-carriers phenomenon). PROVED.
(a) If F is finite, every r_l > 0, and r_l >= varpi^l delta°_l for all but finitely many l (some varpi in (0,1]), then f in R_0^+- subset Rec.
(b) If B is finite and f satisfies (H2), (H3), and r*_l >= varpi^l delta°_l for all but finitely many good l, then f in R_S subset Rec.
In particular near-contact tails or far sign changes on FINITELY many signature sets never obstruct recovery, however fast |z_j| -> 1
there: the obstruction (O1)(i) requires infinitely many carriers whose relative rooms r_l/delta°_l decay faster than any geometric
sequence along every subsequence (failure of (W+-), resp. (W*)).
*Proof.* (a) For the finitely many exceptional l the factors 1 + 3/r_l contribute a constant C_0 to Lambda^+-_f(l); for the others
1 + 3/r_l <= (3/(2 varpi^l))(1 + 2/delta°_l) as in the proof of Theorem thm:Bpm. Hence Lambda^+-_f(l) <= C_0 (3/2)^l varpi^{-l^2} Lambda°(l)
and (W+-) holds; Theorem thm:Bpm. (b) Same computation for Lambda*_f (bad factors are 1 + 3/(2||v_l 1_{S_l\F}||) <= 1 + 2/delta°_l
up to a constant, and only finitely many l are bad); (W*) holds; Theorem thm:S (case B_fin). QED

## 4.2 Proposition (reduction of (O1)(i) to lower semicontinuity along far lowerings). PROVED.
Let F be finite, B finite, and let f satisfy (H2), (H3) (vacuous if B is empty). For L so large that S_l cap F = {} and l notin B for
l > L, let f^L be the far lowering of Remark rem:openZ(O2) (z^L := 0 on union_{l>L} S_l). Then f^L in R_S (in R_0^+- if B is empty), and
f^L -> f. Consequently, at every (O1)(i) point of this kind, Lemma Z holds for (f, g, rho) as soon as dist(rho g, C(f^L)) -> 0 along
some L -> infinity: (O1)(i) is contained in the lower-semicontinuity question (O2).
*Proof.* f^L has base part a and z^L = sgn a on F, so it is a companion of f; z^L -> z coordinatewise, so f^L -> f (Remark rem:openZ(O2)).
At f^L the room of S_l, l <= L, is that of f (the S_l are disjoint and z^L = z on S_l), and for l > L it is ||v_l 1_{S_l}||_1 = delta°_l
(S_l cap F = {}, z^L = 0 there). Hence only the finitely many rooms with l <= L can be small, and the bad set of f^L is B. If B = {}, all
rooms of f^L are positive and 4.1(a) gives f^L in R_0^+-. If B != {}: (H2) at f^L for L large — a good non-degenerate peak k°_m of f has
positive margin, which persists along f^L -> f (Proposition prop:continuity and Lemma lem:threshold), and its carrier stays good (its room
is unchanged); (H3) at f^L for L large — a bad carrier k(l) of f is either a strict non-peak with positive gap (persists), or a
non-degenerate peak (persists, with the same sign), or a degenerate peak with sgn w_m(k(l)) = -eps_l by (H3) at f; since w^L_m(k(l)) ->
w_m(k(l)) != 0, if it is a degenerate peak of f^L its sign is still -eps_l. So (W*) holds at f^L by 4.1(b) and f^L in R_S. QED

## 4.3 The companion route and its exact limits. PROVED (as statements about the method of parts 2-3).
Corollary 3.4 recovers f when, for infinitely many windows W(l_j), the coarse carriers split into
  pinned:      r*_l large enough that Lambda* (product over pinned coarse l) satisfies K_* T_hi -> 0, n^w/K_* -> infinity;
  exactified:  c(delta_j) <= theta_j T_lo(l_j)^2, theta_j -> 0, with well-conditioned companion cones (HF).
For a carrier exactified by raising (case (a)) or flipping (case (b)) on S_l, Lemma 3.1 gives c(delta) >= min(lambda_l, |u_l(delta)|) >=
min(lambda_l, r_l) up to constants (|u_l(delta)| = removed room of S_l, Lemma 1.4). Hence:
 (i) [Room gaps suffice] If there are infinitely many j such that every coarse l <= l_j has either r*_l >= rho_j or r_l <= theta_j
     T_lo(l_j)^2 (with lambda_l-weighted targets ignored), with prod_{l <= l_j, r*_l >= rho_j} (1 + 3/r*_l) = o(l_j 2^{l_j^3} Lambda°(l_j)),
     and the companion cones are well conditioned, then f in Rec. This needs "tower gaps": r_{next} <= exp(-C prod(1/r)) infinitely often.
 (ii) [The band] If, for all large windows, some coarse carrier has room in the band
          theta T_lo(l_*)^2 << r_l << 1/K_*(l_*),
     the method fails at that window: pinning needs n^w >~ 1/r_l, exactification needs r_l << T_lo^2 = 4^{-n^w} T_hi^2. Example: r_l =
     2^{-l^4} delta°_l for infinitely many l in one block: every window W(l_*) contains band carriers (2^{-l^4} >> 4^{-n^w_{l_*}} for l <= l_*,
     and prod_{l<=l_*} 2^{l^4} >> 2^{l_*^3}). The band is intrinsic to window methods: with any design whose windows have length n(l),
     pinning costs n >~ 1/r and exactification needs r << 4^{-n}; rooms r_l ~ 1/n(l)^2 lie in the band of every window. So no choice of
     design removes it (cf. Remark rem:nodesign for the first-order version).
 (iii) [d-neutral carriers] If the exactified carriers of a block are d-neutral at f and carry positive defect, every companion with the
     same base part has q^#_l > 0 for all of them (Lemma 1.4), so its cone forces tau' = 0 in that block and C^#_H >= c/min r_l: the
     companion buys nothing over pinning. Re-tuning the Hilbert part (moving a, possibly with tiny masses on contacts unused by the data, so
     that u_l(zhat^#) = 0 again) removes this obstruction for finitely many carriers per window at cost ~ ||Gram^{-1}|| max r_l
     (SKETCH: the masses must avoid the supports of the window data so that a_min plays no role in Lemma U).

## 4.4 What remains of (O1)(i) (precise statement). OPEN.
After 4.1 and 4.2, (O1)(i) is the following special case of (O2): F finite, infinitely many carriers with positive rooms r_l (or r*_l)
whose relative rooms decay super-geometrically (failure of (W+-)/(W*)) with no tower gaps; the mate g switches through infinitely many
of them at scales t in [sqrt(lambda_l r_l), C lambda_l] (the "free regime" of carrier l: |Delta theta_l| <= min(t/(q_0 r_l), 6 lambda_l/t)).
Remaining step: a recovery mechanism for switching through a carrier in its free regime that tolerates its first-order defect
tau_l r_l <= 6 lambda_l r_l/t, i.e. either (A) lower semicontinuity dist(rho g, C(f^L)) -> 0 along far lowerings (4.2), or (B) a variant of
windowed averaging in which a carrier's frozen error enters through log(1/r_l) instead of 1/r_l (the obstruction in (ii) is the single
scale t ~ sqrt(lambda_l r_l), where the pieces carry switching ~ sqrt(lambda_l/r_l) = t/r_l; an averaging scheme that excludes these
scales must still cover them at the coarser scales, where their frozen error enters through (B')).
