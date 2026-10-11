# G3-ref part 1: Section 2 of G3 (universal constraints) -- line-by-line check

Setting re-derived: forced data (xi, q_0, a, w, z, zhat, nu, e), q*(a) = ||a||_1 + nu = 1, a(zhat) = 1, xi = q_0 zhat,
q_0 + sum sigma_m = p**(xi) = 1, zeta_m = R_m** xi, zeta_m(k) = lambda_k q_0 u_k(zhat), block threshold structure
zeta/sigma = alpha + D^2 w/C (alpha on peaks, ||alpha||_1 = 1 forced by <w, zeta/sigma> = M + C = 1 = N(w)).

## Verdicts (all re-derived by hand)
- Lemma 1.1: correct.  LHS = q_0 q*(A) + sum sigma_m N_m(W_m) - (f+h)(xi) <= pi - 1.
- Lemma 1.2: correct (|x| - zx = (1-|z|)|x| if zx >= 0, >= 2|zx| if zx < 0).
- Cor 1.3: correct.  g(xi) = 0 from 1 +- t g(xi) <= s(t); attainment by weak*-compactness of {||W||_{V*} <= c},
  weak*-continuity of L^*, weak*-lsc of q*; each side separately has E_b <= (s(t)-1)/q_0.
- Lemma 1.4 (a), (b), (c) and (1.1): correct, including (a) at free coordinates.
- Theorem CL (CL0)-(CL2) and the diagonal-base display: correct.  (CL0): x_0 + sum x_m = 0 with x_i <= c_i (s-1),
  sum c_i = 1 gives every x_i >= -(s-1).  Diagonal base: |h_s| <= mu_s <= 1/16 for the design base, so the
  absorption hypothesis max |h| <= 1/2 holds automatically.
- Cor CL.1: correct.  But see PRECISION P-CL1 below.
- Lemma 1.5, Cor 1.6: correct (orientation bookkeeping for eps = -1 checked).
- Lemma 1.7: correct.  Step 1 bound sigma |L(Theta_+-)| <= (s-1)/t; Step 2 uses Phi(k)^2 w(k)/C = zeta(k)/sigma off P.
  Remark (1): the common-peak bound reaches only peaks in supp alpha, with constant t/(2 sigma |alpha(k)|);
  weak peaks (small alpha(k)) and degenerate peaks (alpha(k) = 0) are NOT controlled by it, and they enter S_1 through
  the peak part M Phi_k^2 Delta Theta(k)/C.  (P1) is therefore a genuine hypothesis (as stated), not automatic.
- Cor CL.2: correct.
- Cor 1.8: correct as stated, with the reading that "thin cushions (alpha <= t^2)" restricts the scales to
  t >= alpha^{1/2} unless the near and far coordinates are contacts.

## Numerics N1 (r14/G3_ref_work/refmodel.py, check_universal.py; independent implementation, 2 blocks)
40 random instances x 4 random feasible decompositions (random linear objective on the switching amplitudes),
t in {0.3, 0.1, 0.03}.  Worst normalized slack (LHS - RHS)/(1 + |RHS|):
 L1.4(a) 2e-17, L1.4(b) 0, L1.4(c) 1e-17, Cor1.3 -5e-5, CL0 -1e-2, CL1 -5e-2, CL2 -9e-2, L1.7 step 1 -5e-3,
 L1.7(i) -4e-2, Thm 2.10 (random G, random J_c of ANY coordinates) -7e-2, L1.7(ii) 0.  All hold.
 (alpha off peaks 2.7e-3 in one block: a near-peak coordinate |w| = M - 1.5e-6 misclassified by the 1e-6 peak tolerance;
 not a violation.)

## PRECISION P-CL1 (Cor CL.1 / Reading of Theorem CL; interpretive)
alpha(N cap F) in (CL2) is the TOTAL non-thick support mass of the row.  Taking T = F (all support) gives the
cleanest form ||V 1_{F^c}||_1 <= - sum_{s in F} zhat_s V_s + 3t/q_0 (h = 0 off F): switching on contacts and free
coordinates is paid by anti-signed switching on support coordinates, and a support coordinate s can absorb at most
2|a_s|/t + O(t) (Lemma 1.4(b)).  Thickness is therefore SCALE-RELATIVE: at scale t a coordinate with |a_s| >~ t |u(s)|
acts as a two-sided coordinate.  At window scales of an (R1) stage (s_1 <= theta_0 T/(8 rho A_0) << theta_0 <= b, (L-K2-1)),
every b-thin support coordinate is "thick" at the bottom of the window.  The statement of CL.1 ("or thin support at
scales t <~ alpha/P_k") is correct; the readings that drop this alternative are not (see part 2, G-THIN).
