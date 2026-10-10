# V3 notes (Round 7): item (E) of ADDENDUM 6 -- infinite base support
Part files: r7/V3_part1.md (critical obstruction revisited), V3_part2.md (raise transfer, Theorem E_RT), V3_part3.md (Theorem RS),
V3_part4.md (fixed data, master principle, residuals, numerics). This file supersedes them where they differ.
Script: r7/V3_work/rt_check.py. References: the note paper/martin_density_note.tex ("the note"); r6/Y3_notes.md, Y3_ref_notes.md ("Y3",
"Y3_ref"); r5/Z5_ref_notes.md ("R1" = its Theorem R1, "R2" = its Lemma R2); r5/Z3_notes.md (Theorem E, Lemma 3.1); r6/Y4_ref_notes.md.
Setting: T admissible, I finite (p = p_N; Lemma lem:martintail passes to Martin's p for one N-independent design), f in S_{p*} with forced
data (xi, q_0, a, w, F, z, zhat, e, nu), F = supp a possibly infinite, s_j := sgn a_j (j in F), s(t) := sqrt(1 + t^2).
Labels: PROVED / SKETCH / HEURISTIC / OPEN / FALSE.

## 0. Summary

| # | Result | Scope | Status |
|---|---|---|---|
| 1 | Per-coordinate structure of decompositions on a support-swallowed signature set; the referee's factor 2 belongs to R1's deep assignment, copied data lose only the scale oscillation of the flip coefficient (exact model: [4/3, 3/2]) | D_sigma | PROVED (1.1, 1.2) |
| 2 | Raise transfer lemma (RT): a same-sign raise of a on F transfers every decomposition of f to the raised row f^# with zeroth-order error 2 norm(U* Delta a) + p*(L*(w^# - w)) only -- NOT the raise mass | any T, any F | PROVED (2.3) |
| 3 | Theorem E_RT: windowed recovery through companions with the decoupling condition on that transfer error instead of p*(f_j - f) | any T, any F | PROVED (2.5) |
| 4 | Design D^mu: any SLD-type design over a diagonal base with fast-decaying entries mu_s; raise room (RR); value-preserving raises (Lemma VP) | design | PROVED (3.1-3.3) |
| 5 | **Theorem RS**: support swallowing of ANY profile (sparse, critical, super-critical, mixed), any number of finitely many bad carriers, non-d-neutral, off-F/shared targets, absorbing contacts: f in Rec under (W*), (H2), (H3'), (B_fin), (ND_B), (RR_B). Resolves (O4-crit) and the support part of (O4-nd) | D^mu | PROVED (with inspection items I1-I3) |
| 6 | Theorem A: fixed d-neutral two-piece data at infinite F need NO cushion sparsity (only (RR_W), (ND)) | D^mu | PROVED (4.1) |
| 7 | Master principle at infinite F (raised + exactified companions); infinite-F versions of R1, Z4 Thm A, Y1 Master Thm, Y2 Thm Y | D^mu | reduction PROVED; transport of Y1/Y2 SKETCH (4.3) |
| 8 | (O4-box): raises give box domination only on the deep part; thin shallow support remains | D^mu | SKETCH/OPEN (4.4) |
| 9 | Residuals: mu-thin supports, (O4-box), non-d-neutral fixed data ((SC) at raised rows), degenerate (ND)/(H3-inf), finite-F core | -- | OPEN (4.5) |

Bottom line. The critical obstruction is not structural: at a RAISED companion (|a_s| increased, signs kept, on the coordinates of F
where the bad profile is active at the window scale) the critical flips disappear, and for a diagonal base with fast-decaying entries the
raise costs nothing at second order, although its l_1-mass ~ y m_B(y) is of the order of the window scale squared (or larger). The point is
that a same-sign raise commutes with the triangle inequality; only its Hilbert-part footprint ||U*Delta a|| and the induced normer change
enter, and both are super-polynomially small when U* is small on the raised coordinates -- and U is ours to choose. No counterexample
mechanism was found; leaning positive. Density remains OPEN (finite-F core (A)-(D), (O4-box), mu-thin supports).

## 1. The critical obstruction revisited (D_sigma; superseded by Section 3 for the recovery question)

1.1 Lemma (per-coordinate structure; PROVED). Let l be a support-swallowed carrier (S_l subset F up to finitely many points) and (B_pm, Theta_pm)
a two-sided decomposition at scale t. For s in S_l beyond max supp of the finitely many coarser targets,
  eps B_pm(s) = (gamma_s - theta_pm) v_l(s) + r_pm(s),  gamma_s := eps g_s/v_l(s),  theta_pm := eps lambda_l Theta_pm(k(l)),
|r_pm(s)| <= (4/t) sum{c_{l'} : l' > l, s in supp y_{l'}} <= (2/t) 2^{-2s} c_l delta_l.
Proof. On S_l only u_l (value v_l(s) = delta_l 2^{-s}/n_l) and finer targets are nonzero (allowedness (a), disjointness); box bound |t Theta(k')| <= 3,
lambda_{l'} <= c_{l'}/4, allowedness (b): 2c_{l'} <= 2^{-2s}c_l delta_l, sum over l' >= L(s) of c_{l'} <= (4/3)c_{L(s)}. QED
Consequence. The split of the switching between the two sides at s is p_s = (theta_+ - gamma_s)/(theta_+ - theta_-) up to a fraction
O(c_l/delta_l) of the cushion |a_s|/t ~ v_l(s)^2/t: it is fixed by two numbers and the profile of g, not free per coordinate. The referee's
lower bound Fdec(t) (cushions of both sides used optimally per coordinate) and the certified excess (1-2p)^2 Phi/8 describe R1's DEEP
ASSIGNMENT (+ side at its full allowance, all flips on the - side); data that copy (B_pm) on the deep set pay at scale r the same function
r -> Exc_beta(r)/r^2 (beta = (theta_+ - gamma)_+ v_l) as the decomposition, evaluated at another scale.

1.2 Exact model (PROVED, computation). v_s = c 2^{-s}, |a_s| = v_s^2, beta = D v: Exc_beta(r) = Exc_v(rD) and Phi(x) := Exc_v(x)/x^2 is
log-periodic with Phi(v_s(1+u)) = 2(2/3 + 2u)/(1+u)^2, u in [0,1]: min 4/3 (u in {0,1}), max 3/2 (u = 1/3). (m_v(y) = 2v_s on (v_s, 2v_s];
int_0^{v_s} m_v = 2v_s^2/3.) So copied data lose at most the factor 9/8 on the flip share; with a single phase variable (one critical
carrier, gamma constant on the deep part) a crossing argument even selects loss-free "upper" scales (HEURISTIC), while two critical
populations with routing freedom can lose a constant for every fixed or window-averaged datum (HEURISTIC model). Section 3 makes all this moot.

1.3 Remark (one-step rho-bootstrap is impossible; PROVED). If f_n -> f then every limit of g_n in C(f_n) lies in C(f) (thm:compact). Hence if
g in C(f) has gauge 1 (t g notin C(f) for t > 1), no sequence f_n -> f has (rho/rho_0) g in Li C(f_n) for rho > rho_0: a rho-threshold result
rho_0 C(f) subset {g : (f,g) in cl NA} cannot be bootstrapped by transitivity at nearby rows unless the threshold constant itself improves.

## 2. Raise companions (any admissible T, any F)

2.0 Definition. A RAISE is Delta a in l_1 with supp Delta a subset F and s_j Delta a_j >= 0. Put lambda := q*(a + Delta a), a^# := (a + Delta a)/lambda
and let f^# be the first row with forced data (a^#, z) (Remark rem:lemmaZ(c): e^# := U*a^#/||U*a^#||, zhat^# := z + Ue^#,
q_0^# := (1 + sum_m |R_m** zhat^#|_m)^{-1}, xi^# := q_0^# zhat^#, w^# := J_V(L** xi^#), f^# := a^# + L*w^#; admissible since supp a^# = F and
sgn a^# = z on F). F, K, J, rooms, bad set and swallowing signs are those of f. ("Monotone moves" may also put masses of sign z_j on
contacts j in K; everything below holds verbatim.)

2.1 Lemma (PROVED). (a) 1 + ||Delta a||_1 - ||U*Delta a|| <= lambda <= 1 + ||Delta a||_1 + ||U*Delta a||; so lambda >= 1 if ||U|| <= 1.
(b) ||e^# - e|| <= 2||U*Delta a||/nu. (c) |u(zhat^#) - u(zhat)| <= ||U*u|| ||e^# - e|| (u in l_1); ||zhat^# - zhat||_inf <= ||U|| ||e^# - e||.
(d) ||a^# - a||_1 <= 2||Delta a||_1 + ||U*Delta a||, and f^# -> f in norm as ||Delta a||_1 -> 0.
Proof. (a) Same signs on F: ||a + Delta a||_1 = ||a||_1 + ||Delta a||_1; ||U*a|| -+ ||U*Delta a|| bound ||U*(a + Delta a)||; q*(a) = 1.
(b) Scale invariance of e^# and ||x/||x|| - y/||y|| || <= 2||x - y||/||y||. (c) zhat^# - zhat = U(e^# - e), u(Uh) = <U*u, h>.
(d) a^# - a = Delta a/lambda + (1/lambda - 1)a, |1/lambda - 1| <= lambda - 1. Convergence: proof of Proposition prop:approximants ((ii) => (i)),
which uses only a^# -> a in l_1 and z fixed (Remark rem:lemmaZ(c)). QED

2.2 Lemma (normer change; PROVED). With delta := zhat^# - zhat, eps_e := ||U|| ||e^# - e||, Delta_m := sum_k lambda_{k,m}|u_{k,m}(delta)| <= m2^{-m} eps_e:
if max_m Delta_m <= c_f then |q_0^# - q_0| + |sigma^#_m - sigma_m| + |C^#_m - C_m| <= C_f eps_e and
  p*(L*(w^# - w)) <= (1 + ||U||) sum_m ||R_m*(w^#_m - w_m)||_1 <= C'_f eps_e log(e/eps_e).
Proof. Z3 Lemma 3.1 (refereed): its proof uses only the clamp formula at zhat and zhat^# (v_k = m|u_k(zhat)|/|R** zhat|), never the base
parts, and gives sum_m ||R_m*(w^#_m - w_m)||_1 <= C_f c(delta), c(delta) = sum_m [Delta_m log(e/Delta_m) + sum_k min(lambda_k, |u_k(delta)|)];
|u_k(delta)| <= ||U*u_k|| ||e^# - e|| <= eps_e (q*(u_k) = 1) and sum_k min(lambda_{k,m}, x) <= x(log_2(2m/x) + 3). p* <= q* <= (1+||U||)||.||_1. QED

2.3 Lemma (raise transfer, RT; PROVED). If lambda >= 1, then for every h in X* and r in R
  p*(f^# + r h) <= 1 + (p*(f + lambda r h) - 1 + 2||U*Delta a||)/lambda + p*(L*(w^# - w)).
Proof. Lemma lem:dualball: f + lambda r h = A + L*W with max(q*(A), ||W||) = pi := p*(f + lambda r h). For r != 0 put B := (A - a)/(lambda r),
Theta := (W - w)/(lambda r); then h = B + L*Theta and
  f^# + r h = (a^# + rB) + L*(w + r Theta) + L*(w^# - w).
Base: q*(a + Delta a + lambda r B) <= q*(A) + q*(Delta a) = pi + ||Delta a||_1 + ||U*Delta a|| <= pi + (lambda - 1) + 2||U*Delta a|| (2.1(a)), and
q*(a^# + rB) = q*(a + Delta a + lambda r B)/lambda. Blocks: w_m + r Theta_m = (1 - 1/lambda)w_m + (1/lambda)W_m, so N_m(w_m + r Theta_m) <=
1 + (pi - 1)/lambda. By Lemma lem:dualball, p*((a^# + rB) + L*(w + r Theta)) <= 1 + (pi - 1 + 2||U*Delta a||)/lambda; add p*(L*(w^# - w)). QED
Remark. No smallness of ||Delta a||_1 is needed: a same-sign raise on F commutes with the triangle inequality. Corrections Delta a'' of
arbitrary sign on a finite set F_0 disjoint from supp Delta a, with |Delta a''_s| <= |a_s|/2, add 2||Delta a''||_1 to the error (same proof:
||a + Delta||_1 >= ||a||_1 + ||Delta a||_1 - ||Delta a''||_1).

2.4 Corollary (PROVED). For g in C(f), rho in (0,1] and lambda >= 1: p*(f^# + r rho g) <= 1 + (s(lambda rho r) - 1)/lambda + eps' for all r, with
eps' := 2||U*Delta a|| + p*(L*(w^# - w)); and (s(lambda x) - 1)/lambda <= s(x) - 1 + (lambda - 1)min(lambda^2 x^2/2, 1).
Proof. 2.3 with h = rho g, pi <= s(lambda rho r). phi(lambda) := (s(lambda x) - 1)/lambda has phi' = (s(u) - 1)/(lambda^2 s(u)) (u = lambda x),
0 <= (s(u) - 1)/s(u) <= min(u^2/2, 1); integrate over [1, lambda]. QED

2.5 Theorem E_RT (windowed recovery through companions with transfer error; PROVED). Let f in S_{p*} (F arbitrary), g in C(f), rho in (0,1),
eta_0 in (0,2] with rho^2(1 + eta_0) <= (1 + rho^2)/2. Suppose there are first rows f_j, lambda_j >= 1, eps'_j >= 0, c_flat,j in (0,1] and windows
(T_j, n_j, K_j), T_j in (0,1], n_j in N, K_j >= 0, with:
 (a) p*(f_j + r rho g) <= 1 + (s(lambda_j rho r) - 1)/lambda_j + eps'_j for all r;
 (b) for t in S_j := {T_j 2^{1-i} : 1 <= i <= n_j} functionals g_{j,t} with p*(g - g_{j,t}) <= K_j t and p*(f_j + r rho g_{j,t}) <= 1 + (rho^2 r^2/2)(1 + eta_0)
     for 0 < rho|r| <= c_flat,j t;
 (c) K_j T_j -> 0, n_j >= 48 rho^2 K_j/(c_flat,j (1 - rho^2)), lambda_j -> 1, p*(f_j - f) -> 0;
 (d) eps'_j <= theta_j c_flat,j^2 (T_j 2^{-n_j})^2 with theta_j -> 0;
 (e) for every j: rho gbar_j in C(f_j) implies (f_j, rho gbar_j) in cl NA, where gbar_j := (1/n_j) sum_{t in S_j} g_{j,t}.
Then (f, rho g) in cl NA((c_0,p), l_2^2).
Proof. Fix r_0 in (0,1], r_0^2 <= 1 - rho^2; take j large with theta_j rho^2 <= (1-rho^2)/48, (lambda_j - 1)(1 + lambda_j^2) <= (1-rho^2)r_0^2/48,
eps'_j <= (1-rho^2)r_0^2/48, 2 rho K_j T_j/n_j <= (1-rho^2)r_0/48. For t in S_j: (A) if rho|r| <= c_flat,j t, p*(f_j + r rho g_{j,t}) <= 1 + (rho^2 r^2/2)(1 + eta_0);
(B'') always, p*(f_j + r rho g_{j,t}) <= p*(f_j + r rho g) + rho|r|K_j t <= s(rho r) + (lambda_j - 1)min(lambda_j^2 rho^2 r^2/2, 1) + eps'_j + rho|r|K_j t
(Corollary 2.4). Convexity: p*(f_j + r rho gbar_j) <= (1/n_j) sum_t p*(f_j + r rho g_{j,t}).
|r| <= r_0: let I_r := {t : c_flat,j t < rho|r|}, so sum_{I_r} t < 2 rho|r|/c_flat,j. If I_r is empty, every term is <= 1 + (rho^2 r^2/2)(1 + eta_0)
<= 1 + r^2(1 + rho^2)/4 <= s(r). Otherwise rho|r| > c_flat,j T_j 2^{1-n_j}, so eps'_j < theta_j rho^2 r^2 <= (1-rho^2)r^2/48; also
(lambda_j - 1)lambda_j^2 rho^2 r^2/2 <= (1-rho^2)r^2/48 and (1/n_j) sum_{I_r} rho|r|K_j t <= 2 rho^2 K_j r^2/(c_flat,j n_j) <= (1-rho^2)r^2/24. Hence
p*(f_j + r rho gbar_j) <= max{1 + r^2(1+rho^2)/4, s(rho r)} + (1-rho^2)r^2/12 <= s(r), by 1 + r^2(2+rho^2)/6 <= 1 + r^2/2 - r^4/8 <= s(r)
(r^2 <= 1-rho^2) and s(r) - s(rho r) >= (1-rho^2)r^2/3 (Lemma lem:slack(a), |r| <= 1).
|r| > r_0: (B'') for every t: the extra terms are <= (1-rho^2)r_0^2/48 + (1-rho^2)r_0^2/48 + (1-rho^2)r_0|r|/48 <= (1-rho^2)r_0|r|/16
<= (1-rho^2)min(r^2,|r|)/16, and s(r) - s(rho r) >= (1-rho^2)min(r^2,|r|)/3.
So rho gbar_j in C(f_j), p*(rho gbar_j - rho g) <= 2 rho K_j T_j/n_j; by (e) and (c), (f, rho g) is a limit of points of cl NA. QED
Remarks. (i) eps'_j := p*(f_j - f), lambda_j := 1 recovers Z3 Theorem E (at arbitrary F; (a) by the triangle inequality). (ii) For raised rows
(Cor. 2.4) eps'_j involves only ||U*Delta a_j|| and the normer change, not ||Delta a_j||_1. (iii) K_j = 0, n_j = 1 is allowed.

## 3. The designed base, raise room, Theorem RS

3.1 Design D^mu (PROVED). H := l_2 with orthonormal basis (k_s), U k_s := mu_s e_s with mu_s in (0, 1/2], mu_s -> 0 (recommended
mu_s := 2^{-s^2-1}). U is compact with dense range (range contains c_00), ||U|| <= 1/2, U*e_s* = mu_s k_s, q*(a) = ||a||_1 + (sum mu_s^2 a_s^2)^{1/2}.
SLD, SLD_G, D_sigma, D''', D_X, D^PW and D^Y are defined over any compact dense-range base and use U only through
delta_l = min{2^{-l}, (4(1 + ||U||)||h_l||_1)^{-1}} (and Y4's diagonal-base statements); hence over this base they remain admissible, N-free,
and all their theorems hold. "D^mu" denotes any of them over this base.

3.2 Raise room. For W in l_1, W >= 0: M_mu^W(y) := sum{mu_s W_s : s in F, |a_s| < y W_s};  (RR_W): M_mu^W(y) = O(y^{1+eps}) for some eps > 0.
Lemma 3.1 (PROVED). (a) (RR_a): |a_s| >= c_a mu_s^{1/(1+eps)} on F implies (RR_W) for every W in l_1. (b) For mu_s = 2^{-s^2-1}, (RR_W) holds if
log_2(W_s/|a_s|) <= (1 - eps')s^2 for large s in F cap supp W; for W = U_B (U_B(s) := sum_{l in B}|u_l(s)|) this covers every power-law
swallowing profile |a_s| ~ v_l(s)^{1+b}, b > 0 (sparse b < 1, critical b = 1, super-critical b > 1, and mixtures).
Proof. (a) |a_s| < yW_s gives mu_s < (y||W||_inf/c_a)^{1+eps}; sum <= ||W||_1(y||W||_inf/c_a)^{1+eps}. (b) Active s have 2^{-(1-eps')s^2} < y,
so mu_s < y^{1/(1-eps')}; M <= ||W||_1 y^{1/(1-eps')}. For power laws log(v_l(s)/|a_s|) = O(s). QED
(RR) is not a cushion condition: (CS_W) [m_W(y) = sum{W_s : |a_s| < yW_s} = o(y)] fails for critical and super-critical profiles; (RR) fails
only for mu-thin supports (|a_s| below a power of mu_s on infinitely many active coordinates).

3.3 Lemma VP (value-preserving raises; PROVED). Let L_0 be a finite set of carriers, gamma_k := <U*u_k, U*a>, and assume
 (ND_{L_0}) Lambda: l_1(F) -> R^{L_0}, Lambda(x)_k := sum_{s in F} mu_s^2 x_s (u_k(s) - a_s gamma_k/nu^2), is onto.
Then there are a finite F_0 subset F and c_0, C_0 > 0 such that for every raise Delta a with supp Delta a cap F_0 empty and ||U*Delta a|| <= c_0
there is Delta a'' in l_1(F_0), ||Delta a''||_1 <= C_0||U*Delta a||, |Delta a''_s| <= |a_s|/2, for which the row f^# with forced data
((a + Delta)/q*(a + Delta), z), Delta := Delta a + Delta a'', has u_k(zhat^#) = u_k(zhat) for all k in L_0. (Lemma 2.3 holds with the extra
error 2||Delta a''||_1; lambda >= 1 once ||Delta a''||_1 + ||U*Delta|| <= ||Delta a||_1.)
Proof. Choose F_0 finite with Lambda(l_1(F_0)) = R^{L_0}. G(x)_k := <U*u_k, e(x) - e>, e(x) := U*(a + Delta a + x)/||U*(a + Delta a + x)||
(x in l_1(F_0)) is C^infinity near 0 with bounded second derivatives; DG(x)xi = <U*u_k, P^perp_{e(x)}U*xi>/||U*(a + Delta a + x)||, which at
Delta a = 0, x = 0 equals Lambda(xi)_k/nu (diagonal U), onto on l_1(F_0), hence uniformly onto nearby; |G(0)| <= 2||U||^2||U*Delta a||/nu
(2.1(b),(c)). Graves' theorem gives G(x) = 0 with ||x||_1 <= C_0||U*Delta a||; F_0 finite fixed gives |x_s| <= |a_s|/2 for c_0 small. QED
Remark. (ND) fails iff some nontrivial u = sum c_k u_k has u|_F = kappa a|_F; then sum c_k val_k drops by kappa nu||e^# - e||^2/2 under every move
on F (second order). On deep signature coordinates this forces |a_s| proportional to v_l(s), a cushion-dominated profile. (ND) is generic.

3.4 Theorem RS (support swallowing of any profile). Design D^mu over the SLD operator (or D_sigma), N >= 1. Let f in S_{p_N*} (F arbitrary)
satisfy R1's (W*), (H2), (B_fin) and
 (H3') no bad carrier sits at a degenerate peak;  (ND_B);  (RR_B) := (RR_{U_B}).
Then f in Rec. Status: PROVED, with three inspection items (I1)-(I3) of the same kind as Z3 Lemma U / Y4 Lemma P2 (checked below).
[Removes R1's (CS_B); removes Y3 Theorem 3.5's d-neutrality, supp u_l subset F, monochromatic sign, (QM) and super-criticality, and the
rho-threshold of Y3_ref Prop. 3.4; covers non-d-neutral carriers, off-F and shared targets and absorbing contacts.]
Proof. Fix g in C(f), rho in (0,1); eta_0, kappa_0, eps_tr, eta as in R1. Let C_tau (bounded switching, R1 Step 2'), K* and
K_j := (1 + ||U||)K^R_2(l_j) (R1), c_flat, t_1 (R1 Step 4) be R1's constants at f, with a factor 2 of room.
Step 1 (windows). (W*) gives l_j -> infinity with Lambda*_f(l_j)/(l_j 2^{l_j^3}Lambda°(l_j)) -> 0. Put n_j := ceil(48 rho^2 K_j/(c_flat(1 - rho^2))) and
choose T_j with S_j := {T_j 2^{1-i} : i <= n_j} subset W(l_j) and C(4C_tau T_j)^{eps} log(1/T_j) <= theta_j c_flat^2 4^{-n_j}, theta_j -> 0: possible
because n_j = O(Lambda*_f(l_j)) = o(n^w_{l_j}), so T_j := T_hi(l_j)2^{-m_j} with m_j := ceil((2/eps)(2n_j + log_2(C/(theta_j c_flat^2)))) + 1 keeps
m_j + n_j <= n^w_{l_j}. All smallness conditions of R1 hold on W(l_j) for large j (as in R1 Step 5).
Step 2 (companion). y_j := 4C_tau T_j. Raise along U_B at level y_j: Delta a_s := s_s(y_j U_B(s) - |a_s|)_+ (s in F); then the Lemma VP correction
for L_0 := B; f_j := the resulting row. Then ||Delta a||_1 <= y_j m_B(y_j) -> 0 (the l_1-mass is ~ kappa y_j^2 for critical, >> y_j^2 for
super-critical profiles -- never o(T_lo^2) -- which is irrelevant here), lambda_j - 1 <= 2y_j||U_B||_1, ||U*Delta a|| <= y_j M_mu^{U_B}(y_j), and by
2.2, 2.4, 3.1, 3.3: eps'_j := 2||U*Delta|| + 2||Delta a''||_1 + p*(L*(w_j - w)) = O(y_j^{2+eps} log(1/y_j)) <= theta_j c_flat^2 (T_j 2^{-n_j})^2 (Step 1),
p*(f_j - f) -> 0, and:
 (i) |a^{(j)}_s| >= y_j U_B(s)/lambda_j >= 2C_tau T_j U_B(s) on F;
 (ii) val_l := u_l(zhat) unchanged for l in B; block scalars move by O(eps_e); z, F, K, J, rooms, B, eps_l unchanged. Since q_l = eps_l q_0 val_l/sigma_m
      for a strict non-peak (Lemma lem:threshold: w_m(k) = C_m m q_0 val_k/(Phi_m(k)sigma_m)), the cone Z_f of lem:exactswitch [rows tau_l >= 0
      (l in B_K), target rows on T_0, peak rows, d-rows sum_{m(l)=m} eps_l val_l tau_l = 0] is the same at f_j, with the same Hoffman constant;
      gaps of bad strict non-peaks and margins of bad and (H2) peaks are f-constants, so statuses are unchanged for large j ((H3')).
Step 3 (approximate decompositions at f_j). g_j := g - (g(xi_j)/q_0^{(j)})a^{(j)}, |g(xi_j)| <= ||g||_1||xi_j - xi||_inf = O(eps_e). By Cor. 2.4,
p*(f_j + t g_j) <= 1 + (t^2/2)(1 + eta'_j) on [T_j 2^{-n_j}, T_j], eta'_j -> 0, g_j(xi_j) = 0. (I1) Lemmas lem:twosided, lem:smallness,
lem:budget, lem:suplevel, lem:box, lem:switchbudget, lem:modswallow, lem:badpeaks hold at f_j with s(t) - 1 replaced by (1 + eta'_j)t^2/2:
they use the budget only through s(t) - 1 <= t^2/2 and g(xi) = 0 (constants change by factors <= 2); lem:smallness by compactness of
(f_j, t) -> (f, 0).
Step 4 (exact window data at f_j). R1 Steps 1-3 at f_j: by (ii) the projected switching tau' lies in Z_{f_j} = Z_f with sum|tau - tau'| <= C_f K* t, and
(I2) |tau'_l| <= C_tau (the injectivity modulus of c -> (P^perp_{e_j}U* sum_B c_l u_l, (sum_B c_l u_l)(zhat_j)) in Z5 Lemma 5.2 is continuous in
(e_j, zhat_j)). So |X_s| <= C_tau U_B(s) <= 4|a^{(j)}_s|/t = 2A^{(j)}_s for t <= T_j by (i): R1's deep set D_t is EMPTY. Claim 3.2 of R1 gives
d-neutral two-piece data AT f_j for g_{j,t} with (s b^+)_-, (s b^-)_+ <= 3|a^{(j)}|/t and |b^theta| <= 4|a^{(j)}|/t on F, p*(g_j - g_{j,t}) <= K_j t,
Gamma_w <= (1 + 2kappa_0)^2 = 1 + eta_0/2, and R2's block size conditions.
Step 5 (pieces). (I3) Lemma R2 at f_j with U_* = 0: p*(f_j + r g_{j,t}) <= 1 + (r^2/2)(1 + eta_0) for 0 < |r| <= c_flat t (side by side), with c_flat, t_1
independent of j (R2's constants depend on f_j through nu, q_0, sigma_m, C_m, M_m, the transfer data of lem:persistence and the cushion bound,
all uniform along f_j -> f).
Step 6. Theorem 2.5: (a) by Cor. 2.4 (p*(g - g_j) = O(eps_e) absorbed into eps'_j and K_j); (b) Steps 4-5; (c), (d) Steps 1-2; (e): the averaged data
are d-neutral two-piece data at f_j for gbar_j with kappa_w <= 1 + eta_0/2 and side parts <= 4|a^{(j)}|/T_lo, so (CS-side) holds at f_j
(m(x) = 0 for x < T_lo/4); Y3 Theorem 2.1 at f_j (I_- empty) applied to the mate rho gbar_j with data rho Dbar_j (kappa_w < 1) gives
(f_j, rho' rho gbar_j) in cl NA for all rho' < 1, hence (f_j, rho gbar_j) in cl NA. So (f, rho g) in cl NA; let rho -> 1. QED
Remarks 3.5. (a) Why Y3/Y3_ref's negative arithmetic does not apply: Y3 3.5(i) and Y3_ref 3.3 correctly show that a companion making the
switching cushion-compatible on a window costs l_1-mass ~ kappa D^2 T^2, too much for Z3 Theorem E's decoupling p*(f_j - f) = o(T_lo^2);
Theorem 2.5 needs only eps'_j = o(T_lo^2), and for a same-sign raise on F eps'_j is controlled by ||U*Delta a||. (b) The cushion-sharing factor 2
(Y3_ref 3.2) is a property of deep assignment; at f_j the deep set is empty. (c) (H3') -> R1's (H3-inf) (B_K carriers at degenerate peaks of
sign -eps_l): their status at f_j may move by O(eps_e), but lem:badpeaks(c) uses only the box inequality at k(l), which survives a margin or gap
O(eps_e) << t^2 (SKETCH). (d) (ND_B) can be dropped if the second-order drift of the degenerate combination is handled by Hoffman stability of
Z_f (SKETCH). (e) The theorem is per first row: all mates of f are recovered; with lem:martintail it holds for Martin's p over D^mu.

## 4. Fixed data, master principle, residuals

4.1 Theorem A (fixed d-neutral data without cushion sparsity; PROVED). T admissible over D^mu, I finite, f in S_{p*} (F arbitrary), g in C(f) with
d-neutral two-piece data (b^pm, omega^pm) at f (def:twopiece at arbitrary F), rho^2 kappa_w < 1. Put W := (sb^+)_- + (sb^-)_+ + |b^theta| on F,
L_0 := the carriers in supp omega^+ u supp omega^-. If (RR_W) and (ND_{L_0}) hold, then (f, rho g) in cl NA. [Y3 Theorem 2.1 needs (CS-side).]
Proof. For y -> 0, f_y := raise along W at level y plus the VP correction for L_0; T := y/4. (1) For omega supported in L_0 cap Q_m,
d_m(omega) = (m q_0/sigma_m) sum_k Phi_m(k) val_k omega(k); values of L_0 are preserved and their gaps are f-constants, so
d^{(y)}_m = (q_0^{(y)}sigma_m/(q_0 sigma^{(y)}_m)) d_m on these vectors: the data are d-neutral at f_y and b^+ - b^- = sum_m R_m*(omega^-_m - omega^+_m) is the
consistency relation at both rows; after the common shift b^pm -> b^pm - kappa_y a^{(y)} (kappa_y := G_y(xi_y)/q_0^{(y)}) they are two-piece data at f_y
for g_y with p*(g - g_y) = O(eps_e). (2) (s b^+)_-, (s b^-)_+ <= W <= lambda|a^{(y)}|/y <= 3|a^{(y)}|/t for t <= T; Lemma R2 at f_y (U_* = 0) gives
p*(f_y + r g_y) <= 1 + (r^2/2)(Gamma^{(y)}_w + eps_tr) on the respective sides for |r| <= c_flat T, uniformly in y, and Gamma^{(y)}_w -> Gamma_w.
(3) With rho_1 in (rho, 1), rho_1^2 kappa_w < 1: rho_1 g_y in C(f_y) for small y (small |r| by (2); rho_1|r| > c_flat T by Cor. 2.4 with
eps'_y = O(y^{2+eps}log(1/y)) = o(T^2) and Lemma lem:slack(a)). (4) Y3 Theorem 2.1 at f_y for the mate rho_1 g_y with data rho_1(b^pm, omega^pm), factor
rho/rho_1: (f_y, rho g_y) in cl NA; (f_y, rho g_y) -> (f, rho g). QED
Remark (OPEN). Non-d-neutral data: the consistency vector sum Delta d_m R_m* w_m becomes sum Delta d^{(y)}_m R_m* w^{(y)}_m at f_y (difference O(eps_e)
but of full support, breaking exactness off F), and Theorem 2.1 at f_y would need (SC) at f_y, which is not inherited from f at scales ~ eps_e.

4.2 Corollary ((LSC-trunc); PROVED). Over D^mu, (LSC-trunc) holds for every (f, g) of Theorem A and for every f of Theorem RS (all mates): the
NA approximants of Y3 Theorem 2.1 at f_y have finite base support.

4.3 Master principle at infinite F (item (3)). Theorem M_inf (PROVED as a reduction): over D^mu, (f, rho g) in cl NA as soon as there are windows
(T_j, n_j, K_j) as in Theorem 2.5 and first rows f^ex_j with p*(f^ex_j - f) <= theta_j c_flat^2 (T_j 2^{-n_j})^2 (f^ex_j = f, or the exactifying /
pulled / banked / tuned companions of Y1, Y2, Y4) such that the raised rows f_j := raise of f^ex_j along a weight W_j with (RR)-cost
o((T_j 2^{-n_j})^2) carry exact two-piece window data whose support usage is <= C|a^{(j)}|/t on F (then Lemma R2 with U_* = 0 gives the pieces),
with p*(g - g_{j,t}) <= K_j t, Gamma_w <= 1 + eta_0/2, averaged data d-neutral (or Delta d >= 0, or (SC) at f_j).
Proof. Lemma 2.3 at f^ex_j (whose decompositions of g carry the zeroth-order error p*(f^ex_j - f)) gives (a) of Theorem 2.5 with
eps'_j + p*(f^ex_j - f); (b)-(e) are the hypotheses plus Y3 Theorem 2.1 at f_j. QED
Consequence (SKETCH, by inspection). Theorem S, R1 (= Theorem RS), Z4 Theorem A, Y1's Master Theorem (D_X) and Y2's Theorem Y extend to infinite F
under (B_fin), (RR_B), (ND_B), (H3'): at the raised row the support usage of their data is cushion-dominated at all window scales, and
support-swallowed carriers enter the exact-switching cone with unconstrained sign rows as in R1 Step 2 (their d-rows and target rows are
the rows of f by Lemma VP). For Y1/Y2 the design-level Hoffman constants must include the patterns with support-swallowed carriers (finitely
many more patterns per level). Not written line by line.

4.4 (O4-box) (SKETCH/OPEN). With infinitely many bad carriers the switching on F at scale t is box-size, |X_j| <~ Bx_{B cap U(t)}(j)/t; cushion
compatibility needs |a^#_j| >~ Bx(j): a SCALE-FREE raise whose mass sum{Bx(j) : |a_j| < C Bx(j)} does not tend to 0. Raises give box domination on
the deep part only (mass sum_{j > N} Bx(j) -> 0, cost mu-suppressed); (BD_B) is then needed only on F cap [1, N(T)] with a constant C_a(N(T)) that
may grow with the window depth (for mu_s = 2^{-s^2}: max_{j <= N} Bx(j)/|a_j| = o(N^2) suffices for the transfer). Missing: inheritance of (SC_I)
at raised rows (Theorem N's data are not d-neutral). OPEN.

4.5 What remains of item (E) (precise).
 (E1) mu-thin supports ((RR) fails): |a_s| below a power of mu_s on infinitely many coordinates used by the data (for mu_s = 2^{-s^2}:
      log(1/|a_s|) >~ s^2). The switching is strongly pinned there; Y3 Theorem 3.5 covers the d-neutral monochromatic part. OPEN otherwise.
 (E2) (O4-box) as in 4.4.  (E3) non-d-neutral fixed data / (SC) at raised rows (4.1 Remark).
 (E4) degenerate cases: (ND) fails; (H3-inf) instead of (H3') (SKETCH repairs 3.5(c),(d)).
 (E5) the finite-F core (A)-(D) of ADDENDUM 6, transported to infinite F by 4.3.
RESOLVED for the designed norm: (O4-crit) and the support-swallowing part of (O4-nd) (Theorem RS).

## 5. Numerics (evidence only): V3_work/rt_check.py
Finite SOCP model: 14 base coordinates, 2 blocks x 6 coordinates, random carriers (q*(u) = 1), diagonal base mu_j = 0.5^{1 + j^{1.3}};
first rows from forced data (Remark rem:lemmaZ(c)); p* computed by CLARABEL. p*(f) = 1.000000 in all trials. Raising the three deepest support
coordinates by l_1-mass 0.12-0.18 gives p*(f^# - f) = 0.19-0.27 but eps' = 2||U*Delta a|| + p*(L*(w^# - w)) = 1.7e-4 - 2.6e-4. (RT) checked on
24 random (h, r), r in {0.3, 0.1, 0.03, 0.01}: never violated; minimal slack 1.4e-4 ~ 2||U*Delta a|| (the bound is tight up to the Hilbert term).

## 6. Corrections / precisions to earlier rounds
 (1) Y3_ref 3.2 (cushion-sharing factor 2) and Y3 3.5(i): correct as statements about R1's deep assignment and about Z3 Theorem E's
     decoupling; not obstructions (Theorem RS). Copied data lose only the oscillation of Exc/r^2 (Section 1).
 (2) Y3_ref 3.3 ("nested raises impossible"): correct for the requirement p*(f_j - f) = o(T_lo^2); Theorem 2.5 replaces it by
     eps'_j = o(T_lo^2), and the raise of Theorem RS has eps'_j = O(y^{2+eps}log(1/y)).
 (3) Y3_ref Prop. 3.4 (rho-threshold) and Y3 Theorem 3.5 (super-critical swallowing) are superseded under (RR_B), (ND_B), (H3') by Theorem RS.
 (4) Y3 Remark 3.6(b),(c) / Y3_ref 2.4 (absorbing contacts, q_l != 0): obstructions of the un-switching method only; R1's cone handles them.
