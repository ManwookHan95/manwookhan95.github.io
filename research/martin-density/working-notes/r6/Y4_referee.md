# Referee report on Y4 (Round 6): limits of window methods, non-window recovery, counterexample hunt

Refereed: r6/Y4_notes.md (= Y4_head + Y4_part1..3 + Y4_tail, checked identical), scripts r6/Y4_work/*.py, against
paper/martin_density_note.tex (Sections 1, 7, 8: Def. def:SLD, Thm thm:SLD, Lemmas box, pinning, triangular,
budget, suplevel, Prop. pinned, window certificate, Lemma uniformtransfer, Thm windowed, Thm thm:reductionZ, Toward
Lemma Z incl. Def. def:swallowed, Lemmas modswallow, badpeaks, exactswitch, windowtwopiece, onesidedtransfer, Thm S,
Rem. openZ; Section 7: bookkeeping, transfer data, persistence, two-piece data, Cor. D1) and the refereed Round-5
results (Z3 Thm E, Lemma U, Lemma 3.1, Prop. T + Z3_ref fixes and explosive design (D1^F); Z6_ref design D''' and
Thm U'; Z4 Thm A; Y2's donors where relevant).  My part files: r6/Y4_ref_part1..3.md; assembled fixes and proofs:
r6/Y4_ref_notes.md; scripts: r6/Y4_ref_work/{n3_check.py, pull_check.py, tune_check.py}.

## 0. Bottom line
The counting results (Prop. 1.2, Thm 1.6), the pigeonhole design D^PW, the ray-removal Lemma 1.8, the tuning lemmas
2.2-2.7 and the anti-sign threshold Lemma 2.9 are CORRECT (some with fixable design-bookkeeping gaps).  The central
conclusion of Part 2 is WRONG: Prop. 2.8(b) is true only for Y4's restricted move class (masses with the contact sign,
changes on F, z-moves at free coordinates), and the inference "with a diagonal base, lowering a z-signed functional is
possible only through the |F| - 1 channels on F" — on which the "directional residual (UN+)", Section 4.1(a) and the bottom
line rest — overlooks the FAR PULL (flip a far swallowing contact j of carrier l to the opposite sign and put a tiny mass
of that sign there).  This is the standard lowering device of Round 2 (P1 6.3, P2A, N2 Thm 1; N2 2.1 even notes that
for diagonal U "masses alone can only RAISE ..., which is why far pulls are needed").  At a companion a pull lowers the
value eps_l u_l(zhat) of ONE swallowed carrier by 2 v_l(j), with no first-order effect on any other coarse carrier and at
cost O(v_l(j) log(1/v_l(j))) (Lemma P1, proved); Lemma U / Thm E accept pulled support (Lemma P2); with private banks this
gives TWO-SIDED, PER-CARRIER, EXACT tuning for a diagonal base (Prop. P4, proved), and a sign-constrained Hoffman solve
neutralizes all tiny single-block rays exactly while moving every carrier value away from (or far from) its threshold
(Cor. P5, proved as an exactification step under the status part of Z3's (BS), which every exactification needs because
the block threshold drifts by O(Delta)).  So (UN+) is not a DIRECTIONAL residual of the companion route, Conjecture G_ray
is not needed there, and single-block d-rows are design-controlled at clean sub-windows.  What remains is the assembly (SKETCH), multi-block rays, Y2's coherent shift
resonance and infinite F.  No counterexample is claimed by the author, and nothing I found points to one.

## 1. Verdicts
| Claim (Y4 label) | Verdict | Issues / fixes |
|---|---|---|
| Prop. 1.2 explosive design, Cantor pairing (PROVED) | correct, fixable gaps | counting re-derived (|L_N cap [1,L]| <= N((2L)^{1/2}+1), injective blocking map). Absorption at unblocked windows with R multiplicative types needs u_R(l) = F(l)^{-1/(4Rl)} (else F^{R/4}, not absorbed for R >= 4). Target rooms are per coordinate (need a target-support design restriction); slaved rooms are joint objects, not covered |
| Obs. 1.3 (PROVED/HEURISTIC) | correct | one-signed domination re-derived; nested construction correctly HEURISTIC/OPEN |
| Def. 1.4 / Lemma 1.5 D^PW (PROVED) | correct, fixable gaps | bands disjoint, recursion N-free, box bound (even 3t^2) re-derived. (G-PW1) Design(l) must contain the room-closing factor 2^{s_max(l)}/delta_min(l) (Z3_ref G5); (G-PW3) Q(w) must dominate PRODUCTS of rate factors (room product x d-row Hoffman 1/u x design): take Q(w) = (4 Design/u(w))^{omega+3} |
| Thm 1.6 clean sub-windows (PROVED) | correct | pigeonhole; "any F" should read "F finite" |
| Cor. 1.7 (PROVED as stated) | correct with fixable gaps | absorption needs (G-PW3); cost carries a harmless log; the "exactify if tiny" half is a hypothesis ((X1)); slaving closure of the exactified set should be stated |
| Lemma 1.8 ray removal (PROVED) | correct | re-derived; D_min over ALL extreme rays (one tiny ray ruins it); compensated blocks need no Lemma 1.8 (adding an opposite robust ray) |
| Lemma 2.2 cost of tuned rows (PROVED) | correct | z-moves only with small l_1 norm (rooms of whole signature sets need Z3 Lemma 3.1 directly) |
| Lemma 2.3 banked Lemma U / Thm E (PROVED) | correct | balancing in Prop. T must use kappa a/a(zhat^tau) at tuned rows (harmless) |
| Lemmas 2.4, 2.5 channels (PROVED) | correct | re-derived (gamma = kappa^2/(2 J_max max(1,||U||^2))) |
| Lemma 2.6 raising (PROVED) | correct, fixable gap | ray vectors have infinite contact support: use truncated banks W_J (rate -> ||P^perp U^*W||^2/nu) |
| Prop. 2.7 exact tuning under (TC) (PROVED) | correct | quantitative IFT re-derived |
| Prop. 2.8 / Rem. 2.8' directional obstruction (PROVED) | WRONG (as a statement about lowering) | first-order formula h_W(j) = s_j^2 W(j) off F correct and N1 reproduced; (a) uses a change on F, not a pure bank. But "lowering only through the |F|-1 channels on F (+ one rescaling)" is FALSE: far pulls lower per carrier at first order (Lemma P1). Rem. 2.8' correct but superseded |
| Lemma 2.9 anti-sign threshold (PROVED) | correct | re-derived; consequence correct given |Delta d| M <= K_d t |
| Reductions at clean sub-windows 2.4 (SKETCH) | correct as a sketch, residual misidentified | (i)-(iii) fine as reductions; (iv) (UN+) is not a residual (Cor. P5); (P+) also by pulls; assembly items to add: transplant at changed e, sign-constrained solve, order "push weak peaks, then recompute pattern" |
| 4.1(a) "only (UN+) remains" (PROVED) | wrong | depends on (TC), Y2's open aligned corner, the SKETCH assembly, and the restricted move class |
| 4.1(c) Conjecture G_ray (OPEN) | correct label, not needed | not needed for the companion route (diagonal base, single block) |
| Non-window viewpoints 2.5 (PROVED) | correct | convexity elementary; locality = remark after Prop. prop:scale of the note (needs eps <= (1-rho^2)/3); Baire nothing new |
| Numerics N1 / N2 / N3 | N1 correct; N3 mislabelled | N1 re-run identical. N3 objective is |Delta theta_1|+|Delta theta_2| (absolute), not /t: relative switching is <= 0.47 t (eps_rel = 1), <= 0.10 t (eps_rel = 0.01); qualitative reading unchanged (HEURISTIC) |

## 2. Main findings (proofs in Y4_ref_notes.md)
**F1 (the missing lowering channel; NEW, PROVED).**  Pulled row: A := a - eps_l mu e_j^*, z'_j := -eps_l (j in S_l \ F
far out, beyond the target supports of all coarse carriers).  Lemma P1: val_l moves by -2 v_l(j) + O(mu), every other
coarse carrier by O(mu) (O(mu^2) for a diagonal base), cost <= C_f (v_l(j) + mu) log; rooms, rows and statuses kept;
l stays swallowed.  Lemma P2: Lemma U / Thm E hold with banked AND pulled support (no-flip at pulls from t|b(j)| <=
|a(j)|).  Lemma P3: transplanted data satisfy t|b(j)| <= 12 lambda_l v_l(j), so mu_j = 24 lambda_l v_l(j) works.
Prop. P4 (diagonal base, signature sets with bounded gaps G_l): exact two-sided per-carrier tuning val_l -> val_l + x_l
(pull to overshoot, then private banks with DIAGONAL Jacobian diag(s_{j'}^2 v_l(j')/nu)), others moved O(|x|^2), cost
O(|x| log(1/|x|)).  Cor. P5: at a clean sub-window of D^PW the tiny single-block rays are made EXACTLY d-neutral (d-sum
D_r = (q_0/sigma_m) V_r(zhat)); the sign-constrained system R x = -V, x <= 0 on near-threshold q > 0 carriers, is
feasible (x = -val) and Hoffman gives |x| <= design x b(w); carrier values move away from (or stay far from) their
thresholds (status of NT carriers additionally needs the status part of Z3's (BS): the block threshold drifts by O(Delta)
under every exactification move); cost o(T_lo^2).  Numerics: pull_check.py
(lowering exactly 2v(j), others unchanged) and tune_check.py (exact +-x tuning, residual 1e-16, masses >= 0).
**F2 (design bookkeeping).**  (G-PW1), (G-PW3), and for the explosive design u_R; plus addendum (G) bounded gaps of S_l
and H_tune(l) in Design^PW(l).  All are design choices made before f; N-free.
**F3 (overclaims).**  Prop. 2.8's consequence, 4.1(a), the bottom line ("what remains is DIRECTIONAL") and table items
14/18/23 must be relabelled; the "first draft" correction (neutralization by masses removes K_nn is FALSE) is right for
masses alone but wrong for masses + pulls.

## 3. Attacks attempted
weak* vs norm (decompositions at every scale; Thm E compares with g only beyond c_flat t); uniformity in t (pull masses
fixed per window; no-flip bound holds at every scale of the window), in the window (all new constants are design
quantities of level l times f-constants; Q(w) enlarged), in the number of active carriers (H_tune over all patterns and
subsets of level l), along companions (Lemma P2 needs only convergence of forced data); Hoffman/Farkas constants (right
sides irrelevant; feasibility of the sign-constrained system via x = -val); design N-independence (all added factors
N-free); non-attained infima (Hoffman nearest points exist: polyhedra); signs (pull sign, contact-likeness, NT carriers
lowered only, q_l = q_0 val_l/sigma_m at strict non-peaks); near-contacts vs contacts (pulled coordinates become SUPPORT
coordinates, not anti-sign contacts — otherwise the carrier would acquire a tiny room and the data would violate side
admissibility); c_0 vs l_infty (pulled/banked rows have z in l_infty, not norm attaining; allowed by Thm E); finite vs
infinite (finitely many pulls and banks per window; ray vectors with infinite contact support truncated); hidden
assumptions on T (only (T-a)-(T-d), (P1)-(P3), allowedness (a),(b) used; the base U chosen diagonal, which is admissible);
quantifier order (design (incl. G_l, H_tune) before f; companions after g, rho, window).  None broke F1.

## 4. Single most valuable idea
Far pulls at companions: flipping a far swallowing contact of carrier l into a tiny opposite-sign SUPPORT coordinate lowers
the value of that one carrier at first order and at proportional cost, for every base; with private banks (diagonal base)
this gives two-sided per-carrier exact tuning, so every tiny single-block ray d-sum can be made exactly zero at a clean
sub-window (with a sign-constrained Hoffman solve that moves no carrier value toward its threshold).  This removes Y4's directional residual (UN+),
the single-block part of item (m) and the nearly-neutral rate K_nn of item (r) from the companion route.

## 5. What remains open
Lemma Z and density of NA((c_0,p_N), l_2^2) are OPEN for every admissible T, including D''' and D^PW.  For D^PW (with
the fixes) and F finite, the companion/window route still needs: (a) the full ASSEMBLY (SKETCH): simultaneous
exactification at one pulled-banked-tuned companion per clean sub-window (rooms and target rooms closed, tiny-margin
swallowing peaks pushed, pattern recomputed, tiny rays neutralized, slaving closure, and the status part of (BS) for
near-threshold q > 0 carriers under the O(Delta) drift of the block threshold -- a threshold buffer by Y2's donors works
outside Y2's aligned corner, and two-sided pulls/banks on an unused swallowed carrier of the block should work everywhere:
SKETCH), transplant (Prop. T) at a row with changed a and e, and Thm E; (b) multi-block rays (m'): vector-valued d-rows, where exactification of tiny joint objects is
determinantal rather than linear; (c) Y2's coherent shift resonance (item (h), (H2'') failure with c_* = 0); (d) Y2's
aligned corner (plausibly settled by pulls: SKETCH); (e) (O4) infinite F; (f) non-diagonal bases (only if the base is not
chosen diagonal).  No counterexample; nothing points to one.
