# P1_ref_notes (second, independent referee pass) — Problem R, negative side: small-margin peaks at free coordinates

Report: r15/P1_referee.md.  Parts (this pass): r15/P1_ref_part1.md (SYM, SYM', P, C2), P1_ref_part2.md (C3, Remark (i),
Prop N, first pass's C3'/N'), P1_ref_part3.md (cleanliness; Theorem C2-T / Corollary CL-T at C-tame rows; KSB; numerics),
P1_ref_part4.md (comparison with the first pass; the one-bank failure located at the junction; open list).
Scripts (this pass): r15/P1_ref_work/rb_c2_check.py, rb_model_faithful.py, rb_count_capacity.py (+ rb_count_capacity_lib.py),
rb_junction.py, rb_junction2.py, rb_representability.py; outputs rb_*_out.txt / rb_rerun_*.txt.  The first referee pass
(11 Oct) is preserved unchanged in r15/P1_ref_prev/ (report, notes, parts, scripts).
Setting: one block (N = 1), any admissible T (only Part I forced-data facts, Part I thm:tamefibre / prop:lowerbound and
N3's refereed lemmas are used), any row f' in S_{p*} (norm attaining or not) unless stated.  Labels: PROVED / SKETCH /
HEURISTIC / FALSE / OPEN.  Numerics are finite-model sanity checks only (finite models cannot exhibit non-density, and they
lack the rigidity Y n c_00 = {0}; see 3.4).

## Summary table (verdicts on P1's claims, then additions)
| # | Statement | Verdict / status | Where |
|---|---|---|---|
| 1 | Lemma SYM | CORRECT (PROVED); equivalent interval form (SYM-int) | 1.1 |
| 2 | Corollary SYM' | CORRECT (PROVED); applies where the WHOLE block parts agree; general form (SYM-int) | 1.2 |
| 3 | Lemma P | CORRECT (PROVED); corollary of the one-scale (FREE) | 1.3 |
| 4 | Theorem C2 | CORRECT (PROVED), all 5 steps re-derived; optional sharper Step-4 factor (1 + C'^2/C'^2_{P°})^{1/2}; independent numerics ratio <= 0.134 | 1.4, 3.4 |
| 5 | Corollary C3 | CORRECT with fixable gaps: psi'|_Z != 0 for "in particular"; liminf E°; "generalizes Cor 2.4'" -> "complements" | 2.1 |
| 6 | C3 Remark (i) (log^2 rate implies hypothesis, SKETCH) | WRONG as stated: (H2) "E° bounded" is Z-blind and can fail along every t -> 0; the rate implies only (H1) | 2.2 |
| 7 | Proposition N | CORRECT under its hypothesis (which contains the Z-blind (H2)); superseded by Prop N' (first pass, re-derived) | 2.3, 2.4 |
| 8 | Cleanliness of usable deep carriers (SKETCH) | SKETCH label right.  PROVED exactly at C-tame NA rows (Cor CL-T, new) and under symmetric use (Lemma CL, first pass); the "O(t_k)" precision is HEURISTIC (rigorous: O(t) + O(Phi_B/t), i.e. O(Phi^{1/2})); slack sentence HEURISTIC and unnecessary | 3.1, 3.2 |
| 9 | KSB recovery (HEURISTIC, model) | label right; bank every converted carrier (first pass K1, reproduced at nA = 30, absent at nA = 20); failure of one bank is a JUNCTION effect, not capacity; bank the contact-oscillation set if pi_g is non-constant on kept contacts | 3.3, 4.2 |
| 10 | D_anch admissibility, g in C(f) | not claimed by P1; admissibility routine (SKETCH via N2 Lemma 2.1); g in C(f) model-only | 4.3 |
| 11 | THEOREM C2-T (new): at C-tame NA rows w/o degenerate peaks, g' = sum_{Q'} Phi omega' u - d' psi' off F', ||D omega'||^2 <= C'/(sigma'(1-a')), |Lambda'(g')| <= (C'/(sigma'(1-a')))^{1/2} ||ell 1_{Q'}||_2 | PROVED (from Part I thm:tamefibre + prop:lowerbound) | 3.2 |
| 12 | COROLLARY CL-T (new): along C-tame recovering sequences the used strict non-peaks reproduce rho g + d psi off F'_n in l_1 with bounded D-coefficients | PROVED | 3.2 |
| 13 | Junction precision O(t) + O(Phi_B/t) on J' (new) | PROVED | 3.1(ii) |
| 14 | Model faithfulness: KSB optimum needs no switching below ~Phi_band | numerics | 3.4 |
| 15 | One-bank failure localised to the junction window [1e-3, 5e-3]; C2-T capacity of one carrier exceeds target (ratio 0.68) | numerics (HEURISTIC) | 4.2 |
| 16 | Problem R (negative); density | OPEN | 4.4 |

---


# P1 referee (second independent pass) — part 1: Lemma SYM, Corollary SYM', Lemma P, Theorem C2

Note on files. A first referee pass on P1 exists (written 11 Oct, 14:47). Its files were preserved unchanged in
r15/P1_ref_prev/ (P1_referee.md, P1_ref_notes.md, P1_ref_part0..4.md, P1_ref_work/). This pass re-derives everything
independently and then compares with the first pass (part 4). Scripts of this pass: r15/P1_ref_work/ (files prefixed rb_).

Setting (as in P1 part 4): one block, lambda_k = Phi_k = 2^{-1-k} q*(Te_k) <= 2^{-1-k} (k >= 1), so ||Phi||_2^2 <= 1/12;
a row f' in S_{p*} (NA or not) with normer theta' in S_{p**}, forced data c' = q**(theta'), a', F' = supp a', z',
w' = J(zeta'), zeta' = R** theta', sigma' = |zeta'|, M' + C' = 1, alpha', P', Q', margins mu'_k (k in P'),
Dg' = {k in P' : alpha'(k) = 0}, P° = P' \ Dg', N' = Q' u Dg', psi' = L* w' = sum_k Phi_k w'(k) u_k,
J' = {i notin F' : |z'_i| < 1}, room r_i = 1 - |z'_i|.  g' in C(f'), t in (0,1], e = s(t) - 1 <= t^2/2 <= 1/2.

