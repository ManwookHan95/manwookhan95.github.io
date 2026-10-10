# V1-ref part 3 — verification log: Lemmas CO, ST, NS, RR; Proposition TR; Theorem E''; Master Theorem II; Cor AC; residual list

## Lemma CO — CORRECT. eta <= H_tune(|T|+3) b <= Design b (|D_{r,m}(f)| <= b Phi_max <= b; values move by own closing r^nat <= b,
target closings <= |T| b, second-order donor terms C Design^2 Lam^2 <= b). Cost: closing S^nat sets touches coarse carriers only through
their own signatures (coarse targets ⊂ T(l)); fine carriers contribute sum lambda <= b^2/2; donors <= 3 Lam each; Hilbert part
||e^# - e|| <= C Design Lam; TU part C_T eta log <= Design^4 b log << Lam. theta_w = C_f Design T_lo log(1/T_lo) -> 0.

## Lemma ST — CORRECT. Checked against Y1 Lemma T2 (statement and proof, Y1_notes 2.2; Y1-ref 5(a)): outward push s in [Lam/2, 4Lam]
in zeta-units (zeta(k) = lambda_k u_k(zhat)), E_m <= C_f T_lo^4 <= A s/(8(A+theta+1)) for l >= l_f. Corollary T3 for rho^#.
(K4): rho^# <= (1+b)(1 + C_f D Design b)(1 + c_f Lam)^{-1} <= 1 - c_f Lam/3 since D Design b <= D T_lo^4/l << T_lo^3.
Blocks outside I_D: |theta^# - theta| <= C_1 E_m (T2(a), fixed reference peak); their kept carriers are (K1)-(K3), all robustly below
threshold (rho <= 1-u or rho <= b), so the downward drift C_f T_lo^4 is harmless; dropped carriers there may change status — handled in
Prop. TR Step 5 by datum 0 with error 2 lambda gap/t + |tau| + lambda|Delta d|M (gap <= bM), re-derived from lem:suplevel(f) + peakshift.
(d): q^# = val^#/A^#_m at strict non-peaks (lem:threshold: w(k) = C zeta(k)/(Phi^2 |zeta|), zeta(k) = m Phi u_k(zhat)).

## Lemma NS — CORRECT (S^nat excludes T(l); allowedness (a) + rule (c) put coarser-signature target hits inside T(l)).
## Lemma RR — CORRECT (|D^# - D| <= 2 Design b <= u Phi_max/2; Phi_max >= 1/D(l)).
NOTE: "robust rates stay robust" is NOT claimed (and not true) for the R1-room of a class-R DONOR in case (b) of (C3) — closing
z_{s_m} may make that room tiny. Harmless: donors are pinned at f and carry datum 0 at f^#; no later step uses their room.

