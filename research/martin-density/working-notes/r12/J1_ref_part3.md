# J1 referee, part 3: Propositions J1.10-J1.12, Lemmas J1.13-J1.14, Theorem J1.15; new Lemma R-PB

## 3.1 Proposition J1.10 (legitimate bands).  Verdict: (a) CORRECT for (U)-blocks ((KN)-blocks SKETCH, as labelled); (b) WRONG as worded
## (precision P-D2, fix PROVED); (c) CORRECT as "if" (the "iff" is only "if"); (d) correct as "not shown by (B1)-(B2)".
(a) Re-derived: |Delta R^2| <= m^2 (2 C b beta_* + beta_*^2)/kappa^2 <= C Design^C (b eta'/u + eta'^2/u^2) << eta' (b << u, eta' << u^2/Design^C), and
    the carrier's own rho moves to <= b + Design^C eta'/u << u: (B1), (B2) hold; D2-pushed carriers of the block (margin c eta') are also protected
    since the R^2 change is << eta'.  No rescaling and no peak resource are needed here.
(b) P-D2.  "Blocks without protected statuses (no active carrier at all, i.e. inactive blocks; ...)": an inactive block can contain D2-pushed
    carriers (inactive near-threshold carriers of (U)-blocks pushed inward by eta', cert0 3.4 D2) whose margin is only c eta'.  A band of
    half-width beta_* on a ROBUST row (|r_l| robust) changes R^2 by ~ 2m^2 |r_l| beta_*/kappa ~ Design^C eta'/u and moves those statuses by
    C D^C Design^C eta'/u >> c eta'.  FIX: "without protected statuses" must mean: no active near-threshold carrier AND no D2-/KN-pushed carrier
    (every coarse carrier of the block has a robust status or is a robust peak).  With this definition (b) is correct.  Otherwise use the
    coupling of J1.14 (with F-2 below), which then needs the block's private peak resource.
(c) (B2) is sufficient; necessity is not shown, so "legitimate iff" should read "legitimate if".

## 3.2 Proposition J1.11 (first-order Puiseux margin).  Verdict: SKETCH (label honest); claim plausible.
Re-checked: GEN applied to the union of critical-value cylinders over a Whitney stratification definable over k gives regularity at every point
of Z ∩ {F = 1} (as NLM).  The missing step is a UNIFORM first-order decrease along curves approaching lower strata.  Two remarks: F is Lipschitz
on the compact region, so mu_kappa(h) <= Lip h, i.e. the Puiseux exponent is always >= 1 and J1.11 asserts exactly that it equals 1; and the
gap is a genuine semialgebraic uniformity statement (Whitney (a) controls tangent limits, not the length of admissible curves in the bigger
stratum), not a bookkeeping issue.

## 3.3 Proposition J1.12 (mismatch tolerance).  Verdict: CORRECT as a conditional statement, with precision P-MT.
P-MT.  The (X4^0) rows of block m have coefficients m^2 |r_l| K(sigma_rob, R_a^2) with R_a^2 = m^2 sum_{active} r^2, so moving the ACTIVE ratio r_k
by delta also changes every (X4^0) coefficient of the block by m^2 |r_l| (dK/dR^2) 2 m^2 |r_k| |delta| <= C D^C |delta| (and k's own coefficient
by m^2 K |delta|).  (MT2) must require slack >= C(|gamma_k(t)| + D^C |Delta'_m(t)|) |delta_0| on the class data.  Everything else re-derived.

## 3.4 Lemma J1.13 (target sets).  Verdict: CORRECT as far as checked (PROVED by inspection; one addition).
Checked uses of ratios/values: Gamma^#(kappa, a) is weight-free and involves only ACTIVE ratios, sigma_rob, peak traces (X1 2.2(iv), cert1);
inactive carriers have gamma_l = 0 (X1 Lemma EC), so V does not see their values; statuses through Lemma K (all Omega ratios via R^2); the
true shift is sum r^#_l gamma_l (U1 Lemma 4.6), equal to the cone shift when the data are projected at r^#; Lemma H at r^# has the same bound
when tiny minors vanish exactly (they involve pinned ratios only) and robust ones stay >= u/4 (moves Design^C beta_*/kappa << u); (U)-block
minors are homogeneous in r^{(m)} (cert0 3.4 D1); Sys-DC's targets are the companion's values (K2 4.1); Lemma PM fixes C_m at the approximant
from the companion's values.  ADDITION: in SHIFTED blocks inactive carriers switch by Domega(l) = Delta'' w(l) (cert0 3.5), so their values
also enter the curvature budget H_m and the kind of l; a band changes these by O(Design^C beta_*), far inside the curvature slack and the kind-[2]
requirement (robust gap).  In (U)-blocks Delta'' = 0 and nothing changes.

## 3.5 Lemma J1.14 (rescaling coupling).  Verdict: CORRECT only after FIX F-2 (genuine gap in the non-circularity used by J1.15).
FINDING F-2.  J1.14 rescales "the (U)-block targets s r'^{(m)} of X1 2.1(U)", i.e. the ACTIVE ratios, and J1.15 bounds the resulting change of
phi_y by kappa_m (1 - s_m) zeta_m(r') using |zeta_m| <= 2 eps Design.  But the private peak resource controls zeta_m(y; rt) = sum over ALL rows of
block m (actives, holds, D-pushes) of y_l rt_l (Lemma R-PK), not the active partial sum.  In case (J-c) the banded carrier k is a ROBUST hold:
|y_k| >= c_* u/(8 nu_1) (J1.6(a)) and |rt_k| = |rc_k| is robust, so zeta_act = zeta_m - y_k rt_k - (other holds) = -y_k rt_k + O(eps Design) is ROBUST.
Restoring the active statuses after the band's R^2 drift needs 1 - s ~ (dK/dR^2/K) 2 m^2 |r_k| beta/kappa, so the change of phi_y is ~
(dK/dR^2/K) 2 m^2 r_k^2 beta |y_k|, to be compared with the band's gain beta |y_k|/2: ratio 4 m^2 r_k^2 (dK/dR^2)/K = 2 rho_k^2 Phi_k^2/(K(a - K R^2))
(Lemma K).  Numerics N4 (ref_noncirc.out): the ratio ranges over 0.01 ... 14 for admissible block data (e.g. sigma = 0.02, rho_k = 0.9,
Phi_k = 0.45: 14.3), so the band does NOT absorb phi_y in general: circular, exactly the obstruction J1.10(d)(ii) describes.
FIX F-2 (PROVED).  Rescale ALL targets of block m by the same s_m (active ratios, holds, D2/KN-pushed targets; KN-1 zeros are unchanged) and let
s_m be the largest s <= 1 - C Lip eta' at which every PROTECTED status of block m (actives and D2/KN-pushed) computed at the realized values is
within its margin (actives <= 1 - eta'/2, D2-pushed <= 1 - c eta'/2).  Then:
 (a) Z_kappa is preserved (minors homogeneous of degree 0/1 in the active part of r^{(m)}); robust minors scale by >= s^n >= 1/2;
 (b) by Lemma K, rho_d(s rt) = m s|rt_d| K(sigma, s^2 R^2)/Phi_d <= s rho_d(rt) for EVERY carrier d of the block (R^2 is the full Omega sum), so
     every status decreases; inactive values are used only through statuses (J1.13), so rescaling the holds is legitimate; s_m is continuous
     (each rho_d is strictly increasing in s where rt_d != 0) and 1 - s_m <= C(Lip eta' + D^C sum_l (|r_l| beta_l/kappa_m + beta_l^2/kappa_m^2));
 (c) for a near-certificate y at the targets rt(s) = s rt(1) (on block m), Lemma R-PK gives |zeta_m(y; rt(1))| = |zeta_m(y; rt(s))|/s <= (8/3) eps
     Design, and phi_y(s) = phi_y(1) + kappa_m (1 - s) zeta_m(y; rt(1)), so |phi_y(s) - phi_y(1)| <= 3 kappa_m (1 - s) eps Design: negligible.
 (d) The Brouwer coupling of J1.14(c) needs W >= Design^{C_A} u^{-3} sup_s ||b(s)|| (so that J1.8(b) produces near-certificates of size <= eps_*
     for every s in the range); ||b(s)|| <= ||b(1)|| + kappa_m (1 - s) ||rt^{(m)}||; beta_* depends on rho_0 = C_2 W^2, and the resulting fixed-point
     relation beta = 16 nu_1 (||b|| + 2 C_2 W(beta)^2)/(c_* u) has a solution near 16 nu_1 ||b||/(c_* u) because C_2 Design^{2C} u^{-7} beta << 1.
     P-TU applies (W <= x_TU/24).  The selection is jointly continuous in (s, right-hand side) because the generator set depends on s
     continuously and band-A-regularity holds uniformly (Hoffman bounds uniform on the compact s-range).

## 3.6 Theorem J1.15.  Verdict: CORRECT after F-2, P-TU, P-D2 (modulo J1.13's inspection, J2, and the cited chain).
(J-a): J1.7 with P-TU.  (J-b): K2.17(c)-(e) (refereed).  (J-c), (J-d): J1.9 + J1.13 + J1.14 with F-2 (and, for (J-c) in a block with no active
carrier, P-D2).  For (J-c) with TINY status no coupling is needed (J1.10(a)), hence no private peak resource; J1's residual item (R-np) is
therefore too large (it should exclude nearly neutral zero-data carriers).  (J-e), (J-f): conditional, correct (with P-MT for J1.12).
The conclusion "Theorem K2.15 / J2.1 apply at the stage" requires K2.15's proof to accept a band-realized companion: this is exactly J1.13.

## 3.7 LEMMA R-PB (per-block target hyperplane; new sufficient condition and new necessary condition).  PROVED (modulo the chain).
Let L >= l_f, a stage (L, w, a) after (P) and pre-placements, and a block m such that
 (i) m has a private two-sided peak resource;
 (ii) every tuned carrier of m is thick-type (thick private p, rho_l := a_p/v_l(p); the set K_0 ∩ m), privately tunable (kind (i) of K2.16), or of
      kind (iv) with rt_l eps_l sigma_l of the sign OPPOSITE to S_m below (or 0);
 (iii) K_0 ∩ m != {} and  |S_m| > tau_* := C eps_* Design(L)^3 nu_1/c_*,  S_m := sum_{l in K_0 ∩ m} eps_l rho_l rt_l.
Then Step A carries no near-certificate of size <= eps_*, hence is A-regular (K2.9(b)).
Proof.  Let y be a near-certificate of size eps <= eps_*.  For tuned l, y_l = eps_l coef_l + zeta_m lambda_l dkappa/dzeta(l), so (U1 Lemma 1.4(c),
route V) zeta_m (1 - Xt_m) = sum_{tuned l in m} rt_l eps_l coef_l with Xt_m <= 1/4.  By J1.6(a), coef_l = kappa_y rho_l + O(eps Design^2) on K_0 ∩ m;
by K2.16(2a), |coef_l| <= eps Design^2 on kind (i); on kind (iv), rt_l eps_l coef_l = (rt_l eps_l sigma_l)(coef_l sigma_l) with coef_l sigma_l >=
-(eps Design + |kappa| theta_0) Design, so these terms have the sign of rt_l eps_l sigma_l up to O(eps Design^2 + theta_0 Design^2).  If S_m > tau_*,
kappa_y S_m <= -(c_*/nu_1) tau_* = -C eps_* Design^3, and the kind-(iv) terms are <= O(eps Design^2 |Lambda| max|rt|); hence zeta_m <= -(C/2) eps Design^3
for C large, contradicting Lemma R-PK (|zeta_m| <= (4/3) eps Design).  S_m < -tau_* is symmetric.  QED
NECESSARY CONDITION (PROVED, contrapositive).  At every stage carrying a near-certificate, every block m satisfying (i)-(ii) has |S_m| <= tau_*.
Since eps_l rho_l rc_l = rho_l u_l(zhat_1)/kappa_m (rc_l = eps_l u_l(zhat_1)/kappa_m), this reads
      | Phi_0^{(m)}(zhat_1) + kappa_m sum_{l in K_0 ∩ m} eps_l rho_l (rt_l - rc_l) | <= kappa_m tau_*,     Phi_0^{(m)} := sum_{l in K_0 ∩ m} rho_l u_l,
so |Phi_0^{(m)}(zhat_1)| <= kappa_m (tau_* + C Design max_l |rt_l - rc_l|): the per-block FROZEN VALUE nearly vanishes at EVERY residual stage
(not only in J1's "stable" case).  With K2.16(4) (a = Phi_0 on the thick private coordinates up to eps Design/|kappa|) this is the stage-wise,
approximate form of J1 7.4(c).  Relation to K2.17(f): with h_l = eps_l rho_l/nu_1 one has h^T rt^{(m)} = S_m/nu_1, so R-PB is a per-block version of
K2.17(f)'s bordered scalar with h_c = 0, needing only |S_m| > tau_* (tiny) instead of a robust lower bound, and allowing arbitrary other blocks;
its kind-(iv) clause complements K2.17(g).  Numerics N3 is an instance: displacing the targets along y gives S_m != 0 and kills the certificate.
