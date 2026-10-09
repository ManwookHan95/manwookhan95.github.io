# P2 notes — engineered recovery of switching mates with one-sided resources (replication–averaging–transfer)

Round 2, task P2. Setting: canonical base q, Martín's norm with a FINITE block set I (p_N, any N; Remark martin-tail of Preprint B reduces p to
these); notation of A_notes §1, §4. Only Lemma B's conclusion is used about T. Imports (refereed): (T1)-(T4), A Facts A-F, A Lemmas 4.3, 4.4, 4.7,
7.1, 7.2, A Prop 4.5, A Thm 4.10/4.17/6.8, G_referee 4.7 (parametrization of NA approximants), N_part1 Thm 1 (g in Ls(f) iff (f, rho g) in cl NA for all rho<1).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

**Provenance (important).** Two P2 agents ran concurrently and wrote to the same directory. The file P2_part1.md (toolkit) and the files
P2_part2.md, P2_part3.md (d-neutral theorem, mixed term, garbage identity) are by the OTHER instance; my files are P2x_part2..5.md. This notes
file assembles my results in full (Sections 2-5) and summarises the other instance's main theorem (Section 6, with the step I re-checked); Section 7 answers the task's specific questions.
If a later P2_notes.md from the other instance replaces this file, my results remain in P2x_part2-5.md and P2x_notes.md (identical copy).

## 0. Summary

**Answer.** The one-sided-resource mates whose decompositions near t = 0 use only ROBUST structure — base contacts (with any splitting of the
contact mass between the two sides, contacts on both sides), near-contacts, finitely many FIXED off-peak block carriers (also pushed beyond their
gap at fixed scales) — are recovered along engineered NA approximants, by a three-regime scheme in which regime (ii) is an EXACT transfer of the
one-sided decompositions of f, regime (i) is one two-sided certificate created by window masses on the contacts, and regime (iii) is the slack.
Rigorous: two-piece mates with Delta d_m >= 0 in every block under a cone tuning condition (Theorem 3.5, several blocks); d-neutral two-piece
mates without any tuning condition for one block (other instance's Theorem, pulls). The obstruction is NOT the base mixed term (it is cancelled
by finitely many scalar tunings) but the BLOCK side: x -> J_V(Lx) moves off-peak values by ~ s/Phi_k under an O(s) change of the normer, which is
harmless for fixed carriers (only a Bregman pairing, o(s), enters at first order — new Lemma 2.3) and fatal, for every mass/conversion-based scheme,
for SCALE-DEPENDENT block carriers (weak peaks, super-near-threshold carriers, deep off-peak carriers) in the band [s, sqrt(s)] (Prop 5.4). C's implant
scale gap is confirmed quantitatively (conversion cost identity 5.3) but is not an obstruction to the scheme. Density remains OPEN; no
counterexample is claimed. The exact residual class is listed in 5.6.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Three-regime theorem (abstract replication–averaging–transfer; averaging over J geometric scales with error 4 kappa t^2/(2J)) | PROVED | 1.4, 1.5, 5.1 |
| 2 | Clip formula w(k) = M clip(u_k(y)/(theta Phi_k)); Bregman identity | PROVED | 2.1, 2.2 |
| 3 | Bregman smallness: excess of w at the perturbed point is o(A) (A = normer perturbation), although sum lambda_k|w'(k) - w(k)| = Theta(A) | PROVED (+numerics) | 2.3, 2.4 |
| 4 | Base mixed term delta t <P^perp U*e_j, P^perp U*B_t>/nu: exact form; cancelled by finitely many tunings (finitely many pieces) or up to eta (any bounded family, compactness of U*); NOT an obstruction | PROVED | 2.5, 2.6 |
| 5 | Uniform Hilbert remainders; block uniformity along engineered approximants | PROVED | 3.1, 3.2 |
| 6 | Brouwer tuning lemma for positively spanning moves | PROVED | 3.3 |
| 7 | **Main theorem: two-piece switching mates (any contact split, several blocks), Delta d_m >= 0 for all m, a in c_00, cone condition (TC): (f,g) in cl NA** | PROVED | 3.5 |
| 8 | Delta d_m < 0: convexity provably fails on one side; recovery iff pinning (PIN); pinning at block-tame blocks with robust window peaks | PROVED (failure) / SKETCH (pinning) | 4.1 |
| 9 | (TC) fails: far pulls; exact tuning unnecessary (approximate tuning to eps_0 s_1 suffices: removes the j* issue of P1 6.3) | SKETCH (one block, Delta d = 0: PROVED by the other instance / N2) | 4.2, 6 |
| 10 | a not in c_00; infinitely supported carriers with near-peak decay; degenerate-peak carriers | SKETCH | 4.3, 4.4 |
| 11 | Conversion cost identity (implant scale gap): a two-sided carrier of capacity t_cap created at a peak costs >= 2|c| t_cap in f' - f (absent cancellations) | PROVED (identity) / HEURISTIC (as obstruction) | 5.3 |
| 12 | Precision obstruction: scale-dependent block carriers cannot be transferred across [s, sqrt(s/eps_0)] by any mass/conversion scheme at scale s; averaging does not help | PROVED (for transferred decompositions) / HEURISTIC (as obstruction to recovery) | 5.4 |
| 13 | Classification of where regime (i) can be supplied; exact residual class (R1)-(R4) | PROVED classification of mechanisms / OPEN residual | 5.5, 5.6 |
| 14 | d-neutral two-piece mates (one block, no tuning hypothesis; several blocks under a span hypothesis (S)) — other instance | PROVED there (key step re-checked) | 6 |
| 15 | P1's explicit defect mates (P1 2.3, 6.2): recovered | PROVED (Thm 3.5 if (TC); otherwise other instance's theorem) | 3.6(4), 6 |
| 16 | Density of NA((c_0,p_N), l_2^2) | OPEN | 5.6 |

