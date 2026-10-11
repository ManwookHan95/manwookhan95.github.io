# Referee report on N3 ("Uniform non-lower-semicontinuity: from Theorem NL to all approximants")

Files checked: neg/N3_notes.md (whole), N3_part1-3.md, N3_work/*.py; Part I (lem:bookkeeping, lem:base, lem:threshold,
eq:margin, def:certificate, lem:slack, def:tame, thm:tamefibre, prop:lowerbound, rem:onesided, prop:exact,
cor:twosided, def:twopiece, def:engineered, lem:approxfacts, thm:engineered, prop:continuity, prop:approximants);
Part II (lem:II-sandwich, cor:II-S1, cor:II-S2, prop:II-S3, thm:II-NL, rem:II-NL); N1 referee (Lemma 1.4, P-1b).
Referee parts: neg/N3_ref_part1-3.md; proofs of all fixes and additions: neg/N3_ref_notes.md; scripts: neg/N3_ref_work/.

## 요약 (Korean)
N3의 기본 도구들(스위칭 예산, de-switching, 깊은 carrier로의 이동, 은행 용량, 집단 운동 보조정리, 양의 스케일 프로파일
경계 정리 2.3, 상속 따름정리 2.5, 은행-de-switching 부등식)은 모두 다시 유도했고 옳다.  그러나 중대한 결함이 두 가지
있다.  (1) "정확한 가시성"(H = 0)은 어떤 admissible T에서도 불가능하다 (Lemma B의 꼬리 조밀성 때문에 모든 좌표는 무한히
많은 carrier가 보며, α ≥ α_0인 peak는 유한개뿐).  따라서 따름정리 2.4, 2.8, 정리 2.6(a)·3.1(iii)의 정확한 가시성 부분,
그리고 "sqrt(mu) 법칙"은 공허하다 (수치 모형은 유한 모형이라 H = 0이 가능했을 뿐).  (2) 정리 2.3은 NL의 메커니즘이 아니다.
NL은 C-tame/(BT) 행에서 모든 peak가 -d psi 하나로 묶이는 "정확한" 잠금이고, 정리 2.3은 약한 peak를 H에 넣는 양의 스케일
부등식이다.  고정된 임계값의 양의 스케일 부등식은 실제로 언제나 상속된다 (심사자가 margin 형태 정리 2.3'과 Fatou 보조정리로
일반화하여 증명).  하지만 정확한 메커니즘은 상속되지 않으며, 정리 2.6(b)의 근사열(고정된 S에만 은행)은 S 밖의 진동쌍에서
정확한 메커니즘에 의해 막힐 수 있다.  특히 f의 자유좌표에는 은행도 접촉도 놓을 수 없으므로(가까운 행에서 z'_j -> z_j),
N3의 "aligned or banked" 이분법에는 세 번째 선택지 "strict non-peak로 덮기"가 빠져 있고, 자유좌표에서는 그것이 유일한 탈출로다.
결론: "NL의 균일화는 실패한다"는 접촉/지지 좌표와 양의 스케일 함수에 대해서만 증명되었다.  negative 접근이 남길 곳은
접촉에서의 junction(문제 3.4)보다 더 날카로운 "자유좌표 진동 + 작은 margin peak" 문제(문제 R)이다.  판단: N3와 마찬가지로
반례의 증거는 없고, 양쪽 모두 같은 핵심(약한 peak를 통한 근사 공명)에서 막혀 있다.

## Overall verdict
Part 1 (switching budget, de-switching, migration, rigidity at C-tame NA rows, bank capacity): CORRECT, minor precisions.
Part 2: Lemma 2.2, Theorem 2.3, Corollary 2.5, Theorem 2.6(a) (general form), (b1), (b2) as literally stated: CORRECT.
Corollary 2.4 and every exact-visibility clause: VACUOUS (exact visibility is impossible for admissible T) — Cor 2.4 is
WRONG as the claimed strengthening of [II, cor:II-S1].  The identification "NL mechanism = Theorem 2.3" and the headline
"uniformizing NL fails, provably at the level of the mechanism" are OVERSTATED: proved only for fixed-threshold
positive-scale sandwiches and a fixed set S of contacts.  Part 3: identities correct; the "saturation/sharpness"
consequence is unsupported (it compares with vacuous corollaries); Prop 3.3's conclusion is heuristic.

## Verdicts by claim
| Claim | Verdict | Main issue / fix |
|---|---|---|
| Lemma 1.2 | correct | holds for any e-feasible pair (not only optimal ones) |
| Theorem 1.4 | correct | supplement: omega attained, left-continuous in M (ref notes §1) |
| Corollary 1.5 | correct (gloss) | "weights comparable to or below the scale" should read: used weight outside Lambda >= c(Lambda) t/5 |
| Proposition 1.7 | correct | (d) is a property of the sufficient radius, not a constraint on mates |
| Proposition 1.8 | correct (fixable) | needs F finite for min_F|a_j| > 0; banks impossible at free coordinates of f |
| Lemma 2.2 | correct | weighted form lambda_k eps_k <= t/(2 mu_k): margin, not alpha, is the right classifier |
| Theorem 2.3 | correct | floor 2(15AH)^{1/2} > 0 is intrinsic; lossy (low-weight robust-margin peaks counted in H); Theorem 2.3' |
| Corollary 2.4 | wrong (vacuous) | exact visibility impossible (Lemma R-V); correct replacement Cor 2.4' (rate hypothesis) |
| Corollary 2.5 | correct | inheritance holds for Theorem 2.3-type bounds only; extends to all fixed-threshold floors (Lemma R-F) |
| Theorem 2.6(a) | correct with fixable gaps | exact-visibility form vacuous; replaced by kappa-clean form 2.6(a') |
| Theorem 2.6(b) | correct with fixable gaps (literal) | not a statement about NL's exact mechanism; fixed S insufficient (Prop X(a)); free coords (Prop X(b)) |
| Theorem 2.7 | correct | holds at every row |
| Corollary 2.8 | wrong (vacuous) | needs H_S = 0; band version 2.8' (180 H_S/kappa' <= t <= kappa'/(8A_S)) |
| Proposition 2.9 | correct | "exact resonance" in support/sign sense |
| Lemma 2.10 | correct | "no escape obstruction" only above sqrt(frak(N)) |
| Theorem 3.1 | correct with fixable gaps | identities right; "de-switching exactly s_1" = construction's switch-over; factor-32 comparison void |
| Proposition 3.2 | correct | banks must sit on contacts of f with sign z_s for z' to stay put |
| Proposition 3.3 | correct (bound) | "compensation must come from one-sided resources" is HEURISTIC ((N1) is not necessary) |

## Major findings
M1 (no exact visibility; PROVED, ref notes §2).  For admissible T every coordinate is seen by infinitely many carriers
(density of every tail in S_{q*}), while at any row at most 1/alpha_0 peaks have alpha >= alpha_0.  So H > 0 always.
Even with margin classification, near-kernel carriers (u_k(theta') ~ 0) seeing Z exist in every tail: H(mu_0) > 0.
N3's numerics (one carrier sees S u {j_f}) are a finite-model artifact.  Our check: one extra low-weight STRICT NON-PEAK
seeing S produces Osc_max = 1.14 sqrt(H) at zero bank mass (three weights, constant ratio); a low-weight PEAK produces
none, for every resolvable margin.

M2 (what NL really uses).  Theorem NL rests on exact data ([II, cor:II-S1/S2], Prop. 1.7): at C-tame/(BT) rows ALL peaks,
however small their alpha, enter only through -d psi.  Theorem 2.3 cannot see this (it treats small-alpha peaks one by
one), hence its permanent floor.  The correct positive-scale counterpart is Theorem 2.3' (margin-classified; low-weight
robust-margin peaks cost only t log(1/t)/mu_0) and Corollary 2.4': at ANY row, every mate is proportional to psi' on Z
as soon as the weighted mass of near-kernel carriers seeing Z is o(mu_0/log^2(1/mu_0)) — the correct strengthening of
Cor S1 (no exact data needed), which N3's Cor 2.4 aimed at.

M3 (inheritance vs non-LSC, sharpened).  Lemma R-F (Fatou): the floor eta_j(mu_0; .) is lower semicontinuous along every
convergent sequence of rows, so every fixed-threshold sandwich is inherited from f — this vindicates and generalizes
N3's Corollary 2.5.  The non-LSC of Theorem NL is the instability of the constancy HYPOTHESES (C-tameness off Sigma', or
the rate of Cor 2.4'), which hold at the approximants with approximant-dependent rates and fail at f.  N3's Theorem 2.6(b)
only shows that Theorem 2.3's bounds are defeated; at C-tame banked truncations the exact mechanism still yields
dist_{p*}(rho g, C(f')) >= (2/3) rho |psi(s3)psi(s4)| |pi_g(s3) - pi_g(s4)| - o(1) for any oscillation pair outside S
(Prop X(a)).  Banking the WHOLE oscillation set in [1, N] (as [I, def:engineered] does) is needed.

M4 (free coordinates; the missing alternative).  A fixed free coordinate j of f (|z_j| < 1) is free at every row near f:
it can be neither banked nor made a contact.  N3's "aligned or banked" omits the third alternative of [II, remark after
prop:II-S3], "covered by the support of a strict non-peak", which at free coordinates is the ONLY escape from the exact
mechanism (Prop X(b)) besides non-C-tame approximants.  Lemma R-W: an oscillation of g between two free coordinates of
f is carried by strict non-peaks or degenerate peaks of f seeing them, or by small-margin peaks violating log^2-margin
sparsity.  In the latter case C-tame approximants lock those peaks; bounded-depth strict non-peaks of approximants come
only from strict non-peaks or degenerate peaks of f.  So N3's sentence "a FIXED free coordinate of f can never produce a
uniform obstruction" is proved only for Theorem 2.3-type bounds.

M5 (Theorem 3.1).  Its comparisons are with Cor 2.8 (vacuous) and Theorem 2.6(a) under exact visibility (vacuous); with
the band version 2.8', the junction scale s_1 -> 0 lies below the band 180 H_S/kappa' (H_S >= H_S(f) - o(1) by Lemma
R-F), so no necessary condition applies there.  "The conditions are sharp, not lossy, since the recovering construction
saturates them" is not established; what is supported is the sqrt-scaling of the strict non-peak floor.

## Required fixes (all proofs in N3_ref_notes.md)
F1  Delete Corollary 2.4 or replace it by Corollary 2.4' (§3).  Remove "exact visibility" from Theorem 2.6(a), Cor 2.8,
    Theorem 3.1(iii), the Fact in (b2), §0 and §3.3; replace the sqrt(mu) law by Osc <= 2(A(2mu_S + 15H))^{1/2}, H > 0.
F2  Theorem 2.6(a): replace the exact-visibility sentence by Theorem 2.6(a') (kappa-clean coordinates; clean
    coordinates are new and their clean scales tend to 0).
F3  Corollary 2.8 -> Corollary 2.8' (band).  Theorem 3.1(iii): drop "exactly visible" (unused) and the factor-32 sentence.
F4  Restate Theorem 2.6(b) and §0/§3.4(1): "the bounds produced by Theorem 2.3 (fixed S, fixed eps)" — not "the profile
    mechanism" of NL; add Prop X(a) (fixed S is insufficient) and the remark that at NL's own rows non-uniformity is
    already a theorem ([II, thm:II-NL]: (BT) f is in Rec by [I, Cor 7.22]).
F5  Replace "aligned or banked" by "aligned, banked or covered", and add Prop X(b) (free coordinates of f).
F6  Precisions: Cor 1.5 gloss; Prop 1.8 (F finite); Remark 1.6(c) (F subset [1, N]); Prop 3.2 (bank positions); Lemma 2.10
    (scale range); Prop 3.3 and §3.2 ("must" -> heuristic, relative to (N1)); Theorem 3.1(ii) (switch-over scale, not the
    modulus' de-switching scale, which is <~ c' rho V_{>N''} << s_1).

## Assessment of the track question ("should the answer be negative?")
N3 does not provide evidence for non-density, and neither does this review.  What the review adds: (i) every positive-
scale, fixed-threshold profile obstruction is inherited from f (Theorem 2.3' + Lemma R-F) — such functionals can never
certify non-density; (ii) the only non-inherited constancy is exact/rate-based and can be escaped on contacts and support
by banks (engineered approximants do this); (iii) a uniform obstruction of NL type can only live at FREE coordinates of
f, carried by small-margin peaks of f (Lemma R-W), against approximants that must cover those coordinates or retain
near-threshold structure at all small scales (non-C-tame NA rows).  This is the long-standing (O3) core ("approximate
resonances through weak peaks / summable gaps", [I, rem:summablegaps]) localized where banks are unavailable.  A negative
proof would need a capacity LOWER-bound theory for near-kernel carriers at NA rows and must defeat the plausible positive
mechanism of infinitely many near-threshold carriers tuned by far moves (nested tuning), presumably via far rigidity of T.
Leaning: unchanged (no asymmetric evidence); the negative programme should move from contacts (Problem 3.4) to free
coordinates (Problem R).

## What remains open
(1) Problem R (ref notes §7): uncoverable free-coordinate oscillation carried by small-margin peaks — OPEN.  What a
negative proof must establish: the sqrt-weight capacity upper bound for strict non-peaks/degenerate peaks seeing Z (SKETCH
at a fixed row, ref notes §7) UNIFORMLY along every NA sequence, i.e. a uniform margin-sparsity rate near Z that no
approximant can break by tuning deep near-kernel carriers (u_k(x') ~ vartheta' Phi_k) seeing Z; plus control of
non-C-tame NA rows (their existence near a given f is OPEN).  What a positive proof must do: re-create, at NA rows, weak-peak
freedom at the free coordinates (nested tuning of infinitely many near-threshold deep carriers by far moves) at every
scale below the slack scale.
(2) N3 Problem 3.4 (junction certificate on contacts) — OPEN (its (J1) must use Cor 2.8' and the band).
(3) Theorem 2.6(b3) — SKETCH; the margin form (one monotone parameter mu_0) reduces it to a Dini-type argument (ref notes §7,
not written out).
(4) Whether Cor 2.4' holds under plain (MS) instead of the log^2 rate — OPEN (the exact version at C-tame rows is
[I, thm:tamefibre]).
(5) Sharp capacity constant of strict non-peaks (finite model: Osc_max ~ 0.9-1.14 sqrt(lambda |u|), gap-dependent) — HEURISTIC.
