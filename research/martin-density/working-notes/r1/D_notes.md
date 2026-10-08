# Strategy D — an abstract "dual transfer" theorem for p = q + ||L·||

Notes by the Strategy-D agent. These notes are meant to be self-contained. Every statement carries
one of the labels **PROVED / SKETCH / HEURISTIC / FALSE / OPEN**. "PROVED (mod. X)" means: proved here
in full, assuming only the explicitly named external fact X (taken from Preprint A, Preprint B or
Martín's paper as quoted in the briefing). arXiv was not reachable from this sandbox, so Martín's
Lemma A / Lemma B are used only in the form quoted in Preprint B.

---------------------------------------------------------------------------------------------------

## 0. Executive summary

**Goal of Strategy D.** Prove a general theorem: if NA((X,q),F) is dense for all finite-dimensional F
and L : X → V is compact, then NA((X,p),F) is dense for p = q + ||L·||_V, i.e. for the dual Minkowski
sum B_{p*} = B_{q*} + L*(B_{V*}).

**Verdict.** A fully general theorem is out of reach (and any counterexample to it would be a
counterexample to Lindenstrauss property B for a finite-dimensional space, which is open — §13).
What I can prove is a *conditional* transfer theorem with checkable hypotheses (Theorem 10.4), which
Martín's space satisfies for a large class of mates, giving **new unconditional recovery results for
Martín's norm**:

* **Theorem 11.6 (PROVED mod. standing facts).** For the canonical base and Martín's p (finite or
  infinite block set), every *locally split* contractive operator (f,g) : (c_0,p) → ℓ_2^2 lies in the
  closure of NA. In particular **every norm-one split-contractive operator S_1 + S_2∘L
  (||S_1||_q ≤ 1, ||S_2|| ≤ 1) is a norm limit of norm-attaining operators**, although split NA
  operators themselves are not dense (Preprint A). The approximating NA operators are only *locally*
  split. The proof rests on truncation lemmas with an exact first-order correction (§11.5), whose error
  is second order in t on a fixed range of t (also stress-tested numerically: 0 violations in about
  2.2·10^5 random instances, scripts n3b, n4).
* The finite local-certificate theorem quoted from [Check] and Preprint A's weighted-direction theorem
  are re-derived from Theorem 10.4 (§11.7), so they no longer depend on the unavailable note [Check].
* **Theorem 12.4' (PROVED), a complete abstract transfer in a special case.** For the canonical base
  and a finite-rank Hilbertian perturbation (V = ℓ_2^r, L*(V) ∩ c_00 = {0}), at every first row f whose
  forced base part a is finitely supported and whose base contact has a uniform margin off supp a,
  *every* admissible decomposition of f + tg is differentiable in t with O(t²) remainder, and
  {f} × C(f) ⊂ cl NA. Under the same hypotheses Martín's blocks force unbounded lifts (Preprint A);
  so the lift blow-up comes from the infinite-dimensional, non-Hilbertian block geometry.

What remains open is an *intrinsic* statement about the bidual geometry at a single non-attaining f:

* **Local Splitting Density (LSD), §12 — OPEN.** For every f ∈ S_{p*}, every mate g ∈ C(f) and every
  ρ < 1, ρg is a norm limit of locally split mates of f. LSD ⇒ density of NA((c_0,p),ℓ_2^2)
  (Corollary 11.8). LSD is established for split, locally split, base-type and block-type mates and
  for Preprint A's weighted mates; it is *not* established for mates whose optimal decompositions
  mix base and block parts in a scale-dependent way (second-order "parallel-sum" mates, two-sided
  certificates with infinitely supported base parts, and above all "cross" mates that carry base
  vectors through block coordinates k(t) → ∞, §12). For cross mates,
  approximability by finite certificates is governed by a quantitative rate comparison between
  q*(u_{k,m} − ê_j) and Φ_m(k) that depends on fine details of Martín's operator T (HEURISTIC). In the
  fast regime the carrying block coordinates are automatically off-peak for every point with vanishing
  j-th coordinate (Lemma 12.5, PROVED), so the danger zone is the intermediate regime
  q*(u_{k,m} − ê_j) ≍ Φ_m(k) (§12.6).

Obstructions found for the other mechanisms:

* (a) The star-set (fixed second row) Bishop–Phelps theorem is **FALSE already for the canonical base
  q**, which itself has density for all finite-dimensional ranges: every NA operator (c_0,q) → ℓ_2^2
  has both rows in c_00 (Prop. 4.3). Hence no dual-transfer argument can keep one row fixed.
* (b) The weak*-continuous function F_T attains its maximum on B_{q**}; attainment of T is exactly
  "a maximiser lies in B_q" (Prop. 5.1). For finite-rank L the image of B_q contains the relative
  interior of the image of B_{q**} (Lemma 5.3), but maximisers are always radially extreme
  (Lemma 5.2), so they sit on the relative boundary. No variational principle applies directly
  (X* = ℓ_1 is not Asplund, and maximisers must lie in B_q rather than B_{q**}).
* (c) Range renorming (selection seminorm, Prop. 6.1) reduces the problem to approximating (T,L)
  with a **frozen** second component plus a tightness condition; no mechanism for this is available,
  and its Euclidean fixed-row analogue fails already for the base (§6, HEURISTIC as a route).
* (d) Operators on the graph extend isometrically to (X,q) ⊕_1 V iff they are split (§7); the graph is
  not 1-complemented in Martín's case.
