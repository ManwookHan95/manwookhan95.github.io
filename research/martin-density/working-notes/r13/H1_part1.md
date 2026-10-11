# H1 part 1: Proposition J1.11 (first-order Puiseux margin) -- PROVED; consequence: (R-T) is empty

Setting: X1 2.3-2.5 with the W-fix region (cert1 Section 2).  Fix a level L and a pattern kappa of level L.  N_T = the active
near-threshold carriers of the (T)-blocks of kappa, n := |N_T| >= 1.  Ratio space R^A (A = the active carriers of kappa).
 - K_kappa := {r : R_a(m)(r)^2 <= 1 - sigma_rob(m)/4 for every active block m} (compact, semialgebraic, defined over k);
 - Z := Z_kappa ∩ K_kappa, Z_kappa = common zero set of the tiny minors and tiny cofactor polynomials of Gamma^#(kappa, a);
 - psi_d(r) := m(d) |r_d| K(sigma_rob(m(d)), R_a(m(d))(r)^2), d in N_T (Lemma K; K is Nash on (0, inf) x [0, 1));
 - for Phi in (0, inf)^{N_T}: F_Phi(r) := max_{d in N_T} psi_d(r)/Phi_d, Y_1 := Z ∩ {F_Phi <= 1},
   G_h(r) := inf{F_Phi(r'') : r'' in Z, |r'' - r| < h},  mu_Phi(h) := 1 - max_{r in Y_1} G_h(r)  (mu := 1 if Y_1 = {}).
 - k := k_0(weights of the carriers of kappa outside N_T) (countable); Z, K_kappa, psi_d are defined over k and do not depend on
   Phi (X1 2.2(iv), cert1 Section 2).  The T_fin weights Phi^T := (Phi_d)_{d in N_T} are algebraically independent over k
   (GEN_fin(b), cert1 Section 4).

