# N3 Part 1 — Fibres at norm-attaining rows: rigidity, switching budget, de-switching

Track N3 (negative direction): can the failure of lower semicontinuity of Part II, Theorem NL (thm:II-NL) and Prop. S3
(prop:II-S3) be made UNIFORM over all norm-attaining (NA) approximants f' -> f?  This part collects the exact structure of
fibres C(f') at NA rows that any such uniformization must use.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Citations: [I, label] = paper/martin_density_note.tex, [II, label] = paper2/martin_density_note_II.tex,
[III, label] = paper3/martin_density_note_III.tex, G3 = r14/G3_notes.md (refereed), N1 = neg/N1_notes.md.

Setting.  I finite, T an arbitrary admissible operator [I, def:admissible] unless stated otherwise.  For f in S_{p*}
the forced data are (xi, q_0, a, w, F, z, zhat = z + Ue, nu, e) [I, prop:forced], K = {j notin F : |z_j| = 1} (contacts),
J = N \ (F u K) (free coordinates), zeta_m = R_m** xi, sigma_m, M_m, C_m, P_m (peaks), Q_m (strict non-peaks),
psi_m := R_m* w_m.  An NA row is f' = grad p(x'), x' in S_p; its data are primed: c' = q(x') (= q_0'), xhat' = x'/c'
= z' + U e' with z' in c_0, a' in c_00, F' = supp a' finite, K' finite (z' in c_0), J' cofinite [I, prop:smooth(c)].
s(t) = (1 + t^2)^{1/2}.  For h in X*, L* h-representations use [I, (Lstar)]: L*W = sum_m R_m* W_m =
sum_{k,m} lambda_{k,m} W_m(k) u_{k,m} in Y, with ||u_{k,m}||_1 <= q*(u_{k,m}) = 1.

## 1.1 Pairs at a scale and the switching vector

DEFINITION 1.1.  Let f in S_{p*}, g in X*, t > 0.  A SCALE-t PAIR for g at f is (B+, Omega+; B-, Omega-) with B+- in l_1,
Omega+- in V*, such that g = B+ + L*Omega+ = B- + L*Omega- and
   max(q*(a + t B+), ||w + t Omega+||_{V*}) = p*(f + t g),   max(q*(a - t B-), ||w - t Omega-||_{V*}) = p*(f - t g).
The SWITCHING VECTOR of the pair is V := B+ - B- = L*(Omega- - Omega+) in L*(V*) subset Y; Delta Omega := Omega- - Omega+.
Scale-t pairs exist for every g and t > 0: by [I, lem:dualball] write f + tg = A + L*W with max(q*(A), ||W||) =
p*(f + tg) and put B+ := (A - a)/t, Omega+ := (W - w)/t (and likewise for f - tg).  (PROVED.)
At an NA row the same definition is used with the primed data.

## 1.2 The switching budget (valid at every row)

LEMMA 1.2 (switching budget).  PROVED.  Let f in S_{p*}, g in X* with g(xi) = 0, t > 0, and
e(t) >= max(p*(f + tg), p*(f - tg)) - 1.  For every scale-t pair:
 (a) sum_{j notin F} [ (1 - |z_j|)|B+_j| + 2 (z_j B+_j)_- ] + sum_{j in F} 2 (z_j B+_j + |a_j|/t)_-  <=  e(t)/(q_0 t);
 (b) sum_{j notin F} [ (1 - |z_j|)|B-_j| + 2 (z_j B-_j)_+ ] + sum_{j in F} 2 (z_j B-_j - |a_j|/t)_+  <=  e(t)/(q_0 t);
 (c) the switching vector satisfies
     sum_{j in J} (1 - |z_j|)|V_j| + sum_{j in K} 2 (z_j V_j)_- + sum_{j in F} 2 (z_j V_j + 2|a_j|/t)_-  <=  2 e(t)/(q_0 t).
