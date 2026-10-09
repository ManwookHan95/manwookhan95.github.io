# Z6 part 1: orientation observations (labels as stated)

1.1 (HEURISTIC, primal picture) Resources and their "exact" versions:
 - base: contact j (|z_j|=1): exact one-sided; near-contact (|z_j|=1-eta): primal excess in direction e_j is (s - q_0 eta)_+
   (flat up to q_0 eta, then linear); exact contact: s_+ . phi_z(x) = (1-eta) phi_1(x) + eta phi_0(x) for z = 1-eta (exact identity).
 - block: degenerate peak (alpha=0): exact one-sided (inward free, Lemma overshoot); weak peak (margin mu small): inward free up
   to lambda*mu, then linear first-order cost |alpha||omega| t; strict non-peak with gap: two-sided quadratic up to gap/|omega|.
 - "Exactification" (near -> exact) makes the primal excess STEEPER, hence (slice lemma) heuristically ENLARGES the fibre;
   lowering z (giving room) makes it flatter and heuristically SHRINKS the fibre. So the far-lowering lsc question (O2) is the
   hard direction, exactification the easy one.

1.2 (PROVED, from note Lemma suplevel(c), eq margin) Peak usage is margin-pinned: for k in P_m,
   lambda_k mu_k (|omega_+(k)| + |omega_-(k)|) <= t (sum over peaks <= t), since sigma|alpha(k)| = lambda_k mu_k.
   Hence at every non-degenerate peak, |Delta theta_k + varsigma_k lambda_k Delta d_m M_m| <= t/mu_k (peak-shift identity).
   So at maximal contact, peak carriers switch collectively through the scalar Delta d_m up to margin-controlled errors.

1.3 (HEURISTIC) At maximal contact z = 1 off F (F finite) a carrier with target y_l is a FREE switching resource only if
   (y_l + delta_l h_l) >= 0 off F (resonant) or in positive combinations; a target with a coordinate of room pins its carrier.

1.4 (HEURISTIC) Margins: mu_l ~ q_0 |y_l(zhat) + delta_l h_l(zhat)|/n_l. With design delta°_l >= 2^{-poly(l)}, weak peaks with
   super-small margins need near-cancellation y_l(zhat) ~ -delta_l h_l(zhat); for a fixed target at most O(1) repetitions can
   cancel. Infinitely many weak peaks at arbitrary rates exist when z has free tuning coordinates in target supports.
