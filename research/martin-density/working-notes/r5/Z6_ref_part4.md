# Z6 referee, part 4: proofs of the fixes (to be assembled in Z6_ref_notes.md)

## F1. N-free reciprocal d-weights. PROVED.
Lemma. For the SLD-type designs (q*(T e_{k,m}) = c_l, Phi_l := Phi_{m}(k) = 2^{-m-k} c_l, l = j(k,m)) and every f, every
carrier l of block m that is a peak, or a strict non-peak with gap_m(k) <= M_m/2, satisfies |q_l| >= Phi_l/2, i.e.
1/|q_l| <= 2/Phi_l = 2^{m(l)+k(l)+1}/c_l.
Proof. |q_l| = Phi_l |w_m(k)|/(m C_m) and |w_m(k)| >= M_m/2. By Lemma A(b), M_m >= 1 - ||Phi_m||_1 and C_m = 1 - M_m <=
||Phi_m||_1 <= 2^{-m} sum_k 2^{-k} <= 2^{-m}; so M_m >= 1/2 and |q_l| >= Phi_l (1/4)/(m 2^{-m}) = Phi_l 2^m/(4m) >= Phi_l/2
(2^m >= 2m for m >= 1). QED.
Consequence: the factor 8N 2^{m+k}/c_l of D'' can be replaced by the N-free 1/Phi_l (times 2).

## F2. Design D''' (N-free D'' with corrected signature masses and SLD_G domination). PROVED (admissibility).
In (D1), after y_{l''}, u_{l''}, c_{l''} (l'' <= l) are fixed, put T(l) := union_{l'' <= l} supp y_{l''},
 m^nat_{l''}(l) := ||v_{l''} 1_{S_{l''} \ ([1,l] ∪ T(l))}||_1 > 0   (S_{l''} infinite, [1,l] ∪ T(l) finite),
 D(l) := 1 + sum_{l'' <= l} ( 1/m^nat_{l''}(l) + 1/Phi_{l''} ),
 Xi'(l) := [ l * H_comb(l) * G*(l) * D(l) ]^4 * ( l 2^{l^3} Lambda°(l) G*(l) )^5 ,
with H_comb(l) of Z6 5.2 and G*(l) of Z4 2.2 (both maxima over ALL subsets of [1,l], hence N-free), and
 n^w_l := ceil(l 2^{l^3} Lambda°(l) Xi'(l)), T_hi(l) := min{T_lo(l-1), 2^{-l^3}/(l Lambda°(l) Xi'(l))},
 T_lo(l) := 2^{-n^w_l} T_hi(l), c_{l+1} := min{c_l/4, T_lo(l)^3}.
