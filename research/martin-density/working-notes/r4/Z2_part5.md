# Z2 part 5: the alternative routes (b)(i)-(iii) — what they give and why they do not close Lemma Z by themselves

## 5.1 Route (b)(i): modifying the design
**Proposition 5.1 (swallowing is design-independent). PROVED.**
(a) For EVERY admissible T, every N, every finite F ⊂ N, every a in S_{q*} with supp a = F and every carrier (k,m), m <= N, with u := u_{k,m} not supported in F,
there is f in S_{p_N*} with base a at which this carrier is RESONANT: put z_j := sign u(j) for j in supp u \ F, z_j := sign a_j on F, z_j := 0 elsewhere,
and build f from (a, z) (G3 referee 3.3: zhat = z + Ue, q_0 = 1/(1 + sum_m |R_m** zhat|_m), xi = q_0 zhat, w_m = J_m(R_m** xi), f = a + L*w).
Then phi_{z_j}(-u(j)) ... more precisely the base cost of the switching Delta B = c u 1_{F^c} vanishes for c >= 0: sum_{j notin F} phi_{z_j}(c u(j)) = 0.
So no design gives first-order base control of every carrier at every F-finite first row.
(b) For the SLD design (and any design with private signature sets): z := sigma on every S_l \ F (one constant sign) swallows ALL signature sets
at once; with z == +1 off F, a swallowed carrier is resonant iff y_l >= 0 off F, and infinitely many carriers are non-resonant (each target y^(i)
recurs at infinitely many ladder positions of every block — G3 Thm A's density argument — and the dense target set contains vectors with negative
entries off any finite F).
(c) Two-colour signatures (u_l = (y_l + delta_l(h_l^+ - h_l^-))/n_l on disjoint S_l^+, S_l^-) make z == const roomy, but z := sigma_l(1_{S_l^+} - 1_{S_l^-})
on each S_l swallows every carrier again; several signature sets per carrier, or signatures at different densities, are swallowed by a z matching
each of them. (Same argument as (a).)
*Proof.* (a) z in B_{l_inf}, z = sign a on F, so the construction gives f in S_{p*} with base a and normer xi = q_0 zhat (G3 referee 3.3).
For j notin F with u(j) != 0: c u(j) has sign z_j, so phi_{z_j}(c u(j)) = |c u(j)| - z_j c u(j) = 0. (b), (c): immediate from the definitions. QED.
Consequence: route (b)(i) cannot make the bad set empty. What a design CAN influence is only the fine structure of the resonances (which targets are
resonant at which z); Theorem S shows that FINITELY generated resonances are harmless anyway, so the design question reduces to infinitely generated
ones (maximal contact, 4.2), where the obstruction is the size of Hoffman/d-neutralisation constants, partly design-controlled (HEURISTIC, 4.2).
The modification "signatures that are two-sided because they meet supp a" is counter-productive: base coordinates in F are two-sided free inside
their cushions (4.4), so they give NO pinning at small scales.