Inputs re-checked against the sources (all refereed):
 (L1.2) N3 Lemma 1.2 (a),(b) at every row (proof re-read: uses only [I, lem:bookkeeping(a),(b)], g'(theta') = 0 and
        q_0 + sigma = 1; the intermediate inequality c' G_b(A) + sigma' G(W) <= e holds on each side).
 (L2.2) N3 Lemma 2.2 at every row: Omega+(k) = s_k (L+ - eps_k), 0 <= eps_k, and eps_k <= e/(t sigma' |alpha'(k)|) when
        alpha'(k) != 0.  For DEGENERATE peaks the representation with eps_k := L+ - s_k Omega+(k) >= 0 holds by the
        definition of L+ as a supremum over P' (no upper bound from the margin) — P1 uses exactly this.  Correct.
 (MAR)  [I, eq:margin] with m = 1: sigma' |alpha'(k)| = lambda_k mu'_k = Phi_k mu'_k.  Re-derived from [I, lem:threshold]
        (zeta(k)/|zeta| = alpha(k) + Phi_k^2 w(k)/C on P, signs equal).  Correct.
 (BK-c) [I, lem:bookkeeping(c)]: G(W) = sum_P |alpha'(k)| (||W||_inf - s_k W(k)) + (||DW||_2 - <DW, Dw'>/C'), both >= 0.

