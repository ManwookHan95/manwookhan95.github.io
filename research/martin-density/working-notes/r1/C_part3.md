
---

## 5. Excess profiles of a block

Fix one block and drop m. Phi = (Phi_k) positive with sum Phi_k^2 < 1, D = diag(Phi), |.| = gauge of
B := B_{l_1} + D(B_{l_2}) on l_1, N(v) = ||v||_inf + ||D v||_2 its dual norm on l_inf. Block excess at z != 0:
E(delta) := |z + delta| - |z| - w(delta) >= 0, w := J(z). Data (P, Q, Dg, P°, s, alpha, M, C) as in 1.3.

### 5.1 The two-variable formula

**Lemma 5.1 (exact local formula). [PROVED]** Let y in l_1, P a nonempty set of indices, Q its complement,
s in {+1,-1}^P. Put S := sum_{k in P} s_k y_k, Y := (sum_{k in Q} y_k^2/Phi_k^2)^{1/2} in [0, infinity],
F2 := sum_{k in P} Phi_k^2 in (0,1). Assume 0 < S < infinity and Y <= S. Define

  Lambda(S,Y) := [ S - sqrt(F2) sqrt(S^2 - (1-F2) Y^2) ] / (1 - F2),   lambda := Lambda(S,Y),
  rho_0 := (S/lambda - 1)/F2.

Then lambda > 0, rho_0 >= 0 and (S/lambda - 1)^2/F2 + Y^2/lambda^2 = 1. Moreover:
(a) if s_k y_k >= lambda rho_0 Phi_k^2 for every k in P, then |y| <= lambda;
(b) if |y_k| <= lambda rho_0 Phi_k^2 for every k in Q, then |y| >= lambda, attained by the dual vector
    w_k = M s_k (k in P), w_k = C y_k/(lambda Phi_k^2) (k in Q), M = rho_0/(1+rho_0), C = 1/(1+rho_0),
    for which N(w) = 1 and w(y) = lambda;
(c) if (a) and (b) hold, then |y| = Lambda(S_P(y), ||D^{-1} y_Q||_2) and J(y) = w.

Proof. Delta := S^2 - (1-F2)Y^2 >= F2 S^2 > 0 because Y <= S. The roots of
(1-F2) l^2 - 2 S l + (S^2 + F2 Y^2) = 0 are [S +- sqrt(F2 Delta)]/(1-F2); lambda is the smaller one, and this
equation is equivalent to (S - l)^2 + F2 Y^2 = F2 l^2, i.e. (S/l - 1)^2/F2 + Y^2/l^2 = 1. lambda > 0 since
sqrt(F2 Delta) <= sqrt(F2) S < S. rho_0 >= 0 iff lambda <= S iff S F2 <= sqrt(F2 Delta) iff F2 S^2 <= Delta
iff Y <= S.
(a) Define h in l_2 by h_k := rho_0 Phi_k s_k (k in P), h_k := y_k/(lambda Phi_k) (k in Q). Then
||h||_2^2 = rho_0^2 F2 + Y^2/lambda^2 = 1. Put alpha := y/lambda - D h: alpha_k = 0 on Q and
alpha_k = y_k/lambda - rho_0 Phi_k^2 s_k on P. Under (a), s_k alpha_k >= 0, so
||alpha||_1 = sum_P s_k alpha_k = S/lambda - rho_0 F2 = 1. Thus y/lambda = alpha + D h in B.
(b) ||w||_inf = M since |w_k| = C|y_k|/(lambda Phi_k^2) <= C rho_0 = M on Q. ||D w||_2^2 = M^2 F2 + C^2 Y^2/lambda^2
= C^2(rho_0^2 F2 + Y^2/lambda^2) = C^2, so N(w) = M + C = 1. Using S/lambda = 1 + rho_0 F2 and
Y^2/lambda^2 = 1 - rho_0^2 F2: w(y) = M S + C Y^2/lambda = C lambda (rho_0(1 + rho_0 F2) + 1 - rho_0^2 F2) = C lambda(1+rho_0) = lambda.
Hence |y| >= w(y)/N(w) = lambda.
(c) Both bounds; w attains, and the norming functional of y is unique (|.| is smooth). []

Consistency with the block-threshold lemma: at z with its own (P, s), (a) and (b) hold (alpha is the l_1 part,
h = D w/C), so the lemma reproduces |z|; one checks dLambda/dS = M and dLambda/dY = C Y/lambda.
**Numerical verification** (C_work/lam_check.py, six random instances, n = 6): |y| from an exact
peak-enumeration solver and Lambda agree to 12 digits; dLambda/dS = M and dLambda/dY = C Y/|y| to 6 digits.

Consequences. (i) Near z, as long as (a)-(b) persist, |.| depends on y only through the two numbers
(S_P(y), ||D^{-1} y_Q||): the peak coordinates enter only through their signed sum (the **peak simplex is
exactly flat**), the non-peaks through a Hilbert norm. (ii) If Q is empty (no non-peaks), Lambda(S,0) =
S/(1 + sqrt F2) is linear: the block is locally *affine*, all its curvature comes from structure changes
(peaks crossing the threshold). (iii) Second order (structure-preserving delta, Y > 0): with
h_0 := D^{-1} z_Q, sigma_1 := S_P(delta), sigma_2 := <h_0/Y, D^{-1} delta_Q>,

  E(delta) = (C/(2|z|)) ||P_{h_0 perp} D^{-1} delta_Q||^2 + (Lambda_SS/(2 Y^2)) (Y sigma_1 - S sigma_2)^2 + O(|.|^3),

