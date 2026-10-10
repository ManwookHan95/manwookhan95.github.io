
## 3. Master Theorem VI and the density criterion

### 3.1 MASTER THEOREM VI.  PROVED (modulo the refereed results listed in 3.5; the combination argument of this round is unrefereed).
Let T_fin be the design of Section 1 and p_N the corresponding norm on c_0 (I = {1, ..., N}).
 (a) OPTION (a) (Martin-type norm, ||T_fin|| = c_1 < 1): for EVERY N >= 1 and every f in S_{p_N^*} whose base support F = supp a is finite,
     f is in Rec(p_N): (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f).
 (b) OPTION (b) (T_fin admissible with (T-a) holding with equality at stage 1, which lies in block 2):
     (b1) for N = 1 every f in S_{p_1^*} with finite base support is in Rec(p_1);
     (b2) for N >= 2 every f in S_{p_N^*} with finite base support and rho_1(f) != 1 is in Rec(p_N), where rho_1(f) is the relative position
          (lem:threshold) at f of the norm-one carrier (stage 1, block 2).  The case rho_1(f) = 1 is OPEN (3.6).
Proof of (a).  Fix N, f, g in C(f) and rho < 1.  Let l_f be the stage beyond which all f-constants are absorbed (as in U1-ref's MT IV' and X2's
Theorem UE: companions in the r_f/2-ball of Lemma M2, T_hi(w) <= t_1, C_f^{L^2} 2^{-L^3} small, T below the thresholds T_0(f, rho) of
Lemma S2c^tr).
Step 1 (a clean sub-window at every main stage).  For a main stage L the rate objects of level L evaluated at f are omega(L) real numbers: the
relative positions and margins (V1 (R1)-(R7)), V2's determinantal and shift objects, and the minors and cofactor polynomials of Gamma^#(kappa, a)
for every pattern kappa and class a of level L evaluated at the ratios r(f) (formula-1 kappa with the pattern's Omega: U1-ref 4.3, X1 2.2(iv),
X1-ref K1).  The M(L) = omega(L) + 1 sub-windows of L have pairwise disjoint bands (b(w), u(w)) (U4 Theorem 2.2(c): u(w^+) = b(w) < u(w); adding
(D1), (D2) only lowers b), and each object lies in at most one band; so some sub-window w(L) is CLEAN: every object is <= b(w) or >= u(w)
(V1 Theorem 2', U4 Lemma GW).
Step 2 (a large class set).  For the given (g, rho) each dyadic scale t of W(w(L)) has exactly one activity class (U1 2.3, U1-ref (p-a), 4.5),
and the class is of one of the three exhaustive kinds (no active shift, one-signed, mixed).  Pigeonhole over the <= (J+1) 3^J classes gives a
class a with >= n(w)/((J+1) 3^J) scales; Lemma CM^tr builds its companion; pigeonhole over the (A_max/eps)^p cubes of the normalization (U1
Proposition 2.2(c), (d), eps := c_f (u/Design)^C) gives a (class, cube) set S with |S| >= n(w)/D_cls(w) >= n(w)/D_cls(w)^2.
Step 3.  The hypothesis of Theorem C^tr holds at w(L) for EVERY main stage L >= l_f; hence (f, rho g) in cl NA.  As rho < 1 and g in C(f) are
arbitrary and cl NA is closed, f in Rec(p_N).  N was arbitrary and T_fin does not depend on N.  QED
Proof of (b).  (b1): stage 1 lies in block m_1 = 2, absent from p_1, so no pattern of p_1 contains it; by GEN_fin(b) the weights of all
carriers of p_1 are algebraically independent over k_0, and the proof of (a) applies verbatim (X1-ref W2); alternatively 2.7(b) (route X alone).
(b2): rho_1(f) != 1 and b(w) <= T_lo(w)^4 -> 0 give L_1 such that |rho_1(f) - 1| > b(w) for every sub-window w of every level L >= L_1; then stage 1
is not near-threshold at f, so stage 1 notin N_T(kappa) for the pattern kappa of f at any clean w of level L >= L_1; for these patterns GEN_fin(b)
applies and the design constants of (S5)-(S6) (restricted as stated there) are positive; the proof of (a) applies for L >= max(l_f, L_1).  QED

### 3.2 Corollary VI.1 (finite-F Lemma Z).  PROVED.
For T_fin (option (a), or option (b) with N = 1) and every N: Lemma Z holds at every first row with finite base support in the strong form
f' := f (no approximation of f is needed).  Proof: Master Theorem VI.

### 3.3 Theorem VI.2 (density <=> (LSC-trunc)) and Corollary VI.3.  PROVED.
Let T_fin be as above with option (a) (or option (b) and N = 1).  For every N >= 1 the following are equivalent:
 (i)  NA((c_0, p_N), l_2^2) is norm dense in L((c_0, p_N), l_2^2);
 (ii) (LSC-trunc)_N: for every f in S_{p_N^*}, g in C(f), rho < 1 and eps > 0 there is f' in S_{p_N^*} with FINITE base support such that
      p_N^*(f' - f) < eps and dist_{p_N^*}(rho g, C(f')) < eps.
