# V2-ref part 3 — the shift-extended system, Theorem C1, Corollary C1.1, Theorems E^>= and E^SC

Sources re-read: Y1 Lemmas 3.1-3.6 (r6/Y1_notes.md part 3; Y1-ref m2, m5, F2), V1 2.5 (Lemma 3.4', shift patterns, Lemma S),
Z3 Lemma 5.1 and identity 5.2, Z3 Theorem E (r5/Z3_notes.md 2.2), the note's def:twopiece, def:SC, thm:engineered, cor:D1.

## 1. Lemma 3.1 (relations (R1)-(R7) of the actual decomposition).  VERDICT: CORRECT (PROVED).
Re-derived from the refereed sources, with the decomposition convention delta_m = Delta d_m M_m, Delta d = d_+ - d_-:
* (R1) Y1 Lemma 3.2: sum_G (tau)_- <= K_g t (all of G, peaks included). ✓
* (R2) Y1 Lemma 3.3(b),(c) (= eq:peakshift): anti type -tau/lambda - delta = Y, swallowing type tau/lambda - delta = Y,
  0 <= Y <= t/(lambda mu): |tau - eps vs lambda delta| <= t/mu <= C_f D t/u at peaks of kappa (relative margin >= u/2). ✓
* (R3) e_0 = Delta B 1_{F^c} - V(tau) (Y1 Lemma 3.2); on T(l) the closing (C2) only RAISES (no flips), so Z3 Lemma 3.2 gives
  phi_{z^#} <= 2 phi_z there; contacts: phi_z(x) = 2(zx)_-; free coordinates of kappa: phi_z(x) >= (1-|z|)|x| >= u|x|. ✓
* (R4) eq:didentity: Phi w Delta theta/(mC) = -q tau for G-carriers; class R and fine carriers <= (K_g t + t^7)/(mC); nearly
  neutral carriers |q tau| <= b Phi M 6 lambda/(m C t) <= t^3. ✓  (Consistency check I did: in terms of two-piece DATA the same
  identity reads Delta^{data}(1 - sum_{Omega} Phi^2 w^2/C) = sum q tau^{data}; the decomposition version carries the non-switching
  carriers' shift traces in the class-R/fine error, which is why the coefficient of delta is 1.)
* (R5), (R6): Y1 Lemma 3.4 read half by half (V1 Lemma 3.4', V1-ref confirmed: each half uses only its own source).  (R6) is
  imposed only for class-R sources (U1)/(L1); for (U2)/(L2) the sign comes from (R1)+(R2) at the source peak, for (U3)/(L3) from
  (R4)+(R1)+(R7) — I checked that the system reproduces Y1's (U3) bound: delta(1 + sum |q| lambda rho) <= viol. ✓
* (R7) from the proof of Y1 Lemma 3.4 (U3) with gap <= b M: defect <= 3 lambda b/t <= t^3. ✓
Total violation <= C_f Design(l)^2 K_g t/u(w), uniformly in t in W(w). ✓

## 2. Definition 3.2 and the rate rho^sh.  VERDICT: CORRECT, with precision (P3.1).
rho^sh(kappa, f) = inf{viol(delta, tau) : ||delta||_1 = 1}: viol is convex, piecewise linear and positively homogeneous;
{||delta||_1 = 1} is a finite union of polytopes (one per orthant), so the infimum is an LP minimum, ATTAINED; "possibly
asymptotic solutions" is unnecessary (rho^sh = 0 iff an exact solution with delta != 0 exists).
(P3.1) The system Sigma^sh depends, besides kappa's G, signs, statuses and contact pattern on T(l), on window-dependent
CLASSIFICATIONS: the nearly neutral set (q' := 0 there), the anti-type near-threshold set of (R7), I_sh with its source halves
and source types, G_pk/G_np (tiny-margin peaks declared non-peaks), and F ∩ T(l).  For rho^sh to be a rate object (a number
attached to a design-countable object and depending on f only), the PATTERN must be enlarged to contain all these finite data
(at most 2^{O(l + |T(l)|)} choices per level — design-countable, N-free).  With this enlargement every statement holds; without
it "rho^sh(kappa, f)" would depend on b(w).

## 3. Theorem C1 (dichotomy).  VERDICT: CORRECT (PROVED).
Case (I): ||delta||_1 rho^sh <= viol(actual) <= C_f Design^2 K_g t/u (homogeneity), so ||delta||_1 <= K_sh t with K_sh = C_f
Design^2 K_g/u^2 <= C_f Design^3/u^3 for EVERY block simultaneously (delta ranges over all of I; (R5) rows give |delta_m| for
m notin I_sh).  The downstream uses of (SP_w)/(SH_w) are exactly "|Delta d_m| M_m <= K t for all m": Y1 Lemmas 3.5, 3.6 (Y1-ref
F2), V1 Step 0 of Prop. TR (V1-ref: Lemma S is used only through K_d').  No circularity: (R1)-(R7) come from Y1 Lemmas 3.1-3.3
and the proof of 3.4, none of which assumes a shift bound (3.5, 3.6 do, and are not used in Lemma 3.1).  Case (II) is the
complement at a clean sub-window.  Also: if I_sh = {} then rho^sh >= 1 (the (R5) rows alone), so Y1's (SP_w) => case (I). ✓
Relation to V1's (SH_w) (correction of my first reading; precision P7).  V1's shift cost c(delta; pi) sums phi_{z_j} over ALL j
notin F with the z of f, so it also charges switching through tiny-but-positive rooms (weights <= b on class-G signature sets and on
tiny target rooms).  For the ACTUAL decomposition these extra terms are negligible (b tau <= 6 b lambda/t << t^3), which is why V1's
Lemma S pins the shift when c_pi >= u.  But rho^sh is an infimum over ALL tau (no box), and a near-solution of Sigma^sh may need a
large tau (of order 1/(a small f-dependent minor of Sigma^sh)), for which b ||tau||_1 need not be small; so I cannot derive rho^sh >= u
from c_pi >= u.  The two pinning criteria are independent sufficient conditions.  Consequence: the strongest combined statement is
MASTER THEOREM III': f in Rec if at infinitely many levels some clean sub-window has [rho^sh >= u] or [(SH_w) of V1] (both give
|Delta d_m| M_m <= K t for all m: Theorem C1(I), V1 Lemma S; Theorem B replaces (VR_w) in either case), and the residual (C*) is:
at all but finitely many levels EVERY clean sub-window has rho^sh(kappa(w), f) <= b(w) AND c_{pi(w)}(f) <= b(w) (so I_sh(w) != {}).

## 4. Corollary C1.1.  VERDICT: (a) CORRECT with precision (P3.2); (b) a correct reading.
(a) c^comb(delta; kappa) <= C Design viol(delta, tau) re-derived (x := tau_+ on G_np; L - V(tau) is controlled by (R1), (R2)
defects; phi_z 2-Lipschitz; the S^nat terms are (R1)+(R2) defects).  c^comb_*(kappa) is ONE number per pattern; the positive ones
form a finite set; delta_sh(l) := their minimum is a design constant.
(P3.2) Two small repairs: (i) the weight m^nat_{l'}(l) = ||v_{l'} 1_{S_{l'} \ (F ∪ T(l))}||_1 depends on F; replace it by the
design number ||v_{l'} 1_{S_{l'} \ ([1,l] ∪ T(l))}||_1 <= m^nat (valid since F ⊂ [1,l] for l >= l_f; this only lowers c^comb, and
c^comb <= C Design viol still holds), or put F ∩ [1, s_max(l)] into the pattern; (ii) the minimum over the "sign-sphere" must
be taken over {||delta||_1 = 1, delta in the (R6) sign cone}; for an arbitrary (delta, tau) project delta_{I_sh} onto that cone
(distance <= the (R6) violation; c^comb is C Design-Lipschitz in delta) and use (R5) for m notin I_sh: ||delta||_1 <=
(C Design/delta_sh + 2) viol(delta, tau).  Conclusion rho^sh >= delta_sh/(C' Design) > b(w) unchanged.
The point of (a) is correct and useful: once the pinning rate is itself a rate object, the pigeonhole forbids "positive but
decaying" pinning constants at clean sub-windows (Y2 5.3(c)); only exact/near-exact resonance (case (II)) remains.

## 5. Theorem E^>=.  VERDICT: CORRECT (PROVED).
In the proof of Z3 Theorem E (r5/Z3_notes.md 2.2) Lemma U is applied separately to the side-+ data for r > 0 and the side-- data
for r < 0 — each side represents g_{j,t_i} on its own, so (A) needs no relation between d(omega^+) and d(omega^-); the averaging
preserves side admissibility, the two representations and Delta d_m >= 0 (convex combination; d_m linear), and rho >= 0 keeps the
sign; Corollary cor:D1 at f_j assumes exactly Delta d_m >= 0 with the convention Delta d_m = d_m(omega^-_m) - d_m(omega^+_m) of
def:twopiece.  The same inspection applies to Theorem E' (Y1/Y2) and V1's Theorem E'' (banked/pulled supports; V1-ref).

## 6. Theorem E^SC.  VERDICT: CORRECT (PROVED), as a conditional statement.
rho gbar_j in C(f_j) with averaged data of kappa_w <= kappa' < 1 (Theorem E's proof); the averaged data have Delta d_m < 0 only
on blocks where some scale's data do, a subset of I_-; (SC) passes to subsets (the max over fewer blocks is smaller, same
sequence); thm:engineered at f_j (I finite, F_j finite, rho'_j^2 kappa' < 1) gives (f_j, rho'_j rho gbar_j) in cl NA; the sequence
converges to (f, rho g) in norm (eps_j + rho(1 - rho'_j) p*(gbar_j) + rho p*(gbar_j - g) -> 0).  Note (precision): the hypothesis
should read "Delta d_m <= 0 ... and Delta d_m < 0 only for m in I_-" (data at different scales may have Delta d_m = 0 in some
blocks of I_-); the proof covers this.  How (SC) can be obtained at companions is not addressed (it is a hypothesis).
