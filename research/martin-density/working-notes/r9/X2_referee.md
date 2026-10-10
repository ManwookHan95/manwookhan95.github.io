# Referee report on X2 (Round 9): d-consistent engineered approximants, uniform composition (S2), mixed activity classes (C_mix)

Refereed: r9/X2_notes.md (= X2_head + X2_part1..6, identical up to blank lines, checked with diff) and r9/X2_work/*.py (re-run: dcons_check,
dcons_check2, dc_jacobian, ue_check — numeric outputs identical), against paper/martin_density_note.tex (lem:threshold, def:certificate,
lem:base, lem:block, lem:bookkeeping, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence, lem:assembly, def:twopiece,
def:engineered, lem:approxfacts, lem:F1, lem:anchor, def:SC, lem:scrambling, thm:engineered with its proof, lem:slack, prop:reduction) and the
refereed Rounds 5-8 (Z3 Lemma 3.1 / Theorem E; V1 Proposition TR, Lemma TU; U1 parts 1-5 with U1-ref (Lemma R-kt, Proposition KN, G1, D^{U1'},
MT IV'); U3 Lemma VT with U3-ref F6; U4/U4-ref T_final).  My part files: r9/X2_ref_part1..4.md; assembled proofs of all fixes:
r9/X2_ref_notes.md; scripts: r9/X2_ref_work/ (rmodel.py — an independent multi-block model written from scratch — check_J.py, check_J2.py,
absorber_check.py, with outputs; rerun/ holds the re-runs of X2's scripts).

## 0. Bottom line
X2's main technical line is sound and genuinely advances the program: exact d-CONSISTENCY of the engineered approximant (the normalized
values of all switching carriers re-tuned exactly by levers) removes the only first-order term of thm:engineered that is not uniformly
small; with it, Theorem UE gives per-piece engineered bounds on |tau| <= c_flat t with f-constants K_sharp, c_flat (violated data allowed),
and Theorem E^eng averages AT the norm-attaining approximant, so (S2a'), (S2b), (S2c) are closed (with the design condition (W_exp)).  The
correction of U3-ref F6a (Proposition J) is right: for valid data the junction mismatch is O(s_1 (n |Omega|)^{1/2}), not s_1/t^2.  Lemma DC
(rank-one linearization I - p q^T, Sherman-Morrison, Poincare-Miranda) is correct; Lemma CM's rule (negative fine carriers self-aligned,
positive ones anti-aligned, all failures tolerated as contact violations) is the key new idea for mixed classes.
But Theorem C_mix (and hence the mixed-class part of Master Theorem V) is NOT proved as written: X2 keeps U1's zero-value absorbers in the
switching data and re-tunes them by (S-mass) levers (Lemma LV(d)).  Those levers have a range ~ m_0 mu_{p0}^2 (astronomically small, not a
design quantity of level L), the absorbers' value rooms are ~ their weights (<= c_{L+1}), and the coarse levers (pull flips at coordinates of
E_c, banks/z-moves at j(l)) and the window theta-masses move the absorbers' values far beyond both; untuned, the absorbers become peaks with
nonzero switching coefficients, a FIRST-order cost in the theta regime.  The obstruction is structural for X2's parameters and generic in mixed
classes (violations force s_1 >= 64 rho eps/delta above the rooms of later absorbers).  I give a complete repair (R-abs): in the violation-
tolerant route the absorbers are simply not used (no switching coefficients); fine residues on coarse coordinates and trace corrections become
tolerated violations of mass O(Design c_{L+1}); every remaining lever is coarse with design-quantity constants.  With (R-abs), Theorem C_mix and
Master Theorem V hold as stated.  Further precisions: placement of (W_exp) (only after MAIN stages; as written it contradicts D^{U1'}'s cluster
weights), the radius of Lemma DC, TU pulls as fixed O(1) moves, the late threshold s_late, a missing hypothesis of Theorem E^eng, constants (c3).
Referee addition: d-consistency with Omega = all coarse strict non-peaks freezes C_m (hence all gaps and relative positions of the switching
carriers) up to fine carriers.
No counterexample is claimed or suggested.  The F-finite residual is U1-ref's status coherence ((KN) failure), as X2 says.  Lemma Z and density
of NA((c_0, p_N), l_2^2) (every N) and of NA((c_0, p), l_2^2) remain OPEN for every admissible T.

## 1. Verdicts
| Claim (X2 label) | Verdict | Main point / fix |
|---|---|---|
| Lemma M1, Cor. M1' (PROVED) | correct | re-derived; sharp bound ||X|| <= 4 rho s_1 (nu sum h(b^theta_i))^{1/2} for masses off the support |
| Proposition J (PROVED; attainment HEURISTIC) | correct upper bound, (p-J) | cut-off term is max_Omega t_k; inequality checked in an independent model (max ratio 1 - 6.8e-3, attained for |Omega| = 1); U3-ref F6a's s_1/t^2 concerned data with Gamma ~ t^{-2} |
| d-consistency identities 1.4 (PROVED) | correct | exact to 1e-16 numerically; REFEREE ADDITION 1.2: Omega = Q freezes C up to Q \ Omega |
| Lemma M2 (PROVED) | correct, (p-DC3) | "peaks remain peaks" only above the perturbation |
| Lemma DC (PROVED) | correct as an abstract lemma, (p-DC1), (p-DC2) | radius needs (1 + 1/A_min); pulls are fixed O(1) moves, carriers meeting pulls have super-small weight W_pull |
| Lemma LV (PROVED) | (a)-(c) correct for coarse carriers, (p-LV1), (p-LV2); (d) FALSE in the application | (S-mass) levers of zero-value absorbers have range ~ m_0 mu_{p0}^2; pulls lie in E_c for X2's s_1 |
| Lemma UE-1 (PROVED) | correct after (p-UE1)-(p-UE3) | W_pull terms; Omega carriers are in S_2 whatever Phi gap; c_fine in |c_i| |
| Theorem UE (PROVED) | correct as a conditional theorem after (p-UE4)-(p-UE7), (c3') | K_sharp, c_flat f-constants: the substance is right; s_late must include the K_w powers actually used |
| Theorem E^eng (PROVED) | correct, (p-E1) | add K_w c_fine <= K T^2 and tail_W <= K T^2/K_w |
| (S2c) with (W_exp) (PROVED arithmetic) | correct for coarse levers after (p-W) | false for X2's absorber levers; (W_exp) only after main stages |
| Lemma CM (PROVED) | rule and violation count correct (key idea); used with tuned absorbers it fails; (a)'s x_0 wrong for absorbers of a negative block 1 | replaced by Lemma CM' |
| Theorem C_mix (PROVED mod refereed tools) | GAP as written; TRUE after (R-abs) | Lemma CM', Theorem C_mix' PROVED in X2_ref_notes 4 |
| Design D^{X2} (PROVED by inspection) | correct with (p-W), n_l in (D-lev) | — |
| Master Theorem V (PROVED mod refereed tools) | statement PROVED after (R-abs); contrapositive correct | residual = status coherence |
| Precision of U3-ref F6a; IV.2 superseded; (S1), RT*(c) absorbed (PROVED) | correct (IV.2 after (R-abs)) | — |
| Numerics (sanity) | reproduced; weak as evidence (as X2 says) | finite models rebalance optimally |

## 2. Main findings (proofs in X2_ref_notes.md)
F1 (absorber obstruction; Section 2.3 of the notes).  Every coarse lever acts at a coordinate s of E_c(w) (j(l), and the pull j_p, which lies
in E_c for r >= 4 K_J T^4 s_1, s_1 >= exp(-1/(2T)) >> c_{L+1}^2); every such s has a tuned first pair with |u_a(s)| >= 1/(8 n_a).  A pull flip moves u_a
by >= 1/(4 n_a), a Z/bank lever by >= r/(8 n_a Design), a theta-mass by m_s mu_s^2 |u_a(s)|/nu; the room of a is theta Phi_a/m ~ lambda_a; the (S-mass)
range is <= m_0 mu_{p0}^2/nu downwards and destroys the row upwards.  Lemma DC's hypotheses fail, and untuned absorbers become peaks with
Domega(a) != 0: first-order block excess rho |tau| |Domega(a)|/2 in the theta regime.  Smaller s_1 would avoid it only when the violation mass is
below the rooms of the touched absorbers — generically false in mixed classes.  Illustrated numerically (absorber_check.py).
F2 (repair (R-abs)).  Absorbers carry no switching coefficient (ordinary fine carriers, owner-candidates of type (d)); b^+ := beta + chi V_proj
+ V_fine/2; violations: contacts viol <= |V_fine|, free coordinates with b^theta = 0; eps <= C_f Design c_{L+1} + C_f c_{L+1}^2/T; Omega = coarse
strict non-peaks; levers coarse with design constants; fine carriers moved by levers cost <= C Design c_{L+1} <= c delta s_1.  Then Theorem UE +
E^eng apply verbatim: Theorem C_mix and Master Theorem V hold.
F3 (referee addition).  At a d-consistent approximant with Omega = all coarse strict non-peaks, C' - C is driven only by the fine strict non-peaks
(clamp-formula root argument), so gaps and relative positions of all switching carriers are preserved up to K (c_fine Pi + W_pull): d-consistency
needs one lever per carrier and protects statuses automatically (no conflict with U1-ref Lemma R-kt).  Numerically |C' - C| <= 1.1e-16.
F4 (precisions).  (p-DC1) r := 4 K_J (1 + 1/A_min)(delta_1 + T^4 s_1) + 8 K_J W_pull/A_min.  (p-DC2) TU pulls: fixed O(1) moves; W_pull <= 2m sum_{stages >=
j_p} c, super-small; enter F(0), Bregman, scrambling, cost.  (p-UE5) s_late := c delta (T gap_min x_0/(n A_0 K_w))^{C}; still >= T^{C''}.  (p-E1) as in the
table.  (p-W) (W_exp) in c_{L+1}^low after main stages only.  (c3') rho c_flat (2 A_2 + C_Delta) <= 7.  (p-LV1) n_l in (D-lev).

## 3. Attacks attempted
uniformity in t (per-piece radius c_flat t_i; K_sharp f-constant; the theta regime is common; pieces with c_flat t_i <= s_1 live in the theta regime
only), in the window (K_w and s_late polynomial in T once the absorbers are dropped), in the number of carriers (|Omega| <= LN and n pieces enter only
window constants), along companions (Lemma M2 ball, transfer-data persistence), simultaneous exactifications/levers (FOUND F1; Prop. KN's levers
and Lemma DC's levers use disjoint coordinates at different value scales), the two-lever count of Lemma R-kt (no conflict, F3), Hoffman/minor
constants (only through the refereed Prop. KN), design N-independence/admissibility/well-foundedness (FOUND (p-W); (D-lev) fine with n_l), signs
and one-sidedness (FOUND: (S-mass) levers are one-sided with tiny range; TU pull + bank two-sided; Z-con inward/bank continuous), quantifier
order (design -> f -> g, rho -> transfer data -> main stage, clean w -> companion -> class, cube -> data -> N_w -> s_1 -> levers -> N''),
counterexample search (none: every defect found is a route/bookkeeping defect with a repair).

## 4. Numerics (sanity only)
check_J.py / check_J2.py (independent model): block norming vs CLARABEL; Proposition J's inequality (never violated; attained for |Omega| = 1);
identities (1.1) and H' = (C/C')H exact to 1e-16; C frozen when Omega = Q (1.1e-16) versus 5e-11 when one strict non-peak is left out.
absorber_check.py: zero-value absorber pushed 90-170 times beyond its room by a coarse lever move of size 1e-6; not restorable by its (S-mass).
X2's scripts re-run with identical numeric output (kappa/||X|| = 0.0230; J_fd = I - p q^T to 2.1e-10; UE bound in a finite model).

## 5. Single most valuable idea
Violation tolerance makes EXACT completions unnecessary: negative fine carriers self-aligned (state (R), quadratic scrambling bound), positive
ones anti-aligned, and every failure is a contact or theta-free violation of mass O(Design c_{L+1}), tolerated uniformly in the scale by
d-consistent engineered approximants (Theorem UE) averaged at the norm-attaining point (Theorem E^eng) under super-small weights ((W_exp)).
The referee's complement: in this route the zero-value absorbers must be dropped (they cannot follow the levers), and d-consistency then
freezes the block scalars and all switching statuses up to fine terms.

## 6. What remains open (D^{X2} with the repairs; finite I)
F finite: status coherence — (C*) rows with (KN_{w,a}) failing at almost all scales of all clean sub-windows of all large main stages (an active
block with an active near-threshold switching carrier and no inactive Omega carrier of robust relative position).  F infinite: (E1)-(E5) / U2's
items, and (C*) at infinite F.  Lemma Z and density for p_N (every N) and for p: OPEN for every admissible T.  No counterexample; nothing points to one.
