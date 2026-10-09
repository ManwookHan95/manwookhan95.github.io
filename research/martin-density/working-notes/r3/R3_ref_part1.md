# R3 referee, part 1: Theorem EC, room lemma, Proposition Z (line-by-line check)

Setting checked: finite block set I (p_N), canonical base, admissible T = Lemma B's conclusion. Imports used by R3 and
re-checked here: A Facts A-E, Def 4.1, Lemma 4.4, Prop 4.5; N2 Lemma 1.5.

## 1.1 Theorem EC. VERDICT: CORRECT (PROVED), with two wording corrections.
Step 1 (indices). Uses only (T2) "every tail of (u_{k,m0})_k is q*-dense in S_{q*}". This follows from Lemma B:
a dense subset of a sphere of dimension >= 1 minus finitely many points is still dense (no isolated points), and
S_Y is dense in S_{q*} because Y is dense. ||.||_1 <= q*. OK. NOTE: only an UPPER bound Phi(k) <= Phibar_n on the
depth is obtained; the actual depth of k_{n,i} is chosen by T (Lemma B allows arbitrarily slow approximation), so
"at any prescribed depth" in the task summary must read "at least as fine as any prescribed depth". Nothing in (b)-(d)
needs a lower bound on the depth; the radius bound in (d) is in terms of the actual lambda_{k_{n,i}}.
Step 2. (iv) gives d beta eps <= 1/(8(2+||U||)) <= 1/16; Neumann series: ||A^{-1}|| <= beta/(1-1/16) <= 2 beta. OK.
Step 3. b(x'_N) = b(z'_N) + <U*b, e'_N> -> b(zhat): dominated convergence (|z'_N| <= 1) and e'_N -> e (U*a'_N -> U*a,
nu > 0). N(n) is chosen AFTER the k_{n,i}; it does not depend on them. (3b) puts G_n outside supp a'_{N(n)}. OK.
Step 4. ||eta'|| <= d ||s||_inf <= 2 d beta (max|b(x')| + eps(1+||U||)) <= min/8 + min/4. Row/column convention of
A = (u_{k_i}(eta_l))_{i,l} is consistent with u_{k_i}(x' + eta') = v(i) + (A s)(i) = 0. OK.
Step 5. q(x'') <= 1 because x'' = z'' + U e' with ||z''||_inf <= 1, ||e'|| = 1; a'(x'') = ||a'||_1 + ||U*a'|| = 1; so
grad q(x'') = a' (q Gateaux smooth) and f'' = grad p(x'') is NA (Fact D). z'' -> z coordinatewise; N2 Lemma 1.5
(re-checked: L compact => L x''_n -> L** zhat in norm; J_V norm-to-weak* continuous at L** zhat since all block
components are nonzero; L* weak*-to-norm continuous on bounded sets) gives f''_n -> f in norm. OK.
Step 6. At a coordinate with zeta''(k) = 0: if k were a peak, zeta''(k)/|zeta''| = alpha''(k) + Phi^2 w''(k)/C'' with
alpha''(k) w''(k) >= 0 and |w''(k)| = M'' > 0 has modulus >= Phi^2 M''/C'' > 0, contradiction. So k is a strict
non-peak, w''(k) = 0, gap M'', d''(e_k) = 0. OK.
Step 7. d = 0, b = 0, so kappa = 0, H = sum (Phi_i c_i/lambda_i)^2/C'' = ||c||_2^2/(m0^2 C''), only the box radius
M''/(2||omega||_inf) is finite. Lemma 4.4(c),(d) applies (|s omega(k)| <= M''/2 = gap/2; other peaks keep the sup at M'').
Prop 4.5 gives the bound. OK.
Hidden assumptions on T: none beyond Lemma B. Weak* vs norm: only coordinatewise convergence of z''_n is used, and
norm convergence of f''_n comes from compactness of L, U*. I = N is NOT covered (Fact B/E and strict convexity of p**
are only available for finite I; R3 says so).
Remark 2.2(2) (linear-algebra form of (ii)) checked: suitable eta's exist iff the restrictions of the b_i to
Z := {eta in R^G : phi(eta) = 0, phi in Pi} are linearly independent iff no nontrivial sum mu_i b_i|_G lies in
span{phi|_G}. CORRECT. (Consequence used against 4.5 in part 3: a protected functional whose G-restriction lies in
span{b_i|_G} removes a target direction.)

