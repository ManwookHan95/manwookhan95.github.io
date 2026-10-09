# R3 part 5: what remains of O3 after error carrying; why no counterexample; assessment

## 5.1 The residual adversarial requirements (O3*). HEURISTIC formulation, OPEN.
After Theorem EC (compact error directions carried, no rate), Lemma 4.6 (contacts absorb error parts on far supports while
prescribing finitely many linear quantities) and Theorem 4-EC (averaging needs many converted scales only for the NON-carried
remainder kappa'), an approximate-resonance counterexample of E's type must satisfy, at EVERY candidate boundary scale lambda_b
(the approximant chooses lambda_b, and chooses it after the generic depth):
 (R1) non-compactness: the critical errors (size ~K lambda) of the carriers within J(rho) ~ 32 K/(1-rho^2) scales of lambda_b have a part
      r_lambda of critical size which escapes (r_lambda -> 0 coordinatewise along every sequence of boundaries, ||r_lambda|| >= c K lambda);
      the compact part is carried by EC (Prop 4.3);
 (R2) delayed generic approximants: no generic coordinate at depth >~ K lambda_b^2 approximates the directions r_lambda/||r_lambda|| within a
      fixed small precision (else EC with targets fixed after lambda_b, depth chosen before the scales s_j, carries them; this is
      consistent with Lemma B: targets may be scheduled arbitrarily late, cf. N2 4.5 / P1 2.1);
 (R3) concentration + guards: r_lambda lives on few coordinates (<= the number of linear constraints the approximant must respect there),
      and on each of them some MATCHED carrier above the boundary ("guard") has a mass exceeding its margin divided by the size of a
      contact move (else Lemma 4.6 makes all but boundedly many of these coordinates contacts with masses, absorbing r_lambda);
 (R4) no private handles: a critical escaping mass of a near-boundary carrier on a coordinate that no matched carrier sees critically is
      a conversion handle for that carrier (moving that coordinate by ~theta(1+delta)/K converts it); with J such handles at adjacent
      scales, N2 Theorem 4 applies without carrying anything. So every critical escaping coordinate of every near-boundary carrier must be
      guarded, for every boundary choice;
 (R5) the guards must lack private repairs: the guard's own escaping masses must be guarded in turn (recursive closure), its compact
      part cannot be moved by o(1) window moves at relative size O(1) (true: such moves are o(1), E Prop 8.2), and the global scalars
      (V, detector scalars) are too few;
together with (A1) (near-threshold one-sided carriers of both types at all scales: a fixed point between T and f, not constructed
anywhere, N2 4.6(i)) and the mate condition at f (all these errors absorbed at first order within the budget t^2/2).

## 5.2 Evidence that (R3)-(R5) are very restrictive. SKETCH / HEURISTIC.
(a) Coarsest-guard observation (SKETCH, in the "critical mass" model where a carrier at depth mu is moved beyond its margin by a contact
    move on a coordinate p iff its mass at p is >= c_0 mu): for each escaping coordinate p let c_max(p) be the coarsest carrier with a
    critical mass at p (it exists: a carrier at depth mu can have critical masses c_0 mu on at most K/c_0 coordinates by its error budget
    K mu, and fixed coarse carriers have only small masses far out). Then p is a PRIVATE handle of c_max(p) for every boundary above
    c_max(p). Hence designs in which each position is critical only for carriers within a bounded range of scales (chains, finite
    guard trees) give private handles to the top carriers; the counterexample needs positions that are critical for carriers at
    unboundedly many scales, i.e. SHARED positions (detectors) with critical masses proportional to depth; but a shared position with
    masses proportional to depth shifts all its members by the SAME relative amount, so one move converts all members of one type
    at all depths below the top member (two-sided carriers at every scale below a boundary: averaging over unboundedly many scales,
    A Thm 6.8 / E Thm 5.1 type). Masses not proportional to depth are E's detector design (band conversion), handled in 4.4.
(b) Worked example (PROVED arithmetic in a linear status model): chain guards u_i = v + K 2^{-i}(e_{p_i} + c e_{p_{i+1}}) (carrier i guards
    the position of carrier i+1 with relative weight c). Keeping carrier i_b matched and converting carriers i_b+1, ..., i_b+J requires
    Delta_{i_b+1} = 0 and Delta_i + c Delta_{i+1} = T_i (T_i ~ theta(1+delta)/K the conversion shift) for i = i_b+1..i_b+J, solved by
    Delta_{i+1} = (T_i - Delta_i)/c, which stays bounded by max T/(c - 1) ... in fact by |T|(1 + 1/c + ...)= O(|T|) for c >= 1 and by
    O(|T|/c^J) growth only for c < 1 with |Delta| <= sum c^{-k}|T| — in all cases the moves are O(J max|T|) = O(J theta/K) small, and all
    moved coordinates p_{i_b+2}, ..., p_{i_b+J+1} lie in the destroyed region (they escape as lambda_b -> 0). So chain guards give
    UNBOUNDED conversion capacity through the positions of finer (destroyed) carriers, and N2 Theorem 4 recovers the mates. [For c < 1 the
    recursion Delta_{i+1} = (T - Delta_i)/c can grow like c^{-J}: then use only J with c^{-J} theta/K <= 1, i.e. J ~ log(K/theta)/log(1/c),
    which is unbounded as K grows but bounded for fixed K; combined with EC/contacts (kappa' small) a bounded J suffices. SKETCH.]
(c) None of (a)-(b) is a proof that (R1)-(R5) are inconsistent: the real norm has further couplings (Hilbert part U e', several blocks,
    generic coordinates of other blocks), and the "critical mass" model is an idealisation. OPEN.

## 5.3 Why no counterexample, and what a proof of one would need
 * The closure route needs a closure theorem with multi-scale content (Prop Z kills scale-zero closure). The only candidate
   ingredient, an implant inequality, is unproved and in any case (3.2(c)) cannot exclude mates whose switching errors are carriable;
   EC carries all compact errors without rates.
 * For E's rigid design (compact errors in a fixed finite-dimensional E_c, detectors with disjoint supports, far rigidity), EC +
   contacts on the boundary detector + one converted carrier (one global scalar suffices) yield recovery modulo the transport
   hypothesis (HT-EC) (4.4, SKETCH), and Model N confirms R -> 1 (4.5, NUMERICAL). So the design does not give dist((f, rho g), NA) > 0.
 * A counterexample would have to realise (O3*) of 5.1, including the recursive guard closure, AND prove a LOWER bound for
   r~_{f'}(x_i) uniformly over all NA f' (all window moves, EC conversions, contacts, far moves, transfer peaks, averaging) — no such
   lower-bound technique exists in any of the notes; every device examined lowers the relevant upper bounds.

## 5.4 Assessment
 * Rigorous new results: Theorem EC (generic carriers convertible by vanishing window moves, rate-free), room lemma, Proposition Z
   (scale-zero closure trivial), disjoint block addition, Theorem 4-EC (averaging with carried errors; implication), contact lemma.
 * The conversion-capacity obstruction (O3 as formulated in BRIEFING_R2 ADDENDUM 2: "supply of two-sided carriers with frozen error O(scale)
   at J ~ 16kappa/(1-rho^2) adjacent scales") is REMOVED for compact error directions: only the escaping, recursively guarded part
   (O3*) can still require many conversions. Far rigidity (N2 4.5) is irrelevant to EC (EC uses window moves, not far tails).
 * The remaining open ingredient common to all positive arguments is the transport hypothesis (HT)/(HT-EC) above the boundary.
 * Leaning: positive (density), strengthened.

## 5.5 Suggested next steps
 1. Prove (HT-EC) for a concrete class: f with one-sided near-threshold carriers whose statuses are matched above lambda_b (window
    matched, coarse tails controlled), destroyed fine carriers contributing O(lambda_b/t) (E 2.1's (H-transfer) bookkeeping), errors at
    scale t carried by EC up to tau_gen. This would make 4.4 a theorem for E's rigid design.
 2. Prove a general "escaping-error handle lemma" (5.2(a)) in the real norm: a near-boundary carrier with an unguarded critical escaping
    mass is convertible at cost o(1) without disturbing matched carriers (far moves are free; Cor 6.2 of E is the duality version).
 3. Attack (R1)-(R5) by an l_1-budget/compactness argument (profile decomposition of the boundary errors along boundary sequences,
    coarsest guards) to show that every admissible T admits, at arbitrarily small scales, boundaries where kappa' is small: this would
    close O3 entirely (modulo (HT)).
