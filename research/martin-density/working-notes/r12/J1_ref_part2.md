# J1 referee, part 2: Lemma J1.6, Theorem J1.7, Lemma J1.8, Theorem J1.9 (+ precision P-TU, Remark R-W)

## 2.1 Lemma J1.6(a) (orientation of thick-type coefficients).  Verdict: CORRECT.
Re-derived.  (i) K2.16(3) gives gamma = kappa_y nu_1 <= -c_* for EVERY near-certificate of size <= eps_* (both cases of its proof: gamma <=
-gamma_0, or the kind analysis forces kappa <= -c_U/2; phi_y is only used through |phi_y| <= |Lambda_A|^{1/2} max(x, ||b||) << c_U).  (ii) The TS
generator at a thick private p of k is two-sided (mass change, |a_p| >= u/2 >> W), so |eff_p (Psi(p) - kappa a_p)| <= eps with eff_p >= 1/Design and
Psi(p) = coef_k v_k(p) + (fine part <= C c_{L+1}); dividing by |v_k(p)| >= v_min(L) >= 1/Design gives |coef_k - kappa_y a_p/v_k(p)| <= eps Design^2.
(iii) |kappa_y a_p/v_k(p)| >= (c_*/nu_1)(u/2): robust, so sgn coef_k = -sgn(a_p v_k(p)) for every near-certificate.  The two-coordinate statement
is K2.16's kind-(ii) computation, valid for peaks as well as tuned carriers (only (2b) is used).  Numerics (rerun): coef_k/(kappa rho_k) = 1.0000.
Consequence (PROVED, used below): if block m has a private two-sided peak resource, no coarse PEAK of m is thick-type at a stage carrying a
near-certificate (Lemma R-PK gives |zeta_m| <= (4/3) eps Design, so coef_c = -zeta_m lambda_c (1 - X_m) is tiny, against (iii)).

