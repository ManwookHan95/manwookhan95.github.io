# Referee report on Y3 (Round 6): infinite base support — non-sparse support swallowing, F = N, (LSC-trunc)

Refereed: r6/Y3_notes.md (and Y3_part1..3.md, Y3_notesA..C.md, scripts Y3_work/check_testpoint.py, check_Dsharp.py, both re-run
and reproduced), against the note paper/martin_density_note.tex (Sections 1, 7, 8: def:twopiece, prop:onesidedupper, thm:onesided,
prop:lowerbound (block test), def:engineered, lem:approxfacts, lem:F1, lem:anchor, lem:scrambling, thm:engineered, def:SLD, thm:SLD,
lem:budget, lem:suplevel, lem:box, lem:switchbudget, lem:split, lem:flip, lem:boundedfree, lem:modswallow, lem:badpeaks,
lem:exactswitch, lem:windowtwopiece, lem:onesidedtransfer, lem:avgfunctionals, thm:windowed) and the Round-5 referee-corrected
results (Z5 T8 and Lemma 5.2, R1/R2 in Z5_ref_notes, Z6_ref_notes Lemma 2.1, Z3 Lemma 3.1/5.1 and the explosive design, Z4 Theorem A).
Part files: r6/Y3_ref_part1..3.md; proofs of fixes and additions: r6/Y3_ref_notes.md; script: r6/Y3_ref_work/critical_factor2.py.

## Overall verdict
Y3 is a substantial and essentially correct round. All results labelled PROVED survive, with one exception that is only a label
problem (Section 3.5(i): correct arithmetic, overclaimed as "PROVED about the methods"), one minor range error (Lemma 4.3) and
cosmetic constants. The genuinely new theorems are correct: Theorem 2.1 (raised support: the |b^theta| part of Z5's cushion
sparsity is superfluous), Theorem 4.1 (exact one-sided coefficient at arbitrary F with new test points, no Gram system),
Theorem 3.5 (super-critical support swallowing via un-switching + design D_sigma) and, most importantly, Theorem 5.1 (F = N with a
box-dominating base: every mate recovered for EVERY admissible T, without pinning, room or design). The SKETCH Remark 3.6(b)
(relaxing supp u_l in F) is WRONG as stated: its case split is reversed and the relaxation fails in general; I prove a corrected
version (single "absorbing" target contact, two-sided un-switching) and an obstruction for two such contacts. The heuristic
"worst-scale principle" (Y3 3.5(ii)) for the critical case is refuted in the exactly self-similar model: fixed data lose a factor 2
through cushion sharing, which no choice of scales removes. No counterexample is claimed or suggested; density remains OPEN.

## Verdicts
| # | Claim (Y3 label) | Verdict | Main point |
|---|---|---|---|
| 1 | Lemma 1.1 flip calculus (PROVED) | correct | re-derived (a)-(d) |
| 2 | Lemma 1.2 critical profiles oscillate (PROVED) | correct | m(y+) >= R_i (favourable direction); jump points accumulate at 0 |
| 3 | Theorem 2.1 raised T8 (PROVED) | correct | the raise keeps sgn a', (E1) with 8 for 4; |b^theta| sparsity was used only for theta-flips on F |
| 4 | Theorem 2.2 flip-extended T8 (PROVED) | correct | cosmetic: factor (1+o(1)) not (1+O(T_0+s_1)); theta-hypothesis redundant |
| 5 | Lemma 3.1 un-switching pair (PROVED) | correct | re-derived C_un |
| 6 | Proposition 3.3 design D_sigma (PROVED) | correct | (c) only removes allowed targets; bounded gaps is an instance of (D0) |
| 7 | Lemma 3.4 constrained-switching bound (PROVED) | correct | constant 32 -> 16; in (c) use D' = eta_1/2 |
| 8 | Theorem 3.5 super-critical support swallowing (PROVED) | correct | all claims re-derived; table/Remark 3.6(a) omit the B_sc qualifiers (d-neutral, supp u_l in F, monochromatic) |
| 9 | Remark 3.6(b) relaxing supp u_l in F (SKETCH) | wrong (fixed partially) | one-sided un-switching is inadmissible exactly in the case Y3 calls admissible; corrected version PROVED for one absorbing contact; obstruction for two |
| 10 | Section 3.5(i) methods fail at critical profiles (PROVED) | correct arithmetic, label overclaimed | statements about specific constructions' guarantees; refined by the factor-2 cushion-sharing computation |
| 11 | Theorem 4.1 one-sided coefficient at arbitrary F (PROVED) | correct | test points re-derived; block test accepts any chi_2 in X; Fenchel has no F-constraint |
| 12 | Corollary 4.2 (PROVED) | correct | — |
| 13 | Lemma 4.3 mates at most critical (PROVED) | correct with fixable gap | proved only for r <= 1/(1+3C_a) (needs t <= 1); only small r is used |
| 14 | Theorem 5.1 Theorem N (PROVED) | correct | every step re-derived; minor constant (sum lambda < 2 for general T); (W_M) can use max instead of sum of 1/mu |
| 15 | Claim 5.2 Z4 Thm A / Z6 U' at infinite F (SKETCH) | plausible, unverified | right modifications; three points to check listed |
| 16 | Theorem 6.1 master theorem (PROVED) | correct | packaging of lem:avgfunctionals + Theorem 2.1 |
| 17 | (LSC-trunc) where exact data exist; truncation free (PROVED) | correct | (c) is correct about Theorem 2.1; "never the obstruction" is a gloss |
| 18 | Liminf-sparsity extension (SKETCH) | plausible, gaps as listed | precise hypothesis is liminf m(x)log(1/x)/x = 0; does not touch the critical case |

