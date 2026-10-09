# P2 referee — part 0: provenance and scope
The P2 notes exist in two versions: P2x_notes.md (439 lines, instance "P2x": three-regime theorem 5.1, clip/Bregman 2.1-2.4, mixed term 2.5-2.6,
Thm 3.5 (Delta d_m >= 0, (TC)), 4.1-4.4, 5.3-5.6, 6, 7) and P2_notes.md = P2A_notes.md (512 lines, the other instance "P2A": toolkit 1.1-1.7,
Thm 2.1 d-neutral with pulls, 3.1-3.5, 4.1-4.6). P2_notes.md was overwritten DURING this review (00:55:52) by the P2A version.
The claims assigned to this referee are those of P2x (they quote Thm 3.5, Bregman smallness, conversion cost identity, etc.).
Claims of P2A are checked where P2x relies on them (TC failure / far pulls, A_referee 5.4, 6.1).

## First pass on P2x Thm 3.5 (Delta d_m >= 0, (TC)) — line check done
Checked: Step 3 algebra (Omega'- - Omega'+ = omega_Delta - Delta d w once Delta d' = Delta d; b'- = b- - b+1_(N,inf) - beta a'),
first-order identities (Lemma 4.2 at f'), Step 4 (no sign change, Lemma 3.1/3.2), Step 5 base (kink-free on K cap [1,N]) and block
convexity (x = |sigma| Delta d >= 0 needed), Step 6 assembly ((1-2delta)/(1-delta/8) <= 1-delta). Lemma 1.4 slack inequality re-derived.
Bregman identity, exact form, Prop 2.3 (a)-(c) re-derived. Lemma 2.5 constant: true second-derivative bound of x/||x|| is 2/r^2 <= 8, remainder <= 4||h||^2 (their 6 is fine).
Minor: Step 5 uses Lemma 3.2 at |sigma~| <= tau_1/(1-x) slightly > tau_1 (constant fix). Converse of Fact C re-derived (correct).
4.2 subset-sum parenthetical is FALSE in general (Cantor-type reservoirs, e.g. |V(j)| ~ 3^{-j}); fix: continuous raising move + IVT (P2A) or choose s_1 along the Cantor set.
