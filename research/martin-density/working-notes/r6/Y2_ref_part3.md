# Y2 referee, part 3: Theorem P, Lemmas 3.1, 3.2, Corollary P.1, the aligned corner

## Lemma 3.1 (donors exist) and the raisability bookkeeping. Verdict: CORRECT (PROVED).
Ba_j: b^+ = B_+1_F + chi V' - kappa a with V' = sum_{l: tau'_l != 0} eps_l tau'_l u_l 1_{F^c}, and b^- = b^+ - sum_{Sw_j} eps tau' u_l, so
Ba_j ⊂ F ∪ ∪_{l in Sw_j}(S_l ∪ supp y_l); for l' notin Sw_j, Ba_j ∩ S_{l'} ⊂ F ∪ (finite). Sw_j consists of the carriers with
tau'_l != 0 at some scale of the window; peaks other than the kept degenerate swallowing-type ones have tau' = 0 (dropped), good
carriers are never switching, and Sw_j ⊂ [1, l_j]. Raisability: anti-sign swallowed peak (z_s = -varsigma, raising sign varsigma),
degenerate peak (either sign), q > 0 swallowed strict non-peak (z_s = sgn w, raising sign -sgn w) are raisable; swallowing-type
non-degenerate peaks and q < 0 non-peaks are not. All checked.

