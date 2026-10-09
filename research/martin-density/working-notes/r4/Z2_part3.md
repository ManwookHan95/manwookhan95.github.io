# Z2 part 3: Theorem S — exactly swallowed signatures are harmless when the switching they allow is "finitely generated":
# windowed averaging INTO TWO-PIECE DATA, recovered by S3 Corollary D1 (no approximants of f, no Lemma Z)

Setting: SLD operator T (G3 1.2), p = p_N, notation of part 2. Imports: G3 parts 2, 4, 5 (refereed; with the referee's kappa_0 fix in 5.3),
A Lemma 7.2, A Lemma 4.3 (and the elementary bound below), P2A 1.6 (two-piece data), S3 Corollary D1 (refereed PROVED: F finite, g in C(f) carrying
two-piece data with Delta d_m >= 0 in every block and kappa_w <= 1  =>  g in Ls(f); any admissible T, any contact set K, no condition on Q_m).

## 3.1 Statement
Let f in S_{p*} with F = supp a finite and B := B(f) (exactly swallowed signature sets, 2.4). Hypotheses:
 (H4) every block m <= N has a non-degenerate peak (alpha_{m,k} != 0) whose ladder index is not in B;
 (H5) no l in B sits at a DEGENERATE peak k_l with sign w(k_l) = sigma_l;
 (W*) room off the bad targets for every l notin B, and the window condition (2.4);
 and ONE of:
 (S_fin) B is finite;
 (S_inf) (H3), and EVERY l in B is resonant (2.4), d-neutral (w_{m(l)}(k_l) = 0, equivalently u_l(xi) = 0), hence a strict non-peak.
 (A mixture — finitely many exceptional bad carriers plus infinitely many resonant d-neutral ones — works verbatim if the off-F supports of the
 resonant ones are disjoint from the off-F supports of the exceptional ones; otherwise resonant vectors can cancel wrong signs of exceptional ones
 and the finite polyhedral analysis of 3.2 does not apply as stated.)
**Theorem S (PROVED).** Under these hypotheses f is in R: every mate of f is recovered.
(The class contains first rows whose contact sets swallow signature sets EXACTLY — the P1 phenomenon — including first rows with cofinite contact
set, with arbitrary block structure: infinitely many strict non-peaks, near-threshold carriers, degenerate peaks (other than (H5)), several blocks.
It is disjoint from R_0^± as soon as B is non-empty.)

## 3.2 The free cone and the projection (S_fin)
Write the switching coordinates as tau_l := -sigma_l Delta c_l (l in B cap Cset). For S_fin let B_0 := B (finite; take l_* >= max B), and consider the cost
   c(tau) := sum_{j notin F} phi_{z_j}( sum_{l in B} sigma_l tau_l u_l(j) ),   tau in R^B.
(i) c is POLYHEDRAL: for j in S_l \ F (l in B) the only bad vectors that can be non-zero at j are u_l (signature, value v_l(j) > 0) and targets y_{l'} of bad
l' > l (allowedness (a) excludes l' < l, privacy excludes other signatures); the union T_0 of the supports of the bad targets is FINITE. Hence
c(tau) = sum_{l in B} 2 (tau_l)_- ||v_l 1_{S_l \ (F cup T_0)}||_1 + sum_{j in T_0 \ F} phi_{z_j}(linear form in tau), a finite sum of convex piecewise-linear
functions. Its zero set Z_0 is a polyhedral cone contained in R^B_+ (each S_l \ (F cup T_0) is infinite, so the first sum forces tau >= 0).
(ii) Constraints. Let Bpk := {l in B : k_l is a peak} and, for l in B \ Bpk, a_l := sigma_l Phi_{m(l)}(k_l) w_{m(l)}(k_l)/(m(l) C_{m(l)}).
The "admissible switching cone" is the polyhedral cone
   Z := { tau in Z_0 : tau_l = 0 (l in Bpk),  sum_{l in B, m(l) = m} a_l tau_l = 0 (every block m) }.
By Hoffman's error bound for finite systems of linear inequalities there is H < infinity (depending only on f) with
   dist_1(tau, Z) <= H ( c(tau) + sum_{l in Bpk} |tau_l| + sum_m |sum_{m(l)=m} a_l tau_l| )     for all tau in R^B.        (3.2.1)
(c(tau) is a sum of positive parts of finitely many linear forms plus multiples of (tau_l)_-, so (3.2.1) is the standard Hoffman bound.)
(iii) At window scales: by part 1 (1.2.1) and (F2), with Delta B 1_{F^c} = sum_{l in B} sigma_l tau_l u_l 1_{F^c} + e_0, ||e_0|| <= K* t + 6t^2 (Lemma 2.5(a) and the
box bound for fine carriers; here every l in B is coarse), we get c(tau) <= t/q_0 + 2||e_0||; Lemma 2.6(c) and (H5) give |tau_l| <= K t for l in Bpk;
Lemma 2.6(b) gives |sum a_l tau_l| <= K t. Hence there is tau' in Z with ||tau - tau'||_1 <= K_H t (K_H := C H K*).
For S_inf: put tau'_l := (tau_l)_+ for l in B cap Cset (by Lemma 2.5(b), which uses (H3), sum |tau_l - tau'_l| <= K* t); no projection is needed since
every bad carrier is resonant (so any tau' >= 0 has zero cost) and d-neutral (a_l = 0), and Bpk is empty.
In both cases V' := sum_{l in B cap Cset} sigma_l tau'_l u_l 1_{F^c} is z-signed, supported in K (for tau' in Z: c(tau') = 0), and
   Delta B 1_{F^c} = V' + e',   ||e'||_1 <= K' t,    sum_{m(l) = m} a_l tau'_l = 0 for every m.                       (3.2.2)

