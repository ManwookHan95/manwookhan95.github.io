# Dependency graph of MASTER THEOREM VI (r10/Q1_notes.md 3.1) — Round 11 audit

All paths relative to ctx/ = /tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx
Part I = paper/martin_density_note.tex ("[I]"); Part II = paper2/martin_density_note_II.tex ("[II]", refereed by paper2/refA (Secs 2-3),
refB (Secs 4-5), refC (Sec 6, Secs 1, 7); revisions in paper2/revision_log.md).

## 0. Counting rules and flags
- [I], [II]: proved in Part I / Part II: counts as refereed (no pass flag) — BUT only for the statement and the operator of that paper.
  Part II's operator is NOT T_fin: [II] uses the doubly exponential base mu*_s = 2^{-2^{2^s}} (def:II-base, ||U|| = 1/16), keeps the (FD)
  fresh-dominated stages (used in lem:II-scales(e)), fixed cluster weights c_{p+i} = c^low_{p+1} 4^{1-i} and Part-II absorber targets (p_0 chosen
  with (mu*_{p0})^{2^{2^{p0}}-1} < 2^{-R}); T_fin (Q1 1.1-1.3) uses mu_s = 2^{-s^2-1} (U4's base, ||U|| = 1/4), no (FD), GENERIC weights in
  [(1-2^{-l})c^max_l, c^max_l], Q1's absorber rule and Q1's Q(w).  Every [II] link therefore carries a TRANSFER edge "[II] statement => T_fin",
  which is asserted only through Q1 1.7 (survival audit) — see cluster D.
- Working-note result (rN/XX_notes.md) checked by its round referee: 1 pass; +1 for each later referee who RE-DERIVED it (citing = 0).
- Result proved in a referee's *_ref_notes.md: 1 pass (that referee); +1 if a later referee re-derived it.
- Round 10: Q1_referee_a (+ Q1_refa_notes, Q1_refa_part1..4) and Q1_referee_b (+ Q1_refb_notes, Q1_refb_part1..3).  A Q1 claim re-derived by
  both = 2 passes; a fix proved by only one of them = 1 pass; "spot-checked" = 0.5 (counted as 1 pass overall).
- FLAGS: [1P] exactly one independent referee pass; [INSP] the link is asserted "by inspection" / "verbatim" / "survives" without a written
  re-derivation of the hypotheses; [T] transfer of a statement proved for another operator/design to T_fin.

## 1. Top node and its direct proof (Q1 3.1)
MT VI (Q1 3.1).  T_fin, option (a): every N >= 1, every f in S_{p_N^*} with finite base support F lies in Rec(p_N).  Option (b): N = 1 (b1);
N >= 2 with rho_1(f) != 1 (b2).  Passes: 2 (refa G2, G3; refb Section 3 "escape search", verdict table) — modulo P2, P8 (refa).
Proof edges:
 E1  Step 1 clean sub-window at every main stage: V1 Theorem 2' / U4 Lemma GW / U4 Thm 2.2(c) (bands disjoint, u(w+) = b(w)), plus "(D1),(D2) only
     lower b" (Q1).  -> nodes L3-V1a, L2-U4c, L2-U4b (Sections 4-5); band disjointness for T_fin re-derived by refb 1.1(d).
 E2  Step 2 class + cube pigeonhole: U1 2.3 classes (U1-ref (p-a), 4.5), U1 Prop 2.2(c),(d) normalization; count |S| >= n(w)/D_cls(w).
     -> nodes L2-U1e, L2-U1f, Q-P8.
     -> P8 (refa only) [1P]; P2 order class -> Step A -> cube -> Step B (refa only) [1P].
 E3  Step 3 Theorem C^tr at w(L) for every main stage L >= l_f.
 E4  (b1) GEN_fin(b) + stage 1 in block 2 (X1-ref W2) — or route X alone (2.7(b)) [alternative, off-tree].
 E5  (b2) |rho_1(f)-1| > b(w) for L >= L_1 => stage 1 notin N_T.  (refa G3, refb E8: 2 passes.)
Corollaries: Cor VI.1 (= MT VI, f' := f): 2 passes.  Thm VI.2 (density <=> (LSC-trunc)_N) and Cor VI.3: 2 passes (refa G4, refb 5); edges to
[I] prop:reduction(b), lem:pair, prop:smooth(c), prop:approximants, lem:martintail ([I], refereed) and to the claim "the equality clause of
(T-a) is used in [I] only in def:admissible and admissibility checks (lines 144-154, 2344, 3990)" — re-checked by grep by refa (D2) and refb (1.5):
2 passes.  Z5 Prop 5.4 (T13a) is re-proved in Q1 3.3, so it is not a live edge.

(Sections 2-6: the nodes by layer; Section 7: the flagged links; Section 8: the four clusters.)

## 2. Layer R10 — results proved in r10/Q1_notes.md (referees: Q1_referee_a/refa_notes, Q1_referee_b/refb_notes)
Format: ID. statement used | proved in | passes | flags | edges (what it uses).

Q-T   T_fin (one recursion, 1.1-1.3: rounds PRE/MAIN/CLUSTER, (GM) for l >= 2, c_l generic transcendental over k_0(c_1..c_{l-1}) in
      [(1-2^{-l})c^max_l, c^max_l], (W_exp) only in c^cl(p), (D-lev) with n_l, X1 rate objects, b(w) = min(b_U4, b_X1) with (D1), (D2)) |
      Q1 1.1-1.3 | 2 (refa D1; refb 1.1-1.4) | precisions P7 (refa only), P8 (refa only), P-LIP (refb only), P-R (refb only) [1P each] |
      uses U4 T_final (L2-U4a), D^{U1'} (L2-U1d), X1 rate objects/(D1)/(D2) (L1-X1h), X2 (D-lev)/(W_exp) (L1-X2j).
Q-W   Lemma W_fin (well-founded; positive; N-free) | Q1 1.4 | 2 (refa D1, refb 1.1) | P7 (patterns over blocks of stages <= l; l_f after all
      blocks <= N have coarse carriers) [1P, refa]; P-LIP (Lip*(l) := max(Lip(l), max_kappa Lip_kappa) in delta_0(b), (D1)) [1P, refb] |
      uses Lemma QC(a)-(c) positivity via GEN_fin (L1-X1f, L1-X1g); U4 Lemma W(b) (L2-U4a).
Q-A   Theorem A_fin ((T-b),(T-c),(T-d); (T-a) with ||T|| = c_1 <= 1; Martin-type norm under option (a)) | Q1 1.5 | 2 (refa D2, refb 1.5) | — |
      uses U4 Thm 2.2 argument (L2-U4b), allowedness (a) for absorber targets, (W4''), Y_pool density; [I] def:admissible, rem:lemmaB,
      prop:smooth(c); X1-ref W1 (Martin's proof uses only ||T|| <= 1) — re-read by refb 1.5 ("read in the note") and refa D2: 2 passes.
Q-G   Lemma GEN_fin ((a) all non-weight data in the countable field k_0; (b) (c_l) algebraically independent over k_0) | Q1 1.6 | 2 (refa D3,
      refb 1.6 + F1 "B_kappa contains no datum of f") | — | uses X1 Lemma GEN (L1-X1g) for the conclusion Phi_{N_T} notin B_kappa.
Q-I   Survival audit I1-I10 and CONCLUSION "every refereed result on the tree of MT VI holds for T_fin with level read as main stage" | Q1 1.7 |
      I1-I10 arithmetic: 2 (refa D4; refb 1.2-1.4, with the extra lower-bound use P-R found by refb only); the CONCLUSION sentence: 0 written
      re-derivations — it cites U4/U4-ref (Lemma GW), U1-ref 6.3, X1 Lemma W'(4) (X1-ref 9), X2 6.1 ("PROVED by inspection") |
      [INSP][T] (cluster D) | uses L2-U4c (Lemma GW), L2-U1d, L1-X1i, L1-X2j.
Q-R   Route decision (route V with KN^tr for every class kind; route X off-tree) | Q1 2.0-2.1 | 2 (refa C1, A4, A5; refb verdict "one companion per
      (L, w, class)") | — | uses X2-ref 2.3 (absorber obstruction, L1-X2k), U1 Lemma 3.2/[II] lem:II-firsttouch (absorbers of the current
      cluster are first pairs at stages > L, i.e. fine carriers).
Q-CM  Lemma CM^tr (route-V companion: Step A := KN^tr with KN-1 holds; Step B := X2-ref CM' step (2'); claims (a)-(f)) | Q1 2.2 |
      (b) [statuses at f^#, margin mu/4]: 2 (refa C3 re-derived C Design c_{L+1} <= mu_min/16 and the G1-release effect O(D^2 c^4) << mu;
      refb re-did the arithmetic);
      (a) [exactness, Hoffman <= C(Design/u)^C, A_max]: cited from X1-ref 8(a), V2 Lemma H, U1-ref (p-c) — not re-derived in Round 10;
      (c), (d), (e), (f): taken "as X2-ref CM'" by BOTH Round-10 referees (Q1_refa_part2 C3: "(c) ... X2-ref CM'(b) with C2 above. (d), (e),
      (f): as X2-ref CM'"; refb: "reduction (i)-(iii) spot-checked only") => their content has ONE pass (X2-ref, who proved CM') [1P];
      refa C2 adds (1 pass) the kinds of the inactive Omega carriers (KN-lever kind [2], KN-1-held kind [2], D2-pushed kind [1']);
      REDUCTION CLAIM "X2-ref CM' uses Proposition KN only through (i) coarse statuses, (ii) kind-[3] rows, (iii) exactness of Gamma^#":
      refa C1-C3 (one full pass) + refb spot check [1P];
      precisions: P1 (D2-pushed inactive carriers are kind [1'], accepted by UE Step 3) [1P refa]; P2 (order class -> Step A -> cube -> Step B)
      [1P refa]; P-HOLD (hold EVERY nearly-neutral coarse strict non-peak of a (T)-block exactly) [1P refb] |
      uses L1-X1j (KN^tr), L1-X1k (KN-1), L1-X1l (S-0), L1-X1m (D2), L1-X1c (K1), L1-X1d (floor row + data + kind [3]), L1-X2l (CM'),
      L2-U1g (G1 release), L2-U1h (U1 Lemmas 4.1, 4.2 + U1-ref 7, 4.3, 4.5, 4.6), V1 TU/CO (L3-V1b, L3-V1d), Z3 Lemma 3.1 (L3-Z3).
Q-BR  Proposition BR (the KN^tr companion is a base row of Theorem UE: (U1)-(U7), (W-a), (W-b); window quantities) | Q1 2.3 |
      2 (refa C4; refb verdict: lever coordinate j(l) free, W_lev) | P3 ((U3) at Step-A supports holds only up to V_fine; residue = tolerated
      violation, excess <= 2(z x)_-) [1P refa — and X2-ref's C_mix' proof makes the same tacit step]; P4 (Step A uses a BOUNDED number of S_l
      coordinates; DC pulls in a v-window of ratio 2^{6G(L)}) [1P refa]; refb 1.4 (Step A uses at most the first element beyond s_max; j(l) =
      second element is a free contact) [1P refb, complementary to P4] |
      uses V1 TR(iii)-(iv) (L3-V1e) transferred to the KN^tr companion via X2-ref (c3') (L1-X2h) [T]; Lemma LV(a)-(c) (L1-X2f); (D-lev);
      U1 Lemma 2.1 (L2-U1b) for (U7); U1 Lemma 4.3 for C_S; Lemma DC step (5) for r_0 (L1-X2e).
Q-PM  Lemma PM (at the d-consistent approximant: nv' = nv^# on Omega; |C'_m - C^#_m| <= C_f c_{L+1} (clamp equation
      sum_k min(Phi_k(1-c)/c, v_k)^2 = 1); rho'_k/rho^#_k = [C'/(1-C')]/[C^#/(1-C^#)]; rho'_d <= 1 - mu/8; no status change along |P| <= r) |
      Q1 2.4 | 2 (refa A1, A2, C5, numerics pm_ref; refb 2.1-2.4 + independent 80-digit solver) — clamp equation also X2-ref 1.2: >= 3 |
      P5 (phrasing of (iv)) [1P refa]; natural peak via alpha-mass identity sum_{k in P}(rho_k - 1)Phi_k^2 = C/M [1P refb] |
      uses [I] lem:threshold, lem:F1 (clamp formula), X2 Def 1.4 + Lemma DC conclusion (L1-X2e), Lemma M2 ball (L1-X2c).
Q-S2  Lemma S2c^tr (g_min >= T^{5 Design+2}; K_w <= exp(C log^2(1/T)); s_1 := max(64 rho eps/delta, e^{-1/(2T)}) <= s_late) | Q1 2.5 |
      2 (refa F; refb 3) | — | uses Lemma QC(c) + X1-ref Q2 (L1-X1f); X2 Lemma UE-1 + (p-UE1)-(p-UE6) "K_w polynomial with ABSOLUTE exponents"
      (L1-X2g) [the absolute-exponent property is cited, not re-derived; both referees note the bound survives even exp(C log^3)]; (W_exp).
Q-C   Theorem C^tr (if infinitely many main stages have a clean w with a (class, cube) set of >= n(w)/D_cls(w)^2 scales, then (f, rho g) in cl NA) |
      Q1 2.6 | 2 (refa G1; refb "(E-c)-(E-f) arithmetic re-done") | P6 (Theorem E^eng is stated for FIXED gamma_B but used with gamma_B(w) -> 0;
      fine because its proof uses gamma_B only via c_flat(j)) [1P refa]; P8 for (E-d) [1P refa] |
      uses Q-CM, Q-BR, Q-PM, Q-S2, Theorem UE (L1-X2h), Theorem E^eng (L1-X2i), U1 Lemma 2.4 applied to E^eng's proof (L2-U1c: X2-ref +
      refa G1 = 2 passes for the transfer).
Q-P8  Window bookkeeping fix (D_cls <= C_{f,N} 3^{2L}(p_max+1)^N (Design/u)^{2CN} by support-first pigeonhole; p_max(L) in Design(L);
      Q(w) := (4 Design/u)^{omega(l)+l^2+20} or omega(l) >= 2^l) | Q1_refa_notes 2.7 | 1 (refa); refb F6 only remarks "C_U1 absolute should read
      eventually dominated" | [1P] | NOTE: Part II's D^{U1'} solves the same counting problem differently (def:II-DU1: Dbar(w) with exponent
      C_Gamma(P(L)+2L+2), P(L) = 2^{R_Gamma(L)}, Q(w) >= Dbar(w)^3), refereed in [II] — but T_fin's Q(w) (Q1 (S6)) does NOT contain Dbar(w).

## 3. Layer R9 — X1 (r9/X1_notes.md; referee r9/X1_referee.md + X1_ref_notes.md, ONE pass) and X2 (r9/X2_notes.md; referee
##    r9/X2_referee.md + X2_ref_notes.md, ONE pass).  None of these results is in Part II (grep: no Puiseux / KN^tr / floor row / Lemma DC /
##    Theorem UE / E^eng / (W_exp) in paper2/martin_density_note_II.tex).

### 3.1 X1 nodes (all used through Step A of CM^tr, the (S5)-(S6) design objects of T_fin, and S2c^tr)
L1-X1a Lemma K: if Omega ⊂ Q, k = kappa/theta = K(sigma, R^2), K(s,x) = [s + sqrt(s^2 x + s(1-x))]/(1-x), strictly increasing in both arguments;
       rho_l = m|r_l|k/Phi_l | X1 1.1; X1-ref 1 (re-derived; 60-digit solver) | 1 [1P] — the identities a^2 = Phi_P^2 + k^2R^2 + s_f, k = a +
       Phi_P^2 + s_f, rho_l = m r_l k/Phi_l are [II] cor:II-Rkt / prop:II-Rkt (U1-ref Lemma R-kt, refereed); the closed form and monotonicity in R^2
       beyond that: 1P.  refb E5 uses it (1 - R^2 >= sigma) without re-deriving it.  Used by: L1-X1b, L1-X1d (psi_d), KN^tr statuses, D1.
L1-X1b Lemma F (floor): P ⊇ P_rob, Omega_a ⊂ Omega ⊂ Q => rho_l >= rho^0_l := m|r_l|K(sigma_rob, R_a^2)/Phi_l | X1 1.2; X1-ref 2 | 1 [1P] |
       uses L1-X1a.  Used by: KN^tr Step 0 (F(r_1) <= 1 + C_* b), (X4^0) data for Delta' < 0.
L1-X1c K1 (ratios and Step-0 push computed with formula-1 kappa and the PATTERN's Omega, including active weak peaks; sigma' formula) |
       X1-ref 1 (proved by the referee) | 1 [1P] | uses [II] lem:II-kappa (formula 1).  Used by: KN^tr Step 0, rate objects, GEN (tau_m has no
       N_T weight — re-read by refb F1).
L1-X1d Floor-form row (X4^0) "vs_l gamma_l + Delta'_m m^2|r_l|K(sigma_rob, R_a^2) >= 0" in (T)-blocks; (ii) decomposition data satisfy it up to
       K t (lem:suplevel(f), eq:peakshift, 2.1(T) estimate |rho_l(f) - rho^0_l(r(f))| <= C D^2(b + c^2) in formula-1 convention (D3));
       (iii) kind [3] at f^# with KN-1 (X1-ref 3.3); (iv) weight-freeness of all rows/cofactor polynomials + W-fix (K_kappa := {R(m)^2 <= 1 -
       sigma_rob(m)/4}) | X1 2.1-2.2; X1-ref 3.1-3.4, 4 (D1, D3) | 1 [1P] (refb re-read the weight-freeness for "no f-datum", F1: partial 2nd
       pass for (iv) only) | uses [I] lem:suplevel, eq:peakshift; [II] V1 TR Step 5 shift trick (prop:II-transplant); U1-ref (p-c), (p-d)
       ([II] prop:II-ray).  Used by: CM^tr(c) through reduction item (ii) (kind [3] with the TRUE shift in (T)-blocks).
L1-X1e Lemma NLM: B_kappa := {Phi : F_Phi = max_{d in N_T} psi_d/Phi_d has a local minimum of value 1 on Z_kappa} has dim < |N_T| (semialgebraic Sard
       [BCR 9.6.2], Nash stratification [BCR 9.1.8]) | X1 2.3; X1-ref 5 (with W-fix) | 1 [1P].  Used by: L1-X1g.
L1-X1f Lemma QC: (a) mu_kappa(h) := 1 - max_{Y_1} G_h > 0; (b) Y_1 empty => F >= 1 + m_0 on Z, else dist(., Y_1)^{1/alpha_Y} <= C_Y(F - 1)_+
       [BCR 2.6.7]; (c) Puiseux: mu_kappa(h) >= c_kappa h^{beta_kappa} on (0, h_kappa]; Q1 mu(h) <= Lip(F) h; Q2 Design(L) >= 1/h_kappa; Q3 V2
       Lemma L on the compact semialgebraic K_kappa | X1 2.5; X1-ref 7 | 1 [1P] (Round 10 uses (c), Q1, Q2 as inputs; not re-derived) |
       uses L1-X1g (non-coincidence), [II] lem:II-loj.  Used by: KN^tr Steps 1-3, (D2), W_fin positivity, S2c^tr(i).
L1-X1g Lemma GEN: (c_l) algebraically independent over k_0 => (Phi_d)_{d in N_T} notin B_kappa (Tarski transfer; B_0 ⊂ V(P) over k^rc; norm of
       conjugates) | X1 2.4; X1-ref 6 | 1 [1P] for the algebraic argument; its application to T_fin (k_0 fixed before the weights; B_kappa contains
       no datum of f) = Q-G, 2 passes | uses L1-X1e, L1-X1d(iv).
L1-X1h Design objects of X1 at level l: minors and cofactor polynomials of Gamma^#(kappa, a) with (X4^0)/(X4)/U-rows for ALL patterns; QC data;
       eta'(w) := T_lo^4/(L Design); b_X1(w) from (D1), (D2) [(D3) dropped by S-0] | X1 2.6, 3.1; X1-ref 8, 9 | definitions; positivity and
       well-foundedness re-derived in Round 10 (Q-W): 2.  P-LIP (refb) [1P].
L1-X1i Design T^tr + Lemma W' (W1 option (a) outside the note's class but Martin-type; W2 norm-one carrier in block 2; W3 absorber R from the
       lower end, cluster maxima with (W1); W4 complete list of lower-bound uses) | X1 3.1; X1-ref 9 | 1 [1P]; W1, W2 re-derived in Round 10
       (refa D2, refb 1.5, F7) => 2 for those; W'(4) "every refereed result survives" = [INSP].
L1-X1j Proposition KN^tr (X1-ref 8 corrected statement): at every clean w of a main stage L >= l_f and every class a there is f^(1a) with
       (a) active ratios r'' on Z_kappa, robust minors/cofactor polynomials >= u/2; (b) (T)-blocks: active near-threshold rho <= 1 - mu_kappa(eta'/3)/2
       and inactive Omega values EXACTLY 0; (KN)-blocks: U1-ref Prop KN(b) with eta' for eta; (U)-blocks: active statuses <= 1 - eta' (rescaling
       s_m), inactive near-threshold carriers pushed inward by eta' (D2); all other coarse carriers keep robust status; (c) p*(f^(1a) - f) <=
       C_f Design(L) eta' log(1/eta') | X1 2.6; X1-ref 8 | 1 [1P] (Round 10: only the downstream arithmetic of CM^tr(b) re-derived) |
       uses [II] def:II-companionw ((C1), (C2)), L1-X1b, [II] lem:II-loj (+Q3), L1-X1f(a)(b), L1-X1g, [II] lem:II-TU (joint fixed point,
       block-triangular Jacobian), [II] prop:II-KN (lever push in (KN)-blocks), [II] lem:II-kappader (kappa continuous; peak push restoring
       kappa), [II] lem:II-compcost / lem:II-cost (costs), L1-X1a (statuses via K), L1-X1c.
L1-X1k KN-1 (necessity and realization of the EXACT hold of inactive Omega values of (T)-blocks at 0 inside the joint fixed point; the
       realization "is available (V1 Lemma TU for exactly swallowed carriers, far z-moves for carriers with room)") | X1-ref 8 (proved by the
       referee); Q1 2.2 adds the pull choice v_l(j_p) >= max(correction, c_{L+1}) | 1 [1P] for the necessity/realization; Round 10 checked only
       that the later G1-release drift (<= 4c_{L+1}^2) is harmless (refa C3, B3) and extended the hold to ALL nearly-neutral coarse strict
       non-peaks (P-HOLD, refb only [1P]).
L1-X1l S-0 (U1-ref's later steps, the G1 release and the true-vs-reference shift move statuses and shifts by <= C Design(L) c_{L+1}; dominated by
       mu since c_{L+1} <= b(w)^2 and b(w) <= mu/(8M)) | X1-ref 8 | 1 [1P] for the drift bound C Design c_{L+1}; the comparison with mu
       re-derived by refa C3 and refb (2) — but in route V the steps (1b), (1c) do not exist and the drifts are those of Step B; that S-0 covers
       route V's Step B was checked by refa only (C3, B3) [1P].
L1-X1m D2 (inactive near-threshold carriers of (U)-blocks pushed inward by eta', kappa restored) | X1-ref 4 (by the referee) | 1 [1P]; P1
       (their data are kind [1'], accepted by UE Step 3) refa only [1P].
L1-X1n Lemma EC (effective columns u_l - r_l tau_m weight-free) | X1 1.4; X1-ref | 1 [1P] — enters only through L1-X1d(iv).

### 3.2 X2 nodes (route V: the engineered approximant and the averaging)
L1-X2a Lemma M1 (masses off the support with diagonal base: (i) <U^*u, e_A - e> formula; (ii) ||e_A - e|| <= ||X||/nu; (iii) value moves) and
       Cor M1' | X2 1.1-1.2; X2-ref (re-derived, sharp bound) | 1 [1P] | uses [II] lem:II-base(b)-type diagonal identities (for mu*; for mu-base:
       U4 1.1, U4-ref).  Used by: Lemma DC, UE-1.
L1-X2b d-consistency identities (Def 1.4: nv'_k = nv_k on Omega => d'(omega) = d(omega), w'(k) = (C'/C)w(k), gap' = (C'/C)gap + (1 - C'/C),
       kappa^{+-} = 0, H' = (C/C')H) | X2 1.4; X2-ref (exact to 1e-16) | 1 [1P]; the consequence rho'/rho = [C'/(1-C')]/[C/(1-C)] re-derived by
       refa A1 and refb 2.3 => 3.
L1-X2b' Referee addition 1.2 (Omega = all coarse strict non-peaks => C_m frozen up to the non-Omega strict non-peaks) | X2-ref 1.2 | re-derived
       as Q-PM(ii) by Q1, refa, refb => 3 (no flag).
L1-X2c Lemma M2 (uniform ball r_f(eta_1): C, sigma, q_0, nu within 1/8; F ⊂ supp a''; the natural peak k^nat_m stays a peak with the same sign;
       transfer data persist) | X2 1.5; X2-ref (p-DC3) | 1 [1P] | uses [I] prop:continuity, lem:persistence, lem:transferdata.  Used by:
       Q-PM (slope >= 2Phi_*^2(1-c)/c^3 on the ball), l_f, Theorem UE Step 0'.  refb F2's alpha-mass identity gives an independent proof
       that a natural peak exists [1P refb].
L1-X2d Levers and (SEP) (definitions (Z-free), (Z-con), (TU), (S-mass)) | X2 2.1 | definitions; (S-mass) unused after (R-abs).
L1-X2e Lemma DC (if K_J|F(0)|_inf <= r/2, K_J C_2 r <= 1/4, K_J c_tiny <= 1/4, r <= r_0, v_l(j_p) >= r, then F has a zero P* with |P*| <= r;
       at f(P*): Omega carriers strict non-peaks with nv = nv^0; peaks with margin above the value moves stay peaks; values move <= delta_1 + C_lev r;
       ||X_lev|| <= C_2 r) + (p-DC1) r := 4K_J(1 + 1/A_min)(delta_1 + T^4 s_1) + 8K_J W_pull/A_min, (p-DC2) TU pulls are fixed O(1) moves,
       W_pull super-small, (p-DC3) | X2 2.2; X2-ref 2.1 | 1 [1P] (Round 10: only the pull-coordinate choice, P4/refb 1.4, and the radius vs
       r_0 ~ g_min/C_lev in (LATE)) | uses [I] prop:forced, prop:continuity, lem:F1 (clamp formula), Lemma M1, Sherman-Morrison,
       Poincare-Miranda.  Used by: Q-PM(i),(v), Theorem UE.
L1-X2f Lemma LV(a)-(c) for COARSE carriers ((a) active class G: (TU), bank j(l) = least element of S_l ∩ (s_max, inf) \ F^#, pulls with
       v_l(j_p) in [r, 2^{G(L)} r]; (b) inactive class G incl. KN-1-held: (Z-con); (c) class R: (Z-gen)); (D-lev) gives mu_{j(l)}^2 v_l(j(l)) >=
       1/Design(L); (p-LV1) n_l in (D-lev); (p-LV2) pulls lie in S_l ∩ (s_max, s_far] ⊂ E_c | X2 2.3 (proved at U1's companion WITH tuned
       absorbers); X2-ref 2.2 | 1 [1P] for the lemma; its application at the route-V (KN^tr) companion: X2-ref C_mix' proof + refa C4 (P4) +
       refb 1.4 => 2 for the application (but both use the 1P lemma) | (d) FALSE (X2-ref 2.3), not used.
L1-X2g Lemma UE-1 (explicit estimates at f'; K_w polynomial in n, A_0/T, 1/gap_min, 1/x_0, C_S, lever constants with ABSOLUTE exponents) +
       (p-UE1)-(p-UE3) | X2 3.3; X2-ref 3 | 1 [1P].  The "absolute exponents" property is load-bearing for S2c^tr; both Round-10 referees cite it
       and remark that a Design-dependent exponent would still be absorbed (exp(C log^3(1/T))) — so the conclusion is robust, the lemma is 1P.
L1-X2h Theorem UE (window family (U1)-(U7) at a base row f_0 in the r_f/2-ball, window conditions (W-a)-(W-c), (VT') 64 rho eps <= delta s_1,
       (LATE) s_1 <= s_late => the d-consistent engineered approximant f' is norm attaining, p*(f' - f_0) <= K_w Pi log(e/Pi), and per piece
       p*(f' + tau g'_i) <= 1 + (tau^2/2)(1 - delta) for |tau| <= c_flat t_i and p*(g'_i - rho g_i) <= K_w(K_w s_1 + c_fine + tail_W)/t_i) +
       (p-UE4)-(p-UE7), (c3') rho c_flat(2A_2 + C_Delta) <= 7, s_late := c delta (T gap_min x_0/(n A_0 K_w))^C | X2 3.4-3.5; X2-ref 3 ("re-derived
       line by line against thm:engineered") | 1 [1P] (Round 10: refa A3, P1, P6 partial re-reading) | uses [I] thm:engineered (proof),
       def:engineered, lem:anchor, lem:scrambling, def:SC, lem:block, lem:base, lem:bookkeeping, lem:TV, prop:rebalancing, lem:transferdata,
       lem:persistence, lem:approxfacts, lem:F1, lem:slack; [II] lem:II-VT (U3 Lemma VT + U3-ref F6); L1-X2a, L1-X2b, L1-X2c, L1-X2e, L1-X2g.
L1-X2i Theorem E^eng (base rows f_j -> f with window families (U1)-(U7) and (E-c) p*(g - g_{j,t}) <= K_j t, (E-d) K_j T_j -> 0, n_j c_flat(j)/K_j
       -> inf, theta_j/c_flat(j)^2 -> 0, (E-e) eps_j <= theta_j(T_j 2^{-n_j})^2, (E-f) (W-a), (W-b) and 64 rho eps^viol_j <= delta s_late(j) => (f, rho g)
       in cl NA) + (p-E1) K_w(K_w s_1 + c_fine + tail_W) <= K T^2 | X2 4.1; X2-ref 3 | 1 [1P]; P6 (gamma_B window-dependent) refa only [1P];
       subset version (U1 Lemma 2.4 transferred to E^eng's proof): X2-ref + refa G1 => 2 | uses L1-X2h, [II] lem:II-subset, [I] (convexity of p*).
L1-X2j Design D^{X2} = D^{U1'} + (D-lev) + (W_exp), "admissible, N-free, every refereed result survives" | X2 6.1 "PROVED (by inspection)";
       X2-ref (p-W) ((W_exp) only after MAIN stages), (p-LV1) | 1 [1P] + [INSP]; in T_fin the recursion part is Q-T (2 passes); the survival
       part stays [INSP] (cluster D).
L1-X2k Absorber obstruction (tuned zero-value absorbers cannot follow the levers; Lemma LV(d) false in the application) | X2-ref 2.3 | 1 [1P] |
       a NEGATIVE result: it justifies (R-abs)/route decision; MT VI does not rest on its truth (dropping absorbers is legitimate either way).
L1-X2l Lemma CM' (companion without absorber switching: (1a) Prop KN [now KN^tr]; (1c') kappa and Omega_act values restored, no absorber tuned;
       (2') G1 release + static-ownership recursion on J_fine (owner candidates (a) Omega_act, (b) coarse peaks of active blocks, (d) every carrier
       at a stage > L of an active block incl. absorbers; negative fine owners self-aligned, positive anti-aligned); claims (a) scrambling
       Scr_m(x) <= C(x/q^#_0)^2 for x <= x_0 = c_f gap_min Phi_min(L) and stage->L carriers of negative blocks are (R) peaks with margin
       >= q_0 delta°/2; (b) (b^{+-}, omega^{+-}) with b^+ := beta + chi V_proj + V_fine/2 represent g_t, p*(g - g_t) <= K t, kappa_w <= 1 + eta_0/2,
       kinds [1]-[3]; (c) violation mass eps(t) <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/T_lo(w), b^theta = 0 at violated free coordinates;
       (d) p*(f^# - f) <= theta_w T_lo^2) | X2_ref_notes 4 (proved BY the referee) | 1 [1P] (Round 10 did not re-derive (a)-(d); see Q-CM) |
       uses [II] prop:II-KN, lem:II-recursion, lem:II-domfine (U1 Lemma 4.2 + U1-ref 7), lem:II-SCi, lem:II-coststat, lem:II-trueshift
       (U1 Lemma 4.6(a)), def:II-compclass (2) (G1 release), MT IV' data representation (U1 Prop 2.2(e) as in [II] thm:II-MTIV proof);
       — all [II] statements are for the ROUTE-X companion (tuned absorbers, configuration (i)/(ii)/mixed with exact completions); their use
       at the route-V companion ("absorbers enter only as fine carriers, which those statements cover") is X2-ref's claim [1P][T].
L1-X2m Theorem C_mix' / repair (R-abs) | X2_ref_notes 4 | 1 [1P]; superseded as an assembly by Q-C (2 passes), which still rests on L1-X2l.
L1-X2n (S2c) with (W_exp), (p-W) | X2 4.2; X2-ref 3 | 1 [1P]; superseded by Q-S2 (2 passes).

## 4. Layer R8 — U1 + U1-ref (r8/U1_notes.md, U1_ref_notes.md), U4 + U4-ref (r8/U4_notes.md, U4_ref_notes.md), U3 + U3-ref (Lemma VT).
##    Most of these are integrated in Part II (Sections 2-5), hence refereed for PART II'S operator; the [T] edge to T_fin is cluster D.
L2-U1a U1 Lemmas 1.1-1.5: exactness certificate (data exact iff V(Domega) z-admissible off F; forced coefficient -Delta'' lambda_k w(k)),
       identities (E1), (E2), formula-1 kappa, derivatives of kappa, continuity of kappa (U1-ref 1) | U1 1.1-1.5; U1-ref 1 | [II] lem:II-cert,
       lem:II-kappa, lem:II-kappader (refereed).
L2-U1b U1 Lemma 2.1 (shift bound |Delta_m| <= (8C'^3/(sigma' M'^2 Phi_P^2))^{1/2} when Gamma' <= 2) | U1 2.2; U1-ref | [II] lem:II-shift.
       Used for (U7) of BR.
L2-U1c U1 Lemma 2.4 (averaging on a subset S_j of a window's scales, n'_j >= 48 rho^2 K_j/(c_flat(1 - rho^2)), K_j T_j/n'_j -> 0) |
       U1 2.6; U1-ref | [II] lem:II-subset (for thm:II-E / thm:II-Eshift).  Transfer to Theorem E^eng's proof: X2-ref 3 + refa G1 => 2.
L2-U1d Design D^{U1'} (rounds PRE/MAIN/CLUSTER, absorber targets with R from c^low, cluster weights, (W4''), sub-window data at every stage) and
       Lemma 3.2 under D^{U1'} (first touchers) | U1-ref 6.2-6.4 | [II] def:II-DU1, lem:II-DU1, lem:II-firsttouch — Part II's version has
       the mu*-base absorber rule (p_0 with (mu*_{p0})^{2^{2^{p0}}-1} < 2^{-R}), fixed cluster weights and Dbar(w) in Q(w); T_fin's version
       (Q1 1.2, generic weights, X1-ref W3 cluster maxima, R from lb_l) is Q-T (2 passes) with P-R (refb only).
L2-U1e Activity classes (thresholds A_{i+1} = K_* A_i, K_* >= 2D(L) x Hoffman; at most (J+1)3^J classes; read off the decomposition data) |
       U1 2.3; U1-ref (p-a), 4.5 | [II] lem:II-classes.
L2-U1f Cone Gamma^#(kappa, a) rows (X1)-(X5) with corrected (X4) "vs gamma/lambda + Delta' >= 0" (U1-ref 4.1), aggregation (4.2), ratio
       variables and cofactor minors (4.3), sign-preserving increments (4.4); Proposition 2.2(a)-(d) (projection error K t, Hoffman <= C
       Design^C/u, one shift ray, D_cls count) | U1 2.1, 2.4; U1-ref 4 | [II] def:II-Gamma, prop:II-ray (refereed; its (d) uses Dbar(w), see Q-P8).
       Proposition 2.2(e) (data with the common shift): [II] proof of thm:II-MTIV (route-X form with absorber coefficients); route-V form is
       L1-X2l(b) [1P].
L2-U1g G1 release (far parts S_{l''} ∩ (s_far, inf) of non-owner coarse carriers released into J_fine; values move <= 4c_{L+1}^2, kappa <=
       C Design c_{L+1}^2) | U1-ref 5 | [II] def:II-compclass(2) (route X).  Route-V use: L1-X2l (1P) + refa C3.
L2-U1h U1 Lemmas 4.1 (robust recursion; type-(d) carriers peaks with margin >= q_0 delta°/2 in configuration (i)), 4.2 (dominance; + U1-ref 7
       owners in absorber blocks), 4.3 ((SC) for negative blocks: Scr <= C(x/q_0)^2), 4.5 (cost, statuses), 4.6 (true shift Delta'' =
       Delta' kappa'/kappa^#; trace correction) | U1 4.2-4.7; U1-ref 7 | [II] lem:II-recursion, lem:II-domfine, lem:II-SCi, lem:II-coststat,
       lem:II-trueshift (refereed, route-X companion).  Route-V use (no tuned absorbers, mixed classes with static ownership, positive
       anti-aligned owners): L1-X2l [1P][T].
L2-U1i Lemma R-kt (statuses of Omega carriers are functions of the ratios u/kappa; R < 1; dk/dR^2 > 0) | U1-ref 2 | [II] cor:II-Rkt (with refA
       A-R8 uniqueness), prop:II-Rkt.
L2-U1j Proposition KN (exactification with threshold protection under (KN_{w,a})) | U1-ref 3.3 | [II] prop:II-KN (refereed; stated with eta).
       Used inside KN^tr for (KN)-blocks with eta' in place of eta: X1-ref 8 [1P] (a rescaling of the same argument).
L2-U1k MT IV' assembly | U1-ref 8 (single pass in r8) | [II] thm:II-MTIV (refereed).  NOT on the tree of MT VI (route X only; Q1 2.7).
L2-U4a T_final (U4 1.1-1.3 with fixes C1 (B_mu(l) = 2^{sigma(l)}/mu_{sigma(l)}^2 in Design: the base enters design constants only through the
       bank factor mu_{s'}^2 v(s')), C7 ((GM) only for l >= 2)), Lemma W | U4 1-3; U4-ref | 1 pass for the mu_s = 2^{-s^2-1} version [1P]; [II]
       def:II-Tfinal, lem:II-W, prop:II-bank for the mu*-base version.  T_fin inherits the mu-base => its relevant refereed source is U4 + U4-ref
       (1P) plus Q-T (2 passes, Round 10 re-derived the recursion but not C1's bank-efficiency computation).
L2-U4b U4 Theorem 2.2 ((T-a)-(T-d), Martin's Lemma B; (c) sub-window bands nonempty and pairwise disjoint, u(w+) = b(w) < u(w)) | U4 2; U4-ref |
       [II] thm:II-lemmaB, prop:II-subwindows; for T_fin re-derived in Round 10 (Q-A; refb 1.1(d) for the bands) => 2.
L2-U4c Lemma GW (window theorems use a window only through 4 properties; every window condition is monotone under enlarging Design(l) and shrinking
       b(w), T_lo(w), weights) | U4 4 "PROVED (meta-argument; inspection)"; U4-ref "correct" | [INSP] in r8; [II] lem:II-GW (refereed by refA).
       Used by: MT VI Step 1, I8, I9, X2 6.1, X1 W'(4), refa P8 ("Q only grows").
L2-U4d U4 4.4(a): V1 Lemma DR(ii) and Lemma TU re-verified for the mu-base (+ numerics tu_mu_check: 587 tests) | U4 4.4(a); U4-ref C1 | 1 [1P].
       This is the only refereed source of Lemma TU / bank efficiency for T_fin's base (Part II's lem:II-TU, prop:II-bank use mu*).
L2-U3  Lemma VT (violations of l_1-mass eps cost <= 2 rho|tau| eps; tolerated when 2 rho eps <= delta s_1/16; (V1)-(V3)) with U3-ref F6 |
       U3 + U3-ref | [II] lem:II-VT (refereed).  Its line-by-line merger into Theorem UE: X2 + X2-ref (L1-X2h, 1P).

## 5. Layer R7/R5 — V1, V2 (r7), Z3 (r5): all integrated in Part II
L3-V1a V1 Theorem 2' (clean sub-windows exist: omega(l) rate objects, omega(l)+1 pairwise disjoint bands) | V1 + V1-ref | [II] thm:II-clean,
       cor:II-clean (refereed); for T_fin's enlarged rate scheme (X1 objects, (D1), (D2)): Q1 3.1 Step 1 + refb E2 => 2.
L3-V1b V1 Lemma TU (exact two-sided tuning: pull at the largest j with v(j) >= eps_x, bank at s'(l); val^# = val^(2) + x exactly; others move
       <= C_T eps_x^2; masses <= C_T eps_x) | V1 + V1-ref | [II] lem:II-TU (mu* base) — mu-base: L2-U4d (1P).  MODIFIED USE in Q1 2.2 (KN-1
       holds: pull at a contact with v_l(j_p) >= max(needed correction, c_{L+1}), "the bank absorbs the rest") — asserted by Q1, only the (U3)
       consequence checked (refa B4/P3) [1P][T].
L3-V1c V1 Lemma ST (status table; stability under the threshold drift) | V1 + V1-ref | [II] lem:II-status.
L3-V1d V1 Lemma CO (cost and data of the companion) | V1 + V1-ref | [II] lem:II-compcost (+ [II] lem:II-cost).
L3-V1e V1 Proposition TR(iii)-(iv) (kinds [1]-[3] with A_2 = 22, gamma_B = gamma(w) = u min M/4; contact-like data at banks, t|b| <= |a^#| at pulls)
       | V1 4.1 + V1-ref | [II] prop:II-transplant(iii)-(iv) — proved for the d-neutral companion f^#_w under (SH_w), (VR_w).  Used for the
       KN^tr companion (shifted data, route V) via X2-ref (c3') and refa P3 [1P][T].
L3-V1f V1 moves (C1), (C2) (close tiny rooms / target rooms) | V1 + V1-ref | [II] def:II-companionw.
L3-V1g V1 Lemma D (every block has a robust coarse peak at a clean w) | V1 + V1-ref | [II] lem:II-donorpeak; independent proof by refb F2
       (alpha-mass identity) [1P refb].
L3-V1h V1 Lemma B (second-order cross effects of bank/pull masses, remainder <= C Design^2 size^2) | V1 + V1-ref | [II] lem:II-bankformula
       (mu*); mu-base: L2-U4d.  Used in KN-1's necessity argument and in Lemma M1/DC.
L3-V2a V2 Lemma H (Hoffman constant <= max(1, ||A||)^{n-1}/least NONZERO minor) | V2 + V2-ref | [II] lem:II-hoffman.
L3-V2b V2 Lemma L (Lojasiewicz simultaneous exactification) | V2 + V2-ref | [II] lem:II-loj (polynomials); semialgebraic extension on K_kappa
       (X1-ref Q3) [1P].
L3-V2c V2 Theorem B (all tiny minors made exactly zero at a companion; values only) | V2 + V2-ref | [II] thm:II-B.  Used for (U)-blocks /
       classes without active shift (Q1 2.1 table).
L3-Z3  Z3 Lemma 3.1 (companion cost p*(f^# - f) <= C c(delta)) | Z3 + Z3-ref | [II] lem:II-cost.
L3-Z5  Z5 Proposition 5.4 (T13a: density <=> Lemma Z at finite-F rows + (LSC-trunc)) | Z5 + Z5-ref | superseded: re-proved as Q1 3.3 (2 passes).

## 6. Part I leaves (all refereed; paper/martin_density_note.tex)
lem:threshold (|w(k)| = M min(1, nu_k/theta), theta = AM/C, M + C = 1), lem:F1 (clamp formula), lem:suplevel, eq:peakshift / eq:didentity,
lem:switchbudget, def:twopiece, def:engineered, thm:engineered (its PROOF is modified line by line in Theorem UE), lem:block, lem:base,
lem:bookkeeping, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence, lem:approxfacts, lem:anchor, def:SC, lem:scrambling, lem:slack,
prop:reduction, lem:pair, prop:smooth, prop:approximants, prop:continuity, prop:forced, lem:martintail, def:admissible, rem:lemmaB.
Remark: [I] is stated for admissible T (norm one); option (a) uses ||T|| = c_1 < 1.  The claim that [I]'s arguments use (T-a) only as
q^*(Te) <= 1 was re-checked by grep by both Round-10 referees (2 passes) — but it is a grep-level check of the equality clause, not a re-reading
of every [I] proof used on the tree under ||T|| < 1 [INSP, mild].

## 7. Flagged links (everything below is on the tree of MT VI; route X, Theorem S1/RT*(c), MT IV^tr, V4, MT II/III' are OFF the tree)

### 7.1 Links with exactly ONE independent referee pass [1P]
R9-X1 (single pass X1-ref; not re-derived in Round 10):
 1. Prop KN^tr chain, Steps 0-4 (Lojasiewicz point, Y_1-point, Puiseux point r'', joint TU fixed point) — r9/X1_notes.md 2.6, X1_ref_notes.md 8.
 2. KN-1 (exact hold of inactive Omega values of (T)-blocks) incl. its realization by Lemma TU with the enlarged pull v(j_p) >= max(correction,
    c_{L+1}) — X1_ref_notes.md 8; r10/Q1_notes.md 2.2 bracket.
 3. S-0 drift bound C Design(L) c_{L+1} (its application to route V's Step B: refa only) — X1_ref_notes.md 8.
 4. D2 (U-block inactive near-threshold pushes), D1, D3 — X1_ref_notes.md 4.
 5. K1 (formula-1 kappa with the pattern's Omega) — X1_ref_notes.md 1.
 6. Floor-form row (X4^0): data satisfaction up to K t, kind [3] at f^# — X1_notes.md 2.2(ii)-(iii), X1_ref_notes.md 3.2-3.3.
 7. Weight-freeness of Gamma^#(kappa, a) and psi_d (+ W-fix region K_kappa), Lemma EC — X1_notes.md 1.4, 2.2(iv), X1_ref_notes.md 3.4
    (refb re-read only the "no f-datum" consequence).
 8. Lemma K closed form/monotonicity, Lemma F — X1_notes.md 1.1-1.2, X1_ref_notes.md 1-2 (identities themselves in [II] cor:II-Rkt).
 9. Lemma NLM, Lemma GEN (algebraic proof), Lemma QC (a)-(c) with Q1-Q3 — X1_notes.md 2.3-2.5, X1_ref_notes.md 5-7.
R9-X2 (single pass X2-ref; not re-derived in Round 10):
10. Lemma CM' (a) scrambling, (b) representation, (c) violation count, (d) cost — r9/X2_ref_notes.md 4 (proved BY the referee); Q1's CM^tr(c)-(f).
11. Theorem C_mix' / (R-abs) as the route-V assembly — X2_ref_notes.md 4 (assembly re-done as Theorem C^tr, but resting on 10).
12. Theorem UE + (p-UE4)-(p-UE7), (c3') — r9/X2_notes.md 3.4-3.5, X2_ref_notes.md 3.
13. Lemma UE-1 (K_w polynomial with ABSOLUTE exponents) + (p-UE1)-(p-UE3) — X2_notes.md 3.3, X2_ref_notes.md 3.
14. Theorem E^eng + (p-E1) — X2_notes.md 4.1, X2_ref_notes.md 3.
15. Lemma DC + (p-DC1)-(p-DC3) — X2_notes.md 2.2, X2_ref_notes.md 2.1.
16. Lemma LV(a)-(c) + (p-LV1), (p-LV2) (proved at U1's companion; application at the KN^tr companion re-checked by refa P4/refb 1.4) — X2_notes.md
    2.3, X2_ref_notes.md 2.2.
17. Lemma M1/M1', Lemma M2 (uniform ball, natural peak), identities 1.4 — X2_notes.md 1.1-1.5.  [Lemma M2's natural peak also has refb's
    independent alpha-mass argument, itself 1P.]
18. The applicability claim "absorbers enter U1 Lemmas 4.1, 4.3, 4.5, U1-ref 7 only as fine carriers, which those statements cover" (route-V use
    of [II] lem:II-recursion/domfine/SCi/coststat at a companion without tuned absorbers, mixed classes with positive anti-aligned owners) —
    X2_ref_notes.md 4 proof of CM'.
19. (U3) at Step-A supports: pull data bound (c3') (X2-ref) and residue-as-violation (P3, refa) — two halves, one pass each.
R10 single-referee fixes (proved by one Round-10 referee only):
20. P8 window bookkeeping (support-first pigeonhole; p_max in Design; Q(w) exponent omega + l^2 + 20) — r10/Q1_refa_notes.md 2.7, Q1_refa_part4.md
    H-I.  (refb 1.7/F6 asserts instead that omega(l) -> infinity absorbs the N-dependent exponent — a different, unwritten argument.)
21. P2 order class -> Step A -> cube -> Step B — Q1_refa_notes.md 2.4.
22. P1 kind [1'] for D2-pushed carriers; P3; P4; P5; P6 (E^eng with window-dependent gamma_B); P7 (patterns over blocks of stages <= l; l_f) —
    Q1_refa_notes.md 2.2-2.8, D1.
23. P-LIP (Lip*(l) incl. Lip_kappa of F_Phi in delta_0, (D1)); P-R (absorber least entry eta_k >= mu^2 c^2/2^13 for U1-ref 7); P-HOLD (hold
    EVERY nearly-neutral coarse strict non-peak of a (T)-block); alpha-mass identity (natural peak, sigma_rob > 0) — r10/Q1_refb_notes.md 1.1, 1.3,
    2.2, 4 (E7).
24. The CM^tr reduction claim "X2-ref CM' uses Prop KN only through statuses, kind-[3] rows, exactness" — refa C1-C3 (one pass; the dominance and
    trace-correction items are not written out separately), refb spot check only.
R8 single-pass items still live because T_fin uses the mu-base:
25. U4 C1 + 4.4(a): Lemma TU / Lemma DR(ii) / bank efficiency mu_{s'}^2 v(s') >= Design^{-1/6} for mu_s = 2^{-s^2-1} — r8/U4_notes.md 3 (C1), 4.4(a),
    U4_ref_notes.md (C1).  ([II]'s lem:II-TU, prop:II-bank, lem:II-scales(d) are for mu*.)

### 7.2 Links that are only "by inspection" / survival / transfer [INSP][T]
 I-1. Q1 1.7 CONCLUSION: "every refereed result on the dependency tree of MT VI (3.5) holds for T_fin with 'level' read as 'main stage'" —
      no written hypothesis check; it chains U1-ref 6.3, X1 Lemma W'(4), X2 6.1 and U4 Lemma GW.
 I-2. X2 6.1 Design D^{X2} "PROVED (by inspection)" (r9/X2_notes.md 6.1; X2-ref "correct (PROVED by inspection)").
 I-3. X1 Lemma W'(4) and U1-ref 6.3 "lost features ((W5), (W6), (W7) at absorber/cluster stages) are unused on the tree" — inspection claims.
 I-4. U4 Lemma GW (r8/U4_notes.md 4: "PROVED (meta-argument; inspection)") — now [II] lem:II-GW (refereed), but its application to T_fin's
      modified Q(w) (P8) and enlarged rate scheme is again by "Q only grows".
 I-5. [II] -> T_fin transfer: every [II] tool on the tree (lem:II-TU, lem:II-status, lem:II-compcost, prop:II-transplant(iii)-(iv),
      prop:II-KN, def:II-Gamma, prop:II-ray, lem:II-classes, lem:II-recursion, lem:II-domfine, lem:II-SCi, lem:II-coststat, lem:II-trueshift,
      lem:II-firsttouch, def:II-DU1/lem:II-DU1, lem:II-hoffman, lem:II-loj, thm:II-B, thm:II-clean, lem:II-VT, lem:II-subset, lem:II-cost,
      lem:II-GW) is proved for Part II's operator (mu* base, FD stages, fixed cluster weights, Part-II absorber rule, Q(w) >= Dbar(w)^3), NOT
      for T_fin (mu-base, no FD, generic weights, Q1's absorber rule and Q(w)).  Neither Q1 nor its referees mention Part II.
 I-6. s_max(l) -> infinity for T_fin without FD stages ([II] lem:II-scales(e) uses FD) — true via fresh absorber coordinates, unwritten.
 I-7. Part I under option (a): "[I] uses (T-a) only as q^*(Te) <= 1" — checked by grep of the equality clause (refa D2, refb 1.5), not by
      re-reading each [I] result used on the tree with ||T|| = c_1 < 1.
 I-8. Q1 2.2 "the end of Step A IS X2-ref's step (1c')" and "route V takes from route X only the conclusions of KN^tr" — identification
      claims, checked by refa (C1, A5) only.

## 8. Clusters for re-verification (at most 4)
A. ROUTE-V COMPANION AND ITS DATA (Step A = KN^tr with exact holds; Step B = static ownership; CM' claims): items 1-6, 10, 11, 18, 19, 21, 22
   (P1, P3, P4), 23 (P-R, P-HOLD), 24, I-8.
B. GENERIC-WEIGHT THRESHOLD PROTECTION (X1's real-algebraic chain): items 7, 8, 9, 23 (P-LIP, alpha-mass), and the (S5)-(S6) QC objects.
C. VIOLATION-TOLERANT ENGINEERED APPROXIMANT AND AVERAGING (X2 analytic core): items 12-17, 22 (P6), and S2c^tr's use of item 13.
D. DESIGN TRANSFER TO T_fin AND WINDOW BOOKKEEPING (inspection links): I-1 ... I-7, items 20 (P8), 22 (P7), 25.
Links with >= 2 passes (no flag): T_fin recursion/W_fin/A_fin/GEN_fin/I1-I10 arithmetic, route decision, CM^tr(b), BR's window arithmetic,
Lemma PM (clamp equation: Q1 + refa + refb + X2-ref 1.2), S2c^tr arithmetic, C^tr's (E-c)-(E-f) arithmetic, MT VI quantifier order, (b1)/(b2),
Thm VI.2/Cor VI.3, subset averaging for E^eng (X2-ref + refa), and all [I]/[II] statements themselves.
