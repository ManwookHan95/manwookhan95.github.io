# N1 part 3 — Can one admissible T and one row kill every recovery mechanism? Assessment

Notation as in parts 1-2. "Kill" a mechanism = choose (T, f, g) outside its hypotheses while keeping g in C(f).

## 3.1 Mechanisms, the feature each exploits, and how an adversary kills it

| # | Mechanism (any admissible T unless noted) | Feature of (f, g) exploited | Adversarial kill | Compatible with g in C(f)? |
|---|---|---|---|---|
| 1 | f attains its norm [I prop:reduction(d)] | normer in c_0 | f non-attaining | yes (trivial) |
| 2 | Omega: lsc points, comeager [PrA, I rem:joint] | genericity of f | f in the meagre discontinuity set | yes: discontinuity points exist ([I thm:defect]; [II thm:II-NL]) |
| 3 | transport of finite and shifted certificates [I thm:transport, thm:shifted] | g two-sided, finitely carried, radius >~ t | O(1) one-sided content at cofinal small scales (M2) | yes: two-piece switching mates exist ([I prop:twopiece]) |
| 4 | averaging / ladder / weighted / carriers with non-summable gaps [I Sec 4] | g = certificate + O(t) at all small scales | same as 3, quantitatively | yes |
| 5 | locally split, split-contractive [I thm:locsplit] | one two-sided decomposition for all small t | switching | yes |
| 6 | transfer peaks, K(f), Gamma_w <= 1 [I thm:transfer; II thm:II-transferinf] | balanced finite certificate, Gamma_w <= 1 | g notin S(f), or Gamma_w > 1 (needs non-(BT), [I prop:lowerbound]) | yes |
| 7 | (BT) rows: every mate has two-piece data with kappa_w <= 1 [I thm:onesided, cor:BTrecovered] | F finite, Q_m finite, no degenerate peaks, (MS) | infinitely many strict non-peaks / degenerate peaks / (MS) fails / F infinite | yes; non-(BT) is Baire-GENERIC in fixed-z fibres (V4 Prop 5.1) |
| 8 | engineered NA approximants for EXACT two-piece data [I thm:engineered, cor:D1; II thm:II-raised, II-flipext] | finitely supported, scale-INDEPENDENT one-sided data with kappa_w <= 1; Delta d >= 0 or (SC) | no exact two-piece data (scale-dependent switching through infinitely many carriers), or Delta d < 0 without (SC), or kappa_w > 1 | data-free mates: existence at all scales NOT constructed (3.2) |
| 9 | Theorem E family (windowed recovery through nearby rows) [II thm:II-E, II-ERT] | exact window data at rows second-order close to f | only approximate data at every nearby row ("exactness vs scale") | not constructed |
| 10 | error carrying (R3 Thm EC) | errors in a fixed finite-dimensional space | escaping (non-compact) errors (R3 (R1)) | not constructed |
| 11 | banks, near-contacts, far pulls, contact lemma, fresh zero-weight non-peaks (R3 4.4, II-Sec 2) | the c_0 base and Lemma 1.4 (far freedom) | CANNOT be removed by T; only made insufficient ("bounded conversion capacity") | - |
| 12 | box-dominated support [II thm:II-N] | F = N, Bx <= C_a |a|, (SC_I), (W_M) | F != N or failure of these | yes |
| 13 | all designed-T machinery (Parts I Sec 8, II, III) | signatures, ladders, generic weights, diagonal base, levers | choose a non-designed T | - |

Every hypothesis in rows 1-7 and 12-13 can be violated by a pair (f, g) with g in C(f) (the violations are even generic in the
appropriate fibres). Rows 8-10 are violated only by mates of a kind that has not been constructed (3.2). Row 11 is not a
hypothesis on (f, g) at all: it is the flexibility of NA rows, which an adversary can only out-scale.

## 3.2 What is known about killing everything at once

