# P2x part 2: first-order bookkeeping — the Bregman lemma (blocks) and the mixed term (base)

(Instance "P2x": a second P2 agent writes P2_part2/3.md concurrently; my files are P2x_part*.md. Notation/toolkit: P2_part1.md.)
For a block m (index dropped) and y in l_infinity with R** y != 0 put zeta_y := R** y (zeta_y(k) = lambda_k u_k(y)), w_y := J(zeta_y), M_y, C_y,
  theta_y := M_y |zeta_y| / (m C_y)   (k is a peak of w_y iff |u_k(y)| >= theta_y Phi_k).
Block data are 0-homogeneous in y, so we compare y = zhat (data of f) with y' = xhat' = x'/q(x') (data of f') directly.

## 2.1 Lemma (clip formula). PROVED.
w_y(k) = M_y clip( u_k(y)/(theta_y Phi_k) ),  clip(s) := max(-1, min(1, s)).
*Proof.* P2_part1 Lemma 1.1: w(k) = sgn(zeta(k)) min(M, C r(k)), C r(k) = C m|u_k(y)|/(Phi_k|zeta|) = M|u_k(y)|/(theta Phi_k). QED.

## 2.2 Lemma (Bregman identity). PROVED.
e(y; y') := 1 - <w_y, zeta_{y'}>/|zeta_{y'}| >= 0 (excess of the old functional at the new point). Then
  |zeta_{y'}| e(y;y') + |zeta_y| e(y';y) = <w_{y'} - w_y, zeta_{y'} - zeta_y>.
Exact form: e(y;y') = sum_{k in P'} |alpha'_k| (M_y - sigma'_k w_y(k)) + (C_y C_{y'} - <D w_y, D w_{y'}>)/C_{y'} (both terms >= 0).
*Proof.* <w_y, zeta_y> = |zeta_y|, <w_{y'}, zeta_{y'}> = |zeta_{y'}|; expand. The exact form: Fact C at y', ||alpha'||_1 = 1, M + C = 1. QED.

## 2.3 Proposition (Bregman smallness). PROVED.
Let Delta_k := |u_k(y') - u_k(y)| <= A + t_k (A, t_k >= 0), Lambda := sum lambda_k, T := sum lambda_k t_k,
gamma := |M_{y'} - M_y| + M_y |theta_y/theta_{y'} - 1|, eps(s) := sum_k min(lambda_k, m s) (-> 0 as s -> 0). Then
 (a) |w_{y'}(k) - w_y(k)| <= gamma + M_y min(2, Delta_k/(theta_{y'} Phi_k)) for every k;
 (b) <w_{y'} - w_y, zeta_{y'} - zeta_y> <= gamma(A Lambda + T) + 4 M_y A eps(A/theta_{y'}) + 4 M_y T;
 (c) e(y;y') <= [gamma(A Lambda + T) + 4 M_y A eps(A/theta_{y'}) + 4 M_y T]/|zeta_{y'}|.
Hence along families with A -> 0, T = o(A), y' -> y weak* (gamma -> 0, theta_{y'} -> theta_y > 0): e(y;y') = o(A).
*Proof.* (a) clip is 1-Lipschitz and |clip(rs) - clip(s)| <= |r - 1| (r > 0). With s = u_k(y)/(theta Phi_k), s' = u_k(y')/(theta' Phi_k), s~ = u_k(y)/(theta' Phi_k):
|w'(k) - w(k)| <= |M'-M| + M(|clip(s') - clip(s~)| + |clip(s~) - clip(s)|) <= |M'-M| + M min(2, Delta_k/(theta' Phi_k)) + M|theta/theta' - 1|.
(b) The pairing is <= sum_k |w'(k) - w(k)| lambda_k Delta_k. gamma-part <= gamma(A Lambda + T). Rest: lambda_k Delta_k min(2, Delta_k/(theta' Phi_k)) <=
min(2 lambda_k Delta_k, m Delta_k^2/theta'); if t_k <= A it is <= 4A min(lambda_k, mA/theta'), else <= 4 lambda_k t_k. (c) Lemma 2.2 and e(y';y) >= 0. QED.
Remark. Only the Bregman pairing is o(A). The displacement sum_k lambda_k |w'(k) - w(k)| is in general Theta(A): each off-peak coordinate with
Phi_k >~ A moves by ~ A/Phi_k (from (a), and sharp when u_k(y') - u_k(y) ~ A). This is why d-mismatches cannot simply be put in the base
(A_referee 5.5, E_referee 3.1, N2 3.6).
Numerical check (P2work/bregman.py; one block, n = 60, Phi_k = 2^{-k}U(0.3,1), 17 off-peak coordinates, J by nested 1-D optimisation; random
|u_k(y') - u_k(y)| <= A):  A = 1e-2, 3e-3, 1e-3, 3e-4, 1e-4:  max e/A = 0.11, 0.046, 0.011, 0.0027, 0.00097 (e = O(A^2) here) while
sum lambda|dw|/A = 2.3, 3.5, 3.3, 2.6, 2.9 (Theta(A)).

## 2.4 Lemma (displacements at an engineered approximant). PROVED.
If x' = z' + U e' with z' = z on [1,N] except at finitely many window FREE coordinates j (|z_j| < 1, j notin F) moved by eta_j, and |z'| <= 1 beyond N, then
  Delta_k <= ||U|| ||e' - e|| + sum_j eta_j |u_k(j)| + 2 ||u_k 1_(N,inf)||_1;
so 2.3 applies with A := ||U|| ||e'-e|| + sum_j eta_j, t_k := 2||u_k 1_(N,inf)||_1, T = T_N := 2 sum_{k,m} lambda_{k,m} ||u_{k,m} 1_(N,inf)||_1 -> 0.
If a' = (a + Delta)/q*(a + Delta), ||U*Delta|| <= nu/2, then ||e' - e|| <= 2||U*Delta||/nu.
*Proof.* u_k(x') - u_k(zhat) = u_k(z' - z) + <U*u_k, e' - e>, ||U*u_k|| <= ||U||; ||x/||x|| - y/||y|| || <= 2||x-y||/||y||. QED.
Consequence: masses and tuning moves O(s_1), N chosen after s_1 with T_N <= s_1^2  ==>  e_m(zhat; xhat') = o(s_1) for every block.

## 2.5 Lemma (the base mixed term, exact form). PROVED.
For b in l_1 with b(zhat) = 0: b(xhat') = b(z' - z) + <U*b, e' - e>, and if a' = (a+Delta)/q*(a+Delta), ||U*Delta|| <= nu/2:
  | <U*b, e' - e> - <P_{e-perp}U*b, U*Delta>/nu | <= 6 ||U*b|| ||U*Delta||^2/nu^2.
*Proof.* h := U*Delta/nu, e' = (e+h)/||e+h||; the map h -> (e+h)/||e+h|| has derivative P_{e-perp} at 0 and second derivative <= 12 on ||h|| <= 1/2
(||e + h|| >= 1/2), so ||e' - e - P_{e-perp}h|| <= 6||h||^2. QED.
A tiny contact mass delta at j (Delta = delta z_j e_j*) thus changes the first-order coefficient of a base part b by delta z_j <P_{e-perp}U*b, U*e_j*>/nu + O(delta^2):
this is the "mixed second-order term" delta t <P^perp U*e_j, P^perp U*B_t>/||U*a|| of the task (times t from tau b(xhat')).

## 2.6 Proposition (when the base mixed term is harmless). PROVED.
Let {B_tau} (tau in a set S of scales) be the base parts to be transferred, B_tau(zhat) = 0, sup ||B_tau||_1 < inf. Use at f' the base parts
B'_tau := B_tau - b_0(xhat') a' with ONE reference b_0 (so the represented direction is unchanged). The first-order term of a' + tau B'_tau is
tau (B_tau - b_0)(xhat') = tau (B_tau - b_0)(z' - z) + tau <U*(B_tau - b_0), e' - e>, and
 (a) finitely many pieces b_0..b_r: all first-order terms vanish iff the r scalar conditions (b_i - b_0)(xhat') = 0 hold (tuning);
 (b) any bounded family: {U*(B_tau - b_0)} is relatively compact (U* compact); with E_eta finite-dimensional, dist(U*(B_tau - b_0), E_eta) <= eta, tuning
     e' - e orthogonal to E_eta (dim E_eta conditions) leaves a U-part <= eta||e'-e|||tau| = O(eta s_1|tau|) <= eps_0 tau^2 on |tau| >= s_1 if eta <= eps_0/C;
     the z-part vanishes on the window (z' = z there except at tuning coordinates not charged by the B_tau) and beyond it is a tail.
*Proof.* Linearity, compactness, Cauchy-Schwarz. QED.
**Verdict (task question).** The base mixed term is NOT an obstruction: it is the variation of first-order coefficients, linear in the masses, and is
cancelled exactly (finitely many pieces) or up to eta (compact families) by finitely many scalar tunings, provided tuning moves with two-sided
(positively spanning) effects exist (P2x_part3 3.4). For two-piece data it reduces to the single condition per active block Delta d'_m = Delta d_m,
whose residue is exactly the Bregman excess (P2x_part3 Step 3). The obstructive mismatch is on the BLOCK side (Remark after 2.3).
