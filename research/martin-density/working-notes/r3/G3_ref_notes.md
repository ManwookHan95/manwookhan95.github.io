# G3 referee notes (assembled): verification of G3 and the referee's additions, with proofs

Setting: canonical base q; Martin's norm with finite block set I_N (p := p_N, every N >= 1); the SLD operator T of G3 1.2.
Notation as in G3 (and A_notes 1). Parts: G3_ref_part1.md (G3 parts 1-3), G3_ref_part2.md (G3 parts 4-5, numerics),
G3_ref_part3.md (attacks, side results). Report: G3_referee.md. Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1. Verification summary
Every step of G3 parts 1-5 was re-derived. Results:
* Theorem A (SLD admissible, (P1)-(P3)): PROVED, correct.
* R_0 (definition; NA points and base-tame points belong to it): PROVED, correct.
* Part 2 toolkit (any admissible T): PROVED, correct. Key identities re-derived:
  - budget q_0 E_q(A) + sum_m sigma_m e_m(W_m) <= s(t) - 1, from q_0 + sum sigma_m = 1 and (A + L*W)(xi) = 1;
  - E_q(a + tB) >= sum_{j notin F}(|tB_j| - z_j t B_j) + nu Psi(t U*B/nu);
  - the block excess equals sum_P |alpha_k|(||W|| - sigma_k W(k)) + (||DW|| - <DW,Dw>/C), using ||alpha||_1 = 1 (from M + C = 1);
  - the pointwise inequality |x| + |y| <= |x - y| + (|x| - zx) + (|y| + zy).
* Part 3 pinning: PROVED, correct.
  - Signature privacy gives -Delta B(s) = Delta c_l delta_l 2^{-s}/n_l + sum_{l'>l} Delta c_{l'} y_{l'}(s)/n_{l'} on S_l.
  - The triangular system is solved from l_* downwards. The fine carriers are bounded by the box bound: 6 c_{l_*+1}/t <= 6t^2 for t >= T_lo(l_*).
* Part 4 window certificate: PROVED, correct. The one-sided excess at peaks, at non-peaks beyond the clamp and at contacts is bounded by
  two-sided differences.
* 5.1 uniform transfer expansion: PROVED, correct.
  - (T1) and (T2) re-derived; Step 3's four cases re-derived; Step 4's identity <Dw,h>/C = s d M - eps(e_y - 1) re-derived.
  - ||h|| = O(c_1), so c_1 must depend on eps_tr; G3 handles this.
  - Trivial slip: |E| <= s^2 max(1, 1/q_0) + ..., not 4 s^2. This is harmless, since only E = O(s^2) is used.
* 5.2 windowed averaging: PROVED, correct (self-contained). The scalar inequalities were checked numerically for rho in (0, 1); the maximum
  violation is <= 0. The hypothesis c_1 t^(j) <= rho s_0 is unused.
* Thm B: PROVED after the fix in section 2.
* No intrinsic defect on R_0: PROVED.
* Thm C: PROVED.
* Lemma Z on the Round-2 classes: PROVED but trivial. It is conditional exactly as the imports are.
* Thm B with infinite F: SKETCH, plausible (section 4).

## 2. Fix for 5.3 (PROVED)
**Problem.** 5.3 chooses eta with sqrt(1 + eta_Gamma(eta)) <= sqrt(1 + eta_0/2) - 1/100. This is impossible when sqrt(1 + eta_0/2) < 1.01.
The constraint rho^2(1 + eta_0) <= (1 + rho^2)/2 forces eta_0 <= (1 - rho^2)/(2 rho^2), which is < 0.0201 for rho >= 0.976.
Numerically, rho = 0.99 gives sqrt(1 + eta_0/2) - 0.01 = 0.9925.

