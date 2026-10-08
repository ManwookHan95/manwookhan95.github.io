# E referee — part 3: averaging skeleton, rigidity, critical cross candidate, T1

## Averaging skeleton (E 2.1) — verdict: correct (the convexity bound); hypotheses are the crux, as E says
Re-derived: p*(f'+tg') <= sum_j w_j p*(f'+t h_j); j with s_j >= |t| use (i); j with s_j < |t| (then |t| > s_1, so (ii)
applies when |t| <= T_0) use p*(f'+t h_j) <= p*(f'+t gbar) + |t| kappa s_j. Sum_{s_j<|t|} s_j < 2|t| for dyadic s_j.
Minor: "Q <= rho^2 and J >= 4 kappa/(1-rho^2) gives <= 1 + t^2/2 <= s(t)" is backwards (1 + t^2/2 >= s(t)); E flags
"up to the standard quartic correction": a strict margin (e.g. J >= 8 kappa/(1-rho^2)) and small T_0 fix it.

## Rigidity at NA points (E 2.2) — verdict: correct as a restatement of A Prop 7.4(b) + Fact F(a); the
## interpretive title "two-sided resources are indispensable" is broader than what is proved
Proved content: two t-LINEAR decompositions (B+,Om+) on (0,r], (B-,Om-) on [-r,0) of the same h at an NA point f'
(finite supp a' cup K'), with B+- supported in supp a' cup K' (which Prop 7.4(a) derives from admissibility + h(x')=0),
coincide: B+ - B- in c_00 cap L*(V*) subset c_00 cap Y = {0}, then L* injective. Om+- automatically bounded (linear
admissibility on (0,r] gives |Om(k)| <= ~2/r off peaks), so Fact F(a) applies. Correct.
Not proved: that the frozen certificates h_j of the skeleton (condition (i): a two-sided BOUND on |t| <= s_j) must
consist of two-sided resources. (i) does not require a linear decomposition; at NA points scale-dependent mechanisms
using infinitely many far weak peaks of w' (peak sets are typically cofinite) are not excluded (A Cor 7.5 only says a
defect mate at an NA point lacks a linear decomposition on one side). E's own T4 uses side switching at f'.
Fine one-sided structure (derived here): a one-sided (t>0) linear decomposition has Om = omega - d w with
d = <Dw, D omega>/C, omega = 0 on supp alpha, sigma_k omega(k) <= 0 on P \ supp alpha (downward use only of peaks
with alpha_k = 0). So "peaks used one-sidedly" in a LINEAR decomposition are exactly the alpha-null peaks.

## Critical cross candidate (E 1.2) — verdict: correct with fixable gaps (and it is NOT a counterexample)
Checks: v = (e_j* - xhat_j a)/norm has v(xhat) = 0 (a(xhat)=1). At f the k_i are off-peak with w(k_i) = 0 (full gap).
Mate property for small c: plausible (base first-order cost |t| c K lambda_i (1 -+ 1/2) = O(t^2) since z = 1/2 on B_i;
box needs lambda_i >= 2|t| c n_i/M; Hilbert ~ t^2 c^2 n_i^2/(2 m^2 C); large |t| by monotonicity of (s(t)-1)/|t|).
Destruction: sigma_i(x') = avg_{B_i} z' - c_i x'_{j_0} -> -c_inf xhat_{j_0} = -1/2 for z' in c_0; peaks if K large.
Gaps: (1) as written u_{k_i} = (v + K lambda_i sigma_i)/n_i is in c_00 (a, e_j*, sigma_i are finitely supported),
contradicting Y cap c_00 = {0}; one must add Y-perturbations of size << min(K lambda_i, Phi(k_i)) (to keep k_i off-peak
with gap ~ M at f, and to keep their own free tail mass below the conversion threshold of Cor 6.2). (2) With a' != a
the shift V = v(x' - xhat) re-converts a band near lambda ~ 2|V|/K, so the off-peak set at f' need not be an initial
segment (still finite) — E's later "conversion band" (2.4). (3) The candidate lies in cl Cert(f) by Cor 5.2/A Cor 6.10(c)
(gap M, rate K lambda_i, geometric scales), hence is recovered along EVERY sequence by Transport; destruction of the
fine coordinates at f' is irrelevant because each averaged certificate uses finitely many coarse coordinates, which
are off-peak at f'_n for n large (w'_n(k_i) -> w(k_i) = 0 for each fixed i). E agrees (part 5).

## T1 two-piece mates (E 1.4(i)) — verdict: unclear in general; correct (SKETCH) for d-neutral carriers
E's sketch = A-referee §5.4 (eta-masses on finitely many contacts of f + far truncation). It omits the d-mismatch:
side-minus block part W = omega - d w transfers to W'' = omega - d'' w'', so matching the two one-sided representations
of the SAME g'' forces the base to absorb E'' := d'' L*w'' - d L*w (plus far tail). E'' sits at non-contact window
coordinates with first-order cost ~ |t| ||E''||. Since the eta-masses move a (hence e, x'', Lx'') by ~eta, and
x -> L*J_V(Lx) is not Lipschitz (A-referee 5.5: ||L*(w''-w)|| ~ eta * #{off-peak k: Phi(k) >~ eta} + sum_{Phi<eta} Phi),
||E''|| >~ |d| eta (at least), while the side switch at |t| ~ eta needs ||E''|| <= (1-rho^2) eta/6.
So the argument works when Delta d = d- - d+ = <Dw, D(omega- - omega+)>/C = 0 (A-referee "general form": enforce
Delta d'' = 0 by one linear condition), e.g. carriers at coordinates with w(k_0) = 0, and is incomplete otherwise.
Existence of Delta d != 0 two-piece mates: plausible (fixed-point sign condition), not checked.
