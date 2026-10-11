# G3 (Round 14, adversarial): persistent residual rows -- universal switching constraints, self-pinning, and what a counterexample would need

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "Mod chain" = modulo the refereed links cited (Part III Sections 2-5, Part II
Sections 4-5, K1/K2, H2/H2-ref, J1/J2, U3, G2) with their referee status.  Part files: r14/G3_part1.md (universal lemmas), G3_part2.md
(construction attempts, block results), G3_part3.md (other means, (Q*), numerics).  Where this file and the part files differ, THIS
FILE is authoritative (it corrects a factor in the proof of Cor. 2.11, adds Theorem CL, Corollaries CL.1-CL.2, the scale dichotomy 5.3,
and replaces a stale numerical case).  Scripts and outputs: r14/G3_work/ (model.py, selfpin.py/.out, tworegime.py/.out, conserve.py/.out).

## 0. Summary

TASK.  Prove (LSC-trunc)_N for every first row f, or construct a first row f with infinite base support at which the residual
((R0) refined or (R1) with a fresh wrong-signed pinned resonance) holds at ALL large main stages, and then decide the dangerous mates.

BOTTOM LINE.  No persistent residual row was constructed and nothing found here suggests a counterexample.  (LSC-trunc)_N for every f,
and density of NA((c_0, p_N), l_2^2), remain OPEN.  Leaning: POSITIVE (the residual looks like an artifact of the realization method:
the bias of the preparation, not a property of the mates).  What was obtained:

(1) Method-independent constraints on EVERY mate of EVERY row at EVERY scale (Section 2, PROVED).  The switching vector
    V = B_+ - B_- = L^*(Theta_- - Theta_+) of any pair of decompositions of f +- t g satisfies
      |V(zhat)| <= t/q_0,   z_s V_s >= -(local excess)/(2t) off the support,   s_s V_s >= -(2|a_s| + local excess/2)/t on it,
    and hence the CONSERVATION LAW (Theorem CL): the l_1-mass of V on contacts, free coordinates and thin support is at most the
    (one-signed) zhat-weighted switching on THICK support plus O(t) + O(thin cushion/t).  Consequences: private pinning (Lemma 1.5,
    Cor. 1.6); pinning of a pair by a minor -- wrong-signed contact minors (Lemma 1.7) and FREE-coordinate (FR) minors of either sign
    (Cor. CL.2); the two-regime profile of a dangerous mate (Cor. 1.8: order-one switching on a pair only at scales >~ |minor|).
(2) Unshifted blocks (Section 3, PROVED).  A switching inequality summing all contact rows against the block's d-row (Theorem 2.10)
    and its corollary: strict non-peaks with contact/free/thin private coordinates are pinned with DESIGN constants, never with a
    minor (Cor. 2.11, above the thin-cushion scale).  In particular H2's Example 4.3 (single-contact pair resonance) self-pins: the anti-aligned mass that makes the
    minor tiny pins the pair (Lemma 2.8, Cor. 2.9).  This agrees with G1 Cor. 5.4 (which realizes the same configuration by the
    cushioned Hoffman lemma) from the opposite side: at the norm level such a pair is never an ACTIVE residual above its cushion scale.
(3) Construction (Section 4).  Persistence of open or exact stage conditions with fresh parameters is automatic (Lemmas 2.1, 2.2,
    PROVED).  But the natural constructions are blocked: resonances through private data are coincidences of discrete design data
    (Cor. 2.4; excluded by the design addition (D-pat), HEURISTICally harmless); the continuous data able to tune a resonance are
    themselves two-sided Step-A generators that every near-certificate must annihilate (tuning-lever duality, HEURISTIC); and by
    Theorem CL / Cor. 2.11 active kind-(iv) rows of unshifted blocks switch only through SHARED THICK TARGET support.  The remaining
    adversarial configuration RC_L is a SKETCH, not a construction.  Dangerous mates of wrong-signed rows arise as limits of mates of
    exactly-resonant rows (Cor. 2.7), so persistent residual rows come in families whose members are of bias type.
(4) Other means (Section 5).  Non-recoverability is open on the graph (Lemma 3.1, PROVED): a counterexample must be far from the fibres
    of all finite-support rows, of the comeager Fort set, and of every transport-covered row nearby.  A wrong-signed minor M is
    VT-tolerated in windows above C|M| (Prop. 3.3, PROVED mod chain) and harmless in windows below c|M| where the mate is pinned
    (scale dichotomy 5.3, SKETCH); so the persistent residual is effectively of EXACT/BIAS type, in agreement with G2 Prop. 4.7 /
    Cor. 4.8.  Thick masses are heavy (Lemma 3.4, PROVED mod chain): no invisible pre-modification breaks an (R0) resonance.
(5) The precise remaining property (Section 6, OPEN): (Q*) a two-sided d-consistency lever for the resonant kind-(iv) rows whose BIAS
    on the resonance is <= delta s_1/(32 rho C_d) while its range is >= 16 K_J Pi_X -- a bias-free lever.  It fails exactly at
    the deep-swallowed carriers of G2-ref Thm 4.9' (P-res'); G1's split preparation reduces the bias but not below the VT tolerance.
(6) Numerics (Section 7): finite SOCP models confirm every pinning/freeing prediction and Theorem CL at the scales where the solver is
    accurate; they prove nothing about the infinite-dimensional question.

| # | Result | Status | Sec. |
|---|---|---|---|
| 1 | Lemma 1.1 (weighted excess budget), Lemma 1.2 (coordinate form), Cor. 1.3 (two-sided budget, attained decompositions) | PROVED | 2.1 |
| 2 | Lemma 1.4 (pointwise switching constraints; contacts, free coordinates, support) | PROVED | 2.2 |
| 3 | Theorem CL (conservation law for the switching vector), Cor. CL.1 (pinning by thick switching) | PROVED | 2.3 |
| 4 | Lemma 1.5 (private pinning), Cor. 1.6 (kind-(iv)-type carriers pinned on both sides at f) | PROVED | 2.4 |
| 5 | Lemma 1.7 (pair pinning by a wrong-signed contact minor), Cor. CL.2 (FR minors pin with either sign) | PROVED | 2.5 |
| 6 | Cor. 1.8 (two-regime profile of a dangerous mate) | PROVED | 2.5 |
| 7 | Theorem 2.10 (switching inequality in an unshifted block), Cor. 2.11 (no switching through contacts) | PROVED | 3 |
| 8 | Lemma 2.8, Cor. 2.9 (self-pinning of single-contact pair resonances; H2 Ex. 4.3 never an active residual) | PROVED | 3 |
| 9 | Lemma 2.1 (nested tuning), Lemma 2.2 (triangular exact tuning) | PROVED | 4.1 |
| 10 | Lemma 2.3 (value decomposition), Cor. 2.4 (private resonances = pattern coincidences up to the lever scale) | PROVED (decomposition); conditional on (D-pat) | 4.3 |
| 11 | (D-pat) is compatible with the design and generic | HEURISTIC | 4.3 |
| 12 | Tuning-lever duality (resonance tunings are self-defeating) | HEURISTIC (PROVED ingredients) | 4.4 |
| 13 | Adversarial stage configuration RC_L and its persistence | SKETCH | 4.5 |
| 14 | Lemma 2.6 (fibre map usc), Cor. 2.7 (dangerous mates as limits; transitivity remark) | PROVED (2.7 conditional on the approximants) | 4.6 |
| 15 | Lemma 3.1, Cor. 3.2 (openness of non-recoverability; what a counterexample must defeat) | PROVED | 5.1 |
| 16 | Prop. 3.3 (VT tolerance of wrong-signed minors above C|M|) and the bias obstruction | PROVED mod chain | 5.2 |
| 17 | Scale dichotomy: wrong-signed nonzero minors are harmless in windows below c|M|; residual is of exact/bias type | SKETCH | 5.3 |
| 18 | Lemma 3.4 (thick masses are heavy; no invisible pre-modification for (R0)) | PROVED mod chain | 5.4 |
| 19 | Raise transfer / Theorem N / transitivity give no relief at residual rows | HEURISTIC (transitivity part PROVED) | 5.5 |
| 20 | (Q*) bias-free two-sided levers for the resonant kind-(iv) rows | OPEN | 6 |
| 21 | Existence of a first row with a persistent residual (counterexample candidate) | OPEN (none constructed) | 4.5, 8 |
| 22 | (LSC-trunc)_N for every f; density of NA((c_0, p_N), l_2^2) | OPEN | 8 |

## 1. Setting and notation

Finite or infinite block set, p = p_N, any admissible design T (Sections 2-3 use nothing about the design).  f in S_{p*} has forced
data (xi, q_0, a, w, F, z, zhat, e, nu) [Part I, Prop. 1.9]: f = a + L^*w, q*(a) = ||a||_1 + nu = 1, nu = ||U^*a||, e = U^*a/nu,
zhat = z + U e, xi = q_0 zhat, F = supp a, z = sgn a on F, ||z||_inf <= 1; h := zhat - z = U e.  The base is diagonal throughout (as in
the design): h_s = (mu*_s)^2 a_s/nu, zero off F (Theorem CL holds for any base; Lemma 2.8 and Cor. 2.11 use h = 0 off F).
zeta_m := R_m^** xi, sigma_m := |zeta_m|_m, q_0 + sum_m sigma_m = 1, <w_m, zeta_m> = sigma_m, N_m(w_m) = 1.  lambda_k := m Phi_m(k),
R_m^* Theta = sum_k lambda_k Theta(k) u_{k,m}.  s(t) := (1 + t^2)^{1/2}, so s(t) - 1 <= t^2/2.  Excess functions
   G_b(A) := q*(A) - A(zhat) >= 0,      G_m(W) := N_m(W) - <W, zeta_m>/sigma_m >= 0.
