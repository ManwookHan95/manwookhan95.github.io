# Referee report on Notes A (strategy A: lower-limit reduction and recovery along NA sequences)

Referee: adversarial check of `ctx/r1/A_notes.md` (all 1013 lines), read against `ctx/BRIEFING.md`, Preprint A
(`residual_recovery.tex`) and Preprint B (`hmr_c0_renormings.tex`). Date: 2026-10-08.
Setting and notation are those of the notes (canonical base; finite block set I unless said otherwise).
Status labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Verdicts: correct / correct with fixable gaps / wrong / unclear.
Independent scripts (numpy only) are in `/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/refA/` (list in §4).

---------------------------------------------------------------------------------------------------

## 0. Summary

1. **The mathematical core is sound.** I re-derived by hand every step of R1/R2 (Props 2.1-2.2), Thm 3.1, Thm 3.2,
   Cor 3.3, Thm 3.5, Lemmas 4.3-4.7, Prop 4.8, Thm 4.10, Cors 4.11-4.12, Thm 4.13, Prop 4.16, Thm 4.17, Lemma 6.1,
   Thm 6.2, Lemma 6.3, Lemma 6.4, Thm 6.5, Thm 6.8, Cor 6.9, Lemmas 7.1-7.2, Cor 7.3, Prop 7.4, Lemmas 8.1-8.3,
   Prop 8.4, Lemmas 8.5-8.6. I found no wrong step in any main theorem. The two structural results (Transport
   Theorem 4.10 / lower semicontinuity of cl Cert, and the averaging Theorem 6.8) are correct.
2. **Fixable gaps** (details in §3):
   * (G1) The certificate radius of Definition 4.1 (min gap / 2 max|omega|) differs from the one used in Remark 4.9
     and in the proof of Cor 6.10(a) (coordinatewise min_k gap(k)/(2|omega(k)|)). With Definition 4.1 the proof of
     Cor 6.10(a) (and the second proof of Theorem L in Cor 6.10(b)) cannot secure hypotheses (ii) and (iv) of Thm 6.8
     simultaneously; explicit failure scenario in §3.1. Fix: use the coordinatewise radius everywhere (all lemmas hold
     verbatim).
   * (G2) Cor 6.9 (one-sided admissibility implies H(c_t) <= 1 + o(1)) is proved only if C_m is bounded below on the
     active blocks; fine for finite I, not covered by the blanket "everything also holds for I = N" (§10).
   * (G3) The claim that shifts give "strictly larger recoverable classes" / that the [Check] condition is "NOT sharp"
     (summary row 7, title of §4.5, §10) is not proved in the Martin space: no mate with H > 1 >= H^sh is exhibited,
     r_1 > 0 is never shown to occur, and "not in Cert(f)" does not imply "not in cl Cert(f)". The shifted expansion
     and its transport are correct; the strictness claim should be OPEN (my toy computations, §4, support it).
   * (G4) Minor: Lemma 6.3(ii) omits the case w(k) = 0; Remark 4.9 says "iff" where only "if" is proved; Cor 3.3
     (c)=>(b) needs eps/||x_i|| (trivial); the "O(sqrt eps)" reading of Prop 8.4 needs ||a'-a||_1 = O(eps), which is
     not implied (the notes flag this as heuristic, the task list does not).
3. **Conjecture 7.5 is under-supported.** Two-piece mates over infinite contact sets (Remark 7.6, (P1)(c)) do exist:
   explicit construction in §5.2 (SKETCH, generic data). When the contact mass is split in a constant ratio they are
   already in Cert(f) (§5.1, PROVED); for a non-constant split they are natural defect candidates which need **no**
   approximation rates and no scale resonance, so the heuristic of §7.2 does not address them.
4. **Three-regime scheme (§8.7).** Not a proof, as the notes say. For the mates of §5.2 it can be completed (§5.4,
   SKETCH): the transfer regime is handled by one-sided decompositions that transfer *exactly* to the NA approximants.
   The obstruction met in §8.7 is quantitatively the non-Lipschitz modulus of x -> L*J_V(Lx); for finitely supported
   block carriers it only enters through nonzero d-coefficients, while for the multi-scale carriers of §8.7 it also
   moves the carriers' own values w'(k) (§5.5, HEURISTIC).
5. **Status of the goal.** Density of NA((c_0,p), l_2^2) remains OPEN. The notes claim neither a proof nor a
   counterexample; I agree with their bottom line, except for the overstatements in (G3) and Conjecture 7.5.
6. **Most valuable idea:** the averaging of finite certificates over a geometric ladder of scales (Theorem 6.8),
   combined with the lower semicontinuity of the certified fibre cl Cert(f) (Theorem 4.10 / Cor 4.11). See §6.

---------------------------------------------------------------------------------------------------

## 1. Verdict table

