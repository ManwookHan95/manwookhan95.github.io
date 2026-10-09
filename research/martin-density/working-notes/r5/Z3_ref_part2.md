# Z3 referee, part 2 — Z3 parts 3-4 (companions, transplant, (O1)(i))

## 2.1 Lemma 3.1 (cost of a companion). CORRECT (upper bound). Numerics confirm.
Re-derived: clamp formula Phi_k w(k) = sgn(u_k(zhat)) min(Phi_k M, C v_k), v_k = m|u_k(zhat)|/|R^** zhat|_m (Lemma lem:threshold);
|C^# - C| <= c_2 sum Phi_k|v^#_k - v_k| (proof of Lemma lem:F1, which needs a priori |C^# - C| <= r and |v^#_{k_nat} - v_{k_nat}| <= r; the
first by the sequential argument: Delta -> 0 => R^** zhat^# -> R^** zhat in l_1 => J_m(.) -> J_m weak* (smoothness) => D w^# -> D w;
the second since |u_{k_nat}(delta)| <= Delta/lambda_{k_nat}); per-coordinate bounds in the same-sign and opposite-sign cases; the
counting bound sum_k min(2 lambda_k, x) <= x(log_2(2m/x) + 3) uses only lambda_k <= m 2^{-m-k} (no monotonicity needed); the D-bound by
||D(w^# - w)||^2 <= max_k(Phi_k|Delta w(k)|) * sum_k Phi_k|Delta w(k)|; p* <= q* <= (1 + ||U||)||.||_1. All correct.
Numerics (Z3_ref_work/check_cost_adv.py): 12 fixed blocks with ~10 strict non-peaks each and coordinates within 1e-6..1e-2 of the
threshold, perturbations pushing near-threshold coordinates across it, hitting the main peak, sparse fine, and min(lambda,eps) on all
coordinates, Delta from 1e-4 down to 1e-9: sup L/R <= 0.24 in every block. The unweighted term is necessary (Z3's check_cost2: a deep
strict non-peak has w(k) = C m u_k(zhat)/(Phi_k|R^**zhat|), so lambda_k|Delta w(k)| ~ C m^2|u_k(delta)|/|R^**zhat| is linear in the
UNWEIGHTED perturbation): confirmed analytically.
Caveat (affects 4.3 only): Lemma 3.1 bounds p*(f^# - f) from ABOVE by c(delta). Statements of the form "exactifying costs >~ min(lambda, r)"
are lower bounds on c(delta), i.e. on what the METHOD needs; a lower bound on p*(f^# - f) is not proved (generically true by the
private-signature structure, but unproved). The notes use it only "as a statement about the method": acceptable.

## 2.2 Lemma 3.2 (budget at the companion). CORRECT after one definitional fix.
"Flipped" must mean every j in supp delta with z_j eps_l < 0 (including |z_j| < 1), not only z_j = -eps_l: for sgn z_j = -eps_l,
|z_j| < 1 and sgn x = -eps_l one has phi_{z^#}(x) = 2|x| but phi_{z_j}(x) = (1 - |z_j|)|x|, so phi_{z^#} <= 2 phi_z FAILS there. With the
extended definition everything holds: z_j = 0 is harmless (phi_eps <= 2 phi_0), raised coordinates satisfy phi_{z^#} <= 2 phi_z/(1+|z|),
and on all opposite-sign coordinates phi_{z_j}(eps_l tau v) >= tau v for tau > 0 (since 1 - eps_l z_j >= 1), which is what the bound on
S_fl in the proof of Proposition T uses.

## 2.3 Proposition T (transplant). CORRECT WITH FIXABLE GAPS (all fixes below are mine; none changes the conclusion of Cor 3.4).
Checked step by step against Lemmas lem:modswallow, lem:badpeaks, lem:exactswitch, lem:windowtwopiece:
(1) Pinning modulo B' = A u B. For l in A the bad inequality reads (2||v_l 1_{S_l\F}|| - r_l)(tau_l)_- <= E_l + 2 sum_{l'>l, good} pi |Delta theta_{l'}|,
    because sum_s v_l(s)(1 + eps_l z_s) = 2||v_l 1|| - r_l with r_l := sum v_l(s)(1 - eps_l z_s). FIX T2: eps_l must be the sign minimizing
    r_l (then r_l <= ||v_l 1_{S_l\F}||, and the constant is >= ||v_l 1_{S_l\F}||); use r*_l := ||v_l 1_{S_l\F}||_1 for l in A in Lambda*.
    With the other sign the constant becomes the small room r_l(-eps_l) and nothing is gained over pinning. The good inequalities need S*_l with B' (targets of B'-carriers removed) and (H1) for B'
    — stated.
(2) Violations at f^#. I re-derived the cost directly: on S_l \ (F u T_0), l in A, z^# = eps_l, so phi_{z^#}(eps_l tau_l v_l(s)) = 2(tau_l)_- v_l(s);
    elsewhere z^# = z. Hence c^#(tau) <= (budget at f) + 2||Delta B - L(tau)|| + 4 sum_{l in A}(tau_l)_- = O(K_* t); Lemma 3.2 is not even
    needed here. d-rows: |R^**zhat^#| q^#_l tau_l = eps_l tau_l u_l(zhat^#) for k(l) in Q^#, so the difference of the d-sums is V_m(delta);
    by (H1) for B' and allowedness (a), on S_l (l in A) only v_l is seen, so V_m(delta) = sum_{l in A, m(l)=m} tau_l r_l, and
    (tau_l)_+ r_l <= E_l + O(K_* t), (tau_l)_- r_l <= 2(tau_l)_- = O(K_* t). Hence |V_m(delta)| = O(t + K_* t): correct.
    FIX T4: the "vanishing rows" on T_0 \ (F u K^#) are violated by |L_j| <= phi_{z^#_j}(L_j)/(1 - |z^#_j|); the factor
    C_0^# := max_{j in T_0 \ (F u K^#)} 1/(1 - |z_j|) (finite for each window, but T_0 grows with A, so it may grow with the window) must
    be included in the Hoffman-type constant of (HF) and in the growth conditions of Corollary 3.4 (or one assumes T_0 cap N_theta subset K u F).
(3) Projection: Hoffman constants do not depend on right sides (box rows included): correct.
(4) Split at f^#: Lemma lem:split's proof uses |x| + |y| <= |x - y| + phi_z(x) + phi_{-z}(y), valid for every |z| <= 1, so residual mass on
    non-raised near-contacts is l_1-controlled by ||e|| + budget: correct (this is a point a reader may doubt; it is fine).
(5) Estimates. The frozen-error bound p*(g - g_t) <= C(1 + C_H^#)(K_* + theta)t is correct (|d^#(omega^+)| <= C/t times
    ||R^*(w^# - w)||_1 <= C c(delta) <= C theta t^2; |(d^# - d)(omega^+)| via Lemma 1.2(b) with |(R^*omega^+)(delta)| <= (10/t) Delta; re-clamping
    with gap^# costs (2/t) sum lambda |gap^# - gap| <= C theta t; status changes at the t^2-threshold cost O(t), already present).
    FIX T3: the Gamma bound is misstated. Since ||D Theta_+-||_2 ~ 1/t, |H^#_m(Theta) - H_m(Theta)| <= C ||D Theta||^2 (||D(w^# - w)|| + |C^# - C|)
    <= C t^{-2} c(delta) <= C theta, and likewise |q_0^# - q_0| h(B_+-) <= C theta: the comparison term is an ADDITIVE O(theta), not O(theta t).
    Correct form: Gamma^#_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta) + C theta) + C(1 + C_H^#)(K_* + theta) t)^2. Harmless in Corollary 3.4
    (theta_j -> 0), but the statement as written is false.
    FIX T5 ((BS) is stronger than "small rooms"): c(delta) contains, for EVERY carrier l'' whose target meets a raised set S_l (l in A),
    the term min(lambda_{l''}, |y_{l''}(delta)|/n_{l''}); since |delta_s| <= r_l n_l 2^s/delta_l is the only control, these terms can be
    >> r_l (up to ~sqrt(c_l r_l 2^{-s}) per coordinate). So "rooms <= theta T_lo^2" does NOT imply (BS); a sufficient condition is
    max_{l in A} r_l <= theta T_lo(l_*)^2 delta_min(l_*) 2^{-s_max(l_*)}/C with s_max(l_*) the largest coordinate in the target supports of
    carriers <= l_* (a design quantity; carriers > l_* contribute <= sum_{l''>l_*} lambda_{l''} <= T_lo(l_*)^3). The status/gap parts of (BS)
    remain genuine hypotheses.
    FIX T6 (hidden dependence on B'): the peak rows tau_l = 0 (l in B', k(l) a non-degenerate peak) are violated by
    |tau_l| <= lambda_l(t/(sigma|alpha(k(l))|) + K_d t) = t/mu_{k(l)} + lambda_l K_d t (eq:margin). The notes write "|tau_l| <= C lambda_l t" with C
    "depending only on f", but the sum over B' is t * sum_{l in B' peaks} 1/mu_{k(l)} + K_d t, which grows with B' (exactly as in Z3
    Theorem 5.4, where it is tracked). Likewise the conversion constants 1/m_l (l in B') of the cost function and C_0^# (T4) grow with
    B'. FIX: put K^#_* := K_* + sum_{l in B', nondeg. peak} 1/mu_{k(l)} + C_0^# in place of K_* in the conclusion and in the growth
    conditions of Corollary 3.4 (for a fixed window everything is finite, so the proposition itself is unaffected).
Verdict: the proposition is correct as a conditional statement once T2-T6 are incorporated; Corollary 3.4 follows (with K^#_*).

## 2.4 Corollary 3.4 (exactification windows). CORRECT given Theorem E and Proposition T (with T2-T5).
(E-e): p*(f^#_j - f) <= (1 + ||U||)C_f c(delta_j) <= C theta_j T_lo(l_j)^2 = C theta_j (T_hi 2^{-n^w})^2: matches Theorem E with
T_j = T_hi(l_j), n_j = n^w_{l_j}. Supports: companions keep supp a = F. gamma_B uniform: assumed. Growth: include C_0^# (T4).
IMPROVEMENT (mine, PROVED): Theorem E accepts any (T_j, n_j); Proposition T holds at every t in W(l_*). Hence Corollary 3.4 holds with
the design window replaced by the TOP SUB-WINDOW [2^{-n_j} T_hi(l_j), T_hi(l_j)], n_j <= n^w_{l_j}, under
   (1 + C^#_{H,j})K_{*,j} T_hi(l_j) -> 0,  n_j/((1 + C^#_{H,j})K_{*,j}) -> infinity,  c(delta_j) <= theta_j 4^{-n_j} T_hi(l_j)^2.
With n_j := psi_j (1 + C_H)K_* (psi_j -> infinity slowly) the exactification threshold is 4^{-psi K_*}T_hi^2 instead of 4^{-n^w}T_hi^2 — the
form that the notes' gloss "tower gaps: r_next <= exp(-C prod(1/r))" (4.3(i)) actually requires.

## 2.5 Proposition 4.1. (a) CORRECT. (b) CORRECT after adding a missing hypothesis. Wording fix.
(a) 1 + 3/r_l <= (3/(2 varpi^l))(1 + 2/delta°_l) for r_l >= varpi^l delta°_l: checked; Lambda^+-_f(l) <= C_0(3/2)^l varpi^{-l^2} Lambda°(l).
(b) (W*) requires r*_l > 0 for EVERY good l; the hypothesis "r*_l >= varpi^l delta°_l for all but finitely many good l" does not give it for
the exceptional l. FIX: add "r*_l > 0 for all good l". (r_l > 0 does not imply r*_l > 0: S*_l removes finitely many target coordinates.)
Wording: failure of (W+-) with all r_l > 0 implies "for every varpi > 0, r_l < varpi^l delta°_l for infinitely many l" (liminf of
(r_l/delta°_l)^{1/l} is 0); "decay faster than any geometric sequence along every subsequence" is wrong as stated (and the displayed
condition is necessary, not sufficient, for failure of (W+-)).

## 2.6 Proposition 4.2 (far lowerings). CORRECT after the same fix.
At f^L the rooms of S_l, l <= L, are those of f and r*_l is unchanged for good l <= L (z^L = z on S_l, and the bad set B subset [1,L]); for
l > L, S*_l = S_l and the room is delta°_l. (W*) at f^L therefore needs r*_l > 0 for good l <= L, i.e. at f: ADD this hypothesis
(otherwise a good carrier swallowed off a finite set of later target coordinates breaks (W*) at every f^L). (H2), (H3) at f^L for L large:
checked (margins and gaps persist; a degenerate bad peak of f can only become a strict non-peak, a non-degenerate peak of the same sign
-eps_l, or stay degenerate with sign -eps_l, because w^L -> w coordinatewise and u_{k(l)}(zhat^L) -> u_{k(l)}(zhat)). Also p*(f^L - f) <=
C c(delta^L) <= C sum_{l>L} lambda_l log(e/lambda_l) -> 0 (Lemma 3.1; u_l(delta^L) = 0 for l <= L by allowedness (a)).
The conclusion "(O1)(i) is a quantitative case of (O2)" is then a correct reformulation (Lemma Z is per mate and f^L in G subset Rec).

## 2.7 Section 4.3. (i) CORRECT with the hypotheses of Proposition T made explicit (T2-T5); its "tower gap" gloss is correct only for the
top-sub-window version 2.4. (ii) The band, as a statement about Corollary 3.4 at a given window: CORRECT. The example and the
design-independence claim: NOT PROVED as stated, and the design-independence is FALSE (part 4 below):
* "r_l = 2^{-l^4} delta°_l for infinitely many l in one block" is not a band example: for a sparse set {L_i} (L_{i+1} >= L_i^2) every window
  l_* in [2L_i^{4/3}, L_{i+1}) has pinning product <= 2^{2 L_i^4} Lambda-type factors << 2^{l_*^3}, so (W+-) holds along these windows.
  The example needs the rooms at ALL l in L_N (or in one block whose ladder indices have gaps O(l^{1/2})), AND a design growth bound
  (e.g. delta°_l >= 2^{-l^2}): n^w_{l_*} contains Lambda°(l_*), whose factors from blocks > N do not appear in Lambda^+-; if those
  delta° are tiny, n^w may outrun 2^{sum l^4}. Under these two conditions the example is valid (I checked the arithmetic:
  K/n^w >= 2^{l'^4 - l_*^3 - l_*^3/3 - O(l_*^2)} -> infinity with l' >= l_* - O(l_*^{1/2}); exactification impossible since
  r_{l'} >> 4^{-n^w_{l_*}}).
* "Every design has band carriers ... no choice of design removes it": FALSE in the natural sense. See part 4: with an explosive
  window-length function the bands of different windows are disjoint, each carrier blocks at most one window, and every f with F finite
  has infinitely many band-free windows.
(iii) CORRECT as a method statement, with C_H^# >= |R^**zhat^#|/min Re(u_l) (not 1/r_l; see 1.4). The re-tuning SKETCH: plausible;
note that a^# must keep supp a^# = F for Lemma U, which gives only |F| - 1 degrees of freedom for e^# — at most |F| - 1 independent
d-conditions can be re-tuned without new base coordinates (the SKETCH's "tiny masses on unused contacts" then changes F and
requires a version of Lemma U with growing supports whose new masses are never flipped: plausible, not written).

## 2.8 Section 4.4 / 7.1. The OPEN statement is accurate for the ORIGINAL design (with the example corrected as above). The claim
"defeats every window method" is design-dependent (part 4).
