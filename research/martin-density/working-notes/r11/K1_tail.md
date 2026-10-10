
# 5. Corrections and precisions to earlier rounds (recorded)
 (C1) Q2 Proposition 3.2 (SKETCH) claimed compatibility of the zero-switching faces with "Q1's class/cube pigeonhole (they are sub-patterns, so V2's
      minors cover them)".  Correct for the CLASS part (Lemma K1.2-K1.3, with thresholds enlarged by the Lemma-P constant, which depends on the
      window through 2^{J(w)}); NOT established, and HEURISTICALLY false, for the CUBE part (Remark K1.1').  Repair: drop the cube (Lemma K1.1).
      The constant is C_+ = 5, not C Design/u.
 (C2) Q2-refa C.3 ("bank with offset" block-norm lever is two-sided): FALSE (2.2).  The offset moves the base point along the lever column, so
      the degenerate direction forces the total lever position; with the base mass in the pre-row, |F(0)|_inf >= 2Kr|pi p_{m*}| - |F_orig(0)|
      violates Corollary 4.2's hypothesis K|F(0)| <= r/2 when 4K|pi p_{m*}| > 1.  Repair: TU on the peak (pull + bank), or (P3)/(P4) on the peak.
 (C3) Q1 Lemma CM^tr STEP B, X2 Lemma CM(a) (self-aligned negative fine carriers) and the G1 release: redundant in route V once (W_exp) holds
      (Lemma K1.S).  Q1 CM^tr(e) and Prop. BR's (U5) may be replaced by (U5') (coarse carriers only).  X2's (U5) hypothesis of Theorem UE is
      likewise only needed for coarse carriers when c_{L+1} << s_1.
 (C4) Q1-refa P2 ("order class -> Step A -> cube -> Step B") is moot for route V (no cube, no Step B): order class -> Step A -> data.
 (C5) U2 3.1(iv)/TR-inf's description of TU levers at infinite F needs pulls only for DATA-CARRYING carriers; zero-data carriers need one near
      off-F/thin coordinate (Z-con/Z-gen).  Far z-moves and offset banks are one-sided (2.0, 2.2).
 (C6) Q1/X1 KN^tr Step 4 restores kappa by peak pushes; only ratios are used downstream (cone in ratio form, Lemma K, true shift), so kappa may
      float, and the peak resources become optional BORDERING columns (2.4).  With common-mode resources the ratios of ALL coarse strict non-peaks
      must be tuned (first-order drift otherwise).

# 6. Numerics (sanity checks only; r11/K1_work/)
 offset_check.py -> offset_check.out: 2000 random exactly degenerate bordered systems N = I - g h^T - p q^T with a block-norm column -pi p and a
   bank offset m_0: the bordered solve has residual <= 1.2e-14; the total lever position (offset + adjustment) equals y^T F(0)/(pi y^T p) in every
   trial, independently of the offset; it is negative (infeasible for a bank) in 48.7% of the trials.  Supports (C2).
 deep_assign_check.py -> deep_assign_check.out: 4e5 random instances of the deep assignment with trace slack (part 1.5 (i)): the three claims
   |B_+ - b^+_1| <= f^+ + f^- + |Delta B - X|, s b^+_1 >= -A, s(b^+_1 - X) <= A + tr hold, maximal normalized violations -3.3e-10, 9.8e-17, 2.5e-16
   (rounding).  Supports Proposition K1.A (i).
 Finite models cannot exhibit the infinite-dimensional phenomena (deep raises, Lemma P, windows); the structural claims rest on the proofs.

# 7. What remains open (precise), and the interface with K2
 (1) The NON-LEVER-REGULAR rows (4.3): at all large main stages, at the clean sub-window and the selected class, the bordered lever systems are
     degenerate; every non-privately-tunable carrier is (U) or (S).  The (S)-part is Q2's (NDN2)/4.4(iv) (exact limit: Q2 Lemma 4.3 / U2 Lemma ND,
     a|_F proportional to a combination of signature vectors) -- item (O-c), task K2 (data-side bordering (R3-a), tolerance variant of UE^inf,
     or the cushion route).  The (U)-part is new: one-sided private levers; the ratio trick (2.7 Remark (1)) covers blocks whose (U)-ratios have
     one sign (SKETCH).
 (2) Design bookkeeping (D-K1) of the new rate objects (R-mod), (R-pat), (R-lev) -- a monotone enlargement (U4 Lemma GW), item (O-d) (K2).
 (3) Inherited: the once-refereed links of Q1's chain (U1-ref MT IV' tools, X1-ref KN^tr, X2-ref CM'/C_mix') and of Q2 (UE^inf, E^{eng,RT,inf}).
 (LSC-trunc) for every f, density of NA((c_0, p_N), l_2^2) (every N) and of NA((c_0, p), l_2^2): OPEN.  Combined with Q1 Theorem VI.2, Theorem 5.1
 gives: NA((c_0, p_N), l_2^2) is dense as soon as every (f, g, rho) with infinite base support is lever-regular or is recovered by K2's results
 in the non-lever-regular class.
