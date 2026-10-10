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

## ADDENDUM 3 (Round 3, refereed): r3/S3_*, r3/R3_*, r3/G3_*
- S3 (refereed correct, with the referee's Lemma F1 repair of |C'-C| = O(s_1)): first-order rebalancing through transfer
  peaks replaces all steering; Theorem A (weighted kappa_w), Theorem B (exact one-sided second-order coefficient at (BT)
  points, any contact set, Fenchel duality), Theorem D (engineering with window masses + far truncation only; Delta d_m < 0
  blocks need the scrambling condition (SC_m)), Cor D1 (F finite, Delta d_m >= 0, kappa_w <= 1 two-piece mates are in Ls(f),
  no conditions on Q_m, K or T), Cor D2 (every (BT) point is in R; P1's example: every mate recovered).
- R3 (refereed): no counterexample; Theorem EC (rate-free generic carriers: o(1) window moves make generic tail coordinates
  exact zero-weight strict non-peaks carrying any finite-dimensional family of O(scale) errors); E's rigid design is NOT
  shown recovered (referee: a rho-independent Hilbert/room capacity requirement remains); joint certificates on disjoint
  zero-weight non-peaks pool Hilbert capacity.
- G3 (refereed correct; one constant fix in 5.3: kappa_0 = (sqrt(1+eta_0/2)-1)/2): a DESIGNED admissible T ("signature-ladder
  design", SLD: private signatures delta_l h_l on disjoint infinite coordinate sets S_l, coarse-to-fine allowed targets,
  super-fast weights creating long windows of scales). Theorem B: for the SLD T and every N, every f in R_0 := {F = supp a
  finite, (SR) signature room: ||h_l 1_{S_l ∩ J_gamma}|| >= vartheta^l ||h_l|| for all l, J_gamma = {j ∉ F : |z_j| <= 1-gamma}}
  is recoverable (every mate). R_0 contains all NA points and all base-tame f. Theorem C: for the SLD T, density of
  NA((c_0,p_N), l_2^2) <=> LEMMA Z: every (f, rho g) (g ∈ C(f), rho < 1) is a norm limit of contractive (f', g') with
  f' ∈ R_0 and g' ∈ C(f') (f' need not be NA). Remaining difficulty: "signature-resonant" f (base one-sided resources
  swallow signature sets; e.g. |z_j| = 1 on large parts of the S_l, possibly K cofinite) and infinite F.
  Referee's suggested route: lower |z| on FAR parts of the swallowed signature sets (pinning constant delta' tiny), so that
  at scales well above it f' copies f's mate structure and the windows of f' lie below it (scale decoupling as in P2A); the
  transition band handled by the rho-slack plus Round-2/S3 engineering of the finitely many unpinned carriers (G3 6.3(d)).

## ADDENDUM 4 (Round 4, refereed, and integrated into the note): r4/Z1_*, r4/Z2_*; note = paper/martin_density_note.tex (78 pp)
The note paper/martin_density_note.tex (Section 8, especially Subsection "Toward Lemma Z", lines ~4700-5845, and Remark rem:openZ)
is the authoritative, refereed state; use its numbering and notation. Summary:
- Theorem B* (Z1, refereed): for the SLD T, F finite, every WINDOW-PINNED mate is recovered at ANY f (obstruction is a property of
  the mate: persistent switching through unpinned carriers).
- Theorem B± (Z2): sign-mixed room theta_l = ||v_l 1_{S_l\F}|| - |<v_l 1_{S_l\F}, z>| replaces (SR): cofinite contact sets with
  sign-mixed signatures are in R.
- Theorem S (Z2, with referee fixes): F finite, finitely many EXACTLY swallowed signature sets (or infinitely many, all resonant and
  d-neutral, (H1)), under (W*), (H2), (H3): f in R without approximating f. Method = HOFFMAN MATCHING: on each window the free switching
  violates the finitely many constraints of the polyhedral cone of exact d-neutral resonances by O(K t); Hoffman projection + trimming of
  the + contact base + theta-split give EXACT two-piece data at every window scale; windowed averaging (G3 5.2) + S3 Cor D1 recover.