## 1. Toolkit (from P2_part1.md, re-checked; statements only, proofs there)
1.1 Clamp formula (= 2.1 below). 1.2 Convergence of block data along engineered approximants: if xhat_n = z'_n + U e_n -> zhat weak* and a_n -> a in l_1
with a_n(xhat_n) = 1 = q(xhat_n), then f_n := grad p(xhat_n) -> f in norm, w_{n,m}(k) -> w_m(k), C_{n,m} -> C_m, M_{n,m} -> M_m, D_m w_{n,m} -> D_m w_m in l_2,
R_m* w_{n,m} -> R_m* w_m in l_1 (G_referee 4.7). 1.3 At an NA point with g'(xhat') = 0 and block parts omega - d'w' (omega off-peak), the base part B has
B(xhat') = 0 and q*(a' + tau B) = 1 + Fl' + Kink' + nu'Psi'. 1.4 Assembly: if p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta) on 0 < |tau| <= T_0 with T_0^2 <= 3delta,
p*(f' - f) <= (1-rho^2)T_0^2/6 and p*(g' - rho g) <= (1-rho^2)T_0/6, then g' in C(f') (proof: 1 + x/2 - x^2/8 <= sqrt(1+x); A Lemma 4.7 slack).
1.5 Averaging: with s_j = s_1 2^{1-j}, (i) p*(f' + t h_j) <= 1 + Qt^2/2 on |t| <= s_j, (ii) p*(f' + t gbar) <= 1 + Qt^2/2 on [s_J, T_0], (iii) p*(h_j - gbar) <= kappa s_j imply
p*(f' + t g') <= 1 + (Q + 4kappa/J)t^2/2 on |t| <= T_0 for g' = (1/J) sum h_j (convexity; sum_{s_j < |t|} s_j <= 2|t|). 1.6 Two-piece data: b+-, omega+-_m (finitely
supported, off-peak), d+-_m = <D w_m, D omega+-_m>/C_m, g = b+ + sum R_m*(omega+_m - d+_m w_m) = b- + sum R_m*(omega-_m - d-_m w_m), supp b+- in F u K,
z_j b+_j >= 0 >= z_j b-_j on K; omega_Delta := omega- - omega+, Delta d_m := d-_m - d+_m, v := b+ - b- = sum_m R_m*(omega_Delta,m - Delta d_m w_m); b+-(zhat) = 0.
1.7 One-sided admissibility (with s(tau)) implies all second-order coefficients <= 1.