For g in C(f) one may take e(t) = s(t) - 1 <= t^2/2, so the right sides are <= t/(2 q_0) and t/q_0.
(This is G3 Lemma 1.4, refereed, in the form used below; the proof is included for completeness.)
Proof.  Side +.  Put A := a + tB+, W := w + tOmega+.  [I, lem:bookkeeping(a)] with h = tg gives
q_0 lin_b(A) + sum_m sigma_m lin_m(W_m) = t g(xi) = 0.  Since q*(A) = 1 + lin_b(A) + G_b(A) <= 1 + e and
N_m(W_m) = 1 + lin_m(W_m) + G_m(W_m) <= ||W||_{V*} <= 1 + e, multiplying by q_0, sigma_m >= 0 and adding (q_0 + sum sigma_m
= 1) gives q_0 G_b(A) + sum_m sigma_m G_m(W_m) <= e; as G_m >= 0, q_0 G_b(A) <= e.  By [I, lem:bookkeeping(b)],
G_b(A) >= Exc(tB+) = sum_j (|a_j + tB+_j| - |a_j| - z_j t B+_j).  For j in F (z_j = sgn a_j) the summand is
2(-z_j t B+_j - |a_j|)_+ = 2t (z_j B+_j + |a_j|/t)_-  (identity |x + y| = |x| + sgn(x) y + 2(-sgn(x) y - |x|)_+).
For j notin F it is t(|B+_j| - z_j B+_j) = t[(1 - |z_j|)|B+_j| + 2(z_j B+_j)_-] (check the cases z_j B+_j >= 0 and < 0).
Dividing by q_0 t gives (a).  Side -: f - tg = (a - tB-) + L*(w - tOmega-), the first-order terms add up to
-t g(xi) = 0, and Exc(-tB-) = t[ sum_F 2(z_j B-_j - |a_j|/t)_+ + sum_{notin F} ((1 - |z_j|)|B-_j| + 2(z_j B-_j)_+) ], giving (b).
(c): on J, (1 - |z_j|)|V_j| <= (1 - |z_j|)(|B+_j| + |B-_j|); on K, (z_j V_j)_- <= (z_j B+_j)_- + (z_j B-_j)_+; on F,
z_j V_j + 2|a_j|/t = (z_j B+_j + |a_j|/t) - (z_j B-_j - |a_j|/t) and (x - y)_- <= x_- + y_+.  Add (a) and (b).  QED

READING (resource table at scale t).  At scale t a row offers: on F, two-sided base usage with an ANTI-SIGN ALLOWANCE
|a_j|/t per coordinate; on K, one-sided usage (sign z_j on side +, -z_j on side -); on J, usage at a first-order price
weighted by the room 1 - |z_j|.  All violations together must have mass O(t) (precisely <= e(t)/(q_0 t)).  At an NA row,
F' contains the BANKS F' \ F (small masses), K' is finite and J' is cofinite.

## 1.3 De-switching at rows with finitely many one-sided coordinates

DEFINITION 1.3 (de-switching modulus).  For f in S_{p*}, M > 0 and r >= 0 put
   omega_f(M, r) := sup{ ||L*Delta||_1 : Delta in V*, ||Delta||_{V*} <= M, sum_{j in J}(1 - |z_j|) |(L*Delta)_j| <= r }.
It is nondecreasing in r and in M.

THEOREM 1.4 (de-switching).  PROVED.  Let f in S_{p*} have F u K finite — in particular every NA row.  Then
 (a) omega_f(M, r) -> 0 as r -> 0+, for every M > 0;
 (b) for g with g(xi) = 0 and every scale-t pair with ||Delta Omega||_{V*} <= M:  ||V||_1 <= omega_f(M, 2e(t)/(q_0 t));
 (c) consequently, if g in C(f), t_n -> 0+ and the scale-t_n pairs have bounded block coefficients
     (sup_n ||Delta Omega_n||_{V*} < infinity), then ||V_n||_1 -> 0: bounded-coefficient switching dies out as t -> 0.
Proof.  (a) Suppose omega_f(M, r) >= c > 0 for all r > 0.  Choose Delta_n with ||Delta_n|| <= M, leakage
sum_J (1 - |z_j|)|(L*Delta_n)_j| <= 1/n and ||L*Delta_n||_1 >= c/2.  V* is the dual of the separable space V (finite
l_1-sum of copies of l_1 with equivalent norms), so a subsequence converges weak* to some Delta.  L : X -> V is compact
[I, Sec. 1.2], hence L* maps bounded weak*-convergent sequences to norm-convergent ones; so L*Delta_n -> L*Delta in l_1
and ||L*Delta||_1 >= c/2.  For j in J, (1 - |z_j|) |(L*Delta)_j| = lim_n (1 - |z_j|)|(L*Delta_n)_j| = 0 and
1 - |z_j| > 0, so (L*Delta)_j = 0.  Hence L*Delta is supported in the finite set F u K.  By [I, (Lstar)], L*Delta in Y,
so L*Delta in Y n c_00 = {0} by (T-c): contradiction.
(b) V = L*(Delta Omega) and Lemma 1.2(c) bounds its leakage by 2e(t)/(q_0 t).  (c) e(t) <= t^2/2, so the leakage
bound is <= t_n/q_0 -> 0; apply (a), (b) with M := sup_n ||Delta Omega_n||.  QED

