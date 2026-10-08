# Strategy G: literature and tools survey for NA((c_0,p), F), F finite-dimensional, p = Martín norm

Author: research subagent (strategy G). Date of writing: 2026-10-08.

Status labels used throughout: **PROVED** (complete proof given here, or a short standard argument written
out in full), **PROVED (mod. cited)** (complete proof given, except for one explicitly cited standard
theorem), **SKETCH** (argument outlined; gaps named), **HEURISTIC**, **FALSE**, **OPEN**, **CITED** (statement
taken from the literature; not re-proved here; the reliability of my access to the statement is noted).

---------------------------------------------------------------------------------------------------------

## 0. Access caveat and executive summary

### 0.1 Access caveat (important for how much to trust Part 4)

From this sandbox, every direct fetch of arXiv, ar5iv, the publishers, Granada's repository and the
authors' home pages failed: WebFetch returned DNS errors and curl received a proxy 403. Only a web
*search* engine was reachable. It returns titles, abstracts and short excerpts. So the literature statements
in Part 4 come from three sources: (i) abstracts and excerpts returned by the search engine, (ii) the two
preprints in `ctx/`, and (iii) my own knowledge of the literature. Each item says which applies. Where
an exact formulation matters for a proof, I either re-prove the statement here or mark it **CITED**, with
a warning to check the original before relying on it in a paper.

### 0.2 Bottom line

1. **No published theorem that I could find covers Martín's space.** Each known sufficient condition
   on the *domain* X for density of NA(X, F), F finite-dimensional, fails for X = (c_0, p). The failures
   are proved here, not just asserted:
   - Lindenstrauss property A, Bourgain/RNP, Schachermayer α, Choi–Song quasi-α, and B_X being the closed
     convex hull of uniformly strongly exposed points all fail. X has **no** strongly exposed points
     (Prop. 3.2) and **fails property A** (Thm. 3.3).
   - The Johnson–Wolfe C(K) and L_1-predual mechanism and its compact-operator descendants (Martín's A^k
     for X* isometric to ℓ_1; Dantas–García–Maestre–Martín) fail. X* is not isometric to any L_1(μ), X**
     is not a C(K) (Prop. 3.6), and X admits **no** finite-rank operator P of rank ≥ 2 with P(B_X)
     closed. In particular there is no norm-one finite-rank projection of rank ≥ 2 (Prop. 3.1).
   - M-structure arguments fail. X has no nontrivial M-ideals or M-summands, X* has no nontrivial L- or
     M-summands (Prop. 3.6), and X is **not M-embedded** (Prop. 3.7).
   - Residuality/strong-exposure arguments (Bourgain ASE; Jung–Martín–Rueda Zoca) fail. SE(X) = ∅, so
     ASE(X, Y) = ∅ for every Y ≠ 0 (Cor. 3.4).
   - Dense-subspace and cone arguments (KLMW 2020; Choi–del Río–Fovelle–Jung–Martín 2025) fail. NA(X) ∩ E
     lies in two lines for each 2-dimensional E (Martín 2025).
   - The weak maximizing property and the compact perturbation property are irrelevant here. For
     finite-dimensional ranges each of them forces X to be reflexive (Prop. 4.16.1).
2. **Range-side techniques cannot help without solving the full problem.** Property β, quasi-β,
   ACK_ρ structure, AHSP and the universal BPB range property all give density NA(X, F) *for every X*.
   Applied to F = ℓ_2^2 they would settle the open question of whether ℓ_2^2 has Lindenstrauss
   property B. None is known for ℓ_2^2; β and quasi-β are known to fail for it.
3. **The counterexample mechanisms in the literature are intrinsically infinite-dimensional.** This
   covers Lindenstrauss (c_0 into strictly convex spaces), Gowers (ℓ_p), Acosta, Aguirre, Fovelle
   (locally AMUC ranges), and Martín 2014 (compact operators, through failure of the approximation
   property). Each uses either non-compactness of the target operator or failure of the AP. For
   finite-dimensional F every operator is of finite rank, and the mechanism of Thm. 3.3 degenerates
   (Remark 3.3.2). So the literature gives **no** heuristic evidence for a counterexample either.
4. **Tools that do apply** (all collected with proofs in Parts 2, 3 and 6):
   - the attainment criterion for finite-rank operators (Lemma 2.1);
   - the lift lemma and the permanence theorem (Preprint B; re-proved);
   - the recentering and near-ball lemmas (Preprint B). I re-proved both and found them **correct**.
     The proof of the recentering lemma is a three-line symmetric-containment argument, written in 6.3;
   - the primal transfer theorem (Preprint B);
   - **new here:** p is **Fréchet smooth** on X \ {0} (Thm. 3.8). Hence NA ∩ S_{p*} = ∇p(S_p) = the set of
     w*-strongly exposed points of B_{p*}, and the duality map is norm-to-norm continuous;
   - **new here:** the forced decomposition f ↦ (a, L^*w) is norm-to-norm continuous on S_{p*} (Prop. 3.9);
   - **new here:** an exact asymptotic formula for p*(f + b_n) along w*-null b_n (Prop. 3.10), with the
     bounds 1 + βq_0 ≤ lim p*(f + b_n) ≤ 1 + β;
   - the residual recovery / global compactness results of Preprint A, and the Kuratowski-limit
     reduction (R3) of the briefing.
5. **Assessment.** The problem has to be attacked with tools specific to the structure
   B_{p*} = B_{q*} + (compact), i.e. Preprints A and B. The most promising literature-inspired devices
   are (a) the recentering lemma, used with a *Hilbertian* "osculating disc" containment (this is
   exactly the mate inequality in ball form, see 6.3.3), and (b) Lindenstrauss-type iterative
   perturbations combined with the c_0-flat directions of p. The latter is HEURISTIC; see 7.6.

---------------------------------------------------------------------------------------------------------

## 1. Setting, notation, and what is imported

All spaces are real. X = c_0, X* = ℓ_1, X** = ℓ_∞. The canonical base norm q is given by

  B_q = B_{c_0} + U(B_H),  q*(a) = ||a||_1 + ||U^* a||_H,

with U : H → c_0 compact with dense range, H a Hilbert space. The Martín norm is

  p(x) = q(x) + ||L x||_V,  L x = (R_m x)_{m ∈ I},  V = (⊕_{m∈I} V_m)_{ℓ_1},  V_m = (ℓ_1, |·|_m),
  B_{|·|_m} = B_{ℓ_1} + D_m(B_{ℓ_2}),  N_m(w) := |w|_m^* = ||w||_∞ + ||D_m w||_2,
  (R_m x)(k) = m Φ_m(k) u_{k,m}(x),  Φ_m(k) = 2^{-m-k} q^*(T e_{k,m}),  u_{k,m} = T e_{k,m}/q^*(T e_{k,m}).

I is either a nonempty finite set (the norms p_J, p_N) or N (Martín's norm). Everything in Part 3 holds
for both, and for q itself where it makes sense.

Facts imported from Martín (arXiv:2406.07273) and the preprints, used below:

- (I1) [Martín; Preprint B (M4)] Each R_m : X → ℓ_1 is injective and compact, and ||R_m|| ≤ m 2^{-m}.
  Hence L is compact. B_{p*} = B_{q*} + L^*(B_{V*}), and K := L^*(B_{V*}) is norm compact.
- (I2) [Martín 2025, main theorem; Preprint B Thm. finite-blocks(a) for finite I] For every 2-dimensional
  subspace E ⊂ X*, NA(X, R) ∩ E is contained in the union of two lines. This is the "two-lines property".
- (I3) [Preprint A, citing the companion note "Recovery"; Preprint B Thm. finite-blocks(b) for finite I]
  p** is strictly convex. Every f ∈ S_{p*} has a unique normer ξ ∈ S_{p**} and a unique ("forced")
  decomposition f = a + L^*w with q*(a) = 1, a(ξ) = q**(ξ) =: q_0 > 0, w = J_V(L** ξ), and
  ||L**ξ||_V = 1 − q_0.
- (I4) [DGS smoothing lemma, Preprint B Lemma smoothing] If B_r = B_s + W(B_G) with W compact with dense
  range into (Z, s), G Hilbert, then r* = s* + ||W^*·|| and r is smooth. The proof of smoothness is
  re-done in 3.8.1 for the two cases needed.

Whenever a statement depends on (I2) or (I3), this is said explicitly.

Standard notation: NA(X, F) is the set of norm-attaining operators, and NA(X) := NA(X, R).
SE(X) ⊂ X* is the set of functionals that strongly expose some point of B_X. For a finite-rank
T : X → F, write T* : F* → X*.

---------------------------------------------------------------------------------------------------------

## 2. General tools for finite-dimensional ranges (domain-free)

### Lemma 2.1 (attainment criterion for finite-rank operators). PROVED.

Let X be a Banach space, F a finite-dimensional normed space and T ∈ L(X, F), T ≠ 0. Then T ∈ NA(X, F)
if and only if there is φ ∈ S_{F*} with ||T^*φ|| = ||T|| and T^*φ ∈ NA(X).

*Proof.* (⇒) Let T attain its norm at x_0 ∈ S_X. Choose φ ∈ S_{F*} with φ(Tx_0) = ||Tx_0|| = ||T||.
Then (T^*φ)(x_0) = ||T|| ≥ ||T^*φ||, so ||T^*φ|| = ||T|| and T^*φ attains its norm at x_0.
(⇐) If T^*φ attains its norm at x_0 ∈ S_X, then ||Tx_0|| ≥ φ(Tx_0) = ||T^*φ|| = ||T||. ∎

Also, for every T there is φ ∈ S_{F*} with ||T^*φ|| = ||T||, since S_{F*} is compact and
||T|| = sup_φ ||T^*φ||. So density of NA(X, F) is the following statement: every T can be perturbed so
that one of its "maximal dual directions" becomes a norm-attaining functional.

For F = ℓ_2^2 and T = (f, g), this is the reduction (R1) of the briefing. T attains its norm iff some
maximizer θ of θ ↦ ||cos θ f + sin θ g|| gives a norm-attaining functional cos θ f + sin θ g. After a
rotation (θ = 0), with ||T|| = 1, the statement is f ∈ S_{X*} ∩ NA(X) together with the **mate
inequality** ||f + t g||² ≤ 1 + t² for all t. This is the Kadets–López–Martín–Werner criterion (KLMW,
§4 of arXiv:1905.08272; CITED, consistent with the search excerpt in 4.12).

### Lemma 2.2 (KLMW; dense-subspace lemma). PROVED.

(a) If T is of finite rank and T^*(F^*) = (ker T)^⊥ ⊂ NA(X), then T ∈ NA(X, F).
(b) If D ⊂ NA(X) is a linear subspace that is norm dense in X*, then NA(X, F) ∩ Fin is dense in
Fin(X, F) for every F.

*Proof.* (a) follows from Lemma 2.1. (b) Given finite-rank T = Σ_{i≤n} f_i ⊗ y_i, approximate each f_i
by d_i ∈ D. Then S = Σ d_i ⊗ y_i has S^*(F^*) ⊂ span{d_i} ⊂ D ⊂ NA(X), so S ∈ NA by (a). ∎

*Applicability to Martín:* nil. By (I2), the only subspaces of X* contained in NA(X) have dimension ≤ 1.

### Lemma 2.3 (compact image of the ball forces NA functionals). PROVED.

Let P : X → E be a bounded operator into a finite-dimensional space E such that P(B_X) is closed.
Then P^*(E^*) ⊂ NA(X).

*Proof.* P(B_X) is bounded and closed in a finite-dimensional space, hence compact. For φ ∈ E^*,
||P^*φ|| = sup_{x∈B_X} φ(Px) = max_{u∈P(B_X)} φ(u), and the maximum is attained at some u = P x_0 with
x_0 ∈ B_X. So P^*φ attains its norm at x_0. ∎

### Lemma 2.4 (factorization principle behind Johnson–Wolfe). PROVED.

(a) Let T ∈ L(X, Y) and let P : X → X be a finite-rank operator with P(B_X) closed. Then TP ∈ NA(X, Y).
(b) Suppose X admits a net (P_α) of finite-rank operators with ||P_α|| ≤ 1, P_α(B_X) closed, and
||P_α^* x^* − x^*|| → 0 for every x^* ∈ X^*. Then NA(X, Y) ∩ Fin is dense in K(X, Y) for every Y, in
particular in L(X, F) for every finite-dimensional F.

*Proof.* (a) ||TP|| = sup_{u ∈ P(B_X)} ||Tu||. P(B_X) is closed and bounded in the finite-dimensional
range of P, hence compact, so the supremum is attained at some u = P x_0 with x_0 ∈ B_X.
(b) For compact T, the set T^*(B_{Y*}) is relatively norm compact in X^*. The operators P_α^* are
uniformly bounded and converge pointwise to the identity on X^*, so they converge uniformly on compact
sets. Hence ||T − TP_α|| = sup_{y^* ∈ B_{Y*}} ||T^*y^* − P_α^* T^* y^*|| → 0. Combine with (a). ∎

For c_0 with the sup norm, the coordinate projections P_n satisfy (b): P_n(B) = B_{ℓ_∞^n} is closed and
P_n^* → I pointwise on ℓ_1. For C(K), Johnson and Wolfe use norm-one projections built from partitions
of unity. Note that (b) needs pointwise convergence of the *adjoints*.

### Lemma 2.5 (Bishop–Phelps–Bollobás for functionals). CITED (classical; Bollobás 1970; sharp form
Chica–Kadets–Martín–Moreno-Pulido–Rambla-Barreno 2014).

