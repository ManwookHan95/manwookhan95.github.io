# Z2 referee notes (assembled): verification of Z2 with full re-derivations, corrections and additions

Setting: canonical base q; Martin's norm with finite block set I_N (p = p_N, every N; martin-tail transfers density to p); SLD operator T of G3 1.2
where stated, otherwise any admissible T (Lemma B's conclusion only). Notation of G3 parts 2-5 and Z2. Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Parts: Z2_ref_part1.md (budget, B±, peak pinning, theta-split), Z2_ref_part2.md (pinning modulo B, Theorem S), Z2_ref_part3.md (contacts, cushions,
routes (b), open-class bookkeeping), Z2_ref_part4.md (attacks, numerics). Scripts: ctx/r4/Z2ref_work/checks.py, toy_signmixed.py. Report: Z2_referee.md.

## 0. Verdict summary
| Z2 claim | Verdict | Fix |
|---|---|---|
| Switching budget sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0 (any T) | PROVED, correct | gloss "vanishes elsewhere off F up to l_1-mass O(t)" is FALSE with near-contacts; only (1-|z_j|)-weighted mass is O(t) |
| Theorem B± (R_0 ⊂ R_0^± ⊂ R, SLD) | PROVED, correct | "(W±) if s_1 - s_0 <= C l" is a condition on the design's S_l |
| Peak pinning of the shift (any T) | PROVED, correct | — |
| theta-split (any T) | PROVED, correct (even with t/(2q_0)) | — |
| Pinning modulo swallowed carriers (SLD) | PROVED, correct with a fixable gap | 2.5(b) needs the UNIFIED triangular system; one-sidedness needs (H3) or B finite |
| Theorem S (SLD) | PROVED, correct with fixable gaps | as above + constant in 3.3(d); (H4) automatic and (H5) vacuous under (S_inf); "settles G3 6.3(d)" only under (H4),(H5),(W*) |
| Contact sandwich, cushions (any T) | PROVED, correct | first-order statements |
| Route (b)(i) (any T) | PROVED as a first-order base-cost statement | "signatures inside supp a do not help" is HEURISTIC; does not imply f notin R |
| Route (b)(ii) Lemma Z_cert | PROVED, correct | — |
| Route (b)(iii) Omega / Baire | PROVED, correct | — |
| Open-class table (Z2 4.5, 6) | incomplete | must exclude (BT) points: S3 Cor D2 puts every (BT) point, ANY contact set, in R |

## 1. Elementary tools (PROVED)
phi_z(x) := |x| - zx (|z| <= 1). (F1) phi_z(x - y) <= phi_z(x) + phi_{-z}(y). (F2) |phi_z(x + r) - phi_z(x)| <= 2|r|. (F3) phi_z(-cv) = |c|v(1 + z sign c) (v >= 0).
(F4) min_sigma sum v_s(1 + sigma z_s) = ||v|| - |<v,z>| (v >= 0). For |z| = 1: phi_z(x) = 2(zx)_-, phi_{-z}(x) = 2(zx)_+; for |z| < 1: phi_z(x) >= (1-|z|)|x|.
Proofs: one line each (triangle inequality and the definitions).

## 2. Switching budget (any admissible T). PROVED.
Statement: for g in C(f), any t > 0 and any two-sided decomposition (G3 2.1), sum_{j notin F} phi_{z_j}(B_+(j)) <= t/(2q_0), sum phi_{-z_j}(B_-(j)) <= t/(2q_0),
hence sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0.
Proof. Weights q_0 + sum_m sigma_m = 1, q*(A) >= A(zhat), N_m(W_m) >= <W_m, zeta_m>/sigma_m and (A + L*W)(xi) = (f + tg)(xi) = 1 give
q_0 E_q(A) + sum sigma_m e_m(W_m) <= max(q*(A), N_m(W_m)) - 1 <= s(t) - 1 <= t^2/2. E_q(a + tB) = sum_j (|A_j| - z_j A_j) + (||U*A|| - <U*A, e>)
>= t sum_{j notin F} phi_{z_j}(B_j). Same for a - tB_- with -z. (F1) for the difference. QED.
Correct reading: on K, Delta B is z-signed up to l_1-mass t/(2q_0)... (more precisely sum_K 2(z Delta B)_- <= t/q_0); on J_gamma its l_1-mass is <= t/(gamma q_0);
near-contacts (|z_j| -> 1) are NOT controlled in l_1 (counter-example to the gloss: z_j = 1 - 1/j, Delta B(j) = c_j >= 0 costs only sum c_j/j).

