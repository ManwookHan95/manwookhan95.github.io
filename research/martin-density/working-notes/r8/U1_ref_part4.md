# U1 referee, part 4 — the companion: order of moves, Lemmas 4.1-4.6 (configurations (i), (ii))

## 4.1 Order of moves (4.1).  Verdict: correct as an ordering, but step (1a)/(1c) inherits the gap of Theorem 2.3 (part 2, 2.4), and two
## simplifications/repairs apply.
 * (1a)/(1c) "kappa push ... up to the jumps caused by status changes": there are NO jumps (kappa is continuous in zeta, ref. part 1, 1.3);
   the IVT is exact.  But the kappa push restores theta together with kappa (all peaks act identically), so V1's donor raise (C3) is
   undone and V1 Lemma ST(c) — the only source of the strict-non-peak status of the near-threshold carriers — is no longer available.
   Under (KN_{w,a}) replace the donor raise in active blocks by the kappa-neutral lever (part 2, 2.4); then everything below goes through.
 * (2) J_fine must contain the far parts (j > s_far(w)) of the signature sets of all coarse carriers that are NOT owner-candidates
   (see 4.2, gap G1).

## 4.2 Lemma 4.1 (ownership recursion, configuration (i)).  Verdict: CORRECT for the coordinates it covers (PROVED); gap G1 in coverage,
## fixed (PROVED).
Re-derived: well-foundedness (Y_k uses only coordinates owned by earlier candidates or fixed before step (2); a coordinate of supp u_k not owned
by k is owned by an EARLIER candidate, since k itself meets it); zhat = z on J_fine (diagonal base, j notin supp a^#); with sigma_m = -1 the
own coordinates are self-aligned, |u_k(zhat^#)| = |Y_k| + own_k >= ||v_k||_1 = delta_k H_k/n_k; peak with margin >= q_0^# delta_k H_k/(2 n_k)
because Phi_k <= c_k <= (delta_k H_k)^2 ((W3), which holds at every stage of D^{U1'}, part 3).  recursion_check2.py re-run: identical.
GAP G1.  The far parts S_{l''} ∩ (s_far(w), infinity) of the signature sets of COARSE class-G carriers are closed by V1's (C1) (z = eps_{l''})
and are therefore neither in J_fine nor in E_c.  For owner-candidates of types (a), (b) U1 covers them by dominance (own term).  For coarse
carriers that are NOT owner-candidates — Omega carriers that are inactive in the class (gamma = 0), coarse peaks of inactive blocks — V(j) at
such j is the sum of contributions of LATER carriers (fine type-(d) carriers of active blocks, through their targets, allowed by (W4''));
in configuration (i) the sign of such a contribution is varsigma_k sgn y_k(j) with varsigma_k = sgn Y_k fixed by other coordinates: nothing
makes it eps_{l''}-signed, so z_j V(j) >= 0 fails in general (and in configuration (ii) these coordinates are outside J_free as well).
FIX (PROVED).  In step (2) release z on S_{l''} ∩ (s_far(w), infinity) for every coarse l'' that is not an owner-candidate of the class: put
these coordinates into J_fine (configuration (i): they are owned by the first later candidate meeting them, which dominates by Lemma 4.2(ii);
configuration (ii) and mixed classes: they are in J_free of the Schauder map).  Effect: |Delta u_{l''}(zhat)| <= 4 delta_{l''} 2^{-s_far} <=
4 c_{L+1}^2 for these carriers only; their values are not variables of Gamma^#(kappa, a) (gamma = 0 or block inactive), their statuses are
robust or protected by margins >> c_{L+1}^2, kappa moves by <= C Design c_{L+1}^2 (absorbed exactly as in Lemma 4.6, see 4.7).
(Alternative for inactive Omega carriers only: give them the tiny switching eps_l lambda_l 2^{-s_far(w)}, as U1 does for unused absorbers;
this does not work for peaks of inactive blocks, so the release is the uniform fix.)

## 4.3 Lemma 4.2 (dominance).  Verdict: CORRECT (PROVED) after repairing the proof of case (ii) for owners inside clusters / pre-pair blocks.
Case (i) (signature coordinates) re-derived: ratio <= C_f 2^{m + k(k) - j} T_lo(w)^2/(A_2 K) < 1/2 with j >= 3 * 2^k; for absorbers (type (c))
ratio <= C_f 2^{m + k - (j - s_far(a))} T_lo^2 (gamma_a >= c_0(a) = lambda_a 2^{-s_far(a)}); later carriers meeting S_k are main/pre/cluster
carriers: main and pre carriers obey (W4''); cluster carriers of a later main stage L' have weight <= b(L', M(L'))^2, far below (W4'').
Case (ii) (target coordinates): U1's bound "C_f c_{k+1} <= C_f b(k, M(k))^2" is FALSE for an owner k inside a cluster (c_{k+1} = c_k/4).  Repair:
inside a cluster (or a pre-pair block) no later carrier meets the fresh coordinates or the s of k except its partner (whose term is <= 1/4 of
k's, lambda decreases by >= 8 between consecutive block-1 stages), and the first non-absorber stage after the block has weight
<= b(previous stage)^2 <= 2^{-8 n} with n >= Design >= (B_mu D)^6 >= 1/(eta_k lambda_k)^6 (B_mu >= 2^{2 p_0^2} >= 1/mu_{p_0}^2, D >= 1/Phi):
ratio <= 2^{-n} T_lo(w)^{-1} << 1.  This needs the sub-window data (6) at every stage (part 3, D4).  For main-stage owners U1's argument
stands.  Released coordinates (G1 fix) are target coordinates of their first later candidate: case (ii) applies.

## 4.4 Lemma 4.3 ((SC) at f^#, configuration (i)).  Verdict: CORRECT (PROVED), given the coarse statuses.
Re-derived: fine carriers of active blocks are peaks with margin >= q_0 a_k/(2 n_k), a_k := delta_k H_k super-decreasing, contribution only if
a_k <= X(s) := 2 n Upsilon s/q_0, and then <= Phi_k <= a_k^2: sum <= 2 X^2 = o(s) for EVERY sequence (common to all blocks); finitely many
coarse carriers and tuned absorbers (gap M) do not contribute for small s.  The coarse part needs every coarse carrier of an active negative
block to have a positive margin/gap at f^#: U1 takes this from V1 Lemma ST, which is unavailable after the kappa push (gap of Theorem 2.3);
under (KN_{w,a}) the kappa-neutral lever provides it.  (Class-R peaks, anti-type peaks, class-R/(P-ii) near-threshold strict non-peaks
cannot occur in an active negative block: each pins Delta'_dec >= -C_f D K_g t — checked from eq:peakshift and lem:suplevel(f).)

## 4.5 Lemma 4.4 (Schauder completion, configuration (ii)).  Verdict: CORRECT (PROVED), with J_free enlarged by the released coordinates (G1).
Re-derived as V2 Lemma C5: [-1,1]^{J_free} compact convex metrizable; z' -> zhat coordinatewise continuous; R_m^** zhat(z') l_1-continuous
(dominated convergence); J_m norm-to-weak* continuous; V(z')(j) dominated series; Delta''(z') continuous (kappa^# continuous; the values of
Omega_act do not depend on z'); the clamp fixed point gives V_j = 0 at free and z_j V_j >= 0 at contact coordinates.  The absorbers'
coefficients do not enter V on J_free (their supports avoid J_fine), so there is no feedback.  Linearity in Delta'' (V2-ref P6) is why one
common ray per class suffices — which Proposition 2.2(c) provides.

## 4.6 Lemma 4.5 (cost and statuses).  Verdict: cost CORRECT (PROVED); the status claim is NOT PROVED (gap of Theorem 2.3); PROVED under
## (KN_{w,a}) with the lever.
Cost re-derived: (1a) V1 Lemma CO; (1b), (1c) masses <= C_f c_{L+1} T_hi + c_p^2, values of absorbers O(1) but sum lambda_a <= c_{L+1};
(2) Z3 Lemma 3.1 with delta supported in J_fine: coarse carriers meet J_fine only beyond s_far (2^{-s_far} <= c_{L+1}^2), fine carriers
contribute <= c_{L+1}.  The status sentence "every coarse carrier keeps its status class (V1 Lemma ST)" fails for the near-threshold
carriers after the kappa push (part 2, 2.4).

## 4.7 Lemma 4.6 (reference versus true shift).  Verdict: CORRECT (PROVED) with two corrections.
(a) |kappa^# - kappa'|: no jump term (continuity); after the G1 release there is an extra term C Design c_{L+1}^2, still far below the cluster
capacity A_2 c_{L+1}/(Design t); in configuration (ii) Delta''^* = Delta'^* kappa'/kappa^# is common to all t (re-derived); (b), (c) re-derived
(peak traces are the only shift-dependent coarse coefficients; on S^nat of a peak only that peak lives; signs kept since |Delta'' - Delta'| <<
A K t).  In configuration (i) U1 does not re-realize the values of Omega_act after (1b); the middle term C_f c_{L+1}^2/t of (a) is then
absorbed on T(L) by the cluster pairs (capacity c_{L+1}/(Design t)) — correct.
