# E notes, part 8: what o(1) moves can and cannot do (corrects an error in my earlier reasoning)

## 8.1 A false intermediate claim and its correction

Earlier (part 7.2(iv)) I assumed that a window move eta orthogonal to all SENSITIVE coarse coordinates changes f' only
through coordinates finer than the boundary ("deep peaks do not care"). That is FALSE as stated:
 * a change Delta of zeta' = L x' at deep peaks changes the block norm |zeta'| at first order (by sum over peaks of
   M sign(k) Delta(k), up to normalization) and therefore rescales ALL off-peak values w'(k) = C' zeta'(k)/(Phi_k^2 |zeta'|);
 * moderately deep peaks with |u_k(xhat)| <~ |u_k(eta)| change sign; the coarse ones change w' by O(M lambda_k).
Sanity check that something must fail (PROVED): if a fixed window coordinate l could be moved by a fixed amount gamma at
cost o(1) in ||f' - f||, we would get NA f'_n -> f with x'_n(l) not converging to xhat(l), contradicting
G_notes Prop 3.9 (normers converge weak* when first rows converge in norm; uses uniqueness of the normer).

## 8.2 Proposition (o(1) window moves). PROVED (as a consequence of (F1))

If f'_n -> f in S_{p*} with normers x'_n = q-normalized z'_n + U e'_n, then for every fixed coordinate l,
z'_n(l) -> z(l) and e'_n -> e. Consequently, for every fixed finite window F_0 and every fixed vector y in l_1 supported
in F_0 (in particular every fixed vector u restricted to F_0), y(x'_n) - y(xhat) -> 0.
Proof: G_referee 4.7 / (F1) and Prop 3.9 (e'_n -> e because a'_n -> a in l_1 and U* is bounded, nu_n -> nu > 0). QED

Consequence for conversions (SKETCH, all steps elementary): let resources u_k = (v + K lambda_k sigma_k + (far part_k))/n_k
with sigma_k supported in a fixed window and v fixed. Along any sequence f'_n -> f, the window contribution to the shift
of u_k(x'_n) is v(x'_n - xhat)/n_k + K lambda_k sigma_k(x'_n - xhat)/n_k = V_n/n_k + o(lambda_k): the second term is
o(1) RELATIVE to the scale. So window moves (and moves of a', which act through U(e' - e) in the same way) give exactly
ONE effective conversion parameter for all v-resources: the absolute shift V_n. Individual conversions must come from
the FAR parts (coordinates escaping to infinity), whose capacity is governed by Cor 6.2 (free tail mass) and can be
limited to one scalar per detector group by an adversary (Lemma 6.4 discussion, tiny deviations allowed by Lemma 6.3).

## 8.3 Consequences

 * The bounded-conversion scenario of part 7 does NOT need guard coordinates: Prop 8.2 already blocks individual window
   conversions. The adversary's remaining requirements are (A1), (A3)-(A5) of part 7.3 and "far rigidity": far parts
   of the v-resources nearly collinear inside long detector groups.
 * Then the approximant has about three conversion parameters at a group transition (two group scalars and V), i.e.
   two adjacent scales with both types converted (plus one extra single-type band), and Model N predicts a positive
   boundary excess in the error-dominated regime (part 7.4 / final table).
 * Conversely, for a "generic" T (far parts of distinct resources quantitatively independent), the approximant can
   convert arbitrarily many adjacent scales through far moves (Cor 6.2), and Model M/N predict recovery.
Status: Prop 8.2 PROVED; the consequences SKETCH/HEURISTIC.
