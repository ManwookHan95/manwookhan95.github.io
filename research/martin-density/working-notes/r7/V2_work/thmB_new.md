**Theorem B.**  PROVED (modulo the cited tools: Y4-ref Prop. P4 / V1 Lemma TU, Z3 Lemma 3.1, Y1 Lemma T2).  Design D^{V2},
diagonal U, F finite.  Let w = (l,i) be a clean sub-window for f (Y4 Thm 1.6 with the objects of Def. 2.1), l >= l_f.  Let
an assembly (V1 3.2; Y1 4.1; Y4-ref C.6-C.7) be given in the following form: first its z-moves on coarse supports (closing
class-G rooms on the S^nat sets, closing tiny target rooms on T(l)), producing a row f_1; then finitely many further moves
M_ass at coordinates beyond s_max(l) of carriers NOT in L_0(kappa) (donor raises: z-moves or banks; pulls converting
tiny-margin peaks), and the pattern kappa it produces.  Assume
 (A1) |val_{l'}(f_1) - val_{l'}(f)| <= C_*(l) b(w) for l' in L_0(kappa) (true for the z-move closings: (C1) moves a class-G
      value by its tiny room, (C2) by <= |T(l)| b; V1 Lemma ST(a)), and p*(f_1 - f) <= C_f Design(l) b(w) log(e/b(w));
 (A2) after M_ass every coarse carrier of G has the status prescribed by kappa, with relative margin >= u(w)/2 at peaks of
      kappa and either a gap >= c_f Lambda (V1 Lemma ST, donor raise Lambda = T_lo^3) or a relative position rho <= 1 - u/2 at
      strict non-peaks of kappa (or, if no donor raise is used in a block, all its coarse strict non-peaks of kappa have
      rho <= 1 - u/2 or rho <= C_* b and all its peaks of kappa have relative margin >= u/2 at f_1).
