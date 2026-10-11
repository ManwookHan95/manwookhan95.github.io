# G2 referee notes (Round 14): proofs of the verdicts and of the fixes for r14/G2_notes.md
# (minimax over the certificate hull, joint Farkas form, coupled directions, margin levers, (R0)/(R1) residuals)

Refereed: r14/G2_notes.md (+ G2_part0..4.md, G2_work/).  Checked against: Part III 5.6 (Definition III-SysA, Lemma III-Euler, Definition
III-Areg, Lemma III-cone, Theorem III-Aobs, Corollary III-Asuff, Definition III-resources, Lemma III-K and the block-scalar formula of 2.1),
r13 H1_ref_notes (Lemma SLP, PC, MA', C.6, E), H2_notes 1-4 and H2_ref_notes (P-RANGE, P-31, P-41, F-NE, B.10), r12 J2_ref_notes C.1 (Q-KN),
r11 cert0 3.2, Q1_refb 1.2.  Setting and notation: G2_notes 1.  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN; "PROVED (mod chain)" =
modulo the refereed chain cited by J1.15', J2.1, H1-ref, H2-ref (several links once-refereed).  Part files: r14/G2_ref_part1-3.md.
Scripts and outputs: r14/G2_ref_work/.  This file supersedes the part files where they differ.

## A. Verdicts
| G2 claim (G2 label) | Verdict | Items |
|---|---|---|
| Lemma 1.1, Lemma 1.3, Lemma MS (PROVED mod chain) | correct | B.1; precisions P-LIN, P-EPS, P-WMAX, P-14 |
| Theorem JF, Corollary JF' (PROVED mod chain) | correct | B.2; P-JF1, P-41i |
| Lemma NP' (PROVED mod chain) | correct, residual conclusion incomplete | P-NP'1 (no-peak-lever case), P-NP'2 (sign), P-NP'3 |
| Remark 1.8, P-KN (PROVED mod chain) | correct under the pre-move convention | B.3 |
| Lemma 3.1', Lemma 3.2 (PROVED) | correct; one misstatement | P-32 ("every hull element" false; true for z*) |
| Theorem H2.A', Theorem R1-J (PROVED mod chain) | correct | B.4 |
| Lemma 4.1 ((W4'') re-check) (PROVED, inspection) | correct | B.5 |
| Lemma 4.2 CAP (PROVED) | fixable gap | G-CAP (box capacities break the Brouwer remainder bound) |
| Lemma 4.3 MS^cap, Lemma 4.4 OD, Lemma 4.5 MV (PROVED mod chain) | correct (4.3 after G-CAP) | B.6 |
| Theorem ML (PROVED mod chain + (K1-depth)) | WRONG AS STATED (false proof step); repaired; replaced by ML' | G-MU (numerics R1), G-LAM, G-NAFF; C.6, C.7 |
| Proposition 4.7, Corollary 4.8 | correct (restricted model; statements about the method) | B.7 |
| Theorem 4.9 (PROVED as necessary condition) | residual list too narrow as stated; corrected (Theorem 4.9') | C.8 |
| Lemma 5.1, Theorem 5.2 (PROVED mod chain) | correct with precisions | B.8; P-NP'1, P-NL |
| Lemma 5.3 NL (PROVED) | correct as stated; scope remark overclaims | P-NL |
| Proposition 5.4 (PROVED mod chain) | correct | B.8 |
| Lemma 5.5 (PROVED mod J2.1) | conclusion correct, mechanism wrong in one detail | P-55 (numerics R2) |
| Peak conversion of anti-aligned near-threshold rows (SKETCH) | label honest | G1, G2 OPEN |
| (R0)/(R1) at all large stages; (LSC-trunc)_N every f; density for p_N, p (OPEN) | OPEN | E |

## B. Re-derivations (claims found correct)
B.1 Lemma MS.  Phi(Delta, y) = <kappa y, Delta> - phi_y(rt_0) is linear in Delta and affine in y; D_{h_max} is a compact convex polytope
and conv(Y) is compact convex; von Neumann/Sion gives max_D min_{conv Y} = min_{conv Y} max_D, and the inner minimum of an affine function
over conv(Y) is attained on Y.  (a): Lemma III-cone(b) at rt' gives a near-certificate of size < 4u^3 Des^{-C_A}; generator columns
g = eps_l l_delta(u_l) - rt_l l_delta(K_m) (Lemma III-Euler(b)) are affine in rt with slope <= Des^C, so it is a near-certificate at rt_0 of
size < 4u^3 Des^{-C_A} + Des^C h_max, i.e. in Y; phi_y(rt') = phi_y(rt_0) - <kappa y, Delta*> = -Phi(Delta*, y) <= -rho_0^max: contradiction.
(b): Delta = 0 gives phi_{z*} > -rho_0^max; |phi_{z*}| <= ||z*||_2 ||b(rt_0)||_2 <= ||b(rt_0)||.  (c): LP duality for max{c^T Delta : Delta in V,
A Delta <= 0, |Delta_l| <= rbar_l}; the subspace constraint has multiplier nu in V^perp and the box has conjugate sum rbar_l |.|; dual attained.
Theorem III-Aobs (3) (gamma <= -c_*) holds for EVERY near-certificate of size <= eps_* (its proof uses (1), which needs only |phi_y| <=
|Lambda_A|^{1/2} max(x, ||b||)), so conv(Y) avoids 0.  Lemma 1.3: re-derived (statuses: log rho_d = log(m|r_d|/Phi_d) + log K(sigma, R^2),
first variation l_d <= 0, second derivatives <= Des^C; Des^C h_max^2 <= Des^C u^{-8} eta'^2 << eta'/Des).
B.2 Theorem JF.  V = span(MOV) ⊕ (⊕ V_G) is a direct sum over disjoint coordinate sets (every row is movable or pinned; holds and pushed rows
are movable).  nu vanishes on MOV; nu|_G in V_G^perp = row space of the Jacobian (tangent-space groups) or the orthogonal complement of the
piece vectors (piece-scaling groups); pairing (2.2) with a piece vector uses |rt_{0,l}| <= rbar_l.  Piece vectors of (U)-blocks lie in every
V_G (Euler's identity for P homogeneous in r^{(m)}, H1-ref Lemma PC), so rt^{(m)} is in V for every (U)-block.  Corollary JF' is (JF2) read with
z*_l >= -e_1 (kind (iv)) and |z*_l| <= eps Des^2 + e_X (kind (i)).
B.3 Remark 1.8.  cert0 3.2: the KN pushes s_0 = C D eta' theta Phi_P^2/(rho_{d0} M) are one-shot pre-moves; J2-ref C.1 (Q-KN): then the active
weak peaks are strict non-peaks at f_1 + Pi and (FC) is consistent.  Lemma-MS displacements keep protected statuses at first order (l_d <= 0)
and move them by <= Des^C h_max^2 << c D eta' at second order; d_0 is in N and moves inward only.
B.4 Theorem H2.A'.  Free K^-: rbar_l e_l (inward = oriented up) is in D_1 (Lemma 3.1'(a)), so kappa_m z*_l rbar_l < c_MS; z*_l >= -e_1.  Free K^+
in (U)-blocks: v_l = sgn(rt_l) e_l - c_l rt^{(m)} with c_l = 1[l in N]/|rt_l| + 2 kappa'_max m^2 |rt_l| (l_d(rt^{(m)}) = 1 + 2 kappa'_(d) R^2_(d) >= 1
gives l_d(v_l) <= 0), ||v_l||_rt <= Des^C/u, plus R-PK for z*.  Partners: Lemma 3.1'(c) re-derived (d not in {l, p}: partner condition and
c_lp|rt_p| >= |rt_l|; d = l: exact cancellation with the kappa' of l's own status; d = p: both terms <= 0).  The case analysis of H2.A uses only
(1.2), Proposition 3.1(a)-(c) (linear, inherited by z*) and these per-row bounds.  Theorem R1-J is Theorem JF read at an (R1) stage.
B.5 Lemma 4.1.  Q1-refb 1.2 lists every upper bound on the weights; (W4'') is the only one indexed by E^ch(p), and E^ch'(p) ∩ union_k S_k =
T(p) ∩ union_k S_k (Z_0 meets no signature set), so the constraint set shrinks; allowedness (b) for absorber targets holds because their
signature coordinates lie in T(p) (H2 Lemma 2.2); the lower-bound uses (W6, P-R) do not involve the support.  1 is in Z_0 ∩ [1, p], so the
cluster stage p+1 and s_max(p+1) >= 4/T_lo(p, M(p)) persist.  Legitimacy of (D-abs) beyond the weights rests, as in H2-ref B.10, on route-V
absorbers carrying no switching (X2-ref R-abs) and entering only as fine carriers through their weight (K1.S).
B.6 Lemmas 4.3-4.5.  MS^cap: Phi^cap is convex in y and linear in Delta (Sion); the minimizing z* lies in conv(Y) (need not lie in Y).  OD is the
identity phi_{z*}(rt_0) = <kappa z*, rc - rt_0> with (2.2) inserted (grad P_i . (rc - rt_0) = P_i(rc) for affine P_i, rt_0 in Z_kappa).  MV(a):
pair (2.2) with rt^{(m)} in V: kappa_m zeta_m(z*) - sum_{d in N ∩ m} lambda_d (1 + 2 kappa'_(d) R^2_(d)) = O(c_MS), |zeta_m(z*)| <= (4/3) eps Des
(R-PK, linear).  MV(b): (JF1) at l; both multiplier terms have the sign of rt_l.
B.7 Proposition 4.7.  y := C'^T mu/||C'^T mu|| on G: y^T e_l >= 0 on P, = 0 on Q, y^T rt^G = mu^T M(rt)/||.|| = 0 on Z_G (homogeneous linear
minors), y annihilates (C'^T mu)^perp; phi_y(rt') = kappa_m mu^T(M(rc) - M(rt'))/||.|| = 0 for EVERY rt' in Z_G; b'' = b(rt') - rho_0 y separates.
It obstructs A-REGULARITY (the ball condition), not necessarily every realization (second-order terms are not modelled).  ("span{e_l (l in P,
upward only)}" should read "the cone generated by".)  Corollary 4.8 is a correct statement about the counting route in that model.
B.8 Lemma 5.1, Theorem 5.2, Proposition 5.4.  5.1 = Lemma AL averaged; |z_l rt_l| >= (c_*/nu_1)(u/2)|rt_l| and |rt_l| >= u Phi_l/(mK).  5.2(a):
MV(a), (JF1)*rt_l against 5.1 (Des(L) dominates 1/Phi_l for l <= L, eps_* = u^3 Des^{-C} with C large); pieces by pairing with piece vectors.
5.2(b): pairing with rt^{(m)}; movable rows of robust ratio have kappa_m z*_l rt_l >= 2 kappa' m^2 rt_l^2 Lambda_m - O(c_MS) > 0, which excludes
kind (i) and K^- rows.  5.2(c): an aligned movable thick row pairs with the inward direction by kappa_m |z*_l rt_l| rbar_l/|rt_l| >> c_MS.
(JF2) in 5.2(d) needs no bound on mu.

## C. Findings and fixes (with proofs)
C.1 P-LIN (Lemma 1.1(d)).  Items (2a), (2c) of Theorem III-Aobs carry |kappa_Psi| on the right; averaging is legitimate because kappa_y < 0 for
every y in Y, so sum theta_i |kappa_{y_i}| = |kappa_z|.  Sign statements (Lemma NP(b)) average because the sign is common.
C.2 P-EPS, P-WMAX (Lemma MS(a)).  Take eps_1 := 8u^3 Des^{-C_A} (<= eps_* if C_A >= C_* + 3): it contains every transported certificate and is the
size used in Theorem ML.  Whether a pre-placed TU lever is two-sided (capacity >= W/2; H2 (U'), H2-ref P-RANGE) depends on W = W(rt), which
varies by a factor <= Des^C u^{-4} over rt_0 + D_{h_max}; fix ONE threshold W_max := max over that set, so the generator SET is the same at rt_0
and rt' and only the columns move (Lipschitz).  Both are bookkeeping; no conclusion changes.
C.3 P-JF1.  (a_d)_l = 1[l = d]/rt_{0,d} + 2 kappa'_(d) m^2 rt_{0,l} 1[l in Omega_(d)]; with Puiseux statuses kappa'_(d) differs from the route-V value,
so Lambda^{(l)}_m must be sum_d (kappa'_(d)/kappa'_m) lambda_d.  P-41i: multi-block pinned groups are bilinear (a minor meeting two blocks
contains two (X3) rows), hence non-affine; "(JF2) also multi-block" is essentially vacuous and such groups fall under (JF3)/Lemma NL --
G2's Remark 2.3 says so, the summary "P-41 (i) removed" overstates.  P-14: Remark 1.4(iii) "not realized by any of these levers either"
overclaims for band levers and Brouwer-coupled rescalings (not fixed displacements); H2.A's conclusion is recovered by H2.A'.
C.4 P-32 (Lemma 3.2).  The inequality kappa_m(z_l - c_lp sgn(rt_p) z_p) <= Des^C u^{-3} c_MS is (1.1) for v_lp/||v_lp||_rt in D_1 and holds for the
MINIMAX element z* of Lemma MS(b) only; a general hull element need not pair below c_MS with D_1.  Its use (for z*) is correct.
C.5 G-CAP (Lemma 4.2).  With R a box (each uncapped generator up to W/2), a representation t of a point of R can have ||t||_2 = (W/2)|G|^{1/2},
|G| up to Des^C; the remainder bound ||Rem(t)|| <= C_2 ||t||^2 then gives only C_2 W^2 |G|/4 > rho_0 = C_2 W^2, so T(t) = S(b - Rem(t)) need not be
defined on the Brouwer domain.  FIX (PROVED): R := (W/2) conv(G_u ∪ {0}) + {sum_{G_c} t_g g : 0 <= t_g <= cap_g} with sum_{G_c} cap_g <= W/2 (cap
each margin lever at W/(4|Lambda_A|), which keeps every capacity used below >= cap_min).  Every point of R has a representation with ||t||_1 <=
W, so ||Rem|| <= rho_0 on the domain {t : ||t||_1 <= W}; the min-norm selection is continuous (polyhedral multifunction); Brouwer as in Lemma
III-cone(c).  Separation of b'' in B(b, rho_0) \ R: y^T b'' < (W/2) min(0, min_{G_u} y^T g) - sum_{G_c} cap_g (y^T g)_-, i.e. (b) reads
(W/2) max_{G_u}(y^T g)_- + sum_{G_c} cap_g (y^T g)_- < phi_y + rho_0.  MS^cap is unchanged (only G_c enters Phi^cap).
C.6 G-MU, G-LAM, G-NAFF (Theorem ML, refined form).  The proof needs |S_res,aff| <= |mu| beta(b) with |mu| <= Des^C/u.  (i) G-MU: mu solves
J^T mu = (kappa z* - A^T lambda)|_G - err; its size is ~ ||rhs||/s_J, s_J the smallest NONZERO singular value of the tiny-polynomial Jacobian
J of the group.  J's minors are not rate objects of the design (entries are cofactors; their 2x2 minors are not minors of Gamma^#), so s_J can be
tiny-but-nonzero or intermediate at a clean sub-window, and for affine groups J does not depend on the group's ratios (no target choice can
exactify it).  COUNTEREXAMPLE to the proof step (restricted model, numerics R1): one (U)-block, three pinned kind-(iv) rows, two tiny homogeneous
minors J = [[1,1,1],[1,1+s,1-s]] (every cofactor robust, every 2x2 minor O(s)), P(rc) = (0, beta), full target freedom on Z = ker J, capped
downward levers: the minimal capacity is c_need = 3.33 beta/s (s = 1e-1, ..., 1e-4: c_need/beta = 3.3, 33, 333, 3333), with the one-signed
form mu = (2 - 1/s, 1/s) (mu^T J = (2,3,1) >= 0, mu^T P(rc) = beta/s) giving the certificate lower bound 1.67 beta/s; with a robust J, c_need =
0.5 beta.  All hypotheses (S), (G), (B) of the notes' Theorem ML hold there (no protected statuses; affine group; two-sided peak resource; all
kind-(iv) rows margin-levered), so the theorem AS STATED is not proved, and fails in this model for cap_min ~ C beta.  (ii) G-LAM: ||A^T lambda|_G||
is unbounded when Lambda_m is; MV bounds Lambda_m only in blocks whose statuses descend.  Lambda_m <= Des^C/u^2 when rt^{(m)} is in V or m has a
movable row of robust ratio seen by all its protected statuses (pair (2.2) with -rt^{(m)}, resp. with the inward direction: lambda_l/|rt_l| +
2 kappa' m^2 |rt_l| Lambda_m <= |kappa_m z*_l| + c_MS/rbar_l).  (iii) G-NAFF: S_naff of a non-affine kind-(i) group is <nu|_G, rc - rt_0> with
nu|_G = kappa z*|_G - A^T lambda|_G - err; z* small on kind (i) does not make it small unless Lambda_m is small.
REPAIRED THEOREM ML (PROVED mod chain, (K1-depth), C.5).  Replace (S), (G) by: (S+) Lambda_m <= Des^C (eps + e_1 + e_3 + c_MS)/u^2 (a hypothesis of
Lemma 4.5) in every protected block whose statuses are lowered from rc to rt_0 OR which contains a pinned group; (G+) every pinned group containing
a kind-(iv) row has V_G = tangent space and a robust Jacobian, s_J >= (u/Des)^{C_J} (full row rank for non-affine groups, Lemma NL); and add
Des^C beta(b)/(u s_J) to cap_min.  Proof: Lemma OD; S_prot <= Des^C(eps + e_1 + e_3 + c_MS) eta'/u^3 on blocks of (S+) and <= 0 on blocks whose
statuses are not lowered (no pinned group there, so they contribute no S_res); minimal-norm mu = (J J^T)^{-1} J(rhs) with ||rhs|| <= C + Lambda_m
Des^C/u + c_MS, so |S_res| <= ||mu|| ||P(rc)|| + Des^C|mu| ||rc - rt_0||^2 <= Des^C beta(b)/(u s_J) + small; S_naff (kind-(i) groups) <= ||nu|_G||
||rc - rt_0|| <= Des^C (e_3 + Lambda_m + c_MS) eta'; then (z*_l)_+ <= Des^{-C_m} on margin-levered rows and the case analysis of H2.A' as in G2.
C.7 REFEREE ADDITION: THEOREM ML' (crude margin levers).  PROVED (mod chain and C.5; no (S), no (G), no (K1-depth)).
Statement.  At an (R1) stage put cap'_min := Des^{C_m} max(x, ||b(rt_0)||) (value units; >= 2x).  Call a kind-(iv) row CONTROLLED if it is free and not
locked, or if S_l has a pullable coordinate j with v_l(j) in [cap'_min/2, x''_max] (pinned or locked rows alike; a kind-(iv) row may still have
such coordinates: (U') only says that their AGGREGATED capacity in [c_0 W, x''_max] is < 4W', and below c_0 W nothing is said).  If every block satisfies (B)
(two-sided lever: all K^- or all K^+ rows controlled; kappa-raising lever only: all K^- controlled; kappa-lowering only: all K^+ controlled),
Step A is realized.
Proof.  Pre-place, for every margin-levered row, the pull (mass 24 lambda_l v_l(j), sign -eps_l) with a compensating base bank at a near S_th
coordinate of l (bank mass m_l with eff_l m_l = D_p := (1 + eps_l z_1(j)) v_l(j) >= v_l(j), the pull's downward shift); decreasing the bank
is a capped generator g_l^- with column -eff_l e_l + O(mu_s^2 theta_0 + v^2) and capacity cap_l := min(m_l, W/(4|Lambda_A|)) in mass units, i.e.
eff_l cap_l >= min(v_l(j), W/(4 Des |Lambda_A|)) >= cap'_min/2 in value units (V1 Lemma TU, K1 2.1(b)); increasing it is the old one-sided
generator.  Apply MS^cap (with C.5).  If Step A is not realized, some z* in conv(Y) satisfies (3.1); taking Delta = 0,
   sum_l cap_l (z*^T g_l^-)_- < phi_{z*}(rt_0) + rho_0^max <= ||b(rt_0)|| + rho_0^max      (|phi_{z*}| <= ||z*||_2 ||b(rt_0)||_2, ||z*||_2 <= 1),
and (z*^T g_l^-)_- >= eff_l (z*_l)_+ - O((mu_s^2 theta_0 + v^2)|Lambda_A|^{1/2}); hence (z*_l)_+ <= 4 Des^{-C_m} + small on every margin-levered
row, and z*_l >= -e_1 (linear).  Free rows: the bounds of H2.A' (directions of D_1; no multiplier is used).  The per-block case analysis of H2.A'
with "controlled" as above gives |z*_l| <= c_1/(16|Lambda_A|) on every kind-(iv) row for C_m >= C_3 + C_4 + C, against Proposition 3.1(a) for
z*.  Range: cap'_min/2 >= x, so [cap'_min/2, x''_max] lies in the certified pre-placement range: Definition III-resources certifies pulls
at depths [x, x'_max] (costs, cushions, admissibility), K1-ref R-6 / H2-ref P-RANGE extend this to x''_max; only their CAPACITY was the reason
for J1-ref P-TU's restriction of two-sided TU levers to [x_TU, x'_max].  W/(4 Des |Lambda_A|) >= cap'_min/2 when C_A >= C_m + 4 (u <= 1,
|Lambda_A| <= Des), and sum_l cap_l <= W/4 keeps C.5's budget.  QED
Remarks.  (1) Pulls of capacity below W/4 are NOT full two-sided generators of the cone realization (J1-ref P-TU; this is why H2 needed
aggregated capacity >= 4W'); MS^cap shows they suffice as capped generators.  (2) G2's numerics N2(B) use capacity 4(rho_0 + max|b_P|) ~ ||b||:
they test ML', not the refined cap_min.  (3) The base bank theta_0 = b/Des^{C_P} (preparation) is too small to serve as a margin lever:
b <= (eta'/(3C_L))^{N_L/2} by (QC4).
C.8 THEOREM 4.9' (corrected persistent (R1) residual).  PROVED (mod chain, C.5; (D-abs) mod H2-ref B.10 + Lemma 4.1).  Under the hypotheses of
G2's Theorem 4.9, at every clean sub-window and class:
 (P-res') [from ML'] some block is residual in the sense of H2.A' with "uncontrolled" = pinned or locked and WITHOUT any pullable coordinate
          at depths [cap'_min/2, x''_max] (deep-swallowed over the whole certified range);
 and [from the repaired ML] (P-prot+) (a protected block with lowered statuses or containing a pinned group, violating (S+)) or (P-naff+)
          (a kind-(iv) row pinned in a group without a robust Jacobian -- AFFINE groups included -- or at a non-robust target of a non-affine
          group) or (P-res) with the longer range [cap_min/2, x''_max] (needs (K1-depth)).
 Moreover, outside at most N (up)/(down) events per round range, (P-res') is of type (two) and involves a FRESH deep-swallowed pinned K^-
 carrier.  G2's Theorem 4.9 as stated (with (P-prot), (P-naff) only for shifted blocks / non-affine singular groups) is NOT proved: its
 (P-naff) misses affine groups with a non-robust Jacobian and its (P-prot) misses blocks with large multipliers that contain pinned groups.
C.9 P-NP'1-3 (Lemma NP', Theorem 5.2(c)).  (1) The residual conclusion must read: no two-sided peak resource, and (sigma_m = sgn(Delta''_m)
or m has no one-sided peak lever) -- at (R0) stages all near coordinates of the robust peaks may be thick (no S_th lever).  (2) With
M_i = C^{(i)}_{Delta'} - sum_l r_l C^{(i)}_l: grad M_i . rt^{(m)} = -C^{(i)}_{Delta'} on Z, so sum_i mu_i C^{(i)}_{Delta'} = -(kappa_m zeta_m(z*) -
<A^T lambda, rt^{(m)}>) + O(c_MS) (sign).  (3) That reading needs all pinned groups of m affine (nu is free on non-affine groups of shifted blocks).
C.10 P-NL (Lemma 5.3 and its "Use").  The lemma is correct (Newton contraction re-derived: ||D Phi|| <= (9/8)(1/8) on the ball of radius
2||R_2||/s_J^2; ||E|| <= q^{1/2} Des^C s_max ||Delta||^2/s_J^2).  But: (a) full row rank fails at smooth points of non-complete-intersection
zero sets (minors of a rank-r matrix have dependent gradients), so "non-affine groups at SINGULAR targets" must read "targets where no
subsystem with a robust full-row-rank Jacobian has the same local zero set"; (b) "robust Jacobians can be made a rate object" is a design
change that is not carried out (rate-object count, Lojasiewicz exponent of the enlarged system, b(w), survival): SKETCH; (c) for affine groups J
is data-only (C.6).
C.11 P-55 (Lemma 5.5).  kappa(zeta; Omega) = (|zeta|(|zeta| + theta) - sum_{k in Omega} v_k^2 Phi_k^2)/theta (Part III 2.1); statuses rho_k = v_k/theta
are intrinsic.  The notes pass from (P_rob, Omega) to (P_rob ∪ {d}, Omega \ {d}); then kappa jumps by rho_d^2 theta Phi_d^2 = theta Phi_d^2 at
rho_d = 1 (a^2 = sigma + k^2 R^2 coincide but k = a + sigma does not), so every ratio of block m is rescaled by k/(k + Phi_d^2): harmless in
(U)-blocks (Lemma PC), but in SHIFTED blocks -- where Prop. 5.4 says conversion is needed -- the targets leave Z_kappa.  FIX (PROVED): keep d in
Omega and freeze only the threshold pattern (P_f = P_rob ∪ {d} in the threshold equation); Lemma K's sigma' = Phi_{P\Omega}^2 + sum_{Omega ∩ P}
(1 - rho^2)Phi^2 + s_Q is continuous at rho_d = 1, and at rho_d = 1 both frozen thresholds coincide (d contributes theta^2 Phi_d^2 = v_d^2
Phi_d^2), hence kappa, ratios and statuses coincide; the C^{1,1} bound |d Psi_f/d theta| >= 2 theta Phi_{P_rob}^2 is unchanged.  Numerics R2:
with Omega fixed kappa moves continuously (max step 6.0e-6, the grid), with Omega switched it jumps by 8.018e-4 = theta Phi_d^2 (predicted
8.016e-4); theta and the other statuses are continuous.
C.12 Part-1 Lemma 1.3(b) ("nearly neutral statuses stay <= 2b") is false: a hold moved by h rbar_l has status ~ Des^C h u >> b.  The notes'
version (inside Corollary 2.4's KN-1 band, quadratic status effect Des^C h_max^2 << eta'/Des) is correct.

## D. Numerics (sanity only; r14/G2_ref_work/)
 R1 r1_mu_gap.py (.out): G-MU model above; c_need/beta = 3.3, 33, 333, 3333 for s = 1e-1..1e-4 (= 3.33/s), certificate bound 1.67/s,
    dist(rc, Z) = 7.07 beta/s, robust J: 0.5.
 R2 r2_peak_conversion.py (.out): exact threshold equation sum Phi^2 (v - theta)_+ = (sum Phi^2 min(v, theta)^2)^{1/2} (KKT of the block norm),
    identity |zeta|^2 = theta^2 a^2 to 6e-17; kappa continuity with Omega fixed, jump theta Phi_d^2 with Omega switched.
 G2's N1-N3 re-read: N1 (true Lemma-K function) and N3 (generic minimax/LP duality) are consistent with the notes; N2 tests ML', not the
    refined cap_min (C.7 Remark (2)).

## E. Most valuable idea; what remains open
Most valuable idea.  The capped minimax (Lemma MS^cap) over the hull of near-certificates: one fixed target displacement plus capped
one-sided resources either realizes Step A or produces ONE vector z* carrying every linear certificate property.  With the trivial bound
|phi_{z*}| <= ||b(rt_0)|| it shows (Theorem ML') that a pinned or locked kind-(iv) row is harmless as soon as it has a pullable coordinate at
depth v in [Des^{C_m} max(x, ||b||), x''_max] -- possibly a pull too small to be a two-sided generator of the cone realization, but large
enough at the scale of the right-hand side -- whatever the resonance, the Jacobian or the status multipliers.
OPEN (precise).
 (R1) at all large main stages: (P-res') of Theorem 4.9': in every clean sub-window/class a block with uncontrolled rows -- pinned or locked
      kind-(iv) rows anti-sign-swallowed over the whole range [cap'_min/2, x''_max] (two-sided blocks: on both sides; one-sided blocks: on the
      lever-opposed side), fresh within each round range outside <= N events, together with the normal-form coincidences of Theorem III-Aobs (4)
      for the certificate.  Not excluded.  (Refined: (P-prot+), (P-naff+) or the longer swallowing range.)
 (R0) at all large main stages: Theorem 5.2's coincidence classes ((U)-pieces balanced, the sigma_m = +1 multiplier identity, anti-aligned
      proportional resonances, thick peaks with sigma_m = sgn(Delta''_m) OR no peak lever), non-affine groups without robust Jacobian (incl.
      non-complete-intersection points), (H-7), peak conversion gaps G1, G2.
 Inherited: once-refereed links; (K1-depth) only for the refined range; the J-minor rate-object design change (C.10(b)).
 (LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) for the Martin-type p: OPEN.  No
 counterexample is claimed by G2 or suggested here; the residual is a deep-swallowing pattern plus sign/coincidence conditions that a row must
 renew with fresh carriers at every main stage.
Suggested next steps.  (1) Look for capped downward resources of capacity ~ Des^C x that are not private pulls (shared pulls at target
coordinates; the downward part of TU levers of OTHER carriers acting through the common mode) -- ML' shows this capacity is all that is
needed.  (2) Test G3's persistent rows against ML': compute whether their pinned kind-(iv) carriers are swallowed on [cap'_min/2, x''_max].
(3) Make the Jacobian conditioning of tiny-polynomial systems a rate object (or stratify) so that (P-naff+) becomes a clean dichotomy.
