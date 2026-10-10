# V2-ref part 2 — Design D^{V2} (Lemma 2.1), Lemma 2.3, Theorem B, Corollary B.1

Sources re-read: V1_notes.md 2.5-2.6, 3.1-3.8, 4.1-4.3 (V1 Lemmas B, DR, TU, CO, ST, NS, RR, Proposition TR, Theorem E'',
Master Theorem II; V1 is being refereed in parallel, V1_ref_part1-2.md: correct so far), Y4_ref_notes C.2-C.7, Z3 Prop. T
(HF), (BS), Z3 Lemma 5.1 (inward moves), the note's def:SLD, thm:SLD, lem:threshold, eq:margin.

## 1. Design D^{V2}, Lemma 2.1.  VERDICT: CORRECT (PROVED).
* Admissibility / Lemma B density: only window parameters (b(w), Design(l), omega(l)) change; (D0)-(D2), allowedness and the
  target sequence are those of def:SLD, so (T-a)-(T-d) hold as in thm:SLD.  Diagonal U and bounded gaps are free choices.
* N-freeness: an object (kappa, J, K) involves carriers of level <= l (hence at most l blocks); its polynomial has design
  coefficients (0, +-1, eps z_j u_l(j) with j in T(l)); C_L(l), N_L(l), Lip(l), delta_comb(l) are numbers attached to this
  finite N-free family.  For p_N the patterns containing carriers of blocks > N are simply never used.
* Recursion order: the polynomials of level l are fixed once y_{l''} (l'' <= l) are fixed, i.e. before the sub-windows of
  level l are defined; C_L(l), N_L(l) exist by Lemma L (non-constructive but well defined).  No circularity.
* (2.1) re-derived: beta = (1 + Lip C_*) b = min{eta, (eta/C_L)^{N_L/2}} gives C_L beta^{2/N_L} <= eta and beta <= eta <=
  1/Design < 1/C_L.  Smaller b only weakens every "b <= ..." used in Y1/Y4/V1 (I found no LOWER bound on b(w) used anywhere;
  u(w^+) = b(w) is absorbed by Q(w^+)); bands stay disjoint.
* Precision (P2.1): "Lip(l)" must be a Lipschitz constant for the Euclidean norm on [-2,2]^l, and Step 1 of Theorem B uses
  |val(f_1) - val(f)|_2 <= l^{1/2} C_* b; the factor l^{1/2} goes into Design.  Harmless.

## 2. Lemma 2.3 (buffer peaks).  VERDICT: CORRECT (PROVED), one overstatement in a parenthesis.
sum_P |alpha_m| = 1 (lem:threshold), sigma_m |alpha_m(k)| = lambda_k mu_k (eq:margin with |zeta|_m = sigma_m at xi), mu_k <=
|u_k(xi)| <= q_0, sum_{l'>l} lambda_{l'} <= T_lo(l)^3 ((P2) of thm:SLD; in D^{V2} even smaller): re-derived.  Relative margin:
rho_c - 1 = |alpha(c)| C_m/(Phi_c^2 M_m) = |alpha(c)| A_m/(Phi_c^2 theta_m) >= sigma_m/(2 l q_0 Phi_c^2 theta_m), which is
LARGER than the stated sigma_m/(2 l m q_0 theta_m) (Phi_c^2 <= m); the stated bound is valid.
Overstatement: "(these margins exceed u(w) by any design factor)" is not true at the FIRST sub-window of a level (u(w) =
b(w^-) is fixed at stage l-1, Design(l) at stage l may exceed 1/u(w)).  It is never needed: Theorem B only uses margin >>
C Design(l)^2 eta, and eta <= T_lo(w)^4 with T_lo(w) <= 2^{-4 Design(l)/u(w)}.

## 3. Theorem B.  VERDICT: CORRECT as an exactification theorem (PROVED, conditional on the cited tools; with the
reading (P2.2) of the assembly hypotheses).  Checked step by step:
* (1.0) q_l = val_l/A_m at strict non-peaks: w(k) = C zeta(k)/(Phi_k^2 A), zeta(k) = m Phi_k u_k(zhat) => q = eps Phi w/(m C)
  = val/A.  ✓  Peaks have rows tau = 0 ((Z4)); (Z5) runs over strict non-peaks of f^# (as in Prop. T step (2), "k(l) in Q").
