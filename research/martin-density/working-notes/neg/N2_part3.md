# N2 (negative track) part 3: what a counterexample must contain, the adversarial designs beyond part 2, and why
# neither side wins outright

## 3.1 Inheritance (the lesson of part 2)

PRINCIPLE 3.1 (inheritance under canonical truncation).  HEURISTIC in general; PROVED for T_PB (Thm 2.4).
Let F be finite and f_N := f[a, z 1_{[1,N]}] (NA, f_N -> f).  Then
 (a) EXACT: a' = a, e' = e, zhat_N = zhat on [1,N] and zhat_N - zhat = -z 1_{(N,inf)}; hence u(zhat_N) = u(zhat) - u(z 1_{(N,inf)}) for
     every functional u, i.e. every carrier's value changes only by its pairing with the tail of z beyond N, and every base
     coordinate in [1,N] keeps its status (support, contact, free with the same room).  PROVED (definitions).
 (b) the threshold of each block moves only through the carriers whose tails beyond N are not small relative to their margins;
     if a dominant peak pins the threshold (as in T_PB), relative positions of all other carriers are preserved up to their tails.
     PROVED in T_PB (Lemma 2.2); in general a quantitative version needs Lemma T(f) (perturbed raising moves).
 (c) consequently every decomposition of a mate at f that uses only resources whose usability is decided on [1,N] up to errors
     small against their margins/gaps/rooms transports to f_N with relative error -> 0, at ALL scales.  This is what happened in
     part 2 (resources: staircase peaks on {2,3} with private tails <= Phi^2).  HEURISTIC as a general statement (the
     transport of an arbitrary family of decompositions requires uniform control of first-order level terms; in T_PB it was done
     by hand).

LEMMA 3.2 (two-sidedification of far-valued carriers).  PROVED.
Assume U e is supported in F (true for a diagonal U, since then e = U*a/||U*a|| is supported in F) and F subset [1,N].  Let k be a
carrier with u_k = v^near + v^far, v^near supported in [1,N], v^near(zhat) = 0, v^far supported in (N, inf).  Then u_k(zhat_N) = 0, so
k is a strict non-peak of f_N with w_N(k) = 0.  Proof: zhat_N vanishes on (N, inf) and equals zhat on [1,N]; and zeta(k) = 0 excludes
k from the peak set, because on P the identity zeta/|zeta| = alpha + D^2 w/C has two terms of the same sign, the second nonzero
(Part I lem:threshold); off P, w(k) = C zeta(k)/(Phi(k)^2|zeta|) = 0.  So one-sided carriers whose VALUE comes entirely from far coordinates become exactly two-sided (d-neutral) at the
canonical truncation: their one-sided role at f is upgraded, not destroyed.

LEMMA 3.3 (near free coordinates stay free).  PROVED.
If f'_n -> f in S_{p*} (NA or not) and l is a coordinate with |z_l| < 1, l notin F, then z'_n(l) -> z(l); in particular l is a free
coordinate of f'_n for large n with room -> 1 - |z_l|.  So a near free coordinate of f can never be made a support coordinate
("banked") or a contact along a convergent sequence.
Proof.  Part I prop:continuity: z'_n -> z weak*, i.e. coordinatewise; z'_n(l) = sgn a'_n(l) on supp a'_n has modulus 1.  QED

