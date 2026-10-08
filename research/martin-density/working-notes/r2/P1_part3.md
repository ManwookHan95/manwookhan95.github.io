# P1 part 3: single-scale structure, the transfer identity, matching, and the block-tame description of Def(f)

Setting: finite I, f in S_{p*} with forced data (A_notes §1, §4). For tau != 0 an ADMISSIBLE decomposition at scale tau is
  f + tau g = A + L*W,  q*(A) <= s(tau), N_m(W_m) <= s(tau) for all m;  A = a + tau B, W = w + tau Omega  (so g = B + L*Omega).
eps(tau) := s(tau) - 1 <= tau^2/2. For a block m: level ell_m := ||W_m||_inf, peak deviations delta_k := ell_m - sigma_k W_m(k) >= 0
(k in P_m), weights alpha_{m,k} (Fact C), |alpha_{m,k}| = lambda_{k,m} mu_{k,m}/|zeta_m| with margin mu_{k,m} := |u_{k,m}(xi)| - theta_m Phi_m(k) >= 0.

## 3.1 Lemma (resource bounds at one scale). PROVED.
For every admissible decomposition at scale tau:
 (B1) sum_{j notin F} ( |B_j| - sign(tau) z_j B_j ) <= eps/(q_0 |tau|);  in particular sum_{j notin F} (1 - |z_j|)|B_j| <= eps/(q_0|tau|) and
      the "paid" contact usage sum_{j in K} |B_j| 1[sign(tau B_j) = -z_j] <= eps/(2 q_0 |tau|);
 (B2) Fl_B(tau) = sum_{j in F} 2(-sign(a_j) tau B_j - |a_j|)_+ <= eps/q_0;
 (B3) nu Psi(tau U*B/nu) <= eps/q_0, hence ||P_{e perp} U*B||^2 <= (2 eps/(q_0 tau^2)) nu (1 + |tau| ||U*B||/nu);
 (K1) sum_{k in P_m} |alpha_{m,k}| delta_k <= eps/|zeta_m|;
 (K2) tau^2 ||P_m-perp D_m Omega_m||^2/(||D_m W_m|| + <D_m W_m, D_m w_m>/C_m) <= eps/|zeta_m|;
 (K3) |w_m(k) + tau Omega_m(k)| <= ell_m <= s(tau) for every k (box).
*Proof.* Budget identity (A Lemma 7.1): q_0 E_q(A) + sum_m |zeta_m| e_m(W_m) <= eps, all terms >= 0; exact excess formulas
(A Lemma 7.2) express E_q(A) as Fl + sum_{j notin F}(|tau B_j| - z_j tau B_j) + nu Psi, and e_m as the peak sum plus the
Hilbert term; each nonnegative piece is bounded by the whole. (B3): Psi(h) >= ||h_perp||^2/(2(1 + ||h||)) (A Lemma 4.3). QED.

## 3.2 Definition (window / one-sided / remainder at scale tau; parameter c_0 in (0,1/4]).
 * base window: j in F with |tau B_j| <= |a_j|/c_0 ("two-sided": certificate radius >= c_0|tau| coordinatewise);
 * base one-sided: (i) near-contacts K_{c_0} := {j notin F : |z_j| > 1 - c_0} used with the cheap sign (sign(tau B_j) = sign z_j);
   (ii) near-flip coordinates j in F with |tau B_j| > |a_j|/c_0 used with the cheap sign (sign(tau B_j) = sign a_j);
 * base remainder: everything else off F (free coordinates, paid usages): by (B1),(B2) its l_1 mass is <= 2 eps/(c_0 q_0 |tau|) <= |tau|/(c_0 q_0);
 * block window: off-peak k with |tau Omega(k)| <= gap(k)/(2 c_0) [certificate coordinate with radius >= c_0|tau|], plus the common
   peak shift (the "-d w" part);
 * block one-sided: (iii) peak deviations delta_k (relative to the common level), carried vector -(1/tau) sum_P lambda_k sigma_k delta_k u_k;
   (iv) off-peak coordinates with |tau Omega(k)| > gap(k)/(2c_0) (necessarily in the long direction up to O(eps) overshoot, by (K3));
 * peaks with margin mu_k >= eta ("robust") carry, by (K1) (sum_P lambda_k mu_k delta_k <= eps), at most sum lambda_k delta_k/|tau|
   <= eps/(eta |tau|) = O(|tau|/eta): they belong to the remainder; the genuinely one-sided peaks are the WEAK peaks, mu_k < eta.
