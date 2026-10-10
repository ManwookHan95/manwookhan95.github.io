# cert0 — Round 11 independent re-verification, cluster A of the MT VI graph
# (route-V companion f^#: Step A = KN^tr with exact holds, Step B = X2-ref CM' static ownership)

Referee: cert0 (independent, adversarial).  Root: ctx/ = /tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx
Re-derived from the sources: r9/X1_notes.md 1.1-2.6; r9/X1_ref_notes.md 1-4, 8; r9/X2_ref_notes.md 3-4; r9/X2_notes.md 5.1-5.2; r10/Q1_notes.md 1.1-1.3,
2.0-2.3; r10/Q1_refa_notes.md (+ Q1_refa_part2.md C1-C5); r10/Q1_refb_notes.md (+ Q1_refb_part3.md); r8/U1_notes.md parts 1-5; r8/U1_ref_notes.md
1-8; r7/V1_notes.md 2.2, 3.1-3.6, 4.1-4.2; paper/martin_density_note.tex (lem:threshold, lem:anchor, def:SC, lem:scrambling);
paper2/martin_density_note_II.tex (def:II-compclass, lem:II-trueshift, prop:II-absorb, lem:II-recursion, lem:II-domfine, lem:II-SCi, lem:II-schauder,
lem:II-coststat).  Working notes: r11/cert0_work/notes_part0..2.md.  Scripts: r11/cert0_work/tu_bank_check.py (+ .out), k1_check.py (+ .out).

## 0. Bottom line
Cluster A is SOUND.  No result is wrong; nothing found points to a counterexample.  One genuine (fixable) gap was found in the KN-1 hold
realization (F1: the pull window of the modified Lemma TU), confirmed numerically; it is closed by stating the window with a COMMON level
eta_* := max(|x|_inf, c_{L+1}) (V1 Lemma TU verbatim).  Everything else re-derives, with cosmetic precisions C1-C7.  X2-ref's Lemma CM'
(a)-(d) re-derives line by line at the KN^tr companion (no tuned absorbers, mixed classes, positive anti-aligned owners), and the Part II lemmas
lem:II-recursion / domfine / SCi / coststat / trueshift apply there with the substitutions listed in 3.5.  The reduction claim and the
identification "end of Step A = (1c')" hold item by item, including dominance and the trace correction.

