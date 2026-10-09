# Z5 notes: case (O4) of Remark rem:openZ -- infinite base support F = supp a

Numbering and notation are those of paper/martin_density_note.tex. Part files: r5/Z5_part1.md ... Z5_part5.md (same content, with
more detail in places); scripts: r5/Z5_work/. Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 0. Summary

| # | Result | Scope | Status |
|---|---|---|---|
| T1 | Transfer peaks at arbitrary base vector a (step (iv) of Remark rem:Binf): every Gamma_w-certificate with bounded-ratio (e.g. finitely supported) base part is recovered along "truncated canonical" norm-attaining approximants | every admissible T | PROVED (S2) |
| T2 | Windowed averaging (Theorem thm:windowed) at arbitrary F, for finitely based certificates | every admissible T | PROVED (S2) |
| T3 | Uniform transfer expansion with cushion-proportional base parts (C-a') | every admissible T | PROVED (S3) |
| T4 | Clamped window certificate at arbitrary F | SLD | PROVED (S3) |
| T5 | Theorem B*-inf: window-pinned mates are recovered at every f (any F) | SLD | PROVED (S3) |
| T6 | Theorem B-inf: every f with (SR) (F arbitrary) is in Rec (Remark rem:Binf made rigorous) | SLD | PROVED (S3) |
| T7 | Sign-mixed room (Theorem thm:Bpm) at arbitrary F; cushion-room class (W^c) | SLD | PROVED (S3) |
| T8 | Engineered recovery (Theorem thm:engineered, Cor cor:D1) at arbitrary F for cushion-compatible data, and under cushion sparsity (CS) | every admissible T | PROVED (S4) |
| T9 | Pure base mates transfer exactly along every truncation of a | every admissible T | PROVED (S5) |
| T10 | Bounded free switching (Lemma lem:boundedfree) holds at arbitrary F, even when a is in Y (correction to the note and the R4 referee) | every admissible T | PROVED (S5) |
| T11 | Proxy budget: at scale t an infinite-F first row satisfies all budget inequalities of a finite-F first row with base support F cap [1,M(t)] and the far support as contacts of sign sgn a | every admissible T | PROVED (S5) |
| T12 | Theorem S-inf: finitely many bad carriers (contact-swallowed, or swallowed by the support), cushion-dominated on F, (W*), (H2), (H3-inf): f in Rec. Contains first rows with infinite F, a in Y, and signature sets inside the support | SLD | PROVED (S6) |
| T13 | Reduction "Lemma Z for finite F => Lemma Z for all F" is equivalent to a lower-semicontinuity statement (LSC-trunc) of the same difficulty as Lemma Z; it is NOT obtained by truncation: transplanted decompositions cost 2 alpha(M) at the truncation | SLD | PROVED (equivalence) / OPEN (LSC-trunc) (S5) |
| T14 | Limitation lemma: for a fast-swallowed carrier (signature inside the support, a/v_l -> 0) the base pins switching only with a scale-dependent constant D*(t)/t -> infinity (explicit exponents) | SLD | PROVED (S7) |
| T15 | Deep flips: exact two-piece data cannot reproduce support usage beyond the cushion; this is exactly where the window method fails for (O4) | SLD | PROVED (as a statement about the construction) (S7) |
| T16 | No admissible design can exclude support swallowing (F = N is allowed, and every signature vector is in l_1) | all designs | PROVED (S7) |
| -- | Remaining (O4) core: bad carriers (no room off F) whose signature sets meet F infinitely with inf |a_j|/v_l(j) = 0 ("fast support swallowing", support version of (O1)(i)); infinitely many bad carriers at infinite F (support versions of (O2)/(O3)); (LSC-trunc) in general | SLD | OPEN |

Leaning: positive (no counterexample mechanism; every recoverability theorem of Section 8 extends to infinite F, and the residual
obstruction is of the same "exactness vs scale" type as case (O1)(i)).

## 1. Setting; which results of the note hold at arbitrary F. PROVED.
T admissible, I finite, f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu) and F = supp a possibly infinite;
s_j := sgn a_j = z_j on F; alpha(M) := sum_{j in F, j > M}|a_j|; F_{<=M} := F cap [1,M]; f^+-_j as in Lemma lem:flip.
Checked line by line: the following hold verbatim at arbitrary F: Lemmas lem:twosided, lem:smallness (its proof only uses that A_n -> a
coordinatewise boundedly with limsup||A_n||_1 <= ||a||_1 forces ||A_n - a||_1 -> 0, true for every a in l_1), lem:budget, lem:suplevel,
lem:box, lem:pinning, lem:triangular, Proposition prop:pinned (for f with (SR): J_gamma excludes F), Lemmas lem:phicalc, lem:switchbudget,
lem:split, lem:peakshift, lem:flip (stated there for infinite F), lem:signmixed (the hypothesis "finite base support" is not used in the
proof; rooms are computed on S_l \ F), lem:modswallow(a), lem:badpeaks, lem:avgfunctionals, Theorem thm:transport (certificates with
||b/a||_inf < infinity), and the proof of Theorem thm:windowed up to its last sentence. NOT valid at infinite F: Lemma lem:finitebase,
hence Proposition prop:windowcert(b), Lemma lem:uniformtransfer (its (C-a)), Lemma lem:windowtwopiece(d), Lemma lem:onesidedtransfer
(its no-flip argument uses a_min = min_F|a_j| > 0), Theorem thm:onesided (Gram system on F), and the last sentence of thm:windowed
(which invokes thm:transfer, stated for a in c_00). Sections 2-4 below repair each of these.

Lemma 1.1 (cushion lemma; any f, g in C(f), t > 0, two-sided decomposition at scale t). For j in F,
  (s_j B_+(j))_- <= |a_j|/t + f^+_j,  (s_j B_-(j))_+ <= |a_j|/t + f^-_j,  (s_j Delta B(j))_- <= 2|a_j|/t + f^+_j + f^-_j,
and sum_{j in F}(f^+_j + f^-_j) <= t/(2q_0). PROVED: definition of f^+-_j and Lemma lem:flip.
So at scale t a support coordinate is a contact of sign s_j with an allowance |a_j|/t per side ("cushion"); far support coordinates
(|a_j| << t^2) are contacts, near ones are two-sided.

## 2. Transfer peaks at an arbitrary base vector (T1, T2). PROVED.

