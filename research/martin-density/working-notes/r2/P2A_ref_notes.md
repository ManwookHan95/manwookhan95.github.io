# Referee report on P2, version "P2A" (ctx/r2/P2_notes.md = P2A_notes.md, 512 lines)

Referee: Round 2, adversarial check of the P2A instance (toolkit 1.1-1.7, Thm 2.1, Cor 2.3, Rem 2.4, Props 3.1-3.3, Thm 3.4,
Lemmas 4.1-4.2, Prop 4.3; 4.4-4.6 in passing). The concurrent instance "P2x" is refereed separately (its report is the first part of
ctx/r2/P2_referee.md). Setting used: canonical base q, FINITE block set I (p_N, any N; Preprint B Remark martin-tail), only Lemma B's
conclusion about T. Part files: ctx/r2/P2A_ref_part1..5.md; scripts: ctx/r2/P2Aref_work/. Labels: PROVED/SKETCH/HEURISTIC/FALSE/OPEN.

## 0. Summary
* The core is CORRECT. Theorem 2.1 (engineered recovery of d-neutral two-piece switching mates: any infinite contact set K, any
  non-constant split, one active block, or several under (S)) is PROVED; I re-derived every step (part 2). Its mechanism is sound:
  the one-sided decompositions of f are transported EXACTLY to an engineered NA point f' (d-coefficients recomputed at f';
  one scalar steering condition v_m(x') = 0 per block, achieved by a far negative-mass pull, one raising mass and the IVT), window
  masses and a theta-tail serve |tau| <= s_1, and the slack is needed only beyond a FIXED T_0. Only one trivial gap (rho < 1/32).
  Consequently P1's explicit defect mates and P1's slab ARE in Ls(f) (Cor 2.3(b), slab part, PROVED): P1's nonempty defect is a defect
  of the intrinsic mechanisms only. Toolkit 1.1-1.5, 1.7 and Props 3.1, 3.2 are correct.
* Theorem 3.4 (non-neutral data at block-tame blocks) is WRONG AS STATED: its hypothesis (iii) (linear independence on J_gamma of the
  tuning functionals psi_{k,m}) can NEVER hold for non-trivial two-piece data, because
      sum_{k,m} lambda_{k,m} omega_Delta,m(k) psi_{k,m} = b+ - b- = v,  which vanishes on J_gamma   (Prop. R1, PROVED, numerically checked).
  The sketch's mechanism ("no Far set, no raising mass: steering is part of the tuning") is therefore impossible — the resonance
  direction is invisible to free moves (the authors' own remark after Lemma 4.2). A repair needs base-side steering again, and when that
  steering needs a PULL (Far flips), the flips damage the active block's peaks by amounts not controlled by (MS): a far-tail comparison
  (rate condition on T) is needed. So "A_referee §5.5 is too pessimistic" is NOT established by P2A. (For Delta d >= 0 under a cone
  condition it IS established by the other instance, P2x Thm 3.5, via a Bregman argument that also shows P2A's diagnosis "infinitely many
  strict non-peaks is what breaks it" to be an artefact of putting the d-mismatch into the base.)
* Fixable gaps: Cor 2.3(b) omits the hypothesis g in C(f) (P1-referee's correction C4, cited but not implemented); Prop 3.3 is a
  sufficient condition only and its steering needs a path-uniform E bound; Lemma 4.1's "deep replication costs O(theta)" is false for
  admissible T (correct: O(theta log(1/theta))); Prop 4.3 needs s_1 -> 0 (or J >~ kappa/(1-rho^2)); Lemma 4.2's "iff" holds for l_inf moves.
* Remark 2.4: the shifted extension of Thm 2.1 is a plausible SKETCH (I checked the domination of the shift kink costs), but "together
  with P1 6.1 this would give f in R at P1's example" is unsupported (HEURISTIC): P1 6.1 provides no shifted decompositions with H^sh <= 1.
* No counterexample is claimed or implied. Density of NA((c_0,p_N), l_2^2): OPEN.

## 1. Verdict table (assigned claims)
| Claim | Label (P2A) | Verdict | Main issue |
|---|---|---|---|
| Setting (finite I, only Lemma B, imports) | PROVED | correct | imports used as stated; no hidden property of T |
| Lemma 1.1 clamp formula | PROVED | correct | = A Fact C; also at NA points (degree-0 homogeneity) |
| Lemmas 1.2-1.5 toolkit | PROVED | correct | re-derived (L compact, J_m norm-to-weak* continuous; Lemma 7.2 at f'; slack lemma; geometric sum < 2|t|) |
| Lemma 1.7 (admissible => kappa <= 1) | PROVED | correct | general Lemma 7.2 (b+ not in supp a) + Psi lower bound; A Lemma 4.4(b) |
| Thm 2.1 main | PROVED | correct (one trivial fixable gap) | Step 1 needs V_{>N''} <= V_Far, true only for rho >= 1/32; fix in (C4) |
| Cor 2.3 | PROVED | correct with fixable gaps | (b) must assume g in C(f); (a) cites P1 2.3 (specific example) for a general setting |
| Rem 2.4 shifted data / f in R | SKETCH | unclear | extension plausible; "f in R" HEURISTIC (P1 6.1 gives no H^sh <= 1 data) |
| Prop 3.1 mixed term | PROVED | correct | — |
| Prop 3.2 consistency identity | PROVED | correct | "must be <= eps_0 s_1" is sufficient, not proved necessary |
| Prop 3.3 garbage identity | PROVED | correct with fixable gaps | sufficient only ("provided", not "exactly when"); steering for Delta d != 0 is not verbatim (path-uniform E bound; modified (S)) |
| Thm 3.4 (Delta d != 0, tame blocks) | SKETCH | wrong | hypothesis (iii) never holds (Prop. R1); tuning-only steering impossible; repair needs base steering, and if that needs pulls, Far-flip collateral damage needs a rate condition |
| Lemma 4.1 replication identity | PROVED | correct with fixable gaps | identity right; "O(theta)" consequence false (log factor); c_f depends on rho_W |
| Lemma 4.2 retuning feasibility | PROVED | correct | "iff" for l_inf(G)-moves; c_0-moves reach the relative interior |
| Prop 4.3 abstract scheme | PROVED | correct with fixable gaps | Lemma 1.4(ii) needs p*(g'-rho g) <= (1-rho^2)T_0/6; add s_1 <= eta or J >= 24 kappa/(1-rho^2) |

## 2. Line-by-line verification (condensed; details in P2A_ref_part1.md, part2.md)
2.1 Toolkit. 1.1 is Fact C: on P, |zeta(k)|/|zeta| = |alpha_k| + Phi_k^2 M/C, so C r(k) >= M; off P, |w(k)| = C r(k) < M; zeta(k) = 0 => w(k) = 0.
1.2: L compact => L** weak*-to-norm on bounded sets, L** zhat in V; J_m norm-to-weak* continuous at R_m** zhat != 0 (T3); D_m, R_m* compact;
grad q(xhat_n) = a_n since a_n norms xhat_n; J_V = (J_m)_m for finite I. 1.3: <omega - d'w', R_m x'> = 0 for omega off P'_m (Fact C at f'),
then A Lemma 7.2 at f'. 1.4: 1 + (tau^2/2)(1-delta) <= 1 + tau^2/2 - tau^4/8 <= s(tau) iff tau^2 <= 4 delta; beyond T_0 the slack lemma.
1.5: for s_j < |t|, sum s_j < 2|t|. 1.6: g(xi) = 0 for every mate; b+-(zhat) = 0; v != 0 forces K infinite (v in Y \ c_00 on F cup K).
1.7: base via Lemma 7.2 + Psi(h) >= ||h_perp||^2/(2(1+||h||)), blocks via A Lemma 4.4(b) as tau -> 0+.
2.2 Theorem 2.1. Re-derived: raising coordinate from sum_F v_j<PU*v,U*e_j*> + sum_K |v_j|z_j<PU*v,U*e_j*> = ||PU*v||^2 > 0 (P = P_{e-perp};
PU*v != 0 as v notin Ra, U* injective); Fact D compatibility of z'; v(xhat') = -2V_Far - V_{>N''} + <U*v, e'-e>; the bound
|<U*v, e(a''(0)) - e>| <= (A_0 - 1)s_1 + V_Far/2 <= V_Far; dPsi/dmu >= gamma_+/2; MVT + IVT; p-moves change neither e' nor v(xhat');
d'^+ = d'^- = d'^theta from <Dw', D omega_Delta> = (C'/|Rx'|) v_m(x') = 0; (2.1.2); convergence (z' -> z coordinatewise, masses -> 0,
Lemma 1.2, c -> g(zhat) = 0, B^sigma -> rho b^sigma); block costs within the coordinatewise radius (fix G1) on the FIXED range |tau| <= T_0;
no flips (F, window, j_+, Far: |a'_j| >= 2 rho T_0|v_j|); kinks only beyond N'' (z' = 0), <= rho|tau|V_{>N''}/2 <= eps_0 tau^2 on |tau| >= s_1,
none for sigma = theta; Step 6 arithmetic (tau^2/2)(rho^2 kappa + delta/2) <= (tau^2/2)(1 - delta).
Gap (trivial): Step 1 needs Psi(0) >= -4V_Far, i.e. V_{>N''} <= V_Far; (C4) gives V_{>N''} <= delta s_1/(8 rho) and V_Far >= 2 s_1, so this
holds for rho >= 1/32 only. Fix: V_{>N''} <= min(eps_0 s_1/rho, V_Far) in (C4) (or scale: (f', lambda g') stays NA for |lambda| <= 1).
Hidden assumptions: none found (weak* vs norm: f', g' converge in norm; uniformity: all estimates on a fixed tau-range with finitely
many converging data; c_0: z' in c_00; T: only Y cap c_00 = {0}, injectivity; K and the peak sets may be infinite).

## 3. Main problems
### 3.1 Theorem 3.4 is vacuous (WRONG as stated). Proposition R1 (PROVED).
For two-piece data (P2A 1.6) with omega_Delta != 0 and every gamma > 0, the restrictions to J_gamma = {j notin F : |z_j| <= 1-gamma} of the
functionals psi_{k,m} = u_{k,m} - (u_{k,m}(xi)/|zeta_m|) R_m* w_m (k in Qbar_m, m in I_0) are linearly dependent.
Proof. supp omega_Delta,m lies in the strict non-peaks, hence in Qbar_m. With c_{k,m} := lambda_{k,m} omega_Delta,m(k) (not all zero):
sum_k c_{k,m} u_{k,m} = R_m* omega_Delta,m = v_m and sum_k c_{k,m} u_{k,m}(xi) = <omega_Delta,m, zeta_m> = |zeta_m| Delta d_m (Fact C, omega_Delta,m off P_m).
Hence sum_{k,m} c_{k,m} psi_{k,m} = sum_m (v_m - Delta d_m R_m* w_m) = b+ - b- = v, supported in F cup K, disjoint from J_gamma. QED.
(If omega_Delta = 0 then v = 0 and g is a finite certificate.) Numerically: identity to 4e-14, Fact C to 9e-11 (thm34_dependence3.py).
Consequences. (a) The linearised tuning map in the free variables has range in the hyperplane annihilated by (c_{k,m}|zeta_m|); the
missing direction is exactly the steering quantity v(xhat') (mixed term, Prop 3.1), whose residual after the window masses is ~ s_1.
So the construction "without Far set and raising mass" cannot work. (b) The example sentence is void: at P1's example |Qbar_1| = 1 and
psi_{2,1}|_J = u_{2,1}|_J = 0. (c) Repair (SKETCH): replace (iii) by (iii') "the c-relation is the only relation among the psi_{k,m}|_{J_gamma}"
and steer the c-direction from the base. If two-sided steering by O(s_1) masses exists (some j in F with <PU*v, U*e_j*> != 0, or a contact
with z_j<PU*v, U*e_j*> < 0 — essentially P2x's (TC)), all displacements are O(s_1) in sup norm plus the last cut-off, (MS) + Lemma 4.1 give
||E||_1 = o(s_1) and Prop 3.3 applies: plausible. If a PULL is needed (e.g. |F| = 1, diagonal U: P1's situation), the Far flips
z'_j = -z_j move every u_{k,m}(xhat') by up to 2||u_{k,m} 1_Far||_1, which is not O(s_1) uniformly in k (a peak u_k ~ e_j*/q*(e_j*), j in Far,
changes w(k) by ~ 2M); controlling the resulting E needs a comparison of the tails of the first ~log(1/s_1) block vectors with the tail
tau_N of v — a rate condition not implied by Lemma B (it holds for P1's T by its allowedness rule). The P2x referee reached the same
conclusion for the Bregman variant ("Delta d > 0 with pulls: OPEN / T-dependent").
### 3.2 Cor 2.3(b) misses g in C(f).
Thm 2.1 uses g in C(f) for |tau| >= T_0; rho^2 max(h(g - mu+- u), mu+-^2/C_1) < 1 does not imply it (h sees only ||P_{e-perp}U*b||^2/nu and U* is
compact: a large contact mass far out has small h but large q*). Fix: "every g in E_u cap C(f) with ...". The slab part is fine (P1 6.2).
### 3.3 Remark 2.4's consequence is unsupported.
P1 6.1 proves C(f) in E_u and mu+ <= theta(g) <= mu- for LIMITS of carrier coefficients; it does not provide (shifted) two-piece
decompositions with H^sh <= 1 (P1's own remark: peaks, level shifts, free coordinates may contribute O(t^2) to the costs; P1-referee C1:
the sharp second-order invariant involves transfer-peak rebalancing, Gamma_w <= H^sh, which is not of shift type). "f in R at P1's
example" remains OPEN. The extension itself (shifted two-piece data) is a plausible SKETCH: at window contacts a cheap shift has the sign
of the mass (no flip) and an expensive one costs <= its cost at f; Far flips and the cut-off cost <= 2 tau^2 ||v'_theta 1_{(N,inf)}||_1 = o(1)tau^2.
### 3.4 Lemma 4.1: "deep replication costs O(theta)" is false for admissible T.
Lemma B gives no lower bound on q*(T e_{k,m}); any rescaling T e_{k,m} -> c_{k,m} T e_{k,m} is admissible. With Phi_m(k) = 2^{-m-j^2} on
[j^2 - j, j^2) and 2^{-m-k} elsewhere, sum_{Phi<theta} Phi_k / theta ~ sqrt(log2(1/theta)) at theta = 1.01*2^{-m-j^2} (exact values 4.7 ... 20.8,
lemma41_log.py). Correct bound: sum_{Phi_k<theta} Phi_k <= sum_k min(theta, 2^{-m-k}) <= theta(log2(1/theta) + 2), so O(theta log(1/theta)).
The identity itself (G(C') - G(C) = sum_Ch Phi^2(w'^2 - w^2), |C'-C| <= sum_Ch Phi^2/g_0, the l_1 bound) is correct.
### 3.5 Smaller points.
Prop 3.3: the steering function for Delta d != 0 is F(mu) = v(xhat') - Delta d beta(xhat'), beta(x) := |R_1 x| - <w_1, R_1 x> >= 0, so the
IVT needs |Delta d| beta <= ||E||_1 ||xhat'||_inf small along the whole path; several blocks need (S) for (v_{m,j} - Delta d_m (R_m*w'_m)_j)_m.
Prop 4.3: as in the table. Lemma 4.2: l_inf vs c_0 moves. 4.5: C (C_part6 9.3) claimed only that implants are never the SOLE support at
intermediate scales — Thm 2.1 is consistent with it (the band (s_1, T_0) is carried by transferred shared structure); "FALSE" overstates.
3.5(R5)/4.4(4)(c) (degenerate peaks via one tuning move "then Thm 2.1 applies"): the implanted gap gamma' gives radius ~ gamma'; a one-sided
(inward-only) box lemma is missing. 3.3/3.5(R1) "infinitely many strict non-peaks is what breaks it": an artefact of the base-garbage
method (P2x Thm 3.5's Bregman route needs no finiteness for Delta d >= 0).

## 4. Numerics (ctx/r2/P2Aref_work/)
thm34_dependence3.py (block norming via the consistency equation mu|zeta| = C; 24 random blocks; Fact C 9e-11, identity 4e-14);
lemma41_log.py (exact rational arithmetic, log-factor counterexample). No finite-model test of Thm 2.1: finite models cannot
discriminate (every functional attains its norm; the unsteered pair is also contractive there); the proof was checked by hand.

## 5. Recommendations
1. Keep Thm 2.1 and Cor 2.3 (with g in C(f) added in (b)) as the main result; fix (C4) for small rho.
2. Withdraw Thm 3.4; replace by (iii') + base steering, split into (TC)-type two-sided steering (plausible; cf. P2x Thm 3.5) and
   pull-only steering (needs a far-tail comparison; OPEN, T-dependent). Withdraw "A_referee §5.5 is too pessimistic" or attribute it to P2x
   Thm 3.5 (Delta d >= 0, (TC)).
3. Downgrade the "f in R at P1's example" sentence of Rem 2.4 to HEURISTIC/OPEN; state the needed lemma: every g in C(f) admits limit
   side decompositions (possibly with shifts or transfer peaks) of coefficient <= 1.
4. Correct Lemma 4.1's consequence (log factor) and Prop 4.3 (s_1 <= eta). Reword 4.5.

## 6. Most valuable idea
Scale decoupling by exact transfer (Thm 2.1): transport the two one-sided linear decompositions of f to an engineered NA point f' with
NO first-order error — recompute the block d-coefficients at f' and enforce the single scalar condition v_m(x') = 0 per block by a
far negative-mass pull (sign-flipped far contacts carrying masses), one raising mass and the intermediate value theorem — and use window
masses plus a theta-tail of the target only for |tau| <= s_1. Then the slack is needed only beyond a FIXED T_0, so the engineering scale
s_1 is decoupled from the slack scale sqrt(p*(f'-f)); this is what makes switching mates over infinite contact sets recoverable without any
rate condition on T. (The referee's complementary observation: the tuning functionals satisfy sum c psi = v, so resonance directions can
only be steered through the base — free coordinates never suffice.)

---------------------------------------------------------------------------------------------------
# Appendix: detailed verification (part files P2A_ref_part1..5.md, verbatim)

# P2 referee (P2A version = P2_notes.md, 512 lines) — part 1: provenance, Part-1 toolkit
Provenance: P2_notes.md (= P2A_notes.md, identical by diff) is the "P2A" instance (toolkit 1.1-1.7, Thm 2.1, 3.1-3.5, 4.1-4.6, 5).
A different referee instance wrote P2_ref_part0.md for the P2x version; to avoid file collisions my part files are P2A_ref_part*.md,
the final report is written to P2_referee.md (as instructed) and duplicated as P2A_referee.md.
Setting checked: finite block set I (p_N), only Lemma B's conclusion on T (I found no hidden use of other properties of T in Part 1-2).

## 1.1 Clamp formula. CORRECT (PROVED).
It is A Fact C restated: on P, |zeta(k)|/|zeta| = |alpha_k| + Phi_k^2 M/C, so C r(k) >= M, signs agree; off P, |w(k)| = C r(k) < M;
zeta(k) = 0 => off P => w(k) = 0. At an NA point the normer is x'/p(x') in c_0 and Fact C's proof uses only w' = J_m(R_m x'),
so the same holds (degree-0 homogeneity: x', xhat', x'/p(x') give the same ratios). Remark: "depends on xi only through u(xi)/|zeta|
and C" is true but C is itself determined implicitly by C^2 = sum Phi^2 w^2 (Lemma 4.1 exploits exactly this).

## 1.2 Convergence along engineered approximants. CORRECT (PROVED).
L compact => L** weak*-to-norm on bounded sets, L** zhat in V; J_m norm-to-weak* continuous at R_m** zhat != 0 (T3);
D_m, R_m* compact; a_n(xhat_n) = 1 = q(xhat_n) with a_n in c_00 gives grad q(xhat_n) = a_n; J_V = (J_m)_m (Observation C, finite I).
f = a + L*w because w = J_V(L** xi) = J_V(L** zhat). Fine.

## 1.3 First-order identity at NA points. CORRECT (PROVED).
<omega, R_m x'> = |R_m x'| <D omega, D w'>/C' for omega off P'_m (Fact C at f'), so <omega - d' w', R_m x'> = 0 and B(x') = g'(x') = 0.
The expansion is A Lemma 7.2 at f' (E_q(a'+tau B) = Fl + Kink + nu Psi; a'(xhat') = 1). Re-derived coordinatewise. Fine.

## 1.4 Two-regime assembly. CORRECT (PROVED).
Checked: 1 + (tau^2/2)(1-delta) <= 1 + tau^2/2 - tau^4/8 iff tau^2 <= 4 delta; sqrt(1+x) >= 1 + x/2 - x^2/8 for 0 <= x <= 8.
|tau| >= T_0: (T_0^2 + |tau| T_0)/6 <= tau^2/3 (T_0 <= |tau| <= 1) and <= |tau|/3 (|tau| >= 1); A Lemma 4.7. NA: f'(x') = 1 and
||(f',g')|| <= 1. Fine.

## 1.5 Averaging over scales. CORRECT (PROVED).
For s_j < |t| (=> |t| > s_J) use (ii)+(iii); sum_{s_j < |t|} s_j < 2|t| (geometric, ratio 1/2) => extra <= 2 kappa t^2/J. Fine.

## 1.6 Two-piece data, automatic facts. CORRECT.
g(xi) = 0 for g in C(f) (1 + t g(xi) <= s(t) for all t); <omega - d w, zeta_m> = 0 => b^+-(zhat) = 0, v(zhat) = 0.
v = b+ - b- = sum v_m - sum Delta d_m R_m* w_m: checked. v = 0 => omega_Delta = 0 (L* injective) => b+ = b-.
Useful observation (implicit in Thm 2.1): v != 0 forces K infinite (v in Y \ c_00 lives on F cup K, F finite).

## 1.7 One-sided admissibility => kappa <= 1. CORRECT (PROVED).
Base: Lemma 7.2 (general, b+ not supported in supp a) with b+(zhat) = 0, Fl, Kink >= 0, Psi(h) >= ||h_perp||^2/(2(1+||h||))
(this lower bound holds for all h). Blocks: A Lemma 4.4(b) with tau -> 0+ (Y -> C). Fine.

# P2 referee — part 2: Theorem 2.1 (engineered recovery of d-neutral two-piece mates)
Verdict: CORRECT (PROVED), one trivial gap (G-a) and two remarks. Every step re-derived by hand.

Re-derivations (all OK):
* v != 0 => v not in R a (a in c_00, Y cap c_00 = {0}) => P_{e-perp}U*v != 0 (U* injective). Identity
  sum_F v_j<PU*v,U*e_j*> + sum_K |v_j| z_j<PU*v,U*e_j*> = ||PU*v||^2 > 0 (v z-signed on K) gives j_+ and s_+ (any sign on F,
  s_+ = z_{j+} on K). Also: v != 0 forces K infinite, so the theorem is only non-trivial at non-attaining f.
* Compatibility (Fact D): z' in c_00, |z'| <= 1 (|z_{j_i}| <= 1-gamma, |p_i| <= gamma), z' = sign a' on supp a' (F: sign kept for
  mu <= |a_{j+}|/2; window: m_j z_j; Far: -m'_j z_j with z' = -z; j_+ in K: mass sign z_{j+}). a'(xhat') = q*(a') = 1 >= q(xhat').
* Step 1: v(xhat') = v(z'-z) + <U*v, e'-e>, v(z'-z) = -2V_Far - V_{>N''} (z_j v_j = |v_j| on K, v = 0 off F cup K, F in [1,N]).
  Lipschitz ||x/|x| - y/|y||| <= 2|x-y|/|y|; |<U*v,e(a''(0))-e>| <= (A_0-1)s_1 + V_Far/2 <= V_Far using 16 rho T_0||U||||U*v|| <= nu
  and V_Far >= 2A_0 s_1. z' does not depend on mu (j_+ keeps its sign); dPsi/dmu = s_+<U*v, P_{e(a'')perp}U*e_{j+}*>/||U*a''||
  >= gamma_+/2 near a; MVT + IVT give mu_* in [0, mu_max]. Psi independent of p (v_{j_i} = 0). Multi-block: v_m(xhat') affine in p
  with slope (v_{m,j_i})_m, y in H_0 (d-neutral: sum_m v_m = v), y -> 0 since v_m(zhat) = |zeta_m| Delta d_m/q_0 = 0.
* Step 2: <D w', D omega> = (C'/|R x'|)(R* omega)(x') for omega off P' (Fact C at f') => d'^+ = d'^- = d'^theta; (2.1.2) re-derived:
  B^+ = B^theta + rho theta v, B^- = B^theta - rho(1-theta)v (uses omega^theta - omega^+ = theta omega_Delta and d-neutrality).
