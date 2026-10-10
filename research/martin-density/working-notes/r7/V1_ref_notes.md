# V1 referee notes (Round 7): verification of the D_Omega assembly and proofs of all precisions

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; numbering and notation as there), Round 5-6 refereed results, V1 =
r7/V1_notes.md (= V1_head + V1_part1..5, byte-identical). Finite block set I = {1..N}, p = p_N, F = supp a finite, diagonal base
U^* e_j^* = s_j k_j, s_j = 2^{-j}. Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Referee part files: r7/V1_ref_part1..4.md.
Scripts: r7/V1_ref_work/ (tu_check3.py, tu_check4.py, assembly_check4.py; failing-regime variants tu_check.py, assembly_check2.py).
Notation as in V1: zeta_m := R_m^** zhat, A_m := |zeta_m|_m = sigma_m/q_0, theta_m := A_m M_m/C_m, nu_k := |zeta_m(k)|/Phi_k^2,
rho := nu/theta (peak iff rho >= 1), margin mu = q_0 Phi theta (rho - 1)/m (eq:margin: sigma_m |alpha_m(k)| = lambda_k mu_k, lambda_k = m Phi_k),
val_{l''} := eps_{l''} u_{l''}(zhat), q = val/A at strict non-peaks, b = b(w), u = u(w), Lam = T_lo(w)^3, D = D(l).

## 1. Verdicts
All claims labelled PROVED in V1 are correct. I re-derived every step of Theorem 1', Theorem 2', Lemma D, Lemma 3.4', Lemma S,
Lemma B, Lemma DR, Lemma TU, Lemmas CO, ST, NS, RR, Proposition TR, Theorem E'', Master Theorem II (window arithmetic and quantifier
order), Corollaries M-II.1-3, Corollary AC, Lemma IP and the residual list, against lem:threshold, eq:margin, lem:phicalc,
lem:switchbudget, lem:split, lem:peakshift (eq:peakshift, eq:didentity), lem:suplevel, lem:budget, lem:box, lem:algebra, def:twopiece,
cor:D1, def:SLD/thm:SLD, Y1 Lemmas T2/T3, 3.1-3.6 and Proposition 5.2, Y2 Lemma U'/Theorem E', Y4 Lemmas 1.8, 2.2, 2.3, Y4-ref C.2-C.7,
Z3 Lemmas 3.1, 3.2, Z4 Lemma 5.0. Five precisions (p1)-(p5) are needed; none changes a statement's conclusion or a construction.
One gloss in V1's OPEN section (5.4, on item (B)) is inaccurate (Section 4 below). No counterexample is claimed; nothing found points to one.

## 2. Precisions with proofs

**(p1) The level threshold l_f must also give s_max(l_f) >= max F.  PROVED.**
Used for: s_m := min(S_{c_m} ∩ (s_max(l), inf)) notin F (Lemma DR), pull and bank coordinates notin F (Lemma TU), and
"z^2 = eps_{l''} on S_{l''} \ [1, s_max(l)]" for l'' in L_0 (Lemma TU's exact-swallowing hypothesis follows from (C1) only if
S_{l''} \ [1, s_max(l)] ⊂ S^nat_{l''}(l) = S_{l''} \ (F ∪ T(l))).
Claim: s_max(l) -> infinity. Proof. s_max is nondecreasing. Every target y^(i) is allowed at every large l and occurs infinitely often in
(i_r), so y_l = y^(i) for some l (proof of (T-d) in thm:SLD); hence supp y^(i) ⊂ [1, sup_l s_max(l)] for every i. If the sup were a
finite S, all targets would lie in span{e_1^*, ..., e_S^*}; but for y supported in [1, S], q*(e^*_{S+1}/q*(e^*_{S+1}) - y) >=
||.||_1-part >= 1/q*(e^*_{S+1}) > 0, contradicting density of the targets in S_{q*}. QED. Hence l_f can be enlarged (f-dependent only).

**(p2) Component rates in one-signed blocks.  PROVED.**  V1 part 2, Remark (2) says every component in a block one-signed at w is tiny.
Precisely: kept carriers there have rho <= b, so |val| = rho Phi theta_m/m <= b Phi theta_m/m and the (R5)-rate is <= b theta_m/m (||r||_1 = 1).
Theorem 1'(b) gives b(w) <= 2^{-64/u(w)}, so u/b -> infinity as l -> infinity; for l >= l_f (f-dependent) b theta_m/m < u, and cleanness
forces the rate to be <= b. The conclusion holds for l >= l_f, which is all that is used.

