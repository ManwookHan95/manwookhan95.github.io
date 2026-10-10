# Q1 referee (b) — part 1: design T_fin, Theorem A_fin (working file)

## 1.1 Re-derivations that check out (PROVED, re-derived independently)
B1 (lb_l <= c^max_l at PRE stages).  c^low_l replaces (W3) (delta_l H_l)^2 by (delta^max_l H_l/2)^2 and delta_l by delta^max_l/2 in (W5);
   since delta_l in [delta^max_l/2, delta^max_l] ((GM) interval), each replaced bound is <= the true one; the other entries coincide
   ((W1), (W2), (W4'') at the pair's own s, (W7) — target-independence of (W7) to be checked against U4 1.3(4)).  Hence
   lb_l = (1 - 2^{-l}) c^low_l <= (1 - 2^{-l}) c^max_l <= c_l.  CORRECT.
B2 ((GM) value well defined, in Q(y(j))).  g_l = delta^max_l H_l/(32 * 3^{|supp y|}); each of the 2 * 3^{|supp y|} pairs (sigma, eps)
   excludes an open delta-interval of length 2 g_l/H_l = delta^max_l/(16 * 3^{|supp y|}); total excluded length delta^max_l/8 <
   delta^max_l/2, so the admissible set in [delta^max_l/2, delta^max_l] is a nonempty finite union of closed intervals; its maximum is
   delta^max_l or an endpoint (eps' g_l - sum sigma_j y(j))/(eps H_l), in Q(y(j) : j) because delta^max_l, H_l, g_l are rational
   (H_l = 2^{-3 * 2^l}/(1 - 2^{-2^{l+1}})).  CORRECT.
B3 ((T-b), (T-c)).  For s in S_{l'}: targets of stages l <= l' vanish at s (allowedness (a)); signature vectors other than h_{l'} vanish
   on S_{l'}; every target meeting s at a stage l > l' obeys (W4) (PRE/MAIN: (W4''); cluster: c^cl contains (W4'') for all of E^ch(p)).
   With ||y_l||_1 <= q^*(y_l) = 1, n_l in [3/4, 5/4] and c_l <= c_{l-1}/4:
   |Z(s)| >= c_{l'} delta_{l'} 2^{-s} (|x_{l'}|/n_{l'} - (8/9) ||x||_inf 2^{-s}) > 0 for all large s in S_{l'}.  Z in c_00 forces x = 0.
   CORRECT (re-derived; the argument needs only (W4) and allowedness (a) for EVERY target, absorbers included — verified below).
B4 (allowedness (a) for absorber targets).  PRE pair of round r: s in Sigma(Y_r) has s <= p - 2|supp Y_r| - 1 <= l_r < l by (c+), and
   s in S_{l''} forces l'' < min S_{l''} = 3 * 2^{l''} <= s.  Cluster pair of main stage p: s in S_{l''} ∩ [1, p] gives l'' < s <= p < l;
   s in T(p) ∩ S_{l''} gives l'' < (stage of the target containing s) <= p (allowedness (a) of that target).  p_0..p_R odd, odd
   integers lie in Z_0 (S_l consists of even numbers).  CORRECT.
B5 (norm).  q^*(T_fin e_{k,m}) = c_{j(k,m)} q^*(u_{j(k,m)}) = c_{j(k,m)}; (W1) and the cluster rule give c_l <= c_{l-1}/4 (l >= 2), so
   ||T_fin|| = sup = c_1.  Phi_m(k) = 2^{-m-k} c_{j(k,m)} <= 2^{-m-k}: ||Phi_m||_1 <= 2^{-m} < 1 (Lemma A).  CORRECT.
B6 ((T-d)).  Candidate y = y^(i) is allowed at round r as soon as l_r >= max supp y + 2|supp y| (then p - 2|supp y| - 1 =
   l_r + 2|Sigma(y)| - 2|supp y| >= max supp y gives (c+), and s in S_{l'} ∩ supp y forces l' < s < p, giving (a)).  Each m occurs
   infinitely often in (m_r), i_nu = i infinitely often, l_r -> infinity: infinitely many main stages of block m carry y^(i).
   q^*(u_l - y) <= |1 - 1/n_l| + delta_l q^*(h_l)/n_l <= C 2^{-l} H_l -> 0.  Y_pool dense in S_{q^*}.  CORRECT.

## 1.2 Points to check (open at this stage of reading)
P1 Allowedness rule (c) of U4/Y3 for ABSORBER targets: an absorber target has |supp y_l| = R + 2 with R ~ log(1/(mu_{p_0} lb_l)) >> l.
   If (c) reads "supp y_l ∩ S_{l'} ⊂ [1, l - 2|supp y_l| - 1]" then absorber targets whose s is a signature coordinate violate it.
   Which theorems on the tree use (c) for all targets?  (bounded gaps of S^nat?)
P2 (W7) at absorber stages: target-independent?  (needed for lb_l <= c^max_l)
P3 GENERICITY: is the coincidence set B_kappa of X1's Lemma GEN defined over k_0(other weights) WITHOUT any f-dependent datum
   (sigma_rob, R_a^2, the floor K(sigma_rob, R_a^2), aggregated signature rows at s_far(w))?  If any continuous f-datum enters the
   minors / psi_d, "weights chosen before f" does not exclude coincidences.
P4 R_cl(p) := 2|E^ch(p)| clusters: E^ch(p) includes S_{l''} ∩ [1, p] — finite.  OK.  But Design(l) contains 4^{R_cl(l)} 2^{k(l + R_cl(l))}
   — a forward reference to k(l + R_cl(l)) (the block-1 count after the cluster).  Is it computable at stage l?  (the round structure
   is determined by targets; the k-value of the last cluster stage depends only on the number of block-1 stages, which is fixed by
   R_cl(l) once l is a main stage) — check.

## 1.3 Resolution of P1-P4 (after reading U4 1.3, U1 3.1-3.4, U1-ref 6-7, X1 2.1-2.6)
P1 RESOLVED.  U4's allowedness (c) is "supp y ∩ S_{l'} ⊂ [1, l]" (signature coordinates of a stage-l target are <= l), not the margin form.
   Absorber targets satisfy it: PRE pair s <= l_r < l; cluster pair s <= p < l (s in S_{l''} ∩ [1, p], or s in T(p) ∩ S_{l''} and then
   s <= (stage of that target) <= p by (c) of that target, induction).  (c) is used only by Y3 3.4/3.5, V3 Sec. 1 (infinite F) and by Q1 2.3
   (W_lev: beyond s_max(L) no coarse target meets S_l) — the latter holds BY DEFINITION of s_max(L) = max T(L).  OK.
P2 RESOLVED.  (W7) of U4 1.3(4) is 3 * 2^{-10} tau_{l-1} lambda_{l-1} delta_{l-1} 2^{-(m(l-1)+k(l-1)+min S_{l-1})} eta_{l-1}/(n_{l-1}(1+||U||)):
   stage-(l-1) data only, target-independent.  So B1 holds: lb_l <= c_l.  Moreover each entry of c^low_l is >= 1/4 of the corresponding
   entry of c^max_l, so lb_l >= (1 - 2^{-l}) c^max_l/4 >= c_l/8.
P3 RESOLVED (positively).  B_kappa (X1 2.3) is defined from: u_l on E_c (in k_0 for EVERY coordinate, so the weight-dependent s_far(w)
   is harmless; beyond s_max the rows are aggregated with one nonzero entry each, coefficients in k_0), peak traces (peak vectors in k_0,
   peak weights = weights outside N_T), sigma_rob(m) = sum of Phi^2 over the pattern's robust peaks (weights outside N_T), signs and
   combinatorial labels, weights of (KN)-block carriers (outside N_T), and the ratio VARIABLES r.  No continuous datum of f enters:
   the f-dependence is entirely in WHICH pattern kappa occurs and WHERE r(f) lies.  Since B_kappa is fixed before f and the weights avoid
   it, the order "design -> f" is legitimate.  Also K_kappa (W-fix: R(m)^2 <= 1 - sigma_rob(m)/4) contains every relevant ratio vector:
   from a^2 = sigma + k^2 R^2, k = a + sigma one gets 1 - R^2 = sigma (1 + 2a + sigma)/(a + sigma)^2 >= sigma when a + sigma <= 1, and
   sigma >= sigma_rob - C c_{L+1}^2, so R^2 <= 1 - sigma_rob/2 at every row in question: interior margin for the eta'-moves.  (re-derived)
P4 RESOLVED.  k(l + R_cl(l)) at a main stage l: the stages l+1..l+R_cl(l) are block-1 cluster stages and R_cl(l) = 2|E^ch(l)| is a
   function of T(l) and the S_{l''}; hence k(l + R_cl(l)) = #{block-1 stages <= l} + R_cl(l) is known at stage l.  No forward reference.

## 1.4 R (absorber length) — precision to I3
Q1 I3 says "the only property of R used" is 2^{3-R} <= mu_{p_0}^2 c_l^2/4 (U1 Lemma 3.3 sweep).  Not quite: U1-ref 7 (owners inside absorber
blocks, used by route V's Step B through "U1-ref 7 covers owners inside absorber blocks") uses the LOWER bound eta_k >= mu_{p_0}^2 c_k^2/64 on
the absorber's least entry, i.e. an UPPER bound on R.  With R computed from lb_l: minimality of R gives 2^{4-R} > mu^2 lb_l^2/4 >= mu^2 c_l^2/256,
so eta_k >= 4 * 2^{-R}/q^*(x) >= 2^{-R}/2 >= mu_{p_0}^2 c_k^2/2^{13}: the constant 64 becomes 2^{13}.  U1-ref 7's chain
n(p'-1) >= Design(p'-1) >= (B_mu D)^6 >= (1/(eta_k lambda_k))^6 has slack (B_mu(l) >= 2^{p_0} / mu_{p_0}^2 with p_0 >= 11, D >= 1/Phi_k, sixth
power), so it survives.  PRECISION (no change of statement).

## 1.5 Weight bounds: complete list checked against U4 1.3(4), U1 3.1 (A4), U1-ref 6.2-6.3, X1-ref 8-9 (S-0, W3, W4), X2-ref (p-W)
UPPER bounds (all inside c^max_l, computed from the ACTUAL earlier weights; generic weights lie below them):
 (W1) c_{l-1}/4 [all stages; cluster rule min(c^cl 4^{1-i}, c_{p+i-1}/4) = X1-ref W3];  (W2) b(l-1,M(l-1))^2 [PRE/MAIN; at clusters only b(p,M(p))^2
 inside c^cl — sufficient because sub-windows are used only at main stages, and the only use is "c_{L+1} <= b(L,M(L))^2" for main L];
 (W3) (delta_l H_l)^2 [PRE/MAIN directly; cluster p+1 via (delta^max H/2)^2; clusters p+i, i >= 2: implied, U1-ref 6.3 arithmetic re-done:
 b(p,M(p))^2 <= 2^{-8 n(p,M(p))} while (delta_{p+i}H_{p+i})^2 >= 2^{-2(p+i)-2-6*2^{p+i}}, p+i <= 3p + 2 s_max(p), n(p,M(p)) >= p 2^{p^3} Design(p)
 >= p 2^{p^3} 2^{12 s_max(p)^2}];  (W4'') [PRE/MAIN with T_lo(l-1,M(l-1))^3; clusters with T_lo(p,M(p))^3 for every s of E^ch(p) — weaker than
 the literal (W4'') at p+i but this is all U1 Lemma 4.2(i) uses (U1-ref 6.2)];  (W5), (W7) [PRE, MAIN, cluster p+1];  (W6) [MAIN only;
 not at l = 1: U4 fix C7];  (W_exp) [c^cl only];  X1's (D3) = (W8) is NOT imposed: implied by (W2) + (D2) (X1-ref S-0), re-checked:
 c_{L+1} <= b(L,M(L))^2 <= b(w)^2 <= mu^2/64 <= mu/(8 C D^2) because mu <= Lip_kappa eta' << 1/(C D^2).
 Implicit upper bounds coming from allowedness + (W1): W_pull (carriers meeting a pull coordinate j_p are at stages >= j_p by allowedness (c),
 total weight <= (4/3) c_{j_p}); W_lev (carriers other than l meeting a lever coordinate j > s_max(L) are at stages > L BY DEFINITION of
 s_max(L) = max T(L) — not by (c), as Q1 2.3 says; harmless).
LOWER-bound uses (complete, X1-ref W4 + D^{U1'}): absorber sweep 2^{3-R} <= mu_{p_0}^2 c^2/4 (from lb <= c); absorber least entry (U1-ref 7,
 constant 64 -> 2^{13}, see 1.4); cluster capacity c_{L+i} >= (1/2) c^cl 4^{1-i} (induction re-done: prod_{j}(1 - 2^{-(L+j)}) >= 1/2);
 design-computed bounds (lambda_l >= 1/D(l), Phi_min(L) >= 1/D(L): D(l) >= 1/Phi_{l''} for all l'' <= l by definition) — computed AFTER the
 weights, so exact; s_1 = T_lo^8 c_l and (VT) c_l >= C' D T_lo: not on Master Theorem VI's tree (route V sets s_1 by Lemma S2c^tr).
 VERDICT: I1-I10 correct, with the precisions of 1.4 (R upper bound) and the wording point that (W5),(W7) ARE imposed at PRE stages and at
 the first cluster stage (Q1 1.7 says "not at absorber/cluster stages" — harmless inconsistency: more constraints only).

## 1.6 (W_exp) placement
c^cl(p) contains exp(-1/T_lo(p,M(p))), the smallest T_lo of main stage p; for every sub-window w of p, T_lo(w) >= T_lo(p,M(p)), so
c_{p+1} <= exp(-1/T_lo(w)) (needed form of (W-a)); later weights inherit by (W1).  Cluster stages p+i, i >= 2, are bounded by c^cl 4^{1-i}
(no new (W_exp) for their own, unused, sub-windows — X2-ref (p-W)).  Relation to b: b(p,M(p))^2 <= T_lo(p,M(p))^8 >> exp(-1/T_lo), so
(W_exp) is the binding entry of c^cl.  Compatible with absorber R (R computed from lb_{p+i} which contains (W_exp) — R larger, harmless)
and with the cluster capacity (ratios relative to c^cl, not absolute).  CORRECT.

## 1.7 (D-lev)
Factor max_{l''<=l} 2^{sigma_2(l)} n_{l''}/(mu_{sigma_2(l)}^2 delta_{l''}) in Design(l): for a lever coordinate j <= sigma_2(l) of S_{l''},
mu_j^2 v_{l''}(j) = mu_j^2 delta_{l''} 2^{-j}/n_{l''} >= mu_{sigma_2}^2 delta_{l''} 2^{-sigma_2}/n_{l''} >= 1/Design(l) (mu_s, 2^{-s} decreasing).
No weight enters (delta, n in k_0; sigma_2 an integer computed from T(l)).  CORRECT.  Caveat (precision): Step A of CM^tr may place its TU
pull and bank at the first two elements of S_l beyond s_max — exactly the lever coordinates allowed by (D-lev).  Then the Lemma-DC lever of
that carrier is a MASS change at the bank (efficiency mu_j^2 v_l(j)/nu, same order) instead of a z-move; two-sidedness holds while the bank
mass stays positive (mass >= c_f c_{L+1} >> lever moves C Design c_{L+1}? NO — lever moves are O(r) >> c_{L+1}).  So either enlarge (D-lev)
to the THIRD element beyond s_max (sigma_3) so that a fresh contact is always available (Step A uses at most two per S_l), or bound the
lever's downward range by the bank mass.  Simplest repair: (D-lev) with sigma_3(l) := third element beyond s_max; costs one more factor
2^{G(l)} in Design.  [FIXABLE PRECISION P-LEV]
 CORRECTION to the caveat P-LEV (after reading X2 2.3): X2's lever coordinate is j(l) := least element of S_l ∩ (s_max, inf) \ F^#, and
 X2 notes that inside (s_max, sigma_2(L)] the companion's support meets S_l at most in the FIRST element (a TU/donor bank); TU PULLS sit
 where v_l(j_p) ~ the needed value correction.  In Step A of CM^tr the corrections are O(eta' kappa) (active carriers), O(b theta Phi/m)
 (KN-1 holds of nearly neutral carriers) or ~ c_{L+1} (Q1's floor for the hold pull) — all << v_l(second element) >= delta_l 2^{-sigma_2}/n_l
 (b <= eta <= T_lo^4 <= 2^{-4 n(w)} and n(w) >= Design(L) >= 2^{6 s_max}).  So the pulls lie far beyond sigma_2(L), the bank (if any)
 is the first element, and j(l) (second element) is a free contact: (D-lev) with sigma_2 suffices.  P-LEV is NOT an issue.  Q1 2.3's
 phrase "every window of v-values of ratio 2^{3G} contains >= 3 elements" concerns the DC pull coordinates (v ~ r), also far beyond.
