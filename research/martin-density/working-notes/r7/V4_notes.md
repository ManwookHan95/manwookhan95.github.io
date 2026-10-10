# V4 notes — Can the residual configurations (B)-(E) be excluded by the design of T and a diagonal base U?

Author: V4 (Round 7).  Part files: r7/V4_part1.md ... V4_part5.md (labels below are those of the part files; this file supersedes
them where they differ — see Section 14 for the list of corrections).  Scripts: r7/V4_work/sa_check.py, degenerate_check4.py.
Setting: paper/martin_density_note.tex (Sections 1, 7, 8; notation as there) and the refereed Rounds 5-6 (Z3 Lemma 3.1 / Lemma U /
Theorem E; Z4 (H2''); Y1 Lemma T; Y2 Prop Q, 5.3; Y4 + Y4-ref C.2-C.7 (banks, pulls, Lemma P2, Prop P4)).  Labels: PROVED / SKETCH /
HEURISTIC / FALSE / OPEN.

## 0. Answer in brief
1. (B), (C), (D) can NOT be excluded by design.  For every SLD-type design (after harmless modifications that every design admits,
   Lemma 2.1) and every diagonal base, explicit first rows realize (C) with EXACT coherence and (D) with a weak swallowing-type peak
   (Theorem 2.2, Remark 2.3; PROVED), and (B) (SKETCH).  The only design-only relation among their requirements is the sharing of
   target coordinates between blocks, which density forces (Lemma 1.2).  (E): its CRITICAL form is excluded by lacunary signature
   profiles (Lemma 2.6, PROVED), at the price of pull tuning (HEURISTIC).
2. These configurations are residuals of the window METHOD, not obstructions: the realizing rows are block-tame, hence recovered
   (Corollary 3.1); the most dangerous explicit coherent-shift mates are recovered (Proposition 3.2, numerically checked), also when a
   swallowing-type peak is EXACTLY degenerate (Corollary 5.7).
3. Design cannot exclude near-threshold carriers tuned through F: they are Baire-generic in every fixed-z fibre (Proposition 5.1,
   PROVED; the design question (GO) is answered negatively).  Block-tame rows are nevertheless dense (Theorem 3.5/Proposition 5.3).
