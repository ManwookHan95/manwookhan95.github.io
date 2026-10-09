# Y4 referee, part 1 — Part 1 of Y4 (designs, clean sub-windows, ray removal)

Checked against: paper/martin_density_note.tex (Def. def:SLD, Thm thm:SLD, Lemmas box/pinning/triangular, Prop. pinned,
window certificate, Thm windowed, Thm thm:reductionZ, Toward Lemma Z incl. Def. def:swallowed, Lemmas modswallow,
badpeaks, exactswitch, windowtwopiece, onesidedtransfer, Thm S, Rem. openZ), r5/Z3_ref_part4.md (explosive design
(D1^F), Lemmas 4.1.1, 4.1.2, Props 4.2.1, 4.3.1), r5/Z6_ref_notes.md 3.3 (design D'''), r5/Z3_notes part 2-3 (Lemma U,
Thm E, Lemma 3.1, Prop T), Z3_referee (fixes G1-G8).

## 1.1 Proposition 1.2 (explosive design, per-carrier rates). VERDICT: correct (counting); consequence needs a design tweak.
Re-derivation.  Cantor pairing j(k,m) = (k+m-1)(k+m-2)/2 + m.  With s = k+m-1 >= 1, the values with given s are
s(s-1)/2 + m, 1 <= m <= s, i.e. the block (s(s-1)/2, s(s+1)/2]: j is a bijection N x N -> N, and for fixed m it increases
with k, so (D0) holds.  If j(k,m) <= L then s(s-1)/2 < L, so s - 1 < (2L)^{1/2} and k <= s < (2L)^{1/2} + 1; hence
|L_N cap [1,L]| <= N((2L)^{1/2} + 1).  Bands Band(l) = (b(l),u(l)) of (D1^F) are pairwise disjoint (Z3_ref Lemma 4.1.2,
re-checked: u(l+1) <= b(l) by the third term of F(l+1), b(l) <= 4^{-2F(l)} < F(l)^{-1/(4l)} = u(l)).  Choosing one
blocking pair (l,i) per blocked window gives an INJECTIVE map (if two windows got the same pair (l,i), rho_{l,i} would lie
in two disjoint bands).  So #blocked windows in [1,L] <= R N((2L)^{1/2}+1) = o(L).  PROVED as stated.
Gaps in the surrounding text (all minor, fixable):
 (a) Absorption with R types.  Blocking is only half of the story: at an unblocked window the ROBUST objects must be
     pinned with constants absorbed by n^w_l ~ F(l)Lambda°(l).  Z3_ref Prop 4.3.1(a) uses u^{-|P|} <= u^{-l} = F^{1/4}
     for ONE rate per carrier.  With R multiplicative rate types per carrier the product can reach (4/u)^{Rl} =
     4^{Rl} F^{R/4}, which is NOT absorbed for R >= 4.  FIX: in (D1^F) put u(l) := F(l)^{-1/(4Rl)} and
     F(l+1) >= b(l)^{-4R(l+1)} (R is a design constant); Lemma 4.1.2 and Prop 4.2.1 go through verbatim.  (For rates
     entering additively -- margins, Hoffman constants of single objects -- no change is needed.)
 (b) "Per-carrier" is inaccurate for two of the listed types: slaved rooms (l, A) (A a subset of later carriers) are
     2^{l_*}-fold joint objects, and target rooms (R2) are per COORDINATE (|supp y_l| objects for carrier l, unbounded in
     l since the targets are dense).  Prop 1.2 covers (R2) only under an extra design restriction, e.g. |supp y^{(i)}| <= i
     and i_r <= r^{1/2} (allowed by Def. def:SLD), which makes sum_{l in L_N, l <= L} |supp y_l| = O(N L^{3/4}) = o(L).
     Slaved rooms are not covered by Prop 1.2 at all (Z3_ref needed the hypothesis (S-flat) for them).  The pigeonhole
     design D^PW (below) covers both, since it only needs a design bound omega(l) on the number of objects.
 (c) Remark after the proof: correct (a general (D0) bijection may give L_N positive density; then only R = 1 works).

## 1.2 Observation 1.3. VERDICT: correct.
One-signed blocks: for an extreme ray r >= 0 of the combinatorial cone with q_l of one sign on supp r,
|sum q_l r(l)| = sum |q_l| r(l) >= min{|q_l| : l in supp r, q_l != 0} x (least nonzero coordinate of the finitely many
normalized extreme rays of level l), a design constant.  Mixed blocks: cancellation makes ray d-sums independent rates
(counting argument fails).  The nested-construction remark is correctly labelled HEURISTIC/OPEN.  (Bound
binom(P, m-1) for the number of extreme rays of a cone in R^m with P facets: standard.)

## 1.3 Definition 1.4 / Lemma 1.5 (pigeonhole design D^PW). VERDICT: correct with two fixable gaps.
Re-derivation.  Recursion well defined: at stage l, Design(l) (the D''' factor l 2^{l^3} Lambda°(l) Xi'(l), which uses
only data of index <= l, incl. Phi_{l''} = 2^{-m-k}c_{l''}, l'' <= l) and omega(l) are fixed; the M(l) sub-windows are
defined in order; then c_{l+1}.  (a): T_hi(w) l Q(w) 2^{l^3} <= 1 and n(w) >= l 2^{l^3} Q(w) by definition;
T_hi(w^+) <= T_lo(w) by the min; fine carriers at any sub-window (l,i): sum_{l'>l} lambda_{l'} <= sum_{l'>l} c_{l'}/4 <=
c_{l+1}/2 <= T_lo(l,M(l))^3/2 <= T_lo(w)^3/2, so sum_{l'>l} |Delta theta_{l'}| <= 6 sum lambda/t <= 3 t^2 (better than
stated).  (b): T_lo(w) <= 2^{-n(w)}, n(w) >= Q(w) >= 4/u(w) (omega >= 1, Design >= 1), so b(w) <= 2^{-4/u(w)} < u(w)
(x < 2^{4x} for x = 1/u >= 2); u(w^+) = b(w); the bands are consecutive disjoint open intervals.  Admissibility and
N-freeness: the proof of Thm thm:SLD uses only (D0), allowedness and c_{l+1} <= c_l/4; omega(l) counts objects of ALL
blocks (N-free).  (c): every window proof uses the window only through its dyadic scales, coarse = index <= l, the box
bound for index > l, T_hi x (f-factor <= C_f^{l^2} x design factors of level l) -> 0 and n/(same) -> infinity, and
T_hi(next) <= T_lo(previous) (checked in Thm thm:R0, thm:Bstar, thm:Bpm, thm:S, Z3 Thm E/Prop T, Z6_ref 3.4).  OK.
Gaps:
 (G-PW1) Room-closing conversion factor.  The exactification cost of a tiny room (Z3_ref fix G5, Prop 4.3.1(b)) is
     <= C r (1 + 2^{s_max(l)}/delta_min(l)) because of target-induced terms min(lambda_{l''}, |y_{l''}(delta)|).  D''''s
     Design(l) does not contain 2^{s_max(l)}/delta_min(l) (1/m^nat does not dominate 2^{s_max}).  FIX: put
     Design(l) := l 2^{l^3} Lambda°(l) Xi'(l) (1 + 2^{s_max(l)}/delta_min(l)); nothing else changes.
 (G-PW2) The factor (1 + 3/rho) for robust objects is the right worst case only if every rate enters the pinning
     constants at most through such a factor times a design quantity of level l.  This holds for (R1) (1 + 3/r <=
     (1 + 3/rho)(1 + 1/delta°)), (R2) (C_0^# = max 1/(1-|z_s|)), (R3) (1/mu <= (1/rho)(1/Phi), 1/Phi in D(l)),
     (R4)-(R5) (Lemma 1.8: 1/D_min) -- and for gaps through c_flat <= gamma_B/(2A_2) (Z6_ref 3.6), which enters
     Thm E as 1/c_flat in n >= 48 rho^2 K/(c_flat(1-rho^2)) and as theta_j <= c_flat^2 (1-rho^2)/(24 rho^2):
     both absorbed (n(w) >= Q(w) and theta = C_f T_lo^2/l).  So Theorem 1.6's product bound is adequate, but Y4
     should say that (R3)-gaps enter through c_flat, not through a product.

## 1.4 Theorem 1.6 / Corollary 1.7 (clean sub-windows). VERDICT: Thm 1.6 correct; Cor 1.7 correct only as the
## conditional statement it is (the "exactify if tiny" half is not proved; see part 2).
Thm 1.6: each rate lies in at most one band (disjointness), each object blocks at most one sub-window in total, at most
|O_<=(l)| <= omega(l) of the omega(l)+1 sub-windows of level l are blocked; at a clean sub-window rho_O notin (b(w),u(w)).
Products: 1 + 3/rho <= 1 + 3/u <= 4/u for rho >= u, u <= 1.  b(w) = T_lo^4/(l Design).  PROVED.  (Typo: "any F" should
be "F finite", since rho_O is defined only there.)
Cor 1.7: the absorption arithmetic is right (K T_hi(w) <= C_f^{l^2} Q(w) T_hi(w) <= C_f^{l^2} 2^{-l^3}/l; n(w)/K >=
l 2^{l^3}/C_f^{l^2}; exactification cost C_f Design(l) b(w) log(e/b(w)) -- note the LOG factor of Lemma 3.1/Lemma 2.2,
harmless: <= C_f T_lo^4 (4 n(w) + log(l Design))/l = o(T_lo^2) since T_lo^2 n(w) -> 0).  But "exactification cost
C_f Design(l) b(w)" presupposes that each tiny object can be made EXACT by a move whose size is (design) x (rate) --
which is precisely what part 2 of Y4 says FAILS in the lowering direction.  So Cor 1.7 is a reduction, not a theorem
about recovery; Y4 says so ((X1)).  With the far pulls of my part 2 the single-object version becomes true in both
directions; simultaneous exactification (X1) remains an assembly question.
A further point Y4 does not mention: slaved rooms r*_l(A) depend on the set A of objects exactified at the chosen
sub-window; at a clean sub-window a tiny r*_l(A) with robust r_l forces l into the exactified set, which changes A;
since all pairs (l,A) are objects, the closure terminates in at most l steps (finite), but the final A must be computed
by this closure.  Fine, but should be said.

## 1.5 Lemma 1.8 (ray removal). VERDICT: correct.
Re-derivation: a polyhedral cone in the nonnegative orthant is pointed, hence generated by its extreme rays
(Minkowski-Weyl); ||sum mu_i r_i||_1 = sum mu_i because r_i >= 0, ||r_i||_1 = 1; with D(tau) = e > 0, S_+ :=
sum_{D_i>0} mu_i D_i >= e, theta := e/S_+, tau' := tau - theta sum_{D_i>0} mu_i r_i in C, D(tau') = 0, and
||tau - tau'||_1 = theta sum_{D_i>0} mu_i <= theta S_+/D_min = e/D_min.  PROVED.
Remarks.  (i) Use requires first projecting the actual amplitudes onto the combinatorial cone (H_comb, design) and then
removing; the combined bound is H_comb viol + (|D(tau)| + ||D|| H_comb viol)/D_min.  (ii) D_min is the least NONZERO
|D_i| over ALL extreme rays: one tiny ray ruins it, which is why Y4 needs exact neutralization of tiny rays.  In a
compensated block (robust rays of both signs) one does NOT need Lemma 1.8: ADDING (e/|D_-|) r_- for a robust ray r_- of
the opposite sign neutralizes the mismatch e at l_1-cost e/u regardless of tiny rays (Y4 2.4(iii) says this correctly).
(iii) Multi-block rays (vector-valued D): correctly flagged OPEN (m').
