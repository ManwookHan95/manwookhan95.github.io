# H2 part 4: the residual of (R1) after Theorem H2.A -- one-sided pinned resonance; examples; persistence

Setting of H2_part1-3.  Theorem H2.A leaves, at an (R1) stage, only RESIDUAL blocks: (two) P^-_m, P^+_m != {}; (up) P^-_m != {}; (down)
P^+_m != {} (P^+-_m = pinned or locked kind-(iv) rows of sign +-).  Here we describe exactly what remains.

## 4.1 Reformulation: residual = infeasible one-sided target problem.  PROVED.
Extend Sys-A by the admissible TARGET displacements as generators (H1 Lemma TF; J1 7.4(a)): a displacement Delta of the targets with
rt + s Delta admissible (J1.13 (i)-(ii)) for small s acts on y^T Ft by -s <kappa y, Delta>.  A stage is realized iff the extended generator set
positively spans the needed correction with margin (K2.9 + Lemma TF); a residual stage carries a near-certificate y of the EXTENDED system:
 y^T g >= -eps for every Sys-A generator, |y_l| small on banded rows, and <kappa y, Delta> <= eps' for every admissible displacement Delta.
For a pinned row the admissible displacements are those tangent to Z_kappa (and the block rescaling in (U)-blocks); so on the pinned rows
of a block, kappa y lies (up to eps') in the span of the gradients of the tiny minors and cofactor polynomials (the normal space of
Z_kappa at r''), and phi_y = y^T Ft(R_1) is, to first order, the value at the start row of the corresponding combination of tiny minors.
(Proof: Lagrange/Farkas for the linearized problem; the identification of phi_y uses Ft(R_1) = kappa (rc - rt) (J1.2) and rt in Z_kappa.)

## 4.2 (U)-blocks: the residual is a one-signed linear resonance.  PROVED.
In a (U)-block every minor and cofactor polynomial of Gamma^#(kappa, a) is homogeneous in r^{(m)} and contains r^{(m)} only through the row
(X3)_m: sum_{Omega_a(m)} r_l gamma_l = 0 (X1 2.1(U), X1-ref D1).  Expanding a minor along (X3)_m, M_i(r) = sum_l C_{i,l} r_l with cofactors
C_{i,l} that do not involve r^{(m)} (design data: contact values u_l(j), peak traces, signs).  Write rt_l = eps_l r_l (oriented), C'_{i,l} :=
eps_l C_{i,l}.  The one-sided constraints of kind-(iv) rows, with the two-sided kappa lever and the rescaling s of the block, are:
realized oriented ratios rt^#_l with rho rt^#_l >= rc_l for kind-(iv) l (rho := s kappa^#/kappa > 0 free), rt^# on Z_kappa.
PROPOSITION 4.1.  Let block m be a (U)-block at an (R1) stage, and let the tiny minors involving pinned rows of m be the linear forms M_i
(i in I_m) above (the cofactor polynomials not involving r^{(m)}).  Then block m is residual (no admissible realization of its pinned rows
keeping all kind-(iv) rows one-sided) iff, to first order at the start row, there is lambda in R^{I_m} with
      (lambda^T C')_l >= 0 for every pinned kind-(iv) row l,   (lambda^T C')_l = 0 for every pinned two-sided row l,   sum_i lambda_i M_i(rc) > 0,
i.e. a combination of tiny minors that is a NONNEGATIVE linear form in the oriented pinned kind-(iv) ratios, blind to the two-sided ones,
and strictly positive at the current point.
Proof.  Linearized feasibility of {rt : M_i(rt) = 0 (i in I_m), rt_l >= rc_l/rho (l pinned kind (iv))} with rho free; since the M_i are
homogeneous of degree 1, rho can be absorbed (rt -> rt/rho), so feasibility is that of {A rt = 0, rt_P >= rc_P} with A = (C'_{i,l})_{i,l} on the
pinned columns (two-sided columns unconstrained).  Farkas' lemma (alternative for {A x = 0, x_P >= c_P, x_Q free}): infeasible iff some
lambda has (lambda^T A)_Q = 0, (lambda^T A)_P >= 0 and (lambda^T A)_P c_P > 0, and (lambda^T A)_P c_P = lambda^T A rc = sum_i lambda_i M_i(rc)
(two-sided columns contribute 0).  Free rows are banded (Lemma 3.4(a)).  QED
COROLLARY 4.2.  A (U)-block is NOT residual if some pinned two-sided (kind-(i)) row has a nonzero cofactor in every tiny minor that
involves a pinned kind-(iv) row, or if the cofactors of the pinned kind-(iv) rows in every such minor have both signs (after orientation).

EXAMPLE 4.3 (the residual is non-empty at a single stage).  PROVED (finite algebra).  A (U)-block with exactly two active rows l+, l-
(both kind (iv), rt_{l+} > 0 > rt_{l-}; necessarily of both signs since sum_l rt_l |gamma_l| = Delta'_m = 0, J2-ref D.4) and one tiny minor
M = det[[r_{l+}, r_{l-}], [u_{l+}(j), u_{l-}(j)]] (the (X3)_m row and the contact row at a common target contact j).  In oriented variables
M = C'_+ rt_+ + C'_- rt_-; when C'_+, C'_- > 0 the block is residual iff M(rc) > 0, whatever kappa^# and s.  [The feasible set {rt_+ >=
rc_+, rt_- >= rc_-} ∩ {C'_+ rt_+ + C'_- rt_- = 0} is empty iff C'_+ rc_+ + C'_- rc_- > 0.]  The sign of M(rc) is a datum of f at the stage
(|M(rc)| <= (1 + Lip C_*) b by cleanness), not controlled by the design.  So at a SINGLE stage (R1) can be genuinely obstructed.

