# N3 notes — Can the failure of lower semicontinuity of Theorem NL be made UNIFORM over all norm-attaining approximants?

Track N3 of the negative direction (user question: "이정도로 돌렸는데 증명이 안된다면 negative로 접근해야 하는 거 아닐까").
Sources: Part I (paper/martin_density_note.tex), Part II (paper2/martin_density_note_II.tex: Lemma S, Cor S1/S2, Prop S3,
Theorem NL), Part III (paper3/martin_density_note_III.tex: Theorem UE, E^eng, levers), U3 + U3-referee (r8/), G3 (r14/),
N1 (neg/N1_notes.md).  Part files: neg/N3_part1.md, N3_part2.md, N3_part3.md (reproduced below, authoritative); scripts in
neg/N3_work/.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Every item labelled PROVED has a complete proof below or
is cited from a refereed source.

## 0. Answer and summary

요약 (Korean).  Theorem NL의 비하반연속성을 "모든" norm-attaining 근사열에 대해 균일하게 만드는 것은 불가능하다는 것이
메커니즘 수준에서 증명된다.  (1) NL의 핵심인 프로파일(oscillation) 제약은 사실 모든 행(row)에서 모든 mate에 대해 성립하는
양의 스케일 선형 샌드위치(정리 2.3)이며, 은행(bank) 질량 mu에 대해 Osc <= 2(2A mu)^{1/2} 꼴의 sqrt(mu) 법칙을 준다
(수치적으로 상수 1.22로 5자릿수 범위에서 확인).  (2) 이 제약은 f 자신이 이미 만족하므로 근사열에 "상속"되고(따름정리 2.5),
f의 접촉 구조를 깊이 N까지 복사하고 S에 작은 은행을 두는 근사열이 모든 근방에서 이 메커니즘을 무력화한다(정리 2.6(b);
f의 자유좌표가 유한한 경우 — NL이 실현되는 self-aligned 행 포함 — 완전 증명, 일반적인 경우 SKETCH).  (3) 남는 것은
회복하는 근사열이 반드시 가져야 할 구조(정렬 또는 은행, de-switching, 은행 질량 >~ kappa x de-switching 스케일)이고,
engineered 근사열이 이를 상수배까지 정확히 만족한다(정리 3.1).  (4) 따라서 이 경로의 negative 증명은 de-switching 스케일에서의
"hand-over(접합)"에서만 가능하며, 그것은 일방향 레버에 대한 1차 Farkas 장애 + 원거리 양방향 레버의 약함(명제 3.3)을 요구한다 —
즉 positive 쪽을 막고 있는 "exactness vs one-sidedness"와 정확히 같은 지점이다.  결론: NL을 균일화하는 negative 접근은
실패한다(증명됨); negative로 가려면 hand-over 인증서(문제 3.4)를 겨냥해야 하며, 그런 예는 알려져 있지 않다.  판단: 약하게
positive 쪽(밀도), 낮은 확신.

