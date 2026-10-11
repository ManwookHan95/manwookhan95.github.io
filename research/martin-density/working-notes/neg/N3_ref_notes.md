# N3_ref_notes — proofs of the referee's fixes and additions for track N3

Setting of N3 Part 2: I = {1} (one block, the norm p_1), T admissible ([I, def:admissible]; only (T-a)-(T-d) used),
lambda_k = Phi(k) = 2^{-1-k} q*(Te_k) <= 2^{-1-k} (k >= 1), ||u_k||_inf <= ||u_k||_1 <= q*(u_k) = 1.  For a row f' (NA or
not) its forced data carry primes; theta' in S_{p**} is its normer, sigma' = |zeta'| with zeta' = R** theta', M' + C' = 1,
M' > 0.71.  Margins: mu'_k := |theta'(u_k)| - vartheta' Phi_k for k in P', vartheta' = sigma' M'/C'; by [I, eq:margin]
sigma' |alpha'(k)| = lambda_k mu'_k.  A "pair at scale t" is any decomposition f' +- t g' = (a' +- t B+-) + L*(w' +- t Omega+-)
with both component norms <= 1 + e; for g' in C(f') one may take e = s(t) - 1 <= t^2/2 (Lemma 1.2 of N3 uses nothing
else).  Labels: PROVED / SKETCH / HEURISTIC / OPEN.

## 1. Supplement to Theorem 1.4 (attainment, left-continuity) — PROVED

LEMMA 1.  For every row f, M > 0, r >= 0 the supremum omega_f(M, r) is attained; omega_f(M, r) = M omega_f(1, r/M);
r -> omega_f(1, r) is nondecreasing and right-continuous; hence M -> omega_f(M, r) is left-continuous.
Proof.  The maps Delta -> L*Delta (V* -> l_1) is weak*-to-norm continuous on bounded sets (L compact, V separable), so
Delta -> ||L*Delta||_1 and Delta -> sum_J (1 - |z_j|)|(L*Delta)_j| are weak* continuous on bounded sets.  The feasible set
{||Delta|| <= M, leakage <= r} is weak* compact, so the sup is attained.  Scaling Delta = M Delta' gives the formula.  If
r_n decreases to r and Delta_n are maximizers at r_n, a weak* cluster point Delta has leakage <= r and ||L*Delta||_1 =
lim ||L*Delta_n||_1, so lim omega(1, r_n) <= omega(1, r) <= lim omega(1, r_n).  Left-continuity in M follows from the
scaling formula (r/M decreases as M increases).  QED

## 2. No exact visibility; the margin form of Theorem 2.3

LEMMA R-V (no exact visibility).  PROVED.  (a) For every coordinate j, {k : u_k(j) != 0} is infinite.  (b) At every row,
at most 1/alpha_0 peaks have |alpha'(k)| >= alpha_0.  (c) For every row f', every j, every mu_0 > 0, infinitely many k
with u_k(j) != 0 lie in N_{mu_0}(f') := Q' u {k in P' : mu'_k < mu_0}.
Proof.  (a) (T-d): every tail of (u_k) is dense in S_{q*}; G_j = {v in S_{q*} : v_j != 0} is relatively open and contains
e_j*/q*(e_j*).  (b) ||alpha'||_1 = 1.  (c) If |theta'(u_k)| < mu_0 then k in Q', or k in P' with mu'_k <= |theta'(u_k)|
< mu_0.  The set {v in S_{q*} : |theta'(v)| < mu_0, v_j != 0} is relatively open (theta' in l_inf is continuous on l_1)
and nonempty: if theta'_i != 0 for some i != j take v proportional to theta'_i e_j - theta'_j e_i; otherwise take v
proportional to eps e_j + e_i with eps small.  Every tail meets it.  QED
Consequently "Z exactly visible" (H = 0) in N3's Definition 2.1 never holds, and Corollary 2.4, Corollary 2.8, the
exact-visibility parts of Theorem 2.6(a) and Theorem 3.1(iii), and the sqrt(mu) law are vacuous for admissible T.

LEMMA W (weighted collective motion).  PROVED.  In N3's Lemma 2.2 (any row, pair at scale t in (0,1], e <= t^2/2), for
every peak k with mu'_k > 0:   lambda_k eps+-_k <= min( t/(2 mu'_k), 5 lambda_k / t ).
Proof.  Lemma 2.2 gives eps <= e/(t sigma' |alpha'(k)|) = e/(t lambda_k mu'_k) <= t/(2 lambda_k mu'_k); also
eps+_k = L+ - s_k Omega+(k) <= |L+| + |Omega+(k)| <= 2(2 + e)/t <= 5/t, and likewise eps-_k.  QED

