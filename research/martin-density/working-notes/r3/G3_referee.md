# Referee report on G3 (Round 3): "signature-ladder design" and Theorems A, B, C

Referee setting: as in G3. Canonical base q, Martin's norm with a FINITE block set I_N (norms p_N, every N). The operator T is designed
(SLD) and satisfies Lemma B's conclusion. Supporting files: G3_ref_part1.md (parts 1-3 of G3), G3_ref_part2.md (parts 4-5 + numerics),
G3_ref_part3.md (attacks, side results), G3_ref_notes.md (assembly with proofs), scripts in G3ref_work/.

## 0. Bottom line
I re-derived every step of G3 parts 1-5 and tried the attacks listed in the brief. **I found no mathematical error in Theorems A, B or C.**
I found one bookkeeping slip, in the choice of constants in 5.3. It breaks the proof as written for rho close to 1 and has a one-line fix.
I also found some imprecise wording in part 6, which affects none of the theorems.
The main result is correct: for the designed operator T and every N, every mate at every first row in R_0 is recovered, and density
of NA((c_0,p_N), l_2^2) is equivalent to Lemma Z. Lemma Z is correctly labelled OPEN.
This is a real reduction: it removes the open-core items O1-O3 at every f in R_0 (in particular at every base-tame f, whatever its blocks are),
and O4 for several blocks, for this T. It says nothing about Martin's own (unknown) T, and G3 says so.
The reduction from p to the p_N is also valid. I give a short proof of Remark martin-tail below (section 4).

## 1. Verdict table
| Claim | Verdict | Notes |
|---|---|---|
| Thm A (SLD design) | correct | Recursion well founded; density of tails, injectivity and Ran T cap c_00 = {0} (via weight condition (b)), privacy (P1), (P2), (P3) all checked |
| Class R_0 | correct | NA points: a' in c_00, z' in c_0, so N \ J_gamma is finite and each S_l keeps positive mass; base-tame f likewise |
| Two-sided toolkit (2.1-2.5) | correct | Budget, first-order terms, one-sided base bound, Gamma_w <= 1 + o(1), sup-level parametrization all re-derived |
| Signature pinning (3.1-3.5) | correct | Triangular system, Lambda_f <= vartheta^{-l^2} Lambda°, window cut via the box bound and t >= T_lo(l_*) |
| Window certificate (4.1-4.2) | correct | One-sidedness at peaks, at non-peaks beyond the clamp, and at contacts all bounded by two-sided differences |
| Uniform transfer expansion (5.1) | correct | (T1), (T2), the four sup-norm cases, Hilbert part and base step re-derived; c_1 must be small relative to eps_tr * C_min (G3 does this) |
| Windowed averaging (5.2) | correct | Self-contained proof; scalar inequalities verified numerically for all rho; the hypothesis c_1 t^(j) <= rho s_0 is not needed |
| Thm B | correct with a fixable gap | 5.3's margin "sqrt(1+eta_0/2) - 1/100" is impossible for eta_0 < 0.0201 (forced when rho >= ~0.975); use kappa_0 = (sqrt(1+eta_0/2) - 1)/2 |
| No intrinsic defect on R_0 | correct | Immediate from 5.2 |
| Thm C | correct | (<=) Thm B at f'; (=>) rotation argument; NA is contained in R_0 |
| Lemma Z for Round-2 classes | correct (trivial) | Those mates are already in Ls(f) for any admissible T; the result is conditional exactly as the imports are (N2 Thm 3 / N2-ref Thm 3* assume tuning) |
| Thm B with infinite F | correct with fixable gaps (SKETCH) | Plausible. Needs a flip analysis on F, a modified 5.1 with |b_j| <= 2|a_j|/t (b unbounded) and C Thm 7.4 for a not in c_00, b in c_00; see section 5 |