COROLLARY 1.5 (migration of persistent switching to deep carriers).  PROVED.  Let f have F u K finite, g in C(f),
t_n -> 0+, and scale-t_n pairs with ||V_n||_1 >= c > 0 for all n.  Then for every finite set Lambda of carriers (pairs
(k, m)), the weighted coefficient mass outside Lambda,
   D_n(Lambda) := sum_{(k,m) notin Lambda} lambda_{k,m} |Delta Omega_n(k,m)|,
does not tend to 0 along any subsequence.  (Persistent switching at such a row runs through carriers outside every fixed
finite set, with total weight bounded below; since |Delta Omega_n(k,m)| <= (4 + 2e(t_n))/t_n, these carriers have
weights comparable to or below the scale.)
Proof.  Suppose D_n(Lambda) -> 0 along a subsequence.  Split Delta Omega_n = Delta^Lambda_n + Delta^rest_n (restriction to
Lambda and to its complement).  ||L*Delta^rest_n||_1 <= D_n(Lambda) -> 0 (as ||u_{k,m}||_1 <= 1).  Put r_n :=
||L*Delta^Lambda_n||_1; then r_n >= ||V_n||_1 - D_n >= c/2 eventually.  The vectors Delta^Lambda_n / r_n lie in the
finite-dimensional space of Delta supported in Lambda, on which Delta -> ||L*Delta||_1 is a norm (L* is injective on V*,
[I, (Lstar)]); so they are bounded, and a subsequence converges to Delta_inf with ||L*Delta_inf||_1 = 1.  Its leakage is
lim (leakage(V_n) + ||L*Delta^rest_n||_1)/r_n = 0 (Lemma 1.2(c)), so as in Theorem 1.4 L*Delta_inf in Y n c_00 = {0}:
contradiction.  The bound on |Delta Omega_n(k,m)| follows from ||w +- t Omega+-||_{V*} <= 1 + e(t) and ||w||_{V*} <= 1. QED

REMARKS 1.6.
 (a) Theorem 1.4 is the scale-quantitative form of [II, cor:II-S2] (exact data at NA rows never switch) and of
     [I, prop:exact], [I, cor:twosided] (exact transfers need infinite one-sided sets).  It holds at EVERY NA row, with no
     tameness assumption on the blocks (infinitely many strict non-peaks, degenerate peaks, failure of (MS) are allowed).
 (b) At rows with K infinite the modulus need not vanish: for the row of [I, thm:defect], the exact resonance
     v = c u_{2,1} (supported on {1} u K_0, z-signed) gives omega_f(M, 0) >= ||v||_1 > 0 for M >= c/lambda_0.
 (c) The modulus depends on the row: for the canonical truncations f_N of a row f with an exact resonance V_inf
     (bounded coefficients Delta_inf), omega_{f_N}(M, r) >= ||V_inf||_1 as soon as r >= ||V_inf 1_{K n (N,inf)}||_1
     (the truncated contacts become free coordinates with room 1).  So the DE-SWITCHING SCALE of an approximant —
     the scale below which bounded switching of size c is impossible — tends to 0 as the approximant keeps more contacts.
     (PROVED: the leakage of V_inf at f_N is exactly its mass on K n (N, inf), since V_inf vanishes on J and z^N = z on
     [1, N].)

## 1.4 Infinitesimal rigidity of mates at C-tame NA rows (the mechanism of Theorem NL)

