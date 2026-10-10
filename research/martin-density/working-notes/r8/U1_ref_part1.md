# U1 referee, part 1 — Lemmas 1.1-1.5 (exactness certificate, threshold identities, kappa-reduction, derivatives, tuning)

Checked against: note lem:threshold, eq:margin, def:twopiece, eq:Lstar, lem:suplevel, lem:peakshift (eq:peakshift, eq:didentity);
V2 Part 4 (Prop. C3), V2-ref 9(g) (data vs decomposition shift); Y1 Lemma T (threshold equation).  Script: U1_ref_work/kappa_indep.py.

## 1.1 Lemma 1.1 (exactness certificate).  Verdict: CORRECT (PROVED).
(a) R_m^* x = sum_k lambda_k x(k) u_k (eq:Lstar), so V(Domega) = sum_l gamma_l u_l with gamma_l = lambda_l(Domega(k) - Delta_m w'(k)); off
Omega, Domega = 0 and gamma_l = -Delta_m lambda_l w'(k(l)) (at peaks -Delta_m vs_l lambda_l M' = -Delta'_m vs_l lambda_l).  Re-derived.
(b) Subtracting the two representations: b^+ - b^- = V(Domega); side conditions give V(Domega) 1_{F'^c} z'-admissible.  Re-derived.
(c) Re-derived line by line: off F', b^+ = chi V 1_{K'} vanishes off K' and is z'-signed on K'; b^- = -(1 - chi) V off F' (V(Domega) = V
there; V = 0 at free coordinates by hypothesis) is (-z')-signed; omega^-+ supported in Omega ⊂ Q' (finite); the second representation
is g by linearity of d'.  Nothing else is needed (V in l_1 since sum lambda ||u||_1 < infinity).
Consistency with the decomposition (used later in 2.4): for a two-sided decomposition with omega_+- := Theta_+- + d_+- w
(lem:suplevel), Theta_- - Theta_+ ... gives omega_- - omega_+ = -Delta Theta - Delta d w, hence for EVERY carrier
lambda((omega_- - omega_+)(k) - Delta_dec w(k)) = -Delta theta_k with Delta_dec := -Delta d.  So U1's gamma_dec := -Delta theta is the
exact analogue of gamma (I checked this because a naive reading suggests an extra term -lambda Delta w(k); there is none).

## 1.2 Lemma 1.2 ((E1), (E2), M = theta/(A+theta)).  Verdict: CORRECT (PROVED).
Re-derived from lem:threshold: at peaks |alpha(k)| = Phi_k^2 (nu_k - theta)/A, sum = 1 gives (E1); C^2 = M^2 Phi_P^2 + (C^2/A^2) sum_Q
nu^2 Phi^2 and M/C = theta/A give (E2); theta C = A M and M + C = 1 give M = theta/(A + theta).

## 1.3 Lemma 1.3 (data identity, kappa-reduction).  Verdict: CORRECT (PROVED).
Re-derived: on Q', Phi^2 w'/(lambda C') = u(zhat')/A' and Phi^2 w'^2/C' = C' nu^2 Phi^2/A'^2; hence
Delta (1 - (C'/A'^2) S_Omega) = (1/A') sum_Omega u gamma; multiply by A'^2/C' = A'(A' + theta') and divide by (A' + theta'):
Delta M' [A'(A' + theta') - S_Omega]/theta' = sum_Omega u gamma.  The second form of kappa' is (E2).  Note kappa' >= A' > 0.
Decomposition version (needed for 2.4(a), checked here): eq:didentity + eq:peakshift give, with Delta'_dec := -Delta d M,
   Delta'_dec (1 + M Phi_P^2/C) = (1/A) sum_{Omega} u gamma_dec + (M/C) sum_{P} Phi^2 e_k + (fine and r_m terms),
and (1/A) kappa = 1 + M Phi_P^2/C + S_{Q\Omega}/(A theta); the last term is <= theta sum_fine Phi^2 <= C_f b^4.  So the decomposition
satisfies (X3) up to (M/C) sum_P Phi_k^2 e_k + O(t) + C_f b^4 |Delta'|.  The peak term is O(t) ONLY at peaks with robust margin
(e_k <= t/(lambda_k mu_k)); see referee part 2, gap G2.
REMARK (simplification, PROVED).  The first form kappa' = [A'(A' + theta') - sum_{Omega} nu'^2 Phi^2]/theta' does not involve the peak set:
kappa' is a continuous function of zeta = R_m^** zhat (A' = |zeta|_m is a norm, theta' is the unique root of Y1's threshold equation,
continuous in zeta; nu'_k, k in Omega, continuous), as long as Omega ⊂ Q' (needed for the identity).  In particular kappa' does NOT
jump when a carrier outside Omega changes status (at nu = theta the carrier contributes theta Phi^2 to both theta Phi_P^2 and S/theta).
Hence the intermediate value arguments of 2.5 and 4.1(1a), (1c) are exact: U1's "jumps of size C c_{L+R_cl+1}" in (1c) do not occur,
and the first term of Lemma 4.6(a) reduces to the drift of step (2).

## 1.4 Lemma 1.4 (derivatives).  Verdict: CORRECT (PROVED).
Re-derived by differentiating (E1), (E2) with P fixed: (a) dtheta = C ds/Phi_P^2, dA = M ds, dkappa = (1 - X) ds;
(b) dtheta = -rho_d M ds/Phi_P^2, dA = rho_d M ds, dS = 2 nu_d ds, dkappa = rho_d (2 + M X/C) ds; (c) dkappa = rho_d M X/C ds.
Independent numerical check (kappa_indep.py: norming functional computed by the clamp parametrization w = sgn(zeta) M min(1, nu/theta)
with theta found by bisection of theta = A M/C at 50 digits — a method different from U1's): 163 random blocks,
|N(w) - 1| <= 2.7e-51, (E1) 5.4e-51, (E2) 1.6e-49, the two forms of kappa 5.1e-51, identity (1.3) with random omega^+- 2.6e-50;
derivatives by central differences (h = 1e-25) on FULL recomputations: (a) 163 tests, max rel. err. 1.7e-27; (b) 27 tests, 3.3e-27;
(c) 27 tests, 1.9e-21.  U1's kappa_check.py re-run: output identical to U1's report.

## 1.5 Lemma 1.5 (kappa tunable by one buffer push).  Verdict: CORRECT in its FINAL form (PROVED), with one remark.
Final form: Omega_m = all coarse strict non-peaks (+ zero-value absorbers), so Q_m \ Omega_m consists of fine carriers only and
X_m = C sum_{Q\Omega} rho^2 Phi^2/Phi_P^2 <= C (sum_{fine} Phi)^2 / Phi_c^2 <= C (2 c_{L+1})^2 D(l)^2 <= 1/4 (better than U1's b^2 bound;
Phi_c >= 1/D(l) since D(l) contains 1/Phi_{l''}).  dkappa/ds = 1 - X in [3/4, 1] on every interval of constant peak set, and kappa is
continuous (remark in 1.3), so kappa is strictly increasing in the push and the IVT gives kappa = kappa' EXACTLY.
The pushes are V1's tools (bank at a far coordinate of the buffer peak, two-sided by z-moves (case (a) of V1 (C3)) or by Lemma TU pulls
and banks when the buffer peak is class G with closed room); first-order effect on the buffer peak only, second-order (Hilbert) on all
other values (V1 Lemma B(i); with the mu-base, U4's B_mu in Design).  The ORIGINAL form (alternative (ii)) is also correct but unused.
