# Z2 referee, part 1: switching budget, Theorem B±, peak pinning, theta-split (line-by-line re-derivation)

Setting as in Z2/G3: canonical base q, Martin's norm with finite block set I_N (p = p_N), SLD operator T of G3 1.2 where said,
otherwise any admissible T. Notation of G3 parts 2-5. Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1. phi-calculus (Z2 1.1). PROVED (re-derived).
phi_z(x) = |x| - z x >= 0 for |z| <= 1.
(F1) |x - y| - z(x - y) <= (|x| - zx) + (|y| + zy). (F2) | |x+r| - |x| | + |z||r| <= 2|r|. (F3) phi_z(-cv) = |c|v + zcv = |c|v(1 + z sign c), v >= 0.
(F4) sum v_s(1 + sigma z_s) = ||v|| + sigma<v,z>; min over sigma = ||v|| - |<v,z>|. All correct.
Useful closed forms (used below): for |z| = 1, phi_z(x) = 2(zx)_-, phi_{-z}(x) = 2(zx)_+; for |z| < 1, phi_z(x) >= (1 - |z|)|x|.

## 2. Switching budget (Z2 1.2). PROVED, correct; one gloss is wrong.
Re-derivation: A Lemma 7.1 budget q_0 E_q(A) + sum_m sigma_m e_m(W_m) <= s(t) - 1 <= t^2/2 (uses only q_0 + sum sigma_m = 1,
(A + L*W)(xi) = 1 + t g(xi) = 1 and the subgradient inequalities), and E_q(a + tB) >= sum_{j notin F} t phi_{z_j}(B_j)
(||A||_1 - <A,z> = sum_j (|A_j| - z_j A_j), all terms >= 0; ||U*A|| >= <U*A, e>). Hence sum_{j notin F} phi_{z_j}(B_+(j)) <= t/(2q_0),
sum phi_{-z_j}(B_-(j)) <= t/(2q_0) (no smallness of t is needed for this step), and (F1) gives sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0.
GLOSS TO CORRECT: "the base part of the switching is z-signed on contacts and VANISHES ELSEWHERE OFF F up to l_1-mass O(t)" (Z2 summary, 4.1(c))
is false when there are near-contacts: off F cup K one only has sum (1 - |z_j|)|Delta B(j)| <= t/q_0, so mass of sign z_j on coordinates with
|z_j| -> 1 is cheap and its l_1 mass is NOT O(t). Correct statement: z-signed on K up to l_1-mass t/(2q_0); on J_gamma the l_1 mass is <= t/(gamma q_0);
in general only the phi_z-weighted mass is O(t). (Example: z_j = 1 - 1/j off F, Delta B(j) = c_j >= 0 costs sum c_j/j.) Nothing in Z2's proofs uses the
wrong gloss (the proofs use the phi-form), so this is a wording fix.

