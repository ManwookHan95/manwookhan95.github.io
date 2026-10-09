# N2 referee, part 3: a sharper treatment of Delta d < 0 (Lemma R, Theorem 3*), refuting the strong form of N2 3.4

Notation of N2 (single active block m_0, index dropped). For block functionals w, w' (N(w) = N(w') = 1, M + C = 1 = M' + C',
peak sets P, P') define the STATUS-PRESERVING set
  S := {k in P cap P' : w(k) w'(k) > 0}  cup  {k notin P cup P' : |w'(k) - w(k)| <= M' - |w'(k)|},
its complement S^c (opposite peaks, new peaks, lost peaks, non-peaks pushed beyond their gap at f'), and
  gamma := C' - C,  Delta := D(w' - w),  Y := (w' - w) 1_S,  y := w' + Y,  R_1 := <D w', D (w' - w) 1_{S^c}>.

## Lemma R (status-preserving absorption). PROVED (and checked numerically to 2e-16).
If C + 2 gamma > 0, then
  N(y) <= 1 + gamma_+ + (||Delta||^2 + ||D Y||^2 + 2|R_1|) / (2 (C + 2 gamma)).
Proof. Sup part: on common same-sign peaks |y(k)| = |2 sigma M' - sigma M| = 2M' - M; on S-non-peaks |y(k)| <= |w'(k)| + |w'(k) - w(k)| <= M';
on S^c, y(k) = w'(k). So ||y||_inf <= M' + (M' - M)_+ = M' + (-gamma)_+.
D part: ||D y||^2 = C'^2 + 2<Dw', DY> + ||DY||^2, <Dw', DY> = <Dw', Delta> - R_1, and <Dw', Delta> = C'^2 - <Dw', Dw> = (C'^2 - C^2 + ||Delta||^2)/2.
Hence ||Dy||^2 = 2C'^2 - C^2 + ||Delta||^2 + ||DY||^2 - 2R_1 = (C + 2gamma)^2 - 2 gamma^2 + ||Delta||^2 + ||DY||^2 - 2R_1, and
sqrt(A^2 + x) <= A + x_+/(2A). Adding, with M' = 1 - C - gamma: N(y) <= 1 + gamma + (-gamma)_+ + (...) = 1 + gamma_+ + (...). QED.
Contrast (N2 3.2(b)): the full reflection y = 2w' - w has N >= 1 + 2M at any common opposite peak. Lemma R shows that the reflection is
harmless on status-preserving coordinates; only S^c and the scalar gamma_+ cost at first order.
Numerics (N2ref_work/ytrick_exact.py, exact J by bisection + golden section, 300 random 16-coordinate blocks with non-peaks, perturbation
t in [1e-4,1e-2] and flipped fine peaks): max [N(y) - bound] = 2.2e-16; naive reflection: min (N-1)/(2M) = 1.0000000016.

