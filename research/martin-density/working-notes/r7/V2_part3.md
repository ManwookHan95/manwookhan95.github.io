# V2 part 3 — Item (C): coherent shift resonance.  The shift-pinning rate and the dichotomy at clean sub-windows

## 3.0 Setting and what is used
Design D^{V2} (Part 2), F finite, g in C(f), rho < 1; a clean sub-window w = (l,i), l >= l_f; two-sided decompositions of
g at f at the scales t of w; Y1's classes (R: robust room, pinned diagonally; G: tiny room, closed at the companion,
eps_l = closing sign), Y1 Lemmas 3.1-3.3 (pinning of class R: |Delta theta| <= K_g t; one-sided pinning of class G:
(tau_l)_- <= K_g t with tau_l := -eps_l Delta theta_l; e_0 := Delta B 1_{F^c} - sum_G eps tau u 1_{F^c}, ||e_0||_1 <= K_g t + t^7;
peak relations), Y1's shift sources (U1)-(U3), (L1)-(L3) and Lemma 3.4 (shift pinning under (SP_w)), Y2 Lemma 5.1 (peak
trace), eq:didentity, Lemma lem:switchbudget, Z3 Lemma 3.2 (budget at the closed pattern: raises cost at most twice, flips
are bounded by S_fl <= C K t), K_g <= C_f Design(l)/u(w) (Y1).  kappa = the closed pattern of the companion (Part 2),
with tiny-margin peaks declared strict non-peaks; G_pk (G_np) = class-G peaks (strict non-peaks) of kappa; every peak of
kappa has relative margin >= u(w)/2 (Part 2 (A2)), hence absolute margin mu_k >= c_f Phi_k u(w).
Write delta_m := Delta d_m M_m (decomposition convention Delta d = d_+ - d_-), I_sh := blocks lacking an UPPER or a LOWER
source at w (Y1 Def. 3.3; for the other blocks Y1 Lemma 3.4 gives |delta_m| <= K_d t, K_d = C_f D^3/u(w)).

