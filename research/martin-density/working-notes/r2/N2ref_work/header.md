# N2 referee notes (assembled): verification of N2_notes.md and a sharper treatment of Delta d < 0

Setting: canonical base q, Martin's norm with a FINITE block set I (p_N; by Preprint B Remark martin-tail, density for p_N at arbitrarily
large N gives density for p). Admissible T = Lemma B's conclusion only. Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Part files: N2_ref_part1.md (algebra, Lemma 1.3, Theorem 1), N2_ref_part2.md (Cor 2.5, Rem 2.6, Section 3: Lemma 3.1-3.4, Thms 2-3),
N2_ref_part3.md (new: Lemma R, Theorem 3*, Corollary R), N2_ref_part4.md (kink class, 3.7-3.8, Section 4-5, numerics).
Scripts: N2ref_work/ytrick_exact.py, ytrick_sharp2.py, ytrick_general.py, ytrick_diag.py (Lemma R); N2's own scripts re-run.

Summary of findings.
 * N2 Theorem 1 (Delta d = 0) and Corollary 2.5 (P1's explicit defect recovered): PROVED, every step re-derived.
 * Lemmas 1.2-1.5, 3.1, 3.2, 3.3, Theorem 4, Prop 5.2 (mod R1): PROVED as stated.
 * Theorem 2 (Delta d > 0): correct after a constant fix (s <= 1/2 is not enough in Lemma 1.3's factor 1/(1-s); need s <= eta_0/2).
 * Theorem 3 (Delta d < 0): the IVT tuning step is unjustified without (TT) (psi~_n(0) may be > 0); constant in G_n; fixable by hypotheses.
 * Corollary 3.4 / 4.7 ("mismatch must sit in the base"; "convexity cannot replace (PC)"): FALSE as stated. Lemma R (new, PROVED):
   N(w' + (w'-w)1_S) <= 1 + (C'-C)_+ + second order, S = coordinates where the reflection 2w'-w does not overshoot. Only the status-changing
   part of w'-w and one scalar must be paid. Theorem 3* replaces (PC) by (PC*); Corollary R proves N2's 3.7(a) (block-tame, (TT)) outright.
 * 1.6/3.9 kink class: identification correct when Q is finite; "no new mechanism" over-stated (weighted vs max coefficients).

