---------------------------------------------------------------------------------------------------

## 5. Primal reading of the multi-scale issue (exact identity; interpretation HEURISTIC)

Let f' be in NA cap S_{p*}, attaining at x' in S_p, and let f in S_{p*}, eps := p*(f' - f). Put
delta_1 := 1 - f(x') in [0, eps], gamma := g(x') for g in C(f) (so gamma^2 <= p(x')^2 - f(x')^2 = 2 delta_1 - delta_1^2),
and the corrected direction g^nat := g - gamma f' (so g^nat(x') = 0, p*(g^nat - g) <= sqrt(2 eps)).
Every y in X is y = s x' + h with s = f'(y) and h in ker f'. Then:
* rho g^nat is a mate of f' iff  rho^2 g(h)^2 <= p(s x' + h)^2 - s^2  for all s in R, h in ker f'.   (5.1)
* g in C(f) gives, with G := g(h), phi := f(h) (|phi| <= eps p(h)):
  p(s x' + h)^2 - s^2 >= (s gamma + G)^2 + (s(1 - delta_1) + phi)^2 - s^2
                       = -kappa s^2 + 2 s (gamma G + (1 - delta_1) phi) + G^2 + phi^2,   kappa := 1 - gamma^2 - (1 - delta_1)^2 >= 0.  (5.2)
(5.2) is an identity-based lower bound (PROVED). It implies (5.1) only on the range of s where -kappa s^2 + 2 s(...) is
small compared with (1 - rho^2) G^2, i.e. |s| <~ (1 - rho^2)^{1/2} |G| / sqrt(kappa) with kappa <= 2 delta_1 <= 2 eps. For larger |s|,
writing h = s v, (5.1) is the condition rho^2 g(v)^2 <= 2 Delta'(v) (1 + o(1)) with Delta'(v) := p(x' + v) - f'(x' + v) >= 0, i.e. a
condition on the second-order behaviour of p at x' at the scales ||v|| <~ sqrt(eps). These scales are invisible from f.
This is the primal counterpart of Remark 4.9 (dual scales |t| <~ sqrt(eps)). (Interpretation: HEURISTIC; the identity and the
inequality (5.2) are exact.)

---------------------------------------------------------------------------------------------------

## 6. Beyond finite certificates: weighted certificates (Theorem W) and linear decompositions (Theorem L)

### 6.1 Box tails
For a block m and omega: N -> R vanishing on P_m, put for sigma > 0
  E_m(sigma; omega) := { k not in P_m : sigma |omega(k)| > gap_m(k)/2 },   T_m(sigma; omega) := sum_{k in E_m(sigma; omega)} lambda_{k,m} |omega(k)|.
E_m(sigma; omega) decreases as sigma decreases and its intersection over sigma > 0 is empty (gap_m(k) > 0 off P_m).

**Lemma 6.1 (o(sigma) box tails). PROVED.** T_m(sigma; omega) = o(sigma) as sigma -> 0 in each of the cases:
 (a) sum_k lambda_k omega(k)^2 / gap(k) < infinity ("gap-weighted");
 (b) omega is bounded and |omega(k)| <= K sqrt(gap(k)) whenever gap(k) <= gamma_0 (some K, gamma_0 > 0);
 (c) Preprint A's weighted directions: gap >= M/2 on supp omega and sum_k lambda_k omega(k)^2 < infinity (a special case of (a)).
*Proof.* (a) On E(sigma), lambda_k |omega(k)| < 2 sigma lambda_k omega(k)^2/gap(k); dominated convergence on the convergent series
over the shrinking sets E(sigma). (b) If sigma ||omega||_infinity < gamma_0/2, coordinates with gap > gamma_0 are not in E(sigma); if
gap(k) <= gamma_0 and k is in E(sigma) then gap(k)/2 < sigma K sqrt(gap(k)), so gap(k) < 4K^2 sigma^2 and |omega(k)| < 2K^2 sigma; hence
T(sigma) <= 2K^2 sigma sum_{gap(k) < 4 K^2 sigma^2} lambda_k = o(sigma). (c) sum lambda omega^2/gap <= (2/M) sum lambda omega^2. QED.

### 6.2 Theorem W (weighted certificates)
**Theorem 6.2 (W). PROVED.** Let
* b in l_1 with supp b in supp a, b(zhat) = 0 and flip-weight Fw(b) := sum_{j in supp a} b_j^2/|a_j| < infinity;
* for finitely many blocks m, omega_m: N -> R vanishing on P_m with sum_k lambda_{k,m}|omega_m(k)| < infinity and
  T_m(sigma; omega_m) = o(sigma).
Then D_m omega_m is in l_2, R_m* omega_m converges absolutely; put d_m := <D_m w_m, D_m omega_m>/C_m,
g := b + sum_m R_m*(omega_m - d_m w_m), H := max(h(b), max_m H_m(omega_m)). If g is in C(f) and H <= 1, then g is in cl Cert(f);
consequently g is recovered along every sequence f_n -> f (Corollary 4.11).

This strictly extends Preprint A, Thm 3.1 (which needs b = 0, one block, gap >= M/2 on supp omega and sum lambda omega^2 < infinity):
near-peak supports are allowed as long as sum lambda omega^2/gap < infinity, and flip-weighted base parts are allowed.

*Proof.* Sum_k Phi(k)^2 omega(k)^2 <= (sum_k lambda_k |omega(k)|)^2 (as Phi(k) <= lambda_k), so D omega is in l_2.
Truncations: for J in N let kappa_J := (b 1_{[1,J]})(zhat) (-> b(zhat) = 0), b_J := b 1_{[1,J]} - kappa_J a, omega_{m,J} := omega_m 1_{[1,J]},
c_J := (b_J, (omega_{m,J})). Each c_J is a finite certificate ((C1): supp b_J in supp a, ||b_J/a|| finite since only finitely many j <= J
plus a multiple of a, b_J(zhat) = kappa_J - kappa_J = 0; (C2) clear). g_{c_J} -> g and H(c_J) -> H.

*Claim (uniform expansion).* For every eta > 0 there are sigma_eta > 0 and J_eta such that for J >= J_eta and |sigma| <= sigma_eta:
  p*(f + sigma g_{c_J}) <= 1 + (sigma^2/2)(H(c_J) + eta).
*Proof of the claim.* Fix sigma != 0. For each active block m let K := supp omega_{m,J} \ E_m(|sigma|; omega_m) (kept coordinates),
omega' := omega_m 1_K, d' := <D w_m, D omega'>/C_m, W_m := (1 - d' sigma) w_m + sigma omega', and
Delta_m := R_m*(omega_{m,J} - omega') + (d' - d_{m,J}) R_m* w_m. Put A := a + sigma b_J + sigma sum_m Delta_m. Then
A + sum_m R_m* W_m (other blocks unchanged) = f + sigma g_{c_J}.
Blocks: on K, |sigma omega'(k)| <= gap(k)/2, and |d'| <= ||D omega_m||_2 so |d' sigma| <= 1/2 for small sigma. By Lemma 4.4(c),(d)-type
estimates, N_m(W_m) <= 1 + (sigma^2/2)(||h'_perp||^2/C_m)(1 + 2|d' sigma| M_m/C_m), h' := D omega', and
||h'_perp|| <= ||P-perp D omega_{m,J}|| + ||D omega_m 1_{E_m(|sigma|)}||, where the last term tends to 0 as sigma -> 0 uniformly in J.
So N_m(W_m) <= 1 + (sigma^2/2)(H_m(omega_{m,J}) + o(1)) uniformly in J.
Base: q*(A) <= q*(a + sigma b_J) + |sigma| sum_m q*(Delta_m), and, using q*(u_{k,m}) = 1 and Phi^2 <= lambda,
q*(Delta_m) <= T_m(|sigma|) + (M_m/C_m) sum_{E_m(|sigma|)} Phi(k)^2 |omega_m(k)| q*(R_m* w_m) <= T_m(|sigma|)(1 + M_m q*(R_m* w_m)/C_m) = o(|sigma|)
uniformly in J. By Lemma 4.3 (b_J(zhat) = 0), q*(a + sigma b_J) = 1 + Fl_{b_J}(sigma) + nu Psi(sigma U* b_J/nu). For |sigma kappa_J| <= 1/2,
-sign(a_j) sigma (b_J)_j - |a_j| <= |sigma||b_j| - |a_j|/2 for j <= J and < 0 for j > J; with (x - y/2)_+ <= x^2/(2y) 1[x > y/2]
(as x^2 - 2xy + y^2 >= 0) we get Fl_{b_J}(sigma) <= sigma^2 sum_{j : |b_j|/|a_j| > 1/(2|sigma|)} b_j^2/|a_j| = o(sigma^2) uniformly in J.
And nu Psi(...) <= (sigma^2/2) h(b_J)(1 + 2|sigma| ||U* b_J||/nu). Combining via Fact A proves the claim.
*Conclusion.* Fix rho in (0,1) and eta > 0 with rho(1 + 2 eta) <= 1. For J large, H(c_J) <= 1 + eta. For |t| <= t_1 := min(sigma_eta/rho, 2 sqrt(1-rho), 1):
p*(f + t rho g_{c_J}) <= 1 + (rho^2 t^2/2)(1 + 2 eta) <= 1 + rho t^2/2 <= 1 + t^2/2 - t^4/8 <= s(t). For |t| >= t_1, by Lemma 4.7,
p*(f + t rho g_{c_J}) <= s(rho t) + rho |t| p*(g_{c_J} - g) <= s(t) as soon as p*(g_{c_J} - g) <= (1 - rho^2) t_1/3.
Hence for J large rho g_{c_J} is in C(f) with H(rho c_J) = rho^2 H(c_J) <= 1, i.e. rho g_{c_J} in Cert(f); letting J -> infinity and
rho -> 1 gives g in cl Cert(f). QED.

### 6.3 Linear decompositions (Theorem L)
**Definition.** A *locally admissible linear decomposition* of g in X* is a representation g = b + sum_{m in F} R_m* Omega_m
(F finite, b in l_1, Omega_m in l_infinity) together with tau_0 > 0 such that for all |tau| <= tau_0:
  q*(a + tau b) <= s(tau)  and  N_m(w_m + tau Omega_m) <= s(tau) for m in F.
(Equivalently, by Fact A, the linear path f + tau g = (a + tau b) + L*(w + tau Omega) is admissible at level s(tau).)

**Lemma 6.3 (structure). PROVED.** If (b, Omega) is a locally admissible linear decomposition, then
 (i) supp b is contained in supp a, b(zhat) = 0, and h(b) <= 1;
 (ii) for each m in F there are mu_m in R and a bounded omega_m vanishing on P_m with Omega_m = omega_m - d_m w_m, where
      d_m = -mu_m/M_m = <D w_m, D omega_m>/C_m, and
        |omega_m(k)| <= sqrt(2 gap_m(k)) + |mu_m| gap_m(k)/M_m   whenever gap_m(k) <= tau_0^2/2;
 (iii) H_m(omega_m) <= 1 for each m.
In particular each omega_m has o(sigma) box tails (Lemma 6.1(b)).

*Proof.* (i) phi(tau) := q*(a + tau b) is convex, phi(0) = 1, phi(tau) <= 1 + tau^2/2 on |tau| <= tau_0; hence its one-sided derivatives
satisfy phi'(0+) <= 0 <= phi'(0-) <= phi'(0+), so both vanish. By dominated convergence,
phi'(0+/-) = sum_{supp a} sign(a_j) b_j +/- sum_{j not in supp a} |b_j| + <U*b, e>. Hence sum_{j not in supp a}|b_j| = 0 and b(zhat) = 0.
By the identity of Lemma 4.3 (Fl_b >= 0) and the lower bound for Psi (valid whenever |tau| beta/nu <= 1/2, flips or not),
(tau^2/2) h(b)/(1 + |tau| beta/nu) <= phi(tau) - 1 <= tau^2/2, so h(b) <= 1.
(ii) Fix m; psi(tau) := ||w + tau Omega||_infinity and chi(tau) := ||D(w + tau Omega)||_2 are convex, chi is differentiable at 0 with
chi'(0) = <D Omega, D w>/C. As in (i), N = psi + chi is differentiable at 0 with N'(0) = 0, so psi'(0) exists and equals
mu := -chi'(0). For k in P: psi(tau) >= M + tau sigma_k Omega(k), which for tau -> 0+ and tau -> 0- gives sigma_k Omega(k) = mu.
Next psi(tau) <= s(tau) - chi(tau) <= 1 + tau^2/2 - C - tau chi'(0) = M + tau mu + tau^2/2 (convexity of chi). For k not in P with
w(k) != 0 and sigma'_k := sign w(k): tau(sigma'_k Omega(k) - mu) <= gap(k) + tau^2/2 for |tau| <= tau_0; choosing
tau = +/- min(tau_0, sqrt(2 gap(k))) gives |sigma'_k Omega(k) - mu| <= sqrt(2 gap(k)) when gap(k) <= tau_0^2/2.
Put d := -mu/M and omega := Omega + d w. On P, omega(k) = mu sigma_k - mu sigma_k = 0. Off P,
omega(k) = sigma'_k[(sigma'_k Omega(k) - mu) + mu gap(k)/M], giving the bound (and omega = Omega where w(k) = 0).
Finally mu = -<D Omega, D w>/C = -(<D omega, D w> - d C^2)/C and mu = -d M give d(M + C) = <D omega, Dw>/C, i.e. d = <Dw, D omega>/C.
(iii) w + tau Omega = (1 - d tau) w + tau omega, so Lemma 4.4(b) gives
1 + tau^2 ||h_perp||^2/(sqrt(Y^2 + tau^2||h_perp||^2) + Y) <= 1 + tau^2/2; letting tau -> 0 (Y -> C) gives ||h_perp||^2 <= C, i.e. H_m <= 1. QED.

