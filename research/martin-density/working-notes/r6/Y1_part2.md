# Y1 part 2 — Rate objects, clean sub-windows, and the threshold equation

Design D_X (part 1), N >= 1, f in S_{p*} with F finite and forced data (xi, q_0, a, w, F, z, zhat, e, nu).  For a block m
put zeta_m := R_m^** zhat (zhat-units: zeta_m(k) = lambda_{k,m} u_{k,m}(zhat)), A_m := |zeta_m|_m, and theta_m := A_m M_m/C_m
(so the note's threshold constant is vartheta_m = q_0 theta_m/m).  For a carrier l = j(k,m) put
   nu_l := |zeta_m(k)|/Phi_m(k)^2  and the RELATIVE POSITION  rho_l := nu_l/theta_m = |u_l(zhat)|/(Phi_l theta_m/m).
(Lemma T below: k in P_m iff rho_l >= 1; margin mu_{k,m} = q_0 Phi_l theta_m (rho_l - 1)/m on P_m; gap_m(k) = M_m(1 - rho_l) on
Q_m; for strict non-peaks |q_l| = Phi_l M_m rho_l/(m C_m), and q_l = eps_l u_l(zhat)/A_m for bad l (Z6 2.1).)

## 2.1 Rate objects of level l (l >= l_0(f) := max F)
For l'' <= l:
 (R1) ROOM outside the coarse targets: S^nat_{l''}(l) := S_{l''} \ (F ∪ T(l)),
      r^nat_{l''}(l) := min_{sigma = +-1} sum_{s in S^nat_{l''}(l)} v_{l''}(s)(1 + sigma z_s),  rate_1 := r^nat/||v_{l''} 1_{S^nat}||_1 in [0,2]
      (well defined: S^nat_{l''}(l) contains S_{l''} \ ([1,l] ∪ T(l)), whose v-mass is m^nat_{l''}(l) > 0);
 (R2) TARGET ROOM: for j in T(l) \ F, rate := 1 - |z_j| in [0,1];
 (R3) THRESHOLD DISTANCE: rate := |rho_{l''} - 1|;
 (R4) RELATIVE POSITION (relative d-coefficient): rate := rho_{l''}.
Their number is l + |T(l)| + 2l = omega(l).  At level l, "coarse" = index <= l.

**Theorem 2 (clean sub-windows).  PROVED.**  For every f with F finite and every level l >= max F there is i in {1..M(l)}
such that the sub-window w = (l,i) is CLEAN: no rate of level l lies in Band(w) = (b(w), u(w)).  At a clean sub-window every
rate of level l is TINY (<= b(w)) or ROBUST (>= u(w)).
Proof.  The bands of the M(l) = omega(l) + 1 sub-windows of level l are pairwise disjoint (Theorem 1(b)); each of the omega(l)
numbers lies in at most one of them.  QED
(Same pigeonhole as Y4 Theorem 1.6; it holds at EVERY level, not only along a subsequence.)

Scale relations at a sub-window w = (l,i) (Theorem 1): t in W(w) implies t >= T_lo(w), and
   b(w) = T_lo(w)^4/(l Design(l)),  u(w) = b(w^-) (w != (1,1)),  and T_hi(w) <= 1/Q(w) <= u(w)^{omega(l)+8} << u(w).
In particular, for t in W(w):  b(w) Design(l) <= t^4/l,  and  Design(l)^4 u(w)^{-omega(l)-8} = Q(w) <= 2^{-l^3}/(l T_hi(w)).   (2.1)

## 2.2 The threshold equation (any admissible T)
Fix a block, drop m.  For zeta in l_1 \ {0} and x > 0 put
   Ah(x; zeta) := sum_k (|zeta(k)| - x Phi_k^2)_+ ,   Bh(x; zeta) := sum_k min(x Phi_k, |zeta(k)|/Phi_k)^2 ,   Psi := Ah^2 - Bh.

**Lemma T (threshold equation).  PROVED.**  (a) P = {k : nu_k >= theta}, and |zeta||alpha(k)| = |zeta(k)| - theta Phi_k^2 on P.
(b) |zeta| = Ah(theta; zeta) and |zeta|^2 = Bh(theta; zeta).  (c) Psi(.; zeta') has a unique zero on (0, infinity) for every
zeta' != 0, it is positive before and negative after it, and the zero is theta(zeta').  (Same as Y2 Lemma T (a)-(c).)
Proof.  (a) Lemma lem:threshold: zeta/|zeta| = alpha + D^2 w/C, ||alpha||_1 = 1, alpha on P with the signs of w.  On P, |w| = M,
so |zeta(k)| = |zeta||alpha(k)| + Phi_k^2 |zeta| M/C = |zeta||alpha(k)| + theta Phi_k^2.  Off P, |zeta(k)| = |zeta|Phi_k^2|w(k)|/C <
theta Phi_k^2.  (b) Summing (a) over P: Ah(theta) = |zeta| ||alpha||_1.  C^2 = sum_k Phi_k^2 w(k)^2 with |w(k)| = min(M,
C|zeta(k)|/(Phi_k^2|zeta|)) = (C/|zeta|) min(theta, nu_k); hence C^2 = (C/|zeta|)^2 Bh(theta).  (c) Ah is continuous and
nonincreasing, strictly decreasing while positive; Bh is continuous, nondecreasing, and positive for x > 0; Psi(0+) = ||zeta'||_1^2
> 0; if Ah(x) = 0 then Psi(x) < 0, and Ah(x) -> 0 as x -> infinity by dominated convergence.  So Psi is strictly decreasing on
{Ah > 0}, negative afterwards, and has exactly one zero; by (b) for zeta' it is theta(zeta').  QED