## 2. What I checked, and the key points
* **Pinning (3.2-3.4).** On S_l the only nonzero vectors are u_l's own signature and the targets of finer indices (coarse-to-fine allowedness (a)).
  So -Delta B(s) = Delta c_l delta_l 2^{-s}/n_l + sum_{l'>l} Delta c_{l'} y_{l'}(s)/n_{l'} for s in S_l.
  Base mass on J_gamma costs first order on both sides: sum_{J_gamma}|B_+-| <= t/(2 gamma q_0) (A Lemma 7.1 budget plus E_q >= sum (|tB| -+ z tB)).
  The triangular system is solved from the top window index l_* downwards. Carriers finer than l_* are bounded only by the box bound,
  |c_l| <= 3 lambda_l/t, so their total is <= 6 c_{l_*+1}/t <= 6 t^2. All of this is correct.
* **One-sidedness (4.2(c)).** For every peak (degenerate or weak ones included), sigma omega_+ <= 0 <= sigma omega_-.
  At a non-peak, the + side can move toward the peak level only by (1 - d_+ t) gap/t <= 2 gap/t, and the - side satisfies sigma omega_- >= -2 gap/t.
  So every part of omega_+ beyond the clamp is bounded by |omega_+ - omega_-| <= (|Delta c_k| + lambda_k |Delta d| M)/lambda_k.
  Contacts and near-contacts are covered by ||B_+ 1_{F^c}|| + ||B_- 1_{F^c}|| <= ||Delta B|| + t/q_0. All correct.
* **Gamma_w, not Gamma_max.** The budget bounds exactly q_0 h + sum sigma_m H_m. The transfer peaks of C Thm 7.4 realise the matching
  upper expansion uniformly over certificates with |omega| <= 2 gap/t on gap >= t^2, for |s| <= c_1 t (5.1). Correct.
  Note that ||h|| = O(c_1) here, not o(1), so c_1 must be chosen after eps_tr; G3 does this.
* **Windows and averaging (5.2-5.3).** A single certificate is valid for |s| <= c_1 t (locally) and for |s| >~ K t/(1 - rho^2) (by slack).
  Averaging over n >> K/c_1 dyadic scales of one window fills the gap between these ranges. The averaged certificate is a fixed balanced
  finite certificate with rho g_c in C(f) and Gamma_w(rho c) < 1, and C Thm 7.4 recovers it along the canonical truncations.
  The super-exponential slack 2^{l^3} beats vartheta^{-l^2} and all constants that depend on f, g and rho. Correct.

## 3. Attacks tried (all failed; details in G3_ref_part3.md 3.1)
1. Kink re-splitting, the C-referee finite analogue with Gamma_2 < Gamma_w: the re-splitting amplitude is pinned to O(Lambda_f t), so its second-order gain is O(t^3).
2. Cross-block duplicates: trading coefficients between them is pinned through the disjoint signatures.
3. Weak and degenerate peaks, unbounded internal coefficients (|omega| ~ gap/t, |d_+| ~ 1/t), coarse carriers of tiny weight inside a window,
   fine targets touching coarse signatures: none of these breaks a step.
4. Uniformity in t: the order of choices (eta, t_eta, eps_tr, A_0 = K_b + 1, c_1, t_1, then windows) is consistent.
   No non-attained infimum is used (optimal decompositions exist by weak* compactness).
5. c_0 vs l_inf: z in l_inf, contact sets may be infinite, and C's canonical truncation handles any z.
   F finite is needed only in 2.5 and in the base step of 5.1.
6. Finite-model numerics (CLARABEL SOCP, G3ref_work/test_lemmas.py): the inequality 2.3(b) holds with margin, the pinning inequality 3.2 holds up to
   solver noise (1e-7), and sum|Delta c| = 0.04 t. Finite models are degenerate (p** is not strictly convex, the normer face is 12-dimensional,
   and the mates form only the 3-dimensional certificate space), so this checks signs only.

