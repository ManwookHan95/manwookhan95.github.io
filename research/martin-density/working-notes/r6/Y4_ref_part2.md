# Y4 referee, part 2 — Part 2 of Y4 (tuning channels) and the MISSING LOWERING CHANNEL (far pulls)

## 2.1 Line-by-line verdicts on Y4 2.1-2.3 and 2.9
* Def. 2.1 (tuned rows): admissible by Remark rem:lemmaZ(c) (z + zeta = sgn a^tau on supp a^tau).  OK.
* Lemma 2.2 (cost) — CORRECT.  w^tau_m = J_m(R_m^** zhat^tau) depends only on zhat^tau (J_m is 0-homogeneous) and
  q_0^tau = (1 + sum_m |R_m^** zhat^tau|_m)^{-1}, so the proof of Z3 Lemma 3.1 applies verbatim with delta = zhat^tau - zhat;
  |u(delta)| <= ||u||_inf ||zeta||_1 + ||U^*u|| ||e^tau - e|| <= ||zeta||_1 + ||e^tau - e||; sum_k min(lambda_k, x) <=
  x(log_2(2m/x) + 3).  Limitation (not an error): the bound is through ||zeta||_1, so it does not cover z-moves on
  infinite sets (rooms of whole signature sets); for those Z3 Lemma 3.1 must be used directly (c(delta) with
  min(lambda_k, |u_k(delta)|)), as Y4 does in 2.4(i).
