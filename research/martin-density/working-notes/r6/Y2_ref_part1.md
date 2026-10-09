# Y2 referee, part 1: Lemma T, Lemma U', Theorem E'

## Lemma T (threshold equation). Verdict: CORRECT (PROVED).
Re-derived (a)-(e) line by line.
(a) At k in P: zeta(k)/|zeta| = alpha(k) + Phi_k^2 w(k)/C with alpha(k) of the sign of w(k) or 0 and |w(k)| = M, so
|zeta(k)| = |zeta||alpha(k)| + theta Phi_k^2; off P, |zeta(k)| = |zeta| Phi_k^2 |w(k)|/C < theta Phi_k^2. Hence P = {nu >= theta},
degenerate iff nu = theta. (b) A(theta) = sum_P |zeta||alpha| = |zeta|; C^2 = sum Phi^2 w^2 = (C/|zeta|)^2 B(theta). (c) A' is
Lipschitz nonincreasing, B' Lipschitz nondecreasing, strictly monotone on (0, sup nu'), Psi'(0+) = ||zeta'||_1^2 > 0, Psi' < 0 beyond
sup nu' (or for large th when sup nu' = infinity, dominated convergence). Unique zero; it is theta(zeta') by (b).
(d), (e): the elementary bounds |(x)_+ - (y)_+| <= |x - y| and |min(th,a)^2 - min(th,b)^2| <= 2 th |a - b| (a, b >= 0) are right;
in (ii') the k'-term of B drops by Phi^2(nu^2 - nu'^2) >= nu Delta and A(theta;zeta')^2 >= A^2 - 2AE in both cases A >= E, A < E;
in (i') E < A Delta/(A+theta) < Delta is needed for (A + Delta - E)^2 - A^2 >= 2A(Delta - E), and it holds.
Independent numerical confirmation (referee scripts Y2_ref_work/lemmaT_cert.py, lemmaT_e_mp.py):
 * a PRIMAL-DUAL certificate built from the root theta alone (x_k = sgn(z_k)(|z_k| - theta Phi_k^2)_+, beta = (z - x)/Phi,
   w proportional to sgn(z) min(theta, nu)) has ||x||_1 = ||beta||_2 = <w,z> with N(w) = 1, to relative error 3e-14 on 3000 random
   blocks of size 2..30 -- this is an SOCP-free proof of (a),(b) in finite dimension (and is how one can see the lemma directly:
   the clamp decomposition is optimal for the primal and the clamped w for the dual);
 * Lemma T(e) with adversarial "lowering" perturbations of total size E = 0.999999 x (stated bound), 60-digit decimal arithmetic:
   1868 tests, 0 violations (the double-precision run showed 11 apparent ties at relative level 1e-15, all resolved in high
   precision).
Remark (useful, PROVED by the certificate): Lemma T gives the block norm and its norming functional in closed form from one scalar
root; in particular theta depends continuously on zeta in l_1 (Psi is jointly continuous and strictly decreasing through its zero).

## Lemma U' (inward coordinates, window-dependent A_2, gamma_B). Verdict: CORRECT (PROVED), with two precisions.
Checked against Lemma lem:uniformtransfer, Lemma lem:onesidedtransfer (note lines 4438-4487, 5506-5560) and Z3 Lemma U.
(i) Constant 3 / t^2/2 in kind [1]: radius gap/(2|omega|) >= t/6, so c_flat <= 1/6 suffices; correct.
(ii) Kind [3] (inward) coordinates: the block step of lem:block(d) uses the coordinatewise radius only to get
||W||_inf = (1 - rd)M (lem:block(c)); for inward coordinates varsigma W(k) <= (1 - rd)|w(k)| <= (1 - rd)M on the designated side
and varsigma W(k) >= -c_flat A_2 >= -(1-rd)M, while the maximum (1-rd)M is attained at a NON-degenerate peak (alpha != 0, which exists
because ||alpha||_1 = 1 and alpha vanishes on degenerate peaks) where omega = 0. Then (d) follows verbatim from (a),(c):
N(W) <= 1 + r^2 ||h_perp||^2/(2Y), Y >= C/2. The first-order term <omega, alpha> vanishes because alpha = 0 at degenerate peaks and
off P. The rebalancing step (Lemma lem:TV) only needs ||W - w||_inf <= 2 A_3 c_flat; inward coordinates lying in
L = {|w| >= gamma_m} keep the sign of w, so TV(a),(b) hold. CORRECT.
(iii) Dependence of constants: the constraints in lem:uniformtransfer / lem:onesidedtransfer involving A_2, gamma_B are all upper
bounds on c_flat (c_flat <= gamma_B/(2A_2), C_min/(2A_3), the O(A_3 c_flat) relative errors, ||W-w||_inf <= 2A_3c_flat <= (M - gamma)/12);
the t_1-constraints are "K_3 c_flat^2 t_1^2 (2 + Lambda) <= gamma_m/2", "K_3 c_flat^2 t_1^2 <= (M - gamma)/4" and the r^4-terms with
|r| <= c_flat t <= t/8: all MONOTONE in c_flat, hence satisfied for every smaller c_flat once imposed with c_flat = 1/8. K_3, K_y, K_Y,
eta_1, the transfer data and a_min (a_j = a in all uses) do not involve A_2, gamma_B. So t_1 and j_0 are independent of
(A_2, gamma_B); c_flat >= c_0 gamma_B/A_2 with c_0 = c_0(f, eps_tr, A_0). CORRECT.
Precision 1: the radius 1/(2|d|), C/(2|d|M) needs |d| <= ||D omega||_2 <= A_3/(2t) with A_3 >= max(3, A_2) + 2; Y2's A_3 := 2 + 2A_2
covers kind [1] with constant 3 when A_2 >= 1. Fine.
Precision 2: Lemma U' is applied in Proposition Q only to kind-[3] coordinates that are STRICT non-peaks of f_j; the degenerate-peak
case of kind [3] is also correct (above), but is not needed.

## Theorem E' (window-dependent c_flat). Verdict: CORRECT (PROVED).
In Z3's proof c_flat enters exactly through (A) (Lemma U at scale t_i), the dyadic count sum_{I_r} t_i < 2 rho|r|/c_flat, the bound
2 rho^2 K r^2/(c_flat n) <= (1-rho^2) r^2/24 and eps_j < theta_j rho^2 r^2/c_flat^2 when I_r != {} (rho|r| > c_flat t_n = 2 c_flat tau_j).
With c_flat,j these are (E-d'), (E-e'). (E-d') with K_j >= 1 forces T_j -> 0, so T_j <= t_1 eventually and 2 rho K_j T_j/n_j -> 0.
The averaging step and Corollary cor:D1 at f_j do not involve c_flat. CORRECT. (The same remark as in Z3: any sub-window is allowed.)
