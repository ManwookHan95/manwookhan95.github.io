# H1 part 3: the alignment calculus -- inward relief, outward relief with exchange, group rescaling of pinned rows

Setting of part 2.  Lemma TF is used in the following ENDPOINT form (the proof of 2.1 uses only the endpoint):
LEMMA TF'.  PROVED.  If rt' is an admissible target vector (J1.13 (i)-(ii)), ||kappa (rt' - rt_0)|| <= Design^C (||b(rt_0)|| + x)/u (so that
|rt' - rt_0| C_G <= eps_*/2 and W(rt') <= Design^{C_A + C} u^{-4} (||b(rt_0)|| + x), the order of J1.9's bands; P-TU's x_TU is taken >= 24 W(rt')
as for J1's bands), and every near-certificate y of
size <= eps_* at rt_0 satisfies <kappa y, rt' - rt_0> >= 4(||b(rt_0)|| + x), then Step A is A-regular (hence realized) at rt'.
Proof: 2.1 with s_1 Delta := rt' - rt_0 (||b(rt')|| <= C Design^C (||b(rt_0)|| + x) because <kappa y, rt' - rt_0> <= ||kappa|| ||rt' - rt_0|| and
the displacement is chosen of the minimal size achieving the pairing, up to the factor Design^C allowed below).  QED

## 3.1 Definitions
 - For a thick-type coarse carrier l with thick private coordinate p: rho_l := a_p/v_l(p) (well defined up to the tiny spread of J1.6(a)).
   Its VALUE SIGN is vs_l := sgn u_l(xhat_1) (defined when |u_l(xhat_1)| is not nearly neutral).  l is ALIGNED if rho_l vs_l > 0 (its
   thick private coordinates contribute to u_l(xhat) with the sign of u_l(xhat)), ANTI-ALIGNED if rho_l vs_l < 0.  These are data of f
   (up to O(b) preprocessing), constant along the stages at which l is thick-type.
 - A Sys-A row l is MOVABLE if its target may be displaced without touching Z_kappa: l inactive (hold, D2/KN-pushed, KN-1), or l active
   with a FREE ratio (J1.13).  Its STATUS CLASS at f: nearly neutral (rho <= b), robust (u <= rho <= 1 - u), near-threshold (|rho - 1| <= b,
   including D2-pushed and KN-lever-pushed inactive carriers, and active weak peaks frozen as non-peaks by (FC)).
 - A block m is PROTECTED if it contains a row whose status must be kept below 1 with a margin <= Design^C eta' at the realized point:
   a near-threshold active, a D2-pushed or KN-pushed inactive near-threshold carrier.  (Robust statuses have room u; nearly neutral rows
   enter R^2 quadratically.)
 - For a row l with robust or near-threshold status put Q_l(y) := y_l/rt_l (ratio of certificate weight to target).

## 3.2 Lemma AL (needed direction).  PROVED.
For every near-certificate y of size eps <= eps_* and every thick-type row l with robust or near-threshold status,
      y_l rt_l = kappa_y rho_l u_l(xhat_1)/kappa_m + O(eps Design^2 + |rho_l| |rt_l - rc_l| + C b^2 D^2),
so sgn(y_l rt_l) = -sgn(rho_l vs_l) robustly (|kappa_y rho_l u_l(xhat_1)|/kappa_m >= (c_*/nu_1)(u/2) u Phi_l/(m K) >> the errors), and
      Q_l(y) = kappa_y kappa_m rho_l/u_l(xhat_1) (1 + o(1)):   Q_l < 0 for aligned l, Q_l > 0 for anti-aligned l.
For kind-(i) rows (privately tunable), |y_l| <= eps Design^2 + C b^2 D^2, so Q_l = o(1) uniformly.
Proof.  K2.16 notation: y_l = eps_l coef_l + zeta_m lambda_l (d kappa_m/d zeta(l)); for coarse strict non-peaks under (FC) in route V,
|d kappa/d zeta(l)| <= C b^2 D^2 (J1-ref B.3) and |zeta_m| <= C.  J1.6(a): coef_l = kappa_y rho_l + O(eps Design^2), kappa_y <= -c_*/nu_1.
rc_l = val_l/kappa_m = eps_l u_l(xhat_1)/kappa_m and |rt_l - rc_l| <= eta' + C b.  Multiply (eps_l^2 = 1).  QED
Reading: the certificate asks every thick-type row to move its target INWARD (|rt_l| decreasing) iff it is aligned, OUTWARD iff it is
anti-aligned: a displacement Delta_l pairs positively, kappa_m y_l Delta_l > 0, iff sgn(Delta_l rt_l) = -sgn(rho_l vs_l).