* (f) For any Gateaux-smooth norm ν and nontrivial projection P, ν − ν∘P is never convex (Lemma 9.1);
  so within-block truncation never gives p = q_η + s_η, and even the pointwise lift fails (the largest
  seminorm below the truncation defect is 0, Cor. 9.2'). Martín's space has no norm-one finite-rank
  projections of rank ≥ 2 (Prop. 9.3). A "Read-type" dual transfer theorem (Theorem 9.4) holds when
  the perturbing functionals are finitely supported, recovering Preprint B's argument abstractly.
* Structural facts: abstract global compactness of mate fibres under an (m_1^*)-type hypothesis
  (Thm 10.1); bounded block lifts when V is Hilbert (Prop. 10.2) versus unbounded lifts in Martín's V;
  rigidity of the block component in Martín's space (Prop. 11.9): an NA approximant of a non-attaining
  f can never share a block support functional with f, whereas for finite-rank L the block part can
  generically be frozen; second-order "parallel-sum" calculus for dual Minkowski sums (Prop. 10.3,
  numerically confirmed).

**Leaning:** neutral. Nothing found points to a counterexample; every mate type I can analyse is
recoverable; the remaining class is rate-dependent.

---------------------------------------------------------------------------------------------------

## 0.1 Status table (all claims)

| # | Statement (short) | Status |
|---|---|---|
| 2.1 | B_{p*} = B_{q*} + L*(B_{V*}), weak*-closed; p*(f) = min max(q*(a), ‖v‖) | PROVED |
| 2.2 | p** = q** + ‖L**·‖; L** maps X** into V, weak*-to-norm on bounded sets | PROVED |
| 2.3 | NA_p ∩ S = {a + L*v : a ∈ NA_q ∩ S attaining at y, v ∈ B_{V*}, v(Ly) = ‖Ly‖} | PROVED |
| 2.4 | Mates, KLMW attainment lemma, reduction to (f,ρg) | PROVED |
| 3.1 | Generalised lift lemma (characterises split NA operators) | PROVED |
| 3.2 | Split-contractive set SC is norm closed (L compact, F finite-dim) | PROVED |
| 3.3 | SC ≠ all contractions; NA ∩ SC not dense (Martín) | PROVED (mod. Preprint A Props 3.3–3.4 + Remark 3.5) |
| 3.4(i) | Density forces NA operators at positive distance from SC | PROVED (mod. 11.7) |
| 3.4(ii) | Residually many NA points of c_0-faces carry non-split (weighted) mates | SKETCH (mod. Preprint A uniform estimate) |
| 4.1 | (f,h) attains ⇔ f attains its sup on the star set A_h | PROVED |
| 4.2 | Canonical base: C_q(a) ⊂ span{e_j* : j ∈ supp a} for a ∈ c_00 | PROVED |
| 4.3 | Canonical base: every NA operator into ℓ_2^2 has T*(ℓ_2^2) ⊂ c_00; star-set Bishop–Phelps fails | PROVED |
| 4.4 | Star-set Bishop–Phelps for Martín's p | OPEN |
| 5.1 | T attains ⇔ F_T attains sup on B_q; F_T** weak*-continuous on B_{q**} | PROVED |
| 5.2 | Maximisers of Ψ over K are radially extreme | PROVED |
| 5.3 | Finite-rank L, any (X,q): (T,L)(B_q) ⊇ ri (T**,L**)(B_{q**}) | PROVED |
| 5.4 | Finite-rank L: obstruction to attainment sits in the base part of a maximal row | PROVED |
| 5.5 | Upper semicontinuity of bidual maximisers | PROVED |
| 6.1 | Selection seminorm ν; transfer needs frozen L + tightness | PROVED |
| 6.2 | Range renorming as a route to dual transfer | HEURISTIC (route not viable; frozen-row analogue fails by 4.3) |
| 7.1 | Isometric extension to (X,q) ⊕_1 V ⇔ split; graph not 1-complemented (Martín) | PROVED ((iv) mod. 3.3) |
| 8 | Variational principles (Ekeland, Stegall, Bourgain–Stegall) do not apply directly | HEURISTIC (obstruction analysis) |
| 9.1 | ν Gateaux smooth along ker P ⇒ ν − ν∘P not convex | PROVED |
| 9.2 | Within-block truncation never yields p = q_η + s_η with s_η a seminorm | PROVED |
| 9.2' | Largest seminorm below a within-block truncation defect is 0 (no pointwise lift) | PROVED |
| 9.3 | (c_0,p) has no norm-one finite-rank projection of rank ≥ 2 | PROVED (mod. Martín's theorem) |
| 9.4 | Read-type dual transfer theorem | PROVED |
| 9.5 | Exact "finite rank + small" decomposition of a Martín block | OPEN |
| 9.6 | Dual transfer for finite-rank L in general | OPEN |
| 10.0 | Canonical base satisfies (A1) with N = ‖·‖_1 | PROVED |
| 10.1 | Abstract global compactness of mate fibres under (A1) | PROVED |
| 10.1' | Abstract residual recovery (dense G_δ of good first rows) | PROVED |
| 10.1'' | Finite-test-vector criterion (briefing R3) | PROVED |
| 10.2 | V Hilbert ⇒ ‖W(t) − w‖ ≤ ∣t∣/√(1−q_0) + O(t²) for every admissible decomposition | PROVED |
| 10.2R | Martín's V*: modulus of rotundity at w in direction e_k is O(Φ_m(k)²) | PROVED |
| 10.2' | V Hilbert, canonical base ⇒ mates are two-sided split to first order | SKETCH |
| 10.3 | Parallel-sum second-order formula for dual Minkowski sums | SKETCH (upper bound rigorous for smooth gauges; numerically confirmed) |
| 10.3' | In Martín's space base/block mass shifting pays kink costs | HEURISTIC |
| 10.4 | Conditional dual transfer theorem (split certificates + recovery hypotheses) | PROVED |
| 10.5 | Linear-radius criterion for certified approximants | PROVED |
| 11.1–11.4 | (S), (H_base), (H_V) hold for Martín with finite certificates 𝒞_fin | PROVED (mod. SF1–SF4) |
| 11.5 | Truncation with exact first-order correction (base and block), second-order error | PROVED |
| 11.6 | Martín: every locally split mate is recoverable; normalised SC ⊂ cl NA | PROVED (mod. SF1–SF4) |
| 11.7 | Re-derivation of [Check, Thm 3.1] (as quoted) and of Preprint A's weighted theorem | PROVED (weighted part mod. Preprint A uniform estimate) |
| 11.8 | LSD ⇒ density of NA((c_0,p),ℓ_2^2) | PROVED |
| 11.9 | Block-component rigidity in Martín's space | PROVED (mod. eq. (block-sign), Lemma B) |
| 11.10 | Finite-rank L: block part can generically be frozen | SKETCH |
| 11.11 | a ∈ c_00 and finitely supported two-sided certificates ⇒ split | PROVED |
| 11.11' | Recovery of general two-sided certificates (one-sided kinks) | OPEN |
| 12.1 | LSD for Martín's space | OPEN |
| 12.2 | Cross mates: single-certificate approximability governed by a rate comparison; fails at critical linear rates | HEURISTIC |
| 12.3 | Multi-scale replication in c_0-faces | OPEN |
| 12.4 | Finite-rank Hilbert test case: mates at NA points lie in c_00 + L*(V) with differentiable lifts | PROVED (via 12.4''(i)); full case OPEN |
| 12.4' | Finite-rank Hilbert L, a ∈ c_00, uniform contact margin: lifts differentiable with O(t²) remainder; {f} × C(f) ⊂ cl NA | PROVED |
| 12.4'' | Extensions: (i) differentiable lifts under a finite injectivity condition; (ii) recovery for a ∉ c_00; (iii) oscillating lifts when no such condition | (i) PROVED; (ii) SKETCH; (iii) HEURISTIC |
| 12.5 | Fast regime: carrying coordinates are automatically off-peak for every y with y_j = 0 | PROVED (mod. block-threshold) |
| 12.6 | Rate trichotomy (slow / superfast / intermediate) for cross mates | HEURISTIC |
| 13 | A counterexample to the abstract statement contradicts no known theorem | PROVED (logical remark: it would be a failure of property B for a finite-dimensional space) |
| N1 | Parallel-sum numerics | numerical evidence |
| N2 | Non-convexity of block truncation numerics | numerical evidence (Lemma 9.1 is the proof) |
| N3–N6 | Stress tests of (11.5.1), Lemma 11.5(b), Theorem 12.4'(i), Lemma 11.3 | numerical evidence (0 violations; O(t²) and uniform radius confirmed) |

---------------------------------------------------------------------------------------------------

## 1. Setting, notation, standing facts

All spaces are real. (X,q) is a Banach space, V a Banach space, L : X → V a bounded operator, and

    p(x) = q(x) + ‖Lx‖_V .

Then q ≤ p ≤ (1+‖L‖) q (‖L‖ = ‖L‖_{q→V}), so p is an equivalent norm. Write B_r, S_r, r*, r** for
the ball, sphere, dual and bidual norms of a norm r. NA_r = NA((X,r),ℝ). For T : X → F, ‖T‖_r is
the operator norm with respect to r on X. KLMW = Kadets–López–Martín–Werner.

**Canonical base (c_0 case).** X = c_0, H a Hilbert space, U : H → c_0 compact with dense range,
B_q = B_{c_0} + U(B_H), q*(a) = ‖a‖_1 + ‖U*a‖_H on ℓ_1, NA_q = c_00 (Preprint B, Lemma 2.2 + NA(c_0) =
c_00), U* is injective (dense range of U). B_{q**} = B_{ℓ_∞} + U(B_H) (weak*-closure of B_{c_0} plus the
norm compact set U(B_H)).

**Martín's data** (as quoted in the briefing / Preprint B §2.3): T : ℓ_1(ℕ×ℕ) → Y ⊂ X* injective,
norm one; Y ∩ c_00 = {0}; u_{k,m} = Te_{k,m}/q*(Te_{k,m}); every tail of (u_{k,m})_k is norm dense
in S_{q*} (Lemma B); Φ_m(k) = 2^{-m-k} q*(Te_{k,m}); (R_m x)(k) = mΦ_m(k)u_{k,m}(x);
V_m = (ℓ_1, |·|_m) with B_{|·|_m} = B_{ℓ_1} + D_m(B_{ℓ_2}), dual norm N_m(w) = ‖w‖_∞ + ‖D_m w‖_2
(D_m diagonal with entries Φ_m(k)); V = (⊕_{m∈I} V_m)_{ℓ_1}, V* = (⊕ (ℓ_∞,N_m))_{ℓ_∞};
Lx = (R_m x)_m; R_m*(v) = T(Σ_k v(k) m2^{-m-k} e_{k,m}) ∈ Y for v ∈ ℓ_∞ (Preprint B (M6)).

**Standing facts used (imported, as quoted):**
(SF1) N_m is strictly convex (proved below in one line), hence |·|_m is Gateaux smooth; the ℓ_1-sum
      V is smooth at every point with all blocks nonzero.
(SF2) R_m and R_m** are injective; R_m is compact; ‖R_m‖ ≤ m2^{-m}.
(SF3) Block-threshold lemma (Preprint B Lemma 5.6) and eq. (block-sign) (Preprint B (5.1)): if
      u_{n_j,m} → v and w ≠ 0 supports R_m**ξ with ξ(v) ≠ 0, then eventually w(n_j) = ‖w‖_∞ sign ξ(v).
(SF4) Lemma B (density of tails), Y ∩ c_00 = {0}, injectivity of T.
(SF5) For the results that use them explicitly: Preprint A Theorem 3.1's uniform expansion estimate
      (weighted directions) and Preprint A Prop. 3.3/3.4 (no bounded lift / lift blow-up).

Proof of strict convexity of N_m: if N_m(w_1) = N_m(w_2) = N_m((w_1+w_2)/2) = 1 then both convex
parts ‖·‖_∞ and ‖D_m·‖_2 are affine on the segment; affinity of the Hilbert norm forces D_m w_1, D_m w_2
to be positively proportional, so w_1 = λ w_2 (D_m injective), and N_m(w_1) = N_m(w_2) gives λ = 1. A
norm whose dual norm is strictly convex is Gateaux smooth. For the ℓ_1-sum, the subdifferential at
(z_m) with all z_m ≠ 0 is the product of the (singleton) block subdifferentials. ∎

---------------------------------------------------------------------------------------------------

## 2. Basic abstract facts

**Proposition 2.1 (dual ball). PROVED.** B_{p*} = B_{q*} + L*(B_{V*}); the right side is weak*-compact;
and p*(f) = min{ max(q*(a), ‖v‖) : f = a + L*v } (minimum attained).

*Proof.* "⊇": (a + L*v)(x) = a(x) + v(Lx) ≤ q(x) + ‖Lx‖ = p(x). The set B_{q*} + L*(B_{V*}) is convex
and weak*-compact (B_{q*} and B_{V*} are weak*-compact, L* is weak*-to-weak* continuous, and the sum
of two weak*-compact sets is weak*-compact as a continuous image of their product). Its support
function at x ∈ X equals sup_a a(x) + sup_v v(Lx) = q(x) + ‖Lx‖ = p(x), which is also the support
function of the weak*-closed convex set B_{p*}. Weak*-closed convex sets in X* are determined by their
support functions on X (Hahn–Banach in (X*,w*), whose dual is X). For the gauge formula apply this to
λB_{p*} = λB_{q*} + L*(λB_{V*}); attainment of the minimum follows from weak*-compactness. ∎

**Proposition 2.2 (bidual). PROVED.** p**(ξ) = q**(ξ) + ‖L**ξ‖_{V**}. If L is compact then
L**(X**) ⊂ V and L** is weak*-to-norm continuous on bounded subsets of X**.

*Proof.* p**(ξ) = sup_{f ∈ B_{p*}} ξ(f) = sup_a ξ(a) + sup_v ξ(L*v) = q**(ξ) + ‖L**ξ‖. If L is
compact, L*(B_{V*}) is norm compact; for a bounded net ξ_α → ξ weak*, (L**ξ_α)(v) = ξ_α(L*v) → ξ(L*v)
uniformly in v ∈ B_{V*} (bounded nets of functionals converge uniformly on norm-compact sets), i.e.
L**ξ_α → L**ξ in norm; and L**ξ ∈ V by Gantmacher (or because it is a norm limit of L x_α, Goldstine). ∎

**Proposition 2.3 (norm-attaining functionals). PROVED.** Let f ∈ S_{p*} and x ∈ S_p. Then f(x) = 1 iff
for one (equivalently, every) decomposition f = a + L*v with q*(a) ≤ 1, ‖v‖ ≤ 1 one has a(x) = q(x) and
v(Lx) = ‖Lx‖. In that case q*(a) = 1 (x ≠ 0), and ‖v‖ = 1 if Lx ≠ 0. Conversely, if a ∈ S_{q*}
attains its q-norm at y ∈ S_q and v ∈ B_{V*} satisfies v(Ly) = ‖Ly‖, then f = a + L*v ∈ S_{p*}
attains its p-norm at y/p(y).

*Proof.* 1 = f(x) = a(x) + v(Lx) ≤ q(x) + ‖Lx‖ = 1 forces equality in both terms; q(x) > 0 gives
q*(a) ≥ a(x)/q(x) = 1. Converse: f(y) = 1 + ‖Ly‖ = p(y) and p*(f) ≤ 1 by 2.1. ∎

If moreover V is smooth at Ly (as in Martín's case for every y ≠ 0, by (SF1),(SF2)), v = J_V(Ly) is
forced and NA_p ∩ S = {a + L*J_V(Ly) : a ∈ NA_q ∩ S_{q*}, y ∈ S_q, a(y) = 1}.

**Forced decomposition.** For f ∈ S_{p*} and a normer ξ ∈ S_{p**} (f(ξ) = 1), every decomposition
f = a + L*w with q*(a), ‖w‖ ≤ 1 satisfies a(ξ) = q**(ξ) =: q_0 and w(L**ξ) = ‖L**ξ‖ = 1 − q_0 (same
proof). q_0 ≥ 1/(1+‖L‖) > 0 since q** ≥ p**/(1+‖L‖). Hence q*(a) = 1 and ξ̂ := ξ/q_0 is a q-normer of a
in B_{q**}. If V is smooth at L**ξ, w = J_V(L**ξ) and a = f − L*w are unique. In the canonical base,
ξ̂ = z + U(U*a/‖U*a‖) with z ∈ B_{ℓ_∞}, z_j = sign a_j on supp a (equality case of
a(z + Uh) ≤ ‖a‖_1 + ‖U*a‖, using injectivity of U*).

**Mates.** For f ∈ S_{p*}: C(f) = {g : p*(f+tg) ≤ √(1+t²) ∀t ∈ ℝ}.

**Proposition 2.4. PROVED.** (i) ‖(f,g)‖_{p→ℓ_2^2} ≤ 1 iff g ∈ C(f) (for p*(f) = 1) iff
f(y)² + g(y)² ≤ p(y)² ∀y. (ii) (KLMW) If f attains at x_0 ∈ S_p and g ∈ C(f), then (f,g) attains its
norm 1 at x_0. (iii) Every norm-one T : (X,p) → ℓ_2^2 equals R∘(f,g) for a rotation R, with f ∈ S_{p*},
g ∈ C(f); NA((X,p),ℓ_2^2) is dense iff (f,ρg) ∈ cl NA for all f ∈ S_{p*}, g ∈ C(f), ρ ∈ (0,1).
(iv) For g ∈ C(f): g(ξ) = 0 for every normer ξ of f, and p*(g) ≤ 1.

*Proof.* (i) ‖(f,g)‖ = sup_θ p*(cos θ f + sin θ g) and p*(cos θ f + sin θ g) = |cos θ| p*(f + tan θ g)
with |cos θ| = (1+tan²θ)^{-1/2}; the case θ = π/2 is the limit t → ∞. (ii) |g(x_0)| ≤
(p(x_0)² − f(x_0)²)^{1/2} = 0, so ‖(f,g)x_0‖ = 1. (iii) θ ↦ p*(T*(cos θ, sin θ)) is continuous on the
circle and attains its maximum ‖T‖ = 1; rotate that direction to e_1. (f,ρg) → (f,g) as ρ → 1.
(iv) 1 + t g(ξ) = (f+tg)(ξ) ≤ √(1+t²) for all t forces g(ξ) = 0; divide p*(f+tg) ≤ √(1+t²) by t → ∞. ∎

Note the **slack**: g ∈ C(f) ⇒ p*(f + tρg) ≤ √(1+ρ²t²), and
√(1+t²) − √(1+ρ²t²) = (1−ρ²)t²/(√(1+t²)+√(1+ρ²t²)) ≥ (1−ρ²)t²/(2√(1+t²)).   (2.5)

---------------------------------------------------------------------------------------------------

## 3. Split operators: what bounded lifts can and cannot do

**Definition.** T ∈ L((X,p),F) is *split-contractive* if T = S + Φ∘L with S ∈ L((X,q),F),
Φ ∈ L(V,F), ‖S‖_q ≤ 1, ‖Φ‖ ≤ 1. SC denotes the set of split-contractive operators. Every T ∈ SC
satisfies ‖T‖_p ≤ 1 (‖Tx‖ ≤ q(x) + ‖Lx‖). For F = ℓ_2^2 and T = (f,g) with p*(f) = 1, T ∈ SC iff
f = a + L*w, g = b + L*v with (a,b) contractive on (X,q) and (w,v) contractive on V, i.e.
q*(a+tb) ≤ √(1+t²) and ‖w+tv‖ ≤ √(1+t²) for all t ("g is a split mate of f").

**Lemma 3.1 (generalised lift; split NA operators). PROVED.** Let S ∈ L((X,q),F) attain ‖S‖_q = 1 at
z_0 ∈ S_q, and let Φ ∈ L(V,F), ‖Φ‖ ≤ 1, satisfy Φ(Lz_0) = ‖Lz_0‖·Sz_0/‖Sz_0‖. Then A = S + Φ∘L has
‖A‖_p = 1 and attains it at z_0/p(z_0). Conversely every NA operator lying in SC arises this way.

*Proof.* ‖Ax‖ ≤ q(x) + ‖Lx‖; Az_0 = (1 + ‖Lz_0‖)Sz_0 has norm p(z_0). Conversely if A = S + ΦL ∈ SC
attains at x_0 ∈ S_p then ‖Ax_0‖ = p(x_0) = q(x_0) + ‖Lx_0‖ forces ‖Sx_0‖ = q(x_0), ‖ΦLx_0‖ = ‖Lx_0‖
and Sx_0, ΦLx_0 positively parallel (equality in the triangle inequality in a strictly convex F; for
general F one gets the same conclusion after replacing "parallel" by "on a common face"). ∎

Preprint B's lift lemma is the case Φ = Sz_0 ⊗ J_V(Lz_0).

**Proposition 3.2 (SC is closed). PROVED.** If L is compact and F is finite-dimensional, SC is
norm closed in L((X,p),F).

*Proof.* Let T_α = S_α + Φ_α L → T in norm (nets). Identify F ≅ ℝ^d; Φ_α* ∈ L(F*,V*) lies in a
bounded, hence weak*-compact, set of (V*)^d. Pass to a subnet with Φ_α* → Φ_0 weak*
(coordinatewise). Since L* is compact and weak*-to-weak* continuous, on the norm-compact set
L*(B_{V*}) the weak* and norm topologies coincide, so L*Φ_α* → L*Φ_0 in norm. Then
S_α* = T_α* − L*Φ_α* → T* − L*Φ_0 =: S_0 in norm, ‖S_0‖_q ≤ 1, ‖Φ_0‖ ≤ 1 (weak*-lsc), and
T = S_0* + Φ_0*∘L (adjoints of finite-rank maps). ∎

**Proposition 3.3 (SC is not everything; split NA is not dense). PROVED mod. (SF5).** In Martín's
space (canonical base) there is a contractive T_0 = (f, ρg_0) : (c_0,p) → ℓ_2^2 with T_0 ∉ SC. Hence
cl(NA ∩ SC) ⊂ SC does not contain T_0; since T_0 ∈ cl NA (Preprint A, Remark 3.5; re-derived in §11.7),
NA ∩ SC is not dense even in cl NA.

*Proof.* Take f, g_0, ρ from Preprint A's Remark (non-attaining examples): f has forced decomposition
(a,w) with a ∈ c_00, the normalised base contact z satisfies ‖z|_{F^c}‖_∞ < 1 (F = supp a), and g_0 is a
small multiple of the weighted direction g with unbounded ω. If T_0 ∈ SC then f = s_1 + L*φ_1,
ρg_0 = s_2 + L*φ_2 with (s_1,s_2) q-contractive, (φ_1,φ_2) V-contractive. Since q*(s_1), ‖φ_1‖ ≤ 1,
φ_1 norms L**ξ, so φ_1 = w by smoothness (SF1) and s_1 = a. Then f + tρg_0 = (a+ts_2) + L*(w+tφ_2)
is an admissible decomposition for every t with ‖(w+tφ_2) − w‖/|t| = ‖φ_2‖ bounded, contradicting
Preprint A Prop. 3.4 (applied with t replaced by ρ c t, where g_0 = c g). (I re-checked the logic of
Preprint A Props. 3.3 and 3.4: weak*-limits of bounded block quotients give g = b + L*v with
b(ξ) = 0 = v_l(R_l**ξ), q*'(a;b) ≤ 0, hence Σ_{k∉F}(|b_k| − z_k b_k) ≤ 0, hence b|_{F^c} = 0 by the
margin of z, contradicting the injectivity argument of Prop. 3.3, which uses Y ∩ c_00 = {0}.) ∎

**Proposition 3.4 (dichotomy). PROVED (i) / SKETCH (ii).** Martín's space, canonical base.
(i) There are NA operators (c_0,p) → ℓ_2^2 at positive distance from SC (namely NA approximants of
T_0 from 3.3, which exist by §11.7). In particular *any* density proof must produce NA operators
whose second row is a non-split mate of the first.
(ii) Explicitly: fix a ∈ c_00 ∩ S_{q*}, F = supp a, a block m. In the Baire space
Z_0 = {z ∈ c_0 : z|_F = sign a, sup_{j∉F}|z_j| < 1} (open subset of a closed affine subspace of c_0)
the set of z for which the NA functional f_z = a + L*J_V(L y_z), y_z = z + U(U*a/‖U*a‖), has infinitely
many half-peak indices in block m (|w_{z,m}(k)| < M_{z,m}/2) is a dense G_δ. For such z, Preprint A's
weighted direction g = R_m*ω − d R_m*w_{z,m} with ω(k_j) = j on half-peak indices k_j ≥ j is (after
scaling) a mate of the *norm-attaining* f_z which is not split; hence (f_z, c g) ∈ NA \ SC.

*Proof of (ii) (sketch, all steps checked).* Openness: z ↦ L y_z is norm continuous; J_V is
norm-to-weak* continuous at nonzero points (smoothness); coordinates are weak*-continuous on ℓ_∞;
z ↦ C_{z,m} = ‖D_m w_{z,m}‖_2 is continuous because D_m : ℓ_∞ → ℓ_2 is weak*-to-norm continuous on
bounded sets (Φ_m ∈ ℓ_2, dominated convergence); M = 1 − C. Density: given z, pick j ∉ F,
u = (e_j* − y_z(j)a)/q*(e_j* − y_z(j)a) (so u(y_z) = 0 because a(y_z) = 1, and u(e_j) ≠ 0 because
a_j = 0); by Lemma B pick k_l → ∞ with u_{k_l,m} → u; z_l = z − (u_{k_l,m}(y_z)/u_{k_l,m}(e_j))e_j → z
and u_{k_l,m}(y_{z_l}) = 0. By the block-threshold lemma (SF3) a coordinate k with (R_m y)(k) = 0
cannot be a peak coordinate (the equation α(k) + Φ(k)²w(k)/C = 0 with α(k)w(k) ≥ 0 and |w(k)| = M is
impossible), and then w(k) = C(R_m y)(k)/(Φ(k)²|R_m y|) = 0. So z_l lies in the open set. Mate
property: Preprint A's uniform expansion (proof of its Theorem 3.1, first half) never uses
non-attainment, so p*(f_z + tg) ≤ 1 + Ht²/2 + o(t²), and the triangle inequality away from 0 gives a
finite mate gauge. Non-splitness: g ∈ Y because Σ_j 2^{-k_j} j < ∞; a split decomposition g = b + L*v
with (a,b) q-contractive has b ∈ C_q(a) ⊂ span{e_i* : i ∈ F} ⊂ c_00 (Lemma 4.2), so b ∈ Y ∩ c_00 = {0}
and injectivity of T forces v_m = ω − dw unbounded, a contradiction. ∎

**Remark 3.5.** (i) shows the logical tension that must be resolved by any positive answer: split NA
operators are not dense, so NA operators *must* have non-split mates; (ii) shows they do, already at
"generic" NA points of c_0-faces. There is therefore no contradiction between "split NA is not
dense" and density.

---------------------------------------------------------------------------------------------------

## 4. Mechanism (a): non-convex Bishop–Phelps for star sets

For h ∈ X* with p*(h) < 1 put r_h(x) = (p(x)² − h(x)²)^{1/2} ≥ (1 − p*(h)²)^{1/2} p(x) and
A_h = {x : r_h(x) ≤ 1}, a closed, bounded, symmetric, star-shaped (generally non-convex) set.

**Proposition 4.1. PROVED.** For f ∈ X* \ {0} let σ_f = sup_{A_h} f > 0. Then ‖(f/σ_f, h)‖ = 1, and
(f/σ_f, h) attains its norm iff f attains its supremum on A_h. Moreover, if ‖(f,h)‖ = 1 then σ_f = 1.
Consequently: the norm-attaining operators with *second row exactly h* are exactly the (f/σ_f, h)
with f attaining its sup on A_h.

*Proof.* By homogeneity |f| ≤ σ_f r_h, i.e. (f/σ_f)² + h² ≤ p², and for x with f(x)/σ_f close to
r_h(x) the ratio is close to 1. If f(x_0) = σ_f, x_0 ∈ A_h, then 1 = f(x_0)/σ_f ≤ r_h(x_0) ≤ 1, so
(f(x_0)/σ_f)² + h(x_0)² = p(x_0)². Conversely attainment at x_0 means |f(x_0)|/σ_f = r_h(x_0), and
±x_0/r_h(x_0) ∈ A_h attains σ_f. If ‖(f,h)‖ = 1 and σ_f = c < 1 then f² + h² ≤ c²p² + (1−c²)h² ≤
(c² + (1−c²)p*(h)²)p², so ‖(f,h)‖ < 1. ∎

**Lemma 4.2. PROVED.** Canonical base, a ∈ c_00 ∩ S_{q*}. Then C_q(a) ⊂ span{e_j* : j ∈ supp a}.

*Proof.* Let b ∈ C_q(a), j ∉ supp a. Then q*(a+tb) + q*(a−tb) − 2 ≤ 2(√(1+t²) − 1) ≤ t². The
Hilbert part satisfies ‖U*(a+tb)‖ + ‖U*(a−tb)‖ ≥ 2‖U*a‖, and every coordinate of the ℓ_1 part satisfies
|a_k+tb_k| + |a_k−tb_k| − 2|a_k| ≥ 0, with the coordinate j contributing 2|t||b_j|. So 2|t||b_j| ≤ t²
for all t, i.e. b_j = 0. ∎

**Proposition 4.3 (star-set Bishop–Phelps fails for the base). PROVED.** Canonical base. Every
T ∈ NA((c_0,q),ℓ_2^2) satisfies T*(ℓ_2^2) ⊂ c_00. Hence for every h ∈ ℓ_1 \ c_00 with q*(h) < 1, the
only functional attaining its supremum on the closed bounded star set A_h (built with q) is f = 0;
equivalently no operator with second row h attains its norm. This happens although
NA((c_0,q),F) is dense for every finite-dimensional F (rows in c_00 ⊂ NA_q, Preprint B Lemma 3.5).

*Proof.* Let T attain ‖T‖ = 1 at x_0. Rotate so that Tx_0 = (1,0): T = R(φ,ψ). Then φ(x_0) = 1 =
q*(φ), so φ ∈ NA_q = c_00, and ψ ∈ C_q(φ) ⊂ c_00 by Lemma 4.2. T*(ℓ_2^2) = span{φ,ψ}. The rest is
Prop. 4.1. ∎

**Consequence for dual transfer.** Any approximation scheme must perturb all rows simultaneously;
in particular schemes of the type "keep the second row h and find a better first row" (non-convex
Bishop–Phelps for A_h) are hopeless even for a base that has density for all finite-dimensional
ranges. The same proof shows: whenever NA(Z) is "thin" in the sense that mates at NA points live in
a fixed proper subspace D, operators with a row outside D never attain.

**Remark 4.4 (Martín's p). OPEN.** For Martín's p the analogous question is whether
⋃_{φ ∈ NA_p∩S}(ℝφ + C_p(φ)) is a proper subset of ℓ_1 (it is a union of compact sets by Thm 10.1, but
NA_p ∩ S is not σ-compact, so Baire does not apply directly). Prop. 3.4(ii) shows that mates at NA
points can leave c_00 + L*(V*) (weighted mates with Σλ_kω_k² < ∞ but Σ2^{-k}|ω_k| = ∞ when
q*(Te_{k,m}) is small leave Y as well). I did not settle it; it is irrelevant for density.

---------------------------------------------------------------------------------------------------

## 5. Mechanism (b): the weak*-continuous function F_T

Let T ∈ L((X,p),F), F finite-dimensional, λ = ‖T‖_p > 0, and F_T(x) = ‖Tx‖ − λ‖Lx‖.

**Proposition 5.1. PROVED.** sup_{B_q} F_T = λ, and F_T(y) = λ for some y ∈ B_q iff q(y) = 1 and
‖Ty‖ = λp(y); hence T attains its p-norm iff F_T attains its supremum on B_q. If L is compact,
F_T**(ξ) = ‖T**ξ‖ − λ‖L**ξ‖ is weak*-continuous on B_{q**}, attains its maximum λ there, and its
maximisers are exactly the ξ ∈ B_{q**} with q**(ξ) = 1 and ‖T**ξ‖ = λp**(ξ).

*Proof.* For y ∈ B_q: ‖Ty‖ ≤ λq(y) + λ‖Ly‖ ≤ λ + λ‖Ly‖. Choose x_n ∈ S_p with ‖Tx_n‖ → λ and
y_n = x_n/q(x_n): F_T(y_n) = λ + (‖Tx_n‖ − λ)/q(x_n) → λ because q(x_n) ≥ 1/(1+‖L‖). If F_T(y) = λ
then λ ≤ λq(y) forces q(y) = 1 and ‖Ty‖ = λp(y); the converse is immediate. T** is weak*-continuous
(finite rank), L** is weak*-to-norm on bounded sets (2.2); Goldstine gives sup_{B_{q**}} = λ; the
characterisation of maximisers is the same computation in X**. ∎

So density of NA((X,p),F) is equivalent to: *the set of T whose function F_T** has a maximiser in
B_q (rather than in B_{q**} \ B_q) is dense.* This is a Bishop–Phelps statement for a specific
family of weak*-continuous DC functions on a weak*-compact convex set. Let Θ = (T**,L**) : X** → F × V
and K = Θ(B_{q**}), Ψ(e,v) = ‖e‖ − λ‖v‖; then max_{B_{q**}} F_T** = max_K Ψ.

**Lemma 5.2. PROVED.** Every maximiser k of Ψ over K is radially extreme: (1+ε)k ∉ K for all
ε > 0. In particular, when K is finite-dimensional, maximisers lie on the relative boundary of K.

*Proof.* Ψ is positively homogeneous and max_K Ψ = λ > 0, so Ψ((1+ε)k) = (1+ε)λ > λ when
Ψ(k) = λ. For finite-dimensional symmetric convex K, 0 ∈ ri K and (1+ε)k ∈ K for every k ∈ ri K
and small ε. ∎

**Lemma 5.3 (finite-rank L). PROVED.** If V is finite-dimensional (L finite rank) then for any
(X,q): Θ(B_q) ⊇ ri K.

*Proof.* Θ is weak*-continuous on X** (adjoint of a finite-rank map into X*), and B_q is weak*-dense
in B_{q**} (Goldstine), so the convex set Θ(B_q) is dense in the compact convex set K ⊂ F × V. In
finite dimensions a convex set with the same closure as K contains ri K (Rockafellar, Thm 6.3). ∎

**Corollary 5.4. PROVED.** For finite-rank L, T fails to attain iff no maximiser of Ψ on rbd K lies
in Θ(B_q). At a maximiser k_0 = Θ(ξ) (so q**(ξ) = 1) with e* ∈ S_{F*} norming T**ξ, the concave
continuous function G(e,v) = e*(e) − λ‖v‖ satisfies G ≤ Ψ ≤ λ on K and G(k_0) = λ, so G attains its
maximum over K at k_0. The convex optimality condition (sum rule for the continuous convex −G and the
indicator of K) gives v_0* ∈ ∂‖·‖(L**ξ) such that ℓ = (e*, −λv_0*) attains its maximum over K at
k_0. Its pull-back ℓ∘Θ = T*e* − λL*v_0* lies in X*; since T*e* = λf_0 with f_0 ∈ S_{p*} normed by
ξ/p**(ξ), and (if V is smooth at L**ξ) v_0* is the forced block part of f_0, we get ℓ∘Θ = λa with a
the forced base part of the maximal row f_0. So for finite-rank L the obstruction to attainment is
located in the base part only; cf. the "frozen block part" construction §11.10.

**Proposition 5.5 (upper semicontinuity of maximisers). PROVED.** If L is compact, T_n → T in
L(X,F) (F finite-dimensional) and ξ_n ∈ B_{q**} maximise F_{T_n}**, then every weak*-cluster point of
(ξ_n) maximises F_T**. In particular, if f ∈ S_{p*} has a unique normer ξ and g ∈ C(f), ρ < 1, the
normers x_n of any NA approximants T_n of (f,ρg) satisfy x_n/q(x_n) → ±ξ/q**(ξ) weak* (after fixing
signs).

*Proof.* |F_{T_n}**(η) − F_T**(η)| ≤ (1+‖L‖)(‖T_n − T‖_p + |λ_n − λ|‖L‖) uniformly for η ∈ B_{q**};
combine with weak*-continuity of F_T**. For T = (f,ρg): g ∈ C(f) gives f(η)² + g(η)² ≤ p**(η)² on X**
(Goldstine with norms), so ‖T**η‖² ≤ p**(η)² − (1−ρ²)g(η)², and equality ‖T**η‖ = p**(η) forces
g(η) = 0 and |f(η)| = p**(η), i.e. η ∈ ℝξ. ∎

**What (b) does not give.** For infinite-rank L (Martín) K is an infinite-dimensional compact convex
set; Θ(B_q) is a dense convex subset of K, but by Lemma 5.2 maximisers are radially extreme points of
K, and a dense convex subset of an infinite-dimensional compact convex set need not contain any
prescribed radially extreme point. Lemma 5.3 has no infinite-dimensional analogue, and I found no
general mechanism that pushes the maximiser into B_q by a small perturbation of T (see §8).

---------------------------------------------------------------------------------------------------

## 6. Mechanism (c): renorming the range

In the primal transfer theorem (Preprint B, Thm 4.3) the enlargement B_p = B_q + U(B_G) is absorbed
into the convex inner parallel body D = {v : v + C(B_G) ⊂ B_E} of the range. For the dual sum the
analogous condition ‖Tx‖ − ‖Lx‖ ≤ q(x) describes the set {(e,v) : ‖e‖ − ‖v‖ ≤ 1}, which is **not
convex**; this is the basic obstruction. The best convex substitute is a selection seminorm.

**Proposition 6.1 (selection seminorm). PROVED.** Let ‖T‖_p = 1. For e* ∈ B_{F*} choose
σ(e*) ∈ B_{V*} with q*(T*e* − L*σ(e*)) ≤ 1 (possible by 2.1), with σ odd. Let Γ be the weak*-closure
of {(e*, −σ(e*)) : e* ∈ B_{F*}} in F* × V* and ν(e,v) = sup_{(e*,u*) ∈ Γ} (e*(e) + u*(v)). Then
(i) ν is a continuous seminorm on F ⊕ V with ‖e‖ − ‖v‖ ≤ ν(e,v) ≤ ‖e‖ + ‖v‖;
(ii) S = (T,L) satisfies ν(Sx) ≤ q(x) and ‖S‖_{q→ν} = 1;
(iii) if T' satisfies ν(T'x, Lx) ≤ q(x) for all x, then ‖T'‖_p ≤ 1; if moreover ν(T'x_0, Lx_0) = q(x_0)
is attained at (e_0*,u_0*) ∈ Γ with u_0*(Lx_0) = −‖Lx_0‖ ("tightness"), then T' attains its p-norm at
x_0.

*Proof.* (i) Γ is weak*-compact and symmetric (σ odd), so ν is a continuous seminorm; taking
(e*, −σ(e*)) with e* norming e gives ν(e,v) ≥ ‖e‖ − ‖v‖. (ii) For (e*,u*) = lim(e_α*, −σ(e_α*)):
e*(Tx) + u*(Lx) = lim (T*e_α* − L*σ(e_α*))(x) ≤ q(x); ‖S‖ ≥ sup_x(‖Tx‖ − ‖Lx‖)/q(x) = 1 by 5.1.
(iii) ‖T'x‖ ≤ ν(T'x,Lx) + ‖Lx‖ ≤ p(x); under tightness ‖T'x_0‖ ≥ e_0*(T'x_0) = q(x_0) + ‖Lx_0‖. ∎

