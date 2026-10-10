# U3 part 2 — What (C*) forces, and why the Baire-generic perturbations of self-aligned rows leave (C*)

Setting: design D^{V2} on V1's D_Omega with diagonal base U (U^* e_j^* = s_j kappa_j), finite I, F finite; V2's residual
(C*) = "at all but finitely many levels EVERY clean sub-window w has rho^sh(kappa(w), f) <= b(w) AND c_pi(w) <= b(w)".
Notation as in Part 1; for an SLD-type design u_k = (y_k + delta_k h_k)/n_k, v_k = delta_k h_k/n_k.

## 2.1 Lemma D' (shape of a source-deficient block).  PROVED (V1 Lemma D + V1 Lemma S(a), refereed).
At every clean sub-window w of level l >= l_f, every block has a coarse peak with relative position rho >= 1 + u(w).  If block m
has no UPPER source at w, then every coarse peak of block m with rho >= 1 + u(w) is a class-G SWALLOWING-type peak; if block m
has no LOWER source at w, every such peak is a class-G ANTI-type peak.  (A class-R peak with rho >= 1 + u is a source of both
kinds; a class-G anti-type peak is (U2); a class-G swallowing-type peak with rho >= 1 + u is (L2).)
So in a (C*) block, at all large levels, every robust coarse peak is (relative room <= b(w) on its natural signature set) of ONE
type: the self-aligned rows of V4 (all peaks swallowing-type) are the model of an UPPER-deficient block (configuration (i),
Delta^{data} < 0), the "anti-aligned" rows the model of a LOWER-deficient block (configuration (ii)).

## 2.2 Proposition FZ (fixed-z perturbations create both kinds of exactly swallowed robust peaks).  PROVED.
Let T be ANY admissible operator, U diagonal, F finite with d := |F| >= 2, sigma in {-1,1}^F, z in B_{l_inf} with z = sigma on F,
A_sigma := {a : supp a = F, sgn a = sigma, q*(a) = 1}, f_a the row with forced data (a, z) (Remark rem:lemmaZ(c)).  For a in A_sigma
put nu(a) := ||U^* a||, b(a) := (s_j a_j)_{j in F}/nu(a) and Phi(a) := (sigma_j + s_j b_j(a))_{j in F} in R^F, so that zhat(a)_j =
Phi(a)_j on F and zhat(a)_j = z_j off F.  Let a_0, a_1 in A_sigma with Phi(a_0), Phi(a_1) not positively proportional.  Then there is
eta > 0 such that every block m contains infinitely many carriers k with
     val_k(a_0) >= eta/2 and val_k(a_1) <= -eta/2,
and infinitely many carriers k' with val_{k'}(a_0) >= eta/2 and val_{k'}(a_1) >= eta/2  (val_k(a) := u_k(zhat(a))).
Proof.  For a in A_sigma, b_j(a) = s_j a_j/nu(a) has the sign sigma_j, so Phi(a)_j = sigma_j (1 + s_j |b_j(a)|): every Phi(a) lies in
the OPEN orthant of the signs sigma, and <Phi(a_0), Phi(a_1)> > 0.  Since Phi(a_0), Phi(a_1) are not positively proportional, the closed
rays R_+ Phi(a_0), R_+ Phi(a_1) meet only at 0 and are not opposite, so they are strictly separated by a hyperplane through 0: there is
c in R^F with <c, Phi(a_0)> > 0 > <c, Phi(a_1)>.  Put c' := Phi(a_0).  Let y_0 := c/q*(c), y'_0 := c'/q*(c') (vectors supported in F);
for y supported in F, y(zhat(a)) = <y, Phi(a)> (diagonal base: (Ue)_j = s_j^2 a_j/nu = s_j b_j on F and 0 off F).  Put
eta := min(<y_0, Phi(a_0)>, -<y_0, Phi(a_1)>, <y'_0, Phi(a_0)>, <y'_0, Phi(a_1)>) > 0.  By (T-d) every tail of (u_{k,m})_k is q*-dense in
S_{q*}, so there are carriers k_i -> infinity of block m with q*(u_{k_i} - y_0) < eta/2, and likewise k'_i for y'_0.  Since
q**(zhat(a)) = 1, |u(zhat(a)) - y(zhat(a))| <= q*(u - y) for every a and every u, y in l_1.  QED
(Whether Phi(a_0), Phi(a_1) are positively proportional is a codimension-(d-1) coincidence; for a_1 on a curve through a_0 in a
generic direction it fails for all a_1 != a_0 near a_0.)

