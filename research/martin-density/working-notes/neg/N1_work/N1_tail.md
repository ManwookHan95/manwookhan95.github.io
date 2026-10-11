
# 4. Numerics (sanity checks only; scripts in neg/N1_work/)

No finite-dimensional model can exhibit non-density (every operator on a finite-dimensional space attains its norm); the checks
below only test inequalities used above.
 * twopoint_check.py: smooth norms on R^3 (l_4, and l_4 + 0.3||A.||_2). The support function max_{C(f')} v (LP over 2e3-1e5 sampled
   constraints |g(y)| <= r_{f'}(y), converged to 4 digits) never exceeds inf_tau of the two-point bound of Cor 1.7, and is often strictly
   below the Hessian bound (0.208 vs 0.358; 0.987 vs 1.685): r~ is a genuinely multi-scale infimum and Cor 1.7 is not sharp. Consistent.
 * angle_check.py: Prop 1.5(a) in R^3 with the l_4 norm: for 30 random (f, g, rho, delta) and perturbations of norm < delta, the norming
   direction satisfies |sin phi| <= 0.19 x 2 (delta/(1 - rho^2))^{1/2}. Consistent (random perturbations are far from the worst case).

# 5. Next steps (recommendation to the orchestrator)

 1. Do not abandon the positive programme for T_fin: a counterexample for T_fin needs infinite base support and a failure of
    (LSC-trunc)_N (F7); the negative question is a question about ADVERSARIAL admissible T.
 2. Targeted negative test, in this order:
    (a) Candidate C1 (Section 3.4), N = 1, adversarial base U (slowly decaying ||U^* e_j^*||), a positive proportion of zero-weight strict
        non-peaks at every depth, a two-piece mate with Delta d < 0 and kappa_w = 1. Sub-question: does EVERY norm-attaining approximant
        that terminates the switching at a scale s pay a scrambling mass >~ s on the wrong side (a lower bound for the termination
        footprint), or is there a footprint-free termination through block carriers (escape (e1))? Either answer is progress.
    (b) Aim any non-recovery proof at a TYPE (I) obstruction (Theorem 1.9): one fixed x in c_00 and, for every admissible normer x'
        (Lemma 1.4: window data, arbitrary far data, banks), an explicit cheap multi-scale decomposition of x (Theorem 1.6(c)). This is a
        purely primal, scalar target; it is equivalent to a convex (Hahn-Banach) separation from the local NA set (Prop 1.5bis).
    (c) Only afterwards O3* (C2): build the chain-guard design with alternating types at ratio 1 and escaping errors, and test the boundary
        excess with error carrying switched on (extend E's Model N by R3's EC and by banks).
 3. Positive counterparts that the analysis isolates (each would remove a whole class of potential counterexamples):
    (CAP+) unbounded conversion capacity at some junction for every admissible T; (P-II) a MERGING LEMMA (two NA approximant sequences
    recovering g_1 and g_2 can be merged; then Rec(f) is convex and density reduces to recovering X-exposed mates, Theorem 1.9);
    (P-I) recovery of X-exposed mates (the scalar statement limsup_{NA f' -> f} r~_{f'}(x) = r~_f(x)).
 4. Parallel track N2neg (adversarial construction) should use the necessary conditions of Section 2 as a checklist: any proposed
    (T, f, g) violating one of F1-F6, M1-M6, M8 is recovered by a refereed theorem.
