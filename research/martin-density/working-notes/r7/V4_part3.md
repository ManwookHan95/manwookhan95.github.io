# V4 part 3 — (C) and (D) are residuals of the window method, not of the problem: block-tame instances, exact
# negative-d-mismatch data, fine re-alignment, and transplant to (SC)-companions

Notation of parts 1-2.  Recall (note): (BT) = F finite, every Q_m finite, no degenerate peaks, (MS) [sum{Phi_m(k) : mu_{k,m} < s} = o(s)].
Corollary cor:BTrecovered: every (BT) point is in Rec (Theorem thm:onesided(c) gives two-piece data with kappa_w <= 1 for EVERY mate,
any sign of Delta d; (BT) gives (SC) for every set of blocks; Theorem thm:engineered).

## 3.1 The residual configurations occur at block-tame points
**Corollary 3.1.  PROVED.**  (a) The first row f_SA of Theorem 2.2 satisfies (BT); hence f_SA in Rec.  (b) The aligned-corner instance
of Remark 2.3(2) with a weak peak (relative margin xi > 0) satisfies (BT); hence it is in Rec.  (c) Consequently configurations (C) (exact
coherent shift resonance: UPPER fails and c_*(l) = 0 at every level) and (D) (aligned corner with a weak swallowing-type peak, no donor)
are NOT obstructions to recovery as such: they are residuals of the window/companion method only.  A counterexample inside (B), (C) or
(D) must in addition violate (BT): infinitely many strict non-peaks in some block, or a degenerate peak, or failure of (MS).
*Proof.*  (a) F = {p, p'} finite; by Theorem 2.2(b),(c) every Q_m is finite (Q_{m_0} = {k(l_-)}, Q_m = {} otherwise); no degenerate peak
(2.2(b),(c)); (MS): the peaks with mu < s are, apart from finitely many fixed-margin peaks, those with q_0 delta°_l/2 < s, and Step 8 of
the proof of Theorem 2.2 shows that their Phi-sum is o(s).  (b) Same, with the one weak peak contributing nothing to (MS) for s < its
fixed margin.  (c) Cor. cor:BTrecovered.  The same applies to every finitely-tuned variant (finitely many exceptional carriers tuned
through F), in particular to the (B)-core of Remark 2.3(2): with finitely many switchable carriers the point is (BT).  QED
Interpretation.  The master theorems (Y1, Y2 Thm Y, V1) need shift sources ((SP_w)) because their WINDOW DATA are d-neutral; at (BT)
points Theorem thm:onesided produces, for every mate, exact two-piece data whose Delta d may be NEGATIVE, and Theorem thm:engineered
handles Delta d < 0 under (SC), which (BT) provides.  So the coherent shift is harmless whenever the first row is block-tame.

## 3.2 Explicit coherent-shift mates (the "most dangerous" finite-tuning mates are recovered)
**Proposition 3.2.  PROVED.**  N = 1.  Let f = f_SA, k_- := k(l_-), zeta-hat := R^** zhat, and for Delta_alpha > 0, chi in [0,1]:
   omega^+ := alpha e_{k_-},  omega^- := (alpha + Delta_alpha) e_{k_-},   V := u_{l_-} - (val_{l_-}/|zeta-hat|) R^* w.
Then (i) Delta d := d(omega^-) - d(omega^+) = Delta_alpha lambda_{l_-} val_{l_-}/|zeta-hat| < 0;  (ii) V 1_{F^c} is z-signed and supported in K
(no free coordinate meets it); (iii) with b^+ := chi Delta_alpha lambda_{l_-} V 1_{F^c} + beta^+, b^- := b^+ - Delta_alpha lambda_{l_-} V,
where beta^+ (supported in F) is chosen so that b^+(xi) = 0, the pairs (b^+, omega^+), (b^-, omega^-) are two-piece data with Delta d < 0
for g := b^+ + R^*(omega^+ - d(omega^+) w); (iv) c g in C(f) for all small c > 0, and every such mate is recovered (Theorem thm:engineered
with I_- = {1}; (SC) by Theorem 2.2(f)).
*Proof.*  (i) d(omega) = <Dw, D omega>/C and, off P, Phi_k^2 w(k)/C = zeta(k)/|zeta| (Lemma lem:threshold; scale invariant), so
d(omega^-) - d(omega^+) = Delta_alpha zeta-hat(k_-)/|zeta-hat| = Delta_alpha lambda_{l_-} val_{l_-}/|zeta-hat|, negative since val_{l_-} = -eta/n < 0.
(ii) R^* w = sum_k lambda_k w(k) u_k = M sum_{k != k_-} lambda_k eps_k u_k + lambda_{l_-} w(k_-) u_{l_-} (all other carriers are peaks of
swallowing type, w(k) = varsigma_k M = eps_k M).  Hence V 1_{F^c} = c_1 v_{l_-} + c_2 (W - lambda_{l_-} eps_{l_-} u_{l_-}) 1_{F^c}, with
c_2 := eta M/(n_{l_-} |zeta-hat|) > 0, c_1 := 1 - lambda_{l_-} val_{l_-} w(k_-)/|zeta-hat| = 1 - C m^2 val_{l_-}^2/|zeta-hat|^2 in (0,1] for
eta small (w(k_-) = C lambda val/(Phi^2 |zeta-hat|)).  Off S_{l_-}, V = c_2 W, z-signed with full contacts by Theorem 2.2(d).  On S_{l_-}
(z = +1): V(s) = c_1 v_{l_-}(s) + c_2(W(s) - lambda_{l_-} v_{l_-}(s)) and |W(s) - lambda_{l_-} v_{l_-}(s)| <= 2^{-6} lambda_{l_-} v_{l_-}(s) (later
targets, Step 6 of Theorem 2.2), so V(s) >= (c_1 - 2^{-6} c_2 lambda_{l_-}) v_{l_-}(s) > 0.
(iii) b^+ - b^- = Delta_alpha lambda_{l_-} V = R^*(omega^- - omega^+) - Delta d R^* w (R^* e_{k_-} = lambda_{l_-} u_{l_-}), so both pairs
represent g; off F, b^+ = chi Delta_alpha lambda_{l_-} V is z-signed in K and b^- = -(1-chi)Delta_alpha lambda_{l_-} V is (-z)-signed in K;
omega^+- are finitely supported in Q = {k_-}; b^-(xi) = g(xi) = b^+(xi) = 0 (Lemma lem:algebra).  (iv) Proposition prop:onesidedupper on both
sides gives p*(f + r g) <= 1 + (r^2/2)(kappa_w + o(1)); for small c the global inequality p*(f + t c g) <= s(t) follows from this for
|t c| <= r_0 and from p*(f + t c g) <= 1 + |t| c p*(g) for |t c| >= r_0 (s(t) - 1 >= min(t^2, |t|)/3).  Theorem thm:engineered applies.  QED
These mates switch through the swallowed q < 0 carrier l_- and carry the uniform shift of the block through ALL peaks (the term
-Delta d R^* w), at every scale: they are exactly the "coherent shift" mates that the window method cannot follow (Y2 5.3(c)), and they
are recovered.  (Numerical check of (ii): part 5.)

## 3.3 Exact data with Delta d != 0 force cancellations at every free coordinate
**Lemma 3.3.  PROVED.**  Let F be finite and (b^+-, omega^+-) two-piece data at f with Delta d_m != 0 for m in I_ne.  Put
D := sum_m R_m^*(omega^-_m - omega^+_m) - sum_m Delta d_m R_m^* w_m (= b^+ - b^-).  Then D(j) = 0 at every free coordinate j (|z_j| < 1,
j notin F), and z_j D(j) >= 0 at every contact.  In particular, at every free coordinate j outside the (finite union of) supports of the
carriers carrying omega,  sum_{m in I_ne} Delta d_m (R_m^* w_m)(j) = 0, an exact cancellation of an infinite sum (by Lemma 1.2, j lies in the
targets of infinitely many carriers of every block, all with w != 0 except tuned d-neutral ones).
*Proof.*  b^+ and b^- vanish off F ∪ K, b^+ is z-signed and b^- is (-z)-signed on K (Definition def:twopiece).  QED
Consequence (HEURISTIC, from Lemma 3.3 and Lemma 1.2): exact data with Delta d != 0 live at FULL-CONTACT rows (|z| = 1 off F) up to
non-generic cancellations.  At a full-contact row with diagonal base, carrier values depend continuously only on a (Lemma 1.1): every
near-threshold carrier is tuned through F.

## 3.4 Design genericity of signature masses
**Lemma 3.4 (generic masses (GM)).  PROVED.**  A design satisfying (SF*) can be chosen (by choosing delta_l at stage l outside finitely
many small intervals, and then c_{l+1}) such that for every carrier l, every sign vector sigma in {-1,0,1}^{supp y_l} and eps = +-1,
   | sum_j sigma_j y_l(j) + eps delta_l H_l | >= g_l > 0,    with  (1 + ||U||) Phi_l <= 2^{-l} g_l Phi_{l-1}... and  Phi_{l} <= g_l 2^{-l} (all l).
Consequence: if f has F finite, theta-bound theta_m <= Theta and a carrier l of block m with S_l ∩ F = {}, supp y_l ∩ (F ∪ J) = {}
(all its target coordinates are contacts) is exactly swallowed, then for l large (depending on Theta, i.e. on f) l is a peak with
relative margin >= g_l/(2 theta_m Phi_l/m) - 1 (huge): never near-threshold.  So every near-threshold swallowed carrier beyond an
f-dependent level has a target coordinate in F or in J.
*Proof.*  At stage l the values sum_j sigma_j y_l(j) form a finite set (3^{|supp y_l|} values); delta_l ranges over an interval
(0, delta_l^max]; exclude the finitely many delta_l with |sum sigma y + eps delta_l H_l| < g_l for a g_l small enough that the excluded
set has measure < delta_l^max/2.  Then choose c_l (allowed: c_l enters only after y_l, delta_l, see Lemma 2.1) with Phi_l <= g_l 2^{-l}.  For
the consequence: by Lemma 1.1, n_l val_l = sum_{supp y_l} y_l(j) z_j + eps_l delta_l H_l with z_j in {+-1}: |n_l val_l| >= g_l, while the
threshold is theta_m Phi_l/m <= Theta g_l 2^{-l}/m.  QED
**Design question (GO) (generic offsets).  SKETCH/OPEN.**  Can the design ensure in addition that every first row with F finite has
only finitely many near-threshold carriers whose targets meet F but avoid J?  The tuning conditions are slabs {x : |<y_l|_F, x> + c_l| < tol_l}
in x = zhat_F (|F| continuous parameters), with offsets c_l moved by the design choice of delta_l.  A recursive choice of delta_l
avoiding neighbourhoods of the intersection points of |F| earlier slabs (finitely many F with max F <= N_l, sign patterns and subsets
at stage l; c_l chosen after y_l so that tol_l is small compared with the conditioning of earlier subsets) looks feasible; I have not
written out the bookkeeping (in particular theta enters tol_l and is only bounded per f).  With (GO), full-contact rows have only
finitely many near-threshold carriers, hence (generically) are (BT) up to finitely many degenerate peaks.

## 3.5 Fine re-alignment: block-tame approximants of every first row with finite support
**Theorem 3.5 (fine re-alignment).  PROVED** (design with (SF*), diagonal U, any N).  Let f have F finite and L >= 1.  Define z^(L) by
z^(L) := z on F and on every coordinate lying in the support of some carrier l <= L, and on the remaining coordinates by the owner
recursion of Construction SA run over the carriers l > L (eps_l := sgn A_l, A_l computed with the already assigned coordinates, new target
coordinates aligned, z^(L) := eps_l on S_l \ F); coordinates in no support keep z.  Let f^(L) be the first row with data (a, z^(L)).  Then:
 (a) p*(f^(L) - f) <= C_f c(delta^L) <= C_f' sum_{l > L} lambda_l log(e/sum_{l>L} lambda_l) -> 0  (Z3 Lemma 3.1);
 (b) every carrier l <= L has the same value at f^(L) as at f; every carrier l > L with S_l ∩ F = {} is an exactly swallowed,
     non-degenerate peak of swallowing type with margin >= q_0 delta°_l/2 (beyond the first peak of its block);
 (c) after an arbitrarily small further modification (one free fine coordinate moved continuously), f^(L) has no degenerate peak;
     then f^(L) satisfies (BT).  Hence (BT) points are dense in {f in S_{p*} : F finite}, and Lemma Z holds at f (for all g, rho) as soon
     as dist(rho g, C(f^(L))) -> 0 along some sequence L -> infinity (Lemma Z through block-tame approximants).
*Proof.*  (b) Coarse supports (signature sets S_l, l <= L, and targets y_l, l <= L) are untouched; by allowedness (a) no coarse target meets
a fine signature set, and the fine "new" coordinates are by definition outside coarse supports; so coarse values are unchanged.  For fine
l, the proof of Theorem 2.2 Steps 2 and 4 applies verbatim (it used only the owner rule at l, |val_k| <= 1 + ||U|| for every other
carrier, and (SF*)); the margin bound holds for every fine l after the first peak k_* of its block (theta < nu_{k_*}).  (a) delta^L :=
z^(L) - z is supported in fine signature sets and fine new coordinates, so u_k(delta^L) = 0 for k <= L and |u_k(delta^L)| <= 2 for k > L;
Z3 Lemma 3.1 (same a) gives the bound, with Delta_m <= 2 sum_{l>L} lambda_l.  (c) Q_m^(L) is contained in the finitely many carriers
<= L and the finitely many fine carriers with S_l ∩ F != {}; (MS) holds since all but finitely many margins satisfy mu_l >= q_0 delta°_l/2
(Step 8 of Theorem 2.2).  Degenerate peaks can only occur among these finitely many carriers.  Pick a fine carrier l_a > L of block m
(each m) and one of its new target coordinates j_a; replace z^(L)_{j_a} = eps_{l_a} sgn y_{l_a}(j_a) by t eps_{l_a} sgn y_{l_a}(j_a),
t in (1/2, 1]: val_{l_a} changes continuously and strictly monotonically in modulus, all other values are unchanged except those of later
carriers whose targets contain j_a (a uniformly small, continuous change for t near 1 that keeps their signs by the owner rule margins),
so theta_m^(L) changes continuously and strictly (Lemma T(d)(i)) while the finitely many coarse nu_k are fixed; a value of t near 1 avoids
the finitely many coincidences nu_k = theta_m.  The last statement: f^(L) in Rec by Cor. cor:BTrecovered, and the argument of
Theorem thm:reductionZ.  QED
Remarks.  (1) f^(L) is the block-tame counterpart of the far lowering f^L of Remark rem:openZ (O2) (which makes fine carriers ROOMY): the
re-alignment makes fine carriers SWALLOWED robust peaks.  Mates that use fine one-sided swallowing-type resources (the coherent shift uses
all peaks) keep these resources at f^(L), and lose them at f^L.  (2) Lemma Z at F-finite rows is thus equivalent to lower semicontinuity of
the fibre along SOME sequence of block-tame approximants, and f^(L) is a canonical candidate at cost O(sum_{l>L} lambda_l log).

## 3.6 Transplant of data with Delta d <= 0, and (SC)-companions
**Lemma 3.6 (transplant).  PROVED.**  Let f, f^# have the same F, and let (b^+-, omega^+-) be two-piece data at f for g with Delta d_m <= 0
for all m.  Assume: (T1) every k in supp omega^+-_m is a strict non-peak of f^#; (T2) the vector
   D^# := sum_m R_m^*(omega^-_m - omega^+_m) - sum_m Delta d^#_m R_m^* w^#_m,   Delta d^#_m := d^#_m(omega^-_m) - d^#_m(omega^+_m),
is z^#-signed off F and vanishes at the free coordinates of f^#.  Then there are two-piece data (b^+-_#, omega^+-) at f^# for
G^# := b^+_# + sum_m R_m^*(omega^+_m - d^#_m(omega^+_m) w^#_m), with Delta d^#_m <= 0, and
   ||b^+-_# - b^+-||_1 <= C(||D^# - D||_1 + 2||D 1_{Fl}||_1 + 2||D^# 1_{Fl}||_1) + C|b^+_#(xi^#) - b^+(xi)|-terms,
where D := b^+ - b^- and Fl := {j : z^#_j z_j = -1} (flipped contacts); ||G^# - g|| -> 0 as f^# -> f.
*Proof.*  Off F, at each j with D^#(j) != 0 (a contact of f^#), write D^#(j) = z^#_j s_j with s_j > 0 and split it as b^+_#(j) := z^#_j x_j,
b^-_#(j) := -z^#_j y_j, x_j + y_j = s_j, x_j, y_j >= 0, choosing (x_j, y_j) nearest to (z^#_j b^+(j), -z^#_j b^-(j)) (both >= 0 when
z^#_j = z_j); the distance is <= |D^#(j) - D(j)| when z^#_j = z_j and <= |D(j)| + |D^#(j)| at flips.  Off supp D^# put b^+-_# := 0.  On F
keep b^+ and set b^-_# := b^+_# - D^# there; rebalance with multiples of a (b(xi^#) = 0).  Then b^+_# - b^-_# = D^#, so (b^-_#, omega^-)
represents G^# (the same computation as in Proposition 3.2(iii)); side conditions hold by construction; d^# >= 0 sign: Delta d^#_m has the
sign of Delta d_m when the omega-coordinates are strict non-peaks at both rows (d_m(e_k) = zeta(k)/|zeta| keeps its sign).  ||G^# - g|| ->
0: Z3 Lemma 3.1 gives sum_m ||R_m^*(w^#_m - w_m)||_1 -> 0 and d^# -> d on the fixed finite supports.  QED
**Theorem 3.7 (negative d-mismatch through (SC)-companions).  PROVED.**  Let f have F finite, g in C(f) carrying two-piece data with
Delta d <= 0 and kappa_w <= 1.  Suppose there are first rows f_j -> f with supp a_j = F satisfying (T1), (T2) of Lemma 3.6 for these data
and (SC) for the blocks with Delta d^#_m < 0 (e.g. f_j in (BT)).  Then (f, g) in cl NA((c_0, p), l_2^2).
*Proof.*  Fix rho < 1.  Transplanted data at f_j represent G_j -> g, with kappa^(j)_w -> kappa_w (continuity of h, H_m, sigma_m, q_0 along
f_j -> f, and ||b_# - b||_1 -> 0).  Z3 Lemma U (one-sided uniform transfer along f_j -> f with supp a_j = F; fixed data, kinds [1]/[2]
with the fixed gaps of the omega-coordinates) gives r_1 > 0 and j_0 with p*(f_j + r G_j) <= 1 + (r^2/2)(kappa_w + eps) for |r| <= r_1,
j >= j_0 (on each side with the corresponding pair).  Hence, for rho^2(kappa_w + 2 eps) <= 1 - r_1^2/4, p*(f_j + r rho G_j) <= s(r) for
|r| <= r_1; for |r| >= r_1, p*(f_j + r rho G_j) <= s(rho r) + p*(f_j - f) + |r| rho p*(G_j - g) <= s(r) for j large, since s(r) - s(rho r) >=
c(rho, r_1) min(r^2, |r|) there.  So rho G_j in C(f_j), carrying data with kappa_w(rho G_j) = rho^2 kappa^(j)_w <= 1 and Delta d <= 0;
(SC) holds at f_j; Theorem thm:engineered gives (f_j, rho G_j) in cl NA.  Let j -> infinity, then rho -> 1.  QED
**What Theorem 3.7 still needs (the precise residual of (C) for exact data).**  (SC)-companions preserving (T2).  Block-tame companions
come from fine re-alignment (Theorem 3.5), but (T2) requires D^# to be z^#-signed with D^#(j) = 0 at the free coordinates of f^#; by
Lemma 3.3 this is automatic only at full-contact rows (no free coordinates), and at those rows the coarse structure must keep its
signs under the threshold drift (robust coherence, true where z_j D(j) > 0 strictly and the owner terms dominate).  The re-aligned fine
part -Delta d^# R^* w^#_fine is z^#-signed by the owner rule (Theorem 2.2(d) argument), and fine targets hitting coarse contacts are
dominated by the coarse terms when D(j) != 0.  So: at full-contact rows whose data satisfy STRICT coarse coherence, Theorem 3.5 +
Lemma 3.6 + Theorem 3.7 recover every mate carrying exact negative-d-mismatch data (SKETCH: the strictness/domination bookkeeping at
coordinates where D(j) = 0 is not written out).  The remaining exact-data cases are rows where coherence is achieved by EXACT
cancellations (D(j) = 0 at free coordinates, Lemma 3.3), which a companion moving fine values generally destroys.

## 3.7 Lemma G (generic threshold gives (SC)) — an alternative source of (SC)-companions
**Lemma 3.8 ((SC) from a generic threshold).  PROVED.**  Fix a block m and suppose eps_k := (Phi_m(k+1)/Phi_m(k))^{1/2} is summable
(true for every SLD-type design).  Let kappa > 0 be a lower bound of q_0/m and C_m/|zeta|.  If block m has no degenerate peak and
theta_m notin limsup_k [nu_k - eps_k/kappa, nu_k + eps_k/kappa], then (SC) holds for {m} (for every Upsilon, along s_L :=
(Phi_m(L) Phi_m(L+1))^{1/2}/Upsilon).  If theta can be moved continuously over an interval while each nu_k either stays fixed or moves
with velocity >= v_k > 0 (sum_k eps_k/v_k < infinity), then (SC) holds for Lebesgue-a.e. value of the parameter.
*Proof.*  For a peak, mu_k = q_0 Phi_k (nu_k - theta)/m; for a strict non-peak, Phi_k gap_k = Phi_k C (theta - nu_k)/|zeta|.  A carrier with
Phi_k > Upsilon s_L contributes to Scr_m(Upsilon s_L) only if Phi_k |nu_k - theta| kappa <= Upsilon s_L, i.e. |nu_k - theta| <=
(Phi_L Phi_{L+1})^{1/2}/(kappa Phi_k) <= eps_L/kappa (k <= L).  The carriers with Phi_k <= Upsilon s_L contribute <= sum_{k > L} Phi_k <=
2 Phi_{L+1} = o(s_L).  Under the hypothesis, for all L >= L_0 no k <= L has |nu_k - theta| <= eps_L/kappa (for k >= k_0 since eps is
decreasing and theta is outside I_k; for k < k_0 since theta != nu_k and eps_L -> 0).  So Scr_m(Upsilon s_L)/s_L -> 0.  The a.e. statement:
the set of parameters with theta in I_k has measure <= 2 eps_k/(kappa v_k) for moving nu_k (and is a translate of a set of measure
<= 2 eps_k/(kappa min |theta'|)... for fixed nu_k, the measure is <= 2 eps_k/(kappa inf |d theta/dparam|) when theta is strictly monotone
with derivative bounded below on the interval); Borel-Cantelli.  QED
Use: a donor or bank companion moves theta_m continuously and strictly (Lemma T(d), Y2 Prop Q Step 2); by Lemma 3.8 a.e. move size gives
(SC) at the companion.  For DELTA d != 0 data, however, a z-move donor creates a free coordinate inside the donor's signature set where
R^* w^# != 0, violating (T2); a PULL donor (Y4-ref C.1: the moved coordinate becomes a support coordinate) avoids this, at the price of
F^# = F ∪ {pulled coordinate} (Lemma U with pulled support: Y4-ref Lemma P2).  SKETCH: (SC)-companions by pull donors for
negative-d-mismatch data, with the transplant of Lemma 3.6 (F^# != F: the pulled coordinate carries no data constraint).
