# Y4 part 2 — Tuning channels: banked companions, raising, and the directional obstruction

Any admissible T, I finite, f in S_{p*} with F finite and forced data (xi, q_0, a, w, F, z, zhat, e, nu); K contacts,
J_free := {j notin F : |z_j| < 1}.  P^perp = orthogonal projection of H onto e^perp.  For W in l_1, x in H:
<U^*W, x> = W(Ux).  A vector W in l_1 is *z-signed* if W(j) = 0 for j in J_free and z_j W(j) >= 0 for j in K (no
condition on F).  Every zero-cost switching vector V = sum_l eps_l tau_l u_l (Lemma lem:exactswitch; Z6 5.2) restricted to
F^c is z-signed, and so is every ray vector V_r of a zero-cost cone.  These tools address item (X1) of part 1 and the
re-tuning question of Z3 4.3(iii) / Z3_ref 2.7(iii) (only |F| - 1 degrees of freedom when supp a is frozen).

## 2.1 Banked companions and their cost
**Definition 2.1.**  For a finite set B subset K and m = (m_j)_{j in B}, m_j >= 0, together with a change beta of a on F
(small, signs on F kept) and a z-move zeta supported in J_free (|z_j + zeta_j| < 1), the *tuned row* f^tau is the first
row with forced data (a^tau, z + zeta), a^tau := A/q^*(A), A := a + beta + sum_{j in B} m_j z_j e_j^*.  It is admissible
(Remark rem:lemmaZ(c)): z + zeta = sgn a^tau on supp a^tau = F u {j in B : m_j > 0}.  Then e^tau = U^*A/||U^*A|| and
zhat^tau - zhat = zeta + U(e^tau - e).  If beta = 0 and zeta = 0 we call f^tau a *banked row*.

**Lemma 2.2 (cost).** PROVED.  There are c_f, C_f > 0 (depending only on f, N, T) such that, with mu := ||m||_1 +
||beta||_1 + ||zeta||_1 <= c_f:  ||e^tau - e|| <= C_f(||m||_1 + ||beta||_1),  p*(f^tau - f) <= C_f mu log(e/mu), and
C_m, M_m, sigma_m, q_0, vartheta_m move by at most C_f mu.
*Proof.* ||U^*A - nu e|| <= ||U||(||m||_1 + ||beta||_1) and x -> x/||x|| is 2/nu-Lipschitz near nu e (the factor
1/q^*(A) does not change e^tau).  Put delta := zhat^tau - zhat; then |u_{k,m}(delta)| <= ||zeta||_1 + ||e^tau - e|| for
all k, m (q^*(u) = 1 gives ||u||_inf <= 1, ||U^*u|| <= 1).  The proof of Z3 Lemma 3.1 (cost of a companion) uses only
zhat^# = zhat + delta and the clamp formula of Lemma lem:F1 at both points (block functionals w^tau_m = J_m(R_m^** zhat^tau),
Remark rem:lemmaZ(c)); it applies verbatim and gives sum_m ||R_m^*(w^tau_m - w_m)||_1 <= C_f c(delta), c(delta) =
sum_m[Delta_m log(e/Delta_m) + sum_k min(lambda_{k,m}, |u_{k,m}(delta)|)] <= C mu log(e/mu) by sum_k min(lambda_{k,m}, x)
<= x(log_2(2m/x) + 3).  Finally f^tau - f = (a^tau - a) + L^*(w^tau - w), q^*(a^tau - a) <= C(||m||_1 + ||beta||_1).  QED