ANSWER (English).
 (1) Theorem NL cannot be made uniform over all NA approximants: its mechanism (the profile sandwich) is a positive-scale
     LINEAR constraint satisfied by every mate at every row (Theorem 2.3), it is inherited from f (Corollary 2.5), and in every
     neighbourhood of f there are NA rows (truncation of f's contact pattern at a large depth + banks of mass of order the
     visibility weight of the approximant's free coordinates) at which every lower bound it produces is <= o(1)
     (Theorem 2.6(b): PROVED when f has finitely many free coordinates — this covers the self-aligned rows where NL is
     realized — SKETCH in general).
 (2) The uniform content of NL is a sharp NECESSARY STRUCTURE of recovering NA approximants: aligned-or-banked with the
     quantitative threshold mu_S >= kappa^2/(10 A) (Theorem 2.6(a)); de-switching of bounded switching at every NA row
     (Theorem 1.4) and migration of persistent switching to deep carriers (Corollary 1.5); banks >~ kappa x (de-switching
     scale) below the hand-over (Theorem 2.7, Corollary 2.8).  The engineered approximants of [I, thm:engineered] saturate all
     of these up to absolute constants (Theorem 3.1) — positive evidence.
 (3) The only feature of NA approximants that is NOT inherited from f is the hand-over at the de-switching scale.  A
     non-density certificate of this type must be a JUNCTION certificate (Problem 3.4, OPEN): banks move the switching
     carriers' values at first order (Prop. 3.2), far two-sided levers are too weak by the factor s_1/lambda (Prop. 3.3), so a
     certificate needs a Farkas obstruction against the one-sided resources at moderate depth plus far rigidity of T.  This
     is exactly the consensus core "exactness versus one-sidedness", now localized; no example is known.
 Leaning: POSITIVE (density more likely), low confidence for arbitrary admissible T.  The negative approach via
 uniformizing NL is closed; a negative programme should target Problem 3.4 with an adversarial T (non-diagonal U, far-rigid
 tails, maximal-contact rows, deep switching), not profile functionals.

| # | Result | Status | Where |
|---|---|---|---|
| 1 | Switching budget at every row (scale-t pairs) | PROVED (= G3 L1.4) | Lemma 1.2 |
| 2 | De-switching at rows with F u K finite (all NA rows), modulus omega_f | PROVED | Thm 1.4 |
| 3 | Persistent switching at NA rows migrates to deep carriers | PROVED | Cor 1.5 |
| 4 | Infinitesimal rigidity and profile constancy at C-tame NA rows (NL mechanism) | PROVED (cited) | Prop 1.7 |
| 5 | Banks are contact-like above their capacity scale | PROVED | Prop 1.8 |
| 6 | Collective motion of weighted peaks at every scale | PROVED (+numerics) | Lemma 2.2 |
| 7 | Positive-scale profile bound at every row; sqrt(mu) law | PROVED (+numerics) | Thm 2.3, Cor 2.4 |
| 8 | Cor S1 without two-piece data (exact visibility) | PROVED | Cor 2.4 |
| 9 | Uniform lower bound is inherited from f | PROVED | Cor 2.5 |
| 10 | Aligned-or-banked necessary condition (quantitative) | PROVED | Thm 2.6(a) |
| 11 | Mechanism defeated by truncation + banks | PROVED (J(f) finite) / SKETCH (general) | Thm 2.6(b) |
| 12 | Bank–de-switching inequality and dichotomy | PROVED | Thm 2.7, Cor 2.8 |
| 13 | Persistent bounded switching at f is an exact resonance | PROVED | Prop 2.9 |
| 14 | Tail control of switching extent (no escape obstruction) | PROVED | Lemma 2.10 |
| 15 | Engineered approximants saturate all necessary conditions | PROVED | Thm 3.1 |
| 16 | Banks move carrier values at first order | PROVED | Prop 3.2 |
| 17 | Junction mismatch s_1/t^2, scale invariant | HEURISTIC (U3-ref F6, numerics there) | 3.2 |
| 18 | Far free levers too weak under the cut-off (N1) | PROVED | Prop 3.3 |
| 19 | Junction certificate (J1)-(J4) for some admissible T | OPEN | Problem 3.4 |
| 20 | Uniform NL-type non-density certificate | FALSE as a mechanism (rows with J(f) finite); SKETCH in general | Thm 2.6 |

## Next steps (for a negative programme)
 1. Problem 3.4 at the simplest configuration: one block, maximal contact (J(f) = empty off F), a mate with S-oscillation
    carried by persistent deep switching, non-diagonal U so that banks on S move all coarse carriers' values; compute the
    cone of first-order corrections generated by banks (signs z_j), inward contact moves and pulls, and test whether the
    junction correction can lie outside it (finite LP at a fixed window; this is checkable numerically).
 2. Far rigidity: construct admissible T whose carriers' tails beyond any depth are nearly collinear within groups
    (N2 (round 2) SKETCH) and quantify the far-lever strength against Prop. 3.3.
 3. Complete Theorem 2.6(b3) (uniform inheritance over growing sets of free coordinates) to close the uniform-NL question for
    all rows.
 4. Positive side: Theorem 3.1 shows the necessary conditions are exactly the ones Part III's d-consistent approximants are
    built to satisfy; the hand-over analysis (Props. 3.2-3.3) says the levers must act at moderate depth, which is where the
    designed T_fin places them — a design-free version would need a lever lemma using inward contact moves AND banks with both
    contact signs (two contacts of opposite alignment), which is the natural target.

---
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

---

# N3 Part 2 — Uniformizing the NL mechanism: a positive-scale profile bound at ALL rows, its inheritance, and the
# bank–de-switching inequality

Notation of Part 1.  Throughout this part I = {1} (one block, the norm p_1; a negative answer for ONE N suffices, and
N = 1 is the natural adversarial choice).  Block index dropped: lambda_k = Phi(k) <= 2^{-1-k}, u_k, w, psi := R*w,
alpha(k), sigma, M, C.  Since ||Phi||_2^2 <= sum 4^{-1-k} = 1/12, C <= ||Phi||_2 < 0.29 and M = 1 - C > 0.71 at every row.
For a row f' (NA or not) its data are primed; "j aligned at f'" means z'_j psi'_j > 0.
OSCILLATION: for finite S and h, psi in l_1 put  Osc_S(h; psi) := min_{c real} sum_{j in S} |h_j - c psi_j|.

LEMMA 2.0 (elementary).  PROVED.  (a) |Osc_S(h; psi) - Osc_S(h'; psi)| <= ||(h - h')1_S||_1.
(b) |Osc_S(h; psi) - Osc_S(h; psi')| <= 2 ||h 1_S||_1 ||(psi - psi')1_S||_1 / min(||psi 1_S||_1, ||psi' 1_S||_1).
(c) For S = {s1, s2} with psi != 0 on S: Osc_S(h; psi) = |h_{s1} psi_{s2} - h_{s2} psi_{s1}| / max(|psi_{s1}|, |psi_{s2}|),
    i.e. a multiple of the functional Lambda of [II, prop:II-S3].
Proof.  (a) min of 1-Lipschitz functions.  (b) A minimizer c' for psi' satisfies sum|c' psi'_j| <= sum|h_j - c' psi'_j|
+ sum|h_j| <= 2 sum|h_j|, so |c'| <= 2||h1_S||/||psi'1_S||, and sum|h - c'psi| <= sum|h - c'psi'| + |c'| ||(psi-psi')1_S||;
symmetrize.  (c) The function of c is convex piecewise linear with breakpoints h_{s_i}/psi_{s_i}; evaluate.  QED

## 2.1 Peaks of large weight move together, at every scale

DEFINITION 2.1 (visibility data).  For a row f', a finite set Z of coordinates, a finite set Lambda of peaks of f' and
alpha_0 > 0 with |alpha'(k)| >= alpha_0 (k in Lambda), put for j in Z
   nu_j := sum_{k in Lambda} lambda_k |u_k(j)|,      eta_j := sum_{k notin Lambda} lambda_k |u_k(j)|      (the MISSED weight).
Any finite Lambda is allowed; eta_j -> 0 as Lambda exhausts N, but Lambda must consist of peaks with alpha bounded below.
Z is EXACTLY visible through Lambda if eta_j = 0 on Z (no carrier outside Lambda sees Z — a property of T and Lambda only).

LEMMA 2.2 (collective motion of weighted peaks).  PROVED.  Let f' be any row, g' with g'(xi') = 0, t in (0,1],
e := max_+- p*(f' +- t g') - 1 <= 1/2, and a scale-t pair (Def. 1.1) at f'.  Put L+ := sup_{l in P'} s_l Omega+(l),
L- := inf_{l in P'} s_l Omega-(l), s_l := sgn w'(l).  Then |L+-| <= (2 + e)/t, and for every peak k with alpha'(k) != 0
   Omega+(k) = s_k (L+ - eps+_k),   Omega-(k) = s_k (L- + eps-_k),   0 <= eps+-_k <= e / (t sigma' |alpha'(k)|).
Proof.  From the proof of Lemma 1.2, c' G_b + sigma' G(W+-) <= e, hence sigma' G(W+-) <= e, where W+ = w' + t Omega+ and
W- = w' - t Omega-.  By [I, lem:bookkeeping(c)], G(W) >= |alpha'(k)| (||W||_inf - s_k W(k)) for each peak k.  On peaks
s_k W+(k) = M' + t s_k Omega+(k), so ||W+||_inf >= M' + t L+ and |alpha'(k)| t (L+ - s_k Omega+(k)) <= e/sigma'.  Side -:
s_k W-(k) = M' - t s_k Omega-(k), ||W-||_inf >= M' - t L-, so |alpha'(k)| t (s_k Omega-(k) - L-) <= e/sigma'.  Finally
|L+-| <= ||Omega+-||_inf <= (||w' +- t Omega+-||_inf + ||w'||_inf)/t <= (2 + e)/t.  QED
For g' in C(f'), e <= t^2/2, so eps+-_k <= t/(2 sigma' |alpha'(k)|): peaks of weight >= alpha_0 deviate from the common
level by O(t) only.

## 2.2 The positive-scale profile bound (a quantitative, scale-free version of Cor. S1 at every row)

THEOREM 2.3.  PROVED.  Let f' in S_{p*} be any row (I = {1}), g' in C(f'), j_f a free coordinate of f' (|z'_{j_f}| < 1)
with psi'_{j_f} != 0, and S a finite set, j_f notin S, of coordinates aligned at f' each of which is either a support
coordinate (j in F', z'_j = sgn a'_j) or satisfies |z'_j| >= 1/2 (contact or near-contact).  Let (Lambda, alpha_0, nu, eta)
be visibility data for Z := S u {j_f}.  Put
   mu_S := sum_{j in S n F'} |a'_j|   (bank/support mass on S),   r_f := 1 - |z'_{j_f}|,   rho_S := ||psi' 1_S||_1 / |psi'_{j_f}|,
   A := rho_S/(c' r_f) + 1/c' + (rho_S nu_{j_f} + sum_S nu_j)/(sigma' alpha_0),     H := rho_S eta_{j_f} + sum_S eta_j.
Then for every t in (0, 1]:
   Osc_S(g'; psi')  <=  sum_{j in S} |g'_j - pi(j_f) psi'_j|  <=  A t + (2 mu_S + 15 H)/t,        pi(j_f) := g'_{j_f}/psi'_{j_f}.
Consequently Osc_S(g'; psi') <= 2 (A (2 mu_S + 15 H))^{1/2} if 2 mu_S + 15 H <= A (and <= A + 2 mu_S + 15 H otherwise).
Proof.  Fix t and a scale-t pair.  Block contributions: beta+-_j := (L*Omega+-)(j) = sum_k lambda_k Omega+-(k) u_k(j), so
g'_j = B+-_j + beta+-_j.  By Lemma 2.2, sum_{k in Lambda} lambda_k Omega+-(k) u_k(j) = L+- sum_{Lambda} lambda_k s_k u_k(j)
-+ sum_{Lambda} lambda_k s_k eps+-_k u_k(j); and psi'_j = M' sum_{Lambda} lambda_k s_k u_k(j) + n_j with |n_j| <= eta_j
(|w'| <= 1; w'(k) = s_k M' on peaks).  Hence, with d+- := -L+-/M',
   beta+-_j = -d+- psi'_j + r+-_j,   |r+-_j| <= (|L+-|/M') eta_j + t nu_j/(2 sigma' alpha_0) + ||Omega+-||_inf eta_j
            <= 7.5 eta_j / t + t nu_j/(2 sigma' alpha_0)         (|L+-|, ||Omega+-||_inf <= 2.5/t, M' > 0.71).
Write eps+-_j := |r+-_j|, so B+-_j = g'_j + d+- psi'_j - r+-_j.
 * At j_f: |pi(j_f) + d+-| <= (|B+-_{j_f}| + eps+-_{j_f}) / |psi'_{j_f}|.
 * At j in S, with sigma_j := sgn psi'_j = sgn z'_j: sigma_j (g'_j + d+ psi'_j) >= -(sigma_j B+_j)_- - eps+_j and
   sigma_j (g'_j + d- psi'_j) <= (sigma_j B-_j)_+ + eps-_j; dividing by sigma_j psi'_j = |psi'_j|,
   -d+ - [(sigma_j B+_j)_- + eps+_j]/|psi'_j| <= pi(j) <= -d- + [(sigma_j B-_j)_+ + eps-_j]/|psi'_j|.
Combining, |pi(j) - pi(j_f)| <= (|B+_{j_f}| + |B-_{j_f}| + eps+_{j_f} + eps-_{j_f})/|psi'_{j_f}|
+ [(sigma_j B+_j)_- + (sigma_j B-_j)_+ + eps+_j + eps-_j]/|psi'_j|.  Multiply by |psi'_j| and sum over S:
   sum_S |g'_j - pi(j_f) psi'_j| <= rho_S (|B+_{j_f}| + |B-_{j_f}| + eps+_{j_f} + eps-_{j_f}) + sum_S [(sigma_j B+_j)_- + (sigma_j B-_j)_+ + eps+-_j].
Budget (Lemma 1.2 at f', e <= t^2/2): r_f (|B+_{j_f}| + |B-_{j_f}|) <= 2e/(c' t) <= t/c'.  For j in S \ F',
(sigma_j B_j)_- <= 2(z'_j B_j)_- because |z'_j| >= 1/2; for j in S n F', (z'_j B+_j)_- <= (z'_j B+_j + |a'_j|/t)_- + |a'_j|/t.
Both kinds of terms are parts of the budget (a) [resp. (b)], whose total is <= e/(c' t) <= t/(2c'); so the S-sum of the
B-terms is <= t/c' + 2 mu_S / t.  Insert eps+_j + eps-_j <= 15 eta_j/t + t nu_j/(sigma' alpha_0).  The last claim is the
minimum of A t + K/t over t in (0,1].  QED

COROLLARY 2.4 (profile constancy at every row, all mates, under exact visibility).  PROVED.  If, in Theorem 2.3, Z is
exactly visible (H = 0) and no coordinate of S is a support coordinate (mu_S = 0), then Osc_S(g'; psi') = 0 for EVERY
g' in C(f'): g' is proportional to psi' on S, with the factor pi(j_f).
This holds at non-attaining rows f as well, and it does NOT need two-piece data: it strengthens [II, cor:II-S1] (which
assumes exact two-piece data and j notin Sigma(omega)) by replacing "outside the supports of the used carriers" with the
T-property "seen only by robust peaks".  Proof: let t -> 0 in Theorem 2.3.  QED

## 2.3 Inheritance: the bound never produces a uniform obstruction

COROLLARY 2.5 (uniform lower bound, and its inheritance).  PROVED.  Let f in S_{p*} (I = {1}), g in C(f), rho in (0,1],
j_f in J(f) with psi_{j_f} != 0, S finite aligned at f with S subset F u K, and Lambda a finite set of peaks of f with
|alpha(k)| >= 2 alpha_0.  There is delta > 0 such that for every row f' with p*(f' - f) < delta the hypotheses of
Theorem 2.3 hold at f' (same j_f, S, Lambda, alpha_0; banks on S allowed), with constants A' = A(f') -> A(f) as f' -> f,
and
   dist_{l_1}(rho g, C(f'))  >=  Osc_S(rho g; psi') - 2 (A' (2 mu_S(f') + 15 H))^{1/2}      (when 2 mu_S(f') + 15 H <= A').
But the right side is <= o(1) as f' -> f: indeed Theorem 2.3 at f itself gives Osc_S(g; psi) <= 2(A(f)(2 mu_S(f) + 15H))^{1/2},
and Osc_S(rho g; psi') -> rho Osc_S(g; psi), A' -> A(f), mu_S(f') -> mu_S(f).  So the bound is INHERITED from f: along
every sequence f' -> f it tends to (rho - 1) Osc_S(g; psi) + o(1) <= o(1).
Proof.  Along f' -> f: z' -> z coordinatewise and psi' -> psi in l_1, xi' -> xi weak*, c' -> q_0, sigma' -> sigma, and for
each fixed peak k the margin and alpha'(k) = lambda_k mu'_k / sigma' converge [I, prop:continuity], [I, (eq:margin)].
Hence for f' close to f: j_f is free at f' with r'_f -> r_f, every j in S keeps sgn z'_j = sgn z_j, |z'_j| >= 1/2 or
j in F' (a bank created on a contact of f has sgn a'_j = z'_j = z_j), sgn psi'_j = sgn psi_j, Lambda consists of peaks with
|alpha'| >= alpha_0, psi'_{j_f} != 0.  The displayed inequality is Theorem 2.3 plus Lemma 2.0(a).  The convergence of the
constants is clear; mu_S(f') -> mu_S(f) because a' -> a in l_1.  QED

So a FIXED free coordinate of f can never produce a uniform obstruction: the approximant faces the same linear sandwich as
f, with constants converging to those of f.  A positive lower bound along a sequence f'_n can only come from free
coordinates of f'_n that are NOT free coordinates of f with comparable weight: (b) a contact or support coordinate j of f
made free at f'_n — then r'_n(j) -> 0 for fixed j, so A'_n -> infinity; or (c) j_n -> infinity — then psi'_n(j_n) -> 0, so
rho_S -> infinity and A'_n -> infinity.  In both cases the bound is defeated by banks on S of mass of order 1/A'_n:

THEOREM 2.6 (the profile mechanism is not uniform; sharp "aligned or banked" condition).  PROVED.
 (a) Necessary condition.  Let f'_n -> f be NA rows and g'_n in C(f'_n) with g'_n -> rho g, and let S be aligned at f with
     kappa := Osc_S(rho g; psi) > 0.  Then for all large n and every free coordinate j of f'_n for which Z_j := S u {j}
     satisfies the hypotheses of Theorem 2.3 at f'_n with constants (A_n(j), H(j)) and 2mu_S(f'_n) + 15H(j) <= A_n(j):
        A_n(j) (2 mu_S(f'_n) + 15 H(j)) >= kappa^2/5.
     Under exact visibility (H = 0): mu_S(f'_n) >= kappa^2 / (10 A_n(j)), and A_n(j) <= C (1 + rho_S(j)/r'_n(j)) with
     rho_S(j) = ||psi'_n 1_S||/|psi'_n(j)|: the bank mass on S must dominate the visibility weight |psi'_n(j)| (1 - |z'_n(j)|)
     of EVERY free coordinate j of f'_n, up to the factor kappa^2/(C ||psi 1_S||).  (Quantitative form of "approximants for
     oscillating mates must be aligned or banked", U3 / [II, rem after prop:II-S3].)
 (b) Sufficiency in the data.  Let f have F finite, S subset K u F finite and aligned at f, rho in (0,1], g in C(f), and
     put nu^tot_j := sum_k lambda_k |u_k(j)| (a property of T alone; nu^tot_j -> 0 as j -> infinity, and |psi'_j| <= nu^tot_j
     at EVERY row since |w'| <= 1).
     (b1) [far coordinates]  For every row f' and every free coordinate j of f' with
          8 ||psi' 1_S||_1 mu_S(f') >= c' nu^tot_j Osc_S(rho g; psi')^2  (mu_S(f') = mass of a' on S),
          the lower bound produced by Theorem 2.3 via j is <= 0.  PROVED.
     (b2) [J(f) finite]  If f has only finitely many free coordinates (e.g. the self-aligned rows of [II, rem:II-NL], where
          every coordinate off F is a contact), then for every theta in (0,1] the canonical truncation of f at a depth N
          with banks of mass m_theta := theta on each j in S \ F is an NA row f'_{theta,N} with
          p*(f'_{theta,N} - f) -> 0 as (theta, N) -> (0, infinity), and, for every fixed eps > 0, the supremum over all
          lower bounds produced by Theorem 2.3 at f'_{theta,N} (any free coordinate; visibility data with
          Lambda subset {k : lambda_k >= eps} and alpha_0 := min_Lambda |alpha'(k)|) is <= (rho - 1) Osc_S(g; psi)_+ + o(1).
          PROVED.  (Restricting Lambda to weights >= eps costs nothing essential: a carrier of weight lambda_k has
          |alpha'(k)| = lambda_k mu'_k/sigma' <= lambda_k/sigma', so putting it into Lambda forces alpha_0 <= lambda_k/sigma'
          and inflates A; for fixed eps and finite J(f) the admissible (j, Lambda) with j in J(f) form a finite family, so
          the pointwise inheritance of Corollary 2.5 is uniform over it.)
     (b3) [general f]  The same conclusion for arbitrary f is a SKETCH: it requires inheritance (Corollary 2.5) uniformly
          over the growing finite sets {j in J(f) : nu^tot_j >= theta}, i.e. control of |psi'_j - psi_j| relative to
          |psi_j| there; banks perturb psi by up to O(m log(1/m)) in sup norm (through strict non-peaks seeing j), and a
          coordinate where this perturbation dominates contributes a vacuous bound only when the perturbing carriers enter
          the missed weight eta_j (they do: strict non-peaks are not in Lambda) — the bookkeeping is not carried out here.
Proof.  (a) Theorem 2.3 at f'_n gives Osc_S(g'_n; psi'_n) <= 2(A_n(2mu_S + 15H))^{1/2}, and by Lemma 2.0(a),(b)
Osc_S(g'_n; psi'_n) -> kappa; so 4 A_n (2mu_S + 15H) >= (kappa - o(1))^2 >= 4kappa^2/5 for n large.  The bound on A_n uses
c'_n -> q_0, sigma'_n -> sigma (for the nu-term, bounded by the visibility constant of the fixed set S and of j).
(b1) Whatever the case in Theorem 2.3, the subtracted bound is >= 2(2 A mu_S)^{1/2} (if 2mu_S + 15H > A it is
A + 2mu_S + 15H >= 2(2A mu_S)^{1/2} by AM-GM), and A >= rho_S/(c' r_f) >= ||psi'1_S||/(c' |psi'_j|) >= ||psi'1_S||/(c' nu^tot_j).
So the subtracted bound is >= Osc_S(rho g; psi') under the displayed inequality.
(b2) Let J(f) = {j_1, ..., j_r}.  The truncation keeps z on [1, N] (N >= max J(f)), so the free coordinates of f' are
J(f) (with the rooms of f) and (N, infinity) (room 1).  By N1 Lemma 1.4 (uniform far freedom) p*(f' - f) -> 0.  Far
coordinates j > N: nu^tot_j <= tau(N) := sup_{i > N} nu^tot_i -> 0, so (b1) applies as soon as
8 ||psi'1_S|| theta |S \ F| >= c' tau(N) Osc_S(rho g; psi')^2 — true for N large given theta (if S \ F is empty, i.e.
S subset F, banks are the support masses of f and the inequality reads 8||psi'1_S|| mu_S(f) >= c' tau(N) Osc^2, again true
for N large).  The finitely many j in J(f): Corollary 2.5 at each of them (data of f' converge to those of f as
theta -> 0, N -> infinity), giving <= (rho - 1) Osc_S(g; psi) + o(1) when Theorem 2.3 applies at f via j, and a vacuous
or o(1) bound otherwise: if psi_j = 0 and eta_j = 0 then psi'_j = (M'/M) psi_j = 0 (fact below) and Theorem 2.3 does not
apply via j; if psi_j = 0 and eta_j > 0, the subtracted term is >= 2 (15 A' H)^{1/2} >= 2 rho'_S (15 eta_j/(c' r_j))^{1/2} with
rho'_S = ||psi'1_S||/|psi'_j| -> infinity (psi'_j -> psi_j = 0), so the bound via j is vacuous for f' close to f.  QED
Fact used in (b2): if only peaks of f' see j (eta_j = 0 for some Lambda of peaks of both f and f' with equal signs), then
psi'_j = M' sum_Lambda lambda_k s_k u_k(j) = (M'/M) psi_j: visible values of psi are inherited exactly up to the factor M'/M.
In the main case S subset K (mu_S(f) = 0) with exact visibility, Theorem 2.3 at f shows that Osc_S(g; psi) > 0 forces f to
have no free coordinate j with psi_j != 0 satisfying its hypotheses: the inherited part of (b2) is then void.

READING.  The NL mechanism is a positive-scale LINEAR SANDWICH (Theorem 2.3) that every mate at every row obeys.  It is
inherited from f by any approximant that copies f's one-sided structure (contacts and support) on the window where psi is
large, and banks S with mass of order (visibility weight of its free coordinates); such approximants exist in every
neighbourhood (Theorem 2.6(b)).  Theorem NL is the special case of approximants that are neither aligned nor banked: they
have a visible free coordinate with |psi'| (1 - |z'|) bounded below and no banks on S.  Part (a) is sharp up to constants
for the engineered approximants of [I, thm:engineered] (Part 3).

## 2.4 The bank–de-switching inequality (what banks must pay at NA rows)

THEOREM 2.7 (bank–de-switching inequality).  PROVED.  Let f' have F' u K' finite (e.g. NA), I = {1}, S aligned at f' as in
Theorem 2.3 (no free coordinate is needed), and visibility data (Lambda, alpha_0, nu, eta) for S.  For g' in C(f'), t in
(0,1] and every scale-t pair with ||Delta Omega||_{V*} <= M:
   Osc_S(g'; psi') <= (1/2) omega_{f'}(M, t/c') + A_S t + (2 mu_S + 22.5 H_S)/t,
   A_S := 1/c' + (3/2) sum_S nu_j/(sigma' alpha_0),   H_S := sum_S eta_j,
with omega_{f'} the de-switching modulus of Definition 1.3 (omega_{f'}(M, r) -> 0 as r -> 0 by Theorem 1.4).
Proof.  As in Theorem 2.3, for j in S: -d+ - e+_j <= pi(j) <= -d- + e-_j with e+_j := [(sigma_j B+_j)_- + eps+_j]/|psi'_j|,
e-_j := [(sigma_j B-_j)_+ + eps-_j]/|psi'_j|.  With c := -(d+ + d-)/2: |pi(j) - c| <= (d+ - d-)_+/2 + e+_j + e-_j.  On S the
switching vector is V_j = B+_j - B-_j = beta-_j - beta+_j = (d+ - d-) psi'_j + r-_j - r+_j, so
(d+ - d-)_+ ||psi'1_S||_1 <= ||V 1_S||_1 + sum_S (eps+_j + eps-_j).  Hence
Osc_S(g'; psi') <= ||V||_1/2 + sum_S [(sigma_j B+_j)_- + (sigma_j B-_j)_+] + (3/2) sum_S (eps+_j + eps-_j), and the middle sum is
<= t/c' + 2 mu_S/t (budget), the last <= (3/2)(15 H_S/t + t sum_S nu_j/(sigma' alpha_0)).  Finally ||V||_1 <=
omega_{f'}(M, t/c') by Theorem 1.4(b) (e <= t^2/2).  QED

COROLLARY 2.8 (dichotomy at NA rows).  PROVED.  In the setting of Theorem 2.7 with exact visibility (H_S = 0), if
Osc_S(g'; psi') = kappa' > 0 then for every scale t in (0, kappa'/(4 A_S)] at least one of the following holds:
 (i) mu_S >= kappa' t / 8 (the banks on S carry the oscillation at scale t); or
 (ii) every scale-t pair of g' has ||Delta Omega||_{V*} > M_t, where M_t := sup{M : omega_{f'}(M, t/c') <= kappa'}
      (the switching at scale t runs through large block coefficients — by Corollary 1.5, through deep carriers).
Since omega_{f'}(M, r) -> 0 as r -> 0 for each M, M_t -> infinity as t -> 0: below the de-switching scale of f', bounded
switching cannot carry the oscillation, and either the banks pay mu_S >~ kappa' t or the carriers become deep.
Proof.  If (ii) fails, some pair has ||Delta Omega|| <= M_t and Theorem 2.7 gives kappa' <= kappa'/2 + kappa'/4 + 2mu_S/t. QED

## 2.5 Persistent bounded switching at f is an exact resonance; escape is controlled by the tails of T

PROPOSITION 2.9 (exact resonances as limits).  PROVED.  Let f in S_{p*} (any K), g in C(f), t_n -> 0+, and scale-t_n pairs
at f with ||Delta Omega_n||_{V*} <= M and ||V_n||_1 >= c > 0.  Then a subsequence of Delta Omega_n converges weak* to some
Delta with ||Delta|| <= M, V_inf := L* Delta != 0, V_inf = 0 on J, z_j V_inf(j) >= 0 on K: an exact one-sided transfer
(exact resonance) of f, with bounded coefficients.
Proof.  As in Theorem 1.4: V_n -> V_inf in l_1 (compactness of L*), ||V_inf|| >= c; Lemma 1.2(c) gives
sum_J (1 - |z_j|)|V_n(j)| + sum_K 2 (z_j V_n(j))_- <= t_n/q_0 -> 0.  QED
So bounded-coefficient switching that persists to t -> 0 at f is carried by an exact resonance V_inf, and the canonical
truncations at depth N support it with leakage ||V_inf 1_{K n (N, inf)}||_1 (Remark 1.6(c)): their de-switching scale
tends to 0, and Corollary 2.8(i) can be met with mu_S ~ kappa t^*(N) -> 0.  This is exactly the mechanism of
[I, thm:engineered] (window masses ~ 4 rho s_1 |b^theta|, cut-off N'' with V_{>N''} <= delta s_1/(16 rho)).

LEMMA 2.10 (tail control of the switching extent).  PROVED.  For every row f, g in C(f), t in (0,1], every scale-t pair
and every N:
   ||V 1_{(N, inf)}||_1 <= (5/t) frak_t(N),     frak_t(N) := sum_{k,m} lambda_{k,m} ||u_{k,m} 1_{(N, inf)}||_1  ( -> 0 ).
Proof.  V = L*(Delta Omega) = sum lambda_{k,m} Delta Omega(k,m) u_{k,m} and |Delta Omega(k,m)| <= (4 + 2e)/t <= 5/t. QED
Consequence: at scale t, a truncation at any N with frak_t(N) <= delta t^2/5 loses at most switching mass delta t, whose
first-order cost is <= delta t^2.  Switching can therefore never "escape to infinity" faster than the tails of T allow:
an escape-rate obstruction against truncation-type approximants (switching at depth D(t) -> infinity too fast as t -> 0)
does NOT exist; the requirement is exactly the cut-off condition [I, (N1)] frak(N'') <= s_1^2 of the engineered
construction, with N'' chosen after the junction scale s_1.

## Summary of Part 2
(1) The NL mechanism has a quantitative, scale-free form valid for ALL mates at ALL rows (Theorem 2.3, Corollary 2.4);
it implies "aligned or banked" with a sharp quantitative threshold (Theorem 2.6(a)).
(2) It is INHERITED from f (Corollary 2.5) and DEFEATED in every neighbourhood of f by truncation + banks of mass of
order (visibility weight of the approximant's free coordinates) (Theorem 2.6(b)): PROVED when f has finitely many free
coordinates (this includes the self-aligned rows where Theorem NL is realized), SKETCH in general (uniform inheritance over
growing finite sets of free coordinates of f).  So no profile/oscillation functional of NL type gives a uniform
non-density certificate at such rows, for ANY admissible T and any S.
(3) At NA rows banks must pay mu_S >~ kappa * (de-switching scale) unless the switching runs through deep carriers
(Corollary 2.8); persistent bounded switching at f is an exact resonance (Prop. 2.9), which truncations carry down to an
arbitrarily small de-switching scale; escape of switching is controlled by T's tails (Lemma 2.10).  None of these
constraints obstructs: they are all met, with matching constants, by the engineered approximants (Part 3).

---

# N3 Part 3 — Test against the engineered approximants; the only non-inherited residue (the hand-over); numerics

Notation of Parts 1-2.  [I, def:engineered], [I, thm:engineered] = Part I Definition 7.12 / Theorem 7.18.

## 3.1 The engineered approximants meet every necessary condition of Part 2, with matching constants

Setting of [I, thm:engineered]: I finite, f with F finite, g in C(f) with two-piece data (b+-, omega+-), b^theta, omega^theta,
v = b+ - b-, rho^2 kappa_w < 1, I_- = {m : Delta d_m < 0} satisfying (SC).  The approximant f' (stage (N_w, s_1, N''))
has: window masses m_j = 4 rho s_1 |b^theta_j| on K n [1, N_w] (sign z_j), z' = z on [1, N''], z' = 0 beyond N'', the
cut-off conditions (N1) frak_t(N'') <= s_1^2, (N2), (N3) rho V_{>N''} <= delta s_1/16; it uses the theta-pair for
0 < |tau| <= s_1 and the +- pairs for s_1 < |tau| <= T_0.

THEOREM 3.1 (sharpness of the Part 2 conditions).  PROVED.  For the engineered approximants, at late stages:
 (i) [aligned or banked] every contact of f in [1, N''] is a contact of f' or a window bank with the same sign; the free
     coordinates of f' are J(f) n [1, N''] (rooms of f) and (N'', infinity), where |psi'_j| <= nu^tot_j <= tau(N'') :=
     sup_{i > N''} nu^tot_i; since N'' is chosen after s_1, the necessary condition of Theorem 2.6(a) for far free
     coordinates (mu_S >~ kappa^2 c' tau(N'')/||psi 1_S||) holds for every finite aligned S inside the window.
 (ii) [de-switching scale] the theta-pair has V = 0 (B+ = B- = rho(beta^theta - c a'), Omega+ = Omega- = Omega^theta) and the
     +- pairs have V = rho v != 0 in general: the hand-over (de-switching) scale of the construction is exactly s_1.
 (iii) [bank–de-switching inequality] for S subset K n [1, N_w] aligned, exactly visible (one block), with S disjoint from the
     supports of the carriers of omega^theta: Osc_S(g'; psi') <= rho ||b^theta 1_S||_1 (1 + O(s_1)) and
     mu_S(f') = 4 rho s_1 ||b^theta 1_S||_1 / q*(a''), hence mu_S(f') >= 4 s_1 Osc_S(g'; psi') (1 - o(1)): Corollary 2.8(i)
     (mu_S >= kappa' t/8 at t = s_1) is met with a factor 32 to spare.
 (iv) [tail control] (N1) is exactly the cut-off condition of Lemma 2.10 at the junction scale s_1.
Proof.  (i) Definition of f' and |psi'_j| <= sum_k lambda_k |w'(k)||u_k(j)| <= nu^tot_j.  (ii) Step 2 of the proof of
[I, thm:engineered]: B^theta := rho(beta^theta - c a') is used on both sides for |tau| <= s_1, and beta+ - beta- = v.
(iii) In the theta-regime g'_j = rho(b^theta_j - d'(omega^theta) psi'_j - c a'_j) for j in S (S misses the carrier supports),
so Osc_S(g'; psi') <= rho ||(b^theta - c a')1_S||_1 with |c| -> 0 and ||a' 1_S||_1 = O(s_1); the bank masses are as stated by
[I, lem:approxfacts(a)] (a' = a''/q*(a''), q*(a'') -> 1).  (iv) Definition.  QED

CONSEQUENCE.  For mates with exact two-piece data (Delta d >= 0 or (SC), rho^2 kappa_w < 1) every necessary condition derived
in Parts 1-2 is met by the engineered approximants up to absolute constants, and these approximants recover rho g.  So no
functional of the types of Part 2 (profile/oscillation functionals on contact, signature or free coordinates; switching
moduli; bank-mass functionals) can certify non-density for such mates — and the conditions of Part 2 are sharp, not
lossy, since the recovering construction saturates them.  For mates WITHOUT exact data (scale-dependent switching), the
conditions of Part 2 are still satisfiable in the data (Theorem 2.6(b), Prop. 2.9, Lemma 2.10): they do not obstruct either.

## 3.2 What is not inherited: the hand-over at the de-switching scale

By Theorem 1.4 every NA approximant of a row with an infinite contact set must DE-SWITCH: below some scale s_* (depending
on the approximant) bounded-coefficient switching is impossible, and by Corollary 2.8 the profile oscillation of the mate
must then be carried by banks of mass >~ kappa s_* (or by deep carriers).  Above s_* the approximant can inherit f's
one-sided structure (Corollary 2.5, Prop. 2.9, Lemma 2.10).  The HAND-OVER at s_* is the only place where an NA approximant
is structurally different from f, and the only place where a uniform obstruction could live.

PROPOSITION 3.2 (banks move carrier values at first order).  PROVED (from [III, lem:III-masses(i)] for diagonal U; general U
by the same computation).  Let a have support F, and A = a + sum_{s in Bk} c_s e_s* with Bk disjoint from F (banks).  Then for
every u in l_1, with e_A := U*A/||U*A||, nu := ||U*a||:
   <U*u, e_A - e> = nu^{-1} <P^perp U*u, sum_{s in Bk} c_s U* e_s*> + O(||c||^2),
(diagonal U: = nu^{-1} sum_s c_s (mu*_s)^2 u(s) + O(||c||^2)).  Hence a bank configuration of total mass mu changes the value
u_k(xhat') of a carrier k by a LINEAR form of the (sign-constrained) masses, of size O(mu), and the normalized values
nv'_k = lambda_k u_k(xhat')/A' by O(lambda_k mu) plus the common normalization.
Proof.  e_A - e = (U*A/||U*A||) - (U*a/||U*a||); differentiate at c = 0: d e_A = (P^perp U* dA)/nu.  For diagonal U this is
[III, lem:III-masses(i)].  xhat' - zhat = (z' - z) + U(e_A - e) and z' = z at banks placed on contacts of f with sign z_s. QED

READING (the junction mismatch, U3-referee F6).  For window data whose switching runs through carriers with coefficients of
order 1/t, the d-values d(omega) = sum_k omega(k) nv_k move by O(mu/t) when banks of mass mu ~ s_1 are placed; the resulting
first-order level mismatch at the junction is of order s_1/t^2 per unit tau, i.e. tau^2/t^2 at |tau| = s_1: SCALE
INVARIANT (enlarging the theta-regime enlarges the masses).  [I, thm:engineered] avoids it because its data are FIXED
(coefficients O(1)); Part III removes it by d-CONSISTENCY: the normalized values of the finitely many switching carriers
are re-tuned exactly at f' by levers ([III, def:III-dcons], [III, lem:III-DC]).  HEURISTIC summary of U3-ref F6, verified
numerically there (junction_check.py: kappa t^2/s_1 constant to five digits).

PROPOSITION 3.3 (far free levers are weak at engineered rows).  PROVED.  Let f' be any row whose z' agrees with z on [1, N],
and let Delta z' be any change of z' supported in (N, infinity) with ||Delta z'||_inf <= 2.  Then for every carrier k,
   |u_k(xhat' + Delta z') - u_k(xhat')| <= 2 ||u_k 1_{(N, inf)}||_1 <= 2 frak_t(N)/lambda_k.
In particular, under the cut-off condition (N1) frak_t(N'') <= s_1^2 of [I, thm:engineered], far free moves change the value
of a carrier of weight lambda_k by at most 2 s_1^2/lambda_k, while the banks (Prop. 3.2) change it by order s_1: for coarse
switching carriers (lambda_k >> s_1) the two-sided far levers are too weak by the factor s_1/lambda_k.  Compensation must then
come from moves at moderate depth, where the approximant must keep f's structure, i.e. from ONE-SIDED resources (banks with
prescribed signs, inward contact moves, pulls [III, def:III-levers]) — unless the design of T provides private two-sided
levers (diagonal base + private banks/pulls, as for T_fin).
Proof.  u_k(Delta z') = sum_{j > N} u_k(j) Delta z'_j, and lambda_k ||u_k 1_{(N,inf)}||_1 <= frak_t(N).  QED

So, for an ARBITRARY admissible T, the uniformized NL question reduces to the following, which is precisely the consensus
core "exactness versus one-sidedness" (ADDENDA 13-14), now localized at the de-switching scale:

PROBLEM 3.4 (junction certificate; what a non-density proof along this route must establish).  OPEN.  Find admissible T
(one block suffices), f, g in C(f), rho < 1 such that for every NA f' near f and every g' in C(f') near rho g:
 (J1) g requires persistent switching at f at all small scales with S-oscillation kappa > 0 (so every recovering approximant
      de-switches at some s_*(f') > 0 and must bank S with mass >~ kappa s_*, Theorem 1.4, Corollary 2.8);
 (J2) the first-order corrections needed at the hand-over (re-tuning the switching carriers' normalized values after the
      banks of Prop. 3.2, or an equivalent exact cancellation) lie outside the closed cone generated by the one-sided resources
      available at moderate depth — a Farkas certificate y with y >= 0 on banks / inward moves / pulls and y < 0 on the
      required correction;
 (J3) two-sided resources are too weak: far free moves (Prop. 3.3) and deep carriers cannot supply the correction at the
      required precision ("far rigidity" of T; compatible with Lemma B by N2 (round 2) SKETCH);
 (J4) the scale-invariant mismatch exceeds the slack: a mismatch ratio above delta = (1 - rho^2 kappa)/2 at the hand-over.
Nothing in Parts 1-3 shows (J1)-(J4) can hold simultaneously; nothing excludes it for arbitrary T.  For the designed T_fin
(diagonal base, private levers) (J2)-(J3) fail at finite-support rows (Master Theorem VI).

## 3.3 Numerics (sanity checks only; finite-dimensional SOCP models, CLARABEL)  — N3_work/

 * identity_check.py: the identities |B| -+ zB = (1 - |z|)|B| + 2(zB)_-+ and |x + y| = |x| + sgn(x)y + 2(-sgn(x)y - |x|)_+,
   and the elementary inequalities of Lemma 1.2, on 10^5 random samples: errors <= 1e-15, no violations.
 * sqrt_mu_check.py (+ sqrt_mu_check2.py): 7 coordinates, one block of 6 carriers, diagonal base; S = {1, 2} aligned banks of
   mass m each, j_f = 3 free and exactly visible through one robust peak.  Maximum of Osc_S(g'; psi') over the
   t-discretized fibre (140 scales, |t| in [1e-5, 3.2]):
       m = 0: Osc = 4.9e-5 (grid floor);  m = 1e-7 ... 1e-2: Osc/sqrt(mu_S) = 1.257, 1.239, 1.218, 1.216, 1.217, 1.210.
   The sqrt(mu) law of Corollary 2.4 / Theorem 2.3 holds over five decades with constant 1.22, below the proved constant
   2(2A)^{1/2} = 6.06 (A = 4.59 computed from the formula of Theorem 2.3): the bound is sharp in its scaling.
   Caveat (finite-model artifact): the "maximal aligned contact" comparison also gives Osc = 0 at m = 0, because the finite
   model has no transfer peaks, so shifts are pinned by the lack of rebalancing; finite models cannot show the shift
   mechanism (nor de-switching: Y n c_00 = {0} has no finite analogue).
 * lemma_checks2.py / lemma_checks3.py: on the optimal SOCP decompositions (with g(x') = 0 imposed, as for every mate),
   Lemma 1.2 (a),(b) hold with ratio <= 0.96 on the whole grid; Lemma 2.2 holds with ratio <= 0.32 on t in [1e-3, 3.2]
   (at t <= 3e-5 the budget e ~ t^2/2 ~ 5e-11 is at solver tolerance and the ratio is meaningless).  Without imposing
   g(x') = 0 the discretized optimum has g(xhat') ~ -6e-5, which adds t|g(x')| to the budget (first run, ratios up to 5):
   this is consistent with the proofs, which use g(xi') = 0.

## 3.4 Verdict of the N3 track

 (1) Uniformizing Theorem NL over all NA approximants FAILS, provably at the level of the mechanism: the positive-scale
     profile bound (Theorem 2.3, valid at every row for every mate) is inherited from f (Corollary 2.5) and is defeated in
     every neighbourhood of f by truncation + banks (Theorem 2.6(b): PROVED when f has finitely many free coordinates, which
     covers the self-aligned rows where NL is realized; SKETCH in general).
 (2) What survives is a sharp NECESSARY STRUCTURE of recovering approximants (aligned-or-banked with the quantitative
     threshold of Theorem 2.6(a); de-switching, Theorem 1.4; banks >~ kappa x de-switching scale, Corollary 2.8; migration
     of persistent switching to deep carriers, Corollary 1.5), and the engineered approximants saturate it (Theorem 3.1).
     This is POSITIVE evidence: the conditions are met by an explicit construction whenever the data are exact.
 (3) A non-density certificate along this line would have to be a JUNCTION certificate (Problem 3.4): a first-order Farkas
     obstruction against one-sided levers at the hand-over, combined with the weakness of two-sided far levers
     (Prop. 3.3) — i.e. the same "exactness versus one-sidedness" core that blocks the positive proofs, now localized at the
     de-switching scale.  The failure of the positive programme and a hypothetical negative proof would meet at the same
     point; neither side gains asymmetric evidence from N3.  No candidate (T, f, g) realizing (J1)-(J4) is known.
