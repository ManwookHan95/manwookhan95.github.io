# Research briefing: the density problem for Martín norms

Goal (from the user, a Banach-space theorist): **settle** whether NA((c_0,p),ℓ_2^2) is norm dense in
L((c_0,p),ℓ_2^2) for Martín's norm p (canonical base). Either a complete rigorous proof of density
(possibly for all finite-dimensional ranges), or a rigorous counterexample. A counterexample would make
ℓ_2^2 fail Lindenstrauss property B (Johnson–Wolfe Question 6, open since the 1970s) — extraordinary,
so be extremely skeptical of any counterexample claim. Partial results must be stated honestly.

Context files (read them first):
- `ctx/residual_recovery.tex` — user's latest note (Preprint A). Notation C(f), Γ(f,g), forced decomposition,
  global compactness, residual recovery, weighted directions, no-bounded-lift, lift blow-up.
- `ctx/hmr_c0_renormings.tex` — Han–Martín–Rodríguez-Vidanes preprint (Preprint B). Lift lemma, permanence,
  primal transfer theorem (compact Hilbert enlargement of the primal ball), quadratic criteria, finite blocks,
  Remark martin-tail (reduction to finite-block norms p_N), Problem (density for p_N).
- Martín's paper: arXiv:2406.07273 (Lemma A, Lemma B, Steps 1–8). KLMW: arXiv:1905.08272 (mates, Section 13).
  Fetch with WebFetch if you need exact statements.
- The companion notes [Recovery] and [Check] cited in Preprint A are NOT available. The only thing used from
  [Check] is the "finite local-certificate theorem" (Preprint A, Section 1): if (f, R_m^*(ω - d w_m)) is
  contractive, ω finitely supported strictly below the peak of w_m, d = <D w_m, D ω>/||D w_m||, and the
  block quadratic coefficient is ≤ 1, then the operator is in the closure of NA. If you rely on it, either
  re-prove it or flag it as an imported black box.

## Setting (canonical base, finite or infinite block set I)
X = c_0, X* = ℓ_1, X** = ℓ_∞. q*(a) = ||a||_1 + ||U^*a||_H, B_q = B_{c_0} + U(B_H), U: H → c_0 compact,
dense range. NA(q) = c_00, and q is smooth, so ∇q(x) ∈ c_00 for every x ∈ c_0 \ {0}.
u_{k,m} = T e_{k,m}/q^*(T e_{k,m}) ∈ Y, Y ∩ c_00 = {0}, T: ℓ_1(N×N) → Y injective, norm one; every tail
of (u_{k,m})_k is norm dense in S_{q^*}. Φ_m(k) = 2^{-m-k} q^*(T e_{k,m}) (so Φ_m(k) ≤ 2^{-m-k}).
(R_m x)(k) = m Φ_m(k) u_{k,m}(x). V_m = (ℓ_1, |·|_m), B_{|·|_m} = B_{ℓ_1} + D_m(B_{ℓ_2}),
N_m(w) = |w|_m^* = ||w||_∞ + ||D_m w||_2. V = ℓ_1-sum over m ∈ I, L x = (R_m x)_m compact, injective.
p = q + ||L·||_V; B_{p*} = B_{q*} + L^*(B_{V*}); p** = q** + ||L**·||_V; p smooth; p** strictly convex.
Every f ∈ S_{p*}: unique normer ξ ∈ S_{p**}, forced decomposition f = a + L^*w, q*(a) = 1,
a(ξ) = q**(ξ) =: q_0, w = J_V(L**ξ), ||L**ξ|| = 1 - q_0. Base contact: ξ/q_0 = z + U(U^*a/||U^*a||),
z ∈ B_{ℓ_∞}, z_j = sign a_j on supp a. Block support structure (Lemma block-threshold):
R_m**ξ/|R_m**ξ|_m = α + D D^* w_m/C, α ∈ B_{ℓ_1} supported on the peak set P(w_m) = {k : |w_m(k)| = M}
with matching signs, M = ||w_m||_∞, C = ||D w_m||_2, M + C = 1; off P, w_m(k) = C (R_m**ξ)(k)/(Φ_m(k)^2 |R_m**ξ|).
By Remark martin-tail it suffices to treat finite I (p_N for arbitrarily large N), but a direct treatment of p
is also welcome.

## Reductions already worked out by the orchestrator (verify before relying on them)
(R1) Every norm-one T: X → ℓ_2^2 is, after a rotation of ℓ_2^2, of the form (f,g) with f ∈ S_{p*} and g ∈ C(f)
(T^* attains its norm on the finite-dimensional E^*). Density ⇔ for all f ∈ S_{p*}, g ∈ C(f), ρ ∈ (0,1):
(f, ρ g) ∈ closure of NA. (f, ρ g) has slack sqrt(1+t^2) - sqrt(1+ρ^2 t^2) for t ≠ 0.

(R2) Primal description of the fibre: C(f) = {g ∈ X* : |g| ≤ r_f on X}, r_f := sqrt(p^2 - f^2) ≥ 0.
Hence C(f) = dual ball of the seminorm r̃_f := largest seminorm ≤ r_f (convex envelope), and the support
function of C(f) at x ∈ X equals r̃_f(x) = inf{Σ_j r_f(y_j) : Σ_j y_j = x}.