If x ∈ S_X, f ∈ S_{X*} and f(x) > 1 − ε²/2, then there are x_0 ∈ S_X and f_0 ∈ S_{X*} with
f_0(x_0) = 1, ||x − x_0|| < ε and ||f − f_0|| < ε.

### Lemma 2.6 (primal description of mate fibres; check of briefing (R2)). PROVED.

For f ∈ S_{X*} put C(f) = {g ∈ X* : ||(f, g)||_{X→ℓ_2^2} ≤ 1}. Then
C(f) = {g ∈ X* : |g(y)| ≤ r_f(y) for all y}, where r_f(y) := (||y||² − f(y)²)^{1/2}. Hence C(f) is the
dual unit ball of the seminorm r̃_f, the largest sublinear minorant of r_f:
r̃_f(x) = inf{Σ_j r_f(y_j) : Σ_j y_j = x, finite sums}. Its support function at x is r̃_f(x).

*Proof.* ||(f, g)|| ≤ 1 iff f(y)² + g(y)² ≤ ||y||² for all y, i.e. |g(y)| ≤ r_f(y). The function r_f is
positively homogeneous and even, so its convex envelope r̃_f is a seminorm (even, homogeneous and
subadditive by construction). A linear g satisfies g ≤ r_f iff g ≤ r̃_f, because r̃_f is the largest
sublinear function below r_f and g is sublinear. By evenness, g ≤ r̃_f iff |g| ≤ r̃_f. By Hahn–Banach,
for each x there is a linear g ≤ r̃_f with g(x) = r̃_f(x). It is automatically continuous since
r̃_f ≤ ||·||. ∎

So (R2) of the briefing is **correct**.

---------------------------------------------------------------------------------------------------------

## 3. Structural facts about Martín's space that decide applicability (new proofs)

### Proposition 3.1 (no compact-image operators of rank ≥ 2). PROVED (mod. (I2)).

Let X = (c_0, p) with p a Martín norm (any I). If P : X → E is a finite-rank operator with P(B_X)
closed, then rank P ≤ 1. In particular:
(a) X has no norm-one projection of finite rank ≥ 2;
(b) every S ∈ NA(X, F) of rank ≥ 2 has S(B_X) not closed;
(c) Lemma 2.4 can never produce approximants of a rank-2 operator: for rank T = 2, TP has rank ≥ 2
    only if rank P ≥ 2, which (a) and Lemma 2.3 exclude.

*Proof.* By Lemma 2.3, P^*(E^*) ⊂ NA(X). P^*(E^*) is a linear subspace of dimension rank P. If
rank P ≥ 2 it contains a 2-dimensional subspace E_0 ⊂ NA(X). E_0 is not contained in a union of two
lines, which contradicts (I2). For (a): if P is a projection with ||P|| = 1, then
P(B_X) = B_X ∩ P(X) (since P(B_X) ⊂ B_X ∩ PX ⊂ P(B_X)), which is closed. (b) is the case P = S. ∎

**Remark 3.1.1.** This excludes the entire family of "finite-dimensional factorization" methods:
Johnson–Wolfe partitions of unity on C(K), coordinate projections on c_0 and Read's space (Preprint B
Lemma projections), Lazar–Lindenstrauss ℓ_∞^n-approximation of L_1-preduals, and the metric
π-property / MAP with norm-one finite-rank projections. They all produce NA operators of the form TP
with P(B_X) compact.

### Lemma 3.2.0 (asymptotic c_0-flatness of p). PROVED.

Let p = q + ||L·||_V be a canonical-base Martín norm (any I), or p = q. For every x ∈ X \ {0} and every
0 < δ ≤ q(x)/2 there is n_0 such that q(x ± δ e_n) ≤ q(x) for n ≥ n_0. Moreover
lim_n p(x ± δ e_n) = p(x).

*Proof.* B_q = B_{c_0} + U(B_H) is closed (a closed set plus a compact set). So x/q(x) = z + U h with
||z||_∞ ≤ 1, z ∈ c_0, h ∈ B_H; z ∈ c_0 because U maps into c_0. Choose n_0 with |z_n| ≤ 1/2 for
n ≥ n_0. Then ||z ± (δ/q(x)) e_n||_∞ ≤ 1, so (x ± δe_n)/q(x) ∈ B_q, i.e. q(x ± δ e_n) ≤ q(x).
Next, (e_n) is weakly null in c_0 and L is compact, so ||L e_n||_V → 0 and
p(x ± δ e_n) ≤ q(x) + ||Lx|| + δ||L e_n|| → p(x). Finally, p(x ± δ e_n) ≥ (∇p(x))(x ± δ e_n) =
p(x) ± δ (∇p(x))_n → p(x), since ∇p(x) ∈ ℓ_1 (or use any norming functional). ∎

### Proposition 3.2 (no strongly exposed points; not LUR). PROVED.

For a canonical-base Martín norm p (any I), the unit ball B_p has no strongly exposed points, and p is
not locally uniformly rotund. Consequently SE(X) = ∅.

*Proof.* Let x ∈ S_p and let f ∈ S_{p*} be any functional with f(x) = 1. (By smoothness, 3.8.1, f is
unique, but this is not needed.) Fix δ = q(x)/2 > 0 and put y_n = (x + δ e_n)/p(x + δ e_n). By
Lemma 3.2.0, p(x + δe_n) → 1 and f(x + δ e_n) = 1 + δ f_n → 1 (as f ∈ ℓ_1), so f(y_n) → 1. But with p_n := p(x + δ e_n) → 1 we have y_n − x = (1/p_n − 1)x + (δ/p_n) e_n, so
p(y_n − x) ≥ (δ/p_n) p(e_n) − |1/p_n − 1| and liminf p(y_n − x) ≥ δ c > 0, where c = inf_n p(e_n) > 0
because p is equivalent to the sup norm. So f does not strongly expose x. As x and f were arbitrary, B_p has no strongly exposed points.
Not LUR: with u_n = y_n, p(u_n) = 1 and p(x + u_n) ≥ f(x + u_n) → 2, but u_n does not tend to x. ∎

### Theorem 3.3 (Martín's space fails Lindenstrauss property A). PROVED.

Let X = (c_0, p) with p a canonical-base Martín norm (any I; also p = q). Let Y = (c_0, r) with r an
equivalent LUR norm (exists by Day/Kadec). Then the formal identity I : X → Y is not in the closure of
NA(X, Y). More precisely, every S ∈ NA(X, Y) satisfies ||S e_n||_r → 0. Hence X fails property A.

*Proof.* Let S ∈ NA(X, Y), S ≠ 0, attain its norm at x ∈ S_p. Set λ = ||S|| = r(Sx) > 0 and
δ = q(x)/2. By Lemma 3.2.0, r(Sx ± δ S e_n) ≤ λ p(x ± δ e_n) → λ. Put u = Sx/λ,
u_n^± = (Sx ± δ S e_n)/λ. Then r(u) = 1, limsup r(u_n^±) ≤ 1 and u = (u_n^+ + u_n^−)/2. Hence
r(u_n^+) ≥ 2 − r(u_n^−) gives r(u_n^+) → 1. Also r(u + u_n^+) = r(3u − u_n^−) ≥ 3 − r(u_n^−) → ≥ 2,
and r(u + u_n^+) ≤ r(u) + r(u_n^+) → 2. LUR of r at u gives u_n^+ → u, i.e. δ S e_n → 0.

If ||S − I||_{p→r} < ε, then r(S e_n) ≥ r(e_n) − ε p(e_n) ≥ a − ε b, with a = inf r(e_n) > 0 and
b = sup p(e_n) < ∞. For ε < a/(2b) this contradicts S e_n → 0. So dist(I, NA(X, Y)) ≥ a/(2b) > 0. ∎

**Remark 3.3.1.** By Choi–Song, quasi-α implies A; by Schachermayer, α implies A; by Lindenstrauss,
"B_X is the closed convex hull of a uniformly strongly exposed set" implies A; by Bourgain, the RNP
gives A for all renormings. All of these therefore **fail** for Martín's space. (Some failures also
follow directly from Prop. 3.2.)

**Remark 3.3.2 (why this obstruction says nothing for finite-dimensional F).** In the proof above, the
contradiction came from ||S e_n|| ≥ a/2 > 0, i.e. from S being far from compact. For F
finite-dimensional, every S ∈ L(X, F) is compact, so S e_n → 0 automatically and the first-order
argument is void. What survives is a *second-order* constraint. If S = (f, g) : X → ℓ_2^2 attains its
norm 1 at x, then

  ||Sx + δ S e_n||_2² = 1 + 2δ⟨Sx, S e_n⟩ + δ² ||S e_n||² ≤ p(x + δ e_n)²  for all small δ, all large n.

Combined with the flatness q(x + δ e_n) ≤ q(x), this only constrains the block term
||L(x + δ e_n)||. This is the "far-coordinate mate condition", the content of (R5)/(R6) of the
briefing. HEURISTIC remark; no claim.

### Corollary 3.4 (strong exposure / residuality route closed). PROVED (mod. cited definitions).

SE(X) = ∅ for X = (c_0, p). Hence, for every Banach space Y ≠ {0}, Bourgain's set ASE(X, Y) of
absolutely strongly exposing operators is empty. The Jung–Martín–Rueda Zoca and Bourgain density
theorems (which produce dense ASE operators, and need SE(X) to be dense) cannot apply.

*Proof.* Prop. 3.2. If T ∈ ASE(X, Y) then, by definition, there is x_0 ∈ S_X such that every
maximizing sequence of T converges (up to sign) to x_0. Composing with y^* norming Tx_0 shows that
T^*y^* strongly exposes x_0 (the standard argument; JMRZ note that ASE dense implies SE(X) dense).
So ASE(X, Y) ≠ ∅ would force SE(X) ≠ ∅. ∎

**Remark 3.4.1.** JMRZ (arXiv:2203.04023), according to its abstract, also prove a converse: for
separable X and Y*, residuality of NA(X, Y) implies density of ASE(X, Y). If that statement is as
quoted, it gives that NA((c_0, p), F) is **not residual** in L(X, F) for every finite-dimensional
F ≠ 0. CITED-conditional. For F = R this is independently PROVED in Preprint A
(Prop. nonvacuity: NA ∩ S_{p*} ⊂ ∪_n F_n, a countable union of compact sets, hence meagre).

### Proposition 3.6 (no L/M-structure). PROVED (mod. (I3)).

Let X = (c_0, p), p a Martín norm (any I), and use (I3): p** is strictly convex. Then:
(a) X** has no nontrivial L-summand or M-summand;
(b) X* has no nontrivial L-summand or M-summand;
(c) X has no nontrivial L-summand or M-summand, and no nontrivial M-ideal;
(d) X* is not isometric to any L_1(μ) space and X is not an L_1-predual (Lindenstrauss space);
    in particular X* is not isometric to ℓ_1, and X is not isometric to any C(K) or C_0(L);