* The minors: each (Z5)-row of block m equals (1/A^#_m)(v_l 1[l in L_0, m(l) = m]); every other entry is 0, +-1 or a design
  number.  So minors containing (Z5)-rows are (product of the 1/A^#_m of the rows used) x pi_O(val), the others are design
  numbers.  ✓  I checked that this captures the multi-block obstruction: for an extreme ray r of C(kappa) cut out by n-1
  independent tight rows A_{J'}, det[A_{J'}; Z5_m](v) = +-||c||_1 D_{r,m}(v)/A_m (c = cofactor vector, ||c||_1 a sum of
  design minors), so every V1 ray component is (design) x (a minor); and in the two-ray model the 4x4 minor equals the 2x2
  d-determinant (tworay_tau.py).  Hence Theorem B contains V1's (C4) and the determinantal objects of (m').
* Step 1-2 (Lojasiewicz): alternative (i) excluded by (2.1); robust objects stay >= u/2 (Lip eta <= T_lo^4 <= u/8). ✓
  Only the L_0-coordinates of v' are used (the polynomials of kappa do not involve the others). ✓
* Step 3 (realization): Lemma TU (V1 3.4; = Y4-ref P4 with explicit fixed point; V1-ref: correct, numerics) needs every
  l'' in L_0 exactly swallowed far out (true after (C1) for class-G carriers) and eta <= c_T = (f-const) Design^{-3}; here
  eta <= 2 T_lo^4/(l Design) << c_T. ✓  Targets v' are computed from val(f_1) and realized at the row after M_ass, so the
  second-order effects of M_ass (C Design^2 Lam^2 = O(T_lo^6)) are absorbed by exactness. ✓  Coordinates of pulls/banks/
  buffer push are pairwise distinct and beyond s_max(l). ✓
* Step 4 (statuses): with V1's donor raise Lam = T_lo^3 the extra moves 2 eta + C_T eta^2 are << c_f Lam, so V1 Lemma ST holds
  verbatim (I re-checked ST(c): (1+b)(1 + C D eta)/(1 + c_f Lam) <= 1 - c_f Lam/3 since D eta << Lam; robust carriers move
  relatively by C D eta/u << u). ✓  Buffer variant (self-contained assembly): Lemma QB with s := (16(A+theta+1)/A)
  max{E, phi(X + r_m)} gives R(s) >= 2(X + r_m), so (i) kept near-threshold carriers (nu <= theta + r_m, r_m = C_* b theta,
  C_* >= 2) become strict non-peaks with gap^# >= M^#(X + r_m)/theta^# >= gap (so V1's shift trick / kind [3] still applies:
  it needs gap <= gap^#), (ii) peaks with relative margin >= u/2 stay peaks with their sign, (iii) c stays robust.  The
  circularity (s depends on E, X, which depend on the solve) is resolved by a-priori bounds, as V2 says. ✓
  The push itself is realizable at ANY coarse peak: far signature coordinates of c are free (z-moves), contacts of sign
  vs_c (banks raise vs_c u_c), or contacts of sign -vs_c (pulls lower eps_c u_c = -vs_c u_c, i.e. push outward).  ✓
* Step 5 (cost) ✓.  Step 6 (Hoffman): Lemma H (1.3) with n <= l columns, ||A|| <= (rows cols)^{1/2} max(1, 2/A_min), the
  number of (Z5)-rows in a minor <= min(N, l): C_H^# <= (C(l)/A_min)^l (rows cols)/min(delta_comb, (2A_max)^{-l} u/2) =
  C_f^l Design(l)^2/u(w) (C_f^l absorbed since K T_hi <= C_f^{l^2} 2^{-l^3}/l -> 0). ✓  Box rows are +-e_l (Hoffman constants
  are right-side independent, 0 is feasible). ✓

