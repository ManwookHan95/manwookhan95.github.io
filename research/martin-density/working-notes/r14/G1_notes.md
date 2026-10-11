# G1 (Round 14): exactness only where it is needed -- cushioned Hoffman bound, strict/soft split, linear Step A, split preparation

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "Mod chain" = modulo the links cited by J1-ref Theorem J1.15', J2 Theorem J2.1,
H2 Theorem H2.A and Part III (Prop. III-cushion, Lemma III-CMtr, Lemma III-prep, Lemma III-track, Lemma III-count), with their
referee status.  Part files: r14/G1_part1.md ... G1_part5.md.  Scripts and outputs: r14/G1_work/.

## 0. Summary

The transplant of Part III (Prop. TR / Lemma CM^tr / Step A targets) needs the realized active ratios on Z_kappa for ONE reason: the
coarse data of the mate are projected onto the class cone Gamma^#(kappa, a; r), and V2 Lemma H bounds the Hoffman constant by
(norm)^{n-1}/(least NONZERO minor); a tiny nonzero minor gives a constant ~ 1/b.  G1 shows:

(1) A cushioned, face-wise Hoffman lemma (Lemma CH, PROVED): with rows split into STRICT rows (equalities, strict inequalities) and
    CUSHIONED inequality rows, and only the rows MET by the data counted, the projection constant is p^{p/2} Lambda^p/u (design type)
    provided the met strict minors are 0 or robust and the met minors containing a cushioned row are <= mu or robust; the cushioned
    rows are then violated by at most 2^{n/2}(mu/u)|x'|.  Exactness is NECESSARY for strict rows (two-ray example) and NOT needed
    for minors containing a cushioned row.
(2) In the class cone, every row at a target coordinate that is a contact or (raised) tiny support of the prepared row, and every
    inward row (X4^0)/(X4), is cushioned at the companion with tolerance >= 2 theta/t; only (X3) rows, (X1-FR) rows (free target
    coordinates with robust room) and single-variable rows are strict (Lemma 2.1).  Hence (Theorem G1.A, Cor. G1.B) exactness is
    needed only for STRICTLY PINNED ratios (on Z^str_kappa, the zero set of the tiny STRICT minors); soft tiny minors need only
    |M| <= mu_tol(w), and mu_tol >= Des^{10} b: the near-exactness gap F-NE (b >> s_1/T >> delta_Z) concerns strict objects only.
(3) Strict tiny minors with one (X3) row are AFFINE with design coefficients and are exactified linearly (Lemma LE); a single
    two-(X3) strict minor too (Lemma 5.1).  Step A runs at the linear scale x^nat = Des^C b (Step A^nat), all bookkeeping constraints
    (K2-d), (L-K2-1), (L-K2-2), (W_exp), (LATE), Lemma S2c^tr, Lemma III-drift re-checked (Lemma 3.3); Theorem G1.C realizes a stage
    with single-(X3) strict structure whenever the band-relaxed Step-A^nat system is A-regular (near-threshold carriers descend
    linearly, also inside Z^str when strictly pinned: Lemma 5.5).
(4) A split preparation P^nat (bank/raise mass theta_T = b T_hi (Des/u)^{C_T} at target coordinates, theta_pr at private ones)
    reduces the bank/raise bias on strict objects to b_bias = b T_hi (Des/u)^C << b, keeps every cushion (Lemma 4.2); a move at a
    coordinate j never changes, to first order, a minor containing the row of j (Lemma 4.4).
(5) Consequences: H2 Example 4.3 (the contact-row resonance underlying the persistent-(R1) candidates) and every resonance whose tiny
    minors contain a cushioned row are REALIZED (Cor. 5.4); the preparation-bias source of H2.B is reduced to b_bias; (X4^0)-nonlinear
    pinned groups and cofactor-polynomial exactness disappear; the Puiseux/Lojasiewicz scale disappears where the strict structure is
    single-(X3) (Lemma LE, Lemma 5.5).  REMAINING (Theorem G1.D): (R-S1) one-signed STRICT linear resonances (Farkas alternative over
    tiny strict minors made of one (X3) row and FR rows, annihilated by every FR generator, Prop. 5.2/Cor. 5.3), (R-S2) systems of
    multi-(X3) strict minors, (R-S3) one-sided blocking of linear near-threshold descent, (R-L) locked K^+ rows, (R0^str) H1's
    thick-type residuals with "pinned" read as "strictly pinned".  (LSC-trunc)_N for every f and density remain OPEN.

| # | Result | Status | Sec. |
|---|---|---|---|
| 1 | Lemma CH (cushioned face-wise Hoffman lemma), Cor. CH.1 (parametric form) | PROVED | 2 |
| 2 | Remark CH(c): exactness necessary for strict rows | PROVED (two-ray example) | 2 |
| 3 | Lemma 2.1 (tolerances of cushioned rows at the companion) | PROVED (mod chain) | 3 |
| 4 | Lemma 2.3 (soft tolerance mu_tol >= Des^{10} b) | PROVED | 3 |
| 5 | Theorem G1.A (soft transplant: exactness only for tiny strict minors) | PROVED (mod chain) | 3 |
| 6 | Corollary G1.B (minimal exactness set) | PROVED (inspection for (iv)) | 3 |
| 7 | Remark 2.2 (active-shift (X3) rows cushionable without FR coordinates in supp tau_m) | SKETCH | 3 |
| 8 | Lemma LE (linear exactification of single-(X3) strict resonances) | PROVED | 4 |
| 9 | Lemma 3.2, Theorem G1.C (Step A^nat at the linear scale; realization criterion) | PROVED (mod chain) | 4 |
| 10 | Lemma 3.3 (bookkeeping: (K2-d), (L-K2-1/2), (W_exp), (LATE), S2c^tr, drift, costs) | PROVED (bookkeeping) | 4 |
| 11 | Lemma 4.2 (split preparation P^nat), Lemma 4.4 (row-aligned moves) | PROVED (mod chain) / PROVED | 5 |
| 12 | Lemma 5.1 (single two-(X3) strict minor exactified linearly) | PROVED | 6 |
| 13 | Prop. 5.2, Cor. 5.3 (strict Farkas alternative with generators, restricted model) | PROVED (mod chain, first order) | 6 |
| 14 | Cor. 5.4 (H2 Example 4.3 / contact-row resonances realized) | PROVED (mod chain) | 6 |
| 15 | Lemma 5.5 (linear descent inside Z^str) and (NT_0) | PROVED (mod H1 2.1-2.2, proof of J1.11, Lemma III-K) | 6 |
| 16 | Theorem G1.D (residual after G1) and its persistence form | PROVED as reduction (mod chain); thick-type part SKETCH | 6 |
| 17 | Systems of multi-(X3) strict minors (R-S2) | OPEN | 6 |
| 18 | (LSC-trunc)_N for every f; density of NA((c_0, p_N), l_2^2) | OPEN | 8 |

