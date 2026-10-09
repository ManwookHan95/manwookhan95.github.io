# Z3 referee notes (Round 5): verification of Z3 ((O1): approximate swallowing, inexact free carriers), fixes, and new results

Reference: paper/martin_density_note.tex (numbering, notation). I = {1..N} finite, p = p_N (Lemma lem:martintail transfers density for
infinitely many N to Martin's p). Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Report: Z3_referee.md. Scripts: Z3_ref_work/.
Parts: Z3_ref_part1.md (Z3 parts 1-2), Z3_ref_part2.md (Z3 parts 3-4), Z3_ref_part3.md (Z3 parts 5-6), Z3_ref_part4.md (new).

## Summary of results
A. Verified as correct (re-derived line by line): Lemma 1.1, Lemma 1.2, Corollary 1.3, Lemma 1.4 (with the constant 1/Re(u)),
   Remark 1.5(a),(b) (as statements about upper bounds), Lemma U, THEOREM E, Lemma 3.1 (upper bound; adversarial numerics), Lemma 5.1
   and its multi-coordinate extension (numerics), Identity 5.2, THEOREM 5.3, THEOREM 5.4, 5.5(i), Corollary 6.2 (tautological part).
B. Correct after fixes (fixes PROVED here): Lemma 3.2 (flipped set = all j with z_j eps_l < 0); Proposition T (T2: eps_l the minimizing
   sign and r*_l := ||v_l 1_{S_l\F}|| for l in A; T3: Gamma bound with an additive O(theta); T4: factor C_0^# for the vanishing rows;
   T5: (BS) is not implied by small rooms — target-induced costs; sufficient design-quantity condition given; T6: inverse margins of
   the bad peak carriers in B' and the conversion constants grow with B' and must enter K, K^#_* := K_* + sum 1/mu + C_0^#); Corollary 3.4;
   Proposition 4.1(b) and Proposition 4.2 (add r*_l > 0 for all good l); 4.3(i) (hypotheses of Proposition T made explicit).
C. FALSE: "every design has band carriers; no choice of design removes the band" (Z3 4.3(ii), 7.1). The example "r_l = 2^{-l^4}delta°_l
   for infinitely many l in one block" is not a band example (sparse sets are pinnable); it is valid for ALL l in L_N under (G1') gaps of
   L_N are O(l^{1/2}) and (G2') delta°_l >= 2^{-l^2}.
D. NEW (PROVED, part 4): for the explosive variant (D1^F) of the SLD design (window factor l 2^{l^3} replaced by a recursively chosen F(l))
   (i) all of Section 8 and of Z3 survive; (ii) the bands of different windows are pairwise disjoint, so every first row with finite base
   support has infinitely many band-free windows; (iii) at such windows the coarse carriers split into pinned and exactifiable ones with
   K_* <= C_f^{l} F^{1/4} Lambda° and exactification cost <= theta T_lo^2, theta -> 0; hence f in Rec under the companion-cone hypotheses
   ((H1)-(H3) for E u B, slaving r*_l >= r_l/2, status stability, Hoffman C_H <= F^{1/2}). So for (D1^F), (O1)(i) reduces to the
   Hoffman/companion-cone problem of growing finite sets of nearly exactly swallowed carriers (same difficulty as Remark rem:S(c), (O2)).
E. NEW (PROVED): top-sub-window form of Corollary 3.4 (exactification threshold theta 4^{-n_j}T_hi^2 with n_j ~ psi (1 + C_H)K_*).
F. SKETCH (unchanged status): Remark 1.5(c), 4.3(iii) (and: only |F| - 1 degrees of freedom for re-tuning e^# with supp a^# = F),
   5.5(ii) (genericity of the tuning shift missing), 6.1 (genericity; push range should be sum v(1 - sigma z)).
G. OPEN: (O1)(i) for the original design (band carriers / lsc along far lowerings); (O1)(i) for (D1^F) modulo the cone conditions
   (in particular d-neutral approximately resonant exactified carriers, Lemma 1.4); (O1)(ii) items of Z3 5.6; (O2)-(O4).
# Z3 referee, part 1 — Z3 parts 1-2 (first-order defects; Lemma U; Theorem E)

Reference: paper/martin_density_note.tex (numbering and notation). I finite, p = p_N. Each item: verdict, then the line-by-line check.

## 1.1 Lemma 1.1 (effective contact set). CORRECT.
Re-derived from Lemma lem:switchbudget (valid for every t > 0: its proof uses only Lemma lem:bookkeeping(a), g(xi) = 0,
s(t) - 1 <= t^2/2 and nonnegativity of the block excesses). Off N_theta: phi_{+-z_j}(x) >= (1 - |z_j|)|x| > theta|x|, so the l_1-mass of
EACH of B_+, B_- there is <= t/(2 theta q_0) (for Delta B: t/(theta q_0)). On N_theta with theta < 1 one has |z_j| >= 1 - theta > 0 and, if
sgn(z_j)x < 0, phi_{z_j}(x) = (1 + |z_j|)|x| >= (2 - theta)|x|; symmetrically for B_- with phi_{-z_j}. (c) is phi >= (1 - |z|)|x|.
Remark: theta < 1 is needed in (b) (at theta = 1, N_1 contains coordinates with z_j = 0, which have no sign); the note's statement
respects this.

## 1.2 Lemma 1.2 (d through the normer; defect identity). CORRECT.
(a) Lemma lem:threshold off P_m: Phi_m(k)^2 w_m(k)/C_m = zeta_m(k)/sigma_m; summing against omega in c_00(Q_m) gives
d_m(omega) = <omega, zeta_m>/sigma_m, and zeta_m = q_0 R_m^** zhat, sigma_m = q_0|R_m^** zhat|_m, <omega, R^** theta> = (R^* omega)(theta).
(b) A companion has the same a, hence the same e and nu, and z^# = z on F; so zhat^# - zhat = z^# - z = delta (supported in F^c) and
(a) at both points, for omega in c_00(Q_m cap Q^#_m), subtracts to the identity. Numerically confirmed (Z3_ref_work/check_dnormer.py,
150 random blocks and companions: (a) max relative error 3e-17, (b) 2e-12, i.e. bisection precision).

## 1.3 Corollary 1.3 (raising converts defect into d-mismatch). CORRECT, with one precision.
Lemma 1.2(b) with omega = omega^- - omega^+ (d is linear) and R_m^* e_k = lambda_k u_k. On supp delta with z^#_j = sgn V_j (V_j != 0):
V_j delta_j = |V_j| - z_j V_j = phi_{z_j}(V_j). Precision: only the defect ON supp delta is converted; the identity says nothing about the
defect of V on coordinates that are not moved.
IMPORTANT consequence that the notes state only implicitly (and that I verified): the nonnegative d-mismatch produced at the companion
can NOT be fed to Corollary cor:D1 (which tolerates Delta d_m >= 0) through finitely supported two-piece data: two representations of
one functional force b^+ - b^- = R_m^*(omega^- - omega^+) - Delta d_m R_m^* w^#_m, and R_m^* w^#_m has infinitely many peak terms, so its
restriction to F^c is not supported in K^# u F unless Delta d_m = 0 (Lemma lem:rigidity(b)-type independence). This is Remark rem:S(b)
of the note; it is the reason why Lemma 1.4 matters.

## 1.4 Lemma 1.4 (approximate resonance vs d-neutrality). CORRECT; the Hoffman-constant gloss is HEURISTIC in its constant.
eps u(zhat^#) - eps u(zhat) = sum_{F^c} eps u_j (z^#_j - z_j) = sum (|u_j| - eps u_j z_j) = Re(u): checked. d-neutral at f <=> w_m(k) = 0 <=>
u_k(zhat) = 0 (a zero zeta_m(k) cannot sit on P_m, since alpha would get the sign opposite to w; and w(k) = 0 forces k notin P_m). At a
strict non-peak of f^#: w^#(k) = C^# m u(zhat^#)/(Phi_k |R^** zhat^#|) and q^#_l = eps Phi w^#/(m C^#) = Re(u_l)/|R^** zhat^#|: checked.
Cone consequence: if every switching carrier of a block has q^# > 0, {tau >= 0, sum q^# tau = 0} = {0}: correct.
"Hoffman constant >~ 1/room": the correct lower bound is C_H^# >= |R^** zhat^#|_m / min_l Re(u_l) (test tau = e_l). Since Re(u_l) =
(signature room r_l) + (target part) >= r_l, this is >~ 1/r_l only when the target part of Re is comparable to r_l. As a statement about
the method (the companion buys nothing over pinning when Re ~ r_l) it is right; the constant claim should read 1/Re(u_l).

## 1.5 Remark 1.5 (kink). (a), (b) CORRECT as statements about the available bounds; (c) SKETCH (labelled so) — plausible.
(a) In the proof of Proposition prop:onesidedupper the only change is Exc(tb) = t D^+(b); it enters Gamma-hat with weight q_0, and
through epsilon_m = (G_m - Gamma-hat)/e_y it also enters the rebalancing error with a factor O(eta_1). So the correct bound is
p*(f + r g) <= 1 + q_0 r D^+ (1 + O(eta_1)) + (r^2/2)(Gamma_w + o(1)); harmless. This is an UPPER bound: it shows the data certify
nothing below scale ~D, not that g is not certified by other data (the notes say so).
(b) D_i <= t_i/(2q_0) + O(K t_i) is an upper bound; "the average carries a kink of slope ~T_hi/n" is a statement about the bound
(the actual defects may be smaller). Fine as labelled.
(c) In Theorem thm:engineered a first-order base defect D enters Step 3 as rho|tau|D and is affordable for |tau| > s_1 iff D <~ delta s_1;
for |tau| <= s_1 the theta-data are used, whose base part lives on window contacts WITH mass (exact). Defect data at near-contacts
(|z_j| < 1) cannot receive window masses without raising z_j (z' = sgn a' on supp a'), so either the defect stays (needs D <~ s_1) or
the near-contacts are raised (a companion-type move whose p*-cost must be <~ T_0^2 by Lemma lem:assembly). With s_1 fixed and
N_w, N'' -> infinity the approximants converge to a first row at distance ~ s_1 ||b^theta||_1 from f, and Lemma lem:assembly needs
p*(f' - f) <= (1 - rho^2) T_0^2/6; hence the threshold ~T_0^2. Plausible SKETCH; not needed elsewhere.

## 1.6 Lemma U (uniform one-sided transfer expansion along f_j -> f, supp a_j = F). CORRECT.
I re-traced every constant in the proofs of Lemmas lem:uniformtransfer and lem:onesidedtransfer:
* base: c_flat A_0 <= a_min (no flips), ||r U^* b||/nu <= 1/2 (Psi-bound), K'_A = 2||U||A_0/nu: need a_{j,min} -> a_min > 0 (true: F finite,
  a_j -> a in l_1, supp a_j = F) and nu_j -> nu;
* blocks: |d^{(j)}(omega)| <= ||D omega||_2 (since ||D w_j|| = C_j), radius conditions use gap^{(j)} (hypotheses are stated at f_j), C_min^{(j)};
* rebalancing: transfer data chosen AT f; by Lemma lem:persistence they persist at f_j (k_* stays a peak with positive margin, L_j built
  with |w_j| >= gamma, Y_j/q_0^{(j)}, e_{y,j}, iota_j, D y_j converge); Lemma lem:TV at f_j needs only ||W - w_j||_inf <= (M_j - gamma)/4,
  ||D(W - w_j)|| <= C_j/2, which hold with the limit constants and a factor 2 of room;
* K_3 uses h <= 2/q_0^{(j)}, H_m <= 2/sigma^{(j)}_m, e_y >= 1/2: convergent.
So all constraints on (c_flat, t_1) are uniform for j >= j_0 (j_0 depends on eta_1, i.e. on eps_tr). Also verified: Lemma lem:TV is
robust under the inward moves of Lemma 5.1 (sign of W at k in L is preserved because ||W - w|| < gamma), so the "inward coordinates"
extension of Lemma U (Z3 5.1) is also correct.

## 1.7 Theorem E (windowed recovery through nearby first rows). CORRECT. (Re-derived line by line.)
* (A) at f_j: Lemma U applied to the + data for 0 < rho r <= c_flat t_i and to the - data for -c_flat t_i <= rho r < 0; both represent
  g_{j,t_i}; Gamma <= 1 + eta_0/2 <= 2, eps_tr = eta_0/2 give 1 + (rho^2 r^2/2)(1 + eta_0).
* (B'): p*(f_j + r rho g_{j,t}) <= p*(f + r rho g) + eps_j + rho|r| K t <= s(rho r) + eps_j + rho|r| K t (g in C(f)).
* |r| <= r_0: if I_r != {} then rho|r| > c_flat t_{n} = 2 c_flat tau_j, so eps_j <= theta_j tau_j^2 < theta_j rho^2 r^2/c_flat^2 <= (1-rho^2) r^2/24;
  sum_{I_r} t_i < 2 rho|r|/c_flat (dyadic); extra <= (1-rho^2)r^2/24 + 2 rho^2 K r^2/(c_flat n) <= (1-rho^2) r^2/12 with
  n >= 48 rho^2 K/(c_flat(1-rho^2)). Then 1 + r^2[(1+rho^2)/4 + (1-rho^2)/12] = 1 + r^2(2+rho^2)/6 <= 1 + r^2/2 - r^4/8 iff
  r^2 <= 4(1-rho^2)/3, true for r^2 <= r_0^2 <= 1-rho^2; and s(rho r) + (1-rho^2)r^2/12 <= s(r) by Lemma lem:slack(a).
* |r| >= r_0: extra <= eps_j + 2 rho K T_j|r|/n <= (1-rho^2) r_0|r|/3 <= (1-rho^2) min(r^2,|r|)/3. Checked.
* Averaged data: d-neutral two-piece data at f_j (all defining conditions are linear or convex, d^{(j)} linear); Gamma^{(j)}_w convex;
  rho^2(1 + eta_0/2) <= 1. Corollary cor:D1 at f_j (F finite, I finite) gives (f_j, rho gbar_j) in cl NA, and (f_j, rho gbar_j) -> (f, rho g).
Comment: (E-e) is natural: eps_j enters only through pieces finer than the probing scale, which exist exactly for |r| >~ T_j 2^{-n_j}.
Theorem E is a clean, correct and useful generalization of the mechanism of Theorem thm:S (f_j = f).
Observation (used in part 4 below): Theorem E allows ANY sub-window (T_j, n_j); it is not tied to the design windows. Hence in
Corollary 3.4 the bottom T_lo(l_j) of the design window may be replaced by 2^{-n_j}T_hi(l_j) for any n_j <= n^w_{l_j} with
n_j/((1 + C_H)K_*) -> infinity ("top sub-window"); the exactification threshold then becomes theta 4^{-n_j} T_hi(l_j)^2 with n_j ~ psi K_*,
instead of theta 4^{-n^w} T_hi^2. This is what the notes' own gloss "tower gaps: r_next <= exp(-C prod(1/r))" (4.3(i)) actually needs.
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
# Z3 referee, part 3 — Z3 parts 5-6 ((O1)(ii); peak-ification)

## 3.1 Observation 5.0. CORRECT.
With B finite, every quantity of Theorem thm:S involving bad carriers is a finite min/max: 1/(sigma|alpha(k(l))|) in Lemma
lem:badpeaks(c), gamma_B in Lemma lem:windowtwopiece, the Hoffman constant of a fixed finite system. Weak/near-threshold GOOD carriers
never matter (pinning uses rooms only; the window certificate clamps). So weak/near-threshold carriers are new only for B infinite.

## 3.2 Lemma 5.1 (inward block moves need no gap). CORRECT (any admissible T). Re-derived:
D W(s) = (1 + dsM/C) Dw + s h_perp, ||DW|| <= Y + s^2||h_perp||^2/(2Y), Y >= C/2, C/Y <= 1 + 2|ds|M/C. Sup norm: off supp omega
|W| = (1 - ds)|w| with equality (1 - ds)M at the peaks with alpha != 0 (they exist since ||alpha||_1 = 1 and are not in supp omega);
strict non-peaks need |s omega| <= gap/2 and 1 - ds >= 1/2; at k_0: varsigma W(k_0) = (1 - ds)|w(k_0)| - |s omega(k_0)| in
[-(1-ds)M, (1-ds)M] by the inward and no-overshoot conditions. First-order term: <W - w, zeta>/sigma = s omega(k_0) alpha(k_0) = 0.
Extensions (checked): finitely many inward coordinates (degenerate peaks or strict non-peaks, each inward with no overshoot) work
identically, and Lemma U / Lemma lem:onesidedtransfer extend (Lemma lem:TV is unaffected because ||W - w||_inf < gamma preserves signs on L).
Z3's numerics (check_inward.py) are consistent. My check of the multi-coordinate extension (Z3_ref_work/check_inward_multi.py: 3000
random blocks, two degenerate peaks and two strict non-peaks of gap 1e-6..1e-3 moved inward with no gap condition, plus two ordinary
non-peaks): max[(N(W) - 1) - bound] = 2e-16, max |<W - w, zeta>|/s = 3e-13, ||W||_inf = (1 - ds)M exactly.

## 3.3 Identity 5.2 (d-shift with bad peaks). CORRECT. Re-derived from (eq:didentity), Lemma lem:modswallow(a) and (eq:peakshift):
for a bad peak q_l = eps_l Phi varsigma_l M/(mC) and varsigma_l eps_l tau_l/lambda_l = Delta d M + e_l, hence q_l tau_l = (Phi^2 M/C)(Delta d M + e_l).
Requires B finite with l_* >= max B (no fine bad terms), as stated.

## 3.4 Theorem 5.3 (weakened (H2)/(H3), B finite). CORRECT.
I checked that (H2), (H3) enter the proof of Theorem thm:S only through Lemma lem:badpeaks (a) [used again in Lemma
lem:windowtwopiece(b) for |Delta d|M and the coarse peak terms], (c), and the peak rows of the violation estimate in Lemma lem:exactswitch.
(A_m): Lemma lem:badpeaks(a) holds by (H2) at m. By 5.2, sum_{bad peaks}(Phi^2M/C)e_l = -sum_{np} q tau - Delta d M(1 + S_P) + r'; with all
q >= 0, -sum q tau <= sum q (tau)_- and (tau_l)_- <= c(tau)/(2 m_l) = O(K_* t) (cost function of Lemma lem:exactswitch, valid without
(H1)); all e_l >= 0, so each e_l = O(K_* t)/Phi_l^2 and, at a degenerate bad peak with varsigma = eps, tau_l = lambda_l(Delta d M + e_l) =
O(K_* t) (constants depend on the finitely many Phi_l). The q >= 0 hypothesis is exactly what bounds -q tau from above (tau_+ is only
box-bounded). (B_m): with q = 0 on bad non-peaks, 5.2 gives |Delta d|M (1 + S_P - (M/C) sum_deg Phi^2) <= O(K_* t) in the case Delta d < 0
(non-degenerate bad peaks: e_l <= t/(sigma|alpha|); degenerate ones (varsigma = -eps): e_l <= (tau)_-/lambda + |Delta d|M), and trivially
when Delta d >= 0; the coefficient is >= 1. The d-row of block m is then vacuous. Everything else in the proof of Theorem thm:S is
unchanged. Minor: "O(t)" in the notes should read O(K_* t) (harmless; K_* is the window constant).

## 3.5 Theorem 5.4 (infinitely many bad peaks). CORRECT.
Checked: Lemma lem:modswallow(a),(b) and the unified triangular system need only z = eps_l on S_l \ F and (H1); Lemma lem:badpeaks(a)
with K_d <= C + K_*/lambda_{l°} <= C'K_* (the notes' "K_d fixed" means: up to the factor K_*, which is how it enters K_pk); non-degenerate
bad peaks: |tau_l| <= t/mu_{k(l)} + lambda_l K_d t (by (eq:margin), sigma|alpha(k)| = lambda_k mu_k); degenerate (varsigma = -eps):
tau_l <= lambda_l K_d t and sum (tau_l)_- <= K_* t. Projected data tau' = (tau)_+ on B_np, 0 on B_pk: V' z-signed in K (resonance), d-rows
vacuous (q = 0 on B_np, tau' = 0 on B_pk), ||Delta B 1_{F^c} - V'||_1 <= K_pk t; Lemma lem:windowtwopiece goes through (bad coarse peaks:
omega^+ = 0, lambda rho_k <= |tau_l| + lambda|Delta d|M; B_np gaps equal M). (W*_pk) gives K_pk T_hi -> 0 and n^w/K_pk -> infinity.
"Inverse margins enter additively": correct and a genuine improvement over a triangular treatment.

## 3.6 Section 5.5. (i) CORRECT (peak data are inward on both sides by Lemma lem:suplevel(c)). (ii) SKETCH — coherent:
at f^#_j the former degenerate peak is a strict non-peak of tiny gap; inward data need no gap for Lemma U (3.2 above); Corollary cor:D1 is
applied at each fixed f^#_j, where a tiny gap only shrinks T_0(f^#_j), which is allowed; the tuning perturbation on a fine good
signature set S_{l'} (l' > l_*) does not change u_l(zhat) for coarse l (allowedness (a)) and costs -> 0 as l' -> infinity. Missing, as
stated: a first-order statement that some such perturbation moves vartheta_m in the required direction (it does not follow from
what is written; the clamp equation can move vartheta_m either way). Also needed: (BS)-type status preservation of the other coarse
carriers under the tuning (fine for small shifts unless another coarse carrier is exactly degenerate).

## 3.7 Section 5.6 (OPEN items). Accurate. (b) "exact two-piece data need Delta d_m != 0, impossible when block m has a good carrier with
w != 0": correct (R_m^* w_m carries the good signature mass on roomy sets).

## 3.8 Proposition 6.1 (peak-ification). SKETCH — correct as labelled; the PROVED sub-case is fine.
Checked: pushes on S_l (l >= L) are invisible to u_{l''} for l'' < l (allowedness (a), disjointness), so |u_l(zhat_L)| >= A_l survives
later pushes; choosing the push sign sigma_l maximizing sum v_l(s)(1 - sigma_l z_s) (>= ||v_l 1_{S_l\F}||) gives the needed range
[0, delta°_l] for x_l (the notes' "carry v_l-mass >= ||v||/2 ... after shrinking kappa" is imprecise; measure the available push by
sum v_l(s)(1 - sigma z_s), which is >= ||v_l 1_{S_l\F}|| for the better sign); (D*) needs c_l(3 theta + psi_l) <= delta°_l/8, i.e. (D*)
with psi replaced by psi + 3 theta (harmless); p*(f_L - f) -> 0 by Lemma 3.1 (Delta <= 2 sum_{l>=L} lambda_l, so |theta^L - theta| <= C
sum_{l>=L} lambda_l: no logarithm needed); (MS) at f_L holds because psi_l -> infinity and Phi decreases (super-)geometrically along each
block. The status of the finitely many l < L is preserved when sum_{l>=L} lambda_l = o(min_{l<L} margin/gap terms); the notes' sufficient
condition is correct. In general exact degeneracy at f_L must be avoided by a genericity argument that is not written: SKETCH.
(D*) "can be arranged": plausible (choose S_l recursively avoiding earlier target supports, with min S_l bounded in terms of c_l; the
admissibility proof then goes through because allowedness (a) only requires later S_{l'} to avoid earlier targets). For natural choices
(e.g. S_l = prime powers) (D*) holds automatically, since c_l <= T_lo(l-1)^3 <= 2^{-6/delta°_{l-1}}.

## 3.9 Corollary 6.2. CORRECT but nearly tautological (Lemma Z is per mate; G-approximants exist by 4.2 / 6.1). The phrase "every such
approximant is a companion of f at distance >~ c_L log(1/c_L)" is a LOWER bound that is not proved (Lemma 3.1 gives upper bounds): HEURISTIC.
# Z3 referee, part 4 — the band is a design artifact: explosive windows (new; PROVED unless marked)

Z3 4.3(ii)/7.1 claim that a carrier whose room lies in the band theta T_lo(l_*)^2 << r_l << 1/K_*(l_*) defeats the window method, that
"every design has band carriers for suitable f" and "no choice of design removes it". The first claim (per window) is right; the
design-independence is FALSE. The point: with the SLD window lengths n^w_l ~ l 2^{l^3} Lambda°(l), the bands of consecutive windows
overlap enormously (lower end ~4^{-n^w_l}, upper end ~2^{-l^{2.5}/N}), so ONE carrier blocks ~l^{1.6} consecutive windows and a sequence
of carriers can block all of them. If instead the window-length function grows explosively, the bands become pairwise disjoint, each
carrier blocks at most one window, and since there are far fewer carriers of p_N below L than window indices below L (blocks m > N
also index windows), infinitely many windows are band-free for EVERY f.

## 4.1 The explosive variant (D1^F) of Definition def:SLD.
Keep (D0), allowedness, y_l, n_l, u_l, delta°_l, Lambda°(l) and (D2) unchanged. Replace the factor l 2^{l^3} by a design function F(l):
   n^w_l := ceil(F(l) Lambda°(l)),  T_hi(l) := min{T_lo(l-1), 1/(F(l) Lambda°(l))},  T_lo(l) := 2^{-n^w_l} T_hi(l),
   c_{l+1} := min{c_l/4, T_lo(l)^3},
with F(1) := 2 and, recursively (all quantities on the right are fixed at stage l),
   F(l+1) := max{ F(l)^2, (l+1) 2^{(l+1)^3}, b(l)^{-4(l+1)} },
   b(l) := 4^{-2 n^w_l} T_hi(l)^4 delta_min(l) 2^{-s_max(l)} / l,   u(l) := F(l)^{-1/(4l)},
where delta_min(l) := min_{l'' <= l} delta_{l''} and s_max(l) := max of the union of supp y_{l''}, l'' <= l (finite sets; s_max := 1 if empty).

Lemma 4.1.1 (survival). PROVED. Theorem thm:SLD holds for (D1^F), with (P3) replaced by (P3^F): T_hi(l) F(l) Lambda°(l) <= 1,
n^w_l >= F(l) Lambda°(l), T_hi(l+1) <= T_lo(l). Every result of Section 8 of the note, and every result of Z3 parts 1-6, holds for
(D1^F) after replacing l 2^{l^3} by F(l) in (W+-), (W*), (W*_pk) and in the window-growth conditions.
Proof. The admissibility proof uses only (D0), allowedness (a),(b), c_{l+1} <= c_l/4 and delta_l, n_l; (P1), (P2) are unchanged. In all
recovery proofs (Theorems thm:R0, thm:Bstar, thm:Bpm, thm:S, Z3 Theorems 5.3, 5.4, Corollary 3.4) the window factor enters only through
T_hi(l) * Q_f(l) Lambda°(l) -> 0 and n^w_l / (Q_f(l) Lambda°(l)) -> infinity for f-dependent factors Q_f(l) <= C_f^{l^2} (e.g.
varpi_0^{-l^2}, (3/(2 gamma))^l), or through the (W)-conditions themselves; F(l) >= l 2^{l^3} >= C^{l^2} eventually gives both. The box
bound sum_{l > l_*}|Delta theta_l| <= 6 t^2 uses only c_{l_*+1} <= T_lo(l_*)^3, kept. QED

Lemma 4.1.2 (disjoint bands). PROVED. u is nonincreasing, b(l) < u(l), and u(l') <= b(l) for all l < l'. Hence the open intervals
Band(l) := (b(l), u(l)) are pairwise disjoint.
Proof. u(l+1) = F(l+1)^{-1/(4(l+1))} <= F(l)^{-2/(4(l+1))} <= F(l)^{-1/(4l)} = u(l) (as 2l >= l + 1), and u(l+1) <= b(l) by the third term
of F(l+1). b(l) <= 4^{-2n^w_l} <= 4^{-2F(l)} < F(l)^{-1/(4l)} = u(l). For l < l': u(l') <= u(l+1) <= b(l). QED

## 4.2 Band-free windows exist for every first row.
Proposition 4.2.1. PROVED. Let (D1^F) be as above, N >= 1, and let (rho_l)_{l in L_N} be any numbers in [0, infinity] (in the
application rho_l := r_l/delta°_l, a property of f). Call a window index l_* BLOCKED if some l in L_N with l <= l_* has
rho_l in Band(l_*). Then at most |L_N cap [1,L]| indices in [1,L] are blocked; hence infinitely many indices are not blocked.
Proof. By Lemma 4.1.2 each rho_l lies in at most one Band(l_*), so choosing for each blocked l_* <= L one blocking carrier l <= l_*
defines an injective map into L_N cap [1,L]. The number of unblocked indices in [1,L] is therefore >= |[1,L] \ L_N|, which tends to
infinity because N \ L_N = {l : m(l) > N} is infinite (frak j is a bijection of N x N and N is finite). QED
(For the original design this fails: under the conditions (G1) gaps of L_N are O(l^{1/2}) and (G2) delta°_l >= 2^{-l^2}, the rooms
r_l = 2^{-l^4} delta°_l, l in L_N, block every window; see part 2, 2.7.)

## 4.3 What an unblocked window gives.
Proposition 4.3.1. PROVED (conditional). Let f in S_{p*} have F finite, a finite exactly swallowed set B, and sign-mixed rooms r_l > 0 for
l in L_N \ B; put rho_l := r_l/delta°_l. Let l_* >= l_0(f) be unblocked, and let
   E := {l in L_N cap [1,l_*] \ B : rho_l <= b(l_*)},   P := {l in L_N cap [1,l_*] \ B : rho_l >= u(l_*)}
(so the coarse carriers are B u E u P), let eps_l (l in E) be the sign minimizing sum v_l(s)(1 - eps z_s), and let f^# be the coarse
exactification of f with A := E (Z3 part 3). Then:
 (a) K_* := (1/q_0 + 22) Lambda*_{f,B'}(l_*), B' := E u B, satisfies K_* <= C_f^{l_*} F(l_*)^{1/4} Lambda°(l_*), PROVIDED
     (S-flat) r*_l >= r_l/2 for every l in P (r*_l computed with B'): the targets of later B'-carriers carry at most half of the room of S_l;
 (b) c(delta) + Delta <= theta(l_*) T_lo(l_*)^2 with theta(l_*) := C(T_lo(l_*)^{1/2} + 4^{-n^w_{l_*}} T_hi(l_*)^2) -> 0, and Delta <= c_f;
 (c) consequently, if along infinitely many unblocked windows l_j the remaining hypotheses of Proposition T hold — (S-flat), (H1),
     (H2), (H3) for B'_j, the status part of (BS) with a uniform gamma_B, and (HF) with C^#_{H,j} <= F(l_j)^{1/2} — and the B'_j-dependent
     constants of fixes T4, T6 satisfy C_0^# + sum_{l in B'_j, nondeg. peak} 1/mu_{k(l)} <= F(l_j)^{1/4}, then f in Rec.
Proof. (a) For l in P, r*_l >= r_l/2 >= u delta°_l/2, and 1 + 6/(u delta°) <= (7/u)(1 + 2/delta°) (u <= 1). For l in B', r*_l :=
||v_l 1_{S_l\F}||_1 (fix T2; for l in B the note's 2||v|| is even better) >= c_F delta°_l, where c_F > 0 accounts for the finitely many S_l
meeting F; so 1 + 3/r*_l <= (3/c_F)(1 + 2/delta°_l). Multiplying, Lambda* <= (7/u)^{|P|}(3/c_F)^{l_*} Lambda°(l_*) and u^{-|P|} <= u^{-l_*}
= F^{1/4}. Hence K_* T_hi(l_*) <= C_f^{l_*} F(l_*)^{-3/4} -> 0 and n^w_{l_*}/K_* >= F(l_*)^{3/4} C_f^{-l_*} -> infinity.
(b) delta lives on the sets S_l \ F, l in E, with |delta_s| = 1 - eps_l z_s and r_l = sum_s v_l(s)|delta_s|, so |delta_s| <= r_l n_l 2^s/delta_l.
For a carrier l'': the signature part of u_{l''}(delta) vanishes unless l'' in E, where it is eps r_{l''}/... of modulus <= r_{l''}; the target
part sees S_l only if l < l'' (allowedness (a)); for l'' <= l_*, |y_{l''}(delta)| <= ||y_{l''}||_1 max{|delta_s| : s <= s_max(l_*), s in S_l, l in E}
<= (5/4) max_E r_l 2^{s_max(l_*)}/delta_min(l_*). Since r_l <= rho_l delta°_l <= b(l_*) for l in E (delta° <= 1):
sum_{l'' <= l_*} min(lambda_{l''}, |u_{l''}(delta)|) <= 3 l_* b(l_*)(1 + 2^{s_max}/delta_min) <= 6 * 4^{-2n^w} T_hi^4 = 6 * 4^{-n^w} T_hi^2 * T_lo^2,
while carriers l'' > l_* contribute <= sum_{l''>l_*} lambda_{l''} <= T_lo(l_*)^3 ((P2)). The same bounds give Delta <= (tiny) + 2 T_lo^3, so
Delta log(e/Delta) <= C T_lo^3 log(1/T_lo) <= C T_lo^{5/2}. Summing gives (b); Delta <= c_f for l_* large.
(c) Proposition T applies at f^#_j with these K_*, theta (pinning (P) holds with K_* by (S-flat); (BS)-cost by (b)); with fix T6 its
frozen-error constant is K^#_* <= K_* + F^{1/4} <= 2 C_f^{l} F^{1/4} Lambda°. Corollary 3.4 needs (1 + C_H)K^#_* T_hi -> 0 and
n^w/((1 + C_H)K^#_*) -> infinity, which hold since (1 + F^{1/2}) 2 C_f^l F^{1/4} Lambda° / (F Lambda°) <= 4 C_f^l F^{-1/4} -> 0;
(E-e) holds with theta_j -> 0. QED

## 4.4 Assessment.
* For (D1^F) the band of Z3 4.3(ii) never occurs at unblocked windows, and unblocked windows exist for every f (Proposition 4.2.1).
  So Z3's "main obstacle" 7.1 is an artifact of the window-length function l 2^{l^3}.
* What remains of (O1)(i) for (D1^F) is EXACTLY the companion-cone problem for the growing finite sets E_j of nearly exactly swallowed
  carriers: slaving conditions ((S-flat), (H1)), non-degeneracy ((H2), (H3)), status stability ((BS)), and a Hoffman bound
  C^#_{H,j} <= F(l_j)^{1/2}. This is the same type of difficulty as the open part of Theorem thm:S (Remark rem:S(c); (O2) with exact
  swallowing): (O1)(i) merges into (O2) for the explosive design.
* It does NOT solve (O1)(i): Hoffman constants are f-dependent and cannot be dominated by a design function chosen before f; and by
  Z3 Lemma 1.4 an E-carrier that is d-neutral at f with positive defect makes the cone at f^# degenerate (C_H >= |R^**zhat^#|/Re(u_l),
  with Re(u_l) <= b(l_*) — astronomically large). Re-tuning e (Z3 4.3(iii)) has only |F| - 1 degrees of freedom while supp a = F is
  kept (needed for Lemma U), so at most |F| - 1 such carriers per window can be re-tuned without adding base coordinates.
* Status: PROVED: Lemmas 4.1.1, 4.1.2, Propositions 4.2.1 and 4.3.1 (as a conditional statement). HEURISTIC: that (HF) with
  C_H <= F^{1/2} is "typical" (it holds e.g. when, in every block, the E-carriers are strict non-peaks whose weights q_l are bounded
  below by a design function of l and all have the same sign — then the projection is the explicit d-pinning tau_l <= O(K_* t)/q_l —
  but status stability and slaving remain to be checked case by case).
