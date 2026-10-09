# Z2 part 1: sign-mixed signature room (SR±) and a sharper window condition — Theorem B± (PROVED)

Setting: exactly that of G3 (canonical base q; Martin's norm with finite block set I_N, p := p_N, any N >= 1; the SLD operator T of
G3 1.2; notation of G3 parts 1-5). Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.1 The contact-cost function phi_z
For z in [-1,1] and x real put phi_z(x) := |x| - z x >= 0. Elementary facts (PROVED, one line each):
 (F1) phi_z(x - y) <= phi_z(x) + phi_{-z}(y)   (|x - y| <= |x| + |y| and -z(x - y) = -zx + zy).
 (F2) |phi_z(x + r) - phi_z(x)| <= (1 + |z|)|r| <= 2|r|.
 (F3) for v >= 0 and c real: phi_z(-c v) = |c| v (1 + z sign c).
 (F4) min_{sigma = +-1} sum_s v_s (1 + sigma z_s) = ||v||_1 - |<v, z>| for v >= 0 (the two sums are ||v|| + <v,z> and ||v|| - <v,z>).

## 1.2 Budget for the switching difference (PROVED; any admissible T)
Let f in S_{p*} (F = supp a arbitrary), g in C(f), t <= t_eta with eta <= eta_* (G3 2.2-2.3), and (B_+-, Omega_+-) a two-sided
decomposition of g at scale t (G3 2.1); Delta B := B_+ - B_-. Then
   sum_{j notin F} phi_{z_j}(Delta B(j)) <= t / q_0.                                                     (1.2.1)
*Proof.* G3 2.3(b) (= A Lemma 7.1 + A Lemma 7.2): sum_{j notin F} phi_{z_j}(B_+(j)) <= t/(2q_0) and sum_{j notin F} phi_{-z_j}(B_-(j)) <= t/(2q_0).
Apply (F1) with x = B_+(j), y = B_-(j) and sum. QED.
Meaning: the base part of the switching Delta B may live, at no first-order cost, only on coordinates j notin F with |z_j| = 1, and only with
sign(Delta B(j)) = z_j. ("One-sided contact resources", A Cor 7.3(a); here for the DIFFERENCE of the two sides.)

## 1.3 Definition (sign-mixed room; class R_0^±)
For a ladder index l (with m(l) <= N) let v_l(s) := delta_l 2^{-s}/n_l (s in S_l) be the signature profile of u_l (G3 (P1)) and
   theta_l(f) := min_{sigma = +-1} sum_{s in S_l \ F} v_l(s)(1 + sigma z_s) = ||v_l 1_{S_l \ F}||_1 - |<v_l 1_{S_l \ F}, z>|      (F4).
Put Lambda^±_f(l) := prod_{l' <= l, m(l') <= N} (1 + 3/theta_{l'}(f))  (:= +infinity if some theta_{l'} = 0).
**R_0^±** := { f in S_{p*} : F finite, theta_l(f) > 0 for every l with m(l) <= N, and
               liminf_{l -> infinity} Lambda^±_f(l) / (l 2^{l^3} Lambda°(l)) = 0 }    (condition (W±)).
