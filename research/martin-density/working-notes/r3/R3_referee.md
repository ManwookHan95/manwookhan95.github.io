# Referee report on R3 (rigid T: counterexample attempt; error carrying)

Files checked: r3/R3_notes.md and R3_part1-5.md, r3/work/*.py. Imports re-checked: A Facts A-E, Def 4.1, Lemma 4.4, Prop 4.5,
Lemma 4.7; N2 Lemmas 1.4, 1.5, Thm 4; E 2.4, 4.1-4.4, 6.1-6.4, 7.3-7.5, 8.1-8.3. Setting: finite block set I (p_N), canonical base,
admissible T = Lemma B's conclusion only. Detailed checks: R3_ref_part1-4.md; assembled proofs: R3_ref_notes.md; scripts: r3/refwork/.

## Summary
R3 claims no counterexample. Instead it gives a new recovery tool, Theorem EC. Every PROVED claim of R3 survives a line-by-line
check. Two of them need small wording or bookkeeping fixes. The SKETCH "E's rigid design is recovered by EC + contacts + ONE converted
carrier, modulo (HT-EC)" has a second gap besides (HT-EC). EC removes the ERROR-driven conversion requirement (J ~ 32 kappa/(1-rho^2)).
It does not remove a rho-independent HILBERT/ROOM-capacity requirement on the converted carriers near and below the destruction
boundary. In Model N, R3's own model, the claim "one converted carrier of one type suffices" fails at parameters close to R3's:
 - A = 0.5 gives R = 1.46;
 - B = 0.6 gives R = 1.086;
 - in a variant where the peak cost is tied to the margin as in the real norm, R = 1.09.
In all three, R does not change as tau_gen grows. Converting both types gave R = 1.000 in the tested real-norm-like variant.
No claimed counterexample is involved, and nothing found contradicts Lindenstrauss property B for l_2^2. Density remains OPEN.

## Verdicts
1. Theorem EC: CORRECT (PROVED). Every step was re-derived:
   - tail density follows from Lemma B (no isolated points);
   - Neumann bound;
   - choice of N(n) after the indices;
   - move bound min/8 + min/4;
   - validity via Fact D and N2 Lemma 1.5;
   - strict non-peak via Fact C;
   - certificate data via A Prop 4.5.
   No hypothesis on T beyond Lemma B is used. Wording fix: the depth is only bounded ABOVE (Phi(k) <= Phibar_n). The actual depth is
   chosen by T, so "at any prescribed depth" must read "at least as fine as any prescribed depth".
2. Room lemma: CORRECT. It applies to errors of size O(scale), either a fixed vector of size kappa s or a t-dependent vector of size
   kappa t. For components of relative size O(1) the Hilbert coefficient is not small. That is the implant scale gap, and R3 states
   it correctly.
3. Proposition Z: CORRECT. J infinite is needed and used. 3.2(a) follows correctly from the definitions.
4. Theorem 4-EC: CORRECT as an implication in the R3_notes form (split into kappa_T and kappa_F). R3_part4.md 4.2 has a wrong
   intermediate hypothesis (one kappa' with J >= 32 kappa'/(1-rho^2)); the author corrected it, and the part file should be marked
   superseded. "J = 1 suffices" additionally needs (HC) for h_1, which is a Hilbert-capacity condition (see the main finding).
5. EC on compact error spaces (4.3): CORRECT as arithmetic; notes use beta_T = ||(B^T)^{-1}||, part 4 used beta.
   - Caveat (i): room is guaranteed only up to T_n, and T_n -> 0, while (HT-EC) is needed up to the fixed T_0. The non-carried
     transport remainder on [T_n, T_0] must already be small. This holds for E-type boundary-layer errors (size K lambda_b), so the
     quantifier order works together with (HT).
   - Caveat (ii): Pi must be fixed before the generic coordinates, and must not block target directions.
6. Contact lemma: the LP statement is CORRECT (vertex argument). The absorption statement holds under conditions that should be
   written out:
   - the TOTAL base part vanishes at the normer;
   - masses >= T_0 |B_j|;
   - the change of e'' forces a final EC re-solve;
   - a Hilbert cost of t^2 h''(B)/2.
   The a''-direction step stays SKETCH.
7. Rigid design recovered: SKETCH, with an ADDITIONAL gap (main finding) and three fixable issues:
   - (P1) Protected set. Protecting the band or designated carriers u ~ (v + K lambda sigma)/n together with v protects sigma|_G in
     E_c. By R3's own Remark 2.2(2), hypothesis (ii) fails as soon as the protected sigma|_G, together with v|_G, span a target
     direction. That happens, for example, once dim E_c matched carriers with spanning sigma's are protected. If they span a target
     only approximately, beta blows up instead; this is harmless for EC itself (eps_n is free) but shrinks T_n and tau_F. Fix: protect
     only v. Statuses are then kept anyway, because a move with v(eta) = 0 shifts each v-carrier by the relative amount
     O(K ||sigma|| ||eta||/theta) -> 0.
   - (P2) Order. Far choices and contact masses change u_{k_{n,i}}(x'') by up to 2 eps_n, possibly >> Phi(k). EC must be re-solved
     LAST.
   - (P3) The final EC move (size ~ beta eps_n, fixed before lambda_b) shifts all block coordinates. This is harmless for the
     switching carriers but uncontrolled for other structure of f at depth ~ lambda_b, so it belongs inside (HT-EC).
   Also: a single-coordinate detector may stay fractional (r = 1 in 4.4). R3's restriction to {1 - z_j, -1 - z_j} is unnecessary.
8. Model N with EC: REPRODUCED exactly:
   - both types: 1.0882 / 1.0228 / 1.0054;
   - one type, one carrier: 1.1682 / 1.0406 / 1.0089; without EC 3.406.
   The one-carrier result, however, is a borderline artefact: B S^2 = 0.5 against sup P_f = 0.5225.
9. Near-threshold peak cost: CORRECT (re-derived). Numerically confirmed to O(t^2) (refwork/peakcost.py).
10. Chain guards: the arithmetic is CORRECT in the linear status model:
    - c > 1 bottom-up: bounded;
    - c < 1 top-down: <= T/(1-c);
    - alternating types at c = 1: growth ~ J T.
    Caveat at c = 1: the moves stay bounded only with constant targets; random targets give a random walk. Coarsest guard: HEURISTIC.
    The shared-position dichotomy is not exhaustive. It needs the top member's depth -> 0, which holds for escaping positions.
11. O3*: a reasonable OPEN formulation for errors, but INCOMPLETE. Add (R6): conversion capacity below the Hilbert/room requirement
    at every boundary, even when all errors are compact.

## Main finding: the Hilbert/room-capacity gap
Mechanism. Below the band, |t| << delta lambda_b, the O(1) switching component can only use converted carriers:
 - matched peaks have relative first-order cost delta Phi M/(m C |t|) -> infinity (R3 4.7);
 - destroyed carriers cost ~ a0 s/tau;
 - EC generic carriers cannot take O(1) components (implant scale gap).
With N converted carriers the block coefficient is rho^2 S^2/(N m0^2 C''). So (HC) needs N >= rho^2 S^2/(m0^2 C'' Q). Above the band, the
room of the destroyed carriers, ~ 4 M lambda_b/t at scale t, must also be replaced. EC carries the extra ERROR of re-routing but not the
extra HILBERT load.

Model N (scripts in refwork/):
- Bottom value: P_{f'}(tau -> 0) = B S^2/n_conv exactly.
- One carrier, EC at 2^6: A = 0.5 gives R = 1.463; A = 0.25 gives R = 2.074; A = 1, B = 0.6 gives R = 1.086. All maxima are at the
  bottom scale and do not depend on tau_gen. All three cases are still "error >> peak cost", i.e. inside E's class (A1).
- Two carriers: A = 0.25 gives R = 1.037; A = 0.1 gives R = 1.426.
- Required n_conv ~ B S^2/sup P_f grows like log(1/c) as the linear costs c -> 0 (from 0.96 to 8.12).
- Real-norm coupling (peak cost tied to the margin, a0(1+delta) = delta):
  - the bottom requirement is met by one shift;
  - but with one shift, A = 0.1 delta and delta = 1, R = 1.090 at tau ~ 4.7 for both tau_gen = 2^6 and 2^8 (a boundary-layer room
    deficit);
  - two shifts give R = 1.0000.
- Why one shift fails in the boundary layer. One absolute shift V moves every fine carrier by V/lambda in the same direction, since
  V ~ theta lambda_b dominates detector shifts of size ~ Phi_k. So the whole destroyed region becomes deep peaks of ONE sign, and one
  side of t loses its fine room entirely. A group scalar with opposite P+/P- coefficients leaves deep peaks of both signs, whose cost
  a0 s/tau decays above the band. R3's single-coordinate-detector fallback (4.5(3)) is exactly the one-shift case.
Consequences:
- "One converted carrier / one global scalar suffices" is FALSE in general (also inside E's (A1)-(A5)).
- "Bounded conversion capacity is not an obstruction for compact errors" must be weakened: the error-driven part is gone, a bounded
  rho-independent capacity part remains.
- "E 8.3 is irrelevant" and "far rigidity does not matter" hold for EC itself only.
- E 4.4 (two group scalars at a transition, converting both types) is what the corrected sketch needs.

## Positive addition (PROVED, elementary)
Joint certificates pool Hilbert capacity. Suppose the band certificates h_j live on disjoint zero-weight strict non-peaks. Then
h_A = avg_{j in A} h_j has H = (1/|A|^2) sum H(h_j) and radius >= |A| min r(h_j). Applying convexity to the active and frozen GROUPS,
instead of to all J summands, weakens (HC) to avg_{A_t} H(h_j) <= |A_t| Q. N2 Thm 4 and 4-EC discard this factor
(R3_ref_notes Remark 4.1).

## Most valuable idea
Theorem EC with the room lemma and the quantifier order "generic depth before the boundary":
- dense-tail generic coordinates become exact zero-weight strict non-peaks through o(1) window moves that solve a finite linear
  system against targets in zhat-perp;
- they then carry any fixed finite-dimensional family of O(scale) errors two-sidedly at quadratic cost O(scale^2);
- no rate hypothesis on T is needed.
After EC, what remains of O3 is a CAPACITY count of converted carriers (room/Hilbert), not an error count.

## Recommendations
(1) Restate claim 9 with an explicit capacity hypothesis on the converted carriers, and use both types (group transitions).
(2) Fix P1-P3.
(3) Add (R6) to O3*.
(4) Prove a pooled (joint-certificate) version of Theorem 4-EC.
(5) Attack (HT-EC) for E's design with the room bookkeeping of R3_ref_part3 P6.
