# V2 part 2 — Item (B): multi-block rays.  The d-row Hoffman constant is a design constant at every clean sub-window

## 2.0 What is used
- Design: D^PW of Y4 (Def. 1.4 with Y4-ref A.3 and addendum (G): bounded gaps G_l of the S_l), or V1's unified design;
  only: (D0)-(D2) of def:SLD, allowedness (a),(b), (P1)-(P3), the sub-window recursion (u(w) = b(w^-), disjoint bands
  (b(w), u(w)), Q(w) >= (4 Design(l)/u(w))^{omega(l)+3}), the pigeonhole Theorem 1.6 of Y4 (clean sub-windows), all N-free.
- Base: U diagonal (U^* e_i^* = s_i k_i, (k_i) orthonormal, s_i > 0), a free choice (Y4-ref C.8(iv)).
- Companion tools: far pulls and private banks with exact two-sided per-carrier tuning (Y4-ref C.2-C.6, Prop. P4), Lemma U /
  Theorem E with banked and pulled supports (Y4-ref C.3 Lemma P2, C.4 Lemma P3), Z3 Lemma 3.1 (companion cost), Z3 Prop. T
  (transplant; its hypothesis (HF) is the object of this part), Y1 Lemma T2 / Cor. T3 (quantitative raise), Lemma H, Lemma L,
  Lemma QB (part 1).
- The exact cone at a companion f^#.  As in Prop. T (HF), Y1 Prop. 5.2 and V1's assembly, the transplant projects the
  actual switching amplitudes tau (decompositions of g at f) onto the polyhedron Z^# of the system Sigma^# in the variables
  tau in R^G (G = coarse carriers, level <= l, swallowed at f^#):
    (Z1) tau_l >= 0;  (Z2) z^#_j L_j(tau) >= 0 (j in T(l) cap K^#);  (Z3) L_j(tau) = 0 (j in T(l) \ (F^# u K^#));
    (Z4) tau_l = 0 if k(l) is a peak of f^#;  (Z5) sum_{l in G, m(l) = m, k(l) in Q^#} q^#_l tau_l = 0 (m in I);
    (box) tau_l <= 6 lambda_l/t,
  L_j(tau) := sum_l eps_l tau_l u_l(j).  (Further rows of the same kind used by an assembly, e.g. the generalized
  configuration rows of Y1, change nothing below as long as their coefficients are design data for each pattern.)
  By (1.0), q^#_l = val^#_l/A^#_m in (Z5).  A PATTERN kappa of level l is the finite combinatorial datum fixing Sigma^#
  except the values: the set G, the signs eps_l, the contact pattern and signs z^#_j on T(l), the statuses (peak /
  strict non-peak) of the carriers of G at f^#, the block assignment.  Put L_0(kappa) := {l in G : k(l) strict non-peak}.

## 2.1 Why the linear (component) exactification is not enough
For one block, (Z5) is one row and Y4 Lemma 1.8 bounds its Hoffman part by 1/D_min (D_min = least nonzero ray d-sum);
Y4-ref Cor. P5 / V1 make every tiny ray d-sum (and every tiny COMPONENT D_{r,m} of a multi-block ray d-vector) exactly zero
by LINEAR tuning.  With several blocks the d-vectors D(r) = (D_{r,m})_m in R^N of extreme rays r may be nearly linearly
dependent while all components are robust.  Example (two blocks, two rays): D(r_1) = (1, 1), D(r_2) = (-1, -1 + delta).
For mu = (1,1) (tau = r_1 + r_2) the d-vector is (0, delta), while C cap ker D = {0} for delta != 0: dist_1(tau, Z)/|D tau| >=
2/delta (V2_work/hoffman_minors_check.py: ratio 2/delta for delta = 1e-1..1e-4, bounded (<= 1/2) at delta = 0).  The
obstruction is the 2x2 minor det = delta, a QUADRATIC polynomial in the values: making it zero is not a linear problem.
This is the "determinantal" form of (m') (Y4 1.5 Limitation, Y4-ref C.7/E, V1's (VR_w)).

