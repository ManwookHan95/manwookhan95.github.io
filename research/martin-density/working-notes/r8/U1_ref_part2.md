# U1 referee, part 2 — Lemma 2.1, activity classes, Proposition 2.2, Theorem 2.3, Lemma 2.4

Scripts: U1_ref_work/status_rigidity2.py (+ .out); U1's shift_bound_check.py, recursion_check2.py re-run (identical output).

## 2.1 Lemma 2.1 (shift bound).  Verdict: CORRECT (PROVED).
Re-derived: H_m(x) = ||P^perp_{Dw} D x||^2/C (note, def. of H_m), so sqrt(H) is a seminorm and H(Domega) <= 8/sigma'; with v := D(w' 1_Omega),
chi := ||v||^2/C'^2: Delta = a chi C', C' H >= a^2 C'^2 chi (1 - chi), hence Delta^2 <= H C' chi/(1 - chi), and 1 - chi >= M'^2 Phi_P^2/C'^2
because Omega ⊂ Q'.  U1's numerics re-run (5220 tests, sharp).  Delta_max = C_f at companions: correct (a non-degenerate peak of f persists).

## 2.2 Activity classes (2.3).  Verdict: CORRECT (PROVED), precision (p-a).
Pigeonhole over J+1 intervals is right.  (p-a) The thresholds must be separated by the FULL Hoffman constant of Gamma^#(kappa, a) in the row
normalization used (it contains 1/lambda_l <= D(l) through the inward rows, see (p-b)); then zeroing the components below A_{i(t)} K t and
re-projecting onto Gamma^#(kappa, a(t)) moves no active component across A_{i(t)+1} K t (I checked the potentially dangerous case of an inward
row coupling a small switching gamma_d with a large shift Delta'_m: it forces lambda_d rho_d K_* >= 1, i.e. it cannot occur once K_* >= 2 D(l)).
The class may equally be read off the decomposition data directly (no projection needed for the bookkeeping).

## 2.3 Proposition 2.2 (projection, normalization to one ray).  Verdict: CORRECT after precisions (p-b), (p-c), (p-d); its part (b) inherits
the gap of Theorem 2.3 (Section 2.4 below).
(p-b) [the row (X4) is mis-stated; fix PROVED].  U1 writes the inward row of a kind-[3] carrier as "vs_l gamma_l >= 0".  The kind-[3]
condition (V1 TR(iii): vs omega^+ <= 1.5 gap/t, vs omega^- >= -1.5 gap/t, after the shift trick) needs vs Domega(k) >= -3 gap^#/t with
Domega(k) = gamma_l/lambda_l + Delta_m w^#(k), i.e. vs gamma_l/lambda_l + rho^#_l Delta'_m >= -3 gap^#/t.  With "vs gamma >= 0" alone:
in configuration (ii) the decomposition violates the row by lambda Delta' (not O(t)), so (a) fails; in configuration (i) the row does not
imply the kind-[3] condition.  Correct row (design coefficients):  vs_l gamma_l/lambda_l + Delta'_m >= 0.  Proof that it works:
(1) points of the cone satisfy vs Domega = (vs gamma/lambda + Delta') - Delta'(1 - rho^#) >= -|Delta'| gap^#/M >= -3 gap^#/t (|Delta'| <= C_f,
t small); (2) the decomposition satisfies it up to lambda(3 gap(f)/t + C_f b) (lem:suplevel(f) at strict non-peaks; at peaks of f,
vs(omega_- - omega_+) = e_k >= 0 by eq:peakshift).  The row must be imposed on EVERY coarse strict non-peak of f^# with gap^# < t^2 in
Omega (raised (K4) carriers, and also the dropped (P-ii) carriers, raised tiny-margin peaks and class-R near-threshold strict non-peaks, all of
which U1 puts into Omega; V1 had datum 0 there).  For class-R near-threshold strict non-peaks of an ACTIVE NEGATIVE block the row cannot hold
with gamma = 0 — but such a carrier pins Delta'_dec >= -C_f D K_g t (lem:suplevel(f) with |Delta theta| <= K_g t), so it does not occur in an
active negative block (same for (P-ii), V2's (R7)); in active positive blocks the row holds with gamma = 0.
(p-c) [minors of the Delta'-projections].  A_max in 2.4(c) needs a lower bound for sigma_min(g_J); the minors of the matrices g_J (Delta'-parts
of extreme rays) are not minors of Gamma^# but polynomials in them (rays = cofactor vectors).  Add these polynomials (unnormalized cofactor
rays) to the rate objects and to the Lojasiewicz family; then sigma_min(g_J) >= robust/poly by Cauchy-Binet.  Also: the (X1) rows on a near
signature set are scaled copies of ONE sign row (coefficients v_l(s) down to 2^{-s_far}); aggregate them (l_1 violations add up to the
single row with coefficient ||v_l 1_{near}||_1, a design number), otherwise Lemma H's "least nonzero minor" would see 2^{-s_far}.
(p-d) [signs of increments].  incr(t) is in Gamma^#(kappa, a); its Delta'-part has the sign of the active blocks because (X2) at the robust
coarse peak of every block (Lemma D) forces sgn Delta'_m (an active negative block has only swallowing-type robust G-peaks, an active positive
one only anti-type); hence Delta'^* >= Delta'(t) componentwise in absolute value and activity/signs are preserved.  (Implicit in U1; checked.)
The normalization idea itself (increments of FIXED size p epsilon added to the minus side only; sqrt(Gamma) grows by C_f p epsilon; the
represented functional is untouched) is correct and neat.

