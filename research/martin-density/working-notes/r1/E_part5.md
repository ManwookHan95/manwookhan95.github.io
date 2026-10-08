# E notes, part 5: the Averaging Criterion for cl Cert(f) (PROVED, given A_notes Prop 4.5 and Lemma 4.7)

Notation from A_notes §4: finite certificate c = (b, omega) at f (Def 4.1), direction g_c, coefficient H(c),
radius r(c), cubic constant kappa(c); Cert(f) = {g_c : H(c) <= 1, g_c in C(f)}.
Imported (PROVED in A_notes, I re-checked the statements):
 (P4.5) for |sigma| <= r(c): p*(f + sigma g_c) <= 1 + (sigma^2/2) H(c) (1 + kappa(c)|sigma|);
 (L4.2) c -> g_c linear; H convex and 2-homogeneous; finite certificates form a vector space;
 (L4.7) s(t) - s(rho t) >= (1 - rho^2) min(t^2, |t|)/3, s(t) = sqrt(1+t^2);
 (C4.11) every g in cl Cert(f) is recovered along EVERY sequence f_n -> f in S_{p*} (transport theorem).

## Theorem 5.1 (Averaging Criterion). PROVED (mod. P4.5, L4.2, L4.7, C4.11)

Let f in S_{p*}, g in C(f). Assume there are K_0, kappa_0 >= 0, s_0 > 0 and, for every s in (0, s_0], a finite
certificate c_s at f with
  (a) H(c_s) <= 1,  (b) r(c_s) >= s,  (c) kappa(c_s) <= kappa_0,  (d) p*(g_{c_s} - g) <= K_0 s.
Then g in cl Cert(f); hence (f, g) is in cl NA((X,p), l_2^2), and g is recovered along every sequence f_n -> f.

