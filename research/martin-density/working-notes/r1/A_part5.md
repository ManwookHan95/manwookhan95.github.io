---------------------------------------------------------------------------------------------------

## 8. Engineering NA approximants with free far coordinates

Throughout, x' = z' + U e' with a' in c_00 cap S_{q*}, e' = U*a'/||U*a'||, z' in B_{c_0}, z' = sign a' on supp a' (Fact D), f' := grad p(x').

**Lemma 8.1 (far modifications are norm-small). PROVED.** For N in N let Y_N := { y in c_0 : supp y in [N, infinity) \ supp a', ||z' + y||_infinity <= 1 }.
For y in Y_N, f'_y := grad p(x' + y) = a' + L* J_V(L(x' + y)) is norm attaining with the SAME base component a', and
sup_{y in Y_N} p*(f'_y - f') -> 0 as N -> infinity.
*Proof.* x' + y = (z' + y) + U e' with z' + y in B_{c_0} equal to sign a' on supp a', so grad q(x' + y) = a' (Fact D). Since ||y||_infinity <= 2,
||L y||_V <= sum_{m,k} lambda_{k,m} |u_{k,m}(y)| <= 2 theta_N, theta_N := sum_{m,k} lambda_{k,m} ||u_{k,m} 1_{[N,infinity)}||_1 -> 0 (dominated convergence,
sum lambda_{k,m} <= sum_m m 2^{-m}). The map v -> L*J_V(v) is norm-to-norm continuous at v = L x' (J_V is norm-to-weak* continuous at
vectors with all block components nonzero; L* is weak*-to-norm continuous on bounded sets), hence uniformly small on the balls
{ ||v - Lx'|| <= 2 theta_N }. QED.

**Lemma 8.2 (zeroing a far block coordinate). PROVED.** For every block m, every N and every delta > 0 there are j, k >= N and y = y_j e_j in Y_N
with |y_j| <= delta such that u_{k,m}(x' + y) = 0. For f'_y the coordinate k of block m is then off-peak with w''_m(k) = 0 (maximal gap).
*Proof.* Choose j >= N outside supp a' with |z'_j| <= 1/2 and |x'_j| small (x' in c_0). By (T2) choose k >= N with
||u_{k,m} - e_j*/q*(e_j*)|| <= delta_0, delta_0 small; then u_{k,m}(e_j) >= 1/(2(1 + ||U||)) and |u_{k,m}(x')| <= |x'_j| + delta_0 ||x'||_infinity.
Put y_j := -u_{k,m}(x')/u_{k,m}(e_j). Then (R_m(x' + y))(k) = 0, and by Fact C (at the NA point) k is not a peak and w''_m(k) = 0. QED.
Remark: the index k is chosen by us (u_{k,m} close to a far base vector). A prescribed k cannot in general be zeroed by far
modifications: |u_{k,m}(y)| <= 2 ||u_{k,m} 1_{[N,infinity)}||_1 for y in Y_N, which is smaller than |u_{k,m}(x')| unless u_{k,m}(x') is already tiny.

**Lemma 8.3 (new contacts and new small base support). PROVED.** (a) Setting z'_j := +-1 at finitely many far j (y in Y_N) creates new
one-sided contacts at norm cost -> 0 (Lemma 8.1). (b) For j outside supp a' with |z'_j| = 1 and eta > 0, a'' := (a' + eta z'_j e_j*)/q*(a' + eta z'_j e_j*)
is compatible with z' (sign a''_j = z'_j), and grad p(z' + U e'') -> f' as eta -> 0 (e'' -> e', continuity as in Lemma 8.1).

**Proposition 8.4 (limits of certificate engineering). PROVED.** Let f, f' in S_{p*} with forced data (a, w), (a', w'), and let c' = (b', omega')
be a finite certificate at f' with radius r' := r(c'). Then
 (a) sum_{j in supp a' : |a'_j| <= 2|a'_j - a_j|} |b'_j| <= 2 ||a' - a||_1 / r'; in particular the base mass of c' on new coordinates (j not in supp a)
     is at most ||a' - a||_1 / r';
 (b) for each block m: sum_{k in supp omega'_m : gap_m(k) < gap'_m(k)/2} lambda_{k,m} |omega'_m(k)|
       <= ( sum_k lambda_{k,m} |w'_m(k) - w_m(k)| + |M'_m - M_m| sum_k lambda_{k,m} ) / r'.
     (This includes peaks of w_m that became off-peak at f'.)
*Proof.* (a) |b'_j| <= |a'_j| ||b'/a'||_infinity <= |a'_j|/r'. (b) For k in supp omega'_m, |omega'_m(k)| <= gap'_m(k)/(2r'); if gap_m(k) < gap'_m(k)/2 then
gap'_m(k) < 2(gap'_m(k) - gap_m(k)) <= 2(|M'_m - M_m| + |w'_m(k) - w_m(k)|). QED.
*Interpretation (HEURISTIC).* Under the NA-scale criterion (eps = p*(f' - f) <= (1 - rho^2) r_*^2/6, r_* <= r'), if ||a' - a||_1 and the weighted
distances sum_k lambda_k |w'_m(k) - w_m(k)| are O(eps), then the newly created structure carries only O(eps/r') = O(sqrt(eps)) of the
recovered direction. Macroscopic new structure needs ||a' - a||_1 or sum lambda |w' - w| much larger than eps = p*(f' - f), i.e. cancellations
between a' - a and L*(w' - w) or inside L*(w' - w): a T-dependent phenomenon (near-linear dependences among the lambda_{k,m} u_{k,m},
or near-membership of Y-vectors in c_00).

**Lemma 8.5 (domination). PROVED.** If f, h in B_{p*}, lambda in (0,1) and f' := lambda f + (1 - lambda) h has p*(f') = 1, then
r_{f'} >= lambda r_f on X, hence C(f') contains lambda C(f).
*Proof.* By evenness it suffices to take y with f(y) >= 0. Then p - f' >= p - lambda f - (1 - lambda) p = lambda (p - f) and
p + f' >= p + lambda f - (1 - lambda) p = lambda (p + f), so p^2 - f'^2 >= lambda^2 (p^2 - f^2). QED.

**Lemma 8.6 (rotundity of p*). PROVED (given T1, T3, T4).** For xi in S_{p**} normed by some f in S_{p*}, the face
{h in B_{p*} : h(xi) = 1} equals {f}. Hence p* is rotund, and Lemma 8.5 applies only with h = f: it cannot produce approximants.
*Proof.* If h = A + L*W with q*(A) <= 1, ||W|| <= 1 and h(xi) = 1, then A(xi) = q_0 and <W, L**xi> = 1 - q_0, so W = J_V(L**xi) = w (smoothness)
and A(zhat) = 1 = ||A||_1 + ||U*A||; this forces U*A = ||U*A|| e = (||U*A||/nu) U*a, so A = (||U*A||/nu) a by injectivity of U*, and A(zhat) = 1 gives A = a. QED.
*Approximate version (computation, PROVED; usefulness FALSE).* If f' = lambda f + (1 - lambda) h with p*(h) = 1 + kappa, then for f(y) >= 0
p^2 - f'^2 >= [lambda(p - f) - (1-lambda) kappa p]_+ [lambda(p + f) - (1-lambda) kappa p], which degenerates exactly on the near-normer cone
{ f > (1 - (1-lambda) kappa/lambda) p } of f: the multi-scale region again.

### 8.7 A three-regime scheme for mates outside cl Cert(f) (SKETCH; not completed)
Let g be in the defect, rho < 1, and f' = grad p(x') an NA approximant with z' = z on [1, N] plus finitely many engineered far
modifications; eps := p*(f' - f). Recovery of rho g requires ONE vector g' close to rho g with p*(f' + t g') <= s(t) for all t, certified in
three regimes:
 (i) |t| >= T_0 := sqrt(6 eps/(1 - rho^2)) (and >= 6 ||g' - rho g||/(1 - rho^2)): slack (Lemma 4.7);
 (ii) t_1 <= |t| <= T_0: transfer of the admissible decompositions of f + rho t g (scale rho t) to f'. Requirements: the base resources used
      at these scales (contacts, near-contacts, flips) lie in [1, N] where z' = z, up to cost o(t^2); the block coordinates used with
      non-negligible box/peak usage lie in a finite window where |w'_m(k) - w_m(k)| and the first-order Hilbert mismatch
      |t| <D_m Omega, D_m(w'_m/C'_m - w_m/C_m)> are <= (1 - rho^2) t^2/10; and g'(x') = 0 corrections are absorbed;
 (iii) |t| <= t_1: g' = g_{c'} for a (shifted) certificate c' at f' with radius >= t_1.
For a mate of type (N1) (one-sided contact j in K used on the side t > 0, compensated on t < 0 by a scale-dependent one-sided
mechanism, so that Theorem 6.8 does not apply on either side; if the t < 0 side were "certificate + O(t)", the mate would already be
in cl Cert(f) by Corollary 6.9), the natural engineering is Lemma 8.3(b): give a' a tiny mass eta at the contact j with sign z_j. Then on t > 0 the linear decomposition stays admissible at
f' at ALL scales (|a'_j + t b_j| = |a'_j| + |t b_j|), and on t < 0 the contact is two-sided smooth for |t| <= t_1 ~ eta/|b_j|, so regime (iii)
is available with radius ~ eta; regime (ii) must transfer the cross mechanism of f on [t_1, T_0]. The difficulty: the tiny mass eta moves
e' by O(eta), hence u_{k,m}(x') by O(eta), hence the off-peak values w'_m(k) = C' m u_{k,m}(x')/(Phi_m(k)|R_m x'|) by O(eta/Phi_m(k)), which is O(1)
on the coordinates with Phi_m(k) ~ t_1 ~ eta that the t < 0 mechanism uses at the bottom of regime (ii). One must therefore re-tune
u_{k,m}(x') on the relevant window by far modifications (finitely many linear conditions, solvable by tail independence, Fact F(b)),
with precision o(t_1^2), while keeping Lemma 8.1 smallness. I could not control these precisions uniformly; this is the precise point
where strategy (A) stalls. Status: SKETCH (requirements identified), not a proof.

---------------------------------------------------------------------------------------------------

## 9. Failed attempts (with the reason they fail)

(a) **Direct transfer of decompositions** (A'_t := a' + rho t B_{rho t}, W'_t := w' + rho t Omega_{rho t}, g' := rho g). FALSE as a general method.
    Reasons: (1) w' - w is only weak*-small: ||w' - w||_{V*} need not be small; far peaks of w' may have the opposite sign to those of
    w, so |w'(k) + rho t Omega(k)| can exceed the peak level by O(1) at far coordinates where Omega_{rho t} is large. (2) Even with matching
    structure, N_m(w' + tau Omega) - N_m(w + tau Omega) contains the first-order term tau <D Omega, D(w'/C' - w/C)>, of size |tau| ||D(w' - w)||, which
    is >> tau^2 for |tau| << ||D(w' - w)||. (3) rho g does not vanish at x' (|g(x')| <~ sqrt(2 eps)); the correction g' = rho(g - g(x') f')
    introduces first-order terms of size |tau| sqrt(eps) in each component. Base parts transfer exactly only when a' = a.
(b) **Pointwise domination** r_{f'} >= rho r_f with f' NA and f not NA: FALSE (r_{f'}(x') = 0 < r_f(x')); approximate domination with
    additive errors delta p(y) is useless because the infimum defining r~ involves decompositions with unbounded sum_j p(y_j)
    (pieces +-K x' + v near the normer ray). Convex combinations: Lemmas 8.5-8.6.
(c) **Freezing an optimal decomposition at one scale t** and truncating it to a certificate: radius ~ t, error = non-certificate part at
    scale t, which is typically Theta(t) (e.g. base mass off supp a at non-contact coordinates may use the whole budget:
    ||B_t 1_{F^c}||_1 <= t/(2 q_0 (1 - theta))). The (CA) test needs error <= (1 - rho^2) t/6, which fails as rho -> 1. Rescued only by
    monotonicity (base flips: Lemma 6.4) or by o(t) tails (Theorem 6.2). SUPERSEDED: averaging the frozen certificates over n
    geometric scales (Theorem 6.8) divides the effective error by n, so O(t) remainders suffice; single-scale freezing is the
    wrong construction, not a real obstruction.
(d) **Engineering new structure through finite certificates only** (NA-scale criterion): limited by Proposition 8.4.
(e) **Local second-order analysis alone.** (1) The certificate coefficient H(c) can exceed the true local coefficient (shifts, §4.5).
    (2) The local certificate set {g_c : H(c) <= 1} without the global condition is unbounded in general: its support function at x
    is sup{ <D omega, y> : omega in c_00(S), ||P-perp D omega||^2 <= C } with y_k = m u_{k,m}(x) - (<w, R_m x>/C) Phi_m(k) w(k) on the off-peak set S,
    which is +infinity whenever (u_{k,m}(x))_{k in S} is not square summable (PROVED, elementary). So global contractivity is essential and
    membership in C(f) cannot be decided by second-order data at f alone.
(f) **Subsequential limits of optimal decompositions** (setting: a in c_00, theta := sup_{j not in supp a}|z_j| < 1, finite I). SKETCH of what one gets:
    B_t 1_{F^c} -> 0, B_t 1_F is bounded (using injectivity of U* on R^F and the Hilbert part of the budget), so along subsequences
    B_t -> B_0 in c_00(F). If moreover ||Omega_t||_{V*} stays bounded on both sides, then Omega_t -> Omega_0 weak*, g = B_0 + L* Omega_0, and by
    Fact F(a) the limit does not depend on the side or subsequence; Omega_0 is balanced on every peak set (from Corollary 7.3(b) on
    supp alpha and the one-sided constraints on P \ supp alpha), so Omega_0 = omega_0 - d_0 w with omega_0 off-peak and the consistent d_0. The first-order
    masses t B_t(zhat) and t <Omega_{t,m}, zeta_m> are O(t^2) but need not be o(t^2): their normalized limits are a shift (§4.5), so the limit
    object is a "generalized shifted certificate" (with a base shift vector lim (-t B_t 1_{F^c})/t^2 that need not be a combination of the
    R_m* w_m). Missing for a proof that g lies in cl Cert^sh(f): (i) near-peak decay of omega_0 (o(sigma) box tails) does not pass to the
    limit, because at scale t the box constraints involve Omega_t, not Omega_0; (ii) transport of general shifts with infinitely supported
    shift vectors; (iii) the bounded case itself is an assumption (weighted directions show Omega_t can be unbounded).
    If in addition the off-peak gaps are bounded below (inf_{k notin P_m} gap_m(k) > 0) then (i) disappears (box tails vanish for small sigma).
    By Theorem 6.8 the whole question reduces to showing that the non-certificate parts of (B_t, Omega_t) are O(t) on one side.

---------------------------------------------------------------------------------------------------

## 10. Conclusions, open problems, next steps

**What is now established (finite block set I; everything also holds for I = N given (T4) for p).**
1. (R3) and its finite/mate versions and transitivity are correct (§3).
2. All mates in cl Cert^sh(f) (finite certificates, shifted certificates, weighted certificates of Theorem 6.2, linear decompositions of
   Theorem 6.5, and closed convex hulls) are recovered along EVERY sequence f_n -> f in S_{p*}; the map f -> cl Cert^sh(f) is lower
   semicontinuous. In particular all (R6) classes are recovered simultaneously along one (indeed any) common sequence, and the
   [Check] local-certificate theorem is re-proved with a weaker coefficient condition (§4.5).
2'. Averaging theorem (Theorem 6.8, Corollary 6.9): a mate is in cl Cert(f) as soon as, on one side and at all small scales t, it
   is a finite certificate of radius >~ t up to an O(t) remainder. This covers weighted directions with box tails of exact order
   t (§7.4 resolved), and cross mates with scale-dense approximation rates (Corollary 6.10(c)).
3. Density of NA((c_0,p), l_2^2) (and into l_2^d) follows if, for every f, the defect Def(f) = C(f) \ cl Cert^sh(f) is recovered along some
   NA sequence; in particular if Def(f) is empty for every f, in which case C is even Hausdorff continuous everywhere.
4. Every defect mate needs genuinely scale-dependent decompositions; at points with finite contact set (all NA points) piecewise-linear
   decompositions with bounded block parts are excluded (Proposition 7.4).

**Open problems (precise).**
 (P1) Is Def(f) empty for every f? By §6.4 and §7.2 a defect mate must, on BOTH sides and at arbitrarily small scales, carry a part
      of size >> t through one-sided resources (contacts/near-contacts/near-flip coordinates of the base, weak peaks of the blocks),
      switching between different carriers. Sub-questions: (a) prove a quantitative "independence at scale" statement forcing the
      carriers on the two sides to match up to O(t) (this would prove Conjecture 7.5 under scale separation); (b) decide whether
      Martín's T is scale separated (rates of approximation of base vectors and of block vectors by block vectors at their own scale);
      (c) two-piece mates over infinite contact sets K (Remark 7.6): does Y cap l_1(supp a cup K) contain vectors with the required signs?
 (P2) Make the three-regime engineering of §8.7 rigorous for one-sided-contact mates (the transfer regime with re-tuning of u_{k,m}(x')).
 (P3) Transport of general shifts tau^2 V (Remark 4.19) with infinitely supported V; then redo §9(f) to get "bounded decompositions with
      uniform off-peak gaps => g in cl Cert^{sh,gen}(f)".
 (P4) Get Martín's construction (arXiv:2406.07273, Lemma B) to decide the rate questions; if T can be chosen "scale separated", test
      Conjecture 7.5 on that T (a positive answer for one admissible T would already give a Martín-type space with density, though not
      necessarily Martín's own).
 (P5) General finite-dimensional ranges E (not Hilbert): (R1) used the Hilbert structure; the joint-fibre/certificate machinery extends to
      l_2^d (Theorem 4.13) but not obviously to general E.

**Remarks on the sources (errors / non-sharp statements found).**
* No error found in (R1)-(R3) of the briefing, in Preprint A Thms 2.1-2.2, Props 3.2-3.3, or in the parts of Preprint B used here.
* The coefficient hypothesis "block quadratic coefficient <= 1" in the [Check] local-certificate theorem (as quoted in Preprint A,
  Section 1) and the hypothesis H <= 1 of Preprint A, Thm 3.1, are sufficient but NOT sharp: quadratic shifts along w (§4.5) give
  strictly larger recoverable classes (Example 4.18).
* Preprint A, Thm 3.1 relied on the unavailable [Check]; the dependence is now removed (Corollary 4.12, Theorem 6.2).
* Briefing (R6): "combined recoverability along a common sequence is plausible but not written down" - now proved, and along
  EVERY sequence (Corollaries 4.11-4.12, Theorems 4.17, 6.2, 6.5).
* Briefing (R7)(i) (one-sided base kinks): at points with finite contact set they cannot be used by piecewise-linear
  decompositions (Proposition 7.4); they force scale-dependent (cross) mechanisms.

**Suggested next step for the team.** Attack (P1)(a) on a single block with a in c_00 and finite contact set K: by Proposition 7.4
and Theorem 6.8, a defect mate must there use, on both sides and at all small scales, contact coordinates of K or weak peaks
carrying mass >> t; show (or refute, with explicit u_{k,m}) that two different such carriers cannot represent the same component of
g up to O(t). This is now a concrete approximation problem about (u_{k,m})_k, the weights Phi_m(k) and the values u_{k,m}(xi).

---------------------------------------------------------------------------------------------------

## Appendix. Numerical sanity checks
Script: `ctx/r1/check_expansions.py` (numpy, random instances). Results (run on 2026-10-08):
* Block certificate (Lemma 4.4): max |N(W(tau)) - (1 + tau^2 ||h_perp||^2/(sqrt(Y^2 + tau^2||h_perp||^2) + Y))| = 4.4e-16 over 2000 random
  instances x 21 values of tau in the validity window; the bound of Lemma 4.4(d) held in all cases.
* Base certificate (Lemma 4.3): the two-sided bounds (sigma^2/2) h/(1 + |sigma| beta/nu) <= q*(a + sigma b) - 1 <= (sigma^2/2) h (1 + 2|sigma| beta/nu)
  held in all 2000 x 21 cases.
* Monotone truncation (Lemma 6.4): with random a having many tiny entries (so sign flips occur), the ratio
  [q*(a + sigma c_t) - q*(a + sigma b)] / [sigma^2 (|kappa_t| ||b||_1 + ||c_t - b||_1)] never exceeded 0.098 (the lemma allows a constant
  max(4, 4||U||^2 max(||c||,||b||)/nu)), consistent with the lemma.
