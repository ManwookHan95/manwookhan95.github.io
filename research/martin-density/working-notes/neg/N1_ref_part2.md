# N1 referee, part 2: Sections 2-3 of N1_notes.md (necessary conditions, mechanisms, verdict)

Sources re-read for this part: Part I def:twopiece, def:BT, prop:onesidedupper, thm:onesided, def:SC, thm:engineered,
cor:D1, cor:BTrecovered, cor:exampleRecovered, rem:withoutSC, thm:averaging, cor:ladder, cor:decomposition, prop:intrinsic,
thm:transfer, prop:exact, cor:twosided, rem:resonancetypes, end of sec:status; Part II thm:II-ERT, thm:II-E, cor:II-S2,
prop:II-S3, thm:II-NL, thm:II-N, thm:II-raised, thm:II-flipext, thm:II-transferinf; G3 Section 2 (Lemmas 1.1-1.4,
Cor 1.3, Theorem CL) and G3_referee.md; N2 (r2) 3.1-3.4; R3_notes 5.1 and R3_referee.md; U3_notes summary and U3_referee.

## 2.0 / 2.1: F1-F7 -- CORRECT (with precision P-11)
F1 prop:reduction(d). F2: Fort's theorem (usc compact-valued map from the complete metric space S* into the separable
metric space l_1: lsc points are residual) or rem:joint; at an lsc point every NA sequence recovers C(f). F3: matches
def:BT and cor:BTrecovered (I finite). F4: thm:II-N is stated for arbitrary admissible T and every N; hypotheses quoted
correctly. F5: re-derived from Thm 1.3(iv) (if f'' is recoverable and p*(f''-f) < delta'/2, every h'' in C(f'') with
p*(h''-rho g) < delta'/2 would be in Rec(f'')). F6: Lemma 2.1(b). F7: Part III as cited.
P-11 (F6 quantifiers): the contrapositive of thm:transitivity is "there is rho' < 1 such that NO sequence of recoverable
rows f_n -> f satisfies liminf_n r~_{f_n}(x) >= rho' r~_f(x) on a dense set of x"; the parenthesis "(all rho' < 1)" in N1
reads as the opposite quantifier. Content otherwise correct (the sharp form via Lemma 2.1(b) is right).

## 2.2: M1-M8
M1 CORRECT. U(f) contains cl Cert^sh(f) (thm:shifted) and therefore all classes listed (prop:intrinsic(a) says the mates
of cor:check, cor:ladder, thm:weighted, thm:locsplit, thm:carriers lie in cl Cert(f)).
M2 CORRECT AS A CONTRAPOSITIVE, but the displayed statement needs precise quantifiers (P-6): "component norms <= s(tau)
+ o(tau^2)" at a single scale t is meaningless. Precise form (PROVED): for all c_0 > 0, kappa_1, K < infinity there are
eta > 0 and arbitrarily small t > 0 such that for neither tau = t nor tau = -t does f + tau g admit a decomposition of the
displayed form with r(c_t) >= c_0 t, kappa(c_t) <= kappa_1, p*(e_t) <= K t and all component norms <= s(tau) + eta tau^2.
Proof: let A(t) be the infimum over admissible decompositions (both sides) of [max component norm - s(tau)]. If
limsup_{t->0} A(t)/t^2 <= 0, near-optimal choices (excess <= max(A(t),0) + t^3) satisfy the hypotheses of
cor:decomposition, so g in cl Cert(f) subset Rec(f). Hence for a counterexample limsup A(t)/t^2 =: 2 eta > 0. QED
The READING after M2 (list of resources) is HEURISTIC (it interprets the certificate format), not part of the claim.
M3 CORRECT. Can be sharpened: rho g notin K(f) (K(f) subset Li along the canonical truncations, which are NA rows), and
g notin K(f) follows since K(f) is convex and contains 0.
M4 CORRECT as stated (contrapositive of thm:engineered / cor:D1 for F finite; thm:II-raised, thm:II-flipext for F
infinite); it can be sharpened to "no data with rho^2 kappa_w < 1 and (Delta d >= 0 or (SC))" for the given rho.
The gloss "Hence ... the dangerous mate must exploit the failure of (BT): its one-sided decompositions need infinitely
many carriers, degenerate or near-threshold carriers, or flips of an infinite support" is NOT a consequence: see E-1.
M5 CORRECT (contrapositive of thm:II-E / thm:II-ERT).
M6 first two sentences CORRECT (cor:twosided; prop:exact applied to the averaged decomposition, D = B_+ - B_- in
L*(V*) subset Y; Y cap c_00 = {0} forces F u K infinite for exact switching; cor:II-S2 at rows with F, K finite).
ERROR E-1 (M6 last sentence, M4 gloss, Section 0 (2), table rows M4/M6): "So the switching of the dangerous mate must be
scale-dependent ('approximate resonance') or not of two-piece type" is NOT PROVED. Exact (scale-free) two-piece data are
known to be recovered only when kappa_w <= 1 (or rho^2 kappa_w < 1 for the given rho) AND (Delta d_m >= 0 for all m, or
I_- := {m : Delta d_m < 0} satisfies (SC)) [thm:engineered]; d-neutral data are the special case Delta d = 0. Exact data
with Delta d_m < 0 on blocks failing (SC), or with rho^2 kappa_w >= 1 for every choice of data, are NOT known to be
recovered (rem:withoutSC(b) states this explicitly). N1's own candidate C1 (Section 3.4) is exactly of this kind, so the
notes are internally inconsistent. Corrected statement (PROVED, contrapositive of thm:engineered, I and F finite):
a dangerous mate g (rho g notin Rec(f)) satisfies one of
 (i) g has no two-piece data with rho^2 kappa_w < 1 (in particular: no exact one-sided representation with finitely many
     carriers, no base mass on free coordinates and Gamma_w < rho^{-2} on both sides), or
 (ii) every two-piece datum of g with rho^2 kappa_w < 1 has Delta d_m < 0 on a set of blocks I_- that fails (SC).
