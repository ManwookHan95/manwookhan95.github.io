# Z6 referee, part 1: structural facts 2.1-2.4, Lemma F / 4.2, Theorem C

Conventions checked against the note: Delta d_m := d_{+,m} - d_{-,m} (Lemma suplevel/peakshift); for two-piece data
(Def. twopiece) Delta d_m := d_m(omega^-) - d_m(omega^+) (opposite convention; Z6 uses each consistently).
omega_+ - omega_- = Delta Theta + Delta d w (from omega_pm = Theta_pm + d_pm w).

## 2.1 d-coefficient. CORRECT (PROVED).
Off P: w(k) = C zeta(k)/(Phi(k)^2 sigma), zeta(k) = lambda_k u_k(xi) = m Phi(k) u_k(xi), so Phi w/(mC) = u_k(xi)/sigma.
|w| = M - gap. Nothing else used.

## 2.2 shift pinning by a pair. CORRECT (PROVED).
(peakshift): |omega_+|+|omega_-| = -vs DeltaTheta(k) - Delta d M, DeltaTheta(k) = Delta theta_l/lambda_l = -eps tau/lambda.
So Delta d M = vs eps tau/lambda - Y, 0 <= Y <= t/(sigma|alpha(k)|) = t/(lambda_k mu_k) (eq. margin).
Only k_2 (vs eps = +1) needs alpha != 0; non-degeneracy of k_1 is not used (statement may drop it).
NOTE: the constant t/(sigma|alpha(k_2)|) is the margin of a SWALLOWING-TYPE peak; harmless because the pair is fixed
(f-constant), but (H2') is not margin-free.

## 2.3 doubly swallowed blocks. CORRECT (PROVED).
Re-derived: v = b^+ - b^- is z-signed on K, v = sum_m' R*_{m'}((omega^- - omega^+) - Delta d_{m'} w_{m'}); on S_l\F beyond the
finite target supports of the carriers of omega^pm (finitely supported, in Q_m, so l itself is not among them):
v(s) = -Delta d_m lambda_l w_m(k) v_l(s) + rho(s), |rho(s)| <= (4/3) D sum_{l''>l, s in supp y_l''} lambda_l'' <= (2/9) D 2^{-2s} c_l delta_l
(allowedness (b): 2 c_{L(s)} <= 2^{-2s} c_l delta_l; sum_{l''>=L} lambda <= c_L/3). Main term ~ 2^{-s}: ratio -> 0. Sign
argument gives eps_l vs_k = -sgn(Delta d_m) = eps_l' vs_k'. Contradiction. Holds for any functional (no mate condition).
At maximal contact every block has swallowed peaks of both signs (density + threshold lemma), so every exact two-piece
datum is d-neutral: same as Z4 Prop 5.1 / Z4-referee finding 9 (not new, but an independent, shorter proof).

## 2.4 same-sign transience. CORRECT (PROVED).
For l in Sigma: Phi w Delta theta_l/(mC) = -q_l tau_l (tau = -eps Delta theta). (didentity) gives sum_Sigma q tau = R,
|R| <= A - sum_Sigma |q|(tau)_-. One sign => sum |q|(tau)_+ <= |R| + sum|q|(tau)_- <= A. Elementary identity; the content is in
bounding A by O(t): needs Delta d pinned (2.2 / (H2')), other carriers pinned in the Phi|w|-weighted sense
(good: K* t; fine: (6/(mC)) t^5 via box + (P2) -- re-derived: sum_{l>l*} Phi_l 6 lambda_l/t <= 6 T_lo^6/t <= 6 t^5),
and (tau)_- from signatures. Matches Z4-referee Lemma R (lower bound >= 1/q_l') as an upper bound: CORRECT reading.
Reading "n^w_{l*} << 1/c_{l*-1}" is design-dependent (Lambda°(l) can exceed 1/c_l if the S_l start far out); harmless (a reading).

## Lemma F and 4.2. CORRECT (PROVED), one sign typo.
On A: B_pm(s) = g(s) - theta^pm_l v_l(s); phi_{eps}(x) = 2(eps x)_-, phi_{-eps}(x) = 2(eps x)_+; switching budget
(each side <= t/(2q0)) gives sum_A v (eps theta^+ - rho)_+ <= t/(4q0), sum_A v (rho - eps theta^-)_+ <= t/(4q0).
4.2(a): box bound needs only t <= 1 (suplevel(e): |t Theta| <= s(1)+1 <= 3); optimize t = (12 q0 lambda v)^{1/2} <= 1. OK.
4.2(b): conclusion should read g|_A = eps_l theta*_l v_l|_A (Z6 drops eps_l; with theta* := lim eps theta^pm = rho).
4.2(c): theta^pm = lambda omega_pm - lambda d_pm vs M, lambda|omega_pm| <= t/(2 mu): OK; g|_A = -d* lambda vs M v_l = trace of
-d* R*_m w_m on A. OK.  4.2(d) OK.
Caveat (not an error): A may be empty (later targets may cover S_l); then the lemma is vacuous.

## Theorem C. CORRECT (PROVED), modulo the standard re-proof of the one-sided expansion with "inward-only" coordinates.
Re-derived Steps 1-6. Key checks:
 - Step 4: sum q tau' = e_m + (e_m)_- - (e_m)_+ = 0; tau' >= 0; resonance makes each term tau'_l u~_l z-signed in K.
 - |e_m| = |sum_np q tau + sum_np q (tau)_-| with sum_all = O(K** t) (didentity), peaks O((K_P + K_d) t), (tau)_- O(K* t): OK.
 - Shift trick (np+): P := vs omega^+(k) <= 1.5 gap/t =: a (suplevel(f), |d t| <= 1/2); Q := vs omega^-(k) >= -a - e_k
   (from omega^- = omega_- + eps(tau'-tau)/lambda + Delta d w and suplevel(f) for omega_-); Q - P = vs eps tau'/lambda in [0, A_2/t].
   Shift by vs x = (-a-Q)_+: if x > 0 then P <= Q gives P + vs x <= -a. Then for 0 < r <= c_flat t:
   vs W(k) = (1 - r d)(M - gap) + r P~ <= (1 - r d) M - gap (1 - |r d| - 1.5 c_flat) <= (1-rd)M, and
   vs W(k) >= (1 - r d)(M - gap) - r (a + A_2/t) >= -(1 - r d) M for c_flat <= 1/(4(1.5 + A_2)); same on the - side.
   With ||W||_inf = (1 - r d) M attained at the peaks (omega = 0 on P), the block excess is EXACTLY
   N(W) - <W, zeta>/sigma = ||D W|| - C = C (sqrt(1 + r^2 ||P^perp D omega||^2/C^2) - 1) <= r^2 H(omega)/2:
   no coordinatewise radius is needed (re-derived; matches Z3 Lemma 5.1). Rebalancing needs only ||W - w||_inf <= 2 A_3 c_flat.
   Cost of the shift: lambda_k |x| <= |tau - tau'| + lambda |Delta d| M, summable. OK.
 - Averaged data are fixed, finitely supported on strict non-peaks: Theorem engineered's gamma_0 > 0. OK.
 Formal gap (fixable, routine): Lemma onesidedtransfer must be restated with a third kind of coordinate
 ("inward-only": vs omega^+ <= 1.5 gap/t, vs omega^- >= -1.5 gap/t, |omega| <= A_3/t); its proof goes through verbatim
 because the only use of the coordinate conditions is ||W||_inf = (1 - r d) M.
