# X2 notes (Round 9): (S2) uniform composition with d-CONSISTENT engineered approximants, and (C_mix) mixed activity classes, F finite

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; notation as there), finite block set I = {1..N}, p = p_N, diagonal base (T_final's
mu-base), design D^{U1'} of U1-ref on U4's T_final, enlarged to D^{X2} by two ladder conditions (D-lev), (W_exp) (6.1).  Labels PROVED /
SKETCH / HEURISTIC / FALSE / OPEN; "PROVED" = complete proof here using only refereed results (listed where used).  This file = X2_head +
X2_part1 ... X2_part6 (byte-identical copies).  Scripts and outputs: r9/X2_work/.
No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN; the F-finite residual is reduced to U1-ref's
status-coherence problem ((KN) failure), which is the X1 task.

## 0. Summary of the answers
(1) (S2a') d-consistent engineered approximants: CLOSED.
    * Proposition J (PROVED): for VALID data (Gamma_w <= 2) the theta/+- junction mismatch kappa^+- = -+(rho/2)(d' - d)(Domega) of
      thm:engineered is <= C_f |Omega_m|^{1/2} (||X|| + t(N'')), uniform in the piece scale t (U1 Lemma 2.1 bounds ||D Domega||_2; the diagonal
      base bounds the mass effects by the mass vector X).  U3-ref F6a's order s_1/t^2 was computed for a datum scaled by 1/t whose Gamma_w grows
      like t^{-2}; but the conclusion stands in a different form: the mismatch is NOT uniform along WINDOWS (||X|| carries the masses of all
      n pieces, |Omega| grows with the level), so with fixed transfer inefficiency the rebalancing fails — an exact cancellation is needed.
    * Lemma DC (PROVED): exact d-consistency (nv'_k = nv_k on the finite switching set Omega, hence d' = d on every switching vector, kappa = 0)
      by levers (TU pulls + banks, zero-data z-moves/banks, absorber tuning masses).  The linearization is I - p q^T (rank one, through the
      block norm) with 1 - q^T p >= 1 - C_m >= 1/2 (Sherman-Morrison), plus a block-triangular absorber coupling; Poincare-Miranda gives an
      exact zero.  Lever sizes O(||X||).  Lemma LV (PROVED): such levers exist at U1's companions (design addition (D-lev)).
    * Lemma UE-1 + Theorem UE (PROVED, line-by-line modification of the refereed proof of thm:engineered and of U3's Lemma VT): uniform
      per-piece bounds p*(f' + tau g'_i) <= 1 + (tau^2/2)(1 - delta) for |tau| <= c_flat t_i, c_flat an f-constant (window-dependent only through
      gamma_B, as in V1), with explicit late threshold s_late (a window quantity); lever sizes are checked against the data at lever coordinates
      (zero data, contact-like data, or pull masses 24 lambda v dominating c_flat t |data|); the scrambled-set bound is explicit
      (S_m <= K_w Pi^2 log(e/Pi) + 4m(C_S (K_w Pi)^2 + s_1^2 T^4), second order in the perturbation size Pi <= K_w s_1).
(2) (S2b) averaging at the norm-attaining approximant: Theorem E^eng (PROVED) — Theorem E's averaging run AT the engineered approximant with
    the per-piece bounds of Theorem UE; no exactness of the averaged data, no final call of cor:D1.
(3) (S2c) threshold comparison: PROVED with the design addition (W_exp) c_{l+1} <= exp(-1/T_lo(l, M(l))); (W10) alone does not suffice for
    the late threshold obtained here (s_late ~ T^{15}: gap_min ~ T^4 enters K_w squared; (W10) gives violations ~ T^{10}).
(4) (C_mix): CLOSED (Lemma CM, Theorem C_mix, PROVED): in a mixed class, complete the fine structure by self-aligning every negative fine
    carrier (state (R): explicit (SC)) and anti-aligning positive ones; the only violations are fine-origin contact violations of mass
    <= 4 C_Delta c_{L+1}, tolerated by Theorem UE; frustration is harmless; no exact completion is needed.
(5) MASTER THEOREM V (F finite, design D^{X2}; PROVED modulo the refereed tools it cites): f in Rec(p_N) whenever, for infinitely many main
    stages L, some clean sub-window has >= n(w)/D_cls(w) scales in activity classes (one-signed OR mixed) satisfying (KN_{w,a}).  Hence the
    F-finite residual is: (C*) rows at which, at all large main stages and all clean sub-windows, almost all scales lie in classes violating
    (KN) — U1-ref's status coherence (OPEN).

## Results table
| # | Result | Label | Where |
|---|---|---|---|
| 1 | Lemma M1 (masses off/on the support, diagonal base) | PROVED | 1.1 |
| 2 | Corollary M1' (mass vector of an engineered approximant) | PROVED | 1.2 |
| 3 | Proposition J (junction mismatch for valid data: O(|Omega|^{1/2} ||X||), uniform in t) | PROVED (upper bound); attainment HEURISTIC | 1.3 |
| 4 | Definition / identities of d-consistency (d' = d on Omega, gap identity (1.1), H' = (C/C')H) | PROVED | 1.4 |
| 5 | Lemma M2 (uniform neighborhoods, transfer data) | PROVED | 1.5 |
| 6 | Lemma DC (exact d-consistency by levers; rank-one linearization; Poincare-Miranda) | PROVED | 2.2 |
| 7 | Lemma LV (levers at U1's companions; design addition (D-lev)) | PROVED | 2.3 |
| 8 | Lemma UE-1 (explicit estimates at the d-consistent approximant) | PROVED | 3.3 |
| 9 | Theorem UE (uniform violation-tolerant engineered bound, T_0 = c_flat t) | PROVED | 3.4-3.5 |
| 10 | Theorem E^eng (averaging at the engineered approximant) | PROVED | 4.1 |
| 11 | (S2c) threshold comparison under (W_exp) ((W10) does not suffice for the s_late obtained here) | PROVED (arithmetic) | 4.2 |
| 12 | Lemma CM (self-aligned completion of mixed classes) | PROVED | 5.1 |
| 13 | Theorem C_mix (mixed classes recovered under (KN)) | PROVED mod refereed tools | 5.2 |
| 14 | Design D^{X2} admissible, N-free, refereed results survive | PROVED (by inspection) | 6.1 |
| 15 | Master Theorem V and its contrapositive (F-finite residual = status coherence) | PROVED mod refereed tools | 6.2 |
| 16 | Precision of U3-ref F6a; U1 Cor. IV.2 superseded; (S1), RT*(c) absorbed | PROVED | 6.2-6.3 |
| 17 | Status coherence without (KN) | OPEN (X1) | 6.2 |
| 18 | Numerics (Prop J scaling, exact tuning, Jacobian I - pq^T, UE bound in a finite model) | sanity checks | 6.4 |

## Dependencies (refereed)
Note: lem:threshold, lem:bookkeeping, lem:base, lem:block, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence, def:engineered,
lem:approxfacts, lem:F1, lem:anchor, def:SC, lem:scrambling, thm:engineered (proof), lem:slack, prop:reduction, prop:continuity, prop:smooth.
Z3 Lemma 3.1 (companion cost), Theorem E (structure of the averaging).  V1: Lemma B, Lemma TU, TR(iii)-(iv), Lemma ST, Lemma CO, Theorem E''
(window-dependent c_flat).  V2: MT III'.  U1: Lemmas 1.1, 1.3, 2.1, 2.4, 3.2, 3.3, 4.1-4.6, Proposition 2.2, 3.4 (with U1-ref's fixes:
Proposition KN, G1 release, (X4), D^{U1'}, Lemma 4.2(ii)).  U3: Lemma VT (U3-ref verified).  U4: T_final, Lemma GW.
# X2 part 1 — Setting, mass bookkeeping with the diagonal base, the true size of the junction mismatch, uniform neighborhoods

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; notation as there), I = {1..N} finite, p = p_N, design T_final / D^{U1'}
(U4, U1-ref Section 6) with the diagonal base U k_s = mu_s e_s, U^* e_s^* = mu_s k_s (mu_s = 2^{-s^2-1}; only "diagonal with positive
entries" is used in this part).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.0 Objects
A ROW is f_0 in S_{p*} with forced data (xi_0, q_0, a, w, F, z, zhat, e, nu) (prop:forced), F := supp a finite, zhat = z + Ue, so
(Ue)_s = mu_s^2 a_s / nu, i.e. zhat_s = z_s for s notin F.  zeta_m := R_m^** zhat, A_m := |zeta_m|_m (= sigma_m/q_0), and for a strict
non-peak k of block m the NORMALIZED VALUE nv_k := zeta_m(k)/A_m = lambda_k u_k(zhat)/A_m; by lem:threshold, nv_k = Phi_k^2 w_m(k)/C_m, and
for omega vanishing on the peak set P_m:  d_m(omega) = <D_m w_m, D_m omega>/C_m = sum_k omega(k) nv_k.                          (1.0)
A PIECE at scale t in (0,1] is a functional g with g(xi_0) = 0 together with two pairs (b^+-, omega^+-) REPRESENTING g at f_0
(def:twopiece: g = b^+- + sum_m R_m^*(omega^+-_m - d_m(omega^+-_m) w_m), omega^+-_m in c_00 supported in Q_m), NOT necessarily
side-admissible; Domega := omega^- - omega^+, Delta_m := d_m(Domega_m), v := b^+ - b^- = sum_m R_m^*(Domega_m - Delta_m w_m),
b^theta := (b^+ + b^-)/2, omega^theta := (omega^+ + omega^-)/2.  Violations viol(j), eps := sum_{j notin F} viol(j) as in U3 Lemma VT.

## 1.1 Lemma M1 (masses off the support, diagonal base).  PROVED.
Let J be a finite set disjoint from F, c in R^J, A := a + sum_{s in J} c_s e_s^*, X := sum_{s in J} c_s mu_s k_s, nu_A := ||U^*A||,
e_A := U^*A/nu_A.  Then X ⊥ U^*a, nu_A = (nu^2 + ||X||^2)^{1/2}, and for every u in l_1:
 (i)   <U^*u, e_A - e> = sum_{s in J} c_s mu_s^2 u(s)/nu_A + (nu/nu_A - 1) <U^*u, e>;
 (ii)  ||e_A - e|| <= ||X||/nu,  |<U^*u, e_A - e>| <= ||U^*u|| ||X||/nu,  and 0 <= nu_A - nu <= ||X||^2/(2nu);
 (iii) if z^A is any sign vector admissible with A (|z^A| <= 1, z^A = sgn A on supp A) and xhat_A := z^A + U e_A, then
       |u(xhat_A) - u(zhat)| <= ||U^*u|| ||X||/nu + sum_s |u(s)| |z^A_s - z_s|   (for s in F, z^A_s = z_s = sgn a_s).
Proof.  U^*a = sum_{s in F} a_s mu_s k_s and X lies in span{k_s : s in J}, J ∩ F = {}: orthogonal.  (i) e_A = (nu e + X)/nu_A and
<U^*u, X> = sum_J c_s mu_s <U^*u, k_s> = sum_J c_s mu_s^2 u(s).  (ii) <e_A, e> = nu/nu_A, so ||e_A - e||^2 = 2(1 - nu/nu_A) =
2(nu_A - nu)/nu_A <= ||X||^2/nu^2 because nu_A - nu = ||X||^2/(nu_A + nu) <= ||X||^2/(2nu); Cauchy-Schwarz.  (iii) xhat_A - zhat =
(z^A - z) + U(e_A - e) and u(U h) = <U^*u, h>.  QED
For a carrier, ||U^*u_k|| <= q*(u_k) = 1.  So every value moves by at most ||X||/nu plus its own sign changes.
(iv) If masses are also put on support coordinates (J ∩ F != {}, same signs), X is no longer orthogonal to U^*a and nu_A - nu is of FIRST
order; the general bound ||e_A - e|| <= 2||U^*(A - a)||/nu (||x/|x| - y/|y||| <= 2|x - y|/|y|) replaces (ii), and a mass c at p in F changes
EVERY value at first order through the term (nu/nu_A - 1)<U^*u, e> = -c mu_p^2 a_p <U^*u, e>/nu^2 + O(c^2): a cross effect of relative size
|a_p|/nu compared with the own effect c mu_p^2 u(p)/nu on a carrier with u(p) != 0.  (PROVED, same computation.)

## 1.2 Corollary M1' (masses of an engineered approximant).  PROVED.
Let pieces i = 1..n at scales t_i >= T > 0 satisfy t_i ||b^+-_i||_1 <= A_0, and let the mass set be W (finite, disjoint from F) with
masses m_s := 4 rho s_1 max_i |b^theta_i(s)| (s in W).  Then ||X|| <= sum_W m_s mu_s <= 4 rho s_1 mu_1 n A_0 / T  (crude bound), and
for s notin F the sharper bound sum_{s notin F} mu_s^2 b(s)^2 <= nu h(b) (h of def:certificate; diagonal base: U^*(b 1_{F^c}) ⊥ span
{k_s : s in F} ∋ e) gives ||X||^2 <= 16 rho^2 s_1^2 nu sum_i h(b^theta_i) <= 16 rho^2 s_1^2 nu n Gamma_max/q_0 when W ∩ F = {}.
Proof.  ||X|| <= sum m_s mu_s and max_i |.| <= sum_i |.|; h is a positive semidefinite quadratic form, so h(b^theta) <= (h(b^+) + h(b^-))/2
<= Gamma_w/q_0.  QED
(Only the crude bound is used below: every requirement on s_1 will be "s_1 small compared with window quantities", and the masses
enter only through ||X||.)

## 1.3 Proposition J (the junction mismatch for VALID data).  PROVED (upper bound); the lower-bound statement is HEURISTIC.
Notation of thm:engineered, at the engineered approximant f' of f_0 built from ONE piece (no re-tuning), late stage.  Suppose the piece
has Gamma_w(b^+-, omega^+-) <= Gamma_max and supp omega^+-_m ⊂ Omega_m ⊂ Q_m.  Then for every block
 (a) ||D_m Domega_m||_2^2 = Delta_m^2 + C_m H_m(Domega_m) <= (4 Gamma_max/sigma_m) (C_m + C_m^3/(M_m^2 Phi_{P_m}^2))   [U1 Lemma 2.1];
 (b) |kappa^+-_m| = (rho/2) |(d'_m - d_m)(Domega_m)|
         <= (rho m/2) ||D_m Domega_m||_2 |Omega_m|^{1/2} max_{k in Omega_m} |u_k(xhat') - u_k(zhat)|/A'_m  +  (rho/2)|Delta_m| |A'_m - A_m|/A'_m;
     consequently |kappa^+-_m| <= C_f |Omega_m|^{1/2} (||X|| + t(N'')), C_f depending only on the block constants of f_0, Gamma_max, rho.
Proof.  (a) D Domega = (Delta/C) D w + y with y ⊥ D w, ||y||^2 = C H (def:certificate); Lemma 2.1 of U1 (re-derived by U1-ref) bounds
Delta^2 <= H C^3/(M^2 Phi_P^2) since Domega is supported in Q; and H(Domega) <= 2H(omega^+) + 2H(omega^-) <= 4 Gamma_max/sigma.
(b) kappa^+- = rho (d' - d)(omega^+- - omega^theta) = -+ (rho/2)(d' - d)(Domega) (proof of thm:engineered, Step 2).  By (1.0) at f_0 and
at f' (Omega carriers stay strict non-peaks at late stages), (d' - d)(Domega) = sum_k Domega(k)(nv'_k - nv_k), and nv'_k - nv_k =
lambda_k (u_k(xhat')/A' - u_k(zhat)/A); split as lambda_k (u_k(xhat') - u_k(zhat))/A' + lambda_k u_k(zhat)(1/A' - 1/A); the second part sums
to Delta (A - A')/A' by (1.0); Cauchy-Schwarz with lambda_k = m Phi_k on the first.  Lemma M1(iii): |u_k(xhat') - u_k(zhat)| <= ||X||/nu + t_k
(the cut-off changes z only beyond N''); |A' - A| <= sum_k lambda_k |u_k(xhat' - zhat)| <= ||X||/nu + t(N'').  QED
Consequence.  The mismatch is uniform in the scale t of the piece (U3-ref's estimate kappa ~ s_1/t^2 used a datum scaled by 1/t, whose
Gamma_w grows like t^{-2}; with Gamma_w <= 2 the 1/t-sized parts of b^theta and Domega are forced onto coordinates/directions where they
cost nothing in Gamma, and (a) shows ||D Domega||_2 = O(1)).  But it is NOT uniform in the WINDOW: |Omega_m| and ||X|| (which carries the
masses of all n pieces of the window) grow with the window, while the rebalancing in Step 4 of thm:engineered absorbs a first-order
level shift kappa only at cost |tau kappa| iota with a FIXED inefficiency iota ~ eta_1 (transfer data of f; eta_1 cannot be made
window-dependent without f-dependent rates: Lemma TV(a) needs |eps| Lambda <= gamma/2 with Lambda = Lambda(eta_1) unbounded).  At |tau| = s_1
the ratio (cost)/(budget delta tau^2) is ~ eta_1 C_f |Omega|^{1/2} ||X||/(delta s_1), unbounded along the windows (HEURISTIC: it is attained
in general; the proof below does not need the lower bound).  Hence an exact cancellation is the robust remedy: d-CONSISTENCY.

## 1.4 Definition (d-consistent approximant).
A first row f' (with forced data primed) is d-CONSISTENT with f_0 on a finite set Omega = union_m Omega_m of strict non-peaks of f_0 if
every k in Omega_m is a strict non-peak of f' and nv'_k = nv_k (equivalently u_k(xhat') = (A'_m/A_m) u_k(zhat)).  Then, by (1.0) at both
rows, d'_m(omega) = d_m(omega) for EVERY omega supported in Omega_m, w'_m(k) = (C'_m/C_m) w_m(k) and
    gap'_m(k) = (C'_m/C_m) gap_m(k) + (1 - C'_m/C_m)          (k in Omega_m),                                                   (1.1)
since gap' = M' - (C'/C)|w| = (1 - C') - (C'/C)(1 - C - gap).  In particular kappa^+- = 0 for every piece supported in Omega and
H'_m(omega) = (C_m/C'_m) H_m(omega) for every such omega (H'(omega) = (||D omega||^2 - d'(omega)^2)/C').  (Elementary; PROVED.)

## 1.5 Lemma M2 (uniform neighborhoods).  PROVED.
Let f in S_{p*} have F finite.  Fix, at f, in every block: gamma_m in (M_m/2, M_m) with |w_m(k)| != gamma_m for all k, and, for a given
eta_1 in (0, 1/4], transfer data (gamma_m, k^vs_{*,m}, Lambda^vs_m) (lem:transferdata), and a peak k^nat_m with alpha_m(k^nat_m) != 0.  Then
there is r_f(eta_1) > 0 such that every f'' in S_{p*} with p*(f'' - f) <= r_f(eta_1) satisfies (double primes = data of f''):
 (a) |C''_m - C_m| <= C_m/8, |sigma''_m - sigma_m| <= sigma_m/8, |q''_0 - q_0| <= q_0/8, |nu'' - nu| <= nu/8, F ⊂ supp a'' and
     |a''_j| >= a_min/2 on F (a_min := min_F |a_j|), and the peak k^nat_m of f is a peak of f'' with the same sign;
 (b) the transfer data persist: k^vs_{*,m} is a peak of f'' with w''_m = M''_m and positive margin, P''_m ⊂ L''_m, e''^vs_{y,m} >= 1/2,
     iota''^vs_m <= 2 eta_1, ||D_m y''^vs_m||_2 <= K_y, |Y''^vs_m|/q''_0 <= K_Y, with K_y, K_Y independent of eta_1 (lem:transferdata(b),(d)).
Proof.  If (a) or (b) failed for every r > 0, there would be f_n -> f violating it; Proposition prop:continuity (a_n -> a in l_1, scalar
data converge, w_{n,m} -> w_m coordinatewise, k^nat a peak with positive margin persists as in the proof of lem:persistence) and Lemma
lem:persistence contradict this for n large.  QED
All constants called "f-constants" below are computed from the data of f and are valid on the ball p*(f'' - f) <= r_f; companions
f_j -> f and their engineered approximants eventually lie in that ball, so these constants are uniform along every window sequence.
# X2 part 2 — Exact d-consistency by levers (Lemma DC) and the availability of levers at U1's companions (Lemma LV)

Setting of part 1.  f_0 is a row (F_0 finite), Omega = union_m Omega_m a finite set of strict non-peaks of f_0, split into
Omega^abs (zero-value absorbers of D^{U1'}: u_a(zhat_0) = 0, block 1) and Omega^0 := Omega \ Omega^abs.  A PRE-ROW f_1 = (A_1, z_1) is
obtained from f_0 by adding finitely many masses of sign z_0 at coordinates off F_0 (or same-sign masses on F_0) and by changing
z_0 only on a set Z_1 (e.g. the cut-off z_1 := 0 beyond N''); all carriers' values move by at most delta_1 := max_k |u_k(xhat_1) -
u_k(zhat_0)| (Lemma M1: delta_1 <= ||X_1||/nu + max_k sum_{s in Z_1} |u_k(s)| |z_1(s) - z_0(s)|).

## 2.1 Levers.  (Definitions.)
For l in Omega with block m = m(l) fix a sign eps_l in {+-1} and one of the following lever types; v_l(s) := u_l(s) for s in S_l.
 (Z-free) a coordinate j in S_l \ F_0 that is FREE at f_1 with room 1 - |z_1(j)| >= rr > 0; for P in R put z(j) := z_1(j) + eps_l P/v_l(j).
 (Z-con)  a coordinate j in S_l \ F_0 that is a contact of f_1 with z_1(j) = eps_l; for P <= 0 put z(j) := eps_l (1 - |P|/v_l(j))
          (inward move), for P > 0 a BANK: mass beta_j P with sign eps_l at j, beta_j := nu_1/(mu_j^2 v_l(j)) (nu_1 := ||U^*A_1||).
 (TU)     a PULL coordinate j_p in S_l, a contact of f_1 with z_1 = eps_l, and a BANK coordinate j' in S_l, j' != j_p, a contact of f_1 with
          z_1 = eps_l (or a support coordinate with sgn A_1(j') = eps_l); the pull is fixed: z(j_p) := -eps_l, mass -eps_l mu_p at j_p with
          mu_p := 24 lambda_l v_l(j_p); for P >= -2 v_l(j_p) a bank of mass beta_{j'} (P + 2 v_l(j_p)) with sign eps_l at j'.
 (S-mass) a support coordinate p in F_0 with u_l(p) != 0; for P in R change A(p) by sgn(A_1(p)) beta_p P, beta_p := nu_1/(mu_p^2 |u_l(p)|),
          and put eps_l := sgn(A_1(p) u_l(p)).
Write P = (P_l)_{l in Omega}, f(P) for the resulting row and Lev_l for the lever coordinates of l.  SEPARATION (SEP):
 (i) the sets Lev_l are pairwise disjoint and disjoint from F_0 except for (S-mass); (ii) Lev_l ∩ supp u_k = {} for all k in Omega^0 \ {l};
 (iii) for a in Omega^abs, Lev_a ∩ supp u_k = {} for all k in Omega \ {a}.  (Absorbers may meet lever coordinates of Omega^0.)

## 2.2 Lemma DC (exact d-consistency).  PROVED.
Put, for l in Omega, F_l(P) := eps_l [ u_l(xhat(P)) - (A_m(P)/A_m^0) u_l(zhat_0) ], where A_m(P) := |R_m xhat(P)|_m, A_m^0 := |R_m^** zhat_0|_m.
Zeros of F are exactly the lever parameters at which f(P) is d-consistent with f_0 on Omega (Definition 1.4; statuses below).
Constants: A_min := min_m A_m^0, K_X := max_{a in Omega^abs} sum_{k in Omega^0} sum_{s in Lev_k} |u_a(s)|/v_k(s), K_J := (1 + K_X)(1 + 4/A_min).
There are r_0 > 0 and C_2 < infinity, depending only on f_0, Omega, the lever data (v_l on Lev_l, mu on Lev_l, rooms, pull ratios
v_l(j_p)/r <= 2^{G}) and the status margins of the carriers of Omega and of the peaks of f_0 (all positive), such that: if
      K_J |F(0)|_inf <= r/2,   K_J C_2 r <= 1/4,   K_J c_tiny <= 1/4,   r <= r_0,   and (TU levers) v_l(j_p) >= r,
where c_tiny := max_{m, k in Omega} sum_{l' notin Omega, l' > L} lambda_{l'} sum_{s in Lev_k} |u_{l'}(s)|/v_k(s) (first-order effect of the
levers on the block norms through carriers outside Omega that meet lever coordinates), then F has a zero P* with |P*|_inf <= r.  At f(P*):
every l in Omega is a strict non-peak with nv_l(P*) = nv_l^0 (exact d-consistency), the peaks of f_0 of every block remain peaks with the
same signs, every carrier value moves by at most delta_1 + C_lev r (C_lev := max over carriers k of sum_{s in Lev} |u_k(s)| (|dz_s| + mass
effect) per unit r, a constant of the lever data), the total off-F_0 mass vector satisfies ||X_lev|| <= C_2 r, and the data moved are
only: z on the Z-type and pull coordinates, masses on banks/pulls/S-mass coordinates.
Proof.  (1) Continuity.  For |P|_inf <= r_0 the row f(P) has admissible forced data (bank masses >= 0 have the sign of z; inward z-moves
keep |z| <= 1; (TU) needs P >= -2 v_l(j_p), true for |P| <= r <= v_l(j_p); (S-mass) keeps the sign of A_1(p) for r_0 small; (Z-free) keeps
|z(j)| < 1 for r_0 <= rr min v_l(j)).  Its forced data depend continuously on P (finitely many coordinates move; prop:forced, prop:continuity
applied to the explicit formulas: e(P) = U^*A(P)/||U^*A(P)||, xhat(P) = z(P) + U e(P), A_m(P) = |R_m xhat(P)|_m).
(2) First-order structure.  By construction of the levers and Lemma M1(i) with base A_1: eps_l (u_l(xhat(P)) - u_l(xhat_1)) = P_l + E_l(P), where
E_l collects (a) Hilbert terms: changing masses changes e by Lemma M1(i)-(ii); the first-order part of a mass at its own coordinate s in
Lev_l is exactly the normalized slope (beta_s mu_s^2 v_l(s)/nu_1 = 1) up to the factor nu_1/nu(P) - 1 = O(||X_lev||^2), and the
cross part (nu/nu_A - 1)<U^*u, e> is O(||X_lev||^2); for other masses <U^*u_l, X> vanishes at first order unless the mass coordinate lies in
supp u_l, excluded by (SEP)(ii) for l in Omega^0; (b) for a in Omega^abs, the first-order effects of the Z/TU levers of Omega^0 at
coordinates of supp u_a: sum_k X_{ak} P_k with |X_{ak}| <= sum_{s in Lev_k} |u_a(s)|/v_k(s).  Hence |E_l(P) - sum_k X_{lk} P_k| <= C_2' |P|^2
(X_{lk} := 0 unless l is an absorber).  Next, A_m is a norm with norming functional w_m(P) at R_m xhat(P), so with dxhat := xhat(P) - xhat_1,
0 <= A_m(P) - A_m(1) - <w_m(1), R_m dxhat> <= <w_m(P) - w_m(1), R_m dxhat>; the clamp formula (proof of lem:F1) gives |w_m(P)(k) - w_m(1)(k)|
<= K_cl |dxhat-value at k| for every carrier k of block m whose status does not change, with K_cl depending on 1/Phi_k^2 and the threshold
constants; carriers outside Omega ∪ peaks contribute only through c_tiny and second order.  And <w_m(1), R_m dxhat> = sum_{k in Omega_m}
lambda_k w_m(1)(k) eps_k (P_k + E_k) + (contributions of carriers outside Omega meeting lever coordinates, <= c_tiny |P|_inf A_m^0) +
O(|P|^2).  Finally w_m(1)(k) = w_m^0(k) + O(delta_1/Phi_k^2) and u_l(xhat_1) - u_l(zhat_0) = O(delta_1).
(3) The linearization.  Order the variables (Omega^0, Omega^abs).  With p_l := eps_l u_l(zhat_0)/A_m^0 and q_k := eps_k lambda_k w_m^0(k)
(k, l in Omega_m ∩ Omega^0; p, q := 0 on absorbers, whose values and w vanish), F(P) = F(0) + J P + R(P) with
      J = [[ I - p q^T , 0 ], [ X , I ]]     (p q^T blockwise, i.e. only within each block),
and |R(P)|_inf <= C_2 |P|_inf^2 + c_tiny |P|_inf + C delta_1 |P|_inf on |P|_inf <= r_0 (the last term from replacing data at f_1 by data at f_0;
absorbed into C_2 r once delta_1 <= r).  Now q^T p = sum_{k in Omega_m} w_m^0(k) nv_k^0 = sum_{Omega_m} Phi_k^2 w(k)^2/C_m <= C_m <= 1/2 by
(1.0) and ||D_m w_m||_2 = C_m < 1/2, so by Sherman-Morrison (I - p q^T)^{-1} = I + p q^T/(1 - q^T p) has inf-norm <= 1 + 2||p||_inf ||q||_1
<= 1 + 4/A_min (|u_l(zhat_0)| <= ||zhat_0||_inf <= 2, ||q||_1 <= sum_k lambda_k <= 1).  The block-triangular J has
J^{-1} = [[ (I - pq^T)^{-1}, 0 ], [ -X (I - pq^T)^{-1}, I ]], ||J^{-1}||_inf <= K_J.
(3') Lever masses placed at coordinates s that are ALREADY in supp A_1 ((S-mass) levers; (TU) banks at window contacts that carry a
theta-mass; (Z-con) banks at such contacts) act, by Lemma M1(iv), at first order on every value through the nu-change, with coefficients
Y_{k,l} = -sgn(A_1(s)) beta_s mu_s^2 A_1(s) eps_k <U^*u_k, e_1>/nu_1^2, i.e. |Y_{k,l}| <= |A_1(s)|/(nu_1 v_l(s)) (resp. |A_1(p)|/(nu_1 |u_l(p)|)).
Hence the true linearization is J + Y; if K_J ||Y||_inf <= 1/2 (hypothesis added to the lemma), then ||(J + Y)^{-1}||_inf <= 2 K_J and the
argument below runs with 2K_J in place of K_J.  (At U1's companions: for absorbers |A_1(p_0)| = m_0(a) <= theta_a + c_p^2, theta_a = C_f lambda_a T_hi,
|u_a(p_0)| >= 1/(8 n_a), so their contribution is <= C sum_a m_0(a)/nu <= C_f c_{L+1}; for banks at window contacts |A_1(s)| is a theta-mass
4 rho s_1 max_i |b^theta_i(s)| <= 4 rho s_1 A_0/T, so ||Y||_inf <= C_f c_{L+1} + Design(L) s_1 A_0/T: negligible under (LATE).)
(4) Poincare-Miranda.  G(P) := J^{-1} F(P) = J^{-1} F(0) + P + J^{-1} R(P) is continuous on the cube Q_r := [-r, r]^Omega.  On the face P_l = r,
G_l(P) >= r - K_J |F(0)|_inf - K_J (C_2 r^2 + c_tiny r) >= r - r/2 - r/4 - r/4 >= 0, and symmetrically G_l <= 0 on P_l = -r.  By the
Poincare-Miranda theorem G has a zero P* in Q_r; J^{-1} is invertible, so F(P*) = 0.
(5) Statuses and sizes.  r_0 is chosen below the relative margins/gaps of the peaks and Omega carriers of f_0 (divided by the Lipschitz
constant of the values, which is C_lev), so no status changes; at a zero of F, eps_l u_l(xhat) = eps_l (A_m/A_m^0) u_l(zhat_0) means
nv_l(P*) = nv_l^0, and (1.1) gives gap(P*) >= gap^0/2 once |C(P*) - C^0| <= gap^0_min/4.  Masses of the levers are <= beta (r + 2 v(j_p)) <=
beta 2^{G+2} r and z-moves <= r/v: ||X_lev|| <= C_2 r after enlarging C_2.  QED
Remark.  The rank-one structure is exact: a lever acting on one value changes the block norm, hence ALL normalized values of that block;
the factor 1/(1 - q^T p) >= 1 - C_m >= 1/2 is the reason no second, kappa-neutral lever is needed here (compare U1-ref's Lemma R-kt, which
concerns the different problem of holding ratios while moving statuses).

## 2.3 Lemma LV (levers exist at U1's companions).  PROVED (from U1's refereed structure: Lemma 3.2, Lemma 3.3, Proposition 3.4, Lemma 4.1,
## Lemma 4.2, Section 5 of U1-ref (release G1), and V1 Lemma ST / Proposition TR).
Let f^# be the companion of a clean sub-window w of a main stage L of D^{U1'} (U1 part 4 with U1-ref's fixes) carrying, for every scale t of
a (class, cube) set S, data Domega(t) supported in Omega = (coarse strict non-peaks of f^#) ∪ (tuned absorbers), and let s_max := s_max(L),
s_far := s_far(w).  Then every l in Omega has a lever satisfying (SEP), with lever data that are design quantities of level L:
 Lever coordinate j(l) := the least element of S_l ∩ (s_max, infinity) \ F^# (the first or the second element: inside (s_max, sigma_2(L)]
 the companion's support meets S_l at most in the first element, a donor/tuning bank of V1 (C3)/(C4) or of U1 Prop. KN; V1's and U1's pulls
 sit where v_l <= 2^{G} Design b, far beyond).  DESIGN ADDITION (D-lev), a ladder condition computable at stage L and N-free:
 Design(L) >= max_{l <= L} 2^{sigma_2(L)}/(mu_{sigma_2(L)}^2 delta_l), sigma_2(L) := max_{l <= L} (second element of S_l beyond s_max(L));
 then mu_{j(l)}^2 v_l(j(l)) >= Design(L)^{-1} for all l <= L (efficiency of every lever below).
 (a) ACTIVE class-G carriers (gamma_l != 0 in the class): type (TU) with eps_l := sgn of the switching coefficient, bank coordinate j' := j(l)
     (a contact with z^# = eps_l and contact-like data V_t(j') = gamma_l(t) v_l(j') of sign eps_l; it is met by its first absorber pair,
     a first-order cross effect recorded in X), pull coordinates among the far coordinates of S_l (contacts of f^# with z = eps_l: they
     are owned by l, U1 Lemmas 4.1-4.2 / owners of type (a) in mixed classes, Lemma 5.1); bounded gaps of S_l give, for every r <= r_0, a pull
     coordinate with v_l(j_p) in [r, 2^{G(L)} r];
 (b) INACTIVE class-G carriers (gamma_l = 0) and class-G carriers that are strict non-peaks of value tuned to 0 ((K3)): type (Z-con) at
     j := j(l) in S_l ∩ (s_max, s_far] \ F^#; there z^# = eps_l (closed by V1's (C1)) and the exact data vanish for every scale:
     V_t(j) = L(Delta'', gamma(t))(j) = gamma_l v_l(j) = 0 (Proposition 3.4(b) of U1: exact equality on E_c; only l lives on S_l ∩ (s_max,
     infinity) among coarse carriers, allowedness (a), (c)), hence b^+-_t(j) = chi V_t(j) = 0;
 (c) class-R carriers (robust aggregate room on S^nat): at j := j(l) in S_l ∩ (s_max, s_far] \ F^# the data vanish, V_t(j) = gamma_l v_l(j) = 0
     (gamma_l = 0 for class R, U1 (X2)), whatever z^#(j) is (free or contact).  Use the ZERO-DATA lever (Z-gen): for P in R move
     z(j) := clamp_{[-1,1]}(z^#(j) + eps_l P/v_l(j)) and put the overflow into a bank at j with the sign of the contact reached
     (mass beta_j x overflow in value units).  This is continuous, has first-order slope 1 on both sides, and every state of j is admissible
     because the data at j vanish ((Z-free) and (Z-con) are the special cases of a free coordinate with large room and of a contact);
 (d) tuned absorbers a: type (S-mass) at their continuous tuning coordinate p_0 (support coordinate of f^#, mass m_0 in
     [theta_a, theta_a + c_p^2], U1 Lemma 3.3), with eps_a := sgn(m_0 u_a(p_0)); the data satisfy t|b_t(p_0)| <= m_0 (U1 Prop. 3.4(d)).
(SEP) holds: (i) the coordinates of (a)-(c) lie in the private signature sets S_l, those of (d) are fresh odd coordinates; (ii) beyond s_max no
coarse target meets S_l (allowedness (c): supp y_k ∩ S_l ⊂ [1, k] ⊂ [1, s_max] for coarse k), so a lever coordinate of l lies in no supp u_k,
k in Omega^0 \ {l}; (iii) p_0 lies in no earlier target and in no signature set; later carriers meeting p_0 are fine (not in Omega).  The
only first-order cross effects are those of (b), (c) on the first absorber pair P(j) of each lever coordinate j in (s_max, s_far] (U1
Lemma 3.2), i.e. exactly the matrix X of Lemma DC; an absorber's vector meets at most one lever coordinate (its own target coordinate s;
the other coordinates of its target are fresh), so K_X <= max_l 1/v_l(j(l)) <= Design(L) by (D-lev).
Proof.  Read off from the cited statements; the only new observation is the zero-data property in (b), (c), which is the exactness of the
coarse system on E_c (Proposition 3.4(b) of U1: V(s) = L(Delta'', gamma)(s) for s in E_c \ F^#) combined with gamma_l = 0, and the
representation b^+ = beta + chi V 1_{K} (U1 Proposition 2.2(e) / Lemma 1.1(c): beta is supported in F^#).  For (a): in configuration (i) the
far part of S_l is owned by l (owner-candidate of type (a), Lemma 4.1) with z = sgn(gamma_l v_l) = eps_l; in configuration (ii) and in mixed
classes the fixed owners of types (a)-(c) keep their owned sets (Lemma 4.4 / 5.1 with Lemma 4.2's dominance, whose estimates do not use signs);
the G1 release (U1-ref Section 5) concerns only NON-owner carriers.  QED
Consequence.  At U1's companions Lemma DC applies with lever data of level L: r_0, C_2, C_lev, K_J are (f-constant) x Design(L)^{C}, and
c_tiny <= Design(L)^C c_{L+1} (fine carriers meeting lever coordinates have total weight <= 2 c_{L+1}).
Numerics (X2_work/dcons_check.py, dcons_check2.py; N = 1 model with exact forced data via the threshold equation): for VALID exact data
(Gamma^+ = 0.0066, Gamma^- = 0.031) the untuned mismatch kappa is proportional to ||X|| (kappa/||X|| = 0.0230 constant over s_1 in
[1e-5, 1e-2]); one (TU) lever (pull with v(j_p) in [2 du, 2^G 2 du] plus a bank, brentq on the bank mass) restores nv exactly
(residual <= 2e-17) and kappa_tuned <= 3e-17; the bank mass is 15-26 times ||X|| (the factor varies with the discrete pull coordinate).
# X2 part 3a — (S2a') Uniform per-piece engineered bounds at a d-consistent engineered approximant: statement, construction, estimates

Setting of parts 1-2.  Throughout, f in S_{p*} (F finite) is the TARGET row, rho in (0,1), eta_0 in (0,2] with rho^2 (1 + eta_0) <=
(1 + rho^2)/2, A_0, A_2 >= 1, gamma_B in (0,1]; delta := (1 - rho^2(1 + eta_0/2))/2 >= (1 - rho^2)/8 > 0, so rho^2 kappa <= 1 - 2 delta for every
kappa <= 1 + eta_0/2.  "f-constant" = a number depending only on (f, N, rho, eta_0, A_0, A_2, gamma_B); by Lemma M2 all f-constants are
valid at every row in the ball B_f := {f'' : p*(f'' - f) <= r_f(eta_1)}.

## 3.1 Data at a base row (hypotheses (U1)-(U7)).
A BASE ROW is f_0 in S_{p*} with p*(f_0 - f) <= r_f/2, F_0 = supp a_0 finite, F ⊂ F_0, E := F_0 \ F.  A WINDOW FAMILY at f_0 consists of
pieces i = 1..n at scales t_i in [T, t_1] (t_1 an f-constant fixed in 3.4) with pairs (b^+-_i, omega^+-_i) representing g_i at f_0
(g_i(xi_0) = 0), all pieces sharing a finite set Omega = union_m Omega_m of strict non-peaks of f_0, such that:
 (U1) t_i ||b^+-_i||_1 <= A_0 and Gamma^{(0)}_w(b^+-_i, omega^+-_i) <= 1 + eta_0/2;
 (U2) supp omega^+-_{i,m} ⊂ Omega_m, and every k in supp omega_{i,m} is of kind [1] (gap^0(k) >= t_i^2, |omega_i(k)| <= 2 gap^0(k)/t_i),
      [2] (gap^0(k) >= gamma_B, |omega_i(k)| <= A_2/t_i) or [3] (|omega_i(k)| <= A_2/t_i and inward-signed: vs_k omega^+_i(k) <= 1.5 gap^0(k)/t_i,
      vs_k omega^-_i(k) >= -1.5 gap^0(k)/t_i, vs_k := sgn w^0_m(k)), as in V1 Proposition TR(iii);
 (U3) on E: at every j in E the data are contact-like (z_0(j) b^+_i(j) >= 0 >= z_0(j) b^-_i(j)) or t_i |b^+-_i(j)| <= |a_0(j)|;
 (U4) violations: (H3) of Lemma VT (b^theta_i(j) = 0 at violated free coordinates j <= N_w), total violation mass eps_i <= eps;
 (U5) explicit scrambling for the negative blocks I_- := {m : Delta_{i,m} < 0 for some i}: Scr^{(0)}_m(x) <= C_S x^2 for 0 < x <= x_0;
 (U6) Omega carries levers with (SEP) at f_0 (Lemma DC constants r_0, C_2, K_J, C_lev, c_tiny), and the first-order cross effects of
      lever coordinates on carriers outside Omega have total weight W_lev := sum_{k notin Omega, Lev ∩ supp u_k != {}} lambda_k (|dz|-
      weighted, per unit r) — fine carriers only;
 (U7) |Delta_{i,m}| <= C_Delta (an f-constant: U1 Lemma 2.1 gives C_Delta^2 = 8 max_m C_m^3/(sigma_m M_m^2 Phi_{P_m}^2) up to the factor 2
      between f_0 and f, since Gamma <= 2).
Window quantities: n, T, the lever constants, x_0, C_S, gap_min := min_{k in Omega} gap^0(k), and c_fine := sum over carriers that are
fine (not in Omega, not peaks of f_0 with margin >= x_0) of lambda_k.

## 3.2 Construction of the d-consistent engineered approximant f' = f'(N_w, s_1, N'').
 (i)   N_w >= max F_0 with tail_W := max_i (||b^+-_i 1_{(N_w, inf)}||_1 + ||v_i 1_{(N_w, inf)}||_1) <= T^3;
 (ii)  s_1 in (0, 1]; MASS SET W := {j in [1, N_w] \ F_0 : j a contact of f_0, max_i |b^theta_i(j)| > 0} ∪ {j in E : the data are contact-like
       at j}; masses m_j := 4 rho s_1 max_i |b^theta_i(j)| with sign z_0(j) (added to a_0(j) on E);
 (iii) Pi_X := ||X||/nu_0 with X the mass vector (Lemma M1); r := 4 K_J (Pi_X + T^4 s_1) (radius of the levers); pull coordinates of the (TU)
       levers with v_l(j_p) in [r, 2^{G} r];
 (iv)  N'' > N_w larger than every lever coordinate, with t(N'') := sum_{m,k} lambda_k ||u_k 1_{(N'', inf)}||_1 <= T^4 s_1^2,
       sum_m sum_k Phi_k 1[t_k > s_1 T^4] <= s_1^2 T^4 (cf. (N2)), and rho V_{>N''} <= delta s_1/64 for every piece;
       (A (TU) pull coordinate inside the window that carries a theta-mass gets the total mass -eps_l(mu_p + m_j), i.e. the theta-mass takes the
       sign of z'_j = -eps_l; this only enlarges |a'_j| and is part of the fixed pull configuration of Lemma DC.)
 (v)   the pre-row f_1 := (a_0 + masses, z_0 1_{[1,N'']}) and the lever parameters P* of Lemma DC at f_1 (its hypotheses are checked in 3.3);
       f' := nabla p(x'), x' := xhat'/p(xhat'), xhat' := z' + U e', where (a', z') are the forced data of f(P*) normalized
       (a' := A(P*)/q*(A(P*)); z' = z_0 on [1, N''] except at lever coordinates, z' = 0 beyond N'').
 (vi)  For each piece: g''_i := b^theta_i 1_{[1,N_w]} + sum_m R_m^*(omega^theta_{i,m} - d'_m(omega^theta_{i,m}) w'_m), c_i := g''_i(xhat'),
       g'_i := rho (g''_i - c_i a').
f' is norm attaining (z' in c_00, a' in c_00, Proposition prop:smooth(c)), and d-consistent with f_0 on Omega (Lemma DC).

## 3.3 Lemma UE-1 (explicit estimates at f').  PROVED.
Put Pi := Pi_X + r + t(N'')^{1/2} (the PERTURBATION SIZE).  There is a window constant K_w (a polynomial in n, A_0/T, 1/gap_min, 1/x_0,
C_S, the lever constants and f-constants) such that, if Pi <= 1/K_w, then:
 (a) [sizes] Pi_X <= 4 rho mu_1 n A_0 s_1/(T nu_0); r <= 8 K_J Pi_X; the masses and lever moves satisfy q*(a'' - a_0) + q*(A(P*) - a'') <=
     K_w s_1; p*(f' - f_0) <= K_w (s_1 log(1/s_1) + tail(N_w-independent)) — precisely p*(f' - f_0) <= K_w Pi log(e/Pi);
 (b) [values] every carrier k with Lev ∩ supp u_k = {} has |u_k(xhat') - u_k(zhat_0)| <= Pi_X + C_2 r + t_k(N''); Omega carriers satisfy
     nv'_k = nv^0_k exactly; carriers meeting lever coordinates (fine, total weight <= W_lev r) move by <= C_lev r;
 (c) [block data] |C'_m - C^0_m| + |M'_m - M^0_m| + |A'_m - A^0_m| + |c' - q^0_0| + |nu' - nu_0| + ||e' - e_0|| <= K_w Pi; every peak of f_0 with margin
     > K_w Pi stays a peak with the same sign; every k in Omega has gap'(k) >= gap^0(k)/2; d'_m(omega) = d_m(omega) and
     H'_m(omega) = (C^0_m/C'_m) H_m(omega) for omega supported in Omega_m (Definition 1.4);
 (d) [Bregman] 0 <= Bx_m := <w'_m - w^0_m, R_m xhat'> <= K_w Pi^2 + 4 Pi_X c_fine + 4 C_lev r W_lev r + 2 t(N'');
 (e) [scrambling, m in I_-] the quantity S_m := ||D_m(w'_m - w^0_m)||_2^2 + sum_{k in A_m} (Phi_k^2 + lambda_k(|w'_m(k) - w^0_m(k)| + (C'_m - C^0_m)_+))
     of lem:scrambling (A_m the scrambled set of lem:anchor for (w^0_m, w'_m)) satisfies S_m <= K_w Pi^2 log(e/Pi) + 4m (C_S (K_w Pi)^2 + s_1^2 T^4);
 (f) [base form] for every piece and diamond in {+, -, theta}, with beta^theta := b^theta 1_{[1,N_w]}, beta^+- := b^+- 1_{[1,N_w]} +- (1/2) v 1_{(N_w,inf)}:
     |c' h'(beta^diamond) - q^0_0 h^0(b^diamond)| <= K_w (Pi/T^2 + tail_W/T), where h'(beta) := ||P'^perp U^* beta||^2/nu';
 (g) [targets] |c_i| <= K_w (Pi + tail_W)/t_i and p*(g'_i - rho g_i) <= K_w (Pi + c_fine + tail_W)/t_i.
Proof.  (a) Corollary M1' (crude bound) with t_i >= T and ||b^theta_i||_1 <= A_0/t_i; Lemma DC: |P*| <= r and lever masses <= beta 2^{G+2} r with
beta = nu/(mu_j^2 v_l(j)) a lever constant; z-moves <= r/v.  For p*(f' - f_0): Z3 Lemma 3.1 (companion cost, refereed: p*(f'' - f_0) <=
q*(a'' - a_0) + C_f c(delta), c(delta) = sum_m [Delta_m log(e/Delta_m) + sum_k min(lambda_k, |u_k(delta)|)]) with delta := xhat' - zhat_0, whose
carrier values are bounded by (b); the cut-off contributes t(N'').  (b) Lemma M1(iii) (base f_0, masses and lever masses J := W ∪ Lev,
||X_tot|| <= ||X|| + C_2 r) and Lemma DC.  (c) |A'_m - A^0_m| <= sum_k lambda_k |u_k(xhat') - u_k(zhat_0)| (norm Lipschitz, sum lambda <= 1);
the threshold equation of Y1 Lemma T (theta, A solve (E1), (E2) of U1 Lemma 1.2, a nonsingular system at f_0 with Jacobian bounded below by
Phi_P^2 >= Phi_{k^nat}^2) gives |C' - C| <= K_w max-change, exactly as in the proof of lem:F1 (strict monotonicity of F(c; v) through the fixed
peak k^nat_m of Lemma M2, Lipschitz bound sum_k Phi_k |v'_k - v_k|); q_0 = 1/(1 + sum_m A_m); nu', e': Lemma M1(ii) with q*-normalization.
Peaks: the margin is a Lipschitz function of the value and of theta (lem:threshold).  Omega: (1.1) and |C' - C| <= gap_min/4 for Pi <= 1/K_w.
(d) (E5) of lem:approxfacts: 0 <= Bx_m <= <w'_m - w^0_m, R_m(xhat' - zhat_0)> = sum_k lambda_k (w'_m(k) - w^0_m(k)) u_k(xhat' - zhat_0).  Coarse
carriers (peaks of f_0 with margin > K_w Pi, and Omega): |w' - w^0| <= |C' - C| (peaks: |M' - M|; Omega: (C'/C - 1)|w^0|) <= K_w Pi, values
<= Pi: total <= K_w Pi^2.  Remaining carriers: |w' - w^0| <= 2; those not meeting lever coordinates contribute <= 2 sum lambda_k (Pi_X + t_k)
<= 2 Pi_X c_fine + 2 t(N''); those meeting lever coordinates <= 2 C_lev r * (their weight) <= 2 C_lev W_lev r^2.  (e) Proof of lem:scrambling
read with the perturbation size Pi in place of s_1: by (b), (c), a peak of f_0 with margin > K_* Pi (K_* := K_w) is in S_1, a strict non-peak
with Phi gap and gap > K_* Pi is in S_2 (the margin/gap arguments of lem:scrambling use only |u_k(xhat') - u_k(zhat_0)|, |theta' - theta|,
|C' - C| and lem:F1-type Lipschitz bounds, all <= K_w Pi here); so A_m ∩ {t_k <= Pi} ⊂ {mu_k <= 2K_*Pi or Phi gap <= 2K_*Pi or gap <= 2K_*Pi},
whose Phi-mass is <= Scr^{(0)}_m(2 K_* Pi) <= C_S (2K_*Pi)^2 by (U5) (2K_*Pi <= x_0); {t_k > s_1 T^4} has Phi-mass <= s_1^2 T^4 by (iv); with
|w' - w| <= 2, (C'-C)_+ <= 1, Phi <= 1, lambda = m Phi, the sum over A_m is <= 4m(...).  ||D(w' - w^0)||^2 <= K_w Pi^2 log(e/Pi): the last
display of the proof of lem:F1 with K_F s_1 replaced by K_w Pi (Phi_k |w'(k) - w(k)| <= K_w(Pi + t_k) from the clamp formula).  (f) Three
changes: (1) beta^diamond - b^diamond has l_1-norm <= tail_W, and |h(y) - h(y')| <= ||U||^2 (||y||_1 + ||y'||_1)||y - y'||_1/nu with ||b||_1 <=
A_0/T; (2) ||P'^perp y||^2 - ||P^perp y||^2 = <y, e>^2 - <y, e'>^2, of modulus <= 2 ||y||^2 ||e' - e|| <= 2 ||U||^2 (2A_0/T)^2 K_w Pi;
(3) |c'/nu' - q_0/nu_0| <= K_w Pi.  (g) c_i = (g''_i - g_i)(xhat') + g_i(xhat' - zhat_0) (g_i(zhat_0) = 0 since g_i(xi_0) = 0);
g''_i - g_i = -b^theta_i 1_{(N_w,inf)} + sum_m d^theta_{i,m} R_m^*(w^0_m - w'_m) by d-consistency (d'(omega^theta) = d(omega^theta)), with
|d^theta_{i,m}| <= ||D_m omega^theta||_2 <= A_2 ||Phi_m||_2/t_i ... <= K_w/t_i and ||R_m^*(w^0 - w')||_1 <= sum_k lambda_k |w^0(k) - w'(k)| <= K_w Pi + 2 c_fine;
|g_i(xhat' - zhat_0)| <= |<U^* g_i, e' - e_0>| + sum_{lever, cut-off} |g_i(j)| |z' - z_0|(j) <= ||g_i||_1 (K_w Pi) with ||g_i||_1 <= K_w/t_i; and
p*(.) <= (1 + ||U||) ||.||_1.  QED
# X2 part 3b — Theorem UE (uniform engineered bound, violation tolerant, d-consistent) and its proof

## 3.4 Theorem UE.  PROVED (a line-by-line modification of the refereed proof of thm:engineered and of U3's Lemma VT, with the
## estimates of Lemma UE-1 replacing every "late stage" statement).
There are f-constants t_1 in (0,1], c^f_flat in (0, 1/8], K_sharp >= 1, eta_1 in (0, 1/4], c_late > 0 and the radius r_f := r_f(eta_1) of
Lemma M2 with the following property; put c_flat := min(c^f_flat, gamma_B/(8 rho A_2)) (an f-constant when gamma_B is fixed; >= c_f u(w) for
V1's gamma_B(w)).  Let f_0 be a base row with p*(f_0 - f) <= r_f/2 and let a window family (U1)-(U7) be given at f_0 with scales in [T, t_1].
Suppose the WINDOW CONDITIONS
   (W-a) c_fine <= c_late delta T/(n A_0),      (W-b) K_J c_tiny <= 1/4 and 2 K_J ||Y||_inf <= 1/2 (Lemma DC (3'); the s_1-dependent part of
         ||Y||_inf, <= Design-type x s_1 A_0/T, is covered by (LATE) after enlarging K_w),      (W-c) N_w is chosen with tail_W <= c_late delta T/A_0,
and let s_1 satisfy
   (VT')  64 rho eps <= delta s_1        and        (LATE)  s_1 <= s_late := c_late delta min{ T^3 gap_min/(n A_0 K_w)^2 , x_0 T/(n A_0 K_w) }.
Then the d-consistent engineered approximant f' of 3.2 (any N'' as in 3.2(iv)) is norm attaining, p*(f' - f_0) <= K_w Pi log(e/Pi) with
Pi <= K_w s_1, and for every piece i
   p*(f' + tau g'_i) <= 1 + (tau^2/2)(1 - delta)        for 0 < |tau| <= c_flat t_i,                                       (UE)
   p*(g'_i - rho g_i) <= K_w (K_w s_1 + c_fine + tail_W)/t_i.
(K_w is the window constant of Lemma UE-1; c_late is an f-constant; the conditions (W-a)-(W-c) do not involve s_1.)

## 3.5 Proof.
Step 0' (constants; order of choices f -> K_sharp -> eta_1 -> transfer data, r_f -> t_1, c_flat, c_late -> window -> N_w -> s_1 -> N'' ->
levers).  By (U1) and Lemma M2 every Gamma-quantity is <= 2: h^0(b^diamond) <= 2/q^0_0 <= 4/q_0, H_m(omega^diamond) <= 2/sigma^0_m <= 4/sigma_m.
Put K_sharp := 4 max(1/q_0, max_m 1/sigma_m) (1 + eta_0) + 2 and eta_1 := min(1/4, delta/(192 |I| K_sharp)); choose the transfer data of f in
every block with this eta_1 (lem:transferdata, gamma_m in (M_m/2, M_m)) and r_f := r_f(eta_1) (Lemma M2): at every row in B_f they have
e_y >= 1/2, iota <= 2 eta_1, ||D y|| <= K_y, |Y|/q_0 <= K_Y.  Let a_min := min_F |a_j|, gamma_0 := min_m (M_m - gamma_m), C_min := min_m C_m.
c_flat is the largest number <= 1/8 satisfying the following finitely many inequalities, in which every constant is an f-constant
(K_W := C_W (A_0 + A_2 + C_Delta), C_W an f-constant bounding the f'-block sizes per unit 1/t, see Step 3; K_A := 2(1 + ||U||) A_0 + 1):
 (c1) rho c_flat A_0 <= a_min/32          [no flip on F: |tau rho beta_j| <= rho c_flat t ||b||_inf <= a_min/32 <= |a'_j|/8];
 (c2) rho c_flat <= 1/8                    [no flip on E under (U3): |tau rho b_j| <= |a_0(j)|/8 <= |a'_j|/4];
 (c3) rho c_flat (A_2 + C_Delta + 1) <= 8  [no flip at pull coordinates, Step 3 (Base)];
 (c4) rho c_flat (A_2 + 2) <= min(M_min/2, 1/3), rho c_flat ||Phi||_2 A_2 /C_min <= 1/4, and 8 rho c_flat A_2 <= gamma_B   [block radius,
      kinds [1]-[3], Step 3 (Blocks); the last condition is the only one involving gamma_B: kind [2] needs |sigma omega(k)| <= 2 rho c_flat A_2 <=
      gap'(k)/2 with gap' >= gamma_B/2.  When gamma_B is window-dependent (V1: gamma_B(w) = min_m M_m u(w)/4) so is c_flat:
      c_flat(w) = min(c^f_flat, gamma_B(w)/(8 rho A_2)) >= c_f u(w), exactly as in V1's Theorem E'' / Lemma U'];
 (c5) K_W c_flat <= min(gamma_0/8, C_min/4), and 6 K_sharp c_flat^2 t_1^2 (2 + Lambda_max) <= gamma_min/2, 6 K_sharp c_flat^2 t_1^2 <= gamma_0/8,
      6 |I| K_sharp K_Y c_flat^2 t_1^2 <= 1;
 (c6) 6 |I| K_sharp K_Y K_A c_flat + (48 K_sharp K_W K_y c_flat + 36 K_sharp^2 K_y^2 c_flat^2)/(C_min/2) <= delta/16  [cubic and quartic
      error terms of Step 4: since |tau| <= c_flat t and K_A, K_W enter as K/t, each term is <= (const) c_flat tau^2];
 (c7) K' c_flat (1 + rho^2) <= delta/8, K' := an f-constant times (A_0 + A_2) bounding the relative errors (1 + K_H T_0), (1 + K_h T_0) per
      unit T_0/t (Lemma lem:block(d): 2|d sigma| M/C with |d(omega)| <= ||D omega||_2 <= A_2 ||Phi||_2/t + C_Delta; lem:base(b): 2|t| beta/nu with
      ||U^* beta|| <= ||U|| 2A_0/t).
t_1 := an f-constant so small that (c5)'s quadratic conditions hold (they contain c_flat^2 t_1^2) — t_1 is chosen after c_flat's
first-order conditions; c_late is an f-constant fixed in Steps 3-5 (each use is marked).  Put T_0(i) := c_flat t_i.

Step 1-2 (targets and exact decompositions).  As in thm:engineered, with g''_i, c_i, g'_i of 3.2(vi) and the three decompositions
f' + tau g'_i = (a' + tau B^diamond) + sum_m R_m^*(w'_m + tau Omega^diamond_m), B^diamond := rho(beta^diamond - c_i a').  By d-consistency (Lemma UE-1(c)),
d'_m(omega^diamond) = d_m(omega^diamond) = d^diamond_m, hence kappa^diamond_m = rho (d'_m - d_m)(omega^diamond - omega^theta) = 0 and
      Omega^diamond_m = rho(omega^diamond_m - d'_m(omega^diamond_m) w'_m) + rho(d^diamond_m - d^theta_m)(w'_m - w^0_m)   (diamond = +-),
Omega^theta_m = rho(omega^theta_m - d'_m(omega^theta_m) w'_m).  The identities of Step 2 use only the two representations at f_0 (valid for
violated pairs, U3 Lemma VT (1)).  The anchors (V^an = w^0 if Delta_m >= 0, = y_A of lem:anchor if Delta_m < 0) and the remainder Z are as
there.  ||W^natural_m - w'_m||_inf + ||D_m(W^natural_m - w'_m)||_2 <= (K_W/t_i)|tau|: |omega^diamond(k)| <= A_2/t (kinds [1]-[3]; kind [1]:
2gap/t <= 2/t), ||D omega||_2 <= A_2 ||Phi||_2/t, |d^diamond| <= ||D omega||_2/C... <= K/t, ||V^an - w'||_inf <= 3, |Delta| <= C_Delta.

Step 3 (first-order terms and excesses).
 Blocks.  lin'_m(W^natural_m) = r_m <V^an_m - w'_m, R_m x'>/sigma'_m (the kappa-term is absent), r_m := (1/2)|tau| rho |Delta_m| <= |tau| C_Delta.
 By lem:approxfacts(E5)/lem:anchor, |<V^an - w', R x'>| <= c'(Bx_m + S_m) (for V^an = w^0: = c' Bx_m; for y_A: proof of thm:engineered Step 3,
 with |(R x')(k)| <= lambda_k c').  By Lemma UE-1(d), (e) and the choice of s_1:
      Bx_m + S_m <= K_w Pi^2 log(e/Pi) + 4 Pi_X c_fine + 4 C_lev W_lev r^2 + 2 t(N'') + 4m(C_S (K_w Pi)^2 + s_1^2 T^4) <= c_late delta s_1,
 using Pi <= K_w s_1 (Lemma UE-1(a), 3.2(iii)-(iv)), (LATE) (K_w^3 s_1 log(e/s_1) <= c' delta), (W-a) (Pi_X c_fine <= (4 rho mu_1 n A_0/(T nu_0))
 s_1 c_fine <= c delta s_1), and 3.2(iv).  Hence |lin'_m| <= |tau| C_Delta (2/sigma_m) c_late delta s_1 <= (delta/(64|I|)) |tau| s_1 for c_late
 small (f-constant).
 Excess: write W_0 - r_m w' = (1 - r_m)(w' + t'(omega^diamond - d'(omega^diamond) w')), t' := tau rho/(1 - r_m) (kappa = 0).  The block radius at f'
 for sigma := t', |sigma| <= 2 rho c_flat t_i: for k of kind [1], |sigma omega(k)| <= 4 rho c_flat gap^0(k) <= gap'(k)/2 (gap' >= gap^0/2,
 Lemma UE-1(c), and (c4)); kind [2] likewise with gap' >= gamma_B/2 and |omega| <= A_2/t; kind [3]: with vs := sgn w'(k) = sgn w^0(k), the
 outward part satisfies vs sigma omega(k) <= 1.5 |sigma| gap^0(k)/t <= 3 rho c_flat gap'(k)... so vs W(k) <= (1 - d sigma)(M' - gap') + gap'/2 <=
 (1 - d sigma) M' (|d sigma| <= 1/2 by (c4)), and -vs W(k) <= |sigma omega(k)| <= 2 rho c_flat A_2 <= (1 - d sigma) M' (c4): the INWARD bound of
 Z3 Lemma 5.1.  So ||W(sigma)||_inf = (1 - d' sigma) M' (lem:block(c), whose proof uses only these coordinatewise bounds), and lem:block(d)
 at f' gives N_m(w' + sigma(omega - d' w')) <= 1 + (sigma^2/2) H'_m(omega)(1 + 2|d' sigma| M'/C').  For diamond = theta, |tau| <= s_1 and the
 radius condition |s_1 rho omega^theta(k)| <= gap'(k)/2 holds by (LATE) (s_1 <= T gap_min/(4 rho A_2)).  Therefore, as in thm:engineered,
      G'_m(W^natural_m) <= hat G_m := (rho^2 tau^2/2) H'_m(omega^diamond)(1 + K' T_0/t_i) + r_m g_m,  g_m := N(V^an) - <V^an, R x'>/sigma' <= K(Bx_m + S_m),
 and H'_m(omega) = (C^0_m/C'_m) H_m(omega) (Lemma UE-1(c)).
 Base.  By lem:bookkeeping(b) at f', G'_b(A_tau) = Exc'(tau B^diamond + Z) + nu' Psi'(U^*(tau B^diamond + Z)/nu').  Claim (*) of U3 Lemma VT holds at f'
 with the additional coordinates of f': (1) masses on W: as in VT (theta: |tau rho b^theta_j| <= s_1 rho |b^theta_j| = m_j/4 <= |a'_j|/2; +-: cost
 <= 2 rho|tau| viol(j)); (2) F: no flip by (c1) and |tau rho c_i| <= 1/2 (Lemma UE-1(g) and (LATE)); E: by (U3) and (c2) (contact-like data
 never flip on their sides, theta-masses protect the theta piece; the other alternative gives |tau rho b_j| <= |a'_j|/4); (3) lever coordinates:
 (Z-free/Z-con) coordinates carry zero data (Lemma LV(b),(c)), so their summands vanish whether they are free, contacts or banks at f';
 (TU) banks: contact-like data (sign eps_l = z = sgn a'_j); (TU) pulls: |tau rho beta^diamond_j| <= rho c_flat t_i (|gamma_{i,l}| v_l(j) + later) <=
 rho c_flat (A_2 + C_Delta + 1) lambda_l v_l(j) <= 8 lambda_l v_l(j) = mu_p/3 (c3; "later" = carriers > L meeting j through targets, whose
 coefficients are <= C_Delta lambda and whose total weight is <= 2^{-2j} c_l delta_l, negligible against lambda_l v_l(j)/t_i once r <= T/K_w), so
 a'_j + tau B_j keeps the sign of a'_j: summand 0; (S-mass) p_0: t|b| <= m_0/... as in (U3); (4) contacts in (N_w, N''], free coordinates,
 contacts beyond N'': exactly as in VT.  Hence
      Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} + 2 rho |tau| eps  (diamond = +-),   Exc'(tau B^theta) = 0  (0 < |tau| <= s_1),
 and with ||Z||_1 <= |tau| C_Delta sum_{A_m} lambda_k(|w' - w^0| + (C' - C)_+) <= |tau| C_Delta S_m and lem:base,
      hat G_b := (rho^2 tau^2/2) h'(beta^diamond)(1 + K' T_0/t_i) + (1/2) rho |tau| V_{>N''} + 2 rho|tau| eps + 2|tau| C_Delta sum_m S_m.
 For |tau| > s_1: (1/2) rho V_{>N''} <= delta s_1/128 (3.2(iv)), 2 rho eps <= delta s_1/32 (VT'), 2 C_Delta sum S_m <= delta s_1/128 (c_late):
 the three linear terms are <= (delta/16)|tau| s_1 <= delta tau^2/16.  So hat G_b, hat G_m <= K_sharp tau^2 for |tau| <= T_0(i)
 (H' <= 2H <= 4/sigma, h' <= 2h^0 + small by Lemma UE-1(f)).

Step 4 (rebalancing).  Proposition prop:rebalancing at f' with h := tau g'_i (h(x') = 0 since g'_i(xhat') = 0), the transfer vectors y' of
f' (Lemma M2), eps_m := (lin'_m + hat G_m - hat Gamma)/e'_{y,m}: |eps_m| <= 2(|lin'_m| + hat G_m + hat Gamma) <= 6 K_sharp tau^2 (|tau| > s_1;
|lin'| <= tau^2), <= 4 K_sharp tau^2 (theta).  (R1) via lem:TV with eta := (K_W/t_i)|tau| <= K_W c_flat: conditions (c5).  |lambda| <= 6|I|K_sharp
K_Y tau^2 <= 1 by (c5).  The error E <= 12 |I| K_sharp eta_1 tau^2 + 6|I| K_sharp K_Y |tau|^3 K_A/t_i + (48 K_sharp K_W K_y |tau|^3/t_i +
36 K_sharp^2 K_y^2 tau^4)/(C_min/2) <= (delta/16 + delta/16) tau^2 by eta_1 and (c6) (|tau| <= c_flat t_i; K_A/t_i bounds (|q*(A_tau) - 1| +
q*(A_tau - a'))/|tau|: q*(B^diamond) <= 2(1+||U||) rho A_0/t_i + |c_i|, ||Z||_1/|tau| <= C_Delta S_m <= 1).

Step 5 (levels).  hat Gamma = c' hat G_b + sum_m sigma'_m hat G_m <= (rho^2 tau^2/2)(c' h'(beta^diamond) + sum_m sigma'_m H'_m(omega^diamond))(1 + K' c_flat)
+ (linear terms).  By Lemma UE-1(c), (f): the bracket is <= Gamma^{(0)}_diamond + K_f(A_0^2 Pi/T^2 + A_0 tail_W/T + Pi) <= Gamma^{(0)}_diamond + delta/8
(LATE, W-c; c_late), and Gamma^{(0)}_theta <= max(Gamma^{(0)}_+, Gamma^{(0)}_-) <= 1 + eta_0/2 by convexity (violated pairs included: Gamma_w is
convex in the pair).  The linear terms (base: Step 3; blocks: sum sigma' r_m g_m <= |tau| C_Delta K sum (Bx + S) <= (delta/32) tau^2 for |tau| > s_1)
are absent for diamond = theta.  With (c7), for 0 < |tau| <= T_0(i):
   p*(f' + tau g'_i) <= 1 + hat Gamma + E <= 1 + (tau^2/2)(rho^2 (1 + eta_0/2) + delta/8 + delta/8 + delta/8 + delta/4 + delta/8) <= 1 + (tau^2/2)(1 - delta),
since rho^2(1 + eta_0/2) = 1 - 2 delta.  The remaining assertions are Lemma UE-1(a), (g).  QED

## 3.6 Remarks.
 (a) What changed relative to thm:engineered: (i) the first-order d-mismatch is ZERO (exact d-consistency, Lemma DC) instead of
     K(omega) s_1, so K_sharp is an f-constant (no dependence on the window or on t); (ii) every "late stage" assertion is replaced by an
     explicit bound in terms of the perturbation size Pi (Lemma UE-1), which is linear in s_1 with a WINDOW constant; (iii) the scrambling
     condition is used in the explicit form (U5); (iv) violations are tolerated as in Lemma VT, now uniformly in the piece (the cost
     2 rho|tau| eps does not depend on t); (v) the lever coordinates are protected (zero data, contact-like data, or pull masses dominating
     c_flat t |data|).
 (b) The only interplay between s_1 and the window is the interval [64 rho eps/delta, s_late]: (VT') bounds s_1 from below by the
     violation mass, (LATE) from above by window quantities.  This is exactly U3's (S2c) "threshold comparison", now with an explicit s_late.
 (c) T_0 >= c_flat t_i with c_flat an f-constant: the per-piece radius scales with the piece, as (S2a) requires.  U3's original scaling check
     was correct for every term EXCEPT the d-mismatch, which (Proposition J) is O(sqrt|Omega| ||X||) for valid data (not O(s_1/t^2)), still
     non-uniform along windows, and which d-consistency removes exactly.
# X2 part 4 — (S2b) averaging AT the engineered approximant (Theorem E^eng) and (S2c) the threshold comparison

## 4.1 Theorem E^eng (windowed recovery through d-consistent engineered approximants of nearby rows; violated data allowed).  PROVED.
Let I be finite, f in S_{p*} with F finite, g in C(f), rho in (0,1), eta_0 in (0,2] with rho^2(1 + eta_0) <= (1 + rho^2)/2, delta as in 3.
Suppose there are base rows f_j -> f (eps_j := p*(f_j - f)) and, for every j, a window S_j := {T_j 2^{1-i} : 1 <= i <= n_j} with a window
family at f_j (pieces g_{j,t}, t in S_j) satisfying (U1)-(U7) with FIXED A_0, A_2, gamma_B, and in addition
 (E-c) p*(g - g_{j,t}) <= K_j t for t in S_j;
 (E-d) K_j T_j -> 0 and n_j c_flat(j)/K_j -> infinity, theta_j/c_flat(j)^2 -> 0 (c_flat(j) := c_flat of Theorem UE for the window's gamma_B;
       an f-constant when gamma_B is fixed);
 (E-e) eps_j <= theta_j (T_j 2^{-n_j})^2 with theta_j -> 0;
 (E-f) the window conditions (W-a), (W-b) of Theorem UE hold at f_j, and the THRESHOLD COMPARISON 64 rho eps^{viol}_j <= delta s_late(j)
       holds (eps^{viol}_j := max over the pieces of the violation mass; s_late(j) the bound (LATE) of Theorem UE at f_j).
Then (f, rho g) in cl NA((c_0, p_N), l_2^2).  If the hypotheses hold for every rho < 1, then (f, g) in cl NA.
Proof.  Fix j large (conditions below).  Put n := n_j, K := K_j, t_i := T_j 2^{1-i}, T := t_n = T_j 2^{1-n}.  Theorem UE at f_0 := f_j (p*(f_j - f)
<= r_f/2 for j large) with s_1 := s_late(j) (admissible by (E-f)), N_w with tail_W <= min(c_late delta T/A_0, T^3) and N'' as in 3.2(iv), gives a
norm-attaining f'_j and g'_{j,i} with
 (A^eng) p*(f'_j + tau g'_{j,i}) <= 1 + (tau^2/2)(1 - delta) for |tau| <= c_flat t_i;
 (P)     p*(f'_j - f_j) <= K_w Pi log(e/Pi) and p*(g'_{j,i} - rho g_{j,t_i}) <= K_w(K_w s_1 + c_fine + tail_W)/t_i =: e_{j,i}.
Since Pi <= K_w s_1 and s_1 = s_late(j) is a window quantity, choose (by (LATE) one may decrease s_1 below s_late as long as (VT') holds;
if 64 rho eps^{viol}_j < delta s_late, decrease s_1 to max(64 rho eps^{viol}/delta, s_1 small enough); if eps^{viol} = 0 any small s_1 works)
the stage so that eps'_j := p*(f'_j - f) <= eps_j + K_w Pi log(e/Pi) <= 2 theta'_j T^2 with theta'_j -> 0, and e_{j,i} <= K t_i — possible when
K_w (K_w s_1 + c_fine + tail_W) <= K T^2, which holds under (E-f) by (W-a) and s_1 <= s_late (s_late contains the factor T^3; see 4.2 for the
explicit check at U1's companions).  Two bounds for every i and real r:
 (A) if |r| <= c_flat t_i: p*(f'_j + r g'_{j,i}) <= 1 + (r^2/2)(1 - delta);
 (B) always: p*(f'_j + r g'_{j,i}) <= p*(f + r rho g) + eps'_j + |r| p*(g'_{j,i} - rho g) <= s(rho r) + eps'_j + 2 rho |r| K t_i
     (g in C(f); p*(g'_{j,i} - rho g) <= e_{j,i} + rho K t_i <= 2 K t_i for rho >= 1/2, and <= (1 + rho) K t_i in general).
Put gbar_j := (1/n) sum_i g'_{j,i}; by convexity p*(f'_j + r gbar_j) <= (1/n) sum_i p*(f'_j + r g'_{j,i}).  Let r_0 := min(sqrt(delta), sqrt(1 - rho^2),
c_flat t_1)... precisely r_0 in (0, 1] with r_0^2 <= min(delta, 1 - rho^2).
Case |r| <= r_0.  I_r := {i : c_flat t_i < |r|}; sum_{I_r} t_i < 2|r|/c_flat.  If I_r is empty, all terms obey (A) and 1 + (r^2/2)(1 - delta) <=
1 + r^2/2 - r^4/8 <= s(r) because r^4/8 <= delta r^2/2 (r^2 <= delta... <= 4 delta).  Otherwise |r| > c_flat T, so eps'_j <= 2 theta'_j T^2 <= 2 theta'_j
r^2/c_flat^2, and
   p*(f'_j + r gbar_j) <= max{1 + (r^2/2)(1 - delta), s(rho r)} + 2 theta'_j r^2/c_flat^2 + (1/n) 2 rho |r| K (2|r|/c_flat)
                       <= max{1 + (r^2/2)(1 - delta), s(rho r)} + r^2 min(delta/4, (1 - rho^2)/6)                      (j large: theta'_j -> 0,
                                                                                                                         n_j/K_j -> infinity)
                       <= s(r),
using 1 + (r^2/2)(1 - delta) + delta r^2/4 <= 1 + r^2/2 - r^4/8 (r^2 <= delta) and s(rho r) + (1 - rho^2) r^2/6 <= s(r) (lem:slack(a), |r| <= 1).
Case |r| >= r_0.  By (B) for all i: p*(f'_j + r gbar_j) <= s(rho r) + eps'_j + 2 rho |r| K (2 T_j/n) <= s(rho r) + (1 - rho^2) r_0 |r|/3 <= s(r), once
eps'_j <= (1 - rho^2) r_0^2/6 and 4 rho K_j T_j/n_j <= (1 - rho^2) r_0/6 (true for j large by (E-d)), using lem:slack(a) and min(r^2, |r|) >= r_0 |r|.
Hence gbar_j in C(f'_j), so (f'_j, gbar_j) attains its norm (prop:reduction(d)), and ||(f'_j, gbar_j) - (f, rho g)|| <= eps'_j + p*(gbar_j - rho g)
<= eps'_j + (1/n) sum_i 2K t_i <= eps'_j + 4 K_j T_j/n_j -> 0.  QED
Remarks.  (a) Unlike Z3's Theorem E (and V1's E'', V2's E^>=, E^SC), no exactness of the averaged data and no final call of cor:D1 /
thm:engineered at f_j is needed: the averaging is carried out at the norm-attaining point itself, with the per-piece bounds (A) of
Theorem UE.  This is what makes violated data usable along a sequence of windows (U3's (S2b)).  (b) The scale decoupling (E-e) enters
exactly as in Theorem E (pieces too fine for the scale r are compared with the mate g of f).

## 4.2 (S2c) The threshold comparison at U1's companions; design addition (W_exp).  PROVED (arithmetic).
DESIGN ADDITION (W_exp): at every stage l+1 the weight rule of T_final / D^{U1'} additionally requires
      c_{l+1} <= exp(-1/T_lo(l, M(l)))       (an UPPER bound on the weight, chosen at stage l+1 after all sub-windows of level l).
Admissibility and N-freeness are unaffected: (T-a)-(T-d) use upper bounds on weights only through allowedness (b) and (W4)-type conditions,
which remain satisfiable (V4 Lemma 2.1's argument, U3's (W10)); in D^{U1'} the term is added to c_p^low (U1-ref 6.2), which does not depend on
R, so the absorber-target construction is unchanged; every window theorem uses weights only through upper bounds ((P2), the box bound, Lemma
GW of U4).  (W_exp) implies U3's (W10) and every (W_k) for large l.
Claim.  At the companion f^# of a clean sub-window w of a main stage L (U1 part 4), with T := T_lo(w), n := n(w):
 (i)   every window constant entering Theorem UE is at most exp(C_abs log^2(1/T)) for an absolute C_abs: n <= log_2(1/T) (T_lo = 2^{-n} T_hi);
       Design(L) <= n (n(w) >= l 2^{l^3} Q(w) >= Design); A_0 an f-constant; gap_min >= c_f T^4/(L Design) (U1-ref Proposition KN(b): active near-
       threshold Omega carriers gap >= c_f eta D(L) M, eta = T^4/(L Design); inactive ones >= c_f eta M; others robust or kind [1] with gap >= t^2 >= T^2;
       absorbers 3M/4); x_0 >= c_f gap_min Phi_min(L) >= T^5 (U1 Lemma 4.3: coarse carriers and absorbers do not contribute below s_0(f^#)); C_S <= C/q_0^2
       (U1 Lemma 4.3); lever constants (Lemma LV with (D-lev)) <= Design(L)^C; hence K_w <= T^{-C'} and s_late(w) >= T^{C''} for absolute C', C'' and
       small T;
 (ii)  the fine-origin violation mass, the fine weight c_fine and c_tiny are <= C_f c_{L+1} (U1-ref 5: total l_1-mass of all contributions of carriers
       at stages > L is <= C_f sum_{l' > L} lambda_{l'}; coefficients <= C_Delta lambda) — with (W_exp), c_{L+1} <= exp(-1/T_lo(L, M(L))) <= exp(-1/T)
       (T_lo(L, M(L)) <= T_lo(w));
 (iii) hence (W-a), (W-b) and 64 rho eps^{viol} <= delta s_late hold for all large L: exp(-1/T) <= T^{C''+2} delta/(64 rho C_f) for T small; and the
       requirement K_w(K_w s_1 + c_fine + tail_W) <= K T^2 of 4.1 holds with s_1 := max(64 rho eps^{viol}/delta, exp(-1/(2T))) <= s_late.
So U3's (S2c) holds for the design D^{U1'} + (W_exp).  (W10) alone does not suffice for the s_late obtained here: with gap_min ~ T^4 entering
K_w, the bound is s_late ~ T^{15} or smaller, while (W10) only gives eps^{viol} <= C_f c_{L+1} ~ T^{10}; whether a sharper late threshold would make (W10)
enough is not investigated (it is irrelevant: (W_exp) is a free design choice).  [Without (W_exp) the comparison is OPEN for D^{U1'}; it is a pure design choice.]
# X2 part 5 — (C_mix): mixed activity classes are recovered (given (KN) for the class, as in Master Theorem IV')

Setting: U1 part 4/5 with U1-ref's fixes (design D^{U1'}, Proposition KN, release G1), plus (D-lev) (Lemma LV) and (W_exp) (4.2).  N >= 2,
F finite, w a clean sub-window of a main stage L >= l_f, a (class, cube) set S of scales of ONE activity class a, MIXED: A_- := {m active,
sigma_m = -1} and A_+ := {m active, sigma_m = +1} both nonempty (data convention: sigma_m = sgn Delta''_m).  The class satisfies (KN_{w,a}).

## 5.1 Lemma CM (the self-aligned completion of a mixed class).  PROVED.
Let f^(1c) be the row after U1's steps (1a) [Proposition KN of U1-ref], (1b), (1c), and J_fine as in U1 4.1 with the G1 release (U1-ref
Section 5).  Define z on J_fine by the forward recursion of U1 Lemma 4.1 with STATIC ownership: own(j) := the first OWNER-CANDIDATE (in stage
order) whose vector meets j, where the owner-candidates are U1's types (a)-(c) (Omega_act, coarse peaks of active blocks, tuned absorbers) and
(d) EVERY fine carrier of an active block (its coefficient in V is -Delta''_m lambda_k w(k), Lemma 1.1(a) of U1; it may vanish, which is
harmless below); fine carriers of inactive blocks have coefficient 0 and are not candidates.  The rule at a fine candidate k, processed in
stage order with O(k) := {j in J_fine : own(j) = k} and Y_k := the part of u_k(zhat) fixed by coordinates outside O(k) (all fixed earlier):
   negative block (m(k) in A_-): varsigma_k := sgn Y_k (+1 if Y_k = 0), z_j := varsigma_k sgn u_k(j) on O(k)      [SELF-ALIGNED];
   positive block (m(k) in A_+): varsigma_k := sgn Y_k, z_j := -varsigma_k sgn u_k(j) on O(k)                     [anti-aligned, U1 Lemma 5.4];
coarse owners (types (a)-(c) of U1 Lemma 4.1) set z_j := sgn(coefficient x u_own(j)(j)) on their owned sets; coordinates without owner meet no
carrier with nonzero coefficient (V(j) = 0) and get z_j := 0.  Let f^# be the resulting row.  Then for EVERY scale t in S:
 (a) every fine carrier of a negative block is a self-aligned peak with |u_k(zhat^#)| = |Y_k| + own_k >= delta°_k and margin
     mu_k >= q^#_0 delta°_k/2 (state (R) of U1 Lemma 5.2); hence the negative blocks A_- satisfy the explicit scrambling bound
     Scr^#_m(x) <= C (x/q^#_0)^2 for 0 < x <= x_0(f^#) (U1 Lemma 4.3's proof, whose only input on fine carriers is (R)), with x_0(f^#) >= c_f gap_min
     Phi_min(L) (coarse statuses from Proposition KN(b), tuned absorbers gap 3M/4);
 (b) V(Domega(t)) is z^#-admissible at every coordinate off F^# EXCEPT on the owned sets of positive fine carriers; there are no violations at
     free coordinates ((H3) of Lemma VT is vacuous); the total violation mass satisfies
         eps^{viol}(t) <= sum_{k fine, active} |coef_k| ||u_k||_1 + sum_{j owned by positive k} sum_{k' later} |coef_{k'}| |u_{k'}(j)| <= 2 C_Delta sum_{l > L} lambda_l
                       <= 4 C_Delta c_{L+1};
 (c) everything else of U1's companion is unchanged: exactness on E_c (U1 Proposition 3.4: the biased pairs cancel any residue, continuous in z),
     the coarse owned sets (U1 Lemma 4.2, whose estimates do not use the signs of the shifts), statuses of coarse carriers and absorbers (U1-ref
     Proposition KN(b), U1 Lemma 3.3), cost p*(f^# - f) <= theta_w T_lo(w)^2 (U1 Lemma 4.5), true shifts (U1 Lemma 4.6 (a)-(c)).
Proof.  (a) For a negative fine carrier k the coefficient -Delta''_m lambda_k w(k) has sign varsigma_k... precisely: by the recursion
u_k(zhat^#) = Y_k + varsigma_k sum_{O(k)} |u_k(j)| (zhat^# = z on J_fine, diagonal base), so |u_k(zhat^#)| = |Y_k| + own_k with own_k >= ||u_k 1_{S_k}||_1
= delta°_k (S_k ⊂ O(k): no earlier carrier meets S_k, allowedness (a); S_k ⊂ J_fine); the peak criterion and the margin bound are those of U1
Lemma 4.1 ((W3): theta Phi_k/m << delta°_k).  Scrambling: U1 Lemma 4.3 verbatim (coarse carriers and tuned absorbers do not contribute below
x_0; every other carrier of block m is (R)); the super-exponential decay of delta_k H_k gives sum_{k: delta_k H_k <= X} (delta_k H_k)^2 <= 2X^2.
(b) Coordinates owned by a coarse owner or by a negative fine carrier: U1 Lemma 4.2 (dominance |coef_own| |u_own(j)| >= 2 sum_{later} |coef| |u(j)|;
for a negative owner |coef_k| = |Delta''_m| lambda_k M because k is a peak), so sgn V(j) = sgn(coef_own u_own(j)) = z_j: for negative owners
coef_k = -Delta''_m lambda_k varsigma_k M with Delta''_m < 0, so sgn V(j) = varsigma_k sgn u_k(j) = z_j.  Released coordinates (G1) carry no coarse
contribution (inactive Omega carriers have gamma = 0, coarse peaks of inactive blocks have Delta''_m = 0).  Unowned coordinates: V(j) = 0.
Remaining coordinates are owned by positive fine carriers; there |V(j)| <= |coef_k u_k(j)| + sum_{later} |coef_{k'} u_{k'}(j)| and the violation at j
is at most |V(j)| (viol(j) = (z b^+)_- + (z b^-)_+ <= |b^+(j)| + |b^-(j)| = |V(j)| for the split b^+ = chi V, b^- = (chi - 1)V of U1 Prop. 2.2(e));
coefficients of fine carriers are <= C_Delta lambda (U1 Lemma 2.1; absorbers' coefficients <= C_f lambda, U1 Prop. 3.4) and ||u||_1 <= 1.
All these coordinates are contacts of f^# (z = +-1).  (c) The recursion only fixes z on J_fine; the cited statements use J_fine only through
"z is fixed on J_fine after (1c)" and dominance.  QED

## 5.2 Theorem C_mix (mixed classes are recovered).  PROVED (modulo the refereed tools of U1/U1-ref and parts 2-4 here).
Design D^{U1'} + (D-lev) + (W_exp), N fixed, F finite.  Suppose that for infinitely many main stages L some clean sub-window w of L has a
(class, cube) set S of at least n(w)/D_cls(w)^2 scales of ONE activity class a (one-signed OR mixed) satisfying (KN_{w,a}).  Then f in Rec(p_N).
Proof.  For each such (L, w): companion f^# of Lemma CM (for one-signed classes the same recursion: in configuration (i) it is U1's
recursion, in configuration (ii) it is the anti-aligned rule of Lemma 5.4 with violations only at frustrated carriers — no Schauder completion is
needed).  For every t in S the data of U1 Proposition 2.2(e) at f^# form a window family (U1)-(U7) with: (U1), (U2) from Proposition 2.2(e) and
V1 TR(iii) (kappa_w <= 1 + eta_0/2, kinds [1]-[3], A_2 = 22, A_0 an f-constant), the fine part of the data entering Gamma only through
||V_fine||_1 <= C_f c_{L+1} (contributing <= C_f c_{L+1}^2 / nu); (U3) from V1 TR(iv) and U1 Proposition 3.4(d); (U4) from Lemma CM(b) (contact
violations only, eps^{viol} <= 4 C_Delta c_{L+1}); (U5) from Lemma CM(a); (U6) from Lemma LV with (D-lev); (U7) from U1 Lemma 2.1.  (E-c) p*(g - g_t) <=
K t, K = C_f (Design/u)^C (Proposition 2.2(e)); (E-d), (E-e) as in Master Theorem IV' (U1-ref Section 8: |S| >= l 2^{l^3}(Design/u)^C >> K/c_flat,
K T_hi(w)/|S| -> 0, p*(f^# - f) <= theta_w T_lo(w)^2); the subset version of the averaging is U1 Lemma 2.4's argument applied to the proof of
Theorem E^eng (only "sum_{I_r} t_i < 2|r|/c_flat over dyadic scales" and the count |S| are used).  (E-f) is 4.2 ((W_exp)).  Theorem E^eng gives
(f, rho g) in cl NA for every rho < 1.  QED
Consequences.  (1) U1's Corollary IV.2 (shape of a counterexample) is VOID: frustration of positive carriers is harmless.  (2) The open
item (C_mix) of ADDENDUM 8 is closed (for D^{U1'} + (D-lev) + (W_exp)); the toy phenomena of U1 5.5 (forced wrong branches (W), bad carriers in
threshold bands) do not arise because the completion is never required to be exact on fine coordinates — fine-origin violations are tolerated
(Lemma VT inside Theorem UE) at the price s_1 >= 64 rho eps^{viol}/delta, which (W_exp) makes compatible with (LATE).  (3) Remaining hypothesis:
(KN_{w,a}), i.e. U1-ref's STATUS COHERENCE problem (an active block with an active near-threshold switching carrier and no inactive Omega carrier
of robust relative position) — this is the X1 task, untouched here.
# X2 part 6 — The resulting master theorem for F finite, the residual, corrections, numerics

## 6.1 The design D^{X2}.
D^{X2} := U1-ref's D^{U1'} (built on U4's T_final: SLD with S_l = {2^l(2i+1)}, allowedness (a), (c), (c''), diagonal base mu_s = 2^{-s^2-1},
pigeonhole sub-windows, absorber pre-pairs/clusters, weights (W1)-(W5), (W7), (W4'')) plus two ladder conditions:
 (D-lev) Design(L) >= max_{l <= L} 2^{sigma_2(L)}/(mu_{sigma_2(L)}^2 delta_l)   (efficiency of the d-consistency levers, Lemma LV);
 (W_exp) c_{l+1} <= exp(-1/T_lo(l, M(l)))   (an upper bound on weights; added to c_p^low in D^{U1'}).
Both are computable at the stage where they are imposed, independent of N and of f; admissibility (T-a)-(T-d), (P1), (P2) and N-freeness are
unaffected (they use weights only through upper bounds and Design only through lower bounds); every refereed result valid for D^{U1'}
remains valid (U4 Lemma GW: window results use a window only through properties preserved by enlarging Design and shrinking weights).
PROVED (by inspection, as for U3's (W10) and V4's design conditions).

## 6.2 MASTER THEOREM V (F finite).  PROVED modulo the refereed results it cites (V2 MT III'; U1-ref MT IV', Proposition KN, Section 5-7
## fixes; U1 Lemmas 1.1, 1.3, 2.1, 2.4, 3.2-3.4, 4.1-4.6, Proposition 2.2; V1 TR, TU, ST, CO; Z3 Lemma 3.1; the note's lemmas) and parts 1-5.
Design D^{X2}, N fixed, f in S_{p_N^*} with finite base support F.  If
   for infinitely many main stages L some clean sub-window w of L has at least n(w)/D_cls(w) dyadic scales whose activity class a
   satisfies (KN_{w,a}) — one-signed OR MIXED —,
then f in Rec(p_N), i.e. (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f).
Proof.  Pigeonhole (U1 MT IV') gives a (class, cube) set S with |S| >= n(w)/D_cls(w)^2.  One-signed classes: U1-ref MT IV' (refereed), or
Theorem C_mix's argument.  Mixed classes: Theorem C_mix (5.2): Lemma CM's companion, the window family (U1)-(U7) with fine-origin contact
violations of mass <= 4 C_Delta c_{L+1}, levers by Lemma LV, Theorem UE at each companion, Theorem E^eng along the windows ((E-f) by (W_exp),
(E-d), (E-e) as in MT IV').  QED
COROLLARY (contrapositive; the F-finite residual).  If f (F finite) is not in Rec(p_N) for D^{X2}, then f is a (C*) row (V2 MT III') AND for all
but finitely many main stages L, at EVERY clean sub-window w of L, more than n(w)(1 - 1/D_cls(w)) of the scales lie in activity classes a for
which (KN_{w,a}) FAILS: some active block contains an active near-threshold switching carrier (|rho - 1| <= b(w)) and every inactive
Omega carrier of that block has rho < u(w) (nearly neutral).  This is exactly U1-ref's STATUS COHERENCE problem (OPEN; task X1).
In particular: (C_mix), (S2) = (S2a') + (S2b) + (S2c) of ADDENDUM 8 are CLOSED; (S1) (multi-block coupling) is part of the exactification of
Gamma^#(kappa, a), which Proposition KN performs for all blocks at once, so it is contained in the (KN) residual; U3's RT*(c) is superseded by
U1's coarse exactness (Proposition 2.2 + absorbers).
Status of the density problem (unchanged in kind): Lemma Z at finite F for D^{X2} <= status coherence; Lemma Z at infinite F: (E1)-(E5) of
ADDENDUM 7 / U2's items; density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2): OPEN for every admissible T.  No counterexample is
claimed; nothing found points to one (every obstruction met here was removed by an exact cancellation or by a design choice).

## 6.3 What is new in X2 (labels).
 (1) Proposition J (PROVED): for VALID data (Gamma_w <= 2) the junction mismatch of thm:engineered is O(|Omega_m|^{1/2} ||X||), uniform in the
     piece scale t (U1 Lemma 2.1 bounds ||D Domega||_2; the diagonal base bounds the mass effects by ||X||); U3-ref F6a's s_1/t^2 came from a
     datum scaled by 1/t (Gamma ~ t^{-2}).  Non-uniform along windows (n, |Omega|) -> exact cancellation needed.  [PRECISION of U3-ref F6a.]
 (2) Lemma DC (PROVED): exact d-consistency by levers; the linearization is I - p q^T (rank one through the block norm), invertible with
     1 - q^T p >= 1 - C_m >= 1/2 (Sherman-Morrison), plus block-triangular absorber couplings; Poincare-Miranda gives an exact zero.  No
     kappa-neutral lever is needed for d-consistency (contrast: status coherence).  Numerically: J_fd = I - p q^T to 2e-10.
 (3) Lemma LV (PROVED): levers exist at U1's companions: (TU) for active class-G carriers, zero-data (Z-con)/(Z-free) levers for inactive and
     class-R carriers (exactness on E_c makes V = 0 there), (S-mass) at absorbers' tuning coordinates; design addition (D-lev).
 (4) Lemma UE-1 and Theorem UE (PROVED): uniform per-piece engineered bounds, T_0 = c_flat t with c_flat an f-constant (window-dependent only
     through gamma_B, as in V1), violation tolerant, with explicit late threshold s_late (a window quantity).
 (5) Theorem E^eng (PROVED): averaging at the norm-attaining approximant; no exact averaged data needed (U3's (S2b)).
 (6) (S2c) (PROVED arithmetic): the threshold comparison holds with (W_exp); (W10) does not suffice for the s_late obtained here (~T^{15}).
 (7) Lemma CM / Theorem C_mix (PROVED): mixed classes recovered by the self-aligned completion (negatives (R), positives anti-aligned) with
     fine-origin contact violations; frustration (U1 5.4-5.5) is harmless.  U1's Corollary IV.2 is superseded.
 (8) Master Theorem V (PROVED modulo refereed tools): the F-finite residual is exactly status coherence ((KN) failure) at (C*) rows.

## 6.4 Numerics (X2_work/; sanity checks only — finite models cannot exhibit infinite-dimensional failures)
 dcons_check.py:  N = 1 model, exact data (Gamma^+ = 0.0064, Gamma^- = 0.031): untuned kappa/||X|| = 0.0230 for s_1 = 1e-2 ... 1e-5 (linear in ||X||,
                  Proposition J); one (TU) lever restores nv exactly (residual <= 2e-17), kappa_tuned <= 3e-17.
 dcons_check2.py: same with long signature sets and the pull chosen with v(j_p) in [2 du, 2^G 2 du]: bank mass / ||X|| = 15-26, kappa_tuned <= 3e-17.
 dc_jacobian.py:  6 random blocks with |Omega| = 2 and (Z-free) levers: finite-difference Jacobian of F equals I - p q^T to 2.1e-10; 1 - q.p
                  exceeds 1 - C by >= 0.153 (prediction >= 0).
 ue_check.py:     violated piece (eps = 1.6e-4 at a peak's signature contact), engineered approximants with s_1 in {64 rho eps/delta, 4 rho eps/delta,
                  eps/20}, tuned and untuned, true p* by SOCP on a tau-grid in [1e-4, 0.05]: the bound 1 + (tau^2/2)(1 - delta) holds in all six cases
                  (max excess <= -2.6e-9, solver accuracy ~ 4e-9).  In this model even the sub-threshold and untuned variants satisfy the bound:
                  the SOCP rebalances optimally (finite models have no transfer inefficiency, and the violated contact is not a dead zone);
                  U3-ref's vt_ref_check.py remains the evidence that (VT) is sharp for dead-zone violations.
