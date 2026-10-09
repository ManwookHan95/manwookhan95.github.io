# P2 referee — part 5: other statements, cross-references, numerics

## Other statements of P2A (not in the assigned list, checked in passing)
* 3.3 "Why this is delicate" and 3.5 (R1)/4.6 (R1) ("what breaks engineering is infinitely many strict non-peaks"): an artefact of
  putting the d-mismatch E = -Delta d R*(w'-w) into the BASE (l_1-displacement Theta(s_1)). The concurrent instance P2x (Thm 3.5,
  refereed CORRECT in the P2x referee report) keeps the mismatch in the BLOCK as a multiple of (w - w') and pays only the Bregman excess
  e(zhat; xhat') = o(s_1) (P2x 2.2-2.3), with NO finiteness of non-peaks, for Delta d_m >= 0 under the cone condition (TC). So the
  residual class (R1) should read: Delta d_m < 0 (any structure), and Delta d_m > 0 when (TC) fails and pulls are needed (far-tail
  comparison) — consistent with part 3 (Far-flip collateral damage).
* 3.5 (R5)/4.4(4)(c) (degenerate peaks "turned into strict non-peaks with tiny gap at f' by one tuning move, after which Thm 2.1/3.4
  apply"): Thm 2.1 needs off-peak carriers AT f with gaps >= gamma_0 (Step 4: coordinatewise radius >= rho T_0, T_0 fixed). A tiny implanted
  gap gamma' gives a two-sided radius ~ gamma'; what is needed is a ONE-SIDED box estimate (inward use only: |W(k)| decreasing; outward use
  raises the sup norm at first order — the P2x referee makes the same point for P2x 4.4(b)) plus a theta-certificate with capacity
  gamma' >~ s_1 |omega(k)| for |tau| <= s_1. Plausible, but "Thm 2.1 applies" is not accurate; SKETCH with a missing lemma.
  (Fact C gives w(k) = C zeta(k)/(Phi^2|zeta|) also at degenerate peaks (alpha_k = 0), so the d-identities extend.)
* 4.5 ("C's implant-scale-gap heuristic as an obstruction: FALSE"): C (C_part6 9.3) only claims that the window (Phi, sqrt Phi) "must be
  covered by structure that xi and x' share" and that implants are "never the sole support of a mate component at intermediate
  scales". Thm 2.1 is CONSISTENT with this (the masses serve |tau| <= s_1; (s_1, T_0) is covered by the exactly transferred one-sided
  decompositions of f = shared structure). The FALSE verdict attacks a stronger statement C did not make; correct reading:
  "not an obstruction to engineered recovery when the intermediate band is carried by transferred structure".
* 4.4 (QI): labels (identities PROVED / necessity HEURISTIC / OPEN) are appropriate; with the Lemma 4.1 correction the depth condition
  becomes theta log(1/theta) <~ eps_0 s_J^2.

## Numerics (independent; scripts in ctx/r2/P2Aref_work/)
* thm34_dependence3.py: accurate block norming via the clamp-consistency equation mu|zeta| = C (Lemma 1.1); 24 random blocks with
  non-peaks at half threshold: |N(w) - 1| <= 1e-16, Fact C <omega, zeta> = |zeta| d(omega) to 9e-11 (relative), and the identity
  sum_k lambda_k omega(k) psi_k = R*omega - d R*w to 4e-14 (relative). This is the identity that makes Thm 3.4 (iii) impossible.
  (A first version with grid maximisation of <w,zeta> over M had 1e-3 errors: the objective is flat at its maximum; the consistency
  equation is the well-conditioned characterisation. If no sign change exists, the optimum is the boundary M = 1/(1+||Phi||), all peaks.)
* lemma41_log.py: exact rational computation of the counterexample to "sum_{Phi<theta} lambda <= 2m theta" (ratio grows like
  sqrt(log2(1/theta)), 20.8 at log2(1/theta) = 362).
* I did not re-run a finite-model test of Thm 2.1: in finite models every functional attains its norm and the unsteered pair is also
  contractive (the author says so), so such tests cannot discriminate; the proof was checked by hand instead (part 2).

## Cross-check with the other P2 referee (P2x report, now in P2_referee.md, written 01:21)
Agreement: P2A Thm 2.1 CORRECT; Far flips break the Bregman/E bound for Delta d > 0 with pulls (their 3.2, my part 3); on free
coordinates sum_m V_m(j) = v(j) = 0 so free moves cannot steer the total direction (their 3.4 "structure of (TC)", which is the
one-line reason for my Proposition R1 refuting P2A Thm 3.4 (iii)). New here: Thm 3.4 vacuity, Cor 2.3(b) missing hypothesis,
Rem 2.4 consequence unsupported, Lemma 4.1 log factor, Prop 4.3 gap, Prop 3.3 path-uniformity, 4.5 mischaracterisation.
