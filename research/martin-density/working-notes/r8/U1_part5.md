# U1 part 5 — Mixed activity classes, MASTER THEOREM IV, the remaining step

Setting of part 4: D^{U1}, N fixed, F finite, w a clean sub-window of a main stage L >= l_f, an activity class a with active set A and
signs sigma_m = sgn Delta'_m (m in A).  A is ONE-SIGNED if all sigma_m agree (or A is empty), MIXED if A_- := {sigma = -1} and
A_+ := {sigma = +1} are both nonempty (possible only for N >= 2).  thm:engineered needs (SC) exactly for I_- := {m : Delta d_m < 0}, i.e. for
A_- (Delta d_m and Delta'_m have the same sign up to the positive factors M, kappa); blocks of A_+ need nothing (cor:D1 / Theorem E^>=).

## 5.1 Lemma 5.1 (exactness in every class, mixed ones included).  PROVED.
For every class a (one-signed or mixed) the companion f^# of part 4 can be completed EXACTLY: there is z^* in [-1,1]^{J_free} such that at
f^# := f(z^*) the vector V(Domega(t)) is z^#-admissible off F^# for every scale t of the (class, cube) set S, with the common true shift
Delta''^* (the same for all t in S).
Proof.  Proposition 2.2(c) (normalization) works inside the cone Gamma^#(kappa, a) and never uses signs.  In step (1c) re-realize the values
of Omega_act exactly (as done in configuration (ii)); then Lemma 4.6(a) gives Delta''(t) = Delta'^* kappa'/kappa^#, common to all t in S,
and kappa^#(z') is continuous in z'.  The proof of Lemma 4.4 (Schauder-Tychonoff for Psi(z')_j = clamp(z'_j + V(z')(j)), V2 Lemma C5) uses
only continuity of z' -> V(z') and the common ray, not the signs of the shifts.  The fixed owners (a)-(c) are handled by Lemma 4.2,
whose estimates do not use the signs either; E_c by part 3.  QED
So in a mixed class the ONLY missing property is (SC) for A_- at f^#.  (C*-1), (C*-3), (C*-4), (C*-5) are closed for every class.

