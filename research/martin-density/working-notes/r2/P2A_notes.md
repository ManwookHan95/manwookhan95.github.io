# P2 notes — engineered recovery of mates that use ONE-SIDED resources (replication–averaging–transfer)

Round 2, task P2. Setting: canonical base q, Martin's norm with a FINITE block set I (p_N; Preprint B Remark martin-tail), only Lemma B's
conclusion about T. Imports: A_notes Facts A–F, Lemmas 4.2–4.7, 7.1–7.2, Thms 4.10, 6.5 (refereed, with referee fix G1: coordinatewise
radius); N_part1 Thm 1 (density <=> Ls(f) = C(f) for all f; g in Ls(f) <=> (f, rho g) in cl NA for all rho < 1); P1 2.1–2.3, 6.1–6.2 (refereed).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Part files P2_part1..5.md (assembled below). Scripts: ctx/r2/P2work/.

## 0. Summary

**Main theorem (PROVED, Thm 2.1).** Let f in S_{p*} have finite base support F, and let g in C(f) admit one-sided linear ("two-piece")
decompositions on the two sides of t = 0 whose block parts are finitely supported strictly below the peaks and whose base parts live on
F and the contact set K with the contact signs, with EQUAL d-coefficients on the two sides (d-neutral transfer v = b+ - b-). If one block
is active (or several, under a span hypothesis (S)), then (f, rho g) is in cl NA((c_0,p), l_2^2) for every rho with rho^2 kappa < 1, and for every
rho < 1 when the decompositions are locally admissible. No assumption on K (it may be infinite), on the split of the contact mass between
the sides (non-constant splits allowed), on rates of T, or on the deep block structure of f is needed.
This makes A_referee §5.4 and P1 Prop 6.3 rigorous (Cor 2.3): all explicit defect mates of P1's example (P1 Thm 2.4) and the whole slab of
P1 6.2 lie in Ls(f). The recovering approximants are ENGINEERED (window masses on contacts, far flipped contacts with negative masses,
one raising mass, a theta-tail of the target), as they must be: P1-referee R3 shows these mates are not recovered along canonical truncations.

**Mechanism.** (1) Exact transfer: after recomputing d-coefficients at f' the one-sided decompositions of f transfer to f' with NO first-order
error (Remark 2.2(a)); (2) steering: one scalar condition per block, v_m(x') = 0, forces both sides to represent the same g' (pull by flipped
far contacts with negative masses, raise by one mass, intermediate value theorem); (3) theta-tail: beyond the window the target equals the
two-sided theta-combination, so the small-scale certificate needs masses only on finitely many contacts; (4) slack only for |t| >= T_0 (fixed).
No averaging is needed for this class; Lemma 1.5 (averaging over scales, PROVED) is required only for scale-dependent mates (part 4).

**Answers to the specific questions.**
* Mixed term delta t <P_perp U*e_j, P_perp U*B_t>/||U*a|| (3.1, PROVED): it is the first-order shift of the base part caused by a contact mass.
  For one decomposition it is absorbed by normalizing g'(x') = 0; for two pieces its difference is cancelled EXACTLY by the steering
  condition (Thm 2.1, Step 1) — not an obstruction; for finitely many pieces, finitely many steering conditions; for a continuum of
  scale-dependent pieces it is equivalent (3.2, PROVED identity) to exact replication of infinitely many relative block positions, which is
  where it becomes an obstruction (quantified by (QI), 4.4; OPEN).
* Non-zero d-mismatch (A_referee §5.5): PROVED garbage identity (3.3): the only change is E = -sum Delta d_m R_m*(w'_m - w_m), which must be
  <= eps_0 s_1 in l_1. With finitely many strict non-peaks/degenerate peaks, margin sparsity and a tuning span condition this holds (Thm 3.4,
  SKETCH with all estimates) — so A_referee's "engineering breaks when d != 0" is too pessimistic: what breaks it is infinitely many
  strict non-peaks (or dense near-threshold peaks) in the active block, where deep retuning ((QI)) is needed.
* C's "implant scale gap" (4.5): arithmetic correct; as an obstruction FALSE — Thm 2.1 is a rigorous instance with p*(f'-f) >~ s_1 >> s_1^2
  where the window (s_1, sqrt(p*(f'-f))) is covered by exact transfer. It correctly locates the difficulty for scale-dependent mates ((QI)).
* For which mates can regime (ii) be supplied (4.4(4)): base one-sided usage — always (contact masses; price: steering); off-peak carriers
  with gap — always (replicate finitely many ratios); block one-sided carriers (weak/degenerate peaks, near-threshold, coordinates pushed
  beyond their gap, deep coordinates) — degenerate peaks by one tuning move each (SKETCH); the others only through implanted gaps on
  carriers with rates ||u_k - v|| <~ Phi_k, compatible with replication only under (QI) (OPEN); components carried one-sidedly by block
  resources WITHOUT rates and without a contact representation cannot be supplied by certificates at C-tame approximants (P1-referee R1).
* Exact residual class (4.6): (R1) non-neutral two-piece data at non-tame active blocks; (R2) several active blocks without (S);
  (R3) two-piece data needing shifts (Rem 2.4, SKETCH); (R4) infinite F (near-flips); (R5) genuinely scale-dependent switching
  (approximate resonances) — reduced by the abstract scheme 4.3 to (QI) + implant compatibility, OPEN and T-dependent.
* Density of NA((c_0,p), l_2^2): still OPEN. Nothing here suggests a counterexample: every concrete defect mate known (P1) is recovered.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Clamp formula w(k) = sgn zeta(k) min(M, C r(k)) | PROVED (+numerics) | 1.1 |
| 2 | Convergence of block data along engineered approximants | PROVED | 1.2 |
| 3 | First-order identity at NA points; two-regime assembly; averaging over scales at a fixed point | PROVED | 1.3–1.5 |
| 4 | One-sided admissibility => kappa <= 1 | PROVED | 1.7 |
| 5 | **Engineered recovery of d-neutral two-piece mates** (any K, any split; one block, or (S)) | PROVED (+finite-model check) | 2.1 |
| 6 | A_referee §5.4 and P1 6.3 rigorous; slab and explicit defect mates of P1's example in Ls(f) | PROVED | 2.3 |
| 7 | Shifted two-piece data; all of C(f) at P1's example | SKETCH | 2.4 |
| 8 | Mixed term: formula; absorbed (1 piece), cancelled by steering (2 pieces) | PROVED | 3.1 |
| 9 | Consistency identity for families of transported decompositions | PROVED | 3.2 |
| 10 | Garbage identity for Delta d != 0 | PROVED | 3.3 |
| 11 | Delta d != 0 at block-tame active blocks (finite Qbar, (MS), tuning span) | SKETCH | 3.4 |
| 12 | Replication identity (exact |C'-C| and ||R*(w'-w)|| bounds) | PROVED | 4.1 |
| 13 | Retuning feasibility = restricted radius (duality) | PROVED | 4.2 |
| 14 | Abstract replication–averaging–transfer scheme | PROVED (implication) | 4.3 |
| 15 | Requirements for scale-dependent mates; (QI) | identities PROVED / necessity HEURISTIC / (QI) OPEN | 4.4 |
| 16 | C's implant-scale-gap heuristic as an obstruction | FALSE (Thm 2.1 is a counter-instance) | 4.5 |
| 17 | Residual class R1–R5 | OPEN | 4.6, 3.5 |

# P2 part 1: setting, conventions, and the engineering toolkit

Setting: canonical base q (B_q = B_{c_0} + U(B_H), U: H -> c_0 compact with dense range, U* injective), Martin's norm with a
FINITE block set I (p_N; Preprint B Remark martin-tail). Notation of A_notes §1, §4. Imports (all refereed in Round 1/2):
(T1)-(T4), A Facts A-F, A Lemmas 4.2, 4.3, 4.4, 4.7, 7.2, A Prop 4.5, A Thm 6.5, N_part1 Thm 1 (Ls(f) = C(f) for all f iff density;
g in Ls(f) iff (f, rho g) in cl NA for all rho < 1). s(t) := sqrt(1 + t^2). Only Lemma B's conclusion is used about T.
For f in S_{p*}: forced data xi, q_0, a, w = (w_m), z, e = U*a/nu, nu = ||U*a||, zhat = z + U e = xi/q_0, zeta_m = R_m** xi,
M_m, C_m, P_m, alpha_m; F := supp a; K := {j notin F : |z_j| = 1} (contacts); J_gamma := {j notin F : |z_j| <= 1 - gamma}.
For an NA point f' = grad p(x') (x' in S_p) the same notation with primes; xhat' := x'/q(x') = z' + U e' (A Fact D).
All facts of A §1 (Fact C, Lemma 4.2, Lemma 4.4, Lemma 7.2) hold at NA points with xi replaced by x' (they only use f in S_{p*}
and its normer).

