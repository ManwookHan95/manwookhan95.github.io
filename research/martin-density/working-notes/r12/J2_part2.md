# J2 part 2 (Round 12): the weak-peak pushes of Step 0 are dispensable -- Theorem J2.1

Setting and notation of J2_part1.md.  f^P := the row after the deep raise, (C1), (C2) and the preparation (P), WITHOUT the weak-peak pushes
(WP).  Pi := Step A's pre-placements (K2 5.2: pulls with compensating TU banks at the smallest admissible depth in [x, x'_max]; the D2
pushes of (U)-blocks and the lever pushes of (KN)-blocks, inward by eta' -- cert0 3.2 "one-shot moves first").

## 2.1 LEMMA J2.1 (frozen block system with a designated peak set).  PROVED.
Fix a block m of a row; Lambda_m := its coarse carriers (stage <= L), the others fine.  A FROZEN PATTERN is a nonempty P_f ⊂ Lambda_m with
zeta_k != 0 on P_f; Q_f := Lambda_m \ P_f.  For th > 0 put
   A_f(th) := sum_{k in P_f} (|zeta_k| - th Phi_k^2) + sum_{k fine} (|zeta_k| - th Phi_k^2)_+ ,
   B_f(th) := th^2 Phi_{P_f}^2 + sum_{k in Q_f} nu_k^2 Phi_k^2 + sum_{k fine} Phi_k^2 min(th, nu_k)^2 ,
   Psi_f(th) := A_f(th)^2 - B_f(th),   th_max := sup{th > 0 : A_f(th) > 0}.
(a) [existence, uniqueness]  On (0, th_max), A_f > 0 is strictly decreasing, B_f strictly increasing, so Psi_f is strictly decreasing; Psi_f
    tends to -B_f(th_max) < 0 at th_max.  Hence Psi_f has exactly one zero theta_f in (0, th_max) if Psi_f(0+) = (sum_{P_f} |zeta_k| + sum_{fine}
    |zeta_k|)^2 - sum_{Q_f} nu_k^2 Phi_k^2 > 0, and none otherwise.  Put A_f := A_f(theta_f) > 0.  (theta_f, A_f) are the FROZEN block scalars.
(b) [regularity]  (theta_f, A_f) are positively 1-homogeneous in zeta and locally Lipschitz; on every region where the signs of zeta on P_f are
    fixed and no fine carrier changes status they are C-infinity, and the first-order formulas of Lemma J2.0 hold with P := P_f ∪ {fine peaks},
    Q := Q_f ∪ {fine non-peaks}, theta := theta_f, Phi'^2 := Phi_{P_f}^2 + sum_{fine peaks} Phi^2 (so |d Psi_f/d th| = 2(A_f + th) Phi'^2 >=
    2(A_f + th) Phi_{P_f}^2).  Fine status changes make the scalars Lipschitz with constant <= C sum_{fine} Phi^2 <= C c_{L+1}.
(c) [consistency]  If nu_k >= theta_f for every k in P_f and nu_k <= theta_f for every k in Q_f, then theta_f = theta (the true threshold)
    and A_f = |zeta|_m.
(d) [frozen Lemma K]  Let Omega ⊂ Q_f, S_Omega := sum_{l in Omega} nu_l^2 Phi_l^2, kappa_f := A_f + (A_f^2 - S_Omega)/theta_f, r_l := u_l(xhat)/kappa_f,
    R^2 := m^2 sum_{Omega} r_l^2, a_f := A_f/theta_f, k_f := kappa_f/theta_f, sigma_f := (A_f^2 - S_Omega)/theta_f^2 = Phi'^2 + s_f with s_f :=
    theta_f^{-2} sum_{(Q_f \ Omega) ∪ fine non-peaks} nu^2 Phi^2.  Then
       a_f^2 = sigma_f + k_f^2 R^2,   k_f = a_f + sigma_f,   R < 1,   k_f = K(sigma_f, R^2),   rho^f_l := nu_l/theta_f = m |r_l| K(sigma_f, R^2)/Phi_l (l in Omega),
    kappa_f = A_f + theta_f Phi'^2 + theta_f s_f (U1's expression), and with fixed statuses
       d kappa_f/d|zeta_l| = rho^f_l s_f/(Phi'^2 (1 + a_f))  (l in Omega),      d kappa_f/d|zeta_p| = 1 - a_f s_f/(Phi'^2 (1 + a_f))  (p in P).