**6.2 Why this route fails (HEURISTIC; the reduction itself is PROVED).** To use density for the
base one would approximate S by NA operators S' = (T',L') : (X,q) → (F ⊕ V, ν). Two defects:
(1) L' ≠ L in general, and then (iii) only gives ‖T'‖_{p'} ≤ 1 for the *different* norm
p' = q + ‖L'·‖ (and for infinite-rank L the range F ⊕ V is infinite-dimensional, so base density is
not even applicable); (2) even then, attainment of S' happens at some (e_0*,u_0*) ∈ Γ which need not
be tight, since σ was chosen without reference to the (unknown) attainment point. Freezing the
second component (L' = L) is a fixed-row approximation problem; its Euclidean instance fails already
for the canonical base (Prop. 4.3). I see no way to choose σ adaptively. Conclusion: range renorming
transfers only *split* information (if σ can be taken linear, T ∈ SC), consistent with §3.

---------------------------------------------------------------------------------------------------

## 7. Mechanism (d): the graph in (X,q) ⊕_1 V

**Proposition 7.1. PROVED ((iv) mod. 3.3).** Let Z = (X,q) ⊕_1 V and J : (X,p) → Z, Jx = (x,Lx), an
isometric embedding onto the graph G.
(i) T ∈ L((X,p),F) has an extension T̃ ∈ L(Z,F) with ‖T̃‖ = ‖T‖_p iff T ∈ ‖T‖_p·SC.
(ii) If NA((X,q),F) and NA(V,F) are dense, NA(Z,F) is dense. (For Martín: V is an ℓ_1-sum of
renormings of ℓ_1, so has the RNP and NA(V,F) is dense by Bourgain; NA((c_0,q),F) is dense.)
(iii) If T̃ ∈ L(Z,F) attains its norm at a point of S_Z ∩ G, then T̃∘J ∈ NA((X,p),F) ∩ ‖T̃‖·SC.
(iv) In Martín's space G is not 1-complemented in Z.

*Proof.* (i) ‖T̃‖ = max(‖T̃|_X‖_q, ‖T̃|_V‖) and T̃∘J = T̃|_X + T̃|_V∘L; conversely S + ΦL extends by
(x,v) ↦ Sx + Φv. (ii) For T̃ = (A,B) with ‖A‖ ≥ ‖B‖ approximate A by A' ∈ NA with ‖A'‖ = ‖A‖ and keep
B (or symmetrically). (iii) is (i) plus the definition. (iv) A norm-one projection onto G would give
isometric extensions of all operators on G, so every contraction would be split, contradicting 3.3. ∎

Hence (d) produces exactly the split NA operators of Lemma 3.1, which are not dense (3.3).

---------------------------------------------------------------------------------------------------

## 8. Mechanism (e): variational principles (obstruction analysis, HEURISTIC)

* **Ekeland** on the complete metric space B_q applied to −F_T yields x_ε ∈ B_q with
  F_T(x_ε) ≥ λ − ε and F_T(x) ≤ F_T(x_ε) + ε‖x − x_ε‖ on B_q. In Bishop–Phelps one converts the cone
  condition into a supporting *linear* functional by separating the convex set B_q from an open cone;
  here F_T = ‖T·‖ − λ‖L·‖ is a difference of convex functions and its super-level sets are not convex,
  so there is nothing to separate. A perturbation T' = T + R has to dominate ε‖x − x_ε‖ by
  F_{T'} − F_T, which is not available from linear R.
* **Stegall's variational principle (dual form)** perturbs weak*-usc functions on weak*-compact
  convex sets K ⊂ W* by elements of W and needs W Asplund. Here K = B_{q**}, W = X* = ℓ_1, which is not
  Asplund; and even when it applies it produces maximisers in K = B_{q**}, while attainment needs a
  maximiser in B_q (Prop. 5.1).
* **Bourgain–Stegall** in X needs the RNP of X = c_0: fails.
* **Concrete obstruction.** To make some x ∈ B_q beat the bidual maximiser ξ one needs a perturbation
  φ with φ(x) − φ(ξ) ≥ F_T**(ξ) − F_T(x) =: δ(x). δ(x) is small only if x is weak*-close to ξ along
  T*(F*) and *uniformly* along the compact set L*(B_{V*}) (Prop. 2.2), so φ must be nearly invisible
  to T and L while separating x from ξ. Such φ exist, but after perturbation new bidual maximisers
  appear (Prop. 5.5 only says they stay weak*-close to ξ), and controlling them is the original problem.

No theorem is claimed in this section.

---------------------------------------------------------------------------------------------------

## 9. Mechanism (f): truncation, permanence and finite-rank reductions

Preprint B's permanence theorem needs p = q_η + s_η with q_η a norm, s_η a *seminorm*, s_η ≤ ηq_η, and
d_{q_η}(T) → 0. The tail-block truncation p = p_N + Σ_{m>N}|R_m·|_m is of this form (Remark
martin-tail) because the block norms are added in ℓ_1-fashion. Inside a block nothing similar works:

**Lemma 9.1. PROVED.** Let ν be a norm on a real vector space Z, P a linear projection on Z, x_0 ∈ ran P
and y ∈ ker P with ν(y) > 0, and assume ν is Gateaux differentiable at x_0 in the direction y
(ν'(x_0; −y) = −ν'(x_0; y)). Then φ = ν − ν∘P is not convex.

*Proof.* φ(y) = ν(y) > 0. Since P(±Rx_0 + y) = ±Rx_0,
φ(Rx_0 + y) + φ(−Rx_0 + y) = R[ν(x_0 + y/R) − ν(x_0)] + R[ν(x_0 − y/R) − ν(x_0)] → ν'(x_0;y) + ν'(x_0;−y) = 0
as R → ∞. Convexity would give φ(y) ≤ ½(φ(Rx_0+y) + φ(−Rx_0+y)) → 0. ∎

(For ℓ_1-type norms ν = ν∘P + ν∘(I−P) the difference is a seminorm; Lemma 9.1 shows that any norm
smooth along ker P behaves in the opposite way.)

**Corollary 9.2. PROVED.** Let m be a block, K ≥ 1, P_K the coordinate projection on ℓ_1 onto the first
K coordinates, and q' = q + Σ_{m'≠m}|R_{m'}·|_{m'} + |P_K R_m ·|_m (a norm, p − q' ≥ 0). Then p − q' is not
convex on X; so within-block coordinate truncation never yields a decomposition p = q_η + s_η with
s_η a seminorm.

*Proof.* p − q' = |R_m·|_m − |P_K R_m·|_m. On ℓ_1 the norm |·|_m is Gateaux smooth off 0 (SF1); apply
Lemma 9.1 with x_0 = e_1, y = e_{K+1} to get z_1, z_2 ∈ ℓ_1 violating midpoint convexity of
ψ(z) = |z|_m − |P_K z|_m. ψ is continuous and R_m has dense range ((SF2): R_m* = T∘(diagonal) is
injective), so the violation persists for nearby z_i' = R_m x_i, whose midpoint is R_m((x_1+x_2)/2). ∎

**Corollary 9.2' (no pointwise lift either). PROVED.** With s := p − q' = |R_m·|_m − |P_K R_m·|_m as in
9.2, the largest seminorm σ on X with σ ≤ s is σ = 0. Hence the pointwise form of the lift lemma
(which only needs h ∈ X* with |h| ≤ s and h(z_0) = s(z_0) at the attainment point z_0) is unavailable
at every z_0 with s(z_0) > 0.

*Proof.* Let σ ≤ s be a seminorm (continuous, as σ ≤ p) and x ∈ X, z = R_m x. For x_n ∈ X and R > 0,
σ(x) ≤ ½(σ(Rx_n + x) + σ(−Rx_n + x)) ≤ ½(ψ(R R_m x_n + z) + ψ(−R R_m x_n + z)), ψ(y) = |y|_m − |P_K y|_m.
Since R_m has dense range and ψ is continuous, we may let R_m x_n → z_0 for any z_0 ∈ ℓ_1 (the x_n may
be unbounded; only the right side is used). Take z_0 = e_1 ∈ ran P_K. Then
ψ(±Rz_0 + z) = R[|±z_0 + z/R|_m − |±z_0 + P_K z/R|_m] → ±|·|_m'(z_0; (I − P_K)z) as R → ∞ (Gateaux
smoothness at z_0, linearity of the derivative, |−y| = |y|), so σ(x) ≤ 0. ∎

Numerical illustration (N2, Appendix): for the 3-coordinate block norm with Φ = (1/2,1/4,1/8) and
K = 1: ψ(e_2) = 0.8 while ½(ψ(±R e_1 + e_2)) = 0.62, 0.57, 0.39, 0.13 for R = 1, 3, 10, 30.

**Proposition 9.3 (no norm-one finite-rank projections). PROVED (mod. Martín's theorem / Preprint B
Thm 5.7(a)).** (c_0,p) (any nonempty block set) admits no norm-one projection of finite rank ≥ 2.

*Proof.* If ‖P‖_p = 1 and rank P = r ≥ 2, every e ∈ E := P*(X*) satisfies p*(e) = sup_{P(B_p)} e =
sup_{B_p ∩ ran P} e, attained by compactness; so the r-dimensional space E lies in NA_p, contradicting
"NA_p ∩ E' is contained in two lines for every 2-dimensional E'". ∎

So the Johnson–Wolfe / Lemma-projections route (T ↦ TP_M attains when P_M is contractive) is closed.

**Theorem 9.4 (Read-type dual transfer). PROVED.** Let (X,q) admit finite-rank projections P_M
(M ∈ 𝕄 ⊂ ℕ infinite) with ‖P_M‖_q ≤ 1 and ‖R − RP_M‖_q → 0 for every finite-rank R. Let
V = (⊕_n V_n)_{ℓ_1}, L = (L_n)_n with Σ_n‖L_n‖ < ∞, and suppose every L_n is finitely supported:
L_n P_M = L_n for all large M ∈ 𝕄. Then for every Banach space F the finite-rank norm-attaining
operators are dense in the finite-rank operators on (X, q + ‖L·‖); in particular NA((X,p),F) is dense
for every finite-dimensional F.

*Proof.* q_N = q + Σ_{n≤N}‖L_n·‖. For large M, q_N(P_Mx) ≤ q(x) + Σ_{n≤N}‖L_n x‖ = q_N(x), so P_M is
q_N-contractive and RP_M attains its q_N-norm on the compact set B_{q_N} ∩ ran P_M; with
‖R − RP_M‖ → 0 this gives d_{q_N}(R) = 0. Now p = q_N + s_N, s_N = Σ_{n>N}‖L_n·‖ ≤ η_N q_N,
η_N = Σ_{n>N}‖L_n‖. If A ∈ NA((X,q_N),F) attains at z_0 ∈ S_{q_N} and h ∈ X* satisfies |h| ≤ s_N,
h(z_0) = s_N(z_0) (Hahn–Banach), then A' = A + h ⊗ Az_0 satisfies ‖A'z‖ ≤ ‖A‖(q_N(z) + s_N(z)) = ‖A‖p(z),
‖A'z_0‖ = ‖A‖p(z_0), and ‖A' − A‖_{q_N} ≤ η_N‖A‖_{q_N}. As p ≤ (1+η_N)q_N, operator norms for p and
q_N differ by a factor ≤ 1+η_N, so d_p(R) ≤ (1+η_N)d_{q_N}(R) + η_N(1+η_N)‖R‖ → 0. ∎

This is Preprint B's argument for Read's space (q = ‖·‖_∞, V_n = ℝ, L_n = r_n v_n, v_n ∈ c_00) in
abstract form. It isolates what fails for Martín: L_n = R_m is never finitely supported
(R_m*(V_m*) ⊂ Y and Y ∩ c_00 = {0}), and Corollary 9.2 shows that the obvious finite-rank truncations
inside a block do not produce admissible decompositions. (The canonical DGS base need not have
contractive coordinate projections either, but that defect alone is harmless: "Read-type perturbation
first, DGS smoothing second" is covered by Thm 9.4 followed by the primal transfer theorem.)

**9.5 OPEN.** Whether a Martín block admits *some* exact decomposition |R_m·|_m = ν∘A + s with A of
finite rank, ν a norm and s ≤ ηq a seminorm. Dually: R_m*(B_{N_m}) = K_1 + K_2 with K_1 contained in a
finite-dimensional subspace and K_2 ⊂ ηB_{q*} (Minkowski summands). Lemma 9.1 excludes the coordinate
choices; general summands are not excluded by anything I proved.

**9.6 OPEN.** Dual transfer for finite-rank L in general. Even a positive answer would not settle
Martín's space unless 9.5 has a positive answer. Partial structure: Cor. 5.4, §11.10.

---------------------------------------------------------------------------------------------------

## 10. Positive abstract results

### 10.1 Abstract global compactness and residual recovery

**Hypothesis (A1).** X is separable and there is a norm N on X* with c‖·‖ ≤ N ≤ C‖·‖ (c > 0) such that
for every a ∈ X* and every bounded weak*-null sequence (d_n) ⊂ X*:  q*(a + d_n) − q*(a) − N(d_n) → 0.

**Lemma 10.0. PROVED.** The canonical base satisfies (A1) with N = ‖·‖_1.

*Proof.* Given ε, choose K with Σ_{j>K}|a_j| < ε. Coordinatewise d_n → 0, so
Σ_{j≤K}|a_j + d_{n,j}| → Σ_{j≤K}|a_j| and Σ_{j≤K}|d_{n,j}| → 0, while
|Σ_{j>K}|a_j + d_{n,j}| − Σ_{j>K}|d_{n,j}|| ≤ ε. Hence ‖a + d_n‖_1 = ‖a‖_1 + ‖d_n‖_1 + O(ε) + o(1).
U* is weak*-to-weak continuous (adjoint of U : H → c_0, H reflexive) and compact, so U*d_n → 0 in norm
and ‖U*(a + d_n)‖ → ‖U*a‖. Finally ‖·‖_1 ≤ q* ≤ (1 + ‖U‖)‖·‖_1. ∎

**Theorem 10.1 (global compactness). PROVED.** Assume (A1) and L compact. If f_n → f in S_{p*} and
g_n ∈ C(f_n), then (g_n) has a norm-convergent subsequence and every limit lies in C(f). Hence every
C(f) is norm compact, ⋃_n C(f_n) ∪ C(f) is relatively compact, and f ↦ C(f) is upper semicontinuous.
The same holds for the joint fibres C_d(f) = {(g_1,…,g_d) : f(y)² + Σ_j g_j(y)² ≤ p(y)² ∀y}.

*Proof (Preprint A's argument, with (A1) isolating what is used).* p*(g_n) ≤ 1, so pass to a weak*
convergent subsequence g_n → g; weak*-lsc of p* gives p*(f + tg) ≤ liminf p*(f_n + tg_n) ≤ √(1+t²),
i.e. g ∈ C(f). Let ξ be a normer of f, q_0 = q**(ξ) > 0, so g(ξ) = 0 and ‖L**ξ‖ = 1 − q_0. Let
D = limsup‖g_n − g‖ and pass to a subsequence realising it. Fix t > 0, s = √(1+t²); by 2.1,
f_n + tg_n = a_n + k_n with q*(a_n) ≤ s, k_n ∈ sL*(B_{V*}). By compactness k_n → k in norm along a
further subsequence; then a_n → a := f + tg − k weak*, and a_n − a = (f_n − f) + t(g_n − g) − (k_n − k).
By (A1), q*(a_n) = q*(a) + N(a_n − a) + o(1) = q*(a) + tN(g_n − g) + o(1). Evaluating at ξ:
q_0 q*(a) ≥ a(ξ) = 1 − k(ξ) ≥ 1 − s(1 − q_0), so q*(a) ≥ (1 − s + sq_0)/q_0 and
t·limsup N(g_n − g) ≤ s − q*(a) ≤ (s − 1)/q_0 ≤ t²/(2q_0). Letting t → 0 gives N(g_n − g) → 0. The
remaining assertions are routine (a sequence in ⋃C(f_n) either has infinitely many terms in one
compact C(f_n) or the theorem applies to a subsequence). For C_d apply the result to each row. ∎

**Corollary 10.1' (abstract residual recovery). PROVED.** Assume (A1), L compact, X* separable. There
is a dense G_δ set Ω ⊂ S_{p*} such that for f ∈ Ω and every d, C_d is Hausdorff continuous at f, and
(f,G) ∈ cl NA((X,p),ℓ_2^{d+1}) for all G ∈ C_d(f).

*Proof.* As in Preprint A, Thm 2.4: for a countable dense set (z_j) ⊂ (X*)^d, the functions
f ↦ dist(z_j, C_d(f)) are lower semicontinuous by 10.1, hence continuous on a common dense G_δ
(points of continuity of Baire-one functions on the complete metric space S_{p*}); at such f the
correspondence is lower semicontinuous; Bishop–Phelps gives NA f_n → f and (f_n,G_n) attains by
Prop. 2.4(ii). ∎

**Proposition 10.1'' (finite test vectors). PROVED.** Assume (A1), L compact. Write σ_h(x) =
sup_{g∈C(h)} g(x) (a seminorm ≤ p). Let f ∈ S_{p*} and ρ ∈ (0,1). If for every ε > 0 and every finite
set x_1,…,x_k ∈ X there is f' ∈ NA_p ∩ S_{p*} with ‖f' − f‖ < ε and σ_{f'}(x_i) ≥ ρσ_f(x_i) − ε for all
i, then {f} × ρC(f) ⊂ cl NA((X,p),ℓ_2^2).

*Proof.* Diagonalise over a countable dense set (x_i) to get NA f_n → f with
liminf_n σ_{f_n}(x_i) ≥ ρσ_f(x_i) for all i, hence for all x (all σ_h are p-Lipschitz). By 10.1 the
sets C(f_n) lie in a fixed compact set, so by Blaschke's theorem every subsequence has a further
subsequence with C(f_{n_k}) → C' in the Hausdorff metric; then σ_{C'} = lim σ_{f_{n_k}} ≥ ρσ_f on X,
and since C' is convex and weak*-compact, Hahn–Banach separation by elements of X gives
ρC(f) ⊂ C'. Hence dist(ρg, C(f_n)) → 0 for each g ∈ C(f), and (f_n, g_n) ∈ NA by 2.4(ii). ∎

### 10.2 Hilbert block spaces: bounded lifts

**Proposition 10.2. PROVED.** Let V be a Hilbert space, (X,q) arbitrary, L bounded. Let f ∈ S_{p*}
with normer ξ, q_0 = q**(ξ) ∈ (0,1), w = L**ξ/‖L**ξ‖, and g ∈ X* with g(ξ) = 0. Let t ∈ ℝ,
s = √(1+t²), σ = s − 1, r = q_0/(1 − q_0), and suppose f + tg = A + L*W with q*(A) ≤ s, ‖W‖ ≤ s.
Write W = (1+θ)w + Δ with Δ ⊥ w. Then −σr ≤ θ ≤ σ and, if σr ≤ 1,
‖Δ‖² ≤ 2σ/(1 − q_0) + σ²(1 − r²). In particular ‖W − w‖ ≤ |t|/√(1−q_0) + O(t²) for *every* admissible
decomposition.

*Proof.* A(ξ) = (f + tg)(ξ) − ⟨W, L**ξ⟩ = 1 − (1+θ)(1 − q_0), and A(ξ) ≤ q*(A)q_0 ≤ sq_0; this gives
θ ≥ −σr. ‖W‖ ≥ 1 + θ gives θ ≤ σ. Then ‖Δ‖² ≤ s² − (1+θ)² ≤ (1+σ)² − (1 − σr)² =
2σ(1+r) + σ²(1 − r²), and 1 + r = 1/(1 − q_0). Finally σ ≤ t²/2. ∎

So for Hilbert V there is no "lift blow-up" in the block component: Preprint A's phenomenon
(Prop. 3.4 there) is caused by the geometry of Martín's V*, not by compactness of L.
**Remark (why Martín's V* differs). PROVED.** In V_m*, with w = w_m, J the normalised R_m**ξ
(J = α + D²w/C with α on the peak set), and an off-peak coordinate k:
N_m(w + ce_k) − (w + ce_k)(J) = ‖D(w + ce_k)‖ − ⟨D w, D(w+ce_k)⟩/C = O(c²Φ_m(k)²) for
|c| ≤ M − |w(k)|, while ‖ce_k‖_{V*} ≈ |c|. The modulus of rotundity of B_{V_m*} at w in direction e_k
degenerates like Φ_m(k)² as k → ∞; this is exactly what permits block lifts W(t) − w of size ≫ |t|.

**Proposition 10.2' (first-order structure of mates, Hilbert V, canonical base). SKETCH.** In the
setting of 10.2 with the canonical base and a = forced base part, ξ̂ = z + U(U*a/‖U*a‖): for every
g ∈ C(f) there are v_± ∈ V with ⟨v_±, w⟩ = 0 such that b_± := g − L*v_± satisfy b_±(ξ̂) = 0 and
Σ_{j∉supp a}(|b_{±,j}| ∓ z_j b_{±,j}) = 0, i.e. off supp a the vector b_± lives on {j : |z_j| = 1} with
sign ±z_j ("two-sided split to first order").

*Sketch.* Take admissible decompositions at t_n → 0±, put v_t = (W(t) − w)/t (bounded by 10.2), take
weak limits v_±; b_t = g − L*v_t → b_± in norm (L* compact). Convexity gives
q*(A(t)) ≥ 1 + q*'(a; tb_t) with q*'(a;y) = y(ξ̂) + Σ_{j∉supp a}(|y_j| − z_j y_j). Since
tb_t(ξ̂) = −t⟨v_t,w⟩(1−q_0)/q_0 and 2t⟨v_t,w⟩ ≤ t² (from ‖w + tv_t‖ ≤ s), one gets
K_t := Σ_{j∉supp a}(|b_{t,j}| − sign(t) z_j b_{t,j}) ≤ |t|/(2q_0), and |⟨v_t,w⟩| = O(|t|). K is
‖·‖_1-continuous, so K(b_±) = 0, and ⟨v_±,w⟩ = 0. ∎
What is *not* obtained: second-order bounds q*(a + tb_±) ≤ 1 + O(t²) — norm convergence b_t → b_±
controls only first-order behaviour. Hence even for Hilbert V I cannot prove that every mate is
locally split (§12).

### 10.3 Second-order calculus for dual Minkowski sums

**Proposition 10.3 (parallel sum). SKETCH (smooth finite-dimensional case; numerically confirmed).**
Let K_1, K_2 ⊂ ℝ^n be convex bodies with C² boundaries of positive curvature, B = K_1 + K_2, f = a + k
with a ∈ ∂K_1, k ∈ ∂K_2 sharing the outer normal ξ normalised by f(ξ) = 1, and q_0 = h_{K_1}(ξ). For
y with y(ξ) = 0 let A(y), B(y) be the second derivatives at t = 0 of gauge_{K_1}(a + ty) and
gauge_{K_2}(k + ty). Then for g with g(ξ) = 0

    d²/dt² gauge_B(f + tg)|_{t=0} = inf { q_0 A(b) + (1−q_0) B(c) : b + c = g, b(ξ) = c(ξ) = 0 },

the parallel sum of q_0A and (1−q_0)B. *Upper bound (rigorous for smooth gauges):* use
f + tg = (a + tb + θt²e) + (k + tc − θt²e) with e(ξ) = 1 and optimise θ: the second-order terms are
A(b)/2 + θ/q_0 and B(c)/2 − θ/(1−q_0) (first derivatives of the gauges at a, k in direction e are
e(ξ)/q_0 and e(ξ)/(1−q_0)), and equalising gives (q_0A(b) + (1−q_0)B(c))/2. *Equality:* Hessians of
support functions add, and the gauge Hessian on the tangent space is the inverse of the support
function Hessian (suitably normalised); I did not write this out. Numerics N1 (Appendix): agreement
to all printed digits in dimensions 2 and 3, while the "max-split" value
inf_{b+c=g} max(A(b), B(c)) is strictly larger.

Consequences. (i) The infinitesimal mate set of f is (heuristically) the parallel-sum ellipsoid,
which strictly contains the split set {A ≤ 1} + {B ≤ 1}; certificates that only use the max-combination
(Def. 10.4) miss part of C(f) at second order. (ii) **HEURISTIC (10.3').** In Martín's space with
a ∈ c_00, every shifting direction e ∈ L*(V*) \ {0} has infinite support (Y ∩ c_00 = {0}), so the base
pays an extra kink cost |θ|t² Σ_{j∉supp a}(|e_j| − sign(θ) z_j e_j) for shifting; the effective local
form is a *kink-corrected* parallel sum. Shifted certificates (curves A_t = a + tb + t²c) are
compatible with Theorem 10.4 (whose proof only uses an explicit decomposition at each t), but I verify
the recovery hypotheses only for unshifted ones.

### 10.4 Certificates and the conditional dual transfer theorem

Fix f ∈ S_{p*}, a normer ξ, ξ̂ = ξ/q**(ξ), and the decomposition f = a + L*w of §2.

**Standing hypothesis (S).** V is smooth at L**ξ, so w = J_V(L**ξ) is unique; consequently, as
x' → ξ̂ weak* with x' ∈ S_q, J_V(Lx') → w weak* (norm-to-weak* continuity of the duality map at points
of smoothness, plus Lx' → L**ξ̂ in norm by 2.2) and L*J_V(Lx') → L*w in norm (L* compact).

**Definition 10.4 (split certificate; margin).** A split certificate for g ∈ X* at f with constants
(τ, κ) is a pair (b,v) ∈ X* × V* with g = b + L*v and

    q*(a + tb) ≤ 1 + κt²/2   and   ‖w + tv‖ ≤ 1 + κt²/2     for |t| ≤ τ.

g has global margin ρ_0 < 1 if p*(f + tg) ≤ √(1 + ρ_0²t²) for all t ∈ ℝ.

**Recovery hypotheses for a class 𝒞 of split certificates at f.**
(H_base) For each (b,v,τ,κ) ∈ 𝒞 and κ' > κ there is τ_b > 0 such that for every ε > 0 and every
weak*-neighbourhood W of ξ̂ in B_{q**} there exist a' ∈ NA_q ∩ S_{q*}, x' ∈ S_q ∩ W with a'(x') = 1,
and b' ∈ X*, with ‖a' − a‖ < ε, ‖b' − b‖ < ε and q*(a' + tb') ≤ 1 + κ't²/2 for |t| ≤ τ_b.
(H_V) For each (b,v,τ,κ) ∈ 𝒞 and κ' > κ there is τ_V > 0 such that for every ε > 0 there is a
weak*-neighbourhood W' of ξ̂ such that for every x' ∈ S_q ∩ W' there is v' ∈ V* with
‖L*(v' − v)‖ < ε and ‖J_V(Lx') + tv'‖ ≤ 1 + κ't²/2 for |t| ≤ τ_V.

**Theorem 10.4 (conditional dual transfer). PROVED.** Assume (S), (H_base), (H_V) for 𝒞. If g has a
certificate in 𝒞 with κ < 1 and g has global margin ρ_0 < 1, then (f,g) ∈ cl NA((X,p),ℓ_2^2).

*Proof.* Fix κ' ∈ (κ,1) and τ_1 = min(τ_b, τ_V, 2√(1−κ'), 1). Since √(1+u) ≥ 1 + u/2 − u²/8,
1 + κ't²/2 ≤ √(1+t²) for |t| ≤ τ_1. Put η = min_{|t|≥τ_1} [√(1+t²) − √(1+ρ_0²t²)]/(1+|t|) > 0
(continuous, positive, limit 1 − ρ_0 at infinity). Let ε ∈ (0, η/4). Take W' from (H_V), shrink it so
that ‖L*(J_V(Lx') − w)‖ < ε for x' ∈ S_q ∩ W' (hypothesis (S)), and apply (H_base) with W = W' to get
a', x', b'; then (H_V) gives v'. Put w' = J_V(Lx'), f' = a' + L*w', g' = b' + L*v'. Then:
(i) f' ∈ NA_p ∩ S_{p*}, attaining at x'/p(x') (Prop. 2.3); ‖f' − f‖_{p*} ≤ ‖a'−a‖ + ‖L*(w'−w)‖ < 2ε
(note p* ≤ q*); ‖g' − g‖_{p*} < 2ε.
(ii) For |t| ≤ τ_1: f' + tg' = (a' + tb') + L*(w' + tv'), so by 2.1
p*(f' + tg') ≤ max(q*(a'+tb'), ‖w'+tv'‖) ≤ 1 + κ't²/2 ≤ √(1+t²).
(iii) For |t| ≥ τ_1: p*(f' + tg') ≤ p*(f + tg) + 2ε(1 + |t|) ≤ √(1+ρ_0²t²) + η(1+|t|)/2 ≤ √(1+t²).
So g' ∈ C(f'), (f',g') attains its norm (2.4(ii)), and ‖(f',g') − (f,g)‖ < 4ε. ∎

**Lemma 10.5 (linear-radius criterion). PROVED.** Let g ∈ C(f), ρ_1 ∈ (0,1), κ_0 < 1. Suppose there
are g_ε with ‖g_ε − ρ_1 g‖_{p*} ≤ ε, each having a split certificate (b_ε, v_ε) with constants
(τ_ε, κ_0), where liminf_{ε→0} τ_ε/ε > 2√2/(1 − ρ_1²). Then for small ε, g_ε has global margin
ρ_2 < 1 (for suitable ρ_2), so if the certificates belong to a class satisfying (H_base), (H_V), then
(f, ρ_1 g) ∈ cl NA.

*Proof.* Choose ρ_2 ∈ (max(ρ_1, √κ_0), 1) with (ρ_2² − ρ_1²)·liminf(τ_ε/ε) > 2√2, and
τ_* = min(τ_ε, 2√(ρ_2² − κ_0), 1). For |t| ≤ τ_*, p*(f + tg_ε) ≤ 1 + κ_0t²/2 ≤ √(1 + ρ_2²t²). For
|t| ≥ τ_*, p*(f + tg_ε) ≤ √(1+ρ_1²t²) + ε|t| and by (2.5) the difference
√(1+ρ_2²t²) − √(1+ρ_1²t²) ≥ (ρ_2²−ρ_1²)|t|·|t|/(2√(1+t²)) ≥ (ρ_2² − ρ_1²)|t|τ_*/(2√2) ≥ ε|t| for small ε
(if τ_* = τ_ε by the choice of ρ_2; otherwise because τ_* is then a fixed positive number). ∎

The constant matters: the linear-radius criterion is exactly where "rates" enter (§12).

---------------------------------------------------------------------------------------------------

## 11. Martín's space: verification of the hypotheses and unconditional consequences

Throughout: canonical base, Martín's p with nonempty block set I (finite, i.e. p_J, or I = ℕ),
f ∈ S_{p*}, ξ a normer of f (unique if p** is strictly convex, but uniqueness is never used below),
ξ̂ = ξ/q**(ξ) = z + U h_0 with h_0 = U*a/‖U*a‖, z ∈ B_{ℓ_∞}, z_j = sign a_j on supp a, and the
decomposition f = a + L*w, w = (w_m)_m, w_m = J_m(R_m**ξ), N_m(w_m) = 1, M_m = ‖w_m‖_∞,
C_m = ‖D_m w_m‖_2 > 0, M_m + C_m = 1, M_m > 0.

**11.1 (S) holds. PROVED.** All blocks R_m**ξ are nonzero (SF2) and each |·|_m is smooth (SF1), so V
is smooth at L**ξ and w is unique.

**11.2 The class 𝒞_fin.** Split certificates (b, v, τ, κ) at f such that
* b = b_0 + βa with b_0 ∈ c_00, supp b_0 ⊂ supp a, β ∈ ℝ (then the certificate forces
  b(ξ̂) = 0, i.e. β = −b_0(ξ̂));
* v_m = 0 for m outside a finite set I_0, and for m ∈ I_0: v_m = ω_m − d_m w_m with ω_m ∈ c_00,
  |w_m(k)| < M_m on supp ω_m, and d_m = ⟨D_m w_m, D_m ω_m⟩/C_m (the certificate forces this d_m:
  the first-order term of N_m(w_m + t(ω_m − c w_m)) is −c + ⟨D_m w_m, D_m ω_m⟩/C_m).

For later use: for m ∈ I_0 and small |t|,
N_m(w_m + t v_m) = (1 − d_m t)M_m + ‖(1 − d_m t)D_m w_m + tD_m ω_m‖ = 1 + H_m t²/2 + O(t³),
H_m = (‖D_m ω_m‖² − d_m²)/C_m   (direct expansion, using M_m + C_m = 1; this is Preprint A's H).

**Lemma 11.3 ((H_base) for 𝒞_fin). PROVED.**

*Proof.* Let b = b_0 + βa satisfy q*(a + tb) ≤ 1 + κt²/2 on |t| ≤ τ, and κ' > κ. For N ≥ N_0 :=
max supp b_0 put c_N = q*(P_N a) → 1, a_N = P_N a/c_N, h_N = U*a_N → U*a ≠ 0,
x_N = P_N z + U(h_N/‖h_N‖). Then q(x_N) ≤ 1 and a_N(x_N) = ‖a_N‖_1 + ‖U*a_N‖ = 1 (z_j = sign a_j on
supp a_N), so a_N ∈ NA_q ∩ S_{q*} attains at x_N ∈ S_q; x_N → ξ̂ weak* (bounded, coordinatewise in
ℓ_∞, plus norm convergence of the U-part); ‖a_N − a‖ → 0. Put β_N = b_0(x_N) → b_0(ξ̂) = −β and
b' = b_0 − β_N a_N, so ‖b' − b‖ = ‖β_N a_N + βa‖ → 0.
Let s_0 = min_{j∈supp b_0} |a_j|/(2|b_{0,j}|) and, for |s| ≤ s_0 and N large (|a_{N,j}| ≥ |a_j|/2 on
supp b_0), φ(s) := q*(a + s b_0) and φ_N(s) := q*(a_N + s b_0). No coordinate changes sign, so
φ(s) = 1 + s b_0(ξ̂) + E(s), φ_N(s) = 1 + sβ_N + E_N(s), where E, E_N are the second-order remainders
of ψ(s) = ‖U*a + sU*b_0‖ and ψ_N(s) = ‖h_N + sU*b_0‖ (indeed ‖a + sb_0‖_1 = ‖a‖_1 + sΣ sign(a_j)b_{0,j},
and b_0(x_N) = Σ sign(a_j)b_{0,j} + ψ_N'(0), similarly for ξ̂). ψ_N'' → ψ'' uniformly on a fixed
interval |s| ≤ s_2 (Hilbert norms away from 0), so E_N(s) ≤ E(s) + δ_N s²/2 with δ_N → 0.
The hypothesis: q*(a + tb) = (1 + tβ)φ(t/(1+tβ)) = 1 + (1 + tβ)E(t/(1+tβ)) ≤ 1 + κt²/2 on |t| ≤ τ, i.e.
E(s) ≤ κs²/(2(1 − sβ)) for |s| ≤ s_1. The approximant: a_N + tb' = (1 − tβ_N)(a_N + s b_0) with
s = t/(1 − tβ_N), hence
q*(a_N + tb') = (1 − tβ_N)φ_N(s) = 1 + (1 − tβ_N)E_N(s)
             ≤ 1 + (κ/(2(1 − sβ)) + δ_N/2)(1 − tβ_N)s² = 1 + (κ + O(|t|) + O(δ_N) + O(|t||β_N + β|)) t²/2.
Choose τ_b = τ_b(κ'−κ, β, s_0, s_1, s_2) > 0 so that the bracket is ≤ κ' for |t| ≤ τ_b and N large. ∎

**Lemma 11.4 ((H_V) for 𝒞_fin). PROVED.**

*Proof.* Let x' ∈ S_q, x' → ξ̂ weak*; w'_m = J_m(R_m x'), C'_m, M'_m = 1 − C'_m, and for m ∈ I_0
d'_m = ⟨D_m w'_m, D_m ω_m⟩/C'_m, v'_m = ω_m − d'_m w'_m (v'_m = 0 for m ∉ I_0). Facts: R_m x' → R_m**ξ̂
in norm; w'_m → w_m weak* (smoothness); C'_m → C_m (D_m : ℓ_∞ → ℓ_2 is weak*-to-norm continuous on
bounded sets, since Φ_m ∈ ℓ_2); hence M'_m → M_m, d'_m → d_m, w'_m(k) → w_m(k) for each k, and
‖L*(v' − v)‖ ≤ Σ_{m∈I_0}‖R_m*(d_m w_m − d'_m w'_m)‖ → 0 (R_m* compact).
Let γ = min_{m∈I_0} min_{k∈supp ω_m}(M_m − |w_m(k)|) > 0. For x' close to ξ̂: |w'_m(k)| ≤ M'_m − γ/2 on
supp ω_m, |d'_m| ≤ |d_m| + 1, C'_m ≥ C_m/2. For |t| ≤ τ^(1) := γ/(4(max_m‖ω_m‖_∞ + |d_m| + 2)):
‖(1 − d'_m t)w'_m + tω_m‖_∞ ≤ (1 − d'_m t)M'_m (off supp ω_m trivially; on supp ω_m because
|t|‖ω_m‖ ≤ (1 − d'_m t)γ/2). The Hilbert part X'_m(t) = ‖(1 − d'_m t)D_m w'_m + tD_m ω_m‖ has
X'_m(0) = C'_m and X'_m'(0) = d'_m M'_m, so N_m(w'_m + tv'_m) ≤ 1 + E'_m(t), E'_m the second-order
remainder of X'_m. For the original certificate, ‖(1 − d_m t)w_m + tω_m‖_∞ = (1 − d_m t)M_m (the
supremum M_m is approached off the finite set supp ω_m), so N_m(w_m + tv_m) = 1 + E_m(t) with E_m the
remainder of X_m(t) = ‖(1 − d_m t)D_m w_m + tD_m ω_m‖, and the certificate gives E_m(t) ≤ κt²/2.
The second derivatives of X'_m converge to those of X_m uniformly on |t| ≤ τ^(2) := C_m/(4‖D_m v_m‖ + 4)
(Hilbert norm away from 0, data converging in norm), so E'_m ≤ E_m + o(1)t². Blocks m ∉ I_0
contribute N_m(w'_m) = 1. Hence ‖w' + tv'‖_{V*} ≤ 1 + κ't²/2 for |t| ≤ τ_V := min(τ, τ^(1), τ^(2)) and
x' in a weak*-neighbourhood of ξ̂ depending on ε, κ'. ∎

### 11.5 Truncation with exact first-order correction

The next two lemmas approximate *arbitrary* local split mates by members of 𝒞_fin with an error that
is **second order in t on a fixed range of t** — this is what makes the margin argument work without
any "rate" condition.

**Lemma 11.5(a) (base truncation). PROVED.** Let b ∈ ℓ_1 satisfy q*(a + tb) ≤ √(1+t²) for |t| ≤ τ.
Then b(ξ̂) = 0, supp b ⊂ supp a, and for every δ > 0 there is b'' = P_N b + β_N a (β_N = ((I−P_N)b)(ξ̂))
with b''(ξ̂) = 0, ‖b'' − b‖ < δ and q*(a + tb'') ≤ √(1+t²) + δt² for |t| ≤ τ_a, where
τ_a := min(τ, 1, ‖U*a‖/(2‖U*b‖ + 1))/2 depends only on a, b, τ (not on δ).

*Proof.* Convexity gives q*(a + tb) ≥ 1 + tb(ξ̂) + |t|Σ_{j∉supp a}(|b_j| − sign(t)z_j b_j) (formula for
q*'(a;·)); the two-sided bound ≤ 1 + t²/2 gives b(ξ̂) + Σ_off(|b_j| − z_j b_j) ≤ 0 and
−b(ξ̂) + Σ_off(|b_j| + z_j b_j) ≤ 0; adding, Σ_off|b_j| = 0, and then b(ξ̂) = 0.
Let r = (I − P_N)b, ε_N = ‖U*r‖, β_N = r(ξ̂) → 0. For |s| ≤ τ:
(ℓ_1) ‖a + sP_N b‖_1 ≤ ‖a + sb‖_1 − sΣ_{j>N} z_j r_j, because for j > N in supp a,
|a_j + sr_j| ≥ |a_j| + s sign(a_j) r_j, and r_j = 0 off supp a.
(U) With y_s = U*(a + sb) and ‖y − x‖ ≤ ‖y‖ − ⟨y,x⟩/‖y‖ + ‖x‖²/(2‖y‖):
‖U*(a + sP_N b)‖ ≤ ‖y_s‖ − s⟨h_0, U*r⟩ + C_2 s² ε_N (using ‖y_s/‖y_s‖ − h_0‖ ≤ 2|s|‖U*b‖/‖U*a‖).
Adding and using r(ξ̂) = Σ_{j>N} z_j r_j + ⟨h_0, U*r⟩:
q*(a + sP_N b) ≤ q*(a + sb) − sβ_N + C_2 s² ε_N.     (11.5.1)
Now a + tb'' = (1 + tβ_N)(a + sP_N b) with s = t/(1 + tβ_N), so
q*(a + tb'') ≤ (1 + tβ_N)√(1+s²) − tβ_N + C_3 t² ε_N = 1 + F_t(β_N) + C_3t²ε_N,
F_t(β) := √((1+tβ)² + t²) − (1 + tβ). F_t(0) = √(1+t²) − 1 and ∂_β F_t = t[(1+tβ)/√((1+tβ)²+t²) − 1] =
O(|t|³), so F_t(β_N) ≤ √(1+t²) − 1 + C|β_N||t|³. Take N large. ‖b'' − b‖ ≤ ‖r‖ + |β_N|‖a‖ → 0, and
b''(ξ̂) = b(ξ̂) − r(ξ̂) + β_N = 0. ∎

**Lemma 11.5(b) (block truncation). PROVED.** Let v ∈ V* satisfy ‖w + tv‖_{V*} ≤ √(1+t²) for |t| ≤ τ.
There is τ_3 > 0 (depending on w, v, τ only) such that for every δ > 0 there is v'' of the form in
𝒞_fin with ‖L*(v'' − v)‖ < δ, ‖w + tv''‖_{V*} ≤ √(1+t²) + δt² for |t| ≤ τ_3, and
‖w + tv''‖_{V*} ≤ ‖w + tv‖_{V*} + δ|t| for all t.

*Proof.* Blocks: replacing v_m by 0 for m ∉ I_0 keeps all inequalities (N_m(w_m) = 1) and changes L*v
by at most ‖v‖ Σ_{m∉I_0} m2^{-m}. Fix a block (drop m), w with M, C as above, and
N(w + tv) ≤ √(1+t²) on |t| ≤ τ.
*Step 1 (first-order structure).* The directional derivative of ‖·‖_∞ at w in a bounded direction y is
inf_{δ>0} sup_{|w_k| > M−δ} sign(w_k) y_k. With c = ⟨Dw, Dv⟩/C, the two-sided bound forces
limsup and liminf of sign(w_k)v_k along the near-peak set {|w_k| → M} to equal −c, and
sign(w_k)v_k = −c on the peak set. Hence ω := v + dw with d := c/M vanishes on the peak set,
ω_k → 0 along near-peak sequences, and d = ⟨Dw, Dω⟩/C (indeed ⟨Dw,Dω⟩ = cC + cC²/M = cC/M).
*Step 2 (truncation).* If some off-peak k_0 has w_{k_0} ≠ 0, fix it and γ_0 = M − |w_{k_0}| > 0 (if
every off-peak coordinate has w_k = 0, then d = 0 and no correction is needed below). For γ ∈ (0,γ_0)
and K ≥ k_0 let S = {k ≤ K : M − |w_k| ≥ γ} (finite, ∋ k_0) and
ω'' = ω1_S + c_{γ,K} e_{k_0}, c_{γ,K} = ⟨Dw, D(ω − ω1_S)⟩/(Φ_{k_0}² w_{k_0}), so ⟨Dw,Dω''⟩ = ⟨Dw,Dω⟩.
As γ → 0, K → ∞, ω − ω1_S → 0 pointwise (S^c shrinks to the peak set, where ω = 0) and boundedly; so
Δ := D(ω'' − ω) → 0 in ℓ_2, c_{γ,K} → 0, and ‖R*(ω'' − ω)‖ ≤ Σ_k |ω''_k − ω_k| mΦ(k) → 0. Put
v'' = ω'' − dw.
*Sup part:* coordinates in S \ {k_0} are unchanged; for k ∉ S, |(1−dt)w_k| ≤ |1 − dt|M ≤
‖(1−dt)w + tω‖_∞ (approach the near-peak set, where ω_k → 0); at k_0,
|(1−dt)w_{k_0} + t(ω_{k_0} + c)| ≤ |1 − dt|M for |t| ≤ t_0 := γ_0/(4(|d|M + ‖ω‖_∞ + 2)) (and |c| ≤ 1).
So the sup part does not increase for |t| ≤ t_0 and increases by at most |t||c_{γ,K}| for all t.
*Hilbert part:* with A_t = D((1−dt)w + tω), ⟨Dw, Δ⟩ = 0 gives ⟨A_t, Δ⟩ = t⟨Dω, Δ⟩, so
‖A_t + tΔ‖ ≤ ‖A_t‖ + t²(‖Dω‖‖Δ‖ + ‖Δ‖²)/‖A_t‖ ≤ ‖A_t‖ + 2t²(‖Dω‖‖Δ‖ + ‖Δ‖²)/C for
|t| ≤ t_1 := C/(2‖D(ω − dw)‖ + 2), and ‖A_t + tΔ‖ ≤ ‖A_t‖ + |t|‖Δ‖ for all t.
Adding: N(w + tv'') ≤ N(w + tv) + o(1)t² on |t| ≤ τ_3 := min(τ, t_0, t_1) and ≤ N(w + tv) + o(1)|t|
for all t. ω'' is finitely supported with gap ≥ γ > 0, so v'' is of 𝒞_fin form. ∎

### 11.6 Main unconditional consequence

**Definition.** g ∈ C(f) is *locally split* (with respect to the decomposition (a,w) of the normer ξ)
if there are τ > 0, b ∈ X*, v ∈ V* with g = b + L*v and, for |t| ≤ τ,
q*(a + tb) ≤ √(1+t²) and ‖w + tv‖_{V*} ≤ √(1+t²).

**Theorem 11.6. PROVED (mod. standing facts SF1–SF4).** Canonical base, Martín's p (any nonempty
block set I). If g ∈ C(f) is locally split, then (f,g) ∈ cl NA((c_0,p),ℓ_2^2). In particular every
norm-one split-contractive operator T = S + Φ∘L : (c_0,p) → ℓ_2^2 (‖S‖_q ≤ 1, ‖Φ‖ ≤ 1, ‖T‖_p = 1) is a
norm limit of norm-attaining operators; so the cone generated by SC ∩ S_{L((c_0,p),ℓ_2^2)} lies in
cl NA, although NA ∩ SC is not dense (Prop. 3.3).

*Proof.* Fix ρ ∈ (0,1) and ρ_2 ∈ (ρ,1). Let δ > 0 be small. Lemma 11.5(a) applied to b and Lemma
11.5(b) applied to v give b'' = P_N b + β_N a and v'' (finitely many blocks, finitely supported ω''
with positive gaps, d unchanged) with ‖b'' − b‖ + ‖L*(v'' − v)‖ < δ and, on |t| ≤ τ_5 := min(τ_a, τ_3)
(independent of δ):
q*(a + tb'') ≤ √(1+t²) + δt²,  ‖w + tv''‖ ≤ √(1+t²) + δt².
Put g'' = ρ(b'' + L*v''). Then ρb'' ∈ c_00 + ℝa with finitely supported part inside supp a, and ρv''
has the 𝒞_fin form (ρω'', with d replaced by ρd = ⟨Dw, Dρω''⟩/C), so (ρb'', ρv'') is a 𝒞_fin
certificate: for |t| ≤ τ_5/ρ both norms are ≤ √(1+ρ²t²) + δρ²t² ≤ 1 + ρ²(1+2δ)t²/2, i.e. κ = ρ²(1+2δ) < 1.
Global margin ρ_2: for |t| ≤ τ_5/ρ, p*(f + tg'') ≤ √(1+ρ²t²) + δρ²t² ≤ √(1+ρ_2²t²) by (2.5) once
δρ² ≤ (ρ_2² − ρ²)/(2√(1+τ_5²/ρ²)); for |t| ≥ τ_5/ρ, p*(f + tg'') ≤ p*(f + tρg) + |t|‖g'' − ρg‖ ≤
√(1+ρ²t²) + ρδ|t| ≤ √(1+ρ_2²t²) once ρδ ≤ (ρ_2² − ρ²)(τ_5/ρ)/(2√(1+τ_5²/ρ²)) (monotonicity of
|t|/√(1+t²)); here p*(f + tρg) ≤ √(1+ρ²t²) because g ∈ C(f). By Lemmas 11.3, 11.4 and Theorem 10.4,
(f,g'') ∈ cl NA. Let δ → 0: (f,ρg) ∈ cl NA; let ρ → 1: (f,g) ∈ cl NA.
Split operators: rotate T ∈ SC (rotations preserve SC) so that T = (f,g) with p*(f) = 1. Then
f = s_1 + L*φ_1, g = s_2 + L*φ_2 with (s_1,s_2) q-contractive and (φ_1,φ_2) V-contractive. For any
normer ξ of f, φ_1 norms L**ξ (forced decomposition, §2), so φ_1 = w by smoothness and s_1 = a; the
contractivity of the components says q*(a + ts_2) ≤ √(1+t²), ‖w + tφ_2‖ ≤ √(1+t²) for all t. ∎

**Remark 11.6'.** Since cl NA is closed, Theorem 11.6 gives (f,g) ∈ cl NA whenever g is a norm limit
of locally split mates of f, with no uniformity of their local ranges (this is Cor. 11.8). Inside the
proof, what the exact first-order correction buys is that the range τ_5 on which the truncation error
is second order in t does not shrink as δ → 0; without it the error would be first order (δ|t|) and
one would need the linear-radius criterion of Lemma 10.5, i.e. a rate condition.

### 11.7 Re-derivation of results quoted from [Check] and Preprint A

**Corollary 11.7. PROVED (first part); PROVED mod. (SF5) (second part).**
(i) ([Check, Thm 3.1] as quoted in the briefing.) If (f, R_m*(ω − d w_m)) is contractive, ω is finitely
supported strictly below the peak of w_m, d = ⟨D_m w_m, D_m ω⟩/C_m, and H = (‖D_mω‖² − d²)/C_m ≤ 1,
then (f, R_m*(ω − dw_m)) ∈ cl NA. More generally the same holds for any contractive (f,g) with
g = b + L*v of 𝒞_fin form whose combined coefficient max(A(b), max_m H_m) is ≤ 1, where A(b) is the
second-order coefficient of t ↦ q*(a + tb).
(ii) (Preprint A, Theorem 3.1, second half.) Weighted directions g with Σ_kλ_kω(k)² < ∞ and support in
the half-peak set: if (f,g) is contractive and H ≤ 1 then (f,g) ∈ cl NA.

*Proof.* (i) For ρ < 1, ρg has the 𝒞_fin certificate (ρb, ρv) with κ' slightly above ρ²·max(...) < 1 on
a small range (second-order expansions of 11.2 and of the base part, with b(ξ̂) = 0 forced by
contractivity), and global margin ρ. Apply Theorem 10.4 and let ρ → 1. (ii) Preprint A's proof shows,
via its uniform expansion (uniform in the truncation level J), that (f, ρg_J) is contractive for J
large, g_J = R*ω_J − d_J R*w finitely supported; apply (i) to (f,ρg_J) (its coefficient is ρ²H_J < 1
for J large), then J → ∞ and ρ → 1. This replaces the appeal to the unavailable note [Check]. ∎

### 11.8 Local splitting density

**Corollary 11.8. PROVED.** If **(LSD)** holds — for every f ∈ S_{p*}, every g ∈ C(f) and every ρ < 1,
ρg is a norm limit of locally split mates of f — then NA((c_0,p),ℓ_2^2) is dense in
L((c_0,p),ℓ_2^2). (Theorem 11.6, closedness of cl NA, and Prop. 2.4(iii).)

LSD is a statement about the bidual geometry at the single point ξ; no norm-attaining approximants
appear in it. It holds for: split mates (trivially), base mates with infinite support (Lemma
11.5(a)), block mates with infinitely supported bounded ω (Lemma 11.5(b)), and Preprint A's weighted
mates with unbounded ω (11.7(ii)). Its status in general is discussed in §12.

### 11.9 Rigidity of the block component

**Proposition 11.9. PROVED (mod. SF3, SF4).** Let m ∈ I and ξ, η ∈ X** \ {0}. If R_m**ξ and R_m**η have
a common support functional w ∈ ℓ_∞ \ {0}, then η ∈ (0,∞)ξ. Consequently, if f ∈ S_{p*} does not
attain its norm, then every f' ∈ NA_p ∩ S_{p*} has w_m(f') ≠ w_m(f) for **every** block m: the block
component of a norm-attaining approximant can never be frozen.

*Proof.* If η ∉ (0,∞)ξ there is v ∈ S_{q*} with ξ(v) > 0 > η(v) (if ξ, η are linearly independent the
map v ↦ (ξ(v),η(v)) is onto ℝ²; if η = −cξ with c > 0 take any v with ξ(v) > 0). By Lemma B choose
n_j → ∞ with u_{n_j,m} → v. By (block-sign), eventually w(n_j) = ‖w‖_∞ sign ξ(v) = ‖w‖_∞ and
w(n_j) = ‖w‖_∞ sign η(v) = −‖w‖_∞, so w = 0. For the consequence: the normer x' of f' lies in X while
the normer of f does not, so they are not positively proportional. ∎

This is the mechanism behind Martín's algebraic triviality, seen from the dual-transfer viewpoint:
the block support functionals encode the bidual normer ray, so lower semicontinuity of the block mate
structure along x' → ξ is a genuine issue (Lemma 11.4 resolves it only for finitely supported
certificates).

**11.10 Contrast: finite-rank L (frozen block part). SKETCH.** If L has finite rank with V smooth and
strictly convex, and a' ∈ NA_q with c_0-face F_{a'} = {x ∈ S_q : a'(x) = 1}, then L(F_{a'}) is a dense
convex subset of the compact convex set L(F**_{a'}) ⊂ V (Goldstine + weak*-continuity), hence contains
its relative interior (Rockafellar 6.3). If the ray (0,∞)L**ξ̂ meets ri L(F**_{a'}) — a genericity
condition that can be arranged for truncations a' of a by moving finitely many free coordinates of
the face point inwards — there is x' ∈ F_{a'} with J_V(Lx') = w, i.e. f' = a' + L*w ∈ NA_p shares the
block part of f, and all block-side mate structure is inherited exactly. Prop. 11.9 shows that this
mechanism is unavailable in Martín's space.

**11.11 Two-sided certificates and one-sided base kinks. PROVED (observation) / OPEN (general).**
Call (b_±, v_±) a two-sided certificate if g = b_+ + L*v_+ = b_− + L*v_− and the certificate
inequalities hold for t ∈ [0,τ] with (b_+,v_+) and for t ∈ [−τ,0] with (b_−,v_−). First-order
analysis (as in 11.5(a)) shows that off supp a the vector b_± lives on {j : |z_j| = 1} with sign ±z_j
("one-sided kink coordinates"). *Observation (PROVED):* if a ∈ c_00 and b_+, b_− are finitely
supported, then b_+ − b_− = L*(v_− − v_+) ∈ Y ∩ c_00 = {0}, and since L* is injective (L*v =
T(Σ v_m(k) m2^{-m-k} e_{k,m}), T injective) v_+ = v_−, so the certificate is split and the one-sided
parts vanish. Hence one-sided base kinks at a finitely supported base part can only be exploited by
mates with infinitely supported base parts or genuinely scale-dependent decompositions — this sharpens
obstacle (R7)(i) of the briefing. For general two-sided certificates I could not verify the recovery
hypotheses: approximating the two decompositions separately produces a mismatch
g'_+ − g'_− ≈ −(β_+ − β_−)(a − a') + (d_+ − d_−)L*(w − w') whose components off supp a' create
first-order kink costs at the norm-attaining approximant (OPEN).

---------------------------------------------------------------------------------------------------

## 12. The open core: local splitting density

**12.1 Problem (OPEN).** Does (LSD) hold for Martín's p (or for p_N, N large)? By Cor. 11.8 a positive
answer gives density of NA((c_0,p),ℓ_2^2) (and by the same arguments with joint fibres, presumably
for ℓ_2^d; I did not check general finite-dimensional F).

**12.2 What a counterexample to LSD must look like (HEURISTIC, with the rigorous parts marked).**
Let g ∈ C(f) and consider optimal decompositions f + tg = A_t + L*W_t. If (W_t − w)/t stays bounded
along t → 0, weak*-limits give first-order split structure (as in 10.2'); the obstruction to local
splitness is then purely second order (base kinks/sign flips interacting with the block Hilbert parts),
and the truncation technique of 11.5 suggests these can be handled scale by scale (not proved). If
(W_t − w)/t is unbounded — which happens in Martín's V because the modulus of rotundity of B_{V_m*} at
w in direction e_k degenerates like Φ_m(k)² (Remark after 10.2, PROVED) — the decomposition moves mass
into block coordinates k(t) → ∞. Two sub-cases:
(a) *Weighted type:* the block coefficients themselves form a fixed (possibly unbounded) sequence ω
    and only the truncation level depends on t (Preprint A). These satisfy LSD (11.7(ii)).
(b) *Cross type:* the block coordinates k(t) are used to carry a *base* vector, e.g. e_j* with
    j ∉ supp a and |z_j| < 1 (a two-sided base kink) or a one-sided kink coordinate. Carrying te_j* by
    the block coordinate k needs u_{k,m} ≈ ê_j = e_j*/q*(e_j*) with error ε_k (base kink cost ≈
    (1 + |z_j|)|t|ε_k), coefficient c_k = q*(e_j*)/(mΦ_m(k)) (block sup-norm overflow unless
    |t|c_k ≤ gap_k := M_m − |w_m(k)|), and bounded Hilbert cost ≈ t²(q*(e_j*)/m)²/(2C_m). So the mate
    exists only if the **rate function** R_j(s) = inf{ε_k : mΦ_m(k)gap_k ≥ s q*(e_j*)} satisfies
    R_j(s) ≤ c's for small s with an explicit c' > 0 determined by the remaining quadratic budget.
    Approximating ρg by a single 𝒞_fin certificate needs, by Lemma 10.5, R_j(C_*ε) ≤ ε with
    C_* > 2√2/(1 − ρ²)·(constants) — a stronger linear-rate condition whose constant blows up as
    ρ → 1. Several block coordinates help only through *cancellation* of the errors u_{k,m} − ê_j:
    since v'' must be bounded, the admissible range is dominated by the smallest Φ_m(k)·gap_k used.
    So **for "critical" linear rates, single-certificate approximation of cross mates fails**
    (HEURISTIC), and LSD — if true — would need certificates exploiting error cancellation, or must
    fail.
Whether critical cross mates exist depends on how fast (u_{k,m})_k approximates base vectors relative
to Φ_m(k) — data not controlled by Lemma B alone; with arXiv unavailable I could not inspect Martín's
choice of T. (An explicit choice making all rates superlinear, or all sublinear, would decide this
sub-case.)

**12.3 Beyond certificates: multi-scale replication (OPEN).** Even if LSD fails, density could hold:
norm-attaining approximants f' = a' + L*J_V(Lx') have free far coordinates of x' ∈ c_0 (briefing R4),
and by the Baire argument of Prop. 3.4(ii) one can create infinitely many off-peak block coordinates
at x'. A cross mate could be recovered if x' can be chosen so that, for the infinite set K of block
coordinates used by g, the values u_{k,m}(x') reproduce the off-peak structure of ξ̂ with relative
precision o(Φ_m(k)) (so that gaps and the first-order constants d match), while x' → ξ̂ weak*. Exact
reproduction is impossible (Prop. 11.9); the question is whether a weighted simultaneous
approximation "|u_{k,m}(x') − ξ̂(u_{k,m})| ≤ ε Φ_m(k) for k ∈ K" is solvable in the c_0-face. For
sparse K with almost disjointly supported u_{k,m} it is (adjust one far coordinate per k); in general
it is a concrete problem about Martín's sequence.

**12.4 Finite-rank Hilbert test case.** Canonical base, V = ℓ_2^r, L* injective with
L*(V) ∩ c_00 = {0}. All admissible decompositions have bounded block quotients (Prop. 10.2). At a
norm-attaining f' (a' ∈ c_00, normer x' ∈ c_0 with Lx' ≠ 0, so |z'_j| < 1 off a finite set) Remark 12.4''(i) below
applies (a finite injectivity set exists because L*(V) ∩ c_00 = {0} and dim V < ∞), so every mate of
an NA functional has the form b_0 + L*v_0 with b_0 supported in supp a' and lifts that are
differentiable with O(t²) remainder; in particular mates of NA functionals lie in c_00 + L*(V)
(PROVED). Theorem 12.4' settles recovery at first rows with finitely supported base part and contact
margin; the general case of this test problem is OPEN (Remark 12.4''(iii)).

**Theorem 12.4' (finite-rank Hilbert perturbations: differentiable lifts and full recovery).
PROVED.** Canonical base on c_0; V = ℓ_2^r; L : c_0 → V of rank r with L* injective and
L*(V) ∩ c_00 = {0}. Let f ∈ S_{p*} with normer ξ, L**ξ ≠ 0, forced decomposition f = a + L*w,
and assume a ∈ c_00 and ‖z|_{F^c}‖_∞ < 1, where F = supp a and ξ̂ = z + U(U*a/‖U*a‖). Then:
(i) for every g ∈ C(f) there are b_0 ∈ span{e_j* : j ∈ F} and v_0 ∈ V with ⟨v_0, w⟩ = 0,
g = b_0 + L*v_0, and a constant C such that **every** admissible decomposition
f + tg = A_t + L*W_t (q*(A_t), ‖W_t‖ ≤ √(1+t²)), |t| ≤ 1, has the form
A_t = a + tb_0 + t²c_t,  W_t = w + tv_0 + t²u_t,  c_t = −L*u_t,  ‖u_t‖ ≤ C;
(ii) {f} × C(f) ⊂ cl NA((c_0,p),ℓ_2^2).

*Proof.* (i) Write W_t = w + tv_t; by Prop. 10.2, ‖v_t‖ ≤ C_1. Put b_t = g − L*v_t, so A_t = a + tb_t.
By convexity and the formula q*'(a;y) = y(ξ̂) + Σ_{j∉F}(|y_j| − z_j y_j),
1 + t²/2 ≥ q*(A_t) ≥ 1 + tb_t(ξ̂) + |t|K_t,  K_t = Σ_{j∉F}(|b_{t,j}| − sign(t) z_j b_{t,j}),
and tb_t(ξ̂) = −t(1−q_0)⟨v_t,w⟩/q_0 (because g(ξ) = 0 and L**ξ = (1−q_0)w). From ‖w + tv_t‖² ≤ 1 + t²
we get 2t⟨v_t,w⟩ ≤ t², hence |t|K_t ≤ t²/(2q_0) and |⟨v_t,w⟩| ≤ C_2|t|. Since
K_t ≥ (1 − ‖z|_{F^c}‖_∞)‖b_t|_{F^c}‖_1, we obtain ‖(g − L*v_t)|_{F^c}‖_1 ≤ C_3|t|.
The linear map u ↦ (L*u)|_{F^c} is injective on V (if it vanishes, L*u ∈ span{e_j* : j ∈ F} ⊂ c_00, so
L*u = 0 and u = 0), hence bounded below by some c > 0 (dim V < ∞). Any limit point v_0 of v_t (t → 0)
satisfies (g − L*v_0)|_{F^c} = 0, so v_0 is unique, and
‖v_t − v_0‖ ≤ c^{-1}‖(L*(v_t − v_0))|_{F^c}‖_1 = c^{-1}‖(g − L*v_t)|_{F^c}‖_1 ≤ C_3|t|/c.
Put u_t = (v_t − v_0)/t, b_0 = g − L*v_0 (supported in F), c_t = −L*u_t. Also ⟨v_0,w⟩ = lim⟨v_t,w⟩ = 0.
(ii) Fix ρ < 1 and g ∈ C(f). For |t| ≤ 1 apply (i) with s = ρt to admissible decompositions of
f + sg (they exist by 2.1 and satisfy the bounds √(1+ρ²t²)): f + tρg = A_{ρt} + L*W_{ρt}. Take
x' = P_N z + U(U*a/‖U*a‖) (a normer of a in the c_0-face; x' → ξ̂ weak*), w' = Lx'/‖Lx'‖ → w,
f' = a + L*w' ∈ NA_p (Prop. 2.3), v'_0 = v_0 − ⟨v_0,w'⟩w', g' = ρ(b_0 + L*v'_0) → ρg. Then
f' + tg' = A_{ρt} + L*W'_t with W'_t = w' + ρtv'_0 + ρ²t²u_{ρt} (because c_{ρt} + L*u_{ρt} = 0), and
‖W'_t‖² − ‖W_{ρt}‖² = 2ρ²t²⟨w' − w, u_{ρt}⟩ + ρ²t²(‖v'_0‖² − ‖v_0‖²) + 2ρ³t³⟨v'_0 − v_0, u_{ρt}⟩
≤ o(1)t² uniformly in |t| ≤ 1 (‖v'_0‖ ≤ ‖v_0‖, ‖u_{ρt}‖ ≤ C). Hence for |t| ≤ τ (τ fixed small) and
N large: p*(f' + tg') ≤ max(q*(A_{ρt}), ‖W'_t‖) ≤ (1 + ρ²t² + o(1)t²)^{1/2} ≤ √(1+t²); for |t| ≥ τ
use the slack (2.5) and ‖f' − f‖ + ‖g' − ρg‖ → 0. So g' ∈ C(f'), (f',g') ∈ NA, (f',g') → (f,ρg). ∎

**Remark 12.4'' (extensions). (i) PROVED; (ii) SKETCH; (iii) HEURISTIC.** (i) The proof of part (i)
only uses a *finite* set S ⊂ {j ∉ supp a : |z_j| < 1} on which u ↦ (L*u)|_S is injective: then
Σ_{j∈S}|(g − L*v_t)_j| ≤ |t|/(2q_0(1 − max_S|z_j|)), hence again v_t = v_0 + O(t), and by the two-sided
first-order bounds b_0 = g − L*v_0 vanishes on every j ∉ supp a (also where |z_j| = 1). So
differentiability of lifts holds for arbitrary a (possibly infinite support) under this finite
injectivity condition, which is generic for finite-rank L.
(ii) For a ∉ c_00 the transport in part (ii) must also truncate a; combining the proof with the
truncation estimate (11.5.1) applied to the directions b_0 + s c_s|_{supp a} (the coordinates outside
supp a are identical on both sides, and the tails of the compact family {c_s} are uniformly small)
should give {f} × C(f) ⊂ cl NA in this generality; I have not written out the bookkeeping.
(iii) If no finite S as in (i) exists (e.g. supp a = ℕ), the block parts v_t of optimal
decompositions may oscillate between scales; transporting them to an NA approximant then produces
a t-dependent first-order error ⟨P_w^⊥ v_t, w' − w⟩ L*w' in the base, and I do not know how to avoid
it. Even for finite-rank Hilbert perturbations the dual transfer theorem is therefore not proved in
full here.

*Contrast.* Preprint A, Prop. 3.4 shows that under exactly the hypotheses a ∈ c_00 and
‖z|_{F^c}‖_∞ < 1, Martín's blocks force **unbounded** block difference quotients for suitable mates.
Theorem 12.4' shows that the blow-up is caused by the infinite-dimensional, non-Hilbertian block
geometry (degenerate modulus of rotundity, Remark after 10.2), not by the dual-sum structure: for
finite-rank Hilbert perturbations the lifts are differentiable with O(t²) remainder and every mate
transports along *any* NA sequence in the c_0-face. (For infinite-rank Hilbert V the bounded-below
step fails, and only ‖(L*(v_t − v_0))|_{F^c}‖ = O(t) survives.)

**Lemma 12.5 (automatic off-peak structure in the fast regime). PROVED (mod. block-threshold).**
Fix a block m and a coordinate j, put ê_j = e_j*/q*(e_j*), and let K ⊂ ℕ satisfy
q*(u_{k,m} − ê_j) ≤ c_0 Φ_m(k) for k ∈ K. Let y ∈ X** with y(e_j*) = 0 and R_m**y ≠ 0, and write
w_y = J_m(R_m**y), M_y, C_y for its block data. Then |(R_m**y)(k)| ≤ m c_0 q**(y) Φ_m(k)² for k ∈ K,
and if θ_y := C_y m c_0 q**(y)/|R_m**y|_m < M_y, every k ∈ K is off-peak for w_y with
|w_y(k)| ≤ θ_y, i.e. gap ≥ M_y − θ_y.

*Proof.* (R_m**y)(k) = mΦ_m(k) y(u_{k,m}) = mΦ_m(k) y(u_{k,m} − ê_j), and |y(u_{k,m} − ê_j)| ≤
q**(y) c_0 Φ_m(k). By the block-threshold lemma, R_m**y/|R_m**y| = α + D²w_y/C_y with α ≥ 0 (in the
sign of w_y) supported on the peak set; a peak coordinate k satisfies
|(R_m**y)(k)|/|R_m**y| ≥ Φ_m(k)² M_y/C_y, which is excluded by θ_y < M_y; off the peak
w_y(k) = C_y (R_m**y)(k)/(Φ_m(k)²|R_m**y|), whence |w_y(k)| ≤ θ_y. ∎

**12.6 Rate trichotomy for cross mates (HEURISTIC, built on 12.2 and Lemma 12.5).** For a base
coordinate j and a block m, compare ε_k = q*(u_{k,m} − ê_j) with Φ_m(k) along the coordinates that
could carry e_j*.
* *Slow* (ε_k/Φ_m(k) → ∞): no block coordinate can carry te_j* with error ≲ |t| inside its admissible
  range, so cross mates using (j,m) should not exist.
* *Superfast* (ε_k = o(Φ_m(k)) along infinitely many k): the linear-radius criterion (Lemma 10.5)
  holds for every ρ < 1, so cross mates should satisfy LSD and be recoverable by Theorem 10.4.
  Moreover, by Lemma 12.5, every y with y_j = 0 — the bidual normer *and* every NA approximant x' with
  x'_j = 0 — has all these coordinates off-peak with almost full gap, so Prop. 11.9's rigidity does
  not destroy the cross structure.
* *Intermediate* (ε_k ≍ Φ_m(k)): single-certificate approximation fails for ρ near 1, and Lemma 12.5
  applies only if c_0 is small compared with M_y|R_m**y|/(C_y m q**(y)). This is the only regime in
  which I can imagine LSD failing; there density would require the multi-scale replication of 12.3.
Note that at the bidual normer itself, any cross mate carrying e_j* through block m forces
ξ(e_j*) = 0, because the carrying coordinates must be off-peak, i.e. ξ(u_{k,m}) = O(Φ_m(k)), and
u_{k,m} → ê_j (PROVED by the same block-threshold computation).

---------------------------------------------------------------------------------------------------

## 13. Could the abstract statement fail?

**13.1 Logical status. PROVED (as a remark).** Fix a finite-dimensional F. A counterexample to the
abstract statement ("if NA((X,q),G) is dense for all finite-dimensional G and L is compact, then
NA((X, q + ‖L·‖), F) is dense") is in particular a Banach space (X,p) with NA((X,p),F) not dense, i.e.
F fails Lindenstrauss property B. Whether every finite-dimensional space has property B is open
(Johnson–Wolfe, Question 6; open even for ℓ_2^2). Hence no known theorem excludes a counterexample,
and exhibiting one would solve that problem negatively. Conversely a proof of the abstract statement
would not resolve property B in general (it only covers dual compact perturbations of good spaces).

**13.2 Necessary features of a counterexample** (each item is a theorem from the literature or from
these notes):
* F is not polyhedral (finite-dimensional polyhedral spaces have Lindenstrauss' property β, and β
  implies property B for every domain).
* X fails the RNP (Bourgain: RNP ⇒ NA(X,F) dense for every F; RNP is an isomorphic property, so q and
  p are alike in this respect).
* NA_p contains no dense linear subspace of X* (Preprint B, Lemma 3.5), and (X,p) has no sequence of
  norm-one finite-rank projections approximating the identity on compact sets (Lemma "projections";
  in Martín's case there are none of rank ≥ 2 at all, Prop. 9.3).
* L is not "Read-type" with respect to contractive projections of q (Thm 9.4).
* Under (A1): the first rows f at which recovery fails form a meagre set (Cor. 10.1'); at such f some
  mate is not a limit of locally split mates whenever Theorem 10.4's hypotheses hold for the locally
  split mates (as in Martín's space, Thm 11.6); and every NA approximant must have a moving block part
  (Prop. 11.9, Martín-type blocks).
* The approximating NA operators, if any, must have non-split second rows (Prop. 3.4) — which do exist.

**13.3 Infinite-dimensional ranges (remark).** Property B fails for some infinite-dimensional ranges
(Gowers: ℓ_p, 1 < p < ∞; Acosta: infinite-dimensional strictly convex spaces). This does not give a
counterexample to the abstract statement (those domains are not presented as dual compact
perturbations of good spaces), and the question here concerns finite-dimensional F only.

**13.4 Consistency checks performed.** (i) "Split NA operators are not dense" (Preprint A) versus
"cl NA ⊇ normalised SC" (Thm 11.6): consistent, since the approximants are only locally split.
(ii) If every mate at every NA point were split, every NA operator would be split, cl NA ⊂ SC (closed)
and density would fail; Prop. 3.4(ii) shows non-split mates at NA points exist, so there is no hidden
contradiction. (iii) The briefing's reductions (R1)–(R3) were re-derived (Props. 2.4, 10.1, 10.1'');
(R4) agrees with Prop. 2.3; (R7)(i) is sharpened by 11.11.

---------------------------------------------------------------------------------------------------

## 14. Assessment and next steps

**Strongest abstract theorems proved.** Theorem 10.4 (conditional dual transfer with explicit,
checkable recovery hypotheses), Theorem 9.4 (Read-type dual transfer), Theorem 10.1 / Cor. 10.1'
(abstract global compactness and residual recovery under (A1)), Prop. 10.2 (bounded lifts for Hilbert
V), Theorem 12.4' (full recovery at finitely supported base parts with contact margin, finite-rank
Hilbert perturbations).

**Martín's space.** Hypotheses of Theorem 10.4 verified for finite split certificates (11.1–11.4);
truncation lemmas with exact first-order correction (11.5) then give Theorem 11.6: every locally split
contraction, in particular every normalised split-contractive operator, lies in cl NA. [Check, Thm 3.1]
and Preprint A's weighted theorem follow (11.7). Density is reduced to the intrinsic property LSD
(Cor. 11.8). Structural results: NA operators with non-split mates exist (3.4); fixed-row approximation
is impossible already for the base (4.3); block parts of NA approximants can never be frozen (11.9);
within-block truncation never yields admissible permanence decompositions (9.2); no norm-one
finite-rank projections (9.3); in the fast-rate regime the carrying block coordinates of cross mates
are automatically off-peak at every point with vanishing j-th coordinate (Lemma 12.5).

**Errors found in the preprints / briefing.** None in the parts I re-derived (Preprint A Thm 2.1, the
Baire argument of Thm 2.4, the logic of Props 3.3–3.4 and Remark 3.5; Preprint B Lemmas 3.1, 3.4, 3.5,
Thm 3.2; briefing (R1)–(R4)). Caveats: Preprint A's Thm 3.1 depended on the unavailable [Check]; that
dependence is removed by 11.7. Strict convexity of p** for infinitely many blocks rests on the
unavailable [Recovery]; none of my main results uses it (they work with any normer).

**Next steps (in order of expected payoff).**
1. *Cross mates.* Compute (or bound) the rate functions R_j(s) of §12.2 for Martín's actual operator T
   (needs the paper). Decide whether critical cross mates exist; if all rates are superlinear, try to
   prove LSD for p_N.
2. *Shifted certificates.* Extend Lemmas 11.3–11.5 to curves a + tb + t²c, w + tv − t²v_c with
   L*v_c = c (parallel-sum structure, Prop. 10.3), using the c_0-face freedom (z' = P_{N'}z, N' large) to
   control the kink cost of c off supp a'. This would extend Theorem 11.6 to all mates whose local
   structure is "smooth".
3. *Two-sided certificates* with infinitely supported base parts (one-sided kinks), 11.11.
4. *Multi-scale replication* (12.3) for sparse coordinate sets K: a weighted simultaneous
   approximation problem in the c_0-face.
5. *Finite-rank Hilbert test case* (12.4) as a laboratory: Theorem 12.4' covers first rows with
   finitely supported base part and contact margin; write out Remark 12.4''(ii) (infinite support with
   a finite injectivity set) and attack 12.4''(iii) (oscillating lifts when supp a = ℕ). A full proof
   here would be the first complete dual transfer theorem for a non-trivial class of perturbations.
6. *Ranges ℓ_2^{d+1} and general F.* Theorem 10.4 and Theorem 11.6 extend to joint fibres C_d
   (d second rows g_1,…,g_d, each locally split): the NA approximants in Lemmas 11.3–11.4 (a_N, x_N
   and w' = J_V(Lx')) do not depend on the certified direction, so all d rows are transported along
   the same sequence, and the margin argument is the same with ‖(t_1,…,t_d)‖_2 in place of |t|
   (SKETCH). For a non-Euclidean finite-dimensional F the reduction "first row + mates" must be
   replaced by the local profile of ‖·‖_{F*} near the maximal direction; for polyhedral F nothing is
   needed (property β), and for F with C² positively curved dual sphere the same certificate
   formalism applies with √(1+t²) replaced by that profile (HEURISTIC).

---------------------------------------------------------------------------------------------------

## Appendix: numerical experiments

Scripts are in ctx/r1/D_scripts/ (numpy only).

**N1 (n1_parallel_sum.py): curvature of a Minkowski sum of two ellipsoids.** For random ellipsoids
K_1 = M_1(B), K_2 = M_2(B) in ℝ^n, a random normer ξ (h_{K_1+K_2}(ξ) = 1), f = ∇h_1(ξ) + ∇h_2(ξ) and
random tangent g, the numerical second derivative of gauge_{K_1+K_2}(f + tg) (computed by maximising
⟨x, f + tg⟩/h(x) over the sphere) is compared with the parallel sum (q_0A)^{-1}+((1−q_0)B)^{-1})^{-1}
and with the max-split value. Output:

    n=2  q0=0.5141   numeric d2 = 0.11817 / 0.06356 / 0.57260
                     parallel-sum = 0.11817 / 0.06356 / 0.57260
                     max-split    = 0.13685 / 0.07360 / 0.66310
    n=3  q0=0.3983   numeric d2 = 1.10346 / 0.03684 / 0.66526
                     parallel-sum = 1.10346 / 0.03684 / 0.66526
                     max-split    = 2.74987 / 0.08874 / 1.59317

**N2 (n2_block_trunc.py): non-convexity of |z| − |P_1 z| for a block norm** with unit ball
B_{ℓ_1} + D(B_{ℓ_2}) on ℝ³, Φ = (1/2, 1/4, 1/8), y = e_2:

    R=1: ψ(y)=0.800  ½(ψ(Re_1+y)+ψ(−Re_1+y))=0.616
    R=3:  0.800 vs 0.566;  R=10: 0.800 vs 0.389;  R=30: 0.800 vs 0.134

(and |e_k| = 1/(1 + Φ_k) as expected). Lemma 9.1 is the proof; the numbers only illustrate it.

**N3 / N3b (n3_base_trunc.py, n3b_base_trunc_const.py): the base truncation inequality (11.5.1).**
Random q*(a) = ‖a‖_1 + ‖Ga‖ on ℝ^n (n ≤ 60), a with decaying coordinates (so sign flips |sb_j| > |a_j|
occur in the tail), b with b(ξ̂) = 0, random truncation level N, s on the admissible range
|s| ≤ ‖U*a‖/(2‖U*b‖). In 60 000 tests: 0 violations of the exact ℓ_1 inequality
‖a + sP_Nb‖_1 ≤ ‖a + sb‖_1 − sΣ_{j>N} z_j r_j, 0 violations of the U-part bound with the explicit
constant C_2 = 2‖U*b‖/‖U*a‖ + ε_N/‖U*a‖ (largest observed ratio 0.535 of the bound).

**N4 (n4_block_trunc.py): the block truncation lemma 11.5(b).** Random blocks (n ≤ 40, Φ_k = c^k),
random peak sets and near-peak coordinates, local mates v = ω − dw rescaled until
N(w + tv) ≤ √(1+t²) on |t| ≤ 0.3, truncations with the exact first-order correction at k_0. In
161 753 tests: 0 violations of N(w + tv'') − N(w + tv) ≤ 2(‖Dω‖‖Δ‖ + ‖Δ‖²)t²/C on |t| ≤ min(t_0,t_1)
(largest observed ratio 0.49), and 0 violations of the first-order bound for |t| ≤ 3.

**N5 (n5_finite_rank_hilbert.py): Theorem 12.4'(i).** ℓ_1-part on ℝ^30, Hilbert part of dimension 4,
V = ℝ², supp a = {0,1,2}, contact margin 0.3, split mate g = b_0 + L*v_0. For each t the maximal
deviation D(t) = max ‖W − (w + tv_0)‖ over *all* admissible W (bisection along 720 rays):

    t        0.2    0.1    0.05   0.025  0.0125  0.00625
    D/t²     3.27   4.21   4.59   6.63   6.74    6.79     (D/|t| → 0)

consistent with ‖W_t − w − tv_0‖ = O(t²) for every admissible decomposition.

**N6 (n6_hbase.py): Lemma 11.3 (localized base approximation with uniform radius).** a ∈ ℝ^80 with
geometrically decaying coordinates, b = b_0 + βa (b_0 on the first 5 coordinates, β = −b_0(ξ̂)),
κ = sup_{|t|≤τ} 2(q*(a+tb) − 1)/t². Approximants a_N = P_N a/q*(P_N a), x_N = P_N z + U(h_N/‖h_N‖)
(checked a_N(x_N) = 1), b' = b_0 − b_0(x_N)a_N, κ'_N = sup over the fixed radius τ/3. Typical rows:

    κ = 0.0813:  κ'_N = 0.0537, 0.0725, 0.0803, 0.0807, 0.0807   (N = 8, 15, 30, 60, 80)
    κ = 0.4145:  κ'_N = 0.1451, 0.4472, 0.4012, 0.4107, 0.4106
    κ = 1.5018:  κ'_N = 1.4004, 1.3928, 1.4443, 1.4514, 1.4514

and κ'_60 ≤ κ in all 40 trials (for small N, κ'_N may exceed κ, as the lemma allows).
