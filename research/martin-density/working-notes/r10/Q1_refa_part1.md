# Q1 referee (a) — part 1: reading notes and first checks (working file)

Read: BRIEFING, BRIEFING_R2 (all addenda), martin_paper_summary; r9 X1_referee, X1_ref_notes, X2_referee, X2_ref_notes; X2_notes
parts 1-3 (Def 1.4, Lemma DC, Lemma LV, (U1)-(U7), Theorem UE + proof); X1_notes 2.1-2.6; U1_ref_notes 3-8; U1_notes 2.1-2.6, 3.1-3.5;
r10 Q1_notes.md in full (= Q1_notes_a + b + c), Q1_part0.

## A. Facts confirmed against the sources (PROVED, re-derived)
A1 (d-consistency, X2 Def 1.4).  f' d-consistent with f_0 on Omega iff every k in Omega is a strict non-peak of f' and nv'_k = nv_k
    (nv_k = zeta_m(k)/A_m).  Then rho_k = |nv_k| C/(Phi_k^2 (1 - C)) (lem:threshold: rho = nu/theta, theta = AM/C, nu = |zeta|/Phi^2), so
    rho'_k/rho_k = [C'/(1 - C')]/[C/(1 - C)] for every k in Omega.  Q1 Lemma PM(iii) is this identity.  CORRECT.
A2 (clamp equation).  ||D_m w_m||_2 = C_m and |w(k)| = min(M, C |zeta(k)|/(Phi_k^2 A)) give
    1 = sum_k min(Phi_k (1 - C)/C, v_k)^2,  v_k = |nv_k|/Phi_k.   So C_m is a function of the normalized values ALONE.
    Per-term change: |min(a,x)^2 - min(a,y)^2| <= 2a|x - y| with a = Phi_k(1-c)/c gives <= 2((1-c)/c)|nv'_k - nv_k|.
    Fine carriers (stages > L): sum lambda_k <= sum_{l > L} c_l <= (4/3) c_{L+1}; |u_k(xhat)| <= ||u_k||_1 ||xhat||_inf <= 1 + ||U||.
    Hence |C' - C| <= C_f c_{L+1} INDEPENDENTLY of the perturbation size, provided (i) Omega carriers are exactly d-consistent,
    (ii) every coarse peak stays clamped (margin > its value move), (iii) the natural peak gives the slope.  Q1 Lemma PM(ii) CORRECT
    (this is X2-ref's addition 1.2 with the crude but perturbation-free bound on the fine terms).
A3 (Theorem UE radius for kind [3]).  Only gap'(k) >= gap^0(k)/2 is used; no lower bound on the gap of kind-[3] carriers enters c_flat.
    In the theta regime the condition |s_1 rho omega^theta(k)| <= gap'(k)/2 needs s_1 <= T gap_min/(4 rho A_2): this is where the
    Puiseux margin enters (through gap_min).  Contained in (LATE).  CORRECT.
A4 (absorbers in route V).  U1's tuned absorbers (first pairs P(s), s in E_c(w), cluster of L) are all at stages > L (U1 Lemma 3.2:
    "among the carriers at stages > L whose vectors meet s, the first two ...").  Absorbers of EARLIER rounds are coarse block-1
    carriers at main stage L and are treated like every other coarse carrier (robust peak / Omega member with its private signature
    set S_l / pattern carrier).  So "route V never tunes an absorber; absorbers are ordinary fine carriers" is consistent.
A5 (KN^tr is per block and sign-agnostic).  X1 2.1: (U) unshifted / (KN) shifted with an inactive coarse carrier at rho in [u, 1 + b] /
    (T) shifted with every inactive coarse carrier at rho <= b or >= 1 + u.  The floor row (X4^0) is satisfied by the data for
    Delta'_dec < 0 by Lemma F (rho^0 <= rho) and for Delta'_dec > 0 by the small inactive mass of a (T)-block; nothing uses the signs of
    the OTHER blocks.  Hence KN^tr applies to mixed classes as well (the cone Gamma^#(kappa, a) fixes the sign of each active block by
    (X2), U1-ref 4.4).  X1 only USED it for one-signed classes (MT IV^tr) because route X cannot handle mixed classes; the companion
    construction itself is class-kind-agnostic.  CORRECT (Q1's step (1a) := KN^tr for mixed classes is legitimate).

## B. Items to scrutinize (list kept while reading)
B1 kind of the inactive Omega carriers pushed inward by eta' (D2, (KN)-block pushes): gap ~ eta' M << gamma_B, so not kind [2];
    kind [1] fails for t^2 > gap; they must be kind [3] — need omega^+-(k) inward-signed with bound 1.5 gap/t.  Check U1 Prop 2.2(e)
    (omega^+ := V1's clamped decomposition omega_+) and U1-ref 4.1 (X4) for inactive carriers (gamma = 0).
B2 Lemma PM(v): along the WHOLE lever cube the Omega carriers must remain strict non-peaks (Lemma DC's continuity/linearization); r_0
    <= gap_min/C_lev with gap_min ~ Puiseux margin.  Check that r (p-DC1) <= r_0 is really implied by s_1 <= s_late (delta_1 ~ Pi_X).
B3 KN-1 holds in route V: after Step B (G1 release) held values move by <= 4 c_{L+1}^2 — check KN-1's requirement is "small compared
    with mu" (it is: effect on statuses ~ D^2 c^4 << mu), not "exactly 0" in the sense of an identity used later.
B4 (U3) for KN-1 pulls: V_fine(j_p) ~ c_{L+1}/t (coefficients ~ lambda/t), pull mass 24 lambda_l v_l(j_p) with v_l(j_p) >= c_{L+1}:
    t|b| <= C_f c_{L+1} vs |a^#| >= 24 c_{L+1}/Design: K_3 ~ C_f Design — must be absorbed in (c2) (c_flat <= 1/(8 rho K_3)?).
    Check (c2) and V1 TR(iv) form "t|b| <= K_3 |a^#|".
B5 Option (b), N >= 2, rho_1(f) != 1: at a clean w, |rho_1 - 1| > b(w) => robust, so stage 1 notin N_T.  But the design constants
    (S5)-(S6) are restricted to patterns with stage 1 notin N_T — are there other places where carrier 1's rational weight enters a
    COINCIDENCE (e.g. stage 1 in N(m) of a (KN)- or (U)-block, or as a coarse peak weight in sigma_rob)?  Only N_T weights need
    genericity (GEN); peak weights and (KN)/(U)-block weights may be anything.  Check.
B6 S2c^tr(i): eta'/3 >= T^5 needs 3 L Design(L) <= 1/T; Design(L) <= n(w) and L <= n(w); T <= 2^{-n}: 3 n^2 <= 2^n. Fine for n >= 10.
    mu >= c_kappa h^{beta} needs h <= h_kappa: h = eta'/3 <= 1/Design <= h_kappa iff Design(L) >= 1/h_kappa: in (S5).
B7 Theorem C^tr's (E-d) count: n(w)/D_cls(w)^2 with D_cls containing f-constant C_{f,N}: the design cannot dominate f-constants, but
    l 2^{l^3} absorbs them for L >= l_f.  Check that Q(w)'s exponent C_U1 covers D_cls^2 * K/c_flat.
B8 Quantifier order: l_f depends on (f, N, g, rho); class/cube chosen per (L, w); T_0(f, rho) thresholds.  Check that no window
    constant is needed BEFORE w is chosen and that the pigeonhole class set S is fixed before the companion (U1-ref 2.2: classes read off
    the decomposition data at f, cube after step (1c)).
