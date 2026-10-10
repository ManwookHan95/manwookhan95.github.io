# V1 part 0 — reading digest (for my own use; not a result file)

## Y1 (refereed correct): design D_X, clean sub-windows, companion f^#_w, Prop 5.2, Thm E', master theorem 5.4
- Design(l) = [l 2^{l^3} 2^{sigma(l)} Lambda°(l)(1+|T(l)|) D(l) G*(l) H_comb(l) G**(l)]^6; M(l) = omega(l)+1 sub-windows, omega(l) = 3l+|T(l)|.
  u(w) = b(w^-), Q(w) = Design^4 u^{-omega-8}, n(w) = ceil(l 2^{l^3} Q), T_hi(w) = min{T_lo(w^-), 2^{-l^3}/(l Q)}, T_lo = 2^{-n} T_hi,
  b(w) = T_lo^4/(l Design), c_{l+1} = min{c_l/4, b(l,M(l))^2}.  T(l) = union_{l''<=l} supp y_{l''}, s_max(l) = max T(l),
  sigma(l) = max_{l''<=l} min(S_{l''} ∩ (s_max(l), inf)).  D(l) = 1 + sum (1/m^nat + 1/Phi).
- Rate objects (R1) room on S^nat_{l''}(l) = S_{l''} \ (F ∪ T(l)) normalized; (R2) target room 1-|z_j|, j in T(l)\F; (R3) |rho-1|; (R4) rho.
- Clean sub-window: every rate tiny (<= b(w)) or robust (>= u(w)).
- Classification: class R (robust room) / class G (tiny room; eps = minimizing sign); swallowing-type (eps sgn w = +1, q > 0) / anti-type.
- Pinning (Lemmas 3.1-3.6) : class R diag; G one-sided; peaks; (SP_w) shift sources -> |Delta d| M <= K_d t; anti near-threshold np pinned;
  one-signed blocks: Sigma_m(w) pinned (needs (SP_w)).
- KEPT: (K1) swallowing-type strict non-peaks; (K2) anti-type strict np with robust gap; (K3) nearly neutral rho <= b; (K4) near-threshold
  swallowing-type (weak/degenerate peaks, rho in [1-b,1+b]) in blocks not one-signed. In one-signed blocks only (K3) kept.
- Companion f^# (z only; a fixed): (C1) z^# = eps on S^nat_{l''} for class G; (C2) close tiny target rooms; (C3) donor raise at s_m with
  lambda_c |u_c(Delta)| = T_lo^3. Cost (Lemma 4.1) C_f T_lo^3 log(1/T_lo). Lemma 4.2 status table; Lemma 4.3: closing room of d-neutral
  carrier gives q^# = r^nat/A^# > 0 (forced sign) -> residual (n).
- Prop 5.2 (transplant): Step 1 Hoffman projection on generalized configuration kappa^# (G**), Step 2 d-rows at f^#, Step 3 exact d-repair
  via (Rep^s_m) [compensated] or one-signed + (NN_w), Step 4 split at f^#, Step 5 data & estimates, kinds [1],[2],[3], A_2 = 22.
  K_w <= C_f Design^3 u^{-3}.