## Detailed findings

F1. Theorem 2.1 (CORRECT). The only use of |b^theta| sparsity in Z5's T8 is the theta piece (|tau| <= s_1) on F_{<=N_w}; raising
|a''_j| to max(|a_j|, 8 rho s_1|b^theta_j|) gives |tau rho beta^theta_j| <= |a''_j|/8 < |a''_j|/4 <= s_j(1-tau rho c)a'_j. The raise
has l_1-mass <= 8 rho s_1||b^theta||_1 -> 0, keeps z' = sgn a' (so f' is NA with finite base support) and does not touch z', so (E2)
and everything depending on (E1)-(E3) (lem:F1, lem:scrambling, Bregman terms) is unchanged up to K_e. For the +- pieces the raise only
increases |a'_j|. This makes Theorem 3.5 possible (there |b^theta| ~ (tau'_l)_+ v_l/2 on S_l is NOT sparse).

F2. Theorem 4.1 (CORRECT). With k perp e, kappa = ||k||^2/(2q_0), k_2 = -kappa e: Z_t := eta_t - U h_t = q_0 z + t chi_c, ||h_t||^2 =
q_0^2 + t^4 kappa^2, q**(Z + Uh) <= max(||Z||_inf, ||h||) (a'(Z + Uh) <= ||a'||_1||Z|| + ||U*a'|| ||h||), a(eta_t) = q_0 - t^2 kappa nu,
so E_q <= t^2 nu||k||^2/(2q_0) + O(t^4) for every F. The note's block test (prop:lowerbound) uses chi_2 only through q(chi_2) and
w(t^2 delta_2) (which cancels), so it accepts chi_2 = Uk_2. Strong duality: the cone C_+ vanishes on F, so the dual has no F-constraint.
(c): G_b(a+tb) = Exc_{(sb)_-}(t) + nu Psi; rebalancing needs Exc = O(t^2); transfer data need no finiteness of F. The numerical
check reproduces (remainder ~ c t^4 > 0, consistent with the O(t^4) upper bound).

F3. Theorem 3.5 (CORRECT). Re-derived: tau_l (l in B_sc) enters no row of Z_f (target rows need u_l != 0 off F; B_F has no sign row;
q_l = 0), so tau'_l = tau_l on B_sc; Claims A and B (monochromatic sign makes d_j <= 0 and s_j Xt_j >= 0 on S_l(deep)); the identity
(b^-, omega^-) = Q + sum P_l(-eps_l(tau'_l)_-) (using X - Xt = -sum eps(tau')_- u_l); Lemma 3.4 applies to each l in B_sc separately
because (D1)(c) removes the targets of l' in (l_0, l_*] from S_{l_0} cap (l_*, inf). Scope statements should carry the B_sc
qualifiers (Remark 3.6(a) omits "a of constant sign on S_l").

F4. Remark 3.6(b) (WRONG AS STATED; corrected in ref notes Section 2). For l in B_sc with a target coordinate j notin F (no other bad
carrier at j), kappa_j := z_j eps_l y_l(j): if kappa_j > 0 the CONSTRAINED direction is pinned at O(t) by the budget at j (no
un-switching needed); if kappa_j < 0 the FREE direction is pinned and the contact absorbs the constrained switching. In the latter
case Y3's one-sided un-switching gives b^-_j = -chi_j eps D' y_l(j)/n_l with z_j b^-_j = chi_j D'|kappa_j|/n_l >= 0, NOT side-- admissible
when the + decomposition uses the contact (chi_j > 0). Y3_part1 Remark 1.10(c) has the sign of the moved amount wrong and claims
"PROVED by the same argument". Repair (PROVED): un-switch on both sides, P_l(eps chi_j D') on the + side, so b^+_j = b^-_j = 0; on S_l(deep)
both bases take the projection of x_s + chi_j D' v_l(s) onto [-A_s, A_s], which costs <= f^+_s + f^-_s + |r(s)| per coordinate
(O(K*t) in l_1); Gamma costs C_un chi_j D' and C_un(1-chi_j)D' -> 0. Obstruction (PROVED for exact (CS-side) data): with two absorbing
contacts j_1, j_2 the data must vanish at both, which forces |chi_{j_1} - chi_{j_2}| D' = O(delta).

F5. Section 3.5 (critical case). (i) The arithmetic is right: for 0 < kappa_- <= m/y <= kappa_+ < infinity, D^#(t) stays between two
positive constants (reproduced numerically: 6.94-9.16 at b = 1). But "PROVED as statements about these methods" over-reaches: D^# is
an upper bound for what Lemma 3.4 certifies, the actual amplitude of a mate may be small, and the companion costs quoted are those of
specific constructions. Label as arithmetic/HEURISTIC. (ii) New (model computation, critical_factor2.py): in the exactly
self-similar critical model (S = N, |a_s| = v_l(s)^2 up to constants, m(2y) = 2m(y)), a decomposition at scale t pays at least
Fdec(t) = sum 2(tDv - 2|a|)_+ (it uses the cushions of BOTH sides), whereas deep-assigned fixed data pay at r << t the flip excess
Exc_{Dv}(r) (one cushion): sup_r [Fdata(r)/r^2]/[Fdec(t)/t^2] = 2.000 at every t (b = 1; -> 0 for b = 0.5, unbounded for b = 1.5).
With a tight mate, the certified excess of the best fixed split is (1-2p)^2 Phi/8 (p = the + side's share of the decomposition's flips,
Phi ~ q_0 kappa D^2), zero only for p = 1/2. Hence Y3 3.5(ii) ("select upper points of the log-periodic profile") cannot work as
formulated, and Y3's next step "nested raises with masses o(T_0^2)" is impossible for critical profiles (the top raise alone costs
~ kappa D^2 T_0^2, the order of the assembly slack (1-rho^2)T_0^2/6). All known constructions give only rho-thresholded recovery
1 - rho^2 >~ C kappa D^2. Proposition 3.4 of the ref notes makes this rigorous in the simplest form: for d-neutral monochromatic
support-swallowed carriers with supp u_l in F and ANY profile, (f, rho g) in cl NA for rho < 1/(1 + C_un|B_sc|C_tau) (no design (c),
no (QM), no super-criticality). This localizes the critical obstruction at the boundary of C(f).

F6. Lemma 4.3 (fixable): the box bound |t Theta(k)| <= 3 needs t <= 1, so the statement holds for r <= 1/(1 + 3C_a).

F7. Theorem 5.1 (CORRECT; the key new result). Under (BD) every switching is cushion-sized (|X_j| <= 12 C_a|a_j|/t), all block usage
that two-piece data cannot carry (peaks, fine carriers) is moved into the base at second-order cost controlled by the margins, the
common shift costs only the flips (sum <= t/(2q_0)), and the closeness constant K = (1+||U||)^2/q_0 is an f-constant, so windows of
FIXED length suffice and no design is needed. Block side: every coarse strict non-peak is an inward-only coordinate (Z6-ref Lemma 2.1,
re-derived; constants independent of the number of coordinates). Non-d-neutral data are harmless because F = N removes all side
conditions and R*w is cushion-dominated; negative Delta d is handled by (SC_I) in Theorem 2.1. Checked that (BD) cannot be relaxed to
cushion-sparse Bx in this method (flip cost 2 int_0^{12r/t} m_Bx is Theta(r^2/t^2)).

F8. Claim 5.2 (SKETCH, plausible). To be checked when written: t_1 independent of C_A(l_*) (true for exact cushions), the inactive
coarse bad carriers' l_1 contribution <= 6 l_* t, and (W_inf) absorbing K_j C_A(l_*)/gamma_f (the C_a^2/mu_f^2 scaling).

F9. (LSC-trunc), Theorem 6.1: correct; (b) holds because every listed theorem produces NA approximants with FINITE base support.
"Truncation is never the obstruction" is an interpretation of Theorem 2.1, not a theorem about pairs without exact data.

## Attacks attempted (none broke a PROVED claim beyond the items above)
weak* vs norm (decompositions by compactness; forced data used qualitatively); uniformity in t, in the window, in L (Theorem 5.1:
c_flat, t_1 independent of the number of coarse coordinates; K_4 = C(1 + M_f(L)) absorbed by (W_M)); number of active carriers (B
finite in 3.5; Theorem 5.1 has no active-set bookkeeping); along companions (liminf-sparsity sketch: assembly with respect to the
ORIGINAL (f, g) is consistent since raised coordinates flip only for |tau| > 2T_0); Hoffman constants (Theorem 3.5: B_sc decouples
from Z_f); design N-independence ((c) and bounded gaps do not involve N); non-attained infima (Theorem 4.1(b) via finite-dimensional
Fenchel duality); signs and one-sidedness (found the reversed sign in Remark 3.6(b)); near-contacts vs contacts (case (alpha) of the
corrected remark: pinning constant 1/(1-|z_j|) is an f-constant for finitely many j); c_0 vs l_infty (z' in c_00, x' in c_0); infinite
peak/contact/support sets (Theorem 5.1 with F = N, all peaks, coarse truncation); hidden assumptions on T (Theorem 5.1 uses only
||Phi_m||_2 <= 1/2 and sum lambda < 2, valid for every admissible T); quantifier order (f' chosen inside Theorem 2.1 after the averaged
data, which are chosen after g, rho).

## Single most valuable idea
Theorem N's mechanism: when the base dominates the box profile, EVERYTHING that exact two-piece data cannot carry (peak usage,
fine carriers, arbitrary box-size switching, the w-direction of non-d-neutral data) can be moved into the base, where it costs
only second order (margins) and is cushion-proportional, and the common shift that restores exact one-sided cushion bounds costs
only the flips (O(t)). The closeness constant is then an f-constant, so fixed-length windows suffice and no pinning or design is
needed: the first recovery theorem for F = N with infinitely many swallowed carriers valid for every admissible T. (Runner-up:
the raised support of Theorem 2.1, which removes the average-data sparsity requirement and makes un-switching usable.)