Only in case (i) is the switching "genuinely scale-dependent or not of two-piece type". Case (ii) has exact, scale-free,
finitely carried switching.
M7 CORRECT. Re-derived Lemma 1.1 (weighted budget, uses q_0 + sum sigma_m = 1 and g(xi) = 0), Lemma 1.2, Cor 1.3, Lemma
1.4(a),(c) (summed: sum_{j notin F}(z_j V_j)_- <= t/(2q_0), sum_{j notin F}(1-|z_j|)|V_j| <= t/q_0), (CL0) |V(zhat)| <= t/q_0
and (CL2). V = L*(Theta_- - Theta_+) in Y. These are universal (any row, mate, scale), as N1 says; G3's referee confirmed them.
M8 CORRECT as cited (rem:resonancetypes: sgn w_m(k) = sgn u_{k,m}(xi) is proved; the "cannot switch" conclusion is the
P1 sign rule for exact or o(Phi)-perturbed duplicates; Part I calls the general statement a heuristic guide) -- the
label "PROVED (P1) / HEURISTIC guide (Part I)" is accurate.

## 2.3-2.4 (T1-T3, S1-S2)
T1, T3: HEURISTIC/SKETCH labels accurate.
ERROR E-2 (T2, Section 3.3(iv), (Q-a)): N1 states, following R3_notes, that error carrying (R3 Theorem EC) removes the
model-level boundary excess for compact error directions ("R3: R -> 1"), hence that a counterexample needs ESCAPING
(non-compact) errors (R1) at every boundary, and lists "E's rigid design for compact errors" among the explicit
candidates that were recovered. This ignores the refereed status of R3 (r3/R3_referee.md, "Main finding"): EC removes
only the ERROR-driven conversion requirement; a rho-independent HILBERT/ROOM-capacity requirement on the converted
carriers remains. In R3's own Model N with EC and one converted carrier: R = 1.463 (A = 0.5), 2.074 (A = 0.25),
1.086 (A = 1, B = 0.6), with the maximum at the bottom scale and NO improvement as tau_gen grows; "one converted carrier /
one global scalar suffices" is FALSE in general; converting BOTH types (two group scalars, E 4.4) gave R = 1.000 in the
real-norm-like variant. The referee added (R6) to O3*: conversion capacity below the Hilbert/room requirement at every
boundary, EVEN WHEN ALL ERRORS ARE COMPACT. Consequences for N1:
 - (T2): (R1) is not a necessary condition even heuristically; the class is O3* with (R6) as an ALTERNATIVE route:
   [(R1)-(R5)] OR [(R6): bounded two-type conversion capacity below the room/Hilbert load].
 - 3.3(iv): "So the obstruction must ALSO make the errors at every junction escape to infinity" is unsupported; delete,
   or replace by "or keep the room/Hilbert capacity of converted carriers of at least one type bounded (R6)".
 - (Q-a): "E's rigid design" must move from "recovered" to "OPEN (SKETCH with two gaps: (HT-EC) and the capacity gap)".
