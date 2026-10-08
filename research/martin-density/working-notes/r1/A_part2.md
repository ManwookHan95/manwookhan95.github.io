---------------------------------------------------------------------------------------------------

## 4. Finite certificates, the NA-scale criterion, and the Transport Theorem

Throughout this section f is in S_{p*} with forced data (xi, q_0, a, w, z, e, nu, zhat = z + U e) and, for each block m,
(zeta_m, M_m, C_m, P_m, alpha_m, gap_m(k) = M_m - |w_m(k)|). Block indices are suppressed when only one block is involved.

### 4.1 Definitions
**Definition 4.1.** A *finite certificate* at f is c = (b, omega), omega = (omega_m)_{m in I}, such that
* (C1) b is in l_1, supp b is contained in supp a, ||b/a||_infinity := sup_{j in supp a} |b_j|/|a_j| < infinity, and b(zhat) = 0
  (equivalently b(xi) = 0);
* (C2) each omega_m is in c_00 with supp omega_m disjoint from P_m, and omega_m = 0 for all but finitely many m.

Associated quantities:
* d_m := <D_m w_m, D_m omega_m>/C_m, and the *direction* g_c := b + sum_m R_m*(omega_m - d_m w_m);
* base coefficient h(b) := (||U*b||^2 - <U*b, e>^2)/nu = ||P_{e-perp} U*b||^2/nu, beta := ||U*b||;
* block coefficient H_m(omega_m) := (||D_m omega_m||^2 - d_m^2)/C_m = ||P_m-perp D_m omega_m||^2 / C_m (P_m-perp = orthogonal
  projection onto (D_m w_m)-perp);
* H(c) := max(h(b), max_m H_m(omega_m));
* gap_m(omega_m) := min_{k in supp omega_m} gap_m(k) > 0;
* radius r(c) := min{ 1/||b/a||_infinity, nu/(2 beta), min over m with omega_m != 0 of
  min( gap_m(omega_m)/(2||omega_m||_infinity), 1/(2|d_m|), C_m/(2|d_m| M_m) ) } (with 1/0 = infinity);
* kappa(c) := max{ 2 beta/nu, max_m 2|d_m| M_m / C_m }.

**Cert(f)** := { g_c : c finite certificate at f, H(c) <= 1, g_c in C(f) }.

**Lemma 4.2 (algebra). PROVED.** Finite certificates form a vector space; c -> g_c is linear; H is the maximum of
finitely many positive semidefinite quadratic forms, so H(lambda c) = lambda^2 H(c) and H is convex; r(lambda c) = r(c)/|lambda|,
kappa(lambda c) = |lambda| kappa(c). Every g_c satisfies g_c(xi) = 0. Cert(f) is convex and symmetric.

*Proof.* d_m is linear in omega_m. For the identity g_c(xi) = 0: b(xi) = q_0 b(zhat) = 0, and by Fact C
<omega_m - d_m w_m, zeta_m> = |zeta_m| ( <omega_m, alpha_m> + <omega_m, D^2 w_m>/C_m - d_m(<w_m, alpha_m> + <w_m, D^2 w_m>/C_m) )
= |zeta_m| (0 + d_m - d_m (M_m + C_m)) = 0, because alpha_m lives on P_m and supp omega_m misses P_m. Convexity of Cert(f)
follows from linearity, convexity of H and of C(f). QED.

### 4.2 Exact expansions
**Lemma 4.3 (base expansion). PROVED (numerically checked, Appendix).** Let b in l_1 with supp b contained in supp a.
For every real sigma,
  q*(a + sigma b) = 1 + sigma b(zhat) + Fl_b(sigma) + nu Psi(sigma U*b/nu),
where Fl_b(sigma) := sum_{j in supp a} 2 ( -sign(a_j) sigma b_j - |a_j| )_+ >= 0 (the "sign-flip cost", zero for
|sigma| <= 1/||b/a||_infinity), and Psi(h) := ||e + h|| - 1 - <e, h> = ||h_perp||^2 / ( ||e + h|| + 1 + <e,h> ), h_perp := h - <e,h> e.
For ||h|| <= 1/2: ||h_perp||^2/(2(1+||h||)) <= Psi(h) <= ||h_perp||^2/(2(1-||h||)). Consequently, if b(zhat) = 0 and
|sigma| <= min(1/||b/a||_infinity, nu/(2 beta)):
  (sigma^2/2) h(b)/(1 + |sigma| beta/nu) <= q*(a + sigma b) - 1 <= (sigma^2/2) h(b)/(1 - |sigma| beta/nu) <= (sigma^2/2) h(b)(1 + 2|sigma| beta/nu).