| Claim (task list) | Label in notes | Verdict | Key point |
|---|---|---|---|
| R1/R2 | PROVED | correct | Standard; support function r~_f = convex envelope of r_f; re-derived. |
| Global compactness (Preprint A Thm 2.1) | PROVED | correct | l_1 Brezis-Lieb splitting plus q*(A) >= A(xi)/q_0; D <= (s(t)-1)/(t q_0) -> 0. |
| R3 lower-limit theorem | PROVED | correct | Blaschke selection in compact Q, weak*-separation by c_0. |
| Finite/diagonal/mate versions | PROVED | correct | (c)=>(b) needs eps/||x_i|| (trivial). Remark 3.4 also true (damping argument). |
| Transitivity | PROVED | correct | Direct from Thm 3.2. |
| Exact certificate expansions | PROVED | correct | Re-derived; re-checked numerically in an independent consistent model. Radius inconsistency: see G1. |
| NA-scale criterion | PROVED | correct | Re-derived. Remark 4.9 "usable iff" is only "if". |
| Transport Theorem / lsc of cl Cert | PROVED | correct | Every step re-derived (G_n-truncation, tau_n-correction, uniform radius, Prop 4.8). |
| Known classes (R6); [Check] re-proved | PROVED | correct | Cor 4.12(i) is exactly the [Check] theorem as quoted. |
| Ranges l_2^d | PROVED | correct | Transport is linear in c; H uniform on the sphere of theta. |
| Shifted certificates; H<=1 not sharp | PROVED | correct with fixable gaps | Expansion and transport correct (identity checked to 1e-16). "Strictly larger classes" not shown (G3). |
| Theorem W | PROVED | correct | Uniform-in-J expansion verified line by line. |
| Theorem L and structure lemma | PROVED | correct | Minor omission w(k)=0 in Lemma 6.3(ii) (bound still holds). |
| Averaging (ladder) theorem | PROVED | correct with fixable gaps | Thm 6.8 correct (constants checked). Cor 6.9 needs C_m bounded below (G2). Cor 6.10(a),(b) proof gap via radius (G1). |
| Budget/excess identities | PROVED | correct | Identities checked to 1e-15. |
| Rigidity and one-sided linear decompositions | PROVED | correct | Prop 7.4 correct; fails for infinite K exactly as Remark 7.6 says; see §5. |
| Cross mechanisms and rates | SKETCH | correct with fixable gaps | Positive part = Cor 6.10(c) (conditional on H(c_t) <= 1+o(1)); the "iff" is heuristic; a single carrier costs c^2/(m^2 C_m) in H. |
| Engineering lemmas | PROVED | correct | Lemmas 8.1-8.3 verified (continuity of J_V, tail independence). |
| Limits of certificate engineering | PROVED | correct with fixable gaps | Inequalities correct; the "only O(sqrt eps) new structure" consequence is heuristic and is not an obstruction to engineering (§5.4). |
| Domination lemma and rotundity | PROVED | correct | p* is rotund; Lemma 8.5 holds for all y (evenness not needed). |
| Three-regime engineering scheme | SKETCH | unclear | Not completed (as admitted). Completed by the referee for one class (§5.4). |

---------------------------------------------------------------------------------------------------

## 2. Line-by-line verification (what was re-derived, and where hidden assumptions sit)

**2.1 R1/R2 (Props 2.1-2.2).** ||(f,g)|| <= 1 iff sup_theta p*(cos theta f + sin theta g) <= 1 iff p*(f+tg) <= s(t)
(t = tan theta). r~_f(x) = inf{sum r_f(y_j) : sum y_j = x} is the largest sublinear minorant of the positively
homogeneous even function r_f; linear g <= r_f iff g <= r~_f; Hahn-Banach gives the support function; |g| <= p
gives continuity. Correct. g(xi) = 0 for every mate (Remark 2.3) is correct.

**2.2 Thm 3.1 (global compactness).** I re-derived: t(g_n - g) = (A_n - A) + (L*W_n - k) - (f_n - f), so
t D = limsup ||A_n - A||_1; ||A_n||_1 - ||A_n - A||_1 -> ||A||_1 (finite set + small tail of A);
U*A_n -> U*A in norm; A(xi) = 1 - k(xi) >= 1 - s(1-q_0); hence tD <= s - q*(A) <= (s-1)/q_0. No uniqueness of the
normer is used (any normer works). Correct. The residual Thm 2.2 of Preprint A: lsc of z -> dist(z, C_d(f)) follows
from global compactness; continuity points of countably many lsc functions on the complete metric space S_{p*} form a
dense G_delta; correct.

**2.3 Thm 3.2, Cor 3.3, Thm 3.5.** Hausdorff limits of the C(f_{n_j}) inside the compact Q exist (Blaschke), are
convex (midpoints), and |h_C(x) - h_{C'}(x)| <= d_H(C,C') ||x||_infinity. A norm-compact convex set is weak*-compact
and is separated from an outside point by some x in c_0. Correct. In Cor 3.3, (a)=>(d) uses rho C(f_n) in C(f_n)
(convex, contains 0). Final step: g_n(x_n) = 0 at the norming point of f_n. Remark 3.4 (necessity with g_i/sqrt k) is
true: for (f, rho G) with rho < 1 the only adjoint-norming directions are +-e_1 (strict slack), so nearby NA operators
have norming directions near e_1, and rotating gives NA first rows. Correct.

**2.4 Facts A-F.** All correct. Comments: Fact E(ii) uses that R_m** maps bounded weak*-convergent sequences to norm
convergent ones (compactness of R_m; R_m**(B) lies in the norm closure of R_m(B)); Fact E(iii) needs only weak*
lower semicontinuity of N_m and uniqueness of J_m. In §5 I use the following "bidual" form of Fact D's converse:
*for every a with q*(a) = 1 and every z in B_{l_infinity} with z = sign a on supp a, the functional
f := a + L*J_V(L** xi), xi := q_0(z + U e), q_0 := 1/(1 + sum_m |R_m** (z+Ue)|_m), lies in S_{p*} with normer xi and
forced data (a, w, z)* (f(xi) = 1, p*(f) <= 1, p**(xi) = 1 since a(z + Ue) = 1 forces q**(z+Ue) = 1). PROVED; I use
it in §5.

