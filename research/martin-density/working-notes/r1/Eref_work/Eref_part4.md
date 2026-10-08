# E referee — part 4: conversion bands, NC, T4, Lemmas 6.1-6.4, Prop 8.2, Gordan

## Conversion bands (E 2.4) — verdict: correct (algebra), with a cost bookkeeping slip
Threshold: k peak iff m|u_k(x')| >= Phi(k) M'|zeta'|/C'; with u_k = (v + K lambda_k sigma_k)/n_k and lambda = m Phi this
is |rho_k| >= theta~ := M'|zeta'| n_k/(C' m^2 K) (approximately constant). With sigma_k(xhat) = theta~(1+delta) and
V := v(x') = -K Lambda_0 theta~(1+delta) and sigma_k(x') = sigma_k(xhat) + o(1): rho_k = theta~(1+delta)(1 - Lambda_0/lambda_k);
|rho_k| < theta~ iff Lambda_0 (1+delta)/(2+delta) < lambda_k < Lambda_0 (1+delta)/delta: ratio (2+delta)/delta. CORRECT.
Slip: ||Delta f'|| = O(K Lambda_0) is too optimistic: a window/Delta a move of size s also changes w'(k) at every off-peak
coordinate with Phi(k) >~ s by ~s/Phi(k), and saturates below; ||L*(w'-w)|| ~ s #{off-peak k : Phi(k) >= s} + O(s),
i.e. up to O(s log(1/s)) (A-referee 5.5). Still o(1), so the conclusion survives. Gap inside the band varies from M
(centre) to 0 (edges) — E notes this.

## Candidate NC is a mate (E 3.1) — verdict: correct with fixable gaps (mate property plausible); design
## constraint as literally stated is INCONSISTENT with Lemma B
Checked: u_P(xhat) = u_N(xhat) = 0 (F-compensation); P carries t c v0 at t>0 with base B = c Z_P - c Z_P(xhat) a,
B(xhat) = 0, first-order excess sum_l |t c Z_l|(1 - z_l sign) = t c sum |Z_l| gamma_l <= t c eps_0 c_gamma lambda_P = O(t^2);
at t<0 the same carrier costs ~2|t| c |Z| (one-sided). N symmetric. d = 0 since w(k) = 0. Base Hilbert part small
(U* is w*-to-norm continuous on bounded sets, so ||U* e_l*|| -> 0; the a-multiple is killed by P_perp). OK.
Problem: "every coordinate with j-mass carries errors of size >= eps_0 (j-mass) on near-contacts" contradicts density
of every tail of (u_{k,m})_k in S_{q*}: there are infinitely many k with ||u_k - v0hat|| < eps for every eps. The
consistent version: good approximants of v0 exist only at scales lambda_k <= psi(error) with psi super-fast (rates
are free; values are not). This only affects E's explanation of why earlier tricks fail, not the mate property.
Also as written u_P, u_N are in c_00 unless the "negligible Y-tails" are added (they are mentioned here, unlike 1.2).

## T4 kills NC (E 3.2) — verdict: correct with fixable gaps (plausible SKETCH)
Re-derived the three regimes. (a) |t| <= M lambda_{N*}/(2 rho c n): block carries t rho c n u_{N*} (w'(N*) ~ 0);
base absorbs t B_0 on eta-contacts: t<0 increases |a'_l|; t>0 no flip while t rho c|Z_l| <= eta_l = kappa |Z_l|,
kappa = M lambda_{N*}/n. (b) t<0: base direction rho c (Z^tail_{N*} - Z_{N(t)}) + (a-mult): Z_{N(t)} part z-signed and
cheap; Z^tail wrong-signed, cost 2|t| rho c ||Z^tail||, absorbed by slack once ||Z^tail|| << (1-rho^2) lambda_{N*}.
(c) t>0: rho c (Z^tail_{N*} + Z_{P(t)}) + (a-mult), both z-signed. Head coordinates untouched in (b),(c). Correct.
Gaps: (1) B_0 must be -rho c (Z^head - Z^head(xhat) a): without the a-multiple g' - rho g = -rho c Z(xhat) a + ...
has FIXED size ~ rho c eps_0 (E's displayed "g' = rho c v0 + rho c Z^tail" is wrong by this multiple of a; the
"g'(x') = 0 normalization" item of the bookkeeping list covers it). (2) The eta-masses change e' = U*a'/||U*a'|| by
~ kappa eps_0 (cannot be avoided: U* injective and the masses sit off supp a), which shifts u_k(x') at scale ~lambda_{N*}
by a RELATIVE amount ~eps_0 (not small if eps_0 ~ 1): N*, N(t), P(t) near lambda_{N*} may lose gap or become peaks.
Fix: finitely many linear conditions (carriers at scales >= lambda_{N*}/2) via window moves of size O(kappa eps_0
x condition number) -> 0; plausible, not written. (3) Hilbert terms and C', M', |zeta'| perturbations: routine.

## Lemma 6.1 (duality) — verdict: correct (PROVED)
"<=" trivial; ">=" via (E_perp)* = l_1/(E_perp)^perp = l_1/E (E finite-dim, hence w*-closed; bipolar). Density of
c_00 cap B_{E_perp} in B_{E_perp}: truncate eta_N = eta 1_{<=N}, correct by zeta_N supported on a finite injectivity set
S subset (W,inf) for E (dual map R^S -> E* onto), ||zeta_N|| -> 0, rescale by 1/(1+||zeta_N||); y(.) converges by dominated
convergence. Correct.

## Cor 6.2 — verdict: correct with a cosmetic inconsistency
(a) uses only the trivial direction (valid for any eta in l_inf annihilating E, here (z'-z)1_{>W}, ||.|| <= 2; it is
NOT in c_0 when z is not, but no c_0 is needed). Correct. (b) Lemma 6.1 gives eta in c_00 with ||eta|| < 1 and shift
exactly s for |s| < tau_k, but z' + eta must stay in B_{c_0}: the achievable shift is limited by the room 1 - |z'_l| on
supp eta (and is one-sided where the tail of u_k sits on near-contacts of f with z' = z there). E's own parenthetical
(eta/2 when |z'| <= 1/2) gives shift s/2, so "destroyed <= 2 x shiftable" becomes "<= 4 x" in that case. Harmless.

## Lemma 6.3 — verdict: correct (special case of A Fact F(b)); should say (k,m) != (k',m'); c = 0 included.

## Lemma 6.4 — verdict: first statement correct; consequences HEURISTIC as labelled
Image of B_{c_0(W,inf)} under psi_{>W} is an interval containing +-S_N for all N; sup not attained when supp psi_{>W} is
infinite (equality forces |z'_l| = 1 on supp). "plus an endpoint" should read "plus both endpoints" (finite support);
psi_{>W} = 0 degenerate. Neutralization z' = z on [1,W] with psi((z'-z)1_{>W}) = 0 needs |psi_{>W}(z)| < ||psi_{>W}||_1: OK.

## Prop 8.2 — verdict: correct; in fact trivially stronger
(F1) gives y'_n = z'_n + U e'_n -> xhat weak*, so y(y'_n - xhat) -> 0 for EVERY fixed y in l_1 (dominated convergence),
uniformly on norm-compact subsets of l_1 (equicontinuity), not only for window-supported y. Consequence "window moves
give one parameter V" holds exactly when the normalized core errors sigma_k range in a norm-compact set (e.g. a bounded
subset of a fixed finite window space); resources whose core errors spread over growing windows are partly "far" and
CAN be shifted individually. E's model assumes the fixed-window case.

## Gordan equivalence (E 7.3) — verdict: correct with fixable gaps
Achievable carried core errors on side t>0 form cone{tau_k sigma_k} (P- upward: tau = +1; P+ used downward: tau = -1),
on side t<0 the negative cone; so (A3) read as "no nontrivial nonnegative combination of the tau_k sigma_k vanishes"
is equivalent (Gordan) to existence of Lambda with Lambda(tau_k sigma_k) > 0 FOR FINITELY MANY k. For the infinite
family of resources (all scales) Gordan's alternative FAILS: e.g. a_k = (1, 1/k), a_0 = (-1, 0) in R^2: no nontrivial
vanishing nonnegative combination, yet no Lambda is positive on all a_k. The right statement (and the one an obstruction
needs, since approximate cancellations are as useful to the approximant as exact ones) is: exists Lambda with
inf_k Lambda(tau_k sigma_k)/|sigma_k| > 0  iff  0 notin closed convex hull of {tau_k sigma_k/|sigma_k|} (separation in
finite dimensions). Also "useful" combinations need nonzero v-component; the exact condition is a Motzkin/Farkas
condition on the vectors (tau_k sigma_k, tau_k/n_k); Gordan's Lambda is sufficient, not necessary, for that reading.
