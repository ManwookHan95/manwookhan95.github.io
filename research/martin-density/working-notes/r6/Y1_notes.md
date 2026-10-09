# Y1 notes (Round 6): one N-free design D_X and a master theorem that removes the rate obstruction (r)

Setting: paper/martin_density_note.tex (Sections 1, 7, 8: notation and numbering), Round-5 reports Z3-Z6 with their referee fixes.
Finite block sets I = {1..N}, p = p_N; D_X is ONE admissible operator for all N (so Lemma lem:martintail applies: Lemma Z for
infinitely many N gives density for Martin's norm built with D_X).  F = supp a finite unless said otherwise.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Part files: Y1_part0 (reading digest), Y1_part1..4, Y1_part5a, 5b, 5c
(assembled below in the order 1, 2, 3, 4, 5a, 5c, 5b; 5c contains the definition (Rep) used in 5a and the corrected design factor
Q(w) = Design(l)^4 u(w)^{-omega(l)-8}, already inserted in part 1).  Script: Y1_work/threshold_check.py.
Parallel Round-6 work read after the plan was fixed (unrefereed): Y4 (design D^PW and pigeonhole sub-windows: same idea as
Theorem 2 below), Y2 (Lemma T, donors, Theorem E', Theorem P for degenerate peaks: same threshold mechanism as part 4).  Every
statement used here is proved here; overlaps are marked.  No counterexample is claimed; nothing found points to one.

## 0. Summary
(1) DESIGN D_X (part 1, PROVED admissible, N-free, Section 8 and all refereed Round-5 window theorems survive): SLD with an explosive
ladder of SUB-WINDOWS: each level l has M(l) = omega(l) + 1 consecutive sub-windows with pairwise disjoint bands (b(w), u(w)),
omega(l) = 3l + |T(l)| = number of rate objects of level l; the design factor contains Z4's G*(l), Z6's H_comb(l) and D(l) (D''' fixes:
1/Phi, m^nat), a GENERALIZED configuration Hoffman constant G**(l) (arbitrary contact patterns on all coarse targets), 2^{sigma(l)}
(donor coordinates) and |T(l)|; fine weights c_{l+1} <= b(l, M(l))^2.
(2) RATE DICHOTOMY (part 2, PROVED): at EVERY level l some sub-window w is clean: every rate of level l — room of a signature set
outside all coarse targets (R1), target room (R2), threshold distance |rho - 1| (R3, margins and gaps), relative d-coefficient rho (R4) —
is TINY (<= b(w)) or ROBUST (>= u(w)).  Lemma T (threshold equation, independent of Y2) and Lemma T2 (quantitative raising).
(3) PINNING AT f (part 3, PROVED): robust rooms pin DIAGONALLY (no products, no slaving: coarse targets are excluded from the pinning
sets); tiny-room carriers are "generalized bad" with one-sided budget pinning; robust margins pin swallowing-type peaks; NEW: a
near-threshold strict non-peak of ANTI type is pinned like an anti-type peak (its tiny gap is not a rate); one-signed blocks are
d-row-pinned with constants design x u^{-1} (robust q) — only nearly neutral carriers stay free.
(4) EXACTIFYING COMPANION (part 4, PROVED): f^#_w closes all tiny rooms (C1) and tiny target rooms (C2) and RAISES THE THRESHOLD
(C3) of every block containing near-threshold swallowing-type carriers through a DONOR (a peak whose signature tail has the anti sign;
always available at maximal contact), at cost p*(f^# - f) <= C_f T_lo(w)^3 log(1/T_lo(w)) = o(T_lo(w)^2).  After the raise every
near-threshold coordinate (weak peak, DEGENERATE peak, tiny-gap non-peak) is a strict non-peak of f^# (tiny positive gap), all robust
statuses are preserved, d-neutrality is preserved except through closed rooms/targets (Lemma 4.3 = Z3 Lemma 1.4: forced sign).
(5) MASTER THEOREM (5.4, PROVED): for D_X, f in Rec if at infinitely many levels a clean sub-window satisfies (SP_w) [shift sources],
(Do_w) [donors where a raise is needed], (Cmp_w) [each block compensated at w or one-signed] and (NN_w) [no uncompensable
nearly neutral kept carriers].  No growth/rate condition at all.  Corollaries: maximal contact (M1): weak and degenerate swallowing
peaks, near-threshold carriers, rooms: all harmless; (M2): Z4 Theorem A'' without (H3) and without (W_inf), donors instead of (H3).
(6) RESIDUAL (5.6, OPEN): (n) directional nearly-neutral resources in one-signed blocks (incl. Z3 Lemma 1.4 carriers), (m) blocks
neither compensated nor one-signed, (d) "aligned corner" (no donor), (h) failure of (SP_w), (O4) infinite F.  None is a rate.

How the task items are answered.  (1) D_X: part 1 (Theorem 1; combinatorial Farkas constants: Remark (0)).  (2) Rate dichotomy:
Theorem 2 gives a clean sub-window at EVERY level (not only infinitely many windows); exactification: rooms and target rooms are
CLOSED by explicit raises (C1), (C2); margins and gaps are not exactified to degenerate values but moved away from the threshold by
an explicit THRESHOLD RAISE (C3) (weak, degenerate and tiny-gap swallowing-type carriers become strict non-peaks; no genericity step,
no peak-ification); tiny gaps of anti-type non-peaks need nothing (Lemma 3.5(b)); tiny d-coefficients are harmless in compensated
blocks and in the opposite direction of one-signed blocks.  Lemma 1.4 of Z3: Lemma 4.3 (forced positive sign; residual (n)).
Status stability: Lemma 4.2.  Exact window data with design constants at the companion: Proposition 5.2; uniformity along
companions: Lemma U / Theorem E' (5.3).  Master theorem: 5.4; residual: 5.6.

| # | Statement | Label | Where |
|---|---|---|---|
| 1 | D_X admissible, N-free; (P1), (P2), (P3_X); disjoint bands; survival of Section 8 and Round-5 theorems | PROVED | part 1 |
| 2 | Clean sub-window at every level (pigeonhole) | PROVED | part 2, Thm 2 |
| 3 | Threshold equation Psi(theta) = 0; P = {nu >= theta}; monotonicity | PROVED (+num.) | Lemma T |
| 4 | Quantitative Lipschitz/raising bounds for the threshold; uniform rescaling of relative positions | PROVED | T2, T3 |
| 5 | Diagonal pinning by rooms outside all coarse targets | PROVED | Lemma 3.1 |
| 6 | One-sided pinning of generalized-bad carriers | PROVED | Lemma 3.2 |
| 7 | Shift pinning from window-level sources | PROVED | Lemma 3.4 |
| 8 | Near-threshold anti-type strict non-peaks are pinned | PROVED | Lemma 3.5(b) |
| 9 | d-row pinning of one-signed blocks (robust q) | PROVED | Lemma 3.6 |
| 10 | Exactifying companion: cost o(T_lo^2), status table, d-coefficients | PROVED | Lemmas 4.1, 4.2 |
| 11 | Lemma 1.4 revisited: closing a room of a d-neutral carrier forces q^# = r^nat/A^# > 0 | PROVED | Lemma 4.3 |
| 12 | Repair directions untouched by the companion; (DR) => (Rep) | PROVED | Lemmas 5.1, 5.1' |
| 13 | Transplant: exact d-neutral two-piece data at f^#_w with design x u^{-k} constants | PROVED | Prop 5.2 |
| 14 | Theorem E' (window-dependent c_flat, inward coordinates) | PROVED | 5.3 |
| 15 | MASTER THEOREM | PROVED | 5.4 |
| 16 | Corollaries M1 (maximal contact), M2 (Thm A'' without (H3), (W_inf)) | PROVED | 5.5 |
| 17 | Tiny imbalances can be repaired by converted near-threshold anti-type peaks | SKETCH | 5.6 Remark (3) |
| 18 | Residual (n), (m), (d), (h), (O4) | OPEN | 5.6 |
# Y1 part 1 — The design D_X: definition, admissibility, N-independence, survival

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; numbering and notation as there), Round-5 reports (Z3-Z6 with
referee fixes).  Finite block sets I = {1..N}, p = p_N; D_X will be ONE operator serving every N (Lemma lem:martintail).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Parallel Round-6 work (unrefereed, read after the plan below was fixed): Y4_part1 (design D^PW: pigeonhole sub-windows;
D_X below is a variant of D^PW with a larger design factor and smaller fine weights), Y2_notes (Lemma T, donors, Theorem E').
Where a statement coincides with Y2/Y4 this is said; every statement used below is proved here.

## 1.1 Design quantities computable at stage l
In Definition def:SLD keep (D0) (any bijection j with j(k,m) < j(k',m) for k < k'; j_0; pairwise disjoint infinite
S_l in N \ {j_0}; h_l, delta_l; targets y^{(i)} dense in S_{q*} with y^{(1)} = e*_{j_0}/q*(e*_{j_0}); the sequence (i_r)), the
allowedness rule (a), (b) of (D1) (which only uses c_l and c_{l'}, delta_{l'} for l' < l), and y_l, n_l, u_l, delta°_l,
Lambda°(l).  Put v_l := delta_l h_l/n_l (so u_l = v_l on S_l by (P1)), Phi_l := 2^{-m(l)-k(l)} c_l.  At stage l (after y_l, u_l
and c_{l''}, l'' <= l, are fixed) the following are determined by the design data of index <= l:
 * T(l) := union_{l'' <= l} supp y_{l''} (finite), s_max(l) := max(T(l) ∪ {1});
 * sigma(l) := max_{l'' <= l} min(S_{l''} ∩ (s_max(l), infinity))  ("first free signature coordinate beyond the coarse targets");
 * m^nat_{l''}(l) := ||v_{l''} 1_{S_{l''} \ ([1,l] ∪ T(l))}||_1 > 0  (l'' <= l)  (Z6 referee, D''');
 * D(l) := 1 + sum_{l'' <= l} (1/m^nat_{l''}(l) + 1/Phi_{l''})  (D''');
 * G*(l) (Z4 configuration constant, configurations over ALL subsets of [1,l]: Z4 referee fix), H_comb(l) (Z6 5.2, all patterns
   with B_* in [1,l]), and the GENERALIZED configuration constant G**(l) of 1.2;
 * omega(l) := 3l + |T(l)| (the number of rate objects of level l, part 2).
Every one of these is N-free: none refers to L_N.

## 1.2 Generalized configurations and G**(l)
A *generalized configuration of level l* is kappa = (U, P, eps, F', type) with U a subset of [1,l] (any blocks), P a subset of U,
eps in {+1,-1}^U, F' a subset of T(l), and type : T(l) \ F' -> {+1, -1, 0} ARBITRARY (Z4 imposed type(s) = eps_{l'} on S_{l'};
here no such restriction).  For tau in R^U put L_j(tau) := sum_{l in U} eps_l tau_l u_l(j) (design values).  For beta in
[0,infinity)^U the polyhedron Z_kappa(beta) is defined by
 (Z1) tau_l >= 0 (l in U \ P);  (Z2) type(j) L_j(tau) >= 0 if type(j) = +-1, L_j(tau) = 0 if type(j) = 0 (j in T(l) \ F');
 (Z3) tau_l = 0 (l in P);       (Z4) |tau_l| <= beta_l (l in U).
It contains 0.  Put viol_kappa,beta(tau) := sum_{U\P}(tau_l)_- + sum_{type +-1}(type(j)L_j(tau))_- + sum_{type 0}|L_j(tau)| +
sum_P |tau_l| + sum_U (|tau_l| - beta_l)_+.  By Hoffman's error bound [Hoffman 1952] the constant H(kappa) := sup over beta >= 0
and tau of dist_1(tau, Z_kappa(beta))/viol_kappa,beta(tau) is finite and depends only on the matrix of the system (not on beta);
G**(l) := max(1, max{H(kappa) : kappa generalized configuration of level <= l}) is finite (finitely many kappa) and
nondecreasing.  PROVED (finiteness: U, P, eps, F', type range over finite sets; RHS-independence: Hoffman 1952, the sets are
nonempty for beta >= 0).

## 1.3 Definition of D_X
**Definition 1 (design D_X).**  (D0) and allowedness as above.  (D1_X) Recursively in l = 1, 2, ...: given c_l (c_1 := 1),
choose y_l, n_l, u_l, delta°_l, Lambda°(l) as in def:SLD, compute the quantities of 1.1-1.2 and put
   Design(l) := [ l 2^{l^3} 2^{sigma(l)} Lambda°(l) (1 + |T(l)|) D(l) G*(l) H_comb(l) G**(l) ]^6  (>= 1),
   M(l) := omega(l) + 1  sub-windows w = (l,i), i = 1..M(l); all sub-windows ordered lexicographically, w^- = predecessor;
   u(1,1) := 1/4,   u(w) := b(w^-) (w != (1,1)),
   Q(w) := Design(l)^4 u(w)^{-omega(l)-8},   n(w) := ceil(l 2^{l^3} Q(w)),
   T_hi(w) := min{ T_lo(w^-), 2^{-l^3}/(l Q(w)) }  (T_lo((1,1)^-) := 1),   T_lo(w) := 2^{-n(w)} T_hi(w),
   b(w) := T_lo(w)^4/(l Design(l)),
   c_{l+1} := min{ c_l/4, b(l, M(l))^2 }.
(D2) T e_{k,m} := c_{j(k,m)} u_{j(k,m)}.
The *window* of level l is W(l) := [T_lo(l, M(l)), T_hi(l, 1)] (the union of its sub-windows, which are consecutive
dyadic-scale intervals W(w) := [T_lo(w), T_hi(w)]); n^w_l := log_2(T_hi(l,1)/T_lo(l,M(l))).  Band(w) := (b(w), u(w)).

The recursion is well defined: every quantity of level l uses only data of index <= l and c_l; c_{l+1} is fixed last.

## 1.4 Theorem 1 (D_X is admissible, N-free, and every window theorem survives).  PROVED.
(a) T is admissible (Definition def:admissible) and satisfies (P1) and (P2) of Theorem thm:SLD; more precisely
    sum_{l' > l} c_{l'} <= 2 c_{l+1} <= 2 b(l, M(l))^2  and  sum_{l' > l} lambda_{l'} <= b(l, M(l))^2/2.
(b) (P3_X) for every sub-window w = (l,i):  l 2^{l^3} Q(w) T_hi(w) <= 1,  n(w) >= l 2^{l^3} Q(w) >= l 2^{l^3} Design(l),
    T_hi(w^+) <= T_lo(w); and for the full windows the old (P3): T_hi(l,1) 2^{l^3} Lambda°(l) <= 1/l, n^w_l >= l 2^{l^3} Lambda°(l),
    T_hi(l+1,1) <= T_lo(l,M(l)).  Moreover b(w) < u(w), u(w^+) = b(w), so the bands Band(w) are pairwise disjoint, and
    for every sub-window w of level l: sum_{l' > l} lambda_{l'} <= b(w)^2/2 <= T_lo(w)^8.
(c) D_X does not depend on N.
(d) (Survival.)  For D_X and every N the following hold, with "window W(l)" read either as the full window W(l) or as any
    single sub-window W(w) of level l: all of Section 8 of the note (Theorem thm:SLD with (P3), Theorems thm:R0,
    thm:reductionZ, thm:Bstar, thm:Bpm, thm:S and all lemmas of Section 8, incl. Remark rem:lemmaZ); Z3: Theorem E, Lemma U
    (any admissible T), Lemma 3.1, Lemma 3.2 (with the referee's definition of "flipped"), Proposition T with fixes T2-T6 and
    Corollary 3.4 (with K^#_*), Theorems 5.3, 5.4, Proposition 4.1 (with r*_l > 0 added) and 4.2; Z4: Theorem A'' (N-free G*;
    (H2'') of the Z4 referee), Corollaries 4.2 and 5.4 (with the referee corrections); Z5 (infinite F): the extensions
    refereed in Z5_referee.md (T1-T12, Theorem R1), as they use only (T-a)-(T-d), (P1)-(P3) and allowedness; Z6: Theorem C,
    Theorem U' (design-factor requirement of D''': n^w_l >= l 2^{l^3} Lambda°(l) Xi'(l) and T_hi <= its inverse), Theorem V,
    Proposition P, Corollary V.1, Proposition R1.
Proof.  (a) The proof of Theorem thm:SLD uses (D1) only through allowedness (a),(b) and c_{l+1} <= c_l/4, both kept; (P1) is
unchanged; c_{l+1} <= c_l/4 gives sum_{l'>l} c_{l'} <= (4/3) c_{l+1} <= 2c_{l+1}, and lambda_{l'} <= c_{l'}/4.
(b) T_hi(w) <= 2^{-l^3}/(lQ(w)) and n(w) >= l 2^{l^3}Q(w) by definition; T_hi(w^+) <= T_lo(w) by definition (also across
levels: (l+1,1)^- = (l, M(l))).  Q(w) >= Design(l) >= Lambda°(l), and T_hi(l,1) <= 2^{-l^3}/(l Lambda°(l)), n^w_l >= n(l,1).
Bands: u(w) <= 1/4 for all w (u(w) = b(w^-) <= T_lo(w^-)^4 <= 1/4); n(w) >= Q(w) >= u(w)^{-8} >= 4, so
b(w) <= T_lo(w)^4 <= 2^{-4n(w)} < u(w) (as 2^{-4n} <= 2^{-4u^{-4}} < u for u <= 1/4); u(w^+) = b(w) by definition; the bands
are consecutive open intervals of a decreasing sequence, hence pairwise disjoint.  Finally b(l, M(l)) <= b(w) for every w of
level l (b decreases along the order), so sum_{l'>l} lambda_{l'} <= c_{l+1}/2 <= b(l,M(l))^2/2 <= b(w)^2/2 <= T_lo(w)^8.
(c) Every ingredient of 1.1-1.3 is N-free (configuration/pattern constants are maximized over all subsets of [1,l]).
(d) The note states after Theorem thm:SLD (and the Round-5 referees re-checked for SLD_G, D''', D1^F) that Section 8 uses only
(T-a)-(T-d), (P1), (P2), (P3) and allowedness.  In every window proof the window enters only through (i) the dyadic scales of
ONE window, (ii) conditions "T_hi(l) x (f-dependent factor) -> 0" and "n^w_l/(f-dependent factor) -> infinity" along the
windows used, where the factor is at most C_f^{l^2} times design quantities of level l (Lambda°, G*, H_comb, D(l), Xi'(l) of
D''': Xi'(l) = [l H_comb G* D]^4 (l 2^{l^3} Lambda° G*)^5 <= Design(l)^2 <= Q(w); SLD_G: (l 2^{l^3} Lambda° G*)^6 <= Design(l)), (iii) the box bound sum_{l'>l} |Delta theta_{l'}| <=
6 sum_{l'>l} lambda_{l'}/t <= 6t^2, which needs sum_{l'>l} lambda_{l'} <= T_lo^3, and (iv) T_hi(next) <= T_lo(previous).
By (b), (i)-(iv) hold for the full windows and for every sub-window (Q(w) >= Design(l)^4 dominates every design factor listed,
and C_f^{l^2}/2^{l^3} -> 0).  Z3 Theorem E, Lemma U and Lemma 3.1 hold for every admissible T.  QED

**Remarks.** (0) Farkas constants (Z6 Proposition P).  The Farkas systems of Z6 consist of zero-cost rows (combinatorial: their
faces are again generalized configurations, so their Hoffman/Farkas constants are bounded by G**(l), cf. the Y2 referee's "faces of
configuration cones are free configurations") and d-rows (f-dependent coefficients q_l).  In one-signed blocks the certificate is
the d-row itself with norm <= C/min|q| and |q| >= Phi M/(mC) at peaks and near-threshold carriers, absorbed by 1/Phi in D(l) (Z6
referee 3.1).  The remaining f-dependent Farkas constants (mixed blocks without repair directions) are not design quantities and
are not used below: they belong to the residual (m).
(1) Compared with Y4's D^PW, D_X adds 2^{sigma(l)} (1+|T(l)|) G**(l) to the design factor and takes
c_{l+1} <= b(l,M(l))^2 instead of T_lo(l,M(l))^3: fine carriers then perturb every coarse rate by O(b^2) only (used in part 4).
(2) The order of quantifiers is the usual one: D_X is fixed before f; every f-dependent quantity is either a FIXED f-constant
(absorbed by l 2^{l^3} -> infinity) or a RATE, i.e. a number attached to a design-countable object (part 2).
# Y1 part 2 — Rate objects, clean sub-windows, and the threshold equation

Design D_X (part 1), N >= 1, f in S_{p*} with F finite and forced data (xi, q_0, a, w, F, z, zhat, e, nu).  For a block m
put zeta_m := R_m^** zhat (zhat-units: zeta_m(k) = lambda_{k,m} u_{k,m}(zhat)), A_m := |zeta_m|_m, and theta_m := A_m M_m/C_m
(so the note's threshold constant is vartheta_m = q_0 theta_m/m).  For a carrier l = j(k,m) put
   nu_l := |zeta_m(k)|/Phi_m(k)^2  and the RELATIVE POSITION  rho_l := nu_l/theta_m = |u_l(zhat)|/(Phi_l theta_m/m).
(Lemma T below: k in P_m iff rho_l >= 1; margin mu_{k,m} = q_0 Phi_l theta_m (rho_l - 1)/m on P_m; gap_m(k) = M_m(1 - rho_l) on
Q_m; for strict non-peaks |q_l| = Phi_l M_m rho_l/(m C_m), and q_l = eps_l u_l(zhat)/A_m for bad l (Z6 2.1).)

## 2.1 Rate objects of level l (l >= l_0(f) := max F)
For l'' <= l:
 (R1) ROOM outside the coarse targets: S^nat_{l''}(l) := S_{l''} \ (F ∪ T(l)),
      r^nat_{l''}(l) := min_{sigma = +-1} sum_{s in S^nat_{l''}(l)} v_{l''}(s)(1 + sigma z_s),  rate_1 := r^nat/||v_{l''} 1_{S^nat}||_1 in [0,2]
      (well defined: S^nat_{l''}(l) contains S_{l''} \ ([1,l] ∪ T(l)), whose v-mass is m^nat_{l''}(l) > 0);
 (R2) TARGET ROOM: for j in T(l) \ F, rate := 1 - |z_j| in [0,1];
 (R3) THRESHOLD DISTANCE: rate := |rho_{l''} - 1|;
 (R4) RELATIVE POSITION (relative d-coefficient): rate := rho_{l''}.
Their number is l + |T(l)| + 2l = omega(l).  At level l, "coarse" = index <= l.

**Theorem 2 (clean sub-windows).  PROVED.**  For every f with F finite and every level l >= max F there is i in {1..M(l)}
such that the sub-window w = (l,i) is CLEAN: no rate of level l lies in Band(w) = (b(w), u(w)).  At a clean sub-window every
rate of level l is TINY (<= b(w)) or ROBUST (>= u(w)).
Proof.  The bands of the M(l) = omega(l) + 1 sub-windows of level l are pairwise disjoint (Theorem 1(b)); each of the omega(l)
numbers lies in at most one of them.  QED
(Same pigeonhole as Y4 Theorem 1.6; it holds at EVERY level, not only along a subsequence.)

Scale relations at a sub-window w = (l,i) (Theorem 1): t in W(w) implies t >= T_lo(w), and
   b(w) = T_lo(w)^4/(l Design(l)),  u(w) = b(w^-) (w != (1,1)),  and T_hi(w) <= 1/Q(w) <= u(w)^{omega(l)+8} << u(w).
In particular, for t in W(w):  b(w) Design(l) <= t^4/l,  and  Design(l)^4 u(w)^{-omega(l)-8} = Q(w) <= 2^{-l^3}/(l T_hi(w)).   (2.1)

## 2.2 The threshold equation (any admissible T)
Fix a block, drop m.  For zeta in l_1 \ {0} and x > 0 put
   Ah(x; zeta) := sum_k (|zeta(k)| - x Phi_k^2)_+ ,   Bh(x; zeta) := sum_k min(x Phi_k, |zeta(k)|/Phi_k)^2 ,   Psi := Ah^2 - Bh.

**Lemma T (threshold equation).  PROVED.**  (a) P = {k : nu_k >= theta}, and |zeta||alpha(k)| = |zeta(k)| - theta Phi_k^2 on P.
(b) |zeta| = Ah(theta; zeta) and |zeta|^2 = Bh(theta; zeta).  (c) Psi(.; zeta') has a unique zero on (0, infinity) for every
zeta' != 0, it is positive before and negative after it, and the zero is theta(zeta').  (Same as Y2 Lemma T (a)-(c).)
Proof.  (a) Lemma lem:threshold: zeta/|zeta| = alpha + D^2 w/C, ||alpha||_1 = 1, alpha on P with the signs of w.  On P, |w| = M,
so |zeta(k)| = |zeta||alpha(k)| + Phi_k^2 |zeta| M/C = |zeta||alpha(k)| + theta Phi_k^2.  Off P, |zeta(k)| = |zeta|Phi_k^2|w(k)|/C <
theta Phi_k^2.  (b) Summing (a) over P: Ah(theta) = |zeta| ||alpha||_1.  C^2 = sum_k Phi_k^2 w(k)^2 with |w(k)| = min(M,
C|zeta(k)|/(Phi_k^2|zeta|)) = (C/|zeta|) min(theta, nu_k); hence C^2 = (C/|zeta|)^2 Bh(theta).  (c) Ah is continuous and
nonincreasing, strictly decreasing while positive; Bh is continuous, nondecreasing, and positive for x > 0; Psi(0+) = ||zeta'||_1^2
> 0; if Ah(x) = 0 then Psi(x) < 0, and Ah(x) -> 0 as x -> infinity by dominated convergence.  So Psi is strictly decreasing on
{Ah > 0}, negative afterwards, and has exactly one zero; by (b) for zeta' it is theta(zeta').  QED

Note: M = theta/(theta + |zeta|), C = |zeta|/(theta + |zeta|) (from M/C = theta/|zeta| and M + C = 1).

**Lemma T2 (quantitative stability and raising).  PROVED.**  Let zeta != 0, theta := theta(zeta), A := |zeta|, phi := ||Phi||_2^2,
and let k_0 be a peak with nu_{k_0} > theta (a non-degenerate peak; it exists since ||alpha||_1 = 1); put phi_0 := Phi_{k_0}^2,
h_0 := min(1, nu_{k_0} - theta), C_1 := (1 + 2(theta+1)/A)/phi_0.
(a) (Lipschitz) If zeta' satisfies E := ||zeta' - zeta||_1 with C_1 E < min(h_0, theta), then |theta(zeta') - theta| <= C_1 E.
(b) (raising at a peak) Let c be a peak (nu_c >= theta, degenerate allowed), zeta' with |zeta'(c)| = |zeta(c)| + s, sgn zeta'(c) =
sgn zeta(c), s > 0, and E := sum_{k != c} |zeta'(k) - zeta(k)| <= A s/(8(A + theta + 1)).  Then
   theta(zeta') - theta >= min{1, A s/(8 phi (A + theta + 1))},  and, if C_1(s + E) < h_0,  theta(zeta') - theta <= C_1 (s + E).
Proof.  The c-term of Bh does not change in (b) while c stays a peak; every term of Ah is 1-Lipschitz in |zeta(k)|; every term of
Bh(x; .) is 2x-Lipschitz in |zeta(k)| (both minima are <= x Phi_k, and |min(xPhi, a/Phi) - min(xPhi, a'/Phi)| <= |a - a'|/Phi).
Also, for h >= 0: Ah(x+h) >= Ah(x) - h phi, Ah(x - h) >= Ah(x) + h Phi_{k}^2 for every k with nu_k >= x; Bh(x+h) <= Bh(x) +
(2xh + h^2) phi; Bh is nondecreasing.
(a) Upper bound: for h := C_1 E + epsilon <= h_0, k_0 is in P(theta + h) (for zeta), so Ah(theta+h; zeta) <= A - h phi_0, and
Psi(theta+h; zeta') <= (A - h phi_0 + E)^2 - (A^2 - 2(theta+1)E) < 0 because h phi_0 > E + 2(theta+1)E/A and h phi_0 <= A
(phi_0 h_0 <= Phi_{k_0}^2 (nu_{k_0} - theta) <= |zeta(k_0)| <= A).  [Expand: (A - y)^2 - A^2 = -y(2A - y) <= -yA for 0 <= y <= A,
y := h phi_0 - E.]  Lower bound: Psi(theta - h; zeta') >= (A + h phi_0 - E)^2 - A^2 - 2 theta E > 0 for h phi_0 > E(1 + theta/A).
By Lemma T(c), theta - h < theta(zeta') < theta + h.
(b) Lower bound: with h := min{1, A s/(8 phi(A+theta+1))}, c is a peak of zeta' at level theta + h (nu'_c >= nu_c + s/Phi_c^2 >=
theta + h, since s/Phi_c^2 >= s/phi >= h), so Ah(theta+h; zeta') >= A - h phi + s - E and Bh(theta+h; zeta') <= A^2 + (2theta+1) h phi
+ 2(theta+1)E.  With E <= A s/(8(A+theta+1)) <= s/8 and h phi <= s/8:
   Psi(theta+h; zeta') >= 2A(s - E - h phi) - (2theta+1) h phi - 2(theta+1)E >= (3/2) A s - A s/4 - A s/4 > 0,
so theta(zeta') > theta + h.  Upper bound: as in (a), with A replaced by A + s on the left (the c-term of Ah grows by s).  QED

**Corollary T3 (relative positions under a threshold raise).  PROVED.**  In the situation of Lemma T2(b), for every k != c,
   rho'_k = (|zeta'(k)|/|zeta(k)|) rho_k theta/theta(zeta')   (rho'_k computed for zeta'),
so if zeta'(k) = zeta(k) then rho'_k = rho_k/(1 + delta) with delta := theta(zeta')/theta - 1 >= c_raise s for
s <= 8 phi (A + theta + 1)/A, where c_raise := A/(8 phi theta (A + theta + 1)); and delta <= C_1 (s + E)/theta when C_1(s+E) < h_0.
Proof: rho_k = |zeta(k)|/(Phi_k^2 theta(zeta)); Lemma T2(b).  QED
Reading (PROVED by T, T2): pushing a PEAK outward raises the threshold (rate d log theta/ds = C^2/(M A sum_P Phi^2) at points
where the peak set is locally constant, by differentiating (b)); pushing a STRICT NON-PEAK inward raises it as well (Y2 Lemma
T(d)(ii)); the threshold raise rescales every untouched relative position by the common factor 1/(1+delta).  The d-coefficients
of untouched strict non-peaks, q_l = eps_l u_l(zhat)/A_m, are rescaled by the common factor A_m/A'_m: d-neutrality and the
d-row cone of the block are unchanged (Y2 Section 2 makes the same observation).

## 2.3 Numerical sanity check (Y1_work/threshold_check.py)
200 random finite blocks (n = 12, Phi_k = 2^{-k} x U(0.3,1), random zeta): the block norm computed by SOCP as
min max(||x||_1, ||y||_2) over zeta = x + D y agrees with Ah(theta) at the root of Psi to relative error 6.3e-10; in 582
local pushes the threshold moves in the predicted direction (peak outward: up; strict non-peak outward: down; strict non-peak
inward: up); the derivative of log theta under an outward push of a non-degenerate peak equals C^2/(M A sum_P Phi^2) to relative
error 4e-7.  (A first run with a wrong primal formula, sum instead of max, disagreed; the max form is the Minkowski functional
of B_{l_1} + D(B_{l_2}), dual to ||f||_inf + ||Df||_2.)  Y1_work/t2_check.py: 3000 random blocks (n = 14), random peak c, push
s in [1e-6, 1e-1] A, random perturbation of l_1-size up to A s/(8(A+theta+1)) elsewhere: 0 violations of the lower bound of Lemma
T2(b), 0 of its upper bound, and 0 of the Lipschitz bound T2(a) (3000 random perturbations with C_1 E < min(h_0, theta)).
Sanity checks only.
# Y1 part 3 — Pinning at f on a clean sub-window (all rates robust or tiny)

Setting: D_X, N >= 1, f in S_{p*} with F finite, g in C(f), eta <= eta_* with eta_Gamma(eta) <= 1; w = (l,i) a CLEAN
sub-window (Theorem 2) with l >= l_f, where l_f (depending only on f) is >= max F and >= the indices of the finitely many fixed
carriers used below (donors, repair directions); t in W(w) dyadic, t <= min(t_eta, 1); (B_+-, Theta_+-) a two-sided
decomposition of g at scale t.  "f-constant" = number depending only on f, N (and g, rho where stated), not on l, w, t.
By Theorem 1(b) and (2.1): sum_{l' > l} |Delta theta_{l'}| <= 6 sum_{l'>l} lambda_{l'}/t <= 3 b(w)^2/t <= t^7, and b(w) <= t^4/l.

**Classification of the coarse carriers l'' <= l at w** (rate_1 = normalized room on S^nat_{l''}(l) = S_{l''} \ (F ∪ T(l))):
 * ROBUST-GOOD (class R): rate_1 >= u(w);
 * GENERALIZED-BAD (class G): rate_1 <= b(w).  Then eps_{l''} in {+-1} denotes a sign with
   r^nat_{l''}(l) = sum_{s in S^nat_{l''}} v_{l''}(s)(1 - eps_{l''} z_s), and tau_{l''} := -eps_{l''} Delta theta_{l''}.
   (Every exactly swallowed carrier of the note, z = eps on S_{l''} \ F, is in class G with r^nat = 0 and the same eps.)
For a G-carrier l'' = j(k,m): q_{l''} := eps_{l''} Phi_m(k) w_m(k)/(m C_m) (as in Definition def:swallowed); it is a
SWALLOWING-TYPE carrier if eps_{l''} sgn w_m(k) = +1 (then q > 0) and ANTI-TYPE if = -1 (q < 0); if w_m(k) = 0 it is d-neutral.
Relative positions rho (part 2): peak iff rho >= 1; near-threshold iff |rho - 1| <= b(w); NEARLY NEUTRAL iff rho <= b(w);
otherwise rho is robust on both counts (|rho - 1| >= u(w) and rho >= u(w)).  Put D := D(l) (Theorem 1), so lambda_{l''} >=
Phi_{l''} >= 1/D and m^nat_{l''}(l) >= 1/D for l'' <= l.

**Lemma 3.1 (diagonal pinning of class R).  PROVED.**  sum_{l'' in R} |Delta theta_{l''}| <= K_g t, K_g := (1/q_0 + 1) D/u(w).
Proof.  For s in S^nat_{l''}: no target of a coarse carrier contains s (s notin T(l)), coarser targets avoid S_{l''} (allowedness
(a)), other signatures vanish (disjointness); by (P1) and eq:DeltaB, -Delta B(s) = Delta theta_{l''} v_{l''}(s) + r(s),
r(s) := sum_{l' > l} Delta theta_{l'} y_{l'}(s)/n_{l'}.  By Lemma lem:phicalc(c),(d) (as in the proof of Lemma lem:signmixed),
r^nat_{l''} |Delta theta_{l''}| <= E_{l''} + 2 sum_{s in S^nat_{l''}} |r(s)|,  E_{l''} := sum_{s in S^nat_{l''}} phi_{z_s}(Delta B(s)).
The sets S^nat_{l''} are disjoint subsets of F^c, so sum E <= t/q_0 (Lemma lem:switchbudget), and sum_{l''} sum_s |r(s)| <=
(4/3) sum_{l'>l} |Delta theta_{l'}| <= 2t^7.  For l'' in R, r^nat_{l''} >= u(w) ||v_{l''} 1_{S^nat}||_1 >= u(w) m^nat_{l''}(l) >= u(w)/D.
QED  (No triangular unrolling, no product of rooms, no slaving: coarse targets are excluded from the pinning sets.)

**Lemma 3.2 (one-sided pinning of class G).  PROVED.**  sum_{l'' in G} (tau_{l''})_- <= K_g t, and
e_0 := Delta B 1_{F^c} - sum_{l'' in G} eps_{l''} tau_{l''} u_{l''} 1_{F^c} satisfies ||e_0||_1 <= K_g t + t^7.
Proof.  With the same r(s): Delta B(s) = eps tau v(s) - r(s) on S^nat_{l''}, and phi_{z_s}(eps tau v(s)) = |tau| v(s)(1 - eps z_s sgn tau)
>= (tau)_- v(s)(1 + eps z_s); by Lemma lem:phicalc(c), summing over S^nat_{l''},
(tau)_- sum v(s)(1 + eps z_s) = (tau)_-(2||v 1_{S^nat}||_1 - r^nat) <= E_{l''} + 2 sum|r(s)|,
and 2||v 1|| - r^nat >= ||v 1_{S^nat}|| >= 1/D because r^nat <= b(w)||v 1|| <= ||v 1||.  e_0 = -sum_{R ∪ fine} Delta theta u 1_{F^c},
||u||_1 <= 1, Lemma 3.1.  QED

**Lemma 3.3 (peak relations).  PROVED.**  Let k = k(l''), l'' <= l, be a peak of block m, vs := sgn w_m(k), mu its margin.
 (a) l'' in R: Delta d_m M_m <= |Delta theta_{l''}|/lambda_{l''}; if rho_{l''} >= 1 + u(w), also Delta d_m M_m >= -|Delta theta_{l''}|/lambda
     - t/(lambda mu), and 1/(lambda_{l''} mu_k) <= m D^2/(q_0 theta_m u(w)).
 (b) l'' in G anti-type: Delta d_m M_m <= (tau)_-/lambda and tau <= -lambda Delta d_m M_m.
 (c) l'' in G swallowing-type: tau >= lambda Delta d_m M_m, and if mu > 0: tau <= lambda(Delta d_m M_m + t/(lambda mu)).
Proof.  eq:peakshift: Y := |omega_+(k)| + |omega_-(k)| = -vs Delta Theta_m(k) - Delta d M >= 0, Y <= t/(sigma|alpha(k)|) = t/(lambda mu)
(eq:margin), and Delta Theta_m(k) = Delta theta/lambda = -eps tau/lambda.  (a) |vs Delta Theta| <= |Delta theta|/lambda.  The margin is
mu = q_0 Phi theta_m (rho - 1)/m >= q_0 Phi theta_m u/m (part 2), and lambda = m Phi >= Phi, Phi >= 1/D.  (b) vs eps = -1:
-tau/lambda - Delta d M = Y >= 0.  (c) vs eps = +1: tau/lambda - Delta d M = Y in [0, t/(lambda mu)].  QED

**Definition (shift sources at w).**  For a block m an UPPER source is: (U1) a peak of block m in class R; or (U2) an anti-type
G-peak; or (U3) every coarse G-carrier of block m with q < 0 is an anti-type peak or an anti-type strict non-peak with
|rho - 1| <= b(w) or rho <= b(w).  A LOWER source is: (L1) a class-R peak with rho >= 1 + u(w); or (L2) a swallowing-type G-peak
with rho >= 1 + u(w); or (L3) every coarse G-carrier of block m with q > 0 has rho <= b(w).  (SP_w): every block has an UPPER
and a LOWER source at w.  (This is (H2'') of the Z4 referee read at the window; with fixed exactly swallowed peaks it holds at
every window, e.g. at maximal contact by Lemma 5.0 of Z4: swallowing-type and anti-type peaks with margins >= q_0/4.)

**Lemma 3.4 (shift pinning).  PROVED.**  Under (SP_w): |Delta d_m| M_m <= K_d t for every m, K_d := C_f D^3/u(w), C_f an f-constant.
Proof.  Upper bounds: (U1), (U2) by Lemma 3.3(a),(b), Lemmas 3.1, 3.2 and lambda >= 1/D.  (U3): by eq:didentity,
 Delta d M = (1/(mC)) sum_{R ∪ fine} Phi w Delta theta - sum_{G, m(l'')=m} q tau + r_m,  |r_m| <= 2t/sigma_m
(for a G-carrier Phi w Delta theta/(mC) = -q tau).  The first sum is <= (K_g t + t^7)/(mC).  For q > 0: -q tau <= q (tau)_-,
summing to <= K_g t/C (|q| <= 1/C, |w| <= 1).  For q < 0, -q tau = |q| tau, and by (U3): at anti-type peaks tau <= -lambda Delta d M
(Lemma 3.3(b)); at anti-type strict non-peaks with |rho - 1| <= b, Lemma suplevel(f) gives vs(omega_- - omega_+)(k) >= -3 gap/t,
while vs(omega_- - omega_+)(k) = vs eps tau/lambda - Delta d |w(k)| = -tau/lambda - Delta d |w(k)|, so tau <= lambda(3gap/t - Delta d|w(k)|)
with gap = M(1 - rho) <= b; at carriers with rho <= b, |q| tau <= (b Phi M/(mC)) 6 lambda/t <= t^3.  Hence
 Delta d M (1 + sum_{anti-peaks, anti-np} |q| lambda) <= (K_g + 2)t/C_m + 2t/sigma_m + 3 sum|q| lambda b/t + N t^3,
and the bracket is >= 1.  Lower bounds symmetrically: (L1), (L2) by Lemma 3.3(a),(c) (with 1/(lambda mu) <= m D^2/(q_0 theta u));
(L3): every q > 0 term satisfies |q tau| <= t^3, and -q tau = |q| tau >= -|q|(tau)_- for q < 0.  QED

**Lemma 3.5 (carriers pinned at f).  PROVED.**  With K_P := K_g + K_d + C_f D^2/u(w):
 (a) anti-type G-peaks: |tau| <= K_P t;   (b) anti-type G strict non-peaks with |rho - 1| <= b(w): |tau| <= K_P t;
 (c) swallowing-type G-peaks with rho >= 1 + u(w): |tau| <= K_P t;    (d) class-R carriers: |Delta theta| <= K_g t.
Proof.  (tau)_- <= K_g t (Lemma 3.2) in (a)-(c).  (a) tau <= -lambda Delta d M <= K_d t.  (b) as in the proof of Lemma 3.4:
tau <= lambda(3b/t + K_d t) <= (3t^3 + K_d t).  (c) tau <= lambda K_d t + t/mu, 1/mu <= m D/(q_0 theta u) (Lemma 3.3(a)).  QED
(b) is new: a near-threshold strict non-peak of anti type is pinned like an anti-type peak; its tiny gap is NOT a rate that
needs exactification.  Its counterpart, a near-threshold carrier of swallowing type, is NOT pinned (tau_+ free).

**Lemma 3.6 (d-row pinning of one-signed blocks).  PROVED.**  Let Sigma_m(w) be the set of coarse G-carriers of block m that are
swallowing-type peaks, or strict non-peaks with rho > b(w) which are not anti-type near-threshold.  Call block m
SIGMA-ONE-SIGNED at w (sigma in {+-1}) if sgn q = sigma on Sigma_m(w).  Then for every l'' in Sigma_m(w):
 |tau_{l''}| <= K_O t,  K_O := C_f D^2 (K_g + K_P)/u(w).
Proof.  Z6 2.4 (re-derived by the Z6 referee, 1.4): in eq:didentity the terms of Sigma_m(w) are -q tau with q of one sign, so
sum_{Sigma_m} |q| (tau)_+ <= A_m := |Delta d|M + 2t/sigma + (1/(mC)) sum_{l notin Sigma_m} Phi|w||Delta theta_l| + sum_{Sigma_m} |q|(tau)_-.
Carriers outside Sigma_m(w): class R and fine (K_g t + t^7), anti-type peaks and anti near-threshold non-peaks (Lemma 3.5), G-carriers
with rho <= b (Phi|w||Delta theta| = Phi M rho |tau| <= b 6 lambda/t <= t^3).  So A_m <= C_f (K_g + K_P) t.  For l'' in Sigma_m(w):
|q| = Phi M/(mC) at peaks and |q| = Phi M rho/(mC) >= Phi M u(w)/(mC) at strict non-peaks (rho > b implies rho >= u at a clean
sub-window), and Phi >= 1/D.  QED

**Summary (kept/dropped at w).**  DROPPED (pinned at f with constants <= C_f D^3 K_g/u(w), i.e. design x u(w)^{-2}): class R;
anti-type G-peaks; anti-type near-threshold G strict non-peaks; swallowing-type G-peaks with robust margin; in sigma-one-signed
blocks the whole of Sigma_m(w).  KEPT (switching free, must be carried by exact data): the remaining G-carriers, namely
 (K1) swallowing-type strict non-peaks (q > 0), any gap;  (K2) anti-type strict non-peaks with rho <= 1 - u(w) (robust gap
 gap = M(1 - rho) >= M u(w));  (K3) nearly neutral strict non-peaks (rho <= b(w), incl. exactly d-neutral ones);
 (K4) near-threshold swallowing-type carriers (weak or degenerate peaks with rho in [1, 1+b], non-peaks with rho in [1-b, 1)),
 in blocks that are not one-signed.  In sigma-one-signed blocks only (K3) is kept.
# Y1 part 4 — The exactifying companion f^#_w: closing raises and threshold raises

Setting of part 3 (D_X, f with F finite, clean sub-window w = (l,i), l >= l_f).  Companions keep a (hence e, nu, F): they are
the first rows with forced data (a, z^#), z^# = z on F (Remark rem:lemmaZ(c)), and Delta := zhat^# - zhat = z^# - z.

## 4.1 Donors
**Definition (donor).**  A DONOR of block m is a carrier c = j(k_c, m) such that k_c is a non-degenerate peak of block m
(margin mu_c > 0), S_c ∩ F = {} and vs_c z_s <= 0 for all but finitely many s in S_c (vs_c := sgn w_m(k_c)).
Donors are fixed (f-dependent) carriers; we fix one donor c_m per block that has one, and take l_f >= all c_m.
Examples (PROVED): every exactly swallowed ANTI-TYPE non-degenerate peak (z_s = -vs_c on S_c \ F); at maximal contact (z = eps_0
off F) every block has donors: by Z4 Lemma 5.0 it has non-degenerate peaks with w = -eps_0 M_m (margin >= q_0/4), and their
signature sets are contacts of sign eps_0 = -vs.  A donor is pinned at every window: at w it is either in class R (Lemma 3.5(d))
or in class G with eps_c = -vs_c (the minimizing sign of r^nat_c is -vs_c up to the finitely many exceptional coordinates, which
lie in [1,l] for l >= l_f, so outside S^nat_c), i.e. an anti-type G-peak (Lemma 3.5(a)).  In both cases it is DROPPED.

**Definition (raised blocks).**  Block m NEEDS A RAISE at w if it is not sigma-one-signed at w (Lemma 3.6) and contains a kept
carrier of type (K4) (near-threshold, swallowing type).  Hypothesis (Do_w): every block that needs a raise has a donor.

## 4.2 The companion
**Definition.**  f^# = f^#_w is the companion with z^# := z except:
 (C1) [close rooms] for every class-G carrier l'' <= l: z^#_s := eps_{l''} for s in S^nat_{l''}(l);
 (C2) [close target rooms] for every j in T(l) \ F with 0 < 1 - |z_j| <= b(w): z^#_j := sgn z_j;
 (C3) [raise thresholds] for every block m that needs a raise: let s_m := min(S_{c_m} ∩ (s_max(l), infinity)) (so s_m <= sigma(l),
      s_m notin F ∪ T(l), and vs_{c_m} z_{s_m} <= 0 for l >= l_f) and z^#_{s_m} := z_{s_m} + theta_m vs_{c_m}(1 - vs_{c_m} z_{s_m}),
      theta_m in (0,1] chosen so that lambda_{c_m} |u_{c_m}(Delta)| = T_lo(w)^3 (possible for l >= l_f, see 4.3).
The three sets of modified coordinates are pairwise disjoint (S^nat parts avoid T(l); the S^nat_{l''} lie in distinct signature
sets; s_m notin T(l), and s_m in S_{c_m}; if c_m is in class G, (C3) is applied after (C1)).  |z^#| <= 1 and z^# = z = sgn a on F.

## 4.3 Lemma 4.1 (cost of the companion).  PROVED.
For l >= l_f:  p*(f^#_w - f) <= C_f T_lo(w)^3 log(1/T_lo(w)) =: theta_w T_lo(w)^2,  theta_w := C_f T_lo(w) log(1/T_lo(w)) -> 0,
and ||R_m^*(w^#_m - w_m)||_1 + ||D_m(w^#_m - w_m)||_2 + |C^#_m - C_m| + |M^#_m - M_m| + |sigma^#_m - sigma_m| + |q^#_0 - q_0| <=
C_f T_lo(w)^3 log(1/T_lo(w)).
Proof.  Z3 Lemma 3.1 (any admissible T): p*(f^# - f) <= C_f c(Delta) once max_m Delta_m <= c_f, with Delta_m = sum_k lambda_{k,m}
|u_{k,m}(Delta)| and c(Delta) = sum_m [Delta_m log(e/Delta_m) + sum_k min(lambda_{k,m}, |u_{k,m}(Delta)|)].  Coarse carriers
l'' <= l: (C1) changes u_{l''} only on its own S^nat (no coarse target meets S^nat_{l''}): |u_{l''}(Delta_{C1})| = r^nat_{l''} <= b(w);
(C2) changes every u_{l''} by <= ||u_{l''}||_inf |T(l)| b(w) <= |T(l)| b(w); (C3) changes, among coarse carriers, only u_{c_m}
(s_m notin T(l) and s_m in S_{c_m}), by T_lo(w)^3/lambda_{c_m}.  Fine carriers: sum_{l'>l} min(lambda, .) <= sum lambda <= b(w)^2/2,
and their contribution to Delta_m is <= 2 sum lambda <= b(w)^2.  Hence Delta_m <= l(|T(l)|+1) b(w) + T_lo(w)^3 + b(w)^2 <= 2T_lo(w)^3
(b(w) <= T_lo(w)^4/(l Design(l)) and Design(l) >= 1 + |T(l)|), and c(Delta) <= C N T_lo^3 log(e/T_lo^3) + l(|T|+1) b + sum_m
T_lo^3/lambda_{c_m} + b^2 <= C_f T_lo(w)^3 log(1/T_lo(w)).  The bounds on the block data are those of Z3 Lemma 3.1.
Feasibility of (C3): the available change is lambda_c v_c(s_m)(1 - vs z_{s_m}) >= lambda_c delta_c 2^{-sigma(l)}/n_c, while T_lo(w)^3 <=
T_hi(w)^3 <= Q(w)^{-3} <= Design(l)^{-3} <= 2^{-18 sigma(l)}; so it suffices that 2^{-17 sigma(l)} <= lambda_c delta_c/n_c, true for
l >= l_f since sigma(l) -> infinity (targets have unbounded supports, as they are dense in S_{q*}) and c ranges over N fixed donors.  QED

## 4.4 Lemma 4.2 (data of the companion; status table).  PROVED.
For l >= l_f (l_f larger if necessary, depending only on f) and every coarse carrier l'' <= l other than donors:
 (a) |u_{l''}(zhat^#) - u_{l''}(zhat)| <= (|T(l)| + 1) b(w); and, in zhat-units, ||R_m^** zhat^# - R_m^** zhat||_1 restricted to
     non-donor coordinates is E_m <= 2l(|T(l)|+1) b(w) + b(w)^2.
 (b) In a block m without a raise: |theta^#_m/theta_m - 1| <= C_f E_m (Lemma T2(a)).  In a raised block: theta^#_m/theta_m - 1 =:
     delta_m with c_f T_lo(w)^3 <= delta_m <= C_f T_lo(w)^3 (Lemma T2(b) with s = T_lo(w)^3, E = E_m + b(w)^2 << s; the donor
     stays a peak because its margin is a fixed positive number and the perturbation is <= C_f E_m).
 (c) Relative positions: rho^#_{l''} = rho_{l''} theta_m/theta^#_m + O(C_f D(l)(|T(l)|+1) b(w)).  Hence: robust peaks (rho >= 1+u)
     stay peaks with rho^# >= 1 + u/2; robust strict non-peaks (rho <= 1-u) stay strict non-peaks with rho^# <= 1 - u/2 (gap^# >=
     M^# u/2); nearly neutral carriers keep rho^# <= 2b + C_f D(|T|+1)b; in a RAISED block every near-threshold coordinate
     (|rho - 1| <= b) becomes a strict non-peak with rho^# <= 1 - delta_m/3, i.e. gap^#(k) >= M^#_m delta_m/3 > 0.
 (d) Signature and target structure: class-R carriers keep S^nat_{l''} untouched (rooms unchanged); for a class-G carrier,
     z^# = eps_{l''} on S^nat_{l''}(l) EXACTLY; every j in T(l) \ F is at f^# either a contact (|z^#_j| = 1, with the sign of z_j if
     |z_j| > 0) or a free coordinate with room 1 - |z^#_j| = 1 - |z_j| >= u(w); contacts of f in T(l) keep their sign.
 (e) d-coefficients: for every class-G carrier which is a strict non-peak of f^#, q^#_{l''} = eps u_{l''}(zhat^#)/A^#_m, and
     |q^#_{l''} - q_{l''} A_m/A^#_m| <= (|T(l)|+1) b(w)/A^#_m at strict non-peaks of f (for converted (K4) peaks, |q^#_{l''} -
     Phi M/(m C)| <= C_f(b(w) + delta_m) Phi M/(mC)).  In particular d-neutral carriers (u_{l''}(zhat) = 0) stay EXACTLY d-neutral
     unless their u-vector meets a (C1)-raised set of THEIR OWN S^nat (Lemma 4.3) or a (C2)-raised target coordinate.
Proof.  (a) From the proof of Lemma 4.1 (C3 does not affect non-donor coarse carriers; fine carriers contribute <= b^2 in
l_1(zhat-units)).  (b) Lemma T2 applied to zeta := R_m^** zhat and zeta' := R_m^** zhat^# (all constants of T2 depend on the fixed
vector R_m^** zhat, i.e. on f).  (c) rho = |u(zhat)| m/(Phi theta) (part 2), Phi_{l''} >= 1/D(l), (a), (b); for raised blocks
(1 + b)/(1 + delta) + C_f D(|T|+1) b <= 1 - delta/3 because D(|T|+1)b <= T_lo^4/l << delta; gap^# = M^#(1 - rho^#).  At a clean
sub-window robust means >= u(w) >> delta_m + C_f D(|T|+1) b.  (d) Definitions (C1)-(C3) and the room dichotomy at a clean
sub-window (R2): target rooms are tiny (raised) or >= u(w).  (e) Z6 2.1 at f^# (q = eps u(xi)/sigma = eps u(zhat)/A), (a), and for a
converted peak |u(zhat)| = rho Phi theta/m with |rho - 1| <= b and theta/A = M/C.  QED

## 4.5 Lemma 4.3 (Z3 Lemma 1.4, revisited).  PROVED.
Let l'' be a class-G carrier with r^nat_{l''} > 0 and u_{l''}(zhat) = 0 (d-neutral at f), and suppose no (C2) coordinate meets
supp u_{l''}.  Then eps u_{l''}(zhat^#) = r^nat_{l''} > 0: at f^# it is a strict non-peak with q^# = r^nat/A^#_m > 0, nearly neutral
(rho^# <= C_f D b(w)).  Proof: u(Delta) = sum_{s in S^nat} v(s)(eps - z_s) = eps r^nat by the choice of eps.  QED
So "choose the exactification to keep d-neutrality" is impossible with the same base part (the raise is forced by the closing of
S^nat and its first-order effect has a definite sign: it is the defect Re(u) of Z3), and re-tuning the Hilbert part with supp a
fixed has |F| - 1 degrees of freedom (Z3 referee).  Y4 Proposition 2.8 (unrefereed) shows more: banks of masses at contacts can
only RAISE z-signed functionals (diagonal U), so a positive defect cannot be removed by banks.  In the master theorem (part 5) the
resulting tiny q^# > 0 is HARMLESS in blocks that have a fixed repair direction of negative d-sum (it is compensated by an
O(b(w)/t)-small multiple of that direction), and is the residual item (n) otherwise.
# Y1 part 5a — Transplant: exact d-neutral two-piece data at the companion f^#_w

Setting of parts 3-4: D_X, f with F finite, g in C(f), clean sub-window w = (l,i), l >= l_f, t in W(w) dyadic, t <= min(t_eta,1),
a two-sided decomposition (B_+-, Theta_+-) of g at f at scale t, companion f^# = f^#_w.  Constants: K_g, K_d, K_P, K_O of part 3
(all <= C_f D(l)^5 u(w)^{-3}); G := class-G coarse carriers; P := the DROPPED G-carriers (Summary of part 3: anti-type G-peaks,
anti-type near-threshold G strict non-peaks, swallowing-type G-peaks with robust margin, Sigma_m(w) in one-signed blocks, donors).

**Repair directions.**  For a block m and a sign s, (DR^s_m) means (Z4 Definition (DR), one sign at a time): there is a finitely
supported rho^{m,s} in R^B_{>= 0} (B = exactly swallowed carriers of f) with zero cost at f (sum_l eps_l rho_l u_l 1_{F^c} is z-signed
and supported in K), vanishing at swallowed peaks, with d-sums sum_{m(l)=m} q_l rho_l = s and sum_{m(l)=m'} q_l rho_l = 0 (m' != m).
Block m is COMPENSATED if (DR^+_m) and (DR^-_m) hold (Z4's (DR); e.g. resonant bad strict non-peaks with q > 0 > q', Z6).
Repair directions are fixed f-dependent objects; R_f := max ||rho^{m,s}||_1; l_f is taken >= every carrier in their supports.

**Hypotheses at w.**
 (SP_w)  shift sources (part 3);   (Do_w)  donors for the blocks that need a raise (part 4);
 (Cmp_w) every block is COMPENSATED AT w ((Rep^+_m) and (Rep^-_m), Definition in Y1_part5c / notes 5.1') or sigma-one-signed
         at w (Lemma 3.6) for some sigma = sigma_m;
 (NN_w)  in every sigma-one-signed block m: no KEPT carrier (type (K3)) has sigma q^#_{l''} > 0, and if some kept carrier has
         sigma q^#_{l''} < 0, then (Rep^sigma_m) holds at w.  (q^# = d-coefficient at f^#, Lemma 4.2(e).)
 (Fixed directions: (DR^s_m) at f implies (Rep^s_m) at every clean w of large level, Lemma 5.1'.)

**Lemma 5.1 (repair carriers are untouched by the companion).  PROVED.**  For l >= l_f: every carrier l_R in the support of a
repair direction satisfies u_{l_R}(zhat^#) = u_{l_R}(zhat), hence q^#_{l_R} = q_{l_R} A_m/A^#_m EXACTLY, and every repair direction has
zero cost at f^#; its d-sums at f^# are s A_m/A^#_m in block m and 0 in every other block.
Proof.  l_R is exactly swallowed, so (C1) does nothing on S^nat_{l_R}.  The near-contacts in supp u_{l_R} \ F are finitely many
coordinates with FIXED rooms > 0; for l >= l_f these rooms exceed u(w) (u(w) -> 0), so (C2) does not touch them.  (C3) acts on
s_m notin T(l) in the signature set of a donor (a peak, hence not in the support of a repair direction, which vanishes at peaks).
So u_{l_R}(Delta) = 0, and q^# = eps u(zhat^#)/A^# (Lemma 4.2(e)).  Zero cost at f^#: contacts of f keep their signs at f^#, and at
non-contacts of f the vector of the direction vanishes (zero cost at f).  QED

**Proposition 5.2 (transplant at a clean sub-window).  PROVED (by modification of Z3 Proposition T, Z4 Steps 2-6 and Z6
Theorem U' (5)-(6); every departure is listed).**  Assume (SP_w), (Do_w), (Cmp_w), (NN_w).  Then there is a functional g_t carrying
d-neutral two-piece data (b^+-, omega^+-) AT f^# (Definition def:twopiece at f^#) such that
 (i)   b^+-(xi^#) = 0, t||b^+-||_1 <= A_0 (an f-constant), Gamma^#_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta) + C theta_w) + K_w t)^2;
 (ii)  p*(g - g_t) <= K_w t,  with K_w <= C_f Design(l)^3 u(w)^{-3} (Y1_part5c 5c.2);
 (iii) every k in supp omega^+-_m satisfies, at f^#, one of [1] gap^#(k) >= t^2, |omega(k)| <= 2gap^#(k)/t; [2] gap^#(k) >= gamma(w) :=
       min_m M_m u(w)/4 and |omega(k)| <= A_2/t; [3] k a strict non-peak of f^# with the INWARD sign for the side (vs omega^+(k) <= 0
       <= vs omega^-(k), up to 1.5 gap^#(k)/t) and |omega(k)| <= A_2/t;  A_2 := 22.
Proof.
Step 1 (zero-cost projection; combinatorial).  Let tau := (tau_{l''})_{l'' in G} (tau = -eps Delta theta).  Let kappa^# be the generalized
configuration of level l with U := G, P as above, eps, F' := F ∩ T(l), type(j) := sgn z^#_j if |z^#_j| = 1 and 0 otherwise
(j in T(l) \ F), and box radii beta_{l''} := 12 lambda_{l''}/t.  For tau' in Z_{kappa^#}(beta), V(tau') := sum_G eps tau'_{l''} u_{l''} 1_{F^c}
is z^#-signed and supported in K^#: on S^nat_{l''} only u_{l''} among G-vectors lives (no coarse target there) and z^# = eps_{l''}
(Lemma 4.2(d)), tau' >= 0; on T(l) \ F the rows (Z2); elsewhere the G-vectors vanish (supp u_{l''} \ F is in S^nat_{l''} ∪ T(l)).
Violations by the actual tau (Lemmas 3.2-3.6, 4.2(d); Delta B 1_{F^c} = V(tau) + e_0):
 (Z1): sum (tau)_- <= K_g t;  (Z2) at contacts of f^#: (z^#_j L_j(tau))_- <= (z^#_j Delta B(j))_- + |e_0(j)| and (z^#_j Delta B(j))_- <=
 phi_{z_j}(Delta B(j)) (if z_j = z^#_j = +-1, or z^#_j = sgn z_j with |z_j| < 1: phi_z(x) = |x|(1 + |z|) when sgn x = -sgn z); at
 free coordinates of f^# (room >= u(w)): |L_j(tau)| <= phi_{z_j}(Delta B(j))/u(w) + |e_0(j)|; sum <= (t/q_0)(1 + 1/u(w)) + 2||e_0||;
 (Z3): sum_P |tau| <= l K_O t (Lemmas 3.5, 3.6);  (Z4): |tau| <= 6 lambda/t (Lemma lem:box): no violation.
Hoffman (definition of G**(l)): tau_0 in Z_{kappa^#}(beta) with ||tau - tau_0||_1 <= G**(l) V_w, V_w := C_f l D^5 u(w)^{-3} t.
Step 2 (d-rows at f^#).  Q^#_m(tau') := sum_{l'' in G\P, m(l'')=m} q^#_{l''} tau'_{l''}.  By eq:didentity at f and Lemmas 3.1, 3.5, 3.6:
|sum_{G, m} q tau| <= (K_d + (K_g+1)/C_m + 2/sigma_m) t and |sum_{P,m} q tau| <= l K_O t/C_m.  For kept l'': |q^# - q A/A^#| <=
(b(w) |q| + (|T(l)|+1) b(w))/A^#_m (Lemma 4.2(e); for converted (K4) peaks q = eps vs Phi M/(mC) and |u(zhat)| = rho Phi theta/m with
|rho - 1| <= b), and |tau_0| <= 12 lambda/t; so |Q^#_m(tau_0)| <= K_Q t with K_Q := C_f(K_d + K_g + l K_O + G** V_w/t) + C l(|T(l)|+1)b/t^2,
and b/t^2 <= t^2.
Step 3 (exact d-repair).  Let rho^{m,s} be the directions of (Rep^s_m) at w (d-sums s d_{m,s} in block m, d_{m,s} >= u(w)/Design(l),
0 in the other blocks, all computed at f^#).  Compensated block m: c_m := |Q^#_m(tau_0)|/d_{m,-sgn Q}, add c_m rho^{m, -sgn Q^#_m(tau_0)}.
sigma-one-signed block m: the kept carriers are of type (K3) only; if all have q^# = 0 then Q^#_m(tau_0) = 0; otherwise by (NN_w) all
nonzero q^# of kept carriers have sign -sigma, so sgn Q^#_m(tau_0) in {0, -sigma}, and we add (|Q^#_m(tau_0)|/d_{m,sigma}) rho^{m,sigma}.
Call the result tau'.  The d-sums of the added directions are block-diagonal at f^#, so Q^#_m(tau') = 0 for every m, and
||tau' - tau_0||_1 <= N K_Q t Design(l)/u(w).  Sums of zero-cost vectors with nonnegative coefficients have zero cost (Z4 Lemma 2.3: phi_z is
subadditive and positively homogeneous), so V' := V(tau') is z^#-signed in K^#, and
  ||Delta B 1_{F^c} - V'||_1 <= ||e_0||_1 + ||tau - tau'||_1 <= K_U t,  K_U := K_g + 1 + G** V_w/t + N K_Q Design(l)/u(w).
(Carriers of the repair directions may lie in P; they receive only amounts <= K_Q t Design/u(w); they are strict non-peaks of f^#,
with gap^# >= M u(w)/4 where q^# < 0 (definition of (Rep)).)
Step 4 (split at f^#).  Lemma lem:split at f^# needs sum_{j notin F} [phi_{z^#_j}(B_+(j)) + phi_{-z^#_j}(B_-(j))] = O(t): off the modified
coordinates phi_{z^#} = phi_z; at (C2) coordinates (raises, same sign) phi_{z^#}(x) <= 2 phi_{z}(x) (Z3 Lemma 3.2); at (C1) coordinates with
z_s eps >= 0 likewise; at the remaining modified coordinates (flipped (C1) coordinates, z_s eps < 0, the referee's definition, and the
(C3) coordinates) phi_{z^#}(x) <= 2|x|, and by Lemma lem:phicalc(b), |B_+(j)| + |B_-(j)| <= |Delta B(j)| + phi_{z_j}(B_+(j)) + phi_{-z_j}(B_-(j)),
so these coordinates cost at most 2 sum_j |Delta B(j)| + t/q_0.  On S^nat_{l''}, Delta B(s) = eps tau v(s) - r(s) and the flipped v-mass is
<= r^nat_{l''} <= b(w), so sum_{flipped} |Delta B| <= (6/t) b(w) sum lambda + 2t^7 <= t^2; at s_m only the donor (pinned, |Delta theta_c| <= K_P t)
and fine carriers live: |Delta B(s_m)| <= K_P t + t^7.  So chi, frak e_+- exist with ||frak e_+-||_1 <= K_U t + 2N K_P t + 3t/q_0.
Step 5 (data and estimates).  Define, AT f^#, omega^+_m := clamp of omega_{+,m} with gap^# (Definition def:windowcert) at the coarse
strict non-peaks of f^# carrying no kept switching, 0 at peaks of f^#, omega^+_m(k(l'')) := omega_{+,m}(k(l'')) at kept carriers and at the
repair carriers; omega^-_m := omega^+_m + sum_{l''} (eps tau'_{l''}/lambda_{l''}) e_{k(l'')}; b^+ := B_+ 1_F + chi V' - kappa^# a with
kappa^# := (B_+1_F + chi V')(zhat^#); b^- := b^+ - sum eps tau'_{l''} u_{l''}; g_t := b^+ + sum_m R_m^*(omega^+_m - d^#_m(omega^+_m) w^#_m).
At kept coordinates of types (K1), (K4) (q > 0) apply the shift of Theorem C Step 5 (Z6 referee Section 2): move omega^+-(k) by the
same x with vs x := (-1.5 gap^#/t - vs omega^-(k))_+, lambda_k |x| <= |tau_k - tau'_k| + lambda_k |Delta d| M; it leaves
omega^- - omega^+, Delta d^# and V' unchanged.  Then: two-piece admissibility at f^# and the second representation are those of
Lemma lem:windowtwopiece(a) (b^+ 1_{F^c} = chi V' z^#-signed, b^- 1_{F^c} = -(1-chi)V'); d-neutrality: d^#(omega^-) - d^#(omega^+) =
sum q^# tau' = Q^#_m(tau') = 0 (Step 3).  Estimates: as in Z3 Proposition T step (5) with K^#_* replaced by K_U: replacing (d, w, gap)
by (d^#, w^#, gap^#) costs C_f(t^{-1} + t^{-2} t) c(Delta) <= C theta_w t (Lemma 4.1), re-clamping costs (2/t) sum lambda|gap^# - gap| <=
C theta_w t; at dropped coordinates: pinned (Lemmas 3.1, 3.5, 3.6), and if the status changes between f and f^# the datum 0 is used
with error <= |tau| + lambda|Delta d| M (peak of f) or <= 2 lambda gap/t + |tau| + lambda |Delta d| M with gap <= b(w) (strict non-peak of
f, by the claim in the proof of Proposition prop:windowcert(c)); at (K4) coordinates omega^+ = omega_+ (no error) and the shift error;
Gamma: fix T3 of the Z3 referee.  This gives (i), (ii) with K_w <= C_f (1 + G**) (K_U + 1).  (iii): clamped coordinates are of kind [1];
(K2) have gap^# >= M^# u(w)/2 (Lemma 4.2(c)) and (K3) gap^# >= M^#/2, repair carriers fixed gaps: kind [2]; (K1), (K4) after the
shift: kind [3] (Z6 referee Lemma 2.1 / Y2 Lemma U'); |omega^+| <= 4/t, |tau_0|/lambda <= 12/t, and the repair amounts give
<= K_Q t Design(l) D(l)/u(w) <= 1/t (t in W(w), l large), so A_2 := 22.  QED
# Y1 part 5c — Corrections/generalizations to parts 5a, 5b (self-check)

## 5c.1 Window-level repair directions (generalizes (DR); replaces "compensated" in (Cmp_w), (NN_w))
**Definition (Rep^s_m at w).**  For a block m and s in {+-1}: there is rho in R^G_{>= 0} (G = class-G coarse carriers at w), ||rho||_1 <= 1,
with zero cost AT f^#_w (V(rho) z^#-signed, supported in K^#), supported on carriers that are strict non-peaks of f^#_w, with
gap^# >= M_m u(w)/4 at every member l'' with q^#_{l''} < 0, and with d-sums at f^#: sum_{m(l'')=m} q^#_{l''} rho_{l''} = s d,
d >= u(w)/Design(l), and sum_{m(l'')=m'} q^# rho = 0 for m' != m.
Block m is COMPENSATED AT w if (Rep^+_m) and (Rep^-_m) hold at w.
**Lemma 5.1' (fixed repair directions).  PROVED.**  If (DR^s_m) holds at f (Z4), then (Rep^s_m) holds at every clean w of level l >= l_f.
Proof.  Lemma 5.1 (u-values of repair carriers unchanged, d-sums s A_m/A^#_m and 0, zero cost at f^#), normalization by ||rho||_1 <= R_f:
d = A_m/(A^#_m R_f) >= u(w)/Design(l) for l large; repair carriers are fixed strict non-peaks of f with fixed gaps, which persist at f^#
(Lemma 4.2(c): fixed relative positions are robust for l large).  QED
Other sources of (Rep^s_m) at w: any single resonant G-carrier which is a strict non-peak of f^# with |q^#| >= u(w)/Design(l) of sign s
(and robust gap if s = -) — e.g. a near-threshold resonant swallowing-type peak converted by the threshold raise (q^# ~ Phi M/(mC)).
Revised hypotheses: (Cmp_w) every block is compensated at w or sigma-one-signed at w; (NN_w) in a sigma-one-signed block no kept
carrier has sigma q^# > 0, and if some kept carrier has sigma q^# < 0 then (Rep^sigma_m) holds at w.
Proposition 5.2, Step 3 (revised).  For a compensated block m: c := |Q^#_m(tau_0)|/d, tau' := tau_0 + c rho^{m,-sgn Q^#_m(tau_0)}; for a
sigma-one-signed block with Q^#_m(tau_0) != 0: sgn Q = -sigma by (NN_w) and tau' := tau_0 + (|Q|/d) rho^{m,sigma}.  The d-sums are
block-diagonal at f^# by definition, so all d-rows become exact; ||tau' - tau_0||_1 <= N K_Q t Design(l)/u(w); the repair amounts give
|omega| <= c rho_{l''}/lambda_{l''} <= K_Q t Design(l) D(l)/u(w) <= 1/t at the repair carriers for t in W(w), l large (K_Q t^2 Design D/u
<= C_f T_hi(w)^2 Design^2 u^{-4} -> 0), so A_2 := 22 works; members with q^# < 0 are of kind [2] (gap >= M u/4), members with q^# > 0 of
kind [3] after the shift (or kind [2]).  K_U is now K_g + 1 + G** V_w/t + N K_Q Design(l)/u(w).  Everything else in 5a is unchanged.

## 5c.2 Window arithmetic (constants of parts 3 and 5)
With D := D(l), u := u(w): K_g <= C D/u, K_d, K_P <= C_f D^3/u, K_O <= C_f D^5/u^2, V_w/t <= C_f l D^5/u^2, K_Q <= C_f G** l D^5/u^2,
K_U <= C_f G** l D^5 Design(l)/u^3 (the factor Design/u comes from the normalization d >= u/Design of (Rep)), and
K_w <= C_f (1 + G**)(K_U + K_P + 1) <= C_f Design(l)^3 u(w)^{-3}, because Design(l) = X^6 with X >= l D(l) G**(l).
This is why Definition 1 uses Q(w) := Design(l)^4 u(w)^{-omega(l)-8} (a first draft used Design(l) u^{-omega-4}, which does not
dominate Design^3): K_w/c_flat(w) <= C_f Design^3 u^{-4} = C_f Q(w) u^{omega+4}/Design <= C_f Q(w) u(w), hence n(w) c_flat/K_w >=
l 2^{l^3}/(C_f u(w)) -> infinity, and K_w T_hi(w) <= C_f Design^3 u^{-3} 2^{-l^3}/(l Q(w)) <= C_f 2^{-l^3}/l -> 0.  Theorem 1 only uses
Q >= Design and Q >= u^{-4}, so it is unaffected.  (E-e'): T_lo(w) <= 2^{-n(w)} <= 2^{-u(w)^{-4}}.

## 5c.3 Other checks done (all consistent)
* Pigeonhole is per level: each sub-window band is an open interval, each rate lies in at most one band.
* Fine carriers: sum_{l'>l} lambda <= b(w)^2/2 for every sub-window of level l (c_{l+1} <= b(l, M(l))^2), so fine perturbations of
  every coarse quantity are O(b^2), below every tiny threshold.
* Donor feasibility uses Design >= 2^{6 sigma(l)}; with the corrected Q(w) still T_lo(w)^3 <= 2^{-18 sigma(l)}.
* Statuses at f^#: every KEPT coordinate is a strict non-peak of f^# (robust ones by Lemma 4.2(c); (K4) only in raised blocks, where
  they become strict non-peaks; (K3) has rho^# <= C b); DROPPED coordinates may change status, which is harmless (5a Step 5).
* (SP_w), (Cmp_w), (NN_w) are statements about f at level l and the explicit companion f^#_w; they involve no rate thresholds beyond
  u(w), b(w), which are design numbers.
# Y1 part 5b — The master theorem for D_X, corollaries, and the exact residual list

## 5.3 Theorem E' (window-dependent constants).  PROVED.
Z3 Theorem E holds with (E-b) read with the coordinate kinds [1]-[3] of Proposition 5.2(iii), with A_2 fixed and gamma_B = gamma(w_j)
allowed to depend on j, and with (E-d), (E-e) replaced by
 (E-d') K_j T_j -> 0 and n_j >= 48 rho^2 K_j/(c_{flat,j}(1 - rho^2)) for large j, c_{flat,j} := c_flat(A_2, gamma(w_j)) >= c_0 gamma(w_j)/A_2;
 (E-e') eps_j := p*(f_j - f) <= min{c_{flat,j}^2 (1-rho^2)(T_j 2^{-n_j})^2/(24 rho^2), (1-rho^2) r_0^2/6}  (r_0^2 = 1 - rho^2).
Proof.  Lemma U (Z3) extends to kind [3] (inward-only) coordinates: Z6 referee Lemma 2.1 (block step: ||W||_inf = (1 - rd)M because
inward coordinates move toward 0 and c_flat A' <= M/4; first-order term s omega(k) alpha(k) = 0 at strict non-peaks).  In Lemma U the
constants A_2, gamma_B enter only through upper bounds on c_flat (c_flat <= gamma_B/(2A_2), c_flat <= C_min/(2A_3), c_flat A_2 <= M_min/4,
relative errors O(A_3 c_flat)); t_1 and j_0 are constrained only by r^4-terms and the convergence of the scalar and transfer data of
f_j -> f (Z4 Step 7, verified by the Z4 referee, Section 8).  In the proof of Theorem E (Z3 2.2), after j is fixed, c_flat enters only
through (A), through I_r := {i : c_flat t_i < rho|r|} with sum_{I_r} t_i < 2 rho|r|/c_flat, through 2rho^2 K r^2/(c_flat n) <= (1-rho^2)r^2/24,
and through eps_j < theta_j rho^2 r^2/c_flat^2 when I_r != {} — exactly (E-d'), (E-e').  Corollary cor:D1 is applied at f_j to the averaged
data, which are two-piece data at f_j (kind-[3] coordinates are strict non-peaks of f_j).  QED  (Same statement: Y2 Theorem E'.)

## 5.4 MASTER THEOREM (design D_X).  PROVED (from Theorems 1, 2, E', Lemmas 3.1-3.6, 4.1-4.3, 5.1, Proposition 5.2).
Let T = D_X, N >= 1, and f in S_{p_N^*} with finite base support F.  Suppose that for infinitely many levels l there is a clean
sub-window w(l) of level l (one exists at EVERY level, Theorem 2) at which (SP_w), (Do_w), (Cmp_w) and (NN_w) hold.
Then f in Rec: (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f).
NO RATE CONDITION is imposed: rooms of signature sets (good or slaved), rooms at target coordinates, margins (weak, degenerate),
gaps (near-threshold carriers of both types), d-coefficients and their relative sizes, the number of swallowed carriers, slaving,
(H1), (MS) and contact sets are arbitrary; at each used window every rate is either robust (absorbed by the design) or tiny
(closed, shifted, pinned, or compensated).
Proof.  Fix g in C(f), rho in (0,1), eta_0 in (0,2] with rho^2(1 + eta_0) <= (1 + rho^2)/2, kappa_0 := (sqrt(1 + eta_0/2) - 1)/2, eta <= eta_*
with eta_Gamma(eta) <= 1 and sqrt(1 + eta_Gamma(eta)) <= 1 + kappa_0/2.  Along the given levels l_j -> infinity take w_j := w(l_j),
f_j := f^#_{w_j} (part 4), T_j := T_hi(w_j), n_j := n(w_j), and for each dyadic t in W(w_j) the functional g_{j,t} := g_t of
Proposition 5.2 (built from a two-sided decomposition of g at f at scale t).  Check Theorem E':
 * supp a_j = F; f_j -> f since p*(f_j - f) <= theta_{w_j} T_lo(w_j)^2 -> 0 (Lemma 4.1).
 * (E-a): b^+-(xi_j) = 0, t||b^+-||_1 <= A_0, and Gamma^{(j)}_w <= (1 + kappa_0/2 + C theta_{w_j} + K_{w_j} t)^2 <= 1 + eta_0/2 once
   C theta_w + K_w T_hi(w) <= kappa_0/2 (true for large j, below).  (E-b): Proposition 5.2(iii), A_2 fixed, gamma(w_j) = min M u(w_j)/4.
 * (E-c): p*(g - g_{j,t}) <= K_{w_j} t.
 * (E-d'): K_w <= C_f Design(l)^3 u(w)^{-3} (Y1_part5c 5c.2) and c_flat(w) >= c_f u(w), so with Q(w) = Design(l)^4 u(w)^{-omega(l)-8}:
   K_w/c_flat(w) <= C_f Design^3 u^{-4} = C_f Q(w) u^{omega+4}/Design <= C_f Q(w) u(w), while n(w) >= l 2^{l^3} Q(w); hence
   n(w) c_flat(w)/K_w >= l 2^{l^3}/(C_f u(w)) -> infinity.  K_w T_hi(w) <= C_f Design^3 u^{-3} 2^{-l^3}/(l Q(w)) <= C_f 2^{-l^3}/l -> 0.
 * (E-e'): eps_j <= theta_w T_lo(w)^2 with theta_w = C_f T_lo(w) log(1/T_lo(w)), and c_flat(w)^2 >= c_f u(w)^2, while T_lo(w) <= 2^{-n(w)} <=
   2^{-u(w)^{-4}}; so theta_w <= c_f u(w)^2 (1-rho^2)/(24 rho^2) for large j.  Also eps_j <= (1-rho^2)r_0^2/6 eventually.
Theorem E' gives (f, rho g) in cl NA; rho < 1 was arbitrary.  QED

## 5.5 Corollaries
**Corollary M1 (maximal contact).  PROVED.**  Let F be finite and z = eps_0 on N \ F.  Then f in Rec provided, for infinitely many
levels, at a clean sub-window w: every block is compensated at w (e.g. (DR) of Z4) or sigma-one-signed at w, and in every
sigma-one-signed block no coarse carrier l'' with 0 < sigma q_{l''} and rho_{l''} <= b(w) exists, and if one with sigma q_{l''} < 0,
rho <= b(w) exists then (Rep^sigma_m) holds at w.  In particular weak and DEGENERATE swallowing-type peaks, near-threshold carriers of both types, and all rooms are harmless at
maximal contact (cf. Z4 Remark 5.5 and Z6 referee Proposition R1, where degenerate positive peaks at maximal contact were open).
Proof.  Every carrier is exactly swallowed (class G, r^nat = 0) and T(l) \ F consists of contacts, so (C1), (C2) are void; hence
u_{l''}(zhat^#) = u_{l''}(zhat) for every non-donor coarse l'' and q^# = q A/A^#: exactly d-neutral carriers stay exactly d-neutral, and
(NN_w) is the stated condition.  (SP_w): by Z4 Lemma 5.0, every block has non-degenerate peaks with w = eps_0 M (swallowing type,
margin >= q_0/4: a LOWER source (L2) once u(w) is below the fixed relative margin) and with w = -eps_0 M (anti type: UPPER (U2)).
(Do_w): the anti-type peaks are donors (part 4.1).  QED
**Corollary M2.**  Let F be finite.  Suppose every block m has fixed repair directions of both signs ((DR^+_m) and (DR^-_m), nonzero),
every block has an exactly swallowed anti-type peak (UPPER source and donor) and an exactly swallowed swallowing-type peak with
positive margin (LOWER source).  Then f in Rec.  PROVED (Theorem 5.4: by Lemma 5.1' every block is compensated at every clean w of
large level, so (Cmp_w) holds and (NN_w) is void; (SP_w) and (Do_w) hold by the fixed peaks).  Compared with Z4 Theorem A'' (read
for D_X), the hypotheses (H3) (no degenerate swallowing-sign peaks) and the growth condition (W_inf) (margins, gaps, target rooms,
good rooms) are dropped; a donor replaces (H3).
**Corollary M3 (what the master theorem adds to Round 5).**  For D_X the rate items of the consensus core (r) of ADDENDUM 5 (rooms of
good sets incl. approximate swallowing (O1)(i), margins of non-rigid swallowing-type peaks K_P, gaps gamma_B of kept q < 0 carriers,
rooms gamma_T at target coordinates, relative Farkas/d-coefficients K_nn in the COMPENSATED and in the "opposite-sign" direction of
one-signed blocks) are no longer obstructions; item (d) (degenerate non-rigid swallowing-type peaks) is removed whenever the block has
a donor (always at maximal contact).  PROVED (by Theorem 5.4: each was a failure of a growth condition that 5.4 does not need).

## 5.6 The exact residual list (F finite; design D_X).  OPEN.
Lemma Z (density for p_N) for D_X can fail only at pairs (f, g), g not window-pinned, with f such that at all but finitely many
levels, EVERY clean sub-window w violates one of:
 (n)  [directional nearly neutral resources] a sigma-one-signed block has a KEPT carrier (rho^#-tiny strict non-peak) with d-coefficient
      of sign sigma at f^#_w (or of sign -sigma without (Rep^sigma_m) at w).  Sources: carriers nearly neutral at f with the block's own sign
      (the K_nn rate in its uncompensable direction), Z3 Lemma 1.4 carriers (d-neutral, approximately resonant: q^# = r^nat/A^# > 0,
      Lemma 4.3), d-neutral kept carriers whose targets meet (C2)-raised near-contacts.  Removing it needs either LOWERING a z-signed
      functional (impossible with banks for diagonal U, Y4 Prop. 2.8; with supp a fixed only |F| - 1 Hilbert directions), or a pinning
      statement of Conjecture G type for nearly neutral carriers.
 (m)  [mixed blocks] a block is neither compensated at w ((Rep^+) and (Rep^-)) nor one-signed at w (Y2 Theorem M, unrefereed, reduces this
      to ray rates and a d-forced-face Farkas constant; multi-block rays remain, Y4 (m')).
 (d)  [aligned corner] a block that is not one-signed and contains near-threshold swallowing-type carriers has no donor: every
      non-degenerate peak c of the block with S_c ∩ F = {} has infinitely many s in S_c with vs_c z_s > 0 (coordinates of its OWN
      sign: contacts or free).  Then no signature move of a peak raises the threshold with a design-controlled range.  (The Y2 referee's
      "target donors" (free target coordinates with positive one-sided threshold derivative) would shrink this further; not used here.)
 (h)  [shift pinning] (SP_w) fails: some block lacks an UPPER or a LOWER source (Y2 Theorem H, unrefereed: shift costs).
 (O4) F infinite (Z5 and Y3, separate).
Remarks.  (3) (SKETCH) In (n) the imbalance to be repaired is TINY: |Q^#_m(tau_0)| <= sum_{kept} |q^#| tau'_0 <= C l b(w) D(l)/t, so a repair
direction with |d-sum| ~ Phi M/(mC) needs amounts c <= C l b D^2/t, i.e. |omega| <= C l b D^3/t, and the one-sided expansion at a q < 0
member then needs only gap^# >= C l b D^3 (not a robust gap).  Hence a RESONANT near-threshold anti-type peak, converted by a threshold
raise into a strict non-peak with gap^# ~ M delta ~ T_lo(w)^3 >> l b D^3, can serve as a negative repair direction for (n).  This shrinks
(n) to blocks without such carriers; the bookkeeping (a second kind of (Rep) with amount-dependent gap) is routine but not written.
(1) Nothing in (n), (m), (d), (h) is a rate: each is a structural/directional property of the configuration at a level,
which no design can absorb by lengthening windows.  (2) A counterexample to density for D_X would have to live in one of these
classes; nothing found here points to one (all single-module mates are certificates, Z6 6.2; the directional obstruction (n) concerns
the METHOD: exact data at a companion with the same base part).
