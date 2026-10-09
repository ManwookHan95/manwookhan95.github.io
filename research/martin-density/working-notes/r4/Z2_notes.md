# Z2 notes — Lemma Z of G3 by routes other than far lowering: sign-mixed room, exact resonances recovered without moving f, hard cases, no-go results

Round 4, task Z2. Setting: canonical base q; Martin's norm with FINITE block set I_N (p := p_N, any N >= 1; Remark martin-tail, proved by the G3
referee, transfers density to p); T = the signature-ladder design (SLD) of G3 1.2 unless "any admissible T" is said. Notation of G3 (parts 1-5) and
A_notes §1/§7. Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Part files: ctx/r4/Z2_part1.md ... Z2_part5.md (this file supersedes their wording).
Script: scratchpad/Z2_work/check_split.py (numerical check of 1.1 and Lemma 2.3; max violation 2e-12).
Imports (all refereed): G3 parts 2, 4, 5 with the referee's kappa_0-fix of 5.3; G3 referee 3.3 (construction of f from (a, z)); A Lemmas 4.2, 4.3, 7.1, 7.2;
C Thm 7.4; P2A 1.6 (two-piece data); S3 Corollary D1 (F finite, two-piece data with Delta d_m >= 0 in all blocks and kappa_w <= 1 => g in Ls(f); any
admissible T, any contact set, no condition on Q_m); S3 Cor D2 ((BT) points are in R); Preprint A Thm "residual recovery" and Prop "nonvacuity".