(R3) Lower-limit/compactness reduction. Let f_n → f in S_{p*}. The Kuratowski lower limit Li_n C(f_n) is closed,
convex, symmetric. By the global compactness theorem (Preprint A, Thm 2.1) ∪_n C(f_n) is relatively compact,
so (Blaschke selection in the hyperspace of a compact metric space + support functions at x ∈ c_0 separating
compact convex subsets of ℓ_1): if liminf_n r̃_{f_n}(x) ≥ ρ r̃_f(x) for all x ∈ c_0, then ρ C(f) ⊂ Li_n C(f_n).
Since r̃ ≤ p (equi-Lipschitz), it suffices to check a countable dense set of x, and by diagonalization:
**Sufficient condition for density:** for every f ∈ S_{p*}, ρ < 1, ε > 0 and finitely many x_1,…,x_k ∈ c_0 there is
f' ∈ NA ∩ S_{p*} with ||f' - f|| < ε and r̃_{f'}(x_i) ≥ ρ r̃_f(x_i) - ε (i ≤ k).
Equivalently: finitely many mates g_1,…,g_k ∈ C(f) must be recovered (up to ρ, ε) along a COMMON first row f'.
Also "transitivity": the set 𝓡 = {f : {f}×C(f) ⊂ closure NA} contains NA ∩ S and the residual set Ω, and if
f_n ∈ 𝓡, f_n → f with liminf r̃_{f_n} ≥ ρ r̃_f for each ρ<1 (along suitable sequences), then f ∈ 𝓡.

(R4) NA ∩ S_{p*} = {∇p(x) : x ∈ c_0 \ {0}} = {a' + L^* J_V(L x') : a' ∈ c_00 ∩ S_{q*}, x' in the cone over the
face of a'}. Concretely: pick a' ∈ c_00 with q*(a') = 1 and z' ∈ c_0 with z' = sign a' on supp a', |z'| ≤ 1,
x' = c (z' + U(U^*a'/||U^*a'||)) normalized; then ∇p(x') = a' + L^*J_V(L x'). NA approximants of f are obtained
from a' → a in ℓ_1 and z' → z coordinatewise (weak*), with **the far coordinates of z' completely free**
(any c_0 values of modulus < 1). L^*J_V(L x') → L^*w in norm automatically (compactness). This freedom
(engineering the block peak/non-peak pattern of J_V(L x') at large k) has not been exploited systematically yet.

(R5) Heuristic: mates at an NA point f' with normer x' are constrained by the second-order behaviour of the
primal excess Δ'(y) = p(y) - f'(y) ≥ 0 near x' (g'(y)^2 ≲ 2Δ'(y)); mates at f by the excess p** - f near ξ.
Recovery ⇔ some lower semicontinuity of these "curvature profiles" along well-chosen x' → ξ (weak*), on the
correct range of scales: for ||f'-f|| = ε, scales |t| ≳ sqrt(ε/(1-ρ^2)) are inherited from f by the slack;
smaller scales must come from the local structure at f'.
Block heuristic: in block m, coordinate k contributes to the excess at scale t roughly
min( t^2 m^2 u_{k,m}(y)^2 /(2C), |t| (gap_k/M) m Φ_m(k) |u_{k,m}(y)| ) (quadratic regime for small t, linear beyond),
with gap_k = M - |w_m(k)|; the linear-regime terms with Φ_m(k) ≲ |t| sum to O(t^2) (geometric Φ), so they matter
at every scale. Peaks (gap 0) contribute no curvature.

(R6) Known recoverable mates at f (Preprint A + [Check]): block directions R_m^*(ω - d w_m) with ω finitely
supported off-peak; weighted limits with unbounded ω (Σ λ_k ω_k^2 < ∞, support in half-peak set); base
directions b with finite support inside supp a and b(ξ) = 0 (q*(a+tb) is C^2) — combined recoverability along
a common sequence is plausible but not written down.

(R7) Known obstacles / suspicious mate types:
 (i) one-sided base kinks at coordinates j ∈ I(ξ) \ supp a where |z_j| = 1 but a_j = 0;
 (ii) "cross" mates whose admissible decompositions need block coefficients approximating base vectors such as
      e_j^*: existence depends on approximation RATES of (u_{k,m})_k towards e_j^* relative to Φ_m(k) — i.e. on
      fine details of Martín's choice of T;
 (iii) a ∉ c_00 (infinite base support), sign-flip costs Σ_{|t b_j|>|a_j|};
 (iv) infinite peak sets, near-peak coordinates with |w(k)| → M;
 (v) infinitely many blocks (use Remark martin-tail to avoid, or handle).
 Split NA operators S_1 + S_2∘L (bounded lifts) are NOT dense (Preprint A, Remark at end of Sec. 3).

## Standards
- Write proofs in English, fully rigorous, no abbreviated notation in final statements.
- Mark every step as PROVED / SKETCH / HEURISTIC / FALSE. Never present a heuristic as a proof.
- If you find an error in the preprints or in the reductions above, report it prominently.
- Prefer finite block set I (p_N) when it simplifies; say which setting you use.
