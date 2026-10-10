# Referee report on V1 (Round 7): the unified design D_Omega, the assembled companion, the aligned corner, Master Theorem II

Refereed: r7/V1_notes.md (= V1_head + V1_part1..5, byte-identical; reading digest V1_part0) and r7/V1_work/*.py (re-run), against
paper/martin_density_note.tex (Sections 1, 7, 8: lem:threshold, eq:margin, prop:forced, lem:algebra, lem:base, def:twopiece, cor:D1,
def:SLD, thm:SLD, lem:twosided, lem:smallness, lem:budget, lem:suplevel, lem:box, lem:finitebase, def:windowcert, prop:windowcert,
eq:DeltaB, lem:phicalc, lem:switchbudget, lem:split, lem:peakshift with eq:peakshift and eq:didentity), the Round-6 referee reports and
notes (Y1 Lemmas T2, T3, 3.1-3.6, Proposition 5.2, Theorem E'; Y2 Lemma U', Theorem E', Lemma 5.1/Proposition 5.2; Y4 Lemmas 1.8, 2.2,
2.3; Y4-ref A.3, B.4, C.1-C.7) and Round 5 (Z3 Lemmas 3.1, 3.2; Z4 Lemma 5.0).
My part files: r7/V1_ref_part1..4.md; assembled proofs of all precisions: r7/V1_ref_notes.md; scripts: r7/V1_ref_work/.

## 0. Bottom line
V1 is CORRECT in all its PROVED claims. It does what the open item (A) of ADDENDUM 6 asked for: ONE companion per clean sub-window
of ONE N-free admissible design carries every exactification at once, and it closes item (D) (the aligned corner) for D_Omega.
I re-derived every step (design arithmetic, alpha-mass counting, shift-cost pinning, the explicit bank/pull fixed point, cost, status
table, transplant, Theorem E with banked and pulled supports, window arithmetic, quantifier order) and ran two independent finite-model
checks (exact tuning; one-block end-to-end donor bank + tuning). I found five precisions (p1)-(p5), none changing a statement or a
construction, and one inaccurate gloss in the OPEN section (the reason given for (B)). The key new mechanism — a robust-margin donor
peak exists in EVERY block at every clean sub-window, and with a diagonal base a bank at its first far signature coordinate pushes it
outward at first order while every other coarse value moves only at second order — is sound, and the threshold buffer it creates
(Lam = T_lo^3 against drifts O(T_lo^4/l)) is what makes the unconstrained least-norm tuning legitimate.
For D_Omega and F finite the open core is now: (B) rays with robust d-components in two blocks, (C) coherent shift resonance,
(E) infinite F; for N = 1 only (C) and (E). Lemma Z and density remain OPEN for every admissible T. No counterexample is claimed;
nothing I checked points to one.

## 1. Verdicts
| Claim | V1 label | Verdict | Main point |
|---|---|---|---|
| Theorem 1' (design D_Omega: admissible, N-free, disjoint bands, survival) | PROVED | correct (p1, p0) | S_l = {2^l(2i+1)} disjoint, gaps 2^{l+1}; (T-d) with rule (c); b(w) <= 2^{-64/u} < u = b(w^-); survival is by inspection (only larger Design/Q); (p1): l_f must also give s_max(l_f) >= max F (s_max -> infinity, proved) |
| Lemma D (robust-margin coarse peak in every block) | PROVED | correct | ||alpha||_1 = 1; tiny-margin coarse peaks carry <= (M/4C) b, fine peaks <= q_0 b^2/sigma; clean w excludes rho in (1+b,1+u); such peaks are dropped or class R, pinned |
| Lemma 3.4' / Lemma S (shift pinning by shift cost) | PROVED | correct | halves of Y1 Lemma 3.4 independent; I_up ∩ I_lo = {} from Lemma D; eq:peakshift (-Delta theta = vs lambda(Delta d M + e_k), lambda e_k <= t/mu) and switch budget re-derived; K_d' = C_f l D^3/u^2 |
| Patterns, cones, ray components, (VR_w) | PROVED | correct (p2) | one-signed blocks: component rate <= b theta_m/m, tiny for l >= l_f; faces of the orthant-contained cone |
| Lemma B (formula (3.1)) / Lemma DR (donor raise) | PROVED | correct | (3.1) exact; mu^D <= 2 D 8^sigma Lam/delta_min; bank's first-order effect mu s^2 v/nu > 0 only on the donor (diagonal base); others O(Design^2 Lam^2) |
| Lemma TU (exact two-sided tuning, explicit fixed point) | PROVED | correct (p4) | m(y) solves each equation iff N(m) = y; contraction constant carries 1/(s'^2 v'^2) (design); numerics: exact to 1.8e-15, masses > 0 |
| Lemma CO (cost o(T_lo^2), eta <= Design b) | PROVED | correct | Z3 Lemma 3.1 with Delta_m = sum lambda |u(delta)|; fine carriers <= b^2; TU part << Lam |
| Lemma ST (status table, (BS) via raise buffer) | PROVED | correct | Y1 T2(b) with s in [Lam/2, 4Lam], E_m <= C_f T_lo^4; (K4) -> rho^# <= 1 - c Lam/3; non-raised blocks hold only robust or nearly neutral kept carriers |
| Lemma NS (no slaving) / Lemma RR (robust rates) | PROVED | correct (p5) | S^nat excludes T(l); tiny components exactly 0; robust move <= 2 Design b; donor rooms not claimed and not needed |
| Proposition TR (transplant, K_w <= C_f Design u^{-4}) | PROVED | correct | per-block ray removal non-interacting under (VR_w); lem:split is pointwise (z^(2) allowed); balancing with a/a(zhat^#); data at pulls t|b| <= mu/2 <= |a^#|; kind [3] with 1.5 gap/t allowance covered by Y2 Lemma U'(ii) |
| Theorem E'' (banked + pulled supports) | PROVED | correct (p3) | banks need not be contacts of f: only the sign of a_j at f_j enters the excess |
| MASTER THEOREM II, M-II.1, M-II.2, M-II.3 | PROVED | correct | window arithmetic re-done; quantifiers: design -> f -> levels/clean w/companion -> g, rho -> data at each t; M-II.3 via Z4 Lemma 5.0 ((U2),(L2) at every clean w) |
| Corollary AC (aligned corner empty for D_Omega) | PROVED | correct | within the D_Omega assembly (the bank moves other values at second order, which (C4) absorbs; it would not be free in Y2's tuning-free Proposition Q); diagonal base essential |
| Lemma IP (inward push raises theta) | PROVED | correct | Psi'(theta) >= theta c sum_N Phi^2/4 > 0 re-derived; numerics re-run (13 flagged cases are below double precision) |
| Residual list (B_w), (C_w); exhaustiveness; union with Y1 5.4 | PROVED (logical) | correct | contrapositive at clean windows; Y1 uses (SP_w) only via K_d, Lemma S supplies K_d' |
| OPEN section 5.4: "(B) tiny minors not exactifiable by value tuning without destroying robust components" | (gloss) | inaccurate | minors are polynomials in the values; Lojasiewicz gives an exact zero within C b^{2 gamma} (design constants); the obstruction is only quantitative and designable (ref notes 4; this is V2's route) |

## 2. Main findings
**F1 (the new mechanism is right).** Lemma D's alpha-mass count is the decisive observation: since ||alpha_m||_1 = 1 and every
tiny-margin coarse peak has |alpha| = lambda mu/sigma <= (q_0 theta/sigma) Phi^2 b, a peak with ROBUST margin exists in every block
of every clean sub-window of large level — the aligned corner never lacks a donor. With the diagonal base, a bank at the donor's first
far signature coordinate (closed to its own sign) has first-order effect mu s^2 v/nu on the donor only (<U^*u_k, k_s> = s_s u_k(s) = 0
for every other coarse k), so Lemma T2(b) raises the threshold by >= c_f Lam. The finite-model check confirms the regime condition is
genuinely needed (bank masses of order 0.1-0.5 fail; D_Omega has mu^D <= Design Lam).
**F2 (assembly order).** (C1)-(C3) first, (C4) computed at f^(2): this is what makes the tuning exact despite the second-order
Hilbert effects of the donor banks (V^(2) = R val^(2) already contains them). The unconstrained least-norm solve is legitimate only
because of the raise buffer (Y4-ref's sign-constrained solve is not needed). Checked end-to-end (assembly_check4.py: 300/300).
**F3 (precisions).** (p1) s_max(l_f) >= max F (proof that s_max -> infinity in ref notes 2); (p2) one-signed component rates <= b theta/m;
(p3) Theorem E'' with banks at non-contacts of f; (p4) Lemma TU's contraction constant involves 1/(s'^2 v'^2), c_T ~ Design^{-2/3} suffices;
(p5) donor rooms at f^# are not robust in case (b) and are not used. (p0) rate values of carriers absent for p_N set to 1.
**F4 (gloss on (B)).** V1's reason for (B) being open is wrong; the correct reason is that V1's tuning is linear. See ref notes 4.

## 3. Attacks attempted (none broke a PROVED claim)
weak* vs norm (companion convergence in p* via Z3 Lemma 3.1; Lemma U' j_0 from norm convergence of forced data); uniformity in t
(data at every dyadic scale of W(w) from ONE companion; box row tau' <= 12 lambda/t at every scale gives the pull condition), in the
window (all constants design x u^{-k} x f-constants, Q(w) = (4 Design/u)^{omega+20}), in the number of active carriers (|L_0| <= l,
H_tune and G** maxima over all subsets of [1,l]), along companions (Lemma U' with supports F ∪ Ba ∪ Pu; a_j|_F -> a); simultaneous
exactifications (distinct coordinates; second-order Hilbert cross-effects; (C4) last; tuning moves robust objects by <= 2 Design b);
Hoffman/Farkas constants (G** RHS-independent; ray removal per block non-interacting; R x = -V consistent since V = R val);
design N-independence (patterns arbitrary subsets of [1,l]; ladder fixed for all N); admissibility (D0') and rule (c) with (T-d);
non-attained infima (c(.; pi) used only through upper bounds at x = tau_+; fixed point exists by contraction); signs and one-sidedness
(eq:peakshift sign, bank sign vs, pull sign -eps, z^(2)-signed V', kind [3] inward sign after the shift trick); near-contacts vs contacts
((C2) closing, phi_z >= (sgn z x)_- for |z| >= 1-b); c_0 vs l_infty (companions have z in l_infty, not attaining; cor:D1 at f_j);
finite vs infinite (F^# finite; finitely many kept carriers; fine carriers by box bound; infinite peak sets: alpha-mass only); hidden
assumptions on T (only (T-a)-(T-d), (P1)-(P3), allowedness (a)-(c), bounded gaps; U diagonal is a free choice before T); quantifier order.
Suspected problems examined and refuted: (i) threshold DROP in blocks without donors (only robust or nearly neutral kept carriers there);
(ii) status changes of dropped carriers (datum 0, error 2 lambda gap/t + |tau| + lambda|Delta d|M from lem:suplevel(f) and peakshift);
(iii) banks not at contacts of f (p3); (iv) Lemma TU divergence (only outside c_T, as in tu_check.py).

## 4. Numerics (r7/V1_ref_work; sanity checks only)
tu_check3.py / tu_check4.py: Lemma TU, 1227 tests in regime, exactness 1.8e-15, bank masses > 0, |Phi'| <= 0.018, others O(eta^2).
assembly_check4.py: 300/300 one-block companions: tiny component -> 3.3e-16, theta raise >= 0.75 theta Lam, near-threshold carrier
rho^# - 1 <= -0.75 Lam. assembly_check2.py: failures only with non-small bank masses (outside Lemma DR's regime). V1 scripts re-run.

## 5. Single most valuable idea
Every block always has a donor: by the alpha-mass identity ||alpha_m||_1 = 1, tiny-margin coarse peaks and fine peaks carry only
O(b) of the mass, so at every clean sub-window some coarse peak has robust margin; with a diagonal base a bank at its own-sign far
signature contact pushes it outward at first order and nothing else at first order. The resulting threshold buffer Lam = T_lo^3, which
dominates every exactification drift O(T_lo^4/l), lets ONE companion close all tiny rooms and target rooms and neutralize EXACTLY all
tiny ray d-components by an unconstrained least-norm solve realized by pulls and private banks — reducing the finite-F open core for
D_Omega to genuinely multi-block rays and coherent shift resonance (only the latter for N = 1).

## 6. What remains open after V1 (+ this report), design D_Omega, diagonal base
(B) genuinely multi-block rays: an extreme ray of C(kappa(w)) with robust d-components in two blocks (vector-valued d-row; the
candidate route is determinantal exactification by Lojasiewicz + Hoffman through minors, V2 — not refereed here);
(C) coherent shift resonance: a source-deficient block with tiny shift cost c_{pi(w)} <= b(w) at every clean sub-window of all large
levels (c_pi is a property of f; no companion move changes the decomposition at f);
(E) infinite F: (O4-crit), (O4-nd), (O4-box).
For N = 1 and F finite only (C) remains (maximal contact is unconditionally in Rec for N = 1).
Lemma Z and density of NA((c_0,p_N), l_2^2) and of NA((c_0,p), l_2^2) remain OPEN for every admissible T, including D_Omega.
