# X2 part 6 — The resulting master theorem for F finite, the residual, corrections, numerics

## 6.1 The design D^{X2}.
D^{X2} := U1-ref's D^{U1'} (built on U4's T_final: SLD with S_l = {2^l(2i+1)}, allowedness (a), (c), (c''), diagonal base mu_s = 2^{-s^2-1},
pigeonhole sub-windows, absorber pre-pairs/clusters, weights (W1)-(W5), (W7), (W4'')) plus two ladder conditions:
 (D-lev) Design(L) >= max_{l <= L} 2^{sigma_2(L)}/(mu_{sigma_2(L)}^2 delta_l)   (efficiency of the d-consistency levers, Lemma LV);
 (W_exp) c_{l+1} <= exp(-1/T_lo(l, M(l)))   (an upper bound on weights; added to c_p^low in D^{U1'}).
Both are computable at the stage where they are imposed, independent of N and of f; admissibility (T-a)-(T-d), (P1), (P2) and N-freeness are
unaffected (they use weights only through upper bounds and Design only through lower bounds); every refereed result valid for D^{U1'}
remains valid (U4 Lemma GW: window results use a window only through properties preserved by enlarging Design and shrinking weights).
PROVED (by inspection, as for U3's (W10) and V4's design conditions).

## 6.2 MASTER THEOREM V (F finite).  PROVED modulo the refereed results it cites (V2 MT III'; U1-ref MT IV', Proposition KN, Section 5-7
## fixes; U1 Lemmas 1.1, 1.3, 2.1, 2.4, 3.2-3.4, 4.1-4.6, Proposition 2.2; V1 TR, TU, ST, CO; Z3 Lemma 3.1; the note's lemmas) and parts 1-5.
Design D^{X2}, N fixed, f in S_{p_N^*} with finite base support F.  If
   for infinitely many main stages L some clean sub-window w of L has at least n(w)/D_cls(w) dyadic scales whose activity class a
   satisfies (KN_{w,a}) — one-signed OR MIXED —,
then f in Rec(p_N), i.e. (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f).
Proof.  Pigeonhole (U1 MT IV') gives a (class, cube) set S with |S| >= n(w)/D_cls(w)^2.  One-signed classes: U1-ref MT IV' (refereed), or
Theorem C_mix's argument.  Mixed classes: Theorem C_mix (5.2): Lemma CM's companion, the window family (U1)-(U7) with fine-origin contact
violations of mass <= 4 C_Delta c_{L+1}, levers by Lemma LV, Theorem UE at each companion, Theorem E^eng along the windows ((E-f) by (W_exp),
(E-d), (E-e) as in MT IV').  QED
COROLLARY (contrapositive; the F-finite residual).  If f (F finite) is not in Rec(p_N) for D^{X2}, then f is a (C*) row (V2 MT III') AND for all
but finitely many main stages L, at EVERY clean sub-window w of L, more than n(w)(1 - 1/D_cls(w)) of the scales lie in activity classes a for
which (KN_{w,a}) FAILS: some active block contains an active near-threshold switching carrier (|rho - 1| <= b(w)) and every inactive
Omega carrier of that block has rho < u(w) (nearly neutral).  This is exactly U1-ref's STATUS COHERENCE problem (OPEN; task X1).
In particular: (C_mix), (S2) = (S2a') + (S2b) + (S2c) of ADDENDUM 8 are CLOSED; (S1) (multi-block coupling) is part of the exactification of
Gamma^#(kappa, a), which Proposition KN performs for all blocks at once, so it is contained in the (KN) residual; U3's RT*(c) is superseded by
U1's coarse exactness (Proposition 2.2 + absorbers).
Status of the density problem (unchanged in kind): Lemma Z at finite F for D^{X2} <= status coherence; Lemma Z at infinite F: (E1)-(E5) of
ADDENDUM 7 / U2's items; density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2): OPEN for every admissible T.  No counterexample is
claimed; nothing found points to one (every obstruction met here was removed by an exact cancellation or by a design choice).

## 6.3 What is new in X2 (labels).
 (1) Proposition J (PROVED): for VALID data (Gamma_w <= 2) the junction mismatch of thm:engineered is O(|Omega_m|^{1/2} ||X||), uniform in the
     piece scale t (U1 Lemma 2.1 bounds ||D Domega||_2; the diagonal base bounds the mass effects by ||X||); U3-ref F6a's s_1/t^2 came from a
     datum scaled by 1/t (Gamma ~ t^{-2}).  Non-uniform along windows (n, |Omega|) -> exact cancellation needed.  [PRECISION of U3-ref F6a.]
 (2) Lemma DC (PROVED): exact d-consistency by levers; the linearization is I - p q^T (rank one through the block norm), invertible with
     1 - q^T p >= 1 - C_m >= 1/2 (Sherman-Morrison), plus block-triangular absorber couplings; Poincare-Miranda gives an exact zero.  No
     kappa-neutral lever is needed for d-consistency (contrast: status coherence).  Numerically: J_fd = I - p q^T to 2e-10.
 (3) Lemma LV (PROVED): levers exist at U1's companions: (TU) for active class-G carriers, zero-data (Z-con)/(Z-free) levers for inactive and
     class-R carriers (exactness on E_c makes V = 0 there), (S-mass) at absorbers' tuning coordinates; design addition (D-lev).
 (4) Lemma UE-1 and Theorem UE (PROVED): uniform per-piece engineered bounds, T_0 = c_flat t with c_flat an f-constant (window-dependent only
     through gamma_B, as in V1), violation tolerant, with explicit late threshold s_late (a window quantity).
 (5) Theorem E^eng (PROVED): averaging at the norm-attaining approximant; no exact averaged data needed (U3's (S2b)).
 (6) (S2c) (PROVED arithmetic): the threshold comparison holds with (W_exp); (W10) does not suffice for the s_late obtained here (~T^{15}).
 (7) Lemma CM / Theorem C_mix (PROVED): mixed classes recovered by the self-aligned completion (negatives (R), positives anti-aligned) with
     fine-origin contact violations; frustration (U1 5.4-5.5) is harmless.  U1's Corollary IV.2 is superseded.
 (8) Master Theorem V (PROVED modulo refereed tools): the F-finite residual is exactly status coherence ((KN) failure) at (C*) rows.

## 6.4 Numerics (X2_work/; sanity checks only — finite models cannot exhibit infinite-dimensional failures)
 dcons_check.py:  N = 1 model, exact data (Gamma^+ = 0.0064, Gamma^- = 0.031): untuned kappa/||X|| = 0.0230 for s_1 = 1e-2 ... 1e-5 (linear in ||X||,
                  Proposition J); one (TU) lever restores nv exactly (residual <= 2e-17), kappa_tuned <= 3e-17.
 dcons_check2.py: same with long signature sets and the pull chosen with v(j_p) in [2 du, 2^G 2 du]: bank mass / ||X|| = 15-26, kappa_tuned <= 3e-17.
 dc_jacobian.py:  6 random blocks with |Omega| = 2 and (Z-free) levers: finite-difference Jacobian of F equals I - p q^T to 2.1e-10; 1 - q.p
                  exceeds 1 - C by >= 0.153 (prediction >= 0).
 ue_check.py:     violated piece (eps = 1.6e-4 at a peak's signature contact), engineered approximants with s_1 in {64 rho eps/delta, 4 rho eps/delta,
                  eps/20}, tuned and untuned, true p* by SOCP on a tau-grid in [1e-4, 0.05]: the bound 1 + (tau^2/2)(1 - delta) holds in all six cases
                  (max excess <= -2.6e-9, solver accuracy ~ 4e-9).  In this model even the sub-threshold and untuned variants satisfy the bound:
                  the SOCP rebalances optimally (finite models have no transfer inefficiency, and the violated contact is not a dead zone);
                  U3-ref's vt_ref_check.py remains the evidence that (VT) is sharp for dead-zone violations.