Moreover, for c, c' in l_1 with |sigma| ||U|| max(||c||_1, ||c'||_1) <= nu/2:
  | nu Psi(sigma U*c/nu) - nu Psi(sigma U*c'/nu) | <= (4 sigma^2 ||U||^2/nu) max(||c||_1, ||c'||_1) ||c - c'||_1.

*Proof.* For real x != 0 and y: |x + y| = |x| + sign(x) y + 2(-sign(x) y - |x|)_+. Summing over j in supp a (b vanishes
elsewhere): ||a + sigma b||_1 = ||a||_1 + sigma b(z) + Fl_b(sigma), since z_j = sign a_j on supp a. Next
||U*a + sigma U*b|| = nu ||e + h|| with h = sigma U*b/nu, and ||e+h|| = 1 + <e,h> + Psi(h), nu <e,h> = sigma <U*b, e>. Adding and
using ||a||_1 + nu = 1 and b(z) + <U*b, e> = b(zhat) gives the identity. The formula for Psi follows from
||e+h||^2 - (1 + <e,h>)^2 = ||h||^2 - <e,h>^2; for ||h|| <= 1/2 the denominator lies in [2(1 - ||h||), 2(1 + ||h||)].
With h = sigma U*b/nu: nu ||h_perp||^2 = sigma^2 h(b) and ||h|| = |sigma| beta/nu; 1/(1-x) <= 1 + 2x for x <= 1/2.
Lipschitz bound: grad Psi(h) = (e+h)/||e+h|| - e has norm <= 2||h||/||e+h|| <= 4||h|| on the ball of radius 1/2;
apply the mean value theorem on the segment. QED.

**Lemma 4.4 (block expansion). PROVED (numerically checked).** Fix a block; let omega: N -> R vanish on P with
D omega in l_2; d := <Dw, D omega>/C; h_perp := D omega - (d/C) Dw, so ||h_perp||^2 = ||D omega||^2 - d^2 = C H(omega).
For W(sigma) := (1 - d sigma) w + sigma omega and Y := C + d sigma M:
 (a) ||D W(sigma)||_2 = sqrt(Y^2 + sigma^2 ||h_perp||^2) for all sigma;
 (b) if 1 - d sigma >= 0 then ||W(sigma)||_infinity >= (1 - d sigma) M and hence, when Y > 0,
     N(W(sigma)) >= 1 + sigma^2 ||h_perp||^2 / ( sqrt(Y^2 + sigma^2 ||h_perp||^2) + Y );
 (c) if |d sigma| <= 1/2 and |sigma omega(k)| <= gap(k)/2 for every k with omega(k) != 0, then
     ||W(sigma)||_infinity = (1 - d sigma) M and equality holds in (b);
 (d) for omega in c_00 and |sigma| <= r_m := min( gap(omega)/(2||omega||_infinity), 1/(2|d|), C/(2|d|M) ):
     N(W(sigma)) <= 1 + (sigma^2/2) H(omega) (1 + 2|d sigma| M/C).

*Proof.* (1 - d sigma) Dw + sigma D omega = (1 - d sigma + sigma d/C) Dw + sigma h_perp = (1 + d sigma M/C) Dw + sigma h_perp,
using 1/C - 1 = M/C; orthogonality gives (a). (b): at a peak k, |W(sigma)(k)| = (1 - d sigma) M; then
N(W) >= (1 - d sigma) M + sqrt(Y^2 + sigma^2||h_perp||^2) = 1 + [sqrt(Y^2 + sigma^2 ||h_perp||^2) - Y], as (1 - d sigma) M + Y = M + C = 1.
(c): for k outside supp omega, |W(k)| = (1 - d sigma)|w(k)| <= (1 - d sigma) M; for k in supp omega,
|W(k)| <= (1 - d sigma)|w(k)| + gap(k)/2 = (1 - d sigma) M - (1 - d sigma) gap(k) + gap(k)/2 <= (1 - d sigma) M.
(d): the bracket in (b) is at most sigma^2 ||h_perp||^2/(2Y), and C/Y <= 1/(1 - |d sigma| M/C) <= 1 + 2|d sigma| M/C. QED.

