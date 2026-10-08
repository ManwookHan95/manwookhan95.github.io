### 6.4 The averaging ("ladder") theorem: O(t) remainders suffice

The following result is the strongest positive tool in these notes. It replaces the o(t)-type hypotheses of Theorems 6.2 and 6.5
by O(t), needs no monotonicity, and only uses convexity of p*.

**Theorem 6.8 (averaging over scales). PROVED.** Let g be in C(f). Suppose there are constants c_0 > 0, kappa_0 < infinity, K < infinity,
t_* > 0 and a function eta(t) -> 0 (t -> 0+) such that for every t in (0, t_*] there is a finite certificate c_t at f with
 (i) H(c_t) <= 1 + eta(t),   (ii) r(c_t) >= c_0 t,   (iii) kappa(c_t) <= kappa_0,   (iv) p*(g - g_{c_t}) <= K t.
Then g lies in cl Cert(f); consequently g is recovered along every sequence f_n -> f in S_{p*} (Corollary 4.11).

*Proof.* Fix rho in (0,1). Choose s_0 in (0, 1] and eta_0 > 0 with
  rho^2 (1 + eta_0)(1 + kappa_0 s_0) <= (1 + rho^2)/2   and   s_0^2 <= 1 - rho^2,
then an integer n >= 24 rho^2 K /(c_0 (1 - rho^2)), and finally t_1 in (0, t_*] so small that eta(t) <= eta_0 for t <= t_1,
t_1 <= rho s_0/(2 c_0), and 2 rho K t_1/n <= (1 - rho^2) s_0/3. Put t_i := t_1 2^{1-i} (i = 1, ..., n) and
  c := (1/n) sum_{i=1}^n c_{t_i}   (a finite certificate; g_c = (1/n) sum_i g_{c_{t_i}} by linearity, Lemma 4.2).
For each i and real s we have two bounds:
 (A) if rho|s| <= r(c_{t_i}) (in particular if rho|s| <= c_0 t_i): p*(f + s rho g_{c_{t_i}}) <= 1 + (rho^2 s^2/2)(1 + eta_0)(1 + kappa_0 rho |s|)
     (Proposition 4.5 and (i), (iii));
 (B) always: p*(f + s rho g_{c_{t_i}}) <= p*(f + s rho g) + rho|s| p*(g - g_{c_{t_i}}) <= s(rho s) + rho |s| K t_i (g in C(f) and (iv)).
By convexity of p*, p*(f + s rho g_c) <= (1/n) sum_i p*(f + s rho g_{c_{t_i}}).
*Case |s| <= s_0.* Use (A) for I_c := {i : c_0 t_i >= rho|s|} and (B) for the rest I_f. As the t_i are geometric with ratio 1/2,
sum_{i in I_f} t_i < 2 rho |s|/c_0. Hence
  p*(f + s rho g_c) <= max{ 1 + (rho^2 s^2/2)(1 + eta_0)(1 + kappa_0 s_0),  s(rho s) } + (rho |s| K/n)(2 rho |s|/c_0).
The last term is Q s^2 with Q := 2 rho^2 K/(c_0 n) <= (1 - rho^2)/12. Now
1 + (rho^2 s^2/2)(1 + eta_0)(1 + kappa_0 s_0) + Q s^2 <= 1 + (s^2/2)((1 + rho^2)/2 + (1 - rho^2)/6) <= 1 + (s^2/2)(1 - (1 - rho^2)/4) <= 1 + s^2/2 - s^4/8 <= s(s)
(using s^2 <= s_0^2 <= 1 - rho^2), and s(rho s) + Q s^2 <= s(s) by Lemma 4.7 (s(s) - s(rho s) >= (1 - rho^2) s^2/3 for |s| <= 1).
*Case |s| >= s_0.* Since c_0 t_i <= c_0 t_1 <= rho s_0/2 < rho|s|, every i uses (B):
p*(f + s rho g_c) <= s(rho s) + rho|s| K (1/n) sum_i t_i <= s(rho s) + 2 rho K t_1 |s|/n <= s(rho s) + (1 - rho^2) s_0 |s|/3 <= s(s),
because by Lemma 4.7, s(s) - s(rho s) >= (1 - rho^2) min(s^2, |s|)/3 >= (1 - rho^2) s_0 |s|/3 for |s| >= s_0.
Thus rho g_c lies in C(f). By convexity of H, H(rho c) = rho^2 H(c) <= rho^2 (1 + eta_0) <= (1 + rho^2)/2 <= 1, so rho g_c lies in Cert(f).
Finally p*(rho g_c - rho g) <= (rho/n) sum_i K t_i <= 2 rho K t_1/n, which tends to 0 as t_1 -> 0. Hence rho g is in cl Cert(f) for every
rho < 1, and so is g. QED.

The mechanism: the averaged certificate has, at each scale s, only O(1) of its n components "too fine" for s (their remainders
are O(s) each), while the coarse components are certified by their own expansions; the remainders of the fine components are
geometrically summable, so they cost O(s^2/n).

**Corollary 6.9 (decomposition form of the hypothesis). PROVED.** Let g be in C(f). Suppose that for every small t > 0 there are a
finite certificate c_t = (b_t, omega_t) with r(c_t) >= c_0 t and kappa(c_t) <= kappa_0, and e_t := g - g_{c_t} with p*(e_t) <= K t, such that for
tau = t or for tau = -t (either sign, possibly depending on t) the decomposition
  f + tau g = (a + tau b_t + tau e_t) + sum_m R_m*( (1 - d_{t,m} tau) w_m + tau omega_{t,m} )
