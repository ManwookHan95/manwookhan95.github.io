# X1 part 1 — what a kappa-neutral lever must be: the floor lemma (working notes, to be cleaned)

Setting: U1 / U1-ref notation.  Block m at a first row; P peaks, Q strict non-peaks, Omega ⊂ Q switching set, Omega_a active
part (class a), r_l := u_l(zhat)/kappa_m, R^2 := m^2 sum_{Omega} r_l^2, s_f := theta^{-2} sum_{Q \ Omega} nu^2 Phi^2,
a := A/theta, k := kappa/theta, rho_l = m |r_l| k / Phi_l (l in Omega) (Lemma R-kt).

## 1.1 Lemma K (closed form of k).  PROVED.
Put sigma := Phi_P^2 + s_f.  Lemma R-kt's system a^2 = Phi_P^2 + k^2 R^2 + s_f, k = a + Phi_P^2 + s_f depends on (Phi_P^2, s_f) only through
sigma, and (with R < 1, a > 0) has the unique solution
   k = K(sigma, R^2) := [ sigma + sqrt( sigma^2 R^2 + sigma (1 - R^2) ) ] / (1 - R^2),    a = k - sigma.
K is strictly increasing in sigma and in R^2 (dk/dR^2 = k^2/(2(a - k R^2)) > 0 since a > kR > kR^2).
Proof.  Substitute a = k - sigma into a^2 = sigma + k^2 R^2: (1 - R^2) k^2 - 2 sigma k + sigma^2 - sigma = 0; the root with k > sigma
(a > 0) is the displayed one.  Monotonicity in sigma: numerator increasing, denominator fixed.  In R^2: implicit differentiation as
in U1-ref.  QED
Uniform form: a^2 = E := sum over ALL carriers k of the block of Phi_k^2 min(rho_k, 1)^2 (peaks contribute Phi^2, strict non-peaks
rho^2 Phi^2), and k = a + E - sum_{Omega} rho^2 Phi^2.

## 1.2 Lemma F (floor lemma: levers must be robust at f).  PROVED.
At fixed active ratios (r_l)_{l in Omega_a} and fixed set of robust peaks P_rob, every active Omega carrier l satisfies
   rho_l >= rho^0_l := m |r_l| K(Phi_{P_rob}^2, R_a^2) / Phi_l,    R_a^2 := m^2 sum_{Omega_a} r^2,
with equality iff every inactive Omega ratio is 0, s_f = 0 and P = P_rob.  Hence any sequence of moves that ends at an exact point
(active ratios in the zero set Z of the tiny minors) and creates a carrier of robust relative position from a carrier that was nearly
neutral at f gains NOTHING: the best attainable statuses at an exact point r' are rho^0_l(r').  A kappa-neutral lever helps exactly by the
amount of INACTIVE k-MASS present at f:  I(f) := K(sigma(f), R(f)^2) - K(Phi_{P_rob}^2, R_a(f)^2) >= 0.
Proof.  Lemma K and monotonicity; inactive Omega carriers and fine strict non-peaks only add to R^2 resp. sigma; a near-threshold
peak pushed below threshold contributes rho^2 Phi^2 <= Phi^2 to sigma.  QED
CONSEQUENCE.  A designed lever carrier that is nearly neutral (or absent from the active structure) at f and is TUNED to robust relative
position at a companion cannot replace (KN): it raises k first and its inward push only gives back what it took.  So any design route
to (KN) must produce carriers that are robust and inactive AT f (before the companion), for every f in (C*).
Also: fine levers (weights <= c_{L+1}) have capacity <= c_{L+1}^2 << b(w) and cannot compensate Lojasiewicz displacements eta >= b(w);
medium-weight levers (between sub-windows) are coarse for later sub-windows and break the pigeonhole count (each adds >= 1 rate object
per sub-window: M sub-windows cannot dominate omega_0 + (M - 1) rate objects).
Numerics: X1_work/lemmaK_check.py (50 digits, 70 random blocks): closed form of K rel. err 3.5e-50; a^2 = E rel. err 6.3e-50.

## 1.3 Effective columns (the coupling rows eliminated).  PROVED.
In U1's coarse system put Delta'_m = sum_{l in Omega_a(m)} r_l gamma_l ((X3)_m divided by kappa_m).  Then the coarse certificate is
   L(gamma) = sum_{l in Omega_a} gamma_l c_l(r_l),     c_l(r_l) := u_l|_{E_c} - r_l tau_{m(l)},   tau_m := sum_{p coarse peak of m} vs_p lambda_p u_p|_{E_c},
so the exact cone of a class is {gamma : L(gamma) z^#-admissible on E_c, (X2), (X4), (X5)} with (X4) rewritten through Delta'(gamma).
Each column depends only on its OWN ratio; tau_m (the block's peak trace) is a design vector once the pattern (peak set and signs) is
fixed; the weights Phi_l of the Omega carriers do not enter the cone at all (only lambda_p of peaks, through tau_m).
Proof.  Substitute (X3) into L(Delta', gamma) of U1 2.1.  QED
Consequence: all r-dependence of the exact system is the position of each active column on the line u_l + R tau_m.
