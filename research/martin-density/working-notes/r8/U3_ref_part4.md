# U3-ref part 4 — Part 4 of U3: Lemma QB2, Lemma VT, Proposition RT*, (S1), (S2), Lemma R-pin; numerics

Checked against: note lem:bookkeeping, lem:base, prop:rebalancing, lem:TV, lem:transferdata, lem:persistence, lem:assembly,
def:engineered, lem:approxfacts (E1)-(E5), lem:F1, lem:anchor, def:SC, lem:scrambling, thm:engineered (full proof, Steps 0-6),
lem:twosided, lem:budget, lem:suplevel; V2 Cor. C1.1(a), Lemma 3.1, Def. 3.2; Z3 Lemma 3.1 (companion cost); def:SLD, (P2).
Scripts: U3_ref_work/vt_check.py (re-run, identical), U3_ref_work/vt_ref_check.py (new, independent check of Lemma VT).

## 1. Lemma QB2 (quadratic bank repair).  Verdict: the displayed inequality is CORRECT (trivial); the accounting that makes it
## useful needs four precisions (P4.1)-(P4.4); with them the "quadratic law" stands.
Re-derived: at j in E, z_j = sgn a^b_j, the summand of Exc^b is 2(x - |a^b_j|)_+ with x := -sgn(a^b_j) t B_j, and
2(x - m)_+ <= x^2/(2m) since x^2/(2m) - 2(x - m) = (x - 2m)^2/(2m).  E ⊂ F^b, so b on E is unconstrained.  Correct.
(P4.1) Positive parts.  The sharp bound is 2(x - m)_+ <= (x_+)^2/(2m): at a bank coordinate only the side whose datum is VIOLATED
(z_j b^+_j < 0 for side +, z_j b^-_j > 0 for side -) pays.  With U3's Gamma^E (full b_j^2 on every piece) the non-violated side would be
charged b^-_j^2/|a^b_j|, which is huge when |b^-_j| >> |e_j|; use Gamma^{E,+-} := Gamma_w(b^+-, omega^+-) + q^b_0 sum_E ((z_j b^+-_j)_-+)^2/|a^b_j|.
(P4.2) The theta piece.  In thm:engineered the theta-decomposition is used for 0 < |tau| <= s_1 with BOTH signs of tau; at a bank
coordinate (now in F^b, no window mass) it flips as soon as |tau rho b^theta_j| > |a'_j|, and pays (tau^2 rho^2/2)(b^theta_j)^2/|a'_j|.  So
Gamma_theta acquires q_0 sum_E (b^theta_j)^2/|a^b_j| as well.  Both (P4.1) and (P4.2) are harmless exactly when ALL pieces are of the
size of the violation at the bank coordinates: |b^+-_j| <= C|v_j| with |v_j| the (fine-origin) mismatch there.  For the fine-origin
violations of Proposition RT*(d) this can always be arranged (v_j = -sum_m Delta_m psi_m(j) is a sum over fine/medium carriers, and the
split b^+_j = chi_j v_j with chi_j in [0,1] gives |b^+-_j| <= |v_j|); this hypothesis must be stated.
(P4.3) Cost.  "p*(f^b - f) <= C_f sum_E m_j" should read <= C_f m log(e/m), m := sum_E m_j (Z3 Lemma 3.1: zhat moves only on E at first
order — diagonal base — and the w-change carries the Delta log(e/Delta) term when carriers touch E).  Still o(T_lo^2).
(P4.4) Uniformity.  Imposing (T_1) on F only is legitimate (the flip part on E is bounded for ALL tau by the quadratic term), but the
other (T_0)/(T_1) conditions are evaluated at f^b; they depend continuously on the masses, so uniformity in small masses holds.
Numerics (vt_check.py re-run, identical): m_min/eps^2 = 0.83, 0.79, 0.75, 0.71 (grid ratio 10^{1/8}); the trend is consistent with the
precise prediction m_min = q_0 rho^2 eps^2/(1 - rho^2 kappa_w) = 0.67 eps^2 (maximize 2 q_0 (t rho eps - m) - (t^2/2)(1 - rho^2 kappa_w) over t;
the quadratic bound is tight at the optimum); U3's 0.81 omits q_0 = 0.796 and the slack factor — a constant, not the law.

