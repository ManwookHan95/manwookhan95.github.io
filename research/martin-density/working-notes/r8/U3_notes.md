# U3 notes (Round 8): adversarial and structural analysis of the residual (C*) — near-exact coherent shift resonance

Setting: paper/martin_density_note.tex (notation as there), finite block set I = {1..N}, p = p_N; design D^{V2} on V1's D_Omega with
diagonal base (plus V4's design conditions (SF*), (SF_tau), (b'), (Z0) where cited, and one harmless weight strengthening (W10) in
Part 4); F finite unless said otherwise.  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Part files: r8/U3_part1..5.md
(this file = U3_head + parts 1-5, byte-identical copies).  Scripts: r8/U3_work/{nl_check.py, nl_check2.py, vt_check.py}.
No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN (two precise steps left, Part 4.3/4.3').

## 0. Summary of the answers
(a) Construction.  The suggested route — perturb V4's self-aligned rows Baire-generically in their fixed-z fibre so that (BT) fails while
    (C*) persists — does NOT work: every tilting perturbation of a in a fixed-z fibre of an aligned row creates, in EVERY block,
    infinitely many exactly swallowed robust ANTI-type peaks (and keeps swallowing-type ones), i.e. both shift sources at every clean
    sub-window of every large level; such rows leave (C*) and are recovered by Master Theorem III' (Proposition FZ, Corollary FZ:
    PROVED).  Genuine non-(BT) (C*) rows exist nevertheless: the NESTED-TUNING rows f^infty (Theorem NT) — maximal contact, all
    carriers aligned except the q<0 carrier l_- of Construction SA, and infinitely many ALIGNED near-threshold strict non-peaks obtained
    by anti-owner signs and a nested choice of a; they fail (BT) and even (SC), and have rho^sh = 0 and c_pi = 0 at every clean
    sub-window of every large level (properties PROVED; existence SKETCH).  Their most dangerous mates — oscillating profiles on robust
    class-G peak signature sets, forced shift Delta < 0 — carry EXACT two-piece data (Proposition NT-M, PROVED; g in C(f) verified via
    Proposition prop:onesidedupper).
