# U2 notes (Round 8): infinite base support -- items (E1)-(E5) of ADDENDUM 7

Part files (assembled below, after this head, with light edits): r8/U2_part1.md (E1), U2_part2.md (E2), U2_part3.md (E5),
U2_part4.md (E3, E4); orientation digest U2_part0.md.  Script: r8/U2_work/pair_tuning_check.py.
References: paper/martin_density_note.tex ("the note"); r5/Z5_ref_notes.md (R1 = Theorem R1, R2 = Lemma R2, Lemma R0);
r6/Y3_notes.md (Theorem 2.1, Theorem 6.1, (LSC-trunc)); r7/V1_notes.md (D_Omega, Lemma B, Lemma TU, (C1)-(C4), Prop. TR);
r7/V2_notes.md + V2_ref_notes.md (Theorem B, minors, (C*)); r7/V3_notes.md + V3_ref_notes.md (Lemma 2.3 RT, Theorem 2.5 E_RT,
Lemma VP', Theorem RS'); r8/U4_notes.md + U4_referee.md (T_final, fix C1 B_mu(l)).
Setting: finite block set I = {1..N}, p = p_N (lem:martintail passes density -- not individual rows -- to Martin's p for ONE N-free
design); f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu), F = supp a ARBITRARY (the point of this note: F infinite).
Labels: PROVED / SKETCH / HEURISTIC / OPEN / FALSE.  No counterexample is claimed; nothing found points to one.

## 0. Summary

