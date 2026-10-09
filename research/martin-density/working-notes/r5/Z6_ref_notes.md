# Z6 referee notes (Round 5): verification of Z6, proofs of all fixes and additions

Setting and notation: the note paper/martin_density_note.tex (Sections 1, 7, 8), its numbering; Z6 = r5/Z6_notes.md.
Signature-ladder operator T (Definition def:SLD) or its modifications, N >= 1, I = {1..N}, p = p_N, F = supp a finite.
For a bad carrier l = j(k,m): eps_l (swallowing sign), tau_l := -eps_l Delta theta_l, q_l := eps_l Phi_m(k) w_m(k)/(m C_m);
vs_k := sgn w_m(k).  Delta d_m := d_{+,m} - d_{-,m} for two-sided decompositions (Lemma suplevel); for two-piece data
(Definition twopiece) Delta d_m := d_m(omega^-) - d_m(omega^+).  Labels: PROVED / SKETCH / HEURISTIC / OPEN / FALSE.
Parts: Z6_ref_part0..5.md.  Scripts: Z6_ref_work/check_farkas_shift.py, rerun outputs rerun_R4_k01.txt, rerun_R4_k098.txt.

## 1. Re-derivations of Z6's structural facts (all PROVED, as claimed)
1.1 (Z6 2.1) For k in Q_m: w(k) = C zeta(k)/(Phi(k)^2 sigma) (Lemma threshold) and zeta(k) = m Phi(k) u_k(xi), so
 Phi w/(mC) = u_k(xi)/sigma, |q_l| = (M - gap) Phi/(mC).
1.2 (Z6 2.2) (peakshift) with Delta Theta_m(k) = -eps tau/lambda gives Delta d M = vs eps tau/lambda - Y_k, 0 <= Y_k, and
 Y_k <= t/(sigma|alpha(k)|) = t/(lambda_k mu_k) when alpha(k) != 0 (eq. margin).  Anti-sign k_1: Delta d M <= (tau_1)_-/lambda_1
 (no non-degeneracy needed); swallowing-type non-degenerate k_2: Delta d M >= -(tau_2)_-/lambda_2 - t/(lambda_2 mu_2).
1.3 (Z6 2.3) v = b^+ - b^- is z-signed on K; for s in S_l \ F outside the finite target supports of the carriers of
 omega^pm: v(s) = -Delta d_m lambda_l w_m(k) v_l(s) + rho(s), |rho(s)| <= (4/3) D sum_{l'' >= L(s)} lambda_l'' <= (2/9) D 2^{-2s}
 c_l delta_l (allowedness (b), lambda <= c/4, c_{l+1} <= c_l/4), while the main term is ~ 2^{-s}; so for Delta d_m != 0 the
 sign of v on far points of S_l is -sgn(Delta d_m) vs_k, and z-signedness forces eps_l = -sgn(Delta d_m) vs_k; two peaks with
 eps vs of opposite signs give a contradiction.  (Same content as Z4 Prop. 5.1 / Z4-referee finding 9; independent proof.)
1.4 (Z6 2.4) For l in Sigma, Phi w Delta theta_l/(mC) = -q_l tau_l; (didentity) gives sum_Sigma q tau = R with
 |R| <= A - sum_Sigma |q|(tau)_-; one sign gives sum_Sigma |q| (tau)_+ <= A.  Fine carriers: sum_{l > l*} Phi_l 6 lambda_l/t <=
 6 T_lo(l*)^6/t <= 6 t^5.
1.5 (Z6 Lemma F, 4.2) On A: B_pm(s) = g(s) - theta^pm_l v_l(s); phi_eps(x) = 2(eps x)_-, phi_{-eps}(x) = 2(eps x)_+; the one-sided
 budgets (Lemma switchbudget) give the two displayed inequalities and their difference.  4.2(a) uses the box bound, valid for
 t <= 1; 4.2(b) CORRECTION: g|_A = eps_l theta*_l v_l|_A; 4.2(c),(d) as stated.