## 3.3 Theorem IN (inward relief).  PROVED (modulo the chain cited by J1.15 and J2.1).
If at a stage carrying a near-certificate some MOVABLE thick-type row l is ALIGNED and has robust or near-threshold status, or is
movable and nearly neutral (any alignment), then Step A is realized.  No peak resource, no coupling, any block type.
Proof.  Aligned, robust or near-threshold: rt' := rt with rt'_l := rt_l (1 - s), s := C nu_1 (||b|| + x)/(c_* u kappa_m |rt_l|) (<= Design^C x/u
since |rt_l| >= u Phi_l/(m K)).  Pairing (Lemma AL): <kappa y, rt' - rt> = -s kappa_m y_l rt_l = s |kappa_y rho_l u_l(xhat_1)| (1 + o(1)) >=
4(||b|| + x) for C large.  Admissibility (J1.13): (i) l is inactive (not a variable of Z_kappa) or has a free ratio (enters no tiny
minor or cofactor polynomial); robust minors move by <= Lip s |rt_l| << u; |rt' - r_1| <= eta' + Design^C x/u.  (ii) Statuses (Lemma K,
rho_d = m |r_d| K(sigma, R^2)/Phi_d with R^2 the full Omega sum of the block; in (T)-blocks psi_d with R_a^2, which contains rt_l only if l is
active): l's own status decreases (|r_l| and K decrease); every other status of the block decreases (R^2 decreases, K increasing in R^2);
robust peaks move by <= C Design s << u; other blocks are untouched.  KN-lever margins and (U)-block margins only improve.  The (X4^0)
rows of (T)-blocks are not tiny for a free ratio (else the ratio would be pinned); their robust slacks move by << u.  Lemma TF'.
Nearly neutral (any alignment): |y_l| >= c_* u/(8 nu_1) (J1.6(a) and the bound on d kappa/d zeta), so rt'_l := rt_l + sgn(y_l) beta_*/kappa_m
pairs by >= kappa_m |y_l| beta_*/kappa_m >= 4(||b|| + x) (definition of beta_*); the R^2 change is m^2 (beta_*/kappa_m)^2 + 2 m^2 |rt_l| beta_*/kappa_m
<= Design^C (x/u)^2 + Design^C b x/u, which moves every protected status by << eta' in (U)- and (KN)-blocks and by << mu_kappa(eta'/3) in
(T)-blocks (Corollary 1.3); own status stays nearly neutral up to O(beta_*).  Lemma TF'.  QED
Consequences.  J1's (J-c) and (J-d) hold WITHOUT a peak resource whenever the carrier is aligned (or nearly neutral); J1's (R-KN), (R-D2),
(R-np), (R-Ts) and (R-T) contain no aligned movable carrier and no nearly neutral movable carrier.  [(R-T) is empty by Corollary 1.3.]

