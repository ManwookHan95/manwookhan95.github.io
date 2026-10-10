# U4-ref part 1 — T_final, Lemma W, Theorem 2.2 (admissibility), Theorem 2.3 (features)

Refereed: r8/U4_notes.md Sections 1-2 (= U4_part1 1.1-1.6), against the note (def:admissible, rem:lemmaB, lem:martintail,
prop:smooth, def:SLD, thm:SLD, def:R0, lem:R0, thm:R0, thm:reductionZ), V1 1.2-1.4 (D_Omega), V2 Def. 2.2 / Lemma 2.1, V3 3.1,
V4 Section 3 (design conditions) and V4-ref R6, R11.

## 1.1 Definition of T_final, U_final: re-checked line by line
- Base: U k_s = mu_s e_s, mu_s = 2^{-s^2-1}.  Compact (diagonal, mu_s -> 0), range contains c_00 (dense in c_0), U^* e_s^* = mu_s k_s,
  U^* injective on l_1, ||U|| = mu_1 = 1/4.  q^*(a) = ||a||_1 + (sum mu_s^2 a_s^2)^{1/2}.  prop:smooth(c) (NA((c_0,q)) = c_00) uses
  only: B_q = B_{c_0} + U(B_H) closed (U compact), z in c_0 forces finitely many |z_j| = 1, and injectivity of U^* (strict
  convexity of q^*).  Valid.  CORRECT.
- S_l = {2^l(2i+1) : i >= 1}: even, pairwise disjoint (2-adic valuation l), min S_l = 3*2^l, consecutive gap 2^{l+1}.
  Z_0 = N \ union S_l = odd numbers ∪ {2^r : r >= 1}.  H_l = 2^{-3*2^l}/(1 - 2^{-2^{l+1}}); H_1 = 2^{-6}*16/15 = 1/60.
  delta^max_l = min{2^{-l}, (5 H_l)^{-1}} = 2^{-l} for every l (5 H_l <= 1/12 < 2^l).  CORRECT.
