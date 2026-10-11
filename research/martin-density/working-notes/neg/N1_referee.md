# Referee report on N1 (negative track: shape of a counterexample, certificate of non-density)

Refereed: neg/N1_notes.md (read in full), neg/N1_part1-3.md (identical to the notes up to headers; checked by script),
neg/N1_work/ (both scripts re-run). Checked against: Part I (prop:forced, prop:smooth, prop:continuity, prop:approximants,
prop:reduction, prop:primal, lem:pair, thm:compact, thm:lowerlimit, cor:finite, thm:transitivity, rem:joint, thm:averaging,
cor:ladder, cor:decomposition, prop:intrinsic, thm:transfer, prop:exact, cor:twosided, rem:resonancetypes, def:twopiece,
def:BT, thm:onesided, def:SC, thm:engineered, cor:D1, cor:BTrecovered, rem:withoutSC, end of sec:status); Part II
(thm:II-ERT, thm:II-E, cor:II-S2, prop:II-S3, thm:II-NL, thm:II-N, thm:II-raised, thm:II-flipext, thm:II-transferinf);
G3 Section 2 + G3_referee; N2 (r2) 3.1-3.4; R3_notes 5.1 + R3_referee + R3_ref_part3; U3 summary + U3_referee.
Details: neg/N1_ref_part1.md (Section 1, Lemma 2.1), neg/N1_ref_part2.md (Sections 2-4). Proofs of all fixes and additions:
neg/N1_ref_notes.md. Scripts: neg/N1_ref_work/ref_checks.py, neg/N1_ref_work/rerun_R3_capacity.sh.
Role: adversarial referee, sceptical in both directions.

## 0. Bottom line
N1 claims neither density nor a counterexample, and that bottom line is correct. Every item labelled PROVED in Section 1 and
Lemma 2.1 is correct (re-derived line by line; only precisions). The necessary conditions of Section 2 are correct as
citations, except that one PROVED conclusion is not proved (E-1). One heuristic conclusion of Sections 2.3/3.3 rests on a
claim that the R3 referee refuted (E-2). Both corrections ENLARGE the region where a counterexample could live, compared
with N1's description: exact (scale-free) switching data with negative d-mismatch and failing (SC), and junction-depth-
independent capacity deficits with compact errors, both remain possible. N1's recommendation (no wholesale switch to a
negative programme; a targeted negative test) stands. The target should be re-ranked (Section 4).

## 1. Verdicts on the listed claims

