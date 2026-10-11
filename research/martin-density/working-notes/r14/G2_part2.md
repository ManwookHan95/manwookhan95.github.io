# G2 part 2: (R1) -- coupled directions (Lemma 3.4(c) proved), Theorem H2.A without Brouwer coupling, the joint residual

Notation of Part 1 and of r13/H2_notes 1.  At an (R1) stage every tuned row is kind (i) (two-sided private) or kind (iv) (one-sided
upward); K^+_m / K^-_m = kind-(iv) rows of block m with eps-oriented target ratio rt_l > 0 / < 0.  "Inward" for a row l means a target
displacement with Delta_l rt_l < 0 (|rt_l| decreases), "outward" Delta_l rt_l > 0.  For a kind-(iv) row the HELPFUL direction (the one that
pairs nonnegatively with every certificate, since z_l >= -e_1) is the oriented-up direction Delta_l > 0: inward for K^-, outward for K^+.

## 2.1 Coupled directions

LEMMA 2.1 (status calculus of single and coupled displacements).  PROVED (mod chain).  Let m be a block, d in N ∩ m, and l, p rows of m.
 (a) l_d(-sgn(rt_l) e_l) = -[1[l = d] + 2 kappa'_m m^2 rt_l^2 1[l in Omega_{(d)}]]/|rt_l| <= 0: a single INWARD displacement of a movable row
     is status-safe in every block.
 (b) l_d(sgn(rt_l) e_l) = [1[l = d] + 2 kappa'_m m^2 rt_l^2 1[l in Omega_{(d)}]]/|rt_l| >= 0, > 0 iff l = d or l in Omega_{(d)}: a single
     outward displacement is status-safe iff the block has no protected status that sees l (N ∩ m = {} for route-V statuses; for Puiseux
     statuses of a (T)-block only ACTIVE rows are seen).
 (c) [coupling with a partner] Let l be movable with rt_l != 0 and p != l movable with |rt_p| >= u Design^{-C_3} and p in Omega_{(d)} for
     every d in N ∩ m with l in Omega_{(d)} (a PARTNER of l).  Put
        c_{lp} := (|rt_l| + 1[l in N]/(2 kappa'_m m^2 |rt_l|))/|rt_p|,      v_{lp} := sgn(rt_l) e_l - c_{lp} sgn(rt_p) e_p .
     Then l_d(v_{lp}) <= 0 for every d in N ∩ m, and c_{lp} <= Design^{C}/u^2.
 (d) [coupling with the block scaling in a (U)-block] With rt^{(m)} the target vector of block m (all rows of m) and
        c_l := (1[l in N]/|rt_l| + 2 kappa'_m m^2 |rt_l|)/(1 + 2 kappa'_m R^2_m),     v_l := sgn(rt_l) e_l - c_l rt^{(m)} :
     l_d(v_l) <= 0 for every d in N ∩ m, and c_l <= Design^C/u.  In a (U)-block rt^{(m)} lies in V (sum of the piece scalings of all groups
     meeting m, the free and the movable rows of m; H1-ref Lemma PC), so v_l is in V when l is movable.
Proof.  l_d(Delta) = Delta_d/rt_d + 2 kappa'_m m^2 sum_{k in Omega_{(d)}} rt_k Delta_k (Definition 1.2).  (a), (b): Delta = -/+ sgn(rt_l) e_l.
(c) For d notin {l, p}: l_d(v) = 2 kappa' m^2 (|rt_l| - c |rt_p|) 1[...] = -1[l in N]/|rt_l| <= 0 (using rt_l sgn(rt_l) = |rt_l| and rt_p
sgn(rt_p) = |rt_p|; if l notin Omega_{(d)}, only the p-term remains and it is <= 0).  For d = l in N: 1/|rt_l| + 2 kappa' m^2 (|rt_l| -
c |rt_p|) = 1/|rt_l| - 1/|rt_l| = 0.  For d = p in N: -c/|rt_p| + 2 kappa' m^2(|rt_l| - c|rt_p|) <= 0.  Size: |rt_l| <= Design^{C_4},
kappa'_m >= c_K/8.5 (dK/dR^2 >= c_K, K <= 8.5 on the W-fix region, cert1 1), |rt_p| >= u Design^{-C_3}.  (d) l_d(rt^{(m)}) = 1 + 2 kappa'_m
R^2_{(d)} where R^2_{(d)} = m^2 sum_{Omega_{(d)}} rt^2 <= R^2_m; so l_d(v_l) <= 1[l = d]/|rt_l| + 2 kappa' m^2 |rt_l| - c_l (1 + 2 kappa' R^2_{(d)})
<= 0 when R^2_{(d)} = R^2_m, and for (T)-block Puiseux statuses (R_a^2 <= R^2) replace R^2_m by R_a^2 in c_l (the bound c_l <= Design^C/u
persists).  QED

LEMMA 3.4(c) (outward rows in protected blocks).  PROVED (mod chain).  Let l in K^+_m be free (movable) in a protected shifted block m.  If
l has a partner p in the sense of Lemma 2.1(c) -- a kind-(i) row, a free K^- row with robust ratio, an inactive movable row (hold, D2- or
KN-pushed row; for Puiseux-protected statuses of a (T)-block the partner must be ACTIVE), the KN lever d_0 -- then v_{lp} is in D_1 (after
normalization by ||v_{lp}||_rt <= Design^C/u^2) and every hull element z (in particular the z* of Lemma MS(b)) satisfies
      kappa_m (z_l - c_{lp} sgn(rt_p) z_p) <= Design^C u^{-2} c_MS / rbar_l .                                                 (2.1)
Consequently z*_l <= Design^C u^{-3} c_MS/kappa_m + c_{lp} max(0, sgn(rt_p) z*_p), and with |z*_p| <= eps Design^2 + e_X (p of kind (i)),
z*_p >= -e_1 and z*_p <= c_MS Design^C/u (p in K^-, sgn(rt_p) = -1, both directions of p controlled by (JF1)), or (JF1) for an inactive
partner, z*_l <= delta_2 := Design^C u^{-3}(c_MS + e_1 + eps Design^2 + e_X).
Proof.  v_{lp} in V (both rows movable), status-safe (Lemma 2.1(c)), so v_{lp}/||v_{lp}||_rt in D_1; apply (1.1).  The bounds on z*_p:
(JF1) and Lemma 1.1(d).  QED
Remarks.  (1) This replaces H2's Lemma 3.4(c) SKETCH (and its "all-at-once version for several outward rows"): no simultaneous bands and no
Brouwer coupling are needed, because the minimax treats each coupled direction separately (each v_{lp} is a point of D_1, and (1.1) holds for
all of them at once).  (2) The (KN)-lever bookkeeping is Remark 1.8 (pre-move convention).  (3) R_a^2 in (X4^0) rows: a free ratio is in no
tiny polynomial; if a tiny minor of block m contains an (X4^0) row, every active ratio of m is pinned (J1-ref P-MT), so there is no free K^+
row in m to which (c) would apply; robust minors containing (X4^0) rows move by <= Design^C h << u.

## 2.2 Theorem H2.A without Brouwer coupling

DEFINITION 2.2.  At an (R1) stage: P^-_m := pinned rows of K^-_m; LOCKED rows: free K^+ rows l of a protected block m with no partner in the
sense of Lemma 2.1(c) and, if m is a (U)-block, ... none (Lemma 2.1(d) always applies in (U)-blocks); P^+_m := pinned or locked rows of K^+_m.
Residual block types (two), (up), (down) as in H2 Theorem H2.A.

THEOREM H2.A' .  PROVED (mod chain).  At an (R1) stage, if no block is residual, Step A is realized (Lemma MS(a) at the admissible targets).
Proof.  Suppose not; let z* be as in Lemma MS(b).  Every free K^- row l: the inward direction is in D_1 (Lemma 2.1(a)), so kappa_m z*_l rbar_l
<= c_MS (inward = oriented up for K^-), and z*_l >= -e_1: |z*_l| <= delta_1' := max(e_1, c_MS/(kappa_min u Design^{-C_3})).  Every free K^+
row: (U)-block: v_l of Lemma 2.1(d) is in D_1 after normalization, and kappa_m (z*_l - c_l zeta_m(z*)) <= Design^C c_MS/u with |zeta_m(z*)|
<= (4/3) eps Design (R-PK; every (U)-block has a two-sided peak resource at (R1) stages, H2 Fact 1.1(d)); unprotected shifted block: Lemma
2.1(b); protected block with a partner: Lemma 3.4(c).  So |z*_l| <= delta_2 (+ the R-PK term) on every free kind-(iv) row that is not locked.
Kind-(i) rows: |z*_l| <= eps Design^2 + e_X.  Now H2's case analysis applies verbatim to z* (it uses only (1.2), Proposition 3.1 and the
band bounds, all available for z* by Lemma 1.1(d) and the bounds just proved): two-sided lever and P^-_m = {}: all K^- rows are free, so
sum_{K^+} z*_l rt_l <= sum_{K^-} |z*_l||rt_l| + e_2 + (4/3) eps Design =: Z_m, each K^+ term is >= -e_1 Design^{C_4}, hence z*_l <= Design^{C_3}
(Z_m + |Lambda_A| e_1 Design^{C_4})/u on every K^+ row; two-sided and P^+_m = {}: symmetric; (up) with P^-_m = {}: zeta_m(z*) <= (4/3) eps Design
and all K^- free: the same bound on K^+; (down) with P^+_m = {}: zeta_m(z*) >= -(4/3) eps Design and all K^+ free and not locked: the same
bound on K^-.  So |z*_l| <= c_1/(16 |Lambda_A|) on every kind-(iv) row (C_h in h_max large enough), and sum_{(iv)} z*_l <= c_1/16 < c_1/4,
contradicting Proposition 3.1(a) for z* (Lemma 1.1(d)).  QED
Remarks.  (1) Compared with H2.A: the realization is by ONE fixed displacement (Lemma MS(a)), not by band-relaxation, so the fixed point
beta_1 of G-CPL, the coupled rescaling s of F-2 inside the Brouwer step and Lemma 3.4(c)'s all-at-once SKETCH are not needed.  (2) The
residual is now a statement about ONE hull element z* and the joint system (Theorem JF).