**2.5 Lemmas 4.3-4.6, Prop 4.5.** Re-derived: |x + y| = |x| + sign(x) y + 2(-sign(x) y - |x|)_+; Psi(h) =
||h_perp||^2/(||e+h|| + 1 + <e,h>); block identity (1 - d s) Dw + s D omega = (1 + d s M/C) Dw + s h_perp (uses
1/C - 1 = M/C); box argument (c) needs |d s| <= 1/2; (d) uses C/Y <= 1 + 2|d s|M/C. Lemma 4.6: (1-delta)(1+delta/2)
<= 1 - delta/2 and sqrt(1+x) >= 1 + x/2 - x^2/8. All correct. Note that (c) is coordinatewise, so Prop 4.5 holds
with the coordinatewise radius as well (see G1).

**2.6 Prop 4.8, Lemma 4.7.** s(t) - s(rho t) = (1-rho^2) t^2/(s(t) + s(rho t)) >= (1-rho^2) min(t^2,|t|)/3;
for r_* <= |t| <= 1 each of eps, |t| eta is <= (1-rho^2) t^2/6; for |t| >= 1 the sum is <= (1-rho^2)|t|/3. Correct.

**2.7 Theorem 4.10 (Transport).** Checked: G_n is eventually every j in supp a; b'_n -> b in l_1 by dominated
convergence; on G_n, z_n(j) = sign a_n(j) = sign a_j = z_j, so tau_n -> b(zhat) = 0; b_n(zhat_n) = 0 because
a_n(zhat_n) = 1; ||b_n/a_n|| <= 2||b/a|| + |tau_n|; gaps and d_{n,m} converge because supp omega is finite and
w_{n,m} -> w_m coordinatewise with M_{n,m} = 1 - C_{n,m} -> M_m; R_m* w_{n,m} -> R_m* w_m in norm (adjoint of a
compact operator). Then Prop 4.8 with c' = rho c_n, delta = (1-rho^2)/2. Correct, and it needs neither NA nor any
engineering of the sequence. This is the key structural result of the notes.

**2.8 Prop 4.16 / Thm 4.17 (shifts).** The base identity
q*(a + tau b - tau^2 v) = 1 - tau^2 v(zhat) + tau^2 kappa_q(v) + Fl + nu Psi(...), v(zhat) = sum theta_m |zeta_m|/q_0,
is correct (I re-derived it and checked it numerically, error 7e-16, including contacts |z_j| = 1). The flip bounds
(I), (II) in Thm 4.17 and limsup kappa_{q,n}(v_n) <= kappa_q(v_theta) are correct (dominated convergence; z_n -> z
coordinatewise; v_n -> v_theta in l_1). Joint convexity of H^sh in (b, omega, theta) holds, so Cert^sh(f) is convex.
Correct. Example 4.18 computations are correct as computations; the conclusions drawn from them are not proved (G3).

**2.9 Theorem 6.2 (W).** Checked: D omega in l_2 since Phi <= lambda; discarding E_m(|sigma|) into the base costs
|sigma| q*(Delta_m) <= |sigma| T_m(|sigma|)(1 + M q*(R*w)/C) = o(sigma^2) uniformly in J; flips:
2(|sigma b_j| - |a_j|/2)_+ <= sigma^2 b_j^2/|a_j| 1[...] (from (x - y/2)_+ <= x^2/(2y)); conclusion with
rho(1 + 2 eta) <= 1. Correct.

**2.10 Lemma 6.3, Lemma 6.4, Thm 6.5 (L).** Correct. In Lemma 6.3(ii) the case w(k) = 0 (k not in P, sigma'_k
undefined) is not treated; from +-tau Omega(k) <= M + tau mu + tau^2/2 one gets |Omega(k) -+ mu| <= sqrt(2M), so the
stated bound still holds with gap(k) = M. Lemma 6.4: the extra flip cost on G is <= 2|sigma kappa||a_j| <=
4 sigma^2 |kappa||b_j| because the flip set forces |a_j| <= 2|sigma b_j|; coordinates outside G never flip
(|sigma kappa| <= 1/2). Theorem 6.5's direct proof uses Lemma 6.4 to compare with q*(a + sigma b) on a sigma-range
independent of t, so no radius is needed for the base: correct.

**2.11 Theorem 6.8 (averaging).** I re-derived the whole chain: convexity p*(f + s rho g_c) <=
(1/n) sum_i p*(f + s rho g_{c_{t_i}}); bound (A) for c_0 t_i >= rho|s|, bound (B) otherwise, sum of the "fine" t_i
< 2 rho|s|/c_0 (geometric ratio 1/2); Q = 2 rho^2 K/(c_0 n) <= (1-rho^2)/12; the two cases |s| <= s_0 and |s| >= s_0;
H(rho c) <= rho^2 max_i H(c_{t_i}) by convexity of H. Correct. I also checked the constant bookkeeping numerically
(worst case, every component saturating its bound): no violation over 150 random parameter sets (§4). Remark: only
the ladder scales t_1 2^{1-i} are used, so the hypotheses are needed only along geometric sequences (any ratio
beta < 1 works with 2 replaced by 1/(1-beta)).

**2.12 Cor 6.9.** Correct for finite I (see G2 for I = N). The one-sidedness is genuine: the lower bounds used
(Lemma 4.4(b) and nu Psi >= (tau^2/2) h/(1 + |tau| beta/nu)) only see tau^2 and |tau|.

**2.13 Cor 6.10.** (c) is correct as stated (conditional on H(c_t) <= 1 + o(1)); the radius estimate works even with
Definition 4.1 because omega^0 is fixed and finite. (a) and the second proof in (b): gap G1.

**2.14 Lemmas 7.1-7.2, Cor 7.3.** Identities re-derived and checked numerically (errors 1.8e-15, 8.9e-16).

**2.15 Prop 7.4, Cor 7.5.** Correct: the weighted sum of the two first-order coefficients equals
q_0 sum_{j not in supp a}(|b_j| - z_j b_j) + g(xi), forcing the kink sum to vanish; for supp a cup K finite,
b+ - b- in c_00 cap L*(V*) = {0}. For infinite K the statement (b) is not available, and §5 shows that it genuinely
fails there.