## 2. Lemma VT (violation tolerance at a single stage).  Verdict: CORRECT (PROVED) as a conditional single-stage statement;
## confirmed numerically (vt_ref_check.py).
I re-derived (*) case by case from Step 3 (Base) of the proof of thm:engineered:
 on supp a', summand = 2(-x - A)_+ <= 2 x_- with A = (1 - tau rho c)|a'_j| > 0, x = z'_j tau rho beta_j; F: no flip by (T_1); window contact
 with mass, theta: |x| <= m_j/4 <= A (lem:approxfacts(a)); +: 2 rho|tau|(z b^+)_-; -: 2 rho|tau|(z b^-)_+; window contact without mass:
 b^theta_j = 0 forces beta^theta_j = 0, the +- summands are 2 rho|tau| times the violation; free j <= N_w: (H3) or viol = 0 gives beta^theta_j = 0,
 +-: <= 2 rho|tau||b^+-_j|; contacts in (N_w, N'']: rho|tau|(z_j v_j)_- <= rho|tau| viol(j) since z v >= -(z b^+)_- - (z b^-)_+; free j > N_w:
 |v_j| <= viol(j) (also for j > N'' where z'_j = 0); contacts j > N'': (1/2) rho|tau||v_j| (the V_{>N''} term).  Free coordinates never carry
 masses.  Steps 0-2 use only the REPRESENTATIONS (Gamma_w convex without admissibility; v = sum R^*((omega^- - omega^+) - Delta d w) holds
 for any two representations), Step 3 (Blocks) only supp omega in Q, lem:approxfacts only ||b^theta||_1 and the masses; Step 5 gains
 delta tau^2/16; total (tau^2/2)(1 - 2 delta + 3 delta/4) <= (tau^2/2)(1 - delta).  Correct.  The VT statement correctly excludes Step 6.
Numerical confirmation (new script vt_ref_check.py: N = 1 model with a dead-zone contact j0 violated on side + by eps, the full engineered
approximant built from the violated data, true p* computed by SOCP, kappa_w = 0.048, delta = 0.48):
   eps = 2e-3: s_1 = 32 rho eps/delta = 0.12 -> max_tau [p*(f' + tau g') - 1 - tau^2(1-delta)/2] = -8.6e-9 (holds);  s_1 = 4 rho eps/delta
   -> -2.1e-8 (holds);  s_1 = eps/20 -> +7.8e-6, failing for tau in [5.6e-4, 1.0e-2] (the predicted linear-cost window (m_j0/(rho eps), ~4 rho eps/delta)).
   eps = 5e-4: same pattern (holds, holds, fails on [1.8e-4, 2.4e-3]).
So the threshold (VT) is real (the constant 32 is not sharp; 4 suffices here) and the failure mode below it is the linear flip cost.
Limitation (correctly stated by U3, Remark 4.2(c)): (VT) bounds s_1 from BELOW, "late" bounds it from ABOVE; for fixed violated data
(VT) fails at all late stages.  VT is useful only where eps is small compared with the late threshold of the row (= (S2c)).

## 3. Proposition RT*.  Verdicts: (a) CORRECT; (b) CORRECT (= Lemma A / Lemma S, with the Sigma(omega) clause of P2.2);
## (c) SKETCH (plausible); (d) CORRECT given (c), with a bookkeeping precision (P4.5); (e) SKETCH; (f) CORRECT arithmetic (P4.6).
(a) V2 Cor. C1.1(a): c^comb is a polyhedral function of finitely many variables (T(l), G finite), its minimum over x >= 0 is an attained
LP value, the sign sphere is compact; in case (II) c^comb_* = 0 is ATTAINED: an exact combinatorial resonance exists.  Correct.
(c) I checked the structure: on T(l) the data v^# differ from the combinatorial L by (i) class-R strict non-peaks of shifted blocks (they
must be put into Omega with net coefficient 0 — Lemma R-pin controls the size), (ii) G strict non-peaks of shifted blocks outside the
resonance (same neutralization), (iii) medium/fine contributions.  Plausible; this item is a genuine part of the reduction and is
NOT covered by (S1), (S2): the sentence "Assuming them [(S1), (S2)], every F-finite (C*) row is in Rec" must read "assuming (S1), (S2)
and RT*(c)" (P4.7).
(P4.5) |Delta| is not O(1) at window scales: Delta = d(omega^-) - d(omega^+) with |omega| up to O(1/t) (box bound), so |Delta| <= C D(l)/t and
the fine-origin mass is eps <= C D(l) sum_{c > l} lambda_c / t <= C D(l) T_lo(l)^3/t <= C D(l) T_lo(l)^2 (without (W10)).  The bank cost
eps^2/beta stays o(T_lo^2); the (VT) arithmetic of (f) survives because of (W10) (below).
(P4.6) (f) re-checked with |Delta| <= C/t: free-coordinate mass <= C T_lo(l)^{10}/T_lo(l) = C T_lo(l)^9; s_1 := T_lo(l)^8 c_l satisfies
32 rho eps/delta <= s_1 iff c_l >= C' T_lo(l), true since log(1/c_l) ~ 10 log(1/T_lo(l-1)) << log(1/T_lo(l)) ~ n^w_l; and s_1 <= T_lo(l)^3 times
the least coarse weight.  Correct.  (W10) is an upper bound on weights chosen at stage l before Design(l) and the window of level l; all
window results use weights through upper bounds ((P2)) — compatible, same status as V4's design conditions (not checked line by line
against every constant of D_Omega / D^{V2}).