## 0. Summary
| # | Statement | Status | § |
|---|---|---|---|
| 1 | Switching budget: sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0, phi_z(x) = |x| - zx (any T) | PROVED | 1.2 |
| 2 | **Theorem B±**: R_0 ⊂ R_0^± ⊂ R, R_0^± = {F finite, sign-mixed room theta_l = ||v_l 1_{S_l\F}|| - |<v_l 1_{S_l\F}, z>| > 0, window condition (W±)}. Covers COFINITE contact sets with sign-mixed signatures and near-contacts with geometric room decay (no fixed gamma) | PROVED | 1 |
| 3 | A non-degenerate pinned peak pins the uniform shift Delta d (any T) | PROVED | 2.1 |
| 4 | theta-split: a z-signed switching splits coordinatewise between the two sides, residual O(t) (any T) | PROVED (+numerics) | 2.3 |
| 5 | Pinning modulo exactly swallowed carriers; non-d-neutral and wrong-sign-peak switching is pinned | PROVED | 2.5-2.6 |
| 6 | **Theorem S**: first rows with finitely many exactly swallowed signature sets (any contact set, any blocks; (H4),(H5),(W*)), or infinitely many all resonant and d-neutral ((H3),(H4),(W*)), are in R — recovered WITHOUT approximating f (windowed averaging into two-piece data + S3 Cor D1) | PROVED | 3 |
| 7 | Contact sandwich structure; cushion structure on infinite supports (any T) | PROVED | 4.1, 4.4 |
| 8 | Hard cases: maximal contact (z == const off F), super-fast room decay, full support without room | OPEN (obstructions identified) | 4 |
| 9 | Design modifications cannot remove swallowing (any admissible T) | PROVED | 5.1 |
| 10 | Design-free certificate form of Lemma Z (Lemma Z_cert => density for ANY admissible T; <=> for SLD) | PROVED | 5.2 |
| 11 | Omega ∩ {F finite} meagre; a non-recoverable (f, rho g) forces A_eps = {f' near f with a mate near rho g} to be meagre | PROVED | 5.3 |
| 12 | Scale tension: windowed averaging at an approximant works only in the pinned regime | HEURISTIC | 5.2 |
| 13 | Lemma Z in full generality | OPEN | — |
Leaning: positive. No counterexample to Lemma Z was found; every hard structure that could be analysed completely (exact resonances, sign-mixed
contacts, geometric near-contacts) turned out to be recovered, and the remaining open classes are meagre, non-generic conditions.

## 1. Sign-mixed room: Theorem B± (PROVED)
**1.1 phi-calculus.** For z in [-1,1], phi_z(x) := |x| - zx >= 0. (F1) phi_z(x - y) <= phi_z(x) + phi_{-z}(y). (F2) |phi_z(x + r) - phi_z(x)| <= 2|r|.
(F3) phi_z(-cv) = |c| v (1 + z sign c) for v >= 0. (F4) min_{sigma=+-1} sum_s v_s(1 + sigma z_s) = ||v||_1 - |<v,z>| for v >= 0. (Elementary.)
**1.2 Switching budget (any admissible T).** For g in C(f), t <= t_eta (eta <= eta_*), a two-sided decomposition (B_+-, Omega_+-) (G3 2.1), Delta B := B_+ - B_-:
  sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0.   Proof: G3 2.3(b) (A Lemmas 7.1, 7.2) and (F1). QED.
**1.3 Definition.** v_l(s) := delta_l 2^{-s}/n_l on S_l (signature profile of u_l). theta_l(f) := min_sigma sum_{s in S_l\F} v_l(s)(1 + sigma z_s)
= ||v_l 1_{S_l\F}||_1 - |<v_l 1_{S_l\F}, z>|. Lambda^±_f(l) := prod_{l' <= l, m(l') <= N} (1 + 3/theta_{l'}). R_0^± := {F finite, theta_l > 0 for all l, and
(W±): liminf_l Lambda^±_f(l)/(l 2^{l^3} Lambda°(l)) = 0}.
Facts (PROVED). (a) R_0 ⊂ R_0^±: under (SR), theta_l >= gamma vartheta^l delta°_l, whence Lambda^± <= (3/(2gamma))^l vartheta^{-l^2} Lambda°. (b) theta_l = 0 iff z == sigma_l on all
of S_l \ F (exact monochromatic swallowing). (c) Example: if z alternates in sign along the increasing enumeration s_0 < s_1 < ... of S_l \ F, then
theta_l >= (3/4) 2^{-(s_1 - s_0)} ||v_l 1_{S_l\F}||; so first rows with |z| == 1 off F (cofinite contacts, J_gamma empty for all gamma) are in R_0^± when the
contact signs alternate along the signature sets with s_1 - s_0 <= C l. (d) near-contacts: theta_l >= sum_s v_l(s)(1 - |z_s|), no fixed gamma needed.
**1.4 Lemma (sign-mixed pinning).** With c^+-_l, Delta c_l, kappa_{l',l} as in G3 3.2 and E^±_l := sum_{s in S_l\F} phi_{z_s}(Delta B(s)):
  theta_l |Delta c_l| <= E^±_l + 2 sum_{l'>l} kappa_{l',l} |Delta c_{l'}|,   sum_l E^±_l <= t/q_0.
Proof. On S_l, -Delta B(s) = Delta c_l v_l(s) + r_l(s), r_l(s) = sum_{l'>l} Delta c_{l'} y_{l'}(s)/n_{l'} (G3 (P1)). By (F2), (F3):
|Delta c_l| v_l(s)(1 + z_s sign Delta c_l) <= phi_{z_s}(Delta B(s)) + 2|r_l(s)|; sum over S_l \ F and use the definition of theta_l. QED.
**1.5 Lemma (window defect).** sum_{l <= l_*}|Delta c_l| <= Lambda^±(l_*)[sum E^± + (8/3) sum_{l > l_*}|Delta c_l|], and for t in W(l_*), t <= min(t_eta,1):
sum_l |Delta c_l| <= (1/q_0 + 22) Lambda^±_f(l_*) t.
Proof. D_l <= (X_l + (8/3)S_{l+1})/theta_l with X_l = E^±_l + 2 sum_{fine} kappa D, S_l = sum_{l <= l' <= l_*} D_{l'}; unroll: S_1 <= (sum X_l) prod (1 + 3/theta).
Fine carriers: <= 6t^2 (box bound G3 3.1 and (P2)). QED.
**1.6 Theorem B± (PROVED).** For the SLD T and every N, R_0^± ⊂ R.
Proof. G3 parts 3-5 with 3.2-3.4 replaced by 1.4-1.5 (K := (1/q_0 + 22)Lambda^±(l_*)); G3 3.5, part 4, 5.1, 5.2 do not involve (SR) (gamma entered only K_1).
In 5.3 let l run through a subsequence along which Lambda^±/(l 2^{l^3} Lambda°) -> 0: then Lambda^± T_hi(l) -> 0, n^w_l/Lambda^± -> infinity, which are exactly
the window hypotheses of G3 5.2. QED.  Corollary: for SLD, density <=> Lemma Z with R_0 replaced by R_0^±.

## 2. Lemmas at first rows with swallowed signatures
Notation: omega_+- = Omega_+- + d_+- w (G3 2.4), Delta Omega := Omega_+ - Omega_-, Delta c_k := lambda_k Delta Omega(k), Delta d_m := d_{+,m} - d_{-,m}.
**2.1 Lemma (peak pinning of the shift; any T). PROVED.** For every peak k of block m (sigma_k = sign w(k)):
  |omega_+(k)| + |omega_-(k)| = -sigma_k Delta Omega(k) - Delta d M >= 0;
and if alpha_{m,k} != 0 then  -|Delta Omega(k)| - t/(sigma_m|alpha_k|) <= Delta d M <= |Delta Omega(k)|.
Proof. G3 2.4(c): sigma_k omega_+(k) <= 0 <= sigma_k omega_-(k) and sum_P |alpha_k||omega_+-(k)| <= t/(2sigma_m); w(k) = sigma_k M. QED.
**2.2 Lemma (d-identity; any T). PROVED.** Delta d_m M_m = (1/(m C_m)) sum_k Phi_m(k) w_m(k) Delta c_k + r_m, |r_m| <= 2t/sigma_m. (G3 2.4(d), as in G3 3.5(c).)
**2.3 Lemma (theta-split; any T). PROVED.** If V is supported in K, z-signed, and Delta B 1_{F^c} = V + e, then there are theta: supp V -> [0,1] and r_+- with
  B_+ 1_{F^c} = theta V + r_+,  B_- 1_{F^c} = -(1 - theta)V + r_-,  ||r_+-||_1 <= ||e||_1 + t/q_0.
Proof. Coordinatewise, x = B_+(j), y = B_-(j), x - y = V_j + e_j; G3 2.3(b): sum phi_z(x) <= t/(2q_0), sum phi_{-z}(y) <= t/(2q_0). If V_j = 0 take theta_j = 0, r = (x, y):
|x| + |y| <= |e_j| + phi_z(x) + phi_{-z}(y). If V_j != 0 (|z_j| = 1), X = z_j x, Y = z_j y, v = |V_j|: phi_z(x) = 2X_-, phi_{-z}(y) = 2Y_+;
theta_j := clamp(X/v,0,1); |r_+(j)| = dist(X,[0,v]) <= X_- + Y_+ + |e_j| (X - v = Y + z_j e_j); |r_-(j)| = |Y + (1-theta_j)v| <= X_- + Y_+ + |e_j| (three cases). Sum. QED.
**2.4 Definitions.** B(f) := {l : m(l) <= N, theta_l(f) = 0}, sigma_l the swallowing sign (z == sigma_l on S_l \ F). l in B is RESONANT if
(Res_l) z_j sigma_l u_l(j) = |u_l(j)| for all j notin F; then ũ_l := sigma_l u_l 1_{F^c} is z-signed and supported in K. l is d-NEUTRAL if w_{m(l)}(k_l) = 0
(<=> u_l(xi) = 0, by the block-threshold lemma; such k_l is a strict non-peak). For l notin B: theta*_l := room of S*_l := S_l \ (F ∪ ⋃_{l' in B, l'>l} supp y_{l'});
rho_l := theta*_l (l notin B), rho_l := 2||v_l 1_{S_l\F}|| (l in B); Lambda*_f(l) := prod_{l' <= l} (1 + 3/rho_{l'}).
(W*): rho_l > 0 for all l and liminf Lambda*_f(l)/(l 2^{l^3}Lambda°(l)) = 0. (H3): supp y_{l'} ∩ S_l = empty for l < l' both in B.
(H4): every block has a non-degenerate peak (alpha != 0) with ladder index notin B. (H5): no l in B sits at a degenerate peak with sign w(k_l) = sigma_l.
**2.5 Lemma (pinning modulo swallowed carriers). PROVED.** Assume F finite, (W*); t in W(l_*), l_* large in the (W*) subsequence; K* := (1/q_0 + 22)Lambda*(l_*).
 (a) sum_{l notin B} |Delta c_l| <= K* t.   [Triangular system 1.5 on S*_l; bad finer targets vanish there; no (H3) needed.]
 (b) Under (H3), with tau_l := -sigma_l Delta c_l (l in B): rho_l (tau_l)_- <= E_l + 2 sum_{l'>l, l' notin B} kappa |Delta c_{l'}|, hence sum_{B ∩ Cset}(tau_l)_- <= K* t.
 (c) Under (H3) and if every l in B is resonant: Delta B 1_{F^c} = sum_{B∩Cset}(tau_l)_+ ũ_l + e, ||e|| <= 4K*t + 6t^2.
Proof. (b): on S_l \ F, -Delta B = Delta c_l v_l + (good finer targets) by (H3); z == sigma_l there, and phi_{sigma}(-Delta c v) = 2(sigma Delta c)_+ v. (c): Delta B = -sum Delta c_l u_l. QED.
**2.6 Lemma (switching is d-neutral up to O(t); peaks pin). PROVED.** Assume (H4); k_1 a non-degenerate peak of block m with index notin B, <= l_*. Then
 (a) |Delta d_m| M_m <= t/(sigma_m|alpha_{k_1}|) + K* t/lambda_{k_1} =: K_d* t   (2.1 + 2.5(a));
 (b) |sum_{l in B∩Cset, m(l)=m} a_l tau_l| <= (K_d* + 2/sigma_m) t + (K* t + 6t^2)/(m C_m),  a_l := sigma_l Phi_m(k_l) w_m(k_l)/(m C_m)   (2.2);
 (c) if l in B∩Cset sits at a peak k: when alpha_k != 0, |tau_l| <= lambda_l(t/(sigma_m|alpha_k|) + K_d* t) (plus the lower bound of 2.5(b) or of 3.2); when
     sign w(k) = -sigma_l, tau_l <= lambda_l K_d* t.   [(2.1) at k with Delta Omega(k) = -sigma_l tau_l/lambda_l.] QED.
Remark (PROVED by 2.6): at such f a switching through a non-d-neutral resonant carrier is impossible beyond O(t) (one block, one bad carrier) — the
P2A-type data with Delta d != 0 of Round 2 used unpinned peak coefficients (Delta c_k = lambda_k |Delta d| M at every peak), which SLD signatures forbid.

## 3. Theorem S (PROVED): exact resonances are recovered without moving f
**Statement.** SLD T. Let f have F finite, satisfy (H4), (H5), (W*), and either (S_fin) B(f) finite, or (S_inf) (H3) and every l in B(f) resonant and d-neutral.
Then f is in R.
**3.1 Projection to the admissible switching cone.** (S_fin) Let T_0 := ⋃_{l in B} supp y_l (finite). For tau in R^B, c(tau) := sum_{j notin F} phi_{z_j}(sum_{l in B} sigma_l tau_l u_l(j))
= sum_{l in B} 2(tau_l)_- ||v_l 1_{S_l\(F∪T_0)}|| + sum_{j in T_0\F} phi_{z_j}(linear form) (on S_l only u_l's signature and finer bad targets live): a finite sum of convex
piecewise-linear functions. Let Bpk := {l in B : k_l a peak} and Z := {tau : c(tau) = 0, tau_l = 0 (l in Bpk), sum_{m(l)=m} a_l tau_l = 0 (all m)}, a polyhedral cone
⊂ R^B_+. Hoffman's bound: dist_1(tau, Z) <= H (c(tau) + sum_{Bpk}|tau_l| + sum_m|sum a_l tau_l|), H = H(f). At window scales c(tau) <= t/q_0 + 2(K* t + 6t^2)
(1.2, (F2), 2.5(a)), sum_{Bpk}|tau_l| = O(K*t) (2.6(c), (H5), and c), sum_m |...| = O(K* t) (2.6(b)); so some tau' in Z has ||tau - tau'||_1 <= K_H t.
(S_inf) tau'_l := (tau_l)_+; Bpk = empty, a_l = 0, and sum|tau - tau'| <= K* t (2.5(b)).
In both cases V' := sum_{B∩Cset} sigma_l tau'_l u_l 1_{F^c} is z-signed, supported in K, Delta B 1_{F^c} = V' + e', ||e'|| <= K' t, sum_{m(l)=m} a_l tau'_l = 0.
**3.2 Window two-piece data.** Lemma 2.3 gives B_+1_{F^c} = theta V' + r_+, B_-1_{F^c} = -(1-theta)V' + r_-. Bns := (B ∩ Cset) \ Bpk.
 + : omega^+_m := G3-clamp of omega_{+,m} on good coarse non-peaks with gap >= t^2, plus omega_{+,m}(k_l) at k_l (l in Bns); bhat := B_+1_F + theta V', b^+ := bhat - bhat(zhat) a.
 - : omega^-_m := omega^+_m + sum_{l in Bns, m(l)=m}(sigma_l tau'_l/lambda_l) e_{k_l};  b^- := b^+ - sum_{l in Bns} sigma_l tau'_l u_l.
 g_t := b^+ + sum_m R_m*(omega^+_m - d(omega^+_m)w_m).
**Lemma 3.2 (PROVED).** (a) These are two-piece data (P2A 1.6) for g_t with Delta d_m = 0: z b^+ >= 0 >= z b^- on K (b^- 1_{F^c} = -(1-theta)V'), supports in F ∪ K,
omega^+- finitely supported in Q_m, d(omega^-) - d(omega^+) = sum a_l tau'_l = 0 and R_m*((sigma tau'/lambda) e_{k_l}) = sigma tau' u_l give the second representation; balance
(<omega - d(omega)w, zeta_m> = sigma_m <omega, alpha_m> = 0 off peaks) gives b^+-(zhat) = 0. (b) ||g - g_t||_1 <= K_2' t. (c) Gamma_w(b^+-, omega^+-) <=
(sqrt(1 + eta_Gamma(eta)) + K_4' t)^2. (d) t||b^+-||_1 <= A_0'; |omega^+-(k)| <= 2gap/t at good coordinates (gap >= t^2); |omega^+-(k_l)| <= A_2/t at bad non-peaks,
whose gaps are >= gamma_B > 0. (K', K_2', K_4' = C(f) Lambda*(l_*); A_0', A_2, gamma_B depend on f only.)
Proof. (b) g - g_t = r_+ + kappa a + sum R*(Omega_+ - omega^+ + d(omega^+)w), |kappa| <= t/(2q_0) + (1+||U||)||r_+||; blocks as in G3 4.2(c), with |Delta d| <= K_d* t
(2.6(a)) replacing G3 3.5(c), exact at bad non-peaks, bad peaks pinned (2.6(c)). (c) seminorm property of sqrt(Gamma_w); + side vs (B_+,Omega_+), - side vs
(B_-,Omega_-): B_- - b^- = r_- on F^c and O(K't) on F; Omega_- - (omega^- - d(omega^-)w) = (+ error) + sum sigma_l(tau_l - tau'_l)/lambda_l e_{k_l} - (good part of Delta Omega),
lambda-weighted norm O(K't); G3 2.3(d) for both sides; H_m ignores multiples of w. (d) tau'_l <= 6lambda_l/t + K_H t (box bound) so t sum tau'_l <= 3 + K_H t^2;
||B_+1_F|| via G3 2.5; |omega_+(k_l)| <= 3M/t (box), |omega^-(k_l)| <= (3M + 7)/t. QED.
**3.3 Lemma (one-sided uniform transfer expansion). PROVED.** For eps_tr > 0 there are c_1, t_1 (depending on f, eps_tr, A_0', A_2, gamma_B) such that for t <= t_1, data
(b, omega) of side sigma as in 3.2(d) (b balanced, b1_{F^c} sigma z-signed in K, t||b|| <= A_0', Gamma_w <= 2): p*(f + s g_{(b,omega)}) <= 1 + (s^2/2)(Gamma_w + eps_tr) for
0 < sigma s <= c_1 t.
Proof. G3 5.1 verbatim, except: (base) A Lemma 7.2 gives E_q(a + s'b) = nu Psi(s'U*b/nu) (no flips since c_1 A_0' <= min_F|a_j|; no kink terms since s'b is z-signed on K),
and Psi(x) <= ||P_{e-perp}x||^2/(2(1 - ||x||)), ||x|| <= c_1||U||A_0'/nu small; (blocks) a bad coordinate moves by |s omega| <= c_1 A_2 <= gamma_B/4 and stays below
(1 - sd)M - gamma_B/2; Hilbert and d-terms are O(c_1). QED.
**3.4 Proof of Theorem S.** For g in C(f), rho < 1: choose eta_0, kappa_0, eta, c_1, t_1 as in G3 5.3 (referee fix). On windows l_* of the (W*) subsequence, l_* large,
take the data D_i of 3.2 at t_i = T_hi(l_*)2^{1-i}, i <= n = n^w_{l_*}; by 3.2-3.3 the pieces g_i satisfy p*(f + s g_i) <= 1 + (s^2/2)(1+eta_0) for |s| <= c_1 t_i
(+ data for s > 0, - data for s < 0) and p*(g - g_i) <= (1+||U||)K_2' t_i, with n >= 24 rho^2(1+||U||)K_2'/(c_1(1-rho^2)) and K_2' T_hi/n -> 0. G3 5.2's proof gives
rho g_avg in C(f), g_avg = (1/n) sum g_i. The averaged data are two-piece data (convexity of the sign conditions and of the supports; the identities and
d-neutrality are linear) with kappa_w <= 1 + eta_0 (Gamma_w convex), so rho g_avg carries data with kappa_w <= rho^2(1+eta_0) < 1 and Delta d = 0. S3 Cor D1:
rho g_avg in Ls(f). p*(rho g_avg - rho g) -> 0 and Ls(f) is closed: g in Ls(f). QED.
**3.5 Remarks.** (a) Nothing in f is moved: the unpinned switching is kept in the two-piece part of the data (G3 drops it and therefore needs it O(t)),
and S3's engineering (which accepts any contact set and any blocks but needs EXACT two-piece data) does the rest. (b) Theorem S settles G3 6.3(d)
(HEURISTIC there) for exact finitely generated resonances, including the P1 phenomenon in the SLD space with arbitrary block structure.
(c) Not covered: infinitely many non-resonant or non-d-neutral swallowed carriers (the Hoffman/d-neutralisation constants of the growing finite
systems involve v_l(s) ~ sqrt(c_{l'}) at intersection points and a_l ~ Phi_l, not absorbed by 2^{l^3}); degenerate-peak bad carriers with sign w = sigma_l
(one-sided peak usage is not two-piece data); approximate swallowing (theta_l > 0 tiny): the switching vector is z-signed only up to O(t), and S3 Cor D1
needs exact data.

## 4. The hard cases (task (a))
**4.1 Proposition (contact structure; any T). PROVED.** For g in C(f), t <= t_eta: sum_K (z_j B_+(j))_- <= t/(4q_0), sum_K (z_j B_-(j))_+ <= t/(4q_0); hence on K the mate is
sandwiched in the z-order between the off-F traces of the two block perturbations: z_j(g - L*Omega_+)(j) >= -eps^+_j, z_j(g - L*Omega_-)(j) <= eps^-_j,
sum(eps^+ + eps^-) <= t/(2q_0); and the switching -sum Delta c_k u_k is z-signed on K and vanishes elsewhere off F up to l_1-mass O(t) (1.2).
**4.2 Case (a1): F finite, |z_j| = 1 for all j notin F.** Mates = z-order sandwiches between block traces; the fibre is large (HEURISTIC example: beta e_j* - beta(1 + (Ue)_j) a
for a carrier with target e_j*/q*(e_j*) and beta <~ sqrt(lambda_l)). Status: sign-mixed signatures (W±): in R (Thm B±); finitely many monochromatic S_l with
(H4),(H5),(W*): in R (Thm S_fin; no resonance or d-neutrality needed); infinitely many monochromatic S_l, all resonant and d-neutral: in R (Thm S_inf).
MAXIMAL CONTACT (z == sigma off F): every carrier is swallowed; l is resonant iff sigma y_l >= 0 off F; infinitely many are not (each target recurs
infinitely often) — OPEN, obstruction as in 3.5(c).
**4.3 Case (a2): near-contacts swallowing every signature.** B(f) = empty; carrier l is pinned below the scale theta_l and almost free above (explicit
scale-dependent switching, item O3). In R if the relative rooms decay at most geometrically (Thm B±; G3's fixed gamma is not needed). Super-fast decay: OPEN.
**4.4 Case (a3): infinite F (cushions). Proposition (any T). PROVED.** sum_{j in F}(-sign(a_j)B_+(j) - |a_j|/t)_+ <= t/(4q_0) and sum_{j in F}(sign(a_j)B_-(j) - |a_j|/t)_+ <= t/(4q_0)
(A Lemma 7.2 flip term + budget). So a support coordinate is two-sided free inside its cushion |tB_j| <= |a_j| and contact-like (z_j = sign a_j) beyond.
Status: generic f (supp a = N) are in Omega ⊂ R (Preprint A); room off F: G3 6.3(e) SKETCH, Thm B± likewise SKETCH; full support without room: block switching
is absorbed by in-cushion base mass on both sides and is not pinned — OPEN.

## 5. Routes (b)
**5.1 (b)(i) design. Proposition (any admissible T). PROVED.** For every finite F, a in S_{q*} with supp a = F and carrier (k,m) with u = u_{k,m} not supported in F, the
first row f built from (a, z), z_j := sign u(j) on supp u \ F, z := sign a on F, z := 0 elsewhere, has zero base cost for the switching Delta B = c u 1_{F^c}, c >= 0
(phi_{z_j}(c u(j)) = 0). For private-signature designs z == sigma swallows all signature sets at once and (for SLD) infinitely many swallowed carriers are
non-resonant; two-colour signatures / several signature sets per carrier are swallowed by matching patterns; signatures inside supp a give no pinning
(cushions, 4.4). So no design removes the bad set; designs can only shape the fine structure of resonances, and finitely generated resonances are
harmless anyway (Thm S).
**5.2 (b)(ii) transitivity. Proposition (Lemma Z_cert). PROVED.** For ANY admissible T: if every (f, rho g) is approximated by (f', g') with supp a' finite,
g' in C(f'), and g' = g_c for a balanced finite certificate with Gamma_w <= 1 (C Thm 7.4) or g' carrying two-piece data with Delta d >= 0, kappa_w <= 1 (S3 Cor D1),
then NA((c_0,p_N), l_2^2) is dense; for SLD the converse holds (NA points are in R_0 and G3 Cor 6.4). HEURISTIC (scale tension): making one-sided usage U two-sided
at radius r at an approximant costs p*(f'-f) >~ rU against a slack (1-rho^2)r^2/2, so averaging at approximants handles only U = O(r) (pinned regime); switching mates
need exact structure, which is why Thm S hands them to S3 Cor D1.
**5.3 (b)(iii) Omega. Proposition. PROVED.** (a) R ⊇ Omega ∪ R_0^± ∪ R_S ∪ BT ∪ NA, Omega comeagre; so S \ R is meagre. (b) {supp a finite} is meagre (Preprint A), so
R_0^±, R_S, BT, NA are meagre, Omega ∩ R_0 is meagre and Omega_0 has infinite supports: intersecting Omega with R_0 gives nothing new. (c) If (f, rho g) is not in
cl NA then A_eps := {f' : p*(f'-f) < eps, dist(rho g, C(f')) < eps} is meagre for some eps (indeed A_eps ∩ R = empty, else closedness gives (f, rho g) in cl NA).
So a counterexample needs a mate destroyed by generic small perturbations of f; this is compatible with all remaining open classes (meagre conditions), so
topology alone cannot decide Lemma Z.
**5.4 Relation to far lowering.** At f in R_S far lowering is unnecessary. For the open classes the candidate approximants are far lowering/flipping (room),
far SHARPENING (make near-swallowed far sets exactly monochromatic, landing in R_S when the swallowed carriers are resonant and d-neutral), and cushion
engineering (full support); each needs a mate transfer across a transition band (OPEN).

## 6. Main obstacle and next steps
Main obstacle: infinitely generated switching — first rows at which infinitely many coarse carriers are swallowed and non-resonant/non-d-neutral
(maximal contact z == const off F is the model case), and near-swallowing with super-fast room decay. In both, the per-window switching cone is
polyhedral but its Hoffman/d-neutralisation constants are not controlled by the window slack, and S3 Cor D1 needs exact data.
Next steps: (1) at maximal contact, try to choose the window decompositions so that the switching uses only boundedly many carriers per window
(minimal-support decompositions), which would make the Hoffman constants design-controlled; (2) redesign the ladder so that the window lengths
dominate the (design-computable) Hoffman constants of the cone part, and treat d-neutrality by an anchor/shift argument instead of exact projection;
(3) far sharpening combined with Thm S_inf for near-swallowing; (4) prove the infinite-F version of Thm B± (G3 6.3(e)) and extend S3 Cor D1 to a not in c_00.