## 1.1 Lemma (clamp formula). PROVED.
For f in S_{p*}, every block m and every k:
   w_m(k) = sgn(zeta_m(k)) * min( M_m , C_m r_m(k) ),     r_m(k) := |zeta_m(k)| / (Phi_m(k)^2 |zeta_m|_m) = m |u_{k,m}(xi)| / (Phi_m(k) |zeta_m|_m),
with sgn(0) = 0. In particular k is a peak iff C_m r_m(k) >= M_m, and w_m(k) depends on xi only through the ratio
u_{k,m}(xi)/|zeta_m|_m and the scalar C_m (M_m = 1 - C_m).
*Proof.* A Fact C: zeta/|zeta| = alpha + D^2 w/C with alpha supported on P, sign alpha_k = sign w(k), so for k in P,
|zeta(k)|/|zeta| = |alpha_k| + Phi_k^2 M/C >= Phi_k^2 M/C, i.e. C r(k) >= M, and sign zeta(k) = sign w(k) (both summands have
the sign of w(k) != 0). Off P: w(k) = C zeta(k)/(Phi_k^2|zeta|), so |w(k)| = C r(k) < M. If zeta(k) = 0 then k is not a peak
(peaks have |zeta(k)| > 0) and w(k) = 0. QED.

## 1.2 Lemma (convergence of block data along engineered approximants). PROVED.
Let xhat_n = z'_n + U e_n be bounded in l_infinity with xhat_n -> zhat weak* (i.e. z'_n -> z coordinatewise boundedly and
e_n -> e in H), and let a_n in c_00 cap S_{q*} with a_n(xhat_n) = 1 = q(xhat_n), a_n -> a in l_1. Put f_n := grad p(xhat_n)
= a_n + L* J_V(L xhat_n) (NA, A Fact D). Then f_n -> f in norm, w_{n,m}(k) -> w_m(k) for every (k,m), C_{n,m} -> C_m,
M_{n,m} -> M_m, |R_m xhat_n|_m -> |R_m** zhat|_m, D_m w_{n,m} -> D_m w_m in l_2, R_m* w_{n,m} -> R_m* w_m in l_1.
*Proof.* L is compact, so L xhat_n -> L** zhat in V (norm); each block R_m** zhat != 0 (T3), J_m is norm-to-weak* continuous at
nonzero points (smoothness of |.|_m), hence w_{n,m} = J_m(R_m xhat_n) -> w_m weak*; D_m, R_m* are compact (weak*-to-norm on
bounded sets). J_V is homogeneous of degree 0, so grad p(xhat_n) = grad p(xhat_n/p(xhat_n)). Norm convergence of f_n:
a_n -> a and L* J_V(L xhat_n) -> L* w. (This is G_referee 4.7 (ii) => (i), steps 1-5.) QED.
Remark. Lemma 1.2 is used in "sequential" form: all engineered approximants below come in sequences indexed by the
construction parameters, and every such sequence satisfies the hypotheses of 1.2. Any requirement of the form
"datum(f') is within eps of datum(f)" for finitely many convergent data is therefore met at a late stage of the sequence,
uniformly with respect to the other (coupled) choices made at the same stage.

## 1.3 Lemma (first-order identity at an NA point). PROVED.
Let f' = grad p(x') be NA with data (a', w', z', e', nu', xhat'), g' in X* with g'(xhat') = 0, and suppose
g' = B + sum_m R_m*(omega_m - d'_m w'_m) with omega_m finitely supported and vanishing on the peak set P'_m,
d'_m := <D w'_m, D omega_m>/C'_m. Then B(xhat') = 0, and for every real tau
   q*(a' + tau B) = 1 + Fl'_B(tau) + Kink'(tau B) + nu' Psi'(tau U*B/nu'),
