# Q1 part 3 — Master Theorem VI and the density criterion for every N

Setting: T_fin of part 1; parts 2.2-2.6 (Lemma CM^tr, Proposition BR, Lemma PM, Lemma S2c^tr, Theorem C^tr).
Rec(p_N) := {f in S_{p_N^*} : (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f)}.  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 3.0 Precision on option (b) in the design (needed for well-definedness)
Under option (b) the Lemma QC data of a pattern kappa with stage 1 in N_T(kappa) may be degenerate (mu_kappa may vanish: a coincidence
on the slice Phi_1 = 2^{-3} is not excluded by Lemma GEN).  In T_fin(b), (S5)-(S6) therefore take every minimum/maximum over kappa only
over the patterns with stage 1 notin N_T(kappa) (under option (a): over all patterns).  Lemma W_fin(b) then holds verbatim.

## 3.1 MASTER THEOREM VI.  PROVED (modulo the refereed results listed in 3.4; the combination argument of this round is unrefereed).
Let T_fin be the design of part 1 and p_N the corresponding norm on c_0 (I = {1..N}).
 (a) OPTION (a) (Martin-type norm, ||T_fin|| = c_1 < 1): for EVERY N >= 1 and every f in S_{p_N^*} whose base support F = supp a is
     finite, f is in Rec(p_N).
 (b) OPTION (b) (T_fin admissible, (T-a) with equality at stage 1, which lies in block 2):
     (b1) for N = 1 every f in S_{p_1^*} with finite base support is in Rec(p_1);
     (b2) for N >= 2 every f in S_{p_N^*} with finite base support and rho_1(f) != 1 is in Rec(p_N), where rho_1(f) is the relative position
          (lem:threshold) of the norm-one carrier (stage 1, block 2) at f.  The case rho_1(f) = 1 is OPEN (3.5).
Proof of (a).  Fix N, f, g in C(f), rho < 1.  Let l_f be the stage beyond which all f-constants are absorbed (as in U1-ref MT IV' and X2's
Theorem UE: r_f/2-ball of Lemma M2 reached by the companions, T_hi(w) <= t_1, C_f^{L^2} 2^{-L^3} small, the thresholds T_0(f, rho) of
Lemma S2c^tr).
Step 1 (clean sub-windows exist at every main stage).  For a main stage L the rate objects of level L, evaluated at f, are omega(L) real
numbers: the relative positions and margins (V1 (R1)-(R7)), the determinantal and shift objects (V2), and the minors and cofactor
polynomials of Gamma^#(kappa, a) for every pattern kappa and class a of level L, evaluated at the ratios r(f) computed with formula-1 kappa
and the pattern's Omega (U1-ref 4.3, X1 2.2(iv), X1-ref K1).  The M(L) = omega(L) + 1 sub-windows have pairwise disjoint bands (b(w), u(w))
(U4 Theorem 2.2(c): u(w^+) = b(w) < u(w); b only decreases when (D1), (D2) are added).  Each object lies in at most one band, so some
sub-window w(L) is CLEAN: every object is <= b(w) or >= u(w).  (V1 Theorem 2', U4 Lemma GW.)
Step 2 (a large class set at every clean sub-window).  For the given (g, rho) every dyadic scale t of W(w(L)) has exactly one activity class
(U1 2.3 with U1-ref (p-a), 4.5): no active shift, one-signed, or mixed — the three kinds are exhaustive.  Pigeonhole over the <= (J+1) 3^J
classes gives a class a with >= n(w)/((J+1)3^J) scales; Lemma CM^tr builds its companion; pigeonhole over the (A_max/eps)^p cubes of the
normalization (U1 Prop. 2.2(c),(d) with eps := c_f (u/Design)^C) gives a (class, cube) set S with |S| >= n(w)/D_cls(w) >= n(w)/D_cls(w)^2.
Step 3.  The hypothesis of Theorem C^tr therefore holds at w(L) for EVERY main stage L >= l_f, and Theorem C^tr gives (f, rho g) in cl NA.
rho < 1 and g in C(f) were arbitrary and cl NA is closed: f in Rec(p_N).  N was arbitrary and T_fin does not depend on N.  QED
Proof of (b).  (b1): stage 1 lies in block m_1 = 2, absent from p_1, so no pattern of p_1 contains it; by GEN_fin(b) all weights of p_1 are
algebraically independent over k_0 and the proof of (a) applies verbatim (X1-ref W2; alternatively Corollary IV^tr.1 by route X alone,
since for N = 1 every class is one-signed or unshifted).  (b2): rho_1(f) != 1 and b(w) -> 0 along the sub-windows (b(w) <= T_lo(w)^4) give
a stage L_1 such that for every main stage L >= L_1 and every sub-window w of L, |rho_1(f) - 1| > b(w): stage 1 is not near-threshold at f,
hence not in N_T(kappa) for the pattern kappa of f at any clean w of level L >= L_1; there GEN_fin(b) applies, and 3.0 makes the design
constants of these patterns positive.  The proof of (a) applies for L >= max(l_f, L_1).  QED

## 3.2 Corollary VI.1 (finite-F Lemma Z).  PROVED.
For T_fin (option (a); option (b) with N = 1) and every N: Lemma Z holds at every first row with finite base support, in the strong form
"f' := f".  Proof: Master Theorem VI.

## 3.3 Theorem VI.2 (the density criterion).  PROVED.
Let T_fin be as in 3.1 with option (a) (or option (b) and N = 1).  For every N >= 1 the following are equivalent:
 (i)  NA((c_0, p_N), l_2^2) is norm dense in L((c_0, p_N), l_2^2);
 (ii) (LSC-trunc)_N: for every f in S_{p_N^*}, every g in C(f), every rho < 1 and every eps > 0 there is f' in S_{p_N^*} with FINITE base
      support such that p_N^*(f' - f) < eps and dist_{p_N^*}(rho g, C(f')) < eps.