PROPOSITION 1.7.  PROVED (assembled from [I, thm:tamefibre], [I, prop:lowerbound], [I, rem:onesided(a)],
[II, cor:II-S2]).  Let f' = grad p(x') be NA with C-tame normer (every Q'_m u Dg'_m finite and (MS) at x'; F', K' finite
automatically).  Then:
 (a) C(f') subset S(f'): every mate is g' = b' + sum_m R_m*(omega'_m - d'_m(omega'_m) w'_m) with supp b' subset F',
     b'(x') = 0, omega'_m in c_00(Q'_m); the data (b', omega') are unique.  So C(f') is finite dimensional.
 (b) If there are no degenerate peaks, Gamma'_w(g') := c' h'(b') + sum_m sigma'_m H'_m(omega'_m) <= 1, and
     gamma'^+(g') = gamma'^-(g') = Gamma'_w(g') (no re-splitting gain at t -> 0).
 (c) PROFILE: with Sigma'(f') := F' u U_m U_{k in Q'_m} supp u_{k,m} and psi'_m := R_m* w'_m,
        g' = - sum_m d'_m(omega'_m) psi'_m   on N \ Sigma'(f').
     For one block: g'/psi' is constant on {j notin Sigma'(f') : psi'_j != 0}.
 (d) (radius) If g' in S(f') has a max-form coefficient H(c') <= 1 - delta for its unique data c' = (b', omega'), then
     p*(f' + t g') <= s(t) for |t| <= r_*(c', delta) [I, lem:slack(b)], and the radius satisfies
     r(c') <= min_{j in F', b'_j != 0} |a'_j| / |b'_j|: a mate that uses a bank j two-sidedly has radius at most
     (bank mass)/(coefficient).
Proof.  (a) [I, thm:tamefibre] at eta = x'.  (b) [I, prop:lowerbound] (its hypotheses: a' in c_00, K' finite, Q'_m finite,
no degenerate peaks, (MS)) and [I, rem:onesided(a)].  (c) For j notin Sigma'(f'), b'_j = 0 and (R_m* omega'_m)(j) =
sum_{k in Q'_m} lambda_{k,m} omega'_m(k) u_{k,m}(j) = 0.  (d) Definition of r(c) [I, def:certificate] (term 1/||b/a||_inf).
QED

This is exactly the mechanism of [II, prop:II-S3]: if a finite set S with non-constant profile of g avoids Sigma'(f'),
then dist_{l_1}(rho g, C(f')) >= (oscillation of rho g on S relative to span{psi'_m}).  The mechanism is INFINITESIMAL
(it concerns the unique data, i.e. t -> 0) and it is void on F' (banks) and on the supports of strict non-peaks.

## 1.5 Banks are contact-like above their capacity scale

PROPOSITION 1.8 (bank capacity).  PROVED.  Let f' be NA, Bk subset F' any set of support coordinates ("banks") and
mu := sum_{j in Bk} |a'_j|.  For every g' in C(f'), t > 0 and scale-t pair at f':
   sum_{j in Bk} (z'_j B+_j)_- <= mu/t + t/(4c'),     sum_{j in Bk} (z'_j B-_j)_+ <= mu/t + t/(4c').
Moreover, along every sequence of NA rows f'_n -> f the off-F masses mu_n := sum_{j notin F} |a'_n(j)| tend to 0, and
min_{j in F} |a'_n(j)| -> min_F |a_j| > 0.  Hence at every fixed scale t (and at all scales t_n >> mu_n) the banks of
approximants are used one-sidedly, like contacts with sign z'_j = sgn a'_n(j), up to an anti-sign mass mu_n/t + O(t).
Proof.  (x)_- <= (x + c)_- + c for c >= 0; apply with x = z'_j B+_j, c = |a'_j|/t, sum over Bk and use Lemma 1.2(a) at f'
(e <= t^2/2): sum_{F'} 2(z'_j B+_j + |a'_j|/t)_- <= t/(2c').  Side - likewise.  a'_n -> a in l_1 by
[I, prop:approximants] / [I, prop:continuity], which gives the last claims.  QED

## 1.6 What NA rows can do (far freedom), for the record

 * [I, prop:approximants], N1 Lemma 1.4 (PROVED): NA rows near f are grad p(z' + U(U*a'/||U*a'||)) with a' close to a in
   l_1 (tiny banks anywhere allowed), z' close to z on a window [1, W] and ARBITRARY in B_{c_0} beyond W (subject to
   z' = sgn a' on supp a').  So an approximant may keep the contacts of f up to any finite depth N'', create contacts or
   near-contacts anywhere finitely, bank any finite set, and move far free coordinates two-sidedly.
 * Exact zero-weight strict non-peaks can be created on finitely many generic tail carriers by o(1) window moves
   (R3 Theorem EC, refereed; for finitely many carriers this is linear algebra on c_00(J) by [I, lem:rigidity(b)]).
 * NA rows need not be C-tame (e.g. if infinitely many u_{k,m} vanish at x'); then fibres can be infinite dimensional,
   but Lemma 1.2, Theorem 1.4, Corollary 1.5 and Proposition 1.8 still apply.  (Existence of such rows near a given f
   for a given T is OPEN in general and not needed.)

## Summary of Part 1
At an NA row: (i) one-sided resources are finite (K' finite), so bounded-coefficient switching dies out as t -> 0
(Theorem 1.4) and persistent switching must migrate to deep carriers (Corollary 1.5); (ii) at C-tame NA rows the mates are
rigid finite certificates with constant profile off Sigma'(f') (Prop. 1.7) — the mechanism of Theorem NL; (iii) banks give
two-sided freedom only below the scale (bank mass)/(coefficient) and are contact-like above it (Prop. 1.8).
