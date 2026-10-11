# N3 Part 3 — Test against the engineered approximants; the only non-inherited residue (the hand-over); numerics

Notation of Parts 1-2.  [I, def:engineered], [I, thm:engineered] = Part I Definition 7.12 / Theorem 7.18.

## 3.1 The engineered approximants meet every necessary condition of Part 2, with matching constants

Setting of [I, thm:engineered]: I finite, f with F finite, g in C(f) with two-piece data (b+-, omega+-), b^theta, omega^theta,
v = b+ - b-, rho^2 kappa_w < 1, I_- = {m : Delta d_m < 0} satisfying (SC).  The approximant f' (stage (N_w, s_1, N''))
has: window masses m_j = 4 rho s_1 |b^theta_j| on K n [1, N_w] (sign z_j), z' = z on [1, N''], z' = 0 beyond N'', the
cut-off conditions (N1) frak_t(N'') <= s_1^2, (N2), (N3) rho V_{>N''} <= delta s_1/16; it uses the theta-pair for
0 < |tau| <= s_1 and the +- pairs for s_1 < |tau| <= T_0.

THEOREM 3.1 (sharpness of the Part 2 conditions).  PROVED.  For the engineered approximants, at late stages:
 (i) [aligned or banked] every contact of f in [1, N''] is a contact of f' or a window bank with the same sign; the free
     coordinates of f' are J(f) n [1, N''] (rooms of f) and (N'', infinity), where |psi'_j| <= nu^tot_j <= tau(N'') :=
     sup_{i > N''} nu^tot_i; since N'' is chosen after s_1, the necessary condition of Theorem 2.6(a) for far free
     coordinates (mu_S >~ kappa^2 c' tau(N'')/||psi 1_S||) holds for every finite aligned S inside the window.
 (ii) [de-switching scale] the theta-pair has V = 0 (B+ = B- = rho(beta^theta - c a'), Omega+ = Omega- = Omega^theta) and the
     +- pairs have V = rho v != 0 in general: the hand-over (de-switching) scale of the construction is exactly s_1.
 (iii) [bank–de-switching inequality] for S subset K n [1, N_w] aligned, exactly visible (one block), with S disjoint from the
     supports of the carriers of omega^theta: Osc_S(g'; psi') <= rho ||b^theta 1_S||_1 (1 + O(s_1)) and
     mu_S(f') = 4 rho s_1 ||b^theta 1_S||_1 / q*(a''), hence mu_S(f') >= 4 s_1 Osc_S(g'; psi') (1 - o(1)): Corollary 2.8(i)
     (mu_S >= kappa' t/8 at t = s_1) is met with a factor 32 to spare.
 (iv) [tail control] (N1) is exactly the cut-off condition of Lemma 2.10 at the junction scale s_1.
Proof.  (i) Definition of f' and |psi'_j| <= sum_k lambda_k |w'(k)||u_k(j)| <= nu^tot_j.  (ii) Step 2 of the proof of
[I, thm:engineered]: B^theta := rho(beta^theta - c a') is used on both sides for |tau| <= s_1, and beta+ - beta- = v.
(iii) In the theta-regime g'_j = rho(b^theta_j - d'(omega^theta) psi'_j - c a'_j) for j in S (S misses the carrier supports),
so Osc_S(g'; psi') <= rho ||(b^theta - c a')1_S||_1 with |c| -> 0 and ||a' 1_S||_1 = O(s_1); the bank masses are as stated by
[I, lem:approxfacts(a)] (a' = a''/q*(a''), q*(a'') -> 1).  (iv) Definition.  QED

CONSEQUENCE.  For mates with exact two-piece data (Delta d >= 0 or (SC), rho^2 kappa_w < 1) every necessary condition derived
in Parts 1-2 is met by the engineered approximants up to absolute constants, and these approximants recover rho g.  So no
functional of the types of Part 2 (profile/oscillation functionals on contact, signature or free coordinates; switching
moduli; bank-mass functionals) can certify non-density for such mates — and the conditions of Part 2 are sharp, not
lossy, since the recovering construction saturates them.  For mates WITHOUT exact data (scale-dependent switching), the
conditions of Part 2 are still satisfiable in the data (Theorem 2.6(b), Prop. 2.9, Lemma 2.10): they do not obstruct either.

## 3.2 What is not inherited: the hand-over at the de-switching scale

By Theorem 1.4 every NA approximant of a row with an infinite contact set must DE-SWITCH: below some scale s_* (depending
on the approximant) bounded-coefficient switching is impossible, and by Corollary 2.8 the profile oscillation of the mate
must then be carried by banks of mass >~ kappa s_* (or by deep carriers).  Above s_* the approximant can inherit f's
one-sided structure (Corollary 2.5, Prop. 2.9, Lemma 2.10).  The HAND-OVER at s_* is the only place where an NA approximant
is structurally different from f, and the only place where a uniform obstruction could live.

PROPOSITION 3.2 (banks move carrier values at first order).  PROVED (from [III, lem:III-masses(i)] for diagonal U; general U
by the same computation).  Let a have support F, and A = a + sum_{s in Bk} c_s e_s* with Bk disjoint from F (banks).  Then for
every u in l_1, with e_A := U*A/||U*A||, nu := ||U*a||:
   <U*u, e_A - e> = nu^{-1} <P^perp U*u, sum_{s in Bk} c_s U* e_s*> + O(||c||^2),
(diagonal U: = nu^{-1} sum_s c_s (mu*_s)^2 u(s) + O(||c||^2)).  Hence a bank configuration of total mass mu changes the value
u_k(xhat') of a carrier k by a LINEAR form of the (sign-constrained) masses, of size O(mu), and the normalized values
nv'_k = lambda_k u_k(xhat')/A' by O(lambda_k mu) plus the common normalization.
Proof.  e_A - e = (U*A/||U*A||) - (U*a/||U*a||); differentiate at c = 0: d e_A = (P^perp U* dA)/nu.  For diagonal U this is
[III, lem:III-masses(i)].  xhat' - zhat = (z' - z) + U(e_A - e) and z' = z at banks placed on contacts of f with sign z_s. QED

READING (the junction mismatch, U3-referee F6).  For window data whose switching runs through carriers with coefficients of
order 1/t, the d-values d(omega) = sum_k omega(k) nv_k move by O(mu/t) when banks of mass mu ~ s_1 are placed; the resulting
first-order level mismatch at the junction is of order s_1/t^2 per unit tau, i.e. tau^2/t^2 at |tau| = s_1: SCALE
INVARIANT (enlarging the theta-regime enlarges the masses).  [I, thm:engineered] avoids it because its data are FIXED
(coefficients O(1)); Part III removes it by d-CONSISTENCY: the normalized values of the finitely many switching carriers
are re-tuned exactly at f' by levers ([III, def:III-dcons], [III, lem:III-DC]).  HEURISTIC summary of U3-ref F6, verified
numerically there (junction_check.py: kappa t^2/s_1 constant to five digits).

PROPOSITION 3.3 (far free levers are weak at engineered rows).  PROVED.  Let f' be any row whose z' agrees with z on [1, N],
and let Delta z' be any change of z' supported in (N, infinity) with ||Delta z'||_inf <= 2.  Then for every carrier k,
   |u_k(xhat' + Delta z') - u_k(xhat')| <= 2 ||u_k 1_{(N, inf)}||_1 <= 2 frak_t(N)/lambda_k.
In particular, under the cut-off condition (N1) frak_t(N'') <= s_1^2 of [I, thm:engineered], far free moves change the value
of a carrier of weight lambda_k by at most 2 s_1^2/lambda_k, while the banks (Prop. 3.2) change it by order s_1: for coarse
switching carriers (lambda_k >> s_1) the two-sided far levers are too weak by the factor s_1/lambda_k.  Compensation must then
come from moves at moderate depth, where the approximant must keep f's structure, i.e. from ONE-SIDED resources (banks with
prescribed signs, inward contact moves, pulls [III, def:III-levers]) — unless the design of T provides private two-sided
levers (diagonal base + private banks/pulls, as for T_fin).
Proof.  u_k(Delta z') = sum_{j > N} u_k(j) Delta z'_j, and lambda_k ||u_k 1_{(N,inf)}||_1 <= frak_t(N).  QED

So, for an ARBITRARY admissible T, the uniformized NL question reduces to the following, which is precisely the consensus
core "exactness versus one-sidedness" (ADDENDA 13-14), now localized at the de-switching scale:

PROBLEM 3.4 (junction certificate; what a non-density proof along this route must establish).  OPEN.  Find admissible T
(one block suffices), f, g in C(f), rho < 1 such that for every NA f' near f and every g' in C(f') near rho g:
 (J1) g requires persistent switching at f at all small scales with S-oscillation kappa > 0 (so every recovering approximant
      de-switches at some s_*(f') > 0 and must bank S with mass >~ kappa s_*, Theorem 1.4, Corollary 2.8);
 (J2) the first-order corrections needed at the hand-over (re-tuning the switching carriers' normalized values after the
      banks of Prop. 3.2, or an equivalent exact cancellation) lie outside the closed cone generated by the one-sided resources
      available at moderate depth — a Farkas certificate y with y >= 0 on banks / inward moves / pulls and y < 0 on the
      required correction;
 (J3) two-sided resources are too weak: far free moves (Prop. 3.3) and deep carriers cannot supply the correction at the
      required precision ("far rigidity" of T; compatible with Lemma B by N2 (round 2) SKETCH);
 (J4) the scale-invariant mismatch exceeds the slack: a mismatch ratio above delta = (1 - rho^2 kappa)/2 at the hand-over.
Nothing in Parts 1-3 shows (J1)-(J4) can hold simultaneously; nothing excludes it for arbitrary T.  For the designed T_fin
(diagonal base, private levers) (J2)-(J3) fail at finite-support rows (Master Theorem VI).

## 3.3 Numerics (sanity checks only; finite-dimensional SOCP models, CLARABEL)  — N3_work/

 * identity_check.py: the identities |B| -+ zB = (1 - |z|)|B| + 2(zB)_-+ and |x + y| = |x| + sgn(x)y + 2(-sgn(x)y - |x|)_+,
   and the elementary inequalities of Lemma 1.2, on 10^5 random samples: errors <= 1e-15, no violations.
 * sqrt_mu_check.py (+ sqrt_mu_check2.py): 7 coordinates, one block of 6 carriers, diagonal base; S = {1, 2} aligned banks of
   mass m each, j_f = 3 free and exactly visible through one robust peak.  Maximum of Osc_S(g'; psi') over the
   t-discretized fibre (140 scales, |t| in [1e-5, 3.2]):
       m = 0: Osc = 4.9e-5 (grid floor);  m = 1e-7 ... 1e-2: Osc/sqrt(mu_S) = 1.257, 1.239, 1.218, 1.216, 1.217, 1.210.
   The sqrt(mu) law of Corollary 2.4 / Theorem 2.3 holds over five decades with constant 1.22, below the proved constant
   2(2A)^{1/2} = 6.06 (A = 4.59 computed from the formula of Theorem 2.3): the bound is sharp in its scaling.
   Caveat (finite-model artifact): the "maximal aligned contact" comparison also gives Osc = 0 at m = 0, because the finite
   model has no transfer peaks, so shifts are pinned by the lack of rebalancing; finite models cannot show the shift
   mechanism (nor de-switching: Y n c_00 = {0} has no finite analogue).
 * lemma_checks2.py / lemma_checks3.py: on the optimal SOCP decompositions (with g(x') = 0 imposed, as for every mate),
   Lemma 1.2 (a),(b) hold with ratio <= 0.96 on the whole grid; Lemma 2.2 holds with ratio <= 0.32 on t in [1e-3, 3.2]
   (at t <= 3e-5 the budget e ~ t^2/2 ~ 5e-11 is at solver tolerance and the ratio is meaningless).  Without imposing
   g(x') = 0 the discretized optimum has g(xhat') ~ -6e-5, which adds t|g(x')| to the budget (first run, ratios up to 5):
   this is consistent with the proofs, which use g(xi') = 0.

## 3.4 Verdict of the N3 track

 (1) Uniformizing Theorem NL over all NA approximants FAILS, provably at the level of the mechanism: the positive-scale
     profile bound (Theorem 2.3, valid at every row for every mate) is inherited from f (Corollary 2.5) and is defeated in
     every neighbourhood of f by truncation + banks (Theorem 2.6(b): PROVED when f has finitely many free coordinates, which
     covers the self-aligned rows where NL is realized; SKETCH in general).
 (2) What survives is a sharp NECESSARY STRUCTURE of recovering approximants (aligned-or-banked with the quantitative
     threshold of Theorem 2.6(a); de-switching, Theorem 1.4; banks >~ kappa x de-switching scale, Corollary 2.8; migration
     of persistent switching to deep carriers, Corollary 1.5), and the engineered approximants saturate it (Theorem 3.1).
     This is POSITIVE evidence: the conditions are met by an explicit construction whenever the data are exact.
 (3) A non-density certificate along this line would have to be a JUNCTION certificate (Problem 3.4): a first-order Farkas
     obstruction against one-sided levers at the hand-over, combined with the weakness of two-sided far levers
     (Prop. 3.3) — i.e. the same "exactness versus one-sidedness" core that blocks the positive proofs, now localized at the
     de-switching scale.  The failure of the positive programme and a hypothetical negative proof would meet at the same
     point; neither side gains asymmetric evidence from N3.  No candidate (T, f, g) realizing (J1)-(J4) is known.
