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
