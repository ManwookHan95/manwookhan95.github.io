# Z1 part 4: infinite base support F; bounded free switching

## 4.1 Lemma (flip analysis on an infinite support). PROVED. (Any admissible T, any f.)
Let (B_+-, Omega_+-) be a two-sided decomposition of g in C(f) at scale t <= t_eta (G3 2.1) and put, for j in F,
  f^-_j := (sign(a_j) B_-(j) - |a_j|/t)_+  (flip excess of the - side),  f^+_j := (-sign(a_j) B_+(j) - |a_j|/t)_+  (flip excess of the + side),
  e_j := (sign(a_j) B_+(j) - 2|a_j|/t)_+.
Then sum_j f^-_j <= t/(4 q_0), sum_j f^+_j <= t/(4 q_0), e_j <= |Delta B(j)| + f^-_j, and the clamp
  b^cl(j) := sign(B_+(j)) min(|B_+(j)|, 2|a_j|/t)  (j in F)
satisfies ||(B_+ - b^cl) 1_F||_1 <= ||Delta B 1_F||_1 + t/(2 q_0).
*Proof.* A Lemma 7.2: the flip term of E_q(a + tB_+) is sum_j 2(-sign(a_j) t B_+(j) - |a_j|)_+ = 2t sum f^+_j, and that of E_q(a - tB_-) is
2t sum f^-_j; the budget (A Lemma 7.1) gives q_0 E_q <= t^2/2 for each side. If e_j > 0 then sign(a_j)B_+(j) = 2|a_j|/t + e_j while
sign(a_j) B_-(j) <= |a_j|/t + f^-_j, so sign(a_j) Delta B(j) >= |a_j|/t + e_j - f^-_j >= e_j - f^-_j. The clamp removes e_j in the direction
sign(a_j) and (-sign(a_j)B_+(j) - 2|a_j|/t)_+ <= f^+_j in the other. Sum. QED.
(At f in R_0-type points ||Delta B|| <= K t (G3 3.5(a)), so the clamp costs O(K t): near-flips are pinned exactly like contacts.)

## 4.2 Theorem B^inf (G3 Theorem B for infinite F). SKETCH, with one imported ingredient.
For the SLD T and every N: every f in S_{p_N*} satisfying (SR) (no finiteness of F) is in R; more generally Theorem B* (1.5) holds for
window-pinned mates at f with arbitrary F.
Changes to G3 (each checked):
 (i) Window certificate: replace B_+ 1_F by the clamp b^cl (4.1), then truncate to a finite F_t subset of F with sum_{F \ F_t} |a_j| <= t^2
     (cost ||b^cl 1_{F \ F_t}|| <= 2t), and balance with a_t := a 1_{F_t}/(a 1_{F_t})(zhat) (note (a 1_{F_t})(zhat) -> a(zhat) = 1):
     b_t := b^cl 1_{F_t} - kappa_t a_t, kappa_t := (b^cl 1_{F_t})(zhat) = O(K t) (G3 2.3(a), 3.5(b), 4.1; ||zhat||_inf <= 1 + ||U||).
     Then supp b_t is finite, b_t(zhat) = 0, |b_t(j)| <= 2|a_j|/t + O(K t)|a_j|, and the remainder estimate 4.2(c) gains O(K t) + 2t. G3 2.5
     (finite-dimensional injectivity, used only for ||b_t|| <= K_b) is no longer needed.
 (ii) Uniform transfer expansion G3 5.1 with (C-a) replaced by (C-a'): |b_j| <= 3|a_j|/t on supp b (finite), Gamma_w(c) <= 2. In Step 5 only
     two facts about b were used: no sign flips for |s'| <= c_1 t (now |s' b_j| <= 3 c_1 |a_j| < |a_j| for c_1 < 1/3), and |s'| ||U*b||/nu small
     (now |s'| ||b||_1 <= 3 c_1 ||a||_1, so |s'| ||U*b||/nu <= 3 c_1 ||U||/nu, absorbed by choosing c_1 small after eps_tr). Steps 0-4, 6 do not
     involve b. PROVED modulo this bookkeeping.
 (iii) Windowed averaging G3 5.2: unchanged (it uses only (i)-(ii) and the final recovery).
 (iv) Final recovery: G3 uses C Thm 7.4 (balanced finite certificate with Gamma_w <= 1 is recovered along canonical truncations), proved in C for
     a in c_00. For a not in c_00 one needs C Thm 7.4 with a in l_1 \ c_00 and b in c_00: IMPORTED from the C referee (Remark 7.1' extended to
     b != 0, script rem71_check.py), NOT re-proved here. This is the only reason for the label SKETCH.
Consequence: modulo (iv), infinite base support is not an independent obstruction: Lemma Z may use approximants with (SR) and arbitrary F,
and the open core is exactly signature resonance (failure of (SR)) with persistent switching (1.5 Remark (ii)).

## 4.3 Lemma (bounded free switching). PROVED. (Any admissible T, f with F finite.)
Let U* be a finite set of carriers. There is C_{U*} (depending on f, U*) such that for every two-sided decomposition at scale t <= t_eta,
  max_{l in U*} |Delta c_l| <= C_{U*} ( 1 + || sum_{l notin U*} Delta c_l u_l ||_1 ).
*Proof.* Delta B = -sum_l Delta c_l u_l. By G3 2.3(d), nu h(B_+-) <= nu (1 + eta_Gamma)/q_0, i.e. ||P_{e-perp} U* B_+-|| <= c_f, so
||P_{e-perp} U* sum_{U*} Delta c_l u_l|| <= 2 c_f + ||U|| ||sum_{l notin U*} Delta c_l u_l||_1. The linear map c -> P_{e-perp} U*(sum_{U*} c_l u_l) on R^{U*}
is injective: if it vanishes, U*(sum c_l u_l) is parallel to U*a, hence sum c_l u_l = mu a (U* injective); the left side lies in Y = Ran T, a is in
c_00, and Y cap c_00 = {0}, so mu a = 0 and sum_{U*} c_l u_l = 0; since u_l = T e_{k(l),m(l)}/c_l (weights c_l > 0), this says T(sum_{U*} (c_l/c_l^w) e_{k(l),m(l)}) = 0,
so all coefficients vanish (T injective). A injective linear map on a finite-dimensional space is bounded below. QED.
Use: if the carriers outside U* are pinned on a window (sum_{l notin U*} |Delta c_l| <= K t), the free switching through U* is BOUNDED (not
just box-bounded, |Delta c| <= 6 lambda/t): a finitely-swallowed point has bounded switching amplitudes on every window. (The closure of a finite
set U of swallowed carriers under "slaving" -- add every coarser l with kappa_{l',l} > 0 for some l' already in the set -- is finite, because
targets are finitely supported and the S_l are disjoint; G3_ref 5.)
