# U1 part 2 — The shifted exact cone, a shift bound, normalization to ONE shift ray, subset averaging, exactification

Setting of part 1.  w = (l, i) is a clean sub-window of a MAIN level l (part 3) of D^{U1}, l >= l_f; t ranges over the dyadic scales of
W(w); (B_+-, Theta_+-) is a two-sided decomposition of g in C(f) at scale t; V1's classification (2.2), its moves (C1)-(C3), Lemmas
D, ST, NS, RR are used verbatim (refereed).  K denotes constants of the form C_f (Design(l)/u(w))^{C}; they are absorbed by the window
arithmetic (Q(w) of part 3).  "Decomposition convention": delta_m := Delta d_m M_m (Delta d = d_+ - d_-); "data convention":
Delta_m := d(omega^-) - d(omega^+), Delta'_m := Delta_m M^#_m.  Matching: Delta'_m <-> -delta_m (V2-ref 9(g)).

## 2.1 The shifted exact cone Gamma^# of a pattern
Let f^# be the companion of part 4 (V1's moves, the realization moves of 2.5, the fine structure and the absorbers).  Put
Omega := all coarse strict non-peaks of f^# (kept, clamped and class-R ones; every carrier of V1's Kp(w) is one, V1 Lemma ST(c)), and
coarse PEAKS of f^# with their signs vs_l.  For (Delta', gamma) in R^I x R^Omega define the coarse vector
    L(Delta', gamma) := sum_{l in Omega} gamma_l u_l - sum_m Delta'_m sum_{l coarse peak of f^#, m(l) = m} vs_l lambda_l u_l
restricted to the COARSE coordinates E_c := T(l) ∪ union_{l'' <= l} (S_{l''} ∩ [1, s_far(w)]) minus F^#, where s_far(w) is the least s with
2^{-s} <= c_{l+1}^2 (<= b(w)^4; part 3).  (Every coarse carrier is either a strict non-peak of f^#, hence in Omega (nearly neutral carriers exactified to
w^# = 0 by V2 Theorem B are strict non-peaks of value 0), or a peak of f^#, entering through its trace.)  Gamma^#(kappa) is the set of
(Delta', gamma) with
 (X1) L(Delta', gamma) is z^#-admissible on E_c (zero at free coordinates, z^#-signed at contacts);
 (X2) eps_l gamma_l >= 0 is implied by (X1) at the contacts of S^nat_l for class-G l in Omega; Delta'_m eps_l vs_l <= 0 for class-G peaks
      (implied by (X1) on S^nat_l likewise); gamma_l = 0 for class-R l in Omega (implied by (X1) at the free coordinates of S^nat_l);
 (X3) Delta'_m kappa^#_m(Omega) = sum_{l in Omega_m} u_l(zhat^#) gamma_l   (Lemma 1.3);
 (X4) vs_l gamma_l >= 0 ... the inward sign rows of the kind-[3] carriers (V1 TR(iii)) written for the - side increment (see 2.4);
 (X5) for an ACTIVITY CLASS a (2.3): gamma_l = 0 and Delta'_m = 0 for the components declared inactive in a.
Gamma^#(kappa, a) is a polyhedral cone.  By Lemma 1.3 its coefficients are design numbers lambda_l u_l(j), signs, the values u_l(zhat^#)
(l in Omega) and one scalar kappa^#_m per block; the pattern kappa = (Omega, peaks, signs, types of E_c-coordinates at f^#, activity
class) ranges over a design-countable, N-free set (subsets of [1,l] and of E_c, sign vectors).
Fine carriers do not appear in Gamma^#: their contributions to V(Domega) on E_c are the FINE RESIDUES absorbed in part 3, and on the
fine coordinates they are made admissible by the fine structure of part 4.

## 2.2 Lemma 2.1 (data shifts are bounded).  PROVED.
Let (b^+-, omega^+-) be two-piece data at a first row f' with Gamma'_w <= 2.  Then for every block m
    |Delta_m| <= ( 8 C'^3_m / (sigma'_m M'^2_m Phi_{P'_m}^2) )^{1/2}.
Proof.  Domega := omega^- - omega^+ is supported in Omega_m ⊂ Q'_m and H_m(omega^+-) <= 2/sigma'_m, so (sqrt H is a seminorm)
H_m(Domega) <= 8/sigma'_m.  Write D Domega = a D(w'1_Omega) + y with y ⊥ D(w'1_Omega) (in l_2(Omega)), and chi := ||D w' 1_Omega||^2/C'^2.
Then Delta = d'(Domega) = <D w' 1_Omega, D Domega>/C' = a C' chi, and ||P^perp D Domega||^2 = ||D Domega||^2 - <Dw', D Domega>^2/C'^2 >=
a^2 C'^2 chi (1 - chi), i.e. H(Domega) >= a^2 C' chi(1 - chi).  Hence Delta^2 <= H(Domega) C' chi/(1 - chi), and 1 - chi >= ||D w' 1_{P'}||^2/C'^2
= M'^2 Phi_P^2/C'^2 because Omega ⊂ Q'.  QED
At the companions f^# of the windows of f, C^#, sigma^#, M^# are within C Design Lam of those of f (V1 Lemma CO) and P^# contains a fixed
non-degenerate peak c_0 of every block of f (margins persist), so |Delta'_m| <= Delta_max := C_f (an f-constant) for all data with Gamma <= 2.

## 2.3 Activity classes (pigeonhole over finitely many classes).  PROVED.
Let J(w) := |Omega| + N (number of components of (gamma, Delta')), and fix thresholds A_1 < A_2 < ... < A_{J+2} with A_{i+1} := K_* A_i,
A_1 := K_*, K_* := the constant of the projection in 2.4 (a constant K of the above form).  For a projected data vector (2.4) at scale t,
among the J+1 intervals [A_i K t, A_{i+1} K t) (1 <= i <= J+1) one contains no |component|; let i(t) be the least such i.  The ACTIVITY
CLASS of t is a(t) := (i(t), the set of components with |.| >= A_{i(t)+1} K t, their signs).  Components below A_{i(t)} K t are set to 0
(cost <= J A_{i(t)} K t, again of the form K t).  The number of classes is <= (J+1) 3^J, a design number.
Proof.  Pigeonhole (J components, J+1 intervals).  QED

## 2.4 Proposition 2.2 (projection onto Gamma^#, normalization to one shift ray).  PROVED (modulo V1 TR, refereed, for the routine steps).
For every scale t of W(w) let (Delta'_dec(t), gamma_dec(t)) be the coarse data read off the decomposition: Delta'_m := -delta_m (blocks of
I_sh(w)), := 0 for the other blocks (|delta_m| <= K_d t there, V1 Lemma 3.4'); gamma_dec,l := -Delta theta_l (l in Omega).  Then:
(a) the violations of (X1)-(X4) by (Delta'_dec, gamma_dec) at the coefficients of f^# are <= K t;
(b) by Lemma H (V2) and the exactification of 2.5 (all minors of Gamma^#(kappa, a) are 0 or >= u(w)/Design(l)^C), the l_1-projection onto
    Gamma^#(kappa, a(t)) moves (Delta'_dec, gamma_dec) by <= K t;
(c) NORMALIZATION.  Let g_1, ..., g_p be the nonzero Delta'-projections of the extreme rays r_1, ..., r_p of Gamma^#(kappa, a)
    (normalized ||r_j||_1 = 1).  Write each projected Delta'(t) = sum_j a_j(t) g_j with a(t) in [0, A_max]^p, chosen by a fixed rule
    (a basic solution, Caratheodory); A_max <= C_f (Design/u)^C (inverse of a nonsingular design/value matrix with minors >= u/Design^C,
    and |Delta'(t)| <= Delta_max by Lemma 2.1).  Partition [0, A_max]^p into cubes of side epsilon; for a set S of scales whose
    coefficient vectors a(t) lie in ONE cube with corner a^max (coordinatewise maximum over the cube), put
        Delta'^* := sum_j a^max_j g_j,      incr(t) := sum_j (a^max_j - a_j(t)) r_j  in Gamma^#(kappa, a),
    so that Delta'(t) + Delta'(incr(t)) = Delta'^* for every t in S and ||incr(t)||_1 <= p epsilon.
(d) The number of (activity class, cube) pairs is <= D_cls(w) := (J+1) 3^J (A_max/epsilon)^p, a quantity of the form (Design(l)/u(w))^{C'}
    once epsilon := c_f (u/Design)^C is fixed by (e).
(e) DATA with the common shift.  For t in S define, as in V1 Proposition TR Steps 4-5 (split, data, balancing; banks, pulls, donors):
    omega^+ := the clamped decomposition omega_+ (V1 Step 5), Domega(t) := the vector with gamma = gamma_proj(t) + gamma(incr(t)) on Omega and
    shift Delta'^* (i.e. Domega(k) = gamma_k/lambda_k + Delta_m w^#(k), Delta_m := Delta'^*_m/M^#_m), plus the absorber coefficients of part 3
    and the far parts fixed in part 4; omega^- := omega^+ + Domega(t); b^+ := beta + chi V_proj (V1 Step 4, the split of the + side of the
    decomposition with respect to the PROJECTED coarse vector) + chi_f V_fine (any chi_f in [0,1] on the fine contacts); b^- := b^+ - V(Domega(t)).
    Then (b^+-, omega^+-) are exact two-piece data at f^# (Lemma 1.1(c)) with Delta' = Delta'^* for every t in S, p*(g - g_t) <= K t, the
    + side coincides with V1's + side up to K t, and sqrt(Gamma^#_w(b^-, omega^-)) <= sqrt(Gamma^#_w(B_-, Theta_-)) + K t + C_f p epsilon.
    With epsilon := c_f (u/Design)^C small enough, kappa_w <= 1 + eta_0/2 (as in V1 4.3).
Proof.  (a) As V1 TR Step 1-2: (X1) at E_c-coordinates of f: the budget lem:switchbudget at f gives sum phi_z(Delta B) <= t/q_0; Delta B =
-sum_l Delta theta_l u_l; the coarse part is L(Delta'_dec, gamma_dec) up to (i) the peak errors e_k vs_k lambda_k (eq:peakshift; e_k <=
t/(lambda_k mu_k) <= C_f D t/u at peaks with rho >= 1+u; tiny-margin peaks of f are (K4) carriers, strict non-peaks of f^#, hence in Omega),
(ii) class-R carriers (sum |Delta theta| <= K_g t, V1 (3.1), no shift bound needed), (iii) fine carriers (<= 3 b^2/t), (iv) the
difference between z and z^# on E_c (closed tiny rooms: V1 TR Step 4 bound), (v) the change of the coefficients from f to f^# (values and
kappa move by <= C Design b + realization moves <= T_lo^4, times ||gamma|| <= 12 sum lambda/t, giving <= T_lo^3).  (X3): eq:didentity at f
with the peaks' traces (proof of Lemma 1.3 applied to the decomposition, V2-ref 9(g)); its error is <= K t.  (X4): Lemma lem:suplevel(f).
(b) Lemma H (V2, refereed): the l_1 Hoffman constant of a system whose nonzero minors are >= mu and entries <= 1 is <= C (dim)^C mu^{-1}...;
exactly as in V2 Corollary B.1.  (c) Gamma^# = cone(r_1, ..., r_p) (Minkowski-Weyl, pointed after splitting free variables), so its
Delta'-projection is cone(g_1, ..., g_p); a basic representation uses linearly independent g_J, a_J = (g_J)^+ Delta'(t), and the entries of
(g_J)^+ are ratios of minors of the design/value matrix (Cramer), bounded by (Design/u)^C after exactification.  incr(t) is a nonnegative
combination of extreme rays, hence in Gamma^#(kappa, a); its Delta'-projection is sum (a^max - a(t)) g_j.  (d) Count.  (e) Lemma 1.1(c)
with V := V(Domega(t)) 1_{F^#c}: on E_c it equals L(Delta'^*, gamma(t)) (exact by (X1) for Gamma^#) plus the fine residue, which the
absorbers cancel EXACTLY (part 3); on the fine coordinates it is admissible by the fine structure built for the ray Delta'^* and the
activity class a (part 4); the active far parts of Omega-carriers are dominated by gamma_l (part 4, Lemma 4.2).  The + side is V1's
(projected) + side, so p*(g - g_t) <= K t as in V1 TR Step 5 (the new terms: projection K t, inactive components zeroed J A K t, fine
part ||V_fine||_1 <= C_f b^2 and absorber coefficients <= C_f b^2).  The - side differs from V1's by V(incr(t))|_{E_c} (on the base) and
Domega(incr(t)) (on the blocks); sqrt(Gamma) is a seminorm, and Gamma^#_w(V(r_j), Domega(r_j)) <= C_f for the normalized rays (q_0 h(y) <=
||U||^2 ||y||_1^2/nu, sigma H(x) <= (sum lambda |x|)^2/C).  The size conditions (V1 TR(iii)): incr(t) satisfies the homogeneous inward rows
(X4), so kind [3] is preserved; |Domega(incr)| <= C_f p epsilon / min lambda_Omega <= A_2/t for t <= T_hi(w).  QED

Remark (what 2.2 achieves).  Within one class S, every scale carries exact data with the SAME shift Delta'^*: the fine structure has to
handle ONE ray (gap C*-4 of V2-ref closed), and the averaged data have shift exactly Delta'^*.  Only the - side pays, by O(epsilon) in sqrt
Gamma; the + side, which defines the represented functional g_t, is untouched.  The increments are admissible on the - side precisely
because V(incr) is z^#-admissible: b^- - V(incr) stays (-z^#)-signed (Lemma 1.1(b)).

## 2.5 Theorem 2.3 (exactification of Gamma^# with the single scalar kappa).  PROVED (V2 Lemma L + Lemma TU + Lemma 1.5).
Enlarge the rate scheme of D^{V2} by the objects "minor of Gamma^#(kappa, a)" for all patterns and activity classes of level l (each a
polynomial with design coefficients in the variables (u_l(zhat))_{l in Omega} and (kappa_m)_m, evaluated at f), and let b(w) be a design
power of T_lo(w) absorbing the Lojasiewicz exponents of these finitely many polynomial systems (V2 Def. 2.2).  At a clean w, after V1's
moves (C1)-(C3) (which move values and kappa by <= Design b), there is a point (u'_Omega, kappa') within C_L(Design b)^{1/N_L} <= T_lo^4 of
the current one at which every tiny minor vanishes; it is REALIZED exactly by (i) Lemma TU (V1, refereed: pulls and private banks on the
far parts of the signature sets of the carriers of Omega, two-sided, exact) for the values, then (ii) in every block one push of
Lemma 1.5 (buffer peak or robust dropped strict non-peak; none of them in Omega), whose amount solves kappa_m = kappa'_m by the
intermediate value theorem (kappa_m is continuous and strictly monotone in the push with derivative >= min(1/2, u)).  Robust minors move
by <= Lip x T_lo^4 << u.  Consequently every minor of Gamma^#(kappa, a) at f^# is 0 or >= u/(2 Design^C), and Lemma H gives the Hoffman
constants used in 2.4(b), (c).
Proof.  Lemma L (V2, refereed) applied to the finite family of tiny minors (polynomials in (u_Omega, kappa) with design coefficients).
The pushes of (ii) change the values u_Omega only at second order through the Hilbert part (diagonal base, V1 Lemma B(i)); re-solve (i)
and (ii) jointly: the Jacobian of (u_Omega, kappa) with respect to (Lemma TU parameters, push amounts) is block triangular with identity
and diagonal (dkappa/ds >= min(1/2, u)) blocks, so V1's explicit fixed point (Lemma TU, Step 2) extended by one scalar equation per block
converges (contraction constant <= C Design eta, eta <= T_lo^4).  Status stability, costs: V1 Lemmas ST, CO with eta <= T_lo^4 << Lam.  QED
This closes (C*-3): only ONE block scalar enters (Lemma 1.3), and Lemma 1.5 always provides a push not belonging to Omega.

## 2.6 Lemma 2.4 (windowed averaging on a subset of scales).  PROVED.
Theorem E (Z3), E'' (V1) and E_RT (V3) remain valid if the averaging set {T_j 2^{1-i} : 1 <= i <= n_j} is replaced by any subset S_j of it with
|S_j| =: n'_j, provided n'_j >= 48 rho^2 K_j/(c_flat,j (1 - rho^2)) and K_j T_j / n'_j -> 0.
Proof.  In the proof of Theorem E (Z3 2.2 / V3 2.5) the set of scales enters at three places: (A) for rho|r| <= c_flat t; the set I_r :=
{t in S_j : c_flat t < rho|r|} satisfies sum_{I_r} t <= sum of ALL dyadic t < rho|r|/c_flat <= 2 rho |r|/c_flat; if I_r is empty every term
obeys (A); otherwise rho|r| > c_flat min S_j >= c_flat T_j 2^{-n_j}, which is all that the scale-decoupling condition uses; the averaged
error is (1/n'_j) sum_{I_r} rho|r| K t <= 2 rho^2 K r^2/(c_flat n'_j); and for |r| >= r_0, (1/n'_j) sum_{S_j} rho |r| K t <= 2 rho|r| K T_j/n'_j.
Averaging of the data over S_j preserves exactness, the side conditions and the common shift.  QED
With D_cls(w) <= (Design/u)^{C'} classes, some class contains n'(w) >= n(w)/D_cls(w) scales, and n(w)/D_cls(w) >= l 2^{l^3} Q(w)/D_cls(w)
-> infinity faster than any K of the above form once Q(w) dominates D_cls(w) x (Design/u)^C (design requirement of part 3).
