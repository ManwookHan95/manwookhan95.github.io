# N3 notes — Can the failure of lower semicontinuity of Theorem NL be made UNIFORM over all norm-attaining approximants?

Track N3 of the negative direction (user question: "이정도로 돌렸는데 증명이 안된다면 negative로 접근해야 하는 거 아닐까").
Sources: Part I (paper/martin_density_note.tex), Part II (paper2/martin_density_note_II.tex: Lemma S, Cor S1/S2, Prop S3,
Theorem NL), Part III (paper3/martin_density_note_III.tex: Theorem UE, E^eng, levers), U3 + U3-referee (r8/), G3 (r14/),
N1 (neg/N1_notes.md).  Part files: neg/N3_part1.md, N3_part2.md, N3_part3.md (reproduced below, authoritative); scripts in
neg/N3_work/.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Every item labelled PROVED has a complete proof below or
is cited from a refereed source.

## 0. Answer and summary

요약 (Korean).  Theorem NL의 비하반연속성을 "모든" norm-attaining 근사열에 대해 균일하게 만드는 것은 불가능하다는 것이
메커니즘 수준에서 증명된다.  (1) NL의 핵심인 프로파일(oscillation) 제약은 사실 모든 행(row)에서 모든 mate에 대해 성립하는
양의 스케일 선형 샌드위치(정리 2.3)이며, 은행(bank) 질량 mu에 대해 Osc <= 2(2A mu)^{1/2} 꼴의 sqrt(mu) 법칙을 준다
(수치적으로 상수 1.22로 5자릿수 범위에서 확인).  (2) 이 제약은 f 자신이 이미 만족하므로 근사열에 "상속"되고(따름정리 2.5),
f의 접촉 구조를 깊이 N까지 복사하고 S에 작은 은행을 두는 근사열이 모든 근방에서 이 메커니즘을 무력화한다(정리 2.6(b);
f의 자유좌표가 유한한 경우 — NL이 실현되는 self-aligned 행 포함 — 완전 증명, 일반적인 경우 SKETCH).  (3) 남는 것은
회복하는 근사열이 반드시 가져야 할 구조(정렬 또는 은행, de-switching, 은행 질량 >~ kappa x de-switching 스케일)이고,
engineered 근사열이 이를 상수배까지 정확히 만족한다(정리 3.1).  (4) 따라서 이 경로의 negative 증명은 de-switching 스케일에서의
"hand-over(접합)"에서만 가능하며, 그것은 일방향 레버에 대한 1차 Farkas 장애 + 원거리 양방향 레버의 약함(명제 3.3)을 요구한다 —
즉 positive 쪽을 막고 있는 "exactness vs one-sidedness"와 정확히 같은 지점이다.  결론: NL을 균일화하는 negative 접근은
실패한다(증명됨); negative로 가려면 hand-over 인증서(문제 3.4)를 겨냥해야 하며, 그런 예는 알려져 있지 않다.  판단: 약하게
positive 쪽(밀도), 낮은 확신.

