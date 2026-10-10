# V3 part 4: fixed data without cushion sparsity; master theorem at infinite F; what remains; numerics

## 4.1 Theorem A (fixed d-neutral data at infinite F without cushion sparsity). PROVED.
T admissible over the base D^mu (3.1), I finite, f in S_{p*} (F arbitrary), g in C(f) with d-neutral two-piece data (b^pm, omega^pm) at f
(Definition def:twopiece read at arbitrary F; omega^pm_m finitely supported in Q_m), rho^2 kappa_w < 1. Put W := (s b^+)_- + (s b^-)_+ + |b^theta|
on F (0 off F), L_0 := union_m (supp omega^+_m u supp omega^-_m) (as carriers). If (RR_W) and (ND_{L_0}) hold, then (f, rho g) in cl NA.
[Y3 Theorem 2.1 needs (CS-side): m_{(sb^+)_-}(x), m_{(sb^-)_+}(x) = o(x); here no cushion condition at all is imposed.]
Proof. For y -> 0 let f_y be the raise of f along W at level y followed by the Lemma VP correction for L_0; T := y/4.
(1) d-neutrality and consistency at f_y. For a strict non-peak k, w_m(k) = C_m zeta_m(k)/(Phi_m(k)^2 sigma_m) and zeta_m(k) = m Phi_m(k) q_0 val_k
(Lemma lem:threshold), so for omega supported in L_0 cap Q_m: d_m(omega) = (m q_0/sigma_m) sum_k Phi_m(k) val_k omega(k). The values val_k
(k in L_0) are the same at f_y, the gaps of L_0 are f-constants, so L_0 stays in Q^{(y)}_m and d^{(y)}_m(omega) = (q_0^{(y)} sigma_m/(q_0 sigma^{(y)}_m))
d_m(omega): the data are d-neutral at f_y. Hence b^+ - b^- = sum_m R_m*(omega^-_m - omega^+_m) is the two-piece consistency relation at BOTH
rows, and (b^pm, omega^pm) represent one functional G_y := b^+ + sum_m R_m*(omega^+_m - d^{(y)}_m(omega^+_m) w^{(y)}_m) at f_y. Replace b^pm by
b^pm - kappa_y a^{(y)} with kappa_y := G_y(xi_y)/q_0^{(y)} (lem:algebra), so that the data represent g_y := G_y - kappa_y a^{(y)} with
b(xi_y) = 0. Side admissibility is unchanged (same F, K, J, z; a^{(y)} lives on F). p*(g - g_y) = O(eps_e) (Lemma 2.2, |d^{(y)} - d| = O(eps_e)).
(2) Cushions at f_y: (s b^+)_- <= W <= lambda|a^{(y)}|/y <= 3|a^{(y)}|/t for t <= T, likewise (s b^-)_+; so Lemma R2 at f_y (U_* = 0) gives
p*(f_y + r g_y) <= 1 + (r^2/2)(Gamma^{(y)}_w(b^+, omega^+) + eps_tr) for 0 < r <= c_flat T, and the - side for -c_flat T <= r < 0, with c_flat, t_1
uniform in y; Gamma^{(y)}_w -> Gamma_w (q_0, nu, e, sigma_m, C_m and P^perp move by O(eps_e)).
(3) Mate at f_y. Fix rho_1 in (rho, 1) with rho_1^2 kappa_w < 1. For 0 < rho_1|r| <= c_flat T: p*(f_y + r rho_1 g_y) <= 1 + (rho_1^2 r^2/2)(kappa_w + 2eps_tr)
<= s(r) for small T. For rho_1|r| > c_flat T: by Corollary 2.4, p*(f_y + r rho_1 g_y) <= 1 + (s(lambda rho_1 r) - 1)/lambda + eps'_y + rho_1|r| p*(g - g_y),
and eps'_y = O(y^{2+eps} log(1/y)) = o(T^2), lambda - 1 = O(y): <= s(r) for small y (Lemma lem:slack(a), as in the proof of Theorem 2.5). So
rho_1 g_y in C(f_y).
(4) Y3 Theorem 2.1 at f_y for the mate rho_1 g_y with data rho_1(b^pm, omega^pm) (CS-side at f_y by (2); I_- empty) and the factor rho/rho_1:
(f_y, rho g_y) in cl NA. As y -> 0, (f_y, rho g_y) -> (f, rho g) (Lemma 2.1(d)). QED
Remark. For non-d-neutral data the consistency vector sum_m Delta d_m R_m* w_m changes to sum_m Delta d^{(y)}_m R_m* w^{(y)}_m at f_y; the
difference is O(eps_e) but has full support, so exactness off F is lost; and Theorem 2.1 at f_y would need (SC) AT f_y for the blocks with
Delta d < 0, which is not inherited from f in general (Scr_m is sensitive at scales ~ eps_e). OPEN in this generality.

