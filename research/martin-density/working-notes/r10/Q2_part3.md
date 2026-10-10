# Q2 part 3 -- producing cushion-dominated window families at infinite F: inventory, two new lemmas, the remaining step

By part 2 (Theorem E^{eng,RT,inf}), (LSC-trunc) at (f, g, rho) -- indeed (f, rho g) in cl NA -- follows once base rows f_j with the
raise-transfer property (a) carry window families (U1), (U2), (U3^inf), (U4)-(U7) with (E-c)-(E-f).  For F finite these families are
produced by the finite-F machinery (U1 companions with U1-ref's fixes, X1's Proposition KN^tr, X2's Lemma CM', Lemma DC/LV, V1's TR;
assembled as Master Theorem VI by task Q1).  This part lists every place where that production uses finiteness of F, and what replaces it.
Design: T_fin^* := T_fin (ADDENDUM 9) over U2's doubly exponential diagonal base mu*_s = 2^{-2^{2^s}} with B_mu(l) adapted (U2 1.1,
U2-ref (s1)); all window theorems are unaffected by the base change (U2 Remark after 1.1; U4 Lemma GW).

## 3.0 Inventory (where the finite-F production uses that F is finite)
 (alpha) No-flip on F via a_min = min_F |a_j| (X2 Lemma M2, Theorem UE (c1); V1 TR via lem:windowtwopiece; R1/R2).  REMOVED by part 2:
         only side cushion domination (U3^inf) is needed.
 (beta)  lem:finitebase in V1 Proposition TR(i) (t ||b^+-||_1 <= A_0).  REMOVED by Lemma 3.1 below (smallness instead).
 (gamma) Flips on F: the copied base data B_+- 1_F use the support beyond its cushion (deep flips; Lemma 1.1 of Z5).  At a raised
         companion they are cushion-dominated except at shallow thin coordinates, where Lemma P pins the switching.  Proposition 3.2
         (SKETCH; U2 Lemma W PROVED it for the RS/MT III' data).
 (delta) Levers.  V1 Lemma B / TU, X2 Lemma DC/LV and X1's KN^tr use z-moves, banks and pulls at coordinates j(l) in S_l beyond s_max that
         are OFF the support.  At infinite F these may lie in F.  Replacements: U2 Lemma TR-inf (cases (a), (a'), (c), (c'); PROVED), whose
         residual is (NDN).  Lemma 3.4 below (PROVED) identifies the exact one-sided structure behind (NDN); Remark 3.5 records what it
         implies.
 (eps)   New rate objects (moduli |a_s| at design depth, spreads, Sherman-Morrison denominators, resource determinants) must enter the
         design pigeonhole; done in U4/U2 for T_final^* (U2-ref (s1)), to be repeated for T_fin^* (bookkeeping).

## 3.1 Lemma 3.1 (TR(i) without lem:finitebase).  PROVED.
In V1 Proposition TR (and in every transplant of U1/X1/X2 that copies B_+ 1_F), the bound t||b^+-||_1 <= A_0 holds at arbitrary F with
A_0 := 6 for t <= min(t_eta, t_1) (eta <= 1).
Proof.  The data are b^+ = B_+ 1_F + chi V' - kappa a/a(zhat^#) and b^- = b^+ - sum_Kp eps tau' u (TR Step 5).  Lemma lem:smallness holds at
arbitrary F (Z5 Section 1: its proof uses only that bounded coordinatewise convergence with limsup ||A_n||_1 <= ||a||_1 forces
||A_n - a||_1 -> 0, true for every a in l_1), so t||B_+||_1 <= eta <= 1.  ||V'||_1 <= sum tau' <= 12 sum lambda/t <= 4/t (TR Step 3, box
rows), |kappa| <= C(K_U + N K_P + 1)t (TR, estimates (ii)), q*(a) = 1 and a(zhat^#) >= 1/2.  Hence t||b^+||_1 <= 1 + 4 + 2(1+||U||)C(...)t^2 <= 6
for t small, and t||b^-||_1 <= t||b^+||_1 + t sum tau' <= 10; take A_0 := 10.  (lem:finitebase was used only to bound ||B_+ 1_F||_1.)  QED
Remark.  The same replacement works in Z5's clamped window certificate and in R1 (where it was already done).  With Lemma 3.1, U2-ref's
inspection item G2 ("V1's transplant uses lem:finitebase") reduces to (gamma), i.e. to the cushion domination of B_+ 1_F at the raised
companion.

## 3.2 Proposition 3.2 (cushion domination of transplanted data at a deep-raised companion).  SKETCH.
Let w be a clean sub-window of a main stage L of T_fin^*, f^r the deep box-level raise of f beyond depth J (U2 Lemma DR-inf, with the raise
mass at j >= J augmented by |g_j|: Delta a_j := s_j (8 Bx_*(j) + |g_j| - |a_j|)_+, footprint <= mu*_J (8 sum_{j >= J} Bx_* + ||g||_1)),
and f^# a companion of f^r built by the finite-F moves of Q1's construction with the lever replacements of 3.3.  Then the transplanted
window data satisfy (U3^inf) at f^# with C_+ <= C Design(L)/u(w), after (i) projecting the switching of every carrier that is deep at an
unraised shallow thin coordinate to ZERO (Lemma P: such amplitudes are <= C_q t/v_l(s), and the projection is a face of the pattern cone,
whose Hoffman constant is a design minor, V2 Lemma H), and (ii) clamping the (now one-sided, switching-free) data at those coordinates to 0
(cost <= |a_s|/t + phi_s per coordinate in p*(g - g_t), i.e. O(b/t + t)).
Status: for the RS/MT III' data this is U2's Lemma W (PROVED, refereed with fix W1).  For Q1's data (U1 (class, cube) sets, KN^tr, Lemma CM')
the same three cases occur coordinatewise: deep (raised: |usage| <= |g_j| + 12 Bx_*(j)/t <= 2|a^r_j|/t), shallow robust (|a_j| >= u:
|usage| <= (t|g_j| + 12 Bx)/t <= (Design/u)|a_j|/t), shallow thin (|a_j| <= b: Lemma P + (i)-(ii)).  What is not written line by line is that
the zero-switching faces needed in (i) are compatible with Q1's class/cube pigeonhole (they are sub-patterns, so V2's minors cover their
Hoffman constants; the class labels of pinned carriers become "inactive").  The window-dependent C_+ makes c_flat window dependent,
c_flat(w) >= c_f u(w)/Design(L), which E^eng accepts (as V1's gamma_B(w) does) because n(w) >> Design(L)/u(w).

## 3.3 Levers at infinite F (inventory; U2 Lemma TR-inf restated for Q1's levers)
For a carrier l needing a two-sided value lever at a clean sub-window, look at the first two coordinates s < s' of S_l beyond s_max(L)
(design depth, D-lev: mu*_s^2 v_l(s) >= Design(L)^{-1}).  Exactly one of the following holds:
 (L1) one of them is OFF the support of the current row (contact or free): the finite-F lever there (X2 Lemma LV: zero-data Z-lever, Z-con,
      TU bank + far pull) -- verbatim, since the data at off-support coordinates are produced exactly as at finite F;
 (L2) one of them is in F and THIN (|a| <= b(w)): lower it to a contact of the same sign (cost <= 2|a| <= 2b << T_lo^2 in the transfer
      error, Lemma LT general form; its data are switching-free after Proposition 3.2(i)), then (L1)  [U2 TR-inf (a')];
 (L3) both are in F and THICK (|a| >= u(w)) with ROBUST spread |1 - rho_{s'}/rho_s| >= u(w), rho := a/v_l: the Hilbert PAIR (s, s') with
      Delta' = -(alpha_s/alpha_{s'})Delta, alpha := mu*^2 a/nu^2, cancels the common nu-term exactly at first order, so the pair is a private
      two-sided lever of efficiency >= Design(L)^{-1} u(w) [U2 TR-inf (c), PROVED];
 (L4) both thick, spread TINY: the two S-mass columns are parallel up to b; the lever is private only up to the common direction gamma
      (gamma_k := <U*u_k, U*a>), and the joint system over all such carriers is invertible iff the Sherman-Morrison denominator
      1 - sum c gamma/nu^2 is nonzero [U2 3.3]; robust denominator: invertible with constant Design/u (U2); tiny denominator: (NDN).
(At a clean sub-window "thin/thick" and "tiny/robust" are exhaustive because the moduli |a_s| (s <= d(L)), the spreads and the
denominators are rate objects of level L.)

## 3.4 Lemma 3.4 (the one-sided structure behind (NDN)).  PROVED.
Diagonal base.  Let f° be a row (forced data a°, z°, F°, nu°, e°) and u = sum_k c_k u_k a finite combination of carrier vectors with
u|_{F°} = kappa a°|_{F°} for some kappa != 0 (failure of (ND) for the carriers in supp c).  Let f^1 be ANY row whose forced data (a^1, z^1)
satisfy: z^1 = z° on supp u, and supp a^1 \ F° is disjoint from supp u.  [Allowed: arbitrary raises and lowerings of a on F°, including
truncation to contacts of the same sign and sign changes OUTSIDE supp u; masses at coordinates outside supp u; z-moves outside supp u.]
Then, with val_k := u_k(zhat) (raw values),
        sum_k c_k val_k(f^1) - sum_k c_k val_k(f°) = -(kappa nu°/2) ||e^1 - e°||^2        EXACTLY.
Proof.  sum_k c_k val_k = u(zhat) = u(z) + <U*u, e>.  u(z^1) = u(z°) since z^1 = z° on supp u.  With the diagonal base,
U*u = kappa U*(a° 1_{F°}) + U*(u 1_{F°^c}) = kappa nu° e° + sum_{s notin F°} mu_s u(s) k_s, and e^1 = sum_{s in supp a^1} mu_s a^1(s) k_s/nu^1;
the cross term sum_{s in supp a^1 \ F°} mu_s^2 u(s) a^1(s)/nu^1 vanishes by the disjointness hypothesis.  Hence <U*u, e^1> = kappa nu° <e°, e^1>
and the difference is kappa nu° (<e°, e^1> - 1) = -(kappa nu°/2)||e^1 - e°||^2 (unit vectors).  QED
Consequences (PROVED).  (a) In the (ND)-failure configuration, the combination sum c val attains a strict one-sided extremum at f° over all
rows reachable by moves that do not touch supp u off F° and do not change z on supp u: it can only DECREASE if kappa > 0 (only increase if
kappa < 0).  Every support move (raise, lowering, truncation, S-mass, Hilbert pair, "de-proportionalizing" pair) is of this kind, as are
masses and z-moves away from supp u.  (b) In particular no combination of support moves can move sum c val in the forbidden direction, at
any order; the only two-sided first-order resources for this combination are z-moves, banks and pulls ON supp u \ F° (signature coordinates
of the carriers of supp c outside the support) or sign changes on F° cap supp u (which cost |a_s| in the transfer error).  (c) A
"de-proportionalizing" Hilbert pair (a small relative raise at one thick coordinate of S_l cap F and a compensating lowering at another)
does create first-order efficiency ~ delta' in the forbidden direction at the new row, but by (a) applied at f° every row reachable from f°
by support moves has sum c val <= its value at f° (kappa > 0), with equality iff e^1 = e°, i.e. iff a^1 is proportional to a° on F°.  So the
drift -(kappa nu°/2)||Delta e||^2 created by the de-proportionalizing move can never be compensated by later support moves without undoing it.
(NDN) is therefore NOT removable by support moves alone (this corrects the natural guess that a small de-proportionalizing raise removes it).

## 3.5 Remark 3.5 (what (NDN) is, after Lemma 3.4)
(i) Exact (ND)-failure with (N1) (no usable coordinate of supp u off the support) makes the direction c one-sided for ALL moves of the
companion construction except the cut-off beyond N'' and window masses ON supp u; both are first-order but tail-sized or deep-mu-sized.
(ii) Value tuning in X2's route is needed for exact d-consistency (Lemma DC: kills the first-order junction mismatch, Proposition J) and in
X1's KN^tr for exact zeros (KN-1).  For d-consistency only the d-mismatch (rho/2) sum_k Domega(k)(nv'_k - nv_k) of each piece matters; a
residue along c of SECOND order (Pi^2) would be tolerated by Theorem UE^inf (it needs |kappa^+-| <= c delta s_1).  Lemma 3.4 gives second order
for the RAW values; the block norms A_m, which normalize the values, move at first order through peaks and non-Omega carriers, so a
second-order residue in normalized values requires in addition holding the block norms (one peak lever per block).  Whether this can always be
arranged is not checked: SKETCH/OPEN.
(iii) For a FIXED set of carriers, exact (ND)-failure forces a|_{F} to be proportional to a combination of carrier vectors restricted to F
(U2 Lemma ND); (NDN) at all large levels is a condition on a alone (U2 3.3), non-generic (fails after an arbitrarily small perturbation of a on
the tested coordinates), but not excluded by the design.

