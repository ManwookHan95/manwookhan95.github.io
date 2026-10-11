# H1 part 4: the unit calculus in unshifted blocks; the residual after H1

Setting of parts 2-3.  Fix a (U)-block m.  A UNIT of m is either a pinned group G (Theorem GS) all of whose ratios lie in m (an
"internal" group), or a single movable row l of m (inactive row, or active row with a free ratio).  Pinned groups that link m to other
blocks are treated in Remark 4.3.  For a unit E put zeta^E(y) := sum_{l in E} y_l rt_l, and for E consisting of thick-type and kind-(i)
rows put Xi_E := sum_{thick-type l in E} rho_l u_l(xhat_1)  (so zeta^E(y) = kappa_y Xi_E/kappa_m + O(Design^3 (eps + eta')) by Lemma AL).
Nearly neutral rows are units with zeta^E = O(b) and are relieved by Theorem IN anyway; below "unit" means a unit with |rc_l| robust
for some l, or a pinned group.

## 4.1 Lemma DS (down-scaling of unions of units is admissible).  PROVED (modulo the chain).
Let E_1, ..., E_q be units of a (U)-block m and s in [1 - Design^{-C}, 1].  The targets rt'_l := s rt_l (l in E_1 ∪ ... ∪ E_q), rt'_l := rt_l
otherwise, are admissible (J1.13 (i)-(ii)), and <kappa y, rt' - rt> = -(1 - s) kappa_m sum_i zeta^{E_i}(y).
Proof.  Z_kappa: every tiny polynomial involves the ratios of at most one internal group of m (or none) and is homogeneous in them
(Theorem GS(a)); free and inactive ratios enter no tiny polynomial.  Robust minors move by <= Lip (1 - s) ||rt|| << u.  Statuses (Lemma K,
rho_d = m |r_d| K(sigma, R^2)/Phi_d, R^2 the full Omega sum of m): R^2 does not increase; scaled rows lower |r_d| and K, unscaled rows lower
K: every non-peak status of m decreases; robust peaks move by << u; other blocks are untouched.  In a (U)-block there are no (X4^0) rows
and no Puiseux constraint; the class data are projected at the realized ratios (J1.13 (iii)): the (X3)_m row sum_l r_l gamma_l = 0 is
violated by the original data by <= |rt' - rt| ||gamma|| <= Design^C (x/u)(12 sum lambda/t) << K t.  Distance: as in Theorem RL.  QED

## 4.2 Theorem UC (unit calculus).  PROVED (modulo the chain).
At a stage carrying near-certificates, Step A is realized if some (U)-block m satisfies one of:
 (UC1) some unit E of m has zeta^E(y) <= -z_E for every near-certificate y (z_E := c_* u^3/(C nu_1 Design^C)); for thick/kind-(i) units:
       Xi_E >= u^3 kappa_m/Design^C (an ALIGNED-dominated unit);
 (UC2) m has a private two-sided peak resource and some unit E has zeta^E(y) >= z_E for every near-certificate (thick/kind-(i) units:
       Xi_E <= -u^3 kappa_m/Design^C, an ANTI-ALIGNED-dominated unit);
 (UC3) m has no private two-sided peak resource (zeta_m(y) has the fixed sign sigma_m and |zeta_m| >= z_0, Lemma NP) and some union of
       units E satisfies zeta^E(y) - zeta_m(y) >= z_E for every near-certificate y (then down-scale the complement of E).
Proof.  (UC1) Lemma DS with the single unit E: pairing (1 - s) kappa_m |zeta^E| >= (1 - s) kappa_m z_E; Lemma TF' with 1 - s := 4(||b|| + x)/
(kappa_m z_E).  (UC2) Down-scale ALL units of m other than E and all remaining rows of m (nearly neutral, kind (iv), D2-pushed: each a
movable row or inside an internal group, so the union is a union of units): pairing -(1 - s) kappa_m (zeta_m - zeta^E) and |zeta_m| <=
(4/3) eps Design (R-PK), so the pairing is >= (1 - s) kappa_m (z_E - 2 eps Design) > 0.  Lemma DS, Lemma TF'.  (UC3) the same complement
scaling, pairing -(1 - s) kappa_m (zeta_m - zeta^E) >= (1 - s) kappa_m z_E.  QED
Consequences (PROVED).
 (a) In a (U)-block WITH a private peak resource, a residual stage has: no movable thick-type row with robust or near-threshold status
     (aligned ones by (UC1), anti-aligned ones by (UC2): |zeta^{l}| = |y_l rt_l| is robust by Lemma AL) -- this covers J1's (R-np) for such
     blocks, (R-D2) (D2-pushed anti-aligned rows: the complement is scaled, the D2 row itself keeps its target, its status only decreases),
     and (J-c)/(J-d) without bands; and every internal pinned group is BALANCED: zeta^G(y) is not robustly of one sign over the
     near-certificates -- for thick/kind-(i) groups, |Xi_G| = |sum_{thick l in G} rho_l u_l(xhat_1)| <= u^3 kappa_m/Design^C, a cancellation
     between aligned and anti-aligned PINNED carriers inside one group.
 (b) In a (U)-block WITHOUT a private peak resource: sigma_m = -1 is Theorem RL; for sigma_m = +1 (aligned peaks, zeta_m >= z_0) a residual
     stage has zeta^E >= -z_E for every unit E and zeta_m - zeta^E >= -z_E for every union E, i.e. 0 <~ zeta^E <~ zeta_m for all unions of
     units; together with the failure of up-scaling (protected block, Lemma KC fails).  Since sum over all units + (kind (iv) and nearly
     neutral rows) of zeta^E = zeta_m, at least one unit (or kind-(iv) row) carries a robust positive part: an anti-aligned-dominated
     unit whose up-scaling is blocked by a near-threshold status.
 Remark 4.3 (groups linking several (U)-blocks).  If a pinned group G meets (U)-blocks m_1, ..., m_r, Lemma DS holds with the pairing
 -(1 - s) sum_i kappa_{m_i} zeta^{G ∩ m_i}; (UC1) holds verbatim with the kappa-weighted zeta^G_kappa := sum_{l in G} kappa_{m(l)} y_l rt_l; (UC2)
 needs the complement of G in the union of the blocks met by G (each with a peak resource).  Groups linking a (U)-block to a SHIFTED block
 are not scalable (no homogeneity in shifted blocks): they belong to the class (S) below.

## 4.4 Peak conversion of anti-aligned near-threshold zero-data rows (SKETCH)
Let d be an inactive (zero-data) near-threshold thick-type row of a (U)-block that is anti-aligned (needs OUTWARD) and has no partner.
Instead of the D2 inward push, freeze d as a PEAK in the target pattern ((FC) with P_f := P_rob ∪ {d}) and give Step A the one-sided
band row rho_d in [1 + beta_*, 1 + 3 beta_*] (outward, the needed direction).  In an unshifted block a peak carries no class data (Lemma NP's
proof), so the cone Gamma^#(kappa, a) is unchanged; consistency of (FC) at the realized point holds by the band row (J2's argument);
the frozen system is C^{1,1} along the realization (d crosses the threshold once, inside the frozen system).  If the block has a private peak
resource, J1.6's Corollary then forbids d (a thick-type peak) in any near-certificate unless y_d carries the band weight, and J1.8(b)
gives phi_y > (1/2) |y_d| beta_d - rho_0: the band relieves.  MISSING for a proof: the downstream legitimacy of a zero-data weak peak
of margin ~ beta_* (U1 Prop. 2.2 (a): the peak-error term e_d <= t/(lambda_d mu_d) of the projection must be <= K t, which needs the
decomposition's excess at d to be O(K t) -- true when d is inactive in the class, since inactive components are below A_i K t; and the
kind/screening bounds CM'(a) Scr_m for coarse peaks of non-robust margin).  Label: SKETCH.

## 4.5 The residual after H1 (precise; necessary condition for a stage NOT to be realized).  PROVED as a consequence of 1.3, 2.3, 2.5,
## 3.3-3.7, 4.2 (each modulo the chain cited by J1.15/J2.1).
(f, g, rho) fails to be covered at a main stage only if Step A carries near-certificates and ALL of the following hold, where
"thick row" means a thick-type row with robust or near-threshold status (nearly neutral thick rows are always relieved, Theorem IN):
 (H-1) [no (T)-type residue] nothing: (R-T) is empty (Corollary 1.3);
 (H-2) [aligned movable rows] no thick row that is movable and aligned exists (Theorem IN), in any block;
 (H-3) [unshifted blocks with peak resource] every thick row is pinned and every internal pinned group is balanced (4.2(a));
 (H-4) [unshifted blocks without peak resource] the peaks are aligned (sigma_m = +1), the block is protected, Lemma KC fails, and all
       units satisfy 0 <~ zeta^E <~ zeta_m (4.2(b));
 (H-5) [shifted blocks: (T), (KN)] every movable thick row is anti-aligned; robust ones have no exchange partner and sit in protected
       blocks (Theorem OUT): within each such block all robust movable thick rows share the value of rho_l/u_l(xhat_1) (anti-aligned
       proportional resonance, a_p = -alpha_m u_l(xhat_1) v_l(p), alpha_m > 0), and no aligned or kind-(i) movable row with robust status
       exists there; near-threshold anti-aligned movable rows ((R-D2)-type and free near-threshold actives) are unrelieved;
 (H-6) [shifted blocks: pinned rows and thick-type peaks] the normal resonance of 3.6 (S): no admissible point of Z_kappa pairs robustly
       with all near-certificates;
 (H-7) [J1's conditions] no helpful far coordinate on any thick-type carrier (frozen far windows), no private two-sided design-depth
       resource of a thick-type carrier, tiny spreads (J1.15' (J-a), (J-b)); in blocks with a peak resource, forced mixed alignment or
       kind-(iv) compensation (Proposition MA).
OR (R1) of J1-ref (no thick-type carrier; parallel task H2).
Every item is a codimension >= 1 coincidence among f's data at the stage (balanced groups, proportional resonances, normal resonances)
or a sign/orientation configuration (alignment pattern) that must persist at ALL large main stages.  Nothing points to a non-recoverable
mate; no counterexample is claimed.

## 4.6 Numerics for the unit calculus (sanity only; H1_work/complement_toy.py, complement_toy.out)
Same consistent toy (all targets free, so every row is a unit).  zeta_m(y; rc) = O(1e-7) at the exact certificate (R-PK in variant A).
(UC2) "keep row k, down-scale all other rows" with 1 - s = 4 phi_y/(kappa |zeta^{k} - zeta_m|): for the ANTI-ALIGNED k, phi_y becomes -3e-3 and
the minimal move drops from 2.0e-2..1.0e-1 (variant A) resp. 29..175 (variant B) to 7.0e-4..9.2e-3 (8/8 cases); for the ALIGNED k the same
operation gives phi_y = +5e-3 and the move stays or grows (8/8).  (UC1) for the aligned row is the inward move of 3.8 (8/8 relieved).

## 4.7 Shifted blocks: the residual is "outward-wanting near-threshold rows" (PROVED reading of (H-5), (H-6) for (T)-blocks)
In a (T)-block the admissible target set may be taken as Z_kappa ∩ B(r_1, eta' + Design^C beta_*/kappa) ∩ {F <= 1 - 3mu/4} (J1.13 (i)); by
Proposition J1.11 (Lemma 1.2) its achievable displacements at r'' contain an open cone around the Puiseux direction v (d psi_d v = -Phi_d,
d in D).  If (H-6) holds with the polar representation kappa y|_{T Z} = sum_{d in D} c_d d(psi_d/Phi_d)|_{T Z}, c_d >= 0 (Farkas, smooth point),
then for every admissible endpoint r''' the first-order pairing is sum_d c_d (psi_d(r''')/Phi_d - psi_d(r'')/Phi_d) <= sum_d c_d (1 - 3mu/4 -
psi_d(r'')/Phi_d): the certificate pairs positively ONLY with displacements that raise near-threshold statuses.  So the residual (T)-block
configuration is exactly: the certificate wants some near-threshold ACTIVE carriers d (those with c_d > 0) to move OUTWARD, toward the
threshold -- the same mechanism as (M2) for movable rows.  The analogous reading holds in (KN)-blocks with the KN-lever margins in place
of mu.  [This identifies the obstruction; it does not remove it.  Removing it would need near-threshold actives to cross the threshold,
i.e. a change of the pattern (an active weak peak with peak data in a shifted block), not covered by the chain.]
