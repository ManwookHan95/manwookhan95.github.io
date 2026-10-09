# Z5 part 2: Theorem B^inf made rigorous; window-pinned mates and sign-mixed room at arbitrary F

Setting: T = SLD operator (Definition def:SLD), N >= 1, I = {1..N}, p = p_N; f in S_{p*} with F = supp a arbitrary
(finite or infinite). For j in F put s_j := sgn a_j (= z_j). We write alpha(M) := sum_{j in F, j > M} |a_j| (the tail of a).

## 2.0 Which results of Section 8 hold verbatim for infinite F. PROVED.
The following statements of the note are proved there without using finiteness of F (checked line by line):
Lemma lem:twosided, Lemma lem:smallness (its proof uses only: A_n -> a coordinatewise boundedly and limsup ||A_n||_1 <= ||a||_1
imply ||A_n - a||_1 -> 0, valid for every a in l_1), Lemma lem:budget (a)-(d), Lemma lem:suplevel, Lemma lem:box,
Lemma lem:pinning, Lemma lem:triangular, Proposition prop:pinned (a)-(c) [for f satisfying (SR), J_gamma excludes F],
Lemma lem:phicalc, Lemma lem:switchbudget, Lemma lem:split, Lemma lem:peakshift, Lemma lem:flip (stated for F infinite),
Lemma lem:signmixed (for f with r_l computed on S_l \ F; the hypothesis "finite base support" is not used in its proof),
Lemma lem:avgfunctionals. NOT valid for infinite F: Lemma lem:finitebase (finite-dimensional injectivity), and hence
Proposition prop:windowcert(b), Lemma lem:uniformtransfer (hypothesis (C-a) with A_0 independent of t is not available),
Lemma lem:boundedfree (needs a in c_00, see 4.8), and the last sentence of Theorem thm:windowed (repaired in Part 1, Remark 1.3(c)).

Definition 2.1. R_0^inf := set of f in S_{p*} satisfying (SR) of Definition def:R0 (F arbitrary; J_gamma = {j notin F : |z_j| <= 1-gamma}).
Definition def:windowpinned is read verbatim for arbitrary F.

## 2.1 The clamped window certificate. PROVED.
Let f be arbitrary, eta <= eta_*, l_* a window index, t in W(l_*), t <= min(t_eta, 1), and (B_+-, Theta_+-) a two-sided
decomposition of g in C(f) at scale t. Suppose that on this decomposition
  (PIN_K)   sum_l |Delta theta_l| <= K t   (K >= 1), and hence ||Delta B||_1 <= K t
holds (for f in R_0^inf this is Proposition prop:pinned(a) with K = K_1 Lambda_f(l_*); for window-pinned mates it is the hypothesis).
Then Proposition prop:pinned (b),(c) hold with this K (their proofs use only (a), Lemma lem:budget(b), Lemma lem:suplevel).
Define:
  b^cl(j) := sgn(B_+(j)) min(|B_+(j)|, 2|a_j|/t) for j in F, b^cl := 0 off F;
  M_t := min{M >= 0 : alpha(M) <= t^2},  F_t := F cap [1, M_t] (finite),  a_t := a 1_{F_t};
  kappa_t := (b^cl 1_{F_t})(zhat) / a_t(zhat),  b_t := b^cl 1_{F_t} - kappa_t a_t;
  omega^c_m := as in Definition def:windowcert;   c_t := (b_t, (omega^c_m)_m).

Proposition 2.2 (window certificate, arbitrary F). Assume (PIN_K), K t <= 1 and t^2 <= 1/(2(1+||U||)). Put
K_kappa := 1/(2q_0) + (1+||U||)(2K + 3/(2q_0) + 2). Then:
(a) a_t(zhat) >= 1/2; c_t is a finitely based balanced finite certificate: supp b_t is contained in F_t (finite), b_t(xi) = 0,
    and omega^c_m satisfies (C-b) of Lemma lem:uniformtransfer: supp omega^c_m in {k in Q_m: gap_m(k) >= t^2}, |omega^c_m(k)| <= 2 gap_m(k)/t;
