# Referee report on G1 (Round 14): exactness only where it is needed -- cushioned Hoffman lemma, strict/soft split, linear Step A

Refereed: r14/G1_notes.md (with G1_part1..5.md and G1_work/; scripts re-read, outputs consistent).  Checked against: Part III
(Def. III-pattern, III-cone, Lemmas III-Tblock, III-floorrow, III-Uscale, III-weightfree, III-CMtr and its proof, Prop. III-BR,
Lemmas III-nocube, III-count, Def. III-Tfinstage (S6), Def. III-windowinf, III-approxinf, Lemmas III-nocubeinf, III-deepraise,
III-track, III-nodeep, Prop. III-cushion, Def./Lemma III-prep, Def. III-designinf, Lemmas III-depthclean, III-late, III-costs),
Part II Def. 5.52, Lemma 5.53, Prop. 5.54; J1 Lemma J1.13 and J1-ref B.5, F-2; J2/J2-ref (FC); H1-ref (Lemma SLP, P-KN); H2-ref
(F-NE, F-COR, G-CPL, P-41, P-52, Q-1, Q-2); K2 6.4.  Proofs of every verdict and fix: r14/G1_ref_notes.md (part files
G1_ref_part1-4.md).  Scripts and outputs: r14/G1_ref_work/.  Role: adversarial referee.

## 0. Bottom line
G1 answers the Round-13 request for "a face-wise Hoffman bound insensitive to tiny minors" in a strong form, and its main
mechanism is correct.
 - Lemma CH (cushioned Hoffman lemma) is a correct piece of linear algebra: strict rows (equalities and strict inequalities) are
   made exact, cushioned rows are violated by at most (2^{n/2} mu/u)|x'|, with a constant depending on p, n, u only.  Exactness of
   strict tiny minors is genuinely necessary (two-ray example).  Re-derived; 600/600 independent random checks.
 - Theorem G1.A (soft transplant) is correct after three fixable repairs.  Every row at a banked S_th target coordinate (contact
   or raised tiny support) and every inward row carries a cushion (theta/t, resp. lambda gap/t), and I checked line by line that
   Prop. III-cushion, Lemma III-CMtr (c), (d) and Prop. III-BR use the cone point only through exact (X3), exact FR rows,
   single-variable sign rows, the cushioned signs and the closeness bound.  Hence exactness is needed only for minors made
   entirely of equality rows, and contact-row resonances (H2 Example 4.3, the configuration behind the persistent-(R1)
   candidates) are realized (Cor. 5.4).
 - Lemma LE, the isolated-minor Lemma 5.1, Lemma 5.5 and (NT_0) are correct; wherever the strict structure is single-(X3) the
   exactification and the near-threshold descent are linear.  The linear-scale bookkeeping (Lemma 3.3) is correct up to a constant.
Problems found (none changes a conclusion; all repaired in the ref notes):
 G-T2 (Def. 3.1 (T2), (T5), (E3) of Theorem G1.C; gap).  (T2) gives SYMMETRIC bands to two-sided rows of every block and (T5)
   fixes the (U)-rescaling s_m = 1 - 4 Des^{C_x} b.  In a protected (T)-block a band of width beta on an active row raises the
   protected floor statuses at FIRST order by up to Des^C beta ~ Des^C b/u, while the margin is c Des^{C_x - 1} b; since
   u(w) = b(w^-) <= Des(L)^{-4 omega(L)} for all but the first sub-window of a level, no absolute C_x suffices.  (E3) was checked
   at the targets, not at the realized point.  FIX: use the band set of Theorem H2.A / J1.15' (protected blocks: kind-(i) rows
   exact, K^- shrinking bands, K^+ locked, zero-data bands only under (J-e)); in (U)-blocks use F-2's joint selection of s_m.  This
   is the band set that Theorem G1.D actually uses.
 G-S2 (Lemma 5.1 used out of scope).  Lemma 5.1 treats ONE two-(X3) minor; the proof of G1.D uses it alongside single-(X3) minors
   of the same blocks.  Explicit model: all tiny minors <= b, all first cofactors of the two-(X3) minor robust (+-1/2), yet the
   joint exact set is at distance sqrt(b) (= 1e2..1e5 b) and Lemma 5.1's move destroys the single-(X3) exactness.  FIX: restrict
   Lemma 5.1 to the isolated case, read (R-S2) as "no compatible exact point of Z^str within Des^C b" (G1's own wording in the
   notes), and state Lemma 5.5 and Theorem G1.C for a general compact k-semialgebraic Z^str (their proofs never use affineness).
 P-W (window count of Theorem G1.A).  H_CH = p^{p/2} Lambda^p/(u/2) is ~ B^{p+3}, not a design power (Des/u)^C; Lemma III-count
   assumed an absolute exponent.  G1's "omega(L) >= 2^p because the rate scheme contains all minors" is not supported by that
   reason.  FIX: insert omega(L) >= 8(p(L) + 4)(L + 1) + C_K + 8 (f-free, N-free, monotone); the count then closes.
 P-A1 (closeness clause of G1.A).  (E3)'s |r^# - r(f)| <= u/(4 Lip) does not give the claimed violation bound; the proof uses
   Des^C b.  FIX: require |r^# - r(f)| <= eta'(w), as in J1.13 (i).
 Precisions: P-N (row normalization in Lemma CH costs u -> u/(2 Des^{1/2})), P-23 (C_T fixed after C_A, C_x, C_Lip, C_r), P-L1
   (theta_pr >= 64 rho A_0 s_1/T, Part III's (L1)), P-44 (Lemma 4.4: M is multiplied by 1 - dkappa/kappa, not unchanged; needs no
   other ratio-dependent row -- true for strict minors), P-52' (Prop. 5.2's "iff" only in the restricted linear model; realization
   needs margin, as H2-ref P-41), P-54, P-55, Q-1 (G1.D quantifiers: every clean sub-window and class), P-CH1-3, P-21a/b, P-B.
