# R3 referee notes (assembled; parts R3_ref_part1..4.md; scripts ctx/r3/refwork/*.py)

Setting: canonical base q, Martin's norm with a FINITE block set I (p_N; Preprint B Remark martin-tail), admissible T = Lemma B's
conclusion only. Imports re-checked: A Facts A-E, Def 4.1, Lemma 4.4, Prop 4.5, Lemma 4.7; N2 Lemmas 1.4, 1.5, Thm 4.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN / NUMERICAL.

## 0. Verdicts
| R3 claim | R3 label | Verdict |
|---|---|---|
| Theorem EC | PROVED | CORRECT. Wording: depth is only bounded ABOVE (Phi(k) <= Phibar_n); the actual depth is chosen by T. |
| Room lemma | PROVED | CORRECT. Applies to O(scale) errors (fixed size kappa s, or t-dependent kappa t); not to O(1) components. |
| Proposition Z | PROVED | CORRECT (needs J infinite; used). 3.2(a) is a correct definitional consequence. |
| Theorem 4-EC | PROVED (implication) | CORRECT in the R3_notes form (kappa_T, kappa_F split); R3_part4's intermediate hypothesis was wrong and is superseded. "J = 1 suffices" needs (HC) for h_1, a Hilbert-capacity condition. |
| Prop 4.3 (compact error spaces, quantifier order) | PROVED | CORRECT as arithmetic (beta_T = ||(B^T)^{-1}||). Room up to T_n (-> 0) only; (HT) must cover [T_n, T_0]. |
| Contact lemma | PROVED | LP statement CORRECT. Absorption statement correct under explicit conditions (masses >= T_0|B_j|, totals vanish at the normer, re-solve EC after the mass change); the a''-direction step is SKETCH. |
| Rigid design recovered | SKETCH | SKETCH with an ADDITIONAL gap: Hilbert/room capacity of the converted carriers. "One converted carrier / one global scalar suffices" is FALSE in general (Model N: R = 1.09-2.07 at nearby parameters, independent of tau_gen). Also a protected-set inconsistency (fixable) and an ordering issue (fixable). |
| Model N with EC | NUMERICAL | REPRODUCED exactly; but the one-carrier result is a borderline artefact (B S^2 = 0.5 vs sup P_f = 0.5225). |
| Near-threshold peak cost | PROVED | CORRECT; numerically confirmed. |
| Chain guards / coarsest guard | SKETCH | Chain-guard arithmetic CORRECT (caveat c = 1: constant targets needed); coarsest-guard dichotomy HEURISTIC. |
| O3* residual class | OPEN | Reasonable but INCOMPLETE: add (R6) Hilbert/room-capacity deficit with compact errors. |
| No counterexample; density open | — | Agreed. Nothing found contradicts property B; no counterexample is claimed. |

