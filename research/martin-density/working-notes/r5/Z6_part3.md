# Z6 part 3: four elementary structural facts (SLD operator, N fixed, F finite)

Notation as in the note, Section 8 (two-sided decomposition (B_pm,Theta_pm) of g in C(f) at scale t, Delta theta_l,
tau_l := -eps_l Delta theta_l for swallowed l, d_{pm,m}, omega_{pm,m} from Lemma suplevel).  A carrier l (block m=m(l),
k=k(l)) is "swallowed with sign eps_l" if z = eps_l on S_l \ F (r_l = 0).

## 3.1 Lemma (d-coefficient of a strict non-peak)  [PROVED]
For k in Q_m, Phi_m(k) w_m(k)/(m C_m) = u_{k,m}(xi)/sigma_m.  Hence the weight of Lemma badpeaks is
q_l = eps_l u_l(xi)/sigma_m, and |q_l| <= M_m Phi_m(k)/(m C_m) (non-peak threshold).  Moreover
gap_m(k) = M_m (1 - |u_l(xi)| m C_m/(sigma_m M_m Phi_m(k))), so |q_l| = (M_m - gap_m(k)) Phi_m(k)/(m C_m):
small d-coupling <=> gap close to M_m (d-neutral <=> w_m(k) = 0 <=> gap = M_m).
Proof. Lemma threshold off P: w(k) = C zeta(k)/(Phi(k)^2 sigma), zeta(k) = lambda_k u_k(xi) = m Phi(k) u_k(xi).
So Phi w/(mC) = Phi C m Phi u(xi)/(Phi^2 sigma m C) = u(xi)/sigma.  |w(k)| = M - gap gives the rest.  QED

## 3.2 Lemma (shift pinning by a pair of swallowed peaks)  [PROVED]
Let k_1,k_2 be non-degenerate peaks of block m whose carriers l_1,l_2 are swallowed, with
varsigma_{k_1} eps_{l_1} = -1 and varsigma_{k_2} eps_{l_2} = +1 (varsigma_k = sign w_m(k)).  If (tau_{l_i})_- <= X (i=1,2), then
   -X/lambda_{l_2} - t/(sigma_m |alpha_m(k_2)|) <= Delta d_m M_m <= X/lambda_{l_1}.
