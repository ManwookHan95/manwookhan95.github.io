# Referee report on N2 (negative track: adversarial rigid design and a candidate pair)

Read in full: neg/N2_notes.md, N2_part0-3.md, N2_work/pb_check*.py; sources used: Part I (setting, lem:dualball, lem:threshold,
prop:forced/smooth/continuity/approximants/reduction/primal, lem:pair, thm:compact, thm:lowerlimit, def:tame, thm:tamefibre,
prop:intrinsic, lem:localformula, prop:nonrecovery, def:BT), Part II (f[a', z'], Lemma T, Lemma S, Cor. S1/S2), r14/G3 (Lemmas
1.1-1.4, Cor. 1.3), r1/E_notes 2.2.  Referee parts: neg/N2_ref_part1-4.md; full proofs of all fixes: neg/N2_ref_notes.md;
scripts: neg/N2_ref_work/ (lemma14_check*.py, lemma14_balanced.py, reading_counter.py, pbmodel.py, pb_ref_check*.py,
push_calculus_check.py).

요약 (사용자용).  N2의 증명된 주장들은 (아래 세 가지 수정 후) 모두 맞습니다.  핵심 예제(Lemma B만 쓰는 T_PB, 접점도 strict
non-peak도 없는 행 f, 모든 스케일에서 일방향 peak 계단으로만 운반되는 mate gamma h, K(f) = {0})를 60자리 정밀도로 다시
계산했고, canonical truncation f_N 자체가 gamma h 를 fibre 에 가지므로 (f, gamma h)가 회복된다는 결론은 옳습니다.  수정할 점:
(1) Lemma 1.4 의 "relevant carrier만 기여한다"는 해석은 틀렸습니다(강건한 peak 를 미는 것만으로도 strict non-peak 의 D-질량에
비례하는 2차 비용이 생김) — 균형항을 포함한 올바른 상계(Lemma 1.4'')로 교체;  (2) Remark 1.3 의 "only if" 방향은 단일 mate 용
compactness 논증이 필요(보충함);  (3) N >= 2 블록에 "같은 벡터"를 쓰면 단사성이 깨짐 — 블록별 사적 서명으로 교정하면 N >= 2
결과가 상수 그대로 PROVED.  과장된 표현: "canonical truncation 이 모든 것을 회복한다"는 [-gamma_0, gamma_0]h 에 대해서만 증명됨.
"negative 로 가야 하나?"에 대한 판단: N2 와 이 검토 모두 반례 후보를 주지 않습니다.  새로 증명한 push calculus 는 peak 계단을
통한 일방향 스위칭 비용이 행의 norm-attaining 여부와 무관함을 보여 주므로, 반례는 "어떤 c_0 근사행도 재현할 수 없는" 원거리
상쇄 구조를 요구하고, 비회복 증명은 모든 NA 근사행에 대한 균일한 하한을 요구합니다.  negative 쪽은 주 경로로 권하지 않으며,
유한 "transition cell" 계산을 반증 테스트로 두는 것이 합리적입니다.

## A. Verdicts on the claims submitted for checking

