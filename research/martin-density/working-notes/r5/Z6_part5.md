# Z6 part 5: forced switching, rigidity of mates on swallowed sets, the dangerous candidate (task (a))

## 5.1 Lemma F (forced switching = oscillation)   [PROVED]
Let l be swallowed (z = eps_l on S_l \ F) and A subset S_l \ F a set on which no carrier vector other than u_l is nonzero
(e.g. the part of S_l not met by targets of carriers whose coefficients are not controlled).  Put rho(s) := eps_l g(s)/v_l(s)
(s in A).  For every two-sided decomposition at scale t, with tau_l = -eps_l Delta theta_l,
  tau_l >= sup_{s,s' in A} [ rho(s) - rho(s') - (t/(4 q_0)) (1/v_l(s) + 1/v_l(s')) ],
and, with theta_{pm,l} := lambda_l Theta_{pm,m(l)}(k(l)),
  eps_l theta_{-,l} >= rho(s) - t/(4 q_0 v_l(s)),   eps_l theta_{+,l} <= rho(s') + t/(4 q_0 v_l(s'))   (s, s' in A).
Proof. On A, B_pm(s) = g(s) - theta_{pm,l} v_l(s).  With z = eps on A, phi_z(x) = 2(eps x)_- and phi_{-z}(x) = 2(eps x)_+
(Lemma phicalc(a)); the per-side budgets (Lemma switchbudget) give sum_A v_l(s) (eps theta_+ - rho(s))_+ <= t/(4q_0) and
sum_A v_l(s) (rho(s) - eps theta_-)_+ <= t/(4q_0).  Read each at one coordinate and subtract.  QED

## 5.2 Corollaries (rigidity of mates on swallowed sets)   [PROVED]
(a) Box.  Since |theta_{pm,l}| <= 3 lambda_l/t (Lemma box), for every s in A and every t > 0,
    |rho(s)| <= 3 lambda_l/t + t/(4 q_0 v_l(s)); at t = sqrt(12 q_0 lambda_l v_l(s)) this gives |rho(s)| <= sqrt(3 lambda_l/(q_0 v_l(s))),
    i.e. |g(s)| <= sqrt(3 lambda_l v_l(s)/q_0).  Mates are tiny on private parts of swallowed signature sets.
(b) Proportionality under transience.  If liminf_{t -> 0} tau_l(t) = 0 along some choice of decompositions (e.g. l is an
    uncompensated d-coupled carrier, Proposition 3.4, or a non-degenerate peak, |tau_l| <= t/mu_l + lambda_l K_d t), then rho is
    constant on A: g|_A = theta*_l v_l|_A, and theta*_l = lim eps theta_{pm,l}(t) (both sides converge to the same value).
    Proof: Lemma F with t -> 0 along the sequence.
(c) Peaks.  If k = k(l) is a non-degenerate peak, then lambda_l |omega_pm(k)| <= t/(2 mu_l) (Lemma suplevel(c) and
    sigma|alpha(k)| = lambda_l mu_l), so theta_{pm,l} = -lambda_l varsigma_k M_m d_pm(t) + O(t/mu_l).  Hence along any
    sequence t -> 0 with d_pm(t) -> d* (both sides have the same limit since Delta d = O(t) when pinned), rho is constant
    on A with eps theta*_l = -eps lambda_l varsigma_k M_m d*: on private parts of swallowed peak signature sets the mate is
    the trace of the uniform shift -d* R_m^* w_m (in particular g|_A = 0 iff d* = 0).
(d) Component size.  Under (b), |theta*_l| <= sqrt(3 lambda_l/(q_0 max_A v_l)) (from (a)).

Reading.  Persistent switching through a swallowed carrier is FORCED exactly by the non-proportionality of g to the
signature on its private part; transient carriers (uncompensated d-coupled, non-degenerate peaks) force proportionality.

## 5.3 The dangerous candidate (task (a))  [construction: SKETCH; properties: as labelled]
Data.  SLD operator, one block (N = 1 suffices), F = {j_0}, a = e*_{j_0}/q*(e*_{j_0}), and z := 1 on N \ F (MAXIMAL CONTACT).
Then K = N \ F, every signature set is exactly swallowed with eps_l = 1, every carrier is bad, and the block data are
determined by the numbers u_l(zhat), zhat = z + U e (e = U*a/||U*a||), relative to the thresholds theta-hat Phi(k).
Required features (each is a codimension condition on a, or on a and further coordinates of F; existence of a with
infinitely many of them by a Baire/IVT nested construction over the dense target sequence: SKETCH):
 (C1) peaks of both signs (automatic by density), so every exact two-piece datum is d-neutral (Proposition 3.3);
 (C2) infinitely many weak peaks: mu_{l_i} <= 2^{-2^{l_i^4}}  (so (MR) fails and no window constant controls them);
 (C3) infinitely many resonant strict non-peaks (y_l >= 0 off F, y_l(j_0) < 0 balancing u_l(zhat) ~ 0), all with
      u_l(xi) > 0 (q_l > 0: NO compensators), half of them near-threshold (gap -> 0), half nearly neutral (0 < q_l << Phi_l);
 (C4) slaving: targets of later carriers meet earlier signature sets ((H1) fails), as forced by density of targets.
Position w.r.t. proved classes [PROVED given (C1)-(C4)]: f not in R_0^pm (all r_l = 0); not in R_S (B infinite, contains
non-d-neutral peaks: (B_fin), (B_res) fail); not (BT) ((C2) violates (MS), (C3) gives infinitely many Q); not in R_C
((H1) fails, no compensators, (MR) fails).  Corollary BTrecovered, Theorems Bpm, S, C do not apply.
Mates.  By 5.2(b),(c), every mate is proportional on private parts of all non-compensated carriers and vanishes there for
non-degenerate peaks; switching through (C3)-carriers is transient (3.4) and confined (Lemma F) to bands
 t in [ q_l theta*_l / C , C theta*_l^2 ||v_l|| ... ] around their own weight, of length ~ log(1/q_l) dyadic scales,
and through (C2)-peaks it is capped by t/mu_l.  The model mate is a module sum
 g = sum_l theta*_l (u_l - q_l R^* w) + (base part on F),  |theta*_l| <= sqrt(3 lambda_l/(q_0 v_l(s_0(l)))),
each module being a balanced certificate direction with radius ~ gap_l lambda_l/theta*_l, valid at all scales when
theta*_l^2 <= c gap_l lambda_l/q_l (two-sided below the radius, base/carrier switching above): HEURISTIC verification.
Non-window-pinning [PROVED for the upper-bound structure, HEURISTIC for actual mates]: at window W(l), switching through
carrier l of size theta*_l >> K t on ~log(1/q_l) scales, with K ~ 1/q_l >> n^w_l (SLD) for nearly neutral carriers; weak
peaks add t/mu_l.

## 5.4 Recovery attempts on the candidate
(i) Window method at f: FAILS (constants 1/q_l, 1/mu_l, slaving products exceed n^w_l).  [PROVED as stated: 3.4 is sharp
    up to constants for single modules — see numerics part 6.]
(ii) Theorem S/C projection: the exact cone is {0} on q > 0 carriers (Prop 3.3 + no compensators); projection error = all
    their switching: FAILS for the same reason.
(iii) Certificate approximability (averaging over certificates, Section 4 of the note): if g = sum of modules exactly, then
    c_t := truncation to modules with radius >= c_0 t has ||g - g_{c_t}|| <= sum of dropped |theta*| <= K(t) t with
    K(t) ~ 1/(gap_{L(t)} delta°_{L(t)}) by 5.2(d); this is window-compatible for gaps bounded below, so module sums with
    gaps bounded below are recovered (Theorem windowed applied to certificates): SKETCH.  Near-threshold modules with
    gap -> 0 faster than the windows break this bound; for them the inward usage (part 4.2, q > 0) is available on the
    side data but exact data need d-compensation (3.3): the only remaining quantitative property is
 (UERP) uniform exact-resonance projection: at window scales t in W(l_*), the switching of some two-sided decomposition is
    within K(l_*) t (l_1-weighted by ||u_l||) of an EXACT d-neutral resonance (z-signed on K, finitely supported, data
    admissible incl. inward coordinates), with K(l_*) = o(n^w_{l_*}) along a subsequence.
    For the candidate, (UERP) holds iff the transient switching through (C2),(C3) carriers inside the windows is
    o(n^w) t, which by 3.4 and 5.2 reduces to: q_l, mu_l, gap_l of the coarse carriers at the window not smaller than
    1/(n^w_{l_*} poly) ... i.e. f-dependent rates, which the adversary (C2),(C3) violates.  OPEN whether the candidate's
    mates are recovered by other approximants; nothing indicates non-recovery: each single module IS recovered.
(iv) Far lowering f^L: fine modules (l > L) are dropped at cost sum_{l>L} theta*_l (norm, small); coarse modules keep their
    structure at f^L, and f^L has finitely many weak peaks/non-peaks below level L that matter... but f^L still has
    infinitely many swallowed coarse... no: at f^L only l <= L are swallowed (finitely many bad carriers), so f^L in R_S if
    (H2),(H3) hold — they do ((H2) automatic for B finite, (H3): no degenerate peaks).  So f^L in Rec, and the question is
    dist(rho g, C(f^L)) -> 0.  For module sums this holds if the truncated module sum is a mate of f^L: SKETCH (each
    coarse module's validity uses only coarse data, which f^L keeps; the fine signature sets acquire room, which only removes
    the fine modules' switching, which we dropped).  This is the most promising route for the candidate.
