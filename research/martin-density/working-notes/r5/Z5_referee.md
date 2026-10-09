# Referee report on task Z5 (infinite base support (O4) and reduction to finite base support)

Files reviewed: r5/Z5_notes.md, r5/Z5_part1..5.md, Z5_part4b.md, r5/Z5_work/*.py (all three scripts re-run; outputs reproduced).
Checked against: paper/martin_density_note.tex Sections 1, 3 (thm:transport), 5 (thm:transfer), 7 (Definition def:twopiece,
def:engineered, lem:approxfacts, lem:F1, lem:anchor, lem:scrambling, thm:engineered, cor:D1, cor:weightedengineered) and all of
Section 8; Round-4 reports r4/Z1_referee.md, Z1_ref_notes.md (the "F finite is essential" remark on bounded free switching).
My proofs of fixes and of the extension: r5/Z5_ref_notes.md (part files r5/Z5_ref_part0..4.md; script
r5/Z5_ref_work/check_deep_assignment.py).

## Overall assessment
Z5 is a careful and essentially correct piece of work. Its main achievement is real: Remark rem:Binf is now a theorem (step (iv) =
transfer peaks at a not in c_00, done along truncated canonical approximants), and Theorems B*, B^pm, engineered recovery and S
extend to infinite base support under explicit cushion conditions. I found no false PROVED statement. I found: one overclaimed
conclusion (T14: "windowed averaging cannot apply"), one overclaimed interpretation (T15), an incomplete description of the
(W^c) class (T7), a superfluous-hypothesis/illustration issue in the flagship example of T12 (it is window-pinned, hence already
covered by T5), a missing specification in the (B_res) extension of T12 (which Lambda*_f), and phrasing/typo issues (T10, T14).
More importantly, the open case that Z5 calls "fast support swallowing" is not entirely open: I prove (Theorem R1) that cushion
SPARSITY suffices in place of cushion domination, using Z5's own bounded-switching lemma (T10) and a one-sided "deep coordinate"
assignment. The remaining (O4) core is non-sparse support swallowing, infinitely many bad carriers, decaying room off F,
(H2)/(H3-inf) failures, and (LSC-trunc).

## Verdicts

| # | Claim | Verdict | Main point |
|---|---|---|---|
| T1 | transfer peaks at arbitrary a | correct | all uses of a in c_00 replaced by a_N; uniform no-flip radius; bookkeeping identity at x'_N |
| T2 | windowed averaging at arbitrary F | correct | only the last sentence of thm:windowed used F |
| T3 | uniform transfer expansion (C-a') | correct | error term |lambda| 2q*(rb) = O(c_flat r^2) |
| T4 | clamped window certificate | correct | identity for (b^cl 1_{F_t})(zhat) and lem:flip re-derived |
| T5 | B*-inf | correct | chain Prop 3.1 + Lemma 3.2 + Cor 2.3 checked |
| T6 | B-inf | correct | prop:pinned(a) valid at any F (J_gamma excludes F) |
| T7 | sign-mixed and cushion room | correct with fixable gap | (W^c) is void under monochromatic support swallowing (r^{[M]} = 0 for all M) |
| T8 | engineered recovery at arbitrary F | correct | (N0), far support as contacts, flip budget under (CS-data) checked |
| T9 | pure base mates along truncations | correct | Fl^M <= rho Fl_b re-derived |
| T10 | bounded free switching at any F | correct (phrasing) | corrects R4; rigidity(a) as stated is still true |
| T11 | proxy budget | correct | constants re-derived |
| T12 | Theorem S-inf | correct with fixable gaps | Example 6.2 is window-pinned (T5 suffices); (B_res) extension needs the note's Lambda*_f |
| T13a | reduction equivalence | correct | tautological composition; (LSC-trunc) carries all the difficulty |
| T14 | limitation of base pinning | correct arithmetic, overclaimed | D*/t -> infinity for EVERY support-swallowed carrier; windowed averaging DOES apply (T12, Theorem R1) |
| T15 | deep flips | correct with fixable gaps | obstruction only in the non-sparse regime |
| T16 | no design removes support swallowing | correct | trivial; also defeats cushion sparsity |

## Details

