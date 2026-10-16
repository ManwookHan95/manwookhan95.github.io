# P2 notes (Round 15, positive track): the common core pursued positively

Task items: (1) Problem R positive (approximants re-creating weak-peak freedom at free coordinates); (2) the (R-S1)-with-escape
residual of ADDENDUM 14b for the designed operator; (3) finite merging (P-II of N1-ref, Rec(f) in A(f)).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "Mod chain" = modulo the refereed links named in each statement
(Part III Section 5, G1/G1-ref, G3/G3-ref, H2/H2-ref, K2, J1).  Part files: P2_part0_context.md, P2_part2.md (item 2),
P2_part1.md (item 1), P2_part3.md (item 3); all reproduced below.  Scripts: P2_work/cm_identity_check.py,
P2_work/tuning_check.py (sanity checks only).  Cross-reference: the concurrent track P1 (r15/P1_notes.md) treats Problem R
from the negative side and proposes the KSB approximants; Part 1 below is written to complement it.

## 0. Answer

ITEM (2), the (R-S1)-with-escape residual.  PROVED (mod chain, restricted model of G1 Prop. 5.2): an EXACT common-mode
identity (2.1) for the cofactor combination V of any (R-S1) Farkas obstruction shows that the obstruction needs a ROBUSTLY
NEGATIVE common mode kappa_V <= -||C~||_1/(2H(L)), carried by THICK support of the resonant group on which V = kappa_V a
exactly.  Consequently the "escape" of ADDENDUM 14b is always this common mode: thin shared support (G-THIN), contacts, free
and zero-data coordinates, outside switching and other active strict non-peaks can never be what makes an (R-S1)
obstruction possible, and the escape gives no first-order lever.  The identity also corrects G3-ref R-ESC.2 (the Hilbert
terms h_k summed over a group ARE the common mode and need not be small).  Free-target pairs (the shape G1 Cor. 5.3(iii)
left open) have ROBUST minors unless they have thick or anti-aligned coordinates.  PROVED modulo a design clause (D-sep,
SKETCH, one quantifier point (Q) unchecked): single-minor (R-S1) cannot occur at two consecutive large (R1) main stages
(Theorem 2.10).  OPEN: multi-minor stages (unboundedly many simultaneously tiny strict minors), (R-S2), (R-S3), (R-L),
(R0^str), shifted blocks, non-consecutive stages.

ITEM (1), Problem R.  NOT resolved.  PROVED: (a) the oriented two-signed requirement (Cor. 1.2): each oriented class of
small-margin peaks seeing the free pair must separately violate the log^2 margin-sparsity rate; (b) nested tuning by a
Schauder-Tychonoff fixed point (Prop. 1.3, Cor. 1.4): for EVERY admissible T and EVERY row f there are attaining rows
arbitrarily close to f with infinitely many deep carriers of prescribed profile on the free set, prescribed sign class and
EXACT prescribed margins (or exact zero pairing) -- this answers the existence question left OPEN in N3 Section 1.6 and
realizes the nested-tuning mechanism at the level of rows with no rate hypothesis on T; (c) one strict non-peak is a
certificate of size O(1) and radius ~ gamma lambda (Prop. 1.5), and as a stand-alone mate it has size >= 0.49 (gamma
lambda)^{1/2} (Cor. 1.6, the sqrt-weight law, lower bound); (d) certificate-based recovery in the Problem-R configuration
forces converted carriers of depth -> infinity, radius -> 0 and approximants within the SQUARE of the converted weights
(Prop. 1.7); HEURISTIC: the slack-only junction is therefore impossible and the intermediate scales must be certified by
the kept weak-peak staircase (non-certified).  OPEN: the junction problem (staircase transport with exact first-order
rebalancing and a constant comparison at the junction depth); P1's models favour the approximant.

ITEM (3), finite merging.  NOT resolved in general (OPEN).  PROVED: equivalent forms (directedness of A(f); transitivity
along merging rows; a simultaneous-limsup primal form); the U_NA-fan structure of Rec(f); automatic merging at attaining
rows, at continuity points of C, when C(f) = cl Cert^sh(f), and when all non-core mates lie in one cluster set; under (P-I)
every extreme mate is recovered (Milman) and merging implies density at f; a PLACEMENT criterion (Theorem 3.6): if the
far-locally recovered mates are dense in Rec(f), finite merging holds.  HEURISTIC: which recovery mechanisms are far-local
(certified: yes; tuned carriers: only under a precision-versus-weight rate; KSB: not far-local, but one KSB sequence serves
all mates sharing an oscillation set); mixing approximants does not merge.

Leaning: POSITIVE (weakly).  Every residual examined acquires more structure that favours realizability (item 2), every
positive mechanism can be built at the level of rows for every T (item 1), and nothing found makes merging fail; but no
item is closed, and the decisive points (multi-minor stages, the junction constants, merging of non-certified recoveries)
remain open.

## Results table

| # | Result | Status | Where |
|---|---|---|---|
| 1 | Common-mode identity (2.1)/(2.4) for every finite carrier combination | PROVED (algebra) | 2.2 Thm 2.3(A), 2.4 Lemma 2.7 |
| 2 | (R-S1) obstructions need robust negative common mode kappa_V <= -||C~||/(2H) | PROVED (mod chain) | 2.2 Thm 2.3(B) |
| 3 | Two-sided design-depth support is proportional (V = kappa_V a); thick support carries the compensation | PROVED (mod chain) | 2.3 Cor 2.4, Cor 2.5 |
| 4 | Free-target pairs without thick/anti-aligned coordinates have robust minors | PROVED | 2.3 Prop 2.6', Cor 2.6 |
| 5 | Escape of (R-S1) = common mode; R-ESC.2 correction; no first-order lever | PROVED (mod chain) | 2.4 Consequence 2.8 |
| 6 | Persistence forces f's thick profile into cofactor spans | PROVED (necessary condition, mod chain) | 2.5 Prop 2.9 |
| 7 | Design clause (D-sep) achievable | SKETCH (quantifier point (Q) unchecked) | 2.5 |
| 8 | Single-minor (R-S1) cannot occur at two consecutive large (R1) main stages | PROVED mod (D-sep) | 2.5 Thm 2.10 |
| 9 | Multi-minor stages, (R-S2), (R-S3), (R-L), (R0^str), shifted blocks | OPEN | 2.5 Remark 2.11 |
| 10 | Oriented profile identity; two-signed rate requirement (refines R-W) | PROVED | 1.1 Lemma 1.1, Cor 1.2 |
| 11 | Nested tuning fixed point; non-C-tame attaining rows with prescribed deep near-threshold carriers near every f, every T | PROVED | 1.2 Prop 1.3, Cor 1.4 |
| 12 | Conversion lemma (near shift turns a weak peak into a strict non-peak) | PROVED | 1.2 Remark (c) |
| 13 | One strict non-peak: certificate of size O(1), radius ~ gamma lambda | PROVED | 1.3 Prop 1.5 |
| 14 | sqrt-weight law, lower bound 0.49 (gamma lambda)^{1/2} | PROVED | 1.3 Cor 1.6 |
| 15 | Certificate recovery in Problem R forces deep carriers, radius -> 0, square-precision approximants | PROVED | 1.4 Prop 1.7 |
| 16 | Slack-only junction impossible | HEURISTIC | 1.4 Remark 1.8 |
| 17 | Junction problem (Problem R positive, rho g in Rec(f)) | OPEN | 1.4 |
| 18 | Adversarial T must restrict precision-versus-weight of shapes (meagre-type condition) | HEURISTIC | 1.4 |
| 19 | Equivalent forms of finite merging (directed A(f), transitivity, primal simultaneous limsup) | PROVED | 3.1 Prop 3.1 |
| 20 | U_NA-fan structure of Rec(f) | PROVED | 3.2 Prop 3.2 |
| 21 | Automatic merging (attaining rows, Omega, C = cl Cert^sh, single non-core cluster set) | PROVED | 3.2 Prop 3.3 |
| 22 | Under (P-I): ext C(f) in Rec(f); density at f iff Rec(f) convex; merging implies density at f | PROVED | 3.2 Prop 3.4 |
| 23 | Placement criterion: dense far-locally recovered mates imply finite merging | PROVED | 3.3 Thm 3.6 |
| 24 | Which recovery mechanisms are far-local; mixing does not merge | HEURISTIC | 3.3 Remarks 3.7, 3.8 |
| 25 | Finite merging (P-II) at every f | OPEN | 3.4 |
| 26 | Numerics: identity (2.1) exact to 8e-15; tuning fixed point and pairing-form threshold criterion in a finite model | sanity checks | Section N |

## Main obstacle
Item (2): stages with MANY simultaneously tiny strict minors -- Proposition 2.9(iv) only puts f's thick profile into an
intersection of cofactor spans, which a span version of (D-sep) excludes only if the number of tiny minors per stage stays
bounded.  Item (1): the junction -- the converted (two-sided) carriers certify only scales below ~ gamma lambda, the slack
only scales above ~ (lambda gamma)^{1/2}; the gap must be covered by transporting f's weak-peak staircase to the
approximant with exact first-order rebalancing, which no finite-certificate tool does.  Item (3): merging of NON-certified
recoveries; the placement criterion needs robustness of each recovery against arbitrary far data, which for tuned
carriers is a precision-versus-weight rate and for KSB-type recoveries fails (near shifts interfere when oscillation sets
share carriers).

## Next steps
(i) Item 2: prove a span version of (D-sep) and bound the number of simultaneously tiny strict minors per stage (e.g. by a
pigeonhole over clean sub-windows as in G2), then extend the common-mode identity to shifted blocks (term -kappa_m c_M).
(ii) Item 2: check the quantifier point (Q) of (D-sep) against the recursion of T_fin^{K2} (can window thresholds of a main
stage be chosen after the targets of the following design stages?).
(iii) Item 1: attack the junction in a model with a scale-local staircase (one weak peak per dyadic scale): transport the
staircase decompositions with exact first-order rebalancing (the b_n = b'_n - tau_n a_n device of [I, thm:transport]) and
compare the constants at the junction; combine with P1's KSB models.
(iv) Item 3: prove monotonicity of engineered recoveries under additional tiny banks on contacts (Remark 3.7(d)), and the
g-independence of KSB sequences for mates sharing an oscillation set, to get merging in those classes.

---


# Part 0 (context)

# P2 (Round 15, positive track) -- part 0: context digest and plan

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "Mod chain" = modulo the refereed links cited (Part III Section 5,
G1/G1-ref, G3/G3-ref, H2/H2-ref, K2, J1).

## Sources read
BRIEFING_R2 (all addenda, esp. 13, 14a, 14b, NEG); neg/N1_referee, N1_ref_notes (Lemma R-M, R-I, R-E1); neg/N2_referee;
neg/N3_referee, N3_ref_notes (Lemma R-V, R-F, R-W, Thm 2.3', Cor 2.4', Prop X, Problem R); r14/G1_notes (Lemma LE, Def 3.2,
Prop 5.2, Cor 5.3, Cor 5.4, Thm G1.D), G1_referee; r14/G2_referee (Theorem ML', (P-res')); r14/G3_notes (Lemmas 1.1-1.7,
Thm CL, Thm 2.10, Cor 2.11, Lemma 2.8), G3_referee, G3_ref_notes (Lemma R-ESC, Cor R-ESC.1/.2, G-THIN); r13/H2_notes
(Fact 1.1, Fact 1.2, Prop 4.1, Example 4.3, Theorem H2.B); r12/J1_notes (Lemma J1.1 deviation identity, J1.3, J1.4);
Part I Sections 1-2 (setting, threshold lemma, forced data, approximants, reduction, lower-limit theorem, cor:finite,
transitivity, rem:joint); Part III Sections 5.3-5.6 (resources, Lemma III-identity, Lemma III-actions, preparation and
Lemma III-prep, Step-A system, Euler combination, A-regularity, Lemma III-cone, Theorem III-Aobs, Cor III-Asuff),
Part III 5.5 opening (near coordinates N_l = first six elements of S_l beyond s_max(L) = max T(L); H(L)).

## Plan
Part 2 (item (2), the (R-S1)-with-escape residual): an EXACT identity for the cofactor combination of an (R-S1) Farkas
obstruction (common-mode identity), whose consequences are: (i) robust negative common mode is necessary; (ii) every
two-sided support generator at design depth is proportional; (iii) thin-support / contact / free-coordinate escapes cannot
carry the compensation; (iv) Example 4.3 with a free common target has a ROBUST minor; (v) persistence needs span
coincidences of fresh target combinations with f's thick profile (design clause).
Part 1 (item (1), Problem R): norm-level lemmas (two-signed profile, non-peak capacity, invisible moves, depth escape,
conversion circularity) and a conditional recovery statement.
Part 3 (item (3), merging): abstract criteria, reductions, what is and is not provable.

