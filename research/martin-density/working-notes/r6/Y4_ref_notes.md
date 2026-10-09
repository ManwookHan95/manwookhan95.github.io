# Y4 referee notes (Round 6): fixes and new results, with proofs

Setting: paper/martin_density_note.tex (Sections 1, 7, 8), the refereed Round-5 results (Z3 Thm E, Lemma U, Lemma 3.1,
Prop. T with the Z3-referee fixes; explosive design (D1^F) of Z3_ref part 4; design D''' and Thm U' of Z6_ref 3.3-3.4),
and Y4_notes.md.  Finite block set I = {1..N}, p = p_N, F = supp a finite.  Labels PROVED / SKETCH / HEURISTIC / FALSE /
OPEN.  Part files: Y4_ref_part1.md (Part 1 of Y4), Y4_ref_part2.md (Part 2 + far pulls), Y4_ref_part3.md (reductions,
Part 4, non-window viewpoints, numerics, hunt).  Scripts: Y4_ref_work/{n3_check.py, pull_check.py, tune_check.py}.
Notation: for a carrier l, v_l := delta_l h_l/n_l (so u_l = v_l on S_l, Thm thm:SLD (P1)); the VALUE of l at a first
row is val_l := eps_l u_l(zhat); T(L) := union_{l'' <= L} supp y_{l''}, s_max(L) := max T(L).  A carrier l is SWALLOWED
WITH SIGN eps_l at f if z_s = eps_l for every s in S_l \ F (exactly swallowed, "bad" in Def. def:swallowed).

## A. Fixes to Part 1 of Y4

**A.1 (explosive design with R rate types).**  PROVED.  In (D1^F) of Z3_ref 4.1 replace u(l) := F(l)^{-1/(4l)} by
u_R(l) := F(l)^{-1/(4Rl)} and the third term of F(l+1) by b(l)^{-4R(l+1)}.  Then the bands (b(l), u_R(l)) are pairwise
disjoint (proof of Z3_ref Lemma 4.1.2 verbatim: u_R(l+1) <= F(l)^{-2/(4R(l+1))} <= u_R(l), u_R(l+1) <= b(l) by the new
third term, b(l) <= 4^{-2F(l)} < u_R(l)), Proposition 1.2 of Y4 holds verbatim (counting), and at an unblocked window
the robust factors of R multiplicative types per carrier give a product <= (4/u_R)^{R l} = 4^{Rl} F(l)^{1/4}, absorbed
as in Z3_ref Prop 4.3.1(a).  Without the change the product can reach 4^{Rl} F^{R/4}, not absorbed for R >= 4.
**A.2 (what Prop. 1.2 covers).**  Target rooms are per coordinate (|supp y_l| objects for carrier l, unbounded);
Prop. 1.2 covers them only under a design restriction such as |supp y^{(i)}| <= i and i_r <= r^{1/2} (then
sum_{l in L_N, l <= L} |supp y_l| <= N((2L)^{1/2} + 1)(2L)^{1/4} = o(L)).  Slaved rooms (l, A) are joint objects and are
not covered by Prop. 1.2.  D^PW covers both.
**A.3 (D^PW: three design corrections).**  In Definition 1.4 of Y4 use
   Design^PW(l) := l 2^{l^3} Lambda°(l) Xi'(l) (1 + 2^{s_max(l)}/delta_min(l)) 2^{G_l} H_tune(l),
   Q(w) := (4 Design^PW(l)/u(w))^{omega(l)+3},
everything else unchanged (u(w) := b(w^-), n(w) := ceil(l 2^{l^3} Q(w)), T_hi, T_lo, b(w) := T_lo(w)^4/(l Design^PW(l)),
c_{l+1}).  Here 2^{s_max(l)}/delta_min(l) is the room-closing conversion factor of Z3_ref fix G5 (target-induced terms
min(lambda_{l''}, |y_{l''}(delta)|) with |delta_s| <= r n 2^s/delta), G_l is the gap bound of the signature sets
(addendum (G) below) and H_tune(l) the tuning constants of C.6-C.7 (the maximum, over the finitely many patterns and
subsets of level l, of the Hoffman constants H(R, NT) of C.7, times max_{l' <= l} 1/(s_{j'}^2 v_{l'}(j')) over the design
bank positions j' of C.6).
Reason for the larger Q: the window constant K of Prop. T / Thm U' is a product of the room product
(<= Design (4/u)^omega at a clean sub-window), the d-row Hoffman constant (<= Design/u by Lemma 1.8) and further design
factors; Q(w) must dominate every such product of bounded degree.  Lemma 1.5, Thm 1.6 (pigeonhole) and Cor. 1.7
(absorption) then hold as stated, with K <= C_f^{l^2} Q(w), K T_hi(w) <= C_f^{l^2}/(l 2^{l^3}) -> 0, n(w)/K -> infinity,
and exactification cost <= C_f Design^PW(l) b(w) log(e/b(w)) <= C_f T_lo(w)^4 (4n(w) + log(l Design))/l = o(T_lo(w)^2)
(the log is that of Lemma 3.1 / Lemma 2.2).  PROVED (bookkeeping).  Robust gaps enter through c_flat <= gamma_B/(2A_2)
(Z6_ref 3.6), i.e. through n >= 48 rho^2 K/(c_flat(1-rho^2)) and theta <= c_flat^2(1-rho^2)/(24 rho^2) in Thm E: both
absorbed by the same Q(w) and by theta = C_f T_lo(w)^2 n(w)/l.

## B. Precisions in Part 2 of Y4 (all claims re-derived; verdicts in Y4_ref_part2.md)
**B.1** Lemma 2.6: for a ray vector W, supp W cap K is infinite, so a + mW has infinite support (outside Thm E).  For
finite banks use W_J := W 1_{F u (K cap [1,J])}: d/dm W(zhat(a + mW_J)) = <P^perp U^*W, P^perp U^*W_J>/nu ->
||P^perp U^*W||^2/nu (J -> infinity).  PROVED.
**B.2** Prop. 2.8(a) uses a change m W 1_F on F (not a pure bank).  For a pure bank the rate is
<P^perp U^*W, P^perp U^*(W 1_K)>/nu, which equals sum_{j in K} s_j^2 W(j)^2/nu >= 0 for a diagonal base and has no sign
in general.  PROVED.
**B.3** Prop. 2.8(b) is correct for the move class (masses with the contact sign at contacts, beta on F, zeta on J_free);
its consequence "lowering is possible only through the |F| - 1 channels on F" is FALSE for companions: see C.
**B.4** In Prop. T at a tuned row balance with kappa a/a(zhat^tau) (a(zhat^tau) != 1); a vanishes on banks and pulls.

## C. The far pull: a per-carrier lowering channel at companions (NEW)

**C.1 Definition (pulled row).**  Let l be swallowed with sign eps := eps_l, j in S_l \ F, mu > 0.  Put
A := a - eps mu e_j^*, a' := A/q^*(A), z'_j := -eps, z'_i := z_i (i != j).  Then supp a' = F u {j}, z' = sgn a' on
supp a', |z'| <= 1: (a', z') is admissible forced data (Remark rem:lemmaZ(c)); the first row f' is the PULLED ROW.
Pulls, banks (masses of the contact sign at contacts) and changes on F combine; the resulting rows are not norm attaining
and need not be (Thm E applies Cor. D1 at the row itself).  This is the "far sign-flipped contact with negative mass" of
Round 2 (P1 6.3, P2A, N2 Thm 1), used there on engineered NA approximants; here it is used on companions.

**C.2 Lemma P1 (effect and cost).**  PROVED.  Let L >= l, j > s_max(L), mu ||U|| <= nu/2.
 (a) zhat' - zhat = -2 eps e_j + U(e' - e), ||e' - e|| <= 2 mu ||U^*e_j^*||/nu.
 (b) val_l' - val_l = -2 v_l(j) + rho_l and u_k(zhat') - u_k(zhat) = rho_k for every carrier k != l with k <= L, where
     |rho_k| <= 2 mu ||U^*e_j^*||/nu.  For a diagonal base (U^*e_i^* = s_i k_i, (k_i) orthonormal, s_i > 0):
     rho_k = <U^*u_k, e>(nu (nu^2 + mu^2 s_j^2)^{-1/2} - 1) - eps mu s_j^2 u_k(j) (nu^2 + mu^2 s_j^2)^{-1/2},
     so rho_k = O(mu^2) for k != l, k <= L.
 (c) p*(f' - f) <= C_f (v_l(j) + mu) log(e/(v_l(j) + mu)) when v_l(j) + mu <= c_f.
 (d) Every S_{l''}, l'' != l, has the same room at f' as at f; z' = eps on S_l \ supp a' (l stays swallowed with sign
     eps); the rows of Lemma lem:exactswitch on T(L) are unchanged; coarse carriers keep their status as long as
     v_l(j) + mu is below their threshold distances.
Proof.  (a) z' - z = -2 eps e_j; e' = U^*A/||U^*A|| is scale invariant; ||x/||x|| - y/||y|| || <= 2||x - y||/||y||.
(b) u(zhat') - u(zhat) = -2 eps u(j) + <U^*u, e' - e>, ||U^*u|| <= q^*(u) = 1.  By (P1) and allowedness (a), u_l(j) =
v_l(j), u_{l''}(j) = 0 for l'' < l, and for l'' <= L, l'' != l: j notin S_{l''} (disjointness) and j notin supp y_{l''}
(j > s_max(L)).  Diagonal case: U^*A = U^*a - eps mu s_j k_j with <U^*a, k_j> = s_j a_j = 0 (j notin F), hence
||U^*A||^2 = nu^2 + mu^2 s_j^2 and <U^*u_k, e'> = (nu <U^*u_k, e> - eps mu s_j^2 u_k(j))(nu^2 + mu^2 s_j^2)^{-1/2}.
(c) The proof of Z3 Lemma 3.1 uses only zhat' = zhat + delta and the clamp formula at both rows (w'_m = J_m(R_m^** zhat'),
q'_0 = (1 + sum_m |R_m^** zhat'|_m)^{-1}); together with q^*(a' - a) <= 2(1 + ||U||) mu it gives p*(f' - f) <=
C mu + C_f c(delta), c(delta) = sum_m [Delta_m log(e/Delta_m) + sum_k min(lambda_k, |u_k(delta)|)].  Now
|u_k(delta)| <= 2|u_k(j)| + 2 mu ||U||/nu.  Carriers with u_k(j) != 0: l, and carriers l' > l with j in supp y_{l'}; for
each of the latter allowedness (b) gives 2 c_{l'} <= 2^{-2j} c_l delta_l, so (c_{l'+1} <= c_{l'}/4) the sum of their
lambda_{l'} <= c_{l'}/4 is <= 2^{-2j} c_l delta_l/3 <= 2^{-j} v_l(j) (n_l <= 5/4).  Hence sum_k min(lambda_k,
|u_k(delta)|) <= (2 + 2^{-j}) v_l(j) + sum_k min(lambda_k, 2 mu ||U||/nu) <= C(v_l(j) + mu log(e/mu)) (the last sum by
sum_k min(lambda_k, x) <= x(log_2(2m/x) + 3)), and Delta_m <= C(v_l(j) + mu).
(d) Only coordinate j moved, j in S_l \ T(L); rooms are computed off the support; status by (b) and Lemma 3.1 (block
scalars move by O(Delta)).  QED

**C.3 Lemma P2 (Lemma U and Theorem E with banked and pulled support).**  PROVED (by inspection, as Y4 Lemma 2.3).
Z3 Lemma U and Z3 Theorem E hold for first rows f_n -> f with supp a_n = F u B_n u P_n (B_n banks: contacts of f with
masses of sign z; P_n pulled coordinates: z_n = -z there, masses of sign -z) for data that are contact-like on B_n and
satisfy t |b(j)| <= |a_n(j)| at every j in P_n, t the scale of the data.
Proof.  In Lemma U (proofs of Lemmas lem:uniformtransfer, lem:onesidedtransfer) a_min is used only to exclude flips on
the support, i.e. to get Exc(rb) = sum_{j notin supp a_n}(|rb_j| - z_j r b_j) = 0.  On B_n: contact-like data give
|a_n(i) + r b_i| - |a_n(i)| - z_i r b_i = 0 for r of the side's sign.  On P_n: |r b(j)| <= c_flat t |b(j)| <= |a_n(j)|
(c_flat <= 1/8), so a_n(j) + r b(j) keeps the sign of a_n(j).  All other constants (nu, q_0, sigma_m, C_m, M_m, transfer
data via Lemma lem:persistence) depend only on the convergent forced data.  Thm E then applies Cor. cor:D1 at the fixed
f_n (F u B_n u P_n finite).  QED
**C.4 Lemma P3 (transplanted data at pulls).**  PROVED.  In Prop. T (Z3, with Z3_ref fixes; box rows tau'_l <= 12
lambda_l/t as in Z6_ref 3.4(4)) the switching vector is V' = sum_{l in B'} eps_l tau'_l u_l 1_{F^c}; at a pulled j in
S_l \ F with j > s_max(l_*), V'(j) = eps_l tau'_l v_l(j).  Put b^+(j) := chi_j V'(j), b^-(j) := -(1 - chi_j) V'(j), any
chi_j in [0,1] (two-piece data impose nothing on support coordinates); then t|b^pm(j)| <= 12 lambda_l v_l(j), so the pull
mass mu_j := 24 lambda_l v_l(j) satisfies Lemma P2 (|a_n(j)| = mu_j/q^*(A) >= mu_j/2).  The pull also changes kappa^# and
the d-rows at f^# only by O(lambda_l v_l(j)/t) <= O(Design b(w)/t) << t^2.

**C.5 Design addendum (G).**  Every S_l has bounded gaps (consecutive elements differ by at most G_l), e.g.
S_l := {2^l (2i + 1) : i >= 1}; compatible with Def. def:SLD and with D''' / D^PW (2^{G_l} enters Design^PW).

**C.6 Proposition P4 (two-sided per-carrier exact tuning; diagonal base).**  PROVED.  Let U be diagonal, f with F
finite, L_0 a finite set of carriers, each swallowed with a sign, L >= max L_0, and x in R^{L_0}.  There are eta_0 > 0
and C (depending on f, L_0, L and design data of level L) such that for |x| <= eta_0 there is a first row f^# with
supp a^# = F u {one bank and one pulled coordinate per l in L_0}, z^# = z off the pulled coordinates, and
   val_l^# = val_l + x_l EXACTLY (l in L_0),   |u_k(zhat^#) - u_k(zhat)| <= C |x|^2 (k <= L, k notin L_0),
   p*(f^# - f) <= C |x| log(e/|x|).
Proof.  Let eta := |x|_inf (if x = 0 take f^# = f).  For l in L_0 let j'_l := min(S_l \ (F u [1, s_max(L)])) (bank) and
choose j_l in S_l with j_l > j'_l and 2 v_l(j_l) in [2 eta, 2^{G_l + 1} eta] (possible for eta small: v_l(s) =
delta_l 2^{-s}/n_l and every interval of length G_l beyond min S_l meets S_l).  Step 1 (pulls): pull at every j_l with
mu_l := 24 lambda_l v_l(j_l).  By Lemma P1(b) (diagonal case, applied successively) val_l moves by -2 v_l(j_l) + O(eta^2)
(l in L_0) and u_k(zhat) by O(eta^2) (k notin L_0, k <= L).  Step 2 (banks): for m in R^{L_0} near 0 let A(m) :=
a_pulled + sum_l m_l eps_l e_{j'_l} (a_pulled the unnormalized pulled base) and Psi(m)_l := val_l at the row with forced
data (A(m)/q^*(A(m)), z_pulled).  Psi is C^2 near 0 with |D^2 Psi| <= C_2 (it depends on m only through e =
U^*A/||U^*A||), and since U is diagonal, <U^*u_k, k_{j'_l}> = s_{j'_l} u_k(j'_l) = 0 for k != l (k <= L) and
<U^*a_pulled, k_{j'_l}> = 0, so D Psi(0) = diag(s_{j'_l}^2 v_l(j'_l)/||U^*a_pulled||) =: D_0, a positive diagonal matrix
whose entries are bounded below by C_f^{-1} x (design quantity of level L).  The required increments Delta_l := x_l +
2 v_l(j_l) + O(eta^2) lie in [eta/2, 3 * 2^{G_l} eta]; hence s^0 := D_0^{-1} Delta has s^0_l >= c|Delta| with c > 0
depending only on the entries of D_0, the G_l and |L_0|.  Prop. 2.7 of Y4 (quantitative inverse function theorem; the
bank masses are one-sided channels and (TC) holds with A = D_0) yields m >= 0 with Psi(m) = val + x exactly and
|m| <= C eta, provided C(f) ||D_0^{-1}||^3 |Delta| <= c (true for eta <= eta_0).  For k notin L_0, k <= L, the banks act
only through ||U^*A||, i.e. at second order.  Cost: Lemma P1(c) for the pulls and Y4 Lemma 2.2 for the banks.  The data
conditions of Lemma P2 hold by Lemma P3 (pulls) and contact-likeness of transplanted data (banks).  QED
Numerics (tune_check.py, finite model, diagonal U, carriers with components on F): one pull + two private banks give the
prescribed changes (-x on one carrier, +x on another) with residual <= 1e-16, bank masses >= 0, other carriers moved by
1.4e-4 / 8.9e-6 / 2.7e-6 for x = 1e-3 / 2.5e-4 / 6e-5 (second order up to the discrete overshoot), cost linear in x.
pull_check.py: a pull lowers the pulled value by exactly 2 v(j) (5 digits), other values unchanged, cost O(v(j) + mu).

**C.7 Corollary P5 (exact neutralization of tiny single-block rays).**  PROVED as an exactification step, under the
status part of (BS) for near-threshold q > 0 carriers (see the end of the proof; the subsequent transplant is the
assembly, SKETCH).  Diagonal base, design D^PW with A.3 and (G).  At a clean
sub-window w of level l, let R_t be the set of extreme rays r (normalized, ||r||_1 = 1) of the combinatorial zero-cost
cones of level <= l of one block m whose rate |D_r|/max_{supp r} Phi is <= b(w) (tiny, including exactly neutral rays).
Their carriers are swallowed strict non-peaks (peaks and tiny-gap q < 0 carriers have rows tau = 0 in the pattern,
Lemma lem:exactswitch and Lemma 2.9).  For a strict non-peak, the threshold lemma gives w_m(k) = C_m zeta(k)/(Phi^2
sigma_m) with zeta(k) = m Phi q_0 u_k(zhat), hence q_l = eps_l Phi w_m(k)/(m C_m) = q_0 val_l/sigma_m and
D_r = (q_0/sigma_m) V_r(zhat), V_r := sum_l r(l) eps_l u_l.  Let L_0 be the union of the supports, R := (r(l)) and
V := (V_r(zhat))_{r in R_t} = R val.  Let NT be the set of q > 0 carriers of L_0 with tiny threshold distance.  The
polyhedron {x : R x = -V, x_l <= 0 (l in NT)} is NONEMPTY (x = -val: R(-val) = -V, and -val_l < 0 on NT because
q_l > 0 there); by Hoffman's theorem its point nearest to 0 has |x| <= H(R, NT) |V|, where H(R, NT) depends only on R and
NT, hence is bounded by a design constant H_tune(l) (maximum over the finitely many patterns and subsets of level l).
As |V| <= C_f b(w) (|V_r| = (sigma_m/q_0)|D_r| <= (sigma_m/q_0) b(w) max Phi), Prop. P4 gives a companion f^# with
V_r(zhat^#) = 0, hence D^#_r = 0 EXACTLY for every r in R_t; all other ray d-sums move by <= C Design^PW(l) b(w) << u(w)
(robust rays stay robust); p*(f^# - f) <= C Design^PW(l) b(w) log(e/b(w)) = o(T_lo(w)^2).  STATUS: the tuning moves the
VALUE of every NT carrier away from its threshold, carriers with robust threshold distances (>= u(w) Phi) move by
<< u(w) Phi, q = 0 carriers have gap M.  The only remaining status risk is the drift of the BLOCK threshold, which moves by
O(Delta) (Z3 Lemma 3.1: block scalars move by C_f Delta) under ANY exactification move (closing rooms, banks, pulls alike):
an NT carrier whose gap is below C_f Phi Delta could be pushed into the peak set by the drift.  This is exactly the status
part of the hypothesis (BS) of Z3 Prop. T, which Prop. T needs for every exactification; so: PROVED under the status part
of (BS) for NT carriers (automatic if NT is empty or if the NT gaps exceed C_f Phi Design^PW(l) b(w)).  Without it one needs
a threshold buffer, e.g. by Y2's donors (which raise the block threshold without moving used values; unavailable only in
Y2's aligned corner), or -- using C.6 once more -- one extra exact equation per block (block threshold of f^# := block
threshold of f plus a buffer) controlled two-sidedly by pulls/banks on an UNUSED swallowed carrier of the block whose value
moves the threshold at first order (the clamp formula of Z3 Lemma 3.1 gives a nonzero derivative whenever w_m(k'') != 0,
generically); since pulls and banks act in both directions, Y2's aligned-corner sign obstruction does not apply: SKETCH.
By Y4 Lemma 1.8 at f^#, the d-row of block m then costs at most |mismatch| x Design^PW(l)/u(w): single-block d-rows are
design-controlled at clean sub-windows, WITHOUT compensators, rigidity, (TC) or Conjecture G_ray.
**C.8 Consequences.**  (i) Y4's directional residual (UN+) is NOT a residual of the companion route (diagonal base,
single-block rays).  (ii) Tiny-margin swallowing-type peaks (P+) are pushed below threshold by a pull (lower val_l by
2 v_l(j) > margin + C c(delta)): they become q > 0 strict non-peaks with tiny gap, admissible by the inward-only
expansion (Z6_ref 2.1/6, Z3 Lemma 5.1); the pattern is then recomputed and C.7 applied.  Per carrier, hence plausibly
also in Y2's aligned corner (SKETCH: not checked against Y2's bookkeeping).  (iii) Z3 Lemma 1.4 (closing a room raises a
d-neutral carrier) and Z3_ref 4.4 ("|F| - 1 degrees of freedom") are repaired in both directions.  (iv) Non-diagonal
bases: pulls still lower per carrier (C.2(b)); Gordan's alternative (no y >= 0, y != 0 with A^T y <= 0, excluded for
z-signed linearly independent functionals by Lemma 2.4) gives a simultaneous continuous raise by banks + changes on F,
but exactness after discrete pulls needs the raise in a reachable cone: SKETCH/OPEN.  As the base U is a free choice
(any compact dense-range U gives NA(q) = c_00, Prop. prop:smooth(c)), the diagonal case suffices for the designed norm.

## D. Numerics correction (N3)
The objective of Y4's min_switch is sum_l (lambda_l/t)(W_+ + W_- - 2w)(l) = |Delta theta_1| + |Delta theta_2| (absolute),
not divided by t.  Re-run (n3_check.py): sum|Delta theta|/t = 0.47 / 0.36 / 0.36 / 0.22 on t = 1.5e-2 ... 7.1e-2
(eps_rel = 1) and 0.04 / 0.10 (eps_rel = 0.01); zero (< 1e-9) elsewhere.  "Band of height ~1.4e-2 t" should read "band of
absolute height ~1.5e-2, i.e. relative height <= 0.5 t".  Qualitative reading unchanged; HEURISTIC.

## E. Status after this report
PROVED: Y4 Prop. 1.2 (counting; with A.1 for absorption), Obs. 1.3, Lemma 1.5 and Thm 1.6 (with A.3), Lemma 1.8,
Lemmas 2.2-2.6, Prop. 2.7, Prop. 2.8 (for its move class), Remark 2.8', Lemma 2.9, convexity/locality; C.2-C.7.
CORRECTED: Prop. 2.8's consequence and the "directional residual" (UN+) (FALSE as a residual of the companion route,
diagonal base, single block); Y4 4.1(a) "PROVED" -> SKETCH; N3 labels.
SKETCH: assembly of Thm E + Prop. T at pulled-banked-tuned companions on clean sub-windows (all exactifications at once,
slaving closure, statuses, combinatorial Hoffman part, Hilbert-part comparison at changed e); (P+) via pulls in Y2's
aligned corner; non-diagonal bases.
OPEN: multi-block rays (m') (vector d-rows; exactification is determinantal, not linear); Y2's coherent shift resonance
(item (h)); (O4) infinite F.  Lemma Z and density of NA((c_0,p_N), l_2^2) remain OPEN for every admissible T (including
D''' and D^PW).  No counterexample; nothing found points to one.