## 3.1 The shift-extended system and its pinning rate
**Lemma 3.1 (relations satisfied by the actual decomposition).**  PROVED.  For every scale t of w, the actual vector
(delta, tau) in R^I x R^G satisfies, with errors measured in l_1 and bounded by C_f Design(l)^2 K_g t/u(w):
 (R1) tau_l >= 0 (l in G_np);
 (R2) tau_l = eps_l vs_l lambda_l delta_{m(l)} (l in G_pk), where vs_l := sgn w_{m(l)}(k(l));
 (R3) on T(l): z^#_j V_j(tau) >= 0 at contacts of kappa, V_j(tau) = 0 at free coordinates of kappa, where
      V(tau) := sum_{l in G} eps_l tau_l u_l 1_{F^c};
 (R4) for every block m: delta_m + sum_{l in G, m(l) = m} q'_l tau_l = 0, with q'_l := q_l = eps_l Phi_l w_m(k(l))/(m C_m)
      (q_l = val_l/A_m at strict non-peaks, q_l = eps_l vs_l Phi_l M_m/(m C_m) at peaks), except q'_l := 0 for nearly
      neutral carriers (relative d-coefficient rho_l <= b(w); they are exactified to q^# = 0 at the companion);
 (R5) delta_m = 0 for m notin I_sh;
 (R6) for m in I_sh having exactly one source half: delta_m <= 0 (an UPPER source of type (U1)) or delta_m >= 0 (a LOWER
      source of type (L1)), class-R sources being not variables of the system;
 (R7) for an anti-type class-G strict non-peak l with |rho_l - 1| <= b(w) (pinned by Y1 Lemma 3.5(b)):
      tau_l + lambda_l (|w(k(l))|/M) delta_m <= 0;
and moreover, for l in G_pk, eps_l vs_l = +1 (swallowing type) or -1 (anti type), and (R1) holds also at peaks:
tau_l >= -K_g t, i.e. eps_l vs_l delta_m >= -C K t (this is how the sources (L2), (U2) enter).
Proof.  (R1): Y1 Lemma 3.2.  (R2): Y2 Lemma 5.1, -Delta theta_l = vs lambda (delta_m + e_k), 0 <= e_k <= t/(lambda_l mu_k), so
|tau_l - eps vs lambda delta_m| <= t/mu_k <= C_f D(l) t/u(w).  (R3): Delta B 1_{F^c} = V(tau) + e_0; by Lemma lem:switchbudget
and Z3 Lemma 3.2 the closed-pattern cost sum_{j notin F} phi_{z^#_j}(Delta B(j)) is <= 2t/q_0 + C K t, so by Lemma lem:phicalc(c)
the cost of V(tau) is <= 2t/q_0 + C K t + 2||e_0||_1; at a contact phi_{z}(x) = 2(zx)_-, at a free coordinate of kappa
phi_{z_j}(x) >= (1 - |z_j|)|x| >= u(w)|x| (robust target room).  (R4): eq:didentity, Delta d_m M_m = (1/(mC_m)) sum_k Phi w Delta theta_k
+ r_m, |r_m| <= 2t/sigma_m, and Phi_l w Delta theta_l/(m C_m) = -q_l tau_l for l in G (proof of Lemma lem:badpeaks(b)); class R
and fine carriers contribute <= (K_g t + 6t^2)/(m C_m) (Phi|w| <= 1); nearly neutral carriers contribute |q_l tau_l| <=
b Phi M 6 lambda/(m C t) <= t^3 (box).  (R5), (R6): Y1 Lemma 3.4 (its halves).  (R7): proof of Y1 Lemma 3.4 (U3):
tau_l <= lambda_l(3 gap/t - Delta d_m |w(k)|) with gap <= b(w) M, so the defect is <= 3 lambda b/t <= t^3.  The last claim:
(R1) at peaks is Y1 Lemma 3.2 for all class-G carriers.  QED
(Any further relation satisfied by the actual decompositions within C_f Design^2 K_g t/u may be added to the system; it can
only increase the rate below.)
**Definition 3.2 (shift-extended system, shift-pinning rate).**  Sigma^sh(kappa, f) is the homogeneous system (R1)-(R7) in
the variables (delta, tau) in R^I x R^G, with (R1) imposed on all of G (peaks included) and the coefficients of (R4), (R7)
taken at f.  viol(delta, tau) := the l_1 norm of its violations (positive parts of the inequalities, moduli of the equalities).  The
SHIFT-PINNING RATE of the pattern kappa at f is
      rho^sh(kappa, f) := inf{ viol(delta, tau) : ||delta||_1 = 1, tau in R^G }   (in [0, infinity)).
It is homogeneous of degree 1 in (delta, tau) and rho^sh(kappa, f) = 0 iff Sigma^sh(kappa, f) has (possibly asymptotic) solutions
with delta != 0: an exact (or asymptotically exact) d-CONSTRAINED COHERENT SHIFT RESONANCE.  The objects (kappa, "sh") are
design-countable (one per pattern of level <= l), so rho^sh is a rate object in the sense of Y4 Def. 1.1; D^{V2} includes them.

## 3.2 Theorem C1 (dichotomy at clean sub-windows)
**Theorem C1.**  PROVED.  Let w be a clean sub-window of D^{V2} for f and kappa the closed pattern.  Then either
 (I) rho^sh(kappa, f) >= u(w): then for every scale t of w and every m,
        |Delta d_m| M_m <= K_sh t,   K_sh := C_f Design(l)^2 K_g/u(w)^2 <= C_f Design(l)^3/u(w)^3,
     so the shift is pinned with a DESIGN x u^{-3} constant, absorbed by Q(w) = (4 Design/u)^{omega+3}; every use of (SP_w)
     or of (H2'') in Y1 Lemma 3.4-3.6, Prop. 5.2, Theorem E', the master theorem 5.4, Y2 Theorems H, M, Y, and in V1's
     assembly holds at w with this constant; or
 (II) rho^sh(kappa, f) <= b(w).
Proof.  The pigeonhole (Y4 Thm 1.6) applied to the enlarged scheme gives the dichotomy rho^sh >= u or <= b.  In case (I),
by Lemma 3.1 viol(delta, tau) <= C_f Design^2 K_g t/u for the actual (delta, tau); by homogeneity
||delta||_1 rho^sh <= viol(delta, tau), so ||delta||_1 <= C_f Design^2 K_g t/u^2.  The uses of (SP_w) in the cited proofs are
exactly the bound |Delta d_m| M_m <= K_d t (Y1 Lemma 3.4; Z4 Step 3; Y2 Theorem H's K_sh); all later constants are linear
in it, and the window arithmetic only needs K T_hi(w) -> 0, n(w)/K -> infinity for K = (design) x u^{-O(1)} x C_f^{l^2},
which Q(w) provides (Y4-ref A.3).  QED
**Corollary C1.1 (relation with Y2 Theorem H; "decay beyond the ladder" is a design artifact).**  PROVED.
 (a) If kappa has a robust combinatorial shift cost, i.e. c^comb_*(kappa) > 0, where c^comb(delta; kappa) := inf_{x >= 0}
     [ sum_{T(l)-contacts} phi_{z_j}(L_j) + sum_{T(l)-free} |L_j| + sum_{l' in G} 2 m^nat_{l'} (sign defect of the S^nat_{l'}
     coefficient)_- ], L := sum_{m in I_sh} delta_m Pi_m + sum_{G_np} x_l eps_l u_l, Pi_m := sum_{l in G_pk, m(l) = m} vs_l
     lambda_l u_l 1_{F^c} (Y2 5.2 read on the closed pattern), and c^comb_* its minimum over the sign-sphere, then
     c^comb_*(kappa) >= delta_sh(l) := min{c^comb_*(kappa') : kappa' of level <= l, c^comb_*(kappa') > 0}, a DESIGN constant
     (c^comb is a polyhedral function with design coefficients for each of the finitely many patterns; put 1/delta_sh(l)
     into Design(l)), and rho^sh(kappa, f) >= delta_sh(l)/(C Design(l)) > b(w), hence case (I) by cleanliness.  So the
     residual of Y2 5.3(c) "c_* > 0 but decaying faster than the ladder" does not occur at clean sub-windows of D^{V2}: only
     exact combinatorial coherent resonance (c^comb_* = 0) together with a tiny rho^sh can block pinning.
 (b) Case (II) refines Y2's coherent shift resonance by the d-identity (R4): the shift is free only along (asymptotically)
     exact solutions of the WHOLE system (R1)-(R5), including the coupling delta_m = -sum q_l tau_l, i.e. the shift must be
     generated by zero-cost switching of class-G strict non-peaks of the right d-sign (q < 0 for delta > 0: configuration
     (i); q > 0 for delta < 0: configuration (ii)), in agreement with the Z4-referee Remark 3.3.
Proof of (a).  For (delta, tau) take x := (tau)_+ on G_np.  On S^nat_{l'} the coefficient of v_{l'} in L is eps x_{l'} >= 0 for
l' in G_np (no cost) and vs lambda delta_m for l' in G_pk, whose cost 2 m^nat (eps vs lambda delta_m)_- is <= 2 m^nat((tau_{l'})_-
+ |tau_{l'} - eps vs lambda delta_m|), i.e. (R1) and (R2) defects.  On T(l): with tau_{l'} = eps vs lambda delta_m + (R2 defect) at
peaks, |L_j - V_j(tau)| <= max|u| (sum of (R2) defects + sum_{G_np} (tau)_-), and phi_{z_j}(V_j) = 2(z_j V_j)_- (contact rows),
|V_j| (free rows) are (R3) defects.  So c^comb(delta; kappa) <= C Design(l) viol(delta, tau), and ||delta||_1 delta_sh(l) <=
c^comb(delta; kappa) gives rho^sh >= delta_sh(l)/(C Design(l)).  Finally delta_sh(l) >= 1/Design(l) and b(w) <= 2^{-4 Design(l)}.  QED

## 3.3 Theorem E with non-negative d-mismatch, and with (SC) at the companions
**Theorem E^>=.**  PROVED.  Theorem E of Z3 (and Theorem E' of Y1/Y2 with window-dependent c_flat; Y4-ref Lemma P2 for banked
and pulled supports) holds with "d-neutral two-piece data" replaced by "two-piece data with Delta d_m := d^{(j)}_m(omega^-_m)
- d^{(j)}_m(omega^+_m) >= 0 for every m" (data convention of Definition def:twopiece).
Proof.  In the proof of Theorem E (Z3 2.2) d-neutrality is used exactly twice: (i) it is preserved under the averaging
Dbar_j = (1/n) sum_i (b^+-_i, omega^+-_i) — so is Delta d_m >= 0, since d^{(j)}_m is linear and the average of nonnegative numbers
is nonnegative; (ii) Corollary cor:D1 is applied at f_j to the averaged data — Corollary cor:D1 assumes exactly Delta d_m >= 0.
Lemma U (both sides separately) does not involve Delta d.  QED
**Theorem E^SC.**  PROVED.  If, in Theorem E^>=, the data have Delta d_m < 0 exactly for m in a set I_- for which every f_j
satisfies the scrambling condition (SC) of Definition def:SC (with its own sequence), then (f, rho g) in cl NA.
Proof.  As in Theorem E, rho gbar_j in C(f_j) with two-piece data of kappa_w <= rho^2(1 + eta_0/2) =: kappa' < 1.  Theorem
thm:engineered at f_j (I finite, F_j finite, (SC) for I_-) with the parameter rho'_j := 1 - 1/j (rho'^2_j kappa' < 1) gives
(f_j, rho'_j rho gbar_j) in cl NA, and (f_j, rho'_j rho gbar_j) -> (f, rho g).  QED
These are the two recovery engines available for data that FOLLOW a non-pinned shift (Part 4).