## 4.3 Shifted blocks.  PROVED (statement), SKETCH (explicit Farkas form).
In shifted blocks the minors depend on r through (X3) (Delta'_m = sum r_l gamma_l), the columns c_l(r_l) = u_l - r_l tau_m (Lemma EC) and, in
(T)-blocks, the (X4^0) entries m^2 |r_l| K(sigma_rob, R_a^2) (all active ratios of m through R_a^2).  The residual is the analogous statement:
the normal space of Z_kappa at the Lojasiewicz point contains a vector nonnegative on the oriented pinned kind-(iv) coordinates
(modulo the one-sided kappa lever: in (up) blocks the lever direction rt^{(m)} may be added with a positive coefficient, in (down) blocks with
a negative one), zero on two-sided pinned coordinates, with a positive value at the start row.  SKETCH: the explicit cofactor form is
not written (nonlinear (X4^0) entries).

## 4.4 Persistence: what (R1) at ALL large main stages requires.  PROVED (each item), OPEN (exclusion).
Assume (R1) at every main stage L >= L_0.  Then:
 (a) [Lemma 2.1 at every stage] a is b(w(L))-thin on F ∩ [1, D(L)] \ T(L) for every L >= L_0; with Lemma 2.2, |a_j| <= b(w(L)) for every j in
     F ∩ (union S_k) with L < j <= D(L) and j notin T(L): the base part lives, up to super-thin mass, on target coordinates.
 (b) [Lemmas 2.3, 2.5] at every stage every kind-(iv) carrier's whole pull range is anti-sign super-thin support (the minimum of its private
     range); super-thick pull ranges never occur.
 (c) [Lemma 2.6, memory] no carrier is kind (iv) with the same switching sign at two consecutive main stages, and no unpulled-peak
     (up)/(down) configuration of a block repeats with the same shift sign at consecutive main stages.  In T_fin the memory reaches the
     next TWO main stages (a pull-range coordinate j of stage p enters T only through the absorbers of E^ch(L) with L >= j, and the first
     such main stage is two rounds later); see 4.5 for a design variant with unbounded memory.
 (d) [Theorem H2.A + 4.1-4.3] at every stage some block carries a one-sided pinned resonance (or a locked K^+ row in a (down)/(two) block):
     a combination of tiny minors, one-signed on the oriented pinned kind-(iv) ratios, of the wrong sign at the start row.
 (e) [consequence of (c), (d)] a resonance with the SAME carriers and signs cannot recur at consecutive stages; in particular an EXACT
     relation of f (a tiny minor recurring with the same carriers, hence vanishing exactly at f's ratios) cannot by itself produce (R1) at
     all stages.  [Remark: for such an exact relation the preparation (P2)/(P3) is what puts the start row on the wrong side -- it raises
     every kind-(iv) value by eff v theta_0 > 0, and a nonnegative form then becomes positive; so a stage-wise obstruction from an exact
     relation is an artefact of the preparation, but by (c) it cannot persist anyway.]
 So persistent (R1) needs, at (almost) every main stage, a NEW wrong-signed one-sided resonance among kind-(iv) carriers in fresh
 orientation.  Nothing proved here excludes this; it is a sequence of codimension-one sign conditions on f, one per stage, each among
 fresh data (new coarse carriers, new tiny minors).  OPEN.

## 4.5 Design variant with unbounded memory (SKETCH).
Modify T_fin only in two bookkeeping choices: (D-enum) the pool enumeration satisfies max supp y^(i) <= i and the block schedule
satisfies i_nu <= nu; (D-abs) the coordinates absorbed at CLUSTER stages are E^ch'(p) := T(p) ∪ (Z_0 ∩ [1, p]) (no signature
coordinates).  Then T(L) ∩ (union S_k) ⊂ [1, r(L)], r(L) = number of rounds up to L, and the memory of Lemma 2.6 extends to every later main
stage with r(L'') < j_min(p) -- astronomically many rounds.  Consequently: under (R1) at all large main stages, each (carrier, sign) pair
and each (robust peak, shift sign) pair is used at most once in the kind-(iv) / unpulled role.  Status: (D-enum) is harmless (only the order
of a countable pool); (D-abs) removes absorber stages for signature coordinates -- absorbers carry no switching in route V (X2-ref R-abs,
Q1-refa: route-X absorbers are off the MT VI tree), but the (W4'') weight conditions attached to the removed absorbers would have to be
re-checked line by line: SKETCH.  Even with unbounded memory, (R1) is not excluded (fresh carriers at every stage).

## 4.6 What would close (R1).
 (i) A resource acting on pinned kind-(iv) ratios in the downward direction: none exists privately (Lemma 2.5), none through two-sided
     generators (the certificate is orthogonal to them), none through target freedom in Z_kappa (Prop. 4.1: the normal cone is one-signed).
 (ii) An argument that the class data exclude a wrong-signed one-signed resonance: the data lie in the cone only up to O(K t) >> b, so the
     sign of a tiny minor (<= b) is not seen by the data (HEURISTIC; no proof that it cannot be seen).
 (iii) A different treatment of tiny minors whose zero sets have one-signed normal cones on one-sided coordinates: e.g. keep such minors
     tiny-but-nonzero and control the projection of the class data by the face structure instead of the Hoffman constant of the whole
     cone (V2 Lemma H gives max(1, ||A||)^{n-1}/(least nonzero minor); a face-wise version insensitive to minors not met by the data
     would suffice).  Not attempted here.  This is the most promising direction (it attacks the exactness requirement itself).
