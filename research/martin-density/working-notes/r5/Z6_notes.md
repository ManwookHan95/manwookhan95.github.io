# Z6 notes (Round 5): stress test of Lemma Z for the signature-ladder design, and a design route

Setting and notation: those of the note paper/martin_density_note.tex, Section 8 (SLD operator T, N >= 1, I = {1..N},
p = p_N; forced data (xi, q_0, a, w, F, z, zhat, e, nu); blocks zeta_m, sigma_m, M_m, C_m, P_m, Q_m, alpha_m, gap_m, mu_{k,m};
two-sided decompositions (B_pm, Theta_pm) of g in C(f) at scale t (Lemma twosided); Delta theta_l, Delta B = -sum
Delta theta_l u_l; d_{pm,m}, omega_{pm,m} (Lemma suplevel); windows W(l) = [T_lo(l), T_hi(l)], n^w_l; good/bad carriers,
eps_l, r_l, r*_l, S*_l, Lambda*_f, tau_l := -eps_l Delta theta_l for bad l (Definition swallowed)).  q_l := eps_l
Phi_{m}(k) w_m(k)/(m C_m) for every carrier l = j(k,m) (for bad strict non-peaks this is the weight q_l of the note).
Throughout F is finite unless said otherwise.  Labels: PROVED / SKETCH / HEURISTIC / OPEN / FALSE.

