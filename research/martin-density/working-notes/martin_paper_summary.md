# Martín, "A Banach space whose set of norm-attaining functionals is algebraically trivial" (JFA 288 (2025); preprint dated July 23 2024, revised Dec 12 2024) — verbatim-level summary (read from the PDF supplied by the user)

**Lemma A.** Let Φ be a sequence of positive reals in ℓ_1 with ||Φ||_1 < 1, S_Φ: ℓ_2 → ℓ_1, [S_Φ(a)](n) = Φ(n)a(n). Define |·|_Φ on ℓ_1 by B_{(ℓ_1,|·|_Φ)} = B_{ℓ_1} + S_Φ(B_{ℓ_2}). Then
(a) |f|_Φ^* = ||f||_∞ + ||S_Φ^*(f)||_2 for f ∈ ℓ_∞;
(b) |f|_Φ^* ≥ ||f||_∞ ≥ (1 − ||Φ||_1)|f|_Φ^*;
(c) |x|_Φ ≤ ||x||_1 ≤ (1 + ||Φ||_1)|x|_Φ;
(d) (ℓ_1,|·|_Φ)^* strictly convex, so (ℓ_1,|·|_Φ) smooth;
(e) if x ∈ ℓ_1, f ∈ ℓ_∞, |f|_Φ^* = 1, ⟨f,x⟩ = |x|_Φ and |x(n)| > Φ(n)|x|_Φ, then f(n) = sign(x(n))||f||_∞.
(Proof of (e): x = x_0 + S_Φ(a_0) with x_0 ∈ S_{ℓ_1}, a_0 ∈ S_{ℓ_2}; f attains max on B_{ℓ_1} at x_0, so f(n) = sign(x_0(n))||f||_∞ where x_0(n) ≠ 0; if x(n) > Φ(n) then x_0(n) ≥ x(n) − Φ(n)|a_0(n)| > 0.)
NOTE: Martín's threshold in (e) is the cruder Φ(n)|x|_Φ (Preprint B's block-threshold lemma refines it to |x|_Φ (M/C) Φ(n)^2).

