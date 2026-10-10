# Q2 referee (a), part 3 -- Sections 3 and 4 of Q2

Sources: Q2_notes.md 3-4, Q2_part3.md, Q2_part4.md, Q2_work/*.py (re-run: identical output); r9/X2_notes.md 2.1-2.3 (levers, Lemma DC,
Lemma LV); r7/V1_notes.md 4.1 (Proposition TR); the note (lem:smallness, lem:budget, lem:finitebase, lem:windowtwopiece, lem:threshold).
Referee scripts: Q2_refa_work/smass_jacobian.py, border_inverse.py, drift_check.py (+ outputs quoted below).

## 1. Lemma 3.1 (TR(i) without lem:finitebase).  VERDICT: correct (PROVED).
lem:smallness is proved by compactness (A_n -> a weak*, limsup ||A_n||_1 <= ||a||_1, hence ||A_n - a||_1 -> 0) and never uses finiteness of F;
its t_eta depends only on f (uniform over g in C(f), since C(f) is p*-bounded).  The note's lem:windowtwopiece(d) / V1 TR(i) used lem:finitebase
only to bound ||B_+ 1_F||_1 (through ||P^perp U* B_+|| and B_+(zhat)); lem:smallness gives t||B_+ 1_F||_1 <= t||B_+||_1 <= eta directly.  With
||V'||_1 <= sum tau' <= 12 sum_l lambda_l/t <= 4/t (sum lambda_l <= 1/3 by thm:SLD), |kappa| <= C(K_U + N K_P + 1) t and a(zhat^#) >= 1/2:
t||b^+||_1 <= 1 + 4 + 2C(...)t^2 <= 6 and t||b^-||_1 <= 10.  (Q2_part3 states "A_0 := 6" and then takes 10; the notes say 10: use 10.)
Precision (p3.1): the decompositions B_+- must be taken at the fixed row f (as in V1 TR and V3's raise transfer, where the data of f are moved
to the raised row).  If decompositions at moving base rows f_j -> f were used, the same compactness proof gives a uniform t_eta on a ball around f
(a_j -> a in l_1 by prop:continuity), so nothing changes.

## 2. Proposition 3.2 (cushion domination at a deep-raised companion).  VERDICT: SKETCH is the right label.
Checked coordinatewise: deep raised coordinates (usage <= |g_j| + C Bx_*(j)/t with C = 3 (box, lem:box) + 12 (switching, TR Step 3) = 15 (Q2 writes
12; immaterial): the raise to modulus 8 Bx_* + |g_j| gives C_+ = 2 for t <= 1); shallow robust coordinates (C_+ <= C/u(w)); shallow thin coordinates
(Lemma P pinning + projection + clamping of the anti-sign part beyond the cushion; per coordinate cost <= |a_s|/t + t^2/(2 q_0 t) by lem:budget(b),
finitely many coordinates below the raise depth J).  The unverified step is the one Q2 names (compatibility of the zero-switching faces with Q1's
class/cube pigeonhole).  The window-dependent C_+ is accepted by E^{eng,RT,inf} only after precision (p2.5) (part 2), which holds for the design.

## 3. Lemma 3.4 (exact drift identity).  VERDICT: correct (PROVED).
Re-derivation: with the diagonal base, U*u = kappa nu° e° + sum_{s notin F°} mu_s u(s) k_s; e^1 is supported on {k_s : s in supp a^1}; the cross
term vanishes because supp a^1 \ F° misses supp u; u(z^1) = u(z°); <e°, e^1> - 1 = -||e^1 - e°||^2/2.  Note that supp u is INFINITE whenever u != 0
(u in Y, Y cap c_00 = {0}), so "z^1 = z° on supp u" and "new support off supp u" are strong hypotheses; the allowed moves (raises, lowerings,
truncations to same-sign contacts on F°; masses and z-moves off supp u) are exactly as listed.  Consequences (a)-(c) follow.  Numerics
(drift_check.py, independent): identity error <= 2.5e-15 over 400 random admissible moves (n = 60, |F| = 20, including truncations); max gain
-3.3e-5 <= 0 for kappa > 0; a mass at s in supp u \ F acts at first order (Hilbert part m mu_s^2 u(s)/nu, plus the z-change).  Q2's own check
reproduces (1.7e-15).

## 4. Section 4.0 (exact Jacobian with S-mass common mode).  VERDICT: correct.
Derivation: an S-mass step at p_l changes U*A by sgn(A_1(p)) beta_p P mu_p k_p, so de = (I - e e^T)(...)/nu_1 and
eps_k du_k = P_l [delta_{kl} - g_k h_l] with g_k = eps_k <U* u_k, e_1>, h_l = |A_1(p_l)|/(nu_1 |u_l(p_l)|) (privacy: p_l notin supp u_k, k != l);
dA_m = <w_m, R_m dxhat> = q_m^T dP - G_m h^T dP with G_m summed over ALL carriers of block m.  Hence N = D - gt h^T - sum_m p_m q_m^T, gt = g - sum G_m p_m.
INDEPENDENT NUMERICAL CONFIRMATION (smass_jacobian.py): one-block Martin-type model with exact forced data (threshold equation), three strict
non-peaks with THICK S-mass levers (|A_1(p)| in [0.05, 0.3], h up to 4.9), finite-difference Jacobian of X2's map F versus the formula:
max relative error 9.9e-10 over 194 random instances; the block-norm lever column (z-move at a private coordinate of a peak) equals -pi p with
pi = eps lambda_{k*} w(k*) to 2.8e-9.  Capacitance structure (det N = det D det C, C arrow-shaped with diagonal 1 - q_m^T p_m >= 1/2): re-derived;
numerically exact to 4e-13 (border_inverse.py).  So N has at most one degenerate direction: correct.

## 5. Proposition 4.1 (block-norm bordering).  VERDICT: correct (PROVED).
Every step re-derived: q_m^T D^{-1} p_{m'} = delta_{mm'} q_m^T p_m (q_m^T X = 0, disjoint supports); the ansatz P = D^{-1}(b + g alpha + sum p_m gamma_m)
solves L(P, P_0) = b iff (i) h^T P = alpha, (ii) q_m^T P = gamma_m (m != m*), (iii) pi P_0 = gamma_{m*} - q_{m*}^T P; (ii) is solved explicitly
(denominators >= 1/2); (i) becomes c_alpha alpha - beta_* gamma_{m*} = rhs, solvable with |alpha|, |gamma_{m*}| <= |rhs|/beta_0 whenever
max(|c_alpha|, |beta_*|) >= beta_0; the chain of elementary inequalities giving K is correct (each checked).  The general bordering bound of Remark (b)
re-derived (||y^T N|| >= sigma ||y_perp|| because y_0^T N is orthogonal to y_perp^T N in the SVD; then the case split on ||y_perp||).
Numerics (border_inverse.py, independent implementation, 3000 trials with 3 blocks and absorber rows, one third with exact beta_* = 0, one third with
exact c_alpha = 0): residual <= 1.2e-13, (|P| + |P_0|)/(K |b|) <= 3.7e-5 (K is crude but valid).  In the doubly degenerate case c_alpha = beta_* = 0
the bordered map has rank n - 1 with left null vector y = D^{-T}(h + sum_{m != m*} theta_m q_m), theta_m := h^T D^{-1} p_m/(1 - q_m^T p_m) (|y^T L| = 5e-16):
NOT D^{-T} h unless h^T D^{-1} p_m = 0 for every m != m* (relevant for item 8 below).

## 6. Corollary 4.2 (Lemma DC^inf).  VERDICT: correct as a conditional statement (PROVED), with precisions (p3.2)-(p3.4).
 (p3.2) Poincare-Miranda constants: with G(y) := F(R_b y) on the cube |y|_inf <= r one needs |F(0)|_inf <= r/2, C_2 K^2 r <= 1/4 and c_tiny K <= 1/4, and
        gets |(P*, P_0*)| <= K r; Q2's conditions ("K|F(0)| <= r/2, K C_2 r <= 1/4") are those for the cube |y| <= r/K (then |(P*, P_0*)| <= r).  Either
        version is fine; the statement mixes them.
 (p3.3) Range and remainder of THICK S-mass levers: a step P moves A(p) by beta_p P = nu_1 P/(mu_p^2 |u_l(p)|) and e by ~ P/(mu_p |u_l(p)|).  The sign of
        A_1(p) is kept and the moved modulus stays >= |A_1(p)|/2 (needed by the no-flip argument of Theorem UE^inf at p) iff K r nu_1 <= mu_p^2 |u_l(p)| |A_1(p)|/2;
        the quadratic remainder constant is C_2 ~ (mu_p |u_l(p)|)^{-2}.  With (D-lev) and |A_1(p)| >= u(w) both are design quantities (r_0 >= u(w)/(2 nu Design),
        C_2 <= Design^2); they must be entered in r_0 and in (LATE) (same as (p2.2)).
 (p3.4) The hypothesis "the block-norm lever coordinate carries data V_fine(j) only" is NOT automatic (see item 7): it holds when the pieces are
        d-neutral in block m* (Delta_{m*} = 0); otherwise the data at a peak's private coordinate are the shift term -Delta_{m*} lambda_{k*} w(k*) u_{k*}(j).
        Repair (referee, PROVED as a modification): if those data are contact-like at j (z(j) = sgn of the data, which validity of the window family
        forces, see item 7), use a BANK WITH OFFSET at j: base mass m_0 := 2 K r beta_j with the sign of z(j), lever mass m_0 + beta_j P_0, |P_0| <= K r
        (beta_j := nu_1/(mu_j^2 |u_{k*}(j)|)).  Contact-like data at a same-sign support coordinate have zero anti-sign part on both sides, so (U3^inf) holds
        there with any C_+, and the theta piece is protected once m_0 >= 8 rho s_1 max_i |b^theta_i(j)| (W_F rule).  The offset creates a first-order common
        mode with coefficient h_0 = m_0/(nu_1 |u_{k*}(j)|) <= 2 K r Design^2 (D-lev), i.e. the bordering column becomes -pi p_{m*} - h_0 gt; by the general
        bordering bound (Remark (b)) or a Neumann perturbation the right inverse survives with norm <= 2K once h_0 ||gt||_inf K <= 1/2, a (LATE)-type smallness
        condition on s_1.  The transfer cost of m_0 is O(m_0) = O(K r Design) = O(K K_w Design s_1), inside Pi.

## 7. Lemma 4.3.  VERDICT: (a)-(c) correct (PROVED); the "Consequence" overstates in two places.
 (a) P_F U* u = U*(u 1_F), P_F e = e (diagonal base), so the hypothesis reads U*(u 1_F) = (<U* u, e>/nu) U* a and u 1_F = kappa a by injectivity.
     The hypothesis is exactly "every same-sign support move changes the raw combination only at second order" (d <U*u, e> = <(I - e e^T) U* u, U* da>/nu).
 (b), (c) correct (with kappa != 0; privacy (SEP)(ii)).
 Overstatement 1: "if kappa = 0 the carriers of Lambda do not meet F at all".  kappa = 0 gives u|_F = 0 for the COMBINATION; individual carriers can meet
     F at shallow coordinates where several carriers overlap.  Correct version: no carrier of Lambda meets F inside its private set beyond s_max(L) (only one
     coarse carrier lives there), which is what the lever argument uses.
 Overstatement 2: "every block has peak ZERO-DATA levers".  (c) gives OFF-SUPPORT, not zero data: with a shift Delta_{m*} != 0 in the window pieces, the data
     at j in S_{k*} beyond s_max are -Delta_{m*} lambda_{k*} w(k*) u_{k*}(j) (+ fine), since v = sum_m R_m*(Domega_m - Delta_m w_m) gives every peak the coefficient
     -lambda_k w(k) Delta_m.  For a VALID window family these coordinates must then be contacts with z = sgn(data) (at a free coordinate the violation mass
     |Delta| lambda_{k*} ||u_{k*} 1_{S_{k*}, > s_max}||_1 is not small), and the bank-with-offset lever of (p3.4) applies.  So the conclusion "every block has a
     two-sided block-norm lever" survives, with the repaired lever.  Also needed (implicit in Q2): the peak k* must have ROBUST margin (V1 Lemma D supplies one
     per block at clean sub-windows) so that moves of size K r keep it a peak.

## 8. Section 4.4 (what remains).  VERDICTS: (i) correct; (ii) correct with precision (p3.5); (iii), (iv) OPEN (honest).
 (ii) Re-derivation (X = 0, i.e. X2-ref's (R-abs) route): y^T F = h^T F = u(xhat) - sum_m A_m (h^T p_m) with u := sum_l h_l eps_l u_l; if h^T p_m = 0 for all m,
      then u(zhat_0) = 0 (F(0) = 0 at f_0) and the degenerate component is the RAW value u(xhat), so Lemma 3.4 applies: same-sign support moves (including the
      truncation at N_w, the W_F raises and the S-mass levers) change it by -(kappa nu/2)||Delta e||^2; first-order changes come only from moves on supp u \ F
      (theta-masses on W cap supp u; the cut-off z := 0 beyond N'', of size <= sum_{j > N''} |u(j)|); Z/TU/block-norm levers sit in private sets of OTHER carriers,
      off supp u.  Correct.
 (p3.5) The identification "left null vector = D^{-T} h" requires h^T D^{-1} p_m = 0 for EVERY block m (block-norm levers in every block, all degenerate);
      with block-norm levers in a single block m* the left null vector is D^{-T}(h + sum_{m != m*} theta_m q_m) (item 5), whose extra terms q_m^T F respond to
      support moves at first order.  Lemma 4.3(c) + item 7 make block-norm levers available in every block, so the all-block version is the natural one;
      the statement should say so.
 Also: the sentence "a second-order residue is tolerated by Theorem UE^inf (|kappa^+-| <= c delta s_1)" is not part of UE^inf as stated (which assumes exact
      d-consistency, kappa = 0).  A residual kappa^+- of size <= c delta s_1 is absorbed by the rebalancing of thm:engineered at cost |tau kappa| iota with the fixed
      inefficiency iota ~ eta_1 (X2 1.3), i.e. <= c delta tau^2 iota above s_1, and kappa^theta = 0 always: SKETCH (straightforward, not written).
 (iii) Indeed OPEN; my analysis sharpens it: in the exact case EXACT d-consistency is impossible whenever the first-order term tau_W != 0 (all levers act on the
      degenerate component only at second order), so a tolerance/data-side argument is unavoidable.  Referee suggestion (R3-a), SKETCH: solve F(P, P_0) in R yhat
      instead of F = 0, with yhat orthogonal, block by block, to all switching vectors Domega_i|_{Omega_m} of the window (then the residual does not enter
      kappa^+-, which depends on nv' - nv only through sum_k Domega(k)(nv'_k - nv_k)), and y^T yhat != 0 (then [L | -yhat] is onto, bordering again).  The residual
      lambda yhat, |lambda| <= C|y^T F(0)|/|y^T yhat| = O(tau_W) = O(C_W s_1), moves C_m and the gaps by O(lambda), harmless under (LATE) (gap_min enters s_late),
      and changes H'_m(omega) by O(lambda c_flat^2) on the radius.  This fails only if y|_{Omega_m} lies in the span of the switching vectors in every block, a further
      degeneracy (for U1's one-ray-per-class data: y|_{Omega_m} parallel to the class ray in every switching block).
 (iv) OPEN (KN-1 raw holds): Lemma 3.4(c) shows that raw targets above the value at the proportional row are unreachable by support moves; the block-norm column
      does not act on raw values.  Correctly labelled.
 "(NDN2) is non-generic, codimension two": correct as a description of a zero set of two functions of the level-L data, but HEURISTIC as a statement about rows
 (a single row f has countably many levels; nothing prevents the conditions from holding at all levels for specially constructed f).  Q2's Assessment uses it only
 as a heuristic.
