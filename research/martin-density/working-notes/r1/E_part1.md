# E notes, part 1: framework for an adversarial search; first candidates and how they die

Status labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN / NUMERICAL (numerical evidence in an explicit model).

## 1.0 Setting (finite block set I unless said otherwise)

X = c_0, q*(a) = ||a||_1 + ||U*a||, p = q + ||L.||_V, blocks m with lambda_{k,m} = m Phi_m(k), u_{k,m} in S_{q*},
N_m(w) = ||w||_inf + ||D_m w||_2. For f in S_{p*}: normer xi, q_0 = q**(xi), forced decomposition f = a + L*w,
xhat := xi/q_0 = z + U e, e = U*a/||U*a||, z in B_{l_inf}, z = sign a on supp a.
Budget identity (A_notes Lemma 7.1): for an admissible decomposition f + t g = A_t + L* W_t,
  q_0 E_q(A_t) + (1-q_0) sum_m pi_m e_m(W_{t,m}) <= s(t) - 1,  s(t) = sqrt(1+t^2).
Base first-order excess of a + tB: sum_{j notin supp a} (|tB_j| - z_j t B_j) (plus flips and Hilbert terms).

Facts imported (all PROVED in the r1 notes, re-checked by me where used):
(F1) [G_referee 4.7] f'_n in NA cap S_{p*} tends to f iff f'_n = grad p(z'_n + U(U*a'_n/||U*a'_n||)) with
     a'_n in c_00 cap S_{q*}, a'_n -> a in l_1, z'_n in B_{c_0}, z'_n = sign a'_n on supp a'_n, z'_n -> z coordinatewise.
(F2) [Preprint A Thm 2.1; A_notes 3.1] C(f) compact, f -> C(f) upper semicontinuous.
(F3) [A_notes Cor 3.3] (f, rho g) in cl NA for all g in C(f), rho<1  iff  C(f) is contained in Li_n C(f'_n) for
     some NA sequence f'_n -> f.  A counterexample = (f, g in C(f), rho<1, delta>0) with dist(rho g, C(f')) >= delta
     for every NA f' with ||f'-f|| < delta.
(F4) [A_notes Thms 4.10, 4.17, 6.2, 6.5] every mate in cl Cert^sh(f) (finite/shifted/weighted certificates,
     locally admissible linear decompositions) is recovered along EVERY sequence f_n -> f.

## 1.1 Necessary conditions for a counterexample (PROVED, by collecting the above)

If (f, g, rho) is a counterexample then:
 (N-a) f is not NA, f is not in the residual set Omega of Preprint A, and C is not lower semicontinuous at f.
 (N-b) g is not in cl Cert^sh(f): g has no locally admissible linear decomposition, is not a weighted direction, etc.
 (N-c) [A_notes Prop 7.4] g has no pair of one-sided linear decompositions whose difference is in c_00
       (in particular, if supp a cup K is finite, K = contact set, g has no one-sided linear decompositions on both sides).
 (N-d) Every NA f' near f has the form (F1); so a counterexample must defeat EVERY choice of (a', z'), including the
       completely free far coordinates of z'.
So the decompositions of f + t g must be genuinely scale dependent (A_notes 7.2: mechanisms N1-N4).

## 1.2 The "critical cross mate" candidate and its natural destruction mechanism

Single block, a in c_00, j notin supp a with |z_j| < 1 (two-sided base kink; the base cannot carry e_j* at
first order on either side, and z'_j must stay close to z_j for f' close to f, so the eta-trick of A_notes 8.3 is
not available at j: for fixed j, z'_j = +-1 forces ||f'-f|| >= delta_j > 0).
v := (e_j* - xhat_j a)/norm, so v(xi) = 0. Cross coordinates k_i (i = 1,2,...) with geometric lambda_i and
   u_{k_i} = (v + K lambda_i sigma_i)/n_i,   sigma_i(xhat) = 0,
where sigma_i = avg_{B_i} e* - c_i e_{j_0}*, j_0 in supp a, B_i far disjoint blocks with z = 1/2 on B_i (so xhat is
not in c_0). At f: u_{k_i}(xi) = 0, so every k_i is off-peak with w(k_i) = 0 and full gap M.
Mate g = c v: at scale t carry t c v through k_i with lambda_i ~ |t| c/M; base absorbs t c K lambda_i sigma_i at
first-order cost ~|t| c K lambda_i = O(t^2); block Hilbert cost t^2 c^2/(2C). For c small enough g in C(f). (SKETCH;
the computation is the one in A_notes 7.3 / D_notes 12.2.)

