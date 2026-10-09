# Z4 referee, part 5 (addition): degenerate swallowing-sign peaks -- a gap in Z4's sketch and free steering channels

## 5.1 Observation (PROVED): Z4's sketch 8.1 overlooks the theta-decomposition.
Theorem thm:engineered uses the AVERAGED data (b^theta, omega^theta) = ((b^+ + b^-)/2, (omega^+ + omega^-)/2) for 0 < |tau| <= s_1, for BOTH
signs of tau. At a used degenerate peak k (varsigma omega^+(k) <= 0 <= varsigma omega^-(k)), omega^theta(k) has no fixed inward sign, so for
one sign of tau the move tau rho omega^theta(k) is OUTWARD. Making k a strict non-peak of f' (Z4: "inward moves are free") is therefore not
enough: Lemma lem:block(d) at f' requires |tau rho omega^theta(k)| <= gap'(k)/2 for |tau| <= s_1. At f', for k notin P',
|w'(k)| = M'|u_k(xhat')|/(theta_hat' Phi_k) (threshold Lemma), so with mu'_k := q'_0(|u_k(xhat')| - theta_hat' Phi_k) < 0,
   gap'(k) = M' |mu'_k| / (q'_0 theta_hat' Phi_k).
Hence the requirement is |mu'_k| >= 2 rho s_1 q'_0 theta_hat' Phi_k |omega^theta(k)| / M': the steering must be QUANTITATIVE, of size
kappa_D s_1 with kappa_D proportional to max_{k in D} Phi_k |omega^theta(k)| (a fixed multiple of the switching through D). For the +/-
decompositions (|tau| > s_1) the moves are inward and need no radius, as Z4 says. FIX: steer to mu'_k <= -kappa_D s_1, kappa_D :=
4 rho q_0 theta_hat max_D Phi_k |omega^theta(k)| / M (at late stages q'_0, theta_hat', M' are within factor 2 of q_0, theta_hat, M).

## 5.2 Lemma (free steering channels; PROVED).
Let (b^±, omega^±) be side-admissible data (b^± = 0 off F ∪ K). In Definition def:engineered modify the approximant by
 (i) z'_j := z_j + s_1 A_j at finitely many FREE coordinates j (|z_j| < 1, j notin F ∪ K), with s_1|A_j| <= (1 - |z_j|)/2, and/or
 (ii) a'' := a'' + s_1 Delta, Delta in l_1(F) fixed, s_1||Delta||_1 <= a_min/4.
Then: f' is still norm attaining (finitely many coordinates of z' changed, z' in c_00, |z'| <= 1, z' = sign a' on supp a'); every bound of
Lemma lem:approxfacts, Lemma lem:F1, (E1)-(E5) holds with K_e enlarged by a constant depending only on (A_j), Delta; and Step 3 of the proof
of Theorem thm:engineered acquires NO new base excess: at a free j, B^diamond_j = rho(beta^diamond_j - c a'_j) = 0 because b^± and a' vanish
at j; on F no flip occurs (|a'_j| >= a_min/2 - s_1||Delta||, tau rho |beta_j| <= a_min/8).
Proof. (i) changes xhat' by s_1 A_j e_j, so |u(xhat'_new) - u(xhat'_old)| <= s_1 |A_j| |u(j)| <= s_1 |A_j| q*(u); (ii) changes e' by at most
2 s_1 ||U|| ||Delta||_1/nu (as in (E1)). Insert in the proofs of (E2)-(E5) and Lemma lem:F1. The base claims are read off Step 3. QED.
First-order effect on a used degenerate peak k (block m): d/ds_1 of varsigma_k u_k(xhat') - theta_hat' Phi_k equals
 varsigma_k [ sum_j A_j u_k(j) + <P^perp U* u_k, U* Delta>/nu ] - Phi_k (directional derivative of theta_hat_m), where u_k(j) = y_k(j)/n_k at
free target coordinates. (Z4's channel "tuning masses at far contacts" is a third, one-signed, channel.)

## 5.3 Extension of Corollary cor:D1 to inward degenerate-peak data (SKETCH, improves Z4 8.1).
Hypothesis (FS) for a finite set D of degenerate peaks used inwardly by the data: the first-order effects of the free channels of 5.2 on
(varsigma_k u_k(xhat') - theta_hat' Phi_k)_{k in D} span a subspace of R^D containing a strictly negative vector (both signs of A_j and
Delta are allowed, so this is a LINEAR condition; by Gordan's theorem it fails iff some nonzero lambda >= 0 annihilates all channel
effects). It holds e.g. if every k in D has a private free target coordinate (a j in supp y_k with |z_j| < 1 not in supp y_{k'} for the other
k' in D) and Phi_k is small compared with |y_k(j)|.
Sketch: choose the push so that the channel effect is <= -(K + kappa_D) s_1 on D, where K s_1 bounds the uncontrolled O(s_1) change of
mu'_k produced by window masses and truncation ((E2), (E3), Lemma lem:F1); then mu'_k <= -kappa_D s_1 on D. At f', every k in D is a strict
non-peak with gap'(k) >= 2 rho s_1 |omega^theta(k)| (5.1); (E4) extends to omega supported in Q ∪ D (at a degenerate peak of f,
Phi^2 w(k)/C = zeta(k)/sigma since alpha(k) = 0; at f', k notin P'); lin'_m = tau rho <omega, alpha'> = 0 on D; the block expansion of
Lemma lem:block(d) holds at f' for the +/- data (inward moves at D: |W(k)| <= (1 - d sigma)|w'(k)|) and for the theta data (radius by 5.1).
Steps 4-6 of Theorem thm:engineered are unchanged. Not all estimates have been rewritten: SKETCH.
Consequence (SKETCH): Theorem A'' holds without (H3) for rows where (FS) holds for every finite set of degenerate swallowing-sign swallowed
peaks (Lemma 8.1 of Z4 provides the window data; M_f counts only non-degenerate swallowing-sign peaks).
## 5.4 What stays OPEN in (E-a).
At maximal contact there are no free coordinates; the only free channel is Delta in l_1(F) (dimension <= |F|), while the window data may use
an unbounded number of degenerate swallowing-sign peaks; (FS) can then fail. Super-weak (positive but tiny margin) swallowing-sign peaks are
not affected by this addition (Z4 8.2, HEURISTIC). Both remain OPEN.
