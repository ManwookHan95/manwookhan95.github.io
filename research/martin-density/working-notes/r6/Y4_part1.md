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
