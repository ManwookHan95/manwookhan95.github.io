# P1 referee — part 2 (cross-checks against Round-1 sources; the main corrections)

## A. Lemma 1.2 / Cor 1.3 (linear obstruction): CORRECT, and robust
Checked each class against its source:
 (a) A Def 4.1/4.15: shifted certificates do not change the direction g_c = b + sum R_m*(omega_m - d_m w_m); in S(f).
 (b) A Thm 6.2: truncations c_J are finite certificates; in cl S(f).
 (c) A Lemma 6.3 (Theorem L) and D Lemma 11.5(a),(b) (locally split mates): supp b in F, b(zhat)=0, Omega_m = omega_m - d w_m with
     omega_m bounded and vanishing on P_m; sum_k lambda_k |omega(k)| < inf, so truncations converge in l_1; in cl S(f).
 (d) A Thm 6.8 and P1 Thm 4.3: conclusions are in cl Cert(f).
 (e) C Thm 7.1 AND C Thm 7.4 (transfer-peak rebalancing, not listed by P1): both recover BALANCED FINITE CERTIFICATES (Def 7.0 in C),
     i.e. elements of S(f). So the obstruction also covers C's strongest class. E Thm 5.1 (averaging criterion): in cl Cert(f).
Hence Cor 1.3 holds for every intrinsic class produced in Rounds 1-2. PROVED.

## B. Thm 3.7 / Cor 3.8 / (O1): the "second-order defect" is mis-specified — C Thm 7.4 and C Prop 8.1 were overlooked
P1 defines the second piece of Def(f) at block-tame f as {g_c in C(f): Hhat(c) > 1}, Hhat = min over A's shifts theta R_m* w_m.
C_notes (Round 1) contains (re-read by me, proofs plausible; UNREFEREED):
 * C Thm 7.4: every balanced finite certificate g with (f,g) contractive and Gamma_w(g) := q_0 H_b + sum_m sigma_m H_m <= 1 is
   recovered (along the canonical truncations; the decomposition also works at f itself, C Cor 7.2(c)). The device is a robust deep
   TRANSFER PEAK k_* (u_{k_*} ~ correction making pi^ = R*(sign w 1_{Lset}) a multiple of a), lowered by an O(t^2) amount: a second-order
   shift that is NOT of A's form theta w_m (+ finitely supported off-peak eta_m).
 * C Prop 8.1: Gamma_2^+(g) <= Gamma_w(g) always (a in c_00); and Gamma_2^-(g) >= Gamma_w(g) if every Q_m is finite, Dg_m is empty and (MS)
   holds. So at such f every balanced finite certificate in C(f) has Gamma_w <= 1.
 * Elementary comparison (mine): optimizing A's theta gives Hhat >= Gamma_w (equalizing the levels H_m + 2 theta_m = L forces
   L >= q_0 h(b) + sum sigma_m H_m + 2 q_0 kappa_q(v_theta)); for a pure block direction Hhat = H r_2/(1+r_2) >= (1-q_0) H = Gamma_w,
   with equality iff kappa_q(-R*w) = 0. So {Hhat > 1} strictly contains {Gamma_w > 1} in general.
Consequences:
 (i) Thm 3.7's identity Def(f) = (C(f)\S(f)) u {Hhat > 1} is correct only RELATIVE TO P1's list of classes (which omits C Thm 7.4).
     Relative to all Round-1 results the second piece is {g_c in C(f): Gamma_w(g_c) > 1} (closed in finite-dimensional S(f)).
 (ii) Combining P1 Cor 3.8 with C Prop 8.1 and C Thm 7.4: if f is C-tame (a in c_00, K finite, Qbar_m finite, (MS)) AND has no
     degenerate peaks, then the second piece is EMPTY and f is in the recoverable set R (every mate recovered). [PROVED modulo the
     unrefereed C Thm 6.4, Prop 6.5, Prop 8.1, Thm 7.4; P1's 3.8(a) is exactly what removes C Thm 8.4's hypothesis K = empty.]
     This is a positive theorem that P1 could have stated; instead P1 leaves (O1) open in a form that is largely already answered.
 (iii) Remark after 3.7 ("finite-model computations ... suggesting that it [the second piece] can be nonempty"): not supported. The
     A_referee finite models have no transfer peaks (C Prop 8.2 / Discussion 8.3 explain that finite models have exactly flat
     rebalancing faces with coefficient between Gamma_w and Gamma_max; in Martin's space every tail of (u_{k,m})_k is dense, which supplies
     transfer peaks). Status of that suggestion: HEURISTIC, and pointing the wrong way.
 (iv) (O1)(a) "general shifts" is essentially C's transfer-peak shift; (O1) should be restated as: is there f with Dg nonempty (or Q_m
     infinite) and a balanced certificate g in C(f) with Gamma_w(g) > 1? (OPEN.)

## C. 3.2-3.6: correct core, imprecise bookkeeping
 * 3.4 (transfer identity), 3.5(a)-(c), the peak identity 3.5(b): PROVED (re-derived).
 * 3.5(d) "sign Omega+(k) = -sign w(k) for beyond-window coordinates": needs the level shift ell_m - M_m to be small compared with
   gap(k)(1/(2c_0) - 1). In general ell_m - M_m = O(|t|) (not O(eps)): from t<Omega_m,zeta_m> = sum_P |zeta_k|(ell - M - delta_k) +
   sum_{Q} t Omega(k) zeta(k), the off-peak term is O(t) in general. So for coordinates with gap(k) <~ |t| the "short direction" can also be
   beyond the window. The claim is right for gap(k) >> |t|; for gap(k) <~ |t| the bookkeeping must be done relative to the common level.
   Status: SKETCH (not PROVED).
 * 3.6 inequality [one-sided(+) + one-sided(-)] <= M_{c_0}(D, Omega_D) + K t: the quantities are not defined precisely enough to verify
   ("common", "beyond-window mass", nested thresholds). Conclusions (1),(2) are formal consequences once definitions are fixed. SKETCH.
 * 3.3: "near-contacts are scale-free one-sided resources" is inaccurate: a near-contact with room r_j = 1 - |z_j| > 0 costs r_j |tau B_j|
   at first order, so it can carry O(1) at scale tau only when r_j <~ |tau|. Only exact contacts, near-flips used with the cheap sign,
   degenerate and near-degenerate peaks are scale-free. Also the claim "coordinates with gaps bounded below are one-sided only at depth
   Phi <~ |t|" needs (K2) (Hilbert cost), not (K3) as the proof line says. Minor; the displayed inequalities are PROVED.
