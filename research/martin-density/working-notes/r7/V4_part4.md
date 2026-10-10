# V4 part 4 — Exact negative-d-mismatch data are rigid; the design question (GO); multi-block rays (B)

Notation of parts 1-3.  SLD-type design with (SF*), diagonal U, F finite.

## 4.1 Dominance at a coordinate
**Lemma 4.1 (dominance).  PROVED.**  Let c = (c_k) be coefficients with |c_k| <= C_0 lambda_k for all carriers k, let j notin F, and
let k_0 be the first carrier with c_{k_0} u_{k_0}(j) != 0.  If |c_{k_0}| >= 2^{-3} C_0 lambda_{k_0} (a "non-negligible" leading
coefficient), then sgn(sum_k c_k u_k(j)) = sgn(c_{k_0} u_{k_0}(j)) and |sum_k c_k u_k(j)| >= |c_{k_0} u_{k_0}(j)|/2.
*Proof.*  As in Step 6 of Theorem 2.2: if j in S_{k_0}, later contributions total <= 2^{-5} lambda_{k_0} v_{k_0}(j) C_0 (allowedness (b)
for j > m+k+4: ratio <= (5/18) 2^{m+k-j} < 2^{-5}; (SF*) for j <= m+k+4: ratio <= 2^{-9}); if j in supp y_{k_0} \ S_{k_0}, later contributions are <= C_0 (4/3) sum_{k > k_0} lambda_k <=
2^{-9} C_0 lambda_{k_0} eta_{k_0} <= 2^{-9} C_0 lambda_{k_0} |u_{k_0}(j)| n_{k_0}; carriers earlier than k_0 have c_k u_k(j) = 0.  With
|c_{k_0}| >= 2^{-3} C_0 lambda_{k_0} the leading term is at least four times the rest.  QED

## 4.2 Rigidity of exact data with Delta d != 0
For two-piece data put D := b^+ - b^- = sum_m R_m^*(omega^-_m - omega^+_m) - sum_m Delta d_m R_m^* w_m = sum_k c_k u_k with
c_k = lambda_k [ (omega^-_{m(k)} - omega^+_{m(k)})(k) - Delta d_{m(k)} w_{m(k)}(k) ]  (|c_k| <= C_0 lambda_k, C_0 := max|omega| + 2 max|Delta d|).
Call k NEGLIGIBLE if 0 < |c_k| < 2^{-3} C_0 lambda_k, and a carrier with c_k = 0 NEUTRAL (for k not carrying omega: w(k) = 0 or
Delta d_{m(k)} = 0).
**Proposition 4.2 (rigidity).  PROVED.**  Let (b^+-, omega^+-) be two-piece data at f (F finite).  At every free coordinate j (|z_j| < 1,
j notin F), every carrier k with j in supp u_k is neutral or negligible, or there is an earlier negligible carrier at j.  In
particular: (a) a carrier k of a block with Delta d_m != 0 that is not neutral, not negligible and carries no omega has NO free
coordinate in its support, unless an earlier carrier at that coordinate is negligible; (b) if no carrier is negligible, then for every
free coordinate j all carriers with j in their support are neutral.
*Proof.*  D(j) = 0 at free j (Lemma 3.3).  If the first carrier k_0 with c_{k_0} u_{k_0}(j) != 0 were non-negligible, Lemma 4.1 would
give D(j) != 0.  So either all c_k u_k(j) vanish, or k_0 is negligible.  QED
Reading.  NEGLIGIBLE carriers (not carrying omega) have |w(k)| < 2^{-3}(C_0/|Delta d|) — tiny d-weights; these are "nearly d-neutral" carriers whose values
are tuned extremely close to 0 (the nearly neutral rate objects K_nn of Z6/Y2).  Apart from them, exact negative-d-mismatch data
force every free coordinate to be "dead" (only neutral carriers there) and every non-neutral carrier of a block with Delta d != 0
to be supported in F ∪ K.  Combined with Lemma 3.4 (GM): every NEAR-THRESHOLD carrier of such a block with w != 0 (weak/degenerate
peak, tiny-gap strict non-peak) beyond an f-dependent level is tuned through F (its support meets F), or has an earlier negligible
carrier at one of its free coordinates.

