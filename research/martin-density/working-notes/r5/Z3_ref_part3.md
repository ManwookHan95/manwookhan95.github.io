# Z3 referee, part 3 — Z3 parts 5-6 ((O1)(ii); peak-ification)

## 3.1 Observation 5.0. CORRECT.
With B finite, every quantity of Theorem thm:S involving bad carriers is a finite min/max: 1/(sigma|alpha(k(l))|) in Lemma
lem:badpeaks(c), gamma_B in Lemma lem:windowtwopiece, the Hoffman constant of a fixed finite system. Weak/near-threshold GOOD carriers
never matter (pinning uses rooms only; the window certificate clamps). So weak/near-threshold carriers are new only for B infinite.

## 3.2 Lemma 5.1 (inward block moves need no gap). CORRECT (any admissible T). Re-derived:
D W(s) = (1 + dsM/C) Dw + s h_perp, ||DW|| <= Y + s^2||h_perp||^2/(2Y), Y >= C/2, C/Y <= 1 + 2|ds|M/C. Sup norm: off supp omega
|W| = (1 - ds)|w| with equality (1 - ds)M at the peaks with alpha != 0 (they exist since ||alpha||_1 = 1 and are not in supp omega);
strict non-peaks need |s omega| <= gap/2 and 1 - ds >= 1/2; at k_0: varsigma W(k_0) = (1 - ds)|w(k_0)| - |s omega(k_0)| in
[-(1-ds)M, (1-ds)M] by the inward and no-overshoot conditions. First-order term: <W - w, zeta>/sigma = s omega(k_0) alpha(k_0) = 0.
Extensions (checked): finitely many inward coordinates (degenerate peaks or strict non-peaks, each inward with no overshoot) work
identically, and Lemma U / Lemma lem:onesidedtransfer extend (Lemma lem:TV is unaffected because ||W - w||_inf < gamma preserves signs on L).
Z3's numerics (check_inward.py) are consistent. My check of the multi-coordinate extension (Z3_ref_work/check_inward_multi.py: 3000
random blocks, two degenerate peaks and two strict non-peaks of gap 1e-6..1e-3 moved inward with no gap condition, plus two ordinary
non-peaks): max[(N(W) - 1) - bound] = 2e-16, max |<W - w, zeta>|/s = 3e-13, ||W||_inf = (1 - ds)M exactly.

## 3.3 Identity 5.2 (d-shift with bad peaks). CORRECT. Re-derived from (eq:didentity), Lemma lem:modswallow(a) and (eq:peakshift):
for a bad peak q_l = eps_l Phi varsigma_l M/(mC) and varsigma_l eps_l tau_l/lambda_l = Delta d M + e_l, hence q_l tau_l = (Phi^2 M/C)(Delta d M + e_l).
Requires B finite with l_* >= max B (no fine bad terms), as stated.

## 3.4 Theorem 5.3 (weakened (H2)/(H3), B finite). CORRECT.
I checked that (H2), (H3) enter the proof of Theorem thm:S only through Lemma lem:badpeaks (a) [used again in Lemma
lem:windowtwopiece(b) for |Delta d|M and the coarse peak terms], (c), and the peak rows of the violation estimate in Lemma lem:exactswitch.
(A_m): Lemma lem:badpeaks(a) holds by (H2) at m. By 5.2, sum_{bad peaks}(Phi^2M/C)e_l = -sum_{np} q tau - Delta d M(1 + S_P) + r'; with all
q >= 0, -sum q tau <= sum q (tau)_- and (tau_l)_- <= c(tau)/(2 m_l) = O(K_* t) (cost function of Lemma lem:exactswitch, valid without
(H1)); all e_l >= 0, so each e_l = O(K_* t)/Phi_l^2 and, at a degenerate bad peak with varsigma = eps, tau_l = lambda_l(Delta d M + e_l) =
O(K_* t) (constants depend on the finitely many Phi_l). The q >= 0 hypothesis is exactly what bounds -q tau from above (tau_+ is only
box-bounded). (B_m): with q = 0 on bad non-peaks, 5.2 gives |Delta d|M (1 + S_P - (M/C) sum_deg Phi^2) <= O(K_* t) in the case Delta d < 0
(non-degenerate bad peaks: e_l <= t/(sigma|alpha|); degenerate ones (varsigma = -eps): e_l <= (tau)_-/lambda + |Delta d|M), and trivially
when Delta d >= 0; the coefficient is >= 1. The d-row of block m is then vacuous. Everything else in the proof of Theorem thm:S is
unchanged. Minor: "O(t)" in the notes should read O(K_* t) (harmless; K_* is the window constant).