## 1.1 Lemma SYM — CORRECT (PROVED)
Re-derivation.  For i notin F' with B+_i B-_i >= 0 and m_i := min(|B+_i|, |B-_i|) > 0, both entries are nonzero with a
common sign; with x = |z'_i| the joint contribution of i to the left sides of (a) and (b) is
(1-x)(|B+_i| + |B-_i|) + 2(z'_i B+_i)_- + 2(z'_i B-_i)_+ >= 2(1-x) m_i + 2 x m_i = 2 m_i
(if the common sign equals sgn z'_i the term (z'_i B-_i)_+ = x|B-_i| >= x m_i is present; otherwise (z'_i B+_i)_- =
x|B+_i| >= x m_i; if z'_i = 0 the first term alone is >= 2 m_i).  All other contributions are >= 0, so
sum 2 m_i <= 2e/(c't).  QED.  Valid at every row (normer in the bidual), with F' possibly infinite.
EQUIVALENT FORM (useful, PROVED): with X+-_i := (L*Omega+-)(i), one has B+-_i = g'_i - X+-_i, and B+_i B-_i >= 0 iff g'_i
lies outside the open interval between X+_i and X-_i, in which case min(|B+_i|,|B-_i|) = dist(g'_i, [X+_i ^ X-_i, X+_i v X-_i]).
Hence (SYM-int):  sum_{i notin F'} dist(g'_i, conv{X+_i, X-_i}) <= e/(c' t) <= t/(2c').
Reading: off the support, the mate lies (up to O(t) in l_1) BETWEEN the block parts used on the two sides.  This is the
precise content of "only switching usage off F'": the base absorbs g' - X+ and g' - X- with opposite signs.
NOTE (scope): SYM bounds the MINIMUM of the two usages; one-sided heavy usage (|B+_i| large, B-_i ~ 0) is NOT excluded by
SYM — on contacts it is allowed with the contact sign on side + (and the opposite sign on side -), on free coordinates it is
priced by the room (budget (a),(b)).  P1's reading "base can only be used in switching mode" is accurate in this sense.

## 1.2 Corollary SYM' — CORRECT (PROVED), trivial from SYM
If X+_i = X-_i =: X_i then B+_i = B-_i = g'_i - X_i and min = |g'_i - X_i|.  Summing over such i notin F' gives the claim.
(SYM-int) is the general form (no exact agreement needed): wherever the block parts of the two sides are within delta_i of
each other, sum dist(g'_i, X+_i) <= e/(c't) + sum delta_i.

## 1.3 Lemma P — CORRECT (PROVED), and it is a two-scale corollary of a ONE-scale statement
(FREE)  sum_{i in J'} r_i |g'_i - (L*Omega^s)(i)| = sum_{J'} r_i |B^s_i| <= e/(c't) <= t/(2c')   (s = +, -),
which is just the J'-part of (a)/(b).  Lemma P follows by the triangle inequality: block parts at two scales (either sides)
agree on J' up to (t_1 + t_2)/(2c'), room-weighted.  (P1 part 1, 1.3 states the weaker constant (t_1+t_2)/c' at NA rows;
part 4 the sharper one at every row; both correct.)  Lemma P adds nothing beyond (FREE); in later uses (cleanliness) the
relevant statement is (FREE) itself: at EVERY scale the block part reproduces g' on free coordinates up to O(t).

## 1.4 Theorem C2 — CORRECT (PROVED).  Every step re-derived.
Step 1 (base on Z): r_i |B+_i| <= t/(2c') for i in Z (from (a)); |Lambda'(B+)| <= (t/2c')(|psi'_j'|/r_j + |psi'_j|/r_j').
  [Optional sharpening: since r_j|B+_j| + r_j'|B+_j'| <= t/(2c') jointly, the base term can be replaced by
  (t/2c') max(|psi'_j'|/r_j, |psi'_j|/r_j').]
Step 2 (block identity): Theta := Omega+ - (L+/M') w' is bounded; L*Omega+ = (L+/M') psi' + L*Theta, Lambda'(psi') = 0, so
  Lambda'(L*Omega+) = sum_k Phi_k Theta(k) ell_k (absolutely convergent: |Theta| <= 5/t, |ell_k| <= |psi'_j| + |psi'_j'|).
  On P': Theta(k) = -s_k eps_k (w'(k) = s_k M'); 0 <= eps_k <= |L+| + ||Omega+||_inf <= 2(2+e)/t <= 5/t
  (||Omega+||_inf <= (||w'+tOmega+||_inf + M')/t <= (2+e)/t).  On Q': |Theta(k)| <= ||Omega+||_inf + |L+| <= 5/t.
  On P°: Phi_k eps_k <= e/(t mu'_k) (by (L2.2) and (MAR)) <= t/(2 mu'_k), and <= 5 Phi_k/t; so Phi_k eps_k <= m_k(t).
Step 3 (l_2 control): X := D(w' + tOmega+); P_perp X = t P_perp D Omega+ (Dw' is parallel to e_w := Dw'/C');
  ||X|| - <e_w, X> >= ||P_perp X||^2/(2||X||) and ||X|| <= ||Phi||_2 ||W||_inf <= 1.5/sqrt(12) < 0.434; with
  sigma' G(W) <= e <= t^2/2 (from (L1.2)) and (BK-c): ||P_perp D Omega+||_2^2 <= 0.434/sigma' = kappa_2^2.
Step 4: P_perp D Theta = P_perp D Omega+.  Y := (D Theta)1_{N'}, Y° := (D Theta)1_{P°} (N' and P° partition N),
  ||Y°|| <= E°(t), ||P_perp Y|| <= kappa_2 + E°(t).  With a := ||e_w 1_{N'}||^2 = 1 - C'^2_{P°}/C'^2 < 1 (P° nonempty since
  ||alpha'||_1 = 1, and Phi_k > 0 by injectivity of T): <Y, e_w>(1 - a) = <P_perp Y, e_w 1_{N'}>, hence
  ||Y|| <= ||P_perp Y||/(1 - a) = ||P_perp Y|| C'^2/C'^2_{P°}.  Correct.
  [Optional sharpening (PROVED): since Y vanishes on P°, 0 = (P_perp Y)1_{P°} + <Y,e_w> e_w 1_{P°}, so
  |<Y,e_w>| <= ||P_perp Y||/(1-a)^{1/2} and ||Y|| <= ||P_perp Y|| (1 + C'^2/C'^2_{P°})^{1/2}; this is better than P1's
  factor C'^2/C'^2_{P°} as soon as C'^2/C'^2_{P°} >= 1.62, i.e. in exactly the regime where the factor matters.]
Step 5 (assembly): split sum_k Phi_k Theta(k) ell_k over P°, {k in N' : Phi_k >= st}, {k in N' : Phi_k < st}; bound by
  sum m_k |ell_k|, Cauchy–Schwarz ||Y|| ||ell 1_{N', Phi>=st}||_2, and (5/t) sum Phi_k |ell_k|.  Correct.
Scope check: valid at every row f' (no tameness, no finiteness of F', K', Q'); Z must lie in J' (both rooms > 0);
s in (0,1] arbitrary.  The constant 0.434 uses k >= 1 (||Phi||_2^2 <= 1/12); with k >= 0 replace 0.434 by 0.87.
What C2 does NOT use: the gaps of strict non-peaks.  A sharper per-carrier bound holds (not needed by P1): for k in Q' with
gap gamma'_k = M' - |w'(k)|, |W(k)| <= ||W||_inf forces, up to the alpha'-bracket of (BK-c), Phi_k|Theta(k)| <~
Phi_k (gamma'_k + O(t L+))/t; so a strict non-peak carries O(1) in the l_2 term only at scales t <~ Phi_k gamma'_k
(this is the "t_k ~ Phi_k gamma_k/c_k" of P1 5.2; HEURISTIC as stated, not needed).
Numerical sanity check: see part 3 (independent finite model, script rb_c2_check.py).

---

# P1 referee (second pass) — part 2: Corollary C3, Remark (i), Proposition N; first referee's C3', N'

## 2.1 Corollary C3 — CORRECT (PROVED), with the two precisions already noted by the first referee
Re-derivation.  C2 at t = t_n, s = s_n := 1/log_2^2(1/t_n).  Tail: sum_{k : Phi_k < st} Phi_k <= sum_k min(2^{-1-k}, st)
<= st(log_2(1/(st)) + 1) (checked including the edge case K_0 = 1, i.e. st > 1/4, where the sum is <= 1/2 <= the bound);
|ell_k| <= |psi'_j| + |psi'_j'| (as ||u_k||_inf <= q*(u_k) = 1); so the tail term is <= 5 s_n (log_2(1/(s_n t_n)) + 1)
max|ell| = O(1/log(1/t_n)) -> 0.  Base term -> 0; peak term -> 0 by hypothesis; the l_2 sums increase to
sum_{N'} ell_k^2 (monotone in s_n t_n -> 0); (kappa_2 + E°(t_n)) <= kappa_2 + E_inf.  Limit gives the claim.  Correct.
Precisions (required, cosmetic): (i) E_inf may be replaced by liminf_n E°(t_n); (ii) "in particular g' is proportional to psi'
on Z" needs psi'|_Z != 0 (if psi'_j = psi'_j' = 0 then Lambda' = 0 identically).
Additional precision (this pass): the sharpened Step-4 constant of part 1 gives C3 with C'^2/C'^2_{P°} replaced by
min{C'^2/C'^2_{P°}, (1 + C'^2/C'^2_{P°})^{1/2}}.

## 2.2 Remark (i) of C3 ("the log^2 rate implies the hypothesis", SKETCH) — the SKETCH is WRONG as stated
The hypothesis has a Z-local part (H1) sum_{P°} m_k(t_n)|ell_k| -> 0 and a Z-BLIND part (H2) sup_n E°(t_n) < infinity.
(H2) involves no ell_k at all: E°(t)^2 = sum over ALL non-degenerate peaks of min(t/(2mu'_k), 5Phi_k/t)^2.  A peak with
Phi_k >= t/5 and margin mu'_k <= t/2 contributes >= 1 to E°(t)^2 whatever it sees; a peak with mu'_k << t << Phi_k
contributes up to (t/2mu'_k)^2.  Example (failure along EVERY t -> 0): peaks at all depths with margins mu'_k = Phi_k^3 and
geometric weights; for t ~ Phi_k^2 the term of k is min(1/(2Phi_k), 5/Phi_k)^2 ~ 1/(4t), and the windows (2Phi_k^3, 5Phi_k)
cover (0, t_0); so E°(t) -> infinity, whatever these peaks see.  [Only the part of E° coming from Phi_k <= t is always
O(log(1/t))^{1/2}.]  A rate condition at Z (the log^2 rate of N3-ref Cor 2.4') constrains only peaks seeing Z, hence never
implies (H2).  What IS true (re-derived, agrees with first referee's (R1)): the log^2 rate at Z implies (H1)
(split P° at mu_0, N3-ref Lemma S for margins >= mu_0, (5/t) times the near-kernel weight for margins < mu_0, t := (eta
mu_0)^{1/2}).  Correct verdict: Remark (i) must be restated as "(H1) follows from the log^2 rate at Z; (H2) is an
independent, Z-blind condition"; or replaced by the hypothesis-free C3' (2.4 below).
Consequence for P1's sentence "C3 generalizes N3-ref Cor 2.4'": INACCURATE.  Cor 2.4' needs no (H2), C3 needs it; and
conversely C3 tolerates N'-carriers (counted) that Cor 2.4' excludes by its rate.  "Complements" is correct.

## 2.3 Proposition N — CORRECT (PROVED under its hypothesis); every step re-derived
 (i) Z subset J'_n for large n: z'_n -> z coordinatewise (prop:approximants) and |z_j|, |z_j'| < 1; a coordinate of F'_n has
     |z'_n| = 1 (z' = sgn a' on supp a'), so for large n neither j nor j' is a support/bank or contact coordinate of f'_n.
 (ii) Lambda'_n(g'_n) -> rho Lambda(g): psi'_n -> psi in l_1 (prop:continuity: L*w_n -> L*w in norm), g'_n -> rho g.
 (iii) C3 at f'_n (hypothesis assumed uniformly) gives the displayed lower bound.
 (iv) Constants: kappa_2(f'_n) -> kappa_2(f) (sigma'_n -> sigma); C'_n -> C; C'_{n,P°} >= M'_n Phi_{k_0} for any
     non-degenerate peak k_0 of f (status continuity: theta'_n(u_{k_0}) -> xi(u_{k_0}) and vartheta'_n -> vartheta, so the
     margin of k_0 stays positive by [I, lem:threshold]), and P°(f) != empty.
 (v) Depth: a carrier of a fixed finite set that is a non-degenerate peak of f is one of f'_n for large n; a strict non-peak
     of f stays one (strict inequality); so if no carrier of N(f) sees Z, the N'_n-carriers seeing Z leave every finite set.
     (If "sees Z" is read as Lambda(u_k) != 0 rather than u_k|_Z != 0, the finitely many N(f)-carriers with u_k|_Z parallel
     to psi|_Z have ell_{n,k} -> 0 and the conclusion still holds for the l_2 mass.)
Precision: the hypothesis "margin-sparse at Z (uniformly)" contains the Z-blind (H2); it should be called "(H1) at Z plus
uniformly bounded E°".  Proposition N is superseded by the first referee's Proposition N' (re-checked in 2.4).

## 2.4 First referee's Theorem C3' and Proposition N' — CORRECT (re-derived in this pass)
C3'(a): the proof of C2 uses, for the "counted" group, only |Theta(k)| <= 5/t (true on every peak, eps_k <= 5/t) and for the
"collective" group P_rob(mu_0) = {k in P° : mu'_k >= mu_0} the bound Phi_k eps_k <= m_k(t) <= min(t/2mu_0, 5Phi_k/t).
N3-ref Lemma S (re-checked: sum_k min(a, b 2^{-1-k}) <= (K+1)a with K = ceil(log_2(b/a)) - 1) gives sum_{P_rob} m_k <=
t l(t)/mu_0 and E_rob^2 <= (t/2mu_0) sum m_k <= t^2 l(t)/(2mu_0^2).  1 - ||e_w 1_{N_mu}||^2 = C'^2_rob/C'^2.  Correct.
C3'(b): with t(mu_0) = mu_0/log_2^2(1/mu_0) and s = 1/log_2^2(1/t): t l(t)/mu_0 = l(t)/log_2^2(1/mu_0) -> 0,
t (l/2)^{1/2}/mu_0 -> 0, tail -> 0, C'_rob(mu_0) increases to C'_{P°} (monotone convergence), and the counted l_2-sum is
<= sum_{N'} ell^2 + SM(mu_0).  Correct.  Note SM(mu_0) is a finite sum (Phi_k >= sigma(mu_0) bounds k).
Proposition N' follows from C3'(b) at f'_n with the constants of 2.3(iv).  Correct.
Remark (this pass): the log^2 rate at Z does NOT force SM(mu_0) -> 0 (one Z-seeing small-margin peak of weight ~sigma(mu_0)
per scale is compatible with eta_Z(mu_0) = o(mu_0/log^2(1/mu_0))), confirming that C3' and Cor 2.4' are complementary.

## 2.5 What C2/C3/N do and do not give (assessment)
 * They are UPPER bounds on the oscillation a row can carry (capacity), valid at every row: correct and useful.
 * They cannot certify non-recovery by themselves: Prop N/N' only say WHAT a recovering sequence must create (deep
   N'-count, or an infinite small-margin staircase at the approximant).  Both are things NA rows can create by finitely
   many window/far moves (KSB; T_PB truncations; P2 far nested tuning).  So the "count, not weight" message is the right
   reading: weight-type arguments (N3 Thm 2.3', Fatou Lemma R-F) can never exclude (i).
 * The upper bounds are not sharp (model ratios 0.13 here, 0.24 first pass), so they cannot decide the junction capacity
   comparison (R2) either: e.g. for a geometric staircase of ratio r and margins K vartheta Phi_k the C2 peak term at f is
   ~ (10/(K vartheta))^{1/2}|ell|/ln(1/r), while the band count term at f' is ~ kappa_2 (n_band)^{1/2}|ell| with
   n_band ~ ln((K+1)/(K-1))/ln(1/r); the two UPPER bounds scale differently as r -> 1, so any capacity comparison needs
   LOWER bounds (constructions), not C2.  HEURISTIC (scaling of upper bounds only).

---

# P1 referee (second pass) — part 3: cleanliness, the C-tame case done exactly, KSB, model faithfulness

## 3.1 What is rigorous in P1's cleanliness SKETCH (5.2), at an arbitrary row
P1's claim: "A strict non-peak used symmetrically below scale t_k ~ Phi_k gamma_k/c_k must have its part off F' reproduced by
g' (SYM'), and its J'-profile reproduced by the larger-scale carriers up to O(t_k) (Lemma P).  The slack cannot absorb the
hand-over, since t_* >= 6 eta/(1-rho^2).  So usable deep carriers need their contact parts on banks."
 (i) "part off F' reproduced by g'": PROVED as a one-scale statement, but only on coordinates where the WHOLE block parts of
     the two sides agree (SYM'); in general the correct statement is (SYM-int) (part 1): g' lies between the two block parts.
     Not proved: that deep carriers must be used symmetrically (N3 Thm 1.4 needs bounded coefficients at a FIXED row, and the
     de-switching scale of f'_n is not controlled uniformly in n).
 (ii) "J'-profile reproduced by the larger-scale carriers up to O(t_k)": the rigorous form is weaker.  By (FREE) at a scale t,
     the block part X_t reproduces g' on J' up to room-weighted e/(c't) <= t/(2c'); a strict non-peak k can enter X_t with
     |Phi_k Omega^s(k)| <= (2+e)Phi_k/t <= 2.5 Phi_k/t.  Hence, if at small scales g'|_{J'} is produced by a set B of deep carriers, then
     at every scale t the OTHER carriers reproduce g'|_{J'} up to room-weighted
          t/(2c') + (2.5/t) sum_{k in B} Phi_k ||u_k 1_{J'}||_1   (rooms <= 1),
     which is O(Phi_B^{1/2}) at best (t ~ Phi_B^{1/2}), not O(Phi_B).  PROVED (immediate from (FREE) and C2 Step 2).  The
     O(Phi) precision of P1 (5.2, 2.2(f)) presumes a sharp hand-over at t ~ Phi and is HEURISTIC.  Note the direction: the
     rigorous requirement is WEAKER, i.e. more favourable to approximants (junction carriers need only be O(Phi^{1/2})-near
     duplicates, room-weighted, of what larger scales produce).
 (iii) "the slack cannot absorb the hand-over since t_* >= 6 eta/(1-rho^2)": HEURISTIC.  N1 Prop 1.8 is a sufficient condition
     (scales >= t_* are automatic); it gives no failure below t_*.  Moreover it is not needed: along a recovering sequence
     eta_n = p*(g'_n - rho g) -> 0 by definition, so any pollution must vanish anyway; the only question is HOW the mate is
     carried at the intermediate scales, which (iii) does not address.
 (iv) Conclusion "usable deep carriers need their contact parts on banks": PROVED in two settings — (a) under symmetric use
     (first referee's Lemma CL, re-checked: escaping unbanked coordinate b_n, X+_n(b_n) - X-_n(b_n) -> 0, g'_n(b_n) -> 0
     force the carrier's component there to vanish), and (b) at C-tame NA rows with NO symmetric-use assumption (3.2 below).
     Precision: "on banks, OR compensated by other used carriers, OR matched by rho g at a FIXED coordinate" — banks are
     forced only for components on ESCAPING coordinates (private far contacts, as in D_anch).

## 3.2 The C-tame case is exact (referee, PROVED from Part I thm:tamefibre + prop:lowerbound)
THEOREM C2-T.  One block.  Let f' be NA with C-tame normer x' and no degenerate peaks (F', K', Q' finite, (MS)), and
Z = {j, j'} subset J'.  Every g' in C(f') has the form g' = b' + R*(omega' - d' w'), supp b' subset F', b'(x') = 0,
omega' in c_00(Q'), d' = <Dw', D omega'>/C' (thm:tamefibre), and with a' := ||Dw' 1_{Q'}||^2/C'^2 (< 1 since P' != empty):
 (a) [exact cleanliness]   g' = sum_{k in Q'} Phi_k omega'(k) u_k - d' psi'   on N \ F'  (every coordinate outside the
     support-and-banks set F', contacts included);
 (b) [coefficient bound]   ||D omega'||_2^2 <= C'/(sigma'(1 - a')),  hence |d'| <= (a' C'/(sigma'(1 - a')))^{1/2};
 (c) [exact count capacity] |Lambda'(g')| = |sum_{k in Q'} Phi_k omega'(k) ell_k| <= (C'/(sigma'(1 - a')))^{1/2} ( sum_{k in Q'} ell_k^2 )^{1/2}.
Proof.  (a) R*(omega' - d'w') = sum_k Phi_k (omega'(k) - d' w'(k)) u_k = sum_{Q'} Phi_k omega'(k) u_k - d' psi', and b' = 0 off F'.
(b) prop:lowerbound (its hypotheses a' in c_00, K' finite, Q' finite, no degenerate peaks, (MS) are part of the assumption)
gives Gamma_w(g') = c' h(b') + sigma' H(omega') <= 1 with h >= 0 and H(omega') = (||D omega'||^2 - d'^2)/C' (def:certificate).
Since D omega' is supported in Q', |d'| = |<(Dw'/C')1_{Q'}, D omega'>| <= a'^{1/2} ||D omega'||, so
(1 - a')||D omega'||^2 <= ||D omega'||^2 - d'^2 <= C'/sigma'.  (c) Lambda'(b') = 0 (Z disjoint from F'), Lambda'(psi') = 0, and
Lambda'(sum_{Q'} Phi_k omega'(k) u_k) = <D omega', ell 1_{Q'}>; Cauchy–Schwarz and (b).  QED
COROLLARY CL-T (cleanliness along C-tame recovering sequences; PROVED).  Let f'_n -> f be NA with C-tame normers without
degenerate peaks, g'_n in C(f'_n), g'_n -> rho g.  Then (passing to a subsequence) d'_n -> d, ||D omega'_n||_2 <= B,
and V_n := sum_{Q'_n} Phi_k omega'_n(k) u_k satisfies ||(V_n - rho g - d psi) 1_{N \ F'_n}||_1 -> 0; in particular
||V_n 1_{S_n}||_1 -> 0 for every sequence of sets S_n subset N \ F'_n escaping to infinity.
Proof.  sigma'_n -> sigma > 0, C'_n -> C, and 1 - a'_n >= (M'_n Phi_{k_0}/C'_n)^2 for a robust peak k_0 of f (status
continuity), so B := sup_n (C'_n/(sigma'_n(1-a'_n)))^{1/2} < infinity and |d'_n| <= B.  Off F'_n, V_n = g'_n + d'_n psi'_n
by (a); ||g'_n - rho g||_1 -> 0, psi'_n -> psi in l_1 (prop:continuity), g, psi in l_1.  QED
READING.  (1) At C-tame approximants P1's cleanliness is an IDENTITY: no switching, no hand-over, no symmetric-use assumption.
The Z-oscillation is carried exactly by the used strict non-peaks, with the sharp l_2-count constant (C'/sigma')^{1/2}
(compare C3: (kappa_2 + E_inf) C'^2/C'^2_{P°} with kappa_2 = (0.434/sigma')^{1/2} > (C'/sigma')^{1/2}).  (2) Along C-tame
recovering sequences the used strict non-peaks must REPRODUCE rho g + d psi off F'_n in l_1, with l_2-bounded weighted
coefficients — a representability condition, not a capacity one.  A converted carrier whose private contact part is not
banked is unusable (its coefficient times its contact part must -> 0).  (3) The certificate must in addition satisfy the
mate inequality at ALL positive scales (not only Gamma_w <= 1): this is the junction problem (O1(c) of the first referee).
(4) Hence the genuinely OPEN part of "cleanliness" lives only at NON-C-tame NA rows (infinitely many strict non-peaks or
degenerate peaks near Z, or failure of (MS)) — exactly alternative (ii) of Prop N' and the rows where mates need not be
certificates.  A negative proof must handle these; a positive proof may avoid them (if KSB rows can be chosen C-tame).
C-tameness of KSB rows: holds for T with no accidental near-threshold carriers at x' (finitely many strict non-peaks and
margins mu'_k >> Phi_k eventually); "generic" (Borel–Cantelli heuristic: P(mu'_k <= C Phi_k) ~ Phi_k summable) — HEURISTIC;
for an explicit design it is a design property to be checked.

## 3.3 KSB (5.3): verdicts
 * Construction (K), (S), (B), (D) yields NA rows f'_{L,delta} -> f (prop:approximants): CORRECT.
 * "One clean deep-kernel strict non-peak ... covers all smaller scales": the count law (C2-T) gives a single banked carrier
   the second-order capacity (C'/(sigma'(1-a')))^{1/2}|ell_{k_0}|, which in the first pass's failing regime EXCEEDS the
   target (ratio 0.68, part 4.2(c)).  The one-bank failure found by the first pass (r = 0.75, K = 1.5, deep staircase) is
   reproduced at nA = 30 but absent at nA = 20, and it is located in the junction window between the single carrier's
   coverage and the kept staircase (part 4.2(d)).  So P1's sentence is false at model level for a different reason than
   capacity: ONE carrier does not cover the junction.  "Bank every carrier the shift converts" is the safe statement (banks
   only add two-sided resources); it closes the junction gap in every tested regime.
 * Extra requirement (this pass; PROVED necessary at C-tame rows by C2-T(a)): on every UNBANKED kept contact b, g' = -d'psi'
   (+ used strict non-peaks' components); so if pi_g = g/psi is non-constant on the kept contacts of f (contact oscillation),
   KSB must also bank the whole contact-oscillation set inside the window (summable masses), as in the engineered
   approximants [I, def:engineered] / N3-ref Prop X(a).  In the anchored model g_f vanishes on the contacts (pi_g = 0, 3.4),
   so this is not visible there; for a general Problem-R configuration it is required.
 * Recovery by KSB in an explicit admissible design: OPEN (needs Lemma B for the design, g in C(f), and the junction).

## 3.4 Numerics of this pass (P1_ref_work/rb_*.py; sanity checks only)
 * rb_c2_check.py (independent finite model, 3 seeds, rows with robust peaks, 3 strict non-peaks and 3 small-margin peaks
   seeing Z = {1,2}, a contact; grid mates maximizing Lambda' under g'(y') = 0 and both norm bounds on 26 scales in
   [2e-3, 2]): C2 ratio <= 0.134 at every grid scale (min over s in {1, .3, .1, .03, .01}); N3 budgets (a),(b) ratio <= 0.987
   (nearly tight: the budget is attained); Lemma SYM ratio <= 0.505.  Consistent with C2, SYM, Lemma 1.2.
 * rb_model_faithful.py (anchored model, P1 run7 setting, first referee's excess form): f's maximizing mate vanishes on the
   contacts (pi_g ~ 0) and lives on Z; the KSB optimum (L = 6, band@5, dist 0.0070, reproducing the first pass) satisfies
   g3/psi3 ~ 0 on unbanked kept contacts and g3 = 0 on destroyed contacts; MINIMAL switching ||B+ - B-||_1 needed by g3:
   1.2e-4 (s = 5e-5), 1e-9 (2e-4), 7e-11 (1e-3), 5e-14 (5e-3), 0.148 (2e-2), 0.204 (1e-1).  So below ~5e-3 (~Phi_band) the
   KSB mate is carried WITHOUT switching (symmetric, certificate-like — as genuine NA rows require), above ~1e-2 by the kept
   staircase in switching mode.  This confirms the KSB division of labour and that the model is not relying on
   finite-dimensional persistent switching (which genuine NA rows cannot have, N3 Thm 1.4).  Faithfulness caveat (general):
   finite models have Y n c_00 != {0}; Part I rem:kinks(a) notes the lower bound prop:lowerbound can fail there.  In the
   anchored design the staircase coordinate e_3 with beta_k ∝ -s_k Phi_k and the contact signs make every contact-compatible
   zero-J' combination trivial, which is why the artifact does not occur; other finite models must be checked the same way.
 * Re-run of the first referee's single_vs_band.py (r = 0.75, K = 1.5, nA = 20, L = 14): f Osc 0.1025; distances to 0.9 g_f:
   one bank 0.0086 / 0.0082, others destroyed 0.0086 / 0.0082, bank-all 0.0079 / 0.0077 (ib = 12 / 13).  With this shallower
   staircase a single banked carrier suffices.  With nA = 30 the first pass's numbers are reproduced exactly (one bank
   0.0442 / 0.0964, destroyed 0.0973 / 0.1485, bank-all 0.0078 / 0.0062); localisation of the failure in part 4.2.

---

# P1 referee (second pass) — part 4: comparison with the first referee pass; the one-bank failure located; open list

## 4.1 Agreement with the first pass (r15/P1_ref_prev/)
Re-derived independently and AGREED: SYM, SYM', P, C2 correct; (SYM-int), (FREE) reformulations; C3 correct with the
precisions psi'|_Z != 0 and liminf E°; C3 Remark (i) incomplete because (H2) is Z-blind; (R1) [log^2 rate => (H1)];
Theorem C3' and Proposition N' correct (re-derived in part 2.4); Lemma CL correct; slack sentence heuristic; P1's
small-scale numerics (below ~3e-4 in the O(1)-constraint formulation) unreliable; canonical truncations do not converge in
the anchored model (0.236 at L = 4, 6, 8, reproduced in spirit by this pass's runs at nA = 30: 0.5708 at L = 14).
Additions of this pass: Theorem C2-T and Corollary CL-T (exact cleanliness and sharp count constant at C-tame NA rows),
the O(Phi^{1/2}) (not O(Phi)) rigorous junction precision, the contact-oscillation banking requirement, the
model-faithfulness check (no finite-dimensional persistent switching at small scales), the localisation of the one-bank
failure (4.2), and an explicit example showing that (H2) can fail along EVERY t -> 0 (peaks with mu'_k = Phi_k^3, 2.2).
One disagreement with the first pass: its explanation of K1 as a "capacity deficiency of a single carrier" is not supported
— the second-order count capacity of the single banked carrier exceeds the target, and the failure sits in the junction
window (4.2).  The correction K1 itself stands.

## 4.2 The one-bank failure (first pass's correction K1) re-examined
Setting r = 0.75, K = 1.5, L = 14, rho = 0.9 (anchored model, excess formulation).
 (a) Reproduced at nA = 30 (f Osc 0.3465): one bank 0.0442 / 0.0964, other band carriers destroyed 0.0973 / 0.1485,
     bank-all 0.0078 / 0.0062 (ib = 12 / 13) — identical to the first pass.
 (b) NOT present at nA = 20 (staircase ending at the f-grid bottom, f Osc 0.1025): one bank 0.0086 / 0.0082, destroyed
     0.0086 / 0.0082, bank-all 0.0079 / 0.0077.  So K1 depends on how much small-scale capacity f's emulated staircase has.
 (c) NOT a second-order capacity deficiency (contrary to the first pass's reading "capacity deficiency of a single
     carrier"): with C', sigma' of the one-bank row (C' = 0.2386, sigma' = 0.1492, a' = 2e-4), the exact count capacity of
     Theorem C2-T for the single banked carrier is 1.49e-2 against the target rho|Lambda'(g_f)| = 1.01e-2 (ratio 0.68 < 1;
     bank-all 0.48).  (rb_count_capacity.py.)  Max Z-oscillation of the one-bank row with all scales imposed: 0.3567 >=
     target 0.3353 (normalized), small scales only: 0.62.  (rb_junction.py.)
 (d) It is a JUNCTION effect: distance from 0.9 g_f to the grid fibre of the one-bank row with the mate inequality imposed
     only on windows: [5e-6, 1e-3] 0.0082; [5e-3, 2] 0.0069; [2e-2, 2] 0.0039; but [5e-6, 5e-3] 0.0189, [1e-3, 2] 0.0327, all
     scales 0.0422.  Bank-all: 0.0078 on every window (0.0069 / 0.0039 on the large-scale windows).  (rb_junction2.py.)
     The single banked carrier (Phi ~ 4e-3) covers scales <~ 1e-3, the kept staircase covers >~ 5e-3, and the window
     [1e-3, 5e-3] in between is carried by neither; banking the shallower converted carrier (Phi ~ 7e-3) extends the
     symmetric coverage upward and closes the gap.  Representability on J' is not the issue either (l_1 residual of
     rho g_f|_{J'} from span{banked u_k|_{J'}, psi'|_{J'}}: 4-7e-3 one bank, 1.4e-3 bank-all; rb_representability.py).
 Verdict on K1: the correction ("bank every carrier the shift converts") is right and harmless; its explanation should be
 "junction coverage", not "capacity".  This is exactly the hand-over residue isolated by N3 (Part 3.2) and by P1 itself
 (5.2, 6.2 (O-R1)(b)): the decisive scales are those between the coverage scale of the clean deep carriers and the
 lowest scale at which the kept structure works.  HEURISTIC (model level), but now localised.

## 4.3 Hunt for a recovering approximant / for an obstruction (both directions)
 * Positive side.  Besides KSB (f's own near-duplicate staircase carriers converted at the junction, contact parts banked),
   a second family exists in principle: convert a GENERIC deep carrier u_k approximating the needed J'-vector by FAR moves
   to contacts +-1 plus banks (absorbing its far part, Cor CL-T(ii)); its usability needs a junction near-duplicate rate
   ||u_k - v||_{J', room} <~ Phi_k^{1/2} (3.1(ii)) — a RATE property of the dense sequence (w'_n) that an adversarial
   admissible T can deny.  KSB needs no rate: f's own staircase carriers are near-duplicates at the right rate because
   (FREE) at f forces the active combination at scale t to reproduce g|_J up to O(t) (PROVED for a single carrier per scale,
   first pass; for several carriers per scale only the active combination is constrained).
 * Negative side.  At C-tame approximants every mate is an explicit certificate (C2-T); a non-recovery proof restricted to
   C-tame approximants would have to show that NO certificate on clean strict non-peaks is valid across the junction, for
   every choice of junction depth, shift lever and banks — while KSB provides, in every tested model, such a certificate.
   Non-C-tame approximants (infinite strict non-peak or small-margin families near Z, alternative (ii) of Prop N') only add
   freedom.  No obstruction mechanism is visible; none is claimed.
 * Checks requested by the task: no admissible T is asserted by P1 (D_anch is HEURISTIC; its admissibility is a routine
   adaptation of N2 Lemma 2.1 — private infinite signature sets for (T-b),(T-c), interleaved generic carriers for (T-d),
   the private contacts b_k being single extra coordinates — SKETCH, not written); g in C(f) for D_anch is model-only
   (N2 Prop 2.3 covers the contact-free staircase T_PB, with explicit constants, not D_anch).

## 4.4 What remains OPEN (precise)
 (O1) Problem R, negative: OPEN.  No candidate; a proof would have to defeat KSB at every junction depth (C-tame case:
      no valid band certificate across the junction) and all non-C-tame approximants.
 (O2) KSB as a theorem in ONE explicit admissible design: (a) Lemma B for D_anch (routine); (b) the switching mate g in
      C(f) with explicit constants (N2 Prop 2.3 with anchored contacts); (c) C-tameness of the KSB rows (no accidental
      near-threshold carriers at x'); (d) the JUNCTION: validity of the banked-band certificate (C2-T form, data on the band
      and F' u banks) on the scale window between the band's coverage (~ Phi_band gap/coefficient) and the lowest scale of
      the kept staircase, with the kept staircase in switching mode as at f; (e) contact-oscillation banks if pi_g is not
      constant on the kept contacts.  Model evidence: (d) fails with one bank and succeeds with the banked band in the
      deep small-margin regime (4.2).
 (O3) Cleanliness at NON-C-tame NA rows (necessity of symmetric use; de-switching with unbounded coefficients).
 (O4) Quantitative junction comparison for general T (P1's "duality"); upper bounds (C2, C2-T) cannot decide it.
 (O5) Density of NA((c_0, p_N), l_2^2) for Martin's renormings: OPEN; evidence (models) weakly favours density.