## What remains open after Y3 and this report (design D_sigma or SLD-type designs, finite I; F infinite)
(O4-crit) Critical support swallowing (0 < liminf m_l(y)/y <= limsup m_l(y)/y < infinity, model |a_j| ~ v_l(j)^2) with non-vanishing
  constrained amplitude D: all known constructions (deep assignment, one- or two-sided un-switching, raised or nested companions,
  window averaging, upper-point selection) certify only 1 - rho^2 >~ C q_0 kappa D^2; the exact loss in the self-similar model is the
  cushion-sharing factor 2 (certified excess (1-2p)^2 Phi/8 with the best split). Needed: either D(t) -> 0 along suitable
  decompositions, or a construction that is not a fixed copy of scale-t data (e.g. scale-adaptive approximants whose cushions grow
  like |a|/r at every scale r, at total cost o(T_0^2) — impossible for one-level or nested raises).
(O4-nd) Non-sparse support swallowing through non-d-neutral carriers (Remark 3.6(c)), and through carriers with off-F targets that
  are shared with other bad carriers or have two or more absorbing contacts (z_j eps_l y_l(j) < 0) with different + fractions
  (ref notes 2.4).
(O4-box) Infinitely many bad carriers without box domination of F (box-size switching on thin support; cushion-sparse Bx is not
  enough for the Theorem N mechanism); F = N without (SC_I) or (W_M); Claim 5.2 (contact-swallowed carriers with (BD_B)) to be
  written out.
(O4-fin) The finite-F consensus core of ADDENDUM 5 ((r), (d), (m), (h), (O1)-(O3)), which reappears verbatim at infinite F.
Density of NA((c_0,p),l_2^2) remains OPEN for every admissible T; nothing found here points to a counterexample (the critical
obstruction is a loss of constant factors in specific constructions, not a structural defect).