* Step 3: z' -> z coordinatewise (Far in (N, N_2], cut-off beyond N'', p -> 0), masses -> 0 (s_1 <= tau_N/(4A_0) -> 0,
  V_Far <= 2A_0 s_1 + eps_N -> 0); Lemma 1.2; c = (g''-g)(xhat') + g(xhat') -> g(zhat) = 0; g' -> rho g; B^sigma -> rho b^sigma.
* Step 4: coordinatewise radius (fix G1) re-derived from A Lemma 4.4(c): |W(k)| <= (1-d sigma)M - gap(k)(1/2 - d sigma) on supp omega.
* Step 5: no flips (F: |tau rho beta| <= rho T_0 beta_max <= a_min/8 <= (1 - tau rho c)|a'_j|; window masses: m_j/4 vs |a'_j| >= m_j/2
  for sigma = theta; one-sided signs for sigma = +-; Far: |a'_j| >= 2 rho T_0|v_j| >= 2|tau rho beta_j|); kinks: 0 on J, 0 on
  contacts <= N'' with z' = z (designated sign), <= rho|tau|V_{>N''}/2 beyond N'' (z' = 0), 0 for sigma = theta (beta^theta = 0 beyond N).
* Step 6: (tau^2/2)(rho^2 kappa + delta/4) + eps_0 tau^2 = (tau^2/2)(1 - 3delta/2) <= (tau^2/2)(1-delta); Lemma 1.4 with T_0 FIXED.
  The decisive structural point is correct: T_0 depends only on (f, g, rho), so p*(f'-f) need only be small compared with T_0^2,
  not with s_1^2; the window (s_1, T_0) is covered by the EXACT transfer of the one-sided decompositions.

(G-a) [trivial] Step 1 uses Psi(0) >= -4V_Far, i.e. V_{>N''} <= V_Far. From (C4), V_{>N''} <= eps_0 s_1/rho = delta s_1/(8 rho) and
  V_Far >= 2A_0 s_1 >= 2 s_1: this holds only for rho >= 1/32. Fix: require V_{>N''} <= min(eps_0 s_1/rho, V_Far) in (C4)
  (or deduce small rho from rho = 1/2 by scaling g' -> (rho/rho_1) g', which keeps (f', g') NA since g'(x') = 0 is not even needed:
  ||(f', lambda g')|| <= 1 = f'(x') for |lambda| <= 1).