(e) X** is not isometric to any C(K) space.

*Proof.* (a) If X** = A ⊕_∞ B with A, B ≠ 0, take α ∈ S_A and β ∈ S_B. Then ||α + tβ|| = 1 for |t| ≤ 1,
a segment in the sphere. If X** = A ⊕_1 B, then ||tα + (1 − t)β|| = 1 for t ∈ [0, 1]. Either way strict
convexity fails.
(b) X* = A ⊕_1 B gives X** = A* ⊕_∞ B*, and X* = A ⊕_∞ B gives X** = A* ⊕_1 B*. Apply (a).
(c) X = A ⊕_1 B gives X** = A** ⊕_1 B**, and similarly for ⊕_∞. If J ⊂ X is an M-ideal, then by
definition J^⊥ is an L-summand in X*. By (b), J^⊥ ∈ {0, X*}, i.e. J ∈ {X, 0} (J is closed).
(d) If X* ≅ L_1(μ) isometrically, then X** ≅ L_1(μ)* isometrically. The dual of an AL-space is an AM-space
with unit, hence (Kakutani) isometric to C(K) for a compact K with at least two points, since
dim X** ≥ 2. C(K) is not strictly convex: take 1 and v ∈ C(K) with ||v|| = 1, v(k_0) = 1, v ≠ 1
(Urysohn). Then ||(1 + v)/2|| = 1. Contradiction. If X were isometric to C(K) or C_0(L), then X*
would be isometric to an L_1(μ). (e) is shown in the proof of (d). ∎

**Consequences.** The following are inapplicable to Martín's space:
- Johnson–Wolfe (X = C(K));
- Martín 2014/2016 "X* isometric to ℓ_1 ⇒ property A^k";
- Dantas–García–Maestre–Martín "BPBp-k transfers from (c_0, Y) to (X, Y) when X* ≅ ℓ_1 isometrically,
  and to C_0(L)";
- all arguments based on L-summands, M-summands or M-ideals in X, X* or X**.

### Proposition 3.7 (X is not M-embedded). PROVED (mod. cited: HWW characterization).

Let p be a canonical-base Martín norm (any I). Then X = (c_0, p) is not an M-ideal in its bidual.

*Cited fact* (Harmand–Werner–Werner, *M-ideals in Banach spaces and Banach algebras*, LNM 1547,
Prop. I.1.12 and Remark III.1.2). If X is M-embedded, then X*** = i(X*) ⊕_1 X^⊥, where i is the
canonical embedding. Reason: the L-projection with kernel X^⊥ has range consisting of the unique
norm-preserving extensions of elements of X*, and i(f) is such an extension.

*Proof.* Suppose X is M-embedded. Choose w ∈ V^* with ||w||_{V*} ≤ 1 and L^*w ≠ 0; then c := p*(L^*w) > 0.

(i) Upper bound. L^*w + e_n^* = e_n^* + L^*w is an admissible decomposition in B_{p*} = B_{q*} + L^*(B_{V*})
(scaled), so p*(L^*w + e_n^*) ≤ max(q*(e_n^*), ||w||) ≤ max(1 + ||U^*e_n^*||_H, 1). Now (e_n^*) is
bounded and w*-null in ℓ_1 = c_0^*, and U^* is compact and w*-to-weak continuous, so ||U^*e_n^*|| → 0.
Hence limsup_n p*(L^*w + e_n^*) ≤ 1.

(ii) Lower bound. Let Φ ∈ X*** be a w*-cluster point of (i(e_n^*)) along a free ultrafilter 𝒰.
- Φ ∈ X^⊥, because Φ(x) = lim_𝒰 x_n = 0 for x ∈ c_0.
- ||Φ|| ≤ 1, since p*(e_n^*) ≤ q*(e_n^*) → 1.
- ||Φ|| ≥ 1. Let χ_N = 1_{[N,∞)} ∈ ℓ_∞ = X**. We have Φ(χ_N) = lim_𝒰 χ_N(n) = 1, and
  p**(χ_N) ≤ q**(χ_N) + ||L**χ_N||_V ≤ 1 + ||L**χ_N||_V. Here q**(χ_N) ≤ ||χ_N||_∞ = 1 because
  B_{ℓ_∞} = w*-cl B_{c_0} ⊂ w*-cl B_q = B_{q**}. Also χ_N → 0 in σ(ℓ_∞, ℓ_1), and L** is w*-to-norm
  continuous on bounded sets (L compact), so ||L**χ_N|| → 0. Hence ||Φ|| ≥ sup_N 1/p**(χ_N) = 1.

By the cited L-decomposition and w*-lower semicontinuity of the norm of X***,

  liminf_𝒰 p*(L^*w + e_n^*) ≥ ||i(L^*w) + Φ|| = p*(L^*w) + ||Φ|| = c + 1 > 1,

which contradicts (i). ∎

**Remark 3.7.1.** For the base norm q alone the same computation is consistent with M-embeddedness.
One computes q***(Φ) = q*(πΦ) + ||Φ − πΦ||_{ℓ_1***} for Φ ∈ ℓ_1***, π the canonical projection, since
U***Φ = U^*(πΦ). So (ℓ_1, q*) is L-embedded (SKETCH). It is precisely the compact block term L^*(B_{V*})
that destroys the L-decomposition: compact perturbations of the *dual ball* do not preserve
L-embeddedness, while compact perturbations of the *dual norm* (q* = ||·||_1 + ||U^*·||) do.

### Theorem 3.8 (p is Fréchet smooth). PROVED (mod. (I1)).

Let p be a canonical-base Martín norm (any I), or p = q. Then p is Fréchet differentiable at every
x ≠ 0. Consequently:
(a) the duality map ∇p : S_p → S_{p*} is norm-to-norm continuous;
(b) NA(X) ∩ S_{p*} = ∇p(S_p) = {w*-exposed points of B_{p*}} = {w*-strongly exposed points of B_{p*}};
(c) for every x ∈ S_p and ε > 0 there is δ > 0 such that f ∈ B_{p*} and f(x) > 1 − δ imply
    p*(f − ∇p(x)) < ε. This is the pointwise Šmulyan modulus; it is **not** uniform in x, since
    X = c_0 has no uniformly smooth renorming.

**3.8.1 Smoothness (Gâteaux).** q* is strictly convex: if q*(a) = q*(b) = 1 and q*(a + b) = 2, then
||a + b||_1 = ||a||_1 + ||b||_1 and ||U^*a + U^*b|| = ||U^*a|| + ||U^*b||. U^* is injective (U has dense
range), so either U^*b = λU^*a with λ ≥ 0, or one of them vanishes. U^*b = λ U^*a gives b = λa, and
then λ = 1. If U^*a = 0 then a = 0, which is impossible. So a = b. A dual strictly convex norm makes the
predual norm smooth, so q is smooth. The same argument shows |·|_m is smooth on ℓ_1 (D_m: ℓ_2 → ℓ_1 is
injective with dense range, since its range contains c_00).

For p: ∂p(x) = ∂q(x) + L^* ∂||·||_V(Lx) (sum rule for continuous convex functions; ||·||_V ∘ L has
subdifferential L^*∂||·||_V(Lx)). ∂q(x) is a singleton. Lx = (R_m x)_m has every component nonzero by
injectivity of R_m (I1). For an ℓ_1-sum norm at a point with all components nonzero, the subdifferential
is the product of the component subdifferentials, each a singleton by smoothness of |·|_m. So ∂p(x)
is a singleton.

**3.8.2 Fréchet differentiability.** By Šmulyan's lemma (Deville–Godefroy–Zizler, Lemma I.1.4), it
suffices to show: if x ∈ S_p, f_n ∈ B_{p*} and f_n(x) → 1, then f_n → ∇p(x) in norm.

Write f_n = a_n + L^*w_n with q*(a_n) ≤ 1 and ||w_n||_{V*} ≤ 1. Then a_n(x) ≤ q(x) and
w_n(Lx) ≤ ||Lx||_V, and the sum of the two tends to q(x) + ||Lx|| = 1. Hence a_n(x) → q(x) and
w_n(Lx) → ||Lx||.

*Base part.* Write x = q_0 (z + U h) with q_0 = q(x) > 0, ||z||_∞ ≤ 1, z ∈ c_0, ||h|| ≤ 1. Then

  a_n(x)/q_0 = a_n(z) + ⟨U^*a_n, h⟩ ≤ Σ_j |a_n(j)||z_j| + ||U^*a_n|| = q*(a_n) − Σ_j |a_n(j)|(1 − |z_j|)
            ≤ 1 − Σ_j |a_n(j)|(1 − |z_j|).

So Σ_j |a_n(j)|(1 − |z_j|) → 0. Let G = {j : |z_j| ≥ 1/2}, a finite set since z ∈ c_0. Then
Σ_{j∉G} |a_n(j)| ≤ 2 Σ_j |a_n(j)|(1 − |z_j|) → 0. On the finite set G the coordinates are bounded. So
every subsequence of (a_n) has a further subsequence converging in ℓ_1-norm to some a′ with
q*(a′) ≤ 1 and a′(x) = q(x). By smoothness of q, a′ = ∇q(x) =: a_x is unique. Hence a_n → a_x in norm.

*Block part.* Every subsequence of (w_n) has a w*-convergent further subsequence w_n → w. Since L^* is
w*-to-norm continuous on bounded sets (L compact), L^*w_n → L^*w in norm. Then f := a_x + L^*w ∈ B_{p*}
and f(x) = 1, so f = ∇p(x) by smoothness of p. Hence every subsequence of (f_n) has a further
subsequence converging in norm to ∇p(x), so f_n → ∇p(x).

(a) and (c) are the standard reformulations. For (b): if f ∈ NA ∩ S_{p*} attains at x ∈ S_p, then
{g ∈ B_{p*} : g(x) = 1} = {∇p(x)} = {f}. So f is w*-exposed by x, and by 3.8.2 even w*-strongly exposed.
Conversely, a w*-exposed point is exposed by some x ∈ X, hence attains its norm. ∎

**Remark 3.8.3.** Theorem 3.8 is compatible with Prop. 3.2. Fréchet smoothness is about the *dual*
ball (w*-strong exposure of B_{p*}); Prop. 3.2 is about the *primal* ball. It is a useful positive tool:
NA ∩ S_{p*} is a norm-continuous image of the path-connected separable sphere S_p, and approximate
normers give approximate gradients pointwise (3.8(c)).

**Remark 3.8.4.** For the canonical choice, Martín's (M1) only asserted Gâteaux smoothness. I have not
checked whether Martín's paper uses a base for which Fréchet smoothness fails. The proof above uses
only: B_q = B_{c_0} + U(B_H), U compact with dense range, and L compact with injective components.

### Proposition 3.9 (continuity of the forced decomposition). PROVED (mod. (I3)).

Let f_n → f in S_{p*}, with forced decompositions f_n = a_n + L^*w_n and f = a + L^*w (I3), and normers
ξ_n, ξ ∈ S_{p**}. Then:
- ξ_n → ξ weak*;
- L**ξ_n → L**ξ in norm;
- w_n → w weak* (coordinatewise in each block);
- L^*w_n → L^*w in norm;
- a_n → a in ℓ_1-norm;
- q**(ξ_n) → q**(ξ), i.e. the contact numbers q_0 vary continuously.

*Proof.* B_{p**} is w*-compact. If η is a w*-cluster point of (ξ_n), then
f(η) = lim f_n(ξ_n) − lim (f_n − f)(ξ_n) = 1, so η = ξ by uniqueness of the normer (I3). Hence
ξ_n → ξ weak*. L** is w*-to-norm continuous on bounded sets, so L**ξ_n → L**ξ in norm, and
||L**ξ_n|| → ||L**ξ||, i.e. 1 − q**(ξ_n) → 1 − q**(ξ).

