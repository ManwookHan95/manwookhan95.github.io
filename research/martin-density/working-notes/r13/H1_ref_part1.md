# H1-ref part 1: Lemma 2.2 (stratified projected flow), Proposition J1.11 (first-order Puiseux margin), Corollary 2.4

Sources re-read: r13/H1_part1.md, H1_notes.md 2; r9/X1_notes.md 2.2-2.6, r9/X1_ref_notes.md 3.4, 4 (D1), 5-8 (NLM, GEN, QC, KN^tr, KN-1);
r11/cert0_report 3.4; r12/J1_notes 7.1, J1_ref_notes B.4, E (J1.15').

## 1.1 Lemma 2.2 (stratified projected flow).  Verdict: CORRECT.
Re-derivation.  Fix a finite stratification of the compact semialgebraic set Z into connected Nash submanifolds with the frontier
condition and Whitney (a) (existence: BCR 9.7.11 gives Whitney (b), hence (a); the frontier condition can be imposed simultaneously,
van den Dries-Miller 4.8 / Loi).  Let r_* in S, 0 != v in T_{r_*} S, eps in (0,1).
 (i) Only strata S' with r_* in cl(S') meet a small ball B(r_*, 2 delta) (finitely many strata, the others are at positive distance).
     For such S' != S: S meets cl(S'), so by the frontier condition S ⊂ cl(S') \ S' and dim S < dim S'.  If points x_n in S', x_n -> r_*,
     had dist(v, T_{x_n} S') > eps|v|, a subsequence of T_{x_n} S' converges in the (compact) Grassmannian of dim S'-planes to some tau, and
     Whitney (a) for (S', S) at r_* gives T_{r_*} S ⊂ tau, so dist(v, T_{x_n} S') -> dist(v, tau) = 0: contradiction.  For S' = S use the
     continuity of the tangent bundle.  Hence, for delta small, dist(v, T_x S') <= eps|v| on S' ∩ B(r_*, 2 delta) for every S'.
 (ii) V_{S'}(x) := P_{T_x S'} v is a smooth tangent field on S' with |V_{S'}| <= |v| EVERYWHERE (orthogonal projection), so integral
     curves are |v|-Lipschitz.  A maximal integral curve that stops at a finite time tau_max converges (Cauchy) to some x_1 in cl(S'); if
     x_1 were in S', a compact neighbourhood of x_1 in S' would contain the curve near tau_max, contradicting the escape lemma.  So x_1 in
     cl(S') \ S', hence in a stratum S'' with dim S'' < dim S' (frontier condition).
 (iii) Concatenation from y (|y - r_*| < delta) with budget t <= delta/(2|v|): every point of the curve satisfies |gamma(s) - y| <= |v| s <=
     delta/2, so the curve stays in B(r_*, 3 delta/2), where (i) applies to every stratum it visits; dimensions strictly drop at each
     junction (at most dim Z + 1 pieces); no point stratum other than {r_*} = S could be visited, and S itself is not a point stratum
     (v != 0); the flow in S cannot exit S inside the ball (an exit point would lie in a stratum S'' meeting the ball, so r_* in cl(S''),
     S ⊂ cl(S''), dim S < dim S'', contradicting dim S'' < dim S).  The concatenation is Lipschitz, lies in Z, |gamma'| <= |v| and
     |gamma' - v| <= eps|v| a.e.
Remark.  The proof needs only Whitney (a) and the frontier condition; no reach or curvature bound.  This is exactly the missing uniformity
step of J1 7.1 / J1-ref B.4.

## 1.2 Proposition J1.11 (first-order Puiseux margin).  Verdict: CORRECT.
Checked line by line:
 - Lemma 2.1 (regular contact points): if Phi notin B^reg and r_* in Lambda = Z ∩ {F_Phi = 1}, D = {d : psi_d(r_*) = Phi_d}, then
   d Psi_{D,S}(r_*) is onto (else Phi_D is a critical value of Psi_{D,S}); v in T_{r_*} S with d psi_d(r_*) v = -Phi_d (d in D).  Correct.
   dim B^reg < n = |N_T|: each cylinder {Phi : Phi_D in CV_{D,S}} has dimension <= dim CV_{D,S} + (n - |D|) < n (semialgebraic Sard).
 - Local decrease: psi_d (d in D) is real analytic near r_* (r_{*,d} != 0; the radicand sigma + sigma(sigma - 1)R^2 of K is > 0 and 1 - R^2
   >= sigma_rob/4 on K_kappa); the integral estimate gives psi_d(gamma(t)) - psi_d(y) <= -(3/4) t Phi_d; for d notin D continuity gives
   psi_d/Phi_d <= 1 - 2 m_* on B(r_*, 2 delta).  Hence F(gamma(t)) <= max(F(y) - 3t/4, 1 - 2 m_*).  Correct.
 - Covering: Lambda compact; on Y_1 \ U (compact) F <= 1 - m_U; for r in Y_1 ∩ B(r_*^i, delta_i) and t = h/(2|v_i|), gamma(t) in Z,
   |gamma(t) - r| <= h/2 < h, F(gamma(t)) <= 1 - min(3h/(8|v_i|), 2 m_*^i).  So mu(h) >= 3h/(8V) for h <= h_0.  Correct.
 - Genericity: "mu_Phi(h) >= c h on (0, h_0]" is first-order (max of the usc G_h over the compact Y_1 is attained, so it reads: for every
   r in Y_1 and e > 0 there is r'' in Z, |r'' - r| < h, F_Phi(r'') < 1 - ch + e), with parameters in k (Z_kappa, K_kappa, sigma_rob, and K
   -- which satisfies (1 - R^2)k^2 - 2 sigma k + sigma^2 - sigma = 0 -- are defined over k); quantifier elimination over real closed
   fields keeps the parameters, so B^lin is k-semialgebraic; B^lin ⊂ B^reg gives dim B^lin < n; GEN (X1-ref 6, cert1 4) gives
   Phi^T notin B^lin.  The stratification need not be defined over k.  Correct.
Precisions (do not change the conclusion):
 PJ-1 (option (b)).  GEN needs the N_T weights algebraically independent over k_0(other weights).  This holds under option (a) of T_fin
      (all c_l transcendental, the setting of the goal statement).  Under option (b) (c_1 = 1) the carrier-1 exception of X1-ref W2 remains:
      J1.11 is then proved for every pattern not containing carrier 1 in N_T.  H1 should state "option (a), or patterns with 1 notin N_T".
 PJ-2 (constants).  Remark (4) ("Design(L) >= max(1/c_kappa, 1/h_kappa)") is cert1's P-CHOICE applied to the linear constants; if the QC
      constants were defined through the Puiseux leading term c h^{p/q}, then p/q <= 1 and mu >= c_kappa h^{p/q} >= c_kappa h for h <= 1,
      so either convention gives mu_kappa(eta'/3) >= eta'/(3 Design(L)).  Fine.
 PJ-3 (exponent exactly 1).  Remark (3) uses cert1 Q1 (mu <= Lip h when Lambda != {}): correct.
Numerics: H1's puiseux_toy/puiseux_toyA_fine were re-run conceptually (not needed for the proof; the cusp toy illustrates that genericity is
necessary: exponent 3/2 at a critical tip).  I accept them as illustrations only.

## 1.3 Corollary 2.4 ((R-T) is empty).  Verdict: CORRECT (mod chain), one remark downgraded to an inspection claim.
(J-e) of J1.15' asks mu_kappa(eta'/3) >= C D^C m^2 (beta_*/kappa_m)^2 for a band of half-width beta_* on a KN-1 row of a (T)-block: the band
moves R^2 by <= m^2 (beta_*/kappa_m)^2 (target 0), hence every active near-threshold status by <= (m|r_d|/Phi_d)(dK/dR^2) m^2 (beta_*/kappa)^2
<= C D^C m^2 (beta_*/kappa)^2 (Lemma K, dK/dR^2 <= C D^C), which must be <= mu/4.  Without far placements ||b|| <= |Lambda_A|^{1/2} x, so
beta_* = 16 nu_1(||b|| + 2 rho_0)/(c_* u) <= Design^C x/u (1/c_*, nu_1, |Lambda_A|, 1/kappa_m, m, D <= Design^C for L >= l_f), and the right
side is <= Design^{C'} eta'^2/u^2 with C' absolute.  J1.11 + P-CHOICE: the left side is >= eta'/(3 Design).  Since eta' = T^4/(L Design) and T
<= (u/(4 Design))^{L^2+20}, eta' <= u^2/(3 Design^{C'+1}) once 4L^2 + 80 >= C' + 3 (true for L >= l_f).  Hence (J-e) holds at every main stage
L >= l_f and J1.15' realizes every stage at which some thick-type carrier is KN-1 in a (T)-block: (R-T) is EMPTY.  Correct.
Remark (b) (KN-1 relaxed to |value| <= kappa_m (mu/(C D^C m^2))^{1/2}, >= eta'^{1/2}/Design^C >> beta_*): correct by the same estimate.
Remark (c) ("nothing else in the chain used the exactness"): this is an INSPECTION claim.  It agrees with the two places that introduced the
exact hold -- X1-ref 8 "KN-1 (why the exact hold is necessary)" (the only reason given is the non-explicit exponent beta > 4) and Q1-refb F5
(P-HOLD: the non-explicit margin survives only because there is no second-order value perturbation) -- and I found no other use in X1-ref 8,
cert0 3.1-3.5 or K2 5.2 (K2.9(c) lists "exact KN-1 zeros" only as an output of K1.6(A)).  Label: PROVED by inspection of these sources; the
relaxation is not needed for any H1 result (H1 uses only (J-e)).
