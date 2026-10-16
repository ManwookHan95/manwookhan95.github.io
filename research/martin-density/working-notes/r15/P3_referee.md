# Referee report on P3 (Round 15): transition-cell excess (test (a)) and the capacity route (R6) (test (b))

Read in full: r15/P3_notes.md and part files P3_part0-8 (and P3_final_s0..s6, identical to the notes), P3_work scripts; BRIEFING_R2
Addenda 13, 14a, 14b, NEG; neg/N1-N3 referee reports and ref notes; r3/R3_referee.md, r3/refwork, r3/work/modelN.py; r1/E_notes 4.1-4.4,
7.3-7.5.  Full proofs of every fix and addition: r15/P3_ref_notes.md (parts P3_ref_part0-6).  Scripts: r15/P3_ref_work/ (independent
QP solver sep_ref.py written from scratch; exact/tabulated identities ec_fast.py, ec_vec.py, ec_vec2.py validated against it).
Everything below is about Model N_RN (P3's separable real-norm junction model) unless stated otherwise; numerics are sanity checks.

요약 (사용자용).  P3 의 모델 수준 정리들(Lemma B0, W', W*', FO, Lemma L, Prop W, EC1, EC2)은 독립적으로 다시 유도했고 모두 맞습니다
(독립 solver 로 항등식 12자리, R(W_c) = 1).  두 가지 오류가 있습니다.  (1) Prop SR(합 규칙)은 이산 격자에서 틀립니다 — 결론에는
영향 없음.  (2) 핵심 결함: Lemma BAL 의 가정 (Bal) 은 "cancellation staircase 의 정의"가 아닙니다.  오차 클래스들이 서로 다른 깊이에
있으면(Martin 노름에서는 이것이 일반적) P3 의 순수 V-shift 는 실패합니다(R >= 1.074, 희소 배치에서는 무한대).  그러나 결론 자체는
살아납니다: 심사자가 증명한 Theorem KKT — f 의 균형 문제의 KKT 승수 (V, eta) 를 클래스별 shift 로 쓰면(전역 shift + window 함수)
모든 cancellation cell 에서 R = 1 정확히 (수치로 1e-11).  핵심 도구는 "한 유형 변환 = 용량 공간에서의 평행이동, 프로파일 =
Bregman divergence" 라는 재정식화로, EC2 를 세 줄로 증명합니다.  또한 모든 모델 정리는 A = 0 (지속되는 1차 base 비용 없음)에서만
성립합니다: EC 가 core error 를 제거하지 못하면 one-type 변환에 1차 초과 c_1(ln(a/delta) - l_A) 가 생깁니다 (FO-A).  반례도,
negative 증명의 단계도 없습니다.  주 질문은 OPEN, 증거는 여전히 density 쪽.

## A. Verdicts

| Claim (P3 label) | Verdict | Notes |
|---|---|---|
| Lemma B0, real-norm coupling (PROVED) | CORRECT | identity re-derived; it is the NECESSARY weighted budget (sufficiency at f' = fair block-to-base rebalancing, part of (T)); E's Model N and R3-ref scripts indeed use non-real-norm peak costs (checked in code: 17x and 8x too small, 2x too large for coupled_full) |
| Lemma W' (PROVED) | CORRECT | precision: with varying normalisations n_k (and v-coefficients c_k) the band is in shift-depth Lambda_k = lam_k n_k/c_k; the identity survives because the weight w_k = (c_k/n_k)^2 cancels |
| Theorem W*' (PROVED) | CORRECT | every integral re-derived |
| Proposition FO (PROVED, A = 0) | CORRECT | all six coefficients re-derived (C9 confirmed); referee addition FO-A for A > 0 |
| Proposition SR (PROVED) | CORRECT only in the continuum; FALSE as stated for discrete lattices (fixable) | room step assumes mu^+(tau) = mu^-(tau); exact first-order sum is (C(V)/tau)(mu^+ - mu^-), numerically both sides can drop at first order (phase 1/4: -9.5e-6 and -1.5e-6); harmless for the conclusions |
| Lemma L (PROVED) | CORRECT | add: margins bounded below; weights |
| Proposition W (PROVED) | CORRECT | add: inf psi attained (true for self-similar lattices) |
| Theorem EC1 (PROVED) | CORRECT | every conjugate and the (I-b) KKT check re-derived; 12-digit agreement with an independent solver |
| Corollary EC2 (PROVED) | CORRECT | independent numerics: R(W_c) = 1 + 3e-8 (argmin precision); misplacement slopes 0.56 / 1.15 per per cent; one-line proof via Bregman form (C.1) |
| Restoration depth (SKETCH) | CORRECT, upgraded to PROVED (model) | side + is unchanged by dead deep carriers; side - by convexity in the load: R <= 1 + K 2^-L for lattices with sum_{lam < x} lam <= K_1 x |
| Test (b) capacity route (PROVED at model level) | CORRECT at A = 0; scope restriction for A > 0 | one band at W_c meets the load exactly; two bands: factor 2 at the bottom and strict first-order saving (A = 0); R3-ref deficits are artefacts of their peak/Hilbert ratio; with persistent first-order base costs one-type conversion has a genuine first-order excess (FO-A), so "A > 0 favours the approximant" holds only through EC |
| Lemma G (PROVED) | CORRECT | scope: forbids converting a balanced P- set and a balanced P+ set of one group; needs e_spread > 0 (if E_k(zhat) = 0 destruction converts instead) |
| Lemma GB (PROVED) | CORRECT | general d: Radon's theorem in the (d-1)-dimensional hyperplane {e(zhat) = 1}; independent P-/P+ choices need disjoint group sets, hence 2(d+1) groups |
| Lemma BAL (PROVED) | implication CORRECT; parenthetical FALSE | (Bal) holds only for symmetric layouts; it is not the defining property of cancellation staircases (balance at f is ENFORCED by first-order near-error costs, not produced by the separable optimum) |
| Test (a): "defeated by the pure V-shift at W_c, R = 1 (EC2 + BAL)" (PROVED) | FALSE for asymmetric layouts | two classes +-e at half-octave phase: R >= 1.0743 for every pure V-shift (brute-force and exact identities agree); sparse antiphase classes: R unbounded (one class always has an empty band) |
| Test (a): "no configuration has a uniform hand-over excess; no EC / cross-group partner / two-type conversion needed" (PROVED) | TRUE at A = 0 — by the referee's Theorem KKT; P3's proof covers only (Bal) | class shifts = KKT multipliers (V, eta) of f's balancing problem (global shift + window functional): R = 1 exactly for every cancellation cell with a fixed finite-dimensional near-error space; numerically 1.000000000025 and 0.999999999995 in two asymmetric layouts, 1 + 4e-5 (grid) in a non-simplex three-class layout |
| E's rigid design (SKETCH) | label CORRECT; sub-claim needs restriction | (O4) gives TWO-mode levers and a strict saving at A = 0; E's design is error-dominated (A > 0): then TWO mode with kd = 1 has first-order coefficient c_1(2/a - l_A) > 0 once l_A < 2/a (numerically +0.33 at A = 4); the defeat rests on EC (R3 Thm EC + (HT-EC)) or on kd = 0 |
| Conjecture R6** "model content FALSE" (FALSE) | correct at A = 0 only | clauses (D) and near-error (E) are refuted (Theorem KKT); a core-error version survives as (R6-A) |
| Residuals (R6-tie), (T) (OPEN) | agreed | add (R6-A) |

## B. Required fixes (proofs in P3_ref_notes.md)
 F1 (SR) State Proposition SR under mu^+(tau) = mu^-(tau) (continuum, or equal mirror lattices) and record the general first-order sum
    (C(V)/tau)(mu^+ - mu^-) (notes A.1).  Delete "So there is no strict first-order saving" as a general statement.
 F2 (BAL) Delete "(the defining property of cancellation staircases)"; state Lemma BAL for symmetric layouts.  Replace the test-(a)
    mechanism by Theorem KKT (notes part 4, 4.3): class shifts V_c = V + <eta, E^(c)> = KKT multipliers of f's balancing problem at
    the critical scale.  Record the counterexample to the pure V-shift (notes part 3, 3.5).
 F3 (scope A = 0) Every "PROVED (model)" defeat in Sections 2-5 is at A = 0 (or with EC removing A-costs at all junction scales).
    Add FO-A (notes A.2) and the residual (R6-A); qualify "A > 0 favours the approximant" (1.5) and "E's design is strictly
    favourable" (4.6, 5.2) accordingly.
 F4 (hypotheses) Prop W / EC2: inf psi attained; Lemma L: margins bounded below; weights w_k for varying normalisations (notes 2.7).
 F5 (status) Restoration depth: SKETCH -> PROVED (model), notes 2.6.

## C. Referee additions (all PROVED at model level unless stated)
 C.1 Bregman form.  With Gamma = odd-extended inverse capacity C^{-1} and A = int Gamma: P_f(tau, +-; S) = A(+-S tau)/tau^2 and the
     one-type shift of capacity Y = C(V) gives P_f'(tau, +-; S) = D_A(Y +- S tau, Y)/tau^2 (Bregman divergence).  The parabola s x^2
     (s = sup A(x)/x^2) is tangent to A at every maximiser x* = C(W_c), so D_A(x* + h, x*) <= s h^2: Corollary EC2 in one line.
 C.2 THEOREM KKT.  For any cancellation cell (error classes c with vectors E^(c) in a fixed finite-dimensional space, arbitrary
     lattices/phases/weights, exact balance at f and f'), f's profile is H(t)/t^2 with H the balanced infimal convolution of the A_c;
     at a maximiser Z* of H(x)/x^2 with optimal allocation Y and multipliers (V, eta), the class shifts V_c = V + <eta, E^(c)> give
     P_f'(tau, +-) = D_H(Z* +- tau, Z*)/tau^2 <= s: R = 1, with no EC, no cross-group partner and no two-type conversion.  The
     approximant's levers (global shift, window functionals) are exactly the dual variables of f's balancing constraints.
 C.3 Asymmetric counterexample to the pure V-shift (NUMERICAL, exact identities + brute-force QP): see table A.
 C.4 FO-A (continuum): persistent first-order base cost A lambda/tau per unit at f and f' gives ONE-mode coefficients
     +-c_1(ln(a/delta) - l_A) and TWO-mode -c_1 l_A (kd 0), c_1(2/a - l_A) (kd 1), l_A = ln((2MB a + A)/(2MB delta + A)); confirmed
     numerically (0.4045 vs 0.4055, 0.7592 vs 0.7621, 0.3323 vs 0.3302).
 C.5 Restoration depth bound R <= 1 + K 2^-L (notes 2.6).
 C.6 Numerical caution: the tabulated EC1 identities lose all accuracy for tau << V (cancellation of terms of size (C(V)/tau)^2);
     small residual excesses (1e-5 - 4e-4) seen by grid optimisers are artefacts; use the QP solver there.

## D. On the main question
Nothing in P3 or in this report is a step towards non-density: no admissible T, no row f, no mate g is constructed, and no lower
bound over NA approximants is proved.  At model level both falsification tests are now defeated at A = 0 for ALL cancellation cells
(P3's EC2 for one class, the referee's Theorem KKT for balanced multi-class cells), and the R3-ref capacity deficits are artefacts.
What could still produce a model-level excess is narrow and explicit: (R6-tie) forced destruction right below every junction band, or
(R6-A) persistent, EC-proof first-order base costs at the junction together with the Gordan structure.  Density of NA((c_0, p), l_2^2)
remains OPEN; the evidence continues to favour density (HEURISTIC).

## E. Single most valuable idea
One-type conversion is a translation in capacity space: with A = int C^{-1}, f's one-sided profile is A(t)/t^2 and the converted
approximant's profile is the Bregman divergence D_A(Y +- t, Y)/t^2.  The supporting parabola s x^2 is tangent to A at every maximiser
of A(x)/x^2, so translating there is exactly free; and for balanced multi-class cells the same holds for the infimal convolution H, with
the required class shifts given by the KKT multipliers of f's balancing problem -- the approximant's global shift and window levers are
precisely the dual variables of f's near-error constraints.

## F. Precisely open
 1. (T) Real-norm transfer of Model N_RN: lower bound for the true cost of the mate at f by the model profile (transport of matched
    structure, R3-ref P5); fair block-to-base rebalancing at f' (sufficiency of the weighted budget, r1/A); realisability of (V, eta)
    and of the restored groups by NA rows with finite base support; base block and other blocks.
 2. (R6-tie) A design forcing destruction right below every junction band while keeping the Gordan structure (FO excess c_1 4/a).
 3. (R6-A) Junction carriers with first-order base costs that EC cannot remove (core-error directions escaping every fixed
    finite-dimensional space or not approximable at the required rates, E's (A5)) plus no two-type conversion: FO-A gives a uniform
    first-order excess for every one-type/KKT strategy; whether cross-group two-type conversion or other levers remove it is open.
 4. E's rigid design in the error-dominated regime without EC (equivalently (HT-EC)).
 5. Density of NA((c_0, p), l_2^2) for Martin's renormings (for the designed operator or for every admissible T): OPEN.