Destruction at NA approximants (SKETCH, elementary): for x' = z' + U e with a' = a and z' = z on a window,
sigma_i(x') = avg_{B_i}(z' - z) -> -1/2 as i -> infinity because z' in c_0. Hence u_{k_i}(x') ~ -K lambda_i/2 and,
if K/2 exceeds the block threshold constant, all but finitely many k_i are PEAKS of w' (with w'(k_i) = -M').
So at every NA f' near f the cross mechanism is available only down to a finite scale lambda_I (I chosen by the
approximant through the window), and below lambda_I the fine cross coordinates are gone on at least one side
(deep peaks with w' = -M serve only t>0 one-sidedly; on t<0 nothing).
This is the cleanest "lack of lower semicontinuity" I could build: the structure exists at all scales at f
and is truncated at a finite scale at every f'.

## 1.3 How it dies: the (multi-)frozen representation trick

Single frozen coordinate (SKETCH): put g' := rho c n_I u_{k_I} (an exact block vector at the finest available
off-peak coordinate). Then g' - rho g = rho c K lambda_I sigma_I -> 0, at scales |t| <= M lambda_I/(rho c) g' is
carried exactly by k_I (finite certificate, two-sided), and at larger scales the transferred cross mechanism of f
plus absorption of rho c K lambda_I sigma_I works. Cost bookkeeping shows the absorption roughly DOUBLES the
error part of the cost at scales ~ lambda_I, so a single frozen coordinate recovers only rho^2 < 1/(boundary factor).

Model M (NUMERICAL). Isolate the critical cross mechanism: coordinates i with lambda_i = r^i, at scale tau,
  P(tau) = min_x sum_i [ A |eta_i - lambda_i x_i| / tau + B x_i^2 ]   s.t. sum x_i = S, |x_i| <= M lambda_i/tau,
(A = q_0 K error weight, B = (1-q_0)/(2C) Hilbert weight; mate condition P <= 1/2 at all scales; two-sided symmetric).
At f: all i, eta = 0, S = c.  At f': only i <= 0 (lambda_i >= 1), eta = lambda_i x^fr_i free (frozen representation
g' = rho c v + K sum_i x^fr_i lambda_i sigma_i, sum x^fr_i = rho c).  Scaling: sup_tau P is 2-homogeneous in S, so the
relevant number is the boundary ratio R(J) = min over frozen data on J coordinates of sup_tau P_{f'} / sup_tau P_f.
Results (r = 1/2, M = 1/2; four (A,B) pairs, all consistent):
  J = 1: R ~ 2.00;  J = 2: R ~ 1.27;  J = 3: R ~ 1.08;  J = 5: R ~ 1.007 (Nelder-Mead);
  geometric ansatz x^fr_i proportional to 0.6^{-i} on the J finest available coordinates (finest gets most):
  J = 8: R = 1.0008;  J = 12: R = 1.0000 (to 4 digits), scale window tau in [2^-12, 2^30].
Conclusion (HEURISTIC for Martin's norm, NUMERICAL in Model M): the boundary layer created by truncating the
fine cross coordinates can be made to cost an arbitrarily small factor by spreading the frozen representation
geometrically over many available coordinates. Hence for every rho < 1 the truncated structure recovers rho g.
Mechanism that kills the candidate: MULTI-SCALE FROZEN REPRESENTATION (a geometric "partition of unity in scale"
for the block coefficients, finest coordinate heaviest). Scripts: E_work/modelM.py, modelM_opt.py, modelM_opt2.py.

## 1.4 Other natural candidates already dead (SKETCH arguments)

(i) Two-piece mates over an infinite contact set K (A_notes Remark 7.6): g = y_+ + b_F = -y_- + b_F + L*W with
    y_+- z-signed on K. Killed by the eta-trick at the contacts K cap [1, N'] (contacts of f, so z'_j = z_j = +-1 is
    compatible with (F1)) combined with truncation of the far part: base two-sided for |t| <= eta, one-sided linear
    decompositions transferred for |t| in [tau'/c, T_0] with tau' = ||y|_{>N'}||_1 << eta.
(ii) Cross mates through ONE-SIDED carriers (near-threshold peaks of both signs, P+ for t<0, P- for t>0): a single
    frozen coordinate is one-sided, so 1.3 fails as stated; killed instead by CONVERSION of a near-threshold peak k* into
    an off-peak coordinate at f' (shift u_{k*}(x') by ~theta Phi(k*) through the far tail of u_{k*}, or by an ABSOLUTE
    shift of all v-carriers through v(x') / Delta a), after which 1.3 applies. [Correction, see part 8: individual
    conversions through WINDOW coordinates are NOT available along NA approximants, since window moves must be o(1)
    (Prop 8.2); only far tails and absolute shifts remain.] Whether enough conversions are always available is the
    subject of parts 4 and 7; in the error-dominated regime this is OPEN.
