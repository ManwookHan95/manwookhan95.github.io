# Y1 referee, part 1: Theorem 1 (design D_X), Theorem 2 (clean sub-windows), Lemma T, T2, T3

Sources checked: r6/Y1_notes.md (parts 0-5c), paper/martin_density_note.tex Sections 1, 7, 8 (def:SLD, thm:SLD, lem:threshold,
eq:margin, lem:suplevel, lem:box, lem:pinning, lem:signmixed, def:swallowed, lem:modswallow, lem:badpeaks, lem:exactswitch,
lem:windowtwopiece, lem:onesidedtransfer, thm:windowed, cor:D1), Round-5 referee reports Z3-Z6.

## 1.1 Theorem 1 (design D_X)
Recursion well defined: every quantity of level l (T(l), sigma(l), m^nat, D(l), G*(l), H_comb(l), G**(l), omega(l), Design(l),
M(l), u, Q, n, T_hi, T_lo, b of the sub-windows) uses only y_{l''}, c_{l''} (l'' <= l) and (D0) data. c_{l+1} is fixed last. CORRECT.
(a) admissibility: thm:SLD's proof uses only allowedness and c_{l+1} <= c_l/4. CORRECT.
(b) bands: u(w) = b(w^-) <= T_lo(w^-)^4 <= 1/4; Q(w) >= u(w)^{-omega-8} >= u^{-8}; n(w) >= Q(w); b(w) <= T_lo(w)^4 <= 2^{-4n(w)}
    <= 2^{-4u^{-8}} < u(w). Bands (b(w), u(w)) = consecutive open intervals of a decreasing sequence: pairwise disjoint. CORRECT.
    Fine weights: sum_{l'>l} lambda_{l'} <= c_{l+1}/3 <= b(l,M(l))^2/3 <= b(w)^2/3 for every sub-window of level l. CORRECT.
(c) N-independence: G** maximized over all U in [1,l]; D(l), H_comb, G* N-free. CORRECT.
(d) survival: every window proof of Section 8 uses (P1), (P2) [sum_{fine} lambda <= T_lo^3], (P3) [T_hi 2^{l^3} Lambda° <= 1/l,
    n >= l 2^{l^3} Lambda°] for ONE window. For a sub-window w: T_hi(w) <= 2^{-l^3}/(l Q(w)), Q >= Design >= Lambda°,
    n(w) >= l 2^{l^3} Q(w), fine sum <= T_lo(w)^8. D''' requirement l 2^{l^3} Lambda° Xi'(l) <= X^10 <= Design^2 (X := the bracket
    of Design); SLD_G requirement (l 2^{l^3} Lambda° G*)^6 <= Design. CORRECT.
    PRECISION (m1): the survival list includes Z4 Corollary 5.4 "with the referee corrections". Lemma 5.3 (signature lift) needs the
    clause c_l <= (delta_l ||h_l||_1)^2 (l >= 2), which D_X does not impose; the Z4 referee's corrected form of Cor 5.4 (M_f in place of
    M^canc) does not need it, so the survival claim is correct in that form. If the M^canc form is wanted, put
    c_{l+1} := min{c_l/4, b(l,M(l))^2, (delta_{l+1}||h_{l+1}||_1)^2} (legitimate: h_{l+1}, delta_{l+1} are fixed in (D0); smaller c only
    helps). No Y1 theorem uses Lemma 5.3 (and Corollary M1 supersedes Cor 5.4 at maximal contact).

## 1.2 Theorem 2 (clean sub-windows)
Rate objects of level l: (R1) l rooms r^nat/||v 1_{S^nat}|| (one per l'' <= l), (R2) <= |T(l)| target rooms, (R3) l threshold
distances, (R4) l relative positions: <= 3l + |T(l)| = omega(l) numbers; M(l) = omega(l) + 1 pairwise disjoint open bands; one
band contains none of them. CORRECT (pigeonhole at EVERY level l >= max F).
Remark: only these four families enter the pinning constants (checked in part 3); the other f-dependent quantities (q_0, nu,
sigma_m, C_m, M_m, the fixed donors, the fixed repair directions, C_F, transfer data) are fixed f-constants.

## 1.3 Lemma T, T2, T3 (threshold equation)
Notation check: Y1 uses zeta_m := R_m^** zhat (zhat-units), A_m := |zeta_m|_m = sigma_m/q_0, theta_m := A_m M_m/C_m; then
nu_k := |zeta(k)|/Phi_k^2 = m|u_k(zhat)|/Phi_k, rho := nu/theta; the note's vartheta_m = q_0 theta_m/m and margin
mu = q_0 Phi theta (rho - 1)/m; eq:margin gives sigma|alpha(k)| = lambda mu (used in Lemma 3.3). Consistent.
Lemma T (a)-(c): re-derived. On P, |zeta||alpha(k)| = |zeta(k)| - theta Phi_k^2; degenerate peaks have nu = theta exactly; nu = theta
forces k in P (else |w(k)| = C theta/|zeta| = M). |w(k)| = (C/|zeta|) min(theta, nu_k) gives Bh(theta) = |zeta|^2. Psi strictly
decreasing on {Ah > 0}, negative after. CORRECT.
Lemma T2(a): with k_0 a fixed non-degenerate peak, Ah(theta+h; zeta) <= A - h phi_0 for h <= h_0, Bh(theta+h; zeta') >= A^2 - 2 theta E;
y := h phi_0 - E in [0, A]; Psi(theta+h; zeta') <= -yA + 2(theta+1)E < 0 iff h > C_1 E; lower side symmetric with
Ah(theta-h) >= A + h phi_0. CORRECT.
Lemma T2(b): the c-term of Bh at level theta+h is (theta+h)^2 Phi_c^2 = theta^2 Phi_c^2 + (2 theta h + h^2) Phi_c^2, so
Bh(theta+h; zeta') <= A^2 + (2theta+1) h phi + 2(theta+1)E; Ah(theta+h; zeta') >= A + s - h phi - E; with h phi <= s/8, E <= s/8:
Psi >= (3/2)As - As/4 - As/4 > 0. Upper bound: Ah(theta+h; zeta') <= A + s - h phi_0 + E (k_0 = c or not), Bh(theta; zeta') >=
A^2 - 2 theta E (the c-term of Bh(theta) is theta^2 Phi_c^2 before and after). CORRECT.
Corollary T3 and the derivative d log theta/ds = A/(theta phi_P (A + theta)) = C^2/(M A phi_P): re-derived. CORRECT.
Common rescaling of d-coefficients: q = eps u(zhat)/A at strict non-peaks, so untouched carriers' q scale by A/A'. CORRECT.
Numerics: see part 2 (independent script Y1_ref_work/lemmaT_indep.py).