## 3.3 Proposition (capacities). PROVED.
At scale tau, measured in units of g (i.e. as parts of B or of L*Omega), with eps = s(tau) - 1 <= tau^2/2:
 * remainder (free coordinates, paid usages, robust peaks): l_1 mass <= K(c_0, eta, f)|tau|;
 * one-sided base resources (i) near-contacts, (ii) near-flips: NO a priori bound (free, resp. almost free, at first order);
   they are scale-free resources and can carry O(1) at every scale;
 * peaks: for every mu_* > 0 the carried mass is <= eps/(mu_* |tau|) + (2 s(tau)/|tau|) sum_{k in P, mu_k < mu_*} lambda_k
   [from sum_P lambda_k mu_k delta_k <= eps, i.e. 3.1(K1), and delta_k <= 2 s(tau)]. Hence: robust peaks carry O(|tau|);
   under margin sparsity sum_{mu_k < s} lambda_k = o(s) (C_notes (MS)) all peaks together carry o(1); DEGENERATE peaks (mu_k = 0)
   and near-degenerate coarse peaks are scale-free one-sided resources (like contacts);
 * off-peak coordinates beyond their window: coordinate k carries lambda_k |Omega(k)| <= 2 s(tau) lambda_k/|tau|, and it is beyond the
   window only if gap(k) < 2 c_0 |tau Omega(k)| <= 4 c_0 s(tau). So at depth lambda_k >~ |tau| only near-threshold coordinates
   (gap(k) small) can be one-sided; coordinates with gaps bounded below are one-sided only at depth lambda_k <~ |tau| (Phi_m(k) <~ |tau|).
Summary: one-sided BLOCK resources at scale tau are (a) coordinates of depth Phi_m(k) <~ |tau| (any status), (b) near-threshold
coordinates (small gap or small margin) at any depth; one-sided BASE resources are contacts/near-contacts and near-flip coordinates.
[Proof: 3.1 (B1), (B2), (K1), (K3) and sum_k lambda_k < infinity.]

## 3.4 Lemma (transfer identity). PROVED.
Let t > 0 and let (B+, Omega+) be admissible at scale +t and (B-, Omega-) admissible at scale -t:
  f + t g = (a + t B+) + L*(w + t Omega+),   f - t g = (a - t B-) + L*(w - t Omega-).
Put D := B+ - B-, Omega_D := Omega- - Omega+. Then D = L* Omega_D and
  f = (a + (t/2) D) + L*(w - (t/2) Omega_D),   q*(a + (t/2)D) <= s(t),  N_m(w_m - (t/2)Omega_{D,m}) <= s(t).
*Proof.* B+ + L*Omega+ = g = B- + L*Omega-. Average the two decompositions (f + tg) and (f - tg); convexity of q* and N_m. QED.
So (D, Omega_D) is a "cheap zero-direction transfer": a decomposition of f itself at cost <= s(t), moving the functional
D = L*Omega_D from the blocks to the base. By A Lemma 8.6 (rotundity) a transfer with cost exactly 1 is trivial; cheap transfers
are the second-order flat directions of the decomposition set of f.

## 3.5 Proposition (sign opposition: the one-sided parts of the two sides ADD UP in the transfer). PROVED.
With the notation of 3.4 and paid usages bounded by 3.1:
 (a) contacts/near-contacts: free+ := sum_{K_{c_0}} (sign(z_j) B+_j)_+ and free- := sum_{K_{c_0}} (-sign(z_j) B-_j)_+ satisfy
     free+ + free- <= sum_{j in K_{c_0}} sign(z_j) D_j + 2 eps(t)/(q_0 t) <= ||D 1_{K_{c_0}}||_1 + t/q_0;
 (b) peaks: on P_m, sigma_k Omega_{D}(k) = (delta+_k + delta-_k)/t - (ell+ + ell- - 2M)/t: the transfer's peak profile is a common shift
     plus the SUM of the two sides' (nonnegative) deviations;
 (c) near-flip F-coordinates: if sign(B+_j) = sign(a_j) and sign(B-_j) = -sign(a_j) (cheap on both sides), then |D_j| = |B+_j| + |B-_j|;
 (d) off-peak k used beyond its window on both sides: the long direction is -sign w(k) for tau Omega, i.e. sign Omega+(k) = -sign w(k)
     and sign Omega-(k) = +sign w(k); hence |Omega_D(k)| = |Omega+(k)| + |Omega-(k)|.
*Proof.* (a) z-signed parts: sign(z_j)D_j = sign(z_j)B+_j - sign(z_j)B-_j >= (free+_j - paid+_j) + (free-_j - paid-_j); sum and use 3.1(B1)
(paid usages on K_{c_0} cost at least |t B_j| each). (b) sigma_k W+(k) = ell+ - delta+_k gives sigma_k Omega+(k) = (ell+ - M - delta+_k)/t,
and sigma_k W-(k) = ell- - delta-_k gives sigma_k Omega-(k) = -(ell- - M - delta-_k)/t; subtract. (c),(d): signs. QED.

