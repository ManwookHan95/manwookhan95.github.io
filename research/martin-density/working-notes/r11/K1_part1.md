# K1 part 1 (Round 11): item (O-a) -- cushion domination of route-V data at a deep-raised companion (Q2 Proposition 3.2)

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Sources: r10/Q1_notes.md (route V, Lemma CM^tr, Prop. BR, Lemma PM, Thm C^tr) with
Q1-refa P1-P8 and Q1-refb P-LIP, P-R, P-HOLD; r10/Q2_notes.md (Thm UE^inf, E^{eng,RT,inf}, Lemma 3.1) with Q2-refa precisions;
r8/U2_notes.md 1.2 (Lemma P), 2.1 (Lemma W), 3.0 (Lemma DR-inf) with U2-ref fixes (s1), G1, W1; r5/Z5_ref_notes.md Section 2 (Theorem R1,
Claim 3.1 = the "deep assignment"); r8/U1_notes.md 2.1-2.4, 4.1-4.7 with U1-ref 3-7; r9/X2_notes.md 3.1, 5.1 with X2-ref 4 (Lemma CM').

## 1.0 Setting
DESIGN.  T_fin^* := T_fin of Q1 (option (a)) over the doubly exponential diagonal base mu*_s := 2^{-2^{2^s}} (U2 1.1), with Design(L)
containing B_mu*(L) := 2^{d(L)}/(delta_min(L) (mu*_{d(L)})^2), d(L) := sigma(L) + 6 * 2^{L+1} (U2-ref (s1), enlarged to cover the six near
coordinates of part 2), and with the following objects in the
rate scheme omega(L) (bookkeeping item (O-d), assumed here and listed again in part 4):
 (R-mod) the moduli |a_s|, s in [1, d(L)] (with |a_s| := 0 for s notin F);
 (R-pat) the minors/cofactor polynomials of the ENLARGED class cones of 1.3 below (patterns in which coordinates of T(L) cap F may carry a
         contact row), for all patterns and classes of level L;
 (R-lev) the lever objects of part 2.
Every window theorem uses the base only through B_mu* (U2 Remark after 1.1, U4 Lemma GW); T_fin^* is N-free.
ROW.  N >= 1, f in S_{p_N*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu), F = supp a ARBITRARY; s_j := sgn a_j (j in F); g in C(f),
rho in (0,1); l_f = l_f(f, N, g, rho) as in Q1 3.1 (all f-constants absorbed, companions in the ball of Lemma M2^inf).
WINDOW.  L >= l_f a main stage, w a clean sub-window of L for f; T := T_lo(w), b := b(w), u := u(w), D := D(L); coarse carriers = stages <= L,
fine carriers = stages > L; T(L) := union of the supports of the coarse targets, s_max(L) := max T(L); sum_{l > L} lambda_l <= C c_{L+1} <=
C b^2 <= C T^8 ((W2) and b <= T^4).
SWITCHING VECTOR.  For route-V data with switching Domega supported in Omega (= all coarse strict non-peaks of the companion), U1 Lemma
1.1(a) gives V := V(Domega) = sum_l c_l u_l over ALL carriers, with c_l = gamma_l (l in Omega), c_k = -Delta''_m lambda_k vs_k for a coarse
peak k of block m (primed shift convention, U1 2.1), and c_k = -Delta''_m lambda_k w(k)/M for fine k.  V_c := sum_{l <= L} c_l u_l (coarse
part), V_f := V - V_c (fine part).

## 1.1 Lemma K1.1 (route V needs no shift normalization).  PROVED.
In route V (Q1 Lemma CM^tr Steps A-B, Proposition BR, Lemma PM, Lemma S2c^tr, Theorem C^tr, Master Theorem VI; X2-ref Lemma CM') the cube
pigeonhole and the normalization increment incr(t) of U1 Proposition 2.2(c)-(e) can be omitted: if for every t of a class set S the data
are built from the PROJECTED class data (Delta'(t), gamma(t)) in Gamma^#(kappa, a) (U1 2.2(a), (b), 2.3, U1-ref 4.5) without increment, then
every conclusion of Lemma CM^tr (a)-(f) and of Proposition BR holds, with (c) improved to sqrt(Gamma^#_w(b^-, omega^-)) <= sqrt(Gamma^#_w(B_-,
Theta_-)) + K t (no C_f p eps term), and Theorem C^tr holds with D_cls(w) replaced by the class count D_cl(w) := (J_Om + 1) 3^{J_Om},
J_Om := |Omega| + N (the pattern is determined by f at w and is not pigeonholed).
Proof.  We list every place where route V could use that all scales of S carry the same shift, and check that none does.
 (1) Step B (X2-ref CM' step (2'), Q1 2.2 STEP B) [moot after Lemma K1.S, which omits Step B; recorded for finite-F readers].  Owners and their
     z-assignments: (a) Omega_act carriers own their far signature sets with
     z = sgn(gamma_l v_l) = eps_l; (b) coarse peaks of active blocks with z = sgn(-Delta''_m vs u) = -sigma_m vs sgn u; (d) fine carriers by
     the recursion varsigma_k := sgn Y_k, z := varsigma_k sgn u_k (negative blocks) or -varsigma_k sgn u_k (positive blocks).  Every rule
     uses only the SIGNS sigma_m = sgn Delta''_m and eps_l, which are fixed by the class (U1 2.3: the class records the active set and the
     signs; U1-ref 4.4: sgn Delta'_m is constant on the class cone), and Y_k, which is computed from coordinates fixed before k and does not
     involve the data.  Dominance (U1 Lemma 4.2) is stated "for every Delta'' in the class (active |Delta''_m| >= A_2 K T/2, |Delta''| <= C_f)
     and every gamma(t) of the class"; U1-ref 7 (owners inside absorber blocks) uses only the least absorber entry.  The only construction
     of U1 that is built for ONE shift value is the Schauder completion of configuration (ii) (U1 Lemma 4.4, route X); route V replaces it by
     anti-alignment with tolerated violations (X2 Lemma CM, proof of Theorem C_mix: "no Schauder completion is needed").
 (2) True versus reference shift (U1 Lemma 4.6).  For each t separately, (X3) at f^# and at the realized point (u', kappa') give
     Delta''_m(t) kappa^#_m = sum_{Omega_act,m} u_l(zhat^#) gamma_l(t) and Delta'_m(t) kappa'_m = sum u'_l gamma_l(t); with u^# = u' on Omega_act
     after Step A (exact re-realization) Delta''(t) = Delta'(t) kappa'/kappa^#.  The bound |Delta'' - Delta'| <= C_f Design c_{L+R_cl+1} and the
     trace-correction estimate (U1 Lemma 4.6(b)) are per scale and unchanged; the signs and activity are kept (U1 Lemma 4.6(c)).
 (3) Kind [3] (Q1 2.2 proof of (c)(ii), X1 2.2(iii), U1-ref 4.1): "every point of the cone is inward at f^# with the true shift"; the
     increment was one more point of the cone.  Without it the data are points of the cone.
 (4) Window family (X2 3.1, Q2 2.2): (U1)-(U7) are conditions on each piece separately; (U5) concerns I_- := {m : Delta_{i,m} < 0 for some i},
     which is the set of negative active blocks of the class; (U7) is a per-piece bound.  Theorem UE (UE^inf) builds f' from the masses
     max_i |b^theta_i| and the levers on the common Omega; Theorem E^eng (E^{eng,RT,inf}) averages per-piece bounds by convexity.  No common
     shift is used.
 (5) Lemma PM, Lemma S2c^tr: independent of the data.
 (6) Counting (Theorem C^tr, Q1-refa P8): with no cubes the pigeonhole gives |S| >= n(w)/D_cl(w); every later use of |S| is a lower bound.
 The Gamma estimate: without the increment the - side differs from the decomposition's - side only by the projection and class-zeroing
 errors (U1 2.2(b), 2.3), so sqrt Gamma^#_w(b^-, omega^-) <= sqrt Gamma^#_w(B_-, Theta_-) + K t as in V1 TR Step 5 / U1 2.2(e).  QED
Remark K1.1' (why the increment must be dropped at infinite F).  HEURISTIC (no explicit row constructed).  incr(t) is a nonnegative
combination of extreme rays with coefficients up to the cube side eps = c_f (u/Design)^C (NOT proportional to t), and for class-G carriers
every ray has eps_l gamma_l >= 0 ((X2)).  At an anti-sign support coordinate j in S_l cap F below the raise depth it adds anti-sign switching
up to C p eps v_l(j), which exceeds the cushion |a_j|/t whenever |a_j| < c p eps t v_l(j); Lemma P controls only the decomposition's own
amplitude (|tau_l| v_l(j) <= (16/5)|a_j|/t or tau_l pinned), so an active carrier of small amplitude (between K_*^2 K t and ~eps) can have such
coordinates.  The resulting anti-sign mass is not O(s_1) and cannot be tolerated as a violation.  Q2's sketch ("they are sub-patterns, so
V2's minors cover them") is right for the CLASS part of the pigeonhole and wrong for the CUBE part; Lemma K1.1 removes the cube part.

## 1.2 The deep raise (U2 Lemma W (R), Q2 3.2), adapted.  PROVED.
Box function Bx_L(j) := sum_{l <= L} lambda_l |u_l(j)| (a design function; sum_j Bx_L(j) <= sum_l lambda_l <= 1).  For an integer J put
   R(J) := {j in F : j >= J, |a_j| < 8 Bx_L(j)},   Delta a := sum_{j in R(J)} s_j (8 Bx_L(j) - |a_j|) e_j^*,   lambda_r := q*(a + Delta a),
and let f^r be the row with forced data ((a + Delta a)/lambda_r, z) (V3 2.0: a same-sign raise on F; F, z, K, rooms unchanged).
 (a) raise mass <= psi_L(J) := 8 sum_{j >= J} Bx_L(j) -> 0 (J -> infinity); ||U^* Delta a|| <= mu*_J psi_L(J) <= 8 mu*_J (mu* decreasing).
 (b) (V3 Lemma 2.1, 2.2, Cor. 2.4) lambda_r >= 1, lambda_r -> 1, p*(f^r - f) -> 0, and for every r in R
        p*(f^r + r rho g) <= 1 + (s(lambda_r rho r) - 1)/lambda_r + eps'_r,   eps'_r := 2||U^*Delta a|| + p*(L^*(w^r - w)) <= C_f mu*_J log(e/mu*_J).
 (c) (U2 Lemma DR-inf, U2-ref D1) every value moves by <= C mu*_J, every rate object of level L (incl. (R-mod), (R-pat), (R-lev)) by
     <= C Design(L) mu*_J; (R6)-type shift costs are exactly invariant.
CHOICE.  J = J(w) := the least J >= d(L) + 1 with C_f mu*_J log(e/mu*_J) <= min{ theta_w T^2, b^2 Phi_min(L)/(C Design(L)) } (theta_w of
Q1 CM^tr(f)).  Since mu*_J = 2^{-2^{2^J}}, 2^{J(w)} <= max{2^{d(L)+1}, 2 log_2(8 log_2(1/T) + C_f')}, and log_2(1/T) <= 2 n(w) + log_2(1/T_hi(w))
<= 3 n(w) for L large (T_hi(w) <= T_lo(w^-) and the earlier windows are short compared with n(w)).  So 2^{J(w)} <= Design(L) + 2 log_2(C n(w)).
Then at f^r every tiny rate object of f is <= 2b and every robust one >= u/2 (clean with factor 2), the budget lemmas hold at f^r for the
mate g^r := g - (g(xi^r)/q_0^r) a^r on the window with eta' -> 0 (V3/V3-ref (I1)), and (a) of Theorem E^{eng,RT,inf} holds at f^r.
[Q2's raise level 8 Bx_* + |g_j| is not needed: the |g_j| term was for copied base data; the deep assignment of 1.5 replaces copying.]

## 1.3 Classes with Lemma-P thresholds and enlarged patterns
PATTERN ENLARGEMENT.  For j in T(L) cap F (a target coordinate in the support; at most s_max(L) of them) the clean sub-window gives
|a_j| <= b ("tiny support") or |a_j| >= u ("robust support") ((R-mod)).  The pattern kappa records this label.  In the class cone
Gamma^#(kappa, a) (U1 2.1, U1-ref 4, X1 2.2) add for every TINY support coordinate j in T(L) the CONTACT ROW
   (X1^F)   s_j L(Delta', gamma)(j) >= 0
(the (X1) row of a contact of sign s_j).  Its entries lambda_l u_l(j), lambda_k u_k(j) (peak traces) are non-weight design data, so the
weight-freeness of X1 2.2(iv), Lemmas NLM, GEN, QC and Proposition KN^tr (Step A) apply verbatim to the enlarged patterns ((R-pat)).
THRESHOLDS.  Let C_q := (8/3)(2/q_0 + 8) (Lemma P at rows in the ball, q_0^r >= q_0/2), H the Hoffman constant of the class cones
(<= C Design^C/u after exactification, U1-ref 4.3), K := C_f (Design/u)^C the projection constant of U1 2.2(a)-(b), and
   K_P(w) := 8 C_q 2^{J(w)} D(L)/delta_min(L),     K_*(w) := max{ K_*^{U1}, 5(H J_Om + 2), (K_P(w)/K)^{1/2} }.
Classes are read off the decomposition data at f^r with A_1 := K_*, A_{i+1} := K_* A_i (U1 2.3, U1-ref 4.5).
Lemma K1.2 (active coefficients track the decomposition).  PROVED.  Let t in S, c_l (l <= L) the data coefficients of 1.0 and c^act_l :=
-Delta theta_l the actual coefficients of the decomposition (B_+-, Theta_+-) at f^r (eq:DeltaB: Delta B = -sum_l Delta theta_l u_l).  Then for
every coarse l either c_l = 0, or |c_l - c^act_l| <= |c_l|/5 and |c_l| >= K_*^2 K t/(4 D(L)).
Proof.  Omega carriers: c_l = gamma_l(t), the projected component; class zeroing moves components by <= A_{i(t)} K t each, the projection onto
Gamma^#(kappa, a(t)) by <= H J_Om A_{i(t)} K t + K t (U1 2.2(a)-(b)); an active component has |gamma_l| >= A_{i(t)+1} K t = K_* A_{i(t)} K t >=
5(H J_Om + 2) A_{i(t)} K t, so the total error is <= |gamma_l|/5.  Inactive components: gamma_l(t) = 0.  Coarse peaks k of block m: c_k =
-Delta''_m(t) lambda_k vs_k and, by eq:peakshift at f^r, c^act_k = -Delta'_dec,m lambda_k vs_k + e_k with |e_k| <= C_f D t/u at peaks of
relative margin >= u/2 (U1 2.2(a)(i)); Delta''(t) = Delta'(t) kappa'/kappa^# (K1.1(2)), |Delta'(t) - Delta'_dec(t)| <= (H J_Om + 2) A_{i(t)} K t
for active shifts, Delta'(t) = Delta''(t) = 0 for inactive ones; with |Delta'(t)| >= K_*^2 K t and lambda_k >= 1/D(L), M^# >= 1/2, the same
arithmetic gives the claim (K_*^{U1} absorbs C_f D/u).  QED

## 1.4 Lemma K1.3 (no deep set at the raised row).  PROVED.
For every t in S and every j in F:
     s_j V_c(j) >= -4|a^r_j|/t - tr_j,
where tr_j := |sum_m (Delta''_m(t) - Delta'_m(t)) P_m(j)| (trace correction, nonzero only at j in T(L)) and sum_j tr_j <= C_f Design(L) c_{L+1}
+ C_f c_{L+1}^2/t.
Proof.  Coefficient bound: for coarse l, |c_l| <= C_f D(L) lambda_l.  [Omega: c_l = lambda_l(Domega(k) - Delta_m w^#(k)); by (U1) Gamma_w <= 2
and X2 Proposition J(a), ||D_m Domega||_2 <= C_f, so |Domega(k)| <= C_f/Phi_k <= C_f D(L); |Delta_m| <= C_Delta ((U7)).  Peaks: |c_k| <=
C_Delta lambda_k.]  Hence |V_c(j)| <= C_f D(L) Bx_L(j).  Four cases.
 (D) j >= J.  |a^r_j| >= 8 Bx_L(j)/lambda_r >= 4 Bx_L(j) (1.2), so 4|a^r_j|/t >= 16 Bx_L(j)/t >= |V_c(j)| for t <= T_hi(w) <= 16/(C_f D(L)).
 (Tr) j in T(L), robust: |a^r_j| = |a_j|/lambda_r >= u/2, so 4|a^r_j|/t >= 2u/T_hi(w) >= C_f D(L) >= |V_c(j)| (T_hi(w) <= u/(C Design(L))).
 (Tt) j in T(L), tiny: the data satisfy (X1^F) exactly at the reference coefficients, s_j L(Delta'(t), gamma(t))(j) >= 0; V_c(j) =
      L(Delta''(t), gamma(t))(j) = L(Delta'(t), gamma(t))(j) + sum_m (Delta''_m - Delta'_m) P_m(j) (U1 Lemma 4.6(b)); so s_j V_c(j) >= -tr_j.
      The bound on sum tr_j is U1 Lemma 4.6(a)-(b) (per scale, K1.1(2)).
 (S) j < J, j notin T(L), j in S_l for a coarse l.  Among coarse carriers only l lives at j (coarse targets lie in T(L); signature sets are
      disjoint; (P1)), so V_c(j) = c_l v_l(j).  If c_l = 0 there is nothing to prove.  Otherwise suppose s_j c_l v_l(j) < -4|a^r_j|/t.  By Lemma
      K1.2, c^act_l has the sign of c_l and |c^act_l| >= (4/5)|c_l|, so with tau_l := eps_l c^act_l (any sign convention eps_l) the coordinate is
      of the type opposite to the switching direction and |tau_l| v_l(j) > (16/5)|a^r_j|/t: (P.2) of Lemma P holds at f' := f^r (j is UNRAISED,
      j notin T(L), l <= L).  Lemma P gives |c^act_l| <= C_q t/v_l(j) <= (5/4) C_q 2^{J} t/delta_min(L) (v_l(j) = delta_l 2^{-j}/n_l, n_l <= 5/4).
      [Lemma P's term sum |r_s| <= 8t^2 needs sum_{l''>L} lambda_{l''} <= t^3, true: <= C T^8.]  Hence |c_l| <= (25/16) C_q 2^J t/delta_min(L),
      while Lemma K1.2 gives |c_l| >= K_*^2 K t/(4 D(L)) >= K_P(w) t/(4 D(L)) = 2 C_q 2^J t/delta_min(L): contradiction.
 (O) j < J, j notin T(L), j in no S_l with l <= L: no coarse carrier lives at j, V_c(j) = 0.  [A coordinate of S_l with l > L is not in T(L) by
      allowedness (a), so it falls under (O).]  QED
Remark.  (D) is the deep raise, (S) is U2's pinning-by-Lemma-P with the pinned carriers sent to the zero face by the CLASS pigeonhole (they
are inactive because their actual amplitude is below K_P t <= K_*^2 K t), (Tr)/(Tt) are the clean-sub-window dichotomy of the support moduli
of the target coordinates (U2 Lemma W (S1) and its Sigma-rows, which are automatic at clean sub-windows).  This is exactly Q2's steps (i)
"projecting the switching ... to zero" and the cushion bookkeeping, now inside Q1's class pigeonhole.

## 1.5 The deep assignment on F (Z5-ref Theorem R1, Claim 3.1) and Proposition K1.A (= Q2 Proposition 3.2).  PROVED.
Let f^# be a companion of f^r produced by Q1's Step A with the lever resources of part 2 (Step B is omitted, part 3 Lemma K1.S), and let
F_low ⊂ F be the set of support coordinates LOWERED by those resources (part 2): (i) THIN NEAR coordinates (|a^r_j| <= b, j in N_l) used
as bank or Z-con coordinates -- for a data-carrying carrier l they have s_j = eps_l and become contacts of sign eps_l (then banked: support of
sign eps_l again); for a zero-data carrier they become contacts and may be z-moved; (ii) FAR PULL coordinates (|a^r_j| <= x_max, s_j = eps_l),
which are then pulled, i.e. become support coordinates of sign -eps_l with mass 24 lambda_l v_l(j) at f^#.  Properties of f^# used (proved in part 2 / Q1): (P#1) |a^#_j| >= |a^r_j|/2 for
j in F \ F_low (q*(A^#) <= 2; S-mass levers keep |A(p)| >= |A_1(p)|/2, Q2-refa (p2.2)); (P#2) Step-A supports off F are as in Q1 Prop. BR
((U3) contact-like or t|b| <= K_3 |a^#|, up to V_fine, Q1-refa P3); (P#3) the coarse statuses of Q1 CM^tr(b).
DATA.  For t in S let (B_+-, Theta_+-) be the decomposition of g^r at f^r at scale t, V = V(Domega(t)) the route-V switching (K1.1), and
A_j := 2|a^r_j|/t (j in F).  On F \ F_low define b^+_1 by Z5-ref's deep assignment with X := V_c|_F: x_j := s_j B_+(j), y_j := s_j(B_+(j) - V_c(j)),
sigma_j := the point of [y_j - A_j - tr_j, x_j + A_j] closest to 0, b^+_1(j) := B_+(j) - s_j sigma_j (the interval is nonempty by Lemma K1.3:
x_j - y_j = s_j V_c(j) >= -2A_j - tr_j).  On F_low put b^+_1(j) := chi_j V_c(j) with chi_j in [0,1] (contact split; at a pulled
coordinate this is V1 TR(iv)'s pull data; at a coordinate of a zero-data carrier V_c(j) = 0).  Off F the + side is Q1's:
chi V_proj + V_fine/2 on contacts, Q1's data on the Step-A supports.  Then
     b^+ := b^+_1 + (off-F part) - kappa a^#/a^#(zhat^#),  kappa := (b^+_1 + off-F part)(zhat^#),   b^- := b^+ - V,   omega^+- as in Q1.
PROPOSITION K1.A.  For every t in S, (b^+-, omega^+-) represent g_t at f^# and form, together with the other scales of S, a window family at
f_0 := f^# satisfying (U1), (U2), (U4)-(U7) of Q1 Proposition BR and
 (U3^inf) with C_+ := 5:  (s_j b^+(j))_- <= 5|a^#_j|/t and (s_j b^-(j))_+ <= 5|a^#_j|/t + |V_f(j)| + tr_j for every j in F \ F_low,
 and contact-likeness up to |V_f(j)| on F_low;
the excess terms |V_f(j)| + tr_j are violations (Q1-refa P3: at a support coordinate the base excess of a'_j + x_j is <= 2(z_j x_j)_-) of total
mass <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/t, counted in eps^viol of (U4); and
     p*(g - g_t) <= K_data t,   K_data := J_Om K_*(w)^{J_Om + 1} K + C_f,
     ||B_+ 1_F - b^+_1||_1 <= (1 + eta') t/q_0^r + K t + 7 C c_{L+1}/t.
Proof.  (i) Claim 3.1 of Z5-ref, re-derived with the extra slack tr_j: from lem:flip at f^r, s_j B_+(j) >= -|a^r_j|/t - f^+_j and s_j B_-(j)
<= |a^r_j|/t + f^-_j, sum_F (f^+_j + f^-_j) <= (1 + eta')t/q_0^r.  The point of [y - A - tr, x + A] closest to 0 has modulus (-x - A)_+ +
(y - A - tr)_+ <= f^+_j + f^-_j + |(Delta B - V_c)_j| (B_+ - V_c = B_- + (Delta B - V_c)); so |B_+(j) - b^+_1(j)| <= f^+_j + f^-_j + |(Delta B -
V_c)_j|, and s_j b^+_1(j) = x_j - sigma_j >= -A_j, s_j(b^+_1 - V_c)(j) = y_j - sigma_j <= A_j + tr_j.  On F_low: |B_+(j) - chi_j V_c(j)| <=
|B_+(j)| + |V_c(j)| is bounded by A_j + f^+_j + f^-_j + |(Delta B - V_c)_j| for the choice chi_j := the projection of s_j B_+(j)/(s_j V_c(j)) onto
[0,1] when s_j V_c(j) > 0 (chi_j := 0 otherwise), because the flip bounds at f^r give -A_j/2 - f^+ <= s_j B_+(j) <= s_j V_c(j) + A_j/2 +
f^- + |(Delta B - V_c)_j| (V_c(j) = c_l v_l(j) has the sign s_j = eps_l at a lowered coordinate of a data-carrying carrier, and vanishes
at one of a zero-data carrier); sum_{F_low} A_j <= 2(|Lambda| b + |Lambda| x_max)/t <= 4T/(L Design(L)) + 2|Lambda| b/t <= K t
(|F_low| <= 2|Lambda|, x_max of part 2, b <= T^4).
At a pulled coordinate the cushion at f^# is the pull mass 24 lambda_l v_l(j) >= t|V(j)| (t <= T_hi, |c_l| <= C_f D lambda_l), as in V1 TR(iv).
(ii) ||Delta B - V_c||_{l_1(F)} <= sum_{l <= L} |c^act_l - c_l| ||u_l||_1 + ||sum_{l > L} Delta theta_l u_l||_1 <= K t + 6 sum_{l>L} lambda_l/t
(Lemma K1.2 errors are the projection/zeroing/peak errors of U1 2.2(a)-(b), 2.3, summing to <= K t; lem:box for fine carriers).  This gives
the stated l_1 bound and, with ||V_f||_1 <= C_Delta sum_{l>L} lambda_l <= C c_{L+1}, the closeness: g_t - (Q1's g_t) = b^+_1 - B_+ 1_F +
(kappa terms), so p*(g - g_t) <= (Q1's K t, with K_data of Q1-refa 2.7 for the zeroing) + (1 + ||U||)||B_+ 1_F - b^+_1||_1 <= K_data t.
(iii) Cushion.  |kappa| <= K t as in V1 TR Step 5 / Z5-ref Claim 3.2 (b^+_1 differs from B_+ 1_F by O(K t) in l_1, |B_+(zhat^r)| <= t/(2q_0^r) by
lem:budget(a), |<U^*B_+, e^# - e^r>| <= ||B_+||_1 ||e^# - e^r|| <= (C/t) Design T^3 <= t).  On F \ F_low, by (i) and (P#1):
(s_j b^+(j))_- <= A_j + |kappa| |a^#_j|/a^#(zhat^#) <= 4|a^#_j|/t + 2K t |a^#_j| <= 5|a^#_j|/t, and (s_j b^-(j))_+ = (s_j(b^+_1 - V_c - V_f)(j) -
kappa s_j a^#_j/a^#(zhat^#))_+ <= A_j + tr_j + |V_f(j)| + 2Kt|a^#_j| <= 5|a^#_j|/t + tr_j + |V_f(j)| (Kt^2 <= 1/2).  On F_low the + side is
chi_j V_c(j) and the - side -(1 - chi_j)V_c(j) - V_f(j): at a pulled coordinate t|b^+-(j)| <= t|V(j)| <= 24 lambda_l v_l(j) = |a^#_j| (the
finite-F alternative of (U3), i.e. (U3^inf) with C_+ = 1); at a lowered near coordinate of a data-carrying carrier the data are contact-like
for the sign eps_l = s_j (zero anti-sign part on both sides) up to |V_f(j)|; at a coordinate of a zero-data carrier V_c(j) = 0 and the data
are the fine residue (violation; split 1/2 at a free coordinate so that b^theta = 0).
(iv) The other hypotheses.  Only the base part on F changed; omega^+- and the off-F data are Q1's (with K1.1), so (U2), (U6), (U7) are Q1's
(with the levers of part 2), and (U5) is replaced by (U5') of Lemma K1.S(c).
(U1): t||b^+-||_1 <= t(sum_F A_j + 2||V||_1 + ...) <= 4||a^r||_1 + C_f(1 + D(L) t) <= A_0 (Claim 3.1(iv): |b^+_1(j)| <= A_j + |V_c(j)| + tr_j);
Gamma: sqrt(Gamma^#_w) is a seminorm and q_0 h(y) <= ||U||^2 ||y||_1^2/nu, so the base change of l_1-size O(K t) changes sqrt Gamma by O(K t),
absorbed as in Q1.  (U4): the violation list of Q1 CM^tr(d) plus the excesses above, all with b^theta = 0 at violated FREE coordinates
(the new violations sit at support coordinates, where (H3) is not required: P3).  QED
COROLLARY K1.B (window-constant bookkeeping).  PROVED.  With (W_exp) and the choices above: C_+ = 5 is ABSOLUTE (Q2's C Design/u is not
needed), so c_flat(w) >= c_f u(w) exactly as in Q1 (gamma_B(w) = min_m M_m u/4); K_data <= C_{f,N} (Design(L)/u)^{C(L+N)} (log n(w))^{(L+N+2)/2}
(K_*(w) <= C_f (Design/u)^C (2^{J(w)})^{1/2}, 2^{J(w)} <= Design(L) + 2 log_2(C n(w))); the class count D_cl(w) <= (L + N + 1) 3^{L+N}; and (E-d), (E-e') of Theorem E^{eng,RT,inf} hold along L -> infinity: |S| c_flat/K_data >= n(w) c_f u/(D_cl K_data) -> infinity
because n(w) >= L 2^{L^3} Q(w), Q(w) >= (4 Design/u)^{omega(L) + L^2 + 20} (Q1-refa P8) and (log n)^{L+N+2} <= n^{1/4} once log n >= L^3 >> (L+N)^2;
eps' = eps'_r + p*(f^# - f^r) <= 2 theta_w T^2 by the choice of J (1.2) and Q1 CM^tr(f).
