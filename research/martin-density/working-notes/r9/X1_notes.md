# X1 notes (Round 9): status coherence without (KN), exact coupling (S1), RT*(c) — F finite

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; notation there), finite block set I = {1..N}, p = p_N, first rows f with FINITE
base support F; design D^{U1'} of U1-ref on U4's T_final (diagonal mu-base), modified in Section 3 (generic weights).  Notation of U1 /
U1-ref: block m, zeta = R_m^{**} zhat, A = |zeta|_m, M + C = 1, theta = AM/C, nu_k = |zeta(k)|/Phi_k^2, rho_k = nu_k/theta (peak iff rho >= 1),
P peaks, Q strict non-peaks, Omega ⊂ Q switching set, kappa = A + theta Phi_P^2 + S_f/theta (S_f := sum_{Q \ Omega} nu^2 Phi^2),
r_l := u_l(zhat)/kappa (l in Omega), R^2 := m^2 sum_Omega r_l^2, a := A/theta, k := kappa/theta; data convention Delta = d(omega^-) - d(omega^+),
Delta' = Delta M.  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED" = complete proof here, using only results refereed in earlier
rounds (U1-ref, V1, V2, U4, Y1-Y4 as cited) and standard real-semialgebraic geometry [BCR = Bochnak-Coste-Roy, Real Algebraic Geometry].
Part files r9/X1_part1..4.md; scripts and outputs r9/X1_work/.  No counterexample is claimed; nothing found points to one.

## 0. Summary
(1) LEVERS (task item 1): the requested private levers cannot make (KN) automatic, and they are not needed.
    * Lemma K (PROVED): k = kappa/theta = K(sigma, R^2) := [sigma + sqrt(sigma^2 R^2 + sigma(1 - R^2))]/(1 - R^2), sigma := Phi_P^2 + s_f,
      strictly increasing in sigma and R^2; rho_l = m |r_l| K/Phi_l on Omega (with U1-ref's Lemma R-kt).
    * Lemma F (floor lemma, PROVED): at fixed active ratios every active relative position is >= its FLOOR rho^0_l = m|r_l| K(sigma_rob, R_a^2)/Phi_l;
      inactive Omega carriers, fine carriers and near-threshold peaks only ADD to k.  A lever created or tuned at a companion gives back at
      most what it adds; a private lever helps iff it is robust and inactive AT f.  So (KN) is equivalent to robust inactive k-mass at f,
      a property of f (rate objects (R3), (R4)), not of the design.
(2) STATUS COHERENCE WITHOUT (KN) (the missing step of U1-ref's Master Theorem IV' and of X2's Master Theorem V):
    * Lemma EC (effective columns) and 2.2 (PROVED): after rewriting U1-ref's inward row (X4) at the floor, the exact shifted cone
      Gamma^#(kappa, a) and its tiny-minor zero set Z do NOT contain the weights Phi_d of the active near-threshold carriers; these weights
      enter the whole problem only as the denominators of the floor statuses rho^0_d = psi_d(r)/Phi_d.
    * Lemma NLM (semialgebraic Sard, PROVED): the set of weight vectors for which the threshold value 1 is a local-minimum value of
      max_d psi_d/Phi_d on Z has dimension < |N|.  Lemma GEN (PROVED): weights algebraically independent over the (countable) field of all
      other design data avoid it for EVERY pattern simultaneously (no order-of-choices problem).
    * Lemma QC + Proposition KN^tr (PROVED): quantitative coherence with design constants (compactness, Lojasiewicz, Puiseux): at every clean
      sub-window, for every class, a companion at cost o(T_lo^2) puts the active ratios exactly on Z and every active near-threshold carrier
      strictly below threshold with gap >= (M/2) c_kappa (T_lo^4/(3 L Design))^{beta_kappa}.  The second "lever" is the position of the exact
      point on Z, decoupled from the statuses by the generic weights.
(3) (S1) in general and RT*(c) (task item 2): PROVED for the design T^tr (Theorem S1), any number of shifted blocks.
(4) MASTER THEOREM IV^tr (task item 3; PROVED modulo refereed tools): every activity class without active shift or one-signed is
    recovered, for every N.  COROLLARY: for N = 1 EVERY first row with finite base support is in Rec(p_1) (finite-F Lemma Z for p_1),
    for the design T^tr with (T-a) relaxed to "q*(Te_l) <= 1" (option (a); the equality clause is a normalization: Martin's proof uses only ||T|| <= 1, and we found no use of it in the note).  With
    (T-a) as stated (option (b), c_1 = 1) one explicit thin exception remains (OPEN).  Combined with X2's (unrefereed) Theorem C_mix:
    every F-finite row is in Rec(p_N) for every N (SKETCH, conditional on X2).
Lemma Z and density of NA((c_0, p_N), l_2^2) (every N) and NA((c_0, p), l_2^2) remain OPEN: infinite base support (E1)-(E5) is untouched.

## Results table
| # | Result | Status | Where |
|---|---|---|---|
| 1 | Lemma K (closed form and monotonicity of k) | PROVED (+ numerics 3.5e-50) | 1.1 |
| 2 | Lemma F (floor lemma; levers must be robust at f; (KN) <=> robust inactive k-mass) | PROVED (+ numerics) | 1.2 |
| 3 | Remark: fine / medium / sibling levers cannot make (KN) automatic | PROVED facts + HEURISTIC conclusion | 1.3 |
| 4 | Lemma EC (effective columns u_l - r_l tau_m; Omega-weights absent) | PROVED | 1.4 |
| 5 | Dichotomy KN-blocks / unshifted blocks / T-blocks | PROVED | 2.1 |
| 6 | Floor-form inward rows (X4^0): satisfied by the data, kind [3] at the companion, weight-free | PROVED | 2.2 |
| 7 | Lemma NLM (coincidence set has dimension < |N|) | PROVED (+ toy numerics) | 2.3 |
| 8 | Lemma GEN (algebraically independent weights avoid all coincidences) | PROVED | 2.4 |
| 9 | Lemma QC (quantitative coherence; polynomial margin) | PROVED (+ toy numerics) | 2.5 |
| 10 | Proposition KN^tr (exactification with threshold protection, no (KN)) | PROVED mod refereed tools | 2.6 |
| 11 | Design T^tr, Lemma W' (admissible, N-free, refereed results survive) | PROVED | 3.1 |
| 12 | Theorem S1 ((S1) general, RT*(c)) | PROVED mod refereed tools | 3.2 |
| 13 | Master Theorem IV^tr | PROVED mod refereed tools | 4.1 |
| 14 | Corollary IV^tr.1 (N = 1: finite-F Lemma Z for p_1, option (a)) | PROVED mod refereed tools | 4.1 |
| 15 | Corollary IV^tr.2 (all N, all classes, with X2) | SKETCH (X2 unrefereed) | 4.1 |
| 16 | Option (b) exception (weight-one carrier exactly at threshold) | OPEN | 4.3 |
| 17 | Infinite F; transfer to Martin's p | OPEN (unchanged) | 4.3 |

## 1. What a kappa-neutral lever can and cannot do

### 1.1 Lemma K (closed form of k).  PROVED.
For a block with peak set P, switching set Omega ⊂ Q, put sigma := Phi_P^2 + s_f, s_f := S_f/theta^2.  Then R < 1 and
    k = K(sigma, R^2) := [ sigma + sqrt( sigma^2 R^2 + sigma (1 - R^2) ) ] / (1 - R^2),      a = k - sigma,
and rho_l = m |r_l| K(sigma, R^2)/Phi_l for l in Omega.  K is strictly increasing in sigma and in R^2.  Uniformly,
a^2 = E := sum over ALL carriers k of the block of Phi_k^2 min(rho_k, 1)^2.
Proof.  U1-ref's Lemma R-kt (refereed): a^2 = Phi_P^2 + k^2 R^2 + s_f, k = a + Phi_P^2 + s_f, rho_l = m |r_l| k/Phi_l, R < 1, a > kR.  Both
equations contain (Phi_P^2, s_f) only through sigma.  Substituting a = k - sigma: (1 - R^2) k^2 - 2 sigma k + sigma^2 - sigma = 0, whose
roots are k_+- := [sigma +- sqrt(sigma^2 R^2 + sigma(1 - R^2))]/(1 - R^2).  The minus root satisfies k_- <= sigma (equivalently
sigma R^2 <= sqrt(sigma^2 R^2 + sigma(1 - R^2)), i.e. 0 <= sigma(1 - R^2)(1 + sigma R^2)), so it gives a = k_- - sigma <= 0 and is excluded
by a = A/theta > 0; hence k = k_+.
Monotonicity in sigma: the numerator is increasing, the denominator fixed.  In R^2: differentiate a^2 = sigma + k^2 R^2 with da = dk at fixed
sigma: dk/dR^2 = k^2/(2(a - k R^2)) > 0 since a > kR > kR^2.  Uniform form: (E2) of U1 Lemma 1.2 divided by theta^2:
a^2 = Phi_P^2 + sum_Q rho^2 Phi^2.  QED
Numerics: X1_work/lemmaK_check.py (50 digits, 70 random blocks from the referee's solver): closed form rel. err 3.5e-50, a^2 = E 6.3e-50.

### 1.2 Lemma F (floor lemma).  PROVED.
Fix a block, its ACTIVE switching carriers Omega_a ⊂ Omega (class a) with ratios r_a, and let P_rob be the peaks that remain peaks under every
admissible companion move (at a clean sub-window: the coarse peaks with rho >= 1 + u(w); a companion of cost o(T_lo^2) cannot lower their
values by u theta Phi/m >> T_lo^2).  Put sigma_rob := sum_{P_rob} Phi^2, R_a^2 := m^2 sum_{Omega_a} r^2.  At every first row reachable at
cost o(T_lo^2) at which the active ratios equal r_a, every active carrier satisfies
    rho_l >= rho^0_l(r_a) := m |r_l| K(sigma_rob, R_a^2)/Phi_l      (up to the fine terms sum_{fine} Phi^2 <= C c_{L+1}^2),
with equality iff all inactive Omega carriers have value 0, there are no fine contributions and P = P_rob.
Proof.  Lemma K: rho_l = m|r_l| K(sigma, R^2)/Phi_l with sigma = Phi_P^2 + s_f >= sigma_rob - (fine) (peaks of P_rob persist, further peaks
and strict non-peaks outside Omega only add) and R^2 = R_a^2 + m^2 sum_{inactive} r^2 >= R_a^2; K is increasing in both.  QED
Consequences.  (i) A lever created or tuned at a companion (from value 0 to a robust relative position) raises k first; its inward push can
only return k towards the floor.  A lever helps by exactly the INACTIVE k-MASS present at f,
    I(f) := K(sigma(f), R(f)^2) - K(sigma_rob, R_a(f)^2) >= 0.
(ii) (KN_{w,a}) of U1-ref holds for a block iff that block has an inactive coarse carrier with rho in [u(w), 1 + b(w)] (an inactive strict
non-peak of robust relative position, or an inactive near-threshold carrier, which can first be pushed below threshold): this is read off
the rate objects (R3), (R4) at f.  It is a property of f, not of the design.
(iii) Hence the bad case of U1-ref 3.4 is exactly: tiny inactive k-mass (I(f) <= C D^2 (b + c_{L+1}^2)) and an exact zero set Z on which
max_{d near-threshold active} rho^0_d >= 1 near r(f).
Numerics: X1_work/floor_check.py (34 digits, 11 random blocks with robust inactive mass): removing the inactive mass at fixed active ratios
(fixed point zeta_l = lambda_l r_l kappa) lowered every active rho (min decrease 3.3e-7) and the result equals the floor to 1.6e-34.

### 1.3 Remark (designed levers).  PROVED facts, HEURISTIC conclusion.
(a) Fine levers (weights <= c_{L+1} <= b(L, M(L))^2) have capacity |zeta| <= theta c_{L+1}^2, far below the k-shift ~ D(L) eta needed after
a Lojasiewicz displacement eta, which can be as large as C_L b(w)^{2/N_L} >= b(w) (PROVED).  (b) Levers tuned at the companion must have weight << T_lo(w)^2 (cost ~ theta Phi) and
capacity >> eta(w): they must sit between the scales of w and b(w), i.e. between sub-windows; then they are coarse carriers of all later
sub-windows of the level, each adding >= 1 rate object per sub-window, which defeats the pigeonhole M(L) = omega(L) + 1 (HEURISTIC).
(c) Near-parallel "siblings" (u_{d'} = (n_d u_d + eps h_P)/n_{d'}, P private, eps << theta Phi_d, coarser by a factor 2) are automatically
robust non-peaks when d is near threshold (PROVED: rho_{d'} in [rho_d/5, 4 rho_d/5] if eps ||h_P||_1 <= n_d |v_d|/2), but the coarsest
member of every family has no coarser sibling, and families must keep appearing at all levels for (T-d) (PROVED); so siblings cannot make
(KN) automatic either.  By Lemma F none of this is needed: Section 2 shows that status coherence follows from the geometry of Z.

### 1.4 Lemma EC (effective columns).  PROVED.
In U1's coarse system substitute (X3)_m/kappa_m, Delta'_m = sum_{l in Omega_a(m)} r_l gamma_l.  The coarse certificate on E_c is
    L(gamma) = sum_{l in Omega_a} gamma_l c_l(r_l),     c_l(r_l) := u_l|_{E_c} - r_l tau_{m(l)},    tau_m := sum_{p coarse peak of m} vs_p lambda_p u_p|_{E_c}.
Each column depends only on its own ratio; tau_m is a design vector once the pattern (peaks and signs) is fixed; the weights of the
Omega carriers do not occur.
Proof.  U1 Lemma 1.1(a): V(Domega) = sum_l gamma_l u_l with gamma_l = lambda_l (Domega(l) - Delta_m w(l)); for coarse peaks gamma_p = -Delta_m
lambda_p vs_p M = -Delta'_m lambda_p vs_p; nearly neutral carriers are exactified to w = 0 (gamma = 0); inactive Omega carriers have gamma = 0;
fine carriers contribute the fine residues (absorbed separately, U1 3.5).  Insert Delta'_m.  QED

## 2. Status coherence without (KN)

Setting: a clean sub-window w of a main stage L >= l_f, an activity class a (U1 2.3, fixed before the exactification as in U1-ref),
the companion construction of U1-ref Proposition KN.  b := b(w), u := u(w), D := D(L).  At a clean w every coarse carrier has
rho in [0,b] ∪ [u, 1-u] ∪ [1-b, 1+b] ∪ [1+u, inf) ((R3), (R4)).  For a block m: Omega_a(m) its active Omega carriers, N(m) ⊂ Omega_a(m) the
active near-threshold ones, P_rob(m) its coarse peaks with rho >= 1 + u, sigma_rob(m) := sum_{P_rob(m)} Phi^2 > 0 (V1 Lemma D).

### 2.1 Three kinds of blocks.  PROVED.
 (U) UNSHIFTED: Delta'_m = 0 in the class ((X5) removes the variable Delta'_m).  Then (X3)_m reads sum_{Omega_a(m)} r_l gamma_l = 0 and the
     other rows of block m do not contain r^(m) ((X4) reads vs_l gamma_l >= 0); every minor is homogeneous of degree <= 1 in r^(m), so the
     uniform rescaling r^(m) -> s r^(m) preserves the vanishing of every minor and changes robust ones by a factor in [s, 1].  By Lemma K it
     lowers every active rho of block m by a factor <= s (|r_l| scales by s and K decreases).  So in (U)-blocks the target ratios are
     s_m r''^(m) with 1 - s_m = C Lip eta' (2.6): no lever and no genericity are needed (this is the content of U1-ref's "classes with no
     active shift: V2 Theorem B, values only").
 (KN) Delta'_m active and some INACTIVE coarse carrier of m has rho in [u, 1 + b]: U1-ref Proposition KN's lever (an inactive near-threshold
     peak is first pushed below threshold at cost O(b theta Phi); it is then an inactive Omega carrier with rho >= u).
 (T) Delta'_m active and every inactive coarse carrier of m is nearly neutral (rho <= b) or a robust peak.  Then the inactive k-mass is
     I_m(f) <= C D^2 (b + c_{L+1}^2), so |rho_l(f) - rho^0_l(r(f))| <= C D^2 (b + c_{L+1}^2) for the active carriers (Lemma F, Lemma K's
     Lipschitz bounds on the compact region of 2.3; active weak peaks contribute Phi^2 as peaks and rho^2 Phi^2 = (1 + O(b)) Phi^2 as Omega members).
Only (T) is new.  Let N_T := union of N(m) over the (T)-blocks.

### 2.2 The floor-form inward row; weight-freeness.  PROVED.
For l in N(m), m a (T)-block, replace U1-ref's row (X4) "vs_l gamma_l/lambda_l + Delta'_m >= 0" by
     (X4^0)    vs_l gamma_l + Delta'_m m^2 |r_l| K(sigma_rob(m), R_a(m)^2) >= 0.
(i) Meaning: lambda_l vs_l Domega(l) = vs_l gamma_l + Delta'_m lambda_l rho_l and lambda_l rho^0_l = m^2 |r_l| K(sigma_rob, R_a^2); so (X4^0) is
    "vs Domega(l) >= 0 at the floor".
(ii) The decomposition data satisfy (X4^0) up to lambda_l (3 gap(f)/t + C_f D^2 (b + c_{L+1}^2)) <= K t: at strict non-peaks of f by
    lem:suplevel(f) (vs Domega_dec(l) >= -3 gap(f)/t), at weak peaks of f by eq:peakshift (vs(omega_- - omega_+) = e_l >= 0), and
    |rho_l(f) - rho^0_l(r(f))| <= C D^2 (b + c_{L+1}^2) in a (T)-block (2.1); gap(f) <= b and b << t^2.
(iii) At a companion f^# whose active ratios are r and whose statuses satisfy rho_l(f^#) - rho^0_l(r) <= C c_{L+1}^2 D^2 and
    rho_l(f^#) <= 1 - mu/2: every point of the cone has vs Domega(l) >= -|Delta'_m| C c_{L+1}^2 D^2 >= -3 gap^#(l)/t, which with V1 TR Step 5
    (shift trick) is kind [3]; for the clamped + side vs omega^+(l) <= (1 - d_+ t) gap(f)/t <= 1.5 gap^#(l)/t holds once gap(f) <= M b <=
    gap^#/4 (ensured by 2.6(D2)).  Kind-[3] gaps enter no constant of U1-ref's assembly (V1 TR(iii): c_flat >= c_0 gamma(w)/A_2 uses the
    kind-[2] threshold gamma(w) = min M u/4 only).
(iv) WEIGHT-FREENESS.  In the variables (Delta', gamma), every row of Gamma^#(kappa, a) — (X1) with entries u_l(j) and Delta'_m tau_m(j),
    (X2), (X5) sign/zero rows, (X3)/kappa with entries r_l, aggregated signature rows (one nonzero entry each; their design coefficient does
    not affect the vanishing of minors), (X4^0) with entries vs_l, m^2 |r_l| K(sigma_rob, R_a^2) in (T)-blocks, U1-ref's (X4) in (KN)-blocks,
    vs_l gamma_l >= 0 in (U)-blocks — and every cofactor polynomial (U1-ref (p-c)) is a function of: the vectors u_l on E_c, the peak traces
    (peak vectors and peak weights), sigma_rob, the ratios r, signs, and the weights of (KN)-block carriers.  The weights Phi_d, d in N_T,
    do not occur.  Hence the zero set Z_kappa (ratio space) of the tiny minors of a pattern kappa and the functions
        psi_d(r) := m |r_d| K(sigma_rob(m(d)), R_a(m(d))(r)^2)      (d in N_T)
    are independent of (Phi_d)_{d in N_T}, and rho^0_d = psi_d/Phi_d.  [U1-ref's row with "1" contains 1/lambda_d: it is the only place where an
    N_T-weight would enter, and (X4^0) removes it.]

### 2.3 Lemma NLM (the threshold is not a local-minimum value, for generic weights).  PROVED.
A PATTERN kappa of level L consists of the finite combinatorial data (Omega_a with signs; peak sets and signs; classes R/G; contact/free
types on E_c; the kind (U)/(KN)/(T) of each block; the sets N(m); the tiny/robust labels of the minors).  Fix kappa and all its data except
the weights (Phi_d)_{d in N_T}.  Let K_kappa := {r : |r_l| <= 2 Phi_l/(m k_min), R(m)^2 <= 1 - eps_K for all m} (design numbers k_min, eps_K > 0
chosen so that the data of 2.6 lie in its interior), Z := Z_kappa ∩ K_kappa (closed, semialgebraic), and for Phi in (0, inf)^{N_T}
     F_Phi(r) := max_{d in N_T} psi_d(r)/Phi_d     (r in Z).
COINCIDENCE(Phi): some r_0 in Z with F_Phi(r_0) = 1 is a (possibly non-strict) local minimum of F_Phi on Z.  B_kappa := {Phi : COINCIDENCE(Phi)}.
Claim: B_kappa is semialgebraic of dimension < |N_T|, definable with parameters from the remaining data of kappa.
Proof.  The minors are polynomials in the entries; K satisfies (1 - R^2)k^2 - 2 sigma k + sigma^2 - sigma = 0, k > sigma; so Z and the psi_d
are semialgebraic, independent of Phi (2.2(iv)), and B_kappa is first-order definable, hence semialgebraic (Tarski-Seidenberg).  Take a
finite stratification of Z into connected Nash submanifolds S compatible with the sets {r_d > 0}, {r_d = 0}, {r_d < 0} (d in N_T) [BCR,
Section 9.1]; each psi_d is Nash on each S contained in {r_d != 0} (K is Nash on {R^2 < 1}).  For nonempty D ⊂ N_T and a stratum S ⊂ {r_d != 0,
d in D} let CV_{D,S} be the set of critical values of Psi_{D,S} := (psi_d)_{d in D}|_S : S -> R^D; by the semialgebraic Sard theorem
dim CV_{D,S} < |D| [BCR, Thm. 9.6.2 (Sard for Nash maps)].  Let Phi in B_kappa with witness r_0 in a stratum S and D := {d : psi_d(r_0)
= Phi_d}; D is nonempty and psi_d(r_0) = Phi_d > 0 gives r_0 in {r_d != 0} (d in D).  Suppose r_0 were a regular point of Psi_{D,S}.  Then
there is v in T_{r_0} S with d psi_d(r_0)v = -1 for all d in D, and a Nash curve gamma in S with gamma(0) = r_0, gamma'(0) = v; for small s > 0,
psi_d(gamma(s)) < Phi_d (d in D) and, by continuity, psi_d(gamma(s)) < Phi_d (d in N_T \ D), so F_Phi(gamma(s)) < 1 = F_Phi(r_0): r_0 is not a
local minimum on Z.  Hence r_0 is critical and (Phi_d)_{d in D} in CV_{D,S}, so
    B_kappa ⊂ union over (D, S) of { Phi : (Phi_d)_{d in D} in CV_{D,S} },
a finite union of semialgebraic sets of dimension < |D| + |N_T \ D| = |N_T|.  QED

### 2.4 Lemma GEN (algebraic independence avoids every coincidence).  PROVED.
Let k_0 ⊂ R be the field generated by all non-weight data of the design: the entries of all candidate targets (a countable pool), the
signature data (S_l, delta_l, H_l), the normalizations n_{l,i} of every candidate, the absorber/FD target values, and the base data
(mu_s, ||U||).  k_0 is countable.  If the weights of the carriers in N_T(kappa) are algebraically independent over k_0(all other weights),
then (Phi_d)_{d in N_T} notin B_kappa.
Proof.  B_kappa is semialgebraic of dimension < n := |N_T|, definable over k := k_0(the other weights of kappa) (2.3).  Cylindrical algebraic
decomposition over the real closure k^rc of k [BCR, Thm. 2.3.1; Section 5.3 (extension of real closed fields)] writes B_kappa as a finite
union of cells definable over k^rc; a cell of dimension < n is, at some level i of the cylindrical structure, a graph
x_i = xi(x_1, ..., x_{i-1}) of a continuous semialgebraic function xi defined over k^rc, and xi satisfies a nonzero polynomial relation
P(x_1, ..., x_{i-1}, xi) = 0 with coefficients in k^rc [BCR, Section 2.6: every semialgebraic function satisfies a nonzero polynomial
equation P(x, f(x)) = 0].  So every point of B_kappa has a coordinate algebraic over k^rc(the other coordinates), hence over k(the other coordinates).
The Phi_d = 2^{-m(d)-k(d)} c_d (d in N_T) are algebraically independent over k.  QED

### 2.5 Lemma QC (quantitative coherence).  PROVED.
Fix kappa with Phi := (Phi_d) notin B_kappa, F := F_Phi, Y_1 := Z ∩ {F <= 1}, and G_h(r) := inf{F(r'') : r'' in Z, |r'' - r| < h} (r in Z, h > 0).
(a) mu_kappa(h) := 1 - max_{r in Y_1} G_h(r) > 0 (mu := 1 if Y_1 is empty).
(b) If Y_1 is empty then F >= 1 + m_0 on Z for a number m_0 > 0; otherwise dist(r, Y_1) <= C_Y (F(r) - 1)_+^{alpha_Y} on Z, alpha_Y in (0, 1].
(c) There are c_kappa, beta_kappa, h_kappa > 0 with mu_kappa(h) >= c_kappa h^{beta_kappa} for 0 < h <= h_kappa.
All of these are determined by kappa (design numbers of level L; finitely many kappa per level).
Proof.  (a) G_h is upper semicontinuous on Z: if r_n -> r and r'' in Z with |r'' - r| < h, then |r'' - r_n| < h eventually, so limsup G_h(r_n)
<= F(r'').  Y_1 is compact.  For r in Y_1: if F(r) < 1, G_h(r) <= F(r) < 1; if F(r) = 1, r is not a local minimum of F on Z (Phi notin
B_kappa), so points r'' in Z arbitrarily close to r have F(r'') < 1 and G_h(r) < 1.  An usc function attains its maximum on a compact set.
(b) If Y_1 = {}, F - 1 > 0 is continuous on the compact Z, with minimum m_0 > 0.  Otherwise f_1 := dist(., Y_1), f_2 := (F - 1)_+ are
continuous semialgebraic on the compact Z with f_2^{-1}(0) = Y_1 = f_1^{-1}(0); the Lojasiewicz inequality [BCR, Cor. 2.6.7] gives
f_1^{N} <= C f_2 on Z.  (c) h -> mu_kappa(h) is semialgebraic (first-order definable), positive and nondecreasing; a one-variable
semialgebraic function is Nash on some (0, h_kappa) with a Puiseux expansion mu = c h^{p/q}(1 + o(1)), c > 0, at 0 [BCR, Section 2.6 with
Puiseux series; van den Dries, Tame Topology, Ch. 7]; take c_kappa := c/2, beta_kappa := p/q.  QED

### 2.6 Proposition KN^tr (exactification with threshold protection, without (KN)).  PROVED (modulo U1-ref Prop. KN and refereed tools).
Design: T^tr of 3.1, whose rate scheme contains, for all patterns kappa and classes of level L, the minors of Gamma^#(kappa, a) written
with (X4^0) / (X4) / U-rows as in 2.2(iv) and their cofactor polynomials, and whose sub-window thresholds satisfy, with
eta'(w) := T_lo(w)^4/(L Design(L)) and delta_0(b) := (1 + Lip C_*) b + Lip C_L ((1 + Lip C_*) b)^{2/N_L} + C D^2 b:
 (D1) C_L ((1 + Lip C_*) b(w))^{2/N_L} <= eta'(w)/3   (Lojasiewicz displacement; V2 Lemma L in semialgebraic form, constants C_L, N_L, Lip);
 (D2) delta_0(b(w)) <= min_kappa min( m_0(kappa)/2, (eta'(w)/(3 C_Y(kappa)))^{1/alpha_Y(kappa)} ),  M b(w) <= min_kappa mu_kappa(eta'(w)/3)/8;
 (D3) c_{L+1} <= min_{w, kappa} mu_kappa(eta'(w)/3)/(8 C D(L)^2)  (weight bound (W8)).
(Each right side is a design number of level L computed before b(w), resp. before c_{L+1}; b(w) := min of U4's b(w) and the largest
value satisfying (D1)-(D2).)
Statement.  At every clean sub-window w of every main stage L >= l_f and every class a there is a companion f^(1a) with:
 (a) the active ratios r'' lie on Z_kappa (every tiny minor and tiny cofactor polynomial vanishes) and every robust one is >= u/2;
 (b) in (T)-blocks every active near-threshold carrier has rho <= 1 - mu_kappa(eta'/3)/2, hence gap >= (M/2) c_kappa (eta'/3)^{beta_kappa};
     in (KN)-blocks U1-ref Prop. KN(b) holds; in (U)-blocks the rescaling of 2.1(U) gives rho <= 1 - eta'; every other coarse carrier
     keeps its robust status;
 (c) p*(f^(1a) - f) <= C_f Design(L) eta' log(1/eta') = o(T_lo(w)^2).
Proof.  Step 0: V1's (C1), (C2); in (T)-blocks push every active weak peak inward to rho = 1 - b (value change <= 2 b theta Phi/m; cost
O(b)); now all active near-threshold carriers are strict non-peaks, Lemma R-kt applies, and every tiny minor is <= (1 + Lip C_*) b at the
ratio vector r_1 of this row f_1.  Step 1 (Lojasiewicz): r' in Z_kappa with |r' - r_1| <= eta'/3 (D1).  By 2.1(T) and Lipschitz bounds,
F(r') <= 1 + delta_0(b).  Step 2: by (D2) and 2.5(b), Y_1 is nonempty and there is r_1' in Y_1 with |r_1' - r'| <= eta'/3.  Step 3: by 2.5(a)
there is r'' in Z_kappa with |r'' - r_1'| < eta'/3 and F(r'') <= 1 - mu_kappa(eta'/3).  So |r'' - r_1| <= eta'.  Step 4 (realization, U1-ref
Prop. KN Step 2): in (T)-blocks push the nearly neutral inactive Omega carriers to value 0 (cost <= C b); Lemma TU (V1) on the active
values with targets u_l := r''_l kappa; a peak push restoring kappa exactly (intermediate value theorem; kappa is continuous, U1-ref 1);
re-solve TU (block triangular Jacobian: d(u/kappa)/d(TU) = I/kappa, dkappa/d(TU) = O(X)); in (KN)-blocks the inward lever push and restoration
of U1-ref; in (U)-blocks the TU targets are s_m r''_l kappa (2.1(U)): rho <= s_m (1 + b + Lip eta') <= 1 - eta' for C large (b << eta').  Statuses in (T)-blocks: Lemma K with
sigma - sigma_rob <= C c_{L+1}^2 (fine) and R^2 = R_a^2 (inactive values 0): rho_d = (psi_d(r'')/Phi_d)(1 + O(D^2 c_{L+1}^2)) <=
1 - mu/2 by (D3).  Robust statuses and robust minors move by <= Lip eta' << u.  (X4^0) at the companion: 2.2(iii) (gap(f) <= M b <= gap^#/4
by (D2)).  Costs: V1 Lemmas CO, TU(d).  QED
Remark.  No hypothesis on f is used beyond the clean sub-window; the classes are fixed before the exactification (legitimate, U1-ref 2.2).

## 3. The design T^tr; (S1) in general; RT*(c)

### 3.1 Definition and Lemma W'.  PROVED.
Run U4's recursion for T_final with U1-ref's D^{U1'} (rounds PRE - MAIN - CLUSTER, absorber pairs in block 1, sub-window data at every
stage) — and, optionally, X2's additions (D-lev) (a lower bound on Design(L)) and (W_exp) (an upper bound on c_{l+1}) — with three changes:
 (i) RATE SCHEME: add the objects of 2.6 (minors and cofactor polynomials of Gamma^#(kappa, a) in the form 2.2(iv), all patterns and classes
     of the level); omega(l), M(l) = omega(l) + 1, Q(w), Design(l) are computed with them (finitely many per level, N-free).
 (ii) THRESHOLDS: b(w) := min(U4's b(w), the largest value satisfying (D1), (D2)); Design(L) also dominates Lip, C_L and the finitely many
     constants C_Y, 1/m_0, 1/c_kappa, beta_kappa of the patterns of level L.
 (iii) WEIGHTS: let c_l^max be the value T_final / D^{U1'} / D^{X2} would assign at stage l (the minimum of all upper bounds, including
     (D3)); choose c_l in [(1 - 2^{-l}) c_l^max, c_l^max] TRANSCENDENTAL over k_0(c_1, ..., c_{l-1}) (l >= 2) — possible since that field
     is countable.  Option (a): c_1 in (1/2, 1] chosen likewise, (T-a) read as "q*(Te_l) <= 1"; option (b): c_1 := 1 ((T-a) as stated).
Lemma W'.  (1) T^tr satisfies (T-b), (T-c), (T-d), and (T-a) in the chosen form; (2) it is N-free; (3) {c_l : l >= 2} (option (a): all
c_l) is algebraically independent over k_0, and every non-weight datum lies in k_0; (4) every refereed result on the dependency trees of
U4's audit list, of U1-ref's Master Theorem IV' and of V1/V2's Master Theorems II, III' holds for T^tr.
Proof.  (1)-(2): the admissibility proofs (note thm:SLD; U4 Lemma W and its Section 2; U1-ref 6.3) use the weights only through upper
bounds computed from the actual earlier weights and through ratio bounds (c_{l+1} <= c_l/4, (W1)-(W7)); all hold since c_l <= c_l^max.
The lower bound c_l >= (1 - 2^{-l}) c_l^max replaces "c_l = c_l^max" where the old proofs used it as a lower bound: s_1 = T_lo^8 c_l (U3-ref
RT*(f), F7), absorber capacity c_{L+1}/(Design t) (U1 3.5); constants change by factors <= 2.  (The block-1 cluster ratio of U1-ref 7 —
consecutive block-1 weights lambda differ by a factor >= 8 — is untouched: c_l <= c_{l-1}/4 is the upper bound (W1), always enforced.)  No step
depends on N.  (3): induction on l; the non-weight choices (allowedness (a), (c); (GM) for delta_l, which depends on y_l only; FD and
absorber targets with fresh coordinates and binary values; integer numbers R of absorber coordinates) have OUTCOMES in the countable pool,
whose data generate k_0, whatever the weights are.  (4): the new rate objects are finitely many per level; Design(L), b(w), c_{L+1} only
decrease or acquire further factors; U4-ref's Lemma GW (window theorems use a window only through four properties) and V1 Theorem 1'(d)
apply verbatim.  QED

### 3.2 Theorem S1 ((S1) in general and RT*(c)).  PROVED (modulo U1-ref's refereed assembly).
Design T^tr (option (a); under option (b) exclude the patterns with carrier 1 in N_T).  At every clean sub-window w of every main stage
L >= l_f and for every activity class a — any number of shifted blocks, with or without free-ray carriers — there is a companion f^# at cost
o(T_lo(w)^2) at which (a) the exact shifted cone Gamma^#(kappa, a) has all tiny minors exactly 0 and all robust ones >= u/2, so its
l_1-Hoffman constant is <= C (Design(L)/u(w))^C (V2 Lemma H) and the ray coefficients are bounded by A_max <= C_f (Design/u)^C (U1-ref
(p-c)); (b) every carrier carrying switching is a strict non-peak of f^# with the margins of 2.6(b); (c) the coupling rows
Delta'_m kappa_m = sum_{l in Omega_m} u_l(zhat^#) gamma_l (= U3's rows Delta_m = d^#_m(omega^-) - d^#_m(omega^+), U1 Lemma 1.3) hold for every point
of the cone, all blocks at once.  Consequently the decomposition data of every scale of the class project onto exact shifted two-piece data
at f^# with error K t and are normalized onto one shift ray (U1 Prop. 2.2 with U1-ref (p-a)-(p-d)); the fine residues on the coarse
coordinates are cancelled exactly by the zero-value absorbers (U1 Prop. 3.4) after the G1 release (U1-ref 5): this is RT*(c).
Proof.  2.6 gives (a), (b); (c) is the identity of U1 Lemma 1.3 built into the cone.  U1's Proposition 2.2 (refereed with precisions) used
nothing unproved except Theorem 2.3's status claim, now supplied by 2.6; RT*(c) is steps (1b)-(2) of U1-ref's Master Theorem IV' assembly.
U3's "free-ray q < 0 carrier" case (U3-ref 4.4) is the special case of an effective column (1.4) reducing to -r_k tau_m on E_c.  QED

## 4. Master theorem, answers, what remains, numerics

### 4.1 MASTER THEOREM IV^tr.  PROVED (modulo the refereed tools cited by U1-ref's Master Theorem IV', and Sections 1-3).
Design T^tr (option (a)), N fixed, f in S_{p_N^*} with finite base support F.  If for infinitely many main stages L some clean sub-window w
of L has at least n(w)/D_cls(w) dyadic scales whose activity class has no active shift or is one-signed, then f is in Rec(p_N).
Under option (b) the same holds provided, at those sub-windows and classes, the weight-one carrier 1 is not an active near-threshold carrier
of a (T)-block.
Proof.  U1-ref's proof of its Master Theorem IV' (refereed) uses (KN_{w,a}) only through its Proposition KN: the statuses of the active
near-threshold carriers at the exactified companion (Prop. KN(b)), which also feed U1 Lemma 4.3 ((SC) for negative blocks in
configuration (i)).  Proposition KN^tr supplies (a)-(c) of Proposition KN for every class (Theorem S1).  The rows (X4^0) are satisfied by
the decomposition up to K t (2.2(ii)) and make the cone's points kind [3] (2.2(iii)) — the only properties of (X4) used by U1 Prop. 2.2 and
U1-ref 4.1.  All other steps (classes and cubes; normalization onto one shift ray; zero-value absorbers and G1 release; configuration (i)
recursion with (SC); configuration (ii) Schauder completion; Theorem E^SC / E^>= with banked, pulled and absorber supports; subset
averaging, U1 Lemma 2.4) are U1-ref's, valid for T^tr by Lemma W'(4).  QED
COROLLARY IV^tr.1 (N = 1).  For T^tr (option (a)), every first row of p_1 with finite base support is in Rec(p_1): finite-F Lemma Z for p_1.
Proof.  With one block every class is one-signed or has no active shift.  At every clean sub-window (one exists at every main stage, V1
Theorem 2') some class carries >= n(w)/D_cls(w) scales (pigeonhole, U1 2.3-2.4).  Apply 4.1.  QED
COROLLARY IV^tr.2 (every N; conditional).  X2 (Round 9, NOT yet refereed) proves mixed classes recovered under (KN) (Theorem C_mix, Master
Theorem V), using (KN) only through U1-ref's Proposition KN (X2 5.2) and, quantitatively, through the gap lower bound gap_min >= c_f T^4/(L
Design) in its constant K_w (X2 4.2).  With Proposition KN^tr the gap is >= (M/2) c_kappa (T^4/(3 L Design))^{beta_kappa}, still a power of
T_lo(w) with design exponent, so X2's arithmetic goes through after enlarging the exponents in (W_exp)-type bounds (c_{L+1} is chosen
after kappa's constants).  If X2 is confirmed: every F-finite row is in Rec(p_N) for every N.  Status: SKETCH.

### 4.2 Answers to the three questions
(1) Private levers making (KN) automatic: NOT possible in the requested sense, and NOT needed.  Lemma F: no move can push an active status
    below its floor at fixed active ratios; a lever helps exactly by the inactive k-mass present at f, a property of f.  Fine levers lack
    capacity, companion-tuned levers give back what they add, sibling levers fail for the coarsest member of each family (1.3).  The
    missing second lever is the POSITION of the exact point on Z: the weights of the switching carriers never enter Z, so generic
    (algebraically independent) weights decouple exactness from the threshold (2.2-2.5), and (KN) can be dropped.
(2) (S1) in general and RT*(c): Theorem S1 (PROVED for T^tr), any number of shifted blocks, design-controlled Hoffman constants.
(3) Master Theorem IV^tr: all one-signed activity classes (and classes without active shift) are in Rec for every N; all F-finite rows for
    N = 1 (Corollary IV^tr.1).

### 4.3 What remains (precise)
 (R1) Option (b) only (norm-one normalization c_1 = 1 kept): patterns with carrier 1 an active near-threshold carrier of a (T)-block (this
      forces rho_1(f) = 1 exactly).  OPEN.  [The equality clause of (T-a) is a normalization: Martin's proof uses only ||T|| <= 1 (his Step 2
      needs T(e_{n,m}) in B_Y), and we found no use of the equality in the note; option (a) drops it.]
 (R2) Mixed activity classes, N >= 2: X2's Theorem C_mix (pending its referee) + Corollary IV^tr.2.
 (R3) Infinite base support: (E1)-(E5) of ADDENDUM 7, U2's items; at infinite F the patterns are still finite per level, so Lemmas F, NLM,
      GEN, QC should transfer, but this is NOT checked (U2's Theorem M-inf is itself a SKETCH).
 (R4) Martin's p: row-wise statements do not transfer; density for p follows from density for infinitely many p_N (lem:martintail), which
      needs Lemma Z including infinite F.
 Lemma Z and density of NA((c_0, p_N), l_2^2) (every N, including N = 1) and of NA((c_0, p), l_2^2): OPEN (infinite F).
 No counterexample is claimed; nothing found points to one.

### 4.4 Numerics (sanity checks; r9/X1_work/)
 lemmaK_check.py (+ .out): Lemma K closed form vs. the refereed block solver, 50 digits, 70 random blocks: rel. err 3.5e-50; a^2 = E 6.3e-50.
 floor_check.py (+ .out): Lemma F, 34 digits, 11 random blocks with robust inactive mass: removing it at fixed active ratios lowered every
   active rho (min decrease 3.3e-7); final statuses equal the floor m|r|K(sigma, R_a^2)/Phi to 1.6e-34.
 sard_toy2.py (+ .out): toy exact zero set Z (one tiny 2x2 minor, multi-affine) with two active near-threshold carriers: the coincidence
   set {Phi : a local-minimum value of max_d psi_d/Phi_d on Z equals 1} is a curve in the (Phi_1, Phi_2)-plane (one Phi_2 for each Phi_1 in
   {0.03, 0.05, 0.08}; none for 0.12); at the coincidence the minimizer sits where both statuses equal 1 with opposite tangential
   derivatives (critical for Psi_D, as in Lemma NLM); mu(0.003) = 7.8e-16 (= 0) at the coincidence and 1.0e-3, 4.0e-3 after scaling the
   weights by 1.001, 1.01 (Lemma QC).

## 5. Relation to earlier rounds; points for the referee
 * U1-ref 3.4 "Possible route (HEURISTIC)": a generic design making (rho_d) transversal on the exact zero sets, with three missing pieces:
   (a) a construction (only stage-l parameters free), (b) quantitative transversality near singular strata, (c) dim Z_S < |N|.  Here:
   (a) the relevant parameters are the weights of the switching carriers themselves, which by 2.2(iv) do not enter Z or psi; algebraic
   independence of ALL weights (Lemma GEN) removes the order-of-choices problem; (b) no explicit transversality rate is needed — the
   constants of Lemma QC come from compactness, Lojasiewicz and Puiseux and are design numbers absorbed by b(w) and c_{L+1}; (c) is
   the case dim S < |D| of the Sard argument (every point critical, CV of dimension < |D|).
 * The one modification of U1-ref's cone is the inward row: (X4) with the design coefficient "1" (which contains 1/lambda_d) is replaced in
   (T)-blocks by the floor form (X4^0).  Points to check: 2.2(ii) (data satisfy it, uses tiny inactive mass), 2.2(iii) (kind [3]).
 * Lemma F explains WHY (KN) worked (robust inactive k-mass at f) and why companion-made levers cannot replace it.
 * Toy evidence that coincidences are real for special weights and disappear for generic ones: sard_toy2.out (mu = 0 exactly at the
   coincidence, mu > 0 after a 0.1% change of the weights).
 * Not checked: compatibility of the transcendental weight choice with X2's (D-lev)/(W_exp) beyond the remark in Corollary IV^tr.2; transfer of
   Sections 1-2 to infinite F.