## 4. (S1) for a single shifted block with a free-ray q<0 carrier.  Verdict: CORRECT (PROVED).
After Hoffman projection onto the combinatorial cone (pattern-only, design constant), the coupling residual r = delta + sum q x is
removed by moving x_k of the free-ray carrier (q_k < 0) by r/|q_k| (r > 0) or decreasing it (r < 0, if x_k >= |r|/|q_k|; otherwise set x_k = 0
and the remaining residual forces delta = O(K t), i.e. the pinned case).  |q_k| = Phi_k |w(k)|/(m C) >= Phi_k M u(w)/(m C) at a clean
sub-window (rho_k robust, not nearly neutral), so the constant is design x u^{-1}.  Correct.  Note that this also gives rho^sh = 0 exactly
at f whenever (a) and a free-ray q<0 carrier hold.  General (S1): OPEN, as labelled.

## 5. (S2a)-(S2d).  Verdicts: (S2a) SKETCH, but the "scaling check (PROVED arithmetic)" is WRONG as written (P4.8); (S2b) SKETCH
## (plausible given a corrected (S2a)); (S2c) HEURISTIC (as labelled); (S2d) SKETCH, and its "OPEN sub-case" is avoidable (P4.9).
(P4.8) K_sharp is NOT O(1) uniformly in t — the theta/+- JUNCTION MISMATCH.  K_sharp bounds |lin'_m|/(|tau| s_1); for diamond = +-,
lin'_m = tau kappa^diamond_m + r_m <V^an - w', R x'>/sigma' with kappa^diamond_m = rho (d'_m - d_m)(omega^diamond - omega^theta).  By the proof of
(E4), (d'_m - d_m)(omega) = omega(R xhat')/|R xhat'| - omega(R zhat)/|R zhat|, so |(d' - d)(omega)| <= C ||lambda omega||_1 (K_e s_1 + t(N''));
for window data ||lambda(omega^- - omega^+)||_1 is up to O(1/t) (box bound; O(1) for fixed switching) and K_e = 8 rho ||U|| ||b^theta||_1/nu =
O(1/t) (size condition t||b||_1 <= A_0).  Hence |lin'_m| ~ |tau| s_1/t^2 — the mass-induced change of the block data (first order, of size
s_1 ||b^theta||_1 ~ s_1/t) acting on switching of size 1/t.  At the junction |tau| ~ s_1 this is tau^2/t^2, a factor t^{-2} above the
quadratic terms; the theta-piece cannot be extended (its masses would grow in proportion, the ratio is scale invariant), so the
mismatch must be removed by rebalancing with inefficiency eta_1 <~ delta t^2 and Lambda <~ t^{-2} (Lemma TV(a) needs |eps_m| Lambda <= gamma/2).
Such transfer peaks need a carrier of block m at weight Phi(k_*) in the range [~|tau| s_1/t^2, ~eta_1] approximating the f-dependent
transfer target T/ell to precision ~eta_1 (lem:transferdata: the peak condition forces Phi(k_*) <~ delta_0 ~ eta_1, and Lambda = ell/lambda_{k_*}).
For super-fast ladders (D_Omega: about one weight per window level, c_{l+1} <= T_lo(l)^{10}) only O(1) carriers have weights in that range and
their targets are fixed by the design: in general NO such transfer peak exists.  So U3's scaling check ("K_sharp = O(1) because Gamma_w <= 2
bounds the quadratic terms") overlooks the first-order part of K_sharp, and (S2a) as written is NOT established.
Suggested repair (SKETCH; Section 5 of U3_ref_notes.md): D-CONSISTENT engineered approximants.  Since d'_m(omega) = d_m(omega) for every omega
supported on a set S of strict non-peaks as soon as the normalized block values agree on S ((R_m xhat')(k)/|R_m xhat'| = (R_m zhat)(k)/|R_m zhat|,
k in S), re-tune at f' the normalized values of the finitely many coarse omega-carriers exactly back to their values at the row (V1
Lemma TU: pulls and private banks at far signature coordinates, diagonal base, explicit fixed point; the levers keep f' norm attaining).
Then kappa^diamond_m = 0 for ALL pieces at once, lin'_m reduces to the anchor/Bregman part r_m g_m = |tau| O(|Delta d| (Bx + S_m)) (fine
carriers only, <= |tau| s_1 T_lo^3/t^2 after the tuning), K_sharp = O(1) is restored, fixed transfer data suffice, and the remaining
conditions of Step 0 hold for |tau| <= c_flat t (K_W, K_A, K_h, K_H = O(1/t)), as U3 computed.  Requirements: s_1 <= c delta t^3-type bounds for the
residual terms (met by (f)'s s_1 = T_lo^8 c_l), and the tuning cost (second order plus far lever masses) below the scale-decoupling budget.
(S2b): one stage late for all pieces with masses 4 rho s_1 max_i |b^theta_{i,j}|; K_e ~ 1/T_lo for every piece; with the d-consistent
tuning (one tuning serves all pieces, since it fixes d' = d on all omega supported on the tuned set) the (A^eng)/(B'') averaging is
Theorem E's; plausible.  Without the tuning, (S2b) inherits the junction problem.
(P4.9) (S2d): the pair at a violated in-window free coordinate is determined only up to adding the same number to b^+_j and b^-_j (which
changes the represented functional by that number at j).  Choosing the symmetric split b^+_j = -b^-_j = v_j/2 gives b^theta_j = 0, i.e.
(H3), and b^+_j b^-_j <= 0, at an l_1 cost |b^theta_j| (fine-origin, since exact data at the row have b^+-_j = 0 there).  So the "OPEN sub-case
b^+(j) b^-(j) > 0" is not an obstruction.

## 6. Lemma R-pin.  Verdict: CORRECT (PROVED), consequences (i) correct, (ii) plausible as labelled.
lem:suplevel(f): varsigma omega_+(k) <= (1 - d_+ t) gap/t, varsigma omega_-(k) >= -(1 + d_- t) gap/t, |d t| <= 1/2 gives
varsigma(omega_+ - omega_-)(k) <= 3 gap/t; omega_+ - omega_- = Delta Theta + Delta d w.  Exact.

## 7. Section 4.4(5) (former gaps (C*-1), (C*-2), (C*-4), (C*-5) "not a gap any more").  Verdict: SKETCH-level claims, correctly
## flagged as resting on (S2) — and on RT*(c) (P4.7).
