# Y1 referee notes (Round 6): verification of Y1 and proofs of all corrections and additions

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; numbering and notation as there), Y1 = r6/Y1_notes.md (parts Y1_part0..5c),
refereed Round-5 results (Z3-Z6 with referee fixes). Design D_X of Y1, N >= 1, I = {1..N}, p = p_N, F = supp a finite.
Labels: PROVED / SKETCH / HEURISTIC / OPEN / FALSE. Part files: r6/Y1_ref_part1..5.md. Scripts: r6/Y1_ref_work/.
Notation (Y1): zeta_m := R_m^** zhat, A_m := |zeta_m|_m = sigma_m/q_0, theta_m := A_m M_m/C_m, nu_k := |zeta_m(k)|/Phi_m(k)^2,
rho := nu/theta (peak iff rho >= 1), margin mu = q_0 Phi theta (rho - 1)/m (eq:margin: sigma|alpha(k)| = lambda mu), gap = M(1 - rho)
off the peak set, q = eps u(zhat)/A at strict non-peaks. S^nat_{l''}(l) := S_{l''} \ (F ∪ T(l)), r^nat its sign-minimized room.

## 1. Summary of verdicts
Theorem 1 (D_X): PROVED (precision m1 on the survival of Z4 Cor. 5.4). Theorem 2: PROVED. Lemma T, T2, T3: PROVED (re-derived;
numerics 2). Lemmas 3.1-3.6: PROVED (m2: Lemma 3.6 tacitly uses (SP_w); a harmless constant m5). Lemmas 4.1-4.3: PROVED (m3: the stated
reason why a donor is class R or anti-type class G is wrong; the conclusion is right, correct proof in 3). Lemmas 5.1, 5.1', Proposition 5.2,
Theorem E', Master Theorem 5.4: PROVED. Corollaries M1, M2: PROVED (precision m4). Corollary M3: correct as a statement on hypotheses
(scope precision m6). Remark 5.6(3) (tiny repairs): plausible SKETCH, two additions (6). Residuals (n), (d): not intrinsic (7, SKETCH).
No step of Y1 had to be changed; no PROVED claim is false.

## 2. Numerics (sanity checks only)
(a) lemmaT_cert2.py: 150 random blocks (n = 6..29); the functional w(k) = sgn(zeta_k)(C/A) min(theta, nu_k), theta the root of Psi, has
N(w) = ||w||_inf + ||Phi w||_2 = 1 to 2.2e-16 and <w, zeta> = A to 5.4e-16, and A equals the primal SOCP value to 2.5e-9: an exact
norming certificate (unique, N strictly convex). [A dual-SOCP solve agrees in value; its w is indeterminate at negligible-weight
coordinates (lemmaT_peakset.py): solver behaviour, not a discrepancy.]
(b) lemmaT_indep.py: 2493 adversarial tests of Lemma T2 (half with a degenerate peak constructed by bisection, nu_c = theta; perturbations
of the maximal allowed l_1-size in the threshold-lowering direction): 0 violations of the T2(b) lower bound (minimal ratio actual/bound
8.45), 0 of its upper bound, 0 of T2(a).

## 3. Corrections and precisions
**(m1) Survival of Z4 Corollary 5.4.**  Its M^canc form uses Z4 Lemma 5.3, which needs c_l <= (delta_l ||h_l||_1)^2 (l >= 2); D_X does not
impose this. The Z4 referee's corrected form (M_f in place of M^canc) does not need it, so Theorem 1(d) is correct for that form. If the
M^canc form is wanted: c_{l+1} := min{c_l/4, b(l, M(l))^2, (delta_{l+1}||h_{l+1}||_1)^2} (computable at stage l since h_{l+1}, delta_{l+1}
are fixed in (D0); every statement of Y1 uses c_{l+1} only through upper bounds). Y1's own results do not use Lemma 5.3.