**Fix.** Put kappa_0 := (sqrt(1 + eta_0/2) - 1)/2 > 0. Choose eta <= eta_1 with sqrt(1 + eta_Gamma(eta)) <= 1 + kappa_0, which is possible since eta_Gamma(eta) -> 0.
For large l, require K_4 Lambda_f(l) t <= kappa_0 on the window; this holds since Lambda_f(l) T_hi(l) -> 0. Then 4.2(d) gives
sqrt(Gamma_w(c_t)) <= 1 + 2 kappa_0 = sqrt(1 + eta_0/2), i.e. Gamma_w(c_t) <= 1 + eta_0/2, and the rest of 5.3 is unchanged.

## 3. Remark martin-tail (Preprint B) is valid (PROVED)
**Claim.** If NA((c_0,p_N),F) is dense for infinitely many N, then NA((c_0,p),F) is dense.

**Proof.**
1. Let s_N(x) := sum_{m>N} |R_m x|_m = ||L_{>N} x||_{V_{>N}}. Then |R_m x|_m <= ||R_m x||_1 <= m 2^{-m} q(x), because q*(T e_{k,m}) <= 1 and sum_k 2^{-k} = 1.
   Hence s_N <= eta_N q <= eta_N p with eta_N = (N+2)/2^N, and p_N <= p <= (1 + eta_N) p_N.
2. For an operator A this gives ||A||_p <= ||A||_{p_N} <= (1 + eta_N)||A||_p.
3. Let S in NA((c_0,p_N),F) with ||S||_{p_N} = 1, attained at x_0, so p_N(x_0) = 1 = ||S x_0||.
4. Let J be a norm-one functional on V_{>N} norming L_{>N} x_0 (J := 0 if L_{>N} x_0 = 0), and put phi := J o L_{>N} in l_1.
   Then |phi(x)| <= s_N(x) and phi(x_0) = s_N(x_0).
5. Put S' := S + (S x_0) (x) phi. Then ||S' x|| <= ||S x|| + |phi(x)| <= p_N(x) + s_N(x) = p(x).
   Also ||S' x_0|| = (1 + s_N(x_0))||S x_0|| = p(x_0). So S' is in NA((c_0,p),F) with ||S'||_p = 1.
   Moreover ||S' - S||_p = sup_x |phi(x)|/p(x) <= eta_N.
6. Given T != 0, density for p_N gives a norm-one S in NA_{p_N} with ||S - T/||T||_{p_N}||_{p_N} < 2 eps. Then
   ||T||_{p_N} S' is in NA_p, and ||T||_{p_N} S' - T has p-operator norm <= ||T||_{p_N}(2 eps + eta_N).
   Let eps -> 0 and N -> infinity along the given N. QED

So the restriction to the p_N in G3 (and in the whole project) loses nothing for the question about p.

## 4. Infinite base support with (SR) (SKETCH, plausible; what must be added)
Everything in parts 2-4 except 2.5 is independent of |F|. The required changes are listed below.
* **Flip analysis on F (PROVED).** Let f_j := (B_-(j) sign a_j - |a_j|/t)_+ be the minus-side flip excess.
  Then E_q(a - t B_-) >= sum_{j in F} 2 t f_j, so sum_j f_j <= t/(4 q_0).
  The + side is free in the direction sign(a_j) (no flip), so the excess e_j := (B_+(j) sign a_j - 2|a_j|/t)_+ satisfies e_j <= |Delta B(j)| + f_j.
  An excess in the other direction is a flip of the + side and is O(t) in total.
  Hence clamping B_+ 1_F to |b_j| <= 2|a_j|/t costs <= ||Delta B|| + t/(2 q_0) = O(K t) in l_1.
* **Truncation.** Truncate to F_t with sum_{F \ F_t} |a_j| <= t^2. This costs <= 2t. Then rebalance with kappa_t, which is O(K t) as in 4.2(b).
* **Modified 5.1.** Replace (C-a) by |b_j| <= 2|a_j|/t, so that ||b||_1 <= 2||a||_1/t is unbounded. For |s| <= c_1 t with c_1 <= 1/4:
  - no sign flips occur on F;
  - |s| ||U* b||/nu <= 2 c_1 ||U|| ||a||_1/nu, so the Hilbert part of q* has relative error O(c_1), absorbed by taking c_1 small.
