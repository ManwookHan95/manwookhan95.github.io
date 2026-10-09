# R3 part 2: conversion of generic coordinates by vanishing window moves (Theorem EC) and the room lemma

Setting of 1.0. Fix a block m_0 in I and write u_k := u_{k,m_0}, lambda_k := lambda_{k,m_0}, Phi(k) := Phi_{m_0}(k).
||.||_{inf->inf} is the operator norm on l_inf^d.

## 2.1 Theorem EC (generic carriers at engineered approximants). PROVED.
Let f in S_{p*} and let x'_N = z'_N + U e'_N (N in N) be NA normer data (Fact D) with a'_N -> a in l_1 and z'_N -> z
coordinatewise (e.g. the canonical truncations, or any engineered approximants of P2A/N2). For each n in N let be given:
 (i) d_n in N and targets b_{n,1}, ..., b_{n,d_n} in S_{q*} with b_{n,i}(zhat) = 0;
 (ii) a finite set G_n subset J (free coordinates of f), gamma_n := 1 - max_{j in G_n} |z_j| > 0, and vectors
      eta_{n,1}, ..., eta_{n,d_n} in c_00(G_n) with ||eta_{n,l}||_inf <= 1 such that B_n := (b_{n,i}(eta_{n,l}))_{i,l} is invertible;
      beta_n := ||B_n^{-1}||_{inf->inf};
 (iii) a finite set Pi_n of "protected" functionals phi in l_1 with phi(eta_{n,l}) = 0 for all phi in Pi_n and all l;
 (iv) a depth bound Phibar_n > 0 and a precision eps_n > 0 with  8 (2 + ||U||) d_n beta_n eps_n <= min(gamma_n, 1/n).
