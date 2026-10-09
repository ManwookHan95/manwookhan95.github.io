# R3 notes — Attempted counterexample via far rigidity / approximate-resonance switching (O3), and the mechanism that defeats it

Round 3, task R3. Setting: canonical base q, Martin's norm with a FINITE block set I (the norms p_N; Preprint B Remark martin-tail);
"admissible T" = Lemma B's conclusion only. Imports (refereed): A_notes §1 (Facts A-F), Def 4.1, Lemmas 4.3-4.4, Prop 4.5, Lemma 4.7,
Cor 3.3; N_part1 Thm 1 (Ls(f)); N2 Lemma 1.4 (base excess at NA points), Lemma 1.5 (convergence of engineered approximants), Theorem 4
(averaging at an approximant); E Prop 8.2 (window moves along NA sequences are o(1)), E 4.1 (Model N). Part files R3_part1..5.md;
scripts ctx/r3/work/*.py. Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN / NUMERICAL.

## 0. Answer
**No counterexample.** The rigid design cannot be made into one: it fails at a precise point, and the failure is a new recovery
mechanism that works for every admissible T. The mechanism is ERROR CARRYING (EC). Window moves of sup-norm o(1) on free coordinates
turn generic block coordinates, taken from the dense tails, into strict non-peaks with w'' = 0 at engineered NA approximants. These
coordinates carry, two-sidedly, every component of the frozen and transport errors whose directions lie in a fixed finite-dimensional
space. No approximation rate is needed. The reason: an error of size O(s) at scale s needs room only O(s^2). With EC the
bounded-conversion-capacity obstruction (the O3 core of BRIEFING_R2) disappears for compact error directions. E's Model N agrees:
R -> 1 even with a single converted carrier of one type. Before EC the values were R = 1.19 to 3.4.
What remains of O3 is a sharply restricted class (O3*): escaping, concentrated, recursively guarded critical errors. Nothing here
contradicts Lindenstrauss property B for l_2^2. Leaning: positive (density).

| # | Statement | Status | § |
|---|---|---|---|
| 1 | Theorem EC: rate-free conversion of generic coordinates by vanishing window moves (diagonal form, protected functionals) | PROVED | 2.1 |
| 2 | Room lemma: an O(s) error carried up to scale s needs depth >~ s^2 | PROVED | 2.3 |
| 3 | Proposition Z: scale-zero closure is trivial (every g in xi-perp is a limit of certificates with H -> 0 at NA approximants) | PROVED (J infinite) | 3.1 |
| 4 | Closure theorems must be multi-scale; an implant inequality would be needed; even then it cannot exclude carriable-error mates | PROVED (4a) / HEURISTIC (4b-d) | 3.2 |
| 5 | Disjoint block addition lemma | PROVED | 4.1 |
| 6 | Theorem 4-EC: averaging at an approximant needs many converted scales only for the NON-carried error remainder | PROVED (implication) | 4.2 |
| 7 | EC supplies the carried parts for any fixed finite-dimensional error space (quantifier order generic depth -> boundary) | PROVED | 4.3 |
| 8 | Contact lemma (all but r coordinates of a far set become contacts while r linear quantities are prescribed) | PROVED | 4.4 |
| 9 | E's rigid design (A1)-(A5) is recovered: EC + contacts + ONE converted carrier, modulo the transport hypothesis (HT-EC) | SKETCH | 4.5 |
| 10 | Model N with EC: R -> 1 (both types: 1.088/1.023/1.005; one type, one carrier: 1.168/1.041/1.009) | NUMERICAL | 4.6 |
| 11 | Exact first-order cost of inward use of a near-threshold peak: alpha_k = sigma delta Phi^2 M/C | PROVED | 4.7 |
| 12 | Residual class O3* (escaping, concentrated, recursively guarded critical errors) | OPEN | 5.1 |
| 13 | Chain-guard designs give unbounded conversion capacity; coarsest-guard observation | SKETCH (linear status model) | 5.2 |
| 14 | Some (f, rho g) with dist to NA > 0 | not found; no claim | 5.3 |
| 15 | Density of NA((c_0,p), l_2^2) | OPEN (leaning positive, strengthened) | 5.4 |

## 1. Setting and the task
Notation as in A_notes §1: lambda_{k,m} = m Phi_m(k), (R_m x)(k) = lambda_{k,m} u_{k,m}(x), R_m* w = sum_k lambda_{k,m} w(k) u_{k,m},
N_m(w) = ||w||_inf + ||D_m w||_2. For f in S_{p*}: normer xi, q_0, f = a + L*w, zhat = xi/q_0 = z + U e, F = supp a,
J := {j notin F : |z_j| < 1}, zeta_m = R_m** xi, M_m, C_m, peaks P_m. Fact C: k in P_m iff m|u_{k,m}(xi)| >= Phi_m(k) M_m |zeta_m|/C_m;
off P_m, w_m(k) = C_m m u_{k,m}(xi)/(Phi_m(k)|zeta_m|); zeta_m/|zeta_m| = alpha_m + D_m^2 w_m/C_m with alpha_m on P_m.
NA approximants (A Fact D, G_referee 4.7): f' = grad p(x'), x' = z' + U e', a' in c_00 cap S_{q*}, z' in B_{c_0}, z' = sign a' on supp a'.
N2 Lemma 1.5: a'_n -> a in l_1 and z'_n -> z coordinatewise imply f'_n -> f in norm with all forced data converging.
A counterexample is (f, g in C(f), rho < 1, delta, x_1..x_k) with max_i(rho g(x_i) - r~_{f'}(x_i)) >= delta for every NA f' with
p*(f' - f) < delta (A Cor 3.3; N2 5.1). The task asked for such an object built on E's rigid design (E 7.3: (A1) one-sided
near-threshold carriers u_k = (v + K lambda_k sigma_k + delta_k psi_{n(k)})/n_k of both peak types at all scales, core errors
sigma_k in a fixed finite-dimensional E_c on core window coordinates; (A2) far rigidity; (A3) Gordan sign obstruction;
(A4) destruction by disjoint detector groups; (A5) no critical-rate convertible generic carriers of E_c), with a proof covering
EVERY NA approximant. N2 4.5 (SKETCH) showed far rigidity is compatible with Lemma B. The only model-level evidence was Model N
(E 7.4: R(J) > 1 for every bounded number J of converted scales in the error-dominated regime).

## 2. Error carrying by generic coordinates
Fix a block m_0; write u_k, lambda_k, Phi(k) for u_{k,m_0}, lambda_{k,m_0}, Phi_{m_0}(k); ||.||_{inf->inf} = operator norm on l_inf^d.

### 2.1 Theorem EC. PROVED.
Let f in S_{p*} and let x'_N = z'_N + U e'_N be NA normer data with a'_N -> a in l_1, z'_N -> z coordinatewise. For each n let be given
(i) targets b_{n,1..d_n} in S_{q*} with b_{n,i}(zhat) = 0; (ii) a finite G_n subset J, gamma_n := 1 - max_{G_n}|z_j| > 0, and
eta_{n,1..d_n} in c_00(G_n), ||eta_{n,l}||_inf <= 1, with B_n := (b_{n,i}(eta_{n,l}))_{i,l} invertible, beta_n := ||B_n^{-1}||_{inf->inf};
(iii) a finite set Pi_n subset l_1 with phi(eta_{n,l}) = 0 (phi in Pi_n); (iv) Phibar_n > 0 and eps_n > 0 with
8(2 + ||U||) d_n beta_n eps_n <= min(gamma_n, 1/n). Then there are N(n) >= n, distinct k_{n,1..d_n} and eta'_n in span{eta_{n,l}} such that,
with x''_n := x'_{N(n)} + eta'_n:
 (a) ||u_{k_{n,i}} - b_{n,i}||_1 <= eps_n, Phi(k_{n,i}) <= Phibar_n;
 (b) ||eta'_n||_inf <= min(gamma_n, 1/n)/2; x''_n is NA normer data with base functional a'_{N(n)}; z''_n := z'_{N(n)} + eta'_n -> z
     coordinatewise; f''_n := grad p(x''_n) -> f in norm with all forced data converging; phi(x''_n) = phi(x'_{N(n)}) for phi in Pi_n;
 (c) u_{k_{n,i}}(x''_n) = 0, so each k_{n,i} is a strict non-peak of f''_n with w''(k_{n,i}) = 0, gap M''_n, d''(e_{k_{n,i}}) = 0;
 (d) for c in R^{d_n}, c''_n(c) := (0, omega), omega_{m_0} := sum_i (c_i/lambda_{k_{n,i}}) e_{k_{n,i}}, is a finite certificate at f''_n with
     g = sum_i c_i u_{k_{n,i}}, ||g - sum_i c_i b_{n,i}||_1 <= eps_n||c||_1, H <= ||c||_2^2/(m_0^2 C''_n), kappa = 0,
     r >= M''_n min_i lambda_{k_{n,i}}/(2||c||_inf); hence p*(f''_n + s g) <= 1 + s^2 ||c||_2^2/(2 m_0^2 C''_n) for |s| <= r.
*Proof.* (1) Choose K_n with 2^{-m_0-K_n} <= Phibar_n; by (T2) every tail of (u_k) is dense in S_{q*}, hence l_1-dense
(||.||_1 <= q*); pick k_{n,1} < ... < k_{n,d_n}, all >= K_n, with ||u_{k_{n,i}} - b_{n,i}||_1 <= eps_n. Then Phi(k) <= 2^{-m_0-k} <= Phibar_n.
(2) A_n := (u_{k_{n,i}}(eta_{n,l})) = B_n + E_n, entries of E_n bounded by eps_n, so ||B_n^{-1}E_n|| <= d_n beta_n eps_n <= 1/16 and
||A_n^{-1}|| <= 2 beta_n (Neumann series).
(3) For b in l_1, b(x'_N) = b(z'_N) + <U*b, e'_N> -> b(zhat): dominated convergence, and e'_N -> e because U*a'_N -> U*a with ||U*a|| = nu > 0.
Choose N(n) >= n with 4 d_n beta_n max_i|b_{n,i}(x'_{N(n)})| <= min(gamma_n,1/n)/4 and |z'_{N(n)}(j) - z_j| <= gamma_n/4 on G_n.
Then |z'_{N(n)}| <= 1 - 3gamma_n/4 on G_n, so G_n misses supp a'_{N(n)} (z' = sign a' there).
(4) v_n(i) := u_{k_{n,i}}(x'_{N(n)}), s_n := -A_n^{-1} v_n, eta'_n := sum_l s_{n,l} eta_{n,l}. As ||x'_N||_inf <= 1 + ||U||,
|v_n(i)| <= |b_{n,i}(x'_{N(n)})| + eps_n(1+||U||), and ||eta'_n||_inf <= d_n||s_n||_inf <= 2 d_n beta_n(max_i|b_{n,i}(x'_{N(n)})| + eps_n(1+||U||))
<= min(gamma_n,1/n)(1/8 + 1/4). By construction u_{k_{n,i}}(x'_{N(n)} + eta'_n) = 0, and phi(eta'_n) = 0 for phi in Pi_n.
(5) z''_n is in c_0, equals z'_{N(n)} off G_n, and |z''_n| <= 1 - gamma_n/4 on G_n; z''_n = sign a'_{N(n)} on supp a'_{N(n)}. By Fact D,
x''_n is NA normer data with base functional a'_{N(n)} and f''_n is in NA cap S_{p*}. Coordinatewise z''_n -> z (N(n) -> infinity and
||eta'_n|| -> 0), so N2 Lemma 1.5 gives (b).
(6) The normer is xi''_n = x''_n/p(x''_n) and (R_{m_0}**xi''_n)(k_{n,i}) = 0. Fact C at f''_n: the peak condition
m_0|u_k(xi'')| >= Phi(k)M''|zeta''|/C'' > 0 fails, so w''(k) = C''m_0 u_k(xi'')/(Phi(k)|zeta''|) = 0, gap M''; d''(e_k) = Phi(k)^2 w''(k)/C'' = 0.
(7) c''_n(c) satisfies A Def 4.1 (b = 0; omega in c_00 off the peaks); d = sum_i (c_i/lambda_i)Phi_i^2 w''(k_i)/C'' = 0;
g = sum_i c_i u_{k_i}; H = (||D omega||^2 - d^2)/C'' = sum_i (Phi_i c_i/lambda_i)^2/C'' = ||c||_2^2/(m_0^2 C''); kappa = 0; in r(c) only
gap(omega)/(2||omega||_inf) is finite and ||omega||_inf <= ||c||_inf/min_i lambda_{k_i}. A Prop 4.5 gives the last claim. QED.

### 2.2 Remarks. PROVED unless marked.
(1) No rate. The precision eps_n is constrained only by (iv), which involves the fixed data (d_n, beta_n, gamma_n). The depth bound
Phibar_n can be chosen first and arbitrarily small. Lemma B allows the adversary to control approximation rates, but that only makes
the chosen coordinates deep, which affects nothing in (b)-(d) except the radius.
(2) Hypothesis (ii) is linear algebra: suitable eta's exist iff no nontrivial sum_i mu_i b_{n,i}|_{G_n} lies in span{phi|_{G_n} : phi in Pi_n}.
(3) Protected functionals keep chosen scalars of the approximant fixed: v(x'), the values u_{k,m}(x') of finitely many designated carriers
(their strict statuses are then kept for n large), group scalars.
(4) EC is the rigorous form of E's counter-strategies (C1)/(C3) and of A Lemma 8.2. It converts through WINDOW moves of size o(1),
which E Prop 8.2 allows (that result forbids only moves bounded below), so it needs no far tails. Far rigidity (N2 4.5) is therefore
irrelevant. The targets may also depend on n (diagonal form).
(5) If J is finite, contacts j in K can be pulled inside first (z'_n(j) := (1 - gamma'_n)z_j, gamma'_n -> 0) and then used. SKETCH (routine).

### 2.3 Room lemma. PROVED.
In 2.1, let ||c||_inf <= kappa s and lambda_gen,n := min_i lambda_{k_{n,i}}. If s^2 <= M''_n lambda_gen,n/(2kappa), then
p*(f''_n + t g_{c''_n(c)}) <= 1 + t^2 d_n kappa^2 s^2/(2 m_0^2 C''_n) for |t| <= s.
*Proof.* r >= M''lambda_gen/(2 kappa s) >= s; H <= d_n kappa^2 s^2/(m_0^2 C''). QED.
Reading: an error of size kappa s carried up to scale s needs carriers of depth >~ 2 kappa s^2/M, which is quadratically finer than the
scale. C's "implant scale gap" (an implanted carrier at depth Phi covers scales <~ Phi, while the slack starts at ~sqrt(Phi)) concerns O(1)
components. It does not obstruct carrying O(s) errors.

## 3. The closure route
### 3.1 Proposition Z (scale-zero closure is trivial). PROVED.
Let f in S_{p*} with J infinite, m_0 in I, g in X* with g(xi) = 0. There are NA f''_n -> f and finite certificates c_n at f''_n (block m_0,
base part 0) with ||g_{c_n} - g||_1 -> 0, H(c_n) -> 0, kappa(c_n) = 0.
*Proof.* Assume g != 0; let x'_N be any NA data as in 2.1. Take d_n -> infinity, r_n -> 0 with r_n <= q*(g)/(4(2+||U||)), and distinct
j_{n,1..d_n} in J with sum_l |g_{j_{n,l}}| <= r_n/2 (J infinite, g in l_1). Put zhat_j := z_j + (Ue)_j (|zhat_j| <= 1+||U||),
y_{n,i} := g + r_n(e*_{j_{n,i}} - zhat_{j_{n,i}} a), b_{n,i} := y_{n,i}/q*(y_{n,i}), eta_{n,l} := e_{j_{n,l}}, G_n := {j_{n,l}}, Pi_n := empty.
Then y_{n,i}(zhat) = 0 (a(zhat) = 1, g(zhat) = 0). Also q*(e*_j - zhat_j a) <= 2(2+||U||), so q*(y_{n,i}) is in [q*(g)/2, 2q*(g)]. Since
G_n misses F, y_{n,i}(eta_{n,l}) = g_{j_{n,l}} + r_n delta_{il}, i.e. Y_n = r_n I + 1 gamma^T with ||1 gamma^T||_{inf->inf} = sum|gamma_l| <= r_n/2, so
||Y_n^{-1}|| <= 2/r_n and beta_n <= 4q*(g)/r_n. Choose Phibar_n := 1/n and eps_n from (iv); apply Theorem EC; take c_i := q*(y_{n,i})/d_n.
Then sum_i c_i b_{n,i} = g + (r_n/d_n) sum_i (e*_{j_{n,i}} - zhat_{j_{n,i}} a), within r_n(2+||U||) of g, and ||g_{c_n} - sum c_i b_{n,i}|| <= 2 eps_n q*(g).
H(c_n) <= ||c||_2^2/(m_0^2 C''_n) <= 4q*(g)^2/(d_n m_0^2 C''_n) -> 0 since C''_n -> C_{m_0} > 0. QED.
(If J is finite, the same with d fixed gives H(c_n) <= 4q*(g)^2/(d m_0^2 C) + o(1).)

### 3.2 Consequences
(a) PROVED. Any set K_0(f) defined through second-order data at the normers of approximants (g in K_0(f) whenever g = lim g_{c_n} with
certificates c_n at NA f_n -> f and limsup H(c_n) <= 1) contains the whole hyperplane {g(xi) = 0} (when J is infinite), so it contains
C(f) and separates nothing. A closure theorem Ls(f) subset K(f) must use positive scales: the radii of the new structure and the slack
scale sqrt(p*(f' - f)).
(b) HEURISTIC/OPEN. The natural multi-scale ingredient would be an implant inequality: block coordinates whose status differs
between f and f' carry, two-sidedly at scale t, at most C p*(f' - f)/t. It is not provable for admissible T in general, because L* is not
bounded below and a conversion can be compensated by other status changes or cancellations among nearly parallel u_k.
(c) Arithmetic, given (b). Even an implant inequality allows carrying kappa t at scale t up to t ~ sqrt(eps/kappa) (the room lemma needs
room kappa t^2 <= C eps), which is the slack scale. So it can constrain only components carried with size >> t at scales << sqrt(eps).
For O3 mates the switching component is carried by f's own structure (matched, or converted at the boundary); only its errors are
O(t). An implant-type closure theorem therefore cannot exclude O3 mates whose errors EC can carry.
(d) HEURISTIC. A valid K(f) would have to encode that two-sided critical-rate carriers of the switching component cannot be re-created
near the destruction boundary. By (c) and §4, this can only come from the escaping part of the boundary errors (§5).

## 4. Error carrying in the averaging argument; the rigid design
### 4.1 Disjoint block addition. PROVED.
Let f'' in S_{p*}, S a finite set of strict non-peaks of block m_0 of f'' with w''_{m_0} = 0 on S, W in V* with W_{m_0} = 0 on S, and omega in
c_00(S) with ||omega||_inf <= ||W_{m_0}||_inf. Then N_{m_0}(W_{m_0} + omega) <= N_{m_0}(W_{m_0}) + ||D omega||^2/(2||D W_{m_0}||).
*Proof.* Disjoint supports: ||W + omega||_inf = ||W||_inf, ||D(W + omega)||^2 = ||DW||^2 + ||D omega||^2, and sqrt(A^2+B^2) <= A + B^2/(2A). QED.
For omega = t sum_{k in S}(c_k/lambda_k)e_k: R_{m_0}*omega = t sum_k c_k u_k, ||D omega||^2 = t^2||c||_2^2/m_0^2; the condition reads
|t||c_k| <= lambda_k ||W_{m_0}||_inf (room).

### 4.2 Theorem 4-EC. PROVED (as an implication).
Let f in S_{p*}, g in C(f), rho in (0,1), T_0 in (0, sqrt((1-rho^2)/2)], f'' in NA cap S_{p*}, and m_0, S as in 4.1. Let gbar, h_1..h_J in X*,
scales s_j = s_1 2^{j-1} <= T_0 and constants Q, Q_S, kappa_T, kappa_F >= 0 satisfy:
 (HC) p*(f'' + t h_j) <= 1 + Q t^2/2 for |t| <= s_j;
 (HT-EC) for s_1 <= |t| <= T_0: f'' + t gbar = A_t + L*W_t + t y_t with max(q*(A_t), ||W_t||_{V*}) <= 1 + Q t^2/2, W_{t,m_0} = 0 on S,
   ||D_{m_0}W_{t,m_0}|| >= C''_{m_0}/2, ||W_{t,m_0}||_inf >= M''_{m_0}/2, and y_t = sum_{k in S} c_k(t)u_k + e_t with p*(e_t) <= kappa_T|t|;
 (HE-EC) h_j - gbar = sum_{k in S} c^j_k u_k + e^j with p*(e^j) <= kappa_F s_j;
 (Room) for all j and s_j < |t| <= T_0: ||c(t) + c^j||_2^2 <= Q_S m_0^2 C''_{m_0}/2 and |t||c_k(t) + c^j_k| <= lambda_k M''_{m_0}/2;
and Q + Q_S <= 1 - 3(1-rho^2)/8, kappa_T <= (1-rho^2)/16, J >= 32 kappa_F/(1-rho^2). Then g' := (1/J) sum_j h_j satisfies
p*(f'' + t g') <= s(t) for |t| <= T_0. If moreover p*(f'' - f) <= (1-rho^2)T_0^2/6 and p*(g' - rho g) <= (1-rho^2)T_0/6, then g' is in C(f'')
and (f'', g') is in NA.
*Proof.* p*(f'' + t g') <= (1/J) sum_j p*(f'' + t h_j). If s_j >= |t|, use (HC). If s_j < |t|: f'' + t h_j = [A_t + t(e_t + e^j)] + L*[W_t + omega],
omega := t sum_{k in S}((c_k(t) + c^j_k)/lambda_k)e_k in block m_0. Fact A, the triangle inequality and Lemma 4.1 (room: ||omega||_inf <= M''/2
<= ||W_{t,m_0}||_inf) give p*(f'' + t h_j) <= 1 + Qt^2/2 + t^2||c(t)+c^j||^2/(m_0^2 C'') + kappa_T t^2 + kappa_F|t|s_j
<= 1 + (Q + Q_S)t^2/2 + kappa_T t^2 + kappa_F|t|s_j (using p* <= q* for the base part). Average, with sum_{s_j<|t|} s_j <= 2|t|:
p*(f'' + t g') <= 1 + t^2[1/2 - 3(1-rho^2)/16 + (1-rho^2)/16 + (1-rho^2)/16] = 1 + t^2[1/2 - (1-rho^2)/16] <= s(t), because
s(t) >= 1 + t^2/2 - t^4/8 and t^2 <= (1-rho^2)/2. For |t| >= T_0 use the slack (A Lemma 4.7) as in N2 Thm 1 Step 7. N_part1 Lemma 1.2(a)
gives (f'', g') in NA. QED.
Meaning: compared with N2 Theorem 4, the frozen errors h_j - gbar and the transport errors y_t are split into a part carried by finitely
many generic strict non-peaks S (quadratic cost Q_S) and a remainder. Only the frozen remainder kappa_F needs averaging over many
converted scales. If kappa_F <= (1-rho^2)/32, then J = 1 suffices: a single converted band.

### 4.3 EC supplies the carried parts for compact error directions. PROVED.
Let E be a finite-dimensional subspace of zhat-perp with basis b_1..b_d in S_{q*}, satisfying hypothesis (ii) of Theorem EC on a fixed finite
G subset J modulo a fixed finite Pi; put beta_T := ||(B^T)^{-1}||_{inf->inf}, B := (b_i(eta_l)). For any NA data x'_N -> zhat and any
Phibar_n, eps_n -> 0 with (iv), Theorem EC gives f''_n -> f with generic strict non-peaks S_n = {k_{n,i}}, w'' = 0 on S_n, Pi-values unchanged.
Every y in E is y = sum_i c_i u_{k_{n,i}} + e with ||c||_inf <= beta_T||y||_1 and ||e||_1 <= d beta_T eps_n||y||_1.
*Proof.* Write y = sum_i mu_i b_i; then (y(eta_l))_l = B^T mu, so ||mu||_inf <= beta_T max_l|y(eta_l)| <= beta_T||y||_1. Take c := mu and
e := sum_i mu_i(b_i - u_{k_{n,i}}). QED.
Quantifier order (this is what defeats the adversary's control of rates): choose the generic depth first (Phibar_n, hence
lambda_gen,n := min_i lambda_{k_{n,i}}). Then choose the destruction boundary lambda_b and all scales s_j so small that every error to be
carried (size <= kappa t at scales t <= T_n) satisfies the room condition |t| beta_T kappa t <= lambda_gen,n M''/2, i.e.
T_n <= sqrt(lambda_gen,n M''/(2 beta_T kappa)). For the frozen error of size kappa lambda_b it suffices that
t <= tau_F := lambda_gen,n M''/(2 beta_T kappa lambda_b). Both T_n and tau_F/lambda_b tend to infinity as lambda_b/lambda_gen,n -> 0
(T_n relative to lambda_b, i.e. T_n/lambda_b -> infinity). Then Q_S = O(T_n^2) -> 0 and the carried parts of kappa_T, kappa_F are
O(d beta_T eps_n kappa) -> 0.

### 4.4 Contact lemma. PROVED.
Let G be finite, Lambda: R^G -> R^r linear, and c in Lambda([-1,1]^G). Then some y in [-1,1]^G with Lambda y = c has at most r coordinates in
(-1,1). *Proof.* P := {y in [-1,1]^G : Lambda y = c} is a nonempty polytope; at a vertex the active constraints have rank |G|, and the
equalities contribute rank <= r, so at least |G| - r box constraints are active. QED.
Use: on a far set G, all but r coordinates become contacts z'_j = +-1. They carry masses of sign z'_j, so the base absorbs, two-sidedly
and at zero first-order cost, every small multiple of a vector supported there that vanishes at the normer (N2 Lemma 1.4). At the same
time r linear quantities are prescribed (group scalars, values of designated carriers). Components along a vector not vanishing at the
normer are moved into the a''-direction; their total is fixed by g'(x'') = 0. This last step is routine and SKETCH-level.

### 4.5 The rigid design of E 7.3 is recovered. SKETCH (rigorous ingredients 2.1, 4.1-4.4; open ingredient (HT-EC)).
Quantifier order: rho -> T_0 (from f) -> stage n -> window -> generic depth -> boundary -> far choices.
 1. Window. Take x'_N matched on a window that contains the supports of E_c, v and a. Core coordinates satisfy |z| <= 1 - gamma_0 and lie
    off F, so they are in J. E_c cap zhat-perp satisfies (ii) of Theorem EC modulo Pi = {v, finitely many designated carriers}, given the
    generic position of E_c relative to v (errors are complements of v by definition).
 2. EC. Apply Theorem EC with targets a basis of E_c cap zhat-perp. This gives generic strict non-peaks S_n at depth <= Phibar_n with
    w'' = 0. The precision eps_n -> 0 needs no rate, so (A5) is void.
 3. Boundary. Choose a detector group n_b whose conversion band lies at depth lambda_b << (1-rho^2)lambda_gen,n (4.3); groups exist at
    arbitrarily small scales (E 4.4). Keep the coarser groups matched (z' = z on their detectors). Make all coordinates of G_{n_b}
    contacts with small masses (O(T_0 x detector mass), hence o(1)). Choose the signs by 4.4 so that the group scalar s_{n_b} converts a
    band; finer groups are destroyed (z' -> 0). If psi_{n_b} is a single coordinate, then s_{n_b} is in {1 - z_j, -1 - z_j}. In that case
    use the absolute shift V = v(x'' - zhat) (a window move orthogonal to the protected functionals, of size o(1)) to place at least one
    carrier of one type in the band. Finally re-solve the EC system with a tiny window move protected against the band carriers. The
    contact masses change e'' by O(T_0 theta lambda_b), which is << theta Phi_gen, so S_n stays converted.
 4. Band certificate. Let h be rho times the switching component, carried by the converted band carrier(s); it is exact and two-sided
    for |t| <= s_1 ~ lambda_b. Its frozen error h - gbar has three parts: (E_c part, size K lambda_b) is carried by S_n (4.3); (detector
    part) lives on the contacts of G_{n_b} and is absorbed by their masses; (remainder) is o(lambda_b). Hence kappa_F -> 0 and J = 1.
 5. Transport (HT-EC) on [s_1, T_0]. This uses the matched one-sided structure of f. Its errors near the boundary are E_c-valued and are
    carried by S_n up to T_n, which is the boundary layer that Model N charges. The destroyed fine carriers should contribute
    O(lambda_b/t) at scale t (E 2.1 (H-transfer)). This is the only unproved step.
 6. Theorem 4-EC gives (f''_n, g'_n) in NA with g'_n -> rho g, so g is in Ls(f).
Conclusion: under (HT-EC), E's design gives no lower bound on dist((f, rho g), NA). The conversion-capacity bound of E 8.3 (about three
parameters at a group transition) is irrelevant.

### 4.6 Model N with error carrying. NUMERICAL.
Scripts: ctx/r3/work/ec_modelN.py, ec_frozen_only.py, ec_onetype.py; E's solver modelN.py is unchanged. Parameters as in E 7.4: A = 1,
B = 1/2, M = 1/2, scale ratio 1/2, error-dominated a0 = 0.03. EC is modelled by core-error cost 0 for tau <= tau_gen and frozen error 0
for tau <= tau_F = tau_gen^2 in band units (room lemma: tau_F/tau_gen = tau_gen/lambda_b). R := sup P_{f'}/sup P_f; R <= 1 means no
obstruction.
 * Both types converted at one scale (one group scalar), delta = 1: R = 1.194 without EC (E's value reproduced). With EC at
   tau_gen = 2^2, 2^3, 2^4: R = 1.088, 1.023, 1.005. With delta = 2: R = 1.082, 1.021 at 2^2, 2^3.
 * Frozen error carried, resource errors not: R = 1.088, 1.023, 1.021 for tau_F = 16, 64, 256. The last value is a boundary-layer excess
   just above the band; carrying the resource errors as well removes it.
 * One absolute shift (one type converted, one carrier; the other type is pushed deeper): R = 3.41 (a0 = 0.03) and 2.83 (a0 = 0.3)
   without EC. With EC at tau_gen = 2^4, 2^6, 2^8: R = 1.168, 1.041, 1.009.
The excess sits just above tau_gen or tau_F and decays like (band scale)/tau_gen. It tends to 0 because the quantifier order of 4.3 lets
the band be chosen deep relative to the generic depth. Model N omits Hilbert couplings, d-terms and multi-block effects; it is a proxy,
not a bound for p*.

### 4.7 First-order cost of a near-threshold peak. PROVED.
Let k be a peak of block m at f with m u_{k,m}(xi) = sigma(1+delta)Phi(k)M|zeta|/C (relative margin delta > 0). Then alpha(k) = sigma delta Phi(k)^2 M/C.
Using k inward at scale t, i.e. Omega = omega_k e_k - d w with d = Phi(k)^2 w(k)omega_k/C, sigma t omega_k < 0, and the other peaks at M,
gives the first-order excess N_m(w + t Omega) - 1 - t<Omega, zeta/|zeta|> = |t omega_k| delta Phi(k)^2 M/C + O(t^2).
*Proof.* Fact C: zeta(k)/|zeta| = Phi(k) m u_{k,m}(xi)/|zeta| = sigma(1+delta)Phi^2M/C, and alpha(k) = zeta(k)/|zeta| - Phi^2 w(k)/C. To first
order, ||w + t Omega||_inf = (1-td)M and ||D(w + t Omega)|| = (1-td)C + t<Dw, D omega>/C = C + tdM, so N = 1 + O(t^2); and
<t Omega, zeta/|zeta|> = t omega_k alpha(k) + t d - t d(M + C) = t omega_k alpha(k). QED.
(In carried units beta = lambda_k omega_k the cost is |t beta| delta Phi(k) M/(mC). This is a margin-limited first-order cost. Detector errors
left on fractional coordinates, when the scalar is O(1), are of the same order, which is E's peak-cost-comparable regime where Model N
already gives R <= 1. With contacts (4.4) they are absent.)

## 5. What remains of O3; why no counterexample
### 5.1 The residual class O3*. OPEN (HEURISTIC formulation).
After 2.1, 4.2-4.4, an E-type counterexample must satisfy the following at EVERY candidate boundary lambda_b (chosen by the approximant
after the generic depth):
 (R1) Non-compactness. The critical errors of the carriers within J(rho) ~ 32K/(1-rho^2) scales of lambda_b have an escaping part of
      critical size: it tends to 0 coordinatewise along every boundary sequence while its norm stays >= c K lambda. Otherwise a profile
      decomposition along a subsequence yields a compact part, which 4.3 carries.
 (R2) No early generic approximants. The escaping directions have no generic approximants at depth >~ K lambda_b^2, within a fixed
      precision. Lemma B allows this, since targets may be scheduled late (N2 4.5, P1 2.1).
 (R3) Concentration and guards. The escaping part lives on few coordinates. On each of them a MATCHED carrier above the boundary (a
      "guard") has mass larger than its margin divided by the size of a contact move. Otherwise 4.4 makes these coordinates contacts.
 (R4) No private handles. A critical escaping mass on a coordinate that no matched carrier sees critically is a conversion handle
      (a move of size ~theta(1+delta)/K converts the carrier). J such handles at adjacent scales let N2 Thm 4 apply directly.
 (R5) Recursive closure. The guards' own escaping masses must be guarded in turn. Compact parts cannot be moved by relative O(1)
      (E Prop 8.2), and the global scalars (V, group scalars) are too few.
In addition: (A1) near-threshold one-sided carriers of both types at all scales (a fixed point between T and f, constructed nowhere,
N2 4.6(i)), and the mate condition at f with all these errors absorbed at first order.

### 5.2 Evidence that (R3)-(R5) are restrictive. SKETCH (in a linear "status model": carrier i at depth 2^{-i} is shifted by sum_p
(mass_i(p))(z'_p - z_p); it is converted or destroyed when the relative shift exceeds its margin).
(a) Coarsest guard. A carrier at depth mu can have critical masses (>= c_0 mu) on at most K/c_0 coordinates, by its error budget K mu.
    Fixed coarse carriers have small far masses. So every escaping coordinate p has a coarsest critical carrier c_max(p), and p is a
    PRIVATE handle of c_max(p) for every boundary above c_max(p). Blocking (R4) therefore needs SHARED positions that are critical for
    carriers at unboundedly many scales. If the shared masses are proportional to depth, one move shifts all members by the same relative
    amount and converts all members of one type at every depth below the top member; averaging over unboundedly many scales then
    applies (A Thm 6.8, E Thm 5.1). If the masses are not proportional, this is E's detector design, handled in 4.5.
(b) Chain guards, u_i = v + K2^{-i}(e_{p_i} + c e_{p_{i+1}}). Carrier i_b is kept matched, and J adjacent carriers i_b+1..i_b+J of ONE
    type are converted (targets T_i of one sign, |T_i| <= T ~ theta(1+delta)/K). This needs Delta_{i_b+1} = 0 and
    Delta_i + c Delta_{i+1} = T_i. For c >= 1 the bottom-up recursion Delta_{i+1} = (T_i - Delta_i)/c stays bounded by T, uniformly in
    J (checked numerically, ctx/r3/work: e.g. c = 1.5, 3: max move <= 2T for J = 32). For c < 1 use the top-down recursion
    Delta_i = T_i - c Delta_{i+1}, bounded by T/(1-c); the disturbance of carrier i_b is then avoided by leaving carrier i_b+1
    unconverted (a one-scale gap). In both cases the moved coordinates are positions of finer carriers and escape as lambda_b -> 0.
    So chain guards give UNBOUNDED conversion capacity. (Alternating types are the bad case: with c = 1 the moves grow like J T.)
(c) Neither (a) nor (b) proves (R1)-(R5) inconsistent for the real norm. The real norm adds the Hilbert coupling U e', several blocks and
    generic coordinates of other blocks. OPEN.

### 5.3 Why no counterexample
 * Closure route: scale-zero closure is trivial (Prop Z). Multi-scale closure would need an implant inequality, which is unproved, and
   such an inequality cannot exclude carriable-error mates anyway (3.2).
 * E's rigid design is recovered by EC + contacts + one converted carrier, modulo (HT-EC) (4.5); Model N confirms R -> 1 (4.6).
 * A counterexample must realise O3*, including the recursive guard closure, and prove LOWER bounds for r~_{f'}(x_i) uniformly over all NA
   f' (window moves, EC conversions, contacts, far moves, transfer peaks, averaging). No lower-bound technique exists in any of the notes.
   Every device examined lowers the relevant upper bounds. dist((f, rho g), NA) > 0 is not claimed for any example.

### 5.4 Assessment
 * New rigorous tools: Theorem EC (rate-free generic carriers by vanishing window moves), the room lemma, Proposition Z, disjoint block
   addition, Theorem 4-EC, the contact lemma, and the peak-cost formula.
 * BRIEFING_R2 stated the O3 core as "a supply of two-sided carriers with frozen error O(scale) at J ~ 16kappa/(1-rho^2) adjacent scales".
   That requirement is REMOVED for compact error directions: kappa is replaced by the non-carried remainder. Far rigidity does not matter
   to EC. What remains is O3* (5.1).
 * The common open ingredient of all positive arguments is the transport hypothesis (HT)/(HT-EC) above the boundary.
 * Leaning: positive (density), strengthened.

## 6. Next steps
 1. Prove (HT-EC) for a concrete class: matched near-threshold one-sided carriers above lambda_b, destroyed fine carriers contributing
    O(lambda_b/t) (E 2.1 bookkeeping), errors carried by EC up to T_n. This would turn 4.5 into a theorem for E's rigid design.
 2. Prove an escaping-error handle lemma in the real norm. A near-boundary carrier with an unguarded critical escaping mass should be
    convertible at cost o(1) without disturbing matched carriers; E Cor 6.2 is its duality version.
 3. Attack (R1)-(R5) by an l_1 budget plus a profile decomposition of the boundary errors along boundary sequences (coarsest guards,
    5.2(a)). The goal is to show that every admissible T admits arbitrarily fine boundaries with small non-carried remainder kappa_F.
    Together with (HT-EC) this would close O3.