**Proposition 4.5 (certificate expansion). PROVED.** For a finite certificate c at f and |sigma| <= r(c):
  p*(f + sigma g_c) <= 1 + (sigma^2/2) H(c) (1 + kappa(c) |sigma|).
*Proof.* f + sigma g_c = (a + sigma b) + sum_m R_m* W_m(sigma) with W_m(sigma) = (1 - d_m sigma) w_m + sigma omega_m
(= w_m when omega_m = 0). Apply Fact A, Lemma 4.3 (no flips for |sigma| <= 1/||b/a||) and Lemma 4.4(d). QED.

**Lemma 4.6 (validity window). PROVED.** If H(c) <= 1 - delta with 0 < delta <= 1 and
|sigma| <= r_*(c, delta) := min( r(c), delta/(2 kappa(c) + 2), sqrt(delta) ), then p*(f + sigma g_c) <= s(sigma).
*Proof.* (1 - delta)(1 + kappa|sigma|) <= (1 - delta)(1 + delta/2) <= 1 - delta/2; and
1 + (sigma^2/2)(1 - delta/2) <= 1 + sigma^2/2 - sigma^4/8 <= s(sigma) because sigma^2 <= delta gives sigma^4/8 <= sigma^2 delta/4,
and sqrt(1 + x) >= 1 + x/2 - x^2/8 for x >= 0. QED.

### 4.3 The NA-scale criterion (quantitative multi-scale lemma)
**Lemma 4.7 (slack).** For rho in (0,1) and real t: s(t) - s(rho t) >= (1 - rho^2) min(t^2, |t|)/3.
*Proof.* s(t) - s(rho t) = (1 - rho^2) t^2/(s(t) + s(rho t)) >= (1 - rho^2) t^2/(2 s(t)); and 2 s(t) <= 2 sqrt(2) < 3 for |t| <= 1,
2 s(t) <= 2 sqrt(2) |t| < 3|t| for |t| >= 1. QED.

**Proposition 4.8 (NA-scale criterion). PROVED.** Let f, f' in S_{p*}, g in C(f), rho in (0,1), and let c' be a finite
certificate AT f' with H(c') <= 1 - delta (0 < delta <= 1). Put r_* := r_*(c', delta) (<= 1), eps := p*(f' - f),
eta := p*(g_{c'} - rho g). If
  eps <= (1 - rho^2) r_*^2 / 6   and   eta <= (1 - rho^2) r_* / 6,
then g_{c'} lies in C(f'), hence in Cert(f'), and dist_{p*}(rho g, C(f')) <= eta.

*Proof.* For |t| <= r_*: Lemma 4.6 at f'. For |t| >= r_*:
p*(f' + t g_{c'}) <= p*(f + t rho g) + eps + |t| eta <= s(rho t) + eps + |t| eta, and by Lemma 4.7 it suffices that
eps + |t| eta <= (1 - rho^2) min(t^2, |t|)/3. For r_* <= |t| <= 1 we have eps <= (1-rho^2) t^2/6 and |t| eta <= (1-rho^2) t^2/6;
for |t| >= 1, eps + |t| eta <= (1 - rho^2)(1 + |t|)/6 <= (1 - rho^2)|t|/3. QED.

Remark 4.9 (the multi-scale issue, quantified). With eps = ||f' - f||: the slack alone certifies the scales
|t| >= sqrt(6 eps/(1 - rho^2)) (and |t| >= 6 eta/(1 - rho^2)); the range below must be certified by the local structure
of f'. In terms of a finite certificate the "certificate radius" is
  r(c) = min{ min_{j in supp b} |a_j|/|b_j|  [first sign flip of a base coordinate],
              nu/(2||U*b||)                  [Hilbert part of the base],
              min_m min_{k in supp omega_m} gap_m(k)/(2|omega_m(k)|)  [first box violation of a block coordinate],
              min_m C_m/(2|d_m| M_m), 1/(2|d_m|) }.
So a certificate at f' is usable iff r_* is at least of order sqrt(eps/(1-rho^2)) and its direction is within
(1 - rho^2) r_*/6 of rho g. Proposition 4.8 with f' = f gives the purely local test:
**(CA)** if for every rho < 1 and eta > 0 there is a certificate c at f with H(c) <= 1 - delta_rho and
p*(g_c - rho g) <= min(eta, (1 - rho^2) r_*(c, delta_rho)/6), then g is in cl Cert(f).