| Claim | Verdict | Notes |
|---|---|---|
| Prop 1.2 (structure of Rec(f), Ob = dist(., Rec(f))) | CORRECT | P-2: cite thm:shifted (valid for all I) for cl Cert^sh(f) subset U(f), not prop:intrinsic(c) (finite-I section). |
| Thm 1.3 (exact non-density criterion) | CORRECT | P-4: (iv) is automatic (graph(Rec) = cl G_NA is closed). |
| Lemma 1.4 (far freedom) | CORRECT, with fixable gaps | Only the "if" direction is proved; the word "exactly" needs the converse, Lemma 1.4' (proved in ref notes Sec 1). P-1b: banks at a FIXED free coordinate are impossible near f; inside the window, support coordinates of a' sit only on F, on contacts with the contact sign, or on near-contacts (Cor 1.4''). "Tiny banks anywhere" holds only beyond the window. |
| Prop 1.5 (local structure of NA) | CORRECT | Re-derived; numerics: exhaustive rank-one search in a Euclidean model gives ratio <= 0.49 of the bound. P-3: the sentence "the ball either meets NA or misses it entirely" is vacuous. |
| Prop 1.5bis (Hahn-Banach form) | CORRECT | Separation is from the FATTENED set N_delta (all mates of nearby NA rows). Separation from NA cap B((f, rho g), delta) alone is a different, weaker property; N1 claims nothing about it. |
| Thm 1.6 (dual formula, Bregman form) | CORRECT | Distance duality + Goldstine + weak*-continuity of phi -> max_C phi on bounded sets; Euler identity; uniqueness of the normer from strict convexity of p**. |
| Cor 1.7 (two-point bound) | CORRECT | Re-derived; author's LP check re-run (LP value <= bound in all cases). |
| Prop 1.8 (scale localization) | CORRECT | Slack inequality checked analytically and on a grid; end-to-end test (2000 cases) clean. |
| Thm 1.9 (convex / non-convex dichotomy) | CORRECT | P-5: labels ">=", "<=" swapped in the proof of (a). P-12: Remark 1.10(II) misidentifies the Part I gap; precise relation in Lemma R-M. |
| Lemma 2.1 (global reformulation) | CORRECT | With R = Omega one must use Omega u NA_1; only the needed inclusion is used. |
| F1-F7, M1-M6, M8 | CORRECT AS CITATIONS, with one unproved conclusion (E-1) and precisions | E-1 (M6 last sentence, M4 gloss, Section 0(2), table). P-6: M2 needs quantifiers "eta tau^2", not "o(tau^2)" at a single scale (Prop R-M2). P-11: F6 quantifier on rho'. M3, M4 can be sharpened to rho g notin K(f), rho^2 kappa_w < 1. |
| M7 (universal switching constraints) | CORRECT | Lemma 1.1, 1.2, Cor 1.3, Lemma 1.4(a),(c), (CL0), (CL2) re-derived; V in L*(V*) subset Y. |
| Sec 2.3 (T2), Sec 3.3(iv), (Q-a) [not on the list] | WRONG (E-2) | They rely on R3's pre-referee claim that error carrying removes the boundary excess for compact errors; the R3 referee's main finding (a rho-independent Hilbert/room capacity gap) is ignored. |
| Sec 3 assessment / verdict | HEURISTIC, reasonable | It needs the E-1 and E-2 corrections. Additional escapes (e5), (e6) for candidate C1. |

## 2. Errors

E-1 (M6, M4 gloss; labelled PROVED). "So the switching of the dangerous mate must be scale-dependent ('approximate
resonance') or not of two-piece type" and "its one-sided decompositions need infinitely many carriers, degenerate or
near-threshold carriers, or flips of an infinite support" do not follow. Exact two-piece data are known to be recovered only
under rho^2 kappa_w < 1 together with (Delta d >= 0 or (SC) on I_-) [I, thm:engineered]. Exact data with Delta d < 0 on
blocks failing (SC) are not covered: rem:withoutSC(b) says explicitly that this case is open. N1's own candidate C1 is
exactly of this kind, so the notes contradict themselves. Correct statement (Prop R-E1, PROVED): for I and F finite, a
dangerous mate either (i) has no two-piece data with rho^2 kappa_w < 1, or (ii) has such data and every such datum has
I_- failing (SC). Only (i) forces scale-dependent or non-two-piece switching. In (ii) the switching vector is exact, nonzero,
finitely carried by g, supported in F u K, z-signed, with infinitely many contacts. There the failure of (BT) enters
through the scrambling of f's blocks, not through g's decomposition.

E-2 (T2, 3.3(iv), (Q-a); labelled HEURISTIC, but it narrows the search wrongly). N1 says error carrying (R3 Thm EC) gives
"R -> 1" for compact error directions. From this it concludes that an obstruction "must ALSO make the errors at every
junction escape to infinity (non-compact)", and it lists E's rigid design among the recovered candidates. The R3 referee
found something different. EC removes only the error-driven conversion requirement. A rho-independent Hilbert/room capacity
requirement remains, and "one converted carrier / one global scalar suffices" is FALSE in general. O3* must be completed by
(R6). I re-ran the referee's Model N scripts (rerun_R3_capacity.sh):
 - One type converted, with EC: R = 1.091 (A = 0.5) and 1.447 (A = 0.25). The maximum is at the bottom scale and is identical
   for tau_gen = 2^6 and 2^8.
 - Coupled real-norm-like model: one shift gives R = 1.0901, two shifts give R = 0.9998.
