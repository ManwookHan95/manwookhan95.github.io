# H2 referee, part 1: Facts 1.1/1.2, Lemma 2.1, Lemmas 2.2-2.5 (first pass)

Sources checked: K2 notes 1-2, 4.1, 5.1-5.4, 6.1-6.3; K1 notes 1.0-1.5, 2.0-2.2, 3.1; K1-ref R-6; J1 notes 1-6, 8; J1-ref B-E;
Q1 notes 1.1-1.3 (design T_fin: S_l, Y_pool, rounds (r.1)-(r.4), absorbers, (S4) weights, (W_exp)).

## Fact 1.1 / 1.2 -- correct (mod chain)
(a) Near coordinates N_l lie in S_l ∩ (s_max(L), d(L)], private among coarse carriers; a thick one would make l thick-type.  So (R1)
    excludes thick near coordinates DIRECTLY (Lemma 2.1 is not needed).  No (P3)/(P4) => no kind (ii)/(iii), h = 0 (h is defined only
    through (P4) coordinates, K2.16 notation).  Anchors excluded by K2.17(b) since a near-certificate exists.
(b),(c) K2.16's kind list after (P); data-carrying carriers: off-F near coordinates are data-sign contacts (K1 2.1(b): a free near
    coordinate forces c_l = 0), thin ones data-sign (K1.3(S) with K1.2).  Re-derived the arithmetic: |c_l| v_l(s) <= 4|a^r_s|/t <= 8b/t vs
    |c_l| >= K_*^2 K t/(4D): contradiction since b <= T^4.
(d) unshifted block: Delta'_m = 0 => Delta''_m = Delta'_m kappa'/kappa^# = 0 (K1.1(2)) => peak data 0.  V1 Lemma D: robust coarse peak.
    Non-thick near coordinates => ZD after (P) => R-PK.  PRECISION: at a thin in-F near coordinate the ZD mass move has a common-mode
    term -(mu^2/nu) kappa_u a_s dm with |a_s| <= 2b (K2.4(i)); R-PK's column acquires -h_c gtil with |h_c| <= 2b Design, harmless
    (or lower to a contact first, cost <= b).
(e) re-derived: bank at a data-sign S_th near coordinate s of robust peak c (z_s = -sgn(Delta''_m) vs_c) moves kappa_m by
    -sgn(Delta''_m)(1 - X_m) lambda_c eff_s v_c(s) per unit.  "two-sided iff capacity >= 4W'": only "if" is proved (in (R1) TU on the peak is
    the only candidate; (P3)/(P4) need thick near coordinates).  Fine as used.
Fact 1.2: K2.16(3) with h = 0: gamma_0 = c_1/(4||h||) = +infinity, ||coef_(iv)||_2 >= c_1 - small, kappa <= -c_U/2 = -c_1/(8H).  Correct.

## Lemma 2.1 (extended R-G) -- correct
(R-mod') = (K2-c) covers s in [1, D(L)].  For s in F ∩ [1, D] \ T(L) robust: off U_L = anchor (K2.17(b)); in U_L: supp u_k = supp y_k ∪ S_k,
supp y_k ⊂ T(L) => s in S_k, private among coarse carriers (disjoint S_k; targets in T(L)), thick => k thick-type.  K2.16(4) holds at every
s <= D(L), so nothing restricts to s > s_max(L).  (Privacy is among COARSE carriers only; fine carriers may live at s via later absorbers;
that is the definition used by K2.16/J1.)

## Lemma 2.2 -- correct (does NOT need (D-enum))
Main targets: allowedness (a), (c+).  PRE absorbers: s in Sigma(Y_r) ⊂ [1, p_r - 2|supp Y_r| - 1] ⊂ [1, l_r] (|Sigma| <= |supp Y|), PRE stage > l_r.
CLUSTER absorbers at p+i: s in E^ch(p); its signature coordinates lie in T(p) (induction: <= p) or S ∩ [1, p]; p+i > p.  Odd p_i in Z_0.

## (D-enum) -- harmless, realizable
An enumeration of Y_pool with max supp y^(i) <= i exists (dovetail: position i draws from vectors supported in [1, i]); i_nu <= nu e.g.
1;1,2;1,2,3;...  Density of every block's targets (Lemma B) unaffected (every pool element still recurs; allowedness eventually holds).

## Lemma 2.3 (cluster sweep) -- correct with precisions
(a) lower bound on j: v_l(j) <= x''_max <= T^2 gives j >= 2 log2(1/T) - l - C >= 2n(w) - l - C.  Upper bound: v_l(j) >= c_0 W >= c_0 x =
    c_0 C T^4/p gives j <= 4 log2(1/T) + log2(p/c_0) + C <= 5 log2(1/T).
    s_max(p+1) >= p_R = p_0 + 2R, 2^{3-R} <= mu_{p_0}^2 lb^2/4 <= lb^2/4 => R >= 5 + 2 log2(1/lb) >= 2/T_lo(p, M(p)) (lb <= c^cl(p) <=
    exp(-1/T_lo(p, M(p))), (W_exp)).  T_lo(p, M(p)) <= T_lo(w) (last sub-window lowest).  So j < s_max(p+1).  OK.
    p' <= p + 2(s_max(p) + p) + 2(r+1) + 1 (D-enum gives |Sigma(Y_{r+1})| <= r+1) << 2n(w) <= j  (n(w) >= Q(w) >= (4 Design/u)^{20},
    Design >= 2^{D(p)} >= 2^{s_max(p)}).  Lemma 2.2 => j notin T(p').
    p'': j > p' so j notin E^ch(p'); PRE stages of round r+2 absorb Sigma(Y_{r+2}) ⊂ [1, r+2] (D-enum), main target of p'' ⊂ [1, r+2].  So
    j notin T(p'').  (D-enum) IS used here (and for |Sigma(Y_{r+1})|).
(b) Lemma 2.1 at p'.  OK.
PRECISION P-RANGE: H2 uses the pull range [c_0 W, x''_max] with x''_max = u^2 T^2/(C Design^C log^2(1/T)) > K1-ref R-6's x'_max =
u^2 T^3/(Design^2 |Lambda|).  Cost check (R-6 arithmetic): one carrier's pull/lowering/bank cost <= C Design x''_max log(1/T) = O(u^2 T^2/
(Design^{C-1} log(1/T))), times |Lambda| <= Design: theta'/c_flat^2 gains <= C/(Design^{C-2} log(1/T)) -> 0.  Pullability/super-thickness
must be re-defined with x''_max (lowering threshold |a^r_j| <= x''_max), as R-6 did with x'_max.  Window-level, no design change.
