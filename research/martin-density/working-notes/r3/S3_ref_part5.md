# S3 referee, part 5: 4.3 (quantitative), 4.4 (failure of (MS-Q*)), 4.5 (deep coefficients), global checks

## 5.1 Section 4.3 (quantitative recovery without (SC)). Verdict: the implication is CORRECT; its interpretation is OVERSTATED.
Implication re-derived: on the wrong side the genuine cost is s E_y + 2 s ||R*Z_A||_1 with s = tau rho c^sigma, |c^sigma| <= |Delta d|/2, hence
<= rho (|Delta d|/2) K^scr tau^2 (1 + o(1)) for |tau| >= s_1; each genuine cost sits in one piece, so the max of the levels gets at most
the SUM of them (on a fixed side they are upper-bounded by linear functions of tau and could even be AVERAGED with the weights c', sigma'_m
by first-order rebalancing, which only improves the threshold). With K^scr := limsup (E_y + 2||R*Z_A||_1)/s_1 the condition
rho^2 kappa_w + rho sum |Delta d_m| K_m^scr < 1 suffices; the stated factor 8 is conservative. OK.
Overstatement: "the non-recovered part ... is confined to rho close to 1: rho-defect only" needs K_m^scr < infinity. The note's sufficient
condition ("non-peak gaps bounded below off a finite set") controls only the NON-PEAK part of Scr_m. The PEAK part
sum{min(Phi_k, s) : k in P_m, mu_k <= s} is only O(s log(1/s)) in general (Phi_m(k) <= 2^{-m-k}), and it is ~ (s/2) log2(1/s) if, e.g.,
mu_k ~ 4^{-k} along a density-one (log-counting) subsequence of peaks — compatible with Lemma B, since density of (u_{k,m})_k only
needs a sparse dense subsequence and T can be built after zhat (P1 2.1 technique). Then K^scr = +infinity and 4.3 gives nothing.
Fix: add "(MS) in the block" (then the peak part is o(s)) or state K^scr < infinity as a hypothesis.

