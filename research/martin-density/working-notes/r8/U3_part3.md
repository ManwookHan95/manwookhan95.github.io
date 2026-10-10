# U3 part 3 — Explicit non-(BT) first rows in (C*): the nested-tuning rows f^infty; their mates and their recovery

Design: an SLD-type design with V4's (SF*), (SF_tau), (b'), (Z0) (V4 Lemma 2.1: designable; V4-ref: compatible in appearance with
D_Omega / D^{V2}, not checked line by line — this compatibility is ASSUMED here and flagged); diagonal base; N = 1 (Remark 3.6 for
N >= 2).  F = {p, p', p''} ⊂ Z_0, sigma = (+,+,+), y* = (e_p^* - e_{p'}^*)/q*(e_p^* - e_{p'}^*) a target of the family (Z0).
Owner rule (V4 Construction SA, step (2)): carriers in increasing order; A_l := sum_{j in supp y_l assigned} y_l(j) zhat_j,
B_l := sum_{j in supp y_l unassigned} |y_l(j)|; a carrier with sign eps_l sets z_j := eps_l sgn y_l(j) at its unassigned target
coordinates and z := eps_l on S_l; then n_l val_l = A_l + eps_l (B_l + delta_l H_l) (V4 Lemma 1.1).  OWNER sign: eps_l := sgn A_l
(+1 if A_l = 0); then |n_l val_l| = |A_l| + B_l + delta_l H_l and the carrier is an aligned robust peak (V4 Theorem 2.2 Step 4).
ANTI-OWNER sign: eps_l := -sgn A_l; if |A_l| < B_l + delta_l H_l the value keeps the sign eps_l (still ALIGNED: z = sgn val on S_l)
and |n_l val_l| = B_l + delta_l H_l - |A_l| can be made as small as desired by tuning A_l.

## 3.1 Theorem NT (non-(BT) rows in (C*)).  Existence: SKETCH (nested tuning; every step is a finite-dimensional continuity /
## implicit-function argument, written below in outline).  Properties (b)-(e) of the constructed row: PROVED.
There are a in A_sigma, a carrier l_- with target y*, an infinite set Lambda = {l_1 < l_2 < ...} of carriers and a sign vector
z in {-1,1}^{N \ F} such that the row f^infty with forced data (a, z) satisfies:
 (a) every coordinate off F is a contact (maximal contact); every carrier l notin Lambda ∪ {l_-} carries the OWNER sign;
 (b) l_- carries eps = +1 with n val_{l_-} in (-eta, -eta/2) for a fixed small eta: an exactly swallowed anti-type strict non-peak,
     q_{l_-} < 0, relative position rho_{l_-} <= 1/2 (gap >= M/2), and u_{l_-} 1_{F^c} = v_{l_-} is z-signed;
 (c) every l_i in Lambda carries the ANTI-OWNER sign with |A_{l_i}| < B_{l_i} + delta_{l_i} H_{l_i}: an exactly swallowed ALIGNED
     (swallowing-type, q > 0) strict non-peak with relative gap g_i := 1 - nu_{l_i}/theta in (0, Phi_{l_{i+1}}/2);
 (d) Q = {k_-} ∪ {k(l_i) : i >= 1} is infinite, there is no degenerate peak, so f^infty is NOT (BT); and the block fails (SC):
     Scr(s) >= s for every 0 < s <= Phi_{l_1};
 (e) (C*): at every clean sub-window w of every large level, rho^sh(kappa(w), f^infty) = 0 and c_{pi(w)}(f^infty) = 0.
Construction (outline).  Parametrize A_sigma by b in the open positive orthant Omega of S^2 (d = 3).  Stage 0: by the intermediate
value theorem on the ratio a_p/a_{p'} (V4 Theorem 2.2 Step 1) choose a closed ball B_0 ⊂ Omega on which y*(zhat_F) + delta_{l_-} H_{l_-}
in (-eta, -eta/2) (an open condition; l_- late enough, as in V4).  Stage i -> i+1: we hold a closed ball B_i, a level L_i, the carriers
l_1 < ... < l_i, such that (I1) every carrier l <= L_i has constant owner data (eps_l and assigned/unassigned status of its target
coordinates) on B_i, (I2) all values val_l, l <= L_i, are continuous on B_i, (I3) the non-special carriers <= L_i are aligned robust
peaks and l_1, ..., l_i satisfy (c) on B_i with a provisional gap bound g_i < 2 gamma_i (gamma_i to be fixed at the next stage), (I4)
the carriers > L_i change theta by at most L_Theta 2(1 + ||U||) sum_{l > L_i} lambda_l, which is < gamma_i theta/8 on B_i (Lemma 5.2 of V4:
theta is Lipschitz in zeta).  (i) Pick a vector c in R^F with <c, Phi(b)> = 0 at the centre b^(i) of B_i and with tangential
gradient (s_j c_j)_j independent of the tangential gradient of nu_{l_i} - theta at b^(i) (d - 1 = 2); by (T-d) pick a target r of the
family with q*(y^(r) - c/q*(c)) tiny, and enlarge L_i so that the owners of the finitely many coordinates of supp y^(r) \ F are
<= L_i (shrinking B_i so that (I1) persists: only finitely many owner signs are involved, none with A_l = 0 at b^(i) after an
arbitrarily small move of b^(i)).  Then for every later carrier l using target r, B_l = 0 and A_l = y^(r)(zhat) =: psi_r, a function
on B_i with non-vanishing gradient and |psi_r(b^(i))| tiny.  (ii) Choose such a carrier l_{i+1} > L_i with delta H small enough that
the hypersurface {psi_r = -delta_{l_{i+1}} H_{l_{i+1}}} passes through B_i near b^(i) (implicit function theorem), and give it the
anti-owner sign eps = +1 (so A = psi_r < 0 there and n val = psi_r + delta H in (0, B + delta H)).  (iii) By transversality, the
region of B_i where both g_i in (0, Phi_{l_{i+1}}/2) and n val_{l_{i+1}} in (n theta Phi_{l_{i+1}}(1 - 2 gamma_{i+1})/m, n theta Phi_{l_{i+1}}
(1 - gamma_{i+1})/m) is a non-empty relatively open set (both conditions are thin one-sided neighbourhoods of two transversal
hypersurfaces through points close to b^(i)); choose gamma_{i+1} small, B_{i+1} a closed ball inside it, and L_{i+1} >= l_{i+1} so large
that (I4) holds with gamma_{i+1}, shrinking B_{i+1} to keep (I1).  Then (I1)-(I4) hold at stage i + 1.  Finally b^infty in ∩ B_i, and
z := the owner data of all carriers at b^infty (constant by (I1) along the nest), with the anti-owner sign on Lambda and +1 on l_-.
Proof of (b)-(e) given (a)-(c) at b^infty.  (b), (c): by (I3) and continuity at b^infty (the shell inequalities are strict on each
B_i ⊃ B_{i+1} ∋ b^infty, and the threshold error of (I4) is < gamma theta/8).  (d): Q is as stated; no peak has nu = theta (non-special
peaks have nu >= 2^10 theta beyond the first carrier, V4 Step 4, and the first carrier is a robust peak; specials are strict
non-peaks).  For 0 < s <= Phi_{l_1} pick i with Phi_{l_{i+1}} <= s <= Phi_{l_i} (Phi_{l_i} -> 0); then gap_{l_i} = M g_i < Phi_{l_{i+1}} <= s, so
the strict non-peak l_i contributes min(Phi_{l_i}, s) = s to Scr(s) (Definition def:SC), whence Scr(Upsilon s)/s >= 1 for every
Upsilon >= 1 and (SC) fails.  (e): fix a clean w of a large level l and its closed pattern kappa.  All carriers are exactly swallowed,
so every coarse carrier is of class G (room 0) and there is no class-R carrier; the coarse peaks are the non-special carriers <= l
(swallowing type, relative positions >= 1 + u for large l), the coarse G strict non-peaks are l_- (anti-type, robust) and the
special l_i <= l (swallowing type, near-threshold or robust).  Hence there is no UPPER source ((U1), (U2) fail; (U3) fails because of
l_-) and there is a LOWER source (L2): I_sh = I_up = {1}.  Take delta := 1, tau_c := lambda_c for every coarse G-carrier c other than l_-,
and tau_{l_-} := (1 + sum_{c != l_-} q_c lambda_c)/|q_{l_-}| > 0 (all q_c > 0 for swallowing-type carriers).  (R1): tau >= 0.  (R2): at a
swallowing-type peak eps vs = +1, tau_c = lambda_c delta.  (R4): delta + sum q tau = 1 + sum_{c != l_-} q_c lambda_c - (1 + sum ...) = 0.
(R5) void, (R6): delta >= 0 (lower source only), (R7) void (no anti-type near-threshold carrier).  (R3): V(tau) = sum_{c coarse,
c != l_-} lambda_c eps_c u_c 1_{F^c} + tau_{l_-} v_{l_-}; every coordinate j in T(l) \ F is owned by a coarse carrier o (the first
carrier touching j is <= the carrier whose target contains j); if o != l_-, its term lambda_o eps_o u_o(j) has the sign z_j (owner
rule for non-special o; for special o, z = eps_o on S_o and eps_o sgn y_o on its unassigned coordinates by construction) and
dominates the later coarse terms, whose coefficients are lambda_c with c > o and which never include l_- (supp u_{l_-} = F ∪ S_{l_-}),
by the dominance estimate of V4 Theorem 2.2 Step 6 (moduli only; it uses (SF*) and allowedness (b)); if o = l_-, j in S_{l_-}, the
term tau_{l_-} v_{l_-}(j) > 0 = z_j-signed dominates likewise.  So V(tau) is z-signed and non-zero on T(l) \ F: all contact rows hold, and
there are no free rows.  The violation is 0 with ||delta||_1 = 1, so rho^sh = 0.  For V1's c_pi: with delta = 1 and x := (lambda_c)
on Bf(w) ∪ {l_-}-type carriers the vector sum_m delta_m Pi_m + sum x eps u is supported on coordinates owned by coarse carriers (a
coordinate owned by a fine carrier is touched by no coarse carrier) and z-signed there by the same dominance: c(1; pi) = 0.  QED
Remarks.  (1) The special carriers are needed only to break (BT) and (SC); the coherent resonance comes from the aligned owner
structure and the single q < 0 carrier l_-, exactly as in V4's self-aligned rows.  (2) Every nested choice is finite-dimensional;
the only infinite object is the limit, and all conditions are strict inequalities preserved along the nest.  This is why the
existence part is labelled SKETCH rather than PROVED: the bookkeeping (I1)-(I4) is not written out coordinate by coordinate.
(3) By Corollary FZ (Part 2), every tilting perturbation of a in the fixed-z fibre of f^infty leaves (C*); the rows f^infty are
"isolated" in their fibre in this sense, and the (C*) property is carried by the joint choice (a, z).

## 3.2 Proposition NT-M (explicit coherent-shift mates of f^infty).  PROVED (given Theorem NT (a)-(c)).
Put psi := R^* w.  (i) psi 1_{F^c} is z-signed and non-zero at every coordinate off F ∪ S_{l_-}; on S_{l_-}, z psi < 0.  (ii) For every
finite Omega ⊂ Q containing k_-, every omega^+ supported in Omega, every Dom supported in Omega with Delta := d(Dom) < 0 and
eps_k Dom(k) >= 0 for k in Omega \ {k_-}, Dom(k_-) chosen so that lambda_{l_-}(Dom(k_-) - Delta w(k_-)) > 0, every split
chi : F^c -> [0,1] and every beta supported in F with (beta + chi v 1_{F^c})(zhat) = 0, the pairs
   omega^- := omega^+ + Dom,  v := R^* Dom - Delta psi,  b^+ := chi v 1_{F^c} + beta,  b^- := b^+ - v
are two-piece data (Delta^{data} = Delta < 0) for g := b^+ + R^*(omega^+ - d(omega^+) w).  (iii) c g in C(f^infty) for all small c > 0.
(iv) The profile pi_g(s) = g(s)/psi(s) on S_l (l a non-special carrier) equals -d(omega^+) + chi_s |Delta| exactly; it is
non-constant whenever chi is.
Proof.  (i) Dominance at every coordinate owned by a carrier o != l_- (owner sign or aligned special sign, |w(o)| >= M/2 > 0 since
specials are near-threshold: |w(o)| = M nu/theta >= M(1 - g_o)); on S_{l_-}, w(k_-) < 0 = -z.  (ii) Lemma A of Part 2: off F,
v = R^* Dom - Delta psi; at coordinates owned by k in Omega \ {k_-} the owner coefficient lambda_k (Dom(k) - Delta w(k)) has the sign
eps_k (both terms do: -Delta > 0 and sgn w(k) = eps_k) and dominates; on S_{l_-} the coefficient lambda_{l_-}(Dom(k_-) - Delta w(k_-)) > 0
= z; elsewhere v = -Delta psi is z-signed by (i).  So v is z-signed off F, b^+ is z-signed, b^- = (chi - 1) v 1_{F^c} + (beta - v 1_F) is
(-z)-signed, both vanish nowhere required (no free coordinates); b^+ - b^- = v = R^*(omega^- - omega^+) - Delta psi, so both pairs
represent g; g(xi) = q_0 b^+(zhat) = 0 by the choice of beta (Lemma lem:algebra for the block parts).  (iii) Proposition
prop:onesidedupper on both sides gives p*(f + r g) <= 1 + (r^2/2)(kappa_w + 1) for |r| <= r_0(g); for |rc| >= r_0 use p*(f + rcg) <=
1 + |r| c p*(g) and s(r) - 1 >= min(r^2, |r|)/3 (V4 Proposition 3.2(iv)).  (iv) At s in S_l, l non-special, s notin Sigma(omega):
g(s) = chi_s v(s) - d(omega^+) psi(s) and v(s) = -Delta psi(s).  QED

## 3.3 Corollary NT-R (the exact-data mates of f^infty are recovered).  PROVED modulo V4 Theorem 5.6 (refereed) and the design
## assumption.
Every mate of f^infty carrying two-piece data with kappa_w <= 1, Delta < 0, omega-carriers Omega as in 3.2 and V4's coefficients gamma_k := lambda_k (Dom(k) - Delta w(k)) != 0 on Omega
is in cl NA((c_0, p_1), l_2^2) jointly with f^infty; in particular all mates of 3.2(iii).
Proof.  V4 Theorem 5.6 (N = 1: Delta d < 0 in every block).  (H1): no carrier is neutral (|w(k)| >= min(M rho_{l_-}, M/2) > 0 for every
k; peaks |w| = M); a carrier k notin Omega is negligible iff |gamma_k| = lambda_k |Delta| |w(k)| < 2 tau_k C_1 lambda_k = 2 tau_k |Delta| lambda_k,
i.e. |w(k)| < 2 tau_k, which happens for at most finitely many k since tau_k -> 0 and |w(k)| is bounded below.  (H2): E = ⋃_{k in Omega}
supp y_k \ F is finite; on the coordinates of E' owned by Omega-carriers the owner coefficient is non-zero (3.2(ii): Dom(k) and -Delta w(k) have
the same sign, so |Dom(k) - Delta w(k)| >= |Dom(k)|) and dominates (Lemma 4.1' of V4 with the design thresholds), so D(j) != 0
there; on E itself D(j) = v(j) != 0 unless an exact cancellation occurs, which is removed by an arbitrarily small change of Dom (finitely
many linear conditions).  V4 Lemma R10 (maximal contact) is satisfied.  QED
So the dangerous explicit mates of the non-(BT) (C*) rows f^infty — oscillating profiles on robust class-G peak signature sets, forced
shift Delta < 0, no (SC) at f^infty — are recovered, through V4's (BT) companions (fine re-alignment + bank levers), not through windows.

## 3.4 The general mate of f^infty.  SKETCH (route complete in outline; one assembly step not written line by line).
Let g in C(f^infty) be arbitrary and rho < 1.  The window machinery applies with one change: in case (II) the transplant does not
need a Hoffman projection onto a shifted cone, because Lemma A + 3.2(ii) show that at f^infty EVERY coarse switching pattern obeying the
sign rows (R1) on Omega and every Delta <= 0 is realized by exact two-piece data, with omega-carriers = the coarse strict non-peaks used.
Steps.  (1) Window certificate with shift: at a scale t of a clean sub-window w, a two-sided decomposition (B_+-, Theta_+-) of g gives
omega_+- (clamped on coarse strict non-peaks with gap >= t^2, Definition def:windowcert), Delta := d(omega^-) - d(omega^+) (equal to
-(d_+ - d_-) + O(t/sigma), Lemma lem:suplevel(d)), and v := R^*(omega^- - omega^+) - Delta psi.  The lower source (L2) gives
Delta d^{dec} M >= -K t (V1 Lemma 3.4'), so Delta <= C K t; replace Delta by min(Delta, 0) through Dom(k_-) (cost O(K t)).  The (R1)
defects ((tau)_- <= K_g t on G strict non-peaks, Y1 Lemma 3.2) are removed by moving Dom on Omega by O(K t / lambda) (cost O(K t) in
l_1).  Coarse near-threshold carriers pushed beyond their gaps are handled as in V1's Proposition TR (kind [3], inward moves need no gap:
Z3 Lemma 5.1, Y2 Lemma U'(ii)).  DEAD ZONES (an Omega-carrier whose coefficient Dom(k) - Delta w(k) vanishes) are removed by the BUMP of
Lemma 3.5 below.  The split chi is read off ΔB by Lemma lem:split.  This yields exact data at f^infty for g_t with ||g - g_t||_1 <= K_w t,
K_w = Design u^{-O(1)} C_f (as in Proposition windowcert(c), plus the shift column, whose coefficient is controlled by Lemma 3.1 of V2).
(2) Average the data over the dyadic scales of w (exactness and Delta <= 0 are preserved; kappa_w is convex).  (3) Transplant the
averaged data to V4's (BT) companion f_w := (f^{(L)})^#(mu) (fine re-alignment beyond L >> l + bank levers; Lemmas 5.4, 5.5 of V4,
whose hypotheses (H1), (H2) hold as in 3.3), with p*(f_w - f^infty) <= C_f sum_{l' > L} lambda_{l'} log = o(T_lo(w)^2).  (4) f_w is (BT), so
(SC) holds at f_w; Theorem E^SC of V2 (Z3 Theorem E with Delta d < 0 data and (SC) at the companions) gives (f^infty, rho g) in cl NA.
What is not written out: the window arithmetic of step (1) with the shift column (the constants K_w), which is V1's Proposition TR
with one extra column; nothing new is needed there since no Hoffman constant of a shifted cone enters (exact data exist for every
sign-admissible pattern).  Hence: f^infty in Rec (SKETCH).  In the language of Part 4: for f^infty step (S1) holds (N = 1 and l_- has
its target on F, so its column is a free ray of the zero-cost cone), and only step (S2) — the uniform composition (S2a)-(S2d) of Part 4.3' (Lemma VT itself is PROVED at a single stage, Part 4.2) — is
unwritten.

## 3.5 Lemma (dead-zone bump).  PROVED (any SLD-type design with allowedness (b); one block; F finite).
Let (b^+-, omega^+-) be two-piece data at f, k in Omega a strict non-peak with S_k ∩ F = {} and exactly swallowed signature (z = eps_k
on S_k), and suppose the coefficient c_k := lambda_k (Dom(k) - Delta w(k)) of u_k in v vanishes.  For kappa > 0 replace Dom(k) by
Dom(k) + eps_k kappa (and omega^-(k) accordingly), keep side +, re-split chi on supp u_k.  Then the new pairs are two-piece data for a
functional g' with ||g' - g||_1 <= 2 lambda_k kappa (1 + |d-change| C), Delta changes by eps_k kappa Phi_k^2 w(k)/C, and on S_k the new v is
z-signed and non-zero as soon as kappa lambda_k v_k(s) exceeds the modulus of the later-carrier terms at s, which by allowedness (b) holds
for all s in S_k once kappa >= kappa_k := C_data 2^{m + k_k - min S_k} (C_data a bound for the data coefficients of later carriers).
Proof.  Direct: v_new = v + eps_k kappa lambda_k u_k - (Delta_new - Delta) psi; on S_k the term eps_k kappa lambda_k v_k(s) has the sign z_s
and, against the later terms (at most C_data 2^{-2s} c_k delta_k by allowedness (b)) and the psi-correction (of size |Delta_new - Delta|
|psi(s)| = O(kappa Phi_k^2) lambda_k v_k(s)), dominates under the stated bound.  The functional changes only through the re-split on
supp u_k and the d-change.  QED
Since kappa_k is super-exponentially small in min S_k, dead zones on the signature sets of omega-carriers cost nothing.  Dead zones
at coordinates owned by a PEAK of a block with Delta_m = 0 cannot be bumped (peaks carry no omega): this is the multi-block residual of
Part 4.

## 3.6 Remark (N >= 2).
Take the construction in block 1 and owner-aligned blocks 2..N without exceptional carriers.  Blocks 2..N then have an UPPER source
((U3) is vacuous: no q < 0 carrier) and a LOWER source (L2), so I_sh = {1}, and (e) holds with delta_m = 0 for m >= 2 — but now every
coordinate owned by a carrier of blocks 2..N is a DEAD ZONE for the block-1 shift (Lemma A with W_Delta = Delta_1 psi_1): the
block-1 resonance is z-signed there only if the later block-1 terms are coherent with z, which the construction does not ensure.  If
they are coherent (choose the block-1 targets hitting block-2 signature sets with the right signs — a condition on the row, not the
design), (e) holds; whether all mates are then recovered is exactly the multi-block dead-zone question of Part 4.
