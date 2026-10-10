# X2-ref part 1 — Lemma M1, Corollary M1', Proposition J, d-consistency identities, Lemma M2

Refereed against: martin_density_note.tex (lem:threshold, def:certificate, lem:base, lem:block, def:twopiece, def:engineered,
lem:approxfacts (E2)-(E5), lem:F1, thm:engineered Steps 0-5), U1 Lemma 2.1 (as re-derived by U1-ref), U3-ref F6.
Scripts: r9/X2_ref_work/rmodel.py (independent multi-block model, written from scratch), check_J.py, check_J2.py (+ .out).

## 1.1 Lemma M1 (masses off the support, diagonal base).  Verdict: CORRECT (PROVED).
Re-derived.  With A = a + sum_{s in J} c_s e_s^*, J ∩ F = {} and U^* e_s^* = mu_s k_s: U^*A = nu e + X, X = sum c_s mu_s k_s is orthogonal
to span{k_s : s in F} ∋ e, so nu_A^2 = nu^2 + ||X||^2; e_A = (nu e + X)/nu_A gives (i) with <U^*u, k_s> = mu_s u(s); <e_A, e> = nu/nu_A gives
||e_A - e||^2 = 2(nu_A - nu)/nu_A <= ||X||^2/(nu nu_A) <= ||X||^2/nu^2; (iii) from xhat_A - zhat = (z^A - z) + U(e_A - e).  Normalization
a' = A/q*(A) does not change e_A.  (iv) (masses on F): ||e_A - e|| <= 2||U^*(A - a)||/nu is the general estimate; the first-order cross
effect through nu is as stated.  Nothing to add.

## 1.2 Corollary M1'.  Verdict: CORRECT (PROVED).
Crude bound: triangle inequality.  Sharp bound: max_i^2 <= sum_i, and for b supported off F the vector U^*b is orthogonal to
span{k_s : s in F}, so sum_{s notin F} mu_s^2 b(s)^2 = ||P^perp U^*(b 1_{F^c})||^2 <= ||P^perp U^* b||^2 = nu h(b) (the two components of
P^perp U^* b along span{k_s : s in F} and its complement are orthogonal); h(b^theta) <= (h(b^+) + h(b^-))/2 <= Gamma_max/q_0.
Remark (used below): for the note's engineered approximant (def:engineered) the masses sit on contacts of the row (off its support), so
the SHARP bound applies: ||X|| <= 4 rho s_1 (nu sum_i h(b^theta_i))^{1/2} = O(s_1 sqrt(n)) uniformly in the piece scales.

## 1.3 Proposition J.  Verdict: CORRECT as an upper bound (PROVED), one precision (p-J); the attainment claim is correctly HEURISTIC.
(a) ||D Domega||^2 = Delta^2 + C H(Domega) is the definition of H; the shift bound Delta^2 <= C^3 H/(M^2 Phi_P^2) is U1 Lemma 2.1
(U1-ref re-derived it; I re-derived it once more: D Domega vanishes on P, so the component of D Domega orthogonal to Dw has squared norm
>= (Delta/C)^2 ||D(w 1_P)||^2 = Delta^2 M^2 Phi_P^2/C^2, i.e. C H >= Delta^2 M^2 Phi_P^2/C^2); H(Domega) <= 2H(omega^+) + 2H(omega^-) since sqrt H is
a seminorm.  Phi_P^2 >= Phi_{k^nat}^2 > 0 (f-constant, Lemma M2).
(b) kappa^+- = -+(rho/2)(d' - d)(Domega) (thm:engineered Step 2), and with (1.0) at both rows the split
(d' - d)(Domega) = sum_k Domega(k) lambda_k (u_k(xhat') - u_k(zhat))/A' + Delta (A - A')/A' is exact; Cauchy-Schwarz with lambda_k = m Phi_k.
Numerically (check_J2.py, independent multi-block model, |Omega| = 2, window masses on contacts): the inequality
|(d' - d)(Domega)| <= m ||D Domega||_2 |Omega|^{1/2} max_k |Delta u_k|/A' + |Delta| |A' - A|/A' holds in all instances (max ratio 1 - 6.8e-3;
with |Omega| = 1 it is attained, ratio 1.0000 in check_J.py, as it must be when Cauchy-Schwarz is an equality and both terms have
the same sign).
(p-J) In "consequently |kappa| <= C_f |Omega|^{1/2}(||X|| + t(N''))" the cut-off term is max_{k in Omega} t_k (t_k = ||u_k 1_{(N'',inf)}||_1),
which is <= t(N'')/min_{Omega} lambda_k, not <= t(N''); harmless (N'' is chosen last; replace t(N'') by max_Omega t_k).
Uniformity in t.  The constant is uniform in the piece scale; ||X|| itself is uniform in t by the SHARP bound of Corollary M1' (masses off
the support), ||X|| <= 4 rho s_1 (nu n Gamma_max/q_0)^{1/2}.  So for valid data the per-piece mismatch is O(s_1 |Omega|^{1/2} n^{1/2}), not
O(s_1/t^2).
Precision of U3-ref F6a (CONFIRMED).  U3-ref's "kappa ~ s_1/t^2, generically with equality up to constants" used the crude bounds
||e' - e|| <= K_e s_1 with K_e ~ ||b^theta||_1 ~ 1/t and |(d'-d)(omega)| <= C ||lambda omega||_1 (...) with ||lambda Domega||_1 ~ 1/t; its numerical check
scaled a fixed datum by 1/t, so Gamma_w ~ t^{-2}.  Such data are excluded by the hypothesis rho^2 kappa_w < 1 of thm:engineered.  For valid
data both crude bounds are replaced by the Hilbert-coefficient bound on ||X|| (diagonal base) and by ||D Domega||_2 = O(1) (U1 Lemma 2.1).
U3-ref's QUALITATIVE conclusion survives in the form stated by X2: K_sharp would have to grow like (n |Omega|)^{1/2} along windows, which the
fixed-inefficiency rebalancing of thm:engineered Step 4 cannot absorb (eta_1 would become window-dependent and the transfer constant
Lambda(eta_1) is an uncontrolled f-dependent rate).  Exact cancellation (d-consistency) is the right remedy.  (Attainment of the lower
bound is HEURISTIC, as labelled; nothing depends on it.)

