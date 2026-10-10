# U1 notes (Round 8): the finite-F residual (C*) of Master Theorem III — exact shifted data at companions

Setting: paper/martin_density_note.tex (notation as there), finite block set I = {1..N}, p = p_N, first rows f with FINITE base support F,
diagonal base.  Design: V2's D^{V2} on V1's D_Omega, rebuilt on U4's T_final and enlarged to D^{U1} (part 3).  Labels PROVED / SKETCH /
HEURISTIC / FALSE / OPEN; "PROVED" means: complete proof here, using only results that were refereed in earlier rounds (listed in 5.6).
This file = U1_head.md + U1_part1.md ... U1_part5.md (byte-identical copies).  Numerics: r8/U1_work/.

## 0. Summary
Task: complete V2's Theorem C6 by closing (C*-1) exact absorption of fine residues on coarse free coordinates, (C*-2) (SC) at companions
for blocks with Delta d < 0, (C*-3) exactification of the block scalars, (C*-4) one shift direction along a window, (C*-5) the joint
completion/absorption fixed point; deliver MASTER THEOREM IV or the precise remaining step.

What is proved.
 (1) STRUCTURE (part 1).  Exact two-piece data at a first row f' exist iff the single certificate V(Domega) = sum_m R_m^*(Domega_m -
     d'_m(Domega_m) w'_m) is z'-admissible off F' (Lemma 1.1).  Every carrier outside the switching support enters V with the FORCED coefficient
     -Delta_m lambda_l w'(l); the shift of a block is tied to the switching values by the DATA IDENTITY
         Delta'_m kappa'_m = sum_{l in Omega_m} u_l(zhat') gamma_l,   kappa' = A' + theta' Phi_P^2 + (1/theta') sum_{Q \ Omega} nu'^2 Phi^2   (Lemma 1.3),
     so ONE scalar per block (kappa) enters, not the two scalars (theta, A) of V2's gap (C*-3); kappa is tuned by one push of a buffer peak
     with derivative 1 - X >= 3/4 (Lemmas 1.4, 1.5).  Numerically verified to 1e-15 (identities) and 1e-32 (derivatives, 60 digits).
 (2) (C*-3), (C*-4) (part 2).  Data shifts are bounded (Lemma 2.1); scales are sorted into finitely many ACTIVITY CLASSES (2.3); inside a
     class the data are projected onto the shifted exact cone Gamma^# (Hoffman via V2 Lemma H) and NORMALIZED to one common shift ray by
     increments added to the minus side only (Proposition 2.2: the represented functional is untouched, sqrt(Gamma) grows by O(epsilon));
     the cone is exactified by V2's Lojasiewicz Lemma L in the variables (u_Omega, kappa) and realized by V1's Lemma TU plus one kappa-push
     per block (Theorem 2.3); averaging over a SUBSET of the scales of a window is allowed (Lemma 2.4).
 (3) (C*-1) (part 3).  The design D^{U1} adds ZERO-VALUE ABSORBERS: biased pairs of block-1 carriers whose targets carry fresh binary
     tuning coordinates, placed in a cluster right after every main stage and as deep pairs before any main target can reach a signature
     coordinate (rule (c'')).  The first two carriers meeting any coarse coordinate after the main stage form such a pair (Lemma 3.2); tuned
     to value EXACTLY zero (Lemma 3.3) they carry no d-effect and no kappa-effect, and their switching coefficients cancel the fine residue at
     every coarse coordinate exactly (Proposition 3.4).  D^{U1} is admissible, N-free, and every refereed tool survives (Theorem 3.1).
 (4) (C*-2), (C*-5) for ONE-SIGNED classes (part 4).  Moves are ordered so that nothing feeds back: coarse realization, absorber tuning,
     re-push, then the fine structure on J_fine.  Configuration (i) (all active shifts negative): an ownership recursion makes every fine
     carrier of an active block a robust SELF-ALIGNED peak (Lemma 4.1); the first carrier with a nonzero coefficient dominates V at each
     coordinate (Lemma 4.2, using the weight rule (W4''), numerically necessary); hence V is admissible for every shift vector of the class
     and (SC) holds at the companion with any sequence (Lemma 4.3).  Configuration (ii) (all positive): Schauder-Tychonoff completion
     (Lemma 4.4, V2 Lemma C5).  Reference versus true shifts are reconciled exactly (Lemma 4.6); costs are o(T_lo^2) (Lemma 4.5).
 (5) Mixed classes (part 5).  Exactness holds in EVERY class (Lemma 5.1); only (SC) for the negative blocks can fail.  At any exact
     completion a negative fine carrier is in one of three states (Z') small value, (R) self-aligned robust peak, (W) wrong branch (Lemma
     5.2), and (SC) holds unless some (W) carrier has its value in a threshold band of width ~Phi^{1/2} (Lemma 5.3).  The forward recursion
     survives mixing unless a positive carrier is FRUSTRATED (|Y| < own mass) (Lemma 5.4); frustration forces zero cascades that can force
     (W) (toy model, 5.5).

MASTER THEOREM IV (5.6).  PROVED.  D^{U1}, N fixed, F finite.  If for infinitely many main stages L some clean sub-window w of L has at
least n(w)/D_cls(w) scales in ONE-SIGNED activity classes, then f in Rec(p_N).
 Corollary IV.1.  For N = 1 every class is one-signed: EVERY f with finite F is in Rec(p_1) (finite-F Lemma Z for p_1).
 Corollary IV.4 (intrinsic).  If for infinitely many main stages some clean sub-window has I_up(w) = {} or I_lo(w) = {}, then f in Rec(p_N).
 Corollary IV.2.  A finite-F counterexample for p_N (N >= 2) must have, at every large main stage and every clean sub-window, both
 source deficiencies (I_up, I_lo nonempty) actively shifted at all but a 1/D_cls fraction of the scales, with frustrated positive carriers.

THE PRECISE REMAINING STEP (C_mix) (5.7).  OPEN.  In a mixed class, find an exact completion (exists, Lemma 5.1) at which no negative fine
carrier has its value in its threshold band B_l = (thr_l (1 - Phi_l^{1/2}/M), thr_l + Phi_l^{1/2}).  Bad carriers need the coincidence
own_l - |Y_l| in B_l (measure ~Phi_l^{1/2}); toy data: forced wrong branches occur (3/115), bad ones only with artificially thick bands.
(C_mix) follows from U3's open uniformity step (S2) (violation tolerance), SKETCH of the reduction in 5.7(c).
Not claimed: transfer to Martin's p (the one-signed hypothesis is not N-independent); infinite F (U2's items).

Corrections recorded (5.8): V2's near-coordinate conversion is FALSE as stated (Cantor-set obstruction); V2's two-scalar exactification
is unnecessary (kappa-reduction); this round's part 4 needed c_0(a) > 0 on unused tuned absorbers; a first numerical toy violated (W4'').

## Results table
| # | Result | Status | Where |
|---|---|---|---|
| 1 | Lemma 1.1 exactness certificate V(Domega) | PROVED | 1.1 |
| 2 | Lemma 1.2 threshold identities (E1), (E2) | PROVED (+ numerics) | 1.2 |
| 3 | Lemma 1.3 data identity, kappa-reduction | PROVED (+ numerics) | 1.3 |
| 4 | Lemma 1.4 derivatives of kappa | PROVED (+ 60-digit numerics) | 1.4 |
| 5 | Lemma 1.5 kappa tunable by one buffer-peak push (final form) | PROVED | 1.5 |
| 6 | Lemma 2.1 shift bound | PROVED (+ numerics) | 2.2 |
| 7 | Activity classes | PROVED | 2.3 |
| 8 | Proposition 2.2 projection and normalization to one ray (C*-4) | PROVED (modulo V1 TR, refereed) | 2.4 |
| 9 | Theorem 2.3 exactification with one scalar per block (C*-3) | PROVED | 2.5 |
| 10 | Lemma 2.4 subset averaging | PROVED | 2.6 |
| 11 | Theorem 3.1 D^{U1} admissible, N-free, tools survive | PROVED | 3.2 |
| 12 | Lemma 3.2 first touchers are absorber pairs | PROVED | 3.3 |
| 13 | Lemma 3.3 zero-value tuning, biased pairs | PROVED | 3.4 |
| 14 | Proposition 3.4 exact absorption on coarse coordinates (C*-1) | PROVED | 3.5 |
| 15 | Lemma 4.1 robust self-aligned recursion (configuration (i)) | PROVED (+ numerics) | 4.2 |
| 16 | Lemma 4.2 owner dominance under (W4'') | PROVED (+ numerics) | 4.3 |
| 17 | Lemma 4.3 (SC) at the companion, configuration (i) (C*-2) | PROVED | 4.4 |
| 18 | Lemma 4.4 Schauder completion, configuration (ii) | PROVED | 4.5 |
| 19 | Lemma 4.5 cost and statuses | PROVED | 4.6 |
| 20 | Lemma 4.6 reference versus true shift; move order (C*-5) | PROVED | 4.1, 4.7 |
| 21 | Lemma 5.1 exactness in mixed classes | PROVED | 5.1 |
| 22 | Lemma 5.2 three states of a negative carrier | PROVED | 5.2 |
| 23 | Lemma 5.3 (SC) criterion tolerating wrong branches | PROVED | 5.3 |
| 24 | Lemma 5.4 mixed recursion without frustration | PROVED | 5.4 |
| 25 | Toy evidence on mixed classes | HEURISTIC | 5.5 |
| 26 | MASTER THEOREM IV (one-signed classes) | PROVED | 5.6 |
| 27 | Corollary IV.1 (N = 1: all finite-F rows recovered) | PROVED | 5.6 |
| 28 | Corollary IV.2 (shape of a counterexample) | PROVED | 5.6 |
| 29 | Corollary IV.3 (mixed without frustration) | PROVED | 5.6 |
| 30 | Corollary IV.4 (intrinsic: one source type deficient) | PROVED (modulo V1 Lemma 3.4', refereed) | 5.6 |
| 31 | (C_mix): mixed classes, (SC) at an exact completion | OPEN | 5.7 |
| 32 | (C_mix) follows from U3's (S2) | SKETCH | 5.7(c) |
| 33 | V2's near-coordinate conversion | FALSE as stated | 5.8 |

## Numerics (r8/U1_work/)
 kappa_check.py (+ kappa_lib.py): 307 random blocks; (E1) 8.5e-16, (E2) 7.8e-16, two forms of kappa 3.1e-16, identity (1.3) 3.0e-15,
   duality 2.2e-16 (finite-difference derivative checks 3e-4 / 2e-2 are step-size noise, superseded by kappa_check2).
 kappa_check2.py (mpmath, 60 digits, central differences h = 1e-30): Lemma 1.4 (a), (b), (c) on 211 / 127 / 117 tests, max relative
   errors 2.1e-32, 6.5e-33, 6.4e-33.
 shift_bound_check.py: Lemma 2.1 on 5220 tests, max d^2/bound = 1.0000000000000007 (rounding), equality attained at x = w 1_Omega;
   min (1 - chi)/(M^2 Phi_P^2/C^2) = 0.9999999999999992 (>= 1 up to rounding; equality when Omega = Q).
 recursion_check.py (first toy; later targets ignore (W4'')): admissibility FAILS — the toy, not the lemma, was wrong.
 recursion_check2.py: with (W4'') enforced, 200 instances x 50 shift vectors: all carriers robust self-aligned peaks, V z-signed at every
   coordinate; with (W4'') violated, 27% of the instances fail.
 mixed_fixedpoint_check.py, mixed_forcedW_check.py, mixed_bad_inspect.py: lexicographic model of mixed classes (5.5).

# U1 part 1 — Exact shifted data: the exactness equation and the kappa-reduction of the block scalars

Setting: paper/martin_density_note.tex (Sections 1, 7, 8), finite block set I = {1..N}, p = p_N, first rows with finite base support.
Design: D^{V2} on V1's D_Omega (diagonal base), enlarged in part 3 to D^{U1}.  Notation of V1/V2: carrier l = j(k,m), u_l, lambda_l =
m Phi_l, v_l(s) = delta_l 2^{-s}/n_l on S_l; at a first row f' (forced data a', z', zhat', w', F', K' = contacts off F') put
zeta'_m := R_m^** zhat', A'_m := |zeta'_m|_m, M'_m, C'_m (lem:threshold), theta'_m := A'_m M'_m / C'_m, nu'_k := |zeta'_m(k)|/Phi_k^2,
P'_m (peaks) = {nu' >= theta'}, Q'_m = complement, Phi_P^2 := sum_{k in P'_m} Phi_k^2.  A coordinate j notin F' is a CONTACT if |z'_j| = 1
and FREE if |z'_j| < 1.  A vector V in l_1 is z'-ADMISSIBLE if V(j) = 0 at free j and z'_j V(j) >= 0 at contacts (no condition on F').
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.0 What (C*) asks for
By V2 Master Theorem III' (refereed) f notin Rec only if (C*): at all but finitely many levels every clean sub-window w has rho^sh <= b(w)
and c_pi(w) <= b(w), i.e. the shift Delta d_m of the decompositions is not pinned in the source-deficient blocks I_sh(w) = I_up(w) ∪ I_lo(w).
By V2 Proposition C4, a mate whose profile oscillates on the signature set of a robust class-G peak cannot be followed by d-neutral data at
any first row sharing that peak; so the window data must be SHIFTED (Delta != 0), and by V2 Proposition C3 shifted data are exact only if
the infinite vector W_Delta = sum_m Delta_m R_m^* w'_m is admissible off the data support.  Theorem E (Z3), E'' (V1), E_RT (V3) average
EXACT window data at ONE companion.  The five gaps of V2's Theorem C6 are: (C*-1) absorption of fine residues on coarse free coordinates,
(C*-2) (SC) at companions for Delta < 0 blocks, (C*-3) exactification of block scalars, (C*-4) scale-dependent shift directions,
(C*-5) the joint completion/absorption fixed point.  This part isolates the exact algebraic structure; parts 2-4 treat the gaps.

## 1.1 Lemma 1.1 (exactness depends only on the switching difference).  PROVED.
Let f' be a first row with F' finite, Omega_m ⊂ Q'_m finite, omega^+-_m in c_00 supported in Omega_m.  Put Domega := omega^- - omega^+,
Delta_m := d'_m(omega^-_m) - d'_m(omega^+_m) = d'_m(Domega_m) (d'_m(x) := <D_m w'_m, D_m x>/C'_m), and the CERTIFICATE FUNCTIONAL
    V(Domega) := sum_m R_m^*( Domega_m - d'_m(Domega_m) w'_m ).
