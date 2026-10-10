# V2 part 4 — Item (C), case (II): shifted data.  Rigidity, intrinsic shifts, fine completion, the remaining step

Setting as in Part 3; data convention Delta_m := d_m(omega^-_m) - d_m(omega^+_m) (Definition def:twopiece); for a pair of
two-piece data put Omega := the (finite) set of carriers in the supports of the omega^+-_m, Sigma_Omega := F u
union_{k in Omega} supp u_k, and W_Delta := sum_m Delta_m R_m^* w_m in l_1.

## 4.1 Proposition C3 (rigidity of shifted data).  PROVED.
Let (b^+-, omega^+-) be two-piece data at a first row f with F finite.  Then for every j notin Sigma_Omega:
    W_Delta(j) = 0 if |z_j| < 1,     and   z_j W_Delta(j) <= 0 if |z_j| = 1.
Proof.  Subtracting the two representations, v := b^+ - b^- = sum_m R_m^*(omega^-_m - omega^+_m) - W_Delta.  At j notin
Sigma_Omega the first sum vanishes, and two-piece data have v(j) = 0 off F u K and z_j v(j) >= 0 on K.  QED
**Corollary C3.1.**  PROVED unless marked.
 (a) (Z4-ref Prop. 5.6') On the far part of every signature set S_l (l notin Omega, w_m(k(l)) != 0, Delta_{m(l)} != 0) the own
     term dominates the later targets, so S_l is far-swallowed with eps_l = -sgn(Delta_m) sgn w_m(k(l)).
 (b) For the designs of the note, EVERY coordinate j lies in the target support of infinitely many carriers of EVERY block:
     by density of the targets some y^(i) has q*(y^(i) - e_j^*/q*(e_j^*)) < 1/(2 q*(e_j^*)), hence (q* >= ||.||_1) y^(i)(j) >
     1/(2 q*(e_j^*)) > 0, and every index i is used at
     infinitely many levels of every block (y^(i) is allowed at all large levels and (i_r) repeats i; Theorem thm:SLD).
     Hence, at every free coordinate j outside the finite set Sigma_Omega, (a) does not apply and Proposition C3 is the
     exact cancellation identity
        sum_m Delta_m sum_{k : j in supp y_k} lambda_k w_m(k) y_k(j)/n_k  (+ the own signature term if j in some S_l) = 0,
     an infinite series over carriers of all blocks; the carriers with |u_k(zhat)| >> Phi_k (all but those with tiny values)
     are peaks, w_m(k) = +-M_m.  So shifted data exist only at first rows satisfying one exact identity per free coordinate
     (HEURISTIC reading: non-generic at partial contact; not claimed as a theorem).
 (c) At maximal contact (z = +-1 off F) the identities (b) are void, but there (SP_w) holds at every large level (Y1 Cor. M1
     via Z4 Lemma 5.0) and case (II) of Theorem C1 does not occur.

## 4.2 Proposition C4 (non-constant splits force shifted data).  PROVED.
Let l be a class-G peak of block m of a first row f' (z' = eps_l on S^nat_l \ F'), vs := sgn w'_m(k(l)), and let h carry
two-piece data (b^+-, omega^+-) at f'.  For finite disjoint S_1, S_2 subset S^nat_l \ Sigma_Omega put V_i := sum_{S_i} v_l(s)
and A_i(h) := sum_{s in S_i} eps_l h(s)/V_i.  Then, with tgt := max_{m', +-} |d_{m'}(omega^+-_{m'})| sum_{s in S_1 u S_2}
sum_{l' > l} lambda_{l'} |u_{l'}(s)| (later targets; the double sum is <= (2/9) sum_s 2^{-2s} c_l delta_l by allowedness (b)),
    A_i(h) in [ -d_m(omega^+_m) lambda_l M'_m eps_l vs - tgt/V_i ,  -d_m(omega^-_m) lambda_l M'_m eps_l vs + tgt/V_i ]  (eps_l vs = +1;
    the interval is reversed if eps_l vs = -1),
hence |A_1(h) - A_2(h)| <= |Delta_m| lambda_l M'_m + tgt (1/V_1 + 1/V_2).  Consequently, if g (a mate of f) and functionals g_t
with ||g - g_t||_1 <= K t carry two-piece data at f', then
    |Delta_m(g_t)| >= ( |A_1(g) - A_2(g)| - (K t + tgt)(1/V_1 + 1/V_2) ) / (lambda_l M'_m).
Proof.  At s in S^nat_l \ Sigma_Omega the + representation gives h(s) = b^+(s) - d_m(omega^+_m) lambda_l w'_m(k(l)) v_l(s) + (later
targets at s) (omega^+ vanishes at k(l), a peak, and at carriers not in Omega; other signatures vanish at s; earlier targets
avoid S_l by allowedness (a)); side + gives eps_l b^+(s) >= 0 (z' = eps_l there).  Multiply by eps_l, sum over S_i, divide by
V_i; the - side is symmetric with eps_l b^-(s) <= 0.  The last claim: |A_i(g) - A_i(g_t)| <= Kt/V_i.  QED
Reading.  The DECOMPOSITIONS of g at scale t satisfy the same sandwich with (d_+, d_-) in place of (d(omega^+), d(omega^-)) up
to the budget (B_+- are z-signed up to l_1 mass t/q_0) and the pinned peak terms (|alpha||omega_+-| <= t/(2 sigma) at robust
peaks): the profile eps_l g(s)/v_l(s) on the signature set of a robust class-G peak may OSCILLATE inside an interval of length
|Delta d^dec_m| lambda_l M (the "non-constant split" of the classical switching mates, Round 1-2).  Proposition C4 shows that
such an oscillation is visible to every approximating data set at every first row f' sharing the peak: d-neutral data
(Delta = 0) cannot follow a mate whose profile oscillates by more than (Kt + tgt)(1/V_1 + 1/V_2), at ANY companion.  So in case
(II) of Theorem C1, for mates with persistent oscillating profiles, the exact-data route NEEDS Delta != 0 data, and by
Proposition C3 these need the exact identities of Corollary C3.1(b) at the companion.
Example (PROVED: the data computation).  Let block m be in configuration (i) with EXACT coherence at f: R_m^* w_m 1_{F^c} is
z-signed and vanishes off F u K, and some class-G strict non-peak k_1 of block m with q < 0 is resonant (eps u_{k_1} 1_{F^c}
z-signed, supported in K).  Let c > 0 be small, phi >= 0 supported in S^nat_l (l a swallowing-type robust G-peak of block m)
with phi <= c lambda_l M v_l and phi in l_1, and b_0 supported in F with c q_0 b_0(zhat) = c sigma_m - eps_l q_0 phi(zhat) (possible
since a(zhat) = 1 != 0), so that g(xi) = 0 for
    g := c(b_0 - R_m^* w_m) + eps_l phi
carries the two-piece data (b^+, omega^+) = (c b_0 - kappa lambda_{k_1} u_{k_1} + eps_l phi, kappa e_{k_1}), kappa := c C_m/(Phi_{k_1}^2
w_m(k_1)) (so d(omega^+) = c), and (b^-, omega^-) = (g, 0); Delta_m = -c < 0, and A_1(g) - A_2(g) = sum_{S_1} phi/V_1 -
sum_{S_2} phi/V_2 (+ later-target terms), arbitrary in [-c lambda_l M, c lambda_l M] (choose phi/v_l = 0 on S_1 and = c lambda M
on S_2).  For small c, Gamma_w of both pairs is small, so by Proposition prop:onesidedupper the one-sided coefficients of g
are finite; the example shows the STRUCTURE (forced Delta = -c, oscillating profile), not a new mate class.  (Side +: eps_l phi has the sign eps_l = z on S^nat_l and -kappa lambda u_{k_1} is
z-signed by the choice of k_1; side -: z_j g(j) = -c z_j (R^*w)(j) + phi(j) <= 0 since z(R^*w) = lambda_l M v_l on S^nat_l
for the swallowing-type peak and phi <= c lambda M v_l.)

## 4.3 Lemma C5 (completion of the fine tail).  PROVED.
Let f^# be a first row with finite base support, l a level, J_fine := N \ (F^# u T(l) u union_{l' <= l} S_{l'}) (coordinates
touched by no coarse carrier), and Delta in R^I.  For z' in [-1,1]^{J_fine} let f(z') be the first row with forced data
(a^#, z^# with its J_fine-coordinates replaced by z') (admissible forced data: Remark rem:lemmaZ(c); a, e unchanged), w_m(z')
its block functionals and W(z') := sum_m Delta_m R_m^* w_m(z').  Then there is z'* with
    W(z'*)(j) = 0 if |z'*_j| < 1,   z'*_j W(z'*)(j) <= 0 if |z'*_j| = 1        (j in J_fine),
i.e. the shift vector -W(z'*) is exactly admissible (z-signed on contacts, zero on free coordinates) on J_fine, and
p*(f(z'*) - f^#) <= C_f T_lo(l)^3 log(1/T_lo(l)); coarse values are unchanged and block thresholds move by <= C_f T_lo(l)^3.
Proof.  Phi(z')_j := clamp_{[-1,1]}(z'_j - W(z')(j)) maps the compact convex metrizable set C := [-1,1]^{J_fine} (product
topology, J_fine countable) into itself.  Continuity: zhat(z') = z^#(z') + U e^# depends coordinatewise continuously on z';
(R_m^** zhat(z'))(k) = lambda_k u_k(zhat(z')) is continuous in l_1 by dominated convergence (sum_k lambda_k ||u_k||_1 < infinity);
R_m^** zhat(z') != 0 (a(zhat(z')) = ||a||_1 + nu = 1 and R_m^** is injective); the duality map of the smooth norm |.|_m is
norm-to-weak* continuous (Lemma A(d)), so each w_m(z')(k) is continuous and bounded by 1; W(z')(j) = sum_m Delta_m sum_k
lambda_k w_m(z')(k) u_k(j) is continuous by dominated convergence.  By the Schauder-Tychonoff theorem Phi has a fixed point
z'*; reading clamp(z_j - W_j) = z_j gives the three cases.  Cost: only coordinates of J_fine move, which no coarse carrier
touches; Z3 Lemma 3.1 with sum_{k > l} lambda_k <= T_lo(l)^3 gives the bound and the threshold/scalar motion.  QED
So the fine tail of a shifted data set can always be made exactly admissible at a cheap companion.  What Lemma C5 cannot do is
on the COARSE coordinates T(l) u union_{l' <= l} S^nat_{l'}: there the fine contributions -sum_m Delta_m sum_{k > l} lambda_k
w_m(k) u_k(j) (of size <= |Delta| T_lo(l)^3) must be absorbed EXACTLY by the coarse data.  On the near coordinates of a GOOD
coarse signature set this can be done by converting them into tiny-mass support coordinates with free signs chosen to keep
sum_s v_{l'}(s) z_s (hence the value and the room of l') unchanged up to the far tail (SKETCH: finitely many coordinates, cost
tiny; rooms matter only for pinning at f).  On the free coordinates of T(l) and on the signature sets of UNSWITCHED class-G
carriers hit by wrong-sign fine contributions, absorption requires the coarse shifted system to be STABLE: its exact
solutions with Delta != 0 must persist under perturbations of the Delta-columns of size T_lo(l)^3 (Slater-type condition:
strictly positive switching on those carriers, surjective equality rows on T(l)).

## 4.4 Conditional recovery and the remaining step
**Theorem C6 (case (II) with stable shifted resonance).**  SKETCH.  Suppose that at infinitely many levels a clean
sub-window w with case (II) satisfies: (ST_w) the coarse shifted exact cone at the companion (Part 2 system Sigma^# plus the
columns Delta_m R_m^* w^#_m restricted to coarse coordinates, with the coupling Delta_m = sum q^#_l tau_l of Part 3 (R4)) has a
Slater point with robust margin, and the configuration of every shifted block gives Delta_m >= 0 in the data convention
(configuration (ii): free decomposition shift downward), or Delta_m < 0 in blocks satisfying (SC) at the companions
(configuration (i)).  Then f in Rec.
Sketch.  Transplant (Prop. T with shift columns; Hoffman via Lemma H, exactification via Lemma L extended to the block scalars
A_m, M_m/C_m entering the coupling — this extension is NOT proved: block scalars are not independently tunable by the tools
of Part 2); fine completion by Lemma C5; absorption of the coarse fine-perturbations by (ST_w); recovery by Theorem E^>= or
Theorem E^SC (Part 3).  Gaps: the scalar exactification just named; the near-coordinate conversion; (SC) at the companion in
configuration (i) (the completion can make every fine carrier with H_k >> Phi_k a robust peak of the coherent sign, since in
configuration (i) the self-aligned choice z = sgn u_k on S_k gives |u_k(zhat)| >= delta_k ||h_k 1_{S_k \ F}||/n_k, but the
coarse carriers' distances and the absence of degenerate peaks must also be arranged).
**The precise remaining step for item (C) (OPEN).**  By Theorem C1, f fails the shift pinning at a clean sub-window w only
if rho^sh(kappa, f) <= b(w) (an exact or b-near-exact d-constrained coherent shift resonance of the closed coarse pattern).
If this happens at all but finitely many levels, a mate g whose decompositions use these resonances with oscillating
profiles (Proposition C4; such mates exist under exact coherence, Example in 4.2) can only be followed by data with Delta != 0,
which exist at a companion only if, besides the coarse resonance, the infinitely many identities of Corollary C3.1(b) hold on
the coarse free coordinates (fine tails are completable: Lemma C5).  Needed: either (a) a version of Corollary cor:D1 /
Theorem E for "shifted data exact on coarse coordinates and on J_fine, with errors of l_1 mass <= |Delta| T_lo^3 on the coarse
coordinates touched by fine targets" — an approximately-two-piece statement restricted to errors that are FINE-ORIGIN and
coordinate-localized, or (b) a proof that persistent oscillating shifts at all levels force a cancellation structure making
the identities of C3.1(b) hold at some companion, or (c) a design device making every coarse free coordinate inaccessible to
fine targets of shifted blocks (impossible with (T-d) density: Corollary C3.1(b)), or (d) a mechanism not based on exact
two-piece data.  No counterexample: nothing here suggests that such mates are not recoverable (at maximal contact they do
not arise, and under exact coherence they carry exact data).

**Remark 4.5 (independent tuning of the two block scalars).**  PROVED (local computation).  The coefficients of the coupling
(R4) at peaks and of the shift columns involve, besides values, the block scalars theta_m and A_m = |R_m^** zhat|_m (note
M/C = theta/A).  At a block vector without degenerate peaks and without carriers at the threshold, Lemma T gives
d theta/ds = -(d Psi/ds)/(d Psi/d theta) with d Psi/d theta = -2(A + theta) Phi_P^2 (Phi_P^2 := sum_{k in P} Phi_k^2).  For an
outward push |zeta(c)| -> |zeta(c)| + s at a peak c: d theta/ds = C/Phi_P^2 and dA/ds = 1 - Phi_P^2 d theta/ds = M.  For a push
|zeta(k)| -> |zeta(k)| + s' at a strict non-peak k with relative position rho_k = nu_k/theta: d theta/ds' = -rho_k M/Phi_P^2 and
dA/ds' = rho_k M (= |w(k)|).  Hence det d(theta, A)/d(s, s') = (C/Phi_P^2) rho_k M + (rho_k M/Phi_P^2) M = rho_k M/Phi_P^2 > 0
(the same for (theta, A + theta Phi^2_{pk})).  So both scalars can be tuned exactly and independently (inverse function
theorem, two-sided pushes by pulls/banks/z-moves) whenever the block has a robust peak and a robust strict non-peak with
w != 0 that are NOT variables of the polynomial system; the existence of such a non-peak is not guaranteed in case (II), which
is one of the gaps of Theorem C6.  (All peaks act identically on (theta, A) at first order, so two peaks do not suffice.)
