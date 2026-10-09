# S3 part 4: generic supports (O1) — what is proved, the exact residual property, and whether it can fail

Setting of parts 1-3. "Generic support": some block has infinitely many strict non-peaks (Q_m infinite), possibly with non-peaks at a positive
proportion of fine scales; near-threshold coordinates and degenerate peaks allowed unless stated.

## 4.1 What Theorem D already gives at generic supports. PROVED.
Corollary D1 (part 3) has NO hypothesis on Q_m: if F is finite and g in C(f) carries two-piece data (finitely supported omega^+-) with Delta d_m >= 0
in all blocks and kappa_w <= 1, then g is in Ls(f) — whatever the non-peak structure of f (infinitely many strict non-peaks at all scales, near-threshold
non-peaks, degenerate peaks). The only place where the fine structure of f enters Theorem D is (SC_m) in blocks with Delta d_m < 0.
Reason: the deep coordinates scrambled by the window perturbation (size s_1) enter the proof only through
 (i) ||D_m(w'_m - w_m)||^2 = O(s_1^2 log(1/s_1)) (always; proof of D2(i), which uses only the clamp formula and Phi_m(k) <= 2^{-m-k});
 (ii) the Bregman terms Bx_m = o(s_1) (always; (E5));
 (iii) the anchor remainder sum_{A_m} lambda_k |w'_m(k) - w_m(k)| — needed only on the "wrong" side, i.e. when Delta d_m < 0.

## 4.2 The exact residual quantity and a sufficient structural condition. PROVED.
For a block m and s > 0 let
   Scr_m(s) := sum{ min(Phi_m(k), s) : k in P_m, mu_{k,m} <= s }  +  sum{ min(Phi_m(k), s) : k in Q_m, Phi_m(k) gap_m(k) <= s  or  gap_m(k) <= s }
(lambda-weighted mass, truncated at s, of near-threshold peaks and of non-peaks that a perturbation of relative size s can scramble), and say that
block m satisfies
   (MS-Q*)  liminf_{s -> 0} Scr_m(K s)/s = 0 for every K < infinity  [equivalently along one sequence s_i -> 0 for each K; it suffices: Scr_m(s) = o(s)],
and has no degenerate peaks and no non-peak with gap 0 (i.e. every k off P_m has |w_m(k)| < M_m: automatic for strict non-peaks).
Proposition 4.2. If block m has no degenerate peaks and Scr_m(K s) = o(s) along a sequence s -> 0 for every K, then (SC_m) holds along the approximants
of part 3, 3.3 (with s_1 running through that sequence). Consequently (Theorem D): if F is finite and every block with Delta d_m < 0 satisfies these
conditions, every two-piece mate with kappa_w <= 1 is in Ls(f).
*Proof.* (a) As in D2(i): Phi_k |w'(k) - w(k)| <= K_0(s_1 + t_k) (clamp formula, uniform Lipschitz bound; t_k := ||u_{k,m} 1_{(N'',inf)}||_1) and <= 2 Phi_k,
so ||D(w'-w)||^2 = O(s_1^2 log(1/s_1)) + (tail).
(b) |C' - C| <= K_g s_1 (no hypothesis): with Delta := D(w' - w), |<Dw, Delta>| <= sum_k Phi_k |w(k)| Phi_k |w'(k) - w(k)| <= sum_k Phi_k K_0 (s_1 + t_k) = O(s_1),
and | ||Dw'|| - ||Dw|| - <Dw,Delta>/C | <= ||Delta||^2/C (expand ||Dw + Delta||; C' -> C > 0), so |C' - C| = O(s_1) + O(||Delta||^2) = O(s_1); |M' - M| = |C' - C|.
(c) A peak with mu_k > K_1(s_1 + t_k) stays a same-sign peak of w' (threshold perturbation O(s_1 + t_k)). A strict non-peak with Phi_k gap_k > K_1(s_1 + t_k) and
gap_k > K_1 s_1 satisfies |w'(k) - w(k)| <= K_0(s_1 + t_k)/Phi_k <= gap_k/4 (K_1 >= 4K_0) and |gamma| + |M' - M| <= 2K_g s_1 <= gap_k/4 (K_1 >= 8K_g), so it remains a
non-peak and |2w'(k) - w(k)| <= |w(k)| + 2|w'(k) - w(k)| <= M - gap_k/2 <= M' - |gamma|. Hence A_m is contained in {k in P: mu_k <= K_1(s_1 + t_k)} union
{k in Q: Phi_k gap_k <= K_1(s_1 + t_k) or gap_k <= K_1 s_1}.
(d) On A_m: Phi_k^2 + lambda_k(|w'(k) - w(k)| + gamma_+) <= m(3 min(Phi_k, K_0(s_1 + t_k)) + 2 Phi_k K_g s_1) (Phi_k <= 1). Summing over A_m: the part with t_k <= s_1 is
<= 3mK' Scr_m(2K_1 s_1) + 2 m K_g s_1 sum_{A_m} Phi_k, and sum_{A_m} Phi_k -> 0 (A_m shrinks to the empty set coordinatewise; dominated convergence), so this is o(s_1)
under the hypothesis; the part with t_k > s_1 tends to 0 as N'' -> infinity for fixed s_1 (dominated convergence: every peak has mu_k > 0, every non-peak gap_k > 0, and
t_k -> 0 for each k) and is made <= s_1^2 by choosing N'' after s_1. With (a), (SC_m) holds. QED.

## 4.3 Quantitative recovery without (SC). PROVED.
Without any condition on the Delta d < 0 blocks, the proof of Theorem D gives: (f, rho g) is in cl NA whenever
   rho^2 kappa_w + 8 rho sum_{m : Delta d_m < 0} |Delta d_m| K_m^scr < 1,    K_m^scr := limsup along the construction of (anchor and remainder costs)/s_1,
since the genuine first-order cost on the wrong side is <= |tau| rho |Delta d_m| (E_y + 2||R*Z_A||_1) <= |tau| rho |Delta d_m| K_m^scr s_1 (1 + o(1)) <= rho |Delta d_m| K_m^scr tau^2 (|tau| >= s_1).
K_m^scr <= C_abs m (limsup Scr_m(K s_1)/s_1) is finite when non-peak gaps are bounded below off a finite set (Scr_m(s) <= sum_{Phi <= s/g_0} Phi + ... = O(s)).
So the non-recovered part of a Delta d < 0 two-piece mate is confined to rho close to 1: "ρ-defect" only, never a first-order obstruction.

## 4.4 Can (MS-Q*) / (SC) fail for an admissible T? SKETCH (yes for (MS-Q*); whether recovery fails is OPEN).
Construction (adaptation of P1 2.1, which allows any finite or "density-zero" set of prescribed vectors; and of N2 3.8 for Delta d < 0): fix the first row's
contact vector zhat as in P1 2.2, and in block 1 prescribe u_{2k,1} in zhat-perp cap S_{q*} for all k >= k_0 (a sequence dense in zhat-perp cap S_{q*}), with the odd
indices (and all other blocks) carrying the dense targets of P1 2.1 (so the tail of every block is still dense in S_{q*}, (T-d)); injectivity and Ran T cap c_00 = {0}
via signature tails h_l as in P1 2.1. Then every (2k,1), k >= k_0, is a strict non-peak of f with w_1(2k) = 0 and gap M_1, and
   Scr_1(s) >= sum{Phi_1(2k) : Phi_1(2k) <= s} ~ s/3:   (MS-Q*) FAILS at every scale.
Along the approximants of 3.3, u_{2k,1}(xhat') = s_1 <U*u_{2k,1}, h_N> + o(s_1) with h_N := (e' - e)/s_1 + o(1) fixed by the window masses; since the u_{2k,1}
are dense in zhat-perp cap S, a positive proportion of the deep (2k,1) with Phi_1(2k) << s_1 become peaks of w'_1 (new peaks, |w' - w| = M'), so the anchor remainder
is >= c s_1: (SC_1) FAILS for these approximants. Combined with a Delta d < 0 exact resonance in block 1 (N2 3.8 design; compatible, since the resonance vector is a
single prescribed u_{2,1}), Theorem D does not apply for rho close to 1.
OPEN: whether other approximants pin the deep non-peaks. A sufficient "compensation property" (HEURISTIC): masses at far free coordinates (z'_j := sign of the
mass, j -> infinity; no cost for the two-piece pieces since beta^sigma vanishes on J) that cancel P_perp U*(window masses) up to relative error eta, with total l_1 mass -> 0,
would reduce the scrambling to eta s_1 and give (SC) with an eta-dependent constant, hence recovery (by 4.3 with eta -> 0). This is a property of U and of the
far free coordinates, NOT of T; it needs, roughly, that the tail spans of {P_perp U*e_j* : j in J, j > N_1} approximate the (N-dependent) perturbation direction with
coefficients o(1/s_1) — not proved.

## 4.5 Deep coefficients c_k ~ sqrt(Phi_k) (C_notes 9.2 borderline). PROVED (max-form) / SKETCH (weighted form).
C_notes 9.2 states that sum c_k^2/Phi_k = infinity with |c_k| ~ sqrt(Phi_k) is "not covered by any known recovery technique". This is superseded by A Cor 6.10(a)
(Theorem W with O(sigma) box tails, via the Averaging Theorem 6.8; refereed): for g = b + sum_m R_m*(omega_m - d_m w_m) with b supported in F and
omega_m(k) = c_k/(m Phi_m(k)), gaps bounded below on supp omega_m, the box tail is T_m(sigma) = sum{|c_k| : |c_k| > gap_k Phi_k/(2 sigma)} <= sum{|c_k| : Phi_k <~ sigma^2/g_0^2} = O(sigma)
when |c_k| <= K sqrt(Phi_k) (geometric Phi), so g is in cl Cert(f) provided g is in C(f) and max(h(b), H_m(omega_m)) <= 1 (note ||D omega||^2 = sum c_k^2/m^2 < infinity).
Upgrade to Gamma_w <= 1 (SKETCH): run the averaging with rebalanced certificates; Lemma 1.1 of part 1 applies at f uniformly in the truncation level provided the
cut-off gamma of the transfer vectors is chosen with |tau omega(k)| <= gap_k/2 on L cap supp omega (then lowering coordinates of supp omega in L does not change signs),
which holds for the truncated certificates c_t of A Cor 6.10(a) (box condition). Not written in full.
Mixed case (deep weighted part + switching part, i.e. two-piece data whose COMMON part omega^0 is infinitely supported with O(sigma) tails and whose switching
part omega_Delta is finite): Theorem D at f' plus averaging over scales at f' (P2A Lemma 1.5) is the natural route; the obstruction is that the window
perturbation scrambles the deep part of omega^0 below scale s_1 at f', so the target must drop it (cost sum_{Phi_k <~ s_1}|c_k| ~ sqrt(s_1)) and this must be
paid by the slack at the scale where the truncated certificate's radius ends (~ sqrt(Phi_cut)) — the same borderline as in C 9.2, now at f'. OPEN (SKETCH of the
difficulty only).

## 4.6 Answer to O1 (summary).
 * Generic supports are NOT an obstruction for two-piece mates with Delta d_m >= 0 (PROVED, D1), nor for Delta d_m < 0 when the carrier blocks satisfy
   (MS-Q*) along some sequence of scales (PROVED, 4.2), nor for rho below an explicit threshold in general (PROVED, 4.3).
 * The precise quantitative property needed for Delta d < 0: o(s)-smallness of the lambda-mass (truncated at s) of coordinates scrambled by a perturbation of
   relative size s — (MS) for peaks and (MS-Q*) for non-peaks — along SOME sequence of scales. It is a property of f and T; it CAN fail for admissible T (4.4, SKETCH),
   and then the simplified approximants do not recover Delta d < 0 two-piece mates for rho near 1. Whether some engineering always works is OPEN; a sufficient
   T-independent route is the compensation property of 4.4 (HEURISTIC).
 * The deep-coefficient borderline of C 9.2 is covered by A Cor 6.10(a) for certificate-type mates (PROVED); for mixed switching + deep mates it is OPEN.
 * Beyond two-piece data: at generic supports (Q infinite) Theorem B's lower bound is not available (the block expansion is multiscale: coordinates with
   Phi_k <~ |t| contribute linearly, total O(t^2) "persistent curvature"); whether every mate at such f is a limit of two-piece data is OPEN (this is O3).
