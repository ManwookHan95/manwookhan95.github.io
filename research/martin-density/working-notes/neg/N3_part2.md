# N3 Part 2 — Uniformizing the NL mechanism: a positive-scale profile bound at ALL rows, its inheritance, and the
# bank–de-switching inequality

Notation of Part 1.  Throughout this part I = {1} (one block, the norm p_1; a negative answer for ONE N suffices, and
N = 1 is the natural adversarial choice).  Block index dropped: lambda_k = Phi(k) <= 2^{-1-k}, u_k, w, psi := R*w,
alpha(k), sigma, M, C.  Since ||Phi||_2^2 <= sum 4^{-1-k} = 1/12, C <= ||Phi||_2 < 0.29 and M = 1 - C > 0.71 at every row.
For a row f' (NA or not) its data are primed; "j aligned at f'" means z'_j psi'_j > 0.
OSCILLATION: for finite S and h, psi in l_1 put  Osc_S(h; psi) := min_{c real} sum_{j in S} |h_j - c psi_j|.

LEMMA 2.0 (elementary).  PROVED.  (a) |Osc_S(h; psi) - Osc_S(h'; psi)| <= ||(h - h')1_S||_1.
(b) |Osc_S(h; psi) - Osc_S(h; psi')| <= 2 ||h 1_S||_1 ||(psi - psi')1_S||_1 / min(||psi 1_S||_1, ||psi' 1_S||_1).
(c) For S = {s1, s2} with psi != 0 on S: Osc_S(h; psi) = |h_{s1} psi_{s2} - h_{s2} psi_{s1}| / max(|psi_{s1}|, |psi_{s2}|),
    i.e. a multiple of the functional Lambda of [II, prop:II-S3].
Proof.  (a) min of 1-Lipschitz functions.  (b) A minimizer c' for psi' satisfies sum|c' psi'_j| <= sum|h_j - c' psi'_j|
+ sum|h_j| <= 2 sum|h_j|, so |c'| <= 2||h1_S||/||psi'1_S||, and sum|h - c'psi| <= sum|h - c'psi'| + |c'| ||(psi-psi')1_S||;
symmetrize.  (c) The function of c is convex piecewise linear with breakpoints h_{s_i}/psi_{s_i}; evaluate.  QED

## 2.1 Peaks of large weight move together, at every scale

DEFINITION 2.1 (visibility data).  For a row f', a finite set Z of coordinates, a finite set Lambda of peaks of f' and
alpha_0 > 0 with |alpha'(k)| >= alpha_0 (k in Lambda), put for j in Z
   nu_j := sum_{k in Lambda} lambda_k |u_k(j)|,      eta_j := sum_{k notin Lambda} lambda_k |u_k(j)|      (the MISSED weight).
Any finite Lambda is allowed; eta_j -> 0 as Lambda exhausts N, but Lambda must consist of peaks with alpha bounded below.
Z is EXACTLY visible through Lambda if eta_j = 0 on Z (no carrier outside Lambda sees Z — a property of T and Lambda only).

LEMMA 2.2 (collective motion of weighted peaks).  PROVED.  Let f' be any row, g' with g'(xi') = 0, t in (0,1],
e := max_+- p*(f' +- t g') - 1 <= 1/2, and a scale-t pair (Def. 1.1) at f'.  Put L+ := sup_{l in P'} s_l Omega+(l),
L- := inf_{l in P'} s_l Omega-(l), s_l := sgn w'(l).  Then |L+-| <= (2 + e)/t, and for every peak k with alpha'(k) != 0
   Omega+(k) = s_k (L+ - eps+_k),   Omega-(k) = s_k (L- + eps-_k),   0 <= eps+-_k <= e / (t sigma' |alpha'(k)|).
Proof.  From the proof of Lemma 1.2, c' G_b + sigma' G(W+-) <= e, hence sigma' G(W+-) <= e, where W+ = w' + t Omega+ and
W- = w' - t Omega-.  By [I, lem:bookkeeping(c)], G(W) >= |alpha'(k)| (||W||_inf - s_k W(k)) for each peak k.  On peaks
s_k W+(k) = M' + t s_k Omega+(k), so ||W+||_inf >= M' + t L+ and |alpha'(k)| t (L+ - s_k Omega+(k)) <= e/sigma'.  Side -:
s_k W-(k) = M' - t s_k Omega-(k), ||W-||_inf >= M' - t L-, so |alpha'(k)| t (s_k Omega-(k) - L-) <= e/sigma'.  Finally
|L+-| <= ||Omega+-||_inf <= (||w' +- t Omega+-||_inf + ||w'||_inf)/t <= (2 + e)/t.  QED
For g' in C(f'), e <= t^2/2, so eps+-_k <= t/(2 sigma' |alpha'(k)|): peaks of weight >= alpha_0 deviate from the common
level by O(t) only.

