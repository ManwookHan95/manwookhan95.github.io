# Y4 notes (Round 6): "exactness vs scale" — diagonal first rows, tuning channels, and the directional residual

Setting and notation: paper/martin_density_note.tex (Sections 1, 7, 8) and the refereed Round-5 reports (Z3 Theorem E,
Lemma U, Lemma 3.1, Proposition T with the Z3-referee fixes and the explosive design (D1^F); Z4 Theorem A with (H2'');
Z6-referee design D''' and Theorem U'; Z6 2.4, Conjecture G).  Finite block set I = {1..N}, p = p_N, F = supp a finite
unless said otherwise.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Part files: Y4_part1.md (task (a)),
Y4_part2.md (task (b)), Y4_part3.md (task (c)); scripts in Y4_work/.  No counterexample is claimed; nothing found points to
one.  Lemma Z and density remain OPEN for every admissible T.

## 0. Summary

**(a) Can a diagonal first row beat every window?**
* Explosive design (Z3_ref (D1^F)) with the Cantor pairing as ladder bijection: NO through PER-CARRIER rates.  For any
  first row and any values of R per-carrier rate types (rooms, target rooms, threshold distances = relative margins/gaps,
  relative d-coefficients), at most R N((2L)^{1/2} + 1) windows in [1,L] are blocked (Proposition 1.2, PROVED).
* JOINT rate objects (d-sums of zero-cost rays in MIXED blocks; Farkas/Hoffman data of finite systems) are exponentially
  many per level and the counting fails (Observation 1.3).  In one-signed blocks ray d-sums are dominated by per-carrier
  rates (PROVED).  Whether a diagonal row can block every window of (D1^F) through ray d-sums is OPEN (HEURISTIC: plausible;
  a nested intervals construction in the |F| - 1 base parameters is the natural attempt).
* Pigeonhole design D^PW (Definition 1.4): every level l has M(l) = omega(l) + 1 sub-windows with globally disjoint
  bands, omega(l) a design bound for the number of rate objects of level <= l.  D^PW is admissible, N-free, and every
  window theorem of the note and of Round 5 survives (Lemma 1.5, PROVED).  Every first row has, at EVERY level, a clean
  sub-window at which every rate object is robust (>= u) or tiny (<= b), with robust products absorbed and tiny objects
  exactifiable at cost theta T_lo^2, theta -> 0 (Theorem 1.6, Corollary 1.7, PROVED).  So no first row can beat every
  window through rates: the BAND obstruction and item (r) are design artifacts — modulo the exactification of the tiny
  objects, which is where the real difficulty moves (below).
* d-rows are controlled by ray rates without any compensator: removal of a fraction of the rays of the sign of the
  mismatch costs |mismatch|/D_min (Lemma 1.8, PROVED; single-block rays; multi-block rays need joint objects, OPEN (m')).
* Diagonal candidates: mixed blocks with "ray modules" switching through rays of tiny d-sum; not recovered by any proved
  mechanism for (D1^F); for D^PW they reduce to the directional residual (UN+) below (1.6, HEURISTIC description).

**(b) Non-window tools.**
* Tuned rows (banked companions): masses at contacts, changes of a on F, z-moves at free coordinates; cost
  C_f mu log(e/mu) (Lemma 2.2); Z3 Lemma U and Theorem E hold with banked (growing) support for contact-like data (Lemma
  2.3) — this removes the |F| - 1 limitation of Z3 4.3(iii); channels are jointly injective on Y (Lemma 2.4) with
  design-constant conditioning (Lemma 2.5); the RAISING LEMMA (Lemma 2.6): adding mW to a raises W(zhat) at the rate
  ||P^perp U^*W||^2/nu for every z-signed W; exact tuning under a cone condition (Proposition 2.7).  All PROVED.
* DIRECTIONAL OBSTRUCTION (Proposition 2.8, PROVED): masses at contacts can always raise a z-signed functional; with a
  diagonal base they can never lower it to first order, so lowering is limited to the |F| - 1 two-sided channels on F (and
  one global second-order rescaling, Remark 2.8').  Generic bases do have first-order lowering channels (numerics N1).
* Anti-sign threshold lemma (Lemma 2.9, PROVED): swallowed q < 0 strict non-peaks of tiny gap are pinned like anti-sign
  peaks; the gap rate gamma_B is harmless in both regimes.
* Consequently exactification has a favourable direction (close rooms and target rooms; raise negative tiny d-sums; drop
  anti-sign threshold carriers; raise thresholds — Y2's donors) and an unfavourable one: LOWER a tiny POSITIVE d-sum.
  The sharp residual is
     (UN+) a block whose zero-cost cone has no robust ray of negative d-sum, while the mate switches persistently through
           rays of tiny positive d-sum (nearly neutral, positively d-coupled directions),
  which is Z6's K_nn and the nearly-neutral part of Y2's face Farkas rate K_F^rel, now identified as a DIRECTION problem.
* Non-window viewpoints: convexity of {h : (h, rho g) contractive} (PROVED, not usable directly because the forced-data map
  is not affine); locality (PROVED: Lemma Z is local at f' on the scales |r| <~ p*(f' - f)^{1/2}); Baire (nothing new);
  multi-level companions need no compatibility between levels (Theorem E builds the approximants directly).

**(c) Numerics.**  N1: diagonal bases never lower (0 of 300 x 38 contacts), mixing/random bases lower at ~half of the
contacts; raising derivative confirmed to 2e-8.  N2: lower semicontinuity along tuned rows is trivial in finite models
(dist ~ 7e-4 x cost), as expected (degenerate).  N3: in a finite (UN+) model the forced switching through a ray of tiny
positive d-sum is a transient band of height ~1.4e-2 t that does NOT grow as the d-sum decreases over three decades
(1.54e-2, 1.45e-2, 1.38e-2, 1.37e-2): evidence for a RAY version of Z6's Conjecture G, i.e. that (UN+) is an artifact of
the 1/D pinning bound rather than of the geometry (HEURISTIC).

**Bottom line.**  The "exactness vs scale" obstruction is NOT intrinsic as a RATE phenomenon: a pigeonhole window design
gives every first row clean sub-windows at every level.  What remains for the companion/window route is DIRECTIONAL:
exactification sometimes requires lowering z-signed functionals, which cheap moves cannot do (diagonal bases), and the
corresponding mates must then be shown to need no switching through those directions (Conjecture G_ray).

**Precise remaining step.**  Prove Conjecture G_ray: in a block whose zero-cost cone at level l (of a clean sub-window) has
no robust ray of negative d-sum, at every scale t of the sub-window some two-sided decomposition of g switches through the
rays of tiny positive d-sum by at most C Design(l) t.  Together with Theorem 1.6, Parts 1-2, Y2 (donors, Theorems P, M, H)
and Round 5 (Theorem E, Proposition T, Theorems A'', U') this would leave only the assembly (SKETCH), the aligned corner and
the coherent shift resonance of Y2, multi-block rays (m'), and (O4) infinite F.  Alternative route: a mixing base with
lowering channels of design-bounded conditioning (transversality; OPEN).

# Y4 part 1 — Can a diagonal first row beat every window?  Rate objects, the explosive design, pigeonhole sub-windows

Setting: note paper/martin_density_note.tex (Sections 1, 7, 8), finite block set I = {1..N}, p = p_N, F finite unless said
otherwise.  Round-5 notation: rooms r_l (sign-mixed, Def. def:R0pm), slaved rooms r*_l (Def. def:swallowed), q_l :=
eps_l Phi_{m(l)}(k(l)) w_{m(l)}(k(l))/(m(l) C_{m(l)}) (d-weight of carrier l), margins mu_l, gaps, windows W(l) =
[T_lo(l), T_hi(l)] with n^w_l dyadic scales; explosive design (D1^F) of Z3_ref_notes part 4 (bands Band(l) = (b(l), u(l))
pairwise disjoint); design D''' of Z6_ref_notes 3.3.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.0 What a "window method" needs, abstractly
Every recovery theorem of Section 8 and Round 5 (Theorems thm:R0, thm:Bstar, thm:Bpm, thm:S; Z3 Thm E + Prop T + Cor 3.4;
Z4 Thm A; Z6 Thms C, U', V) has the same skeleton at a window W = [T_lo, T_hi] with n = log_2(T_hi/T_lo) dyadic scales:
 (W-pin) the coarse carriers that are NOT treated exactly are pinned: the window decompositions are within K t of exact
         d-neutral two-piece data, with K = (f-constant) x (design factor) x prod/sum of RECIPROCAL RATES of the pinned
         objects; one needs K T_hi -> 0 and n/K -> infinity along the windows used;
 (W-ex)  the remaining coarse objects are treated EXACTLY, either at f itself or (Z3 Thm E) at a companion f^# with
         p*(f^# - f) <= theta T_lo^2, theta -> 0; the cost of exactifying an object of rate rho is (design) x rho
         (Z3 Lemma 3.1: unweighted, sharp).
A "rate" is an f-dependent number in [0, infinity] attached to a finitely-described object.  The consensus core (r) of
ADDENDUM 5 is the possibility that, at EVERY window, some object has its rate in the band
    T_lo^2 x (design)  <<  rho  <<  1/(n x design),                                                       (Band)
so that it can be neither pinned nor exactified.

**Definition 1.1 (rate objects).**  A *rate scheme* for a design is a sequence of finite sets O(l) (l >= 1), each element
described by finitely many design data of ladder index <= l (e.g. a carrier l' <= l, a target coordinate of a carrier
<= l, a zero-cost ray of a combinatorial cone built from carriers <= l, a finite subsystem), N-free, together with rate
functionals rho_O : {f in S_{p*} : F finite} -> [0, infinity].  Put O_<=(l) := union_{l' <= l} O(l').  The scheme is
*design-countable* if there is a design-computable integer omega(l) >= |O_<=(l)| (computable at stage l of the
recursion).  An object O blocks a window (or sub-window) w of level >= l(O) at f if rho_O(f) lies in Band(w).

The concrete rate types of the open core (r) (Z6_ref_notes 7; Z4_referee; Z3_ref_notes) are all design-countable:
 (R1) rooms: O = (l), rho = r_l/delta°_l; slaved rooms O = (l, A), A a subset of (l, l_*] (later bad/exactified carriers),
      rho = r*_l(A)/delta°_l  [count <= l_* 2^{l_*}];
 (R2) target rooms gamma_T: O = (s), s a target coordinate of a carrier <= l, rho = 1 - |z_s|;
 (R3) threshold distances: O = (l), rho = | |u_l(zhat)| - vartheta_{m(l)} Phi_l | / Phi_l (covers relative margins of
      peaks and relative gaps of strict non-peaks; the threshold constant vartheta_m is a block quantity);
 (R4) relative d-coefficients: O = (l), rho = |q_l|/Phi_l (K_nn of Z6);
 (R5) ray d-sums: O = (pattern P, extreme ray r of the combinatorial zero-cost cone C_P of Lemma lem:exactswitch /
      Z6 5.2 built from carriers <= l), rho = |sum_l q_l r(l)| / max_{l in supp r} Phi_l, rays normalized ||r||_1 = 1
      [the number of patterns and rays at level l is a design-computable bound];
 (R6) joint d-objects for multi-block rays: O = (P, S), S a set of at most N rays of C_P, rho = smallest singular value
      of the N x |S| matrix of their d-vectors (normalized as in R5).
(R1)-(R4) are PER-CARRIER (at most a fixed number R of objects per carrier, plus finitely many coordinates); (R5)-(R6) are
JOINT objects, whose number per level is design-bounded but in general much larger than l.

## 1.2 The explosive design is immune to per-carrier diagonalization

**Proposition 1.2.** PROVED.  Let the design be (D1^F) of Z3_ref_notes 4.1 with the ladder bijection j chosen as the
Cantor pairing j(k,m) := (k+m-1)(k+m-2)/2 + m (it satisfies (D0): j(k,m) < j(k',m) for k < k').  Let R >= 1 and suppose
that for each type i <= R the bands Band_i(l) = (b_i(l), u_i(l)) of the windows are pairwise disjoint in l (for
(D1^F) one may take the same bands for all types).  For ANY first row f and ANY numbers rho_{l,i}(f) in [0, infinity]
(l in L_N, i <= R), call the window l_* blocked if rho_{l,i}(f) in Band_i(l_*) for some i and some l in L_N, l <= l_*.
Then at most R |L_N cap [1,L]| <= R N (2L)^{1/2} + RN windows in [1,L] are blocked; in particular infinitely many windows
are unblocked, for every f.
*Proof.* Fix i.  By disjointness, each number rho_{l,i}(f) lies in at most one Band_i(l_*); choosing for each blocked window
one blocking pair (l,i) with l <= l_* gives a map from blocked windows in [1,L] into (L_N cap [1,L]) x {1..R} which is
injective on each fibre of i.  For the Cantor pairing, j(k,m) <= L forces k + m - 2 <= (2L)^{1/2}, so for each m <= N
there are at most (2L)^{1/2} + 1 such k.  Hence the bound, and L - RN((2L)^{1/2} + 1) -> infinity.  QED
*Remark.* For a general bijection j with (D0), L_N may have positive density; then the conclusion holds for R = 1 only
(Z3_ref Prop 4.2.1: unblocked windows >= |[1,L] \ L_N|).  The choice of j is a design choice, so Proposition 1.2 is
available.  Consequently: **a diagonal first row cannot beat every window of the explosive design through per-carrier
rates of finitely many types (R1)-(R4)**, whatever their values (rooms, margins, gaps, d-coefficients, target rooms).

## 1.3 Joint objects: the counting fails for the explosive design
**Observation 1.3.** PROVED (counting) / HEURISTIC (consequence).  The number of ray objects (R5) at level l is in
general exponential in l (an m-variable cone with P rows can have up to binom(P, m-1) extreme rays), so the injection of
Prop. 1.2 gives no unblocked window when blocking objects are rays.  A diagonal first row would need, at every window l_*,
a zero-cost ray r of carriers <= l_* whose normalized d-sum lies in Band(l_*).  In a ONE-SIGNED block (all q_l of one
sign) this is impossible beyond per-carrier rates: since rays are nonnegative (tau >= 0 is a row of every zero-cost cone),
|sum q_l r(l)| >= min{|q_l| : l in supp r, q_l != 0} x sum_{q_l != 0} r(l), and for an extreme ray which is not
exactly neutral the last sum is >= the least nonzero coordinate of the normalized extreme rays of level l (a design
constant); i.e. (R5) is dominated by (R4) up to a design factor (PROVED).  In a MIXED block (q of both
signs among carriers combined by the combinatorial rows, e.g. a q < 0 carrier whose vector is z-signed only together with a
q > 0 carrier sharing a target coordinate) cancellation inside a ray makes its d-sum an independent rate.  A nested
(Baire/intermediate-value) construction in the finitely many parameters a in l_1(F) (|F| >= 2 at maximal contact; z off
F is frozen there) would place, window after window, the zero of some new ray's d-sum close to the current parameter;
whether this can be continued at EVERY window of (D1^F) depends on how densely the zeros of the rays of level l_* fill
intervals of length ~u(l_*-1); I did not settle this (HEURISTIC: plausible for suitable targets, not excluded by (D1^F)).
So the explosive design is not shown immune to joint rates; the fix below is immune by construction.

## 1.4 The pigeonhole multi-window design D^PW

**Definition 1.4 (D^PW).**  Start from D''' (Z6_ref_notes 3.3): (D0) (with the Cantor pairing), allowedness,
y_l, n_l, u_l, delta°_l, Lambda°(l), and the design factor Design(l) := l 2^{l^3} Lambda°(l) Xi'(l) of D''' (it contains
the combinatorial Hoffman constants H_comb(l), Z4's G*(l), D(l) = 1 + sum_{l'' <= l}(1/m^nat_{l''}(l) + 1/Phi_{l''}),
all maximized over all subsets of [1,l], hence N-free).  Fix any design-countable rate scheme with bound omega(l) (for
instance the scheme (R1)-(R6), counted over all patterns of level <= l), and put M(l) := omega(l) + 1.
Order the sub-windows w = (l,i), l >= 1, 1 <= i <= M(l), lexicographically; w^- is the predecessor.  Recursively:
   u(1,1) := 1/2,   u(w) := b(w^-)  (w != (1,1)),
   Q(w) := Design(l) (4/u(w))^{omega(l)},   n(w) := ceil(l 2^{l^3} Q(w)),
   T_hi(w) := min{T_lo(w^-), 2^{-l^3}/(l Q(w))}  (T_lo((1,1)^-) := 1),   T_lo(w) := 2^{-n(w)} T_hi(w),
   b(w) := T_lo(w)^4/(l Design(l)),     c_{l+1} := min{c_l/4, T_lo(l, M(l))^3},
and (D2) as in Definition def:SLD.  Band(w) := (b(w), u(w)).

**Lemma 1.5 (D^PW is admissible and every window theorem survives).**  PROVED.
(a) T is admissible, N-free, and satisfies (P1), (P2) of Theorem thm:SLD; for every sub-window w = (l,i):
    T_hi(w) l Q(w) 2^{l^3} <= 1, n(w) >= l 2^{l^3} Q(w) >= l 2^{l^3} Design(l), T_hi(w^+) <= T_lo(w),
    sum_{l' > l} c_{l'} <= 2 T_lo(w)^3 (box bound for fine carriers at every scale of every level-l sub-window).
(b) The bands Band(w) are nonempty and pairwise disjoint: b(w) < u(w) and u(w^+) = b(w).
(c) Every result proved for D''' (all of Section 8 of the note, Z3 Thm E/Prop T/Cor 3.4, Z4 Thm A, Z6 Thms C, U', V and
    their corollaries) holds for D^PW with "window W(l)" replaced by "sub-window (l,i)" (any i), and the window-growth
    hypotheses (factors C_f^{l^2} x Design(l)-type quantities) are satisfied a fortiori.
*Proof.* (a) Admissibility (Theorem thm:SLD) uses only (D0), allowedness and c_{l+1} <= c_l/4; (P1), (P2) are unchanged;
the inequalities are immediate from the definitions (Q >= Design >= 1).  N-freeness: every ingredient is N-free
(D''' is, and omega(l) counts objects of all blocks).  The box bound: sum_{l'>l} c_{l'} <= 2c_{l+1} <= 2 T_lo(l,M(l))^3
<= 2 T_lo(w)^3 for every i, so Lemma lem:box + (P2) give sum_{l' > l}|Delta theta_{l'}| <= 6 T_lo(w)^3/t <= 6t^2 for
t in w.  (b) b(w) <= T_lo(w)^4 <= 2^{-4n(w)} <= 2^{-4 u(w)^{-1}} < u(w) since u(w) <= 1/2 and Q(w) >= u(w)^{-1}.  The
bands are consecutive open intervals (b(w), u(w)), (b(w^+), b(w)), ..., hence pairwise disjoint.  (c) As in
Z3_ref_notes Lemma 4.1.1 and Z6_ref_notes 3.3: in every window proof the window enters only through (i) the dyadic scales
of one window, (ii) T_hi times an f-dependent factor (<= C_f^{l^2} times products of design quantities already in
Design(l)) -> 0 and n divided by the same factor -> infinity along the windows used, (iii) the box bound for carriers
of index > l, (iv) T_hi(next) <= T_lo(previous).  All four hold for sub-windows by (a), with Q(w) >= Design(l).  QED

**Theorem 1.6 (clean sub-windows; pigeonhole).**  PROVED.  For the design D^PW and every first row f (any F), every
level l and every assignment of rates rho_O(f) in [0, infinity] (O in O_<=(l)), at least M(l) - omega(l) >= 1 of the
sub-windows (l,1), ..., (l,M(l)) are CLEAN: no object of level <= l has its rate in their band.  At a clean sub-window
w = (l,i) every O in O_<=(l) is either ROBUST (rho_O >= u(w)) or TINY (rho_O <= b(w)), and
    prod_{O robust} (1 + 3/rho_O) <= (4/u(w))^{omega(l)} = Q(w)/Design(l)  (1 + 3/rho <= 4/u for rho >= u),   T_lo(w)^2 / b(w) = l Design(l)/T_lo(w)^2.
*Proof.* By Lemma 1.5(b) each number rho_O(f) lies in at most one band, so each object blocks at most one sub-window;
at most |O_<=(l)| <= omega(l) of the M(l) = omega(l) + 1 sub-windows of level l are blocked.  The two displayed
relations are the definitions of Q(w) and b(w).  QED

**Corollary 1.7 (answer to question (a)).**  PROVED (as a statement about rate obstructions).  For the design D^PW,
NO first row can make every window "rate-blocked": at every level l there is a sub-window at which every object of every
design-countable rate scheme is either robust, with pinning products bounded by Q(w)/Design(l) (absorbed: K T_hi(w) <=
C_f^{l^2}/(l 2^{l^3}) -> 0 and n(w)/K >= l 2^{l^3}/C_f^{l^2} -> infinity), or tiny, with exactification cost
C_f Design(l) b(w) = theta T_lo(w)^2, theta := C_f T_lo(w)^2/l -> 0.  Hence the "band" obstruction (Z3 4.3(ii)) and every "super-fast f-dependent rate" of the
consensus core (r) are DESIGN ARTIFACTS, provided the rate in question is attached to a design-countable family of
objects and enters the window method only through "pin if robust / exactify if tiny".
What remains after Corollary 1.7 is NOT a rate question:
 (X1) [simultaneous exactification] all TINY objects of level <= l must be made EXACT (or be shown harmless) at ONE
      companion f^# with p*(f^# - f) <= C_f Design(l) b(w), without destroying exactness of the others (rooms closed,
      d-sums of tiny rays and tiny d-weights made exactly zero, tiny threshold distances pushed to the favourable side),
      with statuses of all robust objects preserved (automatic: the perturbation C_f Design b(w) << u(w)).  Part 2 shows
      that (X1) splits by DIRECTION: closing moves are available (PROVED for single objects, conditional (TC) for families),
      while opening moves (lowering a z-signed functional: tiny POSITIVE d-sums in blocks without a robust negative ray,
      tiny-margin resonant swallowing-type peaks) are impossible with a diagonal base beyond |F| - 1 dimensions (Prop. 2.8
      of part 2).  So Corollary 1.7 removes the rate obstruction except for the directional residual (UN+) of 2.4
      ((P+) is settled by Y2's threshold-raising donors, except Y2's aligned corner);
 (X2) [exact configurations] at the exactified companion, the window theory for EXACT data must apply with
      design-bounded constants: robust rays control the d-row Hoffman constant (Lemma 1.8 below for single-block rays;
      multi-block rays need (R6)); (H2'')-type shift pinning; degenerate peaks only of the harmless kinds (see 2.6);
 (X3) infinite F (O4), outside this part.
The tuning tools for (X1) are the subject of part 2.

## 1.5 d-rows are controlled by ray rates (no compensator needed)

**Lemma 1.8 (ray removal).**  PROVED.  Let C subset R^B_{>= 0} be a polyhedral cone (contained in the nonnegative orthant)
with extreme rays r_1, ..., r_p, ||r_i||_1 = 1, and let D : R^B -> R be linear, D_i := D(r_i).  Put D_min := min{|D_i| :
D_i != 0} (D_min := infinity if all D_i = 0) and Z := C cap ker D.  Then for every tau in C,
    dist_1(tau, Z) <= |D(tau)| / D_min .
*Proof.* Write tau = sum_i mu_i r_i with mu_i >= 0 (Minkowski-Weyl).  Since every r_i >= 0 coordinatewise, ||tau||_1 =
sum_i mu_i (no cancellation).  Say D(tau) = e > 0 (e < 0 is symmetric, e = 0 trivial).  Then S_+ := sum_{D_i > 0} mu_i D_i
>= e > 0.  Put theta := e/S_+ in (0,1] and tau' := tau - theta sum_{D_i > 0} mu_i r_i = sum_{D_i <= 0} mu_i r_i +
(1-theta) sum_{D_i>0} mu_i r_i in C.  Then D(tau') = e - theta S_+ = 0 and ||tau - tau'||_1 = theta sum_{D_i>0} mu_i <=
theta S_+/D_min = e/D_min.  QED
*Use.* For one block (or when every ray of C lives in one block), apply Lemma 1.8 to the combinatorial zero-cost cone C_P
of the companion (after the combinatorial projection, Hoffman constant H_comb = design) and to the d-row D := Q_m.  At a
clean sub-window, after the tiny rays have been neutralized (D_i = 0 exactly, part 2), every non-neutral ray is robust,
D_min >= u(w) min Phi (design), so the d-row costs a factor <= design/u(w): the "f-dependent d-row Hoffman constants"
of item (m) of the open core reduce, for single-block rays, to the rate objects (R5).  No compensator pair (Theorem C) and
no rigidity (Proposition P) is needed: one only REMOVES a fraction of the rays of the sign of the mismatch.
*Limitation.* For N >= 2 and rays involving several blocks the d-row is vector-valued; removal of a sub-combination
nu <= mu with sum nu_i D_i = e may need |nu| ~ |e|/sigma_min(S) for a subset S of rays (objects (R6)), and the
"exactification" of a tiny sigma_min(S) has no obvious meaning.  OPEN (sub-item (m') of the remaining step).

## 1.6 The diagonal candidates and their mates (task (a), second half)
Description (HEURISTIC/SKETCH, consistent with all PROVED facts above).  For the explosive design (D1^F) the only
candidate for a first row beating every window is a row at (or near) maximal contact with |F| >= 2 and a MIXED block
in which, for infinitely many windows, rays of the zero-cost cone have normalized d-sums inside Band(l_*); its mates
include sums of "ray modules" g = sum_i c_i (V_{r_i} - (d-correction) R^*_m w_m) (V_r = sum_l eps_l r(l) u_l), each a
finite certificate (recovered: Theorem thm:transfer) but whose sums switch through the band rays at every window
(cf. Z6 6.2 for one-carrier modules).  Test against the proved mechanisms: windows at f (Thms S, C, U', A): fail (the
band ray is neither pinned within n nor d-neutral); Z3 Thm E + Prop T: fail at the blocked windows (exactification of a
band ray costs >> T_lo^2); engineered approximants (Cor D1): need exact d-neutral data, fail; certificates/averaging:
only module sums with gaps bounded below (Z6 6.3(iii), SKETCH).  For D^PW the same row has clean sub-windows at every
level (Theorem 1.6), and the only remaining requirements are (X1)-(X2).  So no candidate built from rates alone can be a
counterexample for D^PW; a counterexample would have to come from (X1)/(X2)/(X3).

# Y4 part 2 — Tuning channels: banked companions, raising, and the directional obstruction

Any admissible T, I finite, f in S_{p*} with F finite and forced data (xi, q_0, a, w, F, z, zhat, e, nu); K contacts,
J_free := {j notin F : |z_j| < 1}.  P^perp = orthogonal projection of H onto e^perp.  For W in l_1, x in H:
<U^*W, x> = W(Ux).  A vector W in l_1 is *z-signed* if W(j) = 0 for j in J_free and z_j W(j) >= 0 for j in K (no
condition on F).  Every zero-cost switching vector V = sum_l eps_l tau_l u_l (Lemma lem:exactswitch; Z6 5.2) restricted to
F^c is z-signed, and so is every ray vector V_r of a zero-cost cone.  These tools address item (X1) of part 1 and the
re-tuning question of Z3 4.3(iii) / Z3_ref 2.7(iii) (only |F| - 1 degrees of freedom when supp a is frozen).

## 2.1 Banked companions and their cost
**Definition 2.1.**  For a finite set B subset K and m = (m_j)_{j in B}, m_j >= 0, together with a change beta of a on F
(small, signs on F kept) and a z-move zeta supported in J_free (|z_j + zeta_j| < 1), the *tuned row* f^tau is the first
row with forced data (a^tau, z + zeta), a^tau := A/q^*(A), A := a + beta + sum_{j in B} m_j z_j e_j^*.  It is admissible
(Remark rem:lemmaZ(c)): z + zeta = sgn a^tau on supp a^tau = F u {j in B : m_j > 0}.  Then e^tau = U^*A/||U^*A|| and
zhat^tau - zhat = zeta + U(e^tau - e).  If beta = 0 and zeta = 0 we call f^tau a *banked row*.

**Lemma 2.2 (cost).** PROVED.  There are c_f, C_f > 0 (depending only on f, N, T) such that, with mu := ||m||_1 +
||beta||_1 + ||zeta||_1 <= c_f:  ||e^tau - e|| <= C_f(||m||_1 + ||beta||_1),  p*(f^tau - f) <= C_f mu log(e/mu), and
C_m, M_m, sigma_m, q_0, vartheta_m move by at most C_f mu.
*Proof.* ||U^*A - nu e|| <= ||U||(||m||_1 + ||beta||_1) and x -> x/||x|| is 2/nu-Lipschitz near nu e (the factor
1/q^*(A) does not change e^tau).  Put delta := zhat^tau - zhat; then |u_{k,m}(delta)| <= ||zeta||_1 + ||e^tau - e|| for
all k, m (q^*(u) = 1 gives ||u||_inf <= 1, ||U^*u|| <= 1).  The proof of Z3 Lemma 3.1 (cost of a companion) uses only
zhat^# = zhat + delta and the clamp formula of Lemma lem:F1 at both points (block functionals w^tau_m = J_m(R_m^** zhat^tau),
Remark rem:lemmaZ(c)); it applies verbatim and gives sum_m ||R_m^*(w^tau_m - w_m)||_1 <= C_f c(delta), c(delta) =
sum_m[Delta_m log(e/Delta_m) + sum_k min(lambda_{k,m}, |u_{k,m}(delta)|)] <= C mu log(e/mu) by sum_k min(lambda_{k,m}, x)
<= x(log_2(2m/x) + 3).  Finally f^tau - f = (a^tau - a) + L^*(w^tau - w), q^*(a^tau - a) <= C(||m||_1 + ||beta||_1).  QED

**Lemma 2.3 (Lemma U and Theorem E with banked support).** PROVED (by inspection).  Z3 Lemma U and Z3 Theorem E remain
true if "supp a_j = F" is replaced by "supp a_j = F u B_j, B_j a finite set of contacts of f carrying masses at f_j",
provided the data (b^pm, omega^pm) at f_j are CONTACT-LIKE on B_j: z_i b^+_i >= 0 >= z_i b^-_i (i in B_j).
*Proof.* supp a_j = F is used in Lemma U only for the no-flip condition on F (a_{j,min} -> a_min > 0, Lemma
lem:onesidedtransfer, Base).  On B_j, a_j(i) = m_i z_i, and for side-+ data and r > 0, |a_j(i) + r b_i| - |a_j(i)| -
z_i r b_i = (m_i + r|b_i|) - m_i - r|b_i| = 0; for side-- data and r < 0 likewise.  So B_j contributes nothing to the base
excess, exactly like contacts; all other steps (Hilbert part with nu_j -> nu, blocks, persistence of transfer data along
f_j -> f) are unchanged.  In Theorem E, contact-like data on B_j subset F_j are two-piece data at f_j (no condition is
imposed on support coordinates), and Corollary cor:D1 applies at f_j since F u B_j is finite.  QED
*Remark.* In Z3 Proposition T, b^+ = B_+1_F + chi V' - kappa a with V' z-signed: transplanted data are automatically
contact-like on every contact, in particular on any bank.

## 2.2 Channels; injectivity; raising
For W in l_1 put h_W := U P^perp U^* W in c_0 (so ||P^perp U^*W||^2 = W(h_W) = sum_j W(j) h_W(j)).  To first order, a mass
m_j at j in K changes W(zhat) by (m_j/nu) z_j h_W(j); a change beta_j on F by (beta_j/nu) h_W(j) (either sign); a z-move
zeta_j at j in J_free by zeta_j W(j) (either sign, within the room).

**Lemma 2.4 (joint injectivity).** PROVED.  If W in Y = T(l_1(N x N)), h_W(j) = 0 for all j in F u K and W(j) = 0 for all
j in J_free, then W = 0.
*Proof.* ||P^perp U^*W||^2 = sum_j W(j) h_W(j) = 0 (each term has a vanishing factor).  So U^*W is a multiple of
e = U^*a/nu, W = mu a by injectivity of U^*, and W in Y cap c_00 = {0} (T-c), since a in c_00.  QED

**Lemma 2.5 (quantitative injectivity; design constant).** PROVED.  For s >= 1 and a finite-dimensional subspace W of Y
there are J_max(W,s) and gamma(W,s) > 0 depending only on W, s, U such that for EVERY f with F subset [1,s] (any z):
max_{j <= J_max} chan_j(W) >= gamma ||W||_1 for W in W, where chan_j(W) := |h_W(j)| (j in F u K), |W(j)| (j in J_free).
*Proof.* Compactness: kappa^2 := min{||P^perp_{e'}U^*W||^2 : W in W, ||W||_1 = 1, e' = U^*a'/||U^*a'||, a' in l_1(F'),
||a'||_1 = 1, F' subset [1,s]} > 0 (Lemma 2.4's argument for each pair; continuity).  ||h_W||_inf <= ||U||^2, and the
tail eps(J) := max{||W1_{(J,inf)}||_1 : W in W, ||W||_1 = 1} -> 0.  With ||U||^2 eps(J_max) <= kappa^2/2:
kappa^2/2 <= sum_{j <= J_max} W(j)h_W(j) <= max_{j <= J_max} chan_j(W) (1 + J_max ||U||^2).  QED

**Lemma 2.6 (raising lemma).** PROVED.  Let W be z-signed and nonzero.  For small m > 0 the tuned row with base part
a^m proportional to a + m W (masses m W(j) at j in K cap supp W, change m W(j) on F) is admissible (z unchanged), and
   d/dm W(zhat^m) |_{m=0} = ||P^perp U^* W||^2 / nu > 0 .
More generally, for z-signed W_1, ..., W_p the map m in R^p_{>= 0} -> (W_i(zhat^m))_i, a^m prop. to a + sum m_k W_k, has
derivative G/nu, G_{ik} = <P^perp U^*W_i, P^perp U^*W_k> (the Gram matrix, positive definite when the W_i are linearly
independent, by Lemma 2.4).  Every first-order change obtainable from banks at contacts (beta = 0, zeta = 0) is of the
form (sum_j (m_j/nu) z_j h_{W_i}(j))_i, m >= 0.
*Proof.* a + mW has the signs of a on F (m small) and sign z_j at j in K cap supp W; elsewhere it is 0.  de/dm =
P^perp U^* W/nu, and dW(zhat)/dm = <U^*W, de/dm>.  QED

**Proposition 2.7 (exact tuning in a reachable direction).** PROVED.  Let V_1, ..., V_p in Y and let Delta in R^p.  A
*move* is x = (m, beta, zeta) with m >= 0 on a finite set of contacts, beta on F, zeta on free coordinates; its
first-order effect is Lx := (V_i(d zhat))_i.  Suppose:
  (TC) there are p moves x^(1), ..., x^(p) of l_1-norm 1 (each either a single mass direction e_j, j in K, called
       one-sided, or a two-sided direction on F or J_free) such that the p x p matrix A := [L x^(1), ..., L x^(p)] is
       invertible with ||A^{-1}|| <= Gamma, and s^0 := A^{-1}Delta satisfies s^0_k >= c|Delta| > 0 for every one-sided k.
Then there is C(f) such that if C(f) Gamma^3 |Delta| <= c (and the moves stay inside the rooms of the z-channels used),
there is a tuned row f^tau with V_i(zhat^tau) = V_i(zhat) + Delta_i EXACTLY, a move of l_1-norm <= 2 Gamma |Delta|, and
p*(f^tau - f) <= C_f Gamma |Delta| log(e/(Gamma|Delta|)).
*Proof.* psi(s) := Phi(sum_k s_k x^(k)), s in R^p, where Phi(x) := (V_i(zhat(x)) - V_i(zhat))_i.  psi is C^2 near 0 (masses
and beta enter through e(x) = U^*A(x)/||U^*A(x)||, smooth near nu e; zeta linearly), psi(0) = 0, D psi(0) = A,
|D^2 psi| <= C_2(f).  The map s -> s - A^{-1}(psi(s) - Delta) is a contraction of the ball |s - s^0| <= 2 Gamma^2 C_2
|s^0|^2 into itself when |s^0| <= Gamma|Delta| is small (standard quantitative inverse function theorem); its fixed
point s^* solves psi(s^*) = Delta with |s^* - s^0| <= 2C_2 Gamma^3 |Delta|^2 <= c|Delta|/2, so s^*_k >= c|Delta|/2 > 0 on
one-sided k: the move is admissible.  Lemma 2.2 gives the cost.  QED
If only two-sided channels are used, (TC) needs only independence of the restricted channel vectors (Lemma 2.5).
Masses at contacts are ONE-SIDED channels; this is where the difficulty sits (2.3).

## 2.3 The directional obstruction
**Proposition 2.8 (masses raise z-signed functionals; diagonal bases cannot lower them).** PROVED.
(a) For every z-signed W != 0 there is a bank (namely a^m prop. to a + mW) that strictly increases W(zhat) (Lemma 2.6).
(b) Suppose the base is DIAGONAL: U^*e_j = s_j k_j with (k_j) orthonormal in H and s_j > 0 (an admissible choice of the
canonical base).  Then for every z-signed W and every tuned move with beta = 0, the first-order change of W(zhat) is
sum_{j in K} (m_j/nu) s_j^2 z_j W(j) >= 0 (z-moves on J_free do not see W).  Hence with diagonal U, LOWERING a z-signed
functional is possible only through the |F| two-sided channels beta on F (and normalization removes one of them).
*Proof.* (b) For j notin F, (U P^perp U^* W)(j) = <P^perp U^*W, U^*e_j> = s_j^2 W(j) - <U^*W, e><e, U^*e_j>, and
<e, U^*e_j> = <U^*a, U^*e_j>/nu = s_j^2 a_j/nu = 0 for j notin F.  So z_j h_W(j) = s_j^2 z_j W(j) >= 0 on K, and W = 0 on
J_free.  QED
**Remark 2.8' (second-order global rescaling).** PROVED.  With a diagonal base, let D_c subset K be a finite set of
"donor" contacts disjoint from F and from the supports of a finite family V of vectors, and put masses m_j (j in D_c).
Then X := sum m_j z_j s_j k_j is orthogonal to U^*a and to every U^*V (V in V), so for V in V, EXACTLY,
   V(zhat^tau) = V(z) + lambda <U^*V, e>,   lambda := nu/(nu^2 + ||X||^2)^{1/2} in (0,1],  ||X||^2 = sum m_j^2 s_j^2 :
all Hilbert parts are rescaled by one common factor.  Functionals with <U^*V, e> > 0 are LOWERED by (1 - lambda)<U^*V,e>
at mass cost ~ (nu/s_{j_d}) (2(1 - lambda))^{1/2} (one donor): a square-root cost, affordable by a design with
b(w) <= T_lo(w)^8.  This is one global lowering direction (the base analogue of Y2's donors, which rescale block
quantities); it gives no independent control of several functionals.
*Proof.* <U^*V, k_j> = s_j V(j) = 0 and <U^*a, k_j> = s_j a_j = 0 for j in D_c; hence ||U^*A||^2 = nu^2 + ||X||^2 and
<U^*V, U^*A> = <U^*V, U^*a>.  z is unchanged.  QED

*Reading.*  Exactification has two directions.  CLOSING moves (raise near-contacts to contacts, raise target rooms, raise a
NEGATIVE d-sum V(zhat) < 0 of a z-signed ray to 0) go in the direction that banks provide; OPENING moves (lower a POSITIVE
tiny d-sum of a z-signed ray or carrier to 0; lower a resonant swallowing-type peak below its threshold) go against it.
Closing a room raises eps u_l(zhat) by Re(u_l) >= 0 (Z3 Lemma 1.4) — the same direction as banks.

## 2.4 What tuning and pinning remove, and what remains
At a clean sub-window w of D^PW (part 1), every coarse object is robust (rate >= u(w)) or tiny (rate <= b(w)); a fixed
object with positive rate is robust at all late sub-windows, so tiny objects are those of high level whose rates were
made super-small by f.  Combining Theorem E (+ Lemma 2.3), Lemma 1.8 (ray removal), Lemma 2.2, Propositions 2.7, 2.8:
 (i) rooms (R1), target rooms (R2): tiny ones are closed (closing direction, cost <= design x b(w), Z3_ref Prop 4.3.1(b));
     robust ones pinned.  PROVED as a reduction (given the transplant, Z3 Prop T with Z3_ref fixes).
 (ii) anti-sign (q < 0) swallowed strict non-peaks with tiny gap: dropped, by Lemma 2.9 below; robust gaps are a rate
     (Z6_ref 3.6).  PROVED.
 (iii) d-rows, single-block rays.  If the zero-cost cone of the block contains a ROBUST ray of each sign (robustly
     compensated block): the d-mismatch of the switching vector is removed by Lemma 1.8 (removal of rays of the sign of
     the mismatch) or by ADDING a robust ray of the opposite sign (cost |mismatch|/u(w)); tiny rays need no
     exactification at all.  If there is no robust NEGATIVE ray but tiny negative rays carry the mismatch: raise them
     (Lemma 2.6; exactly, for one ray; for several, under (TC)).  PROVED (single ray) / conditional on (TC).
 (iv) The DIRECTIONAL RESIDUAL (OPEN): 
     (UN+) a block whose zero-cost cone has, at the relevant levels, no robust ray of negative d-sum, while the mate
           switches persistently through rays of TINY POSITIVE d-sum (nearly neutral, positively d-coupled directions;
           this is Z6's item K_nn in uncompensated blocks, now isolated as a direction problem, not a rate problem);
     (P+)  resonant swallowing-type peaks with tiny relative margin carrying persistent switching (Z6's K_P and case (d)):
           pushing them to the non-peak side by moving u_l(zhat) would lower a z-signed functional; but the push can
           instead be done by RAISING THE THRESHOLD of the block (Y2's donors: z-moves on an unused signature set, which
           change no used value u_l(zhat) and rescale all d-coefficients of the block by one factor, Y2 Proposition Q /
           Theorem P).  So (P+) is settled by Y2 except in Y2's "aligned corner"; the genuinely directional residual is (UN+).
     For these the companion route needs LOWERING channels (impossible with a diagonal base beyond |F| - 1 dimensions,
     Prop. 2.8(b)), or a mate-side bound (Z6 Conjecture G for (UN+): switching through nearly neutral directions is
     <= C t x design), or a base U with mixing (non-diagonal) channels satisfying (TC) for lowering directions
     (HEURISTIC: for U^*e_j = s_j(k_j + (-1)^j kappa g), z-signed W have h_W(j) = s_j(-1)^j kappa^2 S(W) + ... of both
     signs at far contacts, so lowering channels exist when S(W) != 0; not proved in the needed uniformity).

**Lemma 2.9 (anti-sign threshold lemma).** PROVED.  Let l = j(k,m) be swallowed with sign eps_l, k in Q_m with
varsigma := sgn w_m(k) = -eps_l (i.e. q_l < 0).  For every two-sided decomposition at scale t <= min(t_eta, 1), with
tau_l := -eps_l Delta theta_l:   tau_l <= lambda_l (3 gap_m(k)/t + |Delta d_m| M_m).
*Proof.* Lemma lem:suplevel(f) and |d_pm t| <= 1/2 give varsigma omega_+(k) <= (3/2) gap/t and varsigma omega_-(k) >=
-(3/2) gap/t.  Since omega_pm = Theta_pm + d_pm w, (omega_+ - omega_-)(k) = Delta Theta(k) + Delta d w(k) with
Delta Theta(k) = Delta theta_l/lambda_l = -eps_l tau_l/lambda_l; multiplying by varsigma (varsigma eps_l = -1):
tau_l/lambda_l + Delta d |w(k)| <= 3 gap/t.  QED
*Consequence.* With (tau_l)_- bounded by the budget on the private part of S_l (Lemma lem:modswallow(b); Z6_ref Thm U'
step (2)), swallowed q < 0 strict non-peaks with gap <= t^2 are pinned like anti-sign peaks: |tau_l| <= lambda_l(3 + K_d)t
+ c/(2m_l).  They can be dropped from the data at cost O(K t): no gap rate and no push is needed for them.

## 2.5 Non-window viewpoints (task (b)(ii)-(iii))
 (a) **Convexity in the first row.** PROVED (elementary).  For fixed g, rho: D(rho g) := {h : (h, rho g) contractive} =
     {h : h(y)^2 <= p(y)^2 - rho^2 g(y)^2 for all y} is convex, symmetric, weak* compact.  Lemma Z for (f,g,rho) is the
     statement that Rec cap S_{p*} meets D(rho g') near f for some g' near g.  The forced-data map (a', z') -> f' is not
     affine (through J_V), so this convexity does not give a convex problem in the forced data; in particular I found no
     way to turn it into an existence proof (HEURISTIC assessment).
 (b) **Locality.** PROVED (Lemma lem:slack + triangle inequality): if p*(f' - f) <= eps then p*(f' + r rho g) <= s(r) for
     |r| >= (6 eps/(1 - rho^2))^{1/2}.  Hence Lemma Z is a LOCAL statement at f' on the scale range |r| <~ p*(f' - f)^{1/2}:
     any method must certify (a modification of) rho g at the small scales of f', i.e. needs exact local structure at f'.
     Theorem E is the quantitative form; a non-window method would have to produce such structure at f' by other means.
 (c) **Baire.** Remark rem:meagre(c) already excludes category arguments.  Nothing new.
 (d) **Multi-level companions.** A tuned row per clean sub-window, used only on that sub-window (scale decoupling), needs no
     compatibility between levels; transitivity (Theorem thm:transitivity) is not needed because Theorem E builds the
     norm-attaining approximants directly.  This is the scheme of (b)(i); its only remaining obstacle is (iv) above.

# Y4 part 3 — Finite-model numerics (scripts in ctx/r6/Y4_work/)

Model (toy.py, copied from r5/Z6_work): X = R^n, q*(A) = ||A||_1 + ||U^T A||_2, one block with carriers
u_k = y_k + 0.15 h_k (private signature coordinates), N_m(W) = ||W||_inf + ||D W||_2, p* by SOCP (Clarabel).  Finite
models are DEGENERATE (every functional attains its norm, every fibre is locally robust); they test signs, first-order
formulas and multi-scale profiles only, never recoverability.

## N1 (n1_channels.py): channel signs and the raising derivative.  CONFIRMS Lemma 2.6 and Proposition 2.8.
n = 40, F = {0,1}, maximal contact with random contact signs, 300 random z-signed W per base.  Quantity: first-order effect
of a unit mass at a contact j on W(zhat), i.e. z_j h_W(j)/nu, h_W = U P^perp U^T W.
 * diagonal U (U^T e_j = s_j k_j):  min_j z_j h_W(j) = 0.000 (never negative): masses only RAISE z-signed functionals;
 * mixing U (U^T e_j = s_j(k_j + (-1)^j 0.6 g)): 46% of the contacts lower W(zhat); min -0.43;
 * random U (rank 6): 48% lowering contacts; min -1.49.
 * raising derivative d/dm W(zhat(a + mW)) vs ||P^perp U^T W||^2/nu: max relative error 2e-8 (all three bases).
Reading: the directional obstruction of Proposition 2.8(b) is real for diagonal bases and absent (to first order, for a
single W) for generic bases.

## N2 (n2_lsc.py): fibre along tuned rows (sanity).  Maximal contact, F = {0,1}, nearly neutral carrier (kappa = 0.05,
q_l = 1.5e-3 > 0), module mate g = c(u_l - q_l L^*w), c = 0.06 (largest valid on the grid), rho = 0.99, scale grid
1e-5..3 (both signs) plus the exact first-order condition h(xi') = 0.
 bank-raise (a' ~ a + mW): cost 3.0e-2 / 1.5e-2 / 7.5e-3 -> dist(rho g, C(f')) = 2.2e-5 / 1.1e-5 / 5.9e-6;
 F-tune to exact neutrality (u_l(zhat') = 8e-17): cost 2.3e-3 -> dist 4.4e-6.
So dist ~ 7e-4 x cost: lower semicontinuity holds trivially in the finite model (degenerate, as expected); no rate
phenomenon can appear in finite dimension.  (The lowering family (C) was not reached within the mass range tried.)

## N3 (n3_ray.py, n3_scan.py): the directional residual (UN+) — switching along a tiny positive ray.
Construction: maximal contact, F = {0}; carriers l1 (q1 > 0) and l2 (q2 < 0), neither z-signed alone; their combinations
mu1 u1 + mu2 u2 are z-signed exactly for mu2/mu1 in [1/2, 2]; extreme rays A (D_A = q1 + q2/2 ~ 1.6e-2, robust) and B
(D_B = q1 + 2q2 = eps_rel |q2|, tiny); NO ray with negative d-sum (uncompensated: the configuration (UN+) of 2.4).  Mate:
ray module g = c(V_B - d-correction).  Measured: min over two-sided decompositions with the TRUE cap s(t) of
(|tau1| + |tau2|)/t (forced switching), at the largest valid c.
 eps_rel = 1:     c_max = 0.024, max_t forced/t = 1.54e-2 (band t in [2.6e-2, 7.1e-2], zero elsewhere)
 eps_rel = 0.1:   c_max = 0.026, max_t forced/t = 1.45e-2
 eps_rel = 0.01:  c_max = 0.026, max_t forced/t = 1.38e-2   (D_B = 8.6e-5)
 eps_rel = 0.001: c_max = 0.026, max_t forced/t = 1.37e-2
At c = 0.02 the forced switching is 0 (< 1e-10) at all 14 scales.
Reading (HEURISTIC): the forced switching through a nearly neutral positive ray is a transient band of height ~1.4e-2
(t-relative) that does NOT grow as its d-sum D_B -> 0 (three decades), whereas the method's pinning bound (Z6 2.4 /
Lemma 1.8) is ~ K/D_B.  The size is set by mate validity (c_max) and gaps (here 0.38, 0.66), i.e. by design-type
quantities.  This is evidence for a RAY version of Z6 Conjecture G and suggests that (UN+) is an artifact of the bound,
not of the geometry.  Caveat: finite models cannot exhibit persistence across infinitely many levels.

# Y4 part 4 — The remaining step, relation to Round 5 / Round 6, labels

## 4.1 Why (UN+) is the right residual, and what Conjecture G_ray would have to say
 (a) PROVED (from Parts 1-2): at a clean sub-window of D^PW the only coarse objects whose tiny regime is not handled by
     closing moves, removal (Lemma 1.8), compensation by a robust ray of the opposite sign, raising (Lemma 2.6/Prop. 2.7),
     the anti-sign threshold lemma (Lemma 2.9) or Y2's threshold-raising donors, are rays of tiny POSITIVE d-sum in blocks
     whose zero-cost cone has no robust negative ray.  Exact d-neutral data then require either dropping their switching
     or lowering their d-sums.
 (b) HEURISTIC (un-switching analysis).  Rays of tiny d-sum are the EASIEST to un-switch: moving the ray component of one
     side from the base (where it is free at first order) into the block coordinates of the ray's carriers changes the
     block's uniform shift only by (amplitude) x D_r (tiny) and changes the levels at first order only by terms
     proportional to D_r.  The obstruction to un-switching is purely second order: the one-sided (base) carriage has
     quadratic cost ~ t^2 mu^2 q_0 h(V_r)/2, the two-sided (block) carriage ~ t^2 mu^2 sigma_m H_m(omega_r)/2, and a mate
     whose optimal one-sided coefficient is strictly below its balanced coefficient (Remark rem:onesided(b), gamma^+ <
     Gamma_w) genuinely prefers switching.  With slack (1 - rho^2) t^2/2 (the mate is rho g) a fraction of the switching
     can always be removed; full removal at O(t) error needs the switching amplitude through such rays to be O(t), which is
     Conjecture G_ray.  For single modules the switching is a transient band (N3, Z6 R4) because the module is a finite
     certificate at small scales; for general mates (infinite module sums, persistent gamma^+ < Gamma_w) it is OPEN.
 (c) Statement.  CONJECTURE G_ray (OPEN).  For the design D^PW, F finite, a clean sub-window w of level l and a block m
     whose zero-cost cone at level l has no ray r with d-sum <= -u(w) D_norm(r), every g in C(f) admits, at every dyadic
     scale t of w, a two-sided decomposition at scale t whose switching through the rays of d-sum in (0, b(w)] has
     l_1-size <= C(f) Design(l) t.
     Under Conjecture G_ray, these rays are pinned with design constants at clean sub-windows and the residual (UN+)
     disappears; the remaining items are then: the assembly of Theorem E + Proposition T + Theorems A''/U'/Y at tuned rows
     on clean sub-windows (SKETCH), multi-block rays (m'), Y2's aligned corner and coherent shift resonance, and (O4).

## 4.2 Relation to the other Round-5/Round-6 work
 * Z3 / Z3-referee: Proposition 1.2 and Theorem 1.6 extend the referee's band-disjointness (Prop. 4.2.1) from one rate per
   carrier to any design-countable family of rate objects (pigeonhole sub-windows).  Lemma 2.3 is the "growing-support
   Lemma U" that the Z3 referee called plausible; it removes the |F| - 1 limitation of re-tuning (Z3 4.3(iii)) in the
   raising direction, and Proposition 2.8 shows the limitation is genuine in the lowering direction for diagonal bases.
 * Z6 / Z6-referee: (UN+) is the direction-refined form of the K_nn item; N3 adds evidence for Conjecture G in a MIXED
   (ray) configuration, with the switching size independent of the d-sum over three decades.
 * Y2 (Round 6): Y2's donors (z-moves on unused signature sets) raise block thresholds and rescale d-coefficients by a
   common factor; Remark 2.8' is the base analogue (masses on donor contacts rescale all Hilbert parts by a common factor).
   Y2's Theorem M reduces item (m) to a face Farkas rate K_F^rel whose nearly-neutral part is exactly (UN+); our Lemma 1.8
   (ray removal) is the single-block special case of that reduction with an explicit constant 1/D_min, and Proposition
   2.8 explains why the nearly-neutral part cannot be removed by tuning (diagonal bases).  Y2 settles (P+) (degenerate
   swallowing-type peaks) by threshold raising, except its aligned corner.

## 4.3 Labels
| # | Statement | Label | Where |
|---|---|---|---|
| 1 | Explosive design + Cantor pairing: per-carrier rates (R types) block <= R N((2L)^{1/2}+1) windows in [1,L] | PROVED | 1.2 |
| 2 | Ray d-sums dominated by per-carrier d-coefficients in one-signed blocks (up to design factors) | PROVED | 1.3 |
| 3 | A diagonal row blocks every window of the explosive design through ray d-sums | OPEN (HEURISTIC: plausible) | 1.3 |
| 4 | D^PW admissible, N-free; all window theorems survive on sub-windows | PROVED (by inspection, as Z3-ref 4.1.1) | 1.4-1.5 |
| 5 | Clean sub-windows at every level for every f and every design-countable rate scheme | PROVED | 1.6 |
| 6 | No first row beats every window through rates (band/rate items are design artifacts modulo exactification) | PROVED (as stated) | 1.7 |
| 7 | Ray removal: dist_1(tau, C cap ker D) <= |D(tau)|/D_min | PROVED | 1.8 |
| 8 | Multi-block rays: joint d-objects | OPEN | 1.8 Limitation |
| 9 | Cost of tuned rows: p*(f^tau - f) <= C mu log(e/mu) | PROVED | 2.2 |
| 10 | Lemma U / Theorem E with banked support (contact-like data) | PROVED (by inspection) | 2.3 |
| 11 | Joint injectivity of channels on Y; design-constant version | PROVED | 2.4, 2.5 |
| 12 | Raising lemma (a + mW raises W(zhat) at rate ||P^perp U^*W||^2/nu) | PROVED (+ numerics N1) | 2.6 |
| 13 | Exact tuning under the cone condition (TC) | PROVED | 2.7 |
| 14 | Diagonal bases cannot lower z-signed functionals at first order (only |F| - 1 channels) | PROVED (+ numerics N1) | 2.8 |
| 15 | Second-order global rescaling by donor contacts | PROVED | 2.8' |
| 16 | Anti-sign threshold lemma (tau <= lambda(3 gap/t + |Delta d| M)) | PROVED | 2.9 |
| 17 | Reductions (i)-(iii) of 2.4 at clean sub-windows (rooms, anti-sign carriers, compensated/raisable d-rows) | PROVED as reductions; assembly SKETCH | 2.4 |
| 18 | Directional residual (UN+) | OPEN | 2.4(iv), 4.1 |
| 19 | Convexity in the first row; locality of Lemma Z | PROVED (elementary) | 2.5 |
| 20 | Finite-model lsc along tuned rows | numerics (trivial, degenerate) | N2 |
| 21 | Switching through a tiny positive ray independent of its d-sum | HEURISTIC (numerics N3) | N3 |
| 22 | Conjecture G_ray | OPEN | 4.1(c) |
| 23 | Un-switching analysis (second-order obstruction only) | HEURISTIC | 4.1(b) |
| 24 | Lowering channels with design conditioning for mixing bases | OPEN (HEURISTIC: plausible) | 2.4(iv) |
FALSE: nothing new.  Corrections to earlier statements: Z3 7.1 "the band defeats every window method" is false for the
pigeonhole design (and for per-carrier rates already for the explosive design, Z3-referee); the claim of the first draft of
this report that exact neutralization by masses removes K_nn is FALSE for positive d-sums with a diagonal base (Prop. 2.8),
corrected in the final text.
