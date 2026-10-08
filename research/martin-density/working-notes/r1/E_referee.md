# Referee report on Notes E (strategy E: adversarial counterexample search)

Referee: adversarial check of `ctx/r1/E_notes.md` (all 771 lines), read against BRIEFING.md, BRIEFING_R2.md,
Preprint A, Preprint B, G_notes §3.8-3.10 and §6.6, A_notes §1-§7 and A_referee. Date: 2026-10-08.
Setting: canonical base, finite block set I (as in E). Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Verdicts: correct / correct with fixable gaps / wrong / unclear. Working files: `ctx/r1/Eref_work/Eref_part1..7.md`,
scripts in `ctx/r1/Eref_work/scripts/` (numpy only).

---------------------------------------------------------------------------------------------------

## 0. Summary

1. **No claimed result is wrong in its main assertion. E claims no counterexample, and I agree that none is
   established.** Every PROVED item survived a line-by-line re-derivation: N1, Thm 5.1, Cor 5.2 (g_0 = 0), the
   averaging skeleton, rigidity, Lemmas 6.1/6.3/6.4, Cor 6.2 and Prop 8.2. I checked Thm 5.1 numerically in the
   worst case and found no violation.
2. **Priority.** Thm 5.1 is a special case of A_notes Theorem 6.8, which the A-referee had already verified: it fixes
   the radius constant c_0 = 1 and requires H(c_s) <= 1 exactly instead of H <= 1 + eta(t). Cor 5.2 is A_notes
   Cor 6.10(c) with the coefficient condition made explicit. The "box tails" item is A_notes Cor 6.10(a), including
   its radius gap G1. E's part 5 imports only P4.5, L4.2, L4.7 and C4.11 from A, so it apparently missed A §6.4.
   BRIEFING_R2 already makes this observation.