1.6 (Z6 Prop. P) Farkas for the cone {G nu >= 0, E nu = 0}: -nu_{l0} >= 0 on it iff -e_{l0} = G^T y + E^T y', y >= 0;
 evaluate at tau, move y_{l0} tau_{l0} left, bound -y_l tau_l <= y_l (tau_l)_-.  Monotonicity: extension by zero from B_*(l)
 to B_*(l+1), or from an active set U to B_*, preserves all rows (new rows see only signatures of old carriers, z = eps there).
 Numerics: 1232 random rigid instances x 200 tau, max(lhs - rhs) = -3.7e-5 (check_farkas_shift.py).
1.7 (Z6 Cor. V.1) Anti-sign peaks vanish on C_0^+, swallowing-type peaks have q > 0, d-neutral q = 0, so Q_m(nu) = 0 with
 q_p nu_p > 0 needs a strict non-peak with q < 0 and nu > 0.

## 2. Theorem C (Z6 3): CORRECT; the one formal gap closed by Lemma 2.1
Lemma 2.1 (one-sided transfer expansion with inward-only coordinates). PROVED.  Lemma onesidedtransfer remains valid if a
coordinate k in supp omega_m may also be of the third kind: side +: vs_k omega(k) <= 1.5 gap(k)/t and vs_k omega(k) >= -A'/t;
side -: vs_k omega(k) >= -1.5 gap(k)/t and vs_k omega(k) <= A'/t; with c_flat <= min(1/3, 1/(4A')) and A_3 := 2 + A_2 + A'.
Proof.  The coordinate conditions enter only through Lemma block(c),(d): ||W||_inf = (1 - r d) M (attained at the peaks, where
omega = 0) and Y = C + d r M >= C/2.  Side +, 0 < r <= c_flat t, |r d| <= 1/2:
 vs W(k) = (1 - r d)(M - gap) + r vs omega(k) <= (1 - r d) M - gap (1 - |r d| - 1.5 c_flat) <= (1 - r d) M,
 vs W(k) >= (1 - r d)(M - gap) - c_flat A' >= -(1 - r d) M   ((1 - r d)(2M - gap) >= M/2 >= 1/4 >= c_flat A').
Side - is symmetric.  Lemma block(a),(b),(c) then give N(W) - 1 = sqrt(Y^2 + r^2 ||h_perp||^2) - Y <= (r^2/2) H(omega)
(1 + 2|d r| M/C).  The rebalancing step uses only ||W - w||_inf <= 2 A_3 c_flat.  QED  (Numerics: 2000 random blocks, gaps
1e-8..1e-1: max(||W||_inf - (1 - r d)M) = 0, max excess - bound = 2e-16.)
In Theorem C step 5: P := vs omega^+(k) <= 1.5 gap/t (suplevel(f)); Q := vs omega^-(k) >= -1.5 gap/t - e_k; Q - P = vs eps
tau'/lambda in [0, A_2/t]; the shift x with vs x = (-a - Q)_+ (a := 1.5 gap/t) gives P~ <= a (if x > 0 then P <= Q, so P~ <= -a),
Q~ >= -a, Q~ - P~ = Q - P; hence P~ >= -a - A_2/t and Q~ <= a + A_2/t, and since a <= 1.5/t the shifted data are
inward-only with A' := 2 + A_2; the d-coefficients and V' are unchanged, and the represented functional moves by x(lambda_k u_k - (Phi_k^2 w(k)/C) R*w) with
lambda_k |x| <= |tau_l - tau'_l| + lambda_k |Delta d| M, summable to O(K** t).  All other steps re-derived; Theorem C PROVED.

