# V2 notes (Round 7): items (B) multi-block rays (m') and (C) coherent shift resonance (h') of ADDENDUM 6, F finite

Setting: paper/martin_density_note.tex (Sections 1, 7, 8), finite block set I = {1..N}, p = p_N, F = supp a finite; the
designed admissible operator of the SLD family with the sub-window pigeonhole (Y4 D^PW with Y4-ref A.3 and (G), or V1's
unified design D_Omega), augmented below to D^{V2}; DIAGONAL base U (a free choice); far pulls and private banks
(Y4-ref C.2-C.7).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Part files V2_part1..4.md; scripts V2_work/.
No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN.

## 0. Summary
**(B) multi-block rays: SETTLED for the companion route (PROVED, modulo the refereed tools cited and the assembly).**
The obstruction behind (m') is determinantal: d-vectors of extreme rays can be nearly dependent while every component is
robust (two-ray example, 2.1: Hoffman ratio 2/delta).  Three tools remove it:
 (1) Lemma H: the Hoffman constant of any finite linear system is <= (norm)^{n-1}/(least NONZERO minor); exactly vanishing
     minors are harmless.
 (2) Lemma L (Lojasiewicz inequality, semialgebraic form): finitely many tiny polynomial objects can be made EXACTLY zero
     simultaneously by a move of size C_L beta^{2/N_L}, with constants depending only on the polynomials.
 (3) The minors of the exact-cone system at a companion are multi-affine polynomials in the carrier VALUES val_l (the
     d-coefficient of a switching strict non-peak is val_l/A_m, Y4-ref C.7), up to one common factor per d-row (Y1 Cor. T3),
     and two-sided per-carrier exact tuning (Y4-ref Prop. P4) realizes any small change of the values exactly.
Making every minor a rate object of the pigeonhole design and choosing b(w) as a design power of T_lo(w) that absorbs the
Lojasiewicz exponent (design D^{V2}), Theorem B gives at every clean sub-window a companion f^# (cost o(T_lo^2)) at which
every minor of the exact system vanishes or is >= u(w)/2, hence the FULL d-row Hoffman constant (all blocks, all rays,
compensated or not, mixed or one-signed) is <= C_f^l Design(l)^2/u(w) (the factor C_f^l, like all C_f^{l^2} factors, is absorbed by the window recursion).  The threshold drift caused by tuning is controlled
by a BUFFER PEAK (Lemma 2.3: every block has, at every large level, a coarse peak with |alpha| >= 1/(2l)) pushed outward by
two-sided tuning (Lemma QB, from Y1 Lemma T2): no donor is needed.  Consequently V1's hypothesis (VR_w) (and Y1's (Cmp_w),
(NN_w), Y2's K_F^rel, Z4's Lemma R constants) are not needed: Corollary B.1, and Master Theorem III below.
**(C) coherent shift resonance: REDUCED (PROVED) to an exact/near-exact d-constrained resonance; remaining step OPEN.**
 - Theorem C1 (dichotomy): with the shift-extended system Sigma^sh (peak traces, zero-cost rows on the coarse targets, the
   d-identity coupling delta_m = -sum q tau, source rows) and its pinning rate rho^sh made a rate object, every clean
   sub-window either pins the shift with a design x u^{-3} constant, or has rho^sh <= b(w).  The case "c_* > 0 but
   decaying beyond the ladder" (Y2 5.3(c)) disappears (Cor. C1.1).
 - Theorem E^>= (Theorem E with Delta d >= 0 data) and Theorem E^SC (Delta d < 0 blocks with (SC) at the companions): PROVED.
 - Proposition C3 (rigidity of shifted data: Sum_m Delta_m R_m^* w_m must vanish at EVERY free coordinate outside the data
   support), Corollary C3.1 (with (T-d) density every coordinate is hit by targets of infinitely many carriers of every
   block: one exact cancellation identity per free coordinate), Proposition C4 (an oscillating profile of the mate on the
   signature set of a robust class-G peak forces |Delta d| >= oscillation/(lambda M) for ALL approximating data at ALL
   first rows sharing the peak: d-neutral data cannot follow non-pinned shifts), Lemma C5 (the fine tail of shifted data
   can always be completed exactly at a cheap companion, Schauder-Tychonoff): PROVED.
 - Remaining step (OPEN, 4.4): in case (II) at all large levels, shifted data are exact at a companion only if the fine
   contributions on the finitely many COARSE free coordinates are absorbed exactly (Slater-stable coarse resonance:
   Theorem C6, SKETCH) — an approximately-two-piece Corollary D1 for fine-origin, coordinate-localized errors, or a
   structural theorem, is needed.
