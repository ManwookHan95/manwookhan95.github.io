# Z5 part 4: truncations, what transfers, and the structure of infinite-F first rows (any admissible T unless stated)

Notation: f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu), s_j = sgn a_j on F, alpha(M) := sum_{j in F, j > M}|a_j|,
F_{<=M} := F cap [1, M]. I finite, T admissible.

## 4.1 Truncated first rows. PROVED.
For M with F_{<=M} nonempty put a^M := a 1_{[1,M]}/q*(a 1_{[1,M]}), and let z^M be ANY vector with |z^M| <= 1, z^M = z on [1, M],
and arbitrary on (M, infinity) (in particular on the far support F cap (M, infinity)). Then (a^M, z^M) is admissible forced data
(z^M = z = sgn a = sgn a^M on supp a^M = F_{<=M}), so it is the forced data of a unique first row f^M (Remark rem:lemmaZ(c)), with
base support F_{<=M} (finite). Since a^M -> a in l_1 and z^M -> z coordinatewise (the free coordinates escape to infinity),
f^M -> f in norm as M -> infinity (proof of Proposition prop:approximants, (ii) => (i), which does not use norm attainment).
Special choices: contact truncation z^M := z (the far support becomes a contact set with the signs of a); free truncation z^M := 0
on F cap (M, infinity); engineered truncations (signs chosen for a given mate, Part 3).

## 4.2 Exact transfer of pure base mates along every truncation. PROVED.
Let C_q(a) := {b in l_1 : q*(a + tb) <= s(t) for all real t}. Since p*(f + tb) <= max(q*(a+tb), ||w||) (Lemma lem:dualball),
C_q(a) is contained in C(f) (the pure base mates).

