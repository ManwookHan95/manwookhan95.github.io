# V1 part 2 — Clean sub-windows: classification, pinning at f, donors, shift control, patterns and rays

Setting: D_Omega (part 1), N >= 1, f in S_{p*} with F finite and forced data (xi, q_0, a, w, F, z, zhat, e, nu); zeta_m := R_m^** zhat,
A_m := |zeta_m|_m = sigma_m/q_0, theta_m := A_m M_m/C_m, nu_k := |zeta_m(k)|/Phi_m(k)^2, rho_l := nu_{k(l)}/theta_{m(l)}; peak iff rho >= 1
(Lemma T of Y1/Y2); margin mu = q_0 Phi theta (rho - 1)/m on P_m; gap = M(1 - rho) on Q_m; eq:margin sigma_m |alpha_m(k)| = lambda_k mu_k.
g in C(f), eta <= eta_* with eta_Gamma(eta) <= 1, t <= min(t_eta, 1) dyadic, (B_+-, Theta_+-) a two-sided decomposition of g at scale t,
Delta theta_l := lambda_l (Theta_+ - Theta_-)_{m(l)}(k(l)), Delta B = -sum_l Delta theta_l u_l (eq:DeltaB), Delta d_m := d_{+,m} - d_{-,m}.
"f-constant": depends only on f, N (and g, rho where said), not on l, w, t.  C_f denotes f-constants (changing from line to line).
l_f: an f-dependent level threshold, enlarged finitely many times below (each time by a condition depending only on f).

