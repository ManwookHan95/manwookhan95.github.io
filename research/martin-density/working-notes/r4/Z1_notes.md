# Z1 notes — Lemma Z for the signature-ladder design: what is proved, and the precise remaining step

Round 4, task Z1. Setting: canonical base q; Martin's norm with a FINITE block set I_N (norms p_N, every N; Remark martin-tail, proved in
G3_referee sec. 4, transfers density for all p_N to Martin's p). T = SLD operator of G3 1.2, with one harmless design adjustment (min S_l strictly
increasing, part 3 preamble; Theorems A-C of G3 unaffected). Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Part files Z1_part1..5.md
(assembled below). Numerical sanity checks of the three scalar inequalities used (1.3, 2.1, 2.4(b)): all hold (max violation <= 0).

## 0. Answer
**Lemma Z is NOT proved.** No counterexample is suggested either. What is proved:
 * Lemma Z (and density) needs to be shown only for mates that are NOT window-pinned (Theorem B*, 1.5): G3's proof of Theorem B uses the
   signature room (SR) only through its conclusion "sum_l |Delta c_l| <= K t on long windows", so every window-pinned mate at ANY f with F finite
   is recovered, whether or not f is in R_0.
 * Infinite base support is not an independent obstruction (4.1 PROVED flip lemma; 4.2 Theorem B^inf SKETCH, its only unproved ingredient is the
   import of C Thm 7.4 for a not in c_00, b in c_00 from the C referee).
 * The referee's route (lower |z| on far parts of swallowed signature sets) necessarily creates a transition band [theta, sqrt(theta)] in which
   f' must reproduce f's switching EXACTLY (3.1); a better family of approximants (lower whole FINE signature sets, keep the coarse ones; 3.2)
   reduces Lemma Z to (A) "finitely-swallowed points are in R" and (B) lower semicontinuity along those approximants (3.3), both OPEN.
 * At finitely-swallowed points the free switching is bounded (4.3, PROVED), and with exact free resources everything reduces to ONE algebraic
   obstruction (5.2, PROVED): the + and - window components cannot be made to represent the same functional because their difference is an
   unsigned O(K t) junk on the swallowed contact set; G3's averaging and S3's Theorem D both need one functional (3.4 (O-c): the naive combination
   fails by the arithmetic K t_1/n >> t_1^2 4^{-n}).
 * Tools: exposed-face lemma (1.2: no approximant f' != f can contain rho C(f) exactly), ray lemma (2.3: a decomposition is reusable at smaller
   scales iff its first-order defect Delta1 vanishes; Delta1 collects near-contacts, weak peaks, flips, wrong-signed contacts).

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | R_0-approximants exist for every f (canonical truncations, far lowerings); Lemma Z is purely a lower-semicontinuity statement | PROVED | 1.1 |
| 2 | Exposed face of B_{p*} at the normer of f is {f}; hence rho C(f) subset C(f') with f' in S_{p*} forces f' = f | PROVED | 1.2-1.3 |
| 3 | Local reduction (P2A 1.4 valid for non-NA f') | PROVED | 1.4 |
| 4 | **Theorem B*: window-pinned mates at any f with F finite are in Ls(f)** (SLD T) | PROVED (by inspection of G3) | 1.5 |
| 5 | Ray lemma: one-sided reuse of a scale-t decomposition on (0, t/2] with first-order defect Delta1(t) <= t/2 | PROVED | 2.1-2.3 |
| 6 | Dichotomy Delta1 = 0 (exact resources: reusable on the whole ray) / Delta1 > 0 (useful only near scale t); averaging needs two-sided objects | PROVED | 2.4 |
| 7 | Far lowering of a coarse swallowed set: pinning only below theta_n ~ 2^{-n}; transition band [theta_n, sqrt(theta_n)] needs exact transfer | PROVED (a,b,d) / HEURISTIC (c: size of p*(f'-f)) | 3.1 |
| 8 | Approximants f^L (lower whole fine signature sets): f^L -> f, coarse data kept, fine carriers fully roomy | PROVED | 3.2 |
| 9 | Reduction: (A) R_fin subset R and (B) lsc along R_fin approximants imply density | PROVED (A, B OPEN) | 3.3 |
| 10 | Window split Cert + Free_+- + O(Kt) at points with finitely many free carriers | SKETCH | 3.4, 5.1 |
| 11 | Window averaging + S3 Thm D cannot be combined naively (scale arithmetic) | PROVED | 3.4 (O-c) |
| 12 | Flip lemma on infinite F: near-flips pinned like contacts | PROVED | 4.1 |
| 13 | Theorem B^inf: (SR) points with infinite F are in R | SKETCH (one import) | 4.2 |
| 14 | Bounded free switching through a finite free set U* (uses Y cap c_00 = {0}, T injective) | PROVED | 4.3 |
| 15 | Common-functional obstruction: unsigned O(Kt) junk on the swallowed contact set | PROVED (algebra) | 5.2 |
| 16 | Lemma Z | OPEN | 3.4, 5.3 |

## Precise remaining step
Either of the following would finish the proof of density for the SLD T (with 1.5, 3.3, 4.2):
 (RS1) [finitely-swallowed points] For f with F finite whose non-roomy signature sets are those of a finite slaving-closed set U* of carriers,
       and every g in C(f): on a sequence of long windows, choose the two side decompositions at each window scale so that the + and - components
       (5.1) represent the same functional up to a two-sided O(K t) certificate (equivalently: the contact junk J_t of 5.2 can be made -z-signed
       modulo span{u_l 1_{K_*}}), and handle near-resources on the swallowed sets (Delta1 > 0, 3.4 (O-a)). Then the averaged object is ONE
       functional with exact two-piece data plus a two-sided certificate, recovered by S3 Theorem D (Delta d >= 0; (SC) otherwise).
 (RS2) [lower semicontinuity] Along the approximants f^L of 3.2 (or any R_fin / R_0 approximants), rho C(f) is contained in Li C(f^L): i.e. the
       switching of g through FINE swallowed carriers (amplitude <= 6 lambda_l/t at scale t, 3.2(d)) can be removed at f^L, where those
       carriers are pinned, below the slack scale sqrt(c_{L+1}).
Both are instances of the Round-2 open core O3 (scale-dependent switching), now localised to signature sets of finitely many carriers (RS1)
or to box-bounded fine carriers (RS2). Leaning: positive (density); nothing found suggests a counterexample.
# Z1 part 1: setting, what Lemma Z really asks, two exact facts

Setting: canonical base q, finite block set I_N (p := p_N, every N; Remark martin-tail, G3_referee sec. 4, reduces the question
for Martin's p to all p_N). T = the SLD operator of G3 1.2. Notation of G3 (f = a + L*w, xi = q_0 zhat, zhat = z + Ue, F = supp a,
zeta_m, sigma_m, M_m, C_m, P_m, alpha_m, J_gamma, K = contacts, s(t) = sqrt(1+t^2), C(f), Ls(f), R, R_0).
Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.1 Membership in R_0 is never the issue. PROVED.
(a) (G3_ref 3.3) Any (a', z') with q*(a') = 1, z' in B_{l_inf}, z' = sign a' on supp a' defines f' = a' + L*w' in S_{p*}
    (zhat' = z' + Ue', q_0' = 1/(1 + sum_m |R_m** zhat'|_m), xi' = q_0' zhat', w'_m = J_m(R_m** xi')); f' -> f in norm when a' -> a in l_1
    and z' -> z coordinatewise (boundedly).
(b) For every f there are f'_n in R_0 with f'_n -> f: e.g. canonical truncations a'_n = a 1_{[1,n]}/q*(..), z'_n = z 1_{[1,n]} (NA, hence in
    R_0 by G3 1.4(a)); or "far lowerings" z'_n = z on [1,n], z'_n = (1 - gamma) z beyond n (not NA): then N \ J'_gamma is contained in
    F' cup [1,n], every S_l with min S_l > n is entirely roomy, and the finitely many S_l meeting [1,n] keep the positive mass
    ||h_l 1_{S_l cap (n,inf)}||, so (SR) holds with this gamma and a small vartheta.
So Lemma Z is purely a LOWER SEMICONTINUITY statement: rho C(f) subset Li C(f'_n) along SOME sequence in R_0 (equivalently, by the
R3 reduction of BRIEFING, liminf r~_{f'_n}(x) >= rho r~_f(x) for x in a countable dense set, along one sequence).

## 1.2 Lemma (the exposed face of B_{p*} at a normer is a point). PROVED.
For f in S_{p*} with normer xi in S_{p**}: {phi in B_{p*} : phi(xi) = 1} = {f}.
*Proof.* Let phi in B_{p*}, phi(xi) = 1. By A Fact A, phi = a' + L*w' with q*(a') <= 1, ||w'||_{V*} <= 1 (the infimum defining p* is
attained by weak* compactness). Then 1 = phi(xi) = a'(xi) + <w', L**xi> <= q**(xi) + ||L**xi||_V = p**(xi) = 1, so a'(xi) = q**(xi) = q_0 > 0 and
<w'_m, zeta_m> = |zeta_m|_m for every m (the V-norm is the l_1-sum and ||w'||_{V*} = max_m N_m(w'_m) <= 1). q* = ||.||_1 + ||U*.|| is strictly convex
(||U*(x+y)|| = ||U*x|| + ||U*y|| forces U*x, U*y parallel, hence x, y parallel as U* is injective), so the maximiser of a'' -> a''(xi) on B_{q*}
is unique: a' = a. |.|_m is smooth at zeta_m != 0 (T3), so w'_m = J_m(zeta_m) = w_m. Hence phi = f. QED.

## 1.3 Consequence: no "free" approximants. PROVED.
Primal form of the fibre (R2): g in C(f) iff g(x)^2 <= p(x)^2 - f(x)^2 for all x. Hence for f' in S_{p*}:
  rho C(f) subset C(f')  <=  f'(x)^2 <= rho^2 f(x)^2 + (1 - rho^2) p(x)^2 for all x  (*)
(if (*) holds and g in C(f): rho^2 g^2 <= rho^2(p^2 - f^2) <= p^2 - f'^2). The right side of (*) is the square of a norm whose dual ball contains
rho^2 f + (1 - rho^2) B_{p*} (Cauchy-Schwarz). But (*) with f' in S_{p*} forces f' = f: evaluating (*) along a net x_i -> xi' (normer of f',
weak*, with the bidual extension) gives 1 <= rho^2 f(xi')^2 + 1 - rho^2, so f(xi') = 1, xi' = xi (unique normer of f, p** strictly convex),
and f' = f by 1.2. Equivalently p*(rho^2 f + (1-rho^2) phi) < 1 for every phi in B_{p*} \ {f}.
Moral: every approximant f' != f must LOSE part of rho C(f) near its own normer; recovery is a genuinely local (small-scale) statement
at f', the slack of rho < 1 helps only at scales >~ sqrt(p*(f' - f)/(1 - rho^2)).

## 1.4 Lemma (local reduction). PROVED. (P2A Lemma 1.4, valid for f' not NA.)
Let f, f' in S_{p*}, g in C(f), rho < 1, 0 < T_0 <= 1, 0 < delta <= 1 with T_0^2 <= 3 delta. If p*(f' - f) <= (1-rho^2)T_0^2/6,
p*(g' - rho g) <= (1-rho^2) T_0/6 and p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta) for |tau| <= T_0, then g' in C(f').
(The proof of P2A 1.4 never uses that f' attains its norm.) So Lemma Z <=> for every (f, g, rho) and small T_0 there are f' in R_0 within
c T_0^2 of f and g' within c T_0 of rho g which are "local mates" (second-order bound with deficit delta) for |tau| <= T_0.

## 1.5 Window-pinned mates (Theorem B*). PROVED (by inspection of G3 parts 2-5 + G3_ref fix of 5.3).
Definition. Let f in S_{p*} with F finite and g in C(f). g is WINDOW-PINNED if there are window indices l_1 < l_2 < ... and constants K_j >= 1
with K_j T_hi(l_j) -> 0 and n^w_{l_j}/K_j -> infinity, such that for every j and every scale t in W(l_j) SOME two-sided decomposition
(B_+-, Omega_+-) of g at scale t (G3 2.1) has  sum_l |Delta c_l| <= K_j t.
Theorem B*. For the SLD T, every N, f in S_{p_N*} with F finite: every window-pinned g in C(f) lies in Ls(f).
*Proof.* G3 uses the signature room (SR) ONLY to derive the conclusion of G3 Lemma 3.4 (with K = K_1 Lambda_f(l_*)) on the windows; parts 2, 4
and 5 use only that conclusion (3.5(a)-(c) are consequences of it and of 2.3, 2.4, valid for any admissible T and any f), applied to one
decomposition per scale. Replace K_1 Lambda_f(l) by K_j throughout part 4 (the constants K_b, K_2, K_4 depend only on f, gamma, N; here
gamma enters only through K_1, which is no longer used) and in 5.3 take t^(j) = T_hi(l_j), n_j = n^w_{l_j}, K_j' := (1 + ||U||) K_2 K_j: the
hypotheses of G3 5.2 hold for large j because K_j T_hi(l_j) -> 0 (giving t <= t_*, K t <= 1, K_4 K_j t <= kappa_0, G3_ref fix) and
n^w_{l_j}/K_j -> infinity. QED.
Remarks. (i) At f in R_0 every mate is window-pinned (G3 3.4, 5.3). (ii) So Lemma Z (and density) needs to be shown only for mates that
are NOT window-pinned at f: on every late window some swallowed carrier switches by >> K t, i.e. "persistent switching through
unpinned carriers". Every such mate lives at a signature-resonant f (outside R_0) or has F infinite.
# Z1 part 2: the ray lemma (what makes a decomposition scale-dependent), any admissible T

Standing: f in S_{p*}, g in C(f), eta <= eta_* (G3 2.3), t <= t_eta, and a "+ side" decomposition at scale t: g = B + L*Omega with
q*(a + tB) <= s(t), N_m(w_m + t Omega_m) <= s(t) (G3 2.1). Notation: Kink(B) := sum_{j notin F} (|B_j| - z_j B_j) >= 0,
Fl_B(tau) := sum_{j in F} 2(-sign(a_j) tau B_j - |a_j|)_+ (A Lemma 7.2), peak_m(tau) := sum_{k in P_m} |alpha_{m,k}| (||W_tau||_inf - sigma_k W_tau(k)),
W_tau := w_m + tau Omega_m, h(B) = ||P_{e-perp} U*B||^2/nu, H_m(Omega) = ||P_m-perp D_m Omega||^2/C_m.
FIRST-ORDER (one-sided-linear) DEFECT of the decomposition:
  Delta1(t) := q_0 [Kink(B) + Fl_B(t)/t] + sum_m sigma_m peak_m(t)/t  >= 0.
Exact one-sided resources contribute nothing to Delta1: base mass on exact contacts with the contact sign, inward use of DEGENERATE peaks
(alpha_k = 0), anything on non-peaks inside the box. Near-contacts (0 < 1 - |z_j| small), wrong-signed contact mass, flips, inward use of
peaks with alpha_k > 0 (weak peaks) contribute linearly.

## 2.1 Lemma (homogeneity / convexity of the defect terms). PROVED.
For 0 < tau <= t: Kink(tau B) = tau Kink(B); Fl_B(tau) <= (tau/t) Fl_B(t); peak_m(tau) <= (tau/t) peak_m(t).
*Proof.* Kink is positively homogeneous. Each flip term tau -> 2(-sign(a_j) tau B_j - |a_j|)_+ is convex and vanishes at 0. For k in P_m,
tau -> ||W_tau||_inf - sigma_k W_tau(k) is convex (a sup of affine functions minus an affine function) and vanishes at tau = 0 (|w(k)| = M,
sigma_k = sign w(k)). A convex function phi with phi(0) = 0 satisfies phi(tau) <= (tau/t) phi(t) on [0,t]. QED.

## 2.2 Lemma (budget form). PROVED.
  Delta1(t) + (t/2) Gamma_w(B, Omega) / (1 + eta_Gamma(eta)) <= t/2,  in particular Delta1(t) <= t/2.
*Proof.* A Lemma 7.1: q_0 E_q(a + tB) + sum_m sigma_m e_m(W_t) <= t^2/2. A Lemma 7.2: E_q(a + tB) = Fl_B(t) + t Kink(B) + nu Psi(t U*B/nu) and
e_m(W_t) = peak_m(t) + t^2 ||P-perp D Omega||^2/(||D W_t|| + <D W_t, D w>/C). Bound the two quadratic terms from below exactly as in G3 2.3(d). QED.

## 2.3 Ray Lemma. PROVED.
There are c_f, eta_r > 0 (depending only on f) such that if eta <= eta_r then: with
  beta_0 := B(zhat) + Kink(B) + Fl_B(t)/t - Delta1(t),   beta_m := <Omega_m, zeta_m>/sigma_m + peak_m(t)/t - Delta1(t),
  g_t := g - beta_0 a - sum_m beta_m R_m* w_m,
one has g_t(xi) = 0, ||g - g_t||_{p*} <= c_f t, and for 0 < tau <= t/2
  p*(f + tau g_t) <= 1 + tau Delta1(t) + (tau^2/2) Gamma_max(B, Omega) (1 + c_f eta),   Gamma_max := max(h(B), max_m H_m(Omega_m)).
*Proof.* (i) q_0 beta_0 + sum_m sigma_m beta_m = [q_0 B(zhat) + sum_m <Omega_m, zeta_m>] + Delta1 - Delta1 (q_0 + sum sigma_m) = g(xi) + 0 = 0
(A Remark 2.3: g(xi) = 0; q_0 + sum sigma_m = 1). Hence g_t(xi) = g(xi) - beta_0 q_0 - sum beta_m <w_m, zeta_m> = 0. By G3 2.3(a) and 2.2,
|beta_0| <= 3t/(2q_0) and |beta_m| <= 3t/(2 sigma_m); since p*(a), p*(R_m* w_m) <= 1, ||g - g_t|| <= c_f t.
(ii) Decomposition: f + tau g_t = [(1 - tau beta_0) a + tau B] + sum_m R_m*[(1 - tau beta_m) w_m + tau Omega_m], so by A Fact A
p*(f + tau g_t) <= max( (1 - tau beta_0) q*(a + tau_0 B), max_m (1 - tau beta_m) N_m(w_m + tau_m Omega_m) ), tau_i := tau/(1 - tau beta_i) <= t for
tau <= t/2 and t small.
(iii) Base: q*(a + sB) = 1 + s B(zhat) + Fl_B(s) + s Kink(B) + nu Psi(s U*B/nu) <= 1 + s (B(zhat) + Kink(B) + Fl_B(t)/t) + (s^2/2) h(B)/(1 - ||U|| eta/nu)
for 0 < s <= t (2.1; Psi(h) <= ||h-perp||^2/(2(1 - ||h||)), ||sU*B/nu|| <= ||U|| eta/nu <= 1/2). With s = tau_0 and the factor (1 - tau beta_0):
(1 - tau beta_0)(1 + tau_0 X) = 1 - tau beta_0 + tau X = 1 + tau Delta1 (X := B(zhat) + Kink + Fl/t), and the quadratic term gets the factor
1/(1 - tau beta_0) <= 1 + c t.
(iv) Block m: N_m(w + sOmega) = 1 + s<Omega, zeta>/sigma_m + peak_m(s) + s^2 ||P-perp D Omega||^2/(||D W_s|| + <D W_s, Dw>/C) and the denominator is
>= 2(C_m - eta) (||s D Omega|| <= ||t D Omega|| <= eta, G3 2.2). With 2.1 and the same algebra, (1 - tau beta_m) N_m(w + tau_m Omega) <=
1 + tau Delta1 + (tau^2/2) H_m(Omega) C_m/(C_m - eta) (1 + c t). Take c_f eta >= the collected relative errors (t <= t_eta and t_eta -> 0 with eta). QED.

## 2.4 Consequences. PROVED.
(a) If Delta1(t) = 0 (only exact one-sided resources are used), the single normalized decomposition g_t is a ONE-SIDED LINEAR (two-piece-type)
    decomposition valid on the whole ray 0 < tau <= t/2, with second-order coefficient Gamma_max(1 + O(eta)).
(b) If Delta1(t) > 0, the same decomposition at scale tau << t costs the first-order excess tau Delta1(t), which by 2.2 can be as large as
    tau t/2: a decomposition that uses near-resources is useful only at its own scale. With rho: the bound
    p*(f + tau rho g_t) <= s(tau) holds for tau in [c_rho Delta1(t), t/2], c_rho := 4 rho/(1 - rho^2 Gamma_max(1 + c_f eta)) (when that number is < 1),
    and in general NOT below.
(c) (Why averaging over scales needs two-sided objects.) Let ghat := (1/n) sum_i rho g_{t_i} over a geometric window. For a target scale tau,
    the summands with t_i >> tau contribute (rho tau/n) sum_{t_i >> tau} Delta1(t_i), which can be of order tau t_1/n (Delta1(t_i) <= t_i/2) and is then >> tau^2 for tau << t_1/n;
    so averaging (G3 5.2, A Thm 6.8) closes the scale gap only if, for the + side AND the - side separately, the near-resource usage
    Delta1 is removable at cost O(K t) in norm (as at R_0 points, where it is bounded by pinned two-sided differences, G3 4.2(c)), or if
    Delta1 = 0. This isolates the exact obstruction for Lemma Z: PERSISTENT SWITCHING THROUGH UNPINNED CARRIERS WHOSE ONE-SIDED RESOURCES ARE NEAR
    (not exact) RESOURCES, or exact resources that differ between the two sides by O(1).
# Z1 part 3: the referee's route, quantified; a better family of approximants; where the proof stops

Standing: SLD T, p = p_N, f in S_{p*} with F finite, g in C(f) NOT window-pinned (otherwise Theorem B* applies), rho < 1.
Design adjustment (harmless): choose the signature sets in (D0) with m_l := min S_l STRICTLY INCREASING in l (e.g. S_l := {2^l(2i+1) : i >= 0}
minus j_0). G3's Theorem A uses only that the S_l are pairwise disjoint infinite subsets of N \ {j_0}; Theorems B, C use nothing else about
the S_l. So A-C remain valid verbatim (PROVED by inspection).

## 3.1 What the far lowering of a swallowed set does (referee's route). PROVED parts / HEURISTIC parts marked.
Let l_0 be a swallowed carrier (S_{l_0} contained, up to finitely many points, in contacts or near-contacts of f), n large, gamma in (0,1), and
f'_n given by (a, z'_n) with z'_n := (1 - gamma) z on G_n := S_{l_0} cap (n, inf), z'_n := z elsewhere (1.1(a)).
 (a) PROVED. f'_n -> f; the room of S_{l_0} at f'_n is ||h_{l_0} 1_{G_n}|| / ||h_{l_0}|| <= 2^{m_{l_0} - n} -> 0, so the pinning constant of
     l_0 at f'_n is delta'_{l_0}(n) <= delta°_{l_0} 2^{m_{l_0}-n}, and G3 3.2 at f'_n gives |Delta c_{l_0}| <= (t/(gamma q_0') + finer)/delta'_{l_0}(n):
     at f'_n the carrier l_0 is effectively pinned only at scales t <~ theta_n := gamma delta'_{l_0}(n) |Delta c|, i.e. below ~ 2^{-n}.
 (b) PROVED (G3 2.3(b) at f'_n). A switching of size |Delta c_{l_0}| through l_0 at scale t costs at f'_n the first-order amount
     gamma t |Delta c_{l_0}| delta'_{l_0}(n) (signature mass on the lowered part), so switching of size O(1) is affordable at f'_n exactly
     for t >~ theta_n.
 (c) HEURISTIC (cannot be proved for general T: L* is not bounded below, R3 3.2(b)). Generically eps_n := p*(f'_n - f) is of order
     min(lambda_{l_0}, gamma delta'_{l_0}(n)) ~ theta_n: by Fact C, if k_{l_0} is a strict non-peak of f, w'(k_{l_0}) - w(k_{l_0}) =
     C m u_{l_0}(xi'_n - xi)/(Phi |zeta|) + o, i.e. lambda_{l_0} |w' - w|(k_{l_0}) ~ C m^2 |u_{l_0}(xi'_n - xi)|/|zeta| ~ gamma delta'_{l_0}(n).
 (d) Consequence (PROVED as arithmetic from (a)-(c)). The slack of rho < 1 covers |tau| >~ sqrt(eps_n/(1 - rho^2)) ~ sqrt(theta_n), the
     pinning of f'_n starts below theta_n, so there is a TRANSITION BAND [theta_n, sqrt(theta_n)] (ratio -> infinity) on which f'_n must
     reproduce f's switching through l_0 with o(tau^2) error, while the trivial transfer costs eps_n >> tau^2 there. Lowering MORE
     (gamma larger, or on a larger part of S_{l_0}) only moves the band; it cannot be removed. So the band needs an EXACT transfer
     (as in P2A Thm 2.1: decompositions recomputed at f'_n, d-coefficients re-solved, steering). This is where the proof stops (3.4).

## 3.2 Better approximants: lower whole FINE signature sets, keep the coarse ones. PROVED.
For L in N let n_L := m_{L+1} - 1 and define f^L by (a, z^L) with z^L_j := 0 for j in S_l, l > L, and z^L_j := z_j otherwise.
 (a) f^L -> f as L -> infinity (z^L differs from z only on [m_{L+1}, inf); 1.1(a)).
 (b) Every S_l with l > L is entirely roomy at f^L (z^L = 0 there, and S_l misses the finite F for L large), with pinning constant
     delta'_l = delta°_l (full mass, gamma = 1/2); every S_l with l <= L keeps exactly the room it had at f. Hence f^L in R_0 iff the
     finitely many coarse sets S_1..S_L have room at f; in general f^L lies in
        R_fin := {f in S_{p*} : F finite, and (SR) holds for all l > L, for some L}  ("finitely swallowed points").
 (c) Coarse data are kept: for l <= L the vector u_l vanishes on the modified coordinates (its signature is on S_l, and by allowedness (a)
     its target y_l misses S_{l'} for l' >= l; for l' > L >= l this is the case), so u_l(zhat^L) = u_l(zhat); the forced data of f^L on coarse
     carriers differ from those of f only through the normalisations q_0, |zeta_m|, C_m, M_m, which converge (P2A Lemma 1.2 / G3_ref 3.3).
 (d) Fine carriers at f are box-bounded: for every two-sided decomposition at scale t, sum_{l > L} |Delta c_l| <= 6 sum_{l>L} lambda_l / t
     <= 6 c_{L+1}/t (G3 3.1, (P2)). So at scales t >> sqrt(c_{L+1}) the switching of g through ALL fine carriers is o(t), i.e. g is "pinned
     modulo the coarse swallowed carriers" there.
So, compared with 3.1, the transition band attached to the fine carriers sits at scales <~ sqrt(c_{L+1}), where these carriers are only
box-bounded (amplitude <= 6 lambda_l/t), and the coarse swallowed carriers are not touched at all.

## 3.3 Reduction. PROVED.
Let R_fin be as in 3.2(b). If (A) R_fin is contained in R and (B) for every f with F finite, g in C(f), rho < 1 there are f' in R_fin
arbitrarily close to f with dist(rho g, C(f')) -> 0, then NA((c_0,p_N), l_2^2) is dense (for F infinite see part 4).
*Proof.* As G3 5.4 (<=) with R_0 replaced by R_fin and Theorem B replaced by (A). QED.
Status: (A) is G3 6.3(d) (finitely many unpinned carriers, plus coarser carriers slaved to them, G3_ref 5): OPEN. (B) along f^L is OPEN.
Neither is implied by the other; both are strictly weaker than the original Lemma Z only in bookkeeping, not in kind.

## 3.4 The precise obstruction (what a proof of Lemma Z must still supply). SKETCH (the split) / PROVED (the arithmetic) / OPEN (the step).
Fix a window W(l_*) of f (l_* >= L). Exactly as in G3 parts 3-4, but declaring the carriers l <= l_* with room < vartheta^l at level gamma
(and those slaved to them) FREE, every two-sided decomposition at a window scale t splits as
   g = Cert(t) + Free_+(t) + Rem_+(t) = Cert(t) + Free_-(t) + Rem_-(t),
where Cert(t) is the (+ side) balanced finite window certificate (valid two-sidedly for |s| <= c_1 t, G3 5.1), Rem_+-(t) = O(K t) in norm
(K = K_1 vartheta^{-l_*^2} Lambda°(l_*)), and Free_+-(t) are the one-sided parts carried by the free carriers and their base counterparts
(signature mass on the swallowed sets, target mass), with Free_+(t) - Free_-(t) = O(K t) AS FUNCTIONALS but O(1) as decompositions.
Two independent defects remain:
 (O-a) NEAR resources in Free (near-contacts on swallowed sets, weak peaks among free carriers): Delta1 > 0, so by the ray lemma (2.3, 2.4(b))
       the one-sided part Free_+(t) is usable only on [c Delta1(t), t]: genuinely scale-dependent switching (O3 localised to signature sets).
 (O-b) Even with EXACT free resources (Delta1 = 0 on Free, so each side is a valid one-sided linear decomposition on the whole ray, 2.4(a)),
       averaging over the window yields two ONE-SIDED objects ghat_+ = avg(Cert + Free_+), ghat_- = avg(Cert + Free_-) with
       ||ghat_+ - ghat_-|| <= 2 K t_1/n, NOT one functional. At scales |s| < c K t_1/n the mismatch costs first order |s| K t_1/n
       (2.4(c)); it is a FIXED vector (not O(scale)), so R3's error carrying (EC + room lemma, which needs errors of size O(scale)) does not
       apply, and P2A/S3's steering removes only finitely many scalar mismatches (d-coefficients), not an infinite-dimensional remainder.
 (O-c) Why the obvious combination "window averaging (G3 5.2) + engineered two-piece recovery (S3 Thm D)" does not close (O-b). PROVED
       (arithmetic). S3 Thm D tolerates a mismatch e between the two side data if 2 rho ||e|| <= eps_0 s_1 (e enters only the side pieces, used
       for |tau| > s_1, as a genuine first-order cost 2 rho |tau| ||e||; the theta-piece used for |tau| <= s_1 represents g' exactly). But
       (i) the averaged block data have coordinatewise radius r ~ c_1 t_1 2^{-n} (bottom of the window), so the slack at f' is usable only if
           p*(f' - f) <~ (1 - rho^2) r^2, and Thm D's approximants have p*(f' - f) >~ s_1 (window masses 4 rho s_1 |b^theta_j|);
       (ii) the mismatch is eta ~ K t_1/n.
       Hence one needs K t_1/(n eps_0) <~ s_1 <~ t_1^2 4^{-n}, impossible since 4^{-n} << K/n. Equivalently: G3's averaging pays its O(K t_i)
       errors with the slack AT f at scales >= c_1 t_i, but at an engineered f' the slack starts only at sqrt(p*(f'-f)) >> bottom of the window.
       G3 escapes this because its averaged object is a single TWO-SIDED certificate, which transports to any f' with no error (A Transport
       Theorem / C Thm 7.4). With free carriers, two DIFFERENT one-sided objects are unavoidable on every window.
REMAINING STEP (OPEN, stated precisely): "two-piece closing with small mismatch": for f with F finite and one-sided exact-resource data
(Cert, Free_+, Free_-) as above with mismatch e := avg(Rem_- - Rem_+), ||e|| <= eta, show that rho ghat_+ is within o_eta(1) of C(f') for some
f' in R_0 near f (or of Ls(f)), uniformly as eta -> 0 along the windows; together with a treatment of (O-a).
# Z1 part 4: infinite base support F; bounded free switching

## 4.1 Lemma (flip analysis on an infinite support). PROVED. (Any admissible T, any f.)
Let (B_+-, Omega_+-) be a two-sided decomposition of g in C(f) at scale t <= t_eta (G3 2.1) and put, for j in F,
  f^-_j := (sign(a_j) B_-(j) - |a_j|/t)_+  (flip excess of the - side),  f^+_j := (-sign(a_j) B_+(j) - |a_j|/t)_+  (flip excess of the + side),
  e_j := (sign(a_j) B_+(j) - 2|a_j|/t)_+.
Then sum_j f^-_j <= t/(4 q_0), sum_j f^+_j <= t/(4 q_0), e_j <= |Delta B(j)| + f^-_j, and the clamp
  b^cl(j) := sign(B_+(j)) min(|B_+(j)|, 2|a_j|/t)  (j in F)
satisfies ||(B_+ - b^cl) 1_F||_1 <= ||Delta B 1_F||_1 + t/(2 q_0).
*Proof.* A Lemma 7.2: the flip term of E_q(a + tB_+) is sum_j 2(-sign(a_j) t B_+(j) - |a_j|)_+ = 2t sum f^+_j, and that of E_q(a - tB_-) is
2t sum f^-_j; the budget (A Lemma 7.1) gives q_0 E_q <= t^2/2 for each side. If e_j > 0 then sign(a_j)B_+(j) = 2|a_j|/t + e_j while
sign(a_j) B_-(j) <= |a_j|/t + f^-_j, so sign(a_j) Delta B(j) >= |a_j|/t + e_j - f^-_j >= e_j - f^-_j. The clamp removes e_j in the direction
sign(a_j) and (-sign(a_j)B_+(j) - 2|a_j|/t)_+ <= f^+_j in the other. Sum. QED.
(At f in R_0-type points ||Delta B|| <= K t (G3 3.5(a)), so the clamp costs O(K t): near-flips are pinned exactly like contacts.)

## 4.2 Theorem B^inf (G3 Theorem B for infinite F). SKETCH, with one imported ingredient.
For the SLD T and every N: every f in S_{p_N*} satisfying (SR) (no finiteness of F) is in R; more generally Theorem B* (1.5) holds for
window-pinned mates at f with arbitrary F.
Changes to G3 (each checked):
 (i) Window certificate: replace B_+ 1_F by the clamp b^cl (4.1), then truncate to a finite F_t subset of F with sum_{F \ F_t} |a_j| <= t^2
     (cost ||b^cl 1_{F \ F_t}|| <= 2t), and balance with a_t := a 1_{F_t}/(a 1_{F_t})(zhat) (note (a 1_{F_t})(zhat) -> a(zhat) = 1):
     b_t := b^cl 1_{F_t} - kappa_t a_t, kappa_t := (b^cl 1_{F_t})(zhat) = O(K t) (G3 2.3(a), 3.5(b), 4.1; ||zhat||_inf <= 1 + ||U||).
     Then supp b_t is finite, b_t(zhat) = 0, |b_t(j)| <= 2|a_j|/t + O(K t)|a_j|, and the remainder estimate 4.2(c) gains O(K t) + 2t. G3 2.5
     (finite-dimensional injectivity, used only for ||b_t|| <= K_b) is no longer needed.
 (ii) Uniform transfer expansion G3 5.1 with (C-a) replaced by (C-a'): |b_j| <= 3|a_j|/t on supp b (finite), Gamma_w(c) <= 2. In Step 5 only
     two facts about b were used: no sign flips for |s'| <= c_1 t (now |s' b_j| <= 3 c_1 |a_j| < |a_j| for c_1 < 1/3), and |s'| ||U*b||/nu small
     (now |s'| ||b||_1 <= 3 c_1 ||a||_1, so |s'| ||U*b||/nu <= 3 c_1 ||U||/nu, absorbed by choosing c_1 small after eps_tr). Steps 0-4, 6 do not
     involve b. PROVED modulo this bookkeeping.
 (iii) Windowed averaging G3 5.2: unchanged (it uses only (i)-(ii) and the final recovery).
 (iv) Final recovery: G3 uses C Thm 7.4 (balanced finite certificate with Gamma_w <= 1 is recovered along canonical truncations), proved in C for
     a in c_00. For a not in c_00 one needs C Thm 7.4 with a in l_1 \ c_00 and b in c_00: IMPORTED from the C referee (Remark 7.1' extended to
     b != 0, script rem71_check.py), NOT re-proved here. This is the only reason for the label SKETCH.
Consequence: modulo (iv), infinite base support is not an independent obstruction: Lemma Z may use approximants with (SR) and arbitrary F,
and the open core is exactly signature resonance (failure of (SR)) with persistent switching (1.5 Remark (ii)).

## 4.3 Lemma (bounded free switching). PROVED. (Any admissible T, f with F finite.)
Let U* be a finite set of carriers. There is C_{U*} (depending on f, U*) such that for every two-sided decomposition at scale t <= t_eta,
  max_{l in U*} |Delta c_l| <= C_{U*} ( 1 + || sum_{l notin U*} Delta c_l u_l ||_1 ).
*Proof.* Delta B = -sum_l Delta c_l u_l. By G3 2.3(d), nu h(B_+-) <= nu (1 + eta_Gamma)/q_0, i.e. ||P_{e-perp} U* B_+-|| <= c_f, so
||P_{e-perp} U* sum_{U*} Delta c_l u_l|| <= 2 c_f + ||U|| ||sum_{l notin U*} Delta c_l u_l||_1. The linear map c -> P_{e-perp} U*(sum_{U*} c_l u_l) on R^{U*}
is injective: if it vanishes, U*(sum c_l u_l) is parallel to U*a, hence sum c_l u_l = mu a (U* injective); the left side lies in Y = Ran T, a is in
c_00, and Y cap c_00 = {0}, so mu a = 0 and sum_{U*} c_l u_l = 0; since u_l = T e_{k(l),m(l)}/c_l (weights c_l > 0), this says T(sum_{U*} (c_l/c_l^w) e_{k(l),m(l)}) = 0,
so all coefficients vanish (T injective). A injective linear map on a finite-dimensional space is bounded below. QED.
Use: if the carriers outside U* are pinned on a window (sum_{l notin U*} |Delta c_l| <= K t), the free switching through U* is BOUNDED (not
just box-bounded, |Delta c| <= 6 lambda/t): a finitely-swallowed point has bounded switching amplitudes on every window. (The closure of a finite
set U of swallowed carriers under "slaving" -- add every coarser l with kappa_{l',l} > 0 for some l' already in the set -- is finite, because
targets are finitely supported and the S_l are disjoint; G3_ref 5.)
# Z1 part 5: the common-functional obstruction at finitely-swallowed points (why exact free resources are not yet enough)

Setting: SLD T, f with F finite, a finite set U* of free carriers closed under slaving (4.3), all other carriers with room (so on every
window sum_{l notin U*} |Delta c_l| <= K t, G3 3.2-3.4 run over l notin U*), and "exact free resources":
 (E1) every l in U* is a strict non-peak of f;  (E2) supp u_l \ F is contained in the contact set K for l in U* (no roomy or near-contact part).
By 4.3, Delta c_{U*} is bounded. Write K_* := union over U* of supp u_l \ F.

## 5.1 What the window decomposition gives. SKETCH (G3 parts 3-4 with U* removed from the pinning system; all estimates as there).
At every window scale t, the + side decomposition splits as
  g = [Cert_+(t)] + [Free_+(t)] + Rem_+(t),
Cert_+(t): G3's balanced finite certificate built from B_+ 1_F and the clamped coarse PINNED carriers (two-sided, valid for |s| <= c_1 t);
Free_+(t): the base part B_+ 1_{K_*} (z-signed, exact contacts) and the U* carrier coefficients c^+_l (strict non-peaks; on the + ray they are
admissible whatever their size, ray lemma 2.3 with Delta1 = 0);
Rem_+(t): base on non-contacts, fine carriers, clamp excess of pinned carriers, normalisations: O(K t) in norm.
Same on the - side with B_- 1_{K_*} (-z-signed). Each "component" Cert_+(t) + Free_+(t) is valid on (0, c_1 t] (one-sided).

## 5.2 The obstruction. PROVED (algebra).
For the windowed averaging (G3 5.2) one needs, at each window scale, a + component and a - component representing the SAME functional
(the + component's functional is Phi_t = g - Rem_+(t)). The - component must use Cert_+(t) (or something within O(K t) two-sided of it), its own
-z-signed base on K_*, and U* carrier coefficients c'_l. Matching the functional forces, on K_*,
  B'_-  =  B_+ 1_{K_*} + sum_{U*} (c^+_l - c'_l) u_l 1_{K_*},
and with c'_l = c^-_l this equals B_- 1_{K_*} + J_t, where J_t := -sum_{l notin U*} Delta c_l u_l 1_{K_*} - (pinned clamp/normalisation terms on K_*)
is O(K t) but has NO sign. B'_- must be -z-signed. Changing c' by xi moves B'_- along span{u_l 1_{K_*}} only. Moving junk between the
sides is impossible: a z-signed addition x on the + side and a -z-signed addition y on the - side change the mismatch by x - y, which lies in
the z-cone; so a mismatch J_t can be cancelled exactly iff -J_t (modulo span{u_l 1_{K_*}}) lies in the z-cone.
Otherwise the wrong-signed part of J_t costs the first-order amount |s| ||J_t^wrong|| <= |s| K t at the scales |s| <= c_1 t where the component
is used, and averaging over the window turns this into |s| K t_1/n (2.4(c)), which is not o(s^2) as s -> 0.
In G3 (no free part) this never arises because the single + certificate is valid on both sides. With free carriers, the two components
differ by an infinite-dimensional, unsigned O(K t) junk on the contact set K_*, and neither G3's averaging nor S3 Theorem D (which needs one
functional, part 3 (O-c)) absorbs it.

## 5.3 Two ways the remaining step could be closed (HEURISTIC; not carried out).
 (a) Make the junk signed: choose, at each window scale, the decompositions (not unique) so that J_t lies in the -z-cone modulo span{u_l 1_{K_*}}.
     Optimal decompositions are only determined up to null pairs (beta, Omega) with beta + L*Omega = 0; it is plausible but not shown that the
     slack rho < 1 (which makes every scale-t decomposition non-tight by (1 - rho^2) t^2/2) leaves enough room for such a choice.
 (b) Engineer the approximant so that the swallowed contact set K_* becomes part of the base support of f' on a window (window masses as in
     P2A/S3 3.3; then contact junk is two-sided there) and lower the far part (3.1); this re-creates the transition band of 3.1(d), now with the
     window-averaged (scale-dependent) data on the band, which is exactly the O3 core localised to the finitely many swallowed signature sets.
