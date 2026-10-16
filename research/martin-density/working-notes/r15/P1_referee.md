# Referee report on P1 (round 15): Problem R, negative side — small-margin peaks at free coordinates

Files checked: r15/P1_notes.md (whole), P1_part0-6, P1_work/*.py; sources N3 notes (Def 1.1, Lemma 1.2, Lemma 2.2, Thm 2.3),
N3 referee report + ref notes (Lemma R-V, W, S, Thm 2.3', R-F, Cor 2.4', R-W, Prop X, Sec. 7), N1 Prop 1.8, G3 Lemma 1.4,
Part I (lem:threshold, eq:margin, prop:forced, lem:dualball, lem:bookkeeping).  Referee parts: r15/P1_ref_part1-4.md;
complete referee notes with all proofs: r15/P1_ref_notes.md; scripts: r15/P1_ref_work/.

## 요약 (Korean)
P1의 엄밀한 도구들은 모두 다시 유도했고 옳다: Lemma SYM(지지집합 밖에서는 mate가 두 블록 부분 사이에 놓인다는 "구간 형태"와
동치), Lemma P(한 척도 형태: 자유좌표에서 블록 부분이 mate 자체를 O(t)로 재현), Theorem C2(l_2 개수 용량 정리), Corollary C3,
Proposition N.  다만 C3의 비고(i)("log^2 비율이 가정을 함축")는 불완전하다: E° 유계성은 Z와 무관한(Z-blind) 조건이다.
심사자는 이를 가정 없는 정리 C3'(Z-국소적 개수 용량)과 이분법 명제 N'으로 대체했다: 회복하는 모든 NA 근사열은 Z를 보는
깊은 near-kernel 구조를 만들어야 한다 — (i) 깊은 strict non-peak들의 l_2 개수 ≥ c (KSB 메커니즘) 또는 (ii) 근사 행 자체의
무한한 small-margin staircase (T_PB/nested tuning).  Cleanliness는 SKETCH가 맞고, 조건부 형태(Lemma CL)는 증명했다; slack 논증은
충분조건(N1 Prop 1.8)을 필요조건처럼 쓴 휴리스틱이다.  수치: P1의 작은 척도(t < 3e-4) 계산은 solver 오차가 e(t)를 넘어서
신뢰할 수 없다(P1의 "절단도 L=8에서 수렴"은 인공물).  잘 조건화된 재정식화로 다시 계산하면: 단순 절단은 전혀 수렴하지 않고,
KSB는 수렴한다.  단, 작은 margin·조밀한 staircase에서는 변환된 carrier 하나만 은행에 넣으면 실패하고(용량 부족), shift가
변환한 band 전체를 은행에 넣어야 한다(필수 수정 K1).  반례 메커니즘은 없고, 판단은 P1과 같이 positive 쪽.

## Overall verdict
All PROVED claims of P1 are correct (Lemma SYM, Cor SYM', Lemma P, Theorem C2, Corollary C3, Proposition N); C3 needs two
precisions and its Remark (i) is incomplete.  The cleanliness SKETCH is honestly labelled; its slack step is heuristic.
The KSB mechanism is sound at model level but must bank the WHOLE converted band; P1's small-scale numerics were
unreliable and are replaced by the referee's well-conditioned re-run, which STRENGTHENS the positive reading (canonical
truncations do not converge at all; banked-band KSB converges in every tested regime).  No negative claim is made by P1,
none is supported, and none is refuted beyond the model level.

## Verdicts by claim
| Claim | Verdict | Main issue / fix |
|---|---|---|
| Lemma SYM | correct | equivalent to (SYM-int): sum_{j notin F'} dist(g'_j,[X+_j,X-_j]) <= e/(c't); plus contact order (ORD) |
| Cor SYM' | correct | holds where the WHOLE block parts agree; general statement is (SYM-int) |
| Lemma P | correct | one-scale form (FREE): sum_{J'} (1-|z'|)|X^s_t - g'| <= e/(c't) is the right statement |
| Theorem C2 | correct | all five steps re-derived; numerics ratio <= 0.24; general partition form C2-gen |
| Corollary C3 | correct with fixable gaps | psi' not identically 0 on Z for "in particular"; E_inf -> liminf E°; "generalizes Cor 2.4'" -> "complements" (C3 needs the Z-blind (H2)) |
| C3 Remark (i) (log^2 rate => hypothesis) | incomplete (SKETCH wrong as stated) | rate implies only the peak-term part (proved, R1); E° bounded is Z-blind; (SIM) suffices (R2); superseded by C3' |
| Proposition N | correct | hypothesis "margin-sparse" contains the Z-blind (H2); superseded by Prop N' (no hypothesis, dichotomy) |
| Cleanliness (5.2) | SKETCH, label right | conditional form = Lemma CL (proved); necessity of symmetric use at small scales OPEN; slack step uses a sufficient condition as if necessary |
| KSB (5.3) recovery in D_anch | HEURISTIC, label right; correction required | bank ALL carriers converted by the shift (K1); one-bank version fails in small-margin dense staircases |
| "a single clean strict non-peak matches the staircase" (2.3 R-ii, 5.4 R2) | wrong (model level) | single carrier lacks capacity at K = 1.5, r = 0.75 (distance plateaus 0.04-0.11); the banked band works |
| D_anch description 2.1 | fixable inconsistency | contact sign: z_{b_k} = -1 for BOTH families with family-dependent F-part (as in part 3/code), not z_{b_k} = -s_k |
| D_anch admissibility, g in C(f) | unproved (not claimed) | Lemma B for D_anch not checked; mate existence model-only |
| P1 numerics (run1-7, mf_run1-2) | unreliable below t ~ 3e-4 | constraint violations up to 10.8 e(t); truncation "convergence" at L = 8 is an artifact |

## Major findings
M1 (C3, Remark (i)).  The hypothesis of C3 has a Z-local part (H1: sum_{P°} m_k|ell_k| -> 0) and a Z-BLIND part (H2: E°
bounded; a cluster of N non-degenerate peaks with Phi in [t,2t] and margin <= t/20 gives E° >= 5 sqrt(N), whatever they
see).  The log^2 rate at Z implies (H1) (proof in notes, R1) but never (H2).  Summable inverse margins (SIM) give both
(dominated convergence, R2).
M2 (referee Theorem C3', PROVED).  Splitting P° at margin mu_0 and moving the small-margin peaks into the counted group
removes every hypothesis:  |Lambda'(g')| <= kappa_2 (C'^2/C'^2_{P°}) ( sum_{N'} ell_k^2 + liminf_{mu_0->0} SM(mu_0) )^{1/2},
SM(mu_0) = sum{ell_k^2 : k in P°, mu'_k < mu_0, Phi_k >= mu_0/polylog(1/mu_0)} (Z-local).  More generally C2 holds for
every partition of the peaks into a collective part P_1 (subset of P°) and a counted part (C2-gen).
M3 (referee Proposition N', PROVED).  For every sequence of rows f'_n -> f with g'_n -> rho g, Lambda(g) != 0, Z in J(f):
for large n either (i) the strict non-peaks/degenerate peaks of f'_n seeing Z have l_2-count >= c_*, or (ii) f'_n has an
infinite family of small-margin peaks seeing Z (liminf SM_n >= c_*).  In Problem R both kinds are deep.  So every
recovering sequence creates deep near-kernel structure at Z, of KSB type (i) or staircase/nested-tuning type (ii); a
negative proof must exclude both at every NA row near f, and (i) is a COUNT condition that weight arguments cannot exclude.
M4 (cleanliness).  Rigorous core: (FREE), (SYM-int), (ORD) at every row and scale; Lemma CL (a carrier used symmetrically
with coefficient bounded below cannot keep an O(1) component on an unbanked escaping coordinate along a recovering
sequence).  Not proved: that deep carriers must be used symmetrically (N3 Thm 1.4 needs bounded coefficients).  The
sentence "the slack cannot absorb the hand-over since t_* >= 6 eta/(1-rho^2)" uses N1 Prop 1.8 (sufficient) as a
necessary condition — heuristic.
M5 (numerics).  P1's formulation (O(1) constraints with slack t^2/2) is ill-conditioned: at t = 5e-5 the solver violates
the norm constraints by 10.8 e(t), so scales below ~3e-4 were effectively unconstrained.  The referee's exact excess
reformulation (P1_ref_work/scaled_model.py; validated against P1 on [8e-3,1], identical optimum 0.162225; independent
verification routine) gives, rho = 0.9:
   one family (run7 setting):  L = 4/6/8: KSB 0.049/0.0070/0.0031, truncation 0.236/0.236/0.233 (P1: 0.275/0.225/0.041);
   two misaligned families:    L = 4/6/8: KSB (band banked) 0.027/0.0039/0.0024, truncation 0.166/0.166/0.166;
   dense, small margins (r = 0.75, K = 1.5): one bank 0.11-0.15 / 0.044-0.096 / 0.042-0.109 / 0.050-0.112 (L = 10/14/18/22,
   no convergence); band banked 0.013-0.021 / 0.006-0.009 / 0.0035-0.0045 (L = 10/14/18); truncation 0.57;
   r = 0.85, K = 1.2: one bank 0.11-0.17, band (7-10 banks) 0.008-0.010, truncation 0.81.
   Destroying the other band carriers makes the one-bank version WORSE: the deficiency is capacity, not
   pollution (0.097-0.149 with them destroyed) — consistent with the count law (M2).  Grid bottoms down to 1e-9 leave the KSB distances unchanged.

## Required fixes (proofs in P1_ref_notes.md)
F1  C3: add "psi' not identically 0 on Z"; E_inf -> liminf E°(t_n); "generalizes" -> "complements" N3-ref Cor 2.4'.
F2  Replace C3 Remark (i) by (R1) + (R2) and the statement that (H2) is Z-blind; better, state Theorem C3' and C2-gen.
F3  Replace Proposition N by Proposition N' (dichotomy (i)/(ii)), or add "(ii) is excluded by the margin-sparsity hypothesis".
F4  Cleanliness 5.2: state (FREE), (SYM-int), (ORD) and Lemma CL as the proved content; mark the necessity of symmetric
    use and the slack sentence as HEURISTIC.
F5  KSB 5.3 (B): bank the contact parts of EVERY carrier converted by the shift (the band), not only k_0; replace "ONE
    clean deep-kernel strict non-peak ... covers all smaller scales" (Sec. 0, 5.3, 5.4) by "the banked band"; delete
    "a single clean strict non-peak already matches the staircase" (2.3 R-ii, 5.4 R2) — false at model level.
F6  D_anch 2.1: contact sign z_{b_k} = -1 for both families, F-part of h family-dependent (as in part 3 and the code).
F7  Replace all P1 model numbers involving scales below ~3e-4 by the referee's re-run (or re-run with the excess form);
    in particular delete "truncations ... until boundary effects" — truncations do not converge.

## Assessment of the track question
Nothing in P1 or in this review is a step toward a counterexample.  The referee's additions sharpen what a negative proof
for Problem R would have to show: at EVERY NA row near f, both alternatives of Prop N' fail — no deep N'-structure with
l_2-count >= c_* that is usable (clean) at the small scales, and no infinite small-margin staircase at Z.  The first is
produced by a single window shift plus banks whenever f's oscillation is carried by a near-duplicate family whose off-J
parts are bankable (contacts or near-contacts; free far parts are forced to be common by (FREE) at f) — HEURISTIC;
in every tested model the banked band has enough count.  Leaning: positive (density more likely), unchanged, low-to-moderate confidence.

## What remains open
(1) KSB recovery as a theorem in ONE explicit admissible design (Lemma B for D_anch; existence of the switching mate g in
    C(f); the junction bookkeeping between the band's coverage scale ~Phi_band and the slack scale ~eps^{1/2}).
(2) Quantitative band-count vs staircase-capacity comparison for general T (P1's "duality"); a negative route remains only
    for designs that decouple the band count from the staircase capacity (e.g. several carriers per scale with
    non-duplicate J-profiles, R3), with no candidate.
(3) Necessity of symmetric use of deep carriers at small scales (de-switching with unbounded coefficients); a two-scale
    cleanliness inequality (O-R4).
(4) Alternative (ii) of Prop N' as a mechanism (non-margin-sparse NA approximants) and its exclusion in a negative proof.
(5) Problem R (negative) and density of NA((c_0, p_N), l_2^2): OPEN.
