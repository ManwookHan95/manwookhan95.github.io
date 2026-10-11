# H1 part 2: target freedom as a lever; the peak-resource dichotomy of unshifted blocks; the block-rescaling lever

Setting and notation of J1 1 / J1-ref (design T_fin^{K2}, (FC), P-TU windows, F-2).  Stage (L, w, a), input row R_1 = f_1 + Pi of Step A,
targets rt (ratio units), Ft_l(rt) = val_l - rt_l kappa_{m(l)}, b(rt) := -Ft(rt), W(rt) = Design^{C_A} u^{-3} max(x, ||b(rt)||),
rho_0(rt) = C_2 W(rt)^2.  Near-certificate of size eps at rt: unit y with y^T g >= -eps for every generator g of Sys-A at rt (and |y^T g| <= eps
for two-sided g).  phi_y(rt) := y^T Ft(rt).  eps_* := Design(L)^{-C} as in K2.16.  For a block m: zeta_m(y; rt) := sum_{l in m} y_l rt_l.
For a vector Delta of target displacements put <kappa y, Delta> := sum_l kappa_{m(l)} y_l Delta_l.

## 2.1 Lemma TF (target freedom as a lever).  PROVED (modulo the chain cited by K2.9).
Let rt_0 be admissible targets (J1.13 (i)-(ii)) and Delta a displacement such that
 (TF1) for 0 <= s <= s_max the targets rt_0 + s Delta are admissible in the sense of J1.13 (pinned active ratios exactly on Z_kappa, robust
       minors >= u/4, statuses (ii), |rt_0 + s Delta - r_1| <= eta' + Design^C beta_*/kappa_min);
 (TF2) every near-certificate y of size <= eps_* at rt_0 satisfies <kappa y, Delta> >= c_Delta > 0;
 (TF3) s_1 := 4(||b(rt_0)|| + x)/c_Delta satisfies s_1 <= s_max and s_1 ||Delta||_2 C_G <= eps_*/2, where C_G bounds the Lipschitz
       dependence of the normalized generator columns on the targets (peak columns, K2-ref P-1: C_G <= C Design^C).
Then Step A at the targets rt_0 + s_1 Delta is A-regular, hence realized (K2.9(c), with J1.13's projection of the data at the realized ratios).
Proof.  Put rt := rt_0 + s_1 Delta.  Ft(rt) = Ft(rt_0) - s_1 (kappa_{m(l)} Delta_l)_l, so ||b(rt)|| <= ||b(rt_0)|| + s_1 ||kappa Delta|| <= C' (||b(rt_0)|| + x)
(||kappa Delta|| / c_Delta <= Design^C by (TF2) applied to any near-certificate; if none exists the stage is A-regular already), hence
W(rt) <= Design^{C_A + C} u^{-3} (||b(rt_0)|| + x) and rho_0(rt) <= C_2 W(rt)^2 <= x/4 (x = C Design eta' and eta' <= u^{2C''}/Design^{C''}, as in
Corollary 1.3).  Suppose the stage is not A-regular at rt.  K2.9(b) gives a near-certificate y at rt of size eps < 4 Design^{-C_A} u^3 with
phi_y(rt) > -rho_0(rt).  The generator columns at rt and rt_0 differ by <= C_G s_1 ||Delta|| <= eps_*/2, so y is a near-certificate at rt_0
of size <= eps_*; by (TF2), phi_y(rt) = phi_y(rt_0) - s_1 <kappa y, Delta> <= ||b(rt_0)|| - 4(||b(rt_0)|| + x) < -x/4 <= -rho_0(rt).
Contradiction.  The realization is K2.9(c); its moves are <= W(rt) and cost <= C_f Design^C W(rt) log(1/W(rt)) = o(u^2 T^2) (same order as
J1.9's band); the remaining requirements of the downstream chain are those of J1.13, guaranteed by (TF1).  QED
Remarks.  (a) J1.9's band on an inactive row k is the special case Delta = +-e_k (|y_k| >= c_* u/(8 nu_1) by J1.6(a)); (TF1) is then J1.10's
legitimacy.  (b) Lemma TF converts target freedom into a lever whenever the pairing with ALL near-certificates has one sign; J1.6(a)
supplies such signs on thick-type carriers, and 2.2 supplies one on whole unshifted blocks.

## 2.2 Lemma NP (peak-resource dichotomy in unshifted blocks).  PROVED.
Let m be a (U)-block of the class (Delta'_m = 0) at a stage carrying a near-certificate of size <= eps_*.
 (a) If m has a private two-sided peak resource, no coarse peak of m is thick-type and |zeta_m(y; rt)| <= (4/3) eps Design for every
     near-certificate y (J1-ref R-PK and J1.6 Corollary).
 (b) If m has NO private two-sided peak resource, then every coarse peak c of m is thick-type; all thick private coordinates of all
     peaks satisfy a_p = rho_c v_c(p) up to the tiny spread of J1.6(a); the numbers rho_c vs_c/lambda_c (c a coarse peak of m, vs_c =
     sgn u_c(xhat_1) its sign) agree up to C eps Design^2/u; and for every near-certificate y of size eps <= eps_*,
        sgn zeta_m(y; rt) = sigma_m := sgn(rho_c vs_c)  and  |zeta_m(y; rt)| >= z_0 := c_* u/(4 nu_1)   (the same sigma_m for all y).
     sigma_m = +1 iff the peaks are ALIGNED: their thick private coordinates contribute to u_c(xhat) with the peak's own sign.
Proof.  (a) R-PK and J1-ref B.2.  (b) Peaks of a (U)-block carry no class data: gamma_p = -Delta'_m lambda_p vs_p = 0 (X1 Lemma EC), and the
aggregated (X1) row on a peak's private coordinates multiplies -Delta'_m vs_p lambda_p = 0 (cert1 2).  Every coordinate s in S_c ∩ [1, D(L)]
private to c lies in U_L, so by K2 4.1(d) it is of type TS, S_th, FR or ZD; an S_th coordinate of c carries no data, hence is ZD (two-sided
composite).  An FR or ZD private coordinate is a private two-sided peak resource.  So in case (b) every private design-depth coordinate
of every peak is TS; the six near coordinates N_c ⊂ (s_max(L), d(L)] ⊂ [1, D(L)] are private, so c has a thick private coordinate:
c is thick-type.  J1.6(a) (valid for peaks, J1-ref B.2) gives |coef_c - kappa_y rho_c| <= eps Design^2 with kappa_y <= -c_*/nu_1 and
|rho_c| = |a_p|/|v_c(p)| >= u/2.  For an untuned coarse carrier the coefficient of u_c in Psi^A_y is coef_c = -zeta_m lambda_c (d kappa_m/
d zeta(c)) (K2.16 notation).  kappa_m depends on the block vector only through |zeta(k)| (the block norm is invariant under coordinate
sign changes), so the SIGNED derivative is d kappa_m/d zeta(c) = vs_c (1 - X_m) with 1 - X_m in [3/4, 1] for every coarse peak under (FC)
(U1 Lemma 1.4(a): d kappa/d|zeta(c)| = 1 - X_m).  Hence zeta_m = -coef_c vs_c/(lambda_c (1 - X_m)) = -kappa_y rho_c vs_c/(lambda_c (1 - X_m)) +
O(eps Design^2/lambda_c); since lambda_c <= 1 and |kappa_y rho_c| >= c_* u/(2 nu_1), |zeta_m| >= c_* u/(4 nu_1) and sgn zeta_m =
-sgn(kappa_y) sgn(rho_c vs_c) = sgn(rho_c vs_c).  Comparing two peaks c, c' (same zeta_m, same 1 - X_m) gives rho_c vs_c/lambda_c =
rho_{c'} vs_{c'}/lambda_{c'} + O(eps Design^2/u).  The spread statement is K2.17(e) (two thick private coordinates of
robust spread exclude near-certificates).  QED
So in an unshifted block exactly one of two things happens at a stage with a near-certificate: a private peak resource kills zeta_m, or
every peak is thick-type and zeta_m is robust with a sign that does not depend on the certificate.

## 2.3 Theorem RL (block-rescaling lever).  PROVED (modulo the chain cited by J1.15 and J2.1).
Let m be a (U)-block without a private two-sided peak resource at a stage (L, w, a) carrying a near-certificate, sigma_m as in 2.2(b).
Suppose
 (RL-) sigma_m = -1; or
 (RL+) sigma_m = +1 and block m has NO near-threshold coarse non-peak: every coarse strict non-peak and every weak peak d of m has
       rho_d(f) <= 1 - u(w) (robust or nearly neutral; at a clean sub-window the alternative is rho_d in [1 - b, 1 + b]).
Then Step A is realized at the stage: replace the targets of ALL rows of block m (active ratios, holds, D2/KN-pushed targets; KN-1
zeros unchanged) by s rt^{(m)} with s := 1 + sigma_m delta, delta := 4 (||b|| + x)/(kappa_m z_0).
Proof.  Apply Lemma TF with Delta := sigma_m rt^{(m)} (zero outside block m).  (TF2): <kappa y, Delta> = sigma_m kappa_m zeta_m(y; rt) =
kappa_m |zeta_m| >= kappa_m z_0 for every near-certificate (2.2(b)), so c_Delta := kappa_m z_0 and s_1 = delta.  (TF1): (i) Z_kappa is
preserved by uniform rescaling of the active ratios of a (U)-block, robust minors change by a factor >= s^n >= 1/2 (X1-ref D1: in a
(U)-block r^{(m)} occurs only in (X3)_m, all minors and cofactor polynomials are homogeneous of degree <= n in r^{(m)}); inactive targets are
used only through statuses (J1.13).  (ii) Statuses, by Lemma K (rho_d(s rt) = m s |rt_d| K(sigma, s^2 R^2)/Phi_d): for s < 1 every status of
the block decreases (K increasing in R^2), robust ones move by <= C Design delta << u; for s > 1 under (RL+) every non-peak status of m
is <= 1 - u at f, hence <= (1 + C Design delta)(1 - u + C b) <= 1 - u/2 at the new targets, nearly neutral ones stay <= 2b, and peaks
(rho >= 1 + u) move by <= C Design delta.  Distance: |s - 1| ||rt^{(m)}|| <= delta ||rt^{(m)}|| <= Design^C (||b|| + x)/u, inside J1.13 (i)'s
allowance eta' + Design^C beta_*/kappa (beta_* has the same order).  (TF3): delta ||rt|| C_G <= Design^C (||b|| + x)/u << eps_* since x,
||b|| <= Design^C eta' and eta' <= (u/Design)^{4L^2}.  The X1 2.1(U) default rescaling (1 - s_m = C Lip eta') and J1-ref F-2 are
superseded in block m by s (for (RL-) s < s_m^default may be taken: Lemma TF only needs some admissible s >= the stated delta; take
s := min(s_m^default, 1 - delta) under (RL-), and s := 1 + delta under (RL+), where no default rescaling is needed since no status is
near threshold).  QED
Remarks.  (a) Nothing about the thick-type carriers of block m (pinned, free, zero-data, peaks) is used: the lever acts through the
whole block.  In particular pinned active ratios of block m are moved, and exactly so, along the line through rt^{(m)} inside Z_kappa.
(b) The sign sigma_m = sgn(rho_c vs_c) is f's datum (orientation of the peaks' thick private coordinates relative to the peak values),
constant along stages as long as the peaks and their thick private coordinates persist.  (RL-) is the ANTI-ALIGNED case; the aligned
case (RL+)/(U+) is the natural one (a peak's thick private coordinates usually carry the peak's sign), so (U+) is a genuine residual.
(c) Unified reading (part 3): a thick-type carrier "needs" its own value to move INWARD iff it is aligned; for a peak, moving its value
inward is the same as raising all ratios of its block (kappa_m falls), which is the up-rescaling of (RL+).

## 2.4 Consequences for the residual (R0) in unshifted blocks.  PROVED (as statements about J1-ref's residual list).
Let k be a thick-type carrier of a (U)-block m at a residual stage.
 (i) If m has a private two-sided peak resource: k is not a peak (2.2(a)); if k is zero-data or free-active, (J-c)/(J-d) apply; so k is
     PINNED-active ((R-pin)) or D2-pushed ((R-D2)), and R-PB's necessary condition holds for m.
 (ii) If m has no private two-sided peak resource: by Theorem RL the stage is realized unless sigma_m = +1 AND m contains a near-
     threshold coarse non-peak (active near-threshold, active weak peak, or D2-pushed).
Hence, in (U)-blocks, J1-ref's types (R-np) and (R-pk), and (R-pin)/(R-D2) inside blocks without a peak resource, reduce to
      (U+)  a (U)-block without private two-sided peak resource, all of whose (thick-type) peaks are ALIGNED (sgn(a_p v_c(p)) = vs_c on
            their thick private coordinates), containing a near-threshold coarse non-peak.
Refinement of (U+) (PROVED, same proof with Delta := rt^{(m)} on the actives and holds of m, and on each D2-pushed row d of m the
displacement chosen so that its status stays <= 1 - c eta'/2): if every near-threshold non-peak of m is INACTIVE (D2-pushed) and is of
kind (i) (privately tunable, |y_d| <= C eps Design^2) or has a robust ratio pairing of the helpful sign (y_d rt_d sigma_m <= 0), the stage
is realized; the residual (U+) therefore needs an ACTIVE near-threshold carrier in m, or a D2-pushed thick-type/kind-(iv) carrier
whose pairing has the harmful sign.
[Why not more: with an active near-threshold carrier d in m (ratio pinned to the rescaling ray by Z_kappa's homogeneity unless V_m has
other directions), raising all active ratios of m raises rho_d above 1 - eta'/2; the only compensations are inward pushes of inactive
robust carriers (KN-type lever, X1 2.1(KN), U1-ref 3.3) whose own target displacement pairs with y_{d_0}; this works when d_0 is of kind
(i) (|y_{d_0}| tiny) or helpfully oriented (2.5).]

## 2.5 Lemma KC (inward compensation in case (U+)).  PROVED (modulo the chain).
Let m be a (U)-block in case (U+) (2.4), z_0 and sigma_m = +1 as in 2.2(b).  Let N_0 be a set of INACTIVE rows of m containing every
D2-pushed row of m and at least one row d_0 with robust status (rho_{d_0}(f) >= u(w)).  Suppose that for every near-certificate y of size
<= eps_* and every l in N_0
      y_l rt_l <= z_0 u^2 / (4 |N_0| Design(L)^{C_K}),                                                   (KC)
C_K the absolute constant below (e.g. l of kind (i): |y_l| <= eps Design^2 + |zeta_m| C b^2 D^2; or l thick-type with eps_l rho_l rt_l >= 0,
since y_l = eps_l kappa_y rho_l + O(eps Design^2) and kappa_y < 0).  Then Step A is realized.
Proof.  Displacement: Delta_l := delta rt_l for every row l of m outside N_0 (actives, holds; KN-1 zeros unchanged), Delta_l := -lambda_l rt_l
for l in N_0 (inward), zero outside m.  (TF1) Z_kappa: the ACTIVE ratios of m are scaled uniformly (homogeneity, X1-ref D1); inactive
targets enter only through statuses.  Statuses (Lemma K, R^2 the full Omega sum of m): every row outside N_0 has rho multiplied by
(1 + delta) K(sigma, R'^2)/K(sigma, R^2); choose lambda_{d_0} so that
      K(sigma, R'^2) <= K(sigma, R^2)/(1 + delta),   R'^2 = (1 + delta)^2 m^2 sum_{l notin N_0} rt_l^2 + m^2 sum_{l in N_0} (1 - lambda_l)^2 rt_l^2,
with lambda_l := delta for l in N_0 \ {d_0} (D2 rows pushed further inward by the same factor, their statuses decrease).  On the W-fix
region dK/dR^2 = k^2/(2(a - kR^2)) >= k^2/(2 a) >= c_K > 0 (cert1 1), and K <= 8.5, so a decrease of R^2 by 3 delta (R^2 + 8.5/c_K) suffices;
the d_0 term m^2 (1 - (1 - lambda)^2) rt_{d_0}^2 >= lambda m^2 rt_{d_0}^2 >= lambda (u Phi_{d_0}/K)^2 provides it with
lambda_{d_0} <= delta Design^{C_K}/(2u^2) (Lemma K: m |rt_{d_0}| = rho_{d_0} Phi_{d_0}/K).  So every status of m outside N_0 is <= its value at rt,
the N_0 statuses decrease, robust ones move by <= Design^C delta << u, and Z_kappa is preserved.  Distance: as in Theorem RL.
(TF2): <kappa y, Delta> = kappa_m (delta sum_{l notin N_0} y_l rt_l - sum_{l in N_0} lambda_l y_l rt_l)
                       = kappa_m (delta zeta_m(y; rt) - sum_{l in N_0} (delta + lambda_l) y_l rt_l)
                       >= kappa_m (delta z_0 - |N_0| delta (1 + Design^{C_K}/(2u^2)) z_0 u^2/(4|N_0| Design^{C_K})) >= kappa_m delta z_0/2
by 2.2(b) and (KC).  Lemma TF with Delta/delta, c_Delta = kappa_m z_0/2, s_1 = delta := 8(||b|| + x)/(kappa_m z_0).  QED
[So (U+) survives only if every admissible choice of N_0 violates (KC): some D2-pushed row, or every robust inactive row, of m pairs
robustly POSITIVELY (y_l rt_l > 0) with all near-certificates -- for thick-type rows: eps_l rho_l rt_l < 0; or m has no robust inactive row.]
