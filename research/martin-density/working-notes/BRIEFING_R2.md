# Round-2 briefing (read after ctx/BRIEFING.md)

All paths below are relative to ctx/ = /tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx

## New primary source: Martín's paper (read ctx/martin_paper_summary.md in full)
Most important facts: Lemma B's T is obtained from an ARBITRARY sequence (w'_n) in S_Y having every point of S_Y as an
accumulation point, via [16, Prop 2.8] (exact construction unavailable); block m uses the same sequence:
the normalized T(e_{n,m}) "follow" w'_n for EVERY m. So (i) Martín's space is a family indexed by admissible choices of T;
(ii) cross-block near-duplicates u_{n,m} ≈ u_{n,m'} at comparable scales Φ_m(n) ≈ 2^{m'-m}Φ_{m'}(n) are built in (up to the
unknown perturbations of [16, Prop 2.8]); (iii) M_m = ||w_m||_∞ ∈ [1 − 2^{-m}, 1], C_m ≤ 2^{-m} in every block.
Any argument may use ONLY: Lemma B's conclusion (T norm one, injective, range in Y, Y ∩ c_00 = {0}, Y dense, every block's
normalized vectors dense in S_Y), unless it explicitly states an extra hypothesis on T. A theorem of the form
"for every admissible T" is the goal; a theorem "for every admissible T satisfying (explicit condition), and such T exist"
is an acceptable fallback (one may construct T satisfying Lemma B directly; Martín's proof uses nothing else about T).

## Refereed Round-1 results (correct unless noted; read the notes for proofs)
- r1/G_notes.md §3.8–3.10, 6.6 (+ r1/G_referee.md §4.7): p is Fréchet smooth; NA ∩ S_{p*} = ∇p(S_p); forced decomposition
  varies norm-continuously; asymptotic dual norm formula along w*-null sequences; exact parametrization of NA approximants
  f'_n → f  (a'_n ∈ c_00 → a in ℓ_1, z'_n ∈ c_0 → z coordinatewise, far coordinates free).
- r1/A_notes.md (+ r1/A_referee.md): (R3) lower-limit theorem and finite/mate versions; exact certificate expansions;
  NA-scale criterion; **Transport Theorem**: every finite certificate at f transports along EVERY sequence f_n → f, so
  cl Cert(f) ⊂ Li C(f_n) for every sequence; shifted certificates (quadratic rebalancing τ²θ_m w_m) transport too;
  Theorem W (weighted), Theorem L (locally admissible linear decompositions); **Averaging Theorem 6.8**: if for all small t
  there is a finite certificate c_t with H ≤ 1+o(1), radius ≥ c_0 t (use the COORDINATEWISE radius — referee fix G1),
  bounded κ, and ||g − g_{c_t}|| ≤ K t, then g ∈ cl Cert(f) (for I = N one needs τ² = o(C_m) on active blocks — fix G2);
  budget identity Lemma 7.1, exact excess formulas Lemma 7.2, Cor 7.3; Prop 7.4 (one-sided linear decompositions; at NA
  points they coincide); classification §7.2 (defect needs SWITCHING between one-sided carriers on the two sides of t=0
  at arbitrarily small scales: contacts/near-contacts/near-flip base coordinates, weak peaks, off-peak coordinates pushed
  beyond their gap); Conjecture 7.5 (scale separation ⇒ empty defect) — UNPROVED. Referee: "shifts strictly enlarge the
  class" is UNPROVED; two-piece mates over infinite contact sets exist (SKETCH) and with constant contact split are in
  Cert(f) (PROVED); with non-constant split they are recoverable along ENGINEERED NA sequences (referee SKETCH, A_referee §5.4).
- r1/D_notes.md: Thm 10.4 (conditional dual transfer), Lemmas 11.3–11.5 (truncation with exact first-order correction),
  **Thm 11.6: every locally split mate is recovered** (in particular every normalized split-contractive operator);
  Cor 11.8: LSD ⇒ density; Prop 11.9 (block rigidity); Thm 12.4' (finite-rank Hilbert test case); §12 cross-mate rate
  trichotomy (HEURISTIC). (Referee report for D may appear as r1/D_referee.md.)
- r1/C_part*.md (in progress, partial): kernel-slice form of the fibre, slack/localisation lemma, transfer lemmas, exact
  local block formula (Lemma 5.1), tame NA points have finite-dimensional fibres (Thm A), tame non-attaining f: every mate
  is a balanced finite certificate (Thm C), recovery of natural finite certificates (Thm B), the gap Γ_w ≤ 1 < Γ_max
  (second-order rebalancing — compare A's shifted certificates), "implant scale gap" heuristic (an engineered non-peak at
  depth k costs ε ≳ Φ_k, so its quadratic window ~Φ_k lies below the slack scale ~sqrt Φ_k).
- r1/E_part*.md (in progress, partial): counterexample candidates; a critical cross-mate candidate whose carriers become
  peaks at every NA approximant — NOTE (orchestrator): that candidate is "certificate + O(t)" at f itself, hence lies in
  cl Cert(f) by A's Averaging Theorem and is recovered along every sequence by the Transport Theorem; E's averaging lemma
  (convex combination of certificates at geometric scales, error 2κt²/J) is the same mechanism.

## The open core after Round 1
Def(f) := C(f) \ (closure of all mates recoverable by the proved mechanisms). Density ⇔ every mate is recovered.
Known: a defect mate must at arbitrarily small scales, on BOTH sides of t = 0, carry a component of size ≫ t through
ONE-SIDED resources, switching carriers between the two sides (A §7.2); this needs a "resonance": approximate linear
relations, at the carriers' own scale Φ, among base contact vectors e_j* and block vectors u_{k,m} (or among block vectors
of different blocks/indices). In Martín's construction such cross-block near-duplicates are built in (same w'_n in every
block), so scale separation of T cannot be assumed for Martín's own T.

