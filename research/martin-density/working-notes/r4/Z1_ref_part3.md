# Z1 referee, part 3: Z1 part 3 (far lowering, the approximants f^L, the reduction, the scale arithmetic)

## 3.0 Design adjustment (Z1 part 3 preamble). Verdict: CORRECT, but UNNECESSARY.
S_l := {2^l (2i+1) : i >= 0} \ {j_0} are pairwise disjoint infinite sets with min S_l = 2^l (or the next element) increasing; G3 Theorem A uses
only disjointness and infiniteness of the S_l (allowedness (b) does not involve min S_l), and Theorems B, C use nothing else. So A-C survive.
The adjustment is not needed for 3.2: since the S_l are pairwise disjoint, every finite set G meets only finitely many S_l, so
(union_{l > L} S_l) cap G is empty for L large. Hence z^L -> z coordinatewise and F cap S_l = empty for l > L (L large) hold for ANY disjoint family.

## 3.1 Far lowering of one swallowed set (Z1 3.1). Verdict: (a), (b) correct as NECESSARY conditions; (d) is HEURISTIC, not PROVED.
(a) ||h_{l_0} 1_{G_n}||_1 <= sum_{s > n} 2^{-s} = 2^{-n} and ||h_{l_0}||_1 >= 2^{-m_{l_0}}: room ratio <= 2^{m_{l_0} - n}. Correct.
(b) The budget gives gamma q_0' |Delta c_{l_0}| delta'_{l_0}(n) <= t + (finer terms) (G3 2.3(b), 3.2 at f'_n): switching of size |Delta c| is IMPOSSIBLE
    below t ~ gamma q_0' delta' |Delta c|. "Affordable exactly for t >~ theta_n" also asserts sufficiency, which is not shown.
(c) Labelled HEURISTIC. Agreed (L* is not bounded below).
(d) "PROVED as arithmetic from (a)-(c)": since (c) is heuristic, (d) is heuristic. The further statements "lowering more only moves the band,
    it cannot be removed" and "the band needs an EXACT transfer" are HEURISTIC. (They are plausible and match P2A's scale decoupling.)

## 3.2 Approximants f^L (Z1 3.2). Verdict: CORRECT (PROVED).
(a) z^L - z is supported in union_{l > L} S_l, which eventually misses every finite set; a unchanged; z^L = z = sign a on F for L large.
    By 1.1(a) (re-derived in part 1), f^L -> f in norm.
(b) For l > L: z^L = 0 on S_l, so S_l subset J^L_gamma for every gamma < 1 (F misses S_l): room ratio 1, delta'_l = delta°_l. For l <= L: z^L = z on S_l
    and F is unchanged, so the room is exactly that at f. Hence f^L in R_0 iff each S_l (l <= L, m(l) <= N) contains some j notin F with |z_j| < 1
    (finitely many l, so a common gamma and vartheta exist). Correct.
(c) For l <= L, u_l = (y_l + delta_l h_l)/n_l vanishes on union_{l' > L} S_{l'} (h_l lives on S_l; y_l misses S_{l'} for l' >= l by allowedness (a)), so
    u_l(zhat^L) = u_l(zhat). The coarse block values are w^L_m(k) = clip(c^L w~_m(k), M^L_m) with the same unclipped value w~ and normalisation
    constants (c^L, M^L) -> (c, M); so "they differ only through the normalisations" is literally true. Note: near-threshold coarse coordinates
    (degenerate peaks) may change status; this is harmless and still "through the normalisations".
(d) |Delta c_l| <= 6 lambda_l/t (G3 3.1) and sum_{l > L} lambda_l <= c_{L+1} ((P2)). Correct.
Additional remark. p*(f^L - f) is not computed in Z1. Heuristically it is O(c_{L+1}) (the fine signature changes are weighted by lambda_l), so the
slack covers |tau| >~ sqrt(c_{L+1}/(1 - rho^2)) -- the same threshold as 3.2(d). This supports Z1's picture that the f^L transition band sits at
scales <~ sqrt(c_{L+1}), where the fine carriers at f are only box-bounded.

## 3.3 Reduction (Z1 3.3). Verdict: CORRECT for F finite; INCOMPLETE for F infinite (fixable).
For F finite: (B) gives f' in R_fin, g' in C(f') with p*(f' - f), p*(g' - rho g) small; (A) gives (f', rho' g') in cl NA; let rho' -> 1. Correct.
For F infinite, Z1 says "see part 4", but part 4 (Theorem B^inf) covers only (SR) points. A point with infinite F and failing (SR) is covered
by neither (A) nor (B) as stated. Fix: state (B) for every f in S_{p*} (approximants in R_fin then require truncating a), or define
R_fin^inf := {(SR) for l > L, any F} and extend (A) to it (via B^inf-type clamping). Since (A) and (B) are OPEN anyway, this is bookkeeping.
"Neither is implied by the other" is unproved; harmless.

## 3.4 The scale arithmetic (O-c) (Z1 3.4). Verdict: arithmetic CORRECT; conclusion is a statement about one method (label it so).
Independent re-derivation of the obstruction. Transplant G3 5.2 to an approximant f': for each window scale t_i use a piece valid at f' for
|s| <= c_1 t_i; for the indices with c_1 t_i < rho|s| one needs a comparison bound at f', and the only one available without a mate at f' is
p*(f' + s rho Psi_i) <= p*(f + s rho g) + p*(f' - f) + rho|s| ||Psi_i - g||, whose ZEROTH-order term p*(f' - f) enters with weight #I_f/n. At
|s| ~ 2 c_1 t_n (one index in I_f) this forces p*(f' - f) <~ n (1 - rho^2) c_1^2 t_n^2. (Z1 states <~ (1 - rho^2) r^2 with r ~ c_1 t_1 2^{-n}; my
bound is larger by the factor n, which is irrelevant.) With a first-order mismatch eta ~ K t_1/n handled as in S3 Theorem D (cost 2 rho |tau| eta
for |tau| > s_1) one needs s_1 >~ eta/eps_0 and p*(f' - f) >~ s_1 (window masses). Since K t_1/n >> n t_1^2 4^{-n}, the two requirements are
incompatible. Correct.
Caveats: (1) "p*(f' - f) >~ s_1" is a generic lower bound, not proved (L* is not bounded below; base and block perturbations could partly cancel).
(2) Both premises are properties of upper-bound chains, so the conclusion is "this combination of the two methods fails", not an impossibility
statement about recovery. Z1's wording ("cannot be combined naively") is accurate; the table label "PROVED" should read "PROVED (arithmetic of
a specific estimate chain)".
(3) The obstruction disappears if the mismatch is EXACTLY zero: then s_1 in Theorem D can be taken << n t_n^2 (s_1 is a free parameter there;
the O(s_1) linear terms of Theorem D Step 3 come from the approximant itself and are paid for |tau| > s_1), and the averaged data are two-piece
data in Theorem D's format (base +-z-signed on K, block parts finitely supported in Q_m, kappa_w <= 1 + eta_0 by convexity of Gamma_w), modulo
(SC_m) in blocks with Delta d_m < 0. So (RS1) as Z1 states it (one functional per window scale, both one-sided decompositions exact) is the
right target. (Mismatches only in the "normalisation directions" a, R_m* w_m are NOT enough: Theorem D tolerates them only at size <~ eps_0 s_1.)