For the negative track this correction matters: (R6) is the one place where refereed model-level evidence shows a bounded,
scale-independent deficit of a specific mechanism; it is a better-founded target than escaping errors.
S1: "PROVED (as a reformulation)" overstates a vague sentence (P-7). What is proved: by Thm 1.3(iii) and Lemma 1.4 (and
1.4'), for every delta there are W, eta such that the defect persists at every NA row whose data agree with f's up to eta
on [1, W], whatever the data beyond W. "It cannot be carried by finitely many coordinates" is HEURISTIC (a type (I) test
vector x may well lie in c_00; what cannot be finitely carried is the REASON for cheapness at all admissible normers).
S2: labels accurate.

## Section 3
3.1 table: accurate as a catalogue (each entry cited). Row 11 ("banks ... anywhere"): see P-1b (banks at fixed free
coordinates are impossible near f; banks live at contacts/near-contacts with the contact sign, or escape to infinity).
3.2 (P-a), (P-b), (P-d), (P-e): CORRECT as cited. (P-c): N2 Lemma 3.3 re-derived (zhat notin c_0, x' in c_0 \ {0} are
independent in l_inf, so some y in S_{q*} has y(zhat) > 0 > y(x'); the dense tail of (u_{k,m})_k and Fact C make infinitely
many k common peaks of opposite signs; this holds for EVERY NA row, not only near f). N1 correctly restricts N2 Cor 3.4 to the
transferred decompositions of N2 3.1.
(Q-a): see E-2; also P-8: for the nested-tuning rows U3 proves recovery only of their exact-data mates (Cor NT-R; general mate
reduced to (S1)/(S2)); full recovery holds for T_fin through Master Theorem VI (finite F), not through U3.
(Q-b), (Q-c), (N-a), (N-b): accurate.
3.3 (i)-(iii): labels accurate; (iii) "banks" subject to P-1b.
3.4 C1: HEURISTIC, correctly labelled OPEN. Referee additions (HEURISTIC):
 (e5) Footprint compensation. The Hilbert footprint of window masses changes zhat' = z' + U e' by U(Delta e) = O(s_1).
      On FREE coordinates of the window it can be cancelled exactly by the O(s_1) move z'_j := z_j - (U Delta e)_j (allowed
      by Lemma 1.4 since O(s_1) < eta), and on contacts in the inward direction; only the footprint on F u K (and on contacts
      needing an outward move) survives. So C1's status-scrambling mechanism needs zero-weight carriers whose vectors carry
      O(1) relative mass on F u K at every depth -- an additional adversarial requirement on T.
 (e6) Non-uniqueness of data. A non-(BT) row may carry several two-piece data for the same g; C1 needs EVERY datum with
      rho^2 kappa_w < 1 to have Delta d < 0 on a non-(SC) block (case (ii) of E-1), which is not addressed.
 (e2) caveat: ||U* e_j*|| -> 0 for every compact U, so far contacts always have small footprint; the adversary can only make
      the footprint of the COARSE window contacts (fixed by g) large.
3.3/3.5 verdict: HEURISTIC; the recommendation (targeted, not wholesale, negative test) is reasonable. Two corrections:
 - 3.5(2) "for ARBITRARY T ... bottleneck is EXACTNESS": for arbitrary T the exactness bottleneck is that of the designed-T
   programme; for arbitrary T almost nothing beyond Parts I-II applies and the open core is the Round-2 core
   (approximate resonances, non-(BT) rows, Delta d < 0 without (SC), Gamma_w > 1, infinite F) plus (R6) (P-10).
 - Remark 1.10(II): "(II) is the precise form of the gap noted at the end of [I, sec:status]" is inaccurate (P-12): that gap
   is whether density forces ONE NA sequence recovering the whole fibre (C(f) in A(f)); (II) is non-convexity of Rec(f).
   Precise relation (referee Lemma R-M, PROVED in N1_ref_notes): finite merging at f <=> Rec(f) in A(f) => Rec(f) convex;
   under density, Rec(f) in A(f) for all f <=> cor:finite(a) for all f (the Part I gap).

## Section 4 (numerics)
Re-ran both scripts; outputs as reported (twopoint: LP <= two-point bound in all 6 cases; angle: max ratio 0.187).
Referee script N1_ref_work/ref_checks.py: Prop 1.5(a) exhaustive rank-one search in the Euclidean model (max ratio 0.49),
slack inequality on a fine grid, Prop 1.8 end-to-end (2000 cases, 0 failures). All consistent; as N1 says, no
finite-dimensional model can test non-density.
