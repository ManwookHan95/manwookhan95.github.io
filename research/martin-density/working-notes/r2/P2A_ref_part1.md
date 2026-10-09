# P2 referee (P2A version = P2_notes.md, 512 lines) — part 1: provenance, Part-1 toolkit
Provenance: P2_notes.md (= P2A_notes.md, identical by diff) is the "P2A" instance (toolkit 1.1-1.7, Thm 2.1, 3.1-3.5, 4.1-4.6, 5).
A different referee instance wrote P2_ref_part0.md for the P2x version; to avoid file collisions my part files are P2A_ref_part*.md,
the final report is written to P2_referee.md (as instructed) and duplicated as P2A_referee.md.
Setting checked: finite block set I (p_N), only Lemma B's conclusion on T (I found no hidden use of other properties of T in Part 1-2).

## 1.1 Clamp formula. CORRECT (PROVED).
It is A Fact C restated: on P, |zeta(k)|/|zeta| = |alpha_k| + Phi_k^2 M/C, so C r(k) >= M, signs agree; off P, |w(k)| = C r(k) < M;
zeta(k) = 0 => off P => w(k) = 0. At an NA point the normer is x'/p(x') in c_0 and Fact C's proof uses only w' = J_m(R_m x'),
so the same holds (degree-0 homogeneity: x', xhat', x'/p(x') give the same ratios). Remark: "depends on xi only through u(xi)/|zeta|
and C" is true but C is itself determined implicitly by C^2 = sum Phi^2 w^2 (Lemma 4.1 exploits exactly this).

## 1.2 Convergence along engineered approximants. CORRECT (PROVED).
L compact => L** weak*-to-norm on bounded sets, L** zhat in V; J_m norm-to-weak* continuous at R_m** zhat != 0 (T3);
D_m, R_m* compact; a_n(xhat_n) = 1 = q(xhat_n) with a_n in c_00 gives grad q(xhat_n) = a_n; J_V = (J_m)_m (Observation C, finite I).
f = a + L*w because w = J_V(L** xi) = J_V(L** zhat). Fine.

## 1.3 First-order identity at NA points. CORRECT (PROVED).
<omega, R_m x'> = |R_m x'| <D omega, D w'>/C' for omega off P'_m (Fact C at f'), so <omega - d' w', R_m x'> = 0 and B(x') = g'(x') = 0.
The expansion is A Lemma 7.2 at f' (E_q(a'+tau B) = Fl + Kink + nu Psi; a'(xhat') = 1). Re-derived coordinatewise. Fine.

## 1.4 Two-regime assembly. CORRECT (PROVED).
Checked: 1 + (tau^2/2)(1-delta) <= 1 + tau^2/2 - tau^4/8 iff tau^2 <= 4 delta; sqrt(1+x) >= 1 + x/2 - x^2/8 for 0 <= x <= 8.
|tau| >= T_0: (T_0^2 + |tau| T_0)/6 <= tau^2/3 (T_0 <= |tau| <= 1) and <= |tau|/3 (|tau| >= 1); A Lemma 4.7. NA: f'(x') = 1 and
||(f',g')|| <= 1. Fine.

## 1.5 Averaging over scales. CORRECT (PROVED).
For s_j < |t| (=> |t| > s_J) use (ii)+(iii); sum_{s_j < |t|} s_j < 2|t| (geometric, ratio 1/2) => extra <= 2 kappa t^2/J. Fine.

## 1.6 Two-piece data, automatic facts. CORRECT.
g(xi) = 0 for g in C(f) (1 + t g(xi) <= s(t) for all t); <omega - d w, zeta_m> = 0 => b^+-(zhat) = 0, v(zhat) = 0.
v = b+ - b- = sum v_m - sum Delta d_m R_m* w_m: checked. v = 0 => omega_Delta = 0 (L* injective) => b+ = b-.
Useful observation (implicit in Thm 2.1): v != 0 forces K infinite (v in Y \ c_00 lives on F cup K, F finite).

## 1.7 One-sided admissibility => kappa <= 1. CORRECT (PROVED).
Base: Lemma 7.2 (general, b+ not supported in supp a) with b+(zhat) = 0, Fl, Kink >= 0, Psi(h) >= ||h_perp||^2/(2(1+||h||))
(this lower bound holds for all h). Blocks: A Lemma 4.4(b) with tau -> 0+ (Y -> C). Fine.
