# H2 referee notes (Round 13): proofs of the verdicts and of the fixes for r13/H2_notes.md ((R1): thin rows, pure (U*) certificates)

Setting and notation: r13/H2_notes.md 1 (design T_fin^{K2} with (FC), P-TU, F-2; diagonal base mu*_s; N >= 1; f in S_{p_N*}, g in C(f),
rho in (0, 1); main stage L, clean sub-window w, class a; b, u, T = T_lo(w), eta', x, W, rho_0, D = D(L), theta_0; Sys-A rows, Ft_l = val_l -
rt_l kappa_{m(l)}, near-certificates y of size eps, phi_y, zeta_m(y; rt) = sum_{l in m} y_l rt_l; K^+_m / K^-_m the kind-(iv) rows with rt_l > 0 /
< 0).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED" = modulo the refereed chain cited by J1.15' (J1-ref E) and J2's Theorem J2.1.
Part files: r13/H2_ref_part1.md (Facts, Lemmas 2.1-2.3), part2 (Lemmas 2.4-2.7, 3.1-3.4, H2.A, Section 4), part3 (3.5, Section 5, (D-abs),
H2.B/H).  Scripts and outputs: r13/H2_ref_work/.  This file supersedes the part files where they differ.

## A. Verdicts
| H2 claim (H2 label) | Verdict | Items |
|---|---|---|
| Fact 1.1, Fact 1.2 (PROVED) | correct | B.1; precision P-11 |
| Lemma 2.1 (PROVED) | correct | B.2 |
| Lemma 2.2 (PROVED) | correct (does not need (D-enum)) | B.3 |
| Lemma 2.3 (PROVED, (D-enum)) | correct with precision | B.3, P-RANGE |
| Lemma 2.4 (PROVED) | correct with precisions | P-RANGE, P-AGG |
| Lemma 2.5 (PROVED) | correct for the certified toolbox; sort (4) and one cushion bound not as stated | P-25 |
| Idea (1), literal reading (FALSE) | correct (it is false) | B.4 |
| Lemmas 2.6, 2.7 (PROVED) | correct | B.5; justification precision P-OWN |
| Proposition 3.1 (PROVED) | correct with constant precision | P-31 |
| Lemma 3.2 (PROVED) | correct | B.6 |
| Lemma 3.3 (PROVED) | correct (mod J1.13) | B.6 |
| Lemma 3.4 (a),(b) PROVED, (c) SKETCH | (a) correct with the coupled Brouwer step (G-CPL); (b) correct; (c) SKETCH honest | G-CPL |
| Theorem H2.A (PROVED) | correct with a fixable gap | G-CPL, B.7 |
| Proposition 3.5 ((d) HEURISTIC) | correct; (d) heuristic honest | B.8 |
| Proposition 4.1 (PROVED) | Farkas algebra correct; "iff"/"EXACTLY" holds only in a restricted single-block model | P-41 |
| Corollary 4.2 (PROVED) | FALSE as stated (several tiny minors); repaired | F-COR |
| Example 4.3 (PROVED) | correct as finite algebra; realizability by an f open | B.9 |
| 4.2 shifted-block Farkas form (SKETCH) | SKETCH, honest | - |
| Lemma 5.2 (PROVED) | correct with precisions | P-52 |
| Proposition NE (SKETCH) | plausible SKETCH (statement about realized ratios) | - |
| 5.3 bias-free preparation (SKETCH) | plausible SKETCH | - |
| 5.4 + bottom line (6): "pinned residual disappears in unshifted blocks and shifted blocks without near-threshold actives; core = inward-locked near-threshold carriers" (SKETCH) | WRONG: rests on a design clause incompatible with (K2-d) + (L-K2-1) | F-NE |
| 4.4 (D-abs) long memory (SKETCH) | consequences re-derived; compatibility check pending; SKETCH honest | B.10 |
| Theorem H2.B, Theorem H (PROVED as necessary conditions) | correct with quantifier precisions | Q-1, Q-2 |
| (R1) excluded at all large stages; (LSC-trunc)_N for every f; density for p_N, p | OPEN (not claimed) | G |