(b) |kappa_t| <= 2 K_kappa t, and if 2 K_kappa t^2 <= 1 then |b_t(j)| <= 3|a_j|/t for every j;
(c) ||B_+ - b_t||_1 <= K_B t with K_B := 2K + 3/(2q_0) + 2 + 2K_kappa, and ||g - g_{c_t}||_1 <= K'_2 K t, K'_2 depending only on f, N, design;
(d) sqrt(Gamma_w(c_t)) <= sqrt(1 + eta_Gamma(eta)) + K'_4 K t, K'_4 depending only on f, N and the design.

Proof. (a) |a_t(zhat) - 1| = |(a - a_t)(zhat)| <= ||zhat||_inf alpha(M_t) <= (1+||U||) t^2 <= 1/2, using a(zhat) = 1 and
||zhat||_inf <= ||z||_inf + ||U e||_inf <= 1 + ||U||. Then b_t(zhat) = (b^cl 1_{F_t})(zhat) - kappa_t a_t(zhat) = 0, so
b_t(xi) = q_0 b_t(zhat) = 0. The statement on omega^c_m is Proposition prop:windowcert(a), whose proof does not involve F.
(b) Write (b^cl 1_{F_t})(zhat) = B_+(zhat) - (B_+ 1_{F^c})(zhat) - ((B_+ - b^cl) 1_F)(zhat) - (b^cl 1_{F \ F_t})(zhat). Here
|B_+(zhat)| <= t/(2q_0) (Lemma lem:budget(a)); ||B_+ 1_{F^c}||_1 <= K t + t/q_0 (Proposition prop:pinned(b));
||(B_+ - b^cl) 1_F||_1 <= ||Delta B 1_F||_1 + t/(2q_0) <= K t + t/(2q_0) (Lemma lem:flip and (PIN_K));
||b^cl 1_{F \ F_t}||_1 <= (2/t) alpha(M_t) <= 2t. Hence |(b^cl 1_{F_t})(zhat)| <= K_kappa t and |kappa_t| <= 2 K_kappa t.
Finally |b_t(j)| <= |b^cl(j)| + |kappa_t| |a_j| <= 2|a_j|/t + 2K_kappa t |a_j| <= 3|a_j|/t when 2K_kappa t^2 <= 1.
(c) B_+ - b_t = B_+ 1_{F^c} + (B_+ - b^cl) 1_F + b^cl 1_{F\F_t} + kappa_t a_t; add the four bounds (||a_t||_1 <= 1).
The block part of g - g_{c_t} is the same as in the proof of Proposition prop:windowcert(c), which uses only Lemma lem:suplevel,
Lemma lem:box, (P2), Proposition prop:pinned (a),(c); it is bounded by (constant depending on f, N, design) x K t.
(d) As in Proposition prop:windowcert(d): sqrt(Gamma_w) is a seminorm on data, Gamma_w(B_+,Theta_+) <= 1 + eta_Gamma(eta)
(Lemma lem:budget(d)), and the remainder (B_+ - b_t, X) has q_0 h(B_+ - b_t) <= ||U||^2 ||B_+ - b_t||_1^2/nu and
sigma_m H_m(X_m) <= (sum_k lambda_{k,m}|X_m(k)|)^2/C_m, both <= (const K t)^2 by (c). QED

## 2.2 Uniform transfer expansion with cushion-proportional base parts. PROVED (any admissible T, I finite, any f).

