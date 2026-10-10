# U3-ref part 2 — Part 2 of U3: Lemma D', Proposition FZ, Corollary FZ, Lemma A

Checked against: Y1 notes (classification R/G, Lemmas 3.1-3.5, source definitions (U1)-(U3), (L1)-(L3)), V1 Lemma D, Lemma S(a),
shift patterns and c_pi (V1 2.5), V2 Lemma 3.1, Def. 3.2, Theorem C1, Master Theorem III' (V2-ref), def:SLD, (T-d), V4 Prop. 5.1.

## 1. Lemma D'.  Verdict: CORRECT (immediate).
At a clean w every coarse carrier is in class R or class G (pigeonhole).  A class-R peak is (U1) (and (L1) if rho >= 1 + u), a
class-G anti-type peak is (U2), a class-G swallowing-type peak with rho >= 1 + u is (L2).  So "no upper source" forces every coarse
peak to be class-G swallowing type (all of them, not only those with rho >= 1 + u), and "no lower source" forces every coarse peak with
rho >= 1 + u to be class-G anti-type; existence of such a peak is V1 Lemma D.  Correct.

## 2. Proposition FZ.  Verdict: CORRECT (any admissible T, any diagonal U).
Re-derived.  For diagonal U, (Ue)_j = s_j^2 a_j/nu, so zhat = Phi(a) on F and = z off F; Phi(a)_j = sigma_j(1 + s_j|b_j|) lies in the open
sigma-orthant, so <Phi(a_0), Phi(a_1)> > 0.  Two non-zero vectors that are not positively proportional are strictly separated by a
linear functional (independent: dual basis; dependent: they would be opposite, impossible here).  y(zhat(a)) = <y, Phi(a)> for y
supported in F; |u(zhat) - y(zhat)| <= q*(u - y) since q**(zhat) <= 1; (T-d) gives carriers of every block, arbitrarily far out, in
any q*-ball.  The four inequalities defining eta are strict.  Correct.
The parenthetical remark is even better than stated: Phi(a_1) = lam Phi(a_0) together with ||b(a_1)||_2 = 1 is a quadratic equation
in lam with the root lam = 1, so at most ONE a_1 != a_0 has Phi(a_1) positively proportional to Phi(a_0).

## 3. Corollary FZ.  Verdict: CORRECT for the stated class (aligned rows); Consequence (a) OVERSTATED (precision P2.1).
Proof re-derived: the flipping carriers k_i (val(a_0) >= eta/2, val(a_1) <= -eta/2) are, for large i, exactly swallowed with z = +1 on
S_{k_i} (hypothesis), hence class G (room 0) anti-type peaks at f_{a_1} with nu -> infinity (Phi_{k_i} -> 0, threshold of f_{a_1}
fixed), margin ~ q_0 eta/2: (U2) at every clean w of every level >= k_i; the non-flipping carriers give (L2).  So (SP_w) at every
clean w of large level, I_sh = {}, (R5) forces delta = 0, viol >= ||delta||_1, rho^sh >= 1 (V2-ref: "(SP_w) => rho^sh >= 1"), and
Master Theorem III' (V2-ref) gives f_{a_1} in Rec (F finite).  Correct.
(P2.1) Consequence (a) says "(C*) is NOT open in any fixed-z fibre".  What is proved is this for (C*) rows satisfying the hypothesis of
the corollary (all but finitely many carriers of EVERY block exactly swallowed with the sign of their value).  For a general (C*) row the
argument shows only that the SOURCE-DEFICIENT blocks acquire both sources at f_{a_1}: by Lemma D' every robust coarse peak of a deficient
block is class G of one type, so the flipping family turns into the other type at f_{a_1} (and a carrier whose room is robust at the
clean sub-windows of f_{a_1} is class R, a source of both kinds).  Blocks that HAVE both sources at f_{a_0} through carriers of both
types may lose one type at f_{a_1} (their flipping family can consist of anti-type carriers and their non-flipping family of
swallowing-type ones; then f_{a_1} has only (L2) from these families), so (C*) could reappear with another deficient block.  Read (a)
as "aligned (C*) rows are isolated in their fixed-z fibre (up to at most one other point)".  No other statement depends on (a).
Consequence (b) is correctly labelled (PROVED only for (BT) rows of the fibre, HEURISTIC otherwise).

## 4. Lemma A (one block: shifted exact data <=> Omega-coherence).  Verdict: CORRECT, with a precision of statement (P2.2).
Necessity = Lemma S.  Sufficiency re-derived: d is linear, d(e_k) = Phi_k^2 w(k)/C, so d(gamma) = Delta is solvable on Omega iff some
k in Omega has w(k) != 0; with v := R^*gamma - Delta psi, b^+ := chi v 1_K + beta, b^- := b^+ - v, side admissibility at a contact j holds
for EVERY chi_j in [0,1] iff z_j v_j >= 0 (chi_j = 0 or 1 included), and at a free j off F iff v_j = 0.  Both pairs represent
h = b^+ + R^*(omega^+ - d(omega^+) w) (direct computation).  Correct.
(P2.2) The hypothesis "omega-differences chosen so that psi-terms on Sigma(omega) are z-signed" should read: "v = R^*gamma - Delta psi
is z-signed at the contacts and vanishes at the free coordinates of Sigma(omega) \ F".  In the Reading, "psi is z-signed at every
coordinate whose owner has w != 0" needs the owner to be NON-NEGLIGIBLE in V4's sense (|w(o)| >= 2 tau_o, V4 Lemma 4.1' /
Prop. 4.2'); for nearly neutral owners dominance can fail (these are V4's dead zones).  The Reading is informal and not used later.
The multi-block remark (coordinates owned by carriers of UNSHIFTED blocks are dead zones for the shifted blocks) is correct and is the
structural core of the multi-block part of (S1).
