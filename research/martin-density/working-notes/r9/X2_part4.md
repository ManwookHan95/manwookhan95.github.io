# X2 part 4 — (S2b) averaging AT the engineered approximant (Theorem E^eng) and (S2c) the threshold comparison

## 4.1 Theorem E^eng (windowed recovery through d-consistent engineered approximants of nearby rows; violated data allowed).  PROVED.
Let I be finite, f in S_{p*} with F finite, g in C(f), rho in (0,1), eta_0 in (0,2] with rho^2(1 + eta_0) <= (1 + rho^2)/2, delta as in 3.
Suppose there are base rows f_j -> f (eps_j := p*(f_j - f)) and, for every j, a window S_j := {T_j 2^{1-i} : 1 <= i <= n_j} with a window
family at f_j (pieces g_{j,t}, t in S_j) satisfying (U1)-(U7) with FIXED A_0, A_2, gamma_B, and in addition
 (E-c) p*(g - g_{j,t}) <= K_j t for t in S_j;
 (E-d) K_j T_j -> 0 and n_j c_flat(j)/K_j -> infinity, theta_j/c_flat(j)^2 -> 0 (c_flat(j) := c_flat of Theorem UE for the window's gamma_B;
       an f-constant when gamma_B is fixed);
 (E-e) eps_j <= theta_j (T_j 2^{-n_j})^2 with theta_j -> 0;
 (E-f) the window conditions (W-a), (W-b) of Theorem UE hold at f_j, and the THRESHOLD COMPARISON 64 rho eps^{viol}_j <= delta s_late(j)
       holds (eps^{viol}_j := max over the pieces of the violation mass; s_late(j) the bound (LATE) of Theorem UE at f_j).
Then (f, rho g) in cl NA((c_0, p_N), l_2^2).  If the hypotheses hold for every rho < 1, then (f, g) in cl NA.
Proof.  Fix j large (conditions below).  Put n := n_j, K := K_j, t_i := T_j 2^{1-i}, T := t_n = T_j 2^{1-n}.  Theorem UE at f_0 := f_j (p*(f_j - f)
<= r_f/2 for j large) with s_1 := s_late(j) (admissible by (E-f)), N_w with tail_W <= min(c_late delta T/A_0, T^3) and N'' as in 3.2(iv), gives a
norm-attaining f'_j and g'_{j,i} with
 (A^eng) p*(f'_j + tau g'_{j,i}) <= 1 + (tau^2/2)(1 - delta) for |tau| <= c_flat t_i;
 (P)     p*(f'_j - f_j) <= K_w Pi log(e/Pi) and p*(g'_{j,i} - rho g_{j,t_i}) <= K_w(K_w s_1 + c_fine + tail_W)/t_i =: e_{j,i}.
