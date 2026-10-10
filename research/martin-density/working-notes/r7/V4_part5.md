# V4 part 5 — Numerics for Proposition 4.5; genericity (Baire) of near-threshold carriers; corrections; where a counterexample must live

Notation of parts 1-4.  N = 1 unless said otherwise.

## 5.1 Numerical check of the perturb-and-realign mechanism (Proposition 4.5)
Script V4_work/degenerate_check4.py (earlier attempts degenerate_check.py, degenerate_check2.py, degenerate_check3.py kept for the
record).  Finite model: one block, L = 10 carriers, F = {0,1,2,3} with diagonal base entries (0.9, 0.7, 0.8, 0.6) on F, 40 further
non-signature coordinates, signature sets of 6 coordinates with weights 2^{-i}; weights chosen recursively with
c_l/c_{l-1} = 2^{-6} delta_{l-1} min(min h_{l-1}, min |y_{l-1}|)   (an (SF*)-type condition; ratios 3e-5 ... 5e-7);
targets random sparse on F, the extra coordinates and the last two coordinates of earlier signature sets (allowedness (a)).
Exceptional carriers: l_- = 1 with target (e_0 - e_1)/q*, tuned to n_- val_- = -eta (eta = 0.2 n_- theta_0 Phi_-), and l_D = 2 with
target (e_2 - e_3)/q*, tuned to val_D = theta Phi_D (EXACT degeneracy), both with eps = +1; owner rule for all other carriers.
Tuning by nested bisection in the ratios a_0/a_1 and a_2/a_3.
Results at f: relative tuning residuals 8.5e-11 and -1.3e-6 (the double-precision limit: theta Phi_D = 5.0e-11 against O(1) terms);
nu/theta = (5.0, 0.2000002, 0.9999987, 1.2e15, 1.5e20, ...); q_- < 0; Delta d = -1.33e-11 < 0; D = Delta_alpha lambda_- u_- - Delta d R^* w
is z-signed off F (all coordinates).
Perturbation a -> a(1 + p (0.3, -0.5, 0.7, -0.2)) with hysteretic re-alignment (Lemma 4.4):
| p | forced flips | nu_D/theta | l_- strict non-peak, q<0 | min other nu/theta | D^p z^p-signed | Delta d^p | ||R^*(w^p - w)||_1 |
|---|---|---|---|---|---|---|---|
| 1e-13 | none | 0.999974 | yes, yes | 5.0 | yes | -1.3312e-11 | 3.9e-15 |
| 1e-12 | none | 0.999740 | yes, yes | 5.0 | yes | -1.3312e-11 | 4.0e-14 |
| 1e-11 | none | 0.997405 | yes, yes | 5.0 | yes | -1.3312e-11 | 4.0e-13 |
| 1e-10 | none | 0.974058 | yes, yes | 5.0 | yes | -1.3312e-11 | 4.0e-12 |
| 1e-9  | none | 0.740577 | yes, yes | 5.0 | yes | -1.3311e-11 | 4.0e-11 |
| 1e-8  | none | 1.594 (val_D < 0) | yes, yes | 5.0 | NO | -1.3303e-11 | 3.8e-10 |
For p <= 1e-9 the degenerate peak becomes a strict non-peak (non-degenerate), everything else is preserved, and the transplant
distance is linear in p: exactly the mechanism of Proposition 4.5.  At p = 1e-8 the perturbation exceeds the scale theta Phi_D of
val_D, val_D changes sign while z = +1 on S_D, and D^p is no longer z^p-signed on S_D: the proof indeed needs p so small that
sgn val_D is preserved.  The earlier model degenerate_check2.py (weights 10^{-2l}, NOT of (SF*)-type) failed z-signedness at one
coordinate of S_7 hit by the target of carrier 8 (later term 1.9e-20 against owner term 1.9e-21): the dominance hypothesis (SF*) is
needed and is the right one.

## 5.2 Near-threshold carriers are Baire-generic in every fixed-z fibre; (GO) is FALSE
**Proposition 5.1.  PROVED.**  Let T be ANY admissible operator (blocks with (T-d)), U diagonal, m a block, F a finite set with
d := |F| >= 2, sigma in {-1,1}^F, and z in B_{l_infty} with z_j = sigma_j on F and infinitely many contacts off F.  Let
A := {a : supp a = F, sgn a = sigma on F, q*(a) = 1} (so every a in A gives admissible forced data (a, z) of a unique first row f_a).
Let (eps_l) be ANY sequence of positive numbers.  Then the set of a in A for which
   |nu_l(f_a) - theta_m(f_a)| < eps_l   for infinitely many carriers l of block m