A coordinate j notin F is a CONTACT if |z_j| = 1 and FREE if |z_j| < 1 (eta_j := 1 - |z_j|).  For a set E, alpha(E) := sum_{E ∩ F} |a_j|.
C(f) := {g : p*(f + t g) <= s(t) for all real t} (the mate fibre; g in C(f) iff ||(f, g)|| <= 1 as an operator into l_2^2).

## 2. Universal constraints on mates (any row, any mate, any scale)

### 2.1 Excess budget

LEMMA 1.1 (weighted excess budget).  PROVED.  If h(xi) = 0 and f + h = A + sum_m R_m^* W_m with max(q*(A), max_m N_m(W_m)) <= pi, then
      q_0 G_b(A) + sum_m sigma_m G_m(W_m) <= pi - 1.
Proof.  (R_m^* W_m)(xi) = <W_m, zeta_m> and xi = q_0 zhat, so the left side equals q_0 q*(A) + sum_m sigma_m N_m(W_m) - (f + h)(xi)
<= pi (q_0 + sum_m sigma_m) - f(xi) = pi - 1.  QED

LEMMA 1.2 (coordinate form).  PROVED.  G_b(A) >= E_b(A) := sum_j (|A_j| - z_j A_j), each summand >= 0; for every j and |z_j| <= 1,
|x| - z_j x >= 2 (z_j x)_-, and |x| - z_j x >= (1 - |z_j|)|x|; at j in F (z_j = s_j := sgn a_j) the summand is 2(-s_j A_j)_+.
Proof.  A(zhat) = A(z) + <U^*A, e> and ||e|| = 1, so G_b(A) >= ||A||_1 - A(z).  If z_j x >= 0 then |x| - z_j x = (1 - |z_j|)|x| >= 0; if
z_j x < 0 then |x| - z_j x = |x| + |z_j x| >= 2|z_j x|, and also >= (1 - |z_j|)|x|.  QED

COROLLARY 1.3 (two-sided budget).  PROVED.  Let g in C(f), t > 0.  Then g(xi) = 0 for every normer xi of f; there are decompositions
      f + t g = A_+ + L^*W_+,   f - t g = A_- + L^*W_-,   max(q*(A_+-), max_m N_m(W_{+-,m})) <= s(t),
and every such pair satisfies E_b(A_+) + E_b(A_-) <= 2(s(t) - 1)/q_0 <= t^2/q_0.
Proof.  (f +- t g)(xi) <= p*(f +- tg) <= s(t) gives +-t g(xi) <= s(t) - 1 <= t^2/2 for all t > 0, so g(xi) = 0.  The infimum
p*(h) = inf{max(q*(A), ||W||_{V*}) : h = A + L^*W} is attained: {W : ||W||_{V*} <= c} is weak*-compact, L^* is weak*-continuous and
q* is weak*-lsc on l_1 = c_0^*.  Apply Lemma 1.1 with h = +-tg, drop the block excesses, and use Lemma 1.2.  QED

NOTATION.  B_+ := (A_+ - a)/t, B_- := (a - A_-)/t, Theta_+ := (W_+ - w)/t, Theta_- := (w - W_-)/t; then g = B_+ + L^*Theta_+ =
B_- + L^*Theta_-, and the SWITCHING VECTOR is V := B_+ - B_- = L^*(Theta_- - Theta_+) = sum_k gamma_k u_k with SWITCHING AMPLITUDES
gamma_k := lambda_k (Theta_- - Theta_+)(k).  e_j^+- := the summand of E_b(A_+-) at j; sum_j (e_j^+ + e_j^-) <= t^2/q_0.

### 2.2 Pointwise sign constraints

LEMMA 1.4.  PROVED.  At every coordinate j:
 (a) j notin F (contact or free):   z_j V_j >= -(e_j^+ + e_j^-)/(2t);
 (b) j in F:                          s_j V_j >= -(2|a_j| + (e_j^+ + e_j^-)/2)/t;
 (c) j notin F:                       (1 - |z_j|) |V_j| <= (e_j^+ + e_j^-)/t.
Consequently, for every set E of coordinates,
      sum_{j in E} (o_j V_j)_- <= 2 alpha(E)/t + t/(2 q_0),        o_j := z_j.                                          (1.1)
Proof.  (a) a_j = 0, so A_+(j) = t B_+(j), A_-(j) = -t B_-(j); by Lemma 1.2, e_j^+ >= 2t (z_j B_+(j))_- and e_j^- >= 2t (z_j B_-(j))_+, and
z_j V_j = z_j B_+(j) - z_j B_-(j) >= -(z_j B_+(j))_- - (z_j B_-(j))_+.  (b) A_+(j) = a_j + t B_+(j): e_j^+ = 2(-s_j a_j - s_j t B_+(j))_+ =
2(-s_j t B_+(j) - |a_j|)_+, so (-s_j B_+(j))_+ <= (|a_j| + e_j^+/2)/t; likewise (s_j B_-(j))_+ <= (|a_j| + e_j^-/2)/t; and
s_j V_j >= -(-s_j B_+(j))_+ - (s_j B_-(j))_+.  (c) e_j^+- >= (1 - |z_j|) t |B_+-(j)| (Lemma 1.2) and |V_j| <= |B_+(j)| + |B_-(j)|.  (1.1):
sum (a), (b) over E; the excesses sum to <= t^2/q_0.  QED
[(a) at free coordinates is new relative to part 1, where it was stated for contacts only.]

### 2.3 The conservation law

THEOREM CL (conservation law for the switching vector).  PROVED.  Let g in C(f), t > 0, decompositions as in Cor. 1.3, and let T ⊂ F be
any set ("thick" support) and N its complement (contacts, free coordinates, and the remaining "thin" support N ∩ F).  Then
 (CL0)  |B_+(zhat)|, |B_-(zhat)| <= (s(t) - 1)/(q_0 t),   hence   |V(zhat)| <= 2(s(t) - 1)/(q_0 t) <= t/q_0;
 (CL1)  sum_{s in T} zhat_s V_s  <=  |<V 1_N, h>| + 3t/(2 q_0) + 2 alpha(N ∩ F)/t        (thick switching is one-signed);
 (CL2)  ||V 1_N||_1  <=  - sum_{s in T} zhat_s V_s + |<V 1_N, h>| + 3t/q_0 + 4 alpha(N ∩ F)/t.
In the diagonal base h = 0 off F and |<V 1_N, h>| <= max_{N ∩ F} |h_s| ||V 1_{N ∩ F}||_1; if this max is <= 1/2,
      ||V 1_N||_1 <= 2 [ - sum_{s in T} zhat_s V_s + 3t/q_0 + 4 alpha(N ∩ F)/t ].
Proof.  (CL0): q*(A_+) >= A_+(zhat) = a(zhat) + t B_+(zhat) = 1 + t B_+(zhat) (a(zhat) = ||a||_1 + nu = 1), so t B_+(zhat) <= s(t) - 1.
For each block, N_m(W_{+,m}) >= <W_{+,m}, zeta_m>/sigma_m, so x_m := t <Theta_{+,m}, zeta_m> <= sigma_m (s(t) - 1).  Evaluating
f + t g = A_+ + L^*W_+ at xi (g(xi) = 0, f(xi) = q_0 + sum_m sigma_m = 1) gives x_0 + sum_m x_m = 0 with x_0 := q_0 t B_+(zhat).  Hence
x_0 = -sum_m x_m >= -(1 - q_0)(s(t) - 1), and q_0 t |B_+(zhat)| <= max(q_0, 1 - q_0)(s(t) - 1) <= s(t) - 1.  The minus side is the same
with f - t g = A_- + L^*W_-, A_- = a - t B_-, W_- = w - t Theta_-.  (CL1), (CL2): split
      V(zhat) = sum_{s in T} zhat_s V_s + sum_{s in N} z_s V_s + <V 1_N, h>.
By Lemma 1.4(a),(b), z_s V_s >= -err_s on N with err_s := (e_s^+ + e_s^-)/(2t) off F and (2|a_s| + (e_s^+ + e_s^-)/2)/t on N ∩ F, and
sum_N err_s <= 2 alpha(N ∩ F)/t + (1/(2t)) sum_N (e_s^+ + e_s^-).  So sum_T zhat_s V_s <= V(zhat) - <V 1_N, h> + sum_N err_s, which is (CL1).
Next sum_N |z_s||V_s| = sum_N z_s V_s + 2 sum_N (z_s V_s)_- <= V(zhat) - sum_T zhat_s V_s - <V 1_N, h> + 2 sum_N err_s, and at free
coordinates (1 - |z_s|)|V_s| <= (e_s^+ + e_s^-)/t (Lemma 1.4(c)); since |z_s| = 1 on the rest of N, adding gives
||V 1_N||_1 <= t/q_0 - sum_T zhat_s V_s + |<V 1_N, h>| + 4 alpha(N ∩ F)/t + (2/t) sum_N (e_s^+ + e_s^-), and the last sum is <= t^2/q_0.
The final display: on N ∩ F, |z_s| = 1 and |<V 1_N, h>| <= (1/2) ||V 1_N||_1; absorb.  QED

READING.  At every scale and for every mate, the switching that a mate performs on contacts, free coordinates and thin support (in
l_1) must be "paid for" by NEGATIVE zhat-weighted switching on thick support; thin support pays only through its cushion
4 alpha/t.  The exact (t -> 0) form is the side admissibility of two-piece data [Part I, Def. 7.7]; Theorem CL is its quantitative,
scale-t form with the thin/thick split.  (Checked numerically in conserve.out, Section 7.)