**2.16 Lemmas 8.1-8.3, Prop 8.4.** Correct. In Lemma 8.1 continuity of v -> L*J_V(v) at Lx' for I = N follows from
coordinatewise norm-to-weak* continuity of each J_m, compactness of each R_m and sum_m ||R_m|| < infinity.
Lemma 8.2: u_{k,m}(e_j) >= 1/(1 + ||U||) - delta_0 and y_j small because x' is in c_0. Prop 8.4(a),(b): direct.

**2.17 Lemmas 8.5-8.6.** p - f' >= lambda(p - f) and p + f' >= lambda(p + f) hold for every y, so the evenness
reduction is unnecessary. Rotundity: a face point h = A + L*W with h(xi) = 1 forces W = J_V(L** xi) (smoothness of
each |.|_m at R_m** xi != 0) and A = a (equality in A(zhat) <= ||A||_1 + ||U*A||, injectivity of U*). Correct.

---------------------------------------------------------------------------------------------------

## 3. Problems found

### 3.1 (G1) Two different certificate radii; proof gap in Cor 6.10(a) and Cor 6.10(b)

*Quote.* Definition 4.1: "radius r(c) := min{ ..., min over m ... of min( gap_m(omega_m)/(2||omega_m||_infinity), ...)}"
with gap_m(omega_m) := min_{k in supp omega_m} gap_m(k). Remark 4.9: "min_m min_{k in supp omega_m} gap_m(k)/(2|omega_m(k)|)
[first box violation of a block coordinate]". Proof of Cor 6.10(a): "Then r(c_t) >= min(t, ...) (radius at least t ...
from the box condition)", where c_t keeps exactly the k with |t omega_m(k)| <= gap_m(k)/2.

*Why it fails.* The box condition gives the coordinatewise radius r^cw >= t, but Definition 4.1's radius is
r(c_t) <= (min over kept k of gap(k)) / (2 max over kept k of |omega(k)|), which can be much smaller than t.
Failure scenario (one block, m = 1): let omega(k_0) = 1 at a coordinate with gap(k_0) = gamma_0 > 0, and
omega(k_i) = sqrt(g_i) at near-peak coordinates k_i = i (i >= 1) with gaps g_i = 2^{-2^i}. Then Sum lambda|omega| < inf
and Lemma 6.1(b) gives T(sigma) = o(sigma), so all hypotheses of Theorem W and of Cor 6.10(a) hold. For the proof's
c_t: every k_i with 4t^2 <= g_i is kept, so r(c_t) <= g_i/2 < c_0 t whenever some g_i lies in [4t^2, 2 c_0 t).
Discarding those k_i instead (to restore r(c_t) >= c_0 t) costs, at t_i slightly above g_i/(2c_0), at least
lambda_{k_i} sqrt(g_i) = lambda_{k_i} sqrt(2 c_0 t_i), and lambda_{k_i} sqrt(2c_0/t_i) -> infinity (lambda_{k_i} ~ 2^{-i}
while sqrt(t_i) ~ 2^{-2^{i-1}}), so (iv) p*(g - g_{c_t}) <= K t fails; discarding k_0 costs lambda_{k_0} = O(1). The bad
windows [g_i/(2c_0), lambda_{k_i} sqrt(g_i)/K] are wide in log-scale, so every geometric ladder of Theorem 6.8 meets them.
(In this example the conclusion is still true, by the direct proof of Theorem 6.2; the point is that the proof of the
O(sigma) extension, which has no other proof, is incomplete as written.)

*Fix (routine).* Define r^cw(c) with the block term min_{k in supp omega_m} gap_m(k)/(2|omega_m(k)|). Lemma 4.4(c) is
coordinatewise, so Lemma 4.4(d), Prop 4.5, Lemma 4.6, Prop 4.8, Thm 4.10 (finitely many coordinates) and Thm 6.8 hold
verbatim with r^cw; then Cor 6.10(a),(b) go through. Prop 8.4(b) holds for either radius.

### 3.2 (G2) Cor 6.9 for infinitely many blocks

The block step bounds H_m from N_m(W) <= s(tau) + eps tau^2 via sqrt(Y^2 + X^2) - Y <= delta := s(tau) - 1 + eps tau^2,
which gives X^2 <= delta(2Y + delta), i.e.
  H_m(omega_{t,m}) <= (1 + 2 eps)(Y/C_m) + (1/2 + eps)^2 tau^2 / C_m.
The last term is o(1) only if tau^2 = o(C_m) on the active blocks. For finite I this is automatic. For I = N one has
C_m <= ||Phi_m||_2 M_m = O(2^{-m}), and nothing in the hypotheses (r(c_t) >= c_0 t, kappa(c_t) <= kappa_0) prevents
active blocks with C_m << t^2. This is not an artifact: if C << tau, a block can stay admissible at scale tau with
||h_perp|| ~ tau/2 + C/tau, i.e. H_m ~ tau^2/(4C) >> 1. Either restrict to finite I (justified by Remark martin-tail of
Preprint B) or add the hypothesis "the set of active blocks is bounded independently of t". The sentence in §10
"everything also holds for I = N given (T4)" should be qualified accordingly.

### 3.3 (G3) "Shifts give strictly larger recoverable classes" is not proved