## 3. Theorem B± (Z2 part 1). PROVED, correct (with two remarks).
* Lemma 1.4: on S_l, -Delta B(s) = Delta c_l v_l(s) + r_l(s) with r_l(s) = sum_{l'>l} Delta c_{l'} y_{l'}(s)/n_{l'} (G3 (P1): coarser targets avoid S_l,
  other signatures live elsewhere). (F2): phi_{z_s}(-Delta c_l v_l(s)) <= phi_{z_s}(Delta B(s)) + 2|r_l(s)|; (F3) and the definition of theta_l
  (min over the CONSTANT sign sigma = sign Delta c_l) give theta_l|Delta c_l| <= E^±_l + 2 sum_{l'>l} kappa_{l',l}|Delta c_{l'}|. sum_l E^±_l <= t/q_0 since
  the S_l are disjoint. Correct.
* Lemma 1.5: D_l <= (X_l + (8/3) S_{l+1})/theta_l, S_l <= X_l/theta_l + (1 + 8/(3theta_l)) S_{l+1}; unrolling and 1/theta_l <= 1 + 3/theta_l give
  S_1 <= Lambda^±(l_*) sum_l X_l; sum_l X_l <= sum E^± + (8/3) sum_fine D (sum_l kappa_{l',l} <= 4/3). Fine carriers: |Delta c_l| <= 6 lambda_l/t (box),
  sum_{l>l_*} lambda_l <= T_lo(l_*)^3 <= t^3. Total <= Lambda^±(t/q_0 + 16t^2) + 6t^2 <= (1/q_0 + 22)Lambda^± t. Correct.
* Theorem 1.6: I checked every place where G3 uses (SR)/gamma: only 3.2-3.4 (through E_l = ||Delta B 1_{S_l cap J_gamma}|| and K_1). G3 3.5(b)
  uses the pointwise inequality |x| + |y| <= |x - y| + phi_z(x) + phi_{-z}(y), valid for every z (contacts included); G3 4.2 uses only 3.4-3.5 and
  the part-2 toolkit; 5.1, 5.2 never use (SR). Running 5.3 along a subsequence L_f with Lambda^±/(l 2^{l^3} Lambda°) -> 0 gives exactly the
  hypotheses of G3 5.2 (Lambda^± T_hi -> 0, n^w/Lambda^± -> infinity, K_l T_hi/n^w -> 0). Correct, with the referee's kappa_0 fix of G3 5.3.
* Fact (a) R_0 ⊂ R_0^±: theta_l >= gamma delta'_l >= gamma vartheta^l delta°_l and 1 + 3/theta_l <= (3/(2gamma)) vartheta^{-l}(1 + 2/delta°_l). Correct.
* Fact (c) (alternating signs): checked by hand and numerically (Z2ref_work/checks.py): theta_l >= (3/2) c 2^{-s_1} and ||v_l 1_{S_l\F}|| <= 2c 2^{-s_0},
  so theta_l >= (3/4)2^{-(s_1-s_0)}||v_l 1_{S_l\F}||. REMARK 1: the conclusion "(W±) holds if s_1 - s_0 <= C l" is a hypothesis on the DESIGN's
  sets S_l (G3 (D0) does not fix them; for S_l with first gaps ~ 2^l alternating z gives Lambda^± ~ 2^{2^{l+2}}, which violates (W±)). Since only
  the first few elements of S_l \ F carry the 2^{-s}-mass, theta_l essentially measures the weight of the FIRST sign change of z along S_l \ F;
  "cofinite contacts with mixed signs" are in R_0^± only if the first sign change on S_l comes within O(l^2)... more precisely when
  sum_{l' <= l} (s_{first change}(l') - min S_{l'}) = o(l^3) along a subsequence. Z2's statement is correct as written (it is conditional).
  REMARK 2: (W±) also needs theta_l > 0 for EVERY l (one exactly swallowed set excludes f from R_0^±), as stated.
Verdict: correct.

## 4. Peak pinning of the shift (Z2 2.1, 2.2). PROVED, correct.
G3 2.4(c) re-derived: at a peak k (w(k) = sigma_k M), |(1 - d_+t)sigma_k M + t omega_+(k)| <= (1 - d_+t)M forces sigma_k omega_+(k) <= 0, and
||W_+|| - sigma_k W_+(k) = t|omega_+(k)|, so the block-excess part of the budget gives sum_P |alpha_k||omega_+(k)| <= t/(2sigma_m); symmetric on the - side.
Then |omega_+(k)| + |omega_-(k)| = sigma_k(omega_- - omega_+)(k) = -sigma_k Delta Omega(k) - Delta d M (omega_- - omega_+ = -Delta Omega - Delta d w), >= 0,
and at a non-degenerate peak it is <= t/(sigma_m|alpha_k|). Hence -|Delta Omega(k)| - t/(sigma_m|alpha_k|) <= Delta d M <= |Delta Omega(k)|. Correct.
d-identity: d(omega_±) - d_± = <Omega_±, zeta>/sigma_m ± sum_P|alpha||omega_±| (re-derived from zeta/sigma_m = alpha + D^2 w/C, <w,alpha> = M, M + C = 1),
so |d(omega_±) - d_±| <= t/sigma_m and Delta d M = <Dw, D Delta Omega>/C + r, |r| <= 2t/sigma_m, <Dw, D Delta Omega> = (1/m) sum Phi_k w(k) Delta c_k. Correct.
Scope of the gloss "every non-d-neutral switching through a single resonant carrier is O(t)": correct for one bad carrier per block
(|a_l tau_l| = O(K* t), a_l = sigma_l Phi w(k_l)/(mC) != 0 fixed), with constant 1/|a_l| and the WINDOW constant K* (not a T-uniform O(t));
it presupposes a pinned non-degenerate peak, which needs the SLD pinning (any-T is only the algebraic identity).

## 5. theta-split (Z2 2.3). PROVED, correct.
Re-derived the three cases (V_j = 0; V_j != 0 with theta in (0,1), = 0, = 1). In fact the sharper bound ||r_±|| <= ||e|| + (1/2)sum(phi_z(B_+) + phi_{-z}(B_-))
<= ||e|| + t/(2q_0) holds (X_- = phi_z(x)/2, Y_+ = phi_{-z}(y)/2 on supp V, and on V_j = 0 one may use |x| <= |x - y| + ... per side).
Independent numerical check (Z2ref_work/checks.py, adversarial e, V, signs, scales 1e-3..1e3): see part 4.