PROVED facts that point TOWARD the possibility of an obstruction:
 (P-a) The intrinsic mechanisms (rows 3-6) can all fail at once: for some admissible T there is a non-attaining f whose
       intrinsically recoverable mates lie on one line while C(f) is infinite dimensional [I thm:defect], and the canonical
       truncations do not recover them [I prop:nonrecovery].
 (P-b) Lower semicontinuity of the fibre map can fail along sequences of block-tame (hence recoverable) rows, even at recoverable f
       [II thm:II-NL, prop:II-NLreal]: recovery cannot be propagated along arbitrary dense sequences of good rows.
 (P-c) Every NA row near a non-attaining f differs from f in every block at infinitely many carriers: there are infinitely many common
       peaks of OPPOSITE sign (N2 Lemma 3.3, refereed). Consequently NA approximants must "scramble" every block below some depth, and for
       two-piece data with Delta d < 0 the convexity mechanism fails on one side with a first-order block cost >= 2M|tau rho c|, so the
       d-mismatch must be paid in the base (N2 Cor 3.4, refereed). This is a genuinely ONE-SIGNED effect; the opposite peaks exist at
       EVERY NA approximant, but the cost bound is proved for the transferred two-piece decompositions of N2 3.1, not for all
       decompositions at f'.
 (P-d) Exact switching requires infinitely many one-sided coordinates [I prop:exact], and exact two-piece data carry no switching at
       rows with F ∪ K finite [II cor:II-S2]; NA rows have F', K' finite. So every NA approximant must TERMINATE the switching of a
       switching mate below some scale (PROVED in the exact form; approximate form = M7).
 (P-e) Far rigidity is compatible with Lemma B (N2 4.5, SKETCH); (SC) can fail for admissible T ([I rem:withoutSC(b)], SKETCH).

PROVED facts that point AWAY from an obstruction:
 (Q-a) Every explicit candidate built so far was recovered: P1's exact resonances [I cor:exampleRecovered]; all d-neutral exact two-piece
       switching mates (Round 2, P2A/N2 Thm 1); Delta d >= 0 [I cor:D1]; E's critical cross mates (Averaging, in cl Cert); E's rigid
       design for compact errors (R3, EC; SKETCH modulo (HT-EC)); self-aligned and nested-tuning rows (II, U3); for T_fin every
       finite-support row (III MT VI).
 (Q-b) No non-recovery statement is known along ALL NA sequences at any row: (P-a), (P-b) and [II prop:II-S3] are relative to
       restricted approximant classes (canonical truncations; block-tame rows with prescribed alignment), and Prop II-S3 itself shows
       how NA rows escape (put the two test coordinates into the support of one strict non-peak: one generic carrier suffices).
 (Q-c) The bad rows form a meagre set (F2), the defect is open on the graph (F5), and the dangerous mate must stay away from the
       fibres of ALL generic rows nearby (Lemma 2.1(b)): it is an exceptional mate of an exceptional row. Exceptional mates exist
       (P-a), but none has been shown to be exceptional relative to NA rows.

