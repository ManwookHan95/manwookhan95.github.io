# U2 part 3: item (E5) -- transporting the finite-F master theorems to infinite F; the VP rate is not needed; what remains is TUNING

Setting: the unified operator T_final of r8/U4 (D_Omega + D^{V2} + D^mu features, diagonal base), with the base replaced by mu*_s :=
2^{-2^{2^s}} (part 1.1) and Design(l) enlarged by B_mu*(l) := 2^{sigma(l)}/(mu*_{sigma(l)})^2 (the analogue of U4's fix C1); call it
T_final^*.  Clean sub-windows w = (l, i) as in V1 Theorem 2' (rate scheme (R1)-(R7) plus V2's minors), b = b(w), u = u(w),
T_lo = T_lo(w).  F arbitrary.  Labels as before.

## 3.0 Where VP entered, and why it is not needed in the transport
V3's Theorem M_inf raises an exactifying companion f^ex_j (built by Y1/V1/V2 at f) and then needs VP to keep the values of the GROWING set
L_0(j) of kept carriers, whose conditioning C_0(j) is an f-dependent rate (V3-ref Section 5).  Reverse the order: raise FIRST (deep, box
level, Lemma W of part 2), then exactify at the raised row.  The deep raise moves every value by O(eps_e) with eps_e <= C mu*_J psi(J),
which can be made <= b(w)^2 by the choice of J (2^J = O(log log(1/b(w))), absorbed by any window).  Then:

Lemma DR-inf (a deep raise preserves the clean classification).  PROVED.  Let w be clean for f, J with C mu*_J psi(J) <= b(w)^2 Phi_min(l)
(Phi_min(l) := min_{l'' <= l} Phi_{l''}, a design quantity), and f^r the deep box-level raise of f beyond J (part 2, (R), WITHOUT VP).  Then every
rate object of level l in (R1)-(R5), (R7) and every minor of V2's systems changes by at most C Design(l) b(w)^2 <= b(w); in particular every
tiny rate of f is <= 2b at f^r and every robust rate is >= u - b >= u/2 at f^r.  (R6) (shift costs, LP values) is continuous in the same data
with a design modulus: SKETCH.
Proof.  The raise does not change z, F, K, J, so (R1), (R2) are unchanged.  ||e^r - e|| <= 2||U^*Delta a||/nu <= C mu*_J psi(J) (V3 Lemma 2.1(b));
so |u_k(zhat^r) - u_k(zhat)| <= ||U^*u_k|| ||e^r - e|| <= C mu*_J psi(J) for every carrier, and the block scalars A_m, theta_m, M_m, C_m move by
<= C_f mu*_J psi(J) (V3 Lemma 2.2).  (R3), (R4) are |val|m/(Phi theta) (Lipschitz with constant <= C m/(Phi_min theta_min)); (R5) is a linear
form in values divided by Phi_max >= Phi_min; (R7) singular values move by at most the operator-norm change (Weyl); minors are polynomials of
bounded degree in values with design-bounded coefficients.  All constants are design quantities of level l times f-constants (theta_min,
nu); the choice of J absorbs them.  QED
Consequence.  VP (and (ND')) is not needed for the deep raise: the classification at w survives at f^r with factors 2, and all subsequent
exactification is done AT f^r, with f^r's own values.  The new requirement is that the exactifying moves of V1/V2 be available at f^r,
whose support is infinite.

## 3.1 What the finite-F assembly uses that depends on F (inspection of V1 Sections 3-4 and V2 Theorem B)
 (i)   (C1) closes rooms on S^nat_{l''} = S_{l''} \ (F cup T(l)) by z-moves: off F, unaffected by F infinite.
 (ii)  (C2) closes target rooms on T(l) \ F: off F, unaffected.
 (iii) (C3) donor raise: a z-move or a BANK at s_m := min(S_{c_m} cap (s_max(l), infinity)) of a robust-margin peak c_m (Lemma D);
       Lemma B (masses OFF the support) makes the bank private at first order.  At infinite F, s_m may lie in F.
 (iv)  (C4) and V2's Lojasiewicz tuning: Lemma TU with banks at j'_{l''} := min(S_{l''} cap (s_max(L), infinity)) and pulls at far
       j_{l''} in S_{l''} with v(j) in [eta, 2^G eta]; it assumes F^2 finite and z = eps_{l''} (contacts) on S_{l''} \ [1, s_max(L)].
       At infinite F, j' and the j may lie in F.
 (v)   Transplant (Prop TR), Theorem E'': the data's switching must be exact; on F it must be cushion-compatible: this is Lemma W
       (part 2) -- Lemma P pins kept carriers at shallow thin coordinates, the deep raise covers the rest; pinned carriers are
       removed by the threshold pigeonhole (faces of the pattern cones: V2's minors include all subsystems), shallow thin target
       coordinates in F become contact rows (a pattern of V1's G**, i.e. arbitrary contact patterns on T(l)).
 (vi)  Final step: V3 Theorem 2.5 + Y3 Theorem 2.1 at the companion (any F).
Items (i), (ii), (v), (vi) are available at infinite F (parts 1-2 and V3).  The ONLY new issue is (iii)-(iv): PRIVATE TWO-SIDED VALUE
TUNING for carriers whose design-depth signature coordinates lie in F ("support-swallowed carriers").

## 3.2 Lemma TR-inf (private tuning resources at infinite F).  PROVED in cases (a)-(c').
Let w be clean (factor 2) for the current row f° (forced data a°, z°, F° possibly infinite), L >= l a level, L_0 a finite set of carriers
<= L, eta := |x|_inf <= Design(L) b(w) the required increments x in R^{L_0}.  For l'' in L_0 consider the following RESOURCES, where
j'_{l''} := min(S_{l''} cap (s_max(L), infinity)) (design depth, j' <= sigma(L)) and d(L) := sigma(L) + 2^{L+2} (the first three coordinates
of each S_{l''} beyond s_max(L) lie in [1, d(L)]):
 (a)  [contact resources, V1]  j'_{l''} notin F° with z°_{j'} = eps_{l''}, and pull coordinates j in S_{l''} \ F° with v(j) in [eta, 2^G eta] and
      z° = eps_{l''} there;
 (a') [convertible support] as (a), except that j' in F° with |a°_{j'}| <= b(w), or a pull coordinate j in F° with |a°_j| <= theta b(w)^{1/2}/|L_0|
      (b(w)^{1/2} = T_lo^2/(l Design)^{1/2}), in each case with support sign s_j = eps_{l''}: LOWER these coordinates to contacts of sign
      s_j first (cost <= |a°_j|, zeroth order).  (With the opposite sign the roles of bank and pull are exchanged -- a bank at a contact of
      sign -eps lowers eps.val, a pull there raises it -- and Lemma TU's fixed point is the same with x replaced by -x on that carrier.)
 (c)  [robust Hilbert pair] two coordinates s < s' in S_{l''} cap F° cap (s_max(L), d(L)] with |a°_s|, |a°_{s'}| >= u and
      |1 - rho_{s'}/rho_s| >= u, rho_s := a°_s/v_{l''}(s);
 (c') [robust coordinate + anchor] one coordinate s' in S_{l''} cap F° cap (s_max(L), d(L)] with |a°_{s'}| >= u, together with a GLOBAL
      ANCHOR s_0 in F°, s_0 <= s_max(L) + 1 <= every tuned coordinate, with |a°_{s_0}| >= u and u_k(s_0) = 0 for every k in L_0 tuned by
      (c) or (c').
If every l'' in L_0 has one of (a), (a'), (c), (c'), then there is a row f^# (moves only at the listed coordinates) with
  val^#_{l''} = val°_{l''} + x_{l''} EXACTLY (l'' in L_0),  |u_k(zhat^#) - u_k(zhat°)| <= C_T eta^2 + (pull/bank side effects of V1 Lemma TU(b))
  for coarse k notin L_0 not touched by an anchor, and <= C_T eta for coarse k whose vector meets an anchor (these are re-tuned or robust),
  p*(f^# - f°) <= C_T eta log(e/eta) + (lowered masses <= |L_0| theta b^{1/2} + b),
with C_T = (f-constant) x Design(L)^C u^{-C}.
Proof.  Lemma B of V1 (masses off the support) is the only place where (a) needs j', j notin F°; after the lowering in (a') the coordinates
are contacts, so (a') reduces to (a) (Lemma TU of V1, verbatim, with s_j := mu*_j; its efficiency constant s'^2 v' >= (mu*_{sigma(L)})^2
2^{-sigma(L)} delta_min/2 is >= Design(L)^{-1/6} by the enlarged Design).  The lowering of j (|a°_j| small) is a "monotone move" of the
opposite kind: its transfer error is <= 2|a°_j| (zeroth order, part 1 and V3 Lemma 2.3's remark), and it changes e by
<= 2 mu*_j |a°_j|/nu, hence every value by <= C mu*_j |a°_j| <= C b^{1/2} (first order but tiny; the exact tuning below is computed at the
lowered row, so this change is absorbed).
Case (c) (support coordinates, no contact): for a move Delta at s in F°, with diagonal U,
   Delta val_k = (mu*_s^2/nu)(u_k(s) - gamma_k a°_s/nu^2) Delta + O(Delta^2),   gamma_k := <U^*u_k, U^*a°>   (V3 Lemma VP's Lambda),
i.e. a PRIVATE part (only k = l'' has u_k(s) != 0 among coarse carriers, s being beyond s_max(L) and in S_{l''}) and a COMMON part along the
fixed vector gamma, proportional to alpha_s Delta, alpha_s := mu*_s^2 a°_s/nu^2.  Take the pair (s, s') with Delta' := -alpha_s Delta/alpha_{s'}:
the common parts cancel exactly at first order.  Let the DEEPER coordinate s' do the work: Delta = -(alpha_{s'}/alpha_s) Delta', so
|Delta| = (mu*_{s'}/mu*_s)^2 (|a°_{s'}|/|a°_s|) |Delta'| <= u^{-1}|Delta'| (mu* is decreasing), and the private effect is
(mu*_{s'}^2 v(s')/nu)(1 - rho_{s'}/rho_s) Delta', of modulus >= c (mu*_{d(L)})^2 2^{-d(L)} delta_min(L) u |Delta'| >= Design(L)^{-1} u |Delta'|
(Design(L) contains (mu*_{d(L)})^{-2} 2^{d(L)}/delta_min(L)).  Both signs of Delta' are allowed: a same-sign raise is unlimited, a lowering
is limited by |a°|/2 >= u/2, and |Delta'|, |Delta| <= C Design u^{-2} eta << u for eta <= Design b.  (Pairing with a deeper partner the
other way round would require |Delta'| ~ (mu*_s/mu*_{s'})^2 |Delta|, astronomically large: the order matters for the base mu*.)  Second-order cross effects are O(Design^2 u^{-4} eta^2); the
simultaneous solution for all l'' (pairs are private to distinct carriers) is a fixed point exactly as in Lemma TU Step 2 (contraction
constant <= C Design^C u^{-C} eta << 1).  Cost: raises cost the footprint (V3 Lemma 2.3) mu*|Delta|; lowerings cost 2|Delta| (zeroth order);
both <= C Design u^{-2} eta << T_lo^2.
Case (c'): the anchor move Delta_0 at s_0 has private effects only on carriers whose vectors meet s_0 (not in the (c)/(c') part of L_0;
those in L_0 are re-tuned by their own resources in the same fixed point, the others are robust and move by <= C_T eta << u) and a
common part alpha_{s_0} Delta_0 gamma; put Delta_0 := -sum_{(c')} alpha_{s'} Delta_{s'}/alpha_{s_0}; since s_0 is not deeper than any tuned
s', |Delta_0| <= sum (mu*_{s'}/mu*_{s_0})^2 (|a°_{s'}|/|a°_{s_0}|)|Delta_{s'}| <= C |L_0| Design u^{-3} eta.  The
private effects mu*_s^2 v(s) Delta_s/nu are then free of common terms, and the rest is as in case (c).  QED

## 3.3 The residual of (E5) (precise) and its relation to (ND')
A carrier l'' in L_0 has NO resource of 3.2 iff, at the window w:
 (N1) every coordinate of S_{l''} beyond s_max(L) with v(j) >= eta (in particular j'_{l''}) lies in F° with |a°_j| > theta b^{1/2}/|L_0|
      (support-swallowed and thick down to the pull depth; no contact/free coordinate at usable depth), and
 (N2) the design-depth coordinates of S_{l''} cap F° beyond s_max(L) have pairwise rho-spread < u ("nearly proportional profile",
      a° ~ c_{l''} v_{l''} there), and there is no robust anchor avoiding the vectors of all such carriers.
Making the spreads |1 - rho_s/rho_{s'}| (s, s' among the first three coordinates of S_{l''} beyond s_max(l), l'' <= l) and the moduli |a_s|
(s in F cap [1, d(l)]) RATE OBJECTS of level l (finitely many per level, N-free, design-indexed), a clean sub-window makes each of them tiny
or robust; robust gives (c) or (c'); tiny |a_s| gives (a').  What remains is: tiny spread for all pairs and no anchor.  Exact version:
a° = c_{l''} v_{l''} on the shallow part of S_{l''} cap F for the carriers of a set L_d, and F cap [1, d(l)] covered by the vectors of L_d.
Then the only first-order resource for L_d on F is the family of columns (mu*^2 v/nu)(e_{l''} - (c_{l''}/nu^2) gamma), whose span is all of
R^{L_d} iff the Sherman-Morrison denominator 1 - sum_{L_d} c_{l''} gamma_{l''}/nu^2 is nonzero; V3's Remark to Lemma VP identifies its
vanishing with (ND') failure (a|_F in span{u_{l''}|_F}), on which sum c val drifts only at second order.  So the residual of (E5) is the
"near-(ND')" rate condition
 (NDN_w)  at every clean w of all large levels, some set L_d of kept carriers satisfies (N1), (N2) and |1 - sum_{L_d} c gamma/nu^2| <= b(w)
(the last quantity is again a rate object, so its robust case is covered by the Sherman-Morrison inverse with constant <= Design/u).
Remark (OPEN).  The coordinates tested in (N2) are the first ones of S_{l''} beyond s_max(L), which move deeper as L grows; so (N2) at
infinitely many levels does not force global proportionality of a on S_{l''} cap F (a profile that is nearly proportional on each tested
triple and thick at the pull depth is possible).  Whether (NDN_w) at all large levels can coexist with a mate that is not recovered by
other means is open; it is a condition on a only, of (ND')-near-degeneracy type, and is not generic (Baire: it fails after an arbitrarily
small perturbation of a on the tested coordinates, but such a perturbation is not available inside Lemma Z without a transfer argument).

Remark (where (NDN) leads).  Tuning is needed only to keep EXACT zeros of objects that are tiny at f (for objects built from FIXED
carriers, "tiny at all large levels" means "exactly zero at f", because b(w) -> 0; the companion moves -- deep raise, (C1)-(C3) -- perturb
them and the tuning restores them).  For a FIXED carrier the efficiency |1 - gamma_k rho_s/nu^2| of a shallow support coordinate s is a fixed
number, and it vanishes for every s in S_k cap F only if rho is constant (= nu^2/gamma_k) on S_k cap F; so for fixed carriers (NDN) is an
f-constant issue except in that exactly proportional case.  The rate character of (NDN) comes from carriers entering L_d at growing levels.
Alternatively, a near-neutral (NDN) carrier can be kept in NON-d-neutral data (Delta d_m = q_k tau'_k), which V2's Theorems E^>=, E^SC accept
when the blocks with Delta d_m < 0 satisfy (SC) at the companion: so (NDN) is contained in the same "(SC) at companions" problem as V2's
(C*-2) (part 4.1(c)).

## 3.4 Theorem M-inf (transport of Master Theorem III' to infinite F).  SKETCH (all ingredients PROVED except the items flagged).
For T_final^* and every N: a first row f with F INFINITE belongs to Rec_N unless, at all but finitely many levels, every clean sub-window
w has (C*_w) [V2-ref's coherent shift resonance, read at the deep-raised row f^r] or (NDN_w) [3.3] or a violation of (H2) or of the
(H3-inf)-type exclusions [bad degenerate peaks with the swallowing sign].
Route.  At a clean w of a level where (C*_w), (NDN_w) fail: (1) deep box-level raise f -> f^r beyond J (Lemma DR-inf; no VP);
(2) at f^r, V1's moves (C1)-(C3) and V2's Lojasiewicz tuning, with banks/pulls replaced by Lemma TR-inf where the coordinates lie in F;
(3) at the companion f^#, exact d-neutral window data from the transplant, cushion-compatible on F by Lemma W of part 2 (Lemma P +
pigeonholes; the shallow thin target coordinates are contact rows of the pattern); (4) V3 Theorem 2.5 (raise transfer: eps' = footprint
of the deep raise + V1's companion cost o(T_lo^2)) and Y3 Theorem 2.1 at f^# (infinite support allowed; (CS-side) from cushion
compatibility).
Flagged (not written line by line): (R6) continuity under the deep raise; V1 Lemma ST (status stability) with Lemma TR-inf's anchor side
effects (C_T eta on robust carriers: harmless by Lemma RR); V2 Theorem B with the extra pattern rows of Lemma W (pinned faces, contact rows on
shallow thin targets) -- these are subsystems of V2's systems, whose minors V2 already lists; window arithmetic (n(w) absorbs (W_inf)'s
rates because every f-dependent factor is now a rate object of the level or an f-constant^{l^2}).
So, modulo the flagged inspection items: Lemma Z at infinite F reduces to the finite-F residual (C*) (read at deep-raised rows) plus the
(ND')-type residual (NDN) of 3.3 plus the block exclusions shared with finite F.
