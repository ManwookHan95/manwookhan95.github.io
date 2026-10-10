# V4 part 1 — What the residual configurations (B)-(E) require: design data versus first-row data

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; numbering and notation as there), the refereed Rounds 5-6
(Z3 Thm E / Lemma U / Lemma 3.1; Z4 Thm A'' and (H2''); Y1 design D_X, Lemma T, master theorem; Y2 Prop Q, Thm H, 5.3;
Y4 + Y4-ref C.2-C.7 pulls, banks, Cor P5; Y3 + Y3-ref).  Finite block set I = {1..N}, p = p_N.  "SLD-type design" = any of
Definition def:SLD, SLD_G, D''', D^PW, D_X, D^Y (only (T-a)-(T-d), (P1)-(P3) and allowedness (a),(b) are used, plus the
super-fast decay c_{l+1} <= c_l T_lo(l)^3 of the weights).  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.0 Standing notation; the diagonal base
DESIGN DATA.  Ladder bijection j, carriers l <-> (k(l), m(l)); pairwise disjoint infinite signature sets S_l; h_l =
sum_{s in S_l} 2^{-s} e_s^*, H_l := ||h_l||_1, delta_l; targets y_l in c_00 ∩ S_{q*} (allowedness (a): supp y_l ∩ S_{l'} = {}
for l' >= l; (b): 2c_l <= 2^{-2s} c_{l'} delta_{l'} for s in supp y_l ∩ S_{l'}, l' < l); n_l = q*(y_l + delta_l h_l);
u_l = (y_l + delta_l h_l)/n_l; v_l := delta_l h_l/n_l; weights c_l; Phi_l := Phi_{m(l)}(k(l)) = 2^{-m(l)-k(l)} c_l;
lambda_l = m(l) Phi_l.  BASE: U diagonal, U^* e_j^* = s_j kappa_j ((kappa_j) orthonormal in H, s_j > 0, sum s_j^2 < infinity):
compact, U^* injective, so U has dense range; this is an admissible base (note, Section 1).
FIRST-ROW DATA.  Any (a, z) with q*(a) = 1, z in B_{l_infty}, z = sgn a on F := supp a (Remark rem:lemmaZ(c): every such pair
is the forced data of exactly one f in S_{p*}).  Derived: nu = ||U^*a|| = (sum_j s_j^2 a_j^2)^{1/2}, e = U^*a/nu,
(Ue)_j = s_j^2 a_j/nu (zero off F), zhat = z + Ue.  Values val_l := u_l(zhat).  For block m: zeta_m := R_m^** zhat,
zeta_m(k) = lambda_{k,m} val_{j(k,m)}; theta_m := theta(zeta_m) (Y2/Y1 Lemma T); nu_k := |zeta_m(k)|/Phi_m(k)^2 =
m |val|/Phi; P_m = {nu_k >= theta_m}; degenerate peaks nu_k = theta_m; margins mu_k = q_0 Phi_k (nu_k - theta_m)/m on P_m;
gaps gap_k = C_m (theta_m - nu_k)/|zeta_m| off P_m; varsigma_k = sgn w_m(k) = sgn val; swallowing sign eps_l (z = eps_l on
S_l \ F); d-weights q_l = eps_l Phi_l w_m(k(l))/(m C_m).  Contacts K = {j notin F : |z_j| = 1}, free coordinates J = rest.

**Lemma 1.1 (value formula, diagonal base).  PROVED.**  For every carrier l and every admissible (a, z),
   n_l val_l = sum_{j in supp y_l \ F} y_l(j) z_j + sum_{j in supp y_l ∩ F} y_l(j)(sgn a_j + s_j^2 a_j/nu)
             + delta_l sum_{s in S_l \ F} 2^{-s} z_s + delta_l sum_{s in S_l ∩ F} 2^{-s}(sgn a_s + s_s^2 a_s/nu).
In particular, if S_l ∩ F = {} (all but finitely many l, since F is finite and the S_l are disjoint) and l is swallowed with sign
eps_l, then  n_l val_l = y_l(zhat) + eps_l delta_l H_l.
*Proof.*  u_l(zhat) = u_l(z) + <U^* u_l, e>, and <U^* u_l, e> = sum_j s_j u_l(j) <kappa_j, e> = sum_j s_j^2 u_l(j) a_j/nu, which
vanishes off F.  QED
So with a diagonal base the first row influences a carrier value only through z on supp u_l and through a on supp u_l ∩ F.

**Lemma 1.2 (forced sharing of coordinates).  PROVED.**  (a) For every admissible T, every coordinate j and every block m,
u_{k,m}(j) != 0 for infinitely many k.  (b) For every SLD-type design, every j and every m, j in supp y_l for infinitely many
carriers l of block m.
*Proof.*  (a) e_j^*/q*(e_j^*) in S_{q*} is a q*-limit (hence l_1-limit) of u_{k,m}, k -> infinity (T-d and the remark after
Definition def:admissible), so u_{k,m}(j) -> 1/q*(e_j^*) != 0.  (b) For carriers l of block m with j notin S_l, u_l(j) =
y_l(j)/n_l; at most one carrier has j in its signature set.  Apply (a).  QED
Consequence: targets of carriers of DIFFERENT blocks share coordinates at infinitely many levels; no design can make the target
supports of two blocks disjoint (this is the design-only part of (B), see 1.2).

## 1.1 What "requirement" means
A residual configuration is a property of (design, f) (and of (g, rho) and a window) under which the proved machinery stops.
Its defining relations split into (DO) relations among design data only, and (FR) relations involving the first-row data (a, z)
(and the design).  As (a, z) is arbitrary, a configuration can be excluded by the design only through a (DO) relation that the
design violates, or through an (FR) system that is unsolvable in (a, z) for the given design.  Remark rem:nodesign shows the
basic obstruction: for ONE vector V, the choice z_j := sgn V(j) off F makes V of zero base cost.  The configurations below need
SIMULTANEOUS conditions on many vectors; the question is whether the design can make these systems unsolvable.

## 1.2 (B) multi-block rays (Y4 1.8 "Limitation", Y4 (R6), Y4-ref E, V1 2.6)
Object.  At a clean sub-window w of level l (after single-block neutralization, Y4-ref Cor P5): the pattern kappa(w) =
(U, P, eps, F', type) and its zero-cost cone C(kappa) = {tau in R^U : tau >= 0 on U \ P, tau = 0 on P, type(j) L_j(tau) >= 0
(contacts), L_j(tau) = 0 (free j), j in T(l) \ F'}, L_j(tau) = sum eps_l tau_l u_l(j); the d-map D : R^U -> R^I,
D_m(tau) = sum_{l in U, m(l) = m} q_l tau_l.  Residual (B): the relative Hoffman constant H(C, D) := sup_{tau in C, D(tau) != 0}
dist_1(tau, C ∩ ker D)/|D(tau)| is not bounded by Design(l) u(w)^{-k} although every single-block ray component is robust or
exactly zero; equivalently (Y4 (R6)) some set S of <= N extreme rays of C(kappa) meeting several blocks has a d-matrix
[D_m(r)]_{m in I, r in S} with tiny but nonzero smallest singular value.
Requirements:
 (B-i)  [FR] switchable carriers in at least two blocks.  Switchable carriers are swallowed strict non-peaks (peaks have
        rows tau = 0 in the pattern; Y4-ref C.7).  A swallowed strict non-peak with S_l ∩ F = {} needs, by Lemma 1.1,
           |y_l(zhat) + eps_l delta_l H_l| < n_l theta_m Phi_l/m,                                              (1.2.1)
        a TUNING of the target value to precision O(Phi_l) (Phi_l is super-small compared with delta_l H_l).  The tuning uses a
        continuous first-row parameter in supp u_l: a coordinate of supp y_l ∩ F (through a), or a free coordinate of supp y_l.
 (B-ii) [DO + FR] a ray of C(kappa) meeting two blocks: a chain of coordinates j in T(l) linking carriers of different blocks;
        the link at j needs j in supp y_{l_1} ∩ supp y_{l_2} (DO; unavoidable by Lemma 1.2) and j free, or a contact at which
        some eps_{l_i} y_{l_i}(j) z_j < 0 (FR).
 (B-iii)[FR] near-degeneracy of a joint d-object.  At strict non-peaks q_l = (q_0/sigma_m) eps_l val_l (Y4-ref C.7), so the
        d-matrix entries D_m(r) = (q_0/sigma_m) sum_{m(l) = m} r(l) eps_l val_l are LINEAR in the first-row values with
        coefficients r(l) fixed by design numbers u_l(j) and the (FR) types.
Design-only content: only the shared coordinates of (B-ii), which no design can remove (Lemma 1.2).  All other relations are
(FR) relations involving tuned values; see part 2 for realizability and part 4 for the triangular structure of D.

## 1.3 (C) coherent shift resonance (Y2 5.2-5.3, Z4-ref 3.3, V1 2.5)
Object.  A block m in configuration (i) (UPPER fails: every coarse peak used as shift source is swallowed with the swallowing
sign eps_l = varsigma_l, and some swallowed carrier has q_l < 0) or (ii) (LOWER fails: every non-degenerate peak swallowed with
anti sign, some swallowed carrier with q_l > 0), together with c_*(l) = 0 (exact coherence) or c_*(l) tiny at the relevant
levels (V1: c_pi <= b(w) at clean sub-windows), where
   c(delta; l) = inf_{x >= 0} sum_{j notin F} phi_{z_j}( sum_m delta_m Pi_m(j) + sum_{l' in Bfree} x_{l'} eps_{l'} u_{l'}(j) ),
   Pi_m = sum_{l in P*_m} varsigma_l lambda_l u_l 1_{F^c}   (the PEAK TRACE of a uniform shift of block m).
Requirements (configuration (i); (ii) is symmetric):
 (C-i)   [FR] z = sgn(val_l) on S_l \ F for every coarse robust-margin peak l of block m (swallowing-type swallowing);
 (C-ii)  [FR] a swallowed carrier l_- of block m with q < 0: eps_{l_-} = -sgn val_{l_-}; if it is a strict non-peak, (1.2.1) holds;
 (C-iii) [FR] zero cost of delta Pi_m + sum x eps u: z_j V(j) = |V(j)| at contacts, V(j) = 0 at free j, for V := that vector.
**Lemma 1.3 (the shift is fed only by negative d-weights).  PROVED.**  In the setting of Lemma lem:budget (two-sided
decomposition at scale t <= min(t_eta, 1)), for a block m in which every coarse peak used is swallowing-type, with K* t the
pinning bound of the good carriers (Lemma lem:modswallow(a) or Y1 Lemma 3.1):
   Delta d_m M_m (1 + sum_{l in Pk} q_l lambda_l) <= sum_{l in B, l <= l_*, q_l < 0} |q_l| (tau_l)_+
                                                     + sum_{l in B, q_l > 0, l notin Pk} q_l (tau_l)_- + C (K* + 1) t/C_m,
where Pk = swallowed coarse peaks of block m, B = swallowed carriers, tau_l = -eps_l Delta theta_l.  In particular, if block m
has no swallowed carrier with q < 0, then Delta d_m M_m <= C(K* + D_-) t (D_- := the projected negative parts, O(K_1 t) in Z4
Step 3), i.e. configuration (i) needs (C-ii); and, since |q_l| < Phi_l M_m/(m C_m) at strict non-peaks and (tau_l)_+ <= 6
lambda_l/t (box), the free shift at scale t is at most (6 M_m/(C_m t)) sum_{l in B, q_l < 0, l <= l_*} Phi_l^2 + C(K*+1)t/C_m:
LARGE (>> t) only through swallowed q < 0 carriers with Phi_l >> t.
*Proof.*  eq:didentity: Delta d M = (1/(mC)) sum_k Phi_k w(k) Delta theta_k + r, |r| <= 2t/sigma.  Good carriers: modulus
<= K* t/(mC) (Phi |w| <= 1).  Fine carriers (> l_*): <= 6 t^2/(mC) (box + (P2)).  Swallowed carriers: Phi w Delta theta/(mC) =
-q_l tau_l (definition of q_l, tau_l).  At a swallowed peak, eq:peakshift / Y2 Lemma 5.1: tau_l = lambda_l (Delta d M + e_k),
e_k >= 0, q_l > 0 (swallowing type: q_l = Phi M/(mC)), so -q_l tau_l <= -q_l lambda_l Delta d M.  At other swallowed carriers,
-q_l tau_l <= |q_l|(tau_l)_+ if q_l < 0 and <= q_l (tau_l)_- if q_l > 0.  Collect the Delta d M terms on the left.  The bounds
on |q_l| and (tau_l)_+ are |w(k)| < M at strict non-peaks and Lemma lem:box.  QED
So (C) is equivalent to: a zero-cost (or nearly zero-cost) combination whose dominant part is switching through swallowed
carriers of NEGATIVE d-weight (a ray of negative d-sum), the peak trace being carried along at relative size |q| ~ Phi.
Design-only content: none.  (C-i)-(C-iii) are sign/zero conditions on (FR) data, linear in the design vectors u_l.

## 1.4 (D) aligned corner (Y2 3.4, Y2-ref 3 (Lemma R-T); V1 2.4 claims donors at every clean window)
Requirements: (D-i) [FR] a non-rigid degenerate swallowing-type peak l_D used for switching: nu_{k(l_D)} = theta_m EXACTLY
(an exact tuning of |val_{l_D}| to theta_m Phi_{l_D}/m); (D-ii) [FR] every good carrier with w != 0 far-aligned (z = varsigma_l
on a cofinite part of S_l \ F for peaks, z = -sgn w for strict non-peaks); (D-iii) [FR] no anti-sign swallowed peak; (D-iv) [FR]
only finitely many raisable carriers; (D-v) [FR] no target move with positive one-sided threshold derivative.  Design-only
content: none.  (V1 part 2.4 proves that every block has, at every clean sub-window of large level, a coarse peak with robust
margin, a donor candidate; together with bank/pull raises this addresses (D) from the method side.  Not refereed here.)

## 1.5 (E) critical support swallowing (Y3 1.1-1.2, 3.5; Y3-ref F5)
Requirements: (E-i) [FR] F infinite and a bad carrier l with S_l ∩ F infinite (support swallowing), z = eps_l on S_l \ F;
(E-ii) [FR + DO] the flip profile m_l(x) := sum{ v_l(s) : s in S_l ∩ F, |a_s| < x v_l(s) } is critical:
0 < liminf_{x->0} m_l(x)/x <= limsup_{x->0} m_l(x)/x < infinity (model |a_s| ~ v_l(s)^2).
Design-only content: the SHAPE of the signature profile (v_l(s))_{s in S_l}.  (E-ii) is a joint relation between the first-row
masses a_s and the design profile; for geometric profiles (v_l(s) = delta_l 2^{-s}/n_l) it is solvable (Y3 model), for
LACUNARY profiles it is not (part 2, Lemma 2.6).

## 1.6 Summary table
| config | design-only (DO) relations | first-row (FR) relations | can a design violate the DO part? |
|---|---|---|---|
| (B) | shared target coordinates of two blocks | tuned values (1.2.1) of switchable carriers; link types; near-singular joint d-matrix (linear in values) | NO (Lemma 1.2) |
| (C) | none | swallowing-type swallowing of the robust peaks; a swallowed q<0 carrier; zero cost of delta Pi + sum x eps u | nothing to violate |
| (D) | none | an exact degenerate peak; alignment of all good carriers; no anti-sign peak; finitely many raisable carriers | nothing to violate |
| (E) | signature profile shape | infinite support swallowing with critical flip profile | YES for criticality (lacunary profiles, Lemma 2.6), at a price (part 2.5) |
Whether the (FR) systems are SOLVABLE for every SLD-type design is the content of part 2 (realizability).
