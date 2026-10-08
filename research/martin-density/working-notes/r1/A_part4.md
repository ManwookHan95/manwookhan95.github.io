---------------------------------------------------------------------------------------------------

## 7. Structure of general mates; where the defect C(f) \ cl Cert(f) can live

### 7.1 Excess bookkeeping
For A in X* and W = (W_m) in V* put
  E_q(A) := q*(A) - A(zhat) >= 0,   e_m(W_m) := N_m(W_m) - <W_m, zeta_m>/|zeta_m|_m >= 0,   pi_m := |zeta_m|_m/(1 - q_0)  (sum_m pi_m = 1).

**Lemma 7.1 (budget). PROVED.** If g is in C(f) and f + t g = A_t + L* W_t with q*(A_t) <= s(t), ||W_t||_{V*} <= s(t), then
  q_0 E_q(A_t) + (1 - q_0) sum_m pi_m e_m(W_{t,m}) <= s(t) - 1 <= t^2/2.
*Proof.* q_0 E_q(A_t) <= q_0 s(t) - A_t(xi) and (1 - q_0) pi_m e_m <= |zeta_m| s(t) - <W_{t,m}, zeta_m>. Summing,
the right sides add up to s(t) - (A_t(xi) + <W_t, L**xi>) = s(t) - (f + t g)(xi) = s(t) - 1, since g(xi) = 0. QED.

**Lemma 7.2 (exact excess formulas). PROVED.** For B in l_1 and real t:
  E_q(a + tB) = Fl_B(t) + sum_{j not in supp a} ( |t B_j| - z_j t B_j ) + nu Psi(t U*B/nu),
with Fl_B(t) := sum_{j in supp a} 2(-sign(a_j) t B_j - |a_j|)_+. For W_m = w_m + t Omega (one block, indices dropped):
  e_m(W) = sum_{k in P} |alpha_k| ( ||W||_infinity - sigma_k W(k) ) + t^2 ||P-perp D Omega||^2 / ( ||D W|| + <D W, D w>/C ).
*Proof.* First: expand ||a + tB||_1 coordinatewise as in Lemma 4.3 and subtract (a + tB)(zhat) = 1 + tB(zhat). Second: by Fact C,
<W, zeta>/|zeta| = <W, alpha> + <D W, D w>/C, and ||W||_infinity - <W, alpha> = sum_k |alpha_k|(||W||_infinity - sigma_k W(k)) because ||alpha||_1 = 1 and
alpha_k = |alpha_k| sigma_k; the Hilbert part is (||DW||^2 - <DW, Dw/C>^2)/(||DW|| + <DW, Dw/C>) and P-perp D W = t P-perp D Omega. QED.

**Corollary 7.3 (what an admissible decomposition can afford). PROVED.** With B_t := (A_t - a)/t, Omega_t := (W_t - w)/t:
 (a) sum_{j not in supp a} (1 - z_j sign(t B_t(j))) |t B_t(j)| <= t^2/(2 q_0): base mass outside supp a is free (at first order) only at
     contact coordinates K := {j not in supp a : |z_j| = 1}, and only with sign(t B_t(j)) = z_j; elsewhere it costs (1 - |z_j|)|t B_t(j)|.
 (b) sum_{k in P_m} |alpha_{m,k}| ( ||W_{t,m}||_infinity - sigma_k W_{t,m}(k) ) <= t^2/(2(1 - q_0) pi_m): deviations of a peak coordinate below the
     sup level cost at first order, weighted by alpha_{m,k}; for far peaks alpha_{m,k} ~ lambda_{k,m} |u_{k,m}(xi)|/|zeta_m| is tiny, so far peaks
     can deviate by O(1) at scale t when lambda_{k,m}|u_{k,m}(xi)| <~ |t|.
 (c) ||P-perp D_m Omega_{t,m}||_2^2 <= s(t)/((1 - q_0) pi_m) (bounded), while off-peak coordinates only satisfy the box
     |w_m(k) + t Omega_{t,m}(k)| <= ||W_{t,m}||_infinity, so Omega_{t,m}(k) may be of size up to ~ 2/|t| (weighted-direction phenomenon).
*Proof.* Lemma 7.1, Lemma 7.2, nonnegativity of each term, and ||D W|| + <DW, Dw>/C <= 2 s(t). QED.

