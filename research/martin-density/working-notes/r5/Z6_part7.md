# Z6 part 7: task (b) — a modified design, and what it buys

## 7.1 Design D'' (lengthened windows) and survival of Section 8   [PROVED]
Keep Definition SLD except (D1): after c_l, y_l, u_l (all l'' <= l) are fixed, put
  Xi(l) := H_comb(l) * prod_{l'' <= l} (1 + 8 N 2^{m(l'')+k(l'')} / c_{l''}) * prod_{l'' <= l} (1 + 1/mu_des(l'')),
  n^w_l := ceil( l 2^{l^3} Lambda°(l) Xi(l) ),  T_hi(l) := min{ T_lo(l-1), 2^{-l^3}/(l Lambda°(l) Xi(l)) },
  T_lo(l) := 2^{-n^w_l} T_hi(l),  c_{l+1} := min{ c_l/4, T_lo(l)^3 },
where H_comb(l) is the combinatorial Hoffman constant of 7.2 and mu_des(l'') := min over l' <= l'' of the design masses
m_{l'} defined in 7.2 (both are functions of the design data with index <= l only).  Xi(l) >= 1.
Survival: (P1),(P2) are unchanged; (P3) becomes T_hi(l) 2^{l^3} Lambda°(l) Xi(l) <= 1/l, n^w_l >= l 2^{l^3} Lambda°(l) Xi(l),
T_hi(l+1) <= T_lo(l), which implies the old (P3).  Every proof in Section 8 uses only (T-a)-(T-d), (P1), (P2) and the old
(P3) (as stated after Theorem SLD), so Theorems SLD, R0, reductionZ, Bstar, Bpm, S, and Theorem C (part 4) hold verbatim
for D''.  Admissibility: (T-b),(T-c) proof unchanged (it uses only allowedness (b) and c_{l+1} <= c_l/4); (T-d) unchanged.

## 7.2 Combinatorial Hoffman constants are design quantities   [PROVED]
Fix l_*.  A PATTERN P consists of: a set B_* subset {1..l_*} (bad carriers) with signs eps_l, a partition of B_* into
KEPT (switchable) and DROPPED carriers, the finite set T_0 := union_{l in B_*} supp y_l, and for each j in T_0 a label
in {F, +contact, -contact, room}.  For a pattern let A_P be the matrix of the linear system in tau in R^{B_*}:
  (con) z_j L_j(tau) >= 0 (j labelled +-contact, z_j its sign),   (room) L_j(tau) = 0 (j labelled room),
  (sgn) tau_l >= 0 (l kept),   (drop) tau_l = 0 (l dropped),   (box) |tau_l| <= b_l,
with L_j(tau) := sum_{l in B_*} eps_l tau_l u_l(j)  (u_l(j) design values: target values and, for j in a signature set
S_{l''}, l'' <= l_*, signature values).  The polyhedron Z_P(b) := {tau : A_P tau <= (0,...,0,b,b)} is nonempty (0).
By Hoffman's theorem there is H(A_P) < infinity with dist_1(tau, Z_P(b)) <= H(A_P) ||(A_P tau - rhs)_+||_1 for all tau
and all b >= 0 (the constant depends on the matrix only).  There are finitely many patterns with index <= l_*, so
  H_comb(l_*) := max_P H(A_P)
is a function of the design data with index <= l_* only.  (F enters only through F cap T_0, finitely many choices; the
signature mass outside T_0 and F, m_l := ||v_l 1_{S_l \ (F cup T_0)}||_1, is positive and depends on F only for the
finitely many l with S_l cap F nonempty; mu_des uses the F-free version, the finitely many exceptions give a constant.)

## 7.3 THEOREM E (design D''): swallowing with arbitrary combinatorics   [PROVED modulo the verbatim parts listed]
Let T be the design D'', N >= 1, f in S_{p*} with F finite.  Assume:
 (E1) exact swallowing: every carrier either is good with r*_l > 0 (S*_l := S_l \ (F cup bad targets)) or has r_l = 0;
 (E2) target rooms: gamma_T := inf{1 - |z_j| : j in union_{l bad} supp y_l, j notin F cup K} > 0;
 (E3) blocks: each block m is either COMPENSATED (it contains two bad resonant strict non-peaks l^+_m, l^-_m with
      q > 0 > q and gaps >= gamma_B) or UNCOMPENSATED (all bad strict non-peaks with q != 0 and all bad degenerate
      peaks with varsigma eps = +1 have the same sign of q; here q_l := eps_l Phi w(k_l)/(mC) for every carrier);
 (E4) in compensated blocks: kept bad carriers are resonant strict non-peaks (q >= 0 any gap; q < 0 gap >= gamma_B),
      d-neutral or not; bad degenerate peaks of swallowing type absent;
 (E5) (H2') in every block (3.2);
 (W_E) liminf_l [ Lambda*_f(l) + K_P(l) + K_nn(l) + 1/gamma_T ] / ( l 2^{l^3} Lambda°(l) ) = 0, where the
      RELATIVE rates are  K_P(l) := max{ Phi_{l'}/mu_{l'} : l' <= l bad non-degenerate peak }  and
      K_nn(l) := max{ Phi_{l'}/|q_{l'}| : l' <= l bad strict non-peak of an uncompensated block, q != 0, gap > M/2 }
      (Phi_{l'} := Phi_{m(l')}(k(l'))); the design factor sum_{l'<=l} 1/Phi_{l'} is absorbed in Xi(l).
Then f in Rec.  No condition (H1), no resonance of dropped carriers, no bound on the number of bad carriers, any contact
set; in particular MAXIMAL CONTACT z = eps off F is covered as soon as (E3)-(E5) and (W_E) hold ((E2) is vacuous there:
no roomy target coordinates; (E5) holds by 3.2 since peaks of both signs exist).
Proof (changes to Theorem S/C).  Window l_*, t in W(l_*), two-sided decomposition.
 (1) Good carriers: Lemma modswallow(a) with S*_l: sum_good |Delta theta| <= K_* t.  Shift: 3.2 with (tau)_- of the two
     chosen bad peaks <= c(tau)/(2 m_l) (budget on S_l \ (F cup T_0), where only u_l lives): |Delta d_m| M <= K_d t.
 (2) Drop rows.  Bad non-degenerate peaks: |tau_l| <= t/mu_l + lambda_l K_d t (Step 2 of part 4).  Uncompensated block:
     Proposition 3.4 applied to the same-sign set Sigma_m (d-neutral carriers contribute 0 to (didentity), peaks by K_P,
     fine carriers t^5, good by K_*) gives sum_{Sigma_m} |q_l| (tau_l)_{+-} <= A = O(K t), hence |tau_l| <= A/|q_l| + c(tau)/(2 m_l);
     for gap <= M/2 (and for degenerate peaks of swallowing type) |q_l| >= M Phi_l/(2 m C_m) >= Phi_l/(4m 2^{-m}) so
     1/|q_l| <= 8 N 2^{m+k}/c_l (part of Xi); for gap > M/2 the sum is K_nn.
 (3) Violations of the other rows: (con) (z_j L_j)_- <= c(tau)/2, (room) |L_j| <= c(tau)/gamma_T, (sgn) (tau_l)_- <=
     c(tau)/(2 m_l), (box) none (|tau_l| <= 6 lambda_l/t <= b_l := 12 lambda_l/t), where c(tau) := sum_{j notin F}
     phi_{z_j}(L_j(tau)) <= t/q_0 + 2 K_* t (Lemma switchbudget, pinned good part removed as in Lemma exactswitch).
 (4) Hoffman (7.2): tau' in Z_P(b) with ||tau - tau'||_1 <= H_comb(l_*) * C_f (K_* + K_P + K_nn + 1/gamma_T + Xi_0(l_*)) t,
     Xi_0 the design part of (2).  In compensated blocks fix d exactly by adding to tau'_{l^pm_m} (Theorem C, Step 4):
     the rows (con),(room),(sgn) stay satisfied because resonant compensators are z-signed and vanish off F cup K (the
     cone is upward closed in their directions); their box rows may be exceeded by O(K t), harmless (fixed lambda).
     Uncompensated blocks: all their q != 0 carriers are dropped, so sum q tau' = 0 there.  Hence the projected switching
     is an EXACT d-neutral resonance: V' := sum eps tau' u 1_{F^c} is z-signed on K and vanishes off F cup K.
 (5) Window two-piece data: Lemma windowtwopiece with the box rows giving tau'_l/lambda_l <= 12/t (A_2 fixed), the gap
     conditions of (E4) and part 4.2 for the one-sided transfer expansion; (b),(c) with the error of (4).
 (6) Windowed averaging + Corollary D1 exactly as in Theorem S.  The window constant is
     K_E(l_*) := H_comb(l_*) C_f (K_* + (sum 1/Phi)(K_P + K_nn) + 1/gamma_T + Xi_0(l_*))
              <= C_f (Lambda*_f + K_P + K_nn + 1/gamma_T + 1) Xi(l_*)   (Xi >= H_comb Xi_0 sum_{l'<=l} 1/Phi_{l'}),
     and with n^w_l >= l 2^{l^3} Lambda°(l) Xi(l), T_hi(l) <= 2^{-l^3}/(l Lambda°(l) Xi(l)), (W_E) gives
     K_E(l_j) T_hi(l_j) -> 0 and n^w_{l_j}/K_E(l_j) -> infinity along a subsequence.  QED
Remarks.  (a) The Hoffman obstruction of Remark rem:S(c) ("Hoffman constants of growing finite systems not controlled
by the window lengths") is removed BY DESIGN for everything combinatorial (targets, slaving, contact patterns, which
carriers are kept or dropped); the d-row is never put into a Hoffman system (compensation is explicit, dropping uses 3.4).
(b) What remains f-dependent in (W_E): rooms of good signature sets (Lambda*), RELATIVE margins mu/Phi of swallowed peaks
(K_P), RELATIVE d-coefficients |q|/Phi of nearly neutral non-peaks in uncompensated blocks (K_nn), rooms at bad target
coordinates (gamma_T).  All are RATES of near-resources (they fail only if they decay faster than 2^{-l^3}/Lambda°(l));
nothing combinatorial is left.  For a generic first row (e.g. maximal contact with generic a: relative margins and
relative d-coefficients of the first l carriers are >= l^{-C} with probability one in natural random models) (W_E)
holds: HEURISTIC.  (c) Structural cases not covered by Theorem E: blocks that are neither compensated nor uncompensated
(mixed-sign d-coupling without a resonant compensator pair: the d-row would enter a Hoffman system with f-dependent
coefficients), swallowing-type degenerate peaks in compensated blocks (extended two-piece data needed, cf. part 8), q < 0
kept carriers with gaps -> 0 in compensated blocks, and infinite F.

## 7.4 Sign-alternating signatures   [PROVED]
Replace h_l by h^alt_l := sum_i (-1)^i 2^{-s_i} e*_{s_i} (s_0 < s_1 < ... the enumeration of S_l), with s_1 = s_0 + 1.
Theorem SLD and Section 8 hold verbatim with v_l signed (r_l := ||v_l 1_{S_l\F}||_1 - |<v_l 1_{S_l\F}, z>| as in the
note; Lemma phicalc(d) applied to |v_l(s)| and z_s sgn v_l(s)).  If S_l cap F = empty and z = eps constant on S_l, then
r_l >= ||v_l||_1 (1 - |sum_i (-1)^i 2^{-s_i}|/sum_i 2^{-s_i}) >= ||v_l||_1/2 (since s_1 = s_0+1).  Hence every first
row with F finite and z constant (= eps) on all but finitely many S_l satisfies (W^pm) and lies in R_0^pm subset Rec.
In particular the literal model case (O3) "z = eps off F" disappears.  Swallowing now means z = eps_l sgn(h^alt_l) on
S_l \ F; Remark rem:nodesign applies unchanged (z := sgn u_l), so this is a re-labelling of the hard set, not a removal.
