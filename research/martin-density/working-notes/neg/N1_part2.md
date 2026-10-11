# N1 part 2 — The shape of a counterexample for an ARBITRARY admissible T (necessary conditions)

Setting as in part 1. A "counterexample" is (T, I, f, g, rho) with T admissible, I a block set (one finite I = {1..N} suffices
for a negative answer: (c_0, p_N) is then a Banach space X with NA(X, l_2^2) not dense), f in S*, g in C(f), rho in (0,1), and
rho g notin Rec(f) (Theorem 1.3). Throughout, "PROVED" means proved in a refereed source cited, or proved here; G3 (round 14) has been refereed
(r14/G3_referee.md): its Section 2 lemmas, Theorem CL and Lemma 3.1/Cor 3.2 are correct.

## 2.0 A global reformulation (PROVED here)

Let G := {(f, g) in S* x X* : g in C(f)} (the mate graph; closed by [I, thm:compact]) and G_NA := {(f, g) in G : f in NA_1}.
LEMMA 2.1. (a) graph(Rec) = cl G_NA (closure in S* x X*). (b) More generally, if R ⊇ NA_1 is any set of rows with
Rec(f') = C(f') for f' in R, then Rec(f) = Ls_{f' -> f, f' in R} C(f') for every f. (c) NA((X,p), l_2^2) is dense iff
G = cl G_NA, and G \ cl G_NA is relatively open in G.
Proof. (a) is the definition of Rec. (b) Rec(f) ⊆ Ls_R C is clear because NA_1 ⊆ R. Conversely, if f_n in R, g_n in C(f_n) = Rec(f_n), g_n -> g and
f_n -> f, choose by (a) (f'_n, g'_n) in G_NA with p*(f'_n - f_n) + p*(g'_n - g_n) < 1/n; then (f, g) in cl G_NA, i.e. g in Rec(f). (c) Prop 1.2(e)
and Theorem 1.3(iv). QED
So a counterexample is a point where the mate graph JUMPS UP relative to the mate graph over norm-attaining rows — equivalently,
by (b), relative to the mate graph over ANY class of rows already known to be recoverable (Omega, (BT) rows, ...). With
R = Omega (comeager, [I, rem:joint]): rho g notin Ls_{f'' -> f, f'' in Omega} C(f''): the dangerous mate is not a limit of mates
of generic rows. It is an "exceptional mate" of an exceptional row.

## 2.1 Conditions on the first row f

(F1) f is not norm attaining. [I, prop:reduction(d)]. PROVED.
(F2) f is not a point of lower semicontinuity of C. The lsc points form a comeager set Omega (Fort's theorem for the usc
     compact-valued map C [I, thm:compact]; residual uniform recovery theorem of Preprint A, [I, rem:joint]); Omega ⊆ Rec.
     So the bad rows form a MEAGRE set. PROVED.
(F3) (I finite) f does not satisfy (BT) [I, cor:BTrecovered]: either F = supp a is infinite, or some Q_m (strict non-peaks) is
     infinite, or a degenerate peak exists (Dg_m != empty), or margin sparsity (MS) fails. In particular f is not C-tame without
     degenerate peaks [I, thm:tame]. The contact set K is irrelevant for this condition (any K is allowed in (BT)). PROVED.
     Remark (V4 Prop 5.1, refereed): (BT) is meagre in every fixed-z fibre (near-threshold carriers are Baire generic), so (F3)
     is a weak restriction: violating (BT) is the generic situation, not an exceptional one.
