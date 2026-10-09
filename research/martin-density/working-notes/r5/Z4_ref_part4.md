# Z4 referee, part 4: scope of Theorem A; one-sided d-resources (E-d) made precise; far lowerings

## 4.1 What Theorem A adds (relative to Corollary cor:BTrecovered and Theorem thm:S). PROVED (bookkeeping).
(BT) allows ANY contact set, so rows with infinitely many swallowed signature sets but finitely many strict non-peaks, no degenerate peaks
and (MS) are already in R. Theorem A (with (H2'') of part 3) adds rows with F finite, infinitely many swallowed carriers not all resonant
and d-neutral, satisfying (H3), (DR), (W_inf), (H2''), and violating (BT) through infinitely many strict non-peaks, degenerate or weak good or
anti-sign peaks, or weak swallowing-sign peaks with M_f/Lambda° within the ladder along a subsequence. CORRECTION of an earlier draft of this
part: (W_inf) does NOT force (MS) on the swallowing side (it bounds M_f/Lambda° only along a subsequence, and Lambda°(l) may exceed 1/c_l);
Remark 5.5(i) needs M_f(l) <= (l 2^{l^3})^3 for all large l. The class is special (maximal contact, F finite: f depends only on finitely
many numbers a_j). No measure-theoretic claim.

## 4.2 Lemma R (one-sided d-resources make the d-row Hoffman constant design-scale). PROVED.
Let block m be such that q_l >= 0 for every swallowed carrier l of block m with k(l) in Q_m, and let l_1 be a swallowed strict non-peak of
block m with q_{l_1} > 0 whose vector eps_{l_1} u_{l_1} 1_{F^c} is z-signed and supported in K (zero cost). Then for every finite U ∋ l_1,
U ⊂ B, the l_1-Hoffman constant of the system defining Z_U (violation viol_{kappa(f,U)} + sum_m |delta_m|) is at least 1/q_{l_1}, and
q_{l_1} <= Phi_m(k(l_1))/(mC_m) <= c_{l_1}/(4mC_m).
Proof. tau := e_{l_1} has zero cost and vanishes at peaks, so viol_{kappa(f,U)}(tau) = 0, delta_m(tau) = q_{l_1}, delta_{m'}(tau) = 0. Every
tau' in Z_U satisfies tau' >= 0 (zero cost, Lemma 2.1 (Z1)), tau'_l = 0 at peaks and sum_{l in U, m(l)=m} q_l tau'_l = 0 with all q_l >= 0
on the strict non-peaks of block m; hence tau'_{l_1} = 0 and ||tau - tau'||_1 >= 1. So the constant is >= 1/q_{l_1}. Finally |w| <= 1,
Phi_m(k) = 2^{-m-k} c_l. QED.
Consequence (PROVED): without (DR), H^Z_f(l) >= max{ m C_m / c_{l'} : l' <= l a zero-cost one-sided strict non-peak as above }, and
c_{l'} <= T_lo(l'-1)^3 <= 2^{-3 n^w_{l'-1}}: a DESIGN-scale constant, fixed after all data that determine the windows below level l'.
HEURISTIC consequence: Corollary 4.1 absorbs it only along windows l >> l' (one-sided d-resources that are SPARSE relative to the ladder);
whether a given design leaves room for this depends on the free choice of the sets S_l (through Lambda°), so I do not claim a sharp
dichotomy. (E-d) is the non-sparse case.
HEURISTIC (one-line estimate, for orientation): with all q_l >= 0 the d-identity only gives sum_U q_l (tau_l)_+ = O(K_1 t); since
q_l = lambda_l |w(k(l))|/(m^2 C), a carrier with lambda_l ~ t can carry tau_l ~ 1/|w(k(l))| at scale t, so making the data exactly d-neutral by
deleting one-sided switching costs O(1) in l_1, not O(t). This is why (DR) (two-sided repair directions) is the natural hypothesis.

## 4.3 Far lowerings (route (2)): referee assessment.
Prop 1.2 (with the fixed step (iv)) and Prop 1.3 are correct. Additional observation (PROVED, elementary): f^L has B(f^L) = B(f) ∩ [1,L]
and all carriers l > L good with full room (S*_l = S_l, r*_l = delta°_l, so (W*) is automatic at f^L once r*_l > 0 for its good
l <= L); if f^L satisfies (H2'') and (H3) (not automatic from f: coarse margins move by O(eps_L)), Corollary 4.2(b) gives f^L ∈ R; the open
question is only dist(rho g, C(f^L)) -> 0. Windowed averaging AT f^L with target rho g works on any window lying entirely in the inherited
band [A t_L, 1] (two-sided decompositions of rho g at f^L exist there by Prop 1.3(a), and Lemma lem:avgfunctionals only uses the bound (B)
p*(f^L + r rho g_t) <= s(rho r) + rho|r| K t and the local expansions); the windows in that band are windows l_* <= L+1 whose coarse
swallowed sets are the same at f^L and at f (Prop 1.3(c)), with block data moved by O(eps_L) in sup norm (fix of Prop 1.2). Hence a proof
along far lowerings needs, for some window inside the band, exactly the absorbability that (W_inf) asks for at f: I agree with Z4's
verdict (HEURISTIC as a "cannot help" statement; there is no proof that no other approximant helps).
