# N1 referee, part 1: Section 1 of N1_notes.md (Prop 1.2 - Thm 1.9, Lemma 2.1)

Referee: adversarial pass on N1 (track "should the answer be negative?"). Every proof below was re-derived from the
cited statements of Part I (paper/martin_density_note.tex: prop:forced, prop:smooth, prop:continuity,
prop:approximants, prop:reduction, prop:primal, lem:pair, thm:compact, thm:lowerlimit, cor:finite, thm:transitivity,
rem:joint, lem:slack, prop:intrinsic, thm:shifted), which I re-read for this purpose.

## Prop 1.2 (structure of Rec(f)) -- CORRECT
(a) Rec(f) subset C(f): if g_n in C(f_n), f_n -> f, g_n -> g then p*(f + t g) = lim p*(f_n + t g_n) <= s(t). Closedness:
diagonal argument as written. Balanced: C(f_n) convex, symmetric, contains 0. Compact: closed subset of the norm compact C(f).
(b) Blaschke selection in the hyperspace of the compact set C(f) u U_n C(f_n) (thm:compact) is legitimate; Hausdorff limits
of compact convex symmetric sets are compact convex symmetric; U(f) subset A for every A in A(f) because A is the Hausdorff
limit along an NA sequence and U(f) is the inner limit along ALL sequences. A(f) nonempty by Bishop-Phelps + Blaschke.
PRECISION P-2: "cl Cert^sh(f) subset U(f)" should be cited from thm:shifted (Section 3 of Part I, valid for every block
set I by rem:blocks), not from prop:intrinsic(c), which sits in Section 6 where I is finite. Also note (used later) that
U(f) is closed and convex (an intersection of lower limits of convex sets).
(c) Both inequalities re-derived. For ">=": choose f_n in NA_1 with p*(f_n - f) < 1/n and
dist(h, C(f_n)) < inf_{B(f,1/n)} + 1/n; the infima increase to Ob(f,h), so dist(h, C(f_n)) -> Ob(f,h); nearest points
g_n in C(f_n) have a convergent subsequence (thm:compact) with limit in Rec(f).
(d) rho = 0 by Bishop-Phelps; rho in (0,1) is lem:pair (whose converse direction uses rho < 1 to force the norming
directions y_k -> e_1). "ρg in Li C(f_n) for some NA sequence <=> ρg in Rec(f)" by nearest points. Last sentence: the
operator-norm distance of (f_n, g_n) to (f, g) is <= p*(f_n - f) + p*(g_n - g).
(e) "<=": rho g in C(f) = Rec(f) and (d); "=>": (d) and closedness. Also checked: Part I's set Rec of rows
(def:recovery) equals {f : Rec(f) = C(f)} (both directions follow from (d) and closedness), so the two notions agree.

## Theorem 1.3 -- CORRECT
All four equivalences re-derived; the Lipschitz estimate Ob(f, rho g) >= Ob(f, g) - (1-rho) p*(g) is the 1-Lipschitz
property of a distance function. PRECISION P-4: (iv) ("the defect is open on the graph") is automatic: by Lemma 2.1(a)
graph(Rec) = cl G_NA is closed, so G \ graph(Rec) is relatively open in G. It carries no information beyond
closedness of the graph; the operator-ball proof given is also correct.

