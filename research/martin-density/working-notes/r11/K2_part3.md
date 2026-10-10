# K2 part 3 (Round 11): bookkeeping (O-d) -- rate objects, omega(L), Design(L), (LATE), N-independence, well-foundedness

Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Design T_fin^* = Q1's T_fin over the base mu*_s = 2^{-2^{2^s}} with K1's (D-K1)
(K1_part4.md 4.1).  Stage structure (S1)-(S7) and Lemma W_fin: r10/Q1_notes.md 1.3-1.4.  Window quantities (S6): u(w), Q(w), n(w), T_hi(w),
T_lo(w), eta(w) = eta'(w) = T_lo(w)^4/(l Design(l)), b(w) = min{b_U4(w), b_X1(w)}.

## 3.1 Design T_fin^{K2} (insertions into T_fin^*).  Definition.
At every stage L (all insertions N-free):
 (K2-a) [in (S5), after the carriers u_k of stages <= L, d(L) and delta_min(L) are fixed, before Design(L)]
        H(L) := 2^{d(L)}/delta_min(L);  D(L) := the least D >= d(L) with  max_{k in Lambda_L} ||u_k 1_{(D, infinity)}||_1 <= 2^{-L^2} H(L)^{-4}
        (Lambda_L := coarse carriers of stages <= L; finitely many vectors of l_1, so D(L) exists);  U_L := union of supp u_k (k in Lambda_L).
 (K2-b) [in (S5)]  Design(L) := [Design(L) of T_fin^*] x (2^{D(L)} D(L) H(L)/(mu*_{D(L)})^2)^{C_D2}, C_D2 an absolute constant (>= 2).
 (K2-c) [rate scheme, (S5)]  add to omega(L):  (R-mod') |a_s| for s in [1, D(L)];  (R-room) 1 - |z_s| for s in [1, D(L)] (z_s := sgn a_s on F,
        so the object is 0 there).  2 D(L) objects, a design number.  [No spread, Sherman-Morrison denominator, c_alpha, beta_* or anchor
        object is needed for Sys-DC (Theorem K2.6 is a uniform dichotomy); K1's (R-lev) objects remain in omega(L) but are not used by K2.]
 (K2-d) [in (S6), after b(w)]  theta_0(w) := b(w)/Design(L)^{C_P}, C_P an absolute constant (C_P >= C_D2 + 4).
 (K2-e) [in (S6)]  b_X1(w) is defined with 2b in place of b in (D1) and (D2) (room for the preparation's value perturbation <= b).
Construction choices (not design): the deep-raise depth J(w) > D(L) and the truncation depth N_w > D(L) (both are chosen "large enough" in
K1 Theorem 5.1 / Q2 2.3 anyway).

## 3.2 Lemma K2.12 (well-foundedness, positivity, N-independence, monotonicity).  PROVED.
(a) Every inserted quantity of stage L is a function of quantities of earlier stages and of earlier steps of stage L: D(L) uses the u_k of
    stages <= L (fixed in (S1)-(S3)/(S7) at stage L), d(L) = sigma(L) + 6 * 2^{L+1} and delta_min(L); Design(L) uses D(L), H(L); omega(L) uses
    D(L); theta_0(w) uses b(w) and Design(L); b_X1(w) with doubled b uses the same data as before.  Hence Lemma W_fin(a) persists.
(b) All new quantities are finite and positive: D(L) < infinity (tails of finitely many l_1 vectors), mu*_{D(L)} > 0, b(w) > 0.
(c) No rule refers to N or to f.  For p_N the rate objects are evaluated on the coordinates present (V1-ref p0); their count 2D(L) is N-free.
(d) Monotonicity: (K2-b), (K2-c) only enlarge Design(L), omega(L) and hence Q(w) = (4 Design(L)/u(w))^{omega(L) + L^2 + 20}, n(w), and only lower
    T_lo(w), eta(w), b(w); (K2-e) only lowers b(w).  By U4 Lemma GW every window condition of Q1/Q2/K1 is monotone under these changes, so every
    window theorem used by K1 Theorem 5.1 survives.  The window count (cert3 Fix A: support-first pigeonhole, exponent omega(L) + L^2 + 20) is
    unchanged in form: the M(L) = omega(L) + 1 sub-windows have pairwise disjoint bands (b(w), u(w)).
Proof.  (a)-(c) by inspection of (K2-a)-(K2-e).  (d) U4 Lemma GW and Q1-refb 1.1(d) (the bands are nonempty and disjoint because u(w^+) = b(w)
< u(w); (D1)/(D2) only lower b).  QED

## 3.3 Lemma K2.13 (clean dichotomy at depth D(L) along the construction).  PROVED.
Let L >= l_f be a main stage, w a clean sub-window (clean for the enlarged rate scheme; exists by the pigeonhole of Q1 Theorem VI Step 1).
Then at f, for every s <= D(L): |a_s| <= b or |a_s| >= u, and 1 - |z_s| <= b or >= u (b = b(w), u = u(w)).  Along the construction
f -> f^r (deep raise beyond J(w) > D(L)) -> Step 0 (V1 (C1), (C2)) -> preparation (P) -> Step A -> Theorem UE^inf pre-row f_1 -> approximant f',
every coordinate s <= D(L) keeps its class: robust objects stay >= u/2, tiny ones stay <= 2b or become exactly 0 (closed rooms), or are
raised/banked to exactly the prescribed theta_0-masses, or are moved by Step A only through its own one-sided/two-sided resources.
Proof.  The deep raise changes a only beyond J(w) > D(L) and renormalizes q*(a) = 1 by a factor 1 + O(eps'_r), eps'_r <= theta_w T^2 << u;
(C1), (C2), (P1) only close rooms (z-moves to contacts); (P2), (P3) create/raise masses to theta_0 <= b; Step A moves by <= Design^C x with x =
C Design(L) eta' = C T^4/L << u (TS and FR coordinates keep >= u/2; S_theta masses only increase, K2.9 uses raise-only generators there); Theorem
UE^inf's pre-row and the levers move by <= K_w s_1 + K_DC r << theta_0 (Lemma K2.14 below); e moves by O(mu*_J) + O(Design T^3) << u (Q2-refa
part 4).  QED

## 3.4 Lemma K2.14 ((LATE) additions).  PROVED.
The following conditions are added to (LATE) (requirements on s_1, i.e. on the late threshold s_late(w)):
 (L-K2-1) s_1 <= theta_0 T/(8 rho A_0)                (theta piece at S_theta coordinates: masses stay >= theta_0/2; 1.6(c));
 (L-K2-2) Design(L) K_DC r <= theta_0/4               (range of the S_theta mass columns of Sys-DC in mass units; Step-A TU banks have mass
          >= beta x/4 >> theta_0, thick coordinates >= u/2, FR rooms >= u/2, ZD columns have no range limit);
 (L-K2-3) C_lev K_DC r <= min(gap_min, robust margins)/2   (statuses along Sys-DC; as Q1 Lemma PM (v));
 (L-K2-4) [only if the tolerance variant K2.1 is used]  C_f |Omega| A_2^2 K_w^2 s_1 <= c_late delta T^2.
The Sys-DC TU levers (X2 Lemma LV(a): pull pre-placed, bank continuous) keep X2's own range conditions (p-DC1/2 with cert C2-4), with K_DC
in place of K_J; these are of the same form as K1's (K_lev = Design^{C_0}/u) and hold by the same argument.
All hold with Lemma S2c^tr's choice s_1 := max(64 rho eps^viol/delta, exp(-1/(2T))) for T small (main stage L >= l_f).
Proof.  Lower bound for theta_0: b(w) is bounded below by a power of eta'(w) = T^4/(L Design(L)) with exponent and constants bounded by a power
of Design(L) (b_U4: (eta/C_L)^{N_L/2}/(1 + Lip C_*); b_X1: the clauses (D1), (D2) and b <= mu_kappa(eta'/3)/8 with mu_kappa(h) >= c_kappa
h^{beta_kappa}; all of N_L, 1/alpha_Y, beta_kappa, C_L, C_Y, Lip, C_*, 1/c_kappa are factors of Design(L), Q1 (S5)).  With Design(L) <= n(w) <=
log_2(1/T) (Lemma S2c^tr (i)) this gives log(1/b(w)) <= C log^3(1/T) and theta_0 = b/Design^{C_P} >= exp(-C log^3(1/T)).
Upper bounds: r <= exp(C log^2(1/T)) s_1 (proof of Lemma S2c^tr), K_DC <= C_{f,N} Design(L)^{C_0} <= C_{f,N} log^{C_0}(1/T) (Theorem K2.6),
C_lev, K_w <= exp(C log^2(1/T)) (Lemma S2c^tr (ii)).  Since s_1 <= (1 + 32 rho/delta) exp(-1/(2T)) (Lemma S2c^tr (iii): eps^viol <= exp(-1/(2T))/2) and
exp(-1/(2T)) <= exp(-C' log^3(1/T)) for T small, (L-K2-1)-(L-K2-4) hold for T small.  QED

## 3.5 Costs.  PROVED.
Preparation: p*(f^P - f^r) <= C D(L) theta_0 log(1/theta_0) + C_f p*(L^*(w^P - w^r)) <= C D(L) b log(1/b)/Design^{C_P - 1} <= b^{1/2} <= T^2
(b <= eta = T^4/(L Design)), i.e. o(T^2) with room; the normer change is controlled by Z3 Lemma 3.1 as for V1's banks.  Step A: as K1 Lemma
K1.6(A) with K_lev replaced by 1/eps_PS or by the cone weight Design^C (Lemma K2.9).  Sys-DC: as X2 Lemma DC with K_J replaced by K_DC.

## 3.6 Where each new object is used (audit).
 D(L): K2.6 Step 3 (tail of Psi^c beyond D(L) <= gamma/16 for L >= l_f, absorbing f- and N-constants by 2^{-L^2}); K2.10(a) (tail <= C_f
   2^{-L^2} H(L)^{-4} << gamma_0); preparation range; J(w), N_w > D(L).
 Design(L) >= 2^{D(L)}/mu*_{D(L)}^2: every design-depth resource has normalized efficiency >= 1/Design(L) (mass change: mu*_s^2/nu; z-move: 1).
 (R-mod'), (R-room): thin/thick and tiny/robust-room classification at depth <= D(L) (types S_theta, TS, FR of 1.6(d)); without them a
   coordinate with b < |a_s| < u could be neither raised (it is not tiny) nor used two-sided at scale x (x >= Design b).
 theta_0(w): S_theta masses; (L-K2-1), (L-K2-2).
 Doubled b in (D1): preparation's value perturbation <= C D(L) theta_0 <= b before the Lojasiewicz step.
None of the new objects enters K, D_cls, A_max or c_flat (which remain of the form design x u^{-C}); they enter only window constants
(K_DC, ranges) and (LATE).  Hence Lemma S2c^tr and Theorem E^{eng,RT,inf}'s hypotheses (E-c)-(E-f) are unchanged.
