# Referee report on Z1 (Round 4): Lemma Z via far lowering and scale decoupling

Files checked: r4/Z1_notes.md, which is identical to the concatenation of Z1_head.md and Z1_part1-5.md (checked with diff).
Imports re-checked against r3/G3_notes.md and G3_ref_notes.md, r3/S3_notes.md (Theorem D, Cor D1), r2/P2_notes.md (1.6, Lemma 1.4),
r1/C_notes.md and C_referee.md (Remark 7.1') and BRIEFING_R2.
Setting: canonical base, finite block set I_N (p_N, every N; martin-tail transfers to p), SLD operator T of G3.
Detailed checks: Z1_ref_part1-5.md; assembled with proofs: Z1_ref_notes.md; scripts: Z1ref_work/.

## 0. Bottom line
- No counterexample is claimed, and nothing here points to one. Density remains OPEN; Lemma Z remains OPEN.
- Most of Z1 is correct:
  - the R_0-approximants;
  - the exposed-face lemma itself;
  - the local reduction;
  - **Theorem B\***: window-pinned mates are recovered at any f with finite F;
  - the ray lemma;
  - the approximants f^L and the (A)+(B) reduction;
  - the flip lemma;
  - bounded free switching.
- Theorem B^inf is a reasonable SKETCH.
- There are **two substantive errors**:
  1. **The "common-functional obstruction" (Z1 5.2, table #15, "PROVED") is not an obstruction.** It comes from fixing the + component's functional
     as g - Rem_+(t). Windowed averaging only needs some functional within O(K t) of g. Under Z1's own exact-resource hypotheses (E1), (E2),
     two steps produce, at every window scale, ONE functional with exact, balanced, d-neutral two-piece data:
     - trim the + side's contact base by O(K t);
     - Hoffman-project the free switching onto the polyhedral cone of exact d-neutral resonances.
     Windowed averaging and S3 Cor D1 then recover every mate. This gives the referee's **Theorem M (SKETCH): finitely swallowed points with exact
     free resources are in R.** Of Z1's remaining step (RS1), only the near-resource case (O-a) is left.
  2. **Z1 1.3 is a non sequitur.** "rho C(f) subset C(f') forces f' = f" does not follow from the exposed-face lemma. Only the sufficient
     primal condition (*) fails. The pattern of inference is false in ell_4^3. This claim is not load-bearing.
- Several labels must be downgraded to HEURISTIC: 2.4(b) "not below", 2.4(c), 3.1(d), and (O-c) as an impossibility statement.
- Two reformulations are imprecise and should be fixed:
  - Lemma Z is a per-mate statement;
  - the reduction 3.3 needs (B) for all f when F is infinite.

## 1. Verdicts
| # | Z1 claim (label) | Verdict | Key point |
|---|---|---|---|
| 1 | R_0-approximants; Lemma Z purely lsc (PROVED) | correct with fixable gaps | f' construction and continuity re-derived (dominated convergence for R_m**, Smulian, L* weak*-to-norm). Far lowerings must also truncate a when F is infinite. "rho C(f) subset Li C(f'_n) along ONE sequence" is stronger than Lemma Z (per mate) and is not shown to be equivalent |
| 2 | Exposed face; hence rho C(f) subset C(f') forces f' = f (PROVED) | wrong (the "hence") | The lemma is right; Z1 asserts zeta_m != 0 without proof, and it is true because R_m** is injective on l_inf. The consequence is unproved. The exact criterion is f'^2 + rho^2 r~_f^2 <= p^2, and the normer only gives C(f) subset ker xi'. In ell_4^3, C(e_1*) = {0}. Positive fact: C_base(a) subset C(f') for every f' with base part a |
| 3 | Local reduction 1.4 (PROVED) | correct | Re-derived; numerics max violation 0 |
| 4 | Theorem B* (PROVED) | correct | (SR) and gamma enter G3 only through 3.4's conclusion; 3.5, 4.1-4.2, 5.1-5.3 use only that conclusion, F finite and the window arithmetic. The hypothesis is needed only on the n_j dyadic scales and only for coarse l |
| 5 | Ray lemma, budget form (PROVED) | correct | Line by line; identity (1 - tau beta_0)(1 + tau_0 X) = 1 + tau Delta1 checked. 2.4(b)'s "in general NOT below" and 2.4(c)'s necessity are HEURISTIC (no lower bounds) |
| 6 | f^L, coarse data kept, fine carriers roomy; (A)+(B) => density (PROVED; A, B OPEN) | correct with fixable gaps | Design adjustment unnecessary (disjointness suffices). For F infinite, (B) must be stated for all f; part 4 covers only (SR) points. "Neither implies the other" is unproved |
| 7 | (O-c) naive averaging + S3 Thm D fails (PROVED) | correct with fixable gaps | The arithmetic is right; re-derived independently (needs p*(f' - f) <~ n(1 - rho^2) t_n^2). The premise p*(f' - f) >~ s_1 is generic, not proved. It is a statement about one method, and it disappears for EXACT matching (see #10) |
| 8 | Flip lemma (PROVED) | correct | Re-derived; 2*10^5 random checks |
| 9 | Theorem B^inf (SKETCH) | correct with fixable gaps | Clamp, truncation and the (C-a') version of 5.1 checked (the base relative error is O(c_1), absorbed). The import is the C referee's two-line extension of Remark 7.1' to b != 0 |
| 10 | Bounded free switching (PROVED) | correct | Injectivity via Y cap c_00 = {0} and T injective; the slaving closure is finite |
| 11 | Common-functional obstruction (PROVED, algebra) | wrong | Algebra right inside Z1's rigid model; conclusion false under (E1), (E2) (Theorem M, SKETCH). Z1's "iff" criterion ignores trimming of the + base. Counterexample to the criterion: one coordinate, B_+ = 1 + eps - beta, B_- = -beta, J = eps |

## 2. Main finding: Hoffman matching (Z1_ref_part5 5.3-5.5)
Setting of Z1 part 5. F is finite. U* is finite and slaving-closed, and (SR) holds off U*. (E1): free carriers are strict non-peaks.
(E2): supp u_l \ F is contained in K for l in U*. K_* := union_{U*} supp u_l \ F.
1. **The cone.** R_0 := {xi in R^{U*} : z_j (sum_{U*} xi_l u_l)(j) >= 0 on K_*, sum_{U*, m(l)=m} xi_l u_l(xi) = 0 for all m} is POLYHEDRAL.
   Off the finite set G_0 = union_{U*} supp y_l, a point of S_l carries only u_l's signature, so all constraints there reduce to eps_l xi_l >= 0,
   or to xi_l = 0 when z has both signs on S_l.
2. **Violations are O(K t).** The actual switching xi° = -Delta c|_{U*} violates every constraint by O(K t + t). Three facts give this:
   - Delta B 1_{K_*} = v_{xi°} + J_t with ||J_t|| <= (4/3) K t; pinned signatures never meet K_* (slaving closure);
   - the wrong-signed contact mass is <= t/(2 q_0) (G3 2.3(b));
   - d-neutrality: sum_k Delta c_k u_k(xi) = <Delta Omega_m, zeta_m>, which lies in [-t, t] by G3 2.3(a).
   The last fact also gives |Delta d_m| = O(K t) at finitely swallowed points, which G3 3.5(c) does not give there.
3. **Projection and trimming.** Hoffman gives xi_t in R_0 with |xi_t - xi°| = O(K t). Trim z_j P(j) := (z_j(B^cl_+ - v_{xi_t})(j))_+ and put V := B^cl_+ - P,
   W := V - v_{xi_t}. Then V is z-signed, W is (-z)-signed, and ||P|| = O(K t).
4. **The two sides.**
   - + side: G3's clamped certificate on the pinned carriers, the unclamped free coefficients, and base B_+ 1_F + V - kappa a, with kappa = O(K t).
   - - side: the free coefficients are shifted by xi_t/lambda, and the base is b^+ - sum xi_t u_l.
   Both represent the same Psi_t exactly, because Delta d(xi_t) = 0, and ||g - Psi_t|| = O(K t). Each side is an O(K t)-perturbation of the actual
   decomposition on that side. Hence Gamma_w <= 1 + eta_0/2, and the one-sided version of 5.1 holds (Step 3(iv) needs a one-line change for free
   coordinates moved away from the peak level).
5. **Conclusion.** Windowed averaging (G3 5.2, + side for s > 0 and - side for s < 0) gives rho Psi in C(f) with exact d-neutral two-piece data
   (P2A 1.6) and kappa_w <= rho^2(1 + eta_0) <= 1. S3 Cor D1 then gives rho Psi in Ls(f), and Psi -> g.
Toy check (Z1ref_work/hm2.py: three free carriers, an O(1) exact resonance, junk and wrong-signed mass of size eps):
|xi_t - xi°|/eps <= 5.1 and ||P||/eps <= 4.3 for eps from 1e-2 to 1e-5, with all signs exact.
The argument extends to finitely many inexact coordinates in the free supports (equations instead of inequalities).
It does NOT cover infinitely many near-contacts (|z_j| -> 1) in a swallowed signature set. There the components carry Delta1 > 0, so the
data are not in P2A 1.6's format. That is the genuine O3 core, now localised.

## 3. Other findings
- **1.3.** Exact criterion: rho C(f) subset C(f') iff f'(x)^2 + rho^2 r~_f(x)^2 <= p(x)^2, with r~_f = max over C(f). By Goldstine, the only
  first-order consequence at xi' is C(f) subset ker xi'. So the conclusion holds at f exactly when C(f)^perp = R xi; that is not shown in general.
  Exact transfer of pure base mates (PROVED): if q*(a + s b) <= s(s) for all s, then p*(f' + s b) <= max(q*(a + s b), 1) <= s(s) for every f'
  with base part a. So the claim that every approximant loses part of rho C(f) is not justified.
- **Theorem B\*** is a correct and useful observation: the obstruction is a property of the mate (persistent switching through unpinned carriers),
  not of f.
- **f^L.** Z1 does not estimate p*(f^L - f). Heuristically it is O(c_{L+1}), which places the slack threshold at sqrt(c_{L+1}). That agrees with
  3.2(d).

## 4. Attacks tried (details in the part files)
- **Weak* vs norm.** Continuity f' -> f, smoothness of |.|_m at zeta_m != 0, compactness of L*: all fine.
- **Uniformity.** In t and in the window scale: B* inherits G3's quantifier order, with K_j T_hi(l_j) -> 0 and n^w/K_j -> infinity. The Hoffman
  constant depends only on f and U*.
- **Non-attained infima.** None are used (optimal decompositions exist by weak* compactness).
- **Signs and one-sidedness.** Flip and clamp inequalities, trimming signs, and convexity of the box in s were all checked.
- **c_0 vs l_inf.** z is allowed in l_inf throughout, and the f' construction needs only z' in B_{l_inf}.
- **Finite vs infinite F.** F infinite is handled by B^inf (SKETCH). 4.3 and Theorem M need F finite: Y may contain a when a is not in c_00.
- **Finite vs infinite peak and contact sets.** Infinite contact sets are allowed, and the Hoffman cone stays polyhedral because U* is finite.
- **I finite.** The p_N setting throughout, via martin-tail.
- **Hidden assumptions on T.** Z1 uses only Lemma B and SLD's (P1)-(P3); Theorem M uses the same plus allowedness (a) and slaving closure.

## 5. Corrections requested
1. 1.3 and table #2: replace "forces f' = f" by "the primal sufficient condition (*) fails for f' != f; the exact condition only forces
   C(f) subset ker xi'". Remove the "moral", or label it HEURISTIC.
2. 1.1: state Lemma Z per mate. Note that the uniform lsc version is a stronger, sufficient condition. Truncate a in the far lowerings when F is infinite.
3. 2.4(b) "in general NOT below", 2.4(c), and 3.1(d) (which depends on (c)): label HEURISTIC. Label (O-c) as an arithmetic statement about one method.
4. 3.3: state (B) for every f, or extend R_fin to infinite F via B^inf.
5. 5.1: add the O(t) wrong-signed contact mass and the d-coefficient bookkeeping (|Delta d| = O(K t) needs the first-order identity of 5.3(2)(ii)).
6. 5.2 and table #15, and (RS1): withdraw "cannot represent the same functional". Replace it by Theorem M (SKETCH), and restate the open part as (O-a)
   (near-resources, i.e. infinitely many inexact one-sided coordinates on swallowed sets) together with (B).

## 6. Assessment and most valuable idea
Z1 is careful and mostly correct, and it sharpens the reduction left by G3:
- Theorem B* moves the obstruction from first rows to mates;
- f^L and the (A)+(B) reduction localise it;
- bounded free switching makes finitely swallowed points finite-dimensional on the free side.
Its negative conclusion about common functionals was premature. With the trimming freedom and a Hoffman projection, the finitely-swallowed
exact-resource case closes (SKETCH).
What remains for density with the SLD operator:
- (O-a): near-contact tails and weak or near-threshold free carriers on swallowed signature sets (genuinely scale-dependent switching);
- (B): lower semicontinuity along f^L-type approximants at points with infinitely many swallowed carriers;
- the import of B^inf.
**Most valuable idea (referee's, building on Z1's 4.3 and B\*).** Hoffman matching. At a finitely swallowed point, the free switching at every
window scale violates the finitely many constraints that define the cone of exact d-neutral resonances by only O(K t). These are sign constraints
from the free signature sets, a few target constraints, and first-order d-neutrality, which is automatic up to O(t) by G3 2.3(a). Since that cone
is polyhedral, Hoffman's lemma projects the switching onto it at cost O(K t). Trimming the + contact base by O(K t) then yields ONE functional with
exact two-piece data on every window scale. Windowed averaging and S3 Cor D1 recover every mate. This removes Z1's "common-functional
obstruction" and confines the open core to inexact (near-resource) switching.
