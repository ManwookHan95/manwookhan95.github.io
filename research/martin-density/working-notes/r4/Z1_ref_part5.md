# Z1 referee, part 5: Z1 part 5 (the "common-functional obstruction") -- it is an artefact; Hoffman matching

Setting of Z1 part 5: SLD T, p = p_N, f with F finite, a finite slaving-closed set U* of free carriers, (SR) for every l notin U*, and
(E1) every l in U* is a strict non-peak; (E2) supp u_l \ F subset K (contacts) for l in U*. K_* := union_{U*} supp u_l \ F. Window scale t in W(l_*),
K := K_1 Lambda*_f(l_*) (pinning constant of the carriers outside U*). Two-sided decomposition (B_+-, Omega_+-) of g at scale t, u-coefficients
c^+-_l (L*Omega = sum_l c_l u_l), Delta c := c^+ - c^-, Delta B = B_+ - B_- = -sum_l Delta c_l u_l.

## 5.1 Z1 5.1 (window split). Verdict: SKETCH, as labelled; two omissions.
(a) The O(t) WRONG-SIGNED contact mass of B_+- on K_* (allowed by the budget, G3 2.3(b): sum_{j notin F} [(z_j B_+(j))_- + (z_j B_-(j))_+] <= t/(2 q_0))
    is not mentioned. It is unstructured junk of size O(t) on K_*, in addition to Z1's J_t.
(b) The d-coefficients. At a finitely swallowed point G3 3.5(c) has an extra term (Phi_k/(m C)) sum_{U*} |Delta c_l| = O(1), so |Delta d_m| = O(K t) is
    NOT automatic. It does hold, by the first-order identity in 5.3(2)(ii) below. Z1 hides this in "normalisation terms".

## 5.2 Z1 5.2. Verdict: the algebra is right inside Z1's model, but the conclusion is WRONG. Z1 FIXES the + component's functional as
## Phi_t = g - Rem_+(t). The averaging (G3 5.2) only needs some functional Psi_t with ||g - Psi_t|| = O(K t) and two exact one-sided decompositions.
Z1's criterion is "J_t can be cancelled exactly iff -J_t (mod span{u_l 1_{K_*}}) lies in the z-cone". It allows only z-signed ADDITIONS to the + side.
It misses the possibility of REDUCING the + side's contact base. The base V stays z-signed as long as z_j V(j) is in [0, z_j B_+(j)], and the change
can be put into the O(K t) remainder exactly like Rem_+. Example (one coordinate, z = 1). Take B_+ = 1 + eps - beta, B_- = -beta (0 <= beta < eps),
sigma := -Delta c u = 1, J = eps. Z1's test fails: B_- + J = eps - beta > 0. Matching still works with V = 1 and W = 0: trim P = eps - beta.

## 5.3 Proposition (Hoffman matching; referee). Steps (1)-(4) PROVED, (5)-(6) SKETCH.
In the setting above, for all late window scales t there is ONE functional Psi_t with ||g - Psi_t||_{p*} <= C_f K t. It carries exact, balanced,
d-NEUTRAL two-piece data in the sense of P2A 1.6: (b^+, omega^+), (b^-, omega^-), supp b^+- subset F cup K_*, z_j b^+(j) >= 0 >= z_j b^-(j) on K_*, and
omega^+- finitely supported off the peaks. Each side is an O(K t)-perturbation of the actual decomposition on that side.
(1) The cone. For xi in R^{U*} put v_xi := sum_{U*} xi_l u_l 1_{K_*} and
      R_0 := {xi : z_j v_xi(j) >= 0 for all j in K_*, and sum_{l in U*, m(l) = m} xi_l u_l(xi) = 0 for all m}.
    R_0 is a POLYHEDRAL cone. Put G_0 := union_{U*} supp y_l (finite). At j in S_l \ G_0 (l in U*), the only free vector that is nonzero is u_l's signature
    delta_l 2^{-j}/n_l > 0, because the S_l are disjoint and targets are finitely supported. So the constraint there is z_j xi_l >= 0. This gives one
    constraint eps_l xi_l >= 0 if z = eps_l is constant on S_l \ G_0, or xi_l = 0 if z takes both signs there. Add finitely many constraints at
    G_0 cap K_* and N equations.