Since Pi <= K_w s_1 and s_1 = s_late(j) is a window quantity, choose (by (LATE) one may decrease s_1 below s_late as long as (VT') holds;
if 64 rho eps^{viol}_j < delta s_late, decrease s_1 to max(64 rho eps^{viol}/delta, s_1 small enough); if eps^{viol} = 0 any small s_1 works)
the stage so that eps'_j := p*(f'_j - f) <= eps_j + K_w Pi log(e/Pi) <= 2 theta'_j T^2 with theta'_j -> 0, and e_{j,i} <= K t_i — possible when
K_w (K_w s_1 + c_fine + tail_W) <= K T^2, which holds under (E-f) by (W-a) and s_1 <= s_late (s_late contains the factor T^3; see 4.2 for the
explicit check at U1's companions).  Two bounds for every i and real r:
 (A) if |r| <= c_flat t_i: p*(f'_j + r g'_{j,i}) <= 1 + (r^2/2)(1 - delta);
 (B) always: p*(f'_j + r g'_{j,i}) <= p*(f + r rho g) + eps'_j + |r| p*(g'_{j,i} - rho g) <= s(rho r) + eps'_j + 2 rho |r| K t_i
     (g in C(f); p*(g'_{j,i} - rho g) <= e_{j,i} + rho K t_i <= 2 K t_i for rho >= 1/2, and <= (1 + rho) K t_i in general).
Put gbar_j := (1/n) sum_i g'_{j,i}; by convexity p*(f'_j + r gbar_j) <= (1/n) sum_i p*(f'_j + r g'_{j,i}).  Let r_0 := min(sqrt(delta), sqrt(1 - rho^2),
c_flat t_1)... precisely r_0 in (0, 1] with r_0^2 <= min(delta, 1 - rho^2).
Case |r| <= r_0.  I_r := {i : c_flat t_i < |r|}; sum_{I_r} t_i < 2|r|/c_flat.  If I_r is empty, all terms obey (A) and 1 + (r^2/2)(1 - delta) <=
1 + r^2/2 - r^4/8 <= s(r) because r^4/8 <= delta r^2/2 (r^2 <= delta... <= 4 delta).  Otherwise |r| > c_flat T, so eps'_j <= 2 theta'_j T^2 <= 2 theta'_j
r^2/c_flat^2, and
   p*(f'_j + r gbar_j) <= max{1 + (r^2/2)(1 - delta), s(rho r)} + 2 theta'_j r^2/c_flat^2 + (1/n) 2 rho |r| K (2|r|/c_flat)
                       <= max{1 + (r^2/2)(1 - delta), s(rho r)} + r^2 min(delta/4, (1 - rho^2)/6)                      (j large: theta'_j -> 0,
                                                                                                                         n_j/K_j -> infinity)
                       <= s(r),
using 1 + (r^2/2)(1 - delta) + delta r^2/4 <= 1 + r^2/2 - r^4/8 (r^2 <= delta) and s(rho r) + (1 - rho^2) r^2/6 <= s(r) (lem:slack(a), |r| <= 1).
Case |r| >= r_0.  By (B) for all i: p*(f'_j + r gbar_j) <= s(rho r) + eps'_j + 2 rho |r| K (2 T_j/n) <= s(rho r) + (1 - rho^2) r_0 |r|/3 <= s(r), once
eps'_j <= (1 - rho^2) r_0^2/6 and 4 rho K_j T_j/n_j <= (1 - rho^2) r_0/6 (true for j large by (E-d)), using lem:slack(a) and min(r^2, |r|) >= r_0 |r|.
Hence gbar_j in C(f'_j), so (f'_j, gbar_j) attains its norm (prop:reduction(d)), and ||(f'_j, gbar_j) - (f, rho g)|| <= eps'_j + p*(gbar_j - rho g)
<= eps'_j + (1/n) sum_i 2K t_i <= eps'_j + 4 K_j T_j/n_j -> 0.  QED
Remarks.  (a) Unlike Z3's Theorem E (and V1's E'', V2's E^>=, E^SC), no exactness of the averaged data and no final call of cor:D1 /
thm:engineered at f_j is needed: the averaging is carried out at the norm-attaining point itself, with the per-piece bounds (A) of
Theorem UE.  This is what makes violated data usable along a sequence of windows (U3's (S2b)).  (b) The scale decoupling (E-e) enters
exactly as in Theorem E (pieces too fine for the scale r are compared with the mate g of f).

## 4.2 (S2c) The threshold comparison at U1's companions; design addition (W_exp).  PROVED (arithmetic).
DESIGN ADDITION (W_exp): at every stage l+1 the weight rule of T_final / D^{U1'} additionally requires
      c_{l+1} <= exp(-1/T_lo(l, M(l)))       (an UPPER bound on the weight, chosen at stage l+1 after all sub-windows of level l).
Admissibility and N-freeness are unaffected: (T-a)-(T-d) use upper bounds on weights only through allowedness (b) and (W4)-type conditions,
which remain satisfiable (V4 Lemma 2.1's argument, U3's (W10)); in D^{U1'} the term is added to c_p^low (U1-ref 6.2), which does not depend on
R, so the absorber-target construction is unchanged; every window theorem uses weights only through upper bounds ((P2), the box bound, Lemma
GW of U4).  (W_exp) implies U3's (W10) and every (W_k) for large l.
Claim.  At the companion f^# of a clean sub-window w of a main stage L (U1 part 4), with T := T_lo(w), n := n(w):
 (i)   every window constant entering Theorem UE is at most exp(C_abs log^2(1/T)) for an absolute C_abs: n <= log_2(1/T) (T_lo = 2^{-n} T_hi);
       Design(L) <= n (n(w) >= l 2^{l^3} Q(w) >= Design); A_0 an f-constant; gap_min >= c_f T^4/(L Design) (U1-ref Proposition KN(b): active near-
       threshold Omega carriers gap >= c_f eta D(L) M, eta = T^4/(L Design); inactive ones >= c_f eta M; others robust or kind [1] with gap >= t^2 >= T^2;
       absorbers 3M/4); x_0 >= c_f gap_min Phi_min(L) >= T^5 (U1 Lemma 4.3: coarse carriers and absorbers do not contribute below s_0(f^#)); C_S <= C/q_0^2
       (U1 Lemma 4.3); lever constants (Lemma LV with (D-lev)) <= Design(L)^C; hence K_w <= T^{-C'} and s_late(w) >= T^{C''} for absolute C', C'' and
       small T;
 (ii)  the fine-origin violation mass, the fine weight c_fine and c_tiny are <= C_f c_{L+1} (U1-ref 5: total l_1-mass of all contributions of carriers
       at stages > L is <= C_f sum_{l' > L} lambda_{l'}; coefficients <= C_Delta lambda) — with (W_exp), c_{L+1} <= exp(-1/T_lo(L, M(L))) <= exp(-1/T)
       (T_lo(L, M(L)) <= T_lo(w));
 (iii) hence (W-a), (W-b) and 64 rho eps^{viol} <= delta s_late hold for all large L: exp(-1/T) <= T^{C''+2} delta/(64 rho C_f) for T small; and the
       requirement K_w(K_w s_1 + c_fine + tail_W) <= K T^2 of 4.1 holds with s_1 := max(64 rho eps^{viol}/delta, exp(-1/(2T))) <= s_late.
So U3's (S2c) holds for the design D^{U1'} + (W_exp).  (W10) alone does not suffice for the s_late obtained here: with gap_min ~ T^4 entering
K_w, the bound is s_late ~ T^{15} or smaller, while (W10) only gives eps^{viol} <= C_f c_{L+1} ~ T^{10}; whether a sharper late threshold would make (W10)
enough is not investigated (it is irrelevant: (W_exp) is a free design choice).  [Without (W_exp) the comparison is OPEN for D^{U1'}; it is a pure design choice.]
