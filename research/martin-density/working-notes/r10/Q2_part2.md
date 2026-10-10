# Q2 part 2 -- finite base support is free in the violation-tolerant route: Theorems UE^inf and E^{eng,RT,inf}

References: X2 = r9/X2_notes.md (Lemma M1, M2, DC, LV, Lemma UE-1, Theorem UE, Theorem E^eng) with the referee precisions of
r9/X2_ref_notes.md section 3 ((p-UE1)-(p-UE7), (c3'), (p-E1), (p-W)); V3 = r7/V3_notes.md (Lemma 2.3 RT, Corollary 2.4, Theorem 2.5
E_RT); Y3 = r6/Y3_notes.md (Theorem 2.1, raised support).  Setting of part 1; T admissible over a diagonal base (any design for which
X2's tools are stated; the designed T_fin over the base mu* is the case of interest).  Labels PROVED / SKETCH / OPEN.

Purpose.  X2's Theorem UE and Theorem E^eng are stated for a TARGET row with finite base support.  Here they are extended to a
target f with ARBITRARY support and base rows of ARBITRARY support, the only new hypothesis being that the side parts of the data use
the support within a fixed multiple of the cushion.  The engineered approximant produced at the end is norm attaining, hence has
FINITE base support; so whenever such window families exist, (f, rho g) is in cl NA and (LSC-trunc) holds at (f, g, rho).

## 2.1 Lemma M2^inf (uniform neighborhoods at arbitrary F).  PROVED.
Let f in S_{p*} (F arbitrary).  Fix, at f, in every block gamma_m in (M_m/2, M_m) with |w_m(k)| != gamma_m for all k, transfer data
(gamma_m, k^vs_{*,m}, Lambda^vs_m) for a given eta_1 in (0,1/4] (lem:transferdata), and a peak k^nat_m with alpha_m(k^nat_m) != 0.  There is
r_f(eta_1) > 0 such that every f'' with p*(f'' - f) <= r_f(eta_1) satisfies X2 Lemma M2 (a) WITHOUT its clause "F subset supp a'' and
|a''_j| >= a_min/2 on F", and X2 Lemma M2 (b).
Proof.  X2's compactness argument: if (a) or (b) failed for every r, there would be f_n -> f violating it; Proposition prop:continuity
(valid for every F: a_n -> a in l_1, scalar data converge, w_{n,m} -> w_m coordinatewise and D_m w_{n,m} -> D_m w_m) and Lemma
lem:persistence (whose proof uses only prop:continuity, the threshold lemma and dominated convergence in the blocks; no property of F)
give a contradiction.  The removed clause is the only place where M2 refers to F.  QED

## 2.2 Window families at a base row of arbitrary support (Definition)
Fix rho in (0,1), eta_0 in (0,2] with rho^2(1+eta_0) <= (1+rho^2)/2, constants A_0, A_2 >= 1, gamma_B in (0,1], C_+ >= 1, and put
delta := (1 - rho^2(1 + eta_0/2))/2.  A BASE ROW is f_0 in S_{p*} with forced data (xi_0, q_0^0, a_0, w^0, F_0, z_0, zhat_0, e_0, nu_0),
F_0 = supp a_0 ARBITRARY, and p*(f_0 - f) <= r_f/2.  A WINDOW FAMILY at f_0 is as in X2 3.1 (pieces i = 1..n at scales t_i in [T, t_1],
pairs (b^+-_i, omega^+-_i) representing g_i at f_0 with g_i(xi_0) = 0, a common finite set Omega of strict non-peaks of f_0), satisfying
X2's (U1), (U2), (U4), (U5), (U6), (U7) (with the precisions (p-UE1)-(p-UE7), (c3')), and, instead of X2's (U3):
 (U3^inf) SIDE CUSHION DOMINATION: for every piece i and every j in F_0, with s_j := sgn a_0(j),
          (s_j b^+_i(j))_- <= C_+ |a_0(j)|/t_i   and   (s_j b^-_i(j))_+ <= C_+ |a_0(j)|/t_i.
(Contact-like data on F_0 -- s_j b^+ >= 0 >= s_j b^- -- satisfy (U3^inf) with anything; X2's alternative "t_i|b^+-_i(j)| <= |a_0(j)|"
satisfies it with C_+ = 1.  (U3^inf) says nothing about the SIGN-direction usage and nothing about the average part b^theta.)
In (U6), (SEP)(i) is read "disjoint from F_0 except for (S-mass) levers".

