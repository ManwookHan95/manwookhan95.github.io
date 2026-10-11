# G1-ref part 4: Lemma 5.1, Prop. 5.2 / Cor. 5.3, Cor. 5.4, Lemma 5.5, Theorem G1.D, persistence

## 4.1 Lemma 5.1 (one two-(X3) strict minor) -- CORRECT IN ISOLATION; scope gap G-S2
Form: multilinearity in the rows (X3)_m, (X3)_{m'} gives M = x^T D y + E^T x + F^T y + G with design coefficients.  dM/dx_l is
(up to sign) the minor obtained by deleting (X3)_m and the column gamma_l: a minor of the cone matrix with one (X3) row, hence a
rate object, tiny or robust at the start.  (i) robust first cofactor: one ratio move of size <= (1 + 2Lip)b/(u/2) zeroes M.
(ii) all first cofactors tiny: A_x, A_y nonempty within Des^2 b (Lemma LE (b)); on A_x x A_y, M = F^T y + G = E^T x + G, so M is
constant there, equal to its value at Cramer points, a ratio of design polynomials, hence 0 or >= delta'_comb/2^{L^4} >= 1/Des;
|M(x^#, y^#)| <= b + Lip 2 Des^2 b < 1/Des forces 0.  Re-derived; G1's me2_check reproduced in spirit.
G-S2 (scope).  The lemma treats M ALONE.  If block m (or m') also carries single-(X3) tiny strict minors (affine set A_m), case
(i) moves one ratio off A_m and case (ii) projects onto A_x, not onto A_m cap A_x.  Restricted to A_m x A_{m'}, M becomes a
bilinear form whose first derivatives are design COMBINATIONS of first cofactors -- not rate objects -- and can be of
intermediate size.  Explicit model (ref_me2_system.py/.out): M_1 = x_1 - x_2, M_1' = y_1 - y_2, M = x_1y_1 + x_2y_2 + (x_1 - x_2)/2 +
(y_1 - y_2)/2 (design coefficients; on A_m x A_{m'}: M = 2st); start s = t = sqrt(b/2) with all tiny minors <= b and ALL four first
cofactors of M ~ +-1/2 (robust).  Lemma 5.1 (i) zeroes M but leaves |M_1| ~ 2.3 b; the joint zero set {M_1 = M_1' = M = 0} is at
distance 1.00 sqrt(b) (b = 1e-4 ... 1e-10), i.e. 1e2 ... 1e5 times b: a NON-linear displacement.  So "Lemma LE (and Lemma 5.1 for
a single two-(X3) minor) gives the (T1) targets" (proof of G1.D) is false when the two-(X3) minor shares a block with
single-(X3) tiny minors.  (Realizability of the model inside an actual class cone is not checked; the point is that G1's
argument does not exclude it.)
FIX: (a) state Lemma 5.1 for a two-(X3) minor that is the ONLY tiny strict minor involving the ratios of its two blocks; (b) in
Theorem G1.D read (R-S2) as G1's notes define it -- "some tiny strict minor contains >= 2 (X3) rows and the strict system has no
point of Z^str within Des^C b of the start compatible with the one-sided constraints" -- and (c) generalize Theorem G1.C and
Lemma 5.5 from prod_m A_m to an arbitrary compact k-semialgebraic Z^str, starting from such a point (see 4.4).  Then the
theorem's statement is unaffected; the model above is an (R-S2) stage.

## 4.2 Proposition 5.2, Corollary 5.3 -- CORRECT in the restricted linearized model (precision P-52')
Farkas: the system sum_P a_l C'_{.,l} + sum_Q b_l C_{.,l} + sum_g c_g D(g) + sum_h e_h D(h) = -M(rc), a, e >= 0, b, c free, is
infeasible iff some lambda has lambda^T C'_P >= 0, lambda^T C_Q = 0, lambda^T D(g) = 0, lambda^T D(h) >= 0, lambda^T M(rc) > 0:
exactly (a)-(c).  Generator action: Delta r^(m) = (c u^(m)(s) - r^(m) dkappa)/kappa_m; the second part changes M_i by
-(dkappa/kappa) M_i(rc) (Lemma 4.4), which the linearization drops: it is a product of a tiny value and the move size, so the
linear model is exact only to first order -- consistent with G1's label "first order at the start row".
P-52'.  As in H2-ref P-41: the "iff" holds for the restricted LINEAR model; the converse "no certificate => realization" needs
strict feasibility with a margin of order rho_0^nat (degenerate feasible systems can be destroyed by the second-order terms and by
the bands' side effects), so the actual residual is CONTAINED in the certificate class (a necessary condition), not equal to it.
Cor. 5.3: (i) Lemma 4.4 for strict minors (D(s) = 0 at the minor's own FR rows); (ii) a single minor: lambda is a nonzero scalar and
(b) forces D_M(g) = 0 for all two-sided g; (iii) D_M(s) = det[[u_+(s), u_-(s)], [u_+(j), u_-(j)]].  Kind-(iv) carriers have no
private two-sided design-depth resource, so only SHARED FR coordinates (and TS generators) enter -- G1's wording is right.
Additional remark (supports G1's main obstacle): f decides which shared target coordinates are free; if all shared targets
except j are contacts, the only remaining generators are one-sided banks/raises with D_M(bank at s) = z_s det[...], whose signs
are f's contact signs.  So a FREE-target strict resonance with adversarial contact signs elsewhere is consistent with every
proved constraint at a single stage; design genericity of target values alone cannot exclude it (G1's next step (1) would need
an additional structural input, e.g. a second FREE shared target).

## 4.3 Corollary 5.4 (contact-row resonances realized) -- CORRECT (mod chain), precision P-54
H2 Ex. 4.3 shape with j a CONTACT target: j is in T(L) cap U_L at depth <= dbar(L), banked by P^nat; (X1-c)_j is cushioned, so M is
SOFT; |M(rc)| <= (1 + 2Lip)b << mu_tol and the bank moves M only by the factor of Lemma 4.4.  l_+- are free or softly pinned and
need only (E2).  P-54: the conclusion "the block is not residual" should read "this resonance does not make the block residual":
the block can still be residual through other strictly pinned rows, through locked K^+ rows of protected blocks ((R-L)), or because
H2.A's band set (G-T2) is restricted there.  Also note the realized set now consists of every resonance whose tiny minors all
contain a cushioned row, as G1 says.

## 4.4 Lemma 5.5 and (NT_0) -- CORRECT; generalization recorded
The proof uses only: Z^str compact and k-semialgebraic (k = field of the non-N_T design data incl. robust-peak and (KN) weights,
Lemma III-weightfree (a)); psi_d defined over k; genericity of Phi^T over k (GEN); H1's stratified projected flow (Lemma 2.2)
and the first-order margin argument of J1.11 for Z^str in place of Z_kappa.  Affineness of Z^str is never used, so Lemma 5.5
holds for every pattern with Z^str := {r in K_kappa : all tiny strict minors vanish} (needed for G-S2 (c)); the coincidence set
for Z^str is again k-semialgebraic of dimension < |N_T| and is avoided by algebraically independent weights (no new insertion
beyond P-CHOICE for eps_0, m_0, V).  Precision P-55: in the covering argument use balls B(r_*^i, delta_i/2) and the local step on
B(r_*^i, delta_i), so the curve from y in a half-ball stays where the step is valid ((3/16) delta_i/V margin suffices then).
(NT_0): PROVED (part 3, 3.4).

## 4.5 Theorem G1.D (residual) -- reduction CORRECT (mod chain) at stages without thick-type carrier after G-S2, G-T2, Q-1;
## thick-type part SKETCH (honest)
Proof check.  At a stage with none of (R-S1)-(R-S3), (R-L): the (T1) targets exist (Lemma LE + one-sided Hoffman when all tiny
strict minors are single-(X3); otherwise the negation of (R-S2) as defined in the notes supplies an exact compatible point within
Des^C b); (T3) targets exist by Lemma 5.5 (general Z^str) unless (R-S3); A-regularity of the band-relaxed system follows from
Theorem H2.A's proof with "pinned" -> "strictly pinned", using H2.A's band set (which respects protection, G-T2) -- softly pinned
rows are banded like free rows since beta_1 <= Des^C b/u << kappa_min D_tol (needs C_T large, P-23); Theorem G1.C then gives the
companion.  I checked that H2.A's proof uses pinning only to exclude bands on pinned rows, so the substitution is legitimate.
Q-1 (quantifiers, as H2-ref Q-1): "at all but finitely many main stages the selected stage has one of ..." must read "at all but
finitely many main stages, EVERY clean sub-window w and EVERY class a with >= n(w)/D_cl(w) scales has one of ...": failure of
(LSC-trunc) means no (w, a) is realized.
Thick-type stages: the transfer of H1's first-order lever lemmas to x^nat with strict pinning is plausible (they are first-order
and scale-free) but unwritten; SKETCH is the right label.  (H-6') "reduced to (R-S2) and thick peaks of shifted blocks": the
(X4^0)-minor part is soft (correct); the cofactor-polynomial part disappears (Cor. G1.B (iv), correct).

## 4.6 Persistence -- CORRECT as a necessary condition (with Q-1)
An (R-S1) block needs a tiny NONZERO strict minor (a vanishing one is already exact), i.e. an approximate linear relation
<C, r^(m)> ~ 0 with coefficients minors of target values at FREE target coordinates with robust room, wrong-signed at the start,
annihilated by every two-sided generator, opposed by every one-sided one; freshness at consecutive (R1) stages is H2 Lemmas
2.6/2.7 (H2-ref Q-2: consecutive stages).  Nothing here shows such f exist or do not exist.

## 4.7 Counterexample / density claims
None made; none implied.  Every residual class is a stage-wise near-coincidence of f's ratios with a design linear (or
multilinear) relation plus sign conditions, renewed at every main stage.
