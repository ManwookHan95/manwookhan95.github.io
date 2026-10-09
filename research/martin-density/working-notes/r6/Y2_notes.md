# Y2 notes (Round 6): items (d), (m), (h) of the open core of ADDENDUM 5 (F finite)

Setting and notation: those of paper/martin_density_note.tex (Sections 1, 7, 8), of the Round-5 reports Z3, Z4, Z6 and their referee
notes (Theorem E and Lemma U of Z3; Theorem A'' = Z4 Theorem A with (H2'') of Z4_ref_notes 3; Theorem U', design D''', Proposition P,
Corollary V.1 of the Z6 referee).  Finite block set I = {1..N}, p = p_N, F = supp a finite throughout.  "SLD-type design" means
Definition def:SLD or one of its window-modifications (SLD_G made N-free, D''', the explosive design, D^Y below): only (T-a)-(T-d),
(P1)-(P3) and allowedness (a),(b) are used.  Labels: PROVED / SKETCH / HEURISTIC / OPEN / FALSE.  Part files: Y2_part1..6.md;
scripts: Y2_work/threshold_check.py, Y2_work/companion_check.py.
No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN for every admissible T.

## 0. Summary

**New mechanism: steering on a companion, not on the approximant.**  The Z4 referee showed that carrying degenerate
swallowing-type peaks through the engineered approximants f' of f requires quantitative steering mu'_k <= -kappa_D s_1 at f', with
first-order costs on every coordinate that carries base switching.  We avoid f' altogether: by Z3's Theorem E (refereed), exact window
data may live on a nearby first row f_j ("companion") at distance o((bottom window scale)^2), and Corollary cor:D1 is then applied AT
f_j to FIXED averaged data, where no gap lower bound is needed.  We build f_j by moving z at a few far coordinates of an unused
signature set ("donor"); this changes no value u_l(zhat) of a carrier used by the data, keeps exact d-neutrality (all d-coefficients of
a block are multiplied by one common factor), and RAISES the threshold of the block strictly, so every used degenerate peak becomes a
strict non-peak of f_j (with a tiny gap, which does not matter).  The threshold monotonicity rests on a new closed form of the block
threshold (Lemma T).

Results (details and proofs in Sections 1-6):
1. Lemma T (threshold equation and strict monotonicity of the threshold).  PROVED.
2. Proposition Q (companion transfer) and Corollary Q' (peak-carrying version of Corollary cor:D1).  PROVED.  This settles item (1)
   (peak-carrying engineering) for SLD-type designs, under a donor condition; no design change, no (FS), no |F|-dimensional channel.
3. Theorem P: degenerate swallowing-type peaks are CARRIED (kept inwardly) instead of dropped: (H3) of Theorem A'' and the d-rigidity
   requirement of (E4') in Theorem U' are replaced by the donor condition (TD).  Corollary P.1: (TD) always holds at maximal contact, so
   degenerate positive peaks (Z6 referee's Proposition R1 case, item (d)) are recovered there.  PROVED.  Items (1),(2) settled except
   for the "aligned corner" (Section 3.4), OPEN.
4. Theorem M: without (DR) and without the compensated/rigid dichotomy, the d-row Hoffman constant is reduced to a design constant G**
   (faces of configuration cones are configuration cones), a fixed repair constant R_f inside the minimal face containing the d-neutral
   cone, and ONE Farkas constant kappa*(U) of the d-forced face rows.  kappa* = 0 when the d-neutral zero-cost cone meets the relative
   interior of the zero-cost cone (e.g. resonant compensators, any gaps); kappa* = Theta(1/q_min) in one-signed blocks (Lemma R and
   Theorem U' in one formula).  PROVED.  Item (m) is thereby reduced to the relative rate K_F^rel; its residual is the generalized
   nearly-neutral rate (zero-cost directions that are nearly but not exactly d-neutral), which Conjecture G-type statements would remove.
   Conjecture G: OPEN (why budget arguments do not prove it: Section 6).
5. Theorem H: (H2'') may be replaced by positivity of a "shift cost" c_*(l): the uniform shift of a block is carried by all its peaks at
   once (Lemma 6.1, peak trace), and its base switching vector Pi_m is paid by the switching budget unless it is an exact zero-cost
   resonance.  Explicit sufficient condition for c_* > 0; gap pinning by near-threshold q < 0 carriers.  PROVED.  Item (h) is reduced to
   the "coherent shift resonance" (c_* = 0 or decaying beyond the ladder), OPEN.
6. Theorem Y (master theorem for the design D^Y): combination of 3-5 with Z4 Theorem A''.  PROVED (by combination; every modification
   checked).

## Index
1. Threshold equation (Lemma T)
2. Companions (Lemma U', Theorem E', Proposition Q, Corollary Q')
3. Theorem P (degenerate swallowing-type peaks; donors; maximal contact; aligned corner)
4. Theorem M (mixed blocks without (DR): face reduction)
5. Theorem H (failure of (H2''): shift costs)
6. Theorem Y; Conjecture G; steering at f' (diagnosis); weak peaks (sketch)
7. Numerics
8. What remains (F finite), and labels

## 1. The threshold equation (any admissible T)

Fix a block and drop its index.  Phi is a sequence of positive numbers with ||Phi||_1 < 1, D the diagonal operator, |.| the
norm of Remark rem:lemmaA, zeta in l_1 \ {0}, w = J(zeta) its norming functional, M = ||w||_inf, C = ||Dw||_2, P = {k : |w(k)| = M},
alpha as in Lemma lem:threshold.  Put
   theta(zeta) := |zeta| M / C,     nu_k := |zeta(k)| / Phi_k^2   (nu_k in [0, infinity)),
   A(th; zeta) := sum_k (|zeta(k)| - th Phi_k^2)_+ ,   B(th; zeta) := sum_k Phi_k^2 min(th, nu_k)^2 ,
   Psi(th; zeta) := A(th; zeta)^2 - B(th; zeta)     (th > 0).
(The series converge: (|zeta(k)| - th Phi_k^2)_+ <= |zeta(k)| and Phi_k^2 min(th, nu_k)^2 <= th Phi_k^2 nu_k = th |zeta(k)|.)
For the block vectors of the note, zeta = R_m^** zhat (or R_m xhat'), zeta(k) = lambda_{k,m} u_{k,m}(zhat), lambda = m Phi; then
nu_k >= theta  iff  |u_{k,m}(zhat)| >= (theta/m) Phi_m(k) = hat-vartheta_m Phi_m(k): theta/m is the threshold constant hat-vartheta of the
proof of Lemma lem:scrambling, and the margin is mu_{k,m} = q_0 Phi_m(k)(nu_k - theta)/m on P.

**Lemma T (threshold equation).  PROVED.**
(a) P = {k : nu_k >= theta(zeta)}; on P, |zeta| |alpha(k)| = |zeta(k)| - theta Phi_k^2; k is a degenerate peak iff nu_k = theta.
(b) |zeta| = A(theta; zeta)  and  |zeta|^2 = B(theta; zeta); hence Psi(theta(zeta); zeta) = 0.
(c) For every zeta' in l_1 \ {0}, Psi(.; zeta') has exactly one zero on (0, infinity); it is positive to the left of the zero and
    negative to the right.  Consequently theta(zeta') is that zero, and
        Psi(theta(zeta); zeta') > 0  implies  theta(zeta') > theta(zeta).
(d) (raising moves) Let k' be a coordinate and zeta' := zeta except at k', with sgn zeta'(k') = sgn zeta(k') or zeta'(k') = 0.
    Then theta(zeta') > theta(zeta) in each of the cases: (i) k' in P and |zeta'(k')| > |zeta(k')|; (ii) k' notin P and
    |zeta'(k')| < |zeta(k')|; (iii) k' a degenerate peak and |zeta'(k')| != |zeta(k')|.
(e) (perturbed raising moves) Let zeta' in l_1, Delta := | |zeta'(k')| - |zeta(k')| | > 0, E := sum_{k != k'} |zeta'(k) - zeta(k)|,
    A := |zeta|, theta := theta(zeta).  Then theta(zeta') > theta(zeta) if either
      (i') k' in P, |zeta'(k')| > |zeta(k')| and E < A Delta/(A + theta), or
      (ii') nu_{k'} > 0, |zeta'(k')| < |zeta(k')| (k' notin P, or k' degenerate) and E < nu_{k'} Delta/(2(A + theta)).

*Proof.* (a) By Lemma lem:threshold, zeta/|zeta| = alpha + D^2 w/C with ||alpha||_1 = 1, alpha supported in P with the signs of w.
For k in P, |w(k)| = M and alpha(k) has the sign of w(k) or vanishes, so |zeta(k)|/|zeta| = |alpha(k)| + Phi_k^2 M/C, i.e.
|zeta(k)| = |zeta||alpha(k)| + theta Phi_k^2 >= theta Phi_k^2.  For k notin P, |zeta(k)| = |zeta| Phi_k^2 |w(k)|/C < |zeta| Phi_k^2 M/C
= theta Phi_k^2.  Hence P = {nu_k >= theta}, and alpha(k) = 0 iff nu_k = theta (degenerate peaks).
(b) By (a), A(theta; zeta) = sum_{k in P} |zeta||alpha(k)| = |zeta|.  Next C^2 = sum_k Phi_k^2 w(k)^2.  On P, Phi_k^2 w(k)^2 =
Phi_k^2 M^2 = (C/|zeta|)^2 Phi_k^2 theta^2 and min(theta, nu_k) = theta.  Off P, w(k) = C zeta(k)/(Phi_k^2 |zeta|), so Phi_k^2 w(k)^2 =
(C/|zeta|)^2 Phi_k^2 nu_k^2 and min(theta, nu_k) = nu_k.  Summing, C^2 = (C/|zeta|)^2 B(theta; zeta).
(c) Fix zeta' != 0 and write A', B', nu'.  A' is continuous and nonincreasing, B' continuous and nondecreasing.  If th < sup_k nu'_k,
the set {k : nu'_k > th} is nonempty; on it each term of A' is strictly decreasing and each term of B' strictly increasing in th,
so Psi' is strictly decreasing on (0, sup nu').  As th -> 0+, A' -> ||zeta'||_1 > 0 and B' -> 0, so Psi' > 0 near 0.  If
th >= sup nu' (possible only if the sup is finite), A' = 0 and Psi' = -B' < 0.  If sup nu' = infinity, A'(th) -> 0 as th -> infinity
(dominated convergence) while B'(th) >= B'(1) > 0 for th >= 1, so Psi' < 0 for large th.  Hence Psi' has exactly one zero, Psi' > 0
before it and Psi' < 0 after it.  By (b) applied to zeta', theta(zeta') is a zero, hence the zero.  If Psi(theta; zeta') > 0 with
theta = theta(zeta), then theta lies before the zero: theta < theta(zeta').
(d) Put theta := theta(zeta) and use (c); Psi(theta; zeta) = 0 by (b).  (i) nu_{k'} >= theta and nu'_{k'} > nu_{k'}: the k'-term of A
increases by |zeta'(k')| - |zeta(k')| > 0 (both positive parts are the differences themselves), the k'-term of B is theta^2 Phi^2 in
both cases; so A' > A, B' = B and Psi(theta; zeta') > 0.  (ii) nu_{k'} < theta and nu'_{k'} < nu_{k'}: the k'-terms of A vanish for
both, the k'-term of B decreases from Phi^2 nu_{k'}^2 to Phi^2 nu'^2_{k'}; so Psi(theta; zeta') > 0.  (iii) nu_{k'} = theta: an increase
is case (i), a decrease is computed as in (ii) (the A-term stays 0, the B-term decreases).
(e) For x, y in R, |(x)_+ - (y)_+| <= |x - y|, and for a, b >= 0, |min(th,a)^2 - min(th,b)^2| <= 2 th |a - b|; hence the coordinates
k != k' change A by at most E and B by at most 2 theta E (Phi_k^2 * 2 theta |nu'_k - nu_k| = 2 theta | |zeta'(k)| - |zeta(k)| |).
(i') A(theta; zeta') >= A + Delta - E >= 0 (as E < Delta), B(theta; zeta') <= B + 2 theta E, so Psi(theta; zeta') >= (A + Delta - E)^2 -
A^2 - 2 theta E >= 2A(Delta - E) - 2 theta E > 0 by the hypothesis on E.
(ii') A(theta; zeta') >= A - E, and the k'-term of B drops by Phi^2(nu^2 - nu'^2) >= Phi^2 nu (nu - nu') = nu_{k'} Delta (with
nu := nu_{k'} <= theta, nu' := nu'_{k'} < nu); so B(theta; zeta') <= B - nu_{k'} Delta + 2 theta E and Psi(theta; zeta') >= (A - E)^2 - A^2
+ nu_{k'} Delta - 2 theta E >= nu_{k'} Delta - 2(A + theta)E > 0.  (Here A(theta; zeta')^2 >= A^2 - 2AE in all cases: if
A - E >= 0 because (A-E)^2 >= A^2 - 2AE, and if A - E < 0 because then A^2 - 2AE < 0.)  QED

**Remarks (Section 1).** (1) Lemma T(b) is a closed form of the clamp equation of Lemma lem:F1 (divide by |zeta|^2: sum min(Phi_k x, v_k)^2 = 1
with x = M/C = theta/|zeta|, v_k = |zeta(k)|/(Phi_k |zeta|)); (a)+(b) give the threshold as the root of ONE explicit equation.
(2) Reading: moving mass toward the peaks (more at a peak, less at a non-peak) raises the threshold; the reverse moves lower it.
At a degenerate peak Psi has a concave kink, so both moves raise theta.
(3) Numerical check (Y2_work/threshold_check.py, 300 random blocks of size 5-13, CLARABEL SOCP for the block norm and its
norming functional): the identities (a),(b) hold to relative accuracy 5e-5 (solver accuracy); all 1100+ raising moves of type
(i),(ii) raise theta; for 200 tuned degenerate peaks both moves (+-1%) raise theta.

## 2. Companions with raised thresholds

Setting: I finite, f in S_{p*} with F = supp a finite, g in C(f), rho in (0,1), eta_0 in (0,2] with rho^2(1+eta_0) <= (1+rho^2)/2.

### 2.1 Inward-only data
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

### 2.2 Theorem E with window-dependent constants
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

### 2.3 Companions with raised thresholds
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
s notin T_j.  A donor may belong to Bl_j \ Sw_j, e.g. a good coarse strict non-peak used by the window certificate.)  For the window data of Section 3 (built from Lemma lem:windowtwopiece / Z4 Step 6), Ba_j ⊂ F ∪ T'_j ∪ union_{l in Sw_j} S_l
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
an engineered approximant of f is not (Section 6.3).  (2) The companion moves z only at donor coordinates, which carry no data and
lie outside the supports of all used carriers: the values u_l(zhat) of used carriers, the base part e, and hence exact d-neutrality are
preserved (only a common factor |zeta|/|zeta'| per block appears).  (3) Nothing about the status of f_j matters (f_j need not be in
any recovered class; the donor's own signature set acquires tiny room, which is irrelevant).

### 2.4 Peak-carrying version of Corollary cor:D1 (answer to item (1))
**Corollary Q' (peak-carrying engineering).  PROVED.**  Let T be an SLD-type design, I finite, f in S_{p*} with F finite, and let
g in C(f) carry d-neutral two-piece data (b^+-, omega^+-) in the extended sense of 2.1: omega^+-_m may be nonzero, with the inward signs
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

## 3. Theorem P: degenerate swallowing-type peaks are carried (items (d), (1), (2))

Design: D''' of the Z6 referee (admissible, N-free; Section 8 of the note, Theorem C, Theorem U', Theorem V and Z4 Theorem A'' hold
for it); or SLD_G made N-free for statement (a).  F finite.  Notation of Z4 (Theorem A'' = Theorem A with (H2'') of Z4_ref_notes 3)
and of Z6_ref_notes 3.4 (Theorem U').

### 3.1 Raisable carriers and the donor condition
A coordinate s in S_l \ F is a *raising coordinate* of the carrier l = j(k,m) if some delta_s != 0 with |z_s + delta_s| <= 1 moves
|u_l(zhat)| in the raising direction of Lemma T(d): increase if k is a non-degenerate peak, decrease if k is a strict non-peak with
w_m(k) != 0, either if k is a degenerate peak.  Concretely: k a non-degenerate peak: z_s != varsigma_k; k in Q_m with w_m(k) != 0:
z_s != -sgn w_m(k); k degenerate: always.  The carrier is *raisable* if it has infinitely many raising coordinates.
Bookkeeping by type (PROVED, from the definitions): a swallowed carrier (z = eps_l on S_l \ F) is raisable iff it is an anti-sign
peak (eps_l = -varsigma), a degenerate peak, or a strict non-peak with q_l > 0 (eps_l = sgn w); swallowing-type non-degenerate peaks,
q_l < 0 strict non-peaks and d-neutral carriers are never raisable.  A good carrier with w != 0 is raisable unless z equals the
"aligned" value (varsigma for peaks, -sgn w for non-peaks) at all but finitely many points of S_l \ F.

**(TD_m)** Block m contains (i) a raisable good carrier, or (ii) a swallowed peak of anti sign, or (iii) infinitely many raisable
carriers.

**Lemma 3.1 (donors exist).  PROVED.**  Let the window data of window j be those of Theorem A'' (or of Theorem U') with the
modification of 3.2 below, so that the switching carriers Sw_j are swallowed carriers <= l_j that are strict non-peaks or degenerate
swallowing-type peaks.  If (TD_m) holds, then for every large j block m contains a donor for window j (Section 2).
*Proof.* Base supports: b^+ = B_+ 1_F + chi V' - kappa a and b^- = b^+ - sum_{l in Sw_j} eps_l tau'_l u_l, so Ba_j ⊂ F ∪ union_{l in Sw_j}
(S_l ∪ supp y_l); for l' notin Sw_j, Ba_j ∩ S_{l'} ⊂ F ∪ union_{Sw_j} supp y_l is finite, and T_j ∪ X_j is finite; so a raisable carrier
l' notin Sw_j is a donor.  (i) good carriers are never in Sw_j; (ii) anti-sign swallowed peaks are dropped (tau' = 0, omega^+- = 0
there) in Theorems A'' and U', so they are not in Sw_j; (iii) only finitely many carriers are <= l_j.  QED

### 3.2 Keeping degenerate swallowing-type peaks
**Modification (M).**  In the proof of Theorem A'' (Z4 Steps 3-6) let D(t) := {l in U : k(l) a degenerate peak with varsigma eps = +1}
(degenerate swallowing-type swallowed peaks of the active set).  Remove from the exact cone Z_U the peak rows tau_l = 0 for l in D(t)
(keep (Z1): tau_l >= 0); all other rows are as in Z4.  In Step 6 define, for l in D(t) with k := k(l), m := m(l):
   omega^+_m(k) := -varsigma_k min(|omega_{+,m}(k)|, tau'_l/lambda_l),   omega^-_m(k) := omega^+_m(k) + eps_l tau'_l/lambda_l
(Z4 part 8.1), and include D(t) in U_np for the definition of V', b^-, omega^- (so V' := sum_{U_np ∪ D(t)} eps_l tau'_l u_l 1_{F^c}).

**Lemma 3.2 (window data with inward degenerate peaks).  PROVED.**  Under the hypotheses of Theorem A'' with (H3) deleted, the data of
(M) satisfy, at every dyadic t in W(l_*) with t <= min(t_eta, 1), t^2 <= min_{U_fix} lambda_l and C_dia t <= 1, the conditions (W1)-(W5)
of Section 2 with D_t := {k(l) : l in D(t)}, A_0 := A*_0, A_2 := 10 + C_dia, gamma_B := gamma_f(l_*), K := (1 + ||U||) K_2, where
C_dia, K_2, A*_0 are the constants of Z4 Steps 5-6 with M_f(l_*) now summing 1/mu only over NON-degenerate swallowing-type peaks.
*Proof.* Step 3 of Z4 (and Lemmas 3.1, 3.2 of the Z4 referee) uses the swallowed peaks only through (H2''), which concerns
non-degenerate peaks for LOWER and arbitrary peaks / signs of q for UPPER; unchanged.  Step 4: the actual tau violates the rows of the
modified cone by at most the old bound, since the deleted rows are the only ones that needed (H3) (a degenerate swallowing-type peak has
no margin, and its row would be violated by tau_l = lambda_l(Delta d M + e_k) with e_k unbounded); so Hoffman (configuration constant
G*(l_*), which covers every choice of the drop set P ⊂ U) gives tau_0 with ||tau|_U - tau_0||_1 <= D_0.  Step 5: the d-rows contain the
carriers of D(t) with weight q_l = Phi M/(mC) > 0 like any other kept carrier; Lemma 2.3 of Z4 (repair through U_R) applies verbatim and
yields tau' in Z_U (modified): zero cost, tau' >= 0, tau' = 0 at the other peaks of U, exact d-rows.
(W1),(W2): By Z4 Step 6(a) the pairs represent the same functional and are d-neutral (the computation d_m(omega^-) - d_m(omega^+) =
sum_{U_np ∪ D(t)} q_l tau'_l = 0 uses only (eps tau'/lambda) Phi^2 w(k)/C = q tau', valid at degenerate peaks since Phi^2 w(k)/C =
zeta(k)/sigma there (alpha(k) = 0)).  At k in D_t: varsigma omega^+(k) = -min(|omega_+(k)|, tau'/lambda) <= 0 and varsigma omega^-(k) =
varsigma omega^+(k) + varsigma eps tau'/lambda = tau'/lambda - min(...) >= 0 (varsigma eps = 1, tau' >= 0): inward on both sides.
Base side conditions: Lemma lem:split as in Z4 (V' is z-signed in K because tau' has zero cost).
(W3): the error bookkeeping of Z4 Step 6(b),(c) needs, at k in D_t, the discrepancies with the actual decomposition; by eq:peakshift
|omega_+(k)| + |omega_-(k)| = tau_l/lambda_l - Delta d M (varsigma eps = 1), and a two-case computation gives, on both sides,
   lambda_l |omega^+-(k) - omega_+-(k)| <= |tau_l - tau'_l| + lambda_l |Delta d_m| M_m
(if |omega_+| <= tau'/lambda: omega^+ = omega_+ and varsigma(omega^- - omega_-) = (tau' - tau)/lambda + Delta d M; otherwise
|omega^+ - omega_+| = |omega_+| - tau'/lambda <= (tau - tau')/lambda - Delta d M - |omega_-| and omega^- = 0, |omega_-| <= (tau - tau')/lambda
- Delta d M).  These are the same quantities that Z4 sums for the other kept and dropped carriers, so (b), (c) hold with the same
constants; t||b^+-||_1 <= A*_0 as in Z4 (||V'||_1 <= sum |tau'_l| <= 3/t).  b^+-(xi) = 0 as in Z4.
(W4): at good coordinates and kept strict non-peaks as in Z4 Step 6(d); at k in D_t: |omega^+(k)| <= |omega_+(k)| <= (3 + eta)/t <= 4/t
(Lemma lem:suplevel(a),(e)), |omega^-(k)| <= 4/t + tau'_l/lambda_l <= (10 + C_dia)/t (|tau'_l| <= 6 lambda_l/t + C_dia t and
lambda_l >= t^2 on U).  (W5): Z4 Step 6(b).  QED

### 3.3 Theorem P
**Theorem P.  PROVED (given Section 2 and the refereed Theorems A'', U').**
(a) For SLD_G (N-free) and for D''': Theorem A'' of Z4 holds with (H3) replaced by: (TD_m) holds for every block m that contains a
degenerate swallowing-sign swallowed peak.  The margin sum M_f in (W_inf) runs over non-degenerate swallowing-sign peaks only.
(b) For D''': Theorem U' holds with (E4') replaced by (E4'') "kept q < 0 non-peaks of compensated blocks have gap >= gamma_B (or gamma_B(l)
as a rate)", for every f such that (TD_m) holds in every compensated block containing a degenerate swallowing-type bad peak that is not
d-rigid; K_P runs over non-rigid NON-degenerate swallowing-type peaks.
*Proof.* (a) Fix g, rho; run Z4 Steps 1-6 with modification (M) along the windows l_j given by (W_inf) (the window arithmetic of Z4
Step 8 is unchanged: K_j/c_{flat,j} <= C G*^4 Lambda°^2 Xi_f with c_{flat,j} >= c_0 gamma_f(l_j)/A_2(j), Lemma U'); Lemma 3.2 gives window data
with inward degenerate peaks satisfying (W1)-(W5) and (E-d') of Theorem E'.  If no window uses an inward coordinate, Z4 Step 9 concludes;
otherwise Lemma 3.1 gives donors in every block with inward coordinates (blocks containing a degenerate swallowing-sign swallowed peak), and
Proposition Q gives (f, rho g) in cl NA.  Let rho -> 1.
(b) In the proof of Theorem U' (Z6_ref_notes 3.4), use the pattern in which the non-rigid degenerate swallowing-type bad peaks of compensated
blocks are KEPT (sign row tau_l >= 0) instead of dropped; the combinatorial Hoffman constant H_comb covers every kept/dropped partition, the
compensation step (5) treats them as kept carriers with q > 0 (upward closure in the compensator directions is unaffected), and the window
two-piece data at them are those of (M), with the discrepancy bound of Lemma 3.2(W3) replacing the drop bound |tau| + lambda|Delta d|M.  The
rest of the proof is unchanged (rigid degenerate peaks are dropped by Theorem V / Proposition P as before).  The resulting data satisfy
(W1)-(W5); conclude with Lemma 3.1 and Proposition Q.  QED

**Corollary P.1 (maximal contact).  PROVED.**  At maximal contact (F finite, z = eps_0 off F) (TD_m) holds in every block: by Lemma 5.0 of Z4
every block has infinitely many peaks with w = -eps_0 M, swallowed with eps = eps_0, i.e. anti-sign swallowed peaks.  Hence: (i) Corollary 5.4 of
Z4 (SLD_G) holds without (H3); (ii) Corollary 3.4' of the Z6 referee (D''') holds for every f with every block compensated or rigid, kept q<0
non-peaks with gap >= gamma_B (or as a rate), and liminf (K_P + K_R)(l)/(l 2^{l^3} Lambda°(l)) = 0, where degenerate positive peaks are
now allowed in compensated blocks.  In particular the case singled out by the Z6 referee's Proposition R1 (at maximal contact every positive
peak of a compensated block is non-rigid) is no longer open for DEGENERATE positive peaks; weak positive peaks (positive tiny margins) remain
a rate (K_P).

