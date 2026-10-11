# G1-ref part 3: Lemma LE, Def. 3.1 / Lemma 3.2, Theorem G1.C, Lemma 3.3, Lemma 4.2, Lemma 4.4

## 3.1 Design numbers and (D-G1a) -- CORRECT with P-21b (part 2)
Minors of size <= 2L of strict design rows are polynomials of degree <= 2L with coefficient sum <= (2L)!; minors of size
<= 2L+1 of matrices with such entries have degree <= 4L^2 + 2L and coefficient sum <= (2L+1)!((2L)!)^{2L+1} <= 2^{L^4} for L
large.  With all data of modulus <= 1 every such value is <= 2^{L^4}; the least nonzero modulus delta'_comb(L) > 0 is a minimum
over finitely many numbers (finitely many patterns of level L).  (D-G1a) is a monotone, f-free, N-free insertion; requiring
u(w) <= delta'_comb(L) only constrains the first sub-window band (u(w) = b(w^-) for the others, Def. III-Tfinstage (S6)).
The data must include robust-peak and (KN)-block weights (P-21b).

## 3.2 Lemma LE -- CORRECT
(a) Expansion along the unique (X3)_m row: entries 1 (column Delta'_m, if active and selected) and -r_l; the complementary minors
involve only FR rows and single-variable rows (no ratio; Lemma III-Uscale (a): (X1) rows contain no ratio).  So M is affine in
r^(m) with design coefficients, c_M = 0 for an inactive shift.  (b) Inconsistency would give lambda with C^T lambda = 0,
c^T lambda = 1; a basic solution has entries = ratios of design polynomials, ||lambda||_1 <= (2L+1) Des^{3/2}; then 1 =
lambda^T(C r_1 + c) <= Des^2 beta < 1.  Cramer point: delta_K = -C_{B,K}^{-1} e_B with |det C_{B,K}| >= delta'_comb >= 1/Des and
cofactors <= 2^{L^4}, so |delta|_2 <= q^{3/2} Des^{3/2} beta; consistency transfers B's equations to all rows.  (c) clear.
Numerics (ref_le_44_check.out): Cramer points exact to rounding in 3000 random integer design systems.
The one-sided version used in (T1) (a point of A_m satisfying eps_l(rho_l - r_{1,l}) >= 0 on strictly pinned kind-(iv) rows, if
one exists, within Des^4 beta): Hoffman's bound for a polyhedron is the max over linearly independent row subsets of the
inverse smallest singular value; rows are design rows of C and coordinate vectors, so every nonzero maximal minor is a design
number >= 1/Des and the constant is <= Des^{2}; r_1 satisfies the one-sided constraints and violates the equations by <= beta.
Correct.  (In (U)-blocks the one-sided constraints must be read at the coupled targets s_m rt, as G1 says; homogeneity keeps A_m.)

## 3.3 Definition 3.1, Lemma 3.2 -- CORRECT after G-T2
Lemma 3.2 (right-hand side at the linear scale): Ft_l = kappa_m(rc_l - rt_l) is 0 for zero-displacement targets, <= kappa Des^4
beta for (T1), <= kappa Des^C b for (T3)-(T5); the TU pre-placement residue is second order.  Re-derived (mod P-TU).
G-T2 (gap in (T2)/(T5) and in (E3) of Theorem G1.C).  (T2) gives "symmetric bands for two-sided rows" of half-width up to
min(beta_*, kappa_min D_tol) to softly pinned and free active ratios of EVERY block.  In a (T)-block a band on an active row l
with r_l != 0 changes R_a(m)^2 by up to 2m^2|r_l| beta_band/kappa at FIRST order, hence the protected floor statuses rho^0_d =
m|r_d| K(sigma_rob, R_a^2)/Phi_d by up to Des^C beta_band.  With beta_* ~ Des^C x^nat/u this is ~ Des^C b/u, while the margin is
mu = c Des^{C_x - 1} b.  Since u(w) = b(w^-) is NOT bounded below by any power of Des(L) (Def. III-Tfinstage (S6)), no choice of
the absolute C_x makes the margin dominate: the verification of (E3) in G1.C ("the frozen statuses at the targets are as
prescribed") checks the targets, not the realized point inside the bands.  The same first-order effect in (U)-blocks is what
J1-ref F-2's coupled rescaling repairs, but (T5) fixes s_m := 1 - 4 Des^{C_x} b instead of F-2's joint selection at the
realized values.
FIX (PROVED; this is the band set of Theorem H2.A, which is all that Theorem G1.D uses): (i) in PROTECTED blocks ((T)-blocks with
N(m) nonempty, (KN)-blocks with pushed inactive near-threshold carriers; elsewhere bands move only robust statuses, by
Des^C beta << u) no symmetric bands: two-sided (kind (i)) rows are realized exactly at their f_1 ratios (private two-sided resources), kind-(iv)
K^- rows get shrinking overshoot bands (Lemma K: shrinking |r_l| lowers every status of the block, sigma being pattern-only),
K^+ rows of protected blocks are locked ((R-L)); quadratic effects of zero-data rows are covered by (J-e):
mu >= C D^C m^2 (beta_*/kappa)^2 holds since (Des^C b/u)^2 << Des^{C_x} b (b << u^2 by b <= T^4 and u >= T^{1/20}).  (ii) in
(U)-blocks s_m is F-2's joint selection at the realized values, 1 - s_m <= C(Des^{C_x} b + D^C sum_l(|r_l| beta_l/kappa +
beta_l^2/kappa^2)) <= Des^C b/u << u; rescaling preserves Z^str (homogeneity, c_M = 0) and moves soft minors by << mu_tol.
With (i)-(ii) the realized protected statuses are <= the target statuses (T-blocks) or restored by s_m (U-blocks).
((KN)-block K^+ bands inherit J1's (KN) SKETCH, as in H1-ref P-KN.)

## 3.4 Theorem G1.C -- CORRECT (mod chain) after G-T2, P-A1, P-23, and with the generalization G-S2 (part 4)
Brouwer realization with frozen (FC) scalars (J2.1, J1.8(a), Lemma III-cone (c)) realizes targets exactly on equality rows and
within the bands elsewhere.  (E1): strictly pinned ratios are realized exactly on A_m (or, after G-S2, at the given exact point of
Z^str); (E2): soft minors move by <= Lip(W^nat + beta_band)/kappa_min << mu_tol (needs C_T as in P-23), robust minors move << u,
(U)-rescaling multiplies minors by s_m^e; (E3): after G-T2.  Closeness |r^# - r(f)| <= Des^C b/u^3 << eta' (P-A1).  Cost
C_f Des^C W^nat log(1/W^nat) <= C_f Des^C b log^3(1/T)/u^3 = o(u^2 T^2) (b <= T^4, u >= T^{1/20}).  The infinitely-many-stages
conclusion is J1.15'/J2.1 + Theorem E^{eng,RT,inf} as before.  The hypothesis "band-relaxed Step-A^nat system A-regular" is a
genuine hypothesis (it is what Theorem G1.D reduces to residual classes).
Hypothesis "(NT_0) automatic": PROVED.  Near-threshold carriers of N(m) have |rho_l(f) - 1| <= b (the threshold distance is a
rate object, so at a clean sub-window it is <= b or >= u; Part II's (X4) criterion gap < t^2 <= T_hi^2 << u selects the first
case); Lemma III-Tblock (a) gives rho^0_l(r(f)) <= 1 + b + C sigma_rob^{-6}(b + c_{L+1}^2) <= 1 + Des^C b; preparation and
projection onto prod A_m add <= Des^C b; and b <= eps_0/Des^C by P-CHOICE (eps_0 a level-L design number fixed before b(w)).

## 3.5 Lemma 3.3 (bookkeeping) -- CORRECT with P-L1
(a) theta_pr must be >= 64 rho A_0 s_1/T, not 8 rho A_0 s_1/T: Part III's (L1) (Lemma III-late) is s_1 <= theta T/(64 rho A_0)
(so that no S_th coordinate enters the raise set W_F: 32 rho s_1 max|b^theta| <= 32 rho s_1 A_0/T <= theta/2).  (P-L1; the
K2 constant 8 is the older form.)  The other purposes of the private mass (Sys-DC levers (L2), cushions, one-sided raises)
are as G1 lists; I checked Lemma III-depthclean: "the pre-row moves design-depth coordinates by <= K_w Pi << theta_0" concerns the
normer/rooms (TS, FR types), not support moduli, which the pre-row only raises (W_F) or leaves; so theta_pr << K_w Pi is
harmless.  (b)-(f): re-derived.  At the linear scale 1/gap_min <= Des^C/b <= exp(C log^3(1/T)) (log(1/b) <= C log^3(1/T),
Lemma III-late), and K_w, Lambda_lev are polynomial in the window quantities (cert2: absolute exponents), so K_w <=
exp(C log^3(1/T)); s_late >= exp(-C' log^3(1/T)) >> s_1 ~ exp(-1/(2T)); (L2), (L3), (L4) hold likewise.  Drifts C_f Des c_{L+1}
<= C_f Des e^{-1/T} << mu.  Costs as stated.

## 3.6 Lemma 4.2 (split preparation P^nat) -- CORRECT (mod chain) with P-L1
(a)-(c) as Lemma III-prep with two masses; (d) is Lemma 2.3 with theta_T; (e) a bank of mass theta at a contact s moves values by
(mu_s^2/nu) theta u(s) z_s (first order; nu changes only at second order since a_s = 0 before the bank), a raise by
(mu_s^2/nu) Delta a_s Dev(s); so strict minors move by <= Lip C dbar(L)(theta_T + theta_pr) =: b_bias = b T_hi (Des/u)^{C_T + C}
<< b (T_hi <= B^{-omega(L)}).  (f) idem.  Note: theta_T << theta_0 = b/Des^{C_P} (G1 lowers the target masses relative to K2 and
gains the tolerance through the division by T_hi in mu_tol), so "(K2-d) is used only at target coordinates" (Lemma 3.3 (a)) should
read: (K2-d) is replaced everywhere, by theta_T at targets and theta_pr elsewhere.  Cosmetic.

## 3.7 Lemma 4.4 (row-aligned moves) -- CORRECT with P-44
First order: Delta r^(m) = (c u^(m)(j) - r^(m) dkappa)/kappa_m; on the columns of M the change of (X3)_m is -(c/kappa)(X1)_j -
(dkappa/kappa)(X3)_m, so dM = -(dkappa/kappa) M: the move multiplies M by (1 - dkappa/kappa); it is ZERO only when M = 0.
P-44: (i) "the first-order change of M is zero" should read "M is multiplied by 1 - dkappa/kappa_m" (in particular a move at j
can neither create nor destroy the vanishing of M, and changes a tiny M only by a tiny relative amount); (ii) the lemma needs that
M contains no other ratio-dependent row (no (X4^0) row of a block whose values move, no second (X3) row): with an extra
(X4^0)-type row the first-order change is not a multiple of M (ref_le_44_check.out: relative deviation 7e1 vs 1e-8).  For
STRICT minors (the case used in Prop. 5.2 / Cor. 5.3) the condition holds automatically.  A bank at a contact j concerns SOFT
minors (the row (X1-c)_j is cushioned), a z-move at a free j concerns strict minors containing (X1-FR)_j.
Numerics: identity dM = -(dkappa/kappa) M confirmed to 1.4e-8 relative in 2000 random instances.
