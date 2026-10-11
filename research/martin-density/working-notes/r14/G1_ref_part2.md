# G1-ref part 2: Lemma 2.1, Lemma 2.3, Theorem G1.A, Corollary G1.B, Remark 2.2

Checked against Part III: Def. III-cone, Lemma III-weightfree, Lemma III-floorrow, Lemma III-track, Lemma III-nodeep,
Prop. III-cushion, Lemma III-prep, Lemma III-CMtr (proof of (c), (d)), Prop. III-BR (U3), Lemma III-nocube, Lemma III-count,
Def. III-windowinf ((U3^inf), (U4^inf)), Def. III-approxinf, Lemma III-late; J1 Lemma J1.13 and J1-ref B.5.

## 2.1 The row list (G1 3.1) -- CORRECT
In the active variables the enlarged class cone has: (X3)_m (entries 1, -r_l), (X1) rows at coordinates of E_c(w) \ F^#
(contact sign rows, free equality rows; aggregated single-variable rows on S_l cap (L, s_far]), (X1^F) at tiny-support target
coordinates (Part III before Lemma III-track), (X4^0)/(X4)/(X4^U).  Signature sets of distinct coarse carriers are disjoint and
only target coordinates (T(L) subset [1, dbar(L)]) carry two coarse carriers, so every row with >= 2 variables is (X3), an (X1)
row at a target coordinate, or (X4)-type.  After (P1)-(P3) (or P^nat) every target coordinate in U_L carrying a contact or
(X1^F) row is an S_th support coordinate of f^P and f^# (Lemma III-prep (d)); free target coordinates have tiny room (closed,
then banked) or robust room (FR); robust support carries no row (Lemma III-nodeep (T)).  Verified.