### 3.4 What remains of (d)
(TD_m) fails only in the **aligned corner**: block m has only finitely many raisable carriers, all of them swallowed (degenerate
swallowing-type peaks or q > 0 non-peaks), no anti-sign swallowed peak, and every good carrier with w != 0 is a non-degenerate peak or a
strict non-peak which is far-aligned (z = varsigma on a cofinite part of S_l \ F for peaks, z = -sgn w for non-peaks; a good degenerate peak
would be raisable).  If moreover a degenerate swallowing-type peak of block m is not d-rigid,
then (Corollary V.1) the block has a swallowed q < 0 strict non-peak, so (H2'') UPPER can only hold through a good peak, which must then be
far-aligned.  In this corner every admissible z-move outside the data supports LOWERS the threshold of block m to first order (Lemma T(d)),
so threshold steering is impossible there; the |F|-dimensional e-channel moves the values of the used carriers and breaks exact
d-neutrality.  OPEN (narrow): recover non-rigid degenerate swallowing-type peaks in aligned blocks.  It never occurs at maximal contact,
nor when the block has an anti-sign swallowed peak, a raisable good carrier, or infinitely many raisable carriers; and at a given window
any raisable carrier that the window data do not use for switching (e.g. a degenerate peak with tau' = 0 at all scales of the window) is a
donor as well (Section 2.3 only needs l' notin Sw_j).

## 4. Theorem M: mixed blocks without (DR) (item (m))

Framework: Z4 Theorem A'' (Steps 1-9, active sets U = U(t) = {l in B ∩ [1,l_*] : lambda_l >= t^2} ⊃ U_fix), configurations kappa =
(U, P, eps, F', type, n) and their cones Z'_kappa (rows (Z1),(Z2)) and Z^0_kappa (rows (Z1)-(Z3)) of Z4 part 2; q_l, Q_m(tau) :=
sum_{l in U, m(l)=m} q_l tau_l (all bad carriers, peaks included: q = varsigma eps Phi M/(mC) for peaks).

### 4.1 The enlarged configuration constant and the design D^Y
In Z4 a configuration has type(s) = eps_{l'} forced on S_{l'} ∩ T(U) (l' in U).  Call a *free configuration* the same object with
type : T(U) \ F' -> {+1, -1, 0} arbitrary.  Put G**(l) := max(1, max over free configurations of level <= l of the l_1-Hoffman
constants of the systems (Z1),(Z2) and (Z1)-(Z3)) -- finite (finitely many free configurations of each level, Hoffman 1952), N-free if U
ranges over all subsets of [1,l] (Z4 referee Section 2), and computable from the design data of the carriers l' <= l.
**Design D^Y**: Definition D''' of the Z6 referee (T(l), m^nat, D(l) := 1 + sum_{l''<=l}(1/m^nat_{l''}(l) + 1/Phi_{l''}), H_comb(l) as
there) with Xi'(l) replaced by
   Xi^Y(l) := [l H_comb(l) G**(l) D(l)]^8 (l 2^{l^3} Lambda°(l) G**(l))^5,
n^w_l := ceil(l 2^{l^3} Lambda°(l) Xi^Y(l)), T_hi(l) := min{T_lo(l-1), 2^{-l^3}/(l Lambda°(l) Xi^Y(l))}, T_lo(l) := 2^{-n^w_l} T_hi(l),
c_{l+1} := min{c_l/4, T_lo(l)^3}.  PROVED: D^Y is admissible and N-free, and every result proved for D''' (all of Section 8 of the
note, Theorems C, U', V, Z4 Theorem A'') holds for D^Y: the recursion is well defined (every ingredient has index <= l), Xi^Y >= Xi' >= 1
gives (P1), (P2) and the (P3) used by D''' (the Z6 referee's Proposition 3.3 uses only that the inserted factor dominates the factors
it needs, is >= 1, computable at stage l and N-free).
**Faces are free configurations (PROVED).**  Every face of Z^0_kappa is Z^0_kappa' for a free configuration kappa': a face is obtained by
turning some inequality rows into equalities; for a row of (Z1) this enlarges P, for a row of (Z2) at j it sets type'(j) := 0.  Hence the
Hoffman constant of every face of every configuration cone of level <= l is at most G**(l).

### 4.2 The d-forced face and its Farkas constant
Fix f (F finite) and a finite U ⊃ U_fix, U ⊂ B.  Let Z^0 := Z^0_{kappa(f,U)} (zero cost, drop rows tau_l = 0 at the peaks that are
dropped; in the setting of Theorem P the kept degenerate swallowing-type peaks have no drop row), C(U) := Z^0 ∩ ker Q (Q = (Q_m)_m), and
F_min(U) the minimal face of Z^0 containing C(U).  Let A(U) be the set of inequality rows r_a of Z^0 that vanish on F_min(U) but not on
all of Z^0 (the *d-forced rows*), and rho_A := sum_{a in A(U)} r_a (rho_A := 0 if A(U) = {}).
**Lemma 4.1 (Farkas pinning of the d-forced face).  PROVED.**  If A(U) != {}, there are y_b >= 0 (inequality rows of Z^0), y'_e in R
(equality rows) and kappa_m in R with -rho_A = sum_b y_b r_b + sum_e y'_e r_e + sum_m kappa_m Q_m.  Let kappa*(U) be the least
sup-norm of such a certificate (an LP; kappa*(U) := 0 if A(U) = {}).  Then for every tau in R^U
   sum_{a in A(U)} |r_a(tau)| <= (kappa*(U) + 2) V_1(tau),   V_1(tau) := sum_b (r_b(tau))_- + sum_e |r_e(tau)| + sum_m |Q_m(tau)|.
*Proof.* rho_A >= 0 on Z^0 and rho_A = 0 on C(U) = Z^0 ∩ ker Q, so -rho_A >= 0 on the polyhedral cone Z^0 ∩ ker Q; Farkas' lemma gives
the certificate.  Evaluating at tau and bounding -y_b r_b(tau) <= y_b (r_b(tau))_-, |y'_e r_e(tau)|, |kappa_m Q_m(tau)|:
rho_A(tau) <= kappa*(U) V_1(tau).  Finally sum_a |r_a(tau)| = rho_A(tau) + 2 sum_a (r_a(tau))_- <= rho_A(tau) + 2 V_1(tau).  QED
**Lemma 4.2 (monotonicity and repair inside the face).  PROVED.**  (a) For U ⊂ U' (finite, ⊃ U_fix) the extension by zero E maps Z^0(U)
into Z^0(U'), C(U) into C(U'), and F_min(U) into F_min(U').  (b) V(U) := Q(F_min(U)) is a linear subspace of R^N, and V(U) ⊂ V(U').
(c) There are a finite set U_V ⊂ B and R_f < infinity (depending only on f) such that for every finite U ⊃ U_V ∪ U_fix and every
v in V(U) there is rho in F_min(U) with Q(rho) = v and ||rho||_1 <= R_f ||v||_1.
*Proof.* (a) Rows of Z^0(U') at coordinates of T(U) and the sign/drop rows of carriers of U are those of Z^0(U) (drop status of a carrier
does not depend on U); a new row at j in T(U') \ T(U) evaluated at E tau reads sum_{l in U} eps_l tau_l u_l(j): j lies in no target of U,
so either j in S_l for one l in U, where the row is eps_l tau_l v_l(j) with type(j) = z_j = eps_l (l swallowed), i.e. tau_l v_l(j) >= 0,
true on Z^0(U); or the value is 0.  New sign/drop rows of carriers of U' \ U vanish at E tau.  Q(E tau) = Q(tau).  So E(Z^0(U)) ⊂ Z^0(U'),
E(C(U)) ⊂ C(U').  Let nu_0 in C(U) ∩ ri F_min(U).  For mu in F_min(U), nu_0 - s mu in F_min(U) for small s > 0, hence E(nu_0) = s E(mu) +
E(nu_0 - s mu) with both summands in Z^0(U'); E(nu_0) lies in C(U') ⊂ F_min(U'), a face, so E(mu) in F_min(U').
(b) Q is linear on the cone F_min(U), so Q(F_min(U)) is a convex cone; it contains a neighbourhood of 0 = Q(nu_0) in Q(span F_min(U))
because nu_0 is a relative interior point; hence it equals the subspace Q(span F_min(U)).  Monotone by (a) and Q∘E = Q.
(c) The subspaces V(U) ⊂ R^N increase along inclusions; take U_V with dim V(U_V) maximal; then V(U) = V(U_V) =: V_inf for U ⊃ U_V.
F_min(U_V) is a finitely generated cone with Q(F_min(U_V)) = V_inf; choose generators rho_1..rho_p and, for a basis of V_inf and its
negatives, nonnegative combinations of the generators; this gives a linear-programming selection v -> rho(v) in F_min(U_V) with
||rho(v)||_1 <= R_f ||v||_1.  For U ⊃ U_V, E rho(v) in F_min(U) by (a).  QED
**Proposition 4.3 (face reduction).  PROVED.**  For U ⊃ U_V ∪ U_fix and every tau in R^U there is tau' in C(U) with
   ||tau - tau'||_1 <= [G**(l)(kappa*(U) + 3) + R_f (1 + N q_max G**(l)(kappa*(U) + 3))] V_1(tau)      (l := max U, q_max := max |q_l| <= 1/C_min).
*Proof.* F_min(U) = Z^0 ∩ {r_a = 0 : a in A(U)} (a face is cut out by the rows tight on it; rows tight on all of Z^0 are rows of Z^0
already), a free configuration cone of level l (4.1).  Hoffman: tau_1 in F_min(U) with ||tau - tau_1||_1 <= G**(l)(viol_{Z^0}(tau) +
sum_a |r_a(tau)|) <= G**(l)(kappa* + 3) V_1(tau) (Lemma 4.1).  Then Q(tau_1) in V(U) (Lemma 4.2(b)); let rho := rho(-Q(tau_1)) (Lemma 4.2(c))
and tau' := tau_1 + rho in F_min(U) (convex cone) with Q(tau') = 0, i.e. tau' in C(U).  ||rho||_1 <= R_f ||Q(tau_1)||_1 <=
R_f(||Q(tau)||_1 + N q_max ||tau - tau_1||_1).  QED
Reading.  The f-dependence of the d-row Hoffman constant is isolated in ONE linear program per active set, kappa*(U), plus a fixed
repair constant R_f; the combinatorial part is the design constant G**.  kappa*(U) = 0 whenever the d-neutral zero-cost cone C(U) meets
the relative interior of the zero-cost cone Z^0 (no d-forced rows): then mixed blocks cost nothing beyond R_f.

### 4.3 Theorem M
Rates: K_F(l) := max{kappa*(U) : U finite, U_V ∪ U_fix ⊂ U ⊂ B ∩ [1,l]} (nondecreasing in l) and its relative version
K_F^rel(l) := K_F(l)/D(l) (D(l) the design factor of D^Y; by 4.4(a) design-scale parts 1/Phi of kappa* are absorbed by D(l)).
**Theorem M.  PROVED (by modification of Z4 Theorem A'' / Theorem P).**  Design D^Y, N >= 1, f with F finite satisfying (H2'') [or the
shift-cost condition of Section 5], (H3) or the donor condition of Theorem P, and
   (W_M)  liminf_l (1 + K_F^rel(l))^2 Xi_f(l) / (l 2^{l^3})^6 = 0     (Xi_f as in Z4 3.1).
Then f in Rec.  No (DR), no compensated/rigid dichotomy, no resonance is assumed: mixed blocks are allowed.
*Proof.* Z4 Steps 1-3 unchanged (they give c_U(tau) <= (1/q_0 + 2K_0)t, the projection bound for the zero-cost rows via Lemma 2.2 of Z4
with gamma_T, and |Delta d_m| M_m <= K_d t).  Step 4 of Z4 bounds the violations of (Z1)-(Z3) by C_2(K_1 + M_f)t; Step 5's first computation
bounds |Q_m(tau|_U)| <= K_q t <= C K_1 t (inactive and fine carriers included).  So V_1(tau|_U) <= C'(K_1 + M_f) t.  Replace the
Hoffman-plus-(DR) argument of Steps 4-5 by Proposition 4.3 (U ⊃ U_V for t small): tau' in C(U) -- zero cost, tau' = 0 at the dropped peaks,
exact d-rows -- with ||tau|_U - tau'||_1 <= C_dia' t, C_dia' := C'' G**(l_*)(1 + K_F(l_*))(K_1 + M_f), C'' an f-constant.  Steps 6-9 (or
Lemma 3.2 + Proposition Q in the setting of Theorem P) are unchanged with C_dia' in place of C_dia; since C_dia' <= C D(l)(1 + K_F^rel)
G**^2 (Lambda* + l + M_f)/gamma_T, Z4 Step 8 needs K_j/c_flat <= C D^2 (1 + K_F^rel)^2 G**^4 Lambda°^2 Xi_f <= n^w_l and K_j T_hi(l) -> 0;
D^Y gives n^w_l >= (l 2^{l^3} Lambda°)^6 G**^{13} D^8 and T_hi(l) <= its inverse, so both hold along the levels given by (W_M).  QED

### 4.4 What K_F measures, and what remains of (m)
(a) PROVED: one block, all its carriers in U resonant strict non-peaks with q_l >= 0: Z^0 is the orthant, C(U) = {tau >= 0 : tau_l = 0
where q_l > 0}, the d-forced rows are the sign rows of the q > 0 carriers, and with q_min := min{q_l > 0}, q_max := max q_l the
certificate -sum_{q_l>0} tau_l = -(1/q_min) Q_m + sum_{q_l>0} (q_l/q_min - 1) tau_l gives 1/q_min <= kappa*(U) <= (1 + q_max)/q_min (the
lower bound: the coefficient kappa of Q_m must satisfy kappa q_l <= -1 for every l with q_l > 0).  So K_F is design scale (q_l >= Phi_l/2
when gap <= M/2, Z6 referee 3.1) times the relative rate K_nn of nearly neutral carriers -- the Z4 referee's Lemma R (lower bound) and
Theorem U' (upper bound) in one formula.
(b) PROVED: K_F(l) = 0 iff A(U) = {} for all U, iff C(U) meets the relative interior of Z^0 (the minimal face containing C(U) is Z^0).
This holds in particular if every block containing a carrier of B with q != 0 has resonant strict non-peaks l^+_m, l^-_m in U_fix with
q_{l^+_m} > 0 > q_{l^-_m} (compensated blocks, NO gap condition needed for this step): take nu_0 in ri Z^0; e_{l^+-_m} in Z^0 (resonance),
so nu := nu_0 + sum_m (x^+_m e_{l^+_m} + x^-_m e_{l^-_m}) in ri Z^0 for x >= 0, and x can be chosen with Q(nu) = 0.  More generally
K_F = 0 whenever some d-neutral zero-cost combination is strictly positive on every non-implicit row of Z^0 ("two-sided mixed blocks").
(c) In general kappa*(U) is the reciprocal of the smallest relative d-coefficient of a zero-cost direction leaving the d-forced face:
by LP duality, kappa*(U) = sup{ rho_A(mu) : mu with V_1-row violations <= 1 and |Q(mu)| <= 1 ... } (HEURISTIC reading, not used).  It is
large exactly when zero-cost switching directions exist that are NEARLY but not exactly d-neutral (generalized K_nn).  This is a genuine
f-rate (the q_l depend continuously on f), and the exact-data method cannot avoid it: the actual switching may run along such a
direction with amplitude up to |Q|-pinning/|Q(direction)|, and no exact d-neutral datum is close to it (the direction is not contained in
any d-neutral zero-cost element).  REMAINING STEP for (m): either a design that bounds kappa*(U) (impossible for one-signed blocks by
Lemma R, so only relative versions K_F/D(l) can be design-bounded), or a joint transient bound of Conjecture G type for nearly neutral
directions (Section 6).

## 5. Theorem H: failure of (H2'') (item (h))

Framework: Z4 Theorem A'' (Steps 1-3), any SLD-type design; F finite; t in W(l_*), a two-sided decomposition of g at scale t,
Delta d_m := d_{+,m} - d_{-,m}, varsigma_k := sgn w_m(k), mu_k margins, e_k := |omega_{+,m}(k)| + |omega_{-,m}(k)| at peaks.
The Z4 referee (finding 3, Remark 3.3) showed that (H2'') fails exactly when some block (i) has all its peaks swallowed with swallowing
sign and a swallowed q < 0 strict non-peak (UPPER fails), or (ii) has all its non-degenerate peaks swallowed with anti sign and a
swallowed carrier with q > 0 (LOWER fails).  Below, I_up (resp. I_lo) denotes the set of blocks in which the upper (resp. lower) half of
(H2'') fails; in the other blocks the corresponding half holds and gives the bound of Z4 Step 3 / Lemmas 3.1-3.2 of the Z4 referee.

### 5.1 The peak trace of the shift
**Lemma 5.1 (peak trace).  PROVED.**  For every peak k = k(l) of block m (good or swallowed, any sign),
   -Delta theta_l = varsigma_k lambda_l (Delta d_m M_m + e_k),   0 <= e_k, and e_k <= t/(lambda_l mu_k) if mu_k > 0.
Hence, on F^c,
   Delta B 1_{F^c} = sum_m Delta d_m M_m Pi_m + E + sum_{l notin P*} (-Delta theta_l) u_l 1_{F^c},
   Pi_m := sum_{l in P*_m} varsigma_{k(l)} lambda_l u_l 1_{F^c},   E := sum_{l in P*} varsigma_{k(l)} lambda_l e_{k(l)} u_l 1_{F^c},
for any set P* = union_m P*_m of coarse (<= l_*) peak carriers with positive margins; ||E||_1 <= t sum_{l in P*} 1/mu_{k(l)}.
*Proof.* eq:peakshift: e_k = -varsigma_k Delta Theta_m(k) - Delta d_m M_m >= 0 with Delta Theta_m(k) = Delta theta_l/lambda_l; and
lambda_l mu_k e_k = sigma_m |alpha_m(k)| e_k <= t (Lemma lem:suplevel(c), eq:margin).  The display is eq:DeltaB split along P*,
with ||u_l||_1 <= 1.  QED
So a uniform shift Delta d_m appears in the base switching as the vector Delta d_m M_m Pi_m: the shift of a block is carried by ALL its peaks
at once.  At a good peak this is pinned (Lemma badpeaks(a)); at swallowed peaks it is zero-cost on their own signature sets exactly when
varsigma eps_l (Delta d_m) >= 0, i.e. for Delta d > 0 at swallowing-type peaks and Delta d < 0 at anti-sign peaks -- which is why
configuration (i) leaves Delta d free upward and (ii) downward.

### 5.2 The shift cost
For a level l, a margin threshold mu_0 > 0 and the corresponding sets P*_m(l) := {coarse non-degenerate peak carriers of block m,
<= l, mu >= mu_0} (m in I_up ∪ I_lo), let Bfree(l) := all swallowed carriers <= l except those in P*(l).  For delta in R^{I_up ∪ I_lo} put
   c(delta; l) := inf_{x in R_+^{Bfree(l)}} sum_{j notin F} phi_{z_j}( sum_m delta_m Pi_m(j) + sum_{l' in Bfree(l)} x_{l'} eps_{l'} u_{l'}(j) )
(the series converges since sum_l lambda_l ||u_l||_1 < infinity and x ranges over a finite-dimensional cone; c(.; l) is the partial
infimum of a jointly convex, positively homogeneous, finite function, hence convex, positively homogeneous, finite and continuous), and
   c_*(l) := inf{ c(delta; l) : ||delta||_1 = 1, delta_m >= 0 (m in I_up \ I_lo), delta_m <= 0 (m in I_lo \ I_up) }.
c(.; l) is convex and positively homogeneous, so c(delta; l) >= c_*(l) ||delta||_1 on the sign cone.

**Proposition 5.2 (shift-cost pinning).  PROVED.**  With K_g t the good pinning bound (Lambda_g, Lemma lem:modswallow(a) / Z4 Step 1)
and K_- t := sum_{l in B, l <= l_*} (tau_l)_- (in the framework of Z4: K_- <= (1/q_0 + 2) K_1 + 6 l_*, from the projection tau° >= 0 of
Z4 Step 3 on the active set and the box bound |tau_l| <= 6 lambda_l/t < 6t for inactive carriers), put
delta_m := (Delta d_m)_+ M_m (m in I_up \ I_lo), -(Delta d_m)_- M_m (m in I_lo \ I_up), Delta d_m M_m (m in I_up ∩ I_lo).  Then
   c_*(l_*) ||delta||_1 <= t/q_0 + 2[ K_g t + 6t^2 + K_- t + t l_*/mu_0 + K_d^{half} t ],
where K_d^{half} t bounds the pinned halves ((Delta d_m)_- M_m for m in I_up \ I_lo, (Delta d_m)_+ M_m for m in I_lo \ I_up; Z4 Step 3 and
Lemmas 3.1, 3.2 of the Z4 referee give K_d^{half} <= C' K_1).  In particular, if c_*(l_*) > 0 then |Delta d_m| M_m <= K_sh t for all m in
I_up ∪ I_lo, with K_sh := C_f (K_g + K_- + l_*/mu_0 + K_1 + 1)/c_*(l_*).
*Proof.* Lemma lem:switchbudget: sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0.  In Lemma 5.1 take P* := P*(l_*) (peaks of the blocks of
I_up ∪ I_lo only).  The remaining terms of Delta B 1_{F^c}: good carriers (||.||_1 <= K_g t), fine carriers (<= 6t^2), swallowed carriers
<= l_* outside P* (this includes all swallowed peaks of the other blocks and the degenerate or weak peaks of the blocks of I_up ∪ I_lo):
-Delta theta_l u_l = eps_l tau_l u_l = eps_l (tau_l)_+ u_l - eps_l (tau_l)_- u_l.  Hence Delta B 1_{F^c} = sum_m delta_m Pi_m +
sum_{l in Bfree} x_l eps_l u_l + R with x_l := (tau_l)_+ >= 0 and ||R||_1 <= ||E||_1 + K_g t + 6t^2 + K_- t + K_d^{half} t max_m ||Pi_m||_1
(||Pi_m||_1 <= sum_l lambda_l <= 1/3).  By Lemma lem:phicalc(c), t/q_0 >= sum_j phi_{z_j}(sum delta Pi + sum x eps u) - 2||R||_1 >=
c(delta; l_*) - 2||R||_1 >= c_*(l_*) ||delta||_1 - 2||R||_1, and ||E||_1 <= t |P*(l_*)|/mu_0 <= t l_*/mu_0 (Lemma 5.1).  QED

**Theorem H.  PROVED (by modification of Z4 Theorem A'' and of Theorems P, M).**  Design D^Y.  In Theorem M (and in Theorem P)
hypothesis (H2'') may be replaced by: there is mu_0 > 0 such that c_*(l) > 0 for all large l, and
   (W_H)  liminf_l (1 + K_F^rel(l))^2 (1 + K_sh^rel(l))^2 Xi_f(l)/(l 2^{l^3})^6 = 0,   K_sh^rel(l) := 1/(c_*(l) D(l))
(K_sh^rel := 0 if (H2'') holds in every block).  Blocks satisfying (H2'') need no shift cost.
*Proof.* (H2'') enters Z4 only in Step 3, through |Delta d_m| M_m <= K_d t with K_d = C_1 K_1; Proposition 5.2 provides this bound with
K_sh = C_f (K_g + K_- + l_*/mu_0 + K_1 + 1)/c_*(l_*) <= C_f (1 + l_*/mu_0) K_1 D(l_*) K_sh^rel(l_*) (K_- <= (1/q_0 + 2)K_1 + 6 l_*, from the
projection tau° >= 0 of Z4 Step 3 and the box bound for inactive carriers; K_g <= K* <= K_1).  All later constants of Z4 and of Theorem M
are linear in K_d, so C_dia' acquires the factor C(1 + l/mu_0) D (1 + K_sh^rel); the window arithmetic of the proof of Theorem M then holds
along the levels given by (W_H): D^Y provides D^8 and the factor (1 + l/mu_0)^2 <= C l^2 <= C Lambda°(l) is absorbed by the surplus
Lambda°^4 of n^w_l.  QED

### 5.3 When is the shift cost positive?  What remains of (h)
(a) PROVED (gap pinning, configuration (i)).  For a swallowed q < 0 strict non-peak l of block m (eps_l = -varsigma_k), the box
inequalities of Lemma lem:suplevel(f) on both sides give tau_l/lambda_l + Delta d_m M_m <= 2 gap_m(k(l))/t, hence
   Delta d_m M_m <= 2 gap_m(k(l))/t + (tau_l)_-/lambda_l:
q < 0 carriers whose gaps are <= K t^2 at the window scales pin the shift from above (near-threshold q < 0 carriers, harmful when kept,
are useful here).  [Derivation: varsigma(omega_+ - omega_-)(k) = tau_l/lambda_l + Delta d |w(k)| and varsigma omega_+ <= (1 - d_+ t)gap/t,
-varsigma omega_- <= (1 + d_- t)gap/t; use |w(k)| + gap = M.]
(b) c_*(l) = 0 iff for some nonzero delta in the sign cone (c is continuous on the compact sign sphere) the vectors sum_m delta_m Pi_m +
sum x_l eps_l u_l, x >= 0, have cost arbitrarily close to 0: the uniform-shift trace on the coarse peaks, corrected by swallowed
switchings, is an exact (or asymptotically exact) zero-cost resonance.  On the peaks' own
signature sets this is automatic in configurations (i)/(ii) (5.1); what must happen in addition is exact sign compatibility (contacts) and
exact cancellation (free coordinates) on the TARGET coordinates of the peaks, including the slaving coordinates where later targets meet
earlier (good) signature sets.  Sufficient condition (PROVED): for every m in I_up ∪ I_lo there is a coordinate j_m notin F with
|z_{j_m}| < 1, Pi_m(j_m) != 0, Pi_{m'}(j_m) = 0 for m' != m, and u_{l'}(j_m) = 0 for every l' in Bfree(l) (a peak target at a free
coordinate that no swallowed carrier reaches).  Indeed then, for ||delta||_1 = 1, the j_m-term of the cost equals
phi_{z_{j_m}}(delta_m Pi_m(j_m)) >= (1 - |z_{j_m}|)|Pi_m(j_m)||delta_m| whatever x is, so c_*(l) >= min_m (1 - |z_{j_m}|)|Pi_m(j_m)|/|I_up ∪ I_lo|
(using ||delta||_1 = 1 and max_m |delta_m| >= 1/|I_up ∪ I_lo|).
(c) REMAINING STEP (OPEN): configurations (i)/(ii) with c_*(l) = 0 or c_*(l) decaying faster than the ladder ("coherent shift
resonance").  There the shift may be O(1) (not O(t)) for some decompositions, and the exact d-neutral window data of Z4 cannot follow it.
Exact data with Delta d != 0 would be needed; Corollary cor:D1 accepts Delta d >= 0 (configuration (ii): decomposition Delta d < 0
corresponds to data Delta d > 0), but by the Z4 referee's Proposition 5.6' such data exist only if all but finitely many non-d-neutral
carriers of the block are swallowed with the coherent sign, AND (new observation, PROVED by the computation of 5.1) the full vector
-Delta d R_m^* w_m must be z-signed on K and vanish at free coordinates, which in addition requires the coherent-resonance property of
(b) for ALL peaks (fine ones included) and for all non-peaks with w != 0.  Whether mates in the coherent case are recovered is open.

## 6. Master theorem, Conjecture G, diagnosis of steering at f', weak peaks

### 6.1 Theorem Y (combination)
**Theorem Y.  PROVED (by combination of Theorems P, M, H with Z4 Theorem A''; every modification is checked in Sections 3.3, 4.3, 5.2).**
Let T be the design D^Y (Section 4.1), N >= 1, and f in S_{p*} with F finite.  Assume
 (Y1) r*_l(l) > 0 for every good l and gamma_T(l) > 0 (notation of Z4 3.1);
 (Y2) in every block, (H2'') holds, or for the failing halves c_*(l) > 0 for all large l with some mu_0 > 0 (Section 5.2);
 (Y3) every block containing a degenerate swallowing-sign swallowed peak satisfies (TD_m) (Section 3.1);
 (Y4) liminf_l (1 + K_F^rel(l))^2 (1 + K_sh^rel(l))^2 Xi_f(l)/(l 2^{l^3})^6 = 0, with Xi_f(l) := [(Lambda*_f(l) + M_f(l) + l)/Lambda°(l)]^2/
      (gamma_T(l)^2 gamma_f(l)) as in Z4, M_f summing 1/mu over NON-degenerate swallowing-sign swallowed peaks <= l.
Then f in Rec: (f, g) in cl NA((c_0,p_N), l_2^2) for every g in C(f).  No (DR), no (H3), no compensated/rigid dichotomy, no resonance, no
bound on the number of swallowed carriers; maximal contact allowed.
*Proof.* Fix g, rho.  Run Z4 Steps 1-2.  Step 3: the zero-cost projection tau° as in Z4; the shift bound |Delta d_m| M_m <= K t from (H2'')
(Z4 Step 3, Z4 referee Lemmas 3.1, 3.2) in the blocks where it holds and from Proposition 5.2 for the failing halves.  Steps 4-5 with
modification (M) (Section 3.2: degenerate swallowing-type peaks kept, no drop row) and with the face reduction (Proposition 4.3) in place of
Hoffman + (DR).  Step 6 with Lemma 3.2 at the kept degenerate peaks.  Step 7-8: Lemma U' and Theorem E' (window-dependent c_flat) at the
companions of Proposition Q (donors by Lemma 3.1 under (Y3)); if no inward coordinate is used in a window, the companion is f itself and
Z4 Step 9 (Corollary cor:D1 at f) applies.  The constant C_dia of Z4 becomes C D (1 + K_F^rel)(1 + l/mu_0) D (1 + K_sh^rel) G**^2
(Lambda* + l + M_f)/gamma_T; the window arithmetic of the proof of Theorem M (with the surplus D^8 Lambda°^4 G**^9 of n^w in D^Y) holds along
the levels given by (Y4).  QED
**Corollary Y.1 (maximal contact).  PROVED.**  If z = eps_0 on N \ F (F finite), then (Y1) is vacuous, (Y2) holds with (H2'') (Lemma 5.0 of
Z4: peaks of both signs, i.e. swallowing-sign and anti-sign swallowed peaks, in every block), (Y3) holds (Corollary P.1), gamma_T = 1 and
Lambda*_f <= C Lambda°.  Hence f in Rec as soon as
   liminf_l (1 + K_F^rel(l))^2 (1 + M_f(l)/Lambda°(l))^2 / (gamma_f(l) (l 2^{l^3})^6) = 0.
At maximal contact (with F finite) the only remaining obstructions are three f-dependent RATES: relative margins of non-degenerate
positive peaks (M_f), gaps of swallowed strict non-peaks (gamma_f), and the relative face Farkas rate K_F^rel (nearly d-neutral zero-cost
directions).  Degenerate peaks, mixed blocks, one-sided d-resources and the (H2'')/(H3) conditions are no longer obstructions there,
except through these rates (one-sided and mixed d-resources enter only via K_F^rel).

### 6.2 Conjecture G (Z6): status OPEN
Statement (Z6 6.2): if l is a swallowed strict non-peak with gap >= M_m/2 in a one-signed block, then at every scale t some two-sided
decomposition switches through l by at most C t/m_u(l), m_u(l) := ||u_l 1_{F^c}||_1; joint version: simultaneously for all coarse such l.
What it would give: in Theorem M the d-forced rows of nearly neutral carriers would not need Farkas pinning, so K_F^rel would be bounded
by design quantities in one-signed blocks (removing K_nn), and in general K_F^rel could be restricted to directions that are not nearly
neutral.  Why the budget does not prove it (HEURISTIC, explicit computation): un-switching an amount s tau_l on the - side
(Theta'_- = Theta_- + y e_k, B'_- = B_- - y lambda_l u_l, y = -eps_l s tau_l/lambda_l) is free on S_l up to the - side's share, but at first
order it raises the block level by t s tau_l q_l and lowers the base level by t s tau_l q_l sigma_m/q_0 (a pure level shift, rebalanced only
at cost iota t s tau_l |q_l| with a fixed inefficiency iota > 0), and costs up to 2 t s tau_l ||y_l||_1/n_l on the target coordinates; with no
slack in the optimal decompositions (and only O(t^2) slack for near-optimal ones) this allows un-switching of O(t)/(|q| iota + m_target), not
a reduction of the switching to O(t/m_u).  A proof must use the validity of the mate (g in C(f)) jointly over scales, as in the Z6 referee's
single-module heuristic (the switching band is empty under the validity bound c^2 <= (M + |w|) lambda/(16 m_u)).  OPEN.

### 6.3 Steering at the engineered approximant (diagnosis; why companions are needed)
(a) PROVED (Z4 referee Observation 9.1): Theorem thm:engineered uses the averaged data for |tau| <= s_1 and both signs; at a used
degenerate peak the averaged datum omega^theta(k) is outward for one sign unless it vanishes.
(b) PROVED: re-decomposing g' at f' without the coordinate k creates first-order level mismatches of size |tau| lambda_k |u_k(xhat')|, i.e.
O(|tau|) (q_k = Phi M/(mC) > 0 at a degenerate swallowing-type peak), which rebalancing cannot absorb for |tau| <= s_1.
(c) HEURISTIC: data used at |tau| <= s_1 must have the same switching amplitudes on all carriers with infinite signature tails (otherwise the
truncation beyond N'' costs |tau| V_{>N''} at first order), so a "middle" datum with omega(D) = 0 exists only under a conic decomposition
condition (always in resonant blocks: the d-neutral cone is then {tau >= 0 : Q(tau) = 0} and prescribed D-components in [0, tau'_D] can be
completed; not in general).  At f' every coordinate carrying base switching is a first-order steering cost, and the e-channels (masses at
contacts with the sign z_j, masses on F) steer only under a Gordan condition on the Gram form G(v,w) = <P^perp U* v, P^perp U* w>, which can
fail for special U.  Companions (Section 2) avoid all of this: there the steering is a zeroth-order perturbation of size o(T_lo^2).

### 6.4 Weak peaks through companions (SKETCH, not checked)
A threshold raise of size Delta-theta turns every peak with relative margin m mu_k/(q_0 Phi_k) < Delta-theta into a strict non-peak of the
companion, at companion cost O(Delta-theta) (Lemma T(e)).  So, at a window l_*, swallowing-type peaks with relative margins <= theta T_lo(l_*)^2
could be CARRIED (as inward coordinates of the companion) instead of dropped with cost t/mu; for non-degenerate peaks alpha(k) != 0, so
the d-coefficient at the companion differs from the scaled one by alpha(k)|zeta|/|zeta'| = O(mu_k), and exact d-neutrality at f_j needs a
repair of size O(sum mu_k tau_k/lambda_k) = o(t) inside the face of Section 4 (fixed R_f).  Combined with the explosive design of the Z3
referee (pairwise disjoint bands, infinitely many band-free windows), this suggests that the margin rate M_f / K_P can be removed: at a
band-free window every coarse peak margin is either below b(l) (carried) or above u(l) (dropped with a design constant).  The bookkeeping
(two thresholds per window, the repair at f_j, the composition with Lemma U') is not written out.  SKETCH.

## 7. Numerics (sanity checks only; finite blocks)
* Y2_work/threshold_check.py: 300 random blocks (size 5-13, ||Phi||_1 in [0.3, 0.95]); block norm and norming functional by SOCP
  (CLARABEL).  Lemma T(a),(b) hold to relative accuracy 5e-5 (solver accuracy).  All raising moves of types (i) (peak, +5%) and (ii)
  (nonzero strict non-peak, -5%) raise theta (minimum relative increase 1e-8 > 0); for 200 tuned degenerate peaks both moves (+-1%) raise
  theta (0 failures).
* Y2_work/companion_check.py: 35 random blocks with a tuned degenerate peak k_D and a donor move (peak +3% or non-peak -3%): theta rises
  and k_D becomes a strict non-peak in all cases; the d-coefficients Phi_k^2 w(k)/C of the unchanged non-peak coordinates and of k_D are
  multiplied by the common factor |zeta|/|zeta'| up to relative error 8e-4 (SOCP accuracy), as Step 3(d) of Proposition Q asserts.
Finite models are norm attaining; they check the block algebra only, not recoverability.

## 8. What remains (F finite), and labels

### 8.1 Status of the items of the task
(1) Peak-carrying engineering: SETTLED for SLD-type designs by companions (Proposition Q, Corollary Q'): steering is done on a companion
    at distance o(T_lo^2), where it is free; no (FS), no |F|-dimensional channel and no design change are needed.  Hypothesis: a donor
    in every block that carries degenerate peaks.  At an engineered approximant itself the steering problem is real (6.3) but irrelevant.
(2) Non-rigid degenerate swallowing-type peaks: RECOVERED under (TD) (Theorem P); automatically at maximal contact (Corollary P.1), in
    particular in the Z6 referee's Proposition R1 configuration.  OPEN only in the aligned corner (3.4): blocks without anti-sign
    swallowed peaks, without unused degenerate peaks and with only finitely many raisable carriers, where every admissible move outside
    the data supports lowers the threshold to first order.
(3) Mixed blocks / failure of (DR): REDUCED by Theorem M to one relative Farkas rate K_F^rel (zero when the d-neutral zero-cost cone meets
    the relative interior of the zero-cost cone, e.g. resonant compensators with any gaps; design-scale times K_nn in one-signed blocks).
    The residual is a genuine f-rate: zero-cost directions that are nearly but not exactly d-neutral.  Conjecture G: OPEN (6.2).
(4) Failure of (H2''): REDUCED by Theorem H to positivity (and a rate) of the shift cost c_*; explicit sufficient condition (a peak target
    at an unreachable free coordinate) and gap pinning by near-threshold q < 0 carriers.  OPEN in the coherent case (c_* = 0 or beyond the
    ladder), where exact data would need Delta d != 0 with -Delta d R_m^* w_m z-signed on all of K (5.3(c)).

### 8.2 Open core after Y2 (design D^Y, F finite, g not window-pinned)
 (r) RATES beyond the ladder: rooms of good signature sets (Lambda_g, approximate swallowing (O1)(i)); margins of non-degenerate
     swallowing-sign swallowed peaks (M_f / K_P; companions suggest a route through the explosive design, 6.4, SKETCH); gaps of swallowed
     strict non-peaks (gamma_f; for q > 0 kept carriers removable by the Z6 shift trick); rooms gamma_T at bad target coordinates; the face
     Farkas rate K_F^rel (generalized nearly-neutral rate; Conjecture G would remove its nearly-neutral part); the shift-cost rate K_sh^rel.
 (a) the aligned corner of item (d) (3.4).
 (c) the coherent shift resonance of item (h) (5.3(c)).
 (O4) infinite F (not treated here).
Density of NA((c_0,p),l_2^2) remains OPEN for every admissible T, including SLD, SLD_G, D''' and D^Y.

### 8.3 Labels
| # | Claim | Label | Where |
|---|---|---|---|
| 1 | Lemma T: threshold equation, uniqueness, strict monotonicity, perturbed version | PROVED | 1 |
| 2 | Lemma U' (inward coordinates, window-dependent A_2, gamma_B; t_1, j_0 independent) | PROVED (by inspection of refereed proofs) | 2.1 |
| 3 | Theorem E' (window-dependent c_flat) | PROVED | 2.2 |
| 4 | Proposition Q (companion transfer; thresholds rise, exact d-neutrality preserved) | PROVED | 2.3 |
| 5 | Corollary Q' (peak-carrying Corollary cor:D1, under donors) | PROVED | 2.4 |
| 6 | Lemma 3.1 (donors from (TD)), raisability bookkeeping | PROVED | 3.1 |
| 7 | Lemma 3.2 (window data with inward degenerate peaks, Z4 constants) | PROVED | 3.2 |
| 8 | Theorem P (A'' without (H3); U' without rigidity of degenerate peaks) | PROVED (given refereed A'', U') | 3.3 |
| 9 | Corollary P.1 (maximal contact: (TD) automatic) | PROVED | 3.3 |
| 10 | aligned corner of (d) | OPEN | 3.4 |
| 11 | design D^Y admissible, N-free; faces of configuration cones are free configurations | PROVED | 4.1 |
| 12 | Lemma 4.1 (Farkas pinning of the d-forced face), Lemma 4.2 (monotonicity, repair), Proposition 4.3 | PROVED | 4.2 |
| 13 | Theorem M (no (DR), no compensated/rigid dichotomy; rate K_F^rel) | PROVED (by modification of A'') | 4.3 |
| 14 | K_F in one-signed blocks = Theta(1/q_min); K_F = 0 iff C meets ri Z^0; resonant compensators give K_F = 0 | PROVED | 4.4(a),(b) |
| 15 | LP-duality reading of kappa* | HEURISTIC | 4.4(c) |
| 16 | Lemma 5.1 (peak trace of the shift) | PROVED | 5.1 |
| 17 | Proposition 5.2 (shift-cost pinning), Theorem H | PROVED | 5.2 |
| 18 | gap pinning (config. (i)); sufficient condition for c_* > 0 | PROVED | 5.3(a),(b) |
| 19 | coherent shift resonance; exact data with Delta d != 0 need -Delta d R*w z-signed on K | OPEN; observation PROVED | 5.3(c) |
| 20 | Theorem Y (master, D^Y), Corollary Y.1 (maximal contact: only rates remain) | PROVED (by combination) | 6.1 |
| 21 | Conjecture G | OPEN (budget un-switching computation: HEURISTIC) | 6.2 |
| 22 | steering at f': (a),(b) | PROVED | 6.3 |
| 23 | steering at f': (c) (tails force equal amplitudes; Gordan condition) | HEURISTIC | 6.3 |
| 24 | weak peaks through companions + explosive design | SKETCH | 6.4 |
| 25 | numerics | sanity checks only | 7 |