where Kink'(y) := sum_{j notin supp a'} (|y_j| - z'_j y_j) >= 0, Fl' and Psi' are those of A Lemma 4.3/7.2 at f' (Psi' with e').
*Proof.* A Lemma 4.2 at f': <omega_m - d'_m w'_m, R_m x'> = 0. Hence B(x') = g'(x') = 0 and B(xhat') = 0. The identity is A
Lemma 7.2 at f' (E_q(a' + tau B) = q*(a' + tau B) - (a' + tau B)(xhat') and a'(xhat') = 1). QED.

## 1.4 Lemma (assembly in two regimes). PROVED.
Let f, f' in S_{p*}, g in C(f), rho in (0,1), g' in X*, and 0 < T_0 <= 1. Suppose
 (i) p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta) for 0 < |tau| <= T_0, where 0 < delta <= 1 and T_0^2 <= 3 delta;
 (ii) p*(f' - f) <= (1 - rho^2) T_0^2/6 and p*(g' - rho g) <= (1 - rho^2) T_0/6.
Then g' in C(f'). If moreover f' is NA, then (f', g') in NA((X,p), l_2^2) and ||(f',g') - (f, rho g)|| <= p*(f'-f) + p*(g'-rho g).
*Proof.* For |tau| <= T_0: 1 + (tau^2/2)(1 - delta) <= 1 + tau^2/2 - tau^4/8 <= s(tau), since tau^2 delta/2 >= tau^4/8 iff
tau^2 <= 4 delta, and sqrt(1+x) >= 1 + x/2 - x^2/8. For |tau| >= T_0: p*(f' + tau g') <= p*(f + tau rho g) + p*(f'-f) + |tau| p*(g' - rho g)
<= s(rho tau) + (1-rho^2)(T_0^2 + |tau| T_0)/6 <= s(tau) by A Lemma 4.7 (s(tau) - s(rho tau) >= (1-rho^2) min(tau^2,|tau|)/3) as in the
proof of A Prop 4.8. NA: KLMW (A Lemma 1.2 of N_part1). QED.

## 1.5 Lemma (averaging over scales at a fixed point; E_part2 §2.1). PROVED.
Let f' in S_{p*}, gbar, h_1, ..., h_J in X*, s_j := s_1 2^{1-j}, Q, kappa >= 0 and 0 < s_1 <= T_0 with
 (i) p*(f' + t h_j) <= 1 + Q t^2/2 for |t| <= s_j;  (ii) p*(f' + t gbar) <= 1 + Q t^2/2 for s_J <= |t| <= T_0;
 (iii) p*(h_j - gbar) <= kappa s_j.
Then g' := (1/J) sum_j h_j satisfies p*(f' + t g') <= 1 + (Q + 4 kappa/J) t^2/2 for |t| <= T_0, and p*(g' - gbar) <= 2 kappa s_1/J.
*Proof.* Convexity: p*(f' + t g') <= (1/J) sum_j p*(f' + t h_j). For s_j >= |t| use (i); for s_j < |t| (then |t| >= s_J) use
p*(f' + t h_j) <= p*(f' + t gbar) + |t| kappa s_j and (ii). Since sum_{s_j < |t|} s_j <= 2|t|, the extra term is <= 2 kappa t^2/J. QED.
(Lemma 1.5 is only needed for scale-dependent mates, part 4; the main theorem of part 2 needs no averaging.)

## 1.6 Notation for one-sided linear decompositions ("two-piece data").
Let f in S_{p*} with F finite. Two-piece data for g in X* consist of a finite set I_0 of blocks and
  (b+, omega+), (b-, omega-):  b+- in l_1, omega+-_m in c_00 (m in I_0), supp omega+-_m cap P_m = empty,
  d+-_m := <D_m w_m, D_m omega+-_m>/C_m,
  g = b+ + sum_{m in I_0} R_m*(omega+_m - d+_m w_m) = b- + sum_{m in I_0} R_m*(omega-_m - d-_m w_m),
  supp b+- in F cup K,  z_j b+_j >= 0 and z_j b-_j <= 0 for j in K.
Derived objects: omega_Delta,m := omega-_m - omega+_m, Delta d_m := d-_m - d+_m = <D w_m, D omega_Delta,m>/C_m,
  v_m := R_m* omega_Delta,m (in Y),  v := b+ - b- = sum_m v_m - sum_m Delta d_m R_m* w_m  (in Y cap l_1(F cup K), z-signed on K).
The data are d-NEUTRAL if Delta d_m = 0 for all m (then v = sum_m v_m). For theta in [0,1]:
  b_theta := (1-theta) b+ + theta b- = b+ - theta v,  omega_theta := (1-theta) omega+ + theta omega-,  d_theta = (1-theta)d+ + theta d-.
Coefficients: h(b) := ||P_{e-perp} U*b||^2/nu (A Def 4.1), H_m(omega) := (||D_m omega||^2 - <D_m w_m, D_m omega>^2/C_m^2)/C_m,
  kappa(data) := max( h(b+), h(b-), max_{m in I_0} H_m(omega+_m), max_m H_m(omega-_m) ).
Since h and H_m are positive semidefinite quadratic forms (convex), h(b_theta) <= max(h(b+),h(b-)) and H_m(omega_theta) <= max(H_m(omega+),H_m(omega-)).
Automatic facts (PROVED): b+-(zhat) = 0 (from g(xi) = 0 and A Lemma 4.2: <omega - d w, zeta_m> = 0); v(zhat) = 0; if v = 0 then
omega_Delta = 0 (L* injective) and b+ = b-, so g has a two-sided linear decomposition.

## 1.7 Lemma (one-sided admissibility gives kappa <= 1). PROVED.
If, in addition, for some tau_0 > 0: q*(a + tau b+) <= s(tau) and N_m(w_m + tau(omega+_m - d+_m w_m)) <= s(tau) for 0 <= tau <= tau_0,
and the same with (b-, omega-) for -tau_0 <= tau <= 0, then kappa(data) <= 1.
*Proof.* Base, side +: by A Lemma 7.2 with first-order term b+(zhat) = 0 and nonnegative flip and kink terms,
q*(a + tau b+) >= 1 + nu Psi(tau U*b+/nu) >= 1 + (tau^2/2) h(b+)/(1 + tau ||U*b+||/nu) (A Lemma 4.3, valid when tau||U*b+|| <= nu/2);
comparing with s(tau) <= 1 + tau^2/2 and letting tau -> 0+ gives h(b+) <= 1. Blocks, side +: A Lemma 4.4(b) (valid for small tau >= 0:
1 - d tau > 0, Y > 0) gives 1 + tau^2||h_perp||^2/(sqrt(Y^2 + tau^2||h_perp||^2) + Y) <= s(tau), and tau -> 0+ (Y -> C) gives
||h_perp||^2 <= C, i.e. H_m(omega+_m) <= 1. Side - symmetric. QED.
# P2 part 2: engineered recovery of d-neutral two-piece (switching) mates

## 2.1 Theorem (engineered recovery of d-neutral two-piece mates). PROVED.
Let f in S_{p*} with F = supp a finite, let g in C(f) carry d-NEUTRAL two-piece data (part 1, 1.6) with coefficient
kappa = kappa(data), and let rho in (0,1) with rho^2 kappa < 1. If |I_0| >= 2 assume the steering hypothesis
 (S) there are gamma > 0 and finitely many coordinates j_1, ..., j_r in J_gamma such that the vectors (v_{m,j_i})_{m in I_0}
     span H_0 := {y in R^{I_0} : sum_m y_m = 0}.
(For j notin F cup K, sum_m v_{m,j} = v_j = 0, so these vectors always lie in H_0.) Then (f, rho g) is in cl NA((c_0,p), l_2^2).
If the data are one-sided admissible (Lemma 1.7), this holds for every rho < 1, i.e. g is in Ls(f) (N_part1 Thm 1).
No condition on K (it may be infinite), on the split of the contact mass between the two sides, on the rates of T, or on the
number of strict non-peaks of f is needed.

*Proof.* If v = 0 then b+ = b- is both z-signed and (-z)-signed on K, hence vanishes on K and is supported in the finite set F;
omega+ = omega- (L* injective). So c := (b+, omega+) is a finite certificate (A Def 4.1) with g_c = g and H(c) <= kappa; rho g is in C(f)
(convexity) and H(rho c) = rho^2 kappa < 1, so rho g in Cert(f), recovered along every sequence (A Thm 4.10). Assume v != 0.
Write theta := 1/2, b^+ := b+, b^- := b-, b^theta := b_theta, and similarly omega^sigma (sigma in {+, -, theta}); all three
share d_m := d+_m = d-_m (d-neutrality), and
   g = b^sigma + sum_{m in I_0} R_m*(omega^sigma_m - d_m w_m),   b^+ = b^theta + theta v,  b^- = b^theta - (1-theta) v.   (2.1.1)

Step 0 (constants depending only on f, g, rho). delta := (1 - rho^2 kappa)/2 in (0, 1/2]; eps_0 := delta/8.
gamma_0 := min{ gap_m(k) : m in I_0, k in supp omega^sigma_m, sigma } > 0; a_min := min_{j in F} |a_j|;
beta_max := max_sigma ||b^sigma||_infinity + 1; Kc := 4 max_sigma max( ||U|| ||b^sigma||_1/nu + 1, max_m |d_m| M_m/C_m + 1 ).
Raising coordinate: v is in Y \ {0}, so v is not in R a (a in c_00, Y cap c_00 = {0}); since U* is injective, U*v is not parallel
to U*a, i.e. P_{e-perp} U*v != 0. As v is supported in F cup K and z-signed on K,
   sum_{j in F} v_j <P_{e-perp}U*v, U*e_j*> + sum_{j in K} |v_j| <P_{e-perp}U*v, z_j U*e_j*> = ||P_{e-perp}U*v||^2 > 0
(U*v = sum_j v_j U*e_j* converges in H). Hence there are j_+ and s_+ in {-1, 1} with s_+ = z_{j_+} if j_+ in K (any sign if
j_+ in F) such that gamma_+ := s_+ <P_{e-perp}U*v, U*e_{j_+}*>/nu > 0. By continuity of a'' -> <U*v, P_{e(a'')-perp}U*e_{j_+}*>/||U*a''||
(e(a'') := U*a''/||U*a''||) at a'' = a there is r_+ > 0 with s_+ <U*v, P_{e(a'')-perp}U*e_{j_+}*>/||U*a''|| >= gamma_+/2 whenever ||a'' - a||_1 <= r_+.
Choose T_0 in (0,1] with
   T_0^2 <= 3 delta,  rho T_0 beta_max <= a_min/8,  Kc T_0 <= 1,  (rho^2 kappa + delta/8)(1 + Kc T_0) <= rho^2 kappa + delta/4,
   rho T_0 <= min_sigma r_sigma/2  (r_sigma := coordinatewise radius at f of the block certificate omega^sigma, A Lemma 4.4(d) with
   referee fix G1: min over m, k of gap_m(k)/(2|omega^sigma_m(k)|), 1/(2|d_m|), C_m/(2|d_m|M_m)),
   16 rho T_0 ||U|| ||U*v|| <= nu.
(Kc bounds, at late stages, both 2||U*B^sigma||/nu' and 2 rho|d'_m|M'_m/C'_m; Kc T_0 <= 1 also gives |tau| ||U*B^sigma|| <= nu'/2.)
Put A_0 := 8 rho ||U|| ||U*v|| ||b^theta||_1/nu + 1.

Construction (parameters chosen in the order N, s_1, Far, N'', mu, p; each later choice may depend on the earlier ones):
 (C1) Window N >= max(F cup {j_+} cup {j_1,...,j_r}). Put tau_N := sum_{j in K, j > N} |v_j| > 0 (v is not in c_00 and lives on
      F cup K with F inside [1,N]) and eps_N := sup_{j > N} |v_j|.
 (C2) Small scale s_1 in (0, T_0] with 4 A_0 s_1 <= tau_N.
 (C3) Window masses m_j := 4 rho s_1 |b^theta_j| for j in K cap [1,N].
      Far set: Far := K cap (N, N_2] with N_2 minimal such that V_Far := sum_{j in Far} |v_j| >= 2 A_0 s_1 (exists by (C2));
      then V_Far <= 2 A_0 s_1 + eps_N. Far masses m'_j := 4 rho T_0 |v_j| (j in Far).
 (C4) Cut-off N'' > N_2 with V_{>N''} := sum_{j in K, j > N''} |v_j| <= eps_0 s_1/rho.
 (C5) For mu >= 0 and p in [-gamma, gamma]^r:
        a''(mu) := a + sum_{j in K cap [1,N]} m_j z_j e_j* - sum_{j in Far} m'_j z_j e_j* + mu s_+ e_{j_+}*,   a' := a''/q*(a''),
        z'_j := z_j on [1,N''] \ (Far cup {j_1..j_r}),  z'_j := -z_j on Far,  z'_{j_i} := z_{j_i} + p_i,  z'_j := 0 for j > N'',
        e' := U*a'/||U*a'||,  xhat' := z' + U e',  x' := xhat'/p(xhat'),  f' := grad p(x') = a' + sum_m R_m* w'_m  (NA).
      Compatibility (A Fact D): z' is in c_00, ||z'||_inf <= 1, and z' = sign a' on supp a' = F cup {window contacts with m_j > 0}
      cup Far (cup {j_+} if mu > 0): on F, z = sign a and the mass at j_+ in F keeps the sign if mu <= |a_{j_+}|/2; on window contacts
      z'_j = z_j = sign(m_j z_j); on Far z'_j = -z_j = sign(-m'_j z_j); j_+ in K gets mass of sign z_{j_+} = z'_{j_+}. Hence
      q(xhat') = a'(xhat') = 1 and f' is norm attaining.

Step 1 (steering: exact carriers). Psi(mu) := v(xhat'(mu, p)) does not depend on p (v_j = 0 at the free coordinates j_i).
Since v(zhat) = 0:  v(xhat') = v(z' - z) + <U*v, e' - e>, and, because z_j v_j = |v_j| on K, v_j = 0 off F cup K, F in [1,N]:
   v(z' - z) = -2 V_Far - V_{>N''}.
Lipschitz bound ||e(a'') - e|| <= 2||U|| ||a'' - a||_1/nu (from ||x/|x| - y/|y||| <= 2|x - y|/|y| and ||U*y|| <= ||U|| ||y||_1):
   |<U*v, e(a''(0)) - e>| <= (2||U|| ||U*v||/nu)(4 rho s_1 ||b^theta||_1 + 4 rho T_0 V_Far) <= A_0 s_1 + V_Far/2 <= V_Far
(by the choice of T_0 and V_Far >= 2A_0 s_1). Hence Psi(0) <= -2V_Far + V_Far = -V_Far < 0 and |Psi(0)| <= 4 V_Far.
Let mu_max := 8 V_Far/gamma_+. At late stages (s_1, eps_N small) ||a''(mu) - a||_1 <= r_+ and mu_max <= |a_{j_+}|/2 (if j_+ in F) for
mu in [0, mu_max]; then by the mean value theorem Psi(mu_max) >= Psi(0) + mu_max gamma_+/2 >= 0. Psi is continuous, so there is
mu_* in [0, mu_max] with Psi(mu_*) = v(xhat') = 0. Fix mu := mu_*.
If |I_0| >= 2: y := (v_m(xhat'(mu_*, 0)))_{m in I_0} lies in H_0 (its sum is v(xhat') = 0, d-neutrality). Let A: R^r -> H_0,
A p := sum_i p_i (v_{m,j_i})_m (onto by (S)) with a fixed linear right inverse A^+. Since v_m(zhat) = <omega_Delta,m, zeta_m>/q_0 =
|zeta_m| Delta d_m/q_0 = 0 (A Fact C), and xhat' -> zhat weak* along the construction (Step 3), y -> 0; at late stages
p := -A^+ y has |p_i| <= gamma, and then v_m(xhat') = y_m + (A p)_m = 0 for every m in I_0 (changing z' at the j_i is affine and does
not change e' or v(xhat')). Result: v_m(xhat') = 0 for all m in I_0.

Step 2 (the target and its three decompositions). d'^sigma_m := <D w'_m, D omega^sigma_m>/C'_m. At late stages supp omega^sigma_m
avoids P'_m (Step 3), so by Lemma 1.1 at f' (w'(k) = C' lambda_k u_k(x')/(Phi_k^2 |zeta'_m|) off P'):
   <D w'_m, D omega_Delta,m> = (C'_m/|zeta'_m|) v_m(x') = 0,  hence d'^+_m = d'^-_m = d'^theta_m =: d'_m.
Define g'' := b^theta 1_{[1,N]} + sum_{m in I_0} R_m*(omega^theta_m - d'_m w'_m), c := g''(xhat'), g' := rho (g'' - c a'), so g'(xhat') = 0.
For sigma in {+, -, theta} put B^sigma := g' - rho sum_m R_m*(omega^sigma_m - d'_m w'_m). Since omega^theta - omega^+ = theta omega_Delta,
omega^theta - omega^- = -(1-theta) omega_Delta and the d'-terms coincide:
   B^theta = rho(b^theta 1_{[1,N]} - c a'),  B^+ = B^theta + rho theta v,  B^- = B^theta - rho(1-theta) v.   (2.1.2)
Write B^sigma = rho(beta^sigma - c a') with beta^theta = b^theta 1_{[1,N]}, beta^+ = b^+ 1_{[1,N]} + theta v 1_{(N,inf)},
beta^- = b^- 1_{[1,N]} - (1-theta) v 1_{(N,inf)} (by (2.1.1)). Then f' + tau g' = (a' + tau B^sigma) + sum_m R_m*(w'_m + tau rho(omega^sigma_m - d'_m w'_m))
for every sigma and tau, so by A Fact A
   p*(f' + tau g') <= max( q*(a' + tau B^sigma), max_{m in I_0} N_m(w'_m + tau rho(omega^sigma_m - d'_m w'_m)) ).   (2.1.3)

Step 3 (convergence along the construction). Along any sequence of constructions with N -> infinity (hence s_1, V_Far, mu_*, |p| -> 0):
the total mass ||a'' - a||_1 <= 4 rho s_1 ||b^theta||_1 + 4 rho T_0 (2A_0 s_1 + eps_N) + mu_max -> 0, so a' -> a, e' -> e; z' -> z coordinatewise
(z' = z on [1,N] except at the fixed j_i, where |p_i| -> 0; Far lies beyond N). Lemma 1.2: f' -> f, w'_m(k) -> w_m(k), M', C', |zeta'| converge.
Consequences at late stages: gap'_m(k) >= gamma_0/2 on supp omega^sigma (so these coordinates are off-peak at f'); d'_m -> d_m;
H'_m(omega^sigma_m) -> H_m(omega^sigma_m); g'' -> g in l_1 (g'' - g = -b^theta 1_{(N,inf)} + sum_m R_m*(d_m w_m - d'_m w'_m)); c = (g'' - g)(xhat') + g(xhat') -> g(zhat) = 0;
g' -> rho g; beta^sigma -> b^sigma in l_1 (beta^+ - b^+ = -b^theta 1_{(N,inf)}, similarly for -), so B^sigma -> rho b^sigma; nu' -> nu and
h'(B^sigma) := ||P_{e'-perp} U*B^sigma||^2/nu' -> rho^2 h(b^sigma).

Step 4 (cost of the block parts). A Lemma 4.4(c),(d) at f' (coordinatewise radius, referee fix G1) for the certificate rho omega^sigma_m:
for |tau| <= T_0 (<= r_sigma/(2 rho) <= coordinatewise radius at f' at late stages),
   N_m(w'_m + tau rho(omega^sigma_m - d'_m w'_m)) <= 1 + (rho^2 tau^2/2) H'_m(omega^sigma_m)(1 + 2 rho |tau d'_m| M'_m/C'_m).
Blocks m notin I_0 contribute N_m(w'_m) = 1.

Step 5 (cost of the base parts). Lemma 1.3 applies (g'(xhat') = 0, supp omega^sigma off P'): q*(a' + tau B^sigma) = 1 + Fl' + Kink' + nu' Psi'.
Use sigma = theta for |tau| <= s_1 and sigma = sign(tau) for s_1 <= |tau| <= T_0. Late stages: |tau rho c| <= 1/2 and 1/2 <= q*(a'') <= 2.
 (a) No sign flips. On supp a', a'_j + tau B^sigma_j = (1 - tau rho c) a'_j + tau rho beta^sigma_j. j in F: |a'_j| >= a_min/4 (also at j_+ in F, as
     mu <= |a_{j_+}|/2) and |tau rho beta^sigma_j| <= rho T_0 beta_max <= a_min/8. Window contacts with mass: for sigma = theta, |tau| <= s_1:
     |tau rho beta^theta_j| <= s_1 rho |b^theta_j| = m_j/4 <= |a'_j|/2; for sigma = +, tau > 0: beta^+_j = b+_j has z_j b+_j >= 0, so tau beta^+_j has
     the sign z_j = sign a'_j; sigma = -, tau < 0: beta^-_j = b-_j, z_j b-_j <= 0, same conclusion. j_+ in K: as for window contacts
     (its mass has sign z_{j_+}). Far: |a'_j| >= m'_j/2 = 2 rho T_0 |v_j| >= 2|tau rho beta^sigma_j| (|beta^sigma_j| <= |v_j| there, beta^theta_j = 0).
     Hence Fl' = 0 in all cases.
 (b) Kinks (j notin supp a'). Non-contacts j in J := N \ (F cup K) (including the j_i): beta^sigma_j = 0 (b+-, v vanish there), so 0.
     Window contacts without mass (b^theta_j = 0): beta^+_j = theta v_j, beta^-_j = -(1-theta)v_j, beta^theta_j = 0, z'_j = z_j, z_j v_j >= 0: on
     the designated side tau beta^sigma_j has the sign z_j, so |tau B_j| - z'_j tau B_j = 0. Contacts in (N, N''] \ Far: same computation.
     Contacts beyond N'' (z'_j = 0): kink |tau rho beta^sigma_j| <= rho |tau| |v_j| for sigma = +-, and 0 for sigma = theta (beta^theta = 0 beyond N).
     Total: Kink' <= rho |tau| V_{>N''} <= eps_0 s_1 |tau| <= eps_0 tau^2 for |tau| >= s_1 (sigma = +-), and Kink' = 0 for sigma = theta.
 (c) Hilbert term (A Lemma 4.3 at f'): nu' Psi'(tau U*B^sigma/nu') <= (tau^2/2) h'(B^sigma)(1 + 2|tau| ||U*B^sigma||/nu') when |tau| ||U*B^sigma|| <= nu'/2.

Step 6 (conclusion). At late stages h'(B^sigma) <= rho^2 kappa + delta/8 and rho^2 H'_m(omega^sigma_m) <= rho^2 kappa + delta/8 (Step 3, and h(b^sigma),
H_m(omega^sigma) <= kappa by convexity, 1.6), and the factors in Steps 4-5(c) are <= 1 + Kc T_0. By (2.1.3), for 0 < |tau| <= T_0,
   p*(f' + tau g') <= 1 + (tau^2/2)(rho^2 kappa + delta/4) + eps_0 tau^2 = 1 + (tau^2/2)(rho^2 kappa + delta/2) <= 1 + (tau^2/2)(1 - delta)
(rho^2 kappa = 1 - 2 delta). With T_0^2 <= 3 delta and, at late stages, p*(f' - f) <= (1-rho^2)T_0^2/6 and p*(g' - rho g) <= (1-rho^2)T_0/6, Lemma 1.4
gives g' in C(f'); (f', g') attains its norm and converges to (f, rho g). QED.

## 2.2 Remarks on the proof. (PROVED statements.)
 (a) No "transfer error" occurs: the one-sided decompositions of f transfer EXACTLY to f' after (i) recomputing the d-coefficients at f'
     (which kills every first-order Hilbert mismatch in the blocks: the first-order block term at f' is <D omega, D w'>/C' - d' = 0),
     (ii) the steering conditions v_m(xhat') = 0 (equivalently d'^+_m = d'^-_m), which make the two side decompositions represent the SAME g',
     and (iii) replacing the tail of g beyond the window by the theta-tail sum_m R_m* omega^theta_m-part (the base part of g' beyond N is 0),
     which turns the non-constant split into a constant split beyond N (A_referee 5.1) while the window part is made two-sided by masses.
 (b) Order of choices: N, then s_1 (<= tau_N/(4A_0)), then Far (pull of size ~ s_1 at costless coordinates: flipped far contacts carrying
     negative masses), then N'' (tail cost <= eps_0 s_1 |tau|), then mu (raise by a mass at j_+, intermediate value theorem), then p.
     No step requires a rate, a tail-independence radius, or any information about the deep block structure of f.
 (c) The mixed second-order/first-order term created by the masses (part 3, 3.1) is exactly cancelled by Step 1: it is the first-order
     difference between the two sides, <U*v, e' - e>, and Step 1 makes v(xhat') = 0.

## 2.3 Corollaries. PROVED.
 (a) (A_referee §5.2/§5.4 made rigorous.) The two-piece mates g = v 1_{K_1} - (v 1_{K_1})(zhat) a, v = c u_{k_0,m}, over an infinite contact set
     with ARBITRARY (non-constant) split K' = K_1 + K_2, are recovered: data b+ = g, omega+ = 0; b- = g - v, omega- = (c/lambda_{k_0,m}) e_{k_0};
     w_m(k_0) = 0 gives d+ = d- = 0 (d-neutral); single block. Lemma 1.7 applies (P1 Prop 2.3 shows one-sided admissibility for small c).
     Hence g in Ls(f). (The "extra degree of freedom in the masses" of A_referee §5.4 is replaced by Step 1: P1's correction is confirmed and
     generalized.)
 (b) (P1 Prop 6.3 made rigorous, with P1-referee's sharpening.) At P1's example (T of P1 2.1, f of P1 2.2): every g in E_u (P1 6.1) with
     mu+ <= inf theta(g), mu- >= sup theta(g) and rho^2 max( h(g - mu+- u), (mu+-)^2/C_1 ) < 1 has (f, rho g) in cl NA. In particular the
     whole slab {g in E_u : ||theta(g)||_inf <= theta_*} (P1 6.2), including all the explicit defect mates of P1 Thm 2.4, lies in Ls(f).
 (c) (Every one-sided-linear exact resonance with one active block is harmless.) If f has F finite and g in C(f) has one-sided admissible
     two-piece data with a single active block and Delta d = 0, then g in Ls(f). This is the complete class of "exact-resonance" switching
     mates of P1 4.1 with finitely supported block carriers whose transfer does not involve R_m* w_m.

## 2.4 Remark (shifted two-piece data; the full fibre at P1's example). SKETCH.
For g in C(f) at P1's example, optimal decompositions at scale t carry, besides g - mu_t u on the base and mu_t u on the carrier, O(t^2)
first-order masses (shifts, A §4.5 / A §9(f)); the limits mu+- of mu_t along t -> 0+- satisfy only SHIFTED second-order bounds
H^sh <= 1, not kappa <= 1. Theorem 2.1 extends verbatim to two-piece data with quadratic shifts tau^2 theta^sigma_m w_m (A Def 4.15) on each
side, the shift kink costs being transported as in the proof of A Thm 4.17 (limsup of kappa_q at f' <= kappa_q at f, by domination) and
the theta-certificate at small scales using the shift theta^theta := (1-theta)theta^+ + theta theta^- (H^sh is convex). Combined with P1 6.1
(every g in C(f) lies in E_u with such limit decompositions) this would give f in R (every mate recovered) at P1's example. The shifted
transport of A Thm 4.17 has non-explicit o(tau^2) remainders, which are harmless here because Theorem 2.1 needs only a FIXED range
|tau| <= T_0 and uniform convergence along the construction. Not written out in full; status SKETCH.

# P2 part 3: the mixed term, d-mismatch, and non-neutral two-piece mates

## 3.1 Proposition (the mixed term created by contact masses). PROVED.
Let a'' = a + delta y with y in c_00 (e.g. y = z_j e_j*, a tiny contact mass), e(delta) := U*a''/||U*a''||. Then e'(0) = P_{e-perp}U*y/nu, and for
every B in l_1 with z' = z on supp B:
   B(xhat') - B(zhat) = <U*B, e(delta) - e> = delta <P_{e-perp}U*B, P_{e-perp}U*y>/nu + O(delta^2 ||B||_1).
Since the first-order term of q*(a' + tau B) at f' is tau B(xhat') (Lemma 1.3 / A Lemma 7.2), a mass delta at j shifts the first-order base
term of a transported decomposition by
   tau delta z_j <P_{e-perp}U*B, P_{e-perp}U*e_j*>/||U*a|| + O(tau delta^2)        (the "mixed term" of the task),
which is of size ~ tau^2 exactly at the scales tau ~ delta where the mass is needed. Its effect depends on how many base parts B must be
served by ONE g':
 (a) One decomposition (B fixed): harmless. The first-order terms of all components of a decomposition of f' + tau g' add up to g'(x')
     (balance, A Lemma 7.1 at f'); recomputing the block coefficients d' at f' (block first-order terms 0) and normalizing g'(xhat') = 0 by
     subtracting c a' (no cost: a' direction is a rescaling) forces B(xhat') = 0 (Lemma 1.3). The mixed term is absorbed into c.
 (b) Two decompositions B+ (tau > 0), B- (tau < 0) of the same g' (two-piece mates): both first-order terms vanish iff
     (B+ - B-)(xhat') = 0, i.e. v(xhat') = 0 for the transfer v = B+ - B-. The mixed-term DIFFERENCE delta z_j<P_{e-perp}U*v, P_{e-perp}U*e_j*>/nu
     is not zero in general, and it is cancelled exactly by the steering step (Thm 2.1, Step 1: far flipped contacts with negative masses
     pull, a mass at j_+ raises, intermediate value theorem). So for two-piece mates the mixed term is NOT an obstruction (PROVED, Thm 2.1).
 (c) Finitely many pieces: one scalar steering condition per independent difference; cancellable under a span hypothesis like (S).
 (d) A continuum of pieces (scale-dependent decompositions B_t, t in [s_1, T_0]): the conditions (B_t - B_{t'})(xhat') = 0 for all t, t' are
     infinitely many; by 3.2 they are equivalent to exact replication at f' of the relative block positions u_{k,m}(x')/|R_m x'| on the union
     of the supports of the block parts, plus smallness of a d-mismatch remainder. This is the precise form in which the mixed term is an
     obstruction (HEURISTIC that it cannot be avoided by other decompositions; PROVED as an identity, 3.2).
*Proof.* d/d delta of (U*a + delta U*y)/||U*a + delta U*y|| at 0 is (U*y - <U*y, e> e)/nu. Then B(Ue(delta)) - B(Ue) = <U*B, e(delta) - e>, and
<U*B, P_{e-perp}U*y> = <P_{e-perp}U*B, P_{e-perp}U*y>. The remainder is bounded by the second derivative of e(.) on a neighbourhood. (a): Lemma 1.3.
(b): for the two transported decompositions, B+ - B- = rho v (Thm 2.1 (2.1.2)) and both have zero first-order term iff v(xhat') = 0; the derivative
of v(xhat') w.r.t. the mass is the displayed mixed-term difference. QED.

## 3.2 Proposition (consistency identity for a family of transported decompositions). PROVED.
Let (B_t, omega_t), t in an index set T, be decompositions of g at f with omega_t = (omega_{t,m}) finitely supported off-peak, d_{t,m} :=
<D w_m, D omega_{t,m}>/C_m, g = B_t + sum_m R_m*(omega_{t,m} - d_{t,m} w_m). Let f' be NA with supp omega_t off P'_m, g' := rho(g'' - c a') as in Thm 2.1
for some reference, and put d'_{t,m} := <D w'_m, D omega_{t,m}>/C'_m, B'_t := g' - rho sum_m R_m*(omega_{t,m} - d'_{t,m} w'_m). Then each B'_t has
B'_t(xhat') = 0 and the block parts have zero first-order terms, and for t, t' in T:
   B'_t - B'_{t'} - rho (B_t - B_{t'}) = -rho sum_m [ (Delta'_m - Delta_m) R_m* w'_m + Delta_m R_m*(w'_m - w_m) ],
   Delta_m := d_{t',m} - d_{t,m},  Delta'_m := d'_{t',m} - d'_{t,m} = <D w'_m, D(omega_{t',m} - omega_{t,m})>/C'_m
            = (1/|R_m x'|_m) (R_m*(omega_{t',m} - omega_{t,m}))(x').
Hence the transported pieces reproduce the transfers of f exactly (up to the two displayed vectors) iff
 (i) (consistency/steering) Delta'_m = Delta_m for all pairs, i.e. (R_m* omega)(x')/|R_m x'|_m = (R_m* omega)(xi)/|zeta_m|_m for omega in the span of the
     differences omega_{t'} - omega_t; and
 (ii) (d-mismatch) sum_m Delta_m R_m*(w'_m - w_m) is negligible (it vanishes when the data are d-neutral, Delta_m = 0).
Both remainder vectors are Y-vectors spread over all coordinates; their parts on non-contact coordinates outside supp a' cost FIRST order
(|tau| times their l_1 mass there, Lemma 1.3), so at scales tau >= s_1 they must be <= eps_0 s_1 in l_1.
*Proof.* Algebra from the definitions (as (2.1.2)); B'_t(xhat') = 0 by Lemma 1.3. Delta'_m formula: Lemma 1.1 at f' (off-peak w'(k) =
C' lambda_k u_k(x')/(Phi_k^2|R_m x'|)). At f the same formula with xi gives Delta_m = (R_m*(omega_{t'} - omega_t))(xi)/|zeta_m|. QED.
Reading: (i) is the multi-piece version of the steering condition (and the base-side manifestation of (i) is the mixed term of 3.1);
for a FINITE family it is a finite set of linear conditions on x' (Thm 2.1 handles one), for a scale-dependent family whose block
supports reach depth ~ t (all small t), it is exact replication of infinitely many relative positions (part 4).

## 3.3 Proposition (non-neutral two-piece data: the garbage identity). PROVED.
Run the construction of Thm 2.1 for two-piece data with Delta d_m != 0, steering instead d'^-_m - d'^+_m = Delta d_m (one scalar condition per block,
equivalently v_m(x')/|R_m x'| = v_m(xi)/|zeta_m| with v_m := R_m* omega_Delta,m). Then (2.1.2) becomes
   B^+ = B^theta + rho theta (v + E),  B^- = B^theta - rho(1-theta)(v + E),  E := -sum_m Delta d_m R_m*(w'_m - w_m),
and the proof of Thm 2.1 goes through verbatim provided, in addition, ||E||_1 <= eps_0 s_1/(2 rho) (E's first-order cost is <= 2 rho |tau| ||E||_1
on each side, also on supp a' where it may cause flips). This is the ONLY change.
*Proof.* As (2.1.2), using 3.2 with Delta'_m = Delta_m. QED.
Why this is delicate (HEURISTIC, with the PROVED clamp formula 1.1): the window masses (size ~ s_1) move xhat' by ~ s_1 in sup norm (through e');
by Lemma 1.1 every strict non-peak k with Phi_m(k) >~ s_1 changes by ~ s_1/Phi_m(k) (until clamped), so without retuning
||R_m*(w'_m - w_m)|| ~ s_1 * #{strict non-peaks k : Phi_m(k) >~ s_1} + (weight of peaks with margin < s_1), which is NOT <= eps_0 s_1 when block m has
infinitely many strict non-peaks (generic f, Preprint A Remark) or dense near-threshold peaks. With finitely many non-peaks the change can be
undone by finitely many tuning moves; this gives 3.4.

## 3.4 Theorem (non-neutral two-piece mates at block-tame active blocks). SKETCH (all estimates given; the uniform implicit-function step is routine).
Let f, g, rho be as in Thm 2.1 except that Delta d_m != 0 is allowed. Assume for every m in I_0:
 (i) Qbar_m := {strict non-peaks} cup {degenerate peaks (alpha_{m,k} = 0)} is finite;
 (ii) (margin sparsity, C_notes (MS)) sum_{k in P_m : 0 < mu_{m,k} < s} Phi_m(k) = o(s) as s -> 0, mu_{m,k} := |u_{k,m}(xi)| - theta_m Phi_m(k);
 (iii) (tuning span) for some gamma > 0 the restrictions to J_gamma of the functionals psi_{k,m} := u_{k,m} - (u_{k,m}(xi)/|zeta_m|_m) R_m* w_m
      (k in Qbar_m, m in I_0) are linearly independent.
Then (f, rho g) is in cl NA whenever rho^2 kappa < 1 (no steering hypothesis (S) is needed).
*Sketch.* Construction of Thm 2.1 without Far set and raising mass (steering is now part of the tuning): window masses as before, N'' last,
and finitely many free tuning moves p at coordinates j_1..j_r in J_gamma chosen so that the matrix (psi_{k,m}(e_{j_i})) has full row rank. Tuning
equations: u_{k,m}(xhat'(p))/|R_m xhat'(p)|_m = u_{k,m}(xi)/|zeta_m|_m, (k,m) in Qbar. The left side is C^1 in p (|R_m(.)|_m restricted to a finite-
dimensional affine family is convex and differentiable, hence C^1), its derivative at the limit is (psi_{k,m}(e_{j_i})/|zeta_m|), surjective by
(iii); along the construction the maps converge in C^1 on a fixed ball (pointwise convergence of differentiable convex functions implies
locally uniform convergence of gradients), and the residuals at p = 0 tend to 0 (masses -> 0, xhat' -> zhat weak*). A uniform surjectivity
(Graves) argument gives solutions p -> 0. After tuning: by Lemma 1.1, w'_m(k) = sign * min(M'_m, C'_m r_m(k)) on Qbar_m (r unchanged), so
d'^-_m - d'^+_m = Delta d_m exactly; peaks with margin >= c_1 s_1 + (deep perturbation) stay peaks with w' = sigma M'; the remaining peaks have total
weight sum lambda_k <= o(s_1) (MS) + o_{N''}(1); the identity C'^2 (1 - rho_0) - (1 - C')^2 S_1 = (changed coordinates) (with rho_0 := sum over
tuned non-peaks of Phi^2 r^2, S_1 := sum over unchanged peaks of Phi^2; the left side is strictly increasing in C') gives |C' - C| = O(sum over
changed k of Phi_m(k)^2) = o(s_1). Hence ||E||_1 <= |Delta d| (||lambda||_1 (1 + max r) |C' - C| + 2M * changed weight) <= eps_0 s_1/(2 rho) at late stages
(N'' chosen after s_1). Apply 3.3. QED (sketch).
Example: P1's example satisfies (i) (Qbar_1 = {2}) and (ii) (margins >= q_0 min(1/4, 2 sqrt Phi), P1 6.0: sum_{mu < s} Phi <= s^2/(4q_0^2) = o(s)),
so non-neutral variants of its exact resonance (carriers with w(k) != 0) are covered once (iii) holds.

## 3.5 What remains open for one-sided-LINEAR (two-piece) mates. OPEN.
 (R1) Delta d != 0 at an active block with infinitely many strict non-peaks or with dense near-threshold peaks (failure of 3.4(i)-(ii)):
      ||R*(w' - w)|| cannot be made <= eps_0 s_1 by finitely many moves; deep retuning of a window of size ~ log(1/s_1) is needed (part 4, (QI)).
 (R2) Several active blocks, d-neutral, without (S) (e.g. all v_m supported in F cup K): steering of the H_0-component then has to use masses
      (directions <P_{e-perp}U*v_m, U*e_j*>), which is plausible but not proved.
 (R3) Second order: kappa > 1/rho^2 for the explicit side decompositions although g in C(f) (the optimal decompositions involve shifts):
      Remark 2.4 (SKETCH).
 (R4) Infinite base support F (near-flip coordinates as one-sided resources): truncation of a at the window turns them into contacts;
      the flip costs must then be transported (A Lemma 6.4 monotone truncation is the natural tool). Not done.
 (R5) Degenerate peaks used linearly as one-sided block resources (the only one-sided block resource compatible with LINEAR usage):
      they can be turned into strict non-peaks with tiny gap at f' by one tuning move each (Lemma 1.1), after which Thm 2.1/3.4 apply.
      SKETCH.
# P2 part 4: scale-dependent switching mates — replication, implants, averaging; the residual class

## 4.1 Lemma (replication identity). PROVED.
Fix a block m (index dropped), f in S_{p*} and f' in S_{p*} (e.g. NA). Partition N into
 W_off: coordinates that are strict non-peaks at f and at f' with r'(k) = r(k) (tuned),
 W_P:  coordinates that are peaks at f and at f' with the same sign (tuned peaks and untouched robust peaks),
 Ch:   the rest ("changed").
Put rho_W := sum_{W_off} Phi_k^2 r(k)^2, S_P := sum_{W_P} Phi_k^2, G(c) := c^2(1 - rho_W) - (1 - c)^2 S_P. Then 1 - rho_W > 0, G is strictly increasing on
[0,1], G(C') - G(C) = sum_{Ch} Phi_k^2 (w'(k)^2 - w(k)^2), hence
   |C' - C| <= sum_{Ch} Phi_k^2 / g_0,   g_0 := min_{c between C, C'} G'(c) >= 2 min(C, C')(1 - rho_W) > 0   (|w|, |w'| <= 1),
and w'(k) - w(k) = sign * r(k)(C' - C) on W_off, = -sigma_k (C' - C) on W_P, |w'(k) - w(k)| <= 2 on Ch, so
   ||R*(w' - w)||_1 <= |C' - C| sum_k lambda_k (1 + r(k) 1_{W_off}) + 2 sum_{Ch} lambda_k.
*Proof.* C^2 = sum_k Phi_k^2 w(k)^2 with w = C sign r on W_off and |w| = M = 1 - C on W_P (Lemma 1.1), and the same at f' with the same r on W_off.
1 - rho_W = 1 - sum_{W_off} Phi^2 w^2/C^2 >= sum_P Phi^2 M^2/C^2 > 0 (P nonempty). G'(c) = 2c(1 - rho_W) + 2(1 - c)S_P > 0. Mean value theorem. QED.
Consequence (deep replication): if every coordinate with Phi_m(k) >= theta is in W_off cup W_P, then ||R_m*(w'_m - w_m)||_1 <= c_f theta
(c_f depends on m, M, C only), since sum_{Phi < theta} lambda_k <= 2 m theta and sum_{Phi < theta} Phi_k^2 <= theta^2.

## 4.2 Lemma (feasibility of retuning moves; duality). PROVED.
Let (u_k)_{k in W} be finitely many elements of l_1, G a set of coordinates, A > 0 and (delta_k) in R^W. There is y supported in G with ||y||_inf <= A
and u_k(y) = delta_k for all k in W iff  sum_k c_k delta_k <= A ||(sum_k c_k u_k) 1_G||_1 for all c in R^W.
Hence, with the restricted radius r_W(G) := min_{||c||_1 = 1} ||(sum_k c_k u_k) 1_G||_1, every correction with max_k |delta_k| <= A r_W(G) is feasible,
and r_W(G) = 0 iff some nonzero combination of the u_k vanishes on G.
*Proof.* {(u_k(y))_k : supp y in G, ||y||_inf <= A} is a compact convex symmetric subset of R^W (weak*-compact l_inf(G)-ball, weak*-continuous map);
its support function at c is A ||(sum c_k u_k)1_G||_1; a point lies in a compact convex set iff it satisfies all support inequalities.
For the radius statement: sum c_k delta_k <= ||c||_1 max|delta_k| <= A r_W(G) ||c||_1 <= A ||(sum c_k u_k) 1_G||_1. QED.
Remark. If the window W contains the support of a resonance carrier (a combination of the u_k supported in F cup K, e.g. v of an exact resonance),
then r_W(J) = 0 on the free coordinates J: these directions must be steered by contacts and masses (Thm 2.1, Step 1), not by free moves.

## 4.3 Proposition (abstract replication–averaging–transfer scheme). PROVED (as an implication; the hypotheses carry the content).
Let f in S_{p*}, g in C(f), rho in (0,1), delta in (0,1/2], T_0 in (0,1] with T_0^2 <= 3 delta, kappa >= 0, J >= 4 kappa/delta. Suppose that for every
eta > 0 there are an NA point f' and gbar, h_1, ..., h_J in X* (s_j = s_1 2^{1-j}, s_1 <= T_0) with
 (TR) [transfer regime]  p*(f' + t gbar) <= 1 + (t^2/2)(1 - 2 delta) for s_J <= |t| <= T_0;
 (TS) [two-sided supply] p*(f' + t h_j) <= 1 + (t^2/2)(1 - 2 delta) for |t| <= s_j, and p*(h_j - gbar) <= kappa s_j;
 (SL) [slack] p*(f' - f) <= eta and p*(gbar - rho g) <= eta.
Then (f, rho g) is in cl NA.
*Proof.* Lemma 1.5 gives g' := (1/J) sum_j h_j with p*(f' + t g') <= 1 + (t^2/2)(1 - 2 delta + 4 kappa/J) <= 1 + (t^2/2)(1 - delta) on |t| <= T_0 and
p*(g' - gbar) <= 2 kappa s_1/J. Lemma 1.4 applies once eta and s_1 are small (p*(f'-f) <= (1-rho^2)T_0^2/6, p*(g' - rho g) <= (1-rho^2)T_0/6). QED.
Theorem 2.1 is the special case J = 1 and h_1 = gbar = g': the theta-tail makes the frozen error vanish, so no averaging is needed.

## 4.4 What (TR) and (TS) require for scale-dependent switching mates. (Identities PROVED; necessity HEURISTIC; (QI) OPEN.)
Let g be a mate whose admissible decompositions (B_t, Omega_t) change with t on a side at all small scales (approximate resonances,
A §7.2, P1 4.1). Transport them to f' as in 3.2 (d'_t recomputed per scale). Then:
 (1) [consistency] by 3.2(i) the transported pieces represent ONE gbar only if the relative positions u_{k,m}(x')/|R_m x'|_m equal those of xi
     on the span of the differences of the block parts used at scales in [s_J, T_0], up to an l_1 error <= eps_0 s_J after multiplication by
     R_m* w'_m; equivalently, the mixed term of 3.1 must vanish for all pairs of pieces.
 (2) [depth of the window] at scale t one-sided block carriers have depth Phi <~ t or are near-threshold (P1 3.3 with P1-referee correction
     C3). Usage at depth Phi < theta moves the functional t lambda_k Omega_t(k) u_k with |t Omega_t(k)| <= 2 s(t) (box), i.e. total
     l_1 mass <= 2 s(t) sum_{Phi < theta} lambda_k = O(theta); dropping it (moving it to the base) costs at most O(theta) (kink, first order in
     the moved mass), which must be <= eps_0 t^2 at t = s_J: the replicated window must reach depth theta <~ eps_0 s_J^2. By 4.1 this means: all
     coordinates with Phi >= theta tuned or untouched robust peaks; then ||R*(w' - w)|| = O(theta).
 (3) [perturbations to undo] the masses needed for (TS) move xhat' by ~ s_1 in sup norm (through e', 3.1); by Lemma 1.1 this moves every strict
     non-peak of depth Phi >~ s_1 and every peak with margin < s_1. Undoing it requires corrections of size ~ s_1 on a window W(theta) of about
     |I_0| log2(1/theta) functionals, using costless coordinates G (free coordinates unused by the base parts at scales >= s_J, far
     coordinates), modulo resonance directions (steered as in Thm 2.1). By 4.2 this is possible iff s_1 <~ r_{W(theta)}(G), i.e.
        (QI)  along a sequence of usable small scales s -> 0:  r_{W(eps_0 s^2)}(G_s) >= c s  for some c > 0.
     (QI) is a quantitative independence property of T relative to f, g, not implied by Lemma B. Example of the difficulty: for a T built as
     in P1 2.1 (super-fast signature tails delta_l 2^{-s} on disjoint sets S_l), the restricted radii of deep windows on FAR coordinates decay
     faster than any power of s, so (QI) could only hold through near free coordinates and depends on the targets y^(i). OPEN.
 (4) [two-sided supply] (TS) needs, at J = O(kappa/delta) scales s_j <= s_1 (a FIXED number), two-sided certificates at f' within O(s_j) of gbar.
     Engineered sources: (a) contact masses for base one-sided usage (always possible; price: the consistency conditions (1));
     (b) off-peak carriers with gap: replicate finitely many ratios (Thm 2.1); (c) degenerate peaks: one tuning move each turns them into
     strict non-peaks with tiny gap (Lemma 1.1), SKETCH; (d) other one-sided block carriers (weak peaks, near-threshold coordinates,
     coordinates pushed beyond their gap, deep coordinates): only through implanted gaps on carriers k with ||u_{k,m} - v|| <~ Phi_m(k)
     (rates; one tuning move per carrier, finitely many), which lie inside the replicated window of (2), hence again (QI); (e) nothing else:
     by P1-referee R1, along C-tame NA approximants every recovered mate is a limit of certificate-span vectors, so a component carried at f
     only by one-sided BLOCK resources, without rates and without a contact representation (exact resonance), cannot be supplied by
     certificates at such approximants.

## 4.5 C's "implant scale gap" heuristic (C_part6 §9.3): verdict.
C's claim: an implanted non-peak at depth k costs eps >~ Phi(k) in p*(f' - f), so the slack covers only |t| >~ sqrt(Phi(k)), while the implant is
quadratic only for |t| <~ Phi(k); hence implants cannot bridge (Phi(k), sqrt(Phi(k))) and are never the sole support of a mate component at
intermediate scales.
 * The arithmetic is correct (PROVED: by Lemma 1.1 a gap gamma' implanted at a former peak changes w(k) by >= gamma', which contributes
   lambda_k gamma' u_k to f' - f; A Prop 8.4(b) bounds the certificate mass it can carry).
 * That the window (Phi, sqrt Phi) must be covered by structure shared by xi and x' is correct; that this obstructs engineered recovery is
   FALSE in general: Theorem 2.1 is a rigorous instance where the implanted two-sided structure (masses ~ s_1, so p*(f' - f) >~ s_1 >> s_1^2)
   serves only |t| <= s_1, while the whole window (s_1, T_0) — far beyond the slack scale sqrt(p*(f'-f)) — is covered by the EXACT transfer
   of f's one-sided decompositions. The slack is needed only for |t| >= T_0 (fixed): p*(f' - f) must be small compared with T_0^2, not s_1^2.
 * For scale-dependent mates the heuristic points at the real difficulty: the shared structure must then be replicated at all scales in
   (s_1, T_0), i.e. (QI).

## 4.6 Exact residual class (what P2 does NOT cover). OPEN.
Covered: (PROVED) two-piece switching mates with finitely supported off-peak block carriers, finite F, any contact set K and any split,
d-neutral transfer, one active block or several under (S) (Thm 2.1); (SKETCH) non-neutral transfers at block-tame active blocks (Thm 3.4),
shifted two-piece data (Rem 2.4), degenerate-peak carriers (3.5 R5).
Not covered:
 (R1) non-neutral two-piece data at active blocks with infinitely many strict non-peaks or dense near-threshold peaks (needs (QI));
 (R2) several active blocks without (S);
 (R3) two-piece data whose explicit side coefficients exceed 1/rho^2 and are not cured by shifts (Rem 2.4 is SKETCH);
 (R4) infinite base support F (near-flip coordinates as one-sided resources);
 (R5) genuinely scale-dependent switching (approximate resonances): one-sided carriers at depth ~ t (weak peaks, near-threshold coordinates,
      coordinates pushed beyond their gap) or contact splits varying with the scale on the SAME side; the scheme 4.3 reduces them to (QI) and
      implant compatibility, OPEN and T-dependent.
At P1's example every mate lies in E_u (P1 6.1); the slab and all explicit defect mates are recovered (Cor 2.3(b), PROVED); the whole fibre
would follow from Rem 2.4 (SKETCH).
# P2 part 5: numerical sanity checks (finite models; numpy + cvxpy/Clarabel). Scripts in ctx/r2/P2work/.

* check_clamp4.py / check_clamp5.py (Lemma 1.1). Random blocks (14 coordinates, Phi_k ~ 2^{-k}), the norming functional computed by a
  one-dimensional reduction (w = clip(mu zeta/Phi^2, -M, M), optimize over M) and certified by the primal block norm
  |zeta|_m = min{ max(||x||_1, ||beta||_2) : zeta = x + D beta } (SOCP): relative primal-dual gap <= 5e-8 in all 30 trials. On blocks
  whose strict non-peaks carry Hilbert weight >= 5% of C^2 (well-conditioned), the clamp identity mu |zeta|_m = C holds to 6.5e-7.
  (On blocks whose non-peaks have tiny zeta the multiplier mu is numerically ill-determined; the objective is still exact.)
  Caveat: a first attempt with the SUM primal ||x||_1 + ||beta||_2 gave a spurious 35% gap — the gauge of B_{l_1} + D(B_{l_2}) is the MAX;
  recorded because the same slip is easy to make elsewhere.
* check_thmC.py (Theorem 2.1 algebra in P1-referee's finite model of P1's example: base coordinate 0, 12 contacts, 10 free
  coordinates, one block of 7 coordinates with the special carrier u, u(zhat) = 0, w(1) = 0; mates g in E_u with non-constant theta(g)
  in [0, 0.15]). Construction exactly as in Thm 2.1 (window of 5 contacts with masses 4 rho s_1 |b_theta|, theta = 1/2, rho = 0.9,
  s_1 = 0.02), steering by a one-parameter path (raise: mass at contact 1; pull: partial move of the last contact, then a full flip of a
  far contact with negative mass) and bisection. Results for 6 seeds: steering reaches u(xhat') = 0 to 1e-16 and d' = 0 to 1e-16;
  max over 50 values t in +-[1e-3, 20] of p*(f' + t g') - s(t) is -5e-7 (= the solver offset; the same offset appears for the mates at f),
  i.e. (f', g') is contractive; (p*(f'+tg')-1)/t^2 <= 0.008 at |t| = 0.01, 0.03. Caveat: in a finite model every functional attains its
  norm and the true p* may use other decompositions, so the run checks the algebra of (2.1.2), the steering and the contractivity of the
  constructed pair, not the necessity of the construction (the unsteered pair is also contractive in the finite model).