### 4.4 The Transport Theorem
**Theorem 4.10 (Transport). PROVED.** Let f_n -> f in S_{p*} (arbitrary sequence, NA or not) and let c = (b, omega) be a
finite certificate at f. Define
  G_n := { j in supp a : sign a_n(j) = sign a_j and |a_n(j)| >= |a_j|/2 },  b'_n := b 1_{G_n},  tau_n := b'_n(zhat_n),
  b_n := b'_n - tau_n a_n,  c_n := (b_n, omega)  (same block coefficients omega_m; d_{n,m} := <D w_{n,m}, D omega_m>/C_{n,m}).
Then for n large c_n is a finite certificate at f_n, ||g_{c_n} - g_c|| -> 0, H(c_n) -> H(c), kappa(c_n) -> kappa(c), and
liminf_n r(c_n) >= r(c)/2. If moreover g_c is in C(f) and H(c) <= 1, then for every rho in (0,1), rho g_{c_n} is in
Cert(f_n) for all large n.

*Proof.* Base. By Fact E, a_n -> a in l_1, nu_n -> nu, e_n -> e, z_n -> z weak*, and z_n = sign a_n on supp a_n. Each
j in supp a eventually lies in G_n, so b'_n -> b in l_1 by dominated convergence. On G_n, z_n(j) = sign a_n(j) = sign a_j = z_j,
hence tau_n = sum_{j in G_n} b_j z_j + <U*b'_n, e_n> -> b(z) + <U*b, e> = b(zhat) = 0, and b_n -> b in l_1.
supp b_n is contained in supp a_n; on G_n, |b_n(j)|/|a_n(j)| <= 2|b_j|/|a_j| + |tau_n|, and on supp a_n \ G_n the ratio is |tau_n|;
so ||b_n/a_n||_infinity <= 2||b/a||_infinity + |tau_n|. Since a_n(zhat_n) = 1 (Fact B at f_n), b_n(zhat_n) = tau_n - tau_n = 0.
Thus (C1) holds at f_n, h_n(b_n) = (||U*b_n||^2 - <U*b_n, e_n>^2)/nu_n -> h(b), and ||U*b_n|| -> beta.
Blocks. For k in supp omega_m (finite) and m in the finite set of active blocks, w_{n,m}(k) -> w_m(k) and M_{n,m} -> M_m
(Fact E), so M_{n,m} - |w_{n,m}(k)| -> gap_m(k) > 0: eventually supp omega_m misses P_{n,m}, and gap_{n,m}(omega_m) -> gap_m(omega_m).
Also d_{n,m} -> d_m, C_{n,m} -> C_m and the block coefficients converge. Hence H(c_n) -> H(c), kappa(c_n) -> kappa(c), and
liminf r(c_n) >= min(1/(2||b/a||), nu/(2 beta), block radii of c) >= r(c)/2.
Directions. g_{c_n} - g_c = (b_n - b) + sum_m (d_m R_m* w_m - d_{n,m} R_m* w_{n,m}) -> 0 since R_m* w_{n,m} -> R_m* w_m in norm.
Mates. Let delta := (1 - rho^2)/2. Then H(rho c_n) = rho^2 H(c_n) -> rho^2 H(c) <= rho^2 < 1 - delta, and
r_*(rho c_n, delta) = min(r(c_n)/rho, delta/(2 rho kappa(c_n) + 2), sqrt(delta)) is bounded below by some r_0 > 0 for n large.
Apply Proposition 4.8 with f' = f_n, c' = rho c_n and g = g_c: eps_n = p*(f_n - f) -> 0 and eta_n = rho p*(g_{c_n} - g_c) -> 0,
so the two inequalities hold for n large, and rho g_{c_n} = g_{rho c_n} lies in Cert(f_n). QED.

**Corollary 4.11 (lower semicontinuity of the certificate fibre). PROVED.** For every sequence f_n -> f in S_{p*}:
  cl Cert(f) is contained in Li_n cl Cert(f_n), which is contained in Li_n C(f_n).
Consequently:
 (a) every mate in cl Cert(f) is recovered along every NA sequence f_n -> f; any finitely many such mates are recovered
     simultaneously along any common sequence; (f, g) is in cl NA((X,p), l_2^2) for every g in cl Cert(f);
 (b) the set G := { f in S_{p*} : C(f) = cl Cert(f) } is contained in R, and C is Hausdorff continuous at every f in G;
 (c) (reduction) if for every f in S_{p*} the defect Def(f) := C(f) \ cl Cert(f) is contained in Li_n C(f_n) for SOME NA
     sequence f_n -> f, then NA((X,p), l_2^2) is dense; in particular density follows if G = S_{p*}.