For w_n: (w_n) is bounded in V^*. If w′ is a w*-cluster point, then
w′(L**ξ) = lim w_n(L**ξ_n) = lim ||L**ξ_n|| = ||L**ξ|| and ||w′|| ≤ 1. So w′ is a norming functional
of L**ξ ∈ V. Since L**ξ has all components R_m**ξ ≠ 0 (R_m** injective, Preprint B), the norm of V is
smooth at L**ξ (3.8.1), so w′ = w. Hence w_n → w weak*, and L^*w_n → L^*w in norm by compactness.
Then a_n = f_n − L^*w_n → f − L^*w = a in norm. ∎

**Remark.** The block support functionals w_n themselves need **not** converge in V^*-norm (ℓ_∞-norm in
each block). One can move far coordinates of w_n by a fixed amount at small cost. This is exactly the
"freedom in the far coordinates" of (R4) (see 6.6.3). Concretely: if |w(k)| < M at a far index k
with tiny Φ_m(k), changing w(k) by a fixed amount changes N_m(w) only through ||D_m w||_2, i.e. by
O(Φ_m(k)), so near-optimal block functionals can differ from w in ℓ_∞-norm by a fixed amount.

### Proposition 3.10 (asymptotic dual norm along w*-null sequences). PROVED.

Let f ∈ X* and let (b_n) ⊂ ℓ_1 be bounded and w*-null (coordinatewise null) with ||b_n||_1 → β. Then

  lim_n p*(f + b_n) = Ψ_f(β) := min_{w ∈ V^*} max( q*(f − L^*w) + β , ||w||_{V*} ).

If f ∈ S_{p*} has normer ξ and contact number q_0 = q**(ξ), then 1 + β q_0 ≤ Ψ_f(β) ≤ 1 + β.

*Proof.* Recall p*(h) = min{max(q*(a), ||w||) : h = a + L^*w}. The minimum is attained because
{||w|| ≤ λ} is w*-compact and w ↦ q*(h − L^*w) is w*-continuous on bounded sets (L^* is w*-to-norm
continuous there).

Key fact (asymptotic additivity in ℓ_1): for c ∈ ℓ_1 and (b_n) as above, ||c + b_n||_1 − ||c||_1 −
||b_n||_1 → 0. Given ε, take N with Σ_{j>N}|c_j| < ε. The first N coordinates of b_n tend to 0, and
the tail estimate gives the claim up to 2ε. Moreover ||U^*b_n|| → 0 (compact adjoint, w*-null bounded
sequence). Hence for c_n → c in norm, q*(c_n + b_n) → q*(c) + β.

Upper bound: for each w, f + b_n = (f − L^*w + b_n) + L^*w, so
limsup p*(f + b_n) ≤ max(q*(f − L^*w) + β, ||w||). Take the infimum over w.

Lower bound: choose optimal decompositions f + b_n = c_n + L^*w_n. Pass to a subsequence realizing the
liminf with w_n → w weak*, so L^*w_n → L^*w in norm. Then c_n = (f − L^*w) + b_n + o(1), so
q*(c_n) → q*(f − L^*w) + β. Also ||w|| ≤ liminf ||w_n||. Hence
liminf p*(f + b_n) ≥ max(q*(f − L^*w) + β, ||w||) ≥ Ψ_f(β).

Bounds: the forced decomposition (w = w_f) gives Ψ_f(β) ≤ max(1 + β, 1) = 1 + β. For the lower bound,
q*(f − L^*w) ≥ (f − L^*w)(ξ)/q_0 ≥ (1 − ||w||(1 − q_0))/q_0. With s = ||w||, the maximum of the
decreasing function (1 − s(1 − q_0))/q_0 + β and the increasing function s is at least the value at
their crossing point s = 1 + βq_0. ∎

**Consequences.**
(i) Far-supported base perturbations are never mates, quantitatively. For g = t e_n^* with n large,
p*(f + t e_n^*) → Ψ_f(|t|) ≥ 1 + |t| q_0 > (1 + t²)^{1/2} for 0 < |t| < 2q_0/(1 − q_0²). This is a
concrete instance of the mechanism behind Preprint A's global compactness theorem.
(ii) Ψ_f(β) < 1 + β whenever a is a smooth point of q* (for instance supp a = N) and β > 0. Proof:
take w = (1 + μ) w_f with μ small; the one-sided derivative of q* at a in direction −L^*w_f equals
−(1 − q_0)/q_0 < 0. This is another manifestation of the failure of M-embeddedness (Prop. 3.7).

---------------------------------------------------------------------------------------------------------

## 4. Literature survey: statements, references, applicability

For each item: statement (as precisely as I could establish), reference with URL, source of my
knowledge, and assessment for X = (c_0, p).

### 4.1 Lindenstrauss (1963)