## 5.2 Route (b)(ii): lower-limit transitivity / certificate form of Lemma Z
**Proposition 5.2 (design-free certificate form of Lemma Z). PROVED.** Let T be ANY admissible operator. Suppose (Lemma Z_cert): for every f in S_{p*},
g in C(f), rho < 1, eps > 0 there are f' in S_{p*} with F' = supp a' finite and p*(f' - f) < eps, and g' in C(f') with p*(g' - rho g) < eps, such that g' is
either (alpha) g_c for a balanced finite certificate c at f' with Gamma_w(c) <= 1 (C Def 7.0), or (beta) carries two-piece data at f' (P2A 1.6) with
Delta d_m >= 0 in every block and kappa_w <= 1. Then NA((c_0, p_N), l_2^2) is dense. For the SLD operator the converse also holds.
*Proof.* (=>density) C Thm 7.4 (case alpha; a' in c_00) or S3 Cor D1 (case beta) give g' in Ls(f'), i.e. (f', rho' g') in cl NA for rho' < 1; let eps -> 0, rho' -> 1
and use closedness of cl NA and A Prop 2.1. (Converse for SLD) Density gives NA approximants (G3 Thm C (=>)); NA points lie in R_0, where every mate
is a norm limit of Gamma_w <= 1 certificate mates (G3 Cor 6.4 / 5.2: the averaged certificates rho g_c are in C(f') and converge to rho g'). QED.
Remarks. (1) Lemma Z_cert removes the dependence on the class R_0 (and on the design) from the target statement; it asks for an explicit
construction at a nearby F-finite first row. (2) HEURISTIC "scale tension" (why a windowed averaging AT an approximant does not suffice for switching
mates): converting one-sided contact usage of size U at radius r into two-sided usage at f' needs base cushions (window masses) of size ~ r U, i.e.
p*(f' - f) >~ r U, while the rho-slack at radius r is only (1 - rho^2) r^2/2; windowed averaging needs certificates at radii far below the slack scale,
so it works only if U = O(r), i.e. in the pinned regime. Switching mates (U ~ 1) need EXACT structure at f' at all small scales: this is what S3 Cor D1
supplies internally, and why Theorem S keeps the switching inside two-piece data instead of averaging it away. (3) Transitivity with
f_n in R and liminf r~_{f_n} >= rho r~_f is equivalent to Lemma Z with approximants in R (A_notes 3.5 / BRIEFING R3); Theorems B±, S enlarge R and
thereby the admissible approximants, but give no new sequence f_n -> f for f outside R.

## 5.3 Route (b)(iii): the residual set Omega
**Proposition 5.3. PROVED.**
 (a) R ⊇ Omega ∪ R_0^± ∪ R_S ∪ BT ∪ (NA ∩ S_{p*}), with Omega comeagre in S_{p*} (Preprint A) — so S_{p*} \ R is meagre.
 (b) {f in S_{p*} : supp a finite} is meagre (Preprint A, Prop "nonvacuity": it lies in the union of the compact sets F_n); hence R_0, R_0^±, R_S, BT and
     NA ∩ S are meagre, Omega ∩ R_0 is meagre, and the residual subset Omega_0 ⊂ Omega consists of first rows with INFINITE base support. Intersecting Omega
     with R_0 ("route (iii)") therefore produces nothing beyond Omega itself; the two recovery mechanisms (Baire continuity, signature pinning)
     live on complementary-category sets.
 (c) (Baire reformulation of a counterexample.) For f, g in C(f), rho < 1 and eps > 0 let
       A_eps := { f' in S_{p*} : p*(f' - f) < eps, dist(rho g, C(f')) < eps }.
     If (f, rho g) is NOT in cl NA((c_0,p), l_2^2), then for some eps > 0 the set A_eps is MEAGRE (indeed A_eps ∩ R = empty). Equivalently: if for every eps
     the set A_eps is non-meagre, then (f, rho g) is in cl NA.
*Proof.* (a), (b): imports cited and part 1/3. (c) If A_eps ∩ R contains some f', then (f', rho' g') in cl NA for a g' in C(f') with p*(g' - rho g) < eps and all rho' < 1
(f' in R); letting eps -> 0, rho' -> 1 gives (f, rho g) in cl NA (closedness). So a counterexample has A_eps ∩ R = empty for small eps, hence
A_eps ⊂ S \ R ⊂ S \ Omega, which is meagre. QED.
Meaning (for scepticism about counterexamples): a non-recoverable mate rho g at f must be destroyed (up to eps) by a GENERIC small perturbation of f: the
first rows near f that keep a mate near rho g form a meagre set. All explicit hard structures met so far are of this kind (exact swallowing,
exact resonance, super-fast room decay are closed nowhere dense conditions), so (c) does not exclude them — but Theorems B± and S show that the
exact ones are nevertheless recovered. (c) also shows that the topological routes alone cannot decide Lemma Z: at f outside Omega, C may be
discontinuous, and only structure (pinning, two-piece data) tells whether rho g survives on a non-meagre set or is recovered otherwise.

## 5.4 Relation to far lowering (the other agent's route)
At f in R_S (finitely generated exact resonances) far lowering is unnecessary: f itself is in R. Far lowering at such f would create a tiny room
theta' on the swallowed set and force mates of f' below the transition scale ~theta' to be pinned; Theorem S shows the switching can instead be kept
and recovered through S3's engineering. For the remaining OPEN classes (maximal contact with infinitely many exceptional swallowed carriers;
super-fast room decay; full support without room) the candidate approximants are: far lowering / far flipping (create room), far SHARPENING
(make near-swallowed far sets exactly monochromatic, moving f toward the R_S class when the swallowed carriers are resonant and d-neutral), and
cushion engineering for full support. All three need a mate transfer across a transition band; none is carried out here (OPEN).