**Lemma 2.3 (Lemma U and Theorem E with banked support).** PROVED (by inspection).  Z3 Lemma U and Z3 Theorem E remain
true if "supp a_j = F" is replaced by "supp a_j = F u B_j, B_j a finite set of contacts of f carrying masses at f_j",
provided the data (b^pm, omega^pm) at f_j are CONTACT-LIKE on B_j: z_i b^+_i >= 0 >= z_i b^-_i (i in B_j).
*Proof.* supp a_j = F is used in Lemma U only for the no-flip condition on F (a_{j,min} -> a_min > 0, Lemma
lem:onesidedtransfer, Base).  On B_j, a_j(i) = m_i z_i, and for side-+ data and r > 0, |a_j(i) + r b_i| - |a_j(i)| -
z_i r b_i = (m_i + r|b_i|) - m_i - r|b_i| = 0; for side-- data and r < 0 likewise.  So B_j contributes nothing to the base
excess, exactly like contacts; all other steps (Hilbert part with nu_j -> nu, blocks, persistence of transfer data along
f_j -> f) are unchanged.  In Theorem E, contact-like data on B_j subset F_j are two-piece data at f_j (no condition is
imposed on support coordinates), and Corollary cor:D1 applies at f_j since F u B_j is finite.  QED
*Remark.* In Z3 Proposition T, b^+ = B_+1_F + chi V' - kappa a with V' z-signed: transplanted data are automatically
contact-like on every contact, in particular on any bank.

## 2.2 Channels; injectivity; raising
For W in l_1 put h_W := U P^perp U^* W in c_0 (so ||P^perp U^*W||^2 = W(h_W) = sum_j W(j) h_W(j)).  To first order, a mass
m_j at j in K changes W(zhat) by (m_j/nu) z_j h_W(j); a change beta_j on F by (beta_j/nu) h_W(j) (either sign); a z-move
zeta_j at j in J_free by zeta_j W(j) (either sign, within the room).

**Lemma 2.4 (joint injectivity).** PROVED.  If W in Y = T(l_1(N x N)), h_W(j) = 0 for all j in F u K and W(j) = 0 for all
j in J_free, then W = 0.
*Proof.* ||P^perp U^*W||^2 = sum_j W(j) h_W(j) = 0 (each term has a vanishing factor).  So U^*W is a multiple of
e = U^*a/nu, W = mu a by injectivity of U^*, and W in Y cap c_00 = {0} (T-c), since a in c_00.  QED

