# V1 part 1 — The unified design D_Omega (diagonal base): definition, admissibility, N-independence, survival

Setting and numbering: paper/martin_density_note.tex (Sections 1, 7, 8), Round 5 (Z3-Z6 with referee fixes), Round 6
(Y1-Y4 with referee fixes).  Finite block sets I = {1..N}, p = p_N; D_Omega is ONE operator for all N (Lemma lem:martintail).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.1 The base
H := l_2 with orthonormal basis (k_j)_{j >= 1}, s_j := 2^{-j}, and U : H -> c_0, (Uh)(j) := s_j <h, k_j>.  Then U is compact
(s_j -> 0), U^* e_j^* = s_j k_j, U^* a = sum_j a_j s_j k_j is injective on l_1, so U has dense range; ||U|| = 1/2.  By
Proposition prop:smooth(c) every compact dense-range U gives NA(q) = c_00, and Martin's construction and all of Sections 1-8 of the
note hold for any such U (the base is fixed before T; it enters (D0) only through ||U||).  We call U the DIAGONAL BASE.
Two identities used throughout (PROVED, direct computation): for b in l_1 and j notin supp b,
   <U^* b, k_j> = s_j b_j = 0 ;      for A = a + sum_{j in J} m_j e_j^*  with J ∩ F = {}:
   U^*A = U^*a + X,  X := sum_{j in J} m_j s_j k_j,  X ⊥ U^*a,  ||U^*A||^2 = nu^2 + ||X||^2.                       (1.1)

