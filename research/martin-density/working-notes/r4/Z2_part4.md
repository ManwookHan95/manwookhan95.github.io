# Z2 part 4: the hard cases of task (a) — mate fibres and status of Lemma Z

Setting: SLD T, p = p_N; F = supp a; K = {j notin F : |z_j| = 1}. "R" = recovered first rows. Known members of R now:
NA ∩ S (trivially), Omega (Preprint A; residual), (BT) points (S3 Cor D2, any K), R_0 ⊂ R_0^± (G3 Thm B, part 1 Thm B±), R_S (part 3 Thm S).
Lemma Z is needed only OUTSIDE their union.

## 4.1 Proposition (structure of switching at contacts; any admissible T). PROVED.
For g in C(f), t <= t_eta and any two-sided decomposition at scale t:
 (a) (one-sided contact usage) sum_{j in K} (z_j B_+(j))_- <= t/(4q_0), sum_{j in K} (z_j B_-(j))_+ <= t/(4q_0); off F cup K: sum (1 - |z_j|)(|B_+(j)| + |B_-(j)|) <= t/q_0.
 (b) (z-order sandwich) For j in K: z_j (g - L*Omega_+)(j) >= -eps^+_j and z_j (g - L*Omega_-)(j) <= eps^-_j with sum (eps^+ + eps^-) <= t/(2q_0).
     I.e. on the contact set the mate is squeezed, in the order defined by z, between the off-F traces of the two block perturbations.
 (c) (switching budget) sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0 (part 1, (1.2.1)): the block switching -sum Delta c_k u_k must be z-signed on K and vanish
     elsewhere off F, up to l_1-mass O(t).
*Proof.* (a) G3 2.3(b) with phi_z(x) = 2(z x)_- (resp. 2(zx)_+ for -z) when |z| = 1, and phi_z(x) >= (1 - |z|)|x|. (b) B_+- = g - L*Omega_+- and (a). (c) part 1. QED.

## 4.2 Case (a1): F finite, contact set cofinite (|z_j| = 1 for all j notin F; J_gamma empty for every gamma)
 * Mate fibre: by 4.1, on K = F^c the + side may add any z-signed base vector at no first-order cost and the - side any (-z)-signed one; mates are
   z-order sandwiches (4.1(b)) between block traces. The fibre is large: e.g. for every j notin F and every carrier l with target y_l = e_j*/q*(e_j*) and
   z_j = +1 on supp u_l \ F, the vector beta e_j* - beta' a (beta' := beta/q_0 z... normalised so that g(xi) = 0) is a mate for 0 < beta <~ sqrt(lambda_l) (the + side
   uses base only, the - side uses carrier l with base compensation -(beta q*(e_j*) n_l) delta_l h_l/n_l <= 0 in the z-order). (HEURISTIC computation; not used.)
 * Status (PROVED unless stated):
   - z sign-mixed on the signature sets with room theta_l satisfying (W±): f in R_0^± ⊂ R (Thm B±). This covers every z that is not "almost
     constant" on the v_l-mass of the S_l (e.g. alternating along each S_l with bounded first gaps).
   - z constant (= sigma_l) on S_l \ F for l in a set B, sign-mixed (with (W*)) on the others:
       B finite: f in R under (H4), (H5) (Thm S_fin). No resonance or d-neutrality is needed: non-d-neutral and non-resonant switching directions are
       pinned (Lemma 2.6, Hoffman bound 3.2).
       B infinite: f in R if every l in B is resonant and d-neutral and (H3), (H4) hold (Thm S_inf).
   - z constant on infinitely many S_l with infinitely many non-resonant or non-d-neutral swallowed carriers, in particular the MAXIMAL-CONTACT
     first rows z == sigma off F: OPEN. Here every carrier is swallowed (B = everything), a carrier is resonant iff sigma y_l >= 0 off F, and since every
     target recurs infinitely often, infinitely many swallowed carriers are non-resonant. The free cone {tau >= 0 : sum tau_l u_l is sigma-signed off F}
     is a polyhedral cone in each window, but the Hoffman constants of these systems involve the values v_l(s) at the finitely many points
     s in S_l cap supp y_{l'} (which allowedness (b) forces to be ~ sqrt(c_{l'}) small) and the d-coefficients a_l ~ Phi_l; neither is controlled by the
     window slack 2^{l^3} Lambda°(l) (part 3, 3.6(c)). The Hoffman constants of the cone part are DESIGN quantities (they depend on F cap J_L, z|J_L only
     through finitely many sign patterns), so a redesigned ladder could absorb them; the d-neutrality coefficients depend continuously on f and
     cannot be absorbed this way. (HEURISTIC assessment.)
 * Lemma Z in case (a1): holds trivially where f is already in R; OPEN for maximal contact. No counterexample mechanism is visible: by part 5.3
   a counterexample would need the set of first rows near f carrying a mate near rho g to be MEAGRE; maximal contact is itself a closed nowhere dense
   condition, so this is not excluded, but every explicit mate we can write at maximal contact is a superposition of finitely-generated switchings
   (each recovered by Thm S-type arguments) plus certificate parts. (HEURISTIC.)

