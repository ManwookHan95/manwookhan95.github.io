ERRATUM (see G3_notes.md, authoritative): Cor. 2.11's free-coordinate bound is t/(q_0 eta_s), not t/(2 q_0 eta_s), and the split needs
1/4 instead of 1/3 when free coordinates are present (corrected statement in the notes); Interpretation (b) wrongly lists shared FREE
targets as an escape (a free coordinate pins V two-sidedly).  The notes also add Theorem CL (conservation law) and Cor. CL.1-CL.2.

# G3 part 2: constructing a persistent residual row -- what can be done, what blocks the natural construction

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Design: T_fin^{K2} with (FC) (J2), P-TU windows and F-2 (J1-ref), diagonal
doubly exponential base mu*_s = 2^{-2^{2^s}}, signature sets S_l = {2^l(2i+1) : i >= 1}, v_l(j) = delta_l 2^{-j}/n_l on S_l, carriers
u_l = y_l + v_l with targets y_l supported in T(l) (coarse), H2 Lemma 2.2: T(l) ∩ union_k S_k ⊂ [1, l].  Notation of part 1 and H2 1.

## 2.1 Abstract persistence lemmas (the "nested tuning" step)

LEMMA 2.1 (nested tuning, open stage conditions).  PROVED.  Let (Z, d) be a complete metric space and O_L ⊂ Z open (L >= L_0).
Assume O_{L_0} != {} and
 (FT) for every L >= L_0, every x in O_{L_0} ∩ ... ∩ O_L and every r > 0 there is x' with d(x', x) < r and
      x' in O_{L_0} ∩ ... ∩ O_{L+1}.
Then the intersection of all O_L (L >= L_0) is nonempty.
Proof.  Pick x_1 in O_{L_0} and s_1 in (0, 1] with B[x_1, s_1] ⊂ O_{L_0}.  Given x_i and s_i with B_i := B[x_i, s_i] ⊂
O_{L_0} ∩ ... ∩ O_{L_0+i-1}, (FT) gives x_{i+1} with d(x_{i+1}, x_i) < s_i/2 in the open set O_{L_0} ∩ ... ∩ O_{L_0+i}; choose
s_{i+1} <= s_i/4 with B[x_{i+1}, s_{i+1}] inside that open set (then it is also inside B_i).  The nested closed balls have radii -> 0,
so they meet in one point, which lies in every O_L.  QED
[Only (FT) carries content: each new stage condition must be reachable by an arbitrarily small move from any point satisfying the
earlier ones.  In the design this is the statement that stage-(L+1) data are "fresh": deep coordinates whose effect on the stage <= L
data is far below the tolerances of those (open) conditions.]

LEMMA 2.2 (exact stage equations, triangular tuning).  PROVED.  Let B := prod_{L >= 1} [-1, 1] and, for L >= 1,
      Phi_L(theta) = c_L theta_L + phi_L(theta_1, ..., theta_{L-1}) + psi_L(theta_{L+1}, theta_{L+2}, ...),      c_L > 0,
with |phi_L| <= c_L/2 and |psi_L| <= c_L/4 on B, |phi_L(x) - phi_L(x')| <= Lambda_L max_{L' < L} |x_{L'} - x'_{L'}| and
|psi_L(y) - psi_L(y')| <= sum_{L' > L} eps_{LL'} |y_{L'} - y'_{L'}|.  If there are weights 1 >= w_1 >= w_2 >= ... > 0 with
      w_L Lambda_L <= (c_L/4) min_{L' < L} w_{L'}       and       sum_{L' > L} eps_{LL'} w_L/w_{L'} <= c_L/4      (all L),
then there is theta* in B with Phi_L(theta*) = 0 for every L.
Proof.  Define T: B -> B by forward substitution: (T theta)_L := -(phi_L((T theta)_{<L}) + psi_L(theta_{>L}))/c_L (recursively in L;
|(T theta)_L| <= 3/4).  Put ||x||_w := sup_L w_L |x_L|; (B, ||.||_w) is complete (a ||.||_w-Cauchy sequence converges coordinatewise, and
the coordinatewise limit is its ||.||_w-limit because sup_L w_L |x^n_L - x^m_L| -> 0 passes to the limit in m).  For theta, theta' in B,
with D := ||theta - theta'||_w and D_T := ||T theta - T theta'||_w (finite),
   w_L |(T theta)_L - (T theta')_L| <= (w_L/c_L)[Lambda_L max_{L'<L} |(T theta)_{L'} - (T theta')_{L'}| + sum_{L'>L} eps_{LL'} |theta_{L'} - theta'_{L'}|]
                                   <= D_T/4 + D/4,