## 4.3 Exact data at rows with (SC), and the role of (GO)
**Corollary 4.3.  PROVED.**  If g in C(f) carries two-piece data with kappa_w <= 1 and the blocks with Delta d_m < 0 satisfy (SC), then
(f, g) in cl NA (Theorem thm:engineered).  In particular this holds at every row whose blocks with Delta d < 0 have no degenerate peak
and whose near-threshold carriers obey the criterion of Lemma 3.8 (e.g. finitely many near-threshold carriers, any number of
d-neutral ones: w = 0 gives gap = M, which never enters Scr at small scales).
**Correction of a tempting step (FALSE as stated).**  "Perturbing a with z fixed gives (T2)-preserving companions" is FALSE in general:
by density (T-d) every block has infinitely many F-dependent carriers whose values tend to 0 (targets approximating vectors y* with
supp y* ∩ F != {} and y*(zhat) = 0); a perturbation p of a moves y*(zhat_F) off 0 linearly in p, so for every p != 0 infinitely many of these
carriers change the sign of their value, their coefficients c_k change sign, and D^# fails to be z-signed on their signature sets
(Lemma 4.1).  The repair is to RE-ALIGN the flipped carriers, with hysteresis:
**Lemma 4.4 (perturb-and-realign companions).  PROVED** for rows built by the owner rule from some level K on (in particular for
self-aligned rows, Theorem 2.2, with any finite set of exceptional carriers tuned through F).  Let f be such a row and a(p) a smooth
family in {supp a = F, signs fixed, q*(a) = 1}, a(0) = a.  Define f^p by re-running the owner recursion from level K with a(p), keeping
eps_l(p) := eps_l(0) unless eps_l(0) A_l(p) <= -(B_l + delta_l H_l)/2, in which case eps_l(p) := sgn A_l(p) (FORCED flip).  Then every
non-exceptional value satisfies n_l|val_l(p)| >= (B_l + delta_l H_l)/2 with sign eps_l(p).  (a) A forced flip at l requires
|A_l(p) - A_l(0)| >= delta_l H_l/2 (as eps_l(0) A_l(0) >= 0), hence delta°_l <= 2C|p|, so the first flipped carrier
l(p) -> infinity as p -> 0, and p*(f^p - f) <= C(|p| + sum_{l >= l(p)} lambda_l log(...)) -> 0 (Z3 Lemma 3.1 for the z-part, continuity
for the a-part); (b) every non-exceptional carrier is a robust peak at f^p with varsigma = eps_l(p) (Theorem 2.2 Step 4 with |val| >= delta°_l/2);
(c) the exceptional carriers (finitely many, coarse) have values continuous in p.
*Proof.*  (a) With eps fixed, n_l val_l(p) = A_l(p) + eps_l(B_l + delta_l H_l) and |A_l(p) - A_l(0)| <= C|p| ||y_l 1_F||_1 (only F-coordinates
and coordinates re-assigned by earlier forced flips change; the latter occur only beyond l(p)); a forced flip needs A_l(p) eps_l <=
-(B_l + delta_l H_l) while A_l(0) eps_l >= 0.  (b), (c) as in Theorem 2.2.  QED
**Proposition 4.5 (exact data at self-aligned rows with degenerate peaks are recovered).  PROVED.**  N = 1 (or block-aligned rows).  Let f be
a self-aligned row (Theorem 2.2) with finitely many exceptional carriers tuned through F, among them EXACTLY DEGENERATE swallowing-type
peaks and swallowed q < 0 strict non-peaks, so that (SC) FAILS at f.  Then every g in C(f) carrying two-piece data with kappa_w <= 1 and
omega supported on the exceptional strict non-peaks and Delta d <= 0 satisfies (f, g) in cl NA.  (At self-aligned rows exactness
forces Delta d <= 0: with Delta d_m > 0 the term -Delta d_m R^* w_m is (-z)-signed at every coordinate dominated by a peak.  The mirror
statement holds at anti-aligned rows, z = -varsigma on every signature set, with Delta d >= 0.)
*Proof.*  Take f^p of Lemma 4.4 for generic small p (|F| >= 2 since each tuning uses two coordinates of F): the exceptional carriers move
continuously and, for p outside a finite union of hypersurfaces, none is degenerate; the q < 0 carriers stay strict non-peaks with q < 0
(open condition); f^p has finitely many strict non-peaks, no degenerate peak and (MS) (owner-rule margins), so f^p is (BT) and satisfies
(SC).  (T1) holds by continuity.  (T2): every coefficient c_k^p is non-negligible with the sign forced by coherence: peaks have
w^p = varsigma M^p with varsigma = eps (owner rule, also after re-alignment), the formerly degenerate peaks keep the sign of their value,
and on S_{l_-} the omega-term dominates as in Proposition 3.2(ii); by Lemma 4.1 (owners dominate) D^p is z^p-signed with no free coordinate
in its support.  Lemma 3.6 transplants the data (cost -> 0 by Lemma 4.4(a)), Theorem 3.7 concludes.  QED
So the typical instance of Problem prob:resonant (negative d-mismatch with a degenerate peak, where (SC) fails) is recovered for the
designed operator; the proof uses only finitely many tuned carriers.
**Theorem 4.6 (scope of the perturb-and-realign route).  SKETCH.**  For a row f (F finite) and exact two-piece data with Delta d <= 0 and
kappa_w <= 1, the route of Proposition 4.5 works whenever (i) f is owner-rule aligned from some level K on, (ii) the blocks with Delta d < 0
contain no NEGLIGIBLE carrier and only finitely many NEUTRAL carriers below level K, and (iii) only finitely many near-threshold carriers
of these blocks are tuned through F ((GO) gives (iii) automatically; (GM) excludes contact-only tuning; Proposition 4.2 excludes free-
coordinate tuning of non-neutral carriers).  The general row need not satisfy (i): its fine levels may be coherent through sign choices
other than the owner rule, and re-aligning them by the owner rule moves z at infinitely many coordinates whose dominant term belongs to a
coarse NEUTRAL carrier ("dead zones", e.g. the signature set of a coarse d-neutral carrier hit by fine targets), where the fine re-aligned
signs need not match the frozen coarse z.  Gaps: dead zones; (GO).
**Consequence.**  For the designed operator, the exact-data part of residual (C) (negative d-mismatch at coherent rows) is reduced to:
(alpha) rows whose coherence uses dead zones of neutral or negligible carriers, (beta) infinitely many near-threshold carriers tuned through
the finitely many parameters of F (a design question: (GO)).  The non-exact part of (C) (mates whose decompositions are not exact data) is
the window-method problem of producing exact Delta d != 0 data, which Proposition 4.2 shows is only possible at coherent rows.