J. Lindenstrauss, *On operators which attain their norm*, Israel J. Math. 1 (1963) 139–148.
(Source: classical; confirmed in survey excerpts, e.g. Martín's RACSAM survey arXiv:1502.07084.)

Statements (CITED):
(a) Property A holds for reflexive X. More generally, it holds if B_X is the closed absolutely convex
    hull of a uniformly strongly exposed set.
(b) Property β of Y (a norming set {y_λ*} ⊂ S_{Y*} with points y_λ ∈ S_Y, y_λ*(y_λ) = 1 and
    |y_μ*(y_λ)| ≤ ρ < 1 for λ ≠ μ) implies property B. Finite-dimensional polyhedral spaces, c_0 and
    ℓ_∞ have β.
(c) For all X, Y, the set {T : T** attains its norm} is dense in L(X, Y).
(d) c_0, C[0, 1] and L_1[0, 1] fail A. The c_0 argument uses a strictly convex renorming of c_0 as
    range.

Applicability:
- (a) fails (Prop. 3.2).
- (b) is range-side; ℓ_2^2 fails β, since β for finite-dimensional spaces forces finitely many extreme
  points (polyhedrality).
- (c) is trivial for finite-dimensional F: T** = T on X** is w*-continuous, and B_{X**} is w*-compact.
- (d): the c_0 argument transfers to Martín's space (Theorem 3.3) but is void for finite-dimensional
  ranges (Remark 3.3.2).

### 4.2 Bourgain (1977), Stegall (1978/86), Huff (1980)

J. Bourgain, *On dentability and the Bishop–Phelps property*, Israel J. Math. 28 (1977) 265–271.
C. Stegall, *Optimization of functions on certain subsets of Banach spaces*, Math. Ann. 236 (1978)
171–176; *Optimization and differentiation in Banach spaces*, Linear Algebra Appl. 84 (1986) 191–211.
R. Huff, *On non-density of norm-attaining operators*, Rev. Roumaine Math. Pures Appl. 25 (1980)
239–241. (Source: classical; JMRZ and RSE-paper excerpts confirm the Bourgain ASE statement.)

Statements (CITED):
- If X has the RNP, then ASE(X, Y) is a dense G_δ in L(X, Y) for every Y; so X has property A in every
  renorming.
- Conversely (Bourgain–Huff), if X fails the RNP, some renorming of X fails property A.
- Stegall's variational principle: if C is a bounded closed convex set with the RNP and φ : C → R is
  usc and bounded above, then for a dense G_δ of x* ∈ X*, φ + x* attains a strong maximum on C.
  Asplund version: if X is Asplund, K ⊂ X* is w*-compact and φ is w*-usc, then for a dense G_δ of
  x ∈ X, φ + x strongly attains its sup on K.

Applicability: X ≅ c_0 fails the RNP. The primal Stegall principle needs RNP of B_X, which fails.
The dual (Asplund) version applies to K ⊂ X*. But the quantity to be maximized is ||Tx|| on B_X, and
its dual reformulation max_{φ∈S_{F*}} p*(T^*φ) is attained trivially (compact S_{F*}). Attainment *at an
NA functional* is not a variational statement on X*. **Inapplicable** in the direct form; see 7.5.

### 4.3 Uhl (1976), Diestel–Uhl (1976/77), Iwanik

J. J. Uhl, *Norm attaining operators on L_1[0,1] and the Radon–Nikodým property*, Pacific J. Math. 63
(1976) 293–300. J. Diestel, J. J. Uhl, *The Radon–Nikodym theorem for Banach space valued measures*,
Rocky Mountain J. Math. 6 (1976) 1–46. (Source: classical; Martín 2014 excerpt confirms the Diestel–Uhl
statement on finite-rank NA operators from L_1(μ).)

Statement (CITED): NA(L_1(μ), Y) ∩ Fin is dense in K(L_1(μ), Y) (Diestel–Uhl), and NA(L_1[0,1], Y) is
dense iff Y has the RNP (Uhl). Applicability: domain L_1. Martín's X* is ℓ_1 isomorphically, but the
domain is X, not X*. **Inapplicable.**

### 4.4 Zizler (1973)

V. Zizler, *On some extremal problems in Banach spaces*, Math. Scand. 32 (1973) 214–224 (density of
operators whose adjoints attain their norms). CITED (classical). For finite-dimensional F, T^* is
defined on a finite-dimensional space and always attains its norm. **Void.**

### 4.5 Johnson–Wolfe (1979) and "Question 6"

J. Johnson, J. Wolfe, *Norm attaining operators*, Studia Math. 65 (1979) 7–19.
https://eudml.org/doc/218261 (Source: search excerpts quoting Martín's surveys, plus memory.)

Statements (CITED):
(a) NA(X, Y) ∩ Fin is dense in K(X, Y) whenever X is a C(K) space, or Y is an L_1(μ) space or an
    isometric predual of an L_1-space. As quoted in Martín's surveys, the L_1 conditions are on the
    **range** Y.
(b) In the real case, NA(C(K), C(S)) is dense in L(C(K), C(S)). The complex case was settled only in
    2026: García–Maestre–Rodríguez-Vidanes, arXiv:2605.28466, by a measure-theoretic phase-correction
    argument.
(c) Johnson–Wolfe asked whether every compact operator, and in particular every finite-rank operator,
    is approximable by NA operators. Martín's 2024 notes quote them calling the finite-rank question
    the "most irritating" open problem. The briefing calls it "Question 6". I could not access the
    numbered list to confirm the number.

Mechanism of (a), domain C(K): partitions of unity give norm-one projections P onto ℓ_∞^n subspaces
with TP → T for compact T, and TP attains its norm (Lemma 2.4).

Applicability: X is not C(K) (Prop. 3.6(d)) and has no norm-one finite-rank projections of rank ≥ 2
(Prop. 3.1). The range condition is useless for F = ℓ_2^2: ℓ_2^2 is not an L_1-predual, since its dual
ℓ_2^2 is not an L_1 space. **Inapplicable.**

### 4.6 Schachermayer (1983)

W. Schachermayer, *Norm attaining operators and renormings of Banach spaces*, Israel J. Math. 44 (1983)
201–212; *Norm attaining operators on some classical Banach spaces*, Pacific J. Math. 105 (1983)
427–438. (Source: classical; survey excerpts.)

Statements (CITED):
- Property α (a family {(x_i, x_i^*)} with x_i^*(x_i) = 1 = ||x_i|| = ||x_i^*||, |x_i^*(x_j)| ≤ ρ < 1
  for i ≠ j, and B_X = cl aco{x_i}) implies property A.
- Every WCG space, in particular c_0, has an equivalent norm with property α.
- Every weakly compact operator from C(K) into any Y is approximable by NA operators.

Applicability: α implies the x_i are uniformly strongly exposed. If x_i^*(y) > 1 − η for y ∈ B_X, then
with y ≈ Σ c_j x_j we get c_i ≥ 1 − η/(1 − ρ) and ||y − x_i|| ≤ 2η/(1 − ρ). So α is excluded by
Prop. 3.2. The C(K) result is excluded by Prop. 3.6. **Inapplicable.** It does show that **c_0 has
renormings with property A**, so failure of A for Martín's norm is a feature of p, not of c_0.

### 4.7 Partington (1982); Acosta–Aguirre–Payá (1996) quasi-β; Choi–Song (2008) quasi-α

J. R. Partington, *Norm attaining operators*, Israel J. Math. 43 (1982) 273–276: every Banach space can
be renormed to have β.
M. D. Acosta, F. J. Aguirre, R. Payá, *A new sufficient condition for the denseness of norm attaining
operators*, Rocky Mountain J. Math. 26 (1996) 407–418: property quasi-β of Y implies B.
Y. S. Choi, H. G. Song, *Property (quasi-α) and the denseness of norm attaining mappings*, Math. Nachr.
281 (2008) 1264–1272, https://doi.org/10.1002/mana.200510676.
(Source: search excerpts. In particular "quasi-α implies A; the Euclidean space R^n fails quasi-α;
quasi-α is stable under finite ℓ_1-sums".)

Definition (CITED from secondary source): X has quasi-α if there are A = {x_λ} ⊂ S_X,
{x_λ^*} ⊂ S_{X*} and ρ : A → [0, 1) with x_λ^*(x_λ) = 1 and |x_μ^*(x_λ)| ≤ ρ(x_μ) for λ ≠ μ, and such
that for every e ∈ ext B_{X**} there is A_e ⊂ A with e or −e in the w*-closure of A_e and
sup_{A_e} ρ < 1.

Applicability: quasi-α implies A, and A fails (Theorem 3.3). quasi-β is range-side: the Euclidean plane
fails it (it has infinitely many extreme points, none isolated). **Inapplicable.**

### 4.8 Range-side counterexamples: Gowers (1990), Acosta (1999), Aguirre (1998), Fovelle (2024)

W. T. Gowers, *Symmetric block bases of sequences with large average growth*, Israel J. Math. 69 (1990)
129–151: ℓ_p (1 < p < ∞) fails B.
M. D. Acosta, *Denseness of norm attaining operators into strictly convex spaces*, Proc. Roy. Soc.
Edinburgh 129A (1999) 1107–1114: infinite-dimensional strictly convex spaces, and infinite-dimensional
L_1(μ), fail B.
F. J. Aguirre, *Norm-attaining operators into strictly convex Banach spaces*, J. Math. Anal. Appl. 222
(1998) 431–437.
A. Fovelle, *Norm attaining operators into locally asymptotically midpoint uniformly convex Banach
spaces*, arXiv:2402.19067 (2024): https://arxiv.org/abs/2402.19067. Locally AMUC Y with a normalized
symmetric basic sequence not equivalent to the ℓ_1 basis, or with upper p-estimates (p > 1), fail B.
(Source: search abstracts and memory.)

Common mechanism: the target operator is an isomorphic embedding of an infinite-dimensional domain (a
Gowers-type space, or c_0) into Y. NA operators near it must be non-compact. Strict or asymptotic
convexity of Y then forbids attainment, as in Theorem 3.3. **None of this works for finite-dimensional
range** (Remark 3.3.2). It gives no evidence either way for ℓ_2^2.

### 4.9 Martín (2014, 2016): compact operators

M. Martín, *Norm-attaining compact operators*, J. Funct. Anal. 267 (2014) 1585–1592, arXiv:1306.1155,
https://arxiv.org/abs/1306.1155.
M. Martín, *The version for compact operators of Lindenstrauss properties A and B*, RACSAM 110 (2016)
269–284, arXiv:1502.07084, https://arxiv.org/abs/1502.07084. (Source: search excerpts.)

Statements (CITED):
- Key lemma (2014): if X is a closed subspace of c_0 (sup norm) and Y is strictly convex, then
  NA(X, Y) ⊂ Fin(X, Y). Combined with Enflo-type failure of the AP, this gives compact operators not
  approximable by NA operators.
- Proposition: if Y is strictly convex without the AP, there are X and a compact T : X → Y not
  approximable by NA operators.
- (2016) X has property A^k whenever X* is isometrically isomorphic to ℓ_1. Y has B^k if Y has
  quasi-β, or is an isometric L_1-predual (Johnson–Wolfe).
- Open: whether every finite-dimensional Y has B^k. This is the same as B, since every operator into a
  finite-dimensional space is compact.

Mechanism of the key lemma: if T attains its norm at x ∈ S_X ⊂ c_0, then x ± δy ∈ B_X for all y in the
finite-codimensional subspace {y : y_j = 0 for |x_j| > 1/2}, ||y|| ≤ 1. Strict convexity of Y then
forces T to vanish there. This is the sup-norm version of Lemma 3.2.0.

For Martín's p, B_p is strictly convex (p** is), so no segments lie in S_p. Lemma 3.2.0 gives only
*asymptotic* flatness, which again forces only S e_n → 0 (Theorem 3.3). The AP plays no role for
finite rank. The ℓ_1-isometric-dual result is excluded by Prop. 3.6(d). **Inapplicable.** Martín 2014
nevertheless explains why compactness alone does not save density in general.

### 4.10 Bishop–Phelps–Bollobás property (BPBp) results

M. D. Acosta, R. M. Aron, D. García, M. Maestre, *The Bishop–Phelps–Bollobás theorem for operators*,
J. Funct. Anal. 254 (2008) 2780–2799: (X, Y) has BPBp if Y has β; and for finite-dimensional X and Y.
S. K. Kim, *The Bishop–Phelps–Bollobás theorem for operators from c_0 to uniformly convex spaces*,
Israel J. Math. 197 (2013) 425–435.
S. K. Kim, H. J. Lee, *Uniform convexity and Bishop–Phelps–Bollobás property*, Canad. J. Math. 66 (2014)
373–386: uniformly convex X gives (X, Y) BPBp for all Y.
R. M. Aron, Y. S. Choi, S. K. Kim, H. J. Lee, M. Martín, *The Bishop–Phelps–Bollobás version of
Lindenstrauss properties A and B*, Trans. AMS 367 (2015) 6085–6101, arXiv:1305.6420: universal BPB range
spaces have a universal η_Y; this property is strictly stronger than B; there is Y with B and (ℓ_1^2, Y)
failing BPBp.
S. Dantas, D. García, M. Maestre, M. Martín, *The Bishop–Phelps–Bollobás property for compact
operators*, Canad. J. Math. 70 (2018) 53–73, arXiv:1604.00618: BPBp-k transfers from (c_0, Y) to
(C_0(L), Y) and to (X, Y) whenever X* ≅ ℓ_1 isometrically.
(Source: search abstracts and memory.)

Applicability. Kim's c_0 argument uses the lattice/M-structure of the sup norm. Near an approximate
maximizer x it pushes the coordinates where |x_j| ≈ 1 to ±1 and uses the coordinate projections.
Martín's p has neither (Props. 3.1, 3.6). The DGMM transfer needs X* ≅ ℓ_1 isometrically, which fails.
Uniform convexity of X fails. **Inapplicable.**

The ACKLM result shows BPB-type *uniform* statements can fail even for 2-dimensional domains. So any
positive proof for Martín's space should be non-quantitative, i.e. not of BPB type uniformly over
operators.

### 4.11 Γ-flatness and ACK_ρ structure (Cascales–Guirao–Kadets–Soloviova 2018); generalized ACK

B. Cascales, A. J. Guirao, V. Kadets, M. Soloviova, *Γ-flatness and Bishop–Phelps–Bollobás type
theorems for operators*, J. Funct. Anal. 274 (2018) 863–888, arXiv:1704.01768,
https://arxiv.org/abs/1704.01768. A generalized ACK structure: arXiv:2204.01991.
(Source: search excerpts and memory.)

Statement (CITED, partially). T : X → Y is Γ-flat (Γ ⊂ B_{Y*} 1-norming) if T^*|_Γ : (Γ, w*) → (X*, ||·||)
is openly fragmented. Asplund operators, in particular finite-rank ones, are Γ-flat. If Y has ACK_ρ
structure, then Γ-flat operators into Y have the BPBp; in particular they lie in the closure of NA.
Uniform algebras and spaces with β have ACK_ρ structure.

Applicability: ACK_ρ is a **range** property. If ℓ_2^2 had ACK_ρ structure, every finite-rank operator
into ℓ_2^2 from every X would be approximable, settling property B for ℓ_2^2. ACK_ρ requires "peak-type"
operators F on Y with F^* acting almost as a projection onto a w*-small cap of Γ, compatible with an
ℓ_∞-type splitting. This is incompatible with the round geometry of ℓ_2^2: taking F = x_1^* ⊗ x_1, the
needed inequality |x^*(Fe)| + (1 − ε)||(I − F)^* x^*|| ≤ 1 fails for x^* = (cos θ, sin θ). This last
claim is HEURISTIC because I could not access the exact form of the ACK axioms. In any case it is
**inapplicable** without solving the main problem. Γ-flatness of the operator is automatic here.

### 4.12 Kadets–López–Martín–Werner, "Norm attaining operators of finite rank" (2020)

V. Kadets, G. López, M. Martín, D. Werner, in: *The Mathematical Legacy of Victor Lomonosov*,
De Gruyter 2020, Chapter 13, pp. 157–188; arXiv:1905.08272, https://arxiv.org/abs/1905.08272.
(Source: abstract and excerpts from the search engine, plus memory. I could **not** access the text, so
item numbers such as "Problem 13.12" cannot be verified. In the book version all items are numbered
13.x because the paper is Chapter 13.)

Statements (CITED; first four confirmed by excerpts):
1. A finite-rank T ∈ L(X, Y) belongs to NA(X, Y) whenever (ker T)^⊥ ⊂ NA(X) (= Lemma 2.2(a)).
2. If NA(X) contains a 2-dimensional subspace, then NA(X, ℓ_2^2) contains rank-two operators. More
   generally, if NA(X) contains a nontrivial cone, then for every Y with dim Y ≥ 2 there are rank-two
   NA operators X → Y.
3. If NA(X) contains a dense linear subspace, then NA finite-rank operators are dense in Fin(X, Y)
   (= Lemma 2.2(b)).
4. §4, Hilbert-space-valued case: NA(X, ℓ_2^2) contains a rank-two operator iff there are f ∈ NA(X) with
   ||f|| = 1 and g ∈ X* \ R f with ||f + tg||² ≤ 1 + t² for all t ∈ R (mates, up to scaling of g).
   The excerpt was truncated, but this agrees with Preprint B Props. quadratic-characterization and
   theta-dual. A "complete characterization" is claimed for Hilbert-space valued operators.
5. Open (stated there; confirmed by Martín's 2024 notes): is there X such that NA(X, ℓ_2^2) contains no
   rank-two operator? For Martín's X this is answered negatively by Preprint B (Theorem finite-short).
6. Second-order criteria. The quadratic-direction space 𝒬(f) and the condition
   Δ(f, g; t) = ||f + tg|| + ||f − tg|| − 2 = O(t²) appear there. Preprint B
   (Props. quadratic-directions, dgs-rank-k) extends them to rank k.

Applicability. Items 1–3 are excluded by (I2): no cones and no 2-dimensional subspaces. Item 4 is the
basic criterion behind (R1) and the mate formalism of Preprint A, and it is **the** tool everybody uses.
The density question is a *lower semicontinuity* problem for mate fibres (R3). KLMW give no density
theorem in the absence of linear structure in NA(X).

### 4.13 Read's space and the nonlineability programme

C. J. Read, *Banach spaces with no proximinal subspaces of codimension 2*, Israel J. Math. 223 (2018)
493–504.
M. Rmoutil, *Norm-attaining functionals need not contain 2-dimensional subspaces*, J. Funct. Anal. 272
(2017) 918–928.
V. Kadets, G. López, M. Martín, *Some geometric properties of Read's space*, J. Funct. Anal. 274 (2018)
889–899, arXiv:1704.00791.
V. Kadets, G. López, M. Martín, D. Werner, *Equivalent norms with an extremely nonlineable set of norm
attaining functionals*, J. Inst. Math. Jussieu 19 (2020) 259–279, arXiv:1709.01756. Every Banach space
containing c_0 and having a countable norming system admits an equivalent norm for which NA contains no
2-dimensional subspaces.
P. Bandyopadhyay, G. Godefroy, *Linear structures in the set of norm-attaining functionals on a Banach
space*, J. Convex Anal. 13 (2006) 489–497: the question answered by Read.
(Source: search abstracts and memory.)

For Read-type norms, NA contains nontrivial cones (KLMW excerpt; Martín 2025 excerpt). So KLMW item 2
gives rank-two NA operators. Preprint B proves NA ∩ Fin dense in K for Read's space and its smoothing
(lift lemma + coordinate projections, since s_N ≤ η_N q_N with η_N → 0).

Applicability: the Read mechanism uses that the "tail" seminorm s_N is *small* relative to a norm q_N
for which coordinate projections are contractive. In Martín's space the block seminorm ||L·|| is **not**
small relative to any norm with contractive projections (Prop. 3.1 excludes such norms in the relevant
sense). The block tail Σ_{m>N} is small (Remark martin-tail), but each finite block is not. Within a
block, a k-truncation is not seminorm-additive; see 7.2.

### 4.14 Martín (2025): the space itself

M. Martín, *A Banach space whose set of norm-attaining functionals is algebraically trivial*, J. Funct.
Anal. 288 (2025) 110815, arXiv:2406.07273, https://arxiv.org/abs/2406.07273.
(Source: search abstract and excerpts.)

Statements (CITED):
- NA(X) contains no nontrivial cone. If f, g ∈ NA are linearly independent, no other point of the
  segment [f, g] is NA. NA(X) ∩ E lies in two lines for every 2-dimensional E. In a quotient by a
  closed subspace of codimension two, at most four points of the unit sphere have norm-one
  representatives.
- "We further relate this example with an open problem on norm-attaining operators": no known result
  implies that NA(X, ℓ_2^2) contains rank-two operators. Martín's 2025 slides ("How small can be the set
  of norm-attaining ...", Cullera) say that "by now, X is the only possible counterexample".

Lemma A and Lemma B (as used in Preprint B):
- Lemma A: for positive Φ ∈ ℓ_1, the norm |·|_Φ with ball B_{ℓ_1} + D_Φ(B_{ℓ_2}) has the threshold
  property of Preprint B Lemma block-threshold.
- Lemma B: existence of T : ℓ_1(N × N) → Y, injective of norm one, such that every row
  (T e_{n,m}/||T e_{n,m}||)_n is dense in S_Y.

I could not retrieve the exact wording of either lemma. Preprint B's versions should be taken as
authoritative for this project.

Status of Martín's space after Preprint B: rank-k NA operators exist into every F (Theorem
finite-short). Density remains OPEN.

### 4.15 Residuality, ASE, RSE (2023–2026)

M. Jung, M. Martín, A. Rueda Zoca, *Residuality in the set of norm attaining operators between Banach
spaces*, J. Funct. Anal. 284 (2023) 109746, arXiv:2203.04023, https://arxiv.org/abs/2203.04023.
G. Choi, H. del Río, A. Fovelle, M. Jung, M. Martín, *Range strongly exposing operators between Banach
spaces*, arXiv:2503.18581 (2025), https://arxiv.org/abs/2503.18581.
*Bollobás-type theorems for range strongly exposing operators*, arXiv:2512.10442, RACSAM 2026,
https://arxiv.org/abs/2512.10442.
(Source: search abstracts and excerpts.)

Statements (CITED):
- JMRZ: ASE(X, Y) is a G_δ. It is dense if SE(X) is dense and Y (or Y*) satisfies RNP-type and
  discreteness conditions on strongly exposed points. Section 3.2 has an immediate corollary for
  finite-dimensional ranges; the exact hypotheses were not retrievable. Conversely, ASE(X, Y) dense
  implies SE(X) dense. For X and Y* separable, NA(X, Y) residual implies ASE(X, Y) dense.
- RSE paper: RSE operators are those T with a point x_0 such that every maximizing sequence has a
  subsequence whose images converge to a unimodular multiple of Tx_0. They sit between ASE and NA.
  - Cor. 2.15: if T ∈ Fin ∩ NA and X/ker T is strictly convex, then T ∈ cl(Fin ∩ RSE).
  - Finite-rank operators on spaces with "sufficiently many" subspaces inside NA(X) are approximable
    by RSE operators.
  - RSE versions of Johnson–Wolfe for compact and Γ-flat operators are given.
  - For every infinite-dimensional Y there is X with RSE(X, Y) not dense.
  - The paper restates that property B for finite-dimensional spaces is open even for ℓ_2^2.

Applicability:
- ASE route closed (Cor. 3.4).
- "Sufficiently many subspaces in NA" excluded by (I2).
- Cor. 2.15 (if as quoted) is relevant in a weak sense. Once one has an NA finite-rank operator, it can
  be upgraded to RSE when X/ker T is strictly convex. For T : X → ℓ_2^2 of rank two, X/ker T is
  2-dimensional with the quotient norm p̂. Is p̂ strictly convex? The dual of X/ker T is
  span{f, g} ⊂ X* with p*. Strict convexity of p̂ is equivalent to smoothness of p* restricted to
  span{f, g}, which is not guaranteed. In any case this is an upgrade tool, not a density tool.

### 4.16 Weak maximizing property, compact perturbation property

R. M. Aron, D. García, D. Pellegrino, E. V. Teixeira, *Reflexivity and nonweakly null maximizing
sequences*, Proc. AMS 148 (2020) 741–750.
M. Han, S. K. Kim, *M-ideals of compact operators and norm attaining operators*, arXiv:2402.12070
(2024), https://arxiv.org/abs/2402.12070: relations between K(X, Y) being an M-ideal, the weak
maximizing property (WMP) and the (adjoint) compact perturbation property.

**Proposition 4.16.1 (irrelevance for finite-dimensional range). PROVED.** Let F ≠ 0 be
finite-dimensional. If (X, F) has the WMP (every T with a non-weakly-null maximizing sequence attains
its norm), then NA(X, F) = L(X, F), and X is reflexive.

*Proof.* Let T ≠ 0 and let (x_n) ⊂ B_X with ||Tx_n|| → ||T||. If (x_n) were weakly null, then
Tx_n → 0, since T is compact (finite rank) and compact operators map weakly null sequences to norm-null
ones. So (x_n) is not weakly null and T attains its norm. Taking F ⊃ R·y and T = f ⊗ y shows that every
f ∈ X* attains its norm, so X is reflexive by James' theorem. ∎

The same argument (with T = 0 plus a compact perturbation) shows that any "compact perturbation
property" requiring T + K ∈ NA whenever ||T + K|| > ||T|| forces NA(X, F) = L(X, F) for
finite-dimensional F. Since Martín's X is non-reflexive, these properties fail and **cannot** be used.

### 4.17 Debs–Godefroy–Saint Raymond (1995)

G. Debs, G. Godefroy, J. Saint Raymond, *Topological properties of the set of norm-attaining linear
functionals*, Canad. J. Math. 47 (1995) 318–329. (Source: memory; search excerpts on related results.)

Statements: for X separable non-reflexive, NA(X) is not a w*-G_δ. The smoothing B_p = B_q + U(B_G)
with U compact and dense range gives p smooth with NA(p) = NA(q). This is used in [KLM 2018] and
Preprint B Lemma smoothing, and it is the origin of the "canonical base" q. **Applicable as a
construction tool**; it gives the base q and the smoothness of p (3.8.1).

### 4.18 Preprints A and B (in-house)

- **Preprint B (Han–Martín–Rodríguez-Vidanes).** Lift lemma, permanence theorem, projections lemma,
  dense-subspace lemma; primal transfer theorem (density preserved under B_p = B_q + U(B_G), G Hilbert);
  quadratic criteria for rank k; finite-block norms p_J (two-lines property and strict convexity of
  p_J**); the base-lift gap (one-step lifts are not dense); Remark martin-tail (reduction to p_N);
  Problem (density for p_N).
  My checks: the lift lemma, permanence estimate, recentering and near-ball lemmas are **correct**
  (proofs in Part 6).
- **Preprint A.** Global compactness and upper semicontinuity of C(f); residual Hausdorff continuity
  of C_d on a dense G_δ Ω; weighted directions; no bounded lift; lift blow-up.
  It relies on the unavailable [Check, Thm. 3.1] (finite local-certificate theorem) — **flagged as an
  imported black box**; I did not re-prove it.
  The global compactness proof is the same mechanism as Prop. 3.10 here. I re-derived its key step and
  found it correct: the ℓ_1-asymptotic additivity plus compactness of U and of the block part.

### 4.19 Other items checked and found irrelevant

- Dantas–Falcó–Jung–Rodríguez-Vidanes, *Linear structures in the set of non-norm-attaining operators*,
  arXiv:2311.17426: spaceability of L(c_0(Γ), Y) \ NA for strictly convex renormings Y. Infinite-
  dimensional ranges only.
- "Norm-attaining tensors and nuclear operators", arXiv:2006.09871: Read's space in tensor products.
  Not about finite-dimensional ranges.
- Group-invariant techniques, arXiv:2110.02066: not relevant.
- Kalton–Werner property (M) / (m_∞), J. reine angew. Math. 461 (1995).
  **Claim (PROVED): (c_0, p) fails (m_∞)** whenever Lx ≠ 0 for some x, i.e. always.
  First, lim_n q(x + c e_n) = max(q(x), c) for c > 0.
  - Lower bound: q(x + ce_n) ≥ e_n^*(x + c e_n)/q*(e_n^*) → c (since q*(e_n^*) → 1), and
    q(x + ce_n) ≥ a_x(x + c e_n) → q(x), where a_x = ∇q(x) ∈ ℓ_1.
  - Upper bound: write x = q(x)(z + Uh) with z ∈ c_0, ||z||_∞ ≤ 1, ||h|| ≤ 1. Let M = max(q(x), c). Then
    x + ce_n = M( (q(x)/M) z + (c/M) e_n + U((q(x)/M)h) ), and
    ||(q(x)/M) z + (c/M)e_n||_∞ ≤ max(1, (q(x)/M)|z_n| + c/M) ≤ 1 + |z_n| → 1.
  Next, p(c e_n) → c, since q(e_n) → 1 and ||Le_n|| → 0. With c = p(x):
  p(x + c e_n) → max(q(x), p(x)) + ||Lx|| = p(x) + ||Lx||, which is > max(p(x), lim p(ce_n)) = p(x)
  when Lx ≠ 0. Not needed elsewhere.

### 4.20 Summary table

| Technique / theorem | Hypothesis needed | Status for X = (c_0,p) | Reason |
|---|---|---|---|
| Reflexive / RNP / Bourgain | X RNP | fails | X ≅ c_0 |
| Lindenstrauss uniformly str. exposed | B_X = cl aco(USE set) | fails | no str. exposed pts (3.2) |
| Schachermayer α | α | fails | 3.2, 3.3 |
| Choi–Song quasi-α | quasi-α | fails | ⇒ A, but A fails (3.3) |
| Strong Bishop–Phelps property (arXiv:2304.12611) | implies A | fails | 3.3 |
| Johnson–Wolfe C(K) | X = C(K) | fails | 3.6(d) |
| Martín A^k, DGMM BPB-k | X* ≅ ℓ_1 isometric | fails | 3.6(d) |
| Norm-one fin.-rank projections (π_1, metric AP via projections) | P(B_X) compact | fails | 3.1 |
| M-ideal / M-embedded | X M-ideal in X** | fails | 3.7 |
| L/M-summand decompositions | nontrivial summands | fail | 3.6 |
| Dense subspace in NA (KLMW) | D ⊂ NA dense lin. | fails | (I2) |
| Cones in NA (KLMW) | nontrivial cone | fails | (I2), Martín 2025 |
| ASE density (Bourgain/JMRZ) | SE(X) dense | fails | SE(X)=∅ (3.4) |
| RSE "many subspaces" | subspaces in NA | fails | (I2) |
| WMP / CPP | — | void | 4.16.1 |
| β, quasi-β, ACK_ρ, AHSP | range-side | not known for ℓ_2^2 | would settle B for ℓ_2^2 |
| Lift + permanence (Read) | s ≤ η q_η, η→0 | only for block tail | blocks not small (4.13) |
| Primal transfer (Preprint B) | Hilbert ball enlargement | applies to q only | p is a *norm sum* |
| Fréchet smoothness (3.8) | — | HOLDS | new tool |
| Residual recovery (Preprint A) | — | HOLDS on Ω | not all f |

---------------------------------------------------------------------------------------------------------

## 5. What the counterexample side of the literature says (and does not say)

5.1. Every known operator not approximable by NA operators is either non-compact (Lindenstrauss, Gowers,
Acosta, Aguirre, Fovelle) or compact into a space without the AP (Martín 2014). For finite-dimensional
range neither ingredient exists. **No known mechanism produces a finite-rank counterexample.** A
counterexample for Martín's space would need an essentially new mechanism, which supports the
briefing's skepticism.

5.2. Martín's space was designed so that NA(X) has *no linear structure*, the obstruction to KLMW's
positive results. Preprint B already shows that rank-k NA operators exist (lifting through the base),
so the "no rank-two NA operator" route to a counterexample is dead. What remains is the *density*
question, which is a semicontinuity question for mate fibres (R3).

5.3. HEURISTIC. Theorem 3.3 shows that the c_0-flat directions of p kill NA operators with
inf ||S e_n|| > 0. For finite rank, the flat directions instead give the *one-sided first-order freedom*
used in (R4) ("far coordinates of z' are free"). This is a mechanism for *positive* results: it lets one
place the far part of the block support pattern of an NA approximant as one likes.

---------------------------------------------------------------------------------------------------------

## 6. Tools for a positive proof: statements and proofs

### 6.1 Lift lemma (Preprint B Lemma lift). PROVED (re-proof).

Let p = q + s, s a q-continuous seminorm. Let S ∈ L((X, q), F) \ {0} attain its norm at z_0 ∈ S_q, and
let h ∈ X* with |h| ≤ s and h(z_0) = s(z_0). Then A := S + h ⊗ S z_0 attains its p-norm at
z_0/p(z_0), and ||A||_p = ||S||_q.

*Proof.* ||Az|| ≤ ||Sz|| + |h(z)| ||Sz_0|| ≤ ||S||_q q(z) + s(z) ||S||_q = ||S||_q p(z). Also
Az_0 = (1 + s(z_0)) S z_0, so ||Az_0|| = ||S||_q (q(z_0) + s(z_0)) = ||S||_q p(z_0). ∎

Remark (uniqueness of the lift for strictly convex F). Look for A = S + h ⊗ v with ||v|| ≤ ||S|| and
equality at z_0. We need ||Sz_0 + s(z_0) v|| = ||Sz_0|| + s(z_0)||v||. For strictly convex F this forces
v to be a nonnegative multiple of Sz_0, and then ||v|| = ||S|| gives v = Sz_0 (when q(z_0) = 1). So in
ℓ_2^2 one-step lifts are rigid. The base-lift gap of Preprint B shows they are not dense.

### 6.2 Permanence (Preprint B Thm. permanence). PROVED (re-proof).

If p = q_η + s_η with s_η a seminorm, s_η ≤ η q_η, then for every T,
d_p(T) ≤ η(1 + η)||T||_p + (1 + η) d_{q_η}(T).

*Proof.* Take S ∈ NA((X, q_η), F) with ||T − S||_{q_η} ≤ d_{q_η}(T) + ε, and lift it to A as in 6.1.
||A − S||_{q_η} ≤ ||h|| ||S||_{q_η} ≤ η ||S||_{q_η}, since |h| ≤ s_η ≤ η q_η. Also
||·||_p ≤ ||·||_{q_η} (because p ≥ q_η) and ||S||_{q_η} ≤ ||T||_{q_η} + d + ε ≤ (1 + η)||T||_p + d + ε.
So ||T − A||_p ≤ ||T − S||_{q_η} + ||S − A||_{q_η} ≤ d + ε + η((1 + η)||T||_p + d + ε). The stated
estimate follows. ∎

For Martín: q_η = p_N, s_η = Σ_{m>N} |R_m ·|_m ≤ η_N q (Remark martin-tail). So density for p follows
from density for p_N along N → ∞. This is the only "smallness" available.

### 6.3 Recentering lemma (Preprint B Lemma recenter). PROVED (new short proof).

Let S ∈ L(Z, E), z_0 ∈ B_Z, a ∈ S_E, ξ ∈ S_{E*} with ξ(a) = 1, and λ > 0. Assume
S(B_Z) ⊂ Sz_0 + λ(B_E − a) and ξ(Sz_0) > 0. Then A = S + (S^*ξ/ξ(Sz_0)) ⊗ (λa − Sz_0) satisfies
||A|| = λ = ||Az_0||.

*Proof.* Az_0 = λa. Fix z ∈ B_Z. Apply the containment to z and to −z: Sz = Sz_0 + λ(b − a) and
−Sz = Sz_0 + λ(b′ − a) with b, b′ ∈ B_E. Adding: Sz_0 = λa − λ(b + b′)/2, i.e.
λa − Sz_0 = λ(b + b′)/2. Subtracting: Sz = λ(b − b′)/2. Put c = ξ(Sz)/ξ(Sz_0). From the containment,
ξ(Sz) = ξ(Sz_0) + λ(ξ(b) − 1) ≤ ξ(Sz_0), and likewise −ξ(Sz) ≤ ξ(Sz_0). So |c| ≤ 1. Then

  Az = Sz + c(λa − Sz_0) = λ[ ((1 + c)/2) b − ((1 − c)/2) b′ ],

a convex combination of λb and −λb′. Hence ||Az|| ≤ λ. ∎

**6.3.1 Near-ball lemma (Preprint B). PROVED.** G Hilbert, L ∈ L(G), φ ∈ S_G, L^*φ ≠ 0,
ψ = L^*φ/||L^*φ||, λ ≥ ||L||²/||L^*φ||. Then L(B_G) ⊂ Lψ + λ(B_G − φ).
*Proof.* For h ∈ B_G:
||L(h − ψ) + λφ||² − λ² = ||L(h − ψ)||² + 2λ||L^*φ||(⟨h, ψ⟩ − 1)
≤ ||L||² · 2(1 − ⟨h, ψ⟩) − 2λ||L^*φ||(1 − ⟨h, ψ⟩) ≤ 0,
using ||h − ψ||² ≤ 2(1 − ⟨h, ψ⟩). ∎

**6.3.2 Correction size.** In 6.3, ||A − S|| ≤ ||S^*ξ|| ||λa − Sz_0|| / ξ(Sz_0). So the recentering gives
a *close* NA operator exactly when Sz_0 is close to λa, i.e. when the ball of radius λ containing S(B_Z)
is almost tangent at the point Sz_0.

**6.3.3 Interpretation for F = ℓ_2^2 (mate inequality in ball form). PROVED.** Let E = ℓ_2^2,
a = ξ = e_1, and T = (f, g) : X → ℓ_2^2. Then T(B_X) ⊂ Tz_0 + λ(B − e_1) iff for all x ∈ B_X

  (f(x) − f(z_0) + λ)² + (g(x) − g(z_0))² ≤ λ².

For λ = 1, f(z_0) = 1 and g(z_0) = 0, this reads (f(x) − 1 + 1)² + g(x)² ≤ 1, i.e. f(x)² + g(x)² ≤ 1
for all x ∈ B_X. That is ||(f, g)|| ≤ 1. Together with ||T z_0|| = 1, this is the statement that T
attains its norm at z_0, and the correction in 6.3 vanishes (λa = Tz_0). So the recentering lemma with a
Hilbert range at λ = 1 is the KLMW mate criterion. The general λ version allows "osculating discs"
of radius λ ≥ 1. This is the mechanism by which the primal transfer theorem converts NA operators for q
(into the auxiliary norm p_D) into NA operators for p.

**Possible use (HEURISTIC).** For Martín's p, choose S close to T and z_0 ∈ X such that S(B_X) is
contained in a disc of radius λ (possibly λ ≫ 1) tangent near Sz_0. This needs only a *one-sided
quadratic upper bound* for the curvature of S(B_X) at Sz_0. That is a weaker requirement than f ∈ NA
plus g ∈ C(f) with the same λ, because λ is free. The constraint ξ(Sz_0) > 0 is harmless. The price is
||A − S|| ≈ ||S^*ξ|| ||λa − Sz_0||/ξ(Sz_0): one needs λa − Sz_0 small, i.e. Sz_0 within o(1) of the
tangency point of a disc of radius λ. For λ large the disc is nearly a half-plane, and the containment
says ξ∘S almost attains at z_0 with a quadratic margin of order λ^{-1}. This is a quantitative
"almost-mate" condition, and it suggests a reformulation of (R3) in which the radius λ_n → ∞ is allowed
along the approximating sequence. NOT developed here.

### 6.4 Primal transfer theorem (Preprint B). CITED (proof sketch in Preprint B; I checked its two
lemmas, 6.3 and 6.3.1).

If NA((X, q), F) is dense for every finite-dimensional F, then the same holds for p with
B_p = B_q + U(B_G), U compact with dense range, G Hilbert. For c_0 with the sup norm, density holds (by
Lemma 2.4 with coordinate projections). So the canonical base (c_0, q) has density for all
finite-dimensional F.

### 6.5 Fréchet smoothness and continuity tools (Part 3). PROVED.

Theorem 3.8 (∇p norm-continuous; NA ∩ S = w*-strongly exposed points), Prop. 3.9 (forced decomposition
continuous), Prop. 3.10 (asymptotic dual norm).

### 6.6 NA approximation of a given f: what is automatic and what is not

**6.6.0 (BPB + smoothness). PROVED.** For f ∈ S_{p*} and ε > 0, every x ∈ S_p with f(x) > 1 − ε²/2
can be moved by less than ε to some x′ ∈ S_p with ||f − ∇p(x′)|| < ε. This is Lemma 2.5 combined with
uniqueness of the supporting functional (3.8.1).

**6.6.1 (weak*-convergence of the normers alone is not enough). FALSE as a general principle; the
counterexample is a SKETCH.** One might hope that x_n ∈ S_p and x_n → ξ weak* (ξ the normer of f) imply
∇p(x_n) → f. What is true is the following.
- Write ∇p(x_n) = a_n + L^*w_n with a_n = ∇q(x_n) and w_n = J_V(Lx_n). By compactness of L,
  Lx_n → L**ξ in norm, and by smoothness of ||·||_V at L**ξ (all block components nonzero),
  L^*w_n → L^*w in norm. So **the block part is automatic.**
- Also q(x_n) = 1 − ||Lx_n|| → 1 − ||L**ξ|| = q**(ξ) = q_0.
- The base part a_n = ∇q(x_n) need **not** converge to a in norm. Sketch: let ξ/q_0 = z + U h_a with
  supp a infinite. Choose x_n whose q-contact equals z on [1, n] and has an extra coordinate N_n → ∞ with
  contact value 1. Choose h_n proportional to U^*(a^{(n)} + β e_{N_n}^*) with β > 0 fixed, where
  a^{(n)} is the restriction of a to [1, n]. Then ∇q(x_n) is proportional to a^{(n)} + β e_{N_n}^*,
  which keeps ℓ_1-mass ≈ β/(1 + β) escaping to infinity. Meanwhile x_n → ξ weak* (up to
  normalization), because U^*e_{N_n}^* → 0 and the coordinates converge. Hence ∇p(x_n) does not
  converge to f in norm. (The normalization bookkeeping is not written out; hence SKETCH.)

**6.6.2 Proposition (controlled NA approximation). PROVED (mod. (I3)).** Let f ∈ S_{p*} have forced
decomposition (a, w) and normer ξ. Let x_n ∈ S_p with x_n → ξ weak*, and assume
∇q(x_n) → a in ℓ_1-norm. Then ∇p(x_n) → f in norm.
*Proof.* By the sum rule (3.8.1), ∇p(x_n) = ∇q(x_n) + L^*J_V(Lx_n). The block part converges to L^*w
by the first bullet of 6.6.1, and the base part converges to a by hypothesis. ∎

**6.6.3 Proposition (complete description of NA(p); briefing (R4)). PROVED.**
(i) For every a′ ∈ c_00 with q*(a′) = 1 and every z′ ∈ c_0 with ||z′||_∞ ≤ 1 and z′_j = sign a′_j on
    supp a′, the vector y′ = z′ + U(U^*a′/||U^*a′||) satisfies q(y′) = 1 and ∇q(y′) = a′.
(ii) Consequently ∇p(y′) = a′ + L^*J_V(Ly′) ∈ NA(p) ∩ S_{p*}.
(iii) Conversely, every element of NA(p) ∩ S_{p*} arises in this way: it equals ∇p(x′) for some
     x′ ∈ S_p, and y′ = x′/q(x′) has this form with a′ = ∇q(x′) ∈ c_00.

*Proof.* (i) a′(y′) = Σ_j |a′_j| + ||U^*a′|| = q*(a′) = 1, and y′ ∈ B_{c_0} + U(B_H) = B_q, so
q(y′) ≤ 1 ≤ a′(y′)/q*(a′) ≤ q(y′). Hence q(y′) = 1 and a′ norms y′; by smoothness of q, ∇q(y′) = a′.
(ii) This is the sum rule for ∇p = ∇q + L^*∇||·||_V∘L, and the gradient of a norm has dual norm 1.
(iii) If f′ = ∇p(x′), the sum rule gives f′ = ∇q(x′) + L^*J_V(Lx′). ∇q(x′) ∈ NA(q) ∩ S_{q*}, and
NA(q) = NA(c_0) = c_00 by the DGS lemma (I4). Write y′ = x′/q(x′) = z′ + U h′ with ||z′||_∞ ≤ 1 and
||h′|| ≤ 1. Then 1 = a′(y′) = a′(z′) + ⟨U^*a′, h′⟩ ≤ ||a′||_1 + ||U^*a′|| = 1, which forces
z′_j = sign a′_j on supp a′ and h′ = U^*a′/||U^*a′||. Also z′ ∈ c_0, since y′ ∈ c_0 and Uh′ ∈ c_0. ∎

So, to approximate f by NA functionals in the controlled way of 6.6.2, it suffices to take
a′ = a^{(n)}/q*(a^{(n)}) for finite truncations a^{(n)} of a (so a′ → a in norm), and z′_n ∈ c_0
with z′_n = sign a on supp a^{(n)}, |z′_n| ≤ 1, z′_n → z coordinatewise. One also needs
y′_n/p(y′_n) → ξ weak*. This holds if z′_n → z coordinatewise and the normalizations converge, since
U h′_n → U h_a in norm. Then 6.6.2 gives ∇p(y′_n) → f. **The coordinates of z′_n outside a finite
window are completely free** (any values of modulus < 1 converging to z coordinatewise). This is the
freedom recorded in (R4). PROVED, except for the routine normalization check
p(y′_n) → p**(ξ/q_0) = 1/q_0. That check holds because q(y′_n) = 1 and ||Ly′_n|| → ||L**(ξ/q_0)|| by
compactness of L.

### 6.7 Kuratowski/Blaschke reduction (briefing (R3)). SKETCH-checked.

I checked the logic of (R3):
- the fibres C(f_n) lie in a common norm-compact set by Preprint A's global compactness;
- the Kuratowski lower limit of compact convex sets is compact and convex;
- support-function inequalities on a dense set of x ∈ c_0, with equi-Lipschitz support functions
  (r̃_f ≤ p), give ρC(f) ⊂ Li_n C(f_n) by Hahn–Banach separation inside ℓ_1. Separation by c_0-vectors
  is legitimate because the sets are norm-compact, and for norm-compact convex sets in ℓ_1 = c_0^* the
  w* and norm topologies agree on them, so w*-separation by x ∈ c_0 suffices.

The diagonal argument for finitely many x_i is standard. I have no objection. Status: SKETCH (correct in
outline).

---------------------------------------------------------------------------------------------------------

## 7. Attempts that fail, with reasons

### 7.1 Johnson–Wolfe factorization through finite-dimensional polyhedral pieces. FALSE for Martín.

Any approximant TP with P(B_X) compact has rank ≤ 1 (Prop. 3.1).

### 7.2 Within-block truncation + permanence. FAILS.

Idea: write p = q_K + s_K, where q_K keeps only the first K coordinates of each block. The candidate
q_K(x) = q(x) + Σ_m |P_K R_m x|_m makes s_K = p − q_K a difference of norms, which is not a seminorm in
general. The ball B_{|·|_m} = B_{ℓ_1} + D_m(B_{ℓ_2}) does not split as an ℓ_1-sum over coordinate
blocks: its dual norm ||w||_∞ + ||Dw||_2 is not additive over coordinate splittings. The alternative
p̃_K := q_K + Σ_m ||(I − P_K) R_m ·||_1 *is* of the form "norm + small seminorm". But p ≤ p̃_K ≤ (1 + 2η)p
with p̃_K ≠ p, and density of NA is not known to be stable under (1 + η)-equivalent renormings of the
domain. (For finite-dimensional F that stability is itself an open problem of the same kind.)

### 7.3 Strong exposure / Bourgain / Stegall in the primal. FAILS.

No strongly exposed points (Prop. 3.2).

### 7.4 M-ideal / L-embedded decompositions of X* (à la Kalton–Werner, HWW, Han–Kim). FAILS.

Prop. 3.7: the compact block term destroys the L-decomposition of the dual.

### 7.5 Dual Stegall (Asplund) variational principle. FAILS as a direct tool.

X is Asplund (X* = ℓ_1 separable) and p is even Fréchet smooth. So for any w*-compact convex
K ⊂ X* the set of x ∈ X strongly exposing K is a dense G_δ. Apply this to
K_T := T^*(B_{F*}) ⊂ X* for T : X → F. Then x ∈ X strongly exposes K_T at T^*φ_x. But T ∈ NA needs some
maximizer φ of p*(T^*φ) with T^*φ ∈ NA(X). The variational principle controls which point of K_T is
exposed by a given x. It does not make the p*-maximal point of K_T an NA functional, and the two
optimizations (linear functional x on K_T, versus the norm p* on K_T) are unrelated. No reduction found.

### 7.6 Lindenstrauss iteration. HEURISTIC only.

Lindenstrauss' proof of density of {T : T** ∈ NA} builds T_∞ = T + Σ ε_k φ_k ⊗ y_k with T_∞** attaining
at a w*-cluster point ξ ∈ X**. For finite rank this is automatic, so the content lies in forcing ξ ∈ X.
For Martín's p, one could try to run the iteration with the perturbing functionals φ_k chosen among the
c_0-flat directions (far coordinates) and with the c_00-supported base functionals of (R4), so as to
keep the maximizer's normer in X. The obstacle: the normer of the limit maximizer is the w*-limit of
normers, and strict convexity of p** makes it unique. One needs norm convergence of the normers, which
Prop. 3.2 shows can fail at every point. Not a proof.

### 7.7 Range-side approximation of ℓ_2^2 by polygons. FAILS.

Polygonal norms |·|_k → ||·||_2 have β, so NA(X, (R², |·|_k)) is dense. But an operator attaining its
|·|_k-norm need not attain its ||·||_2-norm. Property B is not stable under small isomorphisms of the
range, as far as is known (otherwise ℓ_2^2 would have B).

---------------------------------------------------------------------------------------------------------

## 8. Open questions and recommended directions

- (Q1) OPEN. Is NA((c_0, p_N), ℓ_2^2) dense for every N? This is Preprint B Problem blocks.
- (Q2) OPEN. Does the recentering lemma with free radius λ (6.3.3) reduce density to an "almost-mate"
  condition that is easier to verify than exact mates? Formulate: for f ∈ S_{p*}, g ∈ C(f), ρ < 1,
  ε > 0, find x′ ∈ S_p and λ ∈ [1, ∞) with
  (i) ||∇p(x′) − f|| < ε;
  (ii) the operator (∇p(x′), ρg + small) maps B_p into a disc of radius λ tangent at e_1-direction with
       tangency defect o(1/λ).
  Then 6.3 gives an NA operator within O(ε) of (f, ρg).
- (Q3) OPEN. Is p** strictly convex and is p Fréchet smooth for Martín's *original* base (not the
  canonical one)? Here Fréchet smoothness was proved for the canonical base.
