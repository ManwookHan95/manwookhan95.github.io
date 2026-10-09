# Z3 notes (Round 5) — case (O1) of Remark rem:openZ: approximate swallowing and inexact free carriers

Setting: canonical base, finite block set I = {1..N} (p = p_N; Lemma lem:martintail transfers to Martin's p), the note
paper/martin_density_note.tex is the reference (numbering and notation). Parts 1-2 and Lemmas 3.1, 5.1 hold for every admissible T;
the rest is for the signature-ladder design T of Definition def:SLD (part 6 uses a harmless strengthening (D*) of the design).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Part files: Z3_part1..6.md (assembled below). Scripts: ctx/r5/Z3_work/.

## 0. Summary

**(a) "Approximately two-piece" Corollary cor:D1 — what is true.**
* At f itself NO first-order defect proportional to the scale is tolerable (Remark 1.5, PROVED as a statement about the bounds): data with
  defect D certify nothing below scale ~D, window data have D ~ t, and averaging AT f creates a kink of slope ~ T_hi/n. With fixed data,
  the engineered construction tolerates only defects below a positive threshold ~ T_0^2 (SKETCH). Wrong-signed contact mass that is NOT
  forced by the representation is already harmless (Lemma lem:split puts it into the l_1-small remainder); the genuine defect is
  switching through a carrier vector u_l whose signature set is only approximately swallowed.
* **The correct "approximate" version moves the first row (Theorem E, PROVED).** Exact two-piece data may live at a nearby first row
  f_j (same base support), built on a window of n_j dyadic scales, provided p*(f_j - f) = o((bottom of the window)^2) (scale decoupling)
  and the usual window conditions K_j T_j -> 0, n_j/K_j -> infinity hold; windowed averaging is done AT f_j (the mate g of f enters only
  through the zeroth-order error p*(f_j - f) at scales above the window), and Corollary cor:D1 is applied AT f_j.
* **Transplant (Proposition T, PROVED).** Window decompositions of g at f become exact d-neutral two-piece data at a coarse
  exactification f^# (contacts raised/flipped on the approximately swallowed coarse signature sets) with frozen error
  O((1 + C_H^#)(K_* + theta) t), provided: pinning at f off the exactified carriers, block stability c(delta) <= theta T_lo^2, and a
  Hoffman bound C_H^# for the companion cone. Two new identities drive it: raising/flipping converts the first-order defect of the
  switching EXACTLY into a d-mismatch at the companion (Lemma 1.2, Corollary 1.3), and the cost of a companion is governed by the
  UNWEIGHTED quantity sum_k min(lambda_k, |u_k(delta)|) (Lemma 3.1; numerically necessary, part 6).
* **Exactly which defects are tolerable:** those whose exactification cost c(delta) is o(T_lo^2) on windows where all other coarse carriers
  are pinned within the window budget and the companion cone is well conditioned. Two intrinsic limits (PROVED, as statements about
  the method): (i) the BAND — a carrier with room r_l, T_lo^2 << r_l << 1/K, can be neither pinned (needs n >~ 1/r_l) nor exactified
  (needs r_l << T_lo^2 = 4^{-n} T_hi^2); every design has band carriers for suitable f (rooms ~ 1/n(l)^2); (ii) a d-neutral carrier with
  positive room cannot be both exactly resonant and d-neutral at any companion with the same base part (Lemma 1.4): its companion cone
  is degenerate, Hoffman constant >~ 1/r_l (re-tuning the Hilbert part: SKETCH).

**(b) Application to (O1).**
* (O1)(i) near-contact tails / far sign changes: on FINITELY many signature sets always recovered (Proposition 4.1, by Theorems thm:Bpm,
  thm:S); the obstruction requires infinitely many carriers with super-geometrically decaying relative rooms. Then: recovered under
  "tower gaps" of the room sequence with good companion cones (Corollary 3.4, 4.3(i)); Lemma Z at such f reduces to lower
  semicontinuity along the far lowerings f^L in R_0^+- / R_S (Proposition 4.2) — i.e. (O1)(i) is a quantitative case of (O2); the band
  (4.3(ii)) is the precise remaining step (4.4). OPEN.
* (O1)(ii): weak bad peaks and near-threshold bad strict non-peaks matter only for infinitely many bad carriers (5.0, PROVED). Infinitely
  many bad PEAKS are recovered when inverse margins are window-summable (Theorem 5.4, PROVED: peak pinning is additive). Failure of (H2)
  is harmless when the bad strict non-peaks of the block are d-neutral, and failure of (H3) is harmless when the bad strict non-peaks of
  the block have weights q >= 0 (Theorem 5.3, PROVED, via the d-shift identity 5.2 and Lemma 5.1: inward block moves need no gap). The
  general (H3) case reduces to a tuning lemma (5.5, SKETCH). Remaining: infinitely many non-d-neutral bad strict non-peaks; (H2)-failing
  blocks with non-d-neutral switching (exact two-piece data impossible; shifted data needed) — OPEN (5.6).
* Structural: for the (slightly strengthened) SLD design, (BT) points are dense among finitely supported first rows (6.1, SKETCH:
  genericity step), so Lemma Z is a pure lower-semicontinuity statement along explicit approximants in G (6.2).
* No counterexample; nothing found points to one. Density remains OPEN.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Effective contact set at scale t (budget on N_theta, wrong-signed mass O(t)) | PROVED | 1.1 |
| 2 | d-coefficients through the normer; defect identity at companions | PROVED | 1.2 |
| 3 | Raising/flipping converts the first-order defect into a d-mismatch (>= 0) | PROVED | 1.3 |
| 4 | Approximate resonance vs d-neutrality at companions (degenerate cones) | PROVED | 1.4 |
| 5 | No defect proportional to the scale is tolerable at f; kink of averaged defect data | PROVED (bounds) | 1.5(a,b) |
| 6 | Fixed data in Thm thm:engineered tolerate defects below ~ T_0^2 (s_1 may stay fixed) | SKETCH | 1.5(c) |
| 7 | Uniform one-sided transfer expansion along f_j -> f | PROVED | 2.1 |
| 8 | **Theorem E**: windowed recovery through nearby first rows (scale decoupling eps_j = o(T_lo^2)) | PROVED | 2.2 |
| 9 | Cost of a companion: l_1-change of block functionals <= C[Delta log(e/Delta) + sum min(lambda_k,|u_k(delta)|)] | PROVED (+num.) | 3.1, 6.3 |
| 10 | Budget of the actual decomposition at a companion | PROVED | 3.2 |
| 11 | **Proposition T**: transplant of window data to coarse exactifications | PROVED | 3.3 |
| 12 | Corollary: exactification windows => f in Rec | PROVED | 3.4 |
| 13 | (O1)(i) needs infinitely many carriers with super-geometric room decay | PROVED | 4.1 |
| 14 | (O1)(i) reduces to lsc along far lowerings (f^L in R_0^+- / R_S) | PROVED | 4.2 |
| 15 | Tower gaps suffice; band obstruction; d-neutral companion obstruction | PROVED (method) | 4.3 |
| 16 | Re-tuning the Hilbert part for d-neutral approximately resonant carriers | SKETCH | 4.3(iii) |
| 17 | Remaining (O1)(i): band carriers / lsc along far lowerings | OPEN | 4.4 |
| 18 | Weak/near-threshold carriers matter only for B infinite | PROVED | 5.0 |
| 19 | Inward block moves need no gap (one-sided block resources) | PROVED (+num.) | 5.1, 6.3 |
| 20 | d-shift identity with bad peaks | PROVED | 5.2 |
| 21 | Theorem S under (A_m) [(H2)+(H3')] or (B_m) [(H2'')+(H3)] per block | PROVED | 5.3 |
| 22 | Theorem S with infinitely many bad peaks, window-summable inverse margins | PROVED | 5.4 |
| 23 | (H3) failure via tuning companions | SKETCH | 5.5 |
| 24 | Infinitely many non-d-neutral bad non-peaks; (H2) failure with non-d-neutral switching | OPEN | 5.6 |
| 25 | Peak-ification: (BT) points dense among finitely supported first rows (design (D*)) | SKETCH | 6.1 |
| 26 | Lemma Z = lsc along explicit G-approximants | PROVED given 4.2 / 6.1 | 6.2 |

