# Y2 part 6: failure of (H2'') -- pinning the uniform shift by its base cost (item (h))

Framework: Z4 Theorem A'' (Steps 1-3), any SLD-type design; F finite; t in W(l_*), a two-sided decomposition of g at scale t,
Delta d_m := d_{+,m} - d_{-,m}, varsigma_k := sgn w_m(k), mu_k margins, e_k := |omega_{+,m}(k)| + |omega_{-,m}(k)| at peaks.
The Z4 referee (finding 3, Remark 3.3) showed that (H2'') fails exactly when some block (i) has all its peaks swallowed with swallowing
sign and a swallowed q < 0 strict non-peak (UPPER fails), or (ii) has all its non-degenerate peaks swallowed with anti sign and a
swallowed carrier with q > 0 (LOWER fails).  Below, I_up (resp. I_lo) denotes the set of blocks in which the upper (resp. lower) half of
(H2'') fails; in the other blocks the corresponding half holds and gives the bound of Z4 Step 3 / Lemmas 3.1-3.2 of the Z4 referee.

## 6.1 The peak trace of the shift
**Lemma 6.1 (peak trace).  PROVED.**  For every peak k = k(l) of block m (good or swallowed, any sign),
   -Delta theta_l = varsigma_k lambda_l (Delta d_m M_m + e_k),   0 <= e_k, and e_k <= t/(lambda_l mu_k) if mu_k > 0.
Hence, on F^c,
   Delta B 1_{F^c} = sum_m Delta d_m M_m Pi_m + E + sum_{l notin P*} (-Delta theta_l) u_l 1_{F^c},
   Pi_m := sum_{l in P*_m} varsigma_{k(l)} lambda_l u_l 1_{F^c},   E := sum_{l in P*} varsigma_{k(l)} lambda_l e_{k(l)} u_l 1_{F^c},
for any set P* = union_m P*_m of coarse (<= l_*) peak carriers with positive margins; ||E||_1 <= t sum_{l in P*} 1/mu_{k(l)}.
*Proof.* eq:peakshift: e_k = -varsigma_k Delta Theta_m(k) - Delta d_m M_m >= 0 with Delta Theta_m(k) = Delta theta_l/lambda_l; and
lambda_l mu_k e_k = sigma_m |alpha_m(k)| e_k <= t (Lemma lem:suplevel(c), eq:margin).  The display is eq:DeltaB split along P*,
with ||u_l||_1 <= 1.  QED
So a uniform shift Delta d_m appears in the base switching as the vector Delta d_m M_m Pi_m: the shift of a block is carried by ALL its peaks
at once.  At a good peak this is pinned (Lemma badpeaks(a)); at swallowed peaks it is zero-cost on their own signature sets exactly when
varsigma eps_l (Delta d_m) >= 0, i.e. for Delta d > 0 at swallowing-type peaks and Delta d < 0 at anti-sign peaks -- which is why
configuration (i) leaves Delta d free upward and (ii) downward.

## 6.2 The shift cost
For a level l, a margin threshold mu_0 > 0 and the corresponding sets P*_m(l) := {coarse non-degenerate peak carriers of block m,
<= l, mu >= mu_0} (m in I_up ∪ I_lo), let Bfree(l) := all swallowed carriers <= l except those in P*(l).  For delta in R^{I_up ∪ I_lo} put
   c(delta; l) := inf_{x in R_+^{Bfree(l)}} sum_{j notin F} phi_{z_j}( sum_m delta_m Pi_m(j) + sum_{l' in Bfree(l)} x_{l'} eps_{l'} u_{l'}(j) )
(the series converges since sum_l lambda_l ||u_l||_1 < infinity and x ranges over a finite-dimensional cone; c(.; l) is the partial
infimum of a jointly convex, positively homogeneous, finite function, hence convex, positively homogeneous, finite and continuous), and
   c_*(l) := inf{ c(delta; l) : ||delta||_1 = 1, delta_m >= 0 (m in I_up \ I_lo), delta_m <= 0 (m in I_lo \ I_up) }.
