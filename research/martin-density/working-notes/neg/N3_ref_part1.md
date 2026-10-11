# N3 referee — part 1: Part 1 of N3 (Lemma 1.2, Theorem 1.4, Corollary 1.5, Remark 1.6, Proposition 1.7, Proposition 1.8)

Sources re-read: N3_notes.md (whole), Part I [I] lem:bookkeeping, lem:base, def:certificate, lem:slack, lem:threshold,
eq:margin, def:tame, thm:tamefibre, prop:lowerbound, rem:onesided, prop:exact, cor:twosided, prop:approximants,
prop:continuity, prop:smooth, def:admissible, eq:Lstar; Part II lem:II-sandwich, cor:II-S1, cor:II-S2, prop:II-S3,
thm:II-NL, rem:II-NL; N1 referee (Lemma 1.4, P-1b).

## R1.1 Lemma 1.2 (switching budget) — CORRECT (re-derived)

Re-derivation.  For a decomposition f + tg = A + L*W with max(q*(A), ||W||) <= 1 + e, [I, lem:bookkeeping(a)] with
h = tg and g(xi) = 0 gives q_0 lin_b(A) + sum_m sigma_m lin_m(W_m) = 0; adding q_0 x (q*(A) = 1 + lin_b + G_b <= 1 + e)
and sigma_m x (N_m(W_m) = 1 + lin_m + G_m <= 1 + e) gives q_0 G_b(A) + sum sigma_m G_m(W_m) <= e.  [I, lem:bookkeeping(b)]:
G_b(a + B) >= Exc(B) = sum_j (|a_j + B_j| - |a_j| - z_j B_j).  For j notin F: |tb| - z tb = t[(1-|z|)|b| + 2(zb)_-]
(cases zb >= 0, zb < 0).  For j in F (z_j = sgn a_j): with y = |a_j| + t z_j b, |a_j + tb| - z_j(a_j + tb) = |y| - y = 2 y_-
= 2t(z_j b + |a_j|/t)_-.  Side - is the same with -tB-.  (c) follows from (x - y)_- <= x_- + y_+.  All constants agree.
Remarks (precisions, no change of content):
 P1.1  The proof uses only max(q*(A), ||W||) <= 1 + e, not optimality: every result of N3 that uses scale-t pairs holds
       verbatim for "e-feasible pairs" (decompositions with component norms <= 1 + e).  This matters for Theorem 3.1,
       whose decompositions (engineered, rebalanced) are e-feasible but not known to be optimal.
 P1.2  The task summary's phrase "support usage beyond the anti-sign allowance |a_j|/t" is accurate for (a), (b); in
       (c) the allowance is 2|a_j|/t.

## R1.2 Theorem 1.4 (de-switching) — CORRECT (re-derived)

(a): a maximizing sequence Delta_n (||Delta_n|| <= M, leakage <= 1/n, ||L*Delta_n||_1 >= c/2) has a weak* convergent
subsequence (V separable); L compact => L* is weak*-to-norm continuous on bounded sets, so L*Delta_n -> L*Delta in l_1,
||L*Delta||_1 >= c/2, leakage(L*Delta) = 0, so L*Delta is supported in the finite set F u K, and L*Delta in Y n c_00 = {0}
([I, eq:Lstar], (T-c)).  (b), (c) as stated.  At an NA row z' in c_0 (z' = xhat' - U e', both in c_0), so K' is finite;
F' is finite by [I, prop:smooth(c)].  Hypotheses used: (T-b) is not needed, (T-c) is essential.
Supplement (used later, R3): the sup defining omega_f(M, r) is ATTAINED (the feasible set is weak* compact because
Delta -> leakage(L*Delta) and Delta -> ||L*Delta||_1 are weak* continuous on bounded sets), omega_f(M, r) =
M omega_f(1, r/M), omega_f(1, .) is right-continuous, hence omega_f(., r) is left-continuous in M.  PROVED (two lines,
written out in N3_ref_notes §1).

