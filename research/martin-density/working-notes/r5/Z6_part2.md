# Z6 part 2: anatomy of the remaining switching (mostly HEURISTIC, used to aim the proofs)

2.1 (PROVED, algebra) Balance is forced per piece. If (b^+,omega^+) and (b^-,omega^-) represent the same g and each side is
 balanced (<Theta_m^pm, zeta_m> = 0 and b^pm(xi)=0, which is forced at first order: on side + every piece must have first-order
 term <= 0 and they sum to g(xi)=0), then b^+ - b^- = sum_m R_m^*((omega^-_m - omega^+_m) - Delta d_m w_m). Hence any d-mismatch
 puts -Delta d_m R_m^* w_m into the switching vector v; at maximal contact (z = 1 off F) and with strong peaks of both signs in
 block m, R_m^* w_m is not z-signed on F^c, so EXACT two-piece data need Delta d_m = 0 there.

2.2 (PROVED, computation) A degenerate peak k (alpha(k)=0) used inward on each side (varsigma_k omega^+(k) <= 0 <= varsigma_k
 omega^-(k)) has exactly the second-order block expansion of a strict non-peak (Lemma block (a),(b) with ||W||_inf=(1-d tau)M),
 and contributes Delta d = (Phi_k^2 M/C)(|omega^+(k)|+|omega^-(k)|) >= 0. So one-sided usage of degenerate peaks is an EXACT
 resource whose d-mismatch is always nonnegative; by 2.1 it must be compensated by carriers with negative d-contribution.

2.3 (HEURISTIC) Scale bands. With the d-constraint |sum_l q_l tau_l| = O(t) (q_l ~ lambda_l w(k_l)/(m^2 C)) and the box bound
 |tau_l| <= 6 lambda_l/t, a carrier whose q_l has the sign of all other switchable carriers can switch O(1) only for
 t ~ lambda_l (bounded log-band). Since the SLD weights are super-separated, at most one such carrier is active at a time, and
 it sits inside its own window W(l). The d-constraint pins coarse carriers only with constant ~1/lambda_l >> n^w_l: the d-constraint
 never gives window-pinning, and dropping such switching from window data fails the averaging condition n >> K.

2.4 (HEURISTIC) Spurious vs forced switching. Two-sided decompositions are not unique: at scale t one may move x*u_l between the
 base (if resonant, z-signed) and carrier l (block cost t x/lambda_l inside the gap) for free, |x| <~ gap*lambda_l/t. Window
 pinning asks for SOME decomposition with small switching; spurious switching can always be removed. Only forced switching
 (one-sidedness genuinely needed by g) matters.

2.5 (HEURISTIC) Size of fine components of g. On a swallowed fine signature set S_l the sandwich theta_+ v_l <~ g|_{S_l} <~ theta_- v_l
 (up to budget errors t/(2 q_0)) and |theta| <= 3 lambda_l/t give ||g 1_{S_l}||_1 <~ sqrt(lambda_l delta°_l) (optimize t), summable.

2.6 (HEURISTIC) Scale mismatch kills exactification inside one window: exactifying near-resources of room/margin <~ t at window
 scales moves f by ~T_hi * delta°, but the averaging-at-a-nearby-point argument needs p*(f'-f) <~ (1-rho^2) T_lo^2.
 Exactification is only useful if done at the finest scale of the window or uniformly (rooms -> 0 uniformly).

2.7 (OBSERVATION, PROVED) For two first rows with the SAME base functional a (data (a,z) and (a,z')), f'-f = L^*(w'-w): the
 primal base excess q - a is identical; only the block functionals differ. So "near-contact vs contact" is invisible in the
 primal base excess; it enters only through the normer and the block functionals w'.