Proof. Fix rho in (0,1), put e1 := (1 - rho^2)/8. Choose J in N with 2 rho K_0 / J <= e1, and t_* in (0, 1] with
rho^2 kappa_0 t_*/2 <= e1 and t_*^2/8 <= e1. Choose s_J in (0, s_0] (fixed below), s_j := s_J 2^{j-J} (j = 1..J),
h_j := rho g_{c_{s_j}}, and g' := (1/J) sum_j h_j = g_{c'}, c' := (rho/J) sum_j c_{s_j} (a finite certificate, L4.2).
H(c') <= (1/J) sum_j H(rho c_{s_j}) = rho^2 (1/J) sum_j H(c_{s_j}) <= rho^2 (convexity, homogeneity).
Step 1 (|t| <= t_*). By convexity of p*, p*(f + t g') <= (1/J) sum_j p*(f + t h_j).
 - If s_j >= |t|: |rho t| <= s_j <= r(c_{s_j}), so by P4.5
     p*(f + t h_j) <= 1 + (rho^2 t^2/2)(1 + kappa_0 |t|).
 - If s_j < |t|: p*(f + t h_j) <= p*(f + t rho g) + |t| rho p*(g_{c_{s_j}} - g) <= s(rho t) + rho K_0 |t| s_j,
   and s(rho t) <= 1 + rho^2 t^2/2.
 Since sum_{j : s_j < |t|} s_j < 2|t| (geometric), averaging gives
   p*(f + t g') <= 1 + (rho^2 t^2/2)(1 + kappa_0|t|) + 2 rho K_0 t^2/J <= 1 + t^2 (rho^2/2 + 2 e1)
              = 1 + t^2 (1/2 - 2 e1) <= 1 + t^2/2 - t^4/8 <= s(t),
 using rho^2/2 = 1/2 - 4 e1, the choices of J and t_*, and sqrt(1+x) >= 1 + x/2 - x^2/8 (x >= 0).
Step 2 (|t| >= t_*). p*(f + t g') <= p*(f + t rho g) + |t| p*(g' - rho g) <= s(rho t) + |t| rho K_0 (1/J) sum_j s_j
   <= s(rho t) + 2 |t| rho K_0 s_J / J. By L4.7, s(t) - s(rho t) >= (1-rho^2)|t| t_*/3 for |t| >= t_* (t_* <= 1).
   So p*(f + t g') <= s(t) once s_J <= (1-rho^2) t_* J/(6 rho K_0) (any s_J if K_0 = 0).
Step 3. g' in C(f) and H(c') <= 1, so g' in Cert(f), and p*(g' - rho g) <= 2 rho K_0 s_J/J -> 0 as s_J -> 0.
 Hence rho g in cl Cert(f) for every rho < 1; cl Cert(f) is closed, so g in cl Cert(f). The last assertions are C4.11
 and A_notes Cor 3.3. QED

Remarks.
 * Compared with the (CA) test of A_notes Remark 4.9 (one certificate per rho with error <= (1-rho^2) r_*/6, i.e. a
   SMALL constant times the radius), Theorem 5.1 accepts ANY constant K_0, provided certificates exist at all small
   scales. The averaging over J dyadic scales divides the boundary error by J. This is the rigorous form, at f itself,
   of the Model M phenomenon (part 1).
 * Only convexity of p* and the certificate expansion are used; no NA engineering is needed: transport does the rest.

## Corollary 5.2 (critical two-sided cross mates). PROVED (mod. the same imports)

Fix a block m and v in X*, v != 0, write vhat := v/q*(v). Suppose there are off-peak coordinates k_1, k_2, ... of
w_m (at f) with lambda_i := lambda_{k_i,m} -> 0, lambda_{i+1} >= theta_0 lambda_i (theta_0 in (0,1)), gaps
gap_m(k_i) >= gamma > 0, and ||u_{k_i,m} - vhat||_1 <= K lambda_i (a CRITICAL rate: any constant K). Let c > 0 with
c^2 q*(v)^2/(m^2 C_m) <= 1 and suppose g := c v + g_0 in C(f), where g_0 = g_{c_0} for a fixed finite certificate c_0
whose block part is supported away from {k_i} and whose radius is positive, with H(c_0 + single-coordinate part) <= 1
(e.g. g_0 = 0). Then g in cl Cert(f).
Proof with all estimates: for small s let i = i(s) be the LARGEST index with lambda_i >= 2 c q*(v) s/gamma, so that
lambda_i < 2 c q*(v) s/(gamma theta_0) (geometric density). Put omega_s := (c q*(v)/lambda_i) e_{k_i}
(so R_m* omega_s = lambda_i omega_s(k_i) u_{k_i,m} = c q*(v) u_{k_i,m}); then
 r((0,omega_s)) >= min(gamma lambda_i/(2 c q*(v)), 1/(2|d_s|), C_m/(2|d_s| M_m)) >= s for s small, since
 |d_s| = Phi_m(k_i)|w_m(k_i)| c q*(v)/(m C_m) = O(lambda_i) -> 0;
 H = ||P-perp D omega_s||^2/C_m <= (c q*(v)/m)^2/C_m <= 1 (Phi = lambda/m);
 kappa = 2|d_s| M/C bounded;
 g_{(0,omega_s)} - c v = c q*(v)(u_{k_i,m} - vhat) - d_s R_m* w_m, of norm <= c q*(v) K lambda_i + |d_s| q*(R_m* w_m)
   = O(lambda_i) = O(s) because lambda_i < 2 c q*(v) s/(gamma theta_0).
Adding c_0 (fixed, positive radius) keeps (a)-(d) for s small (H of the sum: the two block parts are supported on
disjoint coordinates; the hypothesis on c_0 is used here). Apply Theorem 5.1. QED (the case g_0 != 0 is a SKETCH:
H of a sum of certificates with disjoint supports is not additive in general because of the projection P-perp;
for g_0 = 0 the proof is complete).

Consequences.
 * The "intermediate / critical regime" of D_notes 12.6 and A_notes 7.3 is NOT an obstruction when the carrying
   coordinates are off-peak (two-sided) at f: such mates lie in cl Cert(f) and are recovered along every sequence.
 * A_notes §7.4 (box tails of exact order sigma) is settled in the same way: truncations omega 1_{[1,N(s)]} at the
   level where the box holds at scale s are finite certificates with radius ~ s and error T(s) = O(s) (SKETCH: the
   uniform bound on kappa and H for the truncations is as in A_notes Theorem 6.2).
 * Hence a counterexample must use ONE-SIDED resources at f at a cofinal set of scales (peaks or near-peak
   coordinates used in their long direction, or one-sided base contacts), i.e. resources that are not certificates.
   For base contacts, T4 (part 3) applies; for block peaks, conversion at f' is needed (parts 2, 4).