c(.; l) is convex and positively homogeneous, so c(delta; l) >= c_*(l) ||delta||_1 on the sign cone.

**Proposition 6.2 (shift-cost pinning).  PROVED.**  With K_g t the good pinning bound (Lambda_g, Lemma lem:modswallow(a) / Z4 Step 1)
and K_- t := sum_{l in B, l <= l_*} (tau_l)_- (<= C_f K_g D(l_*) t by the bad inequalities, Z6 referee 3.4 step (2)), put
delta_m := (Delta d_m)_+ M_m (m in I_up \ I_lo), -(Delta d_m)_- M_m (m in I_lo \ I_up), Delta d_m M_m (m in I_up ∩ I_lo).  Then
   c_*(l_*) ||delta||_1 <= t/q_0 + 2[ K_g t + 6t^2 + K_- t + t l_*/mu_0 + K_d^{half} t ],
where K_d^{half} t bounds the pinned halves ((Delta d_m)_- M_m for m in I_up \ I_lo, (Delta d_m)_+ M_m for m in I_lo \ I_up; Z4 Step 3 and
Lemmas 3.1, 3.2 of the Z4 referee give K_d^{half} <= C' K_1).  In particular, if c_*(l_*) > 0 then |Delta d_m| M_m <= K_sh t for all m in
I_up ∪ I_lo, with K_sh := C_f (K_g + K_- + l_*/mu_0 + K_1 + 1)/c_*(l_*).
*Proof.* Lemma lem:switchbudget: sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0.  In Lemma 6.1 take P* := P*(l_*) (peaks of the blocks of
I_up ∪ I_lo only).  The remaining terms of Delta B 1_{F^c}: good carriers (||.||_1 <= K_g t), fine carriers (<= 6t^2), swallowed carriers
<= l_* outside P* (this includes all swallowed peaks of the other blocks and the degenerate or weak peaks of the blocks of I_up ∪ I_lo):
-Delta theta_l u_l = eps_l tau_l u_l = eps_l (tau_l)_+ u_l - eps_l (tau_l)_- u_l.  Hence Delta B 1_{F^c} = sum_m delta_m Pi_m +
sum_{l in Bfree} x_l eps_l u_l + R with x_l := (tau_l)_+ >= 0 and ||R||_1 <= ||E||_1 + K_g t + 6t^2 + K_- t + K_d^{half} t max_m ||Pi_m||_1
(||Pi_m||_1 <= sum_l lambda_l <= 1/3).  By Lemma lem:phicalc(c), t/q_0 >= sum_j phi_{z_j}(sum delta Pi + sum x eps u) - 2||R||_1 >=
c(delta; l_*) - 2||R||_1 >= c_*(l_*) ||delta||_1 - 2||R||_1, and ||E||_1 <= t |P*(l_*)|/mu_0 <= t l_*/mu_0 (Lemma 6.1).  QED

**Theorem H.  PROVED (by modification of Z4 Theorem A'' and of Theorems P, M).**  Design D^Y.  In Theorem M (and in Theorem P)
hypothesis (H2'') may be replaced by: there is mu_0 > 0 such that c_*(l) > 0 for all large l, and
   (W_H)  liminf_l (1 + K_F^rel(l))^2 (1 + K_sh^rel(l))^2 Xi_f(l)/(l 2^{l^3})^6 = 0,   K_sh^rel(l) := 1/(c_*(l) D(l))
(K_sh^rel := 0 if (H2'') holds in every block).  Blocks satisfying (H2'') need no shift cost.
*Proof.* (H2'') enters Z4 only in Step 3, through |Delta d_m| M_m <= K_d t with K_d = C_1 K_1; Proposition 6.2 provides this bound with
K_sh = C_f (K_g + K_- + l_*/mu_0 + K_1 + 1)/c_*(l_*) <= C_f (1 + l_*/mu_0) K_1 D(l_*) K_sh^rel(l_*) (K_- <= (1/q_0 + 2)K_1 + 6 l_*, from the
projection tau° >= 0 of Z4 Step 3 and the box bound for inactive carriers; K_g <= K* <= K_1).  All later constants of Z4 and of Theorem M
are linear in K_d, so C_dia' acquires the factor C(1 + l/mu_0) D (1 + K_sh^rel); the window arithmetic of the proof of Theorem M then holds
along the levels given by (W_H): D^Y provides D^8 and the factor (1 + l/mu_0)^2 <= C l^2 <= C Lambda°(l) is absorbed by the surplus
Lambda°^4 of n^w_l.  QED

## 6.3 When is the shift cost positive?  What remains of (h)
(a) PROVED (gap pinning, configuration (i)).  For a swallowed q < 0 strict non-peak l of block m (eps_l = -varsigma_k), the box
inequalities of Lemma lem:suplevel(f) on both sides give tau_l/lambda_l + Delta d_m M_m <= 2 gap_m(k(l))/t, hence
   Delta d_m M_m <= 2 gap_m(k(l))/t + (tau_l)_-/lambda_l:
q < 0 carriers whose gaps are <= K t^2 at the window scales pin the shift from above (near-threshold q < 0 carriers, harmful when kept,
are useful here).  [Derivation: varsigma(omega_+ - omega_-)(k) = tau_l/lambda_l + Delta d |w(k)| and varsigma omega_+ <= (1 - d_+ t)gap/t,
-varsigma omega_- <= (1 + d_- t)gap/t; use |w(k)| + gap = M.]
(b) c_*(l) = 0 iff some nonzero delta in the sign cone and some x >= 0 make sum_m delta_m Pi_m + sum x_l eps_l u_l zero-cost on F^c:
the uniform-shift trace on the coarse peaks, corrected by swallowed switchings, is an EXACT zero-cost resonance.  On the peaks' own
signature sets this is automatic in configurations (i)/(ii) (6.1); what must happen in addition is exact sign compatibility (contacts) and
exact cancellation (free coordinates) on the TARGET coordinates of the peaks, including the slaving coordinates where later targets meet
earlier (good) signature sets.  Sufficient condition (PROVED): for every m in I_up ∪ I_lo there is a coordinate j_m notin F with
|z_{j_m}| < 1, Pi_m(j_m) != 0, Pi_{m'}(j_m) = 0 for m' != m, and u_{l'}(j_m) = 0 for every l' in Bfree(l) (a peak target at a free
coordinate that no swallowed carrier reaches).  Indeed then, for ||delta||_1 = 1, the j_m-term of the cost equals
phi_{z_{j_m}}(delta_m Pi_m(j_m)) >= (1 - |z_{j_m}|)|Pi_m(j_m)||delta_m| whatever x is, so c_*(l) >= min_m (1 - |z_{j_m}|)|Pi_m(j_m)|/|I_up ∪ I_lo|
(using ||delta||_1 = 1 and max_m |delta_m| >= 1/|I_up ∪ I_lo|).
(c) REMAINING STEP (OPEN): configurations (i)/(ii) with c_*(l) = 0 or c_*(l) decaying faster than the ladder ("coherent shift
resonance").  There the shift may be O(1) (not O(t)) for some decompositions, and the exact d-neutral window data of Z4 cannot follow it.
Exact data with Delta d != 0 would be needed; Corollary cor:D1 accepts Delta d >= 0 (configuration (ii): decomposition Delta d < 0
corresponds to data Delta d > 0), but by the Z4 referee's Proposition 5.6' such data exist only if all but finitely many non-d-neutral
carriers of the block are swallowed with the coherent sign, AND (new observation, PROVED by the computation of 6.1) the full vector
-Delta d R_m^* w_m must be z-signed on K and vanish at free coordinates, which in addition requires the coherent-resonance property of
(b) for ALL peaks (fine ones included) and for all non-peaks with w != 0.  Whether mates in the coherent case are recovered is open.
