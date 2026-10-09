# G3 part 6: which properties of T are used where; the open core after G3; the missing lemma

## 6.1 Use of the design (Remark 1.3.1 made precise)
| Ingredient | Property of T used | Where |
|---|---|---|
| forced decomposition, uniform smallness, budget, first-order terms | Lemma B only (T1)-(T4) | 2.1-2.5 |
| pinning inequality | (P1): private signatures on disjoint S_l; targets of index l avoid S_{l'} for l' >= l (coarse-to-fine allowedness) | 3.2 |
| triangular solution | (P1) + delta_l > 0; amplification Lambda_f <= vartheta^{-l^2} Lambda°(l) | 3.3 |
| fine carriers negligible | (P2): sum_{l > l_*} lambda_l <= T_lo(l_*)^3 | 3.4, 4.2 |
| windowed averaging | (P3): windows with n^w_l >= l 2^{l^3} Lambda°(l) dyadic scales and T_hi(l) 2^{l^3} Lambda°(l) <= 1/l | 5.3 |
| transfer peaks | density of every tail of each block (Lemma B) | 5.1 |
| final recovery | C Thm 7.4 (any admissible T) | 5.2 |
| admissibility (Y cap c_00 = {0}, injectivity) | allowedness (b) + super-fast c_l (P1 2.1's argument) | 1.3 |
NOT used: rates of approximation of targets, any relation between delta_l and lambda_l, quantitative independence of targets, tameness or
margin sparsity of f, the structure of peaks/non-peaks, the number of active blocks, finiteness of the contact set.
Martin's own T (KLMW Prop 2.8, construction unknown to us) is covered only if its vectors carry private signatures with the
allowedness pattern and the weights have windows; nothing is claimed for it.

## 6.2 The open core O1-O4 (BRIEFING_R2 ADDENDUM 2) at first rows in R_0
For the SLD operator and f in R_0 (in particular at every base-tame f, with arbitrary blocks; and at f with infinite contact sets whose
signature sets keep room) Theorem B settles all four items:
 * O1 (infinitely many strict non-peaks, deep coefficients, failure of (MS), (MS-Q)): no block hypothesis is used; every carrier, peak or not,
   is a "coordinate with a two-sided capacity 2 gap/t" whose one-sided excess is pinned (4.2(c)).
 * O2 (second-order rebalancing): the budget controls the weighted invariant Gamma_w of every admissible decomposition (2.3(d)); transfer
   peaks realise Gamma_w at all scales below c_1 t uniformly (5.1). No engineering of approximants is needed: recovery is through
   C Thm 7.4's canonical truncations of an AVERAGED certificate at f.
 * O3 (approximate resonances, scale-dependent switching, near-threshold carriers, weak peaks, contacts/near-contacts as one-sided
   resources): every switching between the two sides of t = 0 is a two-sided difference Delta c, Delta B, pinned to O(Lambda_f(l_*) t) by the
   signatures (3.4-3.5). This is NOT a statement that approximate resonances are absent (they may be forced by the density of the tails and
   by the choice of f); it says their switching amplitude at scale t is O(K t), and the windows contain n >> K dyadic scales so that the
   averaging theorem absorbs them. The quantitative-independence hypotheses (QI), (HT), conversion capacity, (PC), (PC*) of Round 2 are
   all bypassed.
 * O4 (several active blocks, no (S)/(TC), cross-block relations): one ladder through all blocks; nothing block-specific is used.
Outside R_0 (Lemma Z) the items reappear only in the form "base-side one-sided resources sitting on signature sets, or infinite base support".

## 6.3 The missing lemma: Lemma Z (OPEN), its meaning and what is known
Lemma Z: for every f in S_{p_N*}, g in C(f), rho < 1, eps > 0 there is f' in R_0 with p*(f' - f) < eps and dist(rho g, C(f')) < eps.
By Theorem C it is EQUIVALENT to density for the SLD operator. Remarks:
 (a) (PROVED) It holds trivially on R_0. It holds for all mates of f that admit Round-2 engineering: every NA approximant is in R_0, so P2A Thm 2.1,
     N2 Thms 1-3, N2-ref Thm 3*, P2x Thm 3.5 (all valid for any admissible T, under their stated hypotheses) give Lemma Z for the exact two-piece
     mates they cover (hence for P1-type exact resonances with Delta d = 0 at signature-resonant f).
 (b) (Reformulation, PROVED) f is outside R_0 iff F is infinite or for every gamma, vartheta > 0 some signature set S_l (m(l) <= N) has
     ||h_l 1_{S_l cap J_gamma}|| < vartheta^l ||h_l||, i.e. (essentially) the one-sided base resources (support F, contacts, near-contacts) swallow
     the signature of some carrier, or of a fast sequence of carriers. Only these carriers lose their pinning; all others stay pinned.
 (c) (Freedom in Lemma Z, PROVED by Theorem B) The approximants need NOT be norm attaining: any f' with finite base support and room on a
     vartheta^l-fraction of every signature set will do, e.g. f' obtained from f by keeping z on all coordinates except a sparse
     subset of each non-roomy signature set, where |z'| is lowered to 1 - gamma, and by truncating a. Contacts elsewhere (infinitely many) can
     be kept. This is much more freedom than the NA engineering of Rounds 1-2 (which had to replace every infinite contact set by a finite
     window plus far pulls).
 (d) (HEURISTIC) The structure that remains is an exact-resonance structure: if only FINITELY many carriers are unpinned (finitely many
     signature sets swallowed), the argument of parts 3-4 shows that every admissible two-sided decomposition is "pinned part O(K t)" +
     "finitely many free carrier coefficients" + their base counterparts on F cup K cup near-contacts, i.e. an exact (finite-carrier) two-piece
     structure up to O(K t) on whole windows. Combining the window averaging of 5.2 with the engineered recovery of exact resonances
     (P2A/N2/S3) is the natural route to Lemma Z in that case; the case Delta d < 0 and the joint control of averaging and engineering are
     not written. OPEN.
 (e) (SKETCH) Infinite base support F with (SR): the proof of Theorem B goes through with three changes: clamp B_+(j) on F at 2|a_j|/t (the
     excess beyond the no-flip capacity |a_j|/t is one-sided and bounded by |B_+(j) - B_-(j)| plus flip costs, exactly as in 4.2(c));
     truncate the clamped base part to a finite set F_t with sum_{j in F \ F_t} |a_j| <= t^2; in 5.1 the base radius is then of order t (fine for
     |s| <= c_1 t); and use C Thm 7.4 for a not in c_00 with b in c_00 (C Remark 7.1' extended to b != 0 by the C referee, rem71_check.py).
     I have not written the details: SKETCH. If completed, the open core reduces to signature-resonant f only.

## 6.4 Consistency checks and skepticism
 * No counterexample is claimed or suggested. Theorem B is a positive statement on a dense class (it contains NA cap S_{p*}).
 * P1's example (exact resonance whose carrier's signature set is the contact set) is outside R_0 for the analogous design, consistent with
   its nonempty INTRINSIC defect (P1 Thm 2.4): at f in R_0 Theorem B shows there is no intrinsic defect at all relative to the
   Gamma_w-certificate class (every mate is a norm limit of Gamma_w-certificates in C(f)); so P1's phenomenon is exactly the failure of (SR).
   (Concurrent S3 notes claim P1's f is in R by other means; this is compatible.)
 * Corollary (PROVED, from the proof of Theorem B): for f in R_0, C(f) = closure of {g_c in C(f) : c balanced finite certificate, Gamma_w(c) <= 1}
   (the closure being taken in norm). Indeed 5.2 produces such rho g_c -> rho g. In particular C is lower semicontinuous at every f in R_0
   along every sequence along which C Thm 7.4's certificates transport (e.g. canonical truncations).
 * Sanity of the constants: every constant in parts 2-5 depends only on (f, g, rho, gamma, vartheta, N) or on the design; the design's
   super-exponential slack 2^{l^3} beats vartheta^{-l^2} and all fixed constants for l large, which is the only place where the order of
   quantifiers (T before f) matters.
 * Numerics: none were needed; all steps are exact algebra (2.3, 2.4, 3.2, 4.2) or imported refereed expansions (A Lemma 4.3, C (7.2),
   C (7.3), C Thm 7.4, which were numerically confirmed in Round 1).