- (GM) choice of delta_l (l >= 2): 2*3^{|supp y_l|} excluded open intervals, each of delta-length 2g_l/H_l, total <=
  4*3^{|supp|} g_l/H_l = delta^max_l/8; the admissible set [delta^max/2, delta^max] minus a finite union of open intervals is
  compact, of measure >= 3 delta^max/8 > 0; the maximum exists.  CORRECT.  (V4-ref R6 lists delta_l (2) BEFORE y_l (3), which is
  inconsistent because the (GM) intervals depend on y_l; U4's order y_l -> delta_l is the only consistent reading.  Precision (q1).)
- n_l in [3/4, 5/4]: q^*(delta_l h_l) <= (1 + ||U||) delta_l H_l <= 1/4.  CORRECT.
- (W1)-(W7): each is a positive number computable from earlier data.  (W4) is a finite list.  (W7) is the (SF_tau) first half of
  level l-1 transported to c_l via sum_{l'' >= l} lambda_{l''} <= sum_{l''>=l} c_{l''}/4 <= c_l/3 (lambda = m 2^{-m-k} c <= c/4 since
  m 2^{-m} <= 1/2 and 2^{-k} <= 1/2; c_{l''+1} <= c_{l''}/4).  Re-derived: (1 + ||U||) sum_{l''>l} lambda_{l''} <= (1 + ||U||) c_{l+1}/3
  <= 2^{-10} tau_l lambda_l delta_l 2^{-(m(l)+k(l)+min S_l)} eta_l/n_l exactly.  CORRECT.
- (FD) stages k in {2^r : r >= 1} (k = 1 is NOT an FD stage, so the first carrier of every block takes a scheduled target);
  j_l odd, > 9 and > every earlier target coordinate: in no S_i, owned by l (u_{l'}(j_l) = 0 for l' < l), and o_N(j_l) = l when
  m(l) <= N.  |y_l(j_l)| = 1/(1 + mu_{j_l}) >= 4/5 > 1/4 >= (1 + ||U||) delta_l H_l, which is V4's (FD) inequality with
  ||y_l||_1 - |y_l(j_l)| = 0 and max_i s_i = ||U||.  CORRECT.

## 1.2 Lemma W (well-foundedness, positivity, N-independence): CORRECT
I traced every dependency: (1) target: supports of y_{l'} (l' < l), S_{l'}, schedule; (2) delta_l: y_l, H_l; (3) n_l etc.;
(4) c_l: c_{l-1}, b(l-1, M(l-1)) [step (6) of stage l-1], delta_l, H_l, g_l, y_l, lambda_{l-1}, delta_{l-1}, eta_{l-1}, n_{l-1};
(5) level data including c_l (through Phi_l in D(l)) — no factor of Design(l) refers to c_{l+1} or later weights (checked for
D(l), G^*, H_comb, G^**, Xi^Y, H_tune, the cones/rays (defined by u_{l''}(j), j in T(l)), the polynomials pi_O (coefficients =
design numbers, variables = values), Lip, C_L, N_L (Lojasiewicz for a FIXED finite family), delta_comb, delta_sh, rows, cols);
(6) Design(l), omega(l), C_L, N_L, Lip, C_*, predecessor values.  No forward reference.  Positivity: m^nat > 0 (infinite
remainder of S_{l''}), c_l > 0, g_l > 0, C_L may be taken >= 1, Lip >= 1.  N-independence: patterns/objects range over subsets of
[1, l] and the blocks m(l'') of carriers l'' <= l; omega(l) is the same for every N; for p_N an object involving an absent
carrier gets value 1, which lies in no band (all bands lie in (0, 1/4)).  CORRECT.

## 1.3 Theorem 2.2 (admissibility; Martin's Lemma B): CORRECT
- (T-a): q^*(T e_{k,m}) = c_{j(k,m)} q^*(u) = c_{j(k,m)} <= c_1 = 1 by (W1), equality at l = 1.  (C7 is what makes c_1 = 1 possible.)
- (T-b), (T-c): re-derived.  For s in S_{l'}: Z(s) = x_{l'} c_{l'} delta_{l'} 2^{-s}/n_{l'} + sum_{l > l', s in supp y_l} x_l c_l y_l(s)/n_l
  (targets y_l, l <= l', vanish on S_{l'} by allowedness (a); other signatures vanish by disjointness).  (W4) at the least index
  L(s) gives 2 c_{L(s)} <= tau 2^{-2s} c_{l'} delta_{l'} <= 2^{-2s} c_{l'} delta_{l'}; |y_l(s)|/n_l <= 4/3; sum_{l >= L} c_l <= (4/3) c_L;
  so the tail is <= (8/9)||x||_inf 2^{-2s} c_{l'} delta_{l'} and |Z(s)| >= c_{l'} delta_{l'} 2^{-s}(|x_{l'}|/n_{l'} - (8/9)||x||_inf 2^{-s}) > 0
  for all large s in S_{l'} (infinite): Z notin c_00.  So T x in c_00 implies x = 0: injectivity and Y ∩ c_00 = {0}.
- (T-d): y^(i) satisfies (a) and (c) at every l > max(supp y^(i) ∪ {l' : S_{l'} ∩ supp y^(i) != {}}); i occurs infinitely often in
  (i_r); l = j(k_r, m) -> infinity; q^*(u_l - y^(i)) <= 2 q^*(delta_l h_l)/n_l <= (8/3)(5/4) 2^{-l} -> 0.  Dense family => dense.
- Lemma B conclusion: ||T|| = sup q^*(T e_{k,m}) = 1 (l_1(N x N) domain); Y = range is a separable operator range; Y is dense
  (its closure contains a dense subset of S_{q^*}, hence B_{q^*}); Y ∩ NA((c_0,q)) = Y ∩ c_00 = {0}; per-block normalized density.
  Martin's proof uses nothing else (rem:lemmaB).  NOTE: here Y is DEFINED as the range of T (Martin's Step 1 takes Y from
  [KLMW, Prop. 2.4] first); the four properties Martin needs of Y (separable operator range, dense, Y ∩ NA = {0}, T maps onto a
  set with dense normalized block images) hold, which is all Step 2-10 use.  CORRECT.
- (P1), (P2), sub-window (P3): re-derived; b(w) <= eta(w) <= T_lo(w)^4 <= 2^{-4 n(w)}, n(w) >= Q(w) >= (4/u)^{20} >= 16/u, so
  b(w) <= 2^{-64/u} < u; u(w^+) = b(w); bands are consecutive disjoint intervals; sum_{l'>l} lambda_{l'} <= c_{l+1}/3 <=
  b(l, M(l))^2/3 <= b(w)^2/3 for every sub-window w of level l (b decreasing in i).  CORRECT.
- (d) V2's (2.1): beta = (1 + Lip C_*) b = min{eta, (eta/C_L)^{N_L/2}} gives C_L beta^{2/N_L} <= eta; eta <= T_lo^4/(l Design) <=
  1/Design <= 1/C_L (C_L a factor >= 1 of Design).  Last claim: T_lo(w) <= 2^{-Q(w)}, Q(w) >= (4 Design/u)^{20}, so
  Design^4 T_lo <= Design^4 (u/(4 Design))^{40} <= u/8 for EVERY l (the restriction "l large" is unnecessary).  CORRECT.

## 1.4 Theorem 2.3 (features F1-F11): CORRECT, with precision (q2)
(F8) B_mu = 2^{2 sigma^2 + sigma + 2} >= 8^sigma = 2^{3 sigma} since 2 sigma^2 - 2 sigma + 2 > 0.  (F9) c_{l+1} <= b(l,M(l))^2 <=
T_lo(l,M(l))^8.  (F10): (SF_tau) first half via (W7) + (P2); (SF*) both halves (tau <= 1; (W5) for l >= 2); (b') = (W4);
(GM) for l >= 2 = step (2) + (W6) (Phi_l = 2^{-m-k} c_l <= g_l 2^{-l}); (Z0); (FD).
(q2) (SF*) second half and (GM) are imposed only for l >= 2.  The (SF*) second half "c_l <= c_{l-1} delta_l 2^{-min S_l - l - 10}/(1+||U||)"
has no meaning at l = 1 (no c_0), so this is not a restriction; (GM) at l = 1 is C7 (part 2).
