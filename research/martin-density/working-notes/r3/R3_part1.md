# R3 part 1: setting, task, and outcome of the counterexample attempt

## 1.0 Setting (used throughout R3)
Finite block set I (the norms p_N; Preprint B Remark martin-tail reduces Martin's p to these), canonical base q
(q*(a) = ||a||_1 + ||U*a||, U: H -> c_0 compact with dense range, U* injective). "Admissible T" = Lemma B's conclusion only
(T norm one, injective, Ran T = Y, Y cap c_00 = {0}, every tail of (u_{k,m})_k norm dense in S_{q*}). Notation of A_notes §1
(Facts A-F): lambda_{k,m} = m Phi_m(k), (R_m x)(k) = lambda_{k,m} u_{k,m}(x), R_m* w = sum_k lambda_{k,m} w(k) u_{k,m},
N_m(w) = ||w||_inf + ||D_m w||_2, (D_m w)(k) = Phi_m(k) w(k). For f in S_{p*}: normer xi, q_0, forced decomposition
f = a + L*w, zhat = xi/q_0 = z + U e, F = supp a, J := {j notin F : |z_j| < 1} (free coordinates), zeta_m = R_m** xi,
M_m, C_m, peaks P_m, alpha_m (Fact C). Block threshold (Fact C): k in P_m iff m|u_{k,m}(xi)| >= Phi_m(k) M_m |zeta_m|/C_m;
off P_m, w_m(k) = C_m m u_{k,m}(xi)/(Phi_m(k)|zeta_m|).
Finite certificates c = (b, omega), g_c, H(c), r(c), kappa(c): A_notes Def 4.1; expansion: A_notes Prop 4.5
(p*(f + s g_c) <= 1 + (s^2/2) H(c)(1 + kappa(c)|s|) for |s| <= r(c)). NA approximants: (F1) = G_referee 4.7 / A Fact D:
f' = grad p(x'), x' = z' + U e', a' in c_00 cap S_{q*}, z' in B_{c_0}, z' = sign a' on supp a', e' = U*a'/||U*a'||; and
N2 Lemma 1.5: if a'_n -> a in l_1 and z'_n -> z coordinatewise then f'_n := grad p(x'_n) -> f in norm, with all forced data
converging (A Fact E). Ls(f) := {g : (f, rho g) in cl NA for all rho < 1} (N_part1). Labels: PROVED / SKETCH / HEURISTIC /
FALSE / OPEN / NUMERICAL.

## 1.1 The task and what a counterexample must prove
A counterexample is (f, g, rho, delta, x_1..x_k) with f in S_{p*} non-attaining, g in C(f), rho < 1, such that
max_i (rho g(x_i) - r~_{f'}(x_i)) >= delta for EVERY NA f' with p*(f' - f) < delta (N2 5.1; A Cor 3.3). The natural route is a
closure theorem Ls(f) subset K(f) with K(f) closed convex, given by necessary conditions satisfied by all limits of mates at
NA approximants, plus g in C(f) \ K(f). The candidate design is E's "rigid design" (E_notes 7.3: (A1) one-sided
near-threshold carriers of a core direction v at all scales, both peak types, critical errors K lambda sigma on core window
coordinates; (A2) far rigidity; (A3) sign obstruction; (A4) destruction by infinitely many detector groups; (A5) no
critical-rate convertible generic carriers of the error directions), which by N2 4.5 (SKETCH) is compatible with Lemma B
as far as far rigidity is concerned, and whose only model-level evidence is Model N (E 7.4: R(J) > 1 for every bounded number
J of converted scales in the error-dominated regime).

## 1.2 Outcome (summary; details in parts 2-5)
NO counterexample. The attempt fails at a precise point, and the failure is a new recovery mechanism valid for every
admissible T:
 (1) Theorem EC (part 2, PROVED): at engineered NA approximants one can convert, by window moves of sup-norm o(1) on free
     coordinates, finitely many GENERIC block coordinates (taken from the dense tails, at any prescribed depth) into strict
     non-peaks with w'' = 0, approximating any prescribed finite family of targets in zhat-perp with precision -> 0.
     NO approximation rate is needed: the precision only has to tend to 0, the depth is free.
 (2) Room lemma (part 2, PROVED): an error of size O(s) at scale s needs room O(s^2): a converted generic carrier at depth
     Phi carries an error component of size kappa s two-sidedly for all |t| <= s as long as s^2 <= M Phi/(2 c kappa).
     The "implant scale gap" (C, Round 1) concerns carrying O(1) components; it does not obstruct carrying ERRORS.
 (3) Proposition Z (part 3, PROVED): at scale zero the closure set is trivial: every g with g(xi) = 0 is a norm limit of
     certificate directions g_{c_n} at NA approximants f''_n -> f with H(c_n) -> 0. Hence no closure theorem based on
     second-order (Hessian) data of approximants can separate anything; K(f) must involve radii, and the only radius
     constraint available (implant cost) is circumvented for O(s)-size components by (2).
 (4) Part 4 (Theorem 4-EC: PROVED as an implication; application to the rigid design: SKETCH + NUMERICAL): in E's rigid
     design the core errors live in a fixed finite-dimensional space E_c on core window coordinates (this is how (A2)/(A3)
     are formulated), so (1)-(2) carry ALL frozen errors and all boundary-layer errors; the generic carriers are chosen
     BEFORE the boundary scale (quantifier order: generic depth Phi_gen, then boundary lambda_b << sqrt(Phi_gen)).
     In Model N this removes the boundary excess even with ONE converted carrier of ONE type (a single absolute shift V):
     R = 1.168, 1.041, 1.009 when errors are carried 4, 6, 8 octaves above the band (R - 1 ~ band/tau_gen -> 0), versus
     R = 3.41 without carrying; with both types converted R = 1.088, 1.023, 1.005 (versus 1.194). So (A5) is not
     satisfiable in any form that matters, and bounded conversion capacity is NOT an obstruction for compact errors.
     Detector (far) errors are absorbed by making the detector supports contacts with masses; this fixes the group scalars
     at O(1) values and puts the converted band at the depth where detector errors are of position size, i.e. in the
     peak-cost-dominated regime (exact first-order peak cost alpha = delta Phi^2 M/C computed, PROVED), where E's own
     numerics already give R <= 1 (SKETCH).
 (5) What remains of O3 (part 5, OPEN, sharply stated): "escaping guarded errors": the frozen/boundary-layer errors must
     have a non-compact (escaping) part of critical size, carried by single far coordinates (or concentrated sets)
     on which (a) generic approximants are delayed below depth ~lambda_b^2, (b) engineered contacts are blocked because
     near-boundary carriers ("guards") have mass >~ their margins there, and (c) the guards themselves have no individual
     handles (their own escaping parts are shared/guarded). Each carrier's escaping mass of critical size is itself a
     conversion handle for that carrier, so the guard structure must be recursively closed; whether this is consistent
     with Lemma B, with (A1) and with the mate condition at f is OPEN. A counterexample along E's lines must realise this.
 (6) Leaning: positive (density); the obstruction class has shrunk from "bounded conversion capacity" (any rigid T) to
     "non-compact, recursively guarded critical errors".
