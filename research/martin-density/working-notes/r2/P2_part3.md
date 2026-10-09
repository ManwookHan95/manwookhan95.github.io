# P2 part 3: the mixed term, d-mismatch, and non-neutral two-piece mates

## 3.1 Proposition (the mixed term created by contact masses). PROVED.
Let a'' = a + delta y with y in c_00 (e.g. y = z_j e_j*, a tiny contact mass), e(delta) := U*a''/||U*a''||. Then e'(0) = P_{e-perp}U*y/nu, and for
every B in l_1 with z' = z on supp B:
   B(xhat') - B(zhat) = <U*B, e(delta) - e> = delta <P_{e-perp}U*B, P_{e-perp}U*y>/nu + O(delta^2 ||B||_1).
Since the first-order term of q*(a' + tau B) at f' is tau B(xhat') (Lemma 1.3 / A Lemma 7.2), a mass delta at j shifts the first-order base
term of a transported decomposition by
   tau delta z_j <P_{e-perp}U*B, P_{e-perp}U*e_j*>/||U*a|| + O(tau delta^2)        (the "mixed term" of the task),
which is of size ~ tau^2 exactly at the scales tau ~ delta where the mass is needed. Its effect depends on how many base parts B must be
served by ONE g':
 (a) One decomposition (B fixed): harmless. The first-order terms of all components of a decomposition of f' + tau g' add up to g'(x')
     (balance, A Lemma 7.1 at f'); recomputing the block coefficients d' at f' (block first-order terms 0) and normalizing g'(xhat') = 0 by
     subtracting c a' (no cost: a' direction is a rescaling) forces B(xhat') = 0 (Lemma 1.3). The mixed term is absorbed into c.
 (b) Two decompositions B+ (tau > 0), B- (tau < 0) of the same g' (two-piece mates): both first-order terms vanish iff
     (B+ - B-)(xhat') = 0, i.e. v(xhat') = 0 for the transfer v = B+ - B-. The mixed-term DIFFERENCE delta z_j<P_{e-perp}U*v, P_{e-perp}U*e_j*>/nu
     is not zero in general, and it is cancelled exactly by the steering step (Thm 2.1, Step 1: far flipped contacts with negative masses
     pull, a mass at j_+ raises, intermediate value theorem). So for two-piece mates the mixed term is NOT an obstruction (PROVED, Thm 2.1).
 (c) Finitely many pieces: one scalar steering condition per independent difference; cancellable under a span hypothesis like (S).
 (d) A continuum of pieces (scale-dependent decompositions B_t, t in [s_1, T_0]): the conditions (B_t - B_{t'})(xhat') = 0 for all t, t' are
     infinitely many; by 3.2 they are equivalent to exact replication at f' of the relative block positions u_{k,m}(x')/|R_m x'| on the union
     of the supports of the block parts, plus smallness of a d-mismatch remainder. This is the precise form in which the mixed term is an
     obstruction (HEURISTIC that it cannot be avoided by other decompositions; PROVED as an identity, 3.2).
*Proof.* d/d delta of (U*a + delta U*y)/||U*a + delta U*y|| at 0 is (U*y - <U*y, e> e)/nu. Then B(Ue(delta)) - B(Ue) = <U*B, e(delta) - e>, and
<U*B, P_{e-perp}U*y> = <P_{e-perp}U*B, P_{e-perp}U*y>. The remainder is bounded by the second derivative of e(.) on a neighbourhood. (a): Lemma 1.3.
(b): for the two transported decompositions, B+ - B- = rho v (Thm 2.1 (2.1.2)) and both have zero first-order term iff v(xhat') = 0; the derivative
of v(xhat') w.r.t. the mass is the displayed mixed-term difference. QED.

## 3.2 Proposition (consistency identity for a family of transported decompositions). PROVED.
Let (B_t, omega_t), t in an index set T, be decompositions of g at f with omega_t = (omega_{t,m}) finitely supported off-peak, d_{t,m} :=
<D w_m, D omega_{t,m}>/C_m, g = B_t + sum_m R_m*(omega_{t,m} - d_{t,m} w_m). Let f' be NA with supp omega_t off P'_m, g' := rho(g'' - c a') as in Thm 2.1
for some reference, and put d'_{t,m} := <D w'_m, D omega_{t,m}>/C'_m, B'_t := g' - rho sum_m R_m*(omega_{t,m} - d'_{t,m} w'_m). Then each B'_t has
B'_t(xhat') = 0 and the block parts have zero first-order terms, and for t, t' in T:
   B'_t - B'_{t'} - rho (B_t - B_{t'}) = -rho sum_m [ (Delta'_m - Delta_m) R_m* w'_m + Delta_m R_m*(w'_m - w_m) ],
   Delta_m := d_{t',m} - d_{t,m},  Delta'_m := d'_{t',m} - d'_{t,m} = <D w'_m, D(omega_{t',m} - omega_{t,m})>/C'_m
            = (1/|R_m x'|_m) (R_m*(omega_{t',m} - omega_{t,m}))(x').
Hence the transported pieces reproduce the transfers of f exactly (up to the two displayed vectors) iff
 (i) (consistency/steering) Delta'_m = Delta_m for all pairs, i.e. (R_m* omega)(x')/|R_m x'|_m = (R_m* omega)(xi)/|zeta_m|_m for omega in the span of the
     differences omega_{t'} - omega_t; and
 (ii) (d-mismatch) sum_m Delta_m R_m*(w'_m - w_m) is negligible (it vanishes when the data are d-neutral, Delta_m = 0).
Both remainder vectors are Y-vectors spread over all coordinates; their parts on non-contact coordinates outside supp a' cost FIRST order
(|tau| times their l_1 mass there, Lemma 1.3), so at scales tau >= s_1 they must be <= eps_0 s_1 in l_1.
*Proof.* Algebra from the definitions (as (2.1.2)); B'_t(xhat') = 0 by Lemma 1.3. Delta'_m formula: Lemma 1.1 at f' (off-peak w'(k) =
C' lambda_k u_k(x')/(Phi_k^2|R_m x'|)). At f the same formula with xi gives Delta_m = (R_m*(omega_{t'} - omega_t))(xi)/|zeta_m|. QED.
Reading: (i) is the multi-piece version of the steering condition (and the base-side manifestation of (i) is the mixed term of 3.1);
for a FINITE family it is a finite set of linear conditions on x' (Thm 2.1 handles one), for a scale-dependent family whose block
supports reach depth ~ t (all small t), it is exact replication of infinitely many relative positions (part 4).

## 3.3 Proposition (non-neutral two-piece data: the garbage identity). PROVED.
Run the construction of Thm 2.1 for two-piece data with Delta d_m != 0, steering instead d'^-_m - d'^+_m = Delta d_m (one scalar condition per block,
equivalently v_m(x')/|R_m x'| = v_m(xi)/|zeta_m| with v_m := R_m* omega_Delta,m). Then (2.1.2) becomes
   B^+ = B^theta + rho theta (v + E),  B^- = B^theta - rho(1-theta)(v + E),  E := -sum_m Delta d_m R_m*(w'_m - w_m),
and the proof of Thm 2.1 goes through verbatim provided, in addition, ||E||_1 <= eps_0 s_1/(2 rho) (E's first-order cost is <= 2 rho |tau| ||E||_1
on each side, also on supp a' where it may cause flips). This is the ONLY change.
*Proof.* As (2.1.2), using 3.2 with Delta'_m = Delta_m. QED.
Why this is delicate (HEURISTIC, with the PROVED clamp formula 1.1): the window masses (size ~ s_1) move xhat' by ~ s_1 in sup norm (through e');
by Lemma 1.1 every strict non-peak k with Phi_m(k) >~ s_1 changes by ~ s_1/Phi_m(k) (until clamped), so without retuning
||R_m*(w'_m - w_m)|| ~ s_1 * #{strict non-peaks k : Phi_m(k) >~ s_1} + (weight of peaks with margin < s_1), which is NOT <= eps_0 s_1 when block m has
infinitely many strict non-peaks (generic f, Preprint A Remark) or dense near-threshold peaks. With finitely many non-peaks the change can be
undone by finitely many tuning moves; this gives 3.4.

## 3.4 Theorem (non-neutral two-piece mates at block-tame active blocks). SKETCH (all estimates given; the uniform implicit-function step is routine).
Let f, g, rho be as in Thm 2.1 except that Delta d_m != 0 is allowed. Assume for every m in I_0:
 (i) Qbar_m := {strict non-peaks} cup {degenerate peaks (alpha_{m,k} = 0)} is finite;
 (ii) (margin sparsity, C_notes (MS)) sum_{k in P_m : 0 < mu_{m,k} < s} Phi_m(k) = o(s) as s -> 0, mu_{m,k} := |u_{k,m}(xi)| - theta_m Phi_m(k);
 (iii) (tuning span) for some gamma > 0 the restrictions to J_gamma of the functionals psi_{k,m} := u_{k,m} - (u_{k,m}(xi)/|zeta_m|_m) R_m* w_m
      (k in Qbar_m, m in I_0) are linearly independent.
Then (f, rho g) is in cl NA whenever rho^2 kappa < 1 (no steering hypothesis (S) is needed).
*Sketch.* Construction of Thm 2.1 without Far set and raising mass (steering is now part of the tuning): window masses as before, N'' last,
and finitely many free tuning moves p at coordinates j_1..j_r in J_gamma chosen so that the matrix (psi_{k,m}(e_{j_i})) has full row rank. Tuning
equations: u_{k,m}(xhat'(p))/|R_m xhat'(p)|_m = u_{k,m}(xi)/|zeta_m|_m, (k,m) in Qbar. The left side is C^1 in p (|R_m(.)|_m restricted to a finite-
dimensional affine family is convex and differentiable, hence C^1), its derivative at the limit is (psi_{k,m}(e_{j_i})/|zeta_m|), surjective by
(iii); along the construction the maps converge in C^1 on a fixed ball (pointwise convergence of differentiable convex functions implies
locally uniform convergence of gradients), and the residuals at p = 0 tend to 0 (masses -> 0, xhat' -> zhat weak*). A uniform surjectivity
(Graves) argument gives solutions p -> 0. After tuning: by Lemma 1.1, w'_m(k) = sign * min(M'_m, C'_m r_m(k)) on Qbar_m (r unchanged), so
d'^-_m - d'^+_m = Delta d_m exactly; peaks with margin >= c_1 s_1 + (deep perturbation) stay peaks with w' = sigma M'; the remaining peaks have total
weight sum lambda_k <= o(s_1) (MS) + o_{N''}(1); the identity C'^2 (1 - rho_0) - (1 - C')^2 S_1 = (changed coordinates) (with rho_0 := sum over
tuned non-peaks of Phi^2 r^2, S_1 := sum over unchanged peaks of Phi^2; the left side is strictly increasing in C') gives |C' - C| = O(sum over
changed k of Phi_m(k)^2) = o(s_1). Hence ||E||_1 <= |Delta d| (||lambda||_1 (1 + max r) |C' - C| + 2M * changed weight) <= eps_0 s_1/(2 rho) at late stages
(N'' chosen after s_1). Apply 3.3. QED (sketch).
Example: P1's example satisfies (i) (Qbar_1 = {2}) and (ii) (margins >= q_0 min(1/4, 2 sqrt Phi), P1 6.0: sum_{mu < s} Phi <= s^2/(4q_0^2) = o(s)),
so non-neutral variants of its exact resonance (carriers with w(k) != 0) are covered once (iii) holds.

## 3.5 What remains open for one-sided-LINEAR (two-piece) mates. OPEN.
 (R1) Delta d != 0 at an active block with infinitely many strict non-peaks or with dense near-threshold peaks (failure of 3.4(i)-(ii)):
      ||R*(w' - w)|| cannot be made <= eps_0 s_1 by finitely many moves; deep retuning of a window of size ~ log(1/s_1) is needed (part 4, (QI)).
 (R2) Several active blocks, d-neutral, without (S) (e.g. all v_m supported in F cup K): steering of the H_0-component then has to use masses
      (directions <P_{e-perp}U*v_m, U*e_j*>), which is plausible but not proved.
 (R3) Second order: kappa > 1/rho^2 for the explicit side decompositions although g in C(f) (the optimal decompositions involve shifts):
      Remark 2.4 (SKETCH).
 (R4) Infinite base support F (near-flip coordinates as one-sided resources): truncation of a at the window turns them into contacts;
      the flip costs must then be transported (A Lemma 6.4 monotone truncation is the natural tool). Not done.
 (R5) Degenerate peaks used linearly as one-sided block resources (the only one-sided block resource compatible with LINEAR usage):
      they can be turned into strict non-peaks with tiny gap at f' by one tuning move each (Lemma 1.1), after which Thm 2.1/3.4 apply.
      SKETCH.
