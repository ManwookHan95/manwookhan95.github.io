# H2 referee, part 2: Lemmas 2.4-2.7, Prop 3.1, Lemmas 3.2-3.4, Theorem H2.A, Section 4 (first pass)

## Lemma 2.4 (aggregated pulls) -- correct with precisions
K1 2.0 pullability: off F with eps_l z_1(j) > -1/2, or in F with s_j = eps_l and |a^r_j| <= x'_max (R-6).  Capacity (1 + eps_l z_1(j)) v_l(j)
in (v/2, 2v].  V1 TU with several pulls: total downward room Cap_l, bank gives every upward correction; two-sided on {||t|| <= W'} iff room
>= W' (factor 4 is a margin).  PRECISIONS: (i) pullability/super-thickness re-defined with x''_max (lowering threshold |a^r_j| <= x''_max), as
R-6 did; costs checked (part 1).  (ii) The compensating bank must raise eps_l val_l by Cap_l; mass <= 2 Design nu Cap_l.  Choose a SUBSET of
pulls with capacity in [4W', 8W'] (possible since each pull with v < 8W' has capacity < 16W'... take them in increasing v): bank O(Design W'),
second-order residue O(Design^2 W'^2) << rho_0-scale corrections.  (iii) cushion 24 lambda_l v_l(j) >= t|c_l| v_l(j) for t <= T_hi, any v.

## Lemma 2.5 (private minimality) -- correct as a statement about the refereed toolbox; two gaps
(1) z-move off the data sign at an anti-sign SUPPORT coordinate: the needed cushion is |a_s| >= t |c_l(t)| v_l(s)/5 for all t of the
    window; with |c_l(t)| >= K_*^2 K t/(4D) (K1.2) this is >= K_*^2 K T_hi^2/(20 D H) at t = T_hi (H2 writes T_hi/(C D H), which presumes
    |c_l| >= 1/(CD): not justified; the corrected bound still exceeds every affordable mass since T_hi^2 >> u^2 T_lo^2 = u^2 4^{-n} T_hi^2).
(4) "v_l(j) > x''_max: a flip is unaffordable": only cost UPPER bounds are available (Z3 Lemma 3.1, R-6 list).  A pull costs at least its
    support mass ~ 24 lambda_l v (p*-norm equivalent to l_1; the base change has l_1 mass >= v), i.e. >= c v/D(L), so pulls are provably
    unaffordable only for v >> D(L) u^2 T^2 theta'-budget, provably affordable only for v << u^2 T^2/(Design log(1/T)): a band of depths
    with undetermined status.  Lemma 2.5 holds for "moves of the toolbox within the certified budget" (x''_max = the certified limit), not
    for all admissible moves.  Not load-bearing for Theorem H2.A.
"Idea (1) literal: FALSE" -- correct: at s_j = -eps_l the term eps_l v_l(j) z_j = -v_l(j) is already minimal; lowering a_j keeps z_j;
the flip-and-pull composite has net capacity 0; lowering removes the deep-raise cushion of the anti-sign data.
"kind-(iv) pull ranges are ENTIRELY anti-sign super-thin support": overstated: [8W', x''_max] is entirely anti-sign (Cap < 4W'), pullable
coordinates with total capacity < 4W' may remain in [c_0 W, 8W').

## Lemma 2.6 / 2.7 (memory, sign persistence, deactivation) -- correct (mod chain)
Checked: (1) off-F far coordinates of an ACTIVE carrier's (or a shifted block's peak's) signature set are data-sign near-contacts: the
room of S_l on S^nat is tiny or robust at the clean sub-window (Y1/V1 rate objects); robust room puts an (FR)-type aggregated row on the
signature set (cert1: aggregated (X1) rows on S_l ∩ (L, s_far]) and forces gamma_l = 0; tiny room is closed by V1 (C1) in Step 0, so at the
Step-A row they are contacts with z = eps_l (pullable).  (2) pull range ⊂ E_c(w) (s_far(w) >= 2 log2(1/c_{L+1}) >= 2/(T ln 2) >> 5 log2(1/T)).
(3) at L'' the coordinate j is private among coarse carriers (new coarse carriers live on T(L'') ∌ j or on their own S_k), at design depth,
unraised (J(w'') > D(L'') >= j), in F with s_j fixed by f; K1.3(S) at L'' + K1.2 give the contradiction: v_l(j) <= 16 D b(w'')/(K_*^2 K t^2)
<= 16 D T_lo(w'')^2/(K_*^2 K) << c_0 W(w_p) (T_lo(w'') <= 2^{-n(w'')}, n(w'') >= Design(L'')^{20} >= 2^{20 D(L'')}).
(4) 2.7(a) contact case: anti-sign switching at a contact or near-contact (z_s = eps(1 - delta)) costs >= |Delta B(s)| in the flip budget
(excess |tau B|(1 - sgn(tau B) z_s) >= |tau B|(1 + 1 - delta)); |c^act| v_l(s) <= (1 + eta') t/q_0 + C c; with K_*(w')^2 K >= K_P(w') =
8 C_q 2^{J(w')} D(p')/delta_min(p'), 8 C_q >= 128/(3 q_0), 2^{J(w')} >> 2^{d(p)}: contradiction.  If delta >= u(w') the coordinate is free with
robust room at p' and l cannot be active at all.  Thin case: K1.3(S) at p' with |a_s| <= b(w') (needs (R1) at p': the proviso).
(5) privacy of OLD NEAR coordinates s in (s_max(p), d(p)] at p': s may be < p' (p' ~ 2 s_max(p)), so Lemma 2.2 alone does not suffice; the
cluster absorbers after p absorb E^ch(p) whose signature coordinates are <= s_max(p) (needs s_max(p) >= p: true for p >= 2 since every absorber
stage raises s_max by >= 2R + 2); PRE absorbers of round r+1 and the main target of p' lie in [1, r+1] (D-enum), r + 1 < p <= s_max(p) < s.  OK.
(6) peaks: data -Delta''_m lambda_c vs_c (robust peaks: Domega = 0 in the class cone, J2 1.3); vs_c and robustness are f's data.
Weak peaks (Sys-A rows): switching sign eps_k = vs_k sgn(e_k - Delta'_m) = sign of gamma_k = data sign on private coordinates; consistent
with the kind-(iv) orientation (1.2).

## Proposition 3.1 -- correct with precision
(a) re-derived (l1 >= l2 for the positive part; (1.1)-(1.2)).  (b) re-derived the one-sided column: bank at data-sign S_th near s of robust
peak c, z_s = -sgn(Delta''_m) vs_c, d kappa_m/d zeta(c) = vs_c (1 - X_m): y^T g = sgn(Delta''_m)(1 - X_m) lambda_c eff_s v_c(s) zeta_m
+ eff_s |kappa_y| theta_0 (the bank coordinate already carries mass theta_0: D_{Psi}(s) = Psi(s) - kappa a_s).  PRECISION: the bound is
sgn(Delta''_m) zeta_m >= -(4/3)(eps Design + |kappa_y| theta_0 Design) (H2 omits the theta_0 term; it is harmless: |kappa| theta_0 Design
<< c_1/|Lambda|^2 since theta_0 = b/Design^{C_P}).  (c) K2.16(2a).

## Lemma 3.2 -- correct (re-derived): separation of b'' from (W/2)Q - Box (compact convex, contains 0); both terms <= 0.
## Lemma 3.3 -- correct (mod J1.13): all |r^#| <= |rt| on banded K^- rows => R^2 does not increase => every status (Lemma K) <= target value,
   including robust peaks (margin u >> Design^C beta_1/kappa); protected statuses are upper bounds; Z_kappa untouched (free).
## Lemma 3.4 -- (a) correct WITH the coupled Brouwer argument of J1-ref F-2 (rescale ALL targets of the block; see Theorem H2.A below);
   (b) correct (J1.15' (J-f) second clause, P-D2 reading of "protected"); (c) SKETCH, label honest.

## Theorem H2.A -- correct with a fixable gap (coupling bookkeeping)
Case analysis re-derived (two/up/down; non-residual => every kind-(iv) row y_l <= c_1/(16|Lambda|) + small => sum < c_1/4, against 3.1(a)).
Size of the certificate: eps < 2(||b|| + rho_0)/W <= 4 u^3 Design^{-C_A} (W >= Design^{C_A} u^{-3} max(x, ||b||)): eps Design^{C_3+1}/u <<
c_1/|Lambda|.  GAP (G-CPL): K^+ bands in (U)-blocks need F-2's rescaling s_m (statuses), which moves the targets, the right-hand side and
(J1-ref P-1) every generator.  The proof's inequality sum_B beta_1 (y_l)_+ < phi_y + rho_0 <= ||b|| + rho_0 must be read at the coupled
targets rt(s): phi_y(s) = phi_y(1) + kappa_m (1 - s) zeta_m(y; rt(1)), and |zeta_m(y; rt(1))| <= (8/3) eps Design by R-PK (two-sided peak
resource, Fact 1.1(d)), so phi_y(s) <= ||b|| + 3 kappa_m (1 - s) eps Design with 1 - s <= C Design^C beta_1/kappa: the extra term is
<= C Design^{C+1} eps beta_1 << beta_1 delta_1.  [Using ||b(s)|| instead would FAIL: ||b(s)|| <= ||b|| + kappa (1 - s)||rt|| has an extra
C Design^C beta_1 of the size of the band itself.]  Then J1.8(a)-type realization for every s and the joint Brouwer argument of F-2(d).
The proof does not state this; it is J1-ref F-2 verbatim.  Fixed (proof in ref notes).

## Section 4
4.1 reformulation: uses H1 Lemma TF' (target displacement as lever; H1 unrefereed at writing; refereed in parallel).  The FUZZ of J1 7.4(b)
and the margin rho_0 must be kept: "<kappa y, Delta> <= eps'" is a near-certificate condition with eps' relative to the displacement size.
Proposition 4.1 -- Farkas algebra correct; "iff" overclaims: (i) single block with the other blocks' pinned ratios FIXED (a tiny minor may
contain (X3) rows of several blocks: cofactors of block m then depend on r^{(m')}, and the joint problem is multilinear); (ii) restricted
realization class (each kind-(iv) row only raised; shared design-depth generators at target coordinates and common modes ignored);
(iii) margins: realizability needs strict feasibility with margin ~ rho_0-scale (Example 4.3: residual iff M(rc) > -mu (C'_+ + C'_-)).
Corollary 4.2 -- FALSE as stated (several tiny minors): counterexamples (ref_cor42.py): (A) M1 = x1 + y, M2 = x1 + 2x2 + 3x3 + y (every
minor has a two-sided cofactor): residual iff 2rc_2 + 3rc_3 > 0; (B) M1 = x1 - x2, M2 = x2 - x1 + x3 + x4 (mixed signs in every minor):
residual iff rc_3 + rc_4 > 0.  CORRECT version: if the cofactor matrix on the pinned two-sided rows, C'_Q, has full row rank, the block is
not residual (2000/2000 random checks); the original statement holds for a SINGLE tiny minor.
Example 4.3 -- algebra correct (verified); realizability by an actual f open (stated in the notes; the part-file sentence "(R1) can be
genuinely obstructed at a single stage" is an overclaim).