## Lemma 1.4 (far freedom, uniform form) -- CORRECT, with two precisions
Proof by contradiction via prop:approximants (ii)=>(i) re-checked: the hypotheses of that proposition (a'_n in c_00 and in
S_{q*}, a'_n -> a in l_1, z'_n in c_0, |z'_n| <= 1, z'_n = sgn a'_n on supp a'_n, z'_n -> z coordinatewise) are exactly
what the contradiction sequence satisfies.
PRECISION P-1a (two-sided form; needed for the word "exactly" in Section 0 (1) and in the text after Lemma 1.4).
The lemma as proved is only the "if" direction. The converse uniform statement also holds and should be added:
 LEMMA 1.4' (PROVED here). For every eta > 0 and W there is delta_0 > 0 such that every f' in NA_1 with
 p*(f' - f) < delta_0 has forced data (a', z') with ||a' - a||_1 < eta and |z'_j - z_j| < eta for j <= W.
 Proof. Otherwise there are f'_n in NA_1, f'_n -> f, violating the conclusion; by prop:approximants (i)=>(ii)
 (via prop:continuity) a'_n -> a in l_1 and z'_n -> z weak*, i.e. coordinatewise; contradiction. QED
So the NA rows near f are EXACTLY the rows grad p(z' + U(U*a'/||U*a'||)) with (a', z') near (a, z) in the sense of the lemma.
PRECISION P-1b (where banks can sit). Inside the window the sign condition z'_j = sgn a'_j together with
|z'_j - z_j| < eta forces |z_j| > 1 - eta and sgn z_j = sgn a'_j at every j <= W in supp a'. Hence near f a bank
(a support coordinate of a' outside F) can sit at a FIXED coordinate j only if j is a contact of f (|z_j| = 1) with the
contact sign, or a near-contact with |z_j| > 1 - eta; banks at free coordinates must escape to infinity as the
approximant tends to f (Lemma 1.4' with W >= j and eta < 1 - |z_j|). The phrase "tiny banks anywhere" (Section 0 and
the task statement) must be read as "anywhere beyond the window, and at contacts / near-contacts with the contact
sign inside it". This does not affect any conclusion of N1, but it is a real constraint an adversary may exploit
(free coordinates of f can never be banked at a fixed position).

## Prop 1.5 -- CORRECT
Re-derived: p*(T^* u) <= (1 - (1 - rho^2) sin^2 psi)^{1/2}; p*(T^* y) >= <T x_S, y> >= ||S|| - delta >= 1 - 2 delta gives
(1 - rho^2) sin^2 phi <= 4 delta - 4 delta^2 <= 4 delta (the case cos phi = 0 is covered by the same inequality).
(b): R S x_S = ||S|| e_1, so f' := first row / ||S|| satisfies f'(x_S) = 1 = p(x_S) and p*(f') <= 1, hence f' = grad p(x_S)
(prop:smooth(b)); g' in C(f') by prop:reduction(a); g'(x_S) = 0. (c): RS/||S|| - T = (R(S-T) + (R-I)T + (1-||S||)T)/||S||,
||R - I|| = 2|sin(phi/2)| <= |phi| <= (pi/2)|sin phi| for |phi| <= pi/2. Constants as stated.
Numerics (N1_ref_work/ref_checks.py (1)): Euclidean model, exhaustive rank-one perturbations: max ratio
|sin phi| / (2 (delta/(1-rho^2))^{1/2}) = 0.49 (never > 1). In round models the angle is ~ delta/(1-rho) for small delta,
so the square-root bound is a worst-case bound (it is what the slack argument gives); not claimed sharp. Fine.
PRECISION P-3: in the paragraph "CONSEQUENCE (the Hahn-Banach formulation)" the sentence "for small delta the ball
B((f, rho g), delta) either meets NA or misses it entirely" is vacuous (true of any set and any ball). Intended:
"(f, rho g) notin cl NA iff some ball B((f, rho g), delta) misses NA". Cosmetic.

## Prop 1.5bis -- CORRECT
(a) from Prop 1.5 with delta'' small; N_delta subset NA. (b) "<=": Lambda(S) = <S x, e_2> = c(sin phi f'(x) + cos phi g'(x))
<= (1 + delta)(r~_{f'}(x) + delta p(x)) since cos phi > 0 and max_{C(f')} x = r~_{f'}(x); strict inequality for small delta.
"=>": the identification L((X,p), l_2^2) = X* x X* (equivalent norm) and Lambda = (Phi_1, Phi_2) in l_inf x l_inf is
correct; the Goldstine approximation on a finite eps-net of the compact set C(f) u {g}, combined with the outer
semicontinuity C(f') subset C(f) + eps B for f' near f (thm:compact), is correct, with the stated error
eps(1 + 4 p**(Phi_2)).
REMARK (not an error): N_delta contains ALL mates of NA rows near f. Separation of (f, rho g) from the smaller set
NA ∩ B((f, rho g), delta'') is a different (weaker) property: it holds iff (f, rho g) notin cl conv(NA ∩ B(...)); N1 does not
claim anything about it. The reading "a general non-recovery proof only gives a fibrewise separation" is correct.

## Theorem 1.6 -- CORRECT
(a) Standard distance duality dist(h, C) = max_{||phi|| <= 1}(phi(h) - sigma_C(phi)) for a norm compact convex C; the map
phi -> phi(h) - sigma_C(phi) is weak*-continuous on bounded sets (finite nets), so Goldstine reduces the max over B_{p**}
to the sup over B_p, and sigma_C(x) = r~_{f'}(x) on X (prop:primal). l_1 version identical with B_{c_00} weak*-dense in
B_{l_inf}.
(b) Euler's identity grad p(x')(x') = p(x') = 1 gives the two forms of beta; r^2 = (p - f')(p + f') = beta(2p - beta);
uniqueness of the normer from strict convexity of p** (prop:forced(a)) restricted to X. Correct.
(c) Unwinding of sup and inf. Correct.

## Corollary 1.7 -- CORRECT
v = (x' + tau v)/(2 tau) - (x' - tau v)/(2 tau); r even and 1-homogeneous; r(x' +- tau v)^2 <= 2 beta p <= 2(1 + tau p(v)) beta.
Hessian limit: beta(x' +- tau v) = tau^2 Q(v)/2 + o(tau^2). Bidual version via Goldstine nets (|f(y_a)| <= p(y_a) <= p**(Y)
keeps the radicand nonnegative). Re-ran N1_work/twopoint_check.py: LP support values converge and never exceed the
two-point bound (e.g. 0.2077 <= 0.3582). The non-sharpness remark is correct.

## Proposition 1.8 -- CORRECT
Re-derived; the slack inequality s(t) - s(rho t) = (1 - rho^2) t^2/(s(t) + s(rho t)) >= (1 - rho^2) min(t^2, |t|)/3 holds
(2 s(t) <= 2 sqrt 2 < 3 for |t| <= 1, and 2 s(t) <= 2 sqrt 2 |t| for |t| >= 1). Numerics: ref_checks.py (2) grid check
and (3) end-to-end Euclidean test (2000 random cases, no failure).

## Theorem 1.9 -- CORRECT (cosmetic label swap in (a))
(a) Both inequalities correct (PRECISION P-5: the labels ">=" and "<=" in the proof of (a) are interchanged: the first
argument proves sup_{Rec} x <= limsup, the second the reverse). (b1)=>(b2) support functions; (b2)=>(b1) the closed
convex hull of the compact Rec(f) is norm compact hence weak*-compact, separation by x in c_0; (b1)=>(b3) uniqueness of
the maximizer; (b3)=>(b2): Mazur's theorem (continuous convex functions on separable Banach spaces are Gateaux
differentiable on a dense G_delta), the subdifferential of the support function sigma_{C(f)} at x is the maximizer face
{g in C(f) : g(x) = r~_f(x)} (proved by 1-homogeneity), p-Lipschitz extension from the dense set. (c), (d) correct.
The reformulations of (I) are correct (the converse direction uses rho g(x) >= theta > 0, hence g(x) > 0).
Remark 1.10 (I): correct as a reformulation; additionally (referee): since r~_.(x) is usc, the set
{f'' in B(f, delta) : r~_{f''}(x) >= r~_f(x) - theta} is closed, contains f, and misses the dense sets NA_1 and Omega;
so a type (I) obstruction lives on a closed nowhere dense "ridge" through f. (II): correctly labelled OPEN; there is no
soft argument for convexity of Rec(f) (a union of the convex Hausdorff cluster sets A in A(f)).

## Lemma 2.1 -- CORRECT
(a) definition; (b) diagonal argument; when applying (b) with R = Omega one must use R = Omega u NA_1 (Omega need not
contain NA_1), and only the inclusion Ls_Omega subset Ls_{Omega u NA_1} = Rec(f) is needed: correct as used.
(c) see P-4.

VERDICT PART 1: Section 1 and Lemma 2.1 are correct. Fixes are precisions only (P-1a two-sided Lemma 1.4', P-1b bank
positions, P-2 citation, P-3 vacuous sentence, P-4 openness trivial, P-5 label swap). The content is a set of exact
REFORMULATIONS (soft analysis); none of it constrains whether a counterexample exists.