Proof.  For S = (h_1, h_2) : (c_0, p_N) -> l_2^2, ||S|| <= p_N^*(h_1) + p_N^*(h_2).
(ii) => (i): given f in S_{p_N^*}, g in C(f), rho < 1, eps > 0, (LSC-trunc)_N gives f' with finite base support and g' in C(f') with
p^*(f' - f) < eps and p^*(g' - rho g) < eps; f' in Rec(p_N) by Master Theorem VI, so (f', g') in cl NA and ||(f', g') - (f, rho g)|| < 2 eps.
Hence (f, rho g) in cl NA for all f, g, rho, and prop:reduction(b) (every norm-one operator into l_2^2 is, after a rotation of l_2^2, of the form
(f, g) with g in C(f), and density holds iff all (f, rho g), rho < 1, lie in cl NA) gives (i).
(i) => (ii): lem:pair gives norm-attaining f_n -> f with rho g in Li_n C(f_n); every norm-attaining f_n in S_{p_N^*} equals nabla p_N(x_n) and
has its base part in c_00 (prop:smooth(c), prop:approximants), i.e. finite base support.  QED
This is Z5's Proposition 5.4 (T13a; refereed as a correct reformulation), whose first condition (Lemma Z at every f with finite base support) is
now PROVED for T_fin; the proof uses only prop:reduction(b), lem:pair, prop:smooth, prop:approximants (all [any T] in U4 4.2) and Master
Theorem VI (with Rec in place of R_0; NA ∩ S ⊂ Rec trivially: if f attains its norm at x_0 and g in C(f), then g(x_0) = 0 and (f, g) attains
its norm at x_0).  These results use (T-a) only as q^*(Te) <= 1 (through Phi_m(k) <= 2^{-m-k}); in the note the equality clause appears only in
def:admissible and in the verifications of admissibility (lines 144-154, 2344, 3990 of martin_density_note.tex), never in an argument.  Hence
Theorem VI.2 holds for the Martin-type norm of option (a).
COROLLARY VI.3 (Martin's p).  If (LSC-trunc)_N holds for infinitely many N, then NA((c_0, p), l_2^2) is dense for the Martin-type norm p (I = N)
built with T_fin.  Proof: Theorem VI.2 and lem:martintail (its proof uses only |R_m x|_m <= m 2^{-m} q(x), valid for ||T|| <= 1; T_fin is
N-independent).

### 3.4 The answers in one paragraph
For the single N-independent operator T_fin (option (a)), every first row with finite base support of every finite-block norm p_N is
recovered: all its mates are limits of norm-attaining operators (Master Theorem VI).  The two routes are compatible because they are used on
different rows and the only things route V takes from route X are the conclusions of Proposition KN^tr (exact cone, threshold protection,
coupling rows); KN-1's exact hold lives in the companion's joint fixed point, d-consistency transports it exactly to the engineered approximant,
and the Puiseux margin is protected there by the freezing of C_m (Lemma PM).  The non-explicit Puiseux exponent costs only a factor
O(log(1/T)) in the exponents of the window constants, which (W_exp) absorbs (Lemma S2c^tr).  Consequently density of NA((c_0, p_N), l_2^2)
is EQUIVALENT to (LSC-trunc)_N for every N (Theorem VI.2), and (LSC-trunc)_N for infinitely many N gives density for p (Corollary VI.3).

### 3.5 Dependency tree and status flags
Unrefereed (this round): T_fin and Lemma W_fin, Theorem A_fin, Lemma GEN_fin, checks I1-I10 (Section 1); Lemma CM^tr, Proposition BR, Lemma PM,
Lemma S2c^tr, Theorem C^tr (Section 2); Master Theorem VI, Corollary VI.1, Theorem VI.2, Corollary VI.3 (Section 3).
Refereed tools used (with the round's referee fixes):
 * note: lem:threshold, lem:F1 (clamp formula), lem:suplevel, eq:peakshift, def:twopiece, def:engineered and thm:engineered (proof), lem:block,
   lem:base, lem:bookkeeping, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence, lem:approxfacts, lem:anchor, def:SC, lem:scrambling,
   lem:slack, prop:reduction, lem:pair, prop:smooth, prop:approximants, prop:continuity, lem:martintail.
 * U4 + U4-ref: T_final, Lemma GW, Theorem 2.2; V1 (Theorem 2', Lemmas D, TU, CO, ST, moves (C1), (C2), Proposition TR(iii)-(iv)); V2 (Lemmas H,
   L, Theorem B); Z3 Lemma 3.1; U3 Lemma VT (U3-ref F6).
 * U1 + U1-ref (single pass; several statements proved BY the referee): Lemmas 1.1-1.5, 2.1, 2.4, classes 2.3 (p-a), Proposition 2.2 ((p-b)-(p-d)),
   Lemma 3.2 under D^{U1'} (6.4), Lemmas 4.1-4.3, 4.5, 4.6, Lemma R-kt, Proposition KN (for (KN)-blocks), rows 4.1-4.5, G1 release, D^{U1'}, Lemma
   4.2(ii) repair.
 * X1 + X1-ref (single pass; fixes proved by the referee): Lemmas K, F, EC, the floor row (X4^0) and weight-freeness, Lemmas NLM, GEN, QC,
   Proposition KN^tr (KN-1, D2, S-0, K1, Q1-Q3, W-fix), Lemma W' (W1-W4).
 * X2 + X2-ref (single pass; (R-abs), Lemma CM', Theorem C_mix' proved BY the referee and re-derived here as Lemma CM^tr / Theorem C^tr):
   Lemmas M1, M1', M2, identities 1.4 with the referee addition 1.2, Lemma DC ((p-DC1)-(p-DC3)), Lemma LV(a)-(c) ((p-LV1), (p-LV2)), Lemma UE-1
   and Theorem UE ((p-UE1)-(p-UE7), (c3')), Theorem E^eng ((p-E1)), (S2c) with (W_exp) ((p-W)), design D^{X2}.
 * Z5 Proposition 5.4 (refereed), re-proved in 3.3.
NOT used: Master Theorems II, III' and V4's results (the class pigeonhole covers every F-finite row directly); (W5), (W6), (W7) at absorber or
cluster stages, (FD); Theorem S1's RT*(c) and the zero-value absorbers (route X, an alternative only).

### 3.6 What remains open (precise)
 (O1) (LSC-trunc)_N for some/every N — by Theorem VI.2 EQUIVALENT to density for p_N built with T_fin.  It is the infinite-base-support half of
      Lemma Z (Z5 T13; U4's (E1)-(E5) and U2's items: transport of the finite-F master theorems to infinite F (M-inf, SKETCH), tuning regularity
      modulus, (W_inf), (SC) along deep raises, status coherence at infinite F).  Nothing here bears on it.
 (O2) Option (b), N >= 2: rows with rho_1(f) = 1 exactly at which stage 1 is an active near-threshold carrier of a (T)-block at clean
      sub-windows of infinitely many levels, with a coincidence on the slice Phi_1 = 2^{-3} (Phi_1 rational, so Lemma GEN does not apply).
      Precisely: whether 2^{-3} can be a critical value of psi_1 restricted to a stratum of Z_kappa for all values of the generic parameters
      (X1-ref W2 slice remark; if 2^{-3} is a regular value of psi_1 on every stratum, the slice version of Lemma NLM settles it).  Under option
      (a) this does not arise; option (b) for N = 1 is settled (3.1(b1)).
 (O3) Arbitrary admissible T (Martin's own Lemma B operators): Master Theorem VI is proved for the designed T_fin only.
 (O4) Martin's p (I = N): by Corollary VI.3 density follows from (LSC-trunc)_N for infinitely many N; row-wise statements do not transfer.
No counterexample is claimed; nothing found points to one.  Density of NA((c_0, p_N), l_2^2) (every N) and of NA((c_0, p), l_2^2) remain OPEN,
now reduced EXACTLY to (LSC-trunc) for the Martin-type norms built with T_fin.

## 4. Numerics (sanity checks only; r10/Q1_work/)
 (N1) pm_check2.py / pm_check3.py (+ .out): independent block model (mpmath, 50-80 digits), threshold equations (E1), (E2); robust peaks, one
      near-threshold strict non-peak d tuned to rho_d = 1 - mu with mu in {1e-8, 1e-12, 1e-16, 1e-20}, fine carriers of total weight mu^2
      (as c_{L+1} <= b^2 <= mu^2/64), every value perturbed by a relative amount r in {1e-3, 1e-4, 1e-2, 1e-5} >> mu.  Untuned, the perturbation
      moves rho_d by ~r and makes d a PEAK in 7 of 12 instances; after imposing d-consistency on ALL coarse strict non-peaks (fixed point in
      A'), rho_d = 1 - mu to all printed digits and |C' - C| is at the working precision (<= 1.6e-73 at 80 digits for mu in {1e-8, 1e-12, 1e-16},
      7 instances; the clamp-equation bound of Lemma PM(ii) holds); CONTROL: with one coarse strict non-peak left untuned, |C' - C| ranges over
      3e-9 ... 1.3e-4 and d becomes a PEAK in 6 of 12 instances (Lemma PM needs the levers on all of Omega, X2-ref 1.2).  [pm_check.py, a full
      row model with masses, was too slow and was replaced; the row-level lever mechanism is X2's Lemma DC, checked numerically by X2 and
      X2-ref.]  The first (50-digit) run of pm_check3 showed |C' - C| up to 1e-19 for mu = 1e-16, 1e-20: a bisection-resolution artefact (bracket
      [0, max nu] with nu ~ 1/Phi_fine ~ 1e40); it disappears at 80 digits with 520 bisection steps (the mu = 1e-20 instances did not finish
      within the time limit at 80 digits).
 (N2) s2c_check.py (+ .out): log_2-scale arithmetic of Lemma S2c^tr with the worst case Design(L) = n(w) and absolute exponents C in {3, 10, 30},
      f-constants up to 1e12: the threshold comparison 64 rho eps/delta <= s_late and exp(-1/(2T)) <= s_late hold for all n >= 16 ... 23 (T = 2^{-n});
      at n = 60, log_2 s_late ~ -4e5 ... -3.4e7 against log_2(64 rho eps/delta) ~ -1.7e18.  (In T_fin, n(w) >= L 2^{L^3} Q(w) is astronomically larger.)
These checks cannot exhibit infinite-dimensional failures; they confirm the two quantitative mechanisms new in this round.

## 5. Points for the referee
 * Lemma CM^tr's proof claims that X2-ref's CM' uses Proposition KN only through (i) statuses, (ii) kind-[3] rows, (iii) exactness; check
   X2-ref 4 ((a)-(d)) line by line against this claim, in particular the dominance (U1 Lemma 4.2) and the trace-correction bound with the
   TRUE shift in (T)-blocks (X1-ref S-0).
 * The KN-1 hold is realized INSIDE Step A's joint fixed point; Step B's G1 release moves the held values by <= 4 c_{L+1}^2 — check that
   X1-ref's S-0 indeed covers the G1 release in route V (no absorber tuning in between).
 * Lemma PM(ii): the clamp-equation argument requires that the coarse peaks stay clamped and that the natural peak gives a slope bound on the
   ball of Lemma M2; fine status changes are covered by the min(...) bound.
 * Lemma S2c^tr: K_w is polynomial in 1/gap_min, 1/x_0 with ABSOLUTE exponents (X2 Lemma UE-1, X2-ref (p-UE1)-(p-UE6)); if some exponent were
   design-dependent the bound exp(C log^2(1/T)) would become exp(C Design log^2(1/T)) <= exp(C log^3(1/T)), still dominated by (W_exp).
 * The pull coordinates of Lemma DC are chosen unused by Step A (2.3); the extra factor 2^{2G(L)} enters only C_2.
 * Option (a) leaves the note's class only through the equality clause of (T-a), which no argument uses (3.3).