T1. Verified Steps 1-6 of thm:transfer with a -> a_N := a1_[1,N]/q*(a1_[1,N]), z^N := z1_[1,N]: z^N = sgn a_N on supp a_N, so
f'_N is norm attaining (Prop smooth(c)) and f'_N -> f (Prop approximants (ii)=>(i)); kappa_N = (b1_[1,N])(xt_N) -> b(zhat) = 0 by
dominated convergence (xt_N -> zhat weak* boundedly); |b'_N(j)| <= (||b/a|| c^a_N + |kappa_N|)|a_N(j)| gives a no-flip radius uniform in N;
P_N^perp U* b'_N = P_N^perp U*(b1_[1,N]) -> P^perp U* b; e_{m,N} := R_m* y_{m,N} - ((R_m* y_{m,N})(x'_N)/c_N) a_N -> e_{inf,m}
(R_m* y_{m,N} -> R_m* y_m in l_1, x'_N -> xi weak*); a_N(x'_N) = c_N; E = O(t^2) may be negative, harmless. Transfer peaks (Step 2)
are built at xi from a (any a in l_1). Correct; closes step (iv) of rem:Binf.
T2-T6. Correct as stated. Note that (SR) at infinite F requires room OFF F, so B-inf says nothing about support swallowing.
T7. Theorem 3.6 is correct (sum_l E^c_l <= (2/q_0 + 4)t; r^{[M]} decreases in M, so M(T_lo(l_*)) is the right choice). The gloss
"(W^c) holds only for super-fast decay" is incomplete: if sgn a is constant on S_l cap F and r_l = 0, then r_l^{[M]} = 0 for every M
(take sigma = -sgn a), so (W^c) fails whatever the decay. (W^c) is useful only for sign-mixed a on swallowed signature sets.
T8. Correct. Every use of finite F in thm:engineered is replaced: window N_w with alpha(N_w) <= s_1^2 (so (E1)-(E5), lem:F1,
lem:anchor, lem:scrambling are unchanged), a_min replaced by rho T_0 C_R <= 1/8 or by the flip budget 2 rho|tau| m(4 rho|tau|) <=
delta tau^2/16 (K_sharp fixed after T_1, so Fl <= tau^2 uniformly), far support (N_w, N''] as contacts of sign s_j with first-order
cost rho|tau| sum_{j > N_w}(s_j v_j)_- <= |tau| delta s_1/32. Budget 1 - 2delta + 3delta/4 <= 1 - delta.
T9. Correct; numerical check reproduced.
T10. Correct and a genuine correction of the Round-4 referee (Z1_ref_notes.md: "F finite is essential (Y may contain a)"): the
first-order coordinate (sum_U c u)(zhat) pins the a-direction (|Delta B(zhat)| <= t/q_0). Phrasing: Lemma lem:rigidity(a) as stated
(b_+ - b_- in c_00) remains true at every F; what fails is uniqueness of data with base parts in l_1(F cup K).
T11. Correct (bookkeeping only; it does not make g a mate of a finite-F first row).
T12. The proof is correct (Steps 1-5 checked line by line, including the common-shift bound |sigma_j| <= f^+_j + f^-_j + |(Delta B - X)_j|
and the preservation of the cushion bounds under averaging). Two points. (i) Example 6.2 (a = u_{l_0}) is window-pinned: u_{l_0}(zhat) =
a(zhat) = 1 and |Delta B(zhat)| <= t/q_0 give |Delta theta_{l_0}| <= (1/q_0 + K*)t (Z5_ref_notes Lemma R3), so T5 already gives f in Rec,
without (H2), (H3-inf); the example does not exercise the exact-switching content of T12 (genuine examples need a d-neutral bad
carrier with signature inside F). (ii) Remark 6.3(b) ((B_res) with infinitely many bad carriers) uses Lemma lem:modswallow(b), whose
unrolling contains the bad inequalities; (W*) must then use the note's Lambda*_f (product over all l'' in L_N, bad factors included),
not Z5's good-only product. With that reading it is correct. (iii) Minor: the truncation b^+_2 := b^+_1 1_{F_t} is unnecessary (T8
accepts infinite support) and must be dropped in the sparse extension below.
T13a. Correct, but it is a reformulation: (LSC-trunc) is the infinite-F half of Lemma Z. The 2 alpha(M) transplant identity is a
correct base-excess identity; as an argument that truncation fails it is HEURISTIC (forced data zhat^M, w^M also move).
T14. The exponent computation is right for S_l with bounded gaps (typo (1-beta)/(1+beta) in Z5_part4b l.30). But (a) D*_l(t)/t -> infinity
for every support-swallowed carrier: Phi_l(Kt,t) <= Kt m_l(Kt^2/2) = o(t) for every K (cushion-dominated carriers even have D* >= 2c/t),
so the pinning constant is not what separates fast from cushion-dominated swallowing; (b) "windowed averaging cannot apply" is false:
it applies with exact data under (H4-inf) (T12) and under cushion sparsity (Theorem R1 below). Correct statement: window PINNING cannot be
derived from the base budget for support-swallowed carriers.
T15. Lemma 7.4 and the necessity of (s_j X_j)_- <= 2A_j are correct (necessity holds for any data with b^+ - b^- = X on F). The claim that
fixed data reproducing deep flips are unusable holds only in the non-sparse regime: with bounded switching the deep usage is O(U_B(j)) and
its flip cost is 4C|r| m_B(2C|r|) = o(r^2) under cushion sparsity.
T16. Correct (|a_j| := 2^{-j} min_{l <= j, v_l(j) != 0}|v_l(j)|, normalized); it also defeats cushion sparsity.