(2) The actual switching xi° := -Delta c|_{U*} violates every constraint by O(K t + t).
    (i) Slaving-closedness gives that pinned signatures never meet K_*. So Delta B 1_{K_*} = v_{xi°} + J_t with
        J_t := -sum_{l notin U*} Delta c_l u_l 1_{K_*}, and ||J_t||_1 <= (4/3) sum_{l notin U*} |Delta c_l| <= (4/3) K t.
        Also z_j Delta B(j) >= -[(z_j B_+(j))_- + (z_j B_-(j))_+].
        Summing over S_l \ G_0: (eps_l Delta c_l)_+ delta_l ||h_l 1_{S_l \ G_0}||/n_l <= (4/3) K t + t/(2 q_0). The mixed-sign case and the
        constraints at G_0 are handled the same way.
    (ii) d-neutrality. sum_k Delta c_k u_k(xi) = <Delta Omega_m, zeta_m>, since zeta_m(k) = lambda_k u_k(xi). This lies in [-t, t] by G3 2.3(a).
        The pinned part is <= q_0 sum_{l notin U*} |Delta c_l|. Hence |sum_{U*, m(l)=m} Delta c_l u_l(xi)| <= t + q_0 K t.
        (For a strict non-peak, u_k(xi) = sigma_m Phi_k w(k)/(C m) and d(e_k) = Phi_k^2 w(k)/C. So this is exactly Delta d of the free part, and the
        same bound gives |Delta d_m| = O(K t) in G3 3.5(c) at finitely swallowed points.)
(3) Hoffman's lemma for the polyhedral cone R_0 (finitely many constraint normals fixed by f and U*) gives xi_t in R_0 with |xi_t - xi°| <= H (K t + t).
(4) Trimming. Let B^cl_+ be the z-signed part of B_+ on K_*. Put z_j P(j) := (z_j (B^cl_+(j) - v_{xi_t}(j)))_+, V := B^cl_+ - P and W := V - v_{xi_t}.
    Then V is z-signed, and W is (-z)-signed because z_j v_{xi_t}(j) >= 0.
    ||P||_1 <= sum_j (z_j B_-(j))_+ + ||B_+ 1_{K_*} - B^cl_+||_1 + ||J_t||_1 + ||v_{xi_t} - v_{xi°}||_1 = O(K t),
    using v_{xi°} = Delta B 1_{K_*} - J_t = (B_+ - B_-) 1_{K_*} - J_t.
(5) The two sides (SKETCH).
    + side: omega^+ := the G3 block data built from omega_+, clamped at 2 gap/t on pinned coarse non-peaks, 0 on peaks and fine coordinates,
        UNCLAMPED on the free carriers (one-sided use needs no clamp).
        b^+ := B_+ 1_F + V - kappa a, with kappa := (B_+ 1_F + V)(zhat) = B_+(zhat) - (B_+ 1_{F^c \ K_*})(zhat) + (V - B_+ 1_{K_*})(zhat) = O(K t).
        Psi_t := b^+ + sum_m R_m*(omega^+_m - d(omega^+_m) w_m).
    - side: omega^- := omega^+ + sum_{U*} (xi_{t,l}/lambda_l) e_{k(l)} and b^- := b^+ - sum_{U*} xi_{t,l} u_l, so that b^- 1_{K_*} = W.
        Since Delta d(xi_t) = 0, b^- + sum R*(omega^- - d(omega^-) w) = Psi_t exactly. By (E2), supp b^+- subset F cup K_*.
    ||g - Psi_t|| = O(K t). This uses G3 4.2(c) for the pinned part (it needs |Delta d| = O(K t), see (2)(ii)), base mass off F cup K_* being
    O(K t + t), and ||B_+ 1_{K_*} - V|| = O(K t).
(6) Validity (SKETCH). Each side differs from the actual decomposition on that side by O(K t): in l_1 for the base, and in sum lambda_k |.| for the
    blocks. On the free carriers, omega^-(k_l) - omega_-(k_l) = (xi_{t,l} + Delta c_l)/lambda_l + Delta d w(k_l) = O(K t). So Gamma_w <= 1 + eta_0/2 on late
    windows, by the seminorm argument of G3 4.2(d). The one-sided version of 5.1 holds:
     * no kinks on K_* (signs);
     * no flips on F (F finite, bases bounded);
     * pinned data in (C-b);
     * free carriers inside the box at every s <= t, because the box condition is convex in s and holds at s = t. Step 3(iv) of 5.1 needs a
       one-line change for coordinates moved AWAY from the peak level by up to (2M - gap)/t: |s omega| <= c_1(2M - gap) <= M/2 for c_1 <= 1/4.

