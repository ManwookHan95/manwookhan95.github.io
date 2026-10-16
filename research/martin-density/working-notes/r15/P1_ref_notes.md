# P1_ref_notes — referee notes for P1 (round 15, Problem R, negative side): proofs of all fixes and additions

Report: r15/P1_referee.md.  Parts: P1_ref_part1.md (SYM, SYM', P), P1_ref_part2.md (C2, C3, Remark (i)), P1_ref_part3.md
(Prop N, cleanliness, KSB, numerics), P1_ref_part4.md (C3', C2-gen, Prop N').  Scripts: P1_ref_work/ (c2_check.py,
c2_run2.py, c2_debug.py, accuracy_check.py, scaled_model.py, validate_scaled.py, ksb_scaled.py, midcheck.py, midcheck2.py,
r2_dense.py, single_vs_band.py, mf_scaled.py, c3prime_check.py).  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Setting: one block (N = 1), any admissible T (only Part I's forced-data facts and N3's refereed lemmas are used), any row
f' in S_{p*} (norm attaining or not) unless stated.

## Summary of referee results
| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Lemma SYM, Cor SYM', Lemma P (P1) | PROVED (verified) | part 1 |
| 2 | (SYM-int) interval form, (ORD) contact order, (FREE) one-scale form of Lemma P | PROVED (referee) | part 1 |
| 3 | Theorem C2 (P1) | PROVED (verified, numerics) | part 2 §1 |
| 4 | Corollary C3 (P1) with precisions P-C3a/b | PROVED | part 2 §2 |
| 5 | C3 Remark (i) "log^2 rate implies the hypothesis" | INCOMPLETE: (H2) is Z-blind | part 2 §3 |
| 6 | (R1) rate at Z => peak-term hypothesis; (R2) (SIM) => both hypotheses, E° -> 0 | PROVED (referee) | part 2 §3 |
| 7 | Theorem C3' (no hypothesis; Z-local small-margin count SM) and C2-gen (any partition) | PROVED (referee) | part 4 |
| 8 | Proposition N (P1) | PROVED (verified) | part 3 §1 |
| 9 | Proposition N' (dichotomy: deep N'-count >= c_* or infinite small-margin staircase) | PROVED (referee) | part 4 |
| 10 | Lemma CL (conditional cleanliness); single-carrier near-duplicate statement from (FREE) | PROVED (referee) | part 3 §2 |
| 11 | Necessity of symmetric use of deep carriers; "slack cannot absorb the hand-over" | HEURISTIC / OPEN | part 3 §2 |
| 12 | KSB must bank the whole converted band (correction K1) | model evidence (HEURISTIC) | part 3 §3, §5 |
| 13 | "A single clean strict non-peak matches the staircase" (P1) | FALSE at model level (K = 1.5, 1.2) | part 3 §5 |
| 14 | P1's numerics below t ~ 3e-4 | unreliable (violations up to 10.8 e(t)) | part 3 §4 |
| 15 | Canonical truncations converge in the models (P1's "boundary effects") | FALSE (solver artifact) | part 3 §4 |
| 16 | Banked-band KSB converges in all tested models (1 and 2 families, r <= 0.85, K >= 1.2) | HEURISTIC (model) | part 3 §4-5 |
| 17 | KSB recovery in an explicit admissible design; D_anch admissibility; g in C(f) | OPEN | report |

---

# P1 referee — part 1: sources, Lemma SYM, Corollary SYM', Lemma P

Sources re-read: N3 notes (Def 1.1, Lemma 1.2 with proof, Lemma 2.2 with proof, Thm 2.3), N3 referee report and ref notes
(Lemma R-V, Lemma W, Lemma S, Thm 2.3', Lemma R-F, Cor 2.4', Lemma R-W, Prop X, Sec. 7), N1 Prop 1.8, G3 Lemma 1.4,
Part I lem:threshold, eq:margin, prop:forced, lem:bookkeeping, lem:dualball.

Conventions (one block, as in P1): lambda_k = Phi_k, D = diag(Phi_k), N(W) = ||W||_inf + ||DW||_2, zeta' = R** theta',
sigma' = |zeta'|, c' = q**(theta'), c' + sigma' = 1, zeta'/sigma' = alpha' + D^2 w'/C' (lem:threshold), margin identity
sigma'|alpha'(k)| = Phi_k mu'_k (eq:margin).  For a mate g' (g' in C(f')), g'(theta') = 0 (compare theta'(f' +- t g') <=
s(t) as t -> 0+), so N3 Lemma 1.2 applies with e = s(t) - 1 <= t^2/2.  The proof of N3 Lemma 1.2 uses only
q*(a' + tB+) <= 1 + e and N(w' + t Omega+) <= 1 + e (and likewise on side -), so P1's relaxed pair definition ("all four
norms <= 1 + e") is legitimate.  Re-derived: for j notin F', Exc-summand on side + is t[(1-|z'_j|)|B+_j| + 2(z'_j B+_j)_-],
on side - it is t[(1-|z'_j|)|B-_j| + 2(z'_j B-_j)_+]; on F' the anti-sign allowance terms; G_b >= Exc.  Correct.

