# cert1 progress log
## Step 1 (read sources) done: MTVI_graph.md, X1_notes.md (all), X1_ref_notes.md (all), Q1_notes 1.1-1.7, Q1_refb_notes (all).
Items: (1) Lemma K + EC; (2) weight-freeness + W-fix; (3) NLM; (4) GEN; (5) QC + Q1-Q3; (6) (S5)-(S6), b_X1 (D1)(D2); (7) P-LIP + alpha-mass.
Next: read Part I lem:threshold / block norm defs; U1 lemma 1.1-1.3 (formula 1, E2), U1-ref R-kt; Q1_refb_part1..3 for P-LIP/alpha.
## Step 2: numerics blockK_check.py (independent solver: outer concave max over M, inner bisection; 60 dps, 40 blocks)
 thr 7e-30, E2 1.3e-30, alpha-mass 6e-32, Lemma K 1.6e-30, K1 8e-60, rho=m|r|k/Phi 1e-61, E5 min (1-R^2)-sigma = 0.467 >= 0,
 monotonicity ok, Lemma F floor ok.  => Lemma K, K1, alpha-mass, E5: CORRECT.
## Step 3 (mental re-derivations so far):
 - Lemma K: (E2)/theta^2 + formula 1 => a^2 = sigma + k^2R^2, k = a + sigma; R<1 needs sigma>0 (P nonempty, lem:threshold); minus root <= sigma.
   dK/dx = k^2/(2(a-kx)) > 0 since a = sqrt(sigma+k^2x) > k sqrt x >= kx.  On W-fix region K <= 4(1+sqrt(5/4-s/4)) ~ 8.5, dK/dx bounded.
 - alpha-mass = (E1)/theta (U1 Lemma 1.2, refereed).  sigma_rob>0: weak coarse peaks <= b||Phi||^2, fine peaks <= sum lambda/theta.
 - EC: L = sum gamma_l (u_l - r_l tau_m) with (X3)/kappa; tau_m = peak weights only (K1: active weak peaks in Omega).
 - Weight-freeness: rows in (Delta',gamma) [gamma absorbs lambda]; only U1-ref (X4) has 1/lambda -> (X4^0) multiplies by lambda,
   lambda rho^0 = m^2|r|K(sigma_rob,R_a^2).  aggregated coeff ||v_l 1_{S_l cap [1,s]}||_1 in k_0 for every s; scaling a row does not change
   zero sets of minors/cofactor polys -> s_far(w) dependence harmless (remark: define rate objects with s-free coefficient).
 - NLM: Sard argument re-derived; OK on W-fix region (weight-free). GEN: Tarski transfer + Zariski closure + norm: OK.
 - QC(a)-(c), Q1-Q3: OK.  Precision P-CY: (D2) matches X1's normalization dist <= C_Y (F-1)_+^alpha; with X1-ref's normalization
   dist^{1/alpha} <= C_Y (F-1)_+ one needs C_Y >= 1 (WLOG).  Choice rules for C_Y, alpha_Y, c, beta, h must be fixed (V2 remark (a)).
 - P-LIP correct and needed (Q1's Lip(l) = minors' constant); extend to statuses of all active coarse carriers (still <= Design).
Next: check [II] cor:II-Rkt, refb_part1 (P-LIP), X1_ref_part2 (weight-freeness), toy Sard/QC numerics.
## Step 4: nlm_qc_toy.py (EC-structured toy: 2x2 minor affine in r -> Z a line; psi with K; W-fix region):
 generic weights mu(h) ~ 1.34 h (beta 0.999); coincidence weights mu = 0 exactly, slopes -2.39/+1.37 (critical for Psi_D);
 x(1+1e-3) -> mu(1e-3)=1e-3; P(|min F - 1|<eps) = 0.34, 0.032, 0.0032 for eps = .1,.01,.001 (codim 1). Cusp Z: coincidence at tip mu=0, perturbed >0.
 => NLM/QC behave as claimed.  [II] cor:II-Rkt read: same identities (r^II = m|r|), uniqueness of root on half-line a > c0 R/(1-R).
Next: read [II] def:II-Gamma rows to confirm no extra weight-bearing row; then QC/S5-S6 review; then write report.
## Step 5: wfix_bounds.py: on W-fix region max K = 4(1+sqrt(5/4 - s/4)) ~ 8.47; dK/dx <= 32.1/sigma_rob; min (a-kx) = 1.118 sigma_rob
 => Lip of psi_d on K_kappa <= C m/(sigma_rob Phi_d) <= C m D^3 (finite design number).  Data: a+sigma <= 0.372 (m=1).
## Step 6: [II] def:II-Gamma read: rows (X1) (aggregated on S_l cap (L, s_far(w)] with coefficient ||v_l 1_{...}||_1), (X3), (X4), (X5).
 NEW PRECISION P-SFAR: s_far(w) = least s with 2^{-s} <= c_{L+1}^2 is a FORWARD reference (c_{L+1} chosen at stage L+1 after level-L
 sub-windows) inside the level-L rate objects (aggregated coefficients).  No source addresses it (grep).  Fix: rate objects use the s-free
 coefficient ||v_l 1_{S_l cap (L,inf)}||_1 (in k_0); cone at w differs by a positive row scaling in [1 - 2^{s_1 - s_far}, 1]; zero sets of
 minors and cofactor polynomials identical (positive row scaling), robust values / Lemma H / Lemma L constants change by <= factor 2.
 Weight-freeness unaffected (coefficients in k_0 for every integer s).
 P-CY: (D2) matches X1 2.5(b) normalization dist <= C_Y (F-1)_+^alpha; with X1-ref's dist^{1/alpha} <= C_Y (F-1)_+ need C_Y >= 1.
 P-LIP+: Lip* needed in delta_0 (2nd term) and robust-status motion; in (D1) harmless/unneeded.
Verdict draft: (1) correct; (2) correct (W-fix, K1 essential; also aggregated row of d in N_T weight-free only because of K1);
 (3) correct; (4) correct; (5) correct (+cosmetic P-CY, choice rules); (6) correct_with_fixable_gaps (P-LIP, P-SFAR, P-CY);
 (7) P-LIP correct & sufficient (extend to statuses); alpha-mass correct.
## Step 7: cert1_report.md sections 0-2 written. Next: sections 3 (NLM), 4 (GEN), 5 (QC), 6 (S5-S6, P-SFAR), 7 (P-LIP, alpha), 8 numerics, 9 fixes list.
## Step 8: report sections 3-5 appended. Next: 6 (S5-S6 + P-SFAR), 7 (P-LIP/alpha), 8 numerics list, 9 fixes, 10 pass counts.
## Step 9: report complete (sections 0-10). Final verdicts: (1) correct; (2) correct; (3) correct; (4) correct; (5) correct (cosmetic P-CY,
 P-CHOICE); (6) correct_with_fixable_gaps (P-LIP needed, P-SFAR new, P-CY); (7) P-LIP correct+sufficient (P-LIP+ extension), alpha-mass correct.
