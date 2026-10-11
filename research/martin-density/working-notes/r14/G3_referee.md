# Referee report on G3 (Round 14): persistent residual rows -- universal switching constraints, self-pinning, construction attempt

Refereed: r14/G3_notes.md (authoritative), G3_part1-3.md and G3_work/ (scripts re-read, outputs consistent).  Checked against: BRIEFING_R2
Addenda 11-13; r13 H1/H2 referee reports and ref notes (Lemma SLP, F-NE, F-COR, P-41, P-52); r14 G1_notes + G1_referee (Lemma CH,
Lemma 2.1, Def. 3.2 strict/soft, Cor. 5.4, Theorem G1.D, (R-S1)-(R-S3)); G2_referee (Theorem ML', Theorem 4.9'); K2_notes 5.3 (kinds,
K2.16); Part I block-threshold structure.  Proofs of every verdict, fix and referee addition: r14/G3_ref_notes.md (part files
G3_ref_part1-3.md).  Scripts and outputs: r14/G3_ref_work/.  Role: adversarial referee.

## 0. Bottom line
G3 constructs no persistent residual row and claims neither density nor a counterexample; that bottom line is correct.  Its
method-independent norm-level results are all correct: Lemmas 1.1-1.7, Theorem CL, Corollaries CL.1, CL.2 and 1.8, Theorem 2.10,
Corollary 2.11 and Lemma 2.8.  I re-derived each one by hand.  An independent two-block implementation checked every inequality
with exact terms on 160 random decompositions, and the worst slack was 2e-17.  The interpretive and constructive parts have five
problems.  None of them affects a PROVED lemma.
 G-RCL (RC_L is obsolete).  RC_L and (C3) rest on a tiny wrong-signed minor of the value row and a common target CONTACT row.  G1
   Cor. 5.4 is refereed correct mod chain and names "G3 (C3)".  It shows that this configuration does not obstruct: the contact
   row is banked and cushioned, so the minor is soft.  A persistent residual has to be built on STRICT resonances ((R-S1)-(R-S3),
   (R-L), (R0^str)).
 G-THIN (Interpretation (b), the Section 6 reading and RC_L).  The conclusion "persistent (R1) in unshifted blocks needs shared THICK
   target support" drops an escape G3 itself lists: thin support below its cushion scale.  Window bottoms satisfy
   s_1 <= theta_0 T/(8 rho A_0) << theta_0 <= b.  So any shared support of mass >~ K_* s_1^2 H(L) is an escape at the bottom of
   every window, and "thick" holds only relative to the scale.  Tiny shared support is not a TS generator, so the tuning-lever
   duality of 4.4 does not cover it.  In the method these rows are cushioned (G1), so G-THIN creates no new residual; it removes
   the claimed localization.
 G-NU (persistence sketch).  Tuning masses act through the GLOBAL normalization nu = ||U^* a||.  The formula is
   d zhat_s/d a_{s*} = -mu_s^2 a_s mu_{s*}^2 a_{s*}/nu^3.  Suppose a stage minor's Hilbert part is not proportional to its own
   effect c_L.  This happens with a coarse thick coordinate, or with thin support not small compared with c_L, whose size the
   adversary fixes through the depth of s*(L).  Then cross effects are O(1) relative to own effects, and the weight conditions of
   Lemma 2.2 fail for large L.  In the pure product case they hold with geometric weights.  Repair (SKETCH): a rank-one reduction.
   Fix nu, solve the triangular system, then solve the scalar equation for nu by the intermediate value theorem.
 P-33 (Prop. 3.3 / the obstruction).  For contact minors the tolerance is the bank cushion 2 theta_min/t of G1 Lemma 2.1(a), not
   VT, so the obstruction is moot there.  It applies to strict FR minors (tolerance (VT')).
 Precisions:
   - P-29: Cor. 2.9's constant depends on v_0 and C_v, which are f-data.  Design control holds via Cor. 2.11.
   - P-16: the Reading after Cor. 1.6 ignores the near cushion at window scales.
   - P-211: Cor. 2.11's constant is relative to r_Q, Psi and eta_P.
   - P-53: slip in the scale-dichotomy threshold; it should read |M| < C_f s_2^min/(c delta).
   - P-34: Lemma 3.4's general sentence is HEURISTIC; only one move is analysed.
   - Cor. 2.4 also depends on its free-lever SKETCH.
   - P-NUM: G3's own model gives the pair two shared thick coordinates, so Lemma 2.8's disjointness fails there.  Only
     2.8(b),(c) are cleanly tested.
REFEREE ADDITION, Lemma R-ESC (PROVED; a sharpened form of Cor. 2.11).  It applies in an unshifted block.  Only the cushions of
SHARED coordinates and of ANTI-ALIGNED private coordinates enter.  Aligned private support of any mass never helps.  Minors never
enter.  An EXACT resonance without an escape is pinned at every scale.  For kind-(iv) groups (data-direction switching) the possible
escapes are four: shared support, outside switching, other switching strict non-peaks, or a shifted block.  Numerics confirm this
(N2, N3).
(LSC-trunc)_N for every f remains OPEN, as do density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2).  No counterexample is
claimed, and nothing found here points to one.

## 1. Verdicts
| Claim (G3 label) | Verdict | Main point |
|---|---|---|
| Lemma 1.1, 1.2, Cor. 1.3 (PROVED) | correct | attainment by weak*-compactness; each side's E_b <= (s-1)/q_0 |
| Lemma 1.4 (PROVED) | correct | (a) holds at free coordinates too; N1 |
| Theorem CL (PROVED) | correct | N1; P-CL1: thickness is scale-relative, cleanest form with T = F |
| Cor. CL.1 (PROVED) | correct | "in particular" is uninformative at window scales (total thin mass/t); stated correctly |
| Lemma 1.5, Cor. 1.6 (PROVED) | correct | P-16 on the Reading (near cushion at f, window scales) |
| Lemma 1.7 (PROVED) | correct | (P1) is a genuine hypothesis (weak/degenerate peaks uncontrolled); N1 |
| Cor. CL.2 (PROVED) | correct | two-regime confirmed with an escape (N3) |
| Cor. 1.8 (PROVED) | correct under alpha <= t^2 | only for contacts or t >= alpha^{1/2} |
| Theorem 2.10 (PROVED) | correct | any J_c; N1 |
| Cor. 2.11 (PROVED) | correct | P-211; sharpened to Lemma R-ESC (only anti-aligned private and J_c cushions) |
| Lemma 2.8, Cor. 2.9 (PROVED) | correct | P-29 (v_0, C_v in 2.9); Interpretation (a) true via 2.11; consistent with G1 Cor. 5.4 |
| Interpretation (b) of Section 3 | conclusion overclaimed | G-THIN |
| Lemma 2.1, Lemma 2.2 (PROVED) | correct (abstract) | application to RC_L: G-NU |
| Lemma 2.3, Cor. 2.4 (PROVED / conditional) | correct | 2.4 also conditional on its free-lever SKETCH; tail constant |
| (D-pat) (HEURISTIC) | label honest | must hold at every clean sub-window; the pattern set grows as windows shrink |
| Tuning-lever duality (HEURISTIC) | label honest | does not cover tiny shared support (G-THIN) |
| RC_L and its persistence (SKETCH) | label honest; target obsolete | G-RCL; extra unverified point (v) = G-NU |
| Lemma 2.6, Cor. 2.7 (PROVED, 2.7 conditional) | correct | -- |
| Lemma 3.1, Cor. 3.2 (PROVED) | correct | Fort + Bishop-Phelps re-derived |
| Prop. 3.3 and the obstruction (PROVED mod chain) | arithmetic correct; scope P-33 | contact minors: G1 cushions; applies to strict FR minors |
| Scale dichotomy (SKETCH) | label honest | slip P-53; part (i) never applies with the current bias |
| Lemma 3.4 (PROVED mod chain) | correct for the stated move; general claim HEURISTIC | P-34 |
| (Q*) (OPEN) | correctly stated | restrict to strict resonances |
| Persistent residual row; (LSC-trunc)_N; density (OPEN) | OPEN | -- |

## 2. Main findings
F1. The universal lemmas are sound and cheap.  Every one follows from three facts:
 - the weighted excess budget;
 - the coordinate inequality |x| - zx >= 2(zx)_-, (1 - |z|)|x|;
 - the level identity x_0 + sum x_m = 0.
 They hold for every admissible T, row, mate and scale.  The block threshold identity ||alpha||_1 = 1 is forced by
 M + C = 1 (ref notes A.1).
F2. Lemma R-ESC.  Theorem 2.10 never uses the private coordinates, so in Cor. 2.11's case (3) no private cushion appears.  In case
 (1) only the anti-aligned ones appear.  Consequences:
 - The data-direction switching of a deep-swallowed kind-(iv) group in an unshifted block is pinned at O(t)H(L) at EVERY scale
   unless E(t) is large.  E(t) is large only through shared support, outside switching at shared coordinates, other switching
   strict non-peaks, or failure of (P1).
 - An exact FR resonance with contact-only private coordinates is pinned (N2 (vi); N3 control: slope 1.13 for M = 0).
F3. G-RCL.  G1 and G3 ran concurrently.  G1's soft/strict split realizes exactly the configuration on which RC_L is built.  The
 adversarial target therefore moves to (R-S1)-type strict resonances.  By R-ESC their active groups also need an escape.  N3 shows
 the resulting picture: with a shared support target, the strict FR minor governs activity in the two-regime way of Cor. CL.2.
F4. G-THIN and P-CL1.  Thickness is relative to the scale.  At the window bottoms the method needs (s_1 << theta_0), every support
 coordinate of mass >~ K_* t^2 H(L) is two-sided for the mate.  N2 (iii) shows a pair pinned at t = .1 that switches with amplitude
 .9 at t = .003 through a shared target of mass 1e-3.
F5. G-NU.  The triangular-tuning lemma is correct.  Its use needs the global nu-coupling to be removed first, by the rank-one
 reduction.

## 3. Attacks attempted
- Hoffman constants and which rows they involve.  No G3 result uses a Hoffman constant.  The pinning constants are design masses
  (P_k, U_N), q_0, sigma and the outside terms (r_Q, Psi, eta_P).  Cor. 2.9 alone carries the f-data v_0, C_v (P-29).
- Does the transplant need only the face-wise bound?  Not used by G3.  Via G1, the rows of RC_L are cushioned (G-RCL).
- Scale constraints.  b, s_1, theta_0 and delta_Z were checked against (K2-d), (L-K2-1), (VT) and (VT').
  - s_1 << theta_0 <= b drives G-THIN.
  - The bias-to-VT ratio of Prop. 3.3 was re-derived: 512 rho C_d K_J Pi_X/(delta s_1).
  - (W_exp), (LATE) and S2c^tr are not touched by G3.
- Puiseux margin and (FC).  G3 builds no levers.  Not applicable.
- Counting.  RC_L needs a fresh pair at every stage.  Memory (H2 2.6/2.7) and (D-pat) make it a countable family of design
  conditions, which are not verified.
- Design changes.  (D-pat) is f-free and N-free (patterns over present blocks).  Well-foundedness needs choosing T_lo(w) after the
  level's signature weights; plausible.
- Signs.  Lemma 2.8's orientation bookkeeping and identity A val_- - B val_+ = D were re-derived.  The R-ESC sign split was checked
  term by term (check_resc).
- Quantifier order.  Design -> f (nested tuning) -> g, rho, t: consistent.  Companions are not used by G3.
- Persistence at ALL large stages.  Not established: RC_L is a SKETCH with points (i)-(iv) plus G-NU (v), and it is obsolete
  (G-RCL).
- Recovering approximant missed.  Yes for RC_L: G1's soft transplant (Cor. 5.4) recovers it, mod chain.
- Counterexample.  None.  At the norm level every resonance examined is either pinned (no escape) or carried by an escape the
  method treats softly; the strict-resonance-plus-escape configuration (N3) is the open case.

## 4. Numerics (sanity only; r14/G3_ref_work/)
- refmodel.py + check_universal.py: an independent two-block model; 40 instances x 4 decompositions.  All of Lemma 1.4,
  Cor. 1.3, Theorem CL, Lemma 1.7 Step 1, (i), (ii) and Theorem 2.10 hold (worst slack 2e-17).  One apparent alpha-structure
  violation was traced to a near-peak at 1.5e-6 below M.
- test_pin.py, test_pin2.py (N2): one pair with disjoint private supports, deep-swallowed far mass.  The table gives
  max gamma'_+ / t.

  | Variant | Result |
  |---|---|
  | Contacts | pinned, slope 1.27 |
  | Aligned thin private support | pinned at all t, slope 6.3; the anti-data direction is relieved |
  | Shared thin target, a = 1e-3 | relieved: gamma'_+ = .41 at t = .01 and .90 at t = .003 |
  | Free shared target, robust minor | pinned, slope 13.4 |
  | Free shared target, EXACT resonance, contacts | pinned, slope 2.25 |
  | Free shared target, exact resonance, thin near support | relieved, through anti-data switching of one carrier |

- test_fr.py, test_fr_ctrl.py (N3): free shared target plus a second shared coordinate s.  Values are max gamma'_+ at
  t = .1 / .03 / .01.

  | Second shared coordinate s | Result |
  |---|---|
  | Thick | M = 0: 1.38 at every t; M = 1e-2: 1.32 / 1.11 / .74 (two-regime) |
  | Thin, a = 1e-3 | .19 / .21 / .51 for every M |
  | Contact (control) | slope 1.13 for every M, including M = 0 |

- check_resc.py: Lemma R-ESC (1)-(3) checked term by term on 108 decompositions; all hold.
- G3's selfpin, tworegime and conserve outputs were re-read.  They are consistent with the bounds; P-NUM applies.

## 5. Single most valuable idea
The switching inequality (Theorem 2.10) combines the block's value row with the SUMMED sign constraints at the shared coordinates.
The result contains no minor.  Sharpened as Lemma R-ESC, it says that cushions decide whether strict non-peaks of an unshifted
block can switch: shared support and anti-aligned private support, plus outside switching.  The size of a minor never does.  An
exact resonance without an escape is pinned.  A residual strict resonance therefore needs BOTH a tiny strict minor AND an escape at
every large stage.  That is a sharper target for both a proof and a counterexample.

## 6. What remains open (precise)
(1) (LSC-trunc)_N for every f: OPEN.  Density of NA((c_0, p_N), l_2^2) for any N: OPEN.  Density of NA((c_0, p), l_2^2) for the
    Martin-type p: OPEN.
(2) The residual after G1 and G1-ref, refined by R-ESC.  It must hold at every clean sub-window and class of all large main stages.
    It consists of (R-S1) groups that have both of the following:
    - a tiny wrong-signed strict minor of one (X3) row and FR rows at free shared targets with robust room;
    - an escape: a shared support target of mass >~ K_* t^2/H(L) at the active scales, outside switching at a shared coordinate,
      or other active strict non-peaks.
    The other residual classes are (R-S2), (R-S3), (R-L) and (R0^str).
(3) The method-level use of R-ESC.2.  It needs a threshold gap between active and inactive carriers inside K1's class
    bookkeeping.  Not done.
(4) An explicit persistent residual row.  RC_L must be re-targeted to (R-S1) with an escape.  Persistence needs G-NU's rank-one
    reduction and G3's open points (i)-(iv).
(5) Making the scale dichotomy a theorem, with an absolute-error class in the transport theorem.  (Q*) for strict resonances.
    (D-pat) and the free-lever SKETCH of Cor. 2.4.

## 7. Required edits to G3
- Interpretation (b) of Section 3, Section 6 "norm-level reading": replace "shared THICK target support" by "shared SUPPORT targets
  of mass >~ K_* t^2/H(L) at the active scales, outside switching at shared coordinates, or other switching strict non-peaks"
  (G-THIN); add Lemma R-ESC (ref notes B.2).
- Section 4.2 (C3), 4.5 RC_L: note that contact-row resonances are realized by G1 Cor. 5.4; re-target the adversarial
  configuration to strict (R-S1) resonances with an escape (G-RCL).  Add unverified point (v): the nu-coupling, with the
  rank-one repair (G-NU).
- Cor. 2.9: "O(t) with constant C_v [...] depending on v_0 = min(val_+, |val_-|)"; the design-controlled claim via Cor. 2.11
  (P-29).
- Reading after Cor. 1.6: "pinned with 1/U_N when alpha(N_l) <~ t^2" (P-16).  Cor. 2.11: constant relative to r_Q, Psi, eta_P (P-211).
- Prop. 3.3 / obstruction: restrict to strict FR minors; contact minors use G1's cushion tolerance (P-33).
- Scale dichotomy: persistence threshold |M_L(f)| < C_f s_2^min(L)/(c delta) (P-53).
- Lemma 3.4: general sentence HEURISTIC (P-34).  Cor. 2.4: "conditional on the free-lever SKETCH and (D-pat)".
- Numerics: note that the selfpin model's pair shares two thick coordinates (P-NUM).
