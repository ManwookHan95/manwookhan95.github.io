# N2 referee, part 1: first pass over N2_notes (algebra, Lemma 1.3, Theorem 1 skeleton)

Setting used by N2 and by this report: canonical base q, FINITE block set I (p_N), admissible T = Lemma B's conclusion only.

## 1.2 Algebra of exact two-piece representations -- re-derived
(a) g(xi)=0 for g in C(f) (Goldstine: net x_alpha -> xi weak*, p(x_alpha)<=1, f(x_alpha)->1, f^2+g^2<=p^2). For omega in c_00(Q):
    <omega,zeta> = d(omega)|zeta| (Fact C off peaks), <w,zeta> = |zeta|, so <omega - d w, zeta> = 0; hence b+(xi)=g(xi)=0. OK.
(b) v = sum_m R_m*(Delta omega_m - Delta d_m w_m) by linearity of d_m; R_m* omega = T(sum_k omega(k) m 2^{-m-k} e_{k,m}) in Y for omega in
    l_inf. z_j v_j = |b+_j|+|b-_j| on K. OK.
(c) d''(omega) = sum_k Phi^2 w''(k) omega(k)/C'' = sum zeta''(k) omega(k)/|zeta''| (Fact C at f'', omega off P''). OK.
(d) v=0 => L*((Delta omega_m - Delta d_m w_m)_m)=0 => Delta omega_m = Delta d_m w_m, and at a peak (w != 0, Delta omega = 0) Delta d_m = 0. OK.
    v != 0 => v in Y\{0}, Y cap c_00 = {0} => supp v infinite, inside F cup K, F finite. f NA => zhat in c_0 => K finite. OK.
(e) Base: ||a+tau b||_1 = ||a||_1 + tau b(z) for small tau>0 (F finite, z-signed on K); Hilbert excess
    nu*Psi(h) >= tau^2 h(b)/(2(1+tau||U*b||/nu)) since sqrt((1+al)^2+be^2)-(1+al) = be^2/(sqrt(..)+1+al) and both terms <= 1+||h||. OK.
    Block: N(w+tau(omega-d w)) = 1 + tau^2||h_perp||^2/(sqrt(Y^2+tau^2||h_perp||^2)+Y), Y = C + tau d(1-C) -- re-derived exactly
    (the first-order terms -tau d M + tau d(1-C) cancel since M+C=1). OK.
(f) convexity. OK.
VERDICT 1.2: PROVED (correct).

## 1.3 Convex block lemma -- re-derived
W = (1-s)[(1-tau~ d'')w'' + tau~ omega] + s y: (1-s)(1-tau~ d'') = 1-s-tau d'', (1-s)tau~ = tau. Triangle inequality + N(y)<=1. OK.
Bound N(W) <= 1 + tau^2 H''/(2(1-s)) (1+...) follows from A Lemma 4.4(d) applied with tau~ (needs |tau~| <= r''). OK.
VERDICT: PROVED. (Trivial but correct; the content is that the w-direction is an inward direction for s>=0.)

## 1.4 Base excess at an NA point -- re-derived
||a'+tau B||_1 = ||a'||_1 + tau B(z') + kink' (no sign change on supp a'); Hilbert: Psi(h) <= be^2/(2(1+al)) <= be^2/(2(1-||h||)).
Sum: 1 + tau B(xhat') + kink' + tau^2 h'(B)/(2(1-|tau| ||U*B||/nu')). OK. Also the generalisation used implicitly later:
|a + x| <= |a| + sign(a) x + 2|x| for all reals (so sign changes on supp a' cost <= 2|tau B_j|). OK.

## 1.5 Convergence of engineered approximants
L compact => L** weak*-to-norm on bounded sets (range in V); J_V norm-to-weak* continuous at smooth points (Smulian; all block
components of L**zhat nonzero because the normalized u_{k,m} are dense in S_Y and Y is dense); L* weak*-to-norm on bounded sets.
grad q(x'_n) = a'_n by Fact D. OK. PROVED (relies on A Fact E for the "data converge" part).

## 1.6 Kink-class identification: ISSUE (to be checked against C_referee 1.20)
omega'' := v''_Q - (c'/M) w 1_Q is in general NOT finitely supported (w(k) = C zeta(k)/(Phi(k)^2|zeta|) on Q), so (E2) fails unless
Q is finite or w vanishes on Q off a finite set. The algebra (Delta d = -(s+ - s-)c'/M, Lemma 1.2(c) extended to bounded omega'' on Q)
is correct; the CLASS identification needs either Q finite or an extension of Def 1.1 / Theorems 1-3 to omega in l_inf(Q).

## Theorem 1 -- line-by-line check of Steps 0-8 (first pass)
Step 2 estimates re-derived: |<U*v,E(A_n(0))-e>| <= D_n||U||/(2(||U||+1)) + (1/2)S, S := sum_Far |v_j| in [D_n,2D_n];
psi_n(0) <= -D_n, >= -6.5 D_n. 2.2(b): derivative = sigma_+ <P_{E-perp}U*v, U*e*_{j+}>/||U*A_mu||, continuous at (a,0). IVT OK.
Step 4: b'+ = b'_0 + theta v (uses Delta d' = 0), b'+(x') = theta psi_n = 0. OK.
Step 5: certificate (b'_0, omega_theta) at f'_n, coordinatewise radius ~3t_n (window masses 4t_n|b_theta,j|). Need: kappa(c') does
   not involve the coordinate ratio ||b/a'||_inf (TO CHECK in A Def 4.1/Prop 4.5).
Step 6: no sign change on F (4T_0 rho Gamma <= a_min/4), on window contacts (b+ z-signed, a' z-signed), on Far_n
   (|a'_j| >= (3/2)T_0 rho|v_j| >= (3/2)|tau rho theta v_j|); window contacts with b_theta,j = 0 but b+_j != 0 carry no mass,
   are contacts of f' (z'_j = z_j = +-1) with z-signed entries: kink 0. Kink only beyond N''_n: <= 3(1-rho^2) tau t_n/16. OK.
   Constants: base <= 1 + tau^2[rho^2(1+eta_0)^2/2 + 3(1-rho^2)/16] <= 1 + tau^2[1/2 - (1-rho^2)/16] <= s(tau). OK.
Step 7: s(tau)-s(rho tau) = (1-rho^2)tau^2/(s(tau)+s(rho tau)) >= (1-rho^2)min(tau^2,|tau|)/(2 sqrt 2) >= (1-rho^2)min(tau^2,|tau|)/3. OK.
Step 8: rho g' in C(f') <=> p*(f'+t rho g') <= s(t) for all t (p*(rho g') <= 1 is the t -> infinity limit). OK.
First-pass verdict: Theorem 1 correct modulo the imports (A Prop 4.5 constants, Lemma 4.4(d) radii, Fact A).
