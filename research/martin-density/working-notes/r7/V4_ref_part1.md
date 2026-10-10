# V4 referee, part 1: Sections 2-4 of V4_notes (Lemmas 1.1-1.3, requirements table, Lemma 2.1, Theorem 2.2, Remark 2.3, Prop. 2.4)

Checked against: note lem:threshold (+ eq:margin), def:twopiece, prop:onesidedupper, thm:onesided, def:SC (+ remark after it),
thm:engineered, cor:D1, cor:BTrecovered, def:SLD / thm:SLD ((D0)-(D2), (P1)-(P3)), lem:budget, lem:suplevel, lem:box,
lem:switchbudget, lem:peakshift (eq:peakshift, eq:didentity), def:swallowed, lem:modswallow, lem:badpeaks; Z4-ref (H2'') and
Remark 3.3; Y2 Lemma 5.1, Prop. 5.2, 5.3; Y4-ref; V1/V2 referee reports (this round).

## 1.1 Lemma 1.1 (value formula).  CORRECT.
u_l(zhat) = u_l(z) + <U^* u_l, e>, U^* u_l = sum_j u_l(j) s_j kappa_j, e = sum_i a_i s_i kappa_i/nu, so <U^* u_l, e> = sum_{j in F} s_j^2 u_l(j) a_j/nu.
Split u_l = (y_l + delta_l h_l)/n_l.  The swallowed form follows.  (Remark: |val_l| <= q*(u_l) = 1 for every l, since
|u(z + Ue)| <= ||u||_1 + ||U^* u||; V4 uses the weaker 1 + ||U||, harmless.)

## 1.2 Lemma 1.2 (forced sharing).  CORRECT.
(a) As S_{q*} has no isolated points, (T-d) gives k_i -> infinity with q*(u_{k_i,m} - e_j^*/q*(e_j^*)) -> 0, hence
u_{k_i,m}(j) -> 1/q*(e_j^*) != 0 along that subsequence (V4 writes "u_{k,m}(j) -> ...", read: along a subsequence).  (b) at most one
carrier has j in its signature set; for the others u_l(j) = y_l(j)/n_l.  The consequence (no design makes target supports of two
blocks disjoint) is correct.  PRECISION: a link between blocks can also occur through j in S_{l_1} ∩ supp y_{l_2} (l_2 > l_1,
allowedness (b)); V4's (B-ii) mentions only supp y_{l_1} ∩ supp y_{l_2}.  Irrelevant for the conclusion.

