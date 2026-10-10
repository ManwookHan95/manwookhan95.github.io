# X1 part 4 — Master theorem, answers to (1)-(3), residual list, numerics

## 4.1 MASTER THEOREM IV^tr.  PROVED (modulo the refereed tools cited by U1-ref's Master Theorem IV' and Lemma W').
Design T^tr (3.1; option (a), or option (b) with the exception below), N fixed, f in S_{p_N^*} with finite base support F.  If for
infinitely many main stages L some clean sub-window w of L has at least n(w)/D_cls(w) dyadic scales whose activity class a has no
active shift or is one-signed, then f is in Rec(p_N).
Exception under option (b) only: the patterns in which the weight-one carrier 1 is an active near-threshold carrier of a T-block
(this requires rho_1(f) = 1 exactly).
Proof.  U1-ref's proof of Master Theorem IV' uses (KN_{w,a}) exactly once, through Proposition KN (statuses of the active near-threshold
carriers at the exactified companion, and the coarse statuses feeding U1 Lemma 4.3 / (SC)).  Proposition KN^tr (2.6) supplies the same
conclusions (a)-(c) for every class: KN-blocks by U1-ref's lever, T-blocks by Lemmas F, NLM, GEN, QC.  The modified inward rows (X4^0) are
satisfied by the decomposition up to K t (2.2(ii)) and make the cone's points kind [3] (2.2(iii)), which is all that U1 Prop. 2.2 and
U1-ref 4.1 use of (X4).  Everything else (classes and cubes, normalization to one shift ray, absorbers and the G1 release, configuration
(i) recursion with (SC), configuration (ii) Schauder completion, Theorem E^SC / E^>= with banked, pulled and absorber supports, subset
averaging) is U1-ref's refereed assembly, valid for T^tr by Lemma W'(iv).  QED
COROLLARY IV^tr.1 (N = 1).  For T^tr every first row of p_1 with finite base support is in Rec(p_1) (finite-F Lemma Z for p_1).
Proof.  With one block every class is one-signed or has no active shift; the pigeonhole over the D_cls(w) classes gives a class with
>= n(w)/D_cls(w) scales at every clean sub-window (U1 2.3-2.4).  Rows not in (C*) are in Rec by V2's Master Theorem III' (refereed). QED
COROLLARY IV^tr.2 (any N, conditional on X2).  X2's Theorem C_mix / Master Theorem V (Round 9, not yet refereed) recover mixed classes
under (KN); since (KN) enters X2 only through U1-ref's Proposition KN (X2 5.2, (U1)-(U7)), Proposition KN^tr replaces it, and every
F-finite row is in Rec(p_N) for every N — IF X2's results are confirmed and D^{X2}'s additions (D-lev), (W_exp) are imposed (they are an
upper bound on weights and a lower bound on Design(L), compatible with 3.1).  Status: SKETCH (depends on an unrefereed round).

## 4.2 Answers to the three questions of the task
(1) Designed levers.  NEGATIVE as posed, and not needed.
  * Lemma F (PROVED): at fixed active ratios no move can bring an active status below its floor rho^0 = m|r| K(sigma_rob, R_a^2)/Phi;
    a lever created or tuned at a companion only gives back what it adds.  So a private lever carrier helps iff it is robust and
    inactive AT f; whether that holds is a property of f (a rate object), not of the design.  Fine levers (weights <= c_{L+1}) have
    capacity <= c_{L+1}^2 << b(w); medium levers between sub-windows become coarse carriers of the later sub-windows and destroy the
    pigeonhole count (each adds >= 1 rate object per sub-window).  (KN) is therefore equivalent to "robust inactive k-mass at f" and
    cannot be made automatic by private levers (PROVED in the sense just stated; no claim that some other device could not).
  * What replaces the second lever: the position of the exact point on the zero set Z of the tiny minors.  Z and the functions psi_d do
    not contain the weights Phi_d of the switching carriers (2.2(iv), after rewriting (X4) at the floor); so for weights algebraically
    independent over the field of all other design data the threshold value 1 is never a local-minimum value of max_d psi_d/Phi_d on Z
    (Lemmas NLM, GEN: semialgebraic Sard), and status coherence holds with design constants (Lemma QC, Proposition KN^tr).  In this sense
    "the switching carriers' own weights are the levers" — chosen once, generically, in the design.
(2) (S1) in general and RT*(c): PROVED for T^tr (Theorem S1, 3.2), any number of shifted blocks, design x u^{-O(1)} Hoffman constants.
(3) Master theorem: 4.1.  All one-signed activity classes (and classes without active shift) are in Rec for every N; all F-finite rows
    for N = 1.  With X2 (unrefereed): all F-finite rows for every N.

## 4.3 What remains (precise)
 (R1) Option (b) only: rows with rho_1(f) = 1 exactly whose weight-one carrier is active near threshold in a T-block at almost all scales
      of the clean sub-windows of almost all main stages (OPEN; disappears under option (a), which drops only the normalization
      "equality for some (n,m)" of (T-a), never used in Martin's proof or in the note).
 (R2) Mixed classes for N >= 2: X2's Theorem C_mix (to be refereed); with it, Corollary IV^tr.2.
 (R3) Infinite base support F: (E1)-(E5) of ADDENDUM 7 and U2's items (unchanged; (C*) at infinite F would need Lemma F/NLM with
      infinitely many carriers — patterns are still finite per level, so the argument of part 2 should transfer; NOT checked).
 (R4) Transfer to Martin's p: row-wise statements do not transfer; density for p would follow from density for infinitely many p_N
      (lem:martintail), which needs Lemma Z including infinite F.
 Lemma Z and density of NA((c_0, p_N), l_2^2) (every N) and of NA((c_0, p), l_2^2): still OPEN because of infinite F (and (R2) for N >= 2).
 No counterexample is claimed; nothing found points to one.
