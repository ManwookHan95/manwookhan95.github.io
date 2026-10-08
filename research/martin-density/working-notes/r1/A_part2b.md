### 4.5 Shifted certificates: the coefficient condition H(c) <= 1 is not sharp

Since f = a + L*w, for any lambda we may rewrite f = lambda(a + L*w) - (lambda - 1) f. Taking lambda = 1 + theta tau^2 moves an amount of
order tau^2 of "first-order mass" between the base and the blocks. This changes the second-order coefficients.

**Definition 4.15.** A *shifted certificate* is c = (b, omega, theta) where (b, omega) is a finite certificate and theta = (theta_m) is a
finitely supported real family. Put v_theta := sum_m theta_m R_m* w_m (in l_1) and
  kappa_q(v) := sum_{j not in supp a} ( |v_j| + z_j v_j )  in [0, 2||v||_1]   (a "kink cost": zero iff v_j = -|v_j| z_j off supp a, which needs |z_j| = 1 where v_j != 0),
  H^sh(c) := max( h(b) - 2 sum_m theta_m |zeta_m|_m / q_0 + 2 kappa_q(v_theta),  max_m ( H_m(omega_m) + 2 theta_m ) ).
(Note v_theta(zhat) = sum_m theta_m <w_m, zeta_m>/q_0 = sum_m theta_m |zeta_m|/q_0.) The direction is unchanged: g_c := b + sum_m R_m*(omega_m - d_m w_m).
The associated decomposition is
  A(tau) := a + tau b - tau^2 v_theta,   W_m(tau) := (1 + theta_m tau^2) w_m + tau (omega_m - d_m w_m),   A(tau) + sum_m R_m* W_m(tau) = f + tau g_c.
Scaling: rho.c := (rho b, rho omega, rho^2 theta) has g_{rho.c} = rho g_c and H^sh(rho.c) = rho^2 H^sh(c). H^sh is convex in (b, omega, theta), and
Cert^sh(f) := { g_c in C(f) : c shifted certificate with H^sh(c) <= 1 } is convex, symmetric, and contains Cert(f) (theta = 0).

**Proposition 4.16 (shifted expansion). PROVED.** For a shifted certificate c at f there is eps_c(tau) -> 0 (tau -> 0) with
  p*(f + tau g_c) <= 1 + (tau^2/2)( H^sh(c) + eps_c(tau) ).