Proof. eq. (peakshift): |omega_+(k)|+|omega_-(k)| = -varsigma_k Delta Theta_m(k) - Delta d_m M_m in [0, t/(sigma|alpha(k)|)].
Delta Theta_m(k) = Delta theta_l/lambda_l = -eps_l tau_l/lambda_l, so Delta d_m M_m = varsigma_k eps_l tau_l/lambda_l - Y_k with
Y_k in [0, t/(sigma|alpha(k)|)].  For k_1: Delta d M = -tau/lambda - Y <= (tau)_-/lambda.  For k_2: Delta d M = tau/lambda - Y
>= -(tau)_-/lambda - t/(sigma|alpha|).  QED
Consequence: condition (H2) of Definition swallowed may be replaced by
(H2') every block has a non-degenerate peak with a good carrier, OR two non-degenerate peaks with swallowed carriers of
opposite types (varsigma eps = -1 and +1) whose (tau)_- are controlled (e.g. by Lemma modswallow(b) under (H1)).
Remark: under (B_fin) or (B_res) of the note, (H2) is automatic (B finite, resp. bad carriers non-peaks, while every
block has infinitely many non-degenerate peaks: the u_{k,m} are dense in S_{q*} and the threshold Phi_m(k) -> 0).  So
(H2) can only fail for infinitely many swallowed peaks; at maximal contact z = 1 off F, peaks of both signs exist in
every block (density again), so (H2') holds with eps = 1 and varsigma = +-1 provided their (tau)_- are controlled.

## 3.3 Proposition (exact two-piece data force d-neutrality on doubly swallowed blocks)  [PROVED]
Let block m contain peaks k,k' (degenerate or not) whose carriers l,l' are swallowed (S_l \ F, S_{l'} \ F contained in K,
z = eps_l, eps_{l'} there) with opposite types: eps_l varsigma_k = - eps_{l'} varsigma_{k'}.  Then every pair of two-piece
data (Definition twopiece) for any g has Delta d_m = 0.  In particular at maximal contact (z = 1 off F) EXACT two-piece
data are always d-neutral, and the allowance Delta d_m >= 0 of Corollary D1 is void there.
Proof. b^+ is z-signed on K and b^- is (-z)-signed, so v := b^+ - b^- is z-signed on K; both pairs represent g, so
v = sum_{m'} R_{m'}^*((omega^-_{m'} - omega^+_{m'}) - Delta d_{m'} w_{m'}).  Fix s in S_l \ F, s large.  By (P1) the only
vectors nonzero at s are u_l (value v_l(s) = delta_l 2^{-s}/n_l) and targets y_{l''}/n_{l''} of later carriers l'' that are
allowed to meet S_l at s, i.e. 2 c_{l''} <= 2^{-2s} c_l delta_l.  The omega^pm are finitely supported, so for s beyond the
finitely many target supports of their carriers they contribute nothing at s.  Hence
 v(s) = -Delta d_m lambda_l w_m(k) v_l(s) + rho(s),  |rho(s)| <= (4/3) D sum_{l'': 2c_{l''} <= 2^{-2s} c_l delta_l} lambda_{l''},
D := max_{m'} |Delta d_{m'}| M_{m'}.  Since lambda_{l''} <= c_{l''}/4 and c_{l''+1} <= c_{l''}/4, the sum is <= (1/6) 2^{-2s} c_l delta_l,
while |lambda_l w_m(k) v_l(s)| = lambda_l M_m delta_l 2^{-s}/n_l with lambda_l = m 2^{-m-k} c_l.  So
|rho(s)|/|Delta d_m lambda_l M v_l(s)| <= (2/9) (D/|Delta d_m| M_m) n_l 2^{m+k} 2^{-s}/m -> 0 as s -> infinity (if Delta d_m != 0).
Thus for all large s in S_l \ F: sign v(s) = -sign(Delta d_m) varsigma_k, and z-signedness forces -sign(Delta d_m) varsigma_k = eps_l.
The same at l' gives -sign(Delta d_m) varsigma_{k'} = eps_{l'}; multiplying, eps_l varsigma_k = eps_{l'} varsigma_{k'}: contradiction.  QED

## 3.4 Proposition (uncompensated d-coupled switching is transient)  [PROVED]
Let block m, and let Sigma be a set of swallowed strict non-peak carriers of block m with q_l > 0 for l in Sigma.  Write
 A := |Delta d_m| M_m + 2t/sigma_m + (1/(m C_m)) sum_{l notin Sigma, m(l)=m} Phi_m(k_l)|w_m(k_l)| |Delta theta_l|
      + sum_{l in Sigma} q_l (tau_l)_- .
Then sum_{l in Sigma} q_l (tau_l)_+ <= A; in particular (tau_l)_+ <= A/q_l for each l in Sigma.
Proof. eq. (didentity): Delta d_m M_m = (1/(mC_m)) sum_k Phi(k) w(k) Delta theta_k + r_m, |r_m| <= 2t/sigma_m.  For l in Sigma,
Phi w Delta theta_l/(mC) = -q_l tau_l.  Rearrange and add sum q_l (tau_l)_-.  QED
Reading.  If Delta d_m = O(t) (3.2 or (H2)), the other carriers are O(t)-pinned in the Phi|w|-weighted sense (fine
carriers l > l_* contribute <= C t^5 by the box bound, since Phi_l lambda_l <= c_l^2), and (tau_l)_- = O(t) (budget), then
A = O(t) and every l in Sigma switches by at most O(t)/q_l: each single uncompensated d-coupled carrier is pinned with
its own constant 1/q_l ~ 1/Phi_l (by 3.1 when the gap is bounded away from M_m).  Persistent (scale-independent) switching
through d-coupled carriers therefore REQUIRES compensation (carriers with q of both signs) or exact d-neutrality.  The
constant 1/q_l is not bounded by the SLD window lengths (1/Phi_{l_*-1} >> n^w_{l_*}), so 3.4 does not give window pinning.
