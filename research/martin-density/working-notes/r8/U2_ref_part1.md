# U2 referee, part 1: design SLD^star, Lemma P, Theorem RS*  (checked against the note, Z5-ref R1/R2, V3 + V3-ref)

## 1.1 Design SLD^star (U2 1.1).  VERDICT: correct (PROVED), with one statement precision (s1) and one remark (s2).
Re-derived:
 * Base U k_s = mu*_s e_s, mu*_s = 2^{-2^{2^s}}: compact, dense range (contains c_00), U^* e_s^* = mu*_s k_s injective on l_1,
   ||U|| = mu*_1 = 1/16.  The note fixes the base before T and uses it only through ||U|| in delta_l (def:SLD (D0)) and through
   prop:smooth(c) (any compact dense-range U); V3-ref F6 already accepted a diagonal base.  OK.
 * Window factor: s_max(l), delta_min(l), Lambda°(l) are fixed once y_l is chosen at stage l; T_lo(l-1) at stage l-1; so
   Omega(l) = Omega_K(l) Omega_log(l) is computable before n^w_l, T_hi(l), T_lo(l), c_{l+1}.  Recursion well founded, N-free.
   Omega_K >= 2, Omega_log >= 4, so (P3) (T_hi 2^{l^3} Lambda° <= 1/l, n^w >= l 2^{l^3} Lambda°, T_hi(l+1) <= T_lo(l)) holds a fortiori.
   (P1), (P2), (T-a)-(T-d) use (D1) only through allowedness (a), (b) and c_{l+1} = min(c_l/4, T_lo(l)^3): unchanged.  OK.
 * Why the DOUBLY exponential exponent is needed (re-derived; sharpens U2 1.4(b)).  Step 1'' needs a least n with
   n >= A K'(l, J(n)), J(n) = min{J : mu_J <= x(n)^2}, log_2(1/x(n)) = L + 2n + O(log l).
   - mu_s = 2^{-s^2-1}: 2^{J(n)} ~ 2^{sqrt(2(L+2n))}, super-polynomial in n: for n >= L the right side exceeds n, for n < L it is
     >= A 2^{sqrt(2L)} > L for large L: NO solution.  So V3/U4's base cannot be used here (U2 is right).
   - mu_s = 2^{-2^s} (single exponential exponent): 2^{J(n)} ~ 2 log_2(1/x) ~ 2(L + 2n): linear in n with slope ~ 4A C'_B/delta_B,
     and A = 48 rho^2/(c_flat(1-rho^2)) is large: NO solution in general.
   - mu*_s = 2^{-2^{2^s}}: 2^{J(n)} <= 2 log_2(2 log_2(1/x)) = O(log(L + n)): solution exists, n_j <= C_f[(1 + K*) 2^{s_max} +
     log(L_j + C_f)].  So "2^{J} = o(log(1/x))" is exactly what is needed, and the doubly exponential exponent is the natural choice.
(s1) PRECISION (statement).  For T_final^* (D_Omega / D^{V2} version, part 3 of U2) the stated enlargement B_mu*(l) := 2^{sigma(l)}/
   (mu*_{sigma(l)})^2 is NOT what Lemma TR-inf uses: case (c) works at coordinates s' <= d(L) := sigma(L) + 2^{L+2} and its proof
   invokes "Design(L) contains (mu*_{d(L)})^{-2} 2^{d(L)}/delta_min(L)".  Fix: B_mu*(l) := 2^{d(l)}/(delta_min(l) (mu*_{d(l)})^2),
   d(l) := sigma(l) + 2^{l+2} (a design quantity; well defined at stage l).  Moreover T_final^* must also list the NEW RATE
   OBJECTS of U2 3.3 (moduli |a_s|, s <= d(l); ratio spreads of the first three coordinates of each S_{l''} beyond s_max(l);
   Sherman-Morrison denominators of subsets of carriers <= l) in omega(l), so that M(l) = omega(l) + 1 sub-windows still give a
   clean sub-window; these are finitely many, N-free, indexed by design data, so Theorem 2' survives.  Neither change affects
   admissibility (only c-upper bounds / window lengths change).  See also part 3, gap (G1): Design(l) must contain 2^{d(l)} so that
   the deep raise can be taken BELOW the tuning depth.
(s2) Remark.  SLD^star is a design for RS*/RS*_inf (SLD-type windows); the claim "the same two changes can be made in D_Omega/D^{V2}"
   is correct as far as admissibility and N-freeness go (only window lengths and the base change; U4-ref F2: the base enters V1/V2
   only through s'^2 v' at bank coordinates), but U2 itself labels the D_Omega/D^{V2} part SKETCH; I agree.