## 1.2 Definition of D_Omega
(D0) As in Definition def:SLD (ladder bijection j with j(k,m) < j(k',m) for k < k'; targets y^(i) in c_00 ∩ S_{q*} dense in S_{q*},
y^(1) := e*_{j0}/q*(e*_{j0}); a sequence (i_r) in which every integer occurs infinitely often; h_l := sum_{s in S_l} 2^{-s} e_s^*,
delta_l := min{2^{-l}, (4(1+||U||)||h_l||_1)^{-1}}), with the concrete signature sets
   (D0')  j0 := 1,   S_l := {2^l (2i+1) : i >= 1}   (l >= 1),
which are pairwise disjoint, infinite, avoid j0, and have BOUNDED GAPS: consecutive elements of S_l differ by G_l := 2^{l+1}.
Put v_l := delta_l h_l/n_l (so u_l = v_l on S_l by (P1)), v_l(s) = delta_l 2^{-s}/n_l.
(D1) Recursively in l = 1, 2, ...: given c_l (c_1 := 1), a vector y in c_00 is ALLOWED at l if
   (a) supp y ∩ S_{l'} = {} for every l' >= l;   (b) 2c_l <= 2^{-2s} c_{l'} delta_{l'} for l' < l and s in supp y ∩ S_{l'};
   (c) supp y ∩ S_{l'} ⊂ [1, l] for every l' < l          (Y3's rule, design D_sigma).
y_l := y^(i_{k(l)}) if this target is allowed at l, y_l := y^(1) otherwise (y^(1) is allowed at every l: supp y^(1) = {1} meets no S).
n_l := q*(y_l + delta_l h_l), u_l := (y_l + delta_l h_l)/n_l, delta°_l := delta_l ||h_l||_1/n_l, Lambda°(l) := prod_{l''<=l}(1 + 2/delta°_{l''}).
At stage l (after y_{l''}, u_{l''}, c_{l''}, l'' <= l, are fixed) the following DESIGN QUANTITIES are computable:
 * T(l) := union_{l''<=l} supp y_{l''} (finite), s_max(l) := max(T(l) ∪ {1}), sigma(l) := max_{l''<=l} min(S_{l''} ∩ (s_max(l), inf));
 * m^nat_{l''}(l) := ||v_{l''} 1_{S_{l''} \ ([1,l] ∪ T(l))}||_1 > 0, D(l) := 1 + sum_{l''<=l} (1/m^nat_{l''}(l) + 1/Phi_{l''})  (D''', Y1);
 * delta_min(l) := min_{l''<=l} delta_{l''},  G(l) := max_{l''<=l} G_{l''} = 2^{l+1};
 * G*(l) (Z4, configurations over all subsets of [1,l]), H_comb(l) (Z6), G**(l) (Y1 1.2: generalized configurations, arbitrary
   contact types on T(l), all drop sets P), Xi^Y(l) := [l H_comb G** D]^8 (l 2^{l^3} Lambda° G**)^5 (Y2, design D^Y);
 * the PATTERNS of level l (2.3 below: generalized configurations kappa = (U, P, eps, F', type) of level l), for each pattern its
   zero-cost cone C(kappa) (a pointed polyhedral cone in [0,inf)^U defined by design numbers u_{l''}(j), j in T(l)), the finite set
   Ext(kappa) of its extreme rays r normalized by ||r||_1 = 1, and
      H_tune(l) := max{1, max_{kappa, Sigma} (#Sigma)^{1/2} ||R_Sigma^+||_2}  where, for a set Sigma of COMPONENTS (r, m) (r in Ext(kappa), m a
      block meeting supp r), R_Sigma is the matrix with one row (r(l''))_{l''<=l} 1_{m(l'')=m} per component, and R^+ its
      Moore-Penrose pseudo-inverse (R_Sigma := 0 gives ||R^+|| := 0);
 * omega(l) := the number of RATE OBJECTS of level l (1.3 below).
Every one of these is N-free: blocks enter only as the blocks m(l'') of carriers l'' <= l (at most l of them).
DESIGN FACTOR:
   Design(l) := [ l 2^{l^3} 8^{sigma(l)} 2^{s_max(l)} 2^{G(l)} delta_min(l)^{-1} Lambda°(l) (1+|T(l)|) D(l) G*(l) H_comb(l) G**(l) H_tune(l) Xi^Y(l) ]^6.
SUB-WINDOWS: M(l) := omega(l) + 1 sub-windows w = (l,i), 1 <= i <= M(l), ordered lexicographically (w^- = predecessor), and
   u(1,1) := 1/4,   u(w) := b(w^-) (w != (1,1)),   Q(w) := (4 Design(l)/u(w))^{omega(l)+20},   n(w) := ceil(l 2^{l^3} Q(w)),
   T_hi(w) := min{T_lo(w^-), 2^{-l^3}/(l Q(w))} (T_lo((1,1)^-) := 1),   T_lo(w) := 2^{-n(w)} T_hi(w),   b(w) := T_lo(w)^4/(l Design(l)),
   c_{l+1} := min{c_l/4, b(l, M(l))^2, (delta_{l+1} ||h_{l+1}||_1)^2}.
Band(w) := (b(w), u(w)); W(w) := [T_lo(w), T_hi(w)] with its n(w) dyadic scales T_hi(w) 2^{1-i}, 1 <= i <= n(w).
(D2) T e_{k,m} := c_{j(k,m)} u_{j(k,m)}.
The recursion is well defined: every quantity of level l uses only data of index <= l and c_l; c_{l+1} is fixed last (delta_{l+1}, h_{l+1}
are fixed in (D0)).

## 1.3 Rate objects of level l (the rate scheme of D_Omega)
For f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu) (Proposition prop:forced), F finite or not, put for a carrier
l'' = j(k,m): val_{l''} := eps_{l''} u_{l''}(zhat) when a sign eps_{l''} is attached (below), rho_{l''} := |u_{l''}(zhat)| m/(Phi_{l''} theta_m)
(Y1 part 2; theta_m := A_m M_m/C_m, A_m := |R_m^** zhat|_m; k is a peak iff rho >= 1, Lemma T).  The rate objects of level l and
their f-dependent values (numbers in [0, infinity]) are:
 (R1) l'' <= l: rate := r^nat_{l''}(l)/||v_{l''} 1_{S^nat_{l''}(l)}||_1, S^nat_{l''}(l) := S_{l''} \ (F ∪ T(l)), r^nat := min_{sigma=+-1}
      sum_{s in S^nat} v_{l''}(s)(1 + sigma z_s)   [room off all coarse targets; Y1];
 (R2) j in T(l): rate := 1 - |z_j| (rate := 1 if j in F)   [target room];
 (R3) l'' <= l: |rho_{l''} - 1|   [threshold distance];     (R4) l'' <= l: rho_{l''}   [relative position];
 (R5) (kappa, r, m), kappa a pattern of level l, r in Ext(kappa), m a block meeting supp r:
      rate := |sum_{l'' in supp r, m(l'')=m} r(l'') eps_{l''} u_{l''}(zhat)| / max_{l'' in supp r, m(l'')=m} Phi_{l''}    [ray d-COMPONENT];
 (R6) pi a SHIFT PATTERN of level l (2.4 below): rate := c_pi(f), the shift cost of pi   [shift cost];
 (R7) (kappa, J), J a set of extreme rays of C(kappa): rate := smallest singular value of the matrix whose columns are the vectors
      (sum_{l'' in supp r, m(l'')=m} r(l'') eps_{l''} u_{l''}(zhat)/Phi_max(r,m))_m, r in J   [joint ray objects; for V2/Y4].
(The signs eps in (R5)-(R7) are those of the pattern.)  omega(l) := l + |T(l)| + 2l + #(R5) + #(R6) + #(R7): a finite number
computable at stage l and independent of N and of f.

## 1.4 Theorem 1' (D_Omega).  PROVED.
(a) T is admissible (Definition def:admissible) and satisfies (P1), (P2) of Theorem thm:SLD; more precisely
    sum_{l'>l} c_{l'} <= 2c_{l+1} <= 2 b(l,M(l))^2 and sum_{l'>l} lambda_{l'} <= b(l,M(l))^2/2.
(b) For every sub-window w = (l,i): l 2^{l^3} Q(w) T_hi(w) <= 1, n(w) >= l 2^{l^3} Q(w) >= l 2^{l^3} Design(l), T_hi(w^+) <= T_lo(w);
    b(w) < u(w) and u(w^+) = b(w), so the bands Band(w) are pairwise disjoint; sum_{l'>l} lambda_{l'} <= b(w)^2/2 <= T_lo(w)^8.
(c) D_Omega does not depend on N.
(d) (Survival.)  For D_Omega, every N and every sub-window w of level l read as "the window of level l", the following refereed
    results hold: all of Section 8 of the note; Z3 Theorem E, Lemma U, Lemmas 3.1, 3.2 (referee's "flipped"), Proposition T with
    fixes T2-T6, Corollary 3.4, Theorems 5.3, 5.4, Propositions 4.1, 4.2; Z4 Theorem A'' and Corollaries 4.2, 5.4 (both forms, by the
    third term of c_{l+1}); Z5/Y3 (infinite F) T1-T12, R1, Theorems 2.1, 2.2, 3.5, 4.1, 5.1, 6.1; Z6 Theorems C, U', V, Proposition P,
    Corollary V.1, Proposition R1; Y1 Theorems 1, 2, Lemmas T, T2, T3, 3.1-3.6, 4.1-4.3, 5.1, 5.1', Proposition 5.2, Theorem E', Master
    Theorem 5.4, Corollaries M1, M2; Y2 Lemmas T, U', Theorem E', Proposition Q, Corollary Q', Theorem P (D''' form), Lemma 3.1,
    faces, Lemmas 4.1, 4.2, Proposition 4.3, Theorems M, H, Y, Corollary Y.1; Y4 Lemma 1.5, Theorem 1.6, Corollary 1.7 (for the rate
    scheme (R1)-(R7)), Lemma 1.8, Lemmas 2.2-2.6, Proposition 2.7, Lemma 2.9; Y4-referee A.3, C.1-C.7.
Proof.  (a) Theorem thm:SLD uses (D1) only through allowedness (a), (b) and c_{l+1} <= c_l/4; rule (c) only REMOVES targets, and every
finitely supported target satisfies (a), (b), (c) at every large l (supp y^(i) meets finitely many S_{l'}; c_l -> 0; l >= max supp y^(i)),
so (T-d) holds as there (Y3 Proposition 3.3); (T-a)-(T-c), (P1), (P2) are unchanged.  c_{l+1} <= c_l/4 gives sum_{l'>l} c_{l'} <=
(4/3)c_{l+1}, and lambda_{l'} <= c_{l'}/4.
(b) Immediate from the definitions: Q(w) >= Design(l) >= 1, T_hi(w) <= 2^{-l^3}/(lQ(w)), n(w) >= l 2^{l^3} Q(w).  Bands: u(w) <= 1/4
for all w (u(w) = b(w^-) <= T_lo(w^-)^4 <= 1/4), and n(w) >= Q(w) >= (4/u(w))^{20} >= 16/u(w), so b(w) <= T_lo(w)^4 <= 2^{-4n(w)}
<= 2^{-64/u(w)} < u(w); u(w^+) = b(w) by definition; consecutive open intervals of a decreasing sequence are disjoint.  Finally
b(l, M(l)) <= b(w) for every w of level l and c_{l+1} <= b(l,M(l))^2.
(c) Every ingredient of 1.2-1.3 is N-free (configuration, pattern and tuning constants are maxima over all subsets of [1,l]; rate
objects are indexed by carriers <= l, coordinates in T(l), patterns and shift patterns of level l).
(d) The note states after Theorem thm:SLD (re-checked by the Round 5-6 referees for SLD_G, D''', D^Y, D^PW, D_X, D_sigma) that all
listed results use T only through (T-a)-(T-d), (P1), (P2), the window conditions (P3) and allowedness (a), (b) (Y3's results
also (c) and bounded gaps, which D_Omega has).  In every window proof (Y1 Theorem 1(d), Y4 Lemma 1.5(c), Z3-ref Lemma 4.1.1) the
window enters only through (i) the dyadic scales of ONE window, (ii) conditions "T_hi x (f-dependent factor) -> 0" and
"n/(f-dependent factor) -> infinity" along the windows used, the factor being at most C_f^{l^2} times a product of design factors of
level l (Lambda°, Xi' and Xi^Y, G*, G**, H_comb, D(l), 2^{s_max}/delta_min, 2^{G_l}, H_tune) and, for the pigeonhole designs, of at
most omega(l)+3 robust rate factors (<= (4 Design/u)^{omega+3}), (iii) the box bound sum_{l'>l} |Delta theta_{l'}| <= 6 sum_{l'>l}
lambda_{l'}/t <= 6t^2 (needs sum_{l'>l} lambda_{l'} <= T_lo^3), (iv) T_hi(next) <= T_lo(previous).  By (a), (b): Design(l) dominates
every listed design factor (Design_X of Y1, Design^PW of Y4-ref A.3, Xi^Y of Y2, Xi' of D''', the SLD_G factor (l2^{l^3}Lambda°G*)^6),
Q(w) dominates (4 Design/u)^{omega+3} and Y1's Design^4 u^{-omega-8} (omega(l) >= 3l + |T(l)|), and C_f^{l^2}/2^{l^3} -> 0; Z3
Theorem E, Lemma U, Lemma 3.1 and Y4 Lemmas 2.2, 2.3 hold for every admissible T and every base.  The Y4-ref results C.1-C.7 need the
diagonal base, bounded gaps (D0') and H_tune(l) in Design(l), which D_Omega has.  Theorem 1.6 of Y4 / Theorem 2 of Y1 (pigeonhole)
need M(l) = omega(l)+1 disjoint bands: (b).  QED

Remarks.  (1) D_Omega contains: D_X of Y1 (sub-windows, Design_X factors, rate objects (R1)-(R4)); the constants Xi^Y of D^Y (Y2);
D_sigma's bounded gaps and rule (c) (Y3); the Y4-referee fixes (2^{s_max}/delta_min, 2^{G_l}, H_tune, Q(w) dominating
(4Design/u)^{omega+3}; u_R is only needed for the explosive design, which D_Omega replaces by the pigeonhole); the diagonal base and
the private banks/pull coordinates (every far coordinate of every S_l is available, by (D0')).  (2) As usual D_Omega is fixed before
f, g, rho; every f-dependent quantity used below is either a FIXED f-constant (absorbed by l 2^{l^3} -> infinity) or the value of a
rate object of level l (absorbed or exactified at a clean sub-window).