**(p3) Theorem E'': bank coordinates need not be contacts of f.  PROVED.**
Statement to use: Let f_j -> f in S_{p*}, supp a_j = F ∪ Ba_j ∪ Pu_j finite with Ba_j, Pu_j disjoint from F (no condition on z at
these coordinates at f). Suppose the window data at f_j are contact-like on Ba_j w.r.t. z_j (z_j(i) b^+(i) >= 0 >= z_j(i) b^-(i)) and satisfy
t|b^+-(i)| <= |a_j(i)| on Pu_j, plus (E-a), (E-b) (kinds [1'], [2], [3]), (E-c), (E-d'), (E-e'). Then (f, rho g) in cl NA.
Proof. In Lemma U (proofs of lem:uniformtransfer, lem:onesidedtransfer) and Y2 Lemma U', the base support enters only through the
base excess of lem:bookkeeping(b) / eq:baseidentity at f_j: Fl(rb) on supp a_j plus sum_{i notin supp a_j}(|r b_i| - z_j(i) r b_i). Off
supp a_j the data are side-admissible at f_j (two-piece data at f_j). On F: a_{j,min,F} -> a_min > 0 (a_j|_F = a/q*(A_j) -> a). On Ba_j:
for side + and r > 0, sgn(a_j(i)) = z_j(i) and z_j(i) b^+(i) >= 0, so |a_j(i) + r b^+(i)| = |a_j(i)| + z_j(i) r b^+(i): no flip, zero
excess; side - with r < 0 likewise. On Pu_j: |r b(i)| <= c_flat t|b(i)| <= c_flat |a_j(i)| < |a_j(i)| (c_flat <= 1/8): no flip. Only the
sign of a_j(i) AT f_j enters; whether i is a contact of f is never used (Y4 Lemma 2.3's phrase "contacts of f" is only how its banks were
produced). All other constants (nu_j, q_0^(j), sigma_{j,m}, C_{j,m}, M_{j,m}, transfer data via lem:persistence) depend on the norm-convergent
forced data; coordinatewise z_j -> z holds since all modified far coordinates (pulls, banks, s_m) escape to infinity with the level, and the
closed rooms tend to 0. The final step is cor:D1 at the fixed f_j (finite support; the averaged data are d-neutral two-piece data at f_j:
linear/convex conditions). QED  (V1's donor banks s_m in case (b) of (C3) and its tuning banks j'_{l''} are contacts of f^(2) produced by
closings, not necessarily of f; with (p3) Theorem E'' applies to them verbatim.)

**(p4) Constants in Lemma TU.  PROVED.**  In Step 2 the derivative is Phi'(y) = sum_{l''} m_{l''}(y)(Delta_{l''} + beta_{l''})/(v'_{l''} Phi(y)),
and m(y) = (Delta y + beta(y - nu_p))/(s'^2 v'); so the contraction constant carries 1/(s'^2 v'^2) (not only 1/(s'^2 v')). Both are design
numbers of level L: s' = 2^{-j'}, v' = delta_{l''} 2^{-j'}/n_{l''} >= (4/5) delta_min 2^{-sigma(L)} (n in [3/4, 5/4] by (P1)), so
(s'v')^{-2} <= (25/16) 16^{sigma(L)} delta_min^{-2} <= Design(L)^{1/3}. With 2^{G(L)} <= Design^{1/6}, |L_0| <= L <= Design^{1/6} and
kappa <= C L 4^G Design^{1/3} eta^2 one gets |Phi'| <= C_f Design(L)^{2/3}(eta + kappa) <= 1/2 for eta <= c_f Design(L)^{-2/3}; V1's
c_T = f-const x Design^{-3} is therefore more than sufficient, and C_T = f-const x Design^3 bounds m, ||X_tune||^2/eta^2 and the cost.
Numerics (tu_check3/4.py): inside the regime, |val^# - val^(2) - x| <= 1.8e-15, bank masses > 0, |Phi'| <= 0.018, other carriers move
by <= 0.44 x the Lemma B(i) bound (O(eta^2), with a per-model constant independent of eta); outside the regime the iteration can diverge
(tu_check.py), as expected.

**(p5) Rooms of donors at f^#.**  Lemma RR does not (and need not) assert that the R1-room of a class-R DONOR stays robust: in case (b)
of (C3) closing z_{s_m} may remove most of that room (s_m carries the largest weight of S^nat_{c_m}). No step uses it: donors are pinned at
f ((3.1), (3.5), (3.6)), carry tau' = 0 and datum 0 at f^#, V'(s_m) = 0, and b^+-(s_m) = 0.

Minor: (p0) for p_N, rate objects of level l that involve carriers l'' = j(k, m) with m > N are given the value 1 (they do not exist for
p_N); patterns are arbitrary subsets of [1, l], so all design constants are unchanged and N-free.