## 3.6 Theorem 3.6 (transport, SKETCH) and the precise remaining step
Statement (SKETCH).  For T_fin^* and every N, every f in S_{p_N*} with infinite base support satisfies (LSC-trunc) for every mate (indeed f
is in Rec_N), unless at all large main stages every clean sub-window exhibits (C*-residual of Q1's Master Theorem VI, read at the deep-raised
row) or (NDN^x), where (NDN^x) := (NDN) together with failure of the block-norm/peak levers of Remark 3.5(ii) for the corresponding blocks.
Route.  Per clean sub-window w of a main stage L: (1) deep raise f -> f^r beyond J (U2 DR-inf: clean classification preserved);
(2) Q1's companion construction at f^r, with levers replaced as in 3.3 (L1)-(L4); (3) transplanted window data with Lemma 3.1 and
Proposition 3.2 (cushion domination (U3^inf), C_+ <= Design/u); (4) Theorem UE^inf at the companion and Theorem E^{eng,RT,inf} along the
windows ((a) by V3 Lemma 2.3 for the raise plus Z3 Lemma 3.1 for the companion moves, eps' = o(T_lo^2)); the engineered approximants are
norm attaining with finite base support.
PROVED pieces: part 1 (LT), part 2 (UE^inf, E^{eng,RT,inf}), Lemma 3.1, Lemma 3.4; U2: Lemma P, DR-inf, TR-inf (L1)-(L4 robust), Lemma W
(for RS data); V3: RT, E_RT.  SKETCH pieces: Proposition 3.2 for Q1's data; the replacement of every lever of Q1's construction (KN^tr's
levers, Lemma DC's levers, V1's donors) by (L1)-(L4) with status stability (V1 Lemma ST) under the pair side effects (second order, harmless
by Lemma RR); window arithmetic with the new rate objects (eps).
THE PRECISE REMAINING STEP for (LSC-trunc) (given Q1): a line-by-line transport audit of Q1's per-window construction to an infinite-F,
deep-raised base row, with the four substitutions [a_min -> (U3^inf)], [finitebase -> smallness], [flips -> Lemma P projection + clamping],
[off-support levers -> (L1)-(L4)], and a decision on the degenerate configuration (NDN^x): either a block-norm-preserving lever argument
making the residue of Remark 3.5(ii) second order, or a proof that (NDN) at all large levels is incompatible with the (C*)-structure that
requires exact tuning.
