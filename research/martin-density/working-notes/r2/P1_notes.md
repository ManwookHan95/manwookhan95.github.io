# P1 notes — Is the defect empty? (matching at scale, resonances, and an explicit nonempty defect)

Round 2, task P1. Setting: canonical base q (B_q = B_{c_0} + U(B_H), U compact with dense range), Martin's norm with a FINITE block
set I (p_N; by Preprint B Remark martin-tail this suffices; everything also holds for I = N given (T4) there), notation of
A_notes §1, §4 and BRIEFING. Imported as in Round 1: (T4) strict convexity of p** (unique normers, forced decomposition),
A_notes Facts A-F, Lemmas 4.3-4.7, Prop 4.5, Thm 4.10, 4.17, 6.2, 6.5, 6.8, Lemmas 7.1-7.2 (all refereed); in 3.8 also C_notes
Thm 6.4, Prop 6.5, Lemma 5.2 (Round 1, unrefereed; re-checked where used). Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Def(f) := C(f) \ (closure of all mates known to be recoverable by intrinsic means: finite, shifted, weighted certificates,
locally admissible linear decompositions = locally split mates, the averaging class of A Thm 6.8, C Thm 7.1, the constant-split
two-piece mates of A_referee §5.1). Part files: P1_part1.md ... P1_part6.md (this file assembles them). Script:
scripts/check_twopiece.py (numerical check of the two-piece decompositions, 200 random truncated models: max excess over
s(t) on |t| <= 1 is 2e-16).

## 0. Answer and summary