## 1. Where exactness on Z_kappa is used
Reading of the chain (J1.13, Lemma III-CMtr item (iii), Lemma II-classes, Prop. II-ray (b)).  At a stage (L, w, a) the coarse
decomposition data X(t) = (Delta'_dec(t), gamma_dec(t)) of g at f (inactive components zeroed) violate the rows of Gamma^#(kappa, a; r)
at the realized ratios by at most K t (Prop. II-ray (a)), and are projected onto that cone.  Everything else downstream uses the
ratios only through statuses and move sizes (J1.13 proof, J1-ref B.5).  Units: |X(t)| <= K_X := C_f Des(L)^C uniformly for t in the
window (coarse omega^+- components bounded through 1/Phi_l <= D(L); |gamma_l| = lambda_l |Delta omega(l) - Delta_m w(k(l))| and
|Delta'| <= C_Delta bounded; coefficients <= A_max <= K, Prop. II-ray (c)).

## 2. The cushioned face-wise Hoffman lemma
Setting.  Rows a_1, ..., a_p in R^n, |a_i|_2 <= 1; [p] = E u I_s u I_c (equality rows, STRICT inequality rows, CUSHIONED inequality
rows); S := E u I_s, I := I_s u I_c.  For x: slacks s_i := a_i x (i in I); violation V(x) := max(max_E |a_i x|, max_I (a_i x)_-).
For a row set R: A_R the |R| x n submatrix, vol(A_R) := det(A_R A_R^T)^{1/2} = (sum_K det(A_{R,K})^2)^{1/2} (Cauchy-Binet; K over
|R|-subsets of the columns).  R is ROBUST (at level u) if some |R| x |R| minor of A_R has modulus >= u (the empty set is robust).
 (F1) If A_R has independent rows, sigma_min(A_R) >= vol(A_R)/||A_R||_2^{|R|-1} >= vol(A_R)/|R|^{(|R|-1)/2}
      (the product of the |R| singular values is vol(A_R), each is <= ||A_R||_2 <= ||A_R||_F <= |R|^{1/2}).
 (F2) If A_R has independent rows and i notin R: dist_2(a_i, rowspace A_R) = vol(A_{R u {i}})/vol(A_R)  (Gram determinant).
Hypotheses for 0 <= mu < u <= 1 and a row set N:
 (MD_N) every square minor of A_N has modulus <= mu or >= u;
 (SE_N) every square minor of A_{N cap S} is 0 or has modulus >= u.

LEMMA CH.  PROVED.  Let x in R^n, V := V(x), Lambda := p^{p/2}/u + 1, N := E u {i in I : s_i < Lambda^p V} (the rows met by the
data at the scale of the violation).  Assume (MD_N), (SE_N).  Put H := p^{p/2} Lambda^p/u and eta := 2^{n/2} mu/u.  There is x' with
 (i) |x' - x|_2 <= H V;
 (ii) a_i x' = 0 (i in E) and a_i x' >= 0 (i in I_s): the strict rows hold EXACTLY;
 (iii) a_i x' >= -eta |x'|_2 for i in I_c, and a_i x' > 0 for i in I \ N;
 (iv) (sign form) for i in I_c cap N, a_i x' = d_i x' with |d_i| <= eta, d_i orthogonal to the span of a robust set B subset N.
Proof.  If V = 0 take x' = x; let V > 0.
Step 1 (slack pigeonhole).  rho_k := Lambda^k V, k = 0, ..., p.  The <= p slacks s_i cannot meet all p + 1 intervals [rho_k,
rho_{k+1}); fix k such that none does, rho := rho_k, N_k := E u {i in I : s_i < rho} (subset of N since rho <= rho_p).  Every
i in I \ N_k has s_i >= Lambda rho.
Step 2 (strict basis).  q := rank A_{S cap N_k}.  If q >= 1 choose B_s subset S cap N_k, |B_s| = q, with a nonzero q x q minor; by
(SE_N) its modulus is >= u, so B_s is robust, and every a_i (i in S cap N_k) lies in rowspace A_{B_s}.  (q = 0: B_s := {}.)
Step 3 (robust extension).  Choose a robust B with B_s subset B subset N_k of maximal cardinality.  vol(A_B) >= u, so A_B has
independent rows and sigma_min(A_B) >= u/p^{(p-1)/2} (F1).  For i in N_k \ B the set B u {i} is not robust (maximality), so each of
its (|B|+1)-minors has modulus < u, hence <= mu by (MD_N); there are <= 2^n of them, so vol(A_{B u {i}}) <= 2^{n/2} mu and, by (F2),
dist(a_i, rowspace A_B) <= eta.  Write a_i = pi_i + d_i, pi_i in rowspace A_B, |d_i| <= eta, d_i orthogonal to rowspace A_B (d_i = 0
for i in B and, by Step 2, for i in S cap N_k).
Step 4 (projection).  x' := x - A_B^T (A_B A_B^T)^{-1} A_B x (projection onto ker A_B).  For i in B, |a_i x| <= rho (equality rows:
<= V; inequality rows of N_k: -V <= s_i < rho), so |x' - x| <= |A_B x|/sigma_min(A_B) <= p^{1/2} rho p^{(p-1)/2}/u <= H V.
Step 5.  A_B x' = 0, so a_i x' = d_i x' for i in N_k: = 0 on S cap N_k (all of E lies in N_k), >= -eta|x'| on I_c cap N_k.  For
i in I \ N_k: a_i x' >= s_i - |x' - x| >= Lambda rho - p^{p/2} rho/u = rho > 0.  QED
Remarks.  (a) H depends only on p and u; eta is linear in the largest tiny minor.  (b) mu = 0 gives a local form of V2 Lemma H.
(c) NECESSITY for strict rows (PROVED): two equality rows with a tiny nonzero minor collapse the face (V2 2.1 two-ray example:
D tau = (0, delta), distance >= 2/delta), so (SE_N) cannot be weakened to (MD_N) on strict rows.  (d) Sharpness for cushioned rows:
with the wrong sign of the defect the data can be at distance ~ |x| from the EXACT cone while x' violates the cushioned row by
exactly |d_i x'| (numerics, Section 7).
COROLLARY CH.1 (parametric form).  PROVED.  Let A(r) have Lip-Lipschitz rows, split as above; X with violation V_0 at r_0.  If at
r^# (MD_N), (SE_N) hold with N computed at r^# for V := V_0 + Lip |r^# - r_0| |X|, there is X^# with strict rows of A(r^#) exact,
cushioned rows >= -eta |X^#|, |X^# - X| <= H (V_0 + Lip |r^# - r_0| |X|).  Proof: the violation at r^# is <= V; Lemma CH.  QED

## 3. Strict and soft rows; the soft transplant
Setting: Part III Section 5 with the K2/J1/J2/H1/H2 conventions ((FC), P-TU, F-2, (D-enum)); main stage L >= l_f, clean
sub-window w, class a; b = b(w), u = u(w), T = T_lo(w), T_hi = T_hi(w); f^r the deep-raised row, f^P the prepared row, f^# the
companion after Step A; n <= 2L active variables; p = number of rows of the enlarged class cone (p <= C Des(L)).

3.1 Rows of Gamma^#(kappa, a; r) (Part II Def. 5.52, Part III Def. III-cone, enlarged by (X1^F)), in the variables (Delta', gamma):
 (X3)_m   Delta'_m - sum_{l in Omega_a(m)} r_l gamma_l = 0 (active shift) or sum r_l gamma_l = 0 (inactive): equality;
 (X1-FR)  L_j(Delta', gamma) := sum_l gamma_l u_l(j) - sum_m Delta'_m tau_m(j) = 0 at target coordinates j that are free with
          robust room: equality;
 (X1-ag)  aggregated signature rows on S_l cap (L, s_far]: one variable each;
 (X1-c), (X1^F)  s_j L_j >= 0 at target coordinates that are contacts, resp. tiny support, of f^r;
 (X4^0), (X4), (X4^U)  inward rows at near-threshold carriers ((X4^U) has one variable).
Every row with >= 2 variables is (X3), (X1-FR), (X1-c)/(X1^F) at a target coordinate, or (X4)-type (signature sets of distinct coarse
carriers are disjoint; targets lie in T(L) subset [1, Dbar(L)]).  After the preparation, every target coordinate j <= Dbar(L) in U_L
carrying an (X1-c)/(X1^F) row is a support coordinate of type S_th of f^P and f^#, |a^#_j| >= theta_min/2 (contacts banked, tiny
rooms closed then banked, tiny support raised), where theta_min is the least preparation mass at target coordinates (theta_0 =
b/Des^{C_P} in the K2 preparation, theta_T in P^nat, Section 5).  Robust target support carries no row.

LEMMA 2.1 (tolerances at the companion).  PROVED (mod chain: Prop. III-cushion, Lemma III-CMtr kind-[3] verification).  Let C_+ be
the cushion constant of Prop. III-cushion and C'_+ := C_+ + 3 (c_flat <= 1/(32 rho C'_+), a design constant).  At f^#, for every scale
t <= T_hi of the class set:
 (a) [S_th rows]  a violation of (X1-c)/(X1^F) at j by delta >= 0 at the projected data point (s_j V_proj(j) >= -delta) keeps the
     side-cushion condition (U3^inf) at j (anti-signed parts of the two pieces <= C'_+ |a^#_j|/t + r(j)) provided delta <= 4|a^#_j|/t;
     in particular every such row tolerates 2 theta_min/t;
 (b) [(X4^0)/(X4) rows]  a violation v >= 0 of the inward row of a near-threshold carrier d (units of lambda_d vs_d Delta omega(d))
     keeps d of kind [3] relative to gap^#(d) provided v <= lambda_d gap^#(d)/t;
 (c) [strict rows]  (X3), (X1-FR) and single-variable rows must hold exactly at the projected point.
Proof.  (a) Banked contact s: Prop. III-cushion (iv) builds the pieces as a contact-like z_s-signed split of V(s) plus a base term
beta_s, |beta_s| <= 4Kt|a^#_s| <= |a^#_s|/t.  If s_j V(s) = -delta < 0 replace the contact-like split by the symmetric one: b^+ gets
-delta s_j/2, b^- gets +delta s_j/2 (b^+ - b^- = V(s) is kept, the theta-piece receives nothing).  Then (s_j b^+)_- <= delta/2 +
|beta_s| <= 3|a^#_s|/t and (s_j b^-)_+ <= delta/2 + |beta_s| <= 3|a^#_s|/t; r(j) is unchanged.  Raised tiny support j: apply the deep
assignment of Prop. III-cushion with A_j := 2|a^#_j|/t in place of 2|a^r_j|/t; the interval [y_j - A_j - t r_j, x_j + A_j] is nonempty
iff s_j V_c(j) >= -2A_j - t r_j, true for delta <= 4|a^#_j|/t; the conclusions (s_j b^+_1)_- <= A_j, (s_j b^-_1)_+ <= A_j + t r_j and
||B_+ 1_F - b^+_1||_1 <= (1 + eta')t/q_0 + Kt + 7C c_{L+1}/t are unchanged (a larger A_j only shortens sigma_j).
(b) Lemma III-CMtr uses the cone point at a (T)-block carrier only through lambda_l vs_l Delta omega^#(l) >= -C_f lambda_l (c_{L+1} +
D^C c_{L+1}^2), compared with -3 lambda_l gap^#(l)/t; a violation v lowers the left side by v (Lemma III-floorrow (a)), and C_f(c_{L+1}
+ D^C c_{L+1}^2) <= 2 gap^#/t since c_{L+1} <= b^2 and gap^# >= b/Des^C.  (KN)-blocks: the same with (X4) in the units of vs Delta
omega ((KN) clause: -|Delta'*| gap^#/M - C_f c_{L+1} >= -3 gap^#/t).
(c) (X3) defines the true shift (U1 Lemma 4.6, II Lemma 5.58); a mismatch enters the peak traces at FR coordinates and the far
aggregated rows of robust peaks of inactive blocks, where only the (VT') tolerance (mass <= delta s_1/(64 rho)) is available; (X1-FR)
violations are violations at free coordinates (tolerance (VT') only).  QED

DEFINITION 3.2 (strict/soft).  S(kappa) := the (X3), (X1-FR) and single-variable rows (STRICT); all other rows are CUSHIONED.  A
minor of the matrix of Gamma^#(kappa, a; r) is STRICT if all its rows are strict, SOFT otherwise.  A strict minor without (X3) row is
a design number (0 or >= delta'_comb(L), Section 4), so a tiny strict minor contains an (X3) row.  An active ratio is STRICTLY PINNED
if some tiny strict minor depends on it, SOFTLY PINNED if pinned in the sense of J1.13 but not strictly pinned, FREE otherwise.
Z^str_kappa := {r in K_kappa : every tiny strict minor vanishes} (contains Z_kappa).

3.3 Soft tolerance.  g'_min(w) := least gap^# of a near-threshold carrier at the companion (>= b/Des^C by (E3) below); Des^{C_r} bounds
the Euclidean norms of all class-cone rows in their natural units (Lemma CH is applied to the normalized rows);
      mu_tol(w) := u min(theta_min, lambda_min(L) g'_min(w)) / (2^{L+2} Des(L)^{C_r} K_X T_hi(w)),   D_tol(w) := mu_tol(w)/(2 Lip),
Lip := Lipschitz constant of the minors in the ratios (<= Des^C).  By Lemma CH with eta = 2^{n/2} mu/u <= 2^L mu/u and |X^#| <= 2K_X:
if every soft tiny minor is <= mu_tol at the realized ratios, the cushioned rows are violated, in their natural units, by <=
min(theta_min, lambda_min g'_min)/(2 T_hi), i.e. within the tolerances of Lemma 2.1 at every t <= T_hi.
LEMMA 2.3.  PROVED.  If g'_min(w) >= b Des(L)^{-C}: with the K2 preparation mu_tol(w) >= b Q(w)/Des(L)^{C_P + C}; with P^nat
mu_tol(w) >= b (Des/u)^{C_T - C}; in both cases mu_tol >= Des^{10} b/u^{10} (C_T >= C + 10), so every soft tiny minor of the prepared
row (modulus <= (1 + 2Lip) b, Lemma III-prep (b)) is within the tolerance with a factor >= Des^5 to spare.
Proof.  T_hi(w) <= 2^{-L^3}/(L Q(w)), Q(w) = (4 Des/u)^{omega(L) + L^2 + 20} (Lemma III-count); K_X, 2^{L+2}, Des^{C_r}, 1/u,
1/lambda_min(L) <= D(L) are <= (Des/u)^C.  With theta_0: u theta_0/(2^{L+2} K_X T_hi) >= u b L Q(w) 2^{L^3}/(Des^{C_P} 2^{L+2} K_X).  With theta_T = b T_hi
(Des/u)^{C_T}: u theta_T/(2^{L+2} K_X T_hi) = u b (Des/u)^{C_T}/(2^{L+2} K_X).  The g'-term: >= u b Des^{-C-1}/(2^{L+2} K_X T_hi) >=
b Q(w)/Des^{C'}.  QED
So F-NE (b >> s_1/T >> delta_Z, H2-ref) concerns the (VT') tolerance, i.e. STRICT objects only.

THEOREM G1.A (soft transplant).  PROVED (mod chain).  Let f^# be a companion built by Step 0, the preparation and a realization of
Step A whose realized ratios r^# satisfy
 (E1) every tiny STRICT minor vanishes at r^#;
 (E2) every tiny soft minor has modulus <= mu_tol(w) at r^#; every robust minor has modulus >= u/2;
 (E3) the statuses required by J1.13 (ii), with g'_min(w) >= b Des^{-C}; and |r^# - r(f)| <= u/(4 Lip).
Then the conclusions of Lemma III-CMtr (c), (d) and Prop. III-cushion hold at f^# with C'_+ in place of C_+ and K_data replaced by
H_CH K_data, H_CH := p^{p/2} Lambda^p/(u/2), Lambda := 2p^{p/2}/u + 1, provided the class thresholds of Lemma III-track satisfy
K_*(w) >= 6(H_CH (C_Gamma J + 1) + 1).  The stage then feeds Theorem E^{eng,RT,inf} exactly as a stage with r^# on Z_kappa.
Proof.  (SE) at r^# for the strict rows: a strict minor without (X3) row is a design number, 0 or >= delta'_comb(L) >= u (window
thresholds lie below the design constants, (D-G1a)); one with an (X3) row is a rate object, robust (>= u/2 by (E2)) or tiny and then
0 by (E1).  (MD) with mu := mu_tol and u/2: every minor is a rate object (the rate scheme contains all minors of all patterns), tiny
soft ones are <= mu_tol by (E2), robust ones >= u/2.  The data of a scale t violate every row at r^# by V <= (1 + C_Gamma J A_{i(t)}) K t
+ Lip |r^# - r(f)| K_X <= 2(1 + C_Gamma J A_{i(t)}) K t (the second term is <= Des^C b K_X << K T_lo, since |r^# - r(f)| <= Des^C b
for the companions of Theorem G1.C).  Lemma CH (whole cone) gives X^# with strict rows exact, cushioned rows violated by <= eta |X^#|
(within Lemma 2.1's tolerances, 3.3), |X^# - X| <= H_CH V.  Lemma III-track (active components move by <= 1/6 of their modulus) holds
with the enlarged K_*(w).  The pieces (Prop. III-cushion, Lemma III-CMtr (c), (d)) use the cone point only through: exact (X3) (true
shift = cone shift), exact (X1-FR) (V_proj = 0 at free coordinates), the sign of the projected switching at contacts and tiny-support
target coordinates (replaced by Lemma 2.1 (a)), the inward rows (Lemma 2.1 (b)) and the bound on |X^# - X| (multiplied by H_CH).  The
window count (Lemma III-count) absorbs H_CH: log H_CH <= C p^2 log(p/u) while Q(w) contains (Des/u)^{omega(L)}, omega(L) >= 2^p.  QED

COROLLARY G1.B (minimal exactness set).  PROVED ((iv) by inspection of Lemma III-nocube).  Downstream of Step A it suffices that
(i) strictly pinned ratios lie EXACTLY on Z^str_kappa; (ii) softly pinned ratios satisfy (E2), e.g. lie within D_tol(w) of their values at
f^P; (iii) free ratios and inactive values satisfy the status requirements of J1.13; (iv) cofactor polynomials need not be exact (route V
uses no cube normalization, Lemma III-nocube, so A_max and the g_J-minors are not used).  [J1.13 required (i) for every pinned ratio
and every cofactor polynomial.]
Remark 2.2 (SKETCH).  (X3)_m of a block with an ACTIVE shift can also be cushioned when no FR coordinate lies in supp tau_m (the
mismatch then enters only cushioned rows; the far aggregated peak rows keep their sign by |Delta'_m| >= A K t): J1's mismatch tolerance
(Prop. J1.12, (MT1)).  Not used.
Remark 2.4 (necessity).  Exactness of strict tiny minors cannot be dropped (Remark CH (c)); for soft minors mu_tol is the right scale
(the cushioned violation is exactly d_i x', Lemma CH (iv), proportional to the minor).

## 4. Linear exactification and Step A at the linear scale
Design numbers of level L: values of polynomials of degree <= 16 L^4 in the non-weight design data of level L (target values u_l(j),
tau_m(j), coefficients alpha_l, signs, combinatorial data; all of modulus <= 1) with integer coefficients of absolute sum <= 2^{L^4},
and ratios of two such; delta'_comb(L) > 0 := least nonzero modulus of such a polynomial.  (D-G1a): Des(L) >= 4^{L^4}/delta'_comb(L),
Des(L) >= p(L)^{p(L)^2} (p(L) := maximal number of rows of an enlarged class cone of level L), and the robust thresholds u(w) of
level-L windows are <= delta'_comb(L).  All are level-L, N-free and f-free quantities; insertion is monotone (U4 Lemma GW).  Every
design polynomial has modulus <= 2^{L^4} <= Des^{1/2}; every nonzero one >= 1/Des.  Minors of size <= 2L of matrices whose entries
are minors of size <= 2L of design rows are again design polynomials (degree <= 4L^2, coefficient sum <= ((2L)!)^{2L+1} <= 2^{L^4}).

LEMMA LE (linear exactification).  PROVED.  Let every tiny strict minor of kappa contain exactly one (X3) row; for a block m let M_m
be the set of tiny strict minors containing (X3)_m.  Then
 (a) every M in M_m is affine in the block-m ratio vector alone: M(r) = <C_M, r^(m)> + c_M, C_M, c_M design numbers (c_M = 0 if the
     shift of m is inactive);
 (b) if |M(r_1)| <= beta for all M in M_m and beta Des(L)^2 < 1, then A_m := {rho : <C_M, rho> + c_M = 0 (M in M_m)} is nonempty and
     dist_2(r_1^(m), A_m) <= Des(L)^2 beta;
 (c) moving r^(m) inside A_m changes no tiny strict minor of another block.
Proof.  (a) Expand along the unique (X3) row: its entries are 1 (column Delta'_m, if active and selected) and -r_l (columns gamma_l);
the cofactors are minors of strict rows without (X3) row (FR rows with entries u_l(j), tau_m(j); single-variable rows; no other (X3)
row by hypothesis), i.e. design numbers.  (b) Write the system as C rho = -c (rows C_M; at most 2L columns).  If it were inconsistent
there would be lambda with C^T lambda = 0, c^T lambda = 1; take a basic solution (support <= 2L + 1): by Cramer its entries are
ratios of minors of [C^T; c^T], i.e. design numbers <= Des^{1/2}/delta'_comb, so ||lambda||_1 <= (2L + 1) Des^{3/2} <= Des^2.  Then
1 = lambda^T c = lambda^T (C r_1 + c) <= ||lambda||_1 beta < 1 (C^T lambda = 0), a contradiction.  So A_m is a nonempty affine set.
Let q := rank C, B a set of q independent rows and K a set of q columns with det C_{B,K} != 0 (so >= 1/Des).  Put e := C r_1 + c
(|e|_inf <= beta) and delta_K := -C_{B,K}^{-1} e_B, delta := 0 off K.  By Cramer every entry of C_{B,K}^{-1} is a cofactor (<= Des^{1/2})
over the determinant, so |delta|_2 <= q^{3/2} Des^{3/2} beta <= Des^2 beta.  rho := r_1 + delta satisfies the rows B; the other rows are
combinations of the rows B, and since the system is consistent the same combinations hold for c, so rho in A_m.  (c) is (a).  QED
Remark.  A minor with >= 2 (X3) rows is multi-affine (degree one per block); Section 6 (Lemma 5.1) treats one such minor; systems
are the class (R-S2).

DEFINITION 3.1 (Step A^nat).  At a stage (L, w, a) with pattern kappa let f_1 be the row after the deep raise, Step 0 and P^nat
(Section 5).  The Step-A^nat system is the Step-A system of Def. III-SysA with targets:
 (T1) strictly pinned active ratios: a point of A_m (Lemma LE; beta := (1 + 2Lip) b) compatible with the one-sided constraints of the
      strictly pinned kind-(iv) rows (with the block rescaling in (U)-blocks), when one exists -- otherwise the block is (R-S1)-residual
      (Prop. 5.2); since r_1 satisfies the one-sided constraints and violates the design equalities by <= beta, the Cramer form of
      Hoffman's bound (inverses of nonsingular square submatrices of a design matrix have entries <= Des^{3/2}) gives such a point
      within Des^4 beta of r_1;
 (T2) softly pinned and free active ratios: their ratios at f_1, with bands (overshoot bands for kind (iv), symmetric for two-sided
      rows) of half-width beta_band <= min(beta_*, kappa_min D_tol(w));
 (T3) near-threshold active carriers of (T)-blocks: if not strictly pinned, |r_d| lowered by h_d := Des^{C_x} b; if strictly pinned,
      a point of (prod_m A_m) cap {F_Phi <= 1 - 3mu/4} within Des^C b of r_1 (Lemma 5.5, under (NT_0));
 (T4) KN-1 holds: value 0 (displacement <= C b), or bands (H1 Cor. 2.4);
 (T5) inactive near-threshold carriers of (U)/(KN)-blocks pushed to relative position <= 1 - Des^{C_x} b; (KN)-lever push Des^{C_x} b;
      (U)-block rescaling s_m := 1 - 4 Des^{C_x} b by the kappa-lever.
Scale x^nat := Des(L)^{C_x + 4} b; W^nat := Des^{C_A} u^{-3} max(x^nat, ||b||); rho_0^nat := C_2 (W^nat)^2 (Def. III-Areg with x -> x^nat).
LEMMA 3.2.  PROVED (mod chain).  At f_1 + P (P the TU pre-placements) |Ft|_inf <= x^nat; hence ||b|| <= |Lambda_A|^{1/2} x^nat,
W^nat <= Des^C b/u^3 << D_tol(w), and every Step-A^nat move is <= W^nat.
Proof.  Ft_l(R_1) = kappa_m (rc_l - rt_l) (J1.2): 0 for (T2); <= kappa_m Des^4 beta for (T1); <= kappa_m Des^C b for (T3)-(T5)
(kappa_m, Phi bounded below by 1/C_f, 1/D(L)); the TU pre-placements leave a second-order residue <= C Des^C (W')^2 (P-TU, compensating
base banks).  W^nat << D_tol by Lemma 2.3.  QED

THEOREM G1.C (realization at the linear scale).  PROVED (mod chain: Lemma III-cone (c), J1.8, H2 Lemmas 3.2/3.3, J1-ref F-2, J2 (FC),
Theorem G1.A, Lemma 5.5).  Let (L, w, a) be a stage at which every tiny strict minor contains exactly one (X3) row ((NT_0) is then
automatic, Section 6).  If the band-relaxed Step-A^nat system is A-regular (H2 Lemma 3.2:
B(b, rho_0^nat) subset (W^nat/2) conv(G u {0}) - Box), there is a companion f^# satisfying (E1)-(E3), of cost <= C_f Des^C W^nat
log(1/W^nat) = o(u^2 T^2).  If this happens at infinitely many main stages, (LSC-trunc)_N holds at (f, g, rho) (J2.1's (FC) and
Theorem E^{eng,RT,inf} as in J1.15').
Proof.  Brouwer realization as in Lemma III-cone (c) / J1.8 (a) with the frozen (FC) block scalars.  (E1): strictly pinned ratios are
targets of equality rows, realized exactly on A_m, so every tiny strict minor vanishes (Lemma LE (a)).  (E2): for a soft tiny minor
|M(r^#)| <= |M(r_1)| + Lip |r^# - r_1| <= (1 + 2Lip) b + Lip (W^nat + beta_band)/kappa_min <= mu_tol (Lemmas 2.3, 3.2); robust minors
move by << u; the (U)-block rescaling multiplies every minor of the block by s_m^e, e <= n (Lemma III-Uscale), preserving vanishing and
smallness.  (E3): (T)-blocks -- the realized near-threshold statuses are <= 1 - 3mu/4, mu := c Des^{C_x - 1} b (Lemma III-K is
monotone in |r_d| and R^2), and later drifts are <= C_f Des c_{L+1} <= C_f Des b^2 << mu (Lemma III-drift); (U)/(KN)-blocks: margins
Des^{C_x} b M as in Prop. III-KNtr (b) with eta' -> Des^{C_x} b; robust statuses move by <= Des^C W^nat << u.  Theorem G1.A applies.  QED

LEMMA 3.3 (bookkeeping).  PROVED.
 (a) (K2-d): the mass b/Des^{C_P}-type cushions are needed only at TARGET coordinates (Section 3); private coordinates use theta_pr :=
     max(8 rho A_0 s_1/T, 4 Des K_DC r); (L-K2-1) s_1 <= theta T/(8 rho A_0) and (L-K2-2) Des K_DC r <= theta/4 hold for theta in
     {theta_T, theta_pr} (s_1 := max(64 rho eps/delta, exp(-1/(2T))), K2 6.4; theta_T >= b T >> theta_pr since b >= exp(-C log^3(1/T)));
 (b) (W_exp) c_{L+1} <= exp(-1/T_lo) unchanged; eps <= C_f Des c_{L+1} << s_1 (fine carriers through their weight only, K1.S);
 (c) (LATE): s_late = c_late (T gap_min x_0/(n A_0 K_w))^7 with gap_min >= b/Des^C ((T3)-(T5)), x_0 = c_f g_min Phi_min >= b/Des^C,
     K_w <= exp(C log^3(1/T)) (K2 6.4, 1/gap_min <= Des^C/b); hence s_late >= exp(-C' log^3(1/T)) >> exp(-1/(2T)) = s_1 for T small;
 (d) Lemma S2c^tr: no Puiseux exponent enters at stages covered by Theorem G1.C; where the old Puiseux step is kept its cost
     exp(O(log^2(1/T))) is absorbed by (W_exp) as before;
 (e) Lemma III-drift: later moves change statuses by <= C_f Des c_{L+1} <= C_f Des b^2 << mu;
 (f) costs: preparation <= C D(L) theta_T log(1/theta_T) + C_f Dbar(L) b log(1/b), Step A^nat <= C_f Des^C u^{-3} b log(1/b); both
     o(u^2 T^2) since b <= T^4.
Proof.  Substitution in the cited inequalities; the changed inputs are gap_min, x_0 (now >= b/Des^C instead of >= eta'/Des^C) and the
Step-A scale; K2 6.4's estimates are monotone in them.  QED
Remark 3.4 (the scale must be linear).  At the old scale x = C Des eta' (Lojasiewicz/Puiseux displacements ~ eta'), soft minors could
move by Lip eta' >> mu_tol whenever b << eta' T_hi (as soon as a Lojasiewicz exponent exceeds 1: b <= (eta'/C_L)^{N_L/2}).

## 5. The split preparation P^nat
DEFINITION 4.1.  theta_T := b T_hi(w) (Des(L)/u(w))^{C_T} (target coordinates T(L) cap U_L, design depth); theta_pr := max(8 rho A_0
s_1/T, 4 Des(L) K_DC r) (private coordinates S_l cap [1, Dbar(L)], l coarse); C_T absolute.  (P1) unchanged (close every free
s <= Dbar(L), s in U_L, with room 1 - |z_s| <= b).  (P2^nat): bank theta_T z_s at every contact s in T(L) cap U_L, s <= Dbar(L), and
theta_pr z_s at every private contact.  (P3^nat): raise (same sign) every support s in T(L) cap U_L with |a_s| < theta_T to theta_T,
every private thin support with |a_s| < theta_pr to theta_pr.
LEMMA 4.2.  PROVED (mod chain: Lemma III-prep, K2 4.1, 6.3-6.5).
 (a) cost <= C D(L) theta_T log(1/theta_T) + C_f Dbar(L) b log(1/b) = o(u^2 T^2);
 (b) every value moves by <= b + C Dbar(L)(theta_T + theta_pr) <= 2b; the clean classification survives with factor 2;
 (c) types (Lemma III-prep (d)) unchanged with S_th meaning |a_s| >= theta_T/2 at target and >= theta_pr/2 at private coordinates;
     (U3^inf) at banked/raised coordinates as before (contact-like data plus a base term proportional to the mass, Prop. III-cushion
     (iv)); (L-K2-1), (L-K2-2) hold at every banked coordinate;
 (d) mu_tol(w) >= b (Des/u)^{C_T - C} (Lemma 2.3; only target S_th rows are cushioned rows with >= 2 variables);
 (e) banks and raises change every strict minor by <= Lip C Dbar(L)(theta_T + theta_pr) <= b_bias := b T_hi(w) (Des/u)^{C_T + C}, a
     negligible multiple of b (T_hi(w) <= 2^{-L^3}/(L Q(w)), Q(w) >= (Des/u)^{omega(L)}); the rest of the preparation's change of
     strict objects comes from the (P1) closings (<= Lip b, a datum of f at the window);
 (f) H2 Lemma 5.2's bias of kind-(iv) values from private banks is <= eff v theta_pr <= exp(-c/T).
Proof.  (a)-(c) as Lemma III-prep with two masses (cost terms are monotone in the mass; (L-K2-1), (L-K2-2) are lower bounds on the
masses).  A private coordinate needs the mass for: the S_th type for Theorem K2.6's two-sided Sys-DC lever at scale r ((L-K2-2)),
survival of the bank under the theta piece of Theorem UE^inf ((L-K2-1)), one-sided Step-A raises (efficiency mu_s^2/nu, mass-free),
cushion domination (any positive mass): none needs theta ~ b.  At target coordinates the mass also gives the cushions of Lemma 2.1,
which fixes theta_T through mu_tol.  (d): substitute theta_T in Lemma 2.3.  (e): a bank of mass theta at s changes u(xhat) by
(mu_s^2/nu) u(s) z_s theta (Lemma III-actions (ii), J1.1), so values move by <= theta |u(s)|; ratios move by <= C_f (value moves);
strict minors are Lip-Lipschitz in the ratios.  (f) idem.  QED
Remark 4.3.  (P1) closings are kept: a free coordinate with tiny room would carry an (X1-FR) equality with (VT') tolerance only, so it
must become a (banked, cushioned) contact.  Banks are one-sided; P^nat makes their effect on strict objects negligible, it cannot make
it two-sided.

LEMMA 4.4 (row-aligned moves).  PROVED.  Let a move change the values of the coarse carriers by c u_k(j) (k coarse; c scalar), e.g. a
bank of mass theta at the contact j (c = (mu_j^2/nu) z_j theta) or a z-move at a free j (c = dz).  Let M be a minor containing (X1)_j
and exactly one (X3) row, (X3)_m, of a block with inactive shift, with columns among the gamma-columns of block m and columns on which
(X1)_j vanishes.  Then the first-order change of M under the move is zero.
Proof.  r^(m) changes by (c u^(m)(j) - r^(m) dkappa)/kappa_m.  The term -r^(m) dkappa/kappa_m multiplies (X3)_m by (1 - dkappa/kappa_m)
(Lemma III-Uscale), changing M by a factor.  The term c u^(m)(j)/kappa_m adds to (X3)_m a multiple of the restriction of (X1)_j to the
gamma-columns of block m, which on the columns of M is (X1)_j itself; a determinant with two proportional rows is 0.  QED
So moves at j neither help nor harm resonances that contain the row of j (H2-ref P-41 (ii); G3 Cor. 2.4's cancellation).

## 6. What is realized and what remains

LEMMA 5.1 (a single two-(X3) strict minor is exactified linearly).  PROVED.  Let M be a tiny strict minor containing exactly two (X3)
rows, of blocks m, m'; x := r^(m), y := r^(m') (dimensions p', q').  Then M(x, y) = x^T D y + E^T x + F^T y + G with design numbers
D, E, F, G, and at the start ratios (x_1, y_1):
 (i) if a first cofactor dM/dx_l or dM/dy_k is robust (>= u) at (x_1, y_1), moving that single ratio by -M(x_1, y_1)/(cofactor)
     (<= b/u) makes M vanish exactly;
 (ii) otherwise the projections x^#, y^# of x_1, y_1 onto A_x := {D^T x + F = 0}, A_y := {D y + E = 0} satisfy M(x^#, y^#) = 0 and
     |x^# - x_1| + |y^# - y_1| <= 2 Des^2 b.
Proof.  Multilinearity of the determinant in the rows (X3)_m, (X3)_{m'} (entries 1 or -r_l) gives the form, with coefficients minors of
strict design rows.  A first cofactor is, up to sign, the minor obtained by deleting (X3)_m and the column gamma_l (resp. (X3)_{m'} and
gamma_k): a minor with one (X3) row, hence a rate object, tiny or robust.  (i): M is affine in each single ratio.  (ii): all first
cofactors are tiny, i.e. the design systems D y + E = 0, D^T x + F = 0 have residuals <= b at y_1, x_1; Lemma LE (b) gives consistency
and the distance bounds.  On A_x x A_y: x^T D y = -E^T x (from D y = -E) and x^T D y = -F^T y (from D^T x = -F), so M = F^T y + G =
E^T x + G; the first does not depend on x, the second not on y, so M is constant on A_x x A_y, equal to its value at the Cramer basic
points: a design number, 0 or >= 1/Des.  Since |M(x^#, y^#) - M(x_1, y_1)| <= Lip 2Des^2 b and |M(x_1, y_1)| <= b, it is 0.  QED
[me2_check.py: 500 instances, max |M(x^#, y^#)| = 1.4e-14, displacement <= 1.26 b; if the constant on A_x x A_y is instead a tiny
non-design number g' = b, the zero set is at distance >= 316 b (square-root scale): the design-number dichotomy makes it linear.]
For SYSTEMS of multi-(X3) strict minors, case-(i) moves can conflict and the Jacobian minors of one block are polynomials in the
ratios of the others that are not in the rate scheme; closing the rate scheme under them (a finite operation per level) could allow a
block-by-block induction.  OPEN: class (R-S2).

PROPOSITION 5.2 (strict Farkas alternative with generators; restricted model).  PROVED (mod chain; first order at the start row).
Let the blocks carrying tiny strict minors be (U)-blocks (inactive shifts); M_{m,i}(r) = <C_{m,i}, r^(m)> (Lemma LE, c = 0); oriented
cofactors C'_{m,i,l} := eps_l C_{m,i,l}.  For a two-sided generator g (FR generator: z-move at a design-depth free coordinate s with
robust room, action u(s) dz, J1.1 / K2.16(2a); TS generators: the same with u^(m)(s) replaced by the deviation vector Dev^(m)(s) of
J1.1) put D_{m,i}(g) := <C_{m,i}, u^(m)(s)> (for FR: a design number, 0 if s is a row of M_{m,i}, Lemma 4.4); for a one-sided bank
or raise h at s put D_{m,i}(h) := <C_{m,i}, z_s Dev^(m)(s)> (= z_s <C_{m,i}, u^(m)(s)> at a contact).  In the
restricted model (non-strictly-pinned rows banded, the bands absorbing the generators' side effects) the strict exactification is
infeasible iff there are lambda_{m,i} with
 (a) (sum_i lambda_{m,i} C'_{m,i})_l >= 0 on strictly pinned kind-(iv) rows l of m and = 0 on strictly pinned two-sided rows;
 (b) sum_{m,i} lambda_{m,i} D_{m,i}(g) = 0 for every two-sided generator g, and sum_{m,i} lambda_{m,i} D_{m,i}(h) >= 0 for every one-sided
     raise h;
 (c) sum_{m,i} lambda_{m,i} M_{m,i}(rc) > 0 (wrong sign at the prepared start row).
Proof.  Linearized feasibility: r^# = rc + sum_P a_l e_l + sum_Q b_l e_l + sum_g c_g dr(g) + sum_h e_h dr(h), a, e >= 0 (oriented
kind-(iv) raises, one-sided raises), b, c free, subject to <C_{m,i}, r^#(m)> = 0.  The action dr(g) of a generator on r^(m) is
u^(m)(s)/kappa_m times its size plus a multiple of r^(m); the latter multiplies M_{m,i} by a factor (homogeneity, c = 0).  Farkas' lemma
for this polyhedral system gives (a)-(c) (the block rescaling rho of H2 4.1 is absorbed by homogeneity).  A linear solution is turned into
a realization by the Cramer form of Hoffman's bound (within Des^4 b of the start) and Brouwer as in Theorem G1.C.  QED
COROLLARY 5.3.  PROVED.  (i) Moves at the FR rows of a strict resonance never fix it (D = 0 there).  (ii) A single tiny strict minor M
with FR rows R is not residual as soon as one design-depth FR coordinate s notin R (or a TS generator) has D_M(s) != 0.  (iii) For the
Example-4.3 shape with a FREE common target coordinate j (M = det[[r_+, r_-], [u_+(j), u_-(j)]]): residual only if every other
design-depth FR coordinate shared by l_+, l_- has (u_+(s), u_-(s)) parallel to (u_+(j), u_-(j)) and every one-sided raise acts with
the wrong sign.  [me2_check.py: 972 random wrong-signed instances of (iii), all destroyed by one non-parallel extra FR generator.]

COROLLARY 5.4 (contact-row resonances are realized).  PROVED (mod chain).  The configuration of H2 Example 4.3 -- two kind-(iv) rows
l_+ in K^+, l_- in K^- of a (U)-block sharing a coarse target CONTACT j, tiny minor M = det[[r_+, r_-], [u_+(j), u_-(j)]] with one-signed
oriented cofactors and M(rc) > 0, M the only tiny minor involving l_+-, i.e. the configuration (C3) on which the persistent-(R1)
candidates rest -- does NOT obstruct: j lies in
T(L) cap U_L at design depth (U_L = union of supp u_k, Part III), so P^nat banks it, the row (X1-c)_j is cushioned, M is soft with
|M(rc)| <= (1 + 2Lip) b << mu_tol (Lemma 4.2 (d)); l_+- are free or softly pinned, banded as free rows (Theorem H2.A's bands at the
linear scale, ratio moves <= Des^C b/u << D_tol), and the block is not residual.  The same holds for every resonance all of whose tiny
minors contain a cushioned row ((X1-c), (X1^F), (X4^0), (X4) rows).
Proof.  Theorem G1.A ((E2): |M| moves by <= Lip Des^C b/u), Cor. G1.B (ii), and Theorem H2.A with P^+-_m := strictly pinned (or
locked) rows: its proof only uses that the other rows are banded.  QED

LEMMA 5.5 (linear descent inside Z^str).  PROVED (mod H1 Lemmas 2.1-2.2, the proof of J1.11, and Lemma III-K for (NT_0)).
Let every tiny strict minor of kappa contain one (X3) row; Z^str := (prod_m A_m) cap K_kappa (compact, semialgebraic, defined over k);
F := F_{Phi^T}.  There are eps_0, m_0, V > 0 depending only on (kappa, Phi^T) (inserted into Des(L), P-CHOICE) such that for every
y in Z^str with F(y) <= 1 + eps_0 and every mu' in (0, m_0]: either F(y) <= 1 - m_0, or there is y'' in Z^str with |y'' - y| <= 2V(F(y) -
1 + mu') and F(y'') <= 1 - mu'.
Proof.  J1.11 (a), (b) hold for Z^str by the same proof (compactness, semialgebraicity, definability over k, genericity of Phi^T over k;
B^lin(Z^str) is k-semialgebraic of dimension < n).  Cover Lambda := Z^str cap {F = 1} by finitely many balls B(r_*^i, delta_i) of the local
step (Lemma 2.1 gives v_i), U their union, V := max |v_i|, m_U with F <= 1 - m_U on (Z^str cap {F <= 1}) \ U.  There is eps_0 > 0 with
F <= 1 - m_U/2 on (Z^str cap {F <= 1 + eps_0}) \ U (otherwise y_n notin U, F(y_n) in (1 - m_U/2, 1 + 1/n] accumulate at a point of
Lambda \ U = {}).  For y in U the local step gives a curve in Z^str with F(gamma(t)) <= max(F(y) - 3t/4, 1 - 2m_*^i), |gamma(t) - y| <= V t;
take t := (4/3)(F(y) - 1 + mu'), admissible for eps_0, m_0 <= (3/16) min_i delta_i/V; m_0 := min(m_U/2, min_i m_*^i).  QED
(NT_0) holds: by Part III's definition a coarse carrier is near-threshold iff |rho_l(f) - 1| <= b (cleanness: statuses lie in
[0, b] u [u, 1-u] u [1-b, 1+b] u [1+u, inf)); the preparation moves values by <= 2b, so at the start ratios the relative positions
psi_d/Phi_d (Lemma III-K) are <= 1 + Des^C b, and at the projection rho_1 of r_1 onto prod A_m (distance <= Des^2 beta) F(rho_1) <= 1 +
Des^C b <= 1 + eps_0.  Lemma 5.5 with mu' = 3mu/4 (mu = c Des^{C_x - 1} b) gives a (T3) target at distance <= 2V Des^{C'} b: no Puiseux
step.  (For a near-threshold carrier that is not strictly pinned, lowering |r_d| by h_d = Des^{C_x} b lowers its status by >=
h_d/Des^C, Lemma III-K, from <= 1 + Des^C b to <= 1 - 3mu/4.)

THEOREM G1.D (the residual after G1).  PROVED as a reduction at stages without thick-type carrier (mod chain; H2 Lemma 3.4(c) where
used); at thick-type stages the reduction to (R0^str) is SKETCH (transfer of H1's lever lemmas to x^nat and strict pinning).  For
T_fin^{K2} with (FC), P-TU, F-2, (D-enum), (D-G1a), P^nat and Step A^nat, (LSC-trunc)_N holds at (f, g, rho) unless at all but finitely
many main stages the selected stage has one of:
 (R-S1) a one-signed STRICT linear resonance: a block residual in the sense of Theorem H2.A with P^-_m := strictly pinned K^- rows,
        P^+_m := strictly pinned or locked K^+ rows; in (U)-blocks the alternative of Prop. 5.2 (tiny strict minors made of one (X3) row
        and FR rows of free target coordinates with robust room; annihilated by every two-sided generator; wrong-signed at the start);
 (R-S2) tiny strict minors with >= 2 (X3) rows admitting no exact point within Des^C b that is compatible with the one-sided
        constraints (the geometry of one such minor is linear, Lemma 5.1; systems and one-sided compatibility are open);
 (R-S3) a near-threshold carrier of a (T)-block whose LINEAR descent (direct lowering (T3), or Lemma 5.5 when strictly pinned) is
        blocked by one-sidedness -- H2 5.3's inward-locked K^+ carrier without kappa-raising lever, or a strictly pinned carrier all of
        whose descent directions inside Z^str lower a K^+ kind-(iv) row;
 (R-L)  a locked K^+ row (H2 Lemma 3.4(c), SKETCH there);
 (R0^str) H1's thick-type residual conditions (H-2)-(H-5'), (H-7) with "pinned" read as "strictly pinned" and the Step-A scale x^nat
        [that H1's lever lemmas transfer to the linear scale is SKETCH: they are first-order statements]; (H-6') is reduced to (R-S2)
        and the thick peaks of shifted blocks.
Proof.  At a stage with none of these, Lemma LE (and Lemma 5.1 for a single two-(X3) minor) gives the (T1) targets, Lemma 5.5 the (T3)
targets of strictly pinned near-threshold carriers, and the band-relaxed Step-A^nat system is A-regular: by Theorem H2.A (its proof with
"pinned" replaced by "strictly pinned": softly pinned rows are banded like free rows, band half-width beta_1 <= Des^C b/u << kappa_min
D_tol) in the (R1) case, and by H1 in the thick-type case.  Theorem G1.C gives the companion; if this happens at infinitely many main
stages, (LSC-trunc)_N holds.  QED

REALIZED by G1 (residual or unproved before G1):
 - all resonances whose tiny minors contain a cushioned row: H2 Example 4.3 / G3 (C3) contact-row resonances (Cor. 5.4), tiny-support
   target rows, (X4^0)/(X4) rows; H1's (H-6') nonlinear pinned groups coming from R_a^2 entries; exactness of cofactor polynomials;
 - F-NE for soft objects (tolerance mu_tol >= Des^{10} b instead of (VT'));
 - the preparation-bias source of H2 Theorem H2.B: REDUCED from a fixed fraction of b (>= c theta_0/Des^C) to b_bias = b T_hi (Des/u)^C
   (Lemma 4.2 (e)); banks never move the resonances whose rows they cushion (Lemma 4.4); the remaining start-row changes are the (P1)
   closings (a datum of f at the window);
 - non-linear Lojasiewicz/Puiseux displacements wherever the strict structure is single-(X3) (Lemma LE, Lemma 5.5 under (NT_0)) or a
   single two-(X3) minor (Lemma 5.1); Step A runs at x^nat = Des^C b with all bookkeeping re-checked (Lemma 3.3).
NOT realized: (R-S1), (R-S2), (R-S3), (R-L), (R0^str).  Exactness of strict minors cannot be dropped (Remark CH (c)); their tolerance is
(VT') and F-NE persists for them: making FR rows soft would need s_1 >~ b 2^L K_X/(u delta), i.e. bank masses >~ b/T by (L-K2-1),
whose bias (>> b) destroys the clean classification.

PERSISTENCE (strict form of H2 Theorem H2.B; PROVED as a necessary condition, mod chain).  If (LSC-trunc)_N fails at (f, g, rho), one of
(R-S1)-(R-S3), (R-L), (R0^str) occurs at all large main stages.  An (R-S1) block needs a tiny NONZERO strict minor -- a near-linear
relation <C, r^(m)> ~ 0 among f's block ratios whose coefficients are minors of design target values at FREE target coordinates with
robust room -- of the wrong sign at the prepared row, annihilated by every other two-sided generator acting on its carriers (Cor. 5.3)
and opposed by every one-sided raise; by H2 Lemmas 2.6/2.7 its kind-(iv) carriers are fresh at consecutive (R1) stages.  OPEN whether
such f exist; no counterexample is claimed.

## 7. Numerics (sanity only; r14/G1_work/)
 ch_lemma_check.py/.out: random R^4 instances (strict rows: 2 equalities, 1 inequality; cushioned rows: one with a tiny minor mu of
   random sign, one generic) satisfying (MD), (SE): Lemma CH's construction gives strict rows exact and cushioned rows >= -eta|x'| in
   200/200; |x' - x|/V median 2.2.
 ch_debug2.py/.out: exact face distance (well-scaled parametrization): right-signed defects: dist(x, EXACT cone) <= 1.0e-8; wrong-signed
   defects: dist(x, EXACT cone) >= 0.0146 (|x| = 1) while the Lemma-CH point moves by <= 5.9e-14 and min c_1 x' = -7.9e-9 >= -eta|x'|
   (eta = 4 mu/u, mu <= 8.4e-9): exact projection would be catastrophic, the cushioned one is harmless.
 me2_check.py/.out: Lemma 5.1 (500 instances, exact zero at the projection, displacement <= 1.26 b; non-design contrast >= 316 b);
   Cor. 5.3 (972/972 strict wrong-signed Example-4.3-type instances with a free common coordinate destroyed by one extra generic FR
   generator).
Finite models cannot show the infinite-dimensional mechanisms (deep raise, sweep, memory); those rest on the proofs.

## 8. Main obstacle; next steps
MAIN OBSTACLE.  One-signed STRICT resonances: a tiny nonzero minor made of an (X3) row and (X1-FR) equality rows at free target
coordinates with robust room (or several (X3) rows), whose exactification is forced (two-ray example) while its strictly pinned
kind-(iv) carriers are one-sided, every two-sided generator annihilates it to first order (its own FR coordinates always do, Lemma 4.4)
and f sits on the wrong side.  Soft resonances (contact rows, tiny support, inward rows) are no longer obstructions.
NEXT STEPS.
 (1) Prove (or refute) that at an (R1) stage every strict resonance has a two-sided generator acting on it: Cor. 5.3 reduces this to a
     design-genericity statement on target values at FREE target coordinates (e.g. all 2 x 2 and higher minors of (y_l(s)) over shared
     targets nonzero) plus the existence of a second free shared target of the resonant carriers; check against K2.16's normal form
     whether a kind-(iv) pair can have exactly one free shared target and all other shared targets contacts/thin support.
 (2) Close the rate scheme under Jacobian minors and prove a block-by-block linear exactification for systems of multi-(X3) minors
     (R-S2), extending Lemma 5.1.
 (3) Write the one-sided-blocking analysis of the linear descent (R-S3) as an LP over the descent directions of Z^str (the local
     flow of Lemma 5.5 gives a whole cone of admissible directions v_i; the blocking condition is a Farkas alternative on it).
 (4) Re-run H1's (R0) lever analysis at x^nat with strict pinning, and finish H2 Lemma 3.4(c) (locked K^+ rows).
 (5) Test the strict residual on G3's candidate rows: their resonances must use FREE shared targets (contact versions are realized,
     Cor. 5.4).

