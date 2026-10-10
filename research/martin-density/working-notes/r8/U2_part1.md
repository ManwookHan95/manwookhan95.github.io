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
