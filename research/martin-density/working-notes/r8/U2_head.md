# U2 notes (Round 8): infinite base support -- items (E1)-(E5) of ADDENDUM 7

Part files (assembled below, after this head, with light edits): r8/U2_part1.md (E1), U2_part2.md (E2), U2_part3.md (E5),
U2_part4.md (E3, E4); orientation digest U2_part0.md.  Script: r8/U2_work/pair_tuning_check.py.
References: paper/martin_density_note.tex ("the note"); r5/Z5_ref_notes.md (R1 = Theorem R1, R2 = Lemma R2, Lemma R0);
r6/Y3_notes.md (Theorem 2.1, Theorem 6.1, (LSC-trunc)); r7/V1_notes.md (D_Omega, Lemma B, Lemma TU, (C1)-(C4), Prop. TR);
r7/V2_notes.md + V2_ref_notes.md (Theorem B, minors, (C*)); r7/V3_notes.md + V3_ref_notes.md (Lemma 2.3 RT, Theorem 2.5 E_RT,
Lemma VP', Theorem RS'); r8/U4_notes.md + U4_referee.md (T_final, fix C1 B_mu(l)).
Setting: finite block set I = {1..N}, p = p_N (lem:martintail passes density -- not individual rows -- to Martin's p for ONE N-free
design); f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu), F = supp a ARBITRARY (the point of this note: F infinite).
Labels: PROVED / SKETCH / HEURISTIC / OPEN / FALSE.  No counterexample is claimed; nothing found points to one.

## 0. Summary

