# P1 referee — part 1 (reading log and first verifications)

Setting used by me: canonical base q, finite block set I (p_N), as in P1. Imports: A_notes Facts A-F, Lemmas 4.3/4.4/7.1/7.2
(refereed), (T4) strict convexity of p** (Preprint B).

## Verified line by line so far (re-derived by hand)
* 2.1 construction of T: (T-a) norm one (||T|| = sup_l c_l = c_1 = 1); (T-d) density (u_{n,m} - y^{(i(n,m))} -> 0 because
  rho_l, delta_l -> 0, n_l -> 1; every i allowed at all large l); (T-b),(T-c) via the signature coordinates S_{l'}:
  |Z(s)| >= c_{l'} delta_{l'} 2^{-s}(|x_{l'}|/n_{l'} - (8/3)||x||_inf 2^{-s}) (uses sum_{l>=L} c_l <= 2 c_L, |y_l(s)| <= 1, n_l >= 3/4,
  allowedness at L(s)). (P1) kappa > 0 since |<U*h,e>| <= ||h||_1/2 on J_0; u^0(zhat) = 0 exact. (P2) |u_{1,m}(zhat)| >= 7/9.
  (P3) non-exceptional |u(zhat)| >= 2 rho_l > pi; exceptional >= 31/33. All CORRECT.
  (T3) (R_m** injective) is not listed but follows from (T-d) (span of each block dense in l_1). (T4) imported.
* 2.2: f in S_{p*}, unique normer xi = zhat/p**(zhat), forced data (a, w), z = e_1 + 1_{K'}; (1,m) peaks via (P2) and
  |zeta_m| <= q_0 m 2^{-m}; all (k,m) != (2,1) peaks via theta_m Phi_m(k) <= q_0 pi_{k,m} < |u_{k,m}(xi)|; (2,1) strict non-peak with
  w_1(2) = 0. CORRECT.
* 2.3 two-piece mates: side + and side - decompositions re-derived; first-order terms vanish exactly
  (side +: ||v1_{K1}||_1 + <e,h_1> = beta; side -: bracket = v(zhat) = 0); Hilbert bound ||xe+y|| <= x + <e,y> + ||y||^2/(2x)
  (valid for x > 0, all y: (<e,h> + ||h||^2/2)^2 >= 0); block: N_1 = M_1 + sqrt(C_1^2 + s^2 c^2); crude bound for |t| >= 1.
  CORRECT (constants slightly wasteful).
* 2.4: S(f) = R u (F = {1}, zhat_1 != 0, Q_1 = {2}, y_{2,1} = lambda_0 u). g_{K1} = mu u forces c 1_{K1} = mu on K'. CORRECT.
* 3.1 (B1)-(B3),(K1)-(K3): direct from A Lemmas 7.1/7.2, Psi lower bound. CORRECT. (|alpha_k| = lambda_k mu_k/|zeta| re-derived.)
* 3.4 transfer identity: CORRECT (averaging of the +-t decompositions).
* 3.5 (a)-(c) and the peak identity (b): CORRECT. (d) needs care (level shift ell - M can be O(t), not O(eps)).
* 4.1 exact resonances: CORRECT.
* 4.2 sign rule: CORRECT (tautological parametrization |u(xi)| = (1-gamma) theta Phi off P).
* 4.3 weighted averaging: re-derived all inequalities: CORRECT.
* 4.4: CORRECT (no scale-density needed; geometric decay of gamma_i lambda_i).
* 5.1, 5.2, 5.3: CORRECT (Mazur; support function of intersections; one-scale minimum sqrt(P^2-F^2); x_* computation).
* 6.0 margins, 6.1 (C(f) in E_u) steps (1)-(6), 6.2 slab: CORRECT.
* 6.3: plausible SKETCH; missing hypothesis "g in C(f)" (needed for the slack regime); partial-pull coordinate j* has a
  first-order cost that must be put beyond the tail threshold; otherwise consistent.