*Proof.* Blocks: W_m(tau) = (1 + theta_m tau^2)[w_m + tau'(omega_m - d_m w_m)] with tau' := tau/(1 + theta_m tau^2), so by Lemma 4.4(d)
N_m(W_m(tau)) <= (1 + theta_m tau^2)(1 + (tau'^2/2) H_m (1 + kappa |tau'|)) = 1 + tau^2(theta_m + H_m/2) + O(|tau|^3).
Base: apply the identity of Lemma 7.2 with t = tau, B = b - tau v_theta (B(zhat) = -tau v_theta(zhat), and tau B_j = -tau^2 v_j off supp a):
q*(A(tau)) = 1 - tau^2 v(zhat) + tau^2 kappa_q(v) + Fl_{b - tau v}(tau) + nu Psi(tau U*(b - tau v)/nu), v = v_theta.
For |tau| <= 1/(2||b/a||), each flip term is <= 2(tau^2 |v_j| - |a_j|/2)_+, so Fl <= 2 tau^2 sum_{j in supp a, |v_j| > |a_j|/(2 tau^2)} |v_j| = o(tau^2)
(dominated convergence; it vanishes for small tau if a is in c_00). The Hilbert term is (tau^2/2) h(b - tau v)(1 + O(tau)) = (tau^2/2)(h(b) + O(tau)).
Combine with Fact A. QED.

**Theorem 4.17 (shifted transport). PROVED.** Let f_n -> f in S_{p*} (arbitrary), c = (b, omega, theta) a shifted certificate at f, and
c_n := (b_n, omega, theta) with b_n as in Theorem 4.10. For every eta > 0 there are tau_eta > 0 and n_eta such that for n >= n_eta and
|tau| <= tau_eta:  p*(f_n + tau g_{c_n}) <= 1 + (tau^2/2)(H^sh(c) + eta). Moreover limsup_n H^sh_n(c_n) <= H^sh(c) (H^sh_n computed at f_n).
Consequently, if g_c is in C(f) and H^sh(c) <= 1, then for every rho < 1, rho g_{c_n} = g_{rho.c_n} lies in Cert^sh(f_n) for n large; hence
cl Cert^sh(f) is contained in Li_n cl Cert^sh(f_n), which is contained in Li_n C(f_n), for EVERY sequence f_n -> f.

*Proof.* Blocks: exactly as in Proposition 4.16, with the uniform bounds of Theorem 4.10 for (d_{n,m}, H_{n,m}, kappa, radii).
Base at f_n, with v_n := sum theta_m R_m* w_{n,m} (-> v_theta in l_1) and the identity of Lemma 7.2 at f_n:
q*(a_n + tau b_n - tau^2 v_n) = 1 - tau^2 v_n(zhat_n) + Fl^{(n)}(tau) + tau^2 kappa_{q,n}(v_n) + nu_n Psi_n(...),
where kappa_{q,n} uses supp a_n and z_n. For |tau| <= 1/(2||b_n/a_n||) we have |tau b_n(j)| <= |a_n(j)|/2, and each flip term is
 (I) for j in G_n (so |a_n(j)| >= |a_j|/2): <= 2 tau^2 |v_{n,j}| 1[ |v_{n,j}| > |a_j|/(4 tau^2) ];
 (II) for j in supp a_n \ G_n: <= 2(sign(a_n(j)) tau^2 v_{n,j})_+ = tau^2 (|v_{n,j}| + z_n(j) v_{n,j}).
Hence Fl^{(n)} + tau^2 kappa_{q,n}(v_n) <= tau^2 [ 2 sum_{j in supp a} |v_{n,j}| 1[|v_{n,j}| > |a_j|/(4tau^2)] + sum_{j not in supp a} (|v_{n,j}| + z_n(j) v_{n,j})
+ 2 sum_{j in supp a \ G_n} |v_{n,j}| ]. As n -> infinity and tau -> 0: the first sum -> 0 (split |v_{n,j}| <= |v_j| + |v_{n,j} - v_j| and use
dominated convergence, monotone in tau); the second has limsup <= kappa_q(v_theta) (z_n(j) -> z_j, v_n -> v_theta in l_1, domination by 2|v_{n,j}|);
the third -> 0 (each j in supp a eventually lies in G_n). Also v_n(zhat_n) -> v_theta(zhat) (norm x weak*), and the Hilbert term is
(tau^2/2)(h_n(b_n) + O(tau)) with h_n(b_n) -> h(b). This gives the uniform estimate. The same computation (without tau) gives
limsup kappa_{q,n}(v_n) <= kappa_q(v_theta), hence limsup H^sh_n(c_n) <= H^sh(c).
Mates: fix rho < 1, choose eta with rho^2(1 + eta) <= rho; for |tau| <= t_1 := min(tau_eta/rho, 2 sqrt(1 - rho)),
p*(f_n + tau rho g_{c_n}) <= 1 + (rho^2 tau^2/2)(1 + eta) <= 1 + rho tau^2/2 <= s(tau); for |tau| >= t_1 use the slack (Lemma 4.7) with
p*(f_n - f) -> 0 and p*(g_{c_n} - g_c) -> 0. Finally H^sh_n(rho.c_n) = rho^2 H^sh_n(c_n) <= 1 for n large. QED.

**Example 4.18 (shifts genuinely enlarge the recoverable class). PROVED (computation).** Single block, theta >= 0 (resp. <= 0).
* Pure base direction (omega = 0): H^sh = max( h(b) - 2 theta [ (1-q_0)/q_0 - kappa_q(R*w) ], 2 theta ) for theta >= 0. If
  r_1 := (1-q_0)/q_0 - kappa_q(R*w) > 0, optimizing theta = h(b)/(2(1 + r_1)) gives H^sh = h(b)/(1 + r_1) < h(b).
  So base directions with 1 < h(b) <= 1 + r_1 may be mates; they are recovered along every sequence by Theorem 4.17 although
  they are not in Cert(f) when a is in c_00 (then, by Fact F(a), the only finite certificate c' with g_{c'} = b is (b, 0), whose
  coefficient is h(b) > 1).
* Pure block direction (b = 0): for theta = -|theta|, H^sh = max( 2|theta| [ (1-q_0)/q_0 + kappa_q(-R*w) ], H - 2|theta| ); optimizing,
  H^sh = H r_2/(1 + r_2) with r_2 := (1-q_0)/q_0 + kappa_q(-R*w) > 0. So the condition "block quadratic coefficient <= 1" of the [Check]
  theorem can be relaxed to H <= 1 + 1/r_2 = 1 + q_0/((1 - q_0) + q_0 kappa_q(-R*w)).
(Whether such directions are actually mates depends on the global condition; the point is that whenever they are, they are
recovered, while the unshifted theory does not apply. Membership of such b in cl Cert(f) would require approximating c_00
vectors by block vectors at their own scale, i.e. rate conditions on T (§7.3).)

Remark 4.19. Corollary 4.11 (lower semicontinuity, reduction (b)-(c)) holds verbatim with Cert^sh in place of Cert (the defect
C(f) \ cl Cert^sh(f) is smaller). The averaging Theorem 6.8 below is proved for unshifted certificates only (shifted expansions have
non-explicit o(tau^2) remainders; a uniform version would extend it).
More general shifts tau^2 V with V_m = theta_m w_m + eta_m (eta_m finitely supported off-peak) give a further family; their exchange rate
uses kappa_q(R*eta) instead of |theta| kappa_q(R*w). I have not written out their transport (SKETCH: identical proof, since eta_m sits
strictly below the peaks). The general principle: the true local coefficient of g at f is a min-max over all decompositions that are
polynomial in tau; certificates and shifted certificates are its first two layers.