**Lemma 6.4 (monotone truncation of base parts). PROVED (numerically checked).** Let b in l_1, supp b in supp a, b(zhat) = 0;
let G be any subset of supp a, b^G := b 1_G, kappa := b^G(zhat), c := b^G - kappa a (so c(zhat) = 0). If
|sigma| <= min( 1/(2|kappa|), nu/(2||U|| max(||c||_1, ||b||_1)) ) then
  q*(a + sigma c) <= q*(a + sigma b) + sigma^2 [ 4|kappa| ||b||_1 + (4||U||^2/nu) max(||c||_1, ||b||_1) ||c - b||_1 ].
*Proof.* By Lemma 4.3 the first-order terms vanish and q*(a + sigma c) - q*(a + sigma b) = [Fl_c - Fl_b](sigma) + nu[Psi(sigma U*c/nu) - Psi(sigma U*b/nu)].
For j in G, with x_j := -sign(a_j) sigma b_j - |a_j|: -sign(a_j) sigma c_j - |a_j| = x_j + sigma kappa |a_j| <= x_j + |sigma kappa||a_j|, and
(x + e)_+ <= x_+ + e 1[x > -e]; on {x_j > -|sigma kappa||a_j|} we have |sigma b_j| >= |a_j|(1 - |sigma kappa|) >= |a_j|/2.
For j in supp a \ G: -sign(a_j) sigma c_j - |a_j| = (sigma kappa - 1)|a_j| < 0. Hence Fl_c(sigma) <= Fl_b(sigma) + 4 sigma^2 |kappa| ||b||_1
(removing coordinates only removes nonnegative flip terms). The Hilbert difference is bounded by Lemma 4.3. QED.
(Key point: discarding base coordinates never increases sign-flip costs, so no flip-weight is needed.)