## 2.3 The construction (X2 3.2 with three changes)
Order of choices: f -> f-constants (X2 Step 0', with (c1) replaced below) -> window family at f_0 -> s_1 -> N_w -> N'' -> levers.
 (i^inf)  N_w is chosen AFTER s_1, so large that
            tail_W := max_i ( ||b^+-_i 1_{(N_w,inf)}||_1 + ||v_i 1_{(N_w,inf)}||_1 ) <= min{ T^3, delta s_1/(64 rho), K T^2/K_w },
            alpha_0(N_w) := sum_{j > N_w} |a_0(j)| <= theta T^2/(1 + ||U||)   and   ||U* a_0 1_{(N_w,inf)}|| <= s_1 T^4
          (possible: b^+-_i, v_i, a_0 are in l_1 and there are finitely many pieces; theta, K are the constants of 2.5 below).
          The pre-row uses a_0 1_{[1,N_w]} in place of a_0: f_1 := (a_0 1_{[1,N_w]} + masses, z_0 1_{[1,N'']}) (normalized by q*).
          Coordinates of F_0 in (N_w, N''] become CONTACTS of f_1 with sign s_j (z_0 = s_j there), those beyond N'' free.
 (ii^inf) The mass set is X2's W together with
            W_F := { j in F_0 cap [1,N_w] : |a_0(j)| < 8 rho s_1 max_i |b^theta_i(j)| },
          where a_0(j) is RAISED (same sign) to modulus 8 rho s_1 max_i |b^theta_i(j)|  (Y3 Theorem 2.1's raised support).
 (iii)-(vi) as in X2 3.2 (theta-data truncated at N_w: beta^theta := b^theta 1_{[1,N_w]}, beta^+- := b^+- 1_{[1,N_w]} +- (1/2) v 1_{(N_w,inf)}).
 The resulting f' is norm attaining: a' is supported in (F_0 cap [1,N_w]) union W union (lever and pull coordinates), a FINITE set, and
 z' = 0 beyond N'' (Proposition prop:smooth(c)).

## 2.4 Theorem UE^inf.  PROVED (as a line-by-line modification of X2's refereed Theorem UE; the modifications are listed in full).
Let f be arbitrary, f_0 a base row (arbitrary support), and a window family (U1), (U2), (U3^inf), (U4)-(U7) at f_0 with scales in
[T, t_1].  Define c^f_flat as in X2 Step 0' with condition (c1) replaced by
      (c1^inf)  rho c_flat C_+ <= 1/8,
(all other conditions (c2)-(c7), (c3') unchanged), and c_flat := min(c^f_flat, gamma_B/(8 rho A_2)).  Suppose the window conditions (W-a),
(W-b) of X2 (with (p-UE6)) and (VT'), (LATE) (with (p-UE5)) hold, and N_w is chosen as in (i^inf).  Then the engineered approximant f'
of 2.3 is norm attaining (finite base support),
      p*(f' - f_0) <= K_w Pi log(e/Pi) + 2(1 + ||U||) alpha_0(N_w),   Pi := Pi_X + Pi_tr + r + t(N'')^{1/2},   Pi_tr := 2||U* a_0 1_{(N_w,inf)}||/nu_0,
and for every piece i:
      p*(f' + tau g'_i) <= 1 + (tau^2/2)(1 - delta)   for 0 < |tau| <= c_flat t_i,       p*(g'_i - rho g_i) <= K_w (K_w s_1 + c_fine + tail_W)/t_i.
Proof.  X2's proof (Steps 0'-5, Lemma UE-1) is used verbatim except at the following places.
 (M1) f-constants: Lemma M2^inf replaces Lemma M2; X2 uses M2's removed clause only in (c1) (no flip on F), which is replaced below.
 (M2) Lemma UE-1(a)-(c), (g) with Pi enlarged by Pi_tr: the truncation of a_0 beyond N_w moves e by at most 2||U* a_0 1_{(N_w,inf)}||/nu_0
      (Lemma 1.1(b) of part 1) and changes z nowhere (support beyond N_w becomes contacts of the SAME sign); so every carrier value moves by at
      most Pi_tr more (u(Uh) = <U*u, h>, ||U* u_k|| <= 1), the block scalars by K_w Pi_tr more (the clamp/threshold arguments of UE-1(c) use
      only value changes), and the normalization by q*(a_0 1_{[1,N_w]} + masses) changes no value (e' is scale invariant).  The W_F masses are
      raises ON the support: X2 Lemma M1(iv) gives ||e_A - e|| <= 2||U*(A - a)||/nu, i.e. they enter Pi_X through 2||U* X_F||/nu_0 with
      ||U* X_F|| <= 8 rho s_1 mu_1 n A_0/T (the same crude bound as Corollary M1').  In p*(f' - f_0) the l_1-truncation adds
      q*(a_0 1_{(N_w,inf)}) <= (1 + ||U||) alpha_0(N_w), twice (normalization included).
 (M3) Step 3, base, new coordinate classes at f' (all other classes verbatim):
   (2^inf) j in F_0 cap [1,N_w] (support of f').  Put A''_j := a_0(j) or the raised value; |a'_j| >= |A''_j|/2 (q* <= 2 at late stages).
       theta-piece (|tau| <= s_1): |tau rho beta^theta_j| <= s_1 rho |b^theta_j| <= |A''_j|/8 <= |a'_j|/4 (by the definition of W_F);
       +- pieces (s_1 < |tau| <= c_flat t_i, sgn tau = the side): the anti-sign part of tau rho beta^diamond_j is at most
       rho c_flat t_i C_+ |a_0(j)|/t_i <= rho c_flat C_+ |A''_j| <= |a'_j|/4 by (U3^inf) and (c1^inf); the sign-direction part never flips.
       Since a'_j + tau B^diamond_j = (1 - tau rho c_i) a'_j + tau rho beta^diamond_j with |tau rho c_i| <= 1/2 (UE-1(g) and (LATE)),
       |(1 - tau rho c_i) a'_j| >= |a'_j|/2 > |a'_j|/4: no sign change, summand 0 of Exc'.  [This replaces X2's (2) "F: no flip by (c1);
       E: by (U3) and (c2)".]
   (2'^inf) j in F_0 cap (N_w, N''] (contacts of f' of sign s_j): beta^theta_j = 0, beta^+-_j = +-(1/2) v_j, summand of Exc' at a contact
       2(-s_j tau rho beta^diamond_j)_+ <= rho |tau| |v_j|; total <= rho |tau| tail_W <= delta s_1 |tau|/64 <= delta tau^2/64 for |tau| > s_1,
       and 0 for |tau| <= s_1.  (Two-sided use of far support is thereby a TOLERATED VIOLATION of mass tail_W.)
   (2''^inf) j in F_0 beyond N'' (free coordinates of f'): included in X2's cut-off term (1/2) rho |tau| V_{>N''} (V_{>N''} := sum_{j > N''} |v_j|
       already contains them).
   Hence X2's bound Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} + 2 rho|tau| eps holds with the extra term rho|tau| tail_W, and the three
   linear terms of Step 3 plus this one are <= (delta/16 + delta/64)|tau| s_1 <= delta tau^2/16 + delta tau^2/64 for |tau| > s_1.
 (M4) Step 5: the extra delta/64 is absorbed in the slack: X2 ends with rho^2(1 + eta_0/2) + delta/8 + delta/8 + delta/8 + delta/4 + delta/8
      = 1 - 2 delta + 3delta/4 <= 1 - delta - delta/4; adding delta/32 (= 2 x delta/64 in units of tau^2/2) keeps it <= 1 - delta.
 (M5) Steps 1, 2, 4 and Lemma UE-1(d)-(f): verbatim (they use the base only through q*(B^diamond) <= 2(1 + ||U||) rho A_0/t_i + |c_i|, the
      base form (f) -- whose proof uses ||beta^diamond - b^diamond||_1 <= tail_W, unchanged -- and Lemma M1, which holds with e computed at the
      truncated pre-row).  QED

## 2.5 Theorem E^{eng,RT,inf} (averaging at the norm-attaining approximant, raise-transfer version, arbitrary F).  PROVED.
Let f in S_{p*} (F arbitrary), g in C(f), rho, eta_0, delta as in 2.2.  Suppose there are base rows f_j (arbitrary support) with
p*(f_j - f) -> 0, numbers lambda_j >= 1, lambda_j -> 1, eps'_j >= 0, and windows S_j = {T_j 2^{1-i} : 1 <= i <= n_j} carrying window
families at f_j as in 2.2 with FIXED A_0, A_2, gamma_B, C_+, such that
 (a)   p*(f_j + r rho g) <= 1 + (s(lambda_j rho r) - 1)/lambda_j + eps'_j  for all r in R;
 (E-c) p*(g - g_{j,t}) <= K_j t for t in S_j;
 (E-d) K_j T_j -> 0, n_j c_flat/K_j -> infinity (c_flat of 2.4, an f-constant);
 (E-e') eps'_j <= theta_j (T_j 2^{-n_j})^2 with theta_j -> 0;
 (E-f) the window conditions of 2.4 hold at f_j, 64 rho eps^{viol}_j <= delta s_late(j), and (p-E1): K_w c_fine <= K_j T_j^2 4^{-n_j}.
Then (f, rho g) is in cl NA((c_0, p_N), l_2^2), along norm-attaining rows f'_j with FINITE base support; in particular (LSC-trunc) holds at
(f, g, rho).  If the hypotheses hold for every rho < 1, then (f, g) is in cl NA.
Proof.  X2's proof of Theorem E^eng with Theorem UE^inf in place of Theorem UE, s_1 := s_late(j) (or smaller, keeping (VT')), N_w as in
(i^inf) with theta := theta_j, and the following replacement of its bound (B).  For every i and r, by the triangle inequality, (a) and
V3 Corollary 2.4 ((s(lambda x) - 1)/lambda <= s(x) - 1 + (lambda - 1) min(lambda^2 x^2/2, 1)):
 (B')  p*(f'_j + r g'_{j,i}) <= p*(f_j + r rho g) + p*(f'_j - f_j) + |r| p*(g'_{j,i} - rho g)
                            <= s(rho r) + (lambda_j - 1) min(lambda_j^2 rho^2 r^2/2, 1) + eps''_j + 2 rho |r| K_j t_i,
       eps''_j := eps'_j + K_w Pi log(e/Pi) + 2(1 + ||U||) alpha_0(N_w) <= 2 theta'_j (T_j 2^{-n_j})^2,  theta'_j -> 0
 (the middle term by Theorem UE^inf, the last by (E-c) and UE^inf's bound p*(g'_{j,i} - rho g_{j,t_i}) <= K_j t_i, which (p-E1) and the
 choices of s_1 and N_w guarantee).  In X2's case analysis (|r| <= r_0 with I_r empty / nonempty, |r| > r_0) the bound (B) is used only
 through "s(rho r) + eps' + 2 rho |r| K t_i", now with the extra term (lambda_j - 1) min(lambda_j^2 rho^2 r^2/2, 1), which is <=
 (1 - rho^2) r^2/48 for |r| <= 1 and <= (1 - rho^2) r_0^2/48 <= (1 - rho^2) r_0 |r|/48 for |r| > r_0 once (lambda_j - 1)(1 + lambda_j^2) <=
 (1 - rho^2) r_0^2/48 (j large; exactly V3 Theorem 2.5's accounting).  The margins used by X2 ((1 - rho^2) r^2/6 resp. (1 - rho^2) r_0 |r|/3)
 absorb it.  Hence gbar_j := (1/n_j) sum_i g'_{j,i} is in C(f'_j), (f'_j, gbar_j) attains its norm (prop:reduction(d)), and
 ||(f'_j, gbar_j) - (f, rho g)|| <= p*(f'_j - f) + p*(gbar_j - rho g) <= p*(f_j - f) + eps''_j + 4 K_j T_j/n_j -> 0.  QED

Remarks.  (1) With lambda_j = 1 and eps'_j := p*(f_j - f), (a) is the triangle inequality and 2.5 is X2's Theorem E^eng at arbitrary F.
(2) For RAISED base rows (V3 Lemma 2.3: f_j = raise of f, lambda_j = q*(a + Delta a_j)), (a) holds with eps'_j = 2||U* Delta a_j|| +
p*(L*(w^{(j)} - w)) (V3 Corollary 2.4): the raise mass never enters, only its Hilbert footprint and the normer change.  For LOWERED base
rows (part 1, Lemma LT) (a) holds with lambda_j = 1 and eps'_j = 2 max_r Lambda(r) + eps''_M -- usable when the lowered coordinates carry
no cushion usage at the relevant scales.
(3) What this settles.  "Truncation" is free in the violation-tolerant route as well: the only requirement on the support of the base
row is (U3^inf), side cushion domination, which raises (V3 Lemma 2.3) and the pinning Lemma P (U2) provide (part 3).  The far support of
an infinite-F base row is converted into contacts INSIDE the engineered approximant, and its two-sided use by the side data becomes a
violation of mass tail_W, which is made <= delta s_1/(64 rho) by taking N_w after s_1.  This is the violation-tolerant counterpart of Y3
Theorem 2.1 (fixed data) and of V3 Corollary 4.2.
(4) Consequently (LSC-trunc) at (f, g, rho) -- indeed (f, rho g) in cl NA -- follows from the EXISTENCE of window families with (U1), (U2),
(U3^inf), (U4)-(U7) at base rows f_j satisfying (a), (E-c)-(E-f).  Producing them is the infinite-F exactification problem (part 3).
