# V3 referee, part 2: design D^mu, raise room (RR), Lemma VP; numerics

## Design D^mu. CORRECT.
thm:SLD's proof of (T-a)-(T-d), (P1)-(P3) uses U only through q* being a norm with q* <= (1+||U||)||.||_1 (normalisations
n_l = q*(y_l + delta_l h_l), targets in S_{q*}, delta_l via ||U||). Any compact injective-adjoint U is allowed by the problem
set-up (q*(a) = ||a||_1 + ||U*a||, q smooth iff U* injective iff U has dense range). Diagonal U k_s = mu_s e_s, mu_s -> 0, mu_s > 0:
compact, dense range (contains c_00), U*e_s* = mu_s k_s. D_sigma's (D0'), (D1)(c) do not involve U. N-free: nothing depends on N.
Caveat (not an error): with mu_s = 2^{-s^2-1}, nu = ||U*a|| can be astronomically small for some f; every constant that involves
1/nu (h(B), Lemma 2.1(b), Psi-bounds) is an f-constant, so this only affects rates, never the order of quantifiers.

## Lemma 3.1 (RR). CORRECT. (a) and (b) re-derived. ||U*Da|| <= sum mu_s|Da_s| <= y M_mu^W(y) (|Da_s| <= y W_s on the active set).
The converse gloss "(RR) fails only for mu-thin supports" is a heuristic description, not used.

## Lemma VP. CORRECT WITH A FIXABLE GAP in the statement of (ND_{L_0}).
Derivative: DG(0)xi = Lambda(xi)/nu re-derived (diagonal U: <U*u, U*x> = sum mu_s^2 u_s x_s, <U*x, e> = sum mu_s^2 a_s x_s/nu);
Graves/Newton on the finite-dimensional l_1(F_0); |G(0)| <= 2||U||^2||U*Da||/nu... (2||U|| ||U*Da||/nu suffices). OK.
GAP. For a diagonal base, u(zhat^#) - u(zhat) = <U*u, e^# - e> = sum_{s in F} mu_s^2 u_s (a^#_s/||U*a^#|| - a_s/nu) depends only on
u|_F. If some k in L_0 has u_k|_F = 0 (e.g. a contact-swallowed bad carrier l in B_K whose signature set and target avoid F), then
gamma_k = 0 and the k-th row of Lambda vanishes identically: (ND_{L_0}) FAILS, although the value of u_k is preserved automatically
by every move on F. Likewise two carriers with equal restrictions to F. So Theorem RS as stated excludes harmless configurations.
FIX (PROVED). Replace (ND_{L_0}) by
  (ND'_{L_0})  a|_F does not belong to span{u_k|_F : k in L_0}.
Proof that VP holds under (ND'): put V_0 := {c in R^{L_0} : (sum c_k u_k)|_F = 0}. For c in V_0 and any x supported in F,
<U*u_c, U*x> = sum mu_s^2 u_c(s) x_s = 0, hence c.G(x) = <U*u_c, e(x) - e> = 0: G takes values in V_0^perp. The annihilator of
Lambda(l_1(F)) is {c : u_c|_F = kappa a|_F for some kappa} (computation of the adjoint, using <U*u_c, U*a> = kappa nu^2 when
u_c|_F = kappa a|_F); under (ND') this is V_0, so Lambda maps l_1(F) (and some finite l_1(F_0)) ONTO V_0^perp. Apply the
quantitative implicit function theorem to G : l_1(F_0) -> V_0^perp. Everything else is unchanged. (ND') is equivalent to the
remark's characterisation with "kappa != 0".
Numerics (V3_ref_work/vp_check.py): derivative formula confirmed to 6 digits; Newton on F_0 (5 coordinates) restores three values
to 1e-17 with ||Da''||_1/||U*Da|| ~ 0.40 for y = 1e-1..1e-3, signs on F kept; a carrier vanishing on F has a zero Lambda-row and an
exactly zero value shift.
Remark 3.3 (second-order drift kappa nu ||e^# - e||^2/2 when (ND') fails): re-derived (<e, e^#> - 1 = -||e^# - e||^2/2). CORRECT.

## Numerics for (RT) (V3_ref_work/rt_indep.py, independent implementation, seeds 7 and 11). Evidence only.
12 base coordinates, 2 blocks x 5, diagonal mu_j = 0.5 * 0.45^{j^1.25}; rows from forced data (p*(f) = 1 asserted);
raises of l_1-mass up to 2.3 (lam up to 3.33), with and without an arbitrary-sign correction on F_0 (|Da''| <= |a|/2);
r in {1, 0.3, 0.05, 0.01}, random h: max(LHS - RHS) = -1.7e-4 / -4.2e-4 (never violated); Corollary 2.4 with a numerically
certified mate g (p*(f + t g) <= s(t) on a 50-point grid), rho in {1, 0.8}: never violated. p*(f^# - f) up to 1.14 while
2||U*Da|| + p*(L*(w^# - w)) <= 2.8e-2. Side remark on V3's script: its helper block_norm computes the gauge of conv(B_1 u D B_2)
(inf ||alpha||_1 + ||beta||_2), not of B_1 + D B_2; it only feeds q_0, which does not enter f (w_m = J_m(zeta_m) is
0-homogeneous), so V3's reported numbers are unaffected.
