# G3 referee, part 1: line-by-line check of parts 1-3 (Thm A, R_0, toolkit, pinning)

Setting of G3: finite block set I_N (norms p_N), designed T (SLD). G3_notes.md = concatenation of G3_head + G3_part1..6 (checked: identical).

## Theorem A (SLD design) -- CORRECT
* Recursion (D1) is well founded: c_l -> (y_l allowed at l) -> n_l, delta°_l, Lambda°(l) -> T_hi(l), n^w_l, T_lo(l) -> c_{l+1}.
* n_l in [3/4,5/4] since q*(delta_l h_l) <= (1+||U||) delta_l ||h_l||_1 <= 1/4. (P2): c_{l'+1} <= c_{l'}/4 gives sum_{l'>l} c_{l'} <= (4/3) c_{l+1};
  sum lambda <= (2/3) c_{l+1}. (P3) holds by definition (log2(T_hi/T_lo) = n^w_l exactly).
* Density of every tail of every block: a target y^(i) (finite support) meets finitely many S_l', and c_l -> 0, so (a),(b) hold for all
  large l; i occurs infinitely often in (i_k) and iota(.,m) is increasing in k; delta_l -> 0, n_l -> 1. Correct. (Density in S_{q*}
  implies Lemma B's "dense in S_Y" since Y = Ran T is dense in X*.)
* Injectivity / Ran T cap c_00 = {0}: for s in S_{l'} only u_{l'} (signature) and finer targets touch s; (b) at the first finer index
  L(s) touching s gives the tail bound (8/3)||x||_inf c_{L(s)} <= (4/3)||x||_inf 2^{-2s} c_{l'} delta_{l'}; so |Z(s)| > 0 for all large
  s in S_{l'} (infinite). Correct.
* Signature privacy (P1): for s in S_l, u_{l'}(s) = 0 for l' < l (targets of index l' avoid S_{l''}, l'' >= l'), u_l(s) = delta_l 2^{-s}/n_l,
  u_{l'}(s) = y_{l'}(s)/n_{l'} for l' > l. Correct.

## Class R_0 -- CORRECT
NA points: a' in c_00, z' in c_0 (normer in c_0, Ue in c_0), so N \ J_gamma = F' cup K' finite for small gamma; only finitely many S_l
meet it, each keeps positive h_l-mass (S_l infinite); theta := min ratio^{1/l}. Base-tame: same with gamma = 1 - sup|z_j|. Correct.

## Part 2 toolkit (any admissible T) -- CORRECT (re-derived)
* 2.1: optimal decompositions exist (weak* compactness of B_{q*} + L*(B_{V*})); g in C(f) gives p*(f +- t g) <= s(t).
* 2.2: compactness proof correct (uniqueness of forced decomposition; U* weak*-to-norm on bounded sets; l_1 Kadec-Klee for
  coordinatewise convergence + norm convergence; D_m compact). t_eta depends on (f,g,eta): fine (g fixed in Thm B).
* 2.3(a): from q*(A) >= A(zhat), N_m(W) >= <W,zeta_m>/sigma_m and g(xi) = 0; each term <= weight*t/2, sum zero => each >= -t/2.
* 2.3(b): budget q_0 E_q + sum sigma_m e_m <= s(t)-1 <= t^2/2 (re-derived from q_0 + sum sigma_m = 1 and (f+tg)(xi) = 1);
  E_q(a+tB) >= sum_{j notin F}(|tB_j| - z_j t B_j); pointwise identity |x|+|y| <= |x-y| + (|x|-zx) + (|y|+zy) (difference
  |x-y| - z(x-y) >= 0). Correct.
* 2.3(c),(d): block excess = sum_P |alpha_k|(||W||-sigma_k W(k)) + (||DW|| - <DW,Dw>/C) with ||alpha||_1 = 1 (from M + C = 1);
  Hilbert identity (C (7.2)) gives the lower bounds; Gamma_w <= (1+||U|| eta/nu) max_m (1+eta/C_m). Correct.
* 2.4: all items re-derived ((d): d(omega_+) - d_+ = <Omega_+,zeta>/sigma + sum_P |alpha||omega_+|; (e),(f) box). Correct.
* 2.5: injectivity of beta -> (P_{e-perp}U*beta, beta(zhat)) on l_1(F) (U* injective, a(zhat) = 1). Correct; K_F depends on f only.

## Part 3 pinning (SLD, f in R_0) -- CORRECT
* 3.1 box bound from |t Omega(k)| <= s(t) + 1 <= 3.
* 3.2: -Delta B(s) = Delta c_l delta_l 2^{-s}/n_l + sum_{l'>l} Delta c_{l'} y_{l'}(s)/n_{l'} on S_l (P1); l_1 norm over S_l cap J_gamma. Correct.
* 3.3: S_l <= X_l/delta'_l + (1 + 4/(3 delta'_l)) S_{l+1}, unrolled from l_* down; sum_l kappa_{l',l} <= 4/3 (disjoint S_l). Correct.
  Lambda_f <= vartheta^{-l(l+1)/2} Lambda° <= vartheta^{-l^2} Lambda°.
* 3.4: sum_l E_l <= sum_{J_gamma} (|B_+| + |B_-|) <= t/(gamma q_0) (2.3(b)); fine carriers <= 6 c_{l_*+1}/t <= 6 T_lo(l_*)^3/t <= 6 t^2
  (uses t >= T_lo(l_*)). Correct.
* 3.5: (a) ||u_l||_1 <= 1; (b) from 2.3(b); (c) Delta d M = <Dw, D Delta Omega>/C + r, |r| <= 2t/sigma_m, and
  Phi_k^2 w(k) Delta Omega(k) = Phi_k w(k) Delta c_k / m. Correct.
Conceptual check: exact finite relations sum_{l <= L} Delta c_l u_l = beta with beta supported on F cup (non-roomy set) force Delta c = 0
(top index L has an unshared roomy signature); infinite relations are cut by the box bound on fine carriers inside a window.
This is exactly why P1-type (exact resonance through a contact set) and C-referee-type (kink re-splitting) mechanisms cannot occur
at amplitude >> Lambda_f t at f in R_0.