Corrections:
 - (R1) is not necessary. The residual class is [(R1)-(R5)] OR (R6): bounded conversion capacity of at least one type below
   the room/Hilbert load at every junction, with all errors compact.
 - Delete the "must escape to infinity" sentence.
 - Move E's rigid design to OPEN (SKETCH with two gaps).
 - The Korean summary's "bounded capacity + escaping errors" must be changed accordingly.

## 3. Precisions and referee additions (all proved in N1_ref_notes.md)
 - Lemma 1.4' (two-sided far freedom) and Cor 1.4'' (bank positions): PROVED.
 - Lemma R-I (localization of type (I)): Delta_f := r~_f - h_{Rec(f)} is 2p-Lipschitz. Its positivity set is an open cone that
   meets c_00 and the Mazur set D_f. A type (I) obstruction is an unrecovered X-exposed mate g_x, x in c_00 cap D_f. Near f,
   r~_.(x) <= r~_f(x) - 2 theta on every recoverable row, and >= r~_f(x) - theta on a closed nowhere dense "ridge" through f.
   PROVED.
 - Lemma R-M (merging): "finite merging at f" <=> Rec(f) in A(f). Either implies that Rec(f) is convex, so no type (II), and
   that Rec(f) = C(f) iff Delta_f = 0. [I, cor:finite(a)] at f <=> C(f) in A(f). So the Part I gap "does density force one
   sequence recovering the whole fibre?" is exactly "does density force finite merging?". (II) is one way finite merging can
   fail; it is not that gap itself (P-12). PROVED.
 - Prop R-M2 (precise M2) and Prop R-E1 (corrected M4/M6): PROVED.
 - P-7: (S1) "PROVED (as a reformulation)" overstates a vague sentence. The proved content is Thm 1.3(iii) + Lemma 1.4/1.4'.
   "Cannot be carried by finitely many coordinates" is HEURISTIC: a type (I) test vector may lie in c_00.
 - P-8: U3 recovers only the exact-data mates of the nested-tuning rows. Full recovery for T_fin comes from Master Theorem VI
   (F finite), not from U3.
 - P-10: "for ARBITRARY T ... bottleneck is EXACTNESS" (3.5(2)) describes the designed-T programme. For arbitrary T the open
   core is the Round-2 core (approximate resonances, non-(BT) rows, Delta d < 0 without (SC), Gamma_w > 1, infinite F)
   plus (R6).
 - C1 escapes (HEURISTIC; the identity behind (e5) is PROVED):
   - (e5) The Hilbert footprint U(e' - e^0) of window masses can be cancelled exactly on any finite set of free coordinates by
     O(s_1) moves of z' (and, inward only, on contacts). Only the footprint on supp a' and on outward-needing contacts survives.
     So C1 needs zero-weight carriers with O(1) relative mass on F u K at every depth.
   - (e6) EVERY datum with rho^2 kappa_w < 1 must have Delta d < 0 on a non-(SC) block.
   - (e2') ||U*e_j*|| -> 0 for every compact U, so only the coarse window footprint can be made large.

## 4. Assessment of the question of the track ("should the answer be negative?")
 - What N1 establishes is correct and useful. Non-density is equivalent to an upward jump of the mate graph at an exceptional
   row, relative to NA rows (equivalently, to any recoverable class). It splits into type (I) and type (II):
   - Type (I) is a scalar ridge of f -> r~_f(x) for one x in c_00. It is equivalent to Hahn-Banach separation from the
     fattened local NA set, and it is certified by cheap Bregman decompositions of x at every admissible normer.
   - Type (II) is non-convexity of Rec(f), i.e. a failure of finite merging.
   Nothing in N1, and nothing in the 14 rounds, proves a lower bound for dist(rho g, C(f')) over all NA rows near any f. The only
   lower-bound mechanism known, [II, prop:II-S3], is a type-(I) obstruction with the two-point test vector
   x = psi(s_2) e_{s_1} - psi(s_1) e_{s_2}. It is valid only along rows whose mates carry two-piece data and which avoid
   s_1, s_2, and NA rows escape it with one generic carrier.
 - The corrections E-1 and E-2 do not produce evidence for a counterexample, but they show that N1's "shape of a
   counterexample" was too narrow. Two concrete, refereed-model-level routes remain unexcluded:
   - (R6): a junction-depth-independent capacity deficit. In the coupled models it is removed whenever both types can be
     converted.
   - C1 / case (ii) of R-E1: exact data, Delta d < 0, (SC) failing, plus (e5), (e6).
 - Recommendation (agreeing with N1, re-ranked): do not abandon the positive programme for T_fin (a counterexample there
   needs infinite F and a failure of (LSC-trunc)_N). A targeted negative test for an ADVERSARIAL T should aim at a type (I)
   ridge and should test first:
   - (a) (R6): can an admissible T block two-type conversion at every junction? This is the only place with a
     depth-independent model deficit.
   - (b) C1 in case (ii) of R-E1, with (e5), (e6) addressed.
   Leaning: inconclusive, slightly positive. I see no step of a negative proof in hand. I also see no argument that excludes
   one; N1's leaning is a historical heuristic, not evidence of impossibility.

## 5. Most valuable idea
N1's Theorem 1.9 together with Prop 1.5bis and Thm 1.6. Non-density is either:
 - (I) a scalar ridge: for one x in c_00, limsup over NA rows f' -> f of r~_{f'}(x) is < r~_f(x). Equivalently, an unrecovered
   X-exposed mate, or a convex separation from the fattened local NA set. It is certified purely primally by cheap Bregman
   multi-scale decompositions sum_j (beta_{x'}(y_j)(2p(y_j) - beta_{x'}(y_j)))^{1/2} of that x at every admissible normer x'.
 - (II) a failure of merging (non-convex Rec(f)).
With Lemma R-M, a positive proof splits cleanly into:
 - (P-I) recover the X-exposed mates;
 - (P-II) finite merging, which by itself would also settle the Part I gap.

## 6. What remains open
See N1_ref_notes.md Section 8:
 - existence of a counterexample;
 - types (I) and (II);
 - (P-I) and (P-II);
 - C1;
 - (R6);
 - (N-a) and (N-b);
 - (LSC-trunc)_N for T_fin.

## 7. 요약 (Korean summary)
N1의 정리들(Section 1, Lemma 2.1)은 모두 맞습니다. 비조밀성은 (I) 하나의 방향 x에 대한 스칼라 "능선"(NA 행들에서의 r~(x)의 상극한 < r~_f(x)) 또는 (II) Rec(f)의 비볼록성(병합 실패)과 동치입니다.
다만 두 가지 오류가 있습니다.
 - E-1: "위험한 mate의 switching은 반드시 스케일 의존적"이라는 결론은 증명되지 않았습니다. Δd<0이면서 (SC)가 실패하는 정확한 two-piece 데이터가 남아 있고, 이것이 N1 자신의 후보 C1입니다.
 - E-2: "반례는 무한으로 도망가는 오차가 필요"하다는 주장은 R3 심사의 결론과 다릅니다. 오차가 compact해도 변환용량 결손 (R6)이 남습니다. 모델 재계산으로 R=1.09/1.45를 확인했고, 두 유형을 변환하면 R≈1이 됩니다.
결론: 전면적인 negative 전환은 여전히 근거가 없습니다. 다만 표적형 시험은 (R6) 용량 결손과 C1(case ii)을 우선 대상으로 삼는 것이 맞습니다. 현재로서는 어느 쪽도 결정적이지 않습니다.