(b) Recovery.  The exact-data mates of f^infty are recovered (Corollary NT-R: PROVED modulo V4 Theorem 5.6, refereed, and the
    assumed design compatibility of V4's conditions with D^{V2}).  The general mate of f^infty, and every (C*) row, reduce to two
    precise steps (S1) coupling exactness and (S2) uniform composition of violation-tolerant engineered approximants (Part 4); for
    f^infty and for every single-shifted-
    block (C*) row with a free-ray q<0 carrier, (S1) holds (PROVED), so only (S2) remains.  The new mechanism that removes V2-ref's
    gaps (C*-1), (C*-4), (C*-5) is QUADRATIC BANK REPAIR (Lemma QB2, PROVED): a sign violation of l_1-mass epsilon at contacts is
    converted into a second-order cost by banks of total mass ~ epsilon^2/beta, so fine-origin violations (mass <= C T_lo^3, and
    <= C T_lo^{10} under (W10)) cost o(T_lo^6) — no exact absorption and no Slater condition are needed; the tail, including free
    coordinates, is handled by VIOLATION TOLERANCE of the engineered approximants (Lemma VT, PROVED at a single stage by a line-by-line
    modification of the proof of Theorem thm:engineered: a violation of l_1-mass epsilon costs at most 2 rho |tau| epsilon, only in the
    regimes |tau| > s_1, and is absorbed when 2 rho epsilon <= delta s_1/16).  What remains of (S2) is UNIFORMITY of the engineered
    construction along companions, made precise as (S2a)-(S2d) in Part 4.3'.
    Lower semicontinuity: along SOME (BT) sequences (V4's aligned re-alignments) the exact-data mates of f^infty are recovered, but
    lower semicontinuity of the fibre map FAILS along other (BT) sequences, even at a (BT) row: Theorem NL (PROVED) gives (BT) rows
    f_n -> f_SA (one far carrier flipped to an anti-type peak) with liminf dist(rho g, C(f_n)) > 0 for every oscillating mate g.  The
    mechanism is an exact rigidity of two-piece data (Lemma S, Corollary S1, Proposition S3: PROVED): with one block, a single
    anti-aligned contact or free coordinate outside the omega-supports forces Delta = 0 and a CONSTANT profile for every mate.
(c) The quantitative property.  Non-recovery of (C*) would require one of: (i) failure of (S1): the coupling rows Delta_m =
    d_m(omega^-) - d_m(omega^+) cannot be made exact inside the (exact, by V2 Cor. C1.1(a)) combinatorial resonance cone with a
    design-controlled constant — only possible with >= 2 shifted blocks or without a free-ray q<0 carrier; (ii) failure of (S2):
    non-uniformity of the engineered construction along the companions — the late-stage threshold s_late(f^#_w) falling below
    32 rho epsilon_w/delta (epsilon_w = fine-origin violation mass), or T_0 not scaling like the piece radius c_flat t — or in-window free
    violations with b^+(j) b^-(j) > 0.  The violation cost itself is harmless at every single stage obeying 2 rho epsilon <= delta s_1/16
    (Lemma VT, PROVED); the tail term (1/2) rho |tau| V_{>N''} of thm:engineered is absorbed the same way.  Finite SOCP models confirm the exact
    rigidity (oscillating part of the local fibre collapses from 1.6e-2 to 2.4e-8 under a far anti-type flip of norm 8.3e-7) and the
    quadratic bank law (least repairing bank mass / epsilon^2 = 0.83, 0.79, 0.75, 0.71 vs predicted rho^2 = 0.81); the window mass that
    Lemma VT places at a violated contact, 4 rho s_1 |b^theta_j| with s_1 >= 32 rho epsilon/delta, obeys the same quadratic law.

## 1. Results and labels
| # | Result | Label | Part |
|---|---|---|---|
| 1 | Lemma S (exact rigidity/sandwich of two-piece data, any coordinate outside the omega-supports) | PROVED | 1.1 |
| 2 | Corollary S1 (one block: profile constant unless shifted; anti-aligned/free coordinate forces Delta = 0) | PROVED | 1.2 |
| 3 | Corollary S2 (F, K finite, e.g. NA rows: no switching, no shift) | PROVED | 1.3 |
| 4 | Proposition S3 (necessary condition for following a non-constant profile along rows with exact data) | PROVED | 1.4 |
| 5 | Theorem NL (fibre map not lsc at f_SA along (BT) rows; oscillating mates lost) | PROVED (uses V4 Thm 2.2, Prop 3.2, Prop 5.3, refereed) | 1.5 |
| 6 | Lemma D' (shape of source-deficient blocks) | PROVED (V1 Lemma D, Lemma S(a)) | 2.1 |
| 7 | Proposition FZ (fixed-z tilts create anti-type and swallowing-type robust swallowed peaks in every block) | PROVED (any admissible T) | 2.2 |
| 8 | Corollary FZ (fixed-z tilts of aligned rows leave (C*) and are in Rec) | PROVED mod Master Theorem III' | 2.3 |
| 9 | Lemma A (one block: existence of shifted exact data = Omega-coherence of psi) | PROVED | 2.4 |
| 10 | Theorem NT (non-(BT), non-(SC) rows in (C*)): existence | SKETCH | 3.1 |
| 11 | Theorem NT: properties (b)-(e) given (a)-(c) incl. rho^sh = 0, c_pi = 0 | PROVED | 3.1 |
| 12 | Proposition NT-M (explicit oscillating coherent-shift mates of f^infty, exact data, c g in C(f)) | PROVED | 3.2 |
| 13 | Corollary NT-R (these mates are recovered) | PROVED mod V4 Thm 5.6 + design compatibility | 3.3 |
| 14 | Recovery of all mates of f^infty | SKETCH (only the uniform composition (S2) remains) | 3.4, 4.3, 4.3' |
| 15 | Lemma 3.5 (dead-zone bump) | PROVED | 3.5 |
| 16 | Lemma QB2 (quadratic bank repair; uniform flip bound) | PROVED | 4.1 |
| 17 | Lemma VT (violation tolerance of engineered approximants, single stage) | PROVED (modification of the proof of thm:engineered) | 4.2 |
| 18 | Proposition RT* (a),(b),(d),(f) / (c),(e) | PROVED / SKETCH | 4.3 |
| 19 | (S1) for a single shifted block with a free-ray q<0 carrier | PROVED | 4.3 |
| 20 | (S2a) uniform per-piece engineered bounds, (S2b) averaging at the engineered approximant, (S2d) free violations | SKETCH | 4.3' |
| 20' | (S2c) threshold comparison s_late(f^#_w) >= 32 rho epsilon_w/delta under (W_k) | HEURISTIC | 4.3' |
| 20'' | (S1) in general; (S2) as a whole (uniform composition) | OPEN (precise) | 4.3, 4.3' |
| 21 | Numerics (rigidity collapse; quadratic bank law) | sanity checks | 5 |

## 2. What is used
Note: Sections 1, 7, 8 (lem:threshold, lem:bookkeeping, lem:base, def:twopiece, prop:onesidedupper, thm:onesided, def:BT, def:SC,
thm:engineered and its proof, cor:D1, cor:BTrecovered, lem:switchbudget, lem:suplevel, lem:peakshift, rem:lemmaZ(c), def:SLD,
lem:rigidity).  Refereed: V4 Construction SA / Theorem 2.2 (with R3), Proposition 3.2, Proposition 5.3 (hysteretic re-run), Lemma 5.2,
Theorem 5.6 with Lemmas 5.4, 5.5; V1 Lemma D, Lemma S(a), Lemma 3.4', donor raise and assembly; V2 Theorem C1, Corollary C1.1(a),
Lemma 3.1, Theorem E^SC; Z3 Theorem E, Lemma U; Y1 Lemmas 3.2-3.5 and the source definitions.  New design input: (W10)
c_{l+1} <= T_lo(l)^{10} (an upper bound on weights; admissible as in V4 Lemma 2.1) — used only in Part 4.3(f).
# U3 part 1 — Exact rigidity of two-piece data, profile constancy, and failure of lower semicontinuity along block-tame rows

Setting: paper/martin_density_note.tex (notation as there), finite block set I = {1..N}, p = p_N; T admissible (for 1.1-1.4 any
admissible T; for 1.5 an SLD-type design with (SF*), (Z0) as in V4, e.g. D_Omega / D^{V2} augmented by V4's conditions); base
operator U arbitrary in 1.1-1.4, diagonal in 1.5.  Conventions: two-piece data (b^+-, omega^+-) as in Definition def:twopiece; the
DATA convention Delta_m := d_m(omega^-_m) - d_m(omega^+_m); psi_m := R_m^* w_m in l_1 (the block shift vector of f); for a pair of
data put Sigma(omega) := F ∪ ⋃_m ⋃_{k in supp omega^+_m ∪ supp omega^-_m} supp u_{k,m}.

## 1.1 Lemma S (exact rigidity / sandwich).  PROVED (any admissible T).
Let f in S_{p*} have F finite and let h in X* carry two-piece data (b^+-, omega^+-).  Put c^+-(j) := sum_m d_m(omega^+-_m) psi_m(j)
and W_Delta := sum_m Delta_m psi_m.  Then for every j notin Sigma(omega):
 (a) h(j) = b^+(j) - c^+(j) = b^-(j) - c^-(j);
 (b) if j is a free coordinate (|z_j| < 1): b^+(j) = b^-(j) = 0, hence h(j) = -c^+(j) = -c^-(j) and W_Delta(j) = 0;
 (c) if j is a contact (|z_j| = 1): z_j (h(j) + c^+(j)) >= 0 >= z_j (h(j) + c^-(j)); in particular z_j W_Delta(j) <= 0.
Proof.  At j notin Sigma(omega), (R_m^* omega^+-_m)(j) = sum_k lambda_{k,m} omega^+-_m(k) u_{k,m}(j) = 0 for every m, so the two
representations h = b^+- + sum_m R_m^*(omega^+-_m - d_m(omega^+-_m) w_m) read h(j) = b^+-(j) - c^+-(j): (a).  Side admissibility
(Definition def:twopiece): b^+-(j) = 0 for j notin F ∪ K, which gives (b); z_j b^+(j) >= 0 >= z_j b^-(j) for j in K, which gives the
first part of (c).  Subtracting, z_j (c^+(j) - c^-(j)) >= 0, and c^+ - c^- = -W_Delta.  QED
(This is V2's Proposition C3 together with the sandwich inequalities themselves; the point here is that it needs NO smallness or
dominance hypothesis and holds at every coordinate outside Sigma(omega).)

## 1.2 Corollary S1 (one block: the profile is constant unless the data are shifted).  PROVED (N = 1, any admissible T).
Let N = 1, f with F finite, h with two-piece data, psi := R^* w, Delta := d(omega^-) - d(omega^+).  For j notin Sigma(omega) with
psi(j) != 0 put pi_h(j) := h(j)/psi(j) (the PROFILE of h at j).  Call a contact j ALIGNED if z_j psi(j) > 0 and ANTI-ALIGNED if
z_j psi(j) < 0.  Then, for j notin Sigma(omega) with psi(j) != 0:
 (i)   j free: Delta = 0 and pi_h(j) = -d(omega^+) = -d(omega^-);
 (ii)  j aligned contact: -d(omega^+) <= pi_h(j) <= -d(omega^-) (so Delta <= 0);
 (iii) j anti-aligned contact: -d(omega^-) <= pi_h(j) <= -d(omega^+) (so Delta >= 0).
Consequently: the oscillation of pi_h over the aligned contacts outside Sigma(omega) is at most |Delta|; and if, outside
Sigma(omega), there is a free coordinate or an anti-aligned contact with psi != 0, then Delta <= 0 forces Delta = 0 as soon as one
aligned contact exists, and pi_h is CONSTANT (= -d(omega^+)) on all free coordinates and all (aligned or anti-aligned) contacts outside
Sigma(omega) with psi != 0.
Proof.  Lemma S with c^+-(j) = d(omega^+-) psi(j).  (i) is (b).  (ii): divide z_j(h(j) + d^+ psi(j)) >= 0 and z_j(h(j) + d^- psi(j)) <= 0
by z_j psi(j) > 0.  (iii): the same with z_j psi(j) < 0, which reverses both inequalities.  The interval in (ii) is non-empty only if
d^- <= d^+, the one in (iii) only if d^+ <= d^-.  QED

## 1.3 Corollary S2 (finitely many contacts: no switching, no shift).  PROVED (any admissible T, any N).
If F and K are finite (in particular at every norm-attaining f, Proposition prop:smooth(c)), every pair of two-piece data has
b^+ = b^-, omega^+ = omega^- and Delta_m = 0 for every m.
Proof.  v := b^+ - b^- = sum_m R_m^*(omega^-_m - omega^+_m) - W_Delta lies in Y (each R_m^* maps into Y) and is supported in the finite
set F ∪ K (side admissibility).  By (T-c), v = 0.  Then L^* applied to (Delta_m w_m - (omega^-_m - omega^+_m))_m vanishes; L^* is
injective on V^* (eq:Lstar), so Delta_m w_m = omega^-_m - omega^+_m for each m.  The right side is finitely supported in Q_m, while
w_m = +-M_m != 0 on the non-empty peak set P_m; hence Delta_m = 0 and omega^-_m = omega^+_m.  QED
(At NA rows exact data cannot carry ANY shift or switching; scale-dependent structure of mates of NA rows lives only in their
decompositions at positive scales.  This is the precise sense of Remark rem:onesided(a).)

## 1.4 Proposition S3 (necessary condition for following a non-constant profile).  PROVED (N = 1, any admissible T).
Let f in S_{p*} have F finite, g in C(f), rho in (0,1], and let s_1, s_2 be coordinates with psi(s_1), psi(s_2) != 0 and
pi_g(s_1) != pi_g(s_2) (pi with respect to psi = R^* w of f).  Let f_n -> f be rows with F_n finite at which every mate carries
two-piece data (e.g. (BT) rows, Theorem thm:onesided(c)), and let Q_n be the strict non-peak set of f_n and
Sigma_n := F_n ∪ ⋃_{k in Q_n} supp u_k.  Suppose that for infinitely many n:
 (1) s_1, s_2 notin Sigma_n, and each of them is a free coordinate or a contact of f_n; and
 (2) outside Sigma_n, f_n has an aligned contact and, in addition, a free coordinate or an anti-aligned contact with psi_n != 0
     (alignment taken with respect to psi_n := R^* w^{(n)} and z^{(n)}).
Then rho g notin Li_n C(f_n); quantitatively, along those n,
     dist_{l_1}(rho g, C(f_n)) >= (rho kappa_0 - rho ||g||_inf (|psi_n - psi|(s_1) + |psi_n - psi|(s_2)))/2,
     kappa_0 := |psi(s_1) psi(s_2)| |pi_g(s_1) - pi_g(s_2)| > 0,
and the right side tends to rho kappa_0/2 (psi_n -> psi in l_1, Proposition prop:continuity).
Proof.  Let G in C(f_n) and take two-piece data of G at f_n.  Their omega-supports lie in Q_n, so Sigma(omega) ⊂ Sigma_n.  By (2) and
Corollary S1 (applied at f_n), Delta = 0 and pi^{(n)}_G is constant on the free coordinates and contacts outside Sigma_n with psi_n != 0;
by (1) this applies at s_1, s_2 if psi_n(s_i) != 0, and then G(s_1) psi_n(s_2) - G(s_2) psi_n(s_1) = 0.  If psi_n(s_i) = 0 for some i,
Lemma S(a)-(c) with Delta = 0 gives G(s_i) = -d^+ psi_n(s_i) = 0, and the same identity holds.  The functional
Lambda_n(h) := h(s_1) psi_n(s_2) - h(s_2) psi_n(s_1) satisfies |Lambda_n(h)| <= ||h||_1 (|psi_n(s_1)| + |psi_n(s_2)|) <= 2 ||h||_1 since
||psi_n||_inf <= sum_k lambda_k ||u_k||_inf <= 1.  Hence 2 ||G - rho g||_1 >= |Lambda_n(rho g)|, and |Lambda_n(rho g)| >= rho kappa_0 -
rho ||g||_inf (|psi_n - psi|(s_1) + |psi_n - psi|(s_2)).  QED
Reading.  To recover a mate whose profile is not constant on {s_1, s_2}, approximants at which mates have exact data must, for all
large n, either put s_1 or s_2 into Sigma_n (make it a support coordinate — a bank — or cover it by the support of a strict
non-peak), or be ALIGNED WITH MAXIMAL CONTACT outside Sigma_n (no free coordinate and no anti-aligned contact with psi_n != 0).
The engineered approximants of Section sec:engineered use the first alternative (window masses = banks on contacts); NA rows can
only use the first alternative (they have cofinitely many free coordinates, Corollary S2).

## 1.5 Theorem NL (failure of lower semicontinuity at a self-aligned row along block-tame rows).  PROVED
(design with (SF*), (Z0); diagonal U; N = 1; uses only V4's refereed Construction SA / Theorem 2.2 / Proposition 3.2 and the
hysteretic re-run of Proposition 5.3.)
Let f := f_SA (V4 Construction SA(1, eta), Theorem 2.2; N = 1), with its exceptional carrier l_- (target y*, strict non-peak, q < 0)
and k_- := k(l_-).  Then there are rows f_n -> f satisfying (BT) (hence f_n in Rec by Corollary cor:BTrecovered) such that for every
g in C(f) whose profile is non-constant on two coordinates s_1, s_2 of a signature set S_l (l != l_-), and every rho in (0,1],
     liminf_n dist(rho g, C(f_n)) >= rho kappa_0(g; s_1, s_2)/2 > 0.
Such g exist: the coherent-shift mates of V4 Proposition 3.2 with a coordinate-dependent split chi.  In particular the fibre map
f' -> C(f') is NOT lower semicontinuous at the block-tame row f along this sequence of block-tame rows, although every mate of f is
recovered along the engineered approximants of f.
Proof.  Step 1 (the rows f_n).  Recall from Construction SA: F = {p, p'} ⊂ Z_0, every carrier except l_- is owner-assigned with sign
eps_l, z = eps_l on S_l, and n_{l_-} val_{l_-} = y*(zhat_F) + delta_{l_-} H_{l_-} = -eta, so y*(zhat_F) = -(eta + delta_{l_-} H_{l_-}) < 0.
Since y* occurs as a target at infinitely many carriers of the block (Theorem 2.2 Step 1: infinitely many carriers have target y*),
choose such carriers o_n -> infinity, o_n > l_-, with delta_{o_n} H_{o_n} < (eta + delta_{l_-} H_{l_-})/2.  For these, supp y* = F, so
B_{o_n} = 0, A_{o_n} = y*(zhat_F) < 0, eps_{o_n} = -1 and z = -1 on S_{o_n} in f.
Define f_n: same a; z^{(n)} := z except: z^{(n)} := +1 on S_{o_n}, and the coordinates owned by carriers l > o_n are re-assigned by the
HYSTERETIC re-run of V4 Proposition 5.3 (reference signs eps_l of f; keep eps_l unless eps_l A_l <= -(B_l + delta_l H_l)/2, in which
case eps_l := sgn A_l).  Coordinates owned by carriers < o_n are unchanged (allowedness (a): coarser targets avoid S_{o_n}; disjoint
signatures), so z^{(n)} -> z coordinatewise and a^{(n)} = a; by Remark rem:lemmaZ(c), f_n -> f in S_{p*}.
Step 2 (f_n is (BT)).  Values of carriers < o_n are unchanged.  n val_{o_n}^{(n)} = A_{o_n} + delta_{o_n} H_{o_n} <= -(eta + delta_{l_-}
H_{l_-})/2 < 0 while z^{(n)} = +1 on S_{o_n}: o_n is an exactly swallowed ANTI-TYPE carrier with |val| >= eta/(2 n_{o_n}), hence a peak
(nu = m|val|/Phi_{o_n} -> infinity relative to theta; Theorem 2.2 Step 3 bounds theta) with margin >= q_0 eta/4.  Every re-run carrier
l > o_n has n_l |val_l| >= (B_l + delta_l H_l)/2 with sign eps_l (Proposition 5.3's re-run, which uses only the owner recursion,
allowedness and (SF*)), hence is a swallowing-type peak with margin >= q_0 delta°_l/4 (Theorem 2.2 Step 4 with |val_l| >= delta°_l/2).
The threshold theta^{(n)} -> theta (zeta^{(n)} -> zeta in l_1), so the finitely many carriers whose status is not robust by Step 4
(the first carrier of the block and l_-) keep their statuses for large n.  Thus Q^{(n)} = {k_-}, there is no degenerate peak, and
(MS) holds (Theorem 2.2 Step 8 with margins >= q_0 delta°_l/4 beyond a finite set): f_n satisfies (BT).
Step 3 (alignment at f_n).  Sigma_n = F ∪ supp u_{l_-} = F ∪ S_{l_-} (Q^{(n)} = {k_-}, supp y* = F).  Every coordinate off F is a
contact of f_n (the owner recursion assigns +-1 everywhere, V4 Lemma 1.2).  For s in S_c (c a carrier other than l_-, owner c):
psi_n(s) = lambda_c w^{(n)}(c) v_c(s) + sum_{l > c} lambda_l w^{(n)}(l) y_l(s)/n_l, and by the dominance estimate of Theorem 2.2 Step 6
(which bounds MODULI of the later terms using allowedness (b) and (SF*); |w| <= 1) the later sum is at most 2^{-5} lambda_c v_c(s) <=
2^{-4} lambda_c |w^{(n)}(c)| v_c(s) (|w(c)| = M >= 1/2 at peaks).  Hence sgn psi_n(s) = sgn w^{(n)}(c) = sgn val^{(n)}_c, psi_n(s) != 0.
For every swallowing-type peak c (all carriers except l_- and o_n) the contacts of S_c are ALIGNED; the contacts of S_{o_n} are
ANTI-ALIGNED (z = +1, w(o_n) = -M).  Both lie outside Sigma_n.  So hypothesis (2) of Proposition S3 holds at every f_n, and (1) holds
for any s_1, s_2 in S_l, l != l_-, once o_n > l (they are aligned contacts of f_n and of f).
Step 4 (conclusion).  Proposition S3.  Existence of g: in V4 Proposition 3.2 the split chi: F^c -> [0,1] may be chosen coordinatewise
(b^+ := chi Delta_alpha lambda_{l_-} V 1_{F^c} + beta^+ is z-signed because V 1_{F^c} is z-signed and chi >= 0; b^- = b^+ - Delta_alpha
lambda_{l_-} V = (chi - 1) Delta_alpha lambda_{l_-} V 1_{F^c} + beta^- is (-z)-signed because chi <= 1); part (iv) of that proposition gives
c g in C(f) for small c > 0.  At s in S_l (l != l_-), u_{l_-}(s) = 0 and omega^+ vanishes, and V = u_{l_-} - (val_{l_-}/|zeta^|) psi, so
     g(s) = chi_s Delta_alpha lambda_{l_-} V(s) - d(omega^+) psi(s) = psi(s) ( -d(omega^+) + chi_s Delta_alpha lambda_{l_-} |val_{l_-}|/|zeta^| )
EXACTLY.  Hence pi_g(s_1) - pi_g(s_2) = (chi_{s_1} - chi_{s_2}) Delta_alpha lambda_{l_-} |val_{l_-}|/|zeta^| != 0 when chi_{s_1} != chi_{s_2}.  QED
Remarks.  (a) The same proof gives non-recovery along ANY sequence of rows with exact data for all mates which contain, at least
once per row, an exactly swallowed anti-type robust peak (or a free coordinate with psi_n != 0) outside Sigma_n, while keeping two
aligned contacts s_1, s_2 outside Sigma_n.  So the Baire-generic rows of V4 Proposition 5.1 (fixed z, perturbed a; they acquire
anti-type peaks, Part 2) and NA rows without banks on {s_1, s_2} cannot be used to recover oscillating mates.
(b) Theorem NL does not contradict f in Rec (f is (BT)): the engineered approximants of f put window masses (banks) on contacts, i.e.
use the first alternative of Proposition S3, and keep all far carriers aligned.  Any recovery proof for (C*) rows must therefore
use approximants that (i) keep every peak of a shifted block exactly swallowed and ALIGNED at the fine levels (no fine anti-type
robust peak of a shifted block and no fine free coordinate with psi != 0 outside the omega-supports) or (ii) bank the oscillation
coordinates.  This is a precise version of "the approximating sequence must be engineered", and it explains why lower
semicontinuity along the dense set of (BT) rows (V4 Proposition 5.3) cannot be expected for an ARBITRARY dense sequence; Proposition
5.3's own re-alignment keeps the reference signs (hysteresis) and is aligned in this sense.
(c) Numerical check: U3_work/nl_check.py (Part 5).
# U3 part 2 — What (C*) forces, and why the Baire-generic perturbations of self-aligned rows leave (C*)

Setting: design D^{V2} on V1's D_Omega with diagonal base U (U^* e_j^* = s_j kappa_j), finite I, F finite; V2's residual
(C*) = "at all but finitely many levels EVERY clean sub-window w has rho^sh(kappa(w), f) <= b(w) AND c_pi(w) <= b(w)".
Notation as in Part 1; for an SLD-type design u_k = (y_k + delta_k h_k)/n_k, v_k = delta_k h_k/n_k.

## 2.1 Lemma D' (shape of a source-deficient block).  PROVED (V1 Lemma D + V1 Lemma S(a), refereed).
At every clean sub-window w of level l >= l_f, every block has a coarse peak with relative position rho >= 1 + u(w).  If block m
has no UPPER source at w, then every coarse peak of block m with rho >= 1 + u(w) is a class-G SWALLOWING-type peak; if block m
has no LOWER source at w, every such peak is a class-G ANTI-type peak.  (A class-R peak with rho >= 1 + u is a source of both
kinds; a class-G anti-type peak is (U2); a class-G swallowing-type peak with rho >= 1 + u is (L2).)
So in a (C*) block, at all large levels, every robust coarse peak is (relative room <= b(w) on its natural signature set) of ONE
type: the self-aligned rows of V4 (all peaks swallowing-type) are the model of an UPPER-deficient block (configuration (i),
Delta^{data} < 0), the "anti-aligned" rows the model of a LOWER-deficient block (configuration (ii)).

## 2.2 Proposition FZ (fixed-z perturbations create both kinds of exactly swallowed robust peaks).  PROVED.
Let T be ANY admissible operator, U diagonal, F finite with d := |F| >= 2, sigma in {-1,1}^F, z in B_{l_inf} with z = sigma on F,
A_sigma := {a : supp a = F, sgn a = sigma, q*(a) = 1}, f_a the row with forced data (a, z) (Remark rem:lemmaZ(c)).  For a in A_sigma
put nu(a) := ||U^* a||, b(a) := (s_j a_j)_{j in F}/nu(a) and Phi(a) := (sigma_j + s_j b_j(a))_{j in F} in R^F, so that zhat(a)_j =
Phi(a)_j on F and zhat(a)_j = z_j off F.  Let a_0, a_1 in A_sigma with Phi(a_0), Phi(a_1) not positively proportional.  Then there is
eta > 0 such that every block m contains infinitely many carriers k with
     val_k(a_0) >= eta/2 and val_k(a_1) <= -eta/2,
and infinitely many carriers k' with val_{k'}(a_0) >= eta/2 and val_{k'}(a_1) >= eta/2  (val_k(a) := u_k(zhat(a))).
Proof.  For a in A_sigma, b_j(a) = s_j a_j/nu(a) has the sign sigma_j, so Phi(a)_j = sigma_j (1 + s_j |b_j(a)|): every Phi(a) lies in
the OPEN orthant of the signs sigma, and <Phi(a_0), Phi(a_1)> > 0.  Since Phi(a_0), Phi(a_1) are not positively proportional, the closed
rays R_+ Phi(a_0), R_+ Phi(a_1) meet only at 0 and are not opposite, so they are strictly separated by a hyperplane through 0: there is
c in R^F with <c, Phi(a_0)> > 0 > <c, Phi(a_1)>.  Put c' := Phi(a_0).  Let y_0 := c/q*(c), y'_0 := c'/q*(c') (vectors supported in F);
for y supported in F, y(zhat(a)) = <y, Phi(a)> (diagonal base: (Ue)_j = s_j^2 a_j/nu = s_j b_j on F and 0 off F).  Put
eta := min(<y_0, Phi(a_0)>, -<y_0, Phi(a_1)>, <y'_0, Phi(a_0)>, <y'_0, Phi(a_1)>) > 0.  By (T-d) every tail of (u_{k,m})_k is q*-dense in
S_{q*}, so there are carriers k_i -> infinity of block m with q*(u_{k_i} - y_0) < eta/2, and likewise k'_i for y'_0.  Since
q**(zhat(a)) = 1, |u(zhat(a)) - y(zhat(a))| <= q*(u - y) for every a and every u, y in l_1.  QED
(Whether Phi(a_0), Phi(a_1) are positively proportional is a codimension-(d-1) coincidence; for a_1 on a curve through a_0 in a
generic direction it fails for all a_1 != a_0 near a_0.)

## 2.3 Corollary FZ (fixed-z perturbations of aligned rows leave (C*) and are recovered).  PROVED modulo the refereed Master
Theorem II/III' (V1, V2).
Let T = D^{V2} on D_Omega, U diagonal, F finite, d >= 2, and let f_0 = f_{a_0} be a row such that in every block
all but finitely many carriers k are EXACTLY SWALLOWED WITH THE SIGN OF THEIR VALUE (z = sgn val_k(a_0) on S_k; S_k ∩ F = {} for large
k by allowedness (a)) — e.g. the self-aligned rows of V4 Theorem 2.2 and the rows f^infty of Part 3.  Then for every a_1 in A_sigma with
Phi(a_1) not positively proportional to Phi(a_0), the row f_{a_1} (same z) has, in EVERY block, infinitely many exactly swallowed
robust anti-type peaks and infinitely many exactly swallowed robust swallowing-type peaks.  Consequently, at every clean sub-window
of every sufficiently large level, every block has an UPPER source (U2) and a LOWER source (L2); hence (SP_w) holds, Y1/V1's shift
pinning applies, rho^sh(kappa(w), f_{a_1}) >= 1 (V2 Theorem C1, case (I)), f_{a_1} is NOT a (C*) row, and f_{a_1} in Rec (Master Theorem
III').
Proof.  Proposition FZ: carriers k_i of block m have val(a_0) >= eta/2, hence (hypothesis) z = +1 on S_{k_i}, while val(a_1) <= -eta/2:
at f_{a_1} they are exactly swallowed (room 0 on every natural signature set, so class G at every level) with w = -M: anti-type; as
|val(a_1)| >= eta/2 and Phi_{k_i} -> 0, nu = m|val|/Phi -> infinity relative to the (fixed) threshold of f_{a_1}: peaks whose relative
position rho = nu/theta exceeds 1 + u(w) at every clean w of large level (u(w) -> 0).  The carriers k'_i are exactly swallowed robust
swallowing-type peaks in the same way.  A fixed carrier, once coarse, stays coarse; so for all large levels the closed pattern of every
clean w contains, in every block, a class-G anti-type peak (U2) and a class-G swallowing-type peak with rho >= 1 + u (L2).  V2's Theorem
C1 (whose case (I) contains (SP_w), V2-ref verdict table) and Master Theorem III' (f in Rec if infinitely many levels have a clean w
with rho^sh >= u or (SH_w); (SP_w) is (SH_w) with I_up ∪ I_lo = {}) give the claims.  QED
Consequences.  (a) (C*) is NOT open in any fixed-z fibre: it is destroyed by every perturbation of a that tilts Phi.  V4's Baire-generic
near-threshold rows (Proposition 5.1) of a self-aligned fibre are recovered by the window method, not residual.  The task's
suggested construction ("perturb self-aligned rows Baire-generically so that (BT) fails while (C*) persists") therefore does not
work in fixed-z fibres; a (C*) row must keep every robust peak of a deficient block aligned (or anti-aligned) at all fine levels, which
forces z to be re-aligned together with a (Part 3).
(b) Along f_{a_1} -> f_{a_0} (a_1 -> a_0 in a tilting direction), the oscillating coherent-shift mates of f_{a_0} are generically lost:
whenever f_{a_1} is a row at which every mate carries two-piece data (e.g. a (BT) row in the fibre), Proposition S3 applies (its
anti-type peaks provide anti-aligned contacts outside Sigma_n).  For rows of the fibre that are not (BT) this is the window version of
the same mechanism (Y1 Lemma 3.3(b): an anti-type G-peak bounds Delta d_m M_m <= (tau)_-/lambda <= K t/lambda), i.e. the shift is pinned
and Proposition C4 of V2 kills the oscillation at all scales of all large windows.  So the fibre map is not lower semicontinuous at
f_{a_0} along fixed-z perturbations either (HEURISTIC for non-(BT) f_{a_1}; PROVED for (BT) ones by Proposition S3).

## 2.4 Lemma A (what an exact shifted datum needs, one block).  PROVED (N = 1, any admissible T).
Let f have F finite.  Two-piece data with Delta != 0 and omega-carrier set Omega exist for SOME functional only if, outside Sigma(omega):
(i) psi = R^* w vanishes at every free coordinate, and (ii) z_j psi(j) has the sign of -Delta... precisely z_j Delta psi(j) <= 0 at every
contact j (Lemma S(b),(c)).  Conversely, if (i), (ii) hold for some Delta < 0 (resp. > 0) and some finite Omega ⊂ Q with omega-differences
chosen so that psi-terms on Sigma(omega) are z-signed, then for every omega^+ supported in Omega, every split chi in [0,1]^K and every base
part beta on F there are two-piece data with these parameters; they represent h = b^+ + R^*(omega^+ - d(omega^+) w).
Proof.  Necessity is Lemma S.  Sufficiency: put omega^- := omega^+ + gamma with gamma supported in Omega and d(gamma) = Delta (possible
if some k in Omega has w(k) != 0; d(e_k) = Phi_k^2 w(k)/C), v := R^* gamma - Delta psi, b^+ := chi v 1_{K} + beta, b^- := b^+ - v; then b^+ is
z-signed and b^- is (-z)-signed on K iff v is z-signed on K, v vanishes off F ∪ K iff it vanishes at free coordinates; off Sigma(omega),
v = -Delta psi, so (i), (ii) are exactly these conditions there, and on Sigma(omega) they are the stated choice.  The pairs represent the
same h since b^+ - b^- = v = R^*(omega^- - omega^+) - Delta psi.  QED
Reading.  For N = 1 the existence of shifted exact data is a property of (f, Omega) alone: psi must be "Omega-coherent" (zero at free
coordinates and of the sign -sgn(Delta) z at contacts, outside Sigma(omega)).  For an owner-aligned row psi is z-signed at every
coordinate whose owner has w != 0 (dominance, V4 Theorem 2.2 Step 6); so the only obstructions are (a) free coordinates outside the
omega-supports, (b) contacts whose owner is NEUTRAL (w = 0) or anti-aligned ("dead zones", V4 Section 12), and (c) the sign of Delta
(configuration (i) needs psi z-signed, configuration (ii) needs psi (-z)-signed).  With several blocks, psi is replaced by W_Delta =
sum_m Delta_m psi_m and blocks with Delta_m = 0 contribute nothing at the coordinates they own: every coordinate owned by a carrier of an
UNSHIFTED block is a dead zone for the shifted blocks.  This is the structural core of (C*-1).
# U3 part 3 — Explicit non-(BT) first rows in (C*): the nested-tuning rows f^infty; their mates and their recovery

Design: an SLD-type design with V4's (SF*), (SF_tau), (b'), (Z0) (V4 Lemma 2.1: designable; V4-ref: compatible in appearance with
D_Omega / D^{V2}, not checked line by line — this compatibility is ASSUMED here and flagged); diagonal base; N = 1 (Remark 3.6 for
N >= 2).  F = {p, p', p''} ⊂ Z_0, sigma = (+,+,+), y* = (e_p^* - e_{p'}^*)/q*(e_p^* - e_{p'}^*) a target of the family (Z0).
Owner rule (V4 Construction SA, step (2)): carriers in increasing order; A_l := sum_{j in supp y_l assigned} y_l(j) zhat_j,
B_l := sum_{j in supp y_l unassigned} |y_l(j)|; a carrier with sign eps_l sets z_j := eps_l sgn y_l(j) at its unassigned target
coordinates and z := eps_l on S_l; then n_l val_l = A_l + eps_l (B_l + delta_l H_l) (V4 Lemma 1.1).  OWNER sign: eps_l := sgn A_l
(+1 if A_l = 0); then |n_l val_l| = |A_l| + B_l + delta_l H_l and the carrier is an aligned robust peak (V4 Theorem 2.2 Step 4).
ANTI-OWNER sign: eps_l := -sgn A_l; if |A_l| < B_l + delta_l H_l the value keeps the sign eps_l (still ALIGNED: z = sgn val on S_l)
and |n_l val_l| = B_l + delta_l H_l - |A_l| can be made as small as desired by tuning A_l.

## 3.1 Theorem NT (non-(BT) rows in (C*)).  Existence: SKETCH (nested tuning; every step is a finite-dimensional continuity /
## implicit-function argument, written below in outline).  Properties (b)-(e) of the constructed row: PROVED.
There are a in A_sigma, a carrier l_- with target y*, an infinite set Lambda = {l_1 < l_2 < ...} of carriers and a sign vector
z in {-1,1}^{N \ F} such that the row f^infty with forced data (a, z) satisfies:
 (a) every coordinate off F is a contact (maximal contact); every carrier l notin Lambda ∪ {l_-} carries the OWNER sign;
 (b) l_- carries eps = +1 with n val_{l_-} in (-eta, -eta/2) for a fixed small eta: an exactly swallowed anti-type strict non-peak,
     q_{l_-} < 0, relative position rho_{l_-} <= 1/2 (gap >= M/2), and u_{l_-} 1_{F^c} = v_{l_-} is z-signed;
 (c) every l_i in Lambda carries the ANTI-OWNER sign with |A_{l_i}| < B_{l_i} + delta_{l_i} H_{l_i}: an exactly swallowed ALIGNED
     (swallowing-type, q > 0) strict non-peak with relative gap g_i := 1 - nu_{l_i}/theta in (0, Phi_{l_{i+1}}/2);
 (d) Q = {k_-} ∪ {k(l_i) : i >= 1} is infinite, there is no degenerate peak, so f^infty is NOT (BT); and the block fails (SC):
     Scr(s) >= s for every 0 < s <= Phi_{l_1};
 (e) (C*): at every clean sub-window w of every large level, rho^sh(kappa(w), f^infty) = 0 and c_{pi(w)}(f^infty) = 0.
Construction (outline).  Parametrize A_sigma by b in the open positive orthant Omega of S^2 (d = 3).  Stage 0: by the intermediate
value theorem on the ratio a_p/a_{p'} (V4 Theorem 2.2 Step 1) choose a closed ball B_0 ⊂ Omega on which y*(zhat_F) + delta_{l_-} H_{l_-}
in (-eta, -eta/2) (an open condition; l_- late enough, as in V4).  Stage i -> i+1: we hold a closed ball B_i, a level L_i, the carriers
l_1 < ... < l_i, such that (I1) every carrier l <= L_i has constant owner data (eps_l and assigned/unassigned status of its target
coordinates) on B_i, (I2) all values val_l, l <= L_i, are continuous on B_i, (I3) the non-special carriers <= L_i are aligned robust
peaks and l_1, ..., l_i satisfy (c) on B_i with a provisional gap bound g_i < 2 gamma_i (gamma_i to be fixed at the next stage), (I4)
the carriers > L_i change theta by at most L_Theta 2(1 + ||U||) sum_{l > L_i} lambda_l, which is < gamma_i theta/8 on B_i (Lemma 5.2 of V4:
theta is Lipschitz in zeta).  (i) Pick a vector c in R^F with <c, Phi(b)> = 0 at the centre b^(i) of B_i and with tangential
gradient (s_j c_j)_j independent of the tangential gradient of nu_{l_i} - theta at b^(i) (d - 1 = 2); by (T-d) pick a target r of the
family with q*(y^(r) - c/q*(c)) tiny, and enlarge L_i so that the owners of the finitely many coordinates of supp y^(r) \ F are
<= L_i (shrinking B_i so that (I1) persists: only finitely many owner signs are involved, none with A_l = 0 at b^(i) after an
arbitrarily small move of b^(i)).  Then for every later carrier l using target r, B_l = 0 and A_l = y^(r)(zhat) =: psi_r, a function
on B_i with non-vanishing gradient and |psi_r(b^(i))| tiny.  (ii) Choose such a carrier l_{i+1} > L_i with delta H small enough that
the hypersurface {psi_r = -delta_{l_{i+1}} H_{l_{i+1}}} passes through B_i near b^(i) (implicit function theorem), and give it the
anti-owner sign eps = +1 (so A = psi_r < 0 there and n val = psi_r + delta H in (0, B + delta H)).  (iii) By transversality, the
region of B_i where both g_i in (0, Phi_{l_{i+1}}/2) and n val_{l_{i+1}} in (n theta Phi_{l_{i+1}}(1 - 2 gamma_{i+1})/m, n theta Phi_{l_{i+1}}
(1 - gamma_{i+1})/m) is a non-empty relatively open set (both conditions are thin one-sided neighbourhoods of two transversal
hypersurfaces through points close to b^(i)); choose gamma_{i+1} small, B_{i+1} a closed ball inside it, and L_{i+1} >= l_{i+1} so large
that (I4) holds with gamma_{i+1}, shrinking B_{i+1} to keep (I1).  Then (I1)-(I4) hold at stage i + 1.  Finally b^infty in ∩ B_i, and
z := the owner data of all carriers at b^infty (constant by (I1) along the nest), with the anti-owner sign on Lambda and +1 on l_-.
Proof of (b)-(e) given (a)-(c) at b^infty.  (b), (c): by (I3) and continuity at b^infty (the shell inequalities are strict on each
B_i ⊃ B_{i+1} ∋ b^infty, and the threshold error of (I4) is < gamma theta/8).  (d): Q is as stated; no peak has nu = theta (non-special
peaks have nu >= 2^10 theta beyond the first carrier, V4 Step 4, and the first carrier is a robust peak; specials are strict
non-peaks).  For 0 < s <= Phi_{l_1} pick i with Phi_{l_{i+1}} <= s <= Phi_{l_i} (Phi_{l_i} -> 0); then gap_{l_i} = M g_i < Phi_{l_{i+1}} <= s, so
the strict non-peak l_i contributes min(Phi_{l_i}, s) = s to Scr(s) (Definition def:SC), whence Scr(Upsilon s)/s >= 1 for every
Upsilon >= 1 and (SC) fails.  (e): fix a clean w of a large level l and its closed pattern kappa.  All carriers are exactly swallowed,
so every coarse carrier is of class G (room 0) and there is no class-R carrier; the coarse peaks are the non-special carriers <= l
(swallowing type, relative positions >= 1 + u for large l), the coarse G strict non-peaks are l_- (anti-type, robust) and the
special l_i <= l (swallowing type, near-threshold or robust).  Hence there is no UPPER source ((U1), (U2) fail; (U3) fails because of
l_-) and there is a LOWER source (L2): I_sh = I_up = {1}.  Take delta := 1, tau_c := lambda_c for every coarse G-carrier c other than l_-,
and tau_{l_-} := (1 + sum_{c != l_-} q_c lambda_c)/|q_{l_-}| > 0 (all q_c > 0 for swallowing-type carriers).  (R1): tau >= 0.  (R2): at a
swallowing-type peak eps vs = +1, tau_c = lambda_c delta.  (R4): delta + sum q tau = 1 + sum_{c != l_-} q_c lambda_c - (1 + sum ...) = 0.
(R5) void, (R6): delta >= 0 (lower source only), (R7) void (no anti-type near-threshold carrier).  (R3): V(tau) = sum_{c coarse,
c != l_-} lambda_c eps_c u_c 1_{F^c} + tau_{l_-} v_{l_-}; every coordinate j in T(l) \ F is owned by a coarse carrier o (the first
carrier touching j is <= the carrier whose target contains j); if o != l_-, its term lambda_o eps_o u_o(j) has the sign z_j (owner
rule for non-special o; for special o, z = eps_o on S_o and eps_o sgn y_o on its unassigned coordinates by construction) and
dominates the later coarse terms, whose coefficients are lambda_c with c > o and which never include l_- (supp u_{l_-} = F ∪ S_{l_-}),
by the dominance estimate of V4 Theorem 2.2 Step 6 (moduli only; it uses (SF*) and allowedness (b)); if o = l_-, j in S_{l_-}, the
term tau_{l_-} v_{l_-}(j) > 0 = z_j-signed dominates likewise.  So V(tau) is z-signed and non-zero on T(l) \ F: all contact rows hold, and
there are no free rows.  The violation is 0 with ||delta||_1 = 1, so rho^sh = 0.  For V1's c_pi: with delta = 1 and x := (lambda_c)
on Bf(w) ∪ {l_-}-type carriers the vector sum_m delta_m Pi_m + sum x eps u is supported on coordinates owned by coarse carriers (a
coordinate owned by a fine carrier is touched by no coarse carrier) and z-signed there by the same dominance: c(1; pi) = 0.  QED
Remarks.  (1) The special carriers are needed only to break (BT) and (SC); the coherent resonance comes from the aligned owner
structure and the single q < 0 carrier l_-, exactly as in V4's self-aligned rows.  (2) Every nested choice is finite-dimensional;
the only infinite object is the limit, and all conditions are strict inequalities preserved along the nest.  This is why the
existence part is labelled SKETCH rather than PROVED: the bookkeeping (I1)-(I4) is not written out coordinate by coordinate.
(3) By Corollary FZ (Part 2), every tilting perturbation of a in the fixed-z fibre of f^infty leaves (C*); the rows f^infty are
"isolated" in their fibre in this sense, and the (C*) property is carried by the joint choice (a, z).

## 3.2 Proposition NT-M (explicit coherent-shift mates of f^infty).  PROVED (given Theorem NT (a)-(c)).
Put psi := R^* w.  (i) psi 1_{F^c} is z-signed and non-zero at every coordinate off F ∪ S_{l_-}; on S_{l_-}, z psi < 0.  (ii) For every
finite Omega ⊂ Q containing k_-, every omega^+ supported in Omega, every Dom supported in Omega with Delta := d(Dom) < 0 and
eps_k Dom(k) >= 0 for k in Omega \ {k_-}, Dom(k_-) chosen so that lambda_{l_-}(Dom(k_-) - Delta w(k_-)) > 0, every split
chi : F^c -> [0,1] and every beta supported in F with (beta + chi v 1_{F^c})(zhat) = 0, the pairs
   omega^- := omega^+ + Dom,  v := R^* Dom - Delta psi,  b^+ := chi v 1_{F^c} + beta,  b^- := b^+ - v
are two-piece data (Delta^{data} = Delta < 0) for g := b^+ + R^*(omega^+ - d(omega^+) w).  (iii) c g in C(f^infty) for all small c > 0.
(iv) The profile pi_g(s) = g(s)/psi(s) on S_l (l a non-special carrier) equals -d(omega^+) + chi_s |Delta| exactly; it is
non-constant whenever chi is.
Proof.  (i) Dominance at every coordinate owned by a carrier o != l_- (owner sign or aligned special sign, |w(o)| >= M/2 > 0 since
specials are near-threshold: |w(o)| = M nu/theta >= M(1 - g_o)); on S_{l_-}, w(k_-) < 0 = -z.  (ii) Lemma A of Part 2: off F,
v = R^* Dom - Delta psi; at coordinates owned by k in Omega \ {k_-} the owner coefficient lambda_k (Dom(k) - Delta w(k)) has the sign
eps_k (both terms do: -Delta > 0 and sgn w(k) = eps_k) and dominates; on S_{l_-} the coefficient lambda_{l_-}(Dom(k_-) - Delta w(k_-)) > 0
= z; elsewhere v = -Delta psi is z-signed by (i).  So v is z-signed off F, b^+ is z-signed, b^- = (chi - 1) v 1_{F^c} + (beta - v 1_F) is
(-z)-signed, both vanish nowhere required (no free coordinates); b^+ - b^- = v = R^*(omega^- - omega^+) - Delta psi, so both pairs
represent g; g(xi) = q_0 b^+(zhat) = 0 by the choice of beta (Lemma lem:algebra for the block parts).  (iii) Proposition
prop:onesidedupper on both sides gives p*(f + r g) <= 1 + (r^2/2)(kappa_w + 1) for |r| <= r_0(g); for |rc| >= r_0 use p*(f + rcg) <=
1 + |r| c p*(g) and s(r) - 1 >= min(r^2, |r|)/3 (V4 Proposition 3.2(iv)).  (iv) At s in S_l, l non-special, s notin Sigma(omega):
g(s) = chi_s v(s) - d(omega^+) psi(s) and v(s) = -Delta psi(s).  QED

## 3.3 Corollary NT-R (the exact-data mates of f^infty are recovered).  PROVED modulo V4 Theorem 5.6 (refereed) and the design
## assumption.
Every mate of f^infty carrying two-piece data with kappa_w <= 1, Delta < 0, omega-carriers Omega as in 3.2 and V4's coefficients gamma_k := lambda_k (Dom(k) - Delta w(k)) != 0 on Omega
is in cl NA((c_0, p_1), l_2^2) jointly with f^infty; in particular all mates of 3.2(iii).
Proof.  V4 Theorem 5.6 (N = 1: Delta d < 0 in every block).  (H1): no carrier is neutral (|w(k)| >= min(M rho_{l_-}, M/2) > 0 for every
k; peaks |w| = M); a carrier k notin Omega is negligible iff |gamma_k| = lambda_k |Delta| |w(k)| < 2 tau_k C_1 lambda_k = 2 tau_k |Delta| lambda_k,
i.e. |w(k)| < 2 tau_k, which happens for at most finitely many k since tau_k -> 0 and |w(k)| is bounded below.  (H2): E = ⋃_{k in Omega}
supp y_k \ F is finite; on the coordinates of E' owned by Omega-carriers the owner coefficient is non-zero (3.2(ii): Dom(k) and -Delta w(k) have
the same sign, so |Dom(k) - Delta w(k)| >= |Dom(k)|) and dominates (Lemma 4.1' of V4 with the design thresholds), so D(j) != 0
there; on E itself D(j) = v(j) != 0 unless an exact cancellation occurs, which is removed by an arbitrarily small change of Dom (finitely
many linear conditions).  V4 Lemma R10 (maximal contact) is satisfied.  QED
So the dangerous explicit mates of the non-(BT) (C*) rows f^infty — oscillating profiles on robust class-G peak signature sets, forced
shift Delta < 0, no (SC) at f^infty — are recovered, through V4's (BT) companions (fine re-alignment + bank levers), not through windows.

## 3.4 The general mate of f^infty.  SKETCH (route complete in outline; one assembly step not written line by line).
Let g in C(f^infty) be arbitrary and rho < 1.  The window machinery applies with one change: in case (II) the transplant does not
need a Hoffman projection onto a shifted cone, because Lemma A + 3.2(ii) show that at f^infty EVERY coarse switching pattern obeying the
sign rows (R1) on Omega and every Delta <= 0 is realized by exact two-piece data, with omega-carriers = the coarse strict non-peaks used.
Steps.  (1) Window certificate with shift: at a scale t of a clean sub-window w, a two-sided decomposition (B_+-, Theta_+-) of g gives
omega_+- (clamped on coarse strict non-peaks with gap >= t^2, Definition def:windowcert), Delta := d(omega^-) - d(omega^+) (equal to
-(d_+ - d_-) + O(t/sigma), Lemma lem:suplevel(d)), and v := R^*(omega^- - omega^+) - Delta psi.  The lower source (L2) gives
Delta d^{dec} M >= -K t (V1 Lemma 3.4'), so Delta <= C K t; replace Delta by min(Delta, 0) through Dom(k_-) (cost O(K t)).  The (R1)
defects ((tau)_- <= K_g t on G strict non-peaks, Y1 Lemma 3.2) are removed by moving Dom on Omega by O(K t / lambda) (cost O(K t) in
l_1).  Coarse near-threshold carriers pushed beyond their gaps are handled as in V1's Proposition TR (kind [3], inward moves need no gap:
Z3 Lemma 5.1, Y2 Lemma U'(ii)).  DEAD ZONES (an Omega-carrier whose coefficient Dom(k) - Delta w(k) vanishes) are removed by the BUMP of
Lemma 3.5 below.  The split chi is read off ΔB by Lemma lem:split.  This yields exact data at f^infty for g_t with ||g - g_t||_1 <= K_w t,
K_w = Design u^{-O(1)} C_f (as in Proposition windowcert(c), plus the shift column, whose coefficient is controlled by Lemma 3.1 of V2).
(2) Average the data over the dyadic scales of w (exactness and Delta <= 0 are preserved; kappa_w is convex).  (3) Transplant the
averaged data to V4's (BT) companion f_w := (f^{(L)})^#(mu) (fine re-alignment beyond L >> l + bank levers; Lemmas 5.4, 5.5 of V4,
whose hypotheses (H1), (H2) hold as in 3.3), with p*(f_w - f^infty) <= C_f sum_{l' > L} lambda_{l'} log = o(T_lo(w)^2).  (4) f_w is (BT), so
(SC) holds at f_w; Theorem E^SC of V2 (Z3 Theorem E with Delta d < 0 data and (SC) at the companions) gives (f^infty, rho g) in cl NA.
What is not written out: the window arithmetic of step (1) with the shift column (the constants K_w), which is V1's Proposition TR
with one extra column; nothing new is needed there since no Hoffman constant of a shifted cone enters (exact data exist for every
sign-admissible pattern).  Hence: f^infty in Rec (SKETCH).  In the language of Part 4: for f^infty step (S1) holds (N = 1 and l_- has
its target on F, so its column is a free ray of the zero-cost cone), and only step (S2) — the uniform composition (S2a)-(S2d) of Part 4.3' (Lemma VT itself is PROVED at a single stage, Part 4.2) — is
unwritten.

## 3.5 Lemma (dead-zone bump).  PROVED (any SLD-type design with allowedness (b); one block; F finite).
Let (b^+-, omega^+-) be two-piece data at f, k in Omega a strict non-peak with S_k ∩ F = {} and exactly swallowed signature (z = eps_k
on S_k), and suppose the coefficient c_k := lambda_k (Dom(k) - Delta w(k)) of u_k in v vanishes.  For kappa > 0 replace Dom(k) by
Dom(k) + eps_k kappa (and omega^-(k) accordingly), keep side +, re-split chi on supp u_k.  Then the new pairs are two-piece data for a
functional g' with ||g' - g||_1 <= 2 lambda_k kappa (1 + |d-change| C), Delta changes by eps_k kappa Phi_k^2 w(k)/C, and on S_k the new v is
z-signed and non-zero as soon as kappa lambda_k v_k(s) exceeds the modulus of the later-carrier terms at s, which by allowedness (b) holds
for all s in S_k once kappa >= kappa_k := C_data 2^{m + k_k - min S_k} (C_data a bound for the data coefficients of later carriers).
Proof.  Direct: v_new = v + eps_k kappa lambda_k u_k - (Delta_new - Delta) psi; on S_k the term eps_k kappa lambda_k v_k(s) has the sign z_s
and, against the later terms (at most C_data 2^{-2s} c_k delta_k by allowedness (b)) and the psi-correction (of size |Delta_new - Delta|
|psi(s)| = O(kappa Phi_k^2) lambda_k v_k(s)), dominates under the stated bound.  The functional changes only through the re-split on
supp u_k and the d-change.  QED
Since kappa_k is super-exponentially small in min S_k, dead zones on the signature sets of omega-carriers cost nothing.  Dead zones
at coordinates owned by a PEAK of a block with Delta_m = 0 cannot be bumped (peaks carry no omega): this is the multi-block residual of
Part 4.

## 3.6 Remark (N >= 2).
Take the construction in block 1 and owner-aligned blocks 2..N without exceptional carriers.  Blocks 2..N then have an UPPER source
((U3) is vacuous: no q < 0 carrier) and a LOWER source (L2), so I_sh = {1}, and (e) holds with delta_m = 0 for m >= 2 — but now every
coordinate owned by a carrier of blocks 2..N is a DEAD ZONE for the block-1 shift (Lemma A with W_Delta = Delta_1 psi_1): the
block-1 resonance is z-signed there only if the later block-1 terms are coherent with z, which the construction does not ensure.  If
they are coherent (choose the block-1 targets hitting block-2 signature sets with the right signs — a condition on the row, not the
design), (e) holds; whether all mates are then recovered is exactly the multi-block dead-zone question of Part 4.
# U3 part 4 — Recovery of (C*) rows: quadratic banks, violation tolerance, and the precise remaining steps

Setting: D^{V2} on D_Omega with diagonal U (+ V4's (SF*), (SF_tau), (b'), (Z0) where cited), finite I, F finite, g in C(f), rho < 1.
"Exact data" = two-piece data of Definition def:twopiece.  A VIOLATION of a pair (b, omega) at a coordinate j notin F is the amount
by which side admissibility fails there: viol^+(j) := |b(j)| if j is free, := (z_j b(j))_- if j is a contact (side +; symmetric for
side -).  ||viol|| := sum_j (viol^+(j) + viol^-(j)).

## 4.1 Lemma QB2 (a bank turns a linear violation into a quadratic cost).  PROVED (any admissible T).
Let f have F finite, let E be a finite set of contacts, and let f^b be the row with forced data (a^b, z) where
a^b := (a + sum_{j in E} m_j z_j e_j^*)/q*(a + sum_{j in E} m_j z_j e_j^*), m_j > 0 (z unchanged; z_j = sgn a^b_j on E, so the data
(a^b, z) are admissible, Remark rem:lemmaZ(c)).  Then F^b = F ∪ E and, for every B in l_1 and t in R,
     Exc^b(t B) <= Exc^{b,0}(t B) + sum_{j in E} t^2 B_j^2 / (2 |a^b_j|),
where Exc^{b,0} is the excess functional of Lemma lem:bookkeeping(b) with the summands at j in E omitted (they are the flip terms).
Pairs (b, omega) that are side-admissible off E and ARBITRARY on E are two-piece data at f^b (E ⊂ F^b), so Proposition
prop:onesidedupper applies at f^b as stated (as t -> 0 no flip occurs).  The point of the lemma is UNIFORMITY in the bank masses: in
the proofs of Proposition prop:onesidedupper, Lemma U (Z3) and Theorem thm:engineered, the condition "no flip on F" (e.g. (T_1):
rho T_0 (||b^+||_inf + ||b^-||_inf) <= a_min/8) may be imposed on F only, the flip part on E being bounded instead by
(t^2/2) sum_E B_j^2/|a^b_j|; the scale range T_0 is then independent of the masses, and Gamma_w is replaced by
     Gamma^E_w(b, omega) := Gamma_w(b, omega) + q^b_0 sum_{j in E} b_j^2 / |a^b_j| .
Proof.  On F^b the excess summand is 2(-sgn(a^b_j) t B_j - |a^b_j|)_+ (Lemma lem:base); for x >= 0 and m > 0, 2(x - m)_+ <= x^2/(2m)
(the parabola x^2/(2m) - 2(x - m) = (x - 2m)^2/(2m) >= 0), and the summand is 0 when -sgn(a^b_j) t B_j <= 0.  In each of the cited
proofs the flip part of Exc enters only through an upper bound hat G_b for the base excess, and the rebalancing step (Proposition
prop:rebalancing) accepts any upper bound hat G_b.  QED
Quantitative consequence (choice of masses).  Given violations e_j := b(j) (j in E) of total mass epsilon := sum_E |e_j| and a budget
beta > 0 in Gamma, the masses m_j := (q_0 epsilon/beta) |e_j| (times the normalising factor) give q^b_0 sum_E e_j^2/|a^b_j| <= beta(1 + o(1)),
and the companion moves by p*(f^b - f) <= C_f sum_E m_j = C_f q_0 epsilon^2/beta: QUADRATIC in the violation.  Numerical check
(U3_work/vt_check.py, finite N = 1 model, dead-zone contact touched by no carrier, rho = 0.9): the least bank mass that makes
rho g_e a mate is m_min = 1.33e-5, 3.16e-6, 7.50e-7, 1.78e-7 for epsilon = 4e-3, 2e-3, 1e-3, 5e-4, i.e. m_min/epsilon^2 = 0.83, 0.79,
0.75, 0.71 (prediction for kappa_w ~ 0: m_min ~ rho^2 epsilon^2 = 0.81 epsilon^2), and p*(f^b - f) ~ 2 m.

## 4.2 Lemma VT (violation tolerance of the engineered approximants, single stage).  PROVED.
(A line-by-line modification of the proof of Theorem thm:engineered in the note; nothing else is used.)
Setting.  I finite, f in S_{p*} with F finite, rho in (0,1), g in X^* with g(xi) = 0.  Let (b^+, omega^+), (b^-, omega^-) be pairs that
REPRESENT g in the sense of Definition def:twopiece (g = b^+- + sum_m R_m^*(omega^+-_m - d_m(omega^+-_m) w_m), omega^+-_m in c_00,
supp omega^+-_m in Q_m), but are NOT assumed side-admissible.  For j notin F put
   viol(j) := (z_j b^+_j)_- + (z_j b^-_j)_+   if j in K (contact),      viol(j) := |b^+_j| + |b^-_j|   if j notin F u K (free),
and epsilon := sum_{j notin F} viol(j) (<= ||b^+||_1 + ||b^-||_1).  Two-piece data are exactly the case epsilon = 0.  Hypotheses:
 (H1) rho^2 kappa_w < 1, kappa_w := max(Gamma_w(b^+, omega^+), Gamma_w(b^-, omega^-)) (the formula of def:twopiece);
 (H2) I_- := {m : Delta d_m < 0} satisfies (SC) (no assumption if I_- is empty);
 (H3) (theta-exactness at free coordinates of the window) b^+_j + b^-_j = 0, i.e. b^theta_j = 0, at every free coordinate
      j <= N_w with viol(j) > 0 (for instance: at every violated free coordinate).
Statement.  Choose delta, T_1, K_sharp, eta_1, the transfer data and T_0 exactly as in Step 0 of the proof of thm:engineered for the data
(f, b^+-, omega^+-, rho), except that K_sharp is replaced by K_sharp + 1.  Let (N_w, s_1, N'') be a stage of the construction sequence of
that proof which is late in the sense of that proof — i.e. the explicit inequalities used in Steps 1-5 hold at it: (N1)-(N3), persistence
of the transfer data, |lin'_m| <= K_sharp |tau| s_1, hat G_b, hat G_m <= K_sharp tau^2, the bracket bound Gamma_diamond + delta/8, and
(1/2) rho |tau| V_{>N''} + |tau| o(s_1) <= delta tau^2/16 for |tau| > s_1 — and at which (H3) and
     (VT)   2 rho epsilon <= delta s_1 / 16
hold.  Then the engineered approximant f' (Definition def:engineered; norm-attaining) and g' := rho(g'' - c a') of Step 1 satisfy
     p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta)      for 0 < |tau| <= T_0.
Proof.  (1) Where admissibility is used.  Step 0 uses the data only through kappa_w (Gamma_theta <= kappa_w by convexity; (H1)) and
through the finitely many constants listed there; Step 1 and Step 2 use only the two representations (g'' - g -> 0, g'(x-hat') = 0,
the identities beta^+- - beta^theta = +-(1/2)v, v = b^+ - b^- = sum_m R_m^*((omega^-_m - omega^+_m) - Delta d_m w_m)); Step 3 (Blocks)
uses only supp omega^diamond_m in Q_m and the radius conditions; Lemma lem:approxfacts uses b^theta only through the masses
m_j = 4 rho s_1 |b^theta_j| and ||b^theta||_1.  The sign conditions on b^+- enter ONLY the claim of Step 3 (Base),
Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} (and = 0 for diamond = theta).  We replace it by
     Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} + 2 rho |tau| epsilon   (diamond = +-, s_1 < |tau| <= T_0),
     Exc'(tau B^theta) = 0                                                (0 < |tau| <= s_1).                          (*)