Proof.  The norm of an operator S = (h_1, h_2) : (c_0, p_N) -> l_2^2 satisfies ||S|| <= p_N^*(h_1) + p_N^*(h_2).
(ii) => (i).  Let f in S_{p_N^*}, g in C(f), rho < 1, eps > 0.  (LSC-trunc)_N gives f' with finite base support and g' in C(f') with
p^*(f' - f) < eps and p^*(g' - rho g) < eps.  By Master Theorem VI, f' in Rec(p_N), so (f', g') in cl NA; ||(f', g') - (f, rho g)|| < 2 eps.
Hence (f, rho g) in cl NA for all f, g, rho, and prop:reduction(b) (every norm-one operator into l_2^2 is, after a rotation of l_2^2, of the
form (f, g) with g in C(f); density <=> all (f, rho g), rho < 1, in cl NA) gives (i).
(i) => (ii).  If NA is dense, lem:pair gives norm-attaining f_n -> f with rho g in Li_n C(f_n); every norm-attaining f_n in S_{p_N^*} is
nabla p_N(x_n) and has base part a_n in c_00 (prop:smooth(c), prop:approximants; BRIEFING (R4)), i.e. finite base support.  So (ii).  QED
This is Z5's Proposition 5.4 (T13a, refereed as a correct reformulation) with its first condition ("Lemma Z at every f with finite base
support") now PROVED for T_fin; the proof above does not use the SLD-specific thm:reductionZ, only prop:reduction(b), lem:pair and Master
Theorem VI (Rec in place of R_0).  The results of the note used (prop:reduction, lem:pair, prop:smooth, prop:approximants) are [any T] in
U4's audit; they use (T-a) only as the inequality q^*(Te) <= 1 (through Phi_m(k) <= 2^{-m-k}); the equality clause of (T-a) appears in the
note only in the definition and in the verifications of admissibility (lines 144-154, 2344, 3990 of martin_density_note.tex), never in an
argument.  Hence Theorem VI.2 holds for the Martin-type norm of option (a).
Corollary VI.3 (Martin's p).  If (LSC-trunc)_N holds for infinitely many N, then NA((c_0, p), l_2^2) is dense for the Martin-type norm p
(I = N) built with T_fin.  Proof: Theorem VI.2 and lem:martintail (whose proof uses only |R_m x|_m <= m 2^{-m} q(x), valid for ||T|| <= 1;
T_fin is N-independent).  PROVED.

## 3.4 Dependency tree of Master Theorem VI and status flags
Unrefereed (this round): T_fin and Lemma W_fin, Theorem A_fin, GEN_fin, the interaction checks I1-I10 (part 1); Lemma CM^tr, Proposition BR,
Lemma PM, Lemma S2c^tr, Theorem C^tr (part 2); Master Theorem VI, Corollary VI.1, Theorem VI.2, Corollary VI.3 (part 3).
Refereed tools used (with the round's referee fixes):
 * note (Sections 1-8, [any T] and [SLD] tools of U4 4.2): lem:threshold, lem:F1 (clamp formula), lem:suplevel, eq:peakshift, def:twopiece,
   def:engineered and thm:engineered (proof), lem:block, lem:base, lem:bookkeeping, lem:TV, prop:rebalancing, lem:transferdata,
   lem:persistence, lem:approxfacts, lem:anchor, def:SC, lem:scrambling, lem:slack, prop:reduction, lem:pair, prop:smooth, prop:approximants,
   prop:continuity, lem:martintail.
 * U4 + U4-ref: T_final, Lemma GW, Theorem 2.2 (bands disjoint, (P1)-(P3)); V1 (Theorem 2', Lemmas D, TU, CO, ST, (C1), (C2), Proposition
   TR(iii)-(iv)); V2 (Lemmas H, L, Theorem B); Z3 Lemma 3.1; U3 Lemma VT (U3-ref F6).
 * U1 with U1-ref (single pass; several statements proved BY the referee): Lemmas 1.1-1.5, 2.1, 2.4, activity classes 2.3 (p-a), Proposition
   2.2 (p-b)-(p-d), Lemma 3.2 under D^{U1'} (6.4), Lemmas 4.1-4.3, 4.5, 4.6, Lemma R-kt (2), Proposition KN (3.3, for (KN)-blocks), rows 4.1-4.5,
   G1 release (5), D^{U1'} (6), Lemma 4.2(ii) repair (7).
 * X1 with X1-ref (single pass; fixes proved by the referee): Lemmas K, F, EC, the floor row (X4^0) and weight-freeness, Lemmas NLM, GEN, QC,
   Proposition KN^tr (with KN-1, D2, S-0, K1, Q1-Q3, W-fix), Lemma W' (W1-W4).
 * X2 with X2-ref (single pass; (R-abs), Lemma CM', Theorem C_mix' proved BY the referee): Lemmas M1, M1', M2, identities 1.4 and referee
   addition 1.2, Lemma DC (p-DC1)-(p-DC3), Lemma LV(a)-(c) (p-LV1), (p-LV2), Lemma UE-1 and Theorem UE ((p-UE1)-(p-UE7), (c3')), Theorem E^eng
   (p-E1), (S2c) with (W_exp) (p-W), design D^{X2}.
 * Z5 Proposition 5.4 (refereed: correct reformulation), re-proved in 3.3.
NOT used: Master Theorems II, III' and V4's results (the class pigeonhole covers every F-finite row directly); the features (W5), (W6), (W7)
at absorber/cluster stages, (FD); Theorem S1's RT*(c) and the zero-value absorbers (route X only, an alternative for one-signed classes).

## 3.5 What remains open (precise)
 (O1) (LSC-trunc)_N for some/every N — equivalently (Theorem VI.2) density for p_N built with T_fin.  This is the infinite-base-support half
      of Lemma Z (Z5 T13; U4's (E1)-(E5), U2's items: transport of the finite-F master theorems to infinite F (M-inf SKETCH), tuning
      regularity modulus, (W_inf), (SC) along deep raises, status coherence at infinite F).  Nothing in this round bears on it.
 (O2) Option (b), N >= 2: rows with rho_1(f) = 1 exactly at which stage 1 is an active near-threshold carrier of a (T)-block at clean
      sub-windows of infinitely many levels, with a coincidence on the slice Phi_1 = 2^{-3}.  Precisely: whether 2^{-3} can be a critical value
      of psi_1 restricted to a stratum of Z_kappa identically in the generic parameters (X1-ref W2 slice remark).  Under option (a) this does
      not arise.  Option (b) for N = 1 is settled (3.1(b1)).
 (O3) Martin's own operators (an arbitrary admissible T from Lemma B): Master Theorem VI is for the designed T_fin only.
 (O4) Martin's p (I = N): by Corollary VI.3, density follows from (LSC-trunc)_N for infinitely many N; row-wise statements do not transfer.
No counterexample is claimed; nothing found points to one.  Density of NA((c_0, p_N), l_2^2) (every N) and of NA((c_0, p), l_2^2) remain
OPEN, now reduced EXACTLY to (LSC-trunc) for the Martin-type norms built with T_fin.
