# Z5 referee, part 1: verdicts on T1-T11, T13a (line-by-line checks)

## T1 (transfer peaks at arbitrary a). CORRECT (PROVED).
Checked every use of a in c_00 in the proof of thm:transfer: (i) canonical truncations keep a -> replaced by a_N = a1_[1,N]/q*(.)
with z^N = z1_[1,N] (z^N = sgn a_N on supp a_N; Prop smooth(c) gives NA); (ii) Step 1 base: kappa_N := (b1_[1,N])(xt_N) -> b(zhat) = 0
(sum_{j<=N} b_j z_j -> b(z), U*(b1_[1,N]) -> U*b, e_N -> e); no-flip radius uniform in N: |b'_N(j)| <= (||b/a|| c^a_N + |kappa_N|)|a_N(j)|;
P_N^perp U* b'_N = P_N^perp U*(b1_[1,N]) -> P^perp U* b, so h_N -> h(b); (iii) Step 4: beta_{m,N} with a_N; (R_m* y_{m,N})(x'_N) ->
(R_m* y_m)(xi) since R_m* y_{m,N} -> R_m* y_m in l_1 and x'_N -> xi weak* boundedly; e_{m,N} -> e_{inf,m}; the bookkeeping identity
is an identity at x'_N; a_N(x'_N) = c_N so e_{m,N}(x'_N) = 0; (iv) Step 5: A(t) = (1+E)a_N + t rho b'_N + sum eps_m e_{m,N}; E can be
negative but |E| = O(t^2), so (1+E) >= 1/2 and t rho/(1+E) stays inside the no-flip radius. Steps 2, 3 (transfer peaks at xi) and the
block parts never used F. Step 6 only uses g in C(f). Minor: the theorem needs I finite (stated), and Gamma_w is a function of the DATA
(b, omega) (not unique at infinite F); the statement is correctly phrased in terms of data.

## T2 (windowed averaging at arbitrary F). CORRECT.
thm:windowed uses F only in its last sentence; the averaged certificate has base part (1/n) sum b_{t_i}: finite support and bounded ratio.
Hypothesis (i) of thm:windowed must be supplied separately at infinite F (T3). Fine.

## T3 (uniform transfer expansion with |b_j| <= 3|a_j|/t). CORRECT.
Base: |r b_j| <= 3 c_flat |a_j| < |a_j|: no flips; ||b||_1 <= 3/t so ||rU*b||/nu <= 3c_flat||U||/nu; Psi <= ||h_perp||^2/(2(1-||h||)).
Rebalancing error |lambda| 2 q*(rb) <= |I|K_3K_Y r^2 . 6(1+||U||)c_flat. Blocks unchanged. Constants depend on f, eps_tr only.

## T4 (clamped window certificate). CORRECT.
Identity (b^cl 1_{F_t})(zhat) = B_+(zhat) - (B_+1_{F^c})(zhat) - ((B_+ - b^cl)1_F)(zhat) - (b^cl 1_{F\F_t})(zhat) checked; lem:flip clamp
bound re-derived (|B_+ - b^cl| = g_j <= |Delta B(j)| + f^-_j on the sign side, <= f^+_j on the anti-sign side); |a_t(zhat) - 1| <=
(1+||U||)alpha(M_t) <= (1+||U||)t^2. |b_t(j)| <= 2|a_j|/t + 2K_kappa t|a_j| <= 3|a_j|/t. ||B_+ - b_t||_1 = O(Kt) with K_kappa = O(K).

## T5, T6 (B*-inf, B-inf). CORRECT.
prop:pinned(a) at infinite F: J_gamma excludes F, lem:budget(b) holds at any F. Every hypothesis of Prop 3.1/Lemma 3.2/Cor 2.3 follows
from K_j T_hi(l_j) -> 0. NOTE: (SR) at infinite F forces room OFF F: signature sets inside F get no room (so B-inf does not touch
support swallowing). This is a correct and complete proof of Remark rem:Binf (Problem prob:infiniteF in the (SR) case).

## T7 (sign-mixed room, cushion room). CORRECT, with a correction to the gloss of (W^c).
(a) lem:signmixed: E_l over S_l \ F, sum <= t/q_0 by lem:switchbudget (j notin F); valid at any F.
(b) sum_l E^c_l <= t/q_0 + sum_{F, j>M} 2(s_j Delta B(j))_- <= t/q_0 + 2(2alpha(M)/t + t/(2q_0)) = (2/q_0 + 4)t. r^{[M]} DEcreases in
M (fewer coordinates), M(T_lo(l*)) is the largest index needed and gives the smallest room: correct choice.
Correction of the gloss: if sgn a is constant on S_l cap F (monochromatic support swallowing), then r_l^{[M]} = 0 for EVERY M
(sigma = -sgn a kills all far support terms; S_l \ F contributes 0 when r_l = 0). So (W^c) is useful only for SIGN-MIXED a on the
swallowed signature sets (and then super-fast decay is needed). The note's/Z5's description "restrictive unless a decays super-fast"
omits the sign-mixing requirement.

## T9 (pure base mates). CORRECT. (a) from the base identity (all terms after t b(zhat) are >= 0, divide by t -> 0+-).
(b) Fl^M(t) = sum_{F_{<=M}} 2(-s_j t rho b_j - lambda_M(t)|a_j|)_+ <= rho Fl_b(t) for lambda_M >= rho; independence of far z^M values
checked (b^M lives on [1,M]). Numerical script reproduced (ratios 0.40-0.96 < 1).

## T10 (bounded free switching at arbitrary F). CORRECT; it does correct R4 (Z1_ref_notes l.222 "F finite is essential (Y may
contain a)"). Phi(c) = (P^perp U* sum c u, (sum c u)(zhat)) injective: P^perp part 0 => sum c u = (mu/nu) a => (sum c u)(zhat) = mu/nu.
|Delta B(zhat)| <= t/q_0 (lem:budget(a)), ||P^perp U* Delta B|| <= 2(2nu/q_0)^{1/2} (lem:budget(d)). Script reproduced (rank 5 vs 6).
Phrasing fix: lem:rigidity(a) as STATED (b_+ - b_- in c_00) remains true at every F; what fails at infinite F is uniqueness of data
whose base parts lie in l_1(F cup K) (block combinations supported in F, e.g. u_l with supp u_l in F).

## T11 (proxy budget). CORRECT (constants re-derived: sum_{F,j>M} 2(|a_j|/t + f^+_j) <= 2t + t/(2q_0)).
It is a bookkeeping statement about f's decompositions, not a statement that g is a mate of a finite-F first row.

## T13a (reduction equivalence). CORRECT but essentially tautological: (ii) => (i) is the composition of (LSC-trunc) with Lemma Z at
the finite-F row f' (then f'' in R_0 subset Rec and rho rho' -> 1); (i) => (ii) from thm:reductionZ and lem:pair. It moves all of (O4)
into (LSC-trunc), which is not easier than Lemma Z. The 2alpha(M) transplant computation is a correct base-excess identity
(2(-s x)_+ - 2(-s x - |a|)_+ = 2 min((-s x)_+, |a|)) but ignores the change of the forced data (zhat^M, w^M); HEURISTIC as an argument
for "not a consequence of truncation".