## 3. Design D''' (correction of Z6's D'') and Theorem U' (correction of Theorem U)
3.1 Lemma (N-free reciprocal d-weights). PROVED.  For SLD-type designs (Phi_l = 2^{-m-k} c_l), every peak and every strict
non-peak with gap <= M/2 has |q_l| >= Phi_l/2.  Proof: |w| >= M/2, M_m >= 1 - ||Phi_m||_1 >= 1/2 and C_m <= ||Phi_m||_1 <= 2^{-m}
(Lemma A(b)), so |q_l| >= Phi_l 2^m/(4m) >= Phi_l/2.  QED
3.2 Why D'' needs repair. (i) Xi(l) contains 8N 2^{m+k}/c_l: D'' depends on N, while Lemma martintail needs one operator for
infinitely many N.  (ii) Z6 bounds sum_{l<=l*} 1/m_l by C_f sum 1/m^des_l(l*), m_l = ||v_l 1_{S_l \ (F ∪ T_0)}||_1, m^des_l(l) =
||v_l 1_{S_l \ T(l)}||_1: FALSE in general for the finitely many l with S_l ∩ F nonempty (if F contains the first point of
S_l \ T(l*) and later bad targets cover ever more points of S_l -- allowed by allowedness (b) -- then m^des_l(l*) stays >= v_l(min)
while m_l(l*) -> 0).  (iii) "D'' windows dominate those of SLD_G" (Z6 8.2, 11) is FALSE in general: SLD_G has
n^w = (l 2^{l^3} Lambda° G*)^6, and when delta°_l is astronomically small Lambda°(l)^5 and G*(l)^2 exceed every factor of Xi(l).
3.3 Definition (D'''). In (D1), after y_{l''}, u_{l''}, c_{l''} (l'' <= l) are fixed: T(l) := union_{l''<=l} supp y_{l''},
 m^nat_{l''}(l) := ||v_{l''} 1_{S_{l''} \ ([1,l] ∪ T(l))}||_1 > 0,  D(l) := 1 + sum_{l''<=l} (1/m^nat_{l''}(l) + 1/Phi_{l''}),
 Xi'(l) := [l H_comb(l) G*(l) D(l)]^4 (l 2^{l^3} Lambda°(l) G*(l))^5,
 n^w_l := ceil(l 2^{l^3} Lambda°(l) Xi'(l)), T_hi(l) := min{T_lo(l-1), 2^{-l^3}/(l Lambda°(l) Xi'(l))}, T_lo(l) := 2^{-n^w_l} T_hi(l),
 c_{l+1} := min{c_l/4, T_lo(l)^3};
H_comb (Z6 5.2) and G* (Z4 2.2) maximized over ALL subsets of [1,l] (N-free).  Proposition: D''' is admissible, N-free, and
all of Section 8, Theorem C, Theorem U' (3.4), Theorem V (Z6 5.6, with 3.5 below) and Z4 Theorem A hold for it.  Proof:
recursion well defined (all ingredients have index <= l); Xi' >= 1 gives (P1), (P2), old (P3); Theorem SLD's proof uses only
allowedness and c_{l+1} <= c_l/4; Section 8 uses only (T-a)-(T-d), (P1)-(P3); Xi' >= (l 2^{l^3} Lambda° G*)^5 G*^4 gives
n^w >= (l 2^{l^3} Lambda° G*)^6 and T_hi <= its inverse (Z4's requirement).  For l* >= max F, S_l \ (F ∪ T_0) ⊇ S_l \ ([1,l*] ∪
T(l*)), so m_l(l*) >= m^nat_l(l*) for all l <= l*.  QED
3.4 Theorem U' (Theorem U corrected and extended). PROVED (modification of Z6's proof, which was re-derived step by step).
Design D''', f with F finite.  A block is COMPENSATED (Z6) or RIGID: every bad carrier of the block with q != 0 (strict
non-peaks, and swallowing-type peaks, q = Phi M/(mC)) is d-rigid at every level.  One-signed (Z6 "uncompensated") blocks
are rigid (certificate -(1/q_p) Q_m + sum_{l in Sigma, l != p} (q_l/q_p) e_l + sum_anti (q_l/q_p) e_l = -e_p).
Rates at level l (maxima over l' <= l): Lambda_g(l) := prod_{good l'' <= l} (1 + 3/r*_{l''}) (= 1 if no good carrier);
K_P(l) := max Phi_{l'}/mu_{l'} over non-rigid swallowing-type bad peaks of compensated blocks; K_R(l) := max Phi_{l'} kappa*_{l'}(l)
over the q != 0 bad carriers of rigid blocks, kappa* = least sup-norm of a Farkas certificate in C_0^+(l) (in one-signed blocks
K_R <= C_f (1 + K_nn) by 3.1).
Hypotheses: (E1) r*_l > 0 for good l; (E2) gamma_T > 0; (E3') every block compensated or rigid; (E4') compensated blocks: kept
q < 0 non-peaks have gap >= gamma_B (or gamma_B(l) as a rate, 3.6), degenerate swallowing-type bad peaks are d-rigid;
(E5) (H2'); (W_U') liminf_l Lambda_g(l) (1 + K_P(l) + K_R(l))/(l 2^{l^3} Lambda°(l)) = 0.   Conclusion: f in Rec.
Proof (departures from Z6).  l* >= max(max F, fixed carriers), t in W(l*), K_g := (1/q0 + 22) Lambda_g(l*), D := D(l*).
(1) Lemma modswallow(a): the unrolling puts x_l = 0 at bad l and has only good indices on the right, so the product is over
 good l: sum_good |Delta theta| <= K_g t; ||e_0|| <= K_g t + 6 t^2; c := c(tau) <= 3 K_g t.
(2) (tau_l)_- <= c/(2 m^nat_l) for all coarse bad l; by 1.2 or Lemma badpeaks(a), |Delta d_m| M_m <= C_1(c D + t + K_g t) <= K_d t,
 K_d := 5 C_1 K_g D.
(3) Drops: anti-sign peaks |tau| <= lambda K_d t + c/(2m); rigid blocks: Prop. P with bracket beta <= c D + c/2 + c/gamma_T +
 (K_d t + c D) + N(K_d t + 2t/sigma + (K_g t + 6t^5)/(mC)) <= C_2 K_g D t, so |tau_{l0}| <= (K_R/Phi_{l0}) beta + c/(2m) and the sum
 over rigid-block carriers is <= K_R D beta + c D; compensated blocks: non-rigid swallowing-type peaks t K_P/Phi + lambda K_d t,
 rigid ones by Prop. P.
(4) V(t) <= C_3 K_g (1 + K_P + K_R) D^2 t (each rate linearly; gamma_T in C_3); ||tau - tau'||_1 <= H_comb V (Z6 5.2; box rows give
 tau'_l <= 12 lambda_l/t).
(5) Compensation as in Z6 (|e_m| <= C_4 (1 + H_comb) V); rigid blocks keep only q = 0 carriers; ||Delta B 1_{F^c} - V''||_1 <= K_U t,
 K_U := C_5 Lambda_g (1 + K_P + K_R) H_comb D^2.
(6),(7) Window two-piece data (Lemma windowtwopiece; dropped non-peaks clamped, dropped peaks omega^+ = 0 with error <= |tau| +
 lambda|Delta d|M, kept q > 0 by Lemma 2.1, kept q < 0 by gap, q = 0 gap M), windowed averaging, Corollary D1.  Since
 Xi'(l*) >= l* H_comb D^2: K_U T_hi(l*) <= C_5 Lambda_g(1 + K_P + K_R)/(l* 2^{l*^3} Lambda°) and n^w/K_U >= its inverse; (W_U')
 gives the window hypotheses along a subsequence.  QED
Corollary 3.4' (maximal contact). F finite, z ≡ eps off F: (E1),(E2) vacuous, (E5) automatic (1.2), Lambda_g ≡ 1; f in Rec if
every block is compensated or rigid, (E4') holds and liminf (K_P + K_R)(l)/(l 2^{l^3} Lambda°(l)) = 0.  With Z6's (W_U) (bracket
squared, Lambda*_f instead of Lambda_g) this does NOT follow: Lambda*_f ≍ Lambda° at maximal contact.
3.5 Theorem V (Z6 5.6): (a) correct; (b) correct once K_A is taken as the maximum over the cones C_0^+(U) of the active sets
U(t) of Z4 (at most l*+1 per window; rigidity passes to subsets by 1.6), or Prop. P is applied on B_* with the inactive carriers
(|tau| <= 6 lambda/t < 6t) added to the bracket.
3.6 Gaps as a rate (Z6 5.4(c)): correct -- every constraint on c_flat in Lemma onesidedtransfer is an upper bound, gamma_B enters
only through c_flat <= gamma_B/(2A_2), constraints on t_1 are monotone in c_flat; Theorem windowed / Lemma avgfunctionals use
c_flat only through n_j >= 24 rho^2 K_j/(c_flat(1 - rho^2)) and Q = 2 rho^2 K/(c_flat n).  Agrees with Z4 Lemma 6.1.

## 4. Sign-alternating signatures (Z6 5.5): survival correct, statement corrected. PROVED.
Uses of h_l >= 0 in Section 8: (T-c) (needs only |h_l(s)| = 2^{-s}), Lemma pinning / (SR) (l_1-masses), Lemmas signmixed and
modswallow (phi_z(-c v) = |c||v|(1 + z sgn(c v)), swallowing redefined as z_s = eps_l sgn v_l(s)); nothing else.  With
s_1 = s_0 + 1 and S_l ∩ F empty: |sum (-1)^i 2^{-s_i}| <= 2^{-s_0} - 2^{-s_1} + sum_{i>=2} 2^{-s_i}, so r_l >= 2^{1-s_1} = 2^{-s_0}
>= ||v_l||_1/2 (in units delta_l/n_l).  Corrected statement: if z is constant on S_l \ F for all but finitely many l and r_l > 0
for the others, then f is in R_0^pm (Lambda^pm_f(l) <= C 3^l Lambda°(l)).  Z6's version ("z constant on all but finitely many
S_l") omits r_l > 0 on the exceptional sets and is false as stated.  Remark rem:nodesign: only a relabelling (agreed).

## 5. Proposition R1 (new; PROVED under the design choice (Y+))
(Y+): the target sequence contains a countable set of nonnegative vectors dense in the nonnegative part of c_00 ∩ S_{q*}.
Claim: at maximal contact (z ≡ 1 off F), if block m has a resonant bad strict non-peak l^- with q < 0, then every
swallowing-type peak of block m is non-rigid at all large levels.  Proof in Z6_ref_part5.md (repair the finitely many negative
entries of u_p off F by carriers with nonnegative targets, which are positive peaks of the same block, and balance the d-row of
block m with kappa e_{l^-}).  Consequences: at maximal contact Theorem V(a) never applies in compensated blocks (their
compensator l^- is resonant), so all relative margins of positive peaks of such blocks enter K_P and a degenerate positive
peak there is in the open class (d); blocks without non-rigid q < 0 swallowed non-peaks are rigid and need only K_R.

## 6. Candidate and modules (Z6 6): SKETCH-level remarks
6.1: with F = {j0} and z ≡ 1 off F the row is a single point (no parameter); the nested construction needs |F| >= 2 (Z6 hints at
this).  (C2) does not violate (W_U) (K_P counts compensated blocks only).  6.2: + side correct; - side beyond the radius needs
a base/block rebalancing (levels 1 - |r|cq sigma/q0 + 2|r|c m_u and 1 + |r|cq are unequal), routine.  Heuristic (referee): for
a nearly neutral module the band [M lambda/c, c m_u] is EMPTY under the validity bound c^2 <= (M + |w|) lambda/(16 m_u), which
explains R4 (kappa = 0.1: no forced switching) and is the single-module case of Conjecture G.  6.3(iii): covers only modules far
below validity (non-switching).  6.3(ii): correct after 3.4 (Corollary 3.4').  Numerics R4 reproduced exactly; at kappa = 0.98
the forced switching is ~ 0.8 t/q on [3e-3, 1e-2]: the 1/q constant of 1.4 is essentially attained (supports sharpness).

## 7. What remains open (F finite unless stated)
SLD: Lemma Z open; new proved class R_C (Theorem C).  D''' (admissible, N-free): Lemma Z open; proved: R_0^pm, R_S, R_BT, R_C,
R_U' (3.4, incl. Theorem V), R_SBinf (Z4).  Open configurations: (r) rates beyond the ladder: Lambda_g (rooms of good signature
sets, incl. approximate swallowing (O1)(i)), K_P (relative margins of non-rigid positive peaks in compensated blocks -- at
maximal contact ALL positive peaks of such blocks, by 5), K_R (relative Farkas constants; for one-signed blocks the relative
d-coefficients K_nn of nearly neutral non-peaks), gamma_B(l) (gaps of kept q < 0 carriers), gamma_T; (d) degenerate non-rigid
positive (swallowing-type) peaks -- exactly the blocks with a non-rigid q < 0 swallowed strict non-peak (Cor. V.1 and 5); (m) mixed
blocks that are neither compensated nor rigid (f-dependent d-row Hoffman constants, Z4 Cor. 4.1 as a rate); (h) failure of (H2')
((H2'') of the Z4 referee is weaker); (e) failure of (E1) (good signature sets covered by bad targets) or of (E2) uniformly;
(O4) F infinite.  For every admissible T (Martin's family): open.  No counterexample is indicated by anything checked.
