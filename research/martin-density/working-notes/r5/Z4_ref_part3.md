# Z4 referee, part 3: Section 5 (maximal contact, rigidity), Lemma 6.1, part 8, summaries; referee improvement (H2'')

## Lemma 5.0: CORRECT (q**(zhat) = 1 gives y with y(zhat) > 3/4; tails of (u_{k,m})_k dense; threshold Lemma). Note: the argument
works at EVERY f (not only maximal contact): every block has infinitely many peaks of each sign with margin >= q_0/4.
## Prop 5.1: CORRECT. v = b^+ - b^- = sum R^*(delta omega - Delta d w); delta-omega terms vanish on S_{l^±} \ T_omega; the rest is
<= (2/9) 2^{-2s} c delta per block by allowedness (b); dominant term -Delta d_m lambda (±M) v(s) forces opposite signs at l^+, l^-.
## Prop 5.6: CORRECT (constant (2/5) is conservative; (18/5) would do). Consequence: two-piece data with Delta d_m != 0 exist only under
"peak-aligned swallowing" of the far parts of ALL peak signature sets of block m with z_s = -sign(Delta d_m) sign(w_m(k(l))). Valuable.
## Prop 5.2: CORRECT. Lemma 5.3: CORRECT for designs with the clause for large l (only large l are used). Bound M_f <= 2l Lambda°/q_0 +
M^canc + const (1/delta°_{l'} <= Lambda°(l)/2).
## Corollary 5.4: CORRECT for SLD_G (with the clause). Two small imprecisions: (i) the stated growth condition drops a factor l^2 coming from
(l + M^canc/Lambda°)^2; harmless because Step 8 really needs only C' Xi_f <= (l 2^{l^3})^6 Lambda°^4 G*^2 and Lambda°(l) >= 3^l.
(ii) "For the original SLD the same holds": NOT justified as stated, because Lemma 5.3 needs the clause c_l <= (delta_l||h_l||_1)^2,
which the original recursion does not imply (c_{l+1} <= T_lo(l)^3 is controlled by delta°_l, not by delta°_{l+1}, and delta°_{l+1}
depends on min S_{l+1}, which Definition def:SLD leaves free). For the original SLD state the condition with M_f in place of M^canc.
## Remark 5.5(i): CORRECT asymptotically (T_lo(l-1)^3 <= 2^{-3(l-1)2^{(l-1)^3}} = o((l 2^{l^3})^{-3})). (ii) is descriptive.
## Lemma 6.1: CORRECT (c_flat enters only through I_r and Q at fixed j).
## 6.2/6.3: HEURISTIC parts correctly labelled. INACCURACY in 6.3(d): "finitely swallowed rows ... stay open only when (H3) or (H2')
fails" omits the room condition (W*) for the GOOD signature sets (approximate swallowing (E-e) = (O1)(i)); Corollary 4.2(b) needs (W*).
The note itself says "open in case (O1)". Correct statement: finitely swallowed rows are in R under (H2'), (H3), (W*); open otherwise.
The "Hence a proof ... must ..." sentence after Prop 1.3 is interpretive (HEURISTIC), not part of what is PROVED.
## Lemma 8.1: CORRECT. lin_m vanishes because alpha_m = 0 at degenerate peaks and omega = 0 at non-degenerate peaks; inward moves keep
||W||_inf = (1-dr)M (attained at a non-degenerate peak, which exists since ||alpha||_1 = 1) as long as |r omega(k)| <= 2(1-dr)M; the
rebalancing (Lemma lem:TV) only needs ||W - w||_inf small. Window data without (H3): checked (varsigma omega^+ <= 0 <= varsigma omega^-,
discrepancy (|omega_+(k)| - tau'/lambda)_+ <= (tau - tau')_+/lambda + |Delta d M| since |omega_+(k)| <= e_k = tau/lambda - Delta d M).
d-rows must now include the degenerate swallowing-sign peaks with q_l = Phi M/(mC) != 0; the repair (DR) handles them. CORRECT.
## Engineering with degenerate peaks: SKETCH, plausible, correctly labelled. Re-derived the obstruction: at f' with mu'_k > 0 the inward
move does not raise ||W||_inf but splits as lin = -alpha'(k) r|omega(k)| and G = +alpha'(k) r|omega(k)|; after rebalancing the common
level contains sigma alpha'(k) r |omega(k)| = mu'_k r lambda_k |omega(k)| = O(s_1)|r| x (switching through k), which is not
<= delta r^2/16 for |r| just above s_1. Steering to mu'_k < 0 makes the move free (inward moves at strict non-peaks need no radius).
Tuning masses at far contacts j outside supp b^± do not create base excess (no flips: B_j = -rho c a'_j) and move mu'_k at rate
V_j(k) = varsigma_k[<P^perp U* u_k, U* e_j> z_j/nu - Phi_k d(theta_hat)/dm]; ||U* e_j|| -> 0, so only finitely many fixed j matter.
Steerability (a strictly negative vector in cone{V_j}) is an f-dependent hypothesis. Verdict: plausible SKETCH; not checked in detail.

## REFEREE IMPROVEMENT (PROVED): the uniform shift can also be pinned through the d-identity (weakening (H2')).
By eq:didentity and q_l tau_l = -Phi_m(k(l)) w_m(k(l)) Delta theta_l/(mC_m) for l in B,
   Delta d_m M_m = (1/(mC_m)) sum_{good l, m(l)=m} Phi w Delta theta_l - sum_{l in B, m(l)=m} q_l tau_l + r_m,  |r_m| <= 2t/sigma_m.
In the setting of Theorem A (Steps 1-3 before the shift is used): |good sum| <= K* t/(mC_m); for l in U, (tau_l)_- <= |tau_l - tau°_l|,
sum <= D; for swallowed l notin U, sum |q_l tau_l| <= 6t/C_m + 6t^2/C_m (Step 5). Hence:
 (UP) if q_l >= 0 for every swallowed carrier of block m, then Delta d_m M_m <= K* t/(mC) + D/C_m + 12t/C_m + 2t/sigma_m = O(K_1 t);
 (LO) if q_l <= 0 for every swallowed carrier of block m, then Delta d_m M_m >= -O(K_1 t).
(Numerical sign check: Z4_ref_work/didentity_toy.py, seeds 3, 5, 11: |r|/(2t/sigma) <= 0.08, bound never violated.)
So (H2') can be replaced by
 (H2'') for every block m: [LOWER] a non-degenerate peak which is good or swallowed with swallowing sign, OR q_l <= 0 for all swallowed
        carriers of block m; and [UPPER] a peak which is good (degeneracy allowed, see part 2) or swallowed with anti sign, OR q_l >= 0 for
        all swallowed carriers of block m.
Since every block has infinitely many non-degenerate peaks of each sign (Lemma 5.0 at any f), (H2'') fails only if some block either
(i) has all its peaks swallowed with swallowing sign and some swallowed strict non-peak with q_l < 0 (anti-aligned non-peak), or (ii) has
all its non-degenerate peaks swallowed with anti sign and some swallowed carrier with q_l > 0 (a swallowing-sign strict non-peak, or a
degenerate swallowing-sign peak). Example: "self-aligned" rows, z = sign(y_l(zhat)) on every S_l \ F (constructible recursively in l:
y_l(zhat) depends on z only on supp y_l, which meets only coarser S_{l'} (allowedness (a)), F and coordinates outside all S_l; for large l
the signature lift has the same sign, so sign u_l(zhat) = eps_l). There every swallowed carrier has q_l >= 0: (H2') fails (no good and no
anti-sign peaks), (H2'') holds. CAVEAT: if such a row has only finitely many strict non-peaks and no degenerate peaks it is a (BT) point
(with the clause c_l <= (delta_l||h_l||_1)^2 the margins are >= q_0 delta°_l/4 for large l and (MS) follows), so it is new only when it has
infinitely many strict non-peaks; then (DR) needs these to be d-neutral (q_l = 0) or (E-d) occurs. (H2'') is a small but genuine gain.
