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

**Remarks.** (1) Compared with Y4's D^PW, D_X adds 2^{sigma(l)} (1+|T(l)|) G**(l) to the design factor and takes
c_{l+1} <= b(l,M(l))^2 instead of T_lo(l,M(l))^3: fine carriers then perturb every coarse rate by O(b^2) only (used in part 4).
(2) The order of quantifiers is the usual one: D_X is fixed before f; every f-dependent quantity is either a FIXED f-constant
(absorbed by l 2^{l^3} -> infinity) or a RATE, i.e. a number attached to a design-countable object (part 2).