## 5.2 Section 4.4 (MS-Q*) can fail. Verdict: the construction is a fair SKETCH; the conclusion about the approximants is OVERSTATED.
 * Failure of (MS-Q*): prescribing u_{2k,1} in zhat-perp (with P1-type signature tails and an e_1*-correction keeping u(zhat) = 0 exactly)
   makes every (2k,1) a strict non-peak with w = 0 and gap M_1, so Scr_1(s) >= c s at every scale. Fine as SKETCH (T-c / P3-type margins
   for the remaining coordinates must be re-checked, as in P1 2.1).
 * Scrambling: u_{2k,1}(xhat') = <U*u_{2k,1}, e' - e> + o(s_1); new peaks wherever s_1 |<U*u, h_N>| >~ theta Phi_{2k}. "A positive proportion"
   needs an equidistribution property of the enumeration of the dense family (arrangeable by construction, not automatic). SKETCH.
 * OVERCLAIM: the head/summary/table say "the simplified approximants then do not recover Delta d < 0 two-piece mates for rho near 1".
   What is shown is only that (SC_1) — a SUFFICIENT condition in an UPPER bound — fails, i.e. Theorem D's estimate does not apply (which is
   what 4.4's body says). Non-recovery along these f'_n would require a LOWER bound dist(rho g, C(f'_n)) >= c > 0 over all targets g'_n, which
   is not attempted. Correct label for that sentence: HEURISTIC (or OPEN).
 * Remark: the unrefereed sibling notes R3 (Theorem EC) convert FINITELY many generic block coordinates into strict non-peaks with w'' = 0 by
   o(1) window moves; 4.4 would need infinitely many (all deep (2k,1) below s_1) at precision ~ theta Phi_{2k} — not covered; the OPEN label stands.

## 5.3 Section 4.5 (deep coefficients c_k ~ sqrt(Phi_k)). Verdict: CORRECT WITH FIXABLE GAPS (missing hypothesis on Phi); not new.
Box tail: k in E(sigma) iff sigma |c_k| > m Phi_k gap_k/2 (the note drops the factor m — harmless); with |c_k| <= K sqrt(Phi_k), gap >= g_0:
E(sigma) within {Phi_k < 4K^2 sigma^2/(m g_0)^2} and T(sigma) <= K sum_{Phi_k < c sigma^2} sqrt(Phi_k).
 * This is O(sigma) only if Phi is regular, e.g. Phi_m(k+1) <= beta Phi_m(k) (the note's parenthetical "geometric Phi"). Lemma B does NOT
   give this: rescaling the columns of T by any 0 < c_{k,m} <= 1 preserves admissibility, so Phi_m(k) = 2^{-m-k} q*(T e_{k,m}) can cluster
   (e.g. ~2j coordinates at level 2^{-j^2}), and then T(sigma) ~ sigma sqrt(log(1/sigma)) and A Cor 6.10(a) does not apply. Martin's own
   Phi_m(k) = 2^{-m-k}|||v*_{k,m}||| is likewise uncontrolled. The hypothesis must be stated (P1's T satisfies it).
 * Further hypotheses that must be kept explicit (they are in the note, not in the claim list): b supported in F (no contact components),
   gaps bounded below on supp omega, and the MAX-form H = max(h(b), H_m) <= 1 (a mate in C(f) need only satisfy weighted-type bounds).
 * "Supersedes C 9.2": correct as a statement about coverage, but A_notes §7.4 ("The borderline case of box tails of exact order sigma:
   RESOLVED", Round 1, refereed) already says exactly this; S3 re-states it.
 * Gamma_w upgrade (SKETCH): plausible. Caveat for whoever writes it: the rebalanced expansion has a radius ~ sqrt(gamma/(t_max(2 + Lambda)))
   that SHRINKS as the inefficiency eta_1 -> 0 (Lambda ~ q*(T)/(m Phi_*) -> infinity); the averaging must therefore be run at fixed eta_1
   (fixed transfer data, radius bounded below) and eta_1 -> 0 taken last. This order works but should be written.

## 5.4 Global adversarial checks (all passed)
 * Hidden assumptions on T: only per-block density of tails (transfer peaks), U* injective (Gram system), Phi_m(k) <= 2^{-m-k}
   (D2(i) log-bound). Exception: 4.5 (Phi regularity), see 5.3. P1's example uses P1's admissible T.
 * c_0 vs l_inf: normers in l_inf only at f (test points, Theorem B); approximants x' = z' + Ue' with z' in c_00. OK.
 * weak* vs norm: f' -> f in norm (P2A Lemma 1.2), g' -> rho g in l_1 (R* w' -> R* w in l_1, beta^sigma -> b^sigma). OK.
 * Uniformity in tau: all estimates hold for 0 < |tau| <= T_0 at late stages with T_0 fixed before (N, s_1, N''); the theta piece covers
   |tau| <= s_1 with NO first-order terms, the side pieces |tau| > s_1 where |tau| o(s_1) <= o(1) tau^2. OK.
 * Attainment: Theorem B attains its minima (Fenchel (a)); D2 uses minimisers. OK.
 * Signs/one-sidedness: s <= 0 on both sides iff Delta d >= 0 (checked); side-- test points need z_j nu_{c,j} >= 0 with t < 0 (checked);
   raising transfers cost the same inefficiency as lowering (checked).
 * Finite vs infinite K: contacts are never moved by the Hilbert part of the test points (Z_t/H_t split), and beyond N'' the side pieces pay
   rho |tau| V_{>N''} <= eps_0 s_1 |tau|. OK.
 * I finite throughout (p_N); Remark martin-tail invoked for p. OK.
 * Consistency with earlier verdicts: C-referee kink phenomenon explained (and reproduced numerically, part 3); P1-referee R3 (canonical
   truncations fail) not contradicted (window masses); N2-referee Lemma R improved (R+), consistent numerically.
