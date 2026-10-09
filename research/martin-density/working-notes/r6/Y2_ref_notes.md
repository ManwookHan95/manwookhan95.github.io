# Y2 referee notes (Round 6): proofs of the fixes, precisions and extensions

Setting and notation: paper/martin_density_note.tex (Sections 1, 7, 8), Round-5 reports Z3, Z4, Z6 and their referee notes, and
r6/Y2_notes.md (numbering of Y2). Finite block set I = {1..N}, p = p_N, F = supp a finite. SLD-type design as in Y2.
Labels: PROVED / SKETCH / HEURISTIC / OPEN / FALSE. Part files: Y2_ref_part1..5.md. Scripts: Y2_ref_work/*.py.
No counterexample is claimed, and nothing found points to one. Lemma Z and density remain OPEN for every admissible T.

## 0. Verdicts in one line each
Lemma T: correct. Lemma U', Theorem E': correct. Proposition Q: correct; precision (P-Q1) needed by Theorem P(b)/Theorem Y (Section 2).
Corollary Q': correct. Lemma 3.1: correct. Lemma 3.2 / Theorem P(a): fixable gap (G1) when (DR) holds vacuously (Section 4).
Theorem P(b): correct with (P-Q1). Corollary P.1: (ii) correct; (i) correct after the (G1) proviso. Aligned corner (3.4): residual of the
signature-donor method only; target donors narrow it (Section 3). D^Y, faces, Lemmas 4.1, 4.2, Proposition 4.3, Theorem M: correct
(normalization precision (P-M1); "kappa* = Theta(1/q_min) in one-signed blocks" proved only in the resonant model). Lemma 5.1,
Proposition 5.2, Theorem H: correct (5.3(a) gloss and 5.3(c) observation need precision). Theorem Y, Corollary Y.1: correct by
combination (precisions (P-Y1), (P-Y2)). Weak peaks via companions (6.4): SKETCH, three gaps (Section 5.6).

## 1. Lemma T by a primal-dual certificate (independent proof of (a), (b)). PROVED.
Let zeta in l_1 \ {0}, s_k := sgn zeta(k), nu_k := |zeta(k)|/Phi_k^2, and let theta > 0 be the unique zero of
Psi(th) = A(th)^2 - B(th) (Lemma T(c), whose proof uses neither (a) nor (b)); put A := A(theta).
Primal: x_k := s_k(|zeta(k)| - theta Phi_k^2)_+ and beta_k := s_k Phi_k min(nu_k, theta). Then zeta = x + D beta,
||x||_1 = A(theta) = A and ||beta||_2^2 = B(theta) = A^2. Hence zeta/A lies in B_{l_1} + D(B_{l_2}), i.e. |zeta| <= A.
Dual: v_k := s_k min(theta, nu_k). Some nu_k >= theta (otherwise A(theta) = 0 while B(theta) > 0, contradicting Psi(theta) = 0), so
||v||_inf = theta and ||D v||_2 = B(theta)^{1/2} = A, N(v) = theta + A. Using A = sum_{nu >= theta}(|zeta(k)| - theta Phi_k^2) and
Phi_k^2 nu_k^2 = nu_k |zeta(k)|:
  <v, zeta> = theta sum_{nu >= theta}|zeta(k)| + sum_{nu < theta} nu_k|zeta(k)| = theta A + theta^2 sum_{nu>=theta} Phi_k^2 + sum_{nu<theta} Phi_k^2 nu_k^2
            = theta A + B(theta) = A(theta + A).
So w := v/(theta + A) has N(w) = 1 and <w, zeta> = A >= |zeta|. Therefore |zeta| = A, w is the norming functional J(zeta) (unique, by
smoothness), M = theta/(theta + A), C = A/(theta + A), |zeta| M/C = theta, P = {|w| = M} = {nu_k >= theta}, and alpha := zeta/|zeta| - D^2 w/C
= x/A, so alpha(k) = 0 iff nu_k = theta on P. This is (a) and (b), together with the clamp formula w = sgn(zeta) min(theta, nu)/(theta + A).
Numerical confirmation: Y2_ref_work/lemmaT_cert.py (3000 random blocks of size 2..30; primal-dual gap 3e-14). Lemma T(e) re-tested
in 60-digit arithmetic with adversarial perturbations at 0.999999 of the stated bound: 0 violations in 1868 tests (lemmaT_e_mp.py).
First-order form (used in Sections 3 and 5.6; PROVED by the same computation): at theta = theta(zeta),
  d Psi/d theta = -2(A + theta) sum_{nu_k > theta} Phi_k^2  (right derivative; degenerate peaks count on the left),
so a change of size Delta at a non-degenerate peak raises theta at the rate A/((A + theta) sum_{nu>theta} Phi_k^2).

## 2. Proposition Q with inward strict non-peaks (P-Q1). PROVED.
Statement. Proposition Q (and Lemma 3.1) remain true if in (W2) the inward coordinates D_t of window j may be degenerate peaks OR strict
non-peaks of f (inward sign: varsigma_k omega^+(k) <= 0 <= varsigma_k omega^-(k), varsigma_k = sgn w_m(k)), with |omega^+-(k)| <= A_2(j)/t on
D_t and (W4) required only off D_t. (This is the form needed for the shift-trick coordinates of Theorem U', Z6-referee Lemma 2.1, i.e. for
Theorem P(b) and Theorem Y.)
Proof. Only Step 3(b) used that inward coordinates are degenerate peaks. Let k in D_t, block m.
(1) k is a switching coordinate: if omega^+(k) = omega^-(k), then varsigma omega^+(k) <= 0 <= varsigma omega^-(k) forces both to vanish, so k
would not be in the support. Hence its carrier is in Sw_j and, by Step 3(a), zeta'(k) = zeta(k), nu'_k = nu_k.
(2) If m in I_D: nu_k <= theta(zeta) < theta(zeta') (Step 2), so k is a strict non-peak of f_j. If m notin I_D: nu_k < theta(zeta) (strict
non-peak of f), and theta(zeta') -> theta(zeta) as Delta -> 0 (theta(zeta) = |zeta|M/C and |zeta'|, M_{j,m}, C_{j,m} converge, Step 1).
Since the union of the D_t over the n_j scales is finite, for Delta small all these k satisfy nu_k < theta(zeta'), i.e. are strict
non-peaks of f_j.
(3) If w_m(k) != 0, sgn w_{j,m}(k) = sgn zeta'(k) = sgn zeta(k) = varsigma_k, so the inward sign conditions hold at f_j; if w_m(k) = 0 the
coordinate has gap M_m and is of kind [2] (|omega| <= A_2/t, gap >= M/2 at f_j for Delta small). In all cases k is a coordinate of kind [2]
or [3] of Lemma U' at f_j.
(4) Step 3(d) used only that the coordinates of supp(omega^- - omega^+) are switching and strict non-peaks of f_j: unchanged. Steps 3(e)-(i)
and 4 are unchanged. QED

## 3. Target donors (Lemma R-T). PROVED. Consequence: the residual of (d) is smaller than the aligned corner.
Setting of Proposition Q, window j fixed, I_D the blocks with inward coordinates. Let j_1, ..., j_r be coordinates with
   j_i notin F ∪ Ba_j ∪ T_j ∪ ∪_{l in Sw_j} S_l,
signs d_i in {+1, -1} with |z_{j_i} + eta d_i| <= 1 for small eta >= 0 (both signs if |z_{j_i}| < 1, the inward sign if j_i is a contact),
and c in R_+^r. For a block m put Dz_m(k) := lambda_{k,m} sum_i c_i d_i u_{k,m}(j_i) (an l_1 vector, ||Dz_m||_1 <= sum_i c_i/3), and,
with theta := theta(zeta_m), A := |zeta_m|, s_k := sgn zeta_m(k),
  D_m(c) := 2A [ sum_{nu_k > theta} s_k Dz_m(k) + sum_{nu_k = theta} (s_k Dz_m(k))_+ ] - 2 sum_{0 < nu_k < theta} nu_k s_k Dz_m(k)
            + 2 theta sum_{nu_k = theta} (s_k Dz_m(k))_- .
Lemma R-T. (a) D_m(c) is the right derivative at eta = 0 of eta -> Psi_m(theta(zeta_m); zeta_m + eta Dz_m); it is a convex, positively
homogeneous function of the move vector. (b) If D_m(c) > 0 for every m in I_D, the conclusion of Proposition Q holds with the companion
f_j := first row with forced data (a, z + eta sum_i c_i d_i e_{j_i}), eta > 0 small. (c) For a free coordinate j (|z_j| < 1) outside the
excluded sets, D_m(e_j) + D_m(-e_j) >= 0; hence, unless both vanish, one of the two directions at j raises theta_m.
(d) Signature donors and target moves can be combined: blocks of I_D served by signature donors tolerate any O(eta) effect of the
target moves (take their own moves of size K eta, K large, with signature coordinates so far out that their cross-effects are
<= 2^{-r} K eta), so it suffices that D_m(c) > 0 for the blocks of I_D NOT served by signature donors.
Proof. (a) Termwise right derivatives of A(theta; zeta + eta Dz) = sum (|zeta_k + eta Dz_k| - theta Phi_k^2)_+: s_k Dz_k if nu_k > theta,
(s_k Dz_k)_+ if nu_k = theta, 0 if nu_k < theta (including zeta_k = 0); difference quotients are bounded by |Dz_k|, summable, so dominated
convergence gives A'_+. Termwise for B(theta; zeta + eta Dz) = sum Phi_k^2 min(theta, |zeta_k + eta Dz_k|/Phi_k^2)^2: 2 nu_k s_k Dz_k if
0 < nu_k < theta; 0 if zeta_k = 0 (the term is O(eta^2)); 0 if nu_k > theta; -2 theta (s_k Dz_k)_- if nu_k = theta; difference quotients are
bounded by 2 theta |Dz_k| + O(eta) (|min(th,a)^2 - min(th,b)^2| <= 2 th|a - b|), summable. With A(theta; zeta) = |zeta| (Lemma T(b)),
(A^2 - B)'_+ = 2A A'_+ - B'_+ = D_m(c). Each summand is linear in Dz or a positive multiple of a positive/negative part of a linear form, and
Dz is linear in the move, so D_m is convex and positively homogeneous.
(b) If D_m(c) > 0, then Psi_m(theta(zeta_m); zeta_m + eta Dz_m) > 0 for 0 < eta <= eta_m, so theta(zeta'_m) > theta(zeta_m) by Lemma T(c);
take eta <= min_{I_D} eta_m. Step 3 of Proposition Q needs only: (i) the switching carriers keep their values -- u_l is supported in
supp y_l ∪ S_l, and j_i notin T_j ∪ ∪_{Sw_j} S_l; (ii) b^+- vanish at the moved coordinates -- j_i notin Ba_j, so the side conditions at f_j
and b^+-(zhat_j) = 0 hold; (iii) the other used coordinates move continuously in eta -- they are finitely many strict non-peaks with positive
gaps. Steps 3(d)-(i) and 4 are then verbatim.
(c) Convexity and positive homogeneity give 0 = D_m(0) <= (D_m(e) + D_m(-e))/2; if both were <= 0 with nonnegative sum, both would vanish.
(d) In a block m served by a signature donor, its own move of size K eta changes zeta_m at k'_m by K eta x (x > 0 a design/f constant), which
contributes 2A K eta x (peak donor) or nu_{k'} K eta x (non-peak donor) to Psi_m up to o(eta), against O(eta) from the target moves and
<= N 2^{-r} K eta (2A + 2theta) from other signature moves (Step 2 of Proposition Q); choose K, then r. In a block served by target moves the
signature moves contribute <= N 2^{-r} K eta (2A + 2theta), which is < D_m(c) eta/2 once r is large. QED
Consequence (residual of (d)). Theorem P extends to every block m containing non-rigid degenerate swallowing-type peaks for which there is
a signature donor (TD_m) OR a family of admissible moves outside F ∪ Ba_j ∪ T_j ∪ ∪_{Sw_j} S_l with D_m > 0 (jointly with the other blocks of
I_D not served by signature donors). The genuinely open part of (d) is: blocks where, in addition to the aligned-corner conditions, every
such move has D_m <= 0 -- in particular every free coordinate outside the data supports that meets block m has D_m(e_j) = D_m(-e_j) = 0. At
maximal contact (TD) already holds. The note's sentence "every admissible z-move outside the data supports LOWERS the threshold ... so
threshold steering is impossible there" is not proved and should be replaced by this statement.

## 4. Gap (G1) in Lemma 3.2 / Theorem P(a) and its repair. PROVED (fixes (i)-(iii)); (iv) OPEN.
The gap. (DR) of Z4 has a vacuous alternative: "block m contains no swallowed strict non-peak with q_l != 0 (then tau^{m,+-} := 0)". Under
modification (M) the kept degenerate swallowing-type peaks (q_l = Phi_l M/(mC) > 0) enter the d-row of their block. In a block with such
peaks and vacuous (DR), Lemma 2.3 of Z4 cannot correct that row, and the exact (modified) cone forces tau_l = 0 on them (q > 0, tau >= 0).
Fix (i): if (DR) is non-vacuous in every block containing a degenerate swallowing-sign swallowed peak, Lemma 2.3 applies verbatim
(tau' = tau_0 + sum_m |delta_m| tau^{m,-sgn delta_m} keeps the D-components and corrects every d-row). Lemma 3.2 and Theorem P(a) hold.
Fix (ii) (finitely many degenerate peaks in a vacuous-(DR) block): drop them (impose tau_l = 0). Their drop-row violation is bounded as
follows. In block m every swallowed strict non-peak has q = 0, so by Z4 eq:didentity
   sum_{l in D_m ∩ U} q_l tau_l = -Delta d_m M_m + (1/(mC_m)) sum_{good} Phi w Delta theta + r_m - sum_{non-deg. swallowing peaks} q tau
                                  - sum_{anti-sign peaks} q tau - sum_{inactive, fine swallowed} q tau.
The terms are bounded by K_d t (Step 3), K* t/(mC), 2t/sigma, (K_d t/3 + M_f t)/C (Step 4: |tau| <= lambda K_d t + t/mu), (K_d t/3 + D)/C
(anti-sign: tau <= lambda K_d t, (tau)_- <= |tau - tau°|), 6t/C + 6t^2/C (Z4 Step 5), with |q| <= 1/C. By eq:peakshift, tau_l/lambda_l =
Delta d M + e_k >= -K_d t at every swallowing-type peak, so (tau_l)_- <= lambda_l K_d t and
   sum_{D_m ∩ U} |tau_l| <= C'(K_1 + M_f) t / q_min(D_m),
an f-constant multiple of (K_1 + M_f)t because D_m is finite. Hence Step 4 holds with its f-constant C_2 multiplied by the f-constant
(1 + C'/q_min(D_m)) (so (W_inf) is unchanged), the d-row of block m is trivially exact after the projection (all q != 0 carriers of block m
dropped), no donor is needed in block m (no inward coordinate there), and the window data at the dropped degenerate peaks are
omega^+- = 0 with discrepancy lambda(|omega_+| + |omega_-|) = |tau_l| - lambda Delta d M <= |tau_l| + lambda|Delta d|M (eq:peakshift), summable.
Fix (iii) (D''' or D^Y, any number): the same bound with q_min(D_m ∩ [1,l_*]) >= Phi_min/2 (Z6-referee 3.1) gives
sum |tau_l| <= C'(K_1 + M_f) D(l_*) t; D''' absorbs one factor D(l_*) in C_dia (Z4 Step 8 then needs D^2 G*^4 Lambda°^2 Xi_f <= c n^w, and
n^w >= (l 2^{l^3} Lambda°)^6 G*^9 D^4 for D'''), and for D^Y the face reduction of Theorem M treats these rows as d-forced rows with
kappa* <= (1 + q_max)/q_min (when they are the only d-forced rows of the block), i.e. K_F^rel <= C_f. This is Theorem V(b) of Z6 in the
one-signed case, made explicit.
(iv) OPEN for SLD_G: infinitely many degenerate swallowing-type peaks in a block where (DR) is vacuous (the factor 1/q_min ~ 1/Phi_{l_*} is not
absorbed by the windows of SLD_G: 1/c_l >= T_lo(l-1)^{-3} while T_hi(l_*) <= T_lo(l_*-1)).
Corrected statements. Theorem P(a): for SLD_G, (H3) may be replaced by (TD_m) in every block containing a degenerate swallowing-sign swallowed
peak, provided (DR) is non-vacuous in each such block or the block has only finitely many such peaks; for D''' no proviso. Corollary P.1(i):
the same proviso for SLD_G; none for D''' or D^Y (Corollary Y.1).

## 5. Precisions (all PROVED unless labelled)
5.1 (P-M1) Normalization in Lemma 4.1 / Proposition 4.3. Use the unweighted rows tau_l for (Z1) in A(U), in V_1 and in the face violation;
G** is defined with Z4's weights m_l(U,n) <= 1, so viol_{Z^0} <= V_1 and the face violation is <= viol_{Z^0} + sum_a |r_a|. With this
convention Proposition 4.3 is correct; the factor N q_max can be replaced by q_max.
5.2 One-signed blocks. 4.4(a) (resonant model) is correct as stated. In general one-signed blocks, kappa*(U) >= 1/q_{l'} - 2 for every
zero-cost swallowed strict non-peak l' with q_{l'} > 0: test Lemma 4.1 with tau = e_{l'} (zero cost, V_1 = q_{l'}, and the sign row of l' is
d-forced, so sum_a |r_a(e_{l'})| >= 1). An upper bound of the form (design constant)/q_min is plausible (SKETCH: Hoffman on the face
C(U) = Z^0 ∩ {tau_l = 0 : q_l > 0}) but not proved; Y2's phrase "kappa* = Theta(1/q_min) in one-signed blocks" should be restricted to the
resonant model. Theorem M does not use it.
5.3 Gap pinning (Y2 5.3(a)). The inequality Delta d_m M_m <= 2 gap_m(k(l))/t + (tau_l)_-/lambda_l is correct. It pins the shift at O(t)
only if gap_l <= K t^2 on the window and (tau_l)_- <= c_U/(2 m_l) is used (design factor 1/(m_l lambda_l)); for a fixed carrier the first
condition fails at small t, so it acts along windows that carry near-threshold q < 0 carriers with gaps <~ T_lo^2.
5.4 Coherent shift (Y2 5.3(c)). The constraint for exact data with Delta d != 0 is that v = sum_{m'} R_{m'}^*(delta omega_{m'} - Delta d_{m'} w_{m'})
be z-signed on K and vanish on J; off the signature sets and targets of the finitely many used carriers this concerns
-sum_{m'} Delta d_{m'} R_{m'}^* w_{m'} (all blocks together), not -Delta d_m R_m^* w_m alone. Rigorous form on far signature points: Z4-referee
Proposition 5.6'.
5.5 I_up ∩ I_lo = {} always: if both halves of (H2'') failed in block m, it would have no good peak, no anti-sign swallowed peak and no
non-degenerate swallowing-sign peak, hence no non-degenerate peak, contradicting ||alpha_m||_1 = 1.
5.6 Weak peaks through companions (Y2 6.4): SKETCH, with three gaps beyond bookkeeping. (W-a) Lemma T(e) is qualitative; carrying a peak of
relative margin r = nu_k - theta needs theta' - theta > r; by Section 1 the needed donor size is ~ r (A + theta) sum_{nu>theta} Phi^2/A plus
cross-effects, which must be o(T_lo^2). (W-b) A carried non-degenerate peak has alpha(k) != 0 at f, so inward data at f have a nonzero
first-order term; data must be built or corrected at f_j, and the face/repair constants at f_j (different peak status) must be uniform in
j. (W-c) The raise changes the status of unused weak peaks and possibly the active/kept sets at f_j.
5.7 (P-Y1) In (Y1), "r*_l(l) > 0" must read "r*_l(l_*) > 0 for every good l and every level l_* >= l" (r*_l(l_*) is nonincreasing in l_*;
Lambda*_f(l_*) = infinity otherwise). (P-Y2) Theorem Y uses Lambda*_f (all carriers), Theorem U' the good-only Lambda_g; they coincide up to
C Lambda° at maximal contact (used correctly in Corollary Y.1) but not in general.

## 6. Numerics (referee; finite models check algebra only, they are norm attaining)
* lemmaT_cert.py: primal-dual certificate of Lemma T, 3000 blocks, relative gap 3e-14.
* lemmaT_e_mp.py: Lemma T(e) in 60-digit arithmetic, adversarial lowering perturbations at 0.999999 x bound: 0/1868 violations.
* farkas_face_check.py: Lemma 4.1 on 141 random polyhedral cones with nonempty d-forced set, 28200 random tau: max(lhs - rhs) = -0.034.
* target_donor_check.py: Lemma R-T(a),(c): the sign of the one-sided derivative D agrees with the sign of the finite-difference change
  of theta (relative step 1e-9) in 2970/2970 tests, half of the 1500 blocks with a tuned degenerate peak; D(d) + D(-d) >= 0 in all blocks.

## 6a. Remark: donors are needed only for blocks whose degenerate peaks are actually used (PROVED, small improvement of (Y3))
In Theorem M/Y, if at some active set U the sign row of a degenerate swallowing-type peak l lies in the d-forced set A(U), then
tau'_l = 0 on C(U), hence omega^+-(k(l)) = 0 by (M) (min(|omega_+|, 0) = 0 and tau'/lambda = 0): the peak is not an inward coordinate at that
scale. So (Y3) is needed only for blocks containing a degenerate swallowing-type peak with tau'_l != 0 at some scale of infinitely many of
the windows used -- in particular not for blocks whose degenerate peaks are d-rigid (the analogue of Theorem V of Z6), and, by Section 3,
(TD_m) may be replaced by the existence of signature donors OR target moves with D_m > 0.
* Y2's own scripts re-run: companion_check.py reproduces "0 failures, d-ratio deviation 8e-4".

## 7. What remains open after Y2 and this report (design D^Y, F finite, g not window-pinned)
(r) Rates beyond the ladder: Lambda*_f (rooms of good signature sets, approximate swallowing), M_f (weak swallowing-type peaks; 6.4 is a
SKETCH), gamma_f (gaps of kept swallowed strict non-peaks; for q > 0 removable by the shift trick), gamma_T, K_F^rel (nearly but not exactly
d-neutral zero-cost directions; Conjecture G open), K_sh^rel (shift cost). (d') Non-rigid degenerate swallowing-type peaks in blocks with no
signature donor and no target move of positive derivative (Section 3). (h') Coherent shift resonance: c_*(l) = 0 or decaying beyond the
ladder. (O4) Infinite F. For SLD_G additionally (iv) of Section 4. Lemma Z and density of NA((c_0,p),l_2^2) remain OPEN for every admissible
T, including SLD, SLD_G, D''' and D^Y.
