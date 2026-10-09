# N2 part 1: setting, the exact two-piece class, algebraic lemmas

Setting: canonical base q (B_q = B_{c_0} + U(B_H), U compact, dense range, U* injective), Martin's norm with a FINITE
block set I (p_N, any N; Remark martin-tail of Preprint B reduces Martin's p to these). Notation of A_notes §1, §4,
BRIEFING. Imported (refereed): (T1)-(T4), Facts A-F, Lemmas 4.3, 4.4, Prop 4.5, Lemma 4.6, 4.7, Lemmas 7.1-7.2 of
A_notes; N_part1 Theorem 1 (Ls(f); g in Ls(f) iff (f, rho g) in cl NA for all rho < 1); P1 §2 (example).
For f in S_{p*}: normer xi, q_0, forced data f = a + L*w, zhat = xi/q_0 = z + U e, nu = ||U*a||, F := supp a,
K := {j notin F : |z_j| = 1} (contacts = "kinks" of C_notes), J := {j notin F : |z_j| < 1} (free coordinates),
zeta_m = R_m** xi, P_m peaks, Q_m strict non-peaks, M_m, C_m, d_m(omega) := <D_m w_m, D_m omega>/C_m,
h(b) := ||P_{e-perp} U*b||^2/nu, H_m(omega) := ||P_m-perp D_m omega||^2/C_m. Labels PROVED / SKETCH / HEURISTIC / OPEN.

## 1.1 Definition (exact two-piece representation)
Let f in S_{p*} with F finite and g in C(f). An exact two-piece representation of g is (b+, omega+; b-, omega-) with
 (E1) b+, b- in l_1, supp b+- contained in F cup K, and z_j b+_j >= 0 >= z_j b-_j for every j in K;
 (E2) omega+-_m in c_00 with supp omega+-_m contained in Q_m (m in I);
 (E3) g = b+ + sum_m R_m*(omega+_m - d_m(omega+_m) w_m) = b- + sum_m R_m*(omega-_m - d_m(omega-_m) w_m);
 (E4) kappa := max{ h(b+), h(b-), H_m(omega+_m), H_m(omega-_m) : m in I } <= 1.
Derived data: Delta omega_m := omega-_m - omega+_m, Delta d_m := d_m(Delta omega_m), ell_m := R_m* Delta omega_m,
v := b+ - b- (the TRANSFER), I_act := {m : Delta omega_m != 0}. For theta in [0,1]:
b_theta := (1-theta) b+ + theta b- = b+ - theta v, omega_theta := (1-theta) omega+ + theta omega-.
The representation is RESONANT if v != 0. ("Two-piece mates" of A_referee 5.2, P1 2.3, 6.2 are of this form; see 2.6.)

## 1.2 Lemma (algebra of two-piece representations). PROVED.
(a) b+(zhat) = b-(zhat) = 0.
(b) v = sum_m ( ell_m - Delta d_m R_m* w_m ) is in Y := Ran T; supp v in F cup K; z_j v_j = |b+_j| + |b-_j| >= 0 on K.
(c) For every f'' in S_{p*} (normer xi'', block data zeta''_m, w''_m, C''_m) and every omega in c_00 supported in Q''_m:
    d''_m(omega) = (R_m* omega)(xi'')/|zeta''_m|_m. In particular Delta d_m = ell_m(xi)/|zeta_m|.
(d) If v = 0 then b+ = b- is supported in F and omega+ = omega-; then g is in Cert(f) (A Def 4.1) .
    If v != 0 then supp v cap K is infinite (so K is infinite and f is not norm attaining).
(e) If the two decompositions in (E3) are ADMISSIBLE one-sided linear decompositions, i.e. q*(a + tau b+-) <= s(tau)
    and N_m(w_m + tau(omega+-_m - d_m(omega+-_m) w_m)) <= s(tau) for 0 <= +-tau <= tau_0, then (E4) holds.
(f) For every theta in [0,1]: g = b_theta + sum_m R_m*(omega_theta,m - d_m(omega_theta,m) w_m), h(b_theta) <= kappa and
    H_m(omega_theta,m) <= kappa.
*Proof.* (a) For omega in c_00 off the peaks, <omega - d(omega) w, zeta> = 0 (A Lemma 4.2). Hence g(xi) = b+(xi) = q_0 b+(zhat),
and g(xi) = 0 for every mate (A Remark 2.3). Same for b-.
(b) Subtract the two representations in (E3): v = sum_m R_m*(Delta omega_m - Delta d_m w_m), by linearity of d_m. Each R_m* maps into
Y (T1), so v in Y. The support and sign statements follow from (E1).
(c) Off P''_m, Fact C at f'' gives w''_m(k) = C''_m zeta''_m(k)/(Phi_m(k)^2 |zeta''_m|), so
d''_m(omega) = sum_k Phi_m(k)^2 w''_m(k) omega(k)/C''_m = sum_k zeta''_m(k) omega(k)/|zeta''_m| = <omega, R_m** xi''>/|zeta''_m| = (R_m* omega)(xi'')/|zeta''_m|.
(d) If v = 0: on K, 0 <= z_j b+_j = z_j b-_j <= 0, so b+ = b- vanishes on K; and sum_m R_m*(Delta omega_m - Delta d_m w_m) = 0 gives,
by injectivity of L* (T1), Delta omega_m = Delta d_m w_m; at a peak w_m != 0 while Delta omega_m = 0, so Delta d_m = 0 and Delta omega_m = 0.
Then c := (b+, omega+) is a finite certificate (supp b+ in F finite, so ||b+/a||_inf < infinity; b+(zhat) = 0 by (a)) with
H(c) <= kappa <= 1 and g_c = g in C(f): g in Cert(f). If v != 0: v in Y \ {0} and Y cap c_00 = {0}, so supp v is infinite, and
supp v is contained in F cup K with F finite.
(e) Base: for 0 < tau <= tau_0, by A Lemma 7.2 (all terms nonnegative) and the lower bound of A Lemma 4.3,
1 + tau^2 h(b+)/(2(1 + tau ||U*b+||/nu)) <= q*(a + tau b+) <= s(tau) <= 1 + tau^2/2; divide by tau^2 and let tau -> 0: h(b+) <= 1.
Block: A Lemma 4.4(b) gives N_m(...) >= 1 + tau^2 ||h_perp||^2/(sqrt(Y^2 + tau^2||h_perp||^2) + Y) with Y -> C_m, so H_m <= 1.
The minus side is identical with tau < 0.
(f) Convex combination of the two representations; h and H_m are convex quadratic forms. QED.

Remark 1.2.1 (meaning of Delta d). By (b),(c): ell_m(xi) = Delta d_m |zeta_m| is the xi-value of the block carrier functional;
v(xi) = 0 always. Delta d is invariant under g -> -g (the sides swap: b~+ = -b-, b~- = -b+, omega~+ = -omega-, ...,
Delta d~ = d(omega~-) - d(omega~+) = -d(omega+) + d(omega-) = Delta d). So the sign of Delta d is intrinsic to the resonance.

## 1.3 Lemma (convex block lemma; makes the "c-trick" rigorous). PROVED.
Let f'' in S_{p*}, a block m, w'' := w''_m, omega in c_00 supported in Q''_m, d'' := d''_m(omega), and y in l_inf with N_m(y) <= 1.
For real tau and s in [0, 1) put tau~ := tau/(1-s) and
  W := w'' + tau (omega - d'' w'') + s (y - w'').
Then W = (1-s) [ (1 - tau~ d'') w'' + tau~ omega ] + s y, hence
  N_m(W) <= (1-s) N_m((1 - tau~ d'') w'' + tau~ omega) + s,
and if |tau~| <= r''_m(omega) (A Lemma 4.4(d) at f''):  N_m(W) <= 1 + (tau^2/(2(1-s))) H''_m(omega) (1 + 2|d'' tau~| M''/C'').
*Proof.* (1-s)(1 - tau~ d'') = 1 - s - tau d'' and (1-s) tau~ = tau: the identity is algebra. Then use the triangle inequality,
N_m(y) <= 1, and A Lemma 4.4(d) at f''. QED.
Use: in the two-piece engineering the block part of side +- will be w' + tau rho(omega+- - d' w') + tau rho c+-(w' - w) with
s := -tau rho c+- and y := w (the block functional of f, N_m(w_m) = 1). Lemma 1.3 applies iff s >= 0, i.e. tau c+- <= 0.
This proves the A_referee/E_referee "c-trick" for the correct sign WITHOUT any first-order bookkeeping. For the wrong sign
(s < 0, extrapolation beyond w'') the bound fails: if some peak k of w'' has w(k) = -w''(k) (status flips at fine
coordinates are unavoidable along NA approximants, since z' is in c_0), then ||W||_inf >= (1 - tau d'')M'' + |s|(M + M''),
a first-order excess 2|s| M approximately (see part 3).

## 1.4 Lemma (base excess at an NA point). PROVED.
Let a' in c_00 with q*(a') = 1, z' in B_{c_0} with z' = sign a' on supp a', e' := U*a'/nu', nu' := ||U*a'||, xhat' := z' + U e'
(so f' := grad p(xhat') is norm attaining with forced base data (a', z', e'), Fact D). Let B in l_1 with B(xhat') = 0, tau real,
|tau| ||U*B|| <= nu'/2, and |tau B_j| <= |a'_j| for j in supp a'. Then
  q*(a' + tau B) <= 1 + kink'_tau(B) + tau^2 h'(B)/(2(1 - |tau| ||U*B||/nu')),
  kink'_tau(B) := sum_{j notin supp a'} ( |tau B_j| - z'_j tau B_j )  (>= 0),  h'(B) := ||P_{e'-perp} U*B||^2/nu'.
*Proof.* On supp a': |a'_j + tau B_j| = |a'_j| + z'_j tau B_j (no sign change). Off supp a': |tau B_j| = z'_j tau B_j + (|tau B_j| - z'_j tau B_j).
So ||a' + tau B||_1 = ||a'||_1 + tau B(z') + kink'. ||U*a' + tau U*B|| = nu' ||e' + h||, h := tau U*B/nu', and
||e' + h|| = 1 + <e',h> + Psi(h) with Psi(h) <= ||h_perp||^2/(2(1 - ||h||)) for ||h|| <= 1/2 (A Lemma 4.3). Add, use
||a'||_1 + nu' = 1 and B(z') + <U*B, e'> = B(xhat') = 0. QED.
Consequences: kink'_tau(B) = 0 if B lives on supp a' and on contacts of f' (|z'_j| = 1) with sign(tau B_j) = z'_j there;
kink'_tau(B) <= 2|tau| ||B 1_E||_1 for any set E outside of which this holds.

## 1.5 Lemma (convergence of engineered approximants). PROVED.
Let a'_n in c_00 cap S_{q*} with a'_n -> a in l_1, z'_n in B_{c_0} with z'_n = sign a'_n on supp a'_n and z'_n -> z coordinatewise, and
f'_n := grad p(z'_n + U e'_n) (e'_n := U*a'_n/||U*a'_n||). Then f'_n -> f in norm; all forced data converge as in A Fact E; in
particular w'_{n,m}(k) -> w_m(k) for every (k,m), M'_{n,m} -> M_m, C'_{n,m} -> C_m, d'_{n,m}(omega) -> d_m(omega) for every
omega in c_00 off the peaks, and every finite set of strict non-peaks of f is eventually a set of strict non-peaks of f'_n with
gaps converging.
*Proof.* x'_n := z'_n + U e'_n: e'_n -> e in H (U*a'_n -> U*a in norm), so x'_n -> zhat weak* (bounded, coordinatewise).
L is compact, hence L x'_n -> L** zhat in norm (L** zhat in V, Fact B). J_V is norm-to-weak* continuous at L** zhat (all block
components nonzero; each J_m single valued, Smulian), and L* is weak*-to-norm continuous on bounded sets, so
L* J_V(L x'_n) -> L* J_V(L** zhat) = L* w (J_V 0-homogeneous, zhat = xi/q_0). grad p(x'_n) = grad q(x'_n) + L* J_V(L x'_n)
and grad q(x'_n) = a'_n (Fact D). So f'_n -> a + L*w = f; the rest is A Fact E applied to f'_n -> f. QED.

## 1.6 Where the classes of the task fit (PROVED identifications; details in parts 3, 4)
 * P1's example (P1 2.2, 6.1-6.2): every g in E_u with mu+ <= inf theta(g), mu- >= sup theta(g) gives the representation
   b+- := g - mu+- u, omega+- := (mu+-/lambda_0) e_2 (block 1); it is exact two-piece with Delta d = 0 (w_1(2) = 0), I_act = {1},
   v = (mu- - mu+) u, kappa = max(h(g - mu+- u), (mu+-)^2/C_1).
 * A_referee 5.2/5.4 (general form with equal d-coefficients): Delta d = 0.
 * E_referee 3.1 "two-piece mates with Delta d < 0": exactly the case Delta d_m < 0 for some m.
 * C_referee 1.20 "kink re-splitting" (one-sided first-order re-splits through infinitely many kinks): a block vector
   v'' = c' sigma 1_P + v''_Q (c' a constant) with beta = R* v'' supported on F cup K, z-signed, first-order flat. Writing
   sigma 1_P = (w - w 1_Q)/M gives v'' = (c'/M) w + omega'' with omega'' supported on Q, and flatness <v'', zeta> = 0 means
   (Lemma 1.2(c)) d(omega'') = -c'/M. The re-split f + tau g = (a + tau(b + s beta)) + R*(w + tau(Omega - s v'')) of a certificate
   (b, Omega = omega - d(omega) w) by amounts s+ >= 0 >= s- on the two sides has block parts
   Omega - s v'' = (omega - s omega'') - d(omega - s omega'') w, so it is an exact two-piece representation with
   Delta omega = (s+ - s-) omega'' and Delta d = -(s+ - s-) c'/M: the kink phenomenon IS an exact resonance with Delta d != 0
   (the uniform peak component of v'' is precisely the d-term). So the C_referee kink class and the E_referee Delta d < 0
   class coincide at the level of mechanisms; both are treated in part 3.
