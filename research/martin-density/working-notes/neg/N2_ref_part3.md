# N2 referee, part 3: Proposition 2.3, Theorem 2.4, Remarks 2.5

Scripts: neg/N2_ref_work/pb_ref_check2.py (exact decompositions in the high-precision model with the true parameters).

## 3.1 Proposition 2.3 (gamma h in C(f) and in C(f_N), uniformly) -- CORRECT (PROVED)

Re-derived every step.
 * Algebra: with Theta := omega - d w, W := w + t Theta, B := gamma h - L* Theta, one has (a + tB) + L*W = f^# + t gamma h; and
   L* omega = c(nu) h + E, so B = -E + d psi once c(nu) = gamma.  Side -: W := (1 + sd) w - s omega, B := gamma h - L*(omega - d w).
 * S(t) = {k in Sigma_+ : Phi(k) <= theta t} is INFINITE (all deep staircase indices); its largest depth exceeds theta t/8 because the
   depth ratio inside Sigma_+ is exactly 1/8 and t <= t_+ = Phi(12)/theta; sum_{S(t)} Phi^2 <= (64/63)(theta t)^2.
 * Block: ||D W||^2 = (C + t d M)^2 + t^2(||D omega||^2 - d^2) (identity checked), sqrt(A^2 + B) <= A + B/(2A), and ||W||_inf =
   (1 - t d)M (attained at k = 1); so N(W) <= 1 + t^2 ||D omega||^2/(2(C + t d M)) <= 1 + 0.0325 t^2.
 * Base: ||U*A||_H <= mu_1(abar + tB(1)) + t^2 sum_{j>=2} mu_j^2 B_j^2/(2 mu_1(abar + tB(1))), and sum_{j>=2} mu_j^2 B_j^2 <= mu_2^2 ||B||_1^2 =
   2^{-13} mu_1 ||B||_1^2, so N2's quadratic remainder t^2 mu_1 ||B||_1^2/(2 abar) is a valid (generous) bound.  First-order term:
   (1+mu_1)B(1) + ||B 1_{[2,inf)}||_1 = B(zhat^#) + sum_{j>=2}(|B_j| - zhat^#_j B_j) <= B(zhat^#) + (3/2)||B 1_{[2,inf)}||_1, with
   B(zhat^#) = -E(zhat^#) + d psi(zhat^#) <= 4 S_2 (d < 0 <= psi(zhat^#) = |R zhat^#|) and ||B 1_{[2,inf)}||_1 <= 8.01 S_2 + 2 S_2.
   Hence q*(A) <= 1 + 19.2 S_2 t + O(2^{-11} S_2^2 t^2) <= 1 + 0.32 t^2 (S_2 <= 0.01626 t).
 * Large |t|: p*(h) <= q*(h) <= 2.0004; 2.002 gamma_0 = 1.001e-4 <= (3/8) t_- = 1.144e-4; s(t) >= 1 + 3t^2/8 on |t| <= 1, and
   (s(t) - 1)/|t| >= sqrt2 - 1 for |t| >= 1 (convexity).
 * All t are covered: (0, t_+] by side +, [-t_-, 0) by side -, |t| >= t_- by the trivial bound.

Numerical confirmation (pb_ref_check2.py; mpmath 60 digits, true parameters, t from t_+- down to 1e-15 t_+-, both sides, rows f,
f_3, f_10, f_60): identity error of the decompositions <= 2e-61;
   max over t, sides of (max(q*(A), N(W)) - 1)/t^2 = 1.28e-4 for gamma = gamma_0, and = 0.1174 for the maximal content nu = 1/2
   (N2: 0.119 in its coarser model; claimed bound 0.32; needed 3/8).
The constant gamma_0 = 5e-5 is close to the limit of THIS proof: the trivial bound 1 + q*(h) gamma |t| <= s(t) at |t| = t_- needs
gamma <~ t_-/(2 q*(h)) = 7.6e-5 (5.7e-5 with N2's 3t^2/8); the decompositions themselves allow contents up to 0.0048.

## 3.2 Theorem 2.4 -- CORRECT (PROVED), with one precision

(a) S(f) = (l_1(F) cap xi^perp) + span{y_k : k in Q}: F = {1} and xi_1 = q_0(1 + mu_1) != 0 kill the base part, Q = empty (Lemma 2.2(iv)).
    K(f) is contained in cl S(f) = {0} (Part I prop:intrinsic(b)).  (MS) fails: the Sigma_+ margins are mu_k = q_0 |u_k(zhat)| -
    vartheta Phi(k) <= 4 q_0 Phi(k) and positive (numerically about 3.2 q_0 Phi(k)), so sum_{k in P, mu_k < s} Phi(k) >= s/(33 q_0).
(b) Lemma 2.2(i) + Prop. 2.3 + Part I prop:reduction(d).  Correct and, as N2 says, involves no engineering.
(c) Correct as a description.  PRECISION (P-c): at f_N the generic carriers whose targets live beyond N become strict non-peaks
    (observed numerically: Q(f_3), Q(f_10) contain many generic indices), so S(f_N) != {0} in general; the correct reason why gamma h
    has no representation through F and the blocks at f_N is (T-c): gamma h - b in c_00 cap Y = {0} for every b supported in F, so
    gamma h is not in l_1(F) + Y (and a fortiori not in S(f_N)).  The general form is the following lemma (PROVED here).

LEMMA R2 (unbounded block parts).  Let f' in S_{p*} have finite F' cup K', normer eta, q'_0 := q**(eta), and room
eta_free := inf_{j notin F' cup K'} (1 - |z'_j|) > 0 (automatic at NA rows, where z' in c_0).  Let g in C(f'), and for t > 0 let
f' +- t g = A_+- + L* W_+- be decompositions with max(q*(A_+-), ||W_+-||_{V*}) <= s(t) (they exist: G3 Cor. 1.3); put
B_+- := +-(A_+- - a')/t and Theta_+- := +-(W_+- - w')/t.  If g is not in l_1(F' cup K') + Y, then ||Theta_+(t)||_{V*} -> infinity and
||Theta_-(t)||_{V*} -> infinity as t -> 0+.  In particular this holds for every finitely supported mate g of an NA row f' with
supp g not contained in F' cup K'.
Proof.  By G3 Cor. 1.3 and Lemma 1.2 (refereed), E_b(A_+) + E_b(A_-) <= t^2/q'_0, and at j notin F' the summand of E_b(A_+-) is
>= (1 - |z'_j|) t |B_+-(j)| (a'_j = 0 there).  Hence sum_{j notin F' cup K'} |B_+-(j)| <= t/(eta_free q'_0) -> 0.  Suppose
||Theta_+(t_n)|| <= R along t_n -> 0.  The ball of V* is weak*-compact and L* is weak*-to-norm continuous on bounded sets (L compact),
so along a subsequence Theta_+(t_n) -> Theta weak* and L*Theta_+(t_n) -> L*Theta in l_1; then B_+(t_n) = g - L*Theta_+(t_n) -> g - L*Theta
=: b in l_1, and b vanishes off F' cup K' by the first estimate.  Thus g = b + L*Theta in l_1(F' cup K') + Y (eq. (Lstar)):
contradiction.  The same for Theta_-.  For g in c_00 with supp g not in F' cup K': g - b in c_00 cap Y = {0} would force g = b.  QED
So at NA rows, finitely supported mates off F' cup K' are carried ONLY by scale-dependent decompositions with unbounded block
parts (as in Prop. 2.3, where ||Theta|| ~ nu M/t), and Prop. 2.3 shows that such mates exist at NA rows.

## 3.3 Remarks 2.5
 (1) CORRECT (thm:tamefibre needs (MS); (MS) fails at f and at every f_N by the same margin computation).
 (2) CORRECT as an explanation for THIS row (staircase values decided on {2,3}; threshold pinned near 0.8 by the dominant peak;
     the base part uses only |z_j| <= 1/2 off F).
 (3) CORRECT (Part I prop:nonrecovery: for P1's example the canonical truncations are C-tame and fail).
 (4) CORRECT.  The heuristic in question is E's Round-1 gloss (r1/E_notes.md line 256), never used later as a theorem; E's PROVED
     statement (linear decompositions with zero first-order base excess at an NA point are two-sided and coincide) is not
     contradicted.  Lemma R2 is the precise form of the refutation: NA rows carry mates by one-sided, scale-dependent decompositions
     with unbounded block parts; the only universal linear constraint at NA rows is the base-switching bound (Lemma 3.4).
 (5) The factual part is CORRECT (gamma h carries no exact two-piece data at f_N: two-piece data are of the form b + R*(...) with
     b supported in F' cup K', excluded by Lemma R2 / (T-c)).  The methodological conclusion ("the sandwich route cannot work along
     all NA approximants") is a correct CAUTION but HEURISTIC as a general statement: it shows that a non-recovery proof cannot assume
     two-piece data at all approximants; it does not show that a given candidate f has (MS)-violating NA approximants carrying the
     relevant mates (that depends on T and f).
 (6) Upgraded to PROVED (with the operator of fix F3).  For p_n with n >= 2 blocks: block 1 is literally the one-block construction,
     so Lemma 2.2 holds for block 1 verbatim (its proof uses only block-1 vectors, ||Phi_1||_1 <= 1/2, Phi_1(1) = 1/4,
     ||Phi_1||_2^2 <= 1/12); the decompositions f^# + t gamma h = (a + tB) + R_1*W_1 + sum_{m>=2} R_m* w_m give, by lem:dualball for p_n,
     p*(f^# + t gamma h) <= max(q*(a + tB), N_1(W_1), 1), with the SAME constants as Prop. 2.3.  For Thm 2.4(a) in every block m: off P_m,
     |u_{k,m}(zhat)| <= |zeta_m|/m <= 2^{-m}, so the dominant carrier is a peak, C_m >= Phi_m(1) M_m, and the threshold satisfies
     bar-vartheta_m/m <= 2^{-m} 2^{m+1} = 2 (in units of Phi_m(k)); generic carriers (|value| >= 4 Phi_m(k)/n) and the staircase
     near-duplicates (|value| ~ 4 Phi_1(k) = 2^{m+1} Phi_m(k)) are non-degenerate peaks: Q_m = empty for all m, S(f) = {0}.

## 3.4 Overstatements to correct (O1, O2)
 (O1) N2 Section 0/3.5: "in the cleanest adversarial configuration the canonical truncations recover EVERYTHING".  PROVED is only:
      the segment [-gamma_0, gamma_0] h is contained in C(f) and in every C(f_N).  C(f) itself is not determined (it may contain
      larger multiples of h, up to the boundary gamma_max h, and other directions), and f in Rec (i.e. C(f) contained in Li C(f_N),
      or recovery of (f, rho gamma_max h) for rho near 1) is NOT proved.  Plausible (the forced data of f_N agree with those of f on
      every carrier that can carry content at small scales), but OPEN.
 (O2) "Principle 3.1 ... PROVED for T_PB": what is proved is the inheritance of the specific mates gamma h, |gamma| <= gamma_0, at the
      specific row f (and the threshold pinning of Lemma 2.2 at the rows f^#); nothing is proved for other rows of T_PB.