## 3.5 Theorem 5.4 (infinitely many bad peaks). CORRECT.
Checked: Lemma lem:modswallow(a),(b) and the unified triangular system need only z = eps_l on S_l \ F and (H1); Lemma lem:badpeaks(a)
with K_d <= C + K_*/lambda_{l°} <= C'K_* (the notes' "K_d fixed" means: up to the factor K_*, which is how it enters K_pk); non-degenerate
bad peaks: |tau_l| <= t/mu_{k(l)} + lambda_l K_d t (by (eq:margin), sigma|alpha(k)| = lambda_k mu_k); degenerate (varsigma = -eps):
tau_l <= lambda_l K_d t and sum (tau_l)_- <= K_* t. Projected data tau' = (tau)_+ on B_np, 0 on B_pk: V' z-signed in K (resonance), d-rows
vacuous (q = 0 on B_np, tau' = 0 on B_pk), ||Delta B 1_{F^c} - V'||_1 <= K_pk t; Lemma lem:windowtwopiece goes through (bad coarse peaks:
omega^+ = 0, lambda rho_k <= |tau_l| + lambda|Delta d|M; B_np gaps equal M). (W*_pk) gives K_pk T_hi -> 0 and n^w/K_pk -> infinity.
"Inverse margins enter additively": correct and a genuine improvement over a triangular treatment.

## 3.6 Section 5.5. (i) CORRECT (peak data are inward on both sides by Lemma lem:suplevel(c)). (ii) SKETCH — coherent:
at f^#_j the former degenerate peak is a strict non-peak of tiny gap; inward data need no gap for Lemma U (3.2 above); Corollary cor:D1 is
applied at each fixed f^#_j, where a tiny gap only shrinks T_0(f^#_j), which is allowed; the tuning perturbation on a fine good
signature set S_{l'} (l' > l_*) does not change u_l(zhat) for coarse l (allowedness (a)) and costs -> 0 as l' -> infinity. Missing, as
stated: a first-order statement that some such perturbation moves vartheta_m in the required direction (it does not follow from
what is written; the clamp equation can move vartheta_m either way). Also needed: (BS)-type status preservation of the other coarse
carriers under the tuning (fine for small shifts unless another coarse carrier is exactly degenerate).

## 3.7 Section 5.6 (OPEN items). Accurate. (b) "exact two-piece data need Delta d_m != 0, impossible when block m has a good carrier with
w != 0": correct (R_m^* w_m carries the good signature mass on roomy sets).

## 3.8 Proposition 6.1 (peak-ification). SKETCH — correct as labelled; the PROVED sub-case is fine.
Checked: pushes on S_l (l >= L) are invisible to u_{l''} for l'' < l (allowedness (a), disjointness), so |u_l(zhat_L)| >= A_l survives
later pushes; choosing the push sign sigma_l maximizing sum v_l(s)(1 - sigma_l z_s) (>= ||v_l 1_{S_l\F}||) gives the needed range
[0, delta°_l] for x_l (the notes' "carry v_l-mass >= ||v||/2 ... after shrinking kappa" is imprecise; measure the available push by
sum v_l(s)(1 - sigma z_s), which is >= ||v_l 1_{S_l\F}|| for the better sign); (D*) needs c_l(3 theta + psi_l) <= delta°_l/8, i.e. (D*)
with psi replaced by psi + 3 theta (harmless); p*(f_L - f) -> 0 by Lemma 3.1 (Delta <= 2 sum_{l>=L} lambda_l, so |theta^L - theta| <= C
sum_{l>=L} lambda_l: no logarithm needed); (MS) at f_L holds because psi_l -> infinity and Phi decreases (super-)geometrically along each
block. The status of the finitely many l < L is preserved when sum_{l>=L} lambda_l = o(min_{l<L} margin/gap terms); the notes' sufficient
condition is correct. In general exact degeneracy at f_L must be avoided by a genericity argument that is not written: SKETCH.
(D*) "can be arranged": plausible (choose S_l recursively avoiding earlier target supports, with min S_l bounded in terms of c_l; the
admissibility proof then goes through because allowedness (a) only requires later S_{l'} to avoid earlier targets). For natural choices
(e.g. S_l = prime powers) (D*) holds automatically, since c_l <= T_lo(l-1)^3 <= 2^{-6/delta°_{l-1}}.

## 3.9 Corollary 6.2. CORRECT but nearly tautological (Lemma Z is per mate; G-approximants exist by 4.2 / 6.1). The phrase "every such
approximant is a companion of f at distance >~ c_L log(1/c_L)" is a LOWER bound that is not proved (Lemma 3.1 gives upper bounds): HEURISTIC.