Note: M = theta/(theta + |zeta|), C = |zeta|/(theta + |zeta|) (from M/C = theta/|zeta| and M + C = 1).

**Lemma T2 (quantitative stability and raising).  PROVED.**  Let zeta != 0, theta := theta(zeta), A := |zeta|, phi := ||Phi||_2^2,
and let k_0 be a peak with nu_{k_0} > theta (a non-degenerate peak; it exists since ||alpha||_1 = 1); put phi_0 := Phi_{k_0}^2,
h_0 := min(1, nu_{k_0} - theta), C_1 := (1 + 2(theta+1)/A)/phi_0.
(a) (Lipschitz) If zeta' satisfies E := ||zeta' - zeta||_1 with C_1 E < min(h_0, theta), then |theta(zeta') - theta| <= C_1 E.
(b) (raising at a peak) Let c be a peak (nu_c >= theta, degenerate allowed), zeta' with |zeta'(c)| = |zeta(c)| + s, sgn zeta'(c) =
sgn zeta(c), s > 0, and E := sum_{k != c} |zeta'(k) - zeta(k)| <= A s/(8(A + theta + 1)).  Then
   theta(zeta') - theta >= min{1, A s/(8 phi (A + theta + 1))},  and, if C_1(s + E) < h_0,  theta(zeta') - theta <= C_1 (s + E).
Proof.  The c-term of Bh does not change in (b) while c stays a peak; every term of Ah is 1-Lipschitz in |zeta(k)|; every term of
Bh(x; .) is 2x-Lipschitz in |zeta(k)| (both minima are <= x Phi_k, and |min(xPhi, a/Phi) - min(xPhi, a'/Phi)| <= |a - a'|/Phi).
Also, for h >= 0: Ah(x+h) >= Ah(x) - h phi, Ah(x - h) >= Ah(x) + h Phi_{k}^2 for every k with nu_k >= x; Bh(x+h) <= Bh(x) +
(2xh + h^2) phi; Bh is nondecreasing.
(a) Upper bound: for h := C_1 E + epsilon <= h_0, k_0 is in P(theta + h) (for zeta), so Ah(theta+h; zeta) <= A - h phi_0, and
Psi(theta+h; zeta') <= (A - h phi_0 + E)^2 - (A^2 - 2(theta+1)E) < 0 because h phi_0 > E + 2(theta+1)E/A and h phi_0 <= A
(phi_0 h_0 <= Phi_{k_0}^2 (nu_{k_0} - theta) <= |zeta(k_0)| <= A).  [Expand: (A - y)^2 - A^2 = -y(2A - y) <= -yA for 0 <= y <= A,
y := h phi_0 - E.]  Lower bound: Psi(theta - h; zeta') >= (A + h phi_0 - E)^2 - A^2 - 2 theta E > 0 for h phi_0 > E(1 + theta/A).
By Lemma T(c), theta - h < theta(zeta') < theta + h.
(b) Lower bound: with h := min{1, A s/(8 phi(A+theta+1))}, c is a peak of zeta' at level theta + h (nu'_c >= nu_c + s/Phi_c^2 >=
theta + h, since s/Phi_c^2 >= s/phi >= h), so Ah(theta+h; zeta') >= A - h phi + s - E and Bh(theta+h; zeta') <= A^2 + (2theta+1) h phi
+ 2(theta+1)E.  With E <= A s/(8(A+theta+1)) <= s/8 and h phi <= s/8:
   Psi(theta+h; zeta') >= 2A(s - E - h phi) - (2theta+1) h phi - 2(theta+1)E >= (3/2) A s - A s/4 - A s/4 > 0,
so theta(zeta') > theta + h.  Upper bound: as in (a), with A replaced by A + s on the left (the c-term of Ah grows by s).  QED

**Corollary T3 (relative positions under a threshold raise).  PROVED.**  In the situation of Lemma T2(b), for every k != c,
   rho'_k = (|zeta'(k)|/|zeta(k)|) rho_k theta/theta(zeta')   (rho'_k computed for zeta'),
so if zeta'(k) = zeta(k) then rho'_k = rho_k/(1 + delta) with delta := theta(zeta')/theta - 1 >= c_raise s for
s <= 8 phi (A + theta + 1)/A, where c_raise := A/(8 phi theta (A + theta + 1)); and delta <= C_1 (s + E)/theta when C_1(s+E) < h_0.
Proof: rho_k = |zeta(k)|/(Phi_k^2 theta(zeta)); Lemma T2(b).  QED
Reading (PROVED by T, T2): pushing a PEAK outward raises the threshold (rate d log theta/ds = C^2/(M A sum_P Phi^2) at points
where the peak set is locally constant, by differentiating (b)); pushing a STRICT NON-PEAK inward raises it as well (Y2 Lemma
T(d)(ii)); the threshold raise rescales every untouched relative position by the common factor 1/(1+delta).  The d-coefficients
of untouched strict non-peaks, q_l = eps_l u_l(zhat)/A_m, are rescaled by the common factor A_m/A'_m: d-neutrality and the
d-row cone of the block are unchanged (Y2 Section 2 makes the same observation).

## 2.3 Numerical sanity check (Y1_work/threshold_check.py)
200 random finite blocks (n = 12, Phi_k = 2^{-k} x U(0.3,1), random zeta): the block norm computed by SOCP as
min max(||x||_1, ||y||_2) over zeta = x + D y agrees with Ah(theta) at the root of Psi to relative error 6.3e-10; in 582
local pushes the threshold moves in the predicted direction (peak outward: up; strict non-peak outward: down; strict non-peak
inward: up); the derivative of log theta under an outward push of a non-degenerate peak equals C^2/(M A sum_P Phi^2) to relative
error 4e-7.  (A first run with a wrong primal formula, sum instead of max, disagreed; the max form is the Minkowski functional
of B_{l_1} + D(B_{l_2}), dual to ||f||_inf + ||Df||_2.)  Y1_work/t2_check.py: 3000 random blocks (n = 14), random peak c, push
s in [1e-6, 1e-1] A, random perturbation of l_1-size up to A s/(8(A+theta+1)) elsewhere: 0 violations of the lower bound of Lemma
T2(b), 0 of its upper bound, and 0 of the Lipschitz bound T2(a) (3000 random perturbations with C_1 E < min(h_0, theta)).
Sanity checks only.