Standard tools used (all for semialgebraic sets/maps over the reals):
 [W]  Every semialgebraic set Z admits a finite stratification into connected Nash submanifolds (strata) such that
      (W1) the frontier condition holds: if S' ∩ cl(S) != {} for strata S != S', then S' ⊂ cl(S) \ S and dim S' < dim S;
      (W2) Whitney's condition (a) holds for every pair of strata (S, S') at every point of S' ∩ cl(S): if x_n in S, x_n -> y in S'
           and T_{x_n} S -> tau in the Grassmannian, then T_y S' ⊂ tau;
      (W3) it is compatible with finitely many given semialgebraic subsets (each is a union of strata).
      [Bochnak-Coste-Roy, Real Algebraic Geometry, Thm 9.7.11 (Whitney (b) implies (a)); van den Dries-Miller, Geometric
      categories and o-minimal structures, Duke Math. J. 84 (1996), 4.8; Loi, Illinois J. Math. 42 (1998).  The frontier
      condition: BCR Prop. 9.1.8 / vdD-M 4.8.]
 [SS] Semialgebraic Sard: for a Nash map Psi : S -> R^D on a Nash manifold S, the set CV of critical values is semialgebraic of
      dimension < D [BCR Thm 9.6.2].
 [TS] Tarski-Seidenberg: a set first-order definable with parameters in k is semialgebraic and definable over k.
 [GEN] (X1 2.4 in cert1's form) If B ⊂ R^n is semialgebraic, definable over k, and dim B < n, then no point of B has
      coordinates algebraically independent over k.

## 1.1 The regular cylinder set
Fix once and for all a stratification Sigma of Z as in [W], compatible with the sets {r_d > 0}, {r_d = 0}, {r_d < 0} (d in N_T).
For a nonempty D ⊂ N_T and a stratum S ⊂ ∩_{d in D} {r_d != 0}, Psi_{D,S} := (psi_d)_{d in D}|_S is a Nash map S -> R^D (on S,
|r_d| = +-r_d is Nash and R_a^2 < 1).  Let CV_{D,S} be its set of critical values and
      B^reg_kappa := ∪_{(D,S)} { Phi in (0, inf)^{N_T} : (Phi_d)_{d in D} in CV_{D,S} }.
By [SS], B^reg_kappa is a finite union of semialgebraic sets of dimension < |D| + |N_T \ D| = n:  dim B^reg_kappa < n.
(This is the set of X1's Lemma NLM; there it was shown that B_kappa ⊂ B^reg_kappa.)

LEMMA 1.1 (regular contact points).  PROVED.  Let Phi notin B^reg_kappa and r_* in Lambda := Z ∩ {F_Phi = 1}.  Put
D := {d : psi_d(r_*) = Phi_d} (nonempty) and let S be the stratum containing r_*.  Then S ⊂ {r_d != 0} for d in D and there is
v in T_{r_*} S with  d psi_d(r_*) v = -Phi_d  for every d in D.
Proof.  psi_d(r_*) = Phi_d > 0 forces r_{*,d} != 0; by compatibility the stratum of r_* lies in {r_d != 0}.  If d Psi_{D,S}(r_*) were
not onto R^D, (Phi_d)_{d in D} = Psi_{D,S}(r_*) would be a critical value, i.e. Phi in B^reg_kappa.  So it is onto; pick v with
d Psi_{D,S}(r_*) v = -(Phi_d)_{d in D}.  QED

## 1.2 The stratified projected flow (the uniformity lemma)
LEMMA 1.2 (almost-straight curves inside Z).  PROVED.  Let r_* in Z, S the stratum of r_*, v in T_{r_*} S, v != 0, and
eps in (0, 1).  There is delta > 0 such that for every y in Z with |y - r_*| < delta and every t in [0, delta/(2|v|)] there is a
Lipschitz curve gamma : [0, t] -> Z with gamma(0) = y, |gamma(s) - r_*| < 2 delta, |gamma'(s)| <= |v| and |gamma'(s) - v| <= eps |v|
for almost every s.
Proof.  Step 1 (choice of delta).  Only finitely many strata exist.  A stratum S' with r_* notin cl(S') has positive distance
from r_*; choose delta so small that B(r_*, 2 delta) meets only strata S' with r_* in cl(S').  For such S' != S the frontier
condition (W1) gives S ⊂ cl(S'), dim S < dim S', and Whitney (a) (W2) holds for the pair (S', S) at r_*.  Claim: after shrinking
delta, dist(v, T_x S') <= eps |v| for every such S' and every x in S' ∩ B(r_*, 2 delta).  For S' = S this is continuity of the
tangent bundle of the manifold S at r_*.  For S' != S suppose x_n in S', x_n -> r_*, dist(v, T_{x_n} S') > eps |v|; by compactness of
the Grassmannian pass to a subsequence with T_{x_n} S' -> tau; by (W2), v in T_{r_*} S ⊂ tau, so dist(v, T_{x_n} S') -> dist(v, tau) =
0, a contradiction.  Since there are finitely many S', one delta works for all.
Step 2 (one piece).  On a stratum S' meeting B(r_*, 2 delta) let V_{S'}(x) := P_{T_x S'} v (orthogonal projection), a smooth (Nash)
tangent vector field on the Nash manifold S', with |V_{S'}(x)| <= |v| and |V_{S'}(x) - v| = dist(v, T_x S') <= eps |v| on
S' ∩ B(r_*, 2 delta).  Given x_0 in S' ∩ B(r_*, 2 delta) and a time budget tau_0 > 0, let gamma be the maximal integral curve of
V_{S'} in S' starting at x_0, restricted to [0, min(tau_0, tau_max)).  If tau_max < tau_0, then |gamma'| <= |v| makes gamma(s)
Cauchy as s -> tau_max; its limit x_1 lies in cl(S').  If x_1 were in S', a compact neighbourhood of x_1 in the locally compact
manifold S' would contain gamma(s) for s near tau_max, contradicting the escape lemma for maximal integral curves on manifolds.
Hence x_1 in cl(S') \ S', so x_1 lies in a stratum S'' with dim S'' < dim S' (W1).
Step 3 (concatenation).  Start at y (stratum S_0 := the stratum of y) with budget t.  Apply Step 2; if the curve stops at a
frontier point x_1 in S_1 (dim S_1 < dim S_0), continue from x_1 in S_1 with the remaining budget, and so on.  The dimensions
strictly decrease, so after at most dim Z + 1 pieces the budget is exhausted.  The concatenated curve gamma is Lipschitz, lies in
Z (each piece lies in a stratum, the junction points are in Z), satisfies |gamma'| <= |v| and |gamma' - v| <= eps|v| a.e. as long
as it stays in B(r_*, 2 delta); and it does stay there: |gamma(s) - y| <= |v| s <= delta/2, |y - r_*| < delta.  [A piece in a
stratum with dist(v, T S') <= eps |v| < |v| cannot be a point stratum, so no piece is stationary.]  QED

## 1.3 Proposition J1.11
PROPOSITION J1.11.  PROVED.  If Phi notin B^reg_kappa, there are c, h_0 > 0 with mu_Phi(h) >= c h for 0 < h <= h_0.
Consequently, for the T_fin weights Phi^T (and every pattern kappa of every level) the Puiseux exponent of Lemma QC(c) is
beta_kappa <= 1: mu_kappa(h) >= c_kappa h for 0 < h <= h_kappa.
Proof.  (i) Local decrease.  Let r_* in Lambda, D, S, v as in Lemma 1.1 (v != 0 since D != {}).  Every psi_d with d in D is real
analytic on an ambient neighbourhood of r_* (r_{*,d} != 0 and R_a^2 < 1 near K_kappa), and m_* := (1 - max_{d notin D}
psi_d(r_*)/Phi_d)/4 > 0 (put m_* := 1/4 if D = N_T).  Choose eps in (0, 1) with eps (1 + |v| max_{d in D} sup_{B(r_*,1)} |d psi_d|
/Phi_d) <= 1/4, then delta > 0 as in Lemma 1.2 and so small that on B(r_*, 2 delta): |d psi_d(x) - d psi_d(r_*)| |v| <= eps Phi_d (d in
D) and psi_d/Phi_d <= 1 - 2 m_* (d notin D).  For y in Z ∩ B(r_*, delta), 0 < t <= delta/(2|v|) and gamma from Lemma 1.2, for d in D:
 psi_d(gamma(t)) - psi_d(y) = int_0^t [d psi_d(r_*) v + (d psi_d(gamma) - d psi_d(r_*)) v + d psi_d(gamma)(gamma' - v)] ds
                           <= t Phi_d (-1 + eps + eps |v| |d psi_d|/Phi_d) <= -(3/4) t Phi_d.
Hence F(gamma(t)) <= max(F(y) - 3t/4, 1 - 2 m_*).
(ii) Covering.  Lambda is compact (closed in the compact Z).  If Lambda = {}, F < 1 on the compact Y_1, so F <= 1 - m_U there and
mu(h) >= m_U for all h > 0 (or Y_1 = {} and mu = 1).  Otherwise cover Lambda by finitely many balls B(r_*^i, delta_i) from (i),
U := their union.  On the compact set Y_1 \ U, F < 1 (F = 1 only on Lambda), so F <= 1 - m_U.  Put V := max_i |v_i|,
h_0 := min(min_i delta_i, min_i 8 m_*^i |v_i| / 3, m_U ... ) (any positive number below these).  Let r in Y_1, 0 < h <= h_0.  If r in
B(r_*^i, delta_i): take t := h/(2|v_i|) (<= delta_i/(2|v_i|)); gamma(t) in Z, |gamma(t) - r| <= |v_i| t = h/2 < h, and
F(gamma(t)) <= max(1 - 3h/(8|v_i|), 1 - 2 m_*^i) = 1 - 3h/(8|v_i|) <= 1 - 3h/(8V).  So G_h(r) <= 1 - 3h/(8V).  If r notin U: G_h(r) <= F(r)
<= 1 - m_U <= 1 - 3h/(8V) for h <= 8 V m_U/3.  Hence mu(h) >= c h with c := 3/(8V).
(iii) Genericity.  Let B^lin_kappa := {Phi in (0, inf)^{N_T} : there are no c, h_0 > 0 with mu_Phi(h) >= c h on (0, h_0]}.  The
condition "mu_Phi(h) >= c h" reads: for all r in Z with F_Phi(r) <= 1 and all e > 0 there is r'' in Z with |r'' - r| < h and
F_Phi(r'') < 1 - c h + e (or Y_1 = {} and 1 >= ch) -- first-order with parameters in k, so B^lin_kappa is semialgebraic and definable
over k [TS].  By (i)-(ii), B^lin_kappa ⊂ B^reg_kappa, hence dim B^lin_kappa < n.  By [GEN], Phi^T notin B^lin_kappa.  QED
Remarks.  (a) No reach/curvature bound on the strata is needed: the flow of the projected field never needs to stay in one stratum;
it may drop to lower strata (Lemma 1.2 Step 3), and Whitney (a) alone makes every stratum near r_* admit velocities within eps|v| of v.
This fills the gap in J1's sketch (J1 4.1 step (2), J1-ref B.4).  (b) The stratification need not be defined over k: dimension is
intrinsic, and the genericity step (iii) is applied to the k-definable set B^lin_kappa, which contains no reference to Sigma.
(c) If Lambda != {} then also mu(h) <= Lip_kappa h (cert1 Q1), so the exponent is exactly 1; if Lambda = {} the exponent is 0.
(d) The constants c, h_0 are design numbers of level L computed in (S5) of T_fin (cert1 6); with P-CHOICE, Design(L) >= max(1/c_kappa,
1/h_kappa), so  mu_kappa(eta'(w)/3) >= eta'(w)/(3 Design(L))  at every sub-window w of level L (eta'/3 <= 1/Design(L) <= h_kappa).

## 1.4 Consequence: the class (R-T) is empty (and KN-1 needs no exactness)
COROLLARY 1.3.  PROVED (modulo the chain cited by J1.15 and J2.1).  At every main stage L >= l_f, every sub-window w and class a,
condition (J-e) of Theorem J1.15' holds for every zero-data (KN-1) thick-type carrier of a (T)-block:
      mu_kappa(eta'/3) >= C D(L)^C m^2 (beta_*/kappa_m)^2.
Hence (R-T) is empty: a stage at which some thick-type carrier is KN-1 in a (T)-block is realized by J1.15' (band of half-width
beta_* on that carrier's row, J1.9, J1.10(c), J1.13(ii)).
Proof.  beta_* = 16 nu_1 (||b|| + 2 rho_0)/(c_* u) with ||b|| <= |Lambda_A|^{1/2} x + (pre-placement terms) and rho_0 = C_2 W^2 << x (K-7,
P-TU), x = C Design(L) eta'; c_*, nu_1, kappa_m, A_min, N, |Lambda_A| are bounded by Design(L)^C for L >= l_f (K2.16, K2.13).  So the
right side is <= Design(L)^{C'} eta'^2/u^2 (C' absolute).  By 1.3(d) the left side is >= eta'/(3 Design(L)).  The inequality holds
iff eta' <= u^2/(3 Design(L)^{C'+1}); since eta' = T^4/(L Design(L)) and T = T_lo(w) <= (u/(4 Design(L)))^{L^2 + 20} (window design,
cf. J1-ref P-TU), eta' <= (u/(4 Design))^{4L^2 + 80} <= u^2/Design^{C'+1}.  QED
Remarks.  (a) No design change is needed: J1.11 is a property of the existing generic weights; only the bookkeeping value
beta_kappa <= 1 is used.  (b) The same estimate shows that X1's KN-1 exactness (inactive nearly neutral values of (T)-blocks held
EXACTLY at 0, Q1-refb P-HOLD) can be relaxed to |value| <= kappa_m (mu_kappa(eta'/3)/(C D^C m^2))^{1/2}, which is >= eta'^{1/2}/Design^C
>> beta_*: the KN-1 rows of (T)-blocks are always band-legitimate (J1.10(c) holds unconditionally).
(c) With KN-1 rows relaxed, the joint fixed point of KN^tr no longer needs exact zeros of inactive values in (T)-blocks; nothing
else in the chain used the exactness (X1-ref KN-1: it was needed only because the exponent beta_kappa was not explicit).

## 1.5 Numerics (sanity only; H1_work/puiseux_toy.py, puiseux_toyA_fine.py, outputs *.out)
mu(h) computed via D(m) := max_{r in Y_1} dist(r, Z ∩ {F <= 1 - m}) (mu(h) >= m iff D(m) < h), psi_d with Lemma K's closed form.
 Toy A (Z = a CONE in R^3 with vertex near Lambda, N_T = 2 carriers): m/D(m) in [2.35, 4.26] for generic weights and in [2.35, 3.14] when
   the vertex lies on Lambda with both carriers active; fitted exponent on resolved scales 1.15 resp. 1.06 (linear margin; the cone is
   a union of lines through the vertex, so even the coincidence is first-order decreasable -- regularity is sufficient, not necessary).
 Toy B (Z = a CUSP in R^2 whose tangent at the tip is orthogonal to grad psi): coincidence weights (tip on Lambda; a critical
   0-dimensional stratum, i.e. Phi in B^reg) give mu(h) ~ h^{1.495} (exponent 3/2, as predicted by r(s) = c + s^2 t + s^3 n); weights
   perturbed by 1e-3 give m/D(m) -> 0.46 at small scales (exponent 1.05-1.07).  So genericity is necessary for exponent 1 and
   sufficient, as proved.