## 1.2 Lemma P (pinning by an unraised deep coordinate).  VERDICT: correct (PROVED), precision (p1).
Re-derived line by line.  For s in S_l, s notin T(l_*): u_l(s) = v_l(s) (y_l vanishes on S_l by allowedness (a)), signatures of
other carriers vanish (disjointness), targets of l'' < l vanish on S_l (allowedness (a)), targets of l < l'' <= l_* would put s
into T(l_*).  Hence by eq:DeltaB, Delta B(s) = eps_l tau_l v_l(s) - r_s, r_s := sum_{l'' > l_*, s in supp y_{l''}} Delta theta_{l''}
y_{l''}(s)/n_{l''}.  lem:flip (proof uses only G_b(a + tB_+) <= budget/q_0, valid for every t > 0 and with budget (1 + eta')t^2/2):
s_s B_+(s) >= -|a_s|/t - f^+_s, s_s B_-(s) <= |a_s|/t + f^-_s, so s_s Delta B(s) >= -2|a_s|/t - phi_s.  With s_s eps_l = -sigma,
sigma tau_l = |tau_l|: s_s Delta B(s) = -|tau_l| v_l(s) - s_s r_s.  This is (P.1).  Under (P.2), 2|a_s|/t <= (5/8)|tau_l| v_l(s), so
(3/8)|tau_l| v_l(s) <= phi_s + |r_s| <= (1 + eta')t/(2q'_0) + |r_s|.  Good-target variant: r'_s collects the coarse good carriers whose
targets contain s; |r'_s| <= (4/3) sum_good |Delta theta|; (8/3)(1/q' + 8 + (4/3)K*) <= C_q(1 + 2K*).  All correct.
(p1) The bound sum_s |r_s| <= (4/3) sum_{l''>l_*} 6 lambda_{l''}/t <= 8 T_lo(l_*)^3/t is <= 8t^2 only for t >= T_lo(l_*) (in fact for
   t >= T_lo(l_*)^{3/2} one still has <= 8t); the statement "t in (0, min(t_eta, 1)]" must read "t in the window W(l_*) (or above
   T_lo(l_*)^{3/2})".  All applications use scales inside W(l_*): harmless.
(p2) Lemma P holds at ANY row with forced data and any functional with the stated budget; in particular at f itself (used in my
   fix (G2) of part 3).

## 1.3 Theorem RS* (no (RR)).  VERDICT: correct (PROVED; V3's inspection items I1-I3 unchanged), precisions (r1), (r2).
Checked: the thresholds K_1..K_{|B|+2}; the pigeonhole (|B| numbers miss one of |B|+1 intervals); the Hoffman projection onto
Z_f(L') with violation <= C'_f K* t + |B| K_{i_0} t <= K_{i_0+1} t/(4H); sign and size of kept amplitudes ((3/4)|tau| <= |tau'| <=
(5/4)|tau|); the four cases of the "empty deep set" claim; the fixed point n_j (exists, n_j = o(n^w_{l_j}) under (W*) and the window
factor, see 1.1); the footprint arithmetic: eps'_j <= C mu y log(e/(mu y)) with mu <= x^2 gives mu log(e/mu) <= sqrt(mu) <= x and
mu log(1/y_j) <= x (x log(1/y_j) -> 0), so eps'_j <= 2 C x y_j = 8 C C_tau theta_j c_flat^2 T_j^2 4^{-n_j}/C_e: Theorem 2.5 (d) holds
with C_e >= 8 C C_tau.  lambda_j >= 1: ||Delta a''||_1 <= C_0 ||U^*Delta a|| <= C_0 mu*_{J_j}||Delta a||_1 (VP').  J_j -> infinity,
K' T_j -> 0 (T_j log n_j -> 0).  The dependence of K' on 2^{J} is additive, as claimed.
(r1) Bad-PEAK targets.  RS* sets B := B_np and T_B := union of the targets of B_np; Lemma P's correction r'_s lists only GOOD coarse
   carriers, with the justification "bad carriers' targets do not contain s".  Targets of coarse bad PEAK carriers may contain
   s in T(l_j) \ T_B.  Fix (as in U2's own Lemma W): T_B := union of the targets of ALL bad carriers (finite under (B_fin)); then
   case (i) of the claim (finite set of fixed support coordinates, 4|a^{(j)}_s|/t >= |a_s|/T_j -> infinity) covers these
   coordinates.  (Alternatively add the bad-peak amplitudes, |tau| = O(K* t) by lem:badpeaks(c)/RS'(b), to r'_s.)
(r2) Contact rows.  As in Z5 Step 2, T_0 must contain union_{l in B_F}(S_l \ F) (finite contact sets of support-swallowed bad
   carriers) besides the targets; RS* inherits this from R1 verbatim.  No change needed, only noted because Lemma W (part 2)
   restates the cone without it.
Attack summary for RS*: weak* vs norm (f_j -> f in norm: ||Delta a||_1 <= y_j|B| -> 0); uniformity in t (sub-window S_j inside
W(l_j), budget lemmas on S_j only, (I1)); uniformity along companions (constants of R1/R2 at f_j: (I1)-(I3)); simultaneous
exactifications (only raise + VP' on the fixed F_0, J_j > max F_0); quantifier order (design -> f -> g, rho -> l_j -> n_j,
J_j -> companion -> decompositions at f_j -> data): correct; hidden assumptions on T: SLD^star only through (P1)-(P3),
allowedness, the base; non-attained infima: none (nearest points of closed cones exist).  No problem found beyond (r1), (r2).

## 1.4 Theorem ND' and Lemma ND (U2 4.2).  VERDICT: correct (PROVED).
Lemma ND re-derived: for s in F \ T_0 either no u_k (k in L_0) is nonzero at s (supports of u_k are supp y_k ∪ S_k), forcing
kappa a_s = 0 (impossible), or s in S_k for exactly one k, where u_k(s) = v_k(s) and the others vanish: kappa a_s = c_k v_k(s).
Theorem ND': on F \ T_B (T_B: targets of all bad carriers) every s lies in a kernel S_k and U_B(s) = v_k(s) (disjoint signatures),
|a_s| = |c_k/kappa| v_k(s), so sup_{l in B, j in F}|u_l(j)|/|a_j| < infinity (finite exceptional set F ∩ T_B): (H4-inf) holds,
Lemma R0(a) gives (CS_B), R1 applies with no raise.  The dichotomy "(ND') holds -> RS*; fails -> R1" is exhaustive.  Correct.
Also checked: the case B_np empty ((ND'_{empty}) holds as a != 0) and F finite (R1 directly).
