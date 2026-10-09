# P2 referee — part 4: Cor 2.3, Remark 2.4, Lemmas 4.1-4.2, Prop 4.3

## Cor 2.3 (a). CORRECT WITH FIXABLE GAP.
Data check: b+ = g, omega+ = 0; b- = g - v, omega- = (c/lambda_{k0}) e_{k0}; R_m* omega- = v; d- = Phi_{k0}^2 w(k0) c/(lambda C) = 0 = d+;
on K: b+_j = v_j 1_{K1}(j), b-_j = -v_j 1_{K\K1}(j), so the contact signs hold iff v is z-signed on K (built into A_referee 5.2).
Gap: "P1 Prop 2.3 shows one-sided admissibility for small c" is a statement about P1's specific example (F = {1}). For the general
A_referee 5.2 setting the analogue (no flips on the finite F for |tau| <~ min|a_j|/|b_j| ~ 1/c, contacts used with the free sign,
Hilbert term O(c^2 tau^2), block N = M + sqrt(C^2 + tau^2 c^2/m^2), and g in C(f) for small c by the crude bound) is routine but must be
written; it is NOT literally P1 2.3. Also the EXISTENCE of such data in general is still A_referee's generic SKETCH; for P1's T it is
PROVED (P1 2.1-2.3). With these remarks: g in Ls(f) for every such mate.