COROLLARY CL.1 (pinning by thick switching).  PROVED.  Let k be a carrier, P_k ⊂ N a set of coordinates with V_s = gamma_k u_k(s) + psi_s
on P_k (psi = the other carriers), Psi_k := ||psi 1_{P_k}||_1.  Then
      |gamma_k| ||u_k 1_{P_k}||_1  <=  - sum_{s in T} zhat_s V_s + |<V 1_N, h>| + 3t/q_0 + 4 alpha(N ∩ F)/t + Psi_k.
In particular, if no switching carrier meets T (V = 0 on T), every carrier with private mass P_k in N switches with amplitude
O((t + alpha(N ∩ F)/t)/P_k) (diagonal base, |h| <= 1/2 on N ∩ F): at scales t << P_k, switching of order one needs thick support,
or thin support at scales t <~ alpha/P_k.  Free coordinates are NOT an escape: they enter ||V 1_N||_1 with full weight (Lemma 1.4(c)).
(The only other escape is cancellation in V among carriers without private mass in N -- a larger resonant group; in the design every
coarse carrier has private signature mass.)
Proof.  |gamma_k||u_k(s)| <= |V_s| + |psi_s| on P_k; sum and apply (CL2).  The last claim is the final display of Theorem CL.  QED

### 2.4 Private pinning

LEMMA 1.5 (private pinning).  PROVED.  Let k be a carrier and E a set of contacts and support coordinates.  Write V_j = gamma_k u_k(j)
+ psi_j on E, orient j by o_j := sgn(z_j u_k(j)), E^+- := {j in E : o_j = +-1}, U^+- := sum_{E^+-} |u_k(j)|, alpha^+- := alpha(E^+-),
Psi^+- := sum_{E^+-} |psi_j|.  Then
      -(2 alpha^+/t + t/(2 q_0) + Psi^+)/U^+  <=  gamma_k  <=  (2 alpha^-/t + t/(2 q_0) + Psi^-)/U^-                       (1.2)
(a side is void if U^+- = 0).  [Free coordinates j are pinned two-sidedly by Lemma 1.4(c): |gamma_k u_k(j)| <= t/(q_0 eta_j) + |psi_j|.]
Proof.  On E^+, z_j V_j = gamma_k |u_k(j)| + z_j psi_j; summing Lemma 1.4(a),(b) over E^+ and using (1.1): gamma_k U^+ >= -(2 alpha^+/t +
t/(2q_0)) - Psi^+.  On E^-, z_j V_j = -gamma_k |u_k(j)| + z_j psi_j, giving gamma_k U^- <= 2 alpha^-/t + t/(2 q_0) + Psi^-.  QED

COROLLARY 1.6 (kind-(iv)-type carriers are pinned at f on both sides).  PROVED.  Let l be a carrier with data sign eps_l, a set N_l of
"near" coordinates (contacts or support with eps_l z_j u_l(j) > 0) and a set E_far of "far" coordinates (contacts or support with
eps_l z_j u_l(j) < 0), both private up to psi.  Then, with gamma'_l := eps_l gamma_l (data-sign switching),
      -(2 alpha(N_l)/t + t/(2q_0) + Psi_N)/U_N  <=  gamma'_l  <=  (2 alpha(E_far)/t + t/(2q_0) + Psi_far)/U_far,
U_N, U_far the masses of u_l on N_l, E_far.  If alpha(N_l) + alpha(E_far) <= t^2 then |gamma_l| <= [(2 + 1/(2q_0)) t + Psi_N + Psi_far]/min(U_N, U_far).
Proof.  Lemma 1.5 with E^{sgn eps_l} = N_l and E^{-sgn eps_l} = E_far, multiplied by eps_l.  QED
READING.  For the kind-(iv) carriers of (R1) (data-sign near coordinates; anti-sign pull ranges, H2 Thm H2.B(i)) the data-sign
switching at f is pinned with constant 1/U_far: order-one switching occurs only at scales t >~ U_far (the anti-sign far mass), and
the anti-data-sign direction is pinned with the design constant 1/U_N.  This is the norm-level content of "kind (iv) is one-sided".

### 2.5 Pinning by a minor; the two-regime profile

LEMMA 1.7 (pair pinning by a wrong-signed contact minor).  PROVED.  Fix a block (index dropped), a scale t and decompositions as in
Cor. 1.3; Delta Theta := Theta_- - Theta_+.  Let P be the peaks, Q the strict non-peaks.  Assume
 (P1) [unshifted]  |Delta Theta(k)| <= eta_P for every k in P;
 (P2) for two strict non-peaks k_1, k_2:  |sum_{k in Q \ {k_1,k_2}} u_k(zhat) gamma_k| <= r_Q;
 (P3) j is a contact and V_j = gamma_1 u_1(j) + gamma_2 u_2(j) + psi_j  (u_i := u_{k_i}, gamma_i := gamma_{k_i}).
Put Mj := u_1(j) u_2(zhat) - u_2(j) u_1(zhat), S := u_1(zhat) gamma_1 + u_2(zhat) gamma_2, Phi_P^2 := sum_{k in P} Phi(k)^2.  Then
 (i)  |S| <= S_0(t) := t/q_0 + (sigma/q_0) eta_P (1 + M Phi_P^2/C) + r_Q;
 (ii) z_j gamma_1 Mj/u_2(zhat) >= -[ (e_j^+ + e_j^-)/(2t) + |psi_j| + |u_2(j)/u_2(zhat)| S_0(t) ]   (u_2(zhat) != 0).
Hence, if z_j sgn(gamma_1) Mj/u_2(zhat) < 0 (WRONG SIGN):  |gamma_1| <= |u_2(zhat)| [t/(2 q_0) + |psi_j| + |u_2(j)/u_2(zhat)| S_0(t)]/|Mj|.
Proof.  Put L(Theta) := <Theta, zeta>/sigma.  Block threshold structure [Part I]: zeta/sigma = alpha + D^2 w/C with alpha supported on
P, sgn alpha = sgn w on P, ||alpha||_1 = 1, D = diag(Phi), C = ||D w||_2, M = ||w||_inf, M + C = 1.  So
L(Theta) = sum_P |alpha(k)| sgn(w(k)) Theta(k) + <D Theta, D w>/C.
Step 1 (levels).  As in the proof of (CL0): x_m := sigma_m t L_m(Theta_{+,m}) <= sigma_m (s(t) - 1), x_0 := q_0 t B_+(zhat) <= q_0 (s(t) - 1)
and x_0 + sum_m x_m = 0; hence every x_i >= -(s(t) - 1), so sigma |L(Theta_+)| <= (s(t) - 1)/t <= t/2; same for Theta_-.  Thus
sigma |L(Delta Theta)| <= t.
Step 2 (d-row).  By (P1) the alpha-part of L(Delta Theta) has modulus <= eta_P, and the peak part of <D Delta Theta, D w>/C has modulus
<= eta_P M Phi_P^2/C.  Off P, Phi(k)^2 w(k) = C zeta(k)/sigma = C lambda_k q_0 u_k(zhat)/sigma, so the non-peak part equals
(q_0/sigma) sum_Q u_k(zhat) lambda_k Delta Theta(k) = (q_0/sigma) sum_Q u_k(zhat) gamma_k.  Therefore
|sum_Q u_k(zhat) gamma_k| <= t/q_0 + (sigma/q_0) eta_P (1 + M Phi_P^2/C), and (P2) gives (i).
Step 3.  gamma_2 = (S - u_1(zhat) gamma_1)/u_2(zhat), so V_j = gamma_1 Mj/u_2(zhat) + u_2(j) S/u_2(zhat) + psi_j; Lemma 1.4(a) gives (ii),
and (e_j^+ + e_j^-)/(2t) <= t/(2 q_0) gives the last bound.  QED
Remarks.  (1) (P1) is the norm-level form of "unshifted": by Lemma 1.1 at the peaks sgn(w(k)) Theta_+(k) is within t/(2 sigma |alpha(k)|)
of its max over supp alpha, and a peak carrier with private coordinates of both orientations pins the common value to O(t)
(Lemma 1.5).  (2) Lemma 1.7 is the norm-level form of H2 Example 4.3, Z6's Farkas pinning and U3's Lemma R-pin: a nonzero oriented
minor of the wrong sign pins the needed switching with the f-DEPENDENT constant 1/|Mj|; a vanishing minor does not pin.

COROLLARY CL.2 (strict FR minors pin with either sign).  PROVED.  In Lemma 1.7 replace (P3) by: j is a FREE coordinate (eta_j = 1 - |z_j|
> 0).  Then, whatever the sign of Mj,
      |gamma_1| |Mj| <= |u_2(zhat)| [ t/(q_0 eta_j) + |psi_j| ] + |u_2(j)| S_0(t).
Proof.  Step 3 of Lemma 1.7 gives V_j = gamma_1 Mj/u_2(zhat) + u_2(j) S/u_2(zhat) + psi_j; Lemma 1.4(c) gives |V_j| <= t/(q_0 eta_j).  QED
[G1's remaining strict resonances (R-S1) are minors made of a block (X3) row and (X1-FR) rows at free target coordinates with robust
room (G1 Thm G1.D).  Cor. CL.2 is their norm-level counterpart: at f every mate is pinned on such a pair with constant ~ 1/(eta_j |M|),
for both signs of M; the two-regime profile below applies with |M| in place of max(|Mj|, U_far).]

COROLLARY 1.8 (two-regime profile of a dangerous mate).  PROVED.  Let (l_+, l_-) be strict non-peaks of an unshifted block, each of
kind-(iv) type (Cor. 1.6), sharing a contact j with an oriented minor Mj of the wrong sign for the data-sign switching of l_+, with
thin cushions (alpha <= t^2) and psi, eta_P, r_Q negligible.  Then for every mate and every scale t
      -C_f t/U_N(l_+)  <=  gamma'_{l_+}(t)  <=  C_f t / max(|Mj|, U_far(l_+)),
