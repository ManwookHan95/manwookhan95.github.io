# X1-ref part 3 — Proposition KN^tr, design T^tr / Lemma W', Theorem S1

## 1. Proposition KN^tr.  Verdict: CORRECT modulo fixable gaps (W-fix of part 2, D2, Q2, Q3, and S-0 below).
Re-derivation of the chain (one clean sub-window w of a main stage L >= l_f, one class a, pattern kappa).
Step 0.  V1's (C1), (C2); active weak peaks of (T)-blocks pushed to rho = 1 - b (value change <= 2 b theta Phi^2, ratio change O(b) in the
formula-1 convention, part 1 K1).  At f_1: every tiny minor <= (1 + Lip C_*) b; every d in N_T has rho_d(f_1) <= 1 + C_* b.
Step 1.  V2 Lemma L (semialgebraic form, Q3) gives r' in Z_kappa with |r' - r_1| <= C_L((1 + Lip C_*) b)^{2/N_L} <= eta'/3 ((D1);
alternative (i) of Lemma L is excluded by b < 1/C_L).  F(r_1) = max_d rho^0_d(r_1) <= max_d rho_d(f_1) by LEMMA F ALONE (no (T)-hypothesis
needed here), so F(r') <= 1 + delta_0(b).
Step 2.  delta_0 < m_0 (D2): Y_1 is non-empty (else F >= 1 + m_0 on Z, contradicting F(r') <= 1 + delta_0); Lojasiewicz (QC(b)) gives
r_1' in Y_1 with |r_1' - r'| <= C_Y delta_0^{alpha_Y} <= eta'/3.
Step 3.  QC(a) with h = eta'/3 (Q2: h <= h_kappa) gives r'' in Z with |r'' - r_1'| < eta'/3 and F(r'') <= 1 - mu_kappa(eta'/3).
So |r'' - r_1| <= eta', r'' in Z_kappa (all tiny minors and tiny cofactor polynomials vanish), robust ones >= u - Lip eta' >= u/2 (eta' <<
u: T_lo(w) <= 2^{-Q(w)}), and the signs of the r_d are those of r_1 (|r_d| ~ Phi_d/(m K) >> eta').
Step 4 (realization).  (T)-blocks: inactive Omega carriers (all nearly neutral) to value 0 [V2 Theorem B makes tiny rays exactly zero; even
without it they contribute only O(D^2 b^2), part 1 (b)]; V1 Lemma TU sets u_l(zhat) = r''_l kappa (fixed point in kappa: d kappa/d(value of an
Omega carrier) = rho M X/C = O(D^2 c_{L+1}^2), U1 Lemma 1.4(c)); a peak push restores kappa (continuity, U1-ref 1).  Statuses: Lemma K with
sigma = sigma_rob + O(c_{L+1}^2) (fine peaks and fine strict non-peaks only: at a clean sub-window there is no coarse carrier with rho in
(b, u) ∪ (1 + b, 1 + u), active near-threshold peaks were pushed, inactive near-threshold carriers do not exist in (T)-blocks) and R^2 = R_a^2
gives rho_d(f^#) <= F(r'') + C D^2 c_{L+1}^2 <= 1 - mu/2.  (U)-blocks: targets s_m r''^(m) (D1 of part 2: cofactor polynomials scale by s^e,
e <= n); in addition push the inactive near-threshold carriers of (U)-blocks inward by eta' (D2).  (KN)-blocks: U1-ref's lever with eta' in
place of eta (s_0 = C D eta' theta Phi_P^2/(rho_{d_0} M); capacity |zeta(d_0)| >= u theta/D^2 >> s_0).  F involves only (T)-block ratios, so
the (U)-rescaling and the (KN)-levers do not change it; each block's statuses depend only on its own ratios (Lemma K).
Costs: values move by <= eta' (ratio units) plus O(b): V1 Lemma CO / TU(d) give p*(f^(1a) - f) <= C_f Design eta' log(1/eta') = o(T_lo^2).
S-0 (drifts after (1a)).  The later steps of U1-ref's companion ((1b) absorbers, (1c) kappa/ratio restoration, (2) fine structure, G1
release) move the block data by <= C Design(L) c_{L+1} (U1 Lemma 4.5/4.6 with U1-ref 5).  The (T)-block margin mu/2 must dominate this; X1's
(D3) only compares c_{L+1} with mu/D^2.  It suffices: c_{L+1} <= b(L, M(L))^2 ((W2)) <= b(w)^2 and b(w) <= mu/(8M) ((D2)), so Design c_{L+1} <=
Design mu^2 << mu because mu <= Lip eta' << 1/Design (Q1).  So (D3) can be replaced by (W2) + (D2); no new weight bound is needed.
KN-1 (exact HOLD of the inactive values in (T)-blocks; a needed precision).  The (T)-block margin mu(eta'/3) >= c_kappa (eta'/3)^{beta}
has a NON-EXPLICIT Puiseux exponent beta and may be much smaller than eta'^4.  The other blocks' moves (pulls, banks, levers, rescalings
of size ~ eta') act on a (T)-block only at second order through the Hilbert part (V1 Lemma B: remainder <= C Design^2 x size^2), i.e. by
~ Design^2 eta'^2 on values.  For the ACTIVE ratios this is harmless (the joint TU fixed point realizes r'' exactly), and sigma depends only
on the peak SET.  But an inactive Omega carrier that is "pushed to 0" once and then left alone ends with a value ~ Design^2 eta'^2, which
enters R^2 and moves the active statuses by ~ D^2 Design^4 eta'^4: this is NOT << c_kappa (eta'/3)^beta when beta > 4.  Fix: put the inactive
Omega carriers of (T)-blocks into the joint fixed point with target value EXACTLY 0 (two-sided tuning: V1 Lemma TU for exactly swallowed
carriers, far z-moves for carriers with room; V2 Theorem B does exactly this for tiny objects; U1 already holds its absorbers at value 0 in
(1b)-(1c)).  Then R^2 = R_a(r'')^2 exactly and only fine terms (<= C c_{L+1}^2 << mu) separate rho^# from rho^0(r'').  In (KN)-blocks (margin
c_f D eta' M) and (U)-blocks (margin eta') the second-order effects are harmless.
Order of quantifiers: design (weights generic, constants of all level-L patterns, then b(w), then c_{L+1}) -> f -> main stage L, clean w
(depends on f only: the new minors are rate objects of f for EVERY pattern and class) -> g, rho -> class a and pattern (pigeonhole over
scales) -> companion (depends on the class: legitimate, Lemma Z is per mate) -> data at each t.  Checked.

## 2. Design T^tr and Lemma W'.  Verdict: CORRECT with precisions W1-W4.
W1 (option (a) is outside the note's class).  The note's def:admissible (T-a) reads "q*(Te_{n,m}) <= 1 for all (n,m), WITH EQUALITY FOR SOME
(n,m)", and Martin's Lemma B produces a NORM-ONE T.  Under option (a) c_1 < 1, so T^tr(a) is not admissible in the note's sense; the norm
p built with it is a Martin-type norm (Martin's proof uses only ||T|| <= 1: v*_{n,m} in B_Y, ||Phi_m||_1 <= 2^{-m} < 1, |R_m x|_m <= m 2^{-m}
|||x|||, norm density of the normalized vectors — I re-checked these against the summary of Martin's paper), but results for option (a) are
results for that relaxed class.  Rescaling T^tr(a) by 1/c_1 gives an admissible operator with c_1 = 1 rational, i.e. option (b).
W2 (a cheap fix for N = 1 inside the note's class).  The only rational weight under option (b) is that of carrier 1, of block m(1).  The
ladder bijection j of T_final (U4 1.2(i)) only needs j(k, m) < j(k', m) for k < k'; nothing on the dependency trees uses m(1) = 1 (block-1
absorbers of D^{U1'} are later carriers; (GM) is imposed only for l >= 2; with m(1) = 2 (GM) at l = 1 would force c_1 <= 2^3/240 < 1, so
U4's fix C7 is still needed and suffices).  Choose j with m(1) = 2 (e.g. j(1,2) = 1).  For p_N with N < m(1) no carrier of rational weight
occurs in any pattern (rate objects of carriers of blocks > N are constant, V1-ref p0), so Lemma GEN applies to all patterns.  Hence, for
N = 1, Corollary IV^tr.1 holds for an operator T^tr(b) that IS admissible in the note's sense (equality in (T-a)).  For N >= m(1) the
carrier-1 exception of X1 4.3 (R1) remains OPEN.
W3 (absorber sizes).  D^{U1'} chooses the number R of absorber coordinates from c_p^low by 2^{3-R} <= mu_{p_0}^2 c_p^2/4, a LOWER-bound use of
c_p.  With c_p in [(1 - 2^{-p}) c_p^max, c_p^max] and possibly c_p^max = c_p^low, R must be computed from (1 - 2^{-p}) c_p^low (R grows by at
most 1; R is still fixed before c_p, and (W6) is not imposed at absorber stages).  Cluster weights c_{p+i} := c^low_{p+1} 4^{1-i} must be read
as c_{p+i}^max := min(c^low_{p+1} 4^{1-i}, c_{p+i-1}/4) so that (W1) holds with the perturbed predecessor.  X1's "constants change by factors
<= 2" is right once these two readings are made explicit.
W4 (where lower bounds of weights are used).  Besides X1's list (s_1 = T_lo^8 c_l in U3-ref RT*(f) and (VT) c_l >= C' D T_lo; absorber
capacity c_{L+1}/(Design t); block-1 ratio in U1-ref 7, which follows from (W1) and the factor 2^{-k}), U4-ref C2-C6 states that only
design-computed lower bounds (lambda >= 1/D(l), computed after c_l) are used on the trees of MT II / III' / RS'; I found no other use.
Well-foundedness: c_l^max is computed from the actual earlier data; the countable field k_0(c_1, ..., c_{l-1}) cannot exhaust an interval;
N-freeness unaffected.  The rate scheme gains finitely many objects per level (pigeonhole form unchanged), b(w) only decreases (u(w^+) = b(w),
Q(w) adapts), so U4-ref's Lemma GW applies.

## 3. Theorem S1.  Verdict: CORRECT as a consequence of Proposition KN^tr and U1-ref (precision S1-a).
(a) and (b) are Proposition KN^tr plus V2 Lemma H (least nonzero minor >= u/2 after exactification; dimension and entries design-bounded) and
U1-ref 4.3 (Cauchy-Binet for A_max).  (c) is the identity of U1 Lemma 1.3 (with Lemma 1.1 it shows that the coupling rows Delta_m = d^#(Domega)
are EQUIVALENT to (X3) for data supported in Omega), so "the coupling rows hold inside the cone" is automatic once (X3) is a row of the cone;
the substance of U3-ref's open item (S1) is the Hoffman control of the cone containing all rows (X3) when >= 2 blocks are shifted or no free-ray
carrier exists, which is exactly what failed in U1 Theorem 2.3 through the statuses and is now supplied by KN^tr.  RT*(c): the residues on the
coarse coordinates are cancelled per scale by the absorbers' switching coefficients (U1 Prop. 3.4, U1-ref G1 release); their bound does not
depend on the configuration, so the statement holds for every class.
S1-a: for MIXED classes the fine structure (step (2)) is not provided by U1-ref (it is X2's C_mix); Theorem S1 claims only the coarse part and
RT*(c), which is consistent; it must not be read as "mixed classes recovered".