Remarks (PROVED).
 (a) R_0 subset R_0^±. If f has (SR) with constants gamma, vartheta, then on S_l cap J_gamma both weights 1 +- z_s are >= gamma, so
     theta_l >= gamma delta'_l >= gamma vartheta^l delta°_l; hence 1 + 3/theta_l <= (3/(2 gamma)) vartheta^{-l} (1 + 2/delta°_l) and
     Lambda^±_f(l) <= (3/(2gamma))^l vartheta^{-l^2} Lambda°(l) = o(l 2^{l^3} Lambda°(l)).
 (b) R_0^± is strictly larger. It contains first rows with COFINITE contact set (|z_j| = 1 for every j notin F) as soon as every S_l \ F
     sees both contact signs with non-negligible v_l-mass. Example: if z alternates in sign along the increasing enumeration
     s_0 < s_1 < s_2 < ... of S_l \ F, then (alternating series) |<v_l 1_{S_l\F}, z>| <= c(2^{-s_0} - 2^{-s_1}/2) and ||v_l 1_{S_l\F}|| >= c(2^{-s_0} + 2^{-s_1})
     (c = delta_l/n_l), so theta_l >= (3/4) 2^{-(s_1 - s_0)} ||v_l 1_{S_l \ F}||_1; (W±) holds e.g. if s_1 - s_0 <= C l on every S_l.
     In general theta_l = ||v_l 1_{S_l\F}|| - |<v_l 1_{S_l\F}, z>| > 0 whenever z is not constant on S_l \ F, and (W±)
     holds whenever theta_l / delta°_l >= vartheta^l (any vartheta > 0) — more generally whenever prod_{l'<=l} (delta°_{l'}/theta_{l'}) grows
     slower than 2^{l^3} along a subsequence. It also contains near-contact first rows (|z_s| -> 1 on every S_l) as long as the
     weighted defects sum_{s} v_l(s)(1 - |z_s|) decay at most like vartheta^l delta°_l (no fixed gamma is needed).
 (c) theta_l(f) = 0 iff z_s = sigma_l (one constant sign) for EVERY s in S_l \ F (v_l > 0 on all of S_l): "exact monochromatic swallowing".
     f notin R_0^± with F finite iff either some S_l \ F is exactly swallowed, or the relative rooms theta_l/delta°_l decay so fast that
     Lambda^±_f(l) >= c l 2^{l^3} Lambda°(l) for all large l.

## 1.4 Lemma (sign-mixed pinning inequality). PROVED.
Let f, g, t, (B_+-, Omega_+-) be as in 1.2 and let the c^+-_l, Delta c_l, kappa_{l',l} be as in G3 3.2. Put
E^±_l := sum_{s in S_l \ F} phi_{z_s}(Delta B(s)). Then for every l:
   theta_l |Delta c_l| <= E^±_l + 2 sum_{l' > l} kappa_{l',l} |Delta c_{l'}|,      and   sum_l E^±_l <= t/q_0.
*Proof.* By G3 (P1) (signature privacy and coarse-to-fine allowedness), for s in S_l: -Delta B(s) = Delta c_l v_l(s) + r_l(s), with
r_l(s) := sum_{l' > l} Delta c_{l'} y_{l'}(s)/n_{l'}. By (F2) and (F3),
  |Delta c_l| v_l(s)(1 + z_s sign Delta c_l) = phi_{z_s}(-Delta c_l v_l(s)) <= phi_{z_s}(Delta B(s)) + 2|r_l(s)|.
Sum over s in S_l \ F: the left side is >= |Delta c_l| theta_l by definition of theta_l; sum_s |r_l(s)| <= sum_{l'>l} kappa_{l',l}|Delta c_{l'}|.
The bound on sum E^±_l is (1.2.1) (the S_l are disjoint). QED.

## 1.5 Lemma (triangular solution and window defect). PROVED.
For a window index l_* (coarse set Cset = {l <= l_*}, fine set Fset = {l > l_*}, all with m(l) <= N):
  sum_{l in Cset} |Delta c_l| <= Lambda^±_f(l_*) [ sum_{l in Cset} E^±_l + (8/3) sum_{l' in Fset} |Delta c_{l'}| ],
and if t in W(l_*), t <= min(t_eta, 1):   sum_l |Delta c_l| <= K^±_1 Lambda^±_f(l_*) t,   K^±_1 := 1/q_0 + 22.
*Proof.* D_l := |Delta c_l|, X_l := E^±_l + 2 sum_{l' in Fset} kappa_{l',l} D_{l'}, S_l := sum_{l' in Cset, l' >= l} D_{l'}. By 1.4 and kappa <= 4/3,
D_l <= (X_l + (8/3) S_{l+1})/theta_l, so S_l <= X_l/theta_l + (1 + 8/(3 theta_l)) S_{l+1}. Unrolling from l_* down,
S_1 <= sum_{l in Cset} (X_l/theta_l) prod_{l'' < l}(1 + 8/(3theta_{l''})) <= (sum_l X_l) prod_{l'' <= l_*}(1 + 3/theta_{l''})
(1/theta_l <= 1 + 3/theta_l). sum_l X_l <= sum E^±_l + (8/3) sum_{Fset} D (sum_l kappa_{l',l} <= 4/3). For the window bound:
sum E^± <= t/q_0 (1.4), sum_{Fset} D <= 6 t^2 (G3 3.4: box bound 3.1 and (P2), t >= T_lo(l_*)); so
sum_l D_l <= Lambda^±(t/q_0 + 16 t^2) + 6t^2 <= Lambda^± t (1/q_0 + 22) (Lambda^± >= 1, t <= 1). QED.

## 1.6 Theorem B± (PROVED). For the SLD operator T and every N: R_0^± is contained in R.
*Proof.* Identical to G3 parts 3-5 with the following replacements, which are the only places where (SR), gamma or vartheta enter:
 * G3 3.2-3.4 are replaced by 1.4-1.5 (K := K^±_1 Lambda^±_f(l_*)). G3 3.5 holds verbatim with this K: (a) is the triangle inequality,
   (b) is G3 2.3(b) plus (a), (c) uses only G3 2.4(d) and the identity <Dw, D Delta Omega> = (1/m) sum Phi_k w(k) Delta c_k.
 * G3 part 4 (window certificate) uses only 3.4-3.5 and the part-2 toolkit; its constants K_b, K_2, K_4, C' depend on (f, N) only
   (gamma entered only through K_1, now replaced by K^±_1 which does not involve gamma).
 * G3 5.1, 5.2 do not involve (SR).
 * G3 5.3 (with the referee's fix kappa_0 = (sqrt(1 + eta_0/2) - 1)/2): instead of letting l -> infinity through all integers, let l run
   through a sequence L_f along which Lambda^±_f(l)/(l 2^{l^3} Lambda°(l)) -> 0 (exists by (W±)). Along L_f, by (P3):
     Lambda^±_f(l) T_hi(l) <= Lambda^±_f(l) 2^{-l^3}/(l Lambda°(l)) -> 0,
     n^w_l / Lambda^±_f(l) >= l 2^{l^3} Lambda°(l)/Lambda^±_f(l) -> infinity,
   so for l in L_f large: every window scale t satisfies t <= t_*, K t <= 1, K_4 Lambda^± t <= kappa_0; n^w_l >= 24 rho^2 K_l/(c_1(1 - rho^2))
   with K_l := (1 + ||U||) K_2 Lambda^±_f(l); and K_l T_hi(l)/n^w_l -> 0. These are exactly the hypotheses of G3 5.2 with t^(j) := T_hi(l_j).
   G3 5.2 then gives (f, rho' rho g) in cl NA for all rho, rho' < 1. QED.
Corollary (PROVED). For the SLD T, density of NA((c_0,p_N), l_2^2) is equivalent to Lemma Z± := Lemma Z with R_0 replaced by R_0^±
(the class of admissible approximants is enlarged; (<=) by Theorem B±, (=>) since NA ∩ S_{p*} ⊂ R_0 ⊂ R_0^±).

## 1.7 What Theorem B± settles among the "hard cases" of the task (PROVED)
 * First rows with F finite and K cofinite (no |z_j| < 1 anywhere outside F, J_gamma = empty for every gamma): they are in R as soon as
   z is sign-mixed on the signature sets in the quantitative sense (W±). G3's (SR) never holds for them; (SR±) frequently does.
 * First rows whose near-contacts "swallow" every signature set in G3's sense (for every gamma, J_gamma misses most of every S_l): in R
   as soon as the weighted defects sum_s v_l(s)(1 - |z_s|) (or sign mixing) decay at most geometrically in l (relative to delta°_l), or more
   generally slower than allowed by (W±). G3's (SR) requires a FIXED gamma; (SR±) does not.
 * What remains outside R_0^± with F finite: EXACT monochromatic swallowing of some S_l \ F (z == sigma_l on all of it), or super-fast
   decay of the relative room along all l. These are treated in parts 2-4.