Then there are N(n) >= n, distinct indices k_{n,1}, ..., k_{n,d_n} and window moves eta'_n in span{eta_{n,l}} such that,
with x''_n := x'_{N(n)} + eta'_n:
 (a) ||u_{k_{n,i}} - b_{n,i}||_1 <= eps_n and Phi(k_{n,i}) <= Phibar_n (generic coordinates from the dense tails);
 (b) ||eta'_n||_inf <= min(gamma_n, 1/n)/2; x''_n is NA normer data with the same base functional a'_{N(n)}, its z-part
     z''_n := z'_{N(n)} + eta'_n tends to z coordinatewise, and f''_n := grad p(x''_n) -> f in norm (with all forced data
     converging as in A Fact E); phi(x''_n) = phi(x'_{N(n)}) for every phi in Pi_n;
 (c) u_{k_{n,i}}(x''_n) = 0 for all i; hence every k_{n,i} is a strict non-peak of block m_0 of f''_n with
     w''_{n}(k_{n,i}) = 0, gap''(k_{n,i}) = M''_n := M''_{n,m_0}, and d''(e_{k_{n,i}}) = 0;
 (d) for every c in R^{d_n}, c''_n(c) := (0, omega) with omega_{m_0} := sum_i (c_i/lambda_{k_{n,i}}) e_{k_{n,i}} (other blocks 0) is a finite
     certificate at f''_n (A Def 4.1) with
       g_{c''_n(c)} = sum_i c_i u_{k_{n,i}},   ||g_{c''_n(c)} - sum_i c_i b_{n,i}||_1 <= eps_n ||c||_1,
       H(c''_n(c)) = ||c||_2^2/(m_0^2 C''_n) - 0 <= ||c||_2^2/(m_0^2 C''_n),   kappa(c''_n(c)) = 0,
       r(c''_n(c)) >= M''_n min_i lambda_{k_{n,i}} / (2 ||c||_inf);
     consequently (A Prop 4.5) p*(f''_n + s g_{c''_n(c)}) <= 1 + s^2 ||c||_2^2/(2 m_0^2 C''_n) for |s| <= M''_n min_i lambda_{k_{n,i}}/(2||c||_inf).

### Proof.
Step 1 (indices). Choose K_n with 2^{-m_0-K_n} <= Phibar_n. By (T2) every tail of (u_k) is dense in S_{q*} for q*, hence for
||.||_1 <= q*. Choose successively k_{n,1} < ... < k_{n,d_n}, all >= K_n, with ||u_{k_{n,i}} - b_{n,i}||_1 <= eps_n. Then
Phi(k_{n,i}) <= 2^{-m_0-k_{n,i}} <= Phibar_n. This is (a).
Step 2 (the linear system). Put A_n := (u_{k_{n,i}}(eta_{n,l}))_{i,l} = B_n + E_n. Each entry of E_n is (u_{k_{n,i}} - b_{n,i})(eta_{n,l}),
of modulus <= eps_n, so ||E_n||_{inf->inf} <= d_n eps_n and ||B_n^{-1} E_n|| <= d_n beta_n eps_n <= 1/16 by (iv). Hence A_n is
invertible and ||A_n^{-1}||_{inf->inf} <= beta_n/(1 - 1/16) <= 2 beta_n (Neumann series).
Step 3 (choice of N(n)). For b in l_1, b(x'_N) = b(z'_N) + <U*b, e'_N> -> b(z) + <U*b, e> = b(zhat): the first by dominated
convergence (||z'_N||_inf <= 1, z'_N -> z coordinatewise), the second because U*a'_N -> U*a in H and ||U*a|| = nu > 0, so
e'_N -> e. Since b_{n,i}(zhat) = 0 and G_n is finite with |z_j| <= 1 - gamma_n on G_n, we can choose N(n) >= n with
  (3a) 4 d_n beta_n max_i |b_{n,i}(x'_{N(n)})| <= min(gamma_n, 1/n)/4,
  (3b) |z'_{N(n)}(j) - z_j| <= gamma_n/4 for j in G_n.
By (3b), |z'_{N(n)}(j)| <= 1 - 3 gamma_n/4 < 1 on G_n, so G_n is disjoint from supp a'_{N(n)} (Fact D: z' = sign a' on supp a').
Step 4 (the move). Let v_n(i) := u_{k_{n,i}}(x'_{N(n)}) and s_n := -A_n^{-1} v_n, eta'_n := sum_l s_{n,l} eta_{n,l}. Since ||x'_N||_inf <= 1 + ||U||,
|v_n(i)| <= |b_{n,i}(x'_{N(n)})| + eps_n (1 + ||U||). Therefore
  ||eta'_n||_inf <= ||s_n||_1 <= d_n ||s_n||_inf <= 2 d_n beta_n ( max_i |b_{n,i}(x'_{N(n)})| + eps_n(1 + ||U||) )
                 <= min(gamma_n, 1/n)/8 + min(gamma_n, 1/n)/4 <= min(gamma_n, 1/n)/2,
by (3a) and (iv). By construction u_{k_{n,i}}(x'_{N(n)} + eta'_n) = v_n(i) + (A_n s_n)(i) = 0, and phi(eta'_n) = 0 for phi in Pi_n.
Step 5 (validity, (b)). Put z''_n := z'_{N(n)} + eta'_n. It is in c_0 (eta'_n in c_00), it coincides with z'_{N(n)} off G_n, and on G_n
|z''_n(j)| <= 1 - 3gamma_n/4 + gamma_n/2 < 1. As supp a'_{N(n)} misses G_n, z''_n = sign a'_{N(n)} on supp a'_{N(n)}. By Fact D,
x''_n = z''_n + U e'_{N(n)} is NA normer data with base functional a'_{N(n)} (q(x''_n) = 1 = a'_{N(n)}(x''_n)), and
f''_n := grad p(x''_n) is in NA cap S_{p*}. For each fixed j, z''_n(j) -> z_j since z'_{N(n)}(j) -> z_j (N(n) -> infinity) and
||eta'_n||_inf -> 0; and a'_{N(n)} -> a. N2 Lemma 1.5 gives f''_n -> f in norm with convergence of all forced data.
Step 6 ((c)). The normer of f''_n is xi''_n = x''_n/p(x''_n), and (R_{m_0}** xi''_n)(k) = lambda_k u_k(xi''_n) = 0 for k = k_{n,i}.
By Fact C at f''_n, k is a peak iff m_0 |u_k(xi''_n)| >= Phi(k) M''_n |zeta''_n|/C''_n, which fails since the right side is > 0;
so k is a strict non-peak and w''_n(k) = C''_n m_0 u_k(xi''_n)/(Phi(k)|zeta''_n|) = 0, gap''(k) = M''_n. Then
d''(e_k) = <D w''_n, D e_k>/C''_n = Phi(k)^2 w''_n(k)/C''_n = 0.
Step 7 ((d)). c''_n(c) = (0, omega) satisfies (C1) trivially (b = 0) and (C2) (omega in c_00, supp omega in the strict non-peaks).
d = <D w'', D omega>/C'' = sum_i (c_i/lambda_{k_{n,i}}) Phi(k_{n,i})^2 w''(k_{n,i})/C'' = 0. g_c = R_{m_0}* omega =
sum_i (c_i/lambda_{k_{n,i}}) lambda_{k_{n,i}} u_{k_{n,i}} = sum_i c_i u_{k_{n,i}}, and ||g_c - sum_i c_i b_{n,i}||_1 <= sum_i |c_i| eps_n.
H = (||D omega||^2 - d^2)/C'' = sum_i (Phi(k_{n,i}) c_i/lambda_{k_{n,i}})^2/C'' = ||c||_2^2/(m_0^2 C'') (lambda = m_0 Phi).
kappa = max(2 ||U*0||/nu'', 2|d| M''/C'') = 0. In r(c) only the term gap(omega)/(2||omega||_inf) is finite:
gap(omega) = M''_n and ||omega||_inf = max_i |c_i|/lambda_{k_{n,i}} <= ||c||_inf/min_i lambda_{k_{n,i}}. A Prop 4.5 gives the last claim. QED.

## 2.2 Remarks on Theorem EC
(1) NO rate is involved. The only quantitative link between the precision eps_n and the depth is (iv), which involves the
    fixed data (d_n, beta_n, gamma_n) only. In particular the depth bound Phibar_n can be chosen FIRST and arbitrarily small,
    and eps_n arbitrarily small; the adversary's control of approximation rates (Lemma B allows arbitrarily slow rates)
    only affects how deep the chosen coordinates are, which is irrelevant for (b)-(d) (it only shrinks the radius).
(2) Hypothesis (ii) is pure linear algebra: vectors eta_{n,l} as required exist iff no nontrivial combination
    sum_i mu_i b_{n,i} restricted to G_n lies in span{phi restricted to G_n : phi in Pi_n} (duality in the finite-dimensional
    space c_00(G_n) = R^{G_n}). For a fixed finite family of targets in zhat-perp whose restrictions to the free coordinates
    are linearly independent modulo the protected ones, (ii) holds with G fixed and beta fixed.
(3) Protected functionals keep prescribed scalars of the approximant unchanged: e.g. v(x'), the u_{k,m}(x') of finitely many
    designated carriers (statuses with margin are then preserved for n large, since |zeta''|, M'', C'' converge), or the
    group scalars of detectors (which live far, so they are unaffected anyway when G_n is in a window).
(4) The theorem is the rigorous form of E's counter-strategy (C1)/(C3) and of A Lemma 8.2 ("implanted fine coordinates"),
    with two differences that matter: conversion uses WINDOW moves of size o(1) (allowed by E Prop 8.2, which only forbids
    moves of size bounded below), so it does not need far tails (which an adversary can make arbitrarily small: N2 4.5);
    and the targets may be chosen after the approximant index (diagonal form), so the precision can tend to 0.
(5) If J is too small (e.g. J finite and d_n -> infinity is wanted) one can use contacts j in K (|z_j| = 1, j notin F) after
    first pulling them inside, z'_n(j) := (1 - gamma'_n) z_j with gamma'_n -> 0, at the price of losing those contacts for
    base engineering at stage n. SKETCH (routine).

## 2.3 Lemma (room lemma: O(s) errors need O(s^2) room). PROVED.
In the situation of Theorem EC, let s > 0, kappa >= 0 and c in R^{d_n} with ||c||_inf <= kappa s, and put
lambda_gen,n := min_i lambda_{k_{n,i}}. If s^2 <= M''_n lambda_gen,n /(2 kappa), then for all |t| <= s
  p*(f''_n + t g_{c''_n(c)}) <= 1 + t^2 d_n kappa^2 s^2/(2 m_0^2 C''_n),
i.e. the vector g_{c''_n(c)} (an approximation, within eps_n ||c||_1 <= eps_n d_n kappa s, of the "error" sum_i c_i b_{n,i} of size
O(kappa s)) is carried two-sidedly at all scales |t| <= s with a Hilbert coefficient O(s^2).
*Proof.* r(c''_n(c)) >= M''_n lambda_gen,n/(2 kappa s) >= s, and H <= ||c||_2^2/(m_0^2 C'') <= d_n kappa^2 s^2/(m_0^2 C''); apply 2.1(d). QED.
Reading. A frozen or boundary-layer error of size kappa s that has to be carried up to scale s only needs carriers of depth
lambda_gen >~ 2 kappa s^2/M: quadratically finer than the scale. C's "implant scale gap" (an implanted carrier at depth
Phi covers only scales <~ Phi, while the slack starts at ~sqrt(Phi)) concerns carrying O(1)-size components; for O(s)-size
components the gap disappears. This is the arithmetic fact behind Part 4.