## 4.4 What a counterexample with exact data would need (synthesis)
A pair (f, g), g with exact two-piece data, not recovered, must have F finite, |F| >= 2, a block with Delta d_m < 0 in which (SC) fails,
coherence of D (Proposition 4.2), and a failure of the perturb-and-realign route: dead zones of neutral/negligible carriers, or infinitely
many F-tuned near-threshold carriers.  Every z-move at a coordinate where D != 0 breaks (T2) (the dominant coefficient fixes the sign
required of z, Lemma 4.1), every coordinate lies in supports of infinitely many carriers of every block (Lemma 1.2), and a-moves flip
infinitely many small F-dependent values: this is the RIGIDITY of negative-d-mismatch data.  It explains why donors (Y2) work only for
d-neutral data, and it is the reason why the window method's residual (C) cannot be treated by companion moves alone.

## 4.5 (B) multi-block rays: block-triangular structure
**Lemma 4.5 (block-triangularity).  PROVED.**  At strict non-peaks q_l = (q_0/sigma_m) eps_l val_l (Y4-ref C.7), so D_m depends only on
the values of carriers of block m; the zero-cost cone C(kappa) depends only on the pattern (signs, contact types), not on values.
Per-carrier exact tuning (Y4-ref Prop. P4) changes the values of a prescribed finite set exactly and all others at second order.
**Proposition 4.6 (sequential projection).  PROVED.**  Let C be a pointed polyhedral cone in [0, inf)^U, D = (D_1, ..., D_N) linear,
C_0 := C, C_i := C_{i-1} ∩ ker D_i, and D^(i)_min := min{ |D_i(rho)| : rho extreme ray of C_{i-1}, ||rho||_1 = 1, D_i(rho) != 0 }.
Then for tau in C:  dist_1(tau, C ∩ ker D) <= sum_{i=1}^N (1 + ||D||)^{N-i} |D(tau)|_inf ... more precisely, with tau^0 := tau and
tau^i the point of C_i given by Y4 Lemma 1.8 applied to (C_{i-1}, D_i, tau^{i-1}),
   ||tau^i - tau^{i-1}||_1 <= |D_i(tau^{i-1})|/D^(i)_min,   |D_i(tau^{i-1})| <= |D_i(tau)| + ||D_i|| sum_{i' < i} ||tau^{i'} - tau^{i'-1}||_1.
*Proof.*  Y4 Lemma 1.8 for each i (C_{i-1} is a polyhedral cone in the nonnegative orthant); the second line since D_i is Lipschitz.  QED
The extreme rays of C_i are the extreme rays of C_{i-1} with D_i = 0 and, for each 2-face of C_{i-1} spanned by rays rho_a, rho_b with
D_i(rho_a) > 0 > D_i(rho_b), the "sliced ray" |D_i(rho_b)| rho_a + |D_i(rho_a)| rho_b.  So the vector-valued d-row is replaced by N scalar
d-rows on nested cones, and the joint objects (R6) of Y4 become the scalar numbers D_i(rho) for sliced rays rho.
**Remaining step for (B) (precise).  OPEN.**  Exactify, block by block (i = 1, ..., N), the tiny values D_i(rho) of the extreme rays of
C_{i-1} by tuning the values of block-i carriers only (block-<i values frozen: D_1..D_{i-1} and hence C_{i-1} are unchanged).  The tuning
system is LINEAR in the block-i values with matrix R^(i) = (rho(l))_{rho tiny, l in block i}, feasible (x = -val), so the only issue is its
Hoffman constant: the coefficients rho(l) of sliced rays are products of design numbers and ROBUST earlier d-values, and near-dependence of
two tiny sliced rays' coefficient vectors is a new joint object (a minor of R^(i)) that cheap tuning cannot repair (a tiny minor can be
moved only by O(budget^deg)).  (B) is therefore reduced to: tiny minors of sliced-ray matrices at clean sub-windows.  At (BT) points the
issue does not arise (Corollary 3.1), and with finitely many switchable carriers the point is (BT).
