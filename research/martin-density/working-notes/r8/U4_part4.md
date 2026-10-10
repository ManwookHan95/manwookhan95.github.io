# U4 part 4 — Numerical sanity checks (evidence only; scripts in r8/U4_work/)

## 4.1 tu_mu_check.py (conflict C1: V1 Lemma TU with a super-exponentially decaying diagonal base)
Finite model as in V1-ref tu_check4.py (base support F = {0,1,2}; carriers in L_0 with private bounded-gap signature sets,
v_l(s) = d_l 2^{-alpha s}, exactly swallowed beyond a cutoff; four "other" carriers on F and coarse coordinates), but with base
entries s_j = 2^{-beta j^2}, beta in [0.002, 0.006] (finite-model analogue of mu_s = 2^{-s^2-1}).  Pulls of mass 24 lambda v(j) at a
coordinate with v(j) in [eta, 2^G eta], private banks at the first far signature coordinate, explicit scalar fixed point of V1
Lemma TU.  Tuning sizes eta = fac x reg with reg proportional to min_l s_{j'}^2 v(j') (the quantity B_mu(l) controls).
Output (tu_mu_check.out): 587 tests (613 skipped: no pull coordinate in range in the truncated model), 0 failures (no divergence,
no non-positive bank mass, increments >= eta/2); max |val^# - val^(2) - x| = 9.3e-16 (absolute); other carriers move by
<= 1.6e3 eta^2 with a constant independent of eta over four decades (second order); max |Phi'| at the fixed point 2.6e-3;
bank mass x min(s'^2 v')/eta in [O(1), 13.6]: bank masses scale like eta/(s'^2 v'), i.e. exactly through the factor that
B_mu(l) puts into Design(l).

## 4.2 rr_check.py (conflict C1(v): raise room (RR) needs the mu-base)
Profile on a bounded-gap signature set: W_s = 2^{-s}, |a_s| = 2^{-(1+b)s}; local exponent kappa(y) = log M^W(y)/log y at
y = 2^{-200}, 2^{-400}, 2^{-800} (log-domain arithmetic).  Base 2^{-s}: kappa = 4.0, 2.0, 1.33, 1.0, 0.67, 0.40 for b = 0.5, 1, 1.5, 2,
3, 5, matching 2/b: (RR) (kappa > 1) FAILS for b >= 2.  Base 2^{-s^2-1}: kappa grows without bound (e.g. b = 5: 9, 17, 33), (RR)
holds for every b.  So Theorem RS' needs the mu-base, and V1's design factor must be adapted to it (B_mu).

## 4.3 C7 arithmetic ((GM) at l = 1)
S_1 = {6, 10, 14, ...}, H_1 = 2^{-6}/(1 - 2^{-4}) = 1/60, delta^max_1 = min{1/2, (4 (5/4) H_1)^{-1}} = 1/2.  (GM) with sigma = 0 needs
g_1 <= delta_1 H_1 <= 1/120, and Phi_1 = 2^{-m(1)-k(1)} c_1 <= g_1/2 then forces c_1 <= 2^{m(1)+k(1)}/240 < 1 whenever m(1) + k(1) <= 7
(e.g. (k(1), m(1)) = (1,1): c_1 <= 1/60).  Hence (GM) at l = 1 contradicts c_1 = 1 (norm one); imposing (GM) only for l >= 2 removes
the conflict (V4 Lemma 3.4 uses (GM) only for l > log_2(2 Theta) + 1).