## 2.2 Determinantal rate objects and the design D^{V2}
**Definition 2.1 (determinantal objects).**  For a pattern kappa of level l let A_kappa(v) (v in R^{L_0(kappa)}) be the
matrix of Sigma^# with the row (Z5) of block m replaced by (v_l 1[l in L_0(kappa), m(l) = m])_{l in G} (i.e. A^#_m := 1).
Its entries are 0, +-1, design data (eps_l z_j u_l(j), j in T(l)) or coordinates of v; each v_l occurs in exactly one
entry.  For row and column index sets J, K with |J| = |K| >= 1, J containing at least one (Z5)-row and never a row
together with its negative, put pi_{kappa,J,K}(v) := det A_kappa(v)_{J,K}, a multi-affine polynomial with design
coefficients.  The OBJECT O = (kappa, J, K) has the rate rho_O(f) := |pi_{kappa,J,K}((val_l(f))_{l in L_0(kappa)})|.
Minors with J free of (Z5)-rows are design numbers; delta_comb(l) := the least nonzero one over all patterns of level
<= l (a design constant).
The number of objects of level <= l is at most sum_kappa 4^{(rows + columns)(kappa)}: design-computable and N-free (patterns
over all subsets of [1,l], all blocks).  For each level l let C_L(l), N_L(l) be the constants of Lemma L for the finite
family {pi_O : O of level <= l} (variables: all v_l, l <= l), Lip(l) a common Lipschitz constant of these polynomials on
[-2,2]^l, and C_*(l) >= 1 a design constant bounding the motion of the values during the assembly (below).
**Definition 2.2 (design D^{V2}).**  D^PW (or V1's design) with: (i) the objects of Def. 2.1 added to the rate scheme
(omega(l) enlarged accordingly); (ii) Design(l) multiplied by Lip(l) (2 + 1/delta_comb(l)) (rows(l) cols(l))^{l} C_*(l);
(iii) with eta(w) := T_lo(w)^4/(l Design(l)) (Design(l) also contains C_L(l)):
       b(w) := min{ eta(w), (eta(w)/C_L(l))^{N_L(l)/2} } / (1 + Lip(l) C_*(l));
everything else as in D^PW (u(w) := b(w^-), Q(w), n(w), T_hi, T_lo, c_{l+1} := min{c_l/4, T_lo(l,M(l))^3, b(l,M(l))^2}).
**Lemma 2.1.**  PROVED.  D^{V2} is admissible and N-free; the bands (b(w), u(w)) are nonempty and pairwise disjoint; every
statement proved for D^PW (Y4 Lemma 1.5(c), Thm 1.6, Cor 1.7 with Y4-ref A.3) and for V1's assembly holds verbatim, since only
b(w) decreased and Design(l), omega(l) increased by design quantities; moreover, with beta(w) := (1 + Lip(l) C_*(l)) b(w),
     beta(w) <= eta(w) < 1/C_L(l)   and   C_L(l) beta(w)^{2/N_L(l)} <= eta(w),                                  (2.1)
and every design multiple Design(l)^k T_lo(w) (k <= 4) is <= u(w)/8 for l >= l_0 (design).
Proof.  All added quantities are determined by the level-l design data (u_{l'} for l' <= l, the patterns), which are fixed
at stage l of the recursion before the sub-windows of level l are defined (y_l is chosen by allowedness with c_l, fixed at
stage l-1).  b(w) <= T_lo(w)^4 <= 2^{-4n(w)} < u(w) as in Y4 Lemma 1.5(b); smaller b keeps every inequality of the form
"b <= T_lo^4/(l Design)" used before.  (2.1): beta <= min{eta, (eta/C_L)^{N_L/2}}, so C_L beta^{2/N_L} <= eta, and
eta < 1/C_L because C_L(l) <= Design(l) and T_lo <= 2^{-l^3}.  Last claim: n(w) >= l 2^{l^3} Q(w) >= Design(l) (4/u(w)), so
T_lo(w) <= 2^{-4 Design(l)/u(w)} and Design^k 2^{-4 Design/u} <= u/8 once Design(l) >= 8k.  QED

## 2.3 Buffer peaks exist at every level
**Lemma 2.3.**  PROVED.  There is l_f such that for every level l >= l_f and every block m there is a coarse peak c = c_m
(level <= l) with |alpha_m(c)| >= 1/(2l); its relative margin rho_c - 1 = nu_c/theta_m - 1 is >= sigma_m/(2 l m q_0 theta_m) and
its absolute margin is mu_c >= sigma_m/(2 l lambda_c).
Proof.  sum_{k in P_m} |alpha_m(k)| = 1 (Lemma lem:threshold) and |alpha_m(k)| = lambda_k mu_k/sigma_m (eq:margin) with
mu_k <= q_0 |u_k(zhat)| <= q_0; hence the peaks of level > l contribute at most q_0 sum_{l' > l} lambda_{l'}/sigma_m <=
q_0 T_lo(l)^3/sigma_m <= 1/2 for l >= l_f, and block m has at most l coarse peaks.  The margins follow from eq:margin.  QED
(For l >= l_f these margins exceed u(w) by any design factor, since u(w) <= 2^{-l^3}: the buffer peak is ROBUST.)

## 2.4 Theorem B (multi-block exactification)
**Theorem B.**  PROVED (modulo the cited tools: Y4-ref Prop. P4 / V1 Lemma TU, Z3 Lemma 3.1, Y1 Lemma T2).  Design D^{V2},
diagonal U, F finite.  Let w = (l,i) be a clean sub-window for f (Y4 Thm 1.6 with the objects of Def. 2.1), l >= l_f.  Let
an assembly (V1 3.2; Y1 4.1; Y4-ref C.6-C.7) be given in the following form: first its z-moves on coarse supports (closing
class-G rooms on the S^nat sets, closing tiny target rooms on T(l)), producing a row f_1; then finitely many further moves
M_ass at coordinates beyond s_max(l) of carriers NOT in L_0(kappa) (donor raises: z-moves or banks; pulls converting
tiny-margin peaks), and the pattern kappa it produces.  Assume
 (A1) |val_{l'}(f_1) - val_{l'}(f)| <= C_*(l) b(w) for l' in L_0(kappa) (true for the z-move closings: (C1) moves a class-G
      value by its tiny room, (C2) by <= |T(l)| b; V1 Lemma ST(a)), and p*(f_1 - f) <= C_f Design(l) b(w) log(e/b(w));
 (A2) after M_ass every coarse carrier of G has the status prescribed by kappa, with relative margin >= u(w)/2 at peaks of
      kappa and either a gap >= c_f Lambda (V1 Lemma ST, donor raise Lambda = T_lo^3) or a relative position rho <= 1 - u/2 at
      strict non-peaks of kappa (or, if no donor raise is used in a block, all its coarse strict non-peaks of kappa have
      rho <= 1 - u/2 or rho <= C_* b and all its peaks of kappa have relative margin >= u/2 at f_1).
Then there is a companion f^# (the moves M_ass, the tuning of L_0(kappa) and, where needed, one outward push of the buffer
peak c_m per block, realized by ONE application of Lemma TU / Prop. P4) with:
 (a) the pattern of f^# is kappa (same G, signs, contacts on T(l), statuses); supp a^# finite;
 (b) val_l(f^#) = val_l(f_1) + x_l EXACTLY for l in L_0(kappa), with |x|_2 <= eta := T_lo(w)^4/(l Design(l)), and
     pi_O(val(f^#)) = 0 for every object O of kappa that is tiny at f (rho_O(f) <= b(w)), while |pi_O(val(f^#))| >= u(w)/2
     for every object that is robust at f;
 (c) p*(f^# - f) <= p*(f_1 - f) + C_f(cost of M_ass) + C_f Design(l)^2 eta log(e/eta) = o(T_lo(w)^2) (for V1's assembly
     C_f Design T_lo^3 log(1/T_lo));
 (d) the Hoffman constant of Sigma^# at f^# (all rows (Z1)-(Z5), box rows; l_1 residuals and distances) satisfies
        C_H^# <= C_f^l Design(l)^2 / u(w),
     for EVERY configuration of the zero-cost cone (single- or multi-block rays, compensated, mixed or one-signed blocks,
     any face structure).
Proof.  Step 1 (objects at f_1).  For every object O of kappa, |pi_O(val(f_1)) - pi_O(val(f))| <= Lip(l) C_*(l) b(w)
by (A1).  Hence tiny objects satisfy |pi_O(val(f_1))| <= beta = beta(w) of (2.1), robust ones >= u(w) - beta >= 3u(w)/4
(Lemma 2.1, last claim).
Step 2 (Lojasiewicz).  Apply Lemma L to the family of level l with S := the tiny objects of kappa and v := val(f_1)
(in [-2,2]^l since |u_l(zhat)| <= q*(u_l) = 1).  Alternative (i) of Lemma L is excluded because beta < 1/C_L(l) (2.1).
So there is v' with pi_O(v') = 0 (O tiny) and |v' - v|_2 <= C_L(l) beta^{2/N_L(l)} <= eta (2.1).  Put x := v' - v
restricted to L_0(kappa) (the polynomials of kappa involve only these coordinates).  Robust objects: |pi_O(v')| >=
3u/4 - Lip(l) eta >= u/2.
Step 3 (one combined realization).  Apply Lemma TU (V1 3.4; = Y4-ref Prop. P4 with explicit bank solution) at the row
obtained from f_1 by the moves M_ass (their masses and z-changes are part of the base A^p of its proof; their coordinates
are distinct from the pull and bank coordinates of L_0, which lie in the S_{l''}, l'' in L_0, beyond s_max(l)), with the
carrier set L_0(kappa) and the targets val^#_{l''} := v'_{l''}: since Lemma TU solves for EXACT values given all other
masses, the second-order side effects of M_ass on the L_0 values are absorbed, and val^#_{l''} = v'_{l''} = val_{l''}(f_1)
+ x_{l''} exactly.  The required increments are |x| + O(side effects) <= 2 eta <= c_T (c_T = f-constant x Design^{-3} >>
eta = T_lo^4/(l Design), Lemma 2.1).  Other coarse carriers k notin L_0 move by <= C_T eta^2 beyond the effect of M_ass
(Lemma TU(b)); all pulls/banks lie beyond s_max(l), so T(l), the contact pattern on T(l) and all swallowing signs are those
of the assembly; fine carriers: sum_{k > l} lambda_k |Delta u_k| <= 2^{-l} eta + (fine effect of M_ass).  Cost: Lemma TU(d).
Step 4 (statuses).  With V1's assembly, Lemma ST of V1 applies verbatim with the additional value moves |x| + C_T eta^2 <=
2 eta << c_f Lambda = c_f T_lo^3 (V1's raised blocks) and << u(w) (robust carriers): every coarse carrier keeps the status
prescribed by kappa.  In a block without donor raise in which a protection is needed (a self-contained assembly), push the
buffer peak c = c_m of Lemma 2.3 outward inside the same Lemma TU solve (c notin L_0): with zeta := R_m^** zhat_1 and
zeta^# := R_m^** zhat^#, X := max over coarse k != c of |zeta^#(k) - zeta(k)|/Phi_k^2 <= m(2 eta)/Phi_min(l) <= C D(l) eta and
E := sum_{k != c} |zeta^#(k) - zeta(k)| <= phi X + 2^{-l} eta (sum_k m Phi_k |Delta u_k| = sum_k Phi_k^2 (m|Delta u_k|/Phi_k)),
take r_m := C_*(l) b(w) theta_m and the push s := (16(A + theta + 1)/A) max{E, phi(X + r_m)} (a-priori bounds for E, X with
|y| <= C_f Design^2 eta for the push itself; A, theta, phi of block m at f_1).  Then E <= A s/(8(A+theta+1)), so Lemma QB
gives theta^#_m - theta_m >= R(s) >= X + r_m and theta^#_m - theta_m <= C_1(s + E), C_1(s + E) + X <= C_f Design(l)^2 eta <=
u(w) theta_m/4: every coarse strict non-peak of kappa (nu < theta_m, or nu <= theta_m + r_m for a tiny-margin peak declared a
non-peak) stays a strict non-peak (Lemma QB(b)); every coarse peak of kappa (relative margin >= u/2) stays a peak with its
sign (Lemma QB(c)); c stays a robust peak.  So the pattern of f^# is kappa: (a).  The common factors 1/A^#_m of (Z5) change
nothing in (b).
Step 5 (cost).  p*(f^# - f_1) <= C_f(cost of M_ass) + C_T(2 eta) log(e/(2 eta)) + C_f (s/lambda_c) log, and eta, s/lambda_c <=
C_f Design(l)^2 eta, eta = T_lo^4/(l Design): (c) (Lemma 2.1, last claim, for o(T_lo^2)).
Step 6 (Hoffman).  The matrix of Sigma^# at f^# is A_kappa(val(f^#)) with the (Z5)-row of block m multiplied by
1/A^#_m in [1/(2A_max), 2/A_min] (A_m = sigma_m/q_0 moves by C_f Delta: Z3 Lemma 3.1).  Its minors containing (Z5)-rows
equal (prod of the factors 1/A^#_m of the rows used) x pi_O(val(f^#)): by (b) they vanish or have modulus >=
(2A_max)^{-N} u(w)/2; the other minors are design numbers, zero or >= delta_comb(l).  Lemma H (1.3) (with the l_1/l_2
conversion factors sqrt(rows), sqrt(cols) <= (rows cols)(l)) gives C_H^# <= max(1, ||A||_2)^{l-1} (rows cols)(l) /
min(delta_comb(l), (2A_max)^{-N} u(w)/2) <= C_f^l Design(l)^2/u(w) (entries of (Z5)-rows are <= 2/A_min): (d).  QED
**Corollary B.1 (no multi-block residual).**  PROVED (given the assembly).  In Prop. T / Y1 Prop. 5.2 / V1's transplant at
a clean sub-window of D^{V2}, hypothesis (HF) holds with C_H^# <= C_f^l Design(l)^2/u(w), and the d-row violations of the
actual amplitudes at f^# are <= |Delta d|-pinning terms + C eta/t <= (pinning) + C T_lo^3 (since |q^# - q| <= C eta and
sum_l |tau_l| <= 6/t).  Hence the window constant is K <= (room product) x C_f^l Design^2/u x (pinning constants), absorbed
by Q(w); items (m) (f-dependent d-row Hoffman constants: Y2 Theorem M's K_F^rel, Z4 Lemma R, mixed blocks without (DR),
Conjecture G as far as it is used for d-rows) and (m') (multi-block rays) are NOT residuals of the companion route.
What Theorem B does NOT do: the bound on the d-row VIOLATION of tau itself requires the uniform shift Delta d_m to be
pinned at f ((SP_w), Y2 Theorem H) — item (C), Part 3.
Remarks.  (1) No ray enumeration, no (VR_w), no compensators, no one-signedness: Lemma H controls the full system at once.
(2) The exponent 2/N_L(l) of Lemma L is non-explicit; the design absorbs it through (iii) of Def. 2.2, which is legitimate
because b(w) only has to be SOME design quantity (Y4 Cor. 1.7: costs must be o(T_lo^2), bands disjoint).
(3) Status management: in V1's assembly the donor raise Lambda = T_lo^3 (V1 Lemma ST) already dominates the moves
eta <= T_lo^4/(l Design) of Steps 2-3, so Step 4 is needed only in blocks without donors (Y2's aligned corner, item
(D)); Lemma QB + Lemma 2.3 show that the buffer push at a robust coarse peak, available in EVERY block by two-sided
tuning, replaces the donor for the exactification step (and for Y4-ref Cor. P5: its "status part of (BS)" is
discharged the same way).
(4) Tuning a carrier rescales the d-coefficients of its block by the common factor A_m/A^#_m (Y1 Cor. T3, (1.0)): this
multiplies whole (Z5)-rows and never turns a zero minor into a nonzero one (Step 6).