## 2.3 The (R1) residual in joint form

THEOREM R1-J (structure of a non-realized (R1) stage).  PROVED (mod chain).  If Step A is not realized at an (R1) stage, then with z*,
lambda, nu, mu of Theorem JF:
 (a) some block is residual ((two)/(up)/(down) of Definition 2.2);
 (b) on every free kind-(iv) row that is not locked |z*_l| <= delta_2; on locked rows l (free K^+ rows of protected blocks without partner)
     (JF1) gives  kappa_m z*_l = 2 kappa'_m m^2 rt_l Lambda_m^{(l)} + O(c_MS/rbar_l)  (l notin N)  or  = lambda_l/rt_l + 2 kappa'_m m^2 rt_l
     Lambda_m^{(l)} + O(c_MS/rbar_l)  (l in N): the certificate weight on locked rows is R^2-proportional (z*_l/rt_l common up to the own
     multiplier), and it is supported by the status multipliers of the protected statuses of the block (Lambda_m > 0 if some locked row
     carries weight > c_MS Design^C);
 (c) on every affine pinned group G (single-block or multi-block): kappa z*|_G - A^T lambda|_G = sum_i mu_i grad_G P_i + err (JF2); with
     z*_l >= -e_1 on the oriented kind-(iv) rows of G and |z*_l| <= eps Design^2 + e_X on its kind-(i) rows, the form sum_i mu_i grad P_i is
     nonnegative (up to (A^T lambda) and errors) on the oriented kind-(iv) ratios of G and nearly blind to its kind-(i) ratios (Corollary JF');
 (d) on non-affine groups only (JF3) (balance of each (U)-piece against the status multipliers) is available;
 (e) (JF5): phi_{z*}(rt_0) > -x/4, i.e. the joint resonance form sum over groups of sum_i mu_i P_i(rc) plus the status and movable-row terms is
     NOT below -x/4: the start row is on the wrong side of the joint form (or within x/4 of it);
 (f) shared target-coordinate generators restrict z* only through z*^T g >= -eps_1 (JF4); a shared two-sided generator g whose column is not
     orthogonal to the residual direction forces |z*^T g| <= eps_1, which is an additional LINEAR constraint on (mu, lambda) through (JF1)-(JF3).
Proof.  (a) Theorem H2.A'.  (b) (JF1) and Theorem H2.A''s bounds.  (c)-(e) Theorem JF with Lemma 1.1(d).  (f) (JF4).  QED

REMARK 2.3 (what changed relative to H2 4.1-4.2, P-41).  P-41 listed three reasons why H2's single-block Farkas alternative is only a
restricted model: (i) multilinear minors over several blocks, (ii) shared generators at target coordinates, (iii) the margin of order rho_0.
In Theorem R1-J: (i) affine multi-block groups are included exactly (V_G = tangent space of the joint affine zero set) and genuinely
multilinear ones keep their (U)-piece scalings ((d)); (ii) shared generators are part of the certificate set, hence of z* ((f)); (iii) the
margin is built into Lemma MS through the threshold x/4 in (1.2) (equivalently rho_0(rt') <= x/4).  The shifted-block form (H2 4.2, SKETCH)
is the case of Theorem JF in which a block's one-sided kappa lever contributes the inequality zeta_m(z*) <= small (kappa-raising) or >= -small
(kappa-lowering) to (JF4), and the block's affine groups (minors avoiding (X4^0) rows: affine in r^{(m)}, H1-ref D.1) contribute (JF2).
REMARK 2.4 (what is NOT shown).  Theorem R1-J is a necessary condition for non-realization.  It does not show that the residual can be
avoided: the locked residual (b) involves only certificate weights (kind-(iv) weights are not tied to f's data), and the resonance residual
(c), (e) is a sign condition on f's start-row data that is not excluded at a single stage.  Persistence over main stages is Part 3.