C_f depending only on q_0, u_2(zhat), u_2(j) and the constants of 1.6-1.7.  So the pair switches with order-one amplitude only at
scales t >~ max(|Mj|, U_far)/C_f (the FREE regime); below, it is pinned with the f-dependent constant C_f/max(|Mj|, U_far).  If a mate
is active on l_+ with data-sign amplitude >= c_0 at a scale t_a, then
      |Mj| <= C_f t_a/c_0      and      U_far(l_+) <= C_f t_a/c_0.                                                   (1.3)
Proof.  Lower bound: Cor. 1.6.  Upper bound: the minimum of the upper bounds of Cor. 1.6 and Lemma 1.7 (data-sign direction, wrong
sign), with 2 alpha/t <= 2t and S_0(t) <= 2t/q_0 under the negligibility assumptions.  QED
READING.  A wrong-signed resonance constrains a mate only at scales <~ |Mj|.  If the pair's activity is only RELATIVE (|gamma| >= K_* t,
the class thresholds of K1 Lemma K1.2), (1.3) gives only |Mj| <= C_f/K_*: the pair is then "pinned with a window constant", and the
residual concerns the size of that constant relative to the window's tolerances (Section 5).

## 3. Unshifted blocks: the switching inequality and self-pinning (PROVED)

THEOREM 2.10 (switching inequality in an unshifted block).  PROVED (any admissible T, any row, mate and scale).  Fix a block
satisfying (P1) at scale t, decompositions as in Cor. 1.3, a set G of strict non-peaks of the block, r_Q := |sum_{k in Q \ G} u_k(zhat)
gamma_k|, and ANY set J_c of coordinates.  For k in G put
      Rt_k := u_k(zhat) - sum_{j in J_c} u_k(j) z_j        (= sum_{s notin J_c} u_k(s) zhat_s + sum_{j in J_c} u_k(j) h_j),
psi_j := V_j - sum_{k in G} u_k(j) gamma_k (carriers outside G, peaks included), Psi_J := sum_{j in J_c} |psi_j|.  Then
      sum_{k in G} gamma_k Rt_k  <=  E(t) := S_1(t) + r_Q + t/(2 q_0) + 2 alpha(J_c)/t + Psi_J,                          (2.1)
S_1(t) := t/q_0 + (sigma/q_0) eta_P (1 + M Phi_P^2/C).
Proof.  Steps 1-2 of Lemma 1.7 (which use only (P1)) give |sum_{k in Q} u_k(zhat) gamma_k| <= S_1(t), so |sum_{k in G} u_k(zhat) gamma_k|
<= S_1 + r_Q.  Lemma 1.4(a),(b) at each j in J_c, summed with the budget: sum_{j in J_c} z_j V_j >= -t/(2q_0) - 2 alpha(J_c)/t, i.e.
sum_{k in G} gamma_k sum_{j in J_c} u_k(j) z_j >= -t/(2 q_0) - 2 alpha(J_c)/t - Psi_J.  Subtract from the first bound.  QED
Note.  (2.1) involves no minor, is invariant under re-orientation, and the contact rows enter only summed.  It is the scale-t,
quantitative form of U3's exact rigidity (Lemma S, Corollaries S1, S2).  Theorem CL is the global (all-block) analogue with T in place
of the complement of J_c; 2.10 is finer in that it separates the block's peaks and other blocks (through (P1) and r_Q, Psi_J).

COROLLARY 2.11 (no switching through contacts in an unshifted block).  PROVED.  In 2.10 let J_c consist of contacts, free
coordinates and support coordinates with |a_j| <= alpha, and assume that for every k in G each s in supp u_k \ J_c is PRIVATE
to k within G (V_s = gamma_k u_k(s) + psi_s with psi from carriers outside G) and is a contact, a free coordinate, or a support
coordinate with |a_s| <= alpha.  Put
P_k := ||u_k 1_{supp u_k \ J_c}||_1, h_k := sum_{s in supp u_k} |u_k(s) h_s|, Psi_k := sum_{s in supp u_k \ J_c} |psi_s|,
beta_k := 2 alpha(supp u_k \ J_c)/t + 3t/(2 q_0) + Psi_k, and assume h_k < P_k/4.  Then for every k in G
      |gamma_k|  <=  5 [ E(t) + sum_{k' in G} beta_{k'} ] / min_{k' in G} (P_{k'}/4 - h_{k'}).
So at every scale t >= (2 alpha)^{1/2} the whole set G is pinned with a constant that depends only on the private masses P_k (design
quantities: P_k >= near mass >= 6/H(L) for a coarse carrier at an (R1) stage) and on q_0, sigma -- never on a minor.
Proof.  Fix k, eps := sgn gamma_k.  Split the private coordinates of k into ALIGNED ones (contacts/support with eps z_s u_k(s) > 0, or free
with eps z_s u_k(s) > 0), ANTI-ALIGNED ones (the reverse strict inequality), and free ones with z_s = 0; put N^z := sum_aligned |z_s||u_k(s)|,
F^z := sum_anti |z_s||u_k(s)|, Fr := sum_{free} eta_s |u_k(s)|, so that P_k = N^z + F^z + Fr (|z_s| + eta_s = 1 at free s, |z_s| = 1
elsewhere).  (1) If F^z >= P_k/4: Lemma 1.4(a),(b) on the anti-aligned set gives |gamma_k| F^z <= 2 alpha/t + t/(2 q_0) + Psi_k (as in
Lemma 1.5; at a free anti-aligned s, z_s V_s = -|gamma_k||z_s u_k(s)| + z_s psi_s).  (2) If Fr >= P_k/4: Lemma 1.4(c) gives
|gamma_k| eta_s |u_k(s)| <= eta_s |V_s| + |psi_s| and sum_free eta_s |V_s| <= t/q_0, so |gamma_k| Fr <= t/q_0 + Psi_k.  In both cases
|gamma_k| <= 4 beta_k/P_k <= beta_k/(P_k/4 - h_k).  (3) Otherwise N^z > P_k/2, and since Rt_k = sum_{s notin J_c} u_k(s) z_s +
sum_s u_k(s) h_s, eps Rt_k >= N^z - F^z - h_k > P_k/4 - h_k > 0, so gamma_k Rt_k >= |gamma_k| (P_k/4 - h_k).  Let G_1
be the carriers in cases (1)-(2) and G_2 the others.  By (2.1) and |Rt_k| <= P_k + h_k <= (5/4) P_k,
   sum_{G_2} |gamma_k| (P_k/4 - h_k) <= E(t) - sum_{G_1} gamma_k Rt_k <= E(t) + sum_{G_1} (4 beta_k/P_k)(5/4) P_k <= E(t) + 5 sum_{G_1} beta_k.
QED  [Corrects part 2: there the free-coordinate bound had t/(2 q_0 eta_s) instead of t/(q_0 eta_s), and the split used 1/3, which is
not enough when free coordinates are present.]

LEMMA 2.8 (self-pinning of single-contact pair resonances).  PROVED (any admissible T; the norm-level form of H2 Example 4.3).  Fix a
block, a scale t and decompositions satisfying (P1); two strict non-peaks l_+, l_- with data signs eps_+-, oriented values
val_+- := eps_+- u_+-(zhat), val_+ > 0 > val_-; a contact j with y_+-(j) := u_+-(j); E_+- := supp u_+- \ {j} disjoint, consisting of
contacts and support coordinates, V_s = gamma_+- u_+-(s) + psi_s on E_+-, Psi_+- := sum_{E_+-} |psi_s|.  Split E_+- into ALIGNED A_+-
(eps z_s u(s) > 0) and ANTI-ALIGNED R_+- coordinates, with masses N_+-, F_+- and cushions alpha^A_+-, alpha^R_+-; h_+- := eps_+- sum_{E_+-} u_+-(s)
h_s; w_+- := N_+- - F_+- + h_+-; gamma'_+- := eps_+- gamma_+-; S := u_+(zhat) gamma_+ + u_-(zhat) gamma_- (|S| <= S_0(t), Lemma 1.7(i));
      D := val_+ w_- + |val_-| w_+          (the oriented minor of the d-row and the contact row at j).
Then:
 (a) -(2 alpha^A/t + t/(2q_0) + Psi)/N <= gamma' <= (2 alpha^R/t + t/(2q_0) + Psi)/F   for each of l_+, l_-;
 (b) z_j V_j = -gamma'_+ D/|val_-| - B S/|val_-| + z_j psi_j,   B := eps_- y_-(j) z_j;
 (c) if D > 0 ("wrong sign"): gamma'_+ <= [t/(2 q_0) + |B| S_0(t)/|val_-| + |psi_j|] |val_-|/D;
 (d) if |D| <= tau, some l in {+, -} has F_l >= N_l + h_l - tau/v_0, v_0 := min(val_+, |val_-|);
 (e) for that l, with C_v := max(1, val_+/|val_-|, |val_-|/val_+):
      max(gamma'_+, gamma'_-) <= C_v [ (2 alpha^R_l/t + t/(2q_0) + Psi_l)/F_l + S_0(t)/v_0 ].
Proof.  (a) Lemma 1.5 with E = E_l: for eps = +1 the aligned set is E^+; for eps = -1 the roles of E^+- are exchanged and gamma' = -gamma.
(b) On E_+- (contacts/support) z_s = +-1, so eps sum_E u(s) z_s = N - F and val_+ = A + w_+, val_- = B + w_- with A := eps_+ y_+(j) z_j
(zhat_j = z_j).  S = val_+ gamma'_+ + val_- gamma'_-, so gamma'_- = (S - val_+ gamma'_+)/val_-, and
z_j V_j = A gamma'_+ + B gamma'_- + z_j psi_j = gamma'_+ (A val_- - B val_+)/val_- + B S/val_- + z_j psi_j, with
A val_- - B val_+ = A w_- - B w_+ = val_+ w_- - val_- w_+ = D.  (c) Lemma 1.4(a) at j.  (d) If both w_l > tau/v_0 then
D >= v_0 (w_+ + w_-) > 2 tau.  (e) From S = val_+ gamma'_+ + val_- gamma'_-: gamma'_+ <= (|val_-|/val_+) gamma'_- + S_0/val_+ and
gamma'_- <= (val_+/|val_-|) gamma'_+ + S_0/|val_-|; insert (a) for l.  QED