**Lemma 2.5 (quantitative injectivity; design constant).** PROVED.  For s >= 1 and a finite-dimensional subspace W of Y
there are J_max(W,s) and gamma(W,s) > 0 depending only on W, s, U such that for EVERY f with F subset [1,s] (any z):
max_{j <= J_max} chan_j(W) >= gamma ||W||_1 for W in W, where chan_j(W) := |h_W(j)| (j in F u K), |W(j)| (j in J_free).
*Proof.* Compactness: kappa^2 := min{||P^perp_{e'}U^*W||^2 : W in W, ||W||_1 = 1, e' = U^*a'/||U^*a'||, a' in l_1(F'),
||a'||_1 = 1, F' subset [1,s]} > 0 (Lemma 2.4's argument for each pair; continuity).  ||h_W||_inf <= ||U||^2, and the
tail eps(J) := max{||W1_{(J,inf)}||_1 : W in W, ||W||_1 = 1} -> 0.  With ||U||^2 eps(J_max) <= kappa^2/2:
kappa^2/2 <= sum_{j <= J_max} W(j)h_W(j) <= max_{j <= J_max} chan_j(W) (1 + J_max ||U||^2).  QED

**Lemma 2.6 (raising lemma).** PROVED.  Let W be z-signed and nonzero.  For small m > 0 the tuned row with base part
a^m proportional to a + m W (masses m W(j) at j in K cap supp W, change m W(j) on F) is admissible (z unchanged), and
   d/dm W(zhat^m) |_{m=0} = ||P^perp U^* W||^2 / nu > 0 .
More generally, for z-signed W_1, ..., W_p the map m in R^p_{>= 0} -> (W_i(zhat^m))_i, a^m prop. to a + sum m_k W_k, has
derivative G/nu, G_{ik} = <P^perp U^*W_i, P^perp U^*W_k> (the Gram matrix, positive definite when the W_i are linearly
independent, by Lemma 2.4).  Every first-order change obtainable from banks at contacts (beta = 0, zeta = 0) is of the
form (sum_j (m_j/nu) z_j h_{W_i}(j))_i, m >= 0.
*Proof.* a + mW has the signs of a on F (m small) and sign z_j at j in K cap supp W; elsewhere it is 0.  de/dm =
P^perp U^* W/nu, and dW(zhat)/dm = <U^*W, de/dm>.  QED

**Proposition 2.7 (exact tuning in a reachable direction).** PROVED.  Let V_1, ..., V_p in Y and let Delta in R^p.  A
*move* is x = (m, beta, zeta) with m >= 0 on a finite set of contacts, beta on F, zeta on free coordinates; its
first-order effect is Lx := (V_i(d zhat))_i.  Suppose:
  (TC) there are p moves x^(1), ..., x^(p) of l_1-norm 1 (each either a single mass direction e_j, j in K, called
       one-sided, or a two-sided direction on F or J_free) such that the p x p matrix A := [L x^(1), ..., L x^(p)] is
       invertible with ||A^{-1}|| <= Gamma, and s^0 := A^{-1}Delta satisfies s^0_k >= c|Delta| > 0 for every one-sided k.
Then there is C(f) such that if C(f) Gamma^3 |Delta| <= c (and the moves stay inside the rooms of the z-channels used),
there is a tuned row f^tau with V_i(zhat^tau) = V_i(zhat) + Delta_i EXACTLY, a move of l_1-norm <= 2 Gamma |Delta|, and
p*(f^tau - f) <= C_f Gamma |Delta| log(e/(Gamma|Delta|)).
*Proof.* psi(s) := Phi(sum_k s_k x^(k)), s in R^p, where Phi(x) := (V_i(zhat(x)) - V_i(zhat))_i.  psi is C^2 near 0 (masses
and beta enter through e(x) = U^*A(x)/||U^*A(x)||, smooth near nu e; zeta linearly), psi(0) = 0, D psi(0) = A,
|D^2 psi| <= C_2(f).  The map s -> s - A^{-1}(psi(s) - Delta) is a contraction of the ball |s - s^0| <= 2 Gamma^2 C_2
|s^0|^2 into itself when |s^0| <= Gamma|Delta| is small (standard quantitative inverse function theorem); its fixed
point s^* solves psi(s^*) = Delta with |s^* - s^0| <= 2C_2 Gamma^3 |Delta|^2 <= c|Delta|/2, so s^*_k >= c|Delta|/2 > 0 on
one-sided k: the move is admissible.  Lemma 2.2 gives the cost.  QED
If only two-sided channels are used, (TC) needs only independence of the restricted channel vectors (Lemma 2.5).
Masses at contacts are ONE-SIDED channels; this is where the difficulty sits (2.3).

## 2.3 The directional obstruction
**Proposition 2.8 (masses raise z-signed functionals; diagonal bases cannot lower them).** PROVED.
(a) For every z-signed W != 0 there is a bank (namely a^m prop. to a + mW) that strictly increases W(zhat) (Lemma 2.6).
(b) Suppose the base is DIAGONAL: U^*e_j = s_j k_j with (k_j) orthonormal in H and s_j > 0 (an admissible choice of the
canonical base).  Then for every z-signed W and every tuned move with beta = 0, the first-order change of W(zhat) is
sum_{j in K} (m_j/nu) s_j^2 z_j W(j) >= 0 (z-moves on J_free do not see W).  Hence with diagonal U, LOWERING a z-signed
functional is possible only through the |F| two-sided channels beta on F (and normalization removes one of them).
*Proof.* (b) For j notin F, (U P^perp U^* W)(j) = <P^perp U^*W, U^*e_j> = s_j^2 W(j) - <U^*W, e><e, U^*e_j>, and
<e, U^*e_j> = <U^*a, U^*e_j>/nu = s_j^2 a_j/nu = 0 for j notin F.  So z_j h_W(j) = s_j^2 z_j W(j) >= 0 on K, and W = 0 on
J_free.  QED
**Remark 2.8' (second-order global rescaling).** PROVED.  With a diagonal base, let D_c subset K be a finite set of
"donor" contacts disjoint from F and from the supports of a finite family V of vectors, and put masses m_j (j in D_c).
Then X := sum m_j z_j s_j k_j is orthogonal to U^*a and to every U^*V (V in V), so for V in V, EXACTLY,
   V(zhat^tau) = V(z) + lambda <U^*V, e>,   lambda := nu/(nu^2 + ||X||^2)^{1/2} in (0,1],  ||X||^2 = sum m_j^2 s_j^2 :
all Hilbert parts are rescaled by one common factor.  Functionals with <U^*V, e> > 0 are LOWERED by (1 - lambda)<U^*V,e>
at mass cost ~ (nu/s_{j_d}) (2(1 - lambda))^{1/2} (one donor): a square-root cost, affordable by a design with
b(w) <= T_lo(w)^8.  This is one global lowering direction (the base analogue of Y2's donors, which rescale block
quantities); it gives no independent control of several functionals.
*Proof.* <U^*V, k_j> = s_j V(j) = 0 and <U^*a, k_j> = s_j a_j = 0 for j in D_c; hence ||U^*A||^2 = nu^2 + ||X||^2 and
<U^*V, U^*A> = <U^*V, U^*a>.  z is unchanged.  QED

*Reading.*  Exactification has two directions.  CLOSING moves (raise near-contacts to contacts, raise target rooms, raise a
NEGATIVE d-sum V(zhat) < 0 of a z-signed ray to 0) go in the direction that banks provide; OPENING moves (lower a POSITIVE
tiny d-sum of a z-signed ray or carrier to 0; lower a resonant swallowing-type peak below its threshold) go against it.
Closing a room raises eps u_l(zhat) by Re(u_l) >= 0 (Z3 Lemma 1.4) — the same direction as banks.

## 2.4 What tuning and pinning remove, and what remains
At a clean sub-window w of D^PW (part 1), every coarse object is robust (rate >= u(w)) or tiny (rate <= b(w)); a fixed
object with positive rate is robust at all late sub-windows, so tiny objects are those of high level whose rates were
made super-small by f.  Combining Theorem E (+ Lemma 2.3), Lemma 1.8 (ray removal), Lemma 2.2, Propositions 2.7, 2.8:
 (i) rooms (R1), target rooms (R2): tiny ones are closed (closing direction, cost <= design x b(w), Z3_ref Prop 4.3.1(b));
     robust ones pinned.  PROVED as a reduction (given the transplant, Z3 Prop T with Z3_ref fixes).
 (ii) anti-sign (q < 0) swallowed strict non-peaks with tiny gap: dropped, by Lemma 2.9 below; robust gaps are a rate
     (Z6_ref 3.6).  PROVED.
 (iii) d-rows, single-block rays.  If the zero-cost cone of the block contains a ROBUST ray of each sign (robustly
     compensated block): the d-mismatch of the switching vector is removed by Lemma 1.8 (removal of rays of the sign of
     the mismatch) or by ADDING a robust ray of the opposite sign (cost |mismatch|/u(w)); tiny rays need no
     exactification at all.  If there is no robust NEGATIVE ray but tiny negative rays carry the mismatch: raise them
     (Lemma 2.6; exactly, for one ray; for several, under (TC)).  PROVED (single ray) / conditional on (TC).
 (iv) The DIRECTIONAL RESIDUAL (OPEN): 
     (UN+) a block whose zero-cost cone has, at the relevant levels, no robust ray of negative d-sum, while the mate
           switches persistently through rays of TINY POSITIVE d-sum (nearly neutral, positively d-coupled directions;
           this is Z6's item K_nn in uncompensated blocks, now isolated as a direction problem, not a rate problem);
     (P+)  resonant swallowing-type peaks with tiny relative margin carrying persistent switching (Z6's K_P and case (d)):
           pushing them to the non-peak side by moving u_l(zhat) would lower a z-signed functional; but the push can
           instead be done by RAISING THE THRESHOLD of the block (Y2's donors: z-moves on an unused signature set, which
           change no used value u_l(zhat) and rescale all d-coefficients of the block by one factor, Y2 Proposition Q /
           Theorem P).  So (P+) is settled by Y2 except in Y2's "aligned corner"; the genuinely directional residual is (UN+).
     For these the companion route needs LOWERING channels (impossible with a diagonal base beyond |F| - 1 dimensions,
     Prop. 2.8(b)), or a mate-side bound (Z6 Conjecture G for (UN+): switching through nearly neutral directions is
     <= C t x design), or a base U with mixing (non-diagonal) channels satisfying (TC) for lowering directions
     (HEURISTIC: for U^*e_j = s_j(k_j + (-1)^j kappa g), z-signed W have h_W(j) = s_j(-1)^j kappa^2 S(W) + ... of both
     signs at far contacts, so lowering channels exist when S(W) != 0; not proved in the needed uniformity).

**Lemma 2.9 (anti-sign threshold lemma).** PROVED.  Let l = j(k,m) be swallowed with sign eps_l, k in Q_m with
varsigma := sgn w_m(k) = -eps_l (i.e. q_l < 0).  For every two-sided decomposition at scale t <= min(t_eta, 1), with
tau_l := -eps_l Delta theta_l:   tau_l <= lambda_l (3 gap_m(k)/t + |Delta d_m| M_m).
*Proof.* Lemma lem:suplevel(f) and |d_pm t| <= 1/2 give varsigma omega_+(k) <= (3/2) gap/t and varsigma omega_-(k) >=
-(3/2) gap/t.  Since omega_pm = Theta_pm + d_pm w, (omega_+ - omega_-)(k) = Delta Theta(k) + Delta d w(k) with
Delta Theta(k) = Delta theta_l/lambda_l = -eps_l tau_l/lambda_l; multiplying by varsigma (varsigma eps_l = -1):
tau_l/lambda_l + Delta d |w(k)| <= 3 gap/t.  QED
*Consequence.* With (tau_l)_- bounded by the budget on the private part of S_l (Lemma lem:modswallow(b); Z6_ref Thm U'
step (2)), swallowed q < 0 strict non-peaks with gap <= t^2 are pinned like anti-sign peaks: |tau_l| <= lambda_l(3 + K_d)t
+ c/(2m_l).  They can be dropped from the data at cost O(K t): no gap rate and no push is needed for them.

## 2.5 Non-window viewpoints (task (b)(ii)-(iii))
 (a) **Convexity in the first row.** PROVED (elementary).  For fixed g, rho: D(rho g) := {h : (h, rho g) contractive} =
     {h : h(y)^2 <= p(y)^2 - rho^2 g(y)^2 for all y} is convex, symmetric, weak* compact.  Lemma Z for (f,g,rho) is the
     statement that Rec cap S_{p*} meets D(rho g') near f for some g' near g.  The forced-data map (a', z') -> f' is not
     affine (through J_V), so this convexity does not give a convex problem in the forced data; in particular I found no
     way to turn it into an existence proof (HEURISTIC assessment).
 (b) **Locality.** PROVED (Lemma lem:slack + triangle inequality): if p*(f' - f) <= eps then p*(f' + r rho g) <= s(r) for
     |r| >= (6 eps/(1 - rho^2))^{1/2}.  Hence Lemma Z is a LOCAL statement at f' on the scale range |r| <~ p*(f' - f)^{1/2}:
     any method must certify (a modification of) rho g at the small scales of f', i.e. needs exact local structure at f'.
     Theorem E is the quantitative form; a non-window method would have to produce such structure at f' by other means.
 (c) **Baire.** Remark rem:meagre(c) already excludes category arguments.  Nothing new.
 (d) **Multi-level companions.** A tuned row per clean sub-window, used only on that sub-window (scale decoupling), needs no
     compatibility between levels; transitivity (Theorem thm:transitivity) is not needed because Theorem E builds the
     norm-attaining approximants directly.  This is the scheme of (b)(i); its only remaining obstacle is (iv) above.