### 7.2 Classification of the possible defect (statement HEURISTIC; the dichotomy results 7.4-7.5 and §6.4 are PROVED)
By Theorems 6.2, 6.5 and especially Theorem 6.8 / Corollary 6.9, a mate lies in cl Cert(f) as soon as, on ONE side (tau = +t or
tau = -t) and at all small scales t, it admits an admissible decomposition of the form "finite certificate of radius >~ t
and bounded kappa + remainder of norm O(t) placed in the base" (Corollary 6.9). Hence a mate in the defect Def(f) = C(f) \ cl Cert(f) must, on BOTH sides and at arbitrarily small
scales, carry a part of size >> t through first-order-cheap resources that are not certificates. By Corollary 7.3 these are:
 (N1) base mass at contact coordinates j in K (one-sided: allowed sign z_j sign(tau)), at near-contact coordinates (|z_j| -> 1),
      or at coordinates j in supp a with |a_j| small compared with |tau B(j)| (no first-order cost only when sign(tau B(j)) = sign a_j);
 (N2) block coordinates used beyond their two-sided capacity: deviations at weak peaks (peaks with |u_{k,m}(xi)| small; the
      first-order cost is alpha_k dev_k ~ lambda_k |u_{k,m}(xi)| dev_k/|zeta_m|, so at scale t only peaks with |u_{k,m}(xi)| <~ |t| are usable),
      and off-peak coordinates pushed toward the opposite sign by more than gap_m(k) (allowed by the box up to M + |w_m(k)|, with
      only a Hilbert cost ~ Phi_m(k)^2 (2M)^2). Both are one-sided, and both can carry mass ~ lambda_k/|t|, i.e. O(1) in total, from
      coordinates with Phi_m(k) <~ |t|. Peaks with |u_{k,m}(xi)| >= c_1 > 0 only carry O(t/c_1) at scale t (Corollary 7.3(b)).
      HEURISTIC remark ("resonance"): such carriers can represent a FIXED component c v of g at all small scales only if u_{k,m} -> v at
      rate O(Phi_m(k)) along scale-dense sequences AND the carriers stay near the peak threshold, i.e. (u_{k,m} - v)(xi)/Phi_m(k) stays close
      to +-M |zeta_m|/(C_m m); otherwise a subfamily has gaps bounded below and Corollary 6.10(c) puts the mate in cl Cert(f). So defect
      mates, if any, come from a resonance between the normer xi and the fine structure of T.
By contrast: base mass at non-contact coordinates with |z_j| <= theta < 1 only produces O(t) remainders (Corollary 7.3(a)); block
coordinates used within their two-sided capacity (|t Omega(k)| <~ gap(k)) are certificate parts; weighted-type directions whose
discarded tails are O(t), and cross mechanisms with scale-dense rates through carriers with gaps bounded below, are
certificates + O(t) at every scale (Corollary 6.10): none of these can create a defect by itself. Since (N1), (N2) are one-sided, a two-sided defect mate must use
DIFFERENT one-sided carriers on the two sides that represent the same component of g up to O(t) at each scale (N4: switching).

**Proposition 7.4 (one-sided linear decompositions). PROVED.** Let g in C(f). Suppose (b+, Omega+) and (b-, Omega-) (b+- in l_1,
Omega+- in V* supported on finitely many blocks) both represent g, and for some tau_0 > 0
  max(q*(a + tau b+), ||w + tau Omega+||) <= s(tau) for 0 <= tau <= tau_0,   max(q*(a + tau b-), ||w + tau Omega-||) <= s(tau) for -tau_0 <= tau <= 0.
Then (a) supp b+- is contained in supp a cup K, with sign b+_j = z_j and sign b-_j = -z_j for j in K cap supp b+-.
(b) If supp a cup K is finite (this holds at every NA point f, where supp a is finite and z is in c_0), then b+ = b-,
Omega+ = Omega-, supp b+ is contained in supp a, and (b+, Omega+) is a locally admissible linear decomposition; hence g is in cl Cert(f).
*Proof.* (a) For 0 < tau <= tau_0, by Lemma 7.2, q*(a + tau b+) = 1 + tau b+(zhat) + tau sum_{j not in supp a}(|b+_j| - z_j b+_j) + o(tau)
(Fl and Psi are o(tau)), and N_m(w_m + tau Omega+_m) >= 1 + tau <Omega+_m, zeta_m>/|zeta_m|. Admissibility forces both first-order
coefficients to be <= 0. Their combination q_0 [b+(zhat) + sum_{j notin supp a}(|b+_j| - z_j b+_j)] + sum_m |zeta_m| <Omega+_m, zeta_m>/|zeta_m|
equals q_0 sum_{j notin supp a}(|b+_j| - z_j b+_j) + g(xi) = q_0 sum_{j notin supp a}(|b+_j| - z_j b+_j) >= 0 and is <= 0, so
|b+_j| = z_j b+_j for every j outside supp a. The case of b- is symmetric (replace tau by -tau and b- by -b-).
(b) b+ - b- is supported in the finite set supp a cup K, so it lies in c_00; Fact F(a) gives b+ = b- and Omega+ = Omega-.
On K, sign b_j = z_j = -z_j forces b_j = 0. The common decomposition is admissible on both sides; apply Theorem 6.5. QED.