## 0. Summary
Task (a).  The most dangerous candidate is at MAXIMAL CONTACT (z = 1 off F, every signature exactly swallowed, every
carrier bad, slaving through later targets on earlier signature sets), with peaks of both signs (forced by density),
infinitely many weak swallowed peaks with super-fast decaying relative margins, and infinitely many uncompensated
(same-sign q) swallowed strict non-peaks, some near-threshold, some nearly d-neutral (Section 6).  It lies outside
R_0^pm, R_S, (BT) and outside every class of the note; no window of the SLD design pins its mates.  Recovery attempts:
(i) every single switching "module" is a finite certificate and is recovered; (ii) module sums with gaps bounded below
are recovered by windowed averaging of certificates (SKETCH); (iii) the exact failing property is a uniform
exact-resonance projection (UERP, 6.4), which for the designs of Section 5 can fail only through f-dependent RATES.
No non-recovery is claimed or indicated; finite models (Section 7) show a transient switching band with forced switching
<= C t / min(gap m_u, |q|).
PROVED tools (any F finite, SLD): d-coefficient formula (2.1); shift pinning by a pair of swallowed peaks (2.2); exact
two-piece data are d-neutral on doubly swallowed blocks (2.3); same-sign d-coupled switching is transient, |tau_l| <=
O(t)/|q_l| (2.4, the matching upper bound to the Z4 referee's lower bound Lemma R); forced switching = oscillation
(Lemma F) and rigidity of mates on swallowed sets (4.2); Farkas pinning of d-rigid carriers (Proposition P, 5.6).
Recovery theorems: THEOREM C (SLD; compensated resonant swallowing under (H1), near-threshold q >= 0 carriers allowed via a
shift trick) — PROVED.  Task (b): design D'' (5.1: lengthened windows absorbing 1/c_l, signature masses and COMBINATORIAL
Hoffman constants, which are design quantities, 5.2; admissible, all of Section 8 survives) and THEOREM U (5.3): swallowing
with arbitrary combinatorics (no (H1), maximal contact allowed, any number of bad carriers) is recovered when every block is
compensated or uncompensated and the rates are not super-fast.  In UNCOMPENSATED blocks weak and DEGENERATE swallowing-type
peaks and near-threshold d-coupled non-peaks cost only design constants (only nearly d-neutral non-peaks carry a rate,
K_nn).  THEOREM V (5.6): a swallowing-type peak that is d-RIGID (no zero-cost exactly d-neutral direction switches through it)
needs no margin and may be degenerate; this weakens (H3) of Z4 Theorem A / Corollary 4.1 to (H3_rig).  Both PROVED by
modification of Theorem S (referee check recommended).  The compensated part of Theorem U was found independently of, and
is contained in, Z4 Theorem A ((DR) generalizes the compensator pair; Z4 Step 7 makes gaps a rate): see Section 11 for the
precise overlap.  Sign-alternating signatures (5.5) remove the literal case (O3) "z = eps off F" (PROVED), but by Remark
rem:nodesign only relabel the hard set.
Status: Lemma Z remains OPEN for the SLD and for D''.  For D'' with F finite the open core is: (i) super-fast RATES (rooms,
margins of non-rigid swallowing-type peaks, relative d-coefficients of nearly neutral non-peaks in same-sign blocks, gaps,
f-dependent cone/Farkas constants in blocks that are neither compensated nor uncompensated); (ii) NON-rigid degenerate
swallowing-type peaks (exact resources that window data cannot carry); (iii) failure of (H2'); (iv) infinite F (Z5).
For the candidate of task (a): recovered for D'' unless its nearly neutral non-peaks have super-fast relative d-coefficients.

## 1. Two facts used throughout (from the note)
(peakshift) For a peak k of block m (varsigma_k = sgn w_m(k)): |omega_{+,m}(k)| + |omega_{-,m}(k)| = -varsigma_k Delta Theta_m(k)
 - Delta d_m M_m >= 0, and sigma_m |alpha_m(k)| (|omega_+(k)| + |omega_-(k)|) <= t (Lemma peakshift, Lemma suplevel(c)); by
 eq. (margin), sigma_m|alpha_m(k)| = lambda_{k,m} mu_{k,m}.
(didentity) Delta d_m M_m = (1/(m C_m)) sum_k Phi_m(k) w_m(k) Delta theta_{k,m} + r_m, |r_m| <= 2t/sigma_m.

## 2. Structural facts   [all PROVED]
2.1 (d-coefficient of a strict non-peak) For k in Q_m, Phi_m(k) w_m(k)/(m C_m) = u_{k,m}(xi)/sigma_m; hence for a bad strict
non-peak q_l = eps_l u_l(xi)/sigma_m and |q_l| = (M_m - gap_m(k)) Phi_m(k)/(m C_m) <= M_m Phi_m(k)/(m C_m).
Proof. Off P_m, w(k) = C zeta(k)/(Phi(k)^2 sigma) (Lemma threshold) and zeta(k) = lambda_k u_k(xi) = m Phi(k) u_k(xi); and
|w(k)| = M - gap.  QED
Reading: weak d-coupling <=> gap near M_m; d-neutral <=> w(k) = 0.

2.2 (shift pinning by a pair of swallowed peaks) Let k_1, k_2 be non-degenerate peaks of block m whose carriers l_1, l_2 are
swallowed with varsigma_{k_1} eps_{l_1} = -1, varsigma_{k_2} eps_{l_2} = +1.  If (tau_{l_i})_- <= X, then
 -X/lambda_{l_2} - t/(sigma_m|alpha_m(k_2)|) <= Delta d_m M_m <= X/lambda_{l_1}.
Proof. Delta Theta_m(k) = Delta theta_l/lambda_l = -eps_l tau_l/lambda_l, so (peakshift) reads Delta d_m M_m = varsigma eps
tau_l/lambda_l - Y_k with 0 <= Y_k <= t/(sigma|alpha(k)|).  For k_1: Delta d M = -tau/lambda - Y <= (tau)_-/lambda.  For k_2:
Delta d M = tau/lambda - Y >= -(tau)_-/lambda - t/(sigma|alpha|).  QED
(H2') := every block has a non-degenerate peak with a good carrier, or a pair as in 2.2.  It replaces (H2) wherever
(tau)_- of the two carriers is O(K t) (Lemma modswallow(b) under (H1), or 5.3 step (1)).  Under (B_fin) or (B_res), (H2)
is automatic (every block has infinitely many non-degenerate peaks, the u_{k,m} being dense and Phi_m(k) -> 0), so (H2)
can only fail when infinitely many peaks are swallowed; at maximal contact peaks of both signs exist in every block
(density), so the pair of 2.2 exists.

2.3 (exact two-piece data are d-neutral on doubly swallowed blocks) Let block m contain peaks k, k' whose carriers l, l'
are swallowed (S\F contained in K, z = eps there) with eps_l varsigma_k = -eps_{l'} varsigma_{k'}.  Then every pair of
two-piece data (Definition twopiece) for any functional has Delta d_m = 0.  In particular at maximal contact every exact
two-piece datum is d-neutral, and the allowance Delta d_m >= 0 of Corollary D1 is void there.
Proof. v := b^+ - b^- is z-signed on K and v = sum_{m'} R_{m'}^*((omega^-_{m'} - omega^+_{m'}) - Delta d_{m'} w_{m'}).
For s in S_l \ F the only vectors nonzero at s are u_l (value v_l(s) = delta_l 2^{-s}/n_l) and targets y_{l''}/n_{l''} of
later carriers allowed at s, i.e. with 2c_{l''} <= 2^{-2s} c_l delta_l (allowedness (b)).  The omega^pm are finitely
supported, so for s large none of their carriers' finite target supports contains s.  Hence
v(s) = -Delta d_m lambda_l w_m(k) v_l(s) + rho(s), |rho(s)| <= (4/3) D sum_{l'': 2c_{l''} <= 2^{-2s}c_l delta_l} lambda_{l''}
<= (2/9) D 2^{-2s} c_l delta_l, D := max_{m'}|Delta d_{m'}| M_{m'} (lambda <= c/4, c_{l+1} <= c_l/4, ||y||_1/n <= 4/3).  As
lambda_l = m 2^{-m-k} c_l and |w_m(k)| = M_m, the ratio |rho(s)|/|Delta d_m lambda_l w_m(k) v_l(s)| tends to 0 as
s -> infinity if Delta d_m != 0.  So sgn v(s) = -sgn(Delta d_m) varsigma_k for large s in S_l, and z-signedness forces
-sgn(Delta d_m) varsigma_k = eps_l; likewise at l'.  Multiplying, eps_l varsigma_k = eps_{l'} varsigma_{k'}: contradiction.  QED

2.4 (uncompensated d-coupled switching is transient) Let Sigma be a set of bad strict non-peaks (and/or bad degenerate
peaks) of block m whose q_l all have the same sign.  With
 A := |Delta d_m| M_m + 2t/sigma_m + (1/(mC_m)) sum_{l notin Sigma, m(l)=m} Phi_m(k_l)|w_m(k_l)||Delta theta_l| + sum_{Sigma}|q_l|(tau_l)_- ,
one has sum_{Sigma} |q_l| (tau_l)_+ <= A.  (For a bad degenerate peak with varsigma eps = +1, q_l = Phi M/(mC) > 0.)
Proof. In (didentity) the term of l in Sigma is Phi w Delta theta_l/(mC) = -q_l tau_l (for a degenerate peak w = varsigma M).
So sum_Sigma q_l tau_l = R with |R| <= A - sum|q|(tau)_-; as all q_l have one sign, sum |q_l| tau_l = +-R, and
sum |q|(tau)_+ = +-R + sum |q|(tau)_- <= A.  QED
Reading: if Delta d = O(t), the other carriers are O(t)-pinned in the Phi|w|-weighted sense (fine carriers l > l_*
contribute <= (6/(mC)) T_lo(l_*)^6/t <= (6/(mC)) t^5 by the box bound) and the wrong-direction parts are O(t) (budget), then
each l in Sigma switches by O(t)/|q_l| ((tau_l)_- is controlled by the budget on its swallowed signature set): persistent switching through d-coupled carriers needs compensation (q of both
signs) or exact d-neutrality.  The constant 1/|q_l| ~ 1/Phi_l is not beaten by the SLD windows (n^w_{l_*} << 1/c_{l_*-1}).

## 3. Theorem C: compensated resonant swallowing (SLD operator as in the note)   [PROVED]
Definition (class R_C).  f with F finite such that, with B the set of bad carriers and, for bad non-degenerate peaks,
K_P(l) := sum_{l' <= l, l' in B, k(l') in P} 1/mu_{l'}:
 (H1)  supp y_{l'} cap S_l = empty whenever l < l' are both bad;
 (R')  every bad carrier is (np+) a resonant strict non-peak with q_l >= 0 (any gap), or (np-) a resonant strict non-peak
       with q_l < 0 and gap >= gamma_B > 0, or (pk) a non-degenerate peak, or (dg-) a degenerate peak with varsigma eps = -1;
       resonant means u~_l = eps_l u_l 1_{F^c} is z-signed and supported in K;
 (Cmp) every block containing a bad strict non-peak with q_l != 0 contains bad (np+)/(np-) carriers l^+_m, l^-_m with
       q_{l^+_m} > 0 > q_{l^-_m};
 (H2') as in 2.2;
 (W*_P) r*_l > 0 for good l and liminf_l (Lambda*_f(l) + K_P(l))/(l 2^{l^3} Lambda°(l)) = 0.
R_C contains the resonant case (B_res) of R_S (all bad carriers d-neutral non-peaks: q = 0, gap = M, (Cmp) void, K_P = 0).

THEOREM C.  For the SLD operator and every N, R_C is contained in Rec.
Proof.  We run the proof of Theorem S with K_* replaced by K_** := (1/q_0 + 22) Lambda*_f(l_*) + K_P(l_*) and only Lemmas
badpeaks and exactswitch modified.  Fix l_* (larger than all compensator indices), t in W(l_*), t <= min(t_eta, 1), a
two-sided decomposition.  Lemma modswallow (needs only (H1) and r*_l > 0 for good l) gives sum_good|Delta theta| <= K_* t
(+6t^2 fine) and sum_{l in B, l <= l_*} (tau_l)_- <= K_* t.
Step 1. By (H2') and 2.2 (or Lemma badpeaks(a)), |Delta d_m| M_m <= K_d t, K_d <= C_f K_* (C_f depends only on f).
Step 2. For a bad non-degenerate peak, (peakshift) gives varsigma eps tau_l/lambda_l in [Delta d M, Delta d M +
t/(sigma|alpha|)], so |tau_l| <= t/mu_l + lambda_l K_d t; summing over coarse bad peaks, <= (K_P(l_*) + K_d) t.  For (dg-),
(peakshift) gives -tau_l/lambda_l >= Delta d M, i.e. tau_l <= lambda_l K_d t, and (tau_l)_- <= K_* t.
Step 3. In (didentity) for block m: good carriers contribute <= K_* t/(mC_m) (Phi|w| <= 1), fine carriers <= (6/(mC_m)) t^5,
coarse bad carriers -sum q_l tau_l; so |sum_{l in B, l <= l_*, m(l)=m} q_l tau_l| <= C'_f K_** t.
Step 4 (replaces Lemma exactswitch).  tau^1_l := (tau_l)_+ for bad strict non-peaks, := 0 for bad peaks; e_m :=
sum_{m(l)=m} q_l tau^1_l; tau'_l := tau^1_l + (e_m)_-/q_{l^+_m} [l = l^+_m] + (e_m)_+/|q_{l^-_m}| [l = l^-_m].  Then tau' >= 0,
tau' = 0 at bad peaks, sum_{m(l)=m} q_l tau'_l = 0 for all m, V' := sum_{l <= l_*} eps_l tau'_l u_l 1_{F^c} is z-signed and
supported in K (each term is, by resonance), |e_m| <= C''_f K_** t (|q_l| <= M/(mC) for all l), and
sum_{l in B, l <= l_*} |tau_l - tau'_l| <= C_f K_** t,  ||Delta B 1_{F^c} - V'||_1 <= C_f K_** t.
Step 5 (window two-piece data, Lemma windowtwopiece with K_**).  (a) Representation and Delta d_m = sum q_l tau'_l = 0
(computation in its proof: (eps tau'/lambda) Phi^2 w/C = q tau').  (b) At bad coarse peaks omega^+ = 0 and lambda_k rho_k <=
|tau_l| + lambda_k|Delta d|M (summed by Step 2); at bad non-peaks rho_k = 0; good coordinates as before; base error by the
split lemma with e := Delta B 1_{F^c} - V'.  (c) unchanged.  (d) Size: tau'_l/lambda_l <= 6/t for non-compensators (box),
<= (6 + 1/lambda_C)/t for the compensators (C_f K_** t^2 <= 1), so A_2 := 10 + 1/lambda_C.
Gap conditions for the one-sided transfer expansion (Lemma onesidedtransfer) at a kept coordinate k = k(l):
 - (np-), compensators, d-neutral carriers: gap >= gamma_B (resp. M), the expansion of the note applies;
 - (np+) with any gap > 0: put a := 1.5 gap(k)/t, P := varsigma omega^+(k), Q := varsigma omega^-(k).  By Lemma
   suplevel(f) and |d_pm t| <= 1/2, P <= a; since omega^- = omega_- + eps(tau'_l - tau_l)/lambda_l + Delta d w(k) (from
   omega_- - omega_+ = eps tau_l/lambda_l - Delta d w at k), Q >= -a - e_k with e_k := |tau_l - tau'_l|/lambda_l + |Delta d|M;
   and Q - P = varsigma eps tau'_l/lambda_l >= 0 (q_l > 0 means varsigma eps = +1; if w(k) = 0 the gap is M).  Shift both
   omega^pm(k) by x with varsigma x := (-a - Q)_+ <= e_k: then P + varsigma x <= a, Q + varsigma x >= -a, omega^- - omega^+ is
   unchanged (so Delta d and V' are unchanged), and the represented functional changes by -x(lambda_k u_k - (Phi_k^2 w(k)/C)
   R^* w), of l_1-norm <= C lambda_k|x| <= C(|tau_l - tau'_l| + lambda_k|Delta d|M), summable to O(K_** t).  After the shift,
   for 0 < r <= c_flat t (resp. -c_flat t <= r < 0) the coordinate k moves outward by at most |r| a <= gap/2 (c_flat <= 1/3)
   and inward by at most c_flat A_2 <= M/2, so |(1 - d r) w(k) + r omega(k)| <= (1 - d r) M and ||W||_inf = (1 - d r) M; the
   Hilbert part is as in Lemma block.  No lower bound on the gap is needed.
 At the engineering step (Corollary D1 for the averaged data) the data are fixed, finitely supported on strict non-peaks of
 f with positive gaps: the coordinatewise radius is positive and Theorem engineered applies verbatim.
Step 6. Windowed averaging over W(l_j) chosen by (W*_P), Lemma avgfunctionals, d-neutral averaged data, Corollary D1:
verbatim from Theorem S.  QED
Remarks. (1) Exact d-neutrality is obtained by moving the defect onto two fixed carriers; the cone {tau >= 0, sum q tau = 0}
is upward closed in resonant directions, so no Hoffman constant of an infinite system is needed.  (2) Near-threshold
swallowed carriers are harmless when q_l >= 0 (both sides move inward); a gap is needed only for q_l < 0.  (3) (H1) is
essential for this proof (Lemma modswallow(b)); it fails at maximal contact (Section 5 removes it by design).

## 4. Forced switching and rigidity of mates on swallowed signature sets   [PROVED]
4.1 Lemma F.  Let l be swallowed (z = eps_l on S_l \ F) and A subset S_l \ F a set on which no carrier vector other than u_l
is nonzero.  Put rho(s) := eps_l g(s)/v_l(s) on A and theta_{pm,l} := lambda_l Theta_{pm,m(l)}(k(l)).  For every two-sided
decomposition at scale t and s, s' in A:
 eps_l theta_{-,l} >= rho(s) - t/(4 q_0 v_l(s)),  eps_l theta_{+,l} <= rho(s') + t/(4 q_0 v_l(s')),
 tau_l = eps_l(theta_{-,l} - theta_{+,l}) >= rho(s) - rho(s') - (t/(4q_0)) (1/v_l(s) + 1/v_l(s')).
Proof. On A, B_pm(s) = g(s) - theta_{pm,l} v_l(s).  With z = eps on A, phi_z(x) = 2(eps x)_-, phi_{-z}(x) = 2(eps x)_+
(Lemma phicalc(a)), and the one-sided budgets of Lemma switchbudget give sum_A v_l(s)(eps theta_+ - rho(s))_+ <= t/(4q_0),
sum_A v_l(s)(rho(s) - eps theta_-)_+ <= t/(4q_0).  Evaluate at single coordinates and subtract.  QED
4.2 Corollaries.  (a) (size) Since |theta_{pm,l}| <= 3 lambda_l/t (Lemma box), |rho(s)| <= 3 lambda_l/t + t/(4 q_0 v_l(s)) for all
t, hence (t = (12 q_0 lambda_l v_l(s))^{1/2}) |g(s)| <= (3 lambda_l v_l(s)/q_0)^{1/2} on A: mates are tiny on private parts.
(b) (proportionality under transience) If tau_l(t_n) -> 0 along t_n -> 0 for some choice of decompositions (e.g. l in an
uncompensated d-coupled set, 2.4, or a non-degenerate peak, Step 2 of Theorem C), then rho is constant on A, g|_A =
theta*_l v_l|_A, and eps theta_{pm,l}(t_n) -> theta*_l: persistent switching through l is forced exactly by the
non-proportionality of g to the signature on A.
(c) (peaks) If k(l) is a non-degenerate peak, lambda_l|omega_pm(k)| <= t/(2 mu_l), so theta_{pm,l} = -lambda_l varsigma_k M d_pm(t)
+ O(t/mu_l); under (b), d_pm(t_n) converges and g|_A is the trace of the uniform shift -d* R^*_m w_m (zero iff d* = 0).
(d) Under (b), |theta*_l| <= (3 lambda_l/(q_0 max_A v_l))^{1/2}.

## 5. Task (b): the design D'' and Theorem U
5.1 Design D''.  [PROVED: admissible; Section 8 survives]  In Definition SLD (D1), after y_{l''}, u_{l''}, c_{l''} (l'' <= l) are
fixed, define T(l) := union_{l' <= l} supp y_{l'} (finite), the design masses m^des_{l''}(l) := ||v_{l''} 1_{S_{l''} \ T(l)}||_1 > 0,
the combinatorial Hoffman constant H_comb(l) of 5.2, and
  Xi(l) := [ l * H_comb(l) * (1 + sum_{l'' <= l} (1/m^des_{l''}(l) + 8 N 2^{m(l'')+k(l'')}/c_{l''})) ]^4 >= 1,
  n^w_l := ceil(l 2^{l^3} Lambda°(l) Xi(l)),  T_hi(l) := min{T_lo(l-1), 2^{-l^3}/(l Lambda°(l) Xi(l))},
  T_lo(l) := 2^{-n^w_l} T_hi(l),  c_{l+1} := min{c_l/4, T_lo(l)^3}.
(P1),(P2) are unchanged; (P3) holds with Xi inserted, which implies the old (P3).  The admissibility proof of Theorem SLD
uses only allowedness and c_{l+1} <= c_l/4; all proofs of Section 8 use only (T-a)-(T-d), (P1), (P2) and the old (P3) (the
note says so after Theorem SLD).  Hence Theorems SLD, R0, reductionZ, Bstar, Bpm, S and Theorem C hold for D''.

5.2 Combinatorial Hoffman constants.  [PROVED]  Fix l_*.  A pattern P is: a set B_* subset {1..l_*} with signs eps_l, a
partition of B_* into kept and dropped carriers, and for each j in T_0 := union_{l in B_*} supp y_l a label in
{F, +contact, -contact, room}.  For tau in R^{B_*} put L_j(tau) := sum_{l in B_*} eps_l tau_l u_l(j) (design values) and let
A_P be the matrix of the system
 (con) z_j L_j(tau) >= 0 (j a +-contact),  (room) L_j(tau) = 0 (j room),  (sgn) tau_l >= 0 (kept),  (drop) tau_l = 0
 (dropped),  (box) -b_l <= tau_l <= b_l.
Z_P(b) := {solutions} contains 0.  By Hoffman's theorem there is H(A_P) < infinity with dist_1(tau, Z_P(b)) <= H(A_P) *
(l_1-norm of the violations) for all tau and all b >= 0 (the constant depends on the matrix only).  Since T_0 subset T(l_*)
and there are finitely many patterns, H_comb(l_*) := max_P H(A_P) is a function of the design data with index <= l_* only.

5.3 THEOREM U.  [PROVED by modification of Theorem S; referee check recommended]  Let T be the design D'', N >= 1 and
f in S_{p*} with F finite.  Call a block COMPENSATED if it contains two bad resonant strict non-peaks l^pm_m with
q_{l^+_m} > 0 > q_{l^-_m} and gaps >= gamma_B > 0, and UNCOMPENSATED if all its bad strict non-peaks with q != 0 and all its
bad peaks of swallowing type (varsigma eps = +1, degenerate or not; their q = Phi M/(mC) > 0) have q of one sign.  Assume:
 (E1) r*_l > 0 for every good l (S*_l := S_l \ (F cup union_{l' bad} supp y_{l'}));
 (E2) gamma_T := inf{1 - |z_j| : j in union_{l bad} supp y_l, j notin F cup K} > 0;
 (E3) every block is compensated or uncompensated;
 (E4) in compensated blocks: bad strict non-peaks with q < 0 have gap >= gamma_B; no bad degenerate peak with varsigma eps = +1;
 (E5) (H2') (2.2) in every block;
 (W_U) liminf_l [1 + Lambda*_f(l) + K_P(l) + K_nn(l) + 1/gamma_T]^2 / (l 2^{l^3} Lambda°(l)) = 0, with the RELATIVE rates
      K_P(l) := max{Phi_{l'}/mu_{l'} : l' <= l bad non-degenerate peak of SWALLOWING type (varsigma eps = +1) in a
                COMPENSATED block}  (no margin condition at all in uncompensated blocks, and none for peaks with
                varsigma eps = -1),
      K_nn(l) := max{Phi_{l'}/|q_{l'}| : l' <= l bad strict non-peak in an uncompensated block, q != 0, gap > M/2}.
Then f is in Rec.  No (H1), no resonance of non-compensator carriers, no bound on the number of bad carriers; maximal
contact is allowed ((E2) is then vacuous and (E5) holds by 2.2).
Proof.  Window l_* (beyond the compensators and the peaks of (E5)), t in W(l_*), t <= min(t_eta,1), a two-sided
decomposition, B_* := B cap [1,l_*], T_0 := union_{B_*} supp y_l, m_l := ||v_l 1_{S_l \ (F cup T_0)}||_1 (>= m^des_l(l_*) minus
the F-part, which is nonzero for finitely many l only).
(1) Good carriers.  Lemma modswallow(a) (good inequalities on S*_l only involve later good carriers) gives
sum_good |Delta theta_l| <= K_* t, K_* := (1/q_0 + 22) Lambda*_f(l_*).  Write Delta B 1_{F^c} = L(tau) + e_0 with
L(tau) := sum_{B_*} eps_l tau_l u_l 1_{F^c} and ||e_0||_1 <= K_* t + 6t^2 (fine carriers, box bound and (P2)).  Then
c(tau) := sum_{j notin F} phi_{z_j}(L_j(tau)) <= t/q_0 + 2||e_0||_1 (Lemmas switchbudget, phicalc(c)).
(2) Signatures.  On S_l \ (F cup T_0), l in B_*, only u_l among the bad coarse vectors is nonzero and z = eps_l, so
2 (tau_l)_- m_l <= c(tau) (Lemma phicalc(a)).  With 2.2 this gives |Delta d_m| M_m <= K_d t, K_d <= C_f (1 + K_*).
(3) Drop bounds.  (peakshift) gives varsigma eps tau_l/lambda_l in [Delta d M, Delta d M + t/(sigma|alpha(k)|)] at every
bad peak (for degenerate peaks the upper end is +infinity).  Peaks with varsigma eps = -1 (degenerate or not): tau_l <=
lambda_l K_d t and (tau_l)_- <= c/(2m_l), so |tau_l| <= lambda_l K_d t + c/(2 m_l): pinned with design constants.  In an
UNCOMPENSATED block let Sigma consist of the bad strict non-peaks with q != 0 and the bad peaks (degenerate or not) with
varsigma eps = +1; all have q of one sign (for these peaks q = Phi M/(mC) > 0).  The remaining carriers of the block enter
A of 2.4 with design-bounded or zero contributions (d-neutral: w = 0; varsigma eps = -1 peaks: as just shown; good: K_*;
fine: t^5), so 2.4 gives |tau_l| <= A/|q_l| + c/(2m_l) for l in Sigma, A <= C_f (K_d + K_* + 1) t.  Here |q_l| = Phi_l M/(mC)
for the peaks and |q_l| >= M Phi_l/(2mC_m) for non-peaks with gap <= M/2, so 1/|q_l| <= 8N 2^{m+k}/c_l (M >= 1/2,
C_m <= 2^{-m}); for non-peaks with gap > M/2, 1/|q_l| <= K_nn/Phi_l.  In a COMPENSATED block: peaks with varsigma eps = +1
are non-degenerate by (E4) and |tau_l| <= t/mu_l + lambda_l K_d t <= t K_P/Phi_l + lambda_l K_d t.
(4) Projection.  Let P be the pattern of f (kept: d-neutral bad strict non-peaks, and q != 0 bad strict non-peaks of
compensated blocks; dropped: all bad peaks, and the q != 0 non-peaks of uncompensated blocks; labels of T_0 from F, z),
b_l := 12 lambda_l/t.  The actual tau violates (con) by <= c/2 in total, (room) by <= c/gamma_T, (sgn) by <=
c sum_{l<=l_*} 1/(2 m_l), (drop) by the sum of (3), (box) not at all (|tau_l| <= 6 lambda_l/t).  By 5.2 there is
tau' in Z_P(b) with ||tau - tau'||_1 <= H_comb(l_*) V(t).  Collecting (1)-(3) (with c(tau) <= C_f(1 + K_*) t, sum 1/m_l <=
C_f sum 1/m^des(l_*), sum over peaks of t/mu_l <= t K_P sum 1/Phi_l, sum over Sigma's of A/|q_l| <= A(sum 8N2^{m+k}/c_l +
K_nn sum 1/Phi_l)):  V(t) <= C_f (1 + K_* + K_P + K_nn + 1/gamma_T)^2 (1 + sum_{l''<=l_*}(1/m^des_{l''} + 8N 2^{m+k}/c_{l''}))^2 l_* t,
so H_comb(l_*) V(t) <= C_f (1 + K_* + K_P + K_nn + 1/gamma_T)^2 Xi(l_*) t.  (Every product of design factors occurring
here, including K_d <= C_f (1 + K_*) (1 + sum 1/m^des) and the pair constants of 2.2, has degree <= 4 in the bracket defining
Xi, and every product of f-dependent rates has degree <= 2; C_f depends only on f, N, gamma_B and the fixed carriers.)
(5) Exact d-neutrality.  In a compensated block put e_m := sum_{kept, m(l)=m} q_l tau'_l; by (didentity) as in Theorem C
Step 3 and ||tau - tau'||, |e_m| <= C_f(K_d + K_* + H_comb V/t) t; add (e_m)_-/q_{l^+_m} to tau'_{l^+_m} and (e_m)_+/|q_{l^-_m}|
to tau'_{l^-_m}.  The rows (con),(room),(sgn),(drop) stay satisfied: compensators are kept, resonant (z-signed on K, zero
off F cup K), so the polyhedron is upward closed in their directions.  In uncompensated blocks every kept carrier has q = 0.
So tau'' satisfies sum_{m(l)=m} q_l tau''_l = 0 for all m, and V'' := L(tau'') is z-signed on K and vanishes off F cup K:
on T_0 by (con),(room); on S_l \ (F cup T_0) it equals eps_l tau''_l v_l with tau''_l >= 0 or = 0 and z = eps_l there;
elsewhere every coarse bad vector vanishes.  ||Delta B 1_{F^c} - V''||_1 <= ||e_0|| + ||tau - tau''||_1 <= K_U t with
K_U(l_*) := C_f (1 + Lambda*_f + K_P + K_nn + 1/gamma_T)^2 Xi(l_*).
(6) Window two-piece data: Lemma windowtwopiece with tau'' (as in Theorem C Step 5): kept coordinates are d-neutral
(gap M), or q > 0 (any gap, shift trick), or q < 0 (gap >= gamma_B by (E4)); tau''_l/lambda_l <= 12/t by (box) except for
the compensators (fixed lambda); the d-sums vanish exactly; errors O(K_U t).
(7) Windowed averaging and Corollary D1 verbatim from Theorem S.  By (W_U) choose l_j with (1 + Lambda*_f + K_P + K_nn +
1/gamma_T)^2(l_j)/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0; then K_U(l_j) T_hi(l_j) <= C_f(...)^2 2^{-l_j^3}/(l_j Lambda°(l_j)) -> 0 and
n^w_{l_j}/K_U(l_j) >= l_j 2^{l_j^3} Lambda°(l_j)/(C_f(...)^2) -> infinity, which are the window hypotheses (the constants
of Lemmas onesidedtransfer and windowtwopiece depend only on f, N, gamma_B and the compensators).  QED
5.4 Remarks.  (a) Everything combinatorial (targets, slaving through later targets on earlier signature sets, contact
patterns, which carriers are kept or dropped, the number of bad carriers) is absorbed by the design: the Hoffman
obstruction of Remark rem:S(c) disappears; the d-row never enters a Hoffman system (explicit compensation, or dropping by
2.4).  (b) What remains f-dependent are RATES of near-resources: rooms of good signature sets (Lambda*), relative margins
mu/Phi of swallowing-type swallowed peaks in compensated blocks, relative d-coupling |q|/Phi of nearly neutral swallowed
non-peaks in uncompensated blocks, rooms at bad target coordinates; they obstruct only if they decay faster than
2^{-l^3}/Lambda°(l).  In uncompensated blocks weak peaks are harmless: swallowing-type peaks are d-pinned (2.4, q = Phi M/(mC))
and the others are pinned by the budget and (peakshift).  (c) Not covered by Theorem U
itself: blocks that are neither compensated nor uncompensated (an f with such a block is covered by Z4 Corollary 4.1, applied
to all blocks at once, under its growth condition with the f-dependent Hoffman constants H^Z_f: a rate condition); non-rigid swallowing-type degenerate peaks in compensated blocks (rigid ones: Theorem V; 8.3); q < 0
swallowed non-peaks with gaps -> 0 in compensated blocks (a rate: Z4 Step 7, c_flat = min(c^0, gamma/(2A_2)) with t_1 independent
of gamma, and Theorem windowed with j-dependent c_flat — checked against the proofs of Lemmas uniformtransfer, onesidedtransfer and
Theorem windowed); F infinite.
5.5 Sign-alternating signatures.  [PROVED]  Replacing h_l by h^alt_l := sum_i (-1)^i 2^{-s_i} e*_{s_i} (s_0 < s_1 < ... the
enumeration of S_l, s_1 = s_0 + 1) keeps Theorem SLD and Section 8 valid (|v_l| in place of v_l, r_l := ||v_l 1_{S_l\F}||_1 -
|<v_l 1_{S_l\F}, z>|, Lemma phicalc(d) applied to |v_l(s)| and z_s sgn v_l(s); the (T-c) estimate uses |h_l(s)| = 2^{-s}).  If
S_l cap F is empty and z is constant on S_l, then r_l >= ||v_l||_1 (1 - |sum (-1)^i 2^{-s_i}|/sum 2^{-s_i}) >= ||v_l||_1/2.
Hence every f with F finite and z constant (= eps) on all but finitely many S_l is in R_0^pm: the literal case (O3)
"z = eps off F" disappears.  Swallowing becomes z = eps_l sgn h^alt_l on S_l \ F; Remark rem:nodesign is unchanged.

5.6 Farkas pinning and d-rigidity (THEOREM V).  [Proposition P PROVED; Theorem V PROVED by modification, referee check
recommended]  Notation of 5.3: level l_*, B_*, T_0, L_j; q_l := eps_l Phi_m(k) w_m(k)/(m C_m) for EVERY bad carrier (for a peak
q_l = varsigma eps Phi M/(mC)); Q_m(nu) := sum_{l in B_*, m(l)=m} q_l nu_l.  The d-neutral zero-cost cone with peaks free is
 C_0^+(l_*) := {nu in R^{B_*}: nu_l >= 0 (all l); z_j L_j(nu) >= 0 (j in T_0\F, |z_j| = 1); L_j(nu) = 0 (j in T_0\F, |z_j| < 1);
               nu_l = 0 (peaks with varsigma eps = -1); Q_m(nu) = 0 (all m)}.
A bad carrier l is d-RIGID at level l_* if nu_l = 0 for all nu in C_0^+(l_*).  Extension by zero maps C_0^+(l) into C_0^+(l+1)
(a new row at j in T_0(l+1)\(T_0(l) cup F) reads eps_l nu_l v_l(j) for the unique l with j in S_l, or 0, and z_j = eps_l there), so
rigidity at level l+1 implies rigidity at level l.
Proposition P.  If l_0 is d-rigid at level l_*, then by Farkas' lemma (-nu_{l_0} >= 0 on the polyhedral cone C_0^+)
 -e_{l_0} = sum_l y_l e_l + sum_{contacts} y_j z_j L_j + sum_{rooms} y'_j L_j + sum_{anti peaks} y'_l e_l + sum_m kappa_m Q_m
with y >= 0, and for every tau in R^{B_*}, evaluating, moving y_{l_0} tau_{l_0} to the left and bounding each other term below:
 (1 + y_{l_0}) tau_{l_0} <= ||(y,y',kappa)||_inf [sum_{l != l_0}(tau_l)_- + sum_{contacts}(z_j L_j(tau))_- + sum_{rooms}|L_j(tau)|
                            + sum_{anti}|tau_l| + sum_m |Q_m(tau)|].  QED
K_A(l_*) := max over the d-rigid swallowing-type peaks p <= l_* of the least ||(y,y',kappa)||_inf (finite, an LP).  In the window
argument (steps (1)-(3) of 5.3) every bracket term is O(t): (tau)_- <= c/(2m_l), contact/room violations <= c/2, c/gamma_T, anti-sign
peaks |tau| <= lambda K_d t + c/(2m), and |Q_m(tau)| <= |Delta d_m|M_m + 2t/sigma_m + (K_* t + 6t^5)/(mC_m) by (didentity).  Hence a
d-rigid swallowing-type peak satisfies |tau_p| <= (1 + K_A) C_f (1 + K_* + K_d)(1 + 1/gamma_T)(1 + sum_{l<=l_*} 1/m_l) t, with no
margin and no non-degeneracy.
THEOREM V.  (a) In Theorem U, (E4)'s exclusion of degenerate swallowing-type peaks in compensated blocks may be replaced by "every
such peak is d-rigid at all levels", K_P may be restricted to NON-rigid swallowing-type peaks, and (W_U) is required with the bracket
[1 + Lambda*_f + K_P + K_nn + K_A + 1/gamma_T] raised to the power 3 instead of 2.  (b) In Z4 Theorem A run on the design D''
(with Z4's G*(l) inserted into the bracket of Xi(l)), and in Z4 Corollary 4.1 (original design, f-dependent Hoffman constants)
with the extra factor (1 + K_A(l))(1 + sum_{l' <= l} 1/m_{l'}(l)) in its growth bracket, (H3) may be replaced by (H3_rig): every
degenerate swallowing-sign swallowed peak is d-rigid at all levels; and the margin sum M_f may be restricted to non-rigid peaks.
Proof.  The only place where these proofs use the margin of a swallowing-type peak, or its non-degeneracy, is the bound on its
drop-row violation |tau_p| (5.3 step (3); Z4 Steps 3-4 through M_f) and the window-certificate error at the dropped peak, which is
lambda(|omega_+| + |omega_-|) <= |tau_p| + lambda|Delta d|M by (peakshift).  Replace that bound by Proposition P (at most l_* rigid peaks, each
with the bound displayed above).  The new term is a product of K_A with rates already present (K_*, 1/gamma_T) and with the design
factor sum 1/m_l, hence the power 3 in (a) and the extra factor in (b); D'' absorbs sum 1/m_l through 1/m^des in Xi.  QED
Reading.  In an uncompensated block every carrier of the same-sign set is d-rigid with the certificate y_l = q_l/q_p (l in Sigma,
l != p), y'_l = q_l/q_p (anti peaks), kappa_m = -1/q_p, of norm <= (1 + max|q|)/q_p; this is 2.4 in Farkas form.  A NON-rigid
swallowing-type peak can be switched by a zero-cost, exactly d-neutral direction: an exact resource which window two-piece data
cannot carry (they vanish at bad peaks).  In a compensated block every RESONANT swallowing-type peak is non-rigid (e_p plus a
multiple of the compensator l^- lies in C_0^+), so (a) helps only for non-resonant ones there.
Corollary V.1 [PROVED].  A non-rigid swallowing-type peak p of block m forces a NON-rigid bad strict non-peak l of block m with
q_l < 0.  Proof: take nu in C_0^+ with nu_p > 0.  Anti-sign peaks vanish on C_0^+ and nu >= 0, so Q_m(nu) = 0 with q_p nu_p > 0
needs some l in block m with q_l < 0 and nu_l > 0; peaks with q < 0 are exactly the anti-sign peaks, so l is a strict non-peak, and
nu_l > 0 shows it is not rigid.  QED  Hence case 8.2(d) lives only in blocks with d-coupled q < 0 swallowed non-peaks (mixed or
"negative" blocks); at maximal contact such configurations can occur (SKETCH, as in 6.1: density gives resonant targets with u_l(xi)
slightly negative), so (d) is a genuine case there.

## 6. Task (a): the most dangerous candidate, its mates, and recovery attempts
6.1 Data.  [construction SKETCH; listed properties PROVED once the data exist]  SLD (or D''), one block suffices,
F = {j_0}, a = e*_{j_0}/q*(e*_{j_0}), z := 1 on N \ F (MAXIMAL CONTACT).  Then K = N \ F, every signature set is exactly
swallowed with eps_l = 1, every carrier is bad, and the block data are determined by the values u_l(zhat) relative to the
thresholds.  Required features (codimension conditions on a, or on a and further coordinates added to F; existence of
data with infinitely many of each by a nested Baire/intermediate-value construction along the dense target sequence:
SKETCH — for every open set of parameters some target separates two of its points, hence some carrier value crosses its
threshold inside it):
 (C1) peaks of both signs in the block (automatic by density): exact two-piece data are d-neutral (2.3);
 (C2) infinitely many weak peaks with relative margins mu_{l_i}/Phi_{l_i} <= 2^{-2^{l_i^4}} (failure of (MS) and of (W_U));
 (C3) infinitely many resonant strict non-peaks (y_l >= 0 off F, y_l(j_0) < 0 balancing u_l(zhat) ~ 0), all with
      u_l(xi) > 0 (q_l > 0: uncompensated block), some near-threshold (gap -> 0), some nearly neutral with
      |q_l|/Phi_l <= 2^{-2^{l^4}};
 (C4) slaving: later targets meet earlier signature sets ((H1) fails), as forced by density.
Position.  f is not in R_0^pm (all r_l = 0), not in R_S (B infinite with non-d-neutral peaks), not (BT) ((C2) violates
(MS), (C3) gives infinitely many strict non-peaks), not in R_C ((H1) and (W*_P) fail).  No theorem of the note applies.
For D'' (Section 5) the block is uncompensated, so only the nearly neutral part of (C3) violates (W_U) (through K_nn).

6.2 Mates.  Single module.  [SKETCH with explicit constants]  For a resonant bad strict non-peak l = j(k,m) with gap
gamma > 0 and q = q_l, let g_c := c (u_l - (Phi_k w(k)/(m C)) R^*_m w_m) = (c/lambda_k) y_{k,m} (a balanced finite
certificate, b = 0, omega = (c/lambda_k) e_k).  Then g_c in C(f) as soon as
 c^2 <= min( gamma lambda_k q_0/(8 q sigma_m), (M + |w(k)|) lambda_k/(16 m_u) ) and c <= c_0(f),   m_u := ||u_l 1_{F^c}||_1:
for |r| below the radius the certificate expansion (Proposition expansion, Lemma slack(b)) applies; for r > 0 beyond
gamma lambda/(2c) use the base decomposition a + r c u_l, (1 - r c q) w (z-signed: no first-order base cost; levels
1 + r c q sigma_m/q_0 + O(r^2c^2) and 1 - r c q), valid for r >= 4 c q sigma_m/q_0; for r < 0 the certificate moves the
coordinate k inward and stays valid up to |r| <= (M + |w(k)|) lambda/(2c) (sup norm (1 - d r)M as in Theorem C, Step 5),
beyond which the base decomposition with wrong-signed contact mass costs 2|r| c m_u <= r^2/4 for |r| >= 8 c m_u; large |r|
by p*(g_c) small.  Such g_c lies in Cert(f) and is recovered along the canonical truncations (Theorem transfer).
Transient band (PROVED structure, HEURISTIC sizes): the forced switching through l vanishes below ~gamma lambda/c
(two-sided usage) and above ~c m_u (base on both sides), and is positive in between; finite models (Section 7) confirm
the band and the law  max_t (forced switching)/t ~ c^2/(4 gamma lambda_k) <= (M + |w|)/(2 gamma m_u).
Module sums.  [HEURISTIC]  g = sum_i c_i (u_{l_i} - q_{l_i} R^* w), c_i decaying fast, scales super-separated: at each t at
most one module is in its band, coarser ones are certificates, finer ones sit on the base on both sides at cost
2|t| sum_finer c_i m_u <= epsilon t^2.  Such g switch at all small scales, by 4.2(b) they are proportional on private parts
of the l_i, and their switching relative to t is ~ c_i^2/(gamma_i lambda_i) inside the band of l_i.  Validity of the
module forces c_i^2 <~ min(gamma_i lambda_i q_0/(q_i sigma), (M + |w|) lambda_i/m_u), hence
  switching/t <~ min( q_0/(q_i sigma) , (M + |w|)/(gamma_i m_u) ):
~1/Phi_i for near-threshold carriers (q_i ~ M Phi_i/(mC), the bound of 2.4) and ~1/m_u <= n_l/delta°_l for nearly neutral
ones (gap ~ M).  Both are DESIGN quantities: not window-pinned for the SLD (1/lambda_i >> n^w), but window-pinned for D''
(the first by Theorem U, the second only under Conjecture G below).  Weak peaks (C2) add
transient one-sided capacity t/mu_l (peakshift), with mates vanishing on their private parts up to the uniform-shift
trace (4.2(c)).

Conjecture G (geometric transient bound) [OPEN; supported by the module computation and Section 7: R3 (near-optimal cap)
kappa = 0.1 gives forced switching/t <= 0.034 while 1/m_u = 1.37, R4 (true cap s(t)) gives forced switching 0, and R5 (two
modules, joint) gives joint forced switching <= 0.1 t].  If l is a swallowed strict non-peak with gap >= M_m/2 in an uncompensated
block, then at every scale t some two-sided decomposition switches through l by at most C t/m_u(l), C absolute.
A joint version (one decomposition doing this simultaneously for all coarse such carriers, with sum_l C t/m_u(l))
would allow deleting K_nn from (W_U) (HEURISTIC implication).

6.3 Recovery attempts.
 (i) Windows at f (Theorems Bstar, S, C): FAIL for the SLD (constants 1/q_l ~ 1/Phi_l, 1/mu_l, Hoffman constants of the
     slaved systems exceed n^w_l).  [PROVED: the hypotheses fail; sharpness of 2.4 is supported by Section 7.]
 (ii) Design D'' and Theorem U: the candidate's block is UNCOMPENSATED (all q > 0, positive peaks are of swallowing
     type), so its weak peaks (C2) of either sign, its near-threshold non-peaks (C3) and the slaving (C4) cost only DESIGN
     constants; the candidate is recovered for D'' unless its nearly neutral non-peaks have relative d-coefficients
     |q_l|/Phi_l decaying faster than 2^{-l^3}/Lambda°(l) (rate K_nn).  [PROVED for D'' given Theorem U]
 (iii) Certificates: every single module is in Cert(f) (recovered); module sums with gaps bounded below and
     c_i^2 <= epsilon gamma_i lambda_i are in cl Cert(f) by windowed averaging of truncated certificates (truncation at the
     modules whose radius exceeds c_0 t; error sum of dropped c_i <= K t with K ~ 1/(gamma_i delta°_i)).  [SKETCH]
 (iv) Far lowering f^L (z^L = 0 on S_l, l > L): f^L has finitely many swallowed carriers, satisfies (H2) (automatic) and
     (H3) iff no swallowed degenerate peak of swallowing type below L; so f^L in R_S when the remaining conditions hold.
     dist(rho g, C(f^L)) -> 0 holds for module sums (drop the modules beyond L, cost sum_{i: l_i > L} c_i; the coarse
     modules use only data that f^L keeps): SKETCH.  For general mates: OPEN ((O2) of the note; the Z4 referee argues,
     HEURISTIC, that far lowering cannot help where window arguments fail).
 (v) Exactification (near -> exact resources: near-contacts to contacts, weak peaks to degenerate peaks, nearly neutral
     to neutral): moves f by O(room), O(mu), O(|q|) in norm.  For D'' the exactified first rows satisfy (W_U) and fall
     under Theorem U (degenerate peaks of swallowing type are dropped by 2.4 in uncompensated blocks).  The missing step is
     lower semicontinuity of the fibre along exactification: OPEN (Z3 Theorem E / Proposition T make the transfer rigorous
     under scale decoupling c(delta) = o(T_lo^2) with well-conditioned companion cones; Z3's BAND of rooms between T_lo^2 and
     1/K is exactly the super-fast-rate regime).  Caution (PROVED by the budget): exactification is not
     monotone for fibres — a near-contact of room eta admits two-sided base mass <= t/(q_0 eta) at scale t, an exact
     contact does not.

6.4 The exact property that would have to fail (task (a)).
 For the SLD operator:  (UERP) at the window scales t in W(l_*), some two-sided decomposition is within K(l_*) t (l_1) of
 an exact d-neutral resonance (z-signed on K, zero off F cup K, admissible block data), with K(l_*) = o(n^w_{l_*}/l_*)
 along a subsequence.  For the candidate (UERP) can fail only through (a) Hoffman constants of the slaved combinatorial
 systems, (b) 1/Phi-type d-pinning constants and 1/m_l signature constants, (c) f-dependent relative rates: margins (C2)
 and d-coefficients (C3).  (a),(b) are design quantities and are removed by D'' (Theorem U), and in the (uncompensated)
 candidate block (C2) is harmless for D'' as well; only the nearly neutral part of (C3) remains.  So for D'' a counterexample to density would need a mate of a first row whose
 relative margins / relative d-coefficients / rooms decay faster than 2^{-l^3}/Lambda°(l) (or a mixed-sign
 uncompensable block, or infinite F), which is NOT recovered along any approximants.  Nothing found indicates this.

## 7. Finite-model numerics (scripts: r5/Z6_work/toy.py, exp_module.py, scan_module.py, scan_cap.py, joint_G.py)
Model: R^26, q*(A) = ||A||_1 + ||U^T A||_2 (U 26x4, rows ~ 0.15*2^{-0.3 j}), one block with 6 carriers u_k = y_k + 0.15 h_k
(3 private signature coordinates each), five strong peaks of both signs (u_k(xi)/threshold = 14.4, -20.5, 55.9, -68.2,
77.9) and one module carrier l, y_l >= 0 off F = {0}, y_l(0) tuned so that w(k_l) = kappa M (q_l > 0).  Maximal contact:
a = e_0/q*(e_0), z = 1 everywhere; forced data computed by SOCP (block primal norm, norming functionals), p* by SOCP
(Clarabel).  Module mate g = c(u_l - q_l L^* w) (|g(xi)| < 1e-7).  For t in [3e-3, 0.5]: mate test p*(f +- t g) <= s(t), and
the minimal switching |Delta theta_l| over pairs of decompositions with max(q*, N) <= p*(f -+ t g) + 0.05 t^2.
(R1) Phi_l = 2e-3, kappa = 0.5, c = 0.02: mate at all t; forced switching 0 (< 1e-11) for t <= 0.046, positive on
     [0.065, 0.18] (max 6.4e-3, resonant sign), 0 for t >= 0.25; spurious switching up to 0.5 allowed at small t.
(R2) Phi_l = 2e-4: c = 0.02 valid (forced switching/t <= 0.99); c = 0.03, 0.05 NOT mates (the - side fails on
     t in [8e-3, 9e-2], excess up to +1e-3), matching the validity threshold c^2 ~ 2(M + w) lambda/m_u within a factor 2.
(R3) Phi_l = 2e-3, max forced switching/t at valid c: kappa = 0.10 (gap 0.85): 0.034;  0.50 (gap 0.47): 1.21 (c = 0.07);
     0.90 (gap 0.092): 6.4 (c = 0.07; c = 0.085 invalid);  0.98 (gap 0.020): 23.9 (c = 0.085, max at the smallest grid
     scale).  Fit: ratio ~ c^2/(4 gamma lambda) (3.0 vs 3.06 predicted when c: 0.04 -> 0.07).
(R4) (scan_cap.py) Same, but with the TRUE cap s(t) of Lemma twosided (the criterion relevant for window pinning):
     kappa = 0.98, c = 0.085: forced switching/t = 23.4 at t = 3e-3, decreasing to 0 at t >= 0.23 (switching is forced
     although p* - s(t) ~ -0.45 t^2: moving the component costs first order); kappa = 0.5, c = 0.07: <= 0.78;
     kappa = 0.1 (nearly neutral), c = 0.04: forced switching = 0 at ALL scales.
     For c^2 << gamma lambda / p*(u_l - q R^* w) a module is a mate already by Proposition expansion below its radius and
     the triangle inequality p*(f + r g) <= 1 + |r| p*(g) above 2.5 p*(g) (PROVED, elementary); the switching modules are
     the larger ones, up to the validity limit.
(R5) (joint_G.py; two module carriers l1, l2 of the same block, mate g = g1 + g2 at the SAME scales, cap s(t), R^30):
     kappa = (0.1, 0.1), c = (0.04, 0.04): a mate; forced switching 0 except on t in [0.07, 0.10], where min|Dtheta_1|/t = 0.043,
     min|Dtheta_2|/t = 0.024 and min(|Dtheta_1| + |Dtheta_2|)/t = 0.096 > 0.067 (the two cannot be minimized together), all <<
     1/m_u = 1.37.  So, unlike a single module (R4), a SUM of nearly neutral modules can force switching near its validity
     boundary, but jointly of size << t/m_u.  c = (0.05, 0.05): not a mate on [0.047, 0.154] (validity of sums is the binding
     constraint).  kappa = (0.9, 0.1), c = (0.05, 0.04): min|Dtheta_1|/t up to 1.29 (near-threshold, as in R3), min|Dtheta_2| = 0,
     but min(|Dtheta_1| + |Dtheta_2|)/t up to 1.97: minimizing the near-threshold switching pushes switching (<= 0.7 t) onto the
     nearly neutral carrier (channel sharing of same-sign carriers, allowed by 2.4).  One solver warning (inaccurate) at
     t = 4.5e-3 in the last run.  Joint Conjecture G is consistent with R5 (C = 0.05 suffices there).
Reading: the switching profile is a transient band; near-threshold modules switch >> t but within the 2.4 bound K_d/q
(q ~ 0.034 here); nearly neutral modules need no switching at all under the true cap (evidence for Conjecture G).  Finite models are degenerate (every functional attains its norm);
they test only the local multi-scale geometry, not recoverability.

## 8. What remains open (precise), and partial routes
8.1 For the SLD operator of the note: Lemma Z is OPEN.  Beyond Theorems Bpm, S, C and Corollary BTrecovered, the obstruction
at F finite is the failure of window pinning with window-compatible constants: Hoffman constants of the slaved
combinatorial systems (when (H1) fails, e.g. maximal contact), the d-pinning constants 1/|q_l| >= mC/(M Phi_l) of
uncompensated swallowed carriers, and f-dependent rates.  The first two are DESIGN quantities but exceed the SLD window
lengths (n^w_l ~ l 2^{l^3} Lambda°(l) << 1/c_{l-1}).
8.2 For the design D'' (5.1; admissible, all of Section 8 and Theorems C, U, V hold, and so do Z4 Theorem A once Z4's
configuration constant G*(l) (made N-independent as the Z4 referee requires) is inserted into the bracket of Xi(l), which keeps
D'' admissible and makes its windows dominate those of SLD_G, and Z4 Corollary 4.1, whose window requirement D'' exceeds): Lemma Z is OPEN exactly for pairs (f, g) with g not window-pinned and f outside R_0^pm cup R_S cup R_BT cup R_C cup R_U cup
R_V cup R_SBinf (R_V: Theorem V; R_SBinf: Z4).  With F finite this means one of:
 (r) super-fast RATES: rooms of good signature sets (Lambda*), margins of NON-rigid swallowing-type swallowed peaks, relative
     d-coefficients of nearly neutral swallowed non-peaks in same-sign blocks (K_nn; removable under a joint Conjecture G), gaps of
     kept q < 0 non-peaks, rooms at bad target coordinates (gamma_T), the Farkas constants K_A, and in mixed-sign blocks without (DR)
     the f-dependent Hoffman constants H^Z_f of Z4 Corollary 4.1 (for one-signed blocks, which Theorem U handles, they are at
     least design-scale by the Z4 referee's Lemma R and at most design-scale times (1 + K_nn) by 2.4; in mixed-sign blocks without
     (DR) their size is OPEN);
 (d) NON-rigid degenerate swallowing-type peaks (a zero-cost exactly d-neutral direction switches through them; by Corollary V.1
     only in blocks with non-rigid q < 0 swallowed non-peaks; see 8.3 and the Z4 referee's (FS) route, open at maximal contact);
 (h) failure of (H2') (no pinning of the uniform shift: e.g. all swallowing-type swallowed peaks of a block degenerate and no
     good non-degenerate peak);
 and (O4) infinite F (Z5).
 Natural route for (r): exactification approximants f' (6.3(v)) have bounded rates; what is missing is lower semicontinuity of the
 fibre along them (the Z4 referee doubts lsc along far lowerings helps; exactification is a different approximation, OPEN).
 For (d): exact resources need peak-carrying two-piece data and an engineering theorem tolerating them (8.3).
8.3 Extended two-piece data with degenerate peaks.  [SKETCH, with a gap]  Allowing omega^pm on degenerate peaks with the
inward signs varsigma omega^+ <= 0 <= varsigma omega^- gives Delta d >= 0 contributions (Phi^2 M/C)(|omega^+| + |omega^-|)
and the second-order block expansion of a strict non-peak.  In the engineered approximants of Theorem engineered the
degenerate peak drifts by O(s_1) relative to its threshold (through e' - e, from the window masses), which costs
first order |tau| s_1 times a data-dependent constant if it drifts into the peak region.  The drift is favourable for
symmetric data (b^theta = 0 on contacts: no window masses, the truncation tail lowers varsigma u_l(x')), or under a
steering condition (the map beta -> (<U^* u_l, P^perp U^* beta>)_l from l_1(F) onto R^{#used}); in general this is OPEN.
8.4 No counterexample is claimed, and none is indicated: every single switching module is recovered, the module
sums with gaps bounded below are in cl Cert(f) (SKETCH), and every combinatorial obstruction disappears under D''.

## 9. Labels
PROVED: 2.1, 2.2 (and (H2) -> (H2')), 2.3, 2.4, Lemma F and 4.2(a)-(d), Theorem C (with Step 5's shift trick), 5.1
(D'' admissible, Section 8 survives), 5.2, Theorem U (by modification of Theorem S; referee check recommended), 5.5, monotonicity of
C_0^+, Proposition P and Corollary V.1 (5.6), Theorem V (by modification of Theorem U and of Z4 Theorem A / Corollary 4.1; referee check
recommended), the gap-rate observation in 5.4(c) (checked against the proofs in the note; also Z4 Step 7),
6.1 "Position" (given the data), the claims of 6.3(i),(ii), the budget caution in 6.3(v).
SKETCH: existence of the candidate data 6.1; single-module mates 6.2 (routine estimates, constants written); module sums
in cl Cert(f) 6.3(iii); far lowering for module sums 6.3(iv); 8.3.
HEURISTIC: module-sum mates 6.2 and their switching sizes; the reading of Section 7; generic validity of (W_U).
OPEN: Lemma Z (SLD and D''); Conjecture G; lsc along exactification and far lowering for general mates; cases
8.2 (r),(d),(h); the size of H^Z_f in mixed-sign blocks without (DR); infinite F.
FALSE: nothing new; reconfirmed that exact two-piece data cannot carry Delta d != 0 at doubly swallowed blocks (2.3), so
the relaxation "Delta d >= 0" of Corollary D1 does not help at maximal contact (as the Z2 referee noted for roomy sets).

## 10. Referee checklist for Theorem U (the points where it departs from Theorem S)
 1. No (H1): (tau_l)_- of every coarse bad carrier is read off its private signature part S_l \ (F cup T_0), where among
    coarse bad vectors only u_l lives; coarse good and fine bad contributions are in e_0 (||e_0|| <= K_* t + 6t^2).
 2. Peaks are dropped with design constants except swallowing-type peaks in compensated blocks: (peakshift) with
    varsigma eps = -1 gives tau <= lambda K_d t; varsigma eps = +1 peaks in uncompensated blocks are in the same-sign set of
    2.4 (their q = Phi M/(mC)); the window-certificate error at a dropped peak is lambda(|omega_+| + |omega_-|) <=
    |tau_l| + lambda|Delta d| M by (peakshift), so no margin enters there either.
 3. Hoffman is applied only to the combinatorial system (con, room, sgn, drop, box); its constant depends on the matrix,
    not on the right-hand side b = 12 lambda/t; the d-row is handled by compensation (upward closure in resonant
    directions) or vanishes (uncompensated blocks keep only d-neutral carriers).
 4. The averaged data are exact, d-neutral, supported on finitely many strict non-peaks (positive gaps at f), so
    Corollary D1 applies without change; the shift trick of Theorem C Step 5 is used for kept q > 0 carriers.
 5. Window arithmetic: every design product is of degree <= 4 in the bracket of Xi, every product of f-rates of degree
    <= 2; Xi(l) is computable at stage l of the design (targets, signatures, c_{l''}, l'' <= l).
 6. Theorem V: Proposition P is applied at a fixed level l_* to the finite system C_0^+(l_*); its certificate may use the d-rows
    with free coefficients because |Q_m(tau)| = O(t) by (didentity) once Delta d is pinned ((H2')); rigidity is used at the
    window levels only, and rigidity at a level implies rigidity at all lower levels.
Scripts: r5/Z6_work/toy.py (model, SOCP for p*, forced data), exp_module.py (single module profile), scan_module.py
(near-optimal cap scan), scan_cap.py (true cap s(t)), joint_G.py (two modules, joint switching, R5).

## 11. Relation to the other Round-5 reports (Z3, Z4 and its referee, Z5)
Most of Sections 2-5 were found before reading Z3/Z4; the overlaps are real and are stated here so that nothing is
double-counted.
Z4 (Theorem A, design SLD_G, Corollaries 4.1-4.2) and the Z4 referee report.
 - Combinatorial Hoffman constants as design quantities (5.2) = Z4's configuration constants G*(l) (Z4's "single most valuable
   idea"); D'' = SLD_G with additional design factors 1/m^des and 2^{m+k}/c_l in Xi.  Z4 converts l_1 projection errors into
   coordinatewise bounds by active sets U(t) = {lambda_l >= t^2}; Theorem U does it by putting the box rows (|tau_l| <= 12 lambda_l/t)
   into the Hoffman system (Hoffman constants do not depend on right-hand sides).  Either works.
 - 2.2 (shift pinning by a pair of swallowed peaks) = Z4's (H2') (the Z4 referee's (H2'') is weaker still).
 - Compensated blocks of Theorem U are contained in Z4 Theorem A: Z4's (DR) (fixed zero-cost repair directions with d-sums of
   both signs) generalizes the resonant compensator pair of Theorems C and U; Z4 Step 7 makes gaps of kept carriers a rate.
 - NEW relative to Z4 and its referee: (1) same-sign (uncompensated) blocks.  The Z4 referee's Lemma R shows that there the d-row
   Hoffman constant is at least design-scale (>= mC/c_l), so Z4 Corollary 4.1 does not help and (E-d) is listed as open.  2.4 is the
   matching UPPER bound (design-scale times (1 + K_nn)), and D'' absorbs the design scale: Theorem U recovers such blocks with
   weak and DEGENERATE swallowing-type peaks (part of (E-a), including maximal contact, where the Z4 referee lists (E-a) as open),
   near-threshold d-coupled non-peaks (part of (E-b)), and one-signed d-resources (the same-sign part of (E-d)), the only rate
   being K_nn.  (2) Theorem V: margin-free pinning of d-rigid swallowing-type peaks in any block, so (H3) of Z4 Theorem A /
   Corollary 4.1 can be weakened to (H3_rig), with NO engineering step for degenerate peaks (they are dropped, not used), unlike
   the (FS) route of Z4 part 8 / the Z4 referee's 9.3.  (3) 2.3 (exact two-piece data are d-neutral on doubly swallowed blocks)
   is the peak case of the Z4 referee's finding 9 (sign-coherent far swallowing); Lemma F / 4.2 (forced switching = oscillation;
   mates are proportional to signatures on private parts under transience) complements Z4's rigidity Proposition 5.6.
Z3.
 - Z3 Lemma 5.1 (inward block moves need no gap) is the mechanism of the shift trick of Theorem C Step 5; Z3 Theorem 5.4
   (window-summable inverse margins of bad peaks) corresponds to K_P in Theorem C; Z3 Theorem 5.3 ((H3) harmless when the bad
   strict non-peaks of the block have q >= 0, via the d-shift identity) is the finitely-many-non-d-neutral case of the same-sign
   mechanism 2.4; Z3 lists infinitely many non-d-neutral bad strict non-peaks as remaining, and Theorem U covers the same-sign part
   of that case for D''.
 - Z3 Theorem E and Proposition T (exact data at a nearby exactified first row, under scale decoupling c(delta) = o(T_lo^2) and a
   companion-cone Hoffman bound) are the rigorous form of the exactification route of 6.3(v); Z3's BAND (rooms between T_lo^2 and
   1/K) is the precise obstacle to it, and is the same phenomenon as the super-fast rates of 8.2(r).
Z5.  Case (O4) (infinite F) is treated there (Theorems S-inf, B-inf, transfer at arbitrary a); nothing here concerns it.
Net new content of Z6 (for the record): 2.1, 2.3, 2.4, Lemma F and 4.2; Theorem C (SLD, gap-free q >= 0 kept carriers); the
uncompensated part of Theorem U (with D''); Proposition P and Theorem V; 5.5; the maximal-contact candidate analysis (6), the
module mates and their transient bands, Conjecture G and UERP; numerics R1-R4.
