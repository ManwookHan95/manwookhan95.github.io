# Y3 notes (Round 6): the infinite-support part (O4) of the open core

References: paper/martin_density_note.tex ("the note"); r5/Z5_notes.md ("Z5"; T8 = its Theorem 4.3, Lemma 1.1 = cushion lemma);
r5/Z5_ref_notes.md ("R1" = its Theorem R1, Lemma R2 = one-sided expansion with sparse flips); r5/Z3_notes.md (Theorem E, Lemma 3.1);
r5/Z4_notes.md (Theorem A = 3.1); r5/Z6_ref_notes.md ("Z6-L2.1" = one-sided expansion with inward-only coordinates).
Part files: r6/Y3_part1.md, Y3_part2.md, Y3_part3.md (first versions; THIS file supersedes them where they differ).
Scripts: r6/Y3_work/check_testpoint.py, check_Dsharp.py. Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Setting: I finite (p = p_N; Lemma lem:martintail transfers to Martin's p for one N-independent T); f in S_{p*} with forced data
(xi, q_0, a, w, F, z, zhat, e, nu); F = supp a possibly infinite; s_j := sgn a_j on F. For a two-sided decomposition (B_+-, Theta_+-)
of g in C(f) at scale t: f^+_j := (-s_jB_+(j) - |a_j|/t)_+, f^-_j := (s_jB_-(j) - |a_j|/t)_+, sum_F(f^+_j + f^-_j) <= t/(2q_0)
(lem:flip); cushion lemma (s_jB_+(j))_- <= |a_j|/t + f^+_j, (s_jB_-(j))_+ <= |a_j|/t + f^-_j. d_+-, omega_+- as in lem:suplevel
(Theta_+ = omega_+ - d_+w, Theta_- = omega_- - d_-w). Bx(j) := sum_{m in I}sum_k lambda_{k,m}|u_{k,m}(j)| (box profile).

## 0. Summary

| # | Result | Scope | Status |
|---|---|---|---|
| 1 | Flip profiles: Exc_beta(r) = 2 int_0^r m_beta; classification sparse / critical / super-critical; geometric signatures make critical profiles oscillate (factor >= 2) | any T | PROVED (1.1, 1.2) |
| 2 | Raised engineered approximants: T8 needs cushion sparsity only for the side parts (s b^+)_-, (s b^-)_+, not for b^theta; flip-extended version | any T | PROVED (2.1, 2.2) |
| 3 | Un-switching pair (exact rewriting of a d-neutral switching into one side, Gamma cost linear) | any T | PROVED (3.1) |
| 4 | Constrained-switching bound for monochromatic support swallowing (design D_sigma: new allowedness (c)); quasi-monotone dichotomy | D_sigma | PROVED (3.2-3.4) |
| 5 | Theorem SC: non-sparse SUPER-CRITICAL support swallowing (model |a_j| ~ v_l(j)^{1+b}, b > 1) is harmless (with R1: model settled for b != 1) | D_sigma | PROVED (3.5) |
| 6 | Exact one-sided coefficient at ARBITRARY F (new test points k_2 = -kappa e; no Gram system); liminf >= gamma^+-, attainment, upper bound with flips | any T | PROVED (4.1) |
| 7 | Block-tame points with infinite F: mates that are cushion-sparse are recovered | any T | PROVED (4.2) |
| 8 | Theorem N: box-dominated support (forces F = N, a > 0): EVERY mate recovered under (SC) for all blocks and a margin rate; no pinning, no design needed | any T | PROVED (5.1) |
| 9 | Theorem A at infinite F (contact-swallowed bad carriers, box domination on F) | SLD_G | SKETCH (5.2) |
| 10 | Master theorem at infinite F; (LSC-trunc) holds wherever exact data exist; truncation itself is free | any T | PROVED (6.1, 6.2) |
| 11 | Remaining (O4): CRITICAL support swallowing (m_l(y) asymp y), non-d-neutral/non-resonant non-sparse carriers, box-size switching on thin support, F = N without (SC); plus the finite-F core | — | OPEN (7) |

Bottom line: the infinite-support part of the open core shrinks to a single quantitative phenomenon — critical support swallowing,
an "exactness versus scale" rate problem of the same type as (O1)(i) — plus d-neutrality/resonance side conditions and the block-side
conditions shared with finite F. F = N with a box-dominating base (the explicit example of the task) is recovered for every admissible T
under block conditions alone. No counterexample mechanism was found; leaning positive.

## 1. Flip profiles. PROVED.

For beta in l_1, beta >= 0: m_beta(x) := sum{beta_j : j in F, |a_j| < x beta_j}, Exc_beta(r) := sum_{j in F} 2(r beta_j - |a_j|)_+.
Lemma 1.1. (a) Exc_beta(r) = 2 int_0^r m_beta(s) ds; it is convex and nondecreasing in r, Exc_beta(0) = 0.
(b) beta -> Exc_beta(r) is convex and coordinatewise nondecreasing; beta <= beta' implies m_beta <= m_beta'; m_{c beta}(x) = c m_beta(cx);
m_{beta_1 + beta_2}(x) <= 2m_{beta_1}(2x) + 2m_{beta_2}(2x).
(c) For b in l_1, r > 0: sum_{j in F}(|a_j + rb_j| - |a_j| - s_j r b_j) = Exc_{(sb)_-}(r); for r < 0 the same with (sb)_+ and |r|.
(d) m_beta(x) <= kappa x on (0, x_0] implies Exc_beta(r) <= kappa r^2 on (0, x_0]; >= likewise.
Proof. (a) d/dr 2(r beta_j - |a_j|)_+ = 2 beta_j 1[r beta_j > |a_j|] a.e.; monotone convergence. (b) Each summand is convex and
nondecreasing in beta_j. Scaling: substitute. Sum: split {|a| < x(beta_1 + beta_2)} according to which of beta_1, beta_2 is larger; on
the first part beta_1 + beta_2 <= 2beta_1 and |a| < 2x beta_1. (c) |x + y| - |x| - sgn(x)y = 2(-sgn(x)y - |x|)_+ for x != 0. (d) (a). QED
Classification, with kappa_beta(x) := m_beta(x)/x: SPARSE (kappa -> 0; Z5's (CS), Exc = o(r^2)), SUPER-CRITICAL (kappa -> infinity),
CRITICAL (0 < liminf <= limsup < infinity), mixed otherwise.
Lemma 1.2 (critical profiles oscillate for geometric signatures). Let beta := v 1_S with S = {s_1 < s_2 < ...} subset F, v(s) = c 2^{-s},
and rho(s) := |a_s|/v(s) nonincreasing along S with rho(s_i) -> 0. Then at every jump point y = rho(s_i) (with rho(s_{i+1}) < rho(s_i))
kappa_beta(y+)/kappa_beta(y) >= 2; hence limsup_{x->0} kappa_beta(x) >= 2 liminf_{x->0} kappa_beta(x) whenever the latter is positive.
Proof. Put R_i := sum_{i' >= i} v(s_{i'}). As s_{i+1} >= s_i + 1, R_{i+1} <= 2v(s_{i+1}) <= v(s_i), so R_i = v(s_i) + R_{i+1} >= 2R_{i+1}.
For y = rho(s_i): m(y) = R_{i+1} (only s_{i'} with rho < y count) and m(y+) = R_i. QED
Model (Z5 7.1): v_l(s) = c_0 2^{-s} on S_l, |a_s| = 2^{-(1+b)s}: kappa(x) ~ x^{1/b - 1}: sparse iff b < 1, super-critical iff b > 1, critical
(and, by Lemma 1.2, oscillating by a factor >= 2) iff b = 1. Numerics (check_Dsharp.py) confirm the exponents of Lemma 3.2 below.

## 2. Raised engineered approximants. PROVED.

Two-piece data at arbitrary F: side-+ pair (b^+, omega^+) and side-- pair (b^-, omega^-) representing the same g (Definition
def:twopiece with no condition on F); b^theta := (b^+ + b^-)/2, v := b^+ - b^-.
Theorem 2.1 (T8 with raised support). Let T be admissible, I finite, F arbitrary, g in C(f) with two-piece data, rho^2 kappa_w < 1,
I_- := {m : Delta d_m < 0} satisfying (SC), and
  (CS-side)  m_{(sb^+)_-}(x) = o(x)  and  m_{(sb^-)_+}(x) = o(x)  (x -> 0)   [nothing on b^theta].
Then there are norm-attaining f'_i -> f with finite base support and g'_i in C(f'_i), g'_i -> rho g; so (f, rho g) in cl NA, and (f, g)
in cl NA if kappa_w <= 1.
Proof. Z5's proof of T8 (itself a modification of thm:engineered) with one change: for j in F cap [1, N_w] put
r_j := (8 rho s_1|b^theta_j| - |a_j|)_+ and
  a'' := a 1_{[1,N_w]} + sum_{j in K cap [1,N_w]} m_j z_j e_j* + sum_{j in F cap [1,N_w]} r_j s_j e_j*,   m_j := 4 rho s_1|b^theta_j|,
i.e. support coordinates in the window are raised to modulus max(|a_j|, 8 rho s_1|b^theta_j|), same sign; all other definitions and the
order of choices are unchanged.
(1) supp a' = (F cap [1,N_w]) union {window contacts with b^theta_j != 0} and z' = sgn a' there, so f' is norm attaining; ||a'' - a||_1 <=
alpha(N_w) + 8 rho s_1||b^theta||_1, i.e. (E1) of lem:approxfacts holds with 8 in place of 4. Lemma lem:approxfacts (E2)-(E5), Lemmas
lem:F1, lem:anchor, lem:scrambling and Steps 1, 2, 4, 6 use a'' only through (E1) and the forced data of f'; at late stages q*(a'') <= 2 and
|a'_j| >= |a''_j|/2 >= |a_j|/2 on F cap [1, N_w].
(2) Step 3 (base) on j in F cap [1,N_w]: a'_j + tau B^diamond_j = (1 - tau rho c)a'_j + tau rho beta^diamond_j with |tau rho c| <= 1/2, so
s_j(1 - tau rho c)a'_j >= |a''_j|/4. For diamond = theta (|tau| <= s_1): |tau rho beta^theta_j| <= rho s_1|b^theta_j| <= |a''_j|/8: no flip.
For diamond = +- (s_1 < |tau| <= T_0, sgn tau = diamond): the anti-sign part of tau rho beta^diamond_j is <= |tau| rho beta_j with beta =
(sb^+)_- resp. (sb^-)_+, and |a''_j| >= |a_j|, so as in Z5 a flip needs |a_j| < 4 rho|tau| beta_j and costs <= 2|tau| rho beta_j: total
Fl(tau) <= 2 rho|tau| m(4 rho|tau|), m := m_{(sb^+)_-} + m_{(sb^-)_+}. All other coordinates verbatim.
(3) The Step-0 condition "2 rho|tau| m(4 rho|tau|) <= delta tau^2/16 for |tau| <= T_0" uses only the side parts and holds for small T_0 by
(CS-side); Steps 5-6 as in Z5. QED
Remark. The raises do for support coordinates what the window masses do for contacts: absorb the two-sided use of the average data
below scale s_1; their total mass is O(s_1) whatever b^theta is. Consequently R1's requirement on |bbar^theta| is superfluous.

Theorem 2.2 (flip-extended version). Same as Theorem 2.1, but instead of (CS-side) assume: for some t_0 > 0,
  rho^2 max_{diamond = +,-} [ Gamma_w(b^diamond, omega^diamond) + sup_{0 < r <= t_0} Fl_r(b^diamond) ] < 1,
  Fl_r(b^+) := 2q_0 Exc_{(sb^+)_-}(r)/r^2,  Fl_r(b^-) := 2q_0 Exc_{(sb^-)_+}(r)/r^2,  and rho^2 Gamma_w(b^theta, omega^theta) < 1.
Then (f, rho g) in cl NA. PROVED. Proof: in Step 3 the side flip cost at f' is <= Exc_{beta}(rho|tau|(1 + O(T_0))) (|a'_j| >= |a_j|(1 - O(T_0
+ s_1)) after normalization), so it contributes at most (rho^2 tau^2/2)(sup_{r <= t_0}Fl_r + o(1)) to Gammahat (weight c' -> q_0), and it is
O(tau^2), so the rebalancing constant K_sharp of Step 0 still exists. Step 5 then reads Gammahat + E <= (tau^2/2)(rho^2 kappa^fl + delta/2),
kappa^fl := max_diamond(Gamma_diamond + sup Fl) and Gamma_theta <= kappa_w; with delta := (1 - rho^2 kappa^fl)/2 (fixed before T_0 <= t_0/rho)
this is <= (tau^2/2)(1 - delta). The theta-data carry no flips (raised). QED