## 1.4 Definition 1.4 and the identities (1.1).  Verdict: CORRECT (PROVED).
At a strict non-peak k of both rows, Phi_k^2 w(k)/C = nv_k (lem:threshold), so nv'_k = nv_k gives w'(k) = (C'/C) w(k); gap' = (1 - C') -
(C'/C)(1 - C - gap) = (C'/C) gap + 1 - C'/C; d'(omega) = d(omega) for omega supported in Omega (formula (1.0) at both rows); H' = (C/C')H.
Numerically (check_J.py (c), check_J2.py): exact to 1e-16 after an exact nv-restoration.
REFEREE ADDITION (PROVED; strengthens X2, not needed by it).  If the switching set is ALL of Q_m (U1's convention: Omega_m = all coarse strict
non-peaks, Q_m \ Omega_m = fine carriers) then d-consistency freezes C_m up to the fine carriers.  Proof: by the clamp formula (proof of
lem:F1) C is the root in (0,1) of F(c; v) := sum_k min(Phi_k (1 - c)/c, v_k)^2 = 1 with v_k := m|u_k(zhat)|/A = |nv_k|/Phi_k.  Peaks with
v_k > Phi_k (1 - c)/c near c = C contribute Phi_k^2((1 - c)/c)^2, independent of their values; strict non-peaks in Omega contribute
v_k^2 = (nv_k/Phi_k)^2, fixed by d-consistency.  Hence, if the peak set is unchanged, F(.; v') - F(.; v) involves only the
carriers of Q \ Omega, and the monotonicity argument of lem:F1 gives
      |C' - C| <= (2(1 - C)/(C c_*)) sum_{k in Q \ Omega} Phi_k |v'_k - v_k|.
With Q \ Omega = fine carriers this is <= K c_fine Pi.  Numerically: Omega = Q gives |C' - C| <= 1.1e-16 (25 instances); removing one carrier
from Omega gives |C' - C| ~ 5e-11 (check_J2.py).  Consequence: at a d-consistent approximant the GAPS of the Omega carriers are preserved up
to K c_fine Pi (by (1.1)), so the condition |C' - C| <= C gap_min/4 used for "gap' >= gap/2" is automatic once K (c_fine Pi + W_pull) <= C gap_min/4
(the theta-regime radius condition s_1 <= T gap_min/(2 rho A_2) of (LATE) is still needed, for a different reason).  Also every relative position rho_k = |nv_k| C/(Phi_k^2 M) (k in Omega) is preserved up to the
same error: d-consistency preserves the STATUSES of all switching carriers (compare U1-ref Lemma R-kt).

## 1.5 Lemma M2.  Verdict: CORRECT (PROVED), one precision.
The contradiction argument via prop:continuity and lem:persistence is right (lem:persistence is stated for sequences f_n -> f in p*; its
proof gives every listed property eventually, hence on a ball).  Precision: Lemma M2(a) "every peak of f stays a peak" is claimed only for
k^nat_m; the later uses ("every peak of f_0 with margin > K_w Pi stays a peak", Lemma DC(5) "the peaks of f_0 of every block remain peaks")
must be read for peaks with margin above the perturbation — infinitely many fine peaks of f_0 have arbitrarily small margins and can change
status; this is harmless (they enter only through c_fine, the Bregman bound and the scrambled set) but Lemma DC's statement should say
"every peak of f_0 with margin > C_lev r + delta_1 (in particular every coarse peak) remains a peak".