## 3. Re-derivations recorded (selection)
(a) Lemma D: coarse peaks with rho in [1, 1+b] carry sum |alpha| <= (q_0 theta_m b/sigma_m) sum_k Phi_k^2 <= (M_m/(4C_m)) b; fine peaks
<= 2 q_0 sum_{l''>l} lambda_{l''}/sigma_m <= q_0 b^2/sigma_m; ||alpha_m||_1 = 1 (lem:threshold); clean w excludes rho in (1+b, 1+u).
(b) Lemma S: eq:peakshift gives -Delta theta_{l''} = vs lambda (Delta d M + e_k) with 0 <= lambda e_k <= t/mu_k; lem:switchbudget gives
sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0; phi_z is 2-Lipschitz; c(.; pi) is positively homogeneous; c_pi ||delta||_1 <= t/q_0 + 2||R||_1.
(c) Lemma ST(b): Y1 Lemma T2(b) with outward push s in [Lam/2, 4Lam] (zeta-units) and E_m <= C_f T_lo^4 <= A s/(8(A + theta + 1)).
(d) Proposition TR, Step 3: rays with m(r) != m have zero m-component at f^#, so the per-block removals (Y4 Lemma 1.8 on cone{r : m(r) = m},
D_min >= u/(2 D A^#_m)) do not interact; 0 <= tau' <= tau_0 keeps the box rows. Step 4: lem:split is pointwise and accepts any sign vector z'
for which V is z'-signed on {|z'| = 1}, with |e_+-(j)| <= |e(j)| + phi_{z'_j}(B_+(j)) + phi_{-z'_j}(B_-(j)). Step 5: kind [3] with the outward
allowance 1.5 gap^#/t is covered by Y2 Lemma U'(ii): r vs omega <= 1.5 c_flat gap <= (1 - rd) gap (c_flat <= 1/8, |rd| <= 1/2).
(e) Master Theorem II: K_w T_hi <= C_f 2^{-l^3}/l; n c_flat/K_w >= l 2^{l^3}/C_f; theta_w <= c_f u^2(1-rho^2)/(24 rho^2) (T_lo <= 2^{-Q}).
(f) M-II.3: Z4 Lemma 5.0 gives, in every block at maximal contact, fixed swallowed peaks of both signs with margins >= q_0/4, i.e. (U2), (L2)
at every clean w of large level.
(g) Union with Y1 5.4: Y1 uses (SP_w) only through Lemma 3.4's K_d (feeding K_P, K_O, Step 2 of Proposition 5.2); Lemma S provides the
same bound with K_d' = C_f l D^3/u^2 under (SH_w); absorbed by Q(w).

## 4. Correction of a gloss in V1 5.4 (item (B))
V1: "tiny-but-nonzero minors are not exactifiable by value tuning without destroying robust components — determinantal".
This is not right as stated.  PROVED (exactification step only): Fix a pattern kappa of level l. The normalized ray d-matrix has entries
D_{r,m}/A_m with D_{r,m} = sum_{l'' in supp r, m(l'')=m} r(l'') val_{l''}, linear in the value vector val in the compact box [-2, 2]^{L(kappa)};
every minor is a polynomial in val with design coefficients. Let S be any set of such polynomials (components and minors, suitably
normalized by design factors) and g_S := sum_{P in S} P^2. Z(g_S) ⊃ {0} is nonempty, so by the Lojasiewicz inequality there are design
constants C_S, gamma_S in (0, 1] with dist(v, Z(g_S)) <= C_S g_S(v)^{gamma_S} on the box. Taking S := the tiny objects at a clean w
(g_S(val^(2)) <= #S (C b)^2), some v^# with all objects of S EXACTLY zero lies within C' b^{2 gamma_S} of val^(2); robust objects move by
O(b^{2 gamma}) << u; Lemma TU realizes v^# at cost O(b^{2gamma} log(1/b)). The only constraint is quantitative: the move must stay below
the raise buffer Lam = T_lo^3 and the cost below o(T_lo^2), which a design with b(w) := T_lo(w)^{K(l)}/(l Design(l)), K(l) > 3/(2 gamma(l)),
gamma(l) := min_S gamma_S over the finitely many systems of level l, guarantees. So the obstruction in (B) is NOT "destroying robust
components"; the correct statement is "(B) is not reached by V1's LINEAR (least-norm) tuning". This is the route taken in task V2
(V2_part1 Lemma H: Hoffman constants through minors; V2_part2: determinantal objects + Lojasiewicz) — not refereed here.

## 5. Numerics (sanity checks only)
assembly_check4.py: 300/300 one-block companions with a robust donor, a near-threshold carrier (|rho - 1| <= 1e-10) and a tiny
2-carrier ray component: after (C3) (close + bank, Lam = 1e-7) and (C4) (least-norm x, pulls + banks, explicit fixed point) the component
is <= 3.3e-16, theta^# - theta >= 0.75 theta Lam, and rho^# - 1 <= -0.75 Lam at the near-threshold carrier (strict non-peak although
tuned). assembly_check2.py (bank masses 0.1-0.47, outside Lemma DR's regime mu^D <= Design Lam << 1): 3/48 failures, all from
second-order Hilbert effects exceeding the push — shows the smallness of mu^D is genuinely used (it holds in D_Omega).
V1's bank_donor_check.py and lemma_ip_check2.py re-run: identical output.

## 6. What remains open (D_Omega, diagonal base, F finite)
(B) genuinely multi-block rays (an extreme ray of C(kappa(w)) with robust d-components in two blocks) — candidate route: determinantal
exactification + Hoffman-through-minors (Section 4; V2); (C) coherent shift resonance (a source-deficient block with tiny shift cost
c_{pi(w)} <= b(w); c_pi is a property of f that no companion changes); (E) infinite F (O4-crit, O4-nd, O4-box). For N = 1 only (C) and (E)
remain. Lemma Z and density of NA((c_0, p_N), l_2^2) and NA((c_0, p), l_2^2) remain OPEN for every admissible T, including D_Omega.