## 5.4 Theorem M (referee; SKETCH). Finitely swallowed points with exact free resources are recoverable.
For the SLD T and every N, let f in S_{p_N*} have F finite, and let U* be a finite slaving-closed set such that (SR) holds for all l notin U* and
(E1), (E2) hold for l in U*. Then f is in R.
Proof (sketch).
(1) 5.3 on every late window gives Psi_{t_i} for the n dyadic window scales.
(2) G3 5.2 (use the + side for s > 0 and the - side for s < 0; conditions (i)-(iii) hold) gives rho Psi in C(f) with Psi := avg_i Psi_{t_i}.
(3) Psi carries exact d-neutral two-piece data: the averages of the sides. This works because the sign cones are convex, d is linear and Gamma_w is
    convex, so kappa_w(Psi) <= 1 + eta_0.
(4) S3 Cor D1 (F finite, Delta d = 0 >= 0, kappa_w(rho Psi) <= rho^2(1 + eta_0) <= 1; refereed) gives rho Psi in Ls(f).
(5) ||Psi - g|| <= 2 K t_1/n -> 0 along the windows, and Ls(f) is closed under norm limits in this sense. So g is in Ls(f).
Toy check of steps (1)-(4) of 5.3 (Z1ref_work/hm2.py; 3 free carriers, an O(1) exact resonance, junk and wrong-signed mass of size eps):
|xi_t - xi°|/eps <= 5.1, ||P||/eps <= 4.3, all signs exact, for eps = 1e-2 ... 1e-5.
Consequences for Z1:
 * The "common-functional obstruction" (Z1 5.2, table #15) and the remaining step (RS1) are resolved in the exact-resource case (SKETCH).
 * What remains of (RS1) is Z1's (O-a): near-resources on swallowed sets. These are near-contacts (E2 fails), free carriers that are peaks, weak
   or near-threshold (E1 fails), and inexact contacts with |z_j| < 1 inside swallowed signature sets. That is the genuinely scale-dependent part (O3).
 * (A) "R_fin subset R" is reduced to the near-resource case. (B) (lower semicontinuity along f^L) is untouched.

## 5.5 Remarks on the scope of Theorem M.
 (a) Extension (SKETCH, same proof). (E2) may be weakened to (E2'): for l in U*, the set supp u_l \ (F cup K) is FINITE. Examples are finitely many
     coordinates j notin F with |z_j| < 1. At such j the budget (G3 2.3(b)) bounds the base mass of each side by t/(2 q_0 (1 - |z_j|)), so the
     switching vanishes there up to O(t) (constant depending on the finitely many j). Add the
     finitely many equations sum_{U*} xi_l u_l(j) = 0 (no sign condition at these j); R_0 stays polyhedral, and the components put no base
     there (trim B_+(j) = O(t)).
     Slaving can then use kappa^room_{l',l} := ||y_{l'} 1_{S_l cap J_gamma}||_1/n_{l'}. If S_l cap J_gamma is infinite, a free target touching it pins
     the free carrier: |Delta c_l| = O(t) from the roomy tail, and then Delta c_{l'} = O(t) at the touched roomy coordinate.
 (b) What is NOT covered is infinitely many INEXACT one-sided coordinates in the free supports, e.g. near-contacts with |z_j| -> 1 along a
     swallowed S_l. The obstruction there is not the cone geometry: on S_l all constraints still read z_j xi_l >= 0. The obstruction is
     inexactness. Base mass at a near-contact costs (1 - |z_j|)|s| at first order, so a component that uses it has Delta1 > 0 (ray lemma 2.4(b)).
     It is not in P2A 1.6's format (exact signs on K), and trimming all such mass forces xi_l = 0. Yet the actual switching may use O(1) mass
     there at each scale, because the cost is only (1 - |z_j|) t per unit. This is the genuine scale-dependent switching (O3), now localised to
     the near-contact tails of finitely many signature sets (Z1's (O-a)).
     A possible route, not attempted here: approximants f' that RAISE the near-contacts of the swallowed sets to exact contacts
     (z'_j := sign z_j where 1 - |z_j| < eps). Then z' -> z uniformly on those sets, so f' -> f, and f' satisfies (E2). This leaves the usual
     transfer band problem.
