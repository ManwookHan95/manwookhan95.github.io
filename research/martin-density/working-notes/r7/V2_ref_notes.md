# V2 referee notes (Round 7): fixes, supporting proofs, and the precise residual

Setting: paper/martin_density_note.tex (Sections 1, 7, 8), finite block set I = {1..N}, p = p_N, F = supp a finite, the design
D^{V2} of V2 (built on V1's D_Omega), diagonal base U.  Notation of V2 and V1: carrier l = j(k,m), value val_l := eps_l u_l(zhat),
A_m := |R_m^** zhat|_m, theta_m the block threshold of Lemma T (Y1), nu_k := |zeta_m(k)|/Phi_k^2, rho_k := nu_k/theta_m, kept carriers
Kp(w) and dropped carriers as in Y1 part 3 / V1 2.2.  Labels PROVED / SKETCH / HEURISTIC / OPEN.  Report: V2_referee.md; part files
V2_ref_part1..4.md; scripts V2_ref_work/.

## 1. Lemma QB with k_0 = c allowed (fix P1).  PROVED.
Statement (as V2 Lemma QB, with one change): C_1 := (1 + 2(theta+1)/A)/Phi_{k_0}^2 and h_0 := min(1, nu_{k_0} - theta), where k_0 is ANY
non-degenerate peak of zeta, k_0 = c allowed.  Then (a)-(c) of V2 Lemma QB hold.
Proof.  (a), (b) do not involve k_0.  For (c) it suffices to prove theta(zeta') <= theta + C_1(s + E) when C_1(s + E) < h_0; the rest
of (c) is as in V2.  Let h := C_1(s + E) + epsilon <= h_0 (epsilon > 0 small).  Since h <= nu_{k_0} - theta, k_0 belongs to the peak
set of zeta at level theta + h, i.e. |zeta(k_0)| - (theta + h)Phi_{k_0}^2 >= 0.  Write Ah(x; .) and Bh(x; .) as in Y1 Lemma T.
(i) Every term of Ah is 1-Lipschitz in |zeta(k)|; the c-term changes by s and the others by E in total, so Ah(theta+h; zeta') <=
Ah(theta+h; zeta) + s + E.  Moreover Ah(theta+h; zeta) <= Ah(theta; zeta) - h sum_{k: nu_k >= theta + h} Phi_k^2 <= A - h Phi_{k_0}^2,
because each term with nu_k >= theta + h decreases by exactly h Phi_k^2, the terms with theta <= nu_k < theta + h become 0, and the
others are 0 at both levels (Ah(theta; zeta) = A by Lemma T(b)).  Hence
Ah(theta+h; zeta') <= A + s + E - h Phi_{k_0}^2 =: A - y, and y = h Phi_{k_0}^2 - s - E > 0 by the choice of h.
(ii) Bh is nondecreasing in x, and every term of Bh(theta; .) is 2 theta-Lipschitz in |zeta(k)|; the c-term of Bh(theta; .) equals
(theta Phi_c)^2 both for zeta and zeta' (c is a peak of both at level theta, since the push is outward).  So Bh(theta+h; zeta') >=
Bh(theta; zeta') >= Bh(theta; zeta) - 2 theta E = A^2 - 2 theta E (Lemma T(b)).
(iii) 0 < y < A: positivity by the choice of h; and h Phi_{k_0}^2 <= (nu_{k_0} - theta) Phi_{k_0}^2 = |zeta(k_0)| - theta Phi_{k_0}^2 =
A |alpha(k_0)| <= A (Lemma T(a)), so y <= A - s - E < A.  Hence 0 <= Ah(theta+h; zeta') <= A - y and
Psi(theta+h; zeta') <= (A - y)^2 - A^2 + 2 theta E = -y(2A - y) + 2 theta E <= -yA + 2 theta E < 0, because yA = A(h Phi_{k_0}^2 - s - E) >
A(C_1 Phi_{k_0}^2 - 1)(s + E) = 2(theta + 1)(s + E) > 2 theta E.  By Lemma T(c), theta(zeta') < theta + h; let epsilon -> 0.  QED
(With k_0 != c this is Y1's proof; the only point is that the c-term of Ah grows by s, which (i) accounts for.)  Numerics: V2_ref_work/
qb_jac_check.py, k_0 drawn among all non-degenerate peaks including c: 0 violations in 891 upper-bound and 6629 peak-preservation tests.

## 2. Ray components are minors (supports Theorem B and Corollary B.1).  PROVED.
Lemma R.  Let C = {tau in R^n : A_nd tau <= 0} be a pointed polyhedral cone (equalities written as two rows), r an extreme ray with
||r||_1 = 1, and d in R^n any row vector.  There is a set J' of n - 1 linearly independent rows of A_nd, tight at r, such that
     det [A_{J'}; d] = +- ||c||_1 (d . r),       c_i := (-1)^{n+i} det A_{J', [n] \ {i}},   c != 0.
Proof.  The rows tight at r have rank n - 1 (r is extreme in a pointed cone), so pick J' independent among them.  Laplace expansion
along the last row gives det[A_{J'}; d] = d . c for every d; with d a row of A_{J'} the determinant vanishes, so c is in ker A_{J'} =
R r, and c != 0 because A_{J'} has rank n - 1.  So c = +-||c||_1 r.  QED
Consequence.  With d = the (Z5)-row of block m of A_kappa(v) (entries v_l at kept strict non-peaks of block m), d . r = D_{r,m}(v)
(V1's ray component; r vanishes at peaks and dropped carriers by the rows tau = 0), and ||c||_1 is a sum of absolute values of
DESIGN minors (only rows of A_nd are involved), between delta_comb(l) and (rows cols)^l x design.  Hence every V1 ray component is a
design multiple of a minor object of V2, tiny components are tiny minors (after adjusting b by the design factor, which a clean
sub-window of the enlarged scheme allows), and Theorem B's exactification contains V1's (C4).  The converse fails: the cyclic
three-block configuration (V2_ref_work/thmB_toy.py) has all ray components and all 2x2 d-minors robust and a single tiny 3x3
d-determinant; its l_1 Hoffman ratio is ~ 1/beta.

## 3. Theorem B read with the transplant's own system (fix P2).  PROVED (given V1 as refereed).
Replace in V2 2.0 / Def. 2.1 / Theorem B the system Sigma^# by the system of V1 Proposition TR:
 (Z1) tau_l >= 0 (l in Kp);  (Z2) type(j) L_j(tau) >= 0, (Z3) L_j(tau) = 0 on T(l) \ F as in V1 2.6;  (Z4') tau_l = 0 for l in G \ Kp
 (dropped carriers) and at peaks of f^#;  (Z5) sum_{l in Kp, m(l)=m} (val^#_l/A^#_m) tau_l = 0 (m in I);  (box) tau_l <= 12 lambda_l/t,
and put L_0(kappa) := Kp (every kept carrier is a strict non-peak of f^#, V1 Lemma ST(c)); the pattern kappa records Kp.  Then:
(i) The minors are as in V2 (only (Z5)-rows depend on values; rows (Z4') are unit rows whatever the status of the dropped carrier),
so the status of DROPPED carriers at f^# does not enter Sigma^#; V1 Step 5 already gives the datum 0 at dropped carriers whose status
changes.  (ii) (A2) holds for V1's assembly: in blocks with a donor raise, V1 Lemma ST (with V2's extra moves 2 eta + C_T eta^2 << c_f Lam);
in blocks without one, every kept carrier is of kind (K1), (K2) or (K3) (V1 Lemma ST: non-raised blocks hold only robust or nearly
neutral kept carriers), i.e. rho <= 1 - u or rho <= b.  (iii) No sign flips: the 1x1 objects |v_l| (a (Z5)-row and the column l) are in
the scheme; if tiny, Lemma L sends v_l to exactly 0 (exactly d-neutral, kind (K3)); if robust, |v'_l - v_l| <= eta << u <= |v_l|.  So
the TYPE of every kept carrier is kept or it becomes exactly d-neutral.  (iv) Self-contained buffer variant: if a block has kept
near-threshold carriers (|rho - 1| <= C_* b, C_* >= 2) and no donor raise, Step 4 of V2 (Lemma QB as fixed in 1) makes them strict
non-peaks with gap^# >= M^#(X + r_m)/theta^# >= gap, which is what V1's shift trick (kind [3]) needs.
With this reading every step of V2's proof of Theorem B applies verbatim, and Corollary B.1 follows: the Hoffman projection of tau_0
onto Sigma^# (box rows included) gives tau' with all (Z5)-rows zero and ||tau_0 - tau'||_1 <= C_H^# sum_m |Q^#_m(tau_0)|; V1's Steps 3-5
use only ||tau - tau'||_1, the sign rows and the box (not V1's additional tau' <= tau_0).

## 4. Rate-object bookkeeping for the shift system (fixes P3, P4).  PROVED.
(P3) Enlarged shift pattern.  A shift pattern of level l is kappa^sh = (kappa, N_0, R_7, I_sh, src, G_pk, F_T) where kappa is a pattern
of 2.0 (with Kp), N_0 ⊂ G the nearly neutral carriers (q' := 0), R_7 ⊂ G the anti-type near-threshold strict non-peaks of (R7), I_sh
the source-deficient blocks with their source types (U1)/(L1) for (R6), G_pk the class-G peaks kept as peaks (tiny-margin peaks
declared non-peaks are in G \ G_pk), F_T := F ∩ T(l).  There are at most 2^{C(l + |T(l)|)} of them: design-countable and N-free.
For each kappa^sh, rho^sh(kappa^sh, f) := min{viol(delta, tau) : ||delta||_1 = 1} (an LP minimum over finitely many polytopes,
attained) is a number depending on f only.  At a clean sub-window of the scheme containing all of them, the shift pattern of f at w
is one of them, so Theorem C1 holds as stated.
(P4) Corollary C1.1(a) repaired.  Replace the weight 2 m^nat_{l'}(l) by the design number 2 m^d_{l'}(l), m^d := ||v_{l'} 1_{S_{l'} \
([1,l] ∪ T(l))}||_1 <= m^nat (F ⊂ [1,l] for l >= l_f), and define c^comb_*(kappa^sh) as the minimum of c^comb(.; kappa^sh) over
{delta in R^{I_sh} : ||delta||_1 = 1, delta_m <= 0 for (U1)-blocks, delta_m >= 0 for (L1)-blocks}.  Claim: for every (delta, tau),
     ||delta||_1 <= (C Design(l)/c^comb_* + 2) viol(delta, tau)   whenever c^comb_* > 0.
Proof.  V2's computation gives c^comb(delta_{I_sh}; kappa^sh) <= C Design viol(delta, tau) (the T(l) terms by (R1)-(R3), the signature
terms by (R1)+(R2) at G-peaks; the peak traces of blocks outside I_sh enter L - V(tau) only through (R2) defects and |delta_m| <= (R5)
violation).  Let delta' be the l_1-nearest point of the sign cone to delta_{I_sh}: ||delta' - delta_{I_sh}||_1 <= (R6) violation;
c^comb(.; kappa^sh) is C Design-Lipschitz in delta (L is linear in delta with ||Pi_m||_1 <= 1, phi_z is 2-Lipschitz, the sign-defect terms
are lambda-Lipschitz).  So c^comb_* ||delta'||_1 <= c^comb(delta') <= C Design viol, and ||delta||_1 <= ||delta'||_1 + (R6) + (R5)
violations.  QED  Hence rho^sh >= c^comb_*/(C' Design) >= delta_sh(l)/(C' Design) > b(w) and case (I) holds at a clean w.

## 4b. Two independent pinning criteria; Master Theorem III' (precision P7).  PROVED (given V1, refereed correct).
(i) rho^sh >= u does not obviously follow from V1's c_{pi(w)} >= u, nor conversely.  V1's c(delta; pi) = inf_x sum_{j notin F}
phi_{z_j}(sum_m delta_m Pi_m(j) + sum_{Bf} x_l eps_l u_l(j)) uses the z of f on ALL of F^c; on a class-G signature set with tiny
room r^nat > 0 and on a tiny target room it charges b-weighted terms proportional to |coefficient|, which the rows (R1)-(R7) (written
for the closed pattern) do not see.  For the actual decomposition at scale t these terms are <= 6 b lambda/t << t^3 (box), so V1's
Lemma S pins the shift; but rho^sh is an infimum over unconstrained tau and a near-solution of Sigma^sh may need ||tau||_1 of the
order of the inverse of a small f-dependent minor of Sigma^sh, in which case b ||tau||_1 is not small.  Conversely c_pi only sees the
peak traces and the zero-cost condition, not the d-identity (R4), so rho^sh can be robust while c_pi is tiny.
(ii) MASTER THEOREM III'.  Design D^{V2} on V1's D_Omega (whose rate scheme contains the shift costs c_pi), diagonal U, F finite.  If
at infinitely many levels some clean sub-window w satisfies rho^sh(kappa(w), f) >= u(w) or (SH_w), then f in Rec.
Proof.  Either alternative gives |Delta d_m| M_m <= K t for every block m and every scale t of W(w), with K <= C_f Design^3/u^3
(Theorem C1(I)) resp. K <= C_f l D^3/u^2 (V1 Lemma S).  V1's Master Theorem II uses (SH_w) only through this bound (V1-ref) and
(VR_w) only in Step 3 of Proposition TR, which Theorem B / Corollary B.1 replace (§3).  The remaining window arithmetic is V1's.  QED
(iii) Residual.  f notin Rec only if, at all but finitely many levels, EVERY clean sub-window has rho^sh(kappa(w), f) <= b(w) AND
c_{pi(w)}(f) <= b(w) (in particular I_sh(w) != {}).

## 5. Corollary C3.1(c) needs constant contact sign (fix P5).  PROVED (as a statement about what is proved).
(i) If z = eps_0 on N \ F, then (SP_w) holds at every clean w of large level (Y1 Cor. M1 via Z4 Lemma 5.0), so rho^sh >= 1 (rows
(R5)) and case (II) does not occur.  (ii) If |z| = 1 on N \ F with signs not eventually constant, the identities of C3.1(b) are void
(there are no free coordinates), but (SP_w) is not guaranteed by the cited results: Z4 Lemma 5.0 gives, at every f, coarse peaks with
w = +M and w = -M and margins >= q_0/4; their TYPE is eps_l sgn w(k(l)), where eps_l is the sign swallowing S_l.  Signs on the S_l
can be prescribed carrier by carrier, from coarse to fine (u_l depends on S_{l'} only for l' <= l, allowedness (a)): with z := sigma on
S_l \ F, u_l(zhat) = (y_l(zhat) + delta_l(sigma ||h_l||_1 + h_l(Ue)))/n_l; "self-aligned" (sgn u_l(zhat) = sigma) is always achievable,
and "anti-aligned" (sgn u_l(zhat) = -sigma) whenever |y_l(zhat) + delta_l h_l(Ue)| > delta_l ||h_l||_1.  Suppose every coarse peak of
block m is self-aligned and block m has a strict non-peak with robust relative position that is anti-aligned (nothing in the cited
results excludes this at full contact).  Then every coarse peak of block m is a class-G peak of swallowing type, so (U1) and (U2) fail,
and (U3) fails because of the anti-type strict non-peak.  So block m is in I_sh and case (II) is not excluded by the cited results.  (No claim that it occurs; with ALL carriers self-aligned there is no q < 0
carrier at all and (U3) holds vacuously.)

## 6. Lemma C5 and the route of Theorem C6 (precision P6; gaps g4, g5; a route for g3).
(P6) Lemma C5 completes ONE ray of shift vectors.  PROVED.  W_Delta = sum_m Delta_m X_m with X_m := R_m^* w_m(z') is linear in Delta,
so the fixed point z'* for Delta also completes c Delta, c > 0.  For a family of shift vectors spanning a cone with two independent
generators Delta^(1), Delta^(2), admissibility at a free coordinate j requires W_{Delta^(1)}(j) = W_{Delta^(2)}(j) = 0, i.e. X_m(j) = 0
for every m in the span, and at a contact z_j W_{Delta^(r)}(j) <= 0 for both r; a clamp map built from any one combination yields
admissibility of that combination only.
(g4) [OPEN gap of Theorem C6] In case (II) the actual shift delta(t) is not pinned and its direction may vary with t across the scales
of a window; Theorem E (and E^>=, E^SC) averages the data of all scales at ONE companion.  With one shifted block the direction is a
fixed sign (configuration (i) or (ii)) and (P6) is harmless.  With two or more shifted blocks one needs either a transplant that puts
all scales of a window on one shift ray with error O(K t) (a possible handle: by Proposition C4 each block's data shift must dominate
the oscillation of the mate's own profile, a quantity independent of t, so a canonical t-independent choice Delta*_m := -osc_m/(lambda M)
is suggested — whether the switching can absorb the difference is again a resonance question), or per-block fine admissibility.
(g5) [OPEN gap] Lemma C5 moves z on J_fine and thereby changes the fine residues on the coarse coordinates which (ST_w) must absorb; a
joint fixed point (Schauder-Tychonoff on (z'_fine, coarse data), using continuous dependence of the Slater absorption on the residue)
is plausible but not written.
(g3) Route to (SC) at companions (SKETCH).  (SC) fails at a first row only through peaks with margin, or strict non-peaks with gap or
Phi x gap, below Upsilon s for s in a sequence tending to 0.  For the SLD weights Phi_{l'+1} <= c_{l'+1} <= T_lo(l')^3, which is far below
the signature room delta_{l'} ||h_{l'} 1_{far}||_1 of every carrier of level l'.  A regularizing companion that pushes, level by level
(l' = l+1, l+2, ...), every fine carrier by z-moves on its own far signature coordinates to margin or gap >= (its signature room)/4
costs <= sum_{l'>l} lambda_{l'} x O(1) = O(T_lo(l)^3) and moves every threshold by <= C c_{l'+1} after level l', which preserves the
pushes already made; with s_{l'} := (Phi_{l'+1} x room_{l'})^{1/2} the carriers of levels > l' contribute <= 2 Phi_{l'+1} = o(s_{l'}) and
those of levels <= l' contribute 0, for every Upsilon.  The coarse carriers need margins/gaps bounded below, which V1's companion
provides (donor raise; dropped carriers pushed if necessary).  This competes with Lemma C5 for the same coordinates (see g5).

## 7. Numerics (V2_ref_work; sanity checks only)
qb_jac_check.py (Lemma QB, k_0 = c allowed: 0 violations), jac_check2.py (Remark 4.5: entries to 4.7e-7, det ratio 1.000000),
tworay_tau.py (two-ray example in tau-coordinates: minor = delta, Hoffman ratio 4/delta; 1 at delta = 0; Lemma H bound ~22/delta),
thmB_toy.py (cyclic three-block degree-3 obstruction: tiny 3x3 d-determinant only; exactification by a value move ~beta; Hoffman
ratio 4e2-3e5 -> 1.3-1.6; robust minors >= 0.3 after).  V2_work/hoffman_minors_check.py re-run: identical.

## 8. Status after V2 and this report (design D^{V2} on V1's D_Omega, diagonal U, finite I)
PROVED (with fixes P1-P7): Lemmas H, L, QB, the two-ray example, D^{V2} and Lemma 2.1, Lemma 2.3, Theorem B, Corollary B.1, Lemma 3.1,
Definition 3.2, Theorem C1, Corollary C1.1, Master Theorem III' (4b), Theorems E^>=, E^SC, Proposition C3, Corollary C3.1(a),(b),(c) [(c) for constant-sign
maximal contact], Proposition C4 with the Example, Lemma C5, Remark 4.5, Master Theorem III (given V1, refereed correct).
SKETCH: near-coordinate conversion; Theorem C6 (gaps g1-g5); the (SC)-regularization route.
OPEN: (C*) [F finite: at all but finitely many levels every clean sub-window has rho^sh(kappa(w), f) <= b(w) and c_pi(w) <= b(w) (4b);
sub-issues C*-1 exact
absorption of fine-peak residues on coarse free coordinates, C*-2 (SC) at companions in configuration (i), C*-3 block-scalar
exactification, C*-4 scale-dependent shift directions with >= 2 shifted blocks, C*-5 joint completion]; (E) infinite F.
Lemma Z and density of NA((c_0,p_N), l_2^2) and NA((c_0,p), l_2^2) remain OPEN for every admissible T, including D^{V2}.

## 9. Re-derivations recorded (selection; full logs in V2_ref_part1..4.md)
(a) d-coefficients at strict non-peaks (V2 (1.0)).  lem:threshold: off P, w(k) = C zeta(k)/(Phi_k^2 |zeta|); with zeta = R_m^** zhat,
zeta(k) = m Phi_k u_k(zhat), |zeta| = A_m: q_l = eps_l Phi_k w(k)/(m C) = eps_l u_k(zhat)/A_m = val_l/A_m.  Also A_m <= ||zeta||_1 <=
m sum_k Phi_m(k) <= m 2^{-m} <= 1/2, so the row factors 1/A_m in Theorem B(d) are >= 2.
(b) Lemma H.  Projection x* onto P; x - x* = A_J^T v, v > 0, J independent and active (normal cone + conic Caratheodory);
||x - x*||^2 = v . (A_J x - b_J) <= ||v|| ||(A_J x - b_J)_+||, ||v|| <= ||x - x*||/sigma_min(A_J); Cauchy-Binet gives
sigma_min(A_J) >= max_K |det A_{J,K}|/||A_J||^{|J|-1}.
(c) Lemma 2.3.  sum_P |alpha_m| = 1, sigma_m |alpha_m(k)| = lambda_k mu_k (eq:margin), mu_k <= q_0, sum_{l'>l} lambda_{l'} <= T_lo(l)^3:
fine peaks carry <= q_0 T_lo^3/sigma_m <= 1/2 of the alpha-mass for l >= l_f, so some coarse peak has |alpha| >= 1/(2l); its relative
margin is |alpha(c)| A_m/(Phi_c^2 theta_m) >= sigma_m/(2 l q_0 Phi_c^2 theta_m) (>= V2's stated bound since Phi_c^2 <= m).
(d) Remark 4.5.  dPsi/dtheta = -2(A + theta) Phi_P^2; peak push: dPsi/ds = 2A, so dtheta/ds = A/((A+theta)Phi_P^2) = C/Phi_P^2 and
dA/ds = 1 - Phi_P^2 dtheta/ds = M; strict non-peak push: dPsi/ds' = -2 nu_k, dtheta/ds' = -rho_k M/Phi_P^2, dA/ds' = rho_k M;
det = rho_k M (C + M)/Phi_P^2 = rho_k M/Phi_P^2 (M = theta/(A+theta), C = A/(A+theta)).
(e) Theorem C1.  viol is positively homogeneous of degree 1, so viol(delta, tau) >= ||delta||_1 rho^sh for every (delta, tau) with
delta != 0; with Lemma 3.1, ||delta||_1 <= C_f Design^2 K_g t/(u rho^sh).  (R5) alone gives rho^sh >= 1 when I_sh = {}.
(f) Theorem E^>=.  In Z3 Theorem E, bound (A) applies Lemma U to the side-+ pair for r > 0 and to the side-- pair for r < 0 separately
(each represents g_{j,t_i}); averaging is linear and preserves side admissibility and Delta d_m >= 0; cor:D1 at f_j needs exactly
Delta d_m >= 0 and kappa_w <= 1.
(g) Data vs decomposition shift.  For two-piece data with effective switching tau^{data}_l := eps_l lambda_l((omega^- - omega^+)(k) -
Delta_m w(k)) (all carriers), b^+ - b^- = sum_l eps_l tau^{data}_l u_l and Delta_m (1 - sum_{k in Omega_m} Phi_k^2 w(k)^2/C_m) =
sum_{Omega_m} q_l tau^{data}_l; at peaks tau^{data} = -eps vs lambda Delta M.  This matches (R2)-(R4) of V2 with delta_m = -Delta_m M_m
(Delta = data convention), the non-switching carriers' traces being, in the decomposition version, part of the class-R / fine error.
(h) Proposition C3, C4: subtraction of the two representations; sandwich on S^nat_l of a class-G peak (V2_ref_part4 §1, §3).
(i) Lemma C5: Schauder-Tychonoff on [-1,1]^{J_fine} with the clamp map; continuity by dominated convergence and weak* continuity of the
duality maps of the smooth norms |.|_m (V2_ref_part4 §4).