because Lambda is 1-homogeneous (its Hessian is Lambda_SS/Y^2 times (Y,-S) tensor (Y,-S)) and
dLambda/dY = C Y/|z| multiplies the Hilbert excess ||h_0 + D^{-1}delta_Q|| - Y - sigma_2 = ||P_perp D^{-1}delta_Q||^2/(2Y) + O(.).

### 5.2 Upper bound by peak overshoots

**Lemma 5.2 (overshoot bound). [PROVED]** Let delta = mu z + delta' with mu > -1, delta' supported in P and
sum_{k in P} s_k delta'_k = 0. Then

  E(delta) <= 2 sum_{k in P} ( -s_k delta'_k - (1+mu)|z||alpha_k| )_+ <= 2 sum_{k in P} ( |delta'_k| - (1+mu)|z||alpha_k| )_+.

Proof. For a with s a = |a| (s = +-1) and any d: |a + d| = |a| + s d + 2(-s d - |a|)_+. Write
z + delta = [(1+mu)|z| alpha + delta'] + (1+mu)|z| D(Dw/C). The first bracket has l_1 norm
sum_P |(1+mu)|z|alpha_k + delta'_k| = (1+mu)|z| + sum_P s_k delta'_k + 2 sum_P(-s_k delta'_k - (1+mu)|z||alpha_k|)_+
= (1+mu)|z| + 2 ov; the second is (1+mu)|z| times an element of D(B_{l_2}). Hence
|z + delta| <= (1+mu)|z| + 2 ov, while w(delta) = mu|z| + M sum_P s_k delta'_k = mu|z|. []

In the Martín block: |z||alpha_k| = m Phi_k mu_k with the margin mu_k = |u_k(eta)| - theta Phi_k (1.3). For a
primal direction v with R v supported in P° (i.e. u_k(v) = 0 on Q and Dg) and zero peak sum,

  (5.1)  E(t R v) <= 2 m sum_{k in P°} Phi_k ( |t||u_k(v)| - mu_k )_+ <= 2 m |t| q(v) sum_{k in P°: mu_k < |t| q(v)} Phi_k .

### 5.3 Lower bounds

**Lemma 5.3 (single-coordinate Huber bound). [PROVED]** Let k in Q and sigma real with |w_k + sigma| <= M.
Put X := sigma Phi_k^2 w_k/C, Y_s := sigma^2 Phi_k^2/(2C). For delta in l_1 with |z|(1+X) + w(delta) + sigma delta_k >= 0:

  E(delta) >= [ sigma delta_k - |z| Y_s - (X + Y_s) w(delta) ] / (1 + X + Y_s).

Proof. N(w + sigma e_k) = M + (C^2 + 2 sigma Phi_k^2 w_k + sigma^2 Phi_k^2)^{1/2} <= 1 + X + Y_s
(using sqrt(C^2+u) <= C + u/(2C)), and (w + sigma e_k)(z) = |z| + sigma z_k = |z|(1 + X) because
z_k = |z| Phi_k^2 w_k/C on Q. Then |z + delta| >= (w + sigma e_k)(z + delta)/N(w + sigma e_k). []

Optimising sigma when w(delta) = 0: E(delta) >= H_k(delta_k)/(1 + O(Phi_k^2)) with the Huber function
H_k(d) = C d^2/(2|z| Phi_k^2) for |d| <= gamma^{+-}|z|Phi_k^2/C, and gamma^{+-}|d| - |z|(gamma^{+-})^2 Phi_k^2/(2C) beyond,
where gamma^+ = M - w_k (for d > 0), gamma^- = M + w_k (for d < 0). In the primal variable, delta_k = t m Phi_k u_k(v):
quadratic coefficient t^2 m^2 C u_k(v)^2/(2|z|), linear slope gamma m Phi_k |u_k(v)|, transition at
|t| = W_k := gamma |z| Phi_k/(C m |u_k(v)|).

**Lemma 5.4 (sign-flip bound). [PROVED]** For every set A of indices, N(w - 2 sum_{k in A} w_k e_k) = 1.
Consequently, for all delta in l_1,

  E(delta) >= 2 sum_k |w_k| ( -s_k delta_k - |z_k| )_+ ,  s_k := sign z_k = sign w_k.

Proof. Flipping signs of coordinates changes neither ||w||_inf nor ||D w||_2. With w^A := w - 2 sum_A w_k e_k:
|z + delta| >= w^A(z + delta) = |z| + w(delta) - 2 sum_A w_k (z_k + delta_k), and w_k z_k = |w_k||z_k|
(w_k and z_k have the same sign: on P by block-threshold, on Q by the formula for w_k). Take
A = {k : -s_k delta_k > |z_k|}. []

Lemmas 5.2 and 5.4 give two-sided control of the cost of a peak crossing to the opposite sign: between
2M(-s_k delta_k - |z_k|)_+ and 2(-s_k delta_k - |z||alpha_k|)_+; the thresholds differ by the Hilbert share
|z|Phi_k^2 M/C of |z_k| (in which the coordinate is not a peak any more but a non-peak with huge curvature).

### 5.4 Scale picture (HEURISTIC, used as guide only)
Along a primal direction v at a point with block data as above, at displacement t:
* non-peak k: Huber, quadratic (coefficient m^2 C u_k(v)^2/|z|) for |t| <~ W_k ~ Phi_k, linear beyond;
* peak k: zero until its delay T_k ~ mu_k/|u_k(v)| (simplex flatness), then like a non-peak with range 2M;
* rank-one terms from Lambda (peak sum vs Hilbert mass) and the Hilbert transverse term.
The linear contributions of the coordinates with Phi_k <~ |t| sum to O(t^2) ("persistent curvature" at depth
log(1/|t|)); this is the multiscale structure referred to in R5.