## New result (fix/extension): Theorem R1 (Z5_ref_notes Section 2). PROVED.
For the SLD operator and every N: every first row (F arbitrary) with (W*), (H2), (H3-inf), (B_fin) and
  (CS_B)  sum{ U_B(j) : j in F, |a_j| < y U_B(j) } = o(y),  U_B := sum_{l in B}|u_l|,
is in Rec. Equivalently (Lemma R0) each bad carrier with S_l cap F infinite satisfies sum{v_l(j) : |a_j| < y v_l(j)} = o(y). This
contains T12 ((H4-inf) => (CS_B)) and covers fast support swallowing with sparse cushion violations (model |a_j| ~ v_l(j)^{1+beta}, beta < 1;
ratios 1/j). Proof ingredients: (1) bounded switching (T10) gives |tau'_l| <= C_tau uniformly in t, hence |X_j| <= C_tau U_B(j);
(2) common shift where s_j X_j >= -2A_j, and the one-sided assignment b^+_1(j) := -s_j A_j at the "deep" coordinates
s_j X_j < -2A_j, with |B_+(j) - b^+_1(j)| <= f^+_j + f^-_j + |(Delta B - X)_j| in both cases (so the data stay O(K* t)-close to B_+-);
(3) a one-sided transfer expansion that tolerates anti-sign parts 3|a_j|/t + C U_B(j), with flip cost 3C r m_B(2C r) = o(r^2) uniformly
in t (Lemma R2); (4) the averaged window data satisfy (CS-data), so T8 applies. Numerical sanity check of the elementary inequalities
(4e5 random instances) and of the flip-cost dichotomy beta < 1 / beta >= 1 in check_deep_assignment.py.
Also (Remark R1.3): the cushion/near-contact analogy used by Z5 to identify (O4)(b) with (O1)(i) is imperfect: the cushion allowance
2|a_j|/t grows as t -> 0, whereas a near-contact's room is fixed and penalizes BOTH directions at first order; Theorem R1 has no
near-contact analogue. The support version of approximate swallowing is strictly better behaved.

## Most valuable idea
At scale t a support coordinate is a contact of sign sgn a_j plus a free anti-sign allowance 2|a_j|/t that grows as t -> 0 (Z5's
cushion lemma/proxy budget). Together with truncated canonical approximants (transfer peaks at a_N) this transfers every room-based
theorem to infinite F; together with bounded free switching at arbitrary F (first-order pinning of the a-direction) it shows that
switching beyond the allowance is bounded, hence harmless exactly under cushion sparsity (Theorem R1).

## What remains open (O4), SLD operator, finite I
Pairs (f, g) with F infinite, g not window-pinned at f, and: (a) room off F decaying too fast ((W^pm)/(W*) fail); (b') finitely many bad
carriers but some bad carrier with NON-sparse support swallowing, limsup_{y->0} sum{v_l(j): |a_j| < y v_l(j)}/y > 0 (model beta >= 1;
there fixed data with nonzero constrained-direction deep part have flip cost >= r|c| m_l(r|c|/2), not o(r^2)); (c) infinitely many bad
carriers, except (B_res) with uniform cushion domination (e.g. F = N, a > 0); (d) failure of (H2) or (H3-inf). Also open: (LSC-trunc)
(the infinite-F half of Lemma Z), Theorem thm:onesided at infinite F. Together with (O1)-(O3) at finite F this is the open core of
Lemma Z. No counterexample mechanism was found; nothing here points to one.
