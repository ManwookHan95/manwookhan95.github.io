# G2 part 3: persistence of (R1) -- (W4'') re-check, obstruction decomposition, margin levers, and why counting cannot work

Notation of Parts 1-2.  rc := (val_l/kappa_{m(l)})_l the realized ratios of the start row R_1 + P (unpushed prepared row with (FC)),
rt_0 the admissible targets, rho_0^max := max_{Delta in D_{h_max}} rho_0(rt_0 + Delta) <= x/4.  Design facts used (Part III Definition
III-QCreq (QC4) and K2 (L-K2-1)): b(w) <= eta'(w), C_L beta(b)^{2/N_L} <= eta'/3, b enters later quantities only through upper bounds
(so b(w) may be lowered freely); W = Des^{C_A} u^{-3} max(x, ||b(rt)||) >= Des^{C_A+1} u^{-3} eta', rho_0 = C_2 W^2; theta_0 = b/Des^{C_P};
s_1 = max(64 rho eps^viol/delta, exp(-1/(2T))).

## 3.1 The (W4'') re-check for (D-abs)

LEMMA 3.1.  PROVED (by inspection of the weight list Q1-refb 1.2 and cert3 3.4).  In the design variant (D-abs) (cluster absorber
targets supported in E^ch'(p) := T(p) ∪ (Z_0 ∩ [1, p]) instead of E^ch(p) = T(p) ∪ union_{l'' <= p}(S_{l''} ∩ [1, p]); Z_0 = coordinates
in no signature set): (a) the set of pairs (stage, coordinate s in S_{l'}) at which (W4'') imposes an upper bound on a cluster weight is a
SUBSET of the corresponding set for E^ch(p) (E^ch'(p) ∩ union_k S_k = T(p) ∩ union_k S_k ⊂ E^ch(p) ∩ union_k S_k, and Z_0 ∩ S_{l'} = {});
(b) allowedness (b) (= (W4)) for every absorber target, used by (T-b), (T-c), still holds, because every s in supp(absorber target) ∩
S_{l'} lies in T(p) and (W4'') is still imposed there; (c) no LOWER bound on a weight uses E^ch(p) (the lower-bound uses are cert3's
list W6 and P-R: eta_k >= mu_{p0}^2 c_k^2/2^13, which concern the absorber's least entry and the factor 1 - 2^{-l}, not its support).
Hence c^max_l under (D-abs) is >= its value under E^ch(p), every choice of weights admissible for T_fin^{K2} remains admissible, and the
generic-weight choice (QC1) is unaffected (it is an interval choice inside [(1 - 2^{-l}) c^max_l, c^max_l]).
Proof.  (a) Definition of (W4''): at cluster stages it bounds c^cl(p) for every s in E^ch(p) through the signature weights of the
carriers l' with s in S_{l'}; replacing E^ch(p) by E^ch'(p) removes the coordinates of union_{l''<=p}(S_{l''} ∩ [1, p]) \ T(p).  (b) H2
Lemma 2.2 (T(l) ∩ union S_k ⊂ [1, l]).  (c) cert3 3.4 and Q1-refb 1.2 (complete list of upper bounds; the lower-bound uses are W6 and
P-R).  QED
Consequence (with H2-ref B.10).  (D-abs) is a legitimate N-free, well-founded variant of T_fin^{K2} (route-V absorbers carry no switching,
X2-ref R-abs, and are off the MT VI tree, Q1-refa); its memory consequences hold: within a round range [r, s_max(p_r)) every kind-(iv)
carrier of an (R1) main stage is inactive at every later (R1) main stage of the range, switching signs do not flip, and every (up)/(down)
block of an (R1) stage is unshifted at every later (R1) stage of the range; so there are at most N (up)/(down) events per range.
[PROVED mod H2-ref B.10 and Lemma 3.1; the cluster stage p + 1 still pushes s_max(p+1) >= 4/T_lo(p, M(p)) because 1 in Z_0 ∩ [1, p].]

## 3.2 Capped generators

LEMMA CAP (cone realization with capped generators).  PROVED.  Let the Step-A generators be split into G_u (as in Definition III-Areg)
and G_c, each g in G_c carrying a capacity cap_g in (0, W/2] (a resource usable only up to cap_g, e.g. the downward part of a bank
above its downstream minimum, or a TU pair whose pull has depth v: cap = 2v).  Put R := {sum_{g in G_u} t_g g + sum_{g in G_c} t_g g :
0 <= t_g <= W/2 (G_u), 0 <= t_g <= cap_g (G_c)}.
 (a) If B(b, rho_0) ⊂ R, Step A is realized (with the conclusions of Lemma III-cone(c)).
 (b) Otherwise there is a unit y with  (W/2) sum_{G_u} (y^T g)_- + sum_{G_c} cap_g (y^T g)_- < phi_y + rho_0,  where s_- := max(-s, 0); in
     particular y is a near-certificate of size < 2(||b|| + rho_0)/W for G_u, phi_y > -rho_0, and (y^T g)_- < (phi_y + rho_0)/cap_g on G_c.
Proof.  (a) As Lemma III-cone(c): S(b') := argmin{||s||_2 : sum s_g g = b', 0 <= s_g <= cap_g} is a strictly convex parametric QP whose
feasible sets depend Hausdorff-continuously on b' in R (Hoffman's bound for the polytope), so S is continuous on R; T(t) := S(b - Rem(t))
maps the compact convex box into itself (||Rem|| <= rho_0); Brouwer; the frozen-status bookkeeping is unchanged.  (b) Separate b'' in
B(b, rho_0) \ R from the compact convex R: y^T b'' < min_R y^T sigma = -sum_g cap_g (y^T g)_-; and -y^T b'' <= -y^T b + rho_0 = phi_y + rho_0.  QED

