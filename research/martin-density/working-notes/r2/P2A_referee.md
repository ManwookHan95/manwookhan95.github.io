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