LEMMA S (dyadic sum).  For t, mu_0 in (0,1]:  sum_{k >= 1} min(t/(2 mu_0), 5 lambda_k/t) <= t l(t)/mu_0,
l(t) := log_2(1/t) + 2.2.
Proof.  Put a = t/(2mu_0), b = 5/t, K := max(0, ceil(log_2(b/a)) - 1), so b 2^{-1-K} <= a.  As sum_{k > K} lambda_k <=
2^{-1-K}, the sum is <= K a + b 2^{-1-K} <= (K + 1) a, and K + 1 <= log_2(10/t^2) + 1 <= 2 log_2(1/t) + 4.33.  QED

THEOREM 2.3' (margin-classified profile bound).  PROVED.  Let f' be any row, g' in C(f'), j_f a free coordinate
(|z'_{j_f}| < 1) with psi'_{j_f} != 0, and S a finite set, j_f notin S, each of whose coordinates is either free, or a
support coordinate aligned at f', or aligned with |z'_j| >= 1/2.  For mu_0 in (0,1] put eta_j(mu_0) :=
sum_{k in N_{mu_0}(f')} lambda_k |u_k(j)|, mu_S := sum_{S n F'} |a'_j|, r_i := 1 - |z'_i| for free i, rho_S :=
||psi' 1_S||_1/|psi'_{j_f}|, H(mu_0) := rho_S eta_{j_f}(mu_0) + sum_S eta_j(mu_0), S_free := free coordinates of S.  Then
for every t in (0,1]:
   sum_{j in S} |g'_j - pi(j_f) psi'_j| <= t [ rho_S/(c' r_{j_f}) + 1/c' + sum_{S_free} 1/(c' r_j) + 2 (rho_S + |S|) l(t)/mu_0 ]
                                            + (2 mu_S + 15 H(mu_0))/t,          pi(j_f) := g'_{j_f}/psi'_{j_f}.
Proof.  Let R := P' \ N_{mu_0} (peaks with margin >= mu_0; possibly infinite).  Lemma 2.2 gives Omega+-(k) =
s_k(L+- -+ eps+-_k) on R.  Write psi'_j = M' sum_R lambda_k s_k u_k(j) + n_j with |n_j| <= eta_j(mu_0) (|w'| <= M' <= 1).
Then beta+-_j := (L*Omega+-)(j) = -d+- psi'_j + r+-_j with d+- := -L+-/M' and
   |r+-_j| <= (|L+-|/M' + ||Omega+-||_inf) eta_j(mu_0) + sum_R lambda_k eps+-_k |u_k(j)| <= 7.5 eta_j(mu_0)/t + t l(t)/mu_0
by Lemma W and Lemma S (|L|, ||Omega||_inf <= 2.5/t, M' > 0.71).  Hence B+-_j = g'_j + d+- psi'_j - r+-_j.
 Anchor: |pi(j_f) + d+-| <= (|B+-_{j_f}| + |r+-_{j_f}|)/|psi'_{j_f}| and r_{j_f}(|B+_{j_f}| + |B-_{j_f}|) <= t/c' (Lemma 1.2).
 Free i in S: |g'_i + d+ psi'_i| <= |B+_i| + |r+_i| with r_i |B+_i| <= t/(2c'); so |g'_i - pi(j_f) psi'_i| <= |B+_i| + |r+_i|
   + |psi'_i| |pi(j_f) + d+|.
 Aligned i in S (sigma_i := sgn psi'_i = sgn z'_i): exactly as in N3's proof, -d+ - X+_i <= pi(i) <= -d- + X-_i with
   |psi'_i| X+-_i = (sigma_i B+-_i)_-+ + |r+-_i|, and the B-terms over aligned i sum to <= t/c' + 2 mu_S/t (Lemma 1.2,
   |z'_i| >= 1/2 or i in F' with anti-sign allowance |a'_i|/t).
Combining as in N3 (multiply by |psi'_i| and sum) and inserting |r+-| gives the claim (each r-term contributes
7.5 eta/t + t l(t)/mu_0 per side; the anchor is used on both sides, hence the factors 2 and 15).  QED
Remarks.  (i) Compared with N3's Theorem 2.3, robust-margin peaks of arbitrarily small weight no longer enter the floor,
and the alpha_0-term (which grows like 1/(weight of the deepest robust peak)) is replaced by l(t) ~ log(1/t).
(ii) By Lemma R-V(c), H(mu_0) > 0 for every mu_0 > 0; the floor is now the weighted mass of NEAR-KERNEL carriers
(strict non-peaks and small-margin peaks), which margin sparsity controls.

## 3. Fatou inheritance, the correct strengthening of Cor S1, and what carries free-coordinate oscillation

LEMMA R-F (Fatou).  PROVED.  If f'_n -> f in S_{p*}, then for every j and mu_0 > 0:
   liminf_n eta_j(mu_0; f'_n) >= eta_j(mu_0; f).
Proof.  Fix k in N_{mu_0}(f).  By [I, prop:continuity], zeta_n(k) -> zeta(k), sigma_n -> sigma, M_n -> M, C_n -> C,
vartheta_n -> vartheta, theta_n(u_k) -> theta(u_k).  If k in Q(f): |zeta(k)|/sigma < Phi_k^2 M/C (off P, w = C zeta/(Phi^2 sigma)
and |w(k)| < M), a strict inequality that persists, and it excludes k in P_n (on P_n, |zeta_n(k)|/sigma_n = |alpha_n(k)|
+ Phi_k^2 M_n/C_n by [I, lem:threshold]); so k in Q_n eventually.  If k in P(f) with mu_k < mu_0: m_n := |theta_n(u_k)| -
vartheta_n Phi_k -> mu_k < mu_0; if m_n >= 0 then k in P_n with margin m_n < mu_0 eventually (m_n = 0: degenerate peak),
if m_n < 0 then k in Q_n.  So 1[k in N_{mu_0}(f'_n)] -> 1 for every k in N_{mu_0}(f); Fatou's lemma for the series
sum_k lambda_k |u_k(j)| 1[k in N_{mu_0}(f'_n)] gives the claim.  QED
COROLLARY (inheritance of every fixed-threshold sandwich).  PROVED.  For fixed mu_0, the lower bound on
dist_{l1}(rho g, C(f'_n)) produced by Theorem 2.3' through a fixed free coordinate j_f of f and a fixed S subset F u K
aligned at f has limsup <= (rho - 1) Osc_S(g; psi).  Proof: the bound is Osc_S(rho g; psi'_n) - m_n with m_n :=
inf_{t in (0,1]} [A_n(t) t + K_n/t]; A_n(t) -> A(t) pointwise (continuity of rho_S, c', r, mu_S), and liminf K_n >= K(f)
(Lemma R-F, mu_S(f'_n) -> mu_S(f)); so liminf m_n >= inf_t [A(t)t + K(f)/t] >= Osc_S(g; psi) (Theorem 2.3' at f).  QED

COROLLARY 2.4' (profile constancy at every row, for every mate, under a margin-sparsity RATE).  PROVED.
Let f' be any row, g' in C(f'), Z = S u {j_f} as in Theorem 2.3' with S n F' = {} (mu_S = 0), and put
eta_Z(mu_0) := sum_{k in N_{mu_0}(f')} lambda_k sum_{i in Z} |u_k(i)|.  If eta_Z(mu_0) = o(mu_0/log^2(1/mu_0)) as
mu_0 -> 0+, then g' = pi(j_f) psi' on Z.
Proof.  H(mu_0) <= (rho_S + 1) eta_Z(mu_0) =: (rho_S + 1) eta.  If eta = 0 for some mu_0 > 0 let t -> 0 in Theorem 2.3'
(t l(t) -> 0).  Otherwise take t := (eta mu_0)^{1/2} (<= mu_0 <= 1 for small mu_0, as eta = o(mu_0)).  With x := eta/mu_0:
the right side of Theorem 2.3' is <= A_0 (eta mu_0)^{1/2} + 2(rho_S + |S|) l(t) x^{1/2} + 15(rho_S + 1) x^{1/2}, where
l(t) = (1/2) log_2(1/x) + log_2(1/mu_0) + 2.2.  Now x^{1/2} log_2(1/x) -> 0, and x^{1/2} log_2(1/mu_0) -> 0 by the rate
hypothesis.  So the left side is 0.  QED
Remarks.  (i) The rate hypothesis implies that no strict non-peak and no degenerate peak sees Z (each would contribute a
constant to eta_Z(mu_0)); this is the analogue of "j notin Sigma(omega)" in [II, cor:II-S1], but no exact two-piece data
are needed and the row may have infinitely many contacts, near-contacts, degenerate peaks elsewhere, etc.
(ii) Unlike exact visibility, the hypothesis is satisfiable for admissible T: it says that carriers with
|theta'(u_k)| < mu_0 seeing Z first occur at depth >= log_2(1/mu_0) + 2 log_2 log(1/mu_0) + omega(1) (in the weighted
sense) — a sparse-visit property of the dense sequence relative to ker theta'.
(iii) Finite-model check (N3_ref_work/margin_check.py): with one extra carrier seeing S, Osc_max stays at grid level for
every positive margin (0.125 ... 2e-4) and jumps to 0.91-1.14 sqrt(H6) when the carrier crosses the threshold and becomes
a strict non-peak.

LEMMA R-W (what carries a free-coordinate oscillation).  PROVED.  Let f be any row, g in C(f), j, j' in J(f) with
psi_j psi_{j'} != 0 and pi_g(j) != pi_g(j').  Then eta_{{j,j'}}(mu_0; f) is not o(mu_0/log^2(1/mu_0)): either a strict
non-peak or a degenerate peak of f sees j or j', or the small-margin peaks of f seeing j, j' violate the log^2-margin-
sparsity rate.  Proof: Corollary 2.4' at f with j_f = j, S = {j'} (free).  QED

## 4. Repairs of Corollary 2.8 and Theorem 2.6(a) — PROVED

COROLLARY 2.8' (band dichotomy).  In the setting of N3's Theorem 2.7, with Osc_S(g'; psi') = kappa' > 0, for every t with
180 H_S/kappa' <= t <= kappa'/(8 A_S): mu_S >= kappa' t/8, or every pair at scale t has ||Delta Omega|| > M_t :=
max{M : omega_{f'}(M, t/c') <= kappa'} (attained by Lemma 1).  Proof: otherwise Theorem 2.7 gives kappa' <= kappa'/2 +
kappa'/8 + kappa'/8 + 2 mu_S/t.  QED  (Margin form: replace A_S by 1/c' + 3|S| l(t)/mu_0 and H_S by sum_S eta_j(mu_0).)

THEOREM 2.6(a') (aligned-or-banked, correct form).  Let f'_n -> f be rows, g'_n in C(f'_n), g'_n -> rho g, S aligned at
f with S subset K (mu_S(f) = 0), kappa := Osc_S(rho g; psi) > 0.  Call a free coordinate j of f'_n kappa-CLEAN (with clean
scale t_n(j) in (0,1]) if the hypotheses of Theorem 2.3 (fixed Lambda, alpha_0) or 2.3' (fixed mu_0) hold and
A_n(j) t + 15 H_n(j)/t <= kappa/2 at t = t_n(j).  Then for all large n: (i) mu_S(f'_n) >= kappa t_n(j)/8 for every
kappa-clean j; (ii) no j in J(f) with psi_j != 0 is kappa-clean at f'_n.  Hence clean coordinates are new, and their clean
scales tend to 0 (by (i), since mu_S(f'_n) -> 0).
Proof.  (i) Osc_S(g'_n; psi'_n) -> kappa (N3 Lemma 2.0(a),(b)), so it is >= 3kappa/4 for n >= n_0 independently of j;
Theorem 2.3/2.3' at t = t_n(j) gives 3kappa/4 <= kappa/2 + 2 mu_S/t.  (ii) If j in J(f) were clean along a subsequence,
15 H_n/t_n <= kappa/2 and liminf H_n >= H(f) > 0 (alpha-form: H is a T-property, > 0 by Lemma R-V; margin form: Lemma R-F
and Lemma R-V(c)) bound t_n below; a limit t_inf > 0 satisfies A(f) t_inf + 15 H(f)/t_inf <= kappa/2 (A_n -> A(f) by
N3 Cor 2.5).  Theorem 2.3/2.3' at f (mu_S(f) = 0) then gives Osc_S(g; psi) <= kappa/2 = rho Osc_S(g; psi)/2, absurd.  QED

## 5. Obstructions that N3's Theorem 2.6(b) does not address — PROVED

PROPOSITION X (exact mechanism at C-tame NA rows).  Let f' be NA with C-tame normer and s_3, s_4 notin Sigma'(f')
(= F' u union_{k in Q'} supp u_k), and h in X*.  Then dist_{p*}(h, C(f')) >= (2/3) |h(s_3) psi'(s_4) - h(s_4) psi'(s_3)|.
Proof.  Every g' in C(f') equals -d' psi' at s_3, s_4 (N3 Prop. 1.7(c)), so Lambda'(h) := h(s_3)psi'(s_4) -
h(s_4)psi'(s_3) vanishes at g'; |Lambda'(h)| <= ||h||_1 ||psi'||_inf <= ||h||_1/2 ([II, prop:II-S3]: ||psi'||_inf <= 1/2);
so ||h - g'||_1 >= 2|Lambda'(h)|; finally ||.||_1 <= 3 p*(.) ([II, prop:II-S3], proof).  QED
Consequences.  (a) [contacts] If pi_g is non-constant on K \ S, N3's banked truncations f'_{theta,N} (banks on the fixed
S only) satisfy, whenever C-tame with s_3, s_4 notin Sigma', dist_{p*}(rho g, C(f')) >= (2/3) rho |psi(s_3)psi(s_4)|
|pi_g(s_3) - pi_g(s_4)| - o(1).  Banking the whole oscillation set in [1, N] (summable masses) removes this; this is
what [I, def:engineered] does.  (b) [free coordinates] For j, j' in J(f) with pi_g(j) != pi_g(j') the same bound holds
at every C-tame NA f' near f with j, j' notin Sigma'(f'), and neither banks nor contacts can be placed at j, j' by rows near
f (z'_j -> z_j, |z_j| < 1).  The only escapes are covering (j or j' in supp u_k, k in Q'(f')) or non-C-tame approximants.
By status continuity, the strict non-peaks of f'_n of bounded depth are, for large n, strict non-peaks of f or former
degenerate peaks of f; all others have depth -> infinity.  (HEURISTIC continuation: their positive-scale capacity obeys
the sqrt-weight law — finite model: Osc_max ~ 1.14 sqrt(lambda |u|) — while Lemma R-W says the oscillation at f is carried
by small-margin peaks or by strict non-peaks/degenerate peaks of f.)

## 6. Numerics (sanity checks only; finite SOCP model, CLARABEL) — N3_ref_work/
 * floor_check.py: N3's 7-coordinate model + one carrier k6 seeing S = {1,2}.  Strict non-peak (u6 ~ e1 - e2):
   Osc_max(m = 0) = 4.6e-2, 2.3e-2, 1.0e-2 for lambda6 = 2e-3, 5e-4, 1e-4 (Osc/sqrt(H6) = 1.14, 1.14, 1.14).  Low-weight
   robust-margin peak (u6 ~ e1 - 0.5 e2): Osc_max(m = 0) = 1.9e-4, 0.9e-4, 1.8e-4 (baseline grid level 4.9e-5).  With banks
   m = 1e-4: 1.6e-2 to 1.9e-2 in both cases (N3 baseline 1.4e-2).
 * margin_check.py: u6 ~ e1 - (1 - delta) e2, lambda6 = 5e-4: margins 0.125, 0.018, 3.1e-3, 2.2e-4 (peak): Osc_max =
   8.7e-5, 8.6e-5, 1.8e-4, 6.2e-4; margins -3.2e-4, -4.6e-4, -5.0e-4 (strict non-peak): Osc_max = 1.85e-2, 2.26e-2,
   2.31e-2 (0.91-1.14 sqrt(H6)).  The small rise at margin 2.2e-4 is at the resolution of the t-grid (t >= 1e-5).
Interpretation: the floor of Theorem 2.3 is genuine and sharp in scaling for strict non-peaks, an artifact for peaks;
finite models satisfy the rate hypothesis of Cor 2.4' automatically, so they cannot exhibit weak-peak (non-(MS)) freedom.

## 7. Remarks (SKETCH) and open problems
 * SKETCH (route to N3's (b3) and to the eps-restriction of (b2)).  With Theorem 2.3' there is a single monotone parameter
   mu_0 instead of (Lambda, alpha_0).  For banked truncations (bank mass theta on S): (1) mu_0 below
   mu_min(theta) ~ theta l / Osc^2 gives A >= l/mu_0 so large that 2(2 theta A)^{1/2} >= Osc (bound vacuous);
   (2) free coordinates j of f with nu^tot_j <= tau(J_0(theta)) are handled by N3's (b1); (3) the remaining finitely many
   j and mu_0 in [mu_min, 1] are handled by Lemma R-F, monotonicity of eta(mu_0) in mu_0 and a Dini-type argument.  Not
   written out.
 * SKETCH (capacity upper bound at a FIXED row).  If at f' the peaks seeing Z satisfy the log^2 margin-sparsity rate and
   W_Z := weight of the strict non-peaks and degenerate peaks seeing Z (weighted by |u_k| on Z), then choosing
   mu_0 = mu_0(t) ~ t l(t) M(t) with M(t) -> infinity, M = o(log(1/t)), in Theorem 2.3' gives
   Osc_Z(g'; psi') <= 2 (15 A_0 W_Z)^{1/2} + delta_{f'}(W_Z), with delta_{f'}(W) -> 0 as W -> 0 at a rate depending on the
   margin-sparsity RATE of f'.  This is the sqrt-weight capacity law (finite model: constant 0.9-1.14) as an upper bound.
   A negative proof through Problem R needs it UNIFORMLY along approximants, i.e. a uniform margin-sparsity rate near Z —
   precisely what approximants can try to violate by tuning deep near-kernel carriers (u_k(x') ~ vartheta' Phi_k) seeing Z.
 * N3 Theorem 2.6(b3) (uniform inheritance over growing sets of free coordinates): SKETCH (see the first item).
 * N3 Problem 3.4 (junction certificate on contacts): OPEN.
 * PROBLEM R (free-coordinate version): OPEN.  Find admissible T, f, g in C(f), rho < 1 and j, j' in J(f) with
   pi_g(j) != pi_g(j'), carried (Lemma R-W) only by small-margin peaks of f, such that no NA sequence f'_n -> f recovers
   rho g: i.e. along every such sequence, either the constancy hypotheses (C-tameness off Sigma', or the rate of Cor 2.4')
   hold at {j, j'}, or the near-kernel carriers of f'_n seeing j, j' have too little capacity below the slack scale.  A
   negative proof needs a capacity LOWER-bound theory (none exists) and must defeat the plausible positive mechanism of
   infinitely many near-threshold carriers tuned by far moves (nested tuning, cf. U3 rows f^infty), presumably through
   far rigidity of T.