**Theorem 6.5 (L). PROVED.** If g is in C(f) and admits a locally admissible linear decomposition, then g is in cl Cert(f);
consequently g is recovered along every sequence f_n -> f.

*Proof.* Let (b, Omega) be the decomposition and (omega_m, d_m) as in Lemma 6.3. For t in (0, 1) choose J_t -> infinity (as t -> 0) and
  G_t := supp a cap [1, J_t] cap { j : |b_j| <= |a_j|/(2t) },  b^{(t)} := b 1_{G_t},  kappa_t := b^{(t)}(zhat),  b_t := b^{(t)} - kappa_t a,
  omega_{m,t} := omega_m 1_{[1, J_t]},  c_t := (b_t, (omega_{m,t})).
c_t is a finite certificate (||b_t/a|| <= 1/(2t) + |kappa_t|). As t -> 0: b^{(t)} -> b in l_1, kappa_t -> b(zhat) = 0, b_t -> b,
g_{c_t} -> g, and H(c_t) -> max(h(b), H_m(omega_m)) <= 1 (Lemma 6.3).
*Claim.* For every eta > 0 there are sigma_eta, t_eta > 0 such that for 0 < t <= t_eta and |sigma| <= sigma_eta:
  p*(f + sigma g_{c_t}) <= max( q*(a + sigma b) + eta sigma^2, 1 + (sigma^2/2)(max_m H_m(omega_{m,t}) + eta) ).