**The defect is NOT empty in general.** For a suitable admissible T (constructed in 2.1; Lemma B's conclusion only) there is a
non-attaining first row f in S_{p_N*} (any N >= 1) such that every mate obtained by any known intrinsic mechanism lies on ONE
line R u (u := u_{2,1}), while C(f) contains an infinite-dimensional family of "two-piece" switching mates, e.g. the finitely
supported mate c u(j)(e_j* - zhat_j alpha e_1*) for any contact j (Theorem 2.4). The mechanism is an EXACT RESONANCE: the block
vector u of an off-peak coordinate with w = 0 is, as a base functional, supported on supp a plus an infinite contact set K'
with the contact signs, and u(zhat) = 0; splitting the contact set between the two sides of t = 0 produces mates that use
contacts K_1 for t > 0 and the block carrier plus contacts K_2 for t < 0.

"Matching at scale" holds, but it is AUTOMATIC (it is the identity B+ + L*Omega+ = g = B- + L*Omega-) and does not force the
one-sided parts to be small: the two sides' one-sided usages have opposite signs and ADD UP in the transfer (D, Omega_D) =
(B+ - B-, Omega- - Omega+), which is a cheap zero-direction decomposition of f (3.4-3.6). So a defect mate exists only through
RESONANCES = cheap transfers with large one-sided mass. Exact resonances need infinitely many one-sided base coordinates
(contacts or near-flips; 4.1), so none exist at NA points or when a is in c_00 and K is finite; approximate resonances run
through near-threshold block carriers (cross-block near-duplicates switch only if their perturbation is >~ Phi in the xi-direction
with opposite signs, 4.2), and when the gaps of the carriers are not summable the mate is in cl Cert(f) anyway (weighted
averaging, 4.3-4.4). Exact description of the defect: at block-tame f (finitely many strict non-peaks, finite supp a)
Def(f) = (C(f) \ S(f)) union {g_c in C(f): Hhat(c) > 1} with S(f) the finite-dimensional certificate span (3.7); at C-tame f the
first piece is empty (3.8). The dual route reduces everything to c_0-exposed mates but cannot close the gap (5.1-5.3).
The explicit defect of Theorem 2.4 is nevertheless recoverable by ENGINEERED NA approximants (6.3, SKETCH), after correcting
the referee's scheme (far NEGATIVE masses and a constant tail). So it is not a counterexample to density; it shows that
density cannot be proved by intrinsic (sequence-independent) recovery alone.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | All known intrinsic recoverable classes lie in cl S(f), S(f) := span of certificate directions; hence C(f) \ cl S(f) is in Def(f) | PROVED | 1.2-1.3 |
| 2 | Construction of an admissible T with prescribed special vectors and a "badly approximable" zhat (all coordinates but one are peaks) | PROVED | 2.1 |
| 3 | The first row f: non-attaining, contact set infinite, Q_1 = {2}, Q_m empty otherwise | PROVED (T4) | 2.2 |
| 4 | Two-piece mates g_{K_1} in C(f) (explicit decompositions on both sides) | PROVED (+numerics) | 2.3 |
| 5 | **Def(f) != empty**: cl Cert^sh(f) in R u, g_{K_1} not in R u for empty != K_1 != K' | PROVED | 2.4 |
| 6 | Single-scale resource bounds and capacities (window / one-sided / remainder) | PROVED | 3.1-3.3 |
| 7 | Transfer identity; sign opposition; matching at scale is automatic; one-sided parts bounded by the transfer's one-sided mass | PROVED | 3.4-3.6 |
| 8 | Block-tame f: Def(f) = (C(f) \ S(f)) disjoint union {Hhat > 1}; cl Cert^sh = Cert^sh | PROVED | 3.7 |
| 9 | C-tame f: C(f) in S(f), only the second-order defect can survive | PROVED mod C Thm 6.4/Prop 6.5 | 3.8 |
| 10 | Exact resonances force infinitely many one-sided base coordinates (none at NA points) | PROVED | 4.1 |
| 11 | Sign rule; Martin's near-duplicates serve the same side unless perturbed by >~ Phi | PROVED | 4.2 |
| 12 | Weighted averaging theorem; near-threshold carriers with sum of gaps = infinity give mates in cl Cert(f) | PROVED | 4.3-4.4 |
| 13 | Switching through super-near-threshold carriers (summable gaps) or weak peaks: in cl Cert(f)? | OPEN | 4.4 Rem |
| 14 | Support-function criterion; reduction to c_0-exposed mates; explicit support-function gap | PROVED | 5.1-5.3 |
| 15 | At the example, C(f) is contained in E_u (explicit infinite-dimensional space) and contains a slab of it | PROVED | 6.1-6.2 |
| 16 | Engineered recovery of the explicit switching mates at the example (corrected referee scheme) | SKETCH | 6.3 |
| 17 | Second-order defect {Hhat > 1} nonempty somewhere? | OPEN | 3.7 Rem |
| 18 | For EVERY admissible T, some f has Def(f) != empty? | OPEN (true for the constructed T) | 7 |
| 19 | Conjecture A 7.5 (scale separation => empty defect) | cannot hold as stated: the defect of 2.4 uses no approximation property of T (A's 'scale separation' is informal) | 7.1 |

# P1 part 1: the certificate span S(f) and the linear obstruction

Setting: canonical base, finite block set I (Martin's p_N; any N >= 1). Notation of A_notes §1, §4.
f in S_{p*}, normer xi, q_0, forced decomposition f = a + L*w, zhat = z + U e, F = supp a,
K = {j notin F : |z_j| = 1} (contacts), for each block m: zeta_m, w_m, M_m, C_m, P_m (peaks),
Q_m = N \ P_m (strict non-peaks), gap_m(k) = M_m - |w_m(k)|, lambda_{k,m} = m Phi_m(k).

## 1.1 Definition (certificate span)
  S(f) := { b + sum_m R_m*(omega_m - d_m(omega_m) w_m) : b in l_1(F), b(zhat) = 0, omega_m in c_00(Q_m) },
  d_m(omega) := <D_m w_m, D_m omega>/C_m.
Equivalently S(f) = (l_1(F) cap zhat^perp) + span{ y_{k,m} : k in Q_m, m in I },
  y_{k,m} := lambda_{k,m} u_{k,m} - (Phi_m(k)^2 w_m(k)/C_m) R_m* w_m.
(Indeed R_m*(e_k - d_m(e_k) w_m) = y_{k,m} and d_m(e_k) = Phi_m(k)^2 w_m(k)/C_m.) Every element h of S(f) has h(xi) = 0.

## 1.2 Lemma (all known recoverable classes lie in cl S(f)). PROVED.
For every f in S_{p*}, each of the following sets is contained in cl S(f) (norm closure in l_1):
 (a) Cert(f) and Cert^sh(f) (A_notes Def 4.1, 4.15): directions g_c, c = (b, omega[, theta]) with supp b in F,
     omega_m in c_00(Q_m) — literally elements of S(f) (||b/a|| < infinity is extra);
 (b) Theorem W directions (A_notes 6.2): b in l_1(F), omega_m off-peak with sum_k lambda_k |omega_m(k)| < infinity:
     limits of truncations, which lie in S(f) (the truncations c_J in the proof of Thm 6.2 are in S(f) and g_{c_J} -> g);
 (c) mates with a locally admissible linear decomposition (Theorem L, A_notes 6.5) and locally split mates
     (D_notes Thm 11.6): by A Lemma 6.3 / D Lemma 11.5, b is supported in F with b(zhat) = 0 and Omega_m = omega_m - d_m w_m
     with omega_m bounded and vanishing on P_m; truncations of omega_m (finite subsets of Q_m) give elements of S(f)
     converging in norm (sum_k lambda_k |omega(k)| <= ||omega||_inf sum_k lambda_k < infinity, and d is continuous);
 (d) the averaging class (A_notes Thm 6.8): it is contained in cl Cert(f);
 (e) C_notes Theorem 7.1 (natural finite certificates): supp b in F, omega_m in c_00(Q_m): in S(f);
 (f) the referee's constant-split two-piece mates (A_referee §5.1): they are finite certificates.
Hence cl Cert^sh(f) and all mates listed in the briefing as "known recoverable at f by intrinsic means" lie in cl S(f).
(The engineered recovery of A_referee §5.4 (SKETCH) is NOT an intrinsic class and is not covered.)

*Proof.* Each item is a direct reading of the definitions/structure lemmas quoted; closures are norm closures and
cl S(f) is a closed subspace. QED.

## 1.3 Corollary (linear obstruction). PROVED.
If g in C(f) and g notin cl S(f), then g lies in the defect Def(f) = C(f) \ cl Cert^sh(f), and more strongly
g is not a norm limit of mates of any of the types (a)-(f).

## 1.4 Remark (when the obstruction can bite)
cl S(f) is a closed subspace of ker(xi) cap l_1. If some block has infinitely many strict non-peaks whose
vectors u_{k,m} are "spread" (e.g. dense in directions of ker xi), then cl S(f) = l_1 cap ker xi and 1.3 is void.
If every Q_m is FINITE ("block-tame" f), then S(f) is finite-dimensional, hence closed, and 1.3 is a finite
linear-algebra test: g notin span{e_j* : j in F} + span{u_{k,m} : k in Q_m} + span{R_m* w_m}.
In particular, at a block-tame f, every mate with a nonzero component on a contact coordinate (in the sense of
not being in that finite span) is in the defect. This is the route to an explicit nonempty defect (part 3).
# P1 part 2: an admissible T and a first row f with NONEMPTY defect (exact resonance)

Standing: canonical base q (B_q = B_{c_0} + U(B_H), U: H -> c_0 compact, dense range; U* injective, compact),
any finite block set I containing 1 (p_N, N >= 1). "Admissible T" = Lemma B's conclusion:
 (T-a) T: l_1(N x N) -> l_1 bounded, q*(T e_{n,m}) <= 1 with equality for some (n,m) (norm one);
 (T-b) T injective; (T-c) Ran T cap c_00 = {0} (then Y := Ran T is a dense separable operator range with
 Y cap NA(q) = {0}); (T-d) for every m, {u_{n,m} := T e_{n,m}/q*(T e_{n,m}) : n} is norm dense in S_{q*}.
(Every tail is then dense too: S_{q*} has no isolated points.) Imported as in Round 1: (T4) p** strictly convex
for finite I (Preprint B), hence unique normers and the forced decomposition (A_notes Fact B).

## 2.1 Lemma (construction of T). PROVED.
Notation: nu_j := ||U* e_j*|| -> 0 (U* compact, e_j* -> 0 weak*), J_0 := {j >= 2 : nu_j <= 1/2} (cofinite).
alpha := 1/(1 + nu_1), a := alpha e_1* (q*(a) = 1), e := U*e_1*/nu_1 = U*a/||U*a||, so zhat_1 := 1 + (Ue)_1 = 1 + nu_1 = 1/alpha.
Fix a bijection l: N x N -> N with l(n,m) < l(n',m) for n < n' and l(1,1) = 1; pairwise disjoint infinite sets
S_l contained in J_0 (l in N); h_l := sum_{s in S_l} 2^{-s} e_s*; c_l := 2^{-(l-1)^2} (so c_1 = 1, sum_{l' >= l} c_{l'} <= 2 c_l).
Special index l_0 := l(2,1); K' := S_{l_0}; z := e_1 + 1_{K'} in l_infinity; zhat := z + U e.
For k >= 2, (k,m) != (2,1): pi_{k,m} := 2^{1-m-k} c_{l(k,m)}/c_{l(1,m)} (<= 1/4), and rho_l := sqrt(pi_{k,m}) (l = l(k,m)).
Call (k,m) exceptional if pi_{k,m} >= 1/(26(1+||U||))^2 (finitely many). Put
  delta_{l(1,m)} := min(2^{-l}, 1/(8(1+||U||))), delta_{l_0} := 1, delta_l := min(2^{-l}, rho_l/(1+||U||)) otherwise
  (for exceptional l: delta_l := min(2^{-l}, 1/(16(1+||U||)))).
Vectors (n_l denotes the q*-norm of the bracket, so that q*(u_l) = 1):
 * u_{1,m} := (e_1*/q*(e_1*) + delta_l h_l)/n_l, l = l(1,m);
 * u_{2,1} := (-kappa e_1* + h_{l_0})/n_{l_0}, kappa := (||h_{l_0}||_1 + <U* h_{l_0}, e>)/(1 + nu_1) > 0;
 * exceptional (k,m): u_{k,m} := (e_1*/q*(e_1*) + delta_l h_l)/n_l;
 * all other (k,m): u_{k,m} := (y + pi + delta_l h_l)/n_l, where y = y^{(i(k,m))} is a target and pi a correction:
   pi := 0 if |y(zhat)| >= 3 rho_l, else pi := 3 rho_l sigma alpha e_1* with sigma := sign y(zhat) (sigma := 1 if 0).
Targets: (y^{(i)})_{i>=1} subset c_00 cap S_{q*} dense in S_{q*}, y^{(1)} := e_1*/q*(e_1*). Index i is ALLOWED at l if
supp y^{(i)} cap S_l = empty and 2 c_l <= 2^{-2s} c_{l'} delta_{l'} for every s in supp y^{(i)} cap S_{l'}, l' != l.
(y^{(1)} is allowed everywhere; each i is allowed at all large l, since supp y^{(i)} is finite and meets finitely many S_{l'}.)
Fix (i_n) in which every positive integer occurs infinitely often; i(n,m) := i_n if allowed at l(n,m), else 1.
Define T e_{n,m} := c_{l(n,m)} u_{n,m}. Then T is admissible, Phi_m(k) = 2^{-m-k} c_{l(k,m)}, and:
 (P1) u_{2,1} has support {1} cup K', u_{2,1}(1) < 0 < u_{2,1}(j) for j in K', and u_{2,1}(zhat) = 0;
 (P2) |u_{1,m}(zhat)| >= 7/9 for every m;
 (P3) |u_{k,m}(zhat)| > pi_{k,m} for every k >= 2 with (k,m) != (2,1).

*Proof.* (P1): |<U* h, e>| <= ||U* h|| <= sum_{s in K'} 2^{-s} nu_s <= ||h||_1/2 (K' in J_0), so kappa > 0. Since z = 1 on K',
zhat_s = 1 + (Ue)_s there and u^0 := -kappa e_1* + h_{l_0} satisfies u^0(zhat) = -kappa/alpha + ||h||_1 + <h, Ue>
= -kappa(1+nu_1) + ||h||_1 + <U* h, e> = 0.
Norm bounds: for non-special l, q*(pi + delta_l h_l) <= (1+||U||)(3 rho_l + delta_l) <= 4(1+||U||) rho_l <= 4/26 < 1/4
(non-exceptional: rho_l <= 1/(26(1+||U||))), so n_l in [3/4, 5/4]; for l(1,m) and exceptional l, n_l in [7/8, 9/8].
(P2): (e_1*/q*(e_1*))(zhat) = zhat_1 alpha = 1 (q*(e_1*) = 1 + nu_1 = 1/alpha); |delta h_l(zhat)| <= delta ||h_l||_1 sup_{s in S_l}|zhat_s|
<= delta ||U|| <= 1/8 (z = 0 on S_l for l != l_0, |(Ue)_s| <= ||U||). Hence |u_{1,m}(zhat)| >= (7/8)/(9/8) = 7/9.
(P3): non-exceptional: |(y + pi)(zhat)| >= 3 rho_l (by the choice of pi: if pi != 0, (y+pi)(zhat) = y(zhat) + 3 rho_l sigma has
modulus |y(zhat)| + 3 rho_l), |delta_l h_l(zhat)| <= delta_l ||U|| <= rho_l, so |u(zhat)| >= 2 rho_l/(5/4) > rho_l >= pi_{k,m}
(pi <= 1). Exceptional: |u(zhat)| >= (1 - 1/16)/(17/16) > 1/2 > 1/4 >= pi_{k,m}.
(T-a): q*(T e_{n,m}) = c_{l(n,m)} <= 1 = c_1. (T-d): for fixed m, ||u_{n,m} - y^{(i(n,m))}||_1 -> 0 as n -> infinity
(rho_l, delta_l -> 0 and n_l -> 1, because pi_{n,m} -> 0 as n -> infinity), and each i equals i(n,m) for infinitely many n
(it occurs infinitely often in (i_n) and is allowed at all large l). Hence every y^{(i)} is a limit point; density follows.
(T-b),(T-c): let x in l_1(N x N) (index by l) with Z := sum_l x_l c_l u_l in c_00, and suppose x_{l'} != 0. Write
u_l = (y_l + delta_l h_l)/n_l with y_l in c_00 (y_{l_0} = -kappa e_1*, y_{l(1,m)} = e_1*/q*(e_1*), y_l = target + pi else).
Among the tails delta_l h_l only the one with l = l' lives on S_{l'}, and y_{l'} itself misses S_{l'} (allowedness; the special and
first-coordinate vectors have y supported on {1}, and 1 is not in J_0). For s in S_{l'}, letting L(s) := min{l : s in supp y_l} (if any),
  Z(s) = x_{l'} c_{l'} delta_{l'} 2^{-s}/n_{l'} + sum_{l >= L(s), s in supp y_l} x_l c_l y_l(s)/n_l,
and the second sum is bounded by (4/3) ||x||_inf 2 sum_{l >= L(s)} c_l <= (16/3)||x||_inf c_{L(s)} <= (8/3)||x||_inf 2^{-2s} c_{l'} delta_{l'}
(||y_l||_inf <= 2, n_l >= 3/4 for every l touching signature coordinates, and allowedness at L(s)). Hence
|Z(s)| >= c_{l'} delta_{l'} 2^{-s} ( |x_{l'}|/n_{l'} - (8/3)||x||_inf 2^{-s} ) > 0 for all large s in S_{l'}: Z is not in c_00.
So x = 0: T is injective (Z = 0) and Ran T cap c_00 = {0}. QED.

Remark 2.1.1. Only (T-a)-(T-d) are used below, plus (P1)-(P3). The construction is flexible: any finite set of
prescribed vectors can be inserted, targets can be the same in all blocks ("Martin-like"), and the super-fast decay of
c_l is used only for (T-c) and (P3).

## 2.2 Lemma (the first row f and its block structure). PROVED (given T4).
With T from 2.1 and any finite I containing 1, put xi := zhat/p**(zhat) and f := a + L* J_V(L** xi). Then:
 (a) q**(zhat) = 1, f in S_{p*}, xi is its (unique) normer, q_0 = 1/p**(zhat), the forced data of f are (a, w := J_V(L**xi))
     with base contact z = e_1 + 1_{K'}; F = supp a = {1}; the contact set is K = K' (infinite); f is not norm attaining.
 (b) In block 1 the coordinate k_0 := 2 is a strict non-peak with w_1(2) = 0 (gap M_1); every other coordinate (k,m),
     m in I, is a peak. Thus Q_1 = {2} and Q_m = empty for m != 1.
*Proof.* (a) zhat = z + Ue with ||z||_inf = 1, ||e|| = 1, so zhat in B_{q**} = B_{l_inf} + U(B_H); a(zhat) = alpha zhat_1 = 1 = q*(a);
hence q**(zhat) = 1. p** = q** + ||L**.||_V (Preprint A §1), so p**(zhat) = 1 + ||L**zhat||. f(xi) = (a(zhat) + ||L**zhat||)/p**(zhat) = 1,
and p*(f) <= max(q*(a), ||w||) = 1 (A Fact A), so f in S_{p*} is normed by xi; uniqueness (T4) and A Fact B give the forced
data; xi/q_0 = zhat = z + Ue is the contact representation (z = sign a on F). zhat is not in c_0 (z = 1 on the infinite K',
Ue in c_0), so the unique normer is not in X and f is not norm attaining.
(b) Write zeta_m := R_m** xi, so zeta_m(k) = lambda_{k,m} u_{k,m}(xi) = lambda_{k,m} q_0 u_{k,m}(zhat). By A Fact C:
 (i) if k is not a peak then |u_{k,m}(xi)| <= |zeta_m|/m [off P, w(k) = C zeta(k)/(Phi_k^2|zeta|) and C >= Phi_k |w(k)| give
     |zeta(k)| <= Phi_k |zeta|];
 (ii) k is a peak as soon as |zeta(k)| > |zeta| Phi_k^2 M/C, i.e. |u_{k,m}(xi)| > theta_m Phi_m(k), theta_m := M_m|zeta_m|/(m C_m).
|zeta_m| <= ||zeta_m||_1 <= q_0 m sum_k Phi_m(k) <= q_0 m 2^{-m} (|u(zhat)| <= q**(zhat) q*(u) = 1, c_l <= 1).
By (P2), |u_{1,m}(xi)| >= 7 q_0/9 > q_0 2^{-m} >= |zeta_m|/m, so (1,m) is a peak by (i). Then C_m >= Phi_m(1) M_m, so
theta_m Phi_m(k) <= |zeta_m| Phi_m(k)/(m Phi_m(1)) <= q_0 2^{-m} Phi_m(k)/Phi_m(1) = q_0 pi_{k,m}, and (P3) with (ii) shows that every
(k,m) != (2,1), k >= 2, is a peak. Finally u_{2,1}(xi) = 0 by (P1), so zeta_1(2) = 0: k = 2 is not a peak (peaks have
|zeta(k)| >= |zeta| Phi_k^2 M/C > 0) and w_1(2) = C zeta_1(2)/(Phi^2|zeta|) = 0. QED.

## 2.3 Proposition (two-piece mates). PROVED.
Let u := u_{2,1}, lambda_0 := lambda_{2,1} = Phi_1(2), and for c > 0 put v := c u. For every subset K_1 of K' put
K_2 := K' \ K_1, beta := (v 1_{K_1})(zhat) and g_{K_1} := v 1_{K_1} - beta a. There is c_* > 0 (depending on U, M_1, C_1,
lambda_0 only) such that for 0 < c <= c_* every g_{K_1} lies in C(f). Its admissible decompositions are:
  side +  (t >= 0):  f + t g = (a + t g) + L* w;
  side -  (t <= 0):  f + t g = (a + t(g - v)) + L*(w + t D),  D := (c/lambda_0) e_2 in block 1 (L* D = v),
where on side + the contacts K_1 are used with the free sign (t v_j > 0 = z_j-signed), and on side - the contacts K_2
are used with the free sign (-t v_j > 0) and the exact block carrier (1,2) (w_1(2) = 0) carries v.
*Proof.* Recall q*(e_1*) = 1/alpha = zhat_1, nu := ||U*a|| = alpha nu_1, and the elementary Hilbert bound: for x > 0 and
y in H, ||x e + y|| <= x + <e,y> + ||y||^2/(2x) <= x + <e,y> + ||y||^2/x  [||e + h|| = sqrt(1 + 2<e,h> + ||h||^2) <= 1 + <e,h> + ||h||^2/2].
Let |t| <= 1 and assume c <= c_1 := min( nu/(4(1+||U||)), 1/(4(1+||U||)) ); then |beta| <= ||v||_1 ||zhat||_inf <= c(1+||U||) <= 1/4.
Side +, 0 <= t <= 1: a + t g = (1 - t beta) a + t v 1_{K_1}, (1 - t beta) >= 3/4, K_1 does not contain 1, so
 q*(a + t g) = (1 - t beta) alpha + t ||v 1_{K_1}||_1 + ||(1 - t beta) nu e + t h_1||,  h_1 := U*(v 1_{K_1}), ||h_1|| <= c||U|| <= nu/4,
 <= (1 - t beta)(alpha + nu) + t( ||v 1_{K_1}||_1 + <e, h_1> ) + t^2 ||h_1||^2/((3/4) nu)
 = 1 - t beta + t beta + (4/3) t^2 ||h_1||^2/nu,
because ||v 1_{K_1}||_1 + <e,h_1> = (v 1_{K_1})(z + Ue) = beta (v > 0 = z-signed on K_1). The block part is w, N_m(w_m) = 1.
Side -, t = -s, 0 <= s <= 1: g - v = -beta a - v_1 e_1* - v 1_{K_2} (v_1 := v(1) = c u(1) < 0), so
 a + t(g - v) = (alpha(1 + s beta) + s v_1) e_1* + s v 1_{K_2},  coefficient >= alpha(1 - 1/4) - c >= alpha/2 > 0 (c <= alpha/4),
 q*(.) <= (alpha(1 + s beta) + s v_1)(1 + nu_1) + s ||v 1_{K_2}||_1 + s<e, h_2> + (4/3) s^2 ||h_2||^2/nu,  h_2 := U*(v 1_{K_2}),
 = 1 + s[ beta + v_1 zhat_1 + (v 1_{K_2})(zhat) ] + (4/3) s^2 ||h_2||^2/nu = 1 + s v(zhat) + ... = 1 + (4/3) s^2 ||h_2||^2/nu,
since v(zhat) = c u(zhat) = 0 (P1). [The bracket is (v 1_{K_1} + v 1_{{1}} + v 1_{K_2})(zhat).] Block 1: W := w_1 + t D differs from w_1
only at k = 2, W(2) = -s c/lambda_0, |W(2)| <= M_1 if c <= M_1 lambda_0; the peaks keep |W(k)| = M_1, so ||W||_inf = M_1, and
||D_1 W||^2 = C_1^2 + s^2 c^2/1 (Phi_1(2)/lambda_0 = 1/m = 1), so N_1(W) = M_1 + sqrt(C_1^2 + s^2 c^2) <= 1 + s^2 c^2/(2 C_1).
Other blocks: w_m.
Conclusion for |t| <= 1: by A Fact A, p*(f + t g) <= 1 + t^2 max( (4/3)||U||^2 c^2/nu, c^2/(2 C_1) ) <= 1 + (3/8) t^2 <= s(t)
when c also satisfies (4/3)||U||^2 c^2/nu <= 3/8 and c^2/(2C_1) <= 3/8 (s(t) >= 1 + t^2/2 - t^4/8 >= 1 + 3t^2/8 for |t| <= 1).
For |t| >= 1: p*(f + t g) <= 1 + |t| q*(g) and q*(g) <= q*(v) + |beta| <= 2c(1+||U||) <= sqrt 2 - 1 if c <= 0.2/(1+||U||);
since (s(t) - 1)/|t| is increasing, 1 + |t|(sqrt 2 - 1) <= s(t). So c_* := min of the listed bounds works. QED.

## 2.4 Theorem (nonempty defect at an exact resonance). PROVED (given T4).
For T and f as above (any finite I containing 1): every mate obtained by the known intrinsic mechanisms lies in the line
R u_{2,1}; precisely cl S(f) = S(f) = R u_{2,1}, hence
  cl Cert^sh(f) and all classes of part 1, Lemma 1.2 are contained in [-c_max, c_max] u_{2,1} (for some c_max),
whereas C(f) contains g_{K_1} for every K_1 in K' (c fixed small). If K_1 != empty and K_1 != K', then g_{K_1} is not in
R u_{2,1}, so g_{K_1} is in Def(f). The g_{K_1}, j in K', even span an infinite-dimensional subspace: e.g. K_1 = {j} gives
g_{{j}} = c u(j) (e_j* - zhat_j alpha e_1*), a FINITELY SUPPORTED mate in the defect.
*Proof.* S(f) = (l_1(F) cap zhat^perp) + span{y_{k,m} : k in Q_m}. F = {1} and zhat_1 = 1/alpha != 0 give l_1(F) cap zhat^perp = {0};
by 2.2(b) the only strict non-peak is (2,1), and y_{2,1} = lambda_0 u - (Phi^2 w_1(2)/C_1) R_1* w_1 = lambda_0 u. So S(f) = R u, a closed
line, and Lemma 1.2 applies. If g_{K_1} = mu u, compare coordinates j in K' (where a vanishes and u(j) > 0): c 1_{K_1}(j) = mu
for all j in K', impossible unless K_1 is empty or all of K'. QED.

Remark 2.4.1 (what the defect mates look like). The transfer of g_{K_1} (part 3) is the scale-free exact relation
  v = L* D   with v supported on F cup K' and z-signed on K' (u(zhat) = 0):
the block carrier (1,2) (two-sided, w = 0) and the contact vector v 1_{K'} (one-sided) represent the same functional
modulo l_1(F). Splitting the contact part K' = K_1 + K_2 between the two sides produces switching mates. Their membership in
cl Cert(f) would require approximating v 1_{K_1} modulo S(f), impossible here because S(f) is a line.
Remark 2.4.2 (consistency checks). (i) cu = g_{K'} is a two-sided finite certificate (f + t c u = a + L*(w + tD) for all t),
in agreement with S(f) = R u. (ii) C_notes Thm C (tame f has finite-dimensional C(f)) does not apply: K is infinite.
(iii) A_notes Prop 7.4: at points with finite supp a cup K one-sided linear decompositions coincide; here K is infinite and
indeed b+ - b- = v is an infinitely supported element of L*(V*) (A Remark 7.6 / A_referee §5 predicted exactly this).
# P1 part 3: single-scale structure, the transfer identity, matching, and the block-tame description of Def(f)

Setting: finite I, f in S_{p*} with forced data (A_notes §1, §4). For tau != 0 an ADMISSIBLE decomposition at scale tau is
  f + tau g = A + L*W,  q*(A) <= s(tau), N_m(W_m) <= s(tau) for all m;  A = a + tau B, W = w + tau Omega  (so g = B + L*Omega).
eps(tau) := s(tau) - 1 <= tau^2/2. For a block m: level ell_m := ||W_m||_inf, peak deviations delta_k := ell_m - sigma_k W_m(k) >= 0
(k in P_m), weights alpha_{m,k} (Fact C), |alpha_{m,k}| = lambda_{k,m} mu_{k,m}/|zeta_m| with margin mu_{k,m} := |u_{k,m}(xi)| - theta_m Phi_m(k) >= 0.

## 3.1 Lemma (resource bounds at one scale). PROVED.
For every admissible decomposition at scale tau:
 (B1) sum_{j notin F} ( |B_j| - sign(tau) z_j B_j ) <= eps/(q_0 |tau|);  in particular sum_{j notin F} (1 - |z_j|)|B_j| <= eps/(q_0|tau|) and
      the "paid" contact usage sum_{j in K} |B_j| 1[sign(tau B_j) = -z_j] <= eps/(2 q_0 |tau|);
 (B2) Fl_B(tau) = sum_{j in F} 2(-sign(a_j) tau B_j - |a_j|)_+ <= eps/q_0;
 (B3) nu Psi(tau U*B/nu) <= eps/q_0, hence ||P_{e perp} U*B||^2 <= (2 eps/(q_0 tau^2)) nu (1 + |tau| ||U*B||/nu);
 (K1) sum_{k in P_m} |alpha_{m,k}| delta_k <= eps/|zeta_m|;
 (K2) tau^2 ||P_m-perp D_m Omega_m||^2/(||D_m W_m|| + <D_m W_m, D_m w_m>/C_m) <= eps/|zeta_m|;
 (K3) |w_m(k) + tau Omega_m(k)| <= ell_m <= s(tau) for every k (box).
*Proof.* Budget identity (A Lemma 7.1): q_0 E_q(A) + sum_m |zeta_m| e_m(W_m) <= eps, all terms >= 0; exact excess formulas
(A Lemma 7.2) express E_q(A) as Fl + sum_{j notin F}(|tau B_j| - z_j tau B_j) + nu Psi, and e_m as the peak sum plus the
Hilbert term; each nonnegative piece is bounded by the whole. (B3): Psi(h) >= ||h_perp||^2/(2(1 + ||h||)) (A Lemma 4.3). QED.

## 3.2 Definition (window / one-sided / remainder at scale tau; parameter c_0 in (0,1/4]).
 * base window: j in F with |tau B_j| <= |a_j|/c_0 ("two-sided": certificate radius >= c_0|tau| coordinatewise);
 * base one-sided: (i) near-contacts K_{c_0} := {j notin F : |z_j| > 1 - c_0} used with the cheap sign (sign(tau B_j) = sign z_j);
   (ii) near-flip coordinates j in F with |tau B_j| > |a_j|/c_0 used with the cheap sign (sign(tau B_j) = sign a_j);
 * base remainder: everything else off F (free coordinates, paid usages): by (B1),(B2) its l_1 mass is <= 2 eps/(c_0 q_0 |tau|) <= |tau|/(c_0 q_0);
 * block window: off-peak k with |tau Omega(k)| <= gap(k)/(2 c_0) [certificate coordinate with radius >= c_0|tau|], plus the common
   peak shift (the "-d w" part);
 * block one-sided: (iii) peak deviations delta_k (relative to the common level), carried vector -(1/tau) sum_P lambda_k sigma_k delta_k u_k;
   (iv) off-peak coordinates with |tau Omega(k)| > gap(k)/(2c_0) (necessarily in the long direction up to O(eps) overshoot, by (K3));
 * peaks with margin mu_k >= eta ("robust") carry, by (K1) (sum_P lambda_k mu_k delta_k <= eps), at most sum lambda_k delta_k/|tau|
   <= eps/(eta |tau|) = O(|tau|/eta): they belong to the remainder; the genuinely one-sided peaks are the WEAK peaks, mu_k < eta.
## 3.3 Proposition (capacities). PROVED.
At scale tau, measured in units of g (i.e. as parts of B or of L*Omega), with eps = s(tau) - 1 <= tau^2/2:
 * remainder (free coordinates, paid usages, robust peaks): l_1 mass <= K(c_0, eta, f)|tau|;
 * one-sided base resources (i) near-contacts, (ii) near-flips: NO a priori bound (free, resp. almost free, at first order);
   they are scale-free resources and can carry O(1) at every scale;
 * peaks: for every mu_* > 0 the carried mass is <= eps/(mu_* |tau|) + (2 s(tau)/|tau|) sum_{k in P, mu_k < mu_*} lambda_k
   [from sum_P lambda_k mu_k delta_k <= eps, i.e. 3.1(K1), and delta_k <= 2 s(tau)]. Hence: robust peaks carry O(|tau|);
   under margin sparsity sum_{mu_k < s} lambda_k = o(s) (C_notes (MS)) all peaks together carry o(1); DEGENERATE peaks (mu_k = 0)
   and near-degenerate coarse peaks are scale-free one-sided resources (like contacts);
 * off-peak coordinates beyond their window: coordinate k carries lambda_k |Omega(k)| <= 2 s(tau) lambda_k/|tau|, and it is beyond the
   window only if gap(k) < 2 c_0 |tau Omega(k)| <= 4 c_0 s(tau). So at depth lambda_k >~ |tau| only near-threshold coordinates
   (gap(k) small) can be one-sided; coordinates with gaps bounded below are one-sided only at depth lambda_k <~ |tau| (Phi_m(k) <~ |tau|).
Summary: one-sided BLOCK resources at scale tau are (a) coordinates of depth Phi_m(k) <~ |tau| (any status), (b) near-threshold
coordinates (small gap or small margin) at any depth; one-sided BASE resources are contacts/near-contacts and near-flip coordinates.
[Proof: 3.1 (B1), (B2), (K1), (K3) and sum_k lambda_k < infinity.]

## 3.4 Lemma (transfer identity). PROVED.
Let t > 0 and let (B+, Omega+) be admissible at scale +t and (B-, Omega-) admissible at scale -t:
  f + t g = (a + t B+) + L*(w + t Omega+),   f - t g = (a - t B-) + L*(w - t Omega-).
Put D := B+ - B-, Omega_D := Omega- - Omega+. Then D = L* Omega_D and
  f = (a + (t/2) D) + L*(w - (t/2) Omega_D),   q*(a + (t/2)D) <= s(t),  N_m(w_m - (t/2)Omega_{D,m}) <= s(t).
*Proof.* B+ + L*Omega+ = g = B- + L*Omega-. Average the two decompositions (f + tg) and (f - tg); convexity of q* and N_m. QED.
So (D, Omega_D) is a "cheap zero-direction transfer": a decomposition of f itself at cost <= s(t), moving the functional
D = L*Omega_D from the blocks to the base. By A Lemma 8.6 (rotundity) a transfer with cost exactly 1 is trivial; cheap transfers
are the second-order flat directions of the decomposition set of f.

## 3.5 Proposition (sign opposition: the one-sided parts of the two sides ADD UP in the transfer). PROVED.
With the notation of 3.4 and paid usages bounded by 3.1:
 (a) contacts/near-contacts: free+ := sum_{K_{c_0}} (sign(z_j) B+_j)_+ and free- := sum_{K_{c_0}} (-sign(z_j) B-_j)_+ satisfy
     free+ + free- <= sum_{j in K_{c_0}} sign(z_j) D_j + 2 eps(t)/(q_0 t) <= ||D 1_{K_{c_0}}||_1 + t/q_0;
 (b) peaks: on P_m, sigma_k Omega_{D}(k) = (delta+_k + delta-_k)/t - (ell+ + ell- - 2M)/t: the transfer's peak profile is a common shift
     plus the SUM of the two sides' (nonnegative) deviations;
 (c) near-flip F-coordinates: if sign(B+_j) = sign(a_j) and sign(B-_j) = -sign(a_j) (cheap on both sides), then |D_j| = |B+_j| + |B-_j|;
 (d) off-peak k used beyond its window on both sides: the long direction is -sign w(k) for tau Omega, i.e. sign Omega+(k) = -sign w(k)
     and sign Omega-(k) = +sign w(k); hence |Omega_D(k)| = |Omega+(k)| + |Omega-(k)|.
*Proof.* (a) z-signed parts: sign(z_j)D_j = sign(z_j)B+_j - sign(z_j)B-_j >= (free+_j - paid+_j) + (free-_j - paid-_j); sum and use 3.1(B1)
(paid usages on K_{c_0} cost at least |t B_j| each). (b) sigma_k W+(k) = ell+ - delta+_k gives sigma_k Omega+(k) = (ell+ - M - delta+_k)/t,
and sigma_k W-(k) = ell- - delta-_k gives sigma_k Omega-(k) = -(ell- - M - delta-_k)/t; subtract. (c),(d): signs. QED.

## 3.6 Corollary (matching at scale, in its true form). PROVED.
For every g in C(f), t > 0 and admissible decompositions at +-t, the one-sided usages of the two sides (classes (i)-(iv)) are
bounded, resource class by resource class, by the one-sided mass of the transfer (D, Omega_D) plus O(t):
  [one-sided(+) + one-sided(-)] <= M_{c_0}(D, Omega_D) + K t,
where M_{c_0} counts sum_{K_{c_0}}|D_j|, the out-of-window F-mass of D, the peak deviation mass sum_P lambda_k|sigma_k Omega_D(k) - common|,
and the beyond-window off-peak mass of Omega_D. Consequently:
 (1) if f admits no cheap transfer with large one-sided mass at scale t ("bounded transfer capacity": sup M_{c_0} over cheap
     transfers at scale t is <= K' t for all small t), then every mate is, at every small scale and on BOTH sides,
     "window + O(t)";
 (2) a defect mate whose decompositions are not "window + O(t)" on either side forces cheap transfers with one-sided mass >> t at
     arbitrarily small scales ("resonance").
(Boundary effects between "window" and "one-sided" are absorbed by using nested thresholds, e.g. windows |tau Omega(k)| <= gap(k)/(2c_0)
and one-sided usage beyond gap(k)/c_0, similarly for F; the domination then holds up to a factor 2 and the O(t) remainder.)
The "matching" requested in the task (one-sided parts agree modulo two-sided resources up to O(t)) is AUTOMATIC: it is the
identity B+ + L*Omega+ = B- + L*Omega-. What does NOT follow is that the matched one-sided parts are small: by 3.5 they are
dominated by the transfer, and cheap transfers with O(1) one-sided mass exist (Theorem 2.4: the exact resonance v = L*D,
v z-signed on an infinite contact set). Y cap c_00 = {0} kills resonances whose base part is FINITELY supported (A Prop 7.4);
it says nothing about infinitely supported contact vectors in Y, nor about approximate block-block relations at scale.

## 3.7 Theorem (exact description of the defect at block-tame first rows). PROVED.
Assume F = supp a is finite and every Q_m (m in I) is finite. Then S(f) is finite dimensional, the map c -> g_c from
certificate data (b in l_1(F) cap zhat-perp, omega_m in R^{Q_m}) to S(f) is injective, and
  cl Cert^sh(f) = Cert^sh(f) = { g_c in C(f) : Hhat(c) <= 1 },   Hhat(c) := min_theta H^sh(c, theta)  (A Def 4.15),
  Def(f) = ( C(f) \ S(f) )  disjoint union  { g_c in C(f) : Hhat(c) > 1 }.
The first piece ("first-order / switching defect") consists of mates that are not certificate directions at all; the second
("second-order / rebalancing defect") of certificate directions that are mates but whose shifted coefficient exceeds 1.
*Proof.* Injectivity: if g_c = 0 then b = -L*(omega - d w) is in Y cap c_00 = {0}, so b = 0 and (T injective) omega_m - d_m w_m = 0;
on a peak this gives d_m = 0, hence omega_m = 0. Closedness: if g_{c_n} -> g_c in the finite-dimensional S(f) with H^sh(c_n, theta_n) <= 1,
then c_n -> c, and theta_n is bounded: max_m(H_m + 2 theta_m) <= 1 gives theta_{n,m} <= 1/2, and h(b) - 2 sum_m theta_m |zeta_m|/q_0 + 2 kappa_q <= 1
with kappa_q >= 0 gives sum_m theta_m|zeta_m| >= -q_0/2, hence a lower bound for each theta_{n,m}. H^sh is continuous in (c, theta)
(v_theta = sum theta_m R_m* w_m ranges in a finite-dimensional subspace of l_1, kappa_q is 1-Lipschitz in l_1), so a limit point theta
gives H^sh(c, theta) <= 1, and C(f) is closed. The minimum defining Hhat is attained by the same compactness. All other known
classes are contained in cl Cert(f) or in cl Cert^sh(f) (part 1, Lemma 1.2, and A Thms 6.2, 6.5, 6.8, D Thm 11.6 via A Thm 6.5). QED.
Remark. At the example of part 2, S(f) = R u and the first piece is infinite dimensional. Whether the second piece can be
nonempty in a Martin-type space is OPEN (the referee's finite-model computations, A_referee §4 e3_gauge, show true local
coefficient < H^sh in all seeds and H^sh(normalized mate) > 1 in 3 of 14 seeds, suggesting that it can).

## 3.8 Corollary (C-tame first rows: the switching defect is empty). PROVED modulo C_notes Thm 6.4, Prop 6.5, Lemma 5.2
## (Round 1, unrefereed; the parts used are re-derived below).
Assume f is C-tame: a in c_00, K finite, Qbar_m := Q_m cup Dg_m finite (Dg_m = degenerate peaks, alpha_{m,k} = 0), and margin sparsity
(MS) sum_{k in P_m, 0 < mu_k < s} Phi_m(k) = o(s). Then C(f) is contained in S(f); hence (3.7) Def(f) = { g_c in C(f) : Hhat(c) > 1 }:
at C-tame points only the second-order (rebalancing) defect can occur.
*Proof.* By C Thm 6.4, every g in C(f) has a unique representation g = b + sum_m R_m*(omega_m + c_m w_m), supp b in F cup K,
supp omega_m in Qbar_m, and by C Prop 6.5, b(xi) = 0 and c_m = -d_m when omega_m lives on Q_m. It remains to kill b on K and omega_m on Dg_m.
Primal test (C Lemma 2.2): g in C(f) iff xi(g) = 0 and nu(g)^2 <= phi(nu)(2 + phi(nu)) for nu in ker f, phi(nu) = p**(xi + nu) - 1.
Let J := N \ (F cup K) and psi_i the (finitely many) restrictions to J of u_{k,m} (k in Qbar_m) and R_m* w_m; they are linearly independent
on c_00(J) (Y cap c_00 = {0}, T injective; C §1.4 (F5)).
 (a) j in K: put nu := -z_j e_j + nu_J with nu_J in c_00(J) such that psi_i(nu) = 0 for all i (possible by independence). For s > 0 small,
     xi + s nu moves the contact j inward (|z_j - s/q_0| < 1) and finitely many free coordinates slightly: q**(xi + s nu) = q_0 and a(nu) = 0,
     so the base excess vanishes; in each block R_m nu vanishes on Qbar_m and has zero peak sum (w_m(R_m nu) = R_m* w_m(nu) = 0), so by the
     overshoot bound (C Lemma 5.2) E_m(s R_m nu) <= 2 m s q(nu) sum_{k in P_m : 0 < mu_k < s q(nu)} Phi_m(k) = o(s^2) (MS; degenerate peaks
     carry no u-component of nu, since u_{k,m}(nu) = 0 for k in Dg). Also f(nu) = 0. Hence phi(s nu) = o(s^2), and the mate inequality gives
     nu(g) = 0. But nu(g) = b(nu) + sum (omega + c w)-terms = -z_j b_j (all u_{k,m}, k in Qbar, and R_m* w_m vanish at nu; b vanishes on J).
     So b_j = 0.
 (b) k in Dg_m: choose nu in c_00(J) with u_{k,m}(nu) = sigma_k := sign w_m(k), and with all OTHER functionals of the finite list vanishing at nu
     (u_{k',m'}(nu) = 0 for k' in Qbar_{m'}, (k',m') != (k,m), and R_{m'}* w_{m'}(nu) = 0 for all m'; possible by independence). Then R_m nu
     vanishes on Qbar_m \ {k}, has zero peak sum (w_m(R_m nu) = R_m* w_m(nu) = 0 and R_m nu vanishes on Q_m), and its k-th entry
     lambda_k sigma_k moves the degenerate peak OUTWARD for s > 0: in the overshoot bound (C Lemma 5.2) the term 2(-sigma_k s (R_m nu)_k - |zeta||alpha_k|)_+
     is 0 (alpha_k = 0, sigma_k s (R_m nu)_k > 0), the other degenerate peaks do not move, and the non-degenerate peaks contribute o(s^2)
     by (MS). The base excess vanishes (free coordinates only), the other blocks contribute o(s^2) as in (a), and f(nu) = 0. Hence
     phi(s nu) = o(s^2) for s > 0, so nu(g) = 0; but nu(g) = sum_{m'} <omega_{m'} + c_{m'} w_{m'}, R_{m'} nu> = lambda_k sigma_k omega_m(k). So omega_m(k) = 0.
Thus g = b + sum R_m*(omega_m - d_m w_m) with supp b in F, omega_m in c_00(Q_m): g in S(f). QED.
Remark. Together with Theorem 2.4 this locates the switching defect precisely: it needs infinitely many one-sided coordinates of the
base (contacts/near-flips) — exact resonance — or infinitely many near-threshold block coordinates — approximate resonance
(part 4); it is absent at C-tame points, where only the second-order defect {Hhat > 1} may survive (OPEN whether nonempty).
# P1 part 4: resonance types; cross-block near-duplicates; a weighted averaging theorem

## 4.1 Proposition (exact resonances need infinitely many one-sided base coordinates). PROVED.
Let (D, Omega_D) with D = L*Omega_D != 0, Omega_D in V*, and suppose that for a sequence s_n -> 0+ the transfers
f = (a + s_n D) + L*(w - s_n Omega_D) have cost <= s(2 s_n) (an "exact", scale-free resonance). Then
  kappa(D) := sum_{j notin F} (|D_j| - z_j D_j) = 0,
i.e. off F the vector D lives on the contact set K with the sign of z; D is in Y \ {0}, hence not in c_00; so F cup K is infinite.
In particular: at every NA point, and at every f with a in c_00 and K finite, there are no exact resonances (cf. A Prop 7.4).
*Proof.* q*(a + sD) >= 1 + s D(zhat) + s kappa(D) (one-sided derivative of q* at a, A Lemma 7.2), and N_m(w_m - s Omega_m) >=
1 - s <Omega_m, zeta_m>/|zeta_m|. Both are <= s(2s) = 1 + O(s^2); divide by s, let s = s_n -> 0, multiply the block inequalities
by |zeta_m| and the base inequality by q_0, add: q_0 D(zhat) - <Omega_D, L**xi> + q_0 kappa(D) <= 0. The first two terms cancel
(D(xi) = <Omega_D, L**xi> since D = L*Omega_D, and D(xi) = q_0 D(zhat)), so kappa(D) <= 0, hence = 0. D in Y \ {0} and
Y cap c_00 = {0}. QED.
So there are two resonance types: (R-exact) scale-free transfers through infinite contact sets (or near-flip sets when a is not
in c_00) — Theorem 2.4 realizes this; (R-approx) scale-dependent transfers, in which one-sided carriers at depth Phi ~ t
(weak peaks, near-threshold off-peak coordinates, near-contacts) approximately represent the same functional on the two sides.

## 4.2 Proposition (sign rule; which side a one-sided carrier serves). PROVED.
For every block m and k with u_{k,m}(xi) != 0: sign w_m(k) = sign u_{k,m}(xi) (on P by Fact C: sign zeta(k) = sign alpha_k =
sigma_k; off P: w(k) = C zeta(k)/(Phi_k^2|zeta|)). A one-sided usage of (k,m) at scale tau (inward peak deviation, or an off-peak
push beyond the gap in the long direction) has sign(tau Omega(k)) = -sign u_{k,m}(xi). Hence, if (k,m) carries tau c v with
c > 0 and u_{k,m} close to v, then sign(tau) = -sign u_{k,m}(xi): carriers with u(xi) < 0 serve tau > 0, carriers with
u(xi) > 0 serve tau < 0. One-sided carriers are near or above the threshold: |u_{k,m}(xi)| >= (1 - gamma) theta_m Phi_m(k) with
gamma the relative gap (gamma = 0 for peaks). Consequently two carriers (k,m), (k',m') can SWITCH (serve opposite sides) only if
  ||u_{k,m} - u_{k',m'}||_{q*} q**(xi) >= (1 - gamma) theta_m Phi_m(k) + (1 - gamma') theta_{m'} Phi_{m'}(k').
*Application to Martin's built-in cross-block near-duplicates.* If u_{n,m} and u_{n,m'} follow the same w'_n up to a perturbation
that is o(Phi) in the xi-direction (in particular exact duplicates), then u_{n,m}(xi) and u_{n,m'}(xi) have the same sign whenever
they are near the threshold: such pairs serve the SAME side and cannot switch with each other. Switching between near-duplicates
requires perturbations of order >= Phi in the xi-direction AND placement of the two members on opposite sides of 0 near their
respective thresholds. Lemma B's conclusion neither forces nor excludes this (cf. Remark 2.1.1: such pairs can be inserted).

## 4.3 Theorem (weighted averaging). PROVED.
Let g in C(f), rho in (0,1). Suppose there are finite certificates c_1, ..., c_n at f and weights mu_i >= 0, sum mu_i = 1, with
coordinatewise radii r_i := r^cw(c_i) > 0 and errors e_i := p*(g - g_{c_i}), and numbers s_0 in (0, min(1, sqrt(1-rho^2))],
eta_0, kappa_0 >= 0 with rho^2 (1+eta_0)(1+kappa_0) <= (1+rho^2)/2, such that
 (i) H(c_i) <= 1 + eta_0 and kappa(c_i) r_i <= kappa_0 for all i;
 (ii) for every s in (0, s_0]:  sum_{i : r_i < rho s} mu_i e_i <= (1 - rho^2) s/(12 rho);
 (iii) sum_i mu_i e_i <= (1 - rho^2) s_0/(3 rho).
Then rho g_c is in Cert(f) for c := sum_i mu_i c_i, and ||rho g_c - rho g||_{p*} <= rho sum_i mu_i e_i.
Consequently, if for every rho < 1 and eps > 0 such families exist with sum mu_i e_i <= eps, then g in cl Cert(f).
*Proof.* As in A Thm 6.8. By convexity p*(f + s rho g_c) <= sum_i mu_i p*(f + s rho g_{c_i}). For i with r_i >= rho|s| use
A Prop 4.5 (with the coordinatewise radius, referee fix G1): p*(f + s rho g_{c_i}) <= 1 + (rho^2 s^2/2) H(c_i)(1 + kappa(c_i) rho|s|)
<= 1 + (s^2/2)(1+rho^2)/2. For r_i < rho|s|: p*(f + s rho g_{c_i}) <= s(rho s) + rho|s| e_i (g in C(f)). Hence for |s| <= s_0,
p*(f + s rho g_c) <= max(1 + s^2(1+rho^2)/4, s(rho s)) + (1-rho^2)s^2/12 <= s(s) (the two cases exactly as in Thm 6.8, using
s^2 <= 1 - rho^2 and s(s) - s(rho s) >= (1-rho^2)s^2/3). For |s| >= s_0: p*(f + s rho g_c) <= s(rho s) + rho|s| sum mu_i e_i
<= s(rho s) + (1-rho^2)s_0|s|/3 <= s(s). H(rho c) <= rho^2 max_i H(c_i) <= 1 by convexity of H. QED.

## 4.4 Corollary (near-threshold carriers with non-summable gaps are not a defect source). PROVED.
Let g in C(f) and suppose there are a finite certificate c^0, a real c != 0 and strict non-peaks (k_i, m_i), i >= 1, with
lambda_i := lambda_{k_i,m_i}, gamma_i := gap_{m_i}(k_i), such that
 (a) lambda_{i+1} <= lambda_i/2 and gamma_i is nonincreasing;
 (b) p*(g - g_{c^0} - c u_{k_i,m_i}) <= K lambda_i;
 (c) limsup_i H(c^0 + (0, (c/lambda_i) e_{k_i} in block m_i)) <= 1;
 (d) sum_i gamma_i = infinity.
Then g in cl Cert(f). (Thm 6.8/Cor 6.10(c) is the case inf gamma_i > 0.)
*Proof.* c_i := c^0 + (c/lambda_i)e_{k_i}. Its d-coefficient d_i = c Phi_i w(k_i)/(m_i C) -> 0, so for large i the coordinatewise radius is
r_i = min(r(c^0), gamma_i lambda_i/(2|c|)) = gamma_i lambda_i/(2|c|), kappa(c_i) is bounded, kappa(c_i) r_i -> 0, and
e_i <= K lambda_i + |d_i| p*(R*w) <= K' lambda_i. Fix rho; choose eta_0, kappa_0, s_0 as in 4.3. On a stretch i_0 <= i <= i_1 put
mu_i := gamma_i/Gamma, Gamma := sum_{i_0}^{i_1} gamma_i. Since gamma_i lambda_i decreases at least by the factor 1/2,
sum_{i : r_i < rho s} mu_i e_i <= (K'/Gamma) sum_{i : gamma_i lambda_i < 2|c| rho s} gamma_i lambda_i <= 4 K'|c| rho s/Gamma,
which is <= (1 - rho^2)s/(12 rho) once Gamma >= 48 K'|c| rho^2/(1 - rho^2); by (d) such stretches exist with i_0 arbitrarily large, and
then sum mu_i e_i <= 2K' lambda_{i_0} is as small as we like ((iii) and the approximation). (i) holds for i_0 large by (c). QED.
Remarks. (1) Uniform weights (Thm 6.8) need inf gamma > 0; the gap-proportional weights need only sum gamma_i = infinity
(e.g. gamma_i ~ 1/i suffices). (2) For sum gamma_i < infinity the single-coordinate averaging fails (with mu_i <= A gamma_i forced
by (ii) at s ~ gamma_i lambda_i, sum mu_i <= A sum gamma_i). Whether such "super-near-threshold" switching mates lie in cl Cert(f) is
OPEN: there is no linear obstruction (their limit direction v is in cl S(f), being a limit of strict non-peak vectors), so
part 1's method does not apply; a proof of non-membership would need a quantitative obstruction (e.g. a sequence test
f_n -> f with g notin Li C(f_n), using that cl Cert(f) is contained in Li C(f_n) for every sequence, A Cor 4.11).
(3) Weak-peak carriers (margins mu_k -> 0 relative to Phi_k) are never certificate coordinates; switching mates carried only by
weak peaks on both sides are outside the scope of every averaging argument and are the approximate analogue of Theorem 2.4.
# P1 part 5: the dual (support-function) route

## 5.1 Proposition (support-function criterion; reduction to c_0-exposed mates). PROVED.
Let A subset B be norm-compact convex symmetric subsets of l_1 = c_0* (e.g. A = cl Cert^sh(f), B = C(f), both norm compact:
A Thm 3.1). Then
 (a) A = B iff h_A(x) = h_B(x) for all x in a dense subset of c_0 (h_K(x) := max_{k in K} k(x));
 (b) A != B iff some c_0-EXPOSED point of B (the unique maximizer over B of some x in c_0) lies outside A; the set
     {x in c_0 : h_A(x) < h_B(x)} is then open and nonempty, and it contains a dense G_delta subset of exposing vectors.
*Proof.* (a) |h_K(x) - h_K(y)| <= (sup_K ||k||_1) ||x - y||_inf, and weak*-compact convex sets are separated by elements of c_0.
(b) If b in B \ A, separation gives x_0 with b(x_0) > h_A(x_0), hence h_B > h_A on a ball V around x_0. By Mazur's theorem (c_0
separable) the continuous convex function h_B is Gateaux differentiable on a dense G_delta G; for x in G its subdifferential, which
is the face argmax_B x (weak*-compactness of B), is a singleton {b_x}; for x in V cap G, b_x(x) = h_B(x) > h_A(x), so b_x is not in A. QED.

## 5.2 Proposition (scale-by-scale formula). PROVED.
C(f) = intersection over t != 0 of C_t := {g : p*(f + t g) <= s(t)} = (s(t) B_{p*} - f)/t, with
  h_{C_t}(x) = (s(t) p(x) - sign(t) f(x))/|t|,   min_{t != 0} h_{C_t}(y) = r_f(y) = sqrt(p(y)^2 - f(y)^2),
and r~_f(x) = h_{C(f)}(x) = inf { sum_i h_{C_{t_i}}(x_i) : sum_i x_i = x } (finite families), which is (R2).
*Proof.* The C_t are weak*-compact convex and contain 0; the support function of an intersection of such sets is the
weak*-lsc closure of the inf-convolution of their support functions, here a finite continuous sublinear function, hence equal to
it. The one-scale minimum: with t = tan(theta), h = (P - F cos theta)/sin theta (P = p(y), F = |f(y)|) is minimized at cos theta = F/P
with value sqrt(P^2 - F^2). QED.
Reading. The one-scale sets C_t are DECOMPOSITION-BLIND: they only see p*. Certificates, in contrast, are defined through the
forced decomposition and require one TWO-SIDED linear structure valid on a whole window of scales |tau| <= r(c). The variational
characterization therefore gives no handle on which decompositions realize the optimal mate: the maximizer g_x of a given x
over C(f) is only characterized by complementary slackness with the active scales/pieces of a minimizing family in 5.2, and
nothing in that characterization produces two-sided structure.

## 5.3 Proposition (explicit failure of "certificates achieve r~_f"). PROVED.
At the first row f of part 2 take j_1, j_2 in K' (j_1 != j_2) and x_* := e_{j_1} - (u(j_1)/u(j_2)) e_{j_2} in c_00 (u := u_{2,1}). Then
  h_{cl Cert^sh(f)}(x_*) = 0 < c u(j_1) <= r~_f(x_*),
and by 5.1(b) there is an open set of x near x_* whose exposed mates lie in Def(f).
*Proof.* cl Cert^sh(f) is contained in R u (Thm 2.4) and u(x_*) = 0. The mate g := g_{K_1} of Prop 2.3 with j_1 in K_1, j_2 notin K_1
satisfies g(x_*) = c u(j_1) - beta a(x_*) = c u(j_1) > 0 (a(x_*) = 0 since 1 notin {j_1, j_2}). QED.

## 5.4 Conclusion for the dual route (PROVED statements / HEURISTIC reading).
 * (PROVED) The defect is detectable from c_0: Def(f) != empty iff h_{cl Cert^sh(f)} < r~_f somewhere on c_0, iff some c_0-exposed
   mate is outside cl Cert^sh(f) (5.1). So it suffices, in any future positive attempt, to treat EXPOSED mates.
 * (PROVED) A scale-by-scale variational argument cannot show h_{cl Cert^sh(f)} = r~_f in general (5.3); the gap is produced
   exactly by the exact resonance (part 2/4.1): in the minimizing families of 5.2 for x_*, the active pieces live at both signs of
   t and the optimal mate uses the contact set K_1 on one side and the carrier plus K_2 on the other.
 * (HEURISTIC) In positive situations (no resonances, part 3.6(1)) the right dual statement would be: for every exposed mate g_x,
   the optimal pieces at scale t can be chosen "window + O(t)" on one side; by Thm 6.8 this would give g_x in cl Cert(f). The
   shift problem (Thm 3.7, second piece) remains: the window parts are only controlled in the weighted sense Gamma_w <= 1 + o(1)
   (C_notes Prop 8.1), not in the max sense H <= 1, unless the blocks' first-order coefficients vanish.
# P1 part 6: the whole fibre at the example, and engineered recovery of its defect

Setting of part 2 (T from 2.1, f from 2.2, u := u_{2,1}, lambda_0 := lambda_{2,1} = Phi_1(2), K' contacts, J := N \ ({1} cup K')
free coordinates (z = 0 there)). eps := s(t) - 1.

## 6.0 Lemma (margins at f). PROVED.
mu_{k,m} := |u_{k,m}(xi)| - theta_m Phi_m(k) >= q_0 psi(Phi_m(k)) for every peak, psi(phi) := min(1/4, 2 sqrt(phi)).
*Proof.* Non-exceptional k >= 2: |u(xi)| = q_0|u(zhat)| >= 1.6 q_0 rho_l (2.1(P3)), theta Phi <= q_0 pi_{k,m} <= q_0 rho_l^2 <= q_0 rho_l/26
(proof of 2.2(b)), rho_l = sqrt(2 Phi_m(k)/c_{l(1,m)}) >= sqrt(2 Phi_m(k)); so mu >= 1.5 q_0 rho_l >= 2 q_0 sqrt(Phi_m(k)).
Exceptional: |u(zhat)| > 1/2 and pi <= 1/4. k = 1: |u_{1,m}(zhat)| >= 7/9 and theta_m Phi_m(1) <= |zeta_m|/m <= q_0/2. QED.

## 6.1 Theorem (C(f) is contained in E_u). PROVED.
  E_u := { g in l_1 : supp g in {1} cup K', g(xi) = 0, theta(g) := (g_j/u_j)_{j in K'} is bounded }.
More precisely, if g in C(f), then for admissible decompositions at scales t_n -> 0+ (resp. -t_n) the carrier coefficients
mu_n := lambda_0 Omega_{t_n,1}(2) are bounded, and any limit mu+ (resp. mu-) satisfies mu+ <= g_j/u_j <= mu- for all j in K'.
*Proof.* Fix an admissible decomposition (B, Omega) at scale t > 0 (t <= t_1 small). Block m: level l_m := ||W_m||_inf, peak deviations delta_k.
(1) Peaks carry o(1): by 3.1(K1) and |alpha_k| = lambda_k mu_k/|zeta_m|, sum_P lambda_k mu_k delta_k <= eps. Split at Phi_m(k) = t^{4/3}:
    sum lambda_k delta_k <= eps/(q_0 psi(t^{4/3})) + 2 s(t) m sum_{Phi_m(k) < t^{4/3}} Phi_m(k) <= C_1 t^{4/3}
    (Phi_m(k) is decreasing in k with ratio <= 1/2, so the last sum is <= 2 t^{4/3}). Hence (1/t) sum lambda_k delta_k <= C_1 t^{1/3}.
(2) Level shifts are o(t): by the first-order balance (N_m(W_m) >= 1 + t<Omega_m, zeta_m>/|zeta_m|, q*(a+tB) >= 1 + tB(zhat), and
    q_0 B(zhat) + sum_m <Omega_m, zeta_m> = g(xi) = 0) one gets |t <Omega_m, zeta_m>| <= eps for every m. On P_m, t Omega_m(k) =
    sigma_k(l_m - M_m - delta_k); the only strict non-peak (2,1) has zeta_1(2) = 0. So
    (l_m - M_m) sum_{P_m}|zeta_m(k)| = t<Omega_m, zeta_m> + sum_P delta_k |zeta_m(k)|, and |zeta_m(k)| <= q_0 lambda_k, sum_P |zeta_m(k)| >= |zeta_m(1)| > 0:
    |l_m - M_m| <= C_2 t^{4/3}.
(3) Carrier bounded: D_1 e_2 is orthogonal to D_1 w_1 (w_1(2) = 0), so ||P-perp D_1 Omega_1|| >= Phi_1(2)|Omega_1(2)| = |mu_t|
    (m = 1), and 3.1(K2) gives mu_t^2 <= 2 s(t)^2/|zeta_1| <= 3/|zeta_1|.
(4) Decomposition of g: L*Omega = mu_t u + sum_m R_m*(Omega_m 1_{P_m}), and
    R_m*(Omega_m 1_{P_m}) = ((l_m - M_m)/(t M_m)) R_m* w_m - (1/t) sum_P lambda_k sigma_k delta_k u_k
    (w_m 1_{P_m} = w_m since w_1(2) = 0), whose l_1 norm is <= C_3 t^{1/3}. Hence ||g - B - mu_t u||_1 <= C_4 t^{1/3}.
(5) Free coordinates: by 3.1(B1) with z = 0 on J, ||B 1_J||_1 <= eps/(q_0 t) <= t/(2 q_0); u vanishes on J. So ||g 1_J||_1 <= C_5 t^{1/3},
    and letting t -> 0: g = 0 on J, i.e. supp g in {1} cup K'.
(6) Contacts (z = 1 on K'): the paid usage is sum_{K'} (B_j)_- <= eps/(2 q_0 t) (3.1(B1)), so sum_{K'} (g_j - mu_t u_j)_- <= C_6 t^{1/3}.
    Along t_n -> 0 with mu_{t_n} -> mu+: g_j >= mu+ u_j for all j in K'. The side t < 0 is symmetric (cheap sign of B_j is now
    negative): g_j <= mu- u_j. Since u_j > 0 on K', g_j/u_j in [mu+, mu-]. QED.
So C(f) lies in the infinite-dimensional space E_u, while cl Cert^sh(f) lies in the line R u (Theorem 2.4).

## 6.2 Proposition (a large slab of E_u consists of mates). PROVED.
There is theta_* > 0 such that every g in E_u with ||theta(g)||_inf <= theta_* lies in C(f).
*Proof.* As 2.3, with mu+ := inf theta(g), mu- := sup theta(g): side + f + t g = (a + t(g - mu+ u)) + L*(w + t(mu+/lambda_0) e_2), where
g - mu+ u is supported on {1} cup K', >= 0 on K' (cheap for t > 0), and (g - mu+ u)(zhat) = g(zhat) = 0; side - with mu- (<= 0 on K').
The base costs are Hilbert terms O(t^2 ||theta||^2), the block cost is t^2 (mu+-)^2/(2 C_1), the e_1*-coefficient stays positive;
the crude bound handles |t| >= 1. QED.
Consequently Def(f) contains { g in E_u : ||theta(g)||_inf <= theta_*, theta(g) not constant } (infinite dimensional).

## 6.3 Proposition (engineered recovery of the explicit switching mates). SKETCH (all estimates indicated).
Let g in E_u, theta := theta(g), mu+ := inf theta, mu- := sup theta, and let kappa+- := max( h(g - mu+- u), (mu+-)^2/C_1 ) be the
second-order coefficients of the explicit side decompositions of 6.2 (h = base Hilbert coefficient, A Def 4.1). If rho^2 max(kappa+, kappa-) < 1,
then (f, rho g) is in cl NA((c_0,p), l_2^2).
Construction (parameters: window N, mass scale t_m, a finite far set Far, cut-off N'', and mu_inf in [mu+, mu-]):
 * target: g' := g 1_{{1} cup (K' cap [1,N])} + mu_inf u 1_{K' cap (N, infinity)} + (multiple of a' making g'(x') = 0); ||g' - g|| <= 2||theta||_inf sum_{K'>N} u_j + o(1);
 * base: a' := normalization of a + sum_{j in K', j <= N} m_j e_j* + (tuning masses at contacts) - sum_{j in Far} m'_j e_j*, with window masses
   m_j := 2 t_m |theta_j - mu_inf| u_j + t_m u_j > 0 and far masses m'_j := 2 T_0 (|mu+| + |mu-| + |mu_inf|) u_j;
 * contact vector: z' := 1 on {1} cup ((K' cap [1, N'']) \ Far), z' := -1 on Far, z' := 0 elsewhere (z' in c_0, z' -> z coordinatewise);
   here Far is a finite subset of K' cap (N, N''] whose u-mass sum_{Far} u_j is of order t_m (needed in (i));
 * order of choices: N (window), then t_m <= c tau_N with tau_N := sum_{K' > N} u_j (so that Far fits into K' cap (N, infinity)),
   then Far and the tuning masses (by continuity, (i)), then N'' >= max Far so large that sum_{K' > N''} u_j <= (1 - rho^2) t_m/(48 S),
   S := |mu+| + |mu-| + |mu_inf|;
 * x' := z' + U e', e' := U*a'/||U*a'||, f' := grad p(x'/p(x')) = a' + L* J_V(L x') (A Fact D): NA.
(i) Exact carrier. u(x') = <U*u, e' - e> - sum_{K'} u_j (1 - z'_j) (using u(zhat) = 0). Positive tuning masses at a contact j_+ with
  <P_e-perp U*u, U*e_{j_+}*> > 0 raise the first term (j_+ exists: sum_{K'} u_j <P_e-perp U*u, U*e_j*> = ||P_e-perp U*u||^2 > 0, and the
  coordinate 1 contributes 0); the far coordinates (z' = -1) lower the second term by 2 sum_{Far} u_j ("free pulls"); a continuous parameter
  (a partial value of z' on one far coordinate) gives u(x') = 0 exactly (the far masses' own effect on the first term is
  O(T_0 S sum_{Far} u_j nu_j) with nu_j = ||U*e_j*|| -> 0, negligible against the pull 2 sum_{Far} u_j once N is large). Then zeta'_1(2) = 0, w'_1(2) = 0, k = 2 is again a strict
  non-peak of block 1 (gap M'_1), and R_1*((mu/lambda_0) e_2) = mu u is carried by block 1 at cost M'_1 + sqrt(C'^2 + t^2 mu^2) for every mu.
(ii) Small scales |t| <= t_m: f' + t rho g' = (a' + t rho (g' - mu_inf u)) + L*(w' + t rho (mu_inf/lambda_0) e_2). The base part
  g' - mu_inf u = (theta - mu_inf) u on the window, 0 on K' beyond N (this is why the tail of g' is mu_inf u), plus a multiple of a':
  it is supported in supp a' and the window masses exceed |t rho (theta_j - mu_inf) u_j|: no flips, no kinks, first-order term
  rho t (g' - mu_inf u)(x̂') = 0. Its coefficient is max(h'(g' - mu_inf u), mu_inf^2/C'_1) -> max(h(g - mu_inf u), mu_inf^2/C_1) <= max(kappa+, kappa-)
  by convexity of mu -> max(h(g - mu u), mu^2/C_1) on [mu+, mu-]. A two-sided finite certificate at f' with coefficient < 1/rho^2 (approximately).
(iii) Intermediate scales t_m <= |t| <= T_0: side + uses mu+, side - uses mu-. Base part g' - mu+- u: on the window (theta - mu+-)u has the cheap
  sign (window contacts with masses); on K' cap (N, N''] the entries (mu_inf - mu+-)u_j have the cheap sign at the contacts z' = 1; on Far
  they are absorbed by the far masses (|t| |mu_inf - mu+-| u_j <= m'_j: |A_j| - z'_j A_j = 0); beyond N'' (z' = 0) the first-order cost is
  <= |t| |mu_inf - mu+-| sum_{K' > N''} u_j <= (1 - rho^2) t^2/24 for |t| >= t_m, once N'' is chosen large AFTER t_m. Second-order terms -> kappa+-.
(iv) Large scales |t| >= T_0: slack (A Lemma 4.7): p*(f' - f) -> 0 (a' -> a in l_1, z' -> z coordinatewise, A Fact E / G Prop 6.6.3) and
  ||rho g' - rho g|| -> 0 as N -> infinity, t_m -> 0, Far -> infinity.
Hence for suitable parameters (f', rho g') is contractive and attains its norm at x'/p(x'), and (f', rho g') -> (f, rho g).
(The bookkeeping of the second-order terms at f' versus f is the same as in C Thm 7.1 / D Lemmas 11.3-11.4: finitely many changed
coordinates in each Hilbert term and e' -> e.)
Remark (correction to A_referee §5.4). The referee enforces u(x'') = 0 "by one extra degree of freedom in the masses". When every
available positive-mass direction RAISES u(x'') (e.g. U diagonal: <U*u, e'' - e> = sum_{K'} u_j sigma_j^2 m_j/nu + O(m^2) >= 0), the deficit
must be compensated by pulling contacts inward, which costs |t| x O(t_m) at first order on one side, comparable to the slack exactly
at the scale t_m where the masses are needed, with a constant that blows up as rho -> 1. The far NEGATIVE masses (sign-flipped far
contacts: allowed, because z' only has to converge coordinatewise) remove this obstruction. Also the referee's truncation of g must be
replaced by the constant tail mu_inf u (otherwise the carrier's tail costs first order at the smallest scales).
Remark (what is missing for f in R). By 6.1 every mate g lies in E_u, but 6.3 needs rho^2 max(kappa+, kappa-) < 1 for the EXPLICIT side
decompositions. For g in C(f) the actual optimal decompositions may be cheaper (second-order rebalancing through shifts, A §4.5); recovery
of all of C(f) would follow if the explicit decompositions, possibly shifted along R_m* w_m (shifts transport, A Thm 4.17), were
asymptotically optimal. Not proved (HEURISTIC: by the proof of 6.1, peaks, level shifts and free coordinates contribute only o(1) in
g-units, but they may contribute O(t^2) to the costs).

# 7. What remains, corrections to the sources, next steps

## 7.1 Corrections / sharpenings of Round-1 statements
 * A_notes Conjecture 7.5 ("scale separation of T => Def(f) empty for every f"): cannot hold as stated. Theorem 2.4 produces a
   nonempty defect through an EXACT resonance, which involves no approximation rates at all (the construction of 2.1 can be done
   with all non-special vectors as "generic" as one likes). This confirms rigorously the referee's objection (A_referee §3.5).
 * A_referee §5.2 (two-piece mates, SKETCH with a generic existence step): made rigorous for the T of 2.1 (2.3), together with
   their membership in Def(f) (2.4), which the referee left OPEN.
 * A_referee §5.4 (engineered recovery, SKETCH): the "extra degree of freedom in the masses" can fail (e.g. diagonal U: every
   admissible positive mass raises u(x'')); compensating by pulling contacts inward costs first order at exactly the scale where
   the masses are needed, with a constant that blows up as rho -> 1. Fix: far sign-flipped contacts with negative masses ("free
   pulls"); and the truncated target must carry a constant tail mu_inf u (6.3).
 * BRIEFING_R2 / task text: "one-sided resources at scale t only carry mass from coordinates with Phi_m(k) <~ |t| (or contacts)" is
   true only for coordinates whose gaps/margins are bounded below; near-threshold coarse coordinates and degenerate peaks are
   scale-free one-sided resources (3.3).
 * BRIEFING_R2: "cross-block near-duplicates are built in, so scale separation cannot be assumed": by the sign rule (4.2) exact or
   o(Phi)-perturbed duplicates serve the SAME side and cannot switch with each other; switching needs perturbations >~ Phi in the
   xi-direction with opposite signs, and then (4.4) the mate is in cl Cert(f) unless the gaps are summable.

## 7.2 Precise open problems left by P1
 (O1) Second-order defect: is there f (e.g. C-tame) and g_c in C(f) with Hhat(c) > 1? Equivalently: are A's shifts along R_m* w_m
      the last layer of second-order rebalancing? Natural further layers: (a) GENERAL shifts tau^2 Theta with Theta_m = theta_m w_m + eta_m,
      eta_m finitely supported off-peak (A Remark 4.19; base pays tau^2[<Theta, L**xi>/q_0 + kappa(-L*Theta)], block m gains
      -tau^2 <Theta_m, zeta_m>/|zeta_m|) — these are NOT in Cert^sh as defined, so relative to Cert^sh the second piece of 3.7 may already
      be nonempty for this trivial reason; the transport of such shifts is the same as A Thm 4.17 (SKETCH in A), so the class should be
      enlarged accordingly; (b) shifts along weak peaks (block gain Phi_k^2 M/C per unit inward deviation, base cost
      lambda_k(|u_{k,m}(zhat)| + kink(sigma_k u_{k,m}))): competitive only if |u_{k,m}(zhat)| and the kink are O(Phi_k), i.e. through an
      approximate resonance between a weak peak and a kink-free base vector; under (MS) (C-tame f) such peaks are too sparse,
      so at C-tame f layer (b) should be negligible (HEURISTIC). Needed positive tool in any case: an averaging theorem for
      (generalized) shifted certificates with a uniform remainder (A Remark 4.19), plus their transport.
 (O2) Approximate resonances with summable gaps or weak-peak carriers (4.4 Rem): no linear obstruction; a proof of non-membership
      in cl Cert(f) would need a sequence test (find f_n -> f in S_{p*} with g notin Li C(f_n); cl Cert(f) is in Li C(f_n) for every
      sequence).
 (O3) General T: does every admissible T admit f with Def(f) != empty? Two-piece mates exist whenever the (generic) first step of
      A_referee §5.2 can be carried out for some block vector (presumably for every T), but the linear obstruction needs a block-tame f, i.e. a zhat avoiding the slabs |u_{k,m}(zhat)| <= theta Phi_m(k)
      for all but finitely many (k,m); for an adversarial T this may be impossible (Preprint A's residuality of half-peaks).
 (O4) Recovery: prove f in R for the example (all of C(f), not only the explicit switching mates): needs asymptotic optimality of
      the explicit (possibly shifted) decompositions (6.3 Remark). More generally: an engineering theorem for EXACT resonances
      (far negative masses + constant tails + exact carriers) at arbitrary f with infinite contact sets.

## 7.3 Recommendation
The intrinsic program "every mate lies in cl Cert(f)" is dead (Theorem 2.4). The density proof must recover the resonant part of
the fibre along ENGINEERED NA sequences. The present notes show that this is feasible for exact resonances in the explicit
example (6.3) and give the precise list of what an engineered recovery must handle: (i) exact carriers (enforce u(x') = 0 by
masses and free pulls), (ii) window masses for the smallest scales, (iii) far sign-flipped contacts, (iv) constant tails of the
target, (v) the second-order coefficients of the explicit side decompositions. The next step is a general "resonance recovery
theorem" covering mates whose decompositions are, on each side, certificate + exact-resonance part + O(t).
