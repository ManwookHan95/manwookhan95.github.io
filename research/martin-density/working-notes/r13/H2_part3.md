# H2 part 3: the uniform-sign object of (R1), one-sided bands, block levers, peaks; Theorem H2.A

Setting of H2_part1/2.  At an (R1) stage every tuned row is kind (i) or kind (iv) (Fact 1.1), every near-certificate y has
||coef_(iv)||_2 >= c_1/2 (Fact 1.2), |coef_l - eps_l y_l| <= e_X (1.1) and y_l >= -e_1 on kind-(iv) rows (1.2).  For a block m:
zeta_m(y; rt) := sum_{l in m} y_l rt_l (J1 notation), K^+_m / K^-_m := kind-(iv) rows of m with rt_l > 0 / < 0 (|rt_l| >= u/Design^C).

## 3.1 The uniform-sign object of pure (U*) certificates.  PROVED.
PROPOSITION 3.1.  At an (R1) stage, for every near-certificate y of size eps <= eps_*:
 (a) [all-at-once positivity]  sum_{l kind (iv)} y_l >= c_1/4 and y_l >= -e_1 for each kind-(iv) l;
 (b) [per-block balance]  for every block m:
      two-sided peak resource (every unshifted block; shifted blocks with a robust peak of pull capacity >= 4W', Lemma 2.4):
                     |zeta_m(y; rt)| <= (4/3) eps Design;
      one-sided peak resource raising kappa_m (shifted block, Delta''_m < 0, a robust peak with an S_th bank):  zeta_m(y; rt) <= (4/3) eps Design;
      one-sided peak resource lowering kappa_m (shifted block, Delta''_m > 0):                                  zeta_m(y; rt) >= -(4/3) eps Design;
 (c) |y_l| <= eps Design^2 + e_X on every kind-(i) row.
Proof.  (a) ||y_(iv)||_2 >= ||coef_(iv)||_2 - |Lambda_A|^{1/2} e_X >= c_1/2 - small; with y_l >= -e_1: sum_l y_l >= sum_l (y_l)_+ - |Lambda_A| e_1
>= ||(y_(iv))_+||_2 - |Lambda_A| e_1 >= ||y_(iv)||_2 - 2|Lambda_A| e_1 >= c_1/4.  (b) Two-sided: J1-ref Lemma R-PK.  One-sided: the same
computation (R-PK's proof) for a ONE-sided generator.  The bank at the near S_th coordinate s of a robust coarse peak c of block m changes
only u_c(xhat) among coarse carriers (s is private, e unchanged at a contact; at raised thin support the common-mode term is
<= 2b eff, absorbed), by eff v_c(s) z_s per unit, with data sign z_s = -sgn(Delta''_m) vs_c (K1 1.0: c_c = -Delta''_m lambda_c vs_c).  So
|zeta_c| = lambda_c vs_c u_c(xhat) moves by -sgn(Delta''_m) eff v_c(s), and under (FC) d kappa_m/d zeta(c) = 1 - X_m in [3/4, 1]: the generator
moves kappa_m by -sgn(Delta''_m)(1 - X_m) lambda_c eff v_c(s) and every Ft_l (l in m) by -rt_l times that; its action on y^T Ft is
sgn(Delta''_m)(1 - X_m) lambda_c eff v_c(s) zeta_m.  One-sidedness (>= -eps) gives the two inequalities with eff v_c(s) lambda_c (1 - X) >=
3/(4 Design) [K2.16(2): eff_s >= 1/Design, lambda_c v_c(s) >= v_min].  Existence of the bank: V1 Lemma D gives a robust coarse peak in every
block; in (R1) its near coordinates are off F or thin (Fact 1.1(a)), of the data sign (Lemma K1.3 (S) and (X1), as for tuned carriers),
hence S_th after (P2)/(P3).  (c) K2.16(2a) and (1.1).  QED
Remarks.  (1) (a) is the analogue of J1.6(a) for (R1): no single kind-(iv) row carries a uniform robust coefficient, but the SET of all
kind-(iv) rows does, with a fixed (positive) sign.  So relieving ALL kind-(iv) rows at once kills every (U*) certificate; relieving one
does not (different certificates may live on disjoint sets of kind-(iv) rows).  (2) (b) replaces J1.6 inside a block: in a block with a
two-sided peak resource the robust weight of K^+_m equals that of K^-_m up to O(eps Design^3).

## 3.2 One-sided bands.  PROVED (separation as in J1.8; legitimacy from J1.13 and Lemma K).
LEMMA 3.2 (one-sided band version of K2.9 / J1.8).  Split the rows of Sys-A into equality rows and banded rows l in B with boxes [lo_l, hi_l]
containing 0 (the final Ft_l must lie in its box); Box := prod_B [lo_l, hi_l].
 (a) If B(b, rho_0) ⊂ (W/2) conv(G ∪ {0}) - Box, the band-relaxed Step A is realized (K2.9(c)'s Brouwer argument with unknowns (t, sigma) in
     {t >= 0, ||t|| <= W} x Box and the minimal-norm selection, as in J1.8(a)).
 (b) Otherwise some unit y with max_g(-y^T g) < 2(||b|| + rho_0)/W satisfies  sum_{l in B} max(y_l lo_l, y_l hi_l) < phi_y + rho_0 <= ||b|| + rho_0.
Proof.  The realization equation is G t - sigma = b - Rem(t), sigma in Box.  Separate b'' in B(b, rho_0) \ ((W/2)Q - Box): a unit y with
y^T b'' < (W/2) min(0, min_g y^T g) - max_{sigma in Box} y^T sigma.  Both terms on the right are <= 0 (0 in Q, 0 in Box), so (W/2) max_g(-y^T g)
< -y^T b'' <= ||b|| + rho_0 and max_Box y^T sigma < -y^T b'' <= -y^T b + rho_0 = phi_y + rho_0.  (a) is J1.8(a) verbatim with Box.  QED
OVERSHOOT BAND on a row l: box [0, beta] (the realized value may exceed the target by up to beta).  Then (b) gives (y_l)_+ < (||b|| + rho_0)/beta.

LEMMA 3.3 (legitimacy of shrinking bands).  Let l be an ACTIVE row whose ratio is FREE (J1.13: no tiny minor and no tiny cofactor
polynomial of Gamma^#(kappa, a) depends on it), with rt_l < 0 (l in K^-), and let beta <= kappa_min u/(4 Design^C).  Then the overshoot band
[0, beta] on row l is legitimate: realized ratios r^#_l in [rt_l, rt_l + beta/kappa] have |r^#_l| <= |rt_l| and the same sign, every
status of every block is <= its value at the targets (upper protections kept), robust statuses move by <= Design^C beta << u, Z_kappa is
untouched (l free), robust minors stay >= u/4, and the class data projected at the realized ratios satisfy J1.13 (i)-(ii).
Proof.  Lemma K: rho_d = m |r_d| K(sigma, R^2)/Phi_d for every coarse non-peak (and for peaks with their own r), K strictly increasing in R^2,
R^2 = m^2 sum_Omega r^2 decreases when |r_l| decreases; every protected status of route V is an UPPER bound (actives of (T)-blocks <= 1 - mu/2,
(U)-blocks <= 1 - eta'/2, D2/KN pushes, (KN)-blocks U1-ref Prop. KN(b), KN-1 values m^2 sum r^2 small) or robust (margin >= u).  The remaining
items are J1.13 (refereed, with J1-ref B.5's addition).  |r^#_l - r_1,l| <= eta' + beta/kappa_min: inside J1.13 (i)'s allowance.  QED
Precision.  In (T)-blocks the (X4^0) entries m^2|r_l| K(sigma_rob, R_a^2) depend on EVERY active ratio of the block through R_a^2 (J1-ref P-MT);
so when a tiny minor contains an (X4^0) row of block m, every active ratio of m is PINNED in the sense of J1.13.  "Free" is meant in that
strict sense.

LEMMA 3.4 (bands on K^+ rows: when legitimate).  An overshoot band on a free active row l in K^+_m (|r^#_l| may exceed |rt_l|) is legitimate
 (a) if m is a (U)-block: J1.15' (J-d) with J1-ref F-2 (a two-sided band; (R1) gives the private two-sided peak resource, Fact 1.1(d));
 (b) if m has no R^2-sensitive protected status (no active near-threshold carrier, no D2/KN-pushed carrier, no KN-1 hold with
     near-threshold relevance): J1.13 (J-f, second clause);
 (c) [SKETCH] if m contains another FREE active row k (kind (i), or k in K^-_m) with robust ratio and l is not near-threshold, or if m has a
     robust inactive Omega carrier d_0: compensate the R^2 increase 2 m^2 |rt_l| beta/kappa by shrinking |r_k| (resp. pushing d_0 inward) by
     O(Design^C beta/u^2) (H1 Lemma KC's computation); the compensating displacement pairs with every near-certificate by
     <= C eps Design^4 (kind (i), (KN)) or helpfully (k in K^-).  Unproved detail: the (KN)-lever bookkeeping and the R_a^2 dependence of
     (X4^0) rows (both as in J1-ref P-MT).
Otherwise the row is LOCKED.

## 3.3 Theorem H2.A.  PROVED (modulo the chain cited by J1.15' and J2.1, and Lemma 3.4(c) where used).
THEOREM H2.A.  At an (R1) stage (L, w, a), put on every FREE kind-(iv) row l in K^- (all blocks), and on every free kind-(iv) row l in K^+ for
which Lemma 3.4 applies, an overshoot band of half-width
      beta_1 := 16 |Lambda_A| Design(L)^{C_3} (||b|| + rho_0)/(c_1 u),     C_3 := the exponent with |rt_l| >= u/Design^{C_3} on active rows.
Call a block m RESIDUAL if one of the following holds (P^-_m, P^+_m := pinned or locked rows of K^-_m, K^+_m):
 (two)  m has a two-sided peak resource, P^-_m != {} and P^+_m != {};
 (up)   m has only a kappa-RAISING one-sided peak resource (Delta''_m < 0, all robust peaks of pull capacity < 4W') and P^-_m != {};
 (down) m has only a kappa-LOWERING one-sided peak resource (Delta''_m > 0, all robust peaks of capacity < 4W') and P^+_m != {}.
If no block is residual, the band-relaxed Step A is realized, and (with J1.13 and J2.1) the stage feeds (LSC-trunc)_N.
Proof.  Suppose not.  Lemma 3.2(b) with W, rho_0 of the relaxed system gives a near-certificate y of size < 4 Design^{-C_A} <= eps_* with
sum_B beta_1 (y_l)_+ < ||b|| + rho_0, so (y_l)_+ < c_1 u/(16 |Lambda_A| Design^{C_3}) =: delta_1 on banded rows; with (1.2), |y_l| <= max(e_1, delta_1)
there.  Fix a block m.  By 3.1(c) the kind-(i) rows contribute |sum y_l rt_l| <= |Lambda_A| Design^{C}(eps Design^2 + e_X) =: e_2 to zeta_m.
 - two-sided, P^-_m = {}: zeta_m = sum_{K^+} y_l rt_l - sum_{K^-} y_l |rt_l| + O(e_2), |zeta_m| <= (4/3) eps Design, and all K^- rows are banded,
   so sum_{K^+} y_l rt_l <= |Lambda_A| Design^{C_3'} delta_1 + e_2 + 2 eps Design; each term is >= -e_1 |rt_l|, so every K^+ row has
   y_l <= Design^{C_3}(|Lambda_A| Design^{C_3'} delta_1 + small)/u.  Two-sided, P^+_m = {}: symmetric (all K^+ banded, K^- controlled).
 - up, P^-_m = {}: zeta_m <= (4/3) eps Design and all K^- banded: the same bound on K^+.
 - down, P^+_m = {}: zeta_m >= -(4/3) eps Design and all K^+ banded: sum_{K^-} y_l |rt_l| <= sum_{K^+} y_l rt_l + e_2 + 2 eps Design: the same bound on K^-.
(Every block has a peak resource of one of the three types by 3.1(b).)  Hence |y_l| <= c_1/(8|Lambda_A|) on every kind-(iv) row (for
L >= l_f: delta_1 Design^C/u <= c_1/(16|Lambda_A|)... by the choice of beta_1, and eps, e_1, e_2 << c_1/|Lambda_A|^2), so sum_{(iv)} y_l <=
c_1/8, against Proposition 3.1(a).  Legitimacy of the bands: Lemmas 3.3, 3.4; they move ratios by <= beta_1/kappa_min <= Design^C (||b|| +
rho_0)/u, the allowance of J1.13 (i) (same order as J1's beta_*).  QED
[Numerical sanity check of the case analysis (linear model with one-sided rows, three lever types, overshoot boxes; 4000 random
configurations x 40 right-hand sides, exact LP feasibility vs the prediction "no residual block"): r13/H2_work/toy_onesided.py/.out,
4000/4000 agree.]

## 3.4 Peaks of blocks without peak resources (idea (3) of the task)
PROPOSITION 3.5.  PROVED.  At an (R1) stage:
 (a) every UNSHIFTED block has a private two-sided peak resource (Fact 1.1(d)); so in (R1) the class "(R-pk)/(R-np)" of J1-ref and H1's
     case (U+) (unshifted block WITHOUT peak resource) is EMPTY;
 (b) every SHIFTED block has a one-sided peak resource whose direction is -sgn(Delta''_m) on kappa_m (3.1(b)); it is two-sided iff some
     robust coarse peak has pull capacity >= 4W' (Lemma 2.4, K1 2.2's repair "TU on the peak");
 (c) a robust peak of a shifted block is NEVER thick-type in (R1) (no thick-type carrier at all), so the alternative "such peaks are
     thick-type" of idea (3) is FALSE in (R1); in contrast H1 Lemma NP(b) shows it for UNSHIFTED blocks without peak resource.  The
     difference: peaks of shifted blocks carry data (-Delta''_m lambda_c vs_c), so their thin/off-F near coordinates are one-sided S_th
     coordinates, not ZD.
 (d) A design cannot supply two-sided peak resources in shifted blocks.  HEURISTIC (not a theorem): every robust coarse peak of a shifted
     block carries data, so any private coordinate of it is either data-sign (one-sided) or needs a cushion; a row f may put anti-data-sign
     support on the whole pull range of every robust peak (the deep raise provides the cushions); designed extra carriers are either robust
     peaks (then the same applies) or non-peaks (d kappa/d zeta <= C b^2 D^2 in route V: no kappa lever).  So (down)/(up) blocks cannot be
     designed away; Theorem H2.A uses their ONE-sided lever instead.
(e) [Cross-stage, Lemma 2.6] an (up) or (down) configuration of a block cannot repeat with the same shift sign at the next main stage if
    that stage is (R1): its robust peaks' old pull ranges are anti-data-sign thin unraised private coordinates there.