## 4.3 Case (a2): near-contacts swallow every signature set (|z_s| -> 1 on every S_l; J_gamma cap S_l small for each fixed gamma)
 * Here B(f) is empty (theta_l > 0 for all l unless z is exactly constant on some S_l \ F), and the switching amplitude through carrier l at scale t is
   bounded by (t/q_0 + interference)/theta_l (part 1, 1.4): carrier l is pinned at scales t << theta_l and "almost free" at scales t >> theta_l.
   This is genuinely scale-dependent switching (open-core item O3) — but with an explicit, carrier-by-carrier transition scale theta_l.
 * Status: f in R_0^± ⊂ R whenever prod_{l' <= l}(delta°_{l'}/theta_{l'}) = o(l 2^{l^3}) along a subsequence (Thm B±), in particular whenever
   theta_l/delta°_l >= vartheta^l (geometric decay; no fixed gamma needed, contrary to G3's (SR)). If the relative rooms decay faster than allowed by
   the window slack: OPEN. Theorem S does not apply (no exact resonance: the wrong-sign mass of the switching vector is O(t) but not zero, and S3 Cor D1
   needs EXACT two-piece data). Any design with longer windows moves the threshold but cannot remove it (f is chosen after T).
 * Lemma Z here: the natural approximants are "sharpenings" (make the near-swallowed far sets exactly monochromatic, landing in Thm S's class if the
   swallowed carriers are resonant and d-neutral) or "far lowerings" (another agent). Both require mate transfer across the transition band
   t ~ theta_l; OPEN.

## 4.4 Case (a3): infinite base support F, sign flips ("cushions")
**Proposition 4.4 (cushion structure; any admissible T). PROVED.** For g in C(f), t <= t_eta:
   sum_{j in F} ( -sign(a_j) B_+(j) - |a_j|/t )_+ <= t/(4 q_0),     sum_{j in F} ( sign(a_j) B_-(j) - |a_j|/t )_+ <= t/(4 q_0).
*Proof.* A Lemma 7.2: E_q(a + tB) >= Fl_B(t) = sum_{j in F} 2(-sign(a_j) t B_j - |a_j|)_+; budget q_0 E_q <= t^2/2 (A Lemma 7.1); same with -t, B_-. QED.
Meaning: at scale t a support coordinate j is TWO-SIDED free inside its cushion |t B_j| <= |a_j| and behaves like a contact with z_j = sign a_j beyond it.
The effective contact set at scale t is K_t := K cup {j in F : |a_j| <~ t |B_j|}; since a in l_1, every scale has infinitely many cushion-exceeding
coordinates, but their signature mass on S_l tends to 0 with t.
 * Mate fibre: switching through a carrier l whose signature lies in F is two-sided (hence harmless) inside the cushions and one-sided (contact-like,
   resonant if sign a is constant on S_l) outside; the one-sided content at scale t is <= |Delta c_l| v_l({s in S_l : |a_s| < C t}) + O(t).
   If |a_s| >= 2^{-s/2} on S_l (support decaying more slowly than the signature weights), v_l({|a_s| < Ct}) <= delta_l (Ct)^2, so the one-sided
   content is O(lambda_l t) — small without any pinning (HEURISTIC consequence; the block one-sided usage still needs control, see below).
 * Status:
   - generic f (Preprint A Prop: a residual set Omega_0 ⊂ Omega has infinite F; generically supp a = N): in R by Preprint A. PROVED (import).
   - F infinite with room (SR)/(SR±) on S_l \ F: G3 6.3(e) SKETCH, referee "plausible"; Thm B± extends in the same way (SKETCH): only part 1's E^±_l is
     computed on S_l \ F, and the flip analysis of the referee is unchanged.
   - Full support (F = N, so K empty) with no room anywhere: neither G3 (no room) nor Thm S (needs F finite: S3 Cor D1 is for F finite) applies.
     The block one-sided usage (peaks, beyond-clamp non-peaks) is bounded in G3 by pinned two-sided differences; here block switching can be absorbed by
     in-cushion base mass on both sides, so it is NOT pinned and a different control (second-order rebalancing inside cushions) would be needed. OPEN,
     although such f are generically in R (Baire).

## 4.5 Summary of (a)
| Hard case | Status | Where |
|---|---|---|
| K cofinite, z sign-mixed on signatures (W±) | in R (PROVED) | Thm B± (part 1) |
| finitely many exactly swallowed S_l (any K, any blocks), (H4),(H5),(W*) | in R (PROVED) | Thm S_fin (part 3) |
| infinitely many exactly swallowed S_l, all resonant d-neutral, (H3),(H4),(W*) | in R (PROVED) | Thm S_inf (part 3) |
| maximal contact z == sigma off F; generic infinite swallowing | OPEN (obstruction: uncontrolled Hoffman/d-neutralisation constants) | 4.2 |
| near-contacts swallowing with geometric room decay | in R (PROVED) | Thm B± |
| near-contacts with super-fast room decay | OPEN | 4.3 |
| infinite F: generic | in R (PROVED, import) | Preprint A |
| infinite F with room off F | SKETCH | G3 6.3(e), 4.4 |
| full support, no room | OPEN | 4.4 |
No counterexample to Lemma Z was found; in every case where the mate structure could be analysed completely, the mates were recovered
WITHOUT moving f (Thms B±, S). Nothing suggests that Lemma Z fails.