## 1.2 Room lemma. VERDICT: CORRECT (PROVED).
r >= M'' lambda_gen/(2 kappa s) >= s iff s^2 <= M'' lambda_gen/(2 kappa); H <= d kappa^2 s^2/(m0^2 C''). OK.
Reading check. The lemma concerns a FIXED vector of size kappa*s carried at all |t| <= s; its quadratic cost is
t^2 O(kappa^2 s^2) = o(t^2). Two variants matter in R3 and are both fine:
 (a) frozen error of size kappa*lambda_b (independent of t), carried up to tau_F = M'' lambda_gen/(2 beta kappa lambda_b);
 (b) a t-dependent error y_t with ||y_t|| <= kappa |t| (absolute size kappa t^2), carried up to T_n = sqrt(M'' lambda_gen/(2 beta kappa)).
 A t-dependent error of RELATIVE size O(1) (||y_t|| ~ kappa_0, absolute kappa_0 |t|) would have Hilbert coefficient
 ~ d beta^2 kappa_0^2/(m0^2 C''), NOT small: EC carries O(scale) errors, not O(1) components. R3 states this correctly
 (implant scale gap concerns O(1) components). CONFIRMED by the computation of part 3 (boundary-layer errors in E's
 design are of type (a), size K lambda_b, so they are carriable).
The "depth" in the reading must be the ACTUAL depth min_i lambda_{k_{n,i}}, which T chooses; this is why the boundary
must be chosen after the generic coordinates (R3's quantifier order). Correctly stated in R3 4.3.

## 1.3 Proposition Z. VERDICT: CORRECT (PROVED; hypothesis "J infinite" is needed and used).
Checked: y_{n,i}(zhat) = g(zhat) + r_n(zhat_j - zhat_j a(zhat)) = 0; q*(e*_j - zhat_j a) <= 1 + ||U|| + |zhat_j| <= 2(1+||U||);
q*(y) in [q*(g)/2, 3q*(g)/2]; y_i(e_{j_l}) = g_{j_l} + r_n delta_{il} because a_{j_l} = 0 (j_l notin F);
||(r I + 1 gamma^T)^{-1}|| <= 2/r since ||1 gamma^T||_{inf->inf} = sum|gamma_l| <= r/2; beta <= 4q*(g)/r;
||sum c_i b_i - g||_1 <= (r_n/d_n) sum_i (1 + |zhat_{j_i}| ||a||_1) <= r_n(2+||U||); H <= 4 q*(g)^2/(d_n m0^2 C''_n) -> 0
because C''_n -> C_{m0} > 0. kappa = 0, radius > 0 (but radius -> 0 extremely fast, which is the point of 3.2).
3.2(a) is a correct but definitional consequence: any K_0(f) closed under limits of certificate directions with
limsup H <= 1 contains xi-perp (J infinite), hence contains C(f) (every mate vanishes at xi, A Remark 2.3).
Remark (finite J): with d fixed one gets H <= 4q*(g)^2/(d m0^2 C) + o(1); not "trivial closure" then. Fine as stated.
Adversarial check: J can be finite (|z_j| = 1 on a cofinite set is allowed for non-NA f in l_inf), so Prop Z genuinely
needs its hypothesis; 2.2(5) (pulling contacts inside) is SKETCH and would have to be re-checked against the base
budget (a pulled-in contact j in K with a_j = 0 is free, but its sign-constraint role in other engineering is lost).