(F4) (F = N) f does not satisfy (BD) + (SC_I) + (W_M) of [II, thm:II-N] (box-dominated support). PROVED.
(F5) Openness (Theorem 1.3(iv), G3 Lemma 3.1): there is delta' > 0 such that every (f'', h'') in G with p*(f''-f) + p*(h''-rho g)
     < delta' is again non-recovered. In particular rho g keeps distance >= delta'/2 from C(f'') for EVERY recoverable row f'' in
     B(f, delta'/2): all NA rows, all rows of Omega, all (BT) rows, and (for the designed T_fin of Part III) all rows with finite
     base support. PROVED.
(F6) f is not reached by transitivity [I, thm:transitivity]: there is no sequence of recoverable rows f_n -> f with
     liminf r~_{f_n} >= rho' r~_f (all rho' < 1) on a dense set; by Lemma 2.1(b) the sharp form is rho g notin
     Ls_{f'->f, f' in R} C(f') for every recoverable class R. PROVED.
(F7) For the designed operators: for T_fin (Part III, Master Theorem VI, two independent passes) every first row with finite base
     support is recoverable for every N, and density for p_N <=> (LSC-trunc)_N. A counterexample for T_fin must therefore have
     F INFINITE and violate (LSC-trunc)_N at (f, g, rho). For a NEGATIVE answer one should not use T_fin: one admissible T suffices,
     and an adversarial T (without signatures, ladders, generic weights or diagonal base) avoids all of Parts II-III. PROVED
     (as a consequence of Part III) / methodological remark.

## 2.2 Conditions on the mate g (any admissible T)

(M1) rho g notin U(f) ⊇ cl Cert^sh(f) (Prop 1.2(b)). This excludes, with their closures: finite certificates [I, thm:transport],
     shifted certificates [I, thm:shifted], weighted directions with H <= 1 [I, thm:weighted], locally split mates and
     split-contractive operators (I finite) [I, thm:locsplit, cor:splitcontractive], carrier mates with non-summable gaps
     [I, thm:carriers], and the ladder/averaging class [I, cor:ladder]. PROVED.
(M2) (Quantitative contrapositive of [I, cor:ladder] and [I, cor:decomposition], I finite.) For all c_0 > 0, kappa_1, K < infinity
     there are arbitrarily small t > 0 such that for NEITHER tau = t NOR tau = -t does f + tau g admit a decomposition
       f + tau g = (a + tau b_t + tau e_t) + sum_m R_m^*((1 - d_{t,m} tau) w_m + tau omega_{t,m})
     with c_t = (b_t, omega_t) a finite certificate, r(c_t) >= c_0 t, kappa(c_t) <= kappa_1, p*(e_t) <= K t and all component norms
     <= s(tau) + o(tau^2). PROVED (contrapositive; since g notin cl Cert(f) by (M1)).
     READING: at a cofinal set of small scales, on BOTH sides of t = 0, every near-optimal decomposition of f +- t g uses resources
     outside the format "finite two-sided certificate + O(t)": base mass >> t off F (contacts / near-contacts used one-sidedly),
     support coordinates used beyond their cushion (|b_j| > |a_j|/(c_0 t): near-flips), peaks used other than through the common
     shift d_m w_m, strict non-peaks used beyond their radius (near-threshold use: gap_m(k) < 2 c_0 t |omega(k)|), or an infinite
     tail of carriers of l_1-mass >> t.
(M3) If a in c_00: g notin K(f) := cl conv(Cert^sh(f) ∪ B(f)), B(f) = balanced finite certificates with Gamma_w <= 1
     [I, prop:intrinsic(c), thm:transfer]. For arbitrary F: g is not a balanced finite certificate with ||b/a||_inf < infinity
     and Gamma_w <= 1 [II, thm:II-transferinf]. PROVED.
(M4) Two-piece data. If F is finite: g carries NO two-piece data with kappa_w <= 1 and (Delta d_m >= 0 for all m [I, cor:D1], or
     I_- := {m : Delta d_m < 0} satisfying (SC) [I, thm:engineered]); no hypothesis on K, Q_m or rates of T is involved. If F is
     infinite: no such data satisfying (CS-side) [II, thm:II-raised] or rho^2 kappa^fl < 1 [II, thm:II-flipext]. Since Rec(f) is
     closed, rho g is also not a limit of such mates. PROVED.
     Hence, by [I, thm:onesided(c)] (every mate at a (BT) row has two-piece data with kappa_w <= 1), the dangerous mate must
     exploit the failure of (BT) in (F3): its one-sided decompositions need infinitely many carriers, degenerate or
     near-threshold carriers, or flips of an infinite support.
(M5) Windowed recovery through nearby rows (Theorem E family, any admissible T) [II, thm:II-E, thm:II-ERT]: g is not recovered
     through rows f_j -> f carrying (exact d-neutral two-piece, or transfer-error) window data whose transfer error is
     o(c_j^2 (T_j 2^{-n_j})^2). In words: near f there are no rows at which g has EXACT window data that are second-order close
     to f relative to the window bottom. PROVED (as the contrapositive).
(M6) Linear decompositions and exact resonances. If F ∪ K is finite, g has no two-sided decompositions linear in t on
     [-tau, tau] [I, cor:twosided]. In general, any pair of t-linear decompositions has switching vector D = B_+ - B_- in Y that is,
     off F, supported in K and z-signed [I, prop:exact]: EXACT (scale-free) switching needs infinitely many contacts (or near-flips
     of an infinite support). The explicit exact-resonance mates of [I, thm:defect] are recovered [I, cor:exampleRecovered], and
     every d-neutral exact two-piece switching mate is recovered (P2A/N2 Thm 1, Round 2, refereed; contained in [I, cor:D1]).
     PROVED. So the switching of the dangerous mate must be scale-dependent ("approximate resonance") or not of two-piece type.
(M7) Universal scale-t constraints on EVERY decomposition of EVERY mate (G3 Section 2; PROVED, G3 refereed correct): for decompositions
     f +- t g = A_+- + L^*W_+- with component norms <= s(t), B_+- := +-(A_+- - a)/t and switching vector V := B_+ - B_- in Y:
       |V(zhat)| <= t/q_0;   sum_{j notin F} (z_j V_j)_- <= t/(2 q_0);   sum_{j notin F} (1 - |z_j|)|V_j| <= t/q_0;
     and the conservation law (Theorem CL): for any T_th ⊂ F, ||V 1_{N}||_1 <= - sum_{s in T_th} zhat_s V_s + |<V 1_N, h>| + 3t/q_0
     + 4 alpha(N ∩ F)/t, N := complement of T_th. These are properties of all mates (not specific to counterexamples): they say that
     switching off F is one-signed (z-signed) up to O(t) and must be paid by the support F.
(M8) Sign rule (P1, refereed; [I, rem:resonancetypes]): exact or o(Phi)-perturbed cross-block near-duplicates (built into Lemma B's
     construction) serve the same side of t = 0 and cannot switch with each other. So Martin's built-in near-duplicates do not by
     themselves produce switching. PROVED (P1) / HEURISTIC guide (Part I).

## 2.3 Conditions on the operator T (HEURISTIC / model level; Rounds 1-3)

(T1) Rates. For "generic" T (far parts of distinct carriers quantitatively independent) the approximant can convert unboundedly
     many adjacent scales through far moves (E Cor 6.2, PROVED; E 8.3, SKETCH), and averaging then recovers (E Model N: R(J) -> 1).
     A counterexample needs an ADVERSARIAL T: error-dominated carriers (approximation errors >> Phi at the carrier's own depth),
     FAR RIGIDITY (far tails nearly collinear inside long detector groups; compatible with Lemma B: N2 4.5, SKETCH). HEURISTIC.
(T2) Non-compact errors (R3 5.1, the residual class O3*): by R3 Theorem EC (PROVED, any admissible T) every FIXED
     finite-dimensional family of O(scale) errors is carried by generic tail coordinates turned into exact zero-weight strict
     non-peaks by o(1) window moves. A counterexample needs, at every candidate boundary scale: (R1) escaping errors of critical
     size, (R2) no early generic approximants of the escaping directions, (R3) concentration on few coordinates guarded by matched
     carriers, (R4) no private handles, (R5) recursive guarding, plus (A1) near-threshold one-sided carriers of both peak types at all
     scales (a fixed point between T and f, constructed nowhere). HEURISTIC/OPEN.
(T3) Chain guards give unbounded conversion capacity except possibly for ALTERNATING types at ratio c = 1 (R3 5.2, SKETCH in a
     linear status model; referee: bounded only with constant targets). This is the most specific adversarial configuration known.
     SKETCH.

## 2.4 Self-similarity (what persists across scales)

(S1) By Lemma 1.4 the approximant chooses the window W and all far data freely; by Prop 1.8 only scales < t_*(eps, eta, rho) are
     decisive; hence the obstruction must reappear below EVERY window: it cannot be carried by finitely many coordinates or
     carriers. PROVED (as a reformulation).
(S2) For the designed T, persistent residual rows need a FRESH pinned wrong-signed resonance at every main stage (H2 Thm H2.B,
     refereed), and the persistent residual is of exact/bias type (G3 5.3, SKETCH); G3 Cor 3.2 (PROVED, refereed): a
     counterexample is a property of the PAIR (f, g) — rows with active mates near rho g force their own resonances.
     For arbitrary T the analogue is (T2)(R5). HEURISTIC for arbitrary T.

## 2.5 Summary table (arbitrary admissible T, I finite unless noted)

| # | Necessary condition on a counterexample (T, f, g, rho) | Source | Status |
|---|---|---|---|
| F1 | f not norm attaining | I prop:reduction(d) | PROVED |
| F2 | f outside the comeager set Omega of lsc points (bad rows are meagre) | Fort / PrA, I rem:joint | PROVED |
| F3 | f not (BT): F infinite, or some Q_m infinite, or degenerate peaks, or (MS) fails | I cor:BTrecovered | PROVED |
| F4 | if F = N: not (BD)+(SC_I)+(W_M) | II thm:II-N | PROVED |
| F5 | rho g uniformly far from C(f'') for all recoverable f'' near f; defect open on the graph | Thm 1.3(iv), G3 L3.1 | PROVED |
| F6 | rho g notin Ls over any recoverable class (Omega, (BT), NA) | Lemma 2.1(b) | PROVED |
| F7 | for T_fin: F infinite and (LSC-trunc)_N fails | III MT VI, Thm VI.2 | PROVED (Part III) |
| M1 | rho g notin U(f) ⊇ cl Cert^sh(f) (certificates, shifted, weighted, locally split, ladder, carriers) | I Sec 3-4 | PROVED |
| M2 | at cofinal small scales, on both sides, no "certificate + O(t)" decomposition | I cor:decomposition | PROVED |
| M3 | not in K(f) (a in c_00); not a balanced certificate with Gamma_w <= 1 (any F) | I thm:transfer, II thm:II-transferinf | PROVED |
| M4 | no two-piece data with kappa_w <= 1 and (Delta d >= 0 or (SC)); infinite F: no (CS-side)/flip-extended data | I cor:D1, thm:engineered; II raised/flipext | PROVED |
| M5 | no exact window data at second-order-close nearby rows | II thm:II-E, II-ERT | PROVED |
| M6 | switching scale-dependent (exact resonances recovered; exact switching needs infinite F ∪ K) | I prop:exact, cor:twosided, cor:exampleRecovered | PROVED |
| M7 | switching z-signed off F up to O(t); conservation law | G3 Sec 2 | PROVED (G3, refereed) |
| M8 | cross-block near-duplicates cannot switch with each other | P1 sign rule | PROVED |
| T1 | adversarial T: error-dominated carriers, far rigidity | E, N2 4.5 | HEURISTIC / SKETCH |
| T2 | escaping, concentrated, recursively guarded critical errors (O3*) at every boundary | R3 5.1 | HEURISTIC / OPEN |
| T3 | chain guards of alternating type at ratio 1 | R3 5.2 | SKETCH |
| S1 | obstruction must reappear below every window | Lemma 1.4, Prop 1.8 | PROVED (reformulation) |
| S2 | fresh resonance at every stage; obstruction is a property of the pair | H2.B (designed T), G3 3.2 | PROVED (designed) / HEURISTIC (arbitrary) |

What is NOT a necessary condition (to avoid false leads): an infinite contact set K is not required by the proved results
(F3 allows any K; rows with F ∪ K finite but infinitely many near-threshold carriers are open); infinite F is not required for an
arbitrary T (it is required only for T_fin); the d-mismatch sign is not decisive by itself (Delta d < 0 is open only without (SC)).
