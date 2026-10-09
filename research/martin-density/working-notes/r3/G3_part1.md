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
