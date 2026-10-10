# V1 notes (Round 7): one unified design D_Omega, the ASSEMBLY theorem, the aligned corner, and MASTER THEOREM II

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; numbering and notation as there), Round 5 (Z3-Z6 + referee fixes), Round 6
(Y1-Y4 + referee fixes, incl. Y4_ref_notes C.1-C.8).  Finite block sets I = {1..N}, p = p_N; F = supp a FINITE.  The base U is chosen
DIAGONAL (U^* e_j^* = 2^{-j} k_j), which is admissible (any compact dense-range U).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Part files: V1_part1..5.md (assembled below, after this head); reading digest V1_part0.md; scripts V1_work/*.py.
No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN for every admissible T (including D_Omega).

## 0. Summary
(1) DESIGN D_Omega (part 1, Theorem 1'; PROVED: admissible, N-free, all listed refereed theorems survive).  SLD with bounded-gap signature
sets S_l = {2^l(2i+1)} and Y3's allowedness rule (c); one design factor Design(l) dominating every design constant of Y1 (D_X), Y2 (Xi^Y),
Y4-ref (2^{s_max}/delta_min, 2^{G_l}, H_tune) and the bank/pull constants (8^{sigma(l)}/delta_min); a rate scheme (R1)-(R7) = Y1's rooms,
target rooms, threshold distances, relative positions + RAY d-COMPONENTS of all zero-cost cones of level l + SHIFT COSTS of all shift
patterns + joint ray objects; M(l) = omega(l)+1 sub-windows with pairwise disjoint bands; Q(w) = (4 Design/u)^{omega+20}.
(2) ASSEMBLY (parts 2-4; PROVED).  At every clean sub-window w (Theorem 2') ONE companion f^#_w = row (A^#, z^#) carries all
exactifications: (C1) close class-G rooms on S^nat, (C2) close tiny target rooms, (C3) a DONOR RAISE of every block containing kept
near-threshold swallowing-type carriers, by a z-move or a BANK at a robust-margin peak (such a peak exists in EVERY block, Lemma D),
(C4) EXACT neutralization of every tiny ray d-component by one least-norm linear solve realized by pulls + private banks (Lemma TU,
explicit solution).  Proved: cost <= C_f Design T_lo^3 log(1/T_lo) = o(T_lo^2) (Lemma CO); no slaving / closure (Lemma NS); status stability
(BS) under the O(Delta) threshold drift, via the raise buffer Lam = T_lo^3 >> drift Design b (Lemma ST); robust rates stay robust (Lemma RR);
transplant to exact d-NEUTRAL two-piece data at f^#_w with design-controlled constants, via ray removal (Proposition TR); Theorem E''
(Theorem E with window-dependent constants and banked + pulled supports).
(3) MASTER THEOREM II (4.3; PROVED).  For D_Omega, F finite: f in Rec as soon as at a clean sub-window of infinitely many levels
(SH_w) [shift sources, or a robust shift cost] and (VR_w) [every extreme ray of the zero-cost cone has at most one robust d-component] hold.
No donor, compensation, one-signedness, nearly-neutral, rate or growth hypothesis.  Corollaries: N = 1 (only (SH_w) needed); maximal
contact (only (VR_w) needed; for N = 1 unconditional).
(4) ALIGNED CORNER (D): EMPTY for D_Omega (Corollary AC; PROVED): banks at the peak's own-sign far contacts push it outward (diagonal base).
Lemma IP (PROVED): "far pulls on the peak itself" — pushing near-threshold coordinates inward by >= 4b(A+theta) in nu-units raises theta and
makes them strict non-peaks (used only as an alternative tool).
(5) RESIDUAL LIST (5.3; exhaustive for Master Theorem II): f notin Rec only if, at all but finitely many levels, EVERY clean sub-window has
(B_w) a GENUINELY MULTI-BLOCK RAY (an extreme ray of C(kappa(w)) with robust d-components in two blocks) or (C_w) a COHERENT SHIFT RESONANCE
(a source-deficient block with TINY shift cost c_{pi(w)} <= b(w)).  (D) = {}.  (E) infinite F: outside.

## 0.1 Results and labels
| # | Statement | Label | Where |
|---|---|---|---|
| 1 | D_Omega: admissible, N-free, disjoint bands, (P1)-(P3) on sub-windows; survival of the listed refereed results | PROVED | part 1, Thm 1' |
| 2 | Clean sub-windows at every level for the scheme (R1)-(R7) | PROVED | part 2, Thm 2' |
| 3 | Lemma D: every block has a coarse robust-margin peak at every clean w of large level (donor candidate) | PROVED | 2.4 |
| 4 | Lemma 3.4' (sources half by half), Lemma S (shift pinning by a robust shift cost; I_up ∩ I_lo = {}) | PROVED | 2.5 |
| 5 | Patterns, zero-cost cones, ray d-components; one-signed blocks carry no robust component | PROVED | 2.6 |
| 6 | Lemma B (masses off the support, diagonal base: exact formula (3.1)) | PROVED | 3.1 |
| 7 | Lemma DR (donor raise by z-move or bank; first-order raise, second-order side effects) | PROVED | 3.3 |
| 8 | Lemma TU (exact two-sided tuning by pulls + banks, explicit solution; re-proves Y4-ref P4 with design constants) | PROVED | 3.4 |
| 9 | Lemma CO (cost o(T_lo^2); data bounds; size of the tuning eta <= Design b) | PROVED | 3.5 |
| 10 | Lemma ST (status table; (BS) under threshold drift; all kept carriers strict non-peaks of f^#) | PROVED | 3.6 |
| 11 | Lemma NS (no slaving; exactified set closed), Lemma RR (robust rates stay robust; tiny components exactly 0) | PROVED | 3.7, 3.8 |
| 12 | Proposition TR (transplant: exact d-neutral two-piece data at f^#_w; K_w <= C_f Design u^{-4}; kinds [1]-[3]; supports) | PROVED | 4.1 |
| 13 | Theorem E'' (Theorem E with window-dependent constants, banked and pulled supports) | PROVED | 4.2 |
| 14 | MASTER THEOREM II and Corollaries M-II.1 (N = 1), M-II.2 (single-block rays), M-II.3 (maximal contact) | PROVED | 4.3 |
| 15 | Corollary AC: aligned corner empty for D_Omega | PROVED | 5.1 |
| 16 | Lemma IP (inward push of near-threshold coordinates raises theta) | PROVED (+num.) | 5.2 |
| 17 | Residual list (B), (C); exhaustiveness for Master Theorem II | PROVED (logical) | 5.3 |
| 18 | Union with Y1 5.4 (with (SH_w) for (SP_w)) covers doubly-robust rays through compensated blocks | PROVED (by Lemma S + Y1) | 5.3(3) |
| 19 | (B) genuinely multi-block rays; (C) coherent shift resonance; (E) infinite F; Lemma Z; density | OPEN | 5.4 |

## 0.2 Refereed results used (dependency list)
Note (refereed): Lemmas lem:threshold, eq:margin, lem:bookkeeping, lem:algebra, prop:forced, prop:smooth(c), rem:lemmaZ(c), def:twopiece,
cor:D1, def:SLD, thm:SLD, lem:twosided, lem:smallness, lem:budget, lem:suplevel, lem:box, lem:finitebase, def:windowcert,
prop:windowcert (claim in (c)), lem:phicalc, lem:switchbudget, lem:split, lem:peakshift (eq:peakshift, eq:didentity), lem:windowtwopiece
(structure), lem:onesidedtransfer, lem:persistence, lem:martintail, thm:reductionZ.
Z3 (refereed): Theorem E, Lemma U, Lemma 3.1 (cost; also as extended in Y4 Lemma 2.2), Lemma 3.2 (referee's "flipped"), Proposition T
step (5) with fixes T2-T6 (structure of the transplant).
Y1 (refereed): Theorem 1, Theorem 2, Lemmas T, T2, T3, Lemmas 3.1-3.6 (pinning; constants per Y1-ref m2, m5), Proposition 5.2 (structure),
Theorem E', kind [1'] (Y1-ref 4), shift trick (Y1-ref (d)), donor bookkeeping (Y1-ref m3).
Y2 (refereed): Lemma T(c),(d),(e), Lemma U', Theorem E', Lemma 5.1/Proposition 5.2 (shift cost; ported as Lemma S), generalized
configurations / G**, D^Y factor Xi^Y.
Y3 (refereed): design D_sigma (Proposition 3.3).
Y4 (refereed): Lemma 1.8 (ray removal), Lemma 2.2 (cost of tuned rows), Lemma 2.3 (banked Lemma U / Theorem E), Theorem 1.6 (pigeonhole).
Y4-ref (C.1-C.7, proved by the Y4 referee, NOT independently refereed): only re-verified parts are used — P1 (pull effect: Lemma B here),
P2 (pulled support in Lemma U: re-verified in Theorem E''), P3 (data at pulls: Proposition TR(iv)), P4 (tuning: re-proved as Lemma TU).

## 0.3 How the task items are answered
(1) Part 1: D_Omega with all requested features (D_X, Xi^Y, D_sigma's bounded gaps and rule (c), Y4-ref fixes, diagonal base with private
bank and pull coordinates); Theorem 1' (admissibility, N-independence, survival list).
(2) Parts 2-4: the companion f^#_w carries (C1), (C2), (C3) [donor raise: z-move or BANK on a robust-margin peak — always available; target
donors and pulls on the peak are not needed], (C4) [all tiny single-block AND multi-block ray components neutralized EXACTLY by pulls +
private banks, which also disposes of wrong-sign nearly neutral kept carriers, residual (n) of Y1]; cost o(T_lo^2) (Lemma CO); closure under
slaving (Lemma NS); (BS) (Lemma ST); robust rates (Lemma RR); transplant with design-controlled constants (Proposition TR); Theorem E''.
(3) Master Theorem II (4.3) with the residual list (B) genuinely multi-block rays, (C) coherent shift resonance; (D) is empty (5.1);
exhaustiveness checked in 5.3.
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
# V1 part 2 — Clean sub-windows: classification, pinning at f, donors, shift control, patterns and rays

Setting: D_Omega (part 1), N >= 1, f in S_{p*} with F finite and forced data (xi, q_0, a, w, F, z, zhat, e, nu); zeta_m := R_m^** zhat,
A_m := |zeta_m|_m = sigma_m/q_0, theta_m := A_m M_m/C_m, nu_k := |zeta_m(k)|/Phi_m(k)^2, rho_l := nu_{k(l)}/theta_{m(l)}; peak iff rho >= 1
(Lemma T of Y1/Y2); margin mu = q_0 Phi theta (rho - 1)/m on P_m; gap = M(1 - rho) on Q_m; eq:margin sigma_m |alpha_m(k)| = lambda_k mu_k.
g in C(f), eta <= eta_* with eta_Gamma(eta) <= 1, t <= min(t_eta, 1) dyadic, (B_+-, Theta_+-) a two-sided decomposition of g at scale t,
Delta theta_l := lambda_l (Theta_+ - Theta_-)_{m(l)}(k(l)), Delta B = -sum_l Delta theta_l u_l (eq:DeltaB), Delta d_m := d_{+,m} - d_{-,m}.
"f-constant": depends only on f, N (and g, rho where said), not on l, w, t.  C_f denotes f-constants (changing from line to line).
l_f: an f-dependent level threshold, enlarged finitely many times below (each time by a condition depending only on f).

## 2.1 Theorem 2' (clean sub-windows).  PROVED.
For every f (any F) and every level l there is i in {1..M(l)} such that w = (l,i) is CLEAN: no rate object of level l (part 1, 1.3)
has its value in Band(w) = (b(w), u(w)); so every rate of level l is TINY (<= b(w)) or ROBUST (>= u(w)).
Proof.  The omega(l) values each lie in at most one of the M(l) = omega(l)+1 pairwise disjoint bands (Theorem 1'(b)).  QED
Scale relations at a sub-window w of level l (Theorem 1'): for t in W(w): t >= T_lo(w), b(w) Design(l) <= t^4/l, sum_{l'>l} lambda_{l'}
<= b(w)^2/2, and T_hi(w) <= 1/Q(w) <= (u(w)/(4 Design(l)))^{omega(l)+20}.                                                  (2.1)

## 2.2 Classification at a clean sub-window (Y1 part 3; refereed)
Fix a clean w = (l,i), l >= l_f >= max F.  Since rho and |rho - 1| are rate objects ((R3), (R4)) and b(w) < u(w) <= 1/4, every coarse
carrier l'' <= l has rho in [0, b] ∪ [u, 1-u] ∪ [1-b, 1+b] ∪ [1+u, infinity) (b = b(w), u = u(w)).
 * class R: (R1)-rate >= u;  class G: (R1)-rate <= b, with eps_{l''} the minimizing sign of r^nat (unique: the two signed rooms sum to
   2||v 1_{S^nat}||), and tau_{l''} := -eps_{l''} Delta theta_{l''}; G(w) := class-G carriers <= l.  q_{l''} := eps Phi w_m(k)/(m C_m);
   swallowing type if eps sgn w_m(k) = +1 (q > 0), anti type if = -1 (q < 0), d-neutral if w_m(k) = 0 (then rho = 0).
 * ONE-SIGNED blocks (Y1 Lemma 3.6): Sigma_m(w) := coarse G-carriers of block m that are swallowing-type peaks, or strict non-peaks with
   rho > b (hence rho >= u) which are not anti-type with rho >= 1-b; block m is sigma-ONE-SIGNED at w if sgn q = sigma on Sigma_m(w).
 * DROPPED set P(w) ⊂ G(w): (P-i) anti-type peaks; (P-ii) anti-type strict non-peaks with rho >= 1-b; (P-iii) swallowing-type peaks with
   rho >= 1+u; (P-iv) Sigma_m(w) for every block m that is one-signed at w.  KEPT set Kp(w) := G(w) \ P(w), consisting of
   (K1) swallowing-type strict non-peaks with rho in [u, 1-u];  (K2) anti-type strict non-peaks with rho in [u, 1-u];
   (K3) carriers with rho <= b (any type, incl. d-neutral);  (K4) swallowing-type carriers with rho in [1-b, 1+b] (strict non-peaks,
   weak peaks, DEGENERATE peaks) — (K1), (K2), (K4) only in blocks that are not one-signed at w; in one-signed blocks only (K3) is kept.
 * Target coordinates j in T(l) \ F: CONTACT-LIKE if 1 - |z_j| <= b (contacts and tiny rooms), FREE-ROBUST if 1 - |z_j| >= u.
(This is exactly Y1's kept/dropped classification, Y1 part 3, Summary; donors are not added to P(w) — they are dropped or class R anyway.)

## 2.3 Pinning at f under a shift bound (Y1 Lemmas 3.1, 3.2, 3.3, 3.5; refereed, constants as corrected by Y1-ref m5)
Put D := D(l), u := u(w), K_g := (1/q_0 + 1) D/u.  Suppose a SHIFT BOUND |Delta d_m| M_m <= K_d' t holds for every block m.  Then:
 (3.1) sum_{l'' in class R} |Delta theta_{l''}| <= K_g t;
 (3.2) sum_{l'' in G(w)} (tau_{l''})_- <= K_g t, and e_0 := Delta B 1_{F^c} - sum_{G(w)} eps tau u 1_{F^c} has ||e_0||_1 <= K_g t + 4b^2/t;
 (3.5) |tau_{l''}| <= K_P t on (P-i)-(P-iii), K_P := K_g + K_d' + C_f D^2/u;   (3.1') fine carriers: sum_{l''>l} |Delta theta_{l''}| <= 3b^2/t <= t^7;
 (3.6) |tau_{l''}| <= K_O t on (P-iv), K_O := C_f D^2 (K_g + K_P)/u.
Proofs: Y1 Lemmas 3.1, 3.2, 3.5, 3.6 (Lemmas 3.5, 3.6 use the shift only through |Delta d| M <= K_d' t, Y1-ref m2; P-ii by Lemma 3.5(b),
P-iii by 3.5(c) with 1/mu <= m D/(q_0 theta u); P-iv by Lemma 3.6, which uses |q| >= Phi M u/(mC) on Sigma_m(w)).  (3.1), (3.2) need no shift bound.

## 2.4 Lemma D (robust-margin peaks; DONORS exist in every block).  PROVED.
There is l_f such that at every clean w of level l >= l_f every block m in I has a coarse peak k = k(c), c <= l, with rho_c >= 1+u(w)
(hence non-degenerate, margin mu_k >= q_0 theta_m u(w)/(m D(l))).  Every such c is DROPPED or of class R; it is PINNED:
|Delta theta_c| <= max(K_g, K_P, K_O) t under the shift bound ((3.1), (3.5), (3.6)).
Proof.  Fix m.  By Lemma lem:threshold, sum_{k in P_m} |alpha_m(k)| = 1.  Coarse peaks with rho <= 1+b: by eq:margin and the margin
formula, |alpha(k)| = lambda_k mu_k/sigma_m <= m Phi_k (q_0 Phi_k theta_m b/m)/sigma_m, so their total is <= (q_0 theta_m/sigma_m) b sum Phi^2
<= (M_m/(4C_m)) b (q_0 theta_m/sigma_m = theta_m/A_m = M_m/C_m, sum_k Phi_m(k)^2 <= 1/4).  Fine peaks (carrier > l): mu_k <= |u_k(xi)|
<= q_0 ||zhat||_inf <= 2 q_0, so their total is <= 2 q_0 sum_{l''>l} lambda_{l''}/sigma_m <= q_0 b^2/sigma_m.  Take l_f so large that
(M_m/(4C_m)) b + q_0 b^2/sigma_m < 1 for every m and every w of level >= l_f (b(w) <= 2^{-l^3}).  Then some coarse peak has rho > 1+b,
hence rho >= 1+u at a clean w.  It is class R, or class G anti type (P-i), or class G swallowing type with rho >= 1+u (P-iii).  QED
Every block therefore has a donor candidate at every clean sub-window of large level; this is what removes the aligned corner (part 5).

## 2.5 Shift control: sources (Y1) or shift cost (port of Y2 Section 5)
Sources (Y1 part 3, refereed).  UPPER source of block m at w: (U1) a class-R peak; (U2) an anti-type G-peak; (U3) every q < 0 carrier
of G(w) in block m is an anti-type peak, an anti-type strict non-peak with rho >= 1-b, or has rho <= b.  LOWER source: (L1) a class-R
peak with rho >= 1+u; (L2) a swallowing-type G-peak with rho >= 1+u; (L3) every q > 0 carrier of G(w) in block m has rho <= b.
Lemma 3.4' (Y1 Lemma 3.4 read half by half; Y1-ref (b)).  PROVED.  An upper source gives Delta d_m M_m <= K_d t, a lower source gives
Delta d_m M_m >= -K_d t, K_d := C_f D(l)^3/u(w).  (The proof of each half uses only its own source, Lemmas (3.1), (3.2), 3.3, the
pinned DROPPED anti-type carriers via Lemma 3.3(b) and Lemma suplevel(f) — not the other half.)
SHIFT PATTERNS.  A shift pattern of level l is pi = (I_up, I_lo, P*, vs, Bf, eps) with I_up, I_lo disjoint sets of blocks of carriers
<= l, P* ⊂ [1,l] with m(P*) ⊂ I_up ∪ I_lo, vs in {+-1}^{P*}, Bf ⊂ [1,l] \ P*, eps in {+-1}^{Bf}.  Put Pi_m := sum_{l'' in P*, m(l'')=m}
vs_{l''} lambda_{l''} u_{l''} 1_{F^c} and, for delta in R^{I_up ∪ I_lo},
   c(delta; pi) := inf_{x in [0,inf)^{Bf}} sum_{j notin F} phi_{z_j}( sum_m delta_m Pi_m(j) + sum_{l'' in Bf} x_{l''} eps_{l''} u_{l''}(j) ),
   c_pi := inf{ c(delta; pi) : ||delta||_1 = 1, delta_m >= 0 (m in I_up), delta_m <= 0 (m in I_lo) }   (c_pi := +infinity if I_up ∪ I_lo = {}).
(phi_z(x) = |x| - zx.  The series converge: sum_l lambda_l ||u_l||_1 < infinity, x ranges over a finite-dimensional cone.  c(.; pi) is
convex, positively homogeneous and finite, as a partial infimum of such a function; Y2 5.2, refereed.)  These are the rate objects (R6).
The shift pattern of f at w: I_up(w) := blocks without an upper source, I_lo(w) := blocks without a lower source, P*(w) := coarse peaks of
blocks in I_up(w) ∪ I_lo(w) with rho >= 1+u, vs := sgn w_m(k), Bf(w) := G(w) \ P*(w) with the class-G signs.
(SH_w): I_up(w) ∪ I_lo(w) = {}, or c_{pi(w)} >= u(w).   [At a clean w, NOT (SH_w) iff I_up ∪ I_lo != {} and c_{pi(w)} <= b(w).]

**Lemma S (shift pinning at a clean sub-window).  PROVED.**  Let w be clean of level l >= l_f.  (a) I_up(w) ∩ I_lo(w) = {} and
P*(w) ⊂ G(w).  (b) If (SH_w) holds, then |Delta d_m| M_m <= K_d' t for every block m, with K_d' := C_f l D(l)^3/u(w)^2.
Proof.  (a) If m in I_up ∩ I_lo, then (U1), (U2), (L2) fail, so every coarse peak of block m is a class-G swallowing-type peak with
rho in [1, 1+b], contradicting Lemma D.  A class-R peak with rho >= 1+u is a source of both kinds ((U1), (L1)), so blocks of
I_up ∪ I_lo have none: P*(w) ⊂ G(w).
(b) If I_up ∪ I_lo = {}, Lemma 3.4' gives |Delta d_m| M_m <= K_d t.  Otherwise c := c_{pi(w)} >= u.  For a peak k = k(l'') of block m,
eq:peakshift gives -Delta theta_{l''} = vs_k lambda_{l''} (Delta d_m M_m + e_k), e_k := |omega_{+,m}(k)| + |omega_{-,m}(k)| >= 0, and
e_k <= t/(sigma_m |alpha_m(k)|) = t/(lambda_k mu_k) for alpha(k) != 0; on P*(w), mu_k >= q_0 theta_m u/(m D).  Split
Delta B 1_{F^c} = sum_{l''} (-Delta theta_{l''}) u_{l''} 1_{F^c} according to l'' in P*(w), l'' in Bf(w) (class G, -Delta theta = eps tau =
eps (tau)_+ - eps (tau)_-), class R, fine.  For m in I_up (lower source present) put delta_m := (Delta d_m)_+ M_m >= 0, and
(Delta d_m)_- M_m <= K_d t; for m in I_lo put delta_m := -(Delta d_m)_- M_m <= 0, (Delta d_m)_+ M_m <= K_d t (Lemma 3.4').  Then
   Delta B 1_{F^c} = sum_m delta_m Pi_m + sum_{l'' in Bf} (tau_{l''})_+ eps_{l''} u_{l''} 1_{F^c} + R,
   ||R||_1 <= t sum_{P*} 1/mu_k + K_d t sum_m ||Pi_m||_1 + sum_G (tau)_- + sum_R |Delta theta| + sum_{fine} |Delta theta|
          <= C_f l D t/u + K_d t + 2 K_g t + t
(||u||_1 <= q*(u) = 1, ||Pi_m||_1 <= sum lambda <= 1/3, (3.1), (3.2), (3.1')).  By Lemma lem:switchbudget, sum_{j notin F}
phi_{z_j}(Delta B(j)) <= t/q_0; by Lemma lem:phicalc(c), phi_z(x + r) >= phi_z(x) - 2|r|; x := (tau)_+ >= 0 is admissible in the infimum and
delta lies in the sign cone, so  c ||delta||_1 <= c(delta; pi(w)) <= t/q_0 + 2||R||_1.  Hence ||delta||_1 <= C_f (l D/u + K_d + K_g + 1) t/u,
and |Delta d_m| M_m <= |delta_m| + K_d t <= C_f l D^3 t/u^2.  QED
Consequently, under (SH_w), the shift bound of 2.3 holds with K_d' = C_f l D^3/u^2, (3.5) holds with K_P <= C_f l D^3/u^2 and (3.6)
with K_O <= C_f l D^5/u^3.

## 2.6 Patterns, zero-cost cones and ray components (rate objects (R5), (R7))
A PATTERN of level l is kappa = (U, P, eps, F', type): U ⊂ [1,l], P ⊂ U, eps in {+-1}^U, F' ⊂ T(l), type : T(l) \ F' -> {+1,-1,0}
(Y1's generalized configuration).  With L_j(tau) := sum_{l'' in U} eps_{l''} tau_{l''} u_{l''}(j) (design numbers u_{l''}(j)), its
ZERO-COST CONE is
   C(kappa) := {tau in R^U : tau_{l''} >= 0 (l'' in U \ P); tau_{l''} = 0 (l'' in P); type(j) L_j(tau) >= 0 (type(j) = +-1);
                L_j(tau) = 0 (type(j) = 0), j in T(l) \ F'}.
C(kappa) ⊂ [0, inf)^U is a pointed polyhedral cone; Ext(kappa) denotes its extreme rays normalized by ||r||_1 = 1, so C(kappa) =
cone(Ext(kappa)) (Minkowski-Weyl).  Y1's polyhedron Z_kappa(beta) is C(kappa) ∩ {|tau_{l''}| <= beta_{l''}}.
The PATTERN OF f AT w: kappa(w) := (G(w), P(w), eps, F ∩ T(l), type_w), type_w(j) := sgn z_j if j is contact-like, 0 if free-robust.
For r in Ext(kappa(w)) and a block m meeting supp r, the d-COMPONENT is D_{r,m}(f) := sum_{l'' in supp r, m(l'')=m} r(l'') val_{l''},
val_{l''} := eps_{l''} u_{l''}(zhat); its (R5)-rate is |D_{r,m}|/Phi_max(r,m), Phi_max(r,m) := max_{l'' in supp r, m(l'')=m} Phi_{l''}.
At a clean w each component is TINY (rate <= b(w)) or ROBUST (rate >= u(w)).
(VR_w): every r in Ext(kappa(w)) has at most one ROBUST component.
Remarks.  (1) Why values: at a strict non-peak, q_{l''} = val_{l''}/A_m (Z6 2.1; Y4-ref C.7: q = q_0 val/sigma_m), so the d-row of block m
on C(kappa) is tau -> (1/A_m) sum_{l'' in block m} val_{l''} tau_{l''}, and D_{r,m}/A_m is the d-sum of the ray r in block m.  For a
(K4) peak of f the d-coefficient at f is Phi M/(mC) = val/(rho A) with rho in [1, 1+b]: relative difference <= b.
(2) Single-block rays: if supp r lies in one block, (VR_w) holds for r automatically.  If N = 1, (VR_w) always holds.  In a block that is
one-signed at w every kept carrier has rho <= b, so |val| <= b Phi theta/m and EVERY component in that block is tiny: one-signed blocks never
carry robust components.  Dropping more carriers only helps: C(kappa) ∩ {tau_{l''} = 0} is a face of C(kappa) (C(kappa) ⊂ orthant), and
the extreme rays of a face are extreme rays of C(kappa).
(3) (VR_w) is a property of f at level l and of the explicit numbers b(w), u(w); it involves no rate threshold beyond them.
# V1 part 3 — The assembled companion f^#_w: moves, tools (diagonal base), cost, statuses, no slaving, robust rates

Setting of part 2: D_Omega, F finite, clean w = (l,i), l >= l_f, b := b(w), u := u(w), D := D(l), T_lo := T_lo(w), Design := Design(l).
A COMPANION is the first row with prescribed forced data (a', z'): q*(a') = 1, |z'| <= 1, z' = sgn a' on supp a' (Remark rem:lemmaZ(c)):
e' = U^*a'/||U^*a'||, zhat' = z' + Ue', q'_0 = (1 + sum_m |R_m^** zhat'|_m)^{-1}, w'_m = J_m(R_m^** zhat').  For an unnormalized A we write
"the row (A, z')" for the companion with a' = A/q*(A) (e' and zhat' do not depend on the normalization).  Companions need not attain
their norm.  For a carrier l'' with a sign eps_{l''} we write val_{l''} := eps_{l''} u_{l''}(zhat) (and val^#, val^(2) at companions).

## 3.1 Lemma B (masses off the support, diagonal base).  PROVED.
Let (A^0, z^0) be forced data (A^0 unnormalized, nu_0 := ||U^*A^0||, e^0 := U^*A^0/nu_0), J a finite set disjoint from supp A^0,
c in R^J, A := A^0 + sum_{j in J} c_j e_j^*, X := sum_{j in J} c_j s_j k_j.  Then ||U^*A||^2 = nu_0^2 + ||X||^2 and for every u in l_1:
   <U^*u, e^A> = ( nu_0 <U^*u, e^0> + sum_{j in J} c_j s_j^2 u(j) ) / (nu_0^2 + ||X||^2)^{1/2}.                         (3.1)
Hence (i) if u vanishes on J: |<U^*u, e^A> - <U^*u, e^0>| <= ||U|| ||u||_1 ||X||^2/(2 nu_0^2);
(ii) in general <U^*u, e^A> - <U^*u, e^0> = sum_J c_j s_j^2 u(j)/nu_0 + R_u, |R_u| <= (||U|| ||u||_1 + sum_J |c_j| s_j^2 |u(j)|/nu_0) ||X||^2/nu_0^2;
(iii) ||e^A - e^0|| <= 2||X||/nu_0.
Proof.  (1.1) with a := A^0: <U^*A^0, k_j> = s_j A^0_j = 0 for j in J, so U^*A = U^*A^0 + X with X ⊥ U^*A^0, and <U^*u, X> =
sum_J c_j s_j <U^*u, k_j> = sum_J c_j s_j^2 u(j).  Divide by ||U^*A||.  (i), (ii): 0 <= 1 - (1+x)^{-1/2} <= x/2 with x := ||X||^2/nu_0^2,
|<U^*u, e^0>| <= ||U^*u|| <= ||U|| ||u||_1, and (1+x)^{-1/2} >= 1 - x/2.  (iii): ||x/||x|| - y/||y|| || <= 2||x - y||/||y||.  QED
A MASS at j with the sign of z^0_j at a contact (|z^0_j| = 1) is a BANK (z unchanged); a mass -eps mu at j in S_l together with the flip
z_j := -eps (from z^0_j = eps) is a PULL (Y4-ref C.1).  In both cases (A, z) are admissible forced data (z = sgn A on supp A).

## 3.2 The moves at w (in this order)
Fix the classification of part 2 at w.  I_D(w) := blocks containing a (K4) carrier; for m in I_D(w) fix a peak c_m of block m with
rho_{c_m} >= 1+u (Lemma D), vs_m := sgn u_{c_m}(zhat) (= sgn w_m(k(c_m))), and s_m := min(S_{c_m} ∩ (s_max(l), infinity)) (so s_m <= sigma(l)).
 (C1) [close class-G rooms] z^1_s := eps_{l''} for s in S^nat_{l''}(l), l'' in G(w);
 (C2) [close tiny target rooms] z^1_j := sgn z_j for j in T(l) \ F with 0 < 1 - |z_j| <= b;   z^1 := z elsewhere.
 (C3) [donor raise, every m in I_D(w)]  Put Lam := T_lo^3.
      (a) if lambda_{c_m} v_{c_m}(s_m)(1 - vs_m z^1_{s_m}) >= Lam: z^2_{s_m} := z^1_{s_m} + eta_m vs_m, eta_m := Lam/(lambda_{c_m} v_{c_m}(s_m)) (no mass);
      (b) otherwise: z^2_{s_m} := vs_m (close) and a BANK of mass mu^D_m := 2 nu Lam/(lambda_{c_m} s_{s_m}^2 v_{c_m}(s_m)) at s_m with sign vs_m.
      A^2 := a + sum_{m in I_D, case (b)} mu^D_m vs_m e*_{s_m};  z^2 := z^1 elsewhere.  f^(2) := the row (A^2, z^2).
 (C4) [exact tuning of tiny ray components]  Let Sigma_t(w) be the set of TINY components (r, m) of kappa(w) (rate <= b at f), L_0 :=
      union of (supp r ∩ block m) over Sigma_t(w) (⊂ Kp(w)), R := R_{Sigma_t} (rows (r(l''))_{l'' in block m}), V^(2) := (D^(2)_{r,m})_{(r,m) in Sigma_t},
      D^(2)_{r,m} := sum_{l'' in supp r, m(l'')=m} r(l'') val^(2)_{l''}, and x := -R^+ V^(2) (least-norm solution of R x = -V^(2); the system
      is consistent since V^(2) = R val^(2)).  If x = 0 put f^# := f^(2); otherwise apply Lemma TU (3.4) at f^(2) with L_0 and x:
      f^# := f^#_w is the resulting row (pulls and banks on the far parts of the S_{l''}, l'' in L_0).
The coordinates modified by different moves are pairwise distinct: (C1) acts on S^nat sets of class-G carriers (outside T(l) ∪ F);
(C2) on T(l); (C3) on s_m in S_{c_m} (c_m dropped or class R: not in L_0; if c_m is class G, (C3) acts after (C1) on the same
coordinate, as in Y1-ref m3); (C4) on S_{l''} \ [1, s_max(l)] for l'' in L_0 ⊂ Kp(w), disjoint from all S_{c_m}.

## 3.3 Lemma DR (the donor raise).  PROVED.
For l >= l_f and every m in I_D(w): (i) the move (C3) alone increases |u_{c_m}(zhat)| by an amount in [Lam, 3 Lam]/lambda_{c_m}; the
total increase from f to f^# lies in [Lam/2, 4 Lam]/lambda_{c_m} ((C1), (C2) change u_{c_m} by <= (|T(l)|+1) b, (C4) by <= C_f Design^2 eta^2,
eta := |x|_inf); (ii) the bank mass satisfies mu^D_m <= Design Lam;
(iii) for every coarse carrier k != c_m, u_k(zhat) is unaffected by (C3) up to C_f Design^2 Lam^2 (case (b)) and exactly (case (a)).
Proof.  The only coarse carrier whose vector meets s_m is c_m (s_m in S_{c_m}, s_m > s_max(l), disjoint signature sets), with
u_{c_m}(s_m) = v_{c_m}(s_m).  Case (a): u_{c_m}(zhat) moves by v_{c_m}(s_m) eta_m vs_m, i.e. |u_{c_m}(zhat)| grows by Lam/lambda_{c_m}
(Lam/lambda <= v(1 - vs z) by the case condition; the sign of u_c(zhat) is vs and |u_c(zhat)| >= rho Phi theta/m is not crossed).  Case (b):
the closing raises vs u_c by v(s_m)(1 - vs z^1) in [0, Lam/lambda_c); the bank raises it, by Lemma B(ii) with J = {s_m} ∪ {other donor
banks}, by mu^D s^2 v/nu + R with |R| <= C ||X||^2/nu^2 and ||X||^2 = sum (mu^D)^2 s^2; mu^D s^2 v/nu = 2 Lam/lambda_c.  Feasibility and
(ii): s_{s_m}^2 v_{c_m}(s_m) >= 4^{-sigma(l)} delta_min(l) 2^{-sigma(l)}/2 and lambda_c >= 1/D(l), so mu^D <= 4 nu D 8^{sigma} Lam/delta_min
<= Design Lam; hence |R| <= C Design^2 Lam^2 << Lam/lambda_c, and the raise lies in [Lam, 3 Lam]/lambda_c.  (iii) Lemma B(i).  The
tuning (C4) changes u_{c_m}(zhat) only through the Hilbert part (c_m notin L_0 and its vector vanishes at the tuning coordinates), by
Lemma B(i) at most C ||X_tune||^2 <= C_f Design^2 eta^2 (Lemma TU(c)).  QED

## 3.4 Lemma TU (exact two-sided tuning on a finite set of carriers; diagonal base).  PROVED.
Let f^(2) = (A^2, z^2) be forced data with F^2 := supp A^2 finite, nu_2 := ||U^*A^2||, L >= max L_0, F^2 ⊂ [1, s_max(L)] ∪ (union of
S_{c} over finitely many carriers c notin L_0), and suppose every l'' in L_0 is EXACTLY SWALLOWED far out: z^2 = eps_{l''} on
S_{l''} \ [1, s_max(L)].  Let x in R^{L_0}, eta := |x|_inf.  There are c_T, C_T of the form (f-constant) x Design(L)^{-3}, resp.
(f-constant) x Design(L)^3, such that if eta <= c_T, the following hold.  For l'' in L_0 let j'_{l''} := min(S_{l''} ∩ (s_max(L), inf)) (BANK
coordinate) and choose a PULL coordinate j_{l''} in S_{l''}, j_{l''} > j'_{l''}, with v_{l''}(j_{l''}) in [eta, 2^{G_{l''}} eta] (possible by
bounded gaps (D0'): the values v_{l''}(s), s in S_{l''}, decrease by the factor 2^{-G_{l''}} between consecutive elements).  Put
mu_{l''} := 24 lambda_{l''} v_{l''}(j_{l''}).  Then there is m in [0, infinity)^{L_0} such that the row f^# with
   A^# := A^2 - sum_{L_0} eps_{l''} mu_{l''} e*_{j_{l''}} + sum_{L_0} m_{l''} eps_{l''} e*_{j'_{l''}},   z^#_{j_{l''}} := -eps_{l''},  z^# := z^2 elsewhere,
satisfies:
 (a) val^#_{l''} = val^(2)_{l''} + x_{l''} EXACTLY for every l'' in L_0;
 (b) |u_k(zhat^#) - u_k(zhat^(2))| <= C_T eta^2 for every carrier k <= L, k notin L_0;
 (c) ||m||_inf <= C_T eta, the pull masses are <= 6 * 2^{G(L)} eta, ||X_tune||^2 := sum mu^2 s_j^2 + sum m^2 s_{j'}^2 <= C_T eta^2;
 (d) p*(f^# - f^(2)) <= C_T eta log(e/eta), and the block data (C_m, M_m, sigma_m, q_0, theta_m) move by <= C_T eta.
Proof.  (A^#, z^#) are admissible forced data: pulls carry masses of the new sign -eps = z^#; banks sit at j' where z^2 = eps (exact
swallowing far out) with masses of sign eps; F^2 is disjoint from all j, j' (they lie in S_{l''} beyond s_max(L), l'' in L_0).
Step 1 (pulls).  Let A^p := A^2 - sum eps mu e*_j, z^p as stated, nu_p := ||U^*A^p||, e^p.  For l'' in L_0, u_{l''}(j_{l''}) = v_{l''}(j_{l''})
and u_{l''} vanishes at the other pull and bank coordinates (they lie in other signature sets, beyond s_max(L) ⊃ all coarse targets).  So
by Lemma B(ii) val^p_{l''} - val^(2)_{l''} = -2 v_{l''}(j_{l''}) - mu_{l''} s_j^2 v_{l''}(j_{l''})/nu_2 + R with |R| <= C ||X_p||^2, and for k <= L,
k notin L_0, |u_k(zhat^p) - u_k(zhat^(2))| <= C ||X_p||^2 (Lemma B(i); z^p = z^2 on supp u_k).  ||X_p||^2 <= sum mu^2 <= C 4^{G} eta^2 |L_0|.
Step 2 (banks; explicit solution).  For m in [0, inf)^{L_0} let A(m) := A^p + sum m_{l''} eps_{l''} e*_{j'_{l''}}, N(m) := (nu_p^2 + sum_{l''}
m_{l''}^2 s_{j'_{l''}}^2)^{1/2}.  By (3.1) with base A^p and J = {j'}, writing s'_{l''} := s_{j'_{l''}}, v'_{l''} := v_{l''}(j'_{l''}), beta_{l''} :=
eps_{l''} <U^*u_{l''}, e^p> (|beta| <= ||U||):
   val_{l''}(m) - val^p_{l''} = (m_{l''} s'^2 v' + beta nu_p)/N(m) - beta.
Required increments Delta_{l''} := x_{l''} + (val^(2) - val^p)_{l''} = x_{l''} + 2v(j) + O(4^G eta^2) lie in [eta/2, 4 * 2^{G} eta] for eta <= c_T.
For a scalar y >= nu_p put m_{l''}(y) := (Delta_{l''} y + beta_{l''}(y - nu_p))/(s'^2 v'), which solves the l''-th equation if N(m) = y, and
Phi(y) := (nu_p^2 + sum s'^2 m_{l''}(y)^2)^{1/2}.  With s'^2 v' >= 8^{-sigma(L)} delta_min/2 >= Design^{-1/6} and |Delta| <= 4*2^G eta:
on I := [nu_p, nu_p + kappa], kappa := 2 (Phi(nu_p) - nu_p) <= C Design eta^2, one has |Phi'(y)| = |sum m(y)(Delta + beta)/(v' Phi)| <= C |L_0| Design (eta
+ kappa)(eta + ||U||) <= 1/2 for eta <= c_T; and Phi >= nu_p.  So Phi maps I into I (Phi(y) <= Phi(nu_p) + (y - nu_p)/2) and has a fixed point
y*; m := m(y*) solves all equations, and m_{l''} >= (Delta nu_p - ||U|| kappa)/(s'^2 v') > 0.  This gives (a) (val(m) - val^(2) = x).
(b): for k <= L, k notin L_0, u_k vanishes at all j, j' and z^# = z^2 on supp u_k, so Lemma B(i) with base A^2 and J = all pull and bank
coordinates gives |Delta u_k(zhat)| <= C ||X_tune||^2.  (c): m <= C Design eta, pull masses mu <= 6 v(j) <= 6 * 2^G eta, ||X_tune||^2 <=
C(4^G + Design^2) eta^2 <= C_T eta^2.  (d): delta := zhat^# - zhat^(2) = (z^# - z^2) + U(e^# - e^(2)); |u_k(delta)| <= 2|u_k(j_{l''})|-terms +
||e^# - e^(2)||; the carriers with u_k(j_{l''}) != 0 are l'' and carriers l' > L whose targets contain j_{l''}, whose lambda's sum to <= 2^{-j}
v_{l''}(j) by allowedness (b) (Y4-ref P1(c)); so c(delta) <= C (2^G eta + ||e^# - e^2|| log(1/||e^# - e^2||)) and Delta_m <= C (2^G eta + ||e^# -
e^(2)||), ||e^# - e^(2)|| <= 2||X_tune||/nu_2 (Lemma B(iii)).  The proof of Z3 Lemma 3.1 (it uses only zhat^# = zhat^(2) + delta and the clamp
formula at both rows; Y4 Lemma 2.2, refereed) gives p*(f^# - f^(2)) <= q*(a^# - a^(2)) + C_f c(delta) <= C_T eta log(e/eta) and the block-data
bounds.  QED
(Lemma TU is Y4-referee Prop. P4 with an explicit solution of the bank equations in place of the inverse function theorem; constants
are explicit design quantities of level L.  Y4-ref tune_check.py checks it numerically.)

## 3.5 Lemma CO (cost and data of the companion).  PROVED.
For l >= l_f: eta := |x|_inf <= H_tune(l)(|T(l)| + 3) b <= Design b, and
   p*(f^#_w - f) <= C_f Design T_lo^3 log(1/T_lo) =: theta_w T_lo^2,   theta_w := C_f Design T_lo log(1/T_lo) -> 0,
and the block data move by <= C_f Design T_lo^3 log(1/T_lo): ||R_m^*(w^#_m - w_m)||_1 + ||D_m(w^#_m - w_m)||_2 + |C^#_m - C_m| + |M^#_m - M_m|
+ |sigma^#_m - sigma_m| + |q_0^# - q_0| + ||e^# - e|| <= C_f Design T_lo^3 log(1/T_lo).
Proof.  delta := zhat^# - zhat = (z^# - z) + U(e^# - e).  Coarse carriers l'': (C1) changes u_{l''} only on its own S^nat (no coarse
target meets S^nat_{l''}(l), other signature sets are disjoint): |u_{l''}(Delta_C1)| = r^nat_{l''} <= b for class G, 0 otherwise; (C2) changes
u_{l''} by <= |T(l)| b; (C3) changes only u_{c_m} among coarse carriers, by <= 3Lam/lambda_{c_m} <= 3 D Lam (Lemma DR); (C4) by Lemma TU;
||e^# - e|| <= C(sum_m mu^D_m + C_T eta) <= C Design Lam (Lemmas DR, TU, B(iii)).  Fine carriers: sum_{l'>l} min(lambda, .) <= b^2/2.  So
Delta_m <= sum_k lambda_k |u_k(delta)| <= C l(|T|+1) b + 3N Lam + C Design Lam + b^2 <= C Design Lam, and c(delta) <= C_f Design Lam log(1/Lam).
q*(a^# - a) <= C(sum mu^D + sum mu + sum m) <= C Design Lam.  Z3 Lemma 3.1 / Y4 Lemma 2.2 / Y4-ref P1(c) (same proof: forced data at both rows,
clamp formula) give the bounds.  For eta: |V^(2)_{(r,m)}| <= |D_{r,m}(f)| + sum_{l''} r(l'') |val^(2)_{l''} - val_{l''}| <= b + (|T(l)|+2) b (tiny
component at f, ||r||_1 = 1, Phi_max <= 1; values move by (C1), (C2) and second-order (C3) terms), and |x|_inf <= |x|_2 <= ||R^+||_2
|V^(2)|_2 <= H_tune(l) (|T|+3) b.  QED

## 3.6 Lemma ST (status table at f^#; status stability (BS) under the threshold drift).  PROVED.
For l >= l_f: (a) in every block m, E_m := sum_{k != k(c_m)} |zeta^#_m(k) - zeta_m(k)| <= C_f Design b + C Design^2 Lam^2 <= C_f T_lo^4
(zhat-units); (b) for m in I_D(w): c_f Lam <= theta^#_m - theta_m <= C_f Lam; for m notin I_D(w): |theta^#_m - theta_m| <= C_f T_lo^4;
(c) rho^#_{l''} = rho_{l''} (theta_m/theta^#_m)(1 + O(C_f D Design b/u)) for every coarse l'' != c_m with rho_{l''} >= u; hence: robust peaks
(rho >= 1+u) stay peaks with rho^# >= 1 + u/2; robust strict non-peaks (rho <= 1-u) stay strict non-peaks with rho^# <= 1 - u/2; carriers with
rho in [u, 1-u] keep rho^# in [u/2, 1 - u/2]; EVERY (K4) carrier becomes a strict non-peak of f^# with rho^# <= 1 - c_f Lam/3, i.e.
gap^#(k) >= M^#_m c_f Lam/3 > 0; nearly neutral carriers (rho <= b) have rho^# <= C_f D Design b; (d) at every kept (K1), (K2), (K4) carrier
sgn w^#_m(k) = sgn w_m(k), and q^#_{l''} = val^#_{l''}/A^#_m at every kept carrier (all are strict non-peaks of f^#);
(e) contacts of f in T(l) \ F keep their sign; contact-like target coordinates are contacts of f^#; free-robust ones keep room >= u;
z^# = eps_{l''} on S^nat_{l''}(l) \ F^# for every l'' in G(w) except at the donor coordinates s_m of class-G donors.
Proof.  (a) Coarse non-donor carriers: values move by (C1) + (C2) <= (|T|+1) b, by (C3) <= C Design^2 Lam^2 (Lemma DR(iii)), by (C4) <= |x_{l''}|
<= Design b or C_T eta^2 (Lemma TU); sum_k lambda_k <= 1; fine carriers <= 2 sum_{l'>l} lambda_{l'} <= b^2; and b Design <= T_lo^4/l.
(b) Lemma T2(b) of Y1 (refereed) applied to zeta := zeta_m(f), zeta' := zeta_m(f^#), c := k(c_m) (a peak, outward push s in [Lam/2, 4Lam] by
Lemma DR(i)), E := E_m <= A s/(8(A + theta + 1)) for l >= l_f: theta' - theta >= min{1, A s/(8 phi (A + theta + 1))} >= c_f Lam, and the upper
bound C_1(s + E) (C_1 an f-constant: Lemma T2 with the fixed reference peak of block m).  For m notin I_D: Lemma T2(a).
(c) Corollary T3 of Y1: rho'_k = (|zeta'(k)|/|zeta(k)|) rho_k theta/theta'; for rho_{l''} >= u, |zeta(k)| = lambda |u(zhat)| = rho Phi^2 theta >= u theta/D^2,
and |zeta'(k) - zeta(k)| <= lambda((|T|+2) b + |x|) <= 2 m Phi Design b: relative change <= C_f D Design b/u;
for (K4): (1 + b)(1 + C_f D Design b)/(1 + c_f Lam) <= 1 - c_f Lam/3 because D Design b <= T_lo^4/l << Lam = T_lo^3.  Robust cases: u >> C_f Lam.
Nearly neutral: |u(zhat^#)| <= |u(zhat)| + C Design b.  (d) |Delta u(zhat)| <= C Design b << u Phi theta/m <= |u(zhat)| at (K1), (K2), (K4); at a
strict non-peak of f^#, w^#(k) = C^# zeta^#(k)/(Phi^2 |zeta^#|) (Lemma lem:threshold), so q^# = eps Phi w^#(k)/(m C^#) = val^#/A^#_m (Z6 2.1).
(e) (C2) raises same-sign; other moves are outside T(l); (C1) by definition; pulls and banks are support coordinates of f^# (in F^#).  QED

## 3.7 Lemma NS (no slaving; the exactified set is closed).  PROVED.
At f^#: (i) for every coarse carrier l'' the change of u_{l''}(zhat) is the sum of: its own closing r^nat_{l''} (class G), target closings
(<= |T(l)| b), its own donor raise (l'' = c_m) or own tuning x_{l''} (l'' in L_0), and Hilbert second-order terms <= C Design^2 (Lam^2 + eta^2);
no coarse carrier's value depends on the closing of ANOTHER carrier's room (pinning and closing sets S^nat exclude T(l), and no coarse target
meets S^nat; allowedness (a) excludes coarser targets from finer signature sets); (ii) every class-G room on S^nat \ F^# is exactly closed
(except at donor coordinates of class-G donors, which are dropped), every contact-like target coordinate is an exact contact, and every
tiny d-component of kappa(w) is exactly zero at f^#; (iii) the zero-cost cone of the pattern at f^# is C(kappa(w)) (same rows).
Hence the exactified set (closed rooms, closed target rooms, neutralized components) is closed under slaving: closing one object never
reopens or moves another exactified object, and no robust object is moved by more than C Design b (Lemma RR).
Proof.  (i) as in Lemma CO.  (ii) (C1), (C2) by definition; (C4) by Lemma TU(a) applied with x = -R^+ V^(2) (R x = -V^(2), and every carrier of a tiny
component is in L_0, so its value is EXACTLY val^(2) + x); later moves do not touch these coordinates.  (iii) the rows (Z1)-(Z3) of kappa(w) involve
only T(l) \ F (types of f^#: Lemma ST(e)) and the sets P(w), G(w).  QED

## 3.8 Lemma RR (robust rates stay robust).  PROVED.
At f^#: free-robust target rooms are >= u; robust relative positions/threshold distances are as in Lemma ST(c); every ROBUST component
(r, m) of kappa(w) has |D^#_{r,m}| >= u Phi_max(r,m)/2; every TINY component has D^#_{r,m} = 0.
Proof.  Rooms: z^# = z on free-robust coordinates.  Components: |D^#_{r,m} - D_{r,m}(f)| <= sum r(l'') |val^# - val| <= (|T|+2) b + |x|_inf +
C Design^2(Lam^2 + eta^2) <= 2 Design b <= u Phi_max/2 (Phi_max >= 1/D(l), Design b D << u).  Tiny components: Lemma NS(ii).  QED
# V1 part 4 — Transplant at the assembled companion, Theorem E'', and the MASTER THEOREM II

Setting of parts 2-3: D_Omega, F finite, g in C(f), clean w = (l,i), l >= l_f, companion f^# = f^#_w (part 3) with forced data
(xi^#, q_0^#, a^#, w^#, F^#, z^#, zhat^#, e^#, nu^#); F^# = F ∪ Ba ∪ Pu, Ba := bank coordinates (donor banks s_m in case (b) of (C3) and
tuning banks j'_{l''}), Pu := pull coordinates j_{l''} (l'' in L_0).  t in W(w) dyadic, t <= min(t_eta, 1); (B_+-, Theta_+-) a two-sided
decomposition of g at f at scale t.  D := D(l), u := u(w), b := b(w), Lam := T_lo(w)^3.

## 4.1 Proposition TR (transplant at the assembled companion).  PROVED.
Assume (SH_w) and (VR_w).  Then there is g_t carrying d-NEUTRAL two-piece data (b^+-, omega^+-) AT f^# (Definition def:twopiece read at
f^#, with base support F^#) such that
 (i)   b^+-(xi^#) = 0, t||b^+-||_1 <= A_0 (an f-constant), and Gamma^#_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta) + C theta_w) + K_w t)^2;
 (ii)  p*(g - g_t) <= K_w t with K_w <= C_f Design(l) u(w)^{-4};
 (iii) every k in supp omega^+-_m satisfies, at f^#, one of: [1] gap^#(k) >= t^2 and |omega(k)| <= 2 gap^#(k)/t; [2] gap^#(k) >= gamma(w) :=
       min_m M_m u(w)/4 and |omega(k)| <= A_2/t; [3] k is a strict non-peak of f^# with the inward sign (vs_k omega^+(k) <= 1.5 gap^#(k)/t,
       vs_k omega^-(k) >= -1.5 gap^#(k)/t, vs_k := sgn w^#_m(k)) and |omega(k)| <= A_2/t;  A_2 := 22;
 (iv)  b^+- are contact-like on Ba (z^#_j b^+_j >= 0 >= z^#_j b^-_j) and t |b^+-(j)| <= |a^#(j)| for j in Pu.
Proof (modification of Y1 Proposition 5.2, refereed; every departure is marked NEW).
Step 0 (pinning at f).  By (SH_w) and Lemma S, |Delta d_m| M_m <= K_d' t, K_d' <= C_f l D^3/u^2; so 2.3 gives (3.1), (3.2), (3.5), (3.6)
with K_P <= C_f l D^3/u^2, K_O <= C_f l D^5/u^3, K_g <= C D/u.
Step 1 (zero-cost projection; Y1 Step 1 verbatim with kappa^# := kappa(w)).  Let tau := (tau_{l''})_{l'' in G(w)} and beta_{l''} :=
12 lambda_{l''}/t.  On T(l) \ F, Delta B(j) = L_j(tau) + e_0(j).  Violations of the rows of Z_{kappa(w)}(beta) by tau: (Z1) sum (tau)_- <= K_g t;
(Z2) at contact-like j, (type_w(j) L_j(tau))_- <= phi_{z_j}(Delta B(j)) + |e_0(j)| (for type = sgn z_j: phi_z(x) >= (sgn z * x)_-), at
free-robust j, |L_j(tau)| <= phi_{z_j}(Delta B(j))/u + |e_0(j)| (Lemma lem:phicalc(a)); summed <= (t/q_0)(1 + 1/u) + 2||e_0||_1;
(Z3) sum_{P(w)} |tau| <= l (K_P + K_O) t; (Z4) |tau| <= 6 lambda/t (Lemma lem:box): none.  Total V_w <= C_f l^2 D^5 t/u^3.  By the definition of
G**(l) (Hoffman, right-side independent) there is tau_0 in Z_{kappa(w)}(beta) with ||tau - tau_0||_1 <= G**(l) V_w.
Step 2 (d-rows at f^#).  Q^#_m(tau') := sum_{l'' in Kp(w), m(l'')=m} q^#_{l''} tau'_{l''} = (1/A^#_m) sum val^#_{l''} tau'_{l''} (Lemma ST(d)).
By eq:didentity at f (a G-carrier contributes Phi w Delta theta/(mC) = -q tau), (3.1), (3.1'), (3.5):
|sum_{Kp, m} q tau| <= |Delta d_m| M_m + C(K_g + 1) t/C_m + 2t/sigma_m + l (K_P + K_O) t/C_m.  At kept strict non-peaks of f, q = val/A_m; at kept (K4)
peaks of f, q = Phi M/(mC) = val/(rho A_m) with rho in [1, 1+b] (part 2, Remark (1)); with |val^# - val| <= 2 Design b (Lemmas CO, TU),
|q^# - q A_m/A^#_m| <= C_f Design b at every kept carrier.  Hence |Q^#_m(tau_0)| <= K_Q t, K_Q := C_f (K_d' + K_g + l (K_P + K_O) + G** V_w/t)
<= C_f G** l^2 D^5/u^3 (the term l Design b * 12/t^2 <= t^2 is absorbed).
Step 3 (exact d-repair by RAY REMOVAL; NEW, replaces Y1 Step 3 and the hypotheses (Cmp_w), (NN_w)).  tau_0 in C(kappa(w)), so tau_0 =
sum_{r in Ext} mu_r r with mu_r >= 0 (Minkowski-Weyl).  At f^#, the d-vector of a ray r is (D^#_{r,m}/A^#_m)_m; by Lemma RR every component
is 0 (tiny at f, or block not met) or robust, |D^#_{r,m}| >= u Phi_max(r,m)/2 >= u/(2D); by (VR_w) every r has at most one nonzero
component, in a block m(r) (m(r) undefined if all vanish).  For each block m put tau^(m) := sum_{m(r)=m} mu_r r, e_m := Q^#_m(tau^(m)) =
Q^#_m(tau_0) (rays with m(r) != m have zero m-component).  Lemma 1.8 of Y4 (ray removal; refereed) applied to the cone cone{r : m(r) = m}
⊂ [0,inf)^G, the vector tau^(m) and the functional Q^#_m gives tau'^(m) with 0 <= tau'^(m) <= tau^(m) coordinatewise, tau'^(m) in that cone,
Q^#_m(tau'^(m)) = 0 and ||tau^(m) - tau'^(m)||_1 <= |e_m| 2 D A^#_m/u.  Put tau' := sum_{m(r) undefined} mu_r r + sum_m tau'^(m).  Then
tau' in C(kappa(w)) (a convex cone), 0 <= tau' <= tau_0 coordinatewise (box rows kept), Q^#_{m'}(tau') = Q^#_{m'}(tau'^(m')) = 0 for EVERY
block m', and ||tau_0 - tau'||_1 <= 2 N D max_m A^#_m K_Q t/u.  Consequently, with V' := sum_{Kp} eps tau' u 1_{F^c},
   ||Delta B 1_{F^c} - V'||_1 <= ||e_0||_1 + ||tau - tau'||_1 <= K_U t,   K_U := K_g + 1 + G** V_w/t + C_f N D K_Q/u <= C_f G** l^2 D^6/u^4.
Zero cost (NEW bookkeeping for pulls/banks): for j notin F^#, V'(j) is z^#-signed and V' vanishes at free coordinates of f^#: on
S^nat_{l''}(l) only u_{l''} lives among coarse carriers and z^# = eps_{l''} there off F^# (Lemma ST(e); tau' >= 0 on kept, = 0 on dropped
carriers); on T(l) \ F the rows (Z2) of kappa(w), whose types are those of f^# (Lemma ST(e)); elsewhere off F every coarse class-G vector
vanishes (supp u_{l''} ⊂ supp y_{l''} ∪ S_{l''} and S_{l''} \ S^nat_{l''} ⊂ F ∪ T(l)).  Moreover V' is z^(2)-signed and supported in K^(2) :=
{j notin F : |z^(2)_j| = 1} (z^(2) = the sign vector before the pulls): at pulls and tuning banks z^(2) = eps_{l''} (closed by (C1)); at donor
coordinates s_m, V'(s_m) = 0 (c_m notin Kp(w)).
Step 4 (split w.r.t. z^(2); NEW choice of sign vector).  Lemma lem:split with z^(2) in place of z (its proof uses only Lemma lem:phicalc(b)
and the summed budget) applies once sum_{j notin F}[phi_{z^(2)_j}(B_+(j)) + phi_{-z^(2)_j}(B_-(j))] <= C_S t: off the coordinates modified by
(C1)-(C3), phi_{z^(2)} = phi_z (budget t/q_0); at raised coordinates ((C2), and (C1) with z_s eps >= 0) phi_{z^(2)} <= 2 phi_z (Z3 Lemma 3.2,
referee's definition of flipped); at flipped (C1) coordinates (z_s eps < 0) and at the s_m, phi_{z^(2)}(x) <= 2|x| and |B_+(j)| + |B_-(j)| <=
|Delta B(j)| + phi_{z_j}(B_+(j)) + phi_{-z_j}(B_-(j)); on S^nat_{l''} the flipped v-mass is <= r^nat_{l''} <= b, so sum_{flipped} |Delta B| <=
l (6/t) b + 4b^2/t <= t^2, and |Delta B(s_m)| <= K_P t + t^7 (only the pinned donor and fine carriers live at s_m).  So C_S <= C(1 + N K_P), and
B_+ 1_{F^c} = chi V' + e_+, B_- 1_{F^c} = -(1 - chi) V' + e_-, ||e_+-||_1 <= (K_U + C(1 + N K_P)) t.
Step 5 (data at f^#; NEW balancing and supports).  Define
   omega^+_m := clamp of omega_{+,m} with gap^# (Definition def:windowcert at f^#) at coarse strict non-peaks of f^# that are not k(l''),
   l'' in Kp(w); 0 at peaks of f^#; omega^+_m(k(l'')) := omega_{+,m}(k(l'')) for l'' in Kp(w);
   omega^-_m := omega^+_m + sum_{l'' in Kp, m(l'')=m} (eps tau'_{l''}/lambda_{l''}) e_{k(l'')};
   b^+ := B_+ 1_F + chi V' - kappa a/a(zhat^#),  kappa := (B_+ 1_F + chi V')(zhat^#)   (Y4-ref B.4: balance with the ORIGINAL a);
   b^- := b^+ - sum_{Kp} eps tau' u;    g_t := b^+ + sum_m R_m^*(omega^+_m - d^#_m(omega^+_m) w^#_m),
and at kept (K4) coordinates apply the SHIFT TRICK (Y1 Step 5, Y1-ref (d)): move omega^+-(k) by the same x with vs x := (-1.5 gap^#(k)/t
- vs omega^-(k))_+.  [a(zhat^#) = ||a||_1 + nu^2 (nu^2 + ||X||^2)^{-1/2} in [1 - ||X||^2/nu, 1] by (3.1), X the total off-F mass vector.]
 * Two-piece admissibility at f^#: off F^#, b^+ = chi V' and b^- = -(1-chi) V' are z^#- resp. (-z^#)-signed in K^# and vanish at free
   coordinates (Step 3); on F^# no condition; omega^+- are finitely supported in the strict non-peak sets of f^# (Lemma ST(c): every kept
   carrier is a strict non-peak of f^#).  Second representation: b^+ - b^- = sum_{Kp} eps tau' u = sum_m R_m^*(omega^-_m - omega^+_m).
   d-neutrality: d^#_m(omega^-) - d^#_m(omega^+) = sum_{Kp, m} (eps tau'/lambda) Phi^2 w^#(k)/C^# = Q^#_m(tau') = 0 (Step 3).  The shift leaves
   omega^- - omega^+ unchanged.  b^+(zhat^#) = kappa - kappa = 0, and b^-(xi^#) = g_t(xi^#) = b^+(xi^#) = 0 (Lemma lem:algebra at f^#).
 * (iv): at j in Pu (j = j_{l''}), V'(j) = eps tau'_{l''} v_{l''}(j) (only l'' lives there among coarse carriers), so t|b^+-(j)| <= t tau' v(j) <=
   12 lambda v(j) = mu_{l''}/2 <= |a^#(j)| (q*(A^#) <= 2) — this is Y4-ref Lemma P3; at tuning banks V'(j') is z^(2)-signed and z^(2)_{j'} =
   z^#_{j'}, so b^+ = chi V' and b^- = -(1-chi)V' are contact-like; at donor coordinates s_m, b^+- = 0.  The term kappa a/a(zhat^#) lives on F.
 * Estimates (ii): g - g_t = (e_+ + kappa a/a(zhat^#)) + sum_m R_m^* X_m, X_m := Theta_{+,m} - omega^+_m + d^#_m(omega^+_m) w^#_m.
   |kappa| <= |B_+(zhat^#)| + (1 + ||U||)||e_+||_1 and B_+(zhat^#) = B_+(zhat) + sum_j B_+(j)(z^# - z)_j + <U^*B_+, e^# - e>: |B_+(zhat)| <=
   t/(2q_0) (Lemma lem:budget(a)); raised coordinates contribute <= sum (1 - |z_j|)|B_+(j)| <= t/(2q_0); flipped (C1) coordinates, the s_m
   and the pulls (|z^# - z| <= 2) contribute <= 2(t^2 + N(K_P t + t/q_0) + sum_{Pu} |Delta B(j)| + t/q_0), and sum_{Pu} |Delta B(j)| <=
   sum 6 lambda v(j)/t + t^7 <= 6 l 2^{G(l)} eta/t <= t^2; finally ||B_+||_1 <= C/t (Lemma lem:box) and ||e^# - e|| <= C Design Lam (Lemma CO),
   so |<U^*B_+, e^# - e>| <= C Design Lam/t <= t.  So |kappa| <= C(K_U + N K_P + 1) t.  The block part is estimated as in Y1 Step 5 / Z3
   Proposition T step (5) (fix T3): at kept coordinates omega^+ = omega_+ except for the shift, lambda|x| <= |tau - tau'| + lambda |Delta d| M
   (computed from Lemma lem:suplevel(f),(c): vs omega^-(k) >= vs omega_-(k) - |tau - tau'|/lambda - |Delta d| M and vs omega_-(k) >= -1.5 gap/t,
   gap <= b M <= gap^# at (K4)); clamped coordinates by the claim in the proof of Proposition prop:windowcert(c) (read at f^#), dropped carriers
   and status changes between f and f^# with the datum 0 (errors |tau| + lambda |Delta d| M, resp. 2 lambda gap/t + |tau| + lambda|Delta d| M with
   gap <= b); replacing (d, w, gap) by (d^#, w^#, gap^#) costs C_f c(delta)/t + (2/t) sum lambda |gap^# - gap| <= C theta_w t (Lemma CO, c(delta)
   <= theta_w T_lo^2 <= theta_w t^2); fine coordinates as in Proposition prop:windowcert(c).  Altogether p*(g - g_t) <= (1+||U||)||g - g_t||_1
   <= C_f (1 + G**)(K_U + N K_P + 1) t =: K_w t, and K_w <= C_f G**^2 l^2 D^6/u^4 <= C_f Design(l) u^{-4} (Design >= (l D G**)^6).
 * (i): t||b^+-||_1 <= A_0 as in Lemma lem:windowtwopiece(d) (||V'||_1 <= sum tau' <= 12 sum lambda/t <= 4/t; Lemma lem:finitebase on F).
   Gamma: sqrt(Gamma^#_w) is a seminorm at f^#; compare (b^+, omega^+ - d^# w^#) with (B_+, Theta_+): the difference is (e_+ + kappa a/a(zhat^#),
   X), contributing <= C K_w t (q_0^# h^#(y) <= ||U||^2 ||y||_1^2/nu^#, sigma^#_m H^#_m(X) <= (sum lambda|X|)^2/C^#_m).  For Gamma^#_w(B_+, Theta_+):
   (Hilbert part at CHANGED e; NEW) ||P^perp_{e^#} U^*B_+|| <= ||P^perp_e U^*B_+|| + 2||e^# - e|| ||U|| ||B_+||_1 <= (2nu/q_0)^{1/2} + C Design Lam/t,
   and Design Lam/t <= Design T_lo^2 <= theta_w; nu^#, q_0^# are within C Design Lam of nu, q_0; so |q_0^# h^#(B_+) - q_0 h(B_+)| <= C theta_w.
   (Block part; Z3-ref fix T3) |H^#_m(Theta) - H_m(Theta)| <= C ||D_m Theta||^2 (||D(w^# - w)|| + |C^# - C|) <= C t^{-2} C_f Design Lam log(1/Lam)
   <= C theta_w.  With Lemma lem:budget(d) at f: Gamma^#_w(B_+, Theta_+) <= 1 + eta_Gamma(eta) + C theta_w.  The - side likewise (compare with
   (B_-, Theta_-); on F, (B_- - b^-) 1_F = sum_G eps(tau' - tau) u 1_F + sum_{R, fine} Delta theta u 1_F + kappa a/a(zhat^#), as in Lemma
   lem:windowtwopiece(c)).
 * (iii): clamped coordinates are of kind [1] (Definition def:windowcert at f^#); (K1), (K2) have gap^# >= M^# u/2 >= gamma(w), (K3) have
   gap^# >= M^#/2 (Lemma ST(c)): kind [2] with |omega^+| <= 4/t, |omega^-| <= 4/t + 12/t (|omega_+| <= (3+eta)/t by Lemma lem:suplevel(e),
   tau'/lambda <= 12/t); (K4) after the shift: kind [3] (strict non-peaks of f^# by Lemma ST(c); inward up to 1.5 gap^#/t by the choice of x:
   vs omega^+ <= 1.5 gap/t <= 1.5 gap^#/t before the shift and the shift moves vs omega^+- up only when vs omega^- < -1.5 gap^#/t, to exactly that
   value, so vs omega^+ = vs omega^- - tau'/lambda <= 1.5 gap^#/t); before the shift |omega^+| <= 4/t, |omega^-| <= 16/t, the shift has
   |x| <= |omega^-| + 1.5/t <= 17.5/t, so afterwards |omega^+| <= 21.5/t and |omega^-| <= 1.5/t: A_2 = 22 suffices.  QED

## 4.2 Theorem E'' (Theorem E with window-dependent constants, banked and pulled supports).  PROVED.
Let f_j -> f in S_{p*} with supp a_j = F ∪ Ba_j ∪ Pu_j (finite), Ba_j contacts of f carrying masses of sign z at f_j, Pu_j coordinates where
z_j = -z (pulls), and suppose that for every j and every scale t of a window (T_j, n_j) there are d-neutral two-piece data at f_j satisfying
(E-a), (E-b) (kinds [1], [2], [3] with A_2 fixed, gamma_B(j) window-dependent; kind [1] may be relaxed to [1']: gap > 0, |omega| <= 2 gap/t),
(E-c), (E-d'), (E-e') of Y1/Y2 Theorem E', and in addition: the data are contact-like on Ba_j and t|b^+-(i)| <= |a_j(i)| for i in Pu_j.
Then (f, rho g) in cl NA((c_0, p), l_2^2).
Proof.  Theorem E' (Y1 5.3, Y2 2.2; refereed) uses Lemma U' at f_j.  In Lemma U (proofs of Lemmas lem:uniformtransfer, lem:onesidedtransfer)
the base support enters only through the excess term Exc(rb) of Lemma lem:bookkeeping(b) (no flips): on F, a_{j,min,F} -> a_min > 0 as
before; on Ba_j, contact-like data give |a_j(i) + r b_i| - |a_j(i)| - z_i r b_i = 0 for r of the side's sign (Y4 Lemma 2.3, refereed); on Pu_j,
|r b(i)| <= c_flat t |b(i)| <= |a_j(i)| (c_flat <= 1/8), so a_j(i) + r b(i) keeps the sign z_j(i) of a_j(i) and the excess vanishes (Y4-ref
Lemma P2, re-verified here); off supp a_j the side conditions at f_j.  All other constants (nu_j, q_0^(j), sigma_{j,m}, C_{j,m}, M_{j,m},
transfer data via Lemma lem:persistence) depend only on the convergent forced data.  Kind [1'] is Y1-ref Section 4.  The final step
applies Corollary cor:D1 at the fixed f_j (finite base support) to the averaged data, which are d-neutral two-piece data at f_j: contact-
likeness on Ba_j, the side conditions and d-neutrality are linear or convex conditions, preserved by averaging; nothing is required at
support coordinates.  QED

## 4.3 MASTER THEOREM II (design D_Omega, diagonal base).  PROVED.
Let T = D_Omega, N >= 1, f in S_{p_N^*} with finite base support F.  Suppose that for infinitely many levels l there is a clean sub-window
w of level l (one exists at EVERY level, Theorem 2') at which
   (SH_w)  every block has an upper and a lower shift source at w, or the shift cost of the source-deficient blocks is robust,
           c_{pi(w)}(f) >= u(w)   (part 2, 2.5);
   (VR_w)  every extreme ray of the zero-cost cone C(kappa(w)) has at most one robust d-component   (part 2, 2.6).
Then f in Rec: (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f).
No donor hypothesis, no compensation or one-signedness, no nearly-neutral hypothesis, and no rate or growth condition is imposed: rooms,
target rooms, margins (weak, DEGENERATE), gaps, relative d-coefficients and ray d-sums are arbitrary; contact sets, slaving, the number of
swallowed carriers and the alignment of the far signature tails (the "aligned corner") are arbitrary.
Proof.  Fix g in C(f), rho in (0,1), eta_0 in (0,2] with rho^2(1 + eta_0) <= (1 + rho^2)/2, kappa_0 := (sqrt(1 + eta_0/2) - 1)/2, and eta <= eta_*
with eta_Gamma(eta) <= 1 and sqrt(1 + eta_Gamma(eta)) <= 1 + kappa_0/2.  Along the given levels l_j -> infinity (l_j >= l_f) take w_j := w(l_j),
f_j := f^#_{w_j} (part 3), T_j := T_hi(w_j), n_j := n(w_j), and for every dyadic t in W(w_j) the functional g_{j,t} := g_t of Proposition TR.
Check Theorem E'':  supp a_j = F ∪ Ba_j ∪ Pu_j, f_j -> f since p*(f_j - f) <= theta_{w_j} T_lo(w_j)^2 -> 0 (Lemma CO).  (E-a): Proposition TR(i),
Gamma <= (1 + kappa_0/2 + C theta_w + K_w t)^2 <= 1 + eta_0/2 once C theta_w + K_w T_hi(w) <= kappa_0/2 (true for large j, below).  (E-b):
Proposition TR(iii), A_2 = 22, gamma_B(j) = gamma(w_j).  (E-c): Proposition TR(ii).  Supports: Proposition TR(iv).  (E-d'): K_w <= C_f Design u^{-4}
and c_flat(w) >= c_0 gamma(w)/A_2 >= c_f u(w) (Lemma U'); with Q(w) = (4 Design/u)^{omega+20}: K_w T_hi(w) <= C_f Design u^{-4} 2^{-l^3}/(l Q(w))
<= C_f 2^{-l^3}/l -> 0, and n(w) c_flat(w)/K_w >= l 2^{l^3} Q(w) c_f u^5/(C_f Design) >= l 2^{l^3}/C_f -> infinity.  (E-e'): eps_j <= theta_w T_lo^2 with
theta_w = C_f Design T_lo log(1/T_lo), while c_flat(w)^2 >= c_f u^2 and T_lo(w) <= 2^{-n(w)} <= 2^{-Q(w)} <= 2^{-(4/u)^{20}} (and Design <= Q^{1/20}):
theta_w <= c_f u^2 (1 - rho^2)/(24 rho^2) for large j; also eps_j <= (1 - rho^2) r_0^2/6 eventually.  t <= min(t_eta, t_1, 1) on W(w_j) for large j.
Theorem E'' gives (f, rho g) in cl NA; rho < 1 was arbitrary and cl NA is closed.  QED

Corollaries (PROVED from 4.3).
 (M-II.1) [one block] For N = 1, (VR_w) holds at every w (every ray lives in the single block).  Hence for D_Omega and N = 1: f in Rec
          whenever (SH_w) holds at a clean sub-window of infinitely many levels.
 (M-II.2) [single-block rays] If, for infinitely many levels, at some clean w every extreme ray of C(kappa(w)) is supported in one block and
          (SH_w) holds, then f in Rec.  In particular Y1's hypotheses (Do_w) [donors], (NN_w) [nearly neutral carriers] and the one-signed
          alternative of (Cmp_w) are never needed (one-signed blocks carry no robust component, part 2 Remark (2)), and Y1's (SP_w) is the
          special case I_up ∪ I_lo = {} of (SH_w).  The compensated alternative of Y1's (Cmp_w) is NOT contained: Y1 5.4 also covers rays with
          robust components in several COMPENSATED blocks (part 5, 5.3).
 (M-II.3) [maximal contact] F finite, z = eps_0 off F: (SH_w) holds at every clean w of large level (Z4 Lemma 5.0: every block has non-degenerate
          peaks of both kinds with margins >= q_0/4, i.e. sources (L2) and (U2)); so f in Rec whenever (VR_w) holds at a clean sub-window of
          infinitely many levels — in particular for N = 1 always.
# V1 part 5 — The aligned corner (D), far pulls on the peak itself, the residual list and its exhaustiveness

## 5.1 Corollary AC (the aligned corner is empty for D_Omega).  PROVED.
For D_Omega (diagonal base), N >= 1, F finite and every clean sub-window w of level l >= l_f, EVERY block has a threshold donor: a coarse
peak c with rho_c >= 1 + u(w) (Lemma D), dropped or of class R, at whose first far signature coordinate s = min(S_c ∩ (s_max(l), inf)) the
move (C3) raises |u_c(zhat)| by Lam/lambda_c ... 3Lam/lambda_c, Lam = T_lo(w)^3, either by a z-move (when the room toward vs_c carries at least
Lam/lambda_c) or by closing z_s := vs_c and placing a BANK of mass <= Design(l) Lam at s (Lemma DR); the block threshold rises by >= c_f Lam
(Lemma ST(b)) and every kept near-threshold swallowing-type carrier (weak, DEGENERATE, or tiny-gap strict non-peak) becomes a strict
non-peak of f^#_w (Lemma ST(c)), while all d-coefficients of the block are rescaled by the common factor A_m/A^#_m up to C_f Design b.
Consequently Y1's residual (d), Y2's aligned corner (d') and Y2's hypothesis (TD_m) are not needed for D_Omega: Master Theorem II has no
donor hypothesis.
Why the corner was open, and why banks close it.  Y1's and Y2's companions keep the base part a (hence e, nu) fixed and move only z;
a z-move raises |u_c(zhat)| at a coordinate s in S_c only if z_s != vs_c (room toward the peak's own sign).  The aligned corner is exactly
the case where every far coordinate of every usable peak is a CONTACT OF THE PEAK'S OWN SIGN (z_s = vs_c), so no z-move can push a peak
outward (and Y2-ref Lemma R-T's target moves may all have zero derivative).  A BANK at such a contact (mass vs_c mu at s, z unchanged) moves
the Hilbert part: by (3.1), vs_c u_c(zhat) increases by mu s_s^2 v_c(s)/nu + O(mu^2), every other coarse value changes only at second
order (diagonal base: <U^*u_k, k_s> = s_s u_k(s) = 0 for k != c), so the peak is pushed OUTWARD and the threshold rises (Lemma T2(b)).
Y4 Proposition 2.8(b) (banks only raise z-signed functionals) is not an obstruction here: raising the donor's value is exactly what is
needed.  Banks are admissible in Theorem E (Y4 Lemma 2.3; Theorem E'' here).  Numerics: V1_work/bank_donor_check.py (finite model,
diagonal base; in the regime mu <= 0.05 s^2 v nu: 140/140 raises; first-order formula exact up to 0.65 mu^2; other carriers move <= 0.37 mu^2;
when Lemma T2(b)'s hypothesis holds the raise is >= 11 x its lower bound).

## 5.2 Lemma IP (far pulls on the peak itself: inward push of near-threshold coordinates).  PROVED.
Fix a block, zeta in l_1 \ {0}, theta := theta(zeta), A := |zeta|, nu_k := |zeta(k)|/Phi_k^2.  Let 0 < b <= 1/2, N a nonempty set of coordinates
with |nu_k - theta| <= theta b (k in N), c >= 4b(A + theta), and let zeta' satisfy: for k in N, sgn zeta'(k) = sgn zeta(k) and |zeta'(k)| =
|zeta(k)| - c_k Phi_k^2 with c_k in [c, theta/2]; for k notin N arbitrary changes with E := sum_{k notin N} |zeta'(k) - zeta(k)| <=
theta c sum_{k in N} Phi_k^2/(8(A + theta)).  Then theta(zeta') > theta, and nu'_k <= theta(zeta') - (c - theta b) for every k in N: every pushed
coordinate is a STRICT NON-PEAK of zeta' with nu-gap >= c - theta b >= c/2.
Proof.  Put x := theta.  A'(x) = sum_k (|zeta'(k)| - x Phi_k^2)_+: for k in N, |zeta'(k)| - theta Phi_k^2 = Phi_k^2(nu_k - c_k - theta) <= Phi_k^2(theta b - c)
< 0, so N contributes 0; for k notin N the terms change by at most |zeta'(k) - zeta(k)|; and A = sum_{P}(|zeta(k)| - theta Phi_k^2) with the N∩P
terms <= theta b Phi_k^2.  Hence A'(theta) >= A - y, y := theta b sum_N Phi^2 + E.  B'(x) = sum_k Phi_k^2 min(x, nu'_k)^2: for k notin N the terms
change by at most 2 theta |zeta'(k) - zeta(k)| (|min(x,a)^2 - min(x,a')^2| <= 2x|a - a'|); for k in N, min(theta, nu_k) >= theta(1-b) and
0 <= nu'_k = nu_k - c_k <= theta(1+b) - c_k, so the term drops by >= Phi_k^2[theta^2(1-b)^2 - (theta(1+b) - c_k)^2] = Phi_k^2 (c_k - 2 theta b)(2 theta - c_k)
>= Phi_k^2 theta (c - 2 theta b) (as c_k <= theta/2 <= theta).  So B'(theta) <= B - theta(c - 2 theta b) sum_N Phi^2 + 2 theta E.  Using B = A^2
(Lemma T(b)) and A'^2 >= A^2 - 2Ay (if A - y >= 0 since A' >= A - y; if A - y < 0 the right side is negative):
   Psi'(theta) >= -2A(theta b sum_N Phi^2 + E) + theta(c - 2 theta b) sum_N Phi^2 - 2 theta E = theta sum_N Phi^2 (c - 2b(A + theta)) - 2(A + theta)E
              >= theta sum_N Phi^2 c/2 - theta c sum_N Phi^2/4 > 0.
By Lemma T(c), theta(zeta') > theta.  Finally nu'_k = nu_k - c_k <= theta(1 + b) - c < theta(zeta') - (c - theta b).  QED
Numerics: V1_work/lemma_ip_check.py (E = 0: 2962 tests, 0 violations; the gap bound is attained up to 1e-7) and lemma_ip_check2.py
(E > 0 up to the allowed size: 3942 tests; the gap conclusion holds in all of them; theta' > theta holds in all cases where the predicted
raise is above double-precision resolution — the 13 remaining cases have predicted relative raise 4e-20..3e-17 and return theta' = theta
exactly in floating point).
Reading.  This turns Y4-ref C.8(ii) ("tiny-margin swallowing-type peaks are pushed below threshold by a pull", SKETCH) into a theorem at
the block level, for any number of near-threshold coordinates pushed simultaneously, and shows that a push much larger than the margin
RAISES the threshold (the margin part of the push lowers it at rate A/((A+theta) sum_P Phi^2), Y2-ref 1, but once a coordinate crosses the
threshold the inward push raises it, Lemma T(d)(ii); net effect positive as soon as c >= 4b(A + theta)).  Per carrier, a pull at j in S_l with
2 m v_l(j)/Phi_l in [c, 2^{G_l} c] realizes c_l (bounded gaps), at cost O(v log 1/v) (Y4-ref P1).  It is NOT used in the assembly: pushes
that dominate the threshold drift (c >> Design b) move the d-components of rays through the pushed carriers by amounts between b and u,
destroying the tiny/robust dichotomy of (R5) on which the exact tuning rests; the donor raise rescales all d-coefficients of a block by one
common factor and moves no value, so it is compatible with the tuning.  Lemma IP is the right tool when no tiny d-component passes through
the near-threshold carriers (e.g. single-carrier blocks).

## 5.3 The residual list for D_Omega, F finite (contrapositive of Master Theorem II).  PROVED (as a logical statement).
Let T = D_Omega, N >= 1, f in S_{p_N^*} with F finite.  If f notin Rec, then there is l_0 such that for EVERY level l >= l_0 and EVERY clean
sub-window w of level l at least one of the following holds:
 (B_w) [genuinely multi-block ray]  some extreme ray r of the zero-cost cone C(kappa(w)) has ROBUST d-components in two different blocks:
       |sum_{l'' in supp r, m(l'')=m_i} r(l'') eps_{l''} u_{l''}(zhat)| >= u(w) Phi_max(r, m_i), i = 1, 2, m_1 != m_2;
 (C_w) [coherent shift resonance]  some block has no upper or no lower shift source at w (I_up(w) ∪ I_lo(w) != {}), and the shift cost of
       the shift pattern of f at w is TINY: c_{pi(w)}(f) <= b(w).
(D) is EMPTY (Corollary AC).  (E) (infinite F) is outside the statement.
Exhaustiveness (checked item by item).  Master Theorem II has exactly three hypotheses: F finite; (SH_w); (VR_w), at one clean sub-window
of infinitely many levels.  Clean sub-windows exist at every level (Theorem 2').  At a clean w every rate object is tiny or robust, so
NOT (SH_w) <=> (C_w) and NOT (VR_w) <=> (B_w).  Every other ingredient holds unconditionally for l >= l_f(f): donors (Lemma D), the
threshold buffer (Lemma ST), exact tuning (Lemma TU: the tuning system is always consistent, V^(2) = R val^(2), and its size Design b is below
c_T), no slaving (Lemma NS), robust rates (Lemma RR), Hoffman constants (G**, H_tune: design constants), zero cost at f^# (Step 3 of
Proposition TR), the supports of Theorem E'' (Proposition TR(iv)), the window arithmetic (proof of 4.3).  No growth condition, no rate
condition, no compensation, sign or donor condition, and no hypothesis on contact sets, slaving or degenerate peaks remains.
Precisions.  (1) Both items are properties of f at level l and of the explicit numbers b(w), u(w) only; (B_w) is combinatorial-linear
(values of finitely many carriers on finitely many extreme rays), (C_w) is a convex-analytic condition at f.  (2) (B_w) never occurs if
N = 1, nor through blocks that are one-signed at w (Remark (2) of part 2).  (3) The residual of Lemma Z for D_Omega is SMALLER than the
list: f must in addition lie outside every other class proved recoverable for D_Omega (Theorem 1'(d)): R_0^pm, R_S, R_BT (Cor. D2 of S3),
Z4 Theorem A'', Z6 Theorem U', Y2 Theorem Y, Y1 Master Theorem 5.4 (with (SP_w) replaced by (SH_w): Y1's proof uses (SP_w) only through
the shift bound, which Lemma S provides; with its own z-move donors (Do_w)), and the infinite-F classes of Z5/Y3 do not apply (F finite).
In particular the part of (B) in which every block met by a doubly-robust ray is COMPENSATED at w (Y1's (Rep^+_m), (Rep^-_m) at f^#), all
other blocks are one-signed, (NN_w) holds and z-move donors exist, is covered by Y1 5.4.  (4) (C_w) with c_pi > 0 but tiny is not exactified:
c_pi is computed at f (pinning at f), and no companion move changes the decomposition at f.

## 5.4 What is new, and what remains
NEW (PROVED here): bank donors (Lemmas D, DR, Corollary AC: aligned corner empty); exact tuning with an explicit solution (Lemma TU,
re-proving Y4-ref P4 with design constants); the ray-component rate objects (R5) and exact neutralization of all tiny components by one
least-norm solve (Lemma CO, NS), replacing (Cmp_w)/(NN_w) by (VR_w); the clean-window shift-cost lemma (Lemma S, port of Y2 Prop. 5.2 with
I_up ∩ I_lo = {} from Lemma D); the assembly (Lemmas CO, ST, NS, RR; Proposition TR: split w.r.t. z^(2), balancing with a/a(zhat^#),
Hilbert comparison at changed e, supports for Theorem E''); Theorem E''; Master Theorem II and Corollaries M-II.1 (N = 1) and M-II.3
(maximal contact); Lemma IP.
OPEN for D_Omega, F finite: (B) genuinely multi-block rays (vector-valued d-rows; the Hoffman constant of {mu >= 0 : sum mu_r D_r = 0} is
governed by minors of the ray d-matrix, the rate objects (R7); tiny-but-nonzero minors are not exactifiable by value tuning without
destroying robust components — determinantal); (C) coherent shift resonance.  (E) infinite F (O4-crit, O4-nd, O4-box) as in ADDENDUM 6.
Lemma Z, and density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2), remain OPEN for every admissible T, including D_Omega.  No
counterexample is claimed; nothing found points to one.