## 3. Theorem B± (SLD). PROVED.
Room theta_l := min_sigma sum_{s in S_l\F} v_l(s)(1 + sigma z_s), v_l(s) = delta_l 2^{-s}/n_l; Lambda^±(l) := prod_{l'<=l, m(l')<=N}(1 + 3/theta_{l'});
R_0^± := {F finite, all theta_l > 0, liminf_l Lambda^±(l)/(l 2^{l^3} Lambda°(l)) = 0}.
Lemma (pinning). theta_l |Delta c_l| <= E^±_l + 2 sum_{l'>l} kappa_{l',l}|Delta c_{l'}|, E^±_l := sum_{S_l\F} phi_{z_s}(Delta B(s)), sum_l E^±_l <= t/q_0.
Proof. On S_l, -Delta B(s) = Delta c_l v_l(s) + r_l(s), r_l(s) = sum_{l'>l} Delta c_{l'} y_{l'}(s)/n_{l'} (G3 (P1)). (F2): phi_z(-Delta c_l v_l) <= phi_z(Delta B) + 2|r_l|;
(F3) and the fact that sign(-Delta c_l v_l(s)) is the same for all s in S_l: sum_s phi_{z_s}(-Delta c_l v_l(s)) = |Delta c_l| sum_s v_l(s)(1 + z_s sign Delta c_l)
>= theta_l |Delta c_l|. sum_s |r_l(s)| <= sum_{l'>l} kappa_{l',l}|Delta c_{l'}|. Disjointness of the S_l and §2. QED.
Lemma (window). D_l <= (X_l + (8/3)S_{l+1})/theta_l with X_l := E^±_l + 2 sum_{l'>l_*} kappa D_{l'}, S_l := sum_{l<=l'<=l_*} D_{l'}; unroll from l_* down and use
1/theta <= 1 + 3/theta: sum_{l<=l_*} D_l <= Lambda^±(l_*) sum X_l <= Lambda^±(t/q_0 + 16t^2); fine carriers <= 6t^2 (box bound |Delta c_l| <= 6lambda_l/t,
sum_{l>l_*} lambda_l <= T_lo(l_*)^3 <= t^3). So sum_l |Delta c_l| <= (1/q_0 + 22)Lambda^±(l_*) t for t in W(l_*), t <= 1.
Theorem. R_0^± ⊂ R. Proof: G3 3.5 (pointwise inequality |x| + |y| <= |x-y| + phi_z(x) + phi_{-z}(y) valid for all z), part 4 (constants depend on f, N
only), 5.1, 5.2 never use (SR); run G3 5.3 (with the kappa_0 fix) along a subsequence with Lambda^±/(l 2^{l^3}Lambda°) -> 0. QED.
Facts: (a) R_0 ⊂ R_0^± (theta_l >= gamma vartheta^l delta°_l). (c) alternating z on S_l\F: theta_l >= (3/4)2^{-(s_1-s_0)}||v_l 1_{S_l\F}|| (alternating series:
<v,z>/c <= 2^{-s_0} - 2^{-s_1}/2, ||v||/c in [2^{-s_0} + 2^{-s_1}, 2^{1-s_0}]); (W±) then holds if s_1 - s_0 <= C l (A DESIGN CONDITION on S_l, not fixed by G3 (D0);
with first gaps ~2^l it fails). (d) theta_l >= sum v_l(s)(1 - |z_s|).

## 4. Peak pinning and the d-identity (any T). PROVED.
With omega_± = Omega_± + d_± w (G3 2.4): at a peak k, sigma_k omega_+(k) <= 0 <= sigma_k omega_-(k) and sum_P |alpha_k||omega_±(k)| <= t/(2sigma_m) (box inequality at
the peak, and the block-excess part of the budget, using ||W_±|| - sigma_k W_±(k) = t|omega_±(k)|). Hence
  |omega_+(k)| + |omega_-(k)| = sigma_k(omega_- - omega_+)(k) = -sigma_k Delta Omega(k) - Delta d M >= 0   (omega_- - omega_+ = -Delta Omega - Delta d w),
and if alpha_k != 0 the left side is <= t/(sigma_m|alpha_k|): -|Delta Omega(k)| - t/(sigma_m|alpha_k|) <= Delta d M <= |Delta Omega(k)|.
d-identity: from zeta/sigma_m = alpha + D^2 w/C, <w, alpha> = M, M + C = 1: d(omega_±) - d_± = <Omega_±, zeta>/sigma_m ± sum_P|alpha||omega_±| (signs as in G3 2.4(d)),
so |d(omega_±) - d_±| <= t/sigma_m and Delta d M = (1/(mC)) sum_k Phi_k w(k) Delta c_k + r, |r| <= 2t/sigma_m.

## 5. theta-split (any T). PROVED.
If Delta B 1_{F^c} = V + e, V supported in K and z-signed, then B_+1_{F^c} = theta V + r_+, B_-1_{F^c} = -(1-theta)V + r_-, theta in [0,1]^{supp V}, and
||r_±|| <= ||e|| + (1/2)sum_{j notin F}(phi_z(B_+(j)) + phi_{-z}(B_-(j))) <= ||e|| + t/(2q_0).
Proof. V_j = 0: r = (x, y), and |x| <= 2|x - y| + |y| - z(x - y)... i.e. |x| <= |e_j| + (phi_z(x) + phi_{-z}(y))/2, same for |y| (since |x| <= |x-y| + |y| and
|x-y| - z(x-y) >= 0). V_j != 0 (|z_j| = 1): X = z_j x, Y = z_j y, v = |V_j|, X - Y = v + z_j e_j, phi_z(x) = 2X_-, phi_{-z}(y) = 2Y_+; theta_j = clamp(X/v, 0, 1);
|r_+(j)| = dist(X, [0,v]) <= X_- + Y_+ + |e_j|; |r_-(j)| = |Y + (1-theta_j)v| equals |e_j| (0 < theta < 1), is <= X_- + |e_j| (theta = 0), <= Y_+ + |e_j| (theta = 1).
Sum. QED. (Numerically confirmed, part 4.)

## 6. Pinning modulo exactly swallowed carriers (SLD). PROVED (with the unified system).
B := {l : theta_l = 0} (z == sigma_l on S_l\F). S*_l := S_l \ (F ∪ U_{l' in B, l'>l} supp y_{l'}); theta*_l the room on S*_l; rho_l := theta*_l (l notin B),
rho_l := 2||v_l 1_{S_l\F}|| (l in B); Lambda*(l) := prod(1 + 3/rho); (W*): all rho_l > 0 and liminf Lambda*/(l 2^{l^3}Lambda°) = 0; K* := (1/q_0 + 22)Lambda*(l_*).
(a) good l: theta*_l|Delta c_l| <= E_l + 2 sum_{l'>l good} kappa|Delta c_{l'}| (only u_l's signature and good finer targets live on S*_l).
(b) bad l, under (H3): rho_l (tau_l)_- <= E_l + 2 sum_{l'>l good} kappa|Delta c_{l'}| (tau_l := -sigma_l Delta c_l; phi_sigma(-Delta c v) = 2(sigma Delta c)_+ v).
UNIFIED SYSTEM (referee): x_l := |Delta c_l| (good) or (tau_l)_- (bad); every inequality reads x_l <= (X_l + (8/3)S_{l+1})/rho_l with S_l = sum_{l<=l'<=l_*} x_{l'}, since the
right sides contain only later good x's; unrolling gives sum_{l<=l_*} x_l <= Lambda*(l_*)(t/q_0 + 16t^2). Hence sum_{good}|Delta c| <= K* t and sum_{B cap Cset}(tau)_- <= K* t.
(Z2's "rho_l >= 1/Lambda* absorbed" gives only Lambda*^2 t; the unified system is what the factors of bad l in Lambda* are for.)
(c) all bad l resonant: Delta B 1_{F^c} = sum_{B cap Cset}(tau_l)_+ u~_l + e, ||e|| <= 2K* t + 6t^2.
Without (H3) and with B infinite, one-sidedness of the bad switching is not proved; with B finite it follows from the cost function of §7.

## 7. Theorem S (SLD). PROVED (imports: G3 2-5 with kappa_0 fix, S3 Cor D1).
Hypotheses: F finite; (H4) each block has a non-degenerate peak of index notin B; (H5) no bad degenerate peak with sign w(k_l) = sigma_l; (W*); and
(S_fin) B finite, or (S_inf) (H3) and every bad l resonant and d-neutral (u_l(xi) = 0, hence a strict non-peak with gap M; then (H4) is automatic, (H5) vacuous).
Conclusion: f in R.
Proof (re-derived). (i) Delta d pinned: |Delta d_m|M_m <= t/(sigma_m|alpha_{k_1}|) + K* t/lambda_{k_1} by §4 at the good peak k_1. Bad peaks pinned by §4:
|tau_l| <= lambda_l(t/(sigma|alpha|) + K_d* t) if alpha_{k_l} != 0; tau_l <= lambda_l K_d* t if sigma_{k_l} = -sigma_l. d-sum: |sum_{m(l)=m} a_l tau_l| = O(K* t),
a_l = sigma_l Phi(k_l) w(k_l)/(mC) (d-identity of §4 split into good, fine and bad terms).
(ii) (S_fin) cost c(tau) := sum_{j notin F} phi_{z_j}(sum_B sigma_l tau_l u_l(j)) = sum_B 2(tau_l)_-||v_l 1_{S_l\(F∪T_0)}|| + sum_{T_0\F} phi_{z_j}(L_j tau), T_0 = U_B supp y_l
finite: polyhedral; Z := {c = 0, tau = 0 on Bpk, sum_{m(l)=m} a_l tau_l = 0} is a polyhedral cone ⊂ R^B_+ containing 0, and Hoffman gives
||tau - tau'||_1 <= H(c(tau) + sum_{Bpk}|tau| + sum_m|sum a tau|) = O(H K* t) for some tau' in Z (c(tau) <= t/q_0 + 2||e_0||, e_0 the good/fine part, by (F2);
the lower bound on bad degenerate peaks with sign -sigma_l comes from c). (S_inf) tau' := tau_+ (zero cost by resonance, a_l = 0, ||tau - tau'|| <= K* t by §6).
V' := sum_B sigma_l tau'_l u_l 1_{F^c} is z-signed, supported in K, and Delta B 1_{F^c} = V' + e', ||e'|| = O(K't).
(iii) theta-split (§5) and the data: omega^+ := G3 clamp on good coarse non-peaks with gap >= t^2 + exact omega_+(k_l) at bad coarse non-peaks; b^+ := B_+1_F + theta V' - kappa a
(kappa := (B_+1_F + theta V')(zhat)); omega^- := omega^+ + sum (sigma_l tau'_l/lambda_l)e_{k_l}; b^- := b^+ - sum sigma_l tau'_l u_l. Then b^+1_{F^c} = theta V', b^-1_{F^c} = -(1-theta)V'
(sign conditions on K, supports in F ∪ K); R_m*(sigma tau'/lambda e_{k_l}) = sigma tau' u_l and d(omega^-) - d(omega^+) = sum a_l tau'_l = 0 give the second representation;
b^+(zhat) = 0 and b^-(xi) = -sigma_m sum a_l tau'_l = 0 (u_l(xi) = sigma_m Phi w(k_l)/(mC) at non-peaks). These are P2A 1.6 data with Delta d = 0.
||g - g_t|| = O(K't) (G3 4.2(c) at good coordinates, exactness at bad non-peaks, pinned bad peaks, Delta d from (i)); Gamma_w(±) <= (sqrt(1 + eta_Gamma) + O(K't))^2
(seminorm comparison with (B_±, Omega_±) and G3 2.3(d)); t||b^±|| <= A_0'; |omega^±(k_l)| <= A_2/t at bad coordinates (gap >= gamma_B > 0).
(iv) one-sided transfer expansion: for sigma s in (0, c_1 t], E_q(a + s'b) = Fl + sum_{j notin F}phi(s'b_j) + nu Psi(s'U*b/nu) (A Lemma 7.2 is an identity) with Fl = 0
(c_1 A_0' <= min_F|a_j|), phi-terms 0 (sign condition), Psi(y) <= ||P_{e-perp}y||^2/(2(1 - ||y||)); bad block coordinates stay below (1-sd)M - gamma_B/2 when
c_1 A_2 <= gamma_B/4; rest as G3 5.1. So p*(f + s g_t) <= 1 + (s^2/2)(1 + eta_0) for 0 < sigma s <= c_1 t (+ data for s > 0, - data for s < 0).
(v) G3 5.2 (uses only the local expansion, the O(Kt) approximation, g in C(f) and convexity) gives rho g_avg in C(f); averaged data are P2A data
(signs, supports, the two linear identities, d-neutrality preserved; Gamma_w convex), with kappa_w(rho Dbar) <= rho^2(1 + eta_0) < 1; S3 Cor D1 (F finite,
Delta d = 0) gives rho g_avg in Ls(f); p*(g_avg - g) -> 0 and Ls(f) closed. QED.
Remarks. (1) Constant slip: |omega_+(k_l)| <= (3 + eta)/t. In fact the budget gives, for a d-neutral bad carrier, Phi(k_l)|Omega_±(k_l)| <= sqrt((1 + eta_Gamma)C_m/sigma_m),
so the switching through a fixed coarse carrier is O(1). (2) A tempting relaxation FAILS: S3 Cor D1 allows Delta d_m >= 0, but data with Delta d != 0 need
-Delta d R_m* w_m inside the base difference v, and R_m* w_m has signature mass on roomy good signature sets (good peaks), where it is not z-signed. So exact
d-neutrality is necessary for this construction. (3) The "mixture" remark of Z2 3.1 is plausible, not proved.

## 8. Contact sandwich, cushions (any T). PROVED.
sum_K (z B_+)_- <= t/(4q_0), sum_K (z B_-)_+ <= t/(4q_0); z_j(L*Omega_+)(j) - eps^+_j <= z_j g(j) <= z_j(L*Omega_-)(j) + eps^-_j on K, sum eps <= t/(2q_0).
Cushions: for j in F, |a_j + x| - sign(a_j)(a_j + x) = 2(-sign(a_j)x - |a_j|)_+, so sum_F(-sign(a_j)B_+(j) - |a_j|/t)_+ <= t/(4q_0) and the mirror bound for B_-.
(First-order statements; the Hilbert term still constrains B on F at second order.)

## 9. Routes (b). PROVED (with the scope remarks).
(i) For any admissible T, finite F, a with supp a = F and carrier u not supported in F: z := sign u on supp u \ F, sign a on F, 0 elsewhere defines f (q**(z + Ue) = 1,
p**(xi) = 1 = f(xi), uniqueness of normer and forced decomposition) at which phi_{z_j}(c u(j)) = 0 for c >= 0. Private signatures: z == sigma swallows all. This is a
FIRST-ORDER BASE-COST statement only (such f can be in R: Thm S, Thm B±, S3 Cor D2); "signatures inside supp a do not help" is HEURISTIC (first-order cushions only).
(ii) Lemma Z_cert => density (C Thm 7.4 or S3 Cor D1 at f', any T); <= for SLD (NA approximants lie in R_0, G3 Cor 6.4).
(iii) Omega ⊂ R dense G_delta (Preprint A, proof checked); {supp a finite} ⊂ U_n F_n (compact) meagre; a non-recoverable (f, rho g) has A_eps ∩ R = ∅ for small eps.

## 10. Open-class bookkeeping (correction) and status
S3 Cor D2 (refereed): every (BT) point (F finite, Q_m finite, no degenerate peaks, (MS)) is in R with ARBITRARY contact set, any admissible T. So Z2's OPEN classes
"maximal contact z == sigma off F" and "near-contacts with super-fast room decay" are open only OFF (BT). Theorem S with B infinite (S_inf) always concerns
non-(BT) points (infinitely many strict non-peaks), and Theorems B±, S are new exactly where (BT) fails.
Status for SLD after Z2 (+ this report): R ⊇ Omega ∪ NA ∪ BT ∪ R_0^± ∪ R_S. OPEN (Lemma Z): F finite, not (BT), and [infinitely many exactly swallowed sets with
non-resonant or non-d-neutral carriers, or super-fast room decay, or a bad degenerate peak with the swallowing sign]; F infinite without room
(G3 6.3(e)-type extension with room is SKETCH). No counterexample is suggested.
Most valuable idea: keep the unpinned switching as EXACT two-piece data (Hoffman projection onto the zero-cost polyhedral switching cone + coordinatewise
theta-split, d-neutrality forced by one pinned non-degenerate peak), average whole windows of such data, and let S3 Cor D1 do the engineering.
