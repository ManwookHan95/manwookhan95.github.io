# Referee report on Strategy C (r1/C_notes.md): primal second-order multiscale curvature profiles

Role: adversarial referee for strategy C. Setting as in the notes: canonical base B_q = B_{c_0} + U(B_H), finite block
set I, real scalars. I read in full: BRIEFING.md, BRIEFING_R2.md, martin_paper_summary.md, residual_recovery.tex
(Preprint A), hmr_c0_renormings.tex (Preprint B) and r1/C_notes.md. I also consulted C_part*.md and the scripts in
scratchpad/C_work.

Labels: PROVED (re-derived, I agree), SKETCH, HEURISTIC, FALSE, OPEN. "Exact numerics" means my own solvers in
scratchpad/Cref_work. They are independent of the notes' closed-form enumerators and of Nelder-Mead:
* block norm: dual problem, split M + C = 1 (the value is concave in M), inner box-plus-ellipsoid problem solved by
  bisection on the multiplier;
* q and p*: ellipsoid method on the convex programs q(x) = min_h max(||x - Uh||_inf, ||h||) and
  p*(h) = min_W max(q*(h - R^T W), N(W)).
The ellipsoid method only evaluates actual decompositions, so its output is always an upper bound for p*. This makes
the conclusions "coefficient <= c" rigorous up to floating point.

---

## 0. Verdict

