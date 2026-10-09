# R3 referee, part 2: Theorem 4-EC, Proposition 4.3 (compact error spaces), contact lemma, peak-cost formula

## 2.1 Disjoint block addition (Lemma 4.1). CORRECT (PROVED).
Purely about two vectors with disjoint supports: ||W+omega||_inf = max(...), ||D(W+omega)||^2 = ||DW||^2 + ||D omega||^2,
sqrt(A^2+B^2) <= A + B^2/(2A). The hypotheses about f'' are not used. OK.

## 2.2 Theorem 4-EC. CORRECT as an implication, in the form of R3_notes 4.2 (kappa_T, kappa_F split).
Re-derivation. For s_j < |t| (so |t| > s_1, (HT-EC) applies):
 f'' + t h_j = [A_t + t(e_t + e^j)] + L*[W_t + omega], omega = t sum_{k in S} (c_k(t)+c^j_k)/lambda_k e_k (block m0).
 p*(...) <= max(q*(A_t), ||W_t + omega||_{V*}) + |t|(p*(e_t) + p*(e^j))       (Fact A + triangle inequality for p*)
 N_{m0}(W_{t,m0} + omega) <= 1 + Q t^2/2 + t^2||c(t)+c^j||^2/(2 m0^2 ||D W_{t,m0}||) <= 1 + (Q + Q_S) t^2/2
 (Lemma 4.1 applies: W_{t,m0} = 0 on S, ||omega||_inf <= M''/2 <= ||W_{t,m0}||_inf by (Room), ||D W|| >= C''/2).
 Average with sum_{s_j<|t|} s_j < 2|t|: coefficient <= (Q+Q_S)/2 + kappa_T + 2 kappa_F/J <= 1/2 - (1-rho^2)/16,
 and 1 + t^2(1/2 - (1-rho^2)/16) <= 1 + t^2/2 - t^4/8 <= s(t) for t^2 <= (1-rho^2)/2. Slack part (|t| >= T_0) uses
 g in C(f) and A Lemma 4.7 exactly as N2 Thm 4. (f'', g') in NA because g' in C(f'') forces g'(normer) = 0. OK.
Remarks.
 (a) R3_part4.md 4.2 contains an intermediate WRONG hypothesis ("J >= 32 kappa'/(1-rho^2)" for a single kappa' that also
     bounds e_t); the author noticed it ("Hmm: this needs kappa' itself small") and R3_notes 4.2 states the correct split.
     The notes version is the one checked. The part file should be marked superseded.
 (b) "J = 1 suffices when the non-carried frozen remainder is small" is correct AS A STATEMENT ABOUT THE HYPOTHESES:
     J = 1 needs kappa_F <= (1-rho^2)/32 AND (HC) for the single certificate h_1, i.e. H-type bound Q for h_1 on |t| <= s_1.
     (HC) is a Hilbert-capacity condition on the two-sided carriers used by h_1; it is NOT implied by error carrying.
     This matters in 4.5 (see part 3: it fails for a single converted carrier in Model N at nearby parameters).
 (c) Possible sharpening (not in R3; easy, PROVED by the same Fact A + Lemma 4.1 computation): when the h_j use pairwise
     disjoint sets of strict non-peaks, at |t| <= s_1 one may use g' directly instead of convexity; its block coefficient
     is (1/J^2) sum_j H(h_j)-type, i.e. about H(h)/J for equal single-carrier certificates. Convexity (as in N2 Thm 4 and
     4-EC) throws this factor J away. This is the natural way to add Hilbert capacity from several converted bands.
 (d) Hidden requirement in the application: the carried parts must vanish at the normer of f'' (u_k(xi'') = 0 on S), so
     only components of the errors lying in xihat''-perp are carriable; components along a direction with value 1 at xihat''
     must be handled through the normalisation (R3 calls this SKETCH; agreed).

## 2.3 Proposition 4.3 (EC carries compact error spaces; quantifier order). CORRECT (PROVED), arithmetic only.
mu = (B^T)^{-1}(y(eta_l))_l, ||mu||_inf <= beta_T ||y||_1 (|y(eta_l)| <= ||y||_1 ||eta_l||_inf); e = sum mu_i(b_i - u_{k_i}),
||e||_1 <= d beta_T eps_n ||y||_1. (R3_part4 used beta = ||B^{-1}|| here; the notes correctly use beta_T = ||(B^T)^{-1}||.)
Room arithmetic: t-dependent errors of size kappa|t| need |t|^2 beta_T kappa <= lambda_gen M''/2, i.e. |t| <= T_n; a frozen
error of size kappa lambda_b needs |t| <= tau_F = lambda_gen M''/(2 beta_T kappa lambda_b). Both ranges are as large as
wanted relative to lambda_b once lambda_b is chosen after lambda_gen. Q_S -> 0 in both regimes:
 t-dependent: ||c(t)||^2 <= d beta^2 kappa^2 T_n^2 = d beta kappa lambda_gen M''/2 -> 0;
 frozen/boundary-layer (size K lambda_b, constant in t): ||c||^2 <= d beta^2 K^2 lambda_b^2 -> 0.
CAVEATS (wording/ordering, not errors in the proposition):
 (i) T_n -> 0 as lambda_gen -> 0, while (HT-EC) is needed up to the FIXED T_0. On [T_n, T_0] nothing is carried, so the
     non-carried transport remainder must already be <= kappa_T |t| there. For the boundary-layer errors of E's design
     (size K lambda_b in direction units, see part 3) this holds since K lambda_b/T_n -> 0; for f's own matched errors no
     carrying is needed (same absorption as at f). So the quantifier order works, but only together with (HT).
 (ii) The protected set Pi must be fixed BEFORE the generic coordinates; it cannot contain functionals whose restrictions
     to G lie in span{b_i|_G} (Remark 2.2(2)). See part 3, issue P1.

## 2.4 Contact lemma (4.4). The LP statement is CORRECT (PROVED); the absorption statement is SKETCH with conditions.
LP: at a vertex of {y in [-1,1]^G : Lambda y = c} the active constraints have rank |G|; equalities give rank <= r; the active
box constraints are distinct unit vectors, so >= |G| - r coordinates are at +-1. OK.
Absorption (N2 Lemma 1.4, re-checked): q*(a'' + tau B) <= 1 + kink'' + tau^2 h''(B)/(2(1 - |tau| ||U*B||/nu'')), with kink'' = 0
for both signs iff B lives on supp a'' (contacts WITH masses). Conditions that must be stated: (1) B(xhat'') = 0 (only the
total base part is constrained, so this is a statement about totals, not about each piece separately); (2) masses
|a''_j| >= T_0 |B_j| on G (two-sided up to the fixed T_0); (3) renormalisation of a'' and the induced change of e'' (moves
xhat'' everywhere, including at the generic EC coordinates, which must then be re-solved, part 3); (4) the Hilbert cost
tau^2 h''(B)/2 counts against the budget (harmless when ||B||_1 = O(lambda_b)). With these, "error parts supported on the
contacts are absorbed two-sidedly at zero first-order cost" is right. The <= r fractional coordinates keep their errors.

## 2.5 Near-threshold peak cost (4.7). CORRECT (PROVED).
zeta(k)/|zeta| = Phi m u_k(xi)/|zeta| = sigma(1+delta) Phi^2 M/C, alpha(k) = that - Phi^2 sigma M/C = sigma delta Phi^2 M/C.
Inward use Omega = omega_k e_k - d w, d = Phi^2 w(k) omega_k/C: ||w+t Omega||_inf = (1-td)M (needs ANOTHER peak; peak sets are
infinite at non-NA points and contain opposite-sign peaks at NA points, N2 3.3, so fine), ||D(w+t Omega)|| = C + tdM + O(t^2)
(A Lemma 4.4(a)); N = 1 + O(t^2); <t Omega, zeta/|zeta|> = t omega_k alpha(k) (the d-terms cancel: <w,zeta/|zeta|> = M + C = 1).
First-order excess = -t omega_k alpha(k) = |t omega_k| delta Phi^2 M/C since sigma t omega_k < 0. Carried units beta = lambda omega:
|t beta| delta Phi M/(m C). OK.
Observation used in part 3: the relative cost per unit carried amount at scale t is delta Phi M/(m C |t|) and the Hilbert
coefficient per unit^2 is 1/(m^2 C); their ratio is ~ delta M m Phi/|t|. In the real norm the "peak-cost weight" a0 of Model N
is therefore TIED to the margin delta (a0 ~ delta M relative to the Hilbert weight), while Model N treats a0, delta, A, B as
independent. This coupling matters for the Hilbert-capacity question of part 3.
