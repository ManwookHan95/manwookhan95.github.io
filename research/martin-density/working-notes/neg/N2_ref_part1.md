# N2 referee, part 1: the witness calculus (N2 Section 1 = N2_part1.md)

Notation as in Part I (canonical base, finite block set I).  Scripts: neg/N2_ref_work/lemma14_check.py,
lemma14_check2.py, lemma14_balanced.py, reading_counter.py.

## 1.1 Lemma 1.1 (single-piece witness) -- CORRECT (PROVED)
Re-derived.  For g' in C(f') and any x in X, |g'(x)| <= r_{f'}(x) = (p(x)^2 - f'(x)^2)^{1/2} (Part I prop:reduction(a));
hence h(x) <= r_{f'}(x) + p*(h - g') p(x) and dist_{p*}(h, C(f')) >= (h(x) - r_{f'}(x))/p(x).  With x = x' + y this is
Lemma 1.1; with x = x' (r_{f'}(x') = 0) the second inequality.  Precision: neither norm attainment of f' nor the special
form x' + y is used; the inequality holds at every row and every x != 0.

## 1.2 Remark 1.2 (minimax identity) -- CORRECT (PROVED)
dist(h, C) = inf_{g' in C} sup_{x in B_p} (h - g')(x).  C = C(f') is convex and weak*-compact (Part I prop:primal), B_p is
convex, and (g', x) -> (h - g')(x) is affine in each variable and weak*-continuous in g' for fixed x in X.  Sion's minimax
theorem gives inf sup = sup inf = sup_{x in B_p} (h(x) - max_{g' in C} g'(x)) = sup_{x in B_p} (h(x) - r~_{f'}(x)).

## 1.3 Remark 1.3 (finite test spaces) -- CORRECT, but the cited justification is incomplete (fix F1)
N2 justifies the "only if" direction as "the (R3) sufficient condition read contrapositively".  (R3) / Part I cor:finite
are statements about the WHOLE fibre (all of C(f) along one sequence); the single-mate statement needs its own compactness
argument.  Complete proof:

CLAIM.  (f, rho g) is not in cl NA((c_0,p), l_2^2) iff there are delta > 0 and a finite-dimensional subspace E of c_00 such that
every f' in NA cap S_{p*} with p*(f' - f) < delta satisfies sup_{x in E, p(x) <= 1} (rho g(x) - r~_{f'}(x)) >= delta.

Proof.  "If": for such f' and every g' in C(f') and x in E with p(x) <= 1, rho g(x) - g'(x) >= rho g(x) - r~_{f'}(x), so
p*(rho g - g') >= delta after taking the sup over x; hence dist(rho g, C(f')) >= delta for all NA f' within delta of f, and Part I
lem:pair excludes (f, rho g) from cl NA.  "Only if": fix x_1, x_2, ... in c_00 dense in c_0 and E_n := span{x_1,...,x_n}.  If the
condition fails for (delta, E) = (1/n, E_n) for every n, there are NA f_n with p*(f_n - f) < 1/n and
sup_{x in E_n cap B_p} (rho g(x) - r~_{f_n}(x)) < 1/n.  By Part I thm:compact all C(f_n) lie in one norm-compact set; by Blaschke's
selection theorem a subsequence C(f_{n_j}) converges in the Hausdorff metric to a compact convex set A, and support functions
converge: h_A(x) = lim_j r~_{f_{n_j}}(x) for every x in c_0 (Part I proof of thm:lowerlimit).  For x in E_m cap B_p (m fixed,
n_j >= m) we get rho g(x) <= h_A(x).  Both sides are positively homogeneous and p-Lipschitz (h_A <= p, g in B_{p*}), and the union
of the E_m is dense, so rho g(x) <= h_A(x) for all x in c_0.  A is weak*-compact and convex, so rho g in A (separation by
x in c_0), and dist(rho g, C(f_{n_j})) <= d_H(A, C(f_{n_j})) -> 0.  By lem:pair, (f, rho g) in cl NA.  QED
(The sup over the compact set E cap B_p is attained; delta in the conclusion is the smaller of the two deltas.)

## 1.4 Lemma 1.4 (block excess by a primal splitting) -- CORRECT (PROVED); its "Reading" is FALSE as stated (fix F2)

Re-derived line by line (zeta' = sigma' alpha' + D beta', beta' = sigma' D w'/C', |zeta'+t eta| <= max(||x_0||_1, ||b||_2);
no sign change of x_0 by (i); ||b||_2 <= sigma' + t w'(eta_2)/C' + t^2 ||D^{-1}eta_2||^2/(2 sigma'), whose right side is
(A + sigma'^2)/(2 sigma') > 0 so the square-root step is legitimate; (ii) makes both linear coefficients equal to w'(eta)).
Useful remark: (ii) is equivalent to w'(eta_1) = M' w'(eta).  Numerically: 3962 random valid splits, no violation
(lemma14_check.py; largest value of lhs - bound = -2.8e-14).

THE READING.  N2 states (Section 1 and summary): "in direction y only strict non-peaks, degenerate peaks and peaks with margin
< t|u_k(y)| contribute, each by at most m^2 t^2 u_k(y)^2/(2 sigma')".  This ignores condition (ii) (balance between the l_1 and
the l_2 part), and it is FALSE literally:
COUNTEREXAMPLE (reading_counter.py).  One block, Phi = (1/4, 1/8, 1/16, 1/32), zeta = (0.25, 0.1125, 0.000625, 0.025):
carriers 1, 2, 4 are robust peaks, carrier 3 a strict non-peak.  Push eta = Phi(1) e_1 on the ROBUST dominant peak (no carrier
is "relevant" in N2's sense and eta vanishes on the strict non-peak).  The exact excess satisfies excess/t^2 -> 1.5119e-5 > 0,
which equals the exact second-order coefficient of Part I lem:localformula, (1/2) d_S^2 Lambda (dS)^2 = C c_Q (dS)^2/(2|zeta| F_2)
with c_Q = ||D(w 1_Q)||^2, F_2 = sum_P Phi^2.  So every change of the peak sum costs at second order in proportion to the D-mass
of w' off the absorbing peaks, whatever the margins.

CORRECTED STATEMENTS (PROVED here; numerically checked, lemma14_check2.py and lemma14_balanced.py).

LEMMA 1.4' (refined splitting bound).  Under (i), (ii) of Lemma 1.4 and c := sigma' + t w'(eta) > 0,
      |zeta' + t eta| - w'(zeta' + t eta) <= t^2 ||P_perp D^{-1} eta_2||_2^2 / (2c),
where P_perp is the orthogonal projection of l_2 onto (D w')^perp.
Proof.  ||x_0||_1 = c as in Lemma 1.4.  With e := D w'/C' (a unit vector), beta' = sigma' e and D^{-1}eta_2 = X e + Y,
X = <e, D^{-1}eta_2> = w'(eta_2)/C' = w'(eta) (by (ii)), Y = P_perp D^{-1} eta_2.  Then ||b||_2^2 = (sigma' + tX)^2 + t^2||Y||^2 =
c^2 + t^2||Y||^2, so ||b||_2 <= c + t^2||Y||^2/(2c); and w'(zeta' + t eta) = c.  QED

LEMMA 1.4'' (balanced relevant-carrier bound).  Let s_k := sgn w'(k), t > 0, eta in l_1.  Let A be a subset of supp alpha' such
that for every k in A: s_k eta(k) >= 0 or t|eta(k)| <= sigma'|alpha'(k)|/2 ("absorbed carriers"); put R := N \ A ("relevant
carriers": it contains Q', the degenerate peaks and the peaks pushed beyond half their room) and assume ||D^{-1}(eta 1_R)||_2 <
infinity.  Let A_0 be a nonempty subset of A ("balancing peaks"), F_0 := sum_{k in A_0} Phi(k)^2 and
      kappa := ( sum_{k in R} w'(k) eta(k) - C' sum_{k in A} s_k eta(k) ) / F_0 ,
and assume t|kappa| Phi(k)^2 <= sigma'|alpha'(k)|/2 for k in A_0 and c := sigma' + t w'(eta) > 0.  Then
      |zeta' + t eta| - w'(zeta' + t eta) <= t^2 ( ||D^{-1}(eta 1_R)||_2 + (|kappa|/M') ||D(w' 1_{N \ A_0})||_2 )^2 / (2c).
Proof.  eta_1 := eta 1_A + kappa s 1_{A_0} Phi^2 and eta_2 := eta - eta_1 = eta 1_R - kappa s 1_{A_0} Phi^2.  (i): eta_1 lives in
A, which is contained in supp alpha'; if s_k eta_1(k) < 0 then |eta_1(k)| <= |eta(k)| 1[s_k eta(k) < 0] + |kappa| Phi(k)^2 1_{A_0}(k), so
t|eta_1(k)| <= sigma'|alpha'(k)|.  (ii) in the form w'(eta_1) = M' w'(eta): w'(eta_1) = M' sum_A s_k eta(k) + kappa M' F_0 (w' = M' s on
A_0, a set of peaks) and w'(eta) = M' sum_A s_k eta(k) + sum_R w'(k) eta(k); equality is the definition of kappa (M' - 1 = -C').
Finally D^{-1}eta_2 = D^{-1}(eta 1_R) - (kappa/M') D(w' 1_{A_0}) and D(w' 1_{A_0}) = D w' - D(w' 1_{N \ A_0}), whose first term is
killed by P_perp.  Apply Lemma 1.4'.  QED

READING (corrected).  At scale t in direction eta = R y, the block excess is bounded by the relevant carriers PLUS a balancing
term (|kappa|/M') ||D(w' 1_{N \ A_0})||: it vanishes when the strict non-peaks and the relevant carriers carry no D-mass of w'
(e.g. Q' empty and R = empty), and is small when they are deep, but it is not a sum of per-carrier terms.  For a NON-recovery
proof (which needs UPPER bounds on R_{f'}) the literal reading would UNDERESTIMATE the excess and hence produce invalid
witnesses; Lemma 1.4'' (or the exact lem:localformula) must be used instead.  Impact on N2: none of N2's PROVED results uses
the reading (it is used only in the assessment 3.6), so this is a correction of a tool, not of a theorem.

## 1.5 Lemma 1.5 (base flatness) -- CORRECT (PROVED)
Re-derived; it is Part I lem:flat at an NA normer (z' + y/c' in B_{c_0}, a'(y) = 0).  Consequently Delta'(y) =
sum_m [ |R_m(x'+y)|_m - w'_m(R_m(x'+y)) ] for such y (Part I lem:excess).

## Verdict on N2 Section 1
Lemma 1.1, Remark 1.2, Lemma 1.4, Lemma 1.5: CORRECT.  Remark 1.3: CORRECT with the proof above (F1).  The relevant-carrier
reading of Lemma 1.4: FALSE as stated; replace by Lemmas 1.4', 1.4'' (F2).  The statement "non-recovery is equivalent to a
uniform witness inside a fixed finite-dimensional space of finitely supported vectors" is correct (Remark 1.3 as proved
above), with the witness being the full sublinear envelope r~_{f'} (multi-piece decompositions), not only single pieces.