**The mathematical core of the notes is sound.**
* I re-derived line by line: Lemmas 2.1-2.3, 3.0-3.6, 4.1, 5.1-5.4, 6.1 and 6.6; Proposition 6.5; Theorems 6.2 (A),
  6.4 (C), 7.1 (B) and 7.4 (B'); Remark 7.1'; Corollary 7.2; Theorem 8.4. Under the hypotheses actually used, I found
  no error in any of these proofs.
* The two central new results survive:
  1. at tame points, mates are exactly the balanced finite certificates;
  2. the sharp second-order invariant is the mass-weighted coefficient Gamma_w, and it is attained along the
     canonical NA truncations thanks to transfer peaks.
* I confirmed the transfer mechanism by exact computation, in both branches. This includes the sign-sensitive
  Step 6: the wrong-sign transfer coordinate gives no gain at all.
* Theorem 8.4 (density along tame supports with no kinks and no degenerate peaks) is correct, and it re-proves the
  [Check] black box.

**One substantive gap matters for the programme.**
* Proposition 8.1's lower bound silently uses (T2), finitely many kinks: its decoupling step needs J to be cofinite.
* The claim in §0.2 and §9.4(C), labelled PROVED, that "infinitely many kinks do not affect the second-order
  coefficient of finite certificates" is unsupported.
* In a finite-dimensional analogue where every off-support coordinate is a kink (with a non-peak transfer coordinate
  to remove the face effect), the exact coefficient is <= 0.296 < Gamma_w = 0.485 for both signs of t. Moving the
  kinks to |z_j| = 0.999 restores Gamma_w at small t.
* So kink supports may carry finite certificates without kink components that have Gamma_2 < Gamma_w. If such a
  certificate has Gamma_2 <= 1 < Gamma_w, Theorem 7.4 does not recover it. In c_0 this is OPEN; §1.20 gives a
  mechanism.

**Other issues are local:**
* Lemma 4.2's constant is not sharp when |F| >= 2 (off by factors of 1.9 to 42 in my tests).
* The SKETCH in §9.2 has a broken step.
* The SKETCH Remark 6.8 places its hypothesis on the wrong object.
* Remark 6.3 and §9.3 draw an unjustified practical inference ("approximants must be non-tame").
* Proposition 8.2 has the right formula but wrong numbers.

No claim labelled PROVED is false in the setting where it is applied. In particular Theorem 8.4 assumes K = ∅.

### Verdict table

| claim (notes' label) | referee verdict |
|---|---|
| Lemma 2.1/2.2 kernel slices (PROVED) | correct |
| Lemma 2.3 Hahn-Banach distance criterion (PROVED) | correct |
| Lemma 3.0/3.1, Cor 3.2 slack/localisation (PROVED) | correct |
| Lemmas 3.3-3.6 (PROVED) | correct |
| Lemma 4.1/4.2 base profiles (PROVED) | correct as lower bounds; constant 1/(2c kappa_j) not sharp for \|F\| >= 2 (fixable) |
| Remark 4.3 (PROVED) | trivial inequality, correct; its extension to second order is unsupported |
| Lemma 5.1 exact block formula (PROVED) | correct (independently confirmed) |
| Lemmas 5.2-5.4 (PROVED) | correct (300 random exact tests) |
| R5 correction (PROVED) | correct |
| Lemma 6.1 (PROVED) | correct |
| Theorem 6.2 = A (PROVED) | correct; the inference in Remark 6.3/§9.3 does not follow |
| Theorem 6.4 = C (PROVED) | correct |
| Lemma 6.6, Prop 6.5 (PROVED) | correct |
| Remark 6.8 (SKETCH) | sound idea; hypothesis misplaced (fixable) |
| Theorem 7.1 = B (PROVED) | correct |
| Remark 7.1' (PROVED) | correct (extends to b != 0 and to I = N) |
| Theorem 7.4 = B' (PROVED) | correct (exact numerics, both branches); trivial constant slips |
| Corollary 7.2 (PROVED) | correct; (a) should state the I = N case |
| Remark 7.2' (SKETCH) | plausible; needs write-up |
| Prop 8.1 (PROVED) | correct only under the missing hypothesis (T2); fails without free coordinates (finite analogue) |
| §0.2/§9.4(C) "infinitely many kinks harmless for Gamma_2" (PROVED) | unsupported; false in the finite analogue; OPEN in c_0 |
| Prop 8.2 (SKETCH) | formula confirmed exactly; numbers wrong |
| Theorem 8.4 (PROVED) | correct |
| Prop 9.1 (PROVED) | correct |
| §9.2 (SKETCH) | broken step; fixable by strengthening the hypothesis |

---

## 1. Claim-by-claim verdicts

### 1.1 Lemmas 2.1/2.2 (kernel slices) — PROVED, agree
* Lemma 2.1, direction (=>): take y = x', then y = x' + v. Direction (<=): scale by lambda = f'(y) when it is nonzero;
  when f'(y) = 0, use s*y and let s -> infinity with p(x' + s y) <= 1 + s p(y). Correct as written.
* Lemma 2.2: the bidual reformulation of the mate inequality via Goldstine nets is correct, because f and g are
  weak*-continuous on X**. The rest is Lemma 2.1 in X**.
* Nothing in the proof uses f(x') or norm attainment beyond p**(xi) = xi(f) = 1.

### 1.2 Lemma 2.3 (support function, distance criterion) — PROVED, agree
* r_{f'} is 1-homogeneous and even, so its convex envelope equals its largest sublinear minorant.
* A linear g is <= r iff |g| <= r.
* C(f') is the subdifferential at 0 of the continuous sublinear r~, so its support function is r~.
* C(f') + eta B_{p*} is weak* compact with support function r~ + eta p.
* The distance is attained (weak* compactness plus weak* lower semicontinuity of p*), so
  dist <= eta iff l <= r~ + eta p.

### 1.3 Lemma 3.0, Lemma 3.1 and Corollary 3.2 (slack, localisation) — PROVED, agree
* Lemma 3.0: g(x')^2 <= 1 - f(x')^2 <= 2 eps. This does not even need eps <= 1.
* Lemma 3.1: I re-derived g(y)^2 <= Phi(2+Phi) + 2 eps(1+Phi), and |g^(v)| <= sqrt(Phi(2+Phi)) (sqrt(1+2/K) + 1/sqrt K)
  <= (1 + 2/sqrt K) sqrt(Phi(2+Phi)).
* Corollary 3.2 follows from Lemma 2.1 (g^(x') = 0). The estimate p*(rho g^ - rho g) <= sqrt(2 eps) is correct.

### 1.4 Lemmas 3.3-3.6 — PROVED, agree
* Lemma 3.3: the ray argument is correct.
  * phi'(t v) is nondecreasing for t >= 0, being convex in t and zero at t = 0. So the minimal s with
    phi'(sv) = K eps exists (v != 0) and s > 1.
  * The constant lambda^2 = 1 + K eps/2 checks: (2 + K eps) <= (1 + K eps/2)(2 + phi'(v)).
* Lemma 3.4: correct. g(Tv) = g(v) because xi(g) = 0, and f(Tv) = 0.
* Lemma 3.5: correct. It uses uniqueness of the normer, metrizability of B_{p**} (c_0 is separable), and weak*
  lower semicontinuity of p**.
* Lemma 3.6: correct. The one-sided limit t -> 0+ already suffices. The variant with Delta'(x' + tv) for arbitrary
  v in X is also correct, because p + f' -> 2.

### 1.5 Lemmas 4.1/4.2 (base profiles) — Lemma 4.1 PROVED. Lemma 4.2 PROVED as lower bounds; its constant is NOT the curvature when |F| >= 2

* Lemma 4.1 is correct. It uses B_{q**} = B_{l_inf} + U(B_H), which I re-checked: the sum of a weak*-compact set and
  a norm-compact set, contained in the weak* closure of B_q. The inward kink flatness for |t| <= 2c is also correct.
* Lemma 4.2(a)-(c): every computation of first-order terms and Hilbert remainders checks, as lower bounds valid for
  |t| << kappa.
* **The constant 1/(2 c kappa_j), with kappa_j = ||P_{e perp} U^* e_j^*||^2/||U^*a||, is sharp only when |F| = 1.**
  * Better dual test: add gamma in span{e_i^* : i in F} to beta = s sigma e_j^*.
  * Its first-order contribution to q*(a + beta) equals gamma(eta)/c, so it cancels in the ratio.
  * Choose gamma to remove the component of sigma U^* e_j^* in E_F ∩ e^perp, where E_F = span{U^* e_i^* : i in F}.
    The Hilbert remainder then becomes s^2 ||P_{E_F^perp} U^* e_j^*||^2/(2||U^*a||).
  * Result: E_q(t e_j) >= t^2/(2 c kappa~_j)(1 + O(|t|/kappa~_j)) with
    kappa~_j := ||P_{E_F^perp} U^* e_j^*||^2/||U^* a|| <= kappa_j.
  * Primal side: let the cube part on F rise to the common level, as in the LP-optimal decomposition of Prop. 8.1(i).
    This shows the improved constant is attained.
* Exact numerics (Cref_work/kink_test.py; n = 6, d = 3, F = {0,1}, kink at j = 2):

  | trial | notes 1/(2c kappa_j) | sharp 1/(2c kappa~_j) | exact E/t^2 at t = 1e-3 | exact E/t^2 at t = 3e-4 |
  |---|---|---|---|---|
  | 0 | 0.7066 | 1.3136 | 1.3085 | 1.3120 |
  | 1 | 0.4023 | 16.895 | 18.49 | 17.34 (still decreasing toward 16.9) |
  | 2 | 1.2814 | 51.900 | 51.845 | 51.883 |

  * The notes' numerical confirmation (base_profiles.py) used |F| = 1, where the two constants coincide.
  * The same improvement applies to (b) (outward support coordinate, inward via a kink) and to (c).
* Consequences:
  * Nothing downstream breaks: kappa~_j <= kappa_j -> 0, so the stiffness statements are even stronger.
  * §0.2's phrase "outward-kink curvature 1/(2 c kappa_j)" should read "at least".
  * The quadratic window is |t| <~ c kappa~_j, shorter than stated.

### 1.6 Remark 4.3 (far stiffness and l_1 data) — the inequality is trivially true; the "harmlessness" conclusion is HEURISTIC
* The displayed bound reduces to |sum_{j>N} (z_j - z'_j) beta_j| <= 2||beta|_{(N,inf)}||_1, which is trivial.
* It concerns only the first-order contact defect of a fixed beta. It says nothing about:
  * mates with kink components (Remark 7.3);
  * the second-order coefficient. The extension of the "harmless" claim to the second-order coefficient (§0.2,
    §9.4(C)) is not proved and is doubtful; see 1.20.

### 1.7 Lemma 5.1 (exact block formula) — PROVED, agree; the notes' numerical verification is circular, mine is not
* I re-derived:
  * the root selection, and the equivalence with (S/l - 1)^2/F2 + Y^2/l^2 = 1;
  * lambda > 0, and rho_0 >= 0 iff Y <= S;
  * part (a): the construction of h, with ||alpha||_1 = 1;
  * part (b): ||w||_inf = M, ||Dw|| = C, w(y) = lambda;
  * part (c).
* Derivatives at z: dLambda/dS = M, dLambda/dY = CY/|z|, and sqrt(S^2 - (1-F2)Y^2) = |z| sqrt(F2)/C. Hence
  Lambda_SS = sqrt(F2) Y^2/Delta^{3/2} = C c_Q/(|z| F2), using Y^2/|z|^2 = c_Q/C^2.
* The second-order formula (iii) is correct: Lambda is 1-homogeneous, and the Hilbert excess term is
  ||P_perp D^{-1} delta_Q||^2/(2Y).
* The notes' "12 digits" check (lam_check.py) compares Lambda against blockexact.block_norm. That function itself
  solves the same quadratic for each candidate peak set, so the check is circular.
* Independent check (Cref_work/block_hess.py):
  * my dual solver agrees with blockexact to 1e-16;
  * on z built from (P, alpha, w), it reproduces |z| = Lambda exactly;
  * Lambda_SS agrees with C c_Q/(|z|F2) to 12 digits;
  * 2E/t^2 matches formula (iii) to O(t), e.g. 0.13200757 at t = 1e-4 against 0.13200847.

### 1.8 Lemmas 5.2-5.4 (overshoot, Huber, sign flip) — PROVED, agree
* The identity |a + d| = |a| + s d + 2(-s d - |a|)_+ and the decomposition z + delta = [l_1 part] + (1+mu)|z| D(Dw/C)
  are correct. The l_1 part is supported on P and has norm (1+mu)|z| + 2 ov.
* Lemma 5.3: correct with N(w + sigma e_k) <= 1 + X + Y_s. The Huber optimisation requires w(delta) = 0, which is
  the case stated.
* Lemma 5.4: correct. Sign flips preserve N, and w_k z_k = |w_k||z_k| holds on both P and Q.
* Random tests of all three bounds with the exact solver (Cref_work/lemmas5.py): 300 instances, 0 violations.

### 1.9 Correction to briefing R5 — PROVED, agree
* In the w-neutral direction, the deep non-peak Hessian is (C/|z|)/Phi_k^2 in delta-units, i.e. m^2 C u_k^2/|z| in
  t-units.
* Exact check (block_hess.py) of 2E/t^2 * Phi_k^2 against the two candidate constants:

  | quantity | four instances |
  |---|---|
  | 2E/t^2 * Phi_k^2 (exact) | 0.268, 0.278, 0.233, 0.262 |
  | C/\|z\| (notes) | 0.276, 0.278, 0.226, 0.264 |
  | 1/C (briefing) | 2.8 to 3.4 |

  The residual differences come from the rank-one and projection terms of 5.1(iii) for not-so-deep k.
* The slope gamma m Phi_k |u_k| (gap without the 1/M factor) is correct.

### 1.10 Lemma 6.1 (excess splitting) — PROVED, agree.

### 1.11 Theorem 6.2 (Theorem A) — PROVED, agree; one interpretive caveat
* Proof steps:
  * the room r' = min_{J'} (1 - |z'_j|) > 0 because z' is in c_0;
  * delta = t R_m v vanishes on Qbar'_m and has zero peak sum (because w'_m(R_m v) = 0);
  * (5.1) together with (MS) gives o(t^2);
  * f'(v) = 0;
  * Lemma 3.6 then gives g'(v) = 0;
  * finite-codimension linear algebra and finiteness of F' ∪ K' conclude.
* The numerical confirmation (thmA_test.py) has Q' = ∅. It is therefore a weak test, though it agrees.
* Caveat on Remark 6.3 and §9.3, first bullet: the inference "to approximate a mate g that is not a finite
  combination, the NA approximants must be non-tame" does not follow.
  * Theorem A constrains each C(f'_n) to W(x'_n), whose dimension may grow with n.
  * Tame x'_n with finite but growing non-peak sets Qbar'_n can carry finite certificates converging to an infinite
    certificate.
  * This matters strategically. Along tame approximants, Theorem A together with Prop. 8.1 (at x'_n) gives a complete
    second-order description of C(f'_n), so the open regime can be attacked with tame approximants. The notes'
    phrasing steers away from this.

### 1.12 Theorem 6.4 (Theorem C) — PROVED, agree
* With K finite, J is cofinite. V_00 ⊂ c_00(J) uses only finitely many coordinates, each with positive room, so the
  base is flat.
* The block computation is as in Theorem A.
* Density of V_00 in V_0 follows from the (F5) independence on c_00(J), which I checked through the T-coefficients at
  the infinitely many indices k in P°_m. The final linear-algebra step is correct.

### 1.13 Lemma 6.6 and Proposition 6.5 (rebalancing direction, balance) — PROVED, agree
* Lemma 6.6, checked line by line:
  * solvability of the finitely many conditions on nu_J;
  * f(nu) = 0;
  * the base is exactly flat, using xi + t nu = (1 + t lambda)(xi + t nu_J/(1+t lambda));
  * delta'' vanishes on Qbar and has zero peak sum, so the overshoot is o(t^2) by (MS);
  * the formula for g(nu).
* Proposition 6.5: uniqueness, v_m(z_m) = 0, b(xi) = 0, and c_m = -d_m (from omega(z) = sigma d) are all correct.

### 1.14 Remark 6.8 (existence of tame non-attaining f) — SKETCH; correct idea, the hypothesis is misplaced
* The deterministic part is correct: f := a + sum_m R_m^* J_m(R_m** xi) has norm one and normer xi, and it is not NA.
* Probabilistic part, issue (i): the anti-concentration of u_{k,m}(xi) comes only from the randomised coordinates
  off F. The hypothesis must therefore bound ||u_{k,m}|_{F^c}||_2 from below, e.g. >= c Phi_m(k)^{1/3}.
  * A lower bound on ||u_{k,m}||_2 itself is useless.
  * By tail density, infinitely many u_{k,m} approximate functionals supported in F, so their F^c-part can be
    arbitrarily small.
* Issue (ii): the window [0, theta_m Phi_m(k)] depends on xi itself, through theta_m and the normalisation p**.
  * Use instead a deterministic window [-A Phi_m(k), A Phi_m(k)] for u_{k,m}(z + Ue), with A >= sup theta_m p** over
    the perturbation range. A uniform lower bound on C_m is needed for this and should be argued.
  * Sums of independent log-concave variables have density <= const/sd. With the corrected hypothesis,
    Borel-Cantelli then gives (T3).
  * (T4) follows from |u_{k,m}(z + Ue)| >= Phi_m(k)^{1/2} eventually.
* With these corrections the sketch is convincing. It remains conditional on an assumption about T that is not
  verified for Martín's T (as the notes say).

### 1.15 Theorem 7.1 (Theorem B) — PROVED, agree
* Steps 1-7 checked:
  * a(x~_N) = 1, so a = grad q(x~_N);
  * p(x~_N) -> 1/q_0;
  * eps_N <= q*(f'_N - f) -> 0, using p* <= q*;
  * gamma_0 > 0, and the sup-norm bound ||W(t)||_inf = (1 - t d')M' holds with peaks attained outside supp omega;
  * ||P_perp h||^2 = ||D omega||^2 - d'^2;
  * the uniform constants theta(t);
  * slack: D(t) >= c_rho min(t^2, |t|) with c_rho = (1-rho^2)/(2 sqrt 2).
* The first rows f'_N do not depend on g. Moreover g'_N(x'_N) = 0, by the block-threshold identity at x'_N.
* Minor point: H_{b,N} = H_b exactly, since b'_N - b is a multiple of a and P_{e perp} U^* a = 0.

### 1.16 Remark 7.1' (b = 0, arbitrary a) — PROVED, agree
* x~_N = z^N + U e_N lies in B_q, a_N(x~_N) = 1, a_N -> a in l_1, e_N -> e. Steps 2-7 go through.
* The Theorem 7.4 variant also works, with beta_N proportional to a_N.
* Two small additions:
  1. The proof also covers b != 0 finitely supported in F when a is not in c_00. Use b'_N = b - (b(x'_N)/c_N) a_N:
     signs on supp b are stable and the first-order term is b'_N(x~_N) = 0.
  2. Preprint A's weighted-directions theorem also allows I = N. The proof extends verbatim:
     * dominated convergence in m (since ||R_m|| <= m 2^{-m}) for eps_N and for p(x~_N);
     * strict convexity of p** from Martín's Prop. 3.
     Corollary 7.2(a) should say this explicitly.

### 1.17 Theorem 7.4 (Theorem B', sharp condition Gamma_w <= 1) — PROVED, agree; confirmed numerically in both branches
* Re-derived:
  * the formula for e_inf;
  * the bound on q*(e_inf) (my bound is 2 lambda_* delta_1, sharper than stated);
  * lambda_* mu_* <= T(xi) + lambda_* delta_1 q_0;
  * the bookkeeping identity (7.3), where the theta'-terms cancel between lambda_* u_{k_*}(x'_N) and sigma' e_{y,N};
  * the sup norm ||W(t)||_inf = (1 - t rho d')M' - eps, with the transfer coordinate kept inside the sup norm for
    |t| <= t_3;
  * the Hilbert expansion, uniform in N because ||D y_N||^2 = O(1) + (lambda_*/m)^2;
  * equalisation: Gamma_eff = H_N - q_0(H_N - H_b)/(1 + q_0 eps_1/e_y) <= Gamma_w + H_N eps_1;
  * Step 6 with the reversed target T = -tau_* + delta_0 q*(tau_*) a, where (7.3) becomes
    y_N(R x'_N) = sigma' e_{y,N} - lambda_* mu'_*.
* Two trivial slips:
  1. In Step 6 the bound is Gamma_eff <= Gamma_w + 2 H_b eps_1 for eps_1 <= 1/2, because of a 1/(1-x) factor, rather
     than "+ H_b eps_1".
  2. In the several-blocks remark, a block with tau_m < 0 contributes tau_m sigma_m e_{y,m}/q_0 + |tau_m| eps_{1,m}
     to the base level, not tau_m(sigma_m e_{y,m}/q_0 + eps_{1,m}). The conclusion Gamma_w/2 + O(max eps) is
     unchanged.
* Exact numerics in the notes' own finite model (n = 6, d = 3, K = 5; q_0 = 0.8958, sigma = 0.1042, H_N = 2.8620,
  Gamma_w = 0.29824). The quantity is the exact 2(p*(f+tg) - 1)/t^2:

  | model | t = 1e-2 | t = 3e-3 | t = 1e-3 |
  |---|---|---|---|
  | no transfer coordinate | 0.36120 | 0.36535 | 0.36655 (0.36709 at 1e-4) |
  | + peak transfer coord., delta_0 = 0.1 | 0.36123 | 0.36538 | 0.36658 |
  | + peak transfer coord., delta_0 = 0.01 | 0.30689 | 0.30762 | 0.30783 |
  | + peak transfer coord., delta_0 = 0.003 | 0.30008 | 0.30080 | 0.30100 |
  | same, deeper Phi_6 = 1.4e-5 | 0.34017 (outside the window t <= t_3) | 0.30087 | 0.30108 |
  | + non-peak transfer coord. (delta_0 = 0) | 0.29723 | 0.29794 | 0.29814 -> Gamma_w |

  * The notes' explicit decompositions (0.3917, 0.3265, 0.3073, 0.3005 at t = 1e-2; 0.3926, ..., 0.3012 at
    t = 3e-3) are upper bounds, and they are consistent with these exact values.
  * The quoted "0.3005" is the t = 1e-2 value; the explicit limit is about 0.301.
  * At delta_0 = 0.1 the transfer decomposition (0.392) is worse than what the finite model already achieves
    (0.367). This is harmless: the theorem only needs delta_0 -> 0.
* New observation: a non-peak transfer coordinate has zero inefficiency, since there is no margin term in (7.3), and
  it gives exactly Gamma_w.
  * In c_0, robust non-peaks cannot be produced by tail density alone: the window |u_k(xi)| < theta Phi_k is too thin.
    So the notes' choice of peaks is right.
  * The inefficiency eps_1 is purely the price of robustness.
* Step 6 test (pure base certificate; H_b = 22.404 = Gamma_max; Gamma_w = q_0 H_b = 20.070; exact coefficients):

  | model | t = 3e-3 | t = 1e-3 |
  |---|---|---|
  | no transfer | 21.136 | 21.367 |
  | Step-6 transfer, delta_0 = 0.01 | 20.165 | 20.154 |
  | Step-6 transfer, delta_0 = 0.003 | 20.111 | 20.100 |
  | wrong-sign (Step-1) transfer | 21.135 | 21.367 |

  So the sign rule of Step 6 is necessary, and it is the one the notes give.

### 1.18 Corollary 7.2 — PROVED, agree (with the I = N remark of 1.16)
* (b) requires (f, g) contractive; the notes state this.
* "Simultaneously" is legitimate: g'_N does not depend on the transfer decomposition, and Li_N C(f'_N) is closed.
* (c) holds for every f whose a admits the base expansion. b finitely supported in F suffices; a in c_00 is not
  needed.

### 1.19 Remark 7.2' (weighted directions with Gamma_w) — SKETCH, plausible
* Lset = {|w_k| >= gamma} is independent of the truncation index J provided gamma lies in (5M/8, M). Perturbed
  coordinates of omega_{J,t} stay <= M/2 + M/8, and the transfer peak is a peak, hence not in the half-peak set S.
* Preprint A's o(t^2) truncation cost combines additively with the rebalanced levels, uniformly in J.
* Then Theorem 7.4 (b = 0, Remark 7.1') replaces [Check].
* This should be written out, but I see no obstruction.

### 1.20 Proposition 8.1 (sharp second-order coefficient) — upper bound PROVED. Lower bound PROVED only under the additional hypothesis (T2) (K finite); as stated it has a gap. The accompanying claim about kinks is unsupported and doubtful

* Steps (i)-(v) re-derived:
  * the Gram system for k_{2,perp} and its orthogonality to e;
  * |Z_j| = q_0 + t^2 kappa_2 on F and ||H|| = q_0 + t^2 kappa_2 + O(t^3), the latter via q*(a) = 1;
  * base supremum q_0 H_b;
  * the general Lemma 5.1(a) bound with overshoot;
  * the Legendre computation L = (|z|/C)||P_perp D omega~||^2 + d^2 M^2/Lambda_SS = sigma H_N, including the
    degenerate case z_Q = 0 (where M = 1/(1 + sqrt F2) and the coefficient is C/(2|z|)).
* **The gap.** Step (iii) reads "By (F5) (independence lemma), nu_c in c_00(J) can be chosen so that the finitely
  many numbers (u_{k,m}(nu))_{k in Q_m} and pi_m(nu) take any prescribed values".
  * (F5) only applies to relations vanishing on a *cofinite* set, so this needs F ∪ K finite.
  * The hypotheses listed in Prop. 8.1, "(i.e. (T3), (T4) with Dg = empty)", omit (T2).
  * If K is infinite, J is not cofinite. It can even be empty (z_j = ±1 for every j off F, which is allowed for
    xi in l_inf).
  * Lemma B does not exclude elements of span{u_{k,m}, pi_m} ⊂ Y supported on F ∪ K. The decoupling, and with it
    the lower bound, then fail.
* **This is not a formality.** Finite-dimensional analogue (Cref_work/kinks_test.py, kinks_small_t.py): the same
  model, but every off-support coordinate is made a kink (z_j = ±1 for j not in F, so J = ∅). The certificate is the
  pure block certificate with omega on the non-peak k_0 = 1, and the non-peak transfer coordinate removes the face
  effect. Then sigma = 0.1650, H_N = 2.9394, Gamma_w = 0.48511, and the exact coefficient is:

  | model | t > 0 | t < 0 |
  |---|---|---|
  | J = {0,1,2}, free coordinates (Gamma_w = 0.29824) | 0.29814 (t = 1e-3) | 0.29834 (t = -1e-3) |
  | J = ∅, all kinks (Gamma_w = 0.48511) | 0.29567 (3e-4), 0.29568 (1e-4) | 0.28325 (-3e-4), 0.28324 (-1e-4) |

  * With free coordinates the coefficient tends to Gamma_w = 0.29824.
  * With J = ∅ both one-sided coefficients are far below Gamma_w = 0.485. Since the ellipsoid gives upper bounds for
    p*, the inequality Gamma_2 < Gamma_w is rigorous here.
  * Without the transfer coordinate the coefficients are 0.4849 (t > 0) and 0.2866 (t < 0). The liminf is still far
    below Gamma_w.
  * Control (Cref_work/kinks_room.py): move the kinks back inside, |z_j| = 0.999. Then J is nonempty with room about
    0.001 c, and Gamma_w = 0.48491. The coefficient is 0.378 / 0.350 at t = ±1e-3, where the room is exceeded, and
    0.48492 / 0.48489 at t = ±1e-4, i.e. = Gamma_w.
  * So the defect is caused exactly by the absence of free coordinates. Small rooms (rooms -> 0 with K finite) are
    harmless asymptotically, as Prop. 8.1 says, but they delay the onset of the Gamma_w regime to scales below the
    room. This is relevant for any argument that needs uniformity across scales.
  * Mechanism: base components on kink coordinates aligned with z_j cost nothing at first order for one sign of t,
    so the certificate can be re-split one-sidedly through the kinks.
  * In c_0 such a re-split requires (approximate) vectors R^* v supported on F ∪ K with one-sided signs on K. This is
    exactly the "cross-mate resonance" of the briefing (R7(i)/(ii)), and it is not excluded by Lemma B when K is
    infinite.
* **Consequences.**
  1. Prop. 8.1 must assume (T2). More precisely, it needs the finitely many functionals u_{k,m} (k in Q_m) and pi_m
     to be linearly independent on c_00(J). Its last sentence ("every balanced finite certificate in C(f) satisfies
     Gamma_w <= 1") can fail without this assumption.
  2. The statements in §0.2 ("Far stiffness of xi (kinks, rooms -> 0) is harmless ... for the second-order
     coefficient of finite certificates (PROVED...)") and §9.4(C) ("infinitely many kinks - does not affect finite
     certificates without kink components") are unsupported. The finite analogue suggests they are false in general.
     * "Rooms -> 0 with K finite" is genuinely covered, asymptotically; the onset scale degenerates with the room.
     * "Infinitely many kinks" is not.
     * The phrase "the test points ... leave all coordinates off supp a fixed" is also literally false: nu_c moves
       finitely many free coordinates, and U k_perp moves all coordinates.
  3. Configuration (C) of §9.4 should be enlarged. Supports with infinitely many kinks may carry finite certificates
     with Gamma_2 < Gamma_w even without kink components. Theorem 7.4 does not recover such a g when
     Gamma_2(g) <= 1 < Gamma_w(g).
* **Mechanism in c_0** (referee SKETCH). Take a single block, J finite (K cofinite), Q finite with |Q| >= |J| + 1,
  and all peaks non-degenerate.
  * Look for v'' = c' s 1_P + v''_Q, uniform on the peaks so that the block stays first-order flat, with
    beta := R^* v'' vanishing on J and v''(z) = 0. These are |J| + 1 linear equations in 1 + |Q| unknowns, so a nonzero
    solution exists, and beta != 0 by injectivity.
  * If moreover z_j beta_j >= 0 on K, then for t > 0 and s >= 0 the decomposition
    f + tg = (a + t s beta) + R^*(w + t(v - s v'')) is first-order neutral.
  * Its equalised second-order level is Gamma(s) = q_0 s^2 ||P_{e perp} U^* beta||^2/||U^*a|| + sigma H_N(v - s v'').
    This is a convex quadratic with Gamma(0) = Gamma_w and, generically, nonzero slope at 0.
  * So, whenever the alignment holds, one one-sided coefficient drops strictly below Gamma_w. That would contradict
    Prop. 8.1's Gamma_2^- >= Gamma_w at such a support.
  * Lowering both one-sided coefficients, which is what an unrecovered mate needs, requires re-splits with opposite
    sign patterns on K. In the finite analogue both drop.
  * Whether the sign alignment on K can be arranged consistently is OPEN: it is a fixed-point problem, because z on K
    influences the block data.
* Theorem 8.4 is unaffected, since it assumes K = ∅.

### 1.21 Proposition 8.2 (finite-dimensional face formula) — SKETCH; the formula is confirmed exactly, the notes' numbers are wrong
* On the face {p = 1 = f}, both a(y) = q(y) and w(Ry) = |Ry| hold. So sigma(y) = (R^T w)(y) is linear there, and
  the face is a polytope in the variables (c, c z'_J).
* In the notes' model the face is two-dimensional (4 variables, 2 equalities). Its sigma-range is
  [0.04107, 0.12829], not "[0.059, 0.113+]".
* Hence sigma_max H_N = 0.36715.
* The exact coefficient is 0.36120, 0.36535, 0.36655, 0.36697, 0.36709 at t = 1e-2, 3e-3, 1e-3, 3e-4, 1e-4,
  converging to 0.3671. So "Gamma_2 = weighted average at the most unfavourable split on the face" is confirmed.
* The notes' "numerics 0.355-0.362" are t = 1e-2 values, and their "predicted 0.33-0.34" comes from an incomplete
  trace of the face.
* Primal lower bound at the face point y_s with sigma_s = sigma_max: see the addendum (§4).
* The same formula fits the Step 6 base test: c_max H_b = 0.958926 x 22.404 = 21.48, while the exact coefficient is
  21.37 at t = 1e-3 and increasing.

### 1.22 Theorem 8.4 (tame supports are recoverable) — PROVED, agree
* Chain: Theorem 6.4 gives C(f) ⊂ W(xi). Proposition 6.5 (K = Dg = ∅) makes every mate a balanced finite
  certificate. Proposition 8.1 (valid here, since K = ∅ makes J cofinite) gives Gamma_w <= Gamma_2^- <= 1. Then
  Theorem 7.4 applies.
* It is a genuine new result. It is vacuous for non-attaining f until tame non-attaining supports are shown to exist
  for Martín's T (Remark 6.8 is a SKETCH).

### 1.23 Proposition 9.1 (general kernel statement) — PROVED, agree
* The statement "V_00 can be {0} generically" is a plausible HEURISTIC, not a theorem: infinitely many linear
  conditions on finitely many coordinates.
* The density issue is correctly flagged as open.

### 1.24 §9.2 (necessary decay of deep coefficients) — SKETCH with a broken step; fixable under a stronger hypothesis
* Quoted step: "φ(tν) <= o(t^2) + 2m|t|B Σ_{k>K} Φ(k), valid for |t| <= r/B (room). With Lemma 2.2 at |t| = r/B ..."
* The o(t^2) is the shallow-peak overshoot. It is small only as t -> 0 *for fixed K*. At the fixed scale |t| = r/B
  it is bounded only by 2m Σ_{k<=K, k in P} Φ_k (r - μ_k)_+, which is of order r Σ_{μ_k < r} Φ_k.
  * That quantity does not tend to 0 as K -> infinity.
  * So the displayed inequality, and the rate Σ_{k>K}|c_k| = O(sqrt Φ'(K)), do not follow.
* Further defects:
  * the room r must be uniform over supp ν for all K, K' (it fails if rooms -> 0, unless supp ν avoids such
    coordinates);
  * the constant should be 4mB^2 Φ'(K)/r, not B^3;
  * letting K' -> infinity needs Σ|c_k| < infinity a priori.
* Fix: add to the definition of a sign-representing vector that u_k(ν) = 0 on every shallow peak with margin μ_k < r,
  and that rooms on supp ν are >= r. Then the shallow overshoot vanishes exactly for |t| <= r/B, and the claimed
  bound holds with B^2.
* The "borderline gap" conclusion (sqrt(Φ_k) versus Σ c_k^2/Φ_k < infinity) is then correct as a conditional
  statement.

### 1.25 Not on the list but checked
* §10.1, the "rigorous instance" of failure of pointwise excess domination: correct. The T-coefficient argument
  gives 1 <= 2 Φ_k^2 M^2/C, contradicting C > 2Φ_k^2 M^2.
* §0.3 item 2: correct as an observation. [Check]'s H <= 1 is sufficient, not necessary; at tame supports block
  certificates are mates up to sigma_m H_m <= 1.

---

## 2. Substantive issues, ranked

1. **Kinks (Prop. 8.1 hypothesis; §0.2 and §9.4(C) claims).** See 1.20.
   * Prop. 8.1 needs (T2). Its conclusion Gamma_2 = Gamma_w, and "every finite-certificate mate has Gamma_w <= 1",
     can fail without free coordinates (exact finite analogue: <= 0.296 versus 0.485).
   * The PROVED label on "infinitely many kinks are harmless for the second-order coefficient" must be withdrawn.
   * This identifies a concrete *candidate* class of unrecovered mates: finite certificates at supports with infinitely
     many kinks, with Gamma_2 <= 1 < Gamma_w. Their existence in c_0 is OPEN. Recovering them needs resonances (approximate relations between block
     functionals and vectors on F ∪ K with one-sided signs). This is a sharper form of the briefing's obstacle
     R7(i)/(ii).
2. **§9.2 rate.** The rate claim does not follow even conditionally; the fix is in 1.24.
3. **Lemma 4.2 constant.** It is not sharp for |F| >= 2; the sharp kappa~_j uses P_{E_F^perp}. This is a wording
   change only; nothing downstream breaks.
4. **Remark 6.8.** The hypothesis must be on u_{k,m}|_{F^c}, and the threshold windows must be made deterministic.
5. **Remark 6.3 and §9.3.** "Approximants must be non-tame" does not follow from Theorem A. Tame approximants with
   growing non-peak sets are the natural vehicle for (Q2).
6. **Prop. 8.2 numbers.** Correct: exact Gamma_2 = sigma_max H_N = 0.3671 over a 2-dimensional face with sigma in
   [0.041, 0.128].
7. **Minor.**
   * Step 6 constant (2 H_b eps_1).
   * Sign of the eps-term for tau_m < 0 in the several-blocks remark.
   * B^3 should be B^2.
   * lam_check.py is circular.
   * Corollary 7.2(a) should mention I = N.
   * Remark 7.1' extends to b != 0 finitely supported in F.

## 3. Assessment and most valuable idea

**What is established.** I find strategy C's main contributions correct and valuable:
1. Localisation of the mate condition to the small region {phi' < K eps}.
2. The exact local block geometry (Lemma 5.1): the peak simplex is flat, and Lambda_SS = C c_Q/(|z| F2).
3. Absorption (Theorems A and C): at tame points, fibres are finite-dimensional spaces of balanced finite
   certificates.
4. The sharp second-order invariant Gamma_w, as an upper bound everywhere (Cor. 7.2(c)) and as an exact value at tame
   supports with K finite (Prop. 8.1).
5. Recovery of all such certificates along the canonical truncations (Theorem 7.4). This proves the [Check] black
   box, and with Remark 7.1' it frees Preprint A from it.
6. Density along tame supports with K = Dg = ∅ (Theorem 8.4).

**What is open.** Nothing here decides density. The open core, as the notes say, is the non-tame case: infinitely
many non-peaks (generic), failure of (MS), degenerate peaks, a not in c_00. To this I add **infinitely many kinks**,
which the notes wrongly classify as harmless.

**Most valuable idea: transfer peaks (Theorem 7.4).**
* Every tail of (u_{k,m})_k is norm dense in S_{q*}. So one can choose a deep index k_* whose functional approximates
  any prescribed correction T with T(xi) > 0 small.
* Such a k_* is a robust peak of xi and of all canonical NA approximants.
* Lowering its block coordinate by O(t^2/Phi_{k_*}) converts the uniform O(t^2) lowering of all near-peak block
  coordinates into a base perturbation proportional to a. The inefficiency is arbitrarily small.
* Second-order mass transfer between base and blocks thus becomes essentially free. As a result the dual ball of
  Martín's space is exactly as flat at second order as the mass-weighted invariant Gamma_w allows, and this is
  reproduced uniformly along canonical NA approximants.
* In every finite-dimensional model this mechanism is absent, and the coefficient is strictly larger (exactly
  sigma_max H_N = 0.367 versus Gamma_w = 0.298 in the notes' model).
* So it is a genuinely infinite-dimensional effect of Martín's density property. It defeats the most natural
  curvature obstruction, and it is the natural tool for the remaining regimes: approximating infinite certificates by
  finite ones, and possibly the kink-resonance configuration identified above.

**Recommendations.**
1. Add (T2) to Prop. 8.1 and withdraw the kink claims.
2. Study the kink configuration as a new seed:
   * Does Y ∩ R^*(l_inf) contain vectors supported on F ∪ K with one-sided signs on K, or approximate versions at
     the relevant scales?
   * If not, prove Gamma_2 = Gamma_w there.
   * If yes, test recoverability along NA approximants that keep finitely many kinks.
3. Pursue (Q2) along tame NA approximants with growing non-peak sets, where Theorem A and Prop. 8.1 describe the
   fibres completely at second order.
4. Write out Remark 7.2' and the I = N extension.

## 4. Addendum: two-sided exact values in the finite model (Prop. 8.2 and §1.17)

Primal lower bounds p*(f+tg) >= (f+tg)(y)/p(y) were maximised over test points y (Cref_work/face_lower2.py). Any test
point gives a rigorous lower bound, and the ellipsoid values are rigorous upper bounds.
* In the notes' model without a transfer coordinate, the primal lower bound equals the dual upper bound at both
  scales tested. The primal bound was found both from the face point with maximal block mass (sigma_s = 0.12828) and
  when started from x:

  | t | primal lower bound | dual upper bound |
  |---|---|---|
  | 1e-2 | 0.36120 | 0.36120 |
  | 3e-3 | 0.36535 | 0.36535 |

* So the coefficient is pinned from both sides at these scales, well above Gamma_w = 0.2982. Together with the
  monotone exact values up to t = 1e-4 (0.36709), this confirms rigorously, in finite dimensions, that the rebalancing
  obstruction is real without transfer peaks. Its size is the face value sigma_max H_N = 0.36715.

## 5. Files
* Scripts: scratchpad/Cref_work/
  * solvers.py, test_solvers.py: independent exact solvers, cross-checked with the notes' enumerators to 1e-16;
  * kink_test.py: Lemma 4.2 sharp constant;
  * block_hess.py: Lemma 5.1, Lambda_SS, (iii), R5;
  * lemmas5.py: Lemmas 5.2-5.4;
  * exact_gamma.py, exact_transfer.py, step6_test.py, small_t.py: Theorem 7.4;
  * face_lp.py, face_lower2.py: Prop. 8.2;
  * kinks_test.py, kinks_small_t.py, kinks_room.py: Prop. 8.1 and kinks;
  * rem71_check.py: Remark 7.1' extension to b != 0.