Bottom line.  For a designed norm, (E1) and the (ND')-half of (E4) are SETTLED for RS-type rows (finitely many bad carriers), (E2) is
reduced to explicit rate conditions with all structural obstructions removed, and (E3), (E5) and the degenerate-peak half of (E4) are
reduced to the "(SC) at companions / exactness" complex that already forms the finite-F residual (C*), plus one new exotic tuning-degenerate
class (NDN):
 * (E1) mu-thin supports: SETTLED (PROVED) for RS-type rows (finitely many exactly swallowed bad carriers; and, conditionally on rates,
   for infinitely many, part 2) by a design choice plus a new pinning lemma.  With a diagonal base whose entries decay doubly
   exponentially (mu*_s = 2^{-2^{2^s}}), the raise-room condition (RR) of V3's Theorem RS is no longer needed: an unraised coordinate
   that would be deep for the window data PINS the switching carrier through the mate's own flip budget (Lemma P), so only coordinates
   beyond a depth J have to be raised, and their Hilbert footprint is <= mu*_J; the pinning constant 2^J/delta is O(log(window depth)).
 * (E4)(i) failure of (ND'): SETTLED (PROVED): (ND') can be dropped from Theorem RS.  If (ND') fails, the support of a lies (up to
   finitely many target coordinates) in the signature sets of the kernel carriers with profiles PROPORTIONAL to the signatures
   (Lemma ND), so every bad-carrier switching on F is cushion-dominated, no raise is needed, and R1 applies directly.
 * (E2) infinitely many bad carriers / (O4-box): REDUCED to rate conditions (PROVED, conditional).  Box-level deep raises (mass O(2^{-J}))
   plus Lemma P plus a pigeonhole of thresholds give cushion-compatible exact window data with NO bounded switching, NO box domination and
   NO (RR); what remains is a window condition (W_inf) on f-dependent rates (rooms, Hoffman constants of the growing exact cones, VP
   constants, gaps of bad strict non-peaks) -- the same kind of rates that V1/V2's clean sub-windows convert into design constants at
   finite F.  V3's "scale-free raise" obstruction disappears (the scale-free raise is needed only on the deep part, of vanishing mass).
 * (E5) transport of the finite-F master theorems: the VP rate is NOT needed (raise FIRST, deep, then exactify at the raised row: Lemma
   DR-inf keeps the clean classification); the only new ingredient is private two-sided TUNING of values of carriers whose design-depth
   signature coordinates lie in F.  Lemma TR-inf provides it (PROVED) in all cases except a near-(ND')-degenerate configuration (NDN),
   which is a rate condition on a alone and can alternatively be routed through non-d-neutral data, i.e. into "(SC) at companions".
   Theorem M-inf (SKETCH, flagged inspection items): an infinite-F row is in Rec_N unless (C*) [read at deep-raised rows], (NDN), or the
   block exclusions shared with finite F hold at all clean sub-windows of all large levels.
 * (E3) non-d-neutral data at raised rows: never needed in the window theorems (data are built AT the companion and are d-neutral);
   needed only inside (C*), where it is exactly V2's gap (C*-2) "(SC) at companions" (block property, independent of F).  For transported
   FIXED data the representation drift is a nonzero element of Y of infinite support (PROVED) which generically violates side-
   admissibility (HEURISTIC); not needed.
So "Lemma Z at infinite F reduces to Lemma Z at finite F" holds in the following precise sense: for the designed norm, every infinite-F
row is recovered except in configurations that are infinite-F transcriptions of the finite-F residual (C*) / "(SC) at companions",
plus the exotic tuning-degenerate class (NDN) (SKETCH level for the general transport; PROVED for RS-type rows: finitely many bad carriers,
any profile, no (RR), no (ND')).

| # | Result | Scope | Status | Where |
|---|---|---|---|---|
| 1 | Design SLD^star / T_final^*: base mu*_s = 2^{-2^{2^s}}, window factor Omega(l) = (s_max 2^{s_max}/delta_min) x (two design logarithms); admissible, N-free | design | PROVED | 1.1 |
| 2 | Lemma P: an unraised coordinate that is deep for the data pins the carrier, |tau_l| <= C_q t/v_l(s) | any SLD-type T, any F | PROVED | 1.2 |
| 3 | Theorem RS*: support swallowing of ANY profile by finitely many bad carriers, WITHOUT (RR) | SLD^star | PROVED (inspection items I1-I3 of V3 unchanged) | 1.3 |
| 4 | Lemma ND + Theorem ND': (ND') fails => a proportional to kernel signatures => R1 applies; (ND') dropped from RS* | any SLD-type T | PROVED | 4.2 |
| 5 | Lemma W: window data at a deep-raised companion, any number of bad carriers, no bounded switching / box domination | SLD^star | PROVED | 2.1 |
| 6 | Theorem RS*_inf: infinitely many bad carriers under the rate condition (W_inf) | SLD^star | PROVED (conditional) | 2.2 |
| 7 | Lemma DR-inf: a deep raise preserves the clean classification (no VP needed) | T_final^* | PROVED for (R1)-(R5), (R7), minors; (R6) SKETCH | 3.0 |
| 8 | Lemma TR-inf: private two-sided tuning at infinite F (cases (a), (a'), (c), (c')) | T_final^* | PROVED | 3.2 |
| 9 | Residual (NDN) of the tuning; relation to (ND') and to (SC) at companions | -- | precise statement; OPEN | 3.3 |
| 10 | Theorem M-inf: transport of Master Theorem III' to infinite F | T_final^* | SKETCH (flagged items) | 3.4 |
| 11 | (E3): window theorems need no (SC); drift of transported fixed non-d-neutral data; (E3) inside (C*) = (C*-2) | -- | PROVED (structure, drift in Y), HEURISTIC (generic violation), OPEN (C*-2) | 4.1 |
| 12 | (E4)(ii) degenerate swallowing-sign bad peaks: via V1's donor raise in M-inf, needs a donor resource of Lemma TR-inf | T_final^* | SKETCH | 4.3 |
| 13 | Numerics: pair tuning cancels the common term exactly at first order (60 digits) | evidence | -- | 5 |

## 0.1 Answers to the task items
(1) (E5): the f-dependent VP rate is avoided altogether by the order "deep raise, then exactify" (Lemma DR-inf); the new requirement --
two-sided private value tuning of carriers whose shallow signature lies in F -- is met by Lemma TR-inf with design x u^{-C} constants
(contacts / convertible thin support / robust Hilbert pairs / anchors); its failure (NDN) is a rate object whose robust case is covered
and whose tiny case is a near-(ND') degeneracy.  Theorem M-inf states the resulting transport (SKETCH).
(2) (E1): settled by Lemma P + design mu* (Theorem RS*); neither two-stage approximation nor a weighted footprint is needed: the
thin shallow coordinates are handled by the MATE's flip budget (they pin), only the deep part is raised.
(3) (E2): Lemma W + Theorem RS*_inf: per window only the coarse bad carriers matter; box-level deep raises of mass O(2^{-J}); pinned
carriers removed by a pigeonhole of |B(l)|+1 thresholds; shallow thin TARGET coordinates handled by a second pigeonhole (sub-window
position) and contact rows.  Remaining: the rate condition (W_inf).
(4) (E3): structural reduction to (C*-2) (4.1); (E4): (ND') dropped (Theorem ND'); degenerate swallowing-sign bad peaks reduced to the
donor-resource question (4.3).