## 3.6 Corollary (matching at scale, in its true form). PROVED.
For every g in C(f), t > 0 and admissible decompositions at +-t, the one-sided usages of the two sides (classes (i)-(iv)) are
bounded, resource class by resource class, by the one-sided mass of the transfer (D, Omega_D) plus O(t):
  [one-sided(+) + one-sided(-)] <= M_{c_0}(D, Omega_D) + K t,
where M_{c_0} counts sum_{K_{c_0}}|D_j|, the out-of-window F-mass of D, the peak deviation mass sum_P lambda_k|sigma_k Omega_D(k) - common|,
and the beyond-window off-peak mass of Omega_D. Consequently:
 (1) if f admits no cheap transfer with large one-sided mass at scale t ("bounded transfer capacity": sup M_{c_0} over cheap
     transfers at scale t is <= K' t for all small t), then every mate is, at every small scale and on BOTH sides,
     "window + O(t)";
 (2) a defect mate whose decompositions are not "window + O(t)" on either side forces cheap transfers with one-sided mass >> t at
     arbitrarily small scales ("resonance").
(Boundary effects between "window" and "one-sided" are absorbed by using nested thresholds, e.g. windows |tau Omega(k)| <= gap(k)/(2c_0)
and one-sided usage beyond gap(k)/c_0, similarly for F; the domination then holds up to a factor 2 and the O(t) remainder.)
The "matching" requested in the task (one-sided parts agree modulo two-sided resources up to O(t)) is AUTOMATIC: it is the
identity B+ + L*Omega+ = B- + L*Omega-. What does NOT follow is that the matched one-sided parts are small: by 3.5 they are
dominated by the transfer, and cheap transfers with O(1) one-sided mass exist (Theorem 2.4: the exact resonance v = L*D,
v z-signed on an infinite contact set). Y cap c_00 = {0} kills resonances whose base part is FINITELY supported (A Prop 7.4);
it says nothing about infinitely supported contact vectors in Y, nor about approximate block-block relations at scale.

## 3.7 Theorem (exact description of the defect at block-tame first rows). PROVED.
Assume F = supp a is finite and every Q_m (m in I) is finite. Then S(f) is finite dimensional, the map c -> g_c from
certificate data (b in l_1(F) cap zhat-perp, omega_m in R^{Q_m}) to S(f) is injective, and
  cl Cert^sh(f) = Cert^sh(f) = { g_c in C(f) : Hhat(c) <= 1 },   Hhat(c) := min_theta H^sh(c, theta)  (A Def 4.15),
  Def(f) = ( C(f) \ S(f) )  disjoint union  { g_c in C(f) : Hhat(c) > 1 }.
The first piece ("first-order / switching defect") consists of mates that are not certificate directions at all; the second
("second-order / rebalancing defect") of certificate directions that are mates but whose shifted coefficient exceeds 1.
*Proof.* Injectivity: if g_c = 0 then b = -L*(omega - d w) is in Y cap c_00 = {0}, so b = 0 and (T injective) omega_m - d_m w_m = 0;
on a peak this gives d_m = 0, hence omega_m = 0. Closedness: if g_{c_n} -> g_c in the finite-dimensional S(f) with H^sh(c_n, theta_n) <= 1,
then c_n -> c, and theta_n is bounded: max_m(H_m + 2 theta_m) <= 1 gives theta_{n,m} <= 1/2, and h(b) - 2 sum_m theta_m |zeta_m|/q_0 + 2 kappa_q <= 1
with kappa_q >= 0 gives sum_m theta_m|zeta_m| >= -q_0/2, hence a lower bound for each theta_{n,m}. H^sh is continuous in (c, theta)
(v_theta = sum theta_m R_m* w_m ranges in a finite-dimensional subspace of l_1, kappa_q is 1-Lipschitz in l_1), so a limit point theta
gives H^sh(c, theta) <= 1, and C(f) is closed. The minimum defining Hhat is attained by the same compactness. All other known
classes are contained in cl Cert(f) or in cl Cert^sh(f) (part 1, Lemma 1.2, and A Thms 6.2, 6.5, 6.8, D Thm 11.6 via A Thm 6.5). QED.
Remark. At the example of part 2, S(f) = R u and the first piece is infinite dimensional. Whether the second piece can be
nonempty in a Martin-type space is OPEN (the referee's finite-model computations, A_referee §4 e3_gauge, show true local
coefficient < H^sh in all seeds and H^sh(normalized mate) > 1 in 3 of 14 seeds, suggesting that it can).

## 3.8 Corollary (C-tame first rows: the switching defect is empty). PROVED modulo C_notes Thm 6.4, Prop 6.5, Lemma 5.2
## (Round 1, unrefereed; the parts used are re-derived below).
Assume f is C-tame: a in c_00, K finite, Qbar_m := Q_m cup Dg_m finite (Dg_m = degenerate peaks, alpha_{m,k} = 0), and margin sparsity
(MS) sum_{k in P_m, 0 < mu_k < s} Phi_m(k) = o(s). Then C(f) is contained in S(f); hence (3.7) Def(f) = { g_c in C(f) : Hhat(c) > 1 }:
at C-tame points only the second-order (rebalancing) defect can occur.
*Proof.* By C Thm 6.4, every g in C(f) has a unique representation g = b + sum_m R_m*(omega_m + c_m w_m), supp b in F cup K,
supp omega_m in Qbar_m, and by C Prop 6.5, b(xi) = 0 and c_m = -d_m when omega_m lives on Q_m. It remains to kill b on K and omega_m on Dg_m.
Primal test (C Lemma 2.2): g in C(f) iff xi(g) = 0 and nu(g)^2 <= phi(nu)(2 + phi(nu)) for nu in ker f, phi(nu) = p**(xi + nu) - 1.
Let J := N \ (F cup K) and psi_i the (finitely many) restrictions to J of u_{k,m} (k in Qbar_m) and R_m* w_m; they are linearly independent
on c_00(J) (Y cap c_00 = {0}, T injective; C §1.4 (F5)).
 (a) j in K: put nu := -z_j e_j + nu_J with nu_J in c_00(J) such that psi_i(nu) = 0 for all i (possible by independence). For s > 0 small,
     xi + s nu moves the contact j inward (|z_j - s/q_0| < 1) and finitely many free coordinates slightly: q**(xi + s nu) = q_0 and a(nu) = 0,
     so the base excess vanishes; in each block R_m nu vanishes on Qbar_m and has zero peak sum (w_m(R_m nu) = R_m* w_m(nu) = 0), so by the
     overshoot bound (C Lemma 5.2) E_m(s R_m nu) <= 2 m s q(nu) sum_{k in P_m : 0 < mu_k < s q(nu)} Phi_m(k) = o(s^2) (MS; degenerate peaks
     carry no u-component of nu, since u_{k,m}(nu) = 0 for k in Dg). Also f(nu) = 0. Hence phi(s nu) = o(s^2), and the mate inequality gives
     nu(g) = 0. But nu(g) = b(nu) + sum (omega + c w)-terms = -z_j b_j (all u_{k,m}, k in Qbar, and R_m* w_m vanish at nu; b vanishes on J).
     So b_j = 0.
 (b) k in Dg_m: choose nu in c_00(J) with u_{k,m}(nu) = sigma_k := sign w_m(k), and with all OTHER functionals of the finite list vanishing at nu
     (u_{k',m'}(nu) = 0 for k' in Qbar_{m'}, (k',m') != (k,m), and R_{m'}* w_{m'}(nu) = 0 for all m'; possible by independence). Then R_m nu
     vanishes on Qbar_m \ {k}, has zero peak sum (w_m(R_m nu) = R_m* w_m(nu) = 0 and R_m nu vanishes on Q_m), and its k-th entry
     lambda_k sigma_k moves the degenerate peak OUTWARD for s > 0: in the overshoot bound (C Lemma 5.2) the term 2(-sigma_k s (R_m nu)_k - |zeta||alpha_k|)_+
     is 0 (alpha_k = 0, sigma_k s (R_m nu)_k > 0), the other degenerate peaks do not move, and the non-degenerate peaks contribute o(s^2)
     by (MS). The base excess vanishes (free coordinates only), the other blocks contribute o(s^2) as in (a), and f(nu) = 0. Hence
     phi(s nu) = o(s^2) for s > 0, so nu(g) = 0; but nu(g) = sum_{m'} <omega_{m'} + c_{m'} w_{m'}, R_{m'} nu> = lambda_k sigma_k omega_m(k). So omega_m(k) = 0.
Thus g = b + sum R_m*(omega_m - d_m w_m) with supp b in F, omega_m in c_00(Q_m): g in S(f). QED.
Remark. Together with Theorem 2.4 this locates the switching defect precisely: it needs infinitely many one-sided coordinates of the
base (contacts/near-flips) — exact resonance — or infinitely many near-threshold block coordinates — approximate resonance
(part 4); it is absent at C-tame points, where only the second-order defect {Hhat > 1} may survive (OPEN whether nonempty).
