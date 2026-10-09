# Y2 referee, part 5: Lemma 5.1, Proposition 5.2, Theorem H, Theorem Y, Corollary Y.1, Sections 6.2-6.4; target donors

## Lemma 5.1 (peak trace). Verdict: CORRECT (PROVED).
eq:peakshift gives e_k = -varsigma Delta Theta(k) - Delta d M >= 0, Delta theta_l = lambda Delta Theta(k), so -Delta theta_l =
varsigma lambda (Delta d M + e_k); e_k <= t/(sigma|alpha(k)|) = t/(lambda mu) by eq:margin. The split of eq:DeltaB along P* and
||E||_1 <= t sum_{P*} 1/mu are right.

## Proposition 5.2 (shift-cost pinning). Verdict: CORRECT (PROVED).
Decomposition Delta B 1_{F^c} = sum_m delta_m Pi_m + sum_{Bfree} x_l eps_l u_l 1_{F^c} + R with x = (tau)_+ and ||R||_1 as stated
(good: K_g t; fine: 6t^2; (tau)_- on swallowed l <= l_*: K_- t from the projection tau° >= 0 and the box bound; pinned halves; E).
c(.;l) is the partial infimum over a finite-dimensional cone of a jointly convex, positively homogeneous, finite function: convex,
positively homogeneous, finite, hence continuous; c_* is attained on the compact sign sphere (the inner infimum over x need not be
attained, which the note's "arbitrarily close to 0" correctly reflects). phicalc(c) and the switching budget give
c_* ||delta||_1 <= t/q_0 + 2||R||_1. Remark: I_up ∩ I_lo is always empty (both halves failing would leave block m without non-degenerate
peaks, contradicting ||alpha_m||_1 = 1), so the "free sign" case is vacuous; harmless.

## Theorem H. Verdict: CORRECT (PROVED by modification).
(H2'') enters A'' only through K_d; Proposition 5.2 supplies K_d = K_sh <= C_f(1 + l/mu_0) K_1 D K_sh^rel; all later constants are
linear in K_d; the window arithmetic absorbs D^2 (1 + l/mu_0)^2 by the surplus D^6 Lambda°^4 of D^Y (Lambda°(l) >= 3^l >= l^2). Correct.

## 5.3. Verdicts.
(a) The inequality Delta d_m M_m <= 2 gap_m(k(l))/t + (tau_l)_-/lambda_l (q_l < 0 swallowed strict non-peak) is CORRECT (re-derived from
suplevel(f): varsigma(omega_+ - omega_-)(k) = tau/lambda + Delta d |w(k)| and |w| + gap = M). PRECISION on the gloss: to pin at O(t) one
needs gap_l <= K t^2 on the whole window AND (tau_l)_-/lambda_l = O(t); the second holds with the signature budget
(tau_l)_- <= c_U/(2 m_l), i.e. with the design-scale factor 1/(m_l lambda_l) (absorbed by D^Y's D(l)^8), not with lambda_l >= t^2 alone.
For a FIXED carrier gap_l <= K t^2 fails at small t, so gap pinning needs a SEQUENCE of near-threshold q < 0 carriers with gaps <~ T_lo^2
of the window: it converts a rate (gaps beyond the ladder) from an obstruction into a help in configuration (i), as stated, but only
along such windows.
(b) CORRECT (the j_m-term argument). Note that P*(l), Bfree(l) grow with l, so the conditions on j_m must hold at every large level.
(c) OPEN (agreed). The "new observation" is imprecise: what must be z-signed on K and vanish on J is the whole vector
v = sum_{m'} R_{m'}^*(delta omega_{m'} - Delta d_{m'} w_{m'}), i.e. -sum_{m'} Delta d_{m'} R_{m'}^* w_{m'} off the signature sets and
targets of the finitely many used carriers; with several blocks of nonzero Delta d the cross-block sum, not -Delta d_m R_m^* w_m alone,
is constrained. (Single-block reading correct; Z4-referee Prop 5.6' is the rigorous form on far signature points.)

## Theorem Y and Corollary Y.1. Verdict: CORRECT (PROVED by combination), with (P-Q1) and two notational precisions.
Every modification is local and compatible: (M) changes only the drop rows of degenerate swallowing-type peaks; Proposition 4.3
replaces Hoffman + (DR) (the cone with kept degenerate peaks is still a configuration cone, faces are free configurations);
Proposition 5.2 supplies the shift bound; Lemma U'/Theorem E' at companions of Proposition Q (with (P-Q1)); windows of D^Y absorb
D^2(1 + K_F^rel)^2(1 + K_sh^rel)^2(1 + l/mu_0)^2 G**^4 Lambda°^2 Xi_f. In particular gap (G1) of part 3 does not occur here.
Precision (P-Y1): (Y1) should read "r*_l(l_*) > 0 for every good l and every level l_* >= l" (r*_l(l_*) is nonincreasing in l_*;
Lambda*_f(l_*) = infinity otherwise; cf. Z3-referee (G6)); "r*_l(l) > 0" is not enough.
Precision (P-Y2): Theorem Y uses Lambda*_f (all carriers) in Xi_f, not the good-only product Lambda_g of Theorem U'; at maximal contact
Lambda*_f <= C Lambda°, which is what Corollary Y.1 uses (correct), but away from maximal contact Theorem Y and Theorem U' are not
comparable term by term.
Corollary Y.1: (Y1) vacuous (no good carriers, no free coordinates: gamma_T = 1); (H2'') from Lemma 5.0 (non-degenerate peaks of both
signs: LOWER from swallowing-sign, UPPER from anti-sign); (Y3) from Corollary P.1; Xi_f <= C(1 + M_f/Lambda°)^2/gamma_f. CORRECT. The
reading "at maximal contact only three f-dependent rates remain: M_f, gamma_f, K_F^rel" is correct for F finite and the design D^Y.

## 6.2 Conjecture G: OPEN (agreed); the un-switching computation is HEURISTIC as labelled.
## 6.3 (a) PROVED (Z4-referee Observation 9.1); (b) PROVED as a statement about the method (a first-order mismatch O(|tau|) costs
O(|tau| iota) after rebalancing, not o(tau^2)); (c) HEURISTIC as labelled.
## 6.4 Weak peaks through companions: SKETCH (agreed), with these gaps beyond "bookkeeping":
 (W-a) Lemma T(e) is qualitative; carrying a peak of relative margin r = nu_k - theta needs a QUANTITATIVE raise theta' - theta > r.
     First-order: d theta = A Delta/((A + theta) sum_{k in P} Phi_k^2) for a peak donor of size Delta (from d Psi = 2A Delta and
     d Psi/d theta = -2(A + theta) sum_P Phi^2); so the companion cost is ~ r (A + theta) sum_P Phi^2 / A, plus cross-effects, and must be
     o(T_lo^2). This is plausible (sum_P Phi^2 is tiny) but not written.
 (W-b) A carried NON-degenerate peak has alpha(k) != 0 at f, so inward data at f have a nonzero first-order term <omega, alpha>; the window
     data must be built (or corrected) at f_j, and the d-repair at f_j needs face/repair constants at f_j, whose combinatorial type
     (peak status) differs from that of f; uniformity of R_{f_j}, kappa*_{f_j} in j is not addressed.
 (W-c) The raise also turns UNUSED weak peaks into non-peaks and may change which carriers are active/kept; harmless for Corollary cor:D1
     at f_j, but it changes M_f-type bookkeeping at f_j.

## Referee extension: target donors (PROVED; narrows the aligned corner of Section 3.4)
Lemma R-T. In Proposition Q the signature donors may be replaced by any finite family of admissible moves z_{j_i} -> z_{j_i} + eta c_i d_i
(d_i = +-1, c_i >= 0, |z_{j_i} + eta c_i d_i| <= 1 for small eta) at coordinates j_i outside F ∪ Ba_j ∪ T_j ∪ ∪_{l in Sw_j} S_l, provided
   D_m(c) := one-sided derivative at eta = 0+ of Psi_m(theta_m(zeta_m); zeta_m + eta Delta zeta_m(c)) is > 0 for every m in I_D,
where Delta zeta_m(c)(k) = lambda_k sum_i c_i d_i u_k(j_i). Explicitly
   D_m(c) = 2A_m [ sum_{nu_k > theta} s_k Dz_k + sum_{nu_k = theta} (s_k Dz_k)_+ ] - 2 sum_{0 < nu_k < theta} nu_k s_k Dz_k
            + 2 theta_m sum_{nu_k = theta} (s_k Dz_k)_-,     Dz := Delta zeta_m(c), s_k := sgn zeta_m(k),
a convex positively homogeneous function of c. Consequently every FREE coordinate j outside these sets for which D_m(e_j) and
D_m(-e_j) are not both 0 is a donor for block m in one of its two directions (D_m(d) + D_m(-d) >= D_m(0) = 0 by convexity).
Proof: in ./Y2_ref_notes.md, Section 3.