## Proposition TR — CORRECT (with precision p3 below)
Step 1: (Z2) re-derived from lem:phicalc(a) ((sgn z . x)_- <= phi_z(x) for |z| >= 1-b > 0); Hoffman G** (RHS-independent).
Step 2: eq:didentity: G-carriers contribute Phi w Delta theta/(mC) = -q tau; dropped carriers |q tau| <= |tau|/C. Conversion q -> q^#
(strict non-peak: val/A; (K4) peak of f: val/(rho A), rho in [1,1+b]) re-derived.
Step 3 (ray removal per block): every ray's d-vector at f^# has at most one nonzero entry (tiny -> 0 by Lemma TU(a), robust stays
robust; (VR_w)). For block m, Y4 Lemma 1.8 applied to cone{r : m(r) = m} with D_min >= u/(2 D A^#_m); rays with m(r) != m have zero
m-component, so the removals in different blocks do not interact: Q^#_{m'}(tau') = 0 for all m'. 0 <= tau' <= tau_0 keeps the box rows.
Zero cost at f^#: V' lives on S^nat_{l''} (z^# = eps off F^#), on T(l) \ F (rows of kappa(w); types of f^# = types of kappa(w)), and nowhere
else off F. V'(s_m) = 0 (donors not kept). V' is z^(2)-signed on K^(2).
Step 4: lem:split (note, lines 4789-4815) is pointwise; its proof gives |e_+-(j)| <= |e(j)| + phi_{z'_j}(B_+(j)) + phi_{-z'_j}(B_-(j)) for ANY
sign vector z' with V z'-signed on {|z'| = 1}; so only the z^(2)-budget is needed. Raised coordinates: phi_{z'} <= 2 phi_z (both signs);
flipped and donor coordinates: <= 2(|Delta B| + phi_z(B_+) + phi_{-z}(B_-)) with flipped v-mass <= r^nat <= b. Budget C_S <= C(1 + N K_P).
Step 5: second representation, d-neutrality d^#(omega^-) - d^#(omega^+) = sum (eps tau'/lambda) Phi^2 w^#/C^# = Q^#_m(tau') = 0;
b^+(zhat^#) = 0 by balancing with the ORIGINAL a (a(zhat^#) = ||a||_1 + nu^2 (nu^2 + ||X||^2)^{-1/2} in [1 - ||X||^2/(2nu), 1]);
b^-(xi^#) = b^+(xi^#) via lem:algebra (omega^+- vanish on the peak set of f^#). Two-piece admissibility at f^# (def:twopiece: no
condition on supp a^# = F^#; off F^#: K^(2) \ F^# ⊂ K^# and z^# = z^(2) there). (iv): t|b^+-(j)| <= t tau' v(j) <= 12 lambda v(j) =
mu/2 <= |a^#(j)| (q*(A^#) <= 2; box row tau' <= 12 lambda/t at every scale of the window). Shift trick: re-derived for (K4) peaks
of f (vs omega_+ >= -tau/lambda + Delta d M from peakshift), lambda|x| <= |tau - tau'| + lambda|Delta d|M. Kind [3] with the 1.5 gap^#/t
outward allowance is covered by Y2 Lemma U' (ii): r vs omega <= 1.5 c_flat gap <= (1 - rd) gap since c_flat <= 1/8, |rd| <= 1/2.
Estimates (ii): |kappa| <= C(K_U + N K_P + 1)t re-derived (raised coordinates: sum (1-|z_j|)|B_+(j)| <= t/(2q_0) by phicalc(a);
pulls: sum |Delta B| <= 6 l 2^G eta/t <= 6 2^G t^3). (i): Hilbert part at changed e: ||P^perp_{e^#}x|| - ||P^perp_e x|| <= 2||e^# - e|| ||x||,
||U^*B_+|| <= ||U|| eta/t; block part via ||D(w^# - w)|| + |C^# - C|. K_w <= C_f G**^2 l^2 D^6 u^{-4} <= C_f Design u^{-4}.

## Theorem E'' — CORRECT, precision (p3): the hypothesis "Ba_j contacts of f carrying masses of sign z" should read "Ba_j ⊂ supp a_j \ F
(any coordinates; necessarily z_j(i) = sgn a_j(i) there)". The proof of Y4 Lemma 2.3 / Y4-ref P2 uses only the sign of a_j(i) at f_j
(excess |a_j(i) + r b_i| - |a_j(i)| - z_j(i) r b_i = 0 for contact-like data w.r.t. z_j); V1's donor banks s_m (case (b)) and tuning banks j'
are contacts of f^(2), not necessarily of f (z^1 was closed there by (C1) or (C3)). Coordinatewise z_j -> z still holds (all modified
far coordinates escape to infinity, closed rooms -> 0). Nothing else changes.

## Master Theorem II — CORRECT. Window arithmetic re-done: K_w T_hi <= C_f Design u^{-4} 2^{-l^3}/(lQ) <= C_f 2^{-l^3}/l (Q >= Design u^{-4});
n c_flat/K_w >= l 2^{l^3} Q c_f u^5/(C_f Design) -> infinity; theta_w <= c_f u^2 (1-rho^2)/(24 rho^2) since T_lo <= 2^{-Q}, Design <= Q^{1/20};
Gamma: (1 + kappa_0)^2 <= 1 + eta_0/2 with kappa_0 = (sqrt(1+eta_0/2) - 1)/2. Quantifiers: design -> f -> (levels, clean w, companion:
f only) -> g, rho -> data at each dyadic t.
M-II.1, M-II.2: immediate. M-II.3: Z4 Lemma 5.0 (re-read): at maximal contact every block has infinitely many swallowed peaks of both
signs with margins >= q_0/4, all class G with room 0; fixed ones are coarse for l >= l_f and have rho - 1 >= m/(4 Phi theta) >= u:
(U2) and (L2), so I_up ∪ I_lo = {}.

## Corollary AC — CORRECT within Master Theorem II's framework (the bank moves every other value at second order, which is harmless
there because (C4) is computed afterwards at f^(2); it would NOT be harmless in Y2's tuning-free Proposition Q, so "(TD_m) not needed"
is a statement about the D_Omega assembly, as V1 says). The diagonal base is essential (first-order bank effect = mu s_s^2 v_c(s)/nu > 0).

## Residual list — CORRECT as a logical statement (contrapositive at clean windows: NOT (SH_w) <=> (C_w), NOT (VR_w) <=> (B_w)).
