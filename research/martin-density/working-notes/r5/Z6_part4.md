# Z6 part 4: Theorem C (compensated resonant swallowing; infinitely many non-d-neutral swallowed carriers)

Setting: SLD operator, N >= 1, I = {1..N}, f in S_{p*} with F finite.  B = set of swallowed (bad) carriers (r_l = 0),
eps_l, u~_l = eps_l u_l 1_{F^c}, r*_l, Lambda*_f(l) as in Definition swallowed.  For bad l with k(l) a non-degenerate
peak let mu_l := mu_{k(l),m(l)} > 0 (margin) and put K_P(l) := sum_{l' <= l, l' in B, k(l') in P} 1/mu_{l'}.

Definition (class R_C).  f in R_C if F is finite and
 (H1)  supp y_{l'} cap S_l = empty whenever l < l' are both bad;
 (R)   every bad carrier is either (R-np) a strict non-peak which is RESONANT (u~_l z-signed and supported in K) with
       gap_{m(l)}(k(l)) >= gamma_B for a fixed gamma_B > 0, or (R-pk) a NON-degenerate peak;
 (Cmp) every block m containing a bad strict non-peak l with q_l != 0 contains bad strict non-peaks l^+_m, l^-_m
       (compensators) with q_{l^+_m} > 0 > q_{l^-_m}   (q_l = eps_l u_l(xi)/sigma_m by 3.1);
 (H2') as in 3.2 (a good non-degenerate peak, or a pair of bad non-degenerate peaks of opposite types);
 (W*_P) r*_l > 0 for good l, and liminf_l (Lambda*_f(l) + K_P(l)) / (l 2^{l^3} Lambda°(l)) = 0.
No condition on the contact set, on the good blocks' fine structure, or on the number of bad carriers.
R_C contains R_S's resonant case (B_res): there all bad carriers are d-neutral non-peaks (q = 0, gap = M_m), (Cmp) is
vacuous, K_P = 0, and (H2') holds by 3.2's remark.

THEOREM C.  R_C is contained in Rec (every mate is recovered).                                   [PROVED]

Proof.  We follow the proof of Theorem S verbatim, with K_* replaced by K_** := (1/q_0 + 22) Lambda*_f(l_*) + K_P(l_*),
and only Lemmas badpeaks and exactswitch modified.  Fix the window l_*, t in W(l_*), t <= min(t_eta,1), and a two-sided
decomposition at scale t.  By Lemma modswallow (needs only (H1) and r*_l > 0 for good l):
  (i) sum_{good} |Delta theta_l| <= K_* t (+6t^2 fine);  (ii) sum_{l in B, l <= l_*} (tau_l)_- <= K_* t.
Step 1 (shift).  By (H2') and 3.2 (or Lemma badpeaks(a)), |Delta d_m| M_m <= K_d t with K_d <= C_f K_*, C_f depending
only on f (the two fixed peaks: their lambda, alpha).
Step 2 (bad peaks).  For bad l with k(l) a non-degenerate peak, eq. (peakshift) gives varsigma eps tau_l/lambda_l in
[Delta d M, Delta d M + t/(sigma|alpha(k)|)], and sigma|alpha(k)| = lambda_l mu_l (eq. margin), so
|tau_l| <= t/mu_l + lambda_l K_d t.  Hence sum_{bad peaks <= l_*} |tau_l| <= (K_P(l_*) + K_d) t.
Step 3 (d-sums).  eq. (didentity) in block m: the good carriers contribute at most K_* t/(m C_m) (Phi|w| <= 1); the fine
carriers l > l_* at most (6/(m C_m t)) sum_{l>l_*} Phi_l lambda_l <= (6/(mC_m)) T_lo(l_*)^6/t <= (6/(mC_m)) t^5 (box bound
and (P2)); the coarse bad carriers contribute -sum q_l tau_l.  So |sum_{l in B, l<=l_*, m(l)=m} q_l tau_l| <= C'_f K_** t.
Step 4 (exact switching, replaces Lemma exactswitch).  Put tau^1_l := (tau_l)_+ for bad strict non-peaks, tau^1_l := 0 for
bad peaks (l <= l_*), e_m := sum_{m(l)=m} q_l tau^1_l, and
  tau'_l := tau^1_l + (e_m)_-/q_{l^+_m} [l = l^+_m] + (e_m)_+/|q_{l^-_m}| [l = l^-_m]
(l_* >= all compensator indices; blocks without non-neutral bad non-peaks have e_m = 0).  Then tau' >= 0, tau' = 0 at bad
peaks, sum_{m(l)=m} q_l tau'_l = 0 for every m (exact d-neutrality), and V' := sum_{l<=l_*} eps_l tau'_l u_l 1_{F^c} is
z-signed and supported in K (each term is, by (R-np)).  Moreover |e_m| <= |sum q_l tau_l| + sum |q_l|(tau_l)_- +
sum_{peaks} |q_l||tau_l| <= C''_f K_** t (|q_l| <= M/(mC) for all l), hence
  sum_{l in B, l <= l_*} |tau_l - tau'_l| <= C_f K_** t   and   ||Delta B 1_{F^c} - V'||_1 <= C_f K_** t,
with C_f depending only on f (through q_{l^pm_m}, sigma, C, M, the peaks of Step 1).  This is Lemma exactswitch (a)-(c)
with K_* replaced by K_**; the compensators are the only carriers whose amplitude is increased, by at most C_f K_** t.
Step 5 (window two-piece data).  Lemma windowtwopiece holds with the same proof and K_** in place of K_*:
(a) representation and Delta d_m = sum q_l tau'_l = 0 (computation in its proof: (eps tau'/lambda) Phi^2 w/C = q tau');
(b) at bad coarse peaks omega^+ = 0 and lambda_k rho_k <= |tau_l| + lambda_k |Delta d| M, summed by Step 2; at bad
non-peaks rho_k = 0; good coordinates as before; base error via the split lemma with e := Delta B 1_{F^c} - V';
(c) unchanged; (d) the bad strict non-peaks have gap >= gamma_B by (R-np), and tau'_l/lambda_l <= 6/t for
non-compensators (tau'_l <= |tau_l| <= 6 lambda_l/t, box), tau'_l/lambda_l <= (6 + 1/lambda_C)/t for the compensators
(lambda_C := min of their lambda, using C_f K_** t^2 <= 1); so A_2 := 10 + 1/lambda_C works.
Step 6.  The proof of Theorem S (windowed averaging over W(l_j) with (W*_P), Lemma onesidedtransfer, Lemma avgfunctionals,
d-neutral averaged data, Corollary D1) applies verbatim.  QED

Remarks.  (1) Exactness of d-neutrality is achieved by moving the defect onto two FIXED carriers; the Hoffman constant of
the infinite cone is never needed (the cone {tau >= 0, sum q tau = 0} is "upward closed" in the compensator directions,
and resonance makes z-signedness automatic for nonnegative combinations).  (2) Without (Cmp), Proposition 3.4 shows the
switching through same-sign q carriers is O(t)/q_l per carrier (transient), but the exact cone is {0} on them and the
projection error is not O(K t) with window-compatible K: this is the residual obstruction (see part 5).  (3) (H1) is
essential here: at maximal contact (z = 1 off F) (H1) fails because targets meet earlier signature sets (density of
targets forces this), and the bad inequalities couple through later bad targets (slaving).

## 4.2 Relaxation: no gap condition for q_l >= 0, degenerate peaks of the non-swallowing type   [PROVED]
Replace (R) by
 (R') every bad carrier l is one of: (np+) a resonant strict non-peak with q_l >= 0 (ANY gap > 0);
      (np-) a resonant strict non-peak with q_l < 0 and gap >= gamma_B; (pk) a non-degenerate peak (resonance not needed);
      (dg-) a degenerate peak with varsigma_{k(l)} eps_l = -1 (resonance not needed).
THEOREM C holds with (R') (and the compensators of (Cmp) of type (np-)).
Proof of the changes.  (dg-): eq. (peakshift) gives varsigma eps tau_l/lambda_l >= Delta d M, i.e. tau_l <= lambda_l |Delta d| M
<= lambda_l K_d t, and (tau_l)_- <= K_* t by Lemma modswallow(b); so |tau_l| = O(K_** t) and it is dropped like (pk).
(np+): put a := 1.5 gap(k)/t, P := varsigma_k omega^+(k), Q := varsigma_k omega^-(k) for the data of Lemma windowtwopiece at
k = k(l).  By Lemma suplevel(f) and |d_pm t| <= 1/2, P = varsigma omega_{+}(k) <= a, and since omega^- = omega_- + eps_l(tau_l - tau'_l)/
lambda_l + Delta d w(k) (identity omega_- - omega_+ = eps tau/lambda - Delta d w at k), Q >= -a - e_k with
e_k := |tau_l - tau'_l|/lambda_l + |Delta d| M.  Moreover Q - P = varsigma eps tau'_l/lambda_l >= 0 (q_l >= 0 means
varsigma_k eps_l = +1 or w(k) = 0; for w(k) = 0 the gap is M and nothing is needed).  Shift both omega^pm(k) by
x := varsigma (-a - Q)_+ : then P + x <= a (as Q >= P), Q + x >= -a, the difference omega^- - omega^+ is unchanged (so
Delta d stays 0 and V' is unchanged), and both data now represent g_t - x y_{k,m}/lambda_k... precisely g_t changes by
-x (lambda_k u_k - (Phi_k^2 w(k)/C) R^* w) whose l_1-norm is <= C (lambda_k |x|) <= C(|tau_l - tau'_l| + lambda_k |Delta d| M),
summable to O(K_** t) over l (Steps 2-4); the comparison with the actual decompositions in parts (b),(c) of Lemma
windowtwopiece acquires the same O(K_** t).  After the shift, on the + side (r > 0) the coordinate k has outward
part <= a and arbitrary inward part, on the - side (r < 0) likewise.  The one-sided transfer expansion (Lemma
onesidedtransfer) then holds at k with NO lower bound on the gap: for |r| <= c_flat t,
 |(1 - d r) w(k) + r omega(k)| <= (1 - d r)(M - gap) + |r| a <= (1 - d r) M  (c_flat <= 1/3, |dr| <= 1/2),
the inward part only decreasing varsigma W(k) and not overshooting (|r omega(k)| <= c_flat A_2 <= M/2), so ||W||_inf =
(1 - d r) M and the Hilbert part is as in Lemma block; the rest of that proof is unchanged.  At the engineering step
(Corollary D1 for the averaged data) the data are FIXED and supported on finitely many strict non-peaks of f, all with
positive gaps, so their coordinatewise radius is positive and Theorem engineered applies verbatim.  QED
Consequence.  Near-threshold swallowed strict non-peaks (gaps -> 0) are harmless when their d-coefficient has the
"inward" sign q_l >= 0; gaps matter only for q_l < 0 (one side must then move outward).
