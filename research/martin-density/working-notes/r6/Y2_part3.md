# Y2 part 3: companions with raised thresholds (Lemma U', Theorem E', Proposition Q)

Setting: I finite, f in S_{p*} with F = supp a finite, g in C(f), rho in (0,1), eta_0 in (0,2] with rho^2(1+eta_0) <= (1+rho^2)/2.

## 3.1 Inward-only data
For a first row f (or a companion f_j) a pair (b, omega) is **side-+ admissible with inward coordinates** if it is side-+ admissible
(Definition def:twopiece) except that omega_m may also be nonzero on finitely many coordinates k that are degenerate peaks or
strict non-peaks of block m, with varsigma_k omega_m(k) <= 0 (varsigma_k := sgn w_m(k)); side - with varsigma_k omega_m(k) >= 0.
In both cases d_m(omega_m) := <D_m w_m, D_m omega_m>/C_m and the pair represents b + sum_m R_m^*(omega_m - d_m(omega_m) w_m).
Since alpha_m vanishes at degenerate peaks and off P_m, Lemma lem:algebra (first-order terms vanish) holds for such pairs.

**Lemma U' (uniform one-sided transfer with inward coordinates).  PROVED.**  Let f_j -> f in S_{p*} with supp a_j = F for all j.
For every eps_tr > 0 and A_0 >= 1 there are t_1 > 0 and j_0, and for every A_2 >= 1 and gamma_B in (0,1] a number
c_flat = c_flat(A_2, gamma_B) in (0, 1/8] with c_flat >= c_0 gamma_B/A_2 (c_0 > 0 depending only on f, eps_tr, A_0), such that for
j >= j_0, t in (0, t_1] and every side-+ (resp. side--) admissible pair with inward coordinates (b, omega) AT f_j with b(xi_j) = 0,
t||b||_1 <= A_0, Gamma^{(j)}_w(b, omega) <= 2, and every k in supp omega_m satisfying one of
  [1] gap^{(j)}_m(k) >= t^2/2 and |omega_m(k)| <= 3 gap^{(j)}_m(k)/t;
  [2] gap^{(j)}_m(k) >= gamma_B and |omega_m(k)| <= A_2/t;
  [3] k an inward coordinate (degenerate peak or strict non-peak of f_j, inward sign for the side) with |omega_m(k)| <= A_2/t,
the functional G := b + sum_m R_m^*(omega_m - d^{(j)}_m(omega_m) w_{j,m}) satisfies p*(f_j + rG) <= 1 + (r^2/2)(Gamma^{(j)}_w(b,omega) + eps_tr)
for 0 < r <= c_flat t (resp. -c_flat t <= r < 0).
*Proof.* This is Lemma U of Z3 (proved there by inspection of Lemmas lem:uniformtransfer, lem:onesidedtransfer) with three changes,
each checked against those proofs.  (i) The constant 2 in [1] is replaced by 3 and t^2 by t^2/2: in the block step the radius condition
|r omega_m(k)| <= gap/2 needs c_flat <= 1/6 (instead of 1/4); nothing else uses the constant.  (ii) Coordinates of kind [3]: in the block
step, Lemma lem:block(c),(d) needs ||W||_inf = (1 - rd)M with W := (1 - rd) w + r omega (d := d^{(j)}_m(omega_m)); at a kind-[3]
coordinate on side +, varsigma_k W(k) = (1 - rd)|w(k)| + r varsigma_k omega(k) <= (1-rd)|w(k)| <= (1-rd)M, and varsigma_k W(k) >=
(1-rd)|w(k)| - c_flat A_2 >= -(1-rd)M as soon as c_flat A_2 <= M/4 (|rd| <= 1/2); the maximum (1-rd)M is attained at the peaks with
alpha != 0, where omega = 0.  This is Lemma 2.1 of the Z6 referee notes (third kind) with A' := A_2; side - is symmetric.  The
first-order term vanishes since alpha(k) = 0 there.  (iii) Dependence of the constants: as recorded in Step 7 of Z4 (verified by the
Z4 referee, Section 8 of Z4_ref_notes), A_2 and gamma_B enter only through upper bounds on c_flat (c_flat <= gamma_B/(2A_2),
c_flat <= C_min/(2A_3), c_flat A_2 <= M_min/4, and O(A_3 c_flat) relative errors with A_3 := 2 + 2A_2), while t_1 is constrained only by
terms of order r^4 (|r| <= c_flat t <= t) and by the transfer data, and j_0 only by the convergence of the scalar data and of the
transfer data of f_j to those of f (Lemma lem:persistence); none of these involves A_2 or gamma_B.  QED