(a) V(Domega) = sum_l gamma_l u_l with gamma_l := lambda_l ( Domega_{m(l)}(k(l)) - Delta_{m(l)} w'_{m(l)}(k(l)) ) for EVERY carrier l
    (Domega = 0 off Omega).  In particular every carrier outside Omega enters with the forced coefficient -Delta_m lambda_l w'(k(l)) (at peaks
    -Delta_m lambda_l vs_l M'_m), and the carriers of Omega with a coefficient gamma_l that can be prescribed freely by Domega.
(b) If (b^+-, omega^+-) are two-piece data at f' (Definition def:twopiece), then b^+ - b^- = V(Domega), hence V(Domega) 1_{F'^c} is
    z'-admissible.
(c) Conversely, let omega^+ be supported in Omega, Domega supported in Omega with V := V(Domega) 1_{F'^c} z'-admissible, let beta be supported
    in F', chi : K' -> [0,1], and put b^+ := beta + chi V 1_{K'}, b^- := b^+ - V(Domega), omega^- := omega^+ + Domega.  Then (b^+, omega^+),
    (b^-, omega^-) are two-piece data for g := b^+ + sum_m R_m^*(omega^+_m - d'_m(omega^+_m) w'_m) with Delta d = Delta (as above).
Proof.  (a) R_m^* x = sum_k lambda_{k,m} x(k) u_{k,m} (eq:Lstar).  (b) Subtract the two representations of g (as in V2 Proposition C3):
0 = b^+ - b^- + sum_m R_m^*((omega^+ - omega^-) - (d'(omega^+) - d'(omega^-)) w') = b^+ - b^- - V(Domega); side admissibility of b^+ and b^-
gives: off F' u K' both vanish, and on K', z' b^+ >= 0 >= z' b^-, so z'(b^+ - b^-) >= 0.  (c) Off F', b^+ = chi V is z'-signed on K' and 0
at free coordinates; b^- = chi V - V = -(1 - chi) V off F' (V(Domega) = V there), (-z')-signed.  The second representation: b^- + sum R^*
(omega^- - d'(omega^-) w') = b^+ - V(Domega) + sum R^*(omega^+ - d'(omega^+)w') + V(Domega) = g.  QED
So the existence of exact two-piece data is a property of the single vector Domega: V(Domega) must be z'-admissible.  Its restriction to a
coordinate j is a finite sum over Omega plus the infinite series -sum_m Delta_m sum_{l notin Omega, m(l)=m} lambda_l w'(k(l)) u_l(j).

## 1.2 Lemma 1.2 (two threshold identities).  PROVED.
For every block of a first row:   (E1) sum_{k in P} Phi_k^2 (nu_k - theta) = A,      (E2) A^2 = theta^2 Phi_P^2 + sum_{k in Q} nu_k^2 Phi_k^2,
and M = theta/(A + theta), C = A/(A + theta).
Proof.  lem:threshold: zeta/A = alpha + D^2 w/C, ||alpha||_1 = 1, supp alpha ⊂ P with matching signs.  At k in P, w(k) = vs_k M, so
|zeta(k)|/A = |alpha(k)| + Phi_k^2 M/C; with theta = AM/C this is |alpha(k)| = Phi_k^2 (nu_k - theta)/A; summing gives (E1).  Off P,
w(k) = C zeta(k)/(Phi_k^2 A).  Hence C^2 = ||Dw||_2^2 = M^2 Phi_P^2 + (C^2/A^2) sum_Q nu_k^2 Phi_k^2; divide by C^2 and use M/C = theta/A: (E2).
From theta = AM/C and M + C = 1: M = theta C/A = theta(1 - M)/A, so M = theta/(A + theta), C = A/(A + theta).  QED

## 1.3 Lemma 1.3 (the data identity: ONE block scalar).  PROVED.
In the situation of Lemma 1.1 put, for each block m, Delta'_m := Delta_m M'_m and
    kappa'_m(Omega) := [ A'(A' + theta') - sum_{k in Omega_m} nu'_k^2 Phi_k^2 ] / theta'  =  A' + theta' Phi_P^2 + (1/theta') sum_{k in Q'_m \ Omega_m} nu'_k^2 Phi_k^2.
Then for every m
    Delta'_m kappa'_m(Omega) = sum_{l in Omega_m} u_l(zhat') gamma_l.                                                    (1.3)
Proof.  At k in Q', Phi_k w'(k)/(m C') = zeta'(k)/(m Phi_k A') = u_k(zhat')/A' and Phi_k^2 w'(k)^2/C' = C' nu_k^2 Phi_k^2/A'^2.  By
definition of gamma, Domega(k) = gamma_k/lambda_k + Delta w'(k) on Omega, so Delta = d'(Domega) = sum_Omega Phi^2 w'(gamma/lambda + Delta w')/C'
= (1/A') sum_Omega u_k(zhat') gamma_k + Delta (C'/A'^2) sum_Omega nu^2 Phi^2.  Multiply by A'^2/C' = A'(A' + theta') (Lemma 1.2) and divide
by (A' + theta')/theta' = 1/M': Delta M' [A'(A'+theta') - sum_Omega nu^2 Phi^2]/theta' = sum_Omega u_k gamma_k.  The second expression of kappa'
is (E2).  QED
Consequence (kappa-REDUCTION).  Write the exactness conditions of Lemma 1.1 in the variables (Delta'_m)_m and (gamma_l)_{l in Omega}: at a
coordinate j the coarse part of V(Domega)(j) is sum_{l in Omega} gamma_l u_l(j) - sum_m Delta'_m sum_{l coarse peak notin Omega, m(l)=m}
vs_l lambda_l u_l(j) - sum_m (Delta'_m/M'_m) sum_{l coarse non-peak notin Omega} lambda_l w'(k(l)) u_l(j).  At a clean sub-window every coarse
carrier outside Omega that is not a peak is either exactified to w' = 0 (nearly neutral, V1/V2) or kept in Omega (V1's kept/clamped
carriers; part 2), so the coarse coefficients are DESIGN numbers (lambda_l u_l(j)) times combinatorial signs, and the only f'-dependent
coefficients of the whole coarse exact system are the VALUES u_l(zhat') (l in Omega) in (1.3) and ONE scalar kappa'_m per block.  (The
fine part, carriers > l, is handled in parts 3-4.)  In particular V2's gap (C*-3) "independent exactification of theta_m and A_m" is not
needed: one scalar per block enters.

## 1.4 Lemma 1.4 (derivatives of kappa).  PROVED.
Fix a block and Omega ⊂ Q.  Put X := C sum_{k in Q\Omega} nu_k^2 Phi_k^2 / (theta^2 Phi_P^2) >= 0.  As long as the peak set does not change:
(a) an outward push |zeta(c)| -> |zeta(c)| + s of a peak c gives dtheta/ds = C/Phi_P^2, dA/ds = M, and d kappa/ds = 1 - X;
(b) a push |zeta(d)| -> |zeta(d)| + s of a strict non-peak d in Q \ Omega gives dtheta/ds = -rho_d M/Phi_P^2, dA/ds = rho_d M and
    d kappa/ds = rho_d (2 + M X/C), rho_d := nu_d/theta;
(c) a push of a strict non-peak d in Omega gives d kappa/ds = rho_d M X/C (and changes the value u_d(zhat), a variable of (1.3)).
Proof.  Differentiate (E1), (E2) (Lemma 1.2) with P fixed.  (a) nu_c grows by s/Phi_c^2: (E1) gives ds - Phi_P^2 dtheta = dA, (E2) gives
A dA = theta Phi_P^2 dtheta; so dtheta = A ds/(Phi_P^2(A + theta)) = C ds/Phi_P^2 and dA = M ds.  kappa = A + theta Phi_P^2 + S/theta with
S := sum_{Q\Omega} nu^2 Phi^2 unchanged: dkappa = M ds + C ds - (S/theta^2) C ds/Phi_P^2 = (1 - X) ds.  (b) (E1): -Phi_P^2 dtheta = dA;
(E2): A dA = theta Phi_P^2 dtheta + nu_d ds; so dtheta = -nu_d ds/(Phi_P^2 (A + theta)) = -rho_d M ds/Phi_P^2, dA = rho_d M ds, and
dS = 2 nu_d ds: dkappa = dA + Phi_P^2 dtheta + 2 nu_d ds/theta - (S/theta^2) dtheta = rho_d(2 + M X/C) ds.  (c) as (b) without dS.  QED
Numerics: U1_work/kappa_check.py (random blocks; (E1), (E2), the two expressions of kappa, (a), (b) by finite differences and the identity
(1.3) with random omega^+-): see part 5 for the output.

## 1.5 Lemma 1.5 (kappa is tunable with a robust derivative at a clean sub-window).  PROVED (given V1/V2's classification).
FINAL FORM (used in parts 2-5).  In parts 2-4 Omega_m is ALL coarse strict non-peaks of block m (plus the absorbers of part 3, whose
values are exactly 0, so nu = 0 and they contribute nothing to kappa).  Then Q_m \ Omega_m consists of FINE carriers only, and
   X_m = C sum_{k in Q\Omega} rho_k^2 Phi_k^2 / Phi_P^2 <= C (sum_{k fine} Phi_k^2) / Phi_c^2 <= C b(w)^2 D(l)^2 <= 1/4
(rho_k < 1 for strict non-peaks; sum_{fine} Phi_k^2 <= b(w)^2 by Theorem 1'(a) of V1; Phi_P^2 >= Phi_c^2 >= D(l)^{-2} for the coarse peak
c of Lemma D; 4 C b^2 D(l)^2 < 1 for l >= l_f, the same inequality used in the proof below).  Hence alternative (i) below ALWAYS holds:
the buffer peak push of Lemma 1.4(a) has d kappa/ds = 1 - X_m in [3/4, 1].  Alternative (ii) is kept only for the record (it is the form
needed if one insists on keeping some coarse strict non-peaks outside Omega).
ORIGINAL FORM.
Let w be a clean sub-window of level l >= l_f, f^(2) a companion obtained by V1's moves (C1)-(C3) (rates moved by <= Design b), m a block,
Omega_m := the kept and clamped coarse strict non-peaks of block m at f^(2) together with the absorbers of part 3 (all strict non-peaks).
Then at least one of the following holds:
 (i) X_m <= 1/2, and the buffer peak c_m of V2 Lemma 2.3 / the donor of V1 (a coarse peak with rho >= 1+u, Lemma D) has d kappa/ds >= 1/2;
 (ii) some coarse strict non-peak d in Q_m \ Omega_m with rho_d >= u(w)/2 exists, and d kappa/ds_d >= u(w).
In both cases the pushed carrier is not a variable of (1.3) (it is not in Omega_m), and two-sided pushes of size <= T_lo^4 are available
by V1's tools (z-moves / pulls / banks on the far part of its signature set; Lemma TU), leaving the peak sets unchanged (margins and gaps of
the coarse carriers are >= c_f Lam = c_f T_lo^3 or robust, V1 Lemma ST; fine carriers have margins >= their signature room, part 4).
Proof.  If X_m <= 1/2, Lemma 1.4(a).  Otherwise sum_{Q\Omega} rho_d^2 Phi_d^2 = theta^{-2} sum nu^2 Phi^2 = X Phi_P^2/C > Phi_P^2/(2C).  Fine
carriers of a block contribute at most sum_{k fine} Phi_k^2 <= b(w)^2 (Theorem 1'(a) of V1: sum_{l'>l} c_{l'} <= b^2); Phi_P^2 >= Phi_c^2 >=
D(l)^{-2} for the coarse peak c of Lemma D.  If every coarse d in Q\Omega had rho_d <= b(w) (the alternative at a clean w, rate object (R4)),
then sum rho^2 Phi^2 <= b^2 + b^2 < D(l)^{-2}/(2C) for l >= l_f, a contradiction.  So some coarse d in Q\Omega has rho_d >= u(w), and
Lemma 1.4(b) gives dkappa/ds_d >= 2 rho_d >= 2u.  The pushes: V1 Lemma TU realizes value changes of size <= c_T on any carrier exactly
swallowed far out; for a carrier with room on its far part a direct z-move on far free coordinates is two-sided; status stability as in V1
Lemma ST since T_lo^4 << Lam.  QED
Remark.  (1.3) shows why V2 needed two scalars: it used theta_m and A_m separately; the combination kappa'_m is the only one entering.
The realization of a Lojasiewicz point (part 2) therefore needs one push per block, and Lemma 1.5 supplies it in every block without any
hypothesis.  This closes (C*-3) (PROVED modulo the assembly of part 2).

# U1 part 2 — The shifted exact cone, a shift bound, normalization to ONE shift ray, subset averaging, exactification

Setting of part 1.  w = (l, i) is a clean sub-window of a MAIN level l (part 3) of D^{U1}, l >= l_f; t ranges over the dyadic scales of
W(w); (B_+-, Theta_+-) is a two-sided decomposition of g in C(f) at scale t; V1's classification (2.2), its moves (C1)-(C3), Lemmas
D, ST, NS, RR are used verbatim (refereed).  K denotes constants of the form C_f (Design(l)/u(w))^{C}; they are absorbed by the window
arithmetic (Q(w) of part 3).  "Decomposition convention": delta_m := Delta d_m M_m (Delta d = d_+ - d_-); "data convention":
Delta_m := d(omega^-) - d(omega^+), Delta'_m := Delta_m M^#_m.  Matching: Delta'_m <-> -delta_m (V2-ref 9(g)).

## 2.1 The shifted exact cone Gamma^# of a pattern
Let f^# be the companion of part 4 (V1's moves, the realization moves of 2.5, the fine structure and the absorbers).  Put
Omega := all coarse strict non-peaks of f^# (kept, clamped and class-R ones; every carrier of V1's Kp(w) is one, V1 Lemma ST(c)), and
coarse PEAKS of f^# with their signs vs_l.  For (Delta', gamma) in R^I x R^Omega define the coarse vector
    L(Delta', gamma) := sum_{l in Omega} gamma_l u_l - sum_m Delta'_m sum_{l coarse peak of f^#, m(l) = m} vs_l lambda_l u_l
restricted to the COARSE coordinates E_c := T(l) ∪ union_{l'' <= l} (S_{l''} ∩ [1, s_far(w)]) minus F^#, where s_far(w) is the least s with
2^{-s} <= c_{l+1}^2 (<= b(w)^4; part 3).  (Every coarse carrier is either a strict non-peak of f^#, hence in Omega (nearly neutral carriers exactified to
w^# = 0 by V2 Theorem B are strict non-peaks of value 0), or a peak of f^#, entering through its trace.)  Gamma^#(kappa) is the set of
(Delta', gamma) with
 (X1) L(Delta', gamma) is z^#-admissible on E_c (zero at free coordinates, z^#-signed at contacts);
 (X2) eps_l gamma_l >= 0 is implied by (X1) at the contacts of S^nat_l for class-G l in Omega; Delta'_m eps_l vs_l <= 0 for class-G peaks
      (implied by (X1) on S^nat_l likewise); gamma_l = 0 for class-R l in Omega (implied by (X1) at the free coordinates of S^nat_l);
 (X3) Delta'_m kappa^#_m(Omega) = sum_{l in Omega_m} u_l(zhat^#) gamma_l   (Lemma 1.3);
 (X4) vs_l gamma_l >= 0 ... the inward sign rows of the kind-[3] carriers (V1 TR(iii)) written for the - side increment (see 2.4);
 (X5) for an ACTIVITY CLASS a (2.3): gamma_l = 0 and Delta'_m = 0 for the components declared inactive in a.
Gamma^#(kappa, a) is a polyhedral cone.  By Lemma 1.3 its coefficients are design numbers lambda_l u_l(j), signs, the values u_l(zhat^#)
(l in Omega) and one scalar kappa^#_m per block; the pattern kappa = (Omega, peaks, signs, types of E_c-coordinates at f^#, activity
class) ranges over a design-countable, N-free set (subsets of [1,l] and of E_c, sign vectors).
Fine carriers do not appear in Gamma^#: their contributions to V(Domega) on E_c are the FINE RESIDUES absorbed in part 3, and on the
fine coordinates they are made admissible by the fine structure of part 4.

## 2.2 Lemma 2.1 (data shifts are bounded).  PROVED.
Let (b^+-, omega^+-) be two-piece data at a first row f' with Gamma'_w <= 2.  Then for every block m
    |Delta_m| <= ( 8 C'^3_m / (sigma'_m M'^2_m Phi_{P'_m}^2) )^{1/2}.
Proof.  Domega := omega^- - omega^+ is supported in Omega_m ⊂ Q'_m and H_m(omega^+-) <= 2/sigma'_m, so (sqrt H is a seminorm)
H_m(Domega) <= 8/sigma'_m.  Write D Domega = a D(w'1_Omega) + y with y ⊥ D(w'1_Omega) (in l_2(Omega)), and chi := ||D w' 1_Omega||^2/C'^2.
Then Delta = d'(Domega) = <D w' 1_Omega, D Domega>/C' = a C' chi, and ||P^perp D Domega||^2 = ||D Domega||^2 - <Dw', D Domega>^2/C'^2 >=
a^2 C'^2 chi (1 - chi), i.e. H(Domega) >= a^2 C' chi(1 - chi).  Hence Delta^2 <= H(Domega) C' chi/(1 - chi), and 1 - chi >= ||D w' 1_{P'}||^2/C'^2
= M'^2 Phi_P^2/C'^2 because Omega ⊂ Q'.  QED
At the companions f^# of the windows of f, C^#, sigma^#, M^# are within C Design Lam of those of f (V1 Lemma CO) and P^# contains a fixed
non-degenerate peak c_0 of every block of f (margins persist), so |Delta'_m| <= Delta_max := C_f (an f-constant) for all data with Gamma <= 2.

## 2.3 Activity classes (pigeonhole over finitely many classes).  PROVED.
Let J(w) := |Omega| + N (number of components of (gamma, Delta')), and fix thresholds A_1 < A_2 < ... < A_{J+2} with A_{i+1} := K_* A_i,
A_1 := K_*, K_* := the constant of the projection in 2.4 (a constant K of the above form).  For a projected data vector (2.4) at scale t,
among the J+1 intervals [A_i K t, A_{i+1} K t) (1 <= i <= J+1) one contains no |component|; let i(t) be the least such i.  The ACTIVITY
CLASS of t is a(t) := (i(t), the set of components with |.| >= A_{i(t)+1} K t, their signs).  Components below A_{i(t)} K t are set to 0
(cost <= J A_{i(t)} K t, again of the form K t).  The number of classes is <= (J+1) 3^J, a design number.
Proof.  Pigeonhole (J components, J+1 intervals).  QED

## 2.4 Proposition 2.2 (projection onto Gamma^#, normalization to one shift ray).  PROVED (modulo V1 TR, refereed, for the routine steps).
For every scale t of W(w) let (Delta'_dec(t), gamma_dec(t)) be the coarse data read off the decomposition: Delta'_m := -delta_m (blocks of
I_sh(w)), := 0 for the other blocks (|delta_m| <= K_d t there, V1 Lemma 3.4'); gamma_dec,l := -Delta theta_l (l in Omega).  Then:
(a) the violations of (X1)-(X4) by (Delta'_dec, gamma_dec) at the coefficients of f^# are <= K t;
(b) by Lemma H (V2) and the exactification of 2.5 (all minors of Gamma^#(kappa, a) are 0 or >= u(w)/Design(l)^C), the l_1-projection onto
    Gamma^#(kappa, a(t)) moves (Delta'_dec, gamma_dec) by <= K t;
(c) NORMALIZATION.  Let g_1, ..., g_p be the nonzero Delta'-projections of the extreme rays r_1, ..., r_p of Gamma^#(kappa, a)
    (normalized ||r_j||_1 = 1).  Write each projected Delta'(t) = sum_j a_j(t) g_j with a(t) in [0, A_max]^p, chosen by a fixed rule
    (a basic solution, Caratheodory); A_max <= C_f (Design/u)^C (inverse of a nonsingular design/value matrix with minors >= u/Design^C,
    and |Delta'(t)| <= Delta_max by Lemma 2.1).  Partition [0, A_max]^p into cubes of side epsilon; for a set S of scales whose
    coefficient vectors a(t) lie in ONE cube with corner a^max (coordinatewise maximum over the cube), put
        Delta'^* := sum_j a^max_j g_j,      incr(t) := sum_j (a^max_j - a_j(t)) r_j  in Gamma^#(kappa, a),
    so that Delta'(t) + Delta'(incr(t)) = Delta'^* for every t in S and ||incr(t)||_1 <= p epsilon.
(d) The number of (activity class, cube) pairs is <= D_cls(w) := (J+1) 3^J (A_max/epsilon)^p, a quantity of the form (Design(l)/u(w))^{C'}
    once epsilon := c_f (u/Design)^C is fixed by (e).
(e) DATA with the common shift.  For t in S define, as in V1 Proposition TR Steps 4-5 (split, data, balancing; banks, pulls, donors):
    omega^+ := the clamped decomposition omega_+ (V1 Step 5), Domega(t) := the vector with gamma = gamma_proj(t) + gamma(incr(t)) on Omega and
    shift Delta'^* (i.e. Domega(k) = gamma_k/lambda_k + Delta_m w^#(k), Delta_m := Delta'^*_m/M^#_m), plus the absorber coefficients of part 3
    and the far parts fixed in part 4; omega^- := omega^+ + Domega(t); b^+ := beta + chi V_proj (V1 Step 4, the split of the + side of the
    decomposition with respect to the PROJECTED coarse vector) + chi_f V_fine (any chi_f in [0,1] on the fine contacts); b^- := b^+ - V(Domega(t)).
    Then (b^+-, omega^+-) are exact two-piece data at f^# (Lemma 1.1(c)) with Delta' = Delta'^* for every t in S, p*(g - g_t) <= K t, the
    + side coincides with V1's + side up to K t, and sqrt(Gamma^#_w(b^-, omega^-)) <= sqrt(Gamma^#_w(B_-, Theta_-)) + K t + C_f p epsilon.
    With epsilon := c_f (u/Design)^C small enough, kappa_w <= 1 + eta_0/2 (as in V1 4.3).
Proof.  (a) As V1 TR Step 1-2: (X1) at E_c-coordinates of f: the budget lem:switchbudget at f gives sum phi_z(Delta B) <= t/q_0; Delta B =
-sum_l Delta theta_l u_l; the coarse part is L(Delta'_dec, gamma_dec) up to (i) the peak errors e_k vs_k lambda_k (eq:peakshift; e_k <=
t/(lambda_k mu_k) <= C_f D t/u at peaks with rho >= 1+u; tiny-margin peaks of f are (K4) carriers, strict non-peaks of f^#, hence in Omega),
(ii) class-R carriers (sum |Delta theta| <= K_g t, V1 (3.1), no shift bound needed), (iii) fine carriers (<= 3 b^2/t), (iv) the
difference between z and z^# on E_c (closed tiny rooms: V1 TR Step 4 bound), (v) the change of the coefficients from f to f^# (values and
kappa move by <= C Design b + realization moves <= T_lo^4, times ||gamma|| <= 12 sum lambda/t, giving <= T_lo^3).  (X3): eq:didentity at f
with the peaks' traces (proof of Lemma 1.3 applied to the decomposition, V2-ref 9(g)); its error is <= K t.  (X4): Lemma lem:suplevel(f).
(b) Lemma H (V2, refereed): the l_1 Hoffman constant of a system whose nonzero minors are >= mu and entries <= 1 is <= C (dim)^C mu^{-1}...;
exactly as in V2 Corollary B.1.  (c) Gamma^# = cone(r_1, ..., r_p) (Minkowski-Weyl, pointed after splitting free variables), so its
Delta'-projection is cone(g_1, ..., g_p); a basic representation uses linearly independent g_J, a_J = (g_J)^+ Delta'(t), and the entries of
(g_J)^+ are ratios of minors of the design/value matrix (Cramer), bounded by (Design/u)^C after exactification.  incr(t) is a nonnegative
combination of extreme rays, hence in Gamma^#(kappa, a); its Delta'-projection is sum (a^max - a(t)) g_j.  (d) Count.  (e) Lemma 1.1(c)
with V := V(Domega(t)) 1_{F^#c}: on E_c it equals L(Delta'^*, gamma(t)) (exact by (X1) for Gamma^#) plus the fine residue, which the
absorbers cancel EXACTLY (part 3); on the fine coordinates it is admissible by the fine structure built for the ray Delta'^* and the
activity class a (part 4); the active far parts of Omega-carriers are dominated by gamma_l (part 4, Lemma 4.2).  The + side is V1's
(projected) + side, so p*(g - g_t) <= K t as in V1 TR Step 5 (the new terms: projection K t, inactive components zeroed J A K t, fine
part ||V_fine||_1 <= C_f b^2 and absorber coefficients <= C_f b^2).  The - side differs from V1's by V(incr(t))|_{E_c} (on the base) and
Domega(incr(t)) (on the blocks); sqrt(Gamma) is a seminorm, and Gamma^#_w(V(r_j), Domega(r_j)) <= C_f for the normalized rays (q_0 h(y) <=
||U||^2 ||y||_1^2/nu, sigma H(x) <= (sum lambda |x|)^2/C).  The size conditions (V1 TR(iii)): incr(t) satisfies the homogeneous inward rows
(X4), so kind [3] is preserved; |Domega(incr)| <= C_f p epsilon / min lambda_Omega <= A_2/t for t <= T_hi(w).  QED

Remark (what 2.2 achieves).  Within one class S, every scale carries exact data with the SAME shift Delta'^*: the fine structure has to
handle ONE ray (gap C*-4 of V2-ref closed), and the averaged data have shift exactly Delta'^*.  Only the - side pays, by O(epsilon) in sqrt
Gamma; the + side, which defines the represented functional g_t, is untouched.  The increments are admissible on the - side precisely
because V(incr) is z^#-admissible: b^- - V(incr) stays (-z^#)-signed (Lemma 1.1(b)).

## 2.5 Theorem 2.3 (exactification of Gamma^# with the single scalar kappa).  PROVED (V2 Lemma L + Lemma TU + Lemma 1.5).
Enlarge the rate scheme of D^{V2} by the objects "minor of Gamma^#(kappa, a)" for all patterns and activity classes of level l (each a
polynomial with design coefficients in the variables (u_l(zhat))_{l in Omega} and (kappa_m)_m, evaluated at f), and let b(w) be a design
power of T_lo(w) absorbing the Lojasiewicz exponents of these finitely many polynomial systems (V2 Def. 2.2).  At a clean w, after V1's
moves (C1)-(C3) (which move values and kappa by <= Design b), there is a point (u'_Omega, kappa') within C_L(Design b)^{1/N_L} <= T_lo^4 of
the current one at which every tiny minor vanishes; it is REALIZED exactly by (i) Lemma TU (V1, refereed: pulls and private banks on the
far parts of the signature sets of the carriers of Omega, two-sided, exact) for the values, then (ii) in every block one push of
Lemma 1.5 (buffer peak or robust dropped strict non-peak; none of them in Omega), whose amount solves kappa_m = kappa'_m by the
intermediate value theorem (kappa_m is continuous and strictly monotone in the push with derivative >= min(1/2, u)).  Robust minors move
by <= Lip x T_lo^4 << u.  Consequently every minor of Gamma^#(kappa, a) at f^# is 0 or >= u/(2 Design^C), and Lemma H gives the Hoffman
constants used in 2.4(b), (c).
Proof.  Lemma L (V2, refereed) applied to the finite family of tiny minors (polynomials in (u_Omega, kappa) with design coefficients).
The pushes of (ii) change the values u_Omega only at second order through the Hilbert part (diagonal base, V1 Lemma B(i)); re-solve (i)
and (ii) jointly: the Jacobian of (u_Omega, kappa) with respect to (Lemma TU parameters, push amounts) is block triangular with identity
and diagonal (dkappa/ds >= min(1/2, u)) blocks, so V1's explicit fixed point (Lemma TU, Step 2) extended by one scalar equation per block
converges (contraction constant <= C Design eta, eta <= T_lo^4).  Status stability, costs: V1 Lemmas ST, CO with eta <= T_lo^4 << Lam.  QED
This closes (C*-3): only ONE block scalar enters (Lemma 1.3), and Lemma 1.5 always provides a push not belonging to Omega.

## 2.6 Lemma 2.4 (windowed averaging on a subset of scales).  PROVED.
Theorem E (Z3), E'' (V1) and E_RT (V3) remain valid if the averaging set {T_j 2^{1-i} : 1 <= i <= n_j} is replaced by any subset S_j of it with
|S_j| =: n'_j, provided n'_j >= 48 rho^2 K_j/(c_flat,j (1 - rho^2)) and K_j T_j / n'_j -> 0.
Proof.  In the proof of Theorem E (Z3 2.2 / V3 2.5) the set of scales enters at three places: (A) for rho|r| <= c_flat t; the set I_r :=
{t in S_j : c_flat t < rho|r|} satisfies sum_{I_r} t <= sum of ALL dyadic t < rho|r|/c_flat <= 2 rho |r|/c_flat; if I_r is empty every term
obeys (A); otherwise rho|r| > c_flat min S_j >= c_flat T_j 2^{-n_j}, which is all that the scale-decoupling condition uses; the averaged
error is (1/n'_j) sum_{I_r} rho|r| K t <= 2 rho^2 K r^2/(c_flat n'_j); and for |r| >= r_0, (1/n'_j) sum_{S_j} rho |r| K t <= 2 rho|r| K T_j/n'_j.
Averaging of the data over S_j preserves exactness, the side conditions and the common shift.  QED
With D_cls(w) <= (Design/u)^{C'} classes, some class contains n'(w) >= n(w)/D_cls(w) scales, and n(w)/D_cls(w) >= l 2^{l^3} Q(w)/D_cls(w)
-> infinity faster than any K of the above form once Q(w) dominates D_cls(w) x (Design/u)^C (design requirement of part 3).

# U1 part 3 — The design D^{U1} (zero-value absorbers) and exact absorption on the coarse coordinates (gap C*-1)

Base design: U4's T_final (r8/U4_notes.md Section 1: D^mu base mu_s = 2^{-s^2-1}, SLD with S_l = {2^l(2i+1)}, allowedness (a), (c),
weights (W1)-(W7), sub-windows at every stage, rate objects (R1)-(R7) + V2's determinantal and shift objects).  D^{U1} changes the TARGET
schedule (step (1) of T_final), makes the ladder bijection adaptive, adds rule (c''), and modifies the weights at two kinds of stages.
Everything else of T_final is kept.  Labels PROVED / SKETCH / OPEN.  (This version supersedes an earlier draft with absorbers in every
block, whose request queue grew faster than the number of stages.)

## 3.1 Definition of D^{U1}
(A0) ABSORBER TARGETS.  For a coordinate s, a sign beta in {+1,-1} and a stage p, an absorber target is y := x/q^*(x) with
       x := beta e_s^* + e_{p_0}^* + 4 sum_{r=1}^{R} 2^{-r} e_{p_r}^*,
     p_0 < p_1 < ... < p_R FRESH odd integers (in no S_l and in no earlier target), and R = R(p) := the least integer with
     2^{3-R} <= mu_{p_0}^2 c_p^2/4.  Then |y(s)| = 1/q^*(x) in [1/8, 1].  An absorber target is allowed at p (T_final's (a): s is in Z_0 or in
     some S_{l'} with l' < p; (c): s <= p).  p_0 is the CONTINUOUS TUNING coordinate, p_1..p_R the BINARY coordinates.
(A1) MAIN STAGES and CLUSTERS.  After every main stage L, the next stages form a CLUSTER: for every coordinate s in
     E^ch(L) := T(L) ∪ union_{l'' <= L} (S_{l''} ∩ [1, L]) one BIASED PAIR of block 1 (two carriers with absorber targets for (s, +1) and
     (s, -1)), consecutive, in any order; R_cl(L) := 2|E^ch(L)|.  The ladder bijection is chosen adaptively (j(k,1) for the cluster).
(A2) DEEP PAIRS.  For every even s in some S_{l'} one biased pair of block 1 for (s, +-1) is placed at stages in [s, psi^{-1}(s)), where
     psi(p) := floor(p^{1/2}/4); and (c'') a MAIN target placed at stage p may meet S_{l'} only in [1, psi(p)] (this strengthens (c)).
(A3) SCHEDULE.  At a stage of block m: if a cluster is open, serve it (block 1); else serve the oldest pending deep request of block m (if
     m = 1 and one is due); else place T_final's main target if allowed, else an FD target (fresh odd coordinate; always allowed).
(A4) WEIGHTS.  Cluster stages: c_{L+i} := c_{L+1} 4^{1-i} (1 <= i <= R_cl), where c_{L+1} is the minimum of T_final's (W1)-(W7) at stage L+1
     taken over all coordinates s of E^ch(L) in (W4).  All other stages: T_final's rule with (W4) strengthened to
       (W4'')  c_l <= tau_{l'} 2^{-2s} c_{l'} delta_{l'} T_lo(l-1, M(l-1))^3/2   for l' < l and s in supp y_l ∩ S_{l'}.
     Design(L) at a main stage L additionally contains 4^{R_cl(L)}, 2^{k(L+R_cl)} (block-1 index), 1/eta_L and the counts D_cls(w) of
     part 2; Q(w) is enlarged so that Q(w) >= D_cls(w)^2 (Design(L)/u(w))^{C} for the constant C of part 2 (design requirement; the
     square is used by the pigeonhole of Master Theorem IV, part 5.6).
WINDOWS ARE USED ONLY AT MAIN STAGES.

## 3.2 Theorem 3.1 (admissibility, N-freeness, survival).  PROVED.
(a) T(D^{U1}) satisfies (T-a)-(T-d) of def:admissible (so the conclusion of Martin's Lemma B), (P1), and at every main stage L:
    sum_{l' > L} lambda_{l'} <= b(L, M(L))^2/2 <= T_lo(w)^8 (w of level L).
(b) D^{U1} does not depend on N (block 1 is present in every p_N).
(c) Every refereed result used in parts 1, 2, 4 (U4's dependency trees of Master Theorems II, III', V1 Lemmas B, DR, TU, CO, ST, NS, RR,
    Proposition TR, Theorem E'', V2 Lemmas H, L, QB, 2.3, Theorems B, C1, Lemma C5, Z3 Lemma 3.1, Theorem E, Lemma U, the note's lemmas)
    holds for D^{U1} with "level" read as "main stage".
Proof.  (a) (T-a): q^*(Te) = c <= 1.  (T-b), (T-c): T_final's argument (U4 Theorem 2.2) at the least stage L(s) of a target meeting
s in S_{l'} uses only allowedness (a) and (W4); absorber targets satisfy (a), cluster weights satisfy (W4) by the choice of c_{L+1}, other
stages satisfy (W4'') ⊂ (W4).  (T-d): every request is finite and the schedule (A3) serves requests in order; deep requests created up to
stage S number <= 2 psi(S) + 2 + (S^{1/2}) (coordinates s with psi^{-1}(s) <= S), so main stages are not starved: in every block,
infinitely many stages place main or FD targets; a target y^(i) touching finitely many signature coordinates is allowed at all large
stages (c'') once their deep pairs exist; hence y_l = y^(i) at infinitely many stages of each block, and density follows as in T_final.
(P1) as T_final.  (P2) at a main stage L: sum_{l'>L} c_{l'} <= c_{L+1} sum_i 4^{1-i} + (4/3) c_{L+R_cl+1} <= 2 c_{L+1} <= 2 b(L, M(L))^2 ((W2)).
(b) Requests concern block 1 and coordinates; for p_N absent carriers are omitted (as T_final).
(c) U4's Lemma GW: window arguments use one window's dyadic scales, design factors of the level, the box bound (which needs (a)), and
T_hi(next) <= T_lo(previous); all hold at main stages.  Non-window arguments use (T-a)-(T-d), (P1), (P2), allowedness (a), (b) as a
property of (y_l, c_l), (c) (implied by (c'')), bounded gaps, the mu-base, the design factors.  Absorbers are ordinary SLD carriers.  QED

## 3.3 Lemma 3.2 (first touchers).  PROVED.
Let w be a sub-window of a main stage L, s_far(w) the least s with 2^{-s} <= c_{L+1}^2 (so 2^{-s_far} <= b(w)^4), and
E_c(w) := T(L) ∪ union_{l'' <= L} (S_{l''} ∩ [1, s_far(w)]).  For every s in E_c(w), among the carriers at stages > L whose vectors meet s,
the first two form a biased absorber pair for s (a cluster pair of some main stage L' >= L with s in E^ch(L'), or the deep pair of s).
Proof.  If s in E^ch(L), the cluster of L follows L immediately.  If s in S_{l''} ∩ (L, s_far]: a target at a stage p meets s only if
s <= p ((c)) and, if it is a main target, s <= psi(p) ((c'')), i.e. p >= psi^{-1}(s), after the deep pair; FD targets meet only fresh odd
coordinates; signature vectors meet s only for l'' itself; absorber targets meet only their own s' and fresh coordinates.  So the first
carrier after L meeting s is an absorber for s (deep pair, or a cluster pair of a main stage L' with s <= L'), and pairs are
consecutive.  QED

## 3.4 Lemma 3.3 (zero-value tuning of an absorber; biased pair).  PROVED.
Let f^(1) be a companion with finite base support not containing the coordinates p_0, ..., p_R, nor S_a ∩ [1, s_far(a)] (s_far(a): least s'
with 2^{-s'} <= Phi_a^2), and with s notin F^(1).  Put z := +1 at p_0, sigma' := +1 on the near part S_a ∩ [1, s_far(a)], z := +1 on the far
part of S_a, and choose binary signs sigma_r (r >= 1) with
    0 <= Target - 4 sum_r 2^{-r} sigma_r <= 2^{3-R},   Target := -( beta zhat_s + 1 + q^*(x) delta_a h_a(zhat) )
(possible: the binary sums run through the odd multiples of 2^{2-R} in (-4, 4), and Target in [-3.5, 1.5] because zhat_s = z_s (s notin
supp a), |z_s| <= 1, and q^*(x) delta_a ||h_a||_1 <= ||x||_1 (1 + ||U||) delta_a H_a <= 7.5/5 = 1.5 by the choice of delta_a in def:SLD; round DOWN).  Put masses theta_a sigma_r at p_r (r >= 1), theta_a sigma' at the near part of S_a, and
m_0 at p_0 with m_0 in [theta_a, theta_a + c_p^2] (all become support coordinates), theta_a := C_f lambda_a T_hi (the window's T_hi; any
theta_a in (0, lambda_a] works for (i)).
(i) There is m_0 in [theta_a, theta_a + c_p^2] with u_a(zhat) = 0 EXACTLY; a is a strict non-peak with w(a) = 0 (gap M);
(ii) for finitely many absorbers tuned simultaneously, the masses m_0 can be chosen to make all values exactly 0 (contraction);
(iii) a carries no d-effect: u_a(zhat) gamma_a = 0 in (1.3), and nu_a = 0 contributes nothing to kappa (Lemma 1.3, Lemma 1.2);
(iv) cost p*(f^(2) - f^(1)) <= C (lambda_a + sum masses); the other carriers' values move by the second-order Hilbert effect
     <= C (sum masses x mu)^2 (diagonal base, Lemma B of V1), except carriers at stages > p whose targets meet the p_r or near S_a.
Proof.  (i) q^*(x) n_a u_a(zhat) = beta zhat_s + zhat_{p_0} + 4 sum 2^{-r} zhat_{p_r} + q^*(x) delta_a h_a(zhat), with zhat_{p} = z_p + mu_p^2 m_p
z_p/nu at support coordinates (diagonal base; U4 1.1) and zhat = z on S_a's far part and at s (not in the support).  With m_0 = theta_a the
bracket equals -(Target - binary sum) + O(mu^2 theta) in [-2^{3-R} - eps, eps]; raising m_0 by Theta raises zhat_{p_0} by mu_{p_0}^2 Theta/nu' (nu'
changes by a second-order amount), so Theta in [0, c_p^2] sweeps an interval of length >= mu_{p_0}^2 c_p^2/2 >= 2^{4-R} upward, which contains
the value cancelling the bracket; the intermediate value theorem gives u_a(zhat) = 0 exactly.  lem:threshold: zeta(a) = 0 < theta Phi^2, so
a is a strict non-peak with w(a) = 0.
(ii) Each absorber's value depends at first order only on its own m_0 (diagonal base: the other masses enter through nu, a second-order
effect of size <= C (sum masses mu)^2 << mu_{p_0}^2 c_p^2); the joint system is solved by the explicit fixed point of V1 Lemma TU, Step 2.
(iii) Lemma 1.3 and (E1), (E2): a strict non-peak with nu = 0 contributes 0.  (iv) Z3 Lemma 3.1 / U4.  QED
BIASED PAIR.  For a pair (a^+, a^-) and a residue r at s put gamma_{a^+} := c_0 + (-r)_+/|y_{a^+}(s)|, gamma_{a^-} := c_0 |y_{a^+}(s)|/|y_{a^-}(s)| +
r_+/|y_{a^-}(s)|, c_0 := lambda_{a^-} 2^{-s_far(a^-)}.  Then gamma_{a^+} y_{a^+}(s) + gamma_{a^-} y_{a^-}(s) = -r, both coefficients are >= c_0/4,
Lipschitz in r, and on the far parts of S_{a^+-} the absorber's own term gamma_a v_a(s') dominates every later carrier ((W4''): ratio
<= C_f 2^{s_far(a) - s'} T_lo^3 2^{1+k(a)} < 1/2), so z = +1 there is admissible whatever r is.

## 3.5 Proposition 3.4 (exact absorption on E_c).  PROVED (given parts 2 and 4).
Let w be a clean sub-window of a main stage L >= l_f and f^# the companion of part 4, at which the first pair P(s) of Lemma 3.2 is tuned
(Lemma 3.3) for every s in E_c(w) \ F^#.  Let rho(s) := V(Domega)(s) - L(Delta'', gamma)(s) - (contribution of P(s)), the RESIDUE at s
(L(Delta'', gamma): the coarse vector of part 2 with the true shift Delta'' of Lemma 4.6).  Then:
(a) rho(s) = the sum of (coefficient) u_k(s) over carriers k after P(s) (Lemma 3.2), so |rho(s)| <= C_f sum_{k after P(s)} lambda_k; on T(L)
    also the trace correction of Lemma 4.6(b) is absorbed: |(Delta'' - Delta') P(s)| <= C_f Design c_{L+1};
(b) the biased coefficients with r := rho(s) (+ trace correction) make V(Domega)(s) EXACTLY equal to L(Delta'', gamma)(s), which is
    z^#-admissible (part 2 (X1), Lemma 4.6(b));
(c) CAPACITY: |Domega(a)| = |gamma_a|/lambda_a <= A_2/t for t <= T_hi(w) (w(a) = 0), i.e. kind [2] of V1 TR(iii) (gap = M);
(d) data at the support coordinates p_r, near S_a satisfy t|b| <= m_r (no flips), and the masses cost <= C_f c_{L+1} T_hi + C c_{L+1}^2;
(e) the pairs carry no d-effect (Lemma 3.3(iii)).
Proof.  (a) Lemma 3.2 and Lemma 1.1(a); coefficients of later carriers are <= C_f lambda (Lemma 2.1: |Delta''| <= C_f) or gamma <= C_f lambda for
later absorbers.  (b) The biased pair.  (c) Cluster pairs: lambda_a >= 2^{-1-k(a)} 4^{1-R_cl} c_{L+1} >= c_{L+1}/Design(L), while
sum_{k after the cluster} lambda_k <= 2 c_{L+R_cl+1} <= 2 b(L+R_cl)^2 << c_{L+1}/Design and the trace correction is <= C_f Design c_{L+1}; so
|gamma_a|/lambda_a <= C_f Design^2 + 1 << A_2/T_hi(w) (Q(w) >= (Design/u)^C).  Deep pairs (stage p >= s): the residue comes only from
later carriers, sum lambda <= 2 c_{p+1} <= 2 b(p)^2 <= 2^{1-8 n(p)} << lambda_a = 2^{-1-k} c_p (n(p) >= Design(p) >= 2^{k+1}/c_p);
s is not in T(L) (s > L), so no trace correction.  (d) b(p_r) = (coefficient of u_a) u_a(p_r) = gamma_a 2^{1-r}/(q^*(x) n_a): t|b| <=
C_f lambda_a T_hi = theta_a <= m_r.  (e) Lemma 3.3(iii).  QED
Remark.  E_c(w) is finite; F^# stays finite; the absorbers are strict non-peaks with w = 0 (gap M): harmless for (SC) (part 4) and
for Lemma U (kind [2]).  Zero-value absorbers are what makes ONE pair per coordinate (in block 1) sufficient: a pair of a non-shifted
block would otherwise shift that block through (1.3).

# U1 part 4 — The companion: order of moves, the fine structure (gaps C*-2, C*-5), reference versus true coefficients

Setting: D^{U1} (part 3), N fixed, f with F finite, g in C(f), rho < 1; w a clean sub-window of a MAIN stage L >= l_f; an activity class a
(part 2.3) fixed, with active blocks A ⊂ I_sh(w), signs sigma_m := sgn(Delta'_m) (m in A), active coarse Omega-carriers Omega_act (sign
eps_l, class G), inactive ones (gamma = 0).  The class is ONE-SIGNED if all sigma_m (m in A) are equal: CONFIGURATION (i) if sigma = -1
(data shift Delta < 0: the blocks lack an upper source, I_up), CONFIGURATION (ii) if sigma = +1 (I_lo).  K = C_f (Design/u)^C as before.

## 4.1 The companion f^# (order of the moves)
(1a) V1's moves (C1) close class-G rooms on S^nat, (C2) close tiny target rooms, (C3) donor raise; then the realization of a Lojasiewicz
     point (u', kappa') of Gamma^#(kappa, a) (Theorem 2.3): Lemma TU (pulls and private banks on far parts of the signature sets of the
     carriers of Omega) for the values, and one push per block (Lemma 1.5: a bank at the first far coordinate of the buffer peak, or a
     move on a robust dropped strict non-peak) for kappa, solved by the intermediate value theorem up to the jumps caused by status
     changes of carriers at stages > L + R_cl (size <= C c_{L+R_cl+1}).
(1b) Absorbers: for every s in E_c(w) \ F^(1a), tune the first pair P(s) of Lemma 3.2 (block 1) to VALUE ZERO (Lemma 3.3): p_0, ..., p_R
     and the near part of S_a become support coordinates (masses >= theta_a = C_f lambda_a T_hi(w)), far part of S_a := +1.  Also tune all
     absorbers of the cluster of L to value zero (so that no cluster carrier changes status later).
(1c) Re-push kappa (one push per active block, Lemma 1.5) so that |kappa^# - kappa'| <= C c_{L+R_cl+1} (jumps of the intermediate value
     argument), then re-tune all tuned absorbers to value zero and, in configuration (ii), re-realize the values of Omega_act exactly
     (joint explicit fixed point of V1 Lemma TU: each target carrier is controlled at first order by its own masses, cross effects are
     second order in the corrections; geometric convergence).  The re-tuning moves kappa by a second-order amount << c_{L+R_cl+1}.
(2)  The FINE STRUCTURE on J_fine := N \ (F^(1b) ∪ E_c(w) ∪ (all coordinates fixed in (1a), (1b))): configuration (i): the robust
     recursion of 4.2; configuration (ii): the Schauder fixed point of 4.5.
Every move of (1a)-(1c) acts on coordinates distinct from those of the other moves (V1 3.2; absorbers' coordinates are private or in
their own signature sets).  J_fine is fixed after (1c); step (2) does not change the base part a^#, hence not e^#.

## 4.2 Lemma 4.1 (ownership; the robust recursion, configuration (i)).  PROVED.
A carrier k is an OWNER-CANDIDATE if its coefficient in V (Lemma 1.1(a)) is nonzero with a sign known in advance: (a) l in Omega_act (sign
eps_l); (b) coarse peaks of active blocks (coefficient -Delta''_m vs lambda: sign -sigma_m vs); (c) ALL TUNED absorbers: the used pairs
P(s) (biased coefficients >= c_0/4 > 0) and every other tuned absorber a, which gets the constant switching coefficient gamma_a := c_0(a) =
lambda_a 2^{-s_far(a)} > 0 [CORRECTION made in the final check: with gamma_a := 0 the far part of S_a, fixed at z = +1 in (1b), would carry
only later contributions of uncontrolled sign; with gamma_a = c_0(a) > 0 the absorber's own term dominates there by the biased-pair estimate
of 3.4, so z = +1 is admissible; its contribution at its own target coordinate s' lies on a support coordinate (s' in F^(1a)) or is part
of the residue absorbed by the first pair P(s') (Prop 3.4(a)); value zero keeps it free of d-effects (Lemma 3.3(iii))]; (d) fine carriers k (stages > L) of
active blocks other than tuned absorbers (coefficient -Delta''_m lambda_k w(k); sign -sigma_m varsigma_k, varsigma_k := sgn w(k), to be chosen).  For j in J_fine let own(j) := the least owner-candidate (in stage order) whose vector meets j.
Every j in J_fine either has an owner or meets no carrier with a nonzero coefficient; in the latter case V(Domega)(j) = 0 and z_j may
be chosen freely in [-1, 1] (admissible).  (By V2 Cor. C3.1(b) every coordinate meets carriers of every block at infinitely many stages,
so in fact owners exist whenever some block is active; the argument does not need this.)  Define recursively, along the stages k > L of class (d):
    O(k) := {j in J_fine : own(j) = k} (contains S_k ∩ J_fine = S_k: no earlier carrier meets S_k, allowedness (a));
    Y_k := u_k(zhat) computed with the coordinates of supp u_k \ O(k) (all fixed earlier, or owned by earlier candidates);
    varsigma_k := sgn Y_k (:= +1 if Y_k = 0);   z_j := sgn(-sigma_m varsigma_k u_k(j)) for j in O(k),
and for owners of types (a)-(c) put z_j := sgn(coefficient x u_own(j)(j)) on their owned sets (fixed already in (1a)-(1b) for (a), (c)).
In configuration (i) (sigma = -1) this gives z_j = varsigma_k sgn u_k(j) on O(k) (SELF-ALIGNED) and
    |u_k(zhat^#)| = |Y_k| + sum_{j in O(k)} |u_k(j)| >= ||v_k||_1 = delta_k H_k/n_k,                                        (4.1)
so k is a peak of f^# with sign varsigma_k and margin mu_k >= q^#_0 (delta_k H_k/n_k - theta^#_m Phi_k/m) >= q^#_0 delta_k H_k/(2 n_k).
Proof.  The recursion is well founded: Y_k uses only coordinates whose z is fixed before k is processed.  zhat^#_j = z_j on J_fine (j notin
F^#, diagonal base: (Ue)_j = mu_j^2 a^#_j/nu = 0).  With sigma = -1, z_j u_k(j) = varsigma_k |u_k(j)| on O(k), so u_k(zhat^#) = Y_k + varsigma_k
sum_{O(k)} |u_k(j)| has sign varsigma_k and modulus (4.1).  Peak criterion lem:threshold (V1 1.3): rho_k = |u_k| m/(Phi_k theta) >= 1; by (W3)
Phi_k <= c_k <= (delta_k H_k)^2, so theta Phi_k/m <= theta (delta_k H_k)^2 << delta_k H_k/n_k for stages > L >= l_f (theta^# <= C_f).  QED

## 4.3 Lemma 4.2 (dominance: the owner fixes the sign of V).  PROVED.
In the situation of 4.2 (configuration (i)), or for the fixed owners (a)-(c) in configuration (ii), for every j in J_fine owned by k:
    |coefficient_k| |u_k(j)| >= 2 sum_{k' later than k, u_{k'}(j) != 0} |coefficient_{k'}| |u_{k'}(j)|,
hence sgn V(Domega)(j) = sgn(coefficient_k u_k(j)) and z_j V(j) > 0: V is z^#-admissible at every coordinate of J_fine (all of them are
contacts of f^#).  The bound holds for every Delta'' in the class (active |Delta''_m| >= A_2 K T_lo(w)/2, |Delta''| <= C_f) and every
gamma(t) of the class (active |gamma_l| >= A_2 K T_lo(w)/2).
Proof.  Coefficients of carriers k' later than k are <= C_f lambda_{k'} (Lemma 2.1; absorbers' gamma <= C_f lambda_a, part 3.5(c)).
(i) j in S_k (signature coordinate of the owner): carriers k' > k meet j only through targets, allowed only if c_{k'} <= tau_k 2^{-2j} c_k
delta_k T_lo(k-1)^2/2 ((W4')); their total weight is <= (4/3) of the largest, so the right side is <= C_f tau_k 2^{-2j} c_k delta_k T_lo(k-1)^2,
while the left side is >= |coefficient_k| delta_k 2^{-j}/n_k with |coefficient_k| >= (A_2 K T_lo(w)/2) lambda_k M^#/... for type (d), >= A_2 K
T_lo(w)/2 for (a), >= c_0/4 for (c), >= (A_2 K T_lo(w)/2) lambda_k for (b).  Since T_lo(k-1) <= T_lo(w) (k - 1 >= L) and lambda_k = m 2^{-m-k(k)}
c_k with 2^{m + k(k) - j} <= 2^{m - k} (j >= 3 * 2^k), the ratio is <= C_f T_lo(w) 2^{m}/(A_2 K) < 1/2 for types (a), (b), (d); for (c):
j > s_far(a) and c_0 = lambda_a 2^{-s_far(a)} give ratio <= C_f 2^{m + k - (j - s_far(a))} T_lo^2 < 1/2.  For (a), (b) the owned signature
coordinates are the far ones (j > s_far(w)), where 2^{-j} <= b(w)^2 makes the ratio even smaller.
(ii) j a target coordinate of k (j in supp y_k, Z_0 or a coarser signature set): the left side is >= |coefficient_k| eta_k/n_k
(eta_k := least nonzero |y_k(j)|), the right side <= C_f sum_{k'>k} lambda_{k'} <= C_f c_{k+1} <= C_f b(k, M(k))^2 <= C_f 2^{-8 n(k)}, and
n(k) >= Design(k) >= 1/(eta_k lambda_k) (Design contains 1/eta and 1/Phi): ratio <= C_f 2^{-8 n(k)} T_lo(w)^{-1} << 1 (T_lo(w) >= T_lo(k)).
Owners of type (a), (b) have no target coordinates in J_fine (their targets lie in T(L) ⊂ E_c).  QED

## 4.4 Lemma 4.3 ((SC) at f^# for the negative blocks).  PROVED.
In configuration (i), the set I_- := A (all active blocks, Delta''_m < 0) satisfies the scrambling condition (SC) of def:SC at f^#, with
ANY sequence s_i -> 0.
Proof.  Fix m in A and Upsilon >= 1.  Carriers of block m at f^#: (1) coarse (stages <= L): finitely many; peaks have relative margin >=
u/2 (V2 (A2), V1 Lemma ST(c)), strict non-peaks have gap^# >= c_f Lam M^# or robust gaps (V1 Lemma ST(c)), no degenerate peaks; so for s
below a positive bound s_0(f^#) none of them contributes to Scr_m(Upsilon s).  (2) tuned absorbers: finitely many strict non-peaks with
gap >= 3M/4 (Lemma 3.3): no contribution for s < s_0.  (3) all other carriers of block m at stages > L: peaks with margin mu_k >=
q^#_0 delta_k H_k/(2 n_k) (Lemma 4.1).  A carrier of (3) contributes only if mu_k <= Upsilon s, i.e. delta_k H_k <= 2 n_k Upsilon s/q^#_0 =: X(s),
and then contributes min(Phi_k, Upsilon s) <= Phi_k <= c_k <= (delta_k H_k)^2 ((W3)).  The numbers a_k := delta_k H_k decrease super-
exponentially in k (delta_k <= 2^{-k}, H_k <= 2^{1 - 3 * 2^k}), so sum_{k : a_k <= X} a_k^2 <= 2 X a_{k(X)} <= 2 X^2, where k(X) is the least such
k.  Hence Scr_m(Upsilon s) <= C (Upsilon s/q_0)^2 = o(s) for s < s_0.  The sequence may be common to all m in A.  QED
Consequently thm:engineered applies at f^# to data with Delta_m < 0 exactly on A (I finite, F^# finite).

## 4.5 Lemma 4.4 (configuration (ii): exact completion by a fixed point, with the class fixed).  PROVED.
Let the class be of configuration (ii) and let all scales of the class carry the COMMON reference shift Delta'^* (part 2.4(c)).  Put
J_free := J_fine minus the owned sets of the fixed owners (a)-(c) (their signs are fixed by Lemma 4.2).  For z' in [-1,1]^{J_free}
let f(z') be the row with these coordinates replaced, and define the TRUE common shift Delta''(z') by (X3) at f(z') with the class's
gamma(t) (Lemma 4.6: Delta'' does not depend on t after (1c)) and the absorbers' coefficients gamma_abs(z') (part 3.5, continuous in the
residues, which are continuous in z').  Then the map
    Psi(z')_j := clamp_{[-1,1]}( z'_j + V(z')(j) ),   j in J_free,
V(z') := the fine part of V(Domega) at f(z') with shift Delta''(z') (coefficients -Delta''_m lambda_k w_m(z')(k) of the fine carriers of
active blocks), has a fixed point z'^*, and at f^# := f(z'^*) the vector V(Domega) is z^#-admissible on J_fine.
Proof.  As V2 Lemma C5 (refereed): [-1,1]^{J_free} with the product topology is compact convex metrizable; zhat(z') depends coordinatewise
continuously on z'; R_m^** zhat(z') is l_1-continuous by dominated convergence; the duality maps J_m are norm-to-weak* continuous (Lemma
A(d)), so w_m(z')(k) is continuous; V(z')(j) is a dominated series; Delta''(z') is continuous (kappa^#(z') is a continuous function of the
block data, which are continuous; the absorbers' coefficients are Lipschitz in the residues, Lemma 3.3).  Schauder-Tychonoff gives
z'^*; clamp(z_j + V_j) = z_j means V_j = 0 if |z_j| < 1 and z_j V_j >= 0 if |z_j| = 1.  On the owned sets of (a)-(c), Lemma 4.2.  QED
No (SC) is needed in configuration (ii): Delta_m >= 0 for all m, and cor:D1 applies at f^#.

## 4.6 Lemma 4.5 (cost and statuses of f^#).  PROVED.
p*(f^# - f) <= C_f Design T_lo^3 log(1/T_lo) + C_f T_lo^4 log(1/T_lo) + C_f c_{L+1} log(1/c_{L+1}) =: theta_w T_lo(w)^2 with theta_w -> 0;
the block data move by the same order; every coarse carrier keeps its status class (V1 Lemma ST), every robust minor of Gamma^# stays
>= u/(2 Design^C) (Theorem 2.3), and the statuses of the coarse carriers in Omega and of the coarse peaks are those used in Gamma^#.
Proof.  (1a): V1 Lemma CO (refereed) and Theorem 2.3 (moves <= T_lo^4).  (1b), (1c): the absorbers' values move by O(1), cost <= C sum
lambda_a <= C c_{L+1}; masses <= C_f c_{L+1} T_hi.  (2): Z3 Lemma 3.1 with delta = zhat^# - zhat^(1b) supported in J_fine: coarse carriers
meet J_fine only in the far parts of their signature sets (2^{-s} <= 2^{-s_far(w)}), so |u_{l''}(delta)| <= 4 delta_{l''} 2^{-s_far(w)}; carriers at
stages > L contribute <= sum lambda <= c_{L+1}.  c_{L+1} <= b(L, M(L))^2 <= T_lo(w)^8.  Statuses: V1 Lemma ST with the extra drift
C c_{L+1} << Lam.  QED

## 4.7 Lemma 4.6 (reference versus true coefficients; the true shift).  PROVED.
Let (Delta'(t), gamma(t)) in Gamma^#(u', kappa', a) be the reference coarse data of a scale t (projected, and normalized in configuration
(ii)).  The data at f^# with switching gamma(t) on Omega_act (0 on inactive members of Omega, c_0(a) on the other tuned absorbers, the biased
coefficients on the used pairs) have TRUE shift Delta''(t) given by (X3) at f^#:
    Delta''_m(t) kappa^#_m = sum_{l in Omega_act, m(l) = m} u_l(zhat^#) gamma_l(t)        (absorbers contribute 0: value zero, Lemma 3.3(iii)).
Then
(a) |Delta''_m(t) - Delta'_m(t)| <= C_f ( |kappa^#_m - kappa'_m| + ||u^# - u'||_{Omega_act} ||gamma(t)||_1 ) <= C_f Design c_{L+R_cl+1} + C_f c_{L+1}^2/t;
    in configuration (ii) the middle term vanishes (step (1c)), so Delta''(t) = Delta'^* kappa'/kappa^# =: Delta''^* is the SAME for all t of
    the class;
(b) L(Delta''(t), gamma(t)) differs from the admissible L(Delta'(t), gamma(t)) by sum_m (Delta''_m - Delta'_m) P_m, P_m := the coarse peak traces
    of block m restricted to E_c; on the near signature sets of the coarse peaks the total coarse value is the peak's own trace
    -Delta''_m vs lambda v_l(s), of the same sign as -Delta'_m vs (|Delta'' - Delta'| < |Delta'|/2), hence admissible; on T(L) the difference is
    absorbed by the cluster pairs (Proposition 3.4, cluster capacity >= c_{L+1}/(Design T_hi(w)) against a correction <= C_f Design c_{L+1});
(c) the signs and activity of Delta''(t) are those of Delta'(t) (active |Delta'_m| >= A_{i+1} K t/2 >> the bound in (a), since c_{L+1} <= T_lo^8).
Proof.  (a) Subtract (X3) at (u', kappa') from (X3) at (u^#, kappa^#) and divide by kappa^# >= A^# >= c_f.  |kappa^# - kappa'|: after (1c),
<= C c_{L+R_cl+1} (jumps: only carriers at stages > L + R_cl can change status under the push, since the cluster carriers are tuned to value
zero with gap M and the coarse carriers have robust margins/gaps); step (2) changes the block data by <= C (sum_{stages > L+R_cl} lambda +
2^{-s_far(w)}) <= C c_{L+R_cl+1} (Lemma 4.5; coarse carriers meet J_fine only beyond s_far, 2^{-s_far} <= c_{L+1}^2... and cluster carriers do
not meet J_fine except in their far signature parts, fixed at +1 or owned with gamma = 0); kappa is Lipschitz in the block data with
constant <= Design/u (Lemma 1.2: (A, theta) solve (E1), (E2), a nonsingular system at f^# with Jacobian bounded below by Phi_P^2 >= D(L)^{-2}).
||u^# - u'||_{Omega_act}: exact after (1a); (1b), (1c) second-order Hilbert effects <= C (sum masses x mu)^2 <= C c_{L+1}^2; step (2) does not
change u_l (l in Omega_act): their vectors meet J_fine only in their own far signature parts, owned by l with the sign eps_l fixed since
(C1).  In configuration (ii), (1c) re-realizes u^# = u' exactly; kappa^# is common to all scales.
(b) L is linear in Delta'; coarse peaks are the only coarse carriers whose coefficient depends on the shift; on S^nat of a peak only the
peak lives among coarse carriers ((P1), allowedness (a)).  (c) The gaps of the thresholds (2.3).  QED

# U1 part 5 — Mixed activity classes, MASTER THEOREM IV, the remaining step

Setting of part 4: D^{U1}, N fixed, F finite, w a clean sub-window of a main stage L >= l_f, an activity class a with active set A and
signs sigma_m = sgn Delta'_m (m in A).  A is ONE-SIGNED if all sigma_m agree (or A is empty), MIXED if A_- := {sigma = -1} and
A_+ := {sigma = +1} are both nonempty (possible only for N >= 2).  thm:engineered needs (SC) exactly for I_- := {m : Delta d_m < 0}, i.e. for
A_- (Delta d_m and Delta'_m have the same sign up to the positive factors M, kappa); blocks of A_+ need nothing (cor:D1 / Theorem E^>=).

## 5.1 Lemma 5.1 (exactness in every class, mixed ones included).  PROVED.
For every class a (one-signed or mixed) the companion f^# of part 4 can be completed EXACTLY: there is z^* in [-1,1]^{J_free} such that at
f^# := f(z^*) the vector V(Domega(t)) is z^#-admissible off F^# for every scale t of the (class, cube) set S, with the common true shift
Delta''^* (the same for all t in S).
Proof.  Proposition 2.2(c) (normalization) works inside the cone Gamma^#(kappa, a) and never uses signs.  In step (1c) re-realize the values
of Omega_act exactly (as done in configuration (ii)); then Lemma 4.6(a) gives Delta''(t) = Delta'^* kappa'/kappa^#, common to all t in S,
and kappa^#(z') is continuous in z'.  The proof of Lemma 4.4 (Schauder-Tychonoff for Psi(z')_j = clamp(z'_j + V(z')(j)), V2 Lemma C5) uses
only continuity of z' -> V(z') and the common ray, not the signs of the shifts.  The fixed owners (a)-(c) are handled by Lemma 4.2,
whose estimates do not use the signs either; E_c by part 3.  QED
So in a mixed class the ONLY missing property is (SC) for A_- at f^#.  (C*-1), (C*-3), (C*-4), (C*-5) are closed for every class.

## 5.2 Lemma 5.2 (states of a negative fine carrier at an exact completion).  PROVED.
Let z be any point at which V is admissible on J_fine, l a fine carrier (stage > L + R_cl, not a tuned absorber) of a block m in A_-,
v_l := u_l(zhat), thr_l := vartheta_m Phi_m(l) (the peak threshold of lem:threshold), O(l) := the coordinates of supp u_l ∩ J_fine at which
no earlier carrier has a nonzero coefficient (O(l) ⊇ S_l: allowedness (a)), own_l := sum_{j in O(l)} |u_l(j)| (>= delta°_l), and
Y_l := v_l - sum_{j in O(l)} u_l(j) zhat_j (the part of the value fixed by earlier carriers and coarse coordinates).  Then exactly one of:
 (Z') |w_m(l)| < M/2, i.e. |v_l| < thr_l/2: a strict non-peak with gap > M/2;
 (R)  |w_m(l)| >= M/2 and sgn w_m(l) = sgn Y_l (or Y_l = 0): v_l = sgn(w)(|Y_l| + own_l), a peak with margin >= own_l - thr_l >= own_l/2;
 (W)  |w_m(l)| >= M/2 and sgn w_m(l) = -sgn Y_l, which forces |Y_l| < own_l and |v_l| = own_l - |Y_l|.
Proof.  If |w(l)| >= M/2, the coefficient |Delta''_m| lambda_l w(l) of l dominates every later term at every j in O(l) (the estimates of
Lemma 4.2 hold with |coefficient| >= |Delta''| lambda M/2), so V_j != 0 and admissibility forces z_j = sgn(w(l)) sgn(u_l(j)) on O(l)
(j notin F^#, so zhat_j = z_j): v_l = Y_l + sgn(w(l)) own_l, and sgn v_l = sgn w(l) (clamp formula).  Both sign cases are listed;
in the second, sgn(Y_l + sgn(w) own_l) = sgn w with sgn Y_l = -sgn w needs own_l > |Y_l|.  For |w| < M/2 the clamp formula
|w(l)| = M |v_l|/thr_l gives the bound and gap = M - |w| > M/2.  own_l >= delta°_l >= 2 thr_l by (W3).  QED

## 5.3 Lemma 5.3 (an (SC) criterion that tolerates wrong branches).  PROVED.
Call a negative fine carrier BAD if its value lies in the THRESHOLD BAND
      B_l := ( thr_l (1 - Phi_l^{1/2}/M),  thr_l + Phi_l^{1/2} ).
If at f^# no negative fine carrier is bad (and the coarse carriers and tuned absorbers are as in Lemma 4.3), then A_- satisfies (SC) at
f^#; the sequence can be taken common to all m in A_- and is explicit.
Proof.  Fix Upsilon >= 1.  Coarse carriers and tuned absorbers: finitely many, none contributes for s < s_0 (Lemma 4.3 (1), (2)).  A
fine negative carrier contributes to Scr_m(Upsilon s) only if (peak) mu_l = |v_l| - thr_l <= Upsilon s, or (strict non-peak) gap_l <= Upsilon s
or Phi_l gap_l <= Upsilon s.  Not bad means: a peak has mu_l >= Phi_l^{1/2}; a strict non-peak has gap_l = M (1 - |v_l|/thr_l) >= Phi_l^{1/2}.
Hence a contribution requires Phi_l^{1/2} <= Upsilon s or Phi_l gap_l <= Upsilon s; in the latter case either gap_l >= M/2, so Phi_l <=
2 Upsilon s/M, or gap_l < M/2, and then gap_l >= Phi_l^{1/2} gives Phi_l^{3/2} <= Upsilon s.  In all cases Phi_l <= X(s) := max(Upsilon^2 s^2,
2 Upsilon s/M, (Upsilon s)^{2/3}).  Order the fine carriers of ALL blocks by stage.  Inside a cluster (A1) the weights decrease by the
factor 4 ((A4)); between consecutive clusters, and from the last carrier before a main stage to that main stage, they drop super-
exponentially (c_{l+1} <= T_lo(l)^3 and (W4''); in particular Phi_{L'} <= Phi_{L'-1}^7 for every large main stage L', checked from
n^w_l >> 2^{l^3}: 3 n^w_l >= 14 l + 18 log_2(1/T_lo(l-1))).  Hence sum_{l >= L'} Phi_l <= 2 Phi_{L'} for main stages L'.  Choose main stages
L_i -> infinity and s_i with X(s_i) := Phi_{L_i}^{1/2} Phi_{L_i - 1}^{1/2}: then {Phi_l <= X(s_i)} = {l >= L_i}, the contributions are
<= 2 Phi_{L_i}, and s_i >= X(s_i)^{3/2}/Upsilon gives Phi_{L_i}/s_i <= Upsilon Phi_{L_i}^{1/4} Phi_{L_i - 1}^{-3/4} <= Upsilon Phi_{L_i - 1}^{1} -> 0.
So Scr_m(Upsilon s_i) = o(s_i) for every m in A_- along the same sequence.  QED
Remark.  (R) carriers are never bad: own_l >= delta°_l, while thr_l + Phi_l^{1/2} <= C c_l^{1/2} and in D^{U1} c_l <= T_lo(l-1)^3 <=
2^{-3 n^w_{l-1}} << (2^{-l-2^l-2})^8 <= (delta°_l)^8 for large l (S_l = {2^l(2i+1)}, so ||h_l||_1 >= 2^{-2^l}) — call this (W3'); (Z') carriers
are bad only if |v_l| > thr_l (1 - Phi^{1/2}/M), impossible for |v_l| < thr_l/2.  So only (W) carriers with own_l - |Y_l| in B_l can be bad —
an interval of length about Phi_l^{1/2} in the variable |Y_l|.  In configuration (i) the recursion of Lemma 4.1 never produces (W).

## 5.4 Lemma 5.4 (the recursion survives mixing unless a positive carrier is frustrated).  PROVED.
Run the forward recursion of Lemma 4.1 in a mixed class with the rule: a negative fine carrier takes varsigma := sgn Y (self-aligned, (R));
a positive fine carrier l takes varsigma := sgn Y_l and ANTI-aligned own coordinates z_j := -varsigma sgn u_l(j) on O(l).  Call the positive
carrier FRUSTRATED if |Y_l| < own_l + thr_l/2.  If no positive fine carrier is frustrated, the recursion defines z on J_fine at which
V is admissible on J_fine and every negative fine carrier is (R); hence (SC) for A_- holds (Lemma 4.3 / 5.3) and the class is recovered.
Proof.  For a non-frustrated positive carrier, v_l = varsigma (|Y_l| - own_l) with |v_l| >= thr_l/2, so |w(l)| >= M/2 with sign varsigma; its
coefficient -|Delta''| lambda_l w(l) has sign -varsigma and dominates on O(l) (Lemma 4.2 estimates), so sgn V_j = -varsigma sgn u_l(j) = z_j.
Negative carriers: Lemma 4.1.  Every j in J_fine has an owner (part 4).  QED
A frustrated positive carrier has NO consistent contact state: anti-aligned own coordinates give the wrong sign of v_l, aligned ones give
the wrong sign of V on O(l).  It must take a value of modulus < thr_l/2 with |w| small, which needs non-contact coordinates (|z_j| < 1,
forcing V_j = 0) or balanced cancellations among later carriers; these "zero cascades" couple the carrier to the future, and the negative
carriers downstream may be forced off (R).  This is the mechanism of the residual.

## 5.5 Toy evidence (numerics, U1_work/mixed_fixedpoint_check.py, mixed_forcedW_check.py, mixed_bad_inspect.py).  HEURISTIC.
Lexicographic model (the limit of super-decreasing weights: the first carrier with nonzero coefficient fixes sgn V_j; balanced tiny-w
states are NOT modelled), 7 carriers of random type N/P, two signature coordinates per carrier (own mass 0.05), later targets meeting
earlier signature coordinates with coefficients ~0.02-0.1, coarse offsets often 0 (frustration).  All 3^7 sign patterns are enumerated,
the free coordinates solved by LP.  Among 148 mixed instances: the forward recursion meets a frustrated positive carrier in 134; exact
completions (in the model) exist in 115; in 3 of these EVERY exact completion puts some negative carrier in (W) (forced wrong branch;
e.g. mixed_bad_inspect: carrier 0 negative with Y = 0.0445 < own = 0.05 is forced to v = -0.0055 by a frustrated positive carrier two
stages later); with a threshold band of relative width 0.08 one instance has NO good completion, with bands 10 and 100 times thinner
none.  Reading: forced (W) is structural in mixed classes, but a BAD (W) needs the coincidence own_l - |Y_l| in B_l, an interval of length
~ Phi_l^{1/2}, astronomically thin in the design (Phi_l^{1/2} <= c_l^{1/2}).  Earlier check (recursion_check2.py): with (W4'') enforced the
configuration-(i) recursion is admissible for every shift vector of the class (200 instances x 50 shift vectors), and violating (W4'')
breaks admissibility in 27% of the instances — (W4'') is necessary for Lemma 4.2, not an artifact.

## 5.6 MASTER THEOREM IV.  PROVED (modulo the refereed tools listed below).
Design D^{U1} (part 3: U4's T_final with the absorber clusters (A1), deep pairs (A2), rule (c''), weights (A4)/(W4''), Design(L) and Q(w)
enlarged by 4^{R_cl(L)}, 2^k, 1/eta_L and D_cls(w)), N fixed, diagonal base.  Let f in S_{p_N^*} have finite base support F.  Suppose that for
infinitely many main stages L some clean sub-window w of L has at least n(w)/D_cls(w) dyadic scales whose activity class (2.3) is
ONE-SIGNED (all active shifts of the same sign, or no active shift).  Then f in Rec: (f, g) in cl NA((c_0, p_N), l_2^2) for every g in C(f).
Proof.  Fix such (L, w).  Pigeonhole over the D_cls(w) (class, cube) pairs (2.2(d)) gives a set S of >= n(w)/D_cls(w)^2 one-signed scales
with one class a and one cube; the sub-window length n(w) >= l 2^{l^3} Q(w) (as used in 2.6) and Q(w) >= D_cls(w)^2 (Design/u)^C (part 3
(A4)) give |S| >= l 2^{l^3} (Design/u)^C >= 48 rho^2 K/(c_flat (1 - rho^2)) with K = C_f (Design/u)^C, and K T_hi(w)/|S| -> 0, as Lemma
2.4 requires.  Build f^# by part 4: (1a) V1's moves and the realization of the Lojasiewicz point of Gamma^#(kappa, a) (Theorem
2.3: one kappa-push per block, Lemma 1.5 final form), (1b) zero-value tuning of the absorbers (Lemma 3.3), (1c) re-push / re-tune, (2)
the fine structure: configuration (i) the recursion (Lemmas 4.1, 4.2), configuration (ii) the Schauder completion (Lemma 4.4), A empty: no
shifted fine carriers (only the fixed owners).  At every t in S the data of Proposition 2.2(e) are exact two-piece data at f^# with the
common shift Delta''^* (Lemmas 4.6, 5.1; absorption on E_c by Proposition 3.4), they satisfy the size conditions of kinds [1]-[3] (V1 TR(iii),
Prop. 3.4(c)), p*(g - g_t) <= K t, kappa_w <= 1 + eta_0/2, and p*(f^# - f) <= theta_w T_lo(w)^2 with theta_w -> 0 (Lemma 4.5).  In
configuration (i), A_- = A satisfies (SC) at f^# (Lemma 4.3).  The windowed recovery (V2 Theorems E^>= / E^SC = Z3 Theorem E with V1's
banked/pulled supports, Theorem E''), run with the subset S (Lemma 2.4), along the infinitely many windows, gives (f, rho g) in cl NA for
every rho < 1, hence (f, g) in cl NA.  QED
Refereed tools used: V1 (Proposition TR, Lemmas TU, ST, CO, D, S, B; Theorem E''), V2 (Lemmas H, L, C5; Theorems E^>=, E^SC; Theorem B),
Z3 (Theorem E, Lemma U, Lemma 3.1), U4 (T_final, Lemma GW, Lemma W) and the note (lem:threshold, def:twopiece, thm:engineered, cor:D1,
lem:scrambling, def:SC, lem:switchbudget, lem:suplevel).

Corollary IV.1 (one block).  PROVED.  For N = 1 every activity class is one-signed; hence EVERY f in S_{p_1^*} with finite base support is
in Rec(p_1): Lemma Z holds at finite F for p_1 with the design D^{U1}.  (Clean sub-windows exist at every large main stage: V1/U4.)
Corollary IV.2 (structure of a counterexample, N >= 2).  PROVED.  If f (F finite) is not in Rec(p_N), then at every large main stage L and
every clean sub-window w of L, more than n(w)(1 - 1/D_cls(w)) scales carry MIXED classes: both a block with active negative shift (data
Delta d < 0) and a block with active positive shift.  By Lemma 5.4, at each such scale the forward recursion meets a frustrated positive
fine carrier.  [Transfer to Martin's p via lem:martintail is NOT claimed: the one-signed hypothesis is not N-independent.]
Corollary IV.3 (mixed classes without frustration).  PROVED.  The conclusion of Master Theorem IV also holds if the scales are counted
in classes that are one-signed OR mixed with no frustrated positive carrier in the forward recursion of Lemma 5.4.
Corollary IV.4 (intrinsic form).  PROVED (modulo V1 Lemma 3.4', refereed).  If for infinitely many main stages L some clean sub-window w
of L has I_up(w) = {} or I_lo(w) = {} (all source-deficient blocks lack the same source), then f in Rec(p_N).
Proof.  V1 Lemma 3.4': an upper source gives delta_m <= K_d t, a lower source gives delta_m >= -K_d t (decomposition convention delta_m =
Delta d_m M_m; data shift Delta'_dec,m = -delta_m, Prop. 2.2).  Hence a block with both sources has |Delta'_dec,m| <= K_d t; a block of
I_up(w) has a lower source (I_up ∩ I_lo = {}, V1 Lemma S(a)), so Delta'_dec,m <= K_d t: it can be large only NEGATIVELY; a block of I_lo(w)
has an upper source, so Delta'_dec,m >= -K_d t: it can be large only POSITIVELY.  The
projection (2.4(b)) moves components by <= K t, and components below A_1 K t = K_* K t > (K + K_d) t are set to 0 (2.3).  So at every scale
the active negative blocks lie in I_up(w) and the active positive blocks in I_lo(w); if one of these sets is empty every class of w is
one-signed, and Master Theorem IV applies with all n(w) scales.  QED
Remark (where the classes live).  Activity classes are assigned with the coefficients of f^(1a) (after V1's moves and the Lojasiewicz
realization of Theorem 2.3, which exactifies the minors of ALL classes simultaneously and is therefore class-independent); the fine
structure (2) is then built for the chosen class.  No circularity arises.

## 5.7 The precise remaining step (C_mix).  OPEN.
In a mixed class (A_- and A_+ nonempty) at a clean sub-window: find a point z in [-1,1]^{J_free} at which V is admissible on J_fine
(exists: Lemma 5.1) and no negative fine carrier is BAD (value in its threshold band B_l of length ~ Phi_l^{1/2}).  Equivalently (Lemma 5.2):
no negative fine carrier in the wrong branch (W) with own_l - |Y_l| in B_l.  Known: the property holds at every exact completion for the
negative carriers with |Y_l| >= own_l + thr_l (they are (R)); configuration (i) avoids (W) altogether; the toy model shows that mixing can
FORCE (W), and that BAD (W) then requires a coincidence of measure ~ Phi_l^{1/2}.  Natural routes: (a) a selection theorem among the
Schauder fixed points (Browder continuation from A_+-shift 0, where the recursion gives an all-(R) completion, to the actual shift); (b) a
genericity argument in finitely many coarse parameters (a measurable selection of completions plus transversality of Y_l); (c) U3's
violation tolerance (r8/U3_notes.md Lemma VT, Lemma QB2): run the recursion of Lemma 5.4 with frustrated positive carriers simply
anti-aligned; the resulting sign violations sit on their own sets, with l_1-mass <= C_f sum_{l > L} lambda_l own_l <= C_f c_{L+1} (fine
origin), exactly the violations U3's (S2) is designed to tolerate — so (C_mix) is implied by U3's open step (S2) (SKETCH of the reduction).

## 5.8 Corrections to earlier rounds (recorded).
 - V2's "near-coordinate conversion" (SKETCH in V2 4.3) is FALSE as stated for super-decreasing signature weights: free signs on the near
   coordinates of a signature set cannot reproduce the original value up to the far tail (the achievable signed sums form a Cantor set;
   the discrepancy is of the order of the first converted weight).  Replaced by zero-value absorbers (part 3).
 - V2's gap (C*-3) asked for INDEPENDENT exactification of theta_m and A_m: unnecessary — only kappa_m enters (Lemma 1.3); one push per
   block suffices (Lemma 1.5), and the buffer peak always works once Omega contains all coarse strict non-peaks.
 - Part 4 (this round): tuned absorbers that are not used must carry a positive switching coefficient c_0(a) (not 0), otherwise the far
   parts of their signature sets, fixed at +1, are not protected.
 - recursion_check.py (first version) violated (W4''); the corrected toy confirms Lemma 4.2 and the necessity of (W4'').
