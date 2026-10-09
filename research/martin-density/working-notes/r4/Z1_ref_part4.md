# Z1 referee, part 4: Z1 part 4 (flip lemma, Theorem B^inf, bounded free switching)

## 4.1 Flip lemma (Z1 4.1). Verdict: CORRECT (PROVED), any admissible T, any f (F may be infinite).
Re-derived. By A Lemma 7.2 the flip part of E_q(a + t B_+) is sum_{j in F} 2(-sign(a_j) t B_+(j) - |a_j|)_+ = 2t sum_j f^+_j, and that of
E_q(a - t B_-) is 2t sum_j f^-_j; the budget q_0 E_q <= s(t) - 1 <= t^2/2 (the block excesses are >= 0) gives sum_j f^+-_j <= t/(4 q_0).
If e_j > 0: sign(a_j) B_+(j) = 2|a_j|/t + e_j and sign(a_j) B_-(j) <= |a_j|/t + f^-_j, so sign(a_j) Delta B(j) >= |a_j|/t + e_j - f^-_j; in
particular e_j <= |Delta B(j)| + f^-_j (even with the extra -|a_j|/t). Clamp: |B_+(j) - b^cl(j)| = (|B_+(j)| - 2|a_j|/t)_+, which equals e_j
when sign B_+(j) = sign a_j and is <= f^+_j otherwise. Summing: ||(B_+ - b^cl) 1_F||_1 <= ||Delta B 1_F||_1 + t/(2 q_0).
Pointwise inequalities checked on 2*10^5 random instances (scalar_checks.py): max violation 0.

## 4.2 Theorem B^inf (Z1 4.2). Verdict: plausible; SKETCH label appropriate (correct_with_fixable_gaps).
Checked ingredients:
 (i) Truncation: ||b^cl 1_{F \ F_t}||_1 <= (2/t) sum_{F \ F_t} |a_j| <= 2t. kappa_t = (b^cl 1_{F_t})(zhat) = B_+(zhat) - (B_+ 1_{F^c})(zhat)
     - ((B_+ - b^cl) 1_F)(zhat) - (b^cl 1_{F \ F_t})(zhat) = O(t) + O(K t) + O(K t) + O(t) (||zhat||_inf <= 1 + ||U||). |b_t(j)| <= 2|a_j|/t + 2|kappa_t||a_j|
     <= 3|a_j|/t once 2|kappa_t| t <= 1, using (a 1_{F_t})(zhat) -> 1. The remainder B_+ - b_t = B_+ 1_{F^c} + (B_+ - b^cl) 1_F + b^cl 1_{F \ F_t} + kappa_t a_t
     is O(K t) in l_1. Correct.
 (ii) 5.1 under (C-a'): with |s'| <= c_1 t and |b_j| <= 3|a_j|/t, c_1 < 1/3 gives no flips; b finitely supported in F and b(zhat) = 0 give the
     exact identity q*(a + s' b) = 1 + nu Psi(s' U*b/nu), and ||s' U*b/nu|| <= 3 c_1 ||U|| ||a||_1/nu. So the base relative error is O(c_1) (not o(1)
     as in G3, where it was O(s)); it is absorbed by choosing c_1 small after eps_tr, as Z1 says. Steps 0-4 and 6 do not involve b. Correct.
 (iii) 5.2 unchanged (the averaged certificate has finitely supported b). Correct.
 (iv) Final recovery: C Thm 7.4 for a in l_1 \ c_00 and b in c_00. This is the C referee's addition to Remark 7.1' (C_referee 1.16, item 1: use
     b'_N = b - (b(x'_N)/c_N) a_N; signs on supp b are stable; first-order term b'_N(x~_N) = 0), stated in two lines, not written out.
     So B^inf is a SKETCH resting on a refereed but unwritten remark. The label is right.
 Also checked: 2.2 (||A_n - a||_1 -> 0) and 2.3 hold for any a in l_1; 3.2-3.4 use J_gamma, which excludes F, so (SR) with infinite F is
 meaningful; 2.5 (the only finite-dimensional step) is no longer used.

## 4.3 Bounded free switching (Z1 4.3). Verdict: CORRECT (PROVED).
Re-derived: Delta B = -sum_l Delta c_l u_l (both pairs represent g); G3 2.3(d) gives q_0 h(B_+-) <= Gamma_w <= 1 + eta_Gamma, i.e.
||P_{e-perp} U* B_+-|| <= c_f := (nu(1 + eta_Gamma)/q_0)^{1/2}; ||U* x|| <= ||U|| ||x||_1. Injectivity of c -> P_{e-perp} U*(sum_{U*} c_l u_l): a zero gives
sum c_l u_l = mu a/nu with the left side in Y = Ran T and a in c_00 (F finite), so both vanish (Y cap c_00 = {0}), and injectivity of T on the
finitely many distinct basis vectors e_{k(l),m(l)} gives c = 0. Bounded below on R^{U*}. Correct.
Slaving closure: kappa_{l',l} > 0 needs supp y_{l'} cap S_l != empty, hence l < l' (allowedness (a)), and each y_{l'} meets finitely many S_l. Starting
from a finite U, the closure stays inside {1, ..., max U}: finite. Correct.
Remark. F finite is essential (Y may contain a when a is not in c_00). Z1 states the hypothesis.
