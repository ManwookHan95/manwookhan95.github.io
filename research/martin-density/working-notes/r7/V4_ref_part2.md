# V4 referee, part 2: Prop. 5.1, Lemma 2.6, Cor. 3.1, Prop. 3.2, Lemma 3.3, Lemma 3.4 (+ numerics)

## 2.1 Proposition 5.1 (near-threshold carriers are Baire-generic in every fixed-z fibre).  CORRECT.
Re-derived.  (1) a -> b(a) = (s_j a_j)/||(s a)|| is a homeomorphism of A onto the open orthant Omega of S^{d-1} (inverse a_j = t b_j/s_j,
t = 1/(1 + sum|b_j|/s_j)); zhat_j = sigma_j + s_j b_j on F; psi_y(b) := y(zhat(b)) affine; zeta_m(b) is l_1-continuous, theta_m(b) continuous
(unique root of Psi, jointly continuous and strictly decreasing near the root).  (2) psi_y(b_0) = sum_F n_j(sigma_j + s_j b_{0j}) + c z_{j_1}^2 = 0;
its tangential gradient at b_0 is the projection of (n_j s_j) onto b_0^perp, non-zero as (n_j s_j) is not parallel to b_0 (d >= 2).  For
the carriers l_i with q*(u_{l_i} - y) -> 0 (T-d): |val_{l_i}(b) - psi_y(b)| <= |(u - y)(z)| + |<U^*(u - y), e>| <= q*(u_{l_i} - y) uniformly in b.
G_i = m|val_{l_i}|/Phi_{l_i} - theta_m is continuous, > 0 at b_+ (Phi -> 0) and = -theta_m < 0 at a zero of val_{l_i} on a path in O; so
{|G_i| < eps_{l_i}} ∩ O is open and non-empty.  (3) Baire.  The non-(BT) conclusion holds for ANY eps_l -> 0: infinitely many peaks with
mu_l < q_0 Phi_l eps_l/m give sum{Phi : mu < s_l} >= Phi_l with Phi_l/s_l = m/(q_0 eps_l) -> infinity, so the specific choice
eps_l = (Phi_{l+1}/Phi_l)^2 is not needed.  Remarks: (i) one contact suffices (even none: for d >= 2 the hyperplane
{n : sum n_j(sigma_j + s_j b_{0j}) = 0} is never the line R(b_0/s), because sum_j |b_{0j}|/s_j + 1 > 0); (ii) consequence (b) "(BT) is meagre in
every fixed-z fibre, although dense": "dense" refers to {f : F finite} with z varying (Prop. 5.3), not to the fibre; (iii) the same Baire
argument with windows |val_l| < eps_l around ZERO shows that, in every fixed-z fibre, generic a also has infinitely many carriers with
|val_l| < eps_l (for any eps_l > 0), in particular infinitely many NEGLIGIBLE carriers in the sense of Section 9 (relevant to Theorem 5.6,
see part 4).  Consequences (a) ((GO) negative), (c) (exactly degenerate peaks dense in each fibre: G_i = 0 somewhere in O) and (d) correct.