LEMMA MS^cap.  PROVED (mod chain).  In Lemma MS replace Phi by Phi^cap(Delta, y) := <kappa y, Delta> - phi_y(rt_0) + sum_{g in G_c}
cap_g (y^T g)_-.  Phi^cap is affine in Delta and convex in y; Sion's minimax theorem gives the same dichotomy: either a displacement Delta*
realizes Step A (with capped generators), or there is z* in conv(Y) with
      max_{Delta in D_h} <kappa z*, Delta> - phi_{z*}(rt_0) + sum_{G_c} cap_g (z*^T g)_-  <  rho_0^max ,                      (3.1)
so in particular  sum_{G_c} cap_g (z*^T g)_- < phi_{z*}(rt_0) + rho_0^max  and (1.1), (1.3) hold with c_MS replaced by
c_MS^cap := (||b|| + rho_0^max)/h_max.
Proof.  Lemma CAP(b) replaces Lemma III-cone(b) in the proof of Lemma MS(a); (y -> (y^T g)_-) is convex, so Phi^cap is convex in y and
min over conv(Y) of max over D_h equals max over D_h of min over conv(Y) (Sion); the minimum of the convex function y -> Phi^cap(Delta, y)
over conv(Y) need not be attained on Y, which is why the conclusion is stated for z* in conv(Y).  The remaining steps are those of
Lemma MS.  QED

## 3.3 The obstruction decomposition and multiplier vanishing

LEMMA OD (obstruction decomposition).  PROVED (mod chain).  For z* as in Lemma MS(b) (or MS^cap), with lambda, nu, mu of Theorem JF:
      phi_{z*}(rt_0) = S_prot + S_res,aff + S_res,naff + O(c_MS ||rt_0 - rc||_rt),
 S_prot := -sum_{d in N} lambda_d l_d(rt_0 - rc)   (first-order change of the protected statuses from the start row to the targets,
           weighted by the status multipliers; >= 0 when the targets lower these statuses),
 S_res,aff := sum over affine groups G of sum_i mu_i P_i(rc)   (the tiny-polynomial values at the start row),
 S_res,naff := sum over non-affine groups G of <nu|_G, rc^G - rt_0^G>.
Proof.  phi_{z*}(rt_0) = sum_l z*_l (val_l - rt_{0,l} kappa_{m(l)}) = <kappa z*, rc - rt_0>; insert (1.3): kappa z* = A^T lambda + nu + err.
<A^T lambda, rc - rt_0> = -sum_d lambda_d l_d(rt_0 - rc) (l_d linear).  nu = 0 on MOV; on an affine G, nu|_G = sum_i mu_i grad_G P_i and
grad_G P_i . (rc^G - rt_0^G) = P_i(rc) - P_i(rt_0) = P_i(rc) (P_i affine, rt_0 in Z_kappa).  |<err, rc - rt_0>| <= c_MS ||rc - rt_0||_rt.  QED