LEMMA 3.4 (base switching vanishes off the finite window at NA rows).  PROVED (G3 Lemma 1.4(c), applied at an NA row f').
For every mate g' of an NA row f', every t > 0 and every pair of decompositions of f' +- t g' with max-norm <= s(t), the switching
vector V = B_+ - B_- satisfies sum_{j free at f'} (1 - |z'_j|) |V_j| <= t/q'_0; all but finitely many coordinates are free at f'.

CONSEQUENCE 3.5 (necessary structure of a counterexample with F finite).  HEURISTIC (it combines PROVED facts 3.1(a), 3.2-3.4 with
the heuristic 3.1(c)).
A pair (f, rho g), F finite, can fail to be recovered only if g, at arbitrarily small scales, needs order-one one-sided resources
whose usability is destroyed at EVERY NA approximant.  By 3.1 such resources cannot be decided on finitely many coordinates; by 3.2
they cannot be block carriers whose values come entirely from far coordinates; by 3.4 base switching of order one must be carried
by infinitely many contacts (or near-contacts) of f.  What is left:
 (A) BASE resonances: switching vectors V(t) of order one on infinitely many contacts, with block transfer carriers (exact
     resonances, or approximate ones whose contact parts move outward as t -> 0);
 (B) CANCELLATION designs in the blocks: carriers whose far parts carry large values compensated by near parts (so the truncation
     turns them into robust peaks of both signs instead of two-sided carriers), used in groups whose far parts cancel in the mate;
 (C) infinite base support ((LSC-trunc), not treated here).

## 3.2 Design (B): cancelling pairs, and the approximant's answers (HEURISTIC throughout, with the PROVED inputs marked)

Model: pairs p (depth Phi_p -> 0), u_{1,p} = (v - F_0 e_A + phi_p)/n, u_{2,p} = (v + F_0 e_A - phi_p - psi_p)/n with v(zhat) = 0 (the mate
direction, near), e_A a near direction with e_A(zhat) = 1 supported on free coordinates, phi_p far with phi_p(zhat) = F_0 - kappa Phi_p,
psi_p a small far correction with psi_p(zhat) = 2 kappa Phi_p.  Both members are negative peaks with margins ~ kappa Phi_p (type +);
the mate gamma v uses c(u_{1,p} + u_{2,p}) on side +, whose near parts and far parts cancel up to O(Phi); a mirror family (type -)
serves side -.  At f_N the members of pairs with far parts beyond N have values ~ -F_0 and ~ +F_0: robust peaks of opposite signs,
useless.  (This is the configuration that 3.1-3.2 do not cover.)
Approximant answers found:
 (i) RESTORATION: phi_p(z') = phi_p(z) can be reproduced with finitely many far coordinates; any finite set of pairs is restored at
     cost 0 (far moves change only deeper carriers).  Only finitely many pairs can be restored when ||phi_p||_inf <= F_0/delta_0
     (spread far parts; then restoring infinitely many pairs forces |z'| >= delta_0 on infinitely many coordinates, z' not in c_0) --
     the adversary must spread the far parts.
 (ii) GROUP RESTORATION: if the far parts are shared (one phi for all pairs, or for infinitely many pairs), one scalar phi(z') restores
     all of them at once and the whole structure is inherited (as in part 2) -- the adversary must use infinitely many independent far
     parts.
 (iii) CROSSING CONVERSION at the transition depth: with independent far parts per pair (or per group), convert u_{1,p} (set
     phi_p(z') so that its value is 0) and u_{2,p'} of another pair p' (set phi_{p'}(z') accordingly).  The near parts v -+ F_0 e_A of the
     two converted members cancel in e_A exactly; the far parts are on far coordinates and can be banked (far banks only affect
     deeper carriers); the partners u_{2,p}, u_{1,p'} stay type-+ peaks.  This gives two-sided d-neutral carriers of 2v below the
     transition with no near frozen error.  So (B) with independent pair far parts is recovered (at model level).
 (iv) what the adversary needs to block (iii): near parts that do NOT come in cancelling +- pairs, i.e. each conversion leaves a NEAR
     frozen error e_A in a fixed finite-dimensional "error space" E_c on near free coordinates.  By Lemma 3.3 near free coordinates
     cannot be banked, so the frozen error must be absorbed by block carriers ("absorbers": carriers nearly orthogonal to zhat with an
     E_c-component, converted by a near lever of size equal to their value) or paid at first order in the base.  The adversary then
     needs slow rates (absorbers convertible only by near moves of size >> their depth, which destroy the preserved structure above
     the transition) and a sign rule (one-sided absorbers on each side carry E_c-components of the wrong sign).  This is exactly E's
     rigid design (A1)-(A5) (r1/E_notes.md 7.3).
In the rigid design the approximant has, at the transition, a bounded number of independent levers (near moves along the few
directions seen by the switching carriers, plus group scalars), hence a bounded number of conversions; E's Model N then gives a
positive excess R(J) - 1 (1-19% for J <= 4 converted scales) in a constant-factor band of scales above the transition, i.e. failure of
THESE approximants for rho close to 1 (NUMERICAL, model level).  Not excluded: other approximants.  Two new observations here:
 (v) at NA rows block switching is allowed at all scales (part 2), so the approximant does not need to make the structure two-sided
     at the transition at all -- it may RE-CREATE one-sided structure below the transition by moving carrier values: making a peak a
     weak peak does not change its own coordinate w'(k) = +-M' (only the global data M', C', thresholds and non-peak values move, by
     amounts controlled by the size of the move through Lemma T).  The only constraint is the base-switching
     constraint 3.4: the + and - side carriers used below the transition must have near parts that coincide up to O(t) on free
     coordinates and far/contact parts supported in the finite window.  Hence the decisive adversarial property is a LINEAR one:
     (LIN) for small t, no two families of carriers at depth >~ t that can be made weak peaks of opposite orientation by admissible
     moves have near restrictions (on free coordinates of f) agreeing up to O(t) modulo window vectors.
     (LIN) must hold for all approximants simultaneously; it is incompatible with Martin's near-duplicates ONLY if two near-duplicates
     can be pushed to opposite signs, which needs a value separation >~ Phi (sign rule, Part I rem:resonancetypes): with tiny private tails
     (far rigidity) they cannot -- so far rigidity HELPS the adversary here, while it HELPED the approximant in part 2.
 (vi) the Gordan (relative) lever: if the switching carriers' values come from a common near error direction e_0 (values -+ kappa
     Phi e_0-coefficient), a near move along e_0 shifts all of them toward the threshold by the same relative amount; it changes no
     status (only margins), so its cost is that of the deep sign flips it causes, which for generic carriers with values >= tau(Phi)
     is ~ tau^{-1}(eta) -- negligible when tau decays slowly.  It lowers ALL peak costs by a factor (1 - c eta): a free global saving.  It
     does not convert anything, and in an error-dominated design (peak costs a small fraction a_0 of the budget) the saving is small
     (E 7.3: "does not obviously close the gap").

## 3.3 Design (A): base resonances with an adversarial T (status)

 * Exact resonances, d-neutral (Delta d = 0): recovered for EVERY admissible T (P2A Thm 2.1 / r2 N2 Thm 1, refereed).
 * Exact, Delta d >= 0: recovered under (TC) (P2x Thm 3.5); Delta d < 0: recovered under (SC) (Part I thm:engineered) or (PC*) (N2 referee
   Lemma R).  Without (SC): Part I rem:withoutSC -- recovery for rho^2 kappa_w + rho sum |Delta d_m| K^scr_m < 1; for rho close to 1 OPEN.
   An adversarial T with (SC) failing (block vectors in zhat^perp at a positive proportion of indices of one block, strict non-peaks
   with w = 0 at all fine scales) is a natural candidate.  NOTE (HEURISTIC): such carriers stay two-sided at f_N as long as their
   pairing with z 1_{(N,inf)} is small against their depth; the deep ones form the scrambled set of Part I lem:anchor (they may become
   peaks), which is exactly what (SC) quantifies.  A non-canonical truncation that keeps u_k(zhat') = 0 for finitely many of them by
   choosing z' beyond N (one linear condition each) is available; whether it removes the anchor cost for rho close to 1 is OPEN.
 * Approximate base resonances whose switching vectors V(t) move outward (contact parts of the transfer carriers at depth Phi live
   beyond N(Phi) -> infinity): the window banks (Part I def:engineered) handle the base part at all scales below the bank scale; the block
   transfer carriers below the window are destroyed (their contact parts become free coordinates and their values jump by the
   contact mass).  Answers: keep the contact parts of the transfer carriers down to any finite depth as contacts (finite window
   extension, cost 0); below, convert transfer carriers by INWARD moves of their own contact parts (private contact parts = private
   levers; inward moves keep contacts one-sided at scales >> the move) -- the transition problem of 3.2 again, with near frozen
   errors only if the transfer carriers carry critical errors on near free coordinates.  SKETCH.

## 3.4 What a non-recovery proof would need, and why it is out of reach

By Part 1 (Remark 1.3, Lemma 1.1, Lemmas 1.4-1.5) a proof that (f, rho g) is not in cl NA must give, uniformly over ALL NA f' within
delta of f, a primal witness: a direction y in a fixed finite-dimensional space E of finitely supported vectors and a scale t at which
the "relevant carriers" of f' in direction y are too few (Lemma 1.4: relevant = strict non-peaks and peaks with margin <~ t|u_k(y)|, at
depth >~ t).  The approximant chooses x' and thereby the values u_k(x') of all carriers: making a peak relevant (reducing its margin)
costs NOTHING in ||f' - f|| unless the status changes; converting it costs ~ lambda_k; far coordinates are free; near coordinates must
converge (Lemma 3.3) but may move by o(1) amounts that are >> the depth of every deep carrier.  So the required uniform statement is a
quantitative RIGIDITY of the whole dense family (u_k) relative to xi: for every x' weak*-close to xi, the carriers made relevant at
the critical scale cannot reproduce rho g on E.  Such a statement would have to control infinitely many carriers of all depths and
all moves of x' simultaneously; it is (LIN) of 3.2(v) plus E's (A2)-(A5), quantified over all x'.  No technique for such
uniform-over-approximants lower bounds exists in the sources, and every concrete adversarial T examined here or in Rounds 1-14 has
had at least one approximant family that recovers it or that is not excluded.  STATUS: OPEN; no non-recovery statement is claimed.

## 3.5 Answer to the strategic question ("approach it negatively?")
 * The negative approach is not easier: it requires a uniform lower bound over all NA approximants of an infinite-dimensional
   variational quantity (the transition cost), whose positive counterpart is precisely the "exactness versus one-sidedness" problem
   of ADDENDUM 13 seen from the other side.
 * The adversarial choice of T (no private levers, far rigidity, near-duplicates, slow rates) does NOT by itself create an
   obstruction: in the cleanest adversarial row (part 2) far rigidity makes the canonical truncations recover every mate gamma h,
   including mates that are defects of all intrinsic mechanisms (K(f) = {0}).
 * A counterexample, if it exists, needs the rigid design (A1)-(A5) plus (LIN) at every scale, consistent with Lemma B, and a proof
   technique for uniform lower bounds -- none is in sight.  The consistent evidence (Rounds 1-14 and this round) is that each
   adversarial mechanism has a recovering approximant family that is easy to find once the mechanism is explicit.
 * Leaning: positive (density) for the problem as posed; for the negative program the realistic target is a MODEL-LEVEL statement
   (a finite "transition cell problem" whose optimal excess is > 1), not a theorem about p_N.
