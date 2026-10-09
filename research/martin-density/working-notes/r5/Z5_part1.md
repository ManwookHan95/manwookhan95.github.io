# Z5 part 1: transfer peaks at an arbitrary base vector (step (iv) of Remark rem:Binf)

Setting and notation: those of the note paper/martin_density_note.tex (Sections 1-8). T is an arbitrary admissible
operator, I is finite, f in S_{p*} has forced data (xi, q_0, a, w, F, z, zhat, e, nu), F = supp a may be INFINITE.
"Balanced finite certificate" is used in the sense of Definition def:tame: g = b + sum_m R_m*(omega_m - d_m(omega_m) w_m)
with b in l_1(F), b(xi) = 0, omega_m in c_00(Q_m). We add the adjective "finitely based" when supp b is finite.

## 1.1 The truncated canonical approximants. PROVED (any admissible T, any f).

For N in N with a 1_{[1,N]} != 0 put
  c_N^a := q*(a 1_{[1,N]}),   a_N := a 1_{[1,N]} / c_N^a,   F_N := supp a_N = F cap [1,N],
  e_N := U*a_N / ||U*a_N||,   nu_N := ||U*a_N||,   z^N := z 1_{[1,N]},   xt_N := z^N + U e_N,
  x'_N := xt_N / p(xt_N),     f'_N := grad p(x'_N),   c_N := q(x'_N) = 1/p(xt_N).
(For a in c_00 and N >= max F these are the canonical truncations of Section 5.2 of the note.)

