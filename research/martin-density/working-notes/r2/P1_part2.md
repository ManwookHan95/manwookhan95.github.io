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