*Proof.* By Theorem 4.10, rho Cert(f) is contained in Li Cert(f_n) for each rho < 1; Li is closed; so cl Cert(f) is inside
Li Cert(f_n) = Li cl Cert(f_n). (a) then follows from Corollary 3.3. (b): upper semicontinuity (Theorem 3.1) plus
C(f) = cl Cert(f) in Li C(f_n) give Kuratowski convergence of compact sets inside the compact Q, hence Hausdorff convergence.
(c): for that sequence C(f) = cl Cert(f) cup Def(f) lies in Li C(f_n); apply Corollary 3.3. QED.

**Corollary 4.12 (the known classes (R6), simultaneously; re-proof of [Check, Thm 3.1]). PROVED.**
 (i) Block directions g = R_m*(omega - d w_m), omega finitely supported strictly below the peak, with H <= 1 and (f,g)
     contractive: g is in Cert(f), hence recovered along every sequence. This is the finite local-certificate theorem of
     [Check], now proved (and extended to combinations of several blocks and a base part).
 (ii) Base directions b in c_00 (or b in l_1 with ||b/a|| < infinity), supp b in supp a, b(xi) = 0: b/C is in Cert(f) for
     every C >= C_b := max( 1, sqrt(2 h(b)), p*(b) r_0/(s(r_0) - 1) ), where r_0 := min(r(c), 1/(4 kappa(c) + 4), 1/sqrt 2) for c = (b, 0).
 (iii) Weighted directions of Preprint A, Thm 3.1, with H <= 1 and (f,g) contractive: in cl Cert(f) (Theorem 6.2 below).
 (iv) All mates of types (i)-(iii), and their closed convex hull, are recovered simultaneously along ANY NA sequence f_n -> f.
*Proof of (ii).* c/C has H = h(b)/C^2 <= 1/2, kappa(c/C) = kappa(c)/C <= kappa(c), r(c/C) = C r(c) >= r(c); so
r_*(c/C, 1/2) >= r_0 and Lemma 4.6 gives p*(f + sigma b/C) <= s(sigma) for |sigma| <= r_0. For |sigma| >= r_0,
p*(f + sigma b/C) <= 1 + |sigma| p*(b)/C <= s(sigma) because (s(sigma) - 1)/|sigma| is increasing in |sigma|. QED.

**Theorem 4.13 (ranges l_2^{d+1}). PROVED.** Let c_1, ..., c_d be finite certificates at f with
G := (g_{c_1}, ..., g_{c_d}) in the joint fibre C_d(f) (i.e. p*(f + sum_i t_i g_{c_i}) <= s(|t|) for all t in R^d) and
sup_{theta in S^{d-1}} H(sum_i theta_i c_i) <= 1. Then for every sequence f_n -> f in S_{p*} and rho < 1, the transported tuple
rho G_n := (rho g_{c_{1,n}}, ..., rho g_{c_{d,n}}) lies in C_d(f_n) for n large, and G_n -> G. Hence
cl Cert_d(f) is contained in Li_n C_d(f_n), where Cert_d(f) is the set of such tuples.
*Proof.* The transport of Theorem 4.10 is linear in c (with the same G_n and the same tau-correction applied to each b_i),
so c(t) := sum_i t_i c_i transports to c_n(t) = sum_i t_i c_{i,n}. On the unit sphere, r(c(theta)) >= r_0 > 0 (supports of the
omega_{i,m} are finitely many, ||b(theta)/a|| <= sum |theta_i| ||b_i/a||, |d_m(theta)| <= sum |theta_i||d_{i,m}|), uniformly in n large.
Run the proof of Proposition 4.8 along each ray t = |t| theta with the slack s(|t|) - s(rho|t|). QED.

Remark 4.14 (on the condition H(c) <= 1). If g_c is a mate but H(c) > 1, the decompositions that make g_c a mate are not
the linear one. The simplest cheaper decompositions are quadratic "shifts" along w (§4.5): they are transported as well, which
shows that the coefficient condition of the [Check] theorem is NOT sharp (Example 4.18). More general non-linear decompositions
are discussed in §7.