## 2.3 Corollary FZ (fixed-z perturbations of aligned rows leave (C*) and are recovered).  PROVED modulo the refereed Master
Theorem II/III' (V1, V2).
Let T = D^{V2} on D_Omega, U diagonal, F finite, d >= 2, and let f_0 = f_{a_0} be a row such that in every block
all but finitely many carriers k are EXACTLY SWALLOWED WITH THE SIGN OF THEIR VALUE (z = sgn val_k(a_0) on S_k; S_k ∩ F = {} for large
k by allowedness (a)) — e.g. the self-aligned rows of V4 Theorem 2.2 and the rows f^infty of Part 3.  Then for every a_1 in A_sigma with
Phi(a_1) not positively proportional to Phi(a_0), the row f_{a_1} (same z) has, in EVERY block, infinitely many exactly swallowed
robust anti-type peaks and infinitely many exactly swallowed robust swallowing-type peaks.  Consequently, at every clean sub-window
of every sufficiently large level, every block has an UPPER source (U2) and a LOWER source (L2); hence (SP_w) holds, Y1/V1's shift
pinning applies, rho^sh(kappa(w), f_{a_1}) >= 1 (V2 Theorem C1, case (I)), f_{a_1} is NOT a (C*) row, and f_{a_1} in Rec (Master Theorem
III').
Proof.  Proposition FZ: carriers k_i of block m have val(a_0) >= eta/2, hence (hypothesis) z = +1 on S_{k_i}, while val(a_1) <= -eta/2:
at f_{a_1} they are exactly swallowed (room 0 on every natural signature set, so class G at every level) with w = -M: anti-type; as
|val(a_1)| >= eta/2 and Phi_{k_i} -> 0, nu = m|val|/Phi -> infinity relative to the (fixed) threshold of f_{a_1}: peaks whose relative
position rho = nu/theta exceeds 1 + u(w) at every clean w of large level (u(w) -> 0).  The carriers k'_i are exactly swallowed robust
swallowing-type peaks in the same way.  A fixed carrier, once coarse, stays coarse; so for all large levels the closed pattern of every
clean w contains, in every block, a class-G anti-type peak (U2) and a class-G swallowing-type peak with rho >= 1 + u (L2).  V2's Theorem
C1 (whose case (I) contains (SP_w), V2-ref verdict table) and Master Theorem III' (f in Rec if infinitely many levels have a clean w
with rho^sh >= u or (SH_w); (SP_w) is (SH_w) with I_up ∪ I_lo = {}) give the claims.  QED
Consequences.  (a) (C*) is NOT open in any fixed-z fibre: it is destroyed by every perturbation of a that tilts Phi.  V4's Baire-generic
near-threshold rows (Proposition 5.1) of a self-aligned fibre are recovered by the window method, not residual.  The task's
suggested construction ("perturb self-aligned rows Baire-generically so that (BT) fails while (C*) persists") therefore does not
work in fixed-z fibres; a (C*) row must keep every robust peak of a deficient block aligned (or anti-aligned) at all fine levels, which
forces z to be re-aligned together with a (Part 3).
(b) Along f_{a_1} -> f_{a_0} (a_1 -> a_0 in a tilting direction), the oscillating coherent-shift mates of f_{a_0} are generically lost:
whenever f_{a_1} is a row at which every mate carries two-piece data (e.g. a (BT) row in the fibre), Proposition S3 applies (its
anti-type peaks provide anti-aligned contacts outside Sigma_n).  For rows of the fibre that are not (BT) this is the window version of
the same mechanism (Y1 Lemma 3.3(b): an anti-type G-peak bounds Delta d_m M_m <= (tau)_-/lambda <= K t/lambda), i.e. the shift is pinned
and Proposition C4 of V2 kills the oscillation at all scales of all large windows.  So the fibre map is not lower semicontinuous at
f_{a_0} along fixed-z perturbations either (HEURISTIC for non-(BT) f_{a_1}; PROVED for (BT) ones by Proposition S3).

## 2.4 Lemma A (what an exact shifted datum needs, one block).  PROVED (N = 1, any admissible T).
Let f have F finite.  Two-piece data with Delta != 0 and omega-carrier set Omega exist for SOME functional only if, outside Sigma(omega):
(i) psi = R^* w vanishes at every free coordinate, and (ii) z_j psi(j) has the sign of -Delta... precisely z_j Delta psi(j) <= 0 at every
contact j (Lemma S(b),(c)).  Conversely, if (i), (ii) hold for some Delta < 0 (resp. > 0) and some finite Omega ⊂ Q with omega-differences
chosen so that psi-terms on Sigma(omega) are z-signed, then for every omega^+ supported in Omega, every split chi in [0,1]^K and every base
part beta on F there are two-piece data with these parameters; they represent h = b^+ + R^*(omega^+ - d(omega^+) w).
Proof.  Necessity is Lemma S.  Sufficiency: put omega^- := omega^+ + gamma with gamma supported in Omega and d(gamma) = Delta (possible
if some k in Omega has w(k) != 0; d(e_k) = Phi_k^2 w(k)/C), v := R^* gamma - Delta psi, b^+ := chi v 1_{K} + beta, b^- := b^+ - v; then b^+ is
z-signed and b^- is (-z)-signed on K iff v is z-signed on K, v vanishes off F ∪ K iff it vanishes at free coordinates; off Sigma(omega),
v = -Delta psi, so (i), (ii) are exactly these conditions there, and on Sigma(omega) they are the stated choice.  The pairs represent the
same h since b^+ - b^- = v = R^*(omega^- - omega^+) - Delta psi.  QED
Reading.  For N = 1 the existence of shifted exact data is a property of (f, Omega) alone: psi must be "Omega-coherent" (zero at free
coordinates and of the sign -sgn(Delta) z at contacts, outside Sigma(omega)).  For an owner-aligned row psi is z-signed at every
coordinate whose owner has w != 0 (dominance, V4 Theorem 2.2 Step 6); so the only obstructions are (a) free coordinates outside the
omega-supports, (b) contacts whose owner is NEUTRAL (w = 0) or anti-aligned ("dead zones", V4 Section 12), and (c) the sign of Delta
(configuration (i) needs psi z-signed, configuration (ii) needs psi (-z)-signed).  With several blocks, psi is replaced by W_Delta =
sum_m Delta_m psi_m and blocks with Delta_m = 0 contribute nothing at the coordinates they own: every coordinate owned by a carrier of an
UNSHIFTED block is a dead zone for the shifted blocks.  This is the structural core of (C*-1).