## 2.2 Lemma 2.1 (tolerances) -- CORRECT (mod chain), precisions P-21a, P-21b
(a) Banked coordinate s (P2-bank or (P1)-closed-then-banked).  Prop. III-cushion (iv)/Lemma III-prep (c) use the cone point only
to make the route-V data at s contact-like: b^+ = chi V' + beta_s, b^- = -(1 - chi)V' + beta_s with z_s V' >= 0.  If z_s V'(s) =
-delta < 0, the symmetric split b^+ = V'/2 + beta_s, b^- = -V'/2 + beta_s keeps b^+ - b^- = V' and gives (z_s b^+)_- <= delta/2 +
|beta_s|, (z_s b^-)_+ <= delta/2 + |beta_s|; with |beta_s| <= 4Kt|a^#_s| <= |a^#_s|/t and delta <= 4|a^#_s|/t both are <=
3|a^#_s|/t, so (U3^inf) holds with C_+ = 5 already (G1's C'_+ = C_+ + 3 is safe).  (U3^inf) imposes nothing on b^theta at
support coordinates (Def. III-windowinf); b^theta(s) = beta_s is smaller than before, so (L1) of Lemma III-late (no S_th
coordinate in the raise set W_F) is unaffected.  The change of the normalization kappa = (b^+_1 + b^+_off)(zhat^#) is
<= sum_s delta_s <= 4 dbar(L) theta/t << Kt (theta/t <= theta/T <= T^3 T_hi (Des/u)^{C_T}), so |kappa| <= 2Kt and the base term
bound survives with a factor 2.
Raised tiny support j in F cap T(L).  In the deep assignment (Prop. III-cushion, proof (i)) the interval [y_j - A_j - tr_j,
x_j + A_j] is nonempty iff s_j V_c(j) >= -2A_j - tr_j.  Exact (X1^F) gave s_j V_c(j) >= -tr_j (Lemma III-nodeep (T)); a violation
delta gives >= -delta - tr_j, admissible for delta <= 2A_j.  With A_j := 2|a^#_j|/t (>= |a^r_j|/t, since raises and (P#1) give
|a^#_j| >= |a^r_j|/2) the flip-bound argument (|sigma_j| <= f^+_j + f^-_j + |(Delta B - V_c)_j|) is unchanged, and (s_j b^+_1)_-
<= A_j, (s_j(b^+_1 - V_c))_+... <= A_j + tr_j give (i) of Prop. III-cushion with 5|a^#_j|/t.  P-21a (notation): G1 writes "t r_j";
it is the single symbol tr_j (trace term of Lemma III-nodeep).
(b) In the proof of Lemma III-CMtr the kind-[3] verification uses (X4^0) at the cone point only through lambda_l vs_l
Delta omega^#(l) >= -C_f lambda_l(c_{L+1} + D^C c_{L+1}^2), compared with -3 lambda_l gap^#(l)/t; a violation v of the row (in its
natural units, Lemma III-floorrow (a): lambda_l vs_l Delta omega(l) = vs_l gamma_l + Delta'_m lambda_l rho_l) lowers the left side
by at most v.  Correct; (KN) clause likewise.
(c) Correct: (X3) is the definition of the true shift ([II, Lemma 5.58], U1 4.6) and (X1-FR) is V_proj = 0 at free coordinates,
whose only tolerance is (VT').  Classifying single-variable rows as strict is conservative and harmless (they create no tiny
minor; a minor containing a single-variable row is a design multiple of a minor of the other rows).
P-21b.  The "(X1-ag)" single-variable rows have entries alpha_l or -vs_l lambda_l alpha_l (robust-peak WEIGHTS); G1's definition
of "design numbers" (non-weight data) must include the weights of the robust peaks of active blocks and the weights of
(KN)-block carriers (Lemma III-weightfree (a) lists exactly these).  They are level-L data fixed before delta'_comb(L) is
computed, so the argument is unaffected; no weight Phi_d, d in N_T, enters (so genericity is unaffected).

## 2.3 Lemma 2.3 (soft tolerance) -- CORRECT, precision P-23
mu_tol = u min(theta_min, lambda_min g'_min)/(2^{L+2} Des^{C_r} K_X T_hi).  With theta_T = b T_hi (Des/u)^{C_T}: mu_tol >=
b (Des/u)^{C_T - C}; with theta_0 = b/Des^{C_P}: mu_tol >= b Q(w)/Des^{C} (T_hi <= 2^{-L^3}/(L Q(w))); the g'-term is >= b
Q(w)/Des^C when g'_min >= b/Des^C.  Re-derived.
P-23.  The claims "mu_tol >= Des^{10} b/u^{10}" and "a factor >= Des^5 to spare" against (1 + 2 Lip) b, and later (E2) against
Step-A^nat moves Lip W^nat/kappa_min ~ Des^{C_A + C_x + C} b/u^3, hold only if the absolute constant C_T is fixed AFTER the
exponents of Lip, K_X, C_A, C_x: C_T >= C_A + C_x + C_Lip + C_r + C + 10.  Then every soft tiny minor stays below mu_tol with
room.  (C_T absolute, so theta_T and b_bias remain as stated.)

## 2.4 Theorem G1.A (soft transplant) -- CORRECT after fixes P-A1, P-W, P-N
Verified: (SE) at r^# (strict minors: design numbers without (X3) row, 0 or >= delta'_comb >= u; with an (X3) row: rate
objects, robust >= u/2 or tiny and then 0 by (E1)); (MD) with (mu_tol, u/2) (all minors are rate objects, (I3)); Lemma CH on the
whole cone; the list of uses of the cone point in Prop. III-cushion and Lemma III-CMtr (c), (d) (exact (X3), exact (X1-FR),
contact/tiny-support signs -> Lemma 2.1 (a), inward rows -> Lemma 2.1 (b), closeness -> times H_CH).  I re-read both proofs and
Prop. III-BR (U3): the only other sign rows used there (class sign rows "(X2)" making Step-A banks contact-like, aggregated
rows fixing the orthant) are single-variable, hence strict.  No other use of the cone point.
P-A1 (closeness clause; statement gap).  (E3) requires only |r^# - r(f)| <= u/(4 Lip).  The proof needs the data violation
Lip |r^# - r(f)| K_X to be << K T_lo, which u/(4Lip) does not give (it gives u K_X/4).  The proof silently uses |r^# - r(f)| <=
Des^C b from Theorem G1.C.  FIX: replace the clause by |r^# - r(f)| <= eta'(w) (as in J1.13 (i) and Lemma III-floorrow (b),
which needs |r^(m) - r(f)^(m)| <= 2 eta' in (T)-blocks); then Lip eta' K_X <= Des^C T^4 << K T_lo.  The companions of Theorem G1.C
satisfy it (|r^# - r(f)| <= Des^C b/u^3 << eta').
P-W (window count; fixable gap).  H_CH = p^{p/2} Lambda^p/(u/2) is not of the form C(Des/u)^C: with (D-G1a) Des >= p^{p^2},
H_CH <= 2 Des^2 3^p u^{-p-1}, so the class threshold K_*(w) >= 6(H_CH(C_Gamma J + 1) + 1) is ~ B^{p+4} (B = 4Des/u) and
K_data ~ K_*^{J+2} K ~ B^{(p+4)(2L+2)+C}.  Lemma III-count (b) assumes K_* <= B^{C_*} with C_* ABSOLUTE and absorbs K_data by the
L^2 in the exponent of Q(w); that fails once p > C L.  G1's justification "omega(L) >= 2^p (the rate scheme contains all minors
of all patterns)" is not supported by the stated reason: one p x n matrix with n <= 2L << p has sum_k C(p,k)C(n,k) <= 4^L
(p+1)^{2L} minors, which is < 2^p for p large (the bound may still follow by counting PATTERNS, of which there are many, but
this is not written).  FIX (PROVED here): insert into the design (D-G1b) omega(L) >= 8(p(L) + 4)(L + 1) + C_K + 8.  It is a
level-L, f-free, N-free quantity (p(L) is computed from the patterns of level L); enlarging omega(L) only enlarges M(L), Q(w),
n(w) and lowers T_lo(w) (monotone insertion, Lemma III-designinf (d)).  Then (Lemma III-count (c)): log_B(D_cl K_data/c_flat) <=
L + 1 + (p(L)+4)(2L+2) + C_K + 4 <= omega(L) + L^2 + 20 - 2L, so |S| c_flat/K_data >= L 2^{L^3} and K_data T_hi(w) <= 2^{-L^3}/L.
(Alternatively the pigeonhole in Lemma CH can be run over the <= n rows of a basis instead of all p rows; not needed.)
P-N (normalization).  Lemma CH needs rows of norm <= 1; the class-cone rows in natural units have entries u_l(j), tau_m(j), 1,
r_l (<= 1), alpha_l, and in (X4^0) the entry m^2|r_l| K = lambda_l rho^0_l <= 2 lambda_l; multiply the (KN)-rows (X4) by lambda_l
(entries vs_l, lambda_l).  Then every row has norm <= 2(2L)^{1/2}, normalization divides a k x k minor by at most (8L)^{k/2} <=
(8L)^L <= Des^{1/2}, and the robust threshold of the normalized matrix is u/(2 Des^{1/2}); tiny minors only decrease.  So u is
replaced by u/(2Des^{1/2}) in H_CH and eta, i.e. Des^{C_r} -> Des^{C_r + 1} in mu_tol.  Harmless.
With P-A1, P-W, P-N the theorem holds as stated: the stage feeds Theorem E^{eng,RT,inf} with C_+ <= 8 and K_data multiplied by a
factor absorbed in the window count.

## 2.5 Corollary G1.B -- CORRECT (inspection), with P-B
(i) is Theorem G1.A.  (ii): moving the softly pinned ratios by <= D_tol each moves a soft minor by <= Lip (2L)^{1/2} D_tol; read
D_tol := mu_tol/(4 Lip (2L)^{1/2}) (P-B, constant).  (iii) J1.13 (ii) unchanged in form, with the margins of Theorem G1.C.
(iv) Cofactor polynomials (minors of the g_J) are not minors of the cone matrix, so they enter neither (MD) nor (SE); they
were rate objects only for A_max and the cube normalization of [II, Prop. 5.54 (c)-(e)], which route V omits (Lemma III-nocube,
Lemma III-nocubeinf; Lemma III-count counts classes only).  I re-read Lemma III-nocube's list: no other use.  Correct.
Note: J1.13 (ii)'s status margins (T: 1 - mu/2 with the Puiseux mu; U: 1 - eta'/2) are replaced at the linear scale by margins
~Des^{C_x} b (Theorem G1.C); that the downstream lemmas (III-PM, III-drift, III-late, (LATE)) accept these is G1's Lemma 3.3
(part 3 below).

## 2.6 Remark 2.2 (SKETCH) -- label honest
For an active-shift block, a mismatch Delta''_m - sum r_l gamma_l enters the peak traces -Delta'_m tau_m(j) at target coordinates
in supp tau_m and the far aggregated rows of the robust peaks (sign kept if |Delta'_m| >= A K t).  If every target coordinate of
supp tau_m is an S_th coordinate the mismatch only hits cushioned rows.  Plausible; the size bookkeeping (mismatch vs
4 theta_T/t at all scales of the class) is not written.  Not used.
