# Y2 part 2: the threshold equation and strict monotonicity of the threshold (any admissible T)

Fix a block and drop its index.  Phi is a sequence of positive numbers with ||Phi||_1 < 1, D the diagonal operator, |.| the
norm of Remark rem:lemmaA, zeta in l_1 \ {0}, w = J(zeta) its norming functional, M = ||w||_inf, C = ||Dw||_2, P = {k : |w(k)| = M},
alpha as in Lemma lem:threshold.  Put
   theta(zeta) := |zeta| M / C,     nu_k := |zeta(k)| / Phi_k^2   (nu_k in [0, infinity)),
   A(th; zeta) := sum_k (|zeta(k)| - th Phi_k^2)_+ ,   B(th; zeta) := sum_k Phi_k^2 min(th, nu_k)^2 ,
   Psi(th; zeta) := A(th; zeta)^2 - B(th; zeta)     (th > 0).
(The series converge: (|zeta(k)| - th Phi_k^2)_+ <= |zeta(k)| and Phi_k^2 min(th, nu_k)^2 <= th Phi_k^2 nu_k = th |zeta(k)|.)
For the block vectors of the note, zeta = R_m^** zhat (or R_m xhat'), zeta(k) = lambda_{k,m} u_{k,m}(zhat), lambda = m Phi; then
nu_k >= theta  iff  |u_{k,m}(zhat)| >= (theta/m) Phi_m(k) = hat-vartheta_m Phi_m(k): theta/m is the threshold constant hat-vartheta of the
proof of Lemma lem:scrambling, and the margin is mu_{k,m} = q_0 Phi_m(k)(nu_k - theta)/m on P.

**Lemma T (threshold equation).  PROVED.**
(a) P = {k : nu_k >= theta(zeta)}; on P, |zeta| |alpha(k)| = |zeta(k)| - theta Phi_k^2; k is a degenerate peak iff nu_k = theta.
(b) |zeta| = A(theta; zeta)  and  |zeta|^2 = B(theta; zeta); hence Psi(theta(zeta); zeta) = 0.
(c) For every zeta' in l_1 \ {0}, Psi(.; zeta') has exactly one zero on (0, infinity); it is positive to the left of the zero and
    negative to the right.  Consequently theta(zeta') is that zero, and
        Psi(theta(zeta); zeta') > 0  implies  theta(zeta') > theta(zeta).
(d) (raising moves) Let k' be a coordinate and zeta' := zeta except at k', with sgn zeta'(k') = sgn zeta(k') or zeta'(k') = 0.
    Then theta(zeta') > theta(zeta) in each of the cases: (i) k' in P and |zeta'(k')| > |zeta(k')|; (ii) k' notin P and
    |zeta'(k')| < |zeta(k')|; (iii) k' a degenerate peak and |zeta'(k')| != |zeta(k')|.
(e) (perturbed raising moves) Let zeta' in l_1, Delta := | |zeta'(k')| - |zeta(k')| | > 0, E := sum_{k != k'} |zeta'(k) - zeta(k)|,
    A := |zeta|, theta := theta(zeta).  Then theta(zeta') > theta(zeta) if either
      (i') k' in P, |zeta'(k')| > |zeta(k')| and E < A Delta/(A + theta), or
      (ii') nu_{k'} > 0, |zeta'(k')| < |zeta(k')| (k' notin P, or k' degenerate) and E < nu_{k'} Delta/(2(A + theta)).

*Proof.* (a) By Lemma lem:threshold, zeta/|zeta| = alpha + D^2 w/C with ||alpha||_1 = 1, alpha supported in P with the signs of w.
For k in P, |w(k)| = M and alpha(k) has the sign of w(k) or vanishes, so |zeta(k)|/|zeta| = |alpha(k)| + Phi_k^2 M/C, i.e.
|zeta(k)| = |zeta||alpha(k)| + theta Phi_k^2 >= theta Phi_k^2.  For k notin P, |zeta(k)| = |zeta| Phi_k^2 |w(k)|/C < |zeta| Phi_k^2 M/C
= theta Phi_k^2.  Hence P = {nu_k >= theta}, and alpha(k) = 0 iff nu_k = theta (degenerate peaks).
(b) By (a), A(theta; zeta) = sum_{k in P} |zeta||alpha(k)| = |zeta|.  Next C^2 = sum_k Phi_k^2 w(k)^2.  On P, Phi_k^2 w(k)^2 =
Phi_k^2 M^2 = (C/|zeta|)^2 Phi_k^2 theta^2 and min(theta, nu_k) = theta.  Off P, w(k) = C zeta(k)/(Phi_k^2 |zeta|), so Phi_k^2 w(k)^2 =
(C/|zeta|)^2 Phi_k^2 nu_k^2 and min(theta, nu_k) = nu_k.  Summing, C^2 = (C/|zeta|)^2 B(theta; zeta).
(c) Fix zeta' != 0 and write A', B', nu'.  A' is continuous and nonincreasing, B' continuous and nondecreasing.  If th < sup_k nu'_k,
the set {k : nu'_k > th} is nonempty; on it each term of A' is strictly decreasing and each term of B' strictly increasing in th,
so Psi' is strictly decreasing on (0, sup nu').  As th -> 0+, A' -> ||zeta'||_1 > 0 and B' -> 0, so Psi' > 0 near 0.  If
th >= sup nu' (possible only if the sup is finite), A' = 0 and Psi' = -B' < 0.  If sup nu' = infinity, A'(th) -> 0 as th -> infinity
(dominated convergence) while B'(th) >= B'(1) > 0 for th >= 1, so Psi' < 0 for large th.  Hence Psi' has exactly one zero, Psi' > 0
before it and Psi' < 0 after it.  By (b) applied to zeta', theta(zeta') is a zero, hence the zero.  If Psi(theta; zeta') > 0 with
theta = theta(zeta), then theta lies before the zero: theta < theta(zeta').
(d) Put theta := theta(zeta) and use (c); Psi(theta; zeta) = 0 by (b).  (i) nu_{k'} >= theta and nu'_{k'} > nu_{k'}: the k'-term of A
increases by |zeta'(k')| - |zeta(k')| > 0 (both positive parts are the differences themselves), the k'-term of B is theta^2 Phi^2 in
both cases; so A' > A, B' = B and Psi(theta; zeta') > 0.  (ii) nu_{k'} < theta and nu'_{k'} < nu_{k'}: the k'-terms of A vanish for
both, the k'-term of B decreases from Phi^2 nu_{k'}^2 to Phi^2 nu'^2_{k'}; so Psi(theta; zeta') > 0.  (iii) nu_{k'} = theta: an increase
is case (i), a decrease is computed as in (ii) (the A-term stays 0, the B-term decreases).
(e) For x, y in R, |(x)_+ - (y)_+| <= |x - y|, and for a, b >= 0, |min(th,a)^2 - min(th,b)^2| <= 2 th |a - b|; hence the coordinates
k != k' change A by at most E and B by at most 2 theta E (Phi_k^2 * 2 theta |nu'_k - nu_k| = 2 theta | |zeta'(k)| - |zeta(k)| |).
(i') A(theta; zeta') >= A + Delta - E >= 0 (as E < Delta), B(theta; zeta') <= B + 2 theta E, so Psi(theta; zeta') >= (A + Delta - E)^2 -
A^2 - 2 theta E >= 2A(Delta - E) - 2 theta E > 0 by the hypothesis on E.
(ii') A(theta; zeta') >= A - E, and the k'-term of B drops by Phi^2(nu^2 - nu'^2) >= Phi^2 nu (nu - nu') = nu_{k'} Delta (with
nu := nu_{k'} <= theta, nu' := nu'_{k'} < nu); so B(theta; zeta') <= B - nu_{k'} Delta + 2 theta E and Psi(theta; zeta') >= (A - E)^2 - A^2
+ nu_{k'} Delta - 2 theta E >= nu_{k'} Delta - 2(A + theta)E > 0.  (Here A(theta; zeta')^2 >= A^2 - 2AE in all cases: if
A - E >= 0 because (A-E)^2 >= A^2 - 2AE, and if A - E < 0 because then A^2 - 2AE < 0.)  QED

**Remarks.** (1) Lemma T(b) is a closed form of the clamp equation of Lemma lem:F1 (divide by |zeta|^2: sum min(Phi_k x, v_k)^2 = 1
with x = M/C = theta/|zeta|, v_k = |zeta(k)|/(Phi_k |zeta|)); (a)+(b) give the threshold as the root of ONE explicit equation.
(2) Reading: moving mass toward the peaks (more at a peak, less at a non-peak) raises the threshold; the reverse moves lower it.
At a degenerate peak Psi has a concave kink, so both moves raise theta.
(3) Numerical check (Y2_work/threshold_check.py, 300 random blocks of size 5-13, CLARABEL SOCP for the block norm and its
norming functional): the identities (a),(b) hold to relative accuracy 5e-5 (solver accuracy); all 1100+ raising moves of type
(i),(ii) raise theta; for 200 tuned degenerate peaks both moves (+-1%) raise theta.