## 4.2 Corollary (truncation is never the obstruction; (LSC-trunc)). PROVED.
Under D^mu, (LSC-trunc) [for all f, g in C(f), rho < 1, eps > 0 there is f' with finite base support, p*(f' - f) < eps, dist(rho g, C(f')) < eps]
holds for every (f, g) with d-neutral two-piece data satisfying rho^2 kappa_w < 1, (RR_W), (ND_{L_0}) (Theorem A: the NA approximants of
Y3 Theorem 2.1 at f_y have finite base support), and for every f of Theorem RS (all mates).

## 4.3 Master principle at infinite F (item (3) of the task)
Theorem M_inf (PROVED as a reduction). Let T be admissible over D^mu, I finite, f in S_{p*} (F arbitrary), g in C(f), rho in (0,1). Suppose that
for windows (T_j, n_j, K_j) with K_j T_j -> 0 and n_j >= 48 rho^2 K_j/(c_flat(1 - rho^2)) there are first rows f^ex_j with p*(f^ex_j - f) <= theta_j (T_j 2^{-n_j})^2
(e.g. f^ex_j = f, or exactifying companions of Y1/Y2/Y4 at clean sub-windows) and, at the RAISED rows f_j := raise of f^ex_j along a weight W_j at
level y_j ~ T_j with (RR)-cost eps'_j = o((T_j 2^{-n_j})^2), exact two-piece window data at f_j (pieces g_{j,t}, t in S_j) such that
(i) each piece is valid at f_j for 0 < |r| <= c_flat t (Lemma R2 at f_j with U_* = 0; this holds as soon as the support usage of the data is
<= C|a^{(j)}|/t on F, which is what the raise provides), (ii) p*(g - g_{j,t}) <= K_j t, Gamma_w <= 1 + eta_0/2, (iii) the averaged data are
d-neutral (or have Delta d >= 0 / (SC) at f_j). Then (f, rho g) in cl NA.
Proof. Lemma 2.3 applied at f^ex_j (whose decompositions of g carry the extra zeroth-order error p*(f^ex_j - f)) gives (a) of Theorem 2.5 with
eps'_j + p*(f^ex_j - f); (b)-(e) are the hypotheses (with Y3 Theorem 2.1 at f_j for (e)). QED
Consequence (SKETCH, by inspection): every finite-F window theorem whose data construction uses F only through "no flips on the support"
(a_min > 0) and the cone of exact switchings -- Theorem S, R1, Z4 Theorem A, Y1 Master Theorem (D_X), Y2 Theorem Y -- extends to infinite F
under (B_fin), (RR_B), (ND_B), (H3'): at the raised row the support usage is cushion-dominated at all window scales, so (i) holds, and
support-swallowed carriers (S_l subset F up to finitely many points) enter the cone with unconstrained sign rows exactly as in R1 Step 2
(their d-rows and target rows are the f-rows by Lemma VP). Not written line by line for Y1/Y2 (their design-level Hoffman constants must
include the patterns with support-swallowed carriers: a finite enlargement of the pattern set per level).

## 4.4 (O4-box): what raises do and do not give. HEURISTIC/SKETCH.
With infinitely many bad carriers the switching on F at scale t is box-size, |X_j| <~ Bx_{B cap U(t)}(j)/t (Z4 Theorem A, Y3 Claim 5.2).
Making it cushion-compatible needs |a^#_j| >~ Bx_{B cap U(t)}(j): a SCALE-FREE raise of mass sum{Bx(j) : |a_j| < C Bx(j)}, which does not tend to 0.
Raises therefore help only on the deep part (j > N, mass sum_{j > N} Bx(j) -> 0, cost mu-suppressed): box domination (BD_B) is needed only on
F cap [1, N(T)] with a constant C_a(N(T)) that may grow with the window depth as long as the window constants (c_flat ~ 1/C_a, n ~ C_a K)
keep eps' = o((T 2^{-n})^2); for mu_s = 2^{-s^2} this allows max_{j <= N} Bx(j)/|a_j| = o(N^2) (thin but not mu-thin support). The remaining
step is the inheritance of (SC_I) (Theorem N's data are not d-neutral) at the raised rows; OPEN.

## 4.5 What remains of item (E) after V3
 (E1) mu-thin support: (RR) fails, i.e. |a_s| below a power of mu_s on infinitely many coordinates used by the data (for mu_s = 2^{-s^2}:
      log(1/|a_s|) >~ s^2). There raises are not cheap; the switching is strongly pinned there (super-critical), so Y3 Theorem 3.5 (d-neutral,
      supp u_l subset F, monochromatic, (QM)) covers part of it; general case OPEN.
 (E2) (O4-box): infinitely many bad carriers with box-size switching on thin shallow support (4.4).
 (E3) non-d-neutral fixed data / (SC) at raised rows (4.1 Remark).
 (E4) degenerate cases (ND fails; bad carriers at degenerate peaks: (H3-inf) instead of (H3')) -- SKETCH-level repairs indicated.
 (E5) the finite-F consensus core (A)-(D) of ADDENDUM 6 (now transported to infinite F by 4.3).
(O4-crit) and the support-swallowing part of (O4-nd) (non-d-neutral carriers, off-F or shared targets, absorbing contacts) are RESOLVED for the
designed norm (Theorem RS), under (W*), (H2), (H3'), (B_fin), (ND_B), (RR_B).

## 4.6 Numerics (V3_work/rt_check.py). Evidence only.
Finite SOCP model (n = 14 base coordinates, 2 blocks x 6 coordinates, random carriers with q*(u) = 1, diagonal base mu_j = 0.5^{1 + j^1.3}...;
first rows from forced data as in Remark rem:lemmaZ(c); p* computed exactly by CLARABEL). p*(f) = 1.000000 in every trial (forced-data
construction correct). Raising the three deepest support coordinates by l_1-mass 0.12-0.18 gives p*(f^# - f) = 0.19-0.27, while the transfer
error eps' = 2||U*Delta a|| + p*(L*(w^# - w)) = 1.7e-4 - 2.6e-4 (three orders of magnitude smaller). Inequality (RT) checked for 24 random
(h, r), r in {0.3, 0.1, 0.03, 0.01}: never violated (min slack 1.4e-4 ~ 2||U*Delta a||, so the bound is tight up to the Hilbert term).