so D_T <= D/3: T is a contraction; its fixed point solves c_L theta*_L + phi_L + psi_L = 0 for all L.  QED
[Use: exact resonances at every stage, each tuned by a fresh parameter theta_L with own effect c_L, strong but TRIANGULAR dependence on
earlier (coarser) parameters, and weak (doubly exponentially small Hilbert-footprint) dependence on later (deeper) ones.]

## 2.2 What a persistent (R1) stage needs, in norm-level terms

From H2 Theorem H2.B / H2-ref (necessary conditions at all large main stages), Prop. 4.1, Lemma 5.2 and part 1:
 (C1) a is b(w)-thin on F ∩ [1, D(L)] \ T(L) (H2 Lemma 2.1).  Hence a coordinate s that lies at design depth (s <= D(L)) and off the
      coarse targets at the main stages L in an interval [L_s, L'_s) satisfies |a_s| <= min_{L in [L_s, L'_s)} b(w(L)) (PROVED from H2.B(i)).
      [CORRECTION of a first draft: this does NOT force a_s = 0 off a fixed set, because a signature coordinate s of a stage-L carrier
      becomes a TARGET coordinate of carriers of index >= s at later stages (H2 Lemma 2.2 only says T(l) ∩ union S_k ⊂ [1, l]); so the
      support of a persistent (R1) row may contain such coordinates, thin while they are off the targets.]
 (C2) every kind-(iv) pull range is anti-sign (super-thin support or contacts) (H2 Lemmas 2.3, 2.5).
 (C3) at every stage some block carries a one-signed linear resonance of tiny minors of the wrong sign at the prepared start row
      (Prop. 4.1), fresh at consecutive stages (Lemmas 2.6/2.7); in the restricted single-block model of Example 4.3: two kind-(iv)
      rows l_+ in K^+, l_- in K^- of an unshifted block sharing a coarse target CONTACT j, oriented cofactors C'_+, C'_- > 0, and
      M(rc) > 0 at the prepared row R_1.
 (C4) a mate active on the resonant pair.  By Corollary 1.8 its switching on the pair is of order one only at scales
      t >~ max(|Mj(f)|, U_far)/C_f; below it is pinned with the f-dependent constant C_f/max(|Mj(f)|, U_far).

## 2.3 Tunability of kind-(iv) values in (R1): the natural construction is blocked

LEMMA 2.3 (value decomposition of a carrier at an (R1) row).  PROVED (from the definitions; design facts: u_l = y_l + v_l,
supp y_l ⊂ T(l), Lemma 2.2 of H2, (C1)-(C2)).  At a row satisfying (C1)-(C2) at stage L, for every coarse carrier l,
      u_l(zhat) = Y_l + P_l + E_l,
      Y_l := sum_{s in T(l)} y_l(s) zhat_s                                  (target part; coarse, SHARED coordinates),
      P_l := sum_{s in S_l, s <= D'(L)} v_l(s) z_s                          (private PATTERN part; z_s in {-1, +1} at contacts and support),
      |E_l| <= sum_{s in S_l ∩ F, s <= D'(L)} (mu*_s)^2 v_l(s) |a_s|/nu + ||u_l 1_{(D'(L), inf)}||_1,