**Corollary 7.5. PROVED.** If supp a cup K is finite (e.g. f in NA) and g is in Def(f), then on at least one side of t = 0 the
mate g has NO locally admissible linear decomposition with bounded block part: its admissible decompositions are genuinely
scale dependent there. In particular, at NA points one-sided base contacts (K nonempty) can only be exploited through scale-
dependent mechanisms (N4).

Remark 7.6 (infinite contact sets). If K is infinite (possible only when f does not attain its norm: z in l_infinity \ c_0 with
|z_j| = 1 infinitely often off supp a), b+ - b- may be an infinitely supported vector in L*(V*), and Proposition 7.4(b) fails.
Whether two-piece mates of this kind exist depends on whether Y cap l_1(supp a cup K) contains suitable vectors with the sign
pattern of (a). OPEN.

### 7.3 Cross mechanisms and approximation rates (SKETCH / HEURISTIC; the positive part is Corollary 6.10(c), PROVED)
Let v in S_{q*} with v(xi) = 0, c in R, and suppose at scale t the component t c v of t g is carried by one off-peak coordinate k
of block m: put t Omega(k) := t c/lambda_{k,m} (so t R_m*(Omega(k) e_k) = t c u_{k,m}) and let the base absorb t c (v - u_{k,m}).
Costs (Lemma 7.2, Lemma 4.4): box: |t c|/lambda_{k,m} <= gap_m(k)/2; Hilbert: first order t c Phi_m(k) w_m(k)/(m C_m) (absorbed by the
d-correction, and O(t Phi_m(k)) anyway) and second order t^2 c^2/(2 m^2 C_m); base: at most |t||c| (1 + ||U||) ||v - u_{k,m}||_1.
So the cost is O(t^2) iff there is an off-peak k with lambda_{k,m} >= 2|t||c|/gap_m(k) and ||u_{k,m} - v||_1 <~ |t|.
* If such k exist at all small scales (scale-dense rates: ||u_{k_i,m} - v|| <= K' lambda_{k_i,m}, lambda_{k_{i+1}}/lambda_{k_i} >= beta > 0),
  the decomposition at scale t IS "certificate + O(t)", and Corollary 6.10(c) shows that such cross mates lie in cl Cert(f):
  they are recovered along every sequence. (Earlier in this work I expected them to be a defect source; the averaging theorem
  shows they are not.)
* If good approximations are sparse in scale (gaps in the sequence of scales), the single-carrier cross mechanism is not available
  at the intermediate scales, and a mate needing the component c v at those scales must use other resources.
Whether Martín's u_{k,m} have such rates I cannot check (paper unavailable). Status of this subsection: SKETCH (single
mechanism computation), with the positive conclusion PROVED in Corollary 6.10(c).

### 7.4 The borderline case of box tails of exact order sigma: RESOLVED
Weighted certificates whose box tails satisfy T(sigma) = O(sigma) (rather than o(sigma)) lie in cl Cert(f): Corollary 6.10(a).
(A first attempt by single-scale truncation fails for rho -> 1, because the error ~ c t is not small compared with
(1 - rho^2) times the radius ~ t; averaging over n geometric scales divides the effective error by n.)

### 7.5 Conjecture (HEURISTIC)
Call T *scale separated* if no base vector e_j* (j in N) and no block vector u_{k,m} can be approximated, within a fixed multiple of
lambda_{k',m'}, by a combination of block vectors u_{k',m'} at comparable scales lambda_{k',m'} other than itself. Conjecture: if T is
scale separated, then for every f the admissible decompositions of every mate are, on at least one side, "certificate + O(t)"
at all small scales; hence Def(f) is empty for every f, C is Hausdorff continuous on S_{p*}, and NA((c_0,p), l_2^d) is dense for all d.
Evidence: by §7.2 a defect mate needs switching between different one-sided carriers representing the same component of g up to
O(t) at scale t, which is exactly an approximation of one carrier by others at its own scale. Missing: a proof that the carried
components on the two sides must match carrier-by-carrier up to O(t) (a quantitative "linear independence at scale" argument),
and control of contacts/near-contacts and weak peaks. I have no proof. Whether Martín's T is scale separated is unknown to me.