(2) Proof of (*).  By Lemma lem:bookkeeping(b) at f', Exc'(B) = sum_j (|a'_j + B_j| - |a'_j| - z'_j B_j); on supp a' the summand is
2(-sgn(a'_j) B_j - |a'_j|)_+, off supp a' it is |B_j| - z'_j B_j.  With B = tau B^diamond = tau rho(beta^diamond - c a'):
 on supp a', a'_j + tau B_j = (1 - tau rho c) a'_j + tau rho beta^diamond_j with 1 - tau rho c >= 1/2, so the summand equals
 2(-x - (1 - tau rho c)|a'_j|)_+ <= 2 (x)_- with x := z'_j tau rho beta^diamond_j.
 * j in F: no flip by (T_1), summand 0 (unchanged).
 * window contact with mass (j in K, j <= N_w, b^theta_j != 0; z'_j = z_j): diamond = theta: |tau rho b^theta_j| <= m_j/4 <= |a'_j|/2,
   summand 0 (for either sign of b^theta_j).  diamond = +: tau > 0, x = tau rho z_j b^+_j, summand <= 2 rho |tau| (z_j b^+_j)_-.
   diamond = -: tau < 0, x = -|tau| rho z_j b^-_j, summand <= 2 rho |tau| (z_j b^-_j)_+.  In both cases <= 2 rho |tau| viol(j).
 * window contact without mass (b^theta_j = 0, so beta^theta_j = 0 and b^+_j = -b^-_j): off supp a'; diamond = theta: 0;
   diamond = +: |tau rho b^+_j| - z_j tau rho b^+_j = 2 rho |tau| (z_j b^+_j)_-; diamond = -: = 2 rho |tau| (z_j b^-_j)_+; <= 2 rho |tau| viol(j).
 * free j <= N_w: off supp a', |z_j| <= 1; diamond = theta: beta^theta_j = b^theta_j = 0 if viol(j) > 0 by (H3), and b^+-_j = 0 if viol(j) = 0;
   summand 0.  diamond = +-: summand <= 2 rho |tau| |b^diamond_j| <= 2 rho |tau| viol(j).
 * contact j in (N_w, N'']: beta^theta_j = 0; beta^+-_j = +-(1/2) v_j, so for diamond = sgn tau, tau beta^diamond_j = (1/2)|tau| v_j and the
   summand is rho |tau| (z_j v_j)_-.  Since z_j v_j = z_j b^+_j - z_j b^-_j >= -(z_j b^+_j)_- - (z_j b^-_j)_+, (z_j v_j)_- <= viol(j).
 * free j > N_w: beta^theta_j = 0; |beta^+-_j| = |v_j|/2 <= viol(j)/2; summand <= 2 rho |tau| |v_j|/2 <= rho |tau| viol(j).
 * contact j > N'': z'_j = 0, summand rho |tau| |v_j|/2 (diamond = +-) and 0 (theta): this is the term (1/2) rho |tau| V_{>N''} (unchanged).
 Summing gives (*).  (Free coordinates are never in supp a' = F u {window contacts with b^theta != 0}.)
(3) Constants.  For |tau| > s_1, (VT) gives 2 rho |tau| epsilon <= delta |tau| s_1/16 <= delta tau^2/16 <= tau^2/32, so the bound
hat G_b <= K_sharp tau^2 of Step 0 holds with K_sharp + 1, and Step 4 (rebalancing, |varepsilon_m| <= 6 K_sharp tau^2, error E <= delta tau^2/8 by
the choice of eta_1 with the new K_sharp and the (T_0) conditions) is unchanged.  K_A (bound for (|q*(A_tau) - 1| + q*(A_tau - a'))/|tau|) is
finite since beta^diamond in l_1; it is chosen before T_0 as in the note.
(4) Step 5.  hat Gamma = c' hat G_b + sum_m sigma'_m hat G_m gains at most c' 2 rho |tau| epsilon <= delta tau^2/16 (c' = 1/p(x-hat') <= 1) in the
+- regimes and nothing in the theta-regime.  Hence, for 0 < |tau| <= T_0,
     p*(f' + tau g') <= 1 + (tau^2/2)(rho^2 kappa_w + delta/8 + delta/8 + delta/8 + delta/4 + delta/8) = 1 + (tau^2/2)(1 - 2 delta + 3 delta/4)
                     <= 1 + (tau^2/2)(1 - delta).   QED
Remarks.  (a) In-window CONTACT violations need no bank when (VT) holds: their cost is the same linear 2 rho |tau| viol(j), paid only
for |tau| > s_1 (in the theta-regime the masses m_j protect every window contact, whatever the sign of b^theta_j).  Banks (Lemma QB2)
are needed only for violations whose mass is NOT <= delta s_1/(32 rho) at an admissible s_1.
(b) Free violations inside the window with b^theta_j != 0 are NOT tolerated: they cost 2 rho |tau| |b^theta_j| for |tau| <= s_1, which is
not O(tau^2); free coordinates cannot carry masses (that would change z'_j from |z_j| < 1 to +-1, an O(1) move of x-hat').  This is the
reason for (H3).
(c) What the lemma does NOT give.  Step 6 (Lemma lem:assembly) needs a pair (f_0, g_0) with g_0 in C(f_0) and p*(f' - f_0) <=
(1 - rho^2) T_0^2/6, p*(g' - rho g_0) <= (1 - rho^2) T_0/6.  A functional with violated data is in general NOT a mate of f (U3_work/
vt_check.py: positive excess at f), so in applications the assembly is made relative to the ORIGINAL pair (f_0, g_0) = (f, g) of the
(C*) row, which needs T_0 (of the violated data at the companion) to be large compared with sqrt(p*(f' - f_0)): a uniformity statement.
Moreover (VT) bounds s_1 from below, while "late" means s_1 below a threshold s_late(data) (Bx_m = o(s_1), (E4) convergence, scrambling):
the lemma is useful iff epsilon <= delta s_late/(32 rho).  Both points belong to (S2), see 4.3 and 4.3'.

## 4.3 Proposition RT* (structure of the shifted transplant in case (II)).  PROVED parts and SKETCH parts as marked.
Let w be a clean sub-window of level l in case (II) (rho^sh(kappa, f) <= b(w), c_pi(w) <= b(w)), I_sh the source-deficient blocks.
 (a) (PROVED, V2 Corollary C1.1(a)) The COMBINATORIAL coherent resonance is EXACT: c^comb_*(kappa) = 0, i.e. there are delta on the sign
     sphere of I_sh and x >= 0 on the class-G strict non-peaks with sum_m delta_m Pi_m + sum x eps u zero-cost on the coarse target
     coordinates T(l) and without sign defect on the natural signature sets.  (If c^comb_* > 0 it is >= delta_sh(l) > C Design(l) b(w)
     and case (I) holds.)
 (b) (PROVED, Lemma A of Part 2 and its multi-block form Lemma S) Exact shifted data exist at a row f' iff, outside the supports of
     the omega-carriers, W_Delta = sum_m Delta_m psi'_m vanishes at the free coordinates and is (-z')-signed at the contacts; the
     functional (split chi, omega^+, base part on F) is otherwise free.
 (c) (SKETCH) At V1's companion f^# of w (exactifications (C1)-(C4), donor raise Lambda = T_lo^3, aligned fine re-alignment beyond a
     level L' >> l, Proposition 5.3 of V4), the conditions of (b) hold on all COARSE coordinates for every shift delta in the exact
     combinatorial cone of (a) (owners of coarse coordinates are coarse; peaks of shifted blocks carry the coefficients of (a); coarse
     strict non-peaks are omega-carriers and are bumped where their coefficient vanishes, Lemma 3.5 of Part 3), EXCEPT for: (i) the
     coupling rows Delta_m = d_m(omega^-_m) - d_m(omega^+_m) (V2's (C*-3)), and (ii) contributions of carriers > l at coarse coordinates
     ("medium" carriers l < c <= L' and "fine" carriers c > L'), whose total l_1-mass is at most C |Delta| sum_{c > l} lambda_c <= C |Delta|
     T_lo(w)^3.
 (d) (PROVED given (c)) All violations caused by carriers c > l (medium carriers touch coarse coordinates only through their finitely
     supported targets — allowedness (a) keeps coarse targets off S_c — but an anti-aligned medium carrier also violates on its own
     infinite signature set S_c; fine carriers c > L' violate anywhere) have total l_1-mass epsilon <= C |Delta| sum_{c > l} lambda_c <=
     C |Delta| T_lo(w)^3 and are summable over coordinates.  Hence for every epsilon' > 0 all but epsilon' of this mass lies on a finite set
     E of contacts (heads of the signature sets carry almost all of their mass: v_c(s) = delta_c 2^{-s}/n_c).  Banks of Lemma QB2 on E with
     total mass <= C epsilon^2/beta <= C (|Delta| T_lo^3)^2/beta = o(T_lo(w)^2) absorb these violations into Gamma^E at an extra cost beta;
     the tail epsilon' is left to Lemma VT.  (By Remark 4.2(a) in-window contact violations may instead be tolerated directly when
     their mass is <= delta s_1/(32 rho).  Free coordinates cannot be banked; violations at FREE coordinates are of fine origin only —
     coarse free rows are exact by (c) — and Lemma VT tolerates them beyond N_w automatically and inside the window under (H3).)
 (e) (SKETCH) With Lemma VT at the banked companion (s_1 chosen in a scrambling gap below Lambda, with 32 rho epsilon'/delta <= s_1 <=
     theta T_lo^2) and the averaging of Z3 Theorem E carried out AT the engineered approximant (4.3'(S2b): pieces at the scales of w;
     bound (A) via the engineered transfer of each piece up to its own radius, bound (B') via closeness to (f, rho g)), one obtains NA
     pairs converging to (f, rho g).  Mixed signs of Delta_m across blocks
     are allowed by Theorem thm:engineered ((SC) is needed only for blocks with Delta_m < 0 and holds at the companion along gap scales).
 (f) (Scale bookkeeping; PROVED arithmetic, assuming the design strengthening (W10): c_{l+1} <= T_lo(l)^{10}, an upper bound on
     weights that every SLD-type design admits by V4 Lemma 2.1's argument — window theorems use weights only through upper bounds.)
     Violations at FREE coordinates cannot be banked; they have total mass <= C |Delta| sum_{c > l} lambda_c <= C |Delta| T_lo(l)^{10}.
     Lemma VT needs s_1 >= 32 rho (that mass)/delta, while the scrambling estimate at the companion needs s_1 below the donor raise
     Lambda = T_lo^3 times the least coarse weight and inside a gap of the weight sequence; both hold for s_1 := T_lo(l)^{8} c_l (say),
     since T_lo(l) <= 2^{-n^w_l} T_hi(l) is super-exponentially smaller than c_l >= T_lo(l-1)^{10}.  Without (W10) (c_{l+1} ~ T_lo^3) the
     two requirements collide (free-coordinate violations ~ Lambda): this is the precise reason why V2's (C*-1) looked like an exactness
     problem; with (W10) it becomes a bookkeeping problem.
Consequently (C*) reduces to two precise steps, both finite-dimensional or local:
 (S1) [coupling exactness] at the companion, the coupling rows Delta_m = d^#_m(omega^-) - d^#_m(omega^+) can be satisfied EXACTLY
      inside the exact combinatorial cone of (a) with a design x u^{-O(1)} Hoffman constant.  For N = 1 (or a single shifted block)
      this holds whenever some class-G strict non-peak k with q_k < 0 of the shifted block has its column x_k eps_k u_k as a free ray of
      the zero-cost cone (its target coordinates in T(l) are contacts dominated by their owners or lie in F) — e.g. V4's l_- with
      target y* on F — because increasing x_k changes sum q x without changing delta (PROVED).  In general it is a single equation per
      shifted block whose coefficients are values; per-carrier exact tuning (Y4-ref Prop. P4 / V1 Lemma TU) of one value per block
      solves it as soon as its derivative is bounded below, a quantity that can be made a rate object of the design (SKETCH).
 (S2) [uniform composition] Lemma VT is now PROVED at a single stage (4.2); what remains is the uniform composition (e), made
      precise in 4.3' as (S2a)-(S2d).
Neither step involves an f-dependent rate beyond those already absorbed by the window recursion (modulo the exponent bookkeeping
(S2c)), and nothing in (C*) obstructs them.

## 4.3' The precise content of (S2).
 (S2a) [Lemma U^eng: uniform per-piece engineered bounds] SKETCH.  For pieces (b^+-_t, omega^+-_t) at scales t obeying the size
      conditions of Z3 Lemma U (t ||b||_1 <= A_0, Gamma_w <= 2, |omega_m(k)| <= 2 gap/t, or <= A_2/t where gap >= gamma_B) and violations
      of mass epsilon_t, the constant T_0 of the proof of thm:engineered (with Lemma VT) can be taken >= c_flat t, with c_flat independent of
      t and of the row along a convergent family of rows with base support F u E (bank coordinates E handled by Lemma QB2, so a_min is
      needed on F only).  Scaling check (PROVED arithmetic): every condition (T_1), (T_0) has the form T_0 X <= Y with X = O(1/t) and Y
      bounded below: |Delta d_m| <= A_2 ||D_m||^2/(t C_m)-type bounds, ||b^+-||_inf <= A_0/t, coordinatewise radius of omega >= t/4 (size
      conditions), K_W ~ ||Omega^diamond|| = O(1/t), and the error terms 6|I|K_sharp K_Y |tau|^3 K_A and 48 K_sharp K_W K_y |tau|^3/(min C/2)
      with K_A, K_W = O(1/t) are <= delta tau^2/32 for |tau| <= c t; K_sharp = O(1) because Gamma_w <= 2 bounds the quadratic terms.
      Not checked line by line: uniformity in t of the data-dependent late-stage thresholds ((E4) has constant K(omega) = O(1/t)).
 (S2b) [Theorem E^eng: averaging at the engineered approximant] SKETCH (given (S2a)).  For a companion f_j and its finitely many
      pieces g_{j,t_i}, take one stage that is late for every piece, with masses m_j := 4 rho s_1 max_i |b^theta_{i,j}| (Lemma
      lem:approxfacts is unchanged with larger masses) and N'' satisfying (N3) for every piece.  Then f'_j is an engineered approximant
      for every piece simultaneously, and g'_j := (1/n) sum_i g'_{j,i} (Step 1 is linear in the data).  The averaging argument of Z3
      Theorem E runs at f'_j: (A^eng) p*(f'_j + tau g'_{j,i}) <= 1 + (tau^2/2)(1 - delta_*) for |tau| <= c_flat t_i (Lemma VT + (S2a));
      (B'') p*(f'_j + tau g'_{j,i}) <= s(rho tau) + p*(f'_j - f) + |tau| p*(g'_{j,i} - rho g) (g in C(f)); scale decoupling
      p*(f'_j - f) <= theta_j (T_j 2^{-n_j})^2.  Conclusion: g'_j in C(f'_j), f'_j norm-attaining, (f'_j, g'_j) -> (f, rho g).  This replaces
      the final non-uniform call of Theorem E to Corollary cor:D1 (which needs exact data) by a single uniform stage.
 (S2c) [threshold comparison] HEURISTIC.  Lemma VT at the companion f^#_w needs epsilon_w <= delta s_late(f^#_w)/(32 rho).  The row-
      dependent part of s_late (Bx_m = o(s_1) and the scrambling estimate) involves sum_k lambda_k |w'_m(k) - w_m(k)|, which is controlled
      by the gaps of the companion at the levels <= L(eta) where the weight tail drops below eta/4 — a FIXED set of levels, so this part
      is uniform in l as the companions converge to f.  The data-dependent part ((E4) with K(omega) ~ 1/(t gap_min(levels <= l)), and the
      convergence of h', H') gives s_late >~ t gap_min(<= l); with t ~ T_lo(w), exactified gaps at companions >= T_lo^{O(1)} (V1 (C1)-(C4))
      and epsilon_w <= C |Delta| T_lo^k under the design strengthening (W_k): c_{l+1} <= T_lo(l)^k, the comparison holds for k large
      enough.  To be checked: the exponents of V1's exactifications against k.
 (S2d) [free violations] SKETCH.  Violated free coordinates beyond N_w are tolerated automatically (symmetric split of the construction);
      inside the window (H3) is needed.  Far free coordinates (j > J) can moreover be CONVERTED into contacts: replacing z_j (|z_j| < 1) by
      +-1 keeps z' in the subdifferential of ||.||_1 at a (j notin supp a), keeps q(z' + Ue) = 1 (as in Lemma lem:approxfacts(a)), and moves
      R_m x-hat by at most 2 t(J) -> 0 (t(J) = sum_k lambda_k ||u_k 1_{(J,inf)}||_1), so the converted rows converge to the companion
      (Proposition prop:continuity); the converted coordinate is admissible on both sides iff b^+(j) b^-(j) <= 0.  OPEN sub-case: coarse
      in-window free coordinates touched by targets of carriers c > l with b^+(j) b^-(j) > 0 (excluded if targets of carriers lie in F u K,
      as for V4's l_-).

## 4.4 What is (and is not) obtained.  Labels.
 (1) PROVED: Lemma S, Corollaries S1, S2, Proposition S3, Theorem NL, Proposition FZ (Parts 1-2); Lemma A; properties (b)-(e) of
     Theorem NT, Proposition NT-M, the dead-zone bump (Part 3); Lemma QB2, Lemma VT (single stage), Lemma R-pin (this part);
     Proposition RT*(a),(b),(d).
 (2) PROVED modulo refereed results: Corollary FZ (Master Theorem III'), Corollary NT-R (V4 Theorem 5.6; design compatibility of V4's
     conditions with D^{V2} assumed, V4-ref F6).
 (3) SKETCH: existence part of Theorem NT; recovery of all mates of f^infty (Part 3.4); Proposition RT*(c),(e); the general form of
     (S1); (S2a), (S2b), (S2d) of 4.3'.  HEURISTIC: (S2c).  PROVED (new): Lemma VT at a single stage (4.2).
 (4) OPEN (precise): (S1) in general (multi-block coupling with value-dependent coefficients, V2's (C*-3)), and the uniform composition
     (S2) = (S2a)-(S2d) of 4.3'.  Assuming them,
     every F-finite (C*) row is in Rec for D^{V2} (with V4's design conditions), i.e. Lemma Z holds for F finite.
 (5) NOT a gap any more (relative to V2-ref's list): (C*-1) exact absorption of fine-peak residues — replaced by quadratic banks (finitely
     many coordinates) + violation tolerance (tail), no Slater condition needed; (C*-2) (SC) at companions — holds along gap scales below
     the donor raise for aligned re-alignments; (C*-4) scale-dependent shift directions — the exact combinatorial cone of (a) contains
     every direction used at the scales of w up to O(K t) (Hoffman projection inside a FIXED cone at the companion), and fine-level
     incoherence for a direction different from the completed ray is a fine-origin violation; (C*-5) joint completion/absorption —
     no completion (Lemma C5) is needed once fine violations are tolerated.  These claims are SKETCH-level (they rest on (S2)).

## 4.4' Lemma R-pin (pinned strict non-peaks bound the shift from above).  PROVED (any admissible T, any f, scale t <= min(t_eta, 1)).
For every block m and every strict non-peak k in Q_m with w_m(k) != 0, the decompositions of Lemma lem:twosided satisfy
     Delta d_m |w_m(k)| <= 3 gap_m(k)/t + |Delta Theta_m(k)|      (decomposition convention Delta d = d_+ - d_-).
Proof.  Lemma lem:suplevel(f) with varsigma := sgn w_m(k): varsigma omega_+(k) <= (1 - d_+ t) gap/t and varsigma omega_-(k) >= -(1 + d_- t)
gap/t; with |d_+- t| <= 1/2 this gives varsigma (omega_+ - omega_-)(k) <= 3 gap/t.  Since Theta_+- = omega_+- - d_+- w,
omega_+ - omega_- = Delta Theta + Delta d w, so varsigma(omega_+ - omega_-)(k) = varsigma Delta Theta(k) + Delta d |w(k)|.  QED
Consequences.  (i) A class-R strict non-peak (|Delta theta_k| = lambda_k |Delta Theta(k)| <= K_g t, Y1 Lemma 3.1) with gap <= t^2 pins the
upward shift: Delta d |w(k)| <= 3 t + K_g t/lambda_k — it is an UPPER source not listed among Y1's (U1)-(U3) (adding it only enlarges case
(I)).  (ii) [configuration (i), upward shift Delta d^{dec} > 0] In the transplant of 4.3(c), a coarse class-R strict non-peak k of a
shifted block is an omega-carrier with net coefficient 0 (Dom(k) = Delta^{data} w(k)); by the lemma either the shift is O(K t) at the scale
t (then the d-neutral machinery of V1/V2 applies) or |Dom(k)| ~ |Delta d^{dec}||w(k)| <= 3 gap/t + K_g t/lambda_k, which is within the
size conditions of Z3 Lemma U up to a constant factor.  [Configuration (ii) (downward shift): the lemma gives no bound; there the
neutralizing moves are inward (away from the peak level) and are covered by Z3 Lemma 5.1 / Y2 Lemma U'(ii) — SKETCH.]

## 4.5 Remarks on scepticism.
 (a) Lemma QB2's quadratic cost is the key quantitative fact: a violation of mass epsilon costs a companion move of order
     epsilon^2/beta, so fine-origin violations of mass <= T_lo^3 cost o(T_lo^6) — far below the o(T_lo^2) allowed by Theorem E.  Coarse
     violations of size O(K t) (budget errors) would cost K^2 T_hi^2 >> T_lo^2 and are NOT tolerable: coarse exactness (Proposition
     RT*(a) and (S1)) is indispensable.  This matches the structure of all previous rounds (exact data on coarse coordinates).
 (b) Theorem NL shows that the choice of approximants is essential; every approximant used above is ALIGNED (V4's hysteretic
     re-alignment, banks of the contact's own sign), as Proposition S3 requires.
 (c) Finite SOCP models cannot exhibit failure of recovery (finite truncations are block-tame); they confirm Proposition S3 / Theorem NL
     (collapse of the oscillating part of the fibre under a far anti-type flip: max oscillation 0.0160 -> 2.4e-8 while p*(f_n - f) = 8.3e-7)
     and the quadratic bank law of Lemma QB2.
# U3 part 5 — Numerics (finite SOCP models; sanity checks only)

Scripts in r8/U3_work/ (cvxpy 1.9.3 with CLARABEL; double precision).  Finite models are always block-tame, so they cannot show
failure of recovery; they test the EXACT finite-dimensional statements (Lemma S / Proposition S3 / Theorem NL mechanism, Lemma QB2).

Model (nl_check.py): N = 1, m = 1 (lambda = Phi), F = {0, 1} (a > 0), all other coordinates contacts; carriers
 c1: target e_2, signature {3,4,5}, z = +1  (robust swallowing-type peak, val = 0.803);
 c2: target e_6, signature {7,8},  z = -1  (robust swallowing-type peak, val = -0.941);
 lm: target y* = (e_0 - e_1)/q*, signature {9,10}, z = +1; the ratio a_0/a_1 is tuned so that val = -0.002 (anti-type strict non-peak,
     q < 0, nu/theta small);
 o : target y*, signature {11,12} with weight delta = 0.02; z = -1 in f (aligned peak, val = -0.165), z = +1 in f_n (ANTI-TYPE peak,
     val = -0.135).
 Phi = (0.3, 0.1, 0.03, 0.01), signature weights 2^{-(s - s_0) - 1}, diagonal base s_j as in the script.
Results (nl_check2.py):
 * f and f_n have the same peak/non-peak pattern (P = {c1, c2, o}, Q = {lm}); p*(f_n - f) = 8.3e-7.
 * psi = R^* w is z-signed on all signature coordinates of f; at f_n it is anti-aligned on S_o (z psi = -7.5e-5, -3.7e-5).
 * The coherent-shift mate g of f (V4 Prop. 3.2 with chi = 1 at s_1 = 3 and 0 at s_2 = 4): V z-signed off F (min z V = 3e-7 > 0);
   profile pi_g = (2.35e-4, 0, 1.17e-4) on S_c1 (non-constant); p*(f + t g) <= s(t) on the grid |t| in [1e-3, 10] (max excess -5e-7).
 * One-sided coefficients of g (SOCP over side-admissible pairs): at f gamma^+ = 4.1e-9, gamma^- = 8.6e-4 (both finite); at f_n
   gamma^+ = +infinity (INFEASIBLE), gamma^- = 8.6e-4.  So g is not a mate of f_n at any scaling (Theorem thm:onesided at the
   block-tame f_n), as Proposition S3 predicts.
 * Maximum of pi_h(s_1) - pi_h(s_2) over all h carrying two-piece data with kappa_w <= 1: 1.60e-2 at f, 2.4e-8 at f_n (the residual is
   the difference psi_n - psi at s_1, s_2).  The oscillating part of the local fibre collapses under a far anti-type flip of norm 8.3e-7:
   the finite-dimensional shadow of Theorem NL.
 * (nl_check.py, direct grid relaxation of C(f)) — inconclusive: the SOCP over 2 x 46 scales is not accurate enough at |t| <= 1e-3
   (non-monotone values when constraints are added), and the relevant scale of the effect here is ~1e-8; the exact two-piece
   computation above is the reliable test.
Lemma QB2 (vt_check.py): the same model plus a contact j_0 touched by no carrier (a dead zone, psi(j_0) = 0); g := 0.25 x (shift mate),
g_e := g - eps e_{j_0} rebalanced by a multiple of a (so g_e(xi) = 0), rho = 0.9, grid |t| in [1e-5, 10] (97 scales per sign).
 eps      | max_t [p*(f + t rho g_e) - s(t)] | least bank mass m with rho g_e in C_grid(f_m) | m/eps^2 | p*(f_m - f)
 4.0e-3   | +2.0e-5                          | 1.33e-5                                        | 0.83    | 2.7e-5
 2.0e-3   | +4.5e-6                          | 3.16e-6                                        | 0.79    | 6.3e-6
 1.0e-3   | +1.0e-6                          | 7.50e-7                                        | 0.75    | 1.5e-6
 5.0e-4   | +2.4e-7                          | 1.78e-7                                        | 0.71    | 3.5e-7
The violation is fatal at f (positive excess), a bank of mass ~ rho^2 eps^2 (prediction 0.81 eps^2 for kappa_w ~ 0; the mass grid has
ratio 10^{1/8}) repairs it, and the companion moves by ~ 2 m: the quadratic law of Lemma QB2.
Consistency with Lemma VT: at this contact b^+(j_0) = b^-(j_0) = -eps (side + violated, viol(j_0) = eps, b^theta(j_0) = -eps); the engineered
approximant of Lemma VT carries there the window mass 4 rho s_1 |b^theta(j_0)| with s_1 >= 32 rho eps/delta, i.e. >= 128 rho^2 eps^2/delta
(about 2e2 eps^2 here, delta ~ 1/2): the same quadratic law with a non-optimised constant, above the observed least masses (~0.75 eps^2),
as it must be (Lemma VT is a sufficient condition).