What is proved: H^sh(c) <= H(c) (take theta = 0), the shifted expansion, its transport, and the explicit optima
H^sh = h(b)/(1 + r_1) (pure base, if r_1 > 0) and H^sh = H r_2/(1 + r_2) (pure block; r_2 > 0 always).
What is claimed (row 7 of the summary, §4.5 title, §10: "give strictly larger recoverable classes (Example 4.18)"):
existence of recoverable mates that the H <= 1 theory does not cover. Missing:
1. *Existence of the mates.* Example 4.18 itself says "Whether such directions are actually mates depends on the global
   condition". The gauge gamma_f(g)^2 = sup_t (p*(f+tg)^2 - 1)/t^2 is in general attained at moderate t (see §4), so
   the local improvement does not by itself produce a mate with H > 1.
2. *r_1 > 0 is never shown to occur* (r_1 = (1-q_0)/q_0 - kappa_q(R*w) can be negative at every f for all the notes show).
3. *Cert(f) versus cl Cert(f).* Rigidity (Fact F(a)) shows that b is not in Cert(f) when a is in c_00; but what the
   unshifted theory recovers is cl Cert(f). H(c) is not an intrinsic function of the direction g_c: replacing one
   off-peak coefficient omega(k) by N coefficients on off-peak coordinates k_1..k_N with u_{k_i} close to u_k keeps g_c
   almost unchanged and divides that coordinate's contribution to ||D omega||^2 by about N. Whether such
   re-representations stay in C(f) is a rate question (§7.3 of the notes). So "outside cl Cert(f)" is open.
*Evidence (toy model, §4):* in a consistent finite-dimensional model with exact p* computed by an interior-point
method, pure block directions g = R*(omega - d w) have true local coefficient < H^sh < H in all 14 seeds, and the gauge
satisfies gamma^2 < H with H/gamma^2 between 1.22 and 3.79; H^sh/gamma^2 <= 1 in 11 of 14 seeds. So normalized mates
whose canonical block coefficient exceeds 1 do occur, and shifts usually certify them; in 3 seeds even the shifted
coefficient of the normalized mate exceeds 1 while the true local coefficient is smaller (shifts are not the last layer
either). The finite model has no rigidity, so it says nothing about Cert versus cl Cert in the Martin space.
*Recommended wording:* "the sufficient condition H <= 1 is relaxed to H^sh <= 1 (PROVED); whether this enlarges the
class of recoverable mates beyond cl Cert(f) is OPEN (finite-dimensional evidence supportive)".

