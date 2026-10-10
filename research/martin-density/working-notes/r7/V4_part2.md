# V4 part 2 — Realizability: self-aligned rows; (B), (C), (D) cannot be designed away; lacunary profiles and (E)

Notation of part 1.  Throughout: SLD-type design, diagonal base U (U^* e_j^* = s_j kappa_j), N >= 1.

## 2.1 Two harmless design conditions
(SF*) (super-fast decay relative to level-l data)  For every carrier l,
   (1 + ||U||) sum_{l'' > l} lambda_{l''}  <=  2^{-10} lambda_l delta_l 2^{-(m(l) + k(l) + min S_l)} eta_l / n_l,
   eta_l := min(1, min_{j in supp y_l} |y_l(j)|),
and  c_l <= c_{l-1} delta_l 2^{-min S_l - l - 10}/(1 + ||U||)  for l >= 2.
(Z0)  Z_0 := N \ union_l S_l contains two coordinates p != p', and the target family contains y* := (e_p^* - e_{p'}^*)/q*(e_p^* -
e_{p'}^*) (hence, by (D1), y_l = y* for infinitely many carriers l of every block).
**Lemma 2.1.  PROVED.**  Every SLD-type design can be modified to satisfy (SF*) and (Z0) without affecting admissibility,
N-independence, or any theorem of Section 8 of the note or of Rounds 5-6.
*Proof.*  (SF*) only asks c_{l+1} (chosen last at stage l, after y_l, delta_l, S_l, and all level-<= l design quantities) to be smaller
than an explicit positive number computable at stage l; replace c_{l+1} by the minimum of its old value and that number.  Every
window theorem uses the weights only through UPPER bounds on fine weights (box bound sum_{l'>l} lambda_{l'} <= T_lo^3 or b(w)^2, (P2))
and through c_{l+1} <= c_l/4 (admissibility); smaller weights preserve both.  delta_l depends only on S_l and U, so it is known
in advance.  (Z0): choose the S_l inside N \ {p, p'} (e.g. p = j_0 and p' another coordinate excluded from all S_l), and add y*
to the dense target family; allowedness (a),(b) hold for y* at every l since supp y* ∩ union S_l = {}.  QED

## 2.2 Self-aligned rows with one tuned exceptional carrier
**Construction SA(m_0, eta).**  Fix a block m_0, a carrier l_- of block m_0 with y_{l_-} = y* ((Z0)), and eta > 0.
 (1) F := {p, p'}, a := (a_p, a_{p'})/(a_p + a_{p'} + nu) with a_p, a_{p'} > 0 chosen below; so sgn a = +1 on F and
     zhat_p = 1 + s_p^2 a_p/nu, zhat_{p'} = 1 + s_{p'}^2 a_{p'}/nu (scale invariant).
 (2) Recursion over carriers l = 1, 2, ... (all blocks).  "Assigned" coordinates: initially F.  At step l, let
     A_l := sum_{j in supp y_l assigned} y_l(j) zhat_j, B_l := sum_{j in supp y_l unassigned} |y_l(j)|.
     If l != l_-: eps_l := sgn A_l (eps_l := +1 if A_l = 0); assign z_j := eps_l sgn y_l(j) at the unassigned j in supp y_l and
     z_s := eps_l on S_l.  If l = l_-: eps_{l_-} := +1, z := +1 on S_{l_-} (supp y_{l_-} = {p, p'} = F is assigned).
     Coordinates never assigned get z := 0.
 By allowedness (a), S_l is unassigned at step l (earlier targets avoid S_l; F ⊂ Z_0), so the recursion is well defined; z = sgn a
 on F; |z| <= 1; (a, z) is admissible forced data of a unique first row f =: f_SA (Remark rem:lemmaZ(c)).

**Theorem 2.2 (self-aligned rows).  PROVED** (design with (SF*), (Z0); diagonal U; any N).  There are a_p, a_{p'} > 0 such that
f_SA has the following properties.  Put delta°_l := delta_l H_l/n_l and theta_0 := lambda_{l_c} delta°_{l_c}/2, where l_c is the
first carrier of block m_0 (if l_c = l_-, use the second).
 (a) Every carrier l is swallowed with sign eps_l (z = eps_l on S_l; F ∩ S_l = {}).  For l != l_-: n_l val_l = A_l +
     eps_l(B_l + delta_l H_l), so sgn val_l = eps_l and |val_l| >= delta°_l.
 (b) Every l != l_- is a NON-DEGENERATE PEAK of its block, of swallowing type (varsigma_l = eps_l), with margin
     mu_l >= q_0 delta°_l/2 (robust, independent of Phi_l) and nu_l/theta_m >= 2^{10} for all l after the first carrier of the block.
 (c) n_{l_-} val_{l_-} = -eta, and if eta < n_{l_-} theta_0 Phi_{l_-}/(2 m_0), then l_- is a strict non-peak of block m_0 with
     gap >= M_{m_0}/2 and q_{l_-} < 0 (eps_{l_-} = -sgn w), and its base vector u_{l_-} 1_{F^c} = v_{l_-} is z-signed
     (SELF-RESONANT: eps_{l_-} u_{l_-} 1_{F^c} vanishes off K and is z-signed on K).
 (d) The vector W := sum_l lambda_l eps_l u_l 1_{F^c} (all carriers, all blocks) and every partial sum over any set of carriers
     closed downward along supports... more precisely: for every j notin F with W(j) != 0, j is a contact and z_j W(j) > 0;
     the same holds for W^{(L)} := sum_{l <= L} lambda_l eps_l u_l 1_{F^c} for every L, and, for N = 1, for every vector
     sum_l lambda_l rho_l eps_l u_l 1_{F^c} with weights rho_l in [1/2, 1] (dominance is preserved by bounded weights).
 (e) Consequently, in block m_0: (H2'') UPPER fails (all peaks swallowing type, no good carrier, swallowed q<0 carrier l_-), and
     c_*(l) = 0 for every l >= l_- (with delta_{m_0} = 1 and x_{l'} := lambda_{l'} on Bfree): configuration (C) with EXACT coherence.
 (f) (SC) holds in every block: for every Upsilon >= 1, Scr_m(Upsilon s) = o(s) as s -> 0 (along ALL s).
 (g) There are no free coordinates in the support of any carrier; no degenerate peak; finitely many (one) strict non-peaks.
*Proof.*  Step 1 (tuning).  supp y* = {p, p'} = F, so n_{l_-} val_{l_-} = y*(zhat_F) + delta_{l_-} H_{l_-}, independent of the
recursion, and y*(zhat_F) = c*(s_p^2 a_p - s_{p'}^2 a_{p'})/nu, c* := 1/q*(e_p^* - e_{p'}^*), nu = (s_p^2 a_p^2 + s_{p'}^2 a_{p'}^2)^{1/2}.
As a_p/a_{p'} runs over (0, infinity) this runs continuously over (-c* s_{p'}, c* s_p), an interval containing 0; and
-(delta_{l_-} H_{l_-} + eta) lies in it for small delta_{l_-} H_{l_-} + eta (true: delta_l <= 2^{-l}, take l_- late, or eta small and
the interval is open around 0 — if delta_{l_-}H_{l_-} >= c* s_{p'} choose a later carrier with target y*).  Choose the ratio by the
intermediate value theorem: n_{l_-} val_{l_-} = -eta.
Step 2 ((a)).  For l != l_-: supp y_l splits into assigned and newly assigned coordinates, z_j y_l(j) = eps_l |y_l(j)| on the new ones,
S_l ∩ F = {} and z = eps_l on S_l, so by Lemma 1.1 n_l val_l = A_l + eps_l(B_l + delta_l H_l), with eps_l = sgn A_l (or A_l = 0).
Step 3 (lower bound on theta).  For a block m with zeta := R_m^** zhat, Psi(th) = A(th)^2 - B(th) (Lemma T).  A(th) >= ||zeta||_1 -
th ||Phi_m||_2^2 >= ||zeta||_1 - th/4 and B(th) <= th sum_k Phi_k^2 nu_k = th ||zeta||_1; at th = ||zeta||_1/2, Psi >= (49/64 - 1/2)
||zeta||_1^2 > 0, so theta_m > ||zeta||_1/2 >= lambda_{l_c}|val_{l_c}|/2 >= theta_0 (Lemma T(c)).
Step 4 ((b)).  Fix l != l_- in block m and put th := nu_l = m|val_l|/Phi_l.  For a coarser carrier k of block m, the A-term is
(|zeta(k)| - th Phi_k^2)_+ = m Phi_k (|val_k| - |val_l| Phi_k/Phi_l)_+ = 0, because |val_k| <= ||u_k||_1 ||zhat||_inf <= 1 + ||U||
and Phi_l/Phi_k <= c_l/c_{l-1} <= delta_l 2^{-min S_l - l - 10}/(1+||U||) <= |val_l| 2^{-l-9}/(1+||U||) ((SF*), n_l <= 5/4).
Finer carriers contribute at most sum_{finer}|zeta(k)| <= (1 + ||U||) sum_{l''>l} lambda_{l''} <= 2^{-10} lambda_l |val_l| ((SF*),
|val_l| >= delta°_l >= delta_l 2^{-min S_l}/n_l).  Hence A(th) <= 2^{-10} m |val_l| while B(th) >= Phi_l^2 nu_l^2 = m^2 val_l^2, so
Psi(nu_l) < 0 and theta_m < nu_l: l is a peak, non-degenerate, with sign sgn val_l = eps_l.  If l_1 is the first carrier of block m,
theta_m < nu_{l_1} <= m(1 + ||U||)/Phi_{l_1}, and for l later than l_1 the same (SF*) estimate gives nu_l >= 2^{10} m(1+||U||)/Phi_{l_1}
> 2^{10} theta_m, so mu_l = q_0 Phi_l (nu_l - theta_m)/m >= q_0 |val_l|(1 - 2^{-10}) >= q_0 delta°_l/2.  For l = l_1 itself the
margin is a fixed positive number.
Step 5 ((c)).  nu_{l_-} = m_0 eta/(n_{l_-} Phi_{l_-}) < theta_0/2 < theta_{m_0}/2: strict non-peak; gap = C(theta - nu)/|zeta| >=
C theta/(2|zeta|) = M/2.  w(k(l_-)) = C zeta(k(l_-))/(Phi^2 |zeta|) has the sign of val_{l_-} = -eta/n < 0 = -eps_{l_-}, so q_{l_-} =
eps Phi w/(mC) < 0.  u_{l_-} 1_{F^c} = v_{l_-} >= 0 lives on S_{l_-}, where z = +1 = eps_{l_-}.
Step 6 ((d), dominance).  Let j notin F with W(j) != 0 and let o be the first carrier with j in supp u_o (the owner).  If j in S_o,
then z_j = eps_o and the own term lambda_o eps_o v_o(j) dominates all later terms: for j <= m(o)+k(o)+4 by (SF*) (later total
<= (4/3) sum_{l''>o} lambda_{l''} <= 2^{-9} lambda_o v_o(j)), for j > m(o)+k(o)+4 by allowedness (b) (each later l'' with j in supp
y_{l''} has lambda_{l''} <= c_{l''}/4 <= 2^{-2j} c_o delta_o/8, total <= 2^{-2j} c_o delta_o/6 <= 2^{-6} lambda_o v_o(j)).  If j notin S_o,
then j in supp y_o was unassigned at step o (else an earlier carrier would own it), so z_j = eps_o sgn y_o(j), and |lambda_o y_o(j)/n_o|
>= lambda_o eta_o/n_o >= 2^{9}(4/3) sum_{l''>o} lambda_{l''} by (SF*).  In both cases sgn W(j) = sgn(eps_o u_o(j)) = z_j, |z_j| = 1.
Partial sums W^{(L)} contain the owner's term whenever they contain j (the owner is the first carrier at j); bounded weights in
[1/2,1] change the dominance ratios by a factor <= 2.  (For several blocks the owner may belong to another block; (d) is stated for
the full sum W and its downward-closed partial sums; for single-block vectors use N = 1 or 3.5 below.)
Step 7 ((e)).  All peaks of block m_0 are swallowed of swallowing type and l_- is swallowed with q < 0: by Z4-ref Remark 3.3 UPPER
fails (no good peak, no anti-sign swallowed peak, a swallowed q<0 carrier).  With delta_{m_0} = 1, P* = robust coarse peaks of block
m_0 (all coarse carriers of m_0 except l_-, by (b)), Bfree = all other swallowed carriers <= l, and x_{l'} := lambda_{l'} (eps from
the construction), the vector sum_m delta_m Pi_m + sum x eps u equals W^{(l)} restricted to the carriers <= l (all of them appear with
weight lambda), which is z-signed with no free coordinates by (d): its cost is 0.  So c(1; l) = 0 and c_*(l) = 0.
Step 8 ((f)).  Rates: peaks l after the first carrier of their block have mu_l >= q_0 delta°_l/2; finitely many other carriers have fixed
positive rates; l_- has Phi gap >= Phi_{l_-} M/2.  Given s > 0, a carrier contributes to Scr_m(Upsilon s) only if it is one of the
finitely many fixed-rate carriers with rate <= Upsilon s (none for s small), or q_0 delta°_l/2 <= Upsilon s; the latter carriers
have, by (SF*) (c_l <= c_{l-1} delta_l 2^{-min S_l} ...), Phi_l <= c_{l-1} delta°_l 2^{-l} <= c_{l-1} 2^{1-l} Upsilon s/q_0, and their
total contribution is <= sum_{l >= l(s)} Phi_l <= 2 Phi_{l(s)} <= c_{l(s)-1} 2^{2-l(s)} Upsilon s/q_0 = o(s), where l(s) -> infinity
as s -> 0.  Step 9 ((g)) is immediate from the construction.  QED

**Remarks 2.3.**  (1) The construction is the "self-aligned row" of the Z4 referee (Remark 3.3) made exact, plus ONE carrier tuned
through the base support.  The tuning uses only a (two coordinates of F), not z, so it is independent of the recursion.
(2) Varying the construction gives the other residual patterns, each realized exactly:
 * (D) aligned corner (N = 1): tune, with two more coordinates p'', p''' in F (target y** = (e_{p''}^* - e_{p'''}^*)/q* in the family),
   one more carrier l_D to |val_{l_D}| = theta Phi_{l_D}/m (1 + xi) with eps_{l_D} = sgn val_{l_D}: a swallowing-type peak with relative
   margin xi.  Varying the ratio a_{p''}/a_{p'''} moves val_{l_D} continuously; theta moves continuously EXCEPT for jumps caused by sign
   switches eps_l of carriers whose A_l crosses 0 (each such carrier has |A_l| <= tuning range, so only finitely many coarse ones can
   switch for a small range, and the total jump caused by fine ones is <= C sum_{l'' > L} lambda_{l''}, arbitrarily small).  Hence every
   prescribed relative margin xi in (0, xi_0) is attained up to an arbitrarily small error: a WEAK swallowing-type peak with margin as small
   as desired is realized (PROVED); an EXACTLY degenerate one needs the jump issue to be removed (SKETCH).  All other carriers are
   swallowing-type robust peaks with z = varsigma on all of S_l (not raisable), l_- has q < 0 and z = eps_{l_-} on S_{l_-} (not raisable),
   there is no anti-sign swallowed peak and no good carrier, so l_D is the only raisable carrier of the block: (D-ii)-(D-iv).  (D-v): for
   N = 1 every contact j is owned by a carrier of the block whose term dominates at j, so an inward z-move at j lowers |val| of the owner at
   first order and the owner dominates the change of A(theta), i.e. it LOWERS theta; free coordinates carry no carrier.  So no target move
   raises the threshold.  l_D is non-rigid in the sense of Cor. V.1 (the block has the swallowed q < 0 carrier l_-).  For N >= 2 an inward
   move at a contact owned by ANOTHER block can raise theta_{m_0} (anti-aligned block-m_0 terms): realizability then needs block-m_0
   alignment of all its target coordinates (part 3.5 below), SKETCH.
 * (B) core: two blocks m_1 != m_2, tuned carriers l_1, l_2 (one in each, both with target y*-type vectors on disjoint pairs of Z_0
   coordinates) made strict non-peaks through F, plus a link: a coordinate j in supp y_{l_1} ∩ supp y_{l_2}.  With targets supported in F
   the link is invisible (j in F), so a genuine 2-block ray needs a link OFF F: choose instead carriers whose targets share a coordinate
   j in Z_0 \ F and put z_j := 0 (free) with all other target coordinates in F; the cone row L_j(tau) = 0 couples tau_{l_1}, tau_{l_2}.
   The d-vector of the ray is (q_{l_1} r_1, q_{l_2} r_2) with q's linear in the tuned values; two such rays with tuned values give a
   2 x 2 d-matrix with prescribed (tiny) determinant.  SKETCH (needs targets of the required shape in the family, which the design can
   include; the self-aligned remainder is as in Theorem 2.2).
(3) Nothing in (C), (D) requires infinitely many tuned carriers; finitely many tunings through F suffice.  The configurations are
therefore present for every design satisfying (SF*), (Z0) — in particular for every design obtained from D_X, D^PW or D^Y by
Lemma 2.1 — and they cannot be removed by genericity of targets, of signature masses, by private coordinates or disjoint coordinate
sets for different blocks (all of these leave Construction SA intact).

**Proposition 2.4 (single-vector principle, any admissible T).  PROVED.**  For any admissible T, any finite F, any a in S_{q*} with
supp a = F and any countable family of vectors V_i in l_1 such that every coordinate j notin F has an index i(j) with |V_{i(j)}(j)| >
2 sum_{i > i(j)} |V_i(j)| (a dominance order), the choice z_j := sgn V_{i(j)}(j) makes every partial sum sum_{i <= n} V_i that contains
the dominant index z-signed off F.  (Proof: as Step 6.)  This is the general form of Remark rem:nodesign: a design can defeat ONE
z-signing only by destroying dominance (cancellations among comparable terms at the same coordinate), and the first row then still
has the freedom of the signs of the carriers themselves (eps_l), which is what Construction SA uses.
**Remark 2.5 (designs violating (SF*)).**  A design with weights NOT decaying faster than the entries of earlier targets creates
coordinates where several carriers contribute comparably; one can build "sign gadgets" (a later carrier whose target has two dominant
entries at early coordinates of two earlier signature sets forces a relation between the two earlier peak signs, and odd cycles of
such relations force a conflict).  I checked that this does NOT exclude (C): the conflict coordinates are target coordinates, where the
first row may choose z freely, and the earlier carrier then counts as swallowed on S^nat = S \ (F ∪ T(l)) (Y1), while the conflicting
term is dominated by the gadget carrier's own trace (slaving).  HEURISTIC: no design excludes (C) through target or weight structure.

## 2.5 Lacunary signature profiles and (E)
**Lemma 2.6 (no critical flip profile for lacunary signatures).  PROVED.**  Let beta_i > 0 (i >= 1) with beta_{i+1}/beta_i -> 0, let
x_i in (0, infinity] be arbitrary, and m(x) := sum{beta_i : x_i < x}.  Then NOT (0 < liminf_{x->0} m(x)/x <= limsup_{x->0} m(x)/x <
infinity).  In particular, if a design uses signature profiles v_l(s_i) (s_i the i-th element of S_l) with v_l(s_{i+1})/v_l(s_i) -> 0,
no first row has a critical flip profile m_l(x) = sum{v_l(s) : s in S_l ∩ F, |a_s| < x v_l(s)} (take x_i := |a_{s_i}|/v_l(s_i), and
x_i := infinity for s_i notin F).
*Proof.*  Suppose c <= m(x)/x <= C for 0 < x <= x_0.  (i) If x_k < x_0, then for every x in (x_k, x_0], beta_k <= m(x) <= Cx;
letting x decrease to x_k gives beta_k <= C x_k.  (ii) Fix k_0 such that beta_{k+1} <= beta_k/2 for k >= k_0 (lacunarity), and let
x_* := min{x_k : k < k_0, x_k > 0} (x_k = 0 is impossible for k with beta_k counted: x_k = 0 would give m(x) >= beta_k for all x > 0,
contradicting m(x) <= Cx as x -> 0).  Choose i >= k_0 with beta_{i+1} <= c beta_i/(8C) and x := beta_i/(2C) < min(x_0, x_*).  An index
k contributes to m(x) only if x_k < x; then k >= k_0 (as x < x_*) and, by (i), beta_k <= C x_k < Cx = beta_i/2, so k > i (the beta_k,
k >= k_0, are decreasing).  Hence m(x) <= sum_{k > i} beta_k <= 2 beta_{i+1} <= c beta_i/(4C) = cx/2 < cx, a contradiction.  QED
**Price (why this is not a free win).**  (i) Y4-ref Prop. P4 (exact two-sided tuning by pulls) needs pull sizes 2 v_l(j_l) within a
fixed factor of any prescribed eta (bounded gaps (G)); lacunary profiles provide pull sizes only on a lacunary set, so P4 would
overshoot by unbounded factors.  A hybrid profile (geometric on part of S_l, lacunary on the rest) restores pulls but also restores
critical profiles on the geometric part (the first row puts F there).  (ii) Lemma 2.6 removes CRITICAL profiles, not the mixed ones
(liminf m/x = 0 and limsup m/x = infinity), which a first row CAN produce with lacunary signatures (jumps of coarse indices placed at
the bottom of lacunary gaps); these are sparse at some scales and super-critical at others; Y3's methods treat sparse and super-critical
profiles separately (Y3 Thm 2.1/R1, Thm 3.5), and a mixed profile needs window selection at the sparse scales (Y3 liminf-sparsity
extension, SKETCH).  So for (E): a lacunary design converts (O4-crit) into "mixed profiles + pull tuning at infinite F", which is not
obviously easier.  HEURISTIC assessment: the design lever exists but trades (O4-crit) for the assembly-level tuning problem.