## Discipline (a previous agent crashed by exceeding 128k output tokens in one response)
Work in many SHORT steps (≤ ~15k tokens of reasoning per turn before a tool call). Write results incrementally to part
files, then assemble a final notes file. Label every claim PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Proofs in English,
fully rigorous; no heuristic presented as proof. Use numpy for finite-model sanity checks when useful.

## ADDENDUM (after Round 2 task P1 and the Round-1 C, E referee reports)
- r2/P1_notes.md + r2/P1_referee.md (refereed, core correct): there is an admissible T (only Lemma B's conclusion used) and a
  non-attaining f in S_{p_N*} (every N >= 1) such that every intrinsically recoverable class (finite/shifted/weighted
  certificates, locally split, averaging class, C Thm 7.1/7.4) lies on ONE line R u (u = u_{2,1}), while C(f) contains an
  infinite-dimensional family of two-piece SWITCHING mates g_{K1} = c u 1_{K1} - beta a (exact resonance: an off-peak carrier
  with w = 0 whose vector u is supported on supp a plus an infinite contact set, with the contact signs, u(zhat) = 0).
  So Def(f) ≠ ∅ relative to all intrinsic mechanisms; along C-tame NA approximants Li C(f_n) ⊂ Li S(f_n) (referee R1-R3), so
  these mates are NOT recovered along canonical truncations. They ARE recoverable along ENGINEERED NA sequences (P1 §6.3,
  SKETCH: window masses, tuning masses, far sign-flipped contacts with negative masses as free pulls making u(x') = 0
  exactly, constant tail mu_inf u on the target; referee: plausible, three fixable gaps — g ∈ C(f) needed for the slack;
  the partial-pull coordinate j* has first-order cost and must lie beyond the tail threshold; state quantifier order).
  Also PROVED: linear obstruction (intrinsic classes ⊂ cl S(f), S(f) = span of certificate directions); exact resonances
  require infinite one-sided base sets (none at NA points); weighted averaging theorem; sign rule for cross-block
  near-duplicates (exact or o(Phi)-perturbed duplicates serve the same side and cannot switch).
- r1/C_notes.md + r1/C_referee.md: Thm 7.4 (transfer peaks: second-order base/block rebalancing is free; sharp invariant
  Gamma_w = q_0 H_b + sum sigma_m H_m), Thm 8.4: every (f, rho g) is recovered when f is tame with no kinks and no degenerate
  peaks. Referee: Prop 8.1's lower bound needs a cofinite free set; supports with infinitely many kinks join the open core
  (finite analogue: Gamma_2 <= 0.296 < Gamma_w = 0.485 via one-sided first-order re-splitting through kinks).
- r1/E_notes.md + r1/E_referee.md: no counterexample; destruction-conversion duality (Lemma 6.1/Cor 6.2), window moves o(1)
  along NA approximants (Prop 8.2), single far detectors can be neutralized (Lemma 6.4); OPEN loophole: error-dominated
  one-sided near-threshold peak carriers with bounded conversion capacity ("rigid" T); OPEN: two-piece mates with Delta d < 0
  (T1 ignores the d-coefficients of block carriers).

## ADDENDUM 2 (after Round-2 tasks P2 (two instances: P2x and P2A) and N2, all refereed)
Files: r2/P2_notes.md (= P2A), r2/P2x* (other instance; see the top of r2/P2_referee.md), r2/P2A_referee.md,
r2/N2_notes.md, r2/N2_referee.md, r2/N2_ref_notes.md.
PROVED (refereed):
- P2A Thm 2.1 / N2 Thm 1: every d-neutral (Delta d = 0) exact two-piece switching mate (any contact set K, any split, one
  active block, or several under a span hypothesis (S)) is recovered along ENGINEERED NA approximants, with no rate
  condition on T. Tools: window masses on finitely many contacts, far sign-flipped contacts carrying negative masses
  ("far pulls"), one raising/tuning mass fixed by the intermediate value theorem so that v_m(x') = 0 exactly, a constant
  theta-tail of the target used only for |tau| <= s_1; the slack is then needed only beyond a FIXED T_0 (scale decoupling).
  Hence ALL explicit defect mates of P1's example are in Ls(f): P1's defect is a defect of intrinsic mechanisms only.
- P2x Thm 3.5: two-piece switching mates with Delta d_m >= 0 in all blocks (several blocks, any split) under a tuning-cone
  condition (TC): the d-mismatch Delta d_m R_m*(w'_m - w_m) is placed by convexity into the block of the side on which it
  moves toward w_m, paid by a Bregman excess which is o(s) (identity |zeta'|e(y;y') + |zeta|e(y';y) = <w'-w, zeta'-zeta>).
- N2 Thm 2 (Delta d > 0 under (BR)), N2 Thm 3 (Delta d < 0 under (PC)); N2 referee Lemma R: with anchor
  y = w' + (w'-w)1_S (S = coordinates where 2w'-w does not overshoot), N(y) <= 1 + (C'-C)_+ + second order, so Delta d < 0
  needs only (PC*): (C'-C)_+ + ||D(w'-w)||^2 + sum over status-changing k of lambda_k|w'-w| = o(t_n). Every exact
  resonance with a single carrier non-peak is recovered whatever the sign of Delta d.
- Opposite peaks are unavoidable: every NA f' near a non-NA f has, in every block, infinitely many common peaks of
  opposite sign (N2 3.3). Base mixed term (contact masses vs Hilbert part of q*) is NOT an obstruction (cancelled by tuning).
- C's "implant scale gap" is not an obstruction for robust structure (scale decoupling).
FALSE/CORRECTED: P2A Thm 3.4 is vacuous (tuning span can never hold: sum lambda omega_Delta psi = v vanishes on free
coordinates); replication to depth theta costs O(theta log(1/theta)) (not O(theta)) for admissible T.
OPEN CORE after Round 2 (all referees agree; nothing points to a counterexample yet):
 (O1) carrier blocks with strict non-peaks at a positive proportion of fine scales / generic supports with infinitely many
      non-peaks (C's deep coefficients c_k ~ sqrt(Phi_k); margin-sparsity (MS-Q) of fine non-peaks for Delta d < 0);
 (O2) second-order rebalancing at engineered approximants (mates whose explicit side decompositions have coefficient > 1,
      kappa_max > 1, Gamma_w <= 1): combine C's transfer peaks (Thm 7.4) / A's shifts with the engineering;
 (O3) approximate resonances = genuinely scale-dependent switching (weak peaks, near-threshold carriers with summable gaps,
      off-peak coordinates pushed beyond their gap, scale-dependent splits): need a transport hypothesis (HT) / quantitative
      tail independence (QI) of T, or a supply of two-sided carriers with frozen error O(scale) at J ~ 16 kappa/(1-rho^2)
      adjacent scales; "far rigidity" (nearly collinear far tails inside detector groups) is compatible with Lemma B
      (N2 SKETCH), so Lemma B alone does not force conversion capacity;
 (O4) several active blocks without (S)/(TC); infinite block sets.