## 3.3 Window two-piece data
Fix a window scale t (t in W(l_*), l_* large in the subsequence of (W*), t <= min(t_eta, t_1, 1)). Apply Lemma 2.3 to (3.2.2):
B_+ 1_{F^c} = theta V' + r_+, B_- 1_{F^c} = -(1 - theta) V' + r_-, ||r_+-|| <= K' t + t/q_0. Let Bns := (B cap Cset) \ Bpk (bad strict non-peaks).
 + side:  omega^+_m := omega^c_{+,m} (G3 4.1: clamp of omega_{+,m} on GOOD coarse non-peaks with gap >= t^2) + sum_{l in Bns, m(l) = m} omega_{+,m}(k_l) e_{k_l};
          bhat := B_+ 1_F + theta V',  kappa := bhat(zhat),  b^+ := bhat - kappa a.
 - side:  omega^-_m := omega^+_m + sum_{l in Bns, m(l)=m} (sigma_l tau'_l/lambda_l) e_{k_l},   b^- := b^+ - sum_{l in Bns} sigma_l tau'_l u_l.
 vector:  g_t := b^+ + sum_m R_m*(omega^+_m - d(omega^+_m) w_m).
**Lemma 3.3 (PROVED).** For l_* large and t as above:
 (a) (two-piece, d-neutral) b^+- are supported in F cup K with z_j b^+_j >= 0 >= z_j b^-_j on K; omega^+-_m are finitely supported in Q_m; d(omega^-_m) = d(omega^+_m);
     and g_t = b^- + sum_m R_m*(omega^-_m - d(omega^-_m) w_m). [Data in the sense of P2A 1.6 with Delta d_m = 0.]
 (b) ||g - g_t||_1 <= K_2' t.
 (c) Gamma_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta)) + K_4' t)^2.
 (d) t ||b^+-||_1 <= A_0' (scale-invariant size bound); |omega^+-_m(k)| <= 2 gap_m(k)/t on good coordinates (gap >= t^2); |omega^+-_m(k_l)| <= A_2/t at bad
     non-peak coordinates, whose gaps are >= gamma_B := min(min_m M_m, min_{l in B \ Bpk, S_fin} gap(k_l)) > 0 (in case S_inf all bad gaps equal M_m).