Lemma 2.3. For every eps_tr > 0 there are c_flat in (0, 1/8] and t_1 > 0 (depending only on f and eps_tr) such that for every
t in (0, t_1] and every finitely based balanced finite certificate c = (b, omega) at f with
  (C-a')  |b_j| <= 3|a_j|/t for all j, and Gamma_w(c) <= 2;
  (C-b)   supp omega_m in {k in Q_m : gap_m(k) >= t^2} and |omega_m(k)| <= 2 gap_m(k)/t,
we have p*(f + r g_c) <= 1 + (r^2/2)(Gamma_w(c) + eps_tr) for all |r| <= c_flat t.

Proof. Follow the proof of Lemma lem:uniformtransfer; only the base estimates and one error term change.
Let |r| <= c_flat t, A := a + r b, W_m := w_m + r(omega_m - d_m w_m); lin_b(A) = r b(zhat) = 0, lin_m(W_m) = 0 (Lemma lem:algebra).
Base: supp b is contained in F and |r b_j| <= 3 c_flat |a_j| < |a_j| if c_flat < 1/3, so no coordinate of A changes sign on F and b
vanishes off F; by Lemma lem:bookkeeping(b), Exc(r b) = 0 and G_b(A) = nu Psi(r U*b/nu). As ||b||_1 <= 3||a||_1/t <= 3/t,
||r U*b||/nu <= 3 c_flat ||U||/nu <= 1/2 if c_flat <= nu/(6||U|| + 1). By Lemma lem:base,
  G_b(A) <= (r^2/2) h(b) / (1 - ||rU*b||/nu) <= (r^2/2) h(b) (1 + K'_A c_flat),   K'_A := 6||U||/nu.
Blocks: exactly as in Lemma lem:uniformtransfer (no change): G_m(W_m) <= (r^2/2) H_m(omega_m)(1 + 2c_flat/C_min) when
c_flat <= min(1/4, C_min/2). Rebalancing: as there, with transfer data for eta_1 := min(1/4, eps_tr/(8|I|K_3)); conditions (eq:R1)
hold under the same conditions on c_flat, t_1 (||W_m - w_m||_inf <= 3 c_flat, ||D_m(W_m - w_m)||_2 <= 2 c_flat). In the error E of
Proposition prop:rebalancing the term |lambda|(|q*(A) - 1| + q*(A - a)) is now bounded by
  |lambda| . 2 q*(r b) <= |I| K_3 K_Y r^2 . 2(1+||U||) c_flat t ||b||_1 <= 6 |I| K_3 K_Y (1+||U||) c_flat r^2
(instead of a term of order |r|^3). Hence
  p*(f + r g_c) <= 1 + (r^2/2)Gamma_w(c)(1 + K'_A c_flat + 2c_flat/C_min) + |I|K_3 eta_1 r^2
                   + 6|I|K_3K_Y(1+||U||)c_flat r^2 + (8K_3K_y c_flat r^2 + K_3^2 K_y^2 r^4)/C_min.
Choose eta_1 as above, then c_flat so small that 2(K'_A + 2/C_min)c_flat + 6|I|K_3K_Y(1+||U||)c_flat + 8K_3K_y c_flat/C_min <= eps_tr/4
(recall Gamma_w <= 2), then t_1 so small that K_3^2K_y^2 r^2/C_min <= eps_tr/8 for |r| <= c_flat t_1 and the conditions of Lemma lem:TV
hold. The total is <= 1 + (r^2/2)(Gamma_w(c) + eps_tr). QED

## 2.3 Theorems. PROVED.

Theorem 2.4 (window-pinned mates at arbitrary F; Theorem thm:Bstar for every F). Let f in S_{p*} (F arbitrary) and let g in C(f) be
window-pinned at f (Definition def:windowpinned). Then (f, g) in cl NA((c_0, p_N), l_2^2).

Proof. Fix rho in (0,1). Choose eta_0 in (0,2] with rho^2(1+eta_0) <= (1+rho^2)/2, kappa_0 := (sqrt(1+eta_0/2) - 1)/2,
eps_tr := eta_0/2, and c_flat, t_1 from Lemma 2.3; eta <= eta_* with eta_Gamma(eta) <= 1 and sqrt(1+eta_Gamma(eta)) <= 1 + kappa_0.
Let (l_j, K_j) be the data of Definition def:windowpinned and K := K_j + 6 <= 7K_j (as in step (1) of the proof of thm:Bstar, the fine
carriers add <= 6t^2). For j large every dyadic scale t of W(l_j) satisfies t <= min(t_eta, t_1, 1), Kt <= 7K_j T_hi(l_j) <= 1,
t^2 <= 1/(2(1+||U||)), 2K_kappa t^2 <= 1 (K_kappa = O(K), and K T_hi(l_j)^2 -> 0) and K'_4 K t <= kappa_0. For such t take the
decomposition given by window pinning and its clamped window certificate c_t (Proposition 2.2). Then Gamma_w(c_t) <= (1 + 2kappa_0)^2
= 1 + eta_0/2 <= 2, (C-a') and (C-b) hold, so Lemma 2.3 gives p*(f + r g_{c_t}) <= 1 + (r^2/2)(1 + eta_0) for |r| <= c_flat t, and
p*(g - g_{c_t}) <= (1+||U||)||g - g_{c_t}||_1 <= (1+||U||) K'_2 . 7 K_j t. The triples (T_hi(l_j), n^w_{l_j}, 7(1+||U||)K'_2 K_j) satisfy
the hypotheses of Theorem thm:windowed (n^w_{l_j}/K_j -> infinity, K_j T_hi(l_j) -> 0). The proof of thm:windowed up to its last
sentence (valid for every f) gives finitely based balanced finite certificates c with rho g_c in C(f), Gamma_w(rho c) <= 1 and
rho g_c -> rho g; Theorem 1.2 (Part 1) gives (f, rho' rho g_c) in cl NA for every rho' < 1. Hence (f, rho g) in cl NA; rho -> 1. QED

Theorem 2.5 (B^inf). For the SLD operator and every N, R_0^inf is contained in Rec. PROVED.
Proof. By Proposition prop:pinned(a) (valid for arbitrary F, see 2.0), every mate at f in R_0^inf satisfies (PIN_K) on every dyadic
scale of W(l) with K = K_1 Lambda_f(l), and Lambda_f(l) <= varpi_0^{-l^2} Lambda°(l); as in the proof of Theorem thm:R0,
K T_hi(l) -> 0 and n^w_l/K -> infinity. So every mate is window-pinned (Remark rem:Bstar(a) verbatim); apply Theorem 2.4. QED

Theorem 2.6 (sign-mixed room at arbitrary F). Let R_0^{pm,inf} be the set of f in S_{p*} (F arbitrary) with r_l := min_sigma
sum_{s in S_l \ F} v_l(s)(1 + sigma z_s) > 0 for all l in L_N and (W^pm). Then R_0^{pm,inf} is contained in Rec. PROVED.
Proof. Lemma lem:signmixed holds for arbitrary F (2.0); so the proof of Theorem thm:Bpm shows that every mate is window-pinned;
apply Theorem 2.4. QED

## 2.4 Cushion room (support coordinates inside signature sets). PROVED.

Lemma 2.7 (cushion lemma). Let f be arbitrary, g in C(f), t > 0 and (B_+-, Theta_+-) a two-sided decomposition at scale t. For j in F,
  (s_j Delta B(j))_- <= 2|a_j|/t + f^+_j + f^-_j,   sum_{j in F} (f^+_j + f^-_j) <= t/(2q_0)
(f^+-_j as in Lemma lem:flip). Equivalently: on F the switching Delta B is s-signed up to the "cushion allowance" 2|a_j|/t and an
l_1-error of mass t/(2q_0); a support coordinate behaves at scale t like a contact with sign s_j = sgn a_j, plus an allowance.
Proof. By definition of f^+-_j, -s_j B_+(j) <= |a_j|/t + f^+_j and s_j B_-(j) <= |a_j|/t + f^-_j; add. The sum bound is Lemma lem:flip. QED

Definition 2.8 (cushion room). For M >= 0 put F_{<=M} := F cap [1, M] and
  r_l^{[M]} := min_{sigma = +-1} sum_{s in S_l \ F_{<=M}} v_l(s) (1 + sigma z_s)   (z_s = s_s on F),
  Lambda^c_f(l, M) := prod_{l'' <= l, l'' in L_N} (1 + 3/r^{[M]}_{l''})  (:= infinity if some factor is infinite),
  M(t) := min{M : alpha(M) <= t^2}.
(W^c): liminf_{l -> infinity} Lambda^c_f(l, M(T_lo(l))) / (l 2^{l^3} Lambda°(l)) = 0.
Since S_l \ F_{<=M} contains S_l \ F and all summands are >= 0, r_l^{[M]} >= r_l, so (W^pm) implies (W^c).

Theorem 2.9 (cushion room suffices). Every f in S_{p*} satisfying (W^c) belongs to Rec. PROVED.
Proof. Let t > 0, M >= M(t) and E^c_l := sum_{s in S_l \ F_{<=M}} phi_{z_s}(Delta B(s)). Since the S_l are disjoint,
  sum_l E^c_l <= sum_{j notin F} phi_{z_j}(Delta B(j)) + sum_{j in F, j > M} 2 (s_j Delta B(j))_-
             <= t/q_0 + 2 sum_{j in F, j > M} (2|a_j|/t + f^+_j + f^-_j) <= t/q_0 + 4t + t/q_0
(Lemma lem:switchbudget, Lemma lem:phicalc(a) with |z_j| = 1 on F, Lemma 2.7 and alpha(M) <= t^2). For s in S_l, by (P1) and
(eq:DeltaB), -Delta B(s) = Delta theta_l v_l(s) + r_l(s), r_l(s) := sum_{l'>l} Delta theta_{l'} y_{l'}(s)/n_{l'}; as in the proof of
Lemma lem:signmixed (summing |Delta theta_l| v_l(s)(1 + z_s sgn Delta theta_l) <= phi_{z_s}(Delta B(s)) + 2|r_l(s)| over
s in S_l \ F_{<=M}), r_l^{[M]} |Delta theta_l| <= E^c_l + 2 sum_{l'>l} pi_{l',l} |Delta theta_{l'}|. Unrolling as in Lemma lem:signmixed,
for t in W(l_*): sum_l |Delta theta_l| <= (2/q_0 + 26) Lambda^c_f(l_*, M) t.
For t in W(l_*) we have t >= T_lo(l_*), hence M(T_lo(l_*)) >= M(t) (M(.) is nonincreasing in t), and we may take M := M(T_lo(l_*))
for all scales of the window. By (W^c) choose l_1 < l_2 < ... with Lambda^c_f(l_j, M(T_lo(l_j)))/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0 and
put K_j := (2/q_0 + 26) Lambda^c_f(l_j, M(T_lo(l_j))). By (P3), K_j T_hi(l_j) -> 0 and n^w_{l_j}/K_j -> infinity. So every mate is
window-pinned; Theorem 2.4. QED

Remark 2.10 (what (W^c) means; why it rarely helps). If S_l \ F has sign-mixed room, (W^c) adds nothing new. If S_l is (cofinitely)
contained in F, the room of S_l at scale t comes only from S_l cap F beyond M(t), i.e. r_l^{[M(t)]} <= 2||v_l 1_{S_l, s > M(t)}||_1 =
O(delta_l 2^{-M(t)}), and the window bottom T_lo(l) is super-exponentially small (T_lo(l) = 2^{-n^w_l} T_hi(l)); for a with
geometric decay, M(T_lo(l)) ~ n^w_l ~ l 2^{l^3} Lambda°(l), and the product Lambda^c_f grows like 2^{l M(T_lo(l))}, far beyond
2^{l^3}. So (W^c) holds when a decays so fast on the swallowed signature sets that M(T_lo(l)) = o(l^2) along a subsequence
(a super-fast-decaying class), and fails otherwise. This is the quantitative form of the statement that a support coordinate is a
contact with an allowance 2|a_j|/t: a signature set swallowed by F is APPROXIMATELY swallowed (case (O1)(i)), with a room that decays
as fast as the tail of a. See Part 4.
