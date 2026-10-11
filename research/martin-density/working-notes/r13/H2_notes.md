# H2 notes (Round 13): the residual (R1) of Step A -- pull ranges, private minimality, the all-at-once sign object,
# one-sided bands and block levers; precise remaining sub-class (one-sided pinned resonance)

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED (mod chain)" = proved here modulo the refereed chain that J1.15' (J1-ref E) and
J2's Theorem J2.1 already cite (X1/X1-ref, X2/X2-ref, Q1/Q1-ref a,b, cert0-3, Q2/Q2-ref a, K1/K1-ref, K2/K2-ref, J1/J1-ref, J2/J2-ref; several
links once-refereed).  Part files r13/H2_part1.md ... H2_part5.md (this file supersedes them where they differ; corrected constants in
3.3 and the pull range of 2.3 are those stated here).  Scripts and outputs: r13/H2_work/.  Companion task: r13/H1_notes.md ((R0)).

## 0. Bottom line
(1) (R1) IS NOT EXCLUDED; it is REDUCED.  At an (R1) stage every tuned row is privately tunable (kind (i)) or a one-sided kind-(iv) row,
    every near-certificate is of pure type (U*) (h = 0), and every unshifted block has a private two-sided peak resource (Facts 1.1-1.2).
    Theorem H2.A realizes Step A at every (R1) stage except when some block carries certificate weight on PINNED (or status-LOCKED)
    kind-(iv) rows in a sign configuration that the block's peak lever cannot serve.  In unshifted blocks this residual is EXACTLY a
    one-signed linear resonance of tiny minors with the wrong sign at the start row (Proposition 4.1, a Farkas alternative).
(2) Idea (1) of the task (lower thin support of the opposite sign in the pull range, then pull): FALSE as a relief mechanism.  A pull
    moves z_j to -eps_l; anti-sign support already sits there, so its pull capacity is 0, and no admissible private move of a kind-(iv)
    carrier lowers its value by more than O(W) (Lemma 2.5, private minimality).  Under the charitable reading (thin DATA-sign support)
    the coordinates are already pullable by K1's definition.  What IS true and useful: the CLUSTER SWEEP (Lemma 2.3) -- every pull-range
    coordinate of a main stage p lies at design depth, off the targets, at the next main stage p', so (R1) at p' makes it super-thin;
    super-thick pull ranges never occur under (R1) at consecutive stages, and kind-(iv) pull ranges are entirely anti-sign super-thin
    support (the minimum configuration).
(3) Idea (2) (uniform-sign object): PROVED in an all-at-once form (Proposition 3.1): every near-certificate has y_l >= -e_1 on every kind-(iv)
    row and total kind-(iv) weight >= c_1/4, and, block by block, the peak lever forces zeta_m ~ 0 (two-sided), <= 0 (kappa-raising) or >= 0
    (kappa-lowering).  No single kind-(iv) row carries uniform weight (unlike J1.6), but relieving ALL movable kind-(iv) rows at once,
    with one-sided (shrinking) bands, kills every certificate outside the residual.
(4) Idea (3) (peaks without peak resources): in (R1) unshifted blocks ALWAYS have a private two-sided peak resource; shifted blocks always
    have a ONE-sided peak lever of direction -sgn Delta''_m on kappa_m (used by Theorem H2.A); peaks of shifted blocks are never thick-type
    in (R1) (so that alternative is FALSE there); two-sided peak resources in shifted blocks cannot be supplied by design (HEURISTIC).
(5) Cross-stage structure (Lemmas 2.6, 2.7): along consecutive (R1) main stages switching signs never flip, shift signs go sigma -> sigma or
    sigma -> 0, every kind-(iv) carrier of a stage is INACTIVE at the next one, and every (up)/(down) block becomes unshifted.  So the
    residual rows of a stage are never those of the next stage: persistent (R1) needs fresh one-sided resonances at every main stage.
    OPEN whether this can happen.
(6) Why exactness is the crux (Section 5): a near-exactness relaxation (NE) of Z_kappa would remove the pinned residual in unshifted blocks
    and in shifted blocks without near-threshold actives, but the preparation (P2) raises every kind-(iv) value by >> s_1 (Lemma 5.2), so
    (NE) alone cannot absorb it; with a bias-free preparation (SKETCH) the core of (R1) would be "inward-locked near-threshold kind-(iv)
    carriers" of (T)-blocks.
(7) With H1 (r13/H1_notes.md, residual (H-1)-(H-7), unrefereed): neither (R0) nor (R1) is excluded.  (LSC-trunc)_N for every f, density
    of NA((c_0, p_N), l_2^2) for any N and of NA((c_0, p), l_2^2) for the Martin-type p: OPEN.  No counterexample; nothing found points
    to one (every residual configuration is a sign coincidence of stage data of f, needed afresh at almost every stage).

