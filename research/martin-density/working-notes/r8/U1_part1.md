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
