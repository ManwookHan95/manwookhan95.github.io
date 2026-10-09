# Y1 referee, part 5: attacks attempted, hidden-rate audit, open core

## 5.1 Hidden-rate audit (is every f-dependent quantity either a fixed f-constant or one of the omega(l) rate objects?)
Quantities entering K_w, c_flat, the cost bound and the status table, traced through parts 3-5 of Y1:
 rooms of S^nat (R1); target rooms (R2); margins mu = q_0 Phi theta (rho-1)/m and gaps M(1-rho) (R3); d-coefficients |q| = Phi M rho/(mC)
 at strict non-peaks (R4); 1/Phi, 1/m^nat, 1/lambda <= D(l) (design); the configuration Hoffman constant G**(l) (design: matrix entries
 u_l(j), j in T(l), and finitely many combinatorial data); repair normalization d >= u/Design and repair gaps >= M u/4 (hypotheses);
 q_0, nu, sigma_m, C_m, M_m, theta_m, A_m, C_F, transfer data, donors' lambda_c, margins and delta_c, repair norms R_f (fixed f-constants).
No other quantity occurs. In particular slaving and room products are absent (S^nat excludes all coarse targets), and the target-induced
closing terms min(lambda_{l''}, |y_{l''}(Delta)|) of Z3-ref (G5) / Y4-ref (G-PW1) vanish for coarse carriers for the same reason (only fine
targets can meet a closed S^nat, total <= sum_fine lambda <= b^2). VERDICT: no hidden rate.

## 5.2 Attacks attempted (none breaks a PROVED claim beyond the fixable items m1-m6)
* weak* vs norm: decompositions exist at every scale (lem:twosided); companions converge in norm (Z3 Lemma 3.1); fine carriers handled by
  the box bound; nothing uses weak* limits of decompositions.
* uniformity in t: every estimate at t in W(w) uses t >= T_lo(w) only through b(w) <= T_lo^4/(l Design) and sum_fine lambda <= b^2/3.
* uniformity in the window: all constants are design(l) x u(w)^{-k} x f-constants; Q(w) = Design^4 u^{-omega-8} dominates (re-done).
* number of active carriers: G** over all U in [1,l]; l enters linearly (Z3 rows) and is absorbed.
* along companions: Lemma U' (t_1, j_0 independent of A_2, gamma_B; c_flat ~ u(w_j)); companions keep supp a = F.
* Hoffman/Farkas: right-hand-side independence (Hoffman 1952), feasibility via 0 in Z_kappa(beta); the one-signed d-row is an explicit
  certificate with |q| >= Phi M u/(mC) at a clean window.
* design N-independence: all ingredients maximized over subsets of [1,l]; omega(l) counts objects of all blocks.
* non-attained infima: polyhedral projections exist; theta(zeta) is a root of a continuous strictly monotone function; norming functionals
  certified exactly (numerics).
* signs and one-sidedness: eq:peakshift, suplevel(c),(f), the anti/swallowing dichotomy in Lemma 3.5(b), the shift trick signs, the
  outward direction of the donor push (vs z_{s_m} <= 0), the sign of the forced q^# in Lemma 4.3 — all re-derived.
* near-contacts vs contacts: (C2) closes tiny-room target coordinates; free target coordinates have room >= u at a clean window; S^nat rooms
  closed by (C1); flipped coordinates have v-mass <= r^nat <= b.
* c_0 vs l_infty: companions are non-attaining first rows with z^# in l_infty; Corollary D1 handles NA approximation at each f_j.
* finite vs infinite sets: F finite (hypothesis); G and T(l) finite per level; infinitely many contacts allowed.
* hidden assumptions on T: only (T-a)-(T-d), (P1)-(P3), allowedness, and D_X's explicit recursion; D_X is ONE operator for all N.
* quantifier order: D_X before f; w_j, f_j depend on f only; data on (g, rho, t); Lemma Z per mate is not even needed (f_j independent of g).
* suspected counter-scenario (class-G SWALLOWING-type donor making "(C3) after (C1)" infeasible) REFUTED: the tail point s_m in S^nat_c(l)
  has room >= delta_c 2^{-sigma(l)}/n_c >> b(w) in the -vs direction (part 3.1); only Y1's stated reason was wrong (m3).

## 5.3 Open core after Y1 (+ this report), design D_X, F finite, g not window-pinned
f must, at all but finitely many levels and at EVERY clean sub-window, violate one of (SP_w), (Do_w), (Cmp_w), (NN_w), AND lie outside the
other proved classes that survive for D_X (R_0^pm, R_S, R_BT, Z6 Theorem U' (rigid blocks, with its growth condition), Z4 Theorem A'',
Y2 Theorem Y if it survives for D_X). Concretely:
 (n) one-signed blocks whose kept nearly neutral carriers have d-coefficient of the block's own sign at f^#_w (incl. Z3 Lemma 1.4 carriers);
     NOT intrinsic: far pulls + banks (Y4-ref C.2-C.7, diagonal U) tune each such carrier to exact d-neutrality (SKETCH of the assembly).
 (m) mixed blocks neither compensated nor one-signed (rigid ones: Z6 U' under a rate; single-block tiny rays: Y4-ref Cor. P5, SKETCH of the
     assembly); multi-block rays OPEN.
 (d) aligned corner (no donor): shrunk by Y2-ref target donors; pulls on the peak's own closed signature set (Y4-ref C.8(ii)): SKETCH.
 (h) failure of (SP_w) (Y2 Theorem H; coherent shift resonance OPEN).
 (O4) infinite F.
Density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2) remains OPEN for every admissible T, including D_X. No counterexample is
claimed; nothing found points to one.