(R-a) Sharper reading of the hypotheses: kappa only enters through rho^2 kappa < 1; g in C(f) is used (only) in Lemma 1.4 for
  |tau| >= T_0. Both are needed; in Cor 2.3(b) the hypothesis g in C(f) has been dropped (see part 4).
(R-b) Nothing about T beyond Lemma B is used: no rates, tails, or independence (tau_N > 0 only needs v not in c_00).
  Hidden-assumption hunt (weak* vs norm, uniformity in tau, attained infima, c_0 vs l_inf): all OK — z' in c_00, all estimates are
  uniform on the FIXED interval |tau| <= T_0, Lemma 1.2 gives norm convergence of f' (L compact), and only finitely many data
  (gaps on supp omega^sigma, d', C', nu', e') need to converge.

# P2 referee — part 3: Props 3.1-3.3, Theorem 3.4

## Prop 3.1 (mixed term). CORRECT (PROVED).
d/d delta e(a + delta y)|_0 = P_{e-perp}U*y/nu; B(xhat') - B(zhat) = <U*B, e(delta) - e> when z' = z on supp B; second-order
remainder O(delta^2 ||U*B||). (a) absorbed by c = g''(xhat') (Thm 2.1); (b) B^+ - B^- = rho v and both first-order terms vanish iff
v(xhat') = 0 — consistent with Thm 2.1 Step 1. (c),(d) are qualitative (d is labelled HEURISTIC where it should be). Fine.

## Prop 3.2 (consistency identity). CORRECT (PROVED).
Re-derived: B'_t - B'_{t'} = rho sum R*(omega_{t'} - omega_t) - rho sum Delta'_m R* w'_m and B_t - B_{t'} = sum R*(omega_{t'} - omega_t)
- sum Delta_m R* w_m, whence the displayed formula. Delta'_m = (R_m*(omega_{t'} - omega_t))(x')/|R_m x'|_m by Fact C at f' (supports off P').
The sentence "at scales tau >= s_1 they MUST be <= eps_0 s_1 in l_1" is a sufficient condition (cost <= 2|tau| x mass), not a
proved necessity (only the part at non-contacts outside supp a' is charged, with weight 1 - |z'_j|): read "suffices".