## 2.2 Lemma 2.6 (lacunary profiles exclude critical flip profiles).  CORRECT; its use as a design remedy is costly.
Proof re-derived: (i) beta_k <= C x_k for x_k < x_0 (let x decrease to x_k in m(x) >= beta_k); (ii) with x = beta_i/(2C) < min(x_0, x_*) every
counted k has k >= k_0 and beta_k < beta_i/2, hence k > i (beta eventually decreasing by factor 2), and m(x) <= sum_{k>i} beta_k <= 2 beta_{i+1}
<= c x/2.  Application: along S_l ∩ F the ratios are <= those along S_l, so they still tend to 0.  The critical class of Y3/Y3-ref
((O4-crit): 0 < liminf m/x <= limsup m/x < infinity) is exactly what is excluded.
COST (the "price" paragraph, labelled HEURISTIC, is accurate and should be stated more sharply): with h_l = sum 2^{-s} e_s^*, a lacunary
profile means gaps of S_l tending to infinity.  This is incompatible with the bounded-gap requirements used elsewhere: Y3's design
D_sigma ((D0') bounded gaps; Theorem 3.5, super-critical support swallowing), Y4-ref (G) (Prop. P4, exact two-sided per-carrier
tuning by pulls + private banks), and V1's D_Omega (S_l = {2^l(2i+1)}).  Concretely, with lacunary S_l the cheapest exact lowering of
val_l by x uses a pull at s_i with 2 v_l(s_i) >= x and a bank compensating the overshoot 2 v_l(s_i) - x, at cost ~ v_l(s_i) (design factor),
which exceeds x log(1/x) by the unbounded gap factor v_l(s_i)/v_l(s_{i+1}).  So Lemma 2.6 trades (O4-crit) for (a) loss of the finite-F
exact-tuning toolbox in its bounded-gap form and (b) MIXED profiles (liminf m/x = 0 < infinity = limsup m/x), which Lemma 2.6 does not
exclude and which no proved result covers (Y3's liminf-sparsity extension is a SKETCH, hypothesis liminf m(x) log(1/x)/x = 0).
Verdict: Lemma 2.6 PROVED; "(E) critical form excluded by design" correct as stated; it does not shrink the open core.

## 2.3 Corollary 3.1 (the realizing rows are (BT)).  CORRECT.
(a) f_SA: F finite, Q_m ⊂ {k_-}, no degenerate peak, (MS) (Theorem 2.2 Step 8).  (b) For the weak-peak rows of Remark 2.3(1) built with
the HYSTERETIC owner rule (part 1, 1.7), every re-run carrier has margin >= q_0 delta°_l/4, the weak peak has a fixed positive margin, l_-
a fixed gap: (BT).  (c) "finitely-tuned variants" should be defined: rows built by the (hysteretic) owner rule from some level K on, with
finitely many exceptional carriers below K, none of them a degenerate peak.  With that definition (c) holds verbatim.  The corollary
is just cor:BTrecovered applied; the remark "a counterexample inside (B)-(D) must violate (BT)" is a tautology of cor:BTrecovered.

## 2.4 Proposition 3.2 (explicit coherent-shift mates).  CORRECT; re-derived and re-checked at 120 digits.
(i) d(e_{k_-}) = Phi_-^2 w(k_-)/C = zeta^(k_-)/|zeta^| (lem:threshold off P).  (ii) R^* w = M sum_{k != k_-} lambda_k eps_k u_k + lambda_- w(k_-) u_-,
and val_- lambda_- w(k_-)/|zeta^| = C m^2 val_-^2/|zeta^|^2 < 1 because |zeta^|^2 = B(theta) >= Phi_-^2 nu_-^2 = m^2 val_-^2 and C < 1; so
V 1_{F^c} = (c_1 - c_2 lambda_-) v_- + c_2 W 1_{F^c}, c_1 in (0,1], c_2 = eta M/(n|zeta^|) > 0; on S_{l_-}, V(s) = c_1 v_-(s) + c_2(W(s) - lambda_- v_-(s)) >=
(c_1 - 2^{-5} c_2 lambda_-) v_-(s) > 0.  (iii) b^+ - b^- = Delta_alpha lambda_- V = R^*(omega^- - omega^+) - Delta d R^* w checked symbolically; side
admissibility checked; V(zhat) = val_- - (val_-/|zeta^|)<w, zeta^> = 0, so both b^+-(xi) = 0 once beta^+ (a multiple of a) balances b^+.
(iv) prop:onesidedupper requires F finite, g(xi) = 0 and a side-admissible pair: satisfied; it yields r_0 > 0 with p*(f + r g) <= 1 +
(r^2/2)(kappa_w + 1) for |r| <= r_0, and then c g in C(f) for c <= c_0(kappa_w, r_0, p*(g)) (both regimes |tc| <= r_0 and |tc| >= r_0 checked
with s(t) - 1 >= min(t^2, |t|)/3).  Recovery: thm:engineered with (SC) (Theorem 2.2(f)), or directly cor:BTrecovered.
NUMERICS (new, V4_ref_work/sa_check_dec.py, 120-digit decimal arithmetic, (SF*)-type weights): V4's double-precision run tunes
n_- val_- to -4.7e-16, i.e. one ulp, so its sign checks for l_- are at round-off level.  At 120 digits: n_- val_- = -4.18e-60 = target,
l_- strict non-peak with nu/theta = 0.25 exactly as designed, q_- = -2.3e-59 < 0, all other carriers peaks with sign eps and nu/theta from
5 to 8.4e124, N(w) - 1 = 1e-117, <w, zeta> - |zeta| = 5e-118, W and V z-signed off F, V(zhat) = -6.5e-121, Delta d/Delta_alpha = -5.4e-118 < 0.
Confirms Theorem 2.2 and Proposition 3.2 in the finite model.

## 2.5 Lemma 3.3 and Lemma 3.4.  CORRECT.
Lemma 3.3: b^+ - b^- = sum R^*(omega^- - omega^+) - sum (d(omega^-) - d(omega^+)) R^* w; b^+- vanish at free coordinates; z b^+ >= 0 >= z b^- on K.
Lemma 3.4: "all target coordinates contacts" forces supp y_l ∩ F = {} (contacts are off F by definition), so n_l val_l = sum sigma_j y_l(j) +
eps_l delta_l H_l with sigma_j = z_j in {-1, 1} and (GM) applies; nu_l >= (4/5) m g_l/Phi_l >= (4/5) m 2^l.  (GM) is designable (Lemma 2.1,
with the recursion order of part 1, 1.5): note that sigma = 0 is included, which only forces delta_l H_l >= g_l.
