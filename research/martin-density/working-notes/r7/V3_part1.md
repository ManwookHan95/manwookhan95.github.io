# V3 part 1 (working notes, first observations on (O4-crit)); superseded by V3_notes.md where they differ

Setting: design D_sigma (SLD-type, signatures v_l(s) = delta_l 2^{-s}/n_l on S_l), I finite, f with F infinite, a bad carrier l with
S_l subset F up to finitely many points (support swallowing), w_{m(l)}(k(l)) = 0 (d-neutral), sign eps of a on deep S_l.
gamma_s := eps g_s / v_l(s) (signature profile of the mate), rho_s := |a_s|/v_l(s) (cushion profile).

## 1.1 Per-coordinate structure of decompositions on the deep part of S_l (PROVED, elementary)
On S_l only u_l and finer targets y_{l'} (l' > l, allowedness (b): 2c_{l'} <= 2^{-2s}c_l delta_l at s in supp y_{l'} cap S_l) are nonzero.
Hence for a two-sided decomposition at scale t: eps B_pm(s) = (gamma_s - theta_pm) v_l(s) + r_pm(s), theta_pm := eps lambda_l Theta_pm(k(l)),
with |r_pm(s)| <= sum_{l'>l, s in supp y_{l'}} lambda_{l'}|Theta_pm(k(l'))||y_{l'}(s)|/n_{l'} <= (3+eta)/t * sum c_{l'}/4 ... which is
<= C 2^{-2s} c_l delta_l / t, i.e. a fraction O(c_l/delta_l) of the cushion |a_s|/t in the critical regime |a_s| ~ v_l(s)^2.
So the per-coordinate split of the switching between the two sides is NOT free: p_s = (theta_+ - gamma_s)/(theta_+ - theta_-), fixed by
two numbers theta_pm and the profile of g.  (The referee's model Fdec(t) = sum 2(tDv - 2|a|)_+ assumes a free per-coordinate split.)

## 1.2 Copying versus deep assignment (PROVED arithmetic; model statement)
Flip excess of the + side of a decomposition at scale r: E_+(theta, r) = sum_s 2(r (theta - gamma_s)_+ v_s - |a_s|)_+  (= Exc_{beta}(r),
beta = (theta-gamma)_+ v).  Fixed data COPYING (theta_+, theta_-) pay at scale r exactly E_+(theta_+, r): the same function of r as the
decomposition, evaluated at another scale.  Loss = oscillation of r -> E_+(theta, r)/r^2 ("phase"), not cushion sharing.
Exactly geometric model (v_s = c 2^{-s}, |a_s| = v_s^2, gamma constant): Exc_v(x)/x^2 =: Phi(x) is log-periodic with values in
[4/3, 3/2] (computation: m_v(y) = 2v_s on (v_s, 2v_s]; int_0^{v_s} m = (2/3)v_s^2; Phi(v_s(1+u)) = 2(2/3+2u)/(1+u)^2, max 3/2 at u = 1/3,
min 4/3 at u in {0,1}).  So the oscillation of the flip coefficient is a factor 9/8 (not 2).

## 1.3 Upper points (HEURISTIC at this stage; to be made precise)
Single carrier, constant gamma on the deep part: E_+(theta, r)/r^2 = (theta-gamma)^2 Phi(r(theta - gamma)): depends on (theta, r) only
through the phase r(theta-gamma) and a continuous prefactor.  If the + side's optimal coefficient theta_t is continuous in t, the
phase t(theta_t - gamma) sweeps every value near 0, so there are scales t at which theta_t sits at an upper phase: the copied data are
then valid (with flips) at all smaller scales with no loss.  (Crossing argument: the curves r = x_j/(theta-gamma) separate the strip.)

## 1.4 Two-phase routing (HEURISTIC model)
Two critical populations (two near-duplicate bad carriers with the same target and antiphase profiles, or two gamma-values) give a
cost r -> F(theta, log r) with two competing maxima in the phase; the minimizing curve can zigzag around the ends of the ridges, and
fixed (or window-averaged) data can lose a constant (model: harmonic vs arithmetic combination of phi_lo = 4/3, phi_hi = 3/2: about 6%).
