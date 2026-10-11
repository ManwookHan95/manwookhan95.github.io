# G1 part 5: what is realized, what remains (residual classification after G1)
[Working file.  Where it differs, r14/G1_notes.md is final: there (NT_0) is PROVED from Part III's definition of near-threshold
(|rho_l(f) - 1| <= b), Lemma LE/5.1 constants are Des^2, Prop. 5.2 is stated for the restricted model jointly over (U)-blocks, and the
preparation bias is "reduced to b_bias", not removed.]

Conventions of parts 2-4.  "Mod chain" = modulo the links cited by J1.15', J2.1, H2.A and Theorem G1.A.

## 5.1 Two-block strict minors: a single bilinear minor is exactified linearly
LEMMA 5.1 (ME2).  PROVED.  Let M be a tiny strict minor containing exactly two (X3) rows, of blocks m and m', and let x := r^(m),
y := r^(m').  Then M(x, y) = x^T D y + E^T x + F^T y + G with design numbers D, E, F, G, and at the start ratios (x_1, y_1):
 (i) if some first cofactor dM/dx_l (x_1, y_1) or dM/dy_k (x_1, y_1) is robust (>= u), moving that single ratio by
     -M(x_1, y_1)/(cofactor) (<= b/u) makes M vanish exactly;
 (ii) otherwise all first cofactors are tiny, and the projections x^#, y^# of x_1, y_1 onto A_x := {D^T x + F = 0},
     A_y := {D y + E = 0} satisfy M(x^#, y^#) = 0 and |x^# - x_1| + |y^# - y_1| <= 2 Des(L)^3 (p + q)^{1/2} b.
Proof.  Multi-linearity of the determinant in the rows (X3)_m, (X3)_{m'} (entries 1 or -r_l) gives the form; the coefficients are
minors of strict design rows.  The first cofactors are, up to sign, minors with ONE (X3) row (delete (X3)_m and the column gamma_l),
hence rate objects: tiny or robust.  (i): M is affine in each single ratio.  (ii): the systems D y + E = 0 and D^T x + F = 0 have
design coefficients and residuals <= b at y_1, x_1; Lemma LE (b) gives consistency and the distance bounds.  For x in A_x, y in A_y:
x^T D y = -E^T x (use D y = -E) and x^T D y = -F^T y (use D^T x = -F), so M = F^T y + G = E^T x + G on A_x x A_y; the first expression
does not depend on x and the second not on y, hence M is constant on A_x x A_y, equal to M(x*, y*) for the Cramer basic points
x*, y*: a design number (ratio of design polynomials), so 0 or >= Des^{-2} by (D-G1a) (degree bound of (D-G1a) taken large enough
to contain Cramer numerators).  |M(x^#, y^#) - M(x_1, y_1)| <= Lip Des^3 (p+q)^{1/2} b << Des^{-2}, and |M(x_1, y_1)| <= b, so the
constant is 0.  QED
[G1_work/me2_check.py: 500 instances, max |M(x^#, y^#)| = 1.4e-14, displacement <= 1.26 b; contrast: if the constant on A_x x A_y
is a tiny NON-design number g' = b, the zero set is at distance >= 316 b (square-root scale) -- the design-number dichotomy is what
makes the exactification linear.]
Remark.  For SYSTEMS of multi-(X3) strict tiny minors, case (i) moves can conflict between minors and the Jacobians of the system
in one block have entries that are rate objects of the other blocks (their minors are not themselves in the rate scheme).  Closing
the rate scheme under these Jacobian minors (a finite operation at each level) would make a block-by-block induction possible;
not carried out.  OPEN (class (R-S2)).

## 5.2 The strict Farkas alternative in unshifted blocks, with generators
PROPOSITION 5.2.  PROVED (mod chain; first order at the start row; same proof as H2 Prop. 4.1 with H2 4.1's reformulation).
Let m be a (U)-block (inactive shift) at a stage satisfying the hypotheses of Theorem G1.C except A-regularity, and let M_1, ...,
M_k be its tiny strict minors (single (X3) row; M_i(r) = <C_i, r^(m)> by Lemma LE, c_i = 0).  Oriented cofactors C'_{i,l} := eps_l
C_{i,l}.  For a design-depth free coordinate s with robust room (an FR generator, K2.9/K2.16(2a)) put D_i(s) := <C_i, u^(m)(s)>
(a design number; D_i(s) = 0 if s is a row of M_i, Lemma 4.4); for a banked/S_th target coordinate s (one-sided raise) put
D_i(s) z_s.  Block m is residual for the strict system iff there is lambda in R^k with
 (a) (lambda^T C')_l >= 0 on strictly pinned kind-(iv) rows and (lambda^T C')_l = 0 on strictly pinned two-sided rows;
 (b) sum_i lambda_i D_i(s) = 0 for every FR generator s, and sum_i lambda_i D_i(s) z_s >= 0 for every one-sided raise s
     acting on the block;
 (c) sum_i lambda_i M_i(rc) > 0  (wrong sign at the prepared start row).
Proof.  Linearized feasibility: r^# = rc + sum_P a_l e_l + sum_Q b_l e_l + sum_s c_s u^(m)(s) + sum_s' e_s' z_s' u^(m)(s') with a, e >= 0
(oriented kind-(iv) raises and one-sided raises), b, c free, subject to <C_i, r^#> = 0 (strict exactness; all other rows banded,
Theorem H2.A's bands at the linear scale, which are << D_tol, so soft minors impose nothing: Theorem G1.A).  Farkas' lemma for this
polyhedral system gives (a)-(c); the homogeneity factor rho of H2 4.1 is absorbed since M_i(rho r) = rho M_i(r).  The first-order
action of the generator at s on r^(m) is c u^(m)(s)/kappa_m plus a multiple of r^(m) (Lemma 4.4's computation), and the latter changes
M_i only by the factor (1 - dkappa/kappa_m).  Realization of a linear solution: Hoffman for the polyhedral system with design
coefficients (V2 Lemma H; least nonzero minor >= delta'_comb) puts a solution within Des^C b of the start; Brouwer as in Theorem G1.C.
QED
COROLLARY 5.3 (FR generators).  PROVED (from 5.2).  (i) A strict resonance is never fixed by moves at its own FR rows (D_i(s) = 0
for s a row of M_i).  (ii) If block m has one tiny strict minor M with FR rows R and some FR generator s notin R (or a two-sided
thick-support generator, whose action is analogous) with D_M(s) != 0, then m is not residual.  (iii) For the Example-4.3 shape
with a FREE common target coordinate j (M = det[[r_+, r_-], [u_+(j), u_-(j)]]): residual only if every other design-depth FR coordinate
s shared by l_+, l_- has (u_+(s), u_-(s)) parallel to (u_+(j), u_-(j)) and every one-sided raise acts with the wrong sign.
[G1_work/me2_check.py: 972 random wrong-signed instances of (iii), all destroyed by one extra non-parallel FR generator.]

## 5.3 Contact-row resonances are realized
COROLLARY 5.4.  PROVED (mod chain).  The configuration of H2 Example 4.3 (two kind-(iv) rows l_+ in K^+, l_- in K^- of a (U)-block
sharing a coarse target CONTACT j, tiny minor M = det[[r_+, r_-], [u_+(j), u_-(j)]], oriented cofactors of one sign, M(rc) > 0) -- the
configuration (C3) underlying the persistent-residual candidates -- does NOT obstruct Step A^nat: after P^nat, j is a banked S_th
coordinate (Def. 4.1), the row (X1-c)_j is cushioned, M is soft with |M(rc)| <= (1 + 2Lip) b << mu_tol (Lemma 4.2(d)), so l_+-
are free or softly pinned, banded as free rows (Theorem H2.A's bands, ratio moves <= Des^C b/u << D_tol), and the block is not
residual.  The same holds for every resonance all of whose tiny minors contain a cushioned row (contact rows, tiny-support target
rows, (X4^0)/(X4) rows).
Proof.  Theorem G1.A ((E2) holds since |M| moves by <= Lip Des^C b/u), Corollary G1.B (ii), Theorem H2.A with P^+-_m = strictly
pinned rows (5.5 below).  QED

## 5.4 Linear descent inside Z^str for near-threshold carriers
LEMMA 5.5.  PROVED for the descent itself (mod H1 Lemmas 2.1-2.2 and the proof of J1.11); SKETCH for the hypothesis (NT_0).
Let kappa be a pattern whose tiny strict minors each contain one (X3) row, Z^str := (prod_m A_m) cap K_kappa (compact, semialgebraic,
defined over k), F := F_{Phi^T}.  There are constants eps_0, m_0, V > 0 depending only on (kappa, Phi^T) such that for every y in
Z^str with F(y) <= 1 + eps_0 and every mu' in (0, m_0]: there is y'' in Z^str with |y'' - y| <= 2V (F(y) - 1 + mu')_+ and F(y'') <=
1 - mu' (or F(y) <= 1 - m_0 already).  Insert 1/eps_0, 1/m_0, V into Des(L) (P-CHOICE).
Proof.  J1.11 (a)-(b) hold for Z^str by the same proof (it uses only compactness, semialgebraicity, definability over k and the
genericity of Phi^T over k; B^lin(Z^str) is k-semialgebraic of dimension < n).  Take the finite cover of Lambda := Z^str cap {F = 1}
by balls B(r_*^i, delta_i) of the local step, U their union, V := max |v_i|, m_U with F <= 1 - m_U on (Z^str cap {F <= 1}) \ U.  By
compactness there is eps_0 > 0 with F <= 1 - m_U/2 on (Z^str cap {F <= 1 + eps_0}) \ U (a sequence y_n notin U with F(y_n) in
(1 - m_U/2, 1 + 1/n] would accumulate at a point of Lambda \ U = {}).  For y in U the local step gives a curve in Z^str with F(gamma(t))
<= max(F(y) - 3t/4, 1 - 2m_*) and |gamma(t) - y| <= V t; take t := (4/3)(F(y) - 1 + mu'), admissible when eps_0, m_0 <= (3/16) min_i
delta_i/V.  m_0 := min(m_U/2, min_i m_*^i).  QED
(NT_0) (SKETCH): the near-threshold active carriers of (T)-blocks at the start ratios satisfy F(r_1) <= 1 + eps_0/2; then F(rho_1) <=
1 + eps_0 for the projection rho_1 of r_1 onto prod A_m (|rho_1 - r_1| <= Des^3 beta), and Lemma 5.5 with mu' = 3mu/4 (mu = c Des^{C_x
- 1} b) gives a target of (T3) at distance <= Des^C b: no Puiseux step and no non-linear displacement.  Whether the near-threshold
band of the stage selection can be taken <= eps_0/2 (it is a level-L design constant) is not checked against X1/J1.

## 5.5 The residual after G1
THEOREM G1.D.  PROVED (mod chain; H1's unrefereed results where (R0) is concerned; Lemma 3.4(c) of H2 where used).
For the design T_fin^{K2} with (FC), P-TU, F-2, (D-enum), (D-G1a), the split preparation P^nat and Step A^nat: (LSC-trunc)_N holds at
(f, g, rho) unless, at all but finitely many main stages, the selected stage has one of:
 (R-S1) a one-signed STRICT linear resonance: a block residual in the sense of Theorem H2.A with P^-_m := strictly pinned K^- rows and
        P^+_m := strictly pinned or locked K^+ rows; in (U)-blocks exactly the alternative of Proposition 5.2 (tiny strict minors,
        all built from one (X3) row and FR rows of free target coordinates with robust room; annihilated by every FR generator);
 (R-S2) a system of tiny strict minors with >= 2 (X3) rows that is not exactified at the linear scale (Lemma 5.1 covers one minor);
 (R-S3) a near-threshold carrier of a (T)-block whose LINEAR descent (Lemma 5.5, or the direct lowering (T3)) is blocked by
        one-sidedness: H2 5.3's inward-locked K^+ carrier without a kappa-raising lever, or a strictly pinned carrier all of whose
        descent directions inside Z^str lower a K^+ kind-(iv) row;
 (R-L)  a locked K^+ row (H2 Lemma 3.4(c), SKETCH there);
 (R0^str) H1's thick-type residual conditions (H-2)-(H-5'), (H-7) with "pinned" read as "strictly pinned" and Step A at x^nat
        [transfer of H1's lever lemmas to the linear scale: SKETCH, they are first-order statements]; (H-6') reduced to (R-S2) and
        to thick peaks of shifted blocks.
Proof.  If none occurs at infinitely many main stages, Theorem G1.C applies at those stages: (R-S2) absent gives Lemma LE's affine
targets (or Lemma 5.1 when a single two-(X3) minor occurs), (R-S3) absent gives (T3) targets at the linear scale, and the absence of
(R-S1), (R-L), (R0^str) gives A-regularity of the band-relaxed Step-A^nat system by Theorem H2.A (its proof with "pinned" replaced by
"strictly pinned": softly pinned rows are banded as free rows, with band half-width beta_1 <= Des^C b/u << kappa_min D_tol) and by H1
in the thick-type case.  Theorem G1.A then gives the transplant and J1.15'/J2.1 the stage, hence (LSC-trunc)_N.  QED

REALIZED by G1 (were residual or unproved before):
 - every residual whose tiny objects all contain a cushioned row: H2 Example 4.3 / (C3) contact-row resonances (Cor. 5.4), resonances
   through tiny-support target rows, (X4^0)/(X4) rows; H1's (H-6') nonlinear pinned groups coming from R_a^2 entries;
 - the preparation-bias source (ii) of H2 Theorem H2.B (Lemma 4.2(e): b_bias << b; banks do not move the resonances they cushion,
   Lemma 4.4); remaining start-row changes are (P1) closings (f's datum at the window);
 - F-NE (b >> s_1/T >> delta_Z) for soft objects (tolerance mu_tol >> b instead of (VT')); exactness of cofactor polynomials;
 - non-linear Lojasiewicz/Puiseux displacements: single-(X3) strict resonances (Lemma LE), a single two-(X3) strict minor (Lemma 5.1),
   near-threshold descent inside Z^str (Lemma 5.5, given (NT_0)); the Step-A scale is linear in b (Lemma 3.2), with (K2-d),
   (L-K2-1), (L-K2-2), (W_exp), (LATE), Lemma S2c^tr and Lemma III-drift re-checked (Lemma 3.3).
NOT realized: (R-S1), (R-S2), (R-S3), (R-L), (R0^str).  Exactness of strict minors cannot be dropped (two-ray example, part 1
Remark (c)); the strict tolerance is (VT') and F-NE persists for strict objects (part 3 discussion: raising s_1 to the level of b
would need bank masses >> b/T, whose bias wrecks the clean classification).

PERSISTENCE (strict form of H2 Theorem H2.B; PROVED as a necessary condition, mod chain).  If (LSC-trunc)_N fails at (f, g, rho), then
at all large main stages one of (R-S1)-(R-S3), (R-L), (R0^str) occurs; for (R-S1) this requires a tiny NONZERO strict minor, i.e. a
near-linear relation <C, r^(m)> ~ 0 between f's block ratios with coefficients = minors of design target values at FREE target
coordinates with robust room, which (Cor. 5.3) every other FR generator of the carriers must annihilate and every one-sided raise
must act against; by H2 Lemmas 2.6/2.7 the carriers are fresh at consecutive (R1) stages.  OPEN whether such f exist.
