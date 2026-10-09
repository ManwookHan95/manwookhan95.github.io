# N2 referee notes (assembled): verification of N2_notes.md and a sharper treatment of Delta d < 0

Setting: canonical base q, Martin's norm with a FINITE block set I (p_N; by Preprint B Remark martin-tail, density for p_N at arbitrarily
large N gives density for p). Admissible T = Lemma B's conclusion only. Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Part files: N2_ref_part1.md (algebra, Lemma 1.3, Theorem 1), N2_ref_part2.md (Cor 2.5, Rem 2.6, Section 3: Lemma 3.1-3.4, Thms 2-3),
N2_ref_part3.md (new: Lemma R, Theorem 3*, Corollary R), N2_ref_part4.md (kink class, 3.7-3.8, Section 4-5, numerics).
Scripts: N2ref_work/ytrick_exact.py, ytrick_sharp2.py, ytrick_general.py, ytrick_diag.py (Lemma R); N2's own scripts re-run.

Summary of findings.
 * N2 Theorem 1 (Delta d = 0) and Corollary 2.5 (P1's explicit defect recovered): PROVED, every step re-derived.
 * Lemmas 1.2-1.5, 3.1, 3.2, 3.3, Theorem 4, Prop 5.2 (mod R1): PROVED as stated.
 * Theorem 2 (Delta d > 0): correct after a constant fix (s <= 1/2 is not enough in Lemma 1.3's factor 1/(1-s); need s <= eta_0/2).
 * Theorem 3 (Delta d < 0): the IVT tuning step is unjustified without (TT) (psi~_n(0) may be > 0); constant in G_n; fixable by hypotheses.
 * Corollary 3.4 / 4.7 ("mismatch must sit in the base"; "convexity cannot replace (PC)"): FALSE as stated. Lemma R (new, PROVED):
   N(w' + (w'-w)1_S) <= 1 + (C'-C)_+ + second order, S = coordinates where the reflection 2w'-w does not overshoot. Only the status-changing
   part of w'-w and one scalar must be paid. Theorem 3* replaces (PC) by (PC*); Corollary R proves N2's 3.7(a) (block-tame, (TT)) outright.
 * 1.6/3.9 kink class: identification correct when Q is finite; "no new mechanism" over-stated (weighted vs max coefficients).

# N2 referee, part 1: first pass over N2_notes (algebra, Lemma 1.3, Theorem 1 skeleton)

Setting used by N2 and by this report: canonical base q, FINITE block set I (p_N), admissible T = Lemma B's conclusion only.

## 1.2 Algebra of exact two-piece representations -- re-derived
(a) g(xi)=0 for g in C(f) (Goldstine: net x_alpha -> xi weak*, p(x_alpha)<=1, f(x_alpha)->1, f^2+g^2<=p^2). For omega in c_00(Q):
    <omega,zeta> = d(omega)|zeta| (Fact C off peaks), <w,zeta> = |zeta|, so <omega - d w, zeta> = 0; hence b+(xi)=g(xi)=0. OK.
(b) v = sum_m R_m*(Delta omega_m - Delta d_m w_m) by linearity of d_m; R_m* omega = T(sum_k omega(k) m 2^{-m-k} e_{k,m}) in Y for omega in
    l_inf. z_j v_j = |b+_j|+|b-_j| on K. OK.
(c) d''(omega) = sum_k Phi^2 w''(k) omega(k)/C'' = sum zeta''(k) omega(k)/|zeta''| (Fact C at f'', omega off P''). OK.
(d) v=0 => L*((Delta omega_m - Delta d_m w_m)_m)=0 => Delta omega_m = Delta d_m w_m, and at a peak (w != 0, Delta omega = 0) Delta d_m = 0. OK.
    v != 0 => v in Y\{0}, Y cap c_00 = {0} => supp v infinite, inside F cup K, F finite. f NA => zhat in c_0 => K finite. OK.
(e) Base: ||a+tau b||_1 = ||a||_1 + tau b(z) for small tau>0 (F finite, z-signed on K); Hilbert excess
    nu*Psi(h) >= tau^2 h(b)/(2(1+tau||U*b||/nu)) since sqrt((1+al)^2+be^2)-(1+al) = be^2/(sqrt(..)+1+al) and both terms <= 1+||h||. OK.
    Block: N(w+tau(omega-d w)) = 1 + tau^2||h_perp||^2/(sqrt(Y^2+tau^2||h_perp||^2)+Y), Y = C + tau d(1-C) -- re-derived exactly
    (the first-order terms -tau d M + tau d(1-C) cancel since M+C=1). OK.
(f) convexity. OK.
VERDICT 1.2: PROVED (correct).

## 1.3 Convex block lemma -- re-derived
W = (1-s)[(1-tau~ d'')w'' + tau~ omega] + s y: (1-s)(1-tau~ d'') = 1-s-tau d'', (1-s)tau~ = tau. Triangle inequality + N(y)<=1. OK.
Bound N(W) <= 1 + tau^2 H''/(2(1-s)) (1+...) follows from A Lemma 4.4(d) applied with tau~ (needs |tau~| <= r''). OK.
VERDICT: PROVED. (Trivial but correct; the content is that the w-direction is an inward direction for s>=0.)

## 1.4 Base excess at an NA point -- re-derived
||a'+tau B||_1 = ||a'||_1 + tau B(z') + kink' (no sign change on supp a'); Hilbert: Psi(h) <= be^2/(2(1+al)) <= be^2/(2(1-||h||)).
Sum: 1 + tau B(xhat') + kink' + tau^2 h'(B)/(2(1-|tau| ||U*B||/nu')). OK. Also the generalisation used implicitly later:
|a + x| <= |a| + sign(a) x + 2|x| for all reals (so sign changes on supp a' cost <= 2|tau B_j|). OK.

## 1.5 Convergence of engineered approximants
L compact => L** weak*-to-norm on bounded sets (range in V); J_V norm-to-weak* continuous at smooth points (Smulian; all block
components of L**zhat nonzero because the normalized u_{k,m} are dense in S_Y and Y is dense); L* weak*-to-norm on bounded sets.
grad q(x'_n) = a'_n by Fact D. OK. PROVED (relies on A Fact E for the "data converge" part).

## 1.6 Kink-class identification: ISSUE (to be checked against C_referee 1.20)
omega'' := v''_Q - (c'/M) w 1_Q is in general NOT finitely supported (w(k) = C zeta(k)/(Phi(k)^2|zeta|) on Q), so (E2) fails unless
Q is finite or w vanishes on Q off a finite set. The algebra (Delta d = -(s+ - s-)c'/M, Lemma 1.2(c) extended to bounded omega'' on Q)
is correct; the CLASS identification needs either Q finite or an extension of Def 1.1 / Theorems 1-3 to omega in l_inf(Q).

## Theorem 1 -- line-by-line check of Steps 0-8 (first pass)
Step 2 estimates re-derived: |<U*v,E(A_n(0))-e>| <= D_n||U||/(2(||U||+1)) + (1/2)S, S := sum_Far |v_j| in [D_n,2D_n];
psi_n(0) <= -D_n, >= -6.5 D_n. 2.2(b): derivative = sigma_+ <P_{E-perp}U*v, U*e*_{j+}>/||U*A_mu||, continuous at (a,0). IVT OK.
Step 4: b'+ = b'_0 + theta v (uses Delta d' = 0), b'+(x') = theta psi_n = 0. OK.
Step 5: certificate (b'_0, omega_theta) at f'_n, coordinatewise radius ~3t_n (window masses 4t_n|b_theta,j|). Need: kappa(c') does
   not involve the coordinate ratio ||b/a'||_inf (TO CHECK in A Def 4.1/Prop 4.5).
Step 6: no sign change on F (4T_0 rho Gamma <= a_min/4), on window contacts (b+ z-signed, a' z-signed), on Far_n
   (|a'_j| >= (3/2)T_0 rho|v_j| >= (3/2)|tau rho theta v_j|); window contacts with b_theta,j = 0 but b+_j != 0 carry no mass,
   are contacts of f' (z'_j = z_j = +-1) with z-signed entries: kink 0. Kink only beyond N''_n: <= 3(1-rho^2) tau t_n/16. OK.
   Constants: base <= 1 + tau^2[rho^2(1+eta_0)^2/2 + 3(1-rho^2)/16] <= 1 + tau^2[1/2 - (1-rho^2)/16] <= s(tau). OK.
Step 7: s(tau)-s(rho tau) = (1-rho^2)tau^2/(s(tau)+s(rho tau)) >= (1-rho^2)min(tau^2,|tau|)/(2 sqrt 2) >= (1-rho^2)min(tau^2,|tau|)/3. OK.
Step 8: rho g' in C(f') <=> p*(f'+t rho g') <= s(t) for all t (p*(rho g') <= 1 is the t -> infinity limit). OK.
First-pass verdict: Theorem 1 correct modulo the imports (A Prop 4.5 constants, Lemma 4.4(d) radii, Fact A).
# N2 referee, part 2: Corollary 2.5, Remark 2.6, Section 3 (Delta d != 0)

## Corollary 2.5 (P1 example) -- re-derived
R_1*(e_2/lambda_0) = u (lambda_{2,1} = Phi_1(2), m = 1), d_1(e_2) = Phi_1(2)^2 w_1(2)/C_1 = 0, z = 1 on K', u > 0 on K'
=> (E1)-(E3) for b+- = g - mu+- u, omega+- = (mu+-/lambda_0) e_2. H_1 = mu^2/C_1 (D_1 e_2 orthogonal to D_1 w_1).
g_{K1}: mu+ = 0, mu- = c; h(g) <= c^2||U||^2/nu <= 9/32, h(g - c u) = ||P_perp U*(v 1_{K2})||^2/nu <= c^2||U||^2/nu
(P_perp kills U*e_1* = nu_1 e), c^2/C_1 <= 3/4: kappa <= 1 for c <= c_* of P1 2.3. Slab: coefficients <= 4 theta_*^2||U||^2/nu
and theta_*^2/C_1, so "the whole slab" holds after possibly shrinking theta_* (wording). VERDICT: PROVED (given Thm 1, P1 2.1-2.3, 6.1-6.2).

## Remark 2.6 (several active blocks, all Delta d_m = 0) -- check
Conditions: ell_m(x') = 0 for m in I_act. sum_m ell_m = v. v(x') tuned by masses (Thm 1). Moving finitely many fixed near free
coordinates j_1..j_r (r = |I_act|-1) changes ell_m(x') by sum_i ell_m(j_i) dz_i, leaves v(x') (v = 0 on J), the base (b'+- = 0 and
a' = 0 on J) and E (depends only on masses) unchanged; ell_m(zhat) = Delta d_m |zeta_m|/q_0 = 0, so the needed moves are O(|ell_m(x'_n)|)
-> 0 and stay inside the rooms. With the rank condition this is a fixed invertible r x r system. I see no gap; the step can be
written in 5 lines (upgradable to PROVED). VERDICT: correct (SKETCH label conservative).

## Lemma 3.1 (mismatch identity) -- re-derived
b'+ = b'_0 + theta l - theta Delta d' R*w' - c+ R*(w'-w), with l = v + Delta d R*w' - Delta d R*(w'-w): matches. b'+-(x') = -c+- Bx
(g'(x') = 0, <omega - d'(omega) w', R x'> = 0, <w', R x'> = |R x'|). Tuning identity l(x') - Delta d|Rx'| = v(x') - Delta d Bx. PROVED.
Useful reformulation (not in N2): with theta = 0, c+- = 0 one has EXACTLY b'+ = b'_0 and b'- = b'_0 - v', v' := R*(Delta omega - d'(Delta omega) w')
(the transfer recomputed with f''s data), v'(x') = 0 automatically. So the side-minus cost is the kink of v' at f', and
v' - v = -Delta d R*(w'-w) - (Delta d' - Delta d) R*w'. Exact tuning is needed only to kill the second term up to o(t_n).

## Lemma 3.2 -- re-derived
(a) = Lemma 1.3 with y = w. (b) sigma'W(k) = (1 - tau rho d')M' + |s|(M'+M); <DW,Dw'>/C' >= (1 - tau rho d')C' + tau rho d' + |s|C' - |s|C
(uses <Dw,Dw'> <= C C' and s < 0); sum = 1 + |s|(1 + M - C) = 1 + 2M|s|. PROVED. Numerics reproduced (min ratio 0.999998).
## Lemma 3.3 -- re-derived. zhat notin c_0 (f non-NA), xhat' in c_0\{0}; y in S_{q*} separating; tails of (u_{k,m})_k dense;
q**(zhat) = 1 = q(xhat'); Fact C threshold theta_m Phi_m(k) -> 0 and sign w(k) = sign zeta(k) on P. PROVED (needs no closeness of f').

## Corollary 3.4 -- over-stated conclusion
PROVED: within the family Omega'+- = omega+- - d'(omega+-) w' + c+-(w' - w) (i.e. the convexity lemma with y = w), Delta d < 0 forces
tau c > 0 on one side, and then N >= 1 + 2M|s|. NOT proved: that "the mismatch must be absorbed in the base" for every decomposition
of f' + tau rho g' (p* is an inf over all decompositions; other y, partial absorption of (w'-w)1_A with A = opposite peaks, etc.).
I checked the obvious alternatives (y = 2w' - w; y = w' + (w'-w)1_{A^c}): they fail or produce first-order costs ~ |M'-M| + |C'-C|
+ (non-peak shifts), i.e. a pinning condition again; so the HEURISTIC reading is plausible, but the word "must" should be "in the
convexity mechanism". VERDICT: correct_with_fixable_gaps (wording).

## Theorem 2 (Delta d > 0) -- constants gap
Block: Lemma 1.3 gives factor 1/(1-s), s = tau rho theta Delta d <= T_0 rho Delta d. The text only imposes s <= 1/2, which allows the
second-order coefficient to DOUBLE (H'/(1-s) up to 2H'), destroying the bound <= s(tau) when H ~ 1. Fix: add T_0 rho |Delta d| <= eta_0/2
to Step 0 (then 1/(1-s) <= 1 + eta_0). Tuning: psi~_n(0) = psi_n(0) - Delta d Bx_n(0) <= psi_n(0) < 0 (good sign); mubar_n must be
enlarged to 4 nu (7 D_n + Delta d Bx_n(0))/c_+ (still -> 0). d/dmu Bx -> 0 uniformly: J(R x'_n(mu)) -> w weak* uniformly in mu because
R x'_n(mu) -> R**zhat in norm uniformly (z'_n independent of mu, E(A_n(mu)) -> e uniformly), and dE/dmu converges in norm. OK.
(TT) => (BR): Bx <= <w'-w, R(x'-zhat)> (convexity at R x'), <w'-w, RU(E-e)> <= ||E-e|| sum_k lambda_k|w'(k)-w(k)| = o(t_n),
far part <= 2 theta_{N''}; mu_n = O(t_n) since psi~_n(0) = O(t_n) (window O(t_n), tail <= D_n-scale, Bx_n(0) = o(t_n)). OK.
VERDICT: PROVED after the constant fix (correct_with_fixable_gaps).

## Theorem 3 (Delta d < 0) -- tuning-direction gap (substantive but repairable)
The proof says "tune psi~ = v + |Delta d| Bx to 0 (as in 3.5)". In 3.5 the IVT works because psi~_n(0) <= psi_n(0) < 0. For Delta d < 0,
psi~_n(0) = psi_n(0) + |Delta d| Bx_n(0) with psi_n(0) in [-7D_n, -D_n] and Bx_n(0) >= 0 NOT compared with D_n. Without (TT) the only
devices lowering psi~ are the (discrete) far pulls, whose own contribution to Bx is <= 2 sum_k lambda_k |w'(k)-w(k)| |u_k|(Far_n) --
a T-dependent far-tail comparison with sum_Far |v_j| (exactly the comparison N2 itself flags in 3.5/3.7(b)). Moreover common opposite
peaks (Lemma 3.3) contribute POSITIVELY to Bx (each flipped peak k adds lambda_k (M+M')|u_k(x')|), so Bx_n(0) cannot be assumed
negligible. If psi~_n(0) > 0 and only upward devices exist, Delta d' - Delta d is not o(t_n) and side minus carries
(Delta d' - Delta d) R*w', a first-order kink of size ~|tau| |Delta d' - Delta d| ||R*w'||.
FIX: add to the hypotheses either (TT) (then Far_n = empty and psi~ is two-sided tunable) or Bx_n(0) <= D_n/(2|Delta d|) (e.g. (BR)).
Second (minor): G_n must use a larger factor: on Far_n the v-part already eats 2/3 of |a'_j| (|tau rho v_j| <= T_0 rho|v_j| <= (2/3)|a'_j|),
so a further |tau rho E'_j| <= |a'_j|/2 can flip the sign; define G_n with 4 T_0 rho |E'_{n,j}| > |a'_{n,j}| (or double the far masses).
Everything else (side + = certificate (b'_0, omega+) for tau > 0 with no kinks; side - kink <= 2|tau| rho sum_{G_n}|E'_j| via
|a+x+y| <= |a| + sign(a)(x+y) + 2|y| when a+x has the sign of a; h'(b'-) -> h(b-)) is correct.
VERDICT: correct_with_fixable_gaps (PROVED only after adding (TT) or a Bx_n(0) bound to the hypotheses).
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