(LSC-trunc)_N for every f, and density of NA((c_0, p_N), l_2^2) and NA((c_0, p), l_2^2), remain OPEN, as G1 states.  No
counterexample is claimed, and nothing found here points to one.

## 1. Verdicts
| Claim (G1 label) | Verdict | Main point |
|---|---|---|
| Lemma CH (PROVED) | correct | re-derived; |B| <= n gives the sharper n^{n/2}; the Lambda^p pigeonhole factor is real (numerics) |
| Remark CH(c), Cor. CH.1 (PROVED) | correct | two-ray example; Lipschitz transfer; normalization P-N |
| Lemma 2.1 (PROVED mod chain) | correct | symmetric split keeps C_+ = 5 already; deep assignment with A_j = 2|a^#_j|/t |
| Lemma 2.3 (PROVED) | correct | P-23 constant order |
| Theorem G1.A (PROVED mod chain) | correct with fixable gaps | P-A1, P-W, P-N |
| Cor. G1.B (PROVED) | correct | cofactor polynomials used only for A_max / cube normalization, omitted in route V |
| Remark 2.2 (SKETCH) | label honest | not used |
| Lemma LE (PROVED) | correct | Farkas/Cramer with design numbers |
| Lemma 3.2, Theorem G1.C (PROVED mod chain) | correct with fixable gaps | G-T2, P-A1, P-23, generalization for G-S2 |
| Lemma 3.3 (PROVED) | correct with fixable gap | P-L1; (LATE) at exp(-C log^3(1/T)) re-derived |
| Lemma 4.2 (PROVED mod chain) | correct | b_bias << b; theta_T << theta_0 (wording) |
| Lemma 4.4 (PROVED) | correct with fixable gap | P-44 |
| Lemma 5.1 (PROVED) | correct in isolation | G-S2: not applicable with other tiny minors in the same blocks |
| Prop. 5.2, Cor. 5.3 (PROVED, first order) | correct in the restricted linear model | P-52' |
| Cor. 5.4 (PROVED mod chain) | correct | P-54 wording |
| Lemma 5.5, (NT_0) (PROVED) | correct | holds for any compact k-semialgebraic Z^str; P-55 |
| Theorem G1.D without thick-type carrier (PROVED as reduction) | correct with fixable gaps | G-S2, G-T2, Q-1 |
| Theorem G1.D thick-type part (SKETCH) | label honest | H1 levers at x^nat unwritten |
| Persistence (necessary condition) | correct | Q-1, Q-2 |
| (LSC-trunc)_N every f; density (OPEN) | OPEN | -- |

## 2. Attacks attempted
- Hoffman constants and which rows they involve: Lemma CH re-derived; its constant is B^{O(p)} (P-W), not Des^C/u; met rows
  only; cushioned violations exactly d_i x'.
- Does the transplant need only the face-wise bound?  Yes: every use of the cone point downstream was listed and checked
  (Prop. III-cushion (i), (iv); Lemma III-nodeep (T); Lemma III-CMtr (c), (d); Prop. III-BR (U3); Lemma III-track).
- Scale constraints b, s_1, theta_0, theta_T, theta_pr, delta_Z against (K2-d), (L-K2-1)/(L1), (L-K2-2)/(L2), (W_exp), (LATE),
  S2c^tr: all hold at the linear scale since every margin is >= exp(-C log^3(1/T)) and s_1 ~ exp(-1/(2T)); one constant (P-L1).
- Puiseux margin and (FC) consistency: (NT_0) proved; the margin at the linear scale is ~Des^{C_x} b; G-T2 found the only place
  where it can be destroyed (first-order band effects of size Des^C b/u with u not bounded below by a power of Des).
- Counting vs available stages: P-W (window count) and Q-1 (every sub-window and class must be residual).
- Design changes: (D-G1a), (D-G1b), P-CHOICE: level-L, f-free, N-free, monotone; well-founded.
- Signs: Lemma 4.4's factor (P-44); Cor. 5.3 (iii)'s determinant; D_M(bank) = z_s det[...] has f's contact sign (D below).
- Quantifier order: design -> f, g, rho -> L, w, class -> preparation P^nat (theta_T uses b, T_hi; theta_pr uses an a-priori s_1)
  -> targets -> bands -> Brouwer -> data at r^#: consistent.