ANSWER (English).
 (1) Theorem NL cannot be made uniform over all NA approximants: its mechanism (the profile sandwich) is a positive-scale
     LINEAR constraint satisfied by every mate at every row (Theorem 2.3), it is inherited from f (Corollary 2.5), and in every
     neighbourhood of f there are NA rows (truncation of f's contact pattern at a large depth + banks of mass of order the
     visibility weight of the approximant's free coordinates) at which every lower bound it produces is <= o(1)
     (Theorem 2.6(b): PROVED when f has finitely many free coordinates — this covers the self-aligned rows where NL is
     realized — SKETCH in general).
 (2) The uniform content of NL is a sharp NECESSARY STRUCTURE of recovering NA approximants: aligned-or-banked with the
     quantitative threshold mu_S >= kappa^2/(10 A) (Theorem 2.6(a)); de-switching of bounded switching at every NA row
     (Theorem 1.4) and migration of persistent switching to deep carriers (Corollary 1.5); banks >~ kappa x (de-switching
     scale) below the hand-over (Theorem 2.7, Corollary 2.8).  The engineered approximants of [I, thm:engineered] saturate all
     of these up to absolute constants (Theorem 3.1) — positive evidence.
 (3) The only feature of NA approximants that is NOT inherited from f is the hand-over at the de-switching scale.  A
     non-density certificate of this type must be a JUNCTION certificate (Problem 3.4, OPEN): banks move the switching
     carriers' values at first order (Prop. 3.2), far two-sided levers are too weak by the factor s_1/lambda (Prop. 3.3), so a
     certificate needs a Farkas obstruction against the one-sided resources at moderate depth plus far rigidity of T.  This
     is exactly the consensus core "exactness versus one-sidedness", now localized; no example is known.
 Leaning: POSITIVE (density more likely), low confidence for arbitrary admissible T.  The negative approach via
 uniformizing NL is closed; a negative programme should target Problem 3.4 with an adversarial T (non-diagonal U, far-rigid
 tails, maximal-contact rows, deep switching), not profile functionals.

| # | Result | Status | Where |
|---|---|---|---|
| 1 | Switching budget at every row (scale-t pairs) | PROVED (= G3 L1.4) | Lemma 1.2 |
| 2 | De-switching at rows with F u K finite (all NA rows), modulus omega_f | PROVED | Thm 1.4 |
| 3 | Persistent switching at NA rows migrates to deep carriers | PROVED | Cor 1.5 |
| 4 | Infinitesimal rigidity and profile constancy at C-tame NA rows (NL mechanism) | PROVED (cited) | Prop 1.7 |
| 5 | Banks are contact-like above their capacity scale | PROVED | Prop 1.8 |
| 6 | Collective motion of weighted peaks at every scale | PROVED (+numerics) | Lemma 2.2 |
| 7 | Positive-scale profile bound at every row; sqrt(mu) law | PROVED (+numerics) | Thm 2.3, Cor 2.4 |
| 8 | Cor S1 without two-piece data (exact visibility) | PROVED | Cor 2.4 |
| 9 | Uniform lower bound is inherited from f | PROVED | Cor 2.5 |
| 10 | Aligned-or-banked necessary condition (quantitative) | PROVED | Thm 2.6(a) |
| 11 | Mechanism defeated by truncation + banks | PROVED (J(f) finite) / SKETCH (general) | Thm 2.6(b) |
| 12 | Bank–de-switching inequality and dichotomy | PROVED | Thm 2.7, Cor 2.8 |
| 13 | Persistent bounded switching at f is an exact resonance | PROVED | Prop 2.9 |
| 14 | Tail control of switching extent (no escape obstruction) | PROVED | Lemma 2.10 |
| 15 | Engineered approximants saturate all necessary conditions | PROVED | Thm 3.1 |
| 16 | Banks move carrier values at first order | PROVED | Prop 3.2 |
| 17 | Junction mismatch s_1/t^2, scale invariant | HEURISTIC (U3-ref F6, numerics there) | 3.2 |
| 18 | Far free levers too weak under the cut-off (N1) | PROVED | Prop 3.3 |
| 19 | Junction certificate (J1)-(J4) for some admissible T | OPEN | Problem 3.4 |
| 20 | Uniform NL-type non-density certificate | FALSE as a mechanism (rows with J(f) finite); SKETCH in general | Thm 2.6 |

## Next steps (for a negative programme)
 1. Problem 3.4 at the simplest configuration: one block, maximal contact (J(f) = empty off F), a mate with S-oscillation
    carried by persistent deep switching, non-diagonal U so that banks on S move all coarse carriers' values; compute the
    cone of first-order corrections generated by banks (signs z_j), inward contact moves and pulls, and test whether the
    junction correction can lie outside it (finite LP at a fixed window; this is checkable numerically).
 2. Far rigidity: construct admissible T whose carriers' tails beyond any depth are nearly collinear within groups
    (N2 (round 2) SKETCH) and quantify the far-lever strength against Prop. 3.3.
 3. Complete Theorem 2.6(b3) (uniform inheritance over growing sets of free coordinates) to close the uniform-NL question for
    all rows.
 4. Positive side: Theorem 3.1 shows the necessary conditions are exactly the ones Part III's d-consistent approximants are
    built to satisfy; the hand-over analysis (Props. 3.2-3.3) says the levers must act at moderate depth, which is where the
    designed T_fin places them — a design-free version would need a lever lemma using inward contact moves AND banks with both
    contact signs (two contacts of opposite alignment), which is the natural target.

---
