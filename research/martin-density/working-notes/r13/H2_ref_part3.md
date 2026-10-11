# H2 referee, part 3: Prop 3.5, Section 5 (NE, bias), 4.4 (D-abs), Theorems H2.B / H

## Proposition 3.5 -- (a)-(c), (e) correct; (d) HEURISTIC (label honest)
(a) In (R1) there is no thick-type carrier, so J1's (R0)-classes (R-pk), (R-np) are vacuous there (they concern thick-type carriers); H1's
    (U+) needs thick-type peaks (H1 Lemma NP(b)), excluded.  Trivial but correct.
(b) peak bank direction -sgn(Delta''_m) is the same for every robust peak of the block (independent of vs_c): re-derived.  "two-sided iff
    capacity >= 4W'": within the toolbox (in (R1) a data-carrying robust peak has no (P1)/(P3)/(P4)), yes.
(c) correct.  (e) = Lemma 2.6 for peaks; correct.

## Section 5
Lemma 5.2 -- correct with precisions: (i) "per banked near contact s" (a kind-(iv) carrier whose near coordinates are all thin with
|a_s| >= theta_0 receives no bias from (P)); (ii) "charging" must mean a ROBUST oriented cofactor (cofactors are rate objects: tiny or
robust); then the shift of lambda^T M is >= u eff v theta_0/kappa >= u theta_0/Design^C >> delta_Z (s_1 <= theta_0 T/(8 rho A_0), (L-K2-1)).
(iii) Further bias sources H2 does not list: (P3) raises of THIN TARGET coordinates and (P2) banks of TARGET contacts move the values of
every carrier whose target contains the coordinate by eff u_k(j) theta_0 (first order, shared); minors containing the (X1^F) contact row of j
are invariant at first order (the value change is proportional to that row), the others are not.
Proposition NE (5.1) -- SKETCH, plausible as a statement about REALIZED ratios (project the class data at an auxiliary exact point, treat
the shift mismatch as tolerated violations).  Not re-proved.
5.3 bias-free preparation -- SKETCH, plausible (TU pair at the Sys-DC scale: pull of capacity ~ 4 K_DC r and compensating bank, net zero first
order).  Its own conclusion is the honest one: residual = fully swallowed kind-(iv) carriers, or f on the wrong side of a one-signed
resonance by MORE than delta_Z.
5.4 -- the argument FAILS.  It assumes the design clause C_L((1 + Lip C_*) b(w))^{2/N_L} <= delta_Z ("b only appears as an upper threshold").
This is FALSE: by (K2-d) theta_0 = b/Design^{C_P} and by (L-K2-1) s_1 <= theta_0 T/(8 rho A_0), so
      b = Design^{C_P} theta_0 >= 8 rho A_0 Design^{C_P} s_1/T,   while   delta_Z <= delta s_1/(64 rho C_f Design^C).
Since b < 1 and N_L >= 2, b^{2/N_L} >= b, and C_L >= Design^{-C} (dist(r, Z) <= C_L |minor|^{2/N_L} cannot beat the transversal linear case
|minor|/|grad minor|), the clause would need T >= 512 rho^2 A_0 C_f Design^{C_P + 2C}/delta: impossible for small T.  Decoupling theta_0 from b
does not help: (P3)/(P2) at thin target coordinates/target contacts move pinned values by ~ eff theta_0 >> s_1/T >> delta_Z (theta_0 must
exceed s_1 A_0/T by (L-K2-1) and 4 Design K_DC r by (L-K2-2)).  So the start row is NOT within delta_Z of Z_kappa in general (its distance
is up to C_L (2b)^{2/N_L}), the Lojasiewicz displacement remains, and in EVERY block type a wrong-sided one-signed resonance of f with
delta_Z < lambda^T M(r_1) <= C b obstructs.  Hence 5.4 (a), (b) ("no obstruction") and the bottom-line claim (6) / summary "the pinned
residual would disappear in unshifted blocks and in shifted blocks without near-threshold actives, leaving inward-locked near-threshold
kind-(iv) carriers of (T)-blocks as the core" do NOT follow; they contradict H2's own 5.3 sentence.  Correct reading: under NE + 5.3 the
residual consists of (i) wrong-sided one-signed resonances of f's stage data by more than delta_Z (any block type), (ii) fully swallowed
kind-(iv) carriers, (iii) the (T)-block near-threshold phenomena.  NE buys only the window delta_Z << b of near-coincidences.

## 4.4 design variant (D-abs) -- SKETCH, plausible; label honest
With E^ch'(p) := T(p) ∪ (Z_0 ∩ [1, p]): T(L) ∩ (union S_k) ⊂ [1, r(L)] (main targets (D-enum), PRE absorbers Sigma(Y_r) ⊂ [1, r], cluster
absorbers only on T(p) ∪ Z_0).  Re-checked: old near coordinates s in (s_max(p), d(p)] and old pull-range coordinates j stay private while
r(L'') < s (resp. j); design depth (D(L'') >= s_max(p+1) >= 4/T_lo(p, M(p)) > j); unraised (J > D); Lemma 2.1 at any (R1) stage L''.  So the
memory claims hold for every later (R1) stage of round < s_max(p) (intermediate stages need not be (R1)).  At most N (up)/(down) events per
range: each block uses one robust peak c, which forbids both shift signs at later (R1) stages (2.6 + 2.7(a)).  Still to check: (W4'')
upper bounds (fewer constraints: weights may only get larger, but (W1) c_l <= c_{l-1}/4 and (W_exp) at p+1 persist; the cluster stage p+1
still exists since 1 in Z_0 ∩ [1, p], so s_max(p+1) >= 4/T_lo(p, M(p)) persists); absorbers are off the MT VI tree (Q1-refa, X2-ref R-abs).

## Theorems H2.B / H -- correct as necessary conditions, with quantifier precisions
(Q-1) "the selected stage" must read "every clean sub-window and class with >= n(w)/D_cl(w) scales": non-coverage of (LSC-trunc) means no
(w, a) at the stage is realized.  (Q-2) H2.B (iv) / H (b)(iv) need CONSECUTIVE (R1) stages (memory of T_fin reaches one stage for 2.7(a), two
for 2.6); for interleaved (R0)/(R1) stages only (i)-(iii) are per-stage conclusions.  (Q-3) Prop 4.1's identification of the unshifted-block
residual with a Farkas alternative holds only in the restricted single-block model (part 2).