## 3.4 Theorem OUT (outward relief).  PROVED (modulo the chain).
Let k be a movable ANTI-ALIGNED thick-type row with ROBUST status in block m.  Step A is realized if
 (a) m is not protected; or
 (b) m contains another movable row d != k with robust or near-threshold status such that, for every near-certificate y,
     Q_d(y) <= Q_k(y) - c_ex with c_ex := c_* u kappa_m/(C nu_1 Design^C) (e.g. d aligned (Q_d < 0 < Q_k), d of kind (i) (Q_d = o(1)),
     or d anti-aligned with rho_d/u_d(xhat_1) robustly smaller in modulus... precisely kappa_y kappa_m (rho_k/u_k - rho_d/u_d) >= c_ex); or
 (c) m is an unshifted block with a private two-sided peak resource (J1's (J-c)/(J-d) with the F-2 coupling); or
 (d) m is an unshifted block without peak resource with sigma_m = -1 (Theorem RL).
Proof.  (a) rt'_k := rt_k (1 + s), s as in 3.3: pairing s kappa_m y_k rt_k = s |kappa_y rho_k u_k| (1 + o(1)) > 0 (anti-aligned, Lemma AL);
statuses: k robust (room u, moves by Design^C x/u); the R^2 increase 2 m^2 rt_k^2 s moves other statuses of m by <= Design^C x/u, harmless
since m has no status with margin below u/2 (robust actives and inactives, nearly neutral ones, robust peaks).  Lemma TF'.
(b) EXCHANGE: rt'_k := rt_k + t/rt_k, rt'_d := rt_d - t/rt_d (t > 0): R^2 of block m changes by 2 m^2 (rt_k t/rt_k - rt_d t/rt_d) + O(t^2 (rt_k^{-2} +
rt_d^{-2})) = O(Design^C t^2): every status of m moves by <= Design^C t^2 << eta' (t = Design^C (||b|| + x)/c_ex).  Own statuses: k robust
(room u), d inward (decreases).  Z_kappa untouched (both movable).  Pairing: kappa_m (y_k t/rt_k - y_d t/rt_d) = kappa_m t (Q_k - Q_d) >=
kappa_m t c_ex >= 4(||b|| + x).  Lemma TF'.  (c) J1.15 (J-c)/(J-d) with J1-ref F-2.  (d) Theorem RL.  QED

## 3.5 Theorem GS (group rescaling of pinned ratios in unshifted blocks).  PROVED (modulo the chain).
Call two pinned active ratios LINKED if some tiny minor or tiny cofactor polynomial of Gamma^#(kappa, a) contains both; a GROUP G is a
connected component of the linking graph on all pinned ratios.  Suppose G consists of ratios of (U)-blocks only (no tiny polynomial
links G to a ratio of a shifted block).  Put zeta^G(y) := sum_{l in G} kappa_{m(l)} y_l rt_l / kappa_{max}(G) (kappa-weighted; kappa_max(G) the
largest kappa_m over the blocks met by G).  Then:
 (a) for every group G and s > 0 the targets rt^G(s) := (s rt_l for l in G, rt_l otherwise) satisfy Z_kappa (every tiny polynomial of m
     involves the ratios of exactly one group, and is homogeneous of degree <= n in each r^{(m)} (X1-ref D1), hence homogeneous in r^G);
     robust minors move by <= Lip |s - 1| ||rt|| << u for |s - 1| <= Design^{-C};
 (b) put zeta^G(y) := sum_{l in G} y_l rt_l.  If every near-certificate satisfies zeta^G(y) <= -z_G (z_G := c_* u^3/(C nu_1 Design^C)), Step A is
     realized with s := 1 - delta_G, delta_G := 4(||b|| + x)/(kappa_m z_G) (down-scaling of G: always status-admissible);
 (c) if every near-certificate satisfies zeta^G(y) >= z_G, Step A is realized with s := 1 + delta_G provided no row of G is near-threshold
     and either m is unprotected or m contains a movable row d with robust or near-threshold status and Q_d(y) <= -c_ex for all
     near-certificates y (an aligned movable row, or a kind-(i) row up to o(1)) used to cancel the R^2 increase (exchange as in 3.4(b)).
 (d) Sufficient for the sign hypotheses: the thick-type rows of G are all aligned (resp. all anti-aligned) and every non-thick-type row
     of G is of kind (i), or of kind (iv) with rt_l eps_l sigma_l <= 0 (resp. >= 0); then zeta^G(y) = sum_{thick l in G} kappa_y rho_l
     u_l(xhat_1)/kappa_m + (terms of the same sign) + O(eps Design^2), and z_G may be taken = c_* u^2 min_l |u_l(xhat_1)|/(2 nu_1 kappa_m).
Proof.  (a) A tiny polynomial P depends only on the ratios of one group (definition of the linking graph; free ratios enter no tiny
polynomial).  For each (U)-block m met by G, X1-ref D1 gives P(.., s r^{(m)}, ..) = s^{e_m} P(..) (r^{(m)} occurs only in the row (X3)_m);
since P does not depend on the ratios of m outside G, scaling only r^{G ∩ m} has the same effect.  Hence P(rt^G(s)) = s^{sum e_m} P(rt) and
vanishing is preserved; ratios of shifted blocks are not scaled and, by hypothesis, do not occur in P together with G.  (b) Pairing <kappa y, rt^G(s) - rt> = (s - 1) kappa_max(G) zeta^G(y) >= kappa_max(G)
delta_G z_G = 4(||b|| + x) (read kappa_m as kappa_max(G) in delta_G).  Statuses: the rows of G scale down, R^2 decreases: every status of m decreases (Lemma K).  Distance and
(TF3) as in Theorem RL.  Lemma TF'.  (c) Pairing kappa_m delta_G zeta^G(y) >= 4(||b|| + x) plus the exchange row's contribution
-kappa_m Q_d(y) t' >= 0 (t' := the R^2-compensating inward amount, 2 m^2 rt_d t' = 2 m^2 delta_G sum_G rt_l^2); statuses of G: robust, room u;
R^2 unchanged to first order.  (d) Lemma AL for thick rows; K2.16(2c) for kind (iv): y_l rt_l = (eps_l sigma_l rt_l)(coef_l sigma_l) +
O(eps Design^2 b^2 D^2) with coef_l sigma_l >= -(eps Design + |kappa| theta_0) Design.  QED
Remark.  Theorem RL is the special case G = all rows of the block (whole-block rescaling, with zeta_m in place of zeta^G and the
peak-derived sign of 2.2(b)); Theorem GS needs no hypothesis on peak resources: it rescales only pinned rows, which the peak columns see
only through zeta_m(y; rt) -- the change of the peak columns is covered by (TF3).

## 3.6 What the calculus leaves: the refined residual (R0') (necessary condition; PROVED as a consequence of 3.3-3.5, 2.3-2.5, Cor. 1.3)
At a residual stage (Step A carries near-certificates and none of J1.15', Theorems RL, IN, OUT, GS, Lemma KC applies):
 (M)  every movable thick-type row with robust or near-threshold status is ANTI-ALIGNED; no movable thick-type row is nearly neutral;
 (M1) if such a row k has robust status, its block m is protected, is not an unshifted block with peak resource, is not an unshifted
      block without peak resource with sigma_m = -1, and has NO exchange partner: every movable row d != k of m with robust or
      near-threshold status satisfies Q_d >= Q_k - c_ex; in particular m has no aligned movable row and no movable kind-(i) row with
      robust status, and all robust anti-aligned movable rows of m have the same value of rho_l/u_l(xhat_1) up to c_ex/(kappa_y kappa_m)
      ("anti-aligned proportional resonance": a_p = -alpha_m u_l(xhat_1) v_l(p) on their thick private coordinates, alpha_m > 0 common);
 (M2) anti-aligned near-threshold movable rows (D2-pushed, KN-pushed, free near-threshold actives) are relieved by nothing above;
 (G)  in every (U)-block, every group G of pinned ratios has zeta^G not robustly negative, and if robustly positive then (c) fails (a
      near-threshold row in G, or a protected block without an aligned/kind-(i) exchange row); for groups of thick-type and kind-(i)
      rows this means: G contains anti-aligned thick rows and either cancels (mixed alignment with sum_G rho_l u_l(xhat_1) ~ 0) or is
      anti-aligned-dominated with a near-threshold row or no exchange row;
 (U+) unshifted blocks without peak resource have aligned peaks (sigma_m = +1), are protected, and violate (KC) of Lemma KC;
 (S)  pinned thick-type rows of SHIFTED blocks ((T), (KN)) and thick-type peaks of shifted blocks without peak resource: no lever found
      here; for them the obstruction is the polar condition of Lemma TF': no point rt' of Z_kappa within the J1.13 distance, with
      protected statuses kept, pairs by >= 4(||b|| + x) with every near-certificate (a "normal resonance": the certificate functional
      kappa y restricted to the achievable displacements of the exact set lies in the polar of the status-safe cone; by Farkas, at a
      smooth point of Z with near-active set D, kappa y|_{T Z} is a nonnegative combination of the d psi_d|_{T Z}, d in D).
Relation to J1-ref's list: (R-T) empty (Cor. 1.3); (R-KN), (R-np), (R-D2), (R-Ts) are contained in (M1) ∪ (M2) ∪ (U+); (R-pk) in
unshifted blocks is contained in (U+) (Lemma NP: a thick-type peak forces "no peak resource"); (R-pin) is contained in (G) ∪ (S); (R-pk)
in shifted blocks is (S).

## 3.7 Proposition MA (forced mixed alignment in blocks with a peak resource).  PROVED (modulo the chain).
Let y be a near-certificate of size eps <= eps_* and m a block (any kind) with a private two-sided peak resource, containing at least one
thick-type row with robust or near-threshold status.  Then
      sum_{thick-type rows l of m} rho_l u_l(xhat_1)  =  -(kappa_m/kappa_y) sum_{kind-(iv) rows l of m} (rt_l eps_l sigma_l)(coef_l sigma_l) + O(Design^3 (eps + eta')),
and the left side has modulus >= (u^2/2) min |rc_l| kappa_m robustly unless the thick rows have MIXED alignment.  Consequently EITHER
(MA1) m contains both aligned and anti-aligned thick-type rows (with robust values), OR
(MA2) m contains a kind-(iv) row with a robust coefficient whose orientation rt_l eps_l sigma_l has the sign of sum_thick rho_l u_l(xhat_1)
      (positive if all thick rows of m are aligned, negative if all are anti-aligned).
Proof.  K2.16 notation: zeta_m (1 - Xt_m) = sum_{tuned l in m} rt_l eps_l coef_l with |Xt_m| <= 1/4; R-PK: |zeta_m| <= (4/3) eps Design.  Thick-type rows:
rt_l eps_l coef_l = kappa_y rho_l u_l(xhat_1)/kappa_m + O(eps Design^2 + Design eta') (Lemma AL); kind (i): O(eps Design^2); kind (iv):
(rt_l eps_l sigma_l)(coef_l sigma_l) with coef_l sigma_l >= -(eps Design + |kappa| theta_0) Design (K2.16(2c)); kinds (ii) do not occur.  Multiply
by kappa_m/kappa_y (kappa_y <= -c_*/nu_1).  If all thick rows have the same alignment, every term rho_l u_l has that sign and modulus >=
(u/2)|u_l| = (u/2) kappa_m |rc_l|.  QED
Combination with Theorem IN: in a block with a private peak resource and no compensating kind-(iv) row, a residual stage has an
ALIGNED thick-type row, and every aligned thick-type row of the block is PINNED (movable aligned rows are relieved by Theorem IN).  In a
(U)-block with a peak resource the movable anti-aligned rows are relieved too (J-c)/(J-d) (F-2 coupling), so EVERY non-nearly-neutral
thick-type row of such a block is pinned at a residual stage, the block has mixed alignment, and its pinned groups have zeta^G not
robustly negative (Theorem GS(b)).  This is the stage-wise form of J1's "stable exact case": the frozen value Phi_0^{(m)}(zhat) =
sum rho_l u_l(zhat) vanishes by CANCELLATION between aligned and anti-aligned pinned carriers.

## 3.8 Numerics (sanity only; H1_work/align_toy.py, rescale_toy.py, outputs *.out)
J1-ref's CONSISTENT one-block toy (exact resonance Phi0(zhat) = 0, two thick-type carriers, generators recomputed at every target):
 - mixed alignment at the resonance: rho_0 u_0(zhat) = -rho_1 u_1(zhat) in all 8 cases (exactly one aligned carrier), as forced by MA;
 - Lemma AL: sign(y_k rt_k) = -sign(rho_k u_k(zhat)) in 16/16 cases;
 - Theorems IN/OUT: after the obstruction is created (targets displaced along y, phi_y = 1e-3; min ||t||_inf = 2.0e-2..1.0e-1 with a peak
   resource, 29..175 without), moving the ALIGNED carrier's target INWARD or the ANTI-ALIGNED carrier's target OUTWARD (one row only, size
   4 phi_y/(kappa |y_k rt_k|)) gives phi_y = -3e-3 and min move 6.9e-4..7.1e-4 in all 16 cases; the opposite directions give phi_y = +5e-3
   and the move stays or grows (up to 8.7e2);
 - signed peak derivative d kappa/d zeta(c) = +1.0000/-1.0000, flipping with sgn zeta(c) (Lemma NP's bookkeeping, 1 - X ~ 1 in the toy);
 - whole-block rescaling in the direction sgn zeta_m(y; rt) lowers phi_y as predicted by Lemma TF (the toy's peak is not thick-type, so
   zeta is small there and the needed factor is unrealistic; this checks only the pairing algebra, not Lemma NP's robustness).