* **Final recovery.** Use C Thm 7.4 with a not in c_00 and b in c_00. The C referee confirms that Remark 7.1' extends to b != 0;
  several blocks are handled as in C's remark.
No obstruction was found. Label: SKETCH (plausible).

## 5. Corrections to G3 part 6 (PROVED statements about the wording)
* **6.3(b).** If delta'_{l_0} = 0, then for l < l_0 the pinning inequality reads
  delta'_l |Delta c_l| <= E_l + kappa_{l_0,l} |Delta c_{l_0}| + (other finer terms), with Delta c_{l_0} unbounded.
  So every coarser carrier whose signature set is touched by y_{l_0} is slaved to the free coefficient Delta c_{l_0}, and is not pinned.
  "All others stay pinned" is therefore false. The structure of 6.3(d) remains plausible: finitely many free coefficients, coefficients slaved
  linearly to them up to O(t)/delta', and an O(K t) remainder.
* **6.3(c).** f' in S_{p*} can be built from any (a', z') with q*(a') = 1, z' in B_{l_inf} and z' = sign a' on supp a'. Put
  zhat' := z' + U e', q_0' := 1/(1 + sum_m |R_m** zhat'|_m), xi' := q_0' zhat', w'_m := J_m(R_m** xi') and f' := a' + L* w'.
  Then f'(xi') = 1 = p**(xi') and p*(f') = 1.
  If a' -> a in l_1 and z' -> z coordinatewise, then f' -> f, by compactness of R_m and continuity of J_m as in C Thm 7.1 Step 2.
  So the lowering of |z| must be done on far coordinates.
  Whether such an f' satisfies dist(rho g, C(f')) < eps is exactly Lemma Z, which is OPEN.

## 6. Numerics (G3ref_work/)
* model.py, model2.py: a toy model with 16 base coordinates and one block of 6 carriers. Each carrier has a private one-point signature.
  It has one contact and one near-contact, two non-peaks, and a near-threshold peak.
* test_lemmas.py: computes SOCP optimal decompositions of f +- t g, for t from 3e-2 to 1e-3. Results:
  - 2.3(b) holds with a margin of 1e-3 relative to its bound;
  - the pinning inequality 3.2 holds up to 1.4e-7 (solver noise);
  - sum|Delta c| / t = 0.04.
* Caveat: finite models are degenerate (the normer face is 12-dimensional and the mate space is only 3-dimensional), so only signs are tested.
* scalar_52.py: the scalar inequalities of 5.2 hold for all rho, and the 5.3 slip is confirmed.

## 7. Conclusions
* **Theorem B (G3) is correct.** For the SLD operator T and every N, every f in R_0 lies in R.
  R_0 contains all NA points and all base-tame first rows, with any block structure.
* **Theorem C (G3) is correct.** For the SLD operator T, density of NA((c_0,p_N), l_2^2) is equivalent to Lemma Z, which is OPEN.
* **Martin-tail is valid** (section 3), so density for the p_N gives density for p.
* No counterexample is suggested.
* **What remains** is Lemma Z at signature-resonant first rows, i.e. first rows whose contacts or near-contacts swallow signature sets.
  Suggested route (HEURISTIC): lower |z| on far parts of the swallowed sets. At f' the pinning constant becomes tiny, so the windows of f'
  lie below a threshold, while above it the structure of f is copied ("scale decoupling", as in P2A). Combine this with the Round-2 engineering
  for the finitely many free and slaved coefficients, and use the rho-slack in the transition band.
* **Most valuable idea:** signature pinning by design.
  - Private signatures, coarse-to-fine allowed targets and super-fast weights with windows make the block coefficients of any two
    optimal decompositions functions of the mate alone, up to O(Lambda t).
  - So every switching or one-sided resource is a pinned two-sided difference.
  - On whole windows every mate is a Gamma_w-certificate plus O(Lambda t), which windowed averaging and C Thm 7.4 recover.
