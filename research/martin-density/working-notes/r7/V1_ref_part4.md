# V1-ref part 4 — end-to-end numerics, overstatements in the OPEN section, final verdict list

## Numerics (V1_ref_work/; sanity checks only, finite models with a diagonal base)
(N1) tu_check3.py / tu_check4.py — Lemma TU: see part 2 (exactness 1.8e-15, masses > 0, |Phi'| <= 0.018, others O(eta^2)).
(N2) assembly_check4.py — ONE block, K = 5..8 carriers with private bounded-gap signature sets, F = {0,1,2}, diagonal base:
     a robust donor c (rho_c >= 1.2), a near-threshold carrier k4 calibrated to |rho_k4 - 1| <= b = 1e-10, and a 2-carrier "ray"
     on {k4, k1} with tiny component |D| <= b; then (C3) case (b) (close + bank, Lam = 1e-7) and (C4) (x = -R^+ V, pulls + banks,
     explicit fixed point). 300/300 assembled companions: component at f^# <= 3.3e-16 (exactly 0), theta^# - theta >= 0.75 theta Lam,
     rho^#_k4 - 1 <= -0.75 Lam (k4 became a strict non-peak although it was tuned). 
     assembly_check2.py (same with Lam = 1e-5 and small lambda_c s^2 v): 3/48 failures, all with bank mass mu^D = 0.1..0.47 (NOT
     small: second-order Hilbert effects 1e-4 exceed the push 1e-5). This is outside Lemma DR's regime (mu^D <= Design Lam, Lam = T_lo^3
     astronomically small against Design^{-2}); it shows that the smallness of the bank mass relative to the design numbers
     lambda_c s_{s_m}^2 v_c(s_m) is genuinely used (it is guaranteed in D_Omega).

## Overstatement in V1 5.4 (OPEN section; not a PROVED claim)
V1 writes that for (B) "tiny-but-nonzero minors are not exactifiable by value tuning without destroying robust components —
determinantal". As stated this is not right: the d-matrix entries are LINEAR in the values, every minor is a polynomial in the
values with design coefficients, and by the Lojasiewicz inequality (g := sum of squares of the tiny minors and tiny components,
Z(g) nonempty since val = 0 is a zero) there is a value vector within C g(val)^{gamma} <= C' b^{2 gamma} of val^(2) at which all tiny
objects vanish EXACTLY, with C, gamma design constants of level l (finitely many polynomial systems per level); robust objects
move by << u, and Lemma TU realizes the move. The obstruction is only quantitative (Lojasiewicz exponent vs. raise buffer and cost),
and it is removed by a design choice b(w) := T_lo(w)^{K(l)}/(l Design(l)) with K(l) > 3/gamma(l). This is exactly the route
of task V2 (V2_part1: Lemma H, Hoffman bound through minors; V2_part2: determinantal objects, Lojasiewicz exactification).
I did not referee V2; within V1 the correct statement is: "(B) is not handled by V1's linear (least-norm) tuning".

## Final verdicts (details in parts 2-3)
Theorem 1' — correct (p1: s_max(l_f) >= max F; p0: rate values of carriers absent for p_N are set to 1, harmless).
Lemma D — correct.  Lemma 3.4', Lemma S — correct.  Patterns / Remark (2) — correct with p2 (component rate in a one-signed
block is <= b theta_m/m, hence tiny only for l >= l_f).  Lemma B, DR — correct.  Lemma TU — correct (p4: contraction constant
contains 1/(s'^2 v'^2), still a design number; c_T ~ Design^{-2/3} would already suffice).  Lemmas CO, ST, NS, RR — correct
(p5: no claim about the room of a class-R donor at f^#, none needed).  Proposition TR — correct.  Theorem E'' — correct with p3
(banks need not be contacts of f).  Master Theorem II, M-II.1-3 — correct.  Corollary AC — correct (diagonal base essential; within
the D_Omega assembly).  Lemma IP — correct.  Residual list — correct as logic; union with Y1 5.4 — correct by substitution
(Lemma S's K_d' = C_f l D^3/u^2 replaces K_d; absorbed by Q).