COROLLARY 2.9 (single-contact resonances are design-pinned above the cushion scale).  PROVED.  In 2.8, if |D| <= tau <= v_0 N_l/2 for
both l, then at every scale t >= (8 q_0 alpha^R_l)^{1/2}
      max(gamma'_+, gamma'_-) <= C_v [ (3t/(4 q_0) + Psi_l)/(N_l/2 - |h_l|) + S_0(t)/v_0 ]  =  O(t) with no minor in the denominator.
Hence a pair with a tiny minor whose coordinates outside j are contacts or thin support cannot be ACTIVE (above the design pinning
threshold) at any scale t >> (alpha^R)^{1/2}; in (R1) (alpha^R <= #R b) its activity is confined to t <~ (b #R)^{1/2}, the bottom of the
window.  An active pair with a tiny minor at larger scales needs two-sided coordinates outside j -- THICK support (in (R1): thick
TARGET coordinates) -- or other active carriers switching on E_+- (Psi != 0: a larger resonant group).
Proof.  (d) gives F_l >= N_l/2 - |h_l|; 2 alpha^R_l/t <= t/(4 q_0) when t^2 >= 8 q_0 alpha^R_l; insert in (e).  QED

INTERPRETATION (PROVED as stated; the identification of design objects is mod chain).
 (a) H2's Example 4.3 (single common contact, private contact/thin coordinates) is pinned whatever the sign or size of its minor:
     2.8(c) if D > 0 robustly, 2.9 if D is tiny, 2.11 in general.  The configuration "active pinned kind-(iv) pair in a one-signed
     resonance at a single common contact" is EMPTY above the thin-cushion scale.  (G1 Cor. 5.4 realizes the same configuration by
     the cushioned Hoffman lemma: the two results are consistent and complementary.)
 (b) At an (R1) stage (no thick private coordinates, H2 Fact 1.1; design-depth support off the targets thin), active kind-(iv) rows
     of an UNSHIFTED block switch only through SHARED THICK TARGET coordinates, through thin support below its cushion scale, or
     through switching of carriers outside the group at their coordinates (Theorem CL, Cor. 2.11 with J_c := all shared contacts,
     shared free coordinates and shared thin support).  [Correction of part 2, which also listed shared FREE targets as an escape: a
     free coordinate pins V two-sidedly (Lemma 1.4(c)) and may be put into J_c.]  Shared thick targets are two-sided TS generators of
     Step A, so every near-certificate annihilates them up to eps Design (K2.16(2),(4)): Psi_y(s) = kappa_y a_s there.  Persistent (R1) in unshifted blocks therefore needs,
     at every stage, fresh kind-(iv) rows switching through shared thick target support.
 (c) H1's (R0) thick-type rows switch through their thick PRIVATE coordinates: consistent with Theorem CL.
 (d) Shifted blocks escape 2.10-2.11 through the peak traces ((P1) fails), but not Theorem CL, which holds for all blocks at once.

## 4. Constructing a persistent residual row: what can be done and what blocks it

Design: T_fin^{K2} with (FC) (J2), P-TU windows and F-2 (J1-ref), diagonal base mu*_s = 2^{-2^{2^s}}, signature sets
S_l = {2^l(2i+1) : i >= 1} (pairwise disjoint), v_l(j) = delta_l 2^{-j}/n_l on S_l, carriers u_l = y_l + v_l with coarse targets
supp y_l ⊂ T(l), and H2 Lemma 2.2: T(l) ∩ union_k S_k ⊂ [1, l].

### 4.1 Abstract persistence

LEMMA 2.1 (nested tuning, open stage conditions).  PROVED.  Let (Z, d) be complete and O_L ⊂ Z open (L >= L_0), O_{L_0} != {}, and
 (FT) for every L >= L_0, every x in O_{L_0} ∩ ... ∩ O_L and every r > 0 there is x' with d(x', x) < r and x' in O_{L_0} ∩ ... ∩ O_{L+1}.
Then the intersection of all O_L is nonempty.
Proof.  Pick x_1 in O_{L_0}, s_1 in (0, 1] with B[x_1, s_1] ⊂ O_{L_0}.  Given B_i := B[x_i, s_i] ⊂ O_{L_0} ∩ ... ∩ O_{L_0+i-1}, (FT) gives
x_{i+1} with d(x_{i+1}, x_i) < s_i/2 in the open set O_{L_0} ∩ ... ∩ O_{L_0+i}; choose s_{i+1} <= s_i/4 with B[x_{i+1}, s_{i+1}] in that
set; then B_{i+1} ⊂ B_i.  The nested closed balls have radii -> 0, so they meet in one point, which lies in every O_L.  QED
[Only (FT) carries content: stage-(L+1) data must be "fresh" -- reachable by an arbitrarily small move from any point satisfying the
earlier open conditions; in the design, deep coordinates whose effect on stage <= L data is far below the earlier tolerances.]

LEMMA 2.2 (exact stage equations, triangular tuning).  PROVED.  Let B := prod_{L >= 1} [-1, 1] and
      Phi_L(theta) = c_L theta_L + phi_L(theta_1, ..., theta_{L-1}) + psi_L(theta_{L+1}, theta_{L+2}, ...),      c_L > 0,
