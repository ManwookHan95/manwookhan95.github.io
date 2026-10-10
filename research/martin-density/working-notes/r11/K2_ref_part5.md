# K2 referee, part 5: two further precisions found on re-reading Lemma K2.9(c) and the comparison with K1's (LR)

## 1. Remainder bound in the realization of Step A: freeze the coarse statuses (PRECISION K-8; also applies to K1 Lemma K1.6(A)).
K2.9(c) needs ||Rem(t)|| <= C_2 ||t||^2 on the WHOLE domain K = {t >= 0, ||t||_2 <= W}.  The block scalar kappa_m is C^1 only while the peak set
is fixed.  After Step 0 the active near-threshold carriers of (T)-blocks are strict non-peaks with margin ~ b, while points of K move values by up
to W >> b (W ~ Design^C x, x ~ Design eta' and b << eta').  Inside K such a carrier can cross the threshold, and there the derivative of kappa jumps:
for d in Omega, d kappa/d|zeta(d)| = rho_d M X/C (tiny) on the non-peak side (U1 Lemma 1.4(c)), while on the peak side (cert0's formula
kappa = A + theta[Phi_{P\Omega}^2 + sum_{Omega cap P}(1 - rho^2)Phi^2] + S_f/theta, with U1 Lemma 1.4(a)) one finds at rho_d = 1
      d kappa/ds = M + C (Phi_P^2 - Phi_d^2)/Phi_P^2 - 2 + 2 C Phi_d^2/Phi_P^2 - X = -1 + C Phi_d^2/Phi_P^2 - X,
a jump of order 1.  Then Rem(t) contains a FIRST-order term (jump) x lambda_d x (overshoot) in every row of the block, and T(K) inside K can fail.
The same applies to the faces of K1 Lemma K1.6(A)'s Poincare-Miranda cube.  (Sys-DC is not affected: its moves K_DC r are far below every margin.)
FIX (PROVED).  In the fixed-point map use the block scalars computed with the COARSE statuses frozen at f_1 + Pi: (A_m, theta_m) solve (E1), (E2)
with the peak set P^1_m frozen (a nonsingular smooth system, Jacobian bounded below by Phi_{P}^2 >= D^{-2}), fine carriers computed truly (their
status changes cost at most C c_{L+1} ||t|| in Rem, << rho_0/W since c_{L+1} <= exp(-1/T) << W).  This frozen map is C^{1,1} with design
constants on K, so Brouwer (K2.9(c)) and Poincare-Miranda (K1.6(A)) apply.  At the solution the ratios are exactly r'' (frozen formulas), the frozen
rho_d = m|r''_d| K(sigma, R^2)/Phi_d <= 1 - mu/2 for the active near-threshold carriers (Lemma K is exactly the frozen computation), robust peaks
and non-peaks keep their side (moves << u); hence the frozen (A, theta) satisfy the TRUE threshold equations, whose solution is unique (lem:threshold),
so the frozen solution is a true solution.  Fine-status changes enter kappa by <= C c_{L+1} (S-0 drifts, << mu).  No conclusion changes.

## 2. A-regularity must allow move sizes Design^C x/u(w) to contain K1's (LR) (PRECISION K-7).
K2 says (7.2) that (H2) is WEAKER than the Sys-A half of K1's (LR).  (LR) gives a right inverse of norm <= Design^{C_0}/u(w), i.e. a positive-spanning
modulus eps_PS >= u(w)/Design^{C_0}; but u(w) (= b(w^-) for i >= 2) can be far below Design(L)^{-C_1}, so K2.9(a) does not apply with K2's W =
Design^{C_A} max(x, ||b||).  Fix: define A-regularity with W := Design(L)^{C_A} u(w)^{-3} max(x, ||b||) and take eps_* := u(w)^3 Design(L)^{-C}
in Theorem K2.16.  Moves <= W keep all estimates (costs C_f Design^C (x/u^3) log(1/x) = o(u^2 T^2) since x <= C Design T^4/L and u^2 >= 16
log_2(1/T)^{-1/10}; robust objects move by Design^C x/u^3 << u).  K2.9(a) holds with eps_PS >= u Design^{-C_0} once C_A >= C_0 + 2 (then
||b||/eps_PS <= W/4); K2.9(b) gives near-certificates of size < 2(rho_0 + ||b||)/W <= 4 u^3 Design^{-C_A}; and every step of K2.16 survives with
eps <= u^3 Design^{-C}: the only u-sensitive step is kind (ii), |kappa| <= 8 eps Design^3/u^2 <= 8 u Design^{3-C}, still << c_*/nu_1.  With this
definition (LR) => (H2), as K2 claims.