## B. Re-derivations (claims found correct)
B.1 Facts 1.1/1.2.  Near coordinates N_l lie in S_l ∩ (s_max(L), d(L)] and are private among coarse carriers, so a thick one makes l thick-type;
(R1) excludes this directly.  No thick near coordinate => no (P3)/(P4) => no kind (ii)/(iii), and h = 0 (h is defined only through (P4)
coordinates).  Data-carrying carriers: an off-F near coordinate is a data-sign contact (a free one forces c_l = 0, K1 2.1(b)); a thin one has
s_s = eps_l (K1.3(S) with K1.2: |c_l| v_l(s) <= 4|a^r_s|/t <= 8b/t against |c_l| >= K_*^2 K t/(4D), v_l(s) >= 1/H, b <= T^4).  After (P) they are
S_th of the data sign: kind (iv) unless a pre-placed TU lever exists (kind (i)).  Unshifted block: Delta'_m = 0 => Delta''_m = Delta'_m kappa'/
kappa^# = 0 (K1.1(2)) => every coarse peak is zero-data; V1 Lemma D gives a robust one; its near coordinates are off F or thin, hence ZD after
(P): J1-ref R-PK applies.  Shifted block: robust peak data -Delta''_m lambda_c vs_c (robust peaks have Domega = 0 in the class cone, J2 1.3); its
near coordinates are data-sign S_th; with z_s = -sgn(Delta''_m) vs_c and d kappa_m/d zeta(c) = vs_c (1 - X_m) (H1 Lemma NP's computation; (FC),
U1 Lemma 1.4(a)) the bank moves kappa_m by -sgn(Delta''_m)(1 - X_m) lambda_c eff_s v_c(s) per unit, the same direction for every robust peak.
Fact 1.2: K2.16(3) with h = 0, gamma_0 = c_1/(4||h||) = +infinity: ||coef_(i)|| <= small', ||coef_(iv)||_2 >= c_1 - small', kappa <= -c_U/2 =
-c_1/(8 H(L)).  [Weak peaks: their switching sign eps_k = vs_k sgn(e_k - Delta'_m) (J2 1.3) is the sign of gamma_k, i.e. the data sign on their
private coordinates, so the kind-(iv) orientation (1.2) holds for them too.]
B.2 Lemma 2.1.  (R-mod') = (K2-c) covers s <= D(L).  A robust s in F ∩ [1, D] \ T(L) is an anchor (off U_L; K2.17(b)) or lies in S_k for a
coarse k (supp u_k = supp y_k ∪ S_k, supp y_k ⊂ T(L)), private among coarse carriers, thick: k is thick-type.  K2.16(4) holds at every s <= D(L).
B.3 Lemmas 2.2, 2.3.  Lemma 2.2: main targets by allowedness (a), (c+); PRE absorbers: s in Sigma(Y_r) ⊂ [1, p_r - 2|supp Y_r| - 1] ⊂ [1, l_r]
(|Sigma| <= |supp Y|) while the PRE stage exceeds l_r; cluster absorbers at p+i: signature coordinates of E^ch(p) lie in T(p) (induction) or in
S ∩ [1, p]; the odd p_i lie in Z_0.  Lemma 2.3: v_l(j) <= x''_max <= T^2 gives j >= 2n(w) - l - C; v_l(j) >= c_0 W >= c_0 C T^4/p gives j <=
5 log2(1/T).  R(p+1) >= 5 + 2 log2(1/lb_{p+1}) and lb_{p+1} <= c^cl(p) <= exp(-1/T_lo(p, M(p))) ((W_exp)), so s_max(p+1) >= p_0 + 2R >=
4/T_lo(p, M(p)) >= 4/T > j.  p' <= p + 2(s_max(p) + p) + 2(r + 1) + 1 ((D-enum): |Sigma(Y_{r+1})| <= r + 1) << 2n(w) (n(w) >= Q(w) >= (4
Design(p)/u)^{20}, Design(p) >= 2^{D(p)} >= 2^{s_max(p)}), so j notin T(p') by Lemma 2.2.  For p'': j > p' gives j notin E^ch(p'); PRE stages of
round r+2 and the main target of p'' live in [1, r+2] ((D-enum)).  (D-enum) is realizable (dovetail the countable pool so that position i
carries a vector supported in [1, i]; i_nu = 1;1,2;1,2,3;...) and harmless (k_0, allowedness, density of every block's targets unchanged).
B.4 Idea (1).  At j in F with s_j = -eps_l, eps_l v_l(j) z_j = -v_l(j) is already minimal; lowering a_j keeps z_j = -eps_l; flip-then-pull has net
capacity 0; lowering removes the deep-raise cushion of the anti-sign data.  The literal mechanism is void.
B.5 Lemmas 2.6, 2.7.  (i) The pull range lies in E_c(w_p) (s_far >= 2 log2(1/c_{L+1}) >= 2/(T ln 2) >> 5 log2(1/T)).  Off-F coordinates of an
active carrier's (or a shifted block's peak's) signature set are data-sign near-contacts: the signature room is tiny or robust at the clean
sub-window; robust room forces gamma_l = 0; tiny room <= b gives 1 - eps_l z_j <= b/v_l(j) << 1 on the pull range: pullable.  So with Cap_l <
4W' every coordinate of S_l with v_l(j) in [8W', x''_max] is in F with s_j = -eps_l or super-thick; at an (R1) stage L'' Lemma 2.1 excludes
super-thick (|a_j| <= b(w'') << x''_max(w_p)).  (ii) At L'' in {p', p''} the coordinate j is private among coarse carriers (new coarse carriers
live on T(L'') ∌ j or on their own S_k), at design depth (D(L'') >= s_max(p+1) > j), unraised (J(w'') > D(L'')).  K1.3(S) at L'' with the same
data sign: |c_l| v_l(j) <= 4|a^r_j|/t <= 4 b(w'')/t; K1.2: |c_l| >= K_*^2 K t/(4 D(L'')); so v_l(j) <= 16 D b(w'')/(K_*^2 K t^2) <= T_lo(w'')^2 <<
c_0 W(w_p) (T_lo(w'') <= 2^{-n(w'')}, n(w'') >= 2^{20 D(L'')} >= 2^{80/T_lo(w_p)}).  (iii) 2.7(a), contact or near-contact z_s = eps(1 - delta): an
anti-sign switching costs at least |Delta B(s)| in the flip budget (the excess at s is |tau B(s)|(1 - sgn(tau B(s)) z_s) >= |tau B(s)|(1 - delta')
for the anti-sign side), so |c^act_l| v_l(s) <= (1 + eta') t/q_0 + C c_{p'+1}; K_*(w')^2 K >= K_P(w') = 8 C_q 2^{J(w')} D(p')/delta_min(p') with
8 C_q >= 128/(3 q_0) and 2^{J(w')} >> 2^{d(p)}: contradiction (if delta >= u(w') the coordinate is free with robust room at p' and l is inactive).
Thin case: K1.3(S) at p' with |a_s| <= b(w') (this is where (R1) at p' is needed).  (iv) Privacy of the OLD NEAR coordinates s in (s_max(p), d(p)]
at p': cluster absorbers after p take signature coordinates <= s_max(p) (E^ch(p) ⊂ T(p) ∪ [1, p] and s_max(p) >= p for p >= 2, every absorber
stage raising s_max by >= 2R + 2); PRE absorbers of round r+1 and the main target of p' lie in [1, r+1] with r + 1 < p.  So (D-enum) is used.
At p'' the old near coordinates may be absorbed (s < p' is possible), which is why 2.7(a)/(b) reach only p'.  (v) Peaks: vs_c and robustness
are f's data; the K1.2 lower bound covers coarse peaks.
B.6 Lemmas 3.2, 3.3.  3.2: separate b'' in B(b, rho_0) from the compact convex (W/2)Q - Box (contains 0): (W/2) max(0, max_g(-y^T g)) <
-y^T b'' and max_Box y^T sigma < -y^T b'' <= phi_y + rho_0.  3.3: with banded K^- rows only, |r^#_l| <= |rt_l| (beta <= kappa_min u/(4 Design^C)
keeps the sign), so R^2 = m^2 sum_Omega r^2 does not increase; by Lemma K every rho_d = m|r_d| K(sigma, R^2)/Phi_d is <= its target value, where
sigma = Phi_P^2 + s_f depends only on the (frozen) peak PATTERN, not on realized peak values (X1 1.1); protected statuses are upper bounds,
robust ones move by << u; Z_kappa untouched (free rows).
B.7 Theorem H2.A (case analysis).  On banded rows (y_l)_+ < delta_1 = c_1 u/(16 |Lambda|^2 Design^{C_3+C_4}) and y_l >= -e_1 (1.2).  Kind-(i)
rows contribute <= e_2 to zeta_m.  two-sided & P^- = {}: sum_{K^+} y_l|rt_l| <= sum_{K^-} y_l|rt_l| + e_2 + (4/3) eps Design; up & P^- = {}: same
from zeta_m <= small; two-sided or down & P^+ = {}: sum_{K^-} y_l|rt_l| <= sum_{K^+} y_l|rt_l| + small.  With |rt_l| >= u/Design^{C_3}: y_l <=
c_1/(16|Lambda|) + Design^{C_3}(e_2 + 2 eps Design + |Lambda| e_1 Design^{C_4})/u on every kind-(iv) row, so sum_{(iv)} y_l < c_1/4, against
3.1(a).  Size: eps < 2(||b|| + rho_0)/W <= 4 u^3 Design^{-C_A}, so the error terms are << c_1/|Lambda|.  Numerics: H2's toy_onesided rerun
identical (4000/4000); independent model with common-mode perturbations of the private columns: 699/699 non-residual configurations
feasible for all sampled right-hand sides (ref_h2a_shared.out).
B.8 Proposition 3.5.  (a): in (R1) J1's (R-pk)/(R-np) and H1's (U+) are vacuous (they concern thick-type carriers).  (b), (c), (e) as B.1, B.5.
B.9 Example 4.3.  On the line C'_+ x_+ + C'_- x_- = 0, x_+ = t C'_-, x_- = -t C'_+; the constraints x_+ >= rc_+, x_- >= rc_- give t in [rc_+/C'_-,
|rc_-|/C'_+], nonempty iff M(rc) <= 0; with a margin mu on both rows: iff M(rc) <= -mu(C'_+ + C'_-).
B.10 (D-abs).  With E^ch'(p) = T(p) ∪ (Z_0 ∩ [1, p]): T(L) ∩ (union S_k) ⊂ [1, r(L)]; old near coordinates and old pull-range coordinates stay
private while r(L'') < s (resp. j), stay at design depth and unraised, and Lemma 2.1 holds at every (R1) stage L''; intermediate stages need not
be (R1).  Each (up)/(down) block uses one robust peak c, whose old pull range (2.6) and old near coordinates (2.7(a)) forbid both shift signs at
later (R1) stages of the range: at most N such events per range; kind-(iv) carriers are fresh within it.  The cluster stage p+1 still exists
(1 in Z_0 ∩ [1, p]), so s_max(p+1) >= 4/T_lo(p, M(p)) and (W_exp) persist; absorbers are off the MT VI tree (Q1-refa, X2-ref R-abs).  Pending:
the (W4'') list (only removes upper bounds on weights).

## C. Findings and fixes
F-NE (5.4 and bottom line (6); the argument FAILS).  5.4 assumes the design clause C_L((1 + Lip C_*) b(w))^{2/N_L} <= delta_Z, "b only appearing
as an upper threshold".  False: (K2-d) sets theta_0 = b/Design^{C_P}, and (L-K2-1) requires s_1 <= theta_0 T/(8 rho A_0) (the theta piece of
Theorem UE^inf must not destroy the theta_0 banks).  Hence b >= 8 rho A_0 Design^{C_P} s_1/T, while (NE) needs delta_Z <= delta s_1/(64 rho C_f
Design^C).  The clean dichotomy only says that a tiny minor satisfies |M(r_1)| <= (1 + Lip C_*) b; a row f whose tiny minor takes a value
in (Lip(M) delta_Z, b] is admissible, and for it dist(r_1, Z_kappa) >= |M(r_1)|/Lip(M) > delta_Z (Lip(M) <= Design^C).  So a design clause
guaranteeing a near-exact start for EVERY f must give b <= Design^C delta_Z <= delta Design^{C - C'} s_1/(64 rho C_f), contradicting b >=
8 rho A_0 Design^{C_P} s_1/T at small T, for every admissible s_1.  (Equivalently: H2's clause C_L((1 + Lip C_*) b)^{2/N_L} <= delta_Z forces
b^{2/N_L} <= delta_Z/C_L, and b^{2/N_L} >= b since N_L >= 2.)  Decoupling theta_0 from b does not help: theta_0 >= max(8 rho A_0 s_1/T, 4 Design K_DC r) is required ((L-K2-1),
(L-K2-2)), and (P3) raises of thin TARGET coordinates / (P2) banks of target contacts move pinned values by ~ eff u_k(j) theta_0 >> delta_Z.
So the start row is in general at distance ~ C_L (2b)^{2/N_L} >> delta_Z from Z_kappa; the Lojasiewicz displacement remains, and in every block
type a one-signed resonance on which f lies on the wrong side by more than delta_Z (and at most C b) still obstructs.  5.4 (a), (b) and the
summary claim do not follow (they also contradict H2's own 5.3: "remaining honest residual ... or rows with a wrong-sided resonance of f").
CORRECT STATEMENT (SKETCH, conditional on (NE) and 5.3): the residual of (R1) consists of wrong-sided one-signed resonances of f's stage data
by more than delta_Z (any block type), fully swallowed kind-(iv) carriers, and (T)-block near-threshold phenomena; (NE) only removes the
near-coincidences within delta_Z << b.

F-COR (Corollary 4.2: FALSE as stated).  With several tiny minors a Farkas certificate lambda may combine them.  (A) M_1 = x_1 + y, M_2 = x_1
+ 2x_2 + 3x_3 + y (y two-sided, x kind (iv); every minor has a nonzero two-sided cofactor): lambda = (-1, 1) gives (lambda^T C')_Q = 0,
(lambda^T C')_P = (0, 2, 3) >= 0; residual iff 2 rc_2 + 3 rc_3 > 0 (consistent with robust ratios: x_2 > 0 > x_3).  (B) M_1 = x_1 - x_2, M_2 = x_2 -
x_1 + x_3 + x_4 (mixed signs in every minor): M_1 + M_2 = x_3 + x_4, residual iff rc_3 + rc_4 > 0.  LP-verified (ref_cor42.out).  REPAIR (PROVED):
if the cofactor matrix C'_Q of the tiny minors on the pinned two-sided rows has full row rank, then (lambda^T C')_Q = 0 forces lambda = 0 and the
block is not residual (Proposition 4.1); 2000/2000 random checks.  H2's two conditions are correct for a SINGLE tiny minor.

G-CPL (Theorem H2.A / Lemma 3.4(a); fixable gap).  K^+ bands in (U)-blocks need J1-ref F-2's rescaling s_m of ALL targets of the block, which
moves the right-hand side and every generator (J1-ref P-1).  The proof's inequality must be read at the coupled targets rt(s): phi_y(s) =
phi_y(1) + kappa_m (1 - s) zeta_m(y; rt(1)) and |zeta_m(y; rt(1))| <= (8/3) eps Design (R-PK; s >= 1/2), so sum_B beta_1 (y_l)_+ < phi_y(s) + rho_0
<= ||b|| + rho_0 + 3 kappa_m (1 - s) eps Design, with 1 - s <= C(Lip eta' + D^C sum_B (|r_l| beta_1/kappa + beta_1^2/kappa^2)) <= C Design^C
beta_1/kappa_min; the extra term is <= C Design^{C+1} eps beta_1 << beta_1 delta_1, so the bound (y_l)_+ < 2 delta_1 survives and the case analysis
goes through.  [Bounding phi_y(s) by ||b(s)|| <= ||b|| + kappa (1 - s)||rt|| instead would fail: the extra C Design^C beta_1 is of the size of
the band.]  Realization: J1.8(a)-type Brouwer for every s in its range and the joint selection of F-2(d); the fixed point beta_1 =
16|Lambda|^2 Design^{C_3+C_4}(||b|| + C_2 W(beta_1)^2)/(c_1 u) exists as in F-2 (rho_0 << ||b||).  (KN)-blocks: K^+ bands there inherit J1.10's
SKETCH; K^- bands are fine (statuses decrease).

P-41 (Proposition 4.1; scope).  The Farkas alternative is exact for: one block, the other blocks' pinned ratios FIXED, each kind-(iv) row moved
only upward by private resources, no margin.  (i) A tiny minor may contain (X3) rows of several blocks; its cofactors along (X3)_m then depend on
r^{(m')} and the joint problem is multilinear (the per-block "iff" can fail both ways when another block's pinned ratio is two-sided).
(ii) Shared design-depth generators at TARGET coordinates (TS/FR/ZD moves acting on all carriers whose targets contain the coordinate) are not
in the model; they change the realizable set (toy: 478 of 654 privately obstructed residual configurations become realizable with two random
shared two-sided columns, ref_h2a_shared.out).  Moves at a contact coordinate j leave every minor containing j's contact row invariant at first
order (the value change is proportional to that row), so whether they help depends on the minors.  (iii) Realization needs strict feasibility
with margin of order rho_0 (B.9).  Hence "in an unshifted block this residual is EXACTLY a one-signed linear resonance" must read: "the restricted
single-block model obstructs iff ...; the actual residual is contained in the union over such certificates, for the joint system".
The converse direction (no certificate => realization) needs the cone condition of K2.9 at the displaced, primal-feasible target with a
margin of order rho_0 (kind-(iv) components of b(rt') pointing strictly upward), with H1's size bookkeeping (Lemma TF', refereed correct by
H1-ref with precision P-TF on displacement sizes and x_TU).

P-25 (Lemma 2.5).  (1) The cushion for anti-sign data at a design-depth coordinate is |a_s| >= t|c_l(t)| v_l(s)/5 for all t of the window,
>= K_*^2 K T_hi^2/(20 D H) at t = T_hi (H2's "T_hi/(C D H)" presumes |c_l| >= 1/(CD)); the corrected mass is still unaffordable (T_hi^2 >> u^2
T_lo^2).  (4) "v_l(j) > x''_max: unaffordable" is proved only relative to the certified cost bounds: a pull costs at least its support mass
(p* is equivalent to the l_1 norm, the base change has l_1 mass >= 24 lambda_l v), i.e. >= c v/D(L), and at most C Design v log(1/v); depths
in between are undetermined.  Lemma 2.5 is correct for "moves of the toolbox within the certified budget".  Not load-bearing for H2.A.
"Pull ranges are ENTIRELY anti-sign": only [8W', x''_max] is; pullable coordinates of total capacity < 4W' may remain in [c_0 W, 8W').

P-31 (Proposition 3.1(b)).  The bank coordinate already carries the mass theta_0 (D_Psi(s) = Psi(s) - kappa a_s), so the one-sided column is
y^T g = sgn(Delta''_m)(1 - X_m) lambda_c eff_s v_c(s) zeta_m + eff_s |kappa_y| theta_0 >= -eps, i.e. sgn(Delta''_m) zeta_m >= -(4/3)(eps Design^2 +
|kappa_y| theta_0 Design) (eff_s >= 1/Design and lambda_c v_c(s) >= 1/Design separately).  Harmless (theta_0 = b/Design^{C_P} << c_1 u/Design^C).

P-RANGE / P-AGG (Lemmas 2.3, 2.4).  H2's pull range [c_0 W, x''_max], x''_max = u^2 T^2/(C Design^C log^2(1/T)), exceeds R-6's x'_max; pullability
and super-thickness must be re-defined with x''_max (lowering threshold |a^r_j| <= x''_max), as R-6 did.  Cost (R-6 list per carrier: flip
C_f lambda v log(e/v), lowering <= 2(1 + ||U||)|a_j|, pull mass 24 lambda v, bank <= 2 Design nu v): <= C Design x''_max log(1/T) =
O(u^2 T^2/(Design^{C-1} log(1/T))), times |Lambda| <= Design: theta'/c_flat^2 gains C/(Design^{C-2} log(1/T)) -> 0.  Pre-place a SUBSET of pulls
with capacity in [4W', 20W'] (take pullable coordinates in increasing v; each has capacity < 16W' if v < 8W', and a single pull with v >= 8W'
already has capacity >= 4W'): compensating bank O(Design W'), second-order residue O(Design^2 W'^2) << rho_0-scale.

P-OWN (Lemma 2.6 proof).  "owned with z = eps_l, K1 1.1(1)(a)" refers to Step B, which route V omits (K1.S).  The correct reason is B.5(i):
tiny signature room (robust room forces gamma_l = 0).

P-52 (Lemma 5.2).  (i) The bias exists per banked (or raised) near coordinate; a kind-(iv) carrier whose near coordinates are thin with |a_s| >=
theta_0 receives none.  (ii) "Charging a banked row" must mean a ROBUST oriented cofactor (cofactors are rate objects: tiny or robust); then
the shift of lambda^T M is >= u theta_0/Design^C >> delta_Z.  (iii) (P3)/(P2) at TARGET coordinates are further, shared bias sources (F-NE).

Q-1, Q-2 (Theorems H2.B, H).  "The selected stage" must read "every clean sub-window and class with >= n(w)/D_cl(w) scales" (non-coverage of
(LSC-trunc) = no (w, a) realized).  The memory conclusions need CONSECUTIVE (R1) stages (2.7(a),(b): one stage; 2.6: two stages); with
interleaved (R0)/(R1) stages only (i)-(iii) are per-stage conclusions.

## D. Numerics (sanity only; r13/H2_ref_work/)
 rerun/: H2's toy_onesided (4000/4000) and toy_resonance (3000/3000; Example 4.3) reproduced, outputs identical.
 ref_cor42.py/.out: counterexamples (A), (B) to Corollary 4.2 (feasible at lambda^T M(rc) = -1e-4, infeasible at +1e-4); full-row-rank repair
   0/2000 infeasible.
 ref_h2a_shared.py/.out: independent model with common-mode perturbations (1e-3) and optional shared two-sided columns: non-residual
   699/699 feasible; residual 801, of which 654 privately infeasible for a sampled right-hand side and 478 of these rescued by two random
   shared columns (residual = necessary, not sufficient, condition for obstruction in models with shared generators).

## E. Most valuable idea
Cross-stage memory (Lemmas 2.3, 2.6, 2.7).  The cluster absorbers after a main stage push s_max beyond 4/T_lo(p, M(p)), so every coordinate a
kind-(iv) carrier relied on at stage p -- its data-sign near coordinates and its anti-sign far pull range -- is, at the next main stage, a
private, unraised, design-depth coordinate on which (R1) forces |a| <= b.  Lemma K1.3(S) and the flip budget then forbid that carrier (or a
shifted block's robust peak) to be active again with either sign: one-sided obstructions cannot be reused, every kind-(iv) carrier deactivates,
(up)/(down) blocks become unshifted, and with (D-abs) each (carrier, sign) is used at most once per round range.  Together with H2.A (one-sided
overshoot bands on all movable kind-(iv) rows at once, against the all-at-once positivity sum_{(iv)} y_l >= c_1/4 and the per-block lever
balance), this reduces (R1) to fresh, pinned, wrong-signed resonances at every stage.

## G. What remains open (precise)
(1) (R1) at all large main stages: in every clean sub-window/class some block is residual -- (two) pinned K^- and pinned-or-locked K^+ rows, (up)
    pinned K^- rows, (down) pinned-or-locked K^+ rows -- and the resonance is fresh at each consecutive (R1) stage.  In the restricted single-block
    model of an unshifted block this is a wrong-signed one-signed linear resonance of tiny minors (Prop. 4.1); the joint multi-block form, the
    role of shared target-coordinate generators, and the shifted-block form (4.2) are not written.
(2) Lemma 3.4(c) (exchange/compensation in protected shifted blocks): SKETCH; without it such K^+ rows are locked.
(3) Exactness versus one-sidedness: (NE) and the bias-free preparation (5.3) are SKETCHES, and even granted they leave wrong-sided resonances of
    size in (delta_Z, C b] in every block type (F-NE); a genuinely new treatment of pinned kind-(iv) ratios is needed (e.g. a face-wise Hoffman
    bound insensitive to tiny minors, H2 4.6(iii); or a value-neutral preparation at target coordinates).
(4) Persistence: whether fresh wrong-signed resonances can occur at all large stages (with (D-abs): at most N (up)/(down) events per round range).
(5) (D-abs): the (W4'') re-check.  Inherited: the once-refereed links of the chain, H1's (R0) analysis.
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N and of NA((c_0, p), l_2^2) for the Martin-type p: OPEN.  No counterexample is
claimed by H2 or suggested by anything found here: every residual configuration is a stage-wise sign coincidence of f's data that must be
renewed at every main stage.