Lemma 4.1. (a) Every b in C_q(a) satisfies supp b in F and b(zhat) = 0.
(b) Let b in C_q(a), rho in (0,1), and put b^M := b 1_{[1,M]} - kappa_M a^M, kappa_M := (b 1_{[1,M]})(zhat^M), zhat^M := z^M + U e^M,
e^M := U*a^M/||U*a^M||. Then b^M -> b in l_1 and rho b^M in C_q(a^M), hence rho b^M in C(f^M), for all large M, for every choice of the
far values of z^M. In particular every pure base mate of f is recovered along every truncation sequence (and along norm-attaining
ones, since f^M can be taken norm attaining: z^M := z 1_{[1,M']} for any M' >= M gives a norm-attaining f^M by Proposition prop:smooth(c)).

Proof. (a) By (eq:baseidentity), q*(a + tb) = 1 + t b(zhat) + Fl_b(t) + sum_{j notin F} phi_{z_j}(t b_j) + nu Psi(t U*b/nu), with all
terms after t b(zhat) nonnegative. Dividing q*(a+tb) - 1 <= s(t) - 1 <= t^2/2 by t and letting t -> 0+ and t -> 0- gives b(zhat) = 0;
then phi_{z_j}(t b_j) = |t|(|b_j| - z_j sgn(t) b_j) <= t^2/2 for both signs of t forces |b_j| - z_j b_j = 0 = |b_j| + z_j b_j, i.e. b_j = 0
for j notin F.
(b) kappa_M -> b(zhat) = 0: on [1,M], z^M = z, and e^M -> e, so (b1_{[1,M]})(zhat^M) = sum_{j<=M} b_j z_j + <U*(b1_{[1,M]}), e^M> ->
b(z) + <U*b, e> = b(zhat). Hence b^M -> b in l_1 (a^M -> a). Also b^M(zhat^M) = kappa_M - kappa_M a^M(zhat^M) = 0.
Large t: q*(a^M + t rho b^M) <= q*(a + t rho b) + eps_M + rho|t| eps'_M <= s(rho t) + eps_M + rho|t|eps'_M with eps_M := q*(a^M - a),
eps'_M := q*(b^M - b) -> 0; by Lemma lem:slack(a) this is <= s(t) for |t| >= T_0 and M >= M_0(T_0), for any fixed T_0 > 0.
Small t: let c_M := q*(a 1_{[1,M]}) -> 1. The base identity at a^M (proof of Lemma lem:base with data (a^M, z^M, e^M); b^M is supported
in F_{<=M}, so the off-support sum vanishes) gives, with B := t rho b^M,
  q*(a^M + B) = 1 + Fl^M(t) + nu_M Psi_M(t rho U*b^M/nu_M),
  Fl^M(t) = sum_{j in F_{<=M}} 2(-s_j t rho b_j - lambda_M(t)|a_j|)_+,   lambda_M(t) := (1 - t rho kappa_M)/c_M.
(Indeed -s_j t rho b^M_j - |a^M_j| = -s_j t rho b_j - (1 - t rho kappa_M)|a_j|/c_M.) For |t| <= T_0 and M large, lambda_M(t) >= rho, so
each summand is <= 2(rho(-s_j t b_j - |a_j|))_+ = rho . 2(-s_j t b_j - |a_j|)_+, and Fl^M(t) <= rho Fl_b(t), where Fl_b is the flip term
of a + tb; and Fl_b(t) <= s(t) - 1 - nu Psi(tU*b/nu) by the identity of (a). With Lemma lem:base (a) and (b) bounds for Psi and Psi_M
(||t rho U*b^M/nu_M|| <= 1/2 for |t| <= T_0 small):
  q*(a^M + t rho b^M) <= 1 + rho(s(t) - 1) - rho (t^2/2) h(b)/(1 + |t| ||U*b||/nu) + (t^2 rho^2/2) h_M (1 + 2|t| rho||U*b^M||/nu_M),
with h_M := ||P_M^perp U*b^M||^2/nu_M = ||P_M^perp U*(b 1_{[1,M]})||^2/nu_M -> h(b). Hence, with a constant C_0 depending on b, a,
  q*(a^M + t rho b^M) - s(t) <= -(1 - rho)(s(t) - 1) + (t^2 rho/2)(rho|h_M - h(b)| + C_0|t|)
                            <= -(t^2/2)[(1-rho)(1 - t^2/4) - rho^2|h_M - h(b)| - rho C_0|t|] <= 0
for |t| <= T_0 (T_0 small, depending on rho, b) and M large. QED

Remark 4.2. The pure base part of a mate is thus never an obstruction: flips of b on far support coordinates are dominated, after
truncation, by flips of rho b, because truncation removes cushions only where b is removed as well. Contrast: a MIXED mate whose
decompositions use far support coordinates against their sign to compensate block switching cannot simply drop that usage
(Section 4.5).

## 4.3 Bounded free switching at arbitrary F (correction to the note). PROVED.
The note (Lemma lem:boundedfree and the Round-4 referee) states that F finite is essential because Y may contain a when a is not in
c_00. The first-order budget removes this restriction.

Lemma 4.3. Let f be arbitrary, eta <= eta_* with eta_Gamma(eta) <= 1, 0 < t <= min(t_eta, 1), (B_+-, Theta_+-) a two-sided
decomposition of g in C(f) at scale t, Delta theta_{k,m} := lambda_{k,m} Delta Theta_m(k). For every finite set U of pairs (k,m) there is
C_U < infinity depending only on f and U with
  max_{(k,m) in U} |Delta theta_{k,m}| <= C_U (1 + ||sum_{(k,m) notin U} Delta theta_{k,m} u_{k,m}||_1).
Proof. The linear map Phi: R^U -> H x R, c |-> (P^perp U* sum_U c_{k,m} u_{k,m}, (sum_U c_{k,m} u_{k,m})(zhat)) is injective: if
Phi(c) = 0, then U*(sum_U c u) = mu e for some real mu, so sum_U c u = (mu/nu) a (U* injective), and then 0 = (sum_U c u)(zhat) =
(mu/nu) a(zhat) = mu/nu; hence sum_U c u = 0 and c = 0 because T is injective and u_{k,m} = T e_{k,m}/q*(T e_{k,m}). So
||c||_inf <= C_U ||Phi(c)|| (any product norm). Apply this to c := (Delta theta)|_U: by (eq:DeltaB), sum_U Delta theta u = -Delta B - R,
R := sum_{notin U} Delta theta u. By Lemma lem:budget(d), ||P^perp U* B_+-||^2 = nu h(B_+-) <= nu(1 + eta_Gamma)/q_0 <= 2nu/q_0, so
||P^perp U* Delta B|| <= 2(2nu/q_0)^{1/2}; by Lemma lem:budget(a), |Delta B(zhat)| <= t/q_0 <= 1/q_0; and ||P^perp U*R|| <= ||U|| ||R||_1,
|R(zhat)| <= (1 + ||U||)||R||_1. QED
Remark. The a-direction is exactly the direction pinned at first order: if a = sum_U c u (possible when a is not in c_00, e.g. a = u_l for
the SLD operator), switching along it changes Delta B(zhat) by sum_U c_{k,m} u_{k,m}(zhat) = 1 per unit, and |Delta B(zhat)| <= t/q_0. So
"a in Y" is harmless for bounded switching; the genuine new freedom at infinite F is different (4.5).

## 4.4 The proxy budget: an infinite-F first row at scale t is a finite-F first row with extra contacts. PROVED.
Lemma 4.4. Let f be arbitrary, g in C(f), t > 0, (B_+-, Theta_+-) a two-sided decomposition at scale t, and M with alpha(M) <= t^2.
Put Fbar := F_{<=M} (finite), Kbar := K cup (F cap (M, infinity)), and zbar := z (so zbar_j = s_j on F, |zbar| = 1 on Kbar). Then
  sum_{j notin Fbar} phi_{zbar_j}(B_+(j)) <= t/q_0 + 2t,   sum_{j notin Fbar} phi_{-zbar_j}(B_-(j)) <= t/q_0 + 2t,
  sum_{j notin Fbar} phi_{zbar_j}(Delta B(j)) <= 2t/q_0 + 4t,
and on Fbar the flip bounds of Lemma lem:flip hold with the finite set Fbar. That is: every inequality of Lemmas lem:switchbudget,
lem:split, lem:flip used in Section 8 holds for the "proxy" data (Fbar, Kbar, zbar) with the constants t/(2q_0), t/q_0 replaced by
t/q_0 + 2t, 2t/q_0 + 4t.
Proof. Off F: Lemma lem:switchbudget. On F cap (M, infinity): phi_{s_j}(x) = 2(s_j x)_-, and (s_j B_+(j))_- <= |a_j|/t + f^+_j,
(s_j B_-(j))_+ <= |a_j|/t + f^-_j (definition of f^+-_j), with sum_j f^+-_j <= t/(4q_0) (Lemma lem:flip) and sum_{j > M}|a_j|/t <= t.
The Delta B bound follows from Lemma lem:phicalc(b). QED
Consequence. Every window argument of Section 8 that uses only (i) these budget inequalities, (ii) the block lemmas, and (iii)
statements about finitely many carriers, applies at an infinite-F first row on each window with the proxy (F_{<=M(T_lo)}, K cup far F,
z); finite-dimensional statements about the support (Lemma lem:finitebase, the no-flip radius a_min) must be replaced by the clamps of
Part 2. This is how Parts 2-3 were obtained. The proxy changes with the window (M(T_lo(l)) -> infinity), and this is where the
obstruction lies (4.5).