## 5.2 Lemma 5.2 (states of a negative fine carrier at an exact completion).  PROVED.
Let z be any point at which V is admissible on J_fine, l a fine carrier (stage > L + R_cl, not a tuned absorber) of a block m in A_-,
v_l := u_l(zhat), thr_l := vartheta_m Phi_m(l) (the peak threshold of lem:threshold), O(l) := the coordinates of supp u_l ∩ J_fine at which
no earlier carrier has a nonzero coefficient (O(l) ⊇ S_l: allowedness (a)), own_l := sum_{j in O(l)} |u_l(j)| (>= delta°_l), and
Y_l := v_l - sum_{j in O(l)} u_l(j) zhat_j (the part of the value fixed by earlier carriers and coarse coordinates).  Then exactly one of:
 (Z') |w_m(l)| < M/2, i.e. |v_l| < thr_l/2: a strict non-peak with gap > M/2;
 (R)  |w_m(l)| >= M/2 and sgn w_m(l) = sgn Y_l (or Y_l = 0): v_l = sgn(w)(|Y_l| + own_l), a peak with margin >= own_l - thr_l >= own_l/2;
 (W)  |w_m(l)| >= M/2 and sgn w_m(l) = -sgn Y_l, which forces |Y_l| < own_l and |v_l| = own_l - |Y_l|.
Proof.  If |w(l)| >= M/2, the coefficient |Delta''_m| lambda_l w(l) of l dominates every later term at every j in O(l) (the estimates of
Lemma 4.2 hold with |coefficient| >= |Delta''| lambda M/2), so V_j != 0 and admissibility forces z_j = sgn(w(l)) sgn(u_l(j)) on O(l)
(j notin F^#, so zhat_j = z_j): v_l = Y_l + sgn(w(l)) own_l, and sgn v_l = sgn w(l) (clamp formula).  Both sign cases are listed;
in the second, sgn(Y_l + sgn(w) own_l) = sgn w with sgn Y_l = -sgn w needs own_l > |Y_l|.  For |w| < M/2 the clamp formula
|w(l)| = M |v_l|/thr_l gives the bound and gap = M - |w| > M/2.  own_l >= delta°_l >= 2 thr_l by (W3).  QED

## 5.3 Lemma 5.3 (an (SC) criterion that tolerates wrong branches).  PROVED.
Call a negative fine carrier BAD if its value lies in the THRESHOLD BAND
      B_l := ( thr_l (1 - Phi_l^{1/2}/M),  thr_l + Phi_l^{1/2} ).
If at f^# no negative fine carrier is bad (and the coarse carriers and tuned absorbers are as in Lemma 4.3), then A_- satisfies (SC) at
f^#; the sequence can be taken common to all m in A_- and is explicit.
Proof.  Fix Upsilon >= 1.  Coarse carriers and tuned absorbers: finitely many, none contributes for s < s_0 (Lemma 4.3 (1), (2)).  A
fine negative carrier contributes to Scr_m(Upsilon s) only if (peak) mu_l = |v_l| - thr_l <= Upsilon s, or (strict non-peak) gap_l <= Upsilon s
or Phi_l gap_l <= Upsilon s.  Not bad means: a peak has mu_l >= Phi_l^{1/2}; a strict non-peak has gap_l = M (1 - |v_l|/thr_l) >= Phi_l^{1/2}.
Hence a contribution requires Phi_l^{1/2} <= Upsilon s or Phi_l gap_l <= Upsilon s; in the latter case either gap_l >= M/2, so Phi_l <=
2 Upsilon s/M, or gap_l < M/2, and then gap_l >= Phi_l^{1/2} gives Phi_l^{3/2} <= Upsilon s.  In all cases Phi_l <= X(s) := max(Upsilon^2 s^2,
2 Upsilon s/M, (Upsilon s)^{2/3}).  Order the fine carriers of ALL blocks by stage.  Inside a cluster (A1) the weights decrease by the
factor 4 ((A4)); between consecutive clusters, and from the last carrier before a main stage to that main stage, they drop super-
exponentially (c_{l+1} <= T_lo(l)^3 and (W4''); in particular Phi_{L'} <= Phi_{L'-1}^7 for every large main stage L', checked from
n^w_l >> 2^{l^3}: 3 n^w_l >= 14 l + 18 log_2(1/T_lo(l-1))).  Hence sum_{l >= L'} Phi_l <= 2 Phi_{L'} for main stages L'.  Choose main stages
L_i -> infinity and s_i with X(s_i) := Phi_{L_i}^{1/2} Phi_{L_i - 1}^{1/2}: then {Phi_l <= X(s_i)} = {l >= L_i}, the contributions are
<= 2 Phi_{L_i}, and s_i >= X(s_i)^{3/2}/Upsilon gives Phi_{L_i}/s_i <= Upsilon Phi_{L_i}^{1/4} Phi_{L_i - 1}^{-3/4} <= Upsilon Phi_{L_i - 1}^{1} -> 0.
So Scr_m(Upsilon s_i) = o(s_i) for every m in A_- along the same sequence.  QED
Remark.  (R) carriers are never bad: own_l >= delta°_l, while thr_l + Phi_l^{1/2} <= C c_l^{1/2} and in D^{U1} c_l <= T_lo(l-1)^3 <=
2^{-3 n^w_{l-1}} << (2^{-l-2^l-2})^8 <= (delta°_l)^8 for large l (S_l = {2^l(2i+1)}, so ||h_l||_1 >= 2^{-2^l}) — call this (W3'); (Z') carriers
are bad only if |v_l| > thr_l (1 - Phi^{1/2}/M), impossible for |v_l| < thr_l/2.  So only (W) carriers with own_l - |Y_l| in B_l can be bad —
an interval of length about Phi_l^{1/2} in the variable |Y_l|.  In configuration (i) the recursion of Lemma 4.1 never produces (W).

## 5.4 Lemma 5.4 (the recursion survives mixing unless a positive carrier is frustrated).  PROVED.
Run the forward recursion of Lemma 4.1 in a mixed class with the rule: a negative fine carrier takes varsigma := sgn Y (self-aligned, (R));
a positive fine carrier l takes varsigma := sgn Y_l and ANTI-aligned own coordinates z_j := -varsigma sgn u_l(j) on O(l).  Call the positive
carrier FRUSTRATED if |Y_l| < own_l + thr_l/2.  If no positive fine carrier is frustrated, the recursion defines z on J_fine at which
V is admissible on J_fine and every negative fine carrier is (R); hence (SC) for A_- holds (Lemma 4.3 / 5.3) and the class is recovered.
Proof.  For a non-frustrated positive carrier, v_l = varsigma (|Y_l| - own_l) with |v_l| >= thr_l/2, so |w(l)| >= M/2 with sign varsigma; its
coefficient -|Delta''| lambda_l w(l) has sign -varsigma and dominates on O(l) (Lemma 4.2 estimates), so sgn V_j = -varsigma sgn u_l(j) = z_j.
Negative carriers: Lemma 4.1.  Every j in J_fine has an owner (part 4).  QED
A frustrated positive carrier has NO consistent contact state: anti-aligned own coordinates give the wrong sign of v_l, aligned ones give
the wrong sign of V on O(l).  It must take a value of modulus < thr_l/2 with |w| small, which needs non-contact coordinates (|z_j| < 1,
forcing V_j = 0) or balanced cancellations among later carriers; these "zero cascades" couple the carrier to the future, and the negative
carriers downstream may be forced off (R).  This is the mechanism of the residual.

## 5.5 Toy evidence (numerics, U1_work/mixed_fixedpoint_check.py, mixed_forcedW_check.py, mixed_bad_inspect.py).  HEURISTIC.
Lexicographic model (the limit of super-decreasing weights: the first carrier with nonzero coefficient fixes sgn V_j; balanced tiny-w
states are NOT modelled), 7 carriers of random type N/P, two signature coordinates per carrier (own mass 0.05), later targets meeting
earlier signature coordinates with coefficients ~0.02-0.1, coarse offsets often 0 (frustration).  All 3^7 sign patterns are enumerated,
the free coordinates solved by LP.  Among 148 mixed instances: the forward recursion meets a frustrated positive carrier in 134; exact
completions (in the model) exist in 115; in 3 of these EVERY exact completion puts some negative carrier in (W) (forced wrong branch;
e.g. mixed_bad_inspect: carrier 0 negative with Y = 0.0445 < own = 0.05 is forced to v = -0.0055 by a frustrated positive carrier two
stages later); with a threshold band of relative width 0.08 one instance has NO good completion, with bands 10 and 100 times thinner
none.  Reading: forced (W) is structural in mixed classes, but a BAD (W) needs the coincidence own_l - |Y_l| in B_l, an interval of length
~ Phi_l^{1/2}, astronomically thin in the design (Phi_l^{1/2} <= c_l^{1/2}).  Earlier check (recursion_check2.py): with (W4'') enforced the
configuration-(i) recursion is admissible for every shift vector of the class (200 instances x 50 shift vectors), and violating (W4'')
breaks admissibility in 27% of the instances — (W4'') is necessary for Lemma 4.2, not an artifact.

## 5.6 MASTER THEOREM IV.  PROVED (modulo the refereed tools listed below).
Design D^{U1} (part 3: U4's T_final with the absorber clusters (A1), deep pairs (A2), rule (c''), weights (A4)/(W4''), Design(L) and Q(w)
enlarged by 4^{R_cl(L)}, 2^k, 1/eta_L and D_cls(w)), N fixed, diagonal base.  Let f in S_{p_N^*} have finite base support F.  Suppose that for
infinitely many main stages L some clean sub-window w of L has at least n(w)/D_cls(w) dyadic scales whose activity class (2.3) is
ONE-SIGNED (all active shifts of the same sign, or no active shift).  Then f in Rec: (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f).
Proof.  Fix such (L, w).  Pigeonhole over the D_cls(w) (class, cube) pairs (2.2(d)) gives a set S of >= n(w)/D_cls(w)^2 one-signed scales
with one class a and one cube; the sub-window length n(w) >= l 2^{l^3} Q(w) (as used in 2.6) and Q(w) >= D_cls(w)^2 (Design/u)^C (part 3
(A4)) give |S| >= l 2^{l^3} (Design/u)^C >= 48 rho^2 K/(c_flat (1 - rho^2)) with K = C_f (Design/u)^C, and K T_hi(w)/|S| -> 0, as Lemma
2.4 requires.  Build f^# by part 4: (1a) V1's moves and the realization of the Lojasiewicz point of Gamma^#(kappa, a) (Theorem
2.3: one kappa-push per block, Lemma 1.5 final form), (1b) zero-value tuning of the absorbers (Lemma 3.3), (1c) re-push / re-tune, (2)
the fine structure: configuration (i) the recursion (Lemmas 4.1, 4.2), configuration (ii) the Schauder completion (Lemma 4.4), A empty: no
shifted fine carriers (only the fixed owners).  At every t in S the data of Proposition 2.2(e) are exact two-piece data at f^# with the
common shift Delta''^* (Lemmas 4.6, 5.1; absorption on E_c by Proposition 3.4), they satisfy the size conditions of kinds [1]-[3] (V1 TR(iii),
Prop. 3.4(c)), p*(g - g_t) <= K t, kappa_w <= 1 + eta_0/2, and p*(f^# - f) <= theta_w T_lo(w)^2 with theta_w -> 0 (Lemma 4.5).  In
configuration (i), A_- = A satisfies (SC) at f^# (Lemma 4.3).  The windowed recovery (V2 Theorems E^>= / E^SC = Z3 Theorem E with V1's
banked/pulled supports, Theorem E''), run with the subset S (Lemma 2.4), along the infinitely many windows, gives (f, rho g) in cl NA for
every rho < 1, hence (f, g) in cl NA.  QED
Refereed tools used: V1 (Proposition TR, Lemmas TU, ST, CO, D, S, B; Theorem E''), V2 (Lemmas H, L, C5; Theorems E^>=, E^SC; Theorem B),
Z3 (Theorem E, Lemma U, Lemma 3.1), U4 (T_final, Lemma GW, Lemma W) and the note (lem:threshold, def:twopiece, thm:engineered, cor:D1,
lem:scrambling, def:SC, lem:switchbudget, lem:suplevel).

Corollary IV.1 (one block).  PROVED.  For N = 1 every activity class is one-signed; hence EVERY f in S_{p_1^*} with finite base support is
in Rec(p_1): Lemma Z holds at finite F for p_1 with the design D^{U1}.  (Clean sub-windows exist at every large main stage: V1/U4.)
Corollary IV.2 (structure of a counterexample, N >= 2).  PROVED.  If f (F finite) is not in Rec(p_N), then at every large main stage L and
every clean sub-window w of L, more than n(w)(1 - 1/D_cls(w)) scales carry MIXED classes: both a block with active negative shift (data
Delta d < 0) and a block with active positive shift.  By Lemma 5.4, at each such scale the forward recursion meets a frustrated positive
fine carrier.  [Transfer to Martin's p via lem:martintail is NOT claimed: the one-signed hypothesis is not N-independent.]
Corollary IV.3 (mixed classes without frustration).  PROVED.  The conclusion of Master Theorem IV also holds if the scales are counted
in classes that are one-signed OR mixed with no frustrated positive carrier in the forward recursion of Lemma 5.4.
Corollary IV.4 (intrinsic form).  PROVED (modulo V1 Lemma 3.4', refereed).  If for infinitely many main stages L some clean sub-window w
of L has I_up(w) = {} or I_lo(w) = {} (all source-deficient blocks lack the same source), then f in Rec(p_N).
Proof.  V1 Lemma 3.4': an upper source gives delta_m <= K_d t, a lower source gives delta_m >= -K_d t (decomposition convention delta_m =
Delta d_m M_m; data shift Delta'_dec,m = -delta_m, Prop. 2.2).  Hence a block with both sources has |Delta'_dec,m| <= K_d t; a block of
I_up(w) has a lower source (I_up ∩ I_lo = {}, V1 Lemma S(a)), so Delta'_dec,m <= K_d t: it can be large only NEGATIVELY; a block of I_lo(w)
has an upper source, so Delta'_dec,m >= -K_d t: it can be large only POSITIVELY.  The
projection (2.4(b)) moves components by <= K t, and components below A_1 K t = K_* K t > (K + K_d) t are set to 0 (2.3).  So at every scale
the active negative blocks lie in I_up(w) and the active positive blocks in I_lo(w); if one of these sets is empty every class of w is
one-signed, and Master Theorem IV applies with all n(w) scales.  QED
Remark (where the classes live).  Activity classes are assigned with the coefficients of f^(1a) (after V1's moves and the Lojasiewicz
realization of Theorem 2.3, which exactifies the minors of ALL classes simultaneously and is therefore class-independent); the fine
structure (2) is then built for the chosen class.  No circularity arises.

## 5.7 The precise remaining step (C_mix).  OPEN.
In a mixed class (A_- and A_+ nonempty) at a clean sub-window: find a point z in [-1,1]^{J_free} at which V is admissible on J_fine
(exists: Lemma 5.1) and no negative fine carrier is BAD (value in its threshold band B_l of length ~ Phi_l^{1/2}).  Equivalently (Lemma 5.2):
no negative fine carrier in the wrong branch (W) with own_l - |Y_l| in B_l.  Known: the property holds at every exact completion for the
negative carriers with |Y_l| >= own_l + thr_l (they are (R)); configuration (i) avoids (W) altogether; the toy model shows that mixing can
FORCE (W), and that BAD (W) then requires a coincidence of measure ~ Phi_l^{1/2}.  Natural routes: (a) a selection theorem among the
Schauder fixed points (Browder continuation from A_+-shift 0, where the recursion gives an all-(R) completion, to the actual shift); (b) a
genericity argument in finitely many coarse parameters (a measurable selection of completions plus transversality of Y_l); (c) U3's
violation tolerance (r8/U3_notes.md Lemma VT, Lemma QB2): run the recursion of Lemma 5.4 with frustrated positive carriers simply
anti-aligned; the resulting sign violations sit on their own sets, with l_1-mass <= C_f sum_{l > L} lambda_l own_l <= C_f c_{L+1} (fine
origin), exactly the violations U3's (S2) is designed to tolerate — so (C_mix) is implied by U3's open step (S2) (SKETCH of the reduction).

## 5.8 Corrections to earlier rounds (recorded).
 - V2's "near-coordinate conversion" (SKETCH in V2 4.3) is FALSE as stated for super-decreasing signature weights: free signs on the near
   coordinates of a signature set cannot reproduce the original value up to the far tail (the achievable signed sums form a Cantor set;
   the discrepancy is of the order of the first converted weight).  Replaced by zero-value absorbers (part 3).
 - V2's gap (C*-3) asked for INDEPENDENT exactification of theta_m and A_m: unnecessary — only kappa_m enters (Lemma 1.3); one push per
   block suffices (Lemma 1.5), and the buffer peak always works once Omega contains all coarse strict non-peaks.
 - Part 4 (this round): tuned absorbers that are not used must carry a positive switching coefficient c_0(a) (not 0), otherwise the far
   parts of their signature sets, fixed at +1, are not protected.
 - recursion_check.py (first version) violated (W4''); the corrected toy confirms Lemma 4.2 and the necessity of (W4'').
