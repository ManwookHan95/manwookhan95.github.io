# 5. Consequences for the open core (F finite)

**Master Theorem III.**  PROVED modulo V1's Master Theorem II (V1_notes.md 4.3, unrefereed at the time of writing).
Design D^{V2} built on V1's D_Omega (Def. 2.2 and Def. 3.2 added; all of V1's estimates use only b(w) <= T_lo(w)^4/(l Design),
which still holds), diagonal U, F finite.  If for infinitely many levels l some clean sub-window w of level l satisfies
      rho^sh(kappa(w), f) >= u(w),
then f in Rec (every (f, g), g in C(f), is in cl NA((c_0, p_N), l_2^2)).
Proof.  V1's Master Theorem II has exactly two non-structural hypotheses at w: (SH_w) (shift sources or robust shift cost
c_pi(w) >= u(w)) and (VR_w) (every extreme ray of the zero-cost cone has at most one robust d-component).  (SH_w) is used only
through |Delta d_m| M_m <= K'_d t (V1 2.3, Lemma S); Theorem C1(I) provides this with K_sh <= C_f Design^3/u^3 whenever
rho^sh >= u, and the window arithmetic absorbs it (Q(w) = (4 Design/u)^{omega+3}).  (VR_w) is used only to bound the
d-row part of the Hoffman constant of the transplant (V1 Prop. TR step "blockwise ray removal"); Theorem B replaces it: V1's
z-move closings (C1), (C2) give a row f_1 satisfying (A1) (V1 Lemma ST(a): L_0 values move by <= (|T(l)| + 1) b(w)); V1's donor
raise (C3) is the move set M_ass of Theorem B; V1's linear tuning (C4) is replaced by the combined Lemma TU solve of Theorem B,
Step 3, with targets the Lojasiewicz point v' (which absorbs the second-order side effects C Design^2 Lambda^2 of the donor
banks on the L_0 values); V1 Lemma ST gives (A2) and the statuses at f^# (the extra moves 2 eta << c_f Lambda).  At f^# the
whole exact system has Hoffman constant <= C_f^l Design^2/u (Theorem B(d)); the transplant (V1 Prop. TR with the Hoffman
projection onto Sigma^# in place of the blockwise ray removal) gives exact d-neutral window data at f^# with
K <= (room product) x C_f^l Design^2/u x (pinning constants), and Theorem E'' of V1 (= Z3 Theorem E with window-dependent
c_flat and banked/pulled supports) concludes.  The extra cost C_f Design^2 eta log(1/eta) is o(T_lo^2).  QED
**Residual list (F finite, D^{V2}).**  PROVED (logical): f notin Rec only if, for all but finitely many levels, every clean
sub-window w has rho^sh(kappa(w), f) <= b(w) [(C*): an exact or b-near-exact d-constrained coherent shift resonance in some
block lacking a shift source].  Compared with ADDENDUM 6: (A) assembly — V1; (B) multi-block rays — REMOVED (Theorem B);
(C) — reduced to (C*) (Theorem C1), with the structure of Part 4; (D) aligned corner — V1 5.1 (pulls on the peak), and
independently Lemma QB + Lemma 2.3 give a raise in every block (two-sided tuning of a robust buffer peak).
**What (C*) looks like (PROVED pieces, Part 4).**  A block lacking a source (all robust coarse peaks of one swallowing type,
plus a class-G strict non-peak of the opposite d-sign whose switching is zero-cost) in which the shift trace of the peaks is
compensated exactly, at the coarse level, by zero-cost switching satisfying the d-identity.  Mates using it with oscillating
profiles (Prop. C4) need data with Delta d != 0 (configuration (ii): Delta >= 0, Corollary cor:D1 applies; configuration (i):
Delta < 0, needs (SC)), which at a companion require exact cancellation of the fine contributions on the coarse free
coordinates (Prop. C3, Cor. C3.1(b)); the fine tail itself is completable (Lemma C5).  At maximal contact (C*) does not occur
(Cor. C3.1(c)).

# 6. Numerics (V2_work/, sanity checks only)
hoffman_minors_check.py: Lemma H on 300 random systems x 5 points (1500 tests, rows partly dependent / with equalities):
max dist/(bound (1.1)) = 1.0000 (attained for single active rows), max (1/sigma_min)/(minor bound (1.2)) = 1.0000; two-ray
example: dist_1/|D tau|_1 = 2/delta for delta = 1e-1 ... 1e-4 and <= 1/2 at delta = 0 (exact degeneracy is harmless).

# 7. Next steps
1. Referee Theorem B (in particular Step 4 against V1's Lemma ST, and the claim that the minors of every exact system used by
   an assembly are polynomials in the L_0-values up to row factors) and Theorem C1 (the list (R1)-(R7) and its errors).
2. (C*): (a) an approximately-two-piece Corollary D1 / Theorem E tolerating errors of l_1 mass <= |Delta| T_lo^3 localized on
   finitely many coarse free coordinates (they are fine-origin: below the window they are dominated by the scale only if the
   cushion is supplied — investigate tiny near-contact moves z_j -> z_j +- O(T_lo^3) at those coordinates, which change coarse
   values only by O(T_lo^3) and might turn the residual identities into one-sided conditions); (b) block-scalar
   exactification (two-parameter tuning of (theta_m, A_m) by a peak push and a non-peak push: Jacobian determinant
   rho_k M/Phi_P^2 > 0, computed in Part 4 notes as a remark) for Theorem C6; (c) decide whether persistent oscillating
   shifts at all levels are compatible with partial contact at all (a structure theorem would close (C*)).
3. Infinite F (item (E)): Theorem B and Theorem C1 are local in the level and should transfer to Y3's infinite-F framework.