Proof: same decomposition as in the proof of Theorem 6.2 (discarding, at scale sigma, the block coordinates in E_m(|sigma|; omega_m) into
the base). Blocks: as there, using Lemma 6.1(b) for the box tails of omega_m. Base:
q*(a + sigma b_t + sigma sum Delta_m) <= q*(a + sigma b_t) + o(sigma^2) (uniformly in t), and by Lemma 6.4 (with G = G_t)
q*(a + sigma b_t) <= q*(a + sigma b) + sigma^2 [4|kappa_t| ||b||_1 + (4||U||^2/nu) max(||b_t||,||b||) ||b_t - b||_1] = q*(a + sigma b) + o_t(1) sigma^2.
*Conclusion.* Fix rho in (0,1); pick eta with eta <= (1 - rho^2)/(3 rho^2) and rho(1 + 2 eta) <= 1. For |tau| <= tau_1 small (also rho|tau| <= tau_0):
q*(a + rho tau b) + eta rho^2 tau^2 <= s(rho tau) + (1 - rho^2) tau^2/3 <= s(tau) (Lemma 4.7), and
1 + (rho^2 tau^2/2)(max_m H_m(omega_{m,t}) + eta) <= 1 + rho tau^2/2 <= s(tau) for t small. So p*(f + tau rho g_{c_t}) <= s(tau) for |tau| <= tau_1,
and for |tau| >= tau_1 by the slack (Lemma 4.7) once p*(g_{c_t} - g) is small. Thus rho g_{c_t} lies in Cert(f) for small t, and rho g_{c_t} -> rho g. QED.

**Corollary 6.6. PROVED.** The closed convex hull of all mates covered by Theorems 6.2 and 6.5 (and by Corollary 4.12) is contained in
cl Cert(f) and is recovered, simultaneously, along every sequence f_n -> f in S_{p*}.

Remarks 6.7.
* Theorem 6.5 covers: base directions b in l_1 with infinitely many sign flips (relevant when a is not in c_00, briefing R7(iii)), as long
  as the flip cost is paid inside the budget s(tau); bounded block parts using near-peak coordinates (the decay
  |omega(k)| <= sqrt(2 gap(k)) + K gap(k) is then automatic). Theorem 6.2 covers unbounded block parts (weighted directions) with
  near-peak support (part of R7(iv)).
* The unbounded weighted examples of Preprint A (Remark "Non-attaining examples", no bounded lift) are covered by Theorem 6.2; by
  Corollary 4.11 they are recovered along EVERY sequence, simultaneously with all certificate mates. In particular the derivative
  blow-up of Preprint A, Prop. 3.3, is no obstruction to recovery.
* What is NOT covered: mates whose admissible decompositions are not (regularized-)linear in t, i.e. whose decomposition must change
  qualitatively with the scale t. See §7.