## 1. Verdicts
| # | Result (graph item) | Verdict | Fix / remark |
|---|---|---|---|
| 1a | KN^tr Steps 0-3 (Lojasiewicz point, Y_1 point, Puiseux point r'') | correct (cosmetic C1, C2) | C1: inf over the open ball need not be attained: pick r'' with F(r'') <= 1 - (3/4)mu; C2: (D2)'s C_Y convention (X1 2.5(b) vs X1-ref 7(b)) - either form, design constant |
| 1b | KN^tr Step 4 = ONE joint fixed point (actives, exact holds of ALL nearly-neutral coarse strict non-peaks of (T)-blocks, (KN)-lever pushes, D2 pushes, kappa pushes) | correct with fixable gap | F1 (pull window) below; C3 (Step-0 pull sits in S_d, d in L_0: TU hypothesis "exactly swallowed" -> distinct pull coordinates + merged bank, or drop the Step-0 move and bound F(r(f)) by K1); C4 (TU cost constant C_T ~ Design^3, so KN^tr(c) reads C_f Design^3 eta' log(1/eta') = o(T^2) — immaterial) |
| 1c | KN-1 (exact hold; realization by a Lemma TU pull with v(j_p) >= max(correction, c_{L+1})) + bank-mass bound | correct with fixable gap | F1: literal per-carrier rule can force a NEGATIVE bank; fix: common window [eta_*, 2^G eta_*], eta_* = max(\|x\|_inf, c_{L+1}); then bank >= c_f eta_* >= c_f c_{L+1}, pull mass >= 24 lambda eta_* |
| 1d | S-0 drift <= C Design c_{L+1} (route V's Step B) | correct | sharper: clamp equation gives relative drift C_f c_{L+1} |
| 1e | D1, D2, D3, K1 | correct (cosmetic C5) | C5: after the D1 rescaling robust minors are >= u/4 (not u/2); Hoffman bound unchanged up to a factor 2 |
| 2 | Lemma F; floor row (X4^0): data satisfy it up to K t; near-threshold carriers kind [3] at f^# with the TRUE shift after Step B | correct (cosmetic C6) | C6: "M b <= gap^#/4" (X1 2.2(iii), Q1 2.2) is not literally true after Step B; the needed inequality gap(f) <= 1.5 gap^# holds with room |
| 3a | X2-ref CM'(a) scrambling Scr_m(x) <= C(x/q_0)^2, x <= x_0 = c_f g_min Phi_min(L), negative blocks of mixed classes | correct | |
| 3b | CM'(b) representation p*(g - g_t) <= K t, kappa_w <= 1 + eta_0/2, kinds [1]/[1']/[2]/[3] | correct | needs P1 ([1']) |
| 3c | CM'(c) violation mass eps <= C_f Design c_{L+1} + C_f c_{L+1}^2/T, (H3) | correct | trace correction with the true shift = tolerated violation on E_c; positive anti-aligned owners counted without dominance |
| 3d | CM'(d) cost <= theta_w T^2 | correct | |
| 3e | Theorem C_mix' / (R-abs) (assembly) | correct as an assembly | its new content is CM' (checked here); UE / E^eng / DC / LV inputs belong to cluster C |
| 3f | "U1 Lemmas 4.1-4.6 and U1-ref 7 apply at a companion without tuned absorbers" (Part II lem:II-recursion, domfine, SCi, coststat, trueshift) | correct | substitutions in 3.5; wording C7 in U1-ref 7 / lem:II-domfine(ii) |
| 4 | (U3) at Step-A supports: pull-data bound (c3'); residue as tolerated violation (P3) | correct | the c_{L+1} floor of the pulls is needed exactly here; F1's window supplies it |
| 5 | Reduction claim (CM' uses Prop KN only through statuses, kind-[3] rows, exactness); "end of Step A = (1c')" | correct | dominance and trace-correction items written out in 3.6 |
| 6 | P1 (kind [1']), P2 (order), P4 (pull coordinates), P-HOLD, P-R | all correct | P2 is even weaker than needed: route V's Step B depends only on the class signs |

Recommended pass count after this certification: every item of cluster A now has 2 independent passes (X1-ref / X2-ref / one Round-10
referee + cert0), with F1 recorded as a precision of Q1 2.2's bracket.

## 2. Finding F1 (KN-1 hold: pull window of the modified Lemma TU).  Fixable gap, proved here.
Q1 2.2: "For the KN-1 holds the pull of Lemma TU is taken at a contact j_p of the carrier's own set with v_l(j_p) >= max(needed downward
correction, c_{L+1}) (so j_p <= s_far(w)); the bank absorbs the rest."
Exact bank equation (V1 Lemma TU Step 2 via Lemma B (3.1); exact for any diagonal base): after the pulls (row A^p, nu_p := ||U^*A^p||),
   val_l(m) - val^p_l = (nu_p beta_l + m_l s'_l^2 v'_l)/N(m) - beta_l,   N(m) = (nu_p^2 + sum_k m_k^2 s'_k^2)^{1/2},   beta_l = eps_l <U^*u_l, e^p>,
so the bank of carrier l is m_l = (Delta_l N + beta_l (N - nu_p))/(s'_l^2 v'_l) with Delta_l = x_l + 2 v_l(j_l) + O(pull Hilbert terms).
beta_l has either sign (|beta_l| <= ||U|| ||u_l||_1), and N - nu_p is created by the OTHER carriers' banks: N - nu_p ~ sum_k m_k^2 s'^2/(2 nu_p)
~ C Design eta^2 when the active corrections are of size eta ~ eta' (V1: kappa <= C Design eta^2).  A bank must be >= 0 (mass of the sign of z).
Hence m_l >= 0 requires Delta_l N >= -beta_l (N - nu_p), i.e. v_l(j_l) >~ |x_l| + C Design eta^2 when beta_l < 0.  A KN-1 hold may have a tiny
first-order correction (a nearly neutral carrier whose value is already ~ 0), and the floor c_{L+1} <= b^2 is far below Design eta'^2.  So the
rule, read per carrier with the first-order correction, can require a NEGATIVE bank.  Numerics (tu_bank_check.out, 50 digits, exact equations,
residual <= 5e-52): eta = 1e-6, 1e-8, 1e-10 with c = eta^3, beta_h = -0.15: Delta_h = 2e-18, 2e-24, 2e-30 against the positivity threshold
-beta_h(N - nu_p)/N = 7.2e4 eta^2; hold bank m_h = -6.0e-5, -6.0e-9, -6.0e-13 (infeasible).  With beta_h = +0.15 no failure.
FIX (proved): put every pull of the joint fixed point (actives, holds, peak pushes, lever and D2 pushes realized by pulls) in the common window
v_l(j_l) in [eta_*, 2^{G(L)} eta_*], eta_* := max(|x|_inf, c_{L+1}).  This is V1 Lemma TU verbatim with eta replaced by eta_* >= |x|_inf (its proof
uses only |x|_inf <= eta).  Then Delta_l in [eta_*/2, 4 * 2^G eta_*], m_l >= (Delta_l nu_p - ||U|| kappa)/(s'^2 v') >= c_f eta_* >= c_f c_{L+1}
(numerics: m_h = 2000 eta > 0 in every case), pull masses 24 lambda v >= 24 c_{L+1}/Design(L) (BR's (U3) bound), j_l <= s_far(w), cost
C_T eta_* log(e/eta_*) <= C_f Design^3 eta' log(1/eta') + C_T c_{L+1} log(1/c_{L+1}) = o(T^2), and the pulls stay far above the lever coordinate
(v ~ eta_* <= C eta' << v_l(second element beyond s_max) >= 1/Design: refb 1.4 / (D-lev) unaffected).  Equivalent per-carrier form:
v_l(j_l) >= max(|x_l| + C_T eta_*^2, c_{L+1}).  Later re-solves of the fixed point change the corrections only by O(Design^2 eta_*^2) <<
eta_*, absorbed by the banks (pulls are fixed one-shot moves).  The same remark applies to the kappa-restoring peak pushes when they are realized
two-sidedly by Lemma TU (the needed kappa correction can be ~ 0).  Severity: precision; no conclusion changes.

## 3. Re-derivations
### 3.1 KN^tr Steps 0-3 (ratio space)
Step 0: V1 (C1), (C2); active weak peaks of (T)-blocks pushed to rho = 1 - b (value change <= 2b theta Phi/m).  At f_1: P ⊇ P_rob, Omega ⊂ Q,
so Lemma F gives F(r_1) = max_{N_T} psi_d(r_1)/Phi_d <= max_{N_T} rho_d(f_1) <= 1 + C_* b; tiny minors <= (1 + Lip* C_*) b.  [Without the move: K1 gives
sigma' >= sigma_rob - 3b sum Phi^2, so F(r(f)) <= (1 + b)(1 + C D^C b); this is C3's alternative.]
Step 1: V2 Lemma L on the compact semialgebraic K_kappa (Q3) for g := max |tiny minors and cofactor polynomials| (semialgebraic: the (X4^0)
coefficients contain K): if Z ∩ K_kappa = {}, g >= g_min > 0 (design number) contradicts g(r_1) <= (1 + Lip* C_*) b for L >= l_f; otherwise
|r' - r_1| <= C_L g(r_1)^{2/N_L} <= eta'/3 by (D1), and F(r') <= F(r_1) + Lip*_kappa eta'/3 <= 1 + delta_0(b) (P-LIP: Lip* contains 1/Phi_d).
Step 2: QC(b): Y_1 = {} would give F >= 1 + m_0 > 1 + m_0/2 >= 1 + delta_0 (D2); so Y_1 != {} and dist(r', Y_1) <= C_Y delta_0^{alpha_Y} <= eta'/3 (D2).
Step 3: G_h(r'_1) <= max_{Y_1} G_h = 1 - mu_kappa(h), h = eta'/3 (QC(a), non-coincidence by GEN_fin); choose r'' in Z, |r'' - r'_1| < h,
F(r'') <= 1 - (3/4)mu (C1).  |r'' - r_1| < eta'; robust minors >= u - Lip* eta' >= u/2; robust statuses move <= Lip* eta' << u; |r_d| ~
Phi_d/(m K) >= Design^{-2} >> eta' keeps the signs.  Quantifiers: design (level-L objects of ALL patterns, N-free, finitely many) -> f -> L, clean
w -> class -> Steps 0-4; b(w) is computed after Design(L) and the QC data; nothing depends on N beyond f-constants absorbed for L >= l_f.  OK.

### 3.2 Step 4: the joint fixed point (re-derived as one system)
One-shot moves first: all pulls (window of F1), (KN)-lever pushes of size s_0 = C D eta' theta Phi_P^2/(rho_{d0} M), D2 pushes (inward by eta').
Unknowns: banks m_l (l in L_0 := active Omega carriers of all active blocks ∪ class-G nearly-neutral coarse strict non-peaks of (T)-blocks; after
(C1) these are exactly swallowed on S^nat ⊇ far part), z-move amounts y_l on free coordinates of S^nat_l = S_l \ (F ∪ T(L)) for class-R nearly-
neutral carriers of (T)-blocks (class R = both signed rooms >= u ||v 1_{S^nat}||, so a two-sided exact move of the needed size <= C b exists while
keeping every moved coordinate free, i.e. without changing the E_c-types of the pattern), and one kappa-push s_m per block.
Equations: val_l = r''_l kappa*_m (active; (U)-blocks s_m r''_l kappa*_m), val_l = 0 (holds), kappa_m = kappa*_m.
Jacobian: d val_l/d m_l = s'^2 v'/N >= Design^{-1/6}/2; d val_l/d m_k (k != l) = O(C Design eta_*) (Hilbert normalization only, Lemma B(i));
d val_l/d y_l = v_l(j) on the moved coordinates; d val_l/d y_k = 0 (disjoint signature sets; z-moves do not change e); d val/d s = second order;
d kappa_m/d s_m in [3/4, 1] (Lemma 1.4(a), X_m <= C D^2 c^2); d kappa_m/d|zeta(l)| = rho_l M X_m/C = O(D^2 c^2) (Lemma 1.4(c)).
So the Jacobian is diagonal-dominant (block triangular up to O(Design eta_* + D^2 c^2)), and V1's explicit fixed point (scalar y for the banks,
IVT for kappa) converges.  STATUSES in a (T)-block: by Lemma K/K1 rho_d = m|r_d| K(sigma, R^2)/Phi_d depends only on r_d (exact), R^2
(= R_a(r'')^2 EXACTLY, because every non-active coarse strict non-peak is held at 0 — P-HOLD; by (T) these are its nearly neutral carriers) and
sigma (peak SET + fine terms: sigma in [sigma_rob, sigma_rob + C c^2] since coarse peaks = P_rob); peak VALUES never enter (refb E7).
Hence rho_d <= (1 - 3mu/4)(1 + C D^C c^2) <= 1 - mu/2 (c <= b^2 <= mu^2/64, mu <= Lip* eta' << 1/Design).  Necessity of the exact hold (KN-1):
inactive values enter quadratically through R^2 (k1_check.out: floor margin 1e-6; inactive value v gives rho - floor ~ 2e3 v^2; v = 1e-4 turns the
protected carrier into a peak), so value errors ~ Design^2 eta'^2 would beat a Puiseux margin mu << (Design eta')^4.  (KN)-blocks: U1-ref
Prop KN(b) with eta' (displacement <= eta' including the Puiseux step; the lever push dominates by choice of C'); (U)-blocks: D1 rescaling, rho <=
s_m(1 + b + Lip eta') <= 1 - eta'; D2-pushed carriers rho <= 1 - c eta'; second-order effects O(Design^2 eta'^2) << these margins.  OK with F1.

### 3.3 S-0 in route V (Step B drifts)
Step B changes zeta_m only by fine carriers (l1 mass <= sum_{l>L} lambda_l <= C c_{L+1}) and by released far parts of non-owner coarse carriers
(|Delta u_l| <= 2 delta_l sum_{s>s_far} 2^{-s}/n_l <= 4 c_{L+1}^2); it changes neither a (hence nor e) nor any active value (owners' far parts were
fixed in Step A; targets lie in T(L) ⊂ E_c).  Clamp equation 1 = sum_k min(Phi_k(1-C)/C, v_k)^2: coarse-peak terms unchanged near C, Omega terms
change only through A (relative C_f c), fine terms by <= Phi_k^2((1-c)/c)^2; slope >= 2 Phi_*^2(1-c)/c^3 (robust peak) => |Delta C_m| <= C_f c_{L+1};
rho_k = v_k C/(Phi_k M) => relative status drift <= C_f c_{L+1}; kappa = (A^2 - C S_Omega)/(A M) is Lipschitz => |kappa^# - kappa'| <= C_f c_{L+1}.
With c_{L+1} <= b(L,M(L))^2 <= b(w)^2, b <= min(eta', mu/8): drifts <= mu/16; rho^#_d <= 1 - mu/4; held values <= 4c^2 (effect O(c^4)).  CORRECT.

### 3.4 D1, D2, D3, K1
D1: in a (U)-block Delta'_m is removed by (X5), so r^(m) occurs only in (X3)_m (linearly, no constant entry): minors homogeneous of degree 0/1
in r^(m); each cofactor-vector column of g_J is homogeneous of degree e_J in {0,1}, so the minors of g_J are homogeneous; vanishing is preserved
under r^(m) -> s r^(m), robust values scale by >= s^n >= 1/2 (C5); Lemma K: |r_l| -> s|r_l| and K decreases, so rho_l -> <= s rho_l.
D2: inactive near-threshold carriers of (U)-blocks pushed inward by eta' (not variables of Gamma^#; kappa restored).  D3: (T)-block estimate in
formula-1 form: |sigma' - sigma_rob| <= 3b + c^2 (weak peaks in Omega, fine terms), |R^2 - R_a^2| <= C b^2 (rho <= b carriers: m^2 r^2 <= b^2 Phi^2/k^2),
dK/dsigma, dK/dx <= C D^C on {sigma >= D^{-2}, 1 - R^2 >= sigma_rob/4} => |rho(f) - rho^0(r(f))| <= C D^C(b + c^2).
K1: kappa(Omega) = A + theta[Phi_{P\Omega}^2 + sum_{Omega∩P}(1 - rho^2)Phi^2] + S_f/theta and a^2 = sigma' + k^2 R^2 (re-derived from (E2));
numerics k1_check.out (own solver from lem:threshold, 60 digits): 59 blocks, 45 with a weak peak in Omega, max error 5.2e-61.  CORRECT.

### 3.5 Lemma F, floor row, kind [3] (item 2) and CM'(a)-(d) (item 3)
Lemma F: sigma >= sigma_rob (P ⊇ P_rob, s_f >= 0), R^2 >= R_a^2, K increasing => rho_l >= rho^0_l exactly.
(X4^0) data: lambda vs Domega_dec = vs gamma_dec + Delta'_dec lambda rho(f) (strict non-peaks; weak peaks: rho -> 1, eq:peakshift e_l >= 0);
violation at r'' <= 3 lambda gap(f)/t + |Delta'| lambda (C D^C(b + c^2) + Lip*(eta' + Cb)) <= C_f lambda(b/t + D^C b + Lip* eta') <= K t.
Kind [3] at f^# (TRUE shift Delta'' = Delta'^* kappa'/kappa^#, after Step B): for every cone point and increment,
lambda vs Domega^# = vs gamma + Delta'' lambda rho^# >= (Delta'' - Delta'^*) lambda rho^# + Delta'^* lambda (rho^# - rho^0(r'')) >= -C_f lambda(c + D^C c^2)
>= -3 lambda gap^#/t (gap^# >= M mu/4, c <= mu^2/64); + side: vs omega^+ <= gap(f)/t and gap(f) <= M b <= M mu/8 <= 1.5 gap^# (C6); shift-trick cost
lambda|x| <= |Delta'| lambda |rho^# - rho(f)| + K t <= C_f lambda(Lip* eta' + C D^C b + c) + K t.  The cone is fixed at the end of Step A, so Step B
cannot affect data satisfaction.  (KN)-blocks: U1-ref (X4) with the true shift: vs Domega^# >= -|Delta'^*| gap^#/M - C_f c >= -3 gap^#/t.  (U)-blocks:
Delta'' = 0 => vs Domega = vs gamma/lambda >= 0.  CORRECT.
CM'(a): S_k ⊂ O(k) (allowedness (a); S_k ∩ (E_c ∪ F^A ∪ Step-A coordinates) = {} for k > L >= l_f); supp u_k \ O(k) is fixed before k; zhat = z on
J_fine.  A negative fine carrier (any class, absorbers included) is self-aligned: |u_k(zhat^#)| = |Y_k| + own_k >= delta°_k >> vartheta Phi_k (W3): an
(R) peak with margin >= q_0 delta°_k/2 — only sigma_{m(k)} = -1 is used, so mixing is irrelevant; untuned absorbers of a negative block 1 are such
peaks (the route-X obstruction X2-ref A5 disappears).  Scr_m(x): coarse peaks have margin >= q_0 vartheta Phi_min u/2 > x_0, coarse strict
non-peaks gap >= g_min and Phi gap >= Phi_min g_min > x_0 (CM^tr(b); held carriers gap ~ M); fine carriers contribute only if delta°_k <= 2x/q_0, at most
Phi_k <= (delta_k H_k)^2; super-exponential decay => Scr_m(x) <= C (x/q^#_0)^2 for x <= x_0.
CM'(b): g_t differs from U1 Prop 2.2(e)'s by the off-F part of b^+ (V_fine/2 instead of chi_f V_fine; no absorber coefficients): <= (1 + ||U||)
||V_fine||_1 <= C_f(Design c + c + c^2/t) <= K t; sqrt(Gamma) seminorm => kappa_w changes by O(c); Step-A block-data change C_f Design^3 eta' log
times t^{-2} -> 0 (V1 TR Step 5 estimates).  Kinds: active robust [2]; active near-threshold [3] (above); inactive nearly neutral / KN-1-held [2]
(Domega = Delta'' w^# ~ 0, gap ~ M); KN lever [2] (negative blocks: no inactive near-threshold carrier exists there, U1-ref 4.1 exclusions) or [3];
D2-pushed [1'] (gap >= c eta' M may be < t^2; V1 E'' and UE Step 3 use only |omega| <= 2 gap/t).
CM'(c): E_c contact: (X1) at the cube corner ((Delta'^*, gamma(t)) = projected point + increment, in the cone) gives z V_proj >= 0, so (z b^+)_-,
(z b^-)_+ <= |V_fine|/2; E_c free: V_proj = 0, b^± = ±V_fine/2, b^theta = (chi - 1/2)V_proj = 0 (H3).  V_fine|E_c = -(Delta'' - Delta'^*)·P (trace
correction, ||P_m||_1 <= 1, |Delta'' - Delta'^*| <= C_f c) + fine terms (<= C_f sum_{l>L} lambda_l).  Owners' far parts (j > s_far, fixed in A, off E_c):
V = gamma_l v_l(j) + fine with z = eps_l and dominance => admissible.  J_fine: b^± = ±V/2; coarse and negative-fine owners dominate (3.6) =>
admissible; unowned: V = 0, z := 0; positive-owned: viol <= |V(j)|, and no coarse candidate meets such j (own(j) is the FIRST candidate), so
sum <= C_f sum_{l>L} lambda_l.  Hence eps <= C_f Design c_{L+1} (+ C_f c^2/T, harmless).
CM'(d): Step A cost (KN^tr(c), C4) + Step B (Z3 Lemma 3.1 with delta supported in J_fine: coarse <= 4c^2, fine <= C c) <= theta_w T^2.
Part II lemmas at the route-V companion: lem:II-recursion's rule z_j = sgn(-sigma_m varsigma_k u_k(j)) already contains the anti-aligned positive
rule; type (c) (tuned absorbers) is empty and type (d) is enlarged to all carriers at stages > L of active blocks, absorbers included;
lem:II-SCi with "tuned absorbers, gap M" replaced by "absorbers of negative blocks are (R) peaks" and prop:II-KN(b) by CM^tr(b);
lem:II-coststat with KN^tr(c); lem:II-trueshift(a): the first term becomes C_f c_{L+1} (cluster carriers are untuned and may change status in Step
B), the middle term vanishes (Step B does not move Omega_act values); (b): the trace correction on T(L) is NOT absorbed (no tuned cluster) but is a
tolerated violation counted in (c); lem:II-schauder is not used.  CORRECT.

### 3.6 Reduction claim, dominance, trace correction, identification (item 5)
Every use of Proposition KN inside X2-ref's CM' proof: (i) coarse statuses — x_0 in (a); |w| = M of coarse peak owners (their coefficients);
"only carriers at stages > L change status in Step B" (trueshift (a)); statuses/cost (coststat); (ii) kind-[3] rows — kinds in (b); (iii) exactness
of Gamma^#(kappa, a) at r'' — projection with error K t and Hoffman, normalization (A_max), (X1) at the cube corner used in (c).  No other property
enters.  DOMINANCE (written out): owner k, coefficient |coef_k| >= (A K T_lo(w)/2) lambda_k M (types (a), (b), negative (d): |w| = M; positive
non-frustrated (d): >= M/2), later coefficients <= C_f lambda (|Delta''| <= C_f); (i) j in S_k: later carriers meet j only through targets, (W4'') gives
ratio <= C_f 2^{m + k(k) - 3·2^k} T_lo^2 < 1/2; (ii) target coordinates: later total <= C_f c_{k+1} <= C_f 2^{-8n(k)} and n(k) >= Design(k) >= 1/(eta_k
lambda_k).  Absorber owners (block 1 active): only the partner meets the shared coordinate inside the cluster/PRE sequence, lambda drops by >= 8,
so its term is <= (1/8)(M/(M/2))(1 + o(1)) <= 1/4 of the owner's; all carriers after the sequence (first such stage has (W2)) give
C_f 2^{-8n}/(T_lo eta_k lambda_k), and P-R (eta_k >= mu_{p0}^2 c_k^2/2^13, re-derived: R minimal => 2^{-R} > mu^2 lb^2/64, lb >= c/8, least entry
4·2^{-R}/q^*(x) >= 2^{-R}/2) gives 1/(eta_k lambda_k) <= 2^13 D^3/mu_{p0}^2 <= (B_mu D)^6 <= n.  Positive frustrated owners: no dominance claimed
(violation).  TRACE CORRECTION (written out): L(Delta'', gamma) - L(Delta'^*, gamma) = -sum_m (Delta''_m - Delta'^*_m) P_m on E_c, |Delta'' - Delta'^*| =
|Delta'^*||1 - kappa'/kappa^#| <= C_f c_{L+1} (3.3); on the near signature sets of coarse peaks the true coarse value keeps the peak-trace sign
(admissible), elsewhere it is part of V_fine, a tolerated violation of l1 mass <= C_f c_{L+1}; it uses only the S-0 kappa drift and "Omega_act values
exact at the end of Step A and untouched by Step B".  IDENTIFICATION: X2-ref's (1c') is the joint fixed point restoring kappa and the Omega_act values
with no absorber tuned; route V has no (1b), and KN^tr's Step 4 is such a joint fixed point, so the end of Step A is the state after (1c').  CORRECT.

### 3.7 (U3) at Step-A supports (item 4)
Pulls: normalized mass >= 12 lambda v; data t|b| <= t(|gamma_l| v + |V_fine|) <= (2A_2 + C_Delta) lambda v + t C_f c_{L+1} <= K_3 |a^#| because
v >= eta_* >= c_{L+1} (F1) and t <= T_hi(w) << 1/(C_f Design); KN-1 holds (gamma = 0): t C_f c <= 24 lambda v.  Banks: contact-like part (eps gamma >= 0
by (X2); peak coefficients have sign eps_c) + V_fine/2.  P3: at a support coordinate with z = sgn a, |a + x| - |a| - z x = 0 without flip and
= 2(-zx) - 2|a| <= 2(z x)_- with flip, the same form as at a contact, so the residue is a tolerated violation (cost <= 2 rho|tau||V_fine(j)|, in eps of
(U4)); b^theta = (b^+ + b^-)/2 = (chi - 1/2)V_proj does not see V_fine.  CORRECT (the c_{L+1} floor is needed exactly here).

### 3.8 Single-referee fixes (item 6)
P1 correct (see kinds).  P2 correct (class -> Step A -> cube -> Step B); moreover in route V the z-values of Step B depend only on the class signs,
the cube enters only through Delta''^*.  P4 correct: per S_l at most the Step-0 push, one realization or hold pull + bank, a lever/D2 push and a peak
push; banks use the first element beyond s_max; Lemma DC's pulls (v ~ r >= s_1 >> c_{L+1}) are chosen among unused elements in a window of ratio
2^{6G}.  P-HOLD correct and necessary (3.2).  P-R correct (3.6).

## 4. Cosmetic precisions
C1 Step 3: inf over the open ball: choose F(r'') <= 1 - (3/4)mu.  C2 (D2)/QC(b) constant convention (X1 vs X1-ref).  C3 Step-0 pulls vs TU's
"exactly swallowed" hypothesis (distinct coordinates + merged bank, or drop the move).  C4 KN^tr(c) constant Design^3 (TU's C_T) instead of Design.
C5 robust minors >= u/4 after D1.  C6 "M b <= gap^#/4" overclaim; needed gap(f) <= 1.5 gap^# holds.  C7 U1-ref 7 / lem:II-domfine(ii): "first later
non-absorber stage" should read "first stage after the cluster or PRE sequence" (PRE stages are absorber stages that carry (W2)).

## 5. Numerics (sanity checks; finite models cannot exhibit infinite-dimensional failures)
tu_bank_check.py/.out: exact Lemma TU bank equations; literal per-carrier hold pull => negative bank whenever beta_h < 0; common window => positive
bank ~ 2000 eta; threshold scales as 7.2e4 eta^2.  k1_check.py/.out: independent block solver (lem:threshold) at 60 digits; K1/Lemma K identities
to 5.2e-61 on 59 blocks (45 with a weak peak in Omega); quadratic sensitivity of a protected status to an inactive Omega value (KN-1 necessity).