## Lemma R, general form. PROVED (numerically checked: ytrick_general.py, 300 cases; the only violation had C + 2gamma = -0.086 < 0,
## i.e. outside the hypothesis, and there the exact identity for ||Dy|| and the sup bound still held).
For eps >= 0 let S_eps := {k : |2w'(k) - w(k)| <= M' + (M' - M)_+ + eps} (the coordinates where the reflection 2w' - w does not overshoot).
Then, with Y, y, R_1 as before and C + 2gamma > 0:  N(y) <= 1 + gamma_+ + eps + (||Delta||^2 + ||DY||^2 + 2|R_1|)/(2(C + 2gamma)).
Same proof (the sup bound holds by definition of S_eps; the D-identity does not depend on S). S_eps contains all common same-sign peaks,
all same-sign LOST peaks with gap' <= M' (|2w' - w| = M' + (M'-M) - 2 gap'), all non-peaks of both with |w'-w| <= gap'; S_eps^c consists of
common opposite peaks, NEW peaks whose old gap exceeds eps, and non-peaks pushed beyond their gap. (So "no degenerate peaks" is not needed
for peaks that are merely lost.)

## Theorem 3* (Delta d < 0, sharper sufficient condition). PROVED modulo the tuning hypothesis (same as Theorem 3).
Setting of N2 Theorem 3 (F finite, one active block, Delta d < 0, theta := 0, engineered f'_n of Theorem 1), and assume the tuning can be done
(e.g. (TT); see part 2): |Delta d'_n - Delta d| = o(t_n). Suppose
 (PC*)  (C'_n - C)_+  +  ||D(w'_n - w)||_2^2  +  sum_{k in S_n^c} lambda_k |w'_n(k) - w(k)|  =  o(t_n).
Then g is in Ls(f).
Proof. Side + (tau > 0) and small scales: exactly as N2 Thm 3 (side + is the certificate (b'_0, omega+)). Side - (tau < 0, t_n <= |tau| <= T_0):
s := tau rho Delta d = |tau| rho |Delta d| (<= eta_0/2 by the choice of T_0). Block: W := w' + tau rho(omega- - d'(omega-) w') + s Y
= (1-s)[(1 - tau~ d') w' + tau~ omega-] + s y (Lemma 1.3), so N(W) <= 1 + tau^2 rho^2 H'(omega-)(1+eta_0)/(2(1-s)) + s (N(y) - 1), and Lemma R.
Base: with Omega'- := omega- - d'(omega-) w' + Delta d Y, b'- := g' - L*Omega'- = b'_0 - v - (Delta d - Delta d') R*w' + Delta d R*((w'-w)1_{S^c})
(Lemma 3.1 algebra). b'-(x') = -Delta d <Y, R x'> and tau rho b'-(x') = -s <Y, R x'> = -s Bx + s <(w'-w)1_{S^c}, R x'> <= s sum_{S^c} lambda_k|w'-w|(k)
(Bx >= 0, ||u_k||_1 <= 1, ||x'||_inf <= 1 + ||U||). Kinks: Theorem 1's tail term plus 2s ||R*((w'-w)1_{S^c})||_1 <= 2s sum_{S^c} lambda_k|w'-w|(k), plus
|tau| rho |Delta d - Delta d'| ||R*w'||_1 (o(t_n)|tau|). |R_1| <= max_k(Phi(k)/m) sum_{S^c} lambda_k|w'-w|(k). Hence the extra first-order cost on
side - is |tau| o(t_n) <= (1-rho^2) tau^2/64 for |tau| >= t_n, n large; the rest is Steps 5-8 of Theorem 1. QED.

## Corollary R (block-tame carrier block). PROVED modulo writing (upgrades N2 3.7(a) from SKETCH; no perturbation lemma for J needed).
If Q_{m_0} = {k_0}, the carrier block has no degenerate peaks and satisfies (MS), and (TT) holds, then (PC*) holds; so Delta d < 0 two-piece
mates with this structure are in Ls(f).
Proof. Status changes at x'_n: a peak k can change status only if mu_k <= C_1 ||E_n - e|| (= O(t_n)) or mu_k <= 2||u_k 1_{(N''_n,inf)}||_1;
lambda-mass o(t_n) by (MS), resp. -> 0 as N''_n -> infinity by dominated convergence (no degenerate peaks), made <= t_n^2 by choosing N''_n
after t_n. k_0 stays a strict non-peak with |w'(k_0) - w(k_0)| = O(t_n) < gap'/2. So sum_{S^c} lambda_k|w'-w| = o(t_n). ||D(w'-w)||^2 = O(t_n^2)
(Phi(k_0)(w'-w)(k_0) = C' rho'_0 - C rho_0 = O(t_n), peaks Phi^2 (M'-M)^2, S^c tiny). gamma: with rho_k := zeta(k)/(Phi(k)|zeta|),
w(k_0) = C rho_0/Phi(k_0), and A := sum_P Phi^2, the exact identities C^2(1 - rho_0^2) = (1-C)^2 A and
C'^2(1 - rho_0'^2) = (1-C')^2 A - sum_{L} Phi^2 (M'^2 - w'(k)^2) (L = lost peaks; no new peaks since only k_0 is a non-peak and it stays one)
hold; the tuning Delta d' = Delta d means rho'_0 = rho_0 (Delta d' = l(x')/|R x'| with l = R* Delta omega, Delta omega on k_0); the map
x -> x^2(1 - rho_0^2) - (1-x)^2 A is strictly increasing, so C' - C = O(flip Phi^2-mass) = o(t_n). QED.
For |Q_{m_0}| >= 2 finite: C'^2(1 - sum_Q rho'_k^2) = (1-C')^2 A + o(t_n), so (C' - C)_+ = o(t_n) iff sum_Q rho'_k^2 <= sum_Q rho_k^2 + o(t_n):
ONE scalar inequality beyond the tuning (achievable with one extra tuning variable, e.g. a near free coordinate; not written).

## Consequences for N2's claims
 * N2 3.4 / 4.7 "the mismatch Delta d R*(w'-w) must be absorbed in the base": FALSE in the stated generality. Only its status-changing part
   (S^c) and the scalar (C'-C)_+ must be paid; the status-preserving part is absorbed by the block at second order (Lemma R).
 * N2's (PC) is much stronger than needed: it requires the coarse non-peak shifts (~t_n each) to be pinned; (PC*) does not.
 * N2 3.7(c) ("generic case needs ~log(1/t_n) pinning conditions, quantitative tail independence"): the picture is INVERTED by Lemma R.
   Coarse non-peaks (Phi(k) gap(k) >> t_n) are free. The obstruction is the lambda-mass of carrier-block coordinates that the perturbation of
   size t_n SCRAMBLES: fine non-peaks with Phi(k) gap(k) <~ t_n and near-threshold peaks. Under (MS) and
   (MS-Q)  sum{lambda_k : k in Q_{m_0}, Phi(k) gap(k) <= s} = o(s)  (s -> 0, at least along the scales used),
   (PC*) reduces to one scalar inequality. (MS-Q) fails only if the carrier block has strict non-peaks at a positive proportion of fine scales;
   there a bounded number of scales just below t_n would have to be pinned (HEURISTIC). This is the honest residue of the Delta d < 0 problem.