**(m2) Lemma 3.6 uses (SP_w).**  Its constant K_O contains K_P ⊃ K_d, which is defined in Lemma 3.4 under (SP_w). Statement: "Under (SP_w),
for every l'' in Sigma_m(w), |tau_{l''}| <= K_O t." Theorem 5.4 assumes (SP_w).
Addition (PROVED): a +1-one-signed block satisfies (U3) and a -1-one-signed block satisfies (L3).
Proof. At a clean w every coarse class-G carrier is an anti-type peak, a swallowing-type peak, a near-threshold strict non-peak, a strict
non-peak with rho <= b(w), or a robust strict non-peak (rho in [u, 1-u]). Sigma_m(w) contains all swallowing-type G-peaks and all G strict
non-peaks with rho > b(w) except the anti-type near-threshold ones. If sgn q = +1 on Sigma, every q < 0 carrier (anti type) is a peak, an
anti-type near-threshold strict non-peak or has rho <= b(w): (U3). If sgn q = -1 on Sigma, there is no swallowing-type G-peak and no
swallowing-type strict non-peak with rho > b(w), so every q > 0 carrier has rho <= b(w): (L3). QED

**(m3) Donors at clean sub-windows.  PROVED (correct reason).**  Y1 4.1 claims: for l >= l_f a donor c is, at every clean w, in class R or
in class G with eps_c = -vs_c, "because the exceptional coordinates lie in [1,l], outside S^nat_c". The reason is wrong: S^nat_c(l) =
S_c \ (F ∪ T(l)) does not remove [1,l]. The conclusion holds:
Let s_m = min(S_c ∩ (s_max(l), infinity)). Then s_m in S^nat_c(l) (S_c ∩ F = {}, s_m > s_max(l) = max T(l)) and vs_c z_{s_m} <= 0 once
s_max(l) exceeds the finitely many exceptional points (l >= l_f; s_max(l) -> infinity). The room in the direction sigma = -vs_c is
sum_{S^nat_c} v_c(s)(1 - vs_c z_s) >= v_c(s_m) >= delta_c 2^{-sigma(l)}/n_c. On the other hand b(w) <= T_lo(w)^4/(l Design(l)) <=
2^{-24 sigma(l)}/l, because Design(l) >= 2^{6 sigma(l)} and T_lo(w) <= T_hi(w) <= 1/Q(w) <= 1/Design(l). Since delta_c/n_c is a fixed positive
number and sigma(l) -> infinity, v_c(s_m) > b(w) >= b(w)||v_c 1_{S^nat_c}||_1 for l large. So if c is in class G, the minimizing direction is
sigma = +vs_c, i.e. eps_c = -vs_c (anti type); and then no exceptional point s_e lies in S^nat_c(l), since it would contribute
v_c(s_e)(1 + vs_c z_{s_e}) > v_c(s_e) (a fixed positive number) > b(w). Hence the donor is class R (pinned by Lemma 3.5(d)) or a class-G
anti-type peak (pinned by Lemma 3.5(a)); (C1) sets z^# = -vs_c on S^nat_c(l) ∋ s_m, and (C3) applied after (C1) has outward room
2 v_c(s_m) >= 2 delta_c 2^{-sigma(l)}/n_c; in the class-R case (C3) acts on z_{s_m} with vs z_{s_m} <= 0. Lemma 4.1's feasibility computation
applies in both cases. QED

**(m4) Corollary M2.**  The exactly swallowed anti-type peak must be non-degenerate with S_c ∩ F = {} to be a donor (a degenerate one is
still an UPPER source (U2): Z6-ref 1.2); "(DR^+_m) and (DR^-_m) nonzero" is stronger than Z4's (DR) (which allows the vacuous alternative,
cf. the Y2 referee's G1). With these provisos M2 is Theorem 5.4 + Lemma 5.1'.

**(m5) Lemma 3.1 constant.**  sum_{l''} sum_{s in S^nat_{l''}} |r(s)| <= (4/3)(6/t) sum_{l'>l} lambda_{l'} <= 4 b(w)^2/t (not 2t^7); since
b^2/t <= t^7/l^2, K_g is unchanged.