Precision (P2.2) — the hypotheses (A1), (A2) and the set L_0.  As written, (A2)'s no-donor clause ("all its coarse strict
non-peaks of kappa have rho <= 1 - u/2 or rho <= C_* b") is not satisfied by V1's assembly: blocks outside V1's I_D(w) may
contain DROPPED anti-type near-threshold strict non-peaks (rho in [1-b, 1)) and anti-type tiny-margin G-peaks (pinned by Y1
Lemma 3.5).  Fix (consistent with V1 Prop. TR, whose d-rows run over the KEPT carriers Kp(w) only): take as Sigma^# the
system actually used by the transplant — d-rows over kept strict non-peaks of f^#, rows tau = 0 at dropped carriers — and
L_0(kappa) := kept carriers that are strict non-peaks of f^#.  Then the status of dropped carriers does not enter any minor
(a row tau_l = 0 is the same row whatever the status; V1 Step 5 already gives the datum 0 at dropped carriers whose status
changes), (A2)'s no-donor clause is exactly the statement that the kept carriers of non-I_D blocks are (K1)-(K3) (robust
gap or nearly neutral), and Step 4's "nu <= theta + r_m" case is needed only for a self-contained buffer assembly (where (A2)
must then allow kept carriers with |rho - 1| <= C_* b; Step 4 protects them).  With this reading Theorem B is correct.

## 4. Corollary B.1.  VERDICT: CORRECT (PROVED given V1's assembly).
(HF) with C_H^# <= C_f^l Design^2/u: from Theorem B(d).  d-row violation of the projected tau_0 at f^#: |Q^#_m(tau_0) -
(A_m/A^#_m) sum q tau_0| <= (C_* b + 2 eta) sum |tau_0| / A^#_m <= C eta/t <= C T_lo^3 << t (sum tau_0 <= 12/t).  Replacing V1's
Step 3 (ray removal under (VR_w)) by the Hoffman projection onto Sigma^# (with box rows) gives tau' in C(kappa(w)) with all
Q^#_m(tau') = 0 and ||tau_0 - tau'||_1 <= C_H^# N K_Q t; V1's later steps use only |tau - tau'|, tau' >= 0 on kept / = 0 on
dropped carriers and the box tau' <= 12 lambda/t (not V1's extra property tau' <= tau_0): checked in V1 Step 5 (shift trick:
lambda|x| <= |tau - tau'| + lambda|Delta d| M; kind [3]: tau'/lambda <= 12/t).  So (VR_w) is not needed, and (m) and (m')
are not residuals of the companion route.  Like V2, I stress: this is conditional on (SH_w)-type shift pinning (Part 3).

## 5. Numerics for Theorem B's mechanism (V2_ref_work/thmB_toy.py; sanity only)
Three blocks, three TWO-block rays arranged cyclically (r1: blocks 1,2; r2: 2,3; r3: 1,3), six carriers; values chosen with
the positive near-kernel direction mu = (1,1,1) of the 3x3 ray d-matrix, so that every ray has two ROBUST components ((VR_w)
fails), every 2x2 d-minor is robust, but the 3x3 d-determinant (a degree-3 multi-affine polynomial in the values) is ~beta.
Enumerating all square minors of [-I; configuration rows; (Z5)-rows] containing a (Z5)-row: exactly one tiny nonzero minor
(up to sign/scaling).  Nearest common zero by SLSQP: |v' - v| ~ beta (gradient nonzero here: exponent 1), all tiny minors
-> 0 (<= 1e-14), robust minors stay >= 0.3, and the true l_1 Hoffman ratio of {tau >= 0, rows = 0} drops from
4.0e2 / 5.4e3 / 2.9e4 / 3.0e5 (beta = 1e-2 ... 1e-5, i.e. ~ 1/beta, attained at tau = r1 + r2 + r3) to 1.3-1.6.
This is the "determinantal" form of (m') in its simplest genuinely 3-block shape (no 2x2 obstruction at all), and
Theorem B's mechanism removes it.
