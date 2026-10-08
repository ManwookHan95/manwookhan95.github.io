# E referee — part 5: deeper checks of T1, T4 and of E's refined necessary conditions

## 5.1 Structure of one-sided linear decompositions (derived; PROVED here)
Let (b, Om) be admissible for t in [0, tau_0] at f (single block, finite I). As in A Prop 7.4, the first-order block
coefficient vanishes: psi'(0+) + <D Om, D w>/C = 0 and psi'(0+) = <Om, alpha>, where psi(t) = ||w + t Om||_inf. Hence
sigma_k Om(k) = mu on supp alpha, sigma_k Om(k) <= mu on P \ supp alpha. Put d := -mu/M, omega := Om + d w: then
omega = 0 on supp alpha, sigma_k omega(k) <= 0 on P \ supp alpha (only alpha-null peaks are used, downward), and
d = <D w, D omega>/C (same algebra as A Lemma 6.3, using M + C = 1). Off P, |Om(k)| <= ~2/tau_0 + |mu| (box), so
Om is bounded. Consequently two-piece mates have b+ - b- = sum_m R_m*(omega-_m - omega+_m) - Delta d_m R_m* w_m with
Delta d_m = <D_m w_m, D_m(omega-_m - omega+_m)>/C_m.

## 5.2 T1 and the d-mismatch (why the general case is NOT covered)
Transfer to an NA approximant f'' forces the block part omega - d'' w'' (to stay admissible at f''), and both sides
must represent the same g''. The base must then absorb E'' = d'' L*w'' - d L*w (+ far tails). Write
Delta := x'' - xhat. The eta-masses on contacts j in K cap [1,N'] (including the finitely many NEAR contacts, where
||U* e_j*|| is not small) move e by ~eta, hence u_k(x'') by ~eta for generic k. Then
  * fine coordinates (Phi(k) <~ eta) are scrambled (status flips, off-peak values move by O(1)): mass ~ eta;
  * off-peak coordinates with Phi(k) >= eta move by ~eta/Phi(k): mass ~ eta x #(such k);
so ||L*(w'' - w)|| >~ c eta with c not small, and the first-order cost |t| |d| c eta beats the slack
(1-rho^2) t^2/6 on |t| in [eta, 6|d| c eta/(1-rho^2)]: a band of boundedly many octaves where neither the eta-regime
(two-sided, |t| <= eta) nor the transferred one-sided regime works. Attempts I checked that do NOT close it:
  (i) keep the ORIGINAL w in the d-term (W'' = omega - d w): the sup-norm derivative at flipped peaks of w''
      (w''(k) = -w(k) = +-M) is +|d|M on the side where t d > 0: first-order excess 2|t d| M. Works only on the side
      t d < 0.
  (ii) hybrid (w on coarse coords, w'' on fine): coarse mismatch can be killed by finitely many linear conditions,
      but the fine part leaves base mismatch |d| sum_{Phi < C eta} lambda_k 2M ~ |d| eta: same order.
  (iii) rescaling via L*w'' = f'' - a'': moves the mismatch between base and block; total first-order excess is
      unchanged (budget identity, A Lemma 7.1 at f'').
Plausible repair (not proved): averaging over several eta-levels cannot help (mismatch is set by the single f''),
but matching ALL coordinates with Phi(k) >= eps*eta (finitely many, ~log(1/(eps eta)) linear conditions with
tolerance o(Phi)) would make ||E''|| <= eps eta; solvability with o(1) moves is a QUANTITATIVE tail-independence
(condition number) question — the same crux E identifies for block resources. So T1 is proved only (as a sketch) in
the d-neutral case Delta d = 0 (A-referee 5.4), and E's refined condition (R-b) ("one-sided BASE resources are not
enough") is not established for two-piece mates with Delta d != 0. Also near-FLIP base resources (j in supp a,
|a_j| small; A §7.2 (N1)) are not treated by T1/T4 at all.

## 5.3 T4: the status of N* after making its head exact contacts
Making z''_l = s_l on the head shifts u_{N*}(x'') by sum_head |Z_l| gamma_l / n (all terms of ONE sign) <= c_gamma
lambda_{N*} eps_0/n. Relative to the peak threshold |u| >= lambda M|zeta|/(C m^2) this is r := c_gamma eps_0 C m^2/(n M |zeta|).
The mate condition only forces c_gamma eps_0 <~ M/(4 c^2 n) (base first-order cost 2 c^2 eps_0 c_gamma n t^2/M <= t^2/2),
so r can exceed 1 for small c: N* may become a (+) peak at f'' and regime (a) collapses. Even with r < 1, the shift
gives d''_{N*} = rho c n u_{N*}(x'')/|zeta''| != d''_k for the other carriers (whose values are matched), i.e. a
first-order switching cost |t| |Delta d''| kappa_q(L*w''), with coefficient ~ 2 rho^2 c^2 n c_gamma eps_0 kappa/(M|zeta|)
at |t| ~ t_a, which is NOT <= (1-rho^2)/6 for rho near 1 in general. A common window shift V cannot separate N*
from the other v0-carriers (their window parts are nearly collinear: (v0 - Z_k(xhat) a)/n_k with Z_k(xhat) ~ eps_0).
Repair (plausible, not written): average J frozen representations with heads at J dyadic scales (each mismatch is
proportional to its own lambda_{N*_j}, so the boundary excess is divided by J as in Thm 5.1), or require
c_gamma eps_0 small. The e''-shift caused by the masses themselves is harmless here because the masses sit on FAR
near-contacts (||U* e_l*|| -> 0), unlike T1.

## 5.4 Multi-block remark (not in E)
In Martin's construction the same w'_n drives every block, so each carrier has near-duplicates in all blocks at
comparable scales, with relative positions rescaled by the block threshold constants theta~_m. An adversary keeps them
all one-sided by making carriers near-threshold in the block with the LARGEST threshold (deep peaks elsewhere), so this
is not automatically a two-sided resource; but it forces the rigid design to be consistent across blocks. Unexplored.
