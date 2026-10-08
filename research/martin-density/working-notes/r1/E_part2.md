# E notes, part 2: the averaging (multi-frozen) principle, one-sided resources, conversion

## 2.1 Averaging Lemma (SKETCH; the abstract skeleton is PROVED, the hypotheses are the issue)

Skeleton (PROVED, elementary convexity). Let f' in S_{p*}, rho in (0,1), gbar in X*, and let h_1,...,h_J in X*,
weights w_j >= 0 summing to 1, scales 0 < s_1 < ... < s_J, constants kappa, Q >= 0 such that
 (i)  p*(f' + t h_j) <= 1 + Q t^2/2                for |t| <= s_j        (h_j is a two-sided local certificate);
 (ii) p*(f' + t gbar) <= 1 + Q t^2/2               for s_1 <= |t| <= T_0  (transfer regime);
 (iii) p*(h_j - gbar) <= kappa s_j                 (frozen error is of the order of its scale).
Then g' := sum_j w_j h_j satisfies, for every |t| <= T_0,
   p*(f' + t g') <= 1 + Q t^2/2 + kappa |t| sum_{j : s_j < |t|} w_j s_j ,
and for |t| <= s_1 simply p*(f' + t g') <= 1 + Q t^2/2.
Proof: p*(f' + t g') <= sum_j w_j p*(f' + t h_j) (convexity, sum w_j = 1). For j with s_j >= |t| use (i). For
j with s_j < |t| (so |t| >= s_1) use p*(f' + t h_j) <= p*(f' + t gbar) + |t| p*(h_j - gbar) and (ii), (iii). QED.
With w_j = 1/J and geometric s_j = s_1 2^{j-1}: kappa |t| sum_{s_j<|t|} s_j/J <= 2 kappa t^2/J.
So if Q <= rho^2 (+o(1)) and J >= 4 kappa/(1-rho^2), then p*(f' + t g') <= 1 + t^2/2 <= s(t) on |t| <= T_0 (up to the
standard quartic correction), and the slack (A_notes Lemma 4.7) handles |t| >= T_0 once ||g' - rho g|| and
||f' - f|| are small. ||g' - gbar|| <= kappa sum_j w_j s_j <= 2 kappa s_J / J.

This is exactly what Model M (part 1) found numerically: the boundary excess decays like 1/J.

What has to be supplied in Martin's setting (the hypotheses):
 (H-transfer) gbar ~ rho g satisfies (ii) at f' on [s_1, T_0]: needs the structure of f at scales >= s_1 to be
   matched at f' (finitely many block coordinates, window choice; A_notes 8.1, (F1)) and the contribution of the
   UNMATCHED fine coordinates (scales <= lambda_0) at scale t to be O(delta) with delta = lambda_0/s_1 (geometric
   Phi): choose s_1 = lambda_0 * C/(1-rho^2). HEURISTIC (bookkeeping of first-order Hilbert mismatch not written).
 (H-cert) two-sided certificates h_j at the scales s_j with p*(h_j - rho g) = O(s_j): REQUIRES TWO-SIDED RESOURCES
   at f' near the scales s_j. This is the crux.

## 2.2 Why two-sided resources are indispensable at NA points (PROVED, from A_notes Prop 7.4)

At an NA point f' (a' in c_00, z' in c_0, contact set K' finite), suppose h = B+ + L*Om+ = B- + L*Om- where
(B+, Om+) is admissible for 0 < t <= r and (B-, Om-) for -r <= t < 0, both with zero first-order base excess
(B+- supported in supp a' cup K', with the contact signs). Then B+ - B- in c_00 cap Y = {0}, so B+ = B-, Om+ = Om-.
Consequently, if Om+ is supported on peaks of w'_m used "downwards" for t>0 and Om- on peaks used downwards
for t<0 (disjoint sets), both vanish. So one-sided block resources (peaks, near-peak off-peak coordinates used in
their long direction) can NEVER be combined into a two-sided linear certificate at an NA point: the frozen
certificate must use genuinely two-sided resources (off-peak coordinates within their symmetric room, supp a').

## 2.3 The refined candidate: one-sided resources of both signs at all scales

f carries the v-component of g at every scale by near-threshold PEAKS: P+ (w = +M, serve t<0, carry positive
multiples of u_k) and P- (w = -M, serve t>0), at all scales, with good approximation rates u_k ~ v, and NO
off-peak coordinate approximating v. At NA approximants: matched down to lambda_0, destroyed below (deep -M
peaks if the far tails see z = 1/2 on far blocks). By 2.2, the frozen certificate needs two-sided resources.

## 2.4 How it dies (SKETCH): conversion bands through the scalar v(x')

v = (e_j* - xhat_j a)/norm has v(xhat) = 0 and is c_00. The scalar v(x') is freely adjustable at f' by tiny window
moves (delta_j at the non-contact coordinate j) or by Delta a (U*v has a component orthogonal to e by injectivity of
U*). Writing u_k = (v + K lambda_k sigma_k)/n_k, the relative position of k is
   rho_k(x') = v(x')/(K lambda_k) + sigma_k(x'),   off-peak iff |rho_k| < theta~ (threshold, rescaled).
If the near-threshold P+ resources have sigma_k(xhat) = theta~(1+delta), the shift v(x') = -K Lambda_0 theta~(1+delta)
gives rho_k = theta~(1+delta)(1 - Lambda_0/lambda_k), so ALL P+ resources with
lambda_k in ( Lambda_0 (1+delta)/(2+delta), Lambda_0 (1+delta)/delta ) (a band of scale ratio (2+delta)/delta) become
OFF-PEAK (two-sided), with full gap at lambda_k = Lambda_0, while P- become deeper peaks and everything far below
Lambda_0 becomes a deep peak.
One scalar therefore creates a whole BAND of two-sided resources, which is what 2.1 needs. Cost: ||Delta f'|| =
O(K Lambda_0) (only coordinates at scales <~ Lambda_0 change status). The coarse structure is shifted by relative
amounts K Lambda_0/lambda_k, negligible above the band.
Caveat (open in this part): inside the band the t<0 room of the converted P+ resources drops from 2M (one-sided)
to M (symmetric), so the band's own cost profile is worse than f's by a constant factor; for small delta the band
is wide. Whether the averaging still closes is tested numerically in part 4 (Model N).