- Thm E' (window-dependent c_flat).  Master Thm 5.4: (SP_w),(Do_w),(Cmp_w),(NN_w) at infinitely many levels => f in Rec.
- Residuals: (n),(m),(d),(h),(O4).
- Y1-ref: (m3) donor reason corrected; kind [1'] (gap>0, |omega|<=2gap/t suffices); Section 7 outline of pulls replacing (NN_w), (Do_w):
  tune val_l := 0 for kept (K3) carriers of one-signed blocks; pulls at j_l ~ log2(1/b) > sigma(l) > s_max(l); banks at
  min(S_l \ (F ∪ [1, s_max(l)])); design additions: bounded gaps G_l, 1/s_{sigma(l)}^2 (diagonal U) in Design.

## Y2 (refereed): Lemma T, Lemma U', Thm E', Prop Q (donor companions), Cor Q', Thm P, design D^Y (Xi^Y), faces, Thm M, Thm H, Thm Y
- Lemma T(d),(e): raising moves (peak outward / strict np inward / degenerate either way) with perturbation bounds.
- Prop Q: donor = carrier not in Sw_j with infinitely many raising coords outside F ∪ Ba_j ∪ T_j; companion z + delta at donor coords;
  values of switching carriers unchanged; common factor |zeta|/|zeta'| per block; inward coords -> strict non-peaks.
- Y2-ref Lemma R-T: target donors: D_m(c) one-sided derivative of Psi_m; convex pos. homogeneous; at free coordinate D(e)+D(-e) >= 0.
- Y2-ref (G1) gap (only SLD_G); P-Q1 (inward strict non-peaks allowed in Prop Q).
- Thm H: shift cost c_*(l) > 0 replaces (H2''); coherent shift resonance OPEN.

## Y4-ref C.1-C.8 (refereed as new results by the Y4 referee; PROVED there):
- C.1 pulled row: A = a - eps mu e_j^*, z'_j = -eps (j in S_l \ F far out).
- C.2 Lemma P1: val_l moves by -2 v_l(j) + O(mu), others by O(mu ||U^* e_j^*||/nu) (O(mu^2) diagonal); cost C_f (v+mu) log.
- C.3 Lemma P2: Lemma U and Thm E hold with banked and pulled supports (t|b(j)| <= |a_n(j)| on pulls; contact-like data on banks).
- C.4 Lemma P3: transplanted data at pulls: t|b^pm(j)| <= 12 lambda_l v_l(j); mu_j := 24 lambda_l v_l(j).
- C.5 addendum (G): bounded gaps G_l of S_l.
- C.6 Prop P4: two-sided per-carrier exact tuning (diagonal U): pulls then banks (diag Jacobian), val_l^# = val_l + x_l exactly,
  others O(|x|^2), cost C|x| log(e/|x|).
- C.7 Cor P5: tiny single-block rays neutralized exactly (sign-constrained Hoffman, H_tune(l)); status of NT carriers needs (BS) or a
  threshold buffer (donor, or extra equation via pulls/banks on an unused swallowed carrier: SKETCH).
- A.3: Design^PW(l) includes 2^{s_max(l)}/delta_min(l), 2^{G_l}, H_tune(l); Q(w) = (4 Design/u)^{omega+3}.

## PLAN (after reading; key new ideas)
1. BANK DONORS settle (D): every block has, at a clean sub-window of large level, a coarse non-degenerate peak c with ROBUST margin
   (sum of |alpha| over tiny-margin coarse peaks <= (M/4C) b, fine peaks <= C b^2/sigma). c is dropped (pinned). At
   s := min(S_c ∩ (s_max(l),inf)): if sgn-room toward vs_c is large, z-move (Y1 C3); else close z_s := vs_c and BANK mass m at s
   (diagonal U): first-order Delta(vs_c u_c(zhat)) = m s_s^2 v_c(s)/nu > 0, other coarse values O(m^2). Lemma T2(b) => theta raise.
   (aligned corner = all far coords of peaks are own-sign contacts: banks work there.)
2. Rays: rate objects (R5) = (pattern kappa, extreme ray r of C(kappa), block m): |sum_{l in r, m(l)=m} r(l) val_l|/max Phi.
   Tiny components neutralized exactly by tuning (pulls+banks, Prop P4), least-norm solution |x| <= H_tune |V|.
   (VR_w): each extreme ray has <= 1 robust component -> blockwise ray removal (Y4 Lemma 1.8). Residual (B) = failure.
3. Shift: (SH_w) sources (Y1 Lemma 3.4) or shift cost c_pi(w) >= u (port of Y2 Prop 5.2); rate objects (R6) c_pi over shift patterns.
   Residual (C) = some block lacks a source and c_pi(w) <= b(w).
4. Split w.r.t. z^(2) (before tuning pulls); balance with a/a(zhat^#); Hilbert comparison at changed e.
5. Lemma IP (inward push of near-threshold coords by nu-amounts c_k in [c,2^G c], c > 2b(A+theta)): theta' >= theta, nu'_k <= theta'-(c-theta b).
   (alternative to donors; not used in assembly because pushes ~T_lo^3 spoil tiny-ray dichotomy)