## 1.3 Lemma 1.3 (shift fed by negative d-weights).  CORRECT, one fixable imprecision.
Re-derivation.  eq:didentity: Delta d M = (1/(mC)) sum_k Phi_k w(k) Delta theta_k + r, |r| <= 2t/sigma.  Good carriers: modulus
<= K* t/(mC) (Phi|w| <= 1); fine carriers (l > l_*): <= 6 t^2/(mC) (lem:modswallow(a), uses t in W(l_*)); coarse swallowed l:
Phi w Delta theta/(mC) = -q_l tau_l (tau_l = -eps_l Delta theta_l).  At a swallowing-type swallowed peak, eq:peakshift with
Delta Theta(k) = -eps_l tau_l/lambda_l and varsigma_k = eps_l gives tau_l/lambda_l - Delta d M = e_k >= 0, and q_l = Phi M/(mC) > 0, so
-q_l tau_l <= -q_l lambda_l Delta d M.  Elsewhere -q_l tau_l <= |q_l|(tau_l)_+ (q_l < 0; this includes ANTI-sign swallowed peaks, for
which |q_l| = Phi M/(mC) and eq:peakshift gives tau_l <= -lambda_l Delta d M) and <= q_l (tau_l)_- (q_l > 0).  The display follows.
IMPRECISION (fix): the second consequence ("the free shift at scale t is at most (6M/(Ct)) sum_{q_l<0} Phi_l^2 + C(K*+1)t/C_m")
silently drops the term sum_{l in B, q_l > 0, l notin Pk} q_l (tau_l)_-.  It is absorbed only under a bound on the negative parts
(lem:modswallow(b) under (H1): sum (tau_l)_- <= K* t; or Z4's D_-).  Without such a bound the correct statement is
   Delta d_m M_m <= (6 M_m/(C_m t)) sum_{l in B, l <= l_*, l notin Pk} Phi_l^2 + C(K* + 1) t/C_m
(both signs of q at strict non-peaks, using |q_l| <= Phi_l M/(mC) and the box (tau_l)_+-, (tau_l)_- <= 6 lambda_l/t).  The qualitative
reading ("a large shift needs swallowed carriers with Phi_l >> t") is unaffected; the claim "fed ONLY by negative d-weights" needs (H1)
or the D_- bound.

## 1.4 Requirements table.  CORRECT as a classification; its force rests on the realizability results.
The DO/FR split is a bookkeeping device, not a theorem: an FR system CAN be made unsolvable by a design (V4's own Lemma 3.4: under
(GM) a swallowed carrier whose target coordinates are all contacts is a robust peak beyond an f-dependent level; so "near-threshold
carriers tuned only through contacts" is an FR configuration that a design excludes).  Hence "no DO relation" does not by itself
show that (C), (D) cannot be designed away; that is what Theorem 2.2 / Remark 2.3(1) prove (for (C) fully, for (D) only in the weak
form, see 1.7).  For (B) the realizability is only the SKETCH of Remark 2.3(2), so "(B) cannot be excluded by design" is SKETCH-level.
Moreover (B) is no longer a residual of the method for D^{V2} (V2 Theorem B, refereed correct this round), so the design question
for (B) is moot.  The table's (E) entry is checked in part 2 (Lemma 2.6).

## 1.5 Lemma 2.1 (designability).  CORRECT, with a precision on the order of choices.
(SF*) second half, (b') and "Phi_l <= g_l 2^{-l}" are upper bounds on c_l in terms of S_l, delta_l, y_l and earlier data; (SF*) first half
is an upper bound on c_{l+1} (and all later weights, using c_{l''+1} <= c_{l''}/4: sum_{l''>l} lambda_{l''} <= c_{l+1}/3) in terms of level-l
data.  PRECISION: in def:SLD (D1) the weight c_l is fixed BEFORE y_l (y_l is the target y^(i_{k(l)}) if it is allowed at the current
c_l).  (GM) and eta_l depend on y_l and delta_l, so V4's recursion must be (as V4 says) S_l, delta_l (with the (GM) avoidance), y_l by
allowedness (a) only, THEN c_l := min of all upper bounds (allowedness (b), (b'), (SF*) second half, (GM), the design's own window
bound such as T_lo(l-1)^3), then the level-l window/Design constants.  In this order allowedness (b) is always satisfiable, so the
target rule uses y^(i_{k(l)}) whenever (a) holds; (T-d) holds a fortiori.  I checked that no result of Section 8 or Rounds 5-7 uses a
LOWER bound on c_l (V2's referee: "no lower bound on b(w) is used anywhere"; windows depend on delta°, Lambda°, Design(l), all computed
after c_l in the modified order).  Changing delta_l within [delta^max_l/2, delta^max_l] changes Lambda°(l) and delta_min(l) by factors <= 2,
recomputed by the recursion.  (Z0): all designs used have an infinite complement of union S_l (SLD: j_0; D_Omega: the odd numbers).
(FD): fresh coordinates j in Z_0 exist at every stage (finitely many coordinates are in earlier target supports); the extra targets
must be interleaved so that every original target still occurs infinitely often in every block.  N-independence: all conditions are
stated over the full ladder.  So Lemma 2.1 is PROVED once the modified recursion order is written out.

## 1.6 Theorem 2.2 (self-aligned rows).  CORRECT (all of (a)-(g)), re-derived step by step.
Step 1: y*(zhat_F) = c*(s_p^2 a_p - s_{p'}^2 a_{p'})/nu; with r = a_p/a_{p'} this is c*(s_p^2 r - s_{p'}^2)/(s_p^2 r^2 + s_{p'}^2)^{1/2}, continuous,
-> -c* s_{p'} (r -> 0) and -> c* s_p (r -> infinity): IVT.  Order of choices: l_c, theta_0 (design), then l_- (late), then eta, then the ratio.
Recursion well defined: supp y_l ⊂ (union_{l'<l} S_{l'}) ∪ Z_0 by allowedness (a), S_{l'} (l' < l) fully assigned at step l', so the
unassigned coordinates of supp y_l lie in Z_0 \ F; every coordinate is assigned (Lemma 1.2(b) for Z_0, step l for S_l).
Step 2: n_l val_l = A_l + eps_l(B_l + delta_l H_l) with eps_l A_l = |A_l|: correct.  Step 3: A(th) >= ||zeta||_1 - th sum Phi^2,
sum_k Phi_m(k)^2 <= 1/12; B(th) <= th ||zeta||_1; Psi(||zeta||_1/2) >= (49/64 - 1/2)||zeta||_1^2 > 0, so theta_m > ||zeta||_1/2: correct (Psi is
strictly decreasing where A > 0; Lemma T).  Step 4: Phi_l/Phi_k <= c_l/c_{l-1} <= (5/4)|val_l| 2^{-l-10}/(1+||U||) (H_l >= 2^{-min S_l},
n_l <= 5/4), so coarser terms vanish at th = nu_l; finer terms <= (1+||U||) sum_{l''>l} lambda_{l''} <= 2^{-10} lambda_l |val_l|.  Hence
A(nu_l) <= 2^{-10} lambda_l |val_l| < m|val_l| <= B(nu_l)^{1/2} (V4 writes "=" for the last relation; it is ">=" via the l-term alone,
which is what is needed).  Peak with nu_l > theta_m; swallowing type since sgn w = sgn val = eps_l.  nu_l >= 2^{10} m(1+||U||)/Phi_{l_1} >
2^{10} theta_m for l after the first carrier l_1 of its block, mu_l >= q_0 |val_l|(1 - 2^{-10}) >= q_0 delta°_l/2.  (l_- is not the first
carrier of block m_0: it is chosen late.)  Step 5: nu_{l_-} < theta_0/2 < theta_m/2, gap = C(theta - nu)/|zeta| >= M/2; w(k_-) has the sign of
val_{l_-} < 0, eps_{l_-} = +1: q_{l_-} < 0.  Step 6 (dominance): re-derived all three cases: (i) ratio <= (4/3)2^{-6-min S_o}; (ii) via
allowedness (b): later total <= (2/9) 2^{-2j} c_o delta_o vs lambda_o v_o(j) >= (4/5)2^{-m-k} c_o delta_o 2^{-j}, ratio <= (5/18)2^{m+k-j} <
2^{-6}; (iii) (SF*) gives ratio <= (4/3)2^{-10}.  In case j notin S_o, j is unassigned at step o (o is the first carrier with u_o(j) != 0)
and j notin S_{l'} for l' >= o (allowedness (a)).  Partial sums contain the owner term or vanish at j; weights in [1/2, 1] at most
double the ratio.  Step 7 ((e)): all carriers are bad (room 0), block m_0 has only swallowing-type peaks and l_- with q < 0: UPPER of
(H2'') fails (Z4-ref Remark 3.3); the other blocks satisfy both halves (all their swallowed carriers have q > 0).  So I_up = {m_0},
delta = 1, and with x_{l'} := lambda_{l'} the vector Pi_{m_0} + sum x eps u is the partial sum W^(l) (all carriers <= l), z-signed with no
free coordinate: c(1; l) = 0, i.e. c_*(l) = 0 for EVERY l (not only l >= l_-).  Step 8: correct; carriers counted in Scr_m(Upsilon s)
satisfy q_0 delta°_l/2 <= Upsilon s, hence Phi_l <= (5/4) c_{l-1} delta°_l 2^{-l-10} <= c_{l-1} 2^{-l} Upsilon s/q_0, and the count starts at
l(s) -> infinity: o(s).  (MS) the same.  (g) by construction.
SCOPE REMARK.  (e) is configuration (C) in Y2's sense (c_* = 0).  The current residual (C*) (V2-ref) is "rho^sh <= b(w) AND V1's
c_pi(w) <= b(w) at every clean sub-window of all large levels" (rate objects of D^{V2}/D_Omega).  Theorem 2.2 does not check those;
it is plausible (exact coherence gives c_pi = 0 at the pattern level) but not claimed, and it does not matter since f_SA is (BT).

## 1.7 Remark 2.3(1) (weak-peak aligned corner).  Statement plausible; PROOF HAS A GAP (fixable).
The proof argues: theta jumps only at owner-rule sign switches; "coarse switches are finitely many in a small range and fine ones move
theta by <= C sum_{l>L} lambda_l; hence every relative margin xi in (0, xi_0) is attained up to an arbitrarily small error".
GAP.  To move the relative margin of l_D over (0, xi_0) the parameter must sweep val_{l_D} over a range ~ xi_0 theta Phi_{l_D}/m.  With the
PURE owner rule, a carrier l < l_D switches as soon as A_l crosses 0, and nothing prevents |A_l| (a row-dependent number) from being
smaller than this range for some of the l_D - 1 coarser carriers (targets meeting F accumulate at every value by density); a coarse
switch moves theta by up to L_Theta * 2 lambda_l, which can be much larger than xi_0 theta.  "Finitely many coarse switches in a small
range" does not give a switch-free sweep of the required length, because the required length and the set of coarser carriers both
depend on l_D.
FIX (proved in V4_ref_notes, Lemma R1).  Use the HYSTERETIC owner rule (the one V4 itself uses in Prop. 5.3 / Lemma 4.4): fix the
reference signs at the base point, flip eps_l only when eps_l A_l <= -(B_l + delta_l H_l)/2.  A forced flip at l needs A_l to move by
>= delta_l H_l/2, while along the sweep A_l moves by <= ||y_l 1_F||_1 (1 + max_F s_j^2) |Delta b| with |Delta b| = O(theta Phi_{l_D}); by
(SF*) (Phi_{l_D} <= c_{l_D} << delta_l H_l for l < l_D, uniformly), no carrier l < l_D flips, and the jumps of theta from flips of
carriers l > l_D total at most C sum_{l > l_D} lambda_l (each flip of l moves zeta by <= 2(1+||U||) sum_{l' >= l} lambda_{l'}, and a flip of l
needs delta_l H_l/2 <= C |Delta b|, so only carriers with delta_l H_l <= C theta Phi_{l_D} flip, finitely often each).  Every re-run
carrier keeps n_l|val_l| >= (B_l + delta_l H_l)/2 (robust swallowing-type peak, margin >= q_0 delta°_l/4), W stays z-signed (Step 6 uses only
z_j = eps_o sgn u_o(j) at owner coordinates), l_- stays tuned (its value depends only on zhat_F, which a 4-point F lets one keep fixed),
and the relative margin of l_D is an "epsilon'-almost continuous" function of the sweep parameter that changes sign; so every
xi in (0, xi_0) is attained up to epsilon' = C L_Theta sum_{l > l_D} lambda_l/theta.  The resulting rows are hysteretic-self-aligned rather
than "pure" owner-rule rows; they have the same structure ((C) with exact coherence, all peaks swallowing type, l_- with q < 0).
V4 correctly labels EXACT degeneracy in pure form OPEN.  Note: V1's Corollary AC (refereed correct) already shows that the aligned
corner is not a residual for D_Omega, so Remark 2.3(1) only illustrates that the configuration exists.

## 1.8 Remark 2.3(2) ((B) core).  SKETCH, plausible; moot.
Needs N >= 2, design targets of two blocks supported in F ∪ {j} (available after Lemma 2.1-type additions), a free link coordinate
(z_j := 0; later carriers through j are still robust peaks under the (hysteretic) owner rule since their A_l only loses one term), four
switchable carriers for TWO rays meeting both blocks, and tuning of their values to make the 2 x 2 d-determinant tiny (the entries are
linear in the values, Lemma 4.5).  Not written out; superseded by V2 Theorem B (tiny minors are exactified by Lojasiewicz at a cheap
companion), so (B) is not a residual for D^{V2}.

## 1.9 Proposition 2.4 (single-vector principle).  FALSE AS STATED; trivially fixable.
Counterexample to the literal statement: V_1(j) = 10, V_2(j) = -1, V_i(j) = 0 (i >= 3).  i(j) = 2 satisfies |V_2(j)| = 1 > 2 sum_{i>2}|V_i(j)| = 0,
z_j := sgn V_2(j) = -1, but the partial sum V_1 + V_2 = 9 at j is not z-signed.  The hypothesis controls only LATER indices; earlier
nonzero entries are not controlled.  FIX: take i(j) := the FIRST index with V_i(j) != 0 (the "owner", as in Step 6) and require
|V_{i(j)}(j)| > sum_{i > i(j)} |V_i(j)| (factor 1 suffices; factor 2 also covers weights in [1/2, 1]).  Then every partial sum with
n >= i(j) has the sign of V_{i(j)}(j) at j, and vanishes for n < i(j).  The interpretive sentence ("a design can defeat one z-signing
only by destroying dominance") is HEURISTIC.
