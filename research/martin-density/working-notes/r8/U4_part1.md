# U4 part 1 — The final admissible operator T_final and base U_final; recursion, admissibility, conflicts

Notation and numbering: paper/martin_density_note.tex ("the note"; Sections 1, 7, 8), Rounds 5-7 notes with referee fixes.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Finite block sets I = {1..N}, p_N; Martin's p is I = N.

## 1.1 The base U_final (design D^mu, V3 3.1)
H := l_2 with orthonormal basis (k_s)_{s >= 1}; mu_s := 2^{-s^2-1}; U k_s := mu_s e_s.  Then U is compact (diagonal, mu_s -> 0),
its range contains c_00 (dense range), U^* e_s^* = mu_s k_s, U^* is injective on l_1, ||U|| = mu_1 = 1/4, and
     q^*(a) = ||a||_1 + (sum_s mu_s^2 a_s^2)^{1/2}.
By Proposition prop:smooth(c) of the note (valid for every compact dense-range U), NA((c_0,q)) = c_00.  The two diagonal identities
used by every diagonal-base argument (V1 (1.1), Lemma B (3.1); Y4-ref C.2) hold for every diagonal base with positive entries:
for b in l_1 and s notin supp b, <U^*b, k_s> = mu_s b_s = 0; for A = a + sum_{s in J} c_s e_s^* with J ∩ supp a = {},
U^*A = U^*a + X, X := sum_J c_s mu_s k_s ⊥ U^*a, and <U^*u, X> = sum_J c_s mu_s^2 u(s).   (PROVED, direct computation.)