Bottom line.  For a designed norm, (E1) and the (ND')-half of (E4) are SETTLED for RS-type rows (finitely many bad carriers), (E2) is
reduced to explicit rate conditions with all structural obstructions removed, and (E3), (E5) and the degenerate-peak half of (E4) are
reduced to the "(SC) at companions / exactness" complex that already forms the finite-F residual (C*), plus one new exotic tuning-degenerate
class (NDN):
 * (E1) mu-thin supports: SETTLED (PROVED) for RS-type rows (finitely many exactly swallowed bad carriers; and, conditionally on rates,
   for infinitely many, part 2) by a design choice plus a new pinning lemma.  With a diagonal base whose entries decay doubly
   exponentially (mu*_s = 2^{-2^{2^s}}), the raise-room condition (RR) of V3's Theorem RS is no longer needed: an unraised coordinate
   that would be deep for the window data PINS the switching carrier through the mate's own flip budget (Lemma P), so only coordinates
   beyond a depth J have to be raised, and their Hilbert footprint is <= mu*_J; the pinning constant 2^J/delta is O(log(window depth)).
 * (E4)(i) failure of (ND'): SETTLED (PROVED): (ND') can be dropped from Theorem RS.  If (ND') fails, the support of a lies (up to
   finitely many target coordinates) in the signature sets of the kernel carriers with profiles PROPORTIONAL to the signatures
   (Lemma ND), so every bad-carrier switching on F is cushion-dominated, no raise is needed, and R1 applies directly.
 * (E2) infinitely many bad carriers / (O4-box): REDUCED to rate conditions (PROVED, conditional).  Box-level deep raises (mass O(2^{-J}))
   plus Lemma P plus a pigeonhole of thresholds give cushion-compatible exact window data with NO bounded switching, NO box domination and
   NO (RR); what remains is a window condition (W_inf) on f-dependent rates (rooms, Hoffman constants of the growing exact cones, VP
   constants, gaps of bad strict non-peaks) -- the same kind of rates that V1/V2's clean sub-windows convert into design constants at
   finite F.  V3's "scale-free raise" obstruction disappears (the scale-free raise is needed only on the deep part, of vanishing mass).
 * (E5) transport of the finite-F master theorems: the VP rate is NOT needed (raise FIRST, deep, then exactify at the raised row: Lemma
   DR-inf keeps the clean classification); the only new ingredient is private two-sided TUNING of values of carriers whose design-depth
   signature coordinates lie in F.  Lemma TR-inf provides it (PROVED) in all cases except a near-(ND')-degenerate configuration (NDN),
   which is a rate condition on a alone and can alternatively be routed through non-d-neutral data, i.e. into "(SC) at companions".
   Theorem M-inf (SKETCH, flagged inspection items): an infinite-F row is in Rec_N unless (C*) [read at deep-raised rows], (NDN), or the
   block exclusions shared with finite F hold at all clean sub-windows of all large levels.
 * (E3) non-d-neutral data at raised rows: never needed in the window theorems (data are built AT the companion and are d-neutral);
   needed only inside (C*), where it is exactly V2's gap (C*-2) "(SC) at companions" (block property, independent of F).  For transported
   FIXED data the representation drift is a nonzero element of Y of infinite support (PROVED) which generically violates side-
   admissibility (HEURISTIC); not needed.
So "Lemma Z at infinite F reduces to Lemma Z at finite F" holds in the following precise sense: for the designed norm, every infinite-F
row is recovered except in configurations that are infinite-F transcriptions of the finite-F residual (C*) / "(SC) at companions",
plus the exotic tuning-degenerate class (NDN) (SKETCH level for the general transport; PROVED for RS-type rows: finitely many bad carriers,
any profile, no (RR), no (ND')).

| # | Result | Scope | Status | Where |
|---|---|---|---|---|
| 1 | Design SLD^star / T_final^*: base mu*_s = 2^{-2^{2^s}}, window factor Omega(l) = (s_max 2^{s_max}/delta_min) x (two design logarithms); admissible, N-free | design | PROVED | 1.1 |
| 2 | Lemma P: an unraised coordinate that is deep for the data pins the carrier, |tau_l| <= C_q t/v_l(s) | any SLD-type T, any F | PROVED | 1.2 |
| 3 | Theorem RS*: support swallowing of ANY profile by finitely many bad carriers, WITHOUT (RR) | SLD^star | PROVED (inspection items I1-I3 of V3 unchanged) | 1.3 |
| 4 | Lemma ND + Theorem ND': (ND') fails => a proportional to kernel signatures => R1 applies; (ND') dropped from RS* | any SLD-type T | PROVED | 4.2 |
| 5 | Lemma W: window data at a deep-raised companion, any number of bad carriers, no bounded switching / box domination | SLD^star | PROVED | 2.1 |
| 6 | Theorem RS*_inf: infinitely many bad carriers under the rate condition (W_inf) | SLD^star | PROVED (conditional) | 2.2 |
| 7 | Lemma DR-inf: a deep raise preserves the clean classification (no VP needed) | T_final^* | PROVED for (R1)-(R5), (R7), minors; (R6) SKETCH | 3.0 |
| 8 | Lemma TR-inf: private two-sided tuning at infinite F (cases (a), (a'), (c), (c')) | T_final^* | PROVED | 3.2 |
| 9 | Residual (NDN) of the tuning; relation to (ND') and to (SC) at companions | -- | precise statement; OPEN | 3.3 |
| 10 | Theorem M-inf: transport of Master Theorem III' to infinite F | T_final^* | SKETCH (flagged items) | 3.4 |
| 11 | (E3): window theorems need no (SC); drift of transported fixed non-d-neutral data; (E3) inside (C*) = (C*-2) | -- | PROVED (structure, drift in Y), HEURISTIC (generic violation), OPEN (C*-2) | 4.1 |
| 12 | (E4)(ii) degenerate swallowing-sign bad peaks: via V1's donor raise in M-inf, needs a donor resource of Lemma TR-inf | T_final^* | SKETCH | 4.3 |
| 13 | Numerics: pair tuning cancels the common term exactly at first order (60 digits) | evidence | -- | 5 |

## 0.1 Answers to the task items
(1) (E5): the f-dependent VP rate is avoided altogether by the order "deep raise, then exactify" (Lemma DR-inf); the new requirement --
two-sided private value tuning of carriers whose shallow signature lies in F -- is met by Lemma TR-inf with design x u^{-C} constants
(contacts / convertible thin support / robust Hilbert pairs / anchors); its failure (NDN) is a rate object whose robust case is covered
and whose tiny case is a near-(ND') degeneracy.  Theorem M-inf states the resulting transport (SKETCH).
(2) (E1): settled by Lemma P + design mu* (Theorem RS*); neither two-stage approximation nor a weighted footprint is needed: the
thin shallow coordinates are handled by the MATE's flip budget (they pin), only the deep part is raised.
(3) (E2): Lemma W + Theorem RS*_inf: per window only the coarse bad carriers matter; box-level deep raises of mass O(2^{-J}); pinned
carriers removed by a pigeonhole of |B(l)|+1 thresholds; shallow thin TARGET coordinates handled by a second pigeonhole (sub-window
position) and contact rows.  Remaining: the rate condition (W_inf).
(4) (E3): structural reduction to (C*-2) (4.1); (E4): (ND') dropped (Theorem ND'); degenerate swallowing-sign bad peaks reduced to the
donor-resource question (4.3).

# U2 part 1: item (E1) -- removing the raise-room condition (RR) by a design choice and a thin-support dichotomy

References: the note paper/martin_density_note.tex ("the note"); r5/Z5_ref_notes.md (R1 = Theorem R1, R2 = Lemma R2);
r7/V3_notes.md (Lemma 2.1-2.3 = RT, Cor 2.4, Theorem 2.5 = E_RT, Lemma 3.1, Lemma VP); r7/V3_ref_notes.md (Lemma VP', Theorem RS').
Setting: I = {1..N} finite, p = p_N, f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu), F = supp a ARBITRARY,
s_j := sgn a_j (j in F), s(t) := sqrt(1+t^2). Labels PROVED / SKETCH / HEURISTIC / OPEN / FALSE.

## 1.0 What (RR) was for, and why it is not intrinsic
In Theorem RS' (V3-ref Section 3) the exact switching X = sum_{l in B_np} eps_l tau'_l u_l (|tau'_l| <= C_tau, bounded switching)
is anti-signed beyond the cushion on R1's deep set D_t = {j in F : s_j X_j < -4|a_j|/t}; RS raises EVERY coordinate of
{j in F : |a_j| < y U_B(j)} (y ~ 4 C_tau T) and pays the Hilbert footprint y M_mu(y); (RR) says this is o(y^2).  (RR) fails for
mu-thin a (|a_s| below every power of mu_s on infinitely many active s), and such a exist for every fixed mu.
The observation of this part: a coordinate j in S_l cap F which is unraised and deep for the data PINS the actual switching
amplitude tau_l at scale t with constant ~ 1/v_l(j) (flip budget).  So only DEEP coordinates (large j) ever need raising, and
those have tiny mu_j if mu decays fast enough relative to the signature weights v_l(j) ~ 2^{-j}.  This is a property of the
design, not of a.

## 1.1 The design SLD^star (PROVED: admissible, N-free, (P1)-(P3))
Take Definition def:SLD of the note with two changes.
(B*) The base: H = l_2 with orthonormal basis (k_s), U k_s := mu*_s e_s with
        mu*_s := 2^{-2^{2^s}}   (s >= 1).
     U is compact (mu*_s -> 0), has dense range (it contains c_00), ||U|| <= 1/4, U^* e_s^* = mu*_s k_s, and
     q*(a) = ||a||_1 + (sum_s (mu*_s a_s)^2)^{1/2}.
(W*) Window factor: with s_max(l) := max({1} cup T(l)), T(l) := union_{l'' <= l} supp y_{l''} (finite; fixed before the window
     parameters of level l are chosen, since y_{l''}, l'' <= l, are chosen first in (D1)), delta_min(l) := min_{l'' <= l} delta_{l''} and
        Omega_K(l) := s_max(l) 2^{s_max(l)}/delta_min(l),
        Omega_log(l) := (2 + log_2(2 + log_2(1/T_lo(l-1)))) (2 + log_2(l 2^{l^3} Lambda°(l) Omega_K(l))),   Omega(l) := Omega_K(l) Omega_log(l)
        (design quantities of level l: everything in them is fixed before the window parameters of level l),
     replace in (D1)
        n^w_l := ceil(l 2^{l^3} Omega(l) Lambda°(l)),   T_hi(l) := min{T_lo(l-1), 2^{-l^3}/(l Omega(l) Lambda°(l))}.
     (For B finite only the factor 2^{s_max(l)} is used; the full Omega(l) -- including the logarithm of the depth of the previous window,
     which absorbs the pinning constant 2^J when it is MULTIPLIED by the f-dependent threshold factors -- is used for infinitely many bad
     carriers, part 2.)
Proof of the claims.  The base: Proposition prop:smooth(c) and all of Sections 1-8 of the note hold for every compact
dense-range U (the note fixes the base before T and uses it only through ||U|| in delta_l).  (P1), (P2) and admissibility
(Theorem thm:SLD) use (D1) only through allowedness (a), (b) and c_{l+1} <= c_l/4, which are unchanged.  (P3): T_hi(l)2^{l^3}
Lambda°(l) <= 1/l and n^w_l >= l 2^{l^3} Lambda°(l) hold a fortiori; T_hi(l+1) <= T_lo(l) by definition.  N-freeness: no
quantity depends on N.  QED
Remark.  Every result of the note, of Z5/Z5-ref (R1, R2) and of V3/V3-ref stated for "SLD-type designs over any base" holds for
SLD^star (they use the windows only through (P3) and "window length / f-dependent factor -> infinity"; a longer window only helps).
The same two changes can be made in D_Omega / D^{V2} (there Design(l) already contains 2^{s_max(l)}/delta_min(l); the bank constants of V1 Lemma B
involve the base entries at the design depth sigma(l), so Design(l) must include (mu*_{sigma(l)})^{-2} -- a design quantity; not
re-checked line by line here: SKETCH for D_Omega/D^{V2}).

## 1.2 Lemma P (pinning by an unraised deep coordinate).  PROVED (any SLD-type T, any F, any row with forced data).
Let l_* be a window index, t in (0, min(t_eta,1)], (B_+-, Theta_+-) a two-sided decomposition at scale t of a mate g' of a first row
f' (budget p*(f' + r g') <= 1 + (1 + eta')r^2/2, eta' <= 1, g'(xi') = 0), with forced data (a', z', ...) of f', F' = supp a'.
Let l <= l_* be a carrier, tau_l := -eps_l Delta theta_l for a sign eps_l, and s in S_l cap F' with s notin T(l_*).  Put
sigma := sgn tau_l and suppose s_s eps_l = -sigma (the coordinate is of the type opposite to the switching direction).  Then
  |tau_l| v_l(s) <= 2|a'_s|/t + phi_s + |r_s|,                                                                           (P.1)
where phi_s := f^+_s + f^-_s (lem:flip at f'), sum_{s in F'} phi_s <= (1 + eta')t/(2 q'_0), and r_s := sum_{l'' > l_*, s in supp y_{l''}}
Delta theta_{l''} y_{l''}(s)/n_{l''} satisfies sum_s |r_s| <= 8t^2.  Consequently, if
  |tau_l| v_l(s) >= (16/5)|a'_s|/t      (the data coordinate is deep, see 1.3),                                          (P.2)
then |tau_l| <= (8/3)(phi_s + |r_s|)/v_l(s) <= C_q t/v_l(s), C_q := (8/3)(1/q'_0 + 8).
If s in S_l cap T(l_*) \ T_B (T_B := union_{l'' in B} supp y_{l''}), the same holds with r_s replaced by r_s + r'_s, r'_s := sum over
coarse GOOD l'' with s in supp y_{l''} of Delta theta_{l''} y_{l''}(s)/n_{l''}; |r'_s| <= (4/3) sum_{good, coarse}|Delta theta_{l''}|.
Proof.  By (P1) of thm:SLD, for s in S_l: u_l(s) = v_l(s), u_{l'}(s) = 0 for l' < l, u_{l''}(s) = y_{l''}(s)/n_{l''} for l'' > l.
For l < l'' <= l_*, s in supp y_{l''} would put s in T(l_*); so if s notin T(l_*), by eq:DeltaB
  Delta B(s) = -Delta theta_l v_l(s) - sum_{l'' > l_*} Delta theta_{l''} y_{l''}(s)/n_{l''} = eps_l tau_l v_l(s) - r_s.
lem:flip (whose proof uses only the base budget, hence holds with budget (1+eta')t^2/2 and the constant 1/q'_0 replaced by
(1+eta')/q'_0) gives s_s B_+(s) >= -|a'_s|/t - f^+_s and s_s B_-(s) <= |a'_s|/t + f^-_s, so s_s Delta B(s) >= -2|a'_s|/t - phi_s.
Since s_s eps_l = -sigma and tau_l = sigma|tau_l|, s_s Delta B(s) = -|tau_l| v_l(s) - s_s r_s, and this is (P.1).  sum|r_s| <= sum_{l''>l_*}|Delta theta_{l''}| ||y_{l''}||_1/n_{l''}
<= (4/3) 6 sum_{l''>l_*} lambda_{l''}/t <= 8 T_lo(l_*)^3/t <= 8t^2 (lem:box, (P2)).  Under (P.2), 2|a'_s|/t <= (5/8)|tau_l| v_l(s),
and (P.1) gives (3/8)|tau_l| v_l(s) <= phi_s + |r_s|.  For s in T(l_*) \ T_B the extra terms come from coarse targets containing s;
bad carriers' targets do not contain s.  QED

## 1.3 Theorem RS* (support swallowing of any profile; no (RR)).  PROVED (modulo the inspection items (I1)-(I3) of V3/V3-ref,
which are unchanged).
Design SLD^star, every N >= 1.  Let f in S_{p_N*} (F arbitrary) satisfy R1's (W*), (H2), (H3-inf), (B_fin) and (ND'_{B_np})
[B_np := bad strict non-peaks].  Then f in Rec.  [Compared with RS' (V3-ref Section 3): (RR_{U_{B_np}}) is removed.  The hypothesis
(ND'_{B_np}) is removed as well in part 4 (Theorem ND': if it fails, no raise is needed and R1 applies directly).]

Proof.  We describe only the changes to the proof of RS' (V3 Theorem RS with V3-ref Section 3), which runs R1 at a raised
companion f_j and concludes with Theorem 2.5 (E_RT) and Y3 Theorem 2.1.  Fix g in C(f), rho in (0,1), and all of R1's constants
(eta_0, kappa_0, eps_tr, eta, C_tau, K*, C_f, c_flat, t_1), with a factor 2 of room as in RS.  Put B := B_np (B_pk carriers have
tau' = 0 by the cone and do not enter X), delta_B := min_{l in B} delta_l, and let H be the maximum over L' subset B of the Hoffman
constants (for the violation measure of eq:hoffman, augmented by sum_{l in L'}|tau_l|) of the polyhedral cones
  Z_f(L') := Z_f cap {tau_l = 0 : l in L'}
(Z_f is R1's exact-switching cone; finitely many cones, so H is an f-constant).  Let C'_f K* t be R1's bound for the violation
of Z_f by the actual amplitudes (R1 Step 2), and C_q := (8/3)(2/q_0 + 8) (room factor 2 for q'_0 >= q_0/2 at f_j).

Step 1' (thresholds).  For a window index l_j and an integer J put
  K_1(l_j, J) := (5/4) C_q [(1 + 2K*(l_j)) 2^{s_max(l_j)} + 2^J]/delta_B
  (the first term serves target coordinates j in T(l_j) \ T_B, j <= s_max(l_j), where r'_s carries the good-carrier pinning;
   the second serves non-target coordinates j < J, where only fine carriers enter r_s),
  K_{i+1} := 4H(C'_f K* + |B| K_i) + 2K_i  (1 <= i <= |B|+1),  K'(l_j, J) := C_B (K* + K_{|B|+2}),
C_B an f-constant chosen so that K'(l_j,J) t bounds the closeness constant of R1 Claim 3.2(d) when "C_f K* t" there is replaced by
K_{|B|+2} t.  Then K'(l_j, J) <= C'_B [(1 + K*(l_j)) 2^{s_max(l_j)} + 2^J]/delta_B with C'_B := 2 C_B (4H|B| + 3)^{|B|+2} C_q (an
f-constant): the dependence on 2^J is ADDITIVE (no factor K*).

Step 1'' (windows and the raise depth).  By (W*) take levels l_j with Lambda*_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0; by the window
factor of SLD^star, K*(l_j) 2^{s_max(l_j)} T_hi(l_j) -> 0 and K*(l_j) 2^{s_max(l_j)}/n^w_{l_j} -> 0.  Put T_j := T_hi(l_j),
L_j := log_2(1/T_j), A := 48 rho^2/(c_flat(1 - rho^2)), theta_j := 1/l_j, and for n in N let
  x_j(n) := theta_j c_flat^2 T_j 4^{-n}/C_e,   J_j(n) := min{J : mu*_J <= x_j(n)^2},
C_e an f-constant fixed below.  Since mu*_J = 2^{-2^{2^J}}, 2^{J_j(n)} <= 2 log_2(2 log_2(1/x_j(n))) <= 2 log_2(4(L_j + 2n + l_j + C_e')).
Let n_j be the least n >= 1 with n >= A K'(l_j, J_j(n)) (it exists: the right side grows at most logarithmically in n), and
J_j := J_j(n_j).  Then n_j <= 1 + A C'_B [(1 + K*) 2^{s_max(l_j)} + 2 log_2(4(L_j + 2n_j + l_j + C_e'))]/delta_B, hence (using
L_j <= l_j^3 + log_2(l_j 2^{s_max} Lambda°(l_j)) + log_2(1/T_lo(l_j - 1)) and that log_2(1/T_lo(l_j-1)), log n^w are o(n^w_{l_j})):
  n_j = o(n^w_{l_j}),   K'(l_j, J_j) T_j -> 0,   J_j -> infinity.
So S_j := {T_j 2^{1-i} : 1 <= i <= n_j} subset W(l_j), and every t in S_j satisfies R1's smallness conditions for large j.

Step 2' (companion: raise only the deep part).  y_j := 4 C_tau T_j and
  R_j := {s in F cap union_{l in B} S_l : s notin T_B, s >= J_j, |a_s| < y_j U_B(s)},   Delta a_s := s_s (y_j U_B(s) - |a_s|)_+ 1_{R_j}(s),
followed by the VP' correction Delta a'' for L_0 := B on the fixed finite set F_0 of (ND'_{B}) (J_j > max F_0 for large j);
f_j := the row with forced data ((a + Delta a + Delta a'')/lambda_j, z).  Footprint: ||U^* Delta a|| <= sum_{s in R_j} mu*_s y_j U_B(s)
<= mu*_{J_j} y_j ||U_B||_1 <= mu*_{J_j} y_j |B|, and ||U^*Delta a|| <= mu*_{J_j}||Delta a||_1, so lambda_j >= 1 for large j
(V3-ref Section 2).  By V3 Lemmas 2.1, 2.2, VP': eps'_j := 2||U^*(Delta a + Delta a'')|| + 2||Delta a''||_1 + p*(L^*(w_j - w))
<= C mu y_j log(e/(mu y_j)) with mu := mu*_{J_j} <= x^2, x := x_j(n_j); since mu log(e/(mu y)) <= mu log(e/mu) + mu log(1/y)
<= sqrt(mu) + x^2 log(1/y_j) <= 2x for large j (x log(1/y_j) <= T_j log(1/T_j) -> 0), we get eps'_j <= 2C x y_j = 8 C C_tau theta_j
c_flat^2 T_j^2 4^{-n_j}/C_e <= theta_j c_flat^2 (T_j 2^{-n_j})^2 once C_e >= 8 C C_tau.  ||Delta a||_1 <= y_j |B| -> 0, so lambda_j -> 1 and p*(f_j - f) -> 0.  Statuses, rooms, z,
K, J, B, eps_l, T_0 unchanged; values of B preserved (VP'); Z_{f_j} = Z_f (V3-ref Section 3 (a), (b)).

Step 3 (unchanged).  g_j := g - (g(xi_j)/q_0^{(j)}) a^{(j)}; the budget lemmas hold at f_j on [T_j 2^{-n_j}, T_j] ((I1)).

Step 4' (exact window data at f_j without a deep set).  Fix t in S_j and a two-sided decomposition of g_j at f_j at scale t with
actual amplitudes tau_l (l in B).  Since the |B| numbers |tau_l| cannot meet all |B|+1 intervals (K_i t, K_{i+1} t], 1 <= i <= |B|+1,
choose i_0 with no |tau_l| in (K_{i_0} t, K_{i_0+1} t]; put L' := {l in B : |tau_l| <= K_{i_0} t} (PINNED at this scale) and call the
other l in B KEPT (|tau_l| > K_{i_0+1} t).  Let tau' be a nearest point of Z_f(L') to tau.  By the choice of H,
  sum_B |tau_l - tau'_l| <= H(C'_f K* t + |B| K_{i_0} t) <= K_{i_0+1} t/4 <= K_{|B|+2} t,
so tau' satisfies R1 Step 2 with C_f K* t replaced by K_{|B|+2} t (it lies in Z_f, a fortiori), bounded switching |tau'_l| <= C_tau
for large j, tau'_l = 0 for l in L', and sgn tau'_l = sgn tau_l, |tau'_l| <= (5/4)|tau_l| for kept l.
CLAIM: X' := sum_B eps_l tau'_l u_l has EMPTY deep set at f_j: s_j X'_j >= -4|a^{(j)}_j|/t for all j in F.
 (i) j in T_B cap F: a finite set with |a_j| > 0; since |a^{(j)}_j| >= |a_j|/4 (lambda_j <= 2, |Delta a''| <= |a|/2), for t <= T_j and j large,
     4|a^{(j)}_j|/t >= |a_j|/T_j >= C_tau |B| >= |X'_j|.
 (ii) j notin T_B and j notin union_{l in B} S_l: X'_j = 0 (by (P1), off T_B only signatures of B contribute).
 (iii) j in S_l \ T_B, l in B, tau'_l = 0 (in particular l in L'): X'_j = 0.
 (iv) j in S_l \ T_B, l kept, sigma := sgn tau'_l = sgn tau_l.  X'_j = eps_l tau'_l v_l(j); if s_j eps_l = sigma, s_j X'_j >= 0.
      Otherwise s_j eps_l = -sigma and s_j X'_j = -|tau'_l| v_l(j); suppose |tau'_l| v_l(j) > 4|a^{(j)}_j|/t.
      - If j >= J_j: either j in R_j, so |a^{(j)}_j| >= y_j U_B(j)/lambda_j >= y_j v_l(j)/2, or j notin R_j, so |a^{(j)}_j| = |a_j|/lambda_j
        >= y_j v_l(j)/2; in both cases 4|a^{(j)}_j|/t >= 2 y_j v_l(j)/T_j = 8 C_tau v_l(j) > |tau'_l| v_l(j): contradiction.
      - If j < J_j: |tau_l| v_l(j) >= (4/5)|tau'_l| v_l(j) > (16/5)|a^{(j)}_j|/t, which is (P.2) at f' = f_j.
        If j notin T(l_j), Lemma P gives |tau_l| <= C_q t/v_l(j) and v_l(j) = delta_l 2^{-j}/n_l >= (4/5) delta_B 2^{-J_j}.
        If j in T(l_j) \ T_B (so j <= s_max(l_j)), Lemma P with r'_s, |r'_s| <= (4/3) K* t (R1 Step 1 at f_j: good carriers
        pinned), gives |tau_l| <= C_q(1 + 2K*) t/v_l(j) <= (5/4) C_q (1 + 2K*) 2^{s_max(l_j)} t/delta_B.
        In both cases |tau_l| <= K_1 t < K_{i_0+1} t, contradicting "kept".
 Hence D_t = {} for the data of R1 Step 3 built from tau' (A_j := 2|a^{(j)}_j|/t).  R1 Claims 3.1, 3.2 then give d-neutral two-piece
 data at f_j for g_{j,t} with (s b^+)_- <= 3|a^{(j)}|/t and (s b^-)_+ <= 3|a^{(j)}|/t on F (no C_* U_* term),
 p*(g_j - g_{j,t}) <= K'(l_j, J_j) t, Gamma_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta)) + K^R_4' t)^2 with K^R_4' = O(K'(l_j,J_j)),
 and R2's block size conditions (A_2 = 4 + C_tau/lambda_B, gamma_B uniform).
Step 5 (unchanged; Lemma R2 with U_* = 0 at f_j): p*(f_j + r g_{j,t}) <= 1 + (r^2/2)(1 + eta_0) for |r| <= c_flat t.
Step 6 (Theorem 2.5).  (a): Cor. 2.4 with eps'_j of Step 2'; (b): Steps 4'-5 with K_j := K'(l_j, J_j); (c): n_j >= A K_j by Step 1'',
K_j T_j -> 0, lambda_j -> 1, p*(f_j - f) -> 0; (d): Step 2'; (e): the averaged data over S_j are d-neutral two-piece data at f_j with
kappa_w <= 1 + eta_0/2 and side parts <= 3|a^{(j)}|/(T_j 2^{1-n_j}) on F (convexity), so (CS-side) holds at f_j and Y3 Theorem 2.1
(I_- empty) gives (f_j, rho gbar_j) in cl NA.  Theorem 2.5: (f, rho g) in cl NA; rho -> 1.  QED

## 1.4 Remarks
(a) Where the dichotomy is hidden.  At every scale and for every switching carrier, an UNRAISED coordinate that would be deep
for the data is either deep in the sense of mu (j >= J_j, raised at footprint <= mu*_{J_j}) or shallow (j < J_j), and then the
mate's own flip budget pins that carrier with constant ~ 2^{J_j}/delta_B (Lemma P).  The thresholds K_i and the pigeonhole over
|B|+1 intervals separate pinned and kept carriers so that the Hoffman projection onto Z_f(L') does not destroy the sign of kept
carriers.  The resulting window constant is K* x f-constant x (2^{J_j} + 2^{s_max})/delta_B, and with mu* doubly exponential
2^{J_j} = O(log(L_j + n_j)) is absorbed by any window.
(b) What fast decay of mu is needed.  The proof uses only: sum_{s >= J} mu_s U_B(s) <= mu_J ||U_B||_1 (mu nonincreasing) and
"2^{J(x)} = o(n^w_l / K*(l))" where J(x) := min{J : mu_J <= x^2}, x ~ T_hi(l) 4^{-n}; for mu*_s = 2^{-2^{2^s}} this is
2^{J(x)} <= 2 log_2 log_2(1/x^2).  With V3's mu_s = 2^{-s^2-1}, 2^{J(x)} ~ 2^{sqrt(2 log(1/x))}, which is NOT absorbed in general
(it exceeds every power of log(1/T_hi(l)) and may exceed n^w_l/K*): so the design change of 1.1 is genuinely used.
(c) Fixed data (V3 Theorem A) still need (RR_W): fixed two-piece data may use a shallow thin coordinate anti-signed (nothing pins
them); window data cannot (Lemma P).  This is irrelevant for the window theorems (RS, M_inf), where all data are window data.
(d) Scope of the gain.  (E1) is settled for every RS-type situation (finitely many bad carriers, (H2), (H3-inf), (W*); (ND') by part 4):
mu-thin supports are recovered.  Lemma P and Step 4' are local in the level and transfer to any window construction in which
the exact switching is a finite combination of carriers with private signature sets (V1/V2 transplants): see part 3.
# U2 part 2: item (E2) -- infinitely many bad carriers at infinite F (O4-box); no bounded switching, no box domination

Setting and references as in part 1.  Design SLD^star (part 1.1).  For a window index l_* write B(l_*) := B cap [1, l_*] (coarse bad
carriers), B_np(l_*) its strict non-peaks, T_B(l_*) := union_{l in B(l_*)} supp y_l (finite, subset [1, s_max(l_*)]).
B (the set of bad = exactly swallowed carriers, r_l = 0) may now be INFINITE.

## 2.0 What changes when B is infinite (diagnosis)
V3 4.4 described (O4-box) as follows: with infinitely many bad carriers the switching on F is box-size, |X_j| <~ Bx(j)/t, so cushion
compatibility needs |a^#_j| >~ Bx(j), a SCALE-FREE raise whose mass does not tend to 0; raises give box domination on the deep part only,
and "thin shallow support remains" ((BD_B) needed on F cap [1, N(T)]).  Lemma P of part 1 removes exactly the last point: a shallow
coordinate that would be deep for the data PINS the carrier.  The scale-free raise is needed only on the deep part j >= J, whose mass
is O(2^{-J}) -> 0.  Bounded switching (Z5 Lemma 5.2, an f-dependent injectivity modulus that grows with B(l_*)) is not needed either:
box bounds plus the pigeonhole of thresholds control every size bound R1 needs.  What remains are f-dependent rates of the same kind as
at finite F (Hoffman constants of the growing exact cones, VP constants, gaps of bad strict non-peaks, rooms of good carriers).

## 2.1 Lemma W (window data at a deep-raised companion; any number of bad carriers).  PROVED.
Fix f in S_{p_N*} (F arbitrary), g in C(f), rho in (0,1) and R1's constants (eta_0, kappa_0, eps_tr, eta, with room factor 2).
Let l_* be a window index with l_* >= l_f (R1's threshold: good non-degenerate peaks k°_m of (H2) are coarse), and assume for every l
in B_np(l_*) that k(l) is a strict non-peak with gap >= gamma_B(l_*) > 0, and (H3-inf) for the bad carriers <= l_*.
Let Z := Z_f(l_*) subset R^{B(l_*)} be R1's exact-switching cone built from B(l_*) (rows: tau_l >= 0 on B_K; contact and free rows on
T_0 := T_B(l_*) \ F; tau_l = 0 on bad peaks; d-rows sum_{l <= l_*, m(l) = m} q_l tau_l = 0), and for P subset B_np(l_*) and
Sigma subset T_B(l_*) cap F let
   Z(P, Sigma) := Z cap {tau_l = 0 : l in P} cap {s_j sum_{l in B(l_*)} eps_l tau_l u_l(j) >= 0 : j in Sigma};
let H(l_*) >= 1 be the maximum of the Hoffman constants of the Z(P, Sigma) (finitely many polyhedral cones; violation measured as in
eq:hoffman plus sum_P |tau_l| plus the negative parts of the Sigma-rows).  Let K*(l_*) := (1/q_0 + 22) Lambda*_f(l_*) with the rooms
r*_l(l_*) of good l computed on S_l \ (F cup union_{l' in B(l_*), l' > l} supp y_{l'}).
Let f' be a row with forced data ((a + D)/q*(a + D), z), D = Delta a + Delta a'', where
 (R) with Bx_*(s) := sum_{l in B_np(l_*)} lambda_l |u_l(s)| (= lambda_l v_l(s) on S_l \ T_B(l_*)):
     R := {s in F : s >= J, |a_s| < 4 Bx_*(s)},   Delta a := sum_{s in R} s_s (4 Bx_*(s) - |a_s|) e_s^*   [deep raise at BOX level];
     raise mass <= psi(J) := 4 sum_{l in B} lambda_l ||u_l 1_{[J, infinity)}||_1 -> 0 (J -> infinity), footprint <= mu*_J psi(J);
 (V) Delta a'' is the VP' correction for L_0 := B_np(l_*) on its finite set F_0 (which requires (ND'_{B_np(l_*)}), F_0 cap R = {} ).
Let t be a dyadic scale with t <= min(t_eta, t_1, 1), and suppose the following SUB-WINDOW CONDITIONS at t:
 (S1) for every j in T_B(l_*) cap F with j < J: either |a_j| <= theta_1 t^2 or |a_j| >= K_top t^2   [K_top defined below; theta_1 <= 1];
 (S2) the budget at f' is (1 + eta')t^2/2 with eta' <= 1 (Corollary 2.4 of V3 at f' gives this when eps'(f') <= t^2/8 and
      lambda' - 1 <= 1/8), and K_top t <= min(1, kappa_0/K_4) (K_4 an f-constant of R1 Claim 3.2(d)).
Define the thresholds K_1 := (5/4) C_q [(1 + 2K*(l_*)) 2^{s_max(l_*)} + 2^J]/delta_min(l_*) + 4 theta_1 + 4C'_f(1 + K*(l_*)),
K_{i+1} := 4H(l_*)(C'_f(1 + K*(l_*)) + l_* K_i + s_max(l_*) K_1) + 2K_i (1 <= i <= l_*+1), K_top := K_{l_*+2}.
Then every two-sided decomposition of a mate g' of f' at scale t (with g' close to g as in V3 RS Step 3) yields d-neutral two-piece
data (b^+-, omega^+-) at f' for a functional g'_t with
   (s b^+)_- <= 3|a'|/t and (s b^-)_+ <= 3|a'|/t on F,   p*(g' - g'_t) <= C''_f K_top t,
   Gamma_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta)) + C''_f K_top t)^2,   t||b^+-||_1 <= A_0,   |omega^+-_m(k)| <= A_2/t at k = k(l),
with A_0, A_2 absolute multiples of 1 + ||a||_1 (no bounded-switching constant, no lambda_B), C''_f an f-constant.
Proof.
(1) Pinning (R1 Step 1 and lem:badpeaks at f').  Lemma modswallow(a) holds at level l_* with B replaced by B(l_*): the fine bad carriers
l > l_* have |Delta theta_l| <= 6 lambda_l/t (lem:box) and enter the good inequalities only through their targets, with total
contribution <= 8t^2 (P2); so sum_{good} |Delta theta| <= K* t, sum_{l > l_*} |Delta theta_l| <= 6t^2.  lem:badpeaks (a)-(c) at f'
(fixed good peaks of (H2)); in (b) the fine bad d-terms are bounded by sum_{l > l_*} |q_l| 6 lambda_l/t <= 6 T_lo(l_*)^3/(C_min t)
= O(t^2).  So the violation of Z by the actual amplitudes tau = (tau_l)_{l in B(l_*)} is <= C'_f(1 + K*) t (R1 Step 2, with the fine
bad targets on T_0 contributing <= 8t^2).
(2) Pigeonhole and projection.  The <= l_* numbers |tau_l| (l in B_np(l_*)) miss one of the l_*+1 intervals (K_i t, K_{i+1} t]; let
i_0 be such an index, P := {l : |tau_l| <= K_{i_0} t} (pinned), the others KEPT (|tau_l| > K_{i_0+1} t).  Sigma := {j in T_B(l_*) cap F :
j < J, |a_j| <= theta_1 t^2}.  For j in Sigma, by lem:flip at f' (cushion |a'_j| <= (3/2)|a_j|) and eq:DeltaB,
s_j sum_{B(l_*)} eps_l tau_l u_l(j) >= -3|a_j|/t - phi_j - |r_j| >= -(3 theta_1 + C'_f(1 + K*)) t (r_j: good coarse, fine and bad-peak
carriers at j), so the Sigma-rows are violated by <= s_max(l_*) K_1 t in total.  Let tau' be a nearest point of Z(P, Sigma) to tau:
sum |tau - tau'| <= H(l_*)(C'_f(1+K*) + l_* K_{i_0} + s_max K_1) t <= K_{i_0+1} t/4.  Hence tau'_l = 0 on P, and for kept l:
sgn tau'_l = sgn tau_l, (3/4)|tau_l| <= |tau'_l| <= (5/4)|tau_l| <= (15/2) lambda_l/t (lem:box).
(3) No deep set.  Let X' := sum_{B_np(l_*)} eps_l tau'_l u_l (tau' = 0 on bad peaks), so |X'_j| <= (15/2) Bx_*(j)/t.  Assume J > max F_0.
Claim: s_j X'_j >= -4|a'_j|/t for all j in F.  Suppose not, at some j in F.
 - j >= J: if j in R, |a'_j| = 4Bx_*(j)/lambda' >= 2Bx_*(j); if j notin R, |a'_j| = |a_j|/lambda' >= 2Bx_*(j); then
   4|a'_j|/t >= 8Bx_*(j)/t > |X'_j|: contradiction.
 - j < J, j in S_l \ T_B(l_*) for some l in B_np(l_*): X'_j = eps_l tau'_l v_l(j).  If l is pinned, X'_j = 0.  If l is kept, the violation
   forces s_j eps_l = -sgn tau'_l and |tau'_l| v_l(j) > 4|a'_j|/t, hence (P.2) of Lemma P at f' for the actual tau_l (|tau_l| >= (4/5)|tau'_l|),
   so |tau_l| <= C_q(1 + 2K* 1[j in T(l_*)]) t/v_l(j) <= K_1 t < K_{i_0+1} t: contradiction with "kept".
 - j < J, j in T_B(l_*) cap F: if j in Sigma, the Sigma-row gives s_j X'_j >= 0; otherwise (S1) gives |a_j| >= K_top t^2 and:
   by lem:flip at f' and eq:DeltaB, s_j X_j(tau) >= -2|a'_j|/t - phi_j
   - |r_j| >= -2|a'_j|/t - C'_f(1 + K*) t (r_j collects good coarse carriers (<= (4/3)K* t), fine carriers (<= 8t^2) and bad peaks
   (<= lambda K_d t, lem:badpeaks(c)) at j), and |X'_j - X_j(tau)| <= sum|tau' - tau| <= K_top t/4.  Since |a'_j| >= |a_j|/4 (lambda' <= 2,
   |Delta a''| <= |a|/2), 2|a'_j|/t >= K_top t/2 >= (C'_f(1 + K*) + K_top/4) t because K_top >= K_1 >= 4C'_f(1 + K*).  Hence
   s_j X'_j >= -4|a'_j|/t.
 - j < J in no S_l (l in B_np(l_*)) and not in T_B(l_*): X'_j = 0.
So the deep set of R1 Step 3 is empty.
(4) Data (R1 Step 3 with D_t = {}).  R1 Claims 3.1, 3.2 apply verbatim with C_f K* t replaced by K_top t (closeness of tau'), and give
the stated properties; the size bounds use only: sum_F A_j = 2||a'||_1/t <= 2/t, ||X'||_1 <= sum_l |tau'_l| <= (15/2) sum_l lambda_l/t <= 3/t
(sum_l lambda_l <= 1/3), so by R1 Claim 3.1(iv) t||b^+-||_1 <= 2 + 3 + 3 + 1 =: A_0 = 9; and at k = k(l): l kept,
|omega^-(k)| <= |omega^+(k)| + |tau'_l|/lambda_l <= (4 + 15/2)/t; l pinned, omega^-(k) = omega^+(k); so A_2 := 12.  Gamma_w and closeness: R1 Claim 3.2(d) with C_f K* replaced by K_top.  QED

## 2.2 Theorem RS*_inf (infinitely many bad carriers at arbitrary F).  PROVED (conditional on the rate condition (W_inf)).
Design SLD^star, N >= 1.  Let f in S_{p_N*} (F arbitrary, B possibly infinite) satisfy (H2), (H3-inf) for all bad carriers, every bad
carrier at a strict non-peak has positive gap, (ND'_{B_np(l)}) for every l, and
 (W_inf)  liminf_l  Xi_f(l)/(l 2^{l^3} Lambda°(l)) = 0,   Xi_f(l) := (4 H(l) l + 3)^{l+2} (1 + K*(l)) C_VP(l)/gamma_B(l),
where H(l) is as in Lemma W, C_VP(l) := C_0(B_np(l)) 2^{max F_0(B_np(l))}/min_{s in F_0} |a_s| (VP' constants: conditioning, location and capacity of the correction), gamma_B(l) := min of the
gaps of the bad strict non-peaks <= l and of min_m M_m.  Then f in Rec.
Proof.  As the proof of RS* (part 1.3) with Lemma W in place of Step 4', and with these changes.
(i) Levels: by (W_inf) choose l_j with Xi_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0; by the window factor Omega(l) of SLD^star,
Xi_f(l_j) Omega_K(l_j) Omega_log(l_j) T_hi(l_j) -> 0 and Xi_f(l_j) Omega_K(l_j) Omega_log(l_j)/n^w_{l_j} -> 0 (Omega_K contains 2^{s_max},
s_max and 1/delta_min, which enter K_1, the thresholds and the pigeonhole count (iii); Omega_log absorbs the logarithmic factors coming from
the pinning term 2^{J_j}, which is MULTIPLIED by the threshold factor (4H l + 3)^{l+1}, see (iv)).
(ii) Local validity: Lemma R2 with U_* = 0, A_0, A_2 = 12, gamma_B = gamma_B(l_j): its c_flat is >= c gamma_B(l_j) (c an f-constant;
c_flat <= gamma_B/(2A_2) is the only place where the bad gaps enter), and t_1 >= c' gamma_B(l_j)^2 (R2's r^4-terms); both enter n_j and the
smallness of T_j through Xi_f.
(iii) Sub-window: the inner sub-window S_j = {T_j 2^{1-i} : i <= n_j} with n_j the least n >= A K_top(l_j, J_j(n))/c_flat(l_j)
(A := 48 rho^2/(1 - rho^2)) must satisfy (S1) at all its scales: every j in T_B(l_j) cap F with j < J_j must have |a_j| outside
(theta_1 T_lo'^2, K_top T'^2) where [T_lo', T'] is the sub-window.  Each of the <= s_max(l_j) such coordinates excludes, in log_2 of the
position T', an interval of length <= n_j + log_2(K_top/theta_1) + 1; so among the first P_j := (s_max(l_j) + 2)(n_j + log_2 K_top + 2)
dyadic positions below T_hi(l_j) there is one avoiding all of them (theta_1 := 1); P_j = o(n^w_{l_j}) by (i), and the sub-window satisfies
log_2(1/T_lo') <= L_j + P_j (L_j := log_2(1/T_hi(l_j))).
(iv) Raise depth: J_j := max(J°_j, 1 + max F_0(B_np(l_j))), J°_j := min{J : mu*_J <= x_j^2}, x_j := theta_j c_flat^2 2^{-2(L_j + P_j)}/
(C_e(1 + C_VP(l_j))) [the raise footprint is <= mu*_{J} (4 sum_l lambda_l ||v_l|| + 4 sum_j Bx_B(j)) <= C mu*_J, NOT proportional to T_j, so
x_j must be compared with T_lo'^2 >= 2^{-2(L_j + P_j)}]; then 2^{J°_j} <= 2 log_2(2 log_2(1/x_j)) = O(log(L_j + P_j + log C_VP(l_j))) and
2^{1 + max F_0} <= 2 C_VP(l_j).  Since n_j, P_j, K_top depend on J_j only through the additive-then-multiplied term 2^{J_j}, the least n_j
with n_j >= A K_top(l_j, J_j)/c_flat(l_j) exists and satisfies n_j <= C Xi_f(l_j) Omega_K(l_j) [log L_j + log(Xi_f(l_j) Omega_K(l_j))]
(the bracket comes from 2^{J°_j}); since log L_j + log(Xi_f Omega_K) <= C Omega_log(l_j) for large j (L_j <= log_2(1/T_lo(l_j - 1)) + l_j^3 +
log_2(l_j Omega Lambda°), and Xi_f <= l 2^{l^3} Lambda° along the levels of (i)), we get n_j/n^w_{l_j} <= C Xi_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j))
-> 0 and K_top T_hi(l_j) <= C Xi_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0.
The raise mass is <= C 2^{-J_j} -> 0, so lambda_j -> 1 and p*(f_j - f) -> 0.
(v) Theorem 2.5 and Y3 Theorem 2.1 at f_j exactly as in part 1.3 (averaged data d-neutral, side parts cushion-compatible).  QED

## 2.3 Remarks
(a) (O4-box) is settled up to the rate condition (W_inf): box-size switching on thin shallow support is pinned (Lemma P), on the deep part
it is absorbed by a scale-free raise of mass O(2^{-J}); no box domination (BD_B), no (RR), no bounded switching.
(b) The rates in Xi_f.  K*(l): rooms of good carriers (as in (W*)); H(l): Hoffman constants of the exact cones over B(l) augmented by
pinned sets and shallow target rows (f-dependent through the d-rows q_l = eps_l q_0 val_l/sigma_m and the contact pattern on T_B(l) \ F);
C_VP(l): conditioning of the value-preserving correction for B_np(l); gamma_B(l): gaps of bad strict non-peaks.  For B finite all are
f-constants (Theorem RS*).  For B infinite they are exactly the kind of f-dependent rates that the pigeonhole / exactification machinery
of V1/V2 converts into design constants at clean sub-windows (H(l): V2 Theorem B -- minors are polynomials in VALUES; gamma_B: V1's
donor raise / status steering; C_VP: part 3 below).  So RS*_inf + (V1/V2 at clean sub-windows) is the natural route to an unconditional
statement; what that transport needs at infinite F is isolated in part 3.
(c) Simplification of RS*: Lemma W also proves RS* (B finite) without Z5's bounded-switching lemma (box-level deep raise, A_2 = 12).
# U2 part 3: item (E5) -- transporting the finite-F master theorems to infinite F; the VP rate is not needed; what remains is TUNING

Setting: the unified operator T_final of r8/U4 (D_Omega + D^{V2} + D^mu features, diagonal base), with the base replaced by mu*_s :=
2^{-2^{2^s}} (part 1.1) and Design(l) enlarged by B_mu*(l) := 2^{sigma(l)}/(mu*_{sigma(l)})^2 (the analogue of U4's fix C1); call it
T_final^*.  Clean sub-windows w = (l, i) as in V1 Theorem 2' (rate scheme (R1)-(R7) plus V2's minors), b = b(w), u = u(w),
T_lo = T_lo(w).  F arbitrary.  Labels as before.

## 3.0 Where VP entered, and why it is not needed in the transport
V3's Theorem M_inf raises an exactifying companion f^ex_j (built by Y1/V1/V2 at f) and then needs VP to keep the values of the GROWING set
L_0(j) of kept carriers, whose conditioning C_0(j) is an f-dependent rate (V3-ref Section 5).  Reverse the order: raise FIRST (deep, box
level, Lemma W of part 2), then exactify at the raised row.  The deep raise moves every value by O(eps_e) with eps_e <= C mu*_J psi(J),
which can be made <= b(w)^2 by the choice of J (2^J = O(log log(1/b(w))), absorbed by any window).  Then:

Lemma DR-inf (a deep raise preserves the clean classification).  PROVED.  Let w be clean for f, J with C mu*_J psi(J) <= b(w)^2 Phi_min(l)
(Phi_min(l) := min_{l'' <= l} Phi_{l''}, a design quantity), and f^r the deep box-level raise of f beyond J (part 2, (R), WITHOUT VP).  Then every
rate object of level l in (R1)-(R5), (R7) and every minor of V2's systems changes by at most C Design(l) b(w)^2 <= b(w); in particular every
tiny rate of f is <= 2b at f^r and every robust rate is >= u - b >= u/2 at f^r.  (R6) (shift costs, LP values) is continuous in the same data
with a design modulus: SKETCH.
Proof.  The raise does not change z, F, K, J, so (R1), (R2) are unchanged.  ||e^r - e|| <= 2||U^*Delta a||/nu <= C mu*_J psi(J) (V3 Lemma 2.1(b));
so |u_k(zhat^r) - u_k(zhat)| <= ||U^*u_k|| ||e^r - e|| <= C mu*_J psi(J) for every carrier, and the block scalars A_m, theta_m, M_m, C_m move by
<= C_f mu*_J psi(J) (V3 Lemma 2.2).  (R3), (R4) are |val|m/(Phi theta) (Lipschitz with constant <= C m/(Phi_min theta_min)); (R5) is a linear
form in values divided by Phi_max >= Phi_min; (R7) singular values move by at most the operator-norm change (Weyl); minors are polynomials of
bounded degree in values with design-bounded coefficients.  All constants are design quantities of level l times f-constants (theta_min,
nu); the choice of J absorbs them.  QED
Consequence.  VP (and (ND')) is not needed for the deep raise: the classification at w survives at f^r with factors 2, and all subsequent
exactification is done AT f^r, with f^r's own values.  The new requirement is that the exactifying moves of V1/V2 be available at f^r,
whose support is infinite.

## 3.1 What the finite-F assembly uses that depends on F (inspection of V1 Sections 3-4 and V2 Theorem B)
 (i)   (C1) closes rooms on S^nat_{l''} = S_{l''} \ (F cup T(l)) by z-moves: off F, unaffected by F infinite.
 (ii)  (C2) closes target rooms on T(l) \ F: off F, unaffected.
 (iii) (C3) donor raise: a z-move or a BANK at s_m := min(S_{c_m} cap (s_max(l), infinity)) of a robust-margin peak c_m (Lemma D);
       Lemma B (masses OFF the support) makes the bank private at first order.  At infinite F, s_m may lie in F.
 (iv)  (C4) and V2's Lojasiewicz tuning: Lemma TU with banks at j'_{l''} := min(S_{l''} cap (s_max(L), infinity)) and pulls at far
       j_{l''} in S_{l''} with v(j) in [eta, 2^G eta]; it assumes F^2 finite and z = eps_{l''} (contacts) on S_{l''} \ [1, s_max(L)].
       At infinite F, j' and the j may lie in F.
 (v)   Transplant (Prop TR), Theorem E'': the data's switching must be exact; on F it must be cushion-compatible: this is Lemma W
       (part 2) -- Lemma P pins kept carriers at shallow thin coordinates, the deep raise covers the rest; pinned carriers are
       removed by the threshold pigeonhole (faces of the pattern cones: V2's minors include all subsystems), shallow thin target
       coordinates in F become contact rows (a pattern of V1's G**, i.e. arbitrary contact patterns on T(l)).
 (vi)  Final step: V3 Theorem 2.5 + Y3 Theorem 2.1 at the companion (any F).
Items (i), (ii), (v), (vi) are available at infinite F (parts 1-2 and V3).  The ONLY new issue is (iii)-(iv): PRIVATE TWO-SIDED VALUE
TUNING for carriers whose design-depth signature coordinates lie in F ("support-swallowed carriers").

## 3.2 Lemma TR-inf (private tuning resources at infinite F).  PROVED in cases (a)-(c').
Let w be clean (factor 2) for the current row f° (forced data a°, z°, F° possibly infinite), L >= l a level, L_0 a finite set of carriers
<= L, eta := |x|_inf <= Design(L) b(w) the required increments x in R^{L_0}.  For l'' in L_0 consider the following RESOURCES, where
j'_{l''} := min(S_{l''} cap (s_max(L), infinity)) (design depth, j' <= sigma(L)) and d(L) := sigma(L) + 2^{L+2} (the first three coordinates
of each S_{l''} beyond s_max(L) lie in [1, d(L)]):
 (a)  [contact resources, V1]  j'_{l''} notin F° with z°_{j'} = eps_{l''}, and pull coordinates j in S_{l''} \ F° with v(j) in [eta, 2^G eta] and
      z° = eps_{l''} there;
 (a') [convertible support] as (a), except that j' in F° with |a°_{j'}| <= b(w), or a pull coordinate j in F° with |a°_j| <= theta b(w)^{1/2}/|L_0|
      (b(w)^{1/2} = T_lo^2/(l Design)^{1/2}), in each case with support sign s_j = eps_{l''}: LOWER these coordinates to contacts of sign
      s_j first (cost <= |a°_j|, zeroth order).  (With the opposite sign the roles of bank and pull are exchanged -- a bank at a contact of
      sign -eps lowers eps.val, a pull there raises it -- and Lemma TU's fixed point is the same with x replaced by -x on that carrier.)
 (c)  [robust Hilbert pair] two coordinates s < s' in S_{l''} cap F° cap (s_max(L), d(L)] with |a°_s|, |a°_{s'}| >= u and
      |1 - rho_{s'}/rho_s| >= u, rho_s := a°_s/v_{l''}(s);
 (c') [robust coordinate + anchor] one coordinate s' in S_{l''} cap F° cap (s_max(L), d(L)] with |a°_{s'}| >= u, together with a GLOBAL
      ANCHOR s_0 in F°, s_0 <= s_max(L) + 1 <= every tuned coordinate, with |a°_{s_0}| >= u and u_k(s_0) = 0 for every k in L_0 tuned by
      (c) or (c').
If every l'' in L_0 has one of (a), (a'), (c), (c'), then there is a row f^# (moves only at the listed coordinates) with
  val^#_{l''} = val°_{l''} + x_{l''} EXACTLY (l'' in L_0),  |u_k(zhat^#) - u_k(zhat°)| <= C_T eta^2 + (pull/bank side effects of V1 Lemma TU(b))
  for coarse k notin L_0 not touched by an anchor, and <= C_T eta for coarse k whose vector meets an anchor (these are re-tuned or robust),
  p*(f^# - f°) <= C_T eta log(e/eta) + (lowered masses <= |L_0| theta b^{1/2} + b),
with C_T = (f-constant) x Design(L)^C u^{-C}.
Proof.  Lemma B of V1 (masses off the support) is the only place where (a) needs j', j notin F°; after the lowering in (a') the coordinates
are contacts, so (a') reduces to (a) (Lemma TU of V1, verbatim, with s_j := mu*_j; its efficiency constant s'^2 v' >= (mu*_{sigma(L)})^2
2^{-sigma(L)} delta_min/2 is >= Design(L)^{-1/6} by the enlarged Design).  The lowering of j (|a°_j| small) is a "monotone move" of the
opposite kind: its transfer error is <= 2|a°_j| (zeroth order, part 1 and V3 Lemma 2.3's remark), and it changes e by
<= 2 mu*_j |a°_j|/nu, hence every value by <= C mu*_j |a°_j| <= C b^{1/2} (first order but tiny; the exact tuning below is computed at the
lowered row, so this change is absorbed).
Case (c) (support coordinates, no contact): for a move Delta at s in F°, with diagonal U,
   Delta val_k = (mu*_s^2/nu)(u_k(s) - gamma_k a°_s/nu^2) Delta + O(Delta^2),   gamma_k := <U^*u_k, U^*a°>   (V3 Lemma VP's Lambda),
i.e. a PRIVATE part (only k = l'' has u_k(s) != 0 among coarse carriers, s being beyond s_max(L) and in S_{l''}) and a COMMON part along the
fixed vector gamma, proportional to alpha_s Delta, alpha_s := mu*_s^2 a°_s/nu^2.  Take the pair (s, s') with Delta' := -alpha_s Delta/alpha_{s'}:
the common parts cancel exactly at first order.  Let the DEEPER coordinate s' do the work: Delta = -(alpha_{s'}/alpha_s) Delta', so
|Delta| = (mu*_{s'}/mu*_s)^2 (|a°_{s'}|/|a°_s|) |Delta'| <= u^{-1}|Delta'| (mu* is decreasing), and the private effect is
(mu*_{s'}^2 v(s')/nu)(1 - rho_{s'}/rho_s) Delta', of modulus >= c (mu*_{d(L)})^2 2^{-d(L)} delta_min(L) u |Delta'| >= Design(L)^{-1} u |Delta'|
(Design(L) contains (mu*_{d(L)})^{-2} 2^{d(L)}/delta_min(L)).  Both signs of Delta' are allowed: a same-sign raise is unlimited, a lowering
is limited by |a°|/2 >= u/2, and |Delta'|, |Delta| <= C Design u^{-2} eta << u for eta <= Design b.  (Pairing with a deeper partner the
other way round would require |Delta'| ~ (mu*_s/mu*_{s'})^2 |Delta|, astronomically large: the order matters for the base mu*.)  Second-order cross effects are O(Design^2 u^{-4} eta^2); the
simultaneous solution for all l'' (pairs are private to distinct carriers) is a fixed point exactly as in Lemma TU Step 2 (contraction
constant <= C Design^C u^{-C} eta << 1).  Cost: raises cost the footprint (V3 Lemma 2.3) mu*|Delta|; lowerings cost 2|Delta| (zeroth order);
both <= C Design u^{-2} eta << T_lo^2.
Case (c'): the anchor move Delta_0 at s_0 has private effects only on carriers whose vectors meet s_0 (not in the (c)/(c') part of L_0;
those in L_0 are re-tuned by their own resources in the same fixed point, the others are robust and move by <= C_T eta << u) and a
common part alpha_{s_0} Delta_0 gamma; put Delta_0 := -sum_{(c')} alpha_{s'} Delta_{s'}/alpha_{s_0}; since s_0 is not deeper than any tuned
s', |Delta_0| <= sum (mu*_{s'}/mu*_{s_0})^2 (|a°_{s'}|/|a°_{s_0}|)|Delta_{s'}| <= C |L_0| Design u^{-3} eta.  The
private effects mu*_s^2 v(s) Delta_s/nu are then free of common terms, and the rest is as in case (c).  QED

## 3.3 The residual of (E5) (precise) and its relation to (ND')
A carrier l'' in L_0 has NO resource of 3.2 iff, at the window w:
 (N1) every coordinate of S_{l''} beyond s_max(L) with v(j) >= eta (in particular j'_{l''}) lies in F° with |a°_j| > theta b^{1/2}/|L_0|
      (support-swallowed and thick down to the pull depth; no contact/free coordinate at usable depth), and
 (N2) the design-depth coordinates of S_{l''} cap F° beyond s_max(L) have pairwise rho-spread < u ("nearly proportional profile",
      a° ~ c_{l''} v_{l''} there), and there is no robust anchor avoiding the vectors of all such carriers.
Making the spreads |1 - rho_s/rho_{s'}| (s, s' among the first three coordinates of S_{l''} beyond s_max(l), l'' <= l) and the moduli |a_s|
(s in F cap [1, d(l)]) RATE OBJECTS of level l (finitely many per level, N-free, design-indexed), a clean sub-window makes each of them tiny
or robust; robust gives (c) or (c'); tiny |a_s| gives (a').  What remains is: tiny spread for all pairs and no anchor.  Exact version:
a° = c_{l''} v_{l''} on the shallow part of S_{l''} cap F for the carriers of a set L_d, and F cap [1, d(l)] covered by the vectors of L_d.
Then the only first-order resource for L_d on F is the family of columns (mu*^2 v/nu)(e_{l''} - (c_{l''}/nu^2) gamma), whose span is all of
R^{L_d} iff the Sherman-Morrison denominator 1 - sum_{L_d} c_{l''} gamma_{l''}/nu^2 is nonzero; V3's Remark to Lemma VP identifies its
vanishing with (ND') failure (a|_F in span{u_{l''}|_F}), on which sum c val drifts only at second order.  So the residual of (E5) is the
"near-(ND')" rate condition
 (NDN_w)  at every clean w of all large levels, some set L_d of kept carriers satisfies (N1), (N2) and |1 - sum_{L_d} c gamma/nu^2| <= b(w)
(the last quantity is again a rate object, so its robust case is covered by the Sherman-Morrison inverse with constant <= Design/u).
Remark (OPEN).  The coordinates tested in (N2) are the first ones of S_{l''} beyond s_max(L), which move deeper as L grows; so (N2) at
infinitely many levels does not force global proportionality of a on S_{l''} cap F (a profile that is nearly proportional on each tested
triple and thick at the pull depth is possible).  Whether (NDN_w) at all large levels can coexist with a mate that is not recovered by
other means is open; it is a condition on a only, of (ND')-near-degeneracy type, and is not generic (Baire: it fails after an arbitrarily
small perturbation of a on the tested coordinates, but such a perturbation is not available inside Lemma Z without a transfer argument).

Remark (where (NDN) leads).  Tuning is needed only to keep EXACT zeros of objects that are tiny at f (for objects built from FIXED
carriers, "tiny at all large levels" means "exactly zero at f", because b(w) -> 0; the companion moves -- deep raise, (C1)-(C3) -- perturb
them and the tuning restores them).  For a FIXED carrier the efficiency |1 - gamma_k rho_s/nu^2| of a shallow support coordinate s is a fixed
number, and it vanishes for every s in S_k cap F only if rho is constant (= nu^2/gamma_k) on S_k cap F; so for fixed carriers (NDN) is an
f-constant issue except in that exactly proportional case.  The rate character of (NDN) comes from carriers entering L_d at growing levels.
Alternatively, a near-neutral (NDN) carrier can be kept in NON-d-neutral data (Delta d_m = q_k tau'_k), which V2's Theorems E^>=, E^SC accept
when the blocks with Delta d_m < 0 satisfy (SC) at the companion: so (NDN) is contained in the same "(SC) at companions" problem as V2's
(C*-2) (part 4.1(c)).

## 3.4 Theorem M-inf (transport of Master Theorem III' to infinite F).  SKETCH (all ingredients PROVED except the items flagged).
For T_final^* and every N: a first row f with F INFINITE belongs to Rec_N unless, at all but finitely many levels, every clean sub-window
w has (C*_w) [V2-ref's coherent shift resonance, read at the deep-raised row f^r] or (NDN_w) [3.3] or a violation of (H2) or of the
(H3-inf)-type exclusions [bad degenerate peaks with the swallowing sign].
Route.  At a clean w of a level where (C*_w), (NDN_w) fail: (1) deep box-level raise f -> f^r beyond J (Lemma DR-inf; no VP);
(2) at f^r, V1's moves (C1)-(C3) and V2's Lojasiewicz tuning, with banks/pulls replaced by Lemma TR-inf where the coordinates lie in F;
(3) at the companion f^#, exact d-neutral window data from the transplant, cushion-compatible on F by Lemma W of part 2 (Lemma P +
pigeonholes; the shallow thin target coordinates are contact rows of the pattern); (4) V3 Theorem 2.5 (raise transfer: eps' = footprint
of the deep raise + V1's companion cost o(T_lo^2)) and Y3 Theorem 2.1 at f^# (infinite support allowed; (CS-side) from cushion
compatibility).
Flagged (not written line by line): (R6) continuity under the deep raise; V1 Lemma ST (status stability) with Lemma TR-inf's anchor side
effects (C_T eta on robust carriers: harmless by Lemma RR); V2 Theorem B with the extra pattern rows of Lemma W (pinned faces, contact rows on
shallow thin targets) -- these are subsystems of V2's systems, whose minors V2 already lists; window arithmetic (n(w) absorbs (W_inf)'s
rates because every f-dependent factor is now a rate object of the level or an f-constant^{l^2}).
So, modulo the flagged inspection items: Lemma Z at infinite F reduces to the finite-F residual (C*) (read at deep-raised rows) plus the
(ND')-type residual (NDN) of 3.3 plus the block exclusions shared with finite F.
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

# U2 part 5: numerics (evidence only) and what remains

## 5. Numerics: r8/U2_work/pair_tuning_check.py (mpmath, 60 digits)
Finite model of the value map val_k = u_k(zhat), zhat = z + U e, e = U^* a/||U^* a||, z = sgn a on F, diagonal base mu_s = 2^{-(s+1)^{1.5}},
14 support coordinates, one owner carrier with signature on {5, 7, 9}, six other carriers vanishing there.  Pair move at s = 5 < s' = 9
with Delta = -(alpha_{s'}/alpha_s) Delta' (Lemma TR-inf (c)):
  Delta' = +-1e-6: owner change matches the predicted (mu_{s'}^2 v(s')/nu)(1 - rho_{s'}/rho_s) Delta' to relative error 1.5e-14;
                   maximal change of the other carriers 3.4e-31 (second order);
  Delta' = +-1e-9: relative error 1.5e-17; others 3.4e-37 (scales as Delta'^2).
A single unpaired move at s' changes the other carriers by 2.4e-25 >> the owner's own change 3.6e-27: the common term dominates for a
thick coordinate, which is why single support moves are not admissible tuning resources (part 3.2, 4.3(a)).

## 6. What remains open after U2 (designed norm T_final^*, finite I)
Density of NA((c_0,p_N), l_2^2), Lemma Z, and density for Martin's p remain OPEN for every admissible T.  For INFINITE base support:
 (i)   PROVED: RS-type rows (finitely many exactly swallowed bad carriers, ANY support profile, (W*), (H2), (H3-inf); no (RR), no (ND')).
 (ii)  PROVED conditionally: infinitely many bad carriers under (W_inf) (rates: rooms, Hoffman constants of growing exact cones, VP
       constants, gaps of bad strict non-peaks).  To make it unconditional one runs the V1/V2 clean-sub-window machinery at the deep-raised
       row; that is item (iii).
 (iii) SKETCH (Theorem M-inf): transport of Master Theorem III' to infinite F.  Flagged inspection items: continuity of the shift-cost rate
       objects (R6) under the deep raise; V1 Lemma ST with the anchor side effects of Lemma TR-inf; V2 Theorem B with the extra pattern rows
       of Lemma W (pinned faces, contact rows on shallow thin targets); window arithmetic.
 (iv)  OPEN residuals specific to infinite F: (NDN) (near-(ND') degeneracy of a on the shallow signature coordinates of carriers that
       need tuning, together with thick support down to the pull depth) and its alternative route "(SC) at companions"; the RS*_inf corner
       case where targets of infinitely many bad carriers cover the initial parts of kernel signature sets (part 4.2(b)); degenerate
       swallowing-sign bad peaks when no donor of the block has a tuning resource (4.3(c)); transported fixed non-d-neutral data (4.1(d),
       not needed).
 (v)   Shared with finite F: (C*) (near-exact coherent shift resonance) and its gap (C*-2) "(SC) at companions"; failure of (H2).
Leaning: positive.  Every infinite-support mechanism examined is either harmless after the deep raise (thin, critical, super-critical,
mu-thin, box-size switching), pinned by the mate's own flip budget (thin shallow coordinates), cushion-dominated ((ND') failure), or a rate
phenomenon of the same "exactness versus scale" type as at finite F.