is admissible at level s(tau) + o(tau^2). Then H(c_t) <= 1 + o(1), so Theorem 6.8 applies and g is in cl Cert(f).
*Proof.* Blocks: Lemma 4.4(b) (|d_{t,m}| <= kappa_0 C_m/(2M_m), so 1 - d tau > 0 and Y > 0 for small tau) gives
X^2/(sqrt(Y^2 + X^2) + Y) <= tau^2/2 + o(tau^2) with X := |tau| ||h_perp||; hence X -> 0 and ||h_perp||^2 <= (Y + X/2)(1 + o(1)) = C_m + o(1),
i.e. H_m(omega_{t,m}) <= 1 + o(1). Base: B := b_t + e_t satisfies B(zhat) = 0 because g(xi) = 0 and g_{c_t}(xi) = 0 (Lemma 4.2), so by Lemma 7.2
(flip and kink terms are >= 0) q*(a + tau B) - 1 >= nu Psi(tau U*B/nu) >= (tau^2/2) h(B)/(1 + |tau| ||U*B||/nu); with ||U*B|| bounded this gives
h(B) <= 1 + o(1). Since sqrt(h) is a seminorm and h(e_t) <= ||U||^2 ||e_t||_1^2/nu = O(t^2), sqrt(h(b_t)) <= sqrt(h(B)) + sqrt(h(e_t)) <= 1 + o(1). QED.

**Corollary 6.10 (applications). PROVED.**
 (a) *Theorem W with O(sigma) tails.* Theorem 6.2 remains true if T_m(sigma; omega_m) = o(sigma) is weakened to T_m(sigma; omega_m) = O(sigma), and
     the flip-weight condition on b is weakened to sum_{j : |b_j| > |a_j|/(2t)} |b_j| = O(t). In particular the "borderline" case of §7.4
     (box tails of exact order sigma) is IN cl Cert(f).
 (b) *Theorem L* follows again (with the base truncation error O(t) automatic: for a locally admissible linear decomposition,
     Fl_b(t) + Fl_b(-t) = 2 sum_j (|t||b_j| - |a_j|)_+ <= t^2 implies sum_{j : |a_j| <= |t||b_j|/2} |b_j| <= |t|).
 (c) *Cross mates with scale-dense rates are not a source of defect.* Let g = g_{c^0} + c v with c^0 a finite certificate, v in S_{q*},
     v(xi) = 0, and suppose some block m has off-peak coordinates k_1 < k_2 < ... with gap_m(k_i) >= gamma_0 > 0,
     ||u_{k_i,m} - v|| <= K' lambda_{k_i,m}, and lambda_{k_{i+1},m} >= beta lambda_{k_i,m} for some beta in (0,1). If g is in C(f) and the
     certificates c_t := c^0 + (0, (c/lambda_{k(t),m}) e_{k(t)} in block m), where k(t) is the first k_i with lambda_{k_i,m} <= t, satisfy
     H(c_t) <= 1 + o(1) (e.g. via Corollary 6.9), then g is in cl Cert(f).
*Proof.* (a) Truncate at scale t: b^{(t)} := b 1_{G_t} - kappa_t a with G_t := {|b_j| <= |a_j|/(2t)} cap [1,J_t], kappa_t := (b 1_{G_t})(zhat), and omega_{m,t} := omega_m 1_{{k <= J_t, |t omega_m(k)| <= gap_m(k)/2}}
with J_t large. Then r(c_t) >= min(t, ...) (radius at least t from the base ratio 1/(2t) + |kappa_t| and from the box condition),
kappa(c_t) is bounded, p*(g - g_{c_t}) <= C(sum_{|b_j| > |a_j|/(2t)}|b_j| + T_m(t) + tails) = O(t), and H(c_t) -> H <= 1. Apply Theorem 6.8.
(b) As in (a), with Lemma 6.3 (bounded omega with sqrt(gap) decay has o(sigma) tails) and, for the base, the bound
sum_{|a_j| <= 2t|b_j|} |b_j| <= 4t obtained from the displayed flip inequality at scale 4t. (c) r(c_t) >= min(r(c^0), gamma_0 lambda_{k(t)}/(2|c|), ...) >= c_1 t because lambda_{k(t)} >= beta t; the remainder is
c(v - u_{k(t)}) + d_{k(t)} R_m* w_m with ||v - u_{k(t)}|| <= K' t and |d_{k(t)}| = |c| Phi_m(k(t)) |w_m(k(t))|/(m C_m) = O(t); kappa(c_t) is bounded. Apply Theorem 6.8. QED.

**Consequence for the defect.** (PROVED, as the contrapositive of Theorem 6.8 and Corollary 6.9.) If g is in
Def(f) = C(f) \ cl Cert(f), then for all constants c_0, kappa_0, K and every eta(t) -> 0 there are arbitrarily small scales t at which no
finite certificate c with r(c) >= c_0 t, kappa(c) <= kappa_0 and H(c) <= 1 + eta(t) satisfies p*(g - g_c) <= K t; in decomposition terms, on BOTH
sides tau = +t and tau = -t the admissible decompositions at such scales are not "certificate + O(t) remainder in the base".
(HEURISTIC continuation.) By Corollary 7.3 the parts of size >> t must then be carried by the one-sided resources (N1), (N2) listed
in §7.2, on both sides, with different carriers representing the same component of g up to O(t): approximate linear relations,
at their own scales, between base vectors e_j* and block vectors u_{k,m}, or among block vectors.