- Recovering approximant missed?  For (R-S1): closing or banking a FREE target coordinate with robust room costs a z-move of size
  >= u/2 (value moves ~u/Des), far above o(u^2 T^2); raising s_1 to make FR rows soft needs banks >> b/T (G1's own remark).  I
  found no cheaper mechanism.
- Counterexample hunt: at a single stage an Example-4.3 shape with a FREE common target and adversarial contact signs at the
  other shared targets satisfies every proved constraint (ref notes D); persistence over all main stages is not excluded and not
  shown.  No counterexample.

## 3. Numerics (sanity only; r14/G1_ref_work/)
- ref_ch_check.py/.out: independent Lemma CH implementation; 600 instances, n in {3,4,5}, p <= 7, planted exact strict
  dependencies and tiny cushioned defects of both signs: strict exact 600/600, cushioned >= -eta|x'| 600/600, |x'-x| <= HV
  600/600, |B| <= n 600/600; |x'-x|/V median 1.8, max 1.0e6.
- ref_me2_system.py/.out: G-S2 model; joint exact set at distance 1.00 sqrt(b) for b = 1e-4..1e-10, all first cofactors +-1/2.
- ref_le_44_check.py/.out: Lemma 4.4 identity to 1.4e-8; failure with an extra ratio-dependent row (7e1); Lemma LE Cramer points
  exact to rounding (3000 systems).

## 4. Single most valuable idea
The strict/soft split.  Exactness on the zero set is needed only for minors made entirely of EQUALITY rows ((X3) and FR rows at
free target coordinates with robust room).  Rows at banked S_th target coordinates and inward rows carry cushions, and the
cushioned Hoffman lemma converts a tiny minor through such a row into a violation proportional to that minor, which the cushion
absorbs.  This removes contact-row resonances from the residual, pushes the core obstacle onto FREE target coordinates, and makes
the exactification linear wherever the strict structure is single-(X3).

## 5. What remains open (precise)
(1) (R-S1) one-signed STRICT linear resonances at FREE shared target coordinates with robust room: tiny nonzero minors of one (X3)
    row and FR rows, annihilated by every two-sided generator, one-signed against every one-sided raise/bank, wrong-signed at the
    start, at EVERY clean sub-window and class of all large main stages, with fresh carriers (H2 Lemmas 2.6/2.7).  At one stage this
    is consistent with everything proved (f chooses which other shared targets are contacts and their signs); persistence is open.
(2) (R-S2) strict systems with >= 2 (X3) rows, including the shared-block case (G-S2) where exactification can need displacement
    ~ sqrt(b); closing the rate scheme under the Jacobian minors of restricted systems is not done.
(3) (R-S3) one-sided blocking of linear near-threshold descent; (R-L) locked K^+ rows (H2 Lemma 3.4(c) SKETCH).
(4) (R0^str): H1's lever lemmas at x^nat with strict pinning (SKETCH).
(5) Inherited: once-refereed links (H1, H2, J1, J2, Part III Section 5), (KN)-block band bookkeeping (J1 SKETCH).
(LSC-trunc)_N for every f: OPEN.  Density of NA((c_0, p_N), l_2^2) for any N: OPEN.  Density of NA((c_0, p), l_2^2) for the
Martin-type p: OPEN.

## 6. Required edits to G1
- Theorem G1.A: (E3) closeness clause |r^# - r(f)| <= eta'(w) (P-A1); add (D-G1b) omega(L) >= 8(p(L)+4)(L+1) + C_K + 8 and replace
  "omega(L) >= 2^p" (P-W); state the normalization (P-N).
- Definition 3.1 / Theorem G1.C: bands as in H2.A / J1.15' in protected blocks, F-2 joint s_m in (U)-blocks (G-T2); targets (T1)
  := a compatible exact point of Z^str within Des^C b (G-S2 (c)).
- Lemma 5.1: "if M is the only tiny strict minor involving the ratios of blocks m, m'"; proof of G1.D: replace "Lemma LE (and Lemma
  5.1 ...) gives the (T1) targets" by "the negation of (R-S1), (R-S2) gives them" (G-S2).
- Lemma 5.5: state for every compact k-semialgebraic Z^str; half-radius cover (P-55).
- Lemma 4.4: "M is multiplied by 1 - dkappa_m/kappa_m to first order", hypothesis "no other ratio-dependent row" (P-44).
- Prop. 5.2: "iff in the restricted linear model; the realization needs a margin" (P-52').
- Lemma 3.3 (a), Def. 4.1: theta_pr := max(64 rho A_0 s_1/T, 4 Des K_DC r) (P-L1); Lemma 2.3: C_T after C_A, C_x, C_Lip, C_r (P-23).
- Cor. 5.4: "this resonance does not make the block residual" (P-54).  Theorem G1.D / persistence: "every clean sub-window and
  class" (Q-1).
