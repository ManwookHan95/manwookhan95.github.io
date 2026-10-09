# N2 notes — Engineered recovery of resonant switching mates (exact and approximate resonances)

Round 2, task N2. Setting: canonical base q, Martin's norm with a FINITE block set I (p_N, any N; Preprint B Remark martin-tail);
"admissible T" = Lemma B's conclusion only. Imports (refereed): A_notes Facts A-F, Lemmas 4.3, 4.4, Prop 4.5, Lemmas 4.6, 4.7, 7.1, 7.2;
N_part1 Thm 1 / Lemma 1.2 / Prop 1.5 (Ls(f): g in Ls(f) iff (f, rho g) in cl NA for all rho < 1; one sequence per mate suffices);
P1 §2, §6.1-6.2 (example); E Lemma 6.1/Cor 6.2, Prop 8.2; R1 of P1_referee (mod C Thm 6.2/Prop 6.5). Part files: N2_part1.md ... N2_part5.md
(this file assembles them). Scripts: N2_work/thm1_check.py, N2_work/lemma32_check.py.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 0. Answer and summary
**Exact resonances are recovered by engineering, rigorously, whenever Delta d >= 0 (with a mild tuning condition if Delta d > 0);
for Delta d < 0 the recovery reduces to one explicit pinning condition; approximate resonances reduce to a conversion/implant
capacity. No configuration was found where engineering provably fails, so no counterexample is claimed.**
 1. Theorem 1 (PROVED): every mate g in C(f) (F = supp a finite) with an EXACT two-piece representation — admissible one-sided linear
    decompositions on the two sides whose base parts live on F cup K with the contact signs, block parts on finitely many strict
    non-peaks of one block, equal d-coefficients (Delta d = 0) — lies in Ls(f). The proof is P1 6.3's construction made rigorous and
    general: window masses on the contacts, far sign-flipped contacts with negative masses (free pulls), a continuous tuning MASS fixed by
    the intermediate value theorem (replacing P1's partial-pull coordinate, referee gap G2), an arbitrary constant-theta tail, explicit
    quantifier order (G3), g in C(f) used only in the slack regime (G1). Corollary 2.5: P1's explicit defect (Thm 2.4 of P1) and the whole
    slab of P1 6.2 are recovered.
 2. The d-coefficient issue (E_referee 3.1): a rigorous convexity lemma (1.3) shows the "c-trick" for tau c <= 0 costs NOTHING at first order;
    hence Delta d > 0 is recovered (Thm 2) under (TT) two-sided mass tuning, in general under a scalar Bregman condition (BR). For Delta d < 0
    one side necessarily has tau c > 0, and then (Lemmas 3.2(b), 3.3, PROVED) the block cost is >= 1 + 2M|s|: unavoidable common peaks of
    opposite sign exist at EVERY NA approximant of a non-NA f. So for Delta d < 0 the mismatch Delta d R*(w' - w) must sit in the base; Thm 3
    (PROVED, conditional) recovers g under the pinning condition (PC): its kink on near free coordinates is o(t_n).
 3. The C_referee kink class (infinitely many kinks, Gamma_2 < Gamma_w) is IDENTICAL to exact resonances with Delta d = -(s+ - s-) c'/M (1.6, 3.9):
    no new mechanism; c' < 0 / c' = 0 covered, c' > 0 is the Delta d < 0 case.
 4. Delta d < 0 mates exist (P1-type T with u_{2,1} := (h - kappa' pi)/n, 3.8, SKETCH); in block-tame carrier blocks with robust peaks the
    pinning conditions collapse to the single tuned scalar v(x') = 0 (exact identity, 3.7(a)) and (PC) holds up to a perturbation lemma
    (SKETCH); in the generic case (infinitely many strict non-peaks) (PC) is a quantitative tail-independence property: OPEN.
 5. Approximate resonances: Theorem 4 (PROVED, conditional) — recovery holds as soon as the approximant supplies J(rho) ~ 16 kappa/(1-rho^2)
    two-sided carriers with frozen errors O(scale) at adjacent scales below the destruction boundary plus the transport (HT). Prop 5.2
    (PROVED mod R1): along C-tame approximants the FREE-coordinate part of a recovered mate must be carried by off-peak block coordinates of the
    approximants — base engineering cannot help there; this is why conversion capacity is decisive for approximate resonances and irrelevant
    for exact ones. Far rigidity (E (A2)) is compatible with Lemma B (4.5, SKETCH), so Lemma B alone does not give unbounded conversion
    capacity; but implanted/generic carriers are not excluded and no N&S property of T is identified (OPEN).
 6. Item 3: no configuration with provable non-recovery; dist((f, rho g), NA) > 0 is not claimed for any example.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Algebra of exact two-piece representations (b+-(zhat)=0; v in Y, z-signed on K, infinite support; Delta d = ell(xi)/|zeta|; v=0 => Cert) | PROVED | 1.2 |
| 2 | Convex block lemma (c-trick with tau c <= 0 is free) | PROVED | 1.3 |
| 3 | Base excess bound at an NA point; convergence of engineered approximants | PROVED | 1.4, 1.5 |
| 4 | C_referee kink re-splitting = exact resonance with Delta d = -(s+-s-)c'/M | PROVED | 1.6, 3.9 |
| 5 | **Theorem 1**: exact two-piece mates with Delta d = 0 (one active block) are in Ls(f) | PROVED | 2.3 |
| 6 | Corollary: P1's example — slab of 6.2 and all g_{K1} recovered (P1 6.3 made rigorous, gaps G1-G3 fixed) | PROVED | 2.5 |
| 7 | All of C(f) at P1's example recovered | OPEN (needs second-order rebalancing at engineered approximants) | 2.5 Rem |
| 8 | Several active blocks, Delta d_m = 0, rank condition | SKETCH (tuning step) | 2.6 |
| 9 | General mismatch identity with c+- and Bregman excess | PROVED | 3.1 |
| 10 | Wrong-sign c costs >= 2M|s|; common opposite peaks exist at every NA approximant of a non-NA f | PROVED (+numerics) | 3.2, 3.3 |
| 11 | Delta d < 0: convexity mechanism impossible on one side | PROVED | 3.4 |
| 12 | **Theorem 2**: Delta d > 0 recovered under (BR); (TT) => (BR) | PROVED | 3.5 |
| 13 | Delta d > 0 without (TT) | SKETCH (far-tail comparison, T-dependent) | 3.5 |
| 14 | **Theorem 3**: Delta d < 0 recovered under (PC) | PROVED (conditional) | 3.6 |
| 15 | (PC) for block-tame robust carrier blocks | SKETCH | 3.7(a),(b) |
| 16 | (PC) in the generic case (infinitely many strict non-peaks) | OPEN | 3.7(c) |
| 17 | Existence of Delta d < 0 exact two-piece mates | SKETCH | 3.8 |
| 18 | Cross-block exact relations = exact resonances (two active blocks) | PROVED (reduction) | 4.2 |
| 19 | **Theorem 4**: conditional recovery through converted/implanted carriers (averaging at f') | PROVED (conditional) | 4.3 |
| 20 | Transport hypothesis (HT) for approximate resonances | HEURISTIC | 4.3 |
| 21 | Far rigidity compatible with Lemma B | SKETCH | 4.5 |
| 22 | Full rigid design (A1)-(A5) + blocking (C1)-(C3) consistent with Lemma B? | OPEN | 4.6 |
| 23 | N&S property of T for recovering all resonant mates | OPEN (not identified) | 4.7 |
| 24 | Free-coordinate part of mates recovered along C-tame approximants is carried by off-peak block coordinates | PROVED mod R1 | 5.2 |
| 25 | Some (f, rho g) with dist to NA > 0 | not found; no claim | 5.3 |
| 26 | Density of NA((c_0,p), l_2^2) | OPEN (leaning positive) | 5.5 |

# N2 part 1: setting, the exact two-piece class, algebraic lemmas

Setting: canonical base q (B_q = B_{c_0} + U(B_H), U compact, dense range, U* injective), Martin's norm with a FINITE
block set I (p_N, any N; Remark martin-tail of Preprint B reduces Martin's p to these). Notation of A_notes §1, §4,
BRIEFING. Imported (refereed): (T1)-(T4), Facts A-F, Lemmas 4.3, 4.4, Prop 4.5, Lemma 4.6, 4.7, Lemmas 7.1-7.2 of
A_notes; N_part1 Theorem 1 (Ls(f); g in Ls(f) iff (f, rho g) in cl NA for all rho < 1); P1 §2 (example).
For f in S_{p*}: normer xi, q_0, forced data f = a + L*w, zhat = xi/q_0 = z + U e, nu = ||U*a||, F := supp a,
K := {j notin F : |z_j| = 1} (contacts = "kinks" of C_notes), J := {j notin F : |z_j| < 1} (free coordinates),
zeta_m = R_m** xi, P_m peaks, Q_m strict non-peaks, M_m, C_m, d_m(omega) := <D_m w_m, D_m omega>/C_m,
h(b) := ||P_{e-perp} U*b||^2/nu, H_m(omega) := ||P_m-perp D_m omega||^2/C_m. Labels PROVED / SKETCH / HEURISTIC / OPEN.

## 1.1 Definition (exact two-piece representation)
Let f in S_{p*} with F finite and g in C(f). An exact two-piece representation of g is (b+, omega+; b-, omega-) with
 (E1) b+, b- in l_1, supp b+- contained in F cup K, and z_j b+_j >= 0 >= z_j b-_j for every j in K;
 (E2) omega+-_m in c_00 with supp omega+-_m contained in Q_m (m in I);
 (E3) g = b+ + sum_m R_m*(omega+_m - d_m(omega+_m) w_m) = b- + sum_m R_m*(omega-_m - d_m(omega-_m) w_m);
 (E4) kappa := max{ h(b+), h(b-), H_m(omega+_m), H_m(omega-_m) : m in I } <= 1.
Derived data: Delta omega_m := omega-_m - omega+_m, Delta d_m := d_m(Delta omega_m), ell_m := R_m* Delta omega_m,
v := b+ - b- (the TRANSFER), I_act := {m : Delta omega_m != 0}. For theta in [0,1]:
b_theta := (1-theta) b+ + theta b- = b+ - theta v, omega_theta := (1-theta) omega+ + theta omega-.
The representation is RESONANT if v != 0. ("Two-piece mates" of A_referee 5.2, P1 2.3, 6.2 are of this form; see 2.6.)

## 1.2 Lemma (algebra of two-piece representations). PROVED.
(a) b+(zhat) = b-(zhat) = 0.
(b) v = sum_m ( ell_m - Delta d_m R_m* w_m ) is in Y := Ran T; supp v in F cup K; z_j v_j = |b+_j| + |b-_j| >= 0 on K.
(c) For every f'' in S_{p*} (normer xi'', block data zeta''_m, w''_m, C''_m) and every omega in c_00 supported in Q''_m:
    d''_m(omega) = (R_m* omega)(xi'')/|zeta''_m|_m. In particular Delta d_m = ell_m(xi)/|zeta_m|.
(d) If v = 0 then b+ = b- is supported in F and omega+ = omega-; then g is in Cert(f) (A Def 4.1) .
    If v != 0 then supp v cap K is infinite (so K is infinite and f is not norm attaining).
(e) If the two decompositions in (E3) are ADMISSIBLE one-sided linear decompositions, i.e. q*(a + tau b+-) <= s(tau)
    and N_m(w_m + tau(omega+-_m - d_m(omega+-_m) w_m)) <= s(tau) for 0 <= +-tau <= tau_0, then (E4) holds.
(f) For every theta in [0,1]: g = b_theta + sum_m R_m*(omega_theta,m - d_m(omega_theta,m) w_m), h(b_theta) <= kappa and
    H_m(omega_theta,m) <= kappa.
*Proof.* (a) For omega in c_00 off the peaks, <omega - d(omega) w, zeta> = 0 (A Lemma 4.2). Hence g(xi) = b+(xi) = q_0 b+(zhat),
and g(xi) = 0 for every mate (A Remark 2.3). Same for b-.
(b) Subtract the two representations in (E3): v = sum_m R_m*(Delta omega_m - Delta d_m w_m), by linearity of d_m. Each R_m* maps into
Y (T1), so v in Y. The support and sign statements follow from (E1).
(c) Off P''_m, Fact C at f'' gives w''_m(k) = C''_m zeta''_m(k)/(Phi_m(k)^2 |zeta''_m|), so
d''_m(omega) = sum_k Phi_m(k)^2 w''_m(k) omega(k)/C''_m = sum_k zeta''_m(k) omega(k)/|zeta''_m| = <omega, R_m** xi''>/|zeta''_m| = (R_m* omega)(xi'')/|zeta''_m|.
(d) If v = 0: on K, 0 <= z_j b+_j = z_j b-_j <= 0, so b+ = b- vanishes on K; and sum_m R_m*(Delta omega_m - Delta d_m w_m) = 0 gives,
by injectivity of L* (T1), Delta omega_m = Delta d_m w_m; at a peak w_m != 0 while Delta omega_m = 0, so Delta d_m = 0 and Delta omega_m = 0.
Then c := (b+, omega+) is a finite certificate (supp b+ in F finite, so ||b+/a||_inf < infinity; b+(zhat) = 0 by (a)) with
H(c) <= kappa <= 1 and g_c = g in C(f): g in Cert(f). If v != 0: v in Y \ {0} and Y cap c_00 = {0}, so supp v is infinite, and
supp v is contained in F cup K with F finite.
(e) Base: for 0 < tau <= tau_0, by A Lemma 7.2 (all terms nonnegative) and the lower bound of A Lemma 4.3,
1 + tau^2 h(b+)/(2(1 + tau ||U*b+||/nu)) <= q*(a + tau b+) <= s(tau) <= 1 + tau^2/2; divide by tau^2 and let tau -> 0: h(b+) <= 1.
Block: A Lemma 4.4(b) gives N_m(...) >= 1 + tau^2 ||h_perp||^2/(sqrt(Y^2 + tau^2||h_perp||^2) + Y) with Y -> C_m, so H_m <= 1.
The minus side is identical with tau < 0.
(f) Convex combination of the two representations; h and H_m are convex quadratic forms. QED.

Remark 1.2.1 (meaning of Delta d). By (b),(c): ell_m(xi) = Delta d_m |zeta_m| is the xi-value of the block carrier functional;
v(xi) = 0 always. Delta d is invariant under g -> -g (the sides swap: b~+ = -b-, b~- = -b+, omega~+ = -omega-, ...,
Delta d~ = d(omega~-) - d(omega~+) = -d(omega+) + d(omega-) = Delta d). So the sign of Delta d is intrinsic to the resonance.

## 1.3 Lemma (convex block lemma; makes the "c-trick" rigorous). PROVED.
Let f'' in S_{p*}, a block m, w'' := w''_m, omega in c_00 supported in Q''_m, d'' := d''_m(omega), and y in l_inf with N_m(y) <= 1.
For real tau and s in [0, 1) put tau~ := tau/(1-s) and
  W := w'' + tau (omega - d'' w'') + s (y - w'').
Then W = (1-s) [ (1 - tau~ d'') w'' + tau~ omega ] + s y, hence
  N_m(W) <= (1-s) N_m((1 - tau~ d'') w'' + tau~ omega) + s,
and if |tau~| <= r''_m(omega) (A Lemma 4.4(d) at f''):  N_m(W) <= 1 + (tau^2/(2(1-s))) H''_m(omega) (1 + 2|d'' tau~| M''/C'').
*Proof.* (1-s)(1 - tau~ d'') = 1 - s - tau d'' and (1-s) tau~ = tau: the identity is algebra. Then use the triangle inequality,
N_m(y) <= 1, and A Lemma 4.4(d) at f''. QED.
Use: in the two-piece engineering the block part of side +- will be w' + tau rho(omega+- - d' w') + tau rho c+-(w' - w) with
s := -tau rho c+- and y := w (the block functional of f, N_m(w_m) = 1). Lemma 1.3 applies iff s >= 0, i.e. tau c+- <= 0.
This proves the A_referee/E_referee "c-trick" for the correct sign WITHOUT any first-order bookkeeping. For the wrong sign
(s < 0, extrapolation beyond w'') the bound fails: if some peak k of w'' has w(k) = -w''(k) (status flips at fine
coordinates are unavoidable along NA approximants, since z' is in c_0), then ||W||_inf >= (1 - tau d'')M'' + |s|(M + M''),
a first-order excess 2|s| M approximately (see part 3).

## 1.4 Lemma (base excess at an NA point). PROVED.
Let a' in c_00 with q*(a') = 1, z' in B_{c_0} with z' = sign a' on supp a', e' := U*a'/nu', nu' := ||U*a'||, xhat' := z' + U e'
(so f' := grad p(xhat') is norm attaining with forced base data (a', z', e'), Fact D). Let B in l_1 with B(xhat') = 0, tau real,
|tau| ||U*B|| <= nu'/2, and |tau B_j| <= |a'_j| for j in supp a'. Then
  q*(a' + tau B) <= 1 + kink'_tau(B) + tau^2 h'(B)/(2(1 - |tau| ||U*B||/nu')),
  kink'_tau(B) := sum_{j notin supp a'} ( |tau B_j| - z'_j tau B_j )  (>= 0),  h'(B) := ||P_{e'-perp} U*B||^2/nu'.
*Proof.* On supp a': |a'_j + tau B_j| = |a'_j| + z'_j tau B_j (no sign change). Off supp a': |tau B_j| = z'_j tau B_j + (|tau B_j| - z'_j tau B_j).
So ||a' + tau B||_1 = ||a'||_1 + tau B(z') + kink'. ||U*a' + tau U*B|| = nu' ||e' + h||, h := tau U*B/nu', and
||e' + h|| = 1 + <e',h> + Psi(h) with Psi(h) <= ||h_perp||^2/(2(1 - ||h||)) for ||h|| <= 1/2 (A Lemma 4.3). Add, use
||a'||_1 + nu' = 1 and B(z') + <U*B, e'> = B(xhat') = 0. QED.
Consequences: kink'_tau(B) = 0 if B lives on supp a' and on contacts of f' (|z'_j| = 1) with sign(tau B_j) = z'_j there;
kink'_tau(B) <= 2|tau| ||B 1_E||_1 for any set E outside of which this holds.

## 1.5 Lemma (convergence of engineered approximants). PROVED.
Let a'_n in c_00 cap S_{q*} with a'_n -> a in l_1, z'_n in B_{c_0} with z'_n = sign a'_n on supp a'_n and z'_n -> z coordinatewise, and
f'_n := grad p(z'_n + U e'_n) (e'_n := U*a'_n/||U*a'_n||). Then f'_n -> f in norm; all forced data converge as in A Fact E; in
particular w'_{n,m}(k) -> w_m(k) for every (k,m), M'_{n,m} -> M_m, C'_{n,m} -> C_m, d'_{n,m}(omega) -> d_m(omega) for every
omega in c_00 off the peaks, and every finite set of strict non-peaks of f is eventually a set of strict non-peaks of f'_n with
gaps converging.
*Proof.* x'_n := z'_n + U e'_n: e'_n -> e in H (U*a'_n -> U*a in norm), so x'_n -> zhat weak* (bounded, coordinatewise).
L is compact, hence L x'_n -> L** zhat in norm (L** zhat in V, Fact B). J_V is norm-to-weak* continuous at L** zhat (all block
components nonzero; each J_m single valued, Smulian), and L* is weak*-to-norm continuous on bounded sets, so
L* J_V(L x'_n) -> L* J_V(L** zhat) = L* w (J_V 0-homogeneous, zhat = xi/q_0). grad p(x'_n) = grad q(x'_n) + L* J_V(L x'_n)
and grad q(x'_n) = a'_n (Fact D). So f'_n -> a + L*w = f; the rest is A Fact E applied to f'_n -> f. QED.

## 1.6 Where the classes of the task fit (PROVED identifications; details in parts 3, 4)
 * P1's example (P1 2.2, 6.1-6.2): every g in E_u with mu+ <= inf theta(g), mu- >= sup theta(g) gives the representation
   b+- := g - mu+- u, omega+- := (mu+-/lambda_0) e_2 (block 1); it is exact two-piece with Delta d = 0 (w_1(2) = 0), I_act = {1},
   v = (mu- - mu+) u, kappa = max(h(g - mu+- u), (mu+-)^2/C_1).
 * A_referee 5.2/5.4 (general form with equal d-coefficients): Delta d = 0.
 * E_referee 3.1 "two-piece mates with Delta d < 0": exactly the case Delta d_m < 0 for some m.
 * C_referee 1.20 "kink re-splitting" (one-sided first-order re-splits through infinitely many kinks): a block vector
   v'' = c' sigma 1_P + v''_Q (c' a constant) with beta = R* v'' supported on F cup K, z-signed, first-order flat. Writing
   sigma 1_P = (w - w 1_Q)/M gives v'' = (c'/M) w + omega'' with omega'' supported on Q, and flatness <v'', zeta> = 0 means
   (Lemma 1.2(c)) d(omega'') = -c'/M. The re-split f + tau g = (a + tau(b + s beta)) + R*(w + tau(Omega - s v'')) of a certificate
   (b, Omega = omega - d(omega) w) by amounts s+ >= 0 >= s- on the two sides has block parts
   Omega - s v'' = (omega - s omega'') - d(omega - s omega'') w, so it is an exact two-piece representation with
   Delta omega = (s+ - s-) omega'' and Delta d = -(s+ - s-) c'/M: the kink phenomenon IS an exact resonance with Delta d != 0
   (the uniform peak component of v'' is precisely the d-term). So the C_referee kink class and the E_referee Delta d < 0
   class coincide at the level of mechanisms; both are treated in part 3.
# N2 part 2: engineered recovery of exact two-piece mates with Delta d = 0 (rigorous)

Setting and notation of part 1. Throughout: f in S_{p*}, F = supp a finite, g in C(f) with an exact two-piece representation
(b+-, omega+-) (Def 1.1), v = b+ - b- != 0 (else g in Cert(f), Lemma 1.2(d)), a SINGLE active block m_0 (Delta omega_m = 0 for
m != m_0; so v = ell - Delta d R*_{m_0} w_{m_0}, ell := ell_{m_0}, Delta d := Delta d_{m_0}). In this part Delta d = 0, so v = ell.

## 2.1 Lemma (tuning direction). PROVED.
Put c_j := <P_{e-perp} U*v, U*e_j*> (j in N). There are j_+ in F cup K and sigma_+ in {-1, +1}, with sigma_+ = z_{j_+} if j_+ in K,
such that c_+ := sigma_+ c_{j_+} > 0.
*Proof.* v is in Y \ {0} (Lemma 1.2(b),(d)), hence not in c_00, hence not a multiple of a; U* is injective, so U*v is not a multiple
of U*a = nu e, i.e. P_{e-perp} U*v != 0. Since supp v is in F cup K and the series converges in l_1,
  sum_{j in F} v_j c_j + sum_{j in K} |v_j| z_j c_j = <P_{e-perp} U*v, U*v> = ||P_{e-perp} U*v||^2 > 0   (z_j v_j = |v_j| on K).
If c_j != 0 for some j in F take j_+ := j, sigma_+ := sign c_j. Otherwise the first sum vanishes and some j in K has z_j c_j > 0. QED.
(Example: in P1's example F = {1}, U*e_1* = nu_1 e, so c_1 = 0 and only contact directions exist; for diagonal U all
contact directions have z_j c_j >= 0: masses alone can only RAISE v(x'), which is why far pulls are needed.)

## 2.2 Lemma (two elementary continuity facts). PROVED.
(a) For A in l_1 with U*A != 0 let E(A) := U*A/||U*A||. If ||U*(A - a)|| <= nu/2 then ||E(A) - e|| <= 2||U*(A - a)||/nu.
(b) There is delta_1 > 0 such that for all A with ||A - a||_1 <= delta_1 and all real mu with |mu| <= delta_1:
    d/dmu <U*v, E(A + mu sigma_+ e*_{j_+})> >= c_+/(2 nu).
*Proof.* (a) ||x/||x|| - y/||y|| || <= ||x - y||/||y|| + | ||y|| - ||x|| |/||y|| <= 2||x - y||/||y|| with y = U*a, ||y|| = nu.
(b) The derivative equals sigma_+ <P_{E(A_mu)-perp} U*v, U*e*_{j_+}>/||U*A_mu||, A_mu := A + mu sigma_+ e*_{j_+}, a continuous function of
(A, mu) near (a, 0) in l_1 x R, with value c_+/nu at (a, 0). QED.

## 2.3 Theorem 1 (engineered recovery, Delta d = 0). PROVED.
Let f in S_{p*} with F = supp a finite, and let g in C(f) have an exact two-piece representation with a single active block and
Delta d = 0. Then g is in Ls(f): for every rho in (0,1) there are norm-attaining f'_n in S_{p*} and g'_n in C(f'_n)/rho with
(f'_n, rho g'_n) in NA((c_0,p), l_2^2) and (f'_n, rho g'_n) -> (f, rho g). Hence (f, rho g) is in cl NA for all rho < 1.
The approximants are engineered (window masses on the contacts, far sign-flipped contacts carrying negative masses, one
tuning mass fixed by the intermediate value theorem, a constant-theta tail); theta in [0,1] is arbitrary.

### Proof.
**Step 0 (constants; chosen from f and the representation only).** Fix rho, theta. Let eta_0 > 0 with rho^2 (1+eta_0)^3 <= (1+rho^2)/2.
Gamma := 1 + max(||b+||_1, ||b-||_1, ||v||_1); a_min := min_F |a_j|; gamma_min := min over m and k in supp omega+_m cup supp omega-_m of
gap_m(k) (> 0); W_max := max_{m,+-} ||omega+-_m||_inf; d_max := 1 + max_{m,+-} |d_m(omega+-_m)|; C_min := min_m C_m.
Choose T_0 in (0,1] with: T_0^2 <= (1 - rho^2)/2; 2 T_0 rho W_max <= gamma_min/4; 8 T_0 rho d_max (1 + 1/C_min) <= eta_0;
4 T_0 rho Gamma ||U||/nu <= eta_0/(1+eta_0) (Hilbert factor); 4 T_0 rho Gamma <= a_min/4; and T_0 K_c <= eta_0, where
K_c := 16 Gamma ||U||/nu + 8 d_max/C_min bounds the kappa of all certificates used below (A Def 4.1) once the data of f'
are within a factor 2 of those of f. Let j_+, sigma_+, c_+ be as in 2.1 and delta_1 as in 2.2(b).

**Step 1 (parameters for step n).** Write mx(N) := max{|v_j| : j in K, j > N} (> 0: supp v cap K is infinite, Lemma 1.2(d)).
 (i) Window: N_n -> infinity, N_n > max(F cup {j_+}), and 8 T_0 rho ||U*v|| max_{j > N_n} nu_j <= nu (nu_j := ||U*e_j*|| -> 0).
 (ii) D_n := mx(N_n) -> 0 and t_n := nu D_n/(16 ||U*v|| (||U|| + 1) Gamma) -> 0.
 (iii) Far_n := the shortest initial segment (in increasing order) of {j in K : j > N_n, v_j != 0} with sum_{Far_n} |v_j| >= D_n;
      then D_n <= sum_{Far_n} |v_j| <= 2 D_n (the last element added is <= mx(N_n) = D_n).
 (iv) N''_n > max Far_n with rho ||v 1_{K cap (N''_n, infinity)}||_1 <= 3(1 - rho^2) t_n/16 and ||v 1_{K cap (N''_n, infinity)}||_1 <= D_n.
 (v) Masses: m_{n,j} := 4 t_n |b_theta,j| for j in K cap [1, N_n]; far masses m'_{n,j} := 2 T_0 rho |v_j| for j in Far_n. For mu >= 0:
      A_n(mu) := a + sum_{j in K cap [1,N_n]} m_{n,j} z_j e_j* + mu sigma_+ e*_{j_+} - sum_{j in Far_n} m'_{n,j} z_j e_j*,
      a'_n(mu) := A_n(mu)/q*(A_n(mu));  z'_n := z on [1, N''_n] \ Far_n, -z on Far_n, 0 on (N''_n, infinity);
      x'_n(mu) := z'_n + U E(A_n(mu)).
For mu small, a'_n(mu) has the sign of a on F, z'_n is in c_00, |z'_n| <= 1, and z'_n = sign a'_n(mu) on supp a'_n(mu)
(F: z = sign a; window masses and a mass at j_+ in K carry sign z_j; far masses carry sign -z_j = z'_j). So by Fact D,
a'_n(mu)(x'_n(mu)) = q*(a'_n(mu)) = 1 = q(x'_n(mu)), and f'_n(mu) := grad p(x'_n(mu)) is norm attaining, with base data
(a'_n(mu), z'_n, E(A_n(mu))) and base contact xhat' = x'_n(mu).

**Step 2 (exact tuning by the intermediate value theorem).** Let psi_n(mu) := v(x'_n(mu)). Since v(zhat) = 0, supp v in F cup K, z'_n = z on F:
  psi_n(mu) = <U*v, E(A_n(mu)) - e> - 2 sum_{Far_n} |v_j| - ||v 1_{K cap (N''_n, inf)}||_1.          (2.3.1)
By 2.2(a) (||U*(A_n - a)|| <= nu/2 for n large; ||U*e_j*|| <= ||U||) and Step 1(i),(ii):
|<U*v, E(A_n(0)) - e>| <= (2||U*v||/nu)(4 ||U|| t_n Gamma + sum_{Far} m'_{n,j} nu_j) <= D_n ||U||/(2(||U||+1)) + (1/2) sum_{Far} |v_j|
<= D_n/2 + (1/2) sum_{Far} |v_j|. Hence, by (iii),(iv): psi_n(0) <= D_n/2 - (3/2) D_n < 0 and psi_n(0) >= -D_n/2 - 5 D_n - D_n >= -7 D_n.
Put mubar_n := 14 nu D_n/c_+ -> 0. For n large, ||A_n(mu) - a||_1 <= 4 t_n Gamma + mubar_n + 4 T_0 rho D_n <= delta_1 for mu in [0, mubar_n],
so by 2.2(b) psi_n(mubar_n) >= psi_n(0) + mubar_n c_+/(2 nu) >= 0. psi_n is continuous; choose mu_n in (0, mubar_n] with psi_n(mu_n) = 0.
From now on a'_n := a'_n(mu_n), x'_n := x'_n(mu_n), f'_n := grad p(x'_n), and all data of f'_n are primed.

**Step 3 (convergence).** ||A_n(mu_n) - a||_1 -> 0, so a'_n -> a in l_1; z'_n -> z coordinatewise (z'_n = z on [1, N_n], N_n -> infinity).
By Lemma 1.5, f'_n -> f, and for n large: supp omega+-_m is contained in Q'_{n,m} with gaps' >= gamma_min/2, C'_{n,m} >= C_m/2,
nu'_n >= nu/2, |a'_{n,j}| >= a_min/2 on F, |d'_{n,m}(omega+-_m)| <= d_max, q*(A_n(mu_n)) <= 4/3, and the block coefficients
H'_{n,m}(omega) -> H_m(omega) for omega in {omega+_m, omega-_m, omega_theta,m}. Moreover d'_{n,m_0}(Delta omega) = ell(x'_n)/|R_{m_0} x'_n| (Lemma 1.2(c),
homogeneity) = psi_n(mu_n)/|R_{m_0} x'_n| = 0 (ell = v as Delta d = 0); for m != m_0, Delta omega_m = 0. So Delta d'_{n,m} = 0 for all m.

**Step 4 (the target and its three decompositions).** s_n := -(b_theta 1_{[1,N_n]})(x'_n); since z'_n = z on [1, N_n],
(b_theta 1_{[1,N_n]})(x'_n) = (b_theta 1_{[1,N_n]})(zhat) + <U*(b_theta 1_{[1,N_n]}), E_n - e> -> b_theta(zhat) = 0 (Lemma 1.2(a),(f)); so s_n -> 0.
  b'_{0} := b_theta 1_{[1,N_n]} + s_n a'_n,   g'_n := b'_0 + sum_m R_m*( omega_theta,m - d'_{n,m}(omega_theta,m) w'_{n,m} ).
Then g'_n - g = -b_theta 1_{(N_n, inf)} + s_n a'_n + sum_m R_m*( d_m(omega_theta,m) w_m - d'_{n,m}(omega_theta,m) w'_{n,m} ) -> 0 in l_1.
Since Delta d'_{n,m} = 0, d'(omega_theta) = d'(omega+) = d'(omega-) blockwise, and with v = ell = R*_{m_0} Delta omega:
  g'_n = b'+ + sum_m R_m*(omega+_m - d'(omega+_m) w'_m),   b'+ := b'_0 + theta v = b+ 1_{[1,N_n]} + theta v 1_{(N_n,inf)} + s_n a'_n;
  g'_n = b'- + sum_m R_m*(omega-_m - d'(omega-_m) w'_m),   b'- := b'_0 - (1-theta) v = b- 1_{[1,N_n]} - (1-theta) v 1_{(N_n,inf)} + s_n a'_n.
Also b'_0(x'_n) = 0 and b'+-(x'_n) = +- (theta or 1-theta) psi_n(mu_n) = 0.
Coordinate structure (n large): on J (free coordinates) b'_0, b'+, b'- vanish; on supp a'_n they are dominated as described below;
on contacts in (N_n, N''_n] \ Far_n the entries theta v_j (resp. -(1-theta) v_j) are z-signed (resp. anti-z-signed); beyond N''_n they
are theta v_j (resp. -(1-theta)v_j) at coordinates with z'_n = 0.

**Step 5 (small scales |tau| <= min(2 t_n/rho, T_0): a two-sided finite certificate at f'_n).** c' := (b'_0, omega_theta) is a finite
certificate at f'_n (A Def 4.1): supp b'_0 in supp a'_n (F, the window contacts with b_theta,j != 0 carry masses, a'_n-multiple);
b'_0(x'_n) = 0; omega_theta,m in c_00(Q'_{n,m}). Ratios: on F, |b'_{0,j}|/|a'_{n,j}| <= 2 Gamma/a_min + |s_n|; on window mass coordinates
|b_theta,j| q*(A_n)/m_{n,j} + |s_n| <= 1/(3 t_n) + |s_n| (q*(A_n) <= 4/3); elsewhere on supp a'_n only |s_n|. So
1/||b'_0/a'_n||_inf >= 1/(1/(3t_n) + |s_n| + 2Gamma/a_min) >= 2 t_n for n large, and r(c') >= 2 t_n (the Hilbert and block radii are
bounded below independently of n). g_{c'} = g'_n. H(c') = max(h'(b_theta 1_{[1,N_n]}), H'_m(omega_theta,m)) ->
max(h(b_theta), H_m(omega_theta,m)) <= kappa <= 1 (Lemma 1.2(f); h' ignores multiples of a'_n), so H(c') <= 1 + eta_0 for n large; kappa(c') <= K_c.
A Prop 4.5 at f'_n for rho c' (H(rho c') = rho^2 H(c'), r(rho c') = r(c')/rho, kappa(rho c') <= kappa(c')): for |tau| <= min(2t_n/rho, T_0),
  p*(f'_n + tau rho g'_n) <= 1 + (tau^2/2) rho^2 (1+eta_0)(1 + K_c T_0) <= 1 + tau^2 rho^2 (1+eta_0)^2/2 <= 1 + tau^2 (1/2 - (1-rho^2)/4) <= s(tau),
using s(tau) >= 1 + tau^2/2 - tau^4/8 >= 1 + tau^2/2 - (1-rho^2) tau^2/16 for tau^2 <= (1-rho^2)/2.

**Step 6 (intermediate scales t_n <= |tau| <= T_0: one-sided decompositions).** Let 0 < tau <= T_0 (tau < 0 is symmetric with b'-, omega-):
  f'_n + tau rho g'_n = (a'_n + tau rho b'+) + sum_m R_m*( w'_m + tau rho (omega+_m - d'(omega+_m) w'_m) ).
Base (Lemma 1.4 with B := rho b'+, B(x'_n) = 0): no sign changes on supp a'_n: on F, |tau rho b'+_j| <= T_0 rho (Gamma + 1) <= a_min/2 <= |a'_{n,j}|;
on window mass coordinates tau b+_j has the sign z_j of a'_{n,j} (the s_n a'_n part only rescales a'_{n,j} by 1 + tau rho s_n > 0); on Far_n,
|a'_{n,j}| = m'_{n,j}/q*(A_n) >= (3/2) T_0 rho |v_j| >= (3/2)|tau rho theta v_j| (q*(A_n) <= 4/3), and the s_n a'_n part only rescales
a'_{n,j} by 1 + tau rho s_n >= 9/10, so no sign change; at j_+ in K the entry is z-signed. Kinks:
zero on J (entries 0), on contacts with z'_n = z (z-signed entries, tau > 0), and the only contribution is beyond N''_n:
kink'_tau(rho b'+) <= tau rho theta ||v 1_{K cap (N''_n,inf)}||_1 <= 3(1 - rho^2) tau t_n/16 <= 3(1-rho^2) tau^2/16 (tau >= t_n).
Hilbert: tau rho ||U*b'+|| <= T_0 rho Gamma ||U|| (1 + o(1)) <= nu'/2 and h'(b'+) -> h(b+) <= 1 (||b'+ - b+||_1 <= ||b+ 1_{(N_n,inf)}|| +
||v 1_{(N_n,inf)}|| + |s_n| -> 0; h'_n -> h uniformly on bounded sets since e'_n -> e, nu'_n -> nu), so for n large
  q*(a'_n + tau rho b'+) <= 1 + 3(1-rho^2) tau^2/16 + tau^2 rho^2 (1+eta_0)^2/2.
Blocks (A Lemma 4.4(d) at f'_n; |tau rho omega+_m(k)| <= gap'(k)/2 and the d-radii hold by the choice of T_0):
  N_m(w'_m + tau rho(omega+_m - d' w'_m)) <= 1 + (tau^2 rho^2/2) H'_m(omega+_m)(1 + eta_0) <= 1 + tau^2 rho^2 (1+eta_0)^2/2  (n large).
By Fact A, p*(f'_n + tau rho g'_n) <= 1 + tau^2 [rho^2(1+eta_0)^2/2 + 3(1-rho^2)/16] <= 1 + tau^2 [1/2 - (1-rho^2)/16] <= s(tau).
(The certificate of Step 5 covers |tau| <= t_n, so there is no gap between Steps 5 and 6.)

**Step 7 (large scales |tau| >= T_0: slack).** eps_n := p*(f'_n - f) -> 0, eta_n := p*(g'_n - g) -> 0 (Steps 3, 4; p* <= ||.||_1).
For n large, eps_n <= (1-rho^2) T_0^2/6 and rho eta_n <= (1-rho^2) T_0/6. Then for |tau| >= T_0, with A Lemma 4.7,
p*(f'_n + tau rho g'_n) <= p*(f + tau rho g) + eps_n + |tau| rho eta_n <= s(rho tau) + (1-rho^2) min(tau^2, |tau|)/3 <= s(tau)
(for T_0 <= |tau| <= 1: eps_n <= (1-rho^2)tau^2/6, |tau| rho eta_n <= (1-rho^2) tau^2/6; for |tau| >= 1 both are <= (1-rho^2)|tau|/6).

**Step 8 (conclusion).** For n large, p*(f'_n + tau rho g'_n) <= s(tau) for all real tau, i.e. rho g'_n in C(f'_n). By N_part1 Lemma 1.2(a),
(f'_n, rho g'_n) is a norm-one operator attaining its norm (at the normer of f'_n). It converges to (f, rho g). So (f, rho g) in cl NA for
every rho in (0,1), and g in Ls(f) (N_part1 Thm 1(iii)). QED.

Quantifier order (referee gap G3): rho, theta -> eta_0 -> T_0 (from f-data only) -> for each n: N_n -> D_n, t_n -> Far_n -> N''_n ->
mu_n (IVT, depends on all previous choices) -> f'_n, g'_n; then "n large" for the convergence statements of Steps 3-7.

## 2.4 What was fixed relative to P1 6.3 / referee report (C4)
 * (G1) g in C(f) is a hypothesis (used only in Step 7).
 * (G2) No coordinate with fractional value of z' is used: the exact zero psi_n(mu_n) = 0 is obtained from a continuous MASS parameter
   (IVT on mu), not from a partial pull z'_{j*} in (-1,1); the only first-order cost is the v-tail beyond N''_n, chosen after t_n.
 * (G3) Order of quantifiers as above. Also: the far pulls need no a-priori relation "t_m <= c tau_N": D_n := mx(N_n) automatically
   guarantees a far set with pull in [D_n, 2D_n].
 * The tuning direction always exists (Lemma 2.1); if c_j != 0 for some j in F, the tuning mass works in both directions and the
   far pulls can be dropped (Far_n := empty, mu in [-mubar_n, mubar_n]).

## 2.5 Corollary (P1's example; rigorous version of P1 6.3). PROVED.
Let T, f be as in P1 §2 (any finite I containing 1), u := u_{2,1}, lambda_0 := Phi_1(2). Every g in C(f) for which there are
mu+ <= inf_{j in K'} g_j/u_j and mu- >= sup_{j in K'} g_j/u_j with max( h(g - mu+- u), (mu+-)^2/C_1 ) <= 1 lies in Ls(f). In
particular this holds for the whole slab of P1 6.2 and for every two-piece mate g_{K_1} of P1 2.3 (0 < c <= c_*), i.e. the explicit
defect of P1 Thm 2.4 is recovered along engineered NA sequences.
*Proof.* By P1 6.1, g is in E_u. The representation b+- := g - mu+- u, omega+- := (mu+-/lambda_0) e_2 (block 1) satisfies (E1)
(supp in {1} cup K'; z_j(g_j - mu+ u_j) = u_j(g_j/u_j - mu+) >= 0 and similarly <= 0 for mu-), (E2) (Q_1 = {2}), (E3) (R_1*(e_2/lambda_0) =
u and d_1(e_2) = Phi_1(2)^2 w_1(2)/C_1 = 0), (E4) by hypothesis (H_1((mu/lambda_0) e_2) = (Phi_1(2) mu/lambda_0)^2/C_1 = mu^2/C_1 because
D_1 e_2 is orthogonal to D_1 w_1). Single active block, Delta d = 0. Apply Theorem 1. For the slab: P1 6.2's proof gives the
coefficients O(||theta||^2) small. For g_{K_1}: mu+ = 0, mu- = c, and P1 2.3's bounds give the coefficients <= 1 for c <= c_*. QED.
Remark. Whether ALL of C(f) at P1's example is recovered is not settled here: for g in C(f) whose explicit decompositions have
coefficient > 1, the actual decompositions rebalance at second order (peak/level shifts, transfer peaks); Theorem 1 would have to be
combined with a shifted / transfer-peak version at the engineered approximants (C_notes Thm 7.4). OPEN (plausible).

## 2.6 Remark (several active blocks). SKETCH.
If |I_act| >= 2 (all Delta d_m = 0), Step 2 must achieve ell_m(x'_n) = 0 for every active m. Since sum_m ell_m = v vanishes on J, the
v-condition is tuned as above (it is insensitive to free coordinates), and the remaining |I_act| - 1 conditions can be tuned by
o(1) moves of finitely many near free coordinates (which do not change v(x'_n)) PROVIDED the restrictions {ell_m|_J} have rank
|I_act| - 1 (no second resonance inside span{ell_m}). Under this rank condition the proof goes through verbatim (the tuning of the free
coordinates is a linear system with a fixed invertible matrix, solved after mu_n; its effect on v(x'_n) is nil).
# N2 part 3: exact two-piece mates with Delta d != 0 (the E_referee d-coefficient issue and the C_referee kink class)

Setting of parts 1-2: single active block m_0 (drop the index), Delta d := Delta d_{m_0} != 0, v = ell - Delta d R*w, ell = R*Delta omega.
The construction of Theorem 1 (window masses, far pulls, tuning mass, target g'_n := b'_0 + sum R*(omega_theta - d'(omega_theta) w')) is
kept; what changes is the block part of the one-sided decompositions and the tuning condition.

## 3.1 Lemma (general mismatch identity). PROVED.
Let f' be any NA approximant as in Theorem 1 with supp Delta omega in Q', let theta in [0,1], c+, c- real, and put
  Omega'+- := omega+- - d'(omega+-) w' + c+- (w' - w)   (block m_0; other blocks as in Theorem 1),
  b'+- := g' - L*Omega'+-  (so that g' = b'+- + L*Omega'+- exactly). Then, with Delta d' := d'(Delta omega) = ell(x')/|R x'|:
  b'+ = b'_0 + theta v + theta (Delta d - Delta d') R*w' - (theta Delta d + c+) R*(w' - w),
  b'- = b'_0 - (1-theta) v - (1-theta)(Delta d - Delta d') R*w' + ((1-theta) Delta d - c-) R*(w' - w),
and b'+-(x') = -c+- Bx,   Bx := <w' - w, R x'> = |R x'| - <w, R x'> >= 0  (the Bregman excess of w at R x').
Moreover ell(x') - Delta d |R x'| = v(x') - Delta d Bx, so the tuning condition Delta d' = Delta d is psi~(x') := v(x') - Delta d Bx = 0.
*Proof.* Algebra: L*(omega_theta - omega+) = theta ell, d'(omega_theta) - d'(omega+) = theta Delta d', ell = v + Delta d R*w, and
R*w = R*w' - R*(w' - w); similarly for the minus side. b'+-(x') = g'(x') - <Omega'+-, L x'> with g'(x') = 0 and
<omega - d'(omega) w', R x'> = 0 (A Lemma 4.2 at f'), <w', R x'> = |R x'|. The last identity: ell(x') = v(x') + Delta d <w, R x'>. QED.
Consequences. To make both mismatch terms vanish one needs Delta d' = Delta d and c+ = -theta Delta d, c- = (1-theta) Delta d. Then
b'+ = b'_0 + theta v and b'- = b'_0 - (1-theta) v exactly as in Theorem 1, but the base first-order terms are
tau rho theta Delta d Bx (side +) and -tau rho (1-theta) Delta d Bx (side -), and the block parts contain c+-(w' - w).

## 3.2 Lemma (the block convexity mechanism works iff tau c <= 0). PROVED.
(a) If tau c <= 0 then, with s := -tau rho c in [0, 1/2], N(w' + tau rho(omega - d'w') + tau rho c (w' - w)) <= 1 + (tau^2 rho^2/(2(1-s))) H'(omega)(1 + ...)
    (Lemma 1.3 with y = w, N(w) = 1). No first-order cost at all.
(b) If s := -tau rho c < 0 and w' has a peak k outside supp omega with w(k) = -(M/M') w'(k) (a common peak with opposite sign), then
    N(W) >= 1 + 2 M |s|,  W := w' + tau rho (omega - d' w') + s (w - w').
*Proof of (b).* At k: sigma' W(k) = (1 - tau rho d' - s) M' + s sigma' w(k) = (1 - tau rho d') M' + |s| (M' + M). By Cauchy-Schwarz
||D W|| >= <D W, D w'>/C' = (1 - tau rho d' - s) C' + tau rho d' + s <Dw, Dw'>/C' >= (1 - tau rho d') C' + tau rho d' + |s| C' - |s| C
(<Dw, Dw'> <= C C'). Adding: N(W) >= |W(k)| + ||DW|| >= (1 - tau rho d')(M' + C') + tau rho d' + |s|(M' + M + C' - C) = 1 + |s|(1 + M - C) = 1 + 2M|s|. QED.

## 3.3 Lemma (common peaks of opposite sign are unavoidable). PROVED.
Let f in S_{p*} be NOT norm attaining and f' in S_{p*} norm attaining (normer in c_0). Then in every block m there are infinitely many k
which are peaks of both w_m and w'_m, with w'_m(k) w_m(k) < 0.
*Proof.* zhat is not in c_0 and xhat' is in c_0 \ {0}, so they are linearly independent elements of l_inf = (l_1)*; hence y -> (y(zhat), y(xhat'))
maps l_1 onto R^2, and there is y in S_{q*} with y(zhat) =: 2 delta > 0 > -2 delta' := y(xhat'). By (T2) the tail of (u_{k,m})_k is dense in
S_{q*}: infinitely many k satisfy q*(u_{k,m} - y) < min(delta, delta'), so u_{k,m}(zhat) > delta and u_{k,m}(xhat') < -delta' (q**(zhat) = 1 =
q(xhat')). By Fact C (k is a peak as soon as |u_{k,m}(xi)| > theta_m Phi_m(k), theta_m := M_m |zeta_m|/(m C_m), and Phi_m(k) -> 0), all but finitely
many of these k are peaks of w_m with sign + and of w'_m with sign -. QED.

## 3.4 Corollary (Delta d < 0: one side cannot use the convexity mechanism). PROVED.
If Delta d < 0, no choice of theta in [0,1] makes both c+ = -theta Delta d <= 0 and c- = (1 - theta) Delta d >= 0. For any choice, on the
side where tau c > 0 the block part of the exact-mismatch-free decomposition of 3.1 has N(W) >= 1 + 2M |tau| rho |c| (3.2(b), 3.3: the
common opposite peaks are fine coordinates, outside supp omega), a first-order excess that exceeds the slack s(tau) - s(rho tau) <= (1-rho^2)tau^2/2
for all |tau| < 4M|c|/(1-rho^2)... i.e. at every small scale. Hence for Delta d < 0 the mismatch Delta d R*(w' - w) must be put into the base on
at least one side (theta = 0: side -, c- := 0), where it costs the KINK of Delta d R*(w' - w) at f' (Lemma 1.4).
This makes precise why E_referee's repair covers exactly Delta d >= 0.

## 3.5 Theorem 2 (Delta d > 0). PROVED under (BR); (BR) PROVED under two-sided mass tuning.
Let f, g be as in Theorem 1 but with Delta d > 0. Suppose
 (BR) the engineered approximants of Theorem 1 can be chosen with Bx_n := |R x'_n| - <w, R x'_n> = o(t_n) (t_n the window-mass scale).
Then g is in Ls(f). (BR) holds in particular under
 (TT) two-sided mass tuning: c_j != 0 for some j in F, or z_j c_j takes both signs on K (c_j := <P_{e-perp} U*v, U*e_j*>).
*Proof.* Use Lemma 3.1 with c+ = -theta Delta d, c- = (1-theta) Delta d and tune psi~ = v - Delta d Bx to 0 (Step 2 of Theorem 1 with psi_n
replaced by psi~_n; this is possible because d/dmu Bx(x'_n(mu)) = <J(R x'_n(mu)) - w, R U dE/dmu> -> 0 uniformly for mu in [0, mubar_n] (J is
norm-to-weak* continuous at R**zhat, dE/dmu ranges in a norm-compact set), so psi~_n still has derivative >= c_+/(4 nu), and Bx_n(0) -> 0).
Then b'+ = b'_0 + theta v, b'- = b'_0 - (1-theta) v, and the base first-order terms are rho |tau| (theta or 1-theta) Delta d Bx_n, which by
(BR) is <= (1-rho^2) tau^2/32 for |tau| >= t_n, n large. Block parts: Lemma 3.2(a) (tau c+- <= 0 on both sides; s <= T_0 rho Delta d <= 1/2 by
the choice of T_0). Everything else is Steps 3-8 of Theorem 1 verbatim (Lemma 1.4 with B(xhat') != 0 adds tau B(xhat') to the bound).
(TT) => (BR): with (TT) the tuning mass can move psi~ in both directions, so Far_n := empty (Remark 2.4) and the only far modification is
z'_n = 0 beyond N''_n. Then, by convexity of |.| (|R**zhat| >= |R x'| + <w', R**zhat - R x'>),
  Bx_n <= <w'_n - w, R(x'_n - zhat)> <= ||U|| ||E_n - e|| sum_k lambda_k |w'_n(k) - w(k)| + 2 theta_{N''_n},
θ_N := sum_k lambda_k ||u_k 1_{(N,inf)}||_1. Here ||E_n - e|| = O(t_n + mu_n) = O(t_n) (deficit O(t_n), no pulls), sum_k lambda_k |w'_n(k) - w(k)| -> 0
(dominated convergence, Lemma 1.5), and N''_n is chosen after t_n with theta_{N''_n} <= t_n^2. So Bx_n = o(t_n). QED.
Without (TT) the far pulls contribute <w' - w, R(z'_n - z) 1_{Far_n}> to Bx_n, i.e. at most 2 sum_k lambda_k |w'_n(k) - w(k)| |u_k|(Far_n), to be
compared with t_n ~ sum_{Far_n} |v_j|: a comparison between the far tails of v and of the other block vectors (T-dependent; it holds e.g.
for P1-type T, where the only block vectors with mass on K' far out are v-multiples and very fine targets). Status: SKETCH.

## 3.6 Theorem 3 (Delta d < 0). PROVED conditionally on (PC).
Let f, g be as in Theorem 1 but with Delta d < 0. Take theta := 0 and c+ = c- := 0; tune psi~ = v + |Delta d| Bx to 0 (as in 3.5). Then
side + is the certificate itself (b'+ = b'_0), and side - is b'- = b'_0 - v + E'_n with E'_n := Delta d R*(w'_n - w) and b'-(x'_n) = 0.
Suppose
 (PC) sum_{j in G_n} |E'_{n,j}| = o(t_n), where G_n := (complement of supp a'_n) cup {j in supp a'_n : 2 T_0 rho |E'_{n,j}| > |a'_{n,j}|}.
Then g is in Ls(f).
*Proof.* As Theorem 1; on side - (tau < 0) Lemma 1.4 gives the extra first-order term kink'_tau(rho E'_n) <= 2 |tau| rho sum_{G_n} |E'_{n,j}|
(on supp a'_n \ G_n there is no sign change), which is <= (1-rho^2) tau^2/32 for |tau| >= t_n, n large; h'(b'-) -> h(b-) since ||E'_n||_1 -> 0
(Lemma 1.5: R*w'_n -> R*w). QED.
Remarks. (1) Absorbing masses. One may add to a'_n masses of sign z'_j on any contact and on far free coordinates (setting z'_j = +-1 there,
which is allowed beyond a level N_0 -> infinity): then G_n shrinks to the NEAR FREE coordinates J cap [1, N_0] plus the tail beyond N''_n, but
E'_n depends on these masses (they move e'). So (PC) is a genuine fixed-point/pinning requirement: the approximants must keep
R*(w'_n - w) small on the near free coordinates at the precision o(t_n), where t_n is the very scale of the window masses that perturb e'.
(2) Why the requirement is scale-invariant (and therefore not automatic): the window masses move e' by ~ t_n, hence R x' by ~ t_n near the
coarse coordinates, hence w' at off-peak coordinates with Phi >= t_n by ~ t_n/Phi, hence R*(w' - w) by ~ t_n per off-peak coordinate of
scale >= t_n (A_referee 5.5, E_referee 2.7). Enlarging the masses enlarges t_n and the perturbation in the same proportion.

## 3.7 Proposition (cases where (PC) holds). SKETCH.
(a) Block-tame carrier block with robust peaks. Suppose Q_{m_0} = {k_0} (only one strict non-peak in the carrier block), no degenerate peaks,
margin sparsity (MS): sum{lambda_k : k in P_{m_0}, mu_k < s} = o(s), and (TT). Then for block m_0 the "pinning conditions" reduce to the single
tuned scalar: writing R*w = lambda_0 w(k_0) u_{k_0} + M pi, pi := sum_{k in P} sigma_k lambda_k u_k, one has
  v(x') = Delta d M pi(zhat) [ u_{k_0}(x')/u_{k_0}(zhat) - pi(x')/pi(zhat) ]   (exact; uses v(zhat) = 0, u_{k_0}(zhat) != 0 since Delta d != 0),
and, by the converse of Fact C (zeta' = c'(alpha' + D^2 w/C) with alpha' >= 0 on P, ||alpha'||_1 = 1 implies J(zeta') = w), the conditions
"ratio at k_0 = ratio of the peak sum" and "every peak of w stays above the old threshold at x'" give w'_{m_0} = w_{m_0} EXACTLY. So after
tuning v(x'_n) ~ 0, w'_n - w is generated only by the coordinates whose threshold condition fails: near perturbations of size O(t_n) flip
only peaks with margin O(t_n) (total lambda-mass o(t_n) by (MS)), the far modification beyond N''_n flips a lambda-mass that tends to 0
as N''_n -> infinity (no degenerate peaks) and can be made o(t_n). A perturbation estimate for J (the global data M', C', zeta'(k_0) react to
the flipped coordinates only through quantities bounded by their lambda-mass) then gives ||E'_n||_1 = o(t_n), hence (PC).
The perturbation estimate for J at flipped coordinates is the step not written in full (hence SKETCH).
(b) Without (TT) the far pulls flip peaks with ||u_k 1_{Far_n}|| >~ mu_k; (PC) then needs sum{lambda_k : mu_k <= 2 ||u_k 1_{Far_n}||_1} = o(sum_{Far_n} |v_j|),
a comparison of far tails (T-dependent; true for P1-type T).
(c) Infinitely many strict non-peaks in the carrier block (the generic case of Preprint A): pinning needs ~ log(1/t_n) conditions (one per
off-peak coordinate of scale >= t_n) solved by tuning variables with condition numbers that must be o(1/t_n) relative to t_n: a
QUANTITATIVE TAIL-INDEPENDENCE property of T at f. Neither proved nor refuted. OPEN.

## 3.8 Existence of Delta d < 0 mates (so 3.6 is not vacuous). SKETCH.
In P1's construction (P1 2.1) replace the special vector by u_{2,1} := (h - kappa' pi)/n, where h is supported on {1} cup K', z-signed on K',
h(zhat) = 0, pi := sum_{(k,1) != (2,1)} sigma_k lambda_{k,1} u_{k,1} (signs sigma fixed by the robust-peak design, which does not involve u_{2,1}),
and kappa' is small. With all block-1 coordinates except (2,1) peaks, R_1*w_1 = lambda_0 w_1(2) u + M_1 pi, and a direct computation gives
for c u: v = c u - (c u(xi)/|zeta_1|) R_1*w_1 = (c M_1 pi(xi)/(n |zeta_1|)) h (the pi-coefficient is -(c M_1/(n |zeta_1|)) h(xi) = 0), so v is
supported on {1} cup K', z-signed: an exact resonance with Delta d = c u(xi)/|zeta_1| = -c kappa' pi(xi)/(n |zeta_1|), negative for c kappa' > 0.
(2,1) stays a strict non-peak for kappa' small (|u(xi)| below the threshold). Injectivity / Y cap c_00 = {0} follow as in P1 2.1 (h carries a
signature on S_{l_0}). The two-piece mates g_{K_1} are then constructed as in P1 2.3 (second-order coefficients small for c small).

## 3.9 The kink class of C_referee 1.20 (infinitely many kinks). PROVED identification + consequences.
By 1.6, a one-sided first-order re-split through kinks is an exact two-piece representation with Delta d = -(s+ - s-) c'/M. Hence:
 * if the re-splitting block vector v'' has c' < 0 (Delta d > 0): recovered by Theorem 2 under (TT) (or (BR));
 * if c' > 0 (Delta d < 0): recovered by Theorem 3 under (PC); in the C_referee configuration J is FINITE (K cofinite), so the near free
   coordinates form a fixed finite set and (PC) is a finite set of pinning conditions (|J| scalars) plus absorbing masses on contacts:
   SKETCH-level plausible, not proved;
 * if c' = 0 (no peak component; Delta d = 0): recovered by Theorem 1.
In all cases the mate must ALSO satisfy kappa <= 1 for its re-split decompositions (that is how it is a mate when Gamma_w > 1).
So "supports with infinitely many kinks" do not create a new mechanism: they are exact resonances, and the open part is exactly the
Delta d < 0 pinning problem.

## 3.10 Summary for exact resonances
| class | status |
|---|---|
| exact two-piece, Delta d = 0, one active block | recovered along engineered NA sequences: PROVED (Thm 1) |
| several active blocks, all Delta d_m = 0 | PROVED under a rank condition (Remark 2.6, SKETCH of the tuning step) |
| Delta d > 0, two-sided mass tuning (TT) | PROVED (Thm 2) |
| Delta d > 0 without (TT) | PROVED under (BR); (BR) is a far-tail comparison (SKETCH, T-dependent) |
| Delta d < 0 | PROVED under (PC) (Thm 3); the convexity mechanism provably fails on one side (3.4); (PC) SKETCH in block-tame robust cases (3.7a), OPEN in general (needs quantitative tail independence, 3.7c) |
| C_referee kinks | = exact resonances with Delta d = -(s+ - s-)c'/M (3.9): covered by the rows above |
# N2 part 4: approximate resonances, conversion capacity, and the rigid design versus Lemma B

## 4.1 Exact versus approximate resonances (what parts 2-3 do and do not use)
An exact resonance (part 1) is a SCALE-FREE transfer v = L*(Delta omega - Delta d w) supported on F cup K and z-signed on K. Engineering
(Theorems 1-3) uses: masses on finitely many window contacts (two-sided base usage at small scales), the contacts beyond the window
with their own signs (one-sided usage at intermediate scales), far negative masses (free pulls), and a scalar tuning. NO block coordinate
of f has to change status, and NO conversion of one-sided block carriers is needed: the carrier set Q_{m_0} is finite and robust.
An approximate resonance is a family of scale-dependent transfers: at scale t the two sides use DIFFERENT one-sided carriers of depth
Phi ~ t (weak peaks, near-threshold strict non-peaks used beyond their gap, near-contacts, near-flip base coordinates), which represent
the same component of g up to O(t) (A §7.2, P1 3.4-3.6). Known intrinsic results: near-threshold strict non-peak carriers with
sum of gaps = infinity give mates in cl Cert(f) (P1 4.4); single-family carriers with gaps bounded below are certificates + O(t)
(A Cor 6.10(c)). Open intrinsically: summable gaps, weak-peak carriers, near-contact carriers with rooms -> 0 in a summable way.

## 4.2 Proposition (cross-block near-duplicates). PROVED.
(a) (P1 4.2, sign rule) If u_{n,m} and u_{n,m'} differ by o(Phi) in the xi-direction, they serve the same side; they cannot switch.
(b) Exact duplicates u_{n,m} = u_{n,m'} ((n,m) != (n,m')) do not exist (T injective; A Fact F, E Lemma 6.3).
(c) If the difference of two (possibly cross-block) carriers is, up to the d-terms, a contact vector, i.e.
    c(u_{n,m}/... ) relation  v := c u_{n,m} - c' u_{n',m'} - Delta d_m R_m* w_m + Delta d_{m'} R_{m'}* w_{m'} supported on F cup K and z-signed,
    with (n,m), (n',m') strict non-peaks, then the two-piece mates built on this transfer (P1 2.3 construction) are EXACT two-piece mates
    with two active blocks; they are recovered by Theorem 1 + Remark 2.6 when Delta d_m = Delta d_{m'} = 0 and ell_m|_J != 0 (rank condition:
    ell_m|_J = -ell_{m'}|_J since v vanishes on J), and fall under part 3 otherwise (multi-block versions of Thms 2-3: SKETCH).
(d) Martin's built-in near-duplicates (same w'_n in every block) are approximate in general: their differences are the unknown
    perturbations of [16, Prop 2.8], not contact vectors; they create switching only if the perturbations are >~ Phi in the xi-direction
    with opposite signs at every scale (P1 4.2), i.e. an approximate resonance treated below.
*Proof.* (a),(b) quoted. (c): the representation is exact two-piece by construction (Def 1.1), with I_act = {m, m'}; the rank condition is
as stated. QED.

## 4.3 Theorem 4 (recovery through converted or implanted carriers at the approximant; conditional). PROVED.
Let f in S_{p*}, g in C(f), rho in (0,1), T_0 in (0, sqrt((1-rho^2)/2)]. Let f' in NA cap S_{p*}, gbar, h_1, ..., h_J in X*, Q, kappa >= 0 and
scales s_j := s_1 2^{j-1} (s_J <= T_0) satisfy
 (HC) p*(f' + t h_j) <= 1 + Q t^2/2 for |t| <= s_j      (two-sided structure at f' down to scale s_j: CONVERTED or implanted carriers),
 (HT) p*(f' + t gbar) <= 1 + Q t^2/2 for s_1 <= |t| <= T_0   (the structure of f transferred to f' above the boundary scale s_1),
 (HE) p*(h_j - gbar) <= kappa s_j                          (frozen error of the order of its own scale),
with Q <= 1 - 3(1-rho^2)/8 and J >= 16 kappa/(1-rho^2). Put g' := (1/J) sum_j h_j (so p*(g' - gbar) <= 2 kappa s_J/J). Then
p*(f' + t g') <= s(t) for |t| <= T_0. If moreover eps := p*(f' - f) <= (1-rho^2) T_0^2/6 and eta := p*(g' - rho g) <= (1-rho^2) T_0/6, then
g' is in C(f') and (f', g') is in NA. Consequently: if for every rho < 1 there is T_0 > 0 such that data as above exist with eps, eta -> 0,
then g is in Ls(f), i.e. (f, rho g) is in cl NA for all rho < 1.
*Proof (the skeleton of E notes 2.1, re-derived).* By convexity, p*(f' + t g') <= (1/J) sum_j p*(f' + t h_j). For j with s_j >= |t| use (HC);
for s_j < |t| (so |t| >= s_1) use p*(f' + t h_j) <= p*(f' + t gbar) + |t| kappa s_j and (HT). Since sum_{s_j < |t|} s_j <= 2|t|, for |t| <= T_0:
p*(f' + t g') <= 1 + Q t^2/2 + 2 kappa t^2/J <= 1 + t^2 [1/2 - 3(1-rho^2)/16 + (1-rho^2)/8] = 1 + t^2 [1/2 - (1-rho^2)/16] <= s(t)
(s(t) >= 1 + t^2/2 - t^4/8 and t^2 <= (1-rho^2)/2). For |t| >= T_0: p*(f' + t g') <= p*(f + t rho g) + eps + |t| eta <= s(rho t) +
(1-rho^2) min(t^2,|t|)/3 <= s(t) (A Lemma 4.7, as in Theorem 1 Step 7). N_part1 Lemma 1.2(a) gives (f', g') in NA; the last
statement follows from N_part1 Thm 1. QED.
Comment. The theorem isolates exactly what engineering must provide for an approximate resonance: (HT) (transport of the one-sided
structure above a boundary scale; the carriers used at scales >= s_1 must keep their statuses at f' and the destroyed finer carriers must
contribute only O(t) at scale t >= s_1 — the bookkeeping of E 2.1 (H-transfer), HEURISTIC in general) and (HC)+(HE) at J(rho) ~ 16 kappa/(1-rho^2)
ADJACENT DYADIC SCALES just below the boundary. Note that J(rho) is finite for each rho: one does not need infinitely many conversions
for a given rho, but J(rho) -> infinity as rho -> 1 (E's Model M/N: R(J) -> 1 only as J -> infinity).

## 4.4 Conversion capacity (definition, sources, limits)
Definition. At f, for a family of one-sided carriers (k_i) of a switching mate, the CONVERSION CAPACITY is
  CC(f) := sup{ J : for every eps > 0 there is an NA f' with p*(f' - f) <= eps at which J carriers of adjacent dyadic depths just below the
            boundary scale of f' are strict non-peaks with gaps bounded below (two-sided) and the coarser carriers keep their status }.
Sources (all with the refereed estimates):
 (S1) window moves and Delta a act on the carriers u_k = (v + K lambda_k sigma_k + far_k)/n_k only through ONE absolute scalar V = v(x' - xhat)
      up to o(lambda_k) (E Prop 8.2, PROVED); one scalar converts one carrier TYPE in one band of scale ratio (2+delta)/delta (E 2.4, re-derived
      by E_referee 2.7);
 (S2) far tails: carrier k can be shifted by any s with |s| < tau_k (free tail mass relative to the guards, E Lemma 6.1/Cor 6.2, PROVED,
      room factor 2-4 by E_referee 2.10) without disturbing the guards; conversion needs |s| ~ theta Phi_k; so each carrier with
      tau_k >~ Phi_k is individually convertible;
 (S3) detector-group scalars (E Lemma 6.4): one per group of carriers whose far parts are proportional to one detector psi_n.
So CC(f) = infinity whenever infinitely many carriers near every scale have free tail mass >~ Phi_k relative to the coarser guards
("quantitative tail independence at scale"). The adversarial alternative is FAR RIGIDITY: tau_k << Phi_k for all carriers, with far parts
collinear inside long groups (E (A2), far half). Then CC(f) <= (number of independent group scalars at a transition) + 1 <= 3 (E 8.3).

## 4.5 Proposition (far rigidity is compatible with Lemma B). SKETCH (adaptation of the PROVED construction P1 2.1).
For every prescribed family of "carrier" vectors y_i in c_00 (with prescribed scales) and every sequence eps_i -> 0 there is an admissible T
(Lemma B's conclusion: norm one, injective, Ran T cap c_00 = {0}, each block's normalized vectors dense in S_{q*}) whose block vectors include
u_i = (y_i + delta_i (psi_{n(i)} + eps_i h_i))/norm, where the detectors psi_n have pairwise disjoint supports G_n, the signatures h_i have pairwise
disjoint supports S_i disjoint from all G_n and from all supp y, and delta_i, eps_i are as small as we wish. In particular the free tail mass of
u_i relative to the other members of its group is <= delta_i eps_i ||h_i|| << Phi_i: far rigidity (E (A2), far half) holds.
*Sketch.* Copy P1 2.1: targets y^{(l)} dense in S_{q*} with "allowedness" (a target index is used at position l only if its support avoids all
signature sets S_{l'} at which it could compete with the signature coefficient c_{l'} delta_{l'} eps_{l'}); signature tails delta_l eps_l h_l on S_l;
detector parts delta_l psi_{n(l)} supported on G_{n(l)}, disjoint from all S. Injectivity and Ran T cap c_00 = {0}: for Z = sum x_l c_l u_l in c_00 and
s in S_{l'} far out, Z(s) = x_{l'} c_{l'} delta_{l'} eps_{l'} 2^{-s}/n_{l'} + (target contributions, bounded by allowedness), exactly P1's estimate
with delta_{l'} replaced by delta_{l'} eps_{l'}; detectors do not meet S_{l'}. Density: delta_l -> 0 along each block. Norm one: c_1 = 1 as in P1.
The only change is bookkeeping of the constants. (Not written out in full: SKETCH.)
Consequence. Lemma B does NOT force unbounded conversion capacity through source (S2). The E_referee objection "the NC design constraint
contradicts density" concerns a different constraint ("every coordinate with j-mass carries errors >= eps_0 (j-mass)"), which indeed
contradicts density (density requires approximants of e_j*/q*(e_j*) with arbitrarily small error); its RATE version (good approximants of the
core directions occur only at scales lambda_k <= psi(error), psi decaying as fast as one likes) is compatible with Lemma B by the same
construction (the target sequence may be visited arbitrarily late in each block).

## 4.6 What is NOT settled by 4.5 (why the rigid design is not an obstruction)
 (i) A switching mate through one-sided carriers needs a non-NA f whose block statuses are tuned (near-threshold peaks of both signs at all
     scales, E (A1)) — a fixed-point problem between T and f; P1 2.1/2.2 show such fixed points can be engineered for finitely many
     prescribed statuses with robust margins; near-threshold statuses at ALL scales are not constructed anywhere (OPEN, plausible).
 (ii) Even with CC(f) bounded, Theorem 4 can use OTHER two-sided carriers for (HC): implanted fine coordinates (A Lemma 8.2: a fine k with
     u_k close to a target plus a far handle can be set off-peak with w'(k) = 0 at f'), converted generic coordinates of FINE detector groups
     whose scalars are free (E 7.5 (C1)), coarse one-sided carriers of the core directions (C2), combinations (C3). Their usefulness depends on
     approximation RATES of the dense generic family: a carrier at depth lambda used at its own scale must have error O(lambda) ("implant scale
     gap", C Round 1). Lemma B allows arbitrarily slow rates, but slow rates for a FIXED target only push good approximants to fixed (eventually
     coarse) scales, where they are matched rather than convertible (E 7.5). Whether an adversary can block (C1)-(C3) simultaneously with (A1)-(A5)
     is OPEN; no consistent complete design is known (E 7.5, E_referee 4).
 (iii) Model N's positive excess R(J) - 1 (1.2%-19% for J <= 4) is NUMERICAL in a cost model that optimizes only over frozen + transfer
     representations; it is not a lower bound for p* over all decompositions at all approximants.

## 4.7 Answer to task item 2 (precise limit of engineering)
 * For EXACT resonances the decisive quantities are not conversion capacities: Delta d = 0 needs nothing beyond Lemma B (Theorem 1);
   Delta d > 0 needs the scalar Bregman condition (BR) (automatic under two-sided mass tuning, Thm 2); Delta d < 0 needs the pinning condition
   (PC) on the NEAR FREE coordinates (Thm 3), which in the generic case (infinitely many strict non-peaks in the carrier block) is a quantitative
   tail-independence statement at the scale of the window masses (3.7c). Conversely (3.4) the convexity mechanism provably cannot replace (PC).
 * For APPROXIMATE resonances the decisive quantity is the conversion capacity at the destruction boundary, or more generally the supply of
   two-sided carriers with frozen errors O(scale) at J(rho) ~ 16 kappa/(1-rho^2) adjacent scales below the boundary (Theorem 4). Sufficiency:
   PROVED conditionally (Thm 4) given the transport hypothesis (HT) (itself HEURISTIC in general). Necessity: OPEN — and I see no way to prove it,
   because (HC) can be met by carriers that are not conversions of the original ones (4.6(ii)); a necessary-and-sufficient property of T is
   therefore NOT identified. What IS established: (a) unbounded conversion capacity through far tails is not implied by Lemma B (4.5); (b) the
   only rigorous link between T and recovery for one-sided block carriers is through free tail masses (Cor 6.2) and the absolute scalar V (Prop 8.2).
 * Can an admissible T violate the sufficient conditions at some f? For approximate resonances: far rigidity (violating (S2)) is consistent with
   Lemma B (4.5, SKETCH); whether this can be combined with a non-NA f carrying a switching mate and with blocking of (C1)-(C3) is OPEN. For exact
   resonances with Delta d < 0: a P1-type T with Delta d < 0 exists (3.8, SKETCH), and there (PC) holds up to a far-tail comparison (3.7(a),(b)):
   no violation known.
# N2 part 5: can engineering provably fail? (task item 3), localization of any obstruction, numerics, assessment

## 5.1 What a non-recovery proof must show (reformulation; PROVED in N_part1)
By N_part1 Thm 1 and Prop 1.5(c), (f, rho g) is NOT in cl NA for some rho < 1 iff rho g is not in Ls(f) iff there are x_1, ..., x_k in c_0 and
delta > 0 with  max_i ( rho g(x_i) - r~_{f'}(x_i) ) >= delta  for EVERY f' in NA cap S_{p*} with p*(f' - f) < delta,
where r~_{f'}(x) = max{h(x) : h in C(f')} = inf{ sum_j (p(y_j)^2 - f'(y_j)^2)^{1/2} : sum_j y_j = x }.
So a counterexample needs UPPER bounds for r~_{f'} uniformly over all NA f' near f, i.e. for every such f' explicit primal
decompositions of the x_i that make the excess p - f' large. Every engineering device (masses on contacts, far flips with negative
masses, tuning masses, implanted off-peak coordinates, transfer peaks, averaging over scales) LOWERS such upper bounds in specific
directions, and the adversary (the approximant) chooses f' after the x_i are fixed. I found no configuration in which a uniform upper
bound can be established; for every candidate examined, an engineering device either provably recovers the mate (Theorems 1-2) or
the failure of the devices I know is reduced to an explicit quantitative property ((PC), (CC)) whose failure is NOT shown to imply
non-recovery (other devices remain). Hence: no counterexample, and no claim of one.

## 5.2 Proposition (where any obstruction must live: the near-free part). PROVED modulo R1 (P1_referee, itself mod C Thm 6.2/Prop 6.5).
Let f'_n -> f be NA approximants that are C-tame (finitely many strict non-peaks and degenerate peaks in each block, (MS) at x'_n), and let
g be in Li_n C(f'_n). Then for every finite set J_0 of free coordinates of f (|z_j| < 1, j notin F):
  P_{J_0} g = lim_n P_{J_0} ( sum_m R_m*( omega'_{n,m} - d'_{n,m}(omega'_{n,m}) w'_{n,m} ) )  for suitable omega'_{n,m} in c_00(Q'_{n,m}),
i.e. the free-coordinate part of g must be carried by OFF-PEAK BLOCK coordinates of the approximants; base masses cannot carry it.
*Proof.* By R1, g = lim g'_n with g'_n in S(f'_n) = (l_1(supp a'_n) cap xhat'_n-perp) + span{R_m* (e_k - d'(e_k) w'_m) : k in Q'_{n,m}}. For j in J_0,
z'_n(j) -> z(j) with |z(j)| < 1, so |z'_n(j)| < 1 for n large, hence j notin supp a'_n (z' = sign a' on supp a'). Apply P_{J_0}. QED.
Reading. EXACT two-piece mates have their switching part on F cup K (v is supported there), so their J-part is carried by the fixed
certificate parts omega+-; Proposition 5.2 is no obstacle and indeed Theorem 1 recovers them. A mate whose switching component has a
nonzero J-part (approximate resonances with core errors on free coordinates; E's rigid design) can only be recovered by CONVERTED or
IMPLANTED off-peak block coordinates of the approximants: this is the rigorous reason why conversion capacity (part 4) is the
decisive quantity there, and why base engineering alone (masses, flips) cannot suffice for such mates.

## 5.3 The candidates, examined against the full list of approximant devices
 (a) Exact resonances, Delta d = 0 (P1's defect, A_referee 5.2, constant or non-constant splits, cross-block exact relations): RECOVERED
     (Thm 1, rigorous; multi-block under a rank condition).
 (b) Exact resonances, Delta d > 0: RECOVERED under two-sided mass tuning (Thm 2); otherwise under (BR) (a far-tail comparison).
 (c) Exact resonances, Delta d < 0, and the C_referee kink class with c' > 0: the convexity mechanism provably fails on one side (3.4); recovery
     reduces to pinning R*(w' - w) on near free coordinates at precision o(t) (Thm 3). A non-recovery proof would have to show that EVERY
     approximant violates (PC) AND that no other decomposition of f' + tau g' on the bad side avoids the mismatch; e.g. extra absorbing masses
     (3.6 Rem 1), implanted off-peak coordinates (A Lemma 8.2) whose R*-images cancel the J-part of the mismatch, or transfer peaks
     (C Thm 7.4) acting at second order. None of these is excluded. No proof of non-recovery is in sight; in the block-tame robust case (PC)
     holds up to a perturbation lemma (3.7(a), SKETCH).
 (d) Approximate resonances through one-sided block carriers (weak peaks, super-near-threshold non-peaks, perturbed cross-block duplicates):
     recovery needs J(rho) ~ 16 kappa/(1-rho^2) two-sided carriers with frozen errors O(scale) at adjacent scales below the destruction
     boundary (Thm 4). Far rigidity can limit conversions of the ORIGINAL carriers (4.5, consistent with Lemma B), but implanted /
     generic-coordinate carriers (4.6(ii)) are not excluded, and averaging over scales (Thm 4) needs only finitely many for each rho.
     Model N's excess is model-level (NUMERICAL), not a lower bound.
 (e) Second-order (rebalancing) defects ({Gamma_w > 1} with Gamma_2 <= 1): at f with infinitely many kinks these are exactly (c)/(b) (1.6, 3.9);
     at kink-free tame points they are empty (C Thm 8.4 + P1 3.8, PROVED mod unrefereed C).
Conclusion of item 3: no configuration was found in which engineering provably fails; consequently no lower bound dist((f, rho g), NA) > 0 is
claimed. Lindenstrauss property B for l_2^2 is not contradicted by anything established here.

## 5.4 Numerical sanity checks (scripts in ctx/r2/N2_work/)
 * thm1_check.py: finite model of P1's example (referee's model.py: diagonal U, 12 contacts, 10 free coordinates, 7 block coordinates,
   special vector u with u(zhat) = 0), two-piece mate g_{K1} (c = 0.15, random K1), engineered approximant exactly as in Theorem 1
   (window masses 4t|b_theta| on the first 5 contacts, theta = 1/2, one far contact flipped to z' = -1 with negative mass 2 T_0 rho |v_j|,
   tuning mass at a window contact fixed by bisection so that u(x') = 0, hence w'(k_0) = 0 and Delta d' = 0), target g' as in Step 4.
   Exact p* by SOCP (Clarabel). Result (rho = 0.9, 4 seeds, 42 values of t in +-[1e-4, 10]): max_t [p*(f' + t rho g') - s(t)] in
   [-8.4e-9, -1.1e-9] (i.e. rho g' in C(f') to solver accuracy), u(x') = 0 and w'(k_0) = 0 to 1e-15, g'(x') = 0 to 1e-17, ||g' - g||_1 ~ 2-3e-3.
   (In a finite model the far contacts are not small, so the tuning mass and ||f' - f|| are O(0.05-0.4): the check validates the algebra,
   the sign/no-flip structure and the exact tuning, not the asymptotics.) Variant with the last contact set to z' = 0 ("beyond N''"):
   same conclusion (max excess <= -4e-9).
 * lemma32_check.py: random 14-coordinate blocks with a strict non-peak k_0 (w = 0) and 4 flipped fine peaks (176 admissible cases):
   for s >= 0, (N(W) - 1)/tau^2 <= 0.012 (no first-order term, Lemma 1.3/3.2(a)); for s < 0, min (N(W) - 1)/(2M|s|) = 0.999998
   (Lemma 3.2(b) is sharp).

## 5.5 Assessment
 * The only rigorously known defect of intrinsic recovery (P1 Thm 2.4: exact resonance, Delta d = 0) is recovered along engineered
   NA sequences: PROVED (Thm 1). Exact resonances with Delta d > 0 are recovered under a mild tuning condition (Thm 2).
 * The two remaining mechanisms that might defeat engineering are: Delta d < 0 exact resonances (pinning on near free coordinates) and
   approximate resonances with core errors on free coordinates (conversion/implant capacity). Prop 5.2 shows rigorously that the
   second kind can only be recovered through off-peak block coordinates of the approximants; neither kind is shown to resist the full
   list of devices.
 * Leaning: positive (density), with the open core now located precisely: (PC) for Delta d < 0 in the generic (infinitely many
   non-peaks) case, and the supply of two-sided carriers with frozen error O(scale) near the destruction boundary for approximate
   resonances. Both are quantitative tail-independence statements at the scale of the perturbation, i.e. properties of T relative to f.