Every ingredient of Xi'(l) depends only on design data of index <= l, so the recursion is well defined; Xi' >= 1, so (P1),
(P2) and the old (P3) hold, and the proof of Theorem thm:SLD (allowedness and c_{l+1} <= c_l/4 only) gives admissibility.
All of Section 8 survives (it uses only (T-a)-(T-d), (P1)-(P3)); so do Theorem C, Theorem U' below, Theorem V, and Z4
Theorem A (its window requirement n^w >= (l 2^{l^3} Lambda° G*)^6, T_hi <= its inverse, is met since Xi' >= (l2^{l^3}Lambda°G*)^5 G*^4).
The design is independent of N, so Lemma martintail applies to it.
For l* >= max F: S_l \ (F ∪ T_0(l*)) ⊇ S_l \ ([1,l*] ∪ T(l*)), hence m_l(l*) >= m^nat_l(l*) for every l <= l*.

## F3. Theorem U' (corrected statement of Theorem U, with the rigid-block extension). PROVED by modification.
Setting: design D''', N >= 1, f with F finite.  Blocks: COMPENSATED (Z6: two bad resonant strict non-peaks l^pm_m with
q > 0 > q, gaps >= gamma_B), or RIGID: every bad carrier of the block with q_l != 0 (strict non-peaks, and peaks with
vs eps = +1; for those q = Phi M/(mC)) is d-rigid at every level (Z6 5.6).  One-signed (= Z6's uncompensated) blocks are rigid.
Rates (all evaluated at level l, maxima over l' <= l):
 Lambda_g(l) := prod_{good l'' <= l} (1 + 3/r*_{l''})   (good carriers only; = 1 if there is none),
 K_P(l) := max Phi_{l'}/mu_{l'} over non-rigid swallowing-type bad peaks of compensated blocks,
 K_R(l) := max Phi_{l'} * kappa*_{l'}(l) over the q != 0 bad carriers l' of rigid blocks, where kappa*_{l'}(l) is the least
          sup-norm of a Farkas certificate of rigidity of l' in C_0^+(l) (Z6 Prop. P); in a one-signed block
          kappa*_{l'} <= (1 + max|q|)/|q_{l'}|, so K_R <= C_f (1 + K_nn) by F1 (K_nn as in Z6).
Hypotheses: (E1) r*_l > 0 for good l; (E2) gamma_T > 0; (E3') every block compensated or rigid; (E4') in compensated blocks
kept q < 0 non-peaks have gap >= gamma_B (or a gap rate, see Z6 5.4(c)), and every degenerate swallowing-type bad peak is
d-rigid; (E5) (H2') in every block;
 (W_U')  liminf_l Lambda_g(l) (1 + K_P(l) + K_R(l)) / (l 2^{l^3} Lambda°(l)) = 0.
Conclusion: f in Rec.
Proof (only the departures from Z6's proof of Theorem U).  Fix l* >= max(max F, fixed carriers), t in W(l*), t <= min(t_eta,1);
K_g := (1/q0 + 22) Lambda_g(l*).
(1) Lemma modswallow(a): its unrolling sets x_l = 0 at bad l and only good indices appear on the right, so the product runs
    over good l only: sum_good |Delta theta| <= K_g t.  ||e_0|| <= K_g t + 6t^2, c := c(tau) <= 3 K_g t.
(2) (tau_l)_- <= c/(2 m^nat_l(l*)) for every coarse bad l (F2).  Delta d: by 2.2 or Lemma badpeaks(a),
    |Delta d_m| M_m <= C_1 (c D + t + K_g t) <= 5 C_1 K_g D t =: K_d t  (D := D(l*), C_1 f-constant: 1/lambda and 1/(lambda mu)
    of the fixed pair, 1/(sigma|alpha|) of a fixed good peak).
(3) Drop bounds.  Anti-sign peaks: |tau| <= lambda K_d t + c/(2m).  Rigid blocks: Prop. P with bracket
    beta := sum_{l != l0}(tau_l)_- + sum (z_j L_j)_- + sum_rooms |L_j| + sum_anti |tau| + sum_m |Q_m(tau)|
       <= c D + c/2 + c/gamma_T + (K_d t + c D) + N (K_d t + 2t/sigma + (K_g t + 6t^5)/(mC)) <= C_2 K_g D (1 + 1/gamma_T) t,
    so |tau_{l0}| <= (K_R/Phi_{l0}) beta + c/(2m) and sum over rigid-block carriers <= K_R D beta + c D.
    Compensated blocks: non-rigid swallowing-type peaks |tau| <= t K_P/Phi + lambda K_d t; rigid ones by Prop. P as above.
(4) Violation total: V(t) <= C_3 K_g (1 + 1/gamma_T)(1 + K_P + K_R) D^2 t   (each rate appears linearly, Lambda_g once).
    Projection (Z6 5.2): ||tau - tau'||_1 <= H_comb(l*) V(t).
(5) Compensation: |e_m| <= C_4 (V + H_comb V) and the compensator additions cost |e_m|/|q_C|; rigid blocks keep only q = 0
    carriers.  ||Delta B 1_{F^c} - V''||_1 <= K_U t with K_U := C_5 Lambda_g (1 + K_P + K_R) H_comb D^2 (gamma_T, q0, ... in C_5).
(6),(7) as in Z6 (window two-piece data, shift trick for kept q > 0, windowed averaging, Corollary D1).  Window arithmetic:
    K_U T_hi(l*) <= C_5 Lambda_g (1 + K_P + K_R) / (l* 2^{l*^3} Lambda°(l*)) and n^w/K_U >= (l* 2^{l*^3} Lambda°)/(C_5 Lambda_g(1+K_P+K_R)),
    because Xi'(l*) >= l* H_comb D^2.  (W_U') gives a subsequence with both -> 0 / -> infinity.  QED
Corollary (maximal contact). If F is finite and z ≡ eps off F, then (E1), (E2) are vacuous, (E5) holds (2.2), Lambda_g ≡ 1,
and f is in Rec as soon as every block is compensated or rigid, (E4') holds, and liminf (K_P + K_R)(l)/(l 2^{l^3} Lambda°(l)) = 0.
For one-signed blocks K_R <= C_f(1 + K_nn): this is the precise form of Z6 6.3(ii).

## F4. One-sided transfer expansion with inward-only coordinates. PROVED.
Lemma (onesidedtransfer'). Lemma onesidedtransfer holds with a third admissible kind of coordinate k in supp omega_m,
 side +: vs_k omega_m(k) <= 1.5 gap_m(k)/t and vs_k omega_m(k) >= -A'/t;  side -: vs_k omega_m(k) >= -1.5 gap_m(k)/t and
 vs_k omega_m(k) <= A'/t  (vs_k = sgn w_m(k), any sign if w_m(k) = 0),
provided additionally c_flat <= min(1/3, 1/(4A')) (and the old conditions with A_3 := 2 + A_2 + A').
Proof. The coordinate conditions of the original lemma are used only through Lemma block(c),(d), i.e. to guarantee
||W||_inf = (1 - r d) M (attained at the peaks, where omega = 0) and Y = C + d r M >= C/2.  For an inward-only coordinate and
0 < r <= c_flat t (side +), with |r d| <= 1/2: vs W(k) = (1 - r d)(M - gap) + r vs omega(k) <= (1 - r d) M - gap(1 - |rd| - 1.5 c_flat)
<= (1 - r d) M, and vs W(k) >= (1 - r d)(M - gap) - c_flat A' >= (1 - r d) M/... >= -(1 - r d) M since (1 - r d)(2M - gap) >= 1/4
>= c_flat A'.  Side - is symmetric.  Then Lemma block(a),(b) with equality (c) give N(W) - 1 = sqrt(Y^2 + r^2||h_perp||^2) - Y
<= (r^2/2) H(omega)(1 + 2|d r| M/C).  The rebalancing part uses only ||W - w||_inf <= 2 A_3 c_flat.  QED
(Numerically confirmed, part 3.)  This is the statement used in Theorem C step 5 and Theorem U(6).

## F5. Sign-alternating signatures: corrected statement. PROVED.
If z is constant on S_l \ F for all but finitely many l and r_l > 0 for the remaining l in L_N, then f is in R_0^pm.
(For the cofinitely many l with S_l ∩ F empty and z constant: r_l >= ||v_l||_1/2, so 1 + 3/r_l <= 3(1 + 2/delta°_l); finitely many
other factors are constants; hence Lambda^pm_f(l) <= C 3^l Lambda°(l) and (W^pm) holds.)

## F6. Minor corrections.
 - 4.2(b): g|_A = eps_l theta*_l v_l|_A, theta*_l := lim eps_l theta^pm_l(t_n) (= the constant value of rho).
 - 2.2: non-degeneracy of k_1 is not needed.
 - 6.1 (C2): "(W_U)" -> "(W*_P), (MS)"; F = {j0} has no free parameter, take |F| >= 2.
 - 8.2 / 11: "D'' windows dominate SLD_G" needs F2.
 - Theorem V(b): K_A must be the max over the cones C_0^+(U) of the active sets U(t) (at most l*+1 of them; rigidity passes to
   subsets by extension by zero), or Prop. P is applied on B_* with the inactive carriers (|tau| <= 6 lambda/t < 6t) in the bracket.