- Theorem M (Z1 referee, SKETCH): finitely swallowed points with exact free resources are in R.
- Theorem B^inf (Z1, SKETCH): infinite F with room; step (iv) unproved.
- Far lowerings f^L (z^L := 0 on union_{l>L} S_l): admissible forced data, f^L -> f, every S_l (l > L) roomy at f^L, coarse data kept;
  at f fine carriers only box-bounded: sum_{l>L} |Delta theta_l| <= 6 c_{L+1}/t. Heuristically p*(f^L - f) = O(c_{L+1}).
- Corrections: Z1's "exposed face => rho C(f) subset C(f') forces f' = f" is a NON SEQUITUR (exact criterion: f'^2 + rho^2 r~_f^2 <= p^2);
  pure base mates transfer exactly (q*(a + s b) <= s(s) for all s => p*(f' + s b) <= max(q*(a+sb), 1)); Z1's common-functional
  obstruction is WRONG. Z2's switching-budget gloss is false with near-contacts: off F ∪ K only the (1-|z_j|)-weighted mass is O(t).
- Lemma Z is per mate (f' chosen after g, rho). Enlarged target class G := R_0^± ∪ R_S ∪ R_BT ⊂ R (Problem prob:lemmaZper).
OPEN CORE after Round 4 (Remark rem:openZ of the note), all for the SLD T and finite I:
 (O1) genuinely scale-dependent switching on swallowed signature sets, F finite: (i) APPROXIMATE swallowing (rooms positive but decaying
      too fast: near-contact tails |z_j| -> 1 on S_l \ F, or contact signs on S_l changing only far out): switching data are z-signed only
      up to first-order errors of l_1-mass O(t) (weighted), so S3 Cor D1 (needs EXACT two-piece data) does not apply — "exactness vs scale";
      (ii) weak or near-threshold free carriers, bad degenerate peaks with the swallowing sign (H3 fails), blocks whose non-degenerate peaks are
      all swallowed (H2 fails).
 (O2) infinitely many swallowed carriers (non-resonant or non-d-neutral): lower semicontinuity dist(rho g, C(f^L)) -> 0 along far-lowering
      (or other finitely-swallowed) approximants; and are all finitely swallowed first rows in R?
 (O3) maximal contact off (BT): F finite, z ≡ epsilon off F (every signature swallowed, every peak carrier bad, B infinite).
 (O4) infinite base support F without room (with room: B^inf, SKETCH).
Referee suggestions: (i) an "approximately two-piece" version of S3 Cor D1 tolerating first-order defects (sign errors of l_1-mass
O(scale) on near-contacts); (ii) uniform Hoffman constants over growing finite carrier sets (scale-dependent active sets U*(t)).

## ADDENDUM 5 (Round 5, all refereed): r5/Z3_*, r5/Z4_*, r5/Z5_*, r5/Z6_* (notes, referee reports, ref_notes with fixes)
NOT yet integrated into the note. Use the referee-corrected versions (each *_referee.md lists fixes; *_ref_notes.md proves them).
Z3 (O1): Theorem E (PROVED): windowed recovery THROUGH NEARBY FIRST ROWS f_j -> f (same base support): exact d-neutral two-piece window
  data at f_j on windows (T_j, n_j) with K_j T_j -> 0, n_j/K_j -> inf and p*(f_j - f) = o((T_j 2^{-n_j})^2) give (f, rho g) in cl NA.
  Lemma U (uniform one-sided transfer along f_j, supp a_j = F). Lemma 3.1: companion cost p*(f^# - f) <= C c(delta),
  c(delta) = sum_m [Delta_m log(e/Delta_m) + sum_k min(lambda_k, |u_k(delta)|)] (unweighted term necessary). Proposition T (transplant,
  conditional; referee fixes T1-T6) + Cor 3.4: window decompositions at f become exact data at a coarse EXACTIFICATION f^#.
  Lemma 1.4: exactifying a d-neutral approximately resonant carrier destroys d-neutrality (companion cone degenerates).
  Lemma 5.1: inward block moves need no gap. Theorem 5.3 (weakened (H2)/(H3) per block), Theorem 5.4 (infinitely many weak bad peaks).
  Prop 4.1/4.2 (need r*_l > 0 for good l): (O1)(i) only matters for infinitely many carriers; far lowerings f^L lie in R_0^pm or R_S.
  REFEREE: the "band" (T_lo^2 << r_l << 1/n defeats pinning and exactification) is NOT design-independent: an EXPLOSIVE design
  (window function F(l) recursive, F(l+1) >= max{F(l)^2, (l+1)2^{(l+1)^3}, b(l)^{-4(l+1)}}, u(l) = F(l)^{-1/(4l)}) keeps Section 8,
  makes bands pairwise disjoint, so every F-finite f has infinitely many unblocked windows (rooms); then (O1)(i) = Hoffman problem (O2).
Z4 (O2,O3): Theorem A = S_Binf (PROVED for modified design SLD_G with N-independence fix): F finite, infinitely many exactly swallowed,
  non-resonant, non-d-neutral carriers, under (H2'') (referee weakening), (H3), (DR) d-repair, (W_inf). Key: zero-cost cone depends on f
  only through finitely many combinatorial data => Hoffman constant G*(l) is a DESIGN constant absorbed by the ladder; active sets
  U(t) = {lambda_l >= t^2}. Prop 1.2 (p*(f^L - f) = O(eps_L), proof fixed by referee). Cor 5.4: maximal contact recovered for SLD_G
  under growth of margins. Lemma R: without (DR) d-row Hoffman constant ~ 1/c_l. Prop 5.6': non-d-neutral two-piece data need
  sign-coherent far swallowing. Degenerate swallowing-sign peaks: window data exist (Lemma 8.1); engineering via steering is a SKETCH
  under (FS) (free channels: z' at free coordinates and a on F create no base excess, ref Lemma 9.2); open at maximal contact.
Z5 (O4): Remark rem:Binf is now a THEOREM (transfer peaks at a not in c_00 along truncated canonical NA approximants); B*, B±,
  engineered recovery (under cushion compatibility / cushion sparsity (CS)), S extend to infinite F; bounded free switching holds at
  any F (a in Y harmless). Referee Theorem R1: cushion domination replaced by cushion SPARSITY (CS_B). Open at infinite F: off-F room
  decaying too fast; NON-sparse support swallowing (|a_j| ~ v_l(j)^{1+beta}, beta >= 1); infinitely many bad carriers (F = N, a > 0);
  (H2)/(H3-inf) failure; (LSC-trunc) (= infinite-F half of Lemma Z); Theorem thm:onesided at infinite F. Support coordinate at scale t
  = contact of sign sgn a_j + anti-sign allowance 2|a_j|/t growing as t -> 0.
Z6 (stress test): no counterexample. Theorem C (original SLD), Theorem U' (referee-corrected, design D''' N-free), Theorem V
  (d-rigidity: a d-rigid swallowing-type peak needs no margin), Prop P (Farkas pinning: carriers on which every zero-cost exactly
  d-neutral direction vanishes are pinned at O(t) by an LP certificate; in one-signed blocks of size ~1/|q_l| <= 2/Phi_l, a design
  quantity), Cor V.1 (non-rigid swallowing-type peaks only alongside non-rigid q<0 swallowed strict non-peaks), Prop R1 (referee).
  Conjecture G (joint switching bound <= C t/m_u(l) through nearly neutral swallowed non-peaks; numerics support) OPEN.
CONSENSUS OPEN CORE after Round 5 (F finite, g not window-pinned, design D''' / SLD_G / explosive):
 (r) f-dependent RATES decaying faster than any design ladder ("exactness vs scale"): rooms of good signature sets (approximate
     swallowing), margins of non-rigid swallowing-type peaks, relative Farkas constants / d-coefficients of nearly neutral swallowed
     non-peaks (K_nn; Conjecture G would remove), gaps gamma_B of kept q<0 carriers, rooms gamma_T at bad target coordinates;
 (d) degenerate NON-RIGID swallowing-type peaks (need peak-carrying engineering / steering; open at maximal contact);
 (m) mixed blocks neither compensated nor rigid (f-dependent d-row Hoffman constants, failure of (DR));
 (h) failure of (H2''); (O4) infinite F as listed under Z5.
 Window methods for a fixed design absorb only design quantities; the only non-window tool is Z3's Theorem E (companions, cost o(T_lo^2)).

## ADDENDUM 6 (Round 6, all refereed): r6/Y1_*, r6/Y2_*, r6/Y3_*, r6/Y4_* (read *_referee.md first, then notes and ref_notes)
Y1 (refereed CORRECT in all PROVED claims): design D_X = SLD with each window level split into M(l) = omega(l)+1 sub-windows with
  pairwise disjoint bands (b(w), u(w)); Design(l) contains G*(l), H_comb(l), D(l), G**(l) (generalized configuration Hoffman constant,
  arbitrary contact patterns on all coarse targets T(l)), 2^{sigma(l)}, |T(l)|. Admissible, N-free; all of Section 8 and Round-5 window
  theorems hold on sub-windows. Theorem 2 (clean sub-windows, pigeonhole): every F-finite f has at every level a sub-window where every rate
  (room of each signature set on S^nat = S \ (F ∪ T(l)), target rooms, threshold distance |rho-1|, relative position rho) is TINY (<= b)
  or ROBUST (>= u). Lemma T (threshold equation: block threshold theta is the unique root of an explicit equation; raising/Lipschitz bounds;
  a raise rescales every untouched d-coefficient by one common factor). Pinning at clean sub-windows is DIAGONAL (no room products, no
  slaving). Exactifying companion f^#_w (close tiny rooms and target rooms, raise threshold through a DONOR) at cost o(T_lo^2).
  Proposition 5.2 (transplant to exact d-neutral data at f^#_w), Theorem E' (window-dependent c_flat, inward-only coordinates).
  MASTER THEOREM (D_X): F finite; if at infinitely many levels a clean sub-window satisfies (SP_w) shift sources, (Do_w) donors,
  (Cmp_w) each block compensated or one-signed, (NN_w) no uncompensable nearly neutral kept carrier, then f in Rec. NO rate conditions.
  Cor M1 (maximal contact), M2.
Y2 (refereed, strong): status steering is free at a companion (donor = far z-move on an unused signature set raises the threshold,
  turns used degenerate peaks into strict non-peaks, keeps exact d-neutrality). Prop Q / Cor Q' (peak-carrying Cor D1), Theorem P
  (degenerate swallowing-type peaks carried under donor condition (TD_m); always at maximal contact, Cor P.1). Design D^Y; faces of
  configuration cones are free configurations; Prop 4.3 face reduction; Theorem M (mixed blocks without (DR), rate K_F^rel = face-Farkas);
  Theorem H (failure of (H2''): shift-cost pinning c_* > 0); Theorem Y (master theorem for D^Y). Referee: Lemma R-T (target-coordinate
  donors), gap G1 (SLD_G only). OPEN: aligned corner (d'), coherent shift resonance (h'), Conjecture G.
Y3 (refereed): infinite F. Flip-profile calculus (sparse / critical / super-critical: m_beta(x) = sum{beta_j : |a_j| < x beta_j}).
  Theorem 2.1 (T8 with raised support: only one-sided parts need cushion sparsity), Theorem 2.2, un-switching pair (Lemma 3.1), design
  D_sigma (bounded-gap signatures + allowedness rule (c)), Theorem 3.5 (super-critical support swallowing recovered), Theorem 4.1
  (one-sided coefficient at arbitrary F without Gram system), Cor 4.2, Theorem 5.1 = Theorem N (box-dominated support Bx <= C_a|a|, F = N:
  every mate recovered for EVERY admissible T under (SC_I) and a margin rate), Theorem 6.1 (master theorem at infinite F), (LSC-trunc)
  holds wherever exact data exist. Referee: Remark 3.6(b) wrong (corrected), rho-threshold proposition. OPEN: (O4-crit) critical support
  swallowing (model |a_j| ~ v_l(j)^2: fixed data lose the cushion-sharing factor 2 exactly in the self-similar model), (O4-nd), (O4-box).
Y4 (refereed): explosive design vs per-carrier rates (Prop 1.2), pigeonhole design D^PW (Lemma 1.5, Thm 1.6 clean sub-windows; referee
  design fixes u_R, Design incl. 2^{s_max}/delta_min, Q(w)), Lemma 1.8 (ray removal), Lemma 2.3 (Theorem E with BANKED support: growing
  base support inside the contact set), channels/raising lemma. Y4's "directional residual (UN+)" is WRONG: REFEREE (Y4_ref_notes C.2-C.7):
  FAR PULLS at companions (flip a far swallowing contact j in S_l to a tiny opposite-sign support coordinate with mass 24 lambda_l v_l(j):
  lowers that single carrier's value by exactly 2 v_l(j) at first order, cost O(v log 1/v), any base; Lemma U/Thm E accept pulled supports)
  + private banks give two-sided per-carrier exact tuning for a DIAGONAL base U; Cor P5: at every clean sub-window all tiny single-block ray
  d-sums can be made exactly zero at cost o(T_lo^2) (sign-constrained Hoffman solve). Assembly is a SKETCH.
CONSENSUS OPEN CORE after Round 6 (diagonal base U allowed: U is any compact dense-range operator, choose it diagonal):
 (A) ASSEMBLY (SKETCH): one pulled/banked/tuned/donor companion per clean sub-window of a single unified design carrying ALL
     exactifications at once (close rooms and target rooms, raise thresholds, neutralize tiny rays, pull wrong-sign nearly neutral carriers),
     closed under slaving, status stability (BS) under the O(Delta) threshold drift, then transplant (Prop 5.2 / Prop T) and Theorem E'.
     This would remove (NN_w), (Do_w) except the aligned corner, and single-block tiny rays.
 (B) multi-block rays (m'): vector-valued d-rows; exactifying tiny joint objects is determinantal.
 (C) coherent shift resonance (h'): c_*(l) = 0; exact data with Delta d != 0 need sum_m' Delta d_m' R*_m' w_m' z-signed on K.
 (D) aligned corner (d'): no signature donor and no target donor (Lemma R-T); far pulls on the peak itself (SKETCH).
 (E) infinite F: (O4-crit), (O4-nd), (O4-box), plus the finite-F core at infinite F.

## ADDENDUM 7 (Round 7, all refereed): r7/V1_*, r7/V2_*, r7/V3_*, r7/V4_* (read *_referee.md first; *_ref_notes.md prove the fixes)
V1 (all PROVED claims correct, precisions p0-p5): ONE N-free design D_Omega (SLD with bounded-gap S_l = {2^l(2i+1)}, Y3 allowedness (c),
  DIAGONAL base U^*e_j^* = 2^{-j}k_j, Design(l) dominating all earlier design factors, rate scheme (R1)-(R7), M(l) = omega(l)+1 sub-windows,
  Q(w) = (4 Design/u)^{omega+20}). Lemma D: at every clean sub-window every block has a coarse peak with ROBUST margin (alpha-mass counting).
  Lemma DR: a BANK at that peak's own-sign far contact raises its value at first order, all other coarse values only at second order
  (diagonal base essential) -> threshold buffer Lam = T_lo^3 >> drifts T_lo^4/l -> status stability automatic. Lemma TU: exact two-sided
  tuning (pulls + private banks, explicit scalar fixed point). Companion carrying (C1)-(C4) at cost o(T_lo^2); Prop TR (transplant);
  Theorem E'' (banked and pulled supports; banks need not be contacts of f). MASTER THEOREM II: F finite, f in Rec if at infinitely many
  levels a clean sub-window has (SH_w) and (VR_w). Cor AC: the aligned corner (D) is EMPTY for D_Omega.
V2 (all PROVED claims correct, precisions P1-P7): Lemma H (Hoffman constant <= max(1,||A||)^{n-1}/least NONZERO minor), Lemma L
  (Lojasiewicz simultaneous exactification), design D^{V2} (all minors as rate objects, b(w) a design power of T_lo), Theorem B: at every
  clean sub-window all tiny minors are made exactly zero at a companion (pulls + banks), Hoffman constant of the whole exact system
  <= C_f^l Design^2/u: (B) multi-block rays, mixed blocks, K_F^rel, (VR_w), (Cmp_w), (NN_w) are NOT residuals. Theorem C1 (shift dichotomy):
  shift-pinning rate rho^sh is a pigeonhole rate; robust => shift pinned with design u^{-3} constants. Theorems E^>= and E^SC (Theorem E with
  Delta d >= 0 data, or Delta d < 0 with (SC) at companions). Prop C3, C4 (oscillating profiles force shifts), Lemma C5 (fine-tail
  completion, one shift ray). MASTER THEOREM III / III' (D^{V2} on D_Omega, diagonal U, F finite): f in Rec unless at all large levels EVERY
  clean sub-window has rho^sh <= b(w) AND c_pi(w) <= b(w): residual (C*) = near-exact coherent shift resonance. (C*) cannot occur at
  constant-sign maximal contact. Theorem C6 (stable shifted resonance) SKETCH with gaps (C*-1) exact absorption of fine-peak residues on
  finitely many coarse free coordinates, (C*-2) (SC) at companions, (C*-3) exactification of block scalars theta_m, A_m (Jacobian
  rho M/Phi_P^2 > 0 confirmed), (C*-4) shift direction constant along a window's scales with >= 2 shifted blocks, (C*-5) joint fixed point.
V3 (strong; fixes: (ND_B) -> (ND'): a|_F not in span{u_k|_F : k in L_0}): RAISE-TRANSFER Lemma 2.3: a same-sign raise Delta a of a on F
  (lam = q*(a + Delta a)) gives p*(f^# + r h) <= 1 + (p*(f + lam r h) - 1 + 2||U* Delta a||)/lam + p*(L*(w^# - w)); the l_1 raise mass
  cancels against normalisation. Theorem 2.5 (E_RT): windowed recovery through companions with transfer error eps' = o(c_flat^2 (T 2^{-n})^2),
  any F, any admissible T. Design D^mu (diagonal base U k_s = mu_s e_s, mu_s = 2^{-s^2-1}). Theorem RS: support swallowing of ANY profile
  (critical, super-critical, mixed; non-d-neutral carriers, off-F targets) with finitely many bad carriers is recovered under (W*), (H2),
  (H3-inf), (B_fin), (RR) and (ND') for bad strict non-peaks: (O4-crit) settled for D^mu. Theorem A (fixed d-neutral data without cushion
  sparsity). Theorem M_inf (reduction PROVED; transport of Y1/Y2 master theorems to infinite F SKETCH, new rate: VP constants for carrier sets
  growing with the window level). OPEN at infinite F: (E1) mu-thin supports ((RR) fails; exist for every mu), (E2) (O4-box) infinitely many
  bad carriers (scale-free raise), (E3) non-d-neutral fixed data at raised rows ((SC) at f_y), (E4) failure of (ND') and degenerate
  swallowing-sign bad peaks, (E5) transport of the finite-F master theorems (needs VP rates).
V4 (sound): (B), (C), (D) cannot be designed away (explicit self-aligned rows f_SA for every design with (SF*), (Z0)), BUT such rows are
  (BT) and recovered (Cor 3.1, Prop 3.2, Cor 5.7). Prop 5.1: near-threshold carriers are Baire-generic in every fixed-z fibre ((BT) meagre).
  Prop 5.3: (BT) rows dense among F-finite rows (peak-ification PROVED). Theorem 5.6: exact all-negative-Delta d data recovered at F-finite
  rows without dead zones (forces maximal contact). Prop R5 (referee): exact all-negative data exist only on a meagre set, so the exact-data
  route cannot reach generic rows; the decisive F-finite problem is (C*). Lemma 2.6: lacunary profiles exclude critical flip profiles (but
  lose bounded gaps). Design compatibility of V4's conditions with V1/V2 constants: plausible, not checked line by line.
CONSENSUS STATE after Round 7 (design D^{V2} on D_Omega with diagonal base, plus D^mu entries; F finite): Lemma Z holds except at (C*) rows.
  Infinite F: (E1)-(E5). Nothing points to a counterexample.

## ADDENDUM 8 (Round 8, all refereed): r8/U1_*, r8/U2_*, r8/U3_*, r8/U4_* (read *_referee.md first; *_ref_notes.md prove the fixes)
U4 (audit, CORRECT): one operator T_final (recursion with fixed data, stage order: target y_l (allowedness (a),(c)); delta_l by (GM) for
  l >= 2; c_l = min (W1)-(W7); level data and Design(l) incl. B_mu(l) = 2^{sigma(l)}/mu_{sigma(l)}^2; pigeonhole sub-windows with V2's
  Lojasiewicz-adjusted b(w)); diagonal base with super-exponentially decaying entries; N-independent; Martin's Lemma B holds; Lemma GW
  (window theorems use a window only through 4 properties, all valid on every sub-window); every theorem on the dependency trees of Master
  Theorems II, III' and Theorem RS' holds for T_final with two fixes: C1 (B_mu in Design: the base enters a design constant ONLY through the
  bank factor mu_{s'}^2 v(s')), C7 ((GM) only for l >= 2, c_1 = 1). Current master theorem for T_final: (i) F finite: f in Rec_N unless (C*)
  (and not block-tame, not in R_0, R_0^pm, R_S); (ii) F infinite: RS', R1, Y3 Thm 3.5, Thm N, Z5 T6/T7 classes; (iii) residual = (C*) at
  finite F, (E1)-(E5) at infinite F; (iv) density for p_N <=> Lemma Z <=> Rec_N = S_{p_N*} (OPEN for every N); for p: follows from density for
  infinitely many p_N (T_final N-free); row-wise statements do NOT transfer to p.
U2 (infinite F, sound): base mu*_s = 2^{-2^{2^s}} (doubly exponential; B_mu adapts the design); Lemma P (an unraised support coordinate
  that would be deep for the data pins the switching carrier: |tau_l| <= C_q t/v_l(s)); Theorem RS* ((RR) removed: mu-thin supports
  recovered); Lemma ND / Theorem ND' ((ND') removed); Lemma W + Theorem RS*_inf (infinitely many bad carriers under a rate condition
  (W_inf), which must include the bad-peak margin rate 1/mu_B(l)); Lemma DR-inf ((R6) exactly invariant under deep raises); Lemma TR-inf
  (private two-sided value tuning at infinite F in cases a, a', c, c'); Theorem M-inf (transport of MT III' to infinite F) SKETCH; residual:
  tuning regularity modulus (strictly contains (NDN)), degenerate swallowing-sign bad peaks with tiny resource moduli, (SC) transfer along
  the deep raise below eps_e.
U1 ((C*), PARTLY WRONG): Master Theorem IV and Corollary IV.1 (N = 1) are NOT proved: Theorem 2.3 (exactification, C*-3) fails because the
  donor raise moves kappa by ~Lam and the kappa push undoes the raise (all peaks act identically on (theta, A, kappa)). Referee Lemma R-kt:
  the exact shifted system and the relative positions of switching carriers depend on a block only through the ratios u/kappa, so TWO
  independent levers are needed. Master Theorem IV' PROVED under (KN) (a kappa-neutral lever: an inactive Omega carrier with robust relative
  position). Correct new tools: exactness certificate (Lemma 1.1: exact data iff ONE vector V(Domega) is z'-admissible off F'); kappa data
  identity (Delta' kappa' = sum_Omega u gamma); shift bound (Lemma 2.1); normalization of a class's scales onto one shift ray (Prop 2.2);
  zero-value ABSORBER PAIRS (block-1 carriers tuned to value exactly 0 cancel fine residues on coarse coordinates exactly: C*-1 bookkeeping);
  self-aligned recursion giving (SC) for negative blocks (C*-2 in configuration (i)); Schauder completion on one ray (C*-5); mixed-class
  three-state / frustration analysis. Design D^{U1'} (referee-corrected). OPEN: status coherence (sharpened C*-3) without (KN); (C_mix)
  (mixed activity classes, N >= 2).
U3 ((C*) adversarial, structural results correct): Lemma S (exact rigidity / sandwich of two-piece data), Cor S1/S2 (F, K finite: no
  switching, no shift), Prop S3; THEOREM NL: the fibre map is NOT lower semicontinuous at V4's self-aligned (BT) row along (BT) rows (one far
  anti-type flip) — approximants for oscillating mates must be aligned or banked; Prop FZ / Cor FZ (fixed-z tilts of aligned rows leave
  (C*)); nested-tuning rows f^infty (non-(BT), non-(SC), (C*); existence SKETCH, properties PROVED; their exact-data mates recovered);
  Lemma VT (violation tolerance at a single engineered stage: violations of l_1 mass eps cost <= 2 rho |tau| eps, tolerated when
  2 rho eps <= delta s_1/16); Lemma QB2 (quadratic bank repair, fixed accounting); Lemma R-pin. Referee: U3's (S2a) scaling check is WRONG:
  window masses create a first-order theta/+- junction mismatch ~ s_1/t^2; remedy: d-CONSISTENT engineered approximants (re-tune coarse
  omega-carrier values exactly at f' by TU levers so that d' = d on every switching vector) (SKETCH). OPEN: (S1) general exact coupling
  (>= 2 shifted blocks or no free-ray q<0 carrier); (S2) uniform composition ((S2a') d-consistent approximants, (S2b), (S2c)); RT*(c).
CONSENSUS OPEN CORE after Round 8 (T_final; finite I):
 F finite: (C*) rows; sub-problems: status coherence without (KN) (second, kappa-neutral lever), (C_mix) for N >= 2, (S1) multi-block exact
   coupling, (S2) uniform composition with d-consistent engineered approximants.
 F infinite: transport of MT III' (M-inf SKETCH), tuning regularity modulus, (W_inf) rate for infinitely many bad carriers, (SC) along
   deep raises, plus (C*) at infinite F.
