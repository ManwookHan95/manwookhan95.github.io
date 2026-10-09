# Z6 referee, part 2: design D'', combinatorial Hoffman constants, Theorem U, gaps as a rate, 5.5, Prop P, Theorem V, Cor V.1

## 5.1 Design D''. CORRECT WITH FIXABLE GAPS.
Admissibility and survival of Section 8: correct (recursion well defined: Xi(l) uses y_{l''}, u_{l''}, c_{l''}, l'' <= l, all
fixed before T_hi(l); (P1),(P2) unchanged; old (P3) follows from Xi >= 1; Theorem SLD's proof uses only allowedness and
c_{l+1} <= c_l/4).
Gap D1 (N-dependence).  Xi(l) contains 8N 2^{m+k}/c_l, so D'' depends on N, but Lemma martintail needs ONE operator for
infinitely many N (same defect as Z4's SLD_G, found by the Z4 referee).  FIX: replace 8N by 4 m(l''): for every peak and
every strict non-peak with gap <= M/2 one has |q_l| = Phi|w|/(mC) >= (2^{-m-k}c_l)(M/2)/(m 2^{-m}) >= c_l/(4 m 2^k)
(M >= 1/2, C_m <= ||Phi_m||_1 <= 2^{-m} by Lemma A(b)), so 1/|q_l| <= 4 m(l) 2^{k(l)}/c_l, an N-free design quantity.
Gap D2 (F-part of the signature masses).  Z6 uses Sum_{l<=l*} 1/m_l <= C_f Sum 1/m^des_l(l*) with
m_l = ||v_l 1_{S_l \ (F u T_0)}||_1 and m^des_l(l*) = ||v_l 1_{S_l \ T(l*)}||_1.  This is FALSE in general for the finitely
many l with S_l ∩ F nonempty: if F contains min(S_l \ T(l*)) and later bad targets progressively cover the next points of
S_l (allowed by allowedness (b) when c is small), then m^des_l(l*) ~ v_l(min S_l) stays fixed while m_l(l*) -> 0 as l* grows,
so no l*-independent C_f exists.  FIX: m^des_{l''}(l) := ||v_{l''} 1_{S_{l''} \ ([1,l] ∪ T(l))}||_1 (> 0, design-computable);
for l* >= max F, S_l \ (F u T_0) contains S_l \ ([1,l*] u T(l*)), so m_l(l*) >= m^des_l(l*) (Z4 uses the same device:
m_l(U,n) with n = max F).  Same fix for the pair constants of 2.2 used in step (2) of Theorem U (X = c/(2 m_{l_i}(l*))).
Gap D3 ("D'' windows dominate SLD_G", 8.2).  FALSE as stated: SLD_G has n^w = (l 2^{l^3} Lambda°(l) G*(l))^6, D'' has
l 2^{l^3} Lambda°(l) Xi(l) with Xi only ~ (l H_comb G* ...)^4; if delta°_l is astronomically small (S_l far out), Lambda°(l)^5
dominates everything in Xi.  FIX: insert (l 2^{l^3} Lambda°(l) G*(l))^5 into Xi(l) (design-computable), or define the D''
windows as the maximum of both recursions.  Nothing else changes.

## 5.2 Combinatorial Hoffman constants. CORRECT (PROVED).
Hoffman (1952): for a fixed matrix A there is H(A) with dist(x, {Ax <= b}) <= H(A) ||(Ax - b)_+|| for EVERY b for which
the system is feasible; equalities are pairs of inequalities.  Here 0 is feasible for every b >= 0 (box rows).  The
matrices A_P have entries u_l(j), j in T_0 ⊂ T(l*), l <= l*, and signs/labels from a finite set; max over finitely many
patterns is a design quantity.  Patterns range over ALL subsets of [1,l*] (N-free, as required).  Patterns with
inconsistent labels only enlarge the max (harmless).  Numerical check of the Hoffman/Farkas machinery: see part 3.

## Theorem U. CORRECT WITH FIXABLE GAPS (re-derived step by step).
Checked: (1) e_0 and c(tau) <= t/q0 + 2||e_0||; (2) on S_l \ (F u T_0) only u_l among coarse bad vectors is nonzero
(P1 + definition of T_0), z = eps_l, so 2 (tau_l)_- m_l <= c(tau); (3) anti-sign peaks: tau <= lambda K_d t from
(peakshift); uncompensated blocks: 2.4 with A = O(t) (good K* t, fine 6t^5, anti peaks, d-neutral 0, Delta d by 2.2);
compensated blocks: t/mu + lambda K_d t; (4) violations (con) <= c/2, (room) <= c/gamma_T, (sgn) <= c Sum 1/(2 m_l),
(drop) as in (3), (box) none (|tau| <= 6 lambda/t <= b = 12 lambda/t); Hoffman constant independent of b, so the projected
tau' obeys the box rows, giving the COORDINATEWISE bound tau'_l/lambda_l <= 12/t needed by the one-sided expansion
(an alternative to Z4's active sets U(t): valid); (5) compensation keeps (con),(room),(sgn) by resonance of the
compensators; box rows may fail only at the two fixed compensators (fixed lambda), as Z6 says; uncompensated blocks keep
only q = 0 carriers, so the d-sums vanish; (6) dropped non-peaks get the clamp omega^c (Prop. windowcert claim gives
lambda varrho <= |tau_l| + lambda |Delta d| M + 2 t lambda), dropped peaks omega^+ = 0 with lambda varrho <= |tau| + lambda|Delta d|M
(no margin), kept q > 0 via the shift trick, kept q < 0 via gap >= gamma_B, q = 0 gap M; (7) window arithmetic.
Gaps: D1, D2 above, and
Gap U1 (formulation of (W_U); affects the maximal-contact claims).  (W_U) contains Lambda*_f(l) SQUARED.  At maximal contact
all carriers are bad, r*_l = 2||v_l 1_{S_l\F}||, so Lambda*_f(l) ≍ Lambda°(l) and (W_U) would require Lambda°(l) =
o(l 2^{l^3}) along a subsequence -- a condition on the S_l that Definition SLD / D'' does not impose.  So "maximal contact
is allowed" and "the candidate is recovered unless K_nn ..." do not follow from (W_U) as written.  FIX (proved in
Z6_ref_notes, Sec. 2): Theorem U uses only Lemma modswallow(a), whose unrolling involves only GOOD indices (x_l = 0 for
bad l), so Lambda*_f may be replaced by Lambda*_good(l) := prod_{good l'' <= l}(1 + 3/r*_{l''}) (= 1 at maximal contact);
and the bookkeeping is LINEAR in each rate: V(t) <= C_f (1 + Lambda*_good)(1 + K_P + K_nn + 1/gamma_T) (design)^2 t.
Hence the corrected growth condition
 (W_U')  liminf_l (1 + Lambda*_good(l)) (1 + K_P(l) + K_nn(l) + 1/gamma_T) / (l 2^{l^3} Lambda°(l)) = 0.
At maximal contact (W_U') reads liminf K_nn(l)/(l 2^{l^3} Lambda°(l)) = 0, which is exactly the threshold claimed in 6.3(ii)
(up to the factor l).

## Gaps as a rate. CORRECT (PROVED).
In Lemma onesidedtransfer every constraint on c_flat is an upper bound, gamma_B enters only through c_flat <= gamma_B/(2A_2),
A_2 = 10 + 1/lambda_C does not depend on gamma_B, and every constraint on t_1 is monotone in c_flat; so c_flat(j) =
min(c^0, gamma_B(l_j)/(2 A_2)) with t_1 fixed.  Theorem windowed / Lemma avgfunctionals use c_flat only through
n_j >= 24 rho^2 K_j/(c_flat (1 - rho^2)) and Q = 2 rho^2 K/(c_flat n): j-dependence allowed.  Agrees with Z4 Lemma 6.1 /
Step 7 (refereed).  Then 1/gamma_B(l) enters the growth condition linearly.

## 5.5 Sign-alternating signatures. CORRECT WITH A MISSTATEMENT.
Survival of Section 8: checked every use of h_l >= 0: (T-c) uses |h_l(s)| = 2^{-s}; Lemma pinning and (SR) use
||h_l 1_A||_1; Lemma signmixed / modswallow use phi_z(-c v) = |c||v|(1 + z sgn(c v)) (Lemma phicalc(d) with |v| and the
redefined swallowing z_s = eps_l sgn v_l(s)); rooms r_l = ||v_l 1_{S_l\F}||_1 - |<v_l 1_{S_l\F}, z>|. OK.
Estimate: with s_1 = s_0 + 1 and S_l ∩ F empty, |sum (-1)^i 2^{-s_i}| <= 2^{-s_0} - 2^{-s_1} + sum_{i>=2} 2^{-s_i}, so
mass - |alt sum| >= 2 * 2^{-s_1} = 2^{-s_0} >= mass/2. OK.
Misstatement: "every f with F finite and z constant on all but finitely many S_l is in R_0^pm" is false as stated: on the
finitely many exceptional S_l, z may equal eps_l sgn h^alt_l (alternating swallowing), so r_l = 0.  Correct statement: if z
is constant on S_l \ F for all but finitely many l, and r_l > 0 for the remaining l, then f is in R_0^pm ((W^pm) holds since
1 + 3/r_l <= 3(1 + 2/delta°_l) for the cofinitely many l with S_l ∩ F empty, and the other factors are finitely many
constants).  In particular every maximal-contact row (z ≡ eps off F) is in R_0^pm.  "Only relabels the hard set": agreed.

## Proposition P and monotonicity. CORRECT (PROVED).
Farkas for {G nu >= 0, E nu = 0}: -e_{l0} >= 0 on the cone iff -e_{l0} = G^T y + E^T y', y >= 0.  Evaluating at tau and
bounding -y_l tau_l <= y_l (tau_l)_- etc. gives the displayed inequality.  Numerically confirmed (part 3).
Monotonicity: extension by zero from B_*(l) to B_*(l+1) (or from an active set U to B_*): new rows at j in T_0(l+1) \ T_0(l)
see only signatures of old carriers, where z_j = eps_l, so the zero-cost rows stay satisfied; d-rows unchanged. OK:
rigid at a level => rigid at all lower levels and for every sub-carrier-set.
Bracket terms are O(t) at window scales: (tau)_- <= c/(2m_l) for EVERY bad carrier (peaks included), contacts/rooms from
c(tau), anti peaks from (peakshift), |Q_m(tau)| from (didentity) (Q_m sums over all coarse bad carriers of block m, matching
(didentity), which sums over all carriers). OK.

## Theorem V. (a) CORRECT; (b) CORRECT WITH A PRECISION.
(a) The only uses of margin/non-degeneracy of swallowing-type peaks in Theorem U are the drop bound and the window
certificate error at a dropped peak (lambda(|omega_+| + |omega_-|) <= |tau| + lambda|Delta d|M, margin-free).  Replacing
the drop bound by Prop. P is legitimate; K_A is an f-dependent rate (LP value).  (E5)/(H2') still needs one non-degenerate
swallowing-type peak or a good one per block (unchanged hypothesis).
(b) Z4 Theorem A uses (H3) only in Step 4 (|tau_l| <= lambda K_d t + t/mu_l, mu_l > 0 by (H3)) -- confirmed by inspection
of Z4 part 3.  Z4 works with active sets U(t) = {lambda_l >= t^2}; Prop. P must be applied either to the cones C_0^+(U)
(at most l*+1 distinct sets per window; rigidity transfers by monotonicity; K_A := max over them) or to B_* with the
inactive carriers' |tau_l| <= 6 lambda_l/t < 6t added to the bracket (total <= 6 l* t).  Either way (b) holds.  The
statement "D'' windows dominate SLD_G" needs fix D3.

## Corollary V.1. CORRECT (PROVED).
Anti-sign peaks are zero on C_0^+, swallowing-type peaks have q > 0, d-neutral q = 0, so Q_m(nu) = 0 with q_p nu_p > 0
forces some strict non-peak with q < 0 and nu > 0.
Referee extension (PROVED by the same proof, see notes Sec. 3): (E3) of Theorem U can be weakened to (E3'): every block is
compensated, or every bad carrier of the block with q != 0 is d-rigid ("rigid block"); uncompensated blocks are rigid
blocks with certificate norm <= (1 + max|q|)/min|q| (design scale x (1 + K_nn)).
