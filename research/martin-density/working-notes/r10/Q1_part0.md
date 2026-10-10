# Q1 part 0 — reading notes and plan (working file)

Sources read: BRIEFING, BRIEFING_R2 (ADDENDA 1-9), martin_paper_summary, note Sec 1 (def:admissible, lem:martintail),
r9 X1_referee, X1_ref_notes, X1_notes, X2_referee, X2_ref_notes, X2_notes; r8 U1_referee, U1_ref_notes, U1_notes parts 2-3,
U4_referee, U4_notes Sections 1-4.

Key refereed facts used by Q1 (with exact sources):
* T_final (U4 1.1-1.3): base mu_s = 2^{-s^2-1}; S_l = {2^l(2i+1)}; stage l: (1) target, (2) delta_l by (GM) (l >= 2), (3) n_l, u_l,
  (4) c_l = min (W1)-(W7) (c_1 = 1), (5) level data + Design(l), (6) sub-windows. U4-ref: CORRECT; fixes C1 (B_mu), C7 ((GM) l >= 2).
* D^{U1'} (U1-ref 6.2): rounds PRE (absorber pairs, block 1) - MAIN (block m_r) - CLUSTER (biased pairs for E^ch(p)); absorber
  targets (A0) with R from c_p^low; cluster weights c_{p+i} = c_{p+1}^low 4^{1-i}; (W4'') at PRE/MAIN; sub-window data at every stage;
  windows used only at main stages; admissible, N-free (6.3).
* X1-ref: KN^tr PROVED with fixes KN-1 (hold inactive Omega values of (T)-blocks at exactly 0 in the joint fixed point), D2
  (inactive near-threshold carriers of (U)-blocks pushed inward), S-0 (later drifts <= C Design c_{L+1} <= C Design mu^2 << mu),
  K1 (formula-1 kappa with the pattern's Omega), W-fix (eps_K := sigma_rob/4), W1 (option (a) is Martin-type, outside (T-a) equality),
  W2 (N = 1 inside the class with m(1) = 2), W3 (absorber R from (1 - 2^{-p}) c_p^low; cluster maxima), W4 (lower-bound uses).
* X2-ref: Theorem UE, E^eng, (S2c) correct after precisions; Lemma LV(d) FALSE in application (absorber levers); repair (R-abs):
  absorbers carry no switching; Lemma CM' + Theorem C_mix' PROVED; MT V PROVED after (R-abs); (p-W): (W_exp) only after MAIN
  stages; n_l in (D-lev); referee addition 1.2: d-consistency on all coarse strict non-peaks freezes C_m up to fine terms.

PLAN.
 (1) T_fin = D^{U1'} on T_final + X1 3.1 changes (rate objects of KN^tr, thresholds (D1), (D2), generic weights) + X2's (D-lev) with
     n_l and (W_exp) after main stages only.  One recursion; admissibility; N-freeness; genericity (k_0 countable, weights
     transcendental in the intervals [(1 - 2^{-l}) c_l^max, c_l^max]); compatibility with every upper and lower bound.
 (2) Routes: unshifted classes -> U1-ref MT IV' (V2 Theorem B values only), no (KN) needed; one-signed -> either X1's MT IV^tr
     (exact route) or the violation-tolerant route; mixed -> violation-tolerant route (X2-ref Theorem C_mix') with step (1a) :=
     Proposition KN^tr instead of U1-ref Proposition KN.  Check: KN^tr companion as base row f_0 of Theorem UE (hypotheses (U1)-(U7)),
     gap_min with Puiseux exponent, s_late, (W_exp), levers vs mu.
 (3) Master Theorem VI + consequence via Z5 Prop 5.4.
