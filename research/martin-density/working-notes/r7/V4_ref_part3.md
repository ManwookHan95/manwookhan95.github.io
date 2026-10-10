# V4 referee, part 3: Lemma 5.2, Theorem 3.5 / Proposition 5.3, Lemma 3.6, Theorem 3.7, Lemma 3.8; global precision (G1)

## 3.1 Lemma 5.2 (threshold Lipschitz; strictly increasing in peak masses).  CORRECT.
|A(th; zeta) - A(th; zeta')| <= ||zeta - zeta'||_1 (each term 1-Lipschitz in |zeta(k)|); d/d|zeta(k)| [Phi_k^2 min(th, nu_k)^2] = 2 nu_k 1[nu_k < th] <= 2 th;
dPsi/dth = -2(A + th) sum_{nu_k > th} Phi_k^2 (one-sided at kinks), in [-2(A+th)||Phi||_2^2, -2(A+th)Phi_{k_1}^2] while nu_{k_1} > th.  Continuity of
theta (unique root of a jointly continuous function strictly decreasing near the root) keeps nu_{k_1} - theta >= (nu_{k_1}(zeta^0) - theta(zeta^0))/2
on a small ball, which makes the derivative bound usable.  (b): at a peak k (degenerate allowed) A' = A + t and B' = B at th = theta, so
Psi(theta; zeta') = 2At + t^2 >= 2At, then the derivative lower bound.  Both constants uniform on the ball.

## 3.2 Theorem 3.5 (fine re-alignment) and Proposition 5.3 (block-tame approximants).  CORRECT (this upgrades Z3's SKETCH 6.1).
(a) z^(L) = z on supp u_k for k <= L, so u_k(delta) = 0 for k <= L and |u_k(delta)| <= 2||u_k||_1 for k > L; Z3 Lemma 3.1 (same a) gives the cost
once max_m Delta_m <= c_f (L large).  (b) For l > L with S_l ∩ F = {}: S_l is unassigned at step l (allowedness (a) for all earlier targets,
coarse ones included), so n_l val_l = A_l + eps_l(B_l + delta_l H_l), |val_l| >= delta°_l, and Step 4 of Theorem 2.2 applies verbatim (it uses
only |val_k| <= 1 for coarser k and (SF*)).  PRECISION: "margin >= q_0 delta°_l/2 beyond the first peak of its block" must be read at f^(L)
(the first coarse peak of f may be lost if it was degenerate; the first fine carrier of the block is always a peak), and Step 4 then uses
theta_m < nu_{k_1} <= m(1+||U||)/Phi_{k_1} for that first peak k_1.
Prop. 5.3 re-derived: the lever moves val_{l_a(1)} affinely (its A and B are untouched; no forced flip since the change <= delta 2^{-s_1}/4 <
delta H/2); carriers < l_a(1) are untouched because every coordinate of supp u_k is owned by a carrier <= k; later carriers of block 1 change
zeta_1 by <= e_1 in l_1 WHATEVER their hysteretic flips/cascades; phi is strictly monotone by Lemma 5.2(b) (l_a(1) stays a peak); the bad set
{t : theta_1(t) = nu_k} lies in an interval of length <= 2 L_Theta e_1/(rate) <= L_Theta 2^{-8-k(l_a(1))}/c_Theta, which is small for l_a(1) large
(k(l_a(1)) -> infinity inside block 1; the ball of Lemma 5.2 is fixed since zeta_1(t) stays within O(lambda_{l_a}) of zeta_1 at f^(L)).  The block
by block choice with dgap_m and the (MS) count are correct.  The levers make s_m FREE coordinates (|z| = t_m < 1); V4 notes this (Lemma
5.5 is the contact-preserving variant).

## 3.3 Lemma 3.6 (transplant).  CORRECT; one rebalancing precision.
Re-derived: at non-flipped j the nearest split is within |D^#(j) - D(j)|; at flips within |D(j)| + |D^#(j)|; where D^#(j) = 0 the old
pair costs |b^+(j)| + |b^-(j)| = |D(j)| (side admissibility at f forces z b^+ = |b^+|, z b^- = -|b^-|); on F the difference is |D^# - D|;
D^#(xi^#) = 0 by (T1) and <omega - d^#(omega) w^#, zeta^#> = 0; the represented functional is G^# (checked).  b^+(xi^#) -> b^+(xi) = 0 since b^+ in l_1 and
xi^# -> xi coordinatewise boundedly.  PRECISION (banked case): rebalance with multiples of a 1_F (not of a^#): adding c a^# also moves the
bank coordinates by c mu_m eps_m and, for c < 0 and x_j = 0, can destroy the contact-likeness z b^+ >= 0 there; a 1_F has a 1_F(xi^#) =
q_0^# a(zhat^#_F) -> q_0 != 0, so it works and changes nothing on the banks.

## 3.4 Theorem 3.7 (negative mismatch through (SC)-companions).  CORRECT.
Checked the use of Z3 Lemma U: with FIXED omega (finite support, gaps >= gamma_0/2 at f_i for i large by (T1) and continuity), choose t := t_1,
gamma_B := gamma_0/2, A_2 := t_1 max|omega|, A_0 := t_1 sup_i ||b_i||_1; Lemma U gives the bound for 0 < |r| <= c_flat t_1 =: r_1 uniformly in i.
Banked supports: Y4-ref Lemma P2 (contact-like data on banks never flip on the correct side, so a_min over the banks is irrelevant).
The two regimes: rho^2(kappa_w + eps) <= 1 - r^2/4 for |r| <= r_1; for |r| >= r_1, p*(f + r rho g) <= s(rho r) (g in C(f)) and s(r) - s(rho r) >=
c(rho, r_1)|r|.  thm:engineered at f_i with kappa_w(rho G_i) = rho^2 kappa^(i)_w <= 1 and (SC) for {Delta d^#_m < 0}.  Correct.

## 3.5 Lemma 3.8 ((SC) from a generic threshold).  CORRECT for a single block, two precisions.
Re-derived: a contributing carrier satisfies kappa Phi_k |nu_k - theta| <= s (peaks via mu = q_0 Phi(nu - theta)/m, non-peaks via gap =
C(theta - nu)/|zeta|, the case gap <= s implies it since Phi <= 1); with s = Upsilon s_L only k <= L have Phi_k > s, and |nu_k - theta| <=
(Phi_{L+1}/Phi_L)^{1/2}/kappa = eps_L/kappa.  PRECISION 1: "no k <= L has |nu_k - theta| <= eps_L/kappa for L large" needs eps_L <= eps_k for k <= L;
state the lemma with a NONINCREASING summable majorant of (Phi(k+1)/Phi(k))^{1/2} (under (SF*) one may take eps_k := 2^{-(l(k)+11)/2},
l(k) = j(k,m), since Phi_m(k+1)/Phi_m(k) <= c_{l+1}/c_l * 2^{...} <= 2^{-l-11}).  PRECISION 2: def:SC needs ONE sequence for all blocks of I_-;
the lemma gives block-dependent sequences.  A common sequence exists along LADDER gaps: s := (Phi_l Phi_{l+1})^{1/2}-type scales between
consecutive ladder weights (all blocks at once), provided the hypothesis is formulated with the ladder majorant.  Not needed by V4 (Theorem
5.6 uses (BT), which gives Scr_m(Upsilon s) = o(s) for every s).

## 3.6 Global precision (G1): owners and the owner recursion must be relative to L_N.
For p_N with N < infinity, only carriers in L_N = {l : m(l) <= N} exist.  V4 runs the owner recursion of Construction SA "over l = 1, 2, ...
(all blocks)" and defines the owner as the first carrier (any block) with u(j) != 0.  Then a coordinate owned by an ABSENT carrier o (m(o) > N)
receives z_j = eps_o, while every sum over PRESENT carriers (the vector of Step 7 / c_*(l), the d-row D = sum_{k in L_N} gamma_k u_k) is dominated
at j by the first PRESENT carrier k with u_k(j) != 0, whose sign eps_k sgn y_k(j) is unrelated to eps_o.  So Theorem 2.2(d)-(e) for p_N, and the
owner-based statements of Sections 9-10 (where an absent owner would behave like a NEUTRAL carrier), are not justified as written.
FIX (proof in V4_ref_notes, Lemma R3): define o_N(j) := first carrier IN L_N with u(j) != 0, and run every recursion over L_N only.  By Lemma
1.2(b) (block 1 is present) every coordinate is still assigned; a present carrier's signature set is unassigned at its own step (allowedness
(a)); all dominance bounds used are upper bounds by sums over ALL later carriers ((SF*), (SF_tau), allowedness (b), (b')), so they hold a
fortiori for present ones; a coordinate in Z_0 or in the signature set of an absent carrier falls into case (iii) of Step 6 / Lemma 4.1'
(j in supp y_{o_N} \ S_{o_N}).  With this change every statement of V4 holds for every N, and the DESIGN stays N-independent (only the
row construction depends on N, which is harmless: Lemma Z is per (N, f, g, rho)).
