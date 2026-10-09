# N2 notes — Engineered recovery of resonant switching mates (exact and approximate resonances)

Round 2, task N2. Setting: canonical base q, Martin's norm with a FINITE block set I (p_N, any N; Preprint B Remark martin-tail);
"admissible T" = Lemma B's conclusion only. Imports (refereed): A_notes Facts A-F, Lemmas 4.3, 4.4, Prop 4.5, Lemmas 4.6, 4.7, 7.1, 7.2;
N_part1 Thm 1 / Lemma 1.2 / Prop 1.5 (Ls(f): g in Ls(f) iff (f, rho g) in cl NA for all rho < 1; one sequence per mate suffices);
P1 §2, §6.1-6.2 (example); E Lemma 6.1/Cor 6.2, Prop 8.2; R1 of P1_referee (mod C Thm 6.2/Prop 6.5). Part files: N2_part1.md ... N2_part5.md
(this file assembles them). Scripts: N2_work/thm1_check.py, N2_work/lemma32_check.py.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 0. Answer and summary
**Exact resonances are recovered by engineering, rigorously, whenever Delta d >= 0 (with a mild tuning condition if Delta d > 0);
for Delta d < 0 the recovery reduces to one explicit pinning condition; approximate resonances reduce to a conversion/implant
capacity. No configuration was found where engineering provably fails, so no counterexample is claimed.**
 1. Theorem 1 (PROVED): every mate g in C(f) (F = supp a finite) with an EXACT two-piece representation — admissible one-sided linear
    decompositions on the two sides whose base parts live on F cup K with the contact signs, block parts on finitely many strict
    non-peaks of one block, equal d-coefficients (Delta d = 0) — lies in Ls(f). The proof is P1 6.3's construction made rigorous and
    general: window masses on the contacts, far sign-flipped contacts with negative masses (free pulls), a continuous tuning MASS fixed by
    the intermediate value theorem (replacing P1's partial-pull coordinate, referee gap G2), an arbitrary constant-theta tail, explicit
    quantifier order (G3), g in C(f) used only in the slack regime (G1). Corollary 2.5: P1's explicit defect (Thm 2.4 of P1) and the whole
    slab of P1 6.2 are recovered.
 2. The d-coefficient issue (E_referee 3.1): a rigorous convexity lemma (1.3) shows the "c-trick" for tau c <= 0 costs NOTHING at first order;
    hence Delta d > 0 is recovered (Thm 2) under (TT) two-sided mass tuning, in general under a scalar Bregman condition (BR). For Delta d < 0
    one side necessarily has tau c > 0, and then (Lemmas 3.2(b), 3.3, PROVED) the block cost is >= 1 + 2M|s|: unavoidable common peaks of
    opposite sign exist at EVERY NA approximant of a non-NA f. So for Delta d < 0 the mismatch Delta d R*(w' - w) must sit in the base; Thm 3
    (PROVED, conditional) recovers g under the pinning condition (PC): its kink on near free coordinates is o(t_n).
 3. The C_referee kink class (infinitely many kinks, Gamma_2 < Gamma_w) is IDENTICAL to exact resonances with Delta d = -(s+ - s-) c'/M (1.6, 3.9):
    no new mechanism; c' < 0 / c' = 0 covered, c' > 0 is the Delta d < 0 case.
 4. Delta d < 0 mates exist (P1-type T with u_{2,1} := (h - kappa' pi)/n, 3.8, SKETCH); in block-tame carrier blocks with robust peaks the
    pinning conditions collapse to the single tuned scalar v(x') = 0 (exact identity, 3.7(a)) and (PC) holds up to a perturbation lemma
    (SKETCH); in the generic case (infinitely many strict non-peaks) (PC) is a quantitative tail-independence property: OPEN.
 5. Approximate resonances: Theorem 4 (PROVED, conditional) — recovery holds as soon as the approximant supplies J(rho) ~ 16 kappa/(1-rho^2)
    two-sided carriers with frozen errors O(scale) at adjacent scales below the destruction boundary plus the transport (HT). Prop 5.2
    (PROVED mod R1): along C-tame approximants the FREE-coordinate part of a recovered mate must be carried by off-peak block coordinates of the
    approximants — base engineering cannot help there; this is why conversion capacity is decisive for approximate resonances and irrelevant
    for exact ones. Far rigidity (E (A2)) is compatible with Lemma B (4.5, SKETCH), so Lemma B alone does not give unbounded conversion
    capacity; but implanted/generic carriers are not excluded and no N&S property of T is identified (OPEN).
 6. Item 3: no configuration with provable non-recovery; dist((f, rho g), NA) > 0 is not claimed for any example.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Algebra of exact two-piece representations (b+-(zhat)=0; v in Y, z-signed on K, infinite support; Delta d = ell(xi)/|zeta|; v=0 => Cert) | PROVED | 1.2 |
| 2 | Convex block lemma (c-trick with tau c <= 0 is free) | PROVED | 1.3 |
| 3 | Base excess bound at an NA point; convergence of engineered approximants | PROVED | 1.4, 1.5 |
| 4 | C_referee kink re-splitting = exact resonance with Delta d = -(s+-s-)c'/M | PROVED | 1.6, 3.9 |
| 5 | **Theorem 1**: exact two-piece mates with Delta d = 0 (one active block) are in Ls(f) | PROVED | 2.3 |
| 6 | Corollary: P1's example — slab of 6.2 and all g_{K1} recovered (P1 6.3 made rigorous, gaps G1-G3 fixed) | PROVED | 2.5 |
| 7 | All of C(f) at P1's example recovered | OPEN (needs second-order rebalancing at engineered approximants) | 2.5 Rem |
| 8 | Several active blocks, Delta d_m = 0, rank condition | SKETCH (tuning step) | 2.6 |
| 9 | General mismatch identity with c+- and Bregman excess | PROVED | 3.1 |
| 10 | Wrong-sign c costs >= 2M|s|; common opposite peaks exist at every NA approximant of a non-NA f | PROVED (+numerics) | 3.2, 3.3 |
| 11 | Delta d < 0: convexity mechanism impossible on one side | PROVED | 3.4 |
| 12 | **Theorem 2**: Delta d > 0 recovered under (BR); (TT) => (BR) | PROVED | 3.5 |
| 13 | Delta d > 0 without (TT) | SKETCH (far-tail comparison, T-dependent) | 3.5 |
| 14 | **Theorem 3**: Delta d < 0 recovered under (PC) | PROVED (conditional) | 3.6 |
| 15 | (PC) for block-tame robust carrier blocks | SKETCH | 3.7(a),(b) |
| 16 | (PC) in the generic case (infinitely many strict non-peaks) | OPEN | 3.7(c) |
| 17 | Existence of Delta d < 0 exact two-piece mates | SKETCH | 3.8 |
| 18 | Cross-block exact relations = exact resonances (two active blocks) | PROVED (reduction) | 4.2 |
| 19 | **Theorem 4**: conditional recovery through converted/implanted carriers (averaging at f') | PROVED (conditional) | 4.3 |
| 20 | Transport hypothesis (HT) for approximate resonances | HEURISTIC | 4.3 |
| 21 | Far rigidity compatible with Lemma B | SKETCH | 4.5 |
| 22 | Full rigid design (A1)-(A5) + blocking (C1)-(C3) consistent with Lemma B? | OPEN | 4.6 |
| 23 | N&S property of T for recovering all resonant mates | OPEN (not identified) | 4.7 |
| 24 | Free-coordinate part of mates recovered along C-tame approximants is carried by off-peak block coordinates | PROVED mod R1 | 5.2 |
| 25 | Some (f, rho g) with dist to NA > 0 | not found; no claim | 5.3 |
| 26 | Density of NA((c_0,p), l_2^2) | OPEN (leaning positive) | 5.5 |

