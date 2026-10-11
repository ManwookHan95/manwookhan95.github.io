# N3 referee — part 3: Theorem 2.7, Corollary 2.8, Proposition 2.9, Lemma 2.10, Theorem 3.1, Propositions 3.2, 3.3,
# Problem 3.4, numerics; and a correct replacement of Corollary 2.4

## R3.1 Theorem 2.7 (bank–de-switching inequality) — CORRECT (re-derived)
With c := -(d+ + d-)/2: |pi(j) - c| <= (d+ - d-)_+/2 + e+_j + e-_j (checked in both cases d+ >= d-, d+ < d-; in the second
case the sandwich forces |d+ - d-| <= e+_j + e-_j).  V_j = (d+ - d-) psi'_j + r-_j - r+_j on S gives
(d+ - d-)_+ ||psi'1_S|| <= ||V1_S|| + sum_S(eps+ + eps-).  Budget: <= t/c' + 2 mu_S/t.  ||V||_1 <= omega_{f'}(M, t/c')
(Theorem 1.4(b), e <= t^2/2, omega nondecreasing in r).  The inequality holds at EVERY row (finiteness of F' u K' is
needed only for omega -> 0).

## R3.2 Corollary 2.8 (dichotomy) — VACUOUS AS STATED (needs H_S = 0, impossible by Lemma R-V); repaired version PROVED
Repaired statement (Corollary 2.8').  In the setting of Theorem 2.7 (alpha-form, or margin form with A_S replaced by
1/c' + 3 |S| l(t)/mu_0 and H_S by H_S(mu_0)), let Osc_S(g'; psi') = kappa' > 0.  For every t in the BAND
   180 H_S/kappa'  <=  t  <=  kappa'/(8 A_S)
(nonempty iff 1440 A_S H_S <= kappa'^2), (i) mu_S >= kappa' t/8, or (ii) every scale-t pair has ||Delta Omega|| > M_t.
Proof: if (ii) fails, Theorem 2.7 gives kappa' <= kappa'/2 + kappa'/8 + kappa'/8 + 2 mu_S/t.  M_t is attained:
omega(M, r) = M omega(1, r/M) and omega(1, .) is right-continuous (weak* compactness), so omega(., r) is left-continuous
in M and omega(M_t, t/c') <= kappa' (supplement in R1.2).  M_t -> infinity as t -> 0 (Theorem 1.4(a)).  QED
Consequence for the narrative: the "banks >~ kappa x de-switching scale" condition is a necessary condition ONLY on the
band above 180 H_S/kappa'.  Below it (in particular at the junction scale s_1 -> 0 of [I, thm:engineered], at late
stages) Theorem 2.7 imposes nothing on mu_S.

## R3.3 Proposition 2.9 — CORRECT.  Weak* limit Delta, ||Delta|| <= M (weak* lsc), V_n -> V_inf in l_1, leakage and
wrong-sign contact mass -> 0, so V_inf = 0 on J and z_j V_inf(j) >= 0 on K; nothing on F (allowance 2|a_j|/t -> inf).
"Exact resonance" is used in the support/sign sense (the hypothesis of [I, prop:exact] is not verified; not needed).
At F, K finite this contradicts Y n c_00 = {0}, consistently with Theorem 1.4.

## R3.4 Lemma 2.10 — CORRECT (the bound does not depend on t; "frak_t" is just frak).  Its gloss "an escape-rate
obstruction does NOT exist" is valid only ABOVE the scale sqrt(frak(N)/delta) of a given truncation; below it the
approximant must de-switch (Theorem 1.4), which is exactly where N3 places the residue.  State the scale range.

## R3.5 Theorem 3.1 (engineered approximants) — identities CORRECT; the "saturation/sharpness" conclusion NOT SUPPORTED
(i) CORRECT ([I, def:engineered]; supp a' = F u {j in K n [1,N_w] : b^theta_j != 0}; z' = z on [1,N''], 0 beyond).
(ii) CORRECT for the pre-rebalancing decompositions of [I, thm:engineered, Step 2] (Step 4 adds transfer-vector terms of
     coefficient O(tau^2), which perturb V by O(tau^2)).  "De-switching scale exactly s_1" is the construction's switch-over
     scale, NOT the de-switching scale of the modulus: the +- switching vector rho v has leakage rho V_{>N''} <= delta s_1/16
     at f' (by (N3)), so omega_{f'} allows that switching down to scale ~ c' rho V_{>N''} << s_1.
(iii) The formulas Osc_S(g'; psi') <= rho ||(b^theta - c a')1_S||_1 and mu_S(f') = 4 rho s_1 ||b^theta 1_S||_1/q*(a'') are
     CORRECT ("exactly visible" is vacuous AND unused in the proof).  The comparison "Cor 2.8(i) met with factor 32" is
     against a vacuous corollary; with Corollary 2.8' the scale t = s_1 lies BELOW the band (180 H_S/kappa' is fixed and
     H_S(f') >= H_S(f) - o(1) by Lemma R-F) at late stages, so there is no necessary condition to compare with.
(iv) Loose: (N1) gives ||V 1_{>N''}|| <= 5 s_1 at scale s_1 (Lemma 2.10), i.e. delta = 5 in the Lemma-2.10 language; the
     operative tail condition is (N3).
Verdict: the CONSEQUENCE paragraph ("every necessary condition ... met up to absolute constants; the conditions are sharp,
not lossy, since the recovering construction saturates them") is not established.  What IS supported: Theorem 2.3's floor
is sharp in its scaling for strict non-peaks (numerics R2.4: Osc_max ~ 1.14 sqrt(H)).

## R3.6 Proposition 3.2 — CORRECT, with a precision
d(x/||x||) = P^perp dx/||x|| at x = U*a; diagonal U (U*e_s* = mu_s k_s orthonormal) and s notin F give
<P^perp U*u, U*e_s*> = mu_s^2 u(s) (since <e, U*e_s*> = mu_s^2 a_s/nu = 0).  Precision: the conclusion about u_k(xhat')
needs z' unchanged at the banks, i.e. banks on contacts of f with sign z_s (as in the proof); a bank at a coordinate with
|z_s| < 1 forces z'_s = sgn a'_s, a first-order change u(s)(sgn a'_s - z_s) independent of the bank mass (and impossible at
a fixed free coordinate near f, P1.7).

## R3.7 Proposition 3.3 — bound CORRECT; conclusion HEURISTIC
|u_k(Delta z')| <= 2||u_k 1_{(N,inf)}||_1 <= 2 frak(N)/lambda_k is immediate.  But (N1) is a SUFFICIENT condition chosen in
one construction, not a necessary condition on approximants; an approximant may move z' at depths where u_k still has
mass.  Hence "compensation must come from one-sided resources at moderate depth" is HEURISTIC (relative to (N1)-type
cut-offs).  Likewise "banks change it by order s_1" is an upper bound.

## R3.8 Problem 3.4 — OPEN; formulation incomplete
(J1) relies on Corollary 2.8, which (repaired) constrains banks only on the band above 180 H_S/kappa'.  More importantly
the formulation only contemplates contacts/support (bankable) coordinates.  The coordinates where banks are impossible —
FREE coordinates of f — are missing; see R3.9.

## R3.9 A correct strengthening of Cor S1, and where a uniform obstruction can live (new; PROVED parts marked)

COROLLARY 2.4' (profile constancy at every row, every mate, under a margin-sparsity RATE at Z).  PROVED (N3_ref_notes §3).
Let I = {1}, f' any row, g' in C(f'), Z = S u {j_f} with j_f free, psi'_{j_f} != 0, every i in S free or aligned with
|z'_i| >= 1/2, S n F' = {}.  Put eta_Z(mu_0) := sum_{k in Q' u {k in P': mu'_k < mu_0}} lambda_k sum_{i in Z} |u_k(i)|.
If eta_Z(mu_0) = o(mu_0 / log^2(1/mu_0)) as mu_0 -> 0, then g' is proportional to psi' on Z.
(The hypothesis forces that no strict non-peak and no degenerate peak sees Z; it is a T-and-row rate condition that
CAN hold for admissible T, unlike exact visibility.  Finite-model check (margin_check.py): a peak seeing S gives
Osc_max at grid level for every margin from 0.125 down to 2e-4; as soon as it crosses the threshold and becomes a strict
non-peak, Osc_max jumps to 0.91-1.14 sqrt(H6).)

LEMMA R-W (what carries a free-coordinate oscillation).  PROVED.  If g in C(f) has pi_g(j) != pi_g(j') at free coordinates
j, j' of f, then eta_{{j,j'}}(mu_0; f) is NOT o(mu_0/log^2(1/mu_0)): either a strict non-peak or degenerate peak of f sees
j or j', or the weighted mass of small-margin peaks seeing j, j' fails the log^2-margin-sparsity rate.  (Contrapositive of
Cor 2.4' with S = {j'}.)

Reading (HEURISTIC, with the PROVED ingredients cited).  (1) Every positive-scale sandwich with a fixed classification
threshold is inherited (Lemma R-F) — N3's point, extended.  (2) Theorem NL's non-LSC is the instability of the
CONSTANCY hypotheses under limits: at C-tame rows f'_n (plain (MS), exact data) constancy off Sigma' holds exactly
(Prop 1.7(c)), and Cor 2.4' gives it at positive scales at any row with the log^2 rate; these hypotheses hold at f'_n with
f'_n-dependent rates and fail at f, while the floors (fixed mu_0) are lower semicontinuous (Lemma R-F).  (3) On contacts/support the exact mechanism is escaped by banking the whole oscillation set in [1, N]
(engineered approximants).  (4) At FREE coordinates of f banks are impossible (P1.7); a recovering NA sequence must, at
every pair j, j' in J(f) where pi_g differs, either cover j or j' by a strict non-peak of f'_n, or violate the rate
hypothesis of Cor 2.4' at {j, j'} (deep near-kernel carriers u_k(x'_n) ~ 0 seeing j, j').  Strict non-peaks of f'_n at
bounded depth are only those of f or former degenerate peaks of f (status continuity); deep ones have vanishing total
weight, and their capacity at positive scales obeys the sqrt-weight law (numerics; Theorem 2.3' gives the upper bound).
So the sharpest negative target exposed by this review is:
 PROBLEM R (uncoverable free-coordinate oscillation).  OPEN.  Find admissible T, f, g in C(f), rho < 1 and free coordinates
 j, j' of f with pi_g(j) != pi_g(j'), carried (Lemma R-W) only by small-margin peaks of f (no strict non-peak or degenerate
 peak of f sees j, j'), such that every NA row f' near f either satisfies the rate hypothesis of Cor 2.4' at {j, j'} or
 carries, through its strict non-peaks and small-margin peaks seeing j, j', less than the needed capacity at the scales
 below the slack scale.  (Needs: a capacity LOWER-bound theory for small-margin peaks at NA rows; the finite model shows
 robust-margin peaks have none.)
This is the same "approximate resonance through weak peaks" core as Part I rem:summablegaps / ADDENDUM (O3), localized at
free coordinates, where the bank escape that defeats every contact-based obstruction is unavailable.

## Summary of part 3
Correct: Theorem 2.7, Proposition 2.9, Lemma 2.10, Theorem 3.1 identities, Propositions 3.2, 3.3 (bounds).
Vacuous/repaired: Corollary 2.8 (band version 2.8').  Not supported: Theorem 3.1's saturation/sharpness consequence;
Prop 3.3's "must come from one-sided resources" (heuristic).  Problem 3.4 OPEN and incomplete (free coordinates).