NOT KNOWN (the real gap): (N-a) existence, for any admissible T, of (f, g) with g in C(f) whose switching is genuinely
scale-dependent at ALL small scales (approximate resonances through near-threshold carriers or weak peaks at every depth, no exact
two-piece data) — "a fixed point between T and f, constructed nowhere" (R3 5.1); (N-b) any lower bound for dist(rho g, C(f')) over
all NA rows f' near any f.

## 3.3 The transfer principle: where an obstruction would have to live (HEURISTIC, with PROVED ingredients)

(i) Exact finite data transfer uniformly in scale. Two-piece data use finitely many carriers and fixed base vectors; their expansion
    coefficients depend continuously on the forced data, so they transfer to every nearby row with errors that are o(t^2) uniformly for
    |t| below a fixed radius ([II lem:II-U], uniform one-sided transfer; Lemma F1 of Part I). This is why [I cor:D1] needs no rates of T.
    PROVED (the cited lemmas).
(ii) Scale-dependent data transfer only above a junction. A mate violating (M2) uses at scale t carriers in their linear (saturated)
    regime, i.e. at depths in (~t^2, ~t), with O(1) total content (the linear-regime terms sum to O(t^2) in excess, [BRIEFING (R5)]).
    By (P-c) every NA row f' agrees with f only down to some depth lambda(f') > 0 (opposite peaks below), and by Lemma 1.4 the
    approximant can make lambda(f') as small as it likes, at cost p*(f' - f) -> 0. At scales t with t^2 >> lambda(f') the linear-regime
    carriers are copied; at smaller scales f' must supply its own structure. So every NA approximant has a JUNCTION, at a depth it
    chooses. HEURISTIC (the "copying" statement is not proved for arbitrary T: threshold drift caused by the deep alterations can flip
    near-threshold carriers far above lambda when (MS) fails — the designed T protects against this with buffers, V1 Lemma DR).
(iii) Tools at the junction (all available for every T): banks (tiny support masses; total mass O(lambda log(1/lambda)) suffices to carry
    the base-converted linear-regime content of f's altered carriers at all scales between lambda and sqrt(lambda), estimate HEURISTIC),
    near-contacts (one-sided, cost eta|V| t), fresh zero-weight strict non-peaks (O(1) content at scales <= depth, O(s) content at scale s
    needs depth >~ s^2: R3 room lemma, PROVED), error carrying for compact error families (R3 Thm EC, PROVED), and the averaging theorem,
    which needs only J(rho, K) ~ K/(c_0(1 - rho^2)) adjacent scales of two-sided capacity ([I thm:averaging], PROVED).
(iv) Consequence. A counterexample must defeat these tools at EVERY junction depth, by a margin that does not shrink with the depth:
    a SELF-SIMILAR, constant-level obstruction carried by T at every depth and tied to f (fresh resonance at every stage: H2.B for the
    designed T; R3 (R5) recursive guarding for arbitrary T). At model level (E, Model N) bounded conversion capacity J gives a boundary
    excess R(J) > 1 decaying geometrically in J (R(1) ~ 1.19, R(2) ~ 1.04, R(3) ~ 1.009 in the error-dominated regime), and error
    carrying removes it for compact error directions (R3: R -> 1). So the obstruction must ALSO make the errors at every junction
    escape to infinity (non-compact). HEURISTIC/NUMERICAL (model level).

## 3.4 Concrete candidates for an adversarial (T, f, g), ranked by how much is already known

 (C1) Negative d-mismatch without scrambling control: a block in which a positive proportion of indices at every depth are exact
      zero-weight strict non-peaks ([I rem:withoutSC(b)], SKETCH), so that (SC) fails, and a mate with two-piece data, Delta d < 0 and
      kappa_w = 1 (tight). By (P-c) every NA approximant scrambles the block and pays the d-mismatch in the base on one side; the
      engineered estimate then fails for rho close to 1 ([I rem:withoutSC(a)]: recovery needs rho^2 kappa_w + rho sum |Delta d| K^scr < 1).
      OPEN whether other approximants (raised supports, banked companions, (PC*)-tuned rows: N2 Thm 3, Lemma R) avoid the cost for every
      admissible T. This is the candidate with the most PROVED one-signed structure; its weakness: the base cost is a KINK of
      Delta d R*(w' - w), and the approximant controls where R*(w' - w) lives (it can push the scrambling deep), so the obstruction needs a
      reason why the scrambling at the junction is comparable to the junction scale for EVERY approximant.
      A self-similar mechanism of exactly this kind is visible in the engineered construction (HEURISTIC reading of [I, rem:withoutSC(a)],
      K^scr = (scrambling)/s_1): to TERMINATE the switching below a scale s_1, the approximant puts window masses of size ~ s_1 |b^theta_j|
      on the window contacts; their Hilbert footprint U^*(Delta a) moves the normer by ~ s_1 sum_j |b^theta_j| ||U^* e_j^*||/nu on coarse
      coordinates, which changes the status of the carriers at depth <~ s_1 (those with Phi gap <= s_1); if a positive proportion of indices at
      every depth are zero-weight non-peaks (failure of (SC)), the scrambled mass is ~ s_1, so K^scr = O(1) at EVERY termination scale and, for
      Delta d < 0, the one-signed cost (P-c) is a constant fraction of the slack when kappa_w = 1 and rho -> 1. Escapes that an obstruction
      would have to close: (e1) footprint-free termination through BLOCK carriers (fresh zero-weight non-peaks at depth ~ s_1 carrying the
      switching two-sidedly) — this is the conversion-capacity question of (iv) again; (e2) bank efficiency (a base with ||U^* e_j^*|| tiny on
      the termination coordinates, as in the designed diagonal base) — an adversary removes it by choosing U with slowly decaying ||U^* e_j^*||
      (U is a free compact dense-range operator in the construction); (e3) raise transfer (same-sign raises on F cancel their l_1 mass against
      normalisation, [II lem:II-RT]) — applies to masses on F, not on contacts; (e4) d-consistency levers (designed T only).
 (C2) O3* (R3 5.1): error-dominated one-sided carriers of both peak types at all scales, escaping and recursively guarded critical
      errors; the chain-guard model suggests alternating types at ratio exactly 1 as the only configuration with bounded conversion
      capacity (R3 5.2, SKETCH). Nothing beyond model level.
 (C3) Type (II) of Theorem 1.9: two recoverable mates whose recovering approximants are incompatible (e.g. opposite sign requirements on
      the same far coordinates), with the midpoint not recoverable. No mechanism known; it is the only route not excluded by the fact that
      all positive constructions are mate-specific.

## 3.5 Verdict

 1. Killing all KNOWN mechanisms at once is conceivable: their hypotheses are independent, and the violations of rows 1-7 are generic.
    But killing mechanisms is not an obstruction. The approximant's freedom (row 11: far data, banks, near-contacts, fresh carriers)
    is not a finite list of tools; in fourteen rounds every adversarial feature was answered by a new mechanism (averaging, engineering,
    error carrying, convexity placement, Hoffman matching, exactification, levers), and no lower bound for dist(rho g, C(f')) over all NA
    rows has been proved anywhere. HEURISTIC (historical), PROVED in each instance cited.
 2. The present failure to prove density is a failure for ARBITRARY T of the explicit constructions, whose bottleneck is EXACTNESS
    (finite systems that must be solved exactly with one-sided levers). Lemma VT ([II lem:II-VT]) and G3 Prop 3.3 show that approximate data are tolerated
    up to violations of relative size O(1) times a small constant; so exactness is a feature of the method, and it becomes an invariant only
    if violations of relative size bounded below are forced at EVERY junction for EVERY approximant. No such invariant is known; (P-c) is the
    only approximant-independent one-signed effect proved so far, and it is first order in the scrambling, which the approximant controls.
 3. Therefore the evidence does not support switching to a negative programme wholesale. It does support a TARGETED negative test,
    because (a) a counterexample can only live at an adversarial T (for T_fin: only infinite F and failure of (LSC-trunc)); (b) for
    arbitrary T the open core is large (approximate resonances, Delta d < 0 without (SC), Gamma_w > 1, infinite F); (c) the decisive
    quantity — conversion capacity at a junction under adversarial rates, with escaping errors — is open even at model level.
 4. The missing invariant (formulated so that either answer is progress):
    (CAP+) [positive] for every admissible T, every f, g in C(f), rho < 1 and lambda_0 > 0 there is an NA row f' with a junction depth
           lambda < lambda_0 at which J(rho, K) adjacent scales of two-sided capacity carry rho g up to O(scale) (then averaging closes);
    (CAP-) [negative] an admissible T, a row f and a mate g, and a functional Psi(f', lambda) >= c > 0 for every NA row f' near f and every
           junction depth lambda, which lower-bounds the boundary excess (Model N's R - 1) and is monotone under banks, near-contacts, error
           carrying and fresh carriers. By Theorem 1.9 it is natural to aim first at a TYPE (I) obstruction: one fixed direction x in c_00 and,
           for every admissible normer x', a cheap multi-scale decomposition of x (Theorem 1.6(c)) — a purely primal object.
 Leaning: POSITIVE (density more likely), with low confidence for an arbitrary admissible T; no step of a negative proof exists.
