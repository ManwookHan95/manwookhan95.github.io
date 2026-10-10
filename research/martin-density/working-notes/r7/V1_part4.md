# V1 part 4 — Transplant at the assembled companion, Theorem E'', and the MASTER THEOREM II

Setting of parts 2-3: D_Omega, F finite, g in C(f), clean w = (l,i), l >= l_f, companion f^# = f^#_w (part 3) with forced data
(xi^#, q_0^#, a^#, w^#, F^#, z^#, zhat^#, e^#, nu^#); F^# = F ∪ Ba ∪ Pu, Ba := bank coordinates (donor banks s_m in case (b) of (C3) and
tuning banks j'_{l''}), Pu := pull coordinates j_{l''} (l'' in L_0).  t in W(w) dyadic, t <= min(t_eta, 1); (B_+-, Theta_+-) a two-sided
decomposition of g at f at scale t.  D := D(l), u := u(w), b := b(w), Lam := T_lo(w)^3.

## 4.1 Proposition TR (transplant at the assembled companion).  PROVED.
Assume (SH_w) and (VR_w).  Then there is g_t carrying d-NEUTRAL two-piece data (b^+-, omega^+-) AT f^# (Definition def:twopiece read at
f^#, with base support F^#) such that
 (i)   b^+-(xi^#) = 0, t||b^+-||_1 <= A_0 (an f-constant), and Gamma^#_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta) + C theta_w) + K_w t)^2;
 (ii)  p*(g - g_t) <= K_w t with K_w <= C_f Design(l) u(w)^{-4};
 (iii) every k in supp omega^+-_m satisfies, at f^#, one of: [1] gap^#(k) >= t^2 and |omega(k)| <= 2 gap^#(k)/t; [2] gap^#(k) >= gamma(w) :=
       min_m M_m u(w)/4 and |omega(k)| <= A_2/t; [3] k is a strict non-peak of f^# with the inward sign (vs_k omega^+(k) <= 1.5 gap^#(k)/t,
       vs_k omega^-(k) >= -1.5 gap^#(k)/t, vs_k := sgn w^#_m(k)) and |omega(k)| <= A_2/t;  A_2 := 22;
 (iv)  b^+- are contact-like on Ba (z^#_j b^+_j >= 0 >= z^#_j b^-_j) and t |b^+-(j)| <= |a^#(j)| for j in Pu.
Proof (modification of Y1 Proposition 5.2, refereed; every departure is marked NEW).
Step 0 (pinning at f).  By (SH_w) and Lemma S, |Delta d_m| M_m <= K_d' t, K_d' <= C_f l D^3/u^2; so 2.3 gives (3.1), (3.2), (3.5), (3.6)
with K_P <= C_f l D^3/u^2, K_O <= C_f l D^5/u^3, K_g <= C D/u.
Step 1 (zero-cost projection; Y1 Step 1 verbatim with kappa^# := kappa(w)).  Let tau := (tau_{l''})_{l'' in G(w)} and beta_{l''} :=
12 lambda_{l''}/t.  On T(l) \ F, Delta B(j) = L_j(tau) + e_0(j).  Violations of the rows of Z_{kappa(w)}(beta) by tau: (Z1) sum (tau)_- <= K_g t;
(Z2) at contact-like j, (type_w(j) L_j(tau))_- <= phi_{z_j}(Delta B(j)) + |e_0(j)| (for type = sgn z_j: phi_z(x) >= (sgn z * x)_-), at
free-robust j, |L_j(tau)| <= phi_{z_j}(Delta B(j))/u + |e_0(j)| (Lemma lem:phicalc(a)); summed <= (t/q_0)(1 + 1/u) + 2||e_0||_1;
(Z3) sum_{P(w)} |tau| <= l (K_P + K_O) t; (Z4) |tau| <= 6 lambda/t (Lemma lem:box): none.  Total V_w <= C_f l^2 D^5 t/u^3.  By the definition of
G**(l) (Hoffman, right-side independent) there is tau_0 in Z_{kappa(w)}(beta) with ||tau - tau_0||_1 <= G**(l) V_w.
Step 2 (d-rows at f^#).  Q^#_m(tau') := sum_{l'' in Kp(w), m(l'')=m} q^#_{l''} tau'_{l''} = (1/A^#_m) sum val^#_{l''} tau'_{l''} (Lemma ST(d)).
By eq:didentity at f (a G-carrier contributes Phi w Delta theta/(mC) = -q tau), (3.1), (3.1'), (3.5):
|sum_{Kp, m} q tau| <= |Delta d_m| M_m + C(K_g + 1) t/C_m + 2t/sigma_m + l (K_P + K_O) t/C_m.  At kept strict non-peaks of f, q = val/A_m; at kept (K4)
peaks of f, q = Phi M/(mC) = val/(rho A_m) with rho in [1, 1+b] (part 2, Remark (1)); with |val^# - val| <= 2 Design b (Lemmas CO, TU),
|q^# - q A_m/A^#_m| <= C_f Design b at every kept carrier.  Hence |Q^#_m(tau_0)| <= K_Q t, K_Q := C_f (K_d' + K_g + l (K_P + K_O) + G** V_w/t)
<= C_f G** l^2 D^5/u^3 (the term l Design b * 12/t^2 <= t^2 is absorbed).
Step 3 (exact d-repair by RAY REMOVAL; NEW, replaces Y1 Step 3 and the hypotheses (Cmp_w), (NN_w)).  tau_0 in C(kappa(w)), so tau_0 =
sum_{r in Ext} mu_r r with mu_r >= 0 (Minkowski-Weyl).  At f^#, the d-vector of a ray r is (D^#_{r,m}/A^#_m)_m; by Lemma RR every component
is 0 (tiny at f, or block not met) or robust, |D^#_{r,m}| >= u Phi_max(r,m)/2 >= u/(2D); by (VR_w) every r has at most one nonzero
component, in a block m(r) (m(r) undefined if all vanish).  For each block m put tau^(m) := sum_{m(r)=m} mu_r r, e_m := Q^#_m(tau^(m)) =
Q^#_m(tau_0) (rays with m(r) != m have zero m-component).  Lemma 1.8 of Y4 (ray removal; refereed) applied to the cone cone{r : m(r) = m}
⊂ [0,inf)^G, the vector tau^(m) and the functional Q^#_m gives tau'^(m) with 0 <= tau'^(m) <= tau^(m) coordinatewise, tau'^(m) in that cone,
Q^#_m(tau'^(m)) = 0 and ||tau^(m) - tau'^(m)||_1 <= |e_m| 2 D A^#_m/u.  Put tau' := sum_{m(r) undefined} mu_r r + sum_m tau'^(m).  Then
tau' in C(kappa(w)) (a convex cone), 0 <= tau' <= tau_0 coordinatewise (box rows kept), Q^#_{m'}(tau') = Q^#_{m'}(tau'^(m')) = 0 for EVERY
block m', and ||tau_0 - tau'||_1 <= 2 N D max_m A^#_m K_Q t/u.  Consequently, with V' := sum_{Kp} eps tau' u 1_{F^c},
   ||Delta B 1_{F^c} - V'||_1 <= ||e_0||_1 + ||tau - tau'||_1 <= K_U t,   K_U := K_g + 1 + G** V_w/t + C_f N D K_Q/u <= C_f G** l^2 D^6/u^4.
Zero cost (NEW bookkeeping for pulls/banks): for j notin F^#, V'(j) is z^#-signed and V' vanishes at free coordinates of f^#: on
S^nat_{l''}(l) only u_{l''} lives among coarse carriers and z^# = eps_{l''} there off F^# (Lemma ST(e); tau' >= 0 on kept, = 0 on dropped
carriers); on T(l) \ F the rows (Z2) of kappa(w), whose types are those of f^# (Lemma ST(e)); elsewhere off F every coarse class-G vector
vanishes (supp u_{l''} ⊂ supp y_{l''} ∪ S_{l''} and S_{l''} \ S^nat_{l''} ⊂ F ∪ T(l)).  Moreover V' is z^(2)-signed and supported in K^(2) :=
{j notin F : |z^(2)_j| = 1} (z^(2) = the sign vector before the pulls): at pulls and tuning banks z^(2) = eps_{l''} (closed by (C1)); at donor
coordinates s_m, V'(s_m) = 0 (c_m notin Kp(w)).
Step 4 (split w.r.t. z^(2); NEW choice of sign vector).  Lemma lem:split with z^(2) in place of z (its proof uses only Lemma lem:phicalc(b)
and the summed budget) applies once sum_{j notin F}[phi_{z^(2)_j}(B_+(j)) + phi_{-z^(2)_j}(B_-(j))] <= C_S t: off the coordinates modified by
(C1)-(C3), phi_{z^(2)} = phi_z (budget t/q_0); at raised coordinates ((C2), and (C1) with z_s eps >= 0) phi_{z^(2)} <= 2 phi_z (Z3 Lemma 3.2,
referee's definition of flipped); at flipped (C1) coordinates (z_s eps < 0) and at the s_m, phi_{z^(2)}(x) <= 2|x| and |B_+(j)| + |B_-(j)| <=
|Delta B(j)| + phi_{z_j}(B_+(j)) + phi_{-z_j}(B_-(j)); on S^nat_{l''} the flipped v-mass is <= r^nat_{l''} <= b, so sum_{flipped} |Delta B| <=
l (6/t) b + 4b^2/t <= t^2, and |Delta B(s_m)| <= K_P t + t^7 (only the pinned donor and fine carriers live at s_m).  So C_S <= C(1 + N K_P), and
B_+ 1_{F^c} = chi V' + e_+, B_- 1_{F^c} = -(1 - chi) V' + e_-, ||e_+-||_1 <= (K_U + C(1 + N K_P)) t.
Step 5 (data at f^#; NEW balancing and supports).  Define
   omega^+_m := clamp of omega_{+,m} with gap^# (Definition def:windowcert at f^#) at coarse strict non-peaks of f^# that are not k(l''),
   l'' in Kp(w); 0 at peaks of f^#; omega^+_m(k(l'')) := omega_{+,m}(k(l'')) for l'' in Kp(w);
   omega^-_m := omega^+_m + sum_{l'' in Kp, m(l'')=m} (eps tau'_{l''}/lambda_{l''}) e_{k(l'')};
   b^+ := B_+ 1_F + chi V' - kappa a/a(zhat^#),  kappa := (B_+ 1_F + chi V')(zhat^#)   (Y4-ref B.4: balance with the ORIGINAL a);
   b^- := b^+ - sum_{Kp} eps tau' u;    g_t := b^+ + sum_m R_m^*(omega^+_m - d^#_m(omega^+_m) w^#_m),
and at kept (K4) coordinates apply the SHIFT TRICK (Y1 Step 5, Y1-ref (d)): move omega^+-(k) by the same x with vs x := (-1.5 gap^#(k)/t
- vs omega^-(k))_+.  [a(zhat^#) = ||a||_1 + nu^2 (nu^2 + ||X||^2)^{-1/2} in [1 - ||X||^2/nu, 1] by (3.1), X the total off-F mass vector.]
 * Two-piece admissibility at f^#: off F^#, b^+ = chi V' and b^- = -(1-chi) V' are z^#- resp. (-z^#)-signed in K^# and vanish at free
   coordinates (Step 3); on F^# no condition; omega^+- are finitely supported in the strict non-peak sets of f^# (Lemma ST(c): every kept
   carrier is a strict non-peak of f^#).  Second representation: b^+ - b^- = sum_{Kp} eps tau' u = sum_m R_m^*(omega^-_m - omega^+_m).
   d-neutrality: d^#_m(omega^-) - d^#_m(omega^+) = sum_{Kp, m} (eps tau'/lambda) Phi^2 w^#(k)/C^# = Q^#_m(tau') = 0 (Step 3).  The shift leaves
   omega^- - omega^+ unchanged.  b^+(zhat^#) = kappa - kappa = 0, and b^-(xi^#) = g_t(xi^#) = b^+(xi^#) = 0 (Lemma lem:algebra at f^#).
 * (iv): at j in Pu (j = j_{l''}), V'(j) = eps tau'_{l''} v_{l''}(j) (only l'' lives there among coarse carriers), so t|b^+-(j)| <= t tau' v(j) <=
   12 lambda v(j) = mu_{l''}/2 <= |a^#(j)| (q*(A^#) <= 2) — this is Y4-ref Lemma P3; at tuning banks V'(j') is z^(2)-signed and z^(2)_{j'} =
   z^#_{j'}, so b^+ = chi V' and b^- = -(1-chi)V' are contact-like; at donor coordinates s_m, b^+- = 0.  The term kappa a/a(zhat^#) lives on F.
 * Estimates (ii): g - g_t = (e_+ + kappa a/a(zhat^#)) + sum_m R_m^* X_m, X_m := Theta_{+,m} - omega^+_m + d^#_m(omega^+_m) w^#_m.
   |kappa| <= |B_+(zhat^#)| + (1 + ||U||)||e_+||_1 and B_+(zhat^#) = B_+(zhat) + sum_j B_+(j)(z^# - z)_j + <U^*B_+, e^# - e>: |B_+(zhat)| <=
   t/(2q_0) (Lemma lem:budget(a)); raised coordinates contribute <= sum (1 - |z_j|)|B_+(j)| <= t/(2q_0); flipped (C1) coordinates, the s_m
   and the pulls (|z^# - z| <= 2) contribute <= 2(t^2 + N(K_P t + t/q_0) + sum_{Pu} |Delta B(j)| + t/q_0), and sum_{Pu} |Delta B(j)| <=
   sum 6 lambda v(j)/t + t^7 <= 6 l 2^{G(l)} eta/t <= t^2; finally ||B_+||_1 <= C/t (Lemma lem:box) and ||e^# - e|| <= C Design Lam (Lemma CO),
   so |<U^*B_+, e^# - e>| <= C Design Lam/t <= t.  So |kappa| <= C(K_U + N K_P + 1) t.  The block part is estimated as in Y1 Step 5 / Z3
   Proposition T step (5) (fix T3): at kept coordinates omega^+ = omega_+ except for the shift, lambda|x| <= |tau - tau'| + lambda |Delta d| M
   (computed from Lemma lem:suplevel(f),(c): vs omega^-(k) >= vs omega_-(k) - |tau - tau'|/lambda - |Delta d| M and vs omega_-(k) >= -1.5 gap/t,
   gap <= b M <= gap^# at (K4)); clamped coordinates by the claim in the proof of Proposition prop:windowcert(c) (read at f^#), dropped carriers
   and status changes between f and f^# with the datum 0 (errors |tau| + lambda |Delta d| M, resp. 2 lambda gap/t + |tau| + lambda|Delta d| M with
   gap <= b); replacing (d, w, gap) by (d^#, w^#, gap^#) costs C_f c(delta)/t + (2/t) sum lambda |gap^# - gap| <= C theta_w t (Lemma CO, c(delta)
   <= theta_w T_lo^2 <= theta_w t^2); fine coordinates as in Proposition prop:windowcert(c).  Altogether p*(g - g_t) <= (1+||U||)||g - g_t||_1
   <= C_f (1 + G**)(K_U + N K_P + 1) t =: K_w t, and K_w <= C_f G**^2 l^2 D^6/u^4 <= C_f Design(l) u^{-4} (Design >= (l D G**)^6).
 * (i): t||b^+-||_1 <= A_0 as in Lemma lem:windowtwopiece(d) (||V'||_1 <= sum tau' <= 12 sum lambda/t <= 4/t; Lemma lem:finitebase on F).
   Gamma: sqrt(Gamma^#_w) is a seminorm at f^#; compare (b^+, omega^+ - d^# w^#) with (B_+, Theta_+): the difference is (e_+ + kappa a/a(zhat^#),
   X), contributing <= C K_w t (q_0^# h^#(y) <= ||U||^2 ||y||_1^2/nu^#, sigma^#_m H^#_m(X) <= (sum lambda|X|)^2/C^#_m).  For Gamma^#_w(B_+, Theta_+):
   (Hilbert part at CHANGED e; NEW) ||P^perp_{e^#} U^*B_+|| <= ||P^perp_e U^*B_+|| + 2||e^# - e|| ||U|| ||B_+||_1 <= (2nu/q_0)^{1/2} + C Design Lam/t,
   and Design Lam/t <= Design T_lo^2 <= theta_w; nu^#, q_0^# are within C Design Lam of nu, q_0; so |q_0^# h^#(B_+) - q_0 h(B_+)| <= C theta_w.
   (Block part; Z3-ref fix T3) |H^#_m(Theta) - H_m(Theta)| <= C ||D_m Theta||^2 (||D(w^# - w)|| + |C^# - C|) <= C t^{-2} C_f Design Lam log(1/Lam)
   <= C theta_w.  With Lemma lem:budget(d) at f: Gamma^#_w(B_+, Theta_+) <= 1 + eta_Gamma(eta) + C theta_w.  The - side likewise (compare with
   (B_-, Theta_-); on F, (B_- - b^-) 1_F = sum_G eps(tau' - tau) u 1_F + sum_{R, fine} Delta theta u 1_F + kappa a/a(zhat^#), as in Lemma
   lem:windowtwopiece(c)).
 * (iii): clamped coordinates are of kind [1] (Definition def:windowcert at f^#); (K1), (K2) have gap^# >= M^# u/2 >= gamma(w), (K3) have
   gap^# >= M^#/2 (Lemma ST(c)): kind [2] with |omega^+| <= 4/t, |omega^-| <= 4/t + 12/t (|omega_+| <= (3+eta)/t by Lemma lem:suplevel(e),
   tau'/lambda <= 12/t); (K4) after the shift: kind [3] (strict non-peaks of f^# by Lemma ST(c); inward up to 1.5 gap^#/t by the choice of x:
   vs omega^+ <= 1.5 gap/t <= 1.5 gap^#/t before the shift and the shift moves vs omega^+- up only when vs omega^- < -1.5 gap^#/t, to exactly that
   value, so vs omega^+ = vs omega^- - tau'/lambda <= 1.5 gap^#/t); before the shift |omega^+| <= 4/t, |omega^-| <= 16/t, the shift has
   |x| <= |omega^-| + 1.5/t <= 17.5/t, so afterwards |omega^+| <= 21.5/t and |omega^-| <= 1.5/t: A_2 = 22 suffices.  QED

## 4.2 Theorem E'' (Theorem E with window-dependent constants, banked and pulled supports).  PROVED.
Let f_j -> f in S_{p*} with supp a_j = F ∪ Ba_j ∪ Pu_j (finite), Ba_j contacts of f carrying masses of sign z at f_j, Pu_j coordinates where
z_j = -z (pulls), and suppose that for every j and every scale t of a window (T_j, n_j) there are d-neutral two-piece data at f_j satisfying
(E-a), (E-b) (kinds [1], [2], [3] with A_2 fixed, gamma_B(j) window-dependent; kind [1] may be relaxed to [1']: gap > 0, |omega| <= 2 gap/t),
(E-c), (E-d'), (E-e') of Y1/Y2 Theorem E', and in addition: the data are contact-like on Ba_j and t|b^+-(i)| <= |a_j(i)| for i in Pu_j.
Then (f, rho g) in cl NA((c_0, p), l_2^2).
Proof.  Theorem E' (Y1 5.3, Y2 2.2; refereed) uses Lemma U' at f_j.  In Lemma U (proofs of Lemmas lem:uniformtransfer, lem:onesidedtransfer)
the base support enters only through the excess term Exc(rb) of Lemma lem:bookkeeping(b) (no flips): on F, a_{j,min,F} -> a_min > 0 as
before; on Ba_j, contact-like data give |a_j(i) + r b_i| - |a_j(i)| - z_i r b_i = 0 for r of the side's sign (Y4 Lemma 2.3, refereed); on Pu_j,
|r b(i)| <= c_flat t |b(i)| <= |a_j(i)| (c_flat <= 1/8), so a_j(i) + r b(i) keeps the sign z_j(i) of a_j(i) and the excess vanishes (Y4-ref
Lemma P2, re-verified here); off supp a_j the side conditions at f_j.  All other constants (nu_j, q_0^(j), sigma_{j,m}, C_{j,m}, M_{j,m},
transfer data via Lemma lem:persistence) depend only on the convergent forced data.  Kind [1'] is Y1-ref Section 4.  The final step
applies Corollary cor:D1 at the fixed f_j (finite base support) to the averaged data, which are d-neutral two-piece data at f_j: contact-
likeness on Ba_j, the side conditions and d-neutrality are linear or convex conditions, preserved by averaging; nothing is required at
support coordinates.  QED

## 4.3 MASTER THEOREM II (design D_Omega, diagonal base).  PROVED.
Let T = D_Omega, N >= 1, f in S_{p_N^*} with finite base support F.  Suppose that for infinitely many levels l there is a clean sub-window
w of level l (one exists at EVERY level, Theorem 2') at which
   (SH_w)  every block has an upper and a lower shift source at w, or the shift cost of the source-deficient blocks is robust,
           c_{pi(w)}(f) >= u(w)   (part 2, 2.5);
   (VR_w)  every extreme ray of the zero-cost cone C(kappa(w)) has at most one robust d-component   (part 2, 2.6).
Then f in Rec: (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f).
No donor hypothesis, no compensation or one-signedness, no nearly-neutral hypothesis, and no rate or growth condition is imposed: rooms,
target rooms, margins (weak, DEGENERATE), gaps, relative d-coefficients and ray d-sums are arbitrary; contact sets, slaving, the number of
swallowed carriers and the alignment of the far signature tails (the "aligned corner") are arbitrary.
Proof.  Fix g in C(f), rho in (0,1), eta_0 in (0,2] with rho^2(1 + eta_0) <= (1 + rho^2)/2, kappa_0 := (sqrt(1 + eta_0/2) - 1)/2, and eta <= eta_*
with eta_Gamma(eta) <= 1 and sqrt(1 + eta_Gamma(eta)) <= 1 + kappa_0/2.  Along the given levels l_j -> infinity (l_j >= l_f) take w_j := w(l_j),
f_j := f^#_{w_j} (part 3), T_j := T_hi(w_j), n_j := n(w_j), and for every dyadic t in W(w_j) the functional g_{j,t} := g_t of Proposition TR.
Check Theorem E'':  supp a_j = F ∪ Ba_j ∪ Pu_j, f_j -> f since p*(f_j - f) <= theta_{w_j} T_lo(w_j)^2 -> 0 (Lemma CO).  (E-a): Proposition TR(i),
Gamma <= (1 + kappa_0/2 + C theta_w + K_w t)^2 <= 1 + eta_0/2 once C theta_w + K_w T_hi(w) <= kappa_0/2 (true for large j, below).  (E-b):
Proposition TR(iii), A_2 = 22, gamma_B(j) = gamma(w_j).  (E-c): Proposition TR(ii).  Supports: Proposition TR(iv).  (E-d'): K_w <= C_f Design u^{-4}
and c_flat(w) >= c_0 gamma(w)/A_2 >= c_f u(w) (Lemma U'); with Q(w) = (4 Design/u)^{omega+20}: K_w T_hi(w) <= C_f Design u^{-4} 2^{-l^3}/(l Q(w))
<= C_f 2^{-l^3}/l -> 0, and n(w) c_flat(w)/K_w >= l 2^{l^3} Q(w) c_f u^5/(C_f Design) >= l 2^{l^3}/C_f -> infinity.  (E-e'): eps_j <= theta_w T_lo^2 with
theta_w = C_f Design T_lo log(1/T_lo), while c_flat(w)^2 >= c_f u^2 and T_lo(w) <= 2^{-n(w)} <= 2^{-Q(w)} <= 2^{-(4/u)^{20}} (and Design <= Q^{1/20}):
theta_w <= c_f u^2 (1 - rho^2)/(24 rho^2) for large j; also eps_j <= (1 - rho^2) r_0^2/6 eventually.  t <= min(t_eta, t_1, 1) on W(w_j) for large j.
Theorem E'' gives (f, rho g) in cl NA; rho < 1 was arbitrary and cl NA is closed.  QED

Corollaries (PROVED from 4.3).
 (M-II.1) [one block] For N = 1, (VR_w) holds at every w (every ray lives in the single block).  Hence for D_Omega and N = 1: f in Rec
          whenever (SH_w) holds at a clean sub-window of infinitely many levels.
 (M-II.2) [single-block rays] If, for infinitely many levels, at some clean w every extreme ray of C(kappa(w)) is supported in one block and
          (SH_w) holds, then f in Rec.  In particular Y1's hypotheses (Do_w) [donors], (NN_w) [nearly neutral carriers] and the one-signed
          alternative of (Cmp_w) are never needed (one-signed blocks carry no robust component, part 2 Remark (2)), and Y1's (SP_w) is the
          special case I_up ∪ I_lo = {} of (SH_w).  The compensated alternative of Y1's (Cmp_w) is NOT contained: Y1 5.4 also covers rays with
          robust components in several COMPENSATED blocks (part 5, 5.3).
 (M-II.3) [maximal contact] F finite, z = eps_0 off F: (SH_w) holds at every clean w of large level (Z4 Lemma 5.0: every block has non-degenerate
          peaks of both kinds with margins >= q_0/4, i.e. sources (L2) and (U2)); so f in Rec whenever (VR_w) holds at a clean sub-window of
          infinitely many levels — in particular for N = 1 always.
