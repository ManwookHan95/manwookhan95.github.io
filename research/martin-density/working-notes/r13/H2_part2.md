# H2 part 2: far windows of kind-(iv) carriers -- extended R-G, the cluster sweep, private minimality; idea (1)

Setting of H2_part1.md.  T_fin^{K2}: S_l = {2^l(2i+1) : i >= 1} (even integers, bounded gaps 2^{l+1}), v_l(j) = delta_l 2^{-j}/n_l on S_l;
rounds PRE / MAIN / CLUSTER (Q1 1.2); T(l) = union_{l''<=l} supp y_{l''}, s_max(l) = max(T(l) ∪ {1}); d(L) = sigma(L) + 6*2^{L+1} > s_max(L);
D(L) >= d(L); deep raise beyond J(w) > D(L) (K2 4.1); TU window [x_TU, x'_max] of J1-ref P-TU; Brouwer radius W (K-7).

## 2.1 Extended R-G.  PROVED.
LEMMA 2.1.  If a main stage L (clean sub-window w, class a) carries a near-certificate of size <= eps_* and has no thick-type carrier,
then |a_s| <= b(w) for every s in F ∩ [1, D(L)] \ T(L)  (not only for s in (s_max(L), D(L)], J1-ref Observation R-G).
Proof.  (R-mod') makes every |a_s|, s <= D(L), tiny (<= b) or robust (>= u) at f; the deep raise acts beyond J(w) > D(L) and (P3) only
raises thin moduli to theta_0 <= b, so at R_1 the alternatives are <= 2b and >= u/2.  Let s in F ∩ [1, D(L)] \ T(L) be robust.  If s notin U_L,
s is an ANCHOR and K2.17(b) excludes every near-certificate.  If s in U_L, s in supp u_k = supp y_k ∪ S_k for a coarse k; s notin T(L) ⊇
supp y_k forces s in S_k; no other coarse carrier lives at s (signature sets are disjoint; their targets lie in T(L)), so s is a thick PRIVATE
coordinate of k in S_k ∩ [1, D(L)] and k is thick-type (J1 1; K2.16(2b) uses only privacy and v_k(s) >= v_min(L) >= 1/Design(L)).  QED

## 2.2 Where signature coordinates enter the targets.  PROVED.
LEMMA 2.2.  For every stage l: T(l) ∩ (union_k S_k) ⊂ [1, l].
Proof.  Main targets: allowedness (a), (c+) of Q1 1.2(r.1) give supp y ∩ S_{l'} ⊂ [1, p - 2|supp y| - 1] for l' < p and = {} for l' >= p.
PRE/CLUSTER absorber targets (Q1 1.2(r.2), (r.4)): support {s} ∪ {p_0 < ... < p_R} with p_i ODD (hence in no S_k) and s in Sigma(Y_r)
(signature coordinates of the next main target, < its stage) or s in E^ch(p) = T(p) ∪ union_{l''<=p}(S_{l''} ∩ [1, p]); induction on l.  QED

## 2.3 The cluster sweep.  PROVED.
LEMMA 2.3 (cluster sweep).  Let p be a main stage, w a sub-window of p, l <= p a coarse carrier, and j in S_l with v_l(j) >= x_TU(w)/C_0
(any absolute C_0 >= 1; this contains the TU window and the aggregated-pull range of 2.4).  Let p' be the next main stage.  Then
 (a) j < s_max(p + 1) <= s_max(p') < D(p')  and  j notin T(p');
 (b) if p' carries a near-certificate and has no thick-type carrier (i.e. p' is an (R1) stage at its selected sub-window w'), then
     |a_j| <= b(w') for every such j in F.  In particular |a_j| <= b(w') << x_max(w): NO coordinate of the TU window of any carrier at stage p
     is super-thick, and every in-F coordinate there is super-thin.
Proof.  (a) Depth of j: v_l(j) = delta_l 2^{-j}/n_l >= x_TU(w)/C_0 gives j <= log_2(C_0/x_TU(w)) + 1 <= 4 log_2(1/T_lo(w)) + C log_2 Design(p)
(x_TU >= x = C Design(p) eta' >= T_lo(w)^4/p).  The first cluster stage p+1 carries an absorber target with p_R >= p_0 + 2R, R = R(p+1) the
least integer >= 1 with 2^{3-R} <= mu_{p_0}^2 lb_{p+1}^2/4, and lb_{p+1} <= c^max_{p+1} <= c^cl(p) <= exp(-1/T_lo(p, M(p))) by (W_exp) (Q1 1.3(S4));
so R >= 2 log_2(1/lb_{p+1}) >= 2/T_lo(p, M(p)) and s_max(p+1) >= p_R >= 4/T_lo(p, M(p)).  Since T_lo(p, M(p)) <= T_lo(w) (sub-windows are
nested downwards, T_hi(w) <= T_lo(w^-)) and Design(p) <= T_lo(w)^{-1/2} (T_lo(w) <= 2^{-n(w)}, n(w) >= Q(w) >= (4 Design(p)/u)^{20}),
j <= 5 log_2(1/T_lo(w)) < 4/T_lo(w) <= s_max(p+1).  s_max is nondecreasing and D(p') >= d(p') > s_max(p').  For j notin T(p'): by Lemma 2.2
it suffices that j > p'.  p' = p + R_cl(p) + (PRE stages of the next round) + 1 with R_cl(p) = 2|E^ch(p)| <= 2(s_max(p) + p) and at most
2|supp Y| PRE stages, Y the next main target, allowed at p' only if its signature coordinates are < p'; so p' <= 3p + 2 s_max(p) + 2|supp Y| + 1,
a number bounded by a design number of the round, while j >= log_2(1/x'_max(w)) - log_2(C_0 delta_l) >= 2 log_2(1/T_lo(w)) >= 2 n(w) and
n(w) >= p 2^{p^3} Q(w) with Q(w) >= Design(p)^{20} >= 2^{20 s_max(p)}.  [If the next main target Y is large, p' grows with |supp Y| but Y is
fixed by the schedule before f; for the finitely many rounds where 2|supp Y| >= n(w) nothing is claimed -- l_f absorbs them: rounds are
indexed independently of f, and n(w) -> infinity along main stages faster than the schedule's supports, which are those of a fixed
enumeration; we impose (harmless, design-level) that the pool enumeration satisfies max supp y^(i) <= i and i_nu <= nu, so |supp Y| <= r.]
(b) By (a), j in F ∩ [1, D(p')] \ T(p'); Lemma 2.1 at p'.  b(w') <= T_lo(w')^4 <= T_lo(p, M(p))^4 << T_lo(w)^2/(p Design(p)|Lambda|) = x_max(w).  QED
Remark.  No design change is needed for (a) except the bookkeeping clause on the enumeration (which only constrains the ORDER of the
countable target pool; every property of T_fin used elsewhere -- density of the targets, allowedness, Martin's Lemma B -- is unaffected).

## 2.4 Private minimality of kind-(iv) carriers.  PROVED.
For a data-carrying coarse carrier l with switching sign eps_l at stage (L, w) define its PULL CAPACITY
      Cap_l := sum { (1 + eps_l z_1(j)) v_l(j) : j in S_l, c_0 W <= v_l(j) <= x'_max, j pullable (K1 2.0) },     c_0 := 1/32.
LEMMA 2.4 (aggregated pulls).  If Cap_l >= 4W', W' the Brouwer radius of the stage (after pre-placements), then l has a pre-placeable
two-sided TU lever on the whole Brouwer domain: pre-place the pulls at all pullable j of the range with c_0 W <= v_l(j) <= x'_max (pull mass
24 lambda_l v_l(j) of sign -eps_l, after lowering if j in F) and a compensating base bank at a near S_th coordinate; then l is of kind (i).
Proof.  V1 Lemma TU / K1 2.1(b) with several pulls: the total downward shift is Cap_l >= 4W'; the bank provides every upward correction
continuously; cross effects are second order (each pull C_T v^2, sum <= C_T x'_max Cap_l); cushions at each pulled coordinate as for one
pull (24 lambda_l v_l(j) >= t|V(j)|); cost <= C Design sum v log(1/v) <= C Design x'_max log(1/T) (R-6 budget, the range has geometric
v-decay along S_l so the sum is <= 2 x'_max); P-TU: every point of the Brouwer domain moves the bank by <= W' <= Cap_l/4.  QED
So K1/J1's (U) (no pullable coordinate in [x_TU, x'_max]) may be refined to (U'): Cap_l < 4W'.  Below, "kind (iv)" means (U').

LEMMA 2.5 (private minimality).  Let l be kind (iv) in the refined sense at an (R1) stage.  Then every admissible private move of l
(changes of the row only at coordinates of S_l, keeping the route-V data admissible: data-sign contacts or data-sign support at every
data-carrying private coordinate, cushions at anti-sign support, no data at free coordinates) changes val_l = eps_l u_l(xhat) by
      >= -( 4W' + 4 c_0 W + C D(L) eff_max (2b) + C c_{L+1} ),   eff_max := max_s mu_s^2 v_l(s)/nu <= 1,
i.e. by more than -9W'/2 is impossible: l has NO private downward lever at the Step-A scale, and its value is at the minimum of its private
range up to O(W').  In particular the TU-window coordinates, which by Lemma 2.3(b) are in F with s_j = -eps_l (anti-sign, super-thin), are
at the extreme z_j = -eps_l of their range.
Proof.  Private coordinates of l are of four sorts.  (1) Design depth, S_l ∩ [1, D(L)] \ T(L): by Fact 1.1(c) and Lemma 2.1 each is a data-sign
contact (banked with theta_0) or data-sign thin support (|a_s| <= 2b); a mass decrease lowers val_l by <= eff_s v_l(s)|a_s| <= 2b eff_max; a
z-move off the data sign leaves data c_l v_l(s) (|c_l| >= K_*^2 K t/(4D)) at a free or anti-sign coordinate: at a free coordinate this is a
violation of l_1-mass >= t |c_l| v_l(s) >= t^2 K_*^2 K/(4 D H(L)) >> s_1, not tolerated (U3 Lemma VT needs 2 rho eps <= delta s_1/16); at an
anti-sign coordinate it needs a cushion |a_s| >= t|c_l| v_l(s)/5 for every t of the window (C_+ = 5, K1.A), i.e. a mass >= T_hi(w)/(C D H),
whose cost (raise/lowering transfer, V3 Lemma 2.3, Q2 Lemma LT) exceeds o(u^2 T_lo^2).  (2) Window coordinates with v_l(j) in [c_0 W, x'_max]:
pullable ones contribute at most Cap_l < 4W'; non-pullable ones are in F with s_j = -eps_l (z_j = -eps_l, the minimum of eps_l v_l(j) z_j)
or super-thick (excluded by Lemma 2.3(b) at (R1) stages; at any stage a lowering costs > x_max, outside the budget); mass changes there have
efficiency mu_j^2 v_l(j)/nu <= mu*_{D(L)}^2 negligible.  (3) v_l(j) < c_0 W: |sum| <= 2 sum_{v < c_0 W} v_l(j) <= 4 c_0 W (geometric decay
along S_l).  (4) v_l(j) > x'_max: any first-order move of size >= W' there has cost >= C^{-1} x'_max log(1/x'_max) times the moved fraction;
moves of total value change V cost >= V/C (Z3 Lemma 3.1, unweighted term), so a decrease of size >= W' is affordable, but it is a z-move at
a coordinate of S_l that is NOT pullable only if ... -- [see the next remark; (4) is included in (2) by enlarging x'_max to the budget limit]
Fine-carrier terms: C c_{L+1}.  QED
Remark (on sort (4)).  K1-ref R-6 fixes x'_max = u^2 T^3/(Design^2 |Lambda|) as the upper end of the pull range; pulls with x'_max < v <=
x''_max := u^2 T^2/(C Design^C log^2(1/T)) also cost o(u^2 T^2) and are admissible by the same proof.  We therefore READ (U') with the
range [c_0 W, x''_max]; Lemma 2.3(a) holds verbatim (j <= 3 log_2(1/T_lo(w)) + C log Design).  For v > x''_max a pull is unaffordable.
So with this reading sort (4) contributes no admissible downward move of size >= W'/8.

## 2.5 Consequence for idea (1) of the task.  (Literal reading FALSE; charitable reading PROVED but insufficient.)
(i) Literal reading: "thin support coordinates of the OPPOSITE sign (s_j = -eps_l) in the pull range can be lowered to contacts and then
pulled".  FALSE as a relief mechanism: a pull places support of sign -eps_l and lowers eps_l v_l(j) z_j from its current value to its minimum
-v_l(j); at s_j = -eps_l the coordinate already sits at that minimum (z_j = -eps_l), and lowering a_j to 0 does not move z_j.  The
pull shift (1 + eps_l z_1(j)) v_l(j) is 0.  "Lower, then flip to +eps_l, then pull" returns z_j to -eps_l: the composite has zero net
downward capacity (it is a pre-placed raise followed by its own undoing), and a pre-placed bank or flip only RAISES the minimum of the
private range.  By Lemma 2.5 no admissible private move of any kind lowers val_l by more than O(W').  [Also: lowering the anti-sign
support at a window coordinate REMOVES the cushion of the anti-sign data c_l v_l(j) there (deep raise, K1.3 (D)), so the lowered
coordinate would carry an untolerated violation; the deep raise is what keeps it admissible.]
(ii) Charitable reading ("opposite" = opposite to the pull, i.e. DATA-sign support): thin data-sign window coordinates are pullable by K1's
definition (lowered first, cost <= |a_j| <= x_max), and the only non-pullable data-sign coordinates are super-thick, which Lemma 2.3(b)
excludes at every main stage followed by an (R1) stage.  So under (R1) at all large main stages, every kind-(iv) carrier's pull range is
ENTIRELY anti-sign support (super-thin) -- the minimum configuration of Lemma 2.5.  Idea (1) therefore reduces (U) to its sharpest form
but cannot relieve it.

## 2.6 Sign memory across consecutive main stages.  PROVED.
LEMMA 2.6.  Let p be a main stage at which the coarse carrier l is kind (iv) with switching sign eps, and let p' be the next main stage,
an (R1) stage.  Then at p' the carrier l is NOT active with switching sign eps; and if l is a robust coarse peak of a shifted block m at p
with all its TU-window coordinates non-pullable, then at p' the block m is not shifted with the same sign sgn Delta''_m.
Proof.  By Lemma 2.3, every TU-window coordinate j of l at p lies in F ∩ [1, D(p')] \ T(p') with |a_j| <= b(w') and, by 2.5(ii), s_j =
-(data sign of l at p).  j < J(w') (J(w') > D(p')), so j is unraised at p'.  If l is active at p' with the same data sign, Lemma K1.3 (case (S))
at p' gives |c_l| v_l(j) <= 4|a_j|/t <= 4 b(w')/t for t in the window of w', while Lemma K1.2 gives |c_l| >= K_*^2 K t/(4 D(p')) (peaks: c_l =
-Delta''_m lambda_l vs_l, same lemma).  Hence v_l(j) <= 16 D b(w')/(K_*^2 K t^2) <= 16 D T_lo(w')^2/(K_*^2 K) << x_TU(w)/C_0 <= v_l(j): contradiction.
The data sign of a peak is -sgn(Delta''_m) vs_l with vs_l = sgn w_m(l) fixed by f; robust peaks of p stay robust peaks at p' (rho fixed by f,
u(w') <= u(w)).  QED
So no carrier and no unpulled peak configuration can repeat with the same orientation at two consecutive (R1) main stages.  (This does
not by itself exclude (R1) at all stages: orientations may alternate, and new carriers enter at every stage.)