---

# P2 part 2: the (R-S1) residual -- the common-mode identity, and what an escape can and cannot do

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "Mod chain" = modulo the refereed links named in each statement.

## 2.0 Setting

Design T_fin^{K2} with the conventions of G1 (FC, P-TU, F-2, (D-enum), (D-G1a), split preparation P^nat), diagonal base
U k_s = mu_s e_s with mu_s = mu*_s = 2^{-2^{2^s}}.  N >= 1, f in S_{p_N^*}, g in C(f), rho in (0,1).  Main stage L >= l_f,
clean sub-window w, class a; b = b(w), u = u(w); R_1 = the prepared Step-A^nat input row (after deep raise, Step 0, P^nat
and the TU pre-placements) with base data (a, z, e, nu, zhat), zhat = z + U e, F = supp a, q*(a) = ||a||_1 + nu = 1.
Design facts used (Part III 5.5 opening, G3 Section 4): every coarse carrier is u_l = y_l + v_l with supp y_l in T(L)
(the coarse targets), s_max(L) := max T(L), v_l supported on the signature set S_l = {2^l(2i+1) : i >= 1}; beyond
s_max(L) the only coarse carrier that is nonzero on S_l is l, and there v_l(s) = delta_l 2^{-s}/n_l > 0.  The near
coordinates N_l are the first six elements of S_l beyond s_max(L); H(L) := max_{l <= L} max_{s in N_l} 1/v_l(s).

For x in l_1 put kappa_x := <U^* x, e>/nu = sum_s mu_s^2 x(s) a_s/nu^2 and Dev_x := x - kappa_x a (J1 Lemma J1.1).  Then
      x(zhat) = kappa_x + sum_s Dev_x(s) z_s                                    (exact; J1.1)            (2.0)
(proof: x(zhat) = x(z) + kappa_x nu and Dev_x(z) = x(z) - kappa_x ||a||_1, with ||a||_1 + nu = 1).  Note
kappa_x = sum_{s in F} p_s x(s)/a_s with the HILBERT WEIGHTS p_s := mu_s^2 a_s^2/nu^2 >= 0, sum_s p_s = 1.

THE RESTRICTED MODEL (G1 Prop. 5.2, augmented).  All blocks carrying tiny strict minors are (U)-blocks (inactive shifts);
every tiny strict minor contains exactly one (X3) row, so (G1 Lemma LE) M_{m,i}(r) = <C_{m,i}, r^(m)> with design
cofactors C_{m,i} (indexed by the gamma-columns of block m), r_l = u_l(zhat)/kappa_m the (unoriented) ratios at R_1,
kappa_m > 0 the block scalar.  Oriented quantities: eps_l = sign of the switching of l (Def. III-resources),
C'_{m,i,l} := eps_l C_{m,i,l}.  Generators (Def. III-Areg, Lemma III-prep(d), G1 Lemma 4.2(c)): at every design-depth
coordinate s in U_L of type TS (thick support, two-sided mass change), FR (free, robust room, two-sided z-move), ZD
(coordinate of a zero-data carrier: two-sided composite move) and S_th (support of mass >= theta/2 after P^nat: banked
contacts, raised thin support; one-sided RAISES if data-carrying, two-sided if zero-data).  Their first-order actions on
carrier values are (Lemma III-actions): eff_s Dev_{u_l}(s) dm for a mass change at s in F, u_l(s) dz for a z-move at s
notin F, with eff_s = mu_s^2/nu >= 1/Des(L); a raise is dm = z_s |dm|.  [G1 Prop. 5.2 lists FR, TS and one-sided raises;
ZD generators are part of the Step-A generator set and only add constraints on an obstruction.]

