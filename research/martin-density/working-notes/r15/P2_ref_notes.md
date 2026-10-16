# P2-ref notes (Round 15, adversarial referee of task P2, second independent pass)

Scope: P2 = r15/P2_notes.md (parts P2_part0_context.md, P2_part1.md, P2_part2.md, P2_part3.md; scripts r15/P2_work/).
An earlier referee pass of P2 stopped before writing a report; its part files are archived in r15/P2_ref_prev/ and were used
only as a cross-check (agreements and disagreements are marked).  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Referee scripts: r15/P2_ref_work/cm_check2.py, dsep_multilinear.py, cor16_check.py (sanity checks only; finite models cannot
exhibit non-density).

## 0. Verdict in one paragraph
P2 makes no density or non-density claim; it is a structural paper on the positive side, and its PROVED claims are almost all
correct.  Part 2: the common-mode identity is exact (Lemma III-identity in disguise); Theorem 2.3(B) is a correct transfer of
Theorem III-Aobs (3)-(4) to G1's restricted model (with G1's Farkas condition correctly renormalized by 1/kappa_m); Cor 2.5(iii)
and Prop 2.6' use the smallness mu*_{s_max(L)+1}^2 << 1/H(L) with an incomplete justification (it needs s_max(L) >~ log_2 L,
which holds for T_fin^{K2} only because absorber targets push s_max(L) up super-exponentially) -- a design-independent
per-carrier repair is given; Prop 2.6' holds WITHOUT its no-thick hypothesis;
Consequence 2.8(ii) (the R-ESC.2 correction) is right and valuable, but 2.8(iii) ("the escape is ALWAYS the common mode")
conflates the Farkas cofactor vector with the mate's switching vector and is NOT proved (a conditional single-minor version
is sketched here); (D-sep) is a genuine design MODIFICATION (T_fin^{K2} violates it through repeated targets), achievable:
qualitatively (exact model) PROVED here, quantitatively SKETCH with (Q) resolvable by an explicit window condition; Theorem
2.10 is correct conditionally.  Part 1: all PROVED claims correct (nested tuning fixed point is a clean, design-independent
tool that answers N3 Section 1.6); minor precisions.  Part 3: all PROVED claims correct except the last sentence of Prop 3.2
("two mates" -> "a finite set of >= 2 mates").  Nothing here changes the joint conclusion of ADDENDUM NEG; the open core is
unchanged except that single-minor (R-S1) persistence at consecutive (R1) main stages is excluded for the (D-sep)-modified
design (in G1's restricted model).

## 0.1 Verdict table (claims as listed in the task)
| Claim | Verdict | Main issue / fix |
|---|---|---|
| Thm 2.3(A) / Lemma 2.7 (common-mode identity) | correct | exact; = Lemma III-identity with D = s_max(L) + support facts; "h_k sum = common mode" true in signed form |
| Thm 2.3(B) (robust negative common mode) | correct (mod chain) | G1 Prop 5.2 needs the 1/kappa_m factor (PR-1, P2 already uses it); bound -(3/4)W per carrier |
| Cor 2.4-2.5 (proportional support, Hilbert localization) | correct with fixable gaps | PR-3: justification of mu*^2 << 1/H(L) incomplete (true for T_fin^{K2} via absorber growth of s_max; per-carrier repair in general); PR-4: ZD clause of 2.4(i) an artifact of unbounded linearization |
| Consequence 2.8 (escape = common mode) | (i),(ii),(iv) correct; (iii) wrong as stated | conflation of Farkas vector and mate switching vector; correct form = obstruction (A) AND mate escape (B); conditional single-minor link SKETCH |
| Prop 2.6' / Cor 2.6 (free-target pairs) | correct (stronger than stated) | no-thick hypothesis superfluous (PR-5); smallness repaired as PR-3 |
| (D-sep) (SKETCH) | SKETCH confirmed, sharpened | design modification (T_fin^{K2} violates it); identically-constant case PROVED; (Q) resolvable by window condition (SKETCH); qualitative version suffices in exact model (PROVED) |
| Thm 2.10 (no persistence of single-minor (R-S1)) | correct (conditional) | PR-6 coordinate range automatic; c_L -> 1 from costs |
| Lemma 1.1 / Cor 1.2 (two-signed requirement) | correct | constant 7/t can be 5/t |
| Prop 1.3 / Cor 1.4 (nested tuning) | correct | PR-7: Cor 1.4 uses diagonal U; general U fixed; monotone margins NOT needed |
| Conversion lemma | correct with fixable gaps | PR-8: smallness relative to |u_k(j)|; j must stay free |
| Prop 1.5 / Cor 1.6 (strict non-peak capacity) | correct | constants verified on 342,000 grid points |
| Prop 1.7 (square precision) | correct | (iii) only through the scale criterion |
| Prop 3.1 (forms of merging) | correct | all five equivalences re-derived |
| Props 3.2-3.3 (fan, automatic merging) | correct with fixable gap | PR-9: last sentence of 3.2 ("two mates") unproved, corrected |
| Prop 3.4 (merging vs (P-I)) | correct | Mazur + Milman |
| Thm 3.6 (placement criterion) | correct | near-tautological given Def 3.5's strength |
# P2-ref (second, independent pass) part 1: Part 2 of P2 against the sources

The earlier, unfinished referee pass is archived in P2_ref_prev/ (P2_ref_part{1,2,3}_prev.md); this pass re-derives
everything independently and only uses those files as a cross-check.  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.1 Sources confirmed (exact references)
- Part III lines 5462-5482: T(L) = union of supports of coarse targets, s_max(L) = max T(L); beyond s_max(L) the only coarse
  carrier nonzero on S_l is l, v_l(s) = delta_l 2^{-s}/n_l > 0 there; N_l = first six elements of S_l cap (s_max(L), inf);
  d(L) = max_l max N_l, H(L) = max_{l<=L} max_{s in N_l} 1/v_l(s).
- Part III Def III-Tfindata / Part II lines 2040-2042, 2462: h_l = sum_{S_l} 2^{-s} e_s^*, S_l = {2^l(2i+1) : i >= 1}
  (pairwise disjoint, gaps 2^{l+1}), delta_l in [delta^max_l/2, delta^max_l], delta^max_l = 2^{-l} for l >= 2 (H_l tiny),
  n_l in [3/4, 5/4], u_l = (y_l + delta_l h_l)/n_l.  So (S1), (S2) of P2 2.0 hold.
- Part III line 5909: U_L := union_{k in Lambda_L} supp u_k (ALL coarse carriers).  Hence J subset U_L automatically, and
  J subset [1, s_max(L)] subset [1, d(L)] subset [1, dbar(L)] (design depth).
- Part III Lemma III-prep (d) (lines 6127-6134): every s <= dbar(L) in U_L is TS, S_th, FR or ZD at the prepared row; Step A
  uses data-carrying S_th coordinates only through raises.  G1 Def 4.1 / Lemma 4.2 (c): same for P^nat with theta_T, theta_pr.
  After (P1)-(P3) there is NO contact and NO tiny-room free coordinate left in U_L at design depth.
- Part III Lemma III-identity (eq. III-identity, lines 5960-5975) and Lemma III-actions (i)-(iii): the identity
  u(xhat) = kappa_u(1 - alpha(D)) + sum_{s<=D} c_s(u) + sum_{s>D} u(s) z_s and the first-order actions
  (mass change: (mu_s^2/nu) D_u(s) dm; z-move: u(s) dz; bank at contact: (mu_s^2/nu) u(s) z_s dm).
- H2 Fact 1.1 (a)-(c) (r13/H2_notes lines 75-89): at an (R1) stage no near coordinate is thick; zero-data tuned carriers are
  kind (i) (two-sided composites); data-carrying tuned carriers are kind (i) or kind (iv), and a kind-(iv) carrier has ALL near
  coordinates S_th of the data sign (banked data-sign contacts or raised data-sign thin support).
- G1 Prop 5.2 (r14/G1_notes lines 344-360): linearized system r^# = rc + sum_P a_l e_l + sum_Q b_l e_l + sum_g c_g dr(g) +
  sum_h e_h dr(h), a, e >= 0, b, c free, <C_{m,i}, r^#(m)> = 0; dr(g) = u^(m)(s)/kappa_m x size + multiple of r^(m).
  G1 writes (b) with D_{m,i}(g) = <C_{m,i}, u^(m)(s)> WITHOUT the factor 1/kappa_m; the correct Farkas condition is
  sum lambda_{m,i} D_{m,i}(g)/kappa_m = 0.  P2's normalization lambda~ = lambda/kappa_m is the right one (precision PR-1).
- G1 Lemma LE (lines 213-229): single-(X3) strict minors are affine in r^(m) with design coefficients, c_M = 0 for inactive
  shifts; nonzero design polynomials >= 1/Des, all <= Des^{1/2} (G1 Section 4, (D-G1a)).

## 1.2 Theorem 2.3 (A): re-derived, CORRECT (exact algebra)
With zhat = z + Ue, e = U^*a/nu, nu = ||U^*a||, ||a||_1 + nu = 1, z = sgn a on F:
   x(zhat) = x(z) + <U^*x, e> = x(z) + kappa_x nu,   Dev_x(z) = x(z) - kappa_x ||a||_1   =>   x(zhat) = kappa_x + Dev_x(z).
Partition N = J u P u Rest (P = union_G P_l, P_l = S_l cap (s_max(L), inf)); V = 0 on Rest, V = C~_l v_l on P_l by (S1), (S2).
Summing Dev_V(s) z_s over P u Rest gives sum_G C~_l sum_{P_l} v_l z - kappa_V ||a 1_{P u Rest}||_1, and
1 - ||a 1_{P u Rest}||_1 = nu + a_J.  Equivalently (one-line form): V(zhat) = kappa_V nu + sum_J V(s) z_s + sum_G C~'_l pi_l.
This is Lemma III-identity with D = s_max(L) plus the support facts; it holds for ANY coefficients (Lemma 2.7 is the same
statement with gamma in place of C~).  Numerical check: P2_ref_work/cm_check2.py (see part 3).

## 1.3 Lemma 2.1, Lemma 2.2: CORRECT
- Lemma 2.1 (i): V(zhat) = sum_l C~_l u_l(zhat) = sum_m kappa_m sum_{l in m} C~_l rc_l = sum_{m,i} lambda~_{m,i} kappa_m M_{m,i}(rc)
  (M linear, c_M = 0).  (ii): linearity of Dev.  CORRECT.
- Lemma 2.2: z_{n_1} = eps_l (Fact 1.1(c)); tail ratio 2^{-2^{l+1}} <= 1/16, tail <= v(n_1)/15; so pi_l >= (14/15) v_l(n_1(l))
  >= (7/8)/H(L) (P2's 1 - 2^{1-2^{l+1}} is a valid weaker bound).  CORRECT.  Precision: the per-carrier bound
  pi_l >= (14/15) v_l(n_1(l)) is the natural one and is needed for the repair PR-3 below.

## 1.4 Farkas derivation (P2 2.0): CORRECT with the normalization of PR-1
Columns: oriented kind-(iv) band variable of row l: C'_{m,i,l} in the rows of block m; two-sided row: C_{m,i,l} (free);
mass change at s in F: (eff_s/kappa_m) <C_{m,i}, Dev^(m)(s)>; z-move off F: <C_{m,i}, u^(m)(s)>/kappa_m; raise: z_s times the
mass column.  Farkas for {a, e >= 0, b, c free : A x = -M(rc)} gives exactly (a)-(c) with lambda~ = lambda/kappa_m.  The
-r^(m) dkappa_m/kappa_m part of each action multiplies every M_{m,i} by a common factor (homogeneity, c_M = 0) and is dropped.
Kernel removal: C~ = Phi(lambda~) is block-diagonal, C~^(m) = (C^(m))^T lambda~^(m); a basic preimage has entries that are
ratios of design minors, so ||lambda~||_1 <= Des^C ||C~||_1 and (a)-(c) depend on lambda~ only through C~.  CORRECT.
Scope remark: (a) gives a sign only on kind-(iv) and two-sided columns; a column with no freedom at all (locked rows) is outside
the restricted model (class (R-L)).  P2's "G consists of kind-(iv) rows" is correct INSIDE the model.

## 1.5 Theorem 2.3 (B): CORRECT (mod chain), with precision PR-2
Each s in J is TS (Dev_V(s) = 0), data-carrying S_th (raises only: z_s Dev_V(s) >= 0), or FR (V(s) = Dev_V(s) = 0).
[ZD is an overlapping label at design depth: a ZD coordinate in J is also a coordinate of a data-carrying carrier of G, and
after (P1)-(P3) it is TS, S_th or FR.]  So sum_J Dev_V z >= 0, sum C~' pi >= (7/8)||C~||_1/H(L), and
0 < V(zhat) <= beta kappa_max ||lambda~||_1 <= beta kappa_max Des^C ||C~||_1; (2.2), (2.3) follow.
PR-2: the bound kappa_V <= -(3/4)||C~||_1/H(L) is what the argument gives; P2 states the weaker -||C~||_1/(2H(L)).  Better
(per carrier): kappa_V <= -(3/4) W, W := sum_G |C~_l| v_l(n_1(l)) >= ||C~||_1/H(L).

## 1.6 JUSTIFICATION GAP in Cor 2.5 (iii) and Prop 2.6' ("for L large"); condition true for T_fin^{K2}; repaired (PR-3)
P2 needs mu*_{s_max(L)+1}^2 <= nu^2/(16 H(L)) and justifies it by "mu* is doubly exponential".  That alone does not suffice:
delta_l >= 2^{-l-1}, n_l <= 5/4 give H(L) ~ 2^{L + s_max(L) + 12 * 2^L} up to constants (for the youngest carrier l = L,
N_L = {3, 5, ..., 13} x 2^L when s_max(L) < 3 * 2^L, so H(L) >= (4/5) 2^{L + 13 * 2^L}), while mu*_{s_max(L)+1}^2 =
2^{-2^{2^{s_max(L)+1}+1}} is small against 1/H(L) only if 2^{s_max(L)+1} >~ L + 4, i.e. s_max(L) >~ log_2 L.  Main targets
alone would not give this ((D-enum): main targets of round <= r+1 are supported in [1, r+1]).
(a) For T_fin^{K2} the condition DOES hold: by Def III-Tfinrounds every PRE/CLUSTER absorber target of stage l has support
{s, p_0, ..., p_R} with p_0 < ... < p_R the least odd integers > max(9, max T(l-1)) and R(l) >= 2 log_2(1/mu_{p_0}) + 5, so
max T(l) >= max T(l-1) + 2R(l) and s_max grows super-exponentially along absorber stages; at least two thirds of all stages
are absorber stages (each round: one main stage, R_cl(p) = 2|E^ch(p)| >= 2 cluster stages).  Hence s_max(L) >= L for L large
and the smallness holds (for the base 2^{-s^2-1} of T_fin as well).  So P2's conclusion is right for its design; only the stated
reason is incomplete.  (b) Design-independent REPAIR (PROVED; needed for Lemma 2.7-type statements "for any design with the
structure of 2.0"): compare per carrier.  For l in G the private non-near coordinates s in P_l \ N_l satisfy s > n_6(l) > s_max(L), so
   sum_{s in P_l \ N_l} mu_s^2 |V(s)| |a_s| <= |C~_l| (mu*_{s_max(L)+1})^2 (16/15) v_l(n_6(l)) <= 2 (mu*_{s_max(L)+1})^2 |C~_l| v_l(n_1(l)),
and the S_th coordinates contribute at most 2b ||C~||_1 <= 2b H(L) W.  With the per-carrier Theorem 2.3(B), kappa_V <= -(3/4) W:
   sum_{s in J cap TS} mu_s^2 |a_s| |V(s)| >= nu^2 W (3/4 - (2 b H(L) + 2 (mu*_{s_max(L)+1})^2)/nu^2) >= (5/8) nu^2 W
as soon as 2 b H(L) + 2 (mu*_{s_max(L)+1})^2 <= nu^2/8, which DOES hold for L large: b(w) H(L) -> 0 (window thresholds lie
below every level-L design constant, and H(L) <= Des(L)), and s_max(L) -> infinity (every pool target occurs).  Since
W >= ||C~||_1/H(L), Cor 2.5 (iii) holds with constant 5/8 >= 1/4.  Prop 2.6' is repaired identically (see 1.7).

## 1.7 Prop 2.6' and Cor 2.6: CORRECT after PR-3; the no-thick hypothesis is SUPERFLUOUS (PR-5, PROVED)
One-line form with lambda~ = sigma/kappa_m: V(zhat) = sigma M(rc) = kappa_V nu + sum_{J \ {j}} V(s) z_s + sum C~'_l pi_l.
Alignment (eps_l u_l(s) z_s >= 0 for all s <= s_max(L), s != j, thick or not) gives V(s) z_s >= 0 on J \ {j} and
V(s) a_s = |a_s| z_s V(s) >= 0 on J cap F; near private coordinates give V(s) a_s = C~'_l v_l(s) |a_s| >= 0; the remaining
private coordinates give kappa_V nu >= -(2/nu) (mu*_{s_max(L)+1})^2 W.  Hence sigma M(rc) >= W (14/15 - 2 (mu*_{s_max(L)+1})^2/nu)
>= (3/4) W >= (3/4)(|u_+(j)| + |u_-(j)|)/(H(L) kappa_m) for L large (s_max(L) -> infinity).  Thick ALIGNED coordinates help.
So the correct reading: a free-target pair has a tiny minor only if some coordinate s <= s_max(L) is ANTI-ALIGNED
(eps_l u_l(s) z_s < 0 for some l); thick coordinates of an obstruction are of this kind for V (V(s) z_s = kappa_V |a_s| < 0).
P2's own proof (via (2.1)) has a harmless slip: kappa_V (nu + a_J) >= -(mu*)^2 ||C~||_1 (nu + a_J)/nu^2 (not /nu); irrelevant.
Numerics (P2_ref_work/cm_check2.py (2)): 2016 instances with thick aligned target support, min sigma M/W = 2.21 >= 3/4.
Cor 2.6 (no thick coordinate below s_max(L) in the group => not (R-S1)) follows from repaired Cor 2.5 (iii).  CORRECT.

## 1.8 Cor 2.4: (ii), (iii) CORRECT; (i) correct for TS, precision PR-4 for the "zero-data S_th/ZD" clause
(ii) and the TS part of (i) re-derived: at a two-sided mass generator s in F, Dev_V(s) = 0, i.e. V(s) = kappa_V a_s != 0, so
s in supp V; an anchor (thick s notin U_L) would force kappa_V = 0.  This is Theorem III-Aobs (4) transferred to G1's model.
PR-4 (scope).  P2 augments G1's generator list by ZD composite moves ("they only add constraints").  For necessary conditions
this is harmless only if every added generator really acts at the Step-A scale.  A two-sided generator at a zero-data S_th
coordinate s outside supp V acts on the minors only through the common mode, with coefficient eff_s |kappa_V| |a_s|
~ theta/Des, and its lowering range is <= theta/2; the required change is ~ beta = (1 + 2 Lip) b >> theta^2/Des.  So in the
bounded realization it is not a lever, and the clause "(i) ... zero-data S_th/ZD ... s in supp V" is an artifact of the
UNBOUNDED linearization.  Everything else (Theorem 2.3(B), Cor 2.4(ii), Cor 2.5, Cor 2.6, Prop 2.6') holds in G1's own model
(FR, TS, one-sided raises) WITHOUT the augmentation: those proofs use only Dev_V = 0 at TS, V = 0 at FR, z Dev_V >= 0 at raises
on J.  Fix: drop the ZD augmentation (or restrict it to generators with design-sized two-sided action) and state (i) for TS.

## 1.9 Lemma 2.7 and Consequence 2.8
- Lemma 2.7 (2.4): CORRECT (re-derived; it is (2.1) with gamma for C~).  The second claim, read in signed form,
  sum_G gamma_k <U^*u_k, e> = kappa_{V^G} nu, is exact (numerics (3): error 9e-16).  R-ESC's h_k are absolute values,
  h_k = sum_s |u_k(s)| mu_s^2 |a_s|/nu, and only bound this signed sum: sum_G gamma_k <U^*u_k, e> >= -sum |gamma_k| h_k.
- 2.8 (i): CORRECT (mate-side reading of (2.4); notation clash: V there is the block switching vector, not Def 2.0's V).
- 2.8 (ii): CORRECT and VALUABLE.  R-ESC (3) stays true, but R-ESC.2's "c_k >= N_k - U_far(k) - h_k >= c/H(L) (mod chain)" is
  unjustified: a kind-(iv) carrier with a target at a Hilbert-dominant support coordinate s_0 has h_k >= |u_k(s_0)| mu_{s_0}^2
  |a_{s_0}|/nu, of order |u_k(s_0)| mu*_{s_0} (e.g. 1/16 at s_0 = 1), astronomically larger than N_k ~ 6/H(L).  Numerics (3):
  sum |gamma| h_k/sum |gamma| up to 0.51.  Corrected escape list of R-ESC.2: shared support (E(t)), outside switching,
  other strict non-peaks, AND the mate's common mode kappa_{V^G} < 0 (Hilbert-visible support of the group's carriers).
- 2.8 (iii): OVERREACH (NOT PROVED as stated).  The "escape" of ADDENDUM 14b / R-ESC is a property of the MATE's switching
  coefficients gamma_k at the active scales; Theorem 2.3 is a property of the FARKAS cofactor vector C~ at R_1.  These are
  different vectors and P2 proves no link.  What is proved: (A) [obstruction] the cofactor combination has kappa_V <=
  -||C~||_1/(2H(L)), carried by thick group support with V = kappa_V a there; S_th/FR/contact/thin coordinates and outside
  switching cannot create this negative balance.  What a residual stage needs in addition: (B) [mate] an escape from the
  CORRECTED list of 2.8(ii) for the switching vector V^G; nothing excludes G-THIN, outside switching or other strict non-peaks
  from (B).  Correct statement of 2.8(iii): "(R-S1)+escape residual = (A) and (B)".
  Conditional link (SKETCH, referee).  At a single-minor stage whose FR submatrix A (rows: FR rows of M; columns: G) has full row
  rank |G| - 1, the cofactor vector C_M spans ker A (repeated-row identity A C_M = 0).  Lemma 1.4(c) at an FR row j (room >= u/2)
  gives |V_j| <= 2 t/(q_0 u) for the TOTAL switching V_j = V^G(j) + psi_j, so gamma|_G = c C_M + delta with
  |delta| <= Des^C (t/(q_0 u) + Psi_J), Psi_J := sum_{FR rows} |psi_j| (outside carriers).  Active coefficients satisfy
  |gamma_l| >= (5/6) K_*(w)^2 K t with K = C_f (Des/u)^C (Part III Lemma III-track), so the t/(q_0 u) part is negligible
  provided K_*(w)^2 K >> Des^{C'}/(q_0 u) (C' the pseudo-inverse exponent of the FR submatrix); this can be arranged by
  enlarging the class threshold K_*(w) (a monotone insertion) but is not checked against Lemma III-count.
  Hence: if Psi_J <= (u/Des)^{C'} K t, gamma|_G is parallel to C_M up to a negligible relative error, the orientation (a)
  forces sgn c = sgn lambda~, and kappa_{V^G} = (c/lambda~) kappa_V (1 + o(1)) < 0: the mate's escape IS the common mode,
  as P2 asserts.  Otherwise the escape is outside switching at the minor's FR rows (an R-ESC escape).  So at single-minor
  stages the dichotomy "common mode through thick group support OR outside switching at FR rows" is available (SKETCH:
  the transfer of the start-row FR rows of R_1 to the decomposition rows at the active scales is not checked); G-THIN and
  other strict non-peaks are not excluded as ADDITIONAL escapes, and at multi-minor stages no link is available.  The
  unconditional identification in 2.8(iii) remains NOT PROVED.
- 2.8 (iv): CORRECT but tautological (the Farkas conditions (b') say no generator acts on lambda~^T M).
# P2-ref (second pass) part 2: Prop 2.9, (D-sep), Theorem 2.10

## 2.1 Proposition 2.9: CORRECT as a necessary condition (mod chain)
(i) H2 Lemma 2.7(b) (r13/H2_notes lines 170-189): a kind-(iv) carrier at an (R1) main stage p is INACTIVE (zero-data) at the
next main stage p' when p' is (R1).  Groups consist of data-carrying kind-(iv) carriers, so G_L cap G_L' = {}.  CORRECT.
(ii)-(iii) Cor 2.4(ii) at each stage; the base bookkeeping a^(L)|_A = c_L a(f)|_A is exact: on a fixed finite set A of thick
coordinates the only operations preceding Step A are the common renormalization (raises act on thin support, banks on
contacts, closings are z-moves, TU base banks sit at near coordinates, which are private and not thick at (R1) stages, deep
raise/truncation act beyond dbar(L)).  c_L -> 1 by the cost bounds (Lemma III-costs; [I, prop:continuity]).  CORRECT (mod chain).
(iv) V_L = sum_{m,i} lambda~_{m,i} V_{M_{m,i}} by Definition 2.0.  CORRECT.

## 2.2 Theorem 2.10, step (1): CORRECT
r_L - a_s/a_s' = (a_s' e(s) - a_s e(s'))/(a_s' V_L(s')), so |r_L - a_s/a_s'| <= 2e/(a_A |kappa_L| a_A/2) <= 8 H(L) e/a_A^2 with
|kappa_L| >= 1/(2H(L)) (||C~||_1 = 1), |a^(L)_x| >= a_A (c_L >= 1/2), e = Des(L) eps(w_L), a_A^2 >= u(w_L); then
<= 8 E_L/Des(L)^{C_1 - 1} <= E_L/64 for Des >= 2^9.  Both stages: |r_{M_L} - r_{M_L'}| <= E_L/32 (E nonincreasing).

## 2.3 Theorem 2.10, step (2): CORRECT after precision PR-6 (PROVED)
PR-6 (coordinate range).  (D-sep) is stated for s, s' <= s_max(B), but A = {s, s'} is fixed while B may be small.  The range
condition is automatic: every carrier of G_{M_L} u G_{M_L'} is born at a stage <= B, so its target lies in T(B) subset
[1, s_max(B)]; if s > s_max(B), then V_{M_L}(s) != 0 forces s in S_l for some l in G_{M_L}, and V_{M_L'}(s) != 0 forces s in S_l'
for some l' in G_{M_L'}; the S's are pairwise disjoint, so l = l', contradicting G_{M_L} cap G_{M_L'} = {}.  (Same for s'.)
[Agrees with the earlier pass, P2_ref_prev R-3.]  The case analysis Tau(B) = E_prev(B) >= E_L is correct.

## 2.4 (D-sep) is a design MODIFICATION, not a property of T_fin^{K2} (PROVED)
Def III-Tfinrounds (r.1): Y_r := y^{(i_nu)} with nu counting the rounds of block m and (i_nu) taking every value infinitely
often; so EVERY block contains infinitely many carriers l != l' with the same target y (and the fallback y^{(1)} recurs).
For two coordinates s, s' of supp y outside all signature sets (Z_0 = odd numbers and powers of 2), u_l(s)/u_l(s') =
y(s)/y(s') = u_l'(s)/u_l'(s') exactly, so the pseudo-minors {l}, {l'} (disjoint groups) have EQUAL slopes and (D-sep) fails.
This case is not empty: a 1x1 strict minor M = -r_l (tiny value) gives a single-carrier obstruction, and by Theorem 2.3 /
Cor 2.4 its thick profile is proportional to y; a row f with a|_thick proportional to y|_thick is not excluded by the slope
argument for singleton groups {l} at L, {l'} at L'.  So Theorem 2.10 needs the modification; P2's achievability sketch does
perturb target values, but P2 never states that the unmodified design violates the clause.
Admissibility of the modification: choose the perturbed main target IN Y_pool with the same support (Y_pool is dense among
rational directions with a given support).  Then allowedness (a), (c+) (support conditions), (D-enum) (supports), Lemma B
(perturbations -> 0, every pool element still approached in every block), and the field k_0 of GEN (generated by ALL pool
values, delta(y,l), n(y,l)) are unaffected.  Absorbers: route V gives absorbers no switching coefficient (Part III Lemma
III-CMp and the paragraph after it: "absorbers carry no switching coefficient: they are ordinary fine carriers"), so they are
never in a group G (zero-data columns get C~ = 0 by (a)); (D-sep) need only cover minors whose groups consist of main carriers.

## 2.5 The genericity argument (P2's SKETCH): the identically-constant case is CORRECT (PROVED by the referee)
Let M' have the new carrier l_0 (born at B) in G_M', FR submatrix A' = [a_0 | A_old] (a_0 = u_{l_0} on the FR rows), and s, s'
not in supp u_{l_0}.  Then C_{M',l_0} = +-det A_old (independent of a_0), and for l != l_0 the cofactors are linear in a_0, so
by multilinearity V_M'(x) = <a_0, w(x)>, w_j(x) = +-V_{M''_j}(x), where M''_j is the old minor (X3 row, FR rows minus j, columns
G_old).  Hence r_M'(s, s') is constant in a_0 iff w(s) is parallel to w(s'), i.e. r_M' = r_{M''_j} for every j with w_j != 0:
an OLDER minor with group contained in G_M' \ {l_0}, which is disjoint from G_M; (D-sep) for (M, M') is then (D-sep) for
(M, M''_j), imposed at an earlier stage with Tau >= Tau(B) (only one new carrier per stage, so birth(M) < B).
If s in supp u_{l_0} (s is not an FR row of M' because V_M'(s) != 0), V_M'(s) = (1/n)(C_{M',l_0} y(s) + <y|_FR, w(s)>) and
V_M'(s') = (1/n) <y|_FR, w(s')>: the factor 1/n = 1/q^*(y + delta h) CANCELS in the slope, which is affine in t := y(s) with
nonzero slope C_{M',l_0}/<y|_FR, w(s')>; the bad set {t : |r_M' - r_M| < Tau} has length <= 2 Tau K_B, K_B <= Des(B-1)^C.

## 2.6 The quantifier point (Q): resolvable by an explicit window condition (SKETCH, referee)
P2's (Q) Tau(B) K_B N_B < delta_B is NOT automatic (Tau(B) = E_prev(B) is fixed before stage B).  But for MAIN-carrier
minors everything needed is known before the windows of the previous main stage p: l_{r+1} = p_r + R_cl(p_r) with
R_cl(p) = 2|E^ch(p)| fixed after (S1) of stage p; the next main stage p' = l_{r+1} + 2|Sigma(y)| + 1, its candidate
y = y^{(i_nu)} and allowedness are combinatorial; its signature S_p', delta_p' (GM: y, H_p', delta^max_p') and n_p' follow.
The intervening PRE/CLUSTER absorbers (whose targets depend on lb_l, i.e. on b(p, M(p)), T_lo(p, M(p))) are zero-data and do
not enter main-carrier minors (main carriers vanish at absorber-only coordinates).  Hence K_p', N_p' are computable at stage p
before its windows, and the extra window condition
      E_p <= 2^{-p'} / (2 K_p' N_p')      (equivalently u(w) small enough for every sub-window w of p)
makes (Q) hold with delta_p' := 2^{-p'}.  Window thresholds of a stage may be chosen below any quantity known at that point
(monotone insertion, U4 Lemma GW).  [SKETCH: compatibility with the pigeonhole ladders Q(w), b(w), u(w) not re-checked line by
line; the earlier pass's two-pass recursion does NOT work as stated, because absorber lengths R(l) depend on windows and change
T(.), hence the stage numbering; only main-carrier data are window-free, which is what the window condition above uses.]

## 2.7 Simplification: in the EXACT restricted model only a qualitative clause is needed (PROVED, referee)
In G1's restricted model the obstruction is an exact Farkas vector at R_1, so Cor 2.4(ii) gives V_L = kappa_L a^(L) EXACTLY on
thick design-depth coordinates, and a^(L)|_A = c_L a(f)|_A exactly (2.1).  Hence r_{M_L}(s,s') = a_s(f)/a_s'(f) = r_{M_L'}(s,s')
EXACTLY, and Theorem 2.10 (exact model) follows from the qualitative clause
   (D-sep_0)  r_M(s,s') != r_M'(s,s') for all potential main-carrier minors with disjoint groups and all s != s' with the four
              values nonzero,
achieved by a countable genericity argument (2.5: at each stage finitely many proper algebraic conditions on the new target
values, avoided inside Y_pool) with NO quantifier issue.  The quantitative clause (2.6) is needed only for the near-certificate
(robust) version with |V_L(x) - kappa_L a_x| <= Des(L) eps(w_L).

## 2.8 Verdict on Theorem 2.10
CORRECT as a conditional statement: PROVED modulo (D-sep) [a genuine design modification, achievable: qualitative version
PROVED by the referee (2.5, 2.7) in the exact restricted model; quantitative version SKETCH (2.6)] and the chain (memory
Lemma 2.7(b), bookkeeping, G1's restricted model).  Precisions PR-6 (coordinate range automatic) and c_L >= 1/2 (costs -> 0).
Scope: it excludes only single-minor (R-S1) at two CONSECUTIVE (R1) main stages; alternation with other residual classes,
multi-minor stages and shifted blocks remain (P2 Remark 2.11, correctly labelled OPEN).

## 2.9 Referee remark: a generic-f form of the slope rigidity (PROVED in G1's exact restricted model)
Let Sl be the set of all slopes r_M(s, s') = V_M(s)/V_M(s') of potential single-(X3) strict minors M (all stages, blocks,
column sets, FR-row sets, coordinate pairs with V_M(s') != 0).  Sl is countable and f-independent (design data only).  At an
exact single-minor (R-S1) stage, Cor 2.4(ii) and 2.1 give a_s(f)/a_s'(f) = r_{M_L}(s, s') for EVERY pair of thick design-depth
coordinates.  Hence: if a(f) has two support coordinates with a_s(f)/a_s'(f) notin Sl (true off a countable union of
hyperplanes {a_s = r a_s'}), then NO large (R1) main stage of f is single-minor (R-S1)-residual -- no design clause needed.
Theorem 2.10 is the version for ALL f, at the price of (D-sep) and of consecutiveness.  Multi-minor stages give
a|_A in span{V_{M_i}|_A}, a nontrivial constraint only when |A| exceeds the number p_L of simultaneously tiny minors, which is
not bounded (P2 Remark 2.11(a)).
# P2-ref (second pass) part 3: Part 1 of P2 (Problem R, positive side)

Sources used: N3 Def 1.1, Lemma 1.2, Lemma 2.2 (neg/N3_notes lines 102-130, 268-288); N3-ref Lemma W, Lemma S, Lemma R-W
(neg/N3_ref_notes lines 35-45, 107-110); Part I def:certificate (paper/martin_density_note.tex 723-760), lem:slack (864),
prop:scale (880), prop:approximants, prop:continuity, prop:smooth.

## 3.1 Lemma 1.1 (oriented profile identity): CORRECT (PROVED)
Re-derived: on peaks Omega+(k) = s_k (L+ - eps+_k) and Omega-(k) = s_k (L- + eps-_k) are the DEFINITIONS of eps+-_k (>= 0 because
L+ is a sup and L- an inf over ALL peaks, degenerate ones included); psi' = M' sum_P lambda s u + sum_Q lambda w' u gives
sum_P lambda s u = (psi' - sum_Q lambda w' u)/M'; substituting into g' = B+- + L* Omega+- gives (1.1) with d+- = -L+-/M'.
Absolute convergence: coefficients <= 2(2 + e)/t, sum lambda_k ||u_k||_1 < infinity.

## 3.2 Corollary 1.2 (two-signed requirement): CORRECT (PROVED); constant precision
Dividing (1.1) at j and j' and subtracting cancels d+- psi' exactly.  The sign split is right: in the "+" expression the peaks
with s_k D_k > 0 contribute <= 0, in the "-" expression those with s_k D_k < 0 do.  Budget: N3 Lemma 1.2(a),(b) with e <= t^2/2
gives (1 - |z'_i|)|B+-_i| <= t/(2 q'_0) (even jointly over i in {j, j'}), so |b+-| <= A t/2.  Lemma W: lambda eps <= m_k(t).
Strict non-peak coefficient: |Omega+-(k) + d+- w'(k)| <= ||Omega||_inf + |L+-| |w'(k)|/M' <= 5/t (P2's 7/t is valid, not sharp).
(iii): for each fixed mu_0 the class sum is <= D_bar t l(t)/mu_0 + 5 eta(mu_0)/t (Lemma S on the margins >= mu_0, 5 lambda/t on
the rest, degenerate peaks included); t = (eta mu_0)^{1/2} and the log^2 rate give |Delta| -> 0.  Since (i) and (ii) both hold
whatever sigma is, "EITHER set {s_k D_k > 0} or {s_k D_k < 0} satisfies the rate" suffices.  Refines N3-ref Lemma R-W (which
bounds the unoriented mass; degenerate peaks of R-W are absorbed into the classes here, each contributing to eta at every mu_0).

## 3.3 Proposition 1.3 (nested tuning fixed point): CORRECT (PROVED)
- z'(tau) in B_{c_0}, z' = sign a' on supp a'; tau -> z'(tau) is continuous from the product topology into (c_0, sup) because
  sup_i |tau_i - tau'_i| <= max(max_{i<I} |tau_i - tau'_i|, 2 sup_{i>=I} tau_bar_i) and tau_bar_i -> 0.
- [I, prop:smooth(c)]: q(y') = 1 and f'(tau) = grad p(x'(tau)) attains its norm at x'(tau); f', vartheta' continuous
  ([I, prop:smooth(b)], prop:continuity).
- <y', u_{k_i}> = N_i + tau_i m_i + X_i(tau) with X_i a uniformly convergent series (sum_l |u_{k_i}(s_l)| <= ||u_{k_i}||_1).
  Gamma_i(tau) := ((A_i vartheta' Phi + B_i) p - N_i - X_i)/m_i is continuous and |Gamma_i| <= tau_bar_i by (1.2).
- K compact convex in the locally convex space R^N; Schauder-Tychonoff gives tau* = Gamma(tau*).  Types by the threshold
  lemma in pairing form (peak iff |u_k(x')| >= vartheta' Phi_k; off peaks |w'(k)| = M' |u_k(x')|/(vartheta' Phi_k)).  N_i is
  defined with the FULL pairing <U^* u_{k_i}, e'>, so the proposition holds for general U.

## 3.4 Corollary 1.4: CORRECT (PROVED) after precision PR-7 (general U); one earlier precision withdrawn
- (a) Uniform far freedom by contradiction from [I, prop:approximants] ((ii) => (i)): CORRECT.  vartheta_bar: use any a priori
  bound (vartheta' <= vartheta + 1 near f), so the case vartheta = 0 is harmless.
- (b)-(d) arithmetic re-derived: |beta_i| <= 1/2, c'_i in [1/2, 25/16], m_i >= m_low, |N_i| <= 2 eps'_i, c_i <= 2 eps'_i,
  (1.2) with total 3/4 tau_bar_i m_low.
- PR-7 (diagonal U is used).  "Lambda(e_c) = sign a'(c) + mu_c^2 a'(c)/||U^*a'||" and "|N_i| = |Lambda(u_{k_i} 1_W)|" use a
  DIAGONAL U with supp a' subset W (then <U^*u, e'> only sees supp a').  For a general compact dense-range U (the claim is for
  EVERY admissible T): (1) choose c in supp a' with a'(c) (U U^* a')(c) > 0 (exists: sum_c a'(c)(UU^*a')(c) = ||U^*a'||^2 > 0),
  so |Lambda(e_c)| = 1 + |(Ue')(c)| >= 1; (2) N_i acquires sum_{s notin W} u_{k_i}(s)(Ue')(s), whose main part is
  (1/(2c'_i))(Ue')(s_i); choose s_i beyond the point where |Ue'| <= eps'_i (Ue' in c_0), then |N_i| <= (2 + 1/(2c'_i) + ||U||)eps'_i
  and (1.2) holds with eps'_i reduced by a factor 2.  FIXED.
- The margin sequence need NOT be monotone (the earlier pass's precision P1-mono is unnecessary): for mu_0 in (0, mu_1] let i
  be maximal with mu_i >= mu_0 (exists since mu_i -> 0); then mu_{i+1} < mu_0 <= mu_i <= lambda_{k_{i+1}} and
  eta(mu_0) >= d_0 lambda_{k_{i+1}} >= d_0 mu_0.  (Within each class, with the interleaved subsequence.)
- "Answers N3 Section 1.6": N3 1.6 states that existence of non-C-tame NA rows near a given f for a given T is OPEN; C-tame
  means finite Q' u Dg' and (MS) at x' (N3 Prop 1.7).  Cor 1.4 with A_i = B_i = 0 gives infinitely many strict non-peaks with
  u_k(x') = 0 (Q' infinite) near EVERY f for EVERY admissible T.  CORRECT in P2's stated setting (N3's one-block setting
  I = {1}); with several blocks the proof only uses the threshold lemma of the block containing the k_i, whose threshold
  vartheta'_m is continuous along the family, so it extends verbatim (referee: SKETCH-level remark, not needed for P2's claim).

## 3.5 Conversion lemma (Remark (c)): CORRECT (PROVED) with precision PR-8
F(delta) := s_k u_k(x'(delta)) - A vartheta'(delta) Phi_k, F(0) = (1 - A) vartheta' Phi_k + mu_k in [0, mu_k + 2 vartheta' Phi_k];
dF/d delta = s_k (u_k(j) - u_k(x'(delta)) dp/d delta)/p - A Phi_k d vartheta'/d delta; with p <= 3/2 the slope is <= -|u_k(j)|/2 in
the chosen direction provided (vartheta' Phi_k + mu_k)(1 + |u_k(j)| delta_1)C + Phi_k omega(delta_1) <= |u_k(j)|/8, delta_1 :=
4(mu_k + 2 vartheta' Phi_k)/|u_k(j)|, and |z'_j| + delta_1 < 1 (j stays free).  IVT gives the root.  PR-8: "Phi_k, mu_k small"
must be read RELATIVE TO |u_k(j)| as displayed, and the free-room condition must be stated.  Side effects on other margins:
|u_l(j)||delta| + |u_l(x')||p(delta) - p(0)| + Phi_l |Delta vartheta'|: CORRECT.

## 3.6 Proposition 1.5 and Corollary 1.6: CORRECT (PROVED)
Prop 1.5 from def:certificate with D = diag(Phi), R^* e_k = lambda_k u_k, lambda_k = Phi_k (one block): ||D omega||^2 = theta^2 C',
d = theta Phi_k w'(k)/C'^{1/2}, H = theta^2 (1 - Phi^2 w'^2/C'^2), r and kappa as stated; under Phi_k <= C'^{3/2}/4 the gap term
is the binding radius (the other two exceed it by a factor >= C'/(Phi^2) >= 16/C'^2).
Cor 1.6: H <= 1/2, kappa <= C'^{1/4}/8 <= 1/2, r_0 = r(c) in [1.005, 1.01] (gamma Phi)^{1/2} <= 1/6, p^*(g) <= theta C'^{1/2}(1 +
Phi/C') = r_0/2.02 exactly by the choice of theta; (s(t) - 1)/t increasing; size theta C'^{1/2} >= (gamma Phi)^{1/2}/2.02.
Numerics (P2_ref_work/cor16_check.py, 342,000 parameter points): max H = .0025, max kappa = .0038, max r_0 = .054,
max(p^* bound - r_0/(s(r_0)+1)) = -5e-11 (tight by design), min size ratio = .495, gap term binding (ratio >= 4.6).
Reading: this is the LOWER bound of the sqrt-weight law at a fixed row; together with P1's C2/C3 upper bound the law is two-sided.

## 3.7 Proposition 1.7: CORRECT (PROVED), (iii) only through the scale criterion
(i): Z eventually off supp a'_n (z'_n -> z coordinatewise, |z| < 1 on Z), so b'_n = 0 on Z; on Z, g_{c'} = sum_{S_n} lambda omega' u -
d' psi'_n; Osc bound; N3 Lemma 2.0(a),(b), psi'_n -> psi in l_1, ||.||_1 <= 3 p^*: Osc >= kappa/2.  A fixed k in S_n infinitely often
gives |u_k(xi)| <= vartheta Phi_k (weak* convergence of normers, vartheta'_n -> vartheta): a strict non-peak or degenerate peak of f
seeing Z, excluded.  (ii): coordinatewise radius r <= gap'/(2|omega'(k)|) <= 1/(2|omega'(k)|).  (iii) restates the hypotheses of
[I, prop:scale] (a sufficient criterion); it says nothing about recoveries certified otherwise (transport, averaging, staircases).
Remark 1.8 and the junction problem are correctly labelled HEURISTIC / OPEN.  [Heuristic check: with N carriers of weight
lambda, gap gamma', coefficients omega and additive conversion costs N lambda gamma', the scale criterion needs
N lambda >~ kappa^2/gamma' (P2's conclusion); if conversion costs did not add, the requirement would only be N >~ kappa/(gamma'
lambda)^{1/2}, compatible with N lambda -> 0.  So Remark 1.8's impossibility rests on additivity of conversion costs.]
# P2-ref (second pass) part 4: Part 3 of P2 (finite merging)

Sources: N1 Def 1.1, Prop 1.2, Lemma 1.4, Thm 1.9 (neg/N1_notes lines 101-175, 277-300); N1-ref Lemma R-M (neg/N1_ref_notes
lines 69-90); Part I prop:approximants, prop:primal, thm:compact, prop:intrinsic(c).

## 4.1 Proposition 3.1: CORRECT (PROVED), all five equivalences re-derived
(a)<=>(b): members of A(f) lie in Rec(f) (N1 Prop 1.2(b)), so Rec(f) in A(f) contains every member; conversely iterate (b) over
the members containing g_1, ..., g_k and recover all along the sequence defining the common member.
(a)=>(c): along f_n with C(f_n) -> Rec(f) (Hausdorff), each attaining f_n has Rec(f_n) = C(f_n) in A(f_n) (constant sequence),
and lim_H C(f_n) is contained in Li C(f_n).  (c)=>(a): two-step eps/2 argument (finitely many g_i, so one n works for all).
(a)=>(d): support functions are p(x)-Lipschitz in the Hausdorff metric, r~_{f'}(x) = max over C(f') of x ([I, prop:primal]).
(d)=>(a): Blaschke limit A of a bad subsequence has h_A >= h_f = h_K on a dense set, hence everywhere (p-Lipschitz), so K in A
by weak* separation with x in c_0; thus K in Li C(f_n) in Rec(f), Rec(f) = K is convex, and every cluster set equals Rec(f).
(d)<=>(e): diagonal choice over a dense sequence; p-Lipschitz dependence on x.

## 4.2 Proposition 3.2: CORRECT except the last sentence (precision PR-9)
U_NA(f) compact convex symmetric, conv(U_NA u {g}) in the member A containing g, fan/star-shape: re-derived.
PR-9.  "A failure of merging needs two mates outside U_NA(f) that lie in no common member of A(f)" is NOT proved: failure of
directedness gives a FINITE set {g_1, ..., g_k} (k >= 2) contained in no single member (Blaschke: if every eps-merging held for
the set, a cluster set would contain all g_i); pairwise containment in members does not give joint containment (no Helly
property is known for A(f); e.g. the closed family {conv(0, g_1, g_2), conv(0, g_2, g_3), conv(0, g_1, g_3)} is pairwise but
not triple-wise covering).  Mates of U_NA(f) can be removed from a failing set (every member contains them).  Correct form:
"a failure of merging needs a finite set of at least two mates outside U_NA(f) contained in no single member of A(f)".
[Agrees with the earlier pass.]

## 4.3 Proposition 3.3: CORRECT (PROVED)
(a) constant sequence; (b) Hausdorff continuity of C at f gives C(f) in U(f), so U(f) = A = Rec(f) = C(f) for every member;
(c) Rec(f) = U_NA u (Rec \ U_NA) in A in Rec(f); (d) cl Cert^sh(f) in U(f) in Rec(f) in C(f) ([I, prop:intrinsic(c)], N1 Prop
1.2(b)) forces equality (the conclusion of (b), not membership in Omega, which P2's wording "(b) applies" slightly misstates).

## 4.4 Proposition 3.4: CORRECT (PROVED; (iv) an abstract remark, correctly labelled)
(i) Mazur (closed convex hull of a norm-compact set is norm compact) + Milman (ext(cl conv K) in K for compact K with compact
closed convex hull).  (ii), (iii) immediate with Lemma R-M.  (iv) the disk/diameters family is Hausdorff-closed, so the
abstract statement is right; whether mate fibres can realize it is correctly OPEN.

## 4.5 Definition 3.5 / Theorem 3.6: CORRECT (PROVED); Remark 3.7(a) CORRECT
Theorem 3.6 re-derived: c by the intermediate value theorem (q^*(P) <= (1 + ||U||) eta < 1 at c = 0), |c - 1| <= 3(1 + ||U||) eta,
||a' - a||_1 <= (5 + 3||U||) eta < eta(delta), z' = z on [1, W], so p^*(f' - f) < delta (N1 Lemma 1.4); for each i the other patterns
lie in N \ ([1, W_i] u R_i), where Definition 3.5 allows arbitrary z' and l_1-small a' - a; pattern i is placed beyond pattern
i - 1 using the "for every W_1 >= W_g" clause.  Remark 3.7(a): violating rows with W_g = n, eta_g = 1/n converge to f
([I, prop:approximants]); a Blaschke cluster set A of their fibres has dist(g, A) >= eps, so g notin U_NA(f).
Scope: Definition 3.5 is very strong (robustness against ARBITRARY far data and l_1-small base changes elsewhere), so Theorem
3.6 is close to a reformulation; its value is as a target.  Remarks 3.7(b)-(d) and 3.8 are HEURISTIC/elementary, correctly
labelled; Remark 3.8 is a one-line consequence of the pairing form of the threshold lemma.
# P2-ref part 5: what remains open, most valuable idea, numerics

## 5.1 Open (precisely)
1. Multi-minor (R-S1) stages: a|_A in span{V_{M_i}|_A : i <= p_L} is a constraint only if |A| > p_L; p_L unbounded.  A span
   version of (D-sep) plus a bound on simultaneously tiny strict minors per stage: OPEN.
2. Alternating/non-consecutive residual stages ((R-S2), (R-S3), (R-L), (R0^str) in between) and shifted blocks
   (term -kappa_m c_M in Lemma 2.1(i)): OPEN.
3. Mate-side escape (B) of 2.8(iii): OPEN beyond the conditional single-minor link of 1.9 (needs the transfer of start-row FR
   rows to the decomposition rows at the active scales and K_*(w)^2 K >> Des^{C'}/(q_0 u)).
4. (D-sep) quantitative: compatibility of E_p <= 2^{-p'}/(2 K_p' N_p') with the window ladders (Q(w), b(w), u(w),
   Lemma III-count): SKETCH; absorbers zero-data: mod chain (Lemma III-CMp).
5. Problem R positive: the junction problem (OPEN); slack-only impossibility (Remark 1.8) HEURISTIC (rests on additivity of
   conversion costs).
6. Finite merging (P-II) at every f: OPEN; far-locality of tuned/KSB/engineered recoveries HEURISTIC.
7. Density of NA((c_0, p), l_2^2) (designed T or any admissible T): OPEN; no 2-dimensional counterexample to property B.

## 5.2 Single most valuable idea
SLOPE RIGIDITY: the exact common-mode identity forces the cofactor combination of an (R-S1) Farkas obstruction to be exactly
proportional to the base on thick design-depth support (V = kappa_V a, kappa_V robustly negative), so f's thick ratios must
equal DESIGN slopes of the resonant minor; consecutive (R1) stages have disjoint groups, so generic (pool) target values forbid
persistence -- qualitatively in the exact model, and for f off a countable union of hyperplanes no single-minor (R-S1) stage
occurs at all.  Runner-up: the Schauder-Tychonoff nested tuning (Prop 1.3 / Cor 1.4), a design-independent tool showing that an
adversarial T can never prevent tuning, only limit the precision of available shapes relative to their weights.

## 5.3 Numerics (sanity checks only; scripts in r15/P2_ref_work/)
- cm_check2.py: identity (2.1) and one-line form max error 4.4e-15 (3000 models); Prop 2.6' with thick aligned coordinates,
  min sigma M/W = 2.21 (2016 instances); signed Hilbert sum = kappa_{V^G} nu to 8.9e-16, unsigned R-ESC sum up to 0.51 per |gamma|.
- dsep_multilinear.py: V_M'(x) = +-<a_0, w(x)>, w_j = +-V_{M''_j}(x), max error 2.8e-14 (2000 instances).
- cor16_check.py: Corollary 1.6 constant chain on 342,000 parameter points (max H .0025, max kappa .0038, max r_0 .054,
  p^* bound tight by design (-5e-11), min size ratio .495, gap term binding).
