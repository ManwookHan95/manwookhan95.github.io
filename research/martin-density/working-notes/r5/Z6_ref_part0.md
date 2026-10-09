# Z6 referee: part 0 (plan and reading log)

Reading done: BRIEFING, BRIEFING_R2 (ADDENDUM 4), martin_paper_summary, Z6_notes.md (full), note Sec. 1 (martintail OK),
Sec. 7 (two-piece data Def twopiece: omega^pm finitely supported in Q_m; Theorem engineered needs gamma_0 = least gap
on Omega_m > 0, automatic for finitely supported data on strict non-peaks; Cor D1: Delta d >= 0, kappa_w <= 1),
Sec. 8 up to Lemma budget.

Plan: check claims in order 2.1, 2.2, 2.3, 2.4, Lemma F/4.2, Theorem C, D'', 5.2, Theorem U, gap-rate, 5.5,
Prop P, Theorem V, Cor V.1, candidate 6.1, modules 6.2, module sums, candidate under D''.
Key risk points flagged at reading:
 (R-a) D'': Xi(l) contains H_comb(l); must be computable at stage l from data of index <= l only (targets y_{l''},
       u_{l''}(j) on T(l), signs); check that the Hoffman matrices do not involve c_{l+1} or later data.
 (R-b) Theorem U Hoffman system: rows on T_0 only; con rows on signature parts reduce to sgn rows only if
       z = eps_l on all of S_l \ (F u T_0) (exact swallowing); approximate swallowing NOT covered.
 (R-c) b_l := 12 lambda_l / t in the box rows: Hoffman constant independent of b, but the projection tau' must keep
       |tau'_l| <= 12 lambda_l/t to feed Lemma windowtwopiece; check.
 (R-d) Theorem U Step (3): 2.4 bound |tau_l| <= A/|q_l| for l in Sigma, then summed in V(t); 1/|q_l| <= 8N 2^{m+k}/c_l;
       design factor; check degree bookkeeping and that A itself contains only O(t) terms (A contains |Delta d| M,
       which needs (H2') pinned with design constants; but 2.2 uses lambda_l of the pair peaks and t/(sigma|alpha|) =
       t/(lambda mu) of the pair peak k_2: a MARGIN of a swallowing-type peak enters K_d!).
