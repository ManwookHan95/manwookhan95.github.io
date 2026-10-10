# U4 part 3 — The current master theorem for T_final; residual list; p_N versus p; status flags

T = T_final, U = U_final (part 1).  For N >= 1 let p_N be the norm with I = {1..N}; for f in S_{p_N^*} with forced data
(xi, q_0, a, w, F, z, zhat, e, nu) put Rec_N := {f : (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f)}.  Rates, classes,
sources, shift patterns and clean sub-windows are those of the rate scheme of T_final (part 1, 1.3(5)); "clean": no rate object
of level l has its value in Band(w) = (b(w), u(w)) (one exists at every level: V1 Theorem 2', with M(l) = omega(l)+1).

## 3.1 Definitions used in the statement
 (SH_w)  [V1 2.5] I_up(w) ∪ I_lo(w) = {} (every block has an upper and a lower shift source at w), or the shift cost of the
         source-deficient blocks is robust: c_{pi(w)}(f) >= u(w).
 rho^sh  [V2 Def. 3.2 with V2-ref P3] the shift-pinning rate rho^sh(kappa^sh(w), f) of the enlarged shift pattern of f at w (an LP
         minimum of the violation of the shift-extended system (R1)-(R7) over ||delta||_1 = 1).
 (C*)    [F finite] there is l_0 such that for every level l >= l_0 and EVERY clean sub-window w of level l:
             I_up(w) ∪ I_lo(w) != {},   c_{pi(w)}(f) <= b(w),   and   rho^sh(kappa^sh(w), f) <= b(w)
         (a near-exact coherent shift resonance, at all large levels, in a block lacking a shift source).
 Infinite-F conditions [Z5-ref R1; V3 3.2-3.4; V3-ref 2-3]: B := {l in L_N : r_l = 0} (bad carriers), B_K, B_F, B_np (bad strict
 non-peaks), (W*), (H2), (H3-inf), (B_fin), (CS_B), (ND'_{B_np}): a|_F notin span{u_l|_F : l in B_np}, (RR_{U_{B_np}}):
 sum{mu_s U_{B_np}(s) : s in F, |a_s| < y U_{B_np}(s)} = O(y^{1+eps}) for some eps > 0.

## 3.2 MASTER THEOREM (T_final).  
(i) [F finite; PROVED]  If f notin Rec_N, then (C*) holds.  Equivalently: if for infinitely many levels some clean sub-window w
    satisfies (SH_w) or rho^sh(kappa^sh(w), f) >= u(w), then f in Rec_N.  [Master Theorem III' of V2-ref 4b, on V1's Master Theorem
    II, for T_final by part 2.]  In addition f in Rec_N, whether or not (C*) holds, if f is block-tame (cor:BTrecovered), or
    f in R_0 ∪ R_0^± ∪ R_S (thm:R0, thm:Bpm, thm:S).  Constant-sign maximal contact (z = eps_0 off F) never satisfies (C*)
    (V1 M-II.3 / V2-ref P5(i): (SH_w) at every clean w of large level), so such rows are in Rec_N for every N.
    Hence the F-finite RESIDUAL is contained in (C*) \ (BT).
(ii) [F infinite; PROVED] f in Rec_N if one of the following holds:
    (RS')  (W*), (H2), (H3-inf), (B_fin), (ND'_{B_np}), (RR_{U_{B_np}})     [V3 Theorem RS with V3-ref Section 3; inspection standard];
    (R1)   (W*), (H2), (H3-inf), (B_fin), (CS_B)                           [Z5-ref Theorem R1];
    (SC)   super-critical support swallowing: Y3 Theorem 3.5 (D_sigma)  [Y3; refereed];
    (N)    (BD) Bx <= C_a |a|, (SC_I), (W_M)                              [Y3 Theorem 5.1, any admissible T];
    (Z5)   f in R_0^inf, R_0^{±,inf}, R_S^inf                             [Z5 + Z5-ref].
    Per mate (not per row): V3 Theorem A (fixed d-neutral two-piece data with (RR_W), (ND'_{L_0})), Y3 Theorems 2.1 / 6.1, and
    (LSC-trunc) for all these (V3 Cor. 4.2, Y3 6(b)).
(iii) [RESIDUAL LIST; PROVED as a logical statement]  If f notin Rec_N then:
    F finite:   (C*) and f is not block-tame.  [The sketched route Theorem C6 (SKETCH) needs C*-1 exact absorption of fine-peak
                residues on coarse free coordinates, C*-2 (SC) at companions in configuration (i), C*-3 exactification of the block
                scalars theta_m, A_m, C*-4 a shift direction constant along a window when >= 2 blocks are shifted, C*-5 a joint
                completion/absorption fixed point.]
    F infinite: every criterion of (ii) fails; in particular one of the RS' hypotheses fails:
                (E1) (RR_{U_{B_np}}) fails (mu-thin supports: |a_s| below a power of mu_s on infinitely many active coordinates);
                (E2) (B_fin) fails (infinitely many bad carriers; (O4-box), scale-free raises);
                (E4) (ND'_{B_np}) fails, or (H3-inf) fails (a bad carrier at a degenerate peak with the swallowing sign, or B_F at a
                     degenerate peak);
                (E5) (W*) or (H2) fails: the finite-F core at infinite F (transport of Master Theorems II/III' to infinite F;
                     V3 Theorem M_inf reduction PROVED, transport SKETCH with the open rate: VP constants for carrier sets growing with
                     the level must satisfy log C_0(j) = o(n(w_j))).
                (E3) (non-d-neutral fixed data at raised rows: (SC) at f_y) is an obstacle for the per-mate Theorem A, not a row class.
(iv) [DENSITY; OPEN]  For p_N: NA((c_0,p_N), l_2^2) is dense  <=>  Lemma Z for T_final and N (thm:reductionZ, valid for T_final by
    part 2)  <=>  Rec_N = S_{p_N^*}  <=>  every row in the residual classes of (iii) is in Rec_N.  None of (C*), (E1)-(E5) is settled,
    so density for p_N is OPEN for every N.  For Martin's norm p built with T_final and U_final (I = N): by lem:martintail,
    density for p follows from density for p_N for infinitely many N, because T_final and U_final do not depend on N (Lemma W).
    The hypotheses of (i)-(iii) are N-independent in the required sense: the design, the rate scheme, the sub-windows and every
    design constant are N-free; only f-constants (C_f, l_f) and the rate VALUES depend on N (through f), and rate objects that
    involve carriers absent from p_N take the value 1 (V1-ref p0).  No row-wise statement transfers from p_N to p: lem:martintail
    transports DENSITY (an operator statement), not membership of an individual first row in Rec (V3-ref F7; V3 Remark 3.5(e),
    second clause, is FALSE).  Density for p is OPEN.
    Conditional form (PROVED): if for infinitely many N every first row of p_N satisfying (C*) (F finite) or failing all criteria
    of (ii) (F infinite) belongs to Rec_N, then NA((c_0, p), l_2^2) is dense for the norm p built with T_final, U_final.

## 3.3 Proof of 3.2 (assembly of cited results; each step checked in part 2)
(i) By part 2 every hypothesis of V2-ref's Master Theorem III' holds for T_final; III' gives f in Rec_N under the stated
alternative.  Contrapositive: if f notin Rec_N, then for all but finitely many levels l (beyond l_f) every clean w of level l has
rho^sh < u(w) and not (SH_w).  At a clean w the values rho^sh and c_{pi(w)} are rate objects of level l (part 1, (5)), so they avoid
(b(w), u(w)); hence rho^sh <= b(w); and not (SH_w) means I_up ∪ I_lo != {} and c_{pi(w)} < u(w), hence c_{pi(w)} <= b(w).  This is
(C*).  The other classes: cor:BTrecovered [any T], thm:R0/thm:Bpm/thm:S [SLD, Lemma GW].  Constant-sign maximal contact: Z4
Lemma 5.0 gives in every block non-degenerate peaks of both swallowing types with margins >= q_0/4 (f-constants), which at every
clean w of large level are sources (L2) and (U2) (relative margin >= u, robust), so I_up ∪ I_lo = {} and (SH_w) holds (V2-ref P5(i)).
(ii) Part 2.3 for RS'; R1, Y3 Theorems 3.5, 5.1 and the Z5 classes hold for T_final by Lemma GW (R1, 3.5, Z5) resp. for every
admissible T (Theorem 5.1).
(iii) Contrapositives of (i), (ii); (E1), (E2), (E4), (E5) are the negations of the RS' hypotheses grouped as in V3-ref 7.
(iv) thm:reductionZ and prop:reduction (density <=> every (f, rho g) in cl NA) for T_final; lem:martintail; Lemma W.  QED

## 3.4 Status flags (what the master theorem rests on)
 SKETCH dependencies on the critical paths of (i) and (ii): NONE.  The SKETCH items of Rounds 5-7 (Z1 Theorem M; Z4 steering under (FS);
 Y2 6.4; Y4 assembly [superseded by V1, PROVED]; V2 near-coordinate conversion and Theorem C6; V2-ref (SC)-regularization; V3 Theorem
 M_inf transport, (O4-box) 4.4, Remark 3.5(c),(d); V4 Remark 2.3(2)) are used only in the residual descriptions.
 "PROVED by inspection" (a weaker but refereed standard) on the critical paths: Lemma GW (survival of window theorems on
 sub-windows; same meta-argument as V1 Theorem 1'(d), refereed); Z3 Lemma U / Y2 Lemma U' / V1 Theorem E'' (budget lemmas re-read with
 extra supports); Theorem RS' items (I1)-(I3) (V3-ref).
 Single-referee (proved in a referee report, not re-refereed) on the critical paths: V1-ref p0-p5; V2-ref P2, P3, P7 and Master
 Theorem III' (logic re-verified here, part 2.4(c)); V3-ref Lemma VP' (re-verified here, part 2.4(b)) and the (H3-inf)
 strengthening of RS' (if one prefers only double-refereed statements, use RS with (H3') = "no bad carrier at a degenerate peak",
 which is V3's own refereed statement with the (ND') fix); Y4-ref C.1-C.7 (re-verified by V1, refereed).
 New in this audit (both trivially fixable, both FIXED in T_final): C1 (literal V1 design factor 8^{sigma} does not dominate the
 bank factor for the mu-base; B_mu(l) required), C7 ((GM) at l = 1 can force c_1 < 1; impose (GM) for l >= 2).