Constants K', K_2', K_4' are C(f) Lambda*_f(l_*) (times the fixed Hoffman/B_0 constants); A_0, A_2, gamma_B depend on f only.
*Proof.* (a) z-signs: theta V' is z-signed (theta in [0,1]); b^- 1_{F^c} = theta V' - V' = -(1 - theta) V' (as sum sigma_l tau'_l u_l 1_{F^c} = V'), and -kappa a lives on F.
Support: V' is supported in K (resonance/zero cost). d-neutrality: d(e_{k_l}) = Phi^2 w(k_l)/C, so d(omega^-) - d(omega^+) = sum (sigma_l tau'_l/lambda_l) Phi_l^2 w(k_l)/C
= sum a_l tau'_l = 0 by (3.2.2). Vector identity: R_m*(sigma_l tau'_l/lambda_l e_{k_l}) = sigma_l tau'_l u_l. Finally, omega - d(omega)w is "balanced" (<omega - d(omega)w, zeta_m> = 0,
A Lemma 4.2), so b^+(zhat) = 0 is the right normalisation and both representations are balanced.
(b) g = B_+ + sum R_m* Omega_{+,m}, so g - g_t = (r_+ + kappa a) + sum_m R_m*(Omega_{+,m} - omega^+_m + d(omega^+_m) w_m). |kappa| = |B_+(zhat) - r_+(zhat)| <= t/(2q_0) + (1 + ||U||)||r_+||
(G3 2.3(a)). The block term is bounded exactly as in G3 4.2(c): at bad non-peaks the + data are exact; at good coordinates (including bad PEAK carriers,
which are pinned by Lemma 2.6(c) and (H5)) the one-sided excess beyond the clamp is <= |Delta c_k| + lambda_k |Delta d| M + 2 t lambda_k, with sum |Delta c| <= K* t over good
coordinates (Lemma 2.5(a)) and |Delta d| <= K_d* t (Lemma 2.6(a), replacing G3 3.5(c)); fine coordinates contribute O(t^2); the d-difference term as in G3.
(c) sqrt(Gamma_w) is a seminorm (G3 part 2). + side: compare with (B_+, Omega_+) as in G3 4.2(d) using (b)'s estimates. - side: compare with (B_-, Omega_-):
B_- - b^- = r_- on F^c, and on F: B_- 1_F - b^- 1_F = -(Delta B 1_F - sum_{Bns} sigma_l tau'_l u_l 1_F) + kappa a = O(K' t) (Delta B = -sum Delta c_l u_l and ||tau - tau'|| <= K_H t);
blocks: Omega_- - (omega^- - d(omega^-) w) = [Omega_+ - (omega^+ - d(omega^+) w)] - Delta Omega - sum (sigma_l tau'_l/lambda_l) e_{k_l}, and Delta Omega = -sum_{Bns} (sigma_l tau_l/lambda_l) e_{k_l} + (good part),
so the lambda-weighted l_1-norm of the difference is <= (+ side error) + ||tau - tau'||_1 + K* t. By G3 2.3(d) (both signs), Gamma_w(B_+-, Omega_+-) <= 1 + eta_Gamma(eta);
H_m is invariant under adding multiples of w_m; conclude as in G3 4.2(d).
(d) Switching amplitudes: tau'_l <= |tau_l| + |tau_l - tau'_l| <= 6 lambda_l/t + K_H t (box bound G3 3.1: |Delta c_l| <= 6 lambda_l/t), so
t sum_l tau'_l <= 3 + K_H t^2 (sum lambda_l <= 1/2). Off F: ||theta V'||_1 <= sum tau'_l. On F: G3 2.5 gives ||B_+ 1_F|| <= C_F(sqrt(nu h(B_+)) + (1 + ||U|| + ||zhat||) ||B_+ 1_{F^c}|| + t/(2q_0)),
and ||B_+ 1_{F^c}|| <= ||V'|| + ||r_+||; also |kappa| <= (1 + ||U||)||bhat|| and ||b^- 1_F|| <= ||b^+ 1_F|| + sum tau'_l. Hence t||b^+-||_1 <= A_0' with A_0' depending on f only.
(Unlike G3, b need not be bounded: a switching of amplitude ~ 1/t is allowed. The expansion lemma 3.4 needs only the scale-invariant bound
t||b||_1 <= A_0', which prevents sign flips on F for |s| <= c_1 t once c_1 A_0' <= min_F |a_j|, and keeps the Hilbert part's relative error O(c_1).)
Blocks: the clamp gives 2 gap/t; at bad non-peaks |omega_+(k_l)| <= 3M/t (box, G3 2.4(e)) and |omega^-(k_l)| <= 3M/t + tau'_l/lambda_l <= (3M + 7)/t =: A_2/t. QED.

## 3.4 Lemma (one-sided uniform transfer expansion for two-piece data). PROVED.
For every eps_tr > 0 there are c_1 in (0, 1/8], t_1 > 0 (depending on f, eps_tr, A_0', A_2, gamma_B) such that for every t in (0, t_1] and all data
(b, omega) of the side sigma in {+,-} with: b balanced (b(zhat) = 0 together with balanced blocks), b 1_{F^c} supported in K and sigma-signed (sigma z_j b_j >= 0),
t ||b||_1 <= A_0'; omega_m finitely supported in Q_m, each k in supp omega_m with either [gap >= t^2 and |omega(k)| <= 2 gap/t] or [gap >= gamma_B and |omega(k)| <= A_2/t];
Gamma_w(b, omega) <= 2:   p*(f + s g_{(b,omega)}) <= 1 + (s^2/2)(Gamma_w(b, omega) + eps_tr) for all s with sigma s in (0, c_1 t].
*Proof.* G3 5.1 verbatim (transfer peaks, equalisation, decomposition A(s) + sum R* W_m(s)), with two changes.
Base (Step 5): by A Lemma 7.2, for s' := s/(1+E) of sign sigma, E_q(a + s' b) = Fl + sum_{j notin F} phi_{z_j}(s' b_j) + nu Psi(s' U*b/nu). Fl = 0 because |s' b_j| <= c_1 A_0' <= |a_j| on F
(choose c_1 <= min_F |a_j|/A_0'); the phi-terms vanish because s' b_j is z_j-signed on K and b = 0 on F^c \ K. For x in H with ||x|| <= 1/2,
Psi(x) := ||e + x|| - 1 - <e, x> <= ||P_{e-perp} x||^2/(2(1 - ||x||)) (since sqrt((1+x_par)^2 + y^2) <= 1 + x_par + y^2/(2(1 + x_par))), hence
q*(a + s' b) <= 1 + (s'^2/2) h(b)(1 + 2 |s'| ||U*b||/nu), and |s'| ||U*b|| <= c_1 ||U|| A_0' is made small by c_1.
Blocks (Step 3 (iv)): a coordinate of the second kind satisfies |W(k)| <= (1 - sd)(M - gamma_B) + c_1 A_2 <= (1 - sd) M - gamma_B/2 if c_1 A_2 <= gamma_B/4;
|s d(omega)| <= c_1 (2 + A_2) ||Phi||_2 and ||D(s omega)|| <= c_1 (2 + A_2) are made small by c_1 (Step 4). Everything else is unchanged. QED.

## 3.5 Proof of Theorem S. PROVED.
Fix g in C(f), rho in (0,1); eta_0, eps_tr = eta_0/2, kappa_0 = (sqrt(1 + eta_0/2) - 1)/2, eta with sqrt(1 + eta_Gamma(eta)) <= 1 + kappa_0 (G3 5.3 with the referee fix),
c_1, t_1 from 3.4. Along the window subsequence of (W*), for l_* large all window scales satisfy the size conditions, K_4' t <= kappa_0, and
n^w_{l_*} >= 24 rho^2 (1 + ||U||) K_2'/(c_1(1 - rho^2)), K_2' T_hi(l_*)/n^w_{l_*} -> 0 (the extra factors in K', K_2', K_4' are fixed constants times Lambda*_f(l_*)).
For each window scale t_i = T_hi(l_*) 2^{1-i} (i = 1..n) let D_i = (b^+_i, omega^+_i; b^-_i, omega^-_i) be the data of 3.3 and g_i := g_{t_i}. By 3.3(c) and 3.4,
p*(f + s g_i) <= 1 + (s^2/2)(1 + eta_0) for 0 < |s| <= c_1 t_i (+ data for s > 0, - data for s < 0), and p*(g - g_i) <= (1 + ||U||) K_2' t_i.
G3 5.2's proof (it uses only these two properties of the pieces, convexity of p*, and g in C(f)) gives rho g_avg in C(f), g_avg := (1/n) sum g_i.
The averaged data Dbar := (1/n) sum D_i are two-piece data for g_avg in the sense of P2A 1.6: averages of z-signed vectors are z-signed, supports stay in
F cup K and in the finite set of coarse non-peaks, the vector identity and d(omega^-) = d(omega^+) are linear. Gamma_w is a convex quadratic form on each side,
so kappa_w(Dbar) <= 1 + eta_0, and the data rho Dbar of rho g_avg have kappa_w <= rho^2(1 + eta_0) <= (1 + rho^2)/2 < 1 and Delta d_m = 0.
S3 Corollary D1 (F finite) gives rho g_avg in Ls(f). Finally p*(rho g_avg - rho g) <= 2 rho (1 + ||U||) K_2' T_hi(l_*)/n -> 0 and Ls(f) is closed; hence rho g in Ls(f)
for every rho < 1, i.e. g in Ls(f). QED.

## 3.6 Remarks
 (a) The route is DIFFERENT from far lowering and from Lemma Z: nothing is changed in f. The unpinned (one-sided, switching) part of every mate is kept
     as the "two-piece" part of the data instead of being dropped (G3 drops it, which is why G3 needs it to be O(K t)), and the engineering is delegated to
     S3 Corollary D1, which accepts arbitrary contact sets and arbitrary block structure but needs exact two-piece data — exactly what pinning modulo a
     polyhedral switching cone produces.
 (b) Why d-neutrality is not an extra restriction for finitely many bad carriers: by Lemma 2.6 a non-degenerate peak pins the uniform shift, so the
     switching is automatically d-neutral up to O(K t); the Hoffman projection makes it exactly d-neutral at cost O(K t). Non-d-neutral directions of the
     switching cone are therefore NOT available to mates at all (they are pinned) — in contrast with general admissible T, where P2A-type data with
     Delta d != 0 use unpinned peak coefficients (a peak k carries Delta c_k = lambda_k |Delta d| M), which the SLD signatures forbid at f with room off B.
 (c) What the hypotheses exclude (OPEN after Theorem S): infinitely many exceptional bad carriers (non-resonant, or not d-neutral), because the Hoffman
     constant of the growing polyhedral systems is not controlled by the window slack (the coefficients a_l ~ Phi_l and the values v_l(s) at the
     intersection points s in S_l cap supp y_{l'} are super-exponentially small); degenerate-peak bad carriers with sign w(k_l) = sigma_l (one-sided peak
     usage is not two-piece data); and failures of (W*) (room decaying super-fast, part 4).
