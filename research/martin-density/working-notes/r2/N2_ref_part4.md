# N2 referee, part 4: kink class, Section 3.7-3.8, Section 4-5, numerics

## 1.6 / 3.9 Kink class
Algebra re-derived: sigma 1_P = (w - w 1_Q)/M, v'' = (c'/M) w + omega'', omega'' := v''_Q - (c'/M) w 1_Q; flatness <v'',zeta> = 0 gives
d(omega'') = -c'/M (Lemma 1.2(c) extends to bounded omega on Q: sum zeta(k) omega(k) converges absolutely); Omega - s v'' =
(omega - s omega'') - d(omega - s omega'') w; Delta omega = (s+ - s-) omega'', Delta d = -(s+ - s-) c'/M. Correct.
Caveats: (i) omega'' is finitely supported only if Q is finite (true in the C_referee configuration, where Q is finite by assumption);
in general (E2) fails and Theorems 1-3 would need omega in l_inf(Q). (ii) (E4) (max-form kappa <= 1) is an extra hypothesis. The
C_referee class is defined through WEIGHTED second-order coefficients (Gamma_2 <= 1 < Gamma_w, Gamma_w = q_0 H_b + sum sigma_m H_m); mates of
that class can have max(h(b+-), H(omega+-)) > 1, which Theorems 1-3 do not cover (this is N2's own open item 7: second-order rebalancing at
engineered approximants). So "kinks create no new mechanism; the open part is exactly the Delta d < 0 pinning problem" (3.9, 5.3(e))
is over-stated: the second-order (kappa_max > 1, weighted <= 1) part is also open. VERDICT: identification correct (with Q finite);
consequence over-stated.

## 3.7(a),(b),(c)
(a) identity v(x') = Delta d M pi(zhat)[u_{k0}(x')/u_{k0}(zhat) - pi(x')/pi(zhat)] re-derived (A u_{k0}(zhat) = Delta d M pi(zhat) from v(zhat) = 0;
pi(zhat) != 0 because otherwise u_{k0}(zhat) = 0, i.e. w(k_0) = 0 and Delta d = 0). Converse of Fact C re-derived (<w,zeta'> = c', |zeta'| <= c').
Status changes are unavoidable (Lemma 3.3), so "w' = w exactly" never holds at NA points; N2 acknowledges and needs a perturbation lemma.
With Lemma R (part 3) the perturbation lemma is unnecessary: Corollary R proves the block-tame case (with (TT)).
(b) T-dependent, SKETCH label fair. (c) see part 3: the obstruction is mis-located (coarse non-peaks are free; fine scrambled ones count).

## 3.8 Existence of Delta d < 0 mates (SKETCH)
Re-derived: |zeta_1| = w_1(2) lambda_0 u(xi) + M_1 pi(xi), hence c M_1 pi(xi)/|zeta_1| = c - lambda_0 w_1(2) delta, and the pi-coefficient of
v = c u - delta R_1*w_1 vanishes, v = (c M_1 pi(xi)/(n|zeta_1|)) h. Moreover pi(xi) = sum_P lambda_k |u_k(xi)| > 0 automatically (sigma_k = sign u_k(xi)
on peaks), so Delta d < 0 iff c kappa' > 0 and v is z-signed iff c > 0: consistent. Injectivity/Y cap c_00 = {0}: T e_{2,1} = const (h - kappa' pi),
pi a convergent combination of the other T e_{k,1}; the signature argument of P1 2.1 on S_{l_0} = K' still applies. (2,1) a strict non-peak:
u_{2,1}(xi) = -kappa' pi(xi)/n small. Margins of the other peaks are robust (P1 6.0) so (MS) holds (mu >= q_0 min(1/4, 2 sqrt Phi) gives
sum{lambda : mu < s} = O(s^2)). Plausible; SKETCH label fair. With Corollary R + the P1-type far-tail comparison (only v-multiples and
allowedness-suppressed targets have mass on K' far out) these mates are recovered -- i.e. no Delta d < 0 example is known to resist.

## 4.2 Cross-block exact relations
(a),(b) quoted (refereed). (c) correct by definition; sign typo: with Delta omega_{m'} = -(c'/lambda) e_{n'} one gets
v = c u_{n,m} - c' u_{n',m'} - Delta d_m R_m* w_m - Delta d_{m'} R_{m'}* w_{m'} (N2 writes + for the last term; convention). Rank condition for two
active blocks: ell_m|_J != 0. Fine. (d) HEURISTIC remark.

## 4.3 Theorem 4 (conditional averaging) -- re-derived
Convexity of p*; for s_j >= |t| use (HC); for s_j < |t| (then |t| > s_1) use p*(f'+t h_j) <= p*(f'+t gbar) + |t| kappa s_j and (HT);
sum_{s_j < |t|} s_j < 2|t|; total <= 1 + Q t^2/2 + 2 kappa t^2/J <= 1 + t^2[1/2 - (1-rho^2)/16] <= s(t) for t^2 <= (1-rho^2)/2. Large |t|: slack.
p*(g' - gbar) <= (1/J) sum kappa s_j <= 2 kappa s_J/J. Correct. VERDICT: PROVED (as a conditional statement). Its hypotheses (HT) are HEURISTIC
in general and nothing shows they can be met at the resonant f's of interest; the theorem is a clean reformulation of E's averaging
skeleton, not progress on the approximate-resonance core.

## 4.5 Far rigidity compatible with Lemma B (SKETCH)
The P1 2.1 signature argument survives the detector parts (detectors G_n disjoint from every S_l) with delta_l replaced by delta_l eps_l in the
allowedness inequality (2 c_l <= 2^{-2s} c_{l'} delta_{l'} eps_{l'}): any i is allowed at all large l since c_l decays super-exponentially, so
delta_l eps_l can be as small as desired. Free tail mass (E Cor 6.2) of u_i relative to a group member g:
dist(u_i|_{(W,inf)}, R u_g|_{(W,inf)}) <= (delta_i/n_i)(eps_i||h_i|| + eps_g||h_g||) << Phi_i. Plausible; SKETCH label fair. Note: this only blocks
source (S2); (S1), (S3) and implants remain (N2 says so). The NC/rate-version remark: rate version plausible (delay the targets), HEURISTIC.

## 5.2 Localization (PROVED mod R1)
For j in J_0 (|z_j| < 1): z'_n(j) -> z(j) (Fact E(vii)), so |z'_n(j)| < 1 eventually, j notin supp a'_n, P_{J_0} kills l_1(supp a'_n). With R1
(Li C(f_n) in Li S(f_n) for C-tame NA f_n) the conclusion follows. Correct, but note the scope: only C-TAME approximants (finitely many strict
non-peaks and degenerate peaks, (MS)); R1 itself rests on unrefereed C Thm 6.2/Prop 6.5 (refereed in C_referee as correct). VERDICT: correct
(conditional).

## Numerics
N2's lemma32_check.py and thm1_check.py re-run: outputs reproduced exactly (176 cases, 0.0119 / 0.999998; 4 seeds, worst excess -1.1e-9 ...
-8.4e-9). Caveat on thm1_check: the worst value occurs at |t| = 1e-4 where s(t)-1 = 5e-9 is below the SOCP tolerance, so the small-t
end of the test is vacuous; the informative range is moderate t. Referee's ytrick_exact.py: Lemma R holds to 2.2e-16.
