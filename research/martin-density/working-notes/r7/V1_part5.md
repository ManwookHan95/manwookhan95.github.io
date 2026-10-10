# V1 part 5 — The aligned corner (D), far pulls on the peak itself, the residual list and its exhaustiveness

## 5.1 Corollary AC (the aligned corner is empty for D_Omega).  PROVED.
For D_Omega (diagonal base), N >= 1, F finite and every clean sub-window w of level l >= l_f, EVERY block has a threshold donor: a coarse
peak c with rho_c >= 1 + u(w) (Lemma D), dropped or of class R, at whose first far signature coordinate s = min(S_c ∩ (s_max(l), inf)) the
move (C3) raises |u_c(zhat)| by Lam/lambda_c ... 3Lam/lambda_c, Lam = T_lo(w)^3, either by a z-move (when the room toward vs_c carries at least
Lam/lambda_c) or by closing z_s := vs_c and placing a BANK of mass <= Design(l) Lam at s (Lemma DR); the block threshold rises by >= c_f Lam
(Lemma ST(b)) and every kept near-threshold swallowing-type carrier (weak, DEGENERATE, or tiny-gap strict non-peak) becomes a strict
non-peak of f^#_w (Lemma ST(c)), while all d-coefficients of the block are rescaled by the common factor A_m/A^#_m up to C_f Design b.
Consequently Y1's residual (d), Y2's aligned corner (d') and Y2's hypothesis (TD_m) are not needed for D_Omega: Master Theorem II has no
donor hypothesis.
Why the corner was open, and why banks close it.  Y1's and Y2's companions keep the base part a (hence e, nu) fixed and move only z;
a z-move raises |u_c(zhat)| at a coordinate s in S_c only if z_s != vs_c (room toward the peak's own sign).  The aligned corner is exactly
the case where every far coordinate of every usable peak is a CONTACT OF THE PEAK'S OWN SIGN (z_s = vs_c), so no z-move can push a peak
outward (and Y2-ref Lemma R-T's target moves may all have zero derivative).  A BANK at such a contact (mass vs_c mu at s, z unchanged) moves
the Hilbert part: by (3.1), vs_c u_c(zhat) increases by mu s_s^2 v_c(s)/nu + O(mu^2), every other coarse value changes only at second
order (diagonal base: <U^*u_k, k_s> = s_s u_k(s) = 0 for k != c), so the peak is pushed OUTWARD and the threshold rises (Lemma T2(b)).
Y4 Proposition 2.8(b) (banks only raise z-signed functionals) is not an obstruction here: raising the donor's value is exactly what is
needed.  Banks are admissible in Theorem E (Y4 Lemma 2.3; Theorem E'' here).  Numerics: V1_work/bank_donor_check.py (finite model,
diagonal base; in the regime mu <= 0.05 s^2 v nu: 140/140 raises; first-order formula exact up to 0.65 mu^2; other carriers move <= 0.37 mu^2;
when Lemma T2(b)'s hypothesis holds the raise is >= 11 x its lower bound).

## 5.2 Lemma IP (far pulls on the peak itself: inward push of near-threshold coordinates).  PROVED.
Fix a block, zeta in l_1 \ {0}, theta := theta(zeta), A := |zeta|, nu_k := |zeta(k)|/Phi_k^2.  Let 0 < b <= 1/2, N a nonempty set of coordinates
with |nu_k - theta| <= theta b (k in N), c >= 4b(A + theta), and let zeta' satisfy: for k in N, sgn zeta'(k) = sgn zeta(k) and |zeta'(k)| =
|zeta(k)| - c_k Phi_k^2 with c_k in [c, theta/2]; for k notin N arbitrary changes with E := sum_{k notin N} |zeta'(k) - zeta(k)| <=
theta c sum_{k in N} Phi_k^2/(8(A + theta)).  Then theta(zeta') > theta, and nu'_k <= theta(zeta') - (c - theta b) for every k in N: every pushed
coordinate is a STRICT NON-PEAK of zeta' with nu-gap >= c - theta b >= c/2.
Proof.  Put x := theta.  A'(x) = sum_k (|zeta'(k)| - x Phi_k^2)_+: for k in N, |zeta'(k)| - theta Phi_k^2 = Phi_k^2(nu_k - c_k - theta) <= Phi_k^2(theta b - c)
< 0, so N contributes 0; for k notin N the terms change by at most |zeta'(k) - zeta(k)|; and A = sum_{P}(|zeta(k)| - theta Phi_k^2) with the N∩P
terms <= theta b Phi_k^2.  Hence A'(theta) >= A - y, y := theta b sum_N Phi^2 + E.  B'(x) = sum_k Phi_k^2 min(x, nu'_k)^2: for k notin N the terms
change by at most 2 theta |zeta'(k) - zeta(k)| (|min(x,a)^2 - min(x,a')^2| <= 2x|a - a'|); for k in N, min(theta, nu_k) >= theta(1-b) and
0 <= nu'_k = nu_k - c_k <= theta(1+b) - c_k, so the term drops by >= Phi_k^2[theta^2(1-b)^2 - (theta(1+b) - c_k)^2] = Phi_k^2 (c_k - 2 theta b)(2 theta - c_k)
>= Phi_k^2 theta (c - 2 theta b) (as c_k <= theta/2 <= theta).  So B'(theta) <= B - theta(c - 2 theta b) sum_N Phi^2 + 2 theta E.  Using B = A^2
(Lemma T(b)) and A'^2 >= A^2 - 2Ay (if A - y >= 0 since A' >= A - y; if A - y < 0 the right side is negative):
   Psi'(theta) >= -2A(theta b sum_N Phi^2 + E) + theta(c - 2 theta b) sum_N Phi^2 - 2 theta E = theta sum_N Phi^2 (c - 2b(A + theta)) - 2(A + theta)E
              >= theta sum_N Phi^2 c/2 - theta c sum_N Phi^2/4 > 0.
By Lemma T(c), theta(zeta') > theta.  Finally nu'_k = nu_k - c_k <= theta(1 + b) - c < theta(zeta') - (c - theta b).  QED
Numerics: V1_work/lemma_ip_check.py (E = 0: 2962 tests, 0 violations; the gap bound is attained up to 1e-7) and lemma_ip_check2.py
(E > 0 up to the allowed size: 3942 tests; the gap conclusion holds in all of them; theta' > theta holds in all cases where the predicted
raise is above double-precision resolution — the 13 remaining cases have predicted relative raise 4e-20..3e-17 and return theta' = theta
exactly in floating point).
Reading.  This turns Y4-ref C.8(ii) ("tiny-margin swallowing-type peaks are pushed below threshold by a pull", SKETCH) into a theorem at
the block level, for any number of near-threshold coordinates pushed simultaneously, and shows that a push much larger than the margin
RAISES the threshold (the margin part of the push lowers it at rate A/((A+theta) sum_P Phi^2), Y2-ref 1, but once a coordinate crosses the
threshold the inward push raises it, Lemma T(d)(ii); net effect positive as soon as c >= 4b(A + theta)).  Per carrier, a pull at j in S_l with
2 m v_l(j)/Phi_l in [c, 2^{G_l} c] realizes c_l (bounded gaps), at cost O(v log 1/v) (Y4-ref P1).  It is NOT used in the assembly: pushes
that dominate the threshold drift (c >> Design b) move the d-components of rays through the pushed carriers by amounts between b and u,
destroying the tiny/robust dichotomy of (R5) on which the exact tuning rests; the donor raise rescales all d-coefficients of a block by one
common factor and moves no value, so it is compatible with the tuning.  Lemma IP is the right tool when no tiny d-component passes through
the near-threshold carriers (e.g. single-carrier blocks).

## 5.3 The residual list for D_Omega, F finite (contrapositive of Master Theorem II).  PROVED (as a logical statement).
Let T = D_Omega, N >= 1, f in S_{p_N^*} with F finite.  If f notin Rec, then there is l_0 such that for EVERY level l >= l_0 and EVERY clean
sub-window w of level l at least one of the following holds:
 (B_w) [genuinely multi-block ray]  some extreme ray r of the zero-cost cone C(kappa(w)) has ROBUST d-components in two different blocks:
       |sum_{l'' in supp r, m(l'')=m_i} r(l'') eps_{l''} u_{l''}(zhat)| >= u(w) Phi_max(r, m_i), i = 1, 2, m_1 != m_2;
 (C_w) [coherent shift resonance]  some block has no upper or no lower shift source at w (I_up(w) ∪ I_lo(w) != {}), and the shift cost of
       the shift pattern of f at w is TINY: c_{pi(w)}(f) <= b(w).
(D) is EMPTY (Corollary AC).  (E) (infinite F) is outside the statement.
Exhaustiveness (checked item by item).  Master Theorem II has exactly three hypotheses: F finite; (SH_w); (VR_w), at one clean sub-window
of infinitely many levels.  Clean sub-windows exist at every level (Theorem 2').  At a clean w every rate object is tiny or robust, so
NOT (SH_w) <=> (C_w) and NOT (VR_w) <=> (B_w).  Every other ingredient holds unconditionally for l >= l_f(f): donors (Lemma D), the
threshold buffer (Lemma ST), exact tuning (Lemma TU: the tuning system is always consistent, V^(2) = R val^(2), and its size Design b is below
c_T), no slaving (Lemma NS), robust rates (Lemma RR), Hoffman constants (G**, H_tune: design constants), zero cost at f^# (Step 3 of
Proposition TR), the supports of Theorem E'' (Proposition TR(iv)), the window arithmetic (proof of 4.3).  No growth condition, no rate
condition, no compensation, sign or donor condition, and no hypothesis on contact sets, slaving or degenerate peaks remains.
Precisions.  (1) Both items are properties of f at level l and of the explicit numbers b(w), u(w) only; (B_w) is combinatorial-linear
(values of finitely many carriers on finitely many extreme rays), (C_w) is a convex-analytic condition at f.  (2) (B_w) never occurs if
N = 1, nor through blocks that are one-signed at w (Remark (2) of part 2).  (3) The residual of Lemma Z for D_Omega is SMALLER than the
list: f must in addition lie outside every other class proved recoverable for D_Omega (Theorem 1'(d)): R_0^pm, R_S, R_BT (Cor. D2 of S3),
Z4 Theorem A'', Z6 Theorem U', Y2 Theorem Y, Y1 Master Theorem 5.4 (with (SP_w) replaced by (SH_w): Y1's proof uses (SP_w) only through
the shift bound, which Lemma S provides; with its own z-move donors (Do_w)), and the infinite-F classes of Z5/Y3 do not apply (F finite).
In particular the part of (B) in which every block met by a doubly-robust ray is COMPENSATED at w (Y1's (Rep^+_m), (Rep^-_m) at f^#), all
other blocks are one-signed, (NN_w) holds and z-move donors exist, is covered by Y1 5.4.  (4) (C_w) with c_pi > 0 but tiny is not exactified:
c_pi is computed at f (pinning at f), and no companion move changes the decomposition at f.

## 5.4 What is new, and what remains
NEW (PROVED here): bank donors (Lemmas D, DR, Corollary AC: aligned corner empty); exact tuning with an explicit solution (Lemma TU,
re-proving Y4-ref P4 with design constants); the ray-component rate objects (R5) and exact neutralization of all tiny components by one
least-norm solve (Lemma CO, NS), replacing (Cmp_w)/(NN_w) by (VR_w); the clean-window shift-cost lemma (Lemma S, port of Y2 Prop. 5.2 with
I_up ∩ I_lo = {} from Lemma D); the assembly (Lemmas CO, ST, NS, RR; Proposition TR: split w.r.t. z^(2), balancing with a/a(zhat^#),
Hilbert comparison at changed e, supports for Theorem E''); Theorem E''; Master Theorem II and Corollaries M-II.1 (N = 1) and M-II.3
(maximal contact); Lemma IP.
OPEN for D_Omega, F finite: (B) genuinely multi-block rays (vector-valued d-rows; the Hoffman constant of {mu >= 0 : sum mu_r D_r = 0} is
governed by minors of the ray d-matrix, the rate objects (R7); tiny-but-nonzero minors are not exactifiable by value tuning without
destroying robust components — determinantal); (C) coherent shift resonance.  (E) infinite F (O4-crit, O4-nd, O4-box) as in ADDENDUM 6.
Lemma Z, and density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2), remain OPEN for every admissible T, including D_Omega.  No
counterexample is claimed; nothing found points to one.