* Lemma 2.3 (Lemma U / Thm E with banked support) — CORRECT (by inspection, re-done).  In Lemma U a_min enters only
  through "no flips on the support" (Lemma lem:onesidedtransfer, Base); on a bank coordinate i (a_j(i) = m_i z_i) and
  contact-like data, |a_j(i) + r b_i| - |a_j(i)| - z_i r b_i = 0 for r of the side's sign; persistence of transfer data
  needs only f_j -> f (Lemma lem:persistence).  Cor. D1 is applied at the fixed f_j (qualitative).  Remark (minor): in
  Prop. T the balancing term is kappa a with kappa := (B_+1_F + chi V')(zhat^#); at a TUNED row a(zhat^tau) != 1, so
  use kappa/a(zhat^tau) (a vanishes on the bank, so contact-likeness is kept).
* Lemma 2.4 (joint injectivity) — CORRECT.  sum_j W(j) h_W(j) = W(U P^perp U^*W) = ||P^perp U^*W||^2; F u K u J_free = N;
  U^*W in span(e) => W = mu a in Y cap c_00 = {0} (F finite).
* Lemma 2.5 — CORRECT.  kappa^2 > 0 is a minimum of a continuous positive function on a compact set (unit sphere of the
  finite-dimensional W times normalized a' in l_1([1,s])); split at J_max; |W(j) h_W(j)| <= chan_j (j in F u K),
  <= ||U||^2 chan_j (j in J_free); gamma = kappa^2/(2 J_max max(1, ||U||^2)).  Uniform in z.
* Lemma 2.6 (raising lemma) — CORRECT as a derivative formula (de/dm = P^perp U^*W/nu).  Two precisions: (i) for a ray
  vector W, supp W cap K is INFINITE (signature sets), so a + mW has infinite support and the tuned row is outside the
  finite-F theory (Thm E, Cor. D1).  Use the truncations W_J := W 1_{F u (K cap [1,J])}: the derivative is
  <P^perp U^*W, P^perp U^*W_J>/nu -> ||P^perp U^*W||^2/nu, so finite banks raise at a rate as close as desired.
  (ii) Prop 2.8(a) calls a + mW "a bank", but it contains the change beta = m W 1_F on F; for PURE banks (beta = 0) the
  rate is <P^perp U^*W, P^perp U^*(W 1_K)>/nu, positive for diagonal U (= sum_K s_j^2 W(j)^2/nu), not in general.
* Prop. 2.7 (exact tuning under (TC)) — CORRECT.  G(s) := s - A^{-1}(psi(s) - Delta) satisfies G(0) = s^0,
  |G(s) - s^0| <= Gamma C_2 |s|^2/2, Lip(G) <= Gamma C_2 |s| on |s| <= 2|s^0|; contraction of B(s^0, 2 Gamma C_2 |s^0|^2)
  for |s^0| < 1/(2 Gamma C_2).  psi is defined (by the same formula, with possibly "negative masses") on a neighbourhood
  of 0 and the fixed point lies in {s_k >= c|Delta|/2} on one-sided k, so the tuned row at s^* is admissible.
* Prop. 2.8 (b) — CORRECT AS STATED FOR Y4's MOVE CLASS (masses at contacts with the contact sign, beta on F, zeta on
  J_free): h_W(j) = s_j^2 W(j) - <U^*W,e> s_j^2 a_j/nu = s_j^2 W(j) off F.  Confirmed (N1 re-run: min z_j h_W(j) = 0).
  BUT the conclusion drawn from it ("Hence with diagonal U, LOWERING a z-signed functional is possible only through the
  |F| - 1 two-sided channels on F (plus one second-order rescaling)") is FALSE for the companion route: the move class
  omits the FAR PULL (Section 2.2 below), the standard lowering device of Round 2 (P1 6.3, P2A, N2 Thm 1: "far
  sign-flipped contacts carrying negative masses"; N2 2.1 even records that for diagonal U "masses alone can only RAISE
  v(x'), which is why far pulls are needed").  A far pull lowers the value eps_l u_l(zhat) of a single exactly swallowed
  carrier at first order, at cost proportional (up to a log) to the amount lowered, for ANY base.
* Remark 2.8' (donor rescaling) — CORRECT (X := sum m_j z_j s_j k_j is orthogonal to U^*a and to U^*V for V vanishing on
  the donors, so V(zhat^tau) = V(z) + lambda <U^*V,e> exactly).  The cost remark is right (sqrt cost needs b <= T_lo^8;
  the D^PW of Def. 1.4 has b = T_lo^4/(l Design), so the remark is not usable with D^PW as defined).  Superseded by pulls.
* Lemma 2.9 (anti-sign threshold) — CORRECT.  Re-derived: suplevel(f) with |d_pm t| <= 1/2 gives
  varsigma omega_+(k) <= (3/2)gap/t, varsigma omega_-(k) >= -(3/2)gap/t; (omega_+ - omega_-)(k) = -eps_l tau_l/lambda_l
  + Delta d w(k); multiply by varsigma = -eps_l: tau_l/lambda_l + Delta d |w(k)| <= 3 gap/t.  Consequence: with gap <=
  T_lo^2 <= t^2 and |Delta d| M <= K_d t (Lemma badpeaks(a) under (H2''), or Z6_ref U' step (2)): tau_l <= lambda_l(3 +
  K_d)t; (tau_l)_- <= c/(2 m_l) by the bad inequality; dropping costs O(|tau| + lambda(K_d + 2)t) by the claim in the
  proof of Prop. windowcert(c).  OK.

## 2.2 The far pull at a companion (NEW; PROVED)
Setting: design D''' or D^PW (any SLD-type design), I = {1..N}, f in S_{p*} with F finite and forced data
(xi,q_0,a,w,F,z,zhat,e,nu); a carrier l in L_N is SWALLOWED WITH SIGN eps_l if z_s = eps_l for all s in S_l \ F
(exactly swallowed; bad in Def. def:swallowed).  v_l := delta_l h_l/n_l (so u_l = v_l on S_l), s_max(L) :=
max union_{l'' <= L} supp y_{l''}.

**Definition (pulled row).**  For such l, j in S_l \ F and mu > 0 put A := a - eps_l mu e_j^*, a' := A/q^*(A),
z'_j := -eps_l, z'_i := z_i (i != j).  Then supp a' = F u {j} and z' = sgn a' there, |z'| <= 1, so (a',z') is admissible
forced data (Remark rem:lemmaZ(c)); f' is the PULLED ROW.  (Several pulls, banks and changes on F combine in the
obvious way.)

**Lemma P1 (effect and cost of a pull).**  Let L >= l, j in S_l \ F with j > s_max(L), and mu ||U|| <= nu/2.  Then
 (a) zhat' - zhat = -2 eps_l e_j + U(e' - e) with ||e' - e|| <= 2 mu ||U^* e_j^*||/nu;
 (b) eps_l u_l(zhat') - eps_l u_l(zhat) = -2 v_l(j) + rho_l and, for every carrier k != l with k <= L,
     u_k(zhat') - u_k(zhat) = rho_k, where |rho_k| <= 2 mu ||U^*e_j^*||/nu for all k; for a DIAGONAL base
     (U^*e_i^* = s_i k_i), rho_k = <U^*u_k, e>(nu/(nu^2 + mu^2 s_j^2)^{1/2} - 1) - eps_l mu s_j^2 u_k(j)/(nu^2 +
     mu^2 s_j^2)^{1/2}, i.e. rho_k = O(mu^2) for k <= L, k != l;
 (c) c(delta) <= C (v_l(j) + mu) log(e/(v_l(j) + mu)), delta := zhat' - zhat, and p*(f' - f) <= C_f (v_l(j) + mu)
     log(e/(v_l(j) + mu)) once v_l(j) + mu <= c_f (C, c_f, C_f depend only on f, N and the design);
 (d) the room of every S_{l''} computed at f' (off supp a', with z') equals that at f for l'' != l, and z' = eps_l on
     S_l \ supp a': l stays swallowed with sign eps_l; the combinatorial rows of Lemma lem:exactswitch on T(L) are
     unchanged; coarse carriers (index <= L) keep their status when v_l(j) + mu is below their (robust) threshold
     distances.
*Proof.* (a) z' - z = -2 eps_l e_j and e' = U^*A/||U^*A||, ||x/||x|| - y/||y|| || <= 2||x - y||/||y||.
(b) u(zhat') - u(zhat) = -2 eps_l u(j) + <U^*u, e' - e> and ||U^*u|| <= q^*(u) = 1.  By (P1) of Thm thm:SLD and
allowedness (a), u_l(j) = v_l(j) (y_l vanishes on S_l), u_{l''}(j) = 0 for l'' < l and for l'' != l with j notin
supp y_{l''}; for l'' <= L, j > s_max(L) gives y_{l''}(j) = 0.  Diagonal formula: U^*A = U^*a - eps_l mu s_j k_j and
<U^*a, k_j> = s_j a_j = 0, so ||U^*A||^2 = nu^2 + mu^2 s_j^2 and <U^*u_k, e'> = (<U^*u_k,U^*a> - eps_l mu s_j^2
u_k(j))/(nu^2 + mu^2 s_j^2)^{1/2}.
(c) Z3 Lemma 3.1 (its proof uses only zhat' = zhat + delta and the clamp formula at both rows; the base change is
q^*(a' - a) <= 2(1 + ||U||) mu): |u_k(delta)| <= 2|u_k(j)| + 2 mu ||U||/nu.  The carriers with u_k(j) != 0 are l and
carriers l' > l with j in supp y_{l'}; by allowedness (b), 2 c_{l'} <= 2^{-2j} c_l delta_l for each of them, so the sum of
their lambda_{l'} <= c_{l'}/4 is <= 2^{-2j} c_l delta_l/3 <= 2^{-j} v_l(j) (n_l <= 5/4).  Hence
sum_k min(lambda_k, |u_k(delta)|) <= 2 v_l(j) + 2^{-j} v_l(j) + sum_k min(lambda_k, 2 mu||U||/nu) and the last sum is
<= C mu log(e/mu); Delta_m <= sum_k lambda_k |u_k(delta)| <= C(v_l(j) + mu).  Insert in Lemma 3.1.
(d) Rooms and rows: only coordinate j changed, j in S_l, j notin T(L); S_l \ supp a' = (S_l \ F) \ {j} still carries
z' = eps_l.  Status: by (b) and Lemma 3.1 (block scalars move by O(Delta)).  QED

So a pull is a FIRST-ORDER, ONE-SIDED, PER-CARRIER LOWERING channel: amount 2 v_l(j) (discrete, arbitrarily fine as
j -> infinity), cost O(amount x log(1/amount)), no first-order effect on any other coarse carrier.

**Lemma P2 (Lemma U and Theorem E with banked and pulled support).**  Z3 Lemma U and Theorem E hold for f_n -> f with
supp a_n = F u B_n u P_n (B_n: banks = contacts of f with masses of sign z_i; P_n: pulled coordinates, z_n = -z there)
for data that are contact-like on B_n and satisfy t |b(j)| <= |a_n(j)| at every pulled coordinate j in P_n
(t the scale of the data).  PROVED: as for Lemma 2.3, a_min is used only for "no flips on the support"; on P_n,
|r b(j)| <= c_flat t |b(j)| <= |a_n(j)| for |r| <= c_flat t (c_flat <= 1/8).
**Lemma P3 (the transplanted data are admissible at pulls).**  In Prop. T (with Z3_ref fixes) the switching vector is
V' = sum_{l in B'} eps_l tau'_l u_l 1_{F^c} with box rows tau'_l <= 12 lambda_l/t (Z6_ref 3.4(4)); at a pulled
j in S_l \ F with j > s_max(l_*), V'(j) = eps_l tau'_l v_l(j).  Put b^+(j) := chi_j V'(j), b^-(j) := -(1 - chi_j)V'(j)
(any chi_j in [0,1]); then t|b^pm(j)| <= 12 lambda_l v_l(j), so the mass mu_j := 24 lambda_l v_l(j) satisfies Lemma P2
(|a_n(j)| >= mu_j/q^*(A) >= mu_j/2).  PROVED.

## 2.3 Two-sided per-carrier exact tuning for a diagonal base (NEW; PROVED)
**Design addendum (G).**  Each S_l has bounded gaps: consecutive elements differ by at most G_l (e.g. S_l := {2^{l}(2i+1)
: i >= 1}, gaps 2^{l+1}); this is compatible with Def. def:SLD (pairwise disjoint infinite sets) and with D'''/D^PW;
put 2^{G_l} into Design(l).
**Proposition P4.**  Let U be diagonal, f with F finite, L_0 a finite set of carriers each swallowed with a sign eps_l,
L >= max L_0, and x in R^{L_0}.  There are eta_0 > 0 and C (depending on f, L_0, L and the design) such that for
|x| <= eta_0 there is a first row f^# whose support is F, one bank per l in L_0 and one pulled coordinate per l in L_0,
with z^# = z off the pulled coordinates, and
   eps_l u_l(zhat^#) = eps_l u_l(zhat) + x_l EXACTLY (l in L_0),   |u_k(zhat^#) - u_k(zhat)| <= C|x|^2 (k <= L, k notin L_0),
   p*(f^# - f) <= C |x| log(e/|x|).
*Proof.*  Put eta := max(|x|_inf, eta') with eta' > 0 fixed below, j*_l := least element of S_l \ (F u [1, s_max(L)]),
bank positions j'_l := j*_l, pull positions j_l in S_l, j_l > j*_l + G_l, with 2 v_l(j_l) in [2eta, 2^{G_l+1}eta]
(exists for eta small by the gap bound, since v_l(s) = delta_l 2^{-s}/n_l).  Step 1: pull at all j_l with masses
mu_l := 24 lambda_l v_l(j_l) (Lemma P3); by Lemma P1(b) (diagonal case) the values move by -2v_l(j_l) + O(eta^2) on
L_0 and by O(eta^2) elsewhere.  Step 2: banks.  For m in R^{L_0}_{>=0} let A(m) := a_pulled + sum_l m_l eps_l e_{j'_l}
and Psi(m)_l := eps_l u_l(zhat(A(m))) (z fixed).  Psi is smooth near 0 and, since U is diagonal, <U^*u_k, k_{j'_l}> =
s_{j'_l} u_k(j'_l) = 0 for k != l (k <= L) and <U^*a_pulled, k_{j'_l}> = 0, so D Psi(0) = diag(s_{j'_l}^2
v_l(j'_l)/||U^*a_pulled||) =: D_0 (positive diagonal; entries are design quantities times 1/nu) and |D^2 Psi| <= C_2.
The required increments Delta_l := x_l + 2 v_l(j_l) + O(eta^2) lie in [eta/2, 3 * 2^{G_l} eta]; so s^0 = D_0^{-1} Delta
has all entries >= c|Delta| with c depending only on the ratio of the entries of D_0, the G_l and |L_0|; Prop. 2.7
(with (TC) satisfied by these one-sided channels) gives m >= 0 with Psi(m) = target EXACTLY and |m| <= C eta.  Effects
on k notin L_0: second order only (through ||U^*A||), O(eta^2).  Cost: Lemma P1(c) for the pulls and Lemma 2.2 for the
banks: p* <= C eta log(e/eta).  Finally choose eta' := |x| (so eta = |x|).  QED
**Corollary P5 (exact neutralization of tiny rays: the residual (UN+) disappears).**  Single block, diagonal base, D^PW
with the addendum (G) and (G-PW1).  At a clean sub-window w of level l let R_t be the set of extreme rays r (of the
combinatorial cones of level <= l; carriers exactly swallowed strict non-peaks of block m) with rate <= b(w) (tiny,
including exactly neutral ones), and V_r := sum_l r(l) eps_l u_l.  Since the d-weight of a strict non-peak carrier is
q_l = eps_l q_0 u_l(zhat)/sigma_m (threshold lemma: w_m(k) = C zeta(k)/(Phi^2 sigma), zeta(k) = m Phi q_0 u_k(zhat)),
the d-sum of r is D_r = (q_0/sigma_m) V_r(zhat).  Let R be the |R_t| x |L_0| matrix (r(l)), L_0 := union of supports,
and x := -R^+ (V_r(zhat))_{r in R_t} (minimum norm; consistent because (V_r(zhat)) = R (eps_l u_l(zhat))_l).  Then
|x| <= ||R^+|| max_r |V_r(zhat)| <= Design(l) b(w) (||R^+|| over all patterns of level l is a design constant; put it
into Design(l)), and Prop. P4 gives a companion f^# with V_r(zhat^#) = 0, hence D^#_r = 0 EXACTLY for every r in R_t,
whatever the signs of the D_r; every other ray's d-sum moves by <= C Design(l) b(w) << u(w), so robust rays stay robust,
and p*(f^# - f) <= C Design(l) b(w) log(e/b(w)) = o(T_lo(w)^2).  By Lemma 1.8 the d-row Hoffman constant at f^# is
<= Design(l)/u(w): single-block d-rows are design-controlled at clean sub-windows, with no compensator, no rigidity and
NO Conjecture G_ray.
STATUS PRESERVATION (value side; see the caveat below for the block threshold).  The tuning must not push a carrier
across its threshold.  At a clean
sub-window every threshold distance is robust (>= u(w) Phi_l >> |x|: safe in both directions) or tiny.  Tiny-gap q < 0
carriers are not variables of the cone (pinned and dropped, Lemma 2.9: rows tau_l = 0 in the pattern); q = 0 carriers have
gap M.  The only delicate carriers are the set NT of q > 0 strict non-peaks with tiny gap: they must only be LOWERED
(x_l <= 0 moves eps_l u_l(zhat) away from the threshold).  So solve instead
     R x = -(V_r(zhat))_{r in R_t},   x_l <= 0 (l in NT).
This polyhedron is NONEMPTY: x := -v with v_l := eps_l u_l(zhat) satisfies R x = -R v = -V, and x_l = -v_l < 0 on NT
because q_l = eps_l q_0 u_l(zhat)/sigma_m > 0 there.  By Hoffman's theorem (constant depending only on the matrix R and
the selector of NT, not on the right side), its point nearest to 0 satisfies |x| <= H(R, NT) |V| <= Design(l) b(w),
H(R, NT) maximized over the finitely many patterns and subsets of level l being a design constant (put it in Design(l)).
With this x, Prop. P4 applies; the VALUES of all carriers move away from (NT) or stay far from (robust) their
thresholds.  Caveat (found on re-check): the BLOCK threshold itself drifts by O(Delta) (Z3 Lemma 3.1) under every
exactification move (closing rooms, banks, pulls alike), so an NT carrier with gap < C_f Phi Delta could still cross; this
is the status part of the hypothesis (BS) of Z3 Prop. T, needed for every exactification.  So: PROVED as an
exactification step under the status part of (BS) for NT carriers (automatic if NT is empty or the NT gaps exceed
C_f Phi Design b(w)); otherwise a threshold buffer is needed (Y2's donors, outside Y2's aligned corner): SKETCH.
The subsequent transplant + Theorem E at the pulled-banked row is the same assembly that Y4 calls SKETCH, with Lemmas P2,
P3 supplying the support bookkeeping.
**Consequences for Y4's residual list.**  (UN+) is NOT a residual of the companion route: the "unfavourable direction"
of Y4 2.3 exists (pulls).  The same pulls push a tiny-margin swallowing-type peak (P+) below its threshold (lower
eps_l u_l(zhat) by 2v_l(j) > margin + C c(delta)), turning it into a q > 0 strict non-peak, which needs no gap
(inward-only expansion, Z6_ref 6 / Z3 Lemma 5.1): an alternative to Y2's donors that is per carrier (so plausibly also
covers Y2's aligned corner -- SKETCH, not checked against Y2).  They also repair Z3 Lemma 1.4 (closing a room raises a
d-neutral carrier; a pull lowers it back) and Z3_ref 4.4's "|F| - 1 degrees of freedom" in BOTH directions.
**General (non-diagonal) bases.**  Pulls lower per carrier for every base (Lemma P1(b): the z-part is local, the mass
part is O(mu)).  The continuous raising channel is then non-local; Gordan's alternative (if no y >= 0, y != 0 with
A^T y <= 0, then some s >= 0 has A s > 0; for z-signed linearly independent V_i the alternative is excluded by Lemma 2.4)
shows that banks + changes on F can raise any finite family of z-signed functionals simultaneously, but exactness also
needs the raise to fall in the cone reachable after discrete pulls; I did not settle this (SKETCH/OPEN).  Since the base
U is a free choice in Martin's construction (any compact dense-range U gives NA(q) = c_00), the diagonal case suffices
for the density problem for the designed norm.
**Numerics (pull_check.py, finite model, diagonal U, maximal contact).**  Pull at j in S_{l0}: d(u_{l0}(zhat)) =
-2 v(j) to 5 digits for v(j) = 7.5e-2 ... 9.4e-3, other carriers' values change by 0 (machine precision), cost
p*(f' - f) ~ 2 mu + O(v(j)) (ratio cost/v(j) = 0.10 with mu = v(j)/20); private banks raise u_{l0}(zhat) at exactly the
predicted rate s_{j'}^2 v(j')/nu and do not move the others.