## 4. Addition: Remark martin-tail is valid (PROVED; one-step tail lift)
Let s_N := sum_{m>N} |R_m .|_m <= eta_N q, with eta_N = (N+2)/2^N. Take S in NA((c_0,p_N),F) with ||S||_{p_N} = 1, attained at x_0.
Choose phi in l_1 with |phi| <= s_N and phi(x_0) = s_N(x_0) (phi = J o L_{>N}).
Then S' := S + (S x_0) (x) phi satisfies ||S' x|| <= p_N(x) + s_N(x) = p(x) and ||S' x_0|| = p(x_0).
So S' attains its p-norm 1, and ||S' - S||_p <= eta_N. Since ||.||_p <= ||.||_{p_N} on operators, density for infinitely many N gives density for p.
Hence G3's setting p_N is enough for the project's question.

## 5. Corrections requested
1. (5.3) Replace "sqrt(1 + eta_Gamma(eta)) <= sqrt(1 + eta_0/2) - 1/100" by "<= sqrt(1 + eta_0/2) - kappa_0" with kappa_0 := (sqrt(1+eta_0/2) - 1)/2.
   Also require K_4 Lambda_f(l) t <= kappa_0. The current text fails for rho >= ~0.975 (checked numerically), and Ls(f) needs every rho < 1.
2. (6.3(b)) "Only these carriers lose their pinning; all others stay pinned" is false as stated. A coarser carrier whose signature set is
   touched by the target of an unpinned carrier becomes slaved to that carrier's free coefficient. The picture in 6.3(d) still stands.
3. (6.3(c)) Make explicit that "will do" means "is an admissible approximant in Lemma Z". Whether such an f' satisfies the mate condition is
   Lemma Z itself. Constructing f' in S_{p*} from prescribed (a', z') is legitimate (G3_ref_part3 3.3), with the lowering placed on far coordinates.
4. (Infinite F sketch) Write out the following, none of which is an obstruction:
   - the flip analysis on F: excess <= |Delta B(j)| + minus-side flip excess, with sum <= t/(4 q_0);
   - 5.1 with (C-a') |b_j| <= 2|a_j|/t and c_1 small;
   - truncation (cost 2t);
   - C Thm 7.4 for a not in c_00, b in c_00 with several blocks.
5. Minor points:
   - the fine d-term in 4.2(c) is (3/t + t/sigma) t^3/3; G3's bound is larger but harmless;
   - the hypothesis c_1 t^(j) <= rho s_0 in 5.2 is unused;
   - "covers O4" should say "several blocks for each p_N; infinite block sets through martin-tail".

## 6. Assessment
G3 is the strongest positive result of the project so far. It changes the problem in three ways.
(i) The order of quantifiers is turned around: T is designed first, and only Lemma B's conclusion is needed for Martin's theorem.
(ii) Every block-side mechanism of the open core is shown to be a two-sided difference of size O(Lambda_f t) on whole windows of scales.
(iii) Density for the SLD space is reduced to base-side engineering at signature-resonant first rows (Lemma Z), which is formally equivalent to density.
The weak point is that Lemma Z carries the whole remaining difficulty at signature-resonant f.
Every design admits such f, because z can be an arbitrary point of B_{l_inf} with z = sign a on F.
A natural route is to lower |z| on FAR parts of the swallowed signature sets. That makes the pinning constant delta'_{l_0} tiny.
At scales well above it the mate structure of f' then copies that of f, and the windows of f' lie below it ("scale decoupling", as in P2A).
The transition band would be handled by the rho-slack together with the Round-2 engineering of the finitely many unpinned carriers (G3 6.3(d)).

**Most valuable idea.** Signature pinning by design. Give every carrier a private signature on its own coordinate set, choose the targets
coarse-to-fine allowed, and make the weights decay super-fast so that windows of scales appear between consecutive weights.
Then, at any first row whose signature sets keep room, base mass on a signature costs first order on both sides of t = 0. The block coefficients of any two
optimal decompositions are then fixed by the mate itself, through a triangular system cut at the window by the box bound.
So every one-sided (switching) resource, whether contacts, near-contacts, peaks, or coordinates pushed beyond their gap, is pinned to O(Lambda t).
On whole windows every mate is a Gamma_w-certificate plus O(Lambda t), and windowed averaging together with C Thm 7.4 recovers it.