## 1.2 Data fixed in advance (D0_final)
 (i)   A ladder bijection j : N x N -> N with j(k,m) < j(k',m) for k < k'; (k(l), m(l)) := j^{-1}(l).  (Then k(1) = 1.)
 (ii)  j_0 := 1;  S_l := {2^l (2i+1) : i >= 1} (l >= 1): pairwise disjoint, infinite, even, so j_0 notin S_l; BOUNDED GAPS
       G_l := 2^{l+1}; min S_l = 3 * 2^l.  Z_0 := N \ union_l S_l = {odd numbers} ∪ {2^r : r >= 1} (infinite).
 (iii) h_l := sum_{s in S_l} 2^{-s} e_s^*,  H_l := ||h_l||_1,  delta^max_l := min{2^{-l}, (4(1 + ||U||) H_l)^{-1}}.
 (iv)  tau_l := 2^{-l} (decreasing, tau_l -> 0; V4 (SF_tau) with V4-ref R11).
 (v)   Targets: (y^(i))_{i >= 1} in c_00 ∩ S_{q^*}, dense in S_{q^*}, with y^(1) := e_1^*/q^*(e_1^*), and containing
       y^* := (e_3^* - e_5^*)/q^*(e_3^* - e_5^*), y^** := (e_7^* - e_9^*)/q^*(e_7^* - e_9^*)  ((Z0): p, p', p'', p''' = 3, 5, 7, 9 in Z_0).
 (vi)  Schedule: K_FD := {2^r : r >= 1} (the FD stages); N \ K_FD = {k_1 < k_2 < ...}; (i_r)_{r >= 1} a sequence in which every
       positive integer occurs infinitely often.

## 1.3 The recursion (stage l = 1, 2, ...)
Given all data of stages < l (for l >= 2 in particular c_{l-1} and the sub-windows of level l-1), define in this order:
 (1) TARGET y_l.  If k(l) in K_FD: y_l := e_{j_l}^*/q^*(e_{j_l}^*), j_l := the least odd integer > max(9, max union_{l' < l} supp y_{l'})
     (FD target, supported in Z_0, FRESH).  Otherwise k(l) = k_r and y := y^(i_r); y_l := y if y is ALLOWED at l:
       (a) supp y ∩ S_{l'} = {} for every l' >= l;       (c) supp y ∩ S_{l'} ⊂ [1, l] for every l' < l   (Y3, D_sigma);
     and y_l := y^(1) otherwise (y^(1) and every FD target are supported in Z_0, hence allowed at every l).
 (2) SIGNATURE SIZE delta_l.  delta_1 := delta^max_1.  For l >= 2: g_l := delta^max_l H_l/(32 * 3^{|supp y_l|}) and delta_l := the
     largest delta in [delta^max_l/2, delta^max_l] with |sum_j sigma_j y_l(j) + eps delta H_l| >= g_l for all sigma in {-1,0,1}^{supp y_l},
     eps = +-1 ((GM), V4).  [The excluded set is a union of at most 2 * 3^{|supp y_l|} open intervals of length 2 g_l/H_l, total
     <= delta^max_l/8 < delta^max_l/2, so the admissible set is a nonempty compact set and the maximum exists.]
 (3) n_l := q^*(y_l + delta_l h_l), u_l := (y_l + delta_l h_l)/n_l, v_l := delta_l h_l/n_l, delta°_l := delta_l H_l/n_l,
     eta_l := min(1, min_{j in supp y_l}|y_l(j)|), Lambda°(l) := prod_{l'' <= l}(1 + 2/delta°_{l''}).
 (4) WEIGHT c_l.  c_1 := 1.  For l >= 2, c_l := the minimum of the following positive numbers:
     (W1) c_{l-1}/4;   (W2) b(l-1, M(l-1))^2;   (W3) (delta_l H_l)^2;
     (W4) tau_{l'} 2^{-2s} c_{l'} delta_{l'}/2 for every l' < l and s in supp y_l ∩ S_{l'}   [allowedness (b) and V4 (b')];
     (W5) c_{l-1} delta_l 2^{-min S_l - l - 10}/(1 + ||U||)   [(SF*) second half];
     (W6) g_l 2^{m(l) + k(l) - l}   [(GM): Phi_l <= g_l 2^{-l}];
     (W7) 3 * 2^{-10} tau_{l-1} lambda_{l-1} delta_{l-1} 2^{-(m(l-1) + k(l-1) + min S_{l-1})} eta_{l-1}/(n_{l-1}(1 + ||U||))  [(SF_tau)].
     Put Phi_l := 2^{-m(l)-k(l)} c_l and lambda_l := m(l) Phi_l.
 (5) LEVEL-l DESIGN DATA.  T(l) := union_{l'' <= l} supp y_{l''};  s_max(l) := max(T(l) ∪ {1});  sigma(l) := max_{l'' <= l}
     min(S_{l''} ∩ (s_max(l), infinity)) (<= s_max(l) + 2^{l+1});  m^nat_{l''}(l) := ||v_{l''} 1_{S_{l''} \ ([1,l] ∪ T(l))}||_1 > 0;
     D(l) := 1 + sum_{l'' <= l}(1/m^nat_{l''}(l) + 1/Phi_{l''});  delta_min(l) := min_{l'' <= l} delta_{l''};  G(l) := 2^{l+1};
     B_mu(l) := 2^{sigma(l)}/mu_{sigma(l)}^2 = 2^{2 sigma(l)^2 + sigma(l) + 2}   [replaces V1's 8^{sigma(l)}, see C1];
     G^*(l) (Z4, SLD_G), H_comb(l) (Z6), G^**(l) (Y1 1.2), Xi^Y(l) = [l H_comb G^** D]^8 (l 2^{l^3} Lambda° G^**)^5 (Y2);
     the PATTERNS kappa of level l (V1 2.6, read with the kept set Kp as in V2-ref section 3), their zero-cost cones and normalized
     extreme rays, H_tune(l) (V1 1.2); the SHIFT PATTERNS pi (V1 2.5) and the ENLARGED shift patterns kappa^sh (V2-ref P3);
     the DETERMINANTAL OBJECTS O = (kappa, J, K) with polynomials pi_O (V2 Def. 2.1); Lip(l), C_L(l), N_L(l) (Lemma L for the
     family {pi_O : O of level <= l}, fixed by the choice rule of V2 1.2 Remark (a)); delta_comb(l) (least nonzero design minor,
     := 1 if none); C_*(l) := |T(l)| + 2; delta_sh(l) (V2 Cor. C1.1 with the design weights m^d of V2-ref P4, := 1 if no positive value);
     rows(l), cols(l) (maximal size of the systems A_kappa).
     RATE OBJECTS of level l: V1 (R1)-(R7); the determinantal objects O; the shift-pinning objects (kappa^sh, "sh") of V2 Def. 3.2;
     omega(l) := their number (finite, independent of N and of f).
     DESIGN FACTOR:
       Design(l) := [ l 2^{l^3} B_mu(l) 2^{s_max(l)} 2^{G(l)} delta_min(l)^{-1} Lambda°(l) (1 + |T(l)|) D(l) G^*(l) H_comb(l) G^**(l)
                      H_tune(l) Xi^Y(l) ]^6  x  Lip(l) (2 + 1/delta_comb(l)) (rows(l) cols(l))^l C_*(l) C_L(l) (1 + 1/delta_sh(l))
     (every factor >= 1; Lip(l) is taken >= 1).
 (6) SUB-WINDOWS of level l: M(l) := omega(l) + 1; for i = 1..M(l), w = (l,i), w^- its lexicographic predecessor:
       u(w) := 1/4 if w = (1,1), u(w) := b(w^-) otherwise;   Q(w) := (4 Design(l)/u(w))^{omega(l) + 20};   n(w) := ceil(l 2^{l^3} Q(w));
       T_hi(w) := min{T_lo(w^-), 2^{-l^3}/(l Q(w))} (T_lo((1,1)^-) := 1);   T_lo(w) := 2^{-n(w)} T_hi(w);
       eta(w) := T_lo(w)^4/(l Design(l));   b(w) := min{eta(w), (eta(w)/C_L(l))^{N_L(l)/2}}/(1 + Lip(l) C_*(l))   (V2 Def. 2.2(iii)).
     W(w) := [T_lo(w), T_hi(w)] with its n(w) dyadic scales; Band(w) := (b(w), u(w)).
(D2) T_final e_{k,m} := c_{j(k,m)} u_{j(k,m)}, extended linearly and continuously to l_1(N x N).

## 1.4 Lemma W (well-founded recursion; N-independence).  PROVED.
(a) Every quantity defined at stage l is a function of (D0_final) and of quantities defined at earlier stages or earlier in stage l;
(b) all of them are finite and positive where used as divisors; (c) none depends on N.
Proof.  (a) By inspection of (1)-(6): (1) uses only supports of y_{l'} (l' < l), the fixed S_{l'} and the schedule; (2) uses y_l;
(3) uses y_l, delta_l; (4) uses c_{l'}, delta_{l'}, y_{l'}, n_{l'}, eta_{l'} (l' < l), b(l-1, M(l-1)) (computed in (6) of stage l-1),
delta_l, H_l, g_l, y_l; (5) uses data of index <= l, including c_l and Phi_l from (4); the patterns, cones, rays, Hoffman constants
G^*, G^**, H_comb, H_tune, the polynomials pi_O and the Lemma-L constants depend only on the finitely many design numbers u_{l''}(j)
(l'' <= l, j in T(l)), on finitely many sign/contact/status choices and on Phi_{l''}, m^nat (l'' <= l); (6) uses Design(l),
omega(l), C_L(l), N_L(l), Lip(l), C_*(l) and the values T_lo(w^-), b(w^-) of the predecessor, computed earlier.  The (SF_tau)
condition on the weights after level l (an inequality about the future) is imposed at stage l+1 through (W7) and propagated by (W1):
sum_{l'' > l} lambda_{l''} <= sum_{l'' >= l+1} c_{l''}/4 <= c_{l+1}/3.  Nothing refers to a later stage.
(b) m^nat_{l''}(l) > 0 since S_{l''} \ ([1,l] ∪ T(l)) is infinite; c_l > 0 as a minimum of finitely many positive numbers
((W4) is a finite list: supp y_l is finite); g_l > 0; delta_comb, delta_sh > 0 by their definitions; Hoffman constants are finite
(Hoffman's lemma for finitely many systems); C_L(l), N_L(l) exist by the Lojasiewicz inequality (V2 Lemma L).
(c) No step mentions N: patterns, objects and maxima run over subsets of [1,l] and over the blocks m(l'') of carriers l'' <= l
(at most l of them).  For p_N, objects that involve carriers l'' with m(l'') > N receive the rate value 1 (V1-ref (p0)), and
row constructions that use OWNERS (V4 Construction SA, Theorem 3.5, Prop. 5.3, Lemmas 4.4, 5.5) are run over L_N := {l : m(l) <= N}
with o_N(j) := min{l in L_N : u_l(j) != 0} (V4-ref R3); both are statements about rows, not about T_final.  QED

## 1.5 Theorem A_final (admissibility and Martin's Lemma B).  PROVED.
(a) T_final is admissible (note, def:admissible): (T-a) q^*(T e_{k,m}) = c_{j(k,m)} <= 1 = c_1; (T-b) injective; (T-c)
    Y := T_final(l_1(N x N)) satisfies Y ∩ c_00 = {0}; (T-d) for every m, {u_{j(k,m)} : k in N} is norm dense in S_{q^*}.
(b) (Martin's Lemma B conclusion.)  ||T_final|| = 1, T_final is injective, its range Y is a separable operator range in
    (c_0,q)^* = (l_1, q^*), Y is dense, Y ∩ NA((c_0,q)) = Y ∩ c_00 = {0}, and for every m the normalized vectors
    T e_{k,m}/q^*(T e_{k,m}) = u_{j(k,m)} are dense in S_{q^*} (hence in S_Y).
(c) (P1): y_l in c_00, ||y_l||_1 <= 1, n_l in [3/4, 5/4], supp y_l ∩ S_{l'} = {} (l' >= l); for s in S_l: u_l(s) = v_l(s) =
    delta_l 2^{-s}/n_l, u_{l'}(s) = 0 (l' < l), u_{l'}(s) = y_{l'}(s)/n_{l'} (l' > l).  (P2): sum_{l' > l} c_{l'} <= (4/3) c_{l+1},
    sum_{l' > l} lambda_{l'} <= c_{l+1}/3 <= b(l, M(l))^2/3.  Sub-window (P3): for every w = (l,i), T_hi(w) l 2^{l^3} Q(w) <= 1,
    n(w) >= l 2^{l^3} Q(w) >= l 2^{l^3} Design(l) >= l 2^{l^3} Lambda°(l), T_hi(w^+) <= T_lo(w), b(w) < u(w) = b(w^-), the bands are
    pairwise disjoint, and sum_{l' > l} lambda_{l'} <= b(w)^2/2 <= T_lo(w)^8.
(d) V2's relations (2.1): beta(w) := (1 + Lip(l) C_*(l)) b(w) <= eta(w) < 1/C_L(l) and C_L(l) beta(w)^{2/N_L(l)} <= eta(w).
Proof.  (T-a): q^*(u_l) = 1 and c_l <= c_1 = 1 by (W1).  (P1): q^*(y_l) = 1 and ||y_l||_1 <= q^*(y_l); q^*(delta_l h_l) <=
(1 + ||U||) delta_l H_l <= 1/4 because delta_l <= delta^max_l; so n_l in [3/4, 5/4].  The support statement is allowedness (a)
(FD targets and y^(1) live in Z_0); for s in S_l the other signatures vanish (disjointness) and targets y_{l'} with l' <= l vanish
on S_l by (a).  (P2): (W1) gives c_{l'+1} <= c_{l'}/4, and lambda_{l'} = m 2^{-m-k} c_{l'} <= c_{l'}/4 (k, m >= 1); (W2) gives
c_{l+1} <= b(l, M(l))^2.
(T-b), (T-c): verbatim the proof of thm:SLD.  Let x in l_1(N x N), indexed by l, with Z := T x = sum_l x_l c_l u_l in c_00 and
x_{l'} != 0.  For s in S_{l'}, by (P1), Z(s) = x_{l'} c_{l'} delta_{l'} 2^{-s}/n_{l'} + sum_{l > l', s in supp y_l} x_l c_l y_l(s)/n_l.  If the
last sum is non-empty with least index L(s), then (W4) at stage L(s) (tau <= 1) gives 2c_{L(s)} <= 2^{-2s} c_{l'} delta_{l'}, so the sum is
at most (4/3)||x||_inf sum_{l >= L(s)} c_l <= (16/9)||x||_inf c_{L(s)} <= (8/9)||x||_inf 2^{-2s} c_{l'} delta_{l'}; hence |Z(s)| >=
c_{l'} delta_{l'} 2^{-s}(|x_{l'}|/n_{l'} - (8/9)||x||_inf 2^{-s}) > 0 for all large s in S_{l'}, contradicting Z in c_00.  So x = 0.
(T-d): fix m and i.  supp y^(i) is finite, so it meets finitely many S_{l'}; hence y^(i) satisfies (a) and (c) at every
l >= l_i := max(supp y^(i) ∪ {l' : S_{l'} ∩ supp y^(i) != {}}) + 1.  Since i occurs infinitely often in (i_r) and k_r -> infinity,
y_l = y^(i) for infinitely many l = j(k_r, m) (these l -> infinity because j(., m) is strictly increasing).  Along them
q^*(u_l - y^(i)) <= |1/n_l - 1| + q^*(delta_l h_l)/n_l <= 4 q^*(delta_l h_l) <= 5 * 2^{-l} -> 0 (|n_l - 1| <= q^*(delta_l h_l)).
As (y^(i)) is dense in S_{q^*}, so is {u_{j(k,m)} : k}.
(b): ||T_final|| = sup_{k,m} q^*(T e_{k,m}) = 1 (l_1 domain; c_1 = 1 is attained at (k,m) = j^{-1}(1)).  Y is the range of a bounded
operator on a separable Banach space (an operator range, separable).  Y is a linear subspace whose closure contains the dense
subset {u_{j(k,1)}} of S_{q^*}, hence the closed unit ball, hence all of l_1: Y is dense.  Y ∩ c_00 = {0} is (T-c), and
NA((c_0,q)) = c_00 (prop:smooth(c)).  Density of the normalized vectors is (T-d).
(c) sub-window part: T_hi(w) <= 2^{-l^3}/(l Q(w)) and n(w) >= l 2^{l^3} Q(w) by (6); Q(w) >= Design(l) >= Lambda°(l) (u <= 1/4, all
Design factors >= 1); T_hi(w^+) <= T_lo(w) by (6) (for w^+ = (l+1,1) as well).  b(w) <= eta(w) <= T_lo(w)^4 <= 2^{-4n(w)}, and
n(w) >= Q(w) >= (4/u(w))^{20} >= 16/u(w), so b(w) <= 2^{-64/u(w)} < u(w) (u <= 1/4); u(w^+) = b(w) by definition; consecutive open
intervals of a decreasing sequence are disjoint.  Finally sum_{l'>l} lambda_{l'} <= b(l, M(l))^2/3 <= b(w)^2/2 since b is decreasing
along the sub-windows of a level, and b(w)^2 <= T_lo(w)^8.
(d): beta(w) <= min{eta, (eta/C_L)^{N_L/2}} gives C_L beta^{2/N_L} <= eta; eta(w) <= T_lo(w)^4 <= 2^{-4 l^3} < 1/Design(l) <= 1/C_L(l). QED

## 1.6 Theorem F (feature list).  PROVED.
T_final, U_final have every design feature used by the refereed results of Rounds 5-7:
 (F1) SLD structure (D0), (D1)(a),(b), (D2), (P1)-(P3) (per sub-window), so all of Section 8 of the note (Theorem 1.5(c));
 (F2) bounded gaps G_l = 2^{l+1} and allowedness (c) (Y3 D_sigma), j_0 = 1 notin union S_l;
 (F3) diagonal base with positive entries (V1/V2/Y4-ref/V4 diagonal-base statements) and mu_s = 2^{-s^2-1} (V3 D^mu, (RR));
 (F4) private bank and pull coordinates: every far coordinate of every S_l, with bounded gaps (Y4-ref C.2-C.7, V1 Lemma TU);
 (F5) pigeonhole sub-windows M(l) = omega(l)+1, u(w) = b(w^-), Q(w) = (4 Design/u)^{omega+20} (Y1 D_X, Y4 D^PW with Y4-ref A.3, V1);
 (F6) rate scheme: Y1's rooms/target rooms/threshold distances/relative positions, V1 (R1)-(R7) (ray components, shift costs, joint
      ray objects), V2 determinantal objects (all minors) and shift-pinning objects with enlarged patterns (V2-ref P3);
 (F7) b(w) a design power of T_lo(w) absorbing the Lojasiewicz exponent (V2 Def. 2.2(iii)); tuning eta(w) = T_lo^4/(l Design);
 (F8) Design(l) dominating G^*, H_comb, D(l), G^**, Xi^Y (hence Xi' of D''' and the SLD_G factor), 2^{s_max}/delta_min, 2^{G(l)},
      H_tune, the bank/pull factor (B_mu replacing 8^sigma), Lip, 1/delta_comb, (rows cols)^l, C_*, C_L, 1/delta_sh, |T(l)|;
 (F9) c_{l+1} <= c_l/4, <= b(l,M(l))^2 (<= T_lo(l,M(l))^3), <= (delta_{l+1} H_{l+1})^2 (V1; Z4 Thm A'', Cor. 4.2, 5.4);
 (F10) V4: (SF*) and (SF_tau) with tau_l = 2^{-l} -> 0 (both halves), (b'), (Z0) with p, p', p'', p''' = 3, 5, 7, 9, (GM) for l >= 2,
      (FD); the R6 recursion order (y_l, delta_l, then c_l); owners relative to L_N in row constructions;
 (F11) N-independence (Lemma W(c)).
Proof.  (F1)-(F9), (F11): Theorem 1.5, Lemma W and the definitions.  (F10): (SF_tau) first half for level l is (W7) at stage l+1
with (P2): (1 + ||U||) sum_{l''>l} lambda_{l''} <= (1 + ||U||) c_{l+1}/3 <= 2^{-10} tau_l lambda_l delta_l 2^{-(m+k+min S_l)} eta_l/n_l, and
(SF*) follows (tau_l <= 1); the second half is (W5) (l >= 2); (b') is (W4); (GM) for l >= 2 is (2) and (W6); (Z0) by (D0_final)(v)
(3, 5, 7, 9 are odd, so in Z_0); (FD): every block m has the infinitely many stages l = j(2^r, m), r >= 1; there y_l =
e_{j_l}^*/q^*(e_{j_l}^*) with j_l odd (not in any S_i) and fresh (not in supp y_{l'}, l' < l), so u_{l'}(j_l) = 0 for l' < l, i.e. j_l
is owned by l (also o_N(j_l) = l when m <= N); |y_l(j_l)| = 1/(1 + mu_{j_l}) >= 4/5 > (1 + ||U||)(0 + delta_l H_l), because
delta_l H_l <= 1/(4(1 + ||U||)).  QED

## 1.7 Conflicts and their resolution (each PROVED unless stated)
C1 (two diagonal bases: s_j = 2^{-j} in V1/V2 vs mu_s = 2^{-s^2-1} in V3).  RESOLVED by U_final = mu-base and B_mu(l) in Design.
  Proof.  (i) The note, Z3 Theorem E / Lemma U / Lemma 3.1 (it uses only the clamp formula at zhat, zhat^#), Y4 Lemma 2.2, V3 Lemmas
  2.1-2.3, Theorem 2.5 hold for every compact dense-range U.  (ii) Diagonal-base statements (Y4-ref C.1-C.7, V1 Lemma B, DR, TU,
  CO, ST, Corollary AC, V2 Theorem B, V3 Lemma VP', V4 Theorems 2.2, 3.5, 5.6, Prop. 5.3) use only the identities of 1.1 with
  general entries s_j > 0, plus explicit lower bounds on s_j^2 v_l(j) at bank coordinates.  (iii) The ONLY place where the
  numerical value s_j = 2^{-j} enters is that lower bound: V1 Lemma DR(ii) and Lemma TU use s_{s}^2 v_c(s) >= 8^{-sigma(l)}
  delta_min(l)/2 for bank coordinates s <= sigma(l).  For U_final, mu is decreasing, so for s <= sigma(l):
     mu_s^2 v_c(s) >= mu_{sigma(l)}^2 delta_min(l) 2^{-sigma(l)} (4/5) = (4/5) delta_min(l)/B_mu(l) >= Design(l)^{-1/6},
  because Design(l)^{1/6} >= l 2^{l^3} B_mu(l)/delta_min(l) >= (5/4) B_mu(l)/delta_min(l).  This is exactly the inequality used in
  V1 (Lemma TU: "s'^2 v' >= Design^{-1/6}"; Lemma DR(ii): mu^D = 2 nu Lam/(lambda_c s^2 v) <= 4 nu D(l) Lam (5/4) B_mu/delta_min <=
  Design Lam), and the second-order remainders of Lemma B(ii), C ||X||^2/nu^2 with ||X|| = mu^D mu_s <= mu^D, are bounded as in V1.
  (iv) ||U|| = 1/4 <= 1/2 wherever V1/V3 assume ||U|| <= 1/2.  (v) V3's (RR) needs super-exponential decay: for W = U_B and a
  power-law profile |a_s| ~ v_l(s)^{1+b} one has |a_s|/W_s ~ 2^{-b s}, so with entries 2^{-s} one gets M^W(y) ~ y^{2/b}, which is
  O(y^{1+eps}) only for b < 2 — the base 2^{-j} would NOT carry Theorem RS for b >= 2; with mu_s = 2^{-s^2-1}, V3 Lemma 3.1(b) applies to
  every b > 0.  Hence the mu-base is forced and V1's factor must be B_mu.
C2 (recursion order: note fixes c_l before y_l; V4 (GM)/(SF*)/(b') need y_l, delta_l before c_l).  RESOLVED by the R6 order of 1.3.
  Proof.  Every result uses allowedness (b) only as a property of the pair (y_l, c_l) ((W4) gives it, tau <= 1), and (T-d) only through
  "every target is eventually allowed", which is easier when (b) is enforced via c_l (V4-ref R6).  No result uses a LOWER bound on any
  c_l except through design factors (D(l), Lambda°, Design) that are computed after c_l.  (Checked: V1 2.4 uses lambda_c >= 1/D(l);
  Y1 D(l), Z6 D''' likewise; every window theorem uses only upper bounds (box bound, (P2)) and c_{l+1} <= c_l/4.)
C3 (three formulas for c_{l+1}: V1, V2, V4).  RESOLVED by taking the minimum ((W1)-(W7)); each result uses its term as an upper bound.
C4 (two b(w): V1 T_lo^4/(l Design) vs V2's Lojasiewicz-adjusted b).  RESOLVED by V2's b (smaller).  V1's estimates use only
  b(w) <= T_lo(w)^4/(l Design(l)) and the disjointness of bands; b enters lower bounds only through u(w^+) = b(w) inside Q(w^+),
  computed afterwards (V2-ref: "no lower bound on b(w) is used anywhere").
C5 (explosive window function of Z3-ref vs pigeonhole; lacunary signature sets of V4 Lemma 2.6 vs bounded gaps).  RESOLVED by
  pigeonhole + bounded gaps.  No result in the dependency trees of Master Theorems II/III' or Theorem RS' uses the explosive design or
  lacunarity (part 2): Y4 Prop. 1.2 shows the explosive design is insufficient against per-carrier rates, and the pigeonhole gives a
  clean sub-window at EVERY level; V4 Lemma 2.6 is a design remedy for (O4-crit), which T_final settles instead through D^mu + Theorem
  RS'.  V4 Lemma 2.6 itself (a statement about lacunary designs) does NOT hold for T_final and is not claimed.
C6 ((FD) and (Z0) targets).  (FD) targets differ across blocks, so the "same target sequence in every block" of Martin's proof of
  Lemma B is lost at the FD stages; this is harmless: only (T-a)-(T-d) are used (note, rem:lemmaB), and (T-d) holds per block.  (FD)
  serves only the NEGATIVE V4 Prop. 5.8; it may be dropped without affecting any positive statement (V4-ref).  Kept for completeness.
C7 ((GM) at l = 1 vs norm one).  V4-ref R6 imposes Phi_l <= g_l 2^{-l} at EVERY stage; at l = 1 this can force c_1 < 1, i.e.
  ||T|| < 1, violating "norm one" of Lemma B and the equality clause of (T-a).  FIX (adopted): (GM) only for l >= 2, c_1 := 1.  This
  is sufficient: (GM) is used only in V4 Lemma 3.4, whose conclusion concerns carriers l > log_2(2 Theta) + 1 >= 2.  (Alternatively
  rescale; but rescaling would break (GM) at later stages.)  [New precision, found in this audit.]
C8 (V3 Theorem RS' is stated over "SLD, D_sigma, SLD_G, D''', D_X, D^PW, D^Y" over the mu-base, not over D_Omega/D^{V2}).  RESOLVED in
  part 2 (R1/RS window use is generic: one sub-window per level suffices, (W*) is a hypothesis relative to l 2^{l^3} Lambda°(l) <= n(w)).
C9 (j_0 vs signature sets; Y3's example "S_l minus {j_0}").  With j_0 = 1 odd, j_0 notin union S_l: no removal needed.