## R1.3 Corollary 1.5 (migration) — CORRECT; one gloss imprecise

The proof is complete: finite-dimensionality of {Delta supported in Lambda}, injectivity of L* on V*, leakage of the
normalized limit 0, contradiction with Y n c_00 = {0}.
 P1.3  The parenthetical "these carriers have weights comparable to or below the scale" does not follow as written.  What
       follows from |Delta Omega_n(k,m)| <= 5/t_n is: for every finite Lambda, the total weight of the carriers outside
       Lambda that are USED at scale t_n is >= (c(Lambda)/5) t_n, where c(Lambda) := liminf_n D_n(Lambda) > 0.  This is a
       lower bound on used weight, not an upper bound on individual weights.  Replace the gloss accordingly.

## R1.4 Remark 1.6 — CORRECT with one implicit hypothesis

(c) "leakage of V_inf at f_N is exactly its mass on K n (N, infinity)" needs F subset [1, N] (else V_inf also leaks on
the truncated support F n (N, infinity) of a canonical truncation) — automatic for F finite and N >= max F.  State it.

## R1.5 Proposition 1.7 (rigidity at C-tame NA rows) — CORRECT as a citation

(a) = [I, thm:tamefibre] at eta = x' (C-tame: a' in c_00, K' finite automatic at NA rows; Q-bar'_m finite; (MS));
uniqueness of data by [I, lem:rigidity] (stated after def:tame).  (b) = [I, prop:lowerbound] (hypotheses: a in c_00,
K finite, Q_m finite, no degenerate peaks, (MS)) + [I, rem:onesided(a)].  (c) immediate from (a).  (d) r(c) <= 1/||b/a||_inf
is part of [I, def:certificate].
 P1.4  (d)'s gloss "a mate that uses a bank two-sidedly has radius at most (bank mass)/(coefficient)": r(c') is the
       radius of the SUFFICIENT expansion of [I, prop:expansion]; it is not a constraint on mates.  The genuine
       constraint is Proposition 1.8 (one-sidedness above the capacity scale).
 P1.5  Essential observation for what follows (not stated in N3): the profile identity (c) is an ALGEBRAIC consequence of
       exactness of the data — every peak k of P'_m, however small its alpha'(k) (cofinitely many, almost all of them
       of weight alpha' = lambda mu'/sigma' -> 0), enters g' only through the common term -d'_m psi'_m.  No quantitative
       (scale-t) argument that treats weak peaks individually can reproduce it (see R2.3).

## R1.6 Proposition 1.8 (bank capacity) — CORRECT; one hypothesis missing

(x)_- <= (x + c)_- + c (c >= 0) and Lemma 1.2(a) at f' (sum_{F'} 2(z'B + |a'|/t)_- <= t/(2c')) give the bound.
 P1.6  "min_{j in F}|a'_n(j)| -> min_F |a_j| > 0" requires F finite (for F infinite min_F |a_j| = 0).  Add "F finite".
 P1.7  The positions of banks are constrained near f (N1 referee P-1b, Cor 1.4''): inside any fixed window a bank can sit
       only on F, on a contact of f with the contact sign, or on a near-contact; a FIXED free coordinate j of f
       (|z_j| < 1) can never be a bank of an approximant close to f, because z'_j -> z_j and banks force |z'_j| = 1.
       This is used below (R2.6): free coordinates of f are exactly the coordinates where "aligned or banked" cannot be
       met by banking.

## Summary of part 1
All five claims are correct.  Required precisions: P1.3 (gloss of Cor 1.5), P1.6 (F finite in Prop 1.8), F subset [1,N]
in Remark 1.6(c).  Useful supplements: P1.1 (e-feasible pairs), attainment/left-continuity of omega_f (used to make
Cor 2.8's M_t well defined), P1.5 (exactness locks weak peaks; key for R2), P1.7 (free coordinates of f cannot be banked).