**(m6) Scope of Theorem 5.4 vs Z6 Theorem U'.**  (Cmp_w) admits compensated or one-signed blocks; Z6 U' admits RIGID blocks (every q != 0
bad carrier d-rigid; one-signed blocks are rigid) under the growth condition (W_U') on the relative Farkas rate K_R. U' survives for D_X
(Theorem 1(d)). So M3's "the rate items of (r) are no longer obstructions" holds within (Cmp_w); the open core is the intersection of the
complements of Theorem 5.4, Z6 U' and the other surviving classes.

## 4. Kind [1'] coordinates (addition).  PROVED.
In Lemma U (proofs of lem:uniformtransfer, lem:onesidedtransfer, and Z3/Y2 Lemma U along f_j), a coordinate of the first kind enters
only through Lemma lem:block(d), |sigma| <= gap(k)/(2|omega(k)|), and through ||omega||_inf in the rebalancing step. If |omega(k)| <=
2 gap(k)/t, then gap/(2|omega|) >= t/4 >= c_flat t and |omega(k)| <= 2/t. The condition gap(k) >= t^2 is never used: it is part of the
window-certificate definition, where coordinates with gap < t^2 are clamped to 0 at cost 2 t lambda_k. Hence Lemma U holds with
first-kind coordinates "gap(k) > 0 and |omega(k)| <= 2 gap(k)/t". QED

## 5. Verification notes (where Y1's text is terse)
(a) Lemma T2(b): the c-term of Bh at level theta + h is (theta+h)^2 Phi_c^2 = theta^2 Phi_c^2 + (2 theta h + h^2) Phi_c^2 (also when
nu_c < theta + h before the push), so Bh(theta+h; zeta') <= A^2 + (2theta+1) h phi + 2(theta+1)E; for the upper bound the c-term of
Bh(theta; .) is theta^2 Phi_c^2 before and after the push.
(b) Lemma 3.4 (U3): if Delta d M < 0 the upper bound is trivial; otherwise the anti-peak and anti-near-threshold terms give
Delta d M (1 + sum |q| lambda + sum |q| lambda rho) <= ..., bracket >= 1.
(c) Proposition 5.2: K_w <= C_f (1 + G**)(K_U + K_P + 1) <= C_f G**^2 l D^5 Design u^{-3} <= C_f Design^2 u^{-3} (Design = X^6, X >= l D G**);
the stated Design^3 u^{-3} is a weaker valid bound.
(d) Shift trick (Step 5): with P = vs omega^+(k) and Q = P + tau'/lambda (swallowing type), vs x := (-1.5 gap^#/t - Q)_+ gives
lambda|x| <= |tau - tau'| + lambda|Delta d| M + 1.5 lambda (gap - gap^#)_+/t; the last term is O(b/t) for robust (K1) carriers and 0 for (K4)
(gap <= b M <= gap^#). Sizes: unshifted |omega^-| <= 17/t, shifted |omega^+| <= 14.5/t; A_2 = 22 suffices. Signs of w^# at kept K1/K4
carriers equal those of w (|u(Delta)| <= (|T|+1) b << u Phi theta/m).
(e) Master theorem arithmetic: K_w T_hi <= C_f u^{omega+5} 2^{-l^3}/(l Design); n c_flat/K_w >= (l 2^{l^3} Design c/C_f) u^{-omega-4};
eps_j/(c_flat^2 T_lo^2) <= C_f T_lo log(1/T_lo)/u^2 with T_lo <= 2^{-u^{-8}}.
(f) At maximal contact a block is one-signed at infinitely many levels only if it has no anti-type strict non-peak with w != 0 (a fixed one
eventually has robust rho), and then sigma = +1.
(g) Hidden-rate audit: every quantity in the constants is a fixed f-constant (q_0, nu, sigma_m, C_m, M_m, theta_m, A_m, C_F, transfer data,
donors, repair directions) or one of the omega(l) rate objects; no slaving, no room products, and no target-induced closing terms for coarse
carriers (S^nat excludes T(l)); G**(l) is a design constant (matrix entries u_l(j), j in T(l)).

## 6. The sketch "tiny repairs by converted anti-type peaks" (Y1 5.6(3)).  SKETCH (plausible), completed as follows.
(i) The block must be RAISED (a donor, or a pull, Section 7), also when it is one-signed; near-threshold Sigma carriers then change status,
which Step 5 of Proposition 5.2 handles (they are dropped). (ii) The converted member has gap^# ~ M delta ~ T_lo^3 < t^2; by Section 4 it
suffices that |omega| <= 2 gap^#/t, and the required amount gives |omega| <= C l (|T(l)|+1) b D^2/t << T_lo^3/t. (iii) Zero cost of the
member at f^# (resonance) is a hypothesis. With (i)-(iii) the remaining bookkeeping (a (Rep) with amount-dependent gap) is routine.

## 7. Residuals (n) and (d) are not intrinsic: far pulls.  SKETCH (assembly), using Y4-referee C.2-C.7 (Round 6, not yet refereed).
Y1 says that removing (n) needs lowering a z-signed functional, impossible with banks and with only |F| - 1 Hilbert directions on F. Lowering
is possible with a FAR PULL (Round 2: P1 6.3, P2A, N2): for a closed class-G carrier l'' and j in S^nat_{l''}(l) far out, put a support mass
-eps mu at j with z_j := -eps; eps u_{l''}(zhat) drops by 2 v_{l''}(j), every other coarse value moves by O(mu ||U^* e_j^*||/nu) (O(mu^2)
for a diagonal base). The Y4 referee proves Lemma U / Theorem E with pulled and banked supports (no flip at j from t|b(j)| <= |a(j)|, with
mu_j := 24 lambda v(j)) and exact two-sided per-carrier tuning for a diagonal base (Prop. P4).
Outline for D_X: at a clean w, after (C1)-(C3), let L_0 be the kept (K3) carriers of the one-signed blocks; |val^#_l| <= C_f (|T(l)|+1) b(w);
tune val_l := 0 exactly for l in L_0 (pulls at j_l ~ log2(1/b) > sigma(l) > s_max(l); banks at min(S_l \ (F ∪ [1, s_max(l)]))). Then
Q^#_m(tau_0) = 0 in every one-signed block whatever tau_0, so (NN_w) is not needed; the companion moves by O(Design b log(1/b)) = o(T_lo^2);
other coarse values move by O(|x|^2) << b; G** is unchanged (pulls and banks lie beyond s_max(l)); the transplant balances with
kappa a/a(zhat^#). Design additions: bounded gaps G_l of the S_l (2^{G_l} in Design) and, for U = diag(s_i), 1/s_{sigma(l)}^2 in Design.
A kept weak/degenerate swallowing-type peak can likewise be pushed below threshold by a pull on its own closed signature set, replacing
(Do_w) (Y4-ref C.8(ii)). Status: SKETCH; PROVED for diagonal U once Y4-ref C.2-C.7 are refereed and the assembly is written (each step is of
a type already verified in Proposition 5.2).

## 8. What remains open (D_X, F finite, g not window-pinned)
f such that at all but finitely many levels every clean sub-window violates (SP_w), (Do_w), (Cmp_w) or (NN_w), and f outside the surviving
classes (R_0^pm, R_S, R_BT, Z4 Theorem A'', Z6 Theorem U'):
 (n) wrong-sign nearly neutral kept carriers in one-signed blocks [reducible by pulls, Section 7, SKETCH];
 (m) mixed blocks neither compensated nor one-signed (rigid ones by Z6 U' under a rate; single-block tiny rays by Y4-ref Cor. P5, SKETCH;
     multi-block rays OPEN);
 (d) aligned corner without donor [target donors of Y2-ref; pulls, SKETCH];
 (h) failure of (SP_w) [Y2 Theorem H; coherent shift resonance OPEN];
 (O4) infinite F.
Lemma Z and density of NA((c_0, p_N), l_2^2) remain OPEN for every admissible T, including D_X. No counterexample; nothing points to one.