4. Exact two-piece data with negative d-mismatch force OWNER ALIGNMENT of the row outside "dead zones" (Proposition 4.2'), and such
   data are recovered whenever there are no dead zones (Theorem 5.6, PROVED); for designs with fresh-dominated carriers (FD), positive
   mismatches next to negative ones force dead zones (Proposition 5.8); all-non-negative mismatches are recovered by Cor. cor:D1.
5. No counterexample was found.  A counterexample with F finite must use mates without exact two-piece data (window residuals (B), (C))
   or exact data with dead zones; the precise remaining step is a stability statement for nearly exact data at block-tame companions
   (Section 12).  Leaning: positive (density).

## 1. Setting and notation
DESIGN DATA.  Carriers l <-> (k(l), m(l)) (ladder bijection); pairwise disjoint infinite signature sets S_l; h_l = sum_{s in S_l} 2^{-s} e_s^*,
H_l := ||h_l||_1; delta_l; targets y_l in c_00 ∩ S_{q*} with allowedness (a) supp y_l ∩ S_{l'} = {} for l' >= l, (b) 2 c_l <= 2^{-2s} c_{l'} delta_{l'}
for s in supp y_l ∩ S_{l'}, l' < l; n_l = q*(y_l + delta_l h_l) in [3/4, 5/4]; u_l = (y_l + delta_l h_l)/n_l; v_l := delta_l h_l/n_l; weights c_l with
c_{l+1} <= c_l/4; Phi_l := Phi_{m(l)}(k(l)) = 2^{-m(l)-k(l)} c_l; lambda_l = m(l) Phi_l.  "SLD-type design": any of Definition def:SLD,
SLD_G, D''', D^PW, D_X, D^Y, D_Omega (only (T-a)-(T-d), (P1)-(P3), allowedness and super-fast decay are used).
BASE.  U diagonal: U^* e_j^* = s_j kappa_j, (kappa_j) orthonormal, s_j > 0, sum s_j^2 < infinity (compact, injective adjoint, dense range).
FIRST ROW.  Forced data (a, z): q*(a) = ||a||_1 + ||U^* a|| = 1, z in B_{l_infty}, z = sgn a on F := supp a; every such pair is the forced
data of exactly one f in S_{p*} (Remark rem:lemmaZ(c)).  nu := ||U^* a|| = (sum s_j^2 a_j^2)^{1/2}, e := U^* a/nu, (Ue)_j = s_j^2 a_j/nu,
zhat := z + Ue; val_l := u_l(zhat).  Block m: zeta_m(k) = lambda val, theta_m (Lemma T: Psi(th) = A(th)^2 - B(th), A = sum (|zeta(k)| - th
Phi_k^2)_+, B = sum Phi_k^2 min(th, nu_k)^2), nu_k = |zeta(k)|/Phi_k^2 = m|val|/Phi; peaks P_m = {nu >= theta}, degenerate if nu = theta;
strict non-peaks Q_m; margins mu = q_0 Phi (nu - theta)/m; gaps gap = C(theta - nu)/|zeta|; norming w_m: w(k) = sgn(zeta(k)) M on P_m,
w(k) = C zeta(k)/(Phi_k^2 |zeta|) = M (nu_k/theta) sgn(zeta(k)) on Q_m, M + C = 1, M = C theta/|zeta|.  Swallowing sign eps_l (z = eps_l on
S_l \ F); d-weights q_l = eps_l Phi_l w(k(l))/(m C).  Contacts K = {j notin F : |z_j| = 1}; free coordinates J = the rest off F.
OWNER of a coordinate j: the first carrier o(j) with u_{o(j)}(j) != 0 (a design notion; if j in S_l then o(j) = l by allowedness (a)).
(BT) = F finite, every Q_m finite, no degenerate peak, (MS) [sum{Phi_m(k) : mu_{k,m} < s} = o(s)].  (SC) (Def. def:SC): for every
Upsilon there is s_i -> 0 with max_{m in I_-} Scr_m(Upsilon s_i)/s_i -> 0; it excludes degenerate peaks in I_-; (BT) implies (SC) for all
blocks.  Two-piece data (Def. def:twopiece): side-+/- admissible pairs (b^+-, omega^+-) representing g, supp omega_m ⊂ Q_m, Delta d_m :=
d_m(omega^-_m) - d_m(omega^+_m), kappa_w.  Theorem thm:engineered: two-piece data with kappa_w <= 1 and (SC) for I_- := {Delta d_m < 0}
give (f, g) in cl NA; Corollary cor:D1: no (SC) needed if all Delta d_m >= 0; Corollary cor:BTrecovered: (BT) points are in Rec.

## 2. What the configurations require (part 1)
**Lemma 1.1 (value formula).  PROVED.**  For every carrier l and admissible (a, z):
   n_l val_l = sum_{j in supp y_l \ F} y_l(j) z_j + sum_{j in supp y_l ∩ F} y_l(j)(sgn a_j + s_j^2 a_j/nu)
             + delta_l sum_{s in S_l \ F} 2^{-s} z_s + delta_l sum_{s in S_l ∩ F} 2^{-s}(sgn a_s + s_s^2 a_s/nu).
If S_l ∩ F = {} and l is swallowed with sign eps_l: n_l val_l = y_l(zhat) + eps_l delta_l H_l.
*Proof.*  u_l(zhat) = u_l(z) + <U^* u_l, e> and <U^* u_l, e> = sum_j s_j u_l(j) <kappa_j, e> = sum_j s_j^2 u_l(j) a_j/nu, zero off F.  QED
**Lemma 1.2 (forced sharing).  PROVED.**  (a) For every admissible T, every coordinate j and block m, u_{k,m}(j) != 0 for infinitely many k.
(b) For every SLD-type design, every j and m, j in supp y_l for infinitely many carriers l of block m.
*Proof.*  (a) e_j^*/q*(e_j^*) in S_{q*} is a q*-limit (hence l_1-limit) of u_{k,m}, k -> infinity ((T-d)), so u_{k,m}(j) -> 1/q*(e_j^*) != 0.
(b) Off S_l, u_l(j) = y_l(j)/n_l, and at most one carrier has j in its signature set.  QED
**Lemma 1.3 (the coherent shift is fed only by negative d-weights).  PROVED.**  In the setting of Lemma lem:budget (scale t <= min(t_eta, 1)),
for a block m all of whose coarse peaks used are swallowing-type, with K* t the pinning bound of good carriers,
   Delta d_m M_m (1 + sum_{l in Pk} q_l lambda_l) <= sum_{l in B, l <= l_*, q_l < 0} |q_l| (tau_l)_+ + sum_{l in B, q_l > 0, l notin Pk} q_l (tau_l)_-
                                                     + C (K* + 1) t/C_m,
(Pk = swallowed coarse peaks, B = swallowed carriers, tau_l = -eps_l Delta theta_l).  Hence, without a swallowed q < 0 carrier, Delta d_m M_m
<= C (K* + D_-) t; and the free shift at scale t is at most (6 M_m/(C_m t)) sum_{l in B, q_l < 0, l <= l_*} Phi_l^2 + C(K* + 1) t/C_m.
*Proof.*  eq:didentity: Delta d M = (1/(mC)) sum_k Phi_k w(k) Delta theta_k + r, |r| <= 2t/sigma.  Good carriers contribute <= K* t/(mC); fine
carriers <= 6 t^2/(mC) (box, (P2)); a swallowed carrier contributes -q_l tau_l.  At a swallowed swallowing-type peak (eq:peakshift / Y2 Lemma
5.1) tau_l = lambda_l (Delta d M + e_k), e_k >= 0, q_l = Phi M/(mC) > 0, so -q_l tau_l <= -q_l lambda_l Delta d M; elsewhere -q_l tau_l <= |q_l|(tau_l)_+
(q_l < 0) or q_l (tau_l)_- (q_l > 0).  Collect; |q_l| < Phi_l M/(mC) at strict non-peaks and (tau_l)_+ <= 6 lambda_l/t (Lemma lem:box).  QED
Requirements (DO = design-only relation, FR = involves first-row data):
 (B) multi-block rays (Y4 (R6)): (B-i) [FR] switchable carriers (swallowed strict non-peaks) in two blocks, each with
     |y_l(zhat) + eps_l delta_l H_l| < n_l theta_m Phi_l/m (a tuning to precision O(Phi_l) through a coordinate of supp y_l in F or J);
     (B-ii) [DO + FR] a link coordinate j in supp y_{l_1} ∩ supp y_{l_2} (DO; unavoidable by Lemma 1.2), free or a contact with a sign
     conflict; (B-iii) [FR] a near-singular joint d-matrix, whose entries D_m(r) = (q_0/sigma_m) sum r(l) eps_l val_l are LINEAR in values.
 (C) coherent shift resonance (Y2 5.2-5.3): (C-i) [FR] z = sgn(val_l) on S_l \ F for every coarse robust peak used; (C-ii) [FR] a swallowed
     q < 0 carrier (Lemma 1.3); (C-iii) [FR] zero cost of delta Pi_m + sum x eps u.  No DO relation.
 (D) aligned corner (Y2 3.4): (D-i) [FR] an exactly degenerate swallowing-type peak; (D-ii) [FR] all good carriers far-aligned; (D-iii) no
     anti-sign swallowed peak; (D-iv) finitely many raisable carriers; (D-v) no target move with positive threshold derivative.  No DO.
 (E) critical support swallowing (Y3): (E-i) [FR] F infinite, S_l ∩ F infinite, z = eps_l on S_l \ F; (E-ii) [FR + DO] critical flip profile
     0 < liminf m_l(x)/x <= limsup m_l(x)/x < infinity, m_l(x) := sum{v_l(s) : s in S_l ∩ F, |a_s| < x v_l(s)}.  DO part: the profile shape.
| config | DO relations | can a design violate them? |
|---|---|---|
| (B) | shared target coordinates of two blocks | NO (Lemma 1.2) |
| (C) | none | nothing to violate |
| (D) | none | nothing to violate |
| (E) | signature profile shape | YES for criticality (Lemma 2.6), at a price |
Remark rem:nodesign is the one-vector case of the obstruction: for one vector V, z_j := sgn V(j) off F gives V zero cost.  The systems
above involve many vectors; Section 4 shows they are nevertheless solvable for every design.

## 3. Design conditions (all designable)
(SF*)   (1 + ||U||) sum_{l'' > l} lambda_{l''} <= 2^{-10} lambda_l delta_l 2^{-(m(l)+k(l)+min S_l)} eta_l/n_l, eta_l := min(1, min_{supp y_l}|y_l(j)|),
        and c_l <= c_{l-1} delta_l 2^{-min S_l - l - 10}/(1 + ||U||) (l >= 2); the latter gives lambda_l <= delta°_l 2^{-l-9}, delta°_l := delta_l H_l/n_l.
(SF_tau) (SF*) with the extra factor tau_l on the right of the first inequality (tau_l in (0,1] a decreasing design sequence).
(b')    2 c_l <= tau_{l'} 2^{-2s} c_{l'} delta_{l'} for s in supp y_l ∩ S_{l'}, l' < l.
(Z0)    Z_0 := N \ union S_l contains p != p' (and p'', p''') and the family contains y* := (e_p^* - e_{p'}^*)/q* (and y** := (e_{p''}^* - e_{p'''}^*)/q*).
(GM)    |sum_j sigma_j y_l(j) + eps delta_l H_l| >= g_l > 0 for all sigma in {-1,0,1}^{supp y_l}, eps = +-1, and Phi_l <= g_l 2^{-l}.
(FD)    every block has infinitely many carriers l with a coordinate j_l notin union S_i owned by l and
        |y_l(j_l)| > (1 + max_i s_i)(||y_l||_1 - |y_l(j_l)| + delta_l H_l).
**Lemma 2.1 (designability).  PROVED.**  Every SLD-type design can be modified to satisfy all of the above without affecting
admissibility, N-independence, or any theorem of Section 8 of the note or of Rounds 5-6.
*Proof.*  (SF*), (SF_tau), (b'): at stage l the weight c_l is chosen last, after y_l, delta_l, S_l and all earlier data; each condition is an
upper bound on c_l (or on later weights in terms of level-l data) by an explicit positive number computable at that stage (finitely
many pairs (l', s) in (b')); replace c_l by the minimum.  Window theorems use weights only through upper bounds on fine weights (box
bounds, (P2)) and through c_{l+1} <= c_l/4; smaller weights preserve both.  delta_l depends only on S_l and U.  (Z0), (FD): choose the S_l
inside N \ Z_0 with Z_0 infinite, and add y*, y** and, at infinitely many stages and for every block, targets (e_j^* + r)/q*(e_j^* + r) with j
in Z_0 fresh and r tiny; allowedness holds (supports avoid signature sets) and the family stays dense.  (GM): at stage l the values
sum_j sigma_j y_l(j) form a finite set; delta_l ranges over (0, delta^max_l]; exclude the finitely many intervals of length 2 g_l/H_l where
|sum sigma y + eps delta_l H_l| < g_l, with g_l so small that they cover less than delta^max_l/2; then choose c_l with Phi_l <= g_l 2^{-l}.  QED

## 4. Realizability: (B), (C), (D) occur for every design (part 2)
**Construction SA(m_0, eta).**  Design with (SF*), (Z0); a block m_0 and a carrier l_- of block m_0 with y_{l_-} = y*; eta > 0.
 (1) F := {p, p'}, a := (a_p e_p + a_{p'} e_{p'})/(a_p + a_{p'} + nu), a_p, a_{p'} > 0 to be chosen; so zhat_p = 1 + s_p^2 a_p/nu, zhat_{p'} = 1 +
     s_{p'}^2 a_{p'}/nu (scale invariant).
 (2) Owner recursion over l = 1, 2, ... (all blocks); "assigned" coordinates: initially F.  At step l let A_l := sum_{j in supp y_l assigned}
     y_l(j) zhat_j and B_l := sum_{j in supp y_l unassigned} |y_l(j)|.  If l != l_-: eps_l := sgn A_l (+1 if A_l = 0), z_j := eps_l sgn y_l(j) at the
     unassigned j in supp y_l, z := eps_l on S_l.  If l = l_-: eps_{l_-} := +1, z := +1 on S_{l_-}.  Never assigned coordinates: z := 0 (by Lemma
     1.2 there are none).  By allowedness (a), S_l is unassigned at step l (F ⊂ Z_0), so the recursion is well defined and gives admissible
     forced data of a unique first row f_SA.
**Theorem 2.2 (self-aligned rows).  PROVED** (design with (SF*), (Z0); diagonal U; any N).  There are a_p, a_{p'} > 0 such that f_SA has:
 (a) every carrier l is swallowed with sign eps_l (F ∩ S_l = {}), and for l != l_-: n_l val_l = A_l + eps_l (B_l + delta_l H_l), so sgn val_l = eps_l
     and |val_l| >= delta°_l;
 (b) every l != l_- is a non-degenerate swallowing-type peak (varsigma_l = eps_l); beyond the first carrier of its block nu_l >= 2^{10} theta_m and
     mu_l >= q_0 delta°_l/2;
 (c) n_{l_-} val_{l_-} = -eta; if eta < n_{l_-} theta_0 Phi_{l_-}/(2 m_0) (theta_0 := lambda_{l_c} delta°_{l_c}/2, l_c the first carrier of block m_0
     other than l_-), then l_- is a strict non-peak with gap >= M/2 and q_{l_-} < 0, and u_{l_-} 1_{F^c} = v_{l_-} is z-signed;
 (d) W := sum_l lambda_l eps_l u_l 1_{F^c} (all carriers, all blocks) satisfies: for every j notin F with W(j) != 0, j is a contact and z_j W(j) > 0;
     the same holds for every partial sum W^(L) := sum_{l <= L} lambda_l eps_l u_l 1_{F^c} and every sum_l rho_l lambda_l eps_l u_l 1_{F^c} with rho_l in [1/2, 1];
 (e) block m_0 is in configuration (C) with EXACT coherence: (H2'') UPPER fails and c_*(l) = 0 for every l >= l_-;
 (f) every block satisfies Scr_m(Upsilon s) = o(s) as s -> 0 for every Upsilon (so (SC));
 (g) no free coordinate in any carrier support, no degenerate peak, one strict non-peak.
*Proof.*  Step 1 (tuning).  supp y* = F, so n_{l_-} val_{l_-} = y*(zhat_F) + delta_{l_-} H_{l_-}, independent of the recursion, and y*(zhat_F) =
c*(s_p^2 a_p - s_{p'}^2 a_{p'})/nu (c* := 1/q*(e_p^* - e_{p'}^*)) runs continuously over (-c* s_{p'}, c* s_p) as a_p/a_{p'} runs over (0, infinity).
Take l_- late enough that delta_{l_-} H_{l_-} + eta < c* s_{p'} (infinitely many carriers of block m_0 have target y* by density) and choose the
ratio by the intermediate value theorem.  Step 2 ((a)).  New coordinates satisfy z_j y_l(j) = eps_l |y_l(j)|, z = eps_l on S_l, S_l ∩ F = {}; Lemma 1.1.
Step 3 (theta lower bound).  A(th) >= ||zeta||_1 - th ||Phi_m||_2^2 >= ||zeta||_1 - th/4, B(th) <= th sum Phi_k^2 nu_k = th ||zeta||_1; at th = ||zeta||_1/2,
Psi >= (49/64 - 1/2)||zeta||_1^2 > 0, so theta_m > ||zeta||_1/2 >= lambda_{l_c}|val_{l_c}|/2 >= theta_0.  Step 4 ((b)).  For l != l_- in block m put
th := nu_l.  Coarser carriers k of block m: (|zeta(k)| - th Phi_k^2)_+ = m Phi_k (|val_k| - |val_l| Phi_k/Phi_l)_+ = 0, since |val_k| <= 1 + ||U|| and
Phi_l/Phi_k <= c_l/c_{l-1} <= delta_l 2^{-min S_l - l - 10}/(1 + ||U||) <= |val_l| 2^{-l-9}/(1 + ||U||).  Finer carriers contribute <= (1 + ||U||)
sum_{l''>l} lambda_{l''} <= 2^{-10} lambda_l |val_l|.  So A(nu_l) <= 2^{-10} m |val_l| < m|val_l| = (B(nu_l))^{1/2}: Psi(nu_l) < 0, theta_m < nu_l.  If
l_1 is the first carrier of block m, theta_m < nu_{l_1} <= m(1 + ||U||)/Phi_{l_1}, and for later l (SF*) gives nu_l >= 2^{10} m (1 + ||U||)/Phi_{l_1} >
2^{10} theta_m, so mu_l >= q_0 |val_l| (1 - 2^{-10}) >= q_0 delta°_l/2.  Step 5 ((c)).  nu_{l_-} = m_0 eta/(n_{l_-} Phi_{l_-}) < theta_0/2: strict
non-peak, gap >= C theta/(2|zeta|) = M/2; w(k(l_-)) has the sign of val_{l_-} < 0 = -eps_{l_-}, so q_{l_-} < 0; u_{l_-} 1_{F^c} = v_{l_-} lives on S_{l_-}
where z = +1.  Step 6 ((d), dominance).  Let j notin F, W(j) != 0, o = o(j).  If j in S_o: z_j = eps_o, and the later terms total at most
(4/3) 2^{-6 - min S_o} lambda_o v_o(j) <= 2^{-5} lambda_o v_o(j) for j <= m(o) + k(o) + 4 ((SF*): later total <= (4/3) sum_{l'' > o} lambda_{l''}), and at
most 2^{-6} lambda_o v_o(j) for larger j (allowedness (b): each later l'' with j in supp y_{l''} has lambda_{l''} <= c_{l''}/4 <= 2^{-2j} c_o delta_o/8, total <= 2^{-2j} c_o delta_o/6).  If j
notin S_o, j was unassigned at step o, z_j = eps_o sgn y_o(j), and |lambda_o y_o(j)/n_o| >= lambda_o eta_o/n_o >= 2^9 (4/3) sum_{l''>o} lambda_{l''}.  In
both cases sgn W(j) = sgn(eps_o u_o(j)) = z_j, |z_j| = 1.  Partial sums W^(L) contain the owner's term whenever they contain j; weights in
[1/2, 1] change the ratios by a factor <= 2.  Step 7 ((e)).  All peaks of block m_0 are swallowing-type, no good carrier, l_- is swallowed with
q < 0: UPPER fails (Z4-ref Remark 3.3).  With delta_{m_0} = 1, P* = robust coarse peaks of block m_0, Bfree = the other swallowed carriers <= l and
x_{l'} := lambda_{l'}, the vector sum_m delta_m Pi_m + sum x eps u is W^(l) restricted to carriers <= l, z-signed without free coordinates by (d):
c(1; l) = 0.  Step 8 ((f)).  Rates: peaks after the first carrier of their block have mu_l >= q_0 delta°_l/2; finitely many other carriers have fixed
positive rates.  For small s only carriers with q_0 delta°_l/2 <= Upsilon s contribute, and by the second half of (SF*) they have Phi_l <= c_{l-1}
delta°_l 2^{-l} <= c_{l-1} 2^{1-l} Upsilon s/q_0, total <= 2 Phi_{l(s)} = o(s) (l(s) -> infinity).  Step 9 ((g)): by construction.  QED
**Remarks 2.3.**  (1) (D) aligned corner (N = 1) with a WEAK peak.  PROVED.  With F = {p, p', p'', p'''} and a second exceptional carrier l_D
with target y**, eps_{l_D} := sgn val_{l_D}, the ratio a_{p''}/a_{p'''} moves val_{l_D} continuously; theta jumps only when an owner-rule sign
eps_l switches (A_l crossing 0), coarse switches are finitely many in a small range and fine ones move theta by <= C sum_{l > L} lambda_l;
hence every relative margin xi in (0, xi_0) is attained up to an arbitrarily small error: a swallowing-type peak with arbitrarily small
margin, all other carriers swallowing-type robust peaks, l_- with q < 0, no anti-sign swallowed peak, no good carrier; l_D is the only
raisable carrier (D-ii)-(D-iv); (D-v): every contact is owned by a carrier whose term dominates there, so an inward z-move lowers the
owner's |val| at first order and lowers theta; free coordinates carry no carrier.  EXACT degeneracy in this pure self-aligned form: OPEN
(the jumps may skip the degenerate value; at FIXED z exact degeneracy is easy, Proposition 5.1(c), but then the configuration is not pure).
(2) (B) core.  SKETCH.  Two blocks, tuned strict non-peaks l_1, l_2 (one per block) whose targets share a coordinate j in Z_0 \ F with z_j := 0
(free) and all other target coordinates in F: the cone row L_j(tau) = 0 couples tau_{l_1}, tau_{l_2}; two such rays give a 2 x 2 d-matrix with
prescribed tiny determinant.  (3) None of (C), (D) needs infinitely many tunings; genericity of targets or masses, private coordinates
or disjoint coordinate sets of blocks leave Construction SA intact.
**Proposition 2.4 (single-vector principle).  PROVED.**  For any admissible T, finite F, a with supp a = F, and vectors V_i in l_1 such that
every j notin F has an index i(j) with |V_{i(j)}(j)| > 2 sum_{i > i(j)} |V_i(j)|, the choice z_j := sgn V_{i(j)}(j) makes every partial sum
sum_{i <= n} V_i containing the dominant index z-signed off F.  (As Step 6.)  A design can defeat one z-signing only by destroying dominance.
**Remark 2.5 (designs violating (SF*)).  HEURISTIC.**  Slower weights create "sign gadgets" (a later target with two dominant entries in two
earlier signature sets relates the two peak signs; odd cycles conflict), but the conflict coordinates are target coordinates where the row
chooses z freely and the earlier carrier counts as swallowed on S^nat; I do not see a design that excludes (C) through targets or weights.

## 5. Near-threshold carriers are generic (part 5.2)
**Proposition 5.1.  PROVED.**  Let T be ANY admissible operator, U diagonal, m a block, F finite with d := |F| >= 2, sigma in {-1,1}^F, z in
B_{l_infty} with z = sigma on F and infinitely many contacts, A := {a : supp a = F, sgn a = sigma, q*(a) = 1}, and (eps_l) any positive
sequence.  Then {a in A : |nu_l(f_a) - theta_m(f_a)| < eps_l for infinitely many carriers l of block m} is a dense G_delta in A; in particular
f_a is not (BT) for a dense G_delta set of a.
*Proof.*  (1) b(a) := (s_j a_j)_{j in F}/||(s_i a_i)||_2 maps A homeomorphically onto the open orthant Omega of S^{d-1} with signs sigma, and
zhat_j = sigma_j + s_j b_j on F.  For y in l_1, y(zhat) = sum_{j notin F} y_j z_j + sum_{j in F} y_j (sigma_j + s_j b_j) =: psi_y(b) (affine in b); val_l =
psi_{u_l}; zeta_m(b) is l_1-continuous (sum_k lambda_k |val_k(b) - val_k(b')| <= sum lambda_k ||U|| ||e(b) - e(b')||), so theta_m(b) is continuous,
positive, locally bounded.  (2) Fix L, b_0 in Omega and a connected open neighbourhood O of b_0 with compact closure in Omega.  Choose n in
R^F with (n_j s_j)_j not parallel to b_0 (d >= 2), c := -sum_{j in F} n_j(sigma_j + s_j b_{0,j}), a contact j_1 notin F, r := c z_{j_1} e_{j_1}, y :=
(n + r)/q*(n + r): psi_y(b_0) = 0 and psi_y has non-zero differential on the sphere at b_0, so psi_y(b_+-) = +-c_0 for some b_+- in O, c_0 > 0.
By (T-d) there are carriers l_i -> infinity of block m with q*(u_{l_i} - y) -> 0, and sup_b |val_{l_i}(b) - psi_y(b)| <= ||u_{l_i} - y||_1 +
||U^*(u_{l_i} - y)|| <= q*(u_{l_i} - y).  For i large, val_{l_i}(b_+-) has sign +- and modulus >= c_0/2; G_i := nu_{l_i} - theta_m = m|val_{l_i}|/Phi_{l_i} -
theta_m is continuous on O with G_i(b_+) >= m c_0/(2 Phi_{l_i}) - sup_O theta_m > 0, and G_i = -theta_m < 0 at a zero of val_{l_i} on a path from b_+
to b_-.  So G_i vanishes somewhere in O and {b in O : |G_i| < eps_{l_i}} is non-empty and open: V_L := union_{l >= L} {|nu_l - theta_m| < eps_l} is
open dense.  (3) Omega is Baire; take intersection_L V_L.  Infinitely many carriers with |nu - theta| < eps_l are infinitely many strict
non-peaks (Q_m infinite) or peaks with mu_l < q_0 Phi_l eps_l/m, which violate (MS) for eps_l := (Phi_{l+1}/Phi_l)^2.  QED
**Consequences.**  (a) The design question (GO) (can the design ensure finitely many near-threshold carriers tuned through F?) has a
NEGATIVE answer for every admissible design.  (b) (BT) is meagre in every fixed-z fibre, although dense (Proposition 5.3).  (c) Exactly
degenerate peaks tuned through F are dense in every fixed-z fibre ({nu_l = theta_m} is non-empty in every open set).  (d) Owner-rule rows
escape Proposition 5.1 because their z depends on a.

## 6. (E): lacunary signature profiles (part 2.5)
**Lemma 2.6.  PROVED.**  Let beta_i > 0 with beta_{i+1}/beta_i -> 0, x_i in (0, infinity] arbitrary, m(x) := sum{beta_i : x_i < x}.  Then NOT
(0 < liminf_{x->0} m(x)/x <= limsup_{x->0} m(x)/x < infinity).  Hence a design whose signature profiles satisfy v_l(s_{i+1})/v_l(s_i) -> 0 (s_i the
i-th element of S_l) admits no first row with a critical flip profile (x_i := |a_{s_i}|/v_l(s_i), x_i := infinity for s_i notin F).
*Proof.*  Suppose c <= m(x)/x <= C on (0, x_0].  (i) If x_k < x_0 then beta_k <= m(x) <= Cx for x in (x_k, x_0], so beta_k <= C x_k.  (x_k = 0 is
impossible: it would give m(x) >= beta_k for all x > 0.)  (ii) Fix k_0 with beta_{k+1} <= beta_k/2 for k >= k_0, x_* := min{x_k : k < k_0}; choose i >= k_0
with beta_{i+1} <= c beta_i/(8C) and x := beta_i/(2C) < min(x_0, x_*).  Every k counted in m(x) has k >= k_0 and beta_k <= C x_k < Cx = beta_i/2, so
k > i; hence m(x) <= sum_{k > i} beta_k <= 2 beta_{i+1} <= c beta_i/(4C) = cx/2 < cx.  Contradiction.  QED
**Price.  HEURISTIC.**  Exact two-sided tuning by pulls (Y4-ref Prop. P4) needs pull sizes within a bounded factor of any prescribed eta
(bounded gaps (G)); lacunary profiles provide them only on a lacunary set; hybrid profiles restore pulls but also critical profiles on
the geometric part.  Lemma 2.6 removes critical profiles, not mixed ones (liminf m/x = 0, limsup m/x = infinity), which lacunary designs
allow; mixed profiles need window selection at the sparse scales (Y3 liminf-sparsity extension, SKETCH).

## 7. The dangerous instances are recovered (part 3.1-3.2)
**Corollary 3.1.  PROVED.**  (a) f_SA (Theorem 2.2) satisfies (BT), hence f_SA in Rec.  (b) The weak-peak aligned corner of Remark 2.3(1)
satisfies (BT).  (c) The same holds for every finitely-tuned variant (finitely many exceptional carriers tuned through F), in particular
for the (B) core of Remark 2.3(2).  So (B), (C), (D) as such are not obstructions; a counterexample inside them must violate (BT).
*Proof.*  F finite; Q_m finite (Theorem 2.2(b), (c)); no degenerate peak; (MS) by Step 8 of Theorem 2.2 (the weak peak has a fixed positive
margin).  Corollary cor:BTrecovered.  QED
**Proposition 3.2 (explicit coherent-shift mates).  PROVED.**  N = 1, f = f_SA, k_- := k(l_-), zeta^ := R^** zhat, Delta_alpha > 0, chi in [0, 1]:
   omega^+ := alpha e_{k_-},  omega^- := (alpha + Delta_alpha) e_{k_-},  V := u_{l_-} - (val_{l_-}/|zeta^|) R^* w.
(i) Delta d = Delta_alpha lambda_{l_-} val_{l_-}/|zeta^| < 0.  (ii) V 1_{F^c} is z-signed and supported in K.  (iii) b^+ := chi Delta_alpha lambda_{l_-} V 1_{F^c} +
beta^+, b^- := b^+ - Delta_alpha lambda_{l_-} V (beta^+ supported in F with b^+(xi) = 0) are two-piece data with Delta d < 0 for g := b^+ + R^*(omega^+ -
d(omega^+) w).  (iv) c g in C(f) for all small c > 0, and every such mate is recovered.
*Proof.*  (i) d(omega) = <Dw, D omega>/C and Phi_k^2 w(k)/C = zeta(k)/|zeta| off P (Lemma lem:threshold), so Delta d = Delta_alpha zeta^(k_-)/|zeta^|, and
val_{l_-} = -eta/n < 0.  (ii) R^* w = M sum_{k != k_-} lambda_k eps_k u_k + lambda_{l_-} w(k_-) u_{l_-} (all other carriers are swallowing-type peaks).
So V 1_{F^c} = c_1 v_{l_-} + c_2 (W - lambda_{l_-} eps_{l_-} u_{l_-}) 1_{F^c} with c_2 = eta M/(n |zeta^|) > 0 and c_1 = 1 - C m^2 val_{l_-}^2/|zeta^|^2 in (0, 1].
Off S_{l_-}, V = c_2 W (Theorem 2.2(d)); on S_{l_-} (z = +1), V(s) >= (c_1 - 2^{-5} c_2 lambda_{l_-}) v_{l_-}(s) > 0 (Step 6; c_1 is close to 1 and c_2 lambda_{l_-} is tiny).  (iii) b^+ - b^- = Delta_alpha
lambda_{l_-} V = R^*(omega^- - omega^+) - Delta d R^* w (R^* e_{k_-} = lambda_{l_-} u_{l_-}), so both pairs represent g; off F, b^+ is z-signed and b^- =
-(1 - chi) Delta_alpha lambda_{l_-} V is (-z)-signed, both supported in K; omega^+- supported in Q = {k_-}.  (iv) Proposition prop:onesidedupper on both
sides gives p*(f + r g) <= 1 + (r^2/2)(kappa_w + o(1)); for small c this yields p*(f + t c g) <= s(t) for |tc| <= r_0, and p*(f + tcg) <= 1 + |t| c p*(g)
<= s(t) for |tc| >= r_0 (s(t) - 1 >= min(t^2, |t|)/3).  (SC) holds (Theorem 2.2(f)); Theorem thm:engineered.  QED
These mates switch through the swallowed q < 0 carrier and carry the uniform shift through ALL peaks (the term -Delta d R^* w) at every
scale: exactly the coherent shift that the window method cannot follow (Y2 5.3(c)).  Numerics (sa_check.py, N = 1, 9 carriers): all
l != l_- peaks with sign eps, l_- non-peak (nu/theta = 0.24), q_- < 0, N(w) = 1, SOCP block norm = A(theta) (rel. err. 6e-9), W and V z-signed
(72 coordinates), Delta d = -5.9e-30 < 0, identity residual 4e-47.

## 8. Tools (parts 3, 4, 5)
**Lemma 3.3.  PROVED.**  If F is finite and (b^+-, omega^+-) are two-piece data at f, then D := b^+ - b^- = sum_m R_m^*(omega^-_m - omega^+_m) -
sum_m Delta d_m R_m^* w_m vanishes at every free coordinate and z_j D(j) >= 0 at every contact.  (b^+- vanish off F ∪ K, b^+ is z-signed and b^- is
(-z)-signed on K.)
**Lemma 3.4 ((GM) consequence).  PROVED.**  Under (GM), if f has F finite and theta_m <= Theta, then every swallowed carrier l of block m with
S_l ∩ F = {} and all target coordinates contacts satisfies |n_l val_l| >= g_l, hence nu_l >= (4/5) m 2^l, so for l > log_2(2 Theta) + 1 it is a
peak with huge relative margin: near-threshold swallowed carriers beyond an f-dependent level have a target coordinate in F ∪ J.
(Lemma 1.1 with z_j in {-1, 1}; Phi_l <= g_l 2^{-l}.)
**Lemma 5.2 (threshold Lipschitz, strictly monotone in peak masses).  PROVED.**  For zeta^0 with a peak k_1 (nu_{k_1} > theta(zeta^0)) there
are r > 0, 0 < c_Theta <= L_Theta with: (a) |theta(zeta) - theta(zeta')| <= L_Theta ||zeta - zeta'||_1 on B(zeta^0, r); (b) if k is a peak of zeta and
|zeta'(k)| = |zeta(k)| + t, zeta' = zeta elsewhere, then theta(zeta') - theta(zeta) >= c_Theta t.
*Proof.*  |A(th; zeta) - A(th; zeta')| <= ||zeta - zeta'||_1 and |B(th; zeta) - B(th; zeta')| <= 2 th ||zeta - zeta'||_1 (d/d|zeta(k)| of Phi_k^2 min(th,
nu_k)^2 is 2 nu_k <= 2 th or 0), so |Psi(th; zeta) - Psi(th; zeta')| <= (A + A' + 2 th)||zeta - zeta'||_1.  One-sided th-derivatives: -2(A + th)||Phi||_2^2 <=
dPsi/dth <= -2(A + th) Phi_{k_1}^2 while nu_{k_1} > th.  On a small ball, theta, A are bounded above and below.  (a): Psi(theta(zeta) + h; zeta') < 0 for h >
(A + A' + 2 th)||zeta - zeta'||_1/(2(A + th) Phi_{k_1}^2), and symmetrically.  (b): Psi(theta(zeta); zeta') = (A + t)^2 - B >= 2At and Psi(theta(zeta) + h;
zeta') >= 2At - 2(A' + th)||Phi||_2^2 h > 0 for h < At/((A' + th)||Phi||_2^2).  QED
**Theorem 3.5 (fine re-alignment).  PROVED** (design with (SF*), diagonal U, any N).  Let F be finite and L >= 1.  z^(L) := z on F and on
every coordinate in the support of a carrier l <= L; on the other coordinates by the owner recursion of Construction SA over the carriers
l > L.  f^(L) := the row with data (a, z^(L)).  (a) p*(f^(L) - f) <= C_f sum_{l > L} lambda_l log(e/sum_{l > L} lambda_l) (Z3 Lemma 3.1: u_k(z^(L) - z)
= 0 for k <= L, |u_k(z^(L) - z)| <= 2 for k > L).  (b) Carriers l <= L keep their values; every carrier l > L with S_l ∩ F = {} is an exactly
swallowed non-degenerate swallowing-type peak, with margin >= q_0 delta°_l/2 beyond the first peak of its block (Theorem 2.2 Steps 2, 4: they
use only the owner rule at l, |val_k| <= 1 + ||U|| and (SF*); coarse supports are untouched, and by allowedness (a) no coarse target meets a
fine signature set).  (c) = Proposition 5.3.
**Proposition 5.3 (block-tame approximants without degenerate peaks).  PROVED.**  Let K_0 be the finite set of carriers l <= L or with
S_l ∩ F != {}.  For every l_0 there is a row f^(L)_* with the same a, z^(L)_* = z^(L) except at coordinates owned by carriers >= l_0, with no
degenerate peak and (BT), and p*(f^(L)_* - f^(L)) <= C_f sum_{l >= l_0} lambda_l log(e/sum_{l >= l_0} lambda_l).  Hence (BT) points are dense in
{f : F finite}, and Lemma Z holds at f as soon as dist(rho g, C(f^(L)_*)) -> 0 along some sequence (Cor. cor:BTrecovered).
*Proof.*  HYSTERETIC RE-RUN: after modifying coordinates owned by carriers >= l_a, re-run the owner recursion from l_a with reference
signs eps^(L): keep eps_l := eps^(L)_l unless eps^(L)_l A_l <= -(B_l + delta_l H_l)/2 (forced flip: eps_l := sgn A_l).  Every re-run carrier then has
n_l |val_l| >= (B_l + delta_l H_l)/2 with sign eps_l, hence is a robust peak with margin >= q_0 delta°_l/4 (Step 4 with |val_l| >= delta°_l/2); carriers
< l_a are untouched (supp u_k consists of coordinates owned by carriers <= k).  LEVERS: for each block m choose l_a(m) of block m, l_0 <=
l_a(1) < ... < l_a(N), all > max K_0, s_m := min S_{l_a(m)}, and replace z_{s_m} = eps_{l_a(m)} by t_m eps_{l_a(m)}, t_m in [3/4, 1]: |val_{l_a(m)}|
decreases at the exact rate delta_{l_a} 2^{-s_m}/n_{l_a} in 1 - t_m and stays >= (3/4) delta°_{l_a}; only carriers > l_a(m) change otherwise.
CHOICE OF t_1 (t_2 = ... = t_N = 1): zeta_1(t) = zeta_1^fix + own lever term + zeta_1^later(t) with ||zeta_1^later(t) - zeta_1^later(1)||_1 <= e_1 :=
2(1 + ||U||) sum_{l > l_a(1)} lambda_l.  With phi(t) := theta(zeta_1^fix + own term + zeta_1^later(1)), Lemma 5.2 gives |phi(t) - phi(t')| >= c_Theta
lambda_{l_a} delta_{l_a} 2^{-s_1}|t - t'|/n_{l_a} and |theta_1(t) - phi(t)| <= L_Theta e_1.  The nu_k, k in K_0, are fixed, so {t : theta_1(t) = nu_k} lies in an
interval of length <= 2 L_Theta e_1 n_{l_a}/(c_Theta lambda_{l_a} delta_{l_a} 2^{-s_1}) <= L_Theta 2^{-8-k(l_a(1))}/c_Theta by (SF*) (min S_{l_a} = s_1).  For
l_a(1) large these |K_0| intervals cover less than 1/4 of [3/4, 1]; pick t_1 outside, dgap_1 := min_{K_0} |theta_1 - nu_k| > 0.  Choose l_a(2)
with 2 L_Theta (1 + ||U||) sum_{l >= l_a(2)} lambda_l < dgap_1/2, then t_2 likewise, and so on.  Then no carrier of K_0 is degenerate, all others
are robust peaks, Q_m ⊂ K_0, (MS) holds (Step 8 with margins >= q_0 delta°/4): (BT).  Cost: Z3 Lemma 3.1 with Delta_m <= 2 sum_{l >= l_0} lambda_l.  QED
(The levers create N free coordinates; Lemma 5.5 gives a contact-preserving variant.)
**Lemma 3.6 (transplant).  PROVED.**  Let f, f^# have the same F (or F^# = F ∪ B with bank coordinates B, treated as contacts below), let
(b^+-, omega^+-) be two-piece data at f for g with Delta d_m <= 0, and assume (T1) every k in supp omega^+-_m is a strict non-peak of f^#; (T2)
D^# := sum_m R_m^*(omega^-_m - omega^+_m) - sum_m Delta d^#_m R_m^* w^#_m (Delta d^#_m := d^#_m(omega^-_m) - d^#_m(omega^+_m)) is z^#-signed off F and vanishes at
the free coordinates of f^#.  Then there are two-piece data (b^+-_#, omega^+-) at f^# for G^# := b^+_# + sum_m R_m^*(omega^+_m - d^#_m(omega^+_m) w^#_m), with
   ||b^+-_# - b^+-||_1 <= C(||D^# - D||_1 + 2||D 1_Fl||_1 + 2||D^# 1_Fl||_1) + C|b^+_#(xi^#) - b^+(xi)|,
D := b^+ - b^-, Fl := {j : z^#_j z_j = -1}; Delta d^#_m -> Delta d_m and ||G^# - g|| -> 0 as f^# -> f.
*Proof.*  Off F, at each j with D^#(j) != 0 (a contact or bank coordinate of f^#), write D^#(j) = z^#_j s_j, s_j > 0, and split b^+_#(j) := z^#_j x_j,
b^-_#(j) := -z^#_j y_j, x_j + y_j = s_j, x_j, y_j >= 0, choosing (x_j, y_j) nearest to (z^#_j b^+(j), -z^#_j b^-(j)) (both >= 0 when z^#_j = z_j); the
distance is <= |D^#(j) - D(j)| when z^#_j = z_j and <= |D(j)| + |D^#(j)| at flips.  Off supp D^#: b^+-_# := 0.  On F keep b^+ and set b^-_# := b^+_# - D^#;
rebalance with multiples of a (b(xi^#) = 0).  Then b^+_# - b^-_# = D^#, so (b^-_#, omega^-) represents G^# (as in Proposition 3.2(iii)).  Z3 Lemma
3.1 gives sum_m ||R_m^*(w^#_m - w_m)||_1 -> 0 and d^# -> d on the fixed finite supports.  QED
**Theorem 3.7 (negative d-mismatch through (SC)-companions).  PROVED.**  Let F be finite and g in C(f) carry two-piece data with Delta d <= 0,
kappa_w <= 1.  Suppose there are rows f_i -> f with supp a_i = F (or F ∪ B_i, banks) satisfying (T1), (T2) and (SC) for the blocks with
Delta d^#_m < 0, with transplant cost -> 0.  Then (f, g) in cl NA((c_0, p), l_2^2).
*Proof.*  Fix rho < 1.  The transplanted data represent G_i -> g with kappa^(i)_w -> kappa_w.  Z3 Lemma U (with banked support: Y4-ref
Lemma P2, data contact-like on B_i) gives r_1 > 0 and i_0 with p*(f_i + r G_i) <= 1 + (r^2/2)(kappa_w + eps) for |r| <= r_1, i >= i_0.  Hence, for
rho^2(kappa_w + 2 eps) <= 1 - r_1^2/4, p*(f_i + r rho G_i) <= s(r) for |r| <= r_1, and for |r| >= r_1, p*(f_i + r rho G_i) <= s(rho r) + p*(f_i - f) +
|r| rho p*(G_i - g) <= s(r) for i large (s(r) - s(rho r) >= c(rho, r_1) min(r^2, |r|)).  So rho G_i in C(f_i) with kappa_w(rho G_i) <= 1 and Delta d <= 0; (SC)
at f_i; Theorem thm:engineered gives (f_i, rho G_i) in cl NA.  Let i -> infinity, then rho -> 1.  QED
**Lemma 3.8 ((SC) from a generic threshold).  PROVED.**  Fix a block m with eps_k := (Phi_m(k+1)/Phi_m(k))^{1/2} summable and kappa > 0 a lower
bound of q_0/m and C_m/|zeta|.  If block m has no degenerate peak and theta_m notin limsup_k [nu_k - eps_k/kappa, nu_k + eps_k/kappa], then (SC)
holds for {m} along s_L := (Phi_m(L) Phi_m(L+1))^{1/2}/Upsilon.  If, along a one-parameter family, theta_m is C^1 with |theta_m'| >= v_0 > 0 and
each nu_k is either constant or C^1 with |(nu_k - theta_m)'| >= v_k > 0, sum_k eps_k/v_k < infinity, then (SC) holds for {m} for Lebesgue-a.e.
parameter value at which there is no degenerate peak.
*Proof.*  A carrier with Phi_k > Upsilon s_L contributes to Scr_m(Upsilon s_L) only if Phi_k |nu_k - theta| kappa <= Upsilon s_L, i.e. |nu_k - theta| <=
eps_L/kappa (k <= L); carriers with Phi_k <= Upsilon s_L contribute <= 2 Phi_{L+1} = o(s_L).  Under the hypothesis no k <= L has |nu_k - theta| <=
eps_L/kappa for L large.  Family: {t : |nu_k(t) - theta(t)| <= eps_k/kappa} has measure <= 2 eps_k/(kappa v_k) (moving nu_k) or <= 2 eps_k/(kappa v_0)
(constant nu_k); Borel-Cantelli.  QED

## 9. Rigidity of exact data (parts 4, 5.4)
For two-piece data write D = b^+ - b^- = sum_k gamma_k u_k, gamma_k := lambda_k [(omega^-_m - omega^+_m)(k) - Delta d_m w_m(k)] (m = m(k)); K_omega := carriers
in supp omega^+- (finite); E := union_{k in K_omega} supp y_k \ F (finite); C_1 := max_m |Delta d_m|.  Carrier k is NEUTRAL if gamma_k = 0, NEGLIGIBLE if
0 < |gamma_k| < 2 tau_k C_1 lambda_k.  (gamma_k is the d-row coefficient; c_k always denotes the design weight.)
**Lemma 4.1' (dominance with design thresholds).  PROVED** (design with (SF_tau), (b')).  Let j notin F, o = o(j), and |gamma_k| <= C_1 lambda_k for
every k > o with u_k(j) != 0.  If |gamma_o| >= tau_o C_1 lambda_o, then sgn D(j) = sgn(gamma_o u_o(j)) and |D(j)| >= (31/32)|gamma_o u_o(j)|.
*Proof.*  Later carriers k at j have j in supp y_k \ S_k, |u_k(j)| <= 4/3.  (i) j in S_o, j <= m(o) + k(o) + 4: later total <= (4/3) C_1 sum_{k>o}
lambda_k <= (4/3) 2^{-10} tau_o C_1 lambda_o delta_o 2^{-(m + k + min S_o)}/n_o, leading >= tau_o C_1 lambda_o delta_o 2^{-j}/n_o, ratio <= 2^{-5}.  (ii) j in
S_o, j > m(o) + k(o) + 4: by (b') each later k has design weight c_k <= tau_o 2^{-2j} c_o delta_o/2; with c_{k+1} <= c_k/4 and lambda_k <= c_k/2 the later total is
<= (4/9) C_1 tau_o 2^{-2j} c_o delta_o, the leading term >= (4/5) tau_o C_1 2^{-m-k} c_o delta_o 2^{-j} (c_o the design weight of o); ratio <= (5/9) 2^{m + k - j} < 2^{-5}.  (iii) j in
supp y_o \ S_o: later total <= (4/3) C_1 sum_{k > o} lambda_k <= 2^{-9} tau_o C_1 lambda_o eta_o/n_o <= 2^{-9}|gamma_o u_o(j)|.  QED
(Part 4's Lemma 4.1, with threshold 2^{-3} C_0 lambda and C_0 = max|omega| + 2 max|Delta d|, is correct but makes every carrier not carrying
omega "negligible" when |Delta d| << |omega|, the typical case; Lemma 4.1' is the useful form.)
**Proposition 4.2' (exact data force owner alignment).  PROVED** (design with (SF_tau), (b'); F finite; C_1 > 0).  For every j notin F ∪ E
whose owner o is neither neutral nor negligible: D(j) != 0, j is a contact and z_j = sgn(gamma_o u_o(j)); for o notin K_omega,
   z_j = -sgn(Delta d_{m(o)}) sgn(val_o) sgn(u_o(j)).
*Proof.*  If o notin K_omega, a K_omega-carrier at j would have j in S_k (j notin E), hence be the owner; so all carriers at j are outside
K_omega and |gamma_k| = lambda_k |Delta d_m||w(k)| <= C_1 lambda_k (|w| <= M <= 1); if o in K_omega (j in S_o \ E) the later carriers are again outside
K_omega.  Lemma 4.1' and Lemma 3.3; sgn w(k) = sgn zeta(k) = sgn val_k.  QED
Reading (N = 1).  k notin K_omega is neutral iff val_k = 0, negligible iff k is a strict non-peak with 0 < |val_k| < 2 tau_k theta Phi_k/(m M) (nearly
neutral: within a design-tiny fraction of the threshold scale).  Exact data with Delta d < 0 force OWNER ALIGNMENT z_j = sgn(val_o) sgn(u_o(j))
outside F, E and the coordinates owned by K_omega-, neutral or negligible carriers ("dead zones"); in particular no free coordinate is owned
by a non-neutral, non-negligible carrier outside K_omega.
**Perturbing a with z fixed.  FALSE as a (T2)-preserving companion.**  By density (T-d) every block has infinitely many F-dependent carriers
with values tending to 0; perturbing a by p != 0 moves infinitely many of them across 0, their coefficients c_k change sign while z on their
signature sets is fixed, and D^# fails to be z-signed there (Lemma 4.1').  Repair: re-align with hysteresis.
**Lemma 4.4 (perturb-and-realign).  PROVED** for rows built by the owner rule from some level K on, with finitely many exceptional
carriers below K.  Let a(p) be a smooth family in A (supp a = F, signs fixed, q*(a) = 1), a(0) = a; f^p: re-run the owner recursion from K with
a(p), keeping eps_l(p) := eps_l(0) unless eps_l(0) A_l(p) <= -(B_l + delta_l H_l)/2, in which case eps_l(p) := sgn A_l(p).  Then (a) every re-run carrier
has n_l|val_l(p)| >= (B_l + delta_l H_l)/2 with sign eps_l(p); a forced flip at l requires delta°_l <= 2C|p| (C depending on a(.)), so the first flipped
carrier l(p) -> infinity as p -> 0, the carriers >= l(p) carry total weight <= 2 lambda_{l(p)} <= 4C|p| 2^{-l(p)-9} = o(|p|), and p*(f^p - f) -> 0;
(b) re-run carriers are robust peaks (margin >= q_0 delta°_l/4); (c) carriers < l(p) have values smooth in p.
*Proof.*  With eps fixed, n_l val_l(p) = A_l(p) + eps_l(B_l + delta_l H_l), and for l < l(p) only F-coordinates move: |A_l(p) - A_l(0)| <= C|p| ||y_l 1_F||_1.
A forced flip needs eps_l(0) A_l(p) <= -(B_l + delta_l H_l)/2 while eps_l(0) A_l(0) >= 0 (owner rule).  The weight bound is the second half of (SF*);
the cost bound is Z3 Lemma 3.1 (z-part) plus continuity (a-part).  (b) as Theorem 2.2 Step 4.  QED

## 10. Exact negative-d-mismatch data without dead zones are recovered (part 5.5-5.6)
Standing: design with (SF_tau), (b'); diagonal U; F finite; g in C(f) with two-piece data, kappa_w <= 1, Delta d_m < 0 for EVERY block m.
 (H1) no carrier is neutral, and only finitely many carriers (the set Neg) are negligible;
 (H2) D(j) != 0 for every j in E' := E ∪ {j notin F : o(j) in K_omega ∪ Neg, |gamma_{o(j)} u_{o(j)}(j)| <= 32 sum_{k > o(j)} |gamma_k u_k(j)|}.
E' is finite: for o in K_omega ∪ Neg (gamma_o != 0), on S_o \ E the later terms are <= C 2^{-2j} by (b) while |gamma_o| v_o(j) >= c 2^{-j}, and o has finitely
many new target coordinates.
**Lemma 5.4 (fine re-alignment carries exact data).  PROVED.**  Under (H1), (H2), f has no free coordinate off F, and for L >= L_0(f) the
fine re-alignment f^(L) satisfies (T1), (T2); the transplanted data satisfy ||b^+-_L - b^+-||_1 -> 0, Delta d^(L) -> Delta d, G_L -> g.
*Proof.*  No free coordinate: D(j) != 0 at every j notin F (Proposition 4.2' for owners outside K_omega ∪ Neg and j notin E; the definition
of E' and (H2) otherwise), and Lemma 3.3.  Choose L_0 beyond K_omega, Neg, E' and all carriers with S_l ∩ F != {}, and so large that
tau_{L_0} <= min_m |Delta d_m| M_m/(4 C_1).  Uniform convergence: coarse values are unchanged, ||zeta^(L) - zeta||_1 <= 2(1 + ||U||) sum_{l > L} lambda_l,
and w(k) is Lipschitz in zeta uniformly in k <= L (w = sgn(zeta(k)) M on peaks, M (nu_k/theta) sgn(zeta(k)) off peaks, continuous across nu = theta;
theta Lipschitz by Lemma 5.2(a); M, C, |zeta| Lipschitz by Lemma T): sup_{k <= L} |w^(L)(k) - w(k)| <= C_f sum_{l > L} lambda_l <= tau_L/4 by (SF_tau) for
L large; Delta d^(L) -> Delta d.  (T1): the omega-carriers are coarse strict non-peaks with fixed values and theta^(L) -> theta.  (T2):
 - o(j) > L: z^(L)_j = eps^(L)_o sgn u_o(j), w^(L)(o) = eps^(L)_o M^(L), so sgn gamma^(L)_o = eps^(L)_o and |gamma^(L)_o| >= tau_o C^(L)_1 lambda_o (choice of L_0);
   fine coordinates meet no K_omega-carrier; Lemma 4.1' gives z^(L)_j D^(L)(j) > 0.
 - o(j) <= L, o notin K_omega ∪ Neg, j notin E: z_j = sgn(gamma_o u_o(j)) (Proposition 4.2'), |gamma_o| >= 2 tau_o C_1 lambda_o, and the perturbation of gamma_o
   is <= |Delta d^(L)| lambda_o tau_L/4 + |Delta d^(L) - Delta d| lambda_o, so gamma^(L)_o keeps its sign and |gamma^(L)_o| >= tau_o C^(L)_1 lambda_o; Lemma 4.1'
   (which needs only |gamma^(L)_k| <= C^(L)_1 lambda_k for the later carriers, true also for the re-aligned fine ones).
 - o(j) in K_omega ∪ Neg, j notin E' (so j in S_o or a new target coordinate of o): gamma^(L)_o -> gamma_o != 0, and the later terms are bounded
   by C^(L)_1 lambda_k |u_k(j)| (also for re-aligned fine carriers).  For j in S_o beyond a finite set the (b)-bound C 2^{-2j} against |gamma_o| v_o(j) ~
   2^{-j} gives dominance uniformly in L; on the finitely many remaining coordinates the fine contributions are <= (8/3) C_1 sum_{l > L} lambda_l -> 0
   and the coarse ones converge, so the factor-32 dominance at f persists.  - j in E': z_j D(j) > 0 by (H2) and D^(L)(j) -> D(j).
f^(L) has no free coordinate (the owner rule assigns +-1).  Cost (Lemma 3.6): ||D^(L) - D||_1 <= (5/3) sum_k lambda_k |Delta d^(L) w^(L)(k) - Delta d w(k)| -> 0
(dominated convergence); Fl lies in fine coordinates, where D and D^(L) are sums over fine carriers, so ||D 1_Fl||_1 + ||D^(L) 1_Fl||_1 <=
(10/3) C_1 sum_{l > L} lambda_l -> 0.  QED
**Lemma 5.5 (bank levers).  PROVED.**  Let f' := f^(L) (L >= L_0) with the transplanted data.  For each block m pick a fine carrier
l_b(m) > L of block m and s_m := min S_{l_b(m)} (a contact, z = eps_{l_b(m)}), and BANK there: a^#(mu) := (a + sum_m mu_m eps_{l_b(m)} e_{s_m})/q*(.),
mu_m >= 0, z unchanged; then re-run from l_b(1) with hysteresis.  For suitable small mu (chosen block after block, l_b(m) increasing) the row
f^# has support F ∪ {s_1, ..., s_N}, satisfies (BT), carries transplanted exact data with Delta d^# < 0 (bank coordinates contact-like),
and p*(f^# - f') + ||G^# - G'|| -> 0 as mu -> 0.
*Proof.*  nu^2 = nu_0^2 + sum s_{s_m}^2 mu_m^2, so zhat moves by O(mu^2) on F and zhat_{s_m} = eps(1 + s_{s_m}^2 mu_m/nu) + O(mu^2).  |val_{l_b(m)}| increases at
the first-order rate v_{l_b}(s_m) s_{s_m}^2/nu; the other carriers containing s_m are > l_b(m), of total weight <= 2^{-10} lambda_{l_b} v_{l_b}(s_m) 2^{-(m +
k(l_b))} by (SF*) (min S = s_m); F-dependent carriers move by O(mu^2); forced flips occur only at levels >= l(mu) -> infinity, total weight
o(mu) (Lemma 4.4(a) argument).  By Lemma 5.2, theta_m(mu) - theta_m >= kappa_m mu_m/2 for small mu_m (kappa_m := c_Theta lambda_{l_b} v_{l_b}(s_m) s_{s_m}^2/nu,
l_b(m) large), while each coarse nu_k (k <= L, the only candidates for degeneracy) moves by O(mu^2).  So small mu_1 > 0 removes all
degenerate peaks of block 1 (gap dgap_1 > 0); then choose l_b(2), mu_2 so that block 1 moves by < dgap_1/2, etc.  (BT): F^# finite, Q^#_m within
the coarse carriers, no degenerate peak, (MS) by margins.  (T1), (T2): as in Lemma 5.4 (coefficients of carriers < l_b(1) move
continuously in mu; re-run carriers are owner-aligned robust peaks with |gamma| <= C_1 lambda; at s_m the owner l_b(m) dominates, so
D^#(s_m) z_{s_m} > 0 and the data split contact-like there).  Cost: Y4
Lemma 2.2 (banks) and Lemma 3.6.  QED
**Theorem 5.6 (exact negative-d-mismatch data without dead zones are recovered).  PROVED.**  Under the standing hypotheses and (H1),
(H2): (f, g) in cl NA((c_0, p), l_2^2).
*Proof.*  The rows f_i := (f^(L_i))^#(mu_i) (L_i -> infinity, mu_i -> 0) are (BT), hence satisfy (SC) in every block, converge to f, have support
F ∪ B_i, and carry exact two-piece data with Delta d < 0 representing G_i -> g, kappa^(i)_w -> kappa_w (Lemmas 5.4, 5.5).  Theorem 3.7 with
Y4-ref Lemma P2 (Lemma U and Theorem E with banked support, data contact-like on the banks).  QED
**Corollary 5.7 (corrected Proposition 4.5).  PROVED.**  At the self-aligned rows of Theorem 2.2 with finitely many exceptional carriers
tuned through F (including exactly degenerate swallowing-type peaks, if present), every mate with two-piece data, kappa_w <= 1, omega
supported on exceptional strict non-peaks, Delta d < 0 and gamma_k != 0 on the omega-carriers is recovered, provided every exceptional
strict non-peak NOT carrying omega has |w(k)| >= 2 tau_k (true for the rows of Theorem 2.2 and Remark 2.3, whose only exceptional strict
non-peak is l_-).  (E = {} since the exceptional targets lie in F; non-exceptional carriers are robust peaks with |w| = M, so (H1) holds; every coordinate off F is dominated by its owner
with factor >= 48 (Theorem 2.2 Step 6; all non-omega coefficients have |gamma|/lambda = |Delta d| M, the omega-carrier a larger one), so (H2).)
Part 4's Proposition 4.5 omitted the hypothesis gamma_k != 0 on the omega-carriers (otherwise S_k is a dead zone); Delta d >= 0 is Cor. cor:D1.
Numerical check: Section 13.
**Proposition 5.8 (positive mismatch forces dead zones).  PROVED** (design with (SF_tau), (b'), (FD)).  If g in C(f) (F finite) carries
two-piece data with Delta d_m > 0 for some block m, then all but finitely many (FD)-carriers of block m are neutral or negligible.
*Proof.*  For all but finitely many (FD)-carriers l of block m, l notin K_omega and j_l notin F ∪ E.  If l were neither neutral nor negligible,
Proposition 4.2' would give z_{j_l} = -sgn(val_l) sgn(y_l(j_l)), |z_{j_l}| = 1, while Lemma 1.1 gives n_l val_l = y_l(j_l) z_{j_l} + R, |R| <= (1 + max s)
(||y_l||_1 - |y_l(j_l)| + delta_l H_l) < |y_l(j_l)| (|zhat_i| <= 1 + s_i): sgn val_l = sgn(y_l(j_l)) z_{j_l} = -sgn val_l, impossible.  QED
So, if all Delta d_m >= 0 the data are recovered by Cor. cor:D1; if all Delta d_m < 0, by Theorem 5.6 unless (H1) or (H2) fails; MIXED data
(I_- != {} and some Delta d_m >= 0) have dead zones: a block with Delta d_m = 0 has only neutral carriers outside K_omega, and a block with
Delta d_m > 0 has infinitely many nearly neutral ones (Proposition 5.8).

## 11. (B) multi-block rays: block-triangular structure (part 4.5)
**Lemma 4.5 (block-triangularity).  PROVED.**  At strict non-peaks q_l = (q_0/sigma_m) eps_l val_l (Y4-ref C.7), so the d-map component D_m
depends only on the values of carriers of block m, and the zero-cost cone C(kappa) of a clean sub-window depends only on the pattern
(signs, contact types), not on values.  Per-carrier exact tuning (Y4-ref Prop. P4) changes a prescribed finite set of values exactly and
all others at second order.
**Proposition 4.6 (sequential projection).  PROVED.**  Let C be a pointed polyhedral cone in [0, infinity)^U, D = (D_1, ..., D_N) linear, C_0 := C,
C_i := C_{i-1} ∩ ker D_i, D^(i)_min := min{|D_i(rho)| : rho extreme ray of C_{i-1}, ||rho||_1 = 1, D_i(rho) != 0}.  For tau in C let tau^0 := tau and
tau^i the point of C_i given by Y4 Lemma 1.8 for (C_{i-1}, D_i, tau^{i-1}).  Then ||tau^i - tau^{i-1}||_1 <= |D_i(tau^{i-1})|/D^(i)_min and |D_i(tau^{i-1})| <=
|D_i(tau)| + ||D_i|| sum_{i' < i} ||tau^{i'} - tau^{i'-1}||_1; hence dist_1(tau, C ∩ ker D) <= K |D(tau)|_infty with K depending only on the D^(i)_min
and ||D||.  (Y4 Lemma 1.8 for each i; D_i is Lipschitz.)  The extreme rays of C_i are those of C_{i-1} with D_i = 0 and the "sliced rays"
|D_i(rho_b)| rho_a + |D_i(rho_a)| rho_b of 2-faces with D_i(rho_a) > 0 > D_i(rho_b).  So the vector-valued d-row becomes N scalar d-rows on nested
cones, and the joint objects (R6) of Y4 become the scalars D_i(rho) of sliced rays.
**Remaining step for (B).  OPEN.**  Exactify, block by block, the tiny values D_i(rho) of the extreme rays of C_{i-1} by tuning block-i values
only (block-<i values frozen, so C_{i-1} is unchanged).  The system is linear in the block-i values with matrix R^(i) = (rho(l))_{rho tiny, l in
block i} and is feasible (x = -val); the issue is its Hoffman constant: a tiny minor of R^(i) (near-dependence of two tiny sliced rays) is a
new joint object that cheap tuning cannot repair.  At (BT) points the issue does not arise (Corollary 3.1).

## 12. The counterexample hunt: what a counterexample must look like
Designed operator: SLD-type with (SF_tau), (b'), (Z0), (GM), (FD) (Lemma 2.1); U diagonal.
 1. The most dangerous explicit instances of (C) and (D) — self-aligned rows with all peaks swallowing-type, a swallowed q < 0 carrier, exact
    coherence, a weak or exactly degenerate swallowing-type peak, and mates carrying the coherent shift through all peaks — are
    recovered (Corollary 3.1, Proposition 3.2, Corollary 5.7).  g in C(f) was verified rigorously (Proposition prop:onesidedupper), and
    the recovery is by (SC)-companions, not by windows.
 2. Exact two-piece data are recovered at every F-finite row unless (i) the data are MIXED (I_- != {} and some Delta d_m >= 0), or (ii) a
    Delta d < 0 block has infinitely many neutral/nearly neutral carriers, or (iii) D vanishes at one of the finitely many coordinates of E'
    (Cor. cor:D1, Theorem 5.6, Proposition 5.8).  All three are DEAD-ZONE phenomena.
 3. Near-threshold carriers through F are generic (Proposition 5.1), so the design cannot avoid infinitely many of them; block-tame
    approximation (Proposition 5.3) and owner re-alignment (Lemma 5.4) neutralize them for exact data without dead zones.
 4. So a counterexample with F finite needs either a mate WITHOUT exact two-piece data of kappa_w <= 1 at f (Theorem thm:onesided gives such
    data at (BT) points; elsewhere the window method is needed and its residuals are (B) tiny minors of sliced-ray matrices and (C) shift
    resonance at clean windows, V2's domain), or exact data with dead zones; with F infinite, (E) (V3's domain).
Main obstacle (precise).  DEAD ZONES.  A coarse coordinate j all of whose coarse carriers are neutral or nearly neutral (e.g. the signature
set of a carrier of a d-neutral block next to a block with Delta d < 0) has its d-row sign D(j) decided by FINE carriers.  Making the Delta d < 0
blocks satisfy (SC) requires re-aligning those fine carriers (Proposition 5.1 shows that near-threshold fine carriers are unavoidable),
which may reverse sgn D(j) while z_j is frozen; then (T2) fails and the exact data cannot be transplanted.  The violation is tiny: at the
companion f^(L) it is at most (10/3) C_1 sum_{l > L} lambda_l in l_1.
Precise remaining step.  A STABILITY statement: if two-piece data at a (BT) row f# violate (T2) only on a set V of coordinates with
||D^# 1_V||_1 <= epsilon, then f# has a (BT) companion f## at distance o(1) (epsilon -> 0) carrying exact data with the same omega and
||b## - b#||_1 = o(1).  Suggested route: PULL (Y4-ref C.2-C.4) the violated coordinates — a pull flips z_j and makes j a support coordinate,
after which the violated data become admissible (t|b(j)| <= |a(j)| is satisfied by masses of size |D^#(j)|/t, cost O(v(j) log(1/v(j)))) — the
difficulty being that V may be infinite (infinitely many dead-zone coordinates), which leads to infinite support (V3's machinery).

## 13. Numerics
 - sa_check.py (Construction SA, N = 1, 9 carriers, 6 signature coordinates each, 30 extra coordinates): all l != l_- are peaks with
   sign eps; l_- strict non-peak (nu/theta = 0.24) with q < 0; N(w) = ||w||_inf + ||Phi w||_2 = 1; SOCP block norm equals A(theta) (rel. err.
   6.3e-9); W and V z-signed (72 coordinates); Delta d = -5.85e-30 < 0; identity R^*(omega^- - omega^+) - Delta d R^* w = Delta_alpha lambda V to 4.4e-47.
 - degenerate_check4.py (Corollary 5.7 / Lemma 4.4 mechanism; N = 1, 10 carriers, F = {0,1,2,3}, (SF*)-type weights with ratios 3e-5 ... 5e-7;
   l_- = 1 tuned to n val = -eta, l_D = 2 tuned to EXACT degeneracy): tuning residuals 8.5e-11 and 1.3e-6 (double-precision limit, theta Phi_D =
   5e-11); q_- < 0; Delta d = -1.33e-11; D z-signed at f.  Perturbation a -> a(1 + p (0.3, -0.5, 0.7, -0.2)) with hysteresis, p = 1e-13 ... 1e-9: no
   forced flips, nu_D/theta = 0.99997, 0.9997, 0.9974, 0.974, 0.741 (non-degenerate), l_- strict non-peak with q < 0, other nu/theta >= 5, D^p
   z^p-signed, Delta d^p = -1.33e-11, ||R^*(w^p - w)||_1 = 3.9e-15 ... 4.0e-11 (linear in p).  At p = 1e-8 val_D changes sign and D^p fails on S_D
   (the proof needs sgn val_D preserved).  A model with weights 10^{-2l} (violating (SF*)) failed z-signedness at one coordinate of S_7 hit
   by the target of carrier 8: (SF*) is the right dominance hypothesis.
 - Proposition 5.1 needs no numerics (Baire argument); finite truncations are always (BT), so a non-recovery phenomenon can only be a
   limit effect (uniformity of the constants along approximants), which finite SOCP models cannot exhibit directly.

## 14. Corrections relative to the part files
 1. Theorem 2.2(d): garbled sentence replaced by the clean statement in Section 4.
 2. Lemma 3.4: statement cleaned ((GM) with Phi_l <= g_l 2^{-l}; consequence stated with theta-bound Theta).
 3. Theorem 3.5(c): the proof ("theta changes continuously and strictly") ignored the infinitely many later carriers containing the moved
    coordinate (Lemma 1.2), whose sign changes make theta discontinuous; replaced by Proposition 5.3 (hysteretic re-run + Lemma 5.2).
 4. Lemma 3.8: the a.e. statement reworded (C^1 family, |theta'| >= v_0 when some nu_k are constant).
 5. Lemma 4.1 / Proposition 4.2: the negligibility scale C_0 = max|omega| + 2 max|Delta d| made the statement vacuous when |Delta d| << |omega|;
    replaced by Lemma 4.1' / Proposition 4.2' with the design thresholds (SF_tau), (b').
 6. Proposition 4.5: needs gamma_k != 0 on the omega-carriers; now Corollary 5.7 of Theorem 5.6 (no genericity of p needed).
 7. Theorem 4.6 (SKETCH) and the design question (GO): superseded; (GO) is FALSE for every design (Proposition 5.1) but not needed
    (Theorem 5.6).
 8. Remark 2.3(D): exact degeneracy in the pure self-aligned form downgraded to OPEN; at fixed z it is easy (Proposition 5.1(c)).