## 3.2 Theorem E with window-dependent constants
**Theorem E'.  PROVED.**  Theorem E of Z3 (statement recalled in Z3_notes 2.2) remains true if (E-b) is read with Lemma U' and with
window-dependent constants A_2 = A_2(j), gamma_B = gamma_B(j) (A_0 fixed), and (E-d), (E-e) are replaced by
  (E-d') K_j T_j -> 0 and n_j >= 48 rho^2 K_j/(c_{flat,j}(1 - rho^2)) for all large j, where c_{flat,j} := c_flat(A_2(j), gamma_B(j));
  (E-e') eps_j := p*(f_j - f) <= min{ c_{flat,j}^2 (1-rho^2)(T_j 2^{-n_j})^2/(24 rho^2), (1-rho^2) r_0^2/6 } for large j (r_0^2 := 1-rho^2).
*Proof.* In the proof of Theorem E (Z3 2.2) the window index j is fixed from the second sentence on, and c_flat enters only through
(A) (Lemma U at f_j for the scales t_i), the set I_r := {i : c_flat t_i < rho|r|} with sum_{I_r} t_i < 2 rho|r|/c_flat, the bound
2 rho^2 K r^2/(c_flat n) <= (1-rho^2) r^2/24, and the inequality eps_j < theta_j rho^2 r^2/c_flat^2 <= (1-rho^2) r^2/24 when I_r != {}
(there rho|r| > c_flat t_n).  With c_flat := c_{flat,j} these are exactly (E-d'), (E-e').  The final step (averaged data are d-neutral
two-piece data at f_j, Corollary cor:D1 at f_j) does not involve c_flat.  When inward coordinates of kind [3] occur, they are strict
non-peaks of f_j (we shall only use this case), so the averaged data are two-piece data at f_j in the sense of Definition def:twopiece
and Corollary cor:D1 applies verbatim.  QED

## 3.3 Companions with raised thresholds
Now T is an SLD-type design: Definition def:SLD, or its modifications SLD_G (made N-free), D''' or the explosive design; only (T-a)-(T-d),
(P1)-(P3) and allowedness (a),(b) are used.  Recall v_l := delta_l h_l/n_l (u_l = v_l on S_l), lambda_l = m(l) Phi_{m(l)}(k(l)) <= c_l/4.

**Definition (window data with inward degenerate peaks).**  For a window index l_j and the n_j dyadic scales t of W(l_j) let
(b^+-_t, omega^+-_t) be pairs AT f with: (W1) both represent the same functional g_t at f and are d-neutral: b^+_t - b^-_t =
sum_m R_m^*(omega^-_{t,m} - omega^+_{t,m}) and d_m(omega^-_{t,m}) = d_m(omega^+_{t,m}) for all m; (W2) (b^+_t, omega^+_t) is side-+ and
(b^-_t, omega^-_t) side-- admissible with inward coordinates, the inward coordinates being degenerate peaks of f (set D_t); (W3) b^+-_t(xi) = 0,
t||b^+-_t||_1 <= A_0, Gamma_w(b^+-_t, omega^+-_t) <= 1 + eta_0/4; (W4) every k in supp omega^+-_{t,m} \ D_t has gap_m(k) >= t^2 and
|omega| <= 2 gap/t, or gap_m(k) >= gamma_B(j) and |omega| <= A_2(j)/t; and |omega^+-_{t,m}(k)| <= A_2(j)/t on D_t; (W5) p*(g - g_t) <= K_j t.
Let Sw_j be the (finite) set of carriers l with k(l) in supp(omega^-_{t,m} - omega^+_{t,m}) for some scale t of the window (the switching
carriers), Bl_j the set of carriers with k(l) in the support of some omega^+-_t, and Ba_j := F ∪ union_t (supp b^+_t ∪ supp b^-_t).

**Definition (donor).**  A carrier l' of block m is a *donor for window j* if l' notin Sw_j and the set S_{l'} \ (F ∪ Ba_j ∪ T_j), where
T_j := union_{l in Sw_j} supp y_l (finite), contains INFINITELY many coordinates s admitting a *raising move*: a number delta_s != 0
with |z_s + delta_s| <= 1 and either k(l') in P_m and sgn(delta_s) = varsigma_{k(l')} (|u_{l'}(zhat)| increases), or k(l') in Q_m,
w_m(k(l')) != 0 and sgn(delta_s) = -sgn w_m(k(l')) (|u_{l'}(zhat)| decreases), or k(l') a degenerate peak (any sign; then
|u_{l'}(zhat)| > 0 changes).  For a raising coordinate, sgn u_{l'}(zhat) = varsigma_{k(l')} (Lemma lem:threshold: sgn zeta(k) = sgn w(k)
when w(k) != 0, and u_{l'} = v_{l'} >= 0 on S_{l'}), so the stated sign of delta_s does move |u_{l'}(zhat)| as indicated.
(For l' notin Sw_j, the coordinates of S_{l'} lie in no signature set of a carrier of Sw_j, so s notin supp u_l for l in Sw_j iff
s notin T_j.  A donor may belong to Bl_j \ Sw_j, e.g. a good coarse strict non-peak used by the window certificate.)  For the window data of part 4 (built from Lemma lem:windowtwopiece / Z4 Step 6), Ba_j ⊂ F ∪ T'_j ∪ union_{l in Sw_j} S_l
with T'_j finite, so Ba_j ∩ S_{l'} is finite for l' notin Sw_j.

**Proposition Q (companion transfer).  PROVED.**  Let T be an SLD-type design, f, g, rho, eta_0 as above, and suppose that along window
indices l_j -> infinity there are window data with inward degenerate peaks (W1)-(W5) such that (E-d') holds with T_j := T_hi(l_j),
n_j := n^w_{l_j}, and for every j and every block m with D_t ∩ (block m) != {} for some scale t of window j there is a donor for window j
in block m.  Then (f, rho g) in cl NA((c_0,p),l_2^2).

*Proof.* Fix j.  All window data of window j are fixed; we construct a companion f_j and verify Theorem E' at f_j.
Step 1 (the companion).  Let I_D be the set of blocks containing inward coordinates of window j; for m in I_D let l'_m be a donor
for window j in block m and k'_m := k(l'_m).  Let X_j be the finite set of target coordinates of the donors, union_m supp y_{l'_m}.
Choose raising coordinates s_m in S_{l'_m} \ (F ∪ Ba_j ∪ T_j ∪ X_j) with s_m >= m + k'_m + r (r fixed in Step 2; possible since infinitely
many raising coordinates are available), with raising signs sigma_m, and put delta := sum_{m in I_D} eta_m sigma_m e_{s_m}, eta_m > 0 small
(so |z_{s_m} + eta_m sigma_m| <= 1).  Let f_j be the first row with forced data (a, z + delta) (Remark rem:lemmaZ(c); admissible since
|z + delta| <= 1 and z + delta = z = sgn a on F).  Its data: a_j = a, e_j = e, nu_j = nu, zhat_j = zhat + delta, xi_j = q_0^{(j)} zhat_j,
w_{j,m} = J_m(R_m^** zhat_j).  Convergence as max eta_m -> 0: ||R_m^** zhat_j - R_m^** zhat||_1 = sum_k lambda_{k,m} |u_{k,m}(delta)| <=
|I_D| max_m eta_m (|u| <= 1 coordinatewise, sum_k lambda_{k,m} <= 1); so q_0^{(j)} -> q_0, sigma_{j,m} -> sigma_m; every weak* cluster point
w~ of (w_{j,m}) has N_m(w~) <= 1 and w~(R_m^** zhat) = lim |R_m^** zhat_j|_m = |R_m^** zhat|_m, hence w~ = w_m (|.|_m is smooth), so
w_{j,m} -> w_m weak*, D_m w_{j,m} -> D_m w_m in l_2 (Phi_m in l_2), C_{j,m} -> C_m, M_{j,m} -> M_m, L^* w_j -> L^* w in norm (L compact),
and f_j = a + L^* w_j -> f in norm.
Step 2 (thresholds rise in I_D).  Fix m in I_D, zeta := R_m^** zhat, zeta' := R_m^** zhat_j.  The coordinate k'_m changes by
Delta_m := lambda_{l'_m} v_{l'_m}(s_m) eta_m in the raising direction (only u_{l'_m} among signatures lives on s_m).  Every other change of
zeta comes from targets: zeta'(k) - zeta(k) = lambda_l sum_{m'} y_l(s_{m'}) eta_{m'} sigma_{m'}/n_l for carriers l of block m with
s_{m'} in supp y_l; by allowedness (a) such l exceed l'_{m'}, and by allowedness (b) 2c_l <= 2^{-2 s_{m'}} c_{l'_{m'}} delta_{l'_{m'}}.  With
||y_l||_inf <= 1, n_l >= 3/4, lambda_l <= c_l/4, sum_{l >= L} c_l <= (4/3) c_L:
   E_m := sum_{k != k'_m} |zeta'(k) - zeta(k)| <= sum_{m'} (4/3)(1/4)(4/3)(1/2) 2^{-2 s_{m'}} c_{l'_{m'}} delta_{l'_{m'}} eta_{m'}
        <= sum_{m'} (2/9) 2^{-2 s_{m'}} c_{l'_{m'}} delta_{l'_{m'}} eta_{m'}.
Since Delta_{m'} = m' 2^{-m'-k'_{m'}} c_{l'_{m'}} delta_{l'_{m'}} 2^{-s_{m'}} eta_{m'}/n_{l'_{m'}} >= (4/5) 2^{-m'-k'_{m'}-s_{m'}} c delta eta, each
term is at most (5/18) 2^{m'+k'_{m'}-s_{m'}} Delta_{m'} <= 2^{-r} Delta_{m'}.  Choose eta_{m'} so that all Delta_{m'} are equal (= Delta); then
E_m <= N 2^{-r} Delta.  Lemma T(e) gives theta(zeta') > theta(zeta) provided N 2^{-r} < A/(A + theta) in case (i')/(iii, increase), or
N 2^{-r} < nu_{k'_m}/(2(A + theta)) in case (ii')/(iii, decrease) (A = |zeta|, theta = theta(zeta), nu_{k'} > 0 for a donor); fix r
accordingly (it depends on f and the donors only, not on eta).  So for EVERY choice of the common size Delta > 0 the thresholds of all
blocks in I_D rise strictly.
Step 3 (the data at f_j).  Let Delta be so small that the finitely many continuity requirements below hold.
(a) Values of switching carriers are unchanged: for l in Sw_j, s_{m'} notin supp u_l (s_{m'} notin T_j and s_{m'} lies in the signature set
of a donor, which is not in Sw_j), so u_l(zhat_j) = u_l(zhat) and zeta'(k(l)) = zeta(k(l)).  The values of the carriers of Bl_j \ Sw_j
change by at most Delta + E_m (Step 2), which tends to 0 with Delta.
(b) Inward coordinates become strict non-peaks: for k in D_t ∩ block m, nu_k = theta(zeta) (degenerate, Lemma T(a)), and nu'_k = nu_k <
theta(zeta'), so k is a strict non-peak of f_j (Lemma T(a) at f_j) with the same sign varsigma_k; the inward sign conditions are
unchanged, so these are kind-[3] coordinates of Lemma U'.
(c) Other used coordinates: finitely many strict non-peaks of f with gap >= min(t_{n_j}^2, gamma_B(j)) > 0; by coordinatewise convergence of
w_j and M_j they are strict non-peaks of f_j with gap^{(j)} >= gap/(1.5) -- hence of kind [1] or [2] of Lemma U' (constants 3 and t^2/2).
(d) Exact d-neutrality and the representations at f_j: for k in the support of omega^-_{t,m} - omega^+_{t,m} (strict non-peaks of f,
or degenerate peaks), Lemma lem:threshold gives Phi_k^2 w_m(k)/C_m = zeta(k)/|zeta| at f, and at f_j (strict non-peaks)
Phi_k^2 w_{j,m}(k)/C_{j,m} = zeta'(k)/|zeta'| = zeta(k)/|zeta'|.  Hence d^{(j)}_m(omega^-_t - omega^+_t) = (|zeta|/|zeta'|) d_m(omega^-_t -
omega^+_t) = 0, and b^+_t - b^-_t = sum_m R_m^*(omega^-_t - omega^+_t) (an identity independent of the first row) shows that both pairs
represent the same functional G_{j,t} := b^+_t + sum_m R_m^*(omega^+_t - d^{(j)}_m(omega^+_t) w_{j,m}) at f_j, with Delta d^{(j)} = 0.
(e) Side conditions at f_j: K_j ⊇ K \ {s_m}, z + delta = z on Ba_j, and b^+-_t vanish off F ∪ K and are z-signed on K; since
supp b^+-_t ∩ {s_m} = {}, they are side-admissible at f_j.  Block parts: kinds [1],[2],[3] by (b),(c).
(f) b^+-_t(xi_j) = 0: b^+_t(zhat_j) = b^+_t(zhat) + sum_m eta_m sigma_m b^+_t(s_m) = 0, and b^-_t(xi_j) = G_{j,t}(xi_j) = b^+_t(xi_j) because the
block parts are orthogonal to R_m xi_j (Lemma lem:algebra at f_j).
(g) Gamma at f_j: h^{(j)} = h (a, e, nu unchanged), H^{(j)}_m(omega) = ||P^perp_{j,m} D_m omega||^2/C_{j,m} -> H_m(omega) for fixed omega
(D_m w_{j,m} -> D_m w_m), q_0^{(j)} -> q_0, sigma_{j,m} -> sigma_m; so Gamma^{(j)}_w(b^+-_t, omega^+-_t) <= 1 + eta_0/2 for Delta small.
(h) p*(g - G_{j,t}) <= (K_j + 1) t: G_{j,t} - g_t = sum_m R_m^*(d_m(omega^+_t) w_m - d^{(j)}_m(omega^+_t) w_{j,m}) -> 0 in norm (d^{(j)} -> d on the
finitely supported omega^+_t, R_m^* w_{j,m} -> R_m^* w_m in norm); take Delta so small that it is <= t_{n_j} for all scales.
(i) eps_j := p*(f_j - f) satisfies (E-e') for Delta small (f_j -> f).
Step 4.  Along j, f_j -> f and supp a_j = F; Lemma U' applies for j >= j_0 (closeness of f_j to f is ours to choose).  Hypotheses (E-a),
(E-b) (with Lemma U'), (E-c) with K_j + 1, (E-d'), (E-e') of Theorem E' hold, and Theorem E' gives (f, rho g) in cl NA.  QED

Remarks.  (1) The gap of the inward coordinates at f_j is arbitrarily small; Corollary cor:D1 at f_j does not need any lower bound
(the averaged data are FIXED before the engineered approximants of f_j are built).  This is why steering at f_j is free while steering at
an engineered approximant of f is not (part 1, Section 1).  (2) The companion moves z only at donor coordinates, which carry no data and
lie outside the supports of all used carriers: the values u_l(zhat) of used carriers, the base part e, and hence exact d-neutrality are
preserved (only a common factor |zeta|/|zeta'| per block appears).  (3) Nothing about the status of f_j matters (f_j need not be in
any recovered class; the donor's own signature set acquires tiny room, which is irrelevant).

## 3.4 Peak-carrying version of Corollary cor:D1 (answer to item (1))
**Corollary Q' (peak-carrying engineering).  PROVED.**  Let T be an SLD-type design, I finite, f in S_{p*} with F finite, and let
g in C(f) carry d-neutral two-piece data (b^+-, omega^+-) in the extended sense of 3.1: omega^+-_m may be nonzero, with the inward signs
(varsigma_k omega^+_m(k) <= 0 <= varsigma_k omega^-_m(k)), on a finite set D of degenerate peaks; all other conditions of Definition
def:twopiece hold, kappa_w <= 1.  Let Sw be the set of carriers in supp(omega^- - omega^+), T_Sw := union_{l in Sw} supp y_l.  Suppose every
block containing a point of D contains a carrier l' notin Sw with infinitely many raising coordinates in S_{l'} \ (F ∪ supp b^+ ∪
supp b^- ∪ T_Sw).  Then (f, g) in cl NA((c_0,p), l_2^2).
*Proof.* Fix rho < 1 and eta_0 as in Theorem E.  Put A_0 := max(1, ||b^+||_1 + ||b^-||_1), A_2 := 1 + max |omega^+-| and gamma_B := the
least gap of the coordinates of supp omega^+- \ D at f (positive, finitely many).  For t <= 1 the fixed data satisfy (W3) (t||b^+-||_1 <= A_0,
Gamma_w <= kappa_w <= 1) and (W4) (|omega| <= A_2 <= A_2/t, gap >= gamma_B), with g_t := g.  Choose T_j := 2^{-j} and n_j := j.  For each j
build the companion f_j of Proposition Q for these fixed data at all scales of the window {T_j 2^{1-i} : i <= n_j} (Steps 1-3 of its proof use
only (W1)-(W5) and the donors), with Delta_j so small that p*(g - G_j) <= T_j 2^{-n_j}, that eps_j satisfies (E-e') and that
Gamma^{(j)}_w <= kappa_w + eta_0/4 <= 1 + eta_0/2.  Then (E-a)-(E-c) hold with K_j := 1, and (E-d') holds for large j (K_j T_j -> 0, and
n_j >= 48 rho^2/(c_flat(1-rho^2)) since c_flat is fixed: A_0, A_2, gamma_B are fixed).  Theorem E' gives (f, rho g) in cl NA; let rho -> 1.  QED
Remark.  Corollary Q' is the "peak-carrying Corollary cor:D1" asked for in item (1).  The steering is performed on a companion (a
non-norm-attaining first row at distance o((T_j 2^{-n_j})^2) from f), where it is FREE: donor coordinates carry no data, and the inward
coordinates need only become strict non-peaks (any gap).  This replaces the quantitative steering mu'_k <= -kappa_D s_1 at the engineered
approximant (Z4 referee 9.1), which is not needed at all.  The hypothesis "d-neutral" is used in Step 3(d) of Proposition Q (the common factor
|zeta|/|zeta'| preserves Delta d = 0 exactly; with Delta d != 0 the two representations at f_j would differ by
sum_m R_m^*(Delta d_m w_m - Delta d^{(j)}_m w_{j,m}), which is not supported on F ∪ K).
