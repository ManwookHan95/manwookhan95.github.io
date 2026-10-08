
# 7. What remains, corrections to the sources, next steps

## 7.1 Corrections / sharpenings of Round-1 statements
 * A_notes Conjecture 7.5 ("scale separation of T => Def(f) empty for every f"): cannot hold as stated. Theorem 2.4 produces a
   nonempty defect through an EXACT resonance, which involves no approximation rates at all (the construction of 2.1 can be done
   with all non-special vectors as "generic" as one likes). This confirms rigorously the referee's objection (A_referee §3.5).
 * A_referee §5.2 (two-piece mates, SKETCH with a generic existence step): made rigorous for the T of 2.1 (2.3), together with
   their membership in Def(f) (2.4), which the referee left OPEN.
 * A_referee §5.4 (engineered recovery, SKETCH): the "extra degree of freedom in the masses" can fail (e.g. diagonal U: every
   admissible positive mass raises u(x'')); compensating by pulling contacts inward costs first order at exactly the scale where
   the masses are needed, with a constant that blows up as rho -> 1. Fix: far sign-flipped contacts with negative masses ("free
   pulls"); and the truncated target must carry a constant tail mu_inf u (6.3).
 * BRIEFING_R2 / task text: "one-sided resources at scale t only carry mass from coordinates with Phi_m(k) <~ |t| (or contacts)" is
   true only for coordinates whose gaps/margins are bounded below; near-threshold coarse coordinates and degenerate peaks are
   scale-free one-sided resources (3.3).
 * BRIEFING_R2: "cross-block near-duplicates are built in, so scale separation cannot be assumed": by the sign rule (4.2) exact or
   o(Phi)-perturbed duplicates serve the SAME side and cannot switch with each other; switching needs perturbations >~ Phi in the
   xi-direction with opposite signs, and then (4.4) the mate is in cl Cert(f) unless the gaps are summable.

## 7.2 Precise open problems left by P1
 (O1) Second-order defect: is there f (e.g. C-tame) and g_c in C(f) with Hhat(c) > 1? Equivalently: are A's shifts along R_m* w_m
      the last layer of second-order rebalancing? Candidates for cheaper rebalancing: shifts along u_{k,m} at weak peaks (exchange
      rate Phi_k^2 M/C in the block against kink costs of u_{k,m} in the base). Needed positive tool: an averaging theorem for
      (generalized) shifted certificates with a uniform remainder (A Remark 4.19), plus their transport.
 (O2) Approximate resonances with summable gaps or weak-peak carriers (4.4 Rem): no linear obstruction; a proof of non-membership
      in cl Cert(f) would need a sequence test (find f_n -> f in S_{p*} with g notin Li C(f_n); cl Cert(f) is in Li C(f_n) for every
      sequence).
 (O3) General T: does every admissible T admit f with Def(f) != empty? The two-piece mates exist for every T (generic step of
      A_referee §5.2), but the linear obstruction needs a block-tame f, i.e. a zhat avoiding the slabs |u_{k,m}(zhat)| <= theta Phi_m(k)
      for all but finitely many (k,m); for an adversarial T this may be impossible (Preprint A's residuality of half-peaks).
 (O4) Recovery: prove f in R for the example (all of C(f), not only the explicit switching mates): needs asymptotic optimality of
      the explicit (possibly shifted) decompositions (6.3 Remark). More generally: an engineering theorem for EXACT resonances
      (far negative masses + constant tails + exact carriers) at arbitrary f with infinite contact sets.

## 7.3 Recommendation
The intrinsic program "every mate lies in cl Cert(f)" is dead (Theorem 2.4). The density proof must recover the resonant part of
the fibre along ENGINEERED NA sequences. The present notes show that this is feasible for exact resonances in the explicit
example (6.3) and give the precise list of what an engineered recovery must handle: (i) exact carriers (enforce u(x') = 0 by
masses and free pulls), (ii) window masses for the smallest scales, (iii) far sign-flipped contacts, (iv) constant tails of the
target, (v) the second-order coefficients of the explicit side decompositions. The next step is a general "resonance recovery
theorem" covering mates whose decompositions are, on each side, certificate + exact-resonance part + O(t).