is a dense G_delta subset of A.  In particular, for a dense G_delta set of a, block m of f_a has infinitely many near-threshold
carriers whose targets meet F (strict non-peaks with tiny gaps or weak peaks with tiny margins), and f_a is not (BT).
*Proof.*  (1) Parametrization.  b(a) := (s_j a_j)_{j in F}/||(s_i a_i)||_2 maps A homeomorphically onto the open orthant
Omega := {b in S^{d-1} : sgn b_j = sigma_j}, and zhat_j = sigma_j + s_j b_j on F (U^* e_j^* = s_j kappa_j, e = U^* a/nu).  By Lemma 1.1,
for every vector y in l_1, y(zhat) = sum_{j notin F} y_j z_j + sum_{j in F} y_j (sigma_j + s_j b_j) =: psi_y(b), an affine function of b.
In particular val_l(b) = psi_{u_l}(b) is continuous, zeta_m(b) = (lambda_k val_k(b))_k depends continuously on b in l_1
(sum_k lambda_k |val_k(b) - val_k(b')| <= sum_k lambda_k ||U|| ||e(b) - e(b')||), so theta_m(b) is continuous (Lemma T), positive and
bounded on Omega.  (2) Density of each tail.  Fix L, b_0 in Omega and a connected open neighbourhood O of b_0 in Omega.  As d >= 2,
choose n in R^F such that (n_j s_j)_j is not parallel to b_0; then b -> sum_j n_j s_j b_j has non-zero differential on the sphere at
b_0.  Put c := -sum_{j in F} n_j (sigma_j + s_j b_{0,j}), pick a contact j_1 notin F and set r := c z_{j_1} e_{j_1}; let y := (n + r)/q*(n + r).
Then psi_y(b_0) = 0 and psi_y takes both signs in O: there are b_+, b_- in O with psi_y(b_+-) = +-c_0, c_0 > 0.  By (T-d) there are
carriers l_i of block m, l_i -> infinity, with q*(u_{l_i} - y) -> 0, and sup_b |val_{l_i}(b) - psi_y(b)| <= ||u_{l_i} - y||_1 +
||U^*(u_{l_i} - y)|| <= q*(u_{l_i} - y) (||z||_infty <= 1, ||e|| = 1).  For i large: l_i >= L, val_{l_i}(b_+) >= c_0/2 and val_{l_i}(b_-) <= -c_0/2.
Put G_i(b) := nu_{l_i}(b) - theta_m(b) = m|val_{l_i}(b)|/Phi_{l_i} - theta_m(b) (continuous on O).  Then G_i(b_+) >= m c_0/(2 Phi_{l_i}) -
sup_O theta_m > 0 for i large, and on a path in O from b_+ to b_- there is a point b_1 with val_{l_i}(b_1) = 0, where G_i(b_1) =
-theta_m(b_1) < 0.  By the intermediate value theorem G_i vanishes at some b_2 in O, so {b in O : |G_i(b)| < eps_{l_i}} is a non-empty open
set.  Hence V_L := union_{l >= L, l in block m} {b : |nu_l(b) - theta_m(b)| < eps_l} is open and dense in Omega.  (3) Omega is an open
subset of a sphere, hence a Baire space; the set in the statement is (the preimage of) intersection_L V_L.  Non-(BT): infinitely many
carriers with |nu - theta| < eps_l are either infinitely many strict non-peaks (Q_m infinite) or infinitely many peaks with margins
mu_l < q_0 Phi_l eps_l/m; with eps_l := (Phi_{l+1}/Phi_l)^2 (say) the latter violate (MS) along s_i := 2 mu_{l_i}.  QED
**Consequences.**  (a) The design question (GO) of part 3.4 has a NEGATIVE answer for every admissible design: rows with F finite,
|F| >= 2 and full contact off F can have infinitely many near-threshold carriers tuned through F (generically, in the fibre of z).
(b) (BT) is meagre in every fixed-z fibre, although (BT) points are dense (Theorem 3.5): the window method's residuals are
generic phenomena, and block-tame approximation is essential.  (c) EXACT degeneracy is easy at fixed z: the closed sets
{b : nu_l(b) = theta_m(b)} are non-empty in every open set (step (2) with eps -> 0), so rows with exactly degenerate peaks tuned through
F are dense in every fixed-z fibre.  (This answers the realizability question of Remark 2.3(2) for exact degeneracy, but NOT in the pure
self-aligned form: at fixed z the fine F-dependent carriers are not re-aligned, see 5.6.)  (d) The owner rule (Construction SA,
Theorem 3.5) escapes Proposition 5.1 because it chooses z depending on a.

