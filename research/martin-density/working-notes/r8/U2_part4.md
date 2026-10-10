# U2 part 4: items (E3) and (E4)

Setting as in parts 1-3 (T_final^* or SLD^star, finite I, F arbitrary).

## 4.1 (E3) non-d-neutral data at raised rows
(a) PROVED (structural).  In Theorems RS*, RS*_inf and in the transport M-inf (outside (C*)), all window data are constructed AT the
companion (deep-raised and, for M-inf, exactified) from two-sided decompositions at that companion, and they are d-neutral because the
exact cones contain the d-rows (R1 Step 2, Lemma W, V1 Prop. TR / V2 Cor. B.1).  Hence Y3 Theorem 2.1 is applied with I_- = {} and no
scrambling condition (SC) is ever needed at a raised row.  (This is where V3's Theorem A route differs: there FIXED data from f are
transported to the raised row.)
(b) Obstruction for transported fixed data.  Let (b^+-, omega^+-) be two-piece data at f with consistency vector
Delta := sum_m Delta d_m R_m^* w_m != 0, and let f' be a row obtained from f by a move on F that changes e (a raise or a lowering).  The same
pairs represent at f' two functionals whose difference is D := Delta' - Delta, Delta' := sum_m Delta d'_m R_m^* w'_m.  PROVED: D lies in the
operator range Y, so D != 0 forces D to have infinite support (Y cap c_00 = {0}), and D != 0 as soon as sum_m Delta d'_m w'_m != sum_m Delta d_m w_m
(L^* injective); D = O(|Delta d| eps_e) in l_1.  Re-representing at f' (moving D into b^-) violates side-admissibility (b = 0 on J,
z-signs on K) at first order whenever supp D meets a free coordinate or a contact with the wrong sign -- HEURISTIC that this is the generic
situation (it is if, e.g., F^c contains a free coordinate where D does not vanish); exact data then cannot simply be transported.  This is
the precise content of V3 4.1 Remark.
(c) Reduction.  Non-d-neutral data are needed only in V2's treatment of coherent shift resonance (shifted data, Theorems E^>=, E^SC),
i.e. inside the residual (C*).  Data with Delta d_m >= 0 in all blocks need no (SC) (Y3 Theorem 2.1 with I_- = {} works at any F).  For
Delta d_m < 0 the requirement is (SC) at the companion for the blocks of I_-.  (SC) (def:SC) is a property of the block data only
(margins of peaks, gaps of strict non-peaks), not of F; the remark after def:SC shows that block-tame blocks (Q_m finite, no degenerate
peaks, (MS)) satisfy (SC) at every F.  So at infinite F the (SC) requirement is exactly V2's gap (C*-2) at finite F (manufacturing (SC) at
companions, as V4 Theorem 5.6 does at (BT) rows), with the deep raise adding only an O(eps_e) perturbation of the block data, eps_e <= b^2
(Lemma DR-inf): a block whose companion is block-tame in the sense of Y3 4.1 (F arbitrary) satisfies (SC).  (E3) therefore adds nothing to
(C*) beyond the requirement that the block-taming constructions of V4 work at rows with infinite support, which they do as far as they act
on z off F and on values (they never use F finite except through (BT)'s "F finite", which Y3's block-tame notion drops).  SKETCH for the
last sentence (V4's constructions were not re-run at infinite F).
(d) OPEN, not needed: Theorem A (fixed data) with non-d-neutral data at mu-thin supports (raises break exactness by (b); without a raise,
(CS-side) fails on the thin part).

## 4.2 (E4)(i) failure of (ND'): it cannot coexist with a need to raise
Recall V3's Remark to Lemma VP and V3-ref Section 2: for a finite set L_0 of carriers, the value-change map of moves on F has range
V_1^perp, V_1 := {c in R^{L_0} : sum c_k u_k|_F in R a|_F}; (ND'_{L_0}) says V_1 = V_0 := {c : sum c_k u_k|_F = 0}.  For c in V_1 \ V_0 with
sum c_k u_k|_F = kappa a|_F (kappa != 0), every move on F changes sum c_k val_k by exactly -kappa nu ||e' - e||^2/2 (second order, one sign).
Lemma ND (structure of (ND') failure).  PROVED (any SLD-type T, any F).  Let L_0 be a finite set of carriers, T_0 := union_{k in L_0} supp y_k
(finite), and suppose c in V_1 \ V_0, sum_{L_0} c_k u_k|_F = kappa a|_F with kappa != 0.  Then
  F \ T_0  is contained in  union {S_k : k in L_0, c_k != 0},   and   a_s = (c_k/kappa) v_k(s)  for s in S_k cap F \ T_0.
Proof.  Let s in F \ T_0.  If s lies in no S_k with k in L_0, then u_k(s) = 0 for every k in L_0 (signature sets of L_0 miss s, targets of
L_0 miss s), so kappa a_s = 0, contradicting s in F.  If s in S_k, k in L_0, then u_{k'}(s) = 0 for k' in L_0 \ {k} (disjoint signature sets,
targets in T_0) and u_k(s) = v_k(s) (P1), so kappa a_s = c_k v_k(s); a_s != 0 forces c_k != 0.  QED
Theorem ND' ((ND') is not needed in RS*).  PROVED.  Theorem RS* (part 1.3) holds without the hypothesis (ND'_{B_np}): for SLD^star and
every N, every f in S_{p_N*} (F arbitrary) satisfying (W*), (H2), (H3-inf), (B_fin) belongs to Rec.
Proof.  If (ND'_{B_np}) holds, this is part 1.3.  Otherwise Lemma ND with L_0 := B_np gives F \ T_B' subset union_{c_k != 0} S_k (T_B' :=
targets of B_np, contained in T_B) and |a_s| = |c_k/kappa| v_k(s) there.  For s in F \ T_B and l in B: u_l(s) = 0 unless s in S_l (bad targets
lie in T_B), so U_B(s) = v_k(s) for the unique k with s in S_k, whence |u_l(s)|/|a_s| <= max_{c_k != 0} |kappa/c_k| on F \ T_B; on the
finite set F cap T_B the ratio is finite.  So R1's (H4-inf) holds, hence (CS_B) (Z5-ref Lemma R0(a)), and Theorem R1 of Z5-ref gives
f in Rec under (W*), (H2), (H3-inf), (B_fin) -- with NO raise and NO value preservation.  QED
Remarks.  (a) Mechanism: (ND') fails only when the support of a is (up to finitely many target coordinates) carried by the signature sets
of the kernel carriers, with profiles proportional to the signatures -- i.e. exactly when every bad-carrier switching on F is cushion-
dominated and no raise is needed.  The second-order drift that worried V3-ref ("can collapse a d-neutral block cone") never meets a raise.
(b) The same dichotomy holds level by level in RS*_inf (SKETCH).  If (ND'_{B_np(l)}) fails at some level l_0, the same c (extended by zeros) shows
it fails at every l >= l_0, and by Lemma ND, F \ T_B(l_0) lies in the signature sets of the finitely many kernel carriers k, with
a = (c_k/kappa) v_k there.  In Lemma W take R := {s in F : s >= J, |a_s| < 4 Bx_*(s)} \ union_{kernel} S_k.  Kernel carriers never need a
raise: on S_k cap F \ T(l_*) the data are deep at a coordinate s iff |tau'_k| > 4|c_k/kappa|/(lambda' t) -- a condition independent of s
(both sides scale with v_k(s)) -- so if they are deep anywhere they are deep at the FIXED shallowest coordinate s_k of S_k cap F \ T(l_*)
... [for large levels s_k is fixed once T(l_*) cap S_k stabilizes; coordinates of S_k in T(l_*) are target coordinates, handled by (S1)],
and Lemma P at s_k pins k (constant C_q(1 + 2K*) 2^{s_k}/delta_k, an f-constant times K*), contradicting "kept".  At target coordinates j of
growing bad targets inside kernel signature sets, the non-kernel part of X' is <= (15/2) sum_{l > k, j in supp y_l} lambda_l |y_l(j)|/t
<= 5 2^{-2j} c_k delta_k/t (allowedness (b)), far below 4|a_j|/t = 4|c_k/kappa| v_k(j)/t for large j.  Hence R is EMPTY for large levels:
no raise and no VP at all, and the rate C_VP(l) in (W_inf) is needed only when (ND') holds at every level.  So (ND'_{B_np(l)}) can be
dropped from RS*_inf as well.  SKETCH: the pinning at s_k needs s_k notin T_B(l_*); if the targets of infinitely many bad carriers cover
the initial parts of a kernel signature set, Lemma P at those coordinates carries an extra error (4/t) 2^{-2s} c_k delta_k from the
bad targets (allowedness (b)), and the pinning constant is no longer an f-constant times K*; this corner case is not settled.
(c) (Superseded alternative, kept for the record.)  Kernel directions can also be restored after a raise by a BANK at a contact of a
kernel carrier k with c_k eps_k kappa > 0 (V1 Lemma B: first order, positive rate, correct sign of the drift); a triangular Graves argument
then preserves all values exactly.  Not needed after Theorem ND'.

## 4.3 (E4)(ii) degenerate bad peaks with the swallowing sign
R1/RS exclude a bad carrier l at a DEGENERATE peak k(l) with sgn w_m(k) = eps_l ((H3-inf)): its one-sided peak usage is not two-piece data.
(a) PROVED (reduction).  In the transport M-inf (part 3.4) such a carrier is a (K4) carrier of V1's classification at every clean w
(swallowing type, rho in [1-b, 1+b]); V1's donor raise (C3) turns every (K4) carrier into a strict non-peak of the companion with gap
>= c Lam (Lemma ST), after which it is an ordinary kept strict non-peak.  At infinite F the donor raise needs a private resource for the donor
peak c_m (Lemma D) of the block: Lemma TR-inf (a), (a'), (c), (c') -- a one-directional resource suffices for (C3), and its size Lam = T_lo^3
is admissible in cases (c), (c') because the second-order effects are O(Lam^2 Design^2) << b(w).  [A single robust support coordinate
WITHOUT pairing/anchor is NOT admissible: its common term moves every value by ~ rho Lam >> b(w) and destroys the tiny rates.]
(b) So (E4)(ii) is contained in the residual where, in some block, every robust-margin coarse peak lacks a resource of Lemma TR-inf, i.e.
in (NDN)-type configurations for donor peaks.  In RS*-type situations (no exactification needed otherwise) one can also use Y2's Theorem P
(donor condition (TD_m)), whose donor is again a resource question.
(c) OPEN: degenerate swallowing-sign bad peaks when every donor of the block is (NDN)-degenerate.