## Cor 2.3 (b). CORRECT WITH FIXABLE GAP (missing hypothesis).
The first sentence ("every g in E_u with mu+ <= inf theta, mu- >= sup theta and rho^2 max(...) < 1 has (f, rho g) in cl NA") omits
g in C(f). Thm 2.1 uses g in C(f) (Lemma 1.4, |tau| >= T_0), and rho^2 kappa < 1 does NOT imply it (h only sees ||P_{e-perp}U*b||,
and U* is compact: a large contact mass far out has small h but large q*). This is exactly P1-referee's correction (C4), which the
notes cite ("with P1-referee's sharpening") but did not implement. Fix: "every g in E_u cap C(f) with ...".
The slab statement is correct: P1 6.2 gives slab in C(f) and one-sided admissible explicit decompositions with mu+- = inf/sup theta
(d+- = 0 since w_1(2) = 0; signs (theta_j - mu+)u_j >= 0 >= (theta_j - mu-)u_j on K'), so Lemma 1.7 gives kappa <= 1 and Thm 2.1
gives g in Ls(f). The explicit defect mates g_{K1} (P1 2.4, c small) lie in the slab. So: P1's explicit defect mates ARE in Ls(f)
(PROVED), confirming that P1's Def(f) != empty is a defect of the INTRINSIC mechanisms only.

## Cor 2.3 (c). CORRECT (direct from Thm 2.1 + Lemma 1.7). "Complete class of exact-resonance switching mates" is descriptive only.

## Remark 2.4 (shifted two-piece data). First sentence: plausible SKETCH. Second sentence ("would give f in R"): HEURISTIC/OPEN.
(i) Extension to shifts tau^2 theta^sigma_m w'_m: I checked the domination claim coordinate by coordinate. Window contacts with
masses: if the shift is cheap at f (v_theta,j of sign -z_j), the term -tau^2 v'_j has the sign of the mass a'_j (no flip); if it is
expensive at f (kink 2tau^2|v_j|), the flip cost at f' is <= 2tau^2|v'_j|. Far flipped contacts and the cut-off beyond N'' cost at most
2 tau^2 ||v' 1_{(N,inf)}||_1 = o(1) tau^2. So limsup kappa_q' <= kappa_q holds along the construction; with uniform convergence on the
fixed range |tau| <= T_0 the extension is plausible. Not written; SKETCH is the right label.
(ii) "Combined with P1 6.1 this would give f in R": P1 6.1 only proves g in E_u and that LIMITS mu+- of the carrier coefficients
bracket theta(g). It does NOT show that optimal decompositions are asymptotically shifted two-piece decompositions with H^sh <= 1;
P1's own remark says peaks, level shifts and free coordinates may contribute O(t^2) to the costs, and P1-referee (C1) shows the
sharp second-order invariant at such points involves transfer-peak rebalancing (Gamma_w <= H^sh), which is not of shift type.
The assertion "the limits mu+- satisfy only SHIFTED second-order bounds H^sh <= 1" is unproved. So "f in R at P1's example" stays OPEN.

## Lemma 4.1 (replication identity). CORRECT; the "Consequence (deep replication)" is WRONG in its O(theta) form (fixable).
G(c) = c^2(1 - rho_W) - (1-c)^2 S_P: G(C') - G(C) = sum_Ch Phi^2 (w'^2 - w^2) re-derived from C^2 = sum Phi^2 w^2 with w = C sgn r on W_off
and |w| = 1 - C on W_P (Lemma 1.1); 1 - rho_W >= sum_P Phi^2 M^2/C^2 > 0; G' >= 2c(1 - rho_W) on [0,1]; the w'-w formulas and the l_1
bound are right (||u_k||_1 <= q*(u_k) = 1). Two corrections:
(4.1a) "sum_{Phi_m(k) < theta} lambda_k <= 2 m theta" is false for admissible T: Lemma B gives no lower bound on q*(T e_{k,m}), and any
coordinatewise rescaling T e_{k,m} -> c_{k,m} T e_{k,m} (0 < c <= 1, sup attained) is again admissible. Example: Phi_m(k) = 2^{-m-j^2}
for k in [j^2 - j, j^2) (j >= 2), Phi_m(k) = 2^{-m-k} otherwise (admissible: 2^{-m-j^2} <= 2^{-m-k} for k < j^2). At theta_j = 1.01 * 2^{-m-j^2}:
sum_{Phi < theta_j} Phi_k >= j 2^{-m-j^2} ~ theta_j sqrt(log2(1/theta_j)); exact computation (P2Aref_work/lemma41_log.py, m = 1):
ratio sum/theta = 4.7, 7.9, 11.9, 15.8, 20.8 for j = 3, 6, 10, 14, 19 (the claim would give <= 2). The correct general bound is
sum_{Phi_k < theta} Phi_k <= sum_k min(theta, 2^{-m-k}) <= theta (log2(1/theta) + 2), and similarly sum_{Phi<theta} Phi^2 <=
theta^2 (log2(1/theta) + 2). So deep replication to depth theta costs O(theta log(1/theta)), not O(theta) (harmless for 4.4: replace
theta by theta/log(1/theta)).
(4.1b) c_f also depends on rho_W through g_0 (not only on m, M, C).

## Lemma 4.2 (retuning feasibility). CORRECT for moves y in l_inf(G) (weak*-compact ball); for moves in c_0/c_00 (needed so that z'
stays in c_0 and f' is NA) the reachable set is a dense convex subset of the same compact set, so "iff" holds for the relative
interior only, and the radius statement with strict inequality max|delta_k| < A r_W(G). Trivial fix. The resonance remark is right
(and it is precisely what invalidates Thm 3.4 (iii), part 3).

## Prop 4.3 (abstract scheme). CORRECT WITH FIXABLE GAP.
Lemma 1.5 with Q = 1 - 2delta and J >= 4kappa/delta gives the bound (1 - delta) on |t| <= T_0. But Lemma 1.4 also needs
p*(g' - rho g) <= (1 - rho^2)T_0/6, and the proof only has p*(g' - rho g) <= 2kappa s_1/J + eta <= delta s_1/2 + eta. Since s_1 is only
assumed <= T_0, this fails when delta > (1 - rho^2)/3 ("once eta and s_1 are small" is not implied by the hypotheses). Fix: add
s_1 <= eta to the hypotheses (natural), or require J >= max(4kappa/delta, 24 kappa/(1 - rho^2)).
