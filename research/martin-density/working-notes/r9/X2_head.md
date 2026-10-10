# X2 notes (Round 9): (S2) uniform composition with d-CONSISTENT engineered approximants, and (C_mix) mixed activity classes, F finite

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; notation as there), finite block set I = {1..N}, p = p_N, diagonal base (T_final's
mu-base), design D^{U1'} of U1-ref on U4's T_final, enlarged to D^{X2} by two ladder conditions (D-lev), (W_exp) (6.1).  Labels PROVED /
SKETCH / HEURISTIC / FALSE / OPEN; "PROVED" = complete proof here using only refereed results (listed where used).  This file = X2_head +
X2_part1 ... X2_part6 (byte-identical copies).  Scripts and outputs: r9/X2_work/.
No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN; the F-finite residual is reduced to U1-ref's
status-coherence problem ((KN) failure), which is the X1 task.

## 0. Summary of the answers
(1) (S2a') d-consistent engineered approximants: CLOSED.
    * Proposition J (PROVED): for VALID data (Gamma_w <= 2) the theta/+- junction mismatch kappa^+- = -+(rho/2)(d' - d)(Domega) of
      thm:engineered is <= C_f |Omega_m|^{1/2} (||X|| + t(N'')), uniform in the piece scale t (U1 Lemma 2.1 bounds ||D Domega||_2; the diagonal
      base bounds the mass effects by the mass vector X).  U3-ref F6a's order s_1/t^2 was computed for a datum scaled by 1/t whose Gamma_w grows
      like t^{-2}; but the conclusion stands in a different form: the mismatch is NOT uniform along WINDOWS (||X|| carries the masses of all
      n pieces, |Omega| grows with the level), so with fixed transfer inefficiency the rebalancing fails — an exact cancellation is needed.
    * Lemma DC (PROVED): exact d-consistency (nv'_k = nv_k on the finite switching set Omega, hence d' = d on every switching vector, kappa = 0)
      by levers (TU pulls + banks, zero-data z-moves/banks, absorber tuning masses).  The linearization is I - p q^T (rank one, through the
      block norm) with 1 - q^T p >= 1 - C_m >= 1/2 (Sherman-Morrison), plus a block-triangular absorber coupling; Poincare-Miranda gives an
      exact zero.  Lever sizes O(||X||).  Lemma LV (PROVED): such levers exist at U1's companions (design addition (D-lev)).
    * Lemma UE-1 + Theorem UE (PROVED, line-by-line modification of the refereed proof of thm:engineered and of U3's Lemma VT): uniform
      per-piece bounds p*(f' + tau g'_i) <= 1 + (tau^2/2)(1 - delta) for |tau| <= c_flat t_i, c_flat an f-constant (window-dependent only through
      gamma_B, as in V1), with explicit late threshold s_late (a window quantity); lever sizes are checked against the data at lever coordinates
      (zero data, contact-like data, or pull masses 24 lambda v dominating c_flat t |data|); the scrambled-set bound is explicit
      (S_m <= K_w Pi^2 log(e/Pi) + 4m(C_S (K_w Pi)^2 + s_1^2 T^4), second order in the perturbation size Pi <= K_w s_1).
(2) (S2b) averaging at the norm-attaining approximant: Theorem E^eng (PROVED) — Theorem E's averaging run AT the engineered approximant with
    the per-piece bounds of Theorem UE; no exactness of the averaged data, no final call of cor:D1.
(3) (S2c) threshold comparison: PROVED with the design addition (W_exp) c_{l+1} <= exp(-1/T_lo(l, M(l))); (W10) alone does not suffice for
    the late threshold obtained here (s_late ~ T^{15}: gap_min ~ T^4 enters K_w squared; (W10) gives violations ~ T^{10}).
(4) (C_mix): CLOSED (Lemma CM, Theorem C_mix, PROVED): in a mixed class, complete the fine structure by self-aligning every negative fine
    carrier (state (R): explicit (SC)) and anti-aligning positive ones; the only violations are fine-origin contact violations of mass
    <= 4 C_Delta c_{L+1}, tolerated by Theorem UE; frustration is harmless; no exact completion is needed.
(5) MASTER THEOREM V (F finite, design D^{X2}; PROVED modulo the refereed tools it cites): f in Rec(p_N) whenever, for infinitely many main
    stages L, some clean sub-window has >= n(w)/D_cls(w) scales in activity classes (one-signed OR mixed) satisfying (KN_{w,a}).  Hence the
    F-finite residual is: (C*) rows at which, at all large main stages and all clean sub-windows, almost all scales lie in classes violating
    (KN) — U1-ref's status coherence (OPEN).

## Results table
| # | Result | Label | Where |
|---|---|---|---|
| 1 | Lemma M1 (masses off/on the support, diagonal base) | PROVED | 1.1 |
| 2 | Corollary M1' (mass vector of an engineered approximant) | PROVED | 1.2 |
| 3 | Proposition J (junction mismatch for valid data: O(|Omega|^{1/2} ||X||), uniform in t) | PROVED (upper bound); attainment HEURISTIC | 1.3 |
| 4 | Definition / identities of d-consistency (d' = d on Omega, gap identity (1.1), H' = (C/C')H) | PROVED | 1.4 |
| 5 | Lemma M2 (uniform neighborhoods, transfer data) | PROVED | 1.5 |
| 6 | Lemma DC (exact d-consistency by levers; rank-one linearization; Poincare-Miranda) | PROVED | 2.2 |
| 7 | Lemma LV (levers at U1's companions; design addition (D-lev)) | PROVED | 2.3 |
| 8 | Lemma UE-1 (explicit estimates at the d-consistent approximant) | PROVED | 3.3 |
| 9 | Theorem UE (uniform violation-tolerant engineered bound, T_0 = c_flat t) | PROVED | 3.4-3.5 |
| 10 | Theorem E^eng (averaging at the engineered approximant) | PROVED | 4.1 |
| 11 | (S2c) threshold comparison under (W_exp) ((W10) does not suffice for the s_late obtained here) | PROVED (arithmetic) | 4.2 |
| 12 | Lemma CM (self-aligned completion of mixed classes) | PROVED | 5.1 |
| 13 | Theorem C_mix (mixed classes recovered under (KN)) | PROVED mod refereed tools | 5.2 |
| 14 | Design D^{X2} admissible, N-free, refereed results survive | PROVED (by inspection) | 6.1 |
| 15 | Master Theorem V and its contrapositive (F-finite residual = status coherence) | PROVED mod refereed tools | 6.2 |
| 16 | Precision of U3-ref F6a; U1 Cor. IV.2 superseded; (S1), RT*(c) absorbed | PROVED | 6.2-6.3 |
| 17 | Status coherence without (KN) | OPEN (X1) | 6.2 |
| 18 | Numerics (Prop J scaling, exact tuning, Jacobian I - pq^T, UE bound in a finite model) | sanity checks | 6.4 |

## Dependencies (refereed)
Note: lem:threshold, lem:bookkeeping, lem:base, lem:block, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence, def:engineered,
lem:approxfacts, lem:F1, lem:anchor, def:SC, lem:scrambling, thm:engineered (proof), lem:slack, prop:reduction, prop:continuity, prop:smooth.
Z3 Lemma 3.1 (companion cost), Theorem E (structure of the averaging).  V1: Lemma B, Lemma TU, TR(iii)-(iv), Lemma ST, Lemma CO, Theorem E''
(window-dependent c_flat).  V2: MT III'.  U1: Lemmas 1.1, 1.3, 2.1, 2.4, 3.2, 3.3, 4.1-4.6, Proposition 2.2, 3.4 (with U1-ref's fixes:
Proposition KN, G1 release, (X4), D^{U1'}, Lemma 4.2(ii)).  U3: Lemma VT (U3-ref verified).  U4: T_final, Lemma GW.