for every cut-off D'(L) beyond which no condition is imposed.  At an (R1) stage every private coordinate of a kind-(iv) carrier
in S_l ∩ [1, D(L)] is a contact or thin (<= b) support (no free coordinate: a free private coordinate is an FR generator and makes the
carrier kind (i), K2.16(2a)), so z_s in {-1, +1} there and the Hilbert term is <= b/nu per coordinate.
Proof.  zhat_s = z_s + (mu*_s)^2 a_s/nu (diagonal base); split u_l(zhat) over T(l), S_l ∩ [1, D'], S_l ∩ (D', inf) (T(l) and S_l are
disjoint beyond l by H2 Lemma 2.2, and coordinates of S_l below l lying in T(l) are counted in Y_l).  On S_l ∩ [1, D'] the coordinates
are contacts (z_s = +-1, a_s = 0) or support (z_s = sgn a_s); the Hilbert parts sum to the stated bound.  QED

COROLLARY 2.4 (private resonances are coincidences of discrete data up to the lever scale).  PROVED (the decomposition);
the consequence under (D-pat) is conditional on that design addition.  Consider the Example-4.3 configuration (C3) with
T(l_+) ∩ T(l_-) = {j}, j a contact, and the other target coordinates of l_+- contacts or thin support.  Then
      Mj(f) = u_+(j) u_-(zhat) - u_-(j) u_+(zhat) = u_+(j)(P_- + Y'_-) - u_-(j)(P_+ + Y'_+) + E,
where the y_+-(j) zhat_j terms CANCEL EXACTLY (Mj is invariant under every change of zhat_j: a bank or z-move at the common contact
never acts on the resonance), Y'_+- are target parts over T(l_+-) \ {j} (contact signs), P_+- the private parts, and E collects
Hilbert terms of thin support (<= C D b/nu) and the contributions of coordinates of S_{l_+-} that are not contacts.  Classify the
private coordinates s of S_l (l = l_+-) at an (R1) stage:
  (a) design depth s <= D(L): contacts or thin support (no free coordinate: K2.16(2a) would make l of kind (i));
  (b) mid-deep range D(L) < s with v_l(s) > x'_max: unconstrained by (R1) (beyond design depth, above the pull range);
  (c) pull range and the fully swallowed range [c r, x'_max]: anti-sign contacts (C2);
  (d) v_l(s) < c r: unconstrained, total contribution <= 2 c r.
A FREE coordinate of type (b) with eta_s := 1 - |z_s| and eta_s v_l(s) >= Des^C x is a private two-sided value lever (z-move,
efficiency 1, range eta_s v_l(s) in both directions) whose use costs no more than any other value lever, because Lemma 1.4(c) pins
the mate's usage there: |B_+-(s)| <= t/(2 q_0 eta_s) at every scale [SKETCH: the generator list of K2.9 counts FR coordinates only at
design depth; that this type-(b) coordinate is an admissible generator is a natural extension, not checked against K2/K1].  Granting
it, a kind-(iv) carrier has only free type-(b) coordinates with eta_s v_l(s) < Des^C x, which shift P_l by at most Des^C x each
relative to the contact value sgn(z_s) v_l(s).  Hence
      Mj(f) in Pat(L) + [-C N_L Des^C x, C N_L Des^C x] + [-C D b/nu - 4 c r, C D b/nu + 4 c r],
where Pat(L) is the FINITE set of "pattern minors" u_+(j)(P_- + Y'_-) - u_-(j)(P_+ + Y'_+) over all sign choices on the finitely many
coordinates of types (a), (b) and of T(l_+-) \ {j}, and N_L the number of type-(b) coordinates.  Pat(L) depends only on the design data
of l_+- and of the window (through x'_max).  Consequently, under the design addition
 (D-pat) every nonzero element of Pat(L) has modulus >= Des(L)^{C'} x(w) N_L for every clean sub-window w of L,
a tiny minor of such a pair forces an element of Pat(L) to vanish EXACTLY, and then |Mj(f)| <= C N_L Des^C x: the resonance is
"exact up to the lever scale x" and is a coincidence of discrete design data, not a codimension-one condition on f.
Proof.  Expand Mj using Lemma 2.3; the cancellation is u_+(j) y_-(j) zhat_j - u_-(j) y_+(j) zhat_j = 0 since u_+-(j) = y_+-(j) (j is a target
coordinate outside every signature set).  The classification (a)-(d) is H2 Thm H2.B(i), (C1)-(C2) and the definitions; (d) is bounded by
the tail of v_l below c r (super-geometric).  The bound for nearly-contact free coordinates is |v_l(s) z_s - v_l(s) sgn(z_s)| = eta_s v_l(s).
QED
REMARK 2.5 (on (D-pat); HEURISTIC).  Pat(L) is a finite set of expressions in delta_+-/n_+-, y_+-(.) and signs; an element vanishes
identically only by a relation between delta_+/n_+ and delta_-/n_- with dyadic-rational coefficients, excluded if the signature weights
are algebraically independent over the earlier design data (as T_fin does for the block weights).  The number of patterns is
2^{K_L} with K_L ~ 2 log_2(tail/x'_max)/2^{l+1}; a "random" placement of 2^{K_L} values in [-1, 1] comes within ~2^{-K_L} of 0, which is
>> x(w) ~ T_lo^4 for the sparse signature sets of stage-L carriers.  So (D-pat) is plausible for a generic design with windows fine
enough; it is a design proposal, not checked against every constraint of T_fin^{K2}.

INTERPRETATION (tuning-lever duality; HEURISTIC with PROVED ingredients).  A persistent (R1) row needs at every stage a TINY nonzero
resonance of fresh carriers.  By 2.4, resonances through private data are coincidences of discrete design data up to the lever scale
x; they are not tunable by f.  Any continuous datum of f that can tune the resonance at stage L -- a thick magnitude a_s (Hilbert term
(mu*_s)^2 a_s/nu), a free z_s (shared target or private type (b) with eta_s v >= Des^C x) -- is itself a TWO-SIDED Step-A generator
(TS, FR), and a near-certificate must annihilate it up to eps Design (K2.16(2), (4), (5)): Psi_y(s) = kappa_y a_s at thick s, Psi_y(s) ~ 0 at
free s.  In the restricted model of Prop 4.1 the certificate is (up to scale) the Farkas combination lambda^T C', and its action on a
continuous datum theta is d(lambda^T M)/d theta; so at a residual stage the residual combination lambda^T M is STATIONARY (to O(eps Design))
in every two-sided continuous direction and one-signed in the one-sided ones: f sits at an approximate constrained critical point of
lambda^T M with a tiny critical value.  The tuning freedom that would make the value tiny is exactly the freedom the certificate must
annihilate.  This does not exclude persistence (eps ~ Design^{-C} is not small compared with b, so approximate critical values need not be
design-robust), but it shows that the natural one-parameter tunings are self-defeating: a construction needs, at every stage, at least
two independent continuous data acting on the same resonance (one to make lambda^T M tiny, one to cancel its gradient), i.e. a larger
resonant group sharing coarse target coordinates.  I could not exhibit such a group; the parameter count is not decisive.

LEMMA 2.8 (self-pinning of single-contact pair resonances).  PROVED (any admissible T; the norm-level form of H2 Example 4.3).
Fix a block, a scale t and decompositions as in Corollary 1.3 satisfying (P1) of Lemma 1.7, and two strict non-peak carriers l_+, l_-
with orientations eps_+- and oriented values val_+- := eps_+- u_+-(zhat), val_+ > 0 > val_- (rows of K^+ and K^-).  Let j be a contact,
y_+-(j) := u_+-(j), and E_+- := supp u_+- \ {j}, with E_+ ∩ E_- = {}, every s in E_+- a contact or a support coordinate (no free
coordinate), and V_s = gamma_+- u_+-(s) + psi_s on E_+-; Psi_+- := sum_{E_+-} |psi_s|.  Split E_+- into ALIGNED coordinates A_+- (eps z_s u(s) > 0)
and ANTI-ALIGNED ones R_+- (eps z_s u(s) < 0), with masses N_+- := sum_{A_+-} |u_+-(s)|, F_+- := sum_{R_+-} |u_+-(s)| and cushions
alpha^A_+-, alpha^R_+- (sums of |a_s| over the support coordinates among them).  Let h_+- := eps_+- sum_{s in E_+- ∩ F} u_+-(s)(mu*_s)^2 a_s/nu,
w_+- := N_+- - F_+- + h_+-, gamma'_+- := eps_+- gamma_+- (data-sign switching), S := u_+(zhat) gamma_+ + u_-(zhat) gamma_- (|S| <= S_0(t) by
Lemma 1.7(i) when no other strict non-peak switches), and
      D := val_+ w_- + |val_-| w_+          (the oriented minor of the d-row and the contact row at j).
Then:
 (a) -(2 alpha^A/t + t/(2q_0) + Psi)/N <= gamma'  <=  (2 alpha^R/t + t/(2q_0) + Psi)/F     for each of l_+, l_-;
 (b) z_j V_j = -gamma'_+ D/|val_-| - B S/|val_-| + z_j psi_j,   B := eps_- y_-(j) z_j;
 (c) if D > 0 ("wrong sign"): gamma'_+ <= [t/(2 q_0) + |B| S_0(t)/|val_-| + |psi_j|] |val_-|/D;
 (d) if |D| <= tau, then some l in {+, -} has F_l >= N_l + h_l - tau/v_0, v_0 := min(val_+, |val_-|);
 (e) for that l, with C_v := max(1, val_+/|val_-|, |val_-|/val_+), both data-sign switchings are bounded:
      max(gamma'_+, gamma'_-) <= C_v [ (2 alpha^R_l/t + t/(2 q_0) + Psi_l)/F_l + S_0(t)/v_0 ].
Proof.  (a) is Lemma 1.5 with E = E_+- and orientation o_s = sgn(z_s u(s)): for eps = +1 the aligned set is E^+ and the anti-aligned
set E^-; for eps = -1 the roles are exchanged and gamma' = -gamma; in both cases the bounds read as stated.  (b): at contacts and support
coordinates z_s in {-1, +1}, so sum_{E_+-} eps u(s) z_s = N - F and val_+ = A + w_+, val_- = B + w_- with A := eps_+ y_+(j) z_j
(zhat_j = z_j as a_j = 0, and zhat_s = z_s + (mu*_s)^2 a_s/nu).  From S = val_+ gamma'_+ + val_- gamma'_- we get gamma'_- = (S - val_+ gamma'_+)/val_-,
and z_j V_j = A gamma'_+ + B gamma'_- + z_j psi_j = gamma'_+ (A val_- - B val_+)/val_- + B S/val_- + z_j psi_j with
A val_- - B val_+ = A w_- - B w_+ = val_+ w_- - val_- w_+ = D.  (c): Lemma 1.4(a) at j (budget <= t/(2q_0)).  (d): if both w_+-
are >= 0 then v_0 (w_+ + w_-) <= D <= tau; otherwise some w_l < 0.  (e): the coupling gives gamma'_+ = (|val_-| gamma'_- + S)/val_+, i.e.
each data-sign switching is at most C_v times the other plus S_0/v_0; insert (a) for l.  QED
COROLLARY 2.9 (single-contact resonances are window-pinned at scales above the cushions).  PROVED.  In the setting of 2.8, if the
oriented minor is tiny, |D| <= tau <= v_0 N_l/2 for both l (N_l >= the near mass >= 6/H(L) at an (R1) stage), then at every scale
t >= (8 q_0 alpha^R_l)^{1/2} the whole pair is pinned:
      max(gamma'_+, gamma'_-) <= C_v [ (1 + 1/(2 q_0)) t + Psi_l ] / (N_l/2 - |h_l|) + C_v S_0(t)/v_0 = O(H(L) t) + O(Psi),
a DESIGN-controlled pinning constant (no tiny quantity in the denominator).  Hence a pinned-ratio pair with a tiny minor and only
contact/thin-support coordinates outside the common contact cannot be ACTIVE (above the design pinning threshold of K1 Lemma K1.2)
at any scale t >> (alpha^R)^{1/2}; in (R1) (alpha^R <= #R b) its activity is confined to scales t <~ alpha^R_l H(L) <~ b H(L)
(where thin anti-aligned support acts as a cushion).  An active pair with a tiny minor at larger scales needs coordinates outside j
that are two-sided at those scales -- THICK support (in (R1): thick TARGET coordinates, which are two-sided Step-A generators) -- or
other active carriers switching on E_+- (Psi != 0, a larger resonant group).
Proof.  (d) gives F_l >= N_l - tau/v_0 + h_l >= N_l/2 - |h_l|; in (e), 2 alpha^R_l/t <= t/(4 q_0) <= t when t^2 >= 8 q_0 alpha^R_l.  QED
REMARK.  2.8-2.9 say that H2's Example 4.3, read at the level of the norm with private coordinates only, is never an ACTIVE residual:
the same anti-aligned mass that makes the minor tiny pins the pair (and a robust wrong-signed minor pins it by (c)).  So the residual
of Prop. 4.1 can be realized only (i) at scales below the thin anti-aligned cushions, or (ii) with thick shared target support in
supp u_+-, or (iii) in larger groups.  Case (ii) brings in two-sided TS generators (tuning-lever duality above); (i) requires the class
to live at scales <= b H(L), i.e. at the bottom of the window.  This sharpens the target of a persistent-residual construction.

THEOREM 2.10 (switching inequality in an unshifted block).  PROVED (any admissible T, any row, any mate, any scale).  Fix a block
satisfying (P1) at scale t (Lemma 1.7), decompositions as in Corollary 1.3, a set G of strict non-peaks of the block, and put
r_Q := |sum_{k in Q \ G} u_k(zhat) gamma_k|.  Let J_c be ANY set of contacts.  For k in G define the off-J_c value
      Rt_k := u_k(zhat) - sum_{j in J_c} u_k(j) z_j      (= sum over s notin J_c of u_k(s) zhat_s),
and put Psi_J := sum_{j in J_c} |psi_j| with psi_j := V_j - sum_{k in G} u_k(j) gamma_k (carriers outside G, peaks included).  Then
      sum_{k in G} gamma_k Rt_k  <=  E(t) := S_1(t) + r_Q + t/(2 q_0) + Psi_J,                                  (2.1)
S_1(t) := (sigma/q_0)[ t max(1, 1/sigma) + eta_P (1 + M Phi_P^2/C) ] (Lemma 1.7(i)).
Proof.  Lemma 1.7(i) (Steps 1-2 of its proof, which use only (P1)) gives |sum_{k in Q} u_k(zhat) gamma_k| <= S_1(t), hence
|sum_{k in G} u_k(zhat) gamma_k| <= S_1 + r_Q.  Lemma 1.4(a) at each j in J_c: z_j V_j >= -(e_j^+ + e_j^-)/(2t); summing over J_c and using
sum_j (e_j^+ + e_j^-) <= t^2/q_0: sum_{k in G} gamma_k sum_{j in J_c} u_k(j) z_j + sum_j z_j psi_j >= -t/(2 q_0).  Subtract.  QED
Note: (2.1) is invariant under the choice of orientations, involves no minor, and holds for every J_c (the contact rows enter only
summed).  It is the scale-t, quantitative form of U3's exact rigidity (Lemma S, Corollaries S1, S2).

COROLLARY 2.11 (no switching through contacts in an unshifted block).  PROVED.  In the setting of 2.10 assume that every coordinate
of supp u_k \ J_c (k in G) is PRIVATE to k (up to psi) and is a contact, a free coordinate, or a support coordinate of cushion <= alpha.
Let P_k := sum_{s in supp u_k \ J_c} |u_k(s)| (private mass), h_k the Hilbert terms of Lemma 2.8 (|h_k| <= alpha P_k max(mu*)^2/nu), and
assume P_k/3 > |h_k|.  For a free coordinate s put eta_s := 1 - |z_s|.  Then for every k in G
      |gamma_k|  <=  C_G [ E(t) + sum_{k' in G} (2 alpha/t + t/(2 q_0) + Psi_{k'}) ] / min_{k' in G} ( P_{k'}/3 - |h_{k'}| ) ,
with C_G <= 3 + 3 max_k (P_k + |h_k|)/P_k and Psi_k the psi-mass on the private coordinates of k, as soon as the free coordinates satisfy
eta_s |u_k(s)| >= P_k/3 or carry no mass (otherwise replace P_k/3 by the free-coordinate pinning constant of Lemma 1.4(c)).
Hence at every scale t >= (2 alpha)^{1/2} the whole set G is pinned with a constant that depends only on the private masses P_k
(design quantities: P_k >= the near mass >= 6/H(L) for a coarse carrier) and on C_f -- never on a minor.
Proof.  Fix k and let eps := sgn gamma_k.  Split the private coordinates of k into ALIGNED (eps z_s u_k(s) > 0, mass N) and ANTI-ALIGNED
(mass F); N + F = P_k (free coordinates aside).  If F >= P_k/3, Lemma 1.5 (with E^- the anti-aligned set) gives
|gamma_k| <= (2 alpha/t + t/(2q_0) + Psi_k)/F <= 3(2 alpha/t + t/(2 q_0) + Psi_k)/P_k.  Otherwise N - F > P_k/3 and
gamma_k Rt_k = |gamma_k| eps Rt_k = |gamma_k| (N - F + h_k) >= |gamma_k| (P_k/3 - |h_k|) (eps Rt_k = N - F + h_k because zhat_s = z_s + h-terms on
private coordinates).  Let G_1 be the carriers of the first kind and G_2 the others.  By (2.1),
sum_{G_2} |gamma_k|(P_k/3 - |h_k|) <= E(t) - sum_{G_1} gamma_k Rt_k <= E(t) + sum_{G_1} |gamma_k| (P_k + |h_k|), and the G_1 terms are bounded
by the first case.  Free coordinates: Lemma 1.4(c) bounds |V_s| <= (e_s^+ + e_s^-)/(t eta_s), i.e. |gamma_k| <= t/(2 q_0 eta_s |u_k(s)|) + |psi_s|/|u_k(s)|.
QED
INTERPRETATION.  In an unshifted block, strict non-peaks can switch with more than O(t) amplitude only if some switching carrier k
has, in the switching direction, a NEGATIVE off-contact value eps_k Rt_k < 0 that is carried by TWO-SIDED coordinates: shared
non-contact coordinates (thick support, shared free coordinates) or private THICK support -- or thin support at scales below its
cushion.  [Shifted blocks escape through the peak traces: (P1) fails and S_1 contains Delta d.]  Consequences:
 (a) H2's Example 4.3 (Lemma 2.8) is the case |J_c| = 1: the pair is pinned whatever the sign or size of its minor (2.8(c) when D > 0;
     2.11 when D <= 0).  So the configuration "active pinned kind-(iv) pair in a one-signed resonance at a single common contact" is
     EMPTY above the thin-cushion scale.
 (b) At an (R1) stage (no thick private coordinates, Fact 1.1; design-depth support off the targets thin), active kind-(iv) rows of
     an UNSHIFTED block switch only through SHARED THICK TARGET coordinates (or shared free targets, or thin support below its cushion
     scale).  Those are two-sided TS/FR generators of Step A, so by K2.16(2),(4) every near-certificate is annihilated by them up to
     eps Design: Psi_y(s) = kappa_y a_s at shared thick targets.  Persistent (R1) in unshifted blocks therefore needs, at every stage,
     fresh kind-(iv) rows switching through shared thick target support -- the "resonance carried by the base support" configuration.
 (c) (H1's (R0)) thick-type rows switch through their thick PRIVATE coordinates: consistent with 2.11.
 (d) Numerics (part 3, selfpin.out): contact or thin anti-aligned mass pins the pair (slope ~14-21 in t), thick anti-aligned support
     frees it -- as predicted.

## 2.4 The adversarial configuration that remains (SKETCH)

DEFINITION (stage configuration RC_L; adversarial target).  At main stage L: an unshifted (U)-block m with a private two-sided peak
resource; two FRESH coarse carriers l_+ in K^+, l_- in K^- (kind (iv): near coordinates N_l = data-sign contacts; pull ranges and the
range [c r, c_0 W] anti-sign contacts, i.e. fully swallowed, no pull capacity, H2 5.3); a common target contact j; two further
target coordinates s_1* in T(l_+), s_2* in T(l_-) carrying THICK support (tuning coordinates) and shared with fresh auxiliary
carriers k_1, k_2 of other blocks whose rows enter the certificate with the coefficients needed for the s*-equations; the oriented
minor Mj(R_1) at the prepared row in (delta_Z, C b] with C'_+-> 0 (wrong sign) -- or Mj(f) = 0 exactly (bias type: H2 Lemma 5.2 pushes
it to >= c theta_0/Design^C at R_1).
PERSISTENCE (SKETCH).  Choose the RC_L successively.  The open conditions (signs, statuses, "tiny and of the wrong sign") are kept by
Lemma 2.1; for the exact version (bias type), Lemma 2.2 with theta_L := the magnitudes a_{s*_i(L)} (own effect c_L ~ (mu*_{s*})^2 v/nu,
a design-size number at stage L), strong triangular dependence phi_L on the earlier (coarser) tuning parameters, and cross effects
eps_{LL'} (L' > L) bounded by the Hilbert footprints (mu*_s)^2 a_s/nu of the stage-L' tuning coordinates on stage-L values, doubly
exponentially small because those coordinates lie at depth > D(L) (cluster sweep, H2 Lemma 2.3: s_max(L+1) >= 4/T_lo(L)).  The
weight conditions of Lemma 2.2 then hold if eps_{LL'} decays faster than the products of c_i/(4 Lambda_i), i <= L' -- plausible, not
checked.  NOT verified: that the auxiliary carriers k_i and blocks can be chosen
without creating relief elsewhere (new thick-type carriers (R0), anchors K2.17(b), two-sided private coordinates), that the
certificate exists for every clean sub-window and class (the class depends on the mate), and that a mate g in C(f) is active on all
the pairs (C4).  The construction is therefore a SKETCH of an adversarial row, not a construction.

## 2.5 Dangerous mates exist as limits (PROVED, given approximants)

LEMMA 2.6 (upper semicontinuity of the fibre map).  PROVED.  If f_n -> f in S_{p*}, g_n in C(f_n) and g_n -> g in norm, then g in C(f);
and every sequence g_n in C(f_n) has a norm-convergent subsequence (global compactness, Preprint A Thm 2.1 / Part I).
Proof.  ||(f_n, g_n)|| <= 1 and the operator norm is continuous, so ||(f, g)|| <= 1; with p*(f) = 1 this is g in C(f).  Compactness is
the cited global compactness theorem.  QED
COROLLARY 2.7 (construction of dangerous mates).  PROVED (conditional).  Let f satisfy RC_L with Mj(f) != 0 at every large stage, and
let f^(n) -> f be rows that agree with f except that the stage-L_n minor is EXACT (Mj = 0), each carrying a mate g^(n) with exact
two-piece data that switches through the pair of stage L_n with amplitude >= c_0 (e.g. Prop II-NTM-type data).  Then every limit g of
g^(n) lies in C(f).  By Corollary 1.8 g is pinned on the stage-L pair below max(|Mj(f)|, U_far)/C_f, and by continuity of the
decompositions in (f, g) at fixed scale [compactness of the decomposition sets at fixed t] its switching on the pair at scales
t >> |Mj_L(f)| is close to that of g^(n) for the stages where f^(n) and f agree.
Remark (transitivity).  If the rows f^(n) were in Rec, then (f, rho g) would be in cl NA by closedness of cl NA (the pairs
(f^(n), rho g^(n)) are in cl NA and converge to (f, rho g)).  So the natural dangerous mates are recovered as soon as the
exactly-resonant approximants are recovered; the adversary needs the approximants to be residual too -- which is the bias type of
RC (H2 Lemma 5.2).  Hence persistent residual rows come in families: wrong-signed rows are limits of exactly-resonant (bias-type)
rows, and both are outside the current chain.