(e) [near-consistent rows]  Suppose that at the row the TRUE peak set of the block is P_f ∪ W', W' ⊂ Q_f with rho_k in [1, 1 + b] on W', every
    k in Q_f \ W' has rho_k <= 1, and 6 b Phi_{W'}^2 <= Phi_{P_f}^2, 2 b Phi_{W'}^2 <= a := A/theta, b <= 1.  Then Psi_f(0+) > 0, and
       theta (1 - 3b Phi_{W'}^2/Phi_{P_f}^2) <= theta_f <= theta,    |A_f - A| <= 4 b theta Phi_{W'}^2/Phi_{P_f}^2,
    so rho^f_k <= rho_k (1 + 6b Phi_{W'}^2/Phi_{P_f}^2) for every k, and |kappa_f - kappa(Omega)| <= C b theta Phi_{W'}^2/Phi_{P_f}^2, where
    kappa(Omega) := A + (A^2 - S_Omega)/theta is the formula-1 scalar with the TRUE A, theta (X1-ref K1).
Proof.  (a) On (0, th_max): the P_f-terms of A_f have derivative -Phi_k^2 < 0, fine terms <= 0, so A_f is strictly decreasing and positive;
B_f has derivative 2 th Phi_{P_f}^2 + (fine) > 0.  Hence A_f^2 is strictly decreasing and Psi_f strictly decreasing.  At th_max (finite, since
A_f(th) <= sum |zeta| - th Phi_{P_f}^2), A_f = 0 and Psi_f = -B_f < 0.  As th -> 0+, A_f -> sum_{P_f ∪ fine} |zeta_k| and B_f -> sum_{Q_f} nu^2 Phi^2
(fine terms min(th, nu)^2 -> 0).  Intermediate value theorem and monotonicity.
(b) Implicit function theorem for Psi_f(th; zeta) = 0 with d Psi_f/d th = -2 A_f Phi'^2 - 2 th Phi'^2 < 0 (derivatives as in Lemma J2.0's
proof, with the frozen sets in place of the true ones); 1-homogeneity: the equations are invariant under zeta -> c zeta, th -> c th, A -> c A.
Fine kinks: each fine term is Lipschitz in (zeta, th) with constant <= C Phi_k^2 nu-scale, summing to <= C sum_{fine} Phi^2.
(c) Under the hypothesis, for k in P_f: |zeta_k| - theta_f Phi_k^2 = (|zeta_k| - theta_f Phi_k^2)_+ and theta_f^2 Phi_k^2 = Phi_k^2 min(theta_f, nu_k)^2;
for k in Q_f: 0 = (|zeta_k| - theta_f Phi_k^2)_+ and nu_k^2 Phi_k^2 = Phi_k^2 min(theta_f, nu_k)^2.  So A_f(theta_f) = A(theta_f) and B_f(theta_f) =
B(theta_f) (Y2 Lemma T notation; fine terms identical), Psi(theta_f) = 0, and theta_f = theta by Y2 Lemma T(c) (unique zero); A_f = A(theta) =
|zeta|_m by Lemma T(b).
(d) A_f^2 = B_f(theta_f) = theta_f^2 Phi'^2 + sum_{Q_f ∪ fine non-peaks} nu^2 Phi^2, so A_f^2 - S_Omega = theta_f^2 sigma_f with sigma_f as stated.
nu_l Phi_l/theta_f = m |u_l(xhat)|/theta_f = m |r_l| k_f, so S_Omega/theta_f^2 = k_f^2 R^2 and a_f^2 = A_f^2/theta_f^2 = sigma_f + k_f^2 R^2; k_f = a_f +
sigma_f is the definition of kappa_f.  Since sigma_f >= Phi_{P_f}^2 > 0: a_f^2 > k_f^2 R^2 gives a_f > k_f R, and k_f > a_f then gives R < 1.  Eliminating a_f gives (1 - R^2) k_f^2 - 2 sigma_f k_f + sigma_f^2 - sigma_f = 0, whose admissible root (a_f > 0) is
K(sigma_f, R^2) (X1 Lemma K's algebra, X1-ref 1).  rho^f_l = nu_l/theta_f = m|r_l| k_f/Phi_l.  Derivatives: differentiate G1 := A - A_f(th) = 0,
G2 := A^2 - B_f(th) = 0 in |zeta_l| (l in Omega): dA + Phi'^2 dth = 0 and 2A dA - 2 th Phi'^2 dth - 2 nu_l = 0, so dth = -nu_l/(Phi'^2 (A + th)),
dA = nu_l/(A + th); then d kappa_f = dA + (2A dA - 2 nu_l)/th - (A^2 - S_Omega) dth/th^2 = (nu_l/(A + th))(sigma_f/Phi'^2 - 1) = rho^f_l s_f/(Phi'^2
(1 + a_f)).  For p in P (sign fixed): dA + Phi'^2 dth = 1, 2A dA - 2 th Phi'^2 dth = 0, so dth = A/(Phi'^2(A + th)), dA = th/(A + th) and d kappa_f =
(th + 2A)/(A + th) - sigma_f A/(Phi'^2 (A + th)) = 1 - a_f s_f/(Phi'^2(1 + a_f)).
(e) At th = theta: A_f(theta) = A - theta sum_{W'} (rho_k - 1) Phi_k^2 in [A - b theta Phi_{W'}^2, A] (the W'-terms leave A and contribute nothing
to A_f) and B_f(theta) = B(theta) + theta^2 sum_{W'} (rho_k^2 - 1) Phi_k^2 in [B, B + 3b theta^2 Phi_{W'}^2]; with A^2 = B(theta):
      -b theta Phi_{W'}^2 (2A + 3 theta) <= Psi_f(theta) <= 0.
Psi_f(0+) > 0: sum_{P_f} |zeta_k| = (A + theta Phi_P^2) - sum_{W'} |zeta_k| >= A + theta Phi_{P_f}^2 - b theta Phi_{W'}^2 and sum_{Q_f} nu^2 Phi^2 <=
A^2 - theta^2 Phi_{P_f}^2 + 3b theta^2 Phi_{W'}^2 (true identities A = A(theta), A^2 = B(theta)), so Psi_f(0+) >= 2A theta (Phi_{P_f}^2 - b Phi_{W'}^2) +
theta^2 (Phi_{P_f}^2 - 3b Phi_{W'}^2) > 0.  Since Psi_f(theta) <= 0, theta_f <= theta.  On [theta/2, theta], A_f(th) >= A_f(theta) >= A - b theta Phi_{W'}^2
>= A/2 (hypothesis 2b Phi_{W'}^2 <= a; at a clean sub-window a >= u Phi_min(L)^2 >> b by the alpha-mass identity and V1 Lemma D), so
|Psi_f'| = 2(A_f + th) Phi'^2 >= 2(A/2 + theta/2) Phi_{P_f}^2 = (A + theta) Phi_{P_f}^2 there; then Psi_f(theta/2) >= Psi_f(theta) +
(theta/2)(A + theta) Phi_{P_f}^2 >= theta[(A + theta) Phi_{P_f}^2/2 - b Phi_{W'}^2 (2A + 3theta)] > 0 (6b Phi_{W'}^2 <= Phi_{P_f}^2), so theta_f in
(theta/2, theta] and theta - theta_f <= |Psi_f(theta)|/((A + theta) Phi_{P_f}^2) <= 3 b theta Phi_{W'}^2/Phi_{P_f}^2.  |A_f - A| <= |A_f(theta_f) -
A_f(theta)| + |A_f(theta) - A| <= Phi'^2 (theta - theta_f) + b theta Phi_{W'}^2 <= 4 b theta Phi_{W'}^2/Phi_{P_f}^2.  Then rho^f_k = rho_k theta/theta_f <= rho_k/(1 - 3x) <= rho_k (1 + 6x), x := b Phi_{W'}^2/Phi_{P_f}^2 <= 1/6; the bound for kappa_f
follows (kappa(Omega) and kappa_f are the same expression in (A, theta) resp. (A_f, theta_f); A <= theta, A^2 - S_Omega <= 2 theta^2).  QED

## 2.2 The frozen convention with the TARGET pattern (precision to K2-ref K-8; PROVED)
(FC) For Step A (and for the Lojasiewicz start, 2.3) compute every block's scalars with the frozen pattern P_f(m) := P_rob(m) := the coarse
     peaks of f^r with rho >= 1 + u (at a clean sub-window every coarse peak has rho in [1, 1 + b] ∪ [1 + u, infinity); all moves before the end
     of Step A are << u, so P_rob is also the set of coarse peaks with rho >= 1 + u/2 along the construction); every other coarse carrier --
     in particular every weak peak, active or inactive, of every block -- is frozen as a NON-peak; fine carriers are computed truly.
     Omega := Q_f's coarse part (route V's Omega: all coarse non-peaks at the companion); kappa_f, r, rho^f as in Lemma J2.1(d).
Remark (why (FC) is the correct reading of K-8).  K2-ref K-8 freezes "the coarse peak set at f_1 + Pi" and then evaluates the frozen statuses
by Lemma K ("Lemma K is the frozen computation"), which needs Omega ⊂ Q_f.  Literally read, K-8 freezes as PEAKS the active weak peaks of (U)-
and (KN)-blocks, which Step 0 does not push (X1 2.6: (WP) only in (T)-blocks) and which Step A moves to rho <= 1 - eta' ((U)-blocks, X1-ref D1)
resp. below the lever margin ((KN)-blocks, U1-ref Prop. KN(b)): at the realized point such a frozen system would be inconsistent, Lemma
J2.1(c) would not apply, and the frozen scalars would not be the true ones.  With (FC) the frozen pattern IS the status pattern of the
companion (Q1 CM^tr(b): every coarse carrier of f^# is a peak with relative margin >= u/2 or a strict non-peak), so consistency at the
solution is exactly what Step A's targets provide (Step (iii) below).  This precision is needed for K2.15 itself, independently of Step 0.

## 2.3 THEOREM J2.1 (Step 0 without weak-peak pushes).  PROVED modulo the chain cited by Theorem K2.15 (K2-ref G).
Design T_fin^{K2} (unchanged; R-8(ii)'s enlarged (D1) is kept).  Let N >= 1, f in S_{p_N*} (base support F arbitrary), g in C(f), rho in (0,1).
DEFINITION (H2^flat) at a main stage L, clean sub-window w, class a (>= n(w)/D_cl(w) scales): there are admissible PRE-PUSHES Pi_0 -- any set of
moves admissible in (H1*) (K2-ref E), possibly EMPTY, of total size <= Design(L)^C b/u -- such that, with the Lojasiewicz/Puiseux steps 1-3 of
KN^tr started at the frozen ratio vector r_0 of f^0 := (deep raise, (C1), (C2), Pi_0, (P) applied to f in this order) and with Step A's
pre-placements Pi, Step A computed with (FC) is A-regular at f^0 + Pi in the sense of K2 5.2 (with K2-ref K-7's u-scaling W = Design^{C_A} u^{-3} max(x, ||b||)).
STATEMENT.  If (H2^flat) holds at infinitely many main stages, then (f, rho g) lies in the closure of NA((c_0, p_N), l_2^2) along norm-attaining
rows with FINITE base support; in particular (LSC-trunc)_N holds at (f, g, rho).  If it holds for every (g, rho), f is in Rec(p_N).
PROOF.  Fix a stage of the hypothesis; write f^0 := the row after the deep raise, (C1), (C2), Pi_0 and (P), in this order (Pi_0 takes the
place of (WP) in K2's order; f^0 = f^P when Pi_0 = {}).  Only (L1)-(L5) of J2_part1 1.4 involve (WP); we redo them at f^0.
Step (i) [Lojasiewicz start; (L1), (L2)].  Every block of f^0 satisfies the hypothesis of Lemma J2.1(e) with P_f = P_rob, b replaced by
b' := C Design(L) b (the moves (C1), (C2), (P), Pi_0 shift relative positions by <= C Design(L) b, so the coarse peaks outside P_rob have rho in
[1, 1 + b']) and W' := these peaks (6b' Phi_{W'}^2 <= Phi_{P_rob}^2 and 2b' Phi_{W'}^2 <= a since Phi_min(L)^2 >= 1/Design(L) and a >= u Phi_min(L)^2,
while b' << u/Design(L)^2; Psi_f(0+) > 0; P_rob != {} by V1 Lemma D).  [f-constants such as 1/A_min(f) are absorbed for L >= l_f.]  Let r_0 := (u_l(xhat_0)/kappa_f)_{l in Omega_a} with (FC).  The rate objects of the clean sub-window are
evaluated with the formula-1 ratios r(f) with the pattern's Omega (X1-ref K1).  Between f and f^0 values and block data move by: O(mu*_J)
(deep raise, K1-ref R-1), <= b per value ((C1), (C2), K1 2.1(a)), <= C D(L) theta_0 <= b ((P), K2 4.1(b)), <= Design^C b/u (Pi_0, by its
definition and K1-ref R-8); the frozen-versus-formula-1 difference is <= C b Phi_{W'}^2/Phi_{P_rob}^2 <= C Design(L) b relatively (Lemma J2.1(e)).
Ratios r_l = u_l/kappa are 0-homogeneous in the block vector and Lipschitz in these data with constant <= Design(L)^C (kappa >= theta sigma_rob;
the same Lipschitz bounds of the rate objects as in K1-ref R-8 and Q1-refa P-LIP).  Hence |r_0 - r(f)| <=
Design^C b/u, every tiny minor and cofactor polynomial is <= (1 + Lip C_*) Design^C b/u at r_0, and r_0 lies in the W-fix region K_kappa
(1 - R^2 >= sigma_f/2 >= sigma_rob/2 by Lemma J2.1(d), X1-ref W-fix).  The floor statuses: by Lemma J2.1(d) the frozen statuses satisfy Lemma
K with sigma_f >= sigma_rob and R^2 >= R_a^2, so (Lemma F, X1-ref 2, applied to the frozen system) F(r_0) = max_{d in N_T} psi_d(r_0)/Phi_d <=
max_{d in N_T} rho^f_d(f^0) <= (1 + b')(1 + 6b' Design(L)) <= 1 + Design(L)^2 b (Lemma J2.1(e), C absorbed in Design).  These are the inputs of KN^tr Steps 1-3 (X1-ref 8,
cert0 3.1), with the radius of R-8(ii)'s enlarged (D1) and (D2) (which allow Design^C b/u, C large); so Steps 1-3 give r'' in Z_kappa with
|r'' - r_0| <= eta', robust minors >= u/2 and F(r'') <= 1 - mu, mu := mu_kappa(eta'/3) (GEN_fin non-coincidence).  [This is cert0's C3 alternative,
now with the frozen convention.]
Step (ii) [realization; (L3)].  Under (H2^flat), Lemma K2.9(c) at f^0 + Pi with the (FC)-frozen map: K2.9(c)'s proof uses (1) the generators'
first-order actions (K2.4, K2.8(b) -- the chain rule for the frozen kappa_f, which is C^{1,1} by Lemma J2.1(b) with design constants: |d Psi_f/d th|
>= 2 theta_f Phi_{P_rob}^2, |zeta_p| >= theta_f Phi_p^2 on P_rob), (2) the C^{1,1} remainder ||Rem(t)|| <= C_2 ||t||^2 (+ C c_{L+1} ||t|| from fine status
changes, << rho_0/W as in K-8), (3) Brouwer on K = {t >= 0 : ||t|| <= W}.  None of these refers to true statuses.  It yields t* with Ft(f^0 + Pi +
G t*) = 0 for the frozen map: the frozen ratios of the active carriers are r'', the KN-1/P-HOLD carriers have value exactly 0, the (U)-block
targets are s_m r''_l kappa_f, the D2/KN-pushed carriers are at their pushed values, kappa_f floats.  Moves <= W <= Design^C x'_max << u; cost
<= C_f Design^C W log(1/W) = o(u^2 T^2) (K2 6.5).
Step (iii) [consistency => truth].  At the solution every block is (FC)-consistent: (T)-blocks: active near-threshold d (incl. the former
weak peaks): rho^f_d = m|r''_d| K(sigma_f, R^2)/Phi_d with R^2 = R_a(r'')^2 (holds exactly 0) and sigma_f = Phi_{P_rob}^2 + s_f, s_f <= C sum_{fine} Phi^2
<= C c_{L+1}^2 (route V: Omega = all coarse non-peaks), hence rho^f_d <= F(r'')(1 + C D^C c_{L+1}^2) <= 1 - mu/2 (c_{L+1}^2 << mu: X1-ref 8, S-0);
(U)-blocks: rho^f <= s_m(1 + Design^2 b + Lip eta') <= 1 - eta' (X1-ref D1, now from frozen statuses <= 1 + Design^2 b at the start; b << eta'/Design^2); (KN)-blocks: U1-ref
Prop. KN(b) margins; held carriers: value 0; D2/KN-pushed: rho^f <= 1 - c eta'; robust non-peaks: rho^f in [u/2, 1 - u/2]; P_rob: rho^f >= (1 + u)
(1 - 3b' Design)(1 - Design^C W/u) >= 1 + u/2.  So nu_k >= theta_f on P_f and nu_k <= theta_f on Q_f, and Lemma J2.1(c) gives theta_f = theta, A_f =
|zeta|_m in every block: the frozen solution is the TRUE companion f^(1a), with true ratios r'' on Z_kappa (kappa_f = kappa(Omega) at a consistent
point), true statuses as listed, and the Puiseux protection of KN^tr(b).  These are exactly the conclusions of K1 Lemma K1.6(A) used later.
Step (iv) [the rest; (L4), (L5)].  The order is now: deep raise -> (C1), (C2) -> Pi_0 -> classes (read off the decomposition data at f^r,
K1 1.3, so independent of Pi_0) -> (P) -> Lojasiewicz targets -> Pi -> Step A -> data -> s_1 -> N_w -> N'' -> Sys-DC -> approximant.  Lemma K2.13's classification along the construction holds with the
(WP) moves deleted (fewer moves) and Pi_0 of size <= Design^C b/u << u (as R-8 had for (WP)).  (L5): R-8(ii) is no longer needed when Pi_0 = {},
and is kept (it costs nothing).  The data (K1 Proposition K1.A with banked coordinates as in K2 4.1(c)), Sys-DC (Theorem K2.6 at the pre-row of
the companion), Theorem UE^inf (via Lemma DC^inf), and the averaging Theorem E^{eng,RT,inf} with K1-ref's (E-d) check are K2.15's Steps
verbatim: they act at f^r or at the companion, where every active near-threshold carrier is a strict non-peak with the Puiseux margin, and
none of them uses (WP) (J2_part1 1.4).  Costs: (WP) is not performed; Pi_0 costs as in (H1*) (K1-ref R-6 bounds).  QED

## 2.4 COROLLARY J2.2 (Theorem J2.1 contains Theorem K2.15).  PROVED.
(H1*) and (H2) at a stage imply (H2^flat) at that stage.  Proof: take Pi_0 := the (WP) moves given by (H1*).  Then f^0 is K2's row f_1 after (P) (same moves in the same order), the active weak peaks of the (T)-blocks are true
strict non-peaks there, the Lojasiewicz start is K2's r_1, and (FC) at f_1 + Pi coincides with K-8's freezing in the (T)-blocks (and corrects it in
(U)-, (KN)-blocks, 2.2).  So Step A in (H2^flat) with this Pi_0 is Step A of (H2).  QED

## 2.5 COROLLARY J2.3 (the residual class).  PROVED.
If (H2^flat) fails at all but finitely many main stages (every clean sub-window, every admissible class, every admissible Pi_0 -- in particular
Pi_0 = {}), then at each such stage Lemma K2.9(b) gives a near-certificate y at f^0 + Pi for the (FC)-frozen Sys-A, and Theorem K2.16
applies to it verbatim: its proof uses the identity (2.1) at the row, the first-order actions of the generators (K2.4, K2.8(b)), the Euler share
Xt_m <= 1/4 -- which holds for the frozen map because d kappa_f/d|zeta_l| = rho^f_l s_f/(Phi'^2 (1 + a_f)) <= 2 Design(L) sum_{fine} Phi^2 on Omega
(Lemma J2.1(d); route V: Omega = all coarse non-peaks, so s_f <= sum_{fine non-peaks} Phi^2 is fine only; rho^f_l <= 2; 1/Phi'^2 <= 1/Phi_{P_rob}^2 <=
Design(L)); this is U1 Lemma 1.4(c)'s X_m <= C c_{L+1}^2 D^2 for the frozen system -- and the four kinds of tuned carriers after (P); none of these
uses the true statuses of the weak peaks.  Hence the residual of K2 7.3 / K2-ref G is
      (A*) ∪ (U*) at f^0 + Pi (with (FC)), at all large main stages;
the class (W) / (W*) is EMPTY as a separate obstruction: a weak peak without a push resource is, in Step A, a tuned carrier of kind (iii) or
(iv) of K2.16 (one-sided resources of either orientation), exactly as after a hypothetical push.  (LSC-trunc)_N at (f, g, rho) therefore follows
from Theorem J2.1 as soon as Step A (with weak peaks frozen in Omega) is A-regular at infinitely many main stages.

## 2.6 Remarks (labels as stated)
(1) (PROVED) Why nothing is lost.  In the pushed version, Step A must still move every former weak peak from rho = 1 - b to a floor status
    <= 1 - mu with mu >= 8Mb ((D2)): the inward requirement on these rows was ALREADY part of (H2).  (WP) added a second, separate cone condition at
    the scale b with its own feedback analysis (K2-ref W-1: Sherman-Morrison denominators 1 - h_W^T g_W of (P4)/shared pushes).  After the merge
    that feedback is part of Sys-A's linearization J_A = [I - gtil h^T | col_c] (K1 2.4), which Theorem K2.16 already analyzes; and Step A's
    resources include the ratio/threshold lever (two-sided buffer-peak resources, floating kappa), which (WP) as formulated did not use.
(2) (PROVED) The "keep the weak peak as a peak" alternative (Y2 Lemma U' kind [3]) does not help: kind [3] admits inward data only at
    DEGENERATE peaks (alpha(k) = 0, i.e. rho_k = 1 exactly) or strict non-peaks; making a weak peak (rho in (1, 1 + b]) degenerate is an exact
    inward push of the same orientation, and route V's threshold protection (Lemma K, Puiseux margins of N_T) requires the active
    near-threshold carriers to be strict non-peaks at the companion anyway (X1-ref 8(b), Q1 CM^tr(b)).
(3) (PROVED) Data signs (J2_part1 1.3) play no role in Theorem J2.1.