Then there is a companion f^# (the moves M_ass, the tuning of L_0(kappa) and, where needed, one outward push of the buffer
peak c_m per block, realized by ONE application of Lemma TU / Prop. P4) with:
 (a) the pattern of f^# is kappa (same G, signs, contacts on T(l), statuses); supp a^# finite;
 (b) val_l(f^#) = val_l(f_1) + x_l EXACTLY for l in L_0(kappa), with |x|_2 <= eta := T_lo(w)^4/(l Design(l)), and
     pi_O(val(f^#)) = 0 for every object O of kappa that is tiny at f (rho_O(f) <= b(w)), while |pi_O(val(f^#))| >= u(w)/2
     for every object that is robust at f;
 (c) p*(f^# - f) <= p*(f_1 - f) + C_f(cost of M_ass) + C_f Design(l)^2 eta log(e/eta) = o(T_lo(w)^2) (for V1's assembly
     C_f Design T_lo^3 log(1/T_lo));
 (d) the Hoffman constant of Sigma^# at f^# (all rows (Z1)-(Z5), box rows; l_1 residuals and distances) satisfies
        C_H^# <= C_f^l Design(l)^2 / u(w),
     for EVERY configuration of the zero-cost cone (single- or multi-block rays, compensated, mixed or one-signed blocks,
     any face structure).
Proof.  Step 1 (objects at f_1).  For every object O of kappa, |pi_O(val(f_1)) - pi_O(val(f))| <= Lip(l) C_*(l) b(w)
by (A1).  Hence tiny objects satisfy |pi_O(val(f_1))| <= beta = beta(w) of (2.1), robust ones >= u(w) - beta >= 3u(w)/4
(Lemma 2.1, last claim).
Step 2 (Lojasiewicz).  Apply Lemma L to the family of level l with S := the tiny objects of kappa and v := val(f_1)
(in [-2,2]^l since |u_l(zhat)| <= q*(u_l) = 1).  Alternative (i) of Lemma L is excluded because beta < 1/C_L(l) (2.1).
So there is v' with pi_O(v') = 0 (O tiny) and |v' - v|_2 <= C_L(l) beta^{2/N_L(l)} <= eta (2.1).  Put x := v' - v
restricted to L_0(kappa) (the polynomials of kappa involve only these coordinates).  Robust objects: |pi_O(v')| >=
3u/4 - Lip(l) eta >= u/2.
Step 3 (one combined realization).  Apply Lemma TU (V1 3.4; = Y4-ref Prop. P4 with explicit bank solution) at the row
obtained from f_1 by the moves M_ass (their masses and z-changes are part of the base A^p of its proof; their coordinates
are distinct from the pull and bank coordinates of L_0, which lie in the S_{l''}, l'' in L_0, beyond s_max(l)), with the
carrier set L_0(kappa) and the targets val^#_{l''} := v'_{l''}: since Lemma TU solves for EXACT values given all other
masses, the second-order side effects of M_ass on the L_0 values are absorbed, and val^#_{l''} = v'_{l''} = val_{l''}(f_1)
+ x_{l''} exactly.  The required increments are |x| + O(side effects) <= 2 eta <= c_T (c_T = f-constant x Design^{-3} >>
eta = T_lo^4/(l Design), Lemma 2.1).  Other coarse carriers k notin L_0 move by <= C_T eta^2 beyond the effect of M_ass
(Lemma TU(b)); all pulls/banks lie beyond s_max(l), so T(l), the contact pattern on T(l) and all swallowing signs are those
of the assembly; fine carriers: sum_{k > l} lambda_k |Delta u_k| <= 2^{-l} eta + (fine effect of M_ass).  Cost: Lemma TU(d).
Step 4 (statuses).  With V1's assembly, Lemma ST of V1 applies verbatim with the additional value moves |x| + C_T eta^2 <=
2 eta << c_f Lambda = c_f T_lo^3 (V1's raised blocks) and << u(w) (robust carriers): every coarse carrier keeps the status
prescribed by kappa.  In a block without donor raise in which a protection is needed (a self-contained assembly), push the
buffer peak c = c_m of Lemma 2.3 outward inside the same Lemma TU solve (c notin L_0): with zeta := R_m^** zhat_1 and
zeta^# := R_m^** zhat^#, X := max over coarse k != c of |zeta^#(k) - zeta(k)|/Phi_k^2 <= m(2 eta)/Phi_min(l) <= C D(l) eta and
E := sum_{k != c} |zeta^#(k) - zeta(k)| <= phi X + 2^{-l} eta (sum_k m Phi_k |Delta u_k| = sum_k Phi_k^2 (m|Delta u_k|/Phi_k)),
take r_m := C_*(l) b(w) theta_m and the push s := (16(A + theta + 1)/A) max{E, phi(X + r_m)} (a-priori bounds for E, X with
|y| <= C_f Design^2 eta for the push itself; A, theta, phi of block m at f_1).  Then E <= A s/(8(A+theta+1)), so Lemma QB
gives theta^#_m - theta_m >= R(s) >= X + r_m and theta^#_m - theta_m <= C_1(s + E), C_1(s + E) + X <= C_f Design(l)^2 eta <=
u(w) theta_m/4: every coarse strict non-peak of kappa (nu < theta_m, or nu <= theta_m + r_m for a tiny-margin peak declared a
non-peak) stays a strict non-peak (Lemma QB(b)); every coarse peak of kappa (relative margin >= u/2) stays a peak with its
sign (Lemma QB(c)); c stays a robust peak.  So the pattern of f^# is kappa: (a).  The common factors 1/A^#_m of (Z5) change
nothing in (b).
Step 5 (cost).  p*(f^# - f_1) <= C_f(cost of M_ass) + C_T(2 eta) log(e/(2 eta)) + C_f (s/lambda_c) log, and eta, s/lambda_c <=
C_f Design(l)^2 eta, eta = T_lo^4/(l Design): (c) (Lemma 2.1, last claim, for o(T_lo^2)).
Step 6 (Hoffman).  The matrix of Sigma^# at f^# is A_kappa(val(f^#)) with the (Z5)-row of block m multiplied by
1/A^#_m in [1/(2A_max), 2/A_min] (A_m = sigma_m/q_0 moves by C_f Delta: Z3 Lemma 3.1).  Its minors containing (Z5)-rows
equal (prod of the factors 1/A^#_m of the rows used) x pi_O(val(f^#)): by (b) they vanish or have modulus >=
(2A_max)^{-N} u(w)/2; the other minors are design numbers, zero or >= delta_comb(l).  Lemma H (1.3) (with the l_1/l_2
conversion factors sqrt(rows), sqrt(cols) <= (rows cols)(l)) gives C_H^# <= max(1, ||A||_2)^{l-1} (rows cols)(l) /
min(delta_comb(l), (2A_max)^{-N} u(w)/2) <= C_f^l Design(l)^2/u(w) (entries of (Z5)-rows are <= 2/A_min): (d).  QED