## 2.4 Theorem 2.3 (exactification with one scalar per block).  Verdict: GAP (not proved); fixed under an extra hypothesis (KN_w).
The proof asserts "after V1's moves (C1)-(C3) (which move values and kappa by <= Design b)".  FALSE for (C3): V1's donor raise moves the
donor's zeta-entry by [Lam, 3 Lam] (V1 Lemma DR(i)), hence kappa_m by (1 - X)[Lam, 3 Lam] (Lemma 1.4(a)), Lam = T_lo^3 >> Design b.
Then either (i) the Lojasiewicz point is computed before (C3) and the kappa-push of (1a)/(1c) restores kappa — but all peaks act identically
on (theta, A, kappa) (Lemma 1.4(a)), so restoring kappa by a peak push restores theta and UNDOES the raise (numerically exact: (2) of
status_rigidity2.out, theta - theta_0 = 0 to 40 digits); then V1 Lemma ST(c) (K4 carriers become strict non-peaks with gap >= c Lam M/3),
which U1's Lemma 4.5 quotes, no longer holds; or (ii) it is computed after (C3): then the tiny minors are only <= b + Lip Lam and the
Lojasiewicz distance C_L (Lip Lam)^{2/N_L} is NOT <= T_lo^4 (it exceeds Lam for N_L > 2), and realizing it destroys the statuses.
The obstruction is structural (PROVED, Lemma R-kt below): the shifted exact system depends on the block data only through the RATIOS
r_l := u_l(zhat)/kappa_m (l in Omega_m) (Lemma 1.3: (X3) is the only row carrying values or kappa), and so do the relative positions:
 LEMMA R-kt (status rigidity in ratio space).  PROVED.  For a block with peak set P and switching set Omega ⊂ Q put R^2 := m^2 sum_{Omega} r_l^2,
 S_f := sum_{Q\Omega} nu^2 Phi^2.  Then a := A/theta and k := kappa/theta satisfy a^2 = Phi_P^2 + k^2 R^2 + S_f/theta^2, k = a + Phi_P^2 + S_f/theta^2,
 and rho_l = m r_l k/Phi_l for l in Omega.  Proof: (E2) and the second form of kappa, divided by theta^2, with sum_{Omega} nu^2 Phi^2 = kappa^2 R^2.
 Consequently, if Q \ Omega consists of fine carriers only (U1's final form), the relative positions of all Omega carriers are functions of
 (r, Phi_P^2) up to O(S_f/theta^2) = O(c_{L+1}^2): ANY move that keeps the ratios fixed keeps every status fixed.
Numerics (status_rigidity2.out): donor raise of 1e-6 lowers rho of a near-threshold Omega carrier by 1.04e-6; restoring the active ratios
by scaling the Omega values gives rho changes of 1e-22 (pure fine-term effect): the protection disappears.
Hence a near-threshold switching carrier d (|rho_d - 1| <= b at f, nonzero switching in the class) can be kept a strict non-peak at an exact
point only if either the exact zero set Z of the tiny minors (in ratio space) contains, within the realizable distance, points with
rho_d < 1, or the block has a KAPPA-NEUTRAL LEVER.
FIX (PROVED) under
 (KN_{w,a}) every active block m that contains an ACTIVE near-threshold Omega carrier (|rho - 1| <= b(w) at f, switching active in the class a)
            also contains an INACTIVE Omega carrier d_0 (gamma = 0 in the class) with rho_{d_0} >= u(w).
Construction: no donor raise in active blocks; Lojasiewicz point r' in RATIO space (variables r_l of the active Omega carriers; polynomials =
the minors of Gamma^#(kappa, a) after dividing (X3)_m by kappa_m, plus the cofactor minors of (p-c)) within eta of r(f_1); realize
u_l := r'_l kappa^# by Lemma TU; raise theta kappa-neutrally by an inward push of d_0 (Lemma 1.4(c): dkappa/ds = rho M X/C = O(c_{L+1}^2 D^2),
dtheta/ds = rho M/Phi_P^2 >= u M/Phi_P^2), restore kappa^# exactly by a peak push of size O(c_{L+1}^2) (IVT; kappa continuous, part 1);
re-solve TU (block triangular Jacobian).  By Lemma R-kt, rho_l(new) = m r'_l k(new)/Phi_l and dk/dR^2 = k^2/(2(a - k R^2)) > 0 (a > kR since
a^2 > k^2 R^2): decreasing r_{d_0} lowers k, hence every active rho, at fixed active ratios — numerically (4): rho of the active carriers drops
by 1.2e-4 ... 2.1e-4 with |kappa - kappa_0| = 2e-41 and active ratios exact to 6e-42.  Capacity: the push can lower k by >= c u^2/D(l)^2, far
more than the needed Lip x eta.  Inactive near-threshold Omega carriers are pushed inward individually (their values are not variables of
Gamma^#(kappa, a)).  Cost <= C Design eta log(1/eta) = o(T_lo^2).  So under (KN_{w,a}) the conclusion of Theorem 2.3 holds (the classes must
then be fixed BEFORE the exactification, which is legitimate: read them off the decomposition data, 2.2).
Without (KN_{w,a}): OPEN.  Precisely: an active block whose inactive Omega carriers are all nearly neutral, an active near-threshold switching
carrier d, and the exact zero set Z of the tiny minors near r(f) contained in {rho_d >= 1} (equivalently, by Lemma R-kt, Z forces d onto or
above the threshold).  For d a peak at f^# the decomposition's excess e_d = |omega_+(d)| + |omega_-(d)| must be O(Kt/lambda_d), which is not
implied by anything proved.  (C*-3) is therefore NOT closed by U1; it is reduced to this "status coherence" condition.  Remark: when Z is a
finite set near r(f) the bad case requires rho_d(point of Z) = 1 up to O(c_{L+1}^2), a design coincidence that a generic choice of the
free design parameters (e.g. delta_l in an interval, as in (GM)) avoids — so the genuinely open case is a positive-dimensional Z on which
rho_d attains values >= 1 only (HEURISTIC remark, not used).

## 2.5 Lemma 2.4 (subset averaging).  Verdict: CORRECT (PROVED).
Re-derived against Z3 Theorem E / V3 Theorem 2.5: the set of scales enters only through (A) the bad set I_r (sum over dyadic t < rho|r|/c_flat
is <= 2 rho|r|/c_flat, whatever the subset), (B) the scale-decoupling condition rho|r| > c_flat min S_j, and (C) the averaged error
(1/n') sum_{S_j} rho|r| K t <= 2 rho|r| K T_j/n'.  Exactness, side conditions and the sign pattern of the shifts are preserved by averaging.
