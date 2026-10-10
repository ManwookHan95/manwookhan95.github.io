# V3 referee, part 4: Theorem A, Corollary 4.2, Theorem M_inf, (O4-box), residual list, corrections

## Theorem A (fixed d-neutral data, no cushion sparsity). CORRECT with the (ND') fix; one simplification.
(1) re-derived: for omega in c_00(L_0 cap Q_m), d^{(y)}_m(omega) = (m q_0^{(y)}/sigma^{(y)}_m) sum_k Phi_m(k) val_k omega(k)
(lem:threshold at f_y: Phi^2 w^{(y)}(k)/C^{(y)} = m q_0^{(y)} Phi(k) val^{(y)}_k/sigma^{(y)}_m), so d^{(y)} = c^{(y)}_m d on these
vectors, Delta d^{(y)} = 0, and b^+ - b^- = sum_m R_m*(omega^- - omega^+) is the consistency relation at both rows; G_y(xi_y) =
b^+(xi_y) = b^+(xi_y - xi) = O(eps_e) (b^+(xi) = g(xi) = 0; lem:algebra at f_y kills the block terms). Precision:
p*(g - g_y) = O(eps_e log(e/eps_e)) (normer change of w), not O(eps_e); harmless. (2) |a + Da| >= yW on F (and on F_0 for small y),
so W <= lam|a^{(y)}|/y <= 3|a^{(y)}|/t for t <= y/4. (3), (4) re-derived (Lemma R2 for the scaled data rho_1(b, omega) so that
Gamma_w <= 2; Cor 2.4 + lem:slack(a) above c_flat T; Y3 Theorem 2.1 at f_y with factor rho/rho_1). OK.
Simplification: |b^theta| can be dropped from W. Neither Lemma R2 (side parts only) nor Y3 Theorem 2.1 (raises b^theta-support
internally) uses it; W := (sb^+)_- + (sb^-)_+ suffices (smaller W makes (RR_W) weaker).

## Corollary 4.2 ((LSC-trunc)). CORRECT, and in fact immediate: (f, rho g) in cl NA for all rho < 1 implies (LSC-trunc) at (f, g),
because NA first rows have finite base support (prop:smooth(c)) and lem:pair.

## Theorem M_inf (reduction). CORRECT as a reduction: Lemma 2.3 at the base row f^ex_j plus the triangle inequality
p*(f^ex_j + lam r rho g) <= s(lam rho r) + p*(f^ex_j - f) gives (a) of Theorem 2.5 with eps'_j + p*(f^ex_j - f) (divided by lam);
(b)-(e) are hypotheses. The admissible support-usage constant C (instead of 3) only forces c_flat <= 1/(4C).
"Consequence (SKETCH)": plausible, NOT verified; points that must be checked when written:
(i) VP has to be applied at f^ex_j (not at f) and must preserve the values of every carrier entering the exactified cones of
    Y1/Y2/Y4; there L_0 = L_0(j) grows with the level, and the VP constants C_0(j), F_0(j) (conditioning of Lambda on L_0(j)) are
    f-DEPENDENT RATES. They are absorbed only if log C_0(j) = o(n^w_{l_j}) (depth m_j ~ (1/eps)(2n_j + log C_0(j)) must fit in the
    window): this is a new "exactness versus scale"-type condition, not automatic for a fixed design.
(ii) (ND') at f^ex_j for growing L_0(j), and (RR) at f^ex_j (pulls/banks add support coordinates).
(iii) Z4 Theorem A concerns INFINITELY many swallowed carriers; "under (B_fin)" it reduces to R1/RS, so its listing is either
    vacuous or needs (O4-box) (B infinite: U_B need not be in l_1, bounded switching fails). Remove it from the list or qualify.
So: Theorem M_inf PROVED (reduction); transport of Y1 Master Theorem / Y2 Theorem Y to infinite F: SKETCH with gap (i).

## 4.4 (O4-box). SKETCH/OPEN as labelled; the numerical threshold "max_{j<=N} Bx(j)/|a_j| = o(N^2)" is a heuristic estimate.

## Residual list 4.5 and Section 6 corrections. Accurate, with these precisions:
- (E1) is relative to the design: for every fixed mu there are mu-thin f (e.g. |a_s| = mu_s^s on the active set), so (E1) cannot
  be removed by choosing mu faster. Removing those coordinates from F instead of raising costs sum|a_s| over the active set,
  ~ y^{1+o(1)} for mu-thin profiles, not o(y^2): no cheap alternative.
- (E4): (H3-inf) is now covered (part 3, Improvement 2); (ND') failure is a genuine residual (second-order value drift can collapse a
  d-neutral block cone).
- Section 6 (3): "Y3 Theorem 3.5 superseded" is accurate only on the overlap; Theorem 3.5 / Y3_ref Prop 3.4 still cover mu-thin
  d-neutral monochromatic support swallowing, which RS does not.
- Remark 3.5(e), second clause, is an OVERCLAIM: lem:martintail transfers DENSITY for p_N (infinitely many N) to density for p; it
  does not transfer "f in Rec" for an individual first row of p_N to first rows of Martin's p (different dual spheres; Sections
  7-8 assume I finite). Correct reading: RS-type results feed Lemma Z for each N; density for p would follow only from Lemma Z
  (for all f) for infinitely many N with one N-free design.
- Remark 3.5(a) in V3_part3 says the raise has l_1-mass "~ T_j (FIRST order)": it is y m_B(y), ~ kappa y^2 for critical and between
  y^2 and O(y) for super-critical profiles (V3_notes has it right).
