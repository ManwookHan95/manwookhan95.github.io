# Referee report on P1 (round 15), second independent pass: Problem R, negative side — small-margin peaks at free coordinates

Files checked: r15/P1_notes.md (whole), P1_part0-6, P1_work/*.py; sources: BRIEFING_R2 (Addenda 13, 14a/b, NEG), N3 notes
(Def 1.1, Lemma 1.2, Thm 1.4, Prop 1.7, Prop 1.8, Lemma 2.2, Thm 2.3) and N3 referee notes (Lemma R-V, W, S, Thm 2.3', R-F,
Cor 2.4', R-W, Prop X), N1 Prop 1.8, N2 Lemma 2.1 / Prop 2.3, Part I (def:admissible, lem:threshold, eq:margin, prop:forced,
prop:approximants, prop:continuity, def:certificate, lem:block, def:tame, thm:tamefibre, prop:lowerbound, lem:bookkeeping).
A first referee pass exists (11 Oct); it is preserved unchanged in r15/P1_ref_prev/ and is compared in notes part 4.
Notes with all proofs: r15/P1_ref_notes.md (parts P1_ref_part0-4.md).  Scripts: r15/P1_ref_work/rb_*.py (outputs rb_outputs.txt).

## 요약 (Korean)
P1의 엄밀한 도구는 모두 독립적으로 다시 유도했고 옳다: Lemma SYM(구간 형태와 동치), Cor SYM', Lemma P(한 척도 (FREE)의 따름정리),
Theorem C2(l_2 개수 용량, 다섯 단계 모두 확인, 독립 수치 모형에서 비율 <= 0.134), Corollary C3(정밀화 두 가지), Proposition N(가정 하에서).
C3 비고 (i)의 SKETCH는 틀렸다: E° 유계성은 Z와 무관한 조건이며 모든 t -> 0에서 깨질 수 있다(마진 Phi^3 예).
새 결과(PROVED, Part I의 thm:tamefibre + prop:lowerbound에서): C-tame NA 행에서는 모든 mate가 유한 certificate이므로 P1의
"cleanliness"는 항등식이 되고(가정 없이), 개수 용량은 날카로운 상수 (C'/sigma')^{1/2}를 갖는다(Theorem C2-T, Cor CL-T).
따라서 열린 부분은 (a) 접합(junction) 척도에서 band certificate의 유효성과 (b) C-tame이 아닌 근사행뿐이다.
KSB: 첫 심판의 "band 전체를 은행에 넣어라"(K1)는 nA = 30에서 재현되나 nA = 20에서는 은행 하나로 충분하다. 실패는 용량 부족이
아니라(한 carrier의 2차 용량이 목표를 초과, 비율 0.68) 접합 창 [1e-3, 5e-3]에 국한된다. 반례 메커니즘은 없고, 판단은 positive 쪽.

## Overall verdict
P1 makes no negative (non-recovery) claim and none is supported.  Every PROVED claim is correct (Lemma SYM, SYM', Lemma P,
Theorem C2, Corollary C3, Proposition N); C3 needs two cosmetic precisions and its Remark (i) is wrong as stated; the
cleanliness SKETCH is honestly labelled, and this pass proves it EXACTLY at C-tame norm-attaining rows.  The KSB mechanism is
sound at model level with the first pass's correction (bank the whole converted band); its failure mode with one bank is a
junction effect, which is precisely the hand-over residue isolated by N3 and P1.  No admissible T is asserted; D_anch's
admissibility (routine) and g in C(f) (model-only) are unproved.  Leaning: positive (density more likely), low-to-moderate.

## Verdicts by claim
| Claim | Verdict | Main issue / fix |
|---|---|---|
| Lemma SYM | correct | equivalent to (SYM-int): sum_{j notin F'} dist(g'_j, conv{X+_j, X-_j}) <= e/(c't); bounds only the MIN of the two usages |
| Cor SYM' | correct | valid where the WHOLE block parts of the two sides agree; general form (SYM-int) |
| Lemma P | correct | one-scale form (FREE) sum_{J'} r_j |X^s_t(j) - g'_j| <= e/(c't) is the statement to use |
| Theorem C2 | correct | all steps re-derived; Step-4 factor may be improved to min{C'^2/C'^2_{P°}, (1 + C'^2/C'^2_{P°})^{1/2}}; numerics ratio <= 0.134 |
| Corollary C3 | correct with fixable gaps | add psi'|_Z != 0; E_inf -> liminf E°(t_n); "generalizes N3-ref Cor 2.4'" -> "complements" |
| C3 Remark (i) | wrong as stated | log^2 rate at Z gives only (H1); (H2) "E° bounded" is Z-blind and fails along every t -> 0 when mu'_k = Phi_k^3 at all depths |
| Proposition N | correct (under its hypothesis) | hypothesis includes the Z-blind (H2); use first pass's Prop N' (re-derived, correct) |
| Cleanliness (SKETCH) | SKETCH label right; core PROVED in two cases | exact at C-tame NA rows (new Cor CL-T); under symmetric use (Lemma CL); "O(t_k)" precision HEURISTIC, rigorous O(t) + O(Phi_B/t) i.e. O(Phi^{1/2}); slack sentence HEURISTIC and unnecessary |
| KSB recovery (5.3) | HEURISTIC (model), label right | bank every converted carrier (first pass, confirmed at nA = 30, not needed at nA = 20); one-bank failure is a junction effect; bank contact-oscillation set if g/psi is non-constant on kept contacts |
| "single clean strict non-peak matches the staircase" | false at model level (deep small-margin regime) | reason: junction coverage, not capacity |
| D_anch admissibility / g in C(f) | unproved (not claimed) | admissibility = routine adaptation of N2 Lemma 2.1 (SKETCH); g in C(f) model-only |

## Major findings
M1 (C2 and the count law are right).  Independent re-derivation of all five steps; the only inputs are N3 Lemma 1.2 and
Lemma 2.2, [I, eq:margin], [I, lem:bookkeeping(c)], ||Phi||_2^2 <= 1/12.  Independent numerics (new random model with strict
non-peaks, small-margin peaks and a contact, 3 seeds, 26 scales): C2 ratio <= 0.134, Lemma 1.2 budgets <= 0.987 (nearly
attained), SYM <= 0.505.
M2 (Remark (i) of C3).  The hypothesis has a Z-local part (H1) and a Z-blind part (H2).  Explicit failure of (H2): peaks at all
depths with margins mu'_k = Phi_k^3 give a term ~ 1/(4t) at t ~ Phi_k^2, and the windows (2Phi_k^3, 5Phi_k) cover (0, t_0), so
E°(t) -> infinity along every t -> 0, whatever these peaks see.  The log^2 rate at Z implies (H1) only.  The first pass's
hypothesis-free C3' (re-derived) is the right replacement.
M3 (NEW, PROVED: Theorem C2-T and Corollary CL-T).  At an NA row f' with C-tame normer and no degenerate peaks, Part I
thm:tamefibre and prop:lowerbound give, for every mate g' = b' + R*(omega' - d'w'):
   g' = sum_{k in Q'} Phi_k omega'(k) u_k - d' psi'  off F'  (exact cleanliness);
   ||D omega'||_2^2 <= C'/(sigma'(1 - a')), a' = ||Dw' 1_{Q'}||^2/C'^2  (so |d'| is bounded);
   |Lambda'(g')| <= (C'/(sigma'(1 - a')))^{1/2} (sum_{k in Q'} ell_k^2)^{1/2}  (sharp count capacity, no (H1)/(H2)).
Along C-tame recovering sequences the used strict non-peaks must reproduce rho g + d psi off F'_n in l_1 with bounded
D-coefficients; any O(1) component of a used carrier on an escaping unbanked coordinate is forbidden.  So P1's cleanliness is
an IDENTITY at C-tame approximants (no symmetric-use assumption, no hand-over or slack argument); the open part of
cleanliness lives only at non-C-tame NA rows (alternative (ii) of Prop N').
M4 (junction precision).  Rigorous form of "J'-profile reproduced by larger-scale carriers": at every scale t the carriers
other than a deep set B reproduce g' on J' up to room-weighted t/(2c') + (2.5/t) sum_{k in B} Phi_k ||u_k 1_{J'}||_1, i.e.
O(Phi_B^{1/2}) at best — weaker (more favourable to approximants) than P1's O(Phi).
M5 (KSB in the models).  (a) Faithfulness: the KSB optimum (run7 setting) needs NO switching below ~5e-3 ~ Phi_band
(minimal ||B+ - B-||_1 from 1e-9 down to 5e-14) and switching ~0.15-0.2 above 2e-2: the small-scale behaviour is
certificate-like, as genuine NA rows require (N3 Thm 1.4), so the model is not exploiting finite-dimensional persistent
switching (its staircase coordinate with beta_k ∝ -s_k Phi_k plus the contact signs exclude zero-J' contact-compatible
combinations).  (b) The first pass's one-bank failure is reproduced at nA = 30 (0.0442 / 0.0964 vs bank-all 0.0078 / 0.0062)
and absent at nA = 20 (0.0086 vs 0.0079).  (c) It is not a capacity deficiency: the C2-T capacity of the single banked carrier
exceeds the target (ratio 0.68), and its small-scale window [5e-6, 1e-3] and large-scale window [5e-3, 2] are fine (0.0082,
0.0069); the failure appears only when the junction window [1e-3, 5e-3] is imposed (0.0189-0.0422).  Banking the shallower
converted carrier closes the gap (0.0078 on every window).
M6 (contact oscillation).  At C-tame KSB rows, g' = -d'psi' (+ used strict non-peaks) on unbanked kept contacts, so if
pi_g = g/psi is non-constant on the kept contacts of f, KSB must also bank the contact-oscillation set inside the window
(engineered approximants, N3-ref Prop X(a)).  In the anchored model g_f vanishes on the contacts, so this is invisible there.

## Required fixes
F1  C3: add "psi'|_Z != 0" to the "in particular"; replace E_inf by liminf E°(t_n); "generalizes" -> "complements" Cor 2.4'.
F2  C3 Remark (i): state that the log^2 rate implies (H1) only and that (H2) is Z-blind (with the mu'_k = Phi_k^3 example);
    or replace C3 by C3' (first pass) — and, at C-tame rows, by Theorem C2-T.
F3  Prop N: rename the hypothesis "(H1) at Z plus uniformly bounded E°", or replace by Prop N'.
F4  Cleanliness 5.2: record Cor CL-T (exact at C-tame NA rows) and Lemma CL (symmetric use) as the PROVED content; replace
    "up to O(t_k)" by the rigorous O(t) + O(Phi_B/t) (M4); mark the slack sentence HEURISTIC (it is also unnecessary).
F5  KSB 5.3: bank every carrier converted by the shift, and the contact-oscillation set if g/psi is non-constant on kept
    contacts; replace "ONE clean deep-kernel strict non-peak ... covers all smaller scales" and "a single clean strict
    non-peak already matches the staircase" by "the banked band covers the junction" (explanation: junction coverage,
    M5(c); not capacity).
F6  D_anch 2.1: use the sign convention of part 3 and the code (all contacts z_{b_k} = -1, family-dependent F-part).
F7  Replace P1's numbers from scales below ~3e-4 by the first pass's well-conditioned re-run (truncations do not converge).

## Assessment of the track question
Nothing in P1 or in either referee pass is a step toward a counterexample.  With M3 the negative target becomes sharper: at
C-tame approximants every mate is an explicit certificate on finitely many clean strict non-peaks, so a non-recovery proof
must show that NO such certificate is valid across the junction for ANY junction depth, shift lever and bank choice, and
must separately defeat all non-C-tame approximants (which only add freedom).  KSB supplies such certificates in every
tested model once the converted band is banked.  The decisive object is the junction window between the coverage scale of
the clean deep carriers and the lowest scale at which the kept structure works — the same hand-over residue as in N3 and
G1-G3.  Leaning: positive, low-to-moderate confidence.

## Most valuable idea
Capacity is a COUNT, not a weight (P1's Theorem C2), and at C-tame norm-attaining approximants it is EXACT: every mate is a
finite certificate whose Z-oscillation is carried by finitely many clean strict non-peaks with the sharp constant
(C'/sigma')^{1/2} (Theorem C2-T).  Hence Problem R is not a capacity problem but a JUNCTION problem: the only thing that can
fail is the validity of the band certificate on the window of scales between its coverage and the kept staircase — which is
where the one-bank models fail and the banked-band models succeed.

## What remains open
(1) Problem R (negative): OPEN; no candidate mechanism.
(2) KSB as a theorem in one explicit admissible design: Lemma B for D_anch (routine); g in C(f) with explicit constants;
    C-tameness of the KSB rows; the junction validity of the banked-band certificate (the only genuinely new step);
    contact-oscillation banks if needed.
(3) Cleanliness and de-switching at NON-C-tame NA rows (unbounded coefficients; alternative (ii) of Prop N').
(4) A quantitative junction comparison for general admissible T (upper bounds C2/C2-T cannot decide it; generic-carrier
    conversions need an approximation RATE of T that an adversarial T can deny, KSB does not).
(5) Density of NA((c_0, p_N), l_2^2) for Martin's renormings: OPEN.