## 2.1 Theorem 2' (clean sub-windows).  PROVED.
For every f (any F) and every level l there is i in {1..M(l)} such that w = (l,i) is CLEAN: no rate object of level l (part 1, 1.3)
has its value in Band(w) = (b(w), u(w)); so every rate of level l is TINY (<= b(w)) or ROBUST (>= u(w)).
Proof.  The omega(l) values each lie in at most one of the M(l) = omega(l)+1 pairwise disjoint bands (Theorem 1'(b)).  QED
Scale relations at a sub-window w of level l (Theorem 1'): for t in W(w): t >= T_lo(w), b(w) Design(l) <= t^4/l, sum_{l'>l} lambda_{l'}
<= b(w)^2/2, and T_hi(w) <= 1/Q(w) <= (u(w)/(4 Design(l)))^{omega(l)+20}.                                                  (2.1)

## 2.2 Classification at a clean sub-window (Y1 part 3; refereed)
Fix a clean w = (l,i), l >= l_f >= max F.  Since rho and |rho - 1| are rate objects ((R3), (R4)) and b(w) < u(w) <= 1/4, every coarse
carrier l'' <= l has rho in [0, b] ∪ [u, 1-u] ∪ [1-b, 1+b] ∪ [1+u, infinity) (b = b(w), u = u(w)).
 * class R: (R1)-rate >= u;  class G: (R1)-rate <= b, with eps_{l''} the minimizing sign of r^nat (unique: the two signed rooms sum to
   2||v 1_{S^nat}||), and tau_{l''} := -eps_{l''} Delta theta_{l''}; G(w) := class-G carriers <= l.  q_{l''} := eps Phi w_m(k)/(m C_m);
   swallowing type if eps sgn w_m(k) = +1 (q > 0), anti type if = -1 (q < 0), d-neutral if w_m(k) = 0 (then rho = 0).
 * ONE-SIGNED blocks (Y1 Lemma 3.6): Sigma_m(w) := coarse G-carriers of block m that are swallowing-type peaks, or strict non-peaks with
   rho > b (hence rho >= u) which are not anti-type with rho >= 1-b; block m is sigma-ONE-SIGNED at w if sgn q = sigma on Sigma_m(w).
 * DROPPED set P(w) ⊂ G(w): (P-i) anti-type peaks; (P-ii) anti-type strict non-peaks with rho >= 1-b; (P-iii) swallowing-type peaks with
   rho >= 1+u; (P-iv) Sigma_m(w) for every block m that is one-signed at w.  KEPT set Kp(w) := G(w) \ P(w), consisting of
   (K1) swallowing-type strict non-peaks with rho in [u, 1-u];  (K2) anti-type strict non-peaks with rho in [u, 1-u];
   (K3) carriers with rho <= b (any type, incl. d-neutral);  (K4) swallowing-type carriers with rho in [1-b, 1+b] (strict non-peaks,
   weak peaks, DEGENERATE peaks) — (K1), (K2), (K4) only in blocks that are not one-signed at w; in one-signed blocks only (K3) is kept.
 * Target coordinates j in T(l) \ F: CONTACT-LIKE if 1 - |z_j| <= b (contacts and tiny rooms), FREE-ROBUST if 1 - |z_j| >= u.
(This is exactly Y1's kept/dropped classification, Y1 part 3, Summary; donors are not added to P(w) — they are dropped or class R anyway.)

## 2.3 Pinning at f under a shift bound (Y1 Lemmas 3.1, 3.2, 3.3, 3.5; refereed, constants as corrected by Y1-ref m5)
Put D := D(l), u := u(w), K_g := (1/q_0 + 1) D/u.  Suppose a SHIFT BOUND |Delta d_m| M_m <= K_d' t holds for every block m.  Then:
 (3.1) sum_{l'' in class R} |Delta theta_{l''}| <= K_g t;
 (3.2) sum_{l'' in G(w)} (tau_{l''})_- <= K_g t, and e_0 := Delta B 1_{F^c} - sum_{G(w)} eps tau u 1_{F^c} has ||e_0||_1 <= K_g t + 4b^2/t;
 (3.5) |tau_{l''}| <= K_P t on (P-i)-(P-iii), K_P := K_g + K_d' + C_f D^2/u;   (3.1') fine carriers: sum_{l''>l} |Delta theta_{l''}| <= 3b^2/t <= t^7;
 (3.6) |tau_{l''}| <= K_O t on (P-iv), K_O := C_f D^2 (K_g + K_P)/u.
Proofs: Y1 Lemmas 3.1, 3.2, 3.5, 3.6 (Lemmas 3.5, 3.6 use the shift only through |Delta d| M <= K_d' t, Y1-ref m2; P-ii by Lemma 3.5(b),
P-iii by 3.5(c) with 1/mu <= m D/(q_0 theta u); P-iv by Lemma 3.6, which uses |q| >= Phi M u/(mC) on Sigma_m(w)).  (3.1), (3.2) need no shift bound.

## 2.4 Lemma D (robust-margin peaks; DONORS exist in every block).  PROVED.
There is l_f such that at every clean w of level l >= l_f every block m in I has a coarse peak k = k(c), c <= l, with rho_c >= 1+u(w)
(hence non-degenerate, margin mu_k >= q_0 theta_m u(w)/(m D(l))).  Every such c is DROPPED or of class R; it is PINNED:
|Delta theta_c| <= max(K_g, K_P, K_O) t under the shift bound ((3.1), (3.5), (3.6)).
Proof.  Fix m.  By Lemma lem:threshold, sum_{k in P_m} |alpha_m(k)| = 1.  Coarse peaks with rho <= 1+b: by eq:margin and the margin
formula, |alpha(k)| = lambda_k mu_k/sigma_m <= m Phi_k (q_0 Phi_k theta_m b/m)/sigma_m, so their total is <= (q_0 theta_m/sigma_m) b sum Phi^2
<= (M_m/(4C_m)) b (q_0 theta_m/sigma_m = theta_m/A_m = M_m/C_m, sum_k Phi_m(k)^2 <= 1/4).  Fine peaks (carrier > l): mu_k <= |u_k(xi)|
<= q_0 ||zhat||_inf <= 2 q_0, so their total is <= 2 q_0 sum_{l''>l} lambda_{l''}/sigma_m <= q_0 b^2/sigma_m.  Take l_f so large that
(M_m/(4C_m)) b + q_0 b^2/sigma_m < 1 for every m and every w of level >= l_f (b(w) <= 2^{-l^3}).  Then some coarse peak has rho > 1+b,
hence rho >= 1+u at a clean w.  It is class R, or class G anti type (P-i), or class G swallowing type with rho >= 1+u (P-iii).  QED
Every block therefore has a donor candidate at every clean sub-window of large level; this is what removes the aligned corner (part 5).

## 2.5 Shift control: sources (Y1) or shift cost (port of Y2 Section 5)
Sources (Y1 part 3, refereed).  UPPER source of block m at w: (U1) a class-R peak; (U2) an anti-type G-peak; (U3) every q < 0 carrier
of G(w) in block m is an anti-type peak, an anti-type strict non-peak with rho >= 1-b, or has rho <= b.  LOWER source: (L1) a class-R
peak with rho >= 1+u; (L2) a swallowing-type G-peak with rho >= 1+u; (L3) every q > 0 carrier of G(w) in block m has rho <= b.
Lemma 3.4' (Y1 Lemma 3.4 read half by half; Y1-ref (b)).  PROVED.  An upper source gives Delta d_m M_m <= K_d t, a lower source gives
Delta d_m M_m >= -K_d t, K_d := C_f D(l)^3/u(w).  (The proof of each half uses only its own source, Lemmas (3.1), (3.2), 3.3, the
pinned DROPPED anti-type carriers via Lemma 3.3(b) and Lemma suplevel(f) — not the other half.)
SHIFT PATTERNS.  A shift pattern of level l is pi = (I_up, I_lo, P*, vs, Bf, eps) with I_up, I_lo disjoint sets of blocks of carriers
<= l, P* ⊂ [1,l] with m(P*) ⊂ I_up ∪ I_lo, vs in {+-1}^{P*}, Bf ⊂ [1,l] \ P*, eps in {+-1}^{Bf}.  Put Pi_m := sum_{l'' in P*, m(l'')=m}
vs_{l''} lambda_{l''} u_{l''} 1_{F^c} and, for delta in R^{I_up ∪ I_lo},
   c(delta; pi) := inf_{x in [0,inf)^{Bf}} sum_{j notin F} phi_{z_j}( sum_m delta_m Pi_m(j) + sum_{l'' in Bf} x_{l''} eps_{l''} u_{l''}(j) ),
   c_pi := inf{ c(delta; pi) : ||delta||_1 = 1, delta_m >= 0 (m in I_up), delta_m <= 0 (m in I_lo) }   (c_pi := +infinity if I_up ∪ I_lo = {}).
(phi_z(x) = |x| - zx.  The series converge: sum_l lambda_l ||u_l||_1 < infinity, x ranges over a finite-dimensional cone.  c(.; pi) is
convex, positively homogeneous and finite, as a partial infimum of such a function; Y2 5.2, refereed.)  These are the rate objects (R6).
The shift pattern of f at w: I_up(w) := blocks without an upper source, I_lo(w) := blocks without a lower source, P*(w) := coarse peaks of
blocks in I_up(w) ∪ I_lo(w) with rho >= 1+u, vs := sgn w_m(k), Bf(w) := G(w) \ P*(w) with the class-G signs.
(SH_w): I_up(w) ∪ I_lo(w) = {}, or c_{pi(w)} >= u(w).   [At a clean w, NOT (SH_w) iff I_up ∪ I_lo != {} and c_{pi(w)} <= b(w).]

**Lemma S (shift pinning at a clean sub-window).  PROVED.**  Let w be clean of level l >= l_f.  (a) I_up(w) ∩ I_lo(w) = {} and
P*(w) ⊂ G(w).  (b) If (SH_w) holds, then |Delta d_m| M_m <= K_d' t for every block m, with K_d' := C_f l D(l)^3/u(w)^2.
Proof.  (a) If m in I_up ∩ I_lo, then (U1), (U2), (L2) fail, so every coarse peak of block m is a class-G swallowing-type peak with
rho in [1, 1+b], contradicting Lemma D.  A class-R peak with rho >= 1+u is a source of both kinds ((U1), (L1)), so blocks of
I_up ∪ I_lo have none: P*(w) ⊂ G(w).
(b) If I_up ∪ I_lo = {}, Lemma 3.4' gives |Delta d_m| M_m <= K_d t.  Otherwise c := c_{pi(w)} >= u.  For a peak k = k(l'') of block m,
eq:peakshift gives -Delta theta_{l''} = vs_k lambda_{l''} (Delta d_m M_m + e_k), e_k := |omega_{+,m}(k)| + |omega_{-,m}(k)| >= 0, and
e_k <= t/(sigma_m |alpha_m(k)|) = t/(lambda_k mu_k) for alpha(k) != 0; on P*(w), mu_k >= q_0 theta_m u/(m D).  Split
Delta B 1_{F^c} = sum_{l''} (-Delta theta_{l''}) u_{l''} 1_{F^c} according to l'' in P*(w), l'' in Bf(w) (class G, -Delta theta = eps tau =
eps (tau)_+ - eps (tau)_-), class R, fine.  For m in I_up (lower source present) put delta_m := (Delta d_m)_+ M_m >= 0, and
(Delta d_m)_- M_m <= K_d t; for m in I_lo put delta_m := -(Delta d_m)_- M_m <= 0, (Delta d_m)_+ M_m <= K_d t (Lemma 3.4').  Then
   Delta B 1_{F^c} = sum_m delta_m Pi_m + sum_{l'' in Bf} (tau_{l''})_+ eps_{l''} u_{l''} 1_{F^c} + R,
   ||R||_1 <= t sum_{P*} 1/mu_k + K_d t sum_m ||Pi_m||_1 + sum_G (tau)_- + sum_R |Delta theta| + sum_{fine} |Delta theta|
          <= C_f l D t/u + K_d t + 2 K_g t + t
(||u||_1 <= q*(u) = 1, ||Pi_m||_1 <= sum lambda <= 1/3, (3.1), (3.2), (3.1')).  By Lemma lem:switchbudget, sum_{j notin F}
phi_{z_j}(Delta B(j)) <= t/q_0; by Lemma lem:phicalc(c), phi_z(x + r) >= phi_z(x) - 2|r|; x := (tau)_+ >= 0 is admissible in the infimum and
delta lies in the sign cone, so  c ||delta||_1 <= c(delta; pi(w)) <= t/q_0 + 2||R||_1.  Hence ||delta||_1 <= C_f (l D/u + K_d + K_g + 1) t/u,
and |Delta d_m| M_m <= |delta_m| + K_d t <= C_f l D^3 t/u^2.  QED
Consequently, under (SH_w), the shift bound of 2.3 holds with K_d' = C_f l D^3/u^2, (3.5) holds with K_P <= C_f l D^3/u^2 and (3.6)
with K_O <= C_f l D^5/u^3.

## 2.6 Patterns, zero-cost cones and ray components (rate objects (R5), (R7))
A PATTERN of level l is kappa = (U, P, eps, F', type): U ⊂ [1,l], P ⊂ U, eps in {+-1}^U, F' ⊂ T(l), type : T(l) \ F' -> {+1,-1,0}
(Y1's generalized configuration).  With L_j(tau) := sum_{l'' in U} eps_{l''} tau_{l''} u_{l''}(j) (design numbers u_{l''}(j)), its
ZERO-COST CONE is
   C(kappa) := {tau in R^U : tau_{l''} >= 0 (l'' in U \ P); tau_{l''} = 0 (l'' in P); type(j) L_j(tau) >= 0 (type(j) = +-1);
                L_j(tau) = 0 (type(j) = 0), j in T(l) \ F'}.
C(kappa) ⊂ [0, inf)^U is a pointed polyhedral cone; Ext(kappa) denotes its extreme rays normalized by ||r||_1 = 1, so C(kappa) =
cone(Ext(kappa)) (Minkowski-Weyl).  Y1's polyhedron Z_kappa(beta) is C(kappa) ∩ {|tau_{l''}| <= beta_{l''}}.
The PATTERN OF f AT w: kappa(w) := (G(w), P(w), eps, F ∩ T(l), type_w), type_w(j) := sgn z_j if j is contact-like, 0 if free-robust.
For r in Ext(kappa(w)) and a block m meeting supp r, the d-COMPONENT is D_{r,m}(f) := sum_{l'' in supp r, m(l'')=m} r(l'') val_{l''},
val_{l''} := eps_{l''} u_{l''}(zhat); its (R5)-rate is |D_{r,m}|/Phi_max(r,m), Phi_max(r,m) := max_{l'' in supp r, m(l'')=m} Phi_{l''}.
At a clean w each component is TINY (rate <= b(w)) or ROBUST (rate >= u(w)).
(VR_w): every r in Ext(kappa(w)) has at most one ROBUST component.
Remarks.  (1) Why values: at a strict non-peak, q_{l''} = val_{l''}/A_m (Z6 2.1; Y4-ref C.7: q = q_0 val/sigma_m), so the d-row of block m
on C(kappa) is tau -> (1/A_m) sum_{l'' in block m} val_{l''} tau_{l''}, and D_{r,m}/A_m is the d-sum of the ray r in block m.  For a
(K4) peak of f the d-coefficient at f is Phi M/(mC) = val/(rho A) with rho in [1, 1+b]: relative difference <= b.
(2) Single-block rays: if supp r lies in one block, (VR_w) holds for r automatically.  If N = 1, (VR_w) always holds.  In a block that is
one-signed at w every kept carrier has rho <= b, so |val| <= b Phi theta/m and EVERY component in that block is tiny: one-signed blocks never
carry robust components.  Dropping more carriers only helps: C(kappa) ∩ {tau_{l''} = 0} is a face of C(kappa) (C(kappa) ⊂ orthant), and
the extreme rays of a face are extreme rays of C(kappa).
(3) (VR_w) is a property of f at level l and of the explicit numbers b(w), u(w); it involves no rate threshold beyond them.