3. **Main gap: T1 (two-piece mates over infinite contact sets).** The sketch never mentions the d-coefficients of the
   block carrier. Transferring the block part to an NA approximant f'' turns omega - d w into omega - d'' w''. The two
   one-sided decompositions must still represent the same g''. So a mismatch Delta d L*(w'' - w) must be carried
   somewhere. The eta-masses scramble the fine coordinates, so this mismatch has size ~ |Delta d| eta, not O(tau').
   * Delta d = 0: the A-referee's §5.4 covers this case.
   * Delta d = d- - d+ >= 0: I give a referee SKETCH (§3.1) that absorbs the mismatch in the block parts at no
     first-order cost.
   * Delta d < 0: OPEN.
   Hence E's refined necessary condition (R-b), "one-sided BASE resources are not enough", is not established.
   Near-flip base resources (j in supp a with |a_j| small) are not treated anywhere either.
4. **T4 (frozen error on near-contacts + side switching) is plausible but not single-scale as written.**
   * The displayed frozen direction lacks a multiple of a. Without it, the frozen direction is a FIXED distance from
     rho g.
   * Turning the head near-contacts of N* into exact contacts shifts the relative position of N* itself, and also
     its d-coefficient, by an amount of order c_gamma eps_0. The mate condition does not make this small.
   * Both switched regimes, (b) and (c), therefore pay a first-order kink cost. For rho near 1 this exceeds the slack
     against an adversarial c_gamma eps_0.
   * Repair: average over J heads at dyadic scales, the same mechanism as Thm 5.1.
5. **Gordan equivalence holds only for finitely many resources.** E applies it to the infinite family of carriers at
   all scales. There Gordan's alternative fails (explicit counterexample in §3.4). The correct statement, which is
   also the one an obstruction needs, is a uniform-margin version via closed convex hulls.
6. **Minor fixes.**
   * The candidate vectors of 1.2 and 3.1 are in c_00, which contradicts Y ∩ c_00 = {0}; Y-tails must be added.
   * NC's "design constraint" contradicts density of the tails of (u_{k,m})_k.
   * The box-tail truncation is worded as an index truncation, which fails (§3.5).
   * In Cor 6.2(b), the room factor is ignored.
   * The conversion-band cost is O(K Lambda_0 log(1/Lambda_0)), not O(K Lambda_0). It is still o(1).
   * The "iff" in E's imported fact (F3) is only "if" (A Remark 3.4).
7. **Status of the goal: density remains OPEN.**
   * E's model-level residual loophole is HEURISTIC and correctly labelled: error-dominated one-sided block carriers
     of core directions, combined with bounded conversion capacity.
   * Item 3 shows that the set of unresolved mechanisms is larger than E's list (R-a)-(R-e): two-piece mates with
     Delta d < 0 must be added.
   * Nothing in E points towards an actual counterexample. Any such counterexample would also have to satisfy the
     Lemma B constraints, and E has not verified that they are consistent with its design conditions.

---------------------------------------------------------------------------------------------------

## 1. Verdict table

| Claim | E's label | Verdict | Key point |
|---|---|---|---|
| N1 necessary conditions | PROVED | correct | All four items follow from Thm 4.17 (shifted transport), Thm L, Prop 7.4 + Fact F(a), G_referee 4.7. The sharp form is "rho g notin cl Cert^sh(f)". (F3)'s "iff" is only "if". |
| Thm 5.1 Averaging Criterion | PROVED | correct | Re-derived; numerically stress-tested. Special case of A Thm 6.8. It needs H(c_s) <= 1 EXACTLY, so truncation-type uses need A's 1 + eta(t) version. |
| Cor 5.2 critical two-sided cross mates | PROVED (g_0 = 0) / SKETCH | correct | H = (c^2 q*(v)^2/m^2 - d_s^2)/C_m <= 1 exactly. Radius >= s. Error O(lambda_i) = O(s); a factor (1+‖U‖) is missing, which is harmless. For g_0 != 0 the hypothesis should read H_m(omega_0) + c^2 q*(v)^2/(m^2 C_m) < 1. = A Cor 6.10(c). |
| A_notes 7.4 box tails | SKETCH | correct with fixable gaps | The index truncation "omega 1_{[1,N(s)]}" fails; one must truncate by the box condition with the coordinatewise radius (A-referee G1). It also needs H <= 1 + o(1) (A Thm 6.8), not Thm 5.1. = A Cor 6.10(a). |
| Averaging skeleton | PROVED | correct | Convexity bound re-derived. The "1 + t^2/2 <= s(t)" step needs a strict margin, which E acknowledges. |
| Rigidity at NA points | PROVED | correct | = A Prop 7.4(b) + Fact F(a) at f'. The block parts of linear decompositions are automatically bounded. Scope: t-LINEAR decompositions only; the title "two-sided resources are indispensable" claims more than is proved. |
| Critical cross candidate | SKETCH | correct with fixable gaps | Destruction mechanism checked. u_{k_i} as written lie in c_00; Y-perturbations of size << min(K lambda_i, Phi(k_i)) are needed. Not a counterexample: it lies in cl Cert(f) by Cor 5.2. |
| T1 two-piece mates | SKETCH | unclear | The d-mismatch Delta d L*(w''-w) ~ |Delta d| eta is not addressed. The argument covers Delta d = 0 (A-referee 5.4) and Delta d >= 0 (referee §3.1). Delta d < 0 is OPEN. |
| Conversion bands | SKETCH | correct | Band (Lambda_0(1+delta)/(2+delta), Lambda_0(1+delta)/delta) re-derived from the block threshold (also checked numerically). The cost estimate carries a log factor. |
| Candidate NC is a mate | SKETCH | correct with fixable gaps | All first- and second-order terms re-checked. Y-tails are needed. The "design constraint" contradicts density of the tails. |
| T4 kills NC | SKETCH | correct with fixable gaps | a-multiple missing in B_0. The N* status/d-shift from the head contacts is of relative order c_gamma eps_0; the switched regimes pay a first-order kink cost. Repair by averaging over heads. |
| Lemma 6.1 / Cor 6.2 | PROVED | correct | Duality via (E_perp)* = l_1/E and c_00-density by finite correction. Cor 6.2(a) needs only the trivial direction (z ∉ c_0 is fine). In (b), the room 1-|z'| limits the shift (factor 2 or 4). |
| Lemma 6.3 | PROVED | correct | Special case of Fact F(b). It should say (k,m) != (k',m'). |
| Lemma 6.4 | PROVED (first part) | correct | Open interval when supp psi_{>W} is infinite. "Plus an endpoint" should read "plus both endpoints". Consequences HEURISTIC, as labelled. |
| Prop 8.2 | PROVED / SKETCH | correct | Trivially true for EVERY fixed y in l_1, and uniformly on norm-compact sets. The "one parameter V" consequence holds when the core errors range in a compact set. |
| Gordan equivalence | PROVED | correct with fixable gaps | Valid for finitely many resources. False for the infinite family; the uniform-margin / closed-hull version is needed. |

---------------------------------------------------------------------------------------------------

## 2. Line-by-line verification

**2.1 N1.**
* (N-a): if f attains its norm at x in S_p, then g(x)^2 <= p(x)^2 - f(x)^2 = 0, so (f,g) attains.
* For f in Omega, Hausdorff continuity holds. A single NA sequence with C(f) ⊂ Li C(f'_n) suffices (A Cor 3.3).
* (N-b): cl Cert^sh(f) ⊂ Li C(f_n) for every sequence (A Thm 4.17), and Li C(f_n) is convex and contains 0. So the
  sharp condition is rho g ∉ cl Cert^sh(f), which is stronger than E's "g ∉".
* (N-c): if b+ - b- ∈ c_00, Fact F(a) gives equal decompositions. Prop 7.4(a) kills the K-part, and Theorem L
  applies.
  * Linear admissibility on (0,r] forces |Omega(k)| <= ~2/r + |mu| off the peaks, so Omega ∈ V* is automatic.
* (N-d): G_referee 4.7.
* Single-pair characterization, which E uses: (f, rho g) ∉ cl NA iff there is delta with dist(rho g, C(f')) >= delta
  for all NA f' with ‖f'-f‖ < delta. This is TRUE. Proof:
  * The adjoint of (f, rho g) peaks only at ±e_1, by strict slack.
  * Hence NA operators near (f, rho g) peak near ±e_1. Replace x_n by -x_n if necessary.
  * Rotations Q_n -> I then give NA first rows f'_n -> f and second rows in C(f'_n) converging to rho g.
* The "iff" of E's (F3), which requires one sequence recovering all g, is not proved in A (Remark 3.4). It is not
  used.

**2.2 Thm 5.1.** I re-derived every inequality:
* Fine/coarse split. Sum_{s_j<|t|} s_j < 2|t|.
* Bound 1 + (rho^2 t^2/2)(1 + kappa_0|t|) + 2 rho K_0 t^2/J. With rho^2/2 = 1/2 - 4e_1 the total is
  1 + t^2(1/2 - 2e_1) <= 1 + t^2/2 - t^4/8, since t^2 <= t_*^2 <= 8e_1.
* Step 2: for |t| >= t_* (t_* <= 1), min(t^2, |t|) >= t_* |t|.
* H(c') <= rho^2 by convexity and 2-homogeneity.
* Numerical check (thm51_check.py): each averaged component saturates its own bound; 300 random (rho, K_0, kappa_0);
  t ∈ [1e-6, 1e4]; E's exact choices of J, t_*, s_J. No violation; worst normalized excess -6e-4.
  * The case split is essential: using the P4.5 bound for coarse components when |t| > t_* produces violations.
    E's Step 2 correctly switches to the transfer bound there.
* Comparison with A Thm 6.8: Thm 5.1 is the special case c_0 = 1, eta ≡ 0. Requiring H(c_s) <= 1 exactly matters.
  * Truncated certificates typically have H(c_s) -> H from above.
  * Rescaling by H^{-1/2} costs o(1)‖g‖, not O(s).
  * So applications should cite A Thm 6.8.

**2.3 Cor 5.2.**
* Choice of index: i(s) = largest index with lambda_i >= thr := 2 c q*(v) s/gamma. It exists for small s, since
  lambda_i -> 0 makes this index set finite and nonempty. Then lambda_i <= lambda_{i+1}/theta_0 < thr/theta_0, since
  lambda_{i+1} < thr by maximality. No monotonicity of lambda_i is needed.
* Carried vector: R_m* omega_s = c q*(v) u_{k_i}.
* d-coefficient: d_s = Phi(k_i) w(k_i) c q*(v)/(m C_m).
* Coefficient: ‖D omega_s‖^2 = c^2 q*(v)^2/m^2, so H = (c^2 q*(v)^2/m^2 - d_s^2)/C_m <= 1, with no o(1).
* Radius: gap/(2|omega|) >= gamma lambda_i/(2c q*(v)) >= s. The other two radius terms, and kappa, tend to their
  limits since d_s -> 0.
* Error: q*(c q*(v)(u - vhat)) <= (1+‖U‖) c q*(v) K lambda_i. E wrote this without the factor (1+‖U‖).
* Numerical check (block_check.py): the single-coordinate expansion N(W(s)) - 1 <= (s^2/2) H(1 + kappa|s|) holds
  on |s| <= r, with ratio -> 1.
* g_0 != 0. The cross term is <P_perp D omega_0, P_perp D omega_s> = -d_0 d_s -> 0. Hence
  H_m(omega_0 + omega_s) -> H_m(omega_0) + c^2 q*(v)^2/(m^2 C_m), and this limit is the hypothesis needed. E's
  "H(c_0 + single-coordinate part) <= 1" is ambiguous, since that part depends on s.
* Scope: gaps >= gamma and scale density are essential. D_notes 12.2's near-peak or scale-sparse carriers are not
  covered.

**2.4 Averaging skeleton (E 2.1).** Correct as stated:
* convexity of p*;
* (i) for coarse components;
* (ii)+(iii) for fine components, which are only those with |t| > s_j >= s_1.
The hypotheses (H-transfer) and (H-cert) are, as E says, the real content.

**2.5 Rigidity (E 2.2).**
* At an NA point, supp a' ∪ K' is finite. B+ - B- = L*(Om- - Om+) lies in c_00 ∩ Y = {0}, and L* is injective.
  Correct.
* Derived here: a one-sided linear decomposition has Om = omega - d w with
  * d = <Dw, D omega>/C;
  * omega = 0 on supp alpha;
  * sigma_k omega(k) <= 0 on P \ supp alpha.
  So "peaks used one-sidedly" in a LINEAR decomposition are exactly the alpha-null peaks.
* What is NOT proved: that the frozen h_j of the skeleton need two-sided resources. Condition (i) is a two-sided
  BOUND and does not require a linear decomposition.
  * Nothing excludes scale-dependent mechanisms at NA points that use far weak peaks; peak sets are typically
    cofinite. A Cor 7.5 only says that a defect mate at an NA point has no linear decomposition on one side.
  * E's own T4 uses side switching at f'.

**2.6 Critical cross candidate (E 1.2).**
* v(xhat) = 0 because a(xhat) = 1. At f, w(k_i) = 0.
* Mate property for small c: the base first-order cost is |t| c K lambda_i (1 ∓ 1/2) = O(t^2), because z = 1/2 on
  B_i.
* Destruction: sigma_i(x') -> -c_∞ xhat_{j_0} = -1/2 for z' ∈ c_0. With K large these k_i become peaks.
* Gaps:
  * a, e_j*, sigma_i ∈ c_00, so u_{k_i} ∈ c_00 ∩ Y = {0}. Y-perturbations are required, small relative to both
    K lambda_i and Phi(k_i), and with free tail mass below the conversion threshold of Cor 6.2.
  * With a' != a, the shift V re-converts a band near lambda ~ 2|V|/K. The off-peak set at f' is then finite but not
    an initial segment.
* The candidate lies in cl Cert(f) (Cor 5.2) and is transported along every sequence. Each averaged certificate uses
  finitely many coarse k_i, and these are off-peak at f'_n for n large, since w'_n(k_i) -> 0. E agrees in part 5.

**2.7 Conversion bands (E 2.4).**
* Block threshold: m|u_k(x')| >= Phi M'|zeta'|/C' iff |rho_k| >= theta~ := M'|zeta'| n_k/(C' m^2 K).
* With sigma_k(x') = sigma_k(xhat) + o(1) and V = -K Lambda_0 theta~(1+delta), the band and its ratio (2+delta)/delta
  follow; I re-derived them.
* Numerical check (block_check.py): computed J(zeta) directly. The peak set equals the threshold rule, and the
  off-peak values follow C zeta/(Phi^2|zeta|).
* Cost: a move of size s changes off-peak values with Phi(k) >= s by ~ s/Phi(k), so ‖L*(w'-w)‖ = O(s log(1/s)), not
  O(s). Still o(1).

**2.8 NC (E 3.1).**
* Re-checked:
  * u(xhat) = 0;
  * on its own side each carrier has first-order cost t c sum|Z_l| gamma_l <= t c eps_0 c_gamma lambda;
  * d = 0, since w(k) = 0;
  * the base Hilbert part is small, since U* is w*-to-norm continuous on bounded sets, ‖U* e_l*‖ -> 0, and the
    a-multiple is killed by P_perp.
* Two defects in the specification:
  * As written, the carriers are in c_00 unless the "negligible Y-tails" are added.
  * The "design constraint" quoted below contradicts density of every tail of (u_{k,m})_k in S_{q*}:
    > "every coordinate with j-mass carries errors of size >= eps_0 * (j-mass) on near-contacts"
    The consistent form is that good approximants of v0 occur only at scales lambda_k <= psi(error), with psi
    decaying fast.
* Neither defect affects the mate property.

**2.9 T4 (E 3.2).** Regimes (a), (b), (c) are re-derived in §3.2 below, together with the gaps.

**2.10 Lemma 6.1, Cor 6.2.**
* Lemma 6.1, "<=": trivial.
* Lemma 6.1, ">=": (E_perp)* = l_1/(E_perp)^perp, and (E_perp)^perp = E because E is finite-dimensional, hence
  w*-closed (bipolar).
* Lemma 6.1, density of c_00 ∩ B_{E_perp}:
  * Truncate.
  * Correct on a finite injectivity set S ⊂ (W, ∞), using that the dual map R^S -> E* is onto.
  * Rescale by 1/(1 + ‖zeta_N‖).
  * Dominated convergence gives y(eta_N) -> y(eta).
* Cor 6.2(a) uses (z'-z)1_{>W} ∈ l_∞, which has norm <= 2 and annihilates E. No c_0 is needed.
* Cor 6.2(b): Lemma 6.1 gives eta with ‖eta‖ < 1 and exact shift s, but z' + eta must stay in B_{c_0}.
  * The achievable shift is limited by the room 1 - |z'_l| on supp eta.
  * It is one-sided where the tail of u_k lies on near-contacts of f.
  * E's own parenthetical (eta/2) gives shift s/2.
  * Harmless.

**2.11 Lemmas 6.3, 6.4.**
* Lemma 6.3: u_{k,m} - c u_{k',m'} ∈ Y ∩ c_00 = {0}, contradicting injectivity of T; c = 0 is included. Correct.
* Lemma 6.4: the image of B_{c_0(W,∞)} under psi_{>W} is an interval containing ±S_N for every N.
  * Equality |psi(z')| = ‖psi‖_1 forces |z'_l| = 1 on supp psi, which is impossible in c_0 when the support is
    infinite.
  * Correct.

**2.12 Prop 8.2.**
* (F1) gives y'_n = z'_n + U e'_n -> xhat weak*. Hence y(y'_n - xhat) -> 0 for every fixed y ∈ l_1 by dominated
  convergence, uniformly on norm-compact subsets of l_1. Correct.
* The consequence "only V acts at window level" holds exactly when the normalized core errors sigma_k range in a
  norm-compact set, for example bounded in a fixed finite window. That is E's model.

---------------------------------------------------------------------------------------------------

## 3. Problems found

### 3.1 T1 does not handle the d-coefficients (main gap); partial repair

**Quote (E 1.4(i)).**
> "base two-sided for |t| <= eta, one-sided linear decompositions transferred for |t| in [tau'/c, T_0] with
> tau' = ||y|_{>N'}||_1 << eta."

**What is missing: the block part.**
* A one-sided linear decomposition has block part Om± = omega± - d± w, with d± = <Dw, D omega±>/C (derived in 2.5).
* At an NA approximant f'', the block first-order term of w'' + t(omega - delta w'') is t(d''(omega) - delta).
* By the budget identity (A Lemma 7.1 at f''), any delta != d'' produces first-order excess for every t != 0:
  * the block part gives 1 + t(d'' - delta);
  * the base part is >= 1 - t(d'' - delta)(1-q_0'')/q_0''.
* So the transferred block part must be omega± - d±'' w''.

**What is missing: the mismatch.**
* Both decompositions must represent the same g''. Even after enforcing d+'' - d-'' = d+ - d- by one scalar
  condition, the base must therefore absorb Delta d L*(w'' - w), where Delta d = d- - d+.

**Why the mismatch is not small.**
* The eta-masses sit on ALL contacts in K ∩ [1,N'], including the finitely many near ones where ‖U* e_j*‖ is not
  small. They move e = U*a/‖U*a‖ by ~ eta, hence u_k(x'') by ~ eta for generic k.
* This scrambles the coordinates with Phi(k) <~ eta, contributing mass ~ eta.
* It also moves off-peak coordinates with Phi(k) >= eta by ~ eta/Phi(k).
* The first-order cost |t| |Delta d| c eta beats the slack (1-rho^2) t^2/6 on |t| ∈ [eta, 6|Delta d| c eta/(1-rho^2)].
  On this band neither regime works.

**Attempts that do not close the gap for Delta d < 0.**
* Keeping the old w in the d-term: flipped and new peaks of w'' give first-order sup-norm excess 2|t d| M on one
  side.
* A coarse/fine hybrid: the fine mismatch ~ |Delta d| eta remains.
* Rescaling via L*w'' = f'' - a'': this only moves the excess between components (budget identity).

**Referee SKETCH: repair for Delta d >= 0.**
* Assumptions, as in A-referee 5.4: omega± are finitely supported and off-peak, and one scalar condition per block
  enforces (d+'' - d-'') = (d+ - d-).
* Use Om''± := omega± - d±'' w'' + c± (w'' - w) with c+ <= 0 <= c- and c- - c+ = Delta d. The side made two-sided
  by the eta-masses takes c = 0.
* The window base parts are then EXACTLY the transported b±. Only far tails, which cost ~ |t| tau', remain.
* The first-order block term is t c (C C'' - <Dw, Dw''>)/C'' <= 0 by Cauchy-Schwarz:
  * peaks and near-peaks of w'' contribute -d''M'' + c(M'' - M);
  * the D-part contributes d''M'' + c(C'' - <Dw,Dw''>/C'').
* Off supp omega there is the exact bound |W(k)| <= (1 - t d'' - |tc|)|w''(k)| + |tc||w(k)|, so there is no hidden
  second-order excess.

**Delta d < 0: OPEN.**
* The sign constraint fails: one would need t c > 0, i.e. extrapolation away from w.
* Such mates are as plausible as the Delta d > 0 ones: they satisfy the same fixed-point sign condition as A-referee
  5.2, with omega of opposite sign.

**Consequences.**
* E's (R-b), "one-sided BASE resources are not enough", is not established.
* Near-flip base resources (A §7.2 (N1)) are not treated anywhere either.
* The list of open defect mechanisms must include two-piece mates with Delta d < 0.

### 3.2 T4: missing a-multiple and the head-contact shift of N*

**(a) Missing a-multiple.**
* Quote: "B_0 := -rho c Z_{N*}^{head} (so g' = rho c v0 + rho c Z_{N*}^{tail}, close to rho g)".
* Since n u_{N*} = v0 + Z_{N*} - Z_{N*}(xhat) a, this B_0 gives g' - rho g = rho c Z^tail - rho c Z_{N*}(xhat) a.
  The second term has FIXED size ~ rho c eps_0.
* Fix: B_0 := -rho c (Z^head - Z^head(xhat) a). This falls under E's unwritten "g'(x') = 0 normalization".

**(b) The head-contact shift of N*.**
* Quote: "make the head of supp Z_{N*} EXACT contacts (z'_l = s_l; cost ~ gamma_l * influence(l), tiny)".
* The cost in ‖f''-f‖ is tiny. But n u_{N*}(x'') moves by sum_head |Z_l| gamma_l > 0, with all terms of one sign.
  This is up to c_gamma lambda_{N*} eps_0.
* Relative to the peak threshold, this is r = c_gamma eps_0 C m^2/(n M |zeta|).
* The mate condition only forces c_gamma eps_0 <~ M/(4 c^2 n), from the base cost 2c^2 eps_0 c_gamma n t^2/M <= t^2/2.
  So r > 1 is possible for small c, in which case N* becomes a (+) peak.
* Even for r < 1, d''_{N*} = rho c n u_{N*}(x'')/|zeta''| differs from the d'' of the matched carriers. A common
  window shift does not change this difference.
* Keep the carrier's own block part w'' + t(omega_k - d''_k w''), which has zero first-order block term. Then the
  base direction contains eps L*w'', with eps = d''_k - d''_{N*} = -rho c sum|Z_l|gamma_l/|zeta''|. Its value at
  xhat'' is compensated exactly by the carrier difference. What remains is its KINK cost:
  |t| |eps| kappa_q''(±L*w''), with kappa_q''(v) = sum_{l notin supp a''}(|v_l| - z''_l v_l) > 0 at an NA point.
* Moving the mismatch into the block (using d''_{N*} instead of d''_k), or rescaling via f'' = a'' + L*w'', only
  redistributes a first-order excess of the same order between the components. So regimes (b) and (c) both pay
  ~ |t| rho c c_gamma lambda_{N*} eps_0 kappa''/|zeta|. (An earlier draft of this report wrongly said that one side
  is free.)
* Requirement versus allowance:
  * single-scale T4 needs c_gamma eps_0 <= (1-rho^2) M |zeta|/(12 rho^2 c^2 n kappa''), evaluated at
    |t| >= t_a = M lambda_{N*}/(2 rho c n);
  * the mate condition allows a constant factor ~ 3 kappa''/((1-rho^2)|zeta|) more.
  * So the requirement fails for rho near 1.
* Repair (plausible): average J frozen representations with heads at J dyadic scales, as in Thm 5.1. Each mismatch
  is proportional to its own lambda_{N*_j}, so the boundary cost is divided by J. In each (b)/(c)-regime, use
  carriers other than the heads.
* The e''-shift caused by the masses is harmless here, because the masses sit on FAR near-contacts, where
  ‖U* e_l*‖ -> 0. This is unlike T1.

### 3.3 Rigidity title and scope
* E 2.2 title: "Why two-sided resources are indispensable at NA points (PROVED...)".
* What is proved: only two one-sided LINEAR decompositions coincide. See 2.5.

### 3.4 Gordan for infinite families

**Quote (E 7.3).**
> "By Gordan's alternative this holds iff there is a functional Lambda on E_c with tau_k Lambda(sigma_k) > 0 for all
> k".

**The setting.**
* On side t > 0 the achievable carried core errors form cone{tau_k sigma_k}: P- used upward has tau = +1, P+ used
  downward has tau = -1.
* On side t < 0 they form the negative cone.
* For FINITELY many k, Gordan gives exactly the stated equivalence.

**Counterexample for infinitely many resources.**
* In R^2 take a_k = (1, 1/k) for k >= 1, and a_0 = (-1, 0).
* No nontrivial finite nonnegative combination vanishes: the second coordinate forces all y_k = 0, and then y_0 = 0.
* No Lambda is positive on all a_k: positivity at a_0 forces lambda_1 < 0, and then lambda_1 + lambda_2/k < 0 for
  large k.

**Correct statement.**
* There is Lambda with inf_k Lambda(tau_k sigma_k)/|sigma_k| > 0 iff 0 ∉ cl conv{tau_k sigma_k/|sigma_k|}
  (separation in finite dimensions).
* This is also what a quantitative obstruction needs, since approximate cancellations serve the approximant as well
  as exact ones.
* For "useful" combinations (nonzero v-component), the exact condition is a Farkas/Motzkin condition on the vectors
  (tau_k sigma_k, tau_k/n_k).

### 3.5 Box tails: wrong truncation as worded

**Quote (E §5, Consequences).**
> "truncations omega 1_{[1,N(s)]} at the level where the box holds at scale s ... error T(s) = O(s)".

**Failure scenario for index truncation.**
* Take near-peak coordinates k_i with gap(k_i) = 2 s_i |omega(k_i)|, where s_i -> 0 very fast.
* For s ∈ (s_{i+1}, s_i], the violating set is E(s) = {k_j : j > i}.
* Cutting at min E(s) - 1 discards the whole tail beyond k_{i+1}, a FIXED mass, for s all the way down to s_{i+1}.
* So error/s is unbounded.

**Correct version (A Cor 6.10(a)).**
* Truncate as omega 1_{k <= J_s, |s omega(k)| <= gap(k)/2}.
* Use the coordinatewise radius (A-referee G1).
* Apply A Thm 6.8 (H <= 1 + o(1)).

### 3.6 Minor
* 1.2 / 3.1: the u's as written lie in c_00 (see 2.6, 2.8).
* NC design constraint versus density of the tails of (u_{k,m})_k (see 2.8).
* Cor 6.2(b) room factor (see 2.10).
* Conversion cost: log factor (see 2.7).
* Cor 5.2: factor (1+‖U‖) and the precise g_0 != 0 hypothesis (see 2.3).
* Lemma 6.4 endpoints; Lemma 6.3 indexing (k,m).
* (F3) "iff".
* Skeleton: "1 + t^2/2 <= s(t)" needs a strict margin.

---------------------------------------------------------------------------------------------------

## 4. Assessment of the counterexample search and of the residual loophole

**Status of the claims.**
* The PROVED parts of E are correct.
* They do not bear on the existence of a counterexample, except as necessary conditions.

**The model-level loophole (parts 4 and 7).**
* The loophole is: error-dominated one-sided block carriers of a core direction, with conversion capacity bounded by
  far-rigid detector groups.
* It is honestly labelled HEURISTIC.
* The Model N numbers are NUMERICAL; I did not re-run them.

**My view of the loophole.**
* (A1)-(A5) are not shown to be consistent with Lemma B. In particular, density of every tail must coexist with far
  rigidity and with the absence of critical-rate two-sided approximants of E_c directions.
* Even granting the model, a non-recovery proof would need a LOWER bound over all mates at all NA approximants.
  Model N only optimizes over frozen + transfer representations.
* Because of 3.1, the loophole list is incomplete: two-piece mates with Delta d < 0 are an independent unresolved
  mechanism, and it involves no block resonance at all.
* E's overall leaning ("positive for Martin's own T; may depend on T") is reasonable but unsupported by proof.

**Status of the goal.** Density of NA((c_0,p), l_2^2) is OPEN.

## 5. Single most valuable idea

The **destruction-conversion duality** (Lemma 6.1 / Cor 6.2), combined with Prop 8.2 and the averaging mechanism
(Thm 5.1 / skeleton).
* Along NA approximants, window moves are o(1). The only levers on fine block resources are:
  * the absolute shift V;
  * the far tails.
* The free tail mass tau_k = dist_{l_1}(u_k|_{>W}, span{guard tails}) does two things at once:
  * it bounds by 2 tau_k how much a resource can be destroyed while the guards are kept;
  * it measures how far the resource can be shifted (converted) without disturbing the guards.
* Averaging converts any unbounded supply of two-sided scales near the matching boundary into recovery.
* Together these reduce the one-sided-block part of the density problem to a single checkable property of
  Martín's T: QUANTITATIVE tail independence (conversion capacity -> ∞ near every boundary).
* The same property also controls the open Delta d < 0 case of T1, through matching all coordinates down to a small
  multiple of the perturbation scale.
* Recommended next step: compute or bound these condition numbers for Martín's T, or construct an explicit
  admissible T violating them.

## 6. Numerical checks (scripts in ctx/r1/Eref_work/scripts/)
* `block_check.py`: direct computation of J(zeta) for a 14-coordinate block.
  * The peak set coincides with the threshold rule |zeta(k)| >= Phi^2 M |zeta|/C.
  * Off-peak values match C zeta/(Phi^2|zeta|) to 2e-5.
  * Cor 5.2's single-coordinate certificate satisfies N(W(s)) - 1 <= (s^2/2) H (1 + kappa|s|) for |s| <= r, with
    ratio -> 1.
* `thm51_check.py`: worst-case bookkeeping of Thm 5.1, as in 2.2. No violation in 300 random parameter sets.
