# Z3 part 6 — density of block-tame first rows; Lemma Z as pure lower semicontinuity; numerics

## 6.1 Proposition (peak-ification: (BT) points are dense among finitely supported first rows). SKETCH (all steps written except
the final genericity step, see the caveat; status changes of the finitely many coarse carriers are harmless for (BT), only EXACT
degeneracy at f_L must be avoided, i.e. theta^L_m must avoid the finitely many values |u_l(zhat)|/Phi_l, l < L, m(l) = m; theta^L_m is a
continuous, non-constant function of the first push x_L on each interval where the recursion has no case switch, because
d|zeta|_m = sum_k w_m(k) d zeta_m(k) and k(L) is a peak with |w| = M, while the induced changes of the later pushes have total weight
sum_{l>L} lambda_l/delta°_L << lambda_L).  Statement under (D*):
Let T be the SLD operator, and assume the design satisfies
 (D*)  c_l psi_l <= delta°_l / 8 for all large l, for some psi_l -> infinity
(this can be arranged without affecting Theorem thm:SLD: choose the sets S_l recursively, S_l after c_l is known, with
min S_l <= (1/4) log_2(1/c_l), disjoint from all previously used coordinates and target supports; then delta°_l >~ min(2^{-l} c_l^{1/4}, 1)).
Let f in S_{p*} have F finite and no degenerate peaks. Then there are first rows f_L -> f (L -> infinity) with the same base part a,
each satisfying (BT); in particular f_L in R_BT subset Rec (Corollary cor:BTrecovered).
*Proof.* Fix L so large that no S_l, l >= L, meets F. Recursively in l >= L define delta on S_l \ F (and delta := 0 elsewhere):
let V_l := u_l(zhat + delta_{<l}), where delta_{<l} is the part already defined; only the target y_l can see delta_{<l}, and v_l does not.
Put A_l := 3 theta_{m(l)} Phi_l + psi_l Phi_l with Phi_l := Phi_{m(l)}(k(l)), theta_m the threshold constant of f. Choose a push sign
sigma_l for which the coordinates s in S_l \ F with sigma_l z_s < 1 carry v_l-mass >= ||v_l 1_{S_l\F}||/2 (one of the two signs does), and
put delta_s := sigma_l kappa_l on those coordinates with kappa_l in [0, 1] chosen so that x_l := v_l(delta 1_{S_l}) satisfies
|V_l + x_l| >= A_l with |x_l| <= 2 A_l (if sgn V_l = sigma_l or V_l = 0 take |x_l| = A_l, otherwise |x_l| = |V_l| + A_l <= 2A_l).
This is possible since 2A_l <= delta°_l/4 for l large by (D*) (Phi_l <= c_l). Moves keep |z_s + delta_s| <= 1 (sigma_l z_s < 1 and
kappa_l <= 1 - ... after shrinking kappa on coordinates close to sigma_l; the available mass bound absorbs this).
For l' > l, u_l(delta 1_{S_{l'}}) = 0 (y_l avoids S_{l'} by allowedness (a), v_l lives on S_l), so at the final point
|u_l(zhat + delta)| = |V_l + x_l| >= A_l. Cost: |u_l(delta)| <= 2A_l + |y_l(delta_{<l})| and lambda_l <= c_l, so by Lemma 3.1
p*(f_L - f) <= C c(delta) <= C sum_{l >= L} lambda_l log(e/lambda_l) -> 0, and the threshold constants move by o(1).
(BT) at f_L for L large: F_L = F; carriers with l >= L are peaks with margin >= q_0^L(A_l - theta^L Phi_l) >= q_0^L psi_l Phi_l/2
(theta^L -> theta); carriers with l < L keep u_l(zhat_L) = u_l(zhat) and, as f has no degenerate peaks and theta^L -> theta, keep their
status (strict non-peak with positive gap, or peak with positive margin) — for the finitely many l < L this holds once theta^L is close
enough to theta, which we may ensure by taking L larger (L is chosen after nothing else). Hence Q^L_m is finite, there are no degenerate
peaks, and (MS) holds: sum_{mu < s} Phi <= sum_{psi_l Phi_l < 2s/q_0} Phi_l = o(s) because psi -> infinity and Phi_l decreases
geometrically along each block. QED
*Caveat (honest).* "No degenerate peaks" is used for the finitely many l < L, uniformly in L: the step "take L larger" is legitimate only
if the margins/gaps of the l < L dominate |theta^L - theta| Phi_l; since |theta^L - theta| <= C sum_{l>=L} lambda_l log and Phi_l >= Phi_{L-1}
for l < L, this holds when sum_{l >= L} lambda_l log(1/lambda_l) = o(min_{l<L} (margin or gap of l) Phi_l). If f has margins/gaps decaying
faster along l, choose the A_l (a continuum of choices) so that theta^L = theta exactly — possible by one extra tuning push on a fine
signature set (SKETCH, same genericity issue as 5.5). So: PROVED when f has no degenerate peaks and its small margins/gaps decay no faster
than the design's c_l; SKETCH in general.

## 6.2 Corollary (Lemma Z is a pure lower-semicontinuity statement). PROVED given the existence of G-approximants: by 4.2 (PROVED)
when all rooms are positive and B is finite with (H2), (H3); by 6.1 (SKETCH) in general for F finite.
For such f, g in C(f), rho < 1: Lemma Z holds at (f, g, rho) iff dist(rho g, C(f')) -> 0 along SOME sequence f' -> f in G; the sequences
f_L of 6.1 (in R_BT) and, when all rooms are positive, the far lowerings f^L of 4.2 (in R_0^+-) are candidates. In the language of parts 2-4,
every such approximant is a companion of f at distance >~ c_L log(1/c_L) (resp. c_{L+1}), so Theorem E can use it only on windows above
sqrt(c_L); there the coarse carriers l < L keep the rooms of f, and the race of 4.3(ii) is unchanged.

## 6.3 Numerical sanity checks (scripts in ctx/r5/Z3_work/).
 * check_inward.py (Lemma 5.1): 2000 random finite blocks with a degenerate peak; inward moves at the degenerate peak:
   max [(N(W)-1) - bound] = 4.4e-16, max |<W - w, zeta>|/s = 2.3e-13 (no first-order term); the same omega moved OUTWARD has
   (N(W)-1)/|s| >= 2.6e-4 > 0 in all trials (a genuine kink), confirming that the sign condition is what matters, not the gap.
 * check_cost.py (Lemma 3.1): one block, n = 30, norming functionals by the clamp formula certified by N(w) = 1 and <w, zeta> = |zeta|
   (error 1.2e-15); 900 perturbations mixing unweighted-large fine perturbations and small global ones: max L/R = 0.76.
 * check_cost2.py (necessity of the unweighted term): perturbing ONE fine strict non-peak by |dU_k| = 0.1 lambda_k gives
   L/(Delta log(e/Delta)) up to 1.4e8 (median 6.6e5) but L/R <= 3.2: the cost of a companion is governed by
   sum_k min(lambda_k, |u_k(delta)|) (UNWEIGHTED), i.e. exactifying a strict non-peak carrier of room r costs ~ min(lambda, r), not lambda r.
