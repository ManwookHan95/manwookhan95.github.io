# Z1 referee notes (assembled): verification of Z1 (Lemma Z via far lowering and scale decoupling) and the referee's additions

Setting: canonical base q, finite block set I_N (p := p_N, every N; Remark martin-tail, G3_referee sec. 4, transfers to Martin's p);
the SLD operator T of G3 1.2. Notation of G3/Z1. Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Parts: Z1_ref_part1.md (Z1 1.1-1.5), Z1_ref_part2.md (Z1 part 2), Z1_ref_part3.md (Z1 part 3), Z1_ref_part4.md (Z1 part 4),
Z1_ref_part5.md (Z1 part 5 + Theorem M). Scripts: Z1ref_work/scalar_checks.py, Z1ref_work/hm2.py (and hoffman_matching.py, the variant
without an exact resonance). Report: Z1_referee.md.

## Summary of verdicts
| Z1 claim | Verdict | Where |
|---|---|---|
| R_0-approximants exist; Lemma Z is a lower-semicontinuity statement | correct with a fixable overstatement: Lemma Z is PER MATE; the uniform "rho C(f) subset Li C(f'_n) along one sequence" is only sufficient. Far lowerings must also truncate a when F is infinite | 1.1 |
| Exposed face {phi : phi(xi) = 1} = {f} | correct (PROVED) | 1.2 |
| "Hence rho C(f) subset C(f') forces f' = f" | WRONG (non sequitur; only the sufficient condition (*) fails). Exact criterion: f'^2 + rho^2 r~_f^2 <= p^2; it forces only C(f) subset ker xi'. The pattern is false in ell_4^3. New: C_base(a) subset C(f') for every f' with base part a | 1.3 |
| Local reduction (P2A 1.4 for non-NA f') | correct | 1.4 |
| Theorem B* (window-pinned mates, F finite) | correct (traced every use of (SR) and gamma in G3) | 1.5 |
| Ray lemma; budget form; consequences | correct; 2.4(b) "not below" and 2.4(c) "only if" are HEURISTIC, not PROVED | 2.1-2.4 |
| Far lowering of one swallowed set | (a), (b) correct as necessary conditions; (d) is HEURISTIC since it rests on (c) | 3.1 |
| Approximants f^L and reduction (A)+(B) => density | correct for F finite; for F infinite (B) must be stated for all f; the design adjustment is harmless but unnecessary | 3.0, 3.2, 3.3 |
| (O-c): naive window averaging + S3 Thm D fails | arithmetic correct; it is a statement about one estimate chain; it disappears if the mismatch is exactly 0 | 3.4 |
| Flip lemma (infinite F) | correct | 4.1 |
| Theorem B^inf | SKETCH as labelled; plausible; the import is the C referee's two-line remark | 4.2 |
| Bounded free switching | correct | 4.3 |
| Common-functional obstruction (5.2) | WRONG as a conclusion: an artefact of fixing the + component as g - Rem_+. Under Z1's own (E1), (E2) the obstruction is removed by trimming the + contact base by O(K t) and Hoffman-projecting the free switching onto the polyhedral cone of exact d-neutral resonances | 5.2-5.3 |
| (referee) Theorem M: finitely swallowed points with exact free resources are in R | SKETCH (steps 1-4 of the matching PROVED) | 5.4-5.5 |

# Z1 referee, part 1: Z1 sections 1.1-1.5 (approximants in R_0, exposed face, local reduction, Theorem B*)

Setting as in Z1: canonical base q, finite block set I_N (p := p_N), the SLD operator T of G3 1.2. Notation of G3/Z1.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Scripts: r4/Z1ref_work/.

## 1.1 R_0-approximants and the "lsc reformulation" (Z1 1.1). Verdict: correct, with one overstatement.
(a) Re-derived (G3_ref 3.3). Given q*(a') = 1, z' in B_{l_inf}, z' = sign a' on supp a': zhat' := z' + U e' (e' = U*a'/||U*a'||) satisfies
    a'(zhat') = ||a'||_1 + ||U*a'|| = 1 and q**(zhat') <= 1, so q**(zhat') = 1; with q_0' := 1/(1 + sum_m |R_m** zhat'|_m), xi' := q_0' zhat',
    w'_m := J_m(R_m** xi') one gets f'(xi') = q_0' + sum_m |R_m** xi'|_m = 1 = p**(xi') and p*(f') <= max(q*(a'), max_m N_m(w'_m)) = 1.
    Continuity: if a' -> a in l_1 and z' -> z coordinatewise and boundedly, then ||R_m**(zhat' - zhat)||_1 <= sum_k lambda_k |u_k(zhat' - zhat)| -> 0
    by dominated convergence (sum_k lambda_k < infinity, |u_k(zhat' - zhat)| <= 2(1 + ||U||)), so the normalisations converge, J_m is norm-to-weak*
    continuous (V_m smooth, Smulian), and L* is weak*-to-norm continuous on bounded sets (L compact). Hence f' -> f in norm. CORRECT.
(b) Canonical truncations are NA (zhat'_n in c_0), hence in R_0 (G3 1.4(a)). Far lowerings: (SR) holds because the S_l are pairwise disjoint, so
    only finitely many S_l meet [1,n] and each keeps the positive mass of S_l cap (n, inf). CORRECT, with one omission: when F is infinite,
    a must also be truncated (otherwise F' = F is infinite and f' is not in R_0); Z1 specifies only z'_n.
(c) OVERSTATEMENT. Z1 writes "Lemma Z is purely the statement rho C(f) subset Li C(f'_n) along SOME sequence in R_0 (equivalently, liminf
    r~_{f'_n}(x) >= rho r~_f(x) on a countable dense set, along one sequence)". That is the UNIFORM statement (one sequence for all mates). Lemma Z
    (G3 1.1) is a PER-MATE statement: for each (f, g, rho) there is an R_0-sequence f'_n -> f, which may depend on g, with dist(rho g, C(f'_n)) -> 0.
    The uniform statement implies Lemma Z. The converse is not shown: going from separate sequences to one common sequence is exactly the
    "common first row for finitely many mates" condition of the BRIEFING's (R3) reduction, which does not follow from ell_2^2-density.
    Fix: state the reformulation per mate. Nothing else in Z1 depends on the uniform version.

## 1.2 Exposed face (Z1 1.2). Verdict: the lemma is CORRECT (PROVED).
Re-derived: phi = a' + L*w' (A Fact A, infimum attained); phi(xi) = 1 forces a'(xi) = q**(xi) and <w'_m, zeta_m> = |zeta_m|_m for each m.
Two points that Z1 asserts or leaves implicit, both true:
 * zeta_m = R_m** xi != 0 for every m, because R_m** is injective on l_inf: if u_{k,m}(xi) = 0 for all k, then xi vanishes on a norm-dense subset
   of S_{q*} (Lemma B), so xi = 0. This is needed to invoke smoothness of |.|_m at zeta_m.
 * Uniqueness of the maximiser of a'' -> a''(xi) on B_{q*} follows from strict convexity of q* (Hilbert norm strictly convex, U* injective):
   if q*(x) = q*(y) = q*((x+y)/2) = 1, then U*x = lambda U*y with lambda >= 0, so x = lambda y and lambda = 1.

## 1.3 The "consequence" (Z1 1.3). Verdict: WRONG as stated (non sequitur; not load-bearing).
Z1 table #2 says: "hence rho C(f) subset C(f') with f' in S_{p*} forces f' = f | PROVED", and 1.3 draws the "moral" that every approximant f' != f
must lose part of rho C(f). The proof only shows that the SUFFICIENT condition (*) f'^2 <= rho^2 f^2 + (1 - rho^2) p^2 fails for f' != f.
 * Exact criterion (PROVED). Put r~_f(x) := max_{g in C(f)} g(x) (support function; C(f) is weak*-compact). Then
     rho C(f) subset C(f')  <=>  f'(x)^2 + rho^2 r~_f(x)^2 <= p(x)^2 for all x in c_0.
   Since r~_f <= r_f = sqrt(p^2 - f^2), the right side p^2 - rho^2 r~_f^2 is >= rho^2 f^2 + (1 - rho^2) p^2, with strict inequality wherever
   r~_f < r_f. So (*) is sufficient but in general far from necessary.
 * What the exact criterion forces (PROVED). For eta in X**, Goldstine gives a net x_i -> eta weak* with p(x_i) <= p**(eta); passing to the limit,
   f'(eta)^2 + rho^2 g(eta)^2 <= p**(eta)^2 for every g in C(f). At eta = xi' (normer of f') this gives g(xi') = 0 for all g in C(f), i.e.
   C(f) subset ker xi'. That is the only first-order consequence. It forces f' = f exactly when C(f)^perp = R xi in X** (then xi' = +-xi, and
   1.2 applies), e.g. when span C(f) is dense in ker xi. Nothing in Z1 shows this for general f.
 * The inference pattern "exposed faces are points => rho C(f) subset C(f') forces f' = f" is FALSE in general. In X = ell_4^3 (smooth,
   strictly convex, every exposed face of the dual ball a point), f = e_1* has C(f) = {0}: g in C(f) needs g(e_1) = 0 and
   g(s v)^2 <= ||e_1 + s v||_4^2 - 1 = O(s^4) for v in e_1-perp, so g = 0. Then rho C(f) = {0} is contained in every C(f').
 * A positive fact in the opposite direction (PROVED, new). Let C_base(a) := {b in l_1 : q*(a + s b) <= s(s) for all real s}. Then
   C_base(a) subset C(f') for EVERY f' in S_{p*} whose forced base part is a. Proof: f' + s b = (a + s b) + L*w', so by A Fact A
   p*(f' + s b) <= max(q*(a + s b), ||w'||_{V*}) = max(q*(a + s b), 1) <= s(s). So along approximants that keep a (far lowerings and the f^L of
   Z1 3.2 keep a; canonical truncations do not), the pure-base part of the fibre is never lost. This contradicts nothing in Z1 except the moral.
Impact: 1.3 is used only as motivation (0. Answer, 3.1(d) "moral"). No proof depends on it. Fix: replace "forces f' = f" by "the primal
sufficient condition (*) fails for f' != f; the exact condition only forces C(f) subset ker xi'".

## 1.4 Local reduction (Z1 1.4 = P2A Lemma 1.4 for non-NA f'). Verdict: CORRECT (PROVED).
Re-derived. For |tau| <= T_0: 1 + (tau^2/2)(1 - delta) <= s(tau) because s(tau) >= 1 + tau^2/2 - tau^4/8 and tau^2 <= T_0^2 <= 3 delta < 4 delta.
For |tau| >= T_0: p*(f' + tau g') <= s(rho tau) + eps + |tau| eta', and s(tau) - s(rho tau) = (1 - rho^2) tau^2/(s(tau) + s(rho tau)) is
>= (1 - rho^2) tau^2/(2 sqrt 2) for |tau| <= 1 and >= (1 - rho^2)|tau|/(2 sqrt 2) for |tau| >= 1, while eps + |tau| eta' <= (1 - rho^2)tau^2/3
resp. (1 - rho^2)|tau|/3, and 1/3 < 1/(2 sqrt 2). Norm attainment of f' is never used. Numerical check (scalar_checks.py): max violation 0.
The stated equivalence "Lemma Z <=> local mates" is also correct (for "=>" use rho' g'' with g'' in C(f'), rho' < 1, delta = 1 - rho'^2).

## 1.5 Theorem B* (window-pinned mates). Verdict: CORRECT (PROVED by inspection).
I traced every use of (SR) and of gamma in G3 parts 2-5 (with the G3_ref fix of 5.3):
 * gamma enters only in 2.3(b)'s consequence sum_{J_gamma} |B| <= t/(2 gamma q_0) and through it in 3.4 (K_1 = 1/(gamma q_0) + 14); (SR) enters
   only through delta'_l > 0 in 3.2-3.3. Both are consumed by 3.4, whose conclusion sum_l |Delta c_l| <= K t is all that 3.5, 4.1-4.2 and 5.3 use.
 * 3.5(a)-(c), 4.2(a)-(d): valid for any admissible T and any f with F finite, given that conclusion, K t <= 1, t <= t_*, t in W(l_*):
   the fine-carrier estimate in 4.2(c) uses only the box bound 3.1 and (P2), t >= T_lo(l_*); K_b uses 2.5 (F finite).
 * 5.1, 5.2 are for any f with F finite. 5.3 needs only: t^(j) = T_hi(l_j), n_j = n^w_{l_j}, K'_j = (1 + ||U||) K_2-type constant times K_j,
   n_j >= 24 rho^2 K'_j/(c_1(1 - rho^2)) (from n^w/K_j -> infinity), K'_j t^(j)/n_j -> 0 and K_4 K_j t <= kappa_0 (from K_j T_hi(l_j) -> 0).
Remarks. (i) The hypothesis is needed only on the n_j dyadic scales T_hi(l_j) 2^{1-i}, not on all of W(l_j), and only for coarse l <= l_j (the
fine part is <= 6 t^2 at every f, by 3.1 and (P2)). (ii) Remark (ii) of Z1 1.5 ("persistent switching through unpinned carriers") is a
paraphrase of the negation of window-pinning; correct as a description, HEURISTIC as to its consequences. (iii) Bounded free switching (Z1 4.3)
is far from window-pinning: pinning needs switching <= K_j T_lo(l_j) at the bottom of the window, i.e. super-exponentially small.
# Z1 referee, part 2: Z1 part 2 (defect terms, budget form, ray lemma, consequences)

## 2.1 Homogeneity/convexity (Z1 2.1). Verdict: CORRECT (PROVED).
Kink is positively homogeneous. Each flip term tau -> 2(-sign(a_j) tau B_j - |a_j|)_+ is convex and vanishes at 0. For k in P_m,
tau -> ||w + tau Omega||_inf - sigma_k (w + tau Omega)(k) is convex (sup of affine maps minus an affine map) and vanishes at tau = 0 because
|w(k)| = M. A convex phi with phi(0) = 0 satisfies phi(tau) <= (tau/t) phi(t) on [0, t]. Random check (scalar_checks.py): max violation 0.

## 2.2 Budget form (Z1 2.2). Verdict: CORRECT (PROVED).
Re-derived A Lemma 7.1: q_0 q*(A) + sum_m sigma_m N_m(W_m) = q_0 E_q(A) + sum_m sigma_m e_m(W_m) + (A + L*W)(xi), with (A + L*W)(xi) =
f(xi) + t g(xi) = 1 and the left side <= s(t). A Lemma 7.2 (re-derived): E_q(a + tB) = Fl_B(t) + t Kink(B) + nu Psi(t U*B/nu)
(for j in F: |a_j + tB_j| - sign(a_j)(a_j + tB_j) = 2(-|a_j| - sign(a_j) t B_j)_+), and
e_m(W) = sum_P |alpha_k| (||W||_inf - sigma_k W(k)) + ||P-perp D(W - w)||^2/(||DW|| + <DW, Dw>/C), using ||alpha||_1 = 1 (from <w, alpha> = 1 - C = M).
Lower bounds of the two quadratic terms as in G3 2.3(d). Dividing by t gives Delta1(t) + (t/2) Gamma_w/(1 + eta_Gamma) <= t/2.

## 2.3 Ray lemma (Z1 2.3). Verdict: CORRECT (PROVED).
Checked line by line:
 (i) q_0 beta_0 + sum sigma_m beta_m = g(xi) + Delta1 - Delta1 (q_0 + sum sigma_m) = 0, hence g_t(xi) = 0 (a(xi) = q_0, <w_m, zeta_m> = sigma_m).
     |beta_0| <= t/(2 q_0) + t/(2 q_0) + t/2 <= 3t/(2 q_0) and |beta_m| <= 3t/(2 sigma_m) (2.3(a) of G3 and 2.2); p*(a), p*(R_m* w_m) <= 1.
 (ii) f + tau g_t = [(1 - tau beta_0) a + tau B] + sum_m R_m*[(1 - tau beta_m) w_m + tau Omega_m] (exact), and p*(A + L*W) <= max(q*(A), max_m N_m(W_m)).
 (iii) With X := B(zhat) + Kink(B) + Fl_B(t)/t: (1 - tau beta_0)(1 + tau_0 X) = 1 + tau (X - beta_0) = 1 + tau Delta1, tau_0 = tau/(1 - tau beta_0)
     (identity checked numerically to 2e-16). The quadratic bound uses Psi(h) <= ||h-perp||^2/(2(1 - ||h||)) (from
     ||e + h|| - 1 - <e,h> = ||h-perp||^2/(||e+h|| + 1 + <e,h>)) and ||s U*B/nu|| <= ||U|| eta/nu, s <= t. Fl_B(tau_0) <= (tau_0/t) Fl_B(t) needs
     tau_0 <= t, true for tau <= t/2 and t small.
 (iv) Block: N(w + s Omega) = 1 + s<Omega, zeta>/sigma + peak(s) + s^2 ||P-perp D Omega||^2/(||DW_s|| + <DW_s, Dw>/C); the denominator is >= 2(C - eta)
     since ||s D Omega|| <= ||t D Omega|| <= eta. Same algebra with beta_m.
 Two bookkeeping remarks (no effect): the factor (1 + c t) is absorbed into (1 + c_f eta) only if t_eta <= eta, which may be assumed WLOG;
 and the conclusion holds with Gamma_max = max(h(B), max_m H_m(Omega_m)), which can exceed 1 even though Gamma_w <= 1 + o(1).

## 2.4 Consequences (Z1 2.4). Verdict: (a) CORRECT; (b) CORRECT as an upper bound, the clause "and in general NOT below" is unproved;
## (c) a correct explanation of why the averaging upper bound fails, labelled PROVED but it proves no necessity.
(a) Immediate from 2.3 with Delta1 = 0.
(b) Re-derived: for tau in [c_rho Delta1, t/2], rho tau Delta1 <= tau^2 (1 - rho^2 Gamma')/4 and tau^4/8 <= tau^2 (1 - rho^2 Gamma')/4 for tau^2 <=
    2(1 - rho^2 Gamma'), so 1 + rho tau Delta1 + rho^2 tau^2 Gamma'/2 <= s(tau) (Gamma' := Gamma_max(1 + c_f eta) < 1/rho^2). Random check: max
    violation 0. "In general NOT below" would need a LOWER bound p*(f + tau rho g_t) >= 1 + c tau Delta1, which is not shown (the decomposition
    need not be optimal). It should be labelled HEURISTIC.
(c) The computation shows that the specific bound "average of the scale-t_i ray bounds" has an uncompensated first-order term. It does not show
    that no other decomposition of the averaged functional works. Label: HEURISTIC (method-level), not PROVED.
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
# Z1 referee, part 5: Z1 part 5 (the "common-functional obstruction") -- it is an artefact; Hoffman matching

Setting of Z1 part 5: SLD T, p = p_N, f with F finite, a finite slaving-closed set U* of free carriers, (SR) for every l notin U*, and
(E1) every l in U* is a strict non-peak; (E2) supp u_l \ F subset K (contacts) for l in U*. K_* := union_{U*} supp u_l \ F. Window scale t in W(l_*),
K := K_1 Lambda*_f(l_*) (pinning constant of the carriers outside U*). Two-sided decomposition (B_+-, Omega_+-) of g at scale t, u-coefficients
c^+-_l (L*Omega = sum_l c_l u_l), Delta c := c^+ - c^-, Delta B = B_+ - B_- = -sum_l Delta c_l u_l.

## 5.1 Z1 5.1 (window split). Verdict: SKETCH, as labelled; two omissions.
(a) The O(t) WRONG-SIGNED contact mass of B_+- on K_* (allowed by the budget, G3 2.3(b): sum_{j notin F} [(z_j B_+(j))_- + (z_j B_-(j))_+] <= t/(2 q_0))
    is not mentioned. It is unstructured junk of size O(t) on K_*, in addition to Z1's J_t.
(b) The d-coefficients. At a finitely swallowed point G3 3.5(c) has an extra term (Phi_k/(m C)) sum_{U*} |Delta c_l| = O(1), so |Delta d_m| = O(K t) is
    NOT automatic. It does hold, by the first-order identity in 5.3(2)(ii) below. Z1 hides this in "normalisation terms".

## 5.2 Z1 5.2. Verdict: the algebra is right inside Z1's model, but the conclusion is WRONG. Z1 FIXES the + component's functional as
## Phi_t = g - Rem_+(t). The averaging (G3 5.2) only needs some functional Psi_t with ||g - Psi_t|| = O(K t) and two exact one-sided decompositions.
Z1's criterion is "J_t can be cancelled exactly iff -J_t (mod span{u_l 1_{K_*}}) lies in the z-cone". It allows only z-signed ADDITIONS to the + side.
It misses the possibility of REDUCING the + side's contact base. The base V stays z-signed as long as z_j V(j) is in [0, z_j B_+(j)], and the change
can be put into the O(K t) remainder exactly like Rem_+. Example (one coordinate, z = 1). Take B_+ = 1 + eps - beta, B_- = -beta (0 <= beta < eps),
sigma := -Delta c u = 1, J = eps. Z1's test fails: B_- + J = eps - beta > 0. Matching still works with V = 1 and W = 0: trim P = eps - beta.

## 5.3 Proposition (Hoffman matching; referee). Steps (1)-(4) PROVED, (5)-(6) SKETCH.
In the setting above, for all late window scales t there is ONE functional Psi_t with ||g - Psi_t||_{p*} <= C_f K t. It carries exact, balanced,
d-NEUTRAL two-piece data in the sense of P2A 1.6: (b^+, omega^+), (b^-, omega^-), supp b^+- subset F cup K_*, z_j b^+(j) >= 0 >= z_j b^-(j) on K_*, and
omega^+- finitely supported off the peaks. Each side is an O(K t)-perturbation of the actual decomposition on that side.
(1) The cone. For xi in R^{U*} put v_xi := sum_{U*} xi_l u_l 1_{K_*} and
      R_0 := {xi : z_j v_xi(j) >= 0 for all j in K_*, and sum_{l in U*, m(l) = m} xi_l u_l(xi) = 0 for all m}.
    R_0 is a POLYHEDRAL cone. Put G_0 := union_{U*} supp y_l (finite). At j in S_l \ G_0 (l in U*), the only free vector that is nonzero is u_l's signature
    delta_l 2^{-j}/n_l > 0, because the S_l are disjoint and targets are finitely supported. So the constraint there is z_j xi_l >= 0. This gives one
    constraint eps_l xi_l >= 0 if z = eps_l is constant on S_l \ G_0, or xi_l = 0 if z takes both signs there. Add finitely many constraints at
    G_0 cap K_* and N equations.
(2) The actual switching xi° := -Delta c|_{U*} violates every constraint by O(K t + t).
    (i) Slaving-closedness gives that pinned signatures never meet K_*. So Delta B 1_{K_*} = v_{xi°} + J_t with
        J_t := -sum_{l notin U*} Delta c_l u_l 1_{K_*}, and ||J_t||_1 <= (4/3) sum_{l notin U*} |Delta c_l| <= (4/3) K t.
        Also z_j Delta B(j) >= -[(z_j B_+(j))_- + (z_j B_-(j))_+].
        Summing over S_l \ G_0: (eps_l Delta c_l)_+ delta_l ||h_l 1_{S_l \ G_0}||/n_l <= (4/3) K t + t/(2 q_0). The mixed-sign case and the
        constraints at G_0 are handled the same way.
    (ii) d-neutrality. sum_k Delta c_k u_k(xi) = <Delta Omega_m, zeta_m>, since zeta_m(k) = lambda_k u_k(xi). This lies in [-t, t] by G3 2.3(a).
        The pinned part is <= q_0 sum_{l notin U*} |Delta c_l|. Hence |sum_{U*, m(l)=m} Delta c_l u_l(xi)| <= t + q_0 K t.
        (For a strict non-peak, u_k(xi) = sigma_m Phi_k w(k)/(C m) and d(e_k) = Phi_k^2 w(k)/C. So this is exactly Delta d of the free part, and the
        same bound gives |Delta d_m| = O(K t) in G3 3.5(c) at finitely swallowed points.)
(3) Hoffman's lemma for the polyhedral cone R_0 (finitely many constraint normals fixed by f and U*) gives xi_t in R_0 with |xi_t - xi°| <= H (K t + t).
(4) Trimming. Let B^cl_+ be the z-signed part of B_+ on K_*. Put z_j P(j) := (z_j (B^cl_+(j) - v_{xi_t}(j)))_+, V := B^cl_+ - P and W := V - v_{xi_t}.
    Then V is z-signed, and W is (-z)-signed because z_j v_{xi_t}(j) >= 0.
    ||P||_1 <= sum_j (z_j B_-(j))_+ + ||B_+ 1_{K_*} - B^cl_+||_1 + ||J_t||_1 + ||v_{xi_t} - v_{xi°}||_1 = O(K t),
    using v_{xi°} = Delta B 1_{K_*} - J_t = (B_+ - B_-) 1_{K_*} - J_t.
(5) The two sides (SKETCH).
    + side: omega^+ := the G3 block data built from omega_+, clamped at 2 gap/t on pinned coarse non-peaks, 0 on peaks and fine coordinates,
        UNCLAMPED on the free carriers (one-sided use needs no clamp).
        b^+ := B_+ 1_F + V - kappa a, with kappa := (B_+ 1_F + V)(zhat) = B_+(zhat) - (B_+ 1_{F^c \ K_*})(zhat) + (V - B_+ 1_{K_*})(zhat) = O(K t).
        Psi_t := b^+ + sum_m R_m*(omega^+_m - d(omega^+_m) w_m).
    - side: omega^- := omega^+ + sum_{U*} (xi_{t,l}/lambda_l) e_{k(l)} and b^- := b^+ - sum_{U*} xi_{t,l} u_l, so that b^- 1_{K_*} = W.
        Since Delta d(xi_t) = 0, b^- + sum R*(omega^- - d(omega^-) w) = Psi_t exactly. By (E2), supp b^+- subset F cup K_*.
    ||g - Psi_t|| = O(K t). This uses G3 4.2(c) for the pinned part (it needs |Delta d| = O(K t), see (2)(ii)), base mass off F cup K_* being
    O(K t + t), and ||B_+ 1_{K_*} - V|| = O(K t).
(6) Validity (SKETCH). Each side differs from the actual decomposition on that side by O(K t): in l_1 for the base, and in sum lambda_k |.| for the
    blocks. On the free carriers, omega^-(k_l) - omega_-(k_l) = (xi_{t,l} + Delta c_l)/lambda_l + Delta d w(k_l) = O(K t). So Gamma_w <= 1 + eta_0/2 on late
    windows, by the seminorm argument of G3 4.2(d). The one-sided version of 5.1 holds:
     * no kinks on K_* (signs);
     * no flips on F (F finite, bases bounded);
     * pinned data in (C-b);
     * free carriers inside the box at every s <= t, because the box condition is convex in s and holds at s = t. Step 3(iv) of 5.1 needs a
       one-line change for coordinates moved AWAY from the peak level by up to (2M - gap)/t: |s omega| <= c_1(2M - gap) <= M/2 for c_1 <= 1/4.

## 5.4 Theorem M (referee; SKETCH). Finitely swallowed points with exact free resources are recoverable.
For the SLD T and every N, let f in S_{p_N*} have F finite, and let U* be a finite slaving-closed set such that (SR) holds for all l notin U* and
(E1), (E2) hold for l in U*. Then f is in R.
Proof (sketch).
(1) 5.3 on every late window gives Psi_{t_i} for the n dyadic window scales.
(2) G3 5.2 (use the + side for s > 0 and the - side for s < 0; conditions (i)-(iii) hold) gives rho Psi in C(f) with Psi := avg_i Psi_{t_i}.
(3) Psi carries exact d-neutral two-piece data: the averages of the sides. This works because the sign cones are convex, d is linear and Gamma_w is
    convex, so kappa_w(Psi) <= 1 + eta_0.
(4) S3 Cor D1 (F finite, Delta d = 0 >= 0, kappa_w(rho Psi) <= rho^2(1 + eta_0) <= 1; refereed) gives rho Psi in Ls(f).
(5) ||Psi - g|| <= 2 K t_1/n -> 0 along the windows, and Ls(f) is closed under norm limits in this sense. So g is in Ls(f).
Toy check of steps (1)-(4) of 5.3 (Z1ref_work/hm2.py; 3 free carriers, an O(1) exact resonance, junk and wrong-signed mass of size eps):
|xi_t - xi°|/eps <= 5.1, ||P||/eps <= 4.3, all signs exact, for eps = 1e-2 ... 1e-5.
Consequences for Z1:
 * The "common-functional obstruction" (Z1 5.2, table #15) and the remaining step (RS1) are resolved in the exact-resource case (SKETCH).
 * What remains of (RS1) is Z1's (O-a): near-resources on swallowed sets. These are near-contacts (E2 fails), free carriers that are peaks, weak
   or near-threshold (E1 fails), and inexact contacts with |z_j| < 1 inside swallowed signature sets. That is the genuinely scale-dependent part (O3).
 * (A) "R_fin subset R" is reduced to the near-resource case. (B) (lower semicontinuity along f^L) is untouched.

## 5.5 Remarks on the scope of Theorem M.
 (a) Extension (SKETCH, same proof). (E2) may be weakened to (E2'): for l in U*, the set supp u_l \ (F cup K) is FINITE. Examples are finitely many
     coordinates j notin F with |z_j| < 1. At such j the budget (G3 2.3(b)) bounds the base mass of each side by t/(2 q_0 (1 - |z_j|)), so the
     switching vanishes there up to O(t) (constant depending on the finitely many j). Add the
     finitely many equations sum_{U*} xi_l u_l(j) = 0 (no sign condition at these j); R_0 stays polyhedral, and the components put no base
     there (trim B_+(j) = O(t)).
     Slaving can then use kappa^room_{l',l} := ||y_{l'} 1_{S_l cap J_gamma}||_1/n_{l'}. If S_l cap J_gamma is infinite, a free target touching it pins
     the free carrier: |Delta c_l| = O(t) from the roomy tail, and then Delta c_{l'} = O(t) at the touched roomy coordinate.
 (b) What is NOT covered is infinitely many INEXACT one-sided coordinates in the free supports, e.g. near-contacts with |z_j| -> 1 along a
     swallowed S_l. The obstruction there is not the cone geometry: on S_l all constraints still read z_j xi_l >= 0. The obstruction is
     inexactness. Base mass at a near-contact costs (1 - |z_j|)|s| at first order, so a component that uses it has Delta1 > 0 (ray lemma 2.4(b)).
     It is not in P2A 1.6's format (exact signs on K), and trimming all such mass forces xi_l = 0. Yet the actual switching may use O(1) mass
     there at each scale, because the cost is only (1 - |z_j|) t per unit. This is the genuine scale-dependent switching (O3), now localised to
     the near-contact tails of finitely many signature sets (Z1's (O-a)).
     A possible route, not attempted here: approximants f' that RAISE the near-contacts of the swallowed sets to exact contacts
     (z'_j := sign z_j where 1 - |z_j| < eps). Then z' -> z uniformly on those sets, so f' -> f, and f' satisfies (E2). This leaves the usual
     transfer band problem.