**Master Theorem III (with V1).**  For D^{V2} (built on V1's D_Omega), F finite: f in Rec as soon as at a clean
sub-window of infinitely many levels rho^sh(kappa(w), f) >= u(w).  The only F-finite residual is (C*): rho^sh tiny at all
large levels (an exact or b-near-exact d-constrained coherent shift resonance), plus (E) infinite F.

## Results and labels
| # | Result | Label | Where |
|---|---|---|---|
| 1 | Lemma H (Hoffman via independent row sets and nonzero minors) | PROVED | 1.1 |
| 2 | Lemma L (simultaneous exactification, Lojasiewicz) | PROVED (cites BCR Cor. 2.6.7) | 1.2 |
| 3 | Lemma QB (threshold buffer at a peak) | PROVED (from Y1 T2, T3) | 1.3 |
| 4 | Two-ray determinantal example; component exactification insufficient | PROVED (+ numerics) | 2.1 |
| 5 | Design D^{V2} (determinantal objects, Lojasiewicz-adjusted b(w)); Lemma 2.1 | PROVED | 2.2 |
| 6 | Lemma 2.3 (buffer peaks with abs(alpha) >= 1/(2l) at every level) | PROVED | 2.3 |
| 7 | Theorem B (exactification of all tiny minors; d-row Hoffman constant <= C_f^l Design^2/u) | PROVED (modulo cited tools; assembly hypotheses (A1),(A2)) | 2.4 |
| 8 | Corollary B.1 ((HF) of Prop. T with design/u; (m), (m'), (NN_w), (Cmp_w) not residuals) | PROVED (given the assembly) | 2.4 |
| 9 | Lemma 3.1, Definition 3.2 (shift-extended system, pinning rate rho^sh) | PROVED | 3.1 |
| 10 | Theorem C1 (dichotomy at clean sub-windows) | PROVED | 3.2 |
| 11 | Corollary C1.1 (combinatorial shift cost is a design constant; no decay beyond the ladder) | PROVED | 3.2 |
| 12 | Theorem E^>=, Theorem E^SC | PROVED | 3.3 |
| 13 | Proposition C3 (rigidity of shifted data), Cor. C3.1 (a),(c) | PROVED | 4.1 |
| 14 | Cor. C3.1(b) reading "non-generic at partial contact" | HEURISTIC | 4.1 |
| 15 | Proposition C4 (oscillating profiles force shifted data) + example | PROVED | 4.2 |
| 16 | Lemma C5 (fine-tail completion) | PROVED | 4.3 |
| 17 | Near-coordinate conversion on good coarse signature sets | SKETCH | 4.3 |
| 18 | Theorem C6 (stable shifted resonance -> recovery) | SKETCH (block-scalar exactification unproved) | 4.4 |
| 19 | Master Theorem III (V1 Master Theorem II + Theorem B + Theorem C1) | PROVED modulo V1 (unrefereed) | 5 |
| 20 | Residual (C*) and item (E) | OPEN | 5 |

## What is used (exactly)
Design: (D0)-(D2), allowedness (a),(b), (P1)-(P3) of def:SLD; bounded gaps G_l of the S_l (Y4-ref (G)); the sub-window
recursion of D^PW / D_Omega; the two additions of Def. 2.2 (determinantal objects; b(w) adjusted to the Lojasiewicz exponent)
and of Def. 3.2 (shift-pinning objects); 1/delta_comb(l), 1/delta_sh(l), Lip(l), C_L(l) in Design(l).  All N-free.
Base: U diagonal.  Refereed tools: Z3 Theorem E, Lemma U, Lemma 3.1, Lemma 3.2, Prop. T; Y4-ref C.2-C.7 (Lemmas P1-P3,
Prop. P4, Cor. P5); Y1 Lemmas T2, T3, 3.1-3.5, Prop. 5.2, Theorem E'; Y2 Lemma T, Lemma 5.1, Prop. 5.2; Z4-ref Lemma 3.2,
Prop. 5.6'; the note's Lemmas lem:threshold, lem:switchbudget, lem:phicalc, lem:peakshift (eq:didentity), lem:suplevel,
Corollary cor:D1, Theorem thm:engineered.  Unrefereed: V1's assembly (Master Theorem II) for Master Theorem III only.
External: Lojasiewicz inequality (Bochnak-Coste-Roy, Real Algebraic Geometry, Cor. 2.6.7); Schauder-Tychonoff fixed point
theorem; Hoffman-type normal cone description of polyhedra (Farkas), Cauchy-Binet.
# V2 part 1 — Tools: Hoffman constants via minors, semialgebraic exactification, threshold buffer

Setting: paper/martin_density_note.tex (Sections 1, 7, 8), finite block set I = {1..N}, p = p_N, F = supp a finite.
Notation of the Round-6 reports: ladder index l = j(k,m); carrier l has vector u_l, d-coefficient
q_l = eps_l Phi_l w_m(k)/(m C_m); value val_l := eps_l u_l(zhat); A_m := |R_m^** zhat|_m (so sigma_m = q_0 A_m).
At a strict non-peak k(l) of block m (Lemma lem:threshold, Z6 2.1, Y4-ref C.7, V1 Lemma ST(d)):
    q_l = val_l / A_m = (q_0/sigma_m) val_l.                                                         (1.0)
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Scripts: ctx/r7/V2_work/.

## 1.1 Lemma H (Hoffman bound through linearly independent row sets and minors).  PROVED.
Let A in R^{p x n}, b in R^p, and P := {x in R^n : Ax <= b} nonempty.  Call J subset {1..p} *independent* if J is
nonempty and the rows A_i (i in J) are linearly independent; A_J denotes the |J| x n submatrix, sigma_min(A_J) > 0 its
smallest singular value.  Then for every x in R^n
    dist_2(x, P) <= ||(Ax - b)_+||_2 * max{ 1/sigma_min(A_J) : J independent }                     (1.1)
(the maximum over the empty family is 0, which happens only if A = 0).  Moreover, for every independent J,
    sigma_min(A_J) >= max_K |det A_{J,K}| / ||A_J||_2^{|J|-1}        (K ranges over |J|-subsets of columns),   (1.2)
and the maximum in (1.2) is positive.  Consequently, with delta(A) := min{ |det A_{J,K}| : |J| = |K| >= 1, det A_{J,K} != 0 },
    dist_2(x, P) <= max(1, ||A||_2)^{n-1} delta(A)^{-1} ||(Ax - b)_+||_2 .                          (1.3)
Equality constraints Ex = e are included by writing them as Ex <= e, -Ex <= -e: an independent set never contains a
row together with its negative, the residual becomes |Ex - e|, and delta is computed for the matrix [A; E].
Proof.  Let x* be the Euclidean projection of x onto the closed convex set P.  Then x - x* lies in the normal cone of P
at x*, which for a polyhedron is cone{A_i^T : A_i x* = b_i} (Farkas' lemma).  By the conic Caratheodory theorem,
x - x* = sum_{i in J} v_i A_i^T with v_i > 0 and J independent (or x = x*, and there is nothing to prove).  Since
A_i x* = b_i for i in J,
    ||x - x*||_2^2 = sum_{i in J} v_i A_i (x - x*) = sum_{i in J} v_i (A_i x - b_i) <= ||v||_2 ||(A_J x - b_J)_+||_2 ,
using v >= 0.  As x - x* = A_J^T v and A_J^T is injective, ||v||_2 <= ||x - x*||_2 / sigma_min(A_J).  Dividing gives (1.1).
For (1.2): if s_1 >= ... >= s_k > 0 (k = |J|) are the singular values of A_J, then by the Cauchy-Binet formula
s_1^2 ... s_k^2 = det(A_J A_J^T) = sum_K det(A_{J,K})^2 >= max_K det(A_{J,K})^2 > 0 (positive since A_J has rank k), so
s_k >= (s_1 ... s_k)/s_1^{k-1} >= max_K |det A_{J,K}| / ||A_J||_2^{k-1}.  (1.3) follows since every positive max in (1.2)
is >= delta(A), ||A_J||_2 <= ||A||_2 and |J| <= n.  QED
Remarks.  (a) Only the NONZERO minors matter: a configuration in which some minors vanish exactly has a bounded
Hoffman constant; trouble comes only from minors that are small but nonzero.  (b) Hoffman constants do not depend on
the right-hand sides (b, e); (1.3) holds for every b with P nonempty.  (c) l_1/l_infty versions follow with factors
sqrt(n), sqrt(p).  Numerics (V2_work/hoffman_minors_check.py): 1500 random tests, max dist/(bound (1.1)) = 1.0000 (the
bound is attained for single active rows), per-J ratio (1/sigma_min)/(bound (1.2)) <= 1.0000.

## 1.2 Lemma L (simultaneous exactification of polynomial objects).  PROVED (Lojasiewicz inequality).
Let pi_1, ..., pi_s be real polynomials in n variables and Q := [-2, 2]^n.  There are C_L >= 1 and an integer N_L >= 1,
depending only on (pi_1, ..., pi_s), such that for every S subset {1..s} and every v in Q with max_{i in S} |pi_i(v)| <= beta,
0 <= beta <= 1, at least one of the following holds:
    (i) beta >= 1/C_L;
    (ii) there is v' in R^n with pi_i(v') = 0 for all i in S and ||v' - v||_2 <= C_L beta^{2/N_L}.
Proof.  Fix S, put F_S := sum_{i in S} pi_i^2 and Z_S := F_S^{-1}(0) subset R^n.  Let g_S(v) := dist_2(v, Z_S) if Z_S is
nonempty and g_S(v) := 1 for all v otherwise.  F_S and g_S are continuous semialgebraic functions on the compact semialgebraic set Q,
and F_S^{-1}(0) cap Q subset g_S^{-1}(0).  By the Lojasiewicz inequality (Bochnak-Coste-Roy, Real Algebraic Geometry,
Cor. 2.6.7) there are an integer N_S >= 1 and C_S > 0 with g_S(v)^{N_S} <= C_S F_S(v) on Q.  If Z_S is empty this
reads 1 <= C_S F_S(v) <= C_S |S| beta^2, i.e. (i) with any C_L >= (C_S |S|)^{1/2}.  Otherwise a nearest point v' of Z_S
satisfies ||v' - v||_2 = g_S(v) <= (C_S |S| beta^2)^{1/N_S}.  Take N_L := max_S N_S and C_L := max_S max((C_S s)^{1/2},
(C_S s)^{1/N_S}, 1) (for beta <= 1, beta^{2/N_S} <= beta^{2/N_L}).  QED
Remarks.  (a) C_L, N_L are well-defined numbers once the polynomials are fixed (e.g. take for each S the least
admissible N_S and then C_S := 1 + the infimum of admissible constants).  When the polynomials are design data of level
l (below), C_L(l), N_L(l) are design constants computable in principle at stage l of the recursion; only their
existence is used.  (b) Lemma L is the only place where a non-explicit exponent enters; the design absorbs it by
choosing b(w) as a power of T_lo(w) that depends on N_L(l) (Part 2).  (c) The exponent cannot be 1 in general: the
nearest common zero of tiny polynomials can be at distance (tiny)^{1/2} (e.g. v_1^2 + v_2 tiny with v_2 >= 0 forced).

## 1.3 Lemma QB (threshold buffer through a peak).  PROVED (from Y1 Lemma T2(b), Corollary T3; refereed).
One block; zeta in l_1 \ {0}, theta := theta(zeta) (Lemma T: root of Psi), A := |zeta|, phi := ||Phi||_2^2,
nu_k := |zeta(k)|/Phi_k^2 (k is a peak iff nu_k >= theta).  Let c be a peak, s > 0, and zeta' with
sgn zeta'(c) = sgn zeta(c), |zeta'(c)| = |zeta(c)| + s, and E := sum_{k != c} |zeta'(k) - zeta(k)| <= A s/(8(A + theta + 1)).
Let L be any set of coordinates (in applications: the coarse carriers of the block) and put
R(s) := min{1, A s/(8 phi (A + theta + 1))} and X := sup_{k in L, k != c} |zeta'(k) - zeta(k)|/Phi_k^2.  Then
 (a) theta(zeta') >= theta + R(s);
 (b) every k in L \ {c} with nu_k < theta + R(s) - X (in particular every strict non-peak in L, if R(s) > X) is a strict
     non-peak of zeta';
 (c) if C_1(s + E) < h_0 (C_1, h_0 as in Y1 Lemma T2: C_1 = (1 + 2(theta+1)/A)/Phi_{k_0}^2, h_0 = min(1, nu_{k_0} - theta) for
     a fixed non-degenerate peak k_0 != c), then theta(zeta') <= theta + C_1(s + E), and every k in L \ {c} with
     nu_k > theta + C_1(s + E) + X is a peak of zeta' with the sign of zeta(k).
(Coordinates outside L, e.g. fine carriers, may change status; only E, a weighted l_1 quantity, involves them.)
Proof.  (a) is Y1 Lemma T2(b).  (b) nu'_k <= nu_k + X < theta + R(s) <= theta(zeta').  (c) the upper bound is the second
statement of T2(b); then nu'_k >= nu_k - X > theta(zeta'), and sgn zeta'(k) = sgn zeta(k) because
|zeta'(k) - zeta(k)| <= X Phi_k^2 < nu_k Phi_k^2 = |zeta(k)|.  QED
Use.  A buffer peak c is pushed OUTWARD (|value| raised) by a tiny controlled amount; all other moves of the block (the
tuning of Part 2) are the perturbation E, X.  Choosing s with R(s) > X protects every strict non-peak (including the
near-threshold "NT" carriers of Y4-ref C.7 / V1 (K4)), and (c) protects every peak whose margin exceeds C_1(s+E) + X.
Remarks.  (a) Y2/Y1/V1 realize the push by a donor (z-move at an unused signature set); with a diagonal base the push
can be realized at ANY coarse peak whose carrier has infinitely many far contacts or far free coordinates, by banks /
pulls / z-moves (Y4-ref C.6 Prop. P4 / V1 Lemma TU and their proofs; Theorem B, Step 4), in either direction.  (b) Every block has, at
every level l >= l_f, a coarse non-degenerate peak c with |alpha_m(c)| >= 1/(2l) (Part 2, Lemma 2.3), so a buffer
peak with design-controlled constants always exists.
# V2 part 2 — Item (B): multi-block rays.  The d-row Hoffman constant is a design constant at every clean sub-window

## 2.0 What is used
- Design: D^PW of Y4 (Def. 1.4 with Y4-ref A.3 and addendum (G): bounded gaps G_l of the S_l), or V1's unified design;
  only: (D0)-(D2) of def:SLD, allowedness (a),(b), (P1)-(P3), the sub-window recursion (u(w) = b(w^-), disjoint bands
  (b(w), u(w)), Q(w) >= (4 Design(l)/u(w))^{omega(l)+3}), the pigeonhole Theorem 1.6 of Y4 (clean sub-windows), all N-free.
- Base: U diagonal (U^* e_i^* = s_i k_i, (k_i) orthonormal, s_i > 0), a free choice (Y4-ref C.8(iv)).
- Companion tools: far pulls and private banks with exact two-sided per-carrier tuning (Y4-ref C.2-C.6, Prop. P4), Lemma U /
  Theorem E with banked and pulled supports (Y4-ref C.3 Lemma P2, C.4 Lemma P3), Z3 Lemma 3.1 (companion cost), Z3 Prop. T
  (transplant; its hypothesis (HF) is the object of this part), Y1 Lemma T2 / Cor. T3 (quantitative raise), Lemma H, Lemma L,
  Lemma QB (part 1).
- The exact cone at a companion f^#.  As in Prop. T (HF), Y1 Prop. 5.2 and V1's assembly, the transplant projects the
  actual switching amplitudes tau (decompositions of g at f) onto the polyhedron Z^# of the system Sigma^# in the variables
  tau in R^G (G = coarse carriers, level <= l, swallowed at f^#):
    (Z1) tau_l >= 0;  (Z2) z^#_j L_j(tau) >= 0 (j in T(l) cap K^#);  (Z3) L_j(tau) = 0 (j in T(l) \ (F^# u K^#));
    (Z4) tau_l = 0 if k(l) is a peak of f^#;  (Z5) sum_{l in G, m(l) = m, k(l) in Q^#} q^#_l tau_l = 0 (m in I);
    (box) tau_l <= 6 lambda_l/t,
  L_j(tau) := sum_l eps_l tau_l u_l(j).  (Further rows of the same kind used by an assembly, e.g. the generalized
  configuration rows of Y1, change nothing below as long as their coefficients are design data for each pattern.)
  By (1.0), q^#_l = val^#_l/A^#_m in (Z5).  A PATTERN kappa of level l is the finite combinatorial datum fixing Sigma^#
  except the values: the set G, the signs eps_l, the contact pattern and signs z^#_j on T(l), the statuses (peak /
  strict non-peak) of the carriers of G at f^#, the block assignment.  Put L_0(kappa) := {l in G : k(l) strict non-peak}.

## 2.1 Why the linear (component) exactification is not enough
For one block, (Z5) is one row and Y4 Lemma 1.8 bounds its Hoffman part by 1/D_min (D_min = least nonzero ray d-sum);
Y4-ref Cor. P5 / V1 make every tiny ray d-sum (and every tiny COMPONENT D_{r,m} of a multi-block ray d-vector) exactly zero
by LINEAR tuning.  With several blocks the d-vectors D(r) = (D_{r,m})_m in R^N of extreme rays r may be nearly linearly
dependent while all components are robust.  Example (two blocks, two rays): D(r_1) = (1, 1), D(r_2) = (-1, -1 + delta).
For mu = (1,1) (tau = r_1 + r_2) the d-vector is (0, delta), while C cap ker D = {0} for delta != 0: dist_1(tau, Z)/|D tau| >=
2/delta (V2_work/hoffman_minors_check.py: ratio 2/delta for delta = 1e-1..1e-4, bounded (<= 1/2) at delta = 0).  The
obstruction is the 2x2 minor det = delta, a QUADRATIC polynomial in the values: making it zero is not a linear problem.
This is the "determinantal" form of (m') (Y4 1.5 Limitation, Y4-ref C.7/E, V1's (VR_w)).

## 2.2 Determinantal rate objects and the design D^{V2}
**Definition 2.1 (determinantal objects).**  For a pattern kappa of level l let A_kappa(v) (v in R^{L_0(kappa)}) be the
matrix of Sigma^# with the row (Z5) of block m replaced by (v_l 1[l in L_0(kappa), m(l) = m])_{l in G} (i.e. A^#_m := 1).
Its entries are 0, +-1, design data (eps_l z_j u_l(j), j in T(l)) or coordinates of v; each v_l occurs in exactly one
entry.  For row and column index sets J, K with |J| = |K| >= 1, J containing at least one (Z5)-row and never a row
together with its negative, put pi_{kappa,J,K}(v) := det A_kappa(v)_{J,K}, a multi-affine polynomial with design
coefficients.  The OBJECT O = (kappa, J, K) has the rate rho_O(f) := |pi_{kappa,J,K}((val_l(f))_{l in L_0(kappa)})|.
Minors with J free of (Z5)-rows are design numbers; delta_comb(l) := the least nonzero one over all patterns of level
<= l (a design constant).
The number of objects of level <= l is at most sum_kappa 4^{(rows + columns)(kappa)}: design-computable and N-free (patterns
over all subsets of [1,l], all blocks).  For each level l let C_L(l), N_L(l) be the constants of Lemma L for the finite
family {pi_O : O of level <= l} (variables: all v_l, l <= l), Lip(l) a common Lipschitz constant of these polynomials on
[-2,2]^l, and C_*(l) >= 1 a design constant bounding the motion of the values during the assembly (below).
**Definition 2.2 (design D^{V2}).**  D^PW (or V1's design) with: (i) the objects of Def. 2.1 added to the rate scheme
(omega(l) enlarged accordingly); (ii) Design(l) multiplied by Lip(l) (2 + 1/delta_comb(l)) (rows(l) cols(l))^{l} C_*(l);
(iii) with eta(w) := T_lo(w)^4/(l Design(l)) (Design(l) also contains C_L(l)):
       b(w) := min{ eta(w), (eta(w)/C_L(l))^{N_L(l)/2} } / (1 + Lip(l) C_*(l));
everything else as in D^PW (u(w) := b(w^-), Q(w), n(w), T_hi, T_lo, c_{l+1} := min{c_l/4, T_lo(l,M(l))^3, b(l,M(l))^2}).
**Lemma 2.1.**  PROVED.  D^{V2} is admissible and N-free; the bands (b(w), u(w)) are nonempty and pairwise disjoint; every
statement proved for D^PW (Y4 Lemma 1.5(c), Thm 1.6, Cor 1.7 with Y4-ref A.3) and for V1's assembly holds verbatim, since only
b(w) decreased and Design(l), omega(l) increased by design quantities; moreover, with beta(w) := (1 + Lip(l) C_*(l)) b(w),
     beta(w) <= eta(w) < 1/C_L(l)   and   C_L(l) beta(w)^{2/N_L(l)} <= eta(w),                                  (2.1)
and every design multiple Design(l)^k T_lo(w) (k <= 4) is <= u(w)/8 for l >= l_0 (design).
Proof.  All added quantities are determined by the level-l design data (u_{l'} for l' <= l, the patterns), which are fixed
at stage l of the recursion before the sub-windows of level l are defined (y_l is chosen by allowedness with c_l, fixed at
stage l-1).  b(w) <= T_lo(w)^4 <= 2^{-4n(w)} < u(w) as in Y4 Lemma 1.5(b); smaller b keeps every inequality of the form
"b <= T_lo^4/(l Design)" used before.  (2.1): beta <= min{eta, (eta/C_L)^{N_L/2}}, so C_L beta^{2/N_L} <= eta, and
eta < 1/C_L because C_L(l) <= Design(l) and T_lo <= 2^{-l^3}.  Last claim: n(w) >= l 2^{l^3} Q(w) >= Design(l) (4/u(w)), so
T_lo(w) <= 2^{-4 Design(l)/u(w)} and Design^k 2^{-4 Design/u} <= u/8 once Design(l) >= 8k.  QED

## 2.3 Buffer peaks exist at every level
**Lemma 2.3.**  PROVED.  There is l_f such that for every level l >= l_f and every block m there is a coarse peak c = c_m
(level <= l) with |alpha_m(c)| >= 1/(2l); its relative margin rho_c - 1 = nu_c/theta_m - 1 is >= sigma_m/(2 l m q_0 theta_m) and
its absolute margin is mu_c >= sigma_m/(2 l lambda_c).
Proof.  sum_{k in P_m} |alpha_m(k)| = 1 (Lemma lem:threshold) and |alpha_m(k)| = lambda_k mu_k/sigma_m (eq:margin) with
mu_k <= q_0 |u_k(zhat)| <= q_0; hence the peaks of level > l contribute at most q_0 sum_{l' > l} lambda_{l'}/sigma_m <=
q_0 T_lo(l)^3/sigma_m <= 1/2 for l >= l_f, and block m has at most l coarse peaks.  The margins follow from eq:margin.  QED
(For l >= l_f these margins exceed u(w) by any design factor, since u(w) <= 2^{-l^3}: the buffer peak is ROBUST.)

## 2.4 Theorem B (multi-block exactification)
**Theorem B.**  PROVED (modulo the cited tools: Y4-ref Prop. P4 / V1 Lemma TU, Z3 Lemma 3.1, Y1 Lemma T2).  Design D^{V2},
diagonal U, F finite.  Let w = (l,i) be a clean sub-window for f (Y4 Thm 1.6 with the objects of Def. 2.1), l >= l_f.  Let
an assembly (V1 3.2; Y1 4.1; Y4-ref C.6-C.7) be given in the following form: first its z-moves on coarse supports (closing
class-G rooms on the S^nat sets, closing tiny target rooms on T(l)), producing a row f_1; then finitely many further moves
M_ass at coordinates beyond s_max(l) of carriers NOT in L_0(kappa) (donor raises: z-moves or banks; pulls converting
tiny-margin peaks), and the pattern kappa it produces.  Assume
 (A1) |val_{l'}(f_1) - val_{l'}(f)| <= C_*(l) b(w) for l' in L_0(kappa) (true for the z-move closings: (C1) moves a class-G
      value by its tiny room, (C2) by <= |T(l)| b; V1 Lemma ST(a)), and p*(f_1 - f) <= C_f Design(l) b(w) log(e/b(w));
 (A2) after M_ass every coarse carrier of G has the status prescribed by kappa, with relative margin >= u(w)/2 at peaks of
      kappa and either a gap >= c_f Lambda (V1 Lemma ST, donor raise Lambda = T_lo^3) or a relative position rho <= 1 - u/2 at
      strict non-peaks of kappa (or, if no donor raise is used in a block, all its coarse strict non-peaks of kappa have
      rho <= 1 - u/2 or rho <= C_* b and all its peaks of kappa have relative margin >= u/2 at f_1).
Then there is a companion f^# (the moves M_ass, the tuning of L_0(kappa) and, where needed, one outward push of the buffer
peak c_m per block, realized by ONE application of Lemma TU / Prop. P4) with:
 (a) the pattern of f^# is kappa (same G, signs, contacts on T(l), statuses); supp a^# finite;
 (b) val_l(f^#) = val_l(f_1) + x_l EXACTLY for l in L_0(kappa), with |x|_2 <= eta := T_lo(w)^4/(l Design(l)), and
     pi_O(val(f^#)) = 0 for every object O of kappa that is tiny at f (rho_O(f) <= b(w)), while |pi_O(val(f^#))| >= u(w)/2
     for every object that is robust at f;
 (c) p*(f^# - f) <= p*(f_1 - f) + C_f(cost of M_ass) + C_f Design(l)^2 eta log(e/eta) = o(T_lo(w)^2) (for V1's assembly
     C_f Design T_lo^3 log(1/T_lo));
 (d) the Hoffman constant of Sigma^# at f^# (all rows (Z1)-(Z5), box rows; l_1 residuals and distances) satisfies
        C_H^# <= C_f^l Design(l)^2 / u(w),
     for EVERY configuration of the zero-cost cone (single- or multi-block rays, compensated, mixed or one-signed blocks,
     any face structure).
Proof.  Step 1 (objects at f_1).  For every object O of kappa, |pi_O(val(f_1)) - pi_O(val(f))| <= Lip(l) C_*(l) b(w)
by (A1).  Hence tiny objects satisfy |pi_O(val(f_1))| <= beta = beta(w) of (2.1), robust ones >= u(w) - beta >= 3u(w)/4
(Lemma 2.1, last claim).
Step 2 (Lojasiewicz).  Apply Lemma L to the family of level l with S := the tiny objects of kappa and v := val(f_1)
(in [-2,2]^l since |u_l(zhat)| <= q*(u_l) = 1).  Alternative (i) of Lemma L is excluded because beta < 1/C_L(l) (2.1).
So there is v' with pi_O(v') = 0 (O tiny) and |v' - v|_2 <= C_L(l) beta^{2/N_L(l)} <= eta (2.1).  Put x := v' - v
restricted to L_0(kappa) (the polynomials of kappa involve only these coordinates).  Robust objects: |pi_O(v')| >=
3u/4 - Lip(l) eta >= u/2.
Step 3 (one combined realization).  Apply Lemma TU (V1 3.4; = Y4-ref Prop. P4 with explicit bank solution) at the row
obtained from f_1 by the moves M_ass (their masses and z-changes are part of the base A^p of its proof; their coordinates
are distinct from the pull and bank coordinates of L_0, which lie in the S_{l''}, l'' in L_0, beyond s_max(l)), with the
carrier set L_0(kappa) and the targets val^#_{l''} := v'_{l''}: since Lemma TU solves for EXACT values given all other
masses, the second-order side effects of M_ass on the L_0 values are absorbed, and val^#_{l''} = v'_{l''} = val_{l''}(f_1)
+ x_{l''} exactly.  The required increments are |x| + O(side effects) <= 2 eta <= c_T (c_T = f-constant x Design^{-3} >>
eta = T_lo^4/(l Design), Lemma 2.1).  Other coarse carriers k notin L_0 move by <= C_T eta^2 beyond the effect of M_ass
(Lemma TU(b)); all pulls/banks lie beyond s_max(l), so T(l), the contact pattern on T(l) and all swallowing signs are those
of the assembly; fine carriers: sum_{k > l} lambda_k |Delta u_k| <= 2^{-l} eta + (fine effect of M_ass).  Cost: Lemma TU(d).
Step 4 (statuses).  With V1's assembly, Lemma ST of V1 applies verbatim with the additional value moves |x| + C_T eta^2 <=
2 eta << c_f Lambda = c_f T_lo^3 (V1's raised blocks) and << u(w) (robust carriers): every coarse carrier keeps the status
prescribed by kappa.  In a block without donor raise in which a protection is needed (a self-contained assembly), push the
buffer peak c = c_m of Lemma 2.3 outward inside the same Lemma TU solve (c notin L_0): with zeta := R_m^** zhat_1 and
zeta^# := R_m^** zhat^#, X := max over coarse k != c of |zeta^#(k) - zeta(k)|/Phi_k^2 <= m(2 eta)/Phi_min(l) <= C D(l) eta and
E := sum_{k != c} |zeta^#(k) - zeta(k)| <= phi X + 2^{-l} eta (sum_k m Phi_k |Delta u_k| = sum_k Phi_k^2 (m|Delta u_k|/Phi_k)),
take r_m := C_*(l) b(w) theta_m and the push s := (16(A + theta + 1)/A) max{E, phi(X + r_m)} (a-priori bounds for E, X with
|y| <= C_f Design^2 eta for the push itself; A, theta, phi of block m at f_1).  Then E <= A s/(8(A+theta+1)), so Lemma QB
gives theta^#_m - theta_m >= R(s) >= X + r_m and theta^#_m - theta_m <= C_1(s + E), C_1(s + E) + X <= C_f Design(l)^2 eta <=
u(w) theta_m/4: every coarse strict non-peak of kappa (nu < theta_m, or nu <= theta_m + r_m for a tiny-margin peak declared a
non-peak) stays a strict non-peak (Lemma QB(b)); every coarse peak of kappa (relative margin >= u/2) stays a peak with its
sign (Lemma QB(c)); c stays a robust peak.  So the pattern of f^# is kappa: (a).  The common factors 1/A^#_m of (Z5) change
nothing in (b).
Step 5 (cost).  p*(f^# - f_1) <= C_f(cost of M_ass) + C_T(2 eta) log(e/(2 eta)) + C_f (s/lambda_c) log, and eta, s/lambda_c <=
C_f Design(l)^2 eta, eta = T_lo^4/(l Design): (c) (Lemma 2.1, last claim, for o(T_lo^2)).
Step 6 (Hoffman).  The matrix of Sigma^# at f^# is A_kappa(val(f^#)) with the (Z5)-row of block m multiplied by
1/A^#_m in [1/(2A_max), 2/A_min] (A_m = sigma_m/q_0 moves by C_f Delta: Z3 Lemma 3.1).  Its minors containing (Z5)-rows
equal (prod of the factors 1/A^#_m of the rows used) x pi_O(val(f^#)): by (b) they vanish or have modulus >=
(2A_max)^{-N} u(w)/2; the other minors are design numbers, zero or >= delta_comb(l).  Lemma H (1.3) (with the l_1/l_2
conversion factors sqrt(rows), sqrt(cols) <= (rows cols)(l)) gives C_H^# <= max(1, ||A||_2)^{l-1} (rows cols)(l) /
min(delta_comb(l), (2A_max)^{-N} u(w)/2) <= C_f^l Design(l)^2/u(w) (entries of (Z5)-rows are <= 2/A_min): (d).  QED
**Corollary B.1 (no multi-block residual).**  PROVED (given the assembly).  In Prop. T / Y1 Prop. 5.2 / V1's transplant at
a clean sub-window of D^{V2}, hypothesis (HF) holds with C_H^# <= C_f^l Design(l)^2/u(w), and the d-row violations of the
actual amplitudes at f^# are <= |Delta d|-pinning terms + C eta/t <= (pinning) + C T_lo^3 (since |q^# - q| <= C eta and
sum_l |tau_l| <= 6/t).  Hence the window constant is K <= (room product) x C_f^l Design^2/u x (pinning constants), absorbed
by Q(w); items (m) (f-dependent d-row Hoffman constants: Y2 Theorem M's K_F^rel, Z4 Lemma R, mixed blocks without (DR),
Conjecture G as far as it is used for d-rows) and (m') (multi-block rays) are NOT residuals of the companion route.
What Theorem B does NOT do: the bound on the d-row VIOLATION of tau itself requires the uniform shift Delta d_m to be
pinned at f ((SP_w), Y2 Theorem H) — item (C), Part 3.
Remarks.  (1) No ray enumeration, no (VR_w), no compensators, no one-signedness: Lemma H controls the full system at once.
(2) The exponent 2/N_L(l) of Lemma L is non-explicit; the design absorbs it through (iii) of Def. 2.2, which is legitimate
because b(w) only has to be SOME design quantity (Y4 Cor. 1.7: costs must be o(T_lo^2), bands disjoint).
(3) Status management: in V1's assembly the donor raise Lambda = T_lo^3 (V1 Lemma ST) already dominates the moves
eta <= T_lo^4/(l Design) of Steps 2-3, so Step 4 is needed only in blocks without donors (Y2's aligned corner, item
(D)); Lemma QB + Lemma 2.3 show that the buffer push at a robust coarse peak, available in EVERY block by two-sided
tuning, replaces the donor for the exactification step (and for Y4-ref Cor. P5: its "status part of (BS)" is
discharged the same way).
(4) Tuning a carrier rescales the d-coefficients of its block by the common factor A_m/A^#_m (Y1 Cor. T3, (1.0)): this
multiplies whole (Z5)-rows and never turns a zero minor into a nonzero one (Step 6).
# V2 part 3 — Item (C): coherent shift resonance.  The shift-pinning rate and the dichotomy at clean sub-windows

## 3.0 Setting and what is used
Design D^{V2} (Part 2), F finite, g in C(f), rho < 1; a clean sub-window w = (l,i), l >= l_f; two-sided decompositions of
g at f at the scales t of w; Y1's classes (R: robust room, pinned diagonally; G: tiny room, closed at the companion,
eps_l = closing sign), Y1 Lemmas 3.1-3.3 (pinning of class R: |Delta theta| <= K_g t; one-sided pinning of class G:
(tau_l)_- <= K_g t with tau_l := -eps_l Delta theta_l; e_0 := Delta B 1_{F^c} - sum_G eps tau u 1_{F^c}, ||e_0||_1 <= K_g t + t^7;
peak relations), Y1's shift sources (U1)-(U3), (L1)-(L3) and Lemma 3.4 (shift pinning under (SP_w)), Y2 Lemma 5.1 (peak
trace), eq:didentity, Lemma lem:switchbudget, Z3 Lemma 3.2 (budget at the closed pattern: raises cost at most twice, flips
are bounded by S_fl <= C K t), K_g <= C_f Design(l)/u(w) (Y1).  kappa = the closed pattern of the companion (Part 2),
with tiny-margin peaks declared strict non-peaks; G_pk (G_np) = class-G peaks (strict non-peaks) of kappa; every peak of
kappa has relative margin >= u(w)/2 (Part 2 (A2)), hence absolute margin mu_k >= c_f Phi_k u(w).
Write delta_m := Delta d_m M_m (decomposition convention Delta d = d_+ - d_-), I_sh := blocks lacking an UPPER or a LOWER
source at w (Y1 Def. 3.3; for the other blocks Y1 Lemma 3.4 gives |delta_m| <= K_d t, K_d = C_f D^3/u(w)).

## 3.1 The shift-extended system and its pinning rate
**Lemma 3.1 (relations satisfied by the actual decomposition).**  PROVED.  For every scale t of w, the actual vector
(delta, tau) in R^I x R^G satisfies, with errors measured in l_1 and bounded by C_f Design(l)^2 K_g t/u(w):
 (R1) tau_l >= 0 (l in G_np);
 (R2) tau_l = eps_l vs_l lambda_l delta_{m(l)} (l in G_pk), where vs_l := sgn w_{m(l)}(k(l));
 (R3) on T(l): z^#_j V_j(tau) >= 0 at contacts of kappa, V_j(tau) = 0 at free coordinates of kappa, where
      V(tau) := sum_{l in G} eps_l tau_l u_l 1_{F^c};
 (R4) for every block m: delta_m + sum_{l in G, m(l) = m} q'_l tau_l = 0, with q'_l := q_l = eps_l Phi_l w_m(k(l))/(m C_m)
      (q_l = val_l/A_m at strict non-peaks, q_l = eps_l vs_l Phi_l M_m/(m C_m) at peaks), except q'_l := 0 for nearly
      neutral carriers (relative d-coefficient rho_l <= b(w); they are exactified to q^# = 0 at the companion);
 (R5) delta_m = 0 for m notin I_sh;
 (R6) for m in I_sh having exactly one source half: delta_m <= 0 (an UPPER source of type (U1)) or delta_m >= 0 (a LOWER
      source of type (L1)), class-R sources being not variables of the system;
 (R7) for an anti-type class-G strict non-peak l with |rho_l - 1| <= b(w) (pinned by Y1 Lemma 3.5(b)):
      tau_l + lambda_l (|w(k(l))|/M) delta_m <= 0;
and moreover, for l in G_pk, eps_l vs_l = +1 (swallowing type) or -1 (anti type), and (R1) holds also at peaks:
tau_l >= -K_g t, i.e. eps_l vs_l delta_m >= -C K t (this is how the sources (L2), (U2) enter).
Proof.  (R1): Y1 Lemma 3.2.  (R2): Y2 Lemma 5.1, -Delta theta_l = vs lambda (delta_m + e_k), 0 <= e_k <= t/(lambda_l mu_k), so
|tau_l - eps vs lambda delta_m| <= t/mu_k <= C_f D(l) t/u(w).  (R3): Delta B 1_{F^c} = V(tau) + e_0; by Lemma lem:switchbudget
and Z3 Lemma 3.2 the closed-pattern cost sum_{j notin F} phi_{z^#_j}(Delta B(j)) is <= 2t/q_0 + C K t, so by Lemma lem:phicalc(c)
the cost of V(tau) is <= 2t/q_0 + C K t + 2||e_0||_1; at a contact phi_{z}(x) = 2(zx)_-, at a free coordinate of kappa
phi_{z_j}(x) >= (1 - |z_j|)|x| >= u(w)|x| (robust target room).  (R4): eq:didentity, Delta d_m M_m = (1/(mC_m)) sum_k Phi w Delta theta_k
+ r_m, |r_m| <= 2t/sigma_m, and Phi_l w Delta theta_l/(m C_m) = -q_l tau_l for l in G (proof of Lemma lem:badpeaks(b)); class R
and fine carriers contribute <= (K_g t + 6t^2)/(m C_m) (Phi|w| <= 1); nearly neutral carriers contribute |q_l tau_l| <=
b Phi M 6 lambda/(m C t) <= t^3 (box).  (R5), (R6): Y1 Lemma 3.4 (its halves).  (R7): proof of Y1 Lemma 3.4 (U3):
tau_l <= lambda_l(3 gap/t - Delta d_m |w(k)|) with gap <= b(w) M, so the defect is <= 3 lambda b/t <= t^3.  The last claim:
(R1) at peaks is Y1 Lemma 3.2 for all class-G carriers.  QED
(Any further relation satisfied by the actual decompositions within C_f Design^2 K_g t/u may be added to the system; it can
only increase the rate below.)
**Definition 3.2 (shift-extended system, shift-pinning rate).**  Sigma^sh(kappa, f) is the homogeneous system (R1)-(R7) in
the variables (delta, tau) in R^I x R^G, with (R1) imposed on all of G (peaks included) and the coefficients of (R4), (R7)
taken at f.  viol(delta, tau) := the l_1 norm of its violations (positive parts of the inequalities, moduli of the equalities).  The
SHIFT-PINNING RATE of the pattern kappa at f is
      rho^sh(kappa, f) := inf{ viol(delta, tau) : ||delta||_1 = 1, tau in R^G }   (in [0, infinity)).
It is homogeneous of degree 1 in (delta, tau) and rho^sh(kappa, f) = 0 iff Sigma^sh(kappa, f) has (possibly asymptotic) solutions
with delta != 0: an exact (or asymptotically exact) d-CONSTRAINED COHERENT SHIFT RESONANCE.  The objects (kappa, "sh") are
design-countable (one per pattern of level <= l), so rho^sh is a rate object in the sense of Y4 Def. 1.1; D^{V2} includes them.

## 3.2 Theorem C1 (dichotomy at clean sub-windows)
**Theorem C1.**  PROVED.  Let w be a clean sub-window of D^{V2} for f and kappa the closed pattern.  Then either
 (I) rho^sh(kappa, f) >= u(w): then for every scale t of w and every m,
        |Delta d_m| M_m <= K_sh t,   K_sh := C_f Design(l)^2 K_g/u(w)^2 <= C_f Design(l)^3/u(w)^3,
     so the shift is pinned with a DESIGN x u^{-3} constant, absorbed by Q(w) = (4 Design/u)^{omega+3}; every use of (SP_w)
     or of (H2'') in Y1 Lemma 3.4-3.6, Prop. 5.2, Theorem E', the master theorem 5.4, Y2 Theorems H, M, Y, and in V1's
     assembly holds at w with this constant; or
 (II) rho^sh(kappa, f) <= b(w).
Proof.  The pigeonhole (Y4 Thm 1.6) applied to the enlarged scheme gives the dichotomy rho^sh >= u or <= b.  In case (I),
by Lemma 3.1 viol(delta, tau) <= C_f Design^2 K_g t/u for the actual (delta, tau); by homogeneity
||delta||_1 rho^sh <= viol(delta, tau), so ||delta||_1 <= C_f Design^2 K_g t/u^2.  The uses of (SP_w) in the cited proofs are
exactly the bound |Delta d_m| M_m <= K_d t (Y1 Lemma 3.4; Z4 Step 3; Y2 Theorem H's K_sh); all later constants are linear
in it, and the window arithmetic only needs K T_hi(w) -> 0, n(w)/K -> infinity for K = (design) x u^{-O(1)} x C_f^{l^2},
which Q(w) provides (Y4-ref A.3).  QED
**Corollary C1.1 (relation with Y2 Theorem H; "decay beyond the ladder" is a design artifact).**  PROVED.
 (a) If kappa has a robust combinatorial shift cost, i.e. c^comb_*(kappa) > 0, where c^comb(delta; kappa) := inf_{x >= 0}
     [ sum_{T(l)-contacts} phi_{z_j}(L_j) + sum_{T(l)-free} |L_j| + sum_{l' in G} 2 m^nat_{l'} (sign defect of the S^nat_{l'}
     coefficient)_- ], L := sum_{m in I_sh} delta_m Pi_m + sum_{G_np} x_l eps_l u_l, Pi_m := sum_{l in G_pk, m(l) = m} vs_l
     lambda_l u_l 1_{F^c} (Y2 5.2 read on the closed pattern), and c^comb_* its minimum over the sign-sphere, then
     c^comb_*(kappa) >= delta_sh(l) := min{c^comb_*(kappa') : kappa' of level <= l, c^comb_*(kappa') > 0}, a DESIGN constant
     (c^comb is a polyhedral function with design coefficients for each of the finitely many patterns; put 1/delta_sh(l)
     into Design(l)), and rho^sh(kappa, f) >= delta_sh(l)/(C Design(l)) > b(w), hence case (I) by cleanliness.  So the
     residual of Y2 5.3(c) "c_* > 0 but decaying faster than the ladder" does not occur at clean sub-windows of D^{V2}: only
     exact combinatorial coherent resonance (c^comb_* = 0) together with a tiny rho^sh can block pinning.
 (b) Case (II) refines Y2's coherent shift resonance by the d-identity (R4): the shift is free only along (asymptotically)
     exact solutions of the WHOLE system (R1)-(R5), including the coupling delta_m = -sum q_l tau_l, i.e. the shift must be
     generated by zero-cost switching of class-G strict non-peaks of the right d-sign (q < 0 for delta > 0: configuration
     (i); q > 0 for delta < 0: configuration (ii)), in agreement with the Z4-referee Remark 3.3.
Proof of (a).  For (delta, tau) take x := (tau)_+ on G_np.  On S^nat_{l'} the coefficient of v_{l'} in L is eps x_{l'} >= 0 for
l' in G_np (no cost) and vs lambda delta_m for l' in G_pk, whose cost 2 m^nat (eps vs lambda delta_m)_- is <= 2 m^nat((tau_{l'})_-
+ |tau_{l'} - eps vs lambda delta_m|), i.e. (R1) and (R2) defects.  On T(l): with tau_{l'} = eps vs lambda delta_m + (R2 defect) at
peaks, |L_j - V_j(tau)| <= max|u| (sum of (R2) defects + sum_{G_np} (tau)_-), and phi_{z_j}(V_j) = 2(z_j V_j)_- (contact rows),
|V_j| (free rows) are (R3) defects.  So c^comb(delta; kappa) <= C Design(l) viol(delta, tau), and ||delta||_1 delta_sh(l) <=
c^comb(delta; kappa) gives rho^sh >= delta_sh(l)/(C Design(l)).  Finally delta_sh(l) >= 1/Design(l) and b(w) <= 2^{-4 Design(l)}.  QED

## 3.3 Theorem E with non-negative d-mismatch, and with (SC) at the companions
**Theorem E^>=.**  PROVED.  Theorem E of Z3 (and Theorem E' of Y1/Y2 with window-dependent c_flat; Y4-ref Lemma P2 for banked
and pulled supports) holds with "d-neutral two-piece data" replaced by "two-piece data with Delta d_m := d^{(j)}_m(omega^-_m)
- d^{(j)}_m(omega^+_m) >= 0 for every m" (data convention of Definition def:twopiece).
Proof.  In the proof of Theorem E (Z3 2.2) d-neutrality is used exactly twice: (i) it is preserved under the averaging
Dbar_j = (1/n) sum_i (b^+-_i, omega^+-_i) — so is Delta d_m >= 0, since d^{(j)}_m is linear and the average of nonnegative numbers
is nonnegative; (ii) Corollary cor:D1 is applied at f_j to the averaged data — Corollary cor:D1 assumes exactly Delta d_m >= 0.
Lemma U (both sides separately) does not involve Delta d.  QED
**Theorem E^SC.**  PROVED.  If, in Theorem E^>=, the data have Delta d_m < 0 exactly for m in a set I_- for which every f_j
satisfies the scrambling condition (SC) of Definition def:SC (with its own sequence), then (f, rho g) in cl NA.
Proof.  As in Theorem E, rho gbar_j in C(f_j) with two-piece data of kappa_w <= rho^2(1 + eta_0/2) =: kappa' < 1.  Theorem
thm:engineered at f_j (I finite, F_j finite, (SC) for I_-) with the parameter rho'_j := 1 - 1/j (rho'^2_j kappa' < 1) gives
(f_j, rho'_j rho gbar_j) in cl NA, and (f_j, rho'_j rho gbar_j) -> (f, rho g).  QED
These are the two recovery engines available for data that FOLLOW a non-pinned shift (Part 4).
# V2 part 4 — Item (C), case (II): shifted data.  Rigidity, intrinsic shifts, fine completion, the remaining step

Setting as in Part 3; data convention Delta_m := d_m(omega^-_m) - d_m(omega^+_m) (Definition def:twopiece); for a pair of
two-piece data put Omega := the (finite) set of carriers in the supports of the omega^+-_m, Sigma_Omega := F u
union_{k in Omega} supp u_k, and W_Delta := sum_m Delta_m R_m^* w_m in l_1.

## 4.1 Proposition C3 (rigidity of shifted data).  PROVED.
Let (b^+-, omega^+-) be two-piece data at a first row f with F finite.  Then for every j notin Sigma_Omega:
    W_Delta(j) = 0 if |z_j| < 1,     and   z_j W_Delta(j) <= 0 if |z_j| = 1.
Proof.  Subtracting the two representations, v := b^+ - b^- = sum_m R_m^*(omega^-_m - omega^+_m) - W_Delta.  At j notin
Sigma_Omega the first sum vanishes, and two-piece data have v(j) = 0 off F u K and z_j v(j) >= 0 on K.  QED
**Corollary C3.1.**  PROVED unless marked.
 (a) (Z4-ref Prop. 5.6') On the far part of every signature set S_l (l notin Omega, w_m(k(l)) != 0, Delta_{m(l)} != 0) the own
     term dominates the later targets, so S_l is far-swallowed with eps_l = -sgn(Delta_m) sgn w_m(k(l)).
 (b) For the designs of the note, EVERY coordinate j lies in the target support of infinitely many carriers of EVERY block:
     by density of the targets some y^(i) has q*(y^(i) - e_j^*/q*(e_j^*)) < 1/(2 q*(e_j^*)), hence (q* >= ||.||_1) y^(i)(j) >
     1/(2 q*(e_j^*)) > 0, and every index i is used at
     infinitely many levels of every block (y^(i) is allowed at all large levels and (i_r) repeats i; Theorem thm:SLD).
     Hence, at every free coordinate j outside the finite set Sigma_Omega, (a) does not apply and Proposition C3 is the
     exact cancellation identity
        sum_m Delta_m sum_{k : j in supp y_k} lambda_k w_m(k) y_k(j)/n_k  (+ the own signature term if j in some S_l) = 0,
     an infinite series over carriers of all blocks; the carriers with |u_k(zhat)| >> Phi_k (all but those with tiny values)
     are peaks, w_m(k) = +-M_m.  So shifted data exist only at first rows satisfying one exact identity per free coordinate
     (HEURISTIC reading: non-generic at partial contact; not claimed as a theorem).
 (c) At maximal contact (z = +-1 off F) the identities (b) are void, but there (SP_w) holds at every large level (Y1 Cor. M1
     via Z4 Lemma 5.0) and case (II) of Theorem C1 does not occur.

## 4.2 Proposition C4 (non-constant splits force shifted data).  PROVED.
Let l be a class-G peak of block m of a first row f' (z' = eps_l on S^nat_l \ F'), vs := sgn w'_m(k(l)), and let h carry
two-piece data (b^+-, omega^+-) at f'.  For finite disjoint S_1, S_2 subset S^nat_l \ Sigma_Omega put V_i := sum_{S_i} v_l(s)
and A_i(h) := sum_{s in S_i} eps_l h(s)/V_i.  Then, with tgt := max_{m', +-} |d_{m'}(omega^+-_{m'})| sum_{s in S_1 u S_2}
sum_{l' > l} lambda_{l'} |u_{l'}(s)| (later targets; the double sum is <= (2/9) sum_s 2^{-2s} c_l delta_l by allowedness (b)),
    A_i(h) in [ -d_m(omega^+_m) lambda_l M'_m eps_l vs - tgt/V_i ,  -d_m(omega^-_m) lambda_l M'_m eps_l vs + tgt/V_i ]  (eps_l vs = +1;
    the interval is reversed if eps_l vs = -1),
hence |A_1(h) - A_2(h)| <= |Delta_m| lambda_l M'_m + tgt (1/V_1 + 1/V_2).  Consequently, if g (a mate of f) and functionals g_t
with ||g - g_t||_1 <= K t carry two-piece data at f', then
    |Delta_m(g_t)| >= ( |A_1(g) - A_2(g)| - (K t + tgt)(1/V_1 + 1/V_2) ) / (lambda_l M'_m).
Proof.  At s in S^nat_l \ Sigma_Omega the + representation gives h(s) = b^+(s) - d_m(omega^+_m) lambda_l w'_m(k(l)) v_l(s) + (later
targets at s) (omega^+ vanishes at k(l), a peak, and at carriers not in Omega; other signatures vanish at s; earlier targets
avoid S_l by allowedness (a)); side + gives eps_l b^+(s) >= 0 (z' = eps_l there).  Multiply by eps_l, sum over S_i, divide by
V_i; the - side is symmetric with eps_l b^-(s) <= 0.  The last claim: |A_i(g) - A_i(g_t)| <= Kt/V_i.  QED
Reading.  The DECOMPOSITIONS of g at scale t satisfy the same sandwich with (d_+, d_-) in place of (d(omega^+), d(omega^-)) up
to the budget (B_+- are z-signed up to l_1 mass t/q_0) and the pinned peak terms (|alpha||omega_+-| <= t/(2 sigma) at robust
peaks): the profile eps_l g(s)/v_l(s) on the signature set of a robust class-G peak may OSCILLATE inside an interval of length
|Delta d^dec_m| lambda_l M (the "non-constant split" of the classical switching mates, Round 1-2).  Proposition C4 shows that
such an oscillation is visible to every approximating data set at every first row f' sharing the peak: d-neutral data
(Delta = 0) cannot follow a mate whose profile oscillates by more than (Kt + tgt)(1/V_1 + 1/V_2), at ANY companion.  So in case
(II) of Theorem C1, for mates with persistent oscillating profiles, the exact-data route NEEDS Delta != 0 data, and by
Proposition C3 these need the exact identities of Corollary C3.1(b) at the companion.
Example (PROVED: the data computation).  Let block m be in configuration (i) with EXACT coherence at f: R_m^* w_m 1_{F^c} is
z-signed and vanishes off F u K, and some class-G strict non-peak k_1 of block m with q < 0 is resonant (eps u_{k_1} 1_{F^c}
z-signed, supported in K).  Let c > 0 be small, phi >= 0 supported in S^nat_l (l a swallowing-type robust G-peak of block m)
with phi <= c lambda_l M v_l and phi in l_1, and b_0 supported in F with c q_0 b_0(zhat) = c sigma_m - eps_l q_0 phi(zhat) (possible
since a(zhat) = 1 != 0), so that g(xi) = 0 for
    g := c(b_0 - R_m^* w_m) + eps_l phi
carries the two-piece data (b^+, omega^+) = (c b_0 - kappa lambda_{k_1} u_{k_1} + eps_l phi, kappa e_{k_1}), kappa := c C_m/(Phi_{k_1}^2
w_m(k_1)) (so d(omega^+) = c), and (b^-, omega^-) = (g, 0); Delta_m = -c < 0, and A_1(g) - A_2(g) = sum_{S_1} phi/V_1 -
sum_{S_2} phi/V_2 (+ later-target terms), arbitrary in [-c lambda_l M, c lambda_l M] (choose phi/v_l = 0 on S_1 and = c lambda M
on S_2).  For small c, Gamma_w of both pairs is small, so by Proposition prop:onesidedupper the one-sided coefficients of g
are finite; the example shows the STRUCTURE (forced Delta = -c, oscillating profile), not a new mate class.  (Side +: eps_l phi has the sign eps_l = z on S^nat_l and -kappa lambda u_{k_1} is
z-signed by the choice of k_1; side -: z_j g(j) = -c z_j (R^*w)(j) + phi(j) <= 0 since z(R^*w) = lambda_l M v_l on S^nat_l
for the swallowing-type peak and phi <= c lambda M v_l.)

## 4.3 Lemma C5 (completion of the fine tail).  PROVED.
Let f^# be a first row with finite base support, l a level, J_fine := N \ (F^# u T(l) u union_{l' <= l} S_{l'}) (coordinates
touched by no coarse carrier), and Delta in R^I.  For z' in [-1,1]^{J_fine} let f(z') be the first row with forced data
(a^#, z^# with its J_fine-coordinates replaced by z') (admissible forced data: Remark rem:lemmaZ(c); a, e unchanged), w_m(z')
its block functionals and W(z') := sum_m Delta_m R_m^* w_m(z').  Then there is z'* with
    W(z'*)(j) = 0 if |z'*_j| < 1,   z'*_j W(z'*)(j) <= 0 if |z'*_j| = 1        (j in J_fine),
i.e. the shift vector -W(z'*) is exactly admissible (z-signed on contacts, zero on free coordinates) on J_fine, and
p*(f(z'*) - f^#) <= C_f T_lo(l)^3 log(1/T_lo(l)); coarse values are unchanged and block thresholds move by <= C_f T_lo(l)^3.
Proof.  Phi(z')_j := clamp_{[-1,1]}(z'_j - W(z')(j)) maps the compact convex metrizable set C := [-1,1]^{J_fine} (product
topology, J_fine countable) into itself.  Continuity: zhat(z') = z^#(z') + U e^# depends coordinatewise continuously on z';
(R_m^** zhat(z'))(k) = lambda_k u_k(zhat(z')) is continuous in l_1 by dominated convergence (sum_k lambda_k ||u_k||_1 < infinity);
R_m^** zhat(z') != 0 (a(zhat(z')) = ||a||_1 + nu = 1 and R_m^** is injective); the duality map of the smooth norm |.|_m is
norm-to-weak* continuous (Lemma A(d)), so each w_m(z')(k) is continuous and bounded by 1; W(z')(j) = sum_m Delta_m sum_k
lambda_k w_m(z')(k) u_k(j) is continuous by dominated convergence.  By the Schauder-Tychonoff theorem Phi has a fixed point
z'*; reading clamp(z_j - W_j) = z_j gives the three cases.  Cost: only coordinates of J_fine move, which no coarse carrier
touches; Z3 Lemma 3.1 with sum_{k > l} lambda_k <= T_lo(l)^3 gives the bound and the threshold/scalar motion.  QED
So the fine tail of a shifted data set can always be made exactly admissible at a cheap companion.  What Lemma C5 cannot do is
on the COARSE coordinates T(l) u union_{l' <= l} S^nat_{l'}: there the fine contributions -sum_m Delta_m sum_{k > l} lambda_k
w_m(k) u_k(j) (of size <= |Delta| T_lo(l)^3) must be absorbed EXACTLY by the coarse data.  On the near coordinates of a GOOD
coarse signature set this can be done by converting them into tiny-mass support coordinates with free signs chosen to keep
sum_s v_{l'}(s) z_s (hence the value and the room of l') unchanged up to the far tail (SKETCH: finitely many coordinates, cost
tiny; rooms matter only for pinning at f).  On the free coordinates of T(l) and on the signature sets of UNSWITCHED class-G
carriers hit by wrong-sign fine contributions, absorption requires the coarse shifted system to be STABLE: its exact
solutions with Delta != 0 must persist under perturbations of the Delta-columns of size T_lo(l)^3 (Slater-type condition:
strictly positive switching on those carriers, surjective equality rows on T(l)).

## 4.4 Conditional recovery and the remaining step
**Theorem C6 (case (II) with stable shifted resonance).**  SKETCH.  Suppose that at infinitely many levels a clean
sub-window w with case (II) satisfies: (ST_w) the coarse shifted exact cone at the companion (Part 2 system Sigma^# plus the
columns Delta_m R_m^* w^#_m restricted to coarse coordinates, with the coupling Delta_m = sum q^#_l tau_l of Part 3 (R4)) has a
Slater point with robust margin, and the configuration of every shifted block gives Delta_m >= 0 in the data convention
(configuration (ii): free decomposition shift downward), or Delta_m < 0 in blocks satisfying (SC) at the companions
(configuration (i)).  Then f in Rec.
Sketch.  Transplant (Prop. T with shift columns; Hoffman via Lemma H, exactification via Lemma L extended to the block scalars
A_m, M_m/C_m entering the coupling — this extension is NOT proved: block scalars are not independently tunable by the tools
of Part 2); fine completion by Lemma C5; absorption of the coarse fine-perturbations by (ST_w); recovery by Theorem E^>= or
Theorem E^SC (Part 3).  Gaps: the scalar exactification just named; the near-coordinate conversion; (SC) at the companion in
configuration (i) (the completion can make every fine carrier with H_k >> Phi_k a robust peak of the coherent sign, since in
configuration (i) the self-aligned choice z = sgn u_k on S_k gives |u_k(zhat)| >= delta_k ||h_k 1_{S_k \ F}||/n_k, but the
coarse carriers' distances and the absence of degenerate peaks must also be arranged).
**The precise remaining step for item (C) (OPEN).**  By Theorem C1, f fails the shift pinning at a clean sub-window w only
if rho^sh(kappa, f) <= b(w) (an exact or b-near-exact d-constrained coherent shift resonance of the closed coarse pattern).
If this happens at all but finitely many levels, a mate g whose decompositions use these resonances with oscillating
profiles (Proposition C4; such mates exist under exact coherence, Example in 4.2) can only be followed by data with Delta != 0,
which exist at a companion only if, besides the coarse resonance, the infinitely many identities of Corollary C3.1(b) hold on
the coarse free coordinates (fine tails are completable: Lemma C5).  Needed: either (a) a version of Corollary cor:D1 /
Theorem E for "shifted data exact on coarse coordinates and on J_fine, with errors of l_1 mass <= |Delta| T_lo^3 on the coarse
coordinates touched by fine targets" — an approximately-two-piece statement restricted to errors that are FINE-ORIGIN and
coordinate-localized, or (b) a proof that persistent oscillating shifts at all levels force a cancellation structure making
the identities of C3.1(b) hold at some companion, or (c) a design device making every coarse free coordinate inaccessible to
fine targets of shifted blocks (impossible with (T-d) density: Corollary C3.1(b)), or (d) a mechanism not based on exact
two-piece data.  No counterexample: nothing here suggests that such mates are not recoverable (at maximal contact they do
not arise, and under exact coherence they carry exact data).

**Remark 4.5 (independent tuning of the two block scalars).**  PROVED (local computation).  The coefficients of the coupling
(R4) at peaks and of the shift columns involve, besides values, the block scalars theta_m and A_m = |R_m^** zhat|_m (note
M/C = theta/A).  At a block vector without degenerate peaks and without carriers at the threshold, Lemma T gives
d theta/ds = -(d Psi/ds)/(d Psi/d theta) with d Psi/d theta = -2(A + theta) Phi_P^2 (Phi_P^2 := sum_{k in P} Phi_k^2).  For an
outward push |zeta(c)| -> |zeta(c)| + s at a peak c: d theta/ds = C/Phi_P^2 and dA/ds = 1 - Phi_P^2 d theta/ds = M.  For a push
|zeta(k)| -> |zeta(k)| + s' at a strict non-peak k with relative position rho_k = nu_k/theta: d theta/ds' = -rho_k M/Phi_P^2 and
dA/ds' = rho_k M (= |w(k)|).  Hence det d(theta, A)/d(s, s') = (C/Phi_P^2) rho_k M + (rho_k M/Phi_P^2) M = rho_k M/Phi_P^2 > 0
(the same for (theta, A + theta Phi^2_{pk})).  So both scalars can be tuned exactly and independently (inverse function
theorem, two-sided pushes by pulls/banks/z-moves) whenever the block has a robust peak and a robust strict non-peak with
w != 0 that are NOT variables of the polynomial system; the existence of such a non-peak is not guaranteed in case (II), which
is one of the gaps of Theorem C6.  (All peaks act identically on (theta, A) at first order, so two peaks do not suffice.)
# 5. Consequences for the open core (F finite)

**Master Theorem III.**  PROVED modulo V1's Master Theorem II (V1_notes.md 4.3, unrefereed at the time of writing).
Design D^{V2} built on V1's D_Omega (Def. 2.2 and Def. 3.2 added; all of V1's estimates use only b(w) <= T_lo(w)^4/(l Design),
which still holds), diagonal U, F finite.  If for infinitely many levels l some clean sub-window w of level l satisfies
      rho^sh(kappa(w), f) >= u(w),
then f in Rec (every (f, g), g in C(f), is in cl NA((c_0, p_N), l_2^2)).
Proof.  V1's Master Theorem II has exactly two non-structural hypotheses at w: (SH_w) (shift sources or robust shift cost
c_pi(w) >= u(w)) and (VR_w) (every extreme ray of the zero-cost cone has at most one robust d-component).  (SH_w) is used only
through |Delta d_m| M_m <= K'_d t (V1 2.3, Lemma S); Theorem C1(I) provides this with K_sh <= C_f Design^3/u^3 whenever
rho^sh >= u, and the window arithmetic absorbs it (Q(w) = (4 Design/u)^{omega+3}).  (VR_w) is used only to bound the
d-row part of the Hoffman constant of the transplant (V1 Prop. TR step "blockwise ray removal"); Theorem B replaces it: V1's
z-move closings (C1), (C2) give a row f_1 satisfying (A1) (V1 Lemma ST(a): L_0 values move by <= (|T(l)| + 1) b(w)); V1's donor
raise (C3) is the move set M_ass of Theorem B; V1's linear tuning (C4) is replaced by the combined Lemma TU solve of Theorem B,
Step 3, with targets the Lojasiewicz point v' (which absorbs the second-order side effects C Design^2 Lambda^2 of the donor
banks on the L_0 values); V1 Lemma ST gives (A2) and the statuses at f^# (the extra moves 2 eta << c_f Lambda).  At f^# the
whole exact system has Hoffman constant <= C_f^l Design^2/u (Theorem B(d)); the transplant (V1 Prop. TR with the Hoffman
projection onto Sigma^# in place of the blockwise ray removal) gives exact d-neutral window data at f^# with
K <= (room product) x C_f^l Design^2/u x (pinning constants), and Theorem E'' of V1 (= Z3 Theorem E with window-dependent
c_flat and banked/pulled supports) concludes.  The extra cost C_f Design^2 eta log(1/eta) is o(T_lo^2).  QED
**Residual list (F finite, D^{V2}).**  PROVED (logical): f notin Rec only if, for all but finitely many levels, every clean
sub-window w has rho^sh(kappa(w), f) <= b(w) [(C*): an exact or b-near-exact d-constrained coherent shift resonance in some
block lacking a shift source].  Compared with ADDENDUM 6: (A) assembly — V1; (B) multi-block rays — REMOVED (Theorem B);
(C) — reduced to (C*) (Theorem C1), with the structure of Part 4; (D) aligned corner — V1 5.1 (pulls on the peak), and
independently Lemma QB + Lemma 2.3 give a raise in every block (two-sided tuning of a robust buffer peak).
**What (C*) looks like (PROVED pieces, Part 4).**  A block lacking a source (all robust coarse peaks of one swallowing type,
plus a class-G strict non-peak of the opposite d-sign whose switching is zero-cost) in which the shift trace of the peaks is
compensated exactly, at the coarse level, by zero-cost switching satisfying the d-identity.  Mates using it with oscillating
profiles (Prop. C4) need data with Delta d != 0 (configuration (ii): Delta >= 0, Corollary cor:D1 applies; configuration (i):
Delta < 0, needs (SC)), which at a companion require exact cancellation of the fine contributions on the coarse free
coordinates (Prop. C3, Cor. C3.1(b)); the fine tail itself is completable (Lemma C5).  At maximal contact (C*) does not occur
(Cor. C3.1(c)).

# 6. Numerics (V2_work/, sanity checks only)
hoffman_minors_check.py: Lemma H on 300 random systems x 5 points (1500 tests, rows partly dependent / with equalities):
max dist/(bound (1.1)) = 1.0000 (attained for single active rows), max (1/sigma_min)/(minor bound (1.2)) = 1.0000; two-ray
example: dist_1/|D tau|_1 = 2/delta for delta = 1e-1 ... 1e-4 and <= 1/2 at delta = 0 (exact degeneracy is harmless).

# 7. Next steps
1. Referee Theorem B (in particular Step 4 against V1's Lemma ST, and the claim that the minors of every exact system used by
   an assembly are polynomials in the L_0-values up to row factors) and Theorem C1 (the list (R1)-(R7) and its errors).
2. (C*): (a) an approximately-two-piece Corollary D1 / Theorem E tolerating errors of l_1 mass <= |Delta| T_lo^3 localized on
   finitely many coarse free coordinates (they are fine-origin: below the window they are dominated by the scale only if the
   cushion is supplied — investigate tiny near-contact moves z_j -> z_j +- O(T_lo^3) at those coordinates, which change coarse
   values only by O(T_lo^3) and might turn the residual identities into one-sided conditions); (b) block-scalar
   exactification (two-parameter tuning of (theta_m, A_m) by a peak push and a non-peak push: Jacobian determinant
   rho_k M/Phi_P^2 > 0, computed in Part 4 notes as a remark) for Theorem C6; (c) decide whether persistent oscillating
   shifts at all levels are compatible with partial contact at all (a structure theorem would close (C*)).
3. Infinite F (item (E)): Theorem B and Theorem C1 are local in the level and should transfer to Y3's infinite-F framework.