with |phi_L| <= c_L/2, |psi_L| <= c_L/4 on B, |phi_L(x) - phi_L(x')| <= Lambda_L max_{L' < L} |x_{L'} - x'_{L'}|,
|psi_L(y) - psi_L(y')| <= sum_{L' > L} eps_{LL'} |y_{L'} - y'_{L'}|.  If weights 1 >= w_1 >= w_2 >= ... > 0 satisfy
      w_L Lambda_L <= (c_L/4) min_{L' < L} w_{L'}       and       sum_{L' > L} eps_{LL'} w_L/w_{L'} <= c_L/4      (all L),
then some theta* in B has Phi_L(theta*) = 0 for every L.
Proof.  Define T: B -> B by forward substitution, (T theta)_L := -(phi_L((T theta)_{<L}) + psi_L(theta_{>L}))/c_L (|(T theta)_L| <= 3/4).
With ||x||_w := sup_L w_L |x_L|, (B, ||.||_w) is complete (Cauchy sequences converge coordinatewise, and the coordinatewise limit is the
||.||_w-limit).  For theta, theta' in B, D := ||theta - theta'||_w, D_T := ||T theta - T theta'||_w <= 2:
   w_L |(T theta)_L - (T theta')_L| <= (w_L/c_L)[Lambda_L max_{L'<L} |(T theta - T theta')_{L'}| + sum_{L'>L} eps_{LL'} |theta_{L'} - theta'_{L'}|]
                                   <= D_T/4 + D/4,
so D_T <= D/3; the fixed point satisfies c_L theta*_L + phi_L + psi_L = 0 for all L.  QED
[Use: exact resonances at every stage, each tuned by a fresh parameter theta_L with own effect c_L, arbitrary (Lipschitz) triangular
dependence on coarser parameters, and weak dependence on deeper ones (Hilbert footprints (mu*_s)^2 of deep coordinates).]

### 4.2 What a persistent (R1) stage needs

From H2 Theorem H2.B / H2-ref (necessary conditions at all large main stages), H2 Prop. 4.1, Lemma 5.2 and Sections 2-3:
 (C1) a is b(w)-thin on F ∩ [1, D(L)] \ T(L) (H2 Lemma 2.1); a design-depth coordinate off the coarse targets during the stages
      [L_s, L'_s) has |a_s| <= min b(w(L)).  [This does NOT force a_s = 0 off a fixed set: a signature coordinate of a stage-L carrier
      becomes a TARGET coordinate of carriers of index >= s later (H2 Lemma 2.2 only gives T(l) ∩ union S_k ⊂ [1, l]).]
 (C2) every kind-(iv) pull range is anti-sign (super-thin support or contacts) (H2 Lemmas 2.3, 2.5).
 (C3) at every stage some block carries a one-signed linear resonance of tiny minors of the wrong sign at the prepared start row
      (H2 Prop. 4.1), fresh at consecutive stages (H2 Lemmas 2.6/2.7).
 (C4) a mate active on the resonant rows; by Cor. 1.8 / CL.2 its order-one switching lives at scales >~ |minor|; by Theorem CL and
      Cor. 2.11 it is paid for by switching on shared thick target support (Interpretation (b) of Section 3).

### 4.3 Private resonances are pattern coincidences

LEMMA 2.3 (value decomposition).  PROVED (from the definitions and (C1)-(C2)).  At a row satisfying (C1)-(C2) at stage L, for every
coarse carrier l and every cut-off D'(L),
      u_l(zhat) = Y_l + P_l + E_l,   Y_l := sum_{s in T(l)} y_l(s) zhat_s,   P_l := sum_{s in S_l \ T(l), s <= D'} v_l(s) z_s,
      |E_l| <= sum_{s in S_l ∩ F, s <= D'} (mu*_s)^2 v_l(s) |a_s|/nu + ||u_l 1_{(D', inf)}||_1.
At an (R1) stage every private coordinate of a kind-(iv) carrier in S_l ∩ [1, D(L)] is a contact or thin (<= b) support (a free one
is an FR generator and makes the carrier kind (i), K2.16(2a)), so z_s in {-1, +1} there.
Proof.  zhat_s = z_s + (mu*_s)^2 a_s/nu; split u_l(zhat) over T(l), S_l ∩ [1, D'] \ T(l) and the tail.  QED

COROLLARY 2.4 (private resonances are coincidences of discrete data).  PROVED (decomposition); the last consequence is conditional on
(D-pat).  Consider two kind-(iv) carriers l_+-, T(l_+) ∩ T(l_-) = {j}, j a contact, other targets contacts or thin support.  Then
      Mj(f) = u_+(j)(P_- + Y'_-) - u_-(j)(P_+ + Y'_+) + E,
the y_+-(j) zhat_j terms CANCEL EXACTLY (Mj is invariant under every change of zhat_j: no bank or z-move at the common contact acts on
the resonance), Y'_+- are the target parts over T(l_+-) \ {j}, and E collects Hilbert terms (<= C D b/nu) and the coordinates of S_{l_+-}
that are not contacts.  Classify the private coordinates s of S_l at an (R1) stage: (a) s <= D(L): contacts or thin support;
(b) D(L) < s with v_l(s) > x'_max: unconstrained by (R1); (c) the pull range and the fully swallowed range [c r, x'_max]: anti-sign
contacts (C2); (d) v_l(s) < c r: total contribution <= 2 c r.  A FREE type-(b) coordinate with eta_s v_l(s) >= Des^C x is a two-sided
private value lever [SKETCH: K2.9 lists FR generators only at design depth].  Granting it,
      Mj(f) in Pat(L) + [-C N_L Des^C x - C D b/nu - 4 c r,  C N_L Des^C x + C D b/nu + 4 c r],
Pat(L) the FINITE set of pattern minors u_+(j)(P_- + Y'_-) - u_-(j)(P_+ + Y'_+) over all sign choices on the coordinates of types (a),
(b) and of T(l_+-) \ {j}.  Under the design addition
 (D-pat) every nonzero element of Pat(L) has modulus >= Des(L)^{C'} x(w) N_L for every clean sub-window w of L,
a tiny minor of such a pair forces an element of Pat(L) to vanish EXACTLY: the resonance is a coincidence of discrete design data up
to the lever scale x, not a codimension-one condition on f.
Proof.  Expand with Lemma 2.3; u_+(j) y_-(j) zhat_j - u_-(j) y_+(j) zhat_j = 0 since u_+-(j) = y_+-(j) (j lies in no signature set).  The
classification is H2 Thm H2.B(i), (C1)-(C2); (d) is the super-geometric tail of v_l; a free coordinate shifts v_l(s) z_s by eta_s v_l(s)
relative to sgn(z_s) v_l(s).  QED
REMARK 2.5 ((D-pat); HEURISTIC).  Elements of Pat(L) are finite expressions in delta_+-/n_+-, y_+-(.) and signs; one vanishes
identically only through a dyadic-rational relation between delta_+/n_+ and delta_-/n_-, excluded if the signature weights are
algebraically independent over the earlier design data (as T_fin does for block weights).  With 2^{K_L} patterns, a generic placement
stays >~ 2^{-K_L} from 0, far above x(w) ~ T_lo^4.  (D-pat) is a design proposal, not checked against every constraint of T_fin^{K2}.

### 4.4 Tuning-lever duality (HEURISTIC with PROVED ingredients)

A persistent (R1) row needs at every stage a tiny resonance of fresh carriers.  By 2.4, resonances through private data are discrete
coincidences up to the lever scale.  Any continuous datum able to tune a resonance at stage L -- a thick magnitude a_s (through
(mu*_s)^2 a_s/nu), a free z_s at a shared target or a type-(b) private coordinate with eta_s v >= Des^C x -- is itself a TWO-SIDED Step-A
generator (TS, FR), which every near-certificate must annihilate up to eps Design (K2.16(2),(4),(5)): Psi_y(s) = kappa_y a_s at thick s,
Psi_y(s) ~ 0 at free s.  In the restricted model of H2 Prop. 4.1 the certificate is the Farkas combination lambda^T C', and its action on
a continuous datum theta is d(lambda^T M)/d theta.  So at a residual stage lambda^T M is STATIONARY (to O(eps Design)) in every two-sided
continuous direction (modulo the scaling direction kappa) and one-signed in the one-sided ones: f sits at an approximate constrained
critical point of lambda^T M with a tiny critical value.  Either the tuning datum has effect >> eps Design (then it is a generator the
certificate must annihilate, an extra stationarity condition), or its effect is below eps Design (then it cannot move a nonzero
pattern minor, which is >= Des^{C'} x under (D-pat), to zero).  A construction therefore needs, at every stage, at least two
independent continuous data acting on the same resonance (one to make lambda^T M tiny, one to cancel its gradient): a larger
resonant group sharing coarse target coordinates.  I could not exhibit one; the parameter count alone is not decisive (eps ~
Design^{-C} is not small compared with b, so approximate critical values need not be design-robust).

### 4.5 The adversarial configuration that remains (SKETCH)

DEFINITION (stage configuration RC_L).  At main stage L: an unshifted block m with a private two-sided peak resource; two FRESH coarse
carriers l_+ in K^+, l_- in K^- of kind (iv) (near coordinates data-sign contacts; pull ranges and [c r, c_0 W] anti-sign contacts:
fully swallowed, no pull capacity, H2 5.3; deep-swallowed on [cap'_min/2, x''_max] in the sense of G2-ref Thm 4.9' (P-res'), otherwise
G2-ref Theorem ML' controls them);
a common target contact j; further target coordinates s*_1 in T(l_+), s*_2 in T(l_-) carrying THICK support, shared with fresh auxiliary
carriers k_1, k_2 of other blocks (needed by Interpretation (b) of Section 3: the pair must switch through shared thick targets);
oriented minor at the prepared row R_1 of the wrong sign and tiny, and -- by the scale dichotomy 5.3 -- EXACT at f up to below the
bias of every window of stage L (bias type: H2 Lemma 5.2 / G2 Prop. 4.7 push it to >= c theta_0/Design^C at R_1).
PERSISTENCE (SKETCH).  Choose the RC_L successively; open conditions (signs, statuses, "tiny") are kept by Lemma 2.1; exact resonances by
Lemma 2.2 with theta_L := a_{s*_i(L)} (own effect c_L ~ (mu*_{s*})^2 v/nu at stage L), triangular dependence on coarser tunings, and
cross effects eps_{LL'} (L' > L) bounded by doubly exponentially small Hilbert footprints of deeper tuning coordinates (cluster sweep,
H2 Lemma 2.3: s_max(L+1) >= 4/T_lo(L)); the weight conditions of 2.2 then hold if eps_{LL'} decays faster than the products of
c_i/(4 Lambda_i), i <= L' -- plausible, not checked.  NOT verified: (i) that the auxiliary carriers and blocks can be chosen without
creating relief elsewhere (new thick-type carriers (R0), anchors K2.17(b), two-sided private coordinates, margin levers of G2-ref ML');
(ii) the tuning-lever duality of 4.4 (the gradient condition at every stage); (iii) that a certificate exists for every clean
sub-window and class (the class depends on the mate); (iv) that one mate g in C(f) is active on all the pairs (C4), paying for the
switching on the shared thick targets as Theorem CL requires.  RC_L is a SKETCH of an adversarial row, not a construction.

### 4.6 Dangerous mates exist as limits

LEMMA 2.6 (upper semicontinuity of the fibre map).  PROVED.  If f_n -> f in S_{p*}, g_n in C(f_n) and g_n -> g, then g in C(f); every
sequence g_n in C(f_n) has a norm-convergent subsequence.
Proof.  ||(f_n, g_n)|| <= 1 and the operator norm is continuous, so ||(f, g)|| <= 1, i.e. g in C(f) (p*(f) = 1).  Compactness is global
compactness of the fibres (Preprint A Thm 2.1 / Part I).  QED
COROLLARY 2.7 (construction of dangerous mates).  PROVED (conditional on the approximants).  Let f satisfy RC_L with Mj_L(f) != 0 at
every large stage, and let f^(n) -> f agree with f except that the stage-L_n minor is EXACT, each with a mate g^(n) carrying exact
two-piece data that switch through the stage-L_n pair with amplitude >= c_0 (Prop. II-NTM-type data).  Every limit g of g^(n) lies in
C(f) (Lemma 2.6); by Cor. 1.8 g is pinned on the stage-L pair below max(|Mj_L(f)|, U_far)/C_f, and above that scale its switching is
close to that of g^(n) for the stages where f^(n) and f agree (compactness of the decomposition sets at fixed t).
Remark (transitivity).  If the rows f^(n) were recovered, then (f, rho g) would be in cl NA (the pairs (f^(n), rho g^(n)) are in cl NA
and converge).  So the natural dangerous mates are recovered as soon as the exactly-resonant approximants are; the adversary needs
the approximants to be residual too -- the bias type of RC (H2 Lemma 5.2, G2 Prop. 4.7).  Persistent residual rows come in families:
wrong-signed rows are limits of exactly-resonant (bias-type) rows, and both are outside the current chain.

## 5. Recovery by other means at residual rows

### 5.1 Non-recoverability is open on the graph

Let G := {(f, g) : f in S_{p*}, g in C(f)} (closed, Lemma 2.6) and cl NA the closure of NA((c_0, p), l_2^2) in the operator norm.

LEMMA 3.1 (openness).  PROVED.  If (f, h) is contractive and (f, h) notin cl NA, there is delta > 0 such that every contractive (f', h')
within delta of (f, h) is notin cl NA.  In particular, if (f, rho g) notin cl NA then for every row f' with p*(f' - f) < delta/2 at which
every mate is recovered,  dist(rho g, C(f')) >= delta/2.
Proof.  cl NA is closed, so B((f, h), delta) ∩ NA = {} for some delta; if (f', h') in cl NA were within delta/2 of (f, h), an NA operator
within delta/2 of (f', h') would lie in that ball.  If g' in C(f') with p*(g' - rho g) < delta/2, then (f', g') in cl NA (f' recovered)
lies within delta of (f, rho g) (operator norm <= p*(f' - f) + p*(g' - rho g)), a contradiction.  QED
COROLLARY 3.2 (what a counterexample must defeat).  PROVED.  A non-recovered (f, rho g) must stay delta/2-far from the fibres of ALL
rows near f in: (i) the rows with finite base support (Master Theorem VI); (ii) the comeager set Omega of points of lower
semicontinuity of the fibre map (Fort's theorem: f -> C(f) is usc with compact values, Lemma 2.6, and S_{p*} is complete; at f in Omega
every g in C(f) is a limit of mates of NA rows, so Omega consists of recovered rows); (iii) every row covered by the transport theorem,
in particular every row at which the residual fails at infinitely many main stages.  So a counterexample built on a persistent
residual row needs the residual to persist on a whole NEIGHBOURHOOD of f in the sense that every row f' near f carrying mates near
rho g is again a persistent residual row.  A codimension-one coincidence at each stage does not have this property unless the mates
force it -- and they can: by Lemma 1.7 / Cor. CL.2 mates near rho g force minors to be small at rows carrying them (Cor. 1.8 (1.3)).
This does not exclude a counterexample, but it shows that a counterexample is a property of the PAIR (rows with active mates force
their own resonances), which is exactly the bias-type family of Cor. 2.7.

### 5.2 Wrong-signed minors above their scale: VT tolerance, and the bias obstruction

PROPOSITION 3.3 (a wrong-signed minor is harmless above its pinning scale).  PROVED mod chain (engineered-approximant machinery with
window bottom s_1', Lemma VT of U3/X2 and Theorem UE^inf, as in Part III).  In the configuration of Lemma 1.7, take exact data at the
companion with the pair active and the contact row at j NOT exactified (Mj != 0).  The side violation at j is
|V_j| = |gamma_1||Mj|/|u_2(zhat)| (S = 0 and psi_j = 0 for exact data), an l_1-violation of mass eps_j <= C_d |Mj| (C_d := A_max/|u_2(zhat)|,
A_max the data bound).  Lemma VT tolerates it iff 2 rho eps_j <= delta s_1'/16, which holds if
      s_1' >= 32 rho C_d |Mj| / delta.                                                                                   (3.1)
So windows above C|Mj| need NO exactification of Mj; by Cor. 1.8 the pair has order-one switching only at scales >~ |Mj|.
Proof.  Lemma 1.7 Step 3 with exact data; Lemma VT verbatim.  QED
THE OBSTRUCTION (PROVED as a chain of the cited design inequalities).  Part III requires
 (L-K2-1)  s_1 <= theta_0 T/(8 rho A_0),   theta_0 = b/Design^{C_P}        (K2 (K2-d), H2-ref F-NE),
because the Sys-DC levers must be two-sided at a scale r >= 16 K_J Pi_X (Pi_X the Hilbert footprint of the window masses) and, for
kind-(iv) carriers, two-sidedness comes from preparation banks of mass theta_0 with theta_0 eff >= r.  Wrong-signed minors with
|Mj| in (b T/Des^C, C b] violate (3.1) for every admissible s_1.  Moreover the preparation BIAS (H2 Lemma 5.2) shifts every banked
kind-(iv) value by theta_0 eff v >= r, so at the prepared row the minor is >= c r even if Mj(f) = 0, while (3.1) needs
|M| <= delta s_1/(32 rho C_d); the ratio bias/tolerance is >= 512 rho C_d K_J Pi_X/(delta s_1), a fixed large factor (Pi_X >= c s_1 when
window masses sit at near coordinates).

### 5.3 Scale dichotomy: the persistent residual is of exact/bias type (SKETCH)

CLAIM.  Fix a stage L and a resonant pair whose oriented minor at f is M := Mj_L(f) != 0 (contact minor of the wrong sign, or a strict
FR minor of either sign, Cor. CL.2).  For a window w = [s_1, s_2] of stage L:
 (i) [above] if s_1 >= 32 rho C_d |M|/delta and the preparation bias at w is <= delta s_1/(32 rho C_d), the minor needs no
     exactification (Prop. 3.3);
 (ii) [below] if s_2 <= c delta |M|/C_f and the preparation bias at w is <= |M|/2, then by Cor. 1.8 (resp. CL.2) the mate's switching on
     the pair satisfies |gamma(t)| <= C_f t/|M| <= c delta (absolute) for t in w; zeroing it changes the coarse data X(t) by O(delta) and
     the side rows by O(delta), after which the pair is INACTIVE and its minor enters no strict row, so the cone projection has a
     design-controlled Hoffman constant and the approximating mate moves by O(delta).
Hence the pair obstructs only windows that straddle [c delta |M|, C|M|/delta] or whose bias exceeds min(|M|/2, VT tolerance).  If stage L
has a window below c delta |M| with small bias, the pair is harmless at stage L.  A persistent residual therefore needs, at all large
stages, resonances that are EXACT up to the scale range and bias range of their stage (|M_L(f)| below c delta T_lo(L)/C_f or below the
bias of every low window): exactly the bias type of G2 Prop. 4.7 / Cor. 4.8, where the obstruction is the bias, not the minor.
Status SKETCH: (ii) needs that the class/cube machinery (K1 Lemma K1.2, Part III Prop. II-ray) accept as inactive a carrier whose
switching is small in ABSOLUTE terms (<= c delta) but large relative to t (>> K_* t), with an O(delta) absolute error in the
approximating mate; the transport theorem is written with errors in units of t, and this re-bookkeeping was not checked.  It also
needs one window that is good for all resonant pairs of the stage simultaneously (finitely many pairs per stage).

### 5.4 Heavy thick masses: no invisible pre-modification for (R0)

LEMMA 3.4 (thick masses are heavy).  PROVED mod chain (K2.16(4); window scales below the design constants, (D-G1a)).  At an (R0) stage
the thick private coordinates p of a thick-type carrier have |a_p| >= u(w)/2 (after the deep raise, which changes masses by a factor
in [1/2, 2]).  Let f' be the normalized row obtained by changing a_p to (1 + u) a_p (u := u(w)) -- the move that creates robust spread
(K2.17(e)) and destroys every near-certificate -- and assume |a_p| <= 1 - c_0 (a_p is not essentially all of the base mass; otherwise
the move is a rescaling, undone by normalization).  Then the base vectors satisfy
      ||U^*(a' - a)|| >= mu*_p |a'_p - a_p| >= mu*_p c_0 u |a_p| (1 - O(u)) >= c_0 u(w)^2 / (3 Design(L)^{1/2})
((mu*_p)^2 >= 1/Design(L) at design depth), which exceeds s_1(w)^2 by a design factor.  The raise-transfer error contains
2||U^*(a' - a)|| (V3 Lemma 2.3), so no pre-modification of f that breaks an (R0) resonance is invisible to the window data (transfer
error << s_1^2).  The stable-exact direction Phi_0 of J1 7.4(c) (p*(f + t Phi_0) <= 1 + C t^2) keeps the base vector up to normalization,
i.e. moves it by O(t^2): it cannot serve as such a modification either.
Proof.  Thickness: |a_p| >= u/2 by definition (J1 1) and K2.16(4).  Normalization: q*(a + u a_p e_p) = 1 + u|a_p| + O(mu*_p u |a_p|), so
a'_p - a_p = u a_p (1 - |a_p|) + O(u^2 |a_p|) + O(mu*_p u|a_p|), of modulus >= c_0 u |a_p| (1 - O(u)) >= c_0 u^2 (1 - O(u))/2; and
||U^* x|| >= mu*_p |x_p| for the diagonal base.  For Phi_0: f + t Phi_0 = a + L^*(w + t rho~) has the same base vector before
normalization, and the normalization changes it by O(t^2).  QED
So "other means" for (R0) would have to use Phi_0 inside the companion (J1's gauge, J1 7.3, SKETCH there) -- not pursued here.

### 5.5 Raise transfer, Theorem N, transitivity (assessment)

- Raise transfer (V3 Lemma 2.3) moves only same-sign masses, with constant errors 2||U^* Delta a|| + p*(L^*(w^# - w)); it transfers mates
  exactly only above the scale (error)^{1/2}, and cannot change the SIGN data that fix a private resonance (Cor. 2.4) nor, except
  two-sidedly, the thick-target Hilbert data that the certificate annihilates (4.4).  No relief.  HEURISTIC (PROVED ingredients).
- Theorem N (box-dominated support) needs F = N and Bx <= C_a |a| with a margin rate; a persistent (R1) row is thin (<= b) off the
  targets at every stage (C1), so its box ratios are unbounded unless the mate's boxes are thinner still; it does not apply to the
  dangerous mates, whose switching lives on contacts and shared thick targets.  HEURISTIC.
- Transitivity (Cor. 2.7 remark): the natural dangerous mates are limits of mates of exactly-resonant rows, which are bias-type
  residual (H2 Lemma 5.2, G2 Prop. 4.7); transitivity gives nothing new.  PROVED as stated.
- Direct finite-support approximants: rows with finite base support are recovered (Master Theorem VI), and by Lemma 3.1 a
  counterexample stays delta/2-far from all their fibres near f; whether truncations f_n of f carry mates converging to g is
  exactly (LSC-trunc) and was not decided.  OPEN.

## 6. The precise remaining property (Q*); relation to G1, G2 and G2-ref

(Q*) (OPEN).  At a stage of bias type (the only kind that can persist, by 5.3), with resonant kind-(iv) rows R:
      bias(Sys-DC levers on R) + |lambda^T M(f)|  <=  delta s_1^{VT}/(32 rho C_d),
s_1^{VT} the window bottom used by Lemma VT, compatibly with the lever-scale requirement r(s_1^{VT}) >= 16 K_J Pi_X of Sys-DC.
Equivalently: the minimum over two-sided d-consistency levers for R of (lever bias)/(lever range) is <= delta/(512 rho C_d K_J), i.e.
BIAS-FREE two-sided levers exist for the resonant rows.  A persistent (R1) row needs (Q*) to fail at all large main stages.
Known sources of bias-free control, and where they stop:
 (a) G2-ref Theorem ML' (PROVED mod chain; it replaces G2's Theorem ML, which G2-ref found not proved as stated): a pinned or locked
     kind-(iv) row with a pullable coordinate at depth [cap'_min/2, x''_max] is controlled.  (Q*) can fail only at rows that are
     deep-swallowed over the whole certified range (G2-ref Theorem 4.9', (P-res')).
 (b) G1 Lemma 4.4: a move at a coordinate j does not change, to first order, a minor containing the row of j; G1's split preparation
     P^nat lowers the bias on strict objects to b_bias = b T_hi (Des/u)^C << b, which is still above the VT tolerance
     delta s_1/(32 rho C_d) because s_1 <= b T/(8 rho A_0 Des^{C_P}) by (L-K2-1).
 (c) Cor. 2.4: banks at the common contact j are bias-free on Mj (Mj does not depend on zhat_j), but for the same reason they do not act
     on the resonance.
NORM-LEVEL READING OF THE RESIDUAL.  A deep-swallowed carrier has anti-sign far mass U_far <~ x''_max, far below the window scales, so
by Cor. 1.6 it is NOT pinned at any window scale; by Theorem CL its order-one data-sign switching must be paid by negative
zhat-weighted switching on thick support, which at an (R1) stage lies only at shared target coordinates (Interpretation (b) of
Section 3).  So the residual, in norm terms, is: a mate whose order-one switching on fresh deep-swallowed kind-(iv) rows is paid for by
switching on shared thick target support, at rows where the corresponding resonance is exact (bias type), and where no lever is both
two-sided at the scale K_J s_1 and bias-free at the scale delta s_1.  (Answer to G2-ref's suggested test (2): RC_L's carriers must be
deep-swallowed on [cap'_min/2, x''_max], which is a condition on their private signature coordinates and is compatible with the
other requirements of RC_L; nothing in RC_L forces it or excludes it.)
Relation to G1's remaining strict resonances (R-S1)/(R-S2) (minors made of (X3) rows and (X1-FR) rows): by Cor. CL.2 every mate is
pinned on such a pair below eta_j |M| for both signs of M, so the dichotomy 5.3 applies verbatim, and again only exact resonances
can persist.  This is consistent with G2 Prop. 4.7 / Cor. 4.8 (confirmed by G2-ref): exact one-signed resonances obstruct through the
error scale of the realization, not through the size of the minor.

## 7. Numerics (sanity checks only; r14/G3_work/)

model.py: finite one-block Martin-type model on R^n: q*(A) = ||A||_1 + ||mu A||_2, N(W) = ||W||_inf + ||Phi W||_2, forced data of a row
f[a, z], p*(.) by SOCP, and max_switch(t, k): the maximum of gamma'_k over g with g(xi) = 0 and decompositions of f +- t g with norms
<= s(t) -- exactly the quantity bounded by Lemmas 1.5-1.7, 2.8.  Solver CLARABEL (cvxpy); values flagged "optimal_inaccurate" (small t,
where s(t) - 1 ~ t^2/2 reaches the solver tolerance) are not used.
selfpin.py / selfpin.out (re-run with the corrected peak carrier 4): pair l_+ (eps = +1), l_- (eps = -1) of strict non-peaks sharing
the contact j; peaks {2, 3, 4} with private contacts of both orientations ((P1)); p*(f) = 1.00000000 in every case.
   configuration (anti-aligned coordinate r of l_-)        max gamma'_+ at t = 0.1, 0.03, 0.01      reading
   D = +2.05e-3 (wrong sign), r of mass 0                  1.85, 0.62, 0.21  (slope ~20)          pinned by j (Lemma 2.8(c))
   D = 0, r a CONTACT                                      1.37, 0.42, 0.14  (slope ~14)          pinned by r (Cor. 2.9 / 2.11)
   D = 0, r THIN support a_r = 1e-4 (cushion scale 0.032)  1.43, 0.64, 0.80; 1.89 at t = 3e-3   pinned above the cushion scale, relieved below
   D = 0, r THIN support a_r = 1e-3 (cushion scale 0.10)   2.03, 1.87, 1.76                      relieved (below the cushion scale)
   D = 0, r THICK support a_r = 0.15                       2.14, 1.87, 1.76                      FREE
   D = -1e-3 (right sign), r THICK                         2.21, 2.03, 1.96                      FREE
   D = -4e-3, r THICK: l_- becomes a PEAK (peaks {1,2,3,4}) 1.68, 0.57, 0.19 (slope ~19)          outside Lemma 2.8 (l_- not a strict non-peak)
   (The cushion scale is (8 q_0 alpha)^{1/2} of Cor. 2.9 with alpha the normalized a_r; the free level ~2 is, HEURISTICALLY, the
   curvature bound of the l_2 part of the block norm on Theta_- - Theta_+.  Values below t = 0.01 are mostly 'optimal_inaccurate'.
   The last line replaces part 3's stale entry "D = -0.004 FREE", computed before the peak-carrier fix.)
tworegime.py / tworegime.out (thick anti-aligned r): D = 1e-3 (wrong sign): max gamma'_+/t = 41.1 at t = 0.03 and 0.01 (Lemma 2.8(c)
slope |val_-|/(2 q_0 D) = 33.3 plus the O(S_0) terms): PINNED; D = 1e-4: max gamma'_+ = 1.85, 1.74 at t = 0.03, 0.01 (free regime t >> D),
decreasing to 1.49, 1.06 at t = 1e-3, 3e-4 (approaching the pinned regime; inaccurate solves, which even exceed the Lemma 2.8(c)
bound ~ 41 (1e-3/D) t there, so they are not evidence either way); D = 0 and D = -1e-4: free.  The two-regime profile of Cor. 1.8 is
visible at the accurate scales.
conserve.py / conserve.out (Theorem CL): in all five configurations and at t = 0.1, 0.03, 0.01, |V(zhat)| <= 2(s(t) - 1)/(q_0 t) and the
|z|-weighted form of (CL2) hold, with V recomputed as L^*(Theta_- - Theta_+) to 2e-4.  The bound is driven by the predicted term: O(t) when
r is a contact (LHS 0.0095 at t = 0.01), the cushion term 4 alpha/t when r is thin (RHS 0.66 at t = 0.01), the thick switching when r
is thick (t = 0.01: LHS 0.083, thick part 0.073, RHS 0.086).
Conclusion: consistent with every PROVED statement at the scales where the solver is accurate; the numerics prove nothing about the
infinite-dimensional question.

## 8. Conclusion and next steps

STATUS.  (LSC-trunc)_N for every f and density of NA((c_0, p_N), l_2^2) remain OPEN.  No first row with a persistent residual was
constructed; RC_L is a SKETCH whose unverified points are listed in 4.5.  No counterexample is claimed, and none is suggested: every
mechanism examined that could make a residual persist either self-pins at the norm level (Sections 2-3) or reduces to the bias of the
realization (Sections 5-6), which is a property of the method, not of the mates.  Leaning: POSITIVE.
MAIN OBSTACLE.  Exactness versus one-sidedness at bias-type stages: fresh deep-swallowed kind-(iv) rows in an exact one-signed
resonance, whose mates switch through shared thick target support, and for which no lever is simultaneously two-sided at the
lever scale K_J s_1 and bias-free at the VT scale delta s_1 ((Q*)).
NEXT STEPS.
 1. Bias-free levers at shared thick targets.  Theorem CL says the active deep-swallowed rows switch through shared thick target
    coordinates; these carry thick mass, i.e. two-sided TS moves.  Test whether a TS move at a shared thick target whose ROW lies in
    the resonant minor is bias-free in the sense of G1 Lemma 4.4 and two-sided at the scale K_J s_1; if so, (Q*) holds and the (R1)
    residual is removed.
 2. Make the scale dichotomy 5.3 rigorous: re-run the transport bookkeeping (K1 Lemma K1.2, Part III Prop. II-ray) with an ABSOLUTE
    error class for carriers pinned in absolute terms (|gamma| <= c delta at all window scales).  Then every persistent residual is of
    exact type, and the remaining work is exactly G2 Prop. 4.7's setting.
 3. Use the mate itself: its decompositions at a window scale give, by Lemma 1.4 and Theorem CL, an explicit near-solution of the
    switching system with error O(t) + O(alpha/t).  Pair it with a near-certificate of Sys-A (which annihilates the TS generators at
    thick targets, Psi_y(s) = kappa_y a_s) to look for a contradiction "near-certificate + active mate paid by thick targets".
 4. Check (D-pat) against the constraints of T_fin^{K2} (Remark 2.5).
 5. Numerics: groups of three or more carriers sharing two thick targets in the SOCP model, to probe whether an exact resonance can
    coexist with order-one switching paid by the shared thick targets (the infinite-dimensional bias question is not testable this way).