**Lemma B.** Let Y be a separable operator range. Then there is a norm-one injective T: ℓ_1(N×N) → Y such that for every m the set {T(e_{n,m})/||T(e_{n,m})|| : n ∈ N} is dense in S_Y.
*Proof (complete text).* Consider σ: N×N → N bijective and the isometric isomorphism Ψ: ℓ_1(N×N) → ℓ_1 carrying e_{n,m} to e_{σ(n,m)}. Take a sequence {w'_m : m ∈ N} such that every element of S_Y is an accumulation point of it and repeat the proof of Proposition 2.8 of [16] with the sequence w_{σ(n,m)} = w'_n for every n, m.
[16] = Kadets, López, Martín, Werner, "Equivalent norms with an extremely nonlineable set of norm attaining functionals", J. Inst. Math. Jussieu 19 (2020) 259–279. The exact form of T from [16, Prop. 2.8] is NOT available to us. Consequently: the sequence (w'_n) is an ARBITRARY sequence in S_Y having every point of S_Y as an accumulation point, and T is only known to satisfy the conclusion of Lemma B (plus whatever [16, Prop 2.8] gives, presumably T(e_n)/||T e_n|| close to w_n). So "Martín's space" is a family of spaces depending on these choices. A density theorem should either hold for EVERY admissible T, or state explicitly the property of T it uses (and then it is legitimate to note that (w'_n) can be chosen to have it, if [16, Prop 2.8] allows T(e_n)/||T(e_n)|| to be as close to w_n as desired — unverified).
In particular, for each m, the normalized sequence (u_{n,m})_n follows the SAME dense sequence (w'_n)_n (up to the perturbations produced by [16, Prop 2.8]).

**Observation C.** Z = ℓ_1-sum of smooth Z_m; if f = (f_m) ∈ Z^*, ||f||_∞ = 1, ⟨f,z⟩ = ||z||_1, then f_m(z_m) = ||z_m|| for every m, hence ||f_m|| = 1 when z_m ≠ 0. Norm of Z is smooth at z with all z_m ≠ 0.
**Observation D.** Z smooth, z_1^*, z_2^* ∈ S_{Z^*} independent; if ||t z_1^* + (1−t)z_2^*|| = 1 for some 0<t<1 then tz_1^* + (1−t)z_2^* ∉ NA(Z).

**Proof of Theorem 1 (Steps).**
1. X = c_0 with smooth |||·||| with NA((X,|||·|||)) = NA(c_0) (= c_00), from [15, Lemma 11] or [6, Thm 9.(4)] (DGS smoothing); by [16, Prop 2.4] there is a separable operator range Y dense in (X,|||·|||)^* with NA((X,|||·|||)) ∩ Y = {0}.
2. T from Lemma B; v*_{n,m} := T(e_{n,m}) ∈ B_Y; {v*_{n,m}/|||v*_{n,m}||| : n} dense in S_Y, hence in S_{X*}.
3. |·|_m from Lemma A with Φ_m(n) = 2^{-m}2^{-n}|||v*_{n,m}|||. (i) smooth; (ii) |x|_m ≤ ||x||_1 ≤ (1 + 2^{-m})|x|_m; (iii) |f(n)| ≤ |f|_m^*; (iv) if |f|_m^* = 1, ⟨f,x⟩ = |x|_m, |x(n)| > 2^{-m}2^{-n}|||v*_{n,m}||| |x|_m, then f(n) = sign(x(n))||f||_∞ and ||f||_∞ ∈ [1 − 2^{-m}, 1].
   (So in every block M_m = ||w_m||_∞ ≥ 1 − 2^{-m} and C_m = ||D_m w_m||_2 ≤ 2^{-m}.)
4. R_m: (X,|||·|||) → (ℓ_1,|·|_m), [R_m x](n) = (m/2^m)(1/2^n) v*_{n,m}(x). R_m injective; |R_m x|_m ≤ ||R_m x||_1 ≤ (m/2^m)|||x|||.
5. W = (⊕_m (ℓ_1,|·|_m))_{ℓ_1}, R(x) = (R_m x)_m, ||Rx||_W ≤ (Σ m/2^m)|||x|||; norm of W smooth at R(x), x ≠ 0.
6. R^*((w*_m)_m) = T(Σ_m Σ_n w*_m(n)(m/2^m)(1/2^n) e_{n,m}) ∈ Y; R^*(w*) = 0 ⇒ w* = 0.
7. p(x) = |||x||| + ||R(x)||_W; 𝔛 = (X,p) smooth. If p(x) = p*(x*) = x*(x) = 1 then x* = x_0* + R^*(w*) with x_0* ∈ NA(X,|||·|||), |||x_0*||| = 1, w* ∈ S_{W*}, ⟨w*, R x⟩ = ||Rx||_W, and |w*_m|_m^* = 1, w*_m(R_m x) = |R_m x|_m for all m.
8–10. Two-lines property via the sign argument (density of the normalized v*_{n,m} in S_Y and (iv)).

**Remark 2.** For δ > 0, p_δ(x) = |||x||| + δ||Rx||_W also works; p_ε-equivalent to sup norm.
**Proposition 3.** 𝔛** strictly convex (so 𝔛* smooth); p(x**) = |||x**||| + Σ_m |R_m**(x**)|_m, [R_m** x**](n) = (m/2^m)(1/2^n) x**(v*_{n,m}). (Proof uses NORM density of the normalized v*_{n,m}.)
**Proposition 4.** Same construction in any WCG space isomorphic to a subspace of ℓ_∞ containing c_0 (with Y only weak*-dense).
**Remark 5.** Veselý: NA(Z) ∩ S_{Z*} is c-dense; for Fréchet-smooth renormings of c_0, NA ∩ S is pathwise connected.
**Section 2.3, Open Problem 7.** Does NA(𝔛, ℓ_2^2) contain rank-two operators? (Answered positively in Preprint B.) Johnson–Wolfe [13, Question 6] calls density for ℓ_2^2 "the most irritating open problem about norm-attaining operators".