## 1. Theorem EC (re-proof skeleton). PROVED.
Data at stage n: targets b_i in S_{q*} with b_i(zhat) = 0 (i <= d); finite G subset J with gamma = 1 - max_G |z_j| > 0; eta_l in c_00(G),
||eta_l||_inf <= 1, B = (b_i(eta_l)) invertible, beta = ||B^{-1}||_{inf->inf}; protected Pi with phi(eta_l) = 0; eps with
8(2+||U||) d beta eps <= min(gamma, 1/n). Proof: (1) by Lemma B every tail of (u_{k,m0})_k is q*-dense in S_{q*} (a dense set in a
sphere without isolated points stays dense after removing finitely many points), so distinct k_i >= K_n with ||u_{k_i} - b_i||_1 <= eps
exist. (2) A = (u_{k_i}(eta_l)) = B + E, |E_il| <= eps, ||B^{-1}E|| <= 1/16, ||A^{-1}|| <= 2 beta. (3) b(x'_N) -> b(zhat) (dominated
convergence and e'_N -> e); choose N(n) with 4 d beta max|b_i(x'_{N(n)})| <= min/4 and |z'_{N(n)} - z| <= gamma/4 on G (so G misses
supp a'_{N(n)}). (4) s = -A^{-1}(u_{k_i}(x'))_i, eta' = sum s_l eta_l: ||eta'||_inf <= 2 d beta(max|b_i(x')| + eps(1+||U||)) <= min/2,
u_{k_i}(x' + eta') = 0, phi(eta') = 0. (5) z'' = z' + eta' in B_{c_0}, z'' = sign a' on supp a', q(x'') = 1 = a'(x''); f'' = grad p(x'')
is NA; z'' -> z coordinatewise; N2 Lemma 1.5 gives f'' -> f in norm. (6) zeta''(k_i) = 0 forces k_i notin P'' (on P'' the modulus of
zeta''(k)/|zeta''| is >= Phi^2 M''/C'' > 0), so w''(k_i) = 0, gap M'', d''(e_{k_i}) = 0. (7) c = (0, sum (c_i/lambda_{k_i}) e_{k_i}) is a
finite certificate: d = 0, kappa = 0, H = ||c||_2^2/(m0^2 C''), r >= M'' min lambda_{k_i}/(2||c||_inf); A Prop 4.5. QED.
Remark: (ii) holds iff no nontrivial sum mu_i b_i|_G lies in span{phi|_G : phi in Pi} (finite-dimensional duality).

## 2. Room lemma. PROVED. If ||c||_inf <= kappa s and s^2 <= M'' lambda_gen/(2 kappa) then r >= s and H <= d kappa^2 s^2/(m0^2 C'').
A t-dependent error of RELATIVE size kappa_0 (||y_t|| ~ kappa_0) would need c ~ beta kappa_0 and H ~ d beta^2 kappa_0^2/(m0^2 C''), not
small: EC carries O(scale) errors only (this is the implant scale gap for O(1) components, which R3 states correctly).

## 3. Proposition Z. PROVED (J infinite). y_i = g + r(e*_{j_i} - zhat_{j_i} a) in zhat-perp, Y = rI + 1 gamma^T, ||Y^{-1}|| <= 2/r,
beta <= 4 q*(g)/r, c_i = q*(y_i)/d: ||g_c - g||_1 <= r(2+||U||) + 2 eps q*(g), H <= 4 q*(g)^2/(d m0^2 C'') -> 0. All steps re-derived.

## 4. Disjoint block addition and Theorem 4-EC. PROVED (implication).
Lemma: disjoint supports give N(W + omega) <= N(W) + ||D omega||^2/(2||DW||) when ||omega||_inf <= ||W||_inf.
Theorem (R3_notes form): with (HC), (HT-EC), (HE-EC), (Room) and Q + Q_S <= 1 - 3(1-rho^2)/8, kappa_T <= (1-rho^2)/16,
J >= 32 kappa_F/(1-rho^2): p*(f'' + t g') <= s(t) on |t| <= T_0. Proof: for s_j < |t|, Fact A + Lemma give
p*(f''+t h_j) <= 1 + (Q+Q_S) t^2/2 + kappa_T t^2 + kappa_F |t| s_j; average; sum_{s_j<|t|} s_j < 2|t|; coefficient
<= 1/2 - (1-rho^2)/16; s(t) >= 1 + t^2/2 - t^4/8 and t^2 <= (1-rho^2)/2. Slack beyond T_0 as in N2 Thm 4. QED.
Remark 4.1 (joint certificates; PROVED, elementary, new here). Let the h_j be finite certificates at f'' with zero base part and block
parts omega_j (block m0) supported on pairwise disjoint sets S_j of strict non-peaks with w'' = 0 on S_j (so d_j = 0, kappa_j = 0). For
nonempty A subset {1..J} put h_A := (1/|A|) sum_{j in A} h_j. By linearity of c -> g_c (A Lemma 4.2) h_A is the certificate with
omega_A = (1/|A|) sum omega_j, and by orthogonality of disjoint D-supports H(h_A) = (1/|A|^2) sum_{j in A} H(h_j),
||omega_A||_inf = max_{j in A} ||omega_j||_inf/|A|, so r(h_A) >= |A| min_{j in A} r(h_j). With A_t := {j : s_j >= |t|} and F_t its complement,
convexity applied to the TWO groups, p*(f''+t g') <= (|A_t|/J) p*(f''+t h_{A_t}) + (|F_t|/J) p*(f''+t h_{F_t}), shows that (HC) may be
weakened to avg_{j in A_t} H(h_j) <= |A_t| Q at scale t (the frozen group is treated exactly as in 4-EC). Convexity over all J summands
(N2 Thm 4, 4-EC) discards this factor |A_t|; pooling is the natural way to add the Hilbert capacity of several converted bands.

## 5. Proposition 4.3. PROVED. mu = (B^T)^{-1}(y(eta_l)), ||mu||_inf <= beta_T ||y||_1, e = sum mu_i(b_i - u_{k_i}), ||e||_1 <= d beta_T eps ||y||_1.
Room: kappa|t|-errors up to T_n = sqrt(M'' lambda_gen/(2 beta_T kappa)); frozen kappa lambda_b-errors up to tau_F = M'' lambda_gen/(2 beta_T kappa lambda_b);
Q_S -> 0 in both cases. Caveat: T_n -> 0; on [T_n, T_0] no carrying, so the non-carried transport remainder must be <= kappa_T|t| there
(true for boundary-layer errors of size K lambda_b; f's own matched errors need no carrying).

## 6. Contact lemma. PROVED (LP vertex argument). Absorption: N2 Lemma 1.4 with B on supp a'' gives zero kink for both signs; needs
B(xhat'') = 0 for the TOTAL base part, masses >= T_0 |B_j|, and costs tau^2 h''(B)/2 (O(t^2 lambda_b^2) for detector errors).

## 7. Peak cost. PROVED: alpha(k) = sigma delta Phi^2 M/C; first-order inward-use excess |t omega_k| delta Phi^2 M/C (needs another peak to
keep the sup). NUMERICAL confirmation: refwork/peakcost.py (agreement to O(t^2)).

## 8. The rigid design (R3 4.5): issues and the Hilbert-capacity gap.
P1 (protected set). Protecting band/designated carriers u ~ (v + K lambda sigma)/n together with v protects sigma|_G in E_c and, by the
remark in section 1, (ii) fails as soon as the protected sigma|_G and v|_G span a target direction (e.g. once dim E_c matched carriers with
spanning sigma's are protected; an approximate span only inflates beta, which is harmless for EC but shrinks T_n, tau_F).
FIX: protect only v; carriers' statuses are kept
because a move eta with v(eta) = 0 shifts every v-carrier by the relative amount O(K ||sigma||_1 ||eta||_inf/theta) -> 0, uniformly.
P2 (ordering). Far choices and contact masses change u_{k_{n,i}}(x'') by up to 2 eps_n + ||U|| ||Delta e''|| >> Phi(k) possibly; re-solve the
EC system LAST (same matrix A_n; move O(beta eps_n)).
P3. The final EC move (size ~ beta eps_n, fixed before lambda_b) shifts every block coordinate; harmless for the switching carriers
(window part v + O(lambda)), uncontrolled for other structure of f at depth ~ lambda_b: belongs to (HT-EC).
P4. Single-coordinate detector: by 4.4 with r = 1 the coordinate may stay fractional (any scalar value) at one-sided first-order cost.
P5. Components of the errors along a vector with value 1 at xihat'' are not carriable (u_k(x'') = 0 on S): normalisation step, SKETCH.
P6 ((HT-EC), OPEN). Bookkeeping: at f the destroyed carriers carry an ABSOLUTE amount <= sum_{lambda_i<lambda_b} 2 M lambda_i ~ 4 M lambda_b of
t S v at every t >= lambda_b. Re-routing it to matched carriers costs an extra error K lambda_b sigma (constant in t; carriable by EC up to
tau_F) and an extra Hilbert load ~ 2 x Delta x/(m^2 C), Delta x ~ lambda_b/t (NOT carriable); converted band carriers replace it with
room M lambda_b/t each and no error.
HILBERT-CAPACITY GAP (NUMERICAL in Model N; mechanism HEURISTIC). Below the band (|t| << delta lambda_b) matched peaks cost
delta Phi M x/(m C |t|) -> infinity (section 7), destroyed ones ~ a0 s/tau, and EC generic carriers cannot take O(1) components, so the
switching component must ride on converted carriers: N carriers with equal split give block coefficient rho^2 S^2/(N m0^2 C''), so
(HC) needs N >= rho^2 S^2/(m0^2 C'' Q). Model N (refwork scripts):
 - bottom value P_{f'}(tau -> 0) = B S^2/n_conv exactly; R3's parameters give B S^2/sup P_f = 0.957;
 - one carrier, EC at 2^6: A = 0.5: R = 1.463; A = 0.25: R = 2.074; A = 1, B = 0.6: R = 1.086 (all at tau = 2^-8, independent of tau_gen;
   all still "error >> peak" as in E (A1));
 - two carriers (both types, one group scalar): A = 0.5: 1.003; 0.25: 1.037; 0.1: 1.426;
 - needed n_conv ~ B S^2/sup P_f grows like log(1/c) as the linear costs c -> 0 (0.96 -> 8.12);
 - with the real-norm coupling peak cost ~ margin (a0(1+delta) = delta): bottom met by one shift (ratio 0.29-0.83); full profile with
   ONE shift, A = 0.1 delta, delta = 1: R = 1.090 at tau ~ 4.7 for tau_gen = 2^6 and 2^8 (boundary-layer room deficit, no decay);
   delta = 0.3: 1.035 (2^6), 1.024 (2^8); TWO shifts: R = 1.0000.
Mechanism of the one-shift boundary-layer deficit: one absolute shift V moves every fine carrier by V/lambda in the same direction (V ~
theta lambda_b dominates detector shifts ~ Phi_k), so the destroyed region becomes deep peaks of ONE sign and one side of t loses all fine
room; opposite shifts (group scalar with opposite P+/P- coefficients) leave deep peaks of both signs, whose cost a0 s/tau decays above the
band. R3's single-coordinate-detector fallback (4.5(3)) is the one-shift case.
Conclusion: EC removes the error-driven conversion requirement (J ~ 32 kappa/(1-rho^2)) but leaves a rho-independent Hilbert/room
requirement on the converted carriers near and below the boundary. "One converted carrier of one type suffices" is FALSE in general
(also inside E's class (A1)-(A5)); converting both types (available at group transitions, E 4.4) sufficed in every coupled test.

## 9. O3*, guards.
(R1)-(R5) describe what defeats EC for errors; add (R6): conversion capacity below the Hilbert/room requirement at every boundary.
Chain guards: c > 1 bottom-up bounded (0.72 T at c = 1.5, 0.33 T at c = 3, J = 32); c < 1 top-down <= T/(1-c); c = 1 bounded only with
constant targets (random targets: random walk, 3.6 T); alternating types at c = 1 grow like J T. Coarsest guard: HEURISTIC dichotomy.

## 10. Assessment and most valuable idea.
All PROVED claims of R3 survive (with the wording fixes above). The SKETCH "rigid design recovered" overstates: one global scalar is
not enough in general; the corrected statement is "recovered modulo (HT-EC) and a bounded Hilbert/room capacity of converted carriers
(both types)". Density remains OPEN; leaning positive is reasonable; no counterexample is claimed or found.
Most valuable idea: Theorem EC + room lemma + quantifier order — generic dense-tail coordinates become exact zero-weight strict non-peaks
by o(1) window moves solving a finite linear system against targets in zhat-perp, and then carry every fixed finite-dimensional family of
O(scale) errors two-sidedly at quadratic cost O(scale^2), with no rate hypothesis on T, because the boundary is chosen after the generic
depth. The referee's addition: what remains after EC is a capacity count of converted carriers (Hilbert/room), not an error count, and it
can be pooled across bands by joint certificates (Remark 4.1) instead of convexity.