Lemma 1.1. (a) f'_N is norm attaining, f'_N in S_{p*}, its forced data are a_N, e_N, z^N, zhat'_N = xt_N, and
f'_N = a_N + sum_m R_m* w'_{m,N} with w'_{m,N} = J_m(R_m x'_N).
(b) a_N -> a in l_1, nu_N -> nu, e_N -> e in H, f'_N -> f in norm, and all forced data of f'_N converge to those of f
as in Proposition prop:continuity; x'_N -> xi weak*, c_N -> q_0.
(c) (Base identity at f'_N.) For every B in l_1 with supp B contained in F_N and every real t such that
sgn(a_N(j) + t B_j) = sgn a_N(j) for all j in F_N,
  q*(a_N + tB) = 1 + t B(xt_N) + nu_N Psi_N(t U*B/nu_N),   Psi_N(h) := ||e_N + h|| - 1 - <e_N, h>,
and Psi_N(h) <= ||P_N^perp h||^2 / (2(1 - ||h||)) for ||h|| <= 1/2, P_N^perp := orthogonal projection onto e_N^perp.

Proof. (a) a_N in c_00, q*(a_N) = 1; z^N in c_00, |z^N| <= 1, and z^N_j = z_j = sgn a_j = sgn a_N(j) on F_N
(Proposition prop:forced(c)). Proposition prop:smooth(c) gives q(xt_N) = 1, grad q(xt_N) = a_N and
grad p(xt_N) = a_N + L*J_V(L xt_N); f'_N attains its norm at x'_N; Proposition prop:forced at x'_N identifies the data.
(b) c_N^a -> q*(a) = 1 (q* is continuous and a 1_{[1,N]} -> a in l_1), so a_N -> a in l_1; U* is bounded, so
nu_N -> nu > 0 and e_N -> e. z^N -> z coordinatewise. Proposition prop:approximants ((ii) => (i), stated for every
f in S_{p*}) gives f'_N -> f, and Proposition prop:continuity (valid for every norm convergent sequence in S_{p*})
gives the convergence of the forced data.
(c) On F_N, |a_N(j) + tB_j| = |a_N(j)| + z^N_j t B_j (no sign change, z^N_j = sgn a_N(j)); off F_N, B_j = 0. So
||a_N + tB||_1 = ||a_N||_1 + t B(z^N). Also ||U*a_N + tU*B|| = nu_N ||e_N + tU*B/nu_N|| = nu_N + t<U*B, e_N> +
nu_N Psi_N(tU*B/nu_N). Add, and use ||a_N||_1 + nu_N = 1 and B(z^N) + <U*B, e_N> = B(xt_N). The bound for Psi_N is
Lemma lem:base (it only uses ||e_N|| = 1). QED

## 1.2 Theorem T-inf (transfer peaks at arbitrary base support). PROVED.

Theorem 1.2. Let T be admissible, I finite, f in S_{p*} (F arbitrary), and let
  g = b + sum_m R_m*(omega_m - d_m w_m)
be a finitely based balanced finite certificate at f (supp b finite, supp b in F, b(xi) = 0, omega_m in c_00(Q_m),
d_m = d_m(omega_m)) such that (f, g) is contractive (g in C(f)) and Gamma_w(g) = q_0 h(b) + sum_m sigma_m H_m(omega_m) <= 1.
Then for every rho in (0,1) there are g'_N -> g with rho g'_N in C(f'_N) for all large N, where f'_N are the truncated
canonical approximants of 1.1 (which do not depend on g). In particular (f, rho g) and (f, g) lie in cl NA((c_0,p), l_2^2).

Proof. This is the proof of Theorem thm:transfer of the note with a replaced by a_N in the approximants; we list every
place where a in c_00 was used and give the replacement. All other steps (Steps 2, 3 and the block parts of Steps 1, 4, 5,
and Step 6) use only Lemma lem:threshold at x'_N, Lemma lem:block, the convergence of the forced data of f'_N to those
of f (Lemma 1.1(b)), Lemma lem:dualball, the transfer peaks built at xi from a (which exist for every f: they use the
density of the tails of (u_{k,m})_k and the vector tau_{*,m} = (pi_m(xi)/q_0) a - pi_m, defined for any a), and the
contractivity of (f, g); they hold verbatim.

Step 1 (base). Put kappa_N := b(xt_N), b'_N := b - kappa_N a_N. Since b in l_1 and xt_N -> zhat weak* with
||xt_N||_inf <= 1 + ||U||, kappa_N -> b(zhat) = b(xi)/q_0 = 0; with a_N -> a this gives b'_N -> b in l_1.
For N >= max supp b, supp b'_N is contained in F_N, and b'_N(xt_N) = kappa_N - kappa_N a_N(xt_N) = 0 because
a_N(xt_N) = ||a_N||_1 + nu_N = 1. Let r_b := min_{j in supp b} |a_j|/(4|b_j|) > 0 (finite support). For N so large that
c_N^a <= 2 and |kappa_N| <= 1/4, and |t| <= min(r_b, 1): on supp b, |t b'_N(j)| <= |a_j|/4 + |a_N(j)|/4 <= (3/4)|a_N(j)|
(as |a_N(j)| = |a_j|/c_N^a >= |a_j|/2); on F_N \ supp b, |t b'_N(j)| = |t kappa_N| |a_N(j)| <= |a_N(j)|/4. So no
coordinate changes sign and Lemma 1.1(c) gives
  q*(a_N + t b'_N) = 1 + nu_N Psi_N(t U* b'_N / nu_N).
Since U*a_N is parallel to e_N, P_N^perp U* b'_N = P_N^perp U* b, and P_N^perp -> P^perp in operator norm (e_N -> e), so
h_N := ||P_N^perp U*b||^2/nu_N -> ||P^perp U*b||^2/nu = h(b) =: H_b. With ||U*b'_N|| <= 2||U*b|| + 1 for N large, we get
  q*(a_N + t b'_N) <= 1 + (t^2/2) H_b theta(t),   theta(t) -> 1 as t -> 0, uniformly in large N
(if H_b = 0 then the bound reads q*(a_N + t b'_N) <= 1 + (t^2/2) theta_0(t) with theta_0(t) -> 0; use h_N -> 0 in place of
the factor H_b). This replaces Step 1 (base) of the note's proof, where a was kept fixed.

Step 4 (transport of the transfer data). Replace beta_{m,N} := ((R_m* y_{m,N})(x'_N)/c_N) a by
beta_{m,N} := ((R_m* y_{m,N})(x'_N)/c_N) a_N and e_{m,N} := R_m* y_{m,N} - beta_{m,N}. Since R_m* y_{m,N} -> R_m* y_m in
l_1, x'_N -> xi weak* (bounded), c_N -> q_0 and a_N -> a in l_1, we get e_{m,N} -> R_m* y_m - ((R_m* y_m)(xi)/q_0) a =
e_{infty,m}. The bookkeeping identity (eq:bookkeeping) is an identity at x'_N (Lemma lem:threshold at x'_N and the margin
identity (eq:margin) at k_*), unchanged.

Step 5 (the decomposition). Put A(t) := a_N + t rho b'_N + sum_m eps_m R_m* y_{m,N} and W_m(t) := w'_{m,N} +
t rho v'_{m,N} - eps_m y_{m,N}, with eps_m := tau_m rho^2 t^2, v'_{m,N} := omega_m - d'_{m,N} w'_{m,N}. Then
A(t) + sum_m R_m* W_m(t) = f'_N + t rho g'_N with g'_N := b'_N + sum_m R_m* v'_{m,N}. By (eq:bookkeeping),
A(t) = (1 + E) a_N + t rho b'_N + sum_m eps_m e_{m,N}, E := rho^2 t^2 sum_m (tau_m sigma'_{m,N} e_{y,m,N} +
|tau_m| ell_m mu'_{*,N})/c_N, and by homogeneity and Step 1,
  q*(A(t)) <= (1+E) q*(a_N + (t rho/(1+E)) b'_N) + rho^2 t^2 sum_m |tau_m| q*(e_{m,N})
          <= 1 + E + rho^2 t^2 H_b theta(t)/(2(1+E)) + rho^2 t^2 sum_m |tau_m| q*(e_{m,N}),
which is the inequality of the note's Step 5 with a replaced by a_N; the rest of Step 5 (blocks) is unchanged.

Convergence g'_N -> g: b'_N -> b, d'_{m,N} -> d_m and R_m* w'_{m,N} -> R_m* w_m (Lemma 1.1(b)); and g'_N(x'_N) = 0
(b'_N(x'_N) = c_N b'_N(xt_N) = 0; for N large supp omega_m consists of strict non-peaks of w'_{m,N}, and Lemma lem:algebra
at x'_N gives (omega_m - d'_{m,N} w'_{m,N})(R_m x'_N) = 0).

Step 6 (large t) uses p*(f'_N - f) -> 0 and p*(g'_N - g) -> 0 only. Hence rho g'_N in C(f'_N) for N large;
f'_N is norm attaining, so (f'_N, rho g'_N) attains its norm (Proposition prop:reduction(d)) and converges to (f, rho g);
let rho -> 1. QED

Remark 1.3. (a) The certificate must be FINITELY based (or at least ||b/a||_inf < infinity on a finite set outside of which
b = 0) only for the no-flip radius r_b of Step 1; this is the only point where the support of b enters.
(b) For a in c_00 and N >= max F, Theorem 1.2 is Theorem thm:transfer (then a_N = a).
(c) Consequence (windowed averaging at arbitrary F). Theorem thm:windowed holds for every f in S_{p*} (F arbitrary) when
the certificates c_t of its hypothesis are finitely based: the proof of thm:windowed uses F finite only in its last
sentence ("since a in c_00, Theorem thm:transfer gives ..."); the averaged certificate c = (1/n) sum_i c_{t_i} is finitely
based, rho g_c in C(f) and Gamma_w(rho c) <= 1, so Theorem 1.2 applies to rho g_c. PROVED.