| # | Result | Status | Section |
|---|---|---|---|
| 1 | Fact 1.1 (carrier kinds in (R1)), Fact 1.2 (pure (U*), h = 0) | PROVED (mod chain) | 1 |
| 2 | Lemma 2.1 (extended R-G: a thin on [1, D(L)] off the targets) | PROVED (mod chain) | 2 |
| 3 | Lemma 2.2 (signature coordinates enter T(l) only below l) | PROVED | 2 |
| 4 | Lemma 2.3 (cluster sweep; no super-thick pull range under (R1) at the next stage) | PROVED (mod chain; (D-enum) convention) | 2 |
| 5 | Lemma 2.4 (aggregated pulls; refined (U')) | PROVED (mod chain) | 2 |
| 6 | Lemma 2.5 (private minimality of kind-(iv) carriers) | PROVED (mod chain) | 2 |
| 7 | Idea (1), literal reading | FALSE (zero capacity) | 2 |
| 8 | Lemma 2.6 (memory), Lemma 2.7 (sign persistence; kind-(iv) carriers deactivate at the next stage) | PROVED (mod chain) | 2 |
| 9 | Proposition 3.1 (all-at-once positivity; per-block balance for the three lever types) | PROVED (mod chain) | 3 |
| 10 | Lemma 3.2 (one-sided band version of K2.9/J1.8), Lemma 3.3 (shrinking bands legitimate) | PROVED (mod chain) | 3 |
| 11 | Lemma 3.4 (bands on outward rows: (a), (b) PROVED; (c) exchange/compensation SKETCH) | mixed | 3 |
| 12 | Theorem H2.A (realization of (R1) stages outside residual blocks) | PROVED (mod chain) | 3 |
| 13 | Proposition 3.5 (peaks; (d) HEURISTIC) | PROVED except (d) | 3 |
| 14 | Proposition 4.1 (unshifted blocks: residual = one-signed linear resonance), Corollary 4.2, Example 4.3 | PROVED (mod chain) | 4 |
| 15 | Shifted-block Farkas form | SKETCH | 4 |
| 16 | Persistence requirements (4.3); design variant with unbounded memory (4.4) | PROVED / SKETCH | 4 |
| 17 | Proposition NE (near-exactness), bias-free preparation, core under (NE) | SKETCH | 5 |
| 18 | Lemma 5.2 (preparation bias) | PROVED | 5 |
| 19 | (R1) at all large main stages impossible | OPEN | 6 |
| 20 | (LSC-trunc)_N for every f; density for p_N, p | OPEN | 7 |

## 1. Setting; the structure of (R1)
Design T_fin^{K2} (K2 6.1) with J2's frozen convention (FC), J1-ref's P-TU windows and F-2; diagonal base mu*_s = 2^{-2^{2^s}}; S_l =
{2^l(2i+1) : i >= 1}, v_l(j) = delta_l 2^{-j}/n_l on S_l; rounds PRE/MAIN/CLUSTER (Q1 1.2).  N >= 1; f in S_{p_N*} with forced data f = a + L^*w,
q*(a) = ||a||_1 + nu = 1, e = U^*a/nu, zhat = z + Ue, F = supp a; g in C(f); rho in (0, 1).  Main stage L >= l_f, clean sub-window w, class a;
b, u, T = T_lo(w), eta' = T^4/(L Design(L)), x = C Design(L) eta', D = D(L), W = Design^{C_A} u^{-3} max(x, ||b||), rho_0 = C_2 W^2, theta_0 =
b/Design^{C_P}.  Step A (Sys-A) at the unpushed prepared row R_1: rows l (coarse strict non-peaks, (FC)-frozen weak peaks, D-pushed),
Ft_l = val_l - rt_l kappa_{m(l)}, val_l = eps_l u_l(xhat); near-certificates y, phi_y = y^T Ft(R_1), Psi = sum y_l eps_l u_l - sum_m zeta_m K_m,
zeta_m := sum_{l in m} y_l rt_l, coef_k (K2.16 notation); kappa_y := <U^*Psi, e_1>/nu_1.  rt_l is the eps-ORIENTED target ratio; for active
rows |rt_l| >= u/Design^{C_3} (active carriers have rho >= u or are near-threshold) and |rt_l| <= Design^{C_4}.
(R1) at the stage: a near-certificate of size <= eps_* exists and NO coarse carrier is thick-type (no thick private coordinate in S_k ∩ [1, D]).

FACT 1.1 (carrier kinds).  PROVED (mod chain).  At an (R1) stage:
 (a) no near coordinate is thick (N_l ⊂ (s_max(L), d(L)] ⊂ [1, D] \ T(L), Lemma 2.1); hence no (P3)/(P4) resource, no kind-(ii)/(iii)
     carrier (K2.16 proof of (3)), and the signed common-mode vector h vanishes;
 (b) every zero-data tuned carrier is kind (i) (its off-F/thin near coordinates are ZD after (P): two-sided composites);
 (c) every data-carrying tuned carrier is kind (i) (pre-placed TU lever) or kind (iv): near coordinates S_th of the data sign sigma_l = eps_l
     (contacts banked with theta_0, or data-sign thin support raised to theta_0), pull range without pullable coordinate;
 (d) every coarse peak of an UNSHIFTED block (Delta'_m = 0) is zero-data (c_k = -Delta''_m lambda_k vs_k = 0) with ZD near coordinates: every
     unshifted block has a private two-sided peak resource (J1-ref R-PK applies);
 (e) a robust coarse peak c of a SHIFTED block carries data -Delta''_m lambda_c vs_c; its near coordinates are S_th of the data sign; the bank
     there moves kappa_m by -sgn(Delta''_m)(1 - X_m) lambda_c eff v_c(s) per unit (raises kappa_m iff Delta''_m < 0); it is two-sided iff the
     peak has pull capacity >= 4W' (Lemma 2.4; K1 2.2's "TU on the peak").
Proof.  (a) Lemma 2.1 below; K1 2.0.  (b), (c): K2.16's case list after (P) (K2 4.1(d)); a data-carrying carrier has no free near coordinate
(free coordinates force zero data, K1 2.1(b)) and no anti-sign thin near coordinate: Lemma K1.3 case (S) would give |c_l| v_l(s) <= 4|a_s|/t <=
8b/t with v_l(s) >= 1/H(L), i.e. |c_l| <= 8 b H/t, against |c_l| >= K_*^2 K t/(4D) (Lemma K1.2), since b << t^2/(D H Design).  (d), (e): K1 1.0
(peak data), K1.3 case (S) and (X1) for peaks (Lemma K1.2 covers coarse peaks), K2.4(ii), U1 Lemma 1.4(a) with (FC).  QED

FACT 1.2 (pure (U*)).  PROVED (mod chain).  At an (R1) stage every near-certificate of size eps <= eps_* has ||coef_(iv)||_2 >= c_1 - C eps Design^2
|Lambda_A| and kappa_y <= -c_1/(8 H(L)).  Proof: K2.16(3) with h = 0 (Fact 1.1(a)): gamma_0 = +infinity, so the (A*) alternative is void; kind (i)
has |coef| <= eps Design^2 (K2.16(2a)); ||coef_tuned||_2 >= c_1.  QED
ORIENTATION.  In route V d kappa_m/d zeta(l) = rho_l M X/C <= C b^2 D^2 at non-peaks, so |coef_l - eps_l y_l| <= C Design^4 b^2 =: e_X (1.1).
The one-sided generator of a kind-(iv) row (raise at a near S_th coordinate, z_s = eps_l) raises val_l, and K2.16(2c) gives
      y_l >= -e_1 := -((eps Design + |kappa_y| theta_0) Design + e_X)      on every kind-(iv) row.                         (1.2)
K^+_m (K^-_m) := kind-(iv) rows of block m with rt_l > 0 (< 0).  Since sum_{active l in m} rt_l |gamma_l| = Delta'_m ((X3)/kappa; J2-ref D.4),
an unshifted block with active rows has both signs.  For l in K^- an overshoot (realized value above target) SHRINKS |ratio| (inward,
status-safe); for l in K^+ it GROWS |ratio| (outward).  [In H1's language K^- rows behave like aligned and K^+ rows like anti-aligned
thick rows: sgn(y_l rt_l) = sgn rt_l for every certificate with robust y_l.]

## 2. Pull ranges, the cluster sweep, private minimality
LEMMA 2.1 (extended R-G).  PROVED (mod chain).  At a stage with a near-certificate and no thick-type carrier: |a_s| <= b(w) for every
s in F ∩ [1, D(L)] \ T(L).
Proof.  (R-mod') (K2 (K2-c)) makes each |a_s|, s <= D(L), tiny (<= b) or robust (>= u) at f; the deep raise acts beyond J(w) > D(L) and (P3)
raises thin moduli only to theta_0, so at R_1 the alternatives are <= 2b, >= u/2.  A robust s notin U_L is an anchor: K2.17(b) excludes all
near-certificates.  A robust s in U_L \ T(L) lies in supp u_k = supp y_k ∪ S_k for a coarse k with supp y_k ⊂ T(L), hence s in S_k; no other
coarse carrier lives at s (disjoint signature sets, targets in T(L)); so s is a thick PRIVATE coordinate of k in S_k ∩ [1, D] (K2.16(2b) needs
only privacy and v_k(s) >= v_min(L) >= 1/Design), and k is thick-type.  QED
LEMMA 2.2.  PROVED.  T(l) ∩ (union_k S_k) ⊂ [1, l] for every stage l.
Proof.  Main targets: allowedness (a), (c+) (Q1 1.2 (r.1)) put their signature coordinates below p - 2|supp y| - 1 < p.  Absorber targets
(PRE/CLUSTER, Q1 1.2 (r.2), (r.4)) are supported on {s} ∪ {p_0 < ... < p_R}, the p_i ODD (in no S_k), and s in Sigma(Y_r) (below the next
main stage, hence below the PRE stage: p_r = l_r + 2|Sigma| + 1) or s in E^ch(p) = T(p) ∪ union_{l''<=p}(S_{l''} ∩ [1, p]) for a cluster stage
after p.  Induction on l.  QED
CONVENTION (D-enum) (harmless bookkeeping of T_fin's free choices, Q1 1.1 (iii)-(iv)): the pool enumeration has max supp y^(i) <= i and the
schedule has i_nu <= nu.  Then the main target of round r has support in [1, r].
LEMMA 2.3 (cluster sweep).  PROVED (mod chain).  Let p be a main stage, w a sub-window of p, l <= p, j in S_l with c_0 W(w) <= v_l(j) <=
x''_max(w) (c_0 := 1/32, x''_max := u^2 T^2/(C Design^C log^2(1/T)), the affordable pull range), and p' the next main stage.  Then
 (a) j < s_max(p + 1) <= s_max(p') < D(p'), and j notin T(p') (also j notin T(p''), p'' the main stage after p');
 (b) if p' is an (R1) stage (selected sub-window w'), every such j in F has |a_j| <= b(w') << x_max(w): no coordinate of any pull range of stage
     p is super-thick, and every in-F coordinate there is super-thin.
Proof.  Depth: 2^{-j} = n_l v_l(j)/delta_l, so n(w) <= 2 log_2(1/T_lo(w)) - l - C <= j <= 4 log_2(1/T_lo(w)) + C log_2 Design(p) <= 5 log_2(1/T_lo(w))
(W >= x >= T^4/(p Design), x''_max <= T^2; log_2(1/T_lo(w)) >= n(w) >= Q(w) >= Design(p)^{20}).  The first cluster stage p+1 carries an absorber
target with p_R >= 2R(p+1), R the least integer with 2^{3-R} <= mu_{p_0}^2 lb_{p+1}^2/4, and lb_{p+1} <= c^max_{p+1} <= c^cl(p) <= exp(-1/T_lo(p, M(p)))
((W_exp), Q1 1.3 (S4)); so R >= 2 log_2(1/lb) >= 2/T_lo(p, M(p)) and s_max(p+1) >= 4/T_lo(p, M(p)) >= 4/T_lo(w) > j (sub-windows are nested
downwards).  D(p') >= d(p') > s_max(p') >= s_max(p+1).  By Lemma 2.2, j in T(p') needs p' >= j; p' <= p + R_cl(p) + 2|supp Y_{r+1}| + 1 <= 5p +
2 s_max(p) + 1 (R_cl(p) = 2|E^ch(p)| <= 2(s_max(p) + p); (D-enum)) <= Design(p) << n(w) <= j.  For p'': j is absorbed only through E^ch(L) with
L >= j, i.e. at cluster stages after a main stage of index >= j; p' < j, so the first such absorber comes after p''.  (b) j in F ∩ [1, D(p')]
\ T(p'): Lemma 2.1 at p'; b(w') <= T_lo(w')^4 <= T_lo(p, M(p))^4 << x_max(w).  QED

LEMMA 2.4 (aggregated pulls).  PROVED (mod chain).  For a data-carrying coarse l put Cap_l := sum{(1 + eps_l z_1(j)) v_l(j) : j in S_l
pullable (K1 2.0), c_0 W <= v_l(j) <= x''_max}.  If Cap_l >= 4W', then pre-placing ALL these pulls (masses 24 lambda_l v_l(j) of sign -eps_l,
after lowering in-F ones) with one compensating base bank at a near S_th coordinate gives a two-sided TU lever on the whole Brouwer domain:
l is kind (i).
Proof.  V1 Lemma TU / K1 2.1(b) with several pulls: total downward shift Cap_l >= 4W' >= 4 x (radius) (P-TU satisfied); the bank gives every
upward correction continuously; second-order cross effects <= C_T x''_max Cap_l; cushions per pulled coordinate as for one pull; cost <= C
Design sum v log(1/v) <= C Design x''_max log(1/T) = o(u^2 T^2) (geometric decay along S_l).  QED
REFINED (U'): a data-carrying carrier is kind (iv) iff Cap_l < 4W'.

LEMMA 2.5 (private minimality).  PROVED (mod chain).  Let l be kind (iv) (refined) at an (R1) stage.  Every admissible private move of l
(changes only at coordinates of S_l; route-V data stay admissible: data-sign contact/support at data-carrying private coordinates, cushions at
anti-sign support, no data at free coordinates) changes val_l by >= -(4W' + 4c_0 W + 2 b D eff_max + C c_{L+1}) >= -5W'.
Proof.  Four sorts of private coordinates.  (1) S_l ∩ [1, D] \ T(L): data-sign contacts (banked) or data-sign thin support (Fact 1.1(c), Lemma
2.1); lowering a mass changes val_l by <= eff_s v_l(s)|a_s| <= 2b eff_max; a z-move off the data sign leaves data c_l v_l(s) at a free coordinate
(violation of mass >= t^2 K_*^2 K/(4 D H) >> s_1: not tolerated, U3 Lemma VT) or at an anti-sign coordinate (needs a cushion >= t|c_l| v_l(s)/5
for every t of the window (C_+ = 5, K1.A), a mass >= T_hi/(C D H) whose cost exceeds o(u^2 T_lo^2)).  (2) c_0 W <= v_l(j) <= x''_max: pullable ones
contribute <= Cap_l < 4W'; non-pullable ones are in F with s_j = -eps_l (at the minimum of eps_l v_l(j) z_j) or super-thick (lowering costs
> x_max; excluded under (R1) at the next stage by Lemma 2.3); mass changes there have efficiency <= mu*_{D}^2-negligible.  (3) v_l(j) < c_0 W:
total |change| <= 2 sum v <= 4 c_0 W.  (4) v_l(j) > x''_max: a flip is unaffordable (cost >= c x''_max log(1/x''_max)) and a fractional z-move
leaves data at a free coordinate (not tolerated).  Fine carriers: C c_{L+1}.  QED
IDEA (1) OF THE TASK.  FALSE (literal reading).  A pull lowers eps_l v_l(j) z_j from its current value to -v_l(j); at in-F coordinates with
s_j = -eps_l it already equals -v_l(j): capacity (1 + eps_l z_1(j)) v_l(j) = 0.  Lowering a_j to 0 does not move z_j; "lower, flip to +eps_l,
pull back" is a pre-placed raise followed by its own undoing (net capacity 0); lowering also removes the cushion that makes the anti-sign
data c_l v_l(j) admissible (deep raise, K1.3 (D)).  By Lemma 2.5 no admissible private move of any kind helps.  Charitable reading (thin
DATA-sign support): pullable by K1's definition already; the non-pullable data-sign coordinates are super-thick and Lemma 2.3 excludes them.
Net effect: under (R1) at consecutive stages, kind-(iv) pull ranges are entirely anti-sign super-thin support -- the minimum configuration.

LEMMA 2.6 (memory).  PROVED (mod chain).  Let l be kind (iv) with switching sign eps at main stage p (resp. a robust coarse peak, all of
whose pull-range coordinates are non-pullable, of a block shifted with sign sigma at p), and let L'' in {p', p''} be one of the next two main
stages, an (R1) stage.  Then at L'' the carrier l is not active with switching sign eps (resp. the block is not shifted with sign sigma).
Proof.  Off-F coordinates of the far signature set of an active carrier are data-sign contacts at the companion (owned with z = eps_l, K1
1.1(1)(a) and V1 (C1); an anti-sign contact or a free coordinate with data would violate (X1)/(FR) of the class cone on E_c(w_p), which reaches
s_far >= 2/T_lo(p, M(p))), hence pullable; so the non-pullable pull-range coordinates j of l are in F with s_j = -(data sign at p) (super-thick
data-sign ones are excluded by Lemma 2.3(b) at p').  By Lemma 2.3, at L''
they lie in F ∩ [1, D(L'')] \ T(L'') with |a_j| <= b(w''), and j < J(w''), so they are unraised private coordinates of l.  If l had the same
data sign at L'' (for a peak: the data sign -sgn(Delta'') vs_l with vs_l = sgn w_m(l) fixed by f; robust peaks stay robust, u(w'') <= u(w)),
Lemma K1.3 (S) at L'' would give |c_l| v_l(j) <= 4|a_j|/t <= 4b(w'')/t, and Lemma K1.2 (peaks included) |c_l| >= K_*^2 K t/(4 D(L'')); so v_l(j) <=
16 D b(w'')/(K_*^2 K t^2) <= 16 D T_lo(w'')^2/(K_*^2 K) << c_0 W(w_p) <= v_l(j).  QED

LEMMA 2.7 (sign persistence and deactivation).  PROVED (mod chain).  Let p, p' be consecutive main stages, p an (R1) stage.
 (a) If a coarse carrier l carries data at p with switching sign eps (any kind), then at p' it is not active with switching sign -eps,
     provided p' is an (R1) stage or every near coordinate of l at p is off F.
 (b) If l is kind (iv) at p and p' is an (R1) stage, then l is INACTIVE (zero-data) at p'.
 (c) If block m is shifted at p with sign sigma (a robust coarse peak exists, V1 Lemma D), then at p' it is not shifted with sign -sigma
     (same proviso as (a)); if m is an (up)/(down) block at p (every robust peak of capacity < 4W') and p' is (R1), m is UNSHIFTED at p'.
Proof.  (a) At p (R1) the near coordinates s of l (in (s_max(p), d(p)]) are data-sign contacts or data-sign thin support (Fact 1.1(c)).  At p'
they are private (signature coordinates beyond s_max(p) are absorbed only through E^ch(L) with L >= s, at cluster stages AFTER p', and main
targets of round <= r+1 have support in [1, r+1] by (D-enum)), at design depth (<= d(p) < D(p')) and unraised (J(w') > D(p')).  If l were active at
p' with sign -eps, then for every scale t of the window of p' the actual coefficient has sign -eps and |c^act_l| >= (4/5) K_*^2 K t/(4 D(p'))
(Lemma K1.2), and s is ANTI-sign for it.  Contact case: the flip bounds of f's decomposition at scale t (lem:flip: sum over contacts of the
anti-sign parts <= (1 + eta')t/q_0) give |c^act_l| v_l(s) <= (1 + eta')t/q_0 + C c_{p'+1}; thin-support case: Lemma K1.3 (S) at p' gives
|c_l| v_l(s) <= 4|a_s|/t <= 8 b(w')/t (Lemma 2.1 at p').  [A near-contact (tiny room at f, closed by (C1) at p) behaves like a contact:
the ANTI-sign part of the switching at a coordinate with z_s ~ eps costs the full flip budget (Part I lem:flip, lem:budget).]  With v_l(s) >= 1/H(p) both contradict the lower bound, since K_*(w')^2 K >= K_P(w') =
8 C_q 2^{J(w')} D(p')/delta_min(p') >> D(p') H(p)/q_0 (2^{J(w')} >= 2^{d(p')} >= 2^{s_max(p')} >> H(p)) and b(w') << t^2/H(p).
(b) Sign eps at p' is excluded by Lemma 2.6, sign -eps by (a).  (c) Peaks are covered by Lemmas K1.2, K1.3 (data -Delta'' lambda_c vs_c, vs_c
fixed by f, robust peaks of p remain robust peaks at p'); the first claim is (a) for a robust peak, the second adds Lemma 2.6 for the same
sign (all pull-range coordinates with v in [8W', x''_max] are non-pullable when Cap < 4W').  QED
Consequences.  Along consecutive (R1) main stages: switching signs of active carriers never flip; shift signs of blocks go sigma -> sigma or
sigma -> 0 (and 0 -> anything); every kind-(iv) carrier of a stage is inactive at the next one; every (up)/(down) block becomes unshifted.  So
the one-sided rows carrying a residual at stage L are never the residual rows of stage L+ (the next main stage), and an (up)/(down) residual
block at L is an unshifted (two-sided-lever) block at L+.  These are strong combinatorial constraints, but they do not by themselves exclude
(R1) at all stages (fresh carriers, and residual blocks alternating between shifted and unshifted states).

## 3. The all-at-once sign object; one-sided bands; block levers; Theorem H2.A
PROPOSITION 3.1.  PROVED (mod chain).  At an (R1) stage every near-certificate y of size eps <= eps_* satisfies:
 (a) [all-at-once positivity] y_l >= -e_1 on every kind-(iv) row and sum_{kind (iv)} y_l >= c_1/4;
 (b) [per-block balance] for every block m:  |zeta_m(y; rt)| <= (4/3) eps Design if m has a two-sided peak resource (every unshifted block;
     shifted blocks with a robust peak of capacity >= 4W'); zeta_m <= (4/3) eps Design if m has only a kappa-RAISING one-sided peak resource
     (Delta''_m < 0); zeta_m >= -(4/3) eps Design if only a kappa-LOWERING one (Delta''_m > 0); every block has one of the three (Fact 1.1(d), (e));
 (c) |y_l| <= eps Design^2 + e_X on kind-(i) rows.
Proof.  (a) ||y_(iv)||_2 >= ||coef_(iv)||_2 - |Lambda_A|^{1/2} e_X >= c_1/2 - small (Fact 1.2, (1.1)); sum_l y_l >= sum_l (y_l)_+ - |Lambda_A| e_1 >=
||y_(iv)||_2 - 2|Lambda_A| e_1 >= c_1/4.  (b) Two-sided: J1-ref Lemma R-PK.  One-sided: R-PK's computation for a one-sided generator: the bank
at a private near S_th coordinate s of a robust peak c changes only u_c(xhat) among coarse carriers, moving kappa_m by -sgn(Delta''_m)(1 - X_m)
lambda_c eff_s v_c(s) per unit ((FC): d kappa_m/d zeta(c) = 1 - X_m in [3/4, 1]) and every Ft_l (l in m) by -rt_l times that, so its action on
y^T Ft is sgn(Delta''_m)(1 - X_m) lambda_c eff_s v_c(s) zeta_m >= -eps, with (1 - X) lambda_c eff_s v_c(s) >= 3/(4 Design).  (c) K2.16(2a), (1.1).  QED
Remark.  (a) replaces J1.6(a) in (R1): no single kind-(iv) row has a uniform coefficient (different certificates may live on disjoint
sets of kind-(iv) rows), but the SET of all kind-(iv) rows carries a fixed positive weight; so relieving all movable kind-(iv) rows at once
kills every certificate supported on them.

LEMMA 3.2 (one-sided bands).  PROVED.  Let banded rows l in B carry boxes [lo_l, hi_l] ∋ 0 for the final Ft_l, Box := prod_B [lo_l, hi_l].
 (a) If B(b, rho_0) ⊂ (W/2) conv(G ∪ {0}) - Box, the band-relaxed Step A is realized (K2.9(c) / J1.8(a): Brouwer on {t >= 0, ||t|| <= W} x Box
     with the continuous minimal-norm selection).
 (b) Otherwise a unit y with max_g(-y^T g) < 2(||b|| + rho_0)/W has sum_B max(y_l lo_l, y_l hi_l) < phi_y + rho_0 <= ||b|| + rho_0.
Proof.  The realization equation is G t - sigma = b - Rem(t), sigma in Box.  Separate b'' in B(b, rho_0) \ ((W/2)Q - Box) by a unit y:
y^T b'' < (W/2) min(0, min_g y^T g) - max_{Box} y^T sigma; both terms are <= 0, so (W/2) max_g(-y^T g) < -y^T b'' <= ||b|| + rho_0 and
max_Box y^T sigma < -y^T b'' <= phi_y + rho_0.  QED
OVERSHOOT BAND on row l: box [0, beta] (final value up to beta above target); (b) then gives (y_l)_+ < (||b|| + rho_0)/beta.

LEMMA 3.3 (shrinking bands are legitimate).  PROVED (mod chain).  Let l in K^- be an active row with a FREE ratio (J1.13: in no tiny minor and
no tiny cofactor polynomial; in (T)-blocks a tiny minor containing an (X4^0) row of block m pins every active ratio of m through R_a^2,
J1-ref P-MT), and beta <= kappa_min u/(4 Design^{C}).  The overshoot band [0, beta] on l is legitimate: the realized ratio r^#_l in [rt_l, rt_l +
beta/kappa] keeps its sign and |r^#_l| <= |rt_l|, so R^2 does not increase and every status of every block is <= its value at the targets
(Lemma K: rho_d = m|r_d| K(sigma, R^2)/Phi_d, K increasing in R^2), all protected statuses of route V are upper bounds or robust (margin u), robust
objects move by <= Design^C beta << u, Z_kappa is untouched (l free), and the class data projected at the realized ratios meet J1.13 (i)-(ii).  QED
LEMMA 3.4 (bands on OUTWARD rows, l in K^+ free).  (a) (U)-blocks: legitimate (J1.15' (J-d) with F-2; the peak resource is Fact 1.1(d)).  PROVED.
(b) shifted blocks with no R^2-sensitive protected status: legitimate (J1.15' (J-f), second clause).  PROVED.  (c) protected shifted blocks with a
movable partner d (kind (i), or K^- free, robust ratio) or a (KN)-lever: compensate the R^2 increase (and, if l is near-threshold, its own status
increase) by an inward move of d of size <= Design^C beta/u^2 (Lemma K; cf. H1 Theorem OUT(b), H1 Lemma KC).  SKETCH (all-at-once version for
several outward rows; (KN)-lever bookkeeping; R_a^2 in (X4^0) rows).  A free K^+ row covered by none of (a)-(c) is LOCKED.

THEOREM H2.A.  PROVED (mod chain; Lemma 3.4(c) only where it is used).  At an (R1) stage band every free K^- row (all blocks) and every free
K^+ row covered by Lemma 3.4, with half-width
      beta_1 := 16 |Lambda_A|^2 Design(L)^{C_3 + C_4} (||b|| + rho_0)/(c_1 u).
Let P^-_m be the PINNED rows of K^-_m and P^+_m the PINNED or LOCKED rows of K^+_m (K^- rows are never locked).  Block m is RESIDUAL if
 (two)  m has a two-sided peak resource and P^-_m != {} != P^+_m;
 (up)   m has only a kappa-raising one-sided peak resource (Delta''_m < 0) and P^-_m != {};
 (down) m has only a kappa-lowering one-sided peak resource (Delta''_m > 0) and P^+_m != {}.
If no block is residual, the band-relaxed Step A is realized; with J1.13 and J2.1 the stage feeds (LSC-trunc)_N.
Proof.  Otherwise Lemma 3.2(b) gives a near-certificate y (size < 4 Design^{-C_A} <= eps_*) with (y_l)_+ < delta_1 := c_1 u/(16|Lambda_A|^2
Design^{C_3+C_4}) on banded rows, so |y_l| <= max(e_1, delta_1) there ((1.2)).  Fix m; kind-(i) rows contribute |sum y_l rt_l| <= e_2 := |Lambda_A|
Design^{C_4}(eps Design^2 + e_X) to zeta_m (3.1(c)).  Two-sided lever with P^-_m = {}: all K^- rows banded and |zeta_m| <= (4/3) eps Design, so
sum_{K^+} y_l rt_l <= |Lambda_A| Design^{C_4} delta_1 + e_2 + 2 eps Design =: Z; each term is >= -e_1 Design^{C_4}, hence y_l <= Design^{C_3}(Z +
|Lambda_A| e_1 Design^{C_4})/u <= c_1/(16|Lambda_A|) + small on every K^+ row.  Two-sided with P^+_m = {}: symmetric (all K^+ banded; zeta_m >=
-(4/3) eps Design controls K^-).  (up) with P^-_m = {}: zeta_m <= (4/3) eps Design and all K^- banded: the same bound on K^+.  (down) with P^+_m = {}:
zeta_m >= -(4/3) eps Design and all K^+ banded: sum_{K^-} y_l |rt_l| <= Z, the same bound on K^-.  So |y_l| <= c_1/(16|Lambda_A|) + small on every
kind-(iv) row, and sum_{(iv)} y_l <= c_1/16 + small < c_1/4, against Proposition 3.1(a).  The bands move ratios by <= beta_1/kappa_min <=
Design^C (||b|| + rho_0)/u, inside J1.13 (i)'s allowance (||b|| + rho_0 <= Design^C eta' and eta' <= (u/Design)^{4L^2}); legitimacy by Lemmas
3.3, 3.4.  QED
[Numerics: r13/H2_work/toy_onesided.py/.out -- linear model with one-sided rows, three lever types and overshoot boxes, 4000 random
configurations x 40 right-hand sides: exact LP feasibility agrees with "no residual block" in 4000/4000.]

PROPOSITION 3.5 (peaks; idea (3)).  (a) In (R1) every unshifted block has a private two-sided peak resource (Fact 1.1(d)): the classes
"(R-pk)/(R-np)" of J1-ref and H1's case (U+) are EMPTY in (R1).  PROVED.  (b) Every shifted block has a one-sided peak lever of direction
-sgn Delta''_m on kappa_m, two-sided iff a robust peak has capacity >= 4W' (Fact 1.1(e), Lemma 2.4).  PROVED.  (c) Peaks are never thick-type in
(R1); in shifted blocks "no two-sided peak resource" does NOT force thick-type peaks (their thin/off-F near coordinates carry data and are
one-sided S_th, not ZD) -- contrast H1 Lemma NP(b) for unshifted blocks.  So the alternative "such peaks are thick-type" is FALSE in (R1).
PROVED.  (d) Two-sided peak resources in shifted blocks cannot be supplied by design: every robust coarse peak of a shifted block carries
data, a row may put anti-data-sign support on the whole pull range of every robust peak (the deep raise supplies the cushions), and a
designed extra carrier is either a robust peak (same situation) or a non-peak (d kappa/d zeta <= C b^2 D^2: no kappa lever).  HEURISTIC.
(e) An (up)/(down) configuration of a block cannot repeat with the same shift sign at the next two main stages if they are (R1) stages
(Lemma 2.6).  PROVED (mod chain).

## 4. The residual: one-sided pinned resonance
4.1 Reformulation.  PROVED (mod chain).  Admissible target displacements are additional generators (H1 Lemma TF; J1 7.4(a)): a residual
stage carries a near-certificate y of the EXTENDED system, i.e. also <kappa y, Delta> <= eps' for every admissible displacement Delta.  For
pinned rows the admissible displacements are tangent to Z_kappa (plus the block rescaling in (U)-blocks), so on the pinned rows of a block
kappa y lies, up to eps', in the normal space of Z_kappa at the Lojasiewicz point, and phi_y is, to first order, the value at the start row
of the corresponding combination of tiny minors (Ft(R_1) = kappa(rc - rt), J1.2; rt in Z_kappa).

PROPOSITION 4.1 ((U)-blocks: one-signed linear resonance).  PROVED (mod chain; first order at the start row).  In a (U)-block every minor
containing a ratio of the block contains it only through the row (X3)_m (X1 2.1(U), X1-ref D1); expanding along (X3)_m, a tiny minor is
M_i(r) = sum_l C_{i,l} r_l with cofactors C_{i,l} free of r^{(m)}.  Put C'_{i,l} := eps_l C_{i,l} (oriented).  With the two-sided kappa lever and
the rescaling s the kind-(iv) constraints read rho rt^#_l >= rc_l (rho := s kappa^#/kappa > 0 free; absorbed by homogeneity).  Block m is
residual iff there is lambda with
      (lambda^T C')_l >= 0 on pinned kind-(iv) rows,   (lambda^T C')_l = 0 on pinned two-sided rows,   sum_i lambda_i M_i(rc) > 0:
a combination of tiny minors that is a NONNEGATIVE form in the oriented pinned kind-(iv) ratios, blind to the two-sided ones, and of the
wrong sign at the start row.
Proof.  Feasibility of {A rt = 0, rt_P >= rc_P, rt_Q free} (A = C' on pinned columns, P = kind (iv), Q = two-sided; free rows banded by Lemma
3.4(a)); Farkas: infeasible iff some lambda has (lambda^T A)_Q = 0, (lambda^T A)_P >= 0, (lambda^T A)_P rc_P > 0, and the last quantity is lambda^T
M(rc) because the Q-part vanishes.  QED
COROLLARY 4.2.  A (U)-block is not residual if every tiny minor that contains a pinned kind-(iv) ratio has a nonzero cofactor on some pinned
two-sided row, or if in every such minor the oriented cofactors of the pinned kind-(iv) rows take both signs.  PROVED.
EXAMPLE 4.3.  PROVED (finite algebra; the restricted system).  Two active kind-(iv) rows l+, l- (rt_{l+} > 0 > rt_{l-}) of a (U)-block and one tiny
minor M = det[[r_{l+}, r_{l-}], [u_{l+}(j), u_{l-}(j)]] ((X3)_m and the contact row at a common target contact j); in oriented variables M =
C'_+ rt_+ + C'_- rt_-.  If C'_+, C'_- > 0, the block is residual iff M(rc) > 0, for every kappa^# and s.  [toy_resonance.py: M(rc) = -1e-3, -1e-6
feasible; +1e-6, +1e-3 infeasible; and the Farkas alternative of 4.1 in 3000/3000 random instances.]  Whether an f realizes this with no
other generator acting on the two rows (the full K2.16 normal form, Psi ~ kappa_y a on the thick target coordinates) is not constructed.

4.2 Shifted blocks.  SKETCH.  The same alternative with the normal cone of Z_kappa (minors depend on r through (X3), the columns
u_l - r_l tau_m (Lemma EC) and, in (T)-blocks, (X4^0) entries via R_a^2), modified by the one-sided lever: in (up) blocks the direction
rt^{(m)} may be added with a nonnegative coefficient, in (down) blocks with a nonpositive one.  Not written out.

4.3 Persistence: what (R1) at ALL large main stages requires.  PROVED (each item, mod chain).
 (a) a is b(w(L))-thin on F ∩ [1, D(L)] \ T(L) at every main stage L >= L_0 (Lemma 2.1); with Lemma 2.2, the base part lives on target
     coordinates up to super-thin mass;
 (b) every kind-(iv) pull range is anti-sign super-thin support (Lemmas 2.3, 2.5), no super-thick pull range;
 (c) no carrier is kind (iv) with the same sign at the next two main stages, every kind-(iv) carrier is inactive at the next main stage,
     switching and shift signs never flip, and (up)/(down) blocks become unshifted (Lemmas 2.6, 2.7, Proposition 3.5(e));
 (d) at every stage some block carries a one-sided pinned resonance or a locked outward row (Theorem H2.A, 4.1-4.2);
 (e) consequently a resonance among the SAME carriers with the same signs cannot persist: in particular an exact algebraic relation of f
     (a tiny minor recurring with fixed carriers, hence vanishing exactly at f's ratios) cannot by itself produce (R1) at all stages.
So persistent (R1) needs a NEW wrong-signed one-sided resonance at almost every main stage (fresh carriers or alternating orientations).
4.4 Design variant with unbounded memory.  SKETCH.  Replace E^ch(p) by T(p) ∪ (Z_0 ∩ [1, p]) for the cluster absorbers (no signature
coordinates; route-V absorbers carry no switching, X2-ref R-abs, and are off the MT VI tree, Q1-refa) and keep (D-enum).  Then T(L) ∩ (union S_k)
⊂ [1, r(L)] (r(L) = number of rounds), so the private coordinates used in Lemmas 2.6 and 2.7 (old near coordinates and old pull ranges)
stay private at every later main stage of round < s_max(p), and Lemmas 2.6-2.7 hold at all later (R1) main stages of round < s_max(p)
(an astronomically long range: s_max(p) >= 4/T_lo(q, M(q)) for the main stage q preceding p): every kind-(iv) carrier of an (R1) stage stays
inactive, switching signs do not flip, and an (up)/(down) block stays UNSHIFTED there (its robust peaks' data-sign near coordinates and
anti-sign pull ranges persist as thin private coordinates).  Consequently, in the persistent regime, within every round interval
[r, s_max(p_r)) there are at most N (up)/(down) residual events; all other residual blocks are of type (two) (unshifted, or shifted with
a pullable robust peak), and every residual kind-(iv) carrier is FRESH within such an interval.  To check for (D-abs): the (W4'') weight conditions attached to the removed absorbers.  Even then (R1) is not
excluded (a fresh two-signed pinned resonance at every stage remains possible as far as is proved).

## 5. Exactness, near-exactness and the preparation bias
PROPOSITION NE (near-exactness).  SKETCH (audit of J1.13's list; not re-proved line by line).  J1.13's requirement "pinned ratios realized
exactly on Z_kappa" may be weakened to: the realized ratios r^# lie within delta_Z of a point r^flat in Z_kappa with robust minors >= u/4, if
C_f Design^C delta_Z <= delta s_1/(64 rho) ((VT') of Lemma VT).  Argument: project the class data at r^flat (Lemma H there); at f^# the true
shift sum r^#_l gamma_l differs from the cone shift sum r^flat_l gamma_l by <= C_f D delta_Z (|gamma_l| <= C_f D lambda_l); this mismatch enters
the peak traces (U1 Lemma 4.6(b)), the tau_m-terms of (X1) contact rows, the inactive switching Delta'' w(l) of shifted blocks and the
(X4^0)/kind-[3] rows; the first two are contact/support violations of mass <= C_f Design delta_Z tolerated by (VT') (free coordinates split
1/2-1/2, b^theta = 0, as in K1.S), the last two move kinds and floor rows by C Design delta_Z << gap^#/t (gap^# >= eta'/(3 Design), H1 Prop.
J1.11).  Statuses, Sys-DC targets, Lemma PM and (U)-block homogeneity use realized ratios only.
LEMMA 5.2 (preparation bias).  PROVED (mod chain).  (P2)/(P3) raise every kind-(iv) value: val_l(R_1) - val_l(f^r) >= eff_s v_l(s) theta_0 -
C D b theta_0 > 0 per banked near contact s (K2.4(ii), z_s = eps_l), and theta_0 >= 4 Design K_DC r >> Design^C s_1 (K2 4.3 Step 6; r >= 4 K_J Pi_X,
Pi_X ~ s_1 A_0/T, X2 3.2).  Hence a nonnegative resonance form charging a banked kind-(iv) row is pushed to the wrong side by >= c theta_0/
Design^C >> delta_Z for every delta_Z allowed by (NE): (NE) cannot absorb the bias.  QED
Consequence.  The residual of Theorem H2.A has two sources: (i) f itself on the wrong side of a one-signed resonance; (ii) the preparation
bias when f is on the right side by less than c theta_0/Design^C.  Source (ii) is an artefact of K2's preparation, which banks kind-(iv)
near contacts only because Theorem K2.6 wants a two-sided Sys-DC lever at scale r for every Omega carrier.
5.3 Bias-free preparation.  SKETCH.  If a kind-(iv) carrier has pull capacity >= 4 K_DC r in the range c r <= v_l <= c_0 W (BELOW its Step-A
pull range, where (U') says nothing), replace its (P2) bank by a pre-placed TU pair at the Sys-DC scale (net first-order change of val_l = 0;
two-sided at scale r).  With (NE) and a design clause C_L((1 + Lip C_*) b(w))^{2/N_L} <= delta_Z on b(w) (b only appears as an upper threshold):
 - (U)-blocks: realize s r_1 (values of kind-(iv) rows unchanged, kappa^# = kappa/s by the two-sided peak resource): no obstruction;
 - shifted blocks without active near-threshold carriers, and (KN)-blocks: no displacement of kind-(iv) rows is needed: no obstruction;
 - (T)-blocks with active near-threshold carriers: the Puiseux descent must follow Z_kappa (H1 Lemmas 1.1-1.2); it is blocked iff every
   descent direction lowers the value of some K^+ kind-(iv) row.  Simplest instance: a single active near-threshold K^+ kind-(iv) carrier d
   in a (T)-block (Delta'_m = rt_d |gamma_d| > 0, the peak lever LOWERS kappa, rho_d = m|r_d| K(sigma_rob, m^2 r_d^2)/Phi_d cannot decrease).
   This INWARD-LOCKED NEAR-THRESHOLD carrier would be the core of (R1); by Lemma 2.6 the same carrier cannot play this role at consecutive
   (R1) stages, and a fixed carrier with rho_d < 1 is near-threshold at finitely many stages only (rho_d is f's datum).
Remaining under 5.1 + 5.3: fully swallowed kind-(iv) carriers (anti-sign at every depth from W down to r) and wrong-sided resonances of f.

## 6. The remaining class (precise).  PROVED as a necessary condition; OPEN whether it can persist.
THEOREM H2.B.  Let (f, g, rho) be such that at all main stages L >= L_0 the selected stage is an (R1) stage (near-certificate, no thick-type
carrier).  If Theorem H2.A realizes Step A at only finitely many of these stages, then for all large main stages L:
 (i) a is b(w(L))-thin on F ∩ [1, D(L)] \ T(L) (Lemma 2.1), every kind-(iv) pull range is anti-sign super-thin support (Lemmas 2.3, 2.5), and
     no coordinate of any pull range is super-thick;
 (ii) every unshifted block has a private two-sided peak resource; every shifted block has a one-sided peak lever of direction -sgn Delta''_m;
 (iii) some block m is RESIDUAL (Theorem H2.A): (two) pinned rows in K^-_m and pinned/locked rows in K^+_m; (up) pinned rows in K^-_m with only a
      kappa-raising lever; (down) pinned/locked rows in K^+_m with only a kappa-lowering lever; in an unshifted block this is the one-signed
      linear resonance of Proposition 4.1 (wrong sign at the start row);
 (iv) kind-(iv) carriers of stage L are inactive at the next main stage; switching signs never flip and shift signs go sigma -> sigma or
      sigma -> 0 between consecutive stages; (up)/(down) blocks become unshifted (Lemmas 2.6, 2.7).
Sources of (iii): a wrong-signed resonance of f's stage data, or the upward preparation bias (Lemma 5.2).  Nothing proved excludes (i)-(iv)
at all large stages: each stage asks a codimension-one sign coincidence among FRESH data (new coarse carriers / new tiny minors).

## 7. Combination with H1 and the global statement
THEOREM H (combined; PROVED modulo the chain cited by J1.15' and J2.1, and modulo H1's unrefereed results where stated).  For the design
T_fin^{K2} (with (FC), P-TU, F-2, (D-enum)), N >= 1, f in S_{p_N*}, g in C(f), rho in (0, 1): (LSC-trunc)_N holds at (f, g, rho) unless, at all
but finitely many main stages, the selected stage either
 (a) has a thick-type carrier and satisfies H1's residual conditions (H-1)-(H-7) (H1 8; H1 unrefereed), or
 (b) has no thick-type carrier and satisfies (i)-(iv) of Theorem H2.B.
Links used: J2's Theorem J2.1 (Step 0 bypass; refereed); J1-ref's Theorem J1.15' with F-2, P-TU (refereed); J1.13 (refereed, inspection) and
J1-ref B.5; J1-ref Lemma R-PK; K2.9, K2.16, K2.17 (refereed, K2-ref); K1 2.0-2.7 (pulls, pullability, Lemma K1.2, K1.3; refereed); X1 2.1-2.6 and
Lemma K (refereed, certified); X2/U3 Lemma VT (refereed; only in the SKETCH of Section 5); Q2 Theorem UE^inf, E^{eng,RT,inf} (once refereed);
Q1 Theorem VI.2 (certified: density of NA((c_0, p_N), l_2^2) iff (LSC-trunc)_N) and Corollary VI.3 ((LSC-trunc)_N for infinitely many N implies
density for the Martin-type p).
Hence: if (a) and (b) were both impossible at all large stages for every (f, g, rho), then (LSC-trunc)_N would hold for every f, NA((c_0, p_N),
l_2^2) would be dense for every N, and NA((c_0, p), l_2^2) would be dense for the Martin-type norm p built with T_fin^{K2} (option (a), ||T|| =
c_1 < 1, Martin's Remark 2).  Neither exclusion is proved: both residuals are OPEN.  NOT CLAIMED: density for any N.

## 8. Numerics (sanity only; r13/H2_work/)
 toy_onesided.py/.out: linear Step-A model (two-sided and one-sided rows, lever types two/up/down/none, overshoot boxes on banded rows);
   4000 random configurations x 40 right-hand sides; exact LP feasibility versus the prediction of Theorem H2.A ("no residual block"):
   4000/4000 agree.
 toy_resonance.py/.out: Proposition 4.1's Farkas alternative in 3000/3000 random instances (911 infeasible); Example 4.3: M(rc) = -1e-3,
   -1e-6 feasible, +1e-6, +1e-3 infeasible.
 Finite models cannot show the infinite-dimensional mechanisms (sweep, memory, deep raise); those rest on the proofs.

## 9. Main obstacle; next steps
MAIN OBSTACLE.  EXACTNESS versus ONE-SIDEDNESS.  A kind-(iv) carrier sits at the minimum of its private range (Lemma 2.5); its pinned ratio
must land exactly on Z_kappa (J1.13); when the normal cone of Z_kappa at the start row is one-signed on the oriented kind-(iv) coordinates
and the start row is on the wrong side (f's data or the preparation bias), no admissible realization exists.  Equivalently (H1's
language): outward-wanting pinned or near-threshold rows with no neutral rescaling.
NEXT STEPS.  (1) Prove Proposition NE (near-exactness) line by line; it removes the pinned residual wherever the start row is within the
VT tolerance of Z_kappa.  (2) A bias-free preparation for kind-(iv) carriers (5.3): TU pairs at the Sys-DC scale, and a Sys-DC variant
(Theorem K2.6) tolerating one-sided columns for fully swallowed carriers.  (3) Exploit memory: with the variant 4.4 (unbounded memory)
every (carrier, sign) is used once; combine with the base-part thinness 4.3(a) and the certificate's normal form (a's thick part ~ a
combination of the residual carriers' targets) to show that fresh wrong-signed resonances cannot be supplied at all stages by one f -- the
most promising route to EXCLUDE (R1).  (4) Treat inward-locked near-threshold carriers by a peak conversion (H1 7) adapted to active
carriers with inactive excess.
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N and of NA((c_0, p), l_2^2): OPEN.  No counterexample is claimed or
suggested.
