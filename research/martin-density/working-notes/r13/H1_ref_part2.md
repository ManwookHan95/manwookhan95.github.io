# H1-ref part 2: Lemma TF', Lemma NP, Theorem RL, Lemma KC, Lemma AL

Sources: r13/H1_part2.md, H1_part3.md 3.2, H1_notes 3-5; r11/K2_notes 4.1(d), 5.1-5.4 (K2.8, K2.9, K2.16, K2.17); r12/J1_notes 1-6,
J1_ref_notes B-E (R-PK, R-PB, F-2, P-TU, J1.15'); r9/X1_notes 1.1, 2.1, X1_ref_notes D1.  Scripts: r13/H1_ref_work/.

## 2.1 Lemma TF' (target freedom as a lever).  Verdict: CORRECT (mod chain), constants precision P-TF.
Re-derivation.  Ft_l(rt) = val_l - rt_l kappa_{m(l)} with val, kappa at the fixed input row R_1, so Ft(rt') = Ft(rt_0) - (kappa_{m(l)}(rt'_l -
rt_{0,l}))_l and phi_y(rt') = phi_y(rt_0) - <kappa y, rt' - rt_0> exactly.  If Step A is not A-regular at rt', K2.9(b) gives a unit y with
max_g(-y^T g(rt')) < 2(rho_0(rt') + ||b(rt')||)/W(rt') <= 4 Design^{-C_A} u^3 and phi_y(rt') > -rho_0(rt').  The Sys-A columns are AFFINE in the
targets (the peak-resource columns -(1 - X) lambda_c v_c(s) rt^{(m)}, the gtil-terms gtil = g - (rt_l G_{m(l)})_l; J1-ref P-1), with
Lipschitz constant C_G <= Design^C in the per-unit-move normalization of K2 5.2 (not divided by column norms), so y is a near-certificate
of size <= 4 Design^{-C_A} u^3 + C_G |rt' - rt_0| <= eps_* at rt_0 (C_A larger than the exponent of eps_*, as in K2's use of K2.9(b) inside
K2.16).  Then phi_y(rt') <= ||b(rt_0)|| - 4(||b(rt_0)|| + x) < -x/4 <= -rho_0(rt'), a contradiction.  Realization by K2.9(c).
P-TF (precision).  The displacements actually used by H1's levers are <= Design^C u^{-C'}(||b|| + x) with C' up to 3-4 (exchange of OUT(b):
t/rt_k with c_ex ~ u/Design^C and |rt_k| >= u/Design^C gives u^{-2}; KC: lambda_{d_0} ~ delta Design^C/u^2), not always u^{-1} as TF' and
H1 11 state.  This is harmless: (i) C_G |rt' - rt_0| <= eps_*/2 and rho_0(rt') <= x/4 hold for any fixed polynomial in Design/u because
eta' <= (u/(4 Design))^{4L^2 + 80}; (ii) P-TU's x_TU must dominate 24 W(rt') = 24 Design^{C_A} u^{-3} max(x, ||b(rt')||): choose x_TU :=
Design^{C_A + C_J + C_H} u^{-C_H} x with one ABSOLUTE C_H covering all H1 levers; the window [x_TU, x'_max] still has ratio >= 2^{6G(L)} for
L >= l_f (T <= (u/(4 Design))^{L^2 + 20}); enlarging x_TU only enlarges the (U)-class (unpulled carriers), as R-6/P-TU did; (iii) J1.13 (i)'s
distance allowance and the data closeness K t tolerate any Design^C u^{-C} x (violation <= Design^C u^{-C} x/t << K t since x/t <= C T^3).
[The proof of TF in H1_part2 2.1 bounds ||kappa Delta||/c_Delta "by (TF2)", which gives the opposite inequality; the endpoint form TF'
avoids the issue by assuming the size bound directly.  Use TF'.]

## 2.2 Lemma AL (needed direction).  Verdict: CORRECT.
y_l = eps_l coef_l + eps_l zeta_m lambda_l (d kappa_m/d zeta(l)) (H1 omits the eps_l on the second, error, term); coef_l = kappa_y rho_l +
O(eps Design^2) (J1.6(a), every near-certificate of size <= eps_*); rt_l = rc_l + O(x/kappa_m) with rc_l = eps_l u_l(xhat_1)/kappa_m;
|d kappa/d zeta(l)| <= C b^2 D^2 for coarse strict non-peaks in route V under (FC) (J1-ref B.3; in route V kappa_m = sum_{peaks}|zeta(c)| +
S_m/theta_m, so non-peak derivatives come only from the fine S-term).  Hence y_l rt_l = kappa_y rho_l u_l(xhat_1)/kappa_m + O(eps Design^2 +
Design^2 eta' + b^2 D^2); the main term has modulus >= (c_*/nu_1)(u/2)|rc_l| >= c_* u^2 Phi_l/(2 nu_1 m K) for robust status (>= the same
with u -> 1 - b for near-threshold), which dominates the errors because u(w) >= 4(log_2 1/T)^{-1/20} decays only logarithmically while
eps_* = Design^{-C}.  The sign is the same for every near-certificate because kappa_y in [-C, -c_*/nu_1] for all of them (K2.16(3), J1-ref
B.2).  Q_l(y) = y_l/rt_l = kappa_y kappa_m rho_l/u_l(xhat_1)(1 + o(1)).  Kind (i): |coef_l| <= eps Design^2 (K2.16(2a)), so Q_l = o(1).

## 2.3 Lemma NP (peak-resource dichotomy in (U)-blocks).  Verdict: CORRECT; numerically confirmed (new toy).
(a) R-PK and J1-ref B.2's corollary.  Correct.
(b) Logic re-derived.  Every coarse carrier, peaks included, has six private near coordinates N_c in (s_max(L), d(L)] (K1 2.7 / K2 1), all
in U_L ∩ [1, D(L)], hence of type TS, S_th, FR or ZD (K2 4.1(d)).  In a (U)-block a peak carries no class data (gamma_c = -Delta'_m lambda_c
vs_c = 0), so a private S_th coordinate of c is zero-data, hence ZD (K2 4.1(d) proof: "zero-data ones are also ZD").  An FR or ZD private
coordinate is a private two-sided peak resource; a TS coordinate is not (its mass move has the common-mode term kappa_u a_s).  So without
a peak resource all private design-depth coordinates of every peak are TS: every peak is thick-type.  Signed derivative: in route V,
kappa_m = A_m + theta_m Phi_P^2 + S_m/theta_m = sum_{c in P}|zeta(c)| + S_m/theta_m (A = sum_P Phi^2(nu - theta)), the threshold equation
involves the peaks only through sum_P|zeta(c)| and Phi_P^2, so d kappa_m/d zeta(c) = vs_c(1 - X_m) with ONE value 1 - X_m for all peaks
(numerics: H1_ref_work/peakderiv.py, 397 random blocks with >= 2 peaks, spread of d kappa/d|zeta(c)| over the peaks <= 1e-7; with all
strict non-peaks in Omega, X_m = 0 exactly).  Then coef_c = -zeta_m lambda_c vs_c (1 - X_m) and J1.6(a) give zeta_m = -kappa_y rho_c vs_c/
(lambda_c(1 - X_m)) + O(eps Design^2/lambda_c): sign sgn(rho_c vs_c) for EVERY near-certificate, modulus >= c_* u/(4 nu_1).  Correct.
Numerics (H1_ref_work/np_rl_toy2.py, np_rl_toy3.py, outputs .out): J1-ref's consistent one-block toy modified so that the peak has three
private TS coordinates (a = rho_c v_c, |rho_c| = 0.1, aligned or anti-aligned with the peak value, which is carried by generator-free deep
contacts) and NO peak resource; the hole scale t is tuned to the no-peak-resource resonance (see 2.6 below).  In 26/26 runs the near-certificate
has sgn zeta(y; rc) = sgn(rho_c vs_c) (|zeta| ~ 0.088, robust), d kappa/d zeta(c) = +1.0000.  (The toy's constants are not separated -- the
peak's TS columns have efficiency mu^2/nu ~ 3e-3 -- so coef_c/(kappa_y rho_c) = 0.34-0.38 instead of 1; only signs are meaningful.)

## 2.4 Theorem RL (block-rescaling lever).  Verdict: CORRECT (mod chain); numerically confirmed.
Pairing sigma_m delta kappa_m zeta_m >= delta kappa_m z_0 for all near-certificates (Lemma NP(b)); whole-block rescaling of a (U)-block
preserves every tiny polynomial (homogeneity in r^{(m)}: X1-ref D1, also when the polynomial involves ratios of other blocks); statuses by
Lemma K (rho_d(s rt) = m s|rt_d| K(sigma, s^2 R^2)/Phi_d); robust peaks move by << u (theta rises with the non-peak values; margins u);
(RL+) needs no near-threshold coarse non-peak; in (U)-blocks inactive near-threshold carriers are exactly the D2-pushed ones (X1-ref D2), so
(RL+)'s hypothesis is "m unprotected".  Correct.
Numerics (np_rl_toy2/3): after creating an obstruction (targets displaced along y, phi_y = 1e-3; min ||t||_inf = 1.0e-2 .. 4.9e-1),
whole-block rescaling by 1 + sigma_m delta gives phi_y = -3e-3 and min move 6.7e-4 .. 7.1e-4 in 26/26 runs; the opposite direction gives
phi_y = +5e-3 and the move stays at 1.0e-2 .. 2.0e-1.

## 2.5 Lemma KC (inward compensation in (U+)).  Verdict: CORRECT; can be STRENGTHENED (P-KC).
Re-derivation: rows outside N_0 get status factor (1 + delta) K(sigma, R'^2)/K(sigma, R^2) <= 1 once R'^2 <= R^2 - 3 delta(R^2 + 8.5/c_K)
(dK/dR^2 >= c_K, K <= 8.5 on the W-fix region); d_0 provides it with lambda_{d_0} <= delta Design^{C_K}/(2u^2) <= 1; pairing >= kappa_m delta z_0/2
under (KC).  Correct.
P-KC (strengthening, PROVED).  The requirement "N_0 contains every D2-pushed row of m" is unnecessary: a D2-pushed row outside N_0 is up-scaled
by 1 + delta like every other row outside N_0, and its status is multiplied by (1 + delta)K'/K <= 1, so its margin (<= 1 - c eta'/2) is kept.
Hence N_0 = {d_0} suffices, and d_0 may be ANY movable row of m with robust or near-threshold status (an inactive row, or an active row with a
free ratio: its inward displacement does not touch Z_kappa, its own status decreases, and m|rt_{d_0}| >= u Phi_{d_0}/K still gives
lambda_{d_0} <= delta Design^{C_K}/(2u^2)).  (KC) for d_0 alone: y_{d_0} rt_{d_0} <= z_0 u^2/(4 Design^{C_K}) for all near-certificates.
Consequence: in (U+) a residual stage needs y_{d} rt_{d} robustly positive for EVERY movable row d of m with robust or near-threshold status.
Inactive rows are zero-data, so their S_th near coordinates are ZD: an inactive row is of kind (i) (then Q_d = o(1) and (KC) holds) or has six
thick near coordinates (kind (iii), support-swallowed, thick-type), or of kind (ii) (no near-certificate).  So in (H-4): EVERY movable row of
m with robust or near-threshold status is an ANTI-ALIGNED thick-type carrier (or a kind-(iv) active free row with rt eps sigma > 0).

## 2.6 NEW (referee): Proposition MA' -- frozen-value cancellation in EVERY (U)-block, thick-type peaks included.  PROVED (mod chain).
Statement.  Let m be a (U)-block at a stage carrying a near-certificate y of size eps <= eps_*.  Call a coarse carrier of m (row or peak)
thick-type as in J1 (thick private p in S_k ∩ [1, D(L)], rho_k := a_p/v_k(p)).  Then
   sum over ALL thick-type coarse carriers k of m (rows AND peaks) of rho_k u_k(xhat_1)
        = -(kappa_m/kappa_y) sum_{non-thick kind-(iv) rows l of m} (rt_l eps_l sigma_l)(coef_l sigma_l) + O(Design^4 (eps + eta') + D^2 b^2 Design^2).
With a private peak resource no peak is thick-type and this is H1's Proposition MA; WITHOUT a peak resource every peak is thick-type
(Lemma NP(b)) and the peaks enter the cancellation.
Proof.  Rows: zeta_m (1 - Xt_m) = sum_{rows l of m} rt_l eps_l coef_l (from y_l = eps_l coef_l + eps_l zeta_m lambda_l dkappa/dzeta(l)), with
|Xt_m| <= C b^2 D^2 (route V).  Thick rows: rt_l eps_l coef_l = kappa_y rho_l u_l(xhat_1)/kappa_m + O(eps Design^2 + Design^2 eta') (Lemma AL);
kind (i): O(eps Design^2); kind (ii) excluded.  Peaks: with a peak resource |zeta_m| <= (4/3) eps Design (R-PK) and no peak is thick-type.
Without one, for each peak c, coef_c = -zeta_m lambda_c vs_c (1 - X_m) = kappa_y rho_c + O(eps Design^2), so rho_c vs_c/lambda_c = r_m + O(eps
Design^2/u) is common to all peaks and zeta_m = -kappa_y r_m/(1 - X_m) + O(...).  Euler (K2.8): kappa_m = sum_k (d kappa/d zeta(k)) zeta(k) =
(1 - X_m) sum_{c in P} lambda_c |u_c(xhat_1)| + O(b^2 D^2), so sum_{c in P} rho_c u_c(xhat_1) = sum_P (rho_c vs_c/lambda_c) lambda_c |u_c| =
r_m kappa_m/(1 - X_m) + O(...) = -(kappa_m/kappa_y) zeta_m + O(...).  Insert into the row identity and multiply by kappa_m/kappa_y.  QED
Consequences.  (1) The R-PB / stable-exact relation (per-block frozen value ~ 0) holds in EVERY (U)-block at every stage carrying a
near-certificate whose non-thick rows are of kind (i), with the peaks counted in the no-peak-resource case.  (2) In (U+) (aligned peaks,
sum_P rho_c u_c > 0) the THICK ROWS of m must carry a robustly negative frozen value: anti-aligned rows dominate (this is the source of
H1's "anti-aligned-dominated unit" in (H-4)).  (3) The no-peak-resource near-certificates sit on the codimension-one resonance
sum_{thick-type k of m} rho_k u_k(zhat) = 0 (rows and peaks).
Numerics (H1_ref_work/ma_peak_check.py, .out): in the toy of 2.3 the argmin over t of the smallest singular value of the two-sided columns
(the near-certificate) coincides with the root of rho_0 u_0 + rho_1 u_1 + rho_c u_c (zhat) to 5 digits, where the extended frozen value is
<= 4e-4 while the rows-only value is +-0.53 .. 0.70 (10/10); kappa_m = Phi_c |u_c(zhat)| to all digits (route V: kappa = sum_P |zeta(c)|).