Truncated canonical approximants. For N with a 1_{[1,N]} != 0 put c^a_N := q*(a 1_{[1,N]}), a_N := a 1_{[1,N]}/c^a_N,
F_N := F_{<=N}, nu_N := ||U*a_N||, e_N := U*a_N/nu_N, z^N := z 1_{[1,N]}, xt_N := z^N + U e_N, x'_N := xt_N/p(xt_N),
f'_N := grad p(x'_N), c_N := q(x'_N).

Lemma 2.1. (a) f'_N in NA cap S_{p*} with forced data a_N, e_N, z^N, zhat'_N = xt_N. (b) a_N -> a in l_1, e_N -> e, f'_N -> f, and all
forced data of f'_N converge to those of f (Proposition prop:continuity); x'_N -> xi weak*, c_N -> q_0. (c) For B supported in F_N and t
with sgn(a_N(j) + tB_j) = sgn a_N(j) on F_N: q*(a_N + tB) = 1 + tB(xt_N) + nu_N Psi_N(tU*B/nu_N), Psi_N(h) := ||e_N + h|| - 1 - <e_N,h>
<= ||P_N^perp h||^2/(2(1 - ||h||)) for ||h|| <= 1/2 (P_N^perp: projection onto e_N^perp).
Proof. (a) a_N in c_00 with q*(a_N) = 1; z^N in c_00, |z^N| <= 1, z^N = z = sgn a = sgn a_N on F_N; Proposition prop:smooth(c) and
Proposition prop:forced at x'_N. (b) c^a_N -> q*(a) = 1; U* bounded; z^N -> z coordinatewise; Proposition prop:approximants
((ii) => (i), valid for every f) and Proposition prop:continuity. (c) No sign change on F_N gives ||a_N + tB||_1 = ||a_N||_1 + tB(z^N);
||U*a_N + tU*B|| = nu_N + t<U*B,e_N> + nu_N Psi_N(tU*B/nu_N); add, using ||a_N||_1 + nu_N = 1 and B(z^N) + <U*B, e_N> = B(xt_N).
The bound on Psi_N is Lemma lem:base. QED

Theorem 2.2 (T1). Let T be admissible, I finite, f in S_{p*} (F arbitrary), and g = b + sum_m R_m*(omega_m - d_m(omega_m) w_m) a balanced
finite certificate with b in l_1(F), b(xi) = 0, ||b/a||_inf := sup_{j in F}|b_j|/|a_j| < infinity, omega_m in c_00(Q_m), such that
g in C(f) and Gamma_w(g) = q_0 h(b) + sum_m sigma_m H_m(omega_m) <= 1. Then for every rho in (0,1) there are g'_N -> g with
rho g'_N in C(f'_N) for all large N. Hence (f, g) in cl NA((c_0,p), l_2^2).
Proof. We follow the proof of Theorem thm:transfer, whose only use of a in c_00 is that the canonical truncations keep the base vector a.
Steps 2 and 3 (transfer peaks at xi, built from the vector tau_{*,m} = (pi_m(xi)/q_0)a - pi_m and the density of the tails of (u_{k,m})_k)
do not involve the approximants; the block parts of Steps 1, 4, 5 and Step 6 use only Lemma lem:threshold at x'_N, Lemma lem:block, the
convergence of the forced data (Lemma 2.1(b)), Lemma lem:dualball and g in C(f). The changes:
Step 1 (base). Put kappa_N := (b 1_{[1,N]})(xt_N) and b'_N := b 1_{[1,N]} - kappa_N a_N. Since xt_N -> zhat weak* boundedly and z^N = z on
[1,N], kappa_N -> b(zhat) = 0, so b'_N -> b in l_1; supp b'_N is contained in F_N and b'_N(xt_N) = kappa_N - kappa_N a_N(xt_N) = 0
(a_N(xt_N) = 1). For N large, c^a_N <= 2 and |kappa_N| <= 1/4; then for |t| <= r_b := min(1, 1/(4||b/a||_inf)) and j in F_N,
|t b'_N(j)| <= |t||b_j| + |t kappa_N||a_N(j)| <= |a_j|/4 + |a_N(j)|/4 <= (3/4)|a_N(j)|, so no sign changes, and by Lemma 2.1(c)
q*(a_N + t b'_N) = 1 + nu_N Psi_N(tU*b'_N/nu_N) <= 1 + (t^2/2) h_N (1 + 2|t| ||U*b'_N||/nu_N), where h_N := ||P_N^perp U*b'_N||^2/nu_N =
||P_N^perp U*(b 1_{[1,N]})||^2/nu_N -> h(b) = H_b (P_N^perp -> P^perp in norm). Thus q*(a_N + t b'_N) <= 1 + (t^2/2)(H_b + o(1))(1 + O(t))
uniformly in large N, which is what Step 1 of the note provides.
Step 4. Replace beta_{m,N} by ((R_m* y_{m,N})(x'_N)/c_N) a_N and e_{m,N} := R_m* y_{m,N} - beta_{m,N}; then e_{m,N} -> e_{infty,m}
(R_m* y_{m,N} -> R_m* y_m in l_1, x'_N -> xi weak*, c_N -> q_0, a_N -> a). The bookkeeping identity (eq:bookkeeping) is an identity at x'_N.
Step 5. A(t) := a_N + t rho b'_N + sum_m eps_m R_m* y_{m,N} = (1+E) a_N + t rho b'_N + sum_m eps_m e_{m,N}, and
q*(A(t)) <= (1+E) q*(a_N + (t rho/(1+E)) b'_N) + rho^2 t^2 sum_m |tau_m| q*(e_{m,N}), which with Step 1 gives the base bound of the note
with a replaced by a_N. With g'_N := b'_N + sum_m R_m*(omega_m - d'_{m,N} w'_{m,N}) one has g'_N -> g and g'_N(x'_N) = 0 (b'_N(xt_N) = 0;
Lemma lem:algebra at x'_N, supp omega_m consisting of strict non-peaks of w'_{m,N} for N large). Step 6 uses only p*(f'_N - f) -> 0 and
p*(g'_N - g) -> 0. Hence rho g'_N in C(f'_N); (f'_N, rho g'_N) attains its norm and tends to (f, rho g). Let rho -> 1. QED

Corollary 2.3 (T2: windowed averaging at arbitrary F). Theorem thm:windowed holds for every f in S_{p*} when its certificates c_t have
base parts with ||b/a||_inf < infinity (e.g. finitely supported): its proof up to the last sentence does not use F (it uses (A) local
validity, (B) closeness to g in C(f), convexity of p* and of Gamma_w), and the averaged certificate c (base part with bounded ratio,
rho g_c in C(f), Gamma_w(rho c) <= 1) is recovered by Theorem 2.2. PROVED.

## 3. Theorem B-inf made rigorous; window-pinned mates and room conditions at arbitrary F (T3-T7). PROVED.
In this section T is the SLD operator, N >= 1, p = p_N, and f is arbitrary (F possibly infinite).
R_0^inf := {f : (SR) holds} (Definition def:R0 without "F finite"; J_gamma = {j notin F : |z_j| <= 1-gamma}).
Definition def:windowpinned is read verbatim for arbitrary F.

### 3.1 The clamped window certificate (T4).
Let eta <= eta_*, l_* a window index, t in W(l_*), t <= min(t_eta,1), (B_+-, Theta_+-) a two-sided decomposition of g in C(f) at scale t
satisfying
  (PIN_K)  sum_l |Delta theta_l| <= K t  (K >= 1),  hence ||Delta B||_1 <= K t  (||u_l||_1 <= q*(u_l) = 1).
(For f in R_0^inf this is Proposition prop:pinned(a) with K = K_1 Lambda_f(l_*); for window-pinned mates it is the hypothesis.)
Proposition prop:pinned (b),(c) then hold with this K (their proofs use only (a), Lemma lem:budget(b), Lemma lem:suplevel). Define
  b^cl(j) := sgn(B_+(j)) min(|B_+(j)|, 2|a_j|/t) (j in F), b^cl := 0 off F;  M_t := min{M : alpha(M) <= t^2},  F_t := F_{<=M_t},
  a_t := a 1_{F_t},  kappa_t := (b^cl 1_{F_t})(zhat)/a_t(zhat),  b_t := b^cl 1_{F_t} - kappa_t a_t,
  omega^c_m as in Definition def:windowcert,  c_t := (b_t, (omega^c_m)_m).
Proposition 3.1. Assume (PIN_K), Kt <= 1, t^2 <= 1/(2(1+||U||)), and put K_kappa := 1/(2q_0) + (1+||U||)(2K + 3/(2q_0) + 2). Then
(a) a_t(zhat) >= 1/2; c_t is a balanced finite certificate with finitely supported base part (supp b_t in F_t), b_t(xi) = 0, and
    supp omega^c_m in {k in Q_m : gap_m(k) >= t^2}, |omega^c_m(k)| <= 2gap_m(k)/t;
(b) |kappa_t| <= 2K_kappa t, and if 2K_kappa t^2 <= 1 then |b_t(j)| <= 3|a_j|/t for all j;
(c) ||B_+ - b_t||_1 <= (2K + 3/(2q_0) + 2 + 2K_kappa)t and ||g - g_{c_t}||_1 <= K'_2 K t;
(d) sqrt(Gamma_w(c_t)) <= sqrt(1 + eta_Gamma(eta)) + K'_4 K t,
with K'_2, K'_4 depending only on f, N and the design.
Proof. (a) |a_t(zhat) - 1| = |(a - a_t)(zhat)| <= ||zhat||_inf alpha(M_t) <= (1+||U||)t^2 <= 1/2 (a(zhat) = 1, ||zhat||_inf <= 1 + ||U||).
So b_t(zhat) = 0 and b_t(xi) = q_0 b_t(zhat) = 0. The statement on omega^c is Proposition prop:windowcert(a) (no use of F).
(b) (b^cl 1_{F_t})(zhat) = B_+(zhat) - (B_+ 1_{F^c})(zhat) - ((B_+ - b^cl)1_F)(zhat) - (b^cl 1_{F \ F_t})(zhat), with |B_+(zhat)| <= t/(2q_0)
(Lemma lem:budget(a)), ||B_+ 1_{F^c}||_1 <= Kt + t/q_0 (Proposition prop:pinned(b)), ||(B_+ - b^cl)1_F||_1 <= ||Delta B 1_F||_1 + t/(2q_0)
<= Kt + t/(2q_0) (Lemma lem:flip), ||b^cl 1_{F \ F_t}||_1 <= (2/t)alpha(M_t) <= 2t. Hence |kappa_t| <= 2K_kappa t, and
|b_t(j)| <= 2|a_j|/t + 2K_kappa t|a_j| <= 3|a_j|/t.
(c) B_+ - b_t = B_+ 1_{F^c} + (B_+ - b^cl)1_F + b^cl 1_{F \ F_t} + kappa_t a_t. The block part of g - g_{c_t} is bounded as in the proof of
Proposition prop:windowcert(c), which uses only Lemma lem:suplevel, Lemma lem:box, (P2) and Proposition prop:pinned(a),(c).
(d) As in Proposition prop:windowcert(d): sqrt(Gamma_w) is a seminorm on data, Gamma_w(B_+, Theta_+) <= 1 + eta_Gamma(eta), and the
remainder has q_0 h(x) <= ||U||^2||x||_1^2/nu, sigma_m H_m(X_m) <= (sum_k lambda_{k,m}|X_m(k)|)^2/C_m, both (const K t)^2 by (c). QED

### 3.2 Uniform transfer expansion with cushion-proportional base parts (T3; every admissible T).
Lemma 3.2. Let T be admissible, I finite, f arbitrary. For every eps_tr > 0 there are c_flat in (0,1/8] and t_1 > 0 such that for every
t in (0,t_1] and every balanced finite certificate c = (b, omega) at f with
  (C-a') supp b finite (or ||b/a||_inf < infinity), |b_j| <= 3|a_j|/t for all j, and Gamma_w(c) <= 2;
  (C-b)  supp omega_m in {k in Q_m: gap_m(k) >= t^2}, |omega_m(k)| <= 2gap_m(k)/t,
one has p*(f + r g_c) <= 1 + (r^2/2)(Gamma_w(c) + eps_tr) for |r| <= c_flat t.
Proof. As Lemma lem:uniformtransfer, with two changes. Base: supp b in F and |r b_j| <= 3c_flat|a_j| < |a_j| (c_flat < 1/3), so no
sign change on F; Exc(rb) = 0 (Lemma lem:bookkeeping(b)) and G_b(a + rb) = nu Psi(rU*b/nu); ||b||_1 <= 3/t gives
||rU*b||/nu <= 3c_flat||U||/nu <= 1/2 for c_flat <= nu/(6||U|| + 1), whence G_b <= (r^2/2) h(b)(1 + K'_A c_flat), K'_A := 6||U||/nu
(Lemma lem:base). Rebalancing error: |lambda|(|q*(A) - 1| + q*(A - a)) <= |lambda| 2 q*(rb) <= 6|I|K_3K_Y(1+||U||)c_flat r^2 instead of a
term of order |r|^3. Blocks, transfer data and all other estimates are unchanged. Choose eta_1 := min(1/4, eps_tr/(8|I|K_3)), then c_flat
so small that 2(K'_A + 2/C_min)c_flat + 6|I|K_3K_Y(1+||U||)c_flat + 8K_3K_y c_flat/C_min <= eps_tr/4 (with Gamma_w <= 2), then t_1 small
(the r^4 term and the conditions of Lemma lem:TV). QED

### 3.3 Theorems.
Theorem 3.3 (T5: B*-inf). If g in C(f) is window-pinned at f (F arbitrary), then (f,g) in cl NA((c_0,p_N), l_2^2).
Proof. Fix rho; choose eta_0, kappa_0, eps_tr := eta_0/2, eta as in the proof of Theorem thm:R0, and c_flat, t_1 by Lemma 3.2. With the
data (l_j, K_j) of window pinning and K := K_j + 6 <= 7K_j (fine carriers: <= 6t^2), for j large every dyadic scale t of W(l_j) satisfies
t <= min(t_eta, t_1, 1), Kt <= 1, t^2 <= 1/(2(1+||U||)), 2K_kappa t^2 <= 1, K'_4 K t <= kappa_0 (as K_j T_hi(l_j) -> 0). The clamped
certificate c_t (Proposition 3.1) has Gamma_w(c_t) <= (1+2kappa_0)^2 = 1 + eta_0/2 <= 2 and satisfies (C-a'), (C-b), so
p*(f + r g_{c_t}) <= 1 + (r^2/2)(1+eta_0) for |r| <= c_flat t (Lemma 3.2), and p*(g - g_{c_t}) <= 7(1+||U||)K'_2 K_j t. Corollary 2.3 applies
with (t^{(j)}, n_j, K_j) := (T_hi(l_j), n^w_{l_j}, 7(1+||U||)K'_2 K_j) (n^w_{l_j}/K_j -> infinity, K_j T_hi(l_j) -> 0). QED
Theorem 3.4 (T6: B-inf; Remark rem:Binf). R_0^inf is contained in Rec. Proof: Proposition prop:pinned(a) holds at arbitrary F; as in the
proof of thm:R0, K_1 Lambda_f(l)T_hi(l) -> 0 and n^w_l/Lambda_f(l) -> infinity, so every mate is window-pinned; Theorem 3.3. QED
Theorem 3.5 (T7a). Let R_0^{pm,inf} := {f : r_l := min_sigma sum_{s in S_l\F} v_l(s)(1 + sigma z_s) > 0 for all l in L_N, and (W^pm)}.
Then R_0^{pm,inf} is contained in Rec. Proof: Lemma lem:signmixed holds at arbitrary F; proof of thm:Bpm; Theorem 3.3. QED
Theorem 3.6 (T7b: cushion room). For M >= 0 let r_l^{[M]} := min_sigma sum_{s in S_l \ F_{<=M}} v_l(s)(1 + sigma z_s) (z = sgn a on F),
Lambda^c_f(l,M) := prod_{l''<=l, l'' in L_N}(1 + 3/r^{[M]}_{l''}), M(t) := min{M : alpha(M) <= t^2}, and
  (W^c)  liminf_l Lambda^c_f(l, M(T_lo(l)))/(l 2^{l^3} Lambda°(l)) = 0.
Every f with (W^c) is in Rec; (W^pm) implies (W^c) (r^{[M]}_l >= r_l).
Proof. For M >= M(t) let E^c_l := sum_{s in S_l \ F_{<=M}} phi_{z_s}(Delta B(s)). By Lemma lem:switchbudget, Lemma lem:phicalc(a) (on F,
|z_j| = 1 and phi_{s_j}(x) = 2(s_j x)_-) and Lemma 1.1, sum_l E^c_l <= t/q_0 + 2 sum_{j in F, j>M}(2|a_j|/t + f^+_j + f^-_j) <= (2/q_0 + 4)t.
By (P1), (eq:DeltaB) and Lemma lem:phicalc(c),(d), summing |Delta theta_l| v_l(s)(1 + z_s sgn Delta theta_l) <= phi_{z_s}(Delta B(s)) + 2|r_l(s)|
over s in S_l \ F_{<=M} gives r_l^{[M]}|Delta theta_l| <= E^c_l + 2 sum_{l'>l} pi_{l',l}|Delta theta_{l'}|; unrolling as in Lemma
lem:signmixed, sum_l|Delta theta_l| <= (2/q_0 + 26)Lambda^c_f(l_*, M)t for t in W(l_*). Since M(.) is nonincreasing, M := M(T_lo(l_*))
serves all scales of W(l_*). (W^c) and (P3) make every mate window-pinned; Theorem 3.3. QED
Remark 3.7. If S_l is (cofinitely) inside F, r_l^{[M]} = O(delta_l 2^{-M}) on the far part only, and M(T_lo(l)) is of the order of the
window length n^w_l when a decays geometrically; so (W^c) holds only for super-fast decay of a on swallowed signature sets. This is
the first appearance of the obstruction of Section 7.

## 4. Engineered recovery at arbitrary F (T8; every admissible T). PROVED.
Definition def:twopiece is read verbatim at arbitrary F (no condition on F; b^+- vanish off F cup K, z-signs on K, omega^+-_m in c_00(Q_m)).
Put b^theta := (b^+ + b^-)/2, v := b^+ - b^-.
Definition 4.1. Two-piece data are cushion-compatible if, for some C_R < infinity and all j in F,
  (R-inf)  |b^theta_j| <= C_R|a_j|,  (s_j b^+_j)_- <= C_R|a_j|,  (s_j b^-_j)_+ <= C_R|a_j|.
They satisfy cushion sparsity if, for beta in {|b^theta|, (s b^+)_-, (s b^-)_+},
  (CS-data)  m_beta(x) := sum{beta_j : j in F, |a_j| < x beta_j} = o(x) as x -> 0.
(R-inf) implies (CS-data) (the sets are empty for x < 1/C_R); finitely supported data are cushion-compatible; for F finite both are void.
Only the anti-sign directions matter: a support coordinate used by the + piece in the direction sgn a_j (or by the - piece in the
direction -sgn a_j) never flips.

Lemma 4.2 (flip cost). For b in l_1 and r > 0, sum_{j in F}(|a_j + r b_j| - |a_j| - s_j r b_j) = sum_{j in F} 2(r(s_j b_j)_- - |a_j|)_+
<= 2r sum{(s_j b_j)_- : |a_j| < r(s_j b_j)_-}; for r < 0 the same with (s_j b_j)_+ and |r|. PROVED (|x+y| - |x| - sgn(x)y = 2(-sgn(x)y - |x|)_+).

Theorem 4.3 (T8). Let I be finite, T admissible, f in S_{p*} with F arbitrary, g in C(f) carrying two-piece data satisfying (CS-data)
(in particular cushion-compatible data), rho in (0,1) with rho^2 kappa_w < 1, and assume I_- := {m : Delta d_m < 0} satisfies (SC). Then
there are norm-attaining f'_i -> f with FINITE base supports and g'_i in C(f'_i), g'_i -> rho g. In particular (f, rho g) in cl NA, and
(f,g) in cl NA if kappa_w <= 1. Corollaries: Corollary cor:D1 and Corollary cor:weightedengineered hold at arbitrary F for data with
(CS-data).

Proof. Modify Definition def:engineered: with window N_w, scale s_1, cut-off N'' > N_w, m_j := 4 rho s_1|b^theta_j| (j in K cap [1,N_w]),
  a'' := a 1_{[1,N_w]} + sum_{j in K cap [1,N_w]} m_j z_j e_j*,  a' := a''/q*(a''),  z' := z on [1,N''], 0 beyond,  xhat' := z' + U e',
  x' := xhat'/p(xhat'),  f' := grad p(x').
z' = sgn a' on supp a' = F_{<=N_w} cup {window contacts with b^theta_j != 0}, so f' is norm attaining with finite base support; support
coordinates in (N_w, N''] become contacts of f' with the signs s_j, those beyond N'' free coordinates. N_w is chosen AFTER s_1 with
  (N0) alpha(N_w) <= s_1^2,  rho sum_{j in F, j > N_w}(s_j v_j)_- <= delta s_1/32,  rho C s_1 <= 1/8 (C := C_R if (R-inf) is used),
then N'' > N_w with (eq:N1), (eq:N2) and rho V_{>N''} <= delta s_1/32, V_{>N''} := sum_{j > N''}|v_j|. (All possible since v in l_1.)
Lemma lem:approxfacts: q*(a'') <= q*(a 1_{[1,N_w]}) + (1+||U||)4 rho s_1||b^theta||_1 and q*(a 1_{[1,N_w]}) <= 1 + ||U||alpha(N_w), so
|a'_j| >= |a_j|/2 on F_{<=N_w} at late stages; (E1) becomes ||a'' - a||_1 <= 4rho s_1||b^theta||_1 + s_1^2, ||e' - e|| <= K_e s_1 with
K_e := 2||U||(4rho||b^theta||_1 + 1)/nu; (E2) is unchanged (xhat' - zhat = -z 1_{(N'',infinity)} + U(e' - e)); (E3)-(E5), Lemmas
lem:F1, lem:anchor, lem:scrambling follow as in the note. In Step 0, condition (T_1) "rho T_0(||b^+||_inf + ||b^-||_inf) <= a_min/8" is
replaced by rho T_0 C <= 1/8 (under (R-inf)), resp. by "2rho|tau| m(4rho|tau|) <= delta tau^2/16 for |tau| <= T_0" (under (CS-data),
m := sum of the three m_beta). Steps 1, 2, 4, 6 are verbatim (beta^theta := b^theta 1_{[1,N_w]}, beta^+- := b^+- 1_{[1,N_w]} +-
(1/2)v 1_{(N_w,infinity)}; g'' - g = -b^theta 1_{(N_w,infinity)} + (block terms) -> 0).
Step 3 (base). Claim: Exc'(tau B^diamond) <= (1/2)rho|tau|V_{>N''} + rho|tau| sum_{j in F, j>N_w}(s_j v_j)_- + Fl, with Fl <= 2rho|tau|
m(4rho|tau|) (Fl = 0 under (R-inf) with rho T_0 C <= 1/8), and Exc'(tau B^theta) <= Fl. On supp a', a'_j + tau B^diamond_j =
(1 - tau rho c)a'_j + tau rho beta^diamond_j with |tau rho c| <= 1/2. (i) j in F_{<=N_w}: s_j(1 - tau rho c)a'_j >= |a_j|/4; the
anti-sign part of tau rho beta^diamond_j is at most |tau| rho beta_j (beta = |b^theta|, (s b^+)_- or (s b^-)_+ for diamond = theta, +, -,
using sgn tau = diamond for diamond = +-), so a flip needs |a_j| < 4 rho|tau| beta_j and costs <= 2|tau|rho beta_j (Lemma 4.2); under
(R-inf) and rho T_0 C <= 1/8 there is no flip. (ii) window contacts and K: verbatim (side conditions on K). (iii) j in F cap (N_w, N'']:
z'_j = s_j, a'_j = 0, beta^theta_j = 0, beta^+-_j = +-(1/2)v_j, and the summand 2(s_j tau rho beta^diamond_j)_- equals |tau|rho(s_j v_j)_-
for diamond = sgn tau. (iv) j > N'': summand <= (1/2)rho|tau||v_j|. (v) off F cup K: b^+-, v vanish. QED claim.
Step 5. The first-order base costs plus the anchor remainder are <= |tau|delta s_1/64 + |tau|delta s_1/32 + |tau|delta s_1/64 =
|tau|delta s_1/16 <= delta tau^2/16 for |tau| > s_1 (absent for theta), as in the note; the flip cost Fl <= delta tau^2/16 adds delta/8 (in
units of tau^2/2) to the bound rho^2 kappa_w + 5delta/8 = 1 - 2delta + 5delta/8 of the note, leaving 1 - 2delta + 3delta/4 <= 1 - delta
(the constants K_sharp, eta_1 are fixed after the uniform bound Fl <= tau^2). Hence p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta) for
|tau| <= T_0; Lemma lem:assembly concludes. QED

## 5. Truncations, what transfers, and the reduction question (T9-T11, T13).

### 5.1 Truncated first rows. PROVED.
For M with F_{<=M} nonempty let a^M := a 1_{[1,M]}/q*(a 1_{[1,M]}) and let z^M be ANY vector with |z^M| <= 1 and z^M = z on [1,M]
(arbitrary beyond M). (a^M, z^M) is admissible forced data (Remark rem:lemmaZ(c)); the first row f^M has finite base support F_{<=M}, and
f^M -> f as M -> infinity whatever the far values (a^M -> a in l_1, z^M -> z coordinatewise). Contact truncation: z^M := z (far support
becomes contacts of sign s_j). Norm-attaining truncations: z^M := z 1_{[1,M']} with M' >= M.

### 5.2 Pure base mates transfer exactly (T9). PROVED.
C_q(a) := {b : q*(a + tb) <= s(t) for all t} is contained in C(f) (Lemma lem:dualball: p*(f + tb) <= max(q*(a+tb), ||w||)).
Lemma 5.1. (a) b in C_q(a) implies supp b in F and b(zhat) = 0. (b) For b in C_q(a) and rho in (0,1) put b^M := b 1_{[1,M]} - kappa_M a^M,
kappa_M := (b 1_{[1,M]})(zhat^M), zhat^M := z^M + U(U*a^M/||U*a^M||). Then b^M -> b in l_1 and rho b^M in C_q(a^M) (hence in C(f^M)) for
all large M, for every choice of the far values of z^M.
Proof. (a) In (eq:baseidentity) all terms after t b(zhat) are >= 0, and q*(a+tb) - 1 <= t^2/2: dividing by t -> 0+- gives b(zhat) = 0, and
then |t|(|b_j| - z_j sgn(t) b_j) <= t^2/2 for j notin F and both signs of t forces b_j = 0.
(b) kappa_M -> b(zhat) = 0 (z^M = z on [1,M], U*a^M/||U*a^M|| -> e), so b^M -> b; b^M(zhat^M) = 0 and supp b^M in F_{<=M}. Large t: by
Lemma lem:slack(a), q*(a^M + t rho b^M) <= s(rho t) + q*(a^M - a) + rho|t|q*(b^M - b) <= s(t) for |t| >= T_0 and M >= M_0(T_0). Small t: with
c_M := q*(a 1_{[1,M]}) -> 1 and lambda_M(t) := (1 - t rho kappa_M)/c_M, the base identity at a^M gives q*(a^M + t rho b^M) = 1 + Fl^M(t) +
nu_M Psi_M(t rho U*b^M/nu_M), Fl^M(t) = sum_{j in F_{<=M}} 2(-s_j t rho b_j - lambda_M(t)|a_j|)_+. For |t| <= T_0 and M large, lambda_M >= rho,
so Fl^M(t) <= rho Fl_b(t) <= rho(s(t) - 1 - nu Psi(tU*b/nu)). With Lemma lem:base (a) and (b) and h_M := ||P_M^perp U*(b 1_{[1,M]})||^2/nu_M
-> h(b): q*(a^M + t rho b^M) - s(t) <= -(1-rho)(s(t)-1) + (t^2 rho/2)(rho|h_M - h(b)| + C_0|t|) <= -(t^2/2)[(1-rho)(1 - t^2/4) -
rho^2|h_M - h(b)| - rho C_0|t|] <= 0 for |t| <= T_0 small and M large. QED
(Numerical check: Z5_work/check_base_truncation.py, 60-dimensional model with flips at all scales: max_t (q* - 1)/(s(t) - 1) is 0.9999 at f
and 0.40 ... 0.96 at the truncations, rho = 0.9, 0.99.)
Also transferring along every truncation: finite certificates (Theorem thm:transport, any sequence f_n -> f, base parts with ||b/a||_inf <
infinity), Gamma_w-certificates with bounded-ratio base parts (Theorem 2.2), and mates with (CS) two-piece data (Theorem 4.3, along
engineered truncations).

### 5.3 Bounded free switching at arbitrary F (T10; correction). PROVED.
The note (Lemma lem:boundedfree) and the Round-4 referee state that F finite is essential "because Y may contain a when a is not in c_00".
This restriction is unnecessary.
Lemma 5.2. Let f be arbitrary, eta <= eta_* with eta_Gamma(eta) <= 1, 0 < t <= min(t_eta,1), (B_+-, Theta_+-) a two-sided decomposition of
g in C(f) at scale t. For every finite set U of pairs (k,m) there is C_U, depending only on f and U, with
  max_{(k,m) in U}|Delta theta_{k,m}| <= C_U(1 + ||sum_{(k,m) notin U} Delta theta_{k,m} u_{k,m}||_1).
Proof. Phi(c) := (P^perp U* sum_U c u, (sum_U c u)(zhat)) is injective on R^U: Phi(c) = 0 gives U*(sum_U c u) = mu e, hence
sum_U c u = (mu/nu)a (U* injective), hence 0 = (sum_U c u)(zhat) = mu/nu (a(zhat) = 1), so sum_U c u = 0 and c = 0 (T injective). Thus
||c||_inf <= C_U||Phi(c)||. For c = Delta theta|_U: sum_U Delta theta u = -Delta B - R, R := sum_{notin U}Delta theta u (eq:DeltaB);
||P^perp U*Delta B|| <= 2(2nu/q_0)^{1/2} (Lemma lem:budget(d)), |Delta B(zhat)| <= t/q_0 (Lemma lem:budget(a)), ||P^perp U*R|| <=
||U||||R||_1, |R(zhat)| <= (1+||U||)||R||_1. QED
So a in Y (possible for the SLD operator: a = u_l) is harmless for bounded switching: the a-direction is pinned at first order.
(Numerical check: Z5_work/check_boundedfree.py: with a = u_1 the Hilbert-only map has rank k-1, the map Phi has rank k.)
Lemma lem:rigidity(a) (uniqueness of data with base parts in F cup K) does fail at infinite F: block combinations supported in F exist
(e.g. u_l when supp u_l is contained in F). This, not "a in Y", is the new freedom at infinite F (Section 7).

### 5.4 Proxy budget (T11). PROVED.
Lemma 5.3. Let f be arbitrary, g in C(f), t > 0, (B_+-, Theta_+-) at scale t, and M with alpha(M) <= t^2. With Fbar := F_{<=M},
Kbar := K cup (F cap (M,infinity)) and zbar := z (= s on F):
  sum_{j notin Fbar} phi_{zbar_j}(B_+(j)) <= t/q_0 + 2t,  sum_{j notin Fbar} phi_{-zbar_j}(B_-(j)) <= t/q_0 + 2t,
  sum_{j notin Fbar} phi_{zbar_j}(Delta B(j)) <= 2t/q_0 + 4t,
and Lemma lem:flip holds on the finite set Fbar. Proof: Lemma lem:switchbudget off F; on F cap (M,infinity), phi_{s_j}(x) = 2(s_j x)_-
and Lemma 1.1 with sum_{j>M}|a_j|/t <= t; the Delta B bound by Lemma lem:phicalc(b). QED
Thus on each window an infinite-F first row obeys all budget inequalities of the finite-F "proxy" (Fbar, Kbar, zbar), with Fbar growing
as the window moves down (M(T_lo(l)) -> infinity). Parts 3, 4, 6 of these notes are the proxy argument made rigorous; finite-dimensional
facts about F (Lemma lem:finitebase, a_min) are replaced by clamps, common shifts and ratio bounds.

### 5.5 The reduction question (T13).
Proposition 5.4. For the SLD operator and N, the following are equivalent:
(i) NA((c_0,p_N), l_2^2) is dense;
(ii) Lemma Z holds at every f with finite base support, and (LSC-trunc) holds: for every f, g in C(f), rho < 1 and eps > 0 there is f' with
finite base support, p*(f' - f) < eps and dist(rho g, C(f')) < eps.
Proof. (i) => (ii): Theorem thm:reductionZ gives Lemma Z everywhere, and Lemma lem:pair gives norm-attaining (hence finite-support)
approximants with rho g in Li C(f_n). (ii) => (i): given (f, g, rho, eps), (LSC-trunc) gives f' (finite F) and g' in C(f') with
p*(g' - rho g) < eps; Lemma Z at f' for (g', rho', eps) gives f'' in R_0 and g'' in C(f'') with p*(f'' - f') < eps, p*(g'' - rho'g') < eps;
then p*(f'' - f) < 2eps and p*(g'' - rho'rho g) <= p*(g'' - rho'g') + rho' p*(g' - rho g) < 2eps. As rho rho' ranges over (0,1), Lemma Z
holds at f; hence everywhere, and Theorem thm:reductionZ gives (i). PROVED.
Status of (LSC-trunc). PROVED for the mates listed in 5.2 (pure base mates; cl Cert(f); bounded-ratio Gamma_w-certificates; mates that are
limits of mates with (CS) two-piece data and Delta d >= 0 or (SC)), and for every mate at f in R_0^inf, R_0^{pm,inf}, (W^c), R_S^inf, and
every window-pinned mate (all these are in cl NA with finite-support norm-attaining approximants). OPEN in general, and NOT a consequence of
truncation: if a decomposition of f + tg is transplanted to the contact truncation f^M, the far support coordinates lose exactly their
cushions, and the extra base excess is sum_{j in F, j>M} 2 min(|a_j|, t(-s_j B_+(j))_+) <= 2 alpha(M) (PROVED by the flip identity: on F,
|a_j + x| - |a_j| - s_j x = 2(-s_j x - |a_j|)_+, at a contact |x| - s_j x = 2(-s_j x)_+, and the difference is <= 2 min(|a_j|, (-s_j x)_+)).
This is <= eps t^2 only for t >= (2 alpha(M)/eps)^{1/2}; at smaller scales the mates of f may use far cushions against the free direction on
BOTH sides (Lemma 1.1 allows it), which no contact sign can reproduce. So (LSC-trunc) is a lower-semicontinuity statement of the same
type as case (O2) (two-sided far resources made one-sided), and as hard as Lemma Z itself in general. HEURISTIC (not used): a reduction
must engineer the approximant per mate (far contact signs matching the mate's far switching, Theorem 4.3), i.e. it needs fixed data at f.

## 6. Theorem S-inf: finitely many swallowed carriers, including signature sets inside the support (T12). PROVED.
SLD operator, N, p = p_N, f arbitrary. r_l := min_sigma sum_{s in S_l \ F} v_l(s)(1 + sigma z_s) (room off the support); B := {l in L_N :
r_l = 0}; for l in B, z == epsilon_l on S_l \ F (epsilon_l := +1 if S_l \ F is empty); B_K := {l in B : S_l \ F infinite}
(contact-swallowed), B_F := B \ B_K (swallowed by the support: S_l \ F finite). tau_l := -epsilon_l Delta theta_l and q_l as in the note.
For good l: S*_l := S_l \ (F cup U_{l' in B, l' > l} supp y_{l'}), r*_l := min_sigma sum_{S*_l} v_l(s)(1 + sigma z_s),
Lambda*_f(l) := prod_{l'' <= l, l'' in L_N \ B}(1 + 3/r*_{l''}).
 (W*) r*_l > 0 for good l and liminf_l Lambda*_f(l)/(l 2^{l^3}Lambda°(l)) = 0;   (H2) as in the note;
 (H3-inf) no l in B_K sits at a degenerate peak with sgn w(k(l)) = epsilon_l, no l in B_F sits at a degenerate peak;
 (B_fin) B finite;   (H4-inf) c_B := max_{l in B} sup_{j in F}|u_l(j)|/|a_j| < infinity (bad carriers cushion-dominated on F).
R_S^inf := {f : (W*), (H2), (H3-inf), (B_fin), (H4-inf)}. For F finite this is the (B_fin) part of R_S.

Theorem 6.1. R_S^inf is contained in Rec.
Example 6.2. a := u_{l_0} (q*(u_{l_0}) = 1, F = supp y_{l_0} cup S_{l_0} infinite, a in Y), z := sgn a on F, z := 0 off F (admissible data,
Remark rem:lemmaZ(c)). Then B = B_F = {l_0} (if l_0 in L_N), c_B = 1, every other S_l has full room off F up to the finite set
S_l cap supp y_{l_0}, and (W*) holds as for R_0. So f in Rec whenever (H2), (H3-inf) hold. This f is in none of R_0^inf, R_0^{pm,inf},
(W^c): it is an "infinite F without room" first row.

Proof of Theorem 6.1. Fix g, rho, and eta_0, kappa_0, eps_tr, eta as in the proof of Theorem thm:S. Let l_* >= l_f := max(max B, max_m l°_m)
(l°_m from (H2)), t in W(l_*), t <= min(t_eta,1), (B_+-, Theta_+-) at scale t, K* := (1/q_0 + 22)Lambda*_f(l_*).
Step 1. Lemma lem:modswallow(a) holds verbatim (its good inequalities use S*_l, disjoint from F; bad carriers never appear on the right
sides, so B_F needs no inequality): sum_{l notin B}|Delta theta_l| <= K* t, sum_{l > l_*}|Delta theta_l| <= 6t^2. Lemma lem:badpeaks holds verbatim.
Step 2 (exact switching). T_0 := U_{l in B} supp y_l cup U_{l in B_F}(S_l \ F) (finite); L_j(tau) := sum_{l in B} epsilon_l tau_l u_l(j);
c(tau) := sum_{j notin F} phi_{z_j}(L_j(tau)). Off F cup T_0 only signatures of l in B_K can be nonzero, with z_j = epsilon_l there, so
c(tau) = sum_{l in B_K} 2(tau_l)_- m_l + sum_{j in T_0 \ F} phi_{z_j}(L_j(tau)), m_l := ||v_l 1_{S_l \ (F cup T_0)}||_1 > 0. Z_f := {tau : tau_l >= 0
(l in B_K); z_j L_j(tau) >= 0 (j in T_0 cap K); L_j(tau) = 0 (j in T_0 \ (F cup K)); tau_l = 0 (l in B_pk); sum_{m(l)=m} q_l tau_l = 0 (m in I)}
(no sign condition for l in B_F). As in Lemma lem:exactswitch (B_fin case): c(tau) <= t/q_0 + 2K* t (Delta B 1_{F^c} = L(tau)1_{F^c} + e_0,
||e_0||_1 <= K* t), the bad peaks are controlled by Lemma lem:badpeaks(c) and (H3-inf), the d-sums by lem:badpeaks(b), and Hoffman's bound
gives tau' in Z_f with sum_l|tau_l - tau'_l| <= C_f K* t, V' := sum_B epsilon_l tau'_l u_l 1_{F^c} z-signed in K, ||Delta B 1_{F^c} - V'||_1 <= C_f K* t.
Step 3 (window two-piece data). X := sum_B epsilon_l tau'_l u_l; chi, e_+- from Lemma lem:split for e := Delta B 1_{F^c} - V'.
(3a) sum_B|tau'_l| <= 6 sum_l lambda_l/t + C_f K* t <= 3/t (C_f K* t^2 <= 1), so |X_j| <= C_X|a_j|/t on F, C_X := 3c_B (H4-inf).
A_j := C_A|a_j|/t, C_A := max(2, C_X).
(3b) Common shift (Lemma 7.4 below): for j in F, x_j := s_j B_+(j), y_j := s_j(B_+(j) - X_j), x_j - y_j = s_j X_j >= -2A_j; choose
sigma_j in [y_j - A_j, x_j + A_j] closest to 0; |sigma_j| <= (-x_j - A_j)_+ + (y_j - A_j)_+ <= f^+_j + f^-_j + |(Delta B - X)_j|, so
||sigma||_1 <= t/(2q_0) + (C_f + 1)K* t. b^+_1 := sum_{j in F}(B_+(j) - sigma_j s_j)e_j* satisfies -A_j <= s_j b^+_1(j) <= A_j + s_j X_j and
s_j(b^+_1 - X)(j) <= A_j on F; hence |b^+_1(j)| <= (C_A + C_X)|a_j|/t.
(3c) M_t := min{M : alpha(M) <= t^2}, F_t := F_{<=M_t}, a_t := a 1_{F_t}; b^+_2 := b^+_1 1_{F_t} (omitted mass <= (C_A + C_X)t);
kappa := (b^+_2 + chi V')(zhat)/a_t(zhat) (|kappa| <= K_kappa t, K_kappa = O(K*), using (b^+_2 + chi V')(zhat) = B_+(zhat) - e_+(zhat) -
(sigma s)(zhat) - (b^+_1 1_{F \ F_t})(zhat)); b^+ := b^+_2 + chi V' - kappa a_t, b^- := b^+ - X; omega^+-, g_t as in Lemma lem:windowtwopiece.
(3d) (i) (b^+, omega^+) side-+ and (b^-, omega^-) side-- admissible (off F: chi V' and -(1-chi)V'), both represent g_t, d-neutral
(tau'_l = 0 at bad peaks, sum q_l tau'_l = 0), b^+-(xi) = 0. (ii) For K_kappa t^2 <= 1 and j in F: (s_j b^+_j)_- <= (C_A + 1)|a_j|/t,
(s_j b^-_j)_+ <= (C_A + 1)|a_j|/t, |b^+-_j| <= (C_A + 2C_X + 1)|a_j|/t (on F \ F_t: b^+ = 0, b^- = -X); ||b^+-||_1 <= C_b/t. (iii) B_+ - b^+ =
e_+ + (sigma s)1_F + b^+_1 1_{F\F_t} + kappa a_t and B_- - b^- = (B_+ - b^+) - (Delta B - X) are O(K* t) in l_1; the block parts are compared as in
Lemma lem:windowtwopiece (b),(c); so ||g - g_t||_1 <= K*_2 t and Gamma_w(b^+-, omega^+-) <= (sqrt(1+eta_Gamma(eta)) + K*_4 t)^2, with K*_2, K*_4
= (constant) x Lambda*_f(l_*); the block parts satisfy (d) of Lemma lem:windowtwopiece (gamma_B > 0 by (B_fin)).
Step 4 (one-sided transfer expansion at arbitrary F). Lemma lem:onesidedtransfer holds with "t||b||_1 <= A_0" supplemented by the one-sided
cushion bound (s_j b_j)_- <= C_+|a_j|/t on F for side + ((s_j b_j)_+ <= C_+|a_j|/t for side -) and c_flat <= 1/(2C_+): for 0 < r <= c_flat t
no coordinate flips on F (r(s_j b_j)_- <= |a_j|/2; the free direction never flips), off F the side conditions give zero cost, so
G_b(a + rb) = nu Psi(rU*b/nu), and the rest of that proof (which uses ||rU*b||/nu <= c_flat||U||A_0/nu and q*(rb) <= (1+||U||)c_flat A_0) is
unchanged. Apply it with C_+ := C_A + 1, A_0 := C_b.
Step 5. As in the proof of Theorem thm:S: windows l_j from (W*), windowed averaging (Lemma lem:avgfunctionals) gives rho gbar_j in C(f), rho gbar_j
-> rho g; the averaged data are d-neutral two-piece data with kappa_w(rho Dbar_j) <= 1, cushion-compatible with C_R := (C_A + 2C_X + 1)/T_lo(l_j)
(the bounds (ii) are preserved by averaging: x -> x_-, x -> x_+ are convex); Theorem 4.3 (d-neutral, I_- empty) gives (f, rho gbar_j) in cl NA. QED
Remark 6.3. (a) (H4-inf) is used only in (3a): the exact switching X must be compatible with the cushions (the common shift needs
(s_j X_j)_- <= 2A_j). (b) The (B_res) case with infinitely many bad carriers extends likewise if B_F is empty, (H1) holds, all bad carriers are
resonant and d-neutral, and c_B := sup_{l in B}sup_{j in F}|u_l(j)|/|a_j| < infinity (uniform): PROVED by the same argument with Step 2 of
the note's (B_res) case (tau'_l := (tau_l)_+) and sum_B|tau'_l| <= 2/t.

## 7. The obstruction for infinite F without room (T14-T16).
SLD operator; v_l := delta_l h_l/n_l; for a carrier l with S_l cap F infinite, the ratio profile varrho_l(j) := |a_j|/v_l(j) (j in S_l cap F).
l is support-swallowed if S_l \ F is finite; cushion-dominated if inf_{S_l cap F} varrho_l > 0; fast-swallowed if varrho_l -> 0 on S_l cap F.

### 7.1 What the base can pin (T14). PROVED (exact arithmetic of the constraint system).
For a support-swallowed l the only base information on Delta theta_l available to pinning arguments (Lemmas lem:switchbudget, lem:flip,
1.1) is, for j in S := S_l cap F (with -Delta B(j) = Delta theta_l v_l(j) + r_l(j)),
  (s_j Delta B(j))_- <= 2|a_j|/t + f^+_j + f^-_j,   sum_j(f^+_j + f^-_j) <= t/(2q_0).     (7.1)
Lemma 7.1. Let r_l = 0 (no finer carriers) and s_j == epsilon on S (monochromatic). Then s_j Delta B(j) = -epsilon Delta theta_l v_l(j); the
direction epsilon Delta theta_l > 0 (switching amplitude tau_l < 0) is constrained, the other is free, and (7.1) is solvable with
Delta theta_l = epsilon D (D >= 0) iff Phi_l(D,t) := sum_{j in S}(D v_l(j) - 2|a_j|/t)_+ <= t/(2q_0) (minimal f^+_j + f^-_j :=
(D v_l(j) - 2|a_j|/t)_+). For sign-mixed s on S both directions are constrained, each by its sign class. Put D*_l(t) := sup{D : Phi_l(D,t)
<= t/(2q_0)}.
(a) Cushion-dominated (varrho_l >= c > 0): Phi_l(D,t) = 0 for D <= 2c/t, so D*_l(t) >= 2c/t, beyond the box bound 6 lambda_l/t when
c >= 3 lambda_l: the support absorbs the whole switching range; no pinning (and none is needed: Theorem 6.1 keeps it as exact data).
(b) Fast-swallowed with v_l(j) = c_0 2^{-j}, |a_j| = 2^{-(1+beta)j} on S (beta > 0): D*_l(t) is of order t^{(beta-1)/(beta+1)}, hence
D*_l(t)/t ~ t^{-2/(beta+1)} -> infinity.
Proof of (b): the summand is positive iff j > J := beta^{-1} log_2(2/(D c_0 t)), and the sum is comparable to D 2^{-J} = D(D c_0 t/2)^{1/beta};
setting it equal to t/(2q_0) gives D^{(1+beta)/beta} ~ t^{1 - 1/beta}. QED (Numerical check: Z5_work/check_Dstar.py, fitted exponents
-0.333, -0.001, 0.335, 0.500 for beta = 0.5, 1, 2, 3; predicted -1/3, 0, 1/3, 1/2.)
Consequence. Pinning through support coordinates is available only with a scale-dependent constant K_l(t) = D*_l(t)/t -> infinity, and
windowed averaging (Theorem thm:windowed) needs K << n^w on windows whose bottom scale T_lo(l) is super-exponentially small; so the room
method cannot treat fast-swallowed carriers (this is also why (W^c) of Theorem 3.6 is restrictive).

### 7.2 Bounded switching and cushion sparsity. PROVED.
If all carriers outside a finite set U are pinned on a window, the switching through U is bounded (Lemma 5.2), at every F. Fixed data
carrying bounded switching D through a support-swallowed l have anti-sign parts beta_j = D v_l(j) on S, and by Lemma 4.2 their flip cost at
scale r is <= 2|r| D m_l(|r| D), m_l(x) := sum{v_l(j) : j in S, varrho_l(j) < x}. Hence such FIXED data satisfy (CS-data) (flip cost
o(r^2), Theorem 4.3 applies to them) iff m_l(x) = o(x); with v_l(j) ~ 2^{-j}: varrho_l(j) = 1/j gives m_l(x) ~ 2^{-1/x} (CS holds);
|a_j| = 2^{-2j} gives m_l(x) ~ x (borderline: flip cost of exact order r^2); |a_j| = 2^{-3j} gives m_l(x) ~ x^{1/2} ((CS) fails).
Producing (CS)-type fixed data from window decompositions at f would require an exactification tolerating sparse cushion violations
(Lemma 7.4 handles only exact cushion bounds); this is NOT done here (OPEN), so (CS) enters only through Theorem 4.3.

### 7.3 Deep flips: where the window method fails (T15). PROVED (as a statement about the construction).
Lemma 7.4 (common shift). For reals x, y and A >= 0 there is sigma with x - sigma >= -A and y - sigma <= A iff x - y >= -2A; then one may take
|sigma| <= (y - A)_+ + (-x - A)_+. (The admissible sigma form the interval [y - A, x + A].)
Exact two-piece data must satisfy b^+ - b^- = X, a finite block combination, and to be used at scale t they need, at every support
coordinate, one-sided cushion bounds (s_j b^+_j)_- <= A_j, (s_j b^-_j)_+ <= A_j with A_j = O(|a_j|/t) (or (CS)-sparse violations: Lemma 4.2;
a violation of l_1-mass mu at coordinates with |a_j| << t mu costs about 2 r mu at all scales r in (|a_j|/mu, t), which is not O(r^2)).
By Lemma 7.4, common shifts (which keep b^+ - b^- = X) achieve this iff (s_j X_j)_- <= 2A_j for all j in F. This holds when the bad switching
X is cushion-dominated (Theorem 6.1). It FAILS when X contains switching through a fast-swallowed carrier: at far coordinates of S_l cap F,
|a_j| << t v_l(j) |tau_l|. For the true decomposition (7.1) shows that such a usage forces f^+_j + f^-_j >> |a_j|/t: the decomposition at
scale t pays flips there ("deep flips"). Fixed data reproducing deep flips pay them at a first-order rate at smaller scales; so the mate must
switch differently at different scales. This is exactly the "exactness vs scale" mechanism of case (O1)(i), with the near-contacts
(|z_j| -> 1 off F) replaced by small support coordinates (|a_j| -> 0) and the room 1 - |z_j| replaced by the allowance 2|a_j|/t.

### 7.4 No design removes support swallowing (T16). PROVED.
For every admissible T built with private signatures v_l in l_1 (SLD or any variant): F = supp a is arbitrary (F = N is allowed), and for
every family (v_l) of vectors in l_1 there is a in S_{q*} with |a_j|/|v_l(j)| -> 0 along the support of every v_l (take |a_j| <=
2^{-j} min_{l <= j}|v_l(j)| wherever v_l(j) != 0, normalized). Sign-mixed signatures pin from both sides, but each sign class obeys Lemma 7.1(b).
Hence designs cannot exclude fast support swallowing; compare Remark rem:nodesign.

### 7.5 Precise statement of what remains of (O4).
Let f have infinite F. Then f in Rec (Theorem 3.5 if B is empty, Theorem 6.1 or Remark 6.3(b) otherwise) unless one of the following
holds; the list is the complement of the hypotheses of these theorems (PROVED: a case check), and every window-pinned mate is
recovered in any case (Theorem 3.3):
 (a) the room off the support decays too fast: (W^pm) fails (B empty) or (W*) fails (B nonempty): the support-free part of case (O1)(i);
 (b) some bad carrier l (r_l = 0: S_l \ F inside contacts of one sign, or finite with no room) is NOT cushion-dominated, i.e.
     S_l cap F is infinite and inf_{j in S_l cap F}|a_j|/v_l(j) = 0 ("fast support swallowing"); by Lemma 7.1(b) and 7.3 this is case
     (O1)(i) with the near-contacts replaced by small support coordinates and the room 1 - |z_j| replaced by the allowance 2|a_j|/t;
 (c) infinitely many bad carriers, not all contact-swallowed resonant d-neutral and uniformly cushion-dominated (Remark 6.3(b)):
     the support/contact versions of (O2)/(O3) (e.g. F = N with a > 0 swallows every signature set monochromatically);
 (d) (H2) or (H3-inf) fails: case (O1)(ii).
(A cushion-dominated support-swallowed carrier is harmless: Theorem 6.1. A support-swallowed carrier with some room left in S_l \ F is
good, with a FIXED room constant: (W*).) So (O4) is not an independent obstruction: every remaining infinite-F case is a support version of
(O1)(i), (O1)(ii), (O2) or (O3). A formal reduction of Lemma Z at infinite F to Lemma Z at finite F is equivalent to (LSC-trunc)
(Proposition 5.4) and remains OPEN.

## 8. Numerical sanity checks (finite models; evidence only)
- Z5_work/check_base_truncation.py: q*(a) = ||a||_1 + ||U^T a||, n = 60, d = 8, a with full support and geometric decay, b a pure base mate
  scaled to be tight (flips at all scales). At the truncations a^M (M = 5..40) the transferred rho b^M of Lemma 5.1 satisfies
  max_t (q*(a^M + t rho b^M) - 1)/(s(t) - 1) in [0.40, 0.96] < 1 for rho = 0.9, 0.99 (tight value 0.99998 at a itself).
- Z5_work/check_Dstar.py: the exponent of D*_l(t) in Lemma 7.1(b) (fitted -0.333, -0.001, 0.335, 0.500 vs predicted -1/3, 0, 1/3, 1/2).
- Z5_work/check_boundedfree.py: with a = u_1 (a in Y) the Hilbert-only map of Lemma lem:boundedfree loses rank, the map Phi of Lemma 5.2
  (with the first-order coordinate) is injective.

## 9. Status and next steps
Proved here (every admissible T): T1 (step (iv) of Remark rem:Binf: transfer at a not in c_00), T2, T3, T8 (engineered recovery at infinite F
under (R-inf) or (CS-data)), T9, T10 (Lemma lem:boundedfree without F finite), T11, Proposition 5.4. For the SLD operator: T4-T7 (Remark
rem:Binf is now a theorem: (SR) points with arbitrary F are in Rec; window-pinned mates at arbitrary F are recovered; sign-mixed and cushion
room), T12 (Theorem S-inf: finitely many contact- or support-swallowed bad carriers, cushion-dominated on F), T14-T16 (obstruction).
Corrections to the note: (a) Lemma lem:boundedfree and the Round-4 referee remark "F finite is essential (Y may contain a)" -- not needed
(Lemma 5.2). (b) Remark rem:Binf's step (iv) is now proved (Theorem 2.2), so Problem prob:infiniteF is settled in the (SR) case.
(c) In Remark rem:openZ, (O4) should be restated as in 7.5: "infinite base support with a bad carrier whose signature set meets the support
infinitely with inf |a_j|/v_l(j) = 0 (fast support swallowing), or the support versions of (O1)-(O3)"; first rows with (SR), sign-mixed or
cushion room, and first rows with finitely many bad carriers that are cushion-dominated on F (Theorem 6.1) are in Rec.
Open: (LSC-trunc) in general (equivalently, Lemma Z at infinite F given Lemma Z at finite F); fast-swallowed carriers (support version of
(O1)(i)); infinitely many non-resonant support-swallowed carriers (support version of (O2)/(O3), e.g. F = N with a > 0); the exact one-sided
coefficient (Theorem thm:onesided) at infinite F, where the minimizing data may have unbounded ratio on F (so (BT)-type points with infinite F
are not covered).
Suggested next steps: (1) a "cushion-sparse" exactification: replace exact cushion bounds by (CS)-sparse violations in the window two-piece
data, which requires controlling the deep-flip mass sum{f_j : |a_j| < x f_j} = o(x) uniformly on windows -- this is the same quantitative
question as near-contact sparsity in (O1)(i), and a common treatment (allowance 2|a_j|/t <-> room 1 - |z_j|) is natural; (2) Theorem thm:onesided
at infinite F restricted to data with (CS), giving (BT)-type points with infinite F; (3) for (LSC-trunc), engineer far contact signs per mate
(Theorem 4.3 shows that far contacts with the signs of the far switching cost nothing), reducing the question to producing fixed data at f.