## 5.3 Lipschitz threshold; corrected Theorem 3.5(c)
**Lemma 5.2 (threshold is Lipschitz and strictly monotone in peak masses).  PROVED.**  Fix a block, Phi = Phi_m, and zeta^0 in l_1 \ {0}
with a peak k_1 (nu_{k_1} > theta(zeta^0)).  There are r > 0 and 0 < c_Theta <= L_Theta < infinity such that for zeta, zeta' in the
l_1-ball B(zeta^0, r): (a) |theta(zeta) - theta(zeta')| <= L_Theta ||zeta - zeta'||_1; (b) if k is a peak of zeta (nu_k(zeta) > theta(zeta))
and zeta' differs from zeta only by |zeta'(k)| = |zeta(k)| + t, t > 0, then theta(zeta') - theta(zeta) >= c_Theta t.
*Proof.*  Psi(th; zeta) = A^2 - B, A = sum_k (|zeta(k)| - th Phi_k^2)_+, B = sum_k Phi_k^2 min(th, nu_k)^2 (Lemma T); theta(zeta) is the unique
zero of the strictly decreasing function th -> Psi(th; zeta).  (i) |A(th; zeta) - A(th; zeta')| <= ||zeta - zeta'||_1 and, since
d/d|zeta(k)| of Phi_k^2 min(th, nu_k)^2 is 2 nu_k <= 2 th (non-peaks) or 0 (peaks), |B(th; zeta) - B(th; zeta')| <= 2 th ||zeta - zeta'||_1;
so |Psi(th; zeta) - Psi(th; zeta')| <= (A + A' + 2 th) ||zeta - zeta'||_1.  (ii) The right and left th-derivatives of Psi satisfy
-2(A + th) ||Phi||_2^2 <= d Psi/d th <= -2(A + th) sum_{nu_k > th} Phi_k^2 <= -2 (A + th) Phi_{k_1}^2 as long as nu_{k_1} > th.
On B(zeta^0, r) (r small) theta stays in a compact interval below nu_{k_1}, and A, th are bounded above and below by positive
constants.  (a) follows from (i), (ii): Psi(theta(zeta) + h; zeta') <= Psi(theta(zeta); zeta') - c h < 0 for h > (A + A' + 2th)||zeta -
zeta'||_1/c, and symmetrically.  (b) Psi(theta(zeta); zeta') = (A + t)^2 - B > 0 = Psi(theta(zeta); zeta) with Psi(theta(zeta); zeta') >= 2 A t,
and by (ii) Psi(theta(zeta) + h; zeta') >= 2 A t - 2 (A' + th) ||Phi||_2^2 h > 0 for h < A t/((A' + th)||Phi||_2^2).  QED

**Proposition 5.3 (block-tame approximants without degenerate peaks; replaces Theorem 3.5(c)).  PROVED.**  Design with (SF*), diagonal
U, any N.  Let f have F finite and let f^(L) be its fine re-alignment (Theorem 3.5).  Let K_0 be the finite set of carriers l <= L or
with S_l ∩ F != {}.  For every L and every l_0 there is a first row f^(L)_* with the same a, z^(L)_* = z^(L) except at coordinates owned
by carriers >= l_0, such that f^(L)_* has no degenerate peak and satisfies (BT), and p*(f^(L)_* - f^(L)) <= C_f sum_{l >= l_0} lambda_l
log(e/sum_{l >= l_0} lambda_l).  (The construction creates N free coordinates; see Lemma 5.5 for a contact-preserving version.)
*Proof.*  Hysteretic re-run.  For a perturbation of coordinates owned by carriers >= l_a, define the row by re-running the owner
recursion from level l_a with reference signs eps^(L): eps_l := eps_l^(L) unless eps_l^(L) A_l <= -(B_l + delta_l H_l)/2 (forced flip:
eps_l := sgn A_l), and assign the new coordinates and S_l (except levers) accordingly.  Every re-run carrier then has n_l|val_l| >=
(B_l + delta_l H_l)/2 with sign eps_l, hence (Theorem 2.2 Step 4 with |val_l| >= delta°_l/2) is a robust peak with margin >= q_0 delta°_l/4;
carriers < l_a are untouched (the coordinates they own are not touched, and supp u_k is owned by carriers <= k).
Levers.  For blocks m = 1..N choose carriers l_0 <= l_a(1) < ... < l_a(N), l_a(m) of block m and > max K_0, and put s_m := min S_{l_a(m)};
the lever replaces z_{s_m} = eps_{l_a(m)} by t_m eps_{l_a(m)}, t_m in [3/4, 1].  Then |val_{l_a(m)}| decreases at the exact rate
delta_{l_a(m)} 2^{-s_m}/n_{l_a(m)} in 1 - t_m (s_m notin A_{l_a(m)}), stays >= (3/4) delta°_{l_a(m)}, and only carriers > l_a(m) change
otherwise.  Choice of t_1.  With t_2 = ... = t_N = 1 consider block 1: zeta_1(t_1) = zeta_1^fix + (own lever term at k(l_a(1))) +
zeta_1^later(t_1), where ||zeta_1^later(t) - zeta_1^later(1)||_1 <= e_1 := 2(1 + ||U||) sum_{l > l_a(1)} lambda_l.  Let phi(t) := theta of
zeta_1^fix + own term + zeta_1^later(1): by Lemma 5.2(b) |phi(t) - phi(t')| >= c_Theta lambda_{l_a} delta_{l_a} 2^{-s_1} |t - t'|/n_{l_a}, and by
Lemma 5.2(a) |theta_1(t) - phi(t)| <= L_Theta e_1.  The values nu_k, k in K_0, are fixed (carriers of K_0 are < l_a(1)).  So {t : theta_1(t)
= nu_k} lies in an interval of length <= 2 L_Theta e_1 n_{l_a}/(c_Theta lambda_{l_a} delta_{l_a} 2^{-s_1}) <= L_Theta 2^{-8 - k(l_a(1))}/c_Theta
by (SF*) (e_1 <= 2^{-9} lambda_l delta_l 2^{-(m + k(l) + min S_l)} eta_l/n_l with l = l_a(1), min S_l = s_1).  For l_a(1) large the |K_0|
intervals cover less than 1/4: pick t_1 in [3/4, 1] outside them; gamma_1 := min_{k in K_0} |theta_1 - nu_k| > 0.  Then choose l_a(2) so
large that L_Theta 2 (1 + ||U||) sum_{l >= l_a(2)} lambda_l < gamma_1/2 (later levers and their re-runs move theta_1 by < gamma_1/2), and
choose t_2 for block 2 in the same way, etc.  Result: no k in K_0 is degenerate; every other carrier is a robust peak; Q_m is contained
in K_0 (finite); (MS) holds by Theorem 2.2 Step 8 (margins >= q_0 delta°_l/4); so (BT).  Cost: Z3 Lemma 3.1, Delta_m <= 2 sum_{l >= l_0}
lambda_l.  QED
Consequently Theorem 3.5(c) holds as stated (BT points are dense in {F finite}); the earlier proof ("theta changes continuously and
strictly") overlooked the infinitely many later carriers containing the moved coordinate (Lemma 1.2), whose sign changes make
theta discontinuous; the hysteretic re-run plus Lemma 5.2 repairs it.

## 5.4 Design thresholds and the rigidity of exact data (corrects Lemma 4.1 / Proposition 4.2)
Lemma 4.1 as stated is correct, but with C_0 = max|omega| + 2 max|Delta d| "negligible" (|c_k| < 2^{-3} C_0 lambda_k) contains EVERY
carrier not carrying omega when |Delta d| << |omega| (the typical case: in 5.1, Delta d = 1.3e-11, Delta_alpha = 1), so Proposition 4.2
was vacuous there.  The correct scale is C_1 := max_m |Delta d_m| for carriers not carrying omega, with a design-tiny threshold.
Design conditions (tau_l a decreasing design sequence in (0, 1]; n_l in [3/4, 5/4] as before):
 (SF_tau)  (1 + ||U||) sum_{l'' > l} lambda_{l''} <= 2^{-10} tau_l lambda_l delta_l 2^{-(m(l) + k(l) + min S_l)} eta_l/n_l, plus the second half of (SF*);
 (b')      2 c_l <= tau_{l'} 2^{-2s} c_{l'} delta_{l'} for every s in supp y_l ∩ S_{l'}, l' < l.
Both are upper bounds on c_l in terms of data fixed before c_l is chosen (finitely many pairs (l', s) at stage l), so Lemma 2.1 applies
verbatim: every SLD-type design can be modified to satisfy them.  OWNER of a coordinate j: the first carrier o(j) with j in supp u_o
(a design notion; o(j) is the unique l with j in S_l if j is a signature coordinate, by allowedness (a)).
**Lemma 4.1' (dominance with design thresholds).  PROVED.**  Let D = sum_k c_k u_k, j notin F, o = o(j), and C_1 >= 0 with |c_k| <= C_1 lambda_k
for every k > o with u_k(j) != 0.  If |c_o| >= tau_o C_1 lambda_o, then sgn D(j) = sgn(c_o u_o(j)) and |D(j)| >= (31/32)|c_o u_o(j)|.
*Proof.*  Later carriers k at j have j in supp y_k \ S_k and |u_k(j)| <= 4/3.  (i) j in S_o, j <= m(o) + k(o) + 4: later total <= (4/3) C_1
sum_{k > o} lambda_k <= (4/3) 2^{-10} tau_o C_1 lambda_o delta_o 2^{-(m + k + min S_o)}/n_o, leading >= tau_o C_1 lambda_o delta_o 2^{-j}/n_o; ratio
<= (4/3) 2^{-10} 2^{j - m - k - min S_o} <= 2^{-5}.  (ii) j in S_o, j > m(o) + k(o) + 4: by (b') each later k at j has c_k <= tau_o 2^{-2j}
c_o delta_o/2, and c_{k+1} <= c_k/4, lambda_k <= c_k/2, so the later total is <= C_1 (4/3)(1/2)(4/3) tau_o 2^{-2j} c_o delta_o/2 = (4/9) C_1 tau_o
2^{-2j} c_o delta_o, while the leading term is >= tau_o C_1 m 2^{-m-k} c_o delta_o 2^{-j}/n_o >= (4/5) tau_o C_1 2^{-m-k} c_o delta_o 2^{-j}; ratio
<= (5/9) 2^{m + k - j} < 2^{-5}.  (iii) j in supp y_o \ S_o: later total <= (4/3) C_1 sum_{k > o} lambda_k <= 2^{-9} tau_o C_1 lambda_o eta_o/n_o <=
2^{-9}|c_o u_o(j)|.  QED
**Proposition 4.2' (exact data force owner alignment).  PROVED.**  Design with (SF_tau), (b'); F finite; two-piece data at f with
C_1 := max_m |Delta d_m| > 0; c_k := lambda_k [(omega^-_m - omega^+_m)(k) - Delta d_m w_m(k)] (m = m(k)); K_omega := carriers in supp omega^+-
(finite); E := union_{k in K_omega} supp y_k \ F (finite).  Call k NEUTRAL if c_k = 0 and NEGLIGIBLE if 0 < |c_k| < 2 tau_k C_1 lambda_k.
Then for every j notin F ∪ E whose owner o is neither neutral nor negligible:  D(j) != 0, j is a contact, and z_j = sgn(c_o u_o(j)).
For o notin K_omega this reads  z_j = -sgn(Delta d_{m(o)}) sgn(val_o) sgn(u_o(j))  (w(k) has the sign of zeta(k), i.e. of val_k).
*Proof.*  If o notin K_omega: a carrier k in K_omega with u_k(j) != 0 would have j in S_k (j notin E), hence be the owner; so all
carriers at j are outside K_omega and |c_k| = lambda_k |Delta d_m| |w(k)| <= C_1 lambda_k (|w| <= M <= 1).  If o in K_omega (j in S_o \ E),
the later carriers at j are again outside K_omega.  Lemma 4.1' gives D(j) != 0 with the stated sign; Lemma 3.3 (D vanishes at free
coordinates and is z-signed at contacts) gives the rest.  QED
Reading (N = 1, C_1 = |Delta d|).  k notin K_omega is neutral iff val_k = 0, negligible iff 0 < |w(k)| < 2 tau_k, i.e. iff k is a strict
non-peak with 0 < |val_k| < 2 tau_k theta Phi_k/(m M): a value tuned to a DESIGN-TINY fraction of the threshold scale ("nearly neutral";
the objects K_nn of Z6/Y2).  So a row carrying exact data with Delta d < 0 is OWNER-ALIGNED (z_j = sgn val_o sgn u_o(j)) at every
coordinate outside F, E and the coordinates owned by K_omega-, neutral or negligible carriers ("dead zones").  Rows with Delta d_m < 0
for all m: the same with block-wise signs.  (For the self-aligned rows of Theorem 2.2, this is the owner rule.)

## 5.5 Exact negative-d-mismatch data without dead zones are recovered
Standing hypotheses for this section: design with (SF_tau), (b') (hence (SF*)); diagonal U; F finite; g in C(f) carries two-piece data
(b^+-, omega^+-) with kappa_w <= 1 and Delta d_m < 0 for EVERY block m; notation of Proposition 4.2'.
 (H1) No carrier is neutral, and only finitely many carriers are negligible.
 (H2) D(j) != 0 for every j in the finite set E' := E ∪ {j notin F : o(j) in K_omega ∪ Neg, |c_{o(j)} u_{o(j)}(j)| <= 32 sum_{k > o(j)} |c_k u_k(j)|},
      Neg := the negligible carriers.  (E' is finite: for o in K_omega ∪ Neg, c_o != 0, and on S_o the later terms are <= C 2^{-2j} by (b'),
      while c_o v_o(j) ~ 2^{-j}; the new target coordinates of o are finitely many.)
**Lemma 5.4 (fine re-alignment carries exact data).  PROVED.**  Under (H1), (H2): f has no free coordinate off F, and for all L >= L_0(f)
the fine re-alignment f^(L) of Theorem 3.5 satisfies (T1) and (T2) of Lemma 3.6 for these data; the transplanted data (b^+-_L, omega^+-)
satisfy ||b^+-_L - b^+-||_1 -> 0, Delta d^(L)_m -> Delta d_m, G_L -> g (L -> infinity).
*Proof.*  No free coordinate: by Proposition 4.2' (owners outside K_omega ∪ Neg ∪ E), by the definition of E' and (H2) (the rest), D(j) != 0
at every j notin F, so j is a contact (Lemma 3.3).  Take L_0 beyond K_omega, Neg and E', and so large that tau_L <= M_m/2 (all m) for L >= L_0.
Uniform convergence: coarse values are unchanged, ||zeta^(L) - zeta||_1 <= 2(1 + ||U||) sum_{l > L} lambda_l, and w_m(k) = sgn(zeta(k)) M_m
(peaks) or M_m (nu_k/theta_m) sgn(zeta(k)) (strict non-peaks) is Lipschitz in zeta uniformly in k <= L (Lemma 5.2(a) for theta; M, C, |zeta|
are Lipschitz by Lemma T); so sup_{k <= L} |w^(L)(k) - w(k)| <= C_f sum_{l > L} lambda_l <= tau_L (by (SF_tau), L large), and Delta d^(L) ->
Delta d (d(omega) = <Dw, D omega>/C is continuous).  (T1): the omega-carriers are coarse strict non-peaks with fixed values and theta^(L) ->
theta.  (T2), coordinate by coordinate (j notin F; f^(L) has no free coordinate since f has none and the owner rule assigns +-1):
 - o(j) > L (fine): z^(L)_j = eps^(L)_o sgn u_o(j) (owner rule), w^(L)(o) = eps^(L)_o M^(L) (robust peak), so c^(L)_o = -Delta d^(L) lambda_o w^(L)(o)
   has sign eps^(L)_o and |c^(L)_o| >= tau_o C_1^(L) lambda_o (M^(L) >= M/2 >= tau_o); no K_omega-carrier meets fine coordinates; Lemma 4.1' gives
   z^(L)_j D^(L)(j) > 0.
 - o(j) <= L, o notin K_omega ∪ Neg, j notin E: z^(L)_j = z_j = sgn(c_o u_o(j)) (Proposition 4.2'), and |w^(L)(o) - w(o)| <= tau_L <= tau_o with
   |w(o)| >= 2 tau_o (non-negligible) keeps sgn c^(L)_o = sgn c_o and |c^(L)_o| >= tau_o C_1^(L) lambda_o; Lemma 4.1' again.
 - o(j) in K_omega ∪ Neg, j notin E': the owner term dominates by the factor 32 at f; c^(L)_k -> c_k uniformly relative to lambda_k, so it
   still dominates at f^(L) (the definition of E' has room 32 > 2).
 - j in E' (finite): z_j D(j) > 0 strictly by (H2) and D^(L)(j) -> D(j).
Cost (Lemma 3.6): ||D^(L) - D||_1 <= (5/3) sum_k lambda_k |Delta d^(L) w^(L)(k) - Delta d w(k)| -> 0 (dominated convergence: |w| <= 1, sum lambda
< infinity, pointwise convergence); the flipped contacts Fl lie in fine coordinates, where D and D^(L) are sums over fine carriers only, so
||D 1_Fl||_1 + ||D^(L) 1_Fl||_1 <= (10/3) C_1 sum_{l > L} lambda_l -> 0.  QED
**Lemma 5.5 (bank levers remove degenerate peaks and keep exact data).  PROVED.**  Let f' := f^(L) (L >= L_0 of Lemma 5.4) with its
transplanted data.  For each block m choose a fine carrier l_b(m) > L of block m and s_m := min S_{l_b(m)} (a contact with z = eps_{l_b(m)}),
and BANK there: a^#(mu) := (a + sum_m mu_m eps_{l_b(m)} e_{s_m})/q*(...), mu_m >= 0 small, z unchanged, then re-run the owner recursion from
level l_b(1) with hysteresis (as in Proposition 5.3).  For suitable small mu (chosen block after block) the row f^# has support
F ∪ {s_1, ..., s_N}, no degenerate peak, satisfies (BT), carries transplanted exact data (bank coordinates treated as contacts, which
is the contact-likeness required by Y4-ref Lemma P2) with Delta d^# < 0, and p*(f^# - f') + ||G^# - G'|| -> 0 as mu -> 0.
*Proof.*  Effects of a bank of mass mu at s = s_m: (Ue)_j = s_j^2 a_j/nu with nu^2 = nu_0^2 + s_s^2 mu^2, so zhat changes by O(mu^2) on F and
zhat_s = eps(1 + s_s^2 mu/nu) + O(mu^2) (scale invariance).  Hence |val_{l_b(m)}| increases at the exact first-order rate v_{l_b}(s) s_s^2/nu;
carriers whose support contains s are l_b(m) and carriers > l_b(m) (allowedness (a)); F-dependent carriers move by O(mu^2); forced flips
of the re-run occur only at carriers l with delta°_l <= C mu, i.e. at levels >= l(mu) -> infinity, and, by the second half of (SF*)
(lambda_l <= delta°_l 2^{-l-9}), all carriers >= l(mu) together carry weight <= 2 delta°_{l(mu)} 2^{-l(mu)-9} <= C' mu 2^{-l(mu)} = o(mu).
By Lemma 5.2: theta_m(mu) = theta_m + kappa_m mu_m + o(mu_m) with kappa_m >= c_Theta lambda_{l_b} v_{l_b}(s) s_s^2/nu > 0, while every coarse
nu_k (k <= L) moves by O(mu^2).  The finitely many coarse carriers are the only candidates for degeneracy (fine carriers are robust
peaks), so for small mu_1 > 0 block 1 has none (gap gamma_1 > 0); choose l_b(2) and mu_2 so small that block 1 moves by < gamma_1/2, and so
on.  (BT): F^# finite, Q_m^# within the coarse carriers, no degenerate peak, (MS) by margins (Theorem 2.2 Step 8).  (T1), (T2): as in
Lemma 5.4 (all coefficients move continuously in mu, uniformly relative to lambda_k; the re-run part is owner-aligned; at s_m the owner
l_b(m) dominates, so D^#(s_m) z_{s_m} > 0 and the data can be split contact-like there).  Cost: Y4 Lemma 2.2 (banks) and Lemma 3.6.  QED
**Theorem 5.6 (exact negative-d-mismatch data without dead zones are recovered).  PROVED.**  Under the standing hypotheses of 5.5 and
(H1), (H2):  (f, g) in cl NA((c_0, p), l_2^2).
*Proof.*  For L -> infinity and mu -> 0 (diagonal sequence) the rows f_i := (f^(L_i))^#(mu_i) are (BT), hence satisfy (SC) in every
block, converge to f, have support F ∪ B_i (banks) and carry exact two-piece data with Delta d < 0 representing G_i -> g, with
kappa^(i)_w -> kappa_w.  Theorem 3.7 applies with Z3 Lemma U replaced by its banked version (Y4-ref Lemma P2: Lemma U and Theorem E
hold for f_n -> f with supp a_n = F ∪ B_n for data contact-like on B_n).  QED
**Corollary 5.7 (corrected Proposition 4.5).  PROVED.**  At the self-aligned rows of Theorem 2.2 with finitely many exceptional
carriers tuned through F (including EXACTLY degenerate swallowing-type peaks, if present), every mate carrying two-piece data with
kappa_w <= 1, omega supported on exceptional strict non-peaks, Delta d < 0 and c_k != 0 for the omega-carriers is recovered,
provided every exceptional strict non-peak not carrying omega has |w(k)| >= 2 tau_k.  (Proof: the
targets of the exceptional carriers lie in F, so E = {}; all non-exceptional carriers are robust peaks with |w| = M, hence non-neutral and
non-negligible for large k; exceptional ones are finitely many with c != 0; (H2) holds since every coordinate off F is dominated by
its owner, Theorem 2.2(d) and Proposition 3.2(ii).)  Proposition 4.5 as stated in part 4 claimed this for all omega-data with
Delta d <= 0; the hypothesis c_k != 0 on the omega-carriers (no neutral omega-carrier) is needed (otherwise S_k is a dead zone), and the
case Delta d >= 0 is Corollary D1 of the note (no (SC) needed).  Numerical check: 5.1.

## 5.6 Positive d-mismatch exact data force dead zones
**Design condition (FD) (fresh-dominated carriers).**  For every block m there are infinitely many carriers l of block m with a
coordinate j_l notin union_i S_i, owned by l (j_l in no support of a carrier < l), such that
   |y_l(j_l)| > (1 + max_i s_i) (||y_l||_1 - |y_l(j_l)| + delta_l H_l).
(Designable: add to the target family the vectors (e_j^* + r)/q* with r tiny, for fresh j; the family stays dense and (T-a)-(T-d),
(P1)-(P3), allowedness are unaffected.)
**Proposition 5.8.  PROVED.**  Design with (SF_tau), (b'), (FD).  If g in C(f) (F finite) carries two-piece data with Delta d_m > 0 for some
block m, then all but finitely many of the (FD)-carriers of block m are neutral or negligible.  In particular exact data with a
positive d-mismatch in some block live only at rows with infinitely many (nearly) neutral carriers, i.e. with dead zones.
(If ALL Delta d_m >= 0 the data are recovered anyway by Corollary D1; Proposition 5.8 matters for MIXED data, where some block has
Delta d < 0 and needs (SC).)
*Proof.*  For all but finitely many (FD)-carriers l of block m: l notin K_omega and j_l notin F ∪ E (the j_l are pairwise distinct).  If such
an l were neither neutral nor negligible, Proposition 4.2' would give z_{j_l} = -sgn(Delta d_m) sgn(val_l) sgn(y_l(j_l)) = -sgn(val_l) sgn(y_l(j_l)),
|z_{j_l}| = 1.  By Lemma 1.1, n_l val_l = y_l(j_l) z_{j_l} + R with |R| <= (1 + max s)(||y_l||_1 - |y_l(j_l)| + delta_l H_l) < |y_l(j_l)| (|zhat_i| <= 1 + s_i),
so sgn val_l = sgn(y_l(j_l)) z_{j_l} = -sgn val_l, a contradiction (val_l != 0).  QED
Also, for N >= 2, a block with Delta d_m = 0 has only neutral carriers outside K_omega.  So, under (FD), every exact-data configuration
that is not covered by Theorem 5.6 (all Delta d_m < 0) or by Corollary D1 of the note (all Delta d_m >= 0, no (SC) needed) has dead zones: infinitely many neutral or negligible carriers
(blocks with Delta d_m >= 0 next to blocks with Delta d_m < 0, or nearly neutral carriers in Delta d < 0 blocks), or an exact cancellation
D(j) = 0 at one of the finitely many coordinates of E'.

## 5.7 What a counterexample must look like, and the main obstacle
Collecting parts 1-5 (designed operator: SLD-type with (SF_tau), (b'), (Z0), (GM), (FD); diagonal U):
 1. Finitely tuned instances of (B), (C), (D) are (BT) points, recovered (Cor. 3.1); the most dangerous explicit coherent-shift mates
    (Proposition 3.2) and their exactly degenerate variants (Corollary 5.7) are recovered.
 2. Exact two-piece data are recovered at every F-finite row unless the row has DEAD ZONES (Theorem 5.6, Proposition 5.8, Corollary
    D1): infinitely many neutral or nearly neutral carriers (values tuned to within a design-tiny fraction tau_k of the threshold scale,
    or exactly 0), or a block with Delta d_m >= 0 next to one with Delta d_m < 0, or an exact cancellation at a finite exceptional set.
 3. Near-threshold carriers tuned through F are Baire-generic in each fixed-z fibre (Proposition 5.1); the design cannot exclude them;
    block-tame approximation (Proposition 5.3) and owner re-alignment (Lemma 5.4) neutralize them for exact data.
 4. Hence a counterexample (f, g) with F finite must have: g NOT representable with exact two-piece data and kappa_w <= 1 at f (so the
    window method is needed: residuals (B) tiny minors of sliced-ray matrices, (C) shift resonance at clean windows), or exact data
    with dead zones; with F infinite, (E) remains (V3's domain; lacunary profiles remove its critical form, Lemma 2.6).
Main obstacle (precise).  DEAD ZONES: a coarse coordinate j all of whose coarse carriers are neutral or nearly neutral (e.g. carriers of a
d-neutral block, Delta d_m = 0, when N >= 2) has its d-row sign D(j) decided by FINE carriers; block-tame re-alignment of those fine
carriers (needed for (SC)) may reverse that sign while z_j is frozen, so the exact data cannot be transplanted.  The violation is
quantitatively tiny (at most C sum_{l > L} lambda_l in l_1), so the remaining step is a STABILITY statement: exact two-piece data that fail
(T2) at a (BT) companion by an l_1-amount epsilon can be corrected to exact data at a nearby (BT) companion at cost o(1) as epsilon -> 0.