### 3.4 (G4) Minor points
* Remark 4.9: "a certificate at f' is usable iff ..." -- Prop 4.8 is only a sufficient condition.
* Cor 3.3 (c)=>(b): the proof yields r~_{f'}(x_i) >= rho r~_f(x_i) - eps ||x_i||; apply (c) with eps/max_i ||x_i||.
* Lemma 6.3(ii): case w(k) = 0 (see 2.10).
* Prop 8.4 "Interpretation": needs ||a' - a||_1 and sum lambda |w' - w| to be O(eps), which p*(f' - f) = eps does not
  give (cancellations are allowed, as the notes say). The task list reports this consequence under "PROVED"; it is
  HEURISTIC. Moreover, §5.4 shows that recovery does not need large new certificate structure at f' at all when the
  one-sided decompositions of f transfer exactly; so Prop 8.4 is not an obstruction to engineering.
* §7.2 "Peaks with |u_{k,m}(xi)| >= c_1 > 0 only carry O(t/c_1) at scale t": Cor 7.3(b) bounds the deviation of peak k
  by O(t^2/alpha_{m,k}), and by Fact C alpha_{m,k} = lambda_{k,m}|u_{k,m}(xi)|/|zeta_m| - Phi_m(k)^2 M_m/C_m. So the
  component of g carried by peak k is O(t lambda_k/alpha_k), which is O(t |zeta_m|/c_1) only for peaks away from the
  threshold (alpha_k comparable to lambda_k |u(xi)|); finitely many near-threshold peaks with small k can carry more.
  Harmless as a heuristic, but the statement should say "far peaks".

### 3.5 Conjecture 7.5 (HEURISTIC) is not supported by the evidence given
The evidence offered is that a defect mate must switch between one-sided carriers that represent the same component
"up to O(t) ... at their own scale". §5 exhibits two-piece mates over infinite contact sets in which the two carriers
represent the same component **exactly** (b+ - b- = R_m* D with D a single block coordinate). They need no
approximation rates, so a scale-separation hypothesis does not prevent them, while their membership in cl Cert(f)
would require approximations of a restricted block vector v 1_{K_1} by off-peak block vectors at all scales (rates),
which is what scale separation tends to forbid. Hence Conjecture 7.5 is at best unsupported, and false if these mates
lie outside cl Cert(f) for some scale-separated T. This does not affect any PROVED result of the notes.

---------------------------------------------------------------------------------------------------

## 4. Independent numerical checks

All scripts in `/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/refA/`.

* `model.py`: a **consistent** finite model built from the dual side: a with q*(a) = 1, z = sign a on supp a and
  contacts |z_j| = 1 off supp a, e = U*a/||U*a||, xi = q_0(z + Ue); for each block, w with N_m(w) = 1, peaks P, alpha on
  P, zeta = pi_m (1 - q_0)(alpha + D^2 w/C); vectors u_k in S_{q*} with u_k(xi) = zeta(k)/lambda_k. Then f = a + L*w has
  normer xi and forced data (a, w) (f(xi) = 1 to 6e-16).
* `e1_e2.py` (300 models, 2 blocks): g_c(xi) = 0 to 1.4e-15 for random finite certificates; Prop 4.5 bound: 0
  violations; Lemma 7.2 base and block identities exact to 1.8e-15 and 8.9e-16.
* `e2_shift.py`: shifted base identity (with kink costs at contacts) exact to 7e-16; inside the flip radius,
  (decomposition cost - 1)/(tau^2/2) - H^sh = 0.11, 0.011, 0.0011 at |tau| <= 1e-2, 1e-3, 1e-4 (linear in tau, as
  Prop 4.16 predicts). Outside the flip radius large deviations occur (one model with |a_j| = 2.4e-4), as expected.
* `e4_avg2.py`: worst-case bound chain of Theorem 6.8 with the prescribed s_0, eta_0, n, t_1, over 150 random
  parameter sets (rho in [0.3, 0.99], K in [0.01, 100], c_0 in [0.01, 10], kappa_0 in [0.01, 1000], n <= 400) and
  s in [1e-4, 50]: no violation; the largest value of (bound - s(s))/s^2 is -2.4e-4.
* `pstar.py`: exact p* (log-barrier interior-point method for the SOCP
  min max(q*(h - L*W), N_m(W_m))); validated by p*(f) = 1 +- 6e-13 and never exceeding explicit decompositions.
* `e3_gauge.py` (single block, contacts present, pure block directions g = R*(omega - d w) with omega on two random
  off-peak coordinates; "true local coeff" = (p*(f+tg)^2 - 1)/t^2 averaged over t = +-1e-3; gauge^2 = max over 80
  values of t in +-[1e-3, 30]; H^sh = H r_2/(1 + r_2) from Example 4.18; seeds 9 and 11 were rejected by the model
  builder; no solver value ever exceeded an explicit decomposition bound):

  | seed | H | H^sh | true local coeff | gauge^2 | t at max | H/gauge^2 | H^sh/gauge^2 |
  |---|---|---|---|---|---|---|---|
  | 0 | 2.8631 | 0.8274 | 0.7227 | 1.0807 | -0.437 | 2.65 | 0.77 |
  | 1 | 0.8951 | 0.2824 | 0.2447 | 0.3156 | 1.26 | 2.84 | 0.89 |
  | 2 | 0.1216 | 0.0382 | 0.0319 | 0.0439 | -3.62 | 2.77 | 0.87 |
  | 3 | 0.3454 | 0.1236 | 0.0982 | 0.1811 | 0.569 | 1.91 | 0.68 |
  | 4 | 0.1993 | 0.0691 | 0.0522 | 0.0526 | 0.0239 | 3.79 | 1.31 |
  | 5 | 0.9923 | 0.2691 | 0.2524 | 0.2780 | 0.335 | 3.57 | 0.97 |
  | 6 | 0.0223 | 0.0063 | 0.0058 | 0.0183 | 3.62 | 1.22 | 0.34 |
  | 7 | 5.8567 | 1.9506 | 1.5024 | 1.6677 | -0.437 | 3.51 | 1.17 |
  | 8 | 0.3335 | 0.1107 | 0.0891 | 0.1601 | 0.741 | 2.08 | 0.69 |
  | 10 | 1.0124 | 0.3036 | 0.2741 | 0.3246 | -1.64 | 3.12 | 0.94 |
  | 12 | 0.2207 | 0.0752 | 0.0561 | 0.0772 | -0.741 | 2.86 | 0.97 |
  | 13 | 0.2061 | 0.0712 | 0.0645 | 0.0692 | 0.965 | 2.98 | 1.03 |
  | 14 | 0.8311 | 0.2562 | 0.2080 | 0.5453 | -0.257 | 1.52 | 0.47 |
  | 15 | 1.8541 | 0.5410 | 0.4991 | 0.9765 | 0.335 | 1.90 | 0.55 |

  Reading: in every seed true local coefficient < H^sh < H (shifts help, but are not the last layer); the gauge is
  usually attained at moderate |t| (not as t -> 0); H/gauge^2 > 1 always, so g/gauge is a mate whose canonical block
  coefficient exceeds 1 (between 1.22 and 3.79); H^sh/gauge^2 <= 1 in 11 of 14 seeds. Caveat: the model is finite
  dimensional (no rigidity Y cap c_00 = {0}), so it cannot distinguish Cert(f) from cl Cert(f) in the Martin space.
* `e5_twopiece.py`: the two-piece contact mate of §5.2 in a finite model (k_0 with w(k_0) = 0, u_{k_0}(xi) = 0,
  z = sign u_{k_0} off supp a). For g = beta + c u_{k_0} 1_{K_1} with K_1 = odd coordinates: the side+ decomposition
  costs ~0.0000 t^2 for t > 0 but about 0.02|t| (first order) for t < 0; the side- decomposition costs 0.0067 t^2 for
  t < 0 but about 0.02|t| for t > 0; the true p* is second order on both sides (coefficients 0.0000 and 0.0018).

---------------------------------------------------------------------------------------------------

## 5. Two-piece mates over infinite contact sets (referee's additions)

Setting: finite I; a in c_00 with F := supp a; K := {j notin F : |z_j| = 1} possibly infinite.

### 5.1 Constant splitting gives certificates. PROVED.
**Proposition.** Let g in C(f) have one-sided linear decompositions (b+, Omega+) on [0, tau_0] and (b-, Omega-) on
[-tau_0, 0] as in Prop 7.4, with Omega+-_m = omega+-_m - d+-_m w_m, omega+-_m finitely supported and vanishing on P_m.
Put v := b+ - b- (= L*(Omega- - Omega+)). If there is theta in [0,1] with b+_j = theta v_j for all j in K, then
g is in Cert(f).
*Proof.* As in Prop 7.4(a): supp b+- is in F cup K, sign b+_j = z_j and sign b-_j = -z_j on K, b+-(zhat) = 0 and
<Omega+-_m, zeta_m> = 0. One-sided second-order bounds: on its side, q*(a + tau b+-) >= 1 + nu Psi(tau U*b+-/nu) >=
1 + (tau^2/2) h(b+-)/(1 + |tau| beta/nu) (flip and kink terms are >= 0), so h(b+-) <= 1; Lemma 4.4(b) on one side gives
H_m(omega+-_m) <= 1. Let c := (1-theta)(b+, omega+) + theta(b-, omega-). Its base part beta := (1-theta) b+ + theta b-
satisfies beta_j = (1-theta) theta v_j + theta(theta - 1) v_j = 0 on K, vanishes off F cup K, beta(zhat) = 0, and
||beta/a|| < infinity (F finite). Its block parts are finitely supported, vanish on the peaks, and
d_m = (1-theta) d+_m + theta d-_m by linearity. So c is a finite certificate, g_c = (1-theta) g + theta g = g, and
H(c) <= max(H(c+), H(c-)) <= 1 by convexity of H. Hence g in Cert(f). QED.
(For finite K, rigidity gives v = 0, hence b+ = b- and any theta works: this recovers Prop 7.4(b) for finitely
supported block parts. For infinite K rigidity is unavailable and the constant-ratio hypothesis is what replaces it.)

### 5.2 Explicit two-piece mates with arbitrary splitting. SKETCH (existence step uses generic data).
Fix a block m and k_0, and put u := u_{k_0,m} (in S_{q*} cap Y, so u is not in c_00).
1. *Base data.* Choose a finite F and a with supp a = F, sign a_j = -sign u_j on F, and z with z = sign a on F,
   z_j = sign u_j on supp u \ F, such that u(zhat) = 0. Indeed u(zhat) = Delta_F + <U*u, e> with
   Delta_F = sum_{j notin F}|u_j| - sum_{j in F}|u_j|; choose F with |Delta_F| small (|u_j| -> 0), then the magnitudes
   |a_j| so that <U*u, U*a>/||U*a|| = -Delta_F (one scalar equation; solvable when the numbers sign(u_j)(UU*u)_j,
   j in F, are not all of one sign and |Delta_F| is small). This genericity is the only unproved point.
2. *The functional.* By the bidual form of Fact D (2.4), f := a + L*J_V(L** xi) with xi := q_0 zhat is in S_{p*} with
   forced data (a, w, z). It is not norm attaining (|z_j| = 1 on the infinite set supp u \ F, so z is not in c_0).
   Since u(xi) = 0, Fact C gives w_m(k_0) = 0: k_0 is off-peak with gap M_m.
3. *Mates.* Let K' := supp u \ F (contained in K), any K_1 in K', K_2 := K' \ K_1, c > 0 small, v := c u,
   D := (c/lambda_{k_0,m}) e_{k_0} in block m (so R_m* D = v and d(D) = <D_m w_m, D_m D>/C_m = 0), and
   g := v 1_{K_1} - (v 1_{K_1})(zhat) a   (so g(xi) = 0).
   Side +: f + tau g = (a + tau g) + L*w; for tau > 0 the coordinates in K_1 are contacts used with the free sign, so
   q*(a + tau g) = 1 + nu Psi(tau U*g/nu) for small tau (no flips; first order g(zhat) = 0).
   Side -: f + tau g = (a + tau (g - v)) + L*(w + tau D); g - v = (multiple of a) - v 1_F - v 1_{K_2}; for tau < 0 the
   coordinates in K_2 are contacts used with the free sign; (g - v)(zhat) = -c u(zhat) = 0; and
   N_m(w_m + tau D) = M_m + sqrt(C_m^2 + tau^2 c^2/m^2) because D_m w_m(k_0) = 0 (box: |tau| c/lambda_{k_0,m} <= M_m).
   Both one-sided decompositions have second-order coefficients O(c^2); for c small, g is in C(f) (crude bound for
   |tau| >= tau_0).
4. *Status.* If K_1 = K' or K_1 = empty (more generally, constant theta), g is in Cert(f) by 5.1. If K_1 and K_2 are
   both infinite, the contact mass is split non-constantly (theta = 1_{K_1}); Prop 7.4(b) and 5.1 do not apply, and
   I see no way to put g in cl Cert(f) without approximating v 1_{K_1} (modulo span{e_j*: j in F} and certificate
   block vectors) by off-peak block vectors with radius >~ error at all scales. **OPEN; these are the cleanest
   candidates for Def(f), and they answer (P1)(c)/Remark 7.6 affirmatively** (Y does contain vectors with the
   required sign pattern on an infinite contact set, because z can be chosen to match sign u).

### 5.3 Consequence for Conjecture 7.5. HEURISTIC.
See §3.5: exact (scale-free) carrier relations exist; Conjecture 7.5 must either exclude them or be withdrawn.

### 5.4 These mates are recoverable along engineered NA sequences. SKETCH.
Fix rho < 1 and the mate g of 5.2 (any K_1). Choose a small t_m > 0, then N' so large that
eps_{N'} := c ||u 1_{(N', infinity)}||_1 <= (1 - rho^2) t_m/12, and let
* a'' := normalization of a + sum_{j in K_1, j <= N'} eta_j z_j e_j* with eta_j >= 2 t_m |v_j| (tiny masses on the
  K_1-contacts, Lemma 8.3(b)), with one extra degree of freedom in the masses used to enforce u(x'') = 0 exactly
  (one scalar equation; generic implicit-function argument);
* z'' := z on [1, N'], z'' in c_0 with |z''_j| < 1 beyond N'; x'' := z'' + U e''; f'' := grad p(x'') (NA, Fact D).
Then f'' -> f as t_m -> 0 (a'' -> a, x'' -> zhat weak*, L compact, J_V norm-to-weak* continuous), w''_m(k_0) = 0,
hence d''(D) = 0 and R_m* D = v **exactly** at f''. Put g'' := v 1_{K_1 cap [1,N']} + s a'' with s chosen so that
g''(zhat'') = 0 (g'' -> g). Then:
* for tau in [-t_m, tau_0]: f'' + tau rho g'' = (a'' + tau rho g'') + L*w'' has no flips (signs agree on the masses for
  tau >= 0, masses dominate for tau >= -t_m), zero first-order term, second-order coefficient rho^2 h''(g'') < 1;
* for tau in [-tau_0, -t_m]: f'' + tau rho g'' = (a'' + tau rho(g'' - v)) + L*(w'' + tau rho D); on K_2 cap [1,N']
  (contacts of f'') the sign is free, on K_1 cap [1,N'] the base part is a multiple of a'' only, the tail
  -v 1_{(N', infinity)} sits at non-contacts and costs <= 2 rho |tau| eps_{N'} <= (1 - rho^2) tau^2/6, the first-order
  term is -c rho tau u(zhat'') = 0, and the block cost is second order with coefficient rho^2 c^2/(m^2 C''_m);
* for |tau| >= tau_0: the slack (Lemma 4.7), since f'' -> f and g'' -> g.
So rho g'' is in C(f''), (f'', rho g'') is in NA, and (f'', rho g'') -> (f, rho g). This completes the three-regime
scheme of §8.7 for this class: regime (ii) is covered by decompositions that transfer exactly (finitely many contacts
plus one block coordinate frozen at w''(k_0) = 0, so that the block vector R_m* D does not depend on w''), and regime
(iii) by tiny masses on the contacts.

*General form (SKETCH).* The same argument applies to any g in C(f) with a in c_00 and one-sided linear decompositions
(b+, Omega+), (b-, Omega-) as in Prop 7.4 whose block parts Omega+-_m = omega+-_m - d+-_m w_m have finitely supported
off-peak omega+-_m and **equal d-coefficients**, Delta d_m := d-_m - d+_m = 0 for every m. Then v := b+ - b- =
sum_m R_m*(omega-_m - omega+_m) does not involve w, and at the approximants Delta d''_m = 0 is the single linear condition
ell_m(xi'') = 0 with ell_m := sum_k Phi_m(k)(omega-_m - omega+_m)(k) u_{k,m} (off-peak values are
w''(k) = C'' m u_{k,m}(xi'')/(Phi_m(k)|zeta''|)), which the masses can enforce; masses go on the contacts used by
b+ (for tau < 0 the contacts used by b- carry the same sign as these masses, so nothing flips). Conclusion: (f, g) is in
cl NA. Constant-ratio splitting is not needed here, so this covers the non-constant splits of §5.2 that are the
candidates for Def(f).

### 5.5 Where engineering really breaks. HEURISTIC.
If the side-minus block carrier has d != 0, then R_m*(D - d w''_m) involves R_m* w''_m, and the error
||R_m*(w''_m - w_m)|| caused by a perturbation of size t of x'' is, by Fact C, of order
t * #{off-peak k : Phi_m(k) >~ t} + sum_{Phi_m(k) <~ t} Phi_m(k) (off-peak values move by ~ t/Phi_m(k), saturating at
O(M)). At points with infinitely many off-peak coordinates (generic in the sense of Preprint A's Remark "Non-attaining
examples") this is not o(t),
so it is not absorbed by the slack (1 - rho^2) t^2 at scales ~ t. This is the quantitative content of the "re-tuning
to precision o(t_1^2)" problem of §8.7: x -> L*J_V(Lx) is not Lipschitz. For finitely supported carriers the damage is
confined to the d-terms, and the safe carriers are those whose contribution does not involve w'' (equal d-coefficients
on the two sides, e.g. coordinates frozen at w'' = 0). For the multi-scale cross mechanisms of §8.7 the carriers
themselves sit at coordinates with Phi_m(k) ~ t, whose values w''(k) move by O(1), so the §5.4 device does not apply.

---------------------------------------------------------------------------------------------------

## 6. Most valuable idea, and recommendations

**Most valuable idea.** Theorem 6.8: average finite certificates over a geometric ladder of scales. By convexity of p*,
at each scale s only the O(1) "too fine" certificates contribute an O(s) error each, and these errors are geometrically
summable, costing O(s^2/n). Hence a mate that is, at every small scale t and on one side only, a finite certificate of
radius >~ t up to an O(t) remainder lies in cl Cert(f); and by the Transport Theorem cl Cert(f) is lower semicontinuous
along every sequence f_n -> f, so such mates are recovered with no engineering at all. Together these turn the
multi-scale density problem into a single, scale-by-scale, one-sided O(t)-approximation question about the defect
C(f) \ cl Cert(f).

**Recommendations.**
1. Adopt the coordinatewise radius (G1), restrict Cor 6.9 to finite I or bounded active blocks (G2), and downgrade the
   "strictly larger"/"not sharp" claims to OPEN (G3).
2. Replace Conjecture 7.5 by the concrete test of §5.2: decide whether g = v 1_{K_1} - (v 1_{K_1})(zhat) a lies in
   cl Cert(f) for K_1, K_2 both infinite. A "yes" needs approximation rates for restricted block vectors; a "no"
   exhibits a nonempty defect at a non-NA point (which §5.4 nevertheless recovers).
3. Develop §5.4 into a general engineering lemma: one-sided linear decompositions built from contacts and finitely many
   off-peak block coordinates with w = 0 transfer exactly to NA approximants. The remaining issue is block carriers
   with d != 0 (§5.5); test whether every one-sided decomposition can be re-based on d-neutral carriers by zeroing
   w'' at the carrier coordinates (Lemma 8.2 does this for chosen coordinates).
4. A uniform-remainder version of Proposition 4.16 would extend Theorem 6.8 to shifted certificates (Remark 4.19).