## Prop 3.3 (garbage identity, Delta d != 0). CORRECT AS A SUFFICIENT CONDITION, with two fixable gaps.
Algebra re-derived: with Delta d'_m = Delta d_m, B^+ - B^- = rho(v_1... ) = rho(v + E), E = -sum Delta d_m R_m*(w'_m - w_m); E's cost
<= 2 rho theta |tau| ||E||_1 per side (kink or flip, |x| - z'x <= 2|x|), Hilbert change O(||E||) -> 0. B^theta contains no E.
(G3.3a) "exactly when" (task wording) / "the ONLY change" (notes) must read "provided": E may sit on cheap coordinates; no
  necessity is proved.
(G3.3b) Steering for Delta d != 0 is NOT "verbatim": the condition is F(mu) := v_1(xhat') - Delta d |R_1 xhat'|_1 = 0, i.e.
  F = v(xhat') - Delta d beta(xhat') with beta(x) := |R_1 x|_1 - <w_1, R_1 x> = (R_1*(w'_1 - w_1))(x) >= 0. The IVT needs |Delta d| beta
  small compared with V_Far along the WHOLE path mu in [0, mu_max] (|Delta d| beta <= ||E(mu)||_1 ||xhat'||_inf), so the E-bound must
  hold uniformly along the steering path (enlarge mu_max to 16V_Far/gamma_+). For |I_0| >= 2 the span hypothesis must be stated for
  the vectors (v_{m,j} - Delta d_m (R_m* w'_m)_j)_m, not (S).

## Theorem 3.4 (non-neutral two-piece mates at block-tame active blocks). WRONG AS STATED (vacuous), repair possible only partly.
**Proposition R1 (PROVED).** For two-piece data (1.6) with omega_Delta != 0 the restrictions to J_gamma of
{psi_{k,m} : k in Qbar_m, m in I_0} are linearly dependent for every gamma > 0. Hypothesis (iii) of Thm 3.4 therefore never holds
in a non-trivial case (omega_Delta = 0 gives v = 0, a finite certificate).
*Proof.* supp omega_Delta,m is contained in the strict non-peaks, hence in Qbar_m. Put c_{k,m} := lambda_{k,m} omega_Delta,m(k) (not all 0).
Then sum_k c_{k,m} u_{k,m} = R_m* omega_Delta,m = v_m and sum_k c_{k,m} u_{k,m}(xi) = <omega_Delta,m, zeta_m> = |zeta_m| Delta d_m (Fact C,
omega_Delta,m off P_m). Hence sum_{k,m} c_{k,m} psi_{k,m} = sum_m (v_m - Delta d_m R_m* w_m) = b+ - b- = v, and v is supported in F cup K,
which is disjoint from J_gamma = {j notin F : |z_j| <= 1 - gamma}. QED. (Numerical confirmation of the identity: P2Aref_work/thm34_*.py.)
*Meaning.* The derivative of the tuning map p -> (u_{k,m}(xhat'(p))/|R_m xhat'(p)|_m)_{(k,m) in Qbar} in the free variables has range in
the hyperplane {y : sum c_{k,m}|zeta_m| y_{k,m} = 0}; the missing direction is exactly the steering quantity v(xhat') (mixed term of 3.1).
So "construction of Thm 2.1 WITHOUT Far set and raising mass (steering is part of the tuning)" cannot work: the residual of the
window masses along this direction is ~ s_1 gamma_+ and is invisible to free moves. This is the authors' own Remark after 4.2
(resonance carriers make r_W(J) = 0), applied to psi instead of u. The example claim ("P1's example ... covered once (iii) holds")
is void: there |Qbar_1| = 1 and psi_{2,1}|_J = u|_J = 0.
**Repair (SKETCH, my assessment).** Replace (iii) by (iii'): the restrictions to J_gamma of the psi_{k,m} span a space of dimension
|Qbar| - 1 (the c-relation is the only relation), and reinstate base-side steering for the c-direction (Graves in (mu, p); the
tuning map is C^1 on finite-dimensional families: Lipschitz + Gateaux => Hadamard, J_m norm-to-weak* continuous).
Then a NEW issue appears that the notes do not address: when the base steering needs a PULL (all mass directions raise, e.g. |F| = 1
and z_j<P U*v, U*e_j*> >= 0 on K, which is P1's diagonal-U situation), the pull is made by Far flips z'_j = -z_j on
Far in (N, N_2], which move EVERY block functional u_{k,m}(xhat') by up to 2||u_{k,m} 1_Far||_1. In the d-neutral case this is harmless
(only f' -> f matters); in the non-neutral case it enters E through peaks of the active block pushed below threshold or flipped
(a peak u_k ~ e_j*/q*(e_j*), j in Far, changes w(k) by ~ 2M). These perturbations are not O(s_1) uniformly in k, so (MS) at scale s_1
does not control them; controlling them needs a comparison between the tails of the first ~log(1/s_1) block vectors and the tail tau_N
of v (a RATE condition, not implied by Lemma B; it does hold for P1's T thanks to its allowedness rule c_l <= 2^{-2s} c_{l'}).
If two-sided steering by O(s_1) masses is available (some j in F with <PU*v, U*e_j*> != 0, or a contact with z_j<PU*v,U*e_j*> < 0),
all perturbations are O(s_1) in sup norm plus the late cut-off N'', and the repaired statement is plausible (SKETCH): changed peaks
have weight o(s_1) by (MS) + deep weight m 2^{-m-K_0}, Lemma 4.1 gives |C'-C| = o(s_1) and ||E||_1 = o(s_1); degenerate peaks stay
within |w'(k) - w(k)| <= (1 + r)|C' - C|.
**Consequence.** The summary claim "A_referee §5.5 ('engineering breaks when d != 0') is too pessimistic" is NOT established.
What is established: Prop 3.3 (sufficient condition) and, by the repair, a restricted class (two-sided mass steering, finite Qbar,
(MS), (iii')).

# P2 referee — part 4: Cor 2.3, Remark 2.4, Lemmas 4.1-4.2, Prop 4.3

## Cor 2.3 (a). CORRECT WITH FIXABLE GAP.
Data check: b+ = g, omega+ = 0; b- = g - v, omega- = (c/lambda_{k0}) e_{k0}; R_m* omega- = v; d- = Phi_{k0}^2 w(k0) c/(lambda C) = 0 = d+;
on K: b+_j = v_j 1_{K1}(j), b-_j = -v_j 1_{K\K1}(j), so the contact signs hold iff v is z-signed on K (built into A_referee 5.2).
Gap: "P1 Prop 2.3 shows one-sided admissibility for small c" is a statement about P1's specific example (F = {1}). For the general
A_referee 5.2 setting the analogue (no flips on the finite F for |tau| <~ min|a_j|/|b_j| ~ 1/c, contacts used with the free sign,
Hilbert term O(c^2 tau^2), block N = M + sqrt(C^2 + tau^2 c^2/m^2), and g in C(f) for small c by the crude bound) is routine but must be
written; it is NOT literally P1 2.3. Also the EXISTENCE of such data in general is still A_referee's generic SKETCH; for P1's T it is
PROVED (P1 2.1-2.3). With these remarks: g in Ls(f) for every such mate.

## Cor 2.3 (b). CORRECT WITH FIXABLE GAP (missing hypothesis).
The first sentence ("every g in E_u with mu+ <= inf theta, mu- >= sup theta and rho^2 max(...) < 1 has (f, rho g) in cl NA") omits
g in C(f). Thm 2.1 uses g in C(f) (Lemma 1.4, |tau| >= T_0), and rho^2 kappa < 1 does NOT imply it (h only sees ||P_{e-perp}U*b||,
and U* is compact: a large contact mass far out has small h but large q*). This is exactly P1-referee's correction (C4), which the
notes cite ("with P1-referee's sharpening") but did not implement. Fix: "every g in E_u cap C(f) with ...".
The slab statement is correct: P1 6.2 gives slab in C(f) and one-sided admissible explicit decompositions with mu+- = inf/sup theta
(d+- = 0 since w_1(2) = 0; signs (theta_j - mu+)u_j >= 0 >= (theta_j - mu-)u_j on K'), so Lemma 1.7 gives kappa <= 1 and Thm 2.1
gives g in Ls(f). The explicit defect mates g_{K1} (P1 2.4, c small) lie in the slab. So: P1's explicit defect mates ARE in Ls(f)
(PROVED), confirming that P1's Def(f) != empty is a defect of the INTRINSIC mechanisms only.

## Cor 2.3 (c). CORRECT (direct from Thm 2.1 + Lemma 1.7). "Complete class of exact-resonance switching mates" is descriptive only.

## Remark 2.4 (shifted two-piece data). First sentence: plausible SKETCH. Second sentence ("would give f in R"): HEURISTIC/OPEN.
(i) Extension to shifts tau^2 theta^sigma_m w'_m: I checked the domination claim coordinate by coordinate. Window contacts with
masses: if the shift is cheap at f (v_theta,j of sign -z_j), the term -tau^2 v'_j has the sign of the mass a'_j (no flip); if it is
expensive at f (kink 2tau^2|v_j|), the flip cost at f' is <= 2tau^2|v'_j|. Far flipped contacts and the cut-off beyond N'' cost at most
2 tau^2 ||v' 1_{(N,inf)}||_1 = o(1) tau^2. So limsup kappa_q' <= kappa_q holds along the construction; with uniform convergence on the
fixed range |tau| <= T_0 the extension is plausible. Not written; SKETCH is the right label.
(ii) "Combined with P1 6.1 this would give f in R": P1 6.1 only proves g in E_u and that LIMITS mu+- of the carrier coefficients
bracket theta(g). It does NOT show that optimal decompositions are asymptotically shifted two-piece decompositions with H^sh <= 1;
P1's own remark says peaks, level shifts and free coordinates may contribute O(t^2) to the costs, and P1-referee (C1) shows the
sharp second-order invariant at such points involves transfer-peak rebalancing (Gamma_w <= H^sh), which is not of shift type.
The assertion "the limits mu+- satisfy only SHIFTED second-order bounds H^sh <= 1" is unproved. So "f in R at P1's example" stays OPEN.

## Lemma 4.1 (replication identity). CORRECT; the "Consequence (deep replication)" is WRONG in its O(theta) form (fixable).
G(c) = c^2(1 - rho_W) - (1-c)^2 S_P: G(C') - G(C) = sum_Ch Phi^2 (w'^2 - w^2) re-derived from C^2 = sum Phi^2 w^2 with w = C sgn r on W_off
and |w| = 1 - C on W_P (Lemma 1.1); 1 - rho_W >= sum_P Phi^2 M^2/C^2 > 0; G' >= 2c(1 - rho_W) on [0,1]; the w'-w formulas and the l_1
bound are right (||u_k||_1 <= q*(u_k) = 1). Two corrections:
(4.1a) "sum_{Phi_m(k) < theta} lambda_k <= 2 m theta" is false for admissible T: Lemma B gives no lower bound on q*(T e_{k,m}), and any
coordinatewise rescaling T e_{k,m} -> c_{k,m} T e_{k,m} (0 < c <= 1, sup attained) is again admissible. Example: Phi_m(k) = 2^{-m-j^2}
for k in [j^2 - j, j^2) (j >= 2), Phi_m(k) = 2^{-m-k} otherwise (admissible: 2^{-m-j^2} <= 2^{-m-k} for k < j^2). At theta_j = 1.01 * 2^{-m-j^2}:
sum_{Phi < theta_j} Phi_k >= j 2^{-m-j^2} ~ theta_j sqrt(log2(1/theta_j)); exact computation (P2Aref_work/lemma41_log.py, m = 1):
ratio sum/theta = 4.7, 7.9, 11.9, 15.8, 20.8 for j = 3, 6, 10, 14, 19 (the claim would give <= 2). The correct general bound is
sum_{Phi_k < theta} Phi_k <= sum_k min(theta, 2^{-m-k}) <= theta (log2(1/theta) + 2), and similarly sum_{Phi<theta} Phi^2 <=
theta^2 (log2(1/theta) + 2). So deep replication to depth theta costs O(theta log(1/theta)), not O(theta) (harmless for 4.4: replace
theta by theta/log(1/theta)).
(4.1b) c_f also depends on rho_W through g_0 (not only on m, M, C).

## Lemma 4.2 (retuning feasibility). CORRECT for moves y in l_inf(G) (weak*-compact ball); for moves in c_0/c_00 (needed so that z'
stays in c_0 and f' is NA) the reachable set is a dense convex subset of the same compact set, so "iff" holds for the relative
interior only, and the radius statement with strict inequality max|delta_k| < A r_W(G). Trivial fix. The resonance remark is right
(and it is precisely what invalidates Thm 3.4 (iii), part 3).

## Prop 4.3 (abstract scheme). CORRECT WITH FIXABLE GAP.
Lemma 1.5 with Q = 1 - 2delta and J >= 4kappa/delta gives the bound (1 - delta) on |t| <= T_0. But Lemma 1.4 also needs
p*(g' - rho g) <= (1 - rho^2)T_0/6, and the proof only has p*(g' - rho g) <= 2kappa s_1/J + eta <= delta s_1/2 + eta. Since s_1 is only
assumed <= T_0, this fails when delta > (1 - rho^2)/3 ("once eta and s_1 are small" is not implied by the hypotheses). Fix: add
s_1 <= eta to the hypotheses (natural), or require J >= max(4kappa/delta, 24 kappa/(1 - rho^2)).

# P2 referee — part 5: other statements, cross-references, numerics

## Other statements of P2A (not in the assigned list, checked in passing)
* 3.3 "Why this is delicate" and 3.5 (R1)/4.6 (R1) ("what breaks engineering is infinitely many strict non-peaks"): an artefact of
  putting the d-mismatch E = -Delta d R*(w'-w) into the BASE (l_1-displacement Theta(s_1)). The concurrent instance P2x (Thm 3.5,
  refereed CORRECT in the P2x referee report) keeps the mismatch in the BLOCK as a multiple of (w - w') and pays only the Bregman excess
  e(zhat; xhat') = o(s_1) (P2x 2.2-2.3), with NO finiteness of non-peaks, for Delta d_m >= 0 under the cone condition (TC). So the
  residual class (R1) should read: Delta d_m < 0 (any structure), and Delta d_m > 0 when (TC) fails and pulls are needed (far-tail
  comparison) — consistent with part 3 (Far-flip collateral damage).
* 3.5 (R5)/4.4(4)(c) (degenerate peaks "turned into strict non-peaks with tiny gap at f' by one tuning move, after which Thm 2.1/3.4
  apply"): Thm 2.1 needs off-peak carriers AT f with gaps >= gamma_0 (Step 4: coordinatewise radius >= rho T_0, T_0 fixed). A tiny implanted
  gap gamma' gives a two-sided radius ~ gamma'; what is needed is a ONE-SIDED box estimate (inward use only: |W(k)| decreasing; outward use
  raises the sup norm at first order — the P2x referee makes the same point for P2x 4.4(b)) plus a theta-certificate with capacity
  gamma' >~ s_1 |omega(k)| for |tau| <= s_1. Plausible, but "Thm 2.1 applies" is not accurate; SKETCH with a missing lemma.
  (Fact C gives w(k) = C zeta(k)/(Phi^2|zeta|) also at degenerate peaks (alpha_k = 0), so the d-identities extend.)
* 4.5 ("C's implant-scale-gap heuristic as an obstruction: FALSE"): C (C_part6 9.3) only claims that the window (Phi, sqrt Phi) "must be
  covered by structure that xi and x' share" and that implants are "never the sole support of a mate component at intermediate
  scales". Thm 2.1 is CONSISTENT with this (the masses serve |tau| <= s_1; (s_1, T_0) is covered by the exactly transferred one-sided
  decompositions of f = shared structure). The FALSE verdict attacks a stronger statement C did not make; correct reading:
  "not an obstruction to engineered recovery when the intermediate band is carried by transferred structure".
* 4.4 (QI): labels (identities PROVED / necessity HEURISTIC / OPEN) are appropriate; with the Lemma 4.1 correction the depth condition
  becomes theta log(1/theta) <~ eps_0 s_J^2.

## Numerics (independent; scripts in ctx/r2/P2Aref_work/)
* thm34_dependence3.py: accurate block norming via the clamp-consistency equation mu|zeta| = C (Lemma 1.1); 24 random blocks with
  non-peaks at half threshold: |N(w) - 1| <= 1e-16, Fact C <omega, zeta> = |zeta| d(omega) to 9e-11 (relative), and the identity
  sum_k lambda_k omega(k) psi_k = R*omega - d R*w to 4e-14 (relative). This is the identity that makes Thm 3.4 (iii) impossible.
  (A first version with grid maximisation of <w,zeta> over M had 1e-3 errors: the objective is flat at its maximum; the consistency
  equation is the well-conditioned characterisation. If no sign change exists, the optimum is the boundary M = 1/(1+||Phi||), all peaks.)
* lemma41_log.py: exact rational computation of the counterexample to "sum_{Phi<theta} lambda <= 2m theta" (ratio grows like
  sqrt(log2(1/theta)), 20.8 at log2(1/theta) = 362).
* I did not re-run a finite-model test of Thm 2.1: in finite models every functional attains its norm and the unsteered pair is also
  contractive (the author says so), so such tests cannot discriminate; the proof was checked by hand instead (part 2).

## Cross-check with the other P2 referee (P2x report, now in P2_referee.md, written 01:21)
Agreement: P2A Thm 2.1 CORRECT; Far flips break the Bregman/E bound for Delta d > 0 with pulls (their 3.2, my part 3); on free
coordinates sum_m V_m(j) = v(j) = 0 so free moves cannot steer the total direction (their 3.4 "structure of (TC)", which is the
one-line reason for my Proposition R1 refuting P2A Thm 3.4 (iii)). New here: Thm 3.4 vacuity, Cor 2.3(b) missing hypothesis,
Rem 2.4 consequence unsupported, Lemma 4.1 log factor, Prop 4.3 gap, Prop 3.3 path-uniformity, 4.5 mischaracterisation.