The Farkas alternative of the linearized exactification (G1 Prop. 5.2, proof) in the normalization lambda~_{m,i} :=
lambda_{m,i}/kappa_m: the stage is (R-S1)-residual iff there is lambda~ with
 (a) (sum_i lambda~_{m,i} C'_{m,i})_l >= 0 on strictly pinned kind-(iv) rows l of block m, = 0 on strictly pinned
     two-sided rows;
 (b) sum lambda~_{m,i} <C_{m,i}, Dev^(m)(s)> = 0 for every two-sided generator at s in F, sum lambda~ <C, u^(m)(s)> = 0 for
     every two-sided generator at s notin F, and sum lambda~ <C, z_s Dev^(m)(s)> >= 0 for every one-sided raise at s;
 (c) sum_{m,i} lambda~_{m,i} kappa_m M_{m,i}(rc) > 0 (wrong sign at the start row).
[Derivation: the kind-(iv) moves raise oriented ratios (variables a >= 0, column C'), two-sided pinned rows and two-sided
generators are free variables, raises are variables e >= 0; the action of a generator on M_{m,i} is <C_{m,i}, Dev^(m)(s)>/kappa_m
times its size up to a homogeneous rescaling of block m (which does not move the zero set of a (U)-block minor);
Farkas' lemma for {x : a, e >= 0, A x = -M(rc)} gives (a)-(c) with lambda~ = lambda/kappa_m.]

DEFINITION 2.0.  For an obstruction lambda~ put C~_l := sum_i lambda~_{m(l),i} C_{m(l),i,l} (combined cofactor, unoriented),
C~'_l := eps_l C~_l, G := {l : C~_l != 0} (the RESONANT GROUP of the obstruction), and
      V := sum_{l in G} C~_l u_l     (a finite combination of coarse carrier vectors: the COFACTOR COMBINATION),
      J := (union_{l in G} supp u_l) cap [1, s_max(L)],   P_l := S_l cap (s_max(L), infinity) (l in G),
      a_J := sum_{s in J cap F} |a_s|.
By (a), G consists of strictly pinned kind-(iv) rows and C~'_l > 0 on G.  Since the minors are linear in r^(m), V and
lambda~^T M(rc) depend on lambda~ only through C~; we may and do remove from lambda~ its component in the (design) kernel
{lambda~ : C~ = 0}; then ||lambda~||_1 <= Des(L)^C ||C~||_1 (Cramer: nonzero design minors are >= 1/Des, G1 Section 4).

## 2.1 Algebraic identities

LEMMA 2.1.  PROVED (algebra).  For every lambda~:
 (i)  V(zhat) = sum_{m,i} lambda~_{m,i} kappa_m M_{m,i}(rc);
 (ii) for a generator at s: sum lambda~_{m,i} <C_{m,i}, Dev^(m)(s)> = Dev_V(s) and sum lambda~ <C_{m,i}, u^(m)(s)> = V(s).
Proof.  (i) M_{m,i}(rc) = sum_{l in m} C_{m,i,l} u_l(zhat)/kappa_m; multiply by lambda~_{m,i} kappa_m and sum.  (ii) Dev_x is
linear in x (kappa_x is linear), so sum lambda~ sum_l C_{m,i,l} Dev_{u_l}(s) = Dev_{sum C~_l u_l}(s).  QED

So in the restricted model, (b) and (c) are statements about ONE vector V of Y:
 (b')  Dev_V(s) = 0 at two-sided generators in F; V(s) = 0 at two-sided generators off F; z_s Dev_V(s) >= 0 at raises;
 (c')  V(zhat) > 0.

LEMMA 2.2 (aligned private dominance).  PROVED (mod chain: H2 Fact 1.1(c); design facts of 2.0).  Let l be a kind-(iv)
carrier at an (R1)-type stage (no thick-type carrier), with data sign eps_l.  Then at R_1
      pi_l := eps_l sum_{s in P_l} v_l(s) z_s  >=  (1 - 2^{1 - 2^{l+1}}) v_l(n_1(l))  >=  7/(8 H(L)),
n_1(l) := min N_l.
Proof.  By Fact 1.1(c) every near coordinate of l is S_th of the data sign, i.e. at R_1 it lies in F with sgn a_s = eps_l,
so z_{n_1} = eps_l and the term at n_1 is v_l(n_1).  Consecutive elements of S_l differ by 2^{l+1}, so on P_l the values
v_l(s) = delta_l 2^{-s}/n_l decrease by the factor 2^{-2^{l+1}} from one element to the next, and |z_s| <= 1:
sum_{s in P_l, s != n_1} v_l(s) <= v_l(n_1) 2^{-2^{l+1}}/(1 - 2^{-2^{l+1}}) <= 2^{1-2^{l+1}} v_l(n_1).  Finally v_l(n_1) >=
1/H(L) by the definition of H(L), and 1 - 2^{1-4} = 7/8 for l >= 1.  QED
[Remark.  This replaces the bound "c_k >= N_k - U_far - h_k >= c/H(L) (mod chain)" of G3-ref R-ESC.2 by an explicit one,
and in Theorem 2.3 below no Hilbert term h_k appears at all: the Hilbert parts are absorbed exactly by (2.0).]

## 2.2 The common-mode identity

THEOREM 2.3 (common-mode identity; necessity of a robust negative common mode).  PROVED (mod chain: the restricted model
of G1 Prop. 5.2 as stated in 2.0; Lemma 2.2's hypotheses).
(A) For every lambda~ (obstruction or not) the following identity holds EXACTLY at R_1:
      V(zhat) = kappa_V (nu + a_J) + sum_{s in J} Dev_V(s) z_s + sum_{l in G} C~'_l pi_l.                         (2.1)
(B) If lambda~ is an (R-S1) obstruction ((a)-(c)) at an (R1)-type stage and every tiny strict minor satisfies
    |M_{m,i}(rc)| <= beta := (1 + 2 Lip) b (G1 Definition 3.1 (T1)), then
      kappa_V (nu + a_J) <= beta kappa_max Des(L)^C ||C~||_1 - (7/(8 H(L))) ||C~||_1,                             (2.2)
    hence, for L large (beta kappa_max Des(L)^C <= 1/(8 H(L)), true since window thresholds lie below every design
    constant of level L),
      kappa_V <= -||C~||_1 / (2 H(L))     and     V(zhat) > 0.                                                    (2.3)
Proof.  (A) Every s lies in exactly one of J, P := union_{l in G} P_l, Rest := N \ (J u P) (the P_l are disjoint, being
pieces of disjoint signature sets beyond s_max(L), and disjoint from J by definition).  supp V is contained in
union_G supp u_l, which is contained in [1, s_max(L)] u P (supp y_l in T(L), supp v_l = S_l); so V = 0 on Rest, and for
s in P_l, V(s) = C~_l v_l(s) (no other coarse carrier of G is nonzero there).  Hence by (2.0)
  V(zhat) = kappa_V + sum_J Dev_V(s) z_s + sum_{l in G} sum_{P_l} (C~_l v_l(s) - kappa_V a_s) z_s - kappa_V sum_{Rest cap F} |a_s|
          = kappa_V (1 - ||a 1_{P u Rest}||_1) + sum_J Dev_V(s) z_s + sum_{l in G} C~_l sum_{P_l} v_l(s) z_s
(using a_s z_s = |a_s| on F).  Now 1 - ||a 1_{P u Rest}||_1 = nu + ||a 1_J||_1 = nu + a_J, and C~_l = eps_l C~'_l gives the
last sum = sum C~'_l pi_l.
(B) By (b') each term of sum_J Dev_V(s) z_s is >= 0: every s in J is a design-depth coordinate of U_L (J is in T(L) cup
supp of the group's signatures below s_max(L), and T(L) is at design depth), hence of type TS, S_th, FR or ZD (Lemma
III-prep(d), G1 Lemma 4.2(c)); at two-sided generators the term is 0 (Dev_V(s) = 0 in F; V(s) = Dev_V(s) = 0 off F), at
raises it is >= 0.  By (a), C~'_l >= 0, and C~'_l > 0 exactly on G; by Lemma 2.2 sum C~'_l pi_l >= (7/(8H(L))) ||C~||_1.  By
Lemma 2.1(i) and (c), 0 < V(zhat) = sum lambda~ kappa_m M(rc) <= beta kappa_max ||lambda~||_1 <= beta kappa_max Des^C ||C~||_1.
Insert into (2.1).  For (2.3) use nu + a_J <= nu + ||a||_1 = 1 and kappa_V < 0.  QED

READING.  At the start row the cofactor combination V of ANY (R-S1) obstruction satisfies V(zhat) ~ 0 (the minors are tiny),
while its private signature part contributes the robust positive amount sum C~' pi >= ||C~||/H(L) (the near coordinates of
kind-(iv) carriers are aligned with the data sign).  The obstruction conditions (b') forbid every shared design-depth
coordinate from cancelling this amount (each contributes >= 0).  The only remaining term is the COMMON MODE kappa_V (nu + a_J):
an (R-S1) obstruction exists only if the cofactor combination has a robustly NEGATIVE common mode.  This is the restricted-
model counterpart of the pure (U*) normal form of Part III (Theorem III-Aobs(3), H2 Fact 1.2), now with an explicit vector V
attached to the minors.

## 2.3 Consequences: proportional support, Hilbert localization, free-target resonances

COROLLARY 2.4 (two-sided support is proportional).  PROVED (same chain as Theorem 2.3(B)).  Let lambda~ be an (R-S1)
obstruction at a stage as in Theorem 2.3(B).  Then:
 (i)  at every design-depth s in F cap U_L carrying a two-sided generator (TS; zero-data S_th/ZD) one has s in supp V and
      V(s) = kappa_V a_s;
 (ii) every thick design-depth support coordinate s (|a_s| >= u/2) lies in supp V, i.e. is a coordinate of a carrier of the
      resonant group G, and V = kappa_V a there; in particular there is no anchor (consistent with Cor. III-Asuff(b));
 (iii) at every data-carrying S_th coordinate s: z_s V(s) >= kappa_V |a_s| (that is, z_s Dev_V(s) >= 0); at every FR and
      every ZD coordinate off F: V(s) = 0.
Proof.  (b') at s in F with a two-sided generator gives Dev_V(s) = V(s) - kappa_V a_s = 0; kappa_V != 0 by (2.3) and
a_s != 0, so V(s) != 0.  (ii) is (i) for TS coordinates (U_L contains every thick design-depth support coordinate that is
not an anchor, and an anchor s notin U_L would have V(s) = 0 != kappa_V a_s).  (iii) is (b').  QED

COROLLARY 2.5 (Hilbert localization: the compensation sits on thick support of the group).  PROVED (same chain).  Under
Theorem 2.3(B), with nu_f := nu(R_1) > 0:
 (i)   sum_{s in F} mu_s^2 V(s) a_s = kappa_V nu^2 <= -nu^2 ||C~||_1/(2H(L));
 (ii)  the private coordinates contribute at most mu*_{s_max(L)+1}^2 ||C~||_1 to the left side of (i), and with a positive
       sign on the near (aligned) coordinates; S_th coordinates (mass <= 2b, or theta <= 2b after P^nat) contribute at most
       2b ||C~||_1 in modulus;
 (iii) hence, for L large (2b + mu*_{s_max(L)+1}^2 <= nu_f^2/(8 H(L))), the thick support in J carries the compensation:
       sum_{s in J cap TS} mu_s^2 |a_s| |V(s)| >= nu^2 ||C~||_1/(4 H(L)),  in particular J cap TS != {} .
Proof.  (i) is the definition of kappa_V and (2.3).  (ii) On P_l, V(s) a_s = C~_l v_l(s) a_s; at near coordinates
sgn a_s = eps_l (Lemma 2.2) and C~_l = eps_l C~'_l, so the term is C~'_l v_l(s) |a_s| >= 0; every s in P_l exceeds s_max(L),
so mu_s <= mu*_{s_max(L)+1}, and sum |V(s)||a_s| <= ||C~||_1 ||a||_1 <= ||C~||_1.  At S_th coordinates |a_s| <= 2b and
mu_s <= 1.  (iii) Design-depth support is TS or S_th at R_1 (clean classification, Lemma III-prep(d)); coordinates of
F beyond design depth have mu_s <= mu*_{dbar(L)} and are absorbed like the private ones; split (i).  QED
The smallness condition in (iii) holds for L large: nu_f is fixed (nu at R_1 differs from nu at f by o(1)), while
b(w) <= Des(L)^{-C}, H(L) <= Des(L), and mu*_s = 2^{-2^{2^s}} is doubly exponential in s.

COROLLARY 2.6 (resonances without thick support in their coordinates are never (R-S1)).  PROVED (same chain).  If no
coordinate s <= s_max(L) of a carrier of a candidate group G is thick support of R_1, then no (R-S1) obstruction has
resonant group G.  In particular the Example-4.3 shape with a FREE common target (G1 Cor. 5.3(iii)) whose carriers have no
thick support among their coordinates below s_max(L) is never (R-S1)-residual, whatever the other generators.
Proof.  Corollary 2.5(iii).  QED

PROPOSITION 2.6' (free-target pairs have ROBUST minors).  PROVED (algebra + Lemma 2.2; no obstruction condition used).
Let l_+, l_- be kind-(iv) carriers of a (U)-block at an (R1)-type stage, j a common FREE target (robust room) and M =
det[[r_+, r_-], [u_+(j), u_-(j)]] (in G1's convention M(r) = C_+ r_+ + C_- r_- with C_+ = u_-(j), C_- = -u_+(j) up to a common
sign).  Assume: the oriented cofactors eps_+ C_+, eps_- C_- have the same sign sigma; no coordinate s <= s_max(L) of u_+ or
u_- is thick at R_1; and every coordinate s <= s_max(L), s != j, of u_l (l = +, -) is ALIGNED: eps_l u_l(s) z_s >= 0.  Then for
L large
      sigma M(rc) >= (3/4)(|u_+(j)| + |u_-(j)|)/(H(L) kappa_m)     (the minor is robust, not tiny).
Proof.  Take lambda~ := sigma/kappa_m, so C~'_l = sigma eps_l C_l/kappa_m >= 0, ||C~||_1 = (|C_+| + |C_-|)/kappa_m, and
V(zhat) = sigma M(rc) (Lemma 2.1(i)).  In (2.1): V(j) = 0 (repeated row); at every other s in J, V(s) z_s = C~_l u_l(s) z_s =
C~'_l eps_l u_l(s) z_s >= 0, and at s in J cap F (necessarily S_th, |a_s| <= 2b) the extra term -kappa_V |a_s| is >= -2b|J|
|kappa_V|; a_J <= 2b|J|.  kappa_V = sum_{s in F} mu_s^2 V(s) a_s/nu^2: at S_th coordinates of J, V(s) a_s = V(s) z_s |a_s| >= 0;
at near private coordinates >= 0 (Corollary 2.5(ii)); the remaining private coordinates contribute >= -mu*_{s_max(L)+1}^2
||C~||_1/nu^2; so kappa_V >= -mu*_{s_max(L)+1}^2 ||C~||_1/nu^2, and |kappa_V| <= Des^C ||C~||_1/nu (crude bound
|<U^*V, e>| <= ||V||_1).  Hence sigma M(rc) >= ||C~||_1 (7/(8H(L)) - mu*_{s_max(L)+1}^2/nu - 4 b |J| Des^C/nu) >= (3/4)
||C~||_1/H(L) for L large.  QED
So the configuration that G1 Cor. 5.3(iii) left open (free common target, other generators parallel or wrong-signed) is not
even a TINY minor unless the pair has thick or anti-aligned coordinates below s_max(L); with anti-aligned coordinates it can be
tiny, but then (Theorem 2.3(B)) those coordinates cannot serve an obstruction, and the thick support is again forced.

## 2.4 The escape of an (R-S1) group is the COMMON MODE (correction to G3-ref R-ESC.2)

The universal identity behind Theorem 2.3 holds for ANY finite combination of carriers, in particular for the switching
vector of the mate data, and it exhibits an escape that the bookkeeping of G3-ref R-ESC treats as an error term.

LEMMA 2.7 (exact escape identity at the norm level).  PROVED (any admissible design with the structure of 2.0, any row,
mate and scale; algebra + (2.0)).  Let gamma_l (l in G) be numbers with eps_l = sgn gamma_l, V^G := sum_G gamma_l u_l,
J, P_l as in 2.0, pi_l := eps_l sum_{P_l} v_l(s) z_s.  Then
      sum_{l in G} |gamma_l| pi_l  =  V^G(zhat) - kappa_{V^G} (nu + a_J) - sum_{s in J} Dev_{V^G}(s) z_s .           (2.4)
In R-ESC's notation (J_c := J), sum_G gamma_k Rt_k = sum_G |gamma_k| pi_k + kappa_{V^G} nu, i.e. the Hilbert terms
"h_k" of R-ESC are, summed over the group, EXACTLY the common mode kappa_{V^G} nu.
Proof.  (2.1) with C~ replaced by gamma (the proof of (2.1) used only the support structure).  For the second claim:
Rt_k = u_k(zhat) - sum_{J} u_k(j) z_j = sum_{P_k} u_k(s) z_s + <U^* u_k, e> = sum_{P_k} v_k z + kappa_{u_k} nu, and kappa is
linear.  QED

CONSEQUENCE 2.8 (what an escape must be).  PROVED as stated.
 (i)  For an active group (|gamma| large) in an unshifted block, (2.4) together with |V^G(zhat)| <= |V(zhat)| + |V^rest(zhat)|
      (CL0: |V(zhat)| <= t/q_0) says: the aligned private mass sum |gamma| pi >= (7/(8H(L))) sum |gamma| (Lemma 2.2) must be
      compensated by (1) anti-aligned deviations z_s Dev_{V^G}(s) < 0 at the group's coordinates up to s_max(L) -- at support
      coordinates these are the cushion escapes of R-ESC, at free/contact coordinates they are pinned by Lemma 1.4 -- or by
      (2) the COMMON MODE kappa_{V^G}(nu + a_J) < 0, or by (3) the switching of carriers outside G (V^rest(zhat)).
 (ii) G3-ref R-ESC.2 bounds (2) by -sum |gamma_k| h_k and asserts c_k >= N_k - U_far(k) - h_k >= c/H(L) "mod chain".  This is
      not automatic: h_k >= |kappa_{u_k}| nu, and kappa_{u_k} = sum_s p_s u_k(s)/a_s is of order |u_k(s_0)|/|a_{s_0}| when u_k has
      mass at a Hilbert-dominant support coordinate s_0 (p_{s_0} ~ 1), so h_k can be of order mu*_{s_0} >> 1/H(L) (e.g. mu*_1 =
      1/16).  The list of escapes in R-ESC.2 must be completed by (2).
 (iii) By Theorem 2.3, (2) is EXACTLY the escape used by every (R-S1) obstruction: the cofactor combination V has
      kappa_V <= -||C~||_1/(2H(L)), and by Corollaries 2.4-2.5 it is carried by thick support of the group, on which V = kappa_V a.
      By contrast, by Theorem 2.3(B) and Corollary 2.4(iii), escapes of type (1) at S_th, FR, ZD or contact coordinates are
      INCOMPATIBLE with the obstruction conditions (each such coordinate contributes >= 0 to the left side of (2.1)), and
      outside switching does not enter V at all.  So in the "(R-S1) + escape" residual of ADDENDUM 14b, the escape is always
      the common mode through thick (Hilbert-visible) group support; thin shared support (G-THIN), outside switching and
      other active strict non-peaks are never what makes an (R-S1) obstruction possible.
 (iv) The escape provides NO first-order lever in the restricted model: at thick s in supp V the TS action Dev_V(s) vanishes
      (Cor. 2.4), and at thick s notin supp V there is none (Cor. 2.4(ii)).  [HEURISTIC remark: second-order TS moves change M
      by ~ -kappa_V delta^2 eff/kappa_m, of the wrong sign -- the global rigidity of J1 Lemma J1.4 in this setting.]

## 2.5 Persistence: what (R-S1) at all large stages requires, and a design clause that excludes it

PROPOSITION 2.9 (persistence forces f's thick profile into the cofactor spans).  PROVED as a necessary condition (mod
chain: Theorem 2.3, Corollary 2.4, H2 Lemmas 2.6-2.7 (memory)).  Suppose that at two consecutive (R1) main stages L < L'
(both >= some L_0) the selected stages are (R-S1) in the restricted model, with obstructions lambda~_L, lambda~_{L'}, cofactor
combinations V_L, V_{L'} (normalized ||C~||_1 = 1) and resonant groups G_L, G_{L'}.  Let A be a finite set of support
coordinates of f with |a_s| >= u(w_L)/2 and s <= dbar(L) for s in A (thick at both stages; every finite A of F qualifies
for L_0 large, since u(w_L) -> 0 and dbar(L) -> infinity).  Then:
 (i)   G_L and G_{L'} are DISJOINT (memory: a kind-(iv) carrier of an (R1) stage is zero-data at the next (R1) main stage,
       and G consists of kind-(iv) carriers by (a));
 (ii)  V_L = kappa_{V_L} a^(L) and V_{L'} = kappa_{V_{L'}} a^(L') on A, with kappa_{V_.} <= -1/(2H(.)) (Corollary 2.4(ii),
       Theorem 2.3); here a^(L) is the base of the Step-A input row of stage L, which on A equals c_L a (c_L > 0: the deep
       raise, the preparation and the pre-placements do not move thick design-depth coordinates of a fixed finite A once L is
       large; the renormalization q* = 1 is a common factor);
 (iii) consequently V_L|_A and V_{L'}|_A are both proportional to a|_A: the 2 x 2 determinants
            det[[V_L(s), V_L(s')], [V_{L'}(s), V_{L'}(s')]]                                                    (2.5)
       vanish for all s, s' in A;
 (iv)  if stage L carries p_L tiny strict minors (in the (U)-blocks of the obstruction) then V_L lies in the span S_L of their
       block cofactor combinations V_{M_i} := sum_{l in m_i} C_{M_i, l} u_l (i <= p_L); so a|_A lies in S_L|_A cap S_{L'}|_A.
Proof.  (i) H2 Lemma 2.6(b), 2.7.  (ii)-(iii): Corollary 2.4(ii) at each stage; the base statement is bookkeeping of the
operations preceding Step A (Part III Definition III-prep, Lemma III-prep; deep raise beyond D(L); TU pre-placements at far
pull coordinates).  (iv) V_L = sum_i lambda~_i V_{M_i} by Definition 2.0.  QED
[In the near-certificate (not exactly Farkas) version, (ii) holds up to |V(s) - kappa_V a_s| <= tol_L := Des(L) eps(L) per
coordinate (eps(L) <= u(w_L)^3 Des(L)^{-C} the certificate size), and (2.5) is O(Des^C (tol_L + tol_{L'})/nu).]

DESIGN CLAUSE (D-sep) (SKETCH: genericity argument below; compatibility with every other clause of T_fin^{K2} + G1's
additions is not checked line by line; the quantifier point (Q) below must be checked against the recursion).
Potential minors.  A potential (U)-type single-(X3) strict minor M is specified by its block, its columns and its FR-row
set among target coordinates; its group G_M is the set of columns with nonzero cofactor, V_M := sum_{l in G_M} C_{M,l} u_l,
and birth(M) is the design stage of the youngest carrier of G_M.  We also count every single carrier l as a (pseudo-)minor
with V = u_l, G = {l}.  For coordinates s != s' with V_M(s') != 0 put r_M(s, s') := V_M(s)/V_M(s') (the (s, s')-SLOPE of M).
Tolerances.  For a main stage L put
      E_L := max over the clean sub-windows w of L of  Des(L)^{C_1} H(L) eps(w)/u(w)          (C_1 := 2),
where eps(w) <= u(w)^3 Des(L)^{-C} is the Step-A certificate size (so E_L <= Des(L)^{3-C} u(w)^2 is tiny); window thresholds
are chosen recursively below all earlier quantities, so E_L is nonincreasing in L.  For a design stage B let prev(B) be the
last main stage strictly before B and Tau(B) := E_{prev(B)} (a quantity fixed before the targets of stage B are chosen).
(D-sep) requires, at every design stage B, for all potential minors M, M' with DISJOINT groups and max(birth(M), birth(M'))
= B, and all s != s' <= s_max(B) at which V_M(s), V_M(s'), V_{M'}(s), V_{M'}(s') are all nonzero:
      | r_M(s, s') - r_{M'}(s, s') |  >=  C_0 Tau(B)          (C_0 := 1).                                        (2.6)
[Equivalently |V_M(s) V_{M'}(s') - V_M(s') V_{M'}(s)| >= C_0 Tau(B) |V_M(s')| |V_{M'}(s')|.]
Why achievable (SKETCH).  Say birth(M') = B.  If a carrier l'_0 of stage B in G_{M'} has s' (or s) in its target support,
perturb t := y_{l'_0}(s'): V_{M'}(s') is affine in t with slope C_{M',l'_0} != 0 (the cofactor of column l'_0 does not involve
that column, the other cofactors involve it only at FR rows of M', and s' is not an FR row of M' since V_{M'}(s') != 0 by
the repeated-row identity), V_{M'}(s) does not depend on t, and r_{M'} = V_{M'}(s)/V_{M'}(s') is a non-constant Moebius
function of t; the bad set {t : |r_{M'}(t) - r_M| < C_0 Tau(B)} is an interval of length O(Tau(B) K_B), K_B a stage-B design
quantity.  If no stage-B carrier of G_{M'} is nonzero at s, s', then r_{M'} depends on the stage-B targets only through the
cofactors (target values at FR rows), and either it is non-constant in them (same argument) or it is identically equal to
the slope of a sub-combination of OLDER carriers of G_{M'}, i.e. r_{M'} = r_{M''} for an older (pseudo-)minor M'' with
G_{M''} contained in G_{M'} (in the extreme case a single old carrier), and then (2.6) for (M, M') is (2.6) for (M, M''),
which holds from the earlier birth with Tau(birth) >= Tau(B) (prev is nondecreasing, E nonincreasing).  [This last
reduction is the part of the genericity argument that is only sketched: the identically-constant case must be shown to be
always of this form.]  Finitely many conditions, each excluding a set of measure O(Tau(B) K_B), are met by a perturbation
of the new targets below the density tolerance delta_B of the target pool, PROVIDED
   (Q)  Tau(B) K_B N_B < delta_B   (N_B := number of conditions at stage B),
where K_B, N_B, delta_B are stage-B quantities and Tau(B) is fixed before.  (Q) is automatic if the recursion may choose the
window thresholds of a main stage L after the targets of the design stages in (L, L'] (L' the next main stage), or if
delta_B may be taken >= Tau(B) K_B N_B; otherwise it is a genuine constraint relating the main-stage tolerance E_L to the
target geometry of the following design stages.  Density of every block in S_Y (Lemma B) and the combinatorial
allowedness rules are unaffected by small perturbations.  NOT checked: (Q) in the actual recursion; that no other clause
fixes a target value exactly (e.g. absorber targets of rounds PRE/CLUSTER).

THEOREM 2.10 (single-minor (R-S1) cannot persist under (D-sep)).  PROVED modulo (D-sep) and the chain of Proposition 2.9.
Let f have at least two support coordinates (every f with infinite base support, the (LSC-trunc) case, qualifies).  There is
L_1 such that no two consecutive (R1) main stages L < L', L >= L_1, are both (R-S1)-residual in the restricted model through
obstructions supported on a single tiny strict minor each, in the near-certificate form of Proposition 2.9 with
|V_L(x) - kappa_L a_x| <= Des(L) eps(w_L) on A.
Proof.  Fix s != s' in F := supp a(f), A := {s, s'}, a_A := (1/2) min(|a_s(f)|, |a_{s'}(f)|) > 0, and L_1 so large that for
L >= L_1: A is thick and below s_max(L) at stage L; the stage-L bases satisfy a^(L)|_A = c_L a(f)|_A with c_L >= 1/2
(Proposition 2.9(ii)); u(w_L) <= a_A^2; Des(L) >= 2^9.  By Proposition 2.9 the groups G_L, G_{L'} are disjoint and
V_L = c V_{M_L}, V_{L'} = c' V_{M_{L'}} (c, c' != 0, single minors), so r_L := V_L(s)/V_L(s') = r_{M_L}(s, s') and likewise at L'.
(1) Slopes are close.  Write V_L(x) = kappa_L a_x + e_L(x) (x in A; a = a^(L)), |e_L(x)| <= e := Des(L) eps(w_L),
|kappa_L| >= 1/(2H(L)) (Theorem 2.3), |a_x| >= a_A.  Then |V_L(s')| >= |kappa_L| a_A - e >= |kappa_L| a_A/2 (e is far smaller),
V_L(s), V_L(s') != 0, and
      |r_L - a_s/a_{s'}| = |e_L(s) a_{s'} - e_L(s') a_s| / (|a_{s'}| |V_L(s')|) <= 2e/(a_A |kappa_L| a_A/2) <= 8 H(L) e/a_A^2
                        <= 8 H(L) Des(L) eps(w_L)/u(w_L) <= 8 E_L/Des(L)^{C_1 - 1} <= E_L/64.
Since a^(L)|_A and a^(L')|_A are both positive multiples of a(f)|_A, a_s/a_{s'} is the same at both stages; the same bound at
L' (with E_{L'} <= E_L) gives |r_{M_L}(s, s') - r_{M_{L'}}(s, s')| <= E_L/32.
(2) Slopes are separated.  Let B := max(birth(M_L), birth(M_{L'})) <= L'.  Since M_L is residual at L, birth(M_L) <= L.  If
birth(M_{L'}) <= L then B <= L, prev(B) <= L and Tau(B) = E_{prev(B)} >= E_L; otherwise B lies in (L, L'] and prev(B) = L
(L, L' consecutive main stages), so Tau(B) = E_L.  The four values are nonzero and the groups disjoint, so (2.6) gives
|r_{M_L} - r_{M_{L'}}| >= C_0 Tau(B) >= E_L.
(1) and (2) contradict each other.  QED
[Remark.  The proof uses only that (s, s') are two FIXED coordinates of supp a(f): the slope of every residual cofactor
combination converges to a_s/a_{s'} at the rate H Des eps, while (D-sep) keeps the slopes of minors of disjoint groups apart
at a rate fixed before the younger group is born.]

REMARK 2.11 (what remains of (R-S1) after Theorem 2.10).  OPEN.
 (a) Multi-minor stages: with p_L tiny strict minors, Proposition 2.9(iv) only gives a|_A in S_L|_A cap S_{L'}|_A.  A span
     version of (D-sep) (generic position of the cofactor spans of disjoint groups restricted to old coordinates) excludes this
     once |A| > p_L + p_{L'}; since every finite A of F becomes thick, persistence requires the number of SIMULTANEOUSLY tiny
     strict minors per stage to grow without bound, each tiny minor being a near-coincidence among f's ratios at precision
     b(w_L).  Neither excluded nor constructed.
 (b) Non-consecutive residual stages, stages where another residual class ((R-S2), (R-S3), (R-L), (R0^str)) intervenes:
     Theorem 2.10 needs two consecutive (R1) main stages both of type (R-S1).
 (c) Shifted blocks: Theorem 2.3 uses (U)-blocks (c_M = 0 in Lemma LE).  With an active shift, (2.1) acquires the term
     -sum lambda~ kappa_m c_M on the right of V(zhat) = ..., and no sign conclusion follows.
 (d) Outside the restricted model: G1 Prop. 5.2 is first order at the start row; second-order and band effects are the same
     as in G1 (Theorem G1.C).

## 2.6 Summary of part 2 (item (2) of the task)
 * PROVED (algebra, any admissible design with the u_l = y_l + v_l structure): the common-mode identity (2.1)/(2.4) for every
   finite combination of carriers; the R-ESC Hilbert terms h_k summed over a group are exactly the common mode kappa nu.
 * PROVED (mod chain, restricted model of G1 Prop. 5.2): every (R-S1) obstruction has a cofactor combination V with a robust
   NEGATIVE common mode kappa_V <= -||C~||_1/(2H(L)); V = kappa_V a on every two-sided design-depth support coordinate, which
   therefore all lie in the group's supports; the compensation is carried by THICK support of the group; S_th, FR, ZD and
   contact coordinates cannot carry it.
 * Hence the "(R-S1) + escape" residual has a definite escape: the common mode through thick group support.  Thin shared
   support (G-THIN), outside switching and other active strict non-peaks are never what makes an (R-S1) obstruction possible;
   the escape gives no first-order lever (TS actions vanish by proportionality).
 * PROVED: free-target pairs (G1 Cor. 5.3(iii) shape) without thick or anti-aligned coordinates below s_max(L) have ROBUST
   minors (Prop. 2.6'); without thick group support they are never (R-S1) (Cor. 2.6).
 * PROVED modulo a design clause (D-sep, SKETCH; its achievability needs the quantifier point (Q) of 2.5, unchecked against
   the recursion): single-minor (R-S1) cannot occur at two consecutive large (R1) main stages when F has >= 2 points
   (Theorem 2.10, slope form).  OPEN: multi-minor stages with unboundedly many simultaneously tiny strict minors;
   (R-S2), (R-S3), (R-L), (R0^str); shifted blocks.
 * Numerics: P2_work/cm_identity_check.py -- identity (2.1) exact to 8e-15 on 2000 random finite models; J1.1 to 4e-14;
   Prop. 2.6' toy: ratio >= 1.5 on 3000 instances (sanity only).

---

# P2 part 1: Problem R on the positive side -- what recovering approximants must do, what can be built, and the junction

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Setting of N3 Part 2 (one block, I = {1}): lambda_k = Phi(k) <=
2^{-1-k}, u_k := u_{k,1} with q*(u_k) = 1, psi' := R* w' = L* w' for a row f' (primed forced data; x' the normer of an
attaining row, xi the bidual normer in general), sigma', M', C' (M' + C' = 1, C' < 0.29, M' > 0.71), vartheta' :=
sigma' M'/C'.  Threshold lemma in pairing form: k is a peak of f' iff |u_k(x')| >= vartheta' Phi_k; its margin is mu'_k :=
|u_k(x')| - vartheta' Phi_k; a strict non-peak k has |w'(k)| = M' |u_k(x')|/(vartheta' Phi_k) and gap gamma'_k := M' - |w'(k)|.
Scale-t pairs (B+-, Omega+-) and the budget e <= t^2/2 for mates are as in N3 Def. 1.1 / Lemma 1.2; Lemma 2.2 of N3
(collective motion) and Lemma W, Lemma S of N3-ref are used as refereed.  Problem R (N3-ref Section 7): free coordinates
j, j' of f with pi_g(j) != pi_g(j') (pi_g := g/psi), no strict non-peak and no degenerate peak of f seeing {j, j'}.
Relation to the concurrent track P1 (r15/P1_notes.md): P1 proved Lemma SYM, Lemma P (cross-scale consistency on free
coordinates), the l_2-count capacity bound C2/C3 and Proposition N, and proposed the KSB approximants (keep the
staircase, shift on Z, bank) with model evidence.  The results below are complementary and are cross-referenced there.

## 1.1 Oriented profile identity and the two-signed requirement

LEMMA 1.1 (oriented profile identity).  PROVED (algebra on N3 Lemma 2.2).  Let f' be any row, g' in X* with g'(xi') = 0,
t in (0, 1], e := max_{+-} p*(f' +- t g') - 1 <= 1/2, and (B+-, Omega+-) a scale-t pair.  Put L+ := sup over peaks l of
s_l Omega+(l), L- := inf over peaks l of s_l Omega-(l) (s_l := sign of w'(l)), eps+_k := L+ - s_k Omega+(k) >= 0 and
eps-_k := s_k Omega-(k) - L- >= 0 for every peak k, d+- := -L+-/M', and
   E+ := sum over peaks k of lambda_k s_k eps+_k u_k,        E- := sum over peaks k of lambda_k s_k eps-_k u_k,
   N+- := sum over strict non-peaks k of lambda_k (Omega+-(k) + d+- w'(k)) u_k.
Then, exactly (all series absolutely convergent in l_1),
      g' = B+ - d+ psi' - E+ + N+  =  B- - d- psi' + E- + N- .                                                    (1.1)
Proof.  g' = B+- + L* Omega+-.  On peaks Omega+(k) = s_k (L+ - eps+_k) and Omega-(k) = s_k (L- + eps-_k) (definitions of
eps+-).  Since w'(k) = s_k M' on peaks, psi' = M' sum_{peaks} lambda_k s_k u_k + sum_{non-peaks} lambda_k w'(k) u_k, so
sum_{peaks} lambda_k s_k u_k = (psi' - sum_{non-peaks} lambda_k w'(k) u_k)/M'.  Substitute into L* Omega+ = L+ sum_{peaks}
lambda_k s_k u_k - E+ + sum_{non-peaks} lambda_k Omega+(k) u_k and collect; likewise for the minus side.  The coefficients
are bounded by |L+-|, ||Omega+-||_inf <= (2 + e)/t (N3 Lemma 2.2) and sum_k lambda_k ||u_k||_1 < infinity.  QED

COROLLARY 1.2 (two-signed requirement).  PROVED.  Let f' be any row, g' in C(f'), j != j' free coordinates of f' with
psi'_j psi'_{j'} != 0, pi(i) := g'_i/psi'_i, Delta := pi(j) - pi(j') != 0, sigma := sign of Delta, and for every carrier k
the DISCREPANCY D_k := u_k(j)/psi'_j - u_k(j')/psi'_{j'}.  Split the peaks into the two ORIENTED CLASSES
P'_+ := {peaks k : sigma s_k D_k > 0} and P'_- := {peaks k : sigma s_k D_k < 0}.  Put m_k(t) := min(t/(2 mu'_k), 5 lambda_k/t)
(read as 5 lambda_k/t at degenerate peaks) and A := (1/q'_0)(1/((1 - |z'_j|)|psi'_j|) + 1/((1 - |z'_{j'}|)|psi'_{j'}|)).  Then
for every t in (0, 1]:
   (i)  |Delta| <= (A/2) t + sum_{k in P'_-} m_k(t) |D_k| + (7/t) sum_{strict non-peaks k} lambda_k |D_k|,
   (ii) |Delta| <= (A/2) t + sum_{k in P'_+} m_k(t) |D_k| + (7/t) sum_{strict non-peaks k} lambda_k |D_k|.
(iii) (rate form) If no strict non-peak of f' sees {j, j'} and, for ONE of the two classes, eta_pm(mu_0) := sum over k in
      that class with mu'_k < mu_0 of lambda_k |D_k| is o(mu_0/log^2(1/mu_0)) as mu_0 -> 0, then Delta = 0.
So an oscillation of a mate between two free coordinates needs, in EACH oriented class separately, near-kernel mass that
violates the log^2 margin-sparsity rate (or strict non-peaks seeing the pair).
Proof.  Divide (1.1) at i = j by psi'_j and at i = j' by psi'_{j'} and subtract: the d+- terms cancel and
   Delta = b+ - sum_{peaks} lambda_k eps+_k s_k D_k + n+  =  b- + sum_{peaks} lambda_k eps-_k s_k D_k + n-,
with b+- := B+-_j/psi'_j - B+-_{j'}/psi'_{j'} and n+- := sum_{strict non-peaks} lambda_k (Omega+-(k) + d+- w'(k)) D_k.  Take
sigma = +1 (otherwise exchange j and j').  Since eps+-_k >= 0, the peaks with s_k D_k > 0 contribute <= 0 to the first
expression and the peaks with s_k D_k < 0 contribute <= 0 to the second; hence
   Delta <= |b+| + sum_{s_k D_k < 0} lambda_k eps+_k |D_k| + |n+|,    Delta <= |b-| + sum_{s_k D_k > 0} lambda_k eps-_k |D_k| + |n-|.
Budget (N3 Lemma 1.2(a),(b), j, j' free, e <= t^2/2): (1 - |z'_i|)|B+-_i| <= e/(q'_0 t) <= t/(2 q'_0) for i in {j, j'}, so
|b+-| <= A t/2.  Lemma W (N3-ref): lambda_k eps+-_k <= m_k(t) at peaks with mu'_k > 0, and lambda_k eps+-_k <= lambda_k (|L+-| +
||Omega+-||_inf) <= 5 lambda_k/t at every peak.  |Omega+-(k) + d+- w'(k)| <= 2.5/t + 2.5/(0.71 t) <= 7/t.  This gives (i), (ii).
(iii) Let D_bar := 1/|psi'_j| + 1/|psi'_{j'}| >= |D_k| (||u_k||_inf <= 1).  For the class in question,
sum m_k(t)|D_k| <= D_bar sum_{mu'_k >= mu_0} min(t/(2 mu_0), 5 lambda_k/t) + 5 eta(mu_0)/t <= D_bar t l(t)/mu_0 + 5 eta(mu_0)/t
by Lemma S (l(t) = log_2(1/t) + 2.2).  If eta(mu_0) = 0 for some mu_0 let t -> 0.  Otherwise take t := (eta mu_0)^{1/2}
(<= mu_0 <= 1 for small mu_0) and x := eta/mu_0: |Delta| <= (A/2)(eta mu_0)^{1/2} + D_bar l(t) x^{1/2} + 5 x^{1/2}, and
l(t) = (1/2) log_2(1/x) + log_2(1/mu_0) + 2.2; x^{1/2} log_2(1/x) -> 0 and x^{1/2} log_2(1/mu_0) -> 0 by the rate hypothesis.
QED
Remarks.  (a) This refines N3-ref Lemma R-W (which bounds the unoriented mass): at f in the Problem-R configuration BOTH
oriented classes of small-margin peaks seeing {j, j'} must violate the rate; in particular each contains infinitely many
peaks.  (b) The same holds at every recovering approximant (with D_k, s_k computed there).  A strict non-peak contributes
to both (i) and (ii) (term n+-): it is two-sided, which is why one converted carrier can replace both classes (P1's KSB).
(c) For larger free sets Z the identity (1.1) restricted to the free coordinates is the oriented form of P1's Lemma P:
-E+(t) + N+(t) and E-(t) + N-(t) are both within t/(2 q'_0) (room-weighted l_1 on the free set) of the line
g' + R psi' (N3 Lemma 1.2(a),(b)); the free-coordinate profile of g' (modulo psi') is simultaneously a limit of
nonnegative and of nonpositive combinations of oriented peak vectors s_k u_k with coefficients <= m_k(t).

## 1.2 Nested tuning: norm-attaining rows near f with prescribed deep near-threshold carriers exist (any admissible T)

PROPOSITION 1.3 (nested tuning by a fixed point).  PROVED.  Let a' be finitely supported with q*(a') = 1, e' :=
U*a'/||U*a'||, W a finite set containing supp a', z° in [-1, 1]^W with z° = sign a' on supp a', k_1, k_2, ... distinct
carriers, s_1, s_2, ... distinct coordinates outside W, and numbers A_i, B_i (target type of k_i) and 0 < tau_bar_i <= 1
with tau_bar_i -> 0.  For tau in the box K := product of the intervals [-tau_bar_i, tau_bar_i] let z'(tau) := z° on W,
z'(tau)(s_i) := tau_i sign u_{k_i}(s_i), z'(tau) := 0 elsewhere; y'(tau) := z'(tau) + U e'; x'(tau) := y'(tau)/p(y'(tau));
f'(tau) := grad p(x'(tau)), with threshold vartheta'(tau).  Let vartheta_bar := sup_K vartheta', p_bar := sup_K p(y'),
m_i := |u_{k_i}(s_i)|, c_i := sum_{l != i} |u_{k_i}(s_l)|, N_i := sum_{s in W} u_{k_i}(s) z°(s) + <U* u_{k_i}, e'>.  If m_i > 0 and
      (|A_i| vartheta_bar Phi_{k_i} + |B_i|) p_bar + |N_i| + c_i sup_l tau_bar_l  <=  tau_bar_i m_i      for every i,       (1.2)
then there is tau* in K such that, for every i,  u_{k_i}(x'(tau*)) = A_i vartheta'(tau*) Phi_{k_i} + B_i.  The row f' :=
f'(tau*) attains its norm; with A_i = s_i in {-1, 1}, B_i = s_i mu_i (mu_i >= 0) the carrier k_i is a peak of f' of sign s_i
and margin exactly mu_i; with |A_i| < 1, B_i = 0 it is a strict non-peak of f' with gap M'(1 - |A_i|).
Proof.  (1) Continuity.  For tau, tau' in K and every I, ||z'(tau) - z'(tau')||_inf <= max(max_{i<I}|tau_i - tau'_i|,
2 sup_{i>=I} tau_bar_i); since tau_bar_i -> 0, tau -> z'(tau) is continuous from the product topology into c_0 with the sup
norm, and z'(tau) lies in the unit ball of c_0 with z' = sign a' on supp a'.  By [I, prop:smooth(c)] q(y'(tau)) = 1, f'(tau)
attains its norm at x'(tau) and x'(tau) is its normer; p is continuous on X and q(x) <= ||x||_inf, so x'(tau) is norm
continuous, f'(tau) is norm continuous by [I, prop:smooth(b)], and vartheta'(tau) is continuous by [I, prop:continuity]
(along norm convergent rows sigma, M, C converge and C > 0).  K is compact (Tychonoff), so vartheta_bar, p_bar < infinity.
(2) The map.  u_{k_i}(x'(tau)) = <y'(tau), u_{k_i}>/p(y'(tau)) = (N_i + tau_i m_i + X_i(tau))/p(y'(tau)) with
X_i(tau) := sum_{l != i} tau_l u_{k_i}(s_l) sign u_{k_l}(s_l), |X_i| <= c_i sup tau_bar.  Define
Gamma_i(tau) := ((A_i vartheta'(tau) Phi_{k_i} + B_i) p(y'(tau)) - N_i - X_i(tau))/m_i.  Each Gamma_i is continuous on K (X_i is
a uniformly convergent series of continuous functions), and (1.2) gives |Gamma_i| <= tau_bar_i, so Gamma maps the compact
convex set K (in the locally convex space R^N) continuously into itself.  The Schauder-Tychonoff theorem gives a fixed
point tau*, i.e. tau*_i m_i = (A_i vartheta' Phi_{k_i} + B_i) p - N_i - X_i, which is the claimed identity.  The type
statements are the threshold lemma in pairing form.  QED

COROLLARY 1.4 (richly non-C-tame attaining rows near every row).  PROVED.  Let f be any element of S_{p*}, delta > 0, Z a
finite set of free coordinates of f, and for i >= 1 let h_i in R^Z with ||h_i||_1 <= 1/4 and eps_i > 0 be given, together
with types (A_i, B_i) as in Proposition 1.3 with |A_i| <= 1.  There are numbers mu_bar_i > 0 and phi_i > 0 (determined by the
construction) such that whenever |B_i| <= mu_bar_i for all i, there exist an attaining row f' with p*(f' - f) < delta,
z' = z on a window containing Z, and distinct carriers k_i with Phi_{k_i} <= phi_i, ||u_{k_i} 1_Z - h_i/c_i'||_1 <= eps_i for
normalizing factors c_i' in [1/2, 5/2], such that u_{k_i}(x') = A_i vartheta' Phi_{k_i} + B_i for all i.  The B_i may be
chosen AFTER the carriers.  In particular one may prescribe two interleaved sequences of peaks seeing Z, one in each
oriented class (discrepancies |D_k| >= d_0 > 0), with margins mu_i := min(mu_bar_i, lambda_{k_{i+1}}); then the near-kernel
mass of each class satisfies eta(mu_0) >= d_0 mu_0 for all small mu_0, so the log^2 margin-sparsity rate fails at Z in both
classes.  Or: infinitely many strict non-peaks with exactly zero pairing (A_i = B_i = 0).
Proof.  (a) Window.  By [I, prop:approximants] ((ii) implies (i)): if W_n increase to N, a'_n -> a in l_1 (finitely
supported, q* = 1, same signs as a, supp a'_n = supp a cap W_n) and z''_n = z on W_n with ARBITRARY tails in the unit ball
of c_0, then the rows grad p(z''_n + U e''_n) converge to f.  Hence there is n with: every such row built from (W_n, a'_n)
is within delta of f (otherwise a sequence of bad tails would contradict the convergence).  Fix W := W_n containing Z, a' :=
a'_n, z° := z on W (z = sign a' on supp a').  Shrinking delta first, all these rows have vartheta' <= 2 vartheta (continuity of
the forced data at f), and p(y') = 1 + ||L y'|| <= 3/2 (q(y') = 1, ||R_1|| <= 1/2).  So vartheta_bar <= 2 vartheta, p_bar <= 3/2.
(b) Shapes.  Let Lambda(v) := sum_{s in W} v(s) z(s) + <U* v, e'> (only s in supp a' enter the second sum) and fix c in supp a'
(Lambda(e_c) = sign a'(c) + mu_c^2 a'(c)/||U*a'|| != 0).  For i >= 1 choose s_i outside W beyond S_{i-1} (below), put
v_i := h_i + beta_i e_c + (1/2) e_{s_i} with beta_i := -Lambda(h_i)/Lambda(e_c) (so Lambda(v_i 1_W) = 0; |beta_i| <= beta_max :=
1/2, as |Lambda(h)| <= 2||h||_1 and |Lambda(e_c)| >= 1), and vhat_i := v_i/q*(v_i), c_i' := q*(v_i) in [1/2, 2(3/4 + beta_max)].
(c) Carriers.  By (T-d) every tail of (u_k) is dense in S_{q*}: choose k_i not in {k_1, ..., k_{i-1}} with Phi_{k_i} <= phi_i
and ||u_{k_i} - vhat_i||_1 <= eps'_i := min(eps_i, tau_bar_i m_low/16), where m_low := 1/(4 c_max') and tau_bar_i := 2^{-i}.  Then
choose S_i >= s_i so large that ||u_{k_l} 1_{(S_i, infinity)}||_1 <= eps'_l 2^{-i-1} for all l <= i.
(d) Hypotheses of Proposition 1.3.  m_i >= 1/(2 c_i') - eps'_i >= m_low; |N_i| = |Lambda(u_{k_i} 1_W)| <= |Lambda(vhat_i 1_W)| +
2 eps'_i = 2 eps'_i; c_i <= (mass of u_{k_i} - vhat_i on {s_l : l < i}) + sum_{l > i} ||u_{k_i} 1_{(S_{l-1}, inf)}||_1 <= 2 eps'_i.
So (1.2) holds if 3 vartheta phi_i + 1.5 mu_bar_i + 4 eps'_i <= tau_bar_i m_low: take phi_i := tau_bar_i m_low/(12 vartheta + 1)
and mu_bar_i := tau_bar_i m_low/6.  Proposition 1.3 gives tau*; z'(tau*) has tail in the unit ball of c_0 (|tau*_i| <= 2^{-i}),
so f' is within delta of f by (a), and Z is free at f' (z' = z there).  The B_i enter only through (1.2), so they may be fixed
after all carriers are chosen.  For the last claim choose h_i with the prescribed sign of the discrepancy (|D_k| >= d_0 for the
row close to f, as psi' is close to psi), A_i = s_i putting k_i in the desired class, and mu_i := min(mu_bar_i,
lambda_{k_{i+1}}); for mu_0 in (mu_{i+1}, mu_i] the class contains k_{i+1} (or k_{i+2}) with margin < mu_0, so eta(mu_0) >=
d_0 lambda_{k_{i+1}} >= d_0 mu_i >= d_0 mu_0 (interleave the two classes and run the argument in each).  QED
Remarks.  (a) This settles the existence question left OPEN in N3 Section 1.6 ("existence of non-C-tame NA rows near a
given f for a given T"): they exist for EVERY admissible T and every f, with infinitely many prescribed near-threshold
carriers of prescribed profile on Z, prescribed sign class and prescribed margins (or zero pairings).  No rate hypothesis on
T is used: the tuning precision is exact (fixed point), and the far coordinates s_i are private by construction.
(b) What it does NOT give: that the tuned rows have mates with the oscillation of rho g.  Corollary 1.2 and P1's Lemma P are
necessary conditions which such rows can be made to satisfy; sufficiency is the capacity/junction question of 1.4.
(c) A one-carrier version with a NEAR move (P1's "shift on Z") is the following conversion lemma, proved the same way with a
one-parameter family and the intermediate value theorem: if k sees a free coordinate j (u_k(j) != 0), the rows obtained by
changing z' at j by delta (|z'_j + delta| < 1) are norm continuous in delta, u_k(x'(delta)) moves with derivative
u_k(j)/p(y') + O(Phi_k + mu_k + |delta|) while vartheta' moves continuously, so a shift |delta| <= 4(mu_k + 2 vartheta Phi_k)/|u_k(j)| (for
the row close to f and Phi_k, mu_k small; p(y') <= 3/2) turns a peak k of margin mu_k into a strict non-peak of any prescribed
gap ratio, and changes the margin of every other peak l by at most |u_l(j)| |delta| + C |delta| |u_l(x')| + omega(|delta|) Phi_l,
omega a modulus of continuity of vartheta' along the family.  PROVED (intermediate value theorem; the derivative of
u_k(x'(delta)) is u_k(j)/p - u_k(x') (dp/d delta)/p, and u_k(x') = O(Phi_k + mu_k) for a near-threshold carrier).

## 1.3 Capacity of one strict non-peak: certificate radius and the sqrt-weight lower bound

PROPOSITION 1.5 (one strict non-peak as a certificate).  PROVED.  Let f' be any row, k a strict non-peak of f' with gap
gamma > 0, theta in (0, 1], omega := (theta C'^{1/2}/Phi_k) e_k, c := (0, omega).  Then c is a finite certificate,
      g_c = theta C'^{1/2} u_k - d psi',   d = theta Phi_k w'(k)/C'^{1/2},   H(c) = theta^2 (1 - Phi_k^2 w'(k)^2/C'^2) <= theta^2,
      r(c) = min( gamma Phi_k/(2 theta C'^{1/2}),  C'^{1/2}/(2 theta Phi_k |w'(k)|),  C'^{3/2}/(2 theta Phi_k |w'(k)| M') ),
and kappa(c) = 2|d| M'/C' <= 2 theta Phi_k/C'^{3/2}.  Consequently, for H(c) <= 1 - delta, p*(f' + s g_c) <= s(s) for all
|s| <= r_*(c, delta) [I, lem:slack(b)], and for Phi_k <= C'^{3/2}/4 this radius is min(gamma lambda_k/(2 theta C'^{1/2}),
delta/(2 kappa + 2), delta^{1/2}): a strict non-peak of weight lambda_k provides a TWO-SIDED direction of size theta C'^{1/2} u_k
(independent of lambda_k) at all scales below gamma lambda_k/(2 theta C'^{1/2}).
Proof.  [I, def:certificate]: (C1) holds with b = 0, (C2) with supp omega = {k} in Q'.  ||D omega||^2 = Phi_k^2 omega(k)^2 =
theta^2 C', d = <D w', D omega>/C' = Phi_k^2 w'(k) omega(k)/C', H = (||D omega||^2 - d^2)/C', and the radius and kappa are read
off the definitions (beta = 0).  [I, lem:slack(b)].  QED

COROLLARY 1.6 (sqrt-weight LOWER bound at a fixed row).  PROVED.  In Proposition 1.5 with Phi_k <= min(C'^{3/2}/4,
C'/100, 1/40) and theta^2 := gamma Phi_k/(4.04 (C' + Phi_k)), the direction g := theta C'^{1/2} u_k -
d psi' is a mate: g in C(f').  Its contribution is theta C'^{1/2} u_k = (gamma lambda_k C'/(4.04 (C' + Phi_k)))^{1/2} u_k, so for
every finite Z, Osc_Z(g; psi') = theta C'^{1/2} Osc_Z(u_k; psi') >= 0.49 (gamma lambda_k)^{1/2} Osc_Z(u_k; psi')
(as Phi_k <= C'/100).
Proof.  H(c) <= theta^2 <= 1/2; r_0 := r_*(c, 1/2) = min(r(c), 1/(4 kappa + 4), 2^{-1/2}) = gamma Phi_k/(2 theta C'^{1/2}) under the
hypotheses: kappa <= 2 theta Phi_k/C'^{3/2} <= 1/2, so 1/(4 kappa + 4) >= 1/6; the two other radius terms are >= 1; and
gamma Phi_k/(2 theta C'^{1/2}) = (gamma Phi_k)^{1/2} (4.04 (C' + Phi_k)/C')^{1/2}/2 <= 1.01 (gamma Phi_k)^{1/2} <= 1/6 for Phi_k <= 1/40.  For |s| <= r_0 use [I, lem:slack(b)].  For |s| >= r_0,
p*(f' + s g) <= 1 + |s| p*(g) and (s(s) - 1)/|s| is increasing, so it suffices that p*(g) <= (s(r_0) - 1)/r_0 = r_0/(s(r_0) + 1),
which is >= r_0/2.02 for r_0 <= 1/5.  Now p*(g) <= theta C'^{1/2} p*(u_k) + |d| p*(psi') <= theta C'^{1/2}(1 + Phi_k/C')
(p* <= q*, p*(L* w') <= ||w'|| = 1), and theta C'^{1/2}(1 + Phi_k/C') <= gamma Phi_k/(4.04 theta C'^{1/2}) is the choice of theta.
Osc is invariant under adding multiples of psi'.  QED
Reading.  At a FIXED row a strict non-peak supports a genuine mate only of size ~ (gamma lambda_k)^{1/2} (the sqrt-weight law of
N3-ref, now with a proved lower bound of the right order; the upper bound is P1's C2/C3), because the scales above its radius
must be paid by the slack alone.  Inside a COMPOSITE mate, whose larger scales are carried by other structure, the same carrier
contributes O(1) (Proposition 1.5): capacity is a count, not a weight (P1).  Everything therefore hinges on the junction.

## 1.4 The junction: the slack-only route is closed; what remains

PROPOSITION 1.7 (certificate recovery in the Problem-R configuration forces square-precision approximants).  PROVED.
Let f, g in C(f), rho in (0, 1), Z = {j, j'} free coordinates of f with psi_j psi_{j'} != 0, kappa := rho Osc_Z(g; psi) > 0,
and assume no strict non-peak and no degenerate peak of f sees Z.  Let f'_n be attaining rows converging to f and c'_n =
(b'_n, omega'_n) finite certificates at f'_n with H(c'_n) <= 1 and eta_n := p*(g_{c'_n} - rho g) -> 0.  Let S_n be the set of
k in supp omega'_n with u_k 1_Z != 0.  Then for n large:
 (i)   S_n is nonempty, consists of strict non-peaks of f'_n, and min S_n -> infinity;
 (ii)  sum_{k in S_n} lambda_k |omega'_n(k)| >= kappa/2, hence r(c'_n) <= (sum_{k in S_n} lambda_k)/kappa -> 0;
 (iii) if the recovery is certified by the scale criterion [I, prop:scale] with c'_n, then
       p*(f'_n - f) <= (1 - rho^2) r_*^2/6 <= (1 - rho^2)(sum_{k in S_n} lambda_k)^2/(6 kappa^2)  and
       eta_n <= (1 - rho^2)(sum_{k in S_n} lambda_k)/(6 kappa).
Proof.  z'_n -> z coordinatewise ([I, prop:approximants]) and |z_i| < 1 on Z, so Z is disjoint from supp a'_n for large n and
b'_n vanishes on Z.  On Z, g_{c'_n} = sum_{k in S_n} lambda_k omega'_n(k) u_k - d'_n psi'_n, so (taking the constant -d'_n)
Osc_Z(g_{c'_n}; psi'_n) <= sum_{S_n} lambda_k |omega'_n(k)| ||u_k 1_Z||_1 <= sum_{S_n} lambda_k |omega'_n(k)|.  By N3 Lemma 2.0(a),(b),
psi'_n -> psi in l_1 ([I, prop:continuity]) and ||.||_1 <= 3 p*(.), Osc_Z(g_{c'_n}; psi'_n) >= Osc_Z(rho g; psi) - o(1) - 3 eta_n
>= kappa/2 for n large.  This gives (ii)'s first claim and S_n nonempty; supp omega' lies in the strict non-peaks by (C2).
If a fixed k were in S_n for infinitely many n, then |u_k(x'_n)| < vartheta'_n Phi_k with x'_n -> xi weak* and vartheta'_n ->
vartheta ([I, prop:continuity]) would give |u_k(xi)| <= vartheta Phi_k: k would be a strict non-peak or a degenerate peak of f
seeing Z, excluded.  So min S_n -> infinity.  The radius: r(c'_n) <= gamma'_k/(2|omega'_n(k)|) <= 1/(2|omega'_n(k)|) for each k in
S_n, so lambda_k |omega'_n(k)| <= lambda_k/(2 r) and kappa/2 <= sum_{S_n} lambda_k/(2r).  (iii) is [I, prop:scale] with r_* <= r.  QED
REMARK 1.8 (why the slack-only junction cannot work; HEURISTIC).  A carrier in S_n is, at f, a peak (Problem R).  Turning it
into a strict non-peak of gap gamma' lowers its block coefficient by at least gamma' - |M - M'_n|; absent cancellation against
other parts of f'_n - f this moves the row by >~ lambda_k gamma' (the conversion cost), whereas (iii) with r <=
gamma' lambda_k/(2 lambda_k |omega'(k)|) demands p*(f'_n - f) <~ (1 - rho^2)(gamma' lambda_k)^2/(24 (lambda_k|omega'(k)|)^2).  With
|S_n| carriers sharing the oscillation equally the requirement becomes |S_n| >~ kappa^2/(gamma' lambda), i.e. total converted
weight >~ kappa^2/gamma', impossible for carriers whose depth tends to infinity.  So the scales between the certificate
radius (~ lambda_{k_0}) and the slack scale (~ (lambda_{k_0} gamma')^{1/2}) must be certified by the KEPT weak-peak staircase of
f'_n itself, i.e. by a non-certified mechanism (no finite certificate can use peaks).
JUNCTION PROBLEM (the remaining core of Problem R, positive side).  OPEN.  Show that for (f, g, rho) in the Problem-R
configuration there are attaining rows f^L -> f (keeping the peaks of f up to depth L with margins perturbed by a relative o(1),
and converting or tuning near-threshold carriers at depth ~ L by Corollary 1.4 / the conversion lemma) and mates g^L ->
rho g of f^L, where the decompositions of f^L +- t g^L are: for t <~ lambda_{k_0}, the certificate of Proposition 1.5 (two-sided
converted carriers); for t >~ lambda_{k_0}, the scale-t decompositions of f transported to f^L, with the first-order terms
rebalanced exactly (as in [I, thm:transport]: b_n = b'_n - tau_n a_n) and the deep part (depth > L) of f's decompositions
replaced by the converted carriers.  Bookkeeping (HEURISTIC): the deep part of f's scale-t decomposition has l_1 size
<= 5 sum_{k > L} lambda_k/t (Lemma W), the first-order mismatch of the transported decomposition is O(t lambda_{k_0}) when the
block increments have bounded D-norm, and the converted carriers cover t <= gamma' lambda_{k_0}/(2c); so the two regimes overlap
up to a CONSTANT FACTOR at t ~ lambda_{k_0} -- the "capacity comparison at a single junction depth" of P1, which P1's
SOCP models resolve in favour of the approximant (P1 Section 5.3).  A proof must (1) control the D-norm of f's block
increments at scale t uniformly, (2) make the first-order rebalancing t-independent (the mate is one vector), and (3) compare
the junction constants.  None of (1)-(3) is done here.
What an adversarial T would have to do (HEURISTIC).  Defeat both mechanisms simultaneously: make every near-threshold carrier
that is a near-duplicate of the free profile at precision O(lambda) (P1 Lemma P) unusable at the junction -- e.g. no carrier of
f seeing Z can be converted without moving shallower margins by more than they are (the conversion lemma moves margins by
|u_l(j) delta|), and no tuned carrier (Corollary 1.4) is a near-duplicate of the profile at precision O(lambda) (a rate
condition on T: Diophantine-type badly approximable profiles; the set of well-approximable directions is a dense G_delta, so
this is a meagre-type condition on (f, g)).  Corollary 1.4 shows tuning itself can never be prevented; only the PRECISION of
available shapes relative to their weights can be.

## 1.5 Summary of part 1 (item (1) of the task)
 * PROVED: oriented profile identity (1.1) and the two-signed requirement (Cor. 1.2): each oriented class of small-margin
   peaks must separately violate the log^2 rate (refines R-W); strict non-peaks serve both classes.
 * PROVED: nested tuning (Prop. 1.3, Cor. 1.4) -- for EVERY admissible T and EVERY f there are attaining rows arbitrarily
   close to f with infinitely many deep carriers of prescribed profile on Z, sign class and EXACT prescribed margins (or zero
   pairing); this answers the existence question left open in N3 Section 1.6 and realizes the "nested tuning" mechanism at
   the level of rows, with no rate hypothesis on T.  Conversion lemma (Remark (c)): PROVED (IVT).
 * PROVED: one strict non-peak is a certificate of size O(1) and radius ~ gamma lambda/(2 theta C^{1/2}) (Prop. 1.5); as a
   stand-alone mate it has size >= 0.49 (gamma lambda)^{1/2} (Cor. 1.6: the sqrt-weight law, lower bound).
 * PROVED: certificate recovery in the Problem-R configuration forces converted carriers of depth -> infinity, radius ->
   0 and square-precision approximants (Prop. 1.7); HEURISTIC: the slack-only junction is therefore impossible and the kept
   staircase must certify the intermediate scales.
 * OPEN: the junction problem (transport of the weak-peak staircase to f^L with exact first-order rebalancing, and the
   constant comparison at the junction).  Not resolved; P1's models favour the approximant.  Hence "rho g in Rec(f)" for the
   Problem-R configuration is NOT proved here.

---

# P2 part 3: finite merging (P-II of N1-ref) -- equivalent forms, the fan structure, a placement criterion

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Notation of N1 / N1-ref: S* := S_{p*}; NA_1 := attaining rows in S*;
C(f) the mate fibre; Rec(f) the outer limit of C along attaining rows (N1 Def. 1.1); A(f) the family of Hausdorff limits of
C(f_n) along attaining sequences f_n -> f; U(f) the inner limit of C along ALL sequences; Omega the dense G_delta set of
Hausdorff-continuity points of C ([I, rem:joint]).  Facts used (N1 Prop. 1.2, N1-ref Lemma R-M): Rec(f) is norm compact and
balanced, Rec(f) = union of A(f), every A in A(f) is compact convex symmetric with U(f) contained in A contained in C(f);
C is upper semicontinuous ([I, thm:compact]).  FINITE MERGING at f: for all g_1, ..., g_k in Rec(f) and eps > 0 there is
f' in NA_1 with p*(f' - f) < eps and max_i dist(g_i, C(f')) < eps; Lemma R-M: this holds iff Rec(f) belongs to A(f).

## 3.1 Equivalent forms

PROPOSITION 3.1.  PROVED.  For f in S* the following are equivalent:
 (a) finite merging at f (equivalently Rec(f) in A(f));
 (b) A(f) is upward directed: any two members are contained in a third member;
 (c) (transitivity of merging) there are rows f_n -> f in S* (attaining or not), each satisfying finite merging at f_n,
     with Rec(f) contained in the Kuratowski lower limit of Rec(f_n);
 (d) (primal form) there is an attaining sequence f_n -> f with liminf_n r~_{f_n}(x) >= h_f(x) for every x in a dense subset
     of X, where h_f(x) := max over Rec(f) of x = limsup over attaining f' -> f of r~_{f'}(x) (N1 Thm 1.9(a));
 (e) for every eps > 0 and x_1, ..., x_m in X there is f' in NA_1 with p*(f' - f) < eps and r~_{f'}(x_i) >= h_f(x_i) - eps
     for all i.
Proof.  (a) => (b): Rec(f) is in A(f) and contains every member.  (b) => (a): for g_1, ..., g_k in Rec(f) pick A_i in A(f)
containing g_i, and by (b) (iterated) A in A(f) containing all A_i; A is the Hausdorff limit of C(f_n) for an attaining
f_n -> f, so dist(g_i, C(f_n)) <= d_H(C(f_n), A) -> 0.  (a) => (c): take attaining f_n with C(f_n) -> Rec(f) in the
Hausdorff metric; at an attaining row the constant sequence shows Rec(f_n) = C(f_n) in A(f_n), and Rec(f) = lim_H C(f_n) is
contained in Li C(f_n).  (c) => (a): given g_i in Rec(f) and eps, choose n with p*(f_n - f) < eps/2 and h_i in Rec(f_n) with
p*(h_i - g_i) < eps/2; merging at f_n gives f' in NA_1 with p*(f' - f_n) < eps/2 and dist(h_i, C(f')) < eps/2.
(a) => (d): along f_n with C(f_n) -> Rec(f) (Hausdorff), r~_{f_n}(x) = max over C(f_n) of x -> max over Rec(f) of x = h_f(x).
(d) => (a): the argument of [I, thm:lowerlimit] ((ii) => (i)) with the compact convex set K := closed convex hull of
Rec(f) in place of rho C(f): if some g in K had dist(g, C(f_{n_j})) >= delta, a Blaschke limit A of C(f_{n_j}) would be
compact convex with dist(g, A) >= delta and support function h_A(x) = lim r~_{f_{n_j}}(x) >= h_f(x) = h_K(x) on a dense set,
hence everywhere (support functions of subsets of B_{p*} are p-Lipschitz), so K is contained in A (separation by c_0):
contradiction.  Thus K is contained in Li C(f_n), which is contained in Rec(f) (limits of mates along attaining rows); so
Rec(f) = K is convex, and every Hausdorff cluster set A of (C(f_n)) satisfies Rec(f) in A in Rec(f): Rec(f) in A(f).
(d) <=> (e): (e) for a dense sequence (x_i) and eps = 1/n gives (d) by a diagonal choice; (d) gives (e) by taking n large
(liminf for finitely many x_i, and p-Lipschitz dependence on x).  QED
Reading.  Merging is a SIMULTANEOUS-LIMSUP property of the scalar functions f' -> r~_{f'}(x) on attaining rows: each limsup
h_f(x) is attained along some attaining sequence (N1 Thm 1.9(a)); merging asks for one sequence serving all x.

## 3.2 The fan structure and where merging is automatic

PROPOSITION 3.2 (U-fan).  PROVED.  Put U_NA(f) := intersection of all members of A(f) (the mates recovered along EVERY
attaining sequence; it contains U(f)).  Then U_NA(f) is compact, convex and symmetric, and for every g in Rec(f) the convex
hull of U_NA(f) and g is contained in Rec(f).  So Rec(f) is a union of compact convex symmetric sets glued along the common
compact convex set U_NA(f) (a "fan"), and it is star-shaped with respect to every point of U_NA(f).  Consequently every
finite set K contained in U_NA(f) union A (for one A in A(f)) merges, and a failure of merging needs two mates outside
U_NA(f) that lie in no common member of A(f).
Proof.  An intersection of compact convex symmetric sets is such; U(f) lies in every member (N1 Prop. 1.2(b)).  If g is in
Rec(f), g lies in some A in A(f) (N1 Prop. 1.2(b)), A contains U_NA(f) and is convex.  The last claims follow from
Proposition 3.1(b).  QED

PROPOSITION 3.3 (automatic merging).  PROVED.  Finite merging holds at f in each of the following cases:
 (a) f attains its norm (Rec(f) = C(f) is in A(f) via the constant sequence);
 (b) f is in Omega (then C(f) is contained in U(f), so U(f) = A = Rec(f) = C(f) for every A in A(f));
 (c) Rec(f) \ U_NA(f) is contained in a single member A of A(f) (then Rec(f) = A);
 (d) C(f) equals the closure of the shifted certified fibre cl Cert^sh(f) (then cl Cert^sh(f) contained in U(f) contained in
     Rec(f) contained in C(f) gives equality throughout, and (b) applies).
Proof.  (a) N1 Prop. 1.2(b) with f_n = f.  (b) Lower semicontinuity of C at f along every sequence means C(f) is in U(f);
then U(f), A, Rec(f), C(f) coincide.  (c) Rec(f) = U_NA(f) union (Rec(f) \ U_NA(f)) is contained in A, and A is contained in
Rec(f).  (d) [I, prop:intrinsic(c)] / N1 Prop. 1.2(b).  QED

PROPOSITION 3.4 (merging versus (P-I)).  PROVED except (iv), which is an abstract remark.  Suppose (P-I) at f, i.e. the
closed convex hull of Rec(f) is C(f) (no type (I) obstruction at f).  Then:
 (i)  every extreme point of C(f) lies in Rec(f);
 (ii) Rec(f) = C(f) iff Rec(f) is convex;
 (iii) finite merging at f implies Rec(f) = C(f);
 (iv) (abstract) a compact convex symmetric set can be the union of proper compact convex symmetric subsets with a common
      core (the unit disk is the union of its diameters), so convexity of Rec(f) does not by itself force Rec(f) into A(f):
      (P-II) at f is, as a statement about families of convex sets, strictly stronger than "(P-I) and density at f".
      Whether it is strictly stronger for mate fibres: OPEN.
Proof.  (i) Rec(f) is norm compact, and the closed convex hull of a norm-compact set of a Banach space is norm compact
(Mazur); by Milman's converse of the Krein-Milman theorem, ext(cl conv Rec(f)) is contained in Rec(f).  (ii) If Rec(f) is
convex it is closed, so Rec(f) = cl conv Rec(f) = C(f); the converse is trivial (C(f) is convex).  (iii) Lemma R-M: merging
gives convexity; apply (ii).  (iv) Elementary.  QED
So under (P-I) the extreme mates are recovered and density at f is exactly convexity of Rec(f); merging is the stronger
"one sequence for all mates" property, i.e. [I, cor:finite(a)] at f.

## 3.3 A placement criterion

DEFINITION 3.5 (far-local recovery).  A mate g in Rec(f) is FAR-LOCALLY RECOVERED if for every eps > 0 there are W_g in N and
eta_g > 0 such that for every W_1 >= W_g and every theta > 0 there are a finite set R contained in (W_1, infinity) and data
(a'_R, z'_R) on R (|z'_R| <= 1, z'_R = sign a'_R on supp a'_R, ||a'_R||_1 < theta) -- the PATTERN -- with the property:
every attaining row f' whose data (a', z') ([I, prop:smooth(c)]) satisfy
   ||(a' - a) 1_{[1, W_g]}||_1 < eta_g,   |z'_j - z_j| < eta_g for j <= W_g,   (a', z') = (a'_R, z'_R) on R,
   ||(a' - a) 1_{N \ ([1, W_g] u R)}||_1 < eta_g,   z' arbitrary (in the unit ball of c_0) elsewhere,
has dist(g, C(f')) < eps.

THEOREM 3.6 (merging from far-local recoveries).  PROVED.  If the far-locally recovered mates are dense in Rec(f), then
finite merging holds at f.
Proof.  Let g_1, ..., g_k in Rec(f), eps > 0, delta > 0.  Choose far-locally recovered g'_i with p*(g'_i - g_i) < eps/2 and
apply Definition 3.5 to g'_i with eps/2: (W_i, eta_i).  Let (W(delta), eta(delta)) be given by N1 Lemma 1.4 (far freedom,
uniform form) and put eta := min(eta(delta), eta_1, ..., eta_k)/(8 + 8||U||).  Choose W >= max(W(delta), W_1, ..., W_k) so
large that ||a 1_{(W, infinity)}||_1 < eta and |q*(a 1_{[1, W]}) - 1| < eta.  Choose patterns successively: R_1 in (W, infinity)
for g'_1 with mass < eta/k, then R_2 beyond max R_1 for g'_2, ..., R_k beyond max R_{k-1} (the patterns are disjoint); let P
be the sum of the pattern masses, so ||P||_1 < eta and q*(P) <= (1 + ||U||) eta.  Put a' := c a 1_{[1, W]} + P, with c > 0 such
that q*(a') = 1 (intermediate value theorem: the left side is continuous in c, < 1 at c = 0 and -> infinity); the triangle
inequality gives c q*(a 1_{[1,W]}) in [1 - q*(P), 1 + q*(P)], hence |c - 1| <= 3(1 + ||U||) eta for small eta.  Put z' := z on
[1, W], z' := z'_{R_i} on R_i, z' := 0 elsewhere.  Then z' is in the unit ball of c_0 and z' = sign a' on supp a' (on
F cap [1, W] because c > 0, on the patterns by construction); f' := grad p(z' + U(U*a'/||U*a'||)) is attaining
([I, prop:smooth(c)]).  ||a' - a||_1 <= |c - 1| + ||a 1_{(W, inf)}||_1 + ||P||_1 <= (5 + 3||U||) eta < eta(delta), and z' = z on
[1, W(delta)], so p*(f' - f) < delta (N1 Lemma 1.4).  For each i: z' = z on [1, W_i]; ||(a' - a) 1_{[1, W_i]}||_1 <= |c - 1| <
eta_i; the data on R_i are the pattern; ||(a' - a) 1_{N \ ([1, W_i] u R_i)}||_1 <= |c - 1| + ||a 1_{(W, inf)}||_1 + ||P||_1 <
eta_i; z' is arbitrary elsewhere.  Hence dist(g'_i, C(f')) < eps/2 and dist(g_i, C(f')) < eps.  As delta is arbitrary, (beta) of Lemma R-M holds.  QED
Remarks 3.7 (which recoveries are far-local).
 (a) PROVED: every g in U_NA(f) is far-locally recovered with the empty pattern.  (If W_g = n, eta_g = 1/n failed for every
     n, the violating attaining rows would converge to f by [I, prop:approximants] ((ii) implies (i)), while g is recovered
     along every attaining sequence: contradiction.)  So only mates outside U_NA(f) need patterns (Proposition 3.2).
 (b) HEURISTIC: recoveries built from tuned or converted carriers with private far coordinates (Part 1, Corollary 1.4) have
     far patterns, but robustness against ARBITRARY data elsewhere requires the tuned carriers' mass outside [1, W] u R to be
     small compared with their margins or gaps (a precision-versus-weight rate, cf. Part 1, 1.4); without such a rate the
     pattern of g_2 can destroy the tuned margins of g_1.
 (c) HEURISTIC/SKETCH: the KSB recoveries of P1 use a NEAR shift on the oscillation set Z and keep the staircase of f to
     depth L; they are not far-local.  For several mates with the SAME oscillation set Z the KSB construction depends only on
     (f, Z), so one KSB sequence serves all of them (merging, conditional on the junction problem of Part 1).  For mates with
     different oscillation sets Z_1, Z_2 seen by common carriers, a shift on Z_1 moves the margins of the staircase carriers
     of Z_2 by |u_l(j) delta| (Part 1, conversion lemma), which is of the order of the deep margins: interference.
 (d) HEURISTIC: engineered approximants ([I, def:engineered]) bank the oscillation set on contacts and support in [1, N];
     banking the union of the oscillation sets of g_1, g_2 keeps z' unchanged there (contacts keep sign z_j), so merging of
     engineered recoveries reduces to monotonicity of the engineered recovery under additional tiny banks (not checked).

REMARK 3.8 (mixing approximants does not merge; elementary).  If f'_1, f'_2 are attaining with normers x'_1, x'_2, the row
f'_m := grad p(x'_1 + x'_2) has threshold data computed from x'_1 + x'_2: a carrier k is a strict non-peak of f'_m iff
|u_k(x'_1) + u_k(x'_2)| < vartheta'_m Phi_k p(x'_1 + x'_2).  A strict non-peak of f'_1 with u_k(x'_1) = 0 is a peak of f'_m as
soon as |u_k(x'_2)| exceeds that threshold.  So the near-kernel resources that make each f'_i recover g_i are not inherited by
convex combinations of normers; merging has to be achieved by PLACEMENT of patterns (Theorem 3.6), not by mixing.

## 3.4 Summary of part 3 (item (3) of the task)
 * PROVED: equivalent forms of finite merging (directedness of A(f); transitivity along merging rows; simultaneous-limsup
   primal form (d)/(e)); the U_NA-fan structure of Rec(f); automatic merging at attaining rows, at continuity points of C,
   when C(f) = cl Cert^sh(f), and when all non-core mates lie in one cluster set; under (P-I) every extreme mate is
   recovered (Milman), density at f is convexity of Rec(f), and merging implies density at f.
 * PROVED: a placement criterion (Theorem 3.6): density of far-locally recovered mates implies finite merging.
 * HEURISTIC: which known recovery mechanisms are far-local (Remarks 3.7); mixing does not merge (Remark 3.8).
 * OPEN: finite merging (P-II) at every f.  The problem is equivalent to a uniform (one-sequence) recovery of all mates of
   Rec(f) and is not easier than the recovery problems themselves; for Problem-R mates it is tied to the junction problem
   and to the precision-versus-weight question of Part 1.

---

# Section N. Numerics (sanity checks only)

 * P2_work/cm_identity_check.py: the common-mode identity (2.1) on 2000 random finite models (random diagonal base, base
   data, carriers u_l = y_l + v_l with signature tails, random combination coefficients): max |lhs - rhs| = 8.0e-15; the
   deviation identity J1.1: max error 3.9e-14; Proposition 2.6' toy model (aligned free-target pair): min ratio
   V(zhat)/((7/8)||C~||_1/H) = 1.50 over 3000 instances.
 * P2_work/tuning_check.py: finite one-block model (40 coordinates, 30 carriers, weights 2^{-1-k} x U(0.5,1)); three deep
   carriers with private far coordinates tuned by the fixed-point map of Proposition 1.3 to types (peak, margin 3e-7),
   (peak of sign -, margin 5e-7), (strict non-peak with zero pairing).  The iteration converges in 2 steps; tuned pairings
   equal the targets to 1e-17; the norming functional of the block (computed from its KKT form w = clip(zeta/(nu Phi^2),
   -M, M); a generic SOCP solver cannot resolve the deep carriers, whose zeta entries are ~1e-13) gives |w'(k)|/M' = 1 at
   the tuned peaks and w'(k) = 0 at the zero-pairing carrier, and the pairing form of the threshold lemma (peak iff
   |u_k(x')| >= vartheta' Phi_k; |w'(k)| = M' |u_k(x')|/(vartheta' Phi_k) off peaks) has 0 violations over all 30 carriers.