LEMMA MV (multiplier vanishing).  PROVED (mod chain).  Let m be a block and Lambda_m := sum_{d in N ∩ m} lambda_d.
 (a) If m is a (U)-block with a private two-sided peak resource (every (U)-block at an (R1) stage, H2 Fact 1.1(d)), then
     sum_{d in N ∩ m} lambda_d (1 + 2 kappa'_m R^2_{(d)}) <= Des^C (eps + c_MS);  hence Lambda_m <= Des^C (eps + c_MS).
 (b) If m contains a movable row l with |rt_l| >= u Des^{-C_3}, seen by every protected status of m (l in Omega_{(d)} for all d in N ∩ m:
     automatic for route-V statuses; for Puiseux statuses of a (T)-block l must be active), and either |z*_l| <= e_3 := eps Des^2 + e_X
     (kind (i) rows; inactive rows whose private resources are two-sided) or l is a K^- kind-(iv) row (rt_l < 0, z*_l >= -e_1), then
     Lambda_m <= Des^C (e_1 + e_3 + c_MS)/u^2.
In both cases |S_prot restricted to m| <= Lambda_m max_d |l_d(rt_0 - rc)| <= Des^C (eps + e_1 + e_3 + c_MS) eta'/u^3, which is <= rho_0/Des
for the constants of Part 1 (eps <= eps_* = u^3 Des^{-C}, c_MS <= u^4 Des^{-C_h}, and rho_0 >= C_2 Des^{2C_A+2} u^{-6} eta'^2 is NOT used:
we compare with x: Des^C (eps + c_MS) eta'/u^3 << x/Des).
Proof.  (a) In a (U)-block rt^{(m)} is in V (Lemma 2.1(d)), so <nu, rt^{(m)}> = 0; pairing (1.3) with rt^{(m)}: kappa_m zeta_m(z*) -
sum_d lambda_d l_d(rt^{(m)}) = <err, rt^{(m)}> with |.| <= c_MS ||rt^{(m)}||_{rbar,inf}... <= c_MS |Lambda_A|; l_d(rt^{(m)}) = 1 + 2 kappa'_m
R^2_{(d)} for d in m and 0 for d in other blocks; |zeta_m(z*)| <= (4/3) eps Design (R-PK, Lemma 1.1(d)).  (b) (JF1) at l: kappa_m z*_l -
lambda_l 1[l in N]/rt_l - 2 kappa'_m m^2 rt_l Lambda^{(l)}_m = O(c_MS/rbar_l), and Lambda^{(l)}_m = Lambda_m by the hypothesis.  For |z*_l| <=
e_3: the two multiplier terms have the common sign sgn(rt_l), so each is <= kappa_m e_3 + c_MS/rbar_l; kappa'_m >= c_K/8.5, |rt_l| >= u
Des^{-C_3}.  For a K^- row (rt_l < 0): both multiplier terms are <= 0 (lambda >= 0, Lambda >= 0), so lambda_l 1[l in N]/|rt_l| + 2 kappa' m^2
|rt_l| Lambda_m = -kappa_m z*_l + O(c_MS/rbar_l) <= kappa_m e_1 + c_MS/rbar_l (z*_l >= -e_1).  The bound on S_prot:
|l_d(rt_0 - rc)| <= ||rt_0 - rc||_rt (1 + 2 kappa' R^2) <= Des^C eta'/u (targets within eta' of the start, |rc| >= u Des^{-C})... QED

## 3.4 Margin levers

DEFINITION 3.2 (margin lever).  A pinned kind-(iv) row l has a MARGIN LEVER of capacity cap_l if S_l contains a pullable coordinate j
(K1 2.0: a data-sign contact or near-contact of the companion, pull capacity (1 + eps_l z(j)) v_l(j) >= v_l(j)) with v_l(j) in
[cap_l/2, c_0 W]; the lever is the TU pair (pull of mass 24 lambda_l v_l(j) of sign -eps_l at j, pre-placed, plus a compensating base bank
at a near S_th coordinate of l), which lowers val_l by 2 v_l(j) - O(C_T v^2) and is compensated continuously by the bank: a capped
generator g_l^- with column -eff_l e_l + O(mu_s^2 theta_0 + v^2) and capacity >= v_l(j) (V1 Lemma TU, K1 2.1(b)).  Cost <= C Des v log(1/v);
cushions, violations and the window bookkeeping are those of K1's pulls (P-RANGE; the depth is below the Step-A pull range).

THEOREM ML (margin levers kill the resonance part of (R1)).  PROVED (mod chain).  Put
      cap_min := Des^{C_m} (eta' Des^{-C_A + C} + c_MS eta' Des^C/u + rho_0^max + beta(b))/eff_min   (<= eta' Des^{-C_A/2} for C_A, C_h large).
At an (R1) stage assume:
 (i) every pinned kind-(iv) row l has a margin lever with cap_l >= cap_min;
 (ii) every pinned group is affine (Definition 1.2) with robust nonzero minors (>= u/2) at the targets (the targets rt_0 are any admissible
      targets on Z_kappa, e.g. those of KN^tr Steps 1-3; |rt_0 - rc| <= eta' in ratio units);
 (iii) every protected block satisfies a hypothesis of Lemma MV, or its protected statuses are not lowered from the start to the targets
      (l_d(rt_0 - rc) >= 0 for d in N ∩ m);
 (iv) no locked row (Definition 2.2).
Then Step A is realized.
Proof.  Lemma MS^cap with G_c := the margin levers; suppose (3.1) holds for some z*.  Since 0 is in D_h, (3.1) gives
sum_l cap_l (z*^T g_l^-)_- < phi_{z*}(rt_0) + rho_0^max, and (z*^T g_l^-)_- >= eff_l (z*_l)_+ - O((mu_s^2 theta_0 + v^2)|z*|).  Lemma OD (an exact decomposition for ANY targets on Z_kappa: the
tangential part of rt_0 - rc pairs to zero with the normal part of kappa z*):
S_res,naff = 0 by (ii); |S_res,aff| <= sum_i |mu_i| |P_i(rc)| <= Des^C u^{-C} beta(b) (start values of tiny polynomials <= beta(b), Part III
(QC4); |mu| <= Des^C u^{-C} by V2 Lemma H for robust minors); |S_prot| <= Des^C (eps + e_1 + e_3 + c_MS) eta'/u^3 by (iii) and Lemma MV
(or S_prot <= 0 in blocks whose statuses are not lowered), with eps <= 4 u^3 Des^{-C_A} (Lemma III-cone(b)); the error term is <= c_MS
Des^C eta'/u.  Hence phi_{z*} + rho_0^max <= cap_min eff_min Des^{-C_m} and (z*_l)_+ <= Des^{-C_m} on every pinned kind-(iv) row.  With
z*_l >= -e_1, |z*_l| is small there; Theorem H2.A''s bounds give the same on every free kind-(iv) row ((iv) excludes locked rows); so
sum_{(iv)} z*_l < c_1/4 for C_m large, contradicting H2 Proposition 3.1(a) for z* (Lemma 1.1(d)).  QED
REMARK 3.3.  The obstruction of a pinned kind-(iv) group in Step A is driven by the one-sidedness of its rows at the scale of the
realization's errors (second-order margin rho_0, the dual error c_MS eta', the status descent S_prot), not by the size of the resonance:
once the pinned rows have a downward resource of capacity cap_min (a design-small multiple of eta'), every one-signed resonance of
start-row value <= beta(b) is harmless.  The margin lever needs a pullable coordinate of S_l at depths v in [cap_min/2, c_0 W], i.e.
roughly v in [eta' Des^{-C_A/2}, eta' Des^{C_A}/u^3]: an interval of design length just BELOW the Step-A pull range [c_0 W, x''_max] that
defines kind (iv) (in coordinates: j = 4 log_2(1/T) +- O(log Des)), and far shallower than the Sys-DC scale r of H2 5.3.

## 3.5 Exact resonances and the failure of counting

PROPOSITION EX (exact one-signed resonances obstruct A-regularity).  PROVED (restricted linear model).  Let m be a (U)-block with a
private two-sided peak resource and G an internal affine pinned group of m with pinned kind-(iv) rows P and kind-(i) rows Q, whose
tiny minors M_i(r) = sum_l C_{il} r_l (homogeneous linear in r^{(m)}, X1 2.1) vanish EXACTLY at the start: M(rc) = 0.  Suppose mu is a
one-signed form: (mu^T C')_l >= 0 on the oriented rows of P, not all zero, and (mu^T C')_Q = 0, and suppose every generator acting on the
rows of G acts there by a vector of span{e_l (l in P), +-e_l (l in Q), +-rt^G} ⊕ (C'^T mu)^perp with the e_l (l in P) in the allowed
(upward) direction only and no capped downward resource.  Then for EVERY admissible target vector rt' with rt'^G in Z_G, Step A is not
A-regular at rt'.
Proof.  y := C'^T mu/||C'^T mu|| on G, 0 elsewhere.  y^T e_l >= 0 (l in P), y^T e_l = 0 (l in Q), y^T rt^G = (mu^T M(rt))/||.|| = 0 for
rt in Z_G (homogeneity), and y annihilates (C'^T mu)^perp: y^T g >= 0 for every generator, so y is a near-certificate of size 0.  phi_y(rt')
= <kappa y, rc - rt'> = kappa_m mu^T(M(rc) - M(rt'))/||.|| = 0.  Then b'' := b(rt') - rho_0 y is in B(b, rho_0) and y^T b'' = -phi_y - rho_0 =
-rho_0 < 0 <= min_{(W/2)Q} y^T sigma, so B(b, rho_0) is not contained in (W/2)Q.  QED
Remark (what the hypothesis costs in the real system).  The hypothesis on the generators is restrictive: a TS generator at a thick
design-depth coordinate s acts on y by eff_s(Psi_y(s) - kappa_y a_s) (Theorem III-Aobs (2), (4)), and FR/ZD generators by eff_s Psi_y(s).
So y = C'^T mu/||.|| is a near-certificate of the real system only if the base vector satisfies the normal form a_s = Psi_y(s)/kappa_y +
O(eps Des) at every thick s <= dbar(L) and Psi_y vanishes at every free/ZD design-depth coordinate; kappa_y <= -c_* holds automatically
(the S_th coordinates of P carry c_s(Psi_y) >= 0 and the identity of Theorem III-Aobs(1) applies).  These are further coincidences of the
stage data, all already part of the residual description (Theorem JF (JF4), Theorem III-Aobs).  Proposition EX shows that, GRANTED them,
the size of the resonance value plays no role.
COROLLARY EX (counting cannot exclude (R1)).  PROVED (as a statement about the method).  (a) An exact resonance P(r(f)) = 0 is TINY at every
sub-window (|P| <= b(w) for all w), so no pigeonhole over sub-windows or classes based on the tiny/robust dichotomy of rate objects can
remove it; by Proposition EX it obstructs A-regularity at every clean sub-window where its kind-(iv) rows are pinned and have no capped
downward resource; and the preparation bias of H2 Lemma 5.2 is not needed for this.  (b) In the model of Proposition EX a resonance of the WRONG sign obstructs at every sub-window where it is tiny, whatever its size,
and one of the right sign obstructs while its value is below rho_0 ||C'^T mu||/kappa_m; tiny at w means <= b(w), and every sub-window
coarser than the one the value spoils has a larger b.  So the same resonance object obstructs ALL coarser sub-windows: the "fresh
resonance per sub-window" count suggested in the task does not hold.  (c) What memory gives (Lemma 3.1 and H2 Lemmas 2.6, 2.7)
is the stage-to-stage freshness of the CARRIERS, not of the resonance values: persistent (R1) needs, at every (R1) main stage of a round
range except at most N, a one-signed (possibly exact) resonance among kind-(iv) carriers that were not kind (iv) at the earlier (R1) stages
of the range.  Nothing bounds the supply of such carriers (one new coarse carrier per block and level).  So the counting/pigeonhole route
to excluding (R1) is FALSE as a proof strategy; the obstruction must be removed by a resource (Theorem ML) or a different realization.
Proof.  (a) |0| <= b(w).  (b) Proposition EX's proof works with M(rc) of the wrong sign of any size, and with the right sign of size <
rho_0 ||.||/kappa_m (H2-ref B.9 with margin); tiny means <= b(w), and every sub-window coarser than the spoiled one has a larger b.
(c) H2 Lemma 2.7(b) and Lemma 3.1: deactivation concerns carriers; tiny minors of later stages involve the new active carriers.  QED

## 3.6 The persistent (R1) residual (precise)

THEOREM R1-P (necessary condition for persistence).  PROVED (mod chain; (D-abs) mod H2-ref B.10 and Lemma 3.1).  Design T_fin^{K2} with
(FC), P-TU, F-2, (D-enum) and (D-abs), and (no further condition on b(w) is needed).  Let (f, g, rho)
be such that at all main stages L >= L_0 every clean sub-window and class is an (R1) stage and Step A is not realized.  Then in every
round range [r, s_max(p_r)), at every (R1) main stage outside at most N exceptional ones (the (up)/(down) events), at every clean
sub-window and class, some block m satisfies one of:
 (P-res) m contains a pinned kind-(iv) row WITHOUT a margin lever (no pullable coordinate of S_l at depths v in [cap_min/2, c_0 W]) in an
         affine pinned group, and the joint residual of Theorem JF holds with a one-signed form (Corollary JF') and the normal form of
         Theorem III-Aobs (4) -- the carrier being fresh in the range;
 (P-naff) m contains a pinned kind-(iv) row in a NON-affine pinned group ((X4^0)-minors, cofactor polynomials, multilinear multi-block
         minors in a shifted block);
 (P-prot) m is a SHIFTED block (Lemma MV(a) excludes (U)-blocks) without a movable kind-(i)/two-sided-inactive/K^- row of robust ratio
         seen by all its protected statuses, and some protected status of m is lowered from the start row to the targets (a near-threshold
         carrier needing descent);
 (P-lock) m is a protected shifted block of type (two) (two-sided peak resource from a pullable robust peak) with a locked K^+ row.
Proof.  Theorem H2.A' and Theorem ML (contrapositive): if none of (P-res), (P-naff), (P-prot), (P-lock) occurs at some clean sub-window and
class, then (i)-(iv) of Theorem ML hold there [(ii): non-(P-naff) and the robust/zero dichotomy of minors at the targets (V2 Theorem B);
(iii): non-(P-prot) and Lemma MV(a) for (U)-blocks], and Step A is realized.  (up)/(down)
events: at most N per range (Lemma 3.1); outside them every block with a locked row is a protected shifted (two)-block.  QED
Remarks.  (1) In (P-res) the base vector satisfies the normal form a|_{thick} = Psi_{z*}/kappa_{z*} + O(eps Des) at every thick design-depth
coordinate (Theorem III-Aobs (4), linear, so valid for z*); inactive carriers are kind (i) (zero data, ZD near coordinates) and contribute
O(eps Des^2), so at a FIXED thick coordinate s (|a_s| fixed, s in T(L) for all large L) the fresh active kind-(iv) carriers and the peaks
of every large stage must reproduce kappa_{z*} a_s: the targets of fresh carriers keep meeting s.  This is compatible with (D-enum) and the
density of the pool, so it gives no contradiction.  (2) (P-res) at all stages requires, at every main stage, fresh pinned kind-(iv)
carriers whose signature sets are anti-sign (or non-pullable) at all depths v in [cap_min/2, x''_max]; by H2 Lemma 2.3 these coordinates
(j <= 5 log_2(1/T) + O(log Des)) are super-thin at the next (R1) stage, which constrains only the OLD carriers.  (3) Nothing proved here excludes (P-res),
(P-naff), (P-prot) or (P-lock) at all large stages.  (R1) persistence: OPEN; the remaining step is a downward resource of capacity >> rho_0
for deep-swallowed pinned kind-(iv) carriers (or a realization of exactly resonant one-signed groups that does not need the margin
rho_0), plus the classes (P-naff), (P-prot), (P-lock).