## 2.2 The positive-scale profile bound (a quantitative, scale-free version of Cor. S1 at every row)

THEOREM 2.3.  PROVED.  Let f' in S_{p*} be any row (I = {1}), g' in C(f'), j_f a free coordinate of f' (|z'_{j_f}| < 1)
with psi'_{j_f} != 0, and S a finite set, j_f notin S, of coordinates aligned at f' each of which is either a support
coordinate (j in F', z'_j = sgn a'_j) or satisfies |z'_j| >= 1/2 (contact or near-contact).  Let (Lambda, alpha_0, nu, eta)
be visibility data for Z := S u {j_f}.  Put
   mu_S := sum_{j in S n F'} |a'_j|   (bank/support mass on S),   r_f := 1 - |z'_{j_f}|,   rho_S := ||psi' 1_S||_1 / |psi'_{j_f}|,
   A := rho_S/(c' r_f) + 1/c' + (rho_S nu_{j_f} + sum_S nu_j)/(sigma' alpha_0),     H := rho_S eta_{j_f} + sum_S eta_j.
Then for every t in (0, 1]:
   Osc_S(g'; psi')  <=  sum_{j in S} |g'_j - pi(j_f) psi'_j|  <=  A t + (2 mu_S + 15 H)/t,        pi(j_f) := g'_{j_f}/psi'_{j_f}.
Consequently Osc_S(g'; psi') <= 2 (A (2 mu_S + 15 H))^{1/2} if 2 mu_S + 15 H <= A (and <= A + 2 mu_S + 15 H otherwise).
Proof.  Fix t and a scale-t pair.  Block contributions: beta+-_j := (L*Omega+-)(j) = sum_k lambda_k Omega+-(k) u_k(j), so
g'_j = B+-_j + beta+-_j.  By Lemma 2.2, sum_{k in Lambda} lambda_k Omega+-(k) u_k(j) = L+- sum_{Lambda} lambda_k s_k u_k(j)
-+ sum_{Lambda} lambda_k s_k eps+-_k u_k(j); and psi'_j = M' sum_{Lambda} lambda_k s_k u_k(j) + n_j with |n_j| <= eta_j
(|w'| <= 1; w'(k) = s_k M' on peaks).  Hence, with d+- := -L+-/M',
   beta+-_j = -d+- psi'_j + r+-_j,   |r+-_j| <= (|L+-|/M') eta_j + t nu_j/(2 sigma' alpha_0) + ||Omega+-||_inf eta_j
            <= 7.5 eta_j / t + t nu_j/(2 sigma' alpha_0)         (|L+-|, ||Omega+-||_inf <= 2.5/t, M' > 0.71).
Write eps+-_j := |r+-_j|, so B+-_j = g'_j + d+- psi'_j - r+-_j.
 * At j_f: |pi(j_f) + d+-| <= (|B+-_{j_f}| + eps+-_{j_f}) / |psi'_{j_f}|.
 * At j in S, with sigma_j := sgn psi'_j = sgn z'_j: sigma_j (g'_j + d+ psi'_j) >= -(sigma_j B+_j)_- - eps+_j and
   sigma_j (g'_j + d- psi'_j) <= (sigma_j B-_j)_+ + eps-_j; dividing by sigma_j psi'_j = |psi'_j|,
   -d+ - [(sigma_j B+_j)_- + eps+_j]/|psi'_j| <= pi(j) <= -d- + [(sigma_j B-_j)_+ + eps-_j]/|psi'_j|.
Combining, |pi(j) - pi(j_f)| <= (|B+_{j_f}| + |B-_{j_f}| + eps+_{j_f} + eps-_{j_f})/|psi'_{j_f}|
+ [(sigma_j B+_j)_- + (sigma_j B-_j)_+ + eps+_j + eps-_j]/|psi'_j|.  Multiply by |psi'_j| and sum over S:
   sum_S |g'_j - pi(j_f) psi'_j| <= rho_S (|B+_{j_f}| + |B-_{j_f}| + eps+_{j_f} + eps-_{j_f}) + sum_S [(sigma_j B+_j)_- + (sigma_j B-_j)_+ + eps+-_j].
Budget (Lemma 1.2 at f', e <= t^2/2): r_f (|B+_{j_f}| + |B-_{j_f}|) <= 2e/(c' t) <= t/c'.  For j in S \ F',
(sigma_j B_j)_- <= 2(z'_j B_j)_- because |z'_j| >= 1/2; for j in S n F', (z'_j B+_j)_- <= (z'_j B+_j + |a'_j|/t)_- + |a'_j|/t.
Both kinds of terms are parts of the budget (a) [resp. (b)], whose total is <= e/(c' t) <= t/(2c'); so the S-sum of the
B-terms is <= t/c' + 2 mu_S / t.  Insert eps+_j + eps-_j <= 15 eta_j/t + t nu_j/(sigma' alpha_0).  The last claim is the
minimum of A t + K/t over t in (0,1].  QED

COROLLARY 2.4 (profile constancy at every row, all mates, under exact visibility).  PROVED.  If, in Theorem 2.3, Z is
exactly visible (H = 0) and no coordinate of S is a support coordinate (mu_S = 0), then Osc_S(g'; psi') = 0 for EVERY
g' in C(f'): g' is proportional to psi' on S, with the factor pi(j_f).
This holds at non-attaining rows f as well, and it does NOT need two-piece data: it strengthens [II, cor:II-S1] (which
assumes exact two-piece data and j notin Sigma(omega)) by replacing "outside the supports of the used carriers" with the
T-property "seen only by robust peaks".  Proof: let t -> 0 in Theorem 2.3.  QED

## 2.3 Inheritance: the bound never produces a uniform obstruction

COROLLARY 2.5 (uniform lower bound, and its inheritance).  PROVED.  Let f in S_{p*} (I = {1}), g in C(f), rho in (0,1],
j_f in J(f) with psi_{j_f} != 0, S finite aligned at f with S subset F u K, and Lambda a finite set of peaks of f with
|alpha(k)| >= 2 alpha_0.  There is delta > 0 such that for every row f' with p*(f' - f) < delta the hypotheses of
Theorem 2.3 hold at f' (same j_f, S, Lambda, alpha_0; banks on S allowed), with constants A' = A(f') -> A(f) as f' -> f,
and
   dist_{l_1}(rho g, C(f'))  >=  Osc_S(rho g; psi') - 2 (A' (2 mu_S(f') + 15 H))^{1/2}      (when 2 mu_S(f') + 15 H <= A').
But the right side is <= o(1) as f' -> f: indeed Theorem 2.3 at f itself gives Osc_S(g; psi) <= 2(A(f)(2 mu_S(f) + 15H))^{1/2},
and Osc_S(rho g; psi') -> rho Osc_S(g; psi), A' -> A(f), mu_S(f') -> mu_S(f).  So the bound is INHERITED from f: along
every sequence f' -> f it tends to (rho - 1) Osc_S(g; psi) + o(1) <= o(1).
Proof.  Along f' -> f: z' -> z coordinatewise and psi' -> psi in l_1, xi' -> xi weak*, c' -> q_0, sigma' -> sigma, and for
each fixed peak k the margin and alpha'(k) = lambda_k mu'_k / sigma' converge [I, prop:continuity], [I, (eq:margin)].
Hence for f' close to f: j_f is free at f' with r'_f -> r_f, every j in S keeps sgn z'_j = sgn z_j, |z'_j| >= 1/2 or
j in F' (a bank created on a contact of f has sgn a'_j = z'_j = z_j), sgn psi'_j = sgn psi_j, Lambda consists of peaks with
|alpha'| >= alpha_0, psi'_{j_f} != 0.  The displayed inequality is Theorem 2.3 plus Lemma 2.0(a).  The convergence of the
constants is clear; mu_S(f') -> mu_S(f) because a' -> a in l_1.  QED

So a FIXED free coordinate of f can never produce a uniform obstruction: the approximant faces the same linear sandwich as
f, with constants converging to those of f.  A positive lower bound along a sequence f'_n can only come from free
coordinates of f'_n that are NOT free coordinates of f with comparable weight: (b) a contact or support coordinate j of f
made free at f'_n — then r'_n(j) -> 0 for fixed j, so A'_n -> infinity; or (c) j_n -> infinity — then psi'_n(j_n) -> 0, so
rho_S -> infinity and A'_n -> infinity.  In both cases the bound is defeated by banks on S of mass of order 1/A'_n:

THEOREM 2.6 (the profile mechanism is not uniform; sharp "aligned or banked" condition).  PROVED.
 (a) Necessary condition.  Let f'_n -> f be NA rows and g'_n in C(f'_n) with g'_n -> rho g, and let S be aligned at f with
     kappa := Osc_S(rho g; psi) > 0.  Then for all large n and every free coordinate j of f'_n for which Z_j := S u {j}
     satisfies the hypotheses of Theorem 2.3 at f'_n with constants (A_n(j), H(j)) and 2mu_S(f'_n) + 15H(j) <= A_n(j):
        A_n(j) (2 mu_S(f'_n) + 15 H(j)) >= kappa^2/5.
     Under exact visibility (H = 0): mu_S(f'_n) >= kappa^2 / (10 A_n(j)), and A_n(j) <= C (1 + rho_S(j)/r'_n(j)) with
     rho_S(j) = ||psi'_n 1_S||/|psi'_n(j)|: the bank mass on S must dominate the visibility weight |psi'_n(j)| (1 - |z'_n(j)|)
     of EVERY free coordinate j of f'_n, up to the factor kappa^2/(C ||psi 1_S||).  (Quantitative form of "approximants for
     oscillating mates must be aligned or banked", U3 / [II, rem after prop:II-S3].)
 (b) Sufficiency in the data.  Let f have F finite, S subset K u F finite and aligned at f, rho in (0,1], g in C(f), and
     put nu^tot_j := sum_k lambda_k |u_k(j)| (a property of T alone; nu^tot_j -> 0 as j -> infinity, and |psi'_j| <= nu^tot_j
     at EVERY row since |w'| <= 1).
     (b1) [far coordinates]  For every row f' and every free coordinate j of f' with
          8 ||psi' 1_S||_1 mu_S(f') >= c' nu^tot_j Osc_S(rho g; psi')^2  (mu_S(f') = mass of a' on S),
          the lower bound produced by Theorem 2.3 via j is <= 0.  PROVED.
     (b2) [J(f) finite]  If f has only finitely many free coordinates (e.g. the self-aligned rows of [II, rem:II-NL], where
          every coordinate off F is a contact), then for every theta in (0,1] the canonical truncation of f at a depth N
          with banks of mass m_theta := theta on each j in S \ F is an NA row f'_{theta,N} with
          p*(f'_{theta,N} - f) -> 0 as (theta, N) -> (0, infinity), and, for every fixed eps > 0, the supremum over all
          lower bounds produced by Theorem 2.3 at f'_{theta,N} (any free coordinate; visibility data with
          Lambda subset {k : lambda_k >= eps} and alpha_0 := min_Lambda |alpha'(k)|) is <= (rho - 1) Osc_S(g; psi)_+ + o(1).
          PROVED.  (Restricting Lambda to weights >= eps costs nothing essential: a carrier of weight lambda_k has
          |alpha'(k)| = lambda_k mu'_k/sigma' <= lambda_k/sigma', so putting it into Lambda forces alpha_0 <= lambda_k/sigma'
          and inflates A; for fixed eps and finite J(f) the admissible (j, Lambda) with j in J(f) form a finite family, so
          the pointwise inheritance of Corollary 2.5 is uniform over it.)
     (b3) [general f]  The same conclusion for arbitrary f is a SKETCH: it requires inheritance (Corollary 2.5) uniformly
          over the growing finite sets {j in J(f) : nu^tot_j >= theta}, i.e. control of |psi'_j - psi_j| relative to
          |psi_j| there; banks perturb psi by up to O(m log(1/m)) in sup norm (through strict non-peaks seeing j), and a
          coordinate where this perturbation dominates contributes a vacuous bound only when the perturbing carriers enter
          the missed weight eta_j (they do: strict non-peaks are not in Lambda) — the bookkeeping is not carried out here.
Proof.  (a) Theorem 2.3 at f'_n gives Osc_S(g'_n; psi'_n) <= 2(A_n(2mu_S + 15H))^{1/2}, and by Lemma 2.0(a),(b)
Osc_S(g'_n; psi'_n) -> kappa; so 4 A_n (2mu_S + 15H) >= (kappa - o(1))^2 >= 4kappa^2/5 for n large.  The bound on A_n uses
c'_n -> q_0, sigma'_n -> sigma (for the nu-term, bounded by the visibility constant of the fixed set S and of j).
(b1) Whatever the case in Theorem 2.3, the subtracted bound is >= 2(2 A mu_S)^{1/2} (if 2mu_S + 15H > A it is
A + 2mu_S + 15H >= 2(2A mu_S)^{1/2} by AM-GM), and A >= rho_S/(c' r_f) >= ||psi'1_S||/(c' |psi'_j|) >= ||psi'1_S||/(c' nu^tot_j).
So the subtracted bound is >= Osc_S(rho g; psi') under the displayed inequality.
(b2) Let J(f) = {j_1, ..., j_r}.  The truncation keeps z on [1, N] (N >= max J(f)), so the free coordinates of f' are
J(f) (with the rooms of f) and (N, infinity) (room 1).  By N1 Lemma 1.4 (uniform far freedom) p*(f' - f) -> 0.  Far
coordinates j > N: nu^tot_j <= tau(N) := sup_{i > N} nu^tot_i -> 0, so (b1) applies as soon as
8 ||psi'1_S|| theta |S \ F| >= c' tau(N) Osc_S(rho g; psi')^2 — true for N large given theta (if S \ F is empty, i.e.
S subset F, banks are the support masses of f and the inequality reads 8||psi'1_S|| mu_S(f) >= c' tau(N) Osc^2, again true
for N large).  The finitely many j in J(f): Corollary 2.5 at each of them (data of f' converge to those of f as
theta -> 0, N -> infinity), giving <= (rho - 1) Osc_S(g; psi) + o(1) when Theorem 2.3 applies at f via j, and a vacuous
or o(1) bound otherwise: if psi_j = 0 and eta_j = 0 then psi'_j = (M'/M) psi_j = 0 (fact below) and Theorem 2.3 does not
apply via j; if psi_j = 0 and eta_j > 0, the subtracted term is >= 2 (15 A' H)^{1/2} >= 2 rho'_S (15 eta_j/(c' r_j))^{1/2} with
rho'_S = ||psi'1_S||/|psi'_j| -> infinity (psi'_j -> psi_j = 0), so the bound via j is vacuous for f' close to f.  QED
Fact used in (b2): if only peaks of f' see j (eta_j = 0 for some Lambda of peaks of both f and f' with equal signs), then
psi'_j = M' sum_Lambda lambda_k s_k u_k(j) = (M'/M) psi_j: visible values of psi are inherited exactly up to the factor M'/M.
In the main case S subset K (mu_S(f) = 0) with exact visibility, Theorem 2.3 at f shows that Osc_S(g; psi) > 0 forces f to
have no free coordinate j with psi_j != 0 satisfying its hypotheses: the inherited part of (b2) is then void.

READING.  The NL mechanism is a positive-scale LINEAR SANDWICH (Theorem 2.3) that every mate at every row obeys.  It is
inherited from f by any approximant that copies f's one-sided structure (contacts and support) on the window where psi is
large, and banks S with mass of order (visibility weight of its free coordinates); such approximants exist in every
neighbourhood (Theorem 2.6(b)).  Theorem NL is the special case of approximants that are neither aligned nor banked: they
have a visible free coordinate with |psi'| (1 - |z'|) bounded below and no banks on S.  Part (a) is sharp up to constants
for the engineered approximants of [I, thm:engineered] (Part 3).

## 2.4 The bank–de-switching inequality (what banks must pay at NA rows)

THEOREM 2.7 (bank–de-switching inequality).  PROVED.  Let f' have F' u K' finite (e.g. NA), I = {1}, S aligned at f' as in
Theorem 2.3 (no free coordinate is needed), and visibility data (Lambda, alpha_0, nu, eta) for S.  For g' in C(f'), t in
(0,1] and every scale-t pair with ||Delta Omega||_{V*} <= M:
   Osc_S(g'; psi') <= (1/2) omega_{f'}(M, t/c') + A_S t + (2 mu_S + 22.5 H_S)/t,
   A_S := 1/c' + (3/2) sum_S nu_j/(sigma' alpha_0),   H_S := sum_S eta_j,
with omega_{f'} the de-switching modulus of Definition 1.3 (omega_{f'}(M, r) -> 0 as r -> 0 by Theorem 1.4).
Proof.  As in Theorem 2.3, for j in S: -d+ - e+_j <= pi(j) <= -d- + e-_j with e+_j := [(sigma_j B+_j)_- + eps+_j]/|psi'_j|,
e-_j := [(sigma_j B-_j)_+ + eps-_j]/|psi'_j|.  With c := -(d+ + d-)/2: |pi(j) - c| <= (d+ - d-)_+/2 + e+_j + e-_j.  On S the
switching vector is V_j = B+_j - B-_j = beta-_j - beta+_j = (d+ - d-) psi'_j + r-_j - r+_j, so
(d+ - d-)_+ ||psi'1_S||_1 <= ||V 1_S||_1 + sum_S (eps+_j + eps-_j).  Hence
Osc_S(g'; psi') <= ||V||_1/2 + sum_S [(sigma_j B+_j)_- + (sigma_j B-_j)_+] + (3/2) sum_S (eps+_j + eps-_j), and the middle sum is
<= t/c' + 2 mu_S/t (budget), the last <= (3/2)(15 H_S/t + t sum_S nu_j/(sigma' alpha_0)).  Finally ||V||_1 <=
omega_{f'}(M, t/c') by Theorem 1.4(b) (e <= t^2/2).  QED

COROLLARY 2.8 (dichotomy at NA rows).  PROVED.  In the setting of Theorem 2.7 with exact visibility (H_S = 0), if
Osc_S(g'; psi') = kappa' > 0 then for every scale t in (0, kappa'/(4 A_S)] at least one of the following holds:
 (i) mu_S >= kappa' t / 8 (the banks on S carry the oscillation at scale t); or
 (ii) every scale-t pair of g' has ||Delta Omega||_{V*} > M_t, where M_t := sup{M : omega_{f'}(M, t/c') <= kappa'}
      (the switching at scale t runs through large block coefficients — by Corollary 1.5, through deep carriers).
Since omega_{f'}(M, r) -> 0 as r -> 0 for each M, M_t -> infinity as t -> 0: below the de-switching scale of f', bounded
switching cannot carry the oscillation, and either the banks pay mu_S >~ kappa' t or the carriers become deep.
Proof.  If (ii) fails, some pair has ||Delta Omega|| <= M_t and Theorem 2.7 gives kappa' <= kappa'/2 + kappa'/4 + 2mu_S/t. QED

## 2.5 Persistent bounded switching at f is an exact resonance; escape is controlled by the tails of T

PROPOSITION 2.9 (exact resonances as limits).  PROVED.  Let f in S_{p*} (any K), g in C(f), t_n -> 0+, and scale-t_n pairs
at f with ||Delta Omega_n||_{V*} <= M and ||V_n||_1 >= c > 0.  Then a subsequence of Delta Omega_n converges weak* to some
Delta with ||Delta|| <= M, V_inf := L* Delta != 0, V_inf = 0 on J, z_j V_inf(j) >= 0 on K: an exact one-sided transfer
(exact resonance) of f, with bounded coefficients.
Proof.  As in Theorem 1.4: V_n -> V_inf in l_1 (compactness of L*), ||V_inf|| >= c; Lemma 1.2(c) gives
sum_J (1 - |z_j|)|V_n(j)| + sum_K 2 (z_j V_n(j))_- <= t_n/q_0 -> 0.  QED
So bounded-coefficient switching that persists to t -> 0 at f is carried by an exact resonance V_inf, and the canonical
truncations at depth N support it with leakage ||V_inf 1_{K n (N, inf)}||_1 (Remark 1.6(c)): their de-switching scale
tends to 0, and Corollary 2.8(i) can be met with mu_S ~ kappa t^*(N) -> 0.  This is exactly the mechanism of
[I, thm:engineered] (window masses ~ 4 rho s_1 |b^theta|, cut-off N'' with V_{>N''} <= delta s_1/(16 rho)).

LEMMA 2.10 (tail control of the switching extent).  PROVED.  For every row f, g in C(f), t in (0,1], every scale-t pair
and every N:
   ||V 1_{(N, inf)}||_1 <= (5/t) frak_t(N),     frak_t(N) := sum_{k,m} lambda_{k,m} ||u_{k,m} 1_{(N, inf)}||_1  ( -> 0 ).
Proof.  V = L*(Delta Omega) = sum lambda_{k,m} Delta Omega(k,m) u_{k,m} and |Delta Omega(k,m)| <= (4 + 2e)/t <= 5/t. QED
Consequence: at scale t, a truncation at any N with frak_t(N) <= delta t^2/5 loses at most switching mass delta t, whose
first-order cost is <= delta t^2.  Switching can therefore never "escape to infinity" faster than the tails of T allow:
an escape-rate obstruction against truncation-type approximants (switching at depth D(t) -> infinity too fast as t -> 0)
does NOT exist; the requirement is exactly the cut-off condition [I, (N1)] frak(N'') <= s_1^2 of the engineered
construction, with N'' chosen after the junction scale s_1.

## Summary of Part 2
(1) The NL mechanism has a quantitative, scale-free form valid for ALL mates at ALL rows (Theorem 2.3, Corollary 2.4);
it implies "aligned or banked" with a sharp quantitative threshold (Theorem 2.6(a)).
(2) It is INHERITED from f (Corollary 2.5) and DEFEATED in every neighbourhood of f by truncation + banks of mass of
order (visibility weight of the approximant's free coordinates) (Theorem 2.6(b)): PROVED when f has finitely many free
coordinates (this includes the self-aligned rows where Theorem NL is realized), SKETCH in general (uniform inheritance over
growing finite sets of free coordinates of f).  So no profile/oscillation functional of NL type gives a uniform
non-density certificate at such rows, for ANY admissible T and any S.
(3) At NA rows banks must pay mu_S >~ kappa * (de-switching scale) unless the switching runs through deep carriers
(Corollary 2.8); persistent bounded switching at f is an exact resonance (Prop. 2.9), which truncations carry down to an
arbitrarily small de-switching scale; escape of switching is controlled by T's tails (Lemma 2.10).  None of these
constraints obstructs: they are all met, with matching constants, by the engineered approximants (Part 3).
