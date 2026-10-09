# P2 referee — part 3: Props 3.1-3.3, Theorem 3.4

## Prop 3.1 (mixed term). CORRECT (PROVED).
d/d delta e(a + delta y)|_0 = P_{e-perp}U*y/nu; B(xhat') - B(zhat) = <U*B, e(delta) - e> when z' = z on supp B; second-order
remainder O(delta^2 ||U*B||). (a) absorbed by c = g''(xhat') (Thm 2.1); (b) B^+ - B^- = rho v and both first-order terms vanish iff
v(xhat') = 0 — consistent with Thm 2.1 Step 1. (c),(d) are qualitative (d is labelled HEURISTIC where it should be). Fine.

## Prop 3.2 (consistency identity). CORRECT (PROVED).
Re-derived: B'_t - B'_{t'} = rho sum R*(omega_{t'} - omega_t) - rho sum Delta'_m R* w'_m and B_t - B_{t'} = sum R*(omega_{t'} - omega_t)
- sum Delta_m R* w_m, whence the displayed formula. Delta'_m = (R_m*(omega_{t'} - omega_t))(x')/|R_m x'|_m by Fact C at f' (supports off P').
The sentence "at scales tau >= s_1 they MUST be <= eps_0 s_1 in l_1" is a sufficient condition (cost <= 2|tau| x mass), not a
proved necessity (only the part at non-contacts outside supp a' is charged, with weight 1 - |z'_j|): read "suffices".

## Prop 3.3 (garbage identity, Delta d != 0). CORRECT AS A SUFFICIENT CONDITION, with two fixable gaps.
Algebra re-derived: with Delta d'_m = Delta d_m, B^+ - B^- = rho(v_1... ) = rho(v + E), E = -sum Delta d_m R_m*(w'_m - w_m); E's cost
<= 2 rho theta |tau| ||E||_1 per side (kink or flip, |x| - z'x <= 2|x|), Hilbert change O(||E||) -> 0. B^theta contains no E.
(G3.3a) "exactly when" (task wording) / "the ONLY change" (notes) must read "provided": E may sit on cheap coordinates; no
  necessity is proved.
(G3.3b) Steering for Delta d != 0 is NOT "verbatim": the condition is F(mu) := v_1(xhat') - Delta d |R_1 xhat'|_1 = 0, i.e.
  F = v(xhat') - Delta d beta(xhat') with beta(x) := |R_1 x|_1 - <w_1, R_1 x> = (R_1*(w'_1 - w_1))(x) >= 0. The IVT needs |Delta d| beta
  small compared with V_Far along the WHOLE path mu in [0, mu_max] (|Delta d| beta <= ||E(mu)||_1 ||xhat'||_inf), so the E-bound must
  hold uniformly along the steering path (enlarge mu_max to 16V_Far/gamma_+). For |I_0| >= 2 the span hypothesis must be stated for
  the vectors (v_{m,j} - Delta d_m (R_m* w'_m)_j)_m, not (S).

## Theorem 3.4 (non-neutral two-piece mates at block-tame active blocks). WRONG AS STATED (vacuous), repair possible only partly.
**Proposition R1 (PROVED).** For two-piece data (1.6) with omega_Delta != 0 the restrictions to J_gamma of
{psi_{k,m} : k in Qbar_m, m in I_0} are linearly dependent for every gamma > 0. Hypothesis (iii) of Thm 3.4 therefore never holds
in a non-trivial case (omega_Delta = 0 gives v = 0, a finite certificate).
*Proof.* supp omega_Delta,m is contained in the strict non-peaks, hence in Qbar_m. Put c_{k,m} := lambda_{k,m} omega_Delta,m(k) (not all 0).
Then sum_k c_{k,m} u_{k,m} = R_m* omega_Delta,m = v_m and sum_k c_{k,m} u_{k,m}(xi) = <omega_Delta,m, zeta_m> = |zeta_m| Delta d_m (Fact C,
omega_Delta,m off P_m). Hence sum_{k,m} c_{k,m} psi_{k,m} = sum_m (v_m - Delta d_m R_m* w_m) = b+ - b- = v, and v is supported in F cup K,
which is disjoint from J_gamma = {j notin F : |z_j| <= 1 - gamma}. QED. (Numerical confirmation of the identity: P2Aref_work/thm34_*.py.)
*Meaning.* The derivative of the tuning map p -> (u_{k,m}(xhat'(p))/|R_m xhat'(p)|_m)_{(k,m) in Qbar} in the free variables has range in
the hyperplane {y : sum c_{k,m}|zeta_m| y_{k,m} = 0}; the missing direction is exactly the steering quantity v(xhat') (mixed term of 3.1).
So "construction of Thm 2.1 WITHOUT Far set and raising mass (steering is part of the tuning)" cannot work: the residual of the
window masses along this direction is ~ s_1 gamma_+ and is invisible to free moves. This is the authors' own Remark after 4.2
(resonance carriers make r_W(J) = 0), applied to psi instead of u. The example claim ("P1's example ... covered once (iii) holds")
is void: there |Qbar_1| = 1 and psi_{2,1}|_J = u|_J = 0.
**Repair (SKETCH, my assessment).** Replace (iii) by (iii'): the restrictions to J_gamma of the psi_{k,m} span a space of dimension
|Qbar| - 1 (the c-relation is the only relation), and reinstate base-side steering for the c-direction (Graves in (mu, p); the
tuning map is C^1 on finite-dimensional families: Lipschitz + Gateaux => Hadamard, J_m norm-to-weak* continuous).
Then a NEW issue appears that the notes do not address: when the base steering needs a PULL (all mass directions raise, e.g. |F| = 1
and z_j<P U*v, U*e_j*> >= 0 on K, which is P1's diagonal-U situation), the pull is made by Far flips z'_j = -z_j on
Far in (N, N_2], which move EVERY block functional u_{k,m}(xhat') by up to 2||u_{k,m} 1_Far||_1. In the d-neutral case this is harmless
(only f' -> f matters); in the non-neutral case it enters E through peaks of the active block pushed below threshold or flipped
(a peak u_k ~ e_j*/q*(e_j*), j in Far, changes w(k) by ~ 2M). These perturbations are not O(s_1) uniformly in k, so (MS) at scale s_1
does not control them; controlling them needs a comparison between the tails of the first ~log(1/s_1) block vectors and the tail tau_N
of v (a RATE condition, not implied by Lemma B; it does hold for P1's T thanks to its allowedness rule c_l <= 2^{-2s} c_{l'}).
If two-sided steering by O(s_1) masses is available (some j in F with <PU*v, U*e_j*> != 0, or a contact with z_j<PU*v,U*e_j*> < 0),
all perturbations are O(s_1) in sup norm plus the late cut-off N'', and the repaired statement is plausible (SKETCH): changed peaks
have weight o(s_1) by (MS) + deep weight m 2^{-m-K_0}, Lemma 4.1 gives |C'-C| = o(s_1) and ||E||_1 = o(s_1); degenerate peaks stay
within |w'(k) - w(k)| <= (1 + r)|C' - C|.
**Consequence.** The summary claim "A_referee §5.5 ('engineering breaks when d != 0') is too pessimistic" is NOT established.
What is established: Prop 3.3 (sufficient condition) and, by the repair, a restricted class (two-sided mass steering, finite Qbar,
(MS), (iii')).