| Claim | N2 label | Verdict | Notes |
|---|---|---|---|
| Witness calculus: Lemma 1.1 | PROVED | CORRECT | holds at every row and every x != 0 (NA not needed) |
| Remark 1.2 (minimax identity) | PROVED | CORRECT | Sion's theorem, C(f') weak*-compact convex |
| Remark 1.3 (finite test spaces) | PROVED | CORRECT with fix F1 | the cited justification ((R3), whole-fibre statements) does not give the single-mate "only if"; complete proof in ref_notes 1 |
| Lemma 1.4 (primal splitting bound) | PROVED | CORRECT | re-derived; ~4000 random valid splits, no violation |
| "Reading" of Lemma 1.4 (only relevant carriers contribute, per-carrier bound) | stated as the content of the PROVED tool | FALSE as stated (fix F2) | counterexample: a push on a robust peak costs C c_Q (dS)^2/(2|zeta|F_2) > 0 (Part I lem:localformula); replaced by Lemmas 1.4', 1.4'' (balanced), PROVED and numerically checked |
| Lemma 1.5 (base flatness) | PROVED | CORRECT | = Part I lem:flat at an NA normer |
| "Non-recovery <=> uniform witness in a fixed finite-dimensional space" | PROVED | CORRECT (with F1) | the witness is the full envelope r~_{f'}, not only single pieces |
| Lemma 2.1 (T_PB admissible, Lemma B only) | PROVED | CORRECT for one block; parenthetical for N >= 2 WRONG (fix F3) | literally equal vectors in all blocks violate (T-b); corrected operator with block-private signatures in ref_notes 3 |
| T_PB features (dominant carrier, two staircases (h -+ 8 Phi(k) e_0)/n, generic carriers on dense targets, private tails <= 2^{-k}Phi(k)^2, no banks/levers, no generic weights) | - | ACCURATE | private resources move a value by <= delta_k/8 << Phi(k) |
| Lemma 2.2 (forced data of f and all f_N) | PROVED | CORRECT | numerically M = 0.7999, threshold 0.80 (bound 2), staircase values -+3.99945 Phi(k), Q(f) empty; generic carriers become strict non-peaks at f_N (harmless) |
| Prop. 2.3 (gamma h in C(f) and C(f_N), all N >= 3, gamma_0 = 5e-5, bound 1 + 0.32 t^2) | PROVED | CORRECT | every step re-derived; exact decompositions checked to 60 digits: (bound - 1)/t^2 <= 1.3e-4 at gamma_0 and <= 0.1174 at maximal content |
| Thm 2.4 (S(f) = {0}, K(f) = {0}, (MS) fails, recovery by f_N, switching at all scales at NA rows) | PROVED | CORRECT, precision P-c | at f_N, S(f_N) != {0} in general; the right reason is gamma h not in l_1(F) + Y (referee Lemma R2) |
| Remark 2.5(4) ("finest scales need one two-sided linear representation" is false for mates) | PROVED | CORRECT | refutes E's Round-1 gloss (never used later as a theorem); precise form = Lemma R2 |
| Remark 2.5(5) (Lemma S / Thm NL constrain only mates with exact two-piece data; (MS)-violating approximants escape) | PROVED | factual part CORRECT; methodological conclusion HEURISTIC | shows a non-recovery proof cannot assume two-piece data at all approximants; does not show every f has such approximants |
| N >= 2 with cross-block near-duplicates | SKETCH | PROVED (upgraded) | with the operator of F3, block 1 is the one-block construction; other blocks untouched; constants unchanged; Q_m empty in every block |
| Lemma 3.2 (two-sidedification) | PROVED | CORRECT | needs the EXACT condition v^near(zhat) = 0 with the split at the truncation level; diagonal U |
| Lemma 3.3 (near free coordinates stay free) | PROVED | CORRECT | any convergent sequence |
| Lemma 3.4 (base switching at NA rows) | PROVED | CORRECT | G3 Lemma 1.4(c) at the NA normer; holds for B_+ and B_- separately |
| Principle 3.1 | HEURISTIC (PROVED for T_PB) | (a) CORRECT; "PROVED for T_PB" overstated (O2); (c) HEURISTIC | only the mates gamma h of the row f are proved inherited |
| Consequence 3.5, Design (B), Design (A), assessment 3.4/3.6 | HEURISTIC/SKETCH/OPEN | correctly labelled; one error C-B1 | Design (B)(i) uses l_inf where l_1 is relevant and draws the wrong conclusion ("adversary must spread"): restoration of infinitely many pairs is impossible whenever sup ||phi_p||_1 < inf |
| "Canonical truncations recover everything" (Sec. 0, 3.5) | - | OVERSTATED (O1) | proved only for [-gamma_0, gamma_0] h; C(f) not determined; f in Rec OPEN |

## B. Required fixes (all proved in N2_ref_notes.md)
 F1  Remark 1.3: replace the citation by the single-mate Blaschke/support-function argument (ref_notes 1).
 F2  Lemma 1.4 reading: delete the per-carrier gloss; state Lemma 1.4' (orthogonal projection, denominator sigma' + t w'(eta)) and
     Lemma 1.4'' (balanced: relevant carriers plus a balancing term (|kappa|/M')||D(w' 1_{N \ A_0})||).  Any future non-recovery
     argument must use these (or lem:localformula); the per-carrier reading underestimates the excess and would give invalid witnesses.
 F3  Lemma 2.1 parenthetical: use block-private signatures S_{k,m}, generic weights 2^{-l(k,m)^2}, allowedness relative to all S_{k',m'}.
 P-c Theorem 2.4(c) at f_N: cite (T-c)/Lemma R2 instead of S(f_N) = {0}.
 O1  Weaken "recover everything" to the segment [-gamma_0, gamma_0] h; state f in Rec as OPEN.
 O2  "Principle 3.1 PROVED for T_PB" -> "proved for the mates gamma h of the row f of Section 2".
 C-B1 Design (B)(i): l_1 instead of l_inf; restoration of infinitely many pairs is impossible for bounded far l_1-mass, whatever the
     spreading.  C-B2: far errors of linearly used (converted) pairs must be banked on support coordinates, not on contacts.

## C. Referee additions (PROVED, ref_notes 4-6)
 * LEMMA R2 (unbounded block parts): at a row with F' cup K' finite and free room bounded below (every NA row), a mate g not in
   l_1(F' cup K') + Y has ||Theta_+-(t)||_{V*} -> infinity in EVERY family of decompositions; in particular finitely supported mates off
   F' cup K' of NA rows are carried only by scale-dependent decompositions with unbounded block parts -- and N2's example shows that
   such mates exist at NA rows.
 * PUSH CALCULUS: for g = B + L*(omega - d w): (L*(omega - d w))(zhat) = sum_{k in P} omega(k) s_k lambda_k mu^_k;
   N(w + t(omega - d w)) <= 1 + t^2||D omega||^2/(2(C + tdM)) under inward/no-overshoot pushes (NO margin needed); q*(a + tB) >= 1 +
   t g(zhat) - t sum_P omega(k) s_k lambda_k mu^_k.  So pushes on peaks cost exactly their lambda-weighted margins at first order (strict
   non-peaks are free), at ANY row; this is the mechanism of inheritance.
 * N >= 2 version of Section 2: PROVED with unchanged constants.

## D. On the strategic question ("approach it negatively?")
N2's answer -- the negative route is not easier, nothing points to a counterexample, leaning positive -- is consistent with
everything checked here, but it is a JUDGEMENT, not a theorem (N2 says so).  What the checked mathematics does establish:
 (1) One-sided switching through peak staircases at all scales, with no contacts and no strict non-peaks (K(f) = {0}), is
     inherited by the canonical truncations: such f are not counterexamples.  By the push calculus the cost of this mechanism does
     not depend on whether the row attains its norm; only the signs/margins of the pushed carriers matter.
 (2) Hence a counterexample needs staircases whose sign/margin data depend on infinitely many coordinates in a way that no
     z' in c_0 reproduces (cancellation designs with bounded far l_1-mass, C-B1), no alternative staircase in the mate direction (a
     rate condition on the dense family), and robustness against crossing conversions (E's rigid design) -- or base resonances
     through infinitely many contacts with Delta d < 0 and no (SC), or infinite F.
 (3) A non-recovery proof needs a uniform witness over ALL NA approximants in a fixed finite-dimensional test space (F1), with upper
     bounds on r~_{f'} from Lemma 1.4''/lem:localformula.  No technique for such uniform bounds exists in the sources.
Recommendation: do not switch the main effort to the negative side; keep N2's next step 1 (finite transition-cell computation for a
cancellation design with E's rigid structure and (LIN)) as a cheap falsification test of the positive conjecture.

## E. Single most valuable idea
Inheritance by norm-attaining rows: mates carried at scale t by inward pushes of size ~1/t on peaks of depth ~t cost only the
lambda-weighted margins of the pushed peaks (push calculus), at attaining and non-attaining rows alike; so one-sided switching
whose sign/margin data are decided on finitely many coordinates passes to the canonical truncations at ALL scales (N2's example,
PROVED), while NA rows can carry finitely supported mates only through such unbounded scale-dependent decompositions (Lemma R2).
The adversary must therefore make the sign-determining data of the staircases non-reproducible by any z' in c_0, and the prover
of non-recovery must beat every approximant with one finite-dimensional witness.

## F. Precisely open
 1. Non-recovery of any (f, rho g), any admissible T, any n: OPEN (no candidate with a proof strategy).
 2. For T_PB, f: determine C(f) (is it [-gamma_max, gamma_max] h?) and decide f in Rec (C(f) contained in Li C(f_N)?).
 3. General inheritance theorem (F finite, room bounded below, pushed carriers with signs/margins preserved up to o(depth) at f_N,
    e.g. uniform relative tails): control of (M, C, threshold) changes, free-coordinate base parts and the g(zhat_N) correction.
 4. Cancellation designs with bounded far l_1-mass + (LIN) + rigid design: neither recovery (crossing conversions are HEURISTIC)
    nor non-recovery is proved; the finite transition-cell excess is not computed.
 5. Base resonances with Delta d < 0 without (SC) for rho -> 1; infinite F ((LSC-trunc)); and, for the positive program, the residual
    of ADDENDA 13-14, which N2's example does not touch.