## 1. Lemma SYM — CORRECT (PROVED)
Case check (j notin F', x = |z'_j|, m = min(|B+_j|,|B-_j|), B+_j B-_j >= 0):
 z'_j = 0: contribution |B+_j| + |B-_j| >= 2m.  Common sign = sgn z'_j: (z'_j B-_j)_+ = x|B-_j| >= xm.  Common sign =
 -sgn z'_j: (z'_j B+_j)_- = x|B+_j| >= xm.  In both cases (1-x)(|B+_j| + |B-_j|) + 2xm >= 2m.  Summing (a) + (b):
 sum 2m <= 2e/(c't).  The constant e/(c't) <= t/(2c') is right.
REFEREE REFORMULATION (PROVED, immediate; recommended as the statement to cite).  Put X+- := L*Omega+- (block parts), so
B+- = g' - X+-.  B+_j and B-_j have opposite signs (or one vanishes) iff g'_j lies in the closed interval I_j with end
points X+_j, X-_j; if they have the same sign, min(|B+_j|,|B-_j|) = dist(g'_j, I_j).  Hence Lemma SYM is EQUIVALENT to
   (SYM-int)  sum_{j notin F'} dist( g'_j , [X+_j, X-_j] )  <=  e/(c't)  (<= t/(2c')),
and also to   sum_{j notin F'} ( |B+_j| + |B-_j| - |V_j| ) <= 2e/(c't),  V := B+ - B- = X- - X+ (switching vector):
off the support the base mass exceeds the switching mass by O(t) only.  On contacts the ORDER is also fixed: from (a),(b),
   sum_{j notin F'} [ (z'_j X+_j - z'_j g'_j)_+ + (z'_j g'_j - z'_j X-_j)_+ ] <= e/(c't)
(side + may only push the block part to the -z side of g', side - to the +z side; this is G3 Lemma 1.4(a) at the level of
the two sides separately).  Relation to the literature: SYM is a corollary of N3 Lemma 1.2 / G3 Lemma 1.4 (same budget);
the interval form is the cleanest way to say "off F' the base is used in switching mode only".

## 2. Corollary SYM' — CORRECT (PROVED), reading needs one qualification
Statement and proof are right (where X+_j = X-_j the interval degenerates).  QUALIFICATION of the reading: SYM' constrains
coordinates where the WHOLE block parts agree.  If at the same scale other carriers are used in switching mode (V_j != 0),
SYM' says nothing there; the correct general statement is (SYM-int): g' lies between the two block parts.  "A carrier
combination used identically on both sides must reproduce g'" is true only on the coordinates where every other carrier
contributes identically to both sides (e.g. the private far coordinates of that combination).

## 3. Lemma P — CORRECT (PROVED)
X^s_i - X^{s'}_2 = B^{s'}_2 - B^s_1 and sum_{J'} (1-|z'_j|)|B^s_i(j)| <= e_i/(c' t_i) <= t_i/(2c') by (a)/(b).  The
part-4 constant (t_1 + t_2)/(2c') (every row) is sharper than the part-1 version ((t_1+t_2)/c', NA rows) — both correct.
REFEREE REFORMULATION (PROVED): Lemma P is a corollary of the one-scale statement
   (FREE)  sum_{j in J'} (1 - |z'_j|) |X^s_t(j) - g'_j|  <=  e/(c't)  <= t/(2c')     (s = +, -),
i.e. on free coordinates every block part at every scale reproduces the MATE itself up to room-weighted O(t).  This is the
form one should use: it says the J'-profile of anything used at scale t is (room-weighted) g'|_{J'} + O(t), without
reference to a second scale.

Status of Part 1 claims: Lemma SYM PROVED; SYM' PROVED (reading qualified); Lemma P PROVED.

---

# P1 referee — part 2: Theorem C2, Corollary C3, Remark (i)

## 1. Theorem C2 — CORRECT (PROVED); every step re-derived
Step 1. (a) gives (1-|z'_i|)|B+_i| <= e/(c't) <= t/(2c') for each i in Z (Z subset J', so i notin F'); the base term follows.
  (Even (1-|z'_j|)|B+_j| + (1-|z'_j'|)|B+_j'| <= t/(2c') jointly; P1's bound is weaker but valid.)
Step 2. Lambda'(psi') = 0, and Lambda'(L*Theta) = sum_k Phi_k Theta(k) ell_k (Lambda' is a combination of two coordinate
  evaluations; the series converges in l_1 since ||u_k||_1 <= 1 and Theta in l_inf).  On P': Theta(k) = -s_k eps_k (w'(k) =
  s_k M').  |L+| <= ||Omega+||_inf <= (2+e)/t, eps_k <= 2(2+e)/t <= 5/t (e <= t^2/2 <= 1/2).  On Q': |w'(k)| < M', so
  |Theta(k)| <= 2(2+e)/t <= 5/t.  For k in P° (alpha'(k) != 0): Phi_k eps_k <= Phi_k e/(t sigma'|alpha'(k)|) = e/(t mu'_k)
  <= t/(2 mu'_k) (N3 Lemma 2.2 + eq:margin; this is N3-ref Lemma W).  Correct.
Step 3. sigma' G(W) <= e follows from c'G_b + sigma'G <= e (first-order terms cancel because g'(theta') = 0 and
  c' + sigma' = 1).  G(W) = [||W||_inf - <alpha',W>] + [||DW|| - <e_w,DW>] with <zeta'/sigma',w'> = M' + C' = 1.  The
  inequality ||X|| - <e_w,X> = ||P_perp X||^2/(||X|| + <e_w,X>) >= ||P_perp X||^2/(2||X||) is right (if ||X|| + <e_w,X> = 0
  then P_perp X = 0).  ||X|| <= ||Phi||_2 ||W||_inf <= (1+e)/sqrt(12) <= 1.5/sqrt(12) = 0.4330.  P_perp X = t P_perp D Omega+.
  Hence ||P_perp D Omega+||^2 <= 2||X|| e/(sigma' t^2) <= 0.434/sigma'.  Correct.
Step 4. P_perp D Theta = P_perp D Omega+; N' and P° partition N (P' = P° u Dg', N' = Q' u Dg').  The identity
  <Y,e_w>(1 - a) = <P_perp Y, e_w 1_{N'}>, a := ||e_w 1_{N'}||^2, gives ||Y||^2 <= ||P_perp Y||^2 (1 - a + a^2)/(1-a)^2
  <= ||P_perp Y||^2/(1-a)^2, and 1 - a = C'^2_{P°}/C'^2 (> 0: supp alpha' = P° is nonempty since ||alpha'||_1 = 1).  Correct.
Step 5. Assembly correct (Cauchy-Schwarz on N' n {Phi >= st}; |Theta| <= 5/t on the deep part, also on Dg').
Numerical sanity check (P1_ref_work/c2_check.py, c2_run2.py; finite anchored model, rows f, truncation, KSB band row; mates
maximizing Lambda' on symmetric grids, pairs taken from the solver at each grid scale): N3 budgets (a),(b) ratios <= 0.95,
Lemma SYM ratio <= 0.53, eps_k <= m_k(t)/Phi_k on P° always, margin identity to 1e-11, C2 bound ratio <= 0.24.  (One
apparent budget violation, ratio 1.8, was traced to an "optimal_inaccurate" solve whose norm constraint was violated by
1.3 e(t); it disappears on scales where the solver is accurate — see part 3 on the reliability of P1's small-scale numerics.)

## 2. Corollary C3 — CORRECT (PROVED), two precisions
 * The proof (s_n := 1/log_2^2(1/t_n); sum_{Phi_k < st} Phi_k <= st(log_2(1/(st)) + 1)) is right; the tail term is
   <= 5 s_n (log_2(1/(s_n t_n)) + 1) max|ell_k| ~ 5/log_2(1/t_n) -> 0.
 * P-C3a: E_inf may be replaced by liminf_n E°(t_n).
 * P-C3b: "In particular ... g' is proportional to psi' on Z" needs psi' not identically 0 on Z (if psi'_j = psi'_j' = 0
   then Lambda' = 0 and nothing follows).  With psi'_j != 0 the conclusion is g'_j' = (g'_j/psi'_j) psi'_j'.

## 3. Remark (i) of C3 (SKETCH "the log^2 rate implies the hypothesis") — INCOMPLETE as stated; referee repair
The hypothesis of C3 has TWO parts: (H1) sum_{P°} m_k(t_n)|ell_k| -> 0, and (H2) E°(t_n) bounded.  (H1) is a condition at
Z; (H2) is Z-BLIND: E°(t)^2 = sum over ALL non-degenerate peaks of min(t/(2mu'_k), 5Phi_k/t)^2, and a cluster of N
non-degenerate peaks with Phi_k in [t,2t] and margins <= t/20 (seeing Z or not) gives E°(t) >= 5 sqrt(N).  So no rate at Z
can imply (H2).  What is true (PROVED here):
 (R1) [rate at Z => (H1)]  Put eta°(mu_0) := sum_{k in P°, mu'_k < mu_0} Phi_k |ell_k|.  If eta°(mu_0) =
   o(mu_0/log^2(1/mu_0)) then (H1) holds along t = (eta°(mu_0) mu_0)^{1/2}, mu_0 -> 0.
   Proof.  Split P° at mu_0.  Margins >= mu_0: m_k <= min(t/(2mu_0), 5Phi_k/t), and N3-ref Lemma S (re-checked: with
   a = t/(2mu_0), b = 5/t, K = ceil(log_2(b/a)) - 1, the sum is <= (K+1)a <= t l(t)/mu_0, l(t) = log_2(1/t) + 2.2) gives
   <= max|ell| t l(t)/mu_0.  Margins < mu_0: m_k <= 5Phi_k/t, total <= 5 eta°(mu_0)/t.  With x := eta°/mu_0 and t =
   (eta° mu_0)^{1/2}: total <= x^{1/2}(max|ell| l(t) + 5), l(t) = (1/2)log_2(1/x) + log_2(1/mu_0) + 2.2, and
   x^{1/2} log(1/x) -> 0, x^{1/2} log(1/mu_0) -> 0 by the rate.  (If eta°(mu_0) = 0 for some mu_0 > 0 let t -> 0
   directly.)  QED
 (R2) [summable inverse margins => (H1), (H2) with E° -> 0]  Since min(x,y)^2 <= xy, m_k(t)^2 <= 5Phi_k/(2mu'_k) and
   m_k(t) <= (5Phi_k/(2mu'_k))^{1/2}, while m_k(t) -> 0 as t -> 0 for each fixed k (mu'_k > 0).  By dominated convergence:
      (SIM)  sum_{P°} Phi_k/mu'_k < infinity  and  sum_{P°} (Phi_k/mu'_k)^{1/2} |ell_k| < infinity
   imply E°(t) -> 0 and sum_{P°} m_k(t)|ell_k| -> 0 as t -> 0 (along every sequence).  Hence under (SIM):
      |Lambda'(g')| <= kappa_2 (C'^2/C'^2_{P°}) ( sum_{k in N'} ell_k^2 )^{1/2}   for every g' in C(f').      (C3-SIM)
   PROVED.  (SIM) is a sparse-small-margin condition for the whole row; it fails for staircases (mu'_k ~ Phi_k at
   infinitely many depths), which is exactly the Problem-R situation at f.
Remark (i) should be replaced by (R1) + (R2) + the sentence "(H2) is independent of any condition at Z".

## 4. Remark (ii) of C3 ("count, not weight") — correct as a statement about the UPPER bound; reading needs care
C3 bounds the oscillation of a mate by the l_2-COUNT of N'-carriers seeing Z, independently of their weights.  This does
NOT say that one deep strict non-peak can carry O(1) oscillation by itself: N3-ref's model (Osc_max ~ 1.14 sqrt(lambda|u|)
for a lone strict non-peak) shows that a LONE carrier of weight lambda carries only ~sqrt(lambda), because the mate
inequality must also hold at scales t >> lambda, where the carrier contributes at most 5 lambda |ell|/t (Theta <= 5/t) and
the base on Z costs ~ t/(c' r).  The O(1) capacity of a deep carrier is available only at scales t <~ Phi_k gamma_k/c_k
(gamma_k = gap); at larger scales another structure must carry the oscillation.  P1's KSB uses exactly this division of
labour (kept staircase above the junction, converted carrier below), so the reading is consistent with KSB but the
sentence "a single deep strict non-peak seeing Z can carry oscillation of order kappa_2|ell_k| at all small scales" must be
read "at all scales below its own coverage scale ~Phi_k gamma_k/c_k".

---

# P1 referee — part 3: Proposition N, cleanliness (5.2), KSB (5.3), the models

## 1. Proposition N — CORRECT (PROVED under its stated hypotheses), with two precisions
Re-derived: (i) j, j' in J(f) are in J'_n for large n (z'_n -> z coordinatewise; a coordinate of F'_n has |z'_n| = 1, so
free coordinates of f can be neither banked nor made contacts by nearby rows); (ii) Lambda'_n(g'_n) -> rho Lambda(g)
(psi'_n -> psi in l_1, prop:continuity; g'_n -> rho g); (iii) C3 at f'_n; (iv) kappa_2(f'_n) -> kappa_2(f) and
C'_{n,P°} >= M'_n Phi_{k_0} for a non-degenerate peak k_0 of f (status continuity: theta'_n(u_{k_0}) -> theta(u_{k_0}),
vartheta'_n -> vartheta, so the margin stays positive); (v) the depth statement: every carrier of a fixed finite set that sees
Z is a non-degenerate peak of f (Problem-R hypothesis), hence of f'_n for large n.
 * P-N1: the uniform hypothesis contains (H2) "E° bounded", which is Z-blind (part 2, §3); "margin-sparse at Z" is a
   misnomer for it.  Under (SIM) at every f'_n with sup_n of the two (SIM) sums finite, E_inf can be taken 0.
 * P-N2: the conclusion is a COUNT lower bound (l_2 of ell over N'_n); it does not say how many scales these carriers cover
   (part 2, §4).  In KSB they cover only the scales below the junction.

## 2. Cleanliness (5.2) — SKETCH is the right label; rigorous core and conditional form supplied
Rigorous core (PROVED, part 1): at every row and scale,
   (FREE)    sum_{J'} (1-|z'_j|) |X^s_t(j) - g'_j| <= e/(c't)          (the block part reproduces the mate on free coords),
   (SYM-int) sum_{j notin F'} dist(g'_j, [X+_t(j), X-_t(j)]) <= e/(c't)  (off the support g' lies between the two block parts),
   (ORD)     sum_{j notin F'} [(z'_j X+_t(j) - z'_j g'_j)_+ + (z'_j g'_j - z'_j X-_t(j))_+] <= e/(c't).
LEMMA CL (referee; conditional cleanliness, PROVED).  Let f'_n be rows, g'_n in C(f'_n), g'_n -> rho g in l_1, t_n in (0,1],
scale-t_n pairs, and b_n -> infinity coordinates with b_n notin F'_n.  Write X+-_n(b_n) = c+-_n v_n(b_n) + R+-_n(b_n) (any
splitting).  If |c+_n - c-_n| |v_n(b_n)| + |R+_n(b_n)| + |R-_n(b_n)| + t_n/c'_n -> 0 (the carrier v_n is used symmetrically
and the rest of the block part is negligible at b_n), then c+_n v_n(b_n) -> 0.
Proof.  By (SYM-int), |g'_n(b_n) - X+_n(b_n)| <= |X+_n(b_n) - X-_n(b_n)| + e_n/(c'_n t_n) -> 0, and |g'_n(b_n)| <=
||g'_n - rho g||_1 + rho|g(b_n)| -> 0 (g in l_1).  Hence X+_n(b_n) -> 0, and c+_n v_n(b_n) = X+_n(b_n) - R+_n(b_n) -> 0. QED
Reading: along a recovering sequence a carrier used symmetrically with coefficient bounded below cannot keep an O(1)
component on an unbanked escaping coordinate.  This is the precise content of "usable deep carriers need their contact
parts on banks".  What is NOT proved (and is the real SKETCH part): that recovering approximants must use their deep
carriers symmetrically at small scales.  N3 Thm 1.4 (de-switching) needs bounded block coefficients, while the deep
carriers have coefficients ~1/Phi_k and other carriers ~1/t; Cor 1.5 only says persistent switching migrates to carriers
outside every finite set.  Also the sentence "the slack cannot absorb the hand-over, since t_* >= 6 eta/(1-rho^2)" uses
N1 Prop 1.8, which is a SUFFICIENT condition (mate inequality automatic for |t| >= t_*); it gives no lower bound below t_*,
so this step is heuristic, not part of a proof.
Also rigorous from (FREE) (referee, PROVED): if at scale t a single carrier k (plus the common mode psi') carries the
block part on J', i.e. X^s_t = c u_k + d psi' + R with sum_{J'}(1-|z'|)|R| <= rho_t, then u_k|_{J'} is within
(room-weighted) (rho_t + e/(c't))/|c| of span{g'|_{J'}, psi'|_{J'}}.  So P1's "near-duplicates on J forced by Lemma P"
(5.3 Data, R3) is a theorem in the single-carrier-per-scale case; with several carriers per scale only the combination
is constrained.

## 3. KSB (5.3) — mechanism sound; one necessary correction; labels HEURISTIC (model) are right
 * Construction check: f'_{L,delta} = grad p(y'), z' finitely supported on the window (Z shifted, kept contacts, banks), so
   f' is NA; a' -> a in l_1 and z' -> z coordinatewise as L -> infinity, delta -> 0, banks -> 0 (prop:approximants).
   Banking b keeps z'_b = z_b, so it does not move any carrier value except through U e' (negligible for a diagonal U
   with tiny entries) and the normalization of a'.  Bank capacity: symmetric use of c u_{k_0} at b with
   contact component c tau/n needs |B+-_b| <= m_b/t on the anti-sign side, i.e. t <= m_b n/(c tau): masses
   m_b ~ Phi_{k_0} suffice for the coverage range t <~ Phi_{k_0} gamma/c.  Cost O(Phi_{k_0}) in l_1.  Correct.
 * CORRECTION K1 (necessary, found numerically, explained by P1's own 2.2(d)): the common shift turns EVERY carrier of
   the family whose value crosses into (-vartheta Phi, vartheta Phi) into a strict non-peak (n_band >= 1 carriers; many
   when margins are small: n_band ~ log((K+1)/(K-1))/log(1/r_family)).  KSB as defined in 5.3 (S),(B) banks only k_0.
   All converted carriers must be banked ((B') bank the contact parts of every carrier of A that the shift makes a strict
   non-peak).  In the referee's well-conditioned model (below) the one-bank version FAILS in dense small-margin
   staircases (distance 0.04-0.17 to rho g, no convergence visible) while the bank-all version converges.
 * Status: KSB recovery of rho g is NOT proved in any admissible design; D_anch's admissibility (Lemma B) and the
   existence of g in C(f) are unproved (model-level only).  No claim of P1 depends on them being proved (P1 claims nothing
   negative), but the positive claim "KSB breaks Problem R" is a HEURISTIC with model evidence, as labelled.

## 4. Reliability of P1's numerics and the referee's re-run (P1_ref_work/)
 * accuracy_check.py: in P1's formulation (constraints q*(A) <= s(t), N(W) <= s(t) with O(1) entries), the solver's
   constraint violations exceed e(t) = s(t) - 1 for t <~ 2e-4 (ratio 10.8 at t = 5e-5, 3.7 at 1.3e-4); the f-grid is
   marginal at 5e-4 (0.31 e(t)).  So P1's approximant-grid scales below ~3e-4 were effectively unconstrained.
 * scaled_model.py: exact EXCESS reformulation (b + R*o = +-g; base and block constraints written as first-order term +
   excess <= e/s, Hilbert parts by rotated cones; all terms O(1) with slack ~ s/2).  Validated against P1's formulation
   on [8e-3, 1] (same optimum 0.162225); independent verification routine (excess_ratio) re-checks a given g at any scale.
 * ksb_scaled.py (P1's run7 setting, rho = 0.9, f-grid [5e-4, 2], approximant grid [5e-5, 2]; all solves "optimal"):
       L = 4:  KSB 0.049 / 0.069,  plain truncation 0.236;
       L = 6:  KSB 0.0070 / 0.0122, plain truncation 0.236;
       L = 8:  KSB 0.0031 / 0.0045, plain truncation 0.233.
   P1 reported plain truncation 0.275, 0.225, 0.041 ("boundary effects"): the decrease at L = 8 was a SOLVER ARTIFACT;
   with correct numerics canonical-type truncations do not approach rho g at all, while KSB distances decrease together
   with ||f' - f||_1 (0.0125, 0.0027, 0.0007 for the better band choice; ratio distance/||f'-f||_1 between 2.6 and 4.5).  Grid bottoms 5e-7 and 1e-9 give the same KSB distances (0.0071, 0.0032).
   The grid optimum violates the mate inequality somewhat below its own grid bottom (ratio 9.8 at grid/10), but the
   distance is unchanged when the grid is extended (0.00321 -> 0.00322), so the finite-model fibre distance is stable.
   Between grid points the KSB optimum satisfies the mate inequality (ratios <= 0.83).
 * r2_dense.py (junction capacity in denser / smaller-margin staircases; f-grid [5e-4,2], approximant grid [5e-6,2]):
       r = 0.75, K = 3:   f Osc 0.185;  KSB (n_band = 1) 0.0076-0.0112; trunc 0.280.
       r = 0.75, K = 8:   f Osc 0.108;  KSB 0.0085-0.0141; trunc 0.135.
       r = 0.75, K = 1.5: f Osc 0.347;  KSB one bank 0.044-0.096 (FAILS); bank-all (2-3 banks) 0.0062-0.0088;
                          trend in L (bank-all): L = 10: 0.013-0.021, L = 14: 0.006-0.009, L = 18: 0.0035-0.0045;
                          trunc 0.57 at every L.
       r = 0.85, K = 1.2: f Osc 0.486;  one bank 0.107-0.172 (FAILS); bank-all (7-10 banks) 0.008-0.010; trunc 0.806.
   Osc(f') of the bank-all rows is 0.74-1.44 times f's (different grids and psi-normalizations; the distance test is
   the meaningful one: bank-all distances are of the order of ||f' - f||_1, ratio 0.3-4.4, and decrease with L).  So P1's "junction capacity favours the
   approximant" survives in the regimes where it was most in doubt (r -> 1, K -> 1), PROVIDED the whole band is banked;
   this is the model-level confirmation of P1's "duality" (small margins <=> wide band <=> many conversions).
These remain finite-model sanity checks (finite models cannot exhibit non-density).

## 5. One converted carrier versus the band (referee numerics; P1_ref_work/single_vs_band.py, r2_dense.py)
 * One-bank KSB at r = 0.75, K = 1.5 does NOT converge: distance to rho g = 0.11-0.15 (L = 10), 0.044-0.096 (L = 14),
   0.042-0.109 (L = 18), 0.050-0.112 (L = 22) while ||f' - f||_1 -> 0 (4.5e-2 ... 6e-4).  Bank-all converges
   (0.013-0.021, 0.006-0.009, 0.0035-0.0045 at L = 10, 14, 18).
 * Pollution or capacity?  With the other converted band carriers DESTROYED (contacts set to 0, so k_0 is the only clean
   strict non-peak) the distance is WORSE (0.097-0.149) than with them left unbanked (0.044-0.109); banked: 0.0035-0.0078.
   So the failure of the one-bank version is a CAPACITY deficiency of a single carrier (the unbanked band carriers help
   only through positive-scale switching, which N3 Thm 1.4 kills as t -> 0 since their coefficients are bounded).
 * Consequences for P1: the sentences "ONE clean deep-kernel strict non-peak per approximant covers all smaller scales"
   (0, 5.3, 5.4) and "a single clean strict non-peak already matches the staircase" (5.4 R2, 2.3 R-ii) are FALSE at
   model level in the small-margin regime; the correct mechanism is the BANKED BAND (all carriers converted by the shift).
   This is consistent with C3'/Prop N' (capacity = l_2-COUNT of N'-carriers seeing Z) and with P1's own "duality"
   heuristic (small margins <=> wide band); the route (R2) to non-density is therefore NOT closed by the models in the
   form "one carrier suffices", only in the form "the band suffices" (all tested regimes, K >= 1.2, r <= 0.85).

---

# P1 referee — part 4: a hypothesis-free version of C3 and the resulting dichotomy (referee additions)

Notation as in C2 (one block, any row f', Z = {j, j'} subset J', Lambda'(h) = h_j psi'_j' - h_j' psi'_j, ell_k = Lambda'(u_k),
m_k(t) = min(t/(2mu'_k), 5Phi_k/t), kappa_2 = (0.434/sigma')^{1/2}, l(t) = log_2(1/t) + 2.2).

## THEOREM C3' (Z-local count capacity, no margin-sparsity or E°-hypothesis).  PROVED.
For mu_0 in (0,1] put P_rob(mu_0) := {k in P° : mu'_k >= mu_0}, N_mu := N \ P_rob(mu_0) (= N' plus the non-degenerate
peaks of margin < mu_0), C'_rob := ||D w' 1_{P_rob}||_2.  Then:
 (a) for every g' in C(f'), t, s, mu_0 in (0,1] with P_rob(mu_0) nonempty,
   |Lambda'(g')| <= (t/2c')(|psi'_j'|/r_j + |psi'_j|/r_j') + max_k|ell_k| t l(t)/mu_0
                    + (kappa_2 + t (l(t)/2)^{1/2}/mu_0) (C'^2/C'^2_rob) ( sum_{k in N_mu, Phi_k >= st} ell_k^2 )^{1/2}
                    + (5/t) sum_{k in N_mu, Phi_k < st} Phi_k |ell_k| ;
 (b) consequently, with SM(mu_0) := sum{ ell_k^2 : k in P°, mu'_k < mu_0, Phi_k >= sigma(mu_0) },
     sigma(mu_0) := mu_0 / ( log_2^2(1/mu_0) log_2^2(1/t(mu_0)) ),  t(mu_0) := mu_0/log_2^2(1/mu_0):
   |Lambda'(g')| <= kappa_2 (C'^2/C'^2_{P°}) ( sum_{k in N'} ell_k^2 + liminf_{mu_0 -> 0} SM(mu_0) )^{1/2}.
Proof.  (a) Repeat Steps 1-5 of C2 with the partition N = P_rob ⊔ N_mu instead of P° ⊔ N'.  The only properties of
N' used in Steps 4-5 were Theta(k) = -s_k eps_k with 0 <= eps_k <= 5/t or |Theta(k)| <= 5/t; they hold on every peak,
in particular on P° \ P_rob.  On P_rob: Phi_k eps_k <= m_k(t) <= min(t/(2mu_0), 5Phi_k/t); by N3-ref Lemma S (re-checked
in part 2), sum_k min(t/(2mu_0), 5Phi_k/t) <= t l(t)/mu_0, so the P_rob-term is <= max|ell| t l(t)/mu_0 and
E_rob^2 := sum_{P_rob} m_k^2 <= (t/(2mu_0)) sum_{P_rob} m_k <= t^2 l(t)/(2mu_0^2).  Step 4 then gives
||Y|| <= (kappa_2 + E_rob) C'^2/C'^2_rob with Y := (D Theta) 1_{N_mu}, since 1 - ||e_w 1_{N_mu}||^2 = C'^2_rob/C'^2.
(b) Take t = t(mu_0), s = 1/log_2^2(1/t).  Then t l(t)/mu_0 = l(t)/log_2^2(1/mu_0) -> 0, t (l(t)/2)^{1/2}/mu_0 -> 0, the base
term -> 0, the tail term <= 5 s (log_2(1/(st)) + 1) max|ell| -> 0 (as in C3), C'_rob(mu_0) increases to C'_{P°}
(monotone convergence; P_rob nonempty for small mu_0 because P° is nonempty), and the l_2 sum over N_mu with Phi_k >= st
is <= sum_{N'} ell_k^2 + SM(mu_0) (st = sigma(mu_0)).  Take liminf over mu_0 -> 0.  QED
Numerical check of (a) (P1_ref_work/c3prime_check.py, anchored model, K = 3 and 1.5, mu_0 in {1e-3,...,1e-1}, all grid
scales): |Lambda'(g')|/bound <= 0.10.
Remarks.  (i) SM(mu_0) counts only Z-SEEING small-margin peaks of weight >= mu_0/polylog; it tends to 0 whenever such
peaks have margins mu'_k >> Phi_k log^4(1/Phi_k) eventually — a Z-local condition.  So C3' contains C3 (with E_inf = 0)
under any such condition and removes the Z-blind hypothesis (H2) entirely.  It is COMPLEMENTARY to N3-ref Cor 2.4'
(neither contains the other: Cor 2.4' tolerates small-margin peaks of weight o(mu_0/log^2) that C3' counts, while C3'
tolerates N'-carriers and small-margin peaks of tiny weight that Cor 2.4' must exclude by its rate).  In particular
P1's sentence "C3 generalizes N3-ref Cor 2.4'" is inaccurate (C3 also needs (H2)); "complements" is correct.
(ii) For an infinite staircase of small-margin peaks seeing Z (mu'_k ~ Phi_k at all depths) SM(mu_0) ~ #{k : mu_0/polylog
<= Phi_k <~ mu_0} -> infinity: the bound is void, as it must be (staircases carry oscillation).
(iii) GENERAL FORM (C2-gen, PROVED by the same proof): for every partition P' = P_1 ⊔ P_2 of the peak set with P_1 a
nonempty subset of P°, C2 holds with P° replaced by P_1, N' by N' ∪ P_2, E°(t) by (sum_{P_1} m_k(t)^2)^{1/2} and
C'_{P°} by ||D w' 1_{P_1}||_2.  C2 (P_1 = P°), C3' (P_1 = P_rob(mu_0)) and mixed choices (keep a small-margin peak in P_1
when its weight is tiny, count it when its weight is >= the scale) are instances; the optimal partition interpolates
between the weight-type bound of N3-ref Thm 2.3' and the count-type bound of C2.

## PROPOSITION N' (dichotomy for recovering NA sequences; replaces Proposition N).  PROVED.
Let f in S_{p*} (one block), g in C(f), rho in (0,1), Z = {j, j'} subset J(f), Lambda(g) != 0, and let f'_n -> f be NA rows
(more generally any rows) with g'_n in C(f'_n), g'_n -> rho g.  Put B := sup_n kappa_2(f'_n) C'^2_n / C'^2_{n,P°} (finite:
kappa_2(f'_n) -> kappa_2(f), C'_n <= 0.29, C'_{n,P°} >= M'_n Phi_{k_0} for a non-degenerate peak k_0 of f) and
c_* := (rho|Lambda(g)|/(2B))^2 / 2.  Then for all large n at least one of the following holds:
 (i)  sum_{k in N'(f'_n)} Lambda'_n(u_k)^2 >= c_*     (strict non-peaks / degenerate peaks of f'_n seeing Z);
 (ii) liminf_{mu_0 -> 0} SM_n(mu_0) >= c_*           (an INFINITE family of small-margin peaks of f'_n seeing Z, with
      margins mu'_k < mu_0 at weights Phi_k >= mu_0/polylog(1/mu_0), at arbitrarily small mu_0).
If moreover no strict non-peak and no degenerate peak of f sees Z (Problem R), the carriers in (i) leave every finite set
(status continuity), and those in (ii) are infinitely many and arbitrarily deep at each f'_n.
Proof.  For large n, Z subset J'_n and |Lambda'_n(g'_n)| >= rho|Lambda(g)|/2 (part 3, §1); C3'(b) at f'_n gives
(rho|Lambda(g)|/2)^2 <= B^2 (sum_{N'_n} ell^2 + liminf SM_n), so one of the two terms is >= c_*.  Depth: as in part 3, §1;
for (ii), a fixed k with mu'_k > 0 drops out of SM_n(mu_0) once mu_0 <= mu'_k.  QED
Reading.  Every recovering sequence must create, near f, DEEP near-kernel structure seeing Z of one of two kinds:
 (i) deep strict non-peaks or degenerate peaks with l_2-count of oscillation profiles >= c_* — the KSB mechanism; or
 (ii) an infinite staircase of small-margin peaks at the approximant itself — the T_PB / nested-tuning mechanism
      (N2 Thm 2.4; P2's far nested tuning).
P1's Proposition N is the special case in which (ii) is excluded by hypothesis.  A negative proof for Problem R must
exclude BOTH alternatives at every NA row near f; (i) is a COUNT condition (one deep carrier with |ell| >~ c_*^{1/2}
suffices), so it cannot be excluded by weight considerations; only the cleanliness/junction constraints (Lemma CL,
(FREE), (SYM-int), and the hand-over at the coverage scale) can discount such carriers.

---

# Part 5 — what remains open (precise)
(O1) KSB as a theorem in one explicit admissible design: (a) Martin's Lemma B for D_anch (injective, norm one, range in
     Y with Y ∩ c_00 = {0}, every tail of (u_k) dense in S_{q*}) — not checked; (b) existence of the switching mate g in
     C(f) with explicit constants (N2 Prop 2.3 with contacts, sign convention z_{b_k} = -1 for both families) — model
     only; (c) at f'_{L,delta} with the whole band banked: a single mate g' close to rho g satisfying the mate inequality
     at (i) scales >= t_* by the slack (N1 Prop 1.8, rigorous), (ii) scales below the band's coverage scale by a two-sided
     certificate built on the banked band (Part I finite-certificate theory at NA rows), (iii) the junction range in between
     by the kept staircase with the shift and the destroyed deep part as perturbations — the only genuinely new step.
     Structural input already available: by (FREE)/(SYM-int) at f, the mates of f are, off F and off the small-scale
     active carriers, proportional to psi up to O(t) — which is why rho g can be close to the certificate space S(f').
(O2) Quantitative band-count vs staircase-capacity comparison for general T (duality: small margins <=> wide band).
(O3) Alternative (ii) of Prop N' (approximants with infinite small-margin staircases at Z) as a positive mechanism, and
     its exclusion in any negative proof.
(O4) Necessity of symmetric use of deep carriers at small scales (de-switching with unbounded coefficients); a two-scale
     cleanliness inequality.
(O5) Problem R (negative) and density of NA((c_0, p_N), l_2^2) for Martin's p: OPEN; no counterexample mechanism.