## Lemma 3.2 (window data with inward degenerate peaks). Verdict: CORRECT WITH A FIXABLE GAP (G1) in Step 5.
Checked: (M) gives inward signs on both sides (varsigma omega^+ = -min(|omega_+|, tau'/lambda) <= 0, varsigma omega^- = tau'/lambda - min(...) >= 0,
since varsigma eps = 1, tau' >= 0); representation and d-neutrality are purely algebraic ((eps tau'/lambda) Phi^2 w/C = q tau'); V' is
z-signed in K (tau' zero cost). The two-case discrepancy computation lambda|omega^+- - omega_+-| <= |tau - tau'| + lambda|Delta d|M was
re-derived from eq:peakshift (|omega_+| + |omega_-| = tau/lambda - Delta d M at a swallowing-type peak): correct in both cases.
Step 4 (only the deleted rows needed (H3); configuration constant covers every drop set P ⊂ U): correct.
(W4) at D_t: |omega^-| <= 4/t + tau'/lambda <= (10 + C_dia)/t since lambda >= t^2 on U: correct.

(G1) GAP. Step 5 says "Lemma 2.3 of Z4 (repair through U_R) applies verbatim". It does not when (DR) holds through its VACUOUS
alternative ("block m contains no swallowed strict non-peak with q_l != 0; put tau^{m,+-} := 0"), but block m contains kept degenerate
swallowing-type peaks: their weights q_l = Phi M/(mC) > 0 now enter the d-row of block m, which no repair direction can correct.
In such a block the modified exact cone forces tau_l = 0 on D(t) (d-row with q > 0, tau >= 0), i.e. the degenerate peaks are d-rigid,
and the actual switching through them can be of size ~ K t/q_l (the d-identity pins only sum_D q_l (tau_l)_+ = O(K t); Z6's numerics
show the 1/q constant is essentially attained). Projecting onto the exact cone then costs sum_D |tau_l| ~ K t sum_D 1/q_l with
1/q_l ~ 2^{m+k}/c_l -- a DESIGN-scale factor (Lemma R of the Z4 referee), NOT absorbed by SLD_G (for l near l_*, 1/c_l >= T_lo(l_*-1)^{-3}
while T_hi(l_*) <= T_lo(l_*-1)).
FIX (PROVED): (i) If (DR) is non-vacuous in every block containing a degenerate swallowing-sign swallowed peak, Lemma 2.3 applies and the
proof is correct (the repair keeps the D-components of tau_0). (ii) If in such a block (DR) is vacuous but its degenerate swallowing-type
peaks are FINITELY many, they are d-rigid; drop them (drop rows tau = 0): by the d-identity (Z4 eq:didentity, with the anti-sign and
non-degenerate swallowing peaks bounded as in Z4 Step 4 and strict non-peaks of weight 0), sum_D q_l (tau_l)_+ <= C(K_1 + M_f)t and
(tau_l)_- <= lambda_l K_d t, so sum_D |tau_l| <= C(K_1 + M_f)t / q_min(D), an f-constant factor; Step 4 then holds with M_f replaced by
M_f + C/q_min(D). (iii) For D''' (and D^Y), infinitely many such d-rigid degenerate peaks are dropped by Theorem V(b) / Proposition P of
Z6: the certificate -e_p = -(1/q_p)Q_m + sum_{other swallowing-type l}(q_l/q_p)e_l has sup-norm <= (1 + q_max)/q_p <= C_f/Phi_p <= C_f D(l),
absorbed by the D(l)-factors of D'''; for D^Y the face reduction of Theorem M handles it directly (part 4).
(iv) For SLD_G with INFINITELY many degenerate swallowing-type peaks in a block where (DR) is vacuous, the statement is NOT proved.

## Theorem P. Verdict: (a) CORRECT WITH FIXABLE GAP (G1); (b) CORRECT given precision (P-Q1).
(a) Proof = Z4 Steps 1-9 with (M), Lemma 3.2, Lemma 3.1 and Proposition Q; window arithmetic of Z4 Step 8 with c_{flat,j} >= c_0
gamma_f(l_j)/A_2(j) (Lemma U') unchanged: correct, subject to (G1). Corrected statement: "(H3) replaced by (TD_m) for every block containing a
degenerate swallowing-sign swallowed peak, provided (DR) is non-vacuous in each such block or its degenerate swallowing-type peaks are
finitely many (SLD_G); for D''' with no further proviso (Theorem V(b) for the d-rigid ones)."
(b) Theorem U': non-rigid degenerate swallowing-type peaks of compensated blocks kept with sign row only; H_comb covers every
kept/dropped partition; compensation (Z6 5.3 step (5)) adds compensator multiples (upward closure in resonant compensator directions)
and treats kept degenerate peaks as kept q > 0 carriers: correct. The data use, besides inward degenerate peaks, the shift-trick
coordinates (kept q > 0 strict non-peaks used inwardly with ANY gap, Z6-referee Lemma 2.1): Proposition Q must be read with (P-Q1)
(inward strict non-peaks allowed in (W2)); with that, correct. Rigid degenerate peaks: Theorem V / Proposition P as before.
Note: in Theorem P(b) the d-rows are handled by compensation (no (DR)), so (G1) does not arise; rigid blocks drop all their q != 0
carriers by Proposition P.

## Corollary P.1 (maximal contact). Verdict: (ii) CORRECT; (i) correct after the (G1) proviso.
Every block has infinitely many non-degenerate peaks with w = -eps_0 M (Lemma 5.0 of Z4, valid at every f), swallowed with eps = eps_0:
anti-sign swallowed peaks, raisable (z_s = eps_0, raise toward -eps_0, which makes s a free coordinate of the companion -- harmless,
b^+- vanish at s), dropped in A'' and U', hence donors. So (TD) holds in every block. (i) Z4 Corollary 5.4 (SLD_G) holds without (H3)
except in the (G1) sub-case (a block with infinitely many degenerate positive peaks and no swallowed strict non-peak with q != 0).
(ii) Corollary 3.4' (D''') with degenerate positive peaks allowed in compensated blocks: correct. In particular the configuration of the
Z6 referee's Proposition R1 is recovered for DEGENERATE positive peaks (weak positive peaks remain the rate K_P). Agreed.

## Section 3.4 (aligned corner). Verdict: the residual is correctly identified FOR THE SIGNATURE-DONOR METHOD; the gloss
"every admissible z-move outside the data supports LOWERS the threshold ... so threshold steering is impossible there" is NOT PROVED
(HEURISTIC, and probably false in general).
Lemma T(d) concerns a change of ONE coordinate of zeta_m (signature coordinates, where only u_{l'} moves). A move of z at a TARGET
coordinate j outside F ∪ Ba_j ∪ T_j ∪ ∪_{l in Sw_j} S_l changes several coordinates of zeta_m at once (all carriers whose targets contain
j) and does not touch the switching carriers, so it preserves exact d-neutrality exactly as a signature donor does. Its first-order
effect on Psi_m(theta_m; .) is
   d Psi = 2 sum_k lambda_k s_k u_k(j) dz_j [ A 1_P(k) - nu_k 1_Q(k) ]      (s_k := sgn u_k(zhat), one-sided at degenerate peaks),
which has either sign; at a FREE coordinate (|z_j| < 1) both directions are admissible, so one of them raises theta_m unless d Psi = 0.
REFEREE EXTENSION (SKETCH): a "target donor" for block m is such a coordinate with an admissible direction of positive one-sided
derivative; if, for the blocks of I_D, finitely many target donors give a combined move whose derivative vector is positive in every
block of I_D (a Gordan-type condition, like (FS) but now at a companion, where no quantitative size is needed), the proof of Proposition
Q goes through with Lemma T(e) replaced by the first-order expansion of Psi (all other changes are o(move)). So the genuinely open part of
(d) is smaller than the aligned corner: aligned blocks in which, in addition, no admissible combination of target moves outside the data
supports raises the threshold (e.g. at maximal contact, where only one direction is admissible at every coordinate).
