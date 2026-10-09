# Z5 referee, part 4: first-order pinning; Example 6.2 is window-pinned; (B_res) fix; T14 general statement

## Lemma R3 (first-order pinning of the a-direction; any admissible T, any F). PROVED.
Let (B_+-, Theta_+-) be a two-sided decomposition at scale t <= min(t_eta, 1). For every finite set U of carriers and every
c in R^U with (sum_U c_l u_l)(zhat) =: kappa_c,
  |sum_{l in U} c_l Delta theta_l ... |   -- precise form used below:
  |sum_l Delta theta_l u_l(zhat)| = |Delta B(zhat)| <= t/q_0.
Proof: (eq:DeltaB) and Lemma lem:budget(a) (|q_0 B_+-(zhat)| <= t/2). QED
Consequence. If all carriers except l_0 satisfy sum_{l != l_0}|Delta theta_l| <= K t and u_{l_0}(zhat) != 0, then
|Delta theta_{l_0}| <= (1/q_0 + K) t / |u_{l_0}(zhat)|   (|u_l(zhat)| <= q*(u_l) q**(zhat) = 1).
(For the SLD, u_l(zhat) = 0 iff l is d-neutral, i.e. k(l) is a strict non-peak with w(k(l)) = 0: by Lemma lem:threshold,
(R_m** xi)(k) = lambda_{k,m} q_0 u_{k,m}(zhat).)

## Example 6.2 of Z5 is window-pinned (so T5 already covers it, without (H2), (H3-inf)).
a = u_{l_0}, z = sgn a on F = supp u_{l_0}, z = 0 off F. Then u_{l_0}(zhat) = a(zhat) = 1. Good carriers are pinned on windows
(lem:modswallow(a): sum_{l != l_0}|Delta theta_l| <= K* t, by (W*), which holds as Z5 says). By Lemma R3,
|Delta theta_{l_0}| <= (1/q_0 + K*) t. Hence sum_l |Delta theta_l| <= (1/q_0 + 2K*) t on every window scale, K* = (1/q_0 + 22)Lambda*_f(l_*),
and (W*) gives K_j T_hi(l_j) -> 0, n^w_{l_j}/K_j -> infinity: every mate is window-pinned, and f in Rec by T5 (B*-inf). (H2),
(H3-inf) are not needed. [In fact k(l_0) is a non-degenerate peak: zeta(k) = lambda q_0 u(zhat) = lambda q_0, far above threshold.]
So Example 6.2 does not illustrate the exact-switching content of T12. Genuine T12 examples: a bad support-swallowed carrier l with
u_l(zhat) = 0 (d-neutral strict non-peak, w_{m(l)}(k(l)) = 0) and |a_j| >= c v_l(j) on S_l cap F (or (CS_l) for Theorem R1).
The claim "f in Rec whenever (H2), (H3-inf) hold" is TRUE, but the hypotheses are superfluous for this example.

## (B_res) extension (Z5 Remark 6.3(b)): use the note's Lambda*_f.
Lemma lem:modswallow(b) unrolls the bad inequalities r*_l (tau_l)_- <= E_l + 2 sum_{good l' > l} pi_{l',l}|Delta theta_{l'}| together with
the good ones; the resulting product contains the bad factors (1 + 3/r*_l), r*_l := 2||v_l 1_{S_l \ F}||_1 > 0 (B_F empty). Hence in
the (B_res) extension (W*) must be read with the note's Lambda*_f (product over ALL l'' in L_N), not Z5's good-only product.
With this reading the extension is PROVED as stated (box bound sum_B|tau'_l| <= 2/t and uniform c_B give |X_j| <= 2c_B|a_j|/t on F).

## T14, general form. PROVED.
For every support-swallowed carrier (S_l \ F finite, S_l cap F infinite), and every K > 0, Phi_l(Kt, t) := sum_{S_l cap F}(K t v_l(j) -
2|a_j|/t)_+ <= K t m_l(K t^2/2) with m_l(y) := sum{v_l(j) : |a_j| < y v_l(j)} -> 0 (y -> 0), so Phi_l(Kt,t) <= t/(2q_0) for small t:
D*_l(t)/t -> infinity for EVERY support-swallowed carrier (cushion-dominated ones included, where even D*_l(t) >= 2 inf(varrho)/t).
The fast/cushion-dominated distinction is therefore not about pinning but about exactification; the sharp dividing line for the
window method with exact data is cushion sparsity m_l(y) = o(y) (Theorem R1), not inf varrho_l > 0.