## 2.2 Lemma J1.6(b) (helpful far placements).  Verdict: CORRECT (modulo the cited V1 TU / K1 2.1(b) / Q2 LT / Z3 3.1 estimates).
Signs re-derived: the action is coef_k v_k(j)(tau - z_j) = kappa_y |a_p/v_k(p)| |v_k(j)| (1 - tau z_j) + O(eps Design^2 |v_k(j)|) < 0, with
1 - tau z_j >= 1 for helpful j.  Admissibility: for a data-carrying k the data sign at j is sgn(c_k v_k(j)); a far contact of the anti-data sign or
a free far coordinate cannot occur (contact row / free coordinate forces c_k = 0), so a helpful j is either a data-sign contact flipped to
anti-sign support (a V1 pull, data dominated by the mass 24 lambda_k |v_k(j)|), or anti-data-sign support with |a_j| <= x'' lowered to 0 and
replaced by data-sign (aligned) support, or (zero-data k) any state.  For a thick-type PEAK k the anti-sign case is K1 2.2's repaired peak pull.
The mass at j moves e by mu*_j m_j/nu (negligible); second-order terms <= C Design^C |v_k(j)|^2.  Under (FC)/K-8 the generator columns are
C^{1,1} in the row, so they move by <= C Design^C |v_k(j)| (a status crossing of k itself at the intermediate row R' is harmless under (FC)).

## 2.3 Theorem J1.7.  Verdict: CORRECT after precision P-TU (fixable gap in the realization bookkeeping; inherited from K2.9(c)/K1.6(A),
## amplified by the overshoot).
The contradiction argument is correct: a near-certificate at R' of size < 4u^3 Design^{-C_A} is one of size <= eps_* at R_1 + Pi (columns move by
<= C Design^C x'' << that), J1.6(a) applies, and phi'_y = phi_y + coef_k v_k(j)(tau - z_j) + err <= |Lambda_A| x - (c_*/(2nu_1)) Design^{C_J} x +
err < -rho'_0 (C_J = C_A + 4 dominates the f-constants c_1, A_min for L >= l_f; err <= C(c_{L+1} + Design^C x''^2) << x; rho'_0 = C_2 W'^2 << x
because x''^2 << x/Design^{2C_A}).  So K2.9(b)'s contrapositive gives A-regularity at R'.  The placement lowers phi_y for ALL near-certificates
simultaneously, so no new certificate appears -- this is exactly the point K2.11 left open, and J1.7 settles it for thick-type carriers.
P-TU (realization ranges; GAP in the bookkeeping, FIX PROVED).  K2.9(c)'s Brouwer domain is {t >= 0, ||t|| <= W} and every point must be an
admissible move.  A pre-placed TU lever (pull + compensating base bank, K1 2.1(b), K2-ref K-1) is two-sided only within its base bank: it can lower
eps_l val_l by at most the pull's shift D_p = (1 + eps_l z_1(j_p)) v_l(j_p) (plus theta_0 eff), and K1-ref R-6 places the pull at the SMALLEST
pullable depth v >= x, so D_p may be as small as x/2.  K2.9 uses W = Design^{C_A} u^{-3} max(x, ||b||) >> x, and J1.7 uses W' =
Design^{C_A} u^{-3} max(x, ||b'||) with ||b'|| up to ||b|| + 3x'_max (J1's FW_k reaches x'_max), i.e. W' >> x'_max >= every D_p.  So the minimal-norm
selection may ask a TU bank to go negative.  (The same remark applies to K1 Lemma K1.6(A), whose moves are ~ Design^C eta'/u >> x/2.)
FIX.  Fix two window parameters per stage: x'' with Design^{C_J} x/u <= x'' and x_TU with 24 Design^{C_A} u^{-3} (|Lambda|^{1/2} x + 3 x'') <= x_TU <=
2^{-6G(L)} x'_max.  (i) Pre-place every TU pull in [x_TU, x'_max] (pullability and the (U)-class are re-defined on this window, as K1-ref R-6
re-defined them on [x, x'_max]; costs are bounded by R-6's worst case C Design |Lambda| x'_max log(1/T)); (ii) take FW_k := {j in S_k : Design^{C_J}
x/u <= |v_k(j)| <= x''}.  Then every radius used (W, W' <= Design^{C_A} u^{-3}(|Lambda|^{1/2} x + 3x'') <= x_TU/24) is below every TU range D_p/4,
all other two-sided generators have ranges >= u/2 (TS, FR, (P3), (P4)) or are unlimited (ZD, (P1)), and K2.9(c), J1.7 and K1.6(A) hold verbatim.
Both windows are long (ratios >= 2^{6G(L)}) for any choice with, e.g., x'' := Design^{C_J + 1} x/u and x_TU := Design^{C_A + C_J + 2} u^{-4} x.  The
only effect is that the (U)-class, the helpful-coordinate notion and the residual's "frozen far window" refer to these windows.  J1's Remark (3)
(any upper end x'' <= x'_max) is thus correct only with x_TU adjusted accordingly.

## 2.4 Lemma J1.8 (band version of K2.9).  Verdict: CORRECT.
(a): Brouwer on {||t|| <= W} x Box for the joint minimal-norm selection (strictly convex objective; feasible sets Hausdorff-Lipschitz in the
right-hand side by Hoffman); a fixed point gives Ft(R') = sigma in Box (half-width beta_l/2, slightly stronger than stated).  P-TU applies.
(b): separation of b'' from the compact convex set (W/2)Q + Box, whose support function in direction -y is (W/2) max(0, max_g(-y^T g)) +
(1/2) sum_B |y_l| beta_l.  Re-derived.

## 2.5 Theorem J1.9 (one-out-of-many).  Verdict: CORRECT (as a statement about the band-relaxed system); numerical illustration flawed.
Proof re-derived: y_k = eps_k(coef_k + zeta_m lambda_k dkappa/dzeta(k)) with |zeta_m| <= C|Lambda|^{1/2}/A_min and dkappa/dzeta(k) = rho_k M X_m/C
<= C b^2 D^2 (route V; under (FC) for near-threshold k), so |y_k| >= c_* u/(8 nu_1); then phi_y > c_* u beta_k/(16 nu_1) - rho_0 >= ||b|| + rho_0
contradicts |phi_y| <= ||b||.  Whether the band is LEGITIMATE downstream is a separate question (J1.10-J1.14, part 3).
Numerics: J1's check_band numbers (29-143 vs 1.4e-4) come from a STALE generator matrix (part 1, N3).  In J1's toy with consistent generators
there is no obstruction at the displaced targets (Lemma R-PK); in the variant without a private peak resource the obstruction is genuine
(29-175 without band) and the band on the thick-type row removes it (1.6e-4): J1.9 is confirmed there.

## 2.6 Remark R-W (the A-regularity radius is a window quantity).  PROVED modulo P-TU and the cited chain.
K2.9(a)-(c) and J1.7-J1.9 use the radius W only through: moves <= W are admissible (P-TU: W <= x_TU/24), cost C_f Design^C W log(1/W) =
o(u^2 T^2), moves << u, and rho_0 = C_2 W^2.  Hence any W in [Design^{C_A} u^{-3} max(x, ||b||), min(x_TU/24, u^2 T^2/(C_f Design^C log^2(1/T)))]
is admissible, and a non-A-regular stage then carries near-certificates of size < 2(||b|| + C_2 W^2)/W.  With the largest W this is
O(Design^C x/x_TU + C_2 x_TU): obstructions are NEAR-EXACT resonances whenever the pulls of the stage sit high in their window.  Trade-off: raising
x_TU enlarges the (U)-class.  This does not change any verdict; it shows that the size threshold u^3 Design^{-C_A} of K2-ref K-7 is a
convention, and that the relations of K2.16 (proportionality, hole mass) hold with precision tending to 0 faster than any design rate along
residual stages when x_TU can be taken >= T^{-1/2} x.