- (Q4) Literature: JW "Question 6" numbering, KLMW "Problem 13.12" wording, and the exact JMRZ
  finite-dimensional corollary are unverified (no access).

---------------------------------------------------------------------------------------------------------

## 9. References (with URLs where available)

- [AAGM08] Acosta, Aron, García, Maestre, J. Funct. Anal. 254 (2008) 2780–2799.
- [Acosta99] Acosta, Proc. Roy. Soc. Edinburgh 129A (1999) 1107–1114.
- [AAP96] Acosta, Aguirre, Payá, Rocky Mountain J. Math. 26 (1996) 407–418.
- [ACKLM15] Aron, Choi, Kim, Lee, Martín, Trans. AMS 367 (2015) 6085–6101, https://arxiv.org/abs/1305.6420
- [AGPT20] Aron, García, Pellegrino, Teixeira, Proc. AMS 148 (2020) 741–750.
- [BG06] Bandyopadhyay, Godefroy, J. Convex Anal. 13 (2006) 489–497.
- [Bou77] Bourgain, Israel J. Math. 28 (1977) 265–271.
- [CGKS18] Cascales, Guirao, Kadets, Soloviova, J. Funct. Anal. 274 (2018) 863–888, https://arxiv.org/abs/1704.01768
- [CdRFJM25] Choi, del Río, Fovelle, Jung, Martín, https://arxiv.org/abs/2503.18581
- [CS08] Choi, Song, Math. Nachr. 281 (2008) 1264–1272.
- [DGMM18] Dantas, García, Maestre, Martín, Canad. J. Math. 70 (2018) 53–73, https://arxiv.org/abs/1604.00618
- [DGS95] Debs, Godefroy, Saint Raymond, Canad. J. Math. 47 (1995) 318–329.
- [DGZ93] Deville, Godefroy, Zizler, Smoothness and Renormings in Banach Spaces, Longman 1993.
- [Fov24] Fovelle, https://arxiv.org/abs/2402.19067
- [GMRV26] García, Maestre, Rodríguez-Vidanes, On a problem of Johnson and Wolfe, https://arxiv.org/abs/2605.28466
- [Gow90] Gowers, Israel J. Math. 69 (1990) 129–151.
- [HK24] Han, Kim, https://arxiv.org/abs/2402.12070
- [HWW93] Harmand, Werner, Werner, M-ideals in Banach Spaces and Banach Algebras, LNM 1547.
- [JW79] Johnson, Wolfe, Studia Math. 65 (1979) 7–19, https://eudml.org/doc/218261
- [JMRZ23] Jung, Martín, Rueda Zoca, J. Funct. Anal. 284 (2023) 109746, https://arxiv.org/abs/2203.04023
- [KLM18] Kadets, López, Martín, J. Funct. Anal. 274 (2018) 889–899, https://arxiv.org/abs/1704.00791
- [KLMW20a] Kadets, López, Martín, Werner, J. Inst. Math. Jussieu 19 (2020), https://arxiv.org/abs/1709.01756
- [KLMW20b] Kadets, López, Martín, Werner, Norm attaining operators of finite rank, https://arxiv.org/abs/1905.08272
- [Kim13] S. K. Kim, Israel J. Math. 197 (2013) 425–435.
- [KL14] Kim, Lee, Canad. J. Math. 66 (2014) 373–386.
- [Lin63] Lindenstrauss, Israel J. Math. 1 (1963) 139–148.
- [Mar14] Martín, J. Funct. Anal. 267 (2014) 1585–1592, https://arxiv.org/abs/1306.1155
- [Mar16] Martín, RACSAM 110 (2016) 269–284, https://arxiv.org/abs/1502.07084
- [Mar25] Martín, J. Funct. Anal. 288 (2025) 110815, https://arxiv.org/abs/2406.07273
- [Par82] Partington, Israel J. Math. 43 (1982) 273–276.
- [Read18] Read, Israel J. Math. 223 (2018) 493–504.
- [Rm17] Rmoutil, J. Funct. Anal. 272 (2017) 918–928.
- [Sch83a] Schachermayer, Israel J. Math. 44 (1983) 201–212.
- [Sch83b] Schachermayer, Pacific J. Math. 105 (1983) 427–438.
- [Uhl76] Uhl, Pacific J. Math. 63 (1976) 293–300.
- Preprint A, Preprint B: `ctx/residual_recovery.tex`, `ctx/hmr_c0_renormings.tex`.
