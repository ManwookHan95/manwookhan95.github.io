# G3 notes — a designed admissible T for which every first row with "signature room" is recovered; reduction of density to one base-side lemma

Round 3, task G3. Setting: canonical base q; Martin's norm with a FINITE block set I_N = {1..N} (the norms p_N, every N >= 1; Preprint B
Remark martin-tail reduces density for p to density for all p_N). T is DESIGNED (only Lemma B's conclusion is required of T by Martin's
proof of algebraic triviality; our T satisfies it, 1.3). Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Part files: ctx/r3/G3_part1.md ..
G3_part6.md (assembled below). Imports (refereed, Rounds 1-2): A Facts A-F, A Lemmas 4.3, 4.4, 4.7, 7.1, 7.2, A Prop 2.1, the proof of A Thm 6.8;
C (7.2), C (7.3), C Thm 7.4 (and C Cor 7.2(c)).

## 0. Answer and summary
**The full theorem (density for some admissible T and every p_N) is reduced to ONE explicitly stated lemma about the base side (Lemma Z),
which is in fact equivalent to density for the designed T. Everything else -- in particular the four open-core items O1-O4 -- is PROVED for
the designed T at every first row f in the dense class R_0.**

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Theorem A: the "signature-ladder design" (SLD) T is admissible (norm one, injective, Ran T cap c_00 = {0}, each block dense in S_{q*}); private signatures delta_l h_l on disjoint S_l, coarse-to-fine allowedness of targets, one ladder through all blocks, super-fast weights with long windows of scales | PROVED | 1.2-1.3 |
| 2 | Class R_0 := {F = supp a finite and (SR): ||h_l 1_{S_l cap J_gamma}|| >= vartheta^l ||h_l|| for all l}; contains all NA points and all base-tame points; allows infinite contact sets, near-contacts, arbitrary blocks | PROVED (definitions/inclusions) | 1.1, 1.4 |
| 3 | Two-sided decompositions: uniform smallness, first-order terms O(t), one-sided base bounds, weighted budget Gamma_w <= 1 + o(1), sup-level parametrization of blocks | PROVED (any admissible T) | 2.1-2.5 |
| 4 | Signature pinning: delta'_l |Delta c_l| <= E_l + sum_{l'>l} kappa |Delta c_{l'}|; triangular solution; sum |Delta c| <= K_1 Lambda_f(l_*) t on window scales; contact/near-contact switching and uniform shifts pinned | PROVED | 3.1-3.5 |
| 5 | Window certificate: on every window scale a balanced finite certificate c_t with radius ~ t, ||g - g_{c_t}|| <= K_2 Lambda_f t, Gamma_w(c_t) <= 1 + o(1); one-sided excesses bounded by two-sided differences | PROVED | 4.1-4.2 |
| 6 | Uniform transfer expansion: p*(f + s g_c) <= 1 + (s^2/2)(Gamma_w(c) + eps) for |s| <= c_1 t, uniformly over window-type certificates (C Thm 7.4 at f, made uniform) | PROVED | 5.1 |
| 7 | Windowed averaging: certificates on ONE window of n >= C K dyadic scales suffice; recovery via C Thm 7.4 | PROVED | 5.2 |
| 8 | **Theorem B: for the SLD T and every N, R_0 is contained in R (every mate of every f in R_0 is recovered)** | PROVED | 5.3 |
| 9 | Corollary: for f in R_0, C(f) = closure of the Gamma_w <= 1 balanced finite certificates in C(f) (no intrinsic defect) | PROVED | 6.4 |
| 10 | **Theorem C: for the SLD T, density of NA((c_0,p_N), l_2^2) <=> Lemma Z** | PROVED | 5.4 |
| 11 | **Lemma Z: every (f, rho g) is approximated by (f', g') with f' in R_0, g' in C(f')** (base-side engineering only; approximants need not be NA) | OPEN (the single missing lemma) | 1.1, 6.3 |
| 12 | Lemma Z for mates covered by Round-2 engineering (exact two-piece mates under their hypotheses) | PROVED (by import) | 6.3(a) |
| 13 | Extension of Theorem B to infinite base support F (with (SR)) | SKETCH | 6.3(e) |
| 14 | Finitely many unpinned carriers = exact-resonance structure up to O(K t) on windows; route to Lemma Z there | HEURISTIC / OPEN | 6.3(d) |
| 15 | Density for Martin's own (unknown) T | not addressed (OPEN) | 6.1 |

Key ideas. (1) PINNING: if every block vector u_l carries a private signature delta_l h_l on coordinates where the first row has room,
then for ANY two admissible decompositions of a mate (the two sides of t = 0) the difference of the coefficient of u_l is controlled by
base mass on its signature, which costs first order and is O(t) (3.2). Contacts, near-contacts, peaks and near-threshold carriers are
one-sided resources, and every one-sided usage is bounded by a two-sided difference (2.3(b), 4.2(c)), hence pinned. (2) WINDOWS: the price
of pinning (1/delta' per level, amplified triangularly by finer targets touching coarser signatures) is a constant Lambda_f(l_*) that
depends only on the coarse levels; a super-fast ladder of weights creates windows of scales in which the finer carriers are negligible and
which contain >> Lambda_f(l_*) dyadic scales. (3) A's averaging over scales needs certificates only on one window of n dyadic scales.
(4) The budget identity controls exactly C's mass-weighted invariant Gamma_w, and transfer peaks (C Thm 7.4) realise it uniformly, so no
second-order rebalancing problem remains. (5) Since NA points lie in R_0, the remaining problem (Lemma Z) is equivalent to density and
concerns only first rows whose base one-sided resources swallow signature sets (P1's exact resonance is of this type) or whose base
support is infinite.

Leaning: positive (density). No counterexample is suggested by anything here; Theorem B removes every block-side mechanism of the open core.
# G3 part 1: setting, statements, and the designed operator T ("signature-ladder design", SLD)

## 1.0 Setting and imports
Canonical base q (q*(a) = ||a||_1 + ||U*a||, U: H -> c_0 compact, dense range, U* injective), Martin's norm with a FINITE block
set I_N = {1,...,N} (the norms p_N; Preprint B Remark martin-tail: density for all p_N gives density for p). Every statement
below is for an arbitrary fixed N >= 1, p := p_N. Notation of A_notes §1: for a carrier (k,m), Phi_m(k) = 2^{-m-k} q*(T e_{k,m}),
lambda_{k,m} = m Phi_m(k), u_{k,m} = T e_{k,m}/q*(T e_{k,m}), (R_m x)(k) = lambda_{k,m} u_{k,m}(x), R_m* omega = sum_k lambda_{k,m} omega(k) u_{k,m},
N_m(w) = ||w||_inf + ||D_m w||_2, (D_m w)(k) = Phi_m(k) w(k), s(t) := sqrt(1+t^2).
For f in S_{p*}: normer xi, q_0 = q**(xi), zhat = xi/q_0 = z + U e, forced decomposition f = a + L*w (w = (w_m)), F := supp a,
nu := ||U*a||, zeta_m := R_m** xi, sigma_m := |zeta_m|_m (so q_0 + sum_m sigma_m = 1), M_m, C_m, alpha_m, peak set P_m, strict non-peaks
Q_m, gap_m(k) = M_m - |w_m(k)| (A Fact C). C(f) = mates; Ls(f) := {g : (f, rho g) in cl NA((c_0,p), l_2^2) for all rho < 1}; R := {f :
Ls(f) = C(f)}; density iff R = S_{p*} (A Prop 2.1, N_part1 Thm 1).
Imports (all refereed, Rounds 1-2): A Facts A-F (A_notes 1.2-1.7), A Lemma 4.3 (base expansion), A Lemma 4.4 (block expansion),
A Lemma 4.7 (slack), A Lemma 7.1 (budget), A Lemma 7.2 (exact excess formulas), A Thm 6.8 (its proof is re-run in 5.2), C Thm 7.4
(recovery of balanced finite certificates with Gamma_w <= 1 along canonical truncations; C_referee: PROVED) and the identity (7.3)
of its proof, A Prop 2.1 (R1). Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.1 Main results (summary; proofs in parts 2-5)
* **Theorem A (PROVED).** There is an admissible T (Lemma B's conclusion: norm one, injective, Y := Ran T dense operator range with
  Y cap c_00 = {0}, hence NA(q) cap Y = {0}; for every m the normalized vectors u_{k,m}, k in N, are dense in S_{q*}) with the
  additional structure (SLD): one ladder l <-> (k,m) through all blocks, private signatures u_l = (y_l + delta_l h_l)/n_l on pairwise
  disjoint infinite coordinate sets S_l, coarse-to-fine allowedness of the targets y_l in c_00, and super-fast weights c_l creating
  long "windows" of scales. (1.2-1.3.)
* **Definition (class R_0).** f in S_{p*} is in R_0 if (i) F = supp a is finite, and (ii) (SR) "signature room": there are
  gamma in (0,1) and vartheta in (0,1] with ||h_l 1_{S_l cap J_gamma}||_1 >= vartheta^l ||h_l||_1 for every ladder index l of a block
  m <= N, where J_gamma := {j notin F : |z_j| <= 1 - gamma}.
  R_0 contains every norm-attaining f and every "base-tame" f (F finite, finite contact set K, sup_{j notin F cup K} |z_j| < 1);
  contact sets K may be INFINITE and near-contacts may occur in R_0, as long as the signature sets keep room (1.4).
* **Theorem B (main, PROVED).** For the SLD operator T and every N: R_0 is contained in R. I.e. for every f in R_0, every
  g in C(f) and every rho < 1, (f, rho g) lies in the closure of NA((c_0,p_N), l_2^2). (Proof: parts 2-5.)
  No condition on the blocks of f is needed: infinitely many strict non-peaks, near-threshold carriers, weak/degenerate peaks,
  failure of margin sparsity, several active blocks, cross-block relations and second-order base/block rebalancing are all
  allowed. Mechanism: at every f in R_0 the signatures PIN all coarse block coefficients of all admissible decompositions on the two
  sides of t = 0 (up to O(t) times a window constant); in the long windows of scales created by the super-fast ladder the fine
  carriers are negligible; so every mate is, on a whole window of n dyadic scales, a balanced finite certificate + O(K t) with
  n >> K; the weighted invariant Gamma_w (not max(h,H)) is controlled by the exact budget identity; transfer peaks (C Thm 7.4) give
  the matching uniform second-order expansion; a windowed version of A's averaging theorem then puts rho g in the closure of the
  Gamma_w-certificates, which C Thm 7.4 recovers.
* **Theorem C (reduction; PROVED).** For the SLD operator T, NA((c_0,p_N), l_2^2) is dense iff the following holds:
  **Lemma Z (OPEN).** For every f in S_{p_N*}, g in C(f), rho < 1, eps > 0 there is f' in R_0 with p*(f' - f) < eps and
  dist(rho g, C(f')) < eps.
  (Lemma Z is implied by -- and much weaker than -- the NA-engineering statement studied in Rounds 1-2, because NA points lie in
  R_0; conversely Theorem B shows that only the BASE side and the signature coordinates have to be engineered.) The open core is
  thereby confined to first rows f outside R_0: infinite base support F, or "signature-resonant" f whose contact/near-contact/support
  set swallows (a vartheta^l-fraction of) the signature sets (this is exactly where P1's exact resonance lives).

## 1.2 Construction of T (SLD)
Fix once and for all:
 (D0) a bijection iota: N x N -> N, l = iota(k,m), with iota(k,m) < iota(k',m) for k < k'; write (k(l), m(l)) := iota^{-1}(l);
      a coordinate j_0 and pairwise disjoint infinite sets S_l contained in N \ {j_0} (l in N), and h_l := sum_{s in S_l} 2^{-s} e_s* (>= 0);
      delta_l := min{2^{-l}, (4(1 + ||U||) ||h_l||_1)^{-1}} (so q*(delta_l h_l) <= (1+||U||) delta_l ||h_l||_1 <= 1/4);
      targets (y^(i))_{i >= 1} contained in c_00 cap S_{q*}, dense in S_{q*}, with y^(1) := e_{j_0}*/q*(e_{j_0}*); a sequence (i_r)_{r>=1} of positive
      integers in which every positive integer occurs infinitely often.
 (D1) Recursion over l = 1, 2, 3, ... . Given c_l in (0,1] (c_1 := 1), call a target y in c_00 ALLOWED at l if
        (a) supp y cap S_{l'} = empty for every l' >= l, and
        (b) 2 c_l <= 2^{-2s} c_{l'} delta_{l'} for every l' < l and every s in supp y cap S_{l'}.
      (y^(1) is allowed at every l: its support {j_0} meets no S_{l'}.) Let y_l := y^(i_{k(l)}) if this target is allowed at l, else
      y_l := y^(1). Put
        n_l := q*(y_l + delta_l h_l),   u_l := (y_l + delta_l h_l)/n_l,   delta°_l := delta_l ||h_l||_1 / n_l  (signature mass of u_l),
        Lambda°(l) := prod_{l'' <= l} (1 + 2/delta°_{l''}),
        T_hi(l) := min{T_lo(l-1), 2^{-l^3} / (l Lambda°(l))}  (T_lo(0) := 1),   n^w_l := ceil(l 2^{l^3} Lambda°(l)),   T_lo(l) := 2^{-n^w_l} T_hi(l),
        c_{l+1} := min{c_l/4, T_lo(l)^3}.
 (D2) T e_{k,m} := c_{iota(k,m)} u_{iota(k,m)}, extended linearly to l_1(N x N).
So u_{k,m} = u_{iota(k,m)}, q*(T e_{k,m}) = c_l, Phi_{m(l)}(k(l)) = 2^{-m-k} c_l and lambda_l := lambda_{k(l),m(l)} = m 2^{-m-k} c_l <= c_l/2.
The interval W(l) := [T_lo(l), T_hi(l)] is the l-th WINDOW; it contains n^w_l dyadic scales. (The exponents 2^{l^3} are slack
that absorbs the f-dependent constant vartheta^{-l^2} of (SR) and every f-, g-, rho-dependent constant; see 5.3.)

## 1.3 Theorem A. PROVED.
T is admissible, and:
 (P1) u_l = (y_l + delta_l h_l)/n_l with y_l in c_00, ||y_l||_1 <= q*(y_l) = 1, n_l in [3/4, 5/4], supp y_l cap S_{l'} = empty for all l' >= l;
      the signature supports S_l are pairwise disjoint; u_l(s) = delta_l 2^{-s}/n_l + 0 for s in S_l, i.e. on S_l only u_l itself and the
      targets y_{l'} of FINER indices l' > l can be nonzero.
 (P2) sum_{l' > l} c_{l'} <= 2 c_{l+1} <= 2 T_lo(l)^3 and sum_{l'>l} lambda_{l'} <= c_{l+1} <= T_lo(l)^3.
 (P3) Windows: T_hi(l) 2^{l^3} Lambda°(l) <= 1/l, log_2(T_hi(l)/T_lo(l)) = n^w_l >= l 2^{l^3} Lambda°(l), T_hi(l+1) <= T_lo(l).
*Proof.* (P1)-(P3) are immediate from (D0)-(D2): n_l = q*(y_l + delta_l h_l) lies within q*(delta_l h_l) <= 1/4 of q*(y_l) = 1;
||y||_1 <= q*(y); (a) gives the support statement; c_{l'+1} <= c_{l'}/4 gives sum_{l'>l} c_{l'} <= (4/3) c_{l+1} <= 2 c_{l+1}.
Norm one: q*(T e_{k,m}) = c_l <= 1 = c_1 and T is the l_1-extension, so ||T|| = 1.
Density in each block. Fix m and y^(i). Since supp y^(i) is finite it meets only finitely many S_{l'} and, c_l -> 0, conditions (a), (b)
hold at all large l; i occurs infinitely often in (i_r), so y_l = y^(i) for infinitely many l = iota(k,m). Along these, delta_l -> 0 and
n_l -> 1, so ||u_l - y^(i)||_1 -> 0 (also in q*). Hence every y^(i) is a limit of u_{k,m} (k -> infinity), and the dense set {y^(i)} lies in
the closure of {u_{k,m} : k in N} (indeed of every tail).
Injectivity and Ran T cap c_00 = {0} (P1 2.1's argument). Let x in l_1 (indexed by l) with Z := sum_l x_l c_l u_l in c_00 and suppose x_{l'} != 0.
For s in S_{l'}: by (P1), u_l(s) = 0 for l < l' and for l = l' except the signature, so
   Z(s) = x_{l'} c_{l'} delta_{l'} 2^{-s}/n_{l'} + sum_{l > l', s in supp y_l} x_l c_l y_l(s)/n_l.
If the second sum is non-empty let L(s) be its smallest index; by (b) at L(s), 2 c_{L(s)} <= 2^{-2s} c_{l'} delta_{l'}; the sum is bounded by
(4/3)||x||_inf sum_{l >= L(s)} c_l <= (8/3)||x||_inf c_{L(s)} <= (4/3) ||x||_inf 2^{-2s} c_{l'} delta_{l'}. Hence
|Z(s)| >= c_{l'} delta_{l'} 2^{-s} ( |x_{l'}|/n_{l'} - (4/3)||x||_inf 2^{-s} ) > 0 for all large s in S_{l'}, contradicting Z in c_00. So x = 0:
T is injective (take Z = 0) and Ran T cap c_00 = {0}. Y := Ran T is the range of a bounded operator, dense (it contains the u's), and
NA(q) cap Y = c_00 cap Y = {0}. QED.

Remark 1.3.1 (what is and is not used later). Theorem B uses exactly: Lemma B's conclusion (through the imports), (P1) (signature
privacy and coarse-to-fine allowedness), (P2) (fine tails) and (P3) (long windows). It does NOT use any rate of approximation of the
targets, any relation between delta_l and lambda_l, any independence among the targets, or any property of the targets beyond
y_l in c_00, ||y_l||_1 <= 1. Martin's built-in cross-block near-duplicates are compatible with SLD (the same target sequence may be used in
every block); they are harmless because every carrier has its own signature.

## 1.4 The class R_0. PROVED facts.
Definition as in 1.1. For l with S_l cap J_gamma of positive h_l-mass put delta'_l := ||(u_l) 1_{S_l cap J_gamma}||_1 = delta_l ||h_l 1_{S_l cap J_gamma}||_1 / n_l;
(SR) says delta'_l >= vartheta^l delta°_l.
 (a) Every NA f' in S_{p*} is in R_0. Indeed F' = supp a' is finite (A Fact D) and z' is in c_0, so the set of j notin F' with
     |z'_j| > 1/2 is finite; choose gamma < 1/2 smaller than 1 - |z'_j| for each of these j with |z'_j| < 1. Then N \ J_gamma = F' cup K' is finite
     (K' = contacts), so S_l is contained in J_gamma for all but finitely many l, and for the finitely many others ||h_l 1_{S_l cap J_gamma}|| > 0
     (S_l is infinite, F' cup K' finite); take vartheta := min over these l of (ratio)^{1/l} > 0.
 (b) Every base-tame f (F finite, K finite, sup_{j notin F cup K} |z_j| < 1) is in R_0: same argument with gamma := 1 - sup |z_j|.
 (c) R_0 allows infinite contact sets, near-contacts (|z_j| -> 1 along infinitely many j) and arbitrary block structure; it excludes F
     infinite and the "signature-resonant" f for which the non-roomy set F cup {j : |z_j| > 1 - gamma} contains, for every gamma, all
     but a vartheta^l-fraction of the h_l-mass of some (or of a fast sequence of) signature sets. Example outside R_0: P1's f
     (its contact set is the signature set S_{l_0}) -- consistent with P1's nonempty intrinsic defect.
# G3 part 2: two-sided decompositions at a fixed first row (valid for ANY admissible T)

Throughout this part f in S_{p*} (p = p_N) and g in C(f) are fixed; T is any admissible operator. h(B) := ||P_{e-perp} U*B||^2/nu and
H_m(Omega) := ||P_m-perp D_m Omega||_2^2 / C_m, P_m-perp the orthogonal projection of l_2 onto (D_m w_m)-perp. For a pair (B, Omega) put
  Gamma_w(B, Omega) := q_0 h(B) + sum_m sigma_m H_m(Omega_m).
sqrt(Gamma_w) is a seminorm on l_1 x prod_m l_inf (each term is the square of a seminorm, with positive weights).

## 2.1 Lemma (two-sided decompositions). PROVED.
For every t > 0 there are B_+, B_- in l_1 and Omega_+ = (Omega_{+,m}), Omega_- = (Omega_{-,m}) in prod_{m <= N} l_inf with
  q*(a + t B_+) <= s(t),  N_m(w_m + t Omega_{+,m}) <= s(t),  q*(a - t B_-) <= s(t),  N_m(w_m - t Omega_{-,m}) <= s(t)  (all m),
  g = B_+ + L*Omega_+ = B_- + L*Omega_-.
(A "two-sided decomposition of g at scale t".)
*Proof.* A Fact A gives f + t g = A + L*W with max(q*(A), ||W||_{V*}) = p*(f + t g) <= s(t) (g in C(f)); put B_+ := (A - a)/t,
Omega_+ := (W - w)/t; subtracting f = a + L*w gives t B_+ + t L*Omega_+ = t g. Same with -t. QED.

## 2.2 Lemma (uniform smallness). PROVED.
For every eta > 0 there is t_eta > 0 such that every two-sided decomposition at any scale t in (0, t_eta] satisfies, for both signs and
every block m:  ||t B_+-||_1 <= eta,  ||D_m(t Omega_{+-,m})||_2 <= eta,  | ||w_m +- t Omega_{+-,m}||_inf - M_m | <= eta.
*Proof.* If not, there are t_n -> 0 and decompositions violating one inequality (say on the + side; the - side is identical). Put
A_n := a + t_n B_{+,n}, W_n := w + t_n Omega_{+,n}. They are bounded (q*, N_m <= s(t_n) <= 2), so along a subsequence A_n -> A weak* in l_1
and W_{n,m} -> W_m weak* in l_inf. L* is weak*-weak* continuous and A_n + L*W_n = f + t_n g -> f, so A + L*W = f, with q*(A) <= 1 and
N_m(W_m) <= 1 (weak* lower semicontinuity of dual norms). By uniqueness of the forced decomposition (A Fact B), A = a and W = w.
U* is weak*-to-norm continuous on bounded sets (U compact), so ||U*A_n|| -> nu and ||A_n||_1 = q*(A_n) - ||U*A_n|| <= s(t_n) - ||U*A_n|| -> 1 - nu
= ||a||_1. For a bounded coordinatewise convergent sequence in l_1 this gives ||A_n - a||_1 -> 0 (for a finite G, ||(A_n - a)1_G|| -> 0 and
limsup ||A_n 1_{G^c}|| <= ||a||_1 - ||a 1_G||_1). D_m: l_inf -> l_2 is compact (Phi_m in l_2), hence D_m W_n -> D_m w in l_2, i.e.
||D_m(t_n Omega_n)|| -> 0 and ||D_m W_n|| -> C_m; then ||W_n||_inf <= s(t_n) - ||D_m W_n|| -> M_m while liminf ||W_n||_inf >= M_m (weak* lsc).
All three quantities tend to 0, a contradiction. QED.

## 2.3 Lemma (first-order terms, budget, one-sided base bounds, weighted second order). PROVED.
Let t <= t_eta with eta <= eta_* := min(nu/(2||U|| + 2), min_m C_m)/2. Then for both signs:
 (a) |q_0 B_+-(zhat)| <= t/2 and |<Omega_{+-,m}, zeta_m>| <= t/2 for every m.
 (b) Sum_{j notin F} (|B_+(j)| - z_j B_+(j)) <= t/(2 q_0) and sum_{j notin F} (|B_-(j)| + z_j B_-(j)) <= t/(2 q_0). Consequently
     sum_{j in J_gamma} |B_+-(j)| <= t/(2 gamma q_0) for every gamma in (0,1), and
     ||B_+ 1_{F^c}||_1 + ||B_- 1_{F^c}||_1 <= ||(B_+ - B_-) 1_{F^c}||_1 + t/q_0.
 (c) sum_{k in P_m} |alpha_{m,k}| ( ||w_m + t Omega_{+,m}||_inf - sigma_k (w_m + t Omega_{+,m})(k) ) <= t^2/(2 sigma_m), and the same for
     W_- := w - t Omega_-.
 (d) Gamma_w(B_+-, Omega_+-) <= 1 + eta_Gamma(eta),  eta_Gamma(eta) := (1 + ||U|| eta/nu) max_m (1 + eta/C_m) - 1  (-> 0 as eta -> 0).
*Proof.* (a) q**(zhat) = 1, so q*(A) >= A(zhat): 1 + t B_+(zhat) <= s(t), i.e. q_0 B_+(zhat) <= q_0 t/2. By Fact C,
N_m(W) >= <W, zeta_m>/sigma_m = 1 + t<Omega_{+,m}, zeta_m>/sigma_m, so <Omega_{+,m}, zeta_m> <= sigma_m t/2. Evaluating g = B_+ + sum R_m* Omega_{+,m}
at xi = q_0 zhat gives q_0 B_+(zhat) + sum_m <Omega_{+,m}, zeta_m> = g(xi) = 0 (A Remark 2.3). The weights q_0, sigma_m sum to 1, so each term,
being <= (its weight) t/2 while the sum is 0, is >= -t/2. The - side: 1 - t B_-(zhat) <= s(t) and 1 - t<Omega_-, zeta>/sigma <= s(t),
with the same sum identity.
(b) By A Lemma 7.1, q_0 E_q(a + tB_+) + sum_m sigma_m e_m(W_{+,m}) <= s(t) - 1 <= t^2/2 with E_q, e_m >= 0, and by A Lemma 7.2
E_q(a + tB) >= sum_{j notin F} (|tB_j| - z_j t B_j). For the - side apply the same to a + (-t)B_-. On J_gamma, |x| -+ z x >= gamma |x|.
The last inequality: for |z| <= 1 and reals x, y, |x| + |y| <= |x - y| + (|x| - z x) + (|y| + z y), because the difference of the two sides
is |x - y| - z(x - y) >= 0; sum over j notin F.
(c) A Lemma 7.2 (block formula; all terms >= 0) and the budget: sigma_m e_m(W_{+,m}) <= t^2/2.
(d) A Lemma 4.3: E_q(a + tB) >= nu Psi(t U*B/nu) >= (t^2/2) h(B)/(1 + t||U*B||/nu) when t||U*B||/nu <= 1/2 (true: t||B||_1 <= eta <= eta_*).
A Lemma 7.2: e_m(W) >= t^2 ||P-perp D Omega||^2 / (||D W|| + <D W, D w>/C) and the denominator is <= 2||DW|| <= 2(C_m + eta) by 2.2.
Insert both in the budget and divide by t^2/2. QED.

## 2.4 Lemma (sup-level parametrization of a block). PROVED.
Fix m (dropped from the notation) and t <= t_eta, eta <= eta_*. Define d_+, d_- by
  ||w + t Omega_+||_inf = (1 - d_+ t) M,   ||w - t Omega_-||_inf = (1 + d_- t) M,   and   omega_+- := Omega_+- + d_+- w.
Then:
 (a) |d_+-| t <= eta/M; in particular 1 - d_+ t >= 1/2 and 1 + d_- t >= 1/2 for eta <= M/2.
 (b) (box) for every k: |(1 - d_+ t) w(k) + t omega_+(k)| <= (1 - d_+ t) M and |(1 + d_- t) w(k) - t omega_-(k)| <= (1 + d_- t) M.
 (c) (peaks) for k in P, sigma_k := sign w(k): sigma_k omega_+(k) <= 0 <= sigma_k omega_-(k), and sum_{k in P} |alpha_k| |omega_+-(k)| <= t/(2 sigma_m).
 (d) |d(omega_+-) - d_+-| <= t/sigma_m, where d(omega) := <D w, D omega>/C.
 (e) |t Omega_+-(k)| <= 3 for all k, and |d_+-| <= (3 ||Phi_m||_2 / t + t/sigma_m)/M.
 (f) (non-peaks) for k in Q with gap g_k and sigma_k := sign w(k) (any sign if w(k) = 0):
     sigma_k omega_+(k) <= (1 - d_+ t) g_k / t   and   sigma_k omega_-(k) >= -(1 + d_- t) g_k / t.
*Proof.* (a) is 2.2. (b): w + tOmega_+ = (1 - d_+t) w + t omega_+ and w - tOmega_- = (1 + d_-t) w - t omega_-; each coordinate is bounded by the
sup norm. (c): at a peak, |(1 - d_+t) sigma_k M + t omega_+(k)| <= (1 - d_+t) M forces sigma_k t omega_+(k) <= 0, and then
||W_+||_inf - sigma_k W_+(k) = t|omega_+(k)|; insert in 2.3(c). The - side is symmetric (sigma_k omega_-(k) >= 0, ||W_-||_inf - sigma_k W_-(k) =
t|omega_-(k)|). (d): by Fact C, zeta/sigma_m = alpha + D^2 w/C, so <Omega_+, zeta>/sigma_m = <omega_+ - d_+ w, alpha> + <D(omega_+ - d_+ w), Dw>/C
= -sum_P |alpha_k||omega_+(k)| - d_+ M + d(omega_+) - d_+ C, i.e. d(omega_+) - d_+ = <Omega_+, zeta>/sigma_m + sum_P |alpha_k||omega_+(k)|; use 2.3(a)
and (c). For the - side, <Omega_-, zeta>/sigma_m = sum_P |alpha_k||omega_-(k)| + d(omega_-) - d_-. (e): |t Omega(k)| <= |W(k)| + |w(k)| <= s(t) + 1 <= 3;
d(omega) - d = <Dw, D Omega>/C + dC - d = <Dw, D Omega>/C - dM, so |d| M <= ||D Omega||_2 + |d(omega) - d| <= 3||Phi||_2/t + t/sigma_m.
(f): multiply the box inequality of (b) by sigma_k: on the + side (1 - d_+t)(M - g_k) + sigma_k t omega_+(k) <= (1 - d_+t) M; on the - side
(1 + d_-t)(M - g_k) - sigma_k t omega_-(k) <= (1 + d_-t) M. QED.

## 2.5 Lemma (base part on a finite support). PROVED.
If F is finite there is C_F < infinity with ||beta||_1 <= C_F ( ||P_{e-perp} U* beta|| + |beta(zhat)| ) for every beta supported in F.
*Proof.* On the finite-dimensional space l_1(F) the linear map beta -> (P_{e-perp} U* beta, beta(zhat)) is injective: if P_{e-perp} U* beta = 0 then
U* beta = mu e = (mu/nu) U* a, so beta = (mu/nu) a (U* injective), and beta(zhat) = mu/nu a(zhat) = mu/nu; if this also vanishes, beta = 0. QED.
Consequence (for t <= t_eta, eta <= eta_*): beta := B_+ 1_F satisfies
  ||B_+ 1_F||_1 <= C_F ( sqrt(nu h(B_+)) + ||U|| ||B_+ 1_{F^c}||_1 + t/(2 q_0) + ||zhat||_inf ||B_+ 1_{F^c}||_1 ),
using P_{e-perp} U* B_+ 1_F = P_{e-perp} U* B_+ - P_{e-perp} U* B_+ 1_{F^c}, 2.3(a) and beta(zhat) = B_+(zhat) - (B_+ 1_{F^c})(zhat). With 2.3(d),
h(B_+) <= 2/q_0, so ||B_+ 1_F||_1 <= K_F (1 + ||B_+ 1_{F^c}||_1) with K_F depending only on f.
# G3 part 3: signature pinning of block coefficients (uses SLD and (SR))

Standing in this part: T is the SLD operator of 1.2; f in R_0 with constants gamma, vartheta (1.1); g in C(f); eta <= eta_* and t <= t_eta
(part 2); a two-sided decomposition (B_+-, Omega_+-) of g at scale t (2.1). Ladder indices l with m(l) > N play no role (their carriers are
absent from L); all sums over l below run over {l : m(l) <= N}. Put
  c^+-_l := lambda_l Omega_{+-, m(l)}(k(l))   (so L*Omega_+- = sum_l c^+-_l u_l, absolutely convergent in l_1),
  Delta c_l := c^+_l - c^-_l,   Delta B := B_+ - B_- = - sum_l Delta c_l u_l   (both pairs represent g).
For a window index l_* let Cset := {l <= l_*} (coarse) and Fset := {l > l_*} (fine). delta'_l := delta_l ||h_l 1_{S_l cap J_gamma}||_1 / n_l >=
vartheta^l delta°_l > 0 by (SR) and (P1).

## 3.1 Lemma (box bound). PROVED.  |c^+-_l| <= 3 lambda_l / t for every l.
*Proof.* 2.4(e): |t Omega_+-(k)| <= 3. QED.

## 3.2 Lemma (pinning inequality). PROVED.
For every l:  delta'_l |Delta c_l| <= E_l + sum_{l' > l} kappa_{l', l} |Delta c_{l'}|,  where E_l := ||Delta B 1_{S_l cap J_gamma}||_1 and
kappa_{l', l} := ||y_{l'} 1_{S_l}||_1 / n_{l'}. Moreover kappa_{l',l} <= 4/3 and sum_l kappa_{l',l} <= 4/3 for every l'.
*Proof.* Let s in S_l. By (P1): u_{l'}(s) = 0 for l' < l (their targets avoid S_l, their signatures live on S_{l'}); u_l(s) = delta_l 2^{-s}/n_l
(y_l avoids S_l); u_{l'}(s) = y_{l'}(s)/n_{l'} for l' > l. Hence for s in S_l,
  -Delta B(s) = Delta c_l delta_l 2^{-s}/n_l + sum_{l' > l} Delta c_{l'} y_{l'}(s)/n_{l'}.
Take the l_1-norm over s in S_l cap J_gamma and use the triangle inequality; the left side is <= E_l and the first term on the right has norm
|Delta c_l| delta'_l. kappa_{l',l} <= ||y_{l'}||_1/n_{l'} <= 4/3, and the S_l are disjoint. QED.

## 3.3 Lemma (solution of the triangular system). PROVED.
  sum_{l in Cset} |Delta c_l| <= Lambda_f(l_*) [ sum_{l in Cset} E_l + (4/3) sum_{l' in Fset} |Delta c_{l'}| ],
  Lambda_f(l_*) := prod_{l <= l_*} (1 + 2/delta'_l) <= vartheta^{-l_*^2} Lambda°(l_*).
*Proof.* For l in Cset put D_l := |Delta c_l|, X_l := E_l + sum_{l' in Fset} kappa_{l',l} D_{l'} and S_l := sum_{l' in Cset, l' >= l} D_{l'} (S := 0 past l_*).
By 3.2, D_l <= (X_l + (4/3) S_{l+1})/delta'_l, hence S_l <= X_l/delta'_l + (1 + 4/(3 delta'_l)) S_{l+1}. Unrolling from l_* downwards,
S_1 <= sum_{l in Cset} (X_l/delta'_l) prod_{l'' < l} (1 + 4/(3 delta'_{l''})) <= (sum_l X_l) prod_{l'' <= l_*} (1 + 2/delta'_{l''}),
and sum_{l in Cset} X_l <= sum E_l + (4/3) sum_{Fset} D_{l'} by 3.2. Finally 1 + 2/delta'_l <= 1 + 2 vartheta^{-l}/delta°_l <= vartheta^{-l}(1 + 2/delta°_l)
and sum_{l <= l_*} l <= l_*^2. QED.

## 3.4 Lemma (total coefficient defect in a window). PROVED.
If t in W(l_*) and t <= min(t_eta, 1), then
  sum_l |Delta c_l| <= K_1 Lambda_f(l_*) t,   K_1 := 1/(gamma q_0) + 14.
*Proof.* sum_l E_l <= sum_{j in J_gamma} (|B_+(j)| + |B_-(j)|) <= t/(gamma q_0) (2.3(b); the S_l are disjoint). By 3.1 and (P2),
sum_{Fset} |Delta c_{l'}| <= 6 sum_{l' > l_*} lambda_{l'}/t <= 6 c_{l_*+1}/t <= 6 T_lo(l_*)^3/t <= 6 t^2. With 3.3:
sum_l |Delta c_l| <= Lambda_f (t/(gamma q_0) + 8 t^2) + 6 t^2 <= Lambda_f t (1/(gamma q_0) + 14). QED.

## 3.5 Corollary (what pinning controls). PROVED. Same hypotheses as 3.4; K := K_1 Lambda_f(l_*).
 (a) ||Delta B||_1 = ||sum_l Delta c_l u_l||_1 <= sum_l |Delta c_l| <= K t   (||u_l||_1 <= q*(u_l) = 1).
 (b) Base mass off the support: ||B_+ 1_{F^c}||_1 + ||B_- 1_{F^c}||_1 <= K t + t/q_0   (2.3(b) and (a)).
     In particular the total mass that the two decompositions put on CONTACTS and NEAR-CONTACTS (one-sided base resources, possibly
     infinitely many) is O(K t): contact switching is pinned by the block signatures.
 (c) Uniform shifts: for every block m, |Delta d_m| := |d_{+,m} - d_{-,m}| <= (Phi^max_m/(m C_m)) sum_{l : m(l) = m} |Delta c_l| + 2t/(sigma_m M_m) <= K_d K t,
     K_d := max_m (1/(m C_m) + 2/(sigma_m M_m)) (Phi^max_m := max_k Phi_m(k) <= 1).
*Proof of (c).* Put Delta Omega := Omega_+ - Omega_- and Delta omega := omega_+ - omega_- = Delta Omega + Delta d w. By 2.4(d),
Delta d = d(Delta omega) + r with |r| <= 2t/sigma_m, and d(Delta omega) = <Dw, D Delta Omega>/C + Delta d C. Hence Delta d M = <Dw, D Delta Omega>/C + r.
Since lambda_k = m Phi_k, <Dw, D Delta Omega> = sum_k Phi_k^2 w(k) Delta Omega(k) = (1/m) sum_k Phi_k w(k) Delta c_k, of modulus <= (M Phi^max/m) sum_k |Delta c_k|.
Divide by M. QED.

## 3.6 Remark (why this is the heart of the matter).
3.2-3.5 hold for ANY two decompositions of g (two sides, or two scales). They say: on every f in R_0 the block content of a mate is
determined, carrier by carrier, by the mate itself up to the base mass that the decompositions put on the roomy part of the signature sets,
which costs first order and is therefore O(t). This is exactly what fails at P1's example (the signature set of the resonant carrier is a
contact set: the signature can be carried for free on one side, and the carrier coefficient is not pinned). The price of pinning is the
factor 1/delta' per level and the triangular amplification Lambda_f(l_*) (coarse-to-fine contamination of signature sets by finer
targets, which cannot be avoided because targets must approximate vectors supported on signature sets); the windows of the SLD design are
long enough to absorb it (part 5).
# G3 part 4: extraction of a balanced finite certificate on every window scale

Standing: as in part 3 (SLD operator, f in R_0, g in C(f), window index l_*, t in W(l_*), t <= min(t_eta, 1), eta <= eta_1 :=
min(eta_*, min_m M_m/2), a two-sided decomposition at scale t). K := K_1 Lambda_f(l_*) (3.4). We also assume K t <= 1 (true in the windows
used later: K T_hi(l_*) -> 0, see 5.3). "Coarse coordinates" of block m: Cset_m := {k : iota(k,m) <= l_*}; fine: the others.
Constants written K_b, K_2, K_4, C' depend only on f, gamma, N (not on g, t, l_*).

## 4.1 Definition (the window certificate c_t).
 * Base: kappa_t := (B_+ 1_F)(zhat), b_t := B_+ 1_F - kappa_t a.
 * Block m: for k in Cset_m cap Q_m with g_k := gap_m(k) >= t^2 put omega^c_m(k) := clamp(omega_{+,m}(k); [-2 g_k/t, 2 g_k/t]); put omega^c_m(k) := 0 at all
   other k (peaks, coarse non-peaks with gap < t^2, fine coordinates). Here omega_+ = Omega_+ + d_+ w (2.4).
 * c_t := (b_t, (omega^c_m)_m), g_{c_t} := b_t + sum_m R_m*(omega^c_m - d(omega^c_m) w_m), d(omega) := <D_m w_m, D_m omega>/C_m.

## 4.2 Proposition (window certificate). PROVED.
 (a) c_t is a balanced finite certificate in the sense of C Def 7.0 (supp b_t in F, b_t(xi) = 0, omega^c_m finitely supported in Q_m), with
     gap_m(k) >= t^2 and |omega^c_m(k)| <= 2 gap_m(k)/t on supp omega^c_m, ||D_m omega^c_m||_2 <= 2/t and |d(omega^c_m)| <= 2/t.
 (b) ||b_t||_1 <= K_b.
 (c) (remainder) ||g - g_{c_t}||_1 <= K_2 Lambda_f(l_*) t.
 (d) (weighted coefficient) sqrt(Gamma_w(c_t)) <= sqrt(1 + eta_Gamma(eta)) + K_4 Lambda_f(l_*) t, where Gamma_w(c) := q_0 h(b) + sum_m sigma_m H_m(omega_m)
     is C's mass-weighted coefficient (C Def 7.0; H_m(omega - d(omega) w) = H_m(omega)).
*Proof.* (a) b_t(zhat) = kappa_t - kappa_t a(zhat) = 0, and xi = q_0 zhat. The coarse set is finite. The bounds on omega^c are the clamp;
||D omega^c||_2 <= (2/t)||Phi_m||_2 <= 2/t, and |d(omega)| <= ||D omega||_2 ||D w||_2 / C = ||D omega||_2.
(b) |kappa_t| <= |B_+(zhat)| + ||zhat||_inf ||B_+ 1_{F^c}||_1 <= t/(2q_0) + (1 + ||U||)(K t + t/q_0) by 2.3(a), 3.5(b); and ||B_+ 1_F||_1 <= K_F(1 + Kt + t/q_0)
by 2.5. Use K t <= 1, t <= 1.
(c) g - g_{c_t} = (B_+ - b_t) + sum_m R_m* X_m with X_m := Omega_{+,m} - omega^c_m + d(omega^c_m) w_m. Base: B_+ - b_t = B_+ 1_{F^c} + kappa_t a, so
||B_+ - b_t||_1 <= (2 + ||U||)(K t + t/q_0) + t/(2q_0) (||a||_1 <= 1). Block m (index dropped): with Omega_+ = omega_+ - d_+ w and 1_C, 1_F the
indicators of coarse and fine coordinates,
   X = [ (omega_+ - omega^c) 1_C - (d_+ - d(omega^c)) w 1_C ] + [ Omega_+ 1_F + d(omega^c) w 1_F ],
and ||R* x||_1 <= sum_k lambda_k |x(k)|.
 Fine part: sum_F lambda_k |Omega_+(k)| = sum_{Fset} |c^+_l| <= 3 sum_{l > l_*} lambda_l / t <= 3 t^2 (3.1, (P2), t >= T_lo(l_*)), and
 |d(omega^c)| sum_F lambda_k |w(k)| <= (2/t) c_{l_*+1} <= 2 t^2.
 Coarse excess: rho_k := |omega_+(k) - omega^c(k)|. CLAIM: lambda_k rho_k <= |Delta c_k| + lambda_k |Delta d| M + 2 t lambda_k for every coarse k, where
 Delta c_k := lambda_k (Omega_+(k) - Omega_-(k)), so that lambda_k |omega_+(k) - omega_-(k)| <= |Delta c_k| + lambda_k |Delta d| M.
  - Peak k: omega^c(k) = 0 and, by 2.4(c), omega_+(k) and omega_-(k) have opposite signs (weakly), so rho_k = |omega_+(k)| <= |omega_+(k) - omega_-(k)|.
  - Non-peak k (gap g_k > 0), if |omega_+(k)| > 2 g_k/t: by 2.4(f) and |d_+ t| <= 1, sigma_k omega_+(k) <= 2 g_k/t, so sigma_k omega_+(k) < -2 g_k/t and the
    clamp excess is e_k := -sigma_k omega_+(k) - 2 g_k/t > 0; by 2.4(f) and |d_- t| <= 1, sigma_k omega_-(k) >= -2 g_k/t, hence
    sigma_k(omega_-(k) - omega_+(k)) >= e_k: the part of omega_+(k) beyond the clamp is ONE-SIDED and is bounded by the two-sided difference.
    If g_k >= t^2 then rho_k = e_k (or 0); if g_k < t^2 then omega^c(k) = 0 and rho_k <= 2 g_k/t + e_k <= 2t + |omega_+(k) - omega_-(k)|.
 Summing, with sum_k lambda_k <= 1, 3.4 and 3.5(c): sum_C lambda_k rho_k <= K t + K_d K t M + 2t.
 d-difference: |d_+ - d(omega^c)| <= |d_+ - d(omega_+)| + |d(omega_+ - omega^c)| <= t/sigma_m + sum_k Phi_k |omega_+(k) - omega^c(k)|
 (|d(x)| <= ||Dx||_2 <= ||Dx||_1), and sum_k Phi_k |...| <= (1/m) sum_C lambda_k rho_k + sum_F Phi_k (|Omega_+(k)| + |d_+| M)
 <= (1/m) sum_C lambda_k rho_k + 3t^2 + (3/t + 1/sigma_m) t^3 (2.4(e), (P2)). Multiply by sum_C lambda_k |w(k)| <= 1.
 Collecting terms, ||g - g_{c_t}||_1 <= C'(K t + t) <= K_2 Lambda_f(l_*) t (Lambda_f >= 1).
(d) sqrt(Gamma_w) is a seminorm on pairs (base vector, block vectors) (part 2), and H_m vanishes on multiples of w_m, so
sqrt(Gamma_w(c_t)) <= sqrt(Gamma_w(B_+, Omega_+)) + sqrt(Gamma_w(B_+ - b_t, (omega_+ - omega^c)_m)). The first term is <= sqrt(1 + eta_Gamma(eta)) (2.3(d)).
For the second: q_0 h(x) <= ||U||^2 ||x||_1^2/nu and sigma_m H_m(x) <= ||D x||_2^2/C_m <= (sum_k Phi_k |x(k)|)^2/C_m; both were bounded by C'(K t + t) in (c). QED.

## 4.3 Remarks.
 (i) Nothing about the blocks of f was assumed: Q_m may be infinite, peaks may be degenerate or weak, (MS) may fail, several blocks may be
     active, contact sets may be infinite. All one-sided resources (peaks, coordinates pushed beyond 2 gap/t, contacts, near-contacts) enter
     only through the two-sided differences |Delta c_k|, ||Delta B||, which are pinned (part 3).
 (ii) The certificate is built from the + side only; the - side is used solely to bound the one-sided excess of the + side.
 (iii) Gamma_w, not Gamma_max = max(h, H_m), is the controlled quantity: the first-order terms of base and blocks are individually only O(t)
     (2.3(a)), so each piece separately can exceed the s(t)-level at second order (this is the second-order rebalancing of the open core
     item O2); the budget identity controls exactly the mass-weighted sum. Part 5 therefore uses transfer peaks (C Thm 7.4).
# G3 part 5: uniform transfer expansion, windowed averaging, proofs of Theorems B and C

## 5.1 Lemma (uniform transfer expansion at f). PROVED. (Any admissible T.)
Let f in S_{p*} with F finite. For every eps_tr > 0 and A_0 >= 1 there are c_1 in (0, 1/8] and t_1 > 0 such that for every t in (0, t_1] and every
balanced finite certificate c = (b, (omega_m)) at f (C Def 7.0) with
  (C-a) ||b||_1 <= A_0 and Gamma_w(c) <= 2;  (C-b) supp omega_m subset {k in Q_m : gap_m(k) >= t^2} and |omega_m(k)| <= 2 gap_m(k)/t,
we have  p*(f + s g_c) <= 1 + (s^2/2)(Gamma_w(c) + eps_tr)  for all |s| <= c_1 t.
*Proof.* This is C Thm 7.4, Steps 1-4, run at f itself ("N = infinity", C Cor 7.2(c)) with constants made uniform over the class (C-a), (C-b).
Step 0 (transfer peaks; they depend on f and eps_tr only). For each block m put pihat_m := R_m*(sgn(w_m) 1_{P_m}) in l_1 and tau_m := pihat_m(zhat) a - pihat_m
(so tau_m(zhat) = 0). For delta_0, delta_1 > 0 let T^dn := tau_m + delta_0 q*(tau_m) a and T^up := -tau_m + delta_0 q*(tau_m) a (if tau_m = 0 take T := delta_0 a);
T(zhat) > 0. By density of every tail of (u_{k,m})_k choose k_* = k_*^{m,dn}, k_*^{m,up} with q*(u_{k_*,m} - T/q*(T)) <= delta_1 so deep that k_* is a peak
of sign +1 with positive margin mu_* := u_{k_*,m}(xi) - theta_m Phi_m(k_*) (theta_m := M_m sigma_m/(m C_m)): indeed u_{k_*}(zhat) >= T(zhat)/q*(T) - delta_1 > 0
(|v(zhat)| <= q*(v) as q**(zhat) = 1) while Phi_m(k_*) -> 0 (Fact C). Put lambda_* := q*(T), Phi_* := Phi_m(k_*) and, for t > 0,
  Lset_t := {k : |w_m(k)| >= M_m - t^2/2} (contains P_m),  y_t := sgn(w_m) 1_{Lset_t} +- (lambda_*/(m Phi_*)) e_{k_*}  (+ for dn, - for up),
  beta_t := (R_m* y_t)(zhat),  e_t := R_m* y_t - beta_t a (so e_t(zhat) = 0),  e_{y,t} := 1 + <D w, D y_t>/C.
Facts. (T1) q_0 beta_t = sigma_m e_{y,t} +- lambda_* mu_* (C (7.3) at f): from zeta = sigma_m(alpha + D^2 w/C), <sgn(w) 1_{Lset_t}, alpha> = sum_P |alpha_k| = 1, and
sigma_m |alpha_{k_*}| = m Phi_* mu_* (Fact C at the peak k_*). (T2) q*(e_t) <= 2 lambda_* delta_1 + 2(1 + ||U||) sum_{k in Lset_t \ P} lambda_k: at t = 0 (Lset = P),
e_0 = +-[(lambda_* u_{k_*} - T) + (T(zhat) - lambda_* u_{k_*}(zhat)) a] (C Step 1), and y_t - y_0 = sgn(w) 1_{Lset_t \ P}. The sum tends to 0 as t -> 0
(dominated convergence; the sets Lset_t \ P decrease to the empty set). (T3) lambda_* mu_* <= q_0 (T(zhat) + lambda_* delta_1) = q_0(delta_0 q*(tau) + lambda_* delta_1).
(T4) For k_* deep, e_{y,t} in [1/2, Y_1] with Y_1 independent of t, and Y_0 := sup_t ||D y_t||_2 < infinity.
Choose delta_0, then delta_1, then t_1, so that eps_1 := max_{m, dn/up} sup_{t <= t_1} (lambda_* mu_*/q_0 + q*(e_t)) <= eps_tr/(16 N (2 + 2/sigma_min)).
Step 1 (equalisation parameters). Let c satisfy (C-a), (C-b); Gamma := Gamma_w(c), h := h(b) <= 2/q_0, H_m := H_m(omega_m) <= 2/sigma_m, d_m := d(omega_m),
|d_m| <= ||D omega_m||_2 <= 2/t. For each m use the dn-peak if H_m >= Gamma and the up-peak otherwise, and put tau_m := (H_m - Gamma)/(2 e_{y,m,t}),
eps_m := tau_m s^2; |tau_m| <= tau_max := 2 + 2/sigma_min, and tau_m(+-lambda_* mu_*) = |tau_m| lambda_* mu_* >= 0 in both cases.
Step 2 (decomposition). A(s) := a + s b + sum_m eps_m R_m* y_m and W_m(s) := w_m + s(omega_m - d_m w_m) - eps_m y_m satisfy A(s) + sum_m R_m* W_m(s) = f + s g_c,
so p*(f + s g_c) <= max(q*(A(s)), max_m N_m(W_m(s))) (A Fact A).
Step 3 (block sup norm). Let |s| <= c_1 t with c_1 <= 1/8 and c_1^2 tau_max <= 1/8, and t_1 so small that t^2 (2 + lambda_*/(m Phi_*)) <= M_m for all m.
Then |s d| <= 1/4 and |eps| <= t^2/8, and ||W(s)||_inf = (1 - s d) M - eps:
 (i) k in Lset_t, k != k_*: omega(k) = 0 (supp omega has gap >= t^2), W(k) = sgn(w(k))((1 - sd)|w(k)| - eps), and (1 - sd)|w(k)| >= |eps|; equality at peaks.
 (ii) k = k_*: W(k_*) = (1 - sd) M - eps(1 +- lambda_*/(m Phi_*)) lies in [-((1 - sd)M - eps), (1 - sd)M - eps] (dn: eps >= 0; up: eps < 0; the
     choice of t_1).
 (iii) k notin Lset_t cup supp omega: |W(k)| = (1 - sd)|w(k)| <= (1 - sd)(M - t^2/2) <= (1 - sd) M - eps.
 (iv) k in supp omega (gap g >= t^2): |W(k)| <= (1 - sd)(M - g) + |s| 2g/t <= (1 - sd) M - g(3/4 - 2c_1) <= (1 - sd)M - t^2/2 <= (1 - sd)M - eps.
Step 4 (block Hilbert part). D W = D w + h, h := -s d D w + s D omega - eps D y, ||h|| <= 4 c_1 + Y_0 t^2 <= C_min/2 (c_1 <= C_min/16, t_1 small).
By C (7.2), ||Dw + h|| <= C + <Dw, h>/C + ||P-perp h||^2/(2(C - ||h||)), with <Dw, h>/C = s d M - eps(e_y - 1) and
||P-perp h||^2 <= (1 + th) s^2 C H + (1 + 1/th) eps^2 Y_0^2 (th > 0 to be chosen). Since eps e_y = s^2 (H - Gamma)/2,
  N(W(s)) <= 1 + (s^2/2) Gamma + (s^2/2) H [(1 + th)(1 + 2||h||/C) - 1] + (1 + 1/th) tau_max^2 Y_0^2 s^4/C.
Step 5 (base). With E := sum_m eps_m beta_m, A(s) = (1 + E) a + s b + sum_m eps_m e_m, so q*(A(s)) <= (1 + E) q*(a + s' b) + sum_m |eps_m| q*(e_m),
s' := s/(1 + E). A Lemma 4.3 (b(zhat) = 0, supp b in F finite, ||b/a||_inf <= A_0/min_F |a_j|, ||U*b|| <= ||U|| A_0) gives, for |s| <= c_1 t_1 small,
q*(a + s'b) <= 1 + (s'^2/2) h (1 + 2|s'| ||U|| A_0/nu). By (T1) and Step 1, sum_m tau_m sigma_m e_{y,m}/q_0 = sum_m sigma_m (H_m - Gamma)/(2 q_0) = (Gamma - h)/2
(sum_m sigma_m H_m = Gamma - q_0 h, sum_m sigma_m = 1 - q_0), hence E = (s^2/2)(Gamma - h) + s^2 sum_m |tau_m| lambda_* mu_*/q_0 and
  q*(A(s)) <= 1 + (s^2/2) Gamma + (s^2/2) h [ (1 + 2|s'| ||U|| A_0/nu)/(1 + E) - 1 ] + s^2 N tau_max eps_1.
Step 6. Choose th, then c_1 and t_1, so small that every bracket times its bounded coefficient (H <= 2/sigma_min, h <= 2/q_0, |E| <= 4 s^2 + s^2 N tau_max eps_1)
plus the s^4 term is <= (s^2/2) eps_tr/2, and recall s^2 N tau_max eps_1 <= (s^2/2) eps_tr/8. QED.

## 5.2 Theorem (windowed averaging over scales). PROVED.
Let f in S_{p*} with F finite, g in C(f), rho in (0,1), and eta_0 > 0 with rho^2(1 + eta_0) <= (1 + rho^2)/2. Suppose there are c_1 in (0,1] and a sequence of
triples (t^(j), n_j, K_j) with t^(j) -> 0, n_j >= 24 rho^2 K_j/(c_1(1 - rho^2)) and K_j t^(j)/n_j -> 0 such that for every j and every t in
{t^(j) 2^{1-i} : i = 1, ..., n_j} there is a balanced finite certificate c_t at f with
 (i) p*(f + s g_{c_t}) <= 1 + (s^2/2)(1 + eta_0) for |s| <= c_1 t;  (ii) p*(g - g_{c_t}) <= K_j t;  (iii) Gamma_w(c_t) <= 1 + eta_0.
Then (f, rho' rho g) is in cl NA((c_0,p), l_2^2) for every rho' < 1.
*Proof.* A Thm 6.8's proof, with the expansion (A) replaced by (i), the n certificates taken only on ONE window of n_j dyadic scales, and
the final recovery by C Thm 7.4. Fix s_0 in (0,1] with s_0^2 <= 1 - rho^2 and j so large that c_1 t^(j) <= rho s_0 and 2 rho K_j t^(j)/n_j <= (1 - rho^2) s_0/3.
Write n = n_j, K = K_j, t_i := t^(j) 2^{1-i}, c := (1/n) sum_i c_{t_i} (a balanced finite certificate; g_c = (1/n) sum_i g_{c_{t_i}}).
(A) if rho|s| <= c_1 t_i: p*(f + s rho g_{c_{t_i}}) <= 1 + (rho^2 s^2/2)(1 + eta_0) by (i);
(B) always: p*(f + s rho g_{c_{t_i}}) <= p*(f + s rho g) + rho|s| K t_i <= s(rho s) + rho|s| K t_i (g in C(f), (ii)).
By convexity p*(f + s rho g_c) <= (1/n) sum_i p*(f + s rho g_{c_{t_i}}).
|s| <= s_0: with I_f := {i : c_1 t_i < rho|s|}, sum_{I_f} t_i < 2 rho|s|/c_1 (geometric), so p*(f + s rho g_c) <= max{1 + (rho^2 s^2/2)(1 + eta_0), s(rho s)} + Q s^2,
Q := 2 rho^2 K/(c_1 n) <= (1 - rho^2)/12; and 1 + (rho^2 s^2/2)(1 + eta_0) + Q s^2 <= 1 + (s^2/2)(1 - (1 - rho^2)/3) <= 1 + s^2/2 - s^4/8 <= s(s)
(s^2 <= 1 - rho^2), while s(rho s) + Q s^2 <= s(s) by A Lemma 4.7.
|s| >= s_0: all i use (B): p*(f + s rho g_c) <= s(rho s) + 2 rho K t^(j)|s|/n <= s(rho s) + (1 - rho^2) s_0 |s|/3 <= s(s) (A Lemma 4.7).
Hence rho g_c is in C(f). Gamma_w is a convex quadratic form, so Gamma_w(rho c) <= rho^2 (1 + eta_0) <= 1. C Thm 7.4 (a in c_00, (f, rho g_c) contractive,
rho g_c a balanced finite certificate with Gamma_w <= 1) gives (f, rho' rho g_c) in cl NA for all rho' < 1. Finally
p*(rho g_c - rho g) <= (rho/n) sum_i K t_i <= 2 rho K t^(j)/n -> 0 (j -> infinity), and cl NA is closed. QED.

## 5.3 Proof of Theorem B. PROVED.
Fix N, the SLD operator T, f in R_0 (constants gamma, vartheta), g in C(f) and rho in (0,1). Choose eta_0 with rho^2(1 + eta_0) <= (1 + rho^2)/2,
eps_tr := eta_0/2, A_0 := K_b + 1 (4.2(b)), and c_1, t_1 from 5.1. Choose eta <= eta_1 with sqrt(1 + eta_Gamma(eta)) <= sqrt(1 + eta_0/2) - 1/100 (possible
since eta_Gamma(eta) -> 0), and put t_* := min(t_eta, t_1, 1).
For a window index l put t^(l) := T_hi(l), n_l := n^w_l, K_l := (1 + ||U||) K_2 Lambda_f(l) (p* <= q* <= (1 + ||U||)||.||_1). The n_l scales
t_i = T_hi(l) 2^{1-i} lie in W(l) (t_{n_l} = 2 T_lo(l)). By 3.3 and (P3),
  Lambda_f(l) T_hi(l) <= vartheta^{-l^2} Lambda°(l) T_hi(l) <= vartheta^{-l^2} 2^{-l^3}/l -> 0   (l -> infinity).
Hence for all large l and every window scale t: t <= t_*, K t <= 1 (part 4), K_4 Lambda_f(l) t <= 1/100, so by 4.2 the window certificate c_t satisfies
(C-a) (||b_t|| <= K_b <= A_0, Gamma_w(c_t) <= 1 + eta_0/2 <= 2) and (C-b); by 5.1, p*(f + s g_{c_t}) <= 1 + (s^2/2)(1 + eta_0) for |s| <= c_1 t; and
p*(g - g_{c_t}) <= K_l t. The window conditions of 5.2 hold for l large:
  n_l >= l 2^{l^3} Lambda°(l) >= 24 rho^2 (1 + ||U||) K_2 vartheta^{-l^2} Lambda°(l)/(c_1(1 - rho^2)) = 24 rho^2 K_l/(c_1(1 - rho^2))
(because l 2^{l^3} vartheta^{l^2} -> infinity), and K_l t^(l)/n_l <= (1 + ||U||) K_2 vartheta^{-l^2} 2^{-l^3}/l -> 0. Theorem 5.2 gives
(f, rho' rho g) in cl NA for all rho, rho' < 1, i.e. g in Ls(f). As g in C(f) was arbitrary, f is in R. QED.

## 5.4 Proof of Theorem C. PROVED.
(<=) Let f in S_{p*}, g in C(f), rho < 1, eps > 0. Lemma Z gives f' in R_0 and g' in C(f') with p*(f' - f) < eps, p*(g' - rho g) < eps. By Theorem B,
(f', rho' g') is in cl NA for every rho' < 1; letting eps -> 0 and rho' -> 1, (f, rho g) is in cl NA. By A Prop 2.1 (R1) NA((c_0,p), l_2^2) is dense.
(=>) Assume density; let f, g in C(f), rho < 1, eps > 0. S_0 := (f, rho g) has norm 1 (g in C(f) and rho < 1). Take S in NA with ||S - S_0|| < eps', attaining
its norm at x in S_p, and replace x by -x if necessary. Since (f, g) is contractive, f(x)^2 + g(x)^2 <= 1, while f(x)^2 + rho^2 g(x)^2 = ||S_0 x||^2 >= (1 - 2eps')^2;
hence |g(x)| <= 2 (eps'/(1 - rho^2))^{1/2} and |f(x)| >= 1 - 2 eps' - ..., so v := Sx/||Sx|| is within o(1) of +-e_1 as eps' -> 0. Let Q be the rotation of
l_2^2 with Q v = e_1 (Q -> identity) and S' := QS/||S|| = (f', g'). Then f'(x) = 1, g'(x) = 0, ||S'|| = 1, so f' in S_{p*} attains its norm, g' in C(f')
(A Prop 2.1), and (f', g') -> (f, rho g) as eps' -> 0. NA points belong to R_0 (1.4(a)). So Lemma Z holds. QED.
# G3 part 6: which properties of T are used where; the open core after G3; the missing lemma

## 6.1 Use of the design (Remark 1.3.1 made precise)
| Ingredient | Property of T used | Where |
|---|---|---|
| forced decomposition, uniform smallness, budget, first-order terms | Lemma B only (T1)-(T4) | 2.1-2.5 |
| pinning inequality | (P1): private signatures on disjoint S_l; targets of index l avoid S_{l'} for l' >= l (coarse-to-fine allowedness) | 3.2 |
| triangular solution | (P1) + delta_l > 0; amplification Lambda_f <= vartheta^{-l^2} Lambda°(l) | 3.3 |
| fine carriers negligible | (P2): sum_{l > l_*} lambda_l <= T_lo(l_*)^3 | 3.4, 4.2 |
| windowed averaging | (P3): windows with n^w_l >= l 2^{l^3} Lambda°(l) dyadic scales and T_hi(l) 2^{l^3} Lambda°(l) <= 1/l | 5.3 |
| transfer peaks | density of every tail of each block (Lemma B) | 5.1 |
| final recovery | C Thm 7.4 (any admissible T) | 5.2 |
| admissibility (Y cap c_00 = {0}, injectivity) | allowedness (b) + super-fast c_l (P1 2.1's argument) | 1.3 |
NOT used: rates of approximation of targets, any relation between delta_l and lambda_l, quantitative independence of targets, tameness or
margin sparsity of f, the structure of peaks/non-peaks, the number of active blocks, finiteness of the contact set.
Martin's own T (KLMW Prop 2.8, construction unknown to us) is covered only if its vectors carry private signatures with the
allowedness pattern and the weights have windows; nothing is claimed for it.

## 6.2 The open core O1-O4 (BRIEFING_R2 ADDENDUM 2) at first rows in R_0
For the SLD operator and f in R_0 (in particular at every base-tame f, with arbitrary blocks; and at f with infinite contact sets whose
signature sets keep room) Theorem B settles all four items:
 * O1 (infinitely many strict non-peaks, deep coefficients, failure of (MS), (MS-Q)): no block hypothesis is used; every carrier, peak or not,
   is a "coordinate with a two-sided capacity 2 gap/t" whose one-sided excess is pinned (4.2(c)).
 * O2 (second-order rebalancing): the budget controls the weighted invariant Gamma_w of every admissible decomposition (2.3(d)); transfer
   peaks realise Gamma_w at all scales below c_1 t uniformly (5.1). No engineering of approximants is needed: recovery is through
   C Thm 7.4's canonical truncations of an AVERAGED certificate at f.
 * O3 (approximate resonances, scale-dependent switching, near-threshold carriers, weak peaks, contacts/near-contacts as one-sided
   resources): every switching between the two sides of t = 0 is a two-sided difference Delta c, Delta B, pinned to O(Lambda_f(l_*) t) by the
   signatures (3.4-3.5). This is NOT a statement that approximate resonances are absent (they may be forced by the density of the tails and
   by the choice of f); it says their switching amplitude at scale t is O(K t), and the windows contain n >> K dyadic scales so that the
   averaging theorem absorbs them. The quantitative-independence hypotheses (QI), (HT), conversion capacity, (PC), (PC*) of Round 2 are
   all bypassed.
 * O4 (several active blocks, no (S)/(TC), cross-block relations): one ladder through all blocks; nothing block-specific is used.
Outside R_0 (Lemma Z) the items reappear only in the form "base-side one-sided resources sitting on signature sets, or infinite base support".

## 6.3 The missing lemma: Lemma Z (OPEN), its meaning and what is known
Lemma Z: for every f in S_{p_N*}, g in C(f), rho < 1, eps > 0 there is f' in R_0 with p*(f' - f) < eps and dist(rho g, C(f')) < eps.
By Theorem C it is EQUIVALENT to density for the SLD operator. Remarks:
 (a) (PROVED) It holds trivially on R_0. It holds for all mates of f that admit Round-2 engineering: every NA approximant is in R_0, so P2A Thm 2.1,
     N2 Thms 1-3, N2-ref Thm 3*, P2x Thm 3.5 (all valid for any admissible T, under their stated hypotheses) give Lemma Z for the exact two-piece
     mates they cover (hence for P1-type exact resonances with Delta d = 0 at signature-resonant f).
 (b) (Reformulation, PROVED) f is outside R_0 iff F is infinite or for every gamma, vartheta > 0 some signature set S_l (m(l) <= N) has
     ||h_l 1_{S_l cap J_gamma}|| < vartheta^l ||h_l||, i.e. (essentially) the one-sided base resources (support F, contacts, near-contacts) swallow
     the signature of some carrier, or of a fast sequence of carriers. Only these carriers lose their pinning; all others stay pinned.
 (c) (Freedom in Lemma Z, PROVED by Theorem B) The approximants need NOT be norm attaining: any f' with finite base support and room on a
     vartheta^l-fraction of every signature set will do, e.g. f' obtained from f by keeping z on all coordinates except a sparse
     subset of each non-roomy signature set, where |z'| is lowered to 1 - gamma, and by truncating a. Contacts elsewhere (infinitely many) can
     be kept. This is much more freedom than the NA engineering of Rounds 1-2 (which had to replace every infinite contact set by a finite
     window plus far pulls).
 (d) (HEURISTIC) The structure that remains is an exact-resonance structure: if only FINITELY many carriers are unpinned (finitely many
     signature sets swallowed), the argument of parts 3-4 shows that every admissible two-sided decomposition is "pinned part O(K t)" +
     "finitely many free carrier coefficients" + their base counterparts on F cup K cup near-contacts, i.e. an exact (finite-carrier) two-piece
     structure up to O(K t) on whole windows. Combining the window averaging of 5.2 with the engineered recovery of exact resonances
     (P2A/N2/S3) is the natural route to Lemma Z in that case; the case Delta d < 0 and the joint control of averaging and engineering are
     not written. OPEN.
 (e) (SKETCH) Infinite base support F with (SR): the proof of Theorem B goes through with three changes: clamp B_+(j) on F at 2|a_j|/t (the
     excess beyond the no-flip capacity |a_j|/t is one-sided and bounded by |B_+(j) - B_-(j)| plus flip costs, exactly as in 4.2(c));
     truncate the clamped base part to a finite set F_t with sum_{j in F \ F_t} |a_j| <= t^2; in 5.1 the base radius is then of order t (fine for
     |s| <= c_1 t); and use C Thm 7.4 for a not in c_00 with b in c_00 (C Remark 7.1' extended to b != 0 by the C referee, rem71_check.py).
     I have not written the details: SKETCH. If completed, the open core reduces to signature-resonant f only.

## 6.4 Consistency checks and skepticism
 * No counterexample is claimed or suggested. Theorem B is a positive statement on a dense class (it contains NA cap S_{p*}).
 * P1's example (exact resonance whose carrier's signature set is the contact set) is outside R_0 for the analogous design, consistent with
   its nonempty INTRINSIC defect (P1 Thm 2.4): at f in R_0 Theorem B shows there is no intrinsic defect at all relative to the
   Gamma_w-certificate class (every mate is a norm limit of Gamma_w-certificates in C(f)); so P1's phenomenon is exactly the failure of (SR).
   (Concurrent S3 notes claim P1's f is in R by other means; this is compatible.)
 * Corollary (PROVED, from the proof of Theorem B): for f in R_0, C(f) = closure of {g_c in C(f) : c balanced finite certificate, Gamma_w(c) <= 1}
   (the closure being taken in norm). Indeed 5.2 produces such rho g_c -> rho g. In particular C is lower semicontinuous at every f in R_0
   along every sequence along which C Thm 7.4's certificates transport (e.g. canonical truncations).
 * Sanity of the constants: every constant in parts 2-5 depends only on (f, g, rho, gamma, vartheta, N) or on the design; the design's
   super-exponential slack 2^{l^3} beats vartheta^{-l^2} and all fixed constants for l large, which is the only place where the order of
   quantifiers (T before f) matters.
 * Numerics: none were needed; all steps are exact algebra (2.3, 2.4, 3.2, 4.2) or imported refereed expansions (A Lemma 4.3, C (7.2),
   C (7.3), C Thm 7.4, which were numerically confirmed in Round 1).
