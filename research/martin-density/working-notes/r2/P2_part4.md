# P2 part 4: scale-dependent switching mates — replication, implants, averaging; the residual class

## 4.1 Lemma (replication identity). PROVED.
Fix a block m (index dropped), f in S_{p*} and f' in S_{p*} (e.g. NA). Partition N into
 W_off: coordinates that are strict non-peaks at f and at f' with r'(k) = r(k) (tuned),
 W_P:  coordinates that are peaks at f and at f' with the same sign (tuned peaks and untouched robust peaks),
 Ch:   the rest ("changed").
Put rho_W := sum_{W_off} Phi_k^2 r(k)^2, S_P := sum_{W_P} Phi_k^2, G(c) := c^2(1 - rho_W) - (1 - c)^2 S_P. Then 1 - rho_W > 0, G is strictly increasing on
[0,1], G(C') - G(C) = sum_{Ch} Phi_k^2 (w'(k)^2 - w(k)^2), hence
   |C' - C| <= sum_{Ch} Phi_k^2 / g_0,   g_0 := min_{c between C, C'} G'(c) >= 2 min(C, C')(1 - rho_W) > 0   (|w|, |w'| <= 1),
and w'(k) - w(k) = sign * r(k)(C' - C) on W_off, = -sigma_k (C' - C) on W_P, |w'(k) - w(k)| <= 2 on Ch, so
   ||R*(w' - w)||_1 <= |C' - C| sum_k lambda_k (1 + r(k) 1_{W_off}) + 2 sum_{Ch} lambda_k.
*Proof.* C^2 = sum_k Phi_k^2 w(k)^2 with w = C sign r on W_off and |w| = M = 1 - C on W_P (Lemma 1.1), and the same at f' with the same r on W_off.
1 - rho_W = 1 - sum_{W_off} Phi^2 w^2/C^2 >= sum_P Phi^2 M^2/C^2 > 0 (P nonempty). G'(c) = 2c(1 - rho_W) + 2(1 - c)S_P > 0. Mean value theorem. QED.
Consequence (deep replication): if every coordinate with Phi_m(k) >= theta is in W_off cup W_P, then ||R_m*(w'_m - w_m)||_1 <= c_f theta
(c_f depends on m, M, C only), since sum_{Phi < theta} lambda_k <= 2 m theta and sum_{Phi < theta} Phi_k^2 <= theta^2.

## 4.2 Lemma (feasibility of retuning moves; duality). PROVED.
Let (u_k)_{k in W} be finitely many elements of l_1, G a set of coordinates, A > 0 and (delta_k) in R^W. There is y supported in G with ||y||_inf <= A
and u_k(y) = delta_k for all k in W iff  sum_k c_k delta_k <= A ||(sum_k c_k u_k) 1_G||_1 for all c in R^W.
Hence, with the restricted radius r_W(G) := min_{||c||_1 = 1} ||(sum_k c_k u_k) 1_G||_1, every correction with max_k |delta_k| <= A r_W(G) is feasible,
and r_W(G) = 0 iff some nonzero combination of the u_k vanishes on G.
*Proof.* {(u_k(y))_k : supp y in G, ||y||_inf <= A} is a compact convex symmetric subset of R^W (weak*-compact l_inf(G)-ball, weak*-continuous map);
its support function at c is A ||(sum c_k u_k)1_G||_1; a point lies in a compact convex set iff it satisfies all support inequalities.
For the radius statement: sum c_k delta_k <= ||c||_1 max|delta_k| <= A r_W(G) ||c||_1 <= A ||(sum c_k u_k) 1_G||_1. QED.
Remark. If the window W contains the support of a resonance carrier (a combination of the u_k supported in F cup K, e.g. v of an exact resonance),
then r_W(J) = 0 on the free coordinates J: these directions must be steered by contacts and masses (Thm 2.1, Step 1), not by free moves.

## 4.3 Proposition (abstract replication–averaging–transfer scheme). PROVED (as an implication; the hypotheses carry the content).
Let f in S_{p*}, g in C(f), rho in (0,1), delta in (0,1/2], T_0 in (0,1] with T_0^2 <= 3 delta, kappa >= 0, J >= 4 kappa/delta. Suppose that for every
eta > 0 there are an NA point f' and gbar, h_1, ..., h_J in X* (s_j = s_1 2^{1-j}, s_1 <= T_0) with
 (TR) [transfer regime]  p*(f' + t gbar) <= 1 + (t^2/2)(1 - 2 delta) for s_J <= |t| <= T_0;
 (TS) [two-sided supply] p*(f' + t h_j) <= 1 + (t^2/2)(1 - 2 delta) for |t| <= s_j, and p*(h_j - gbar) <= kappa s_j;
 (SL) [slack] p*(f' - f) <= eta and p*(gbar - rho g) <= eta.
Then (f, rho g) is in cl NA.
*Proof.* Lemma 1.5 gives g' := (1/J) sum_j h_j with p*(f' + t g') <= 1 + (t^2/2)(1 - 2 delta + 4 kappa/J) <= 1 + (t^2/2)(1 - delta) on |t| <= T_0 and
p*(g' - gbar) <= 2 kappa s_1/J. Lemma 1.4 applies once eta and s_1 are small (p*(f'-f) <= (1-rho^2)T_0^2/6, p*(g' - rho g) <= (1-rho^2)T_0/6). QED.
Theorem 2.1 is the special case J = 1 and h_1 = gbar = g': the theta-tail makes the frozen error vanish, so no averaging is needed.

## 4.4 What (TR) and (TS) require for scale-dependent switching mates. (Identities PROVED; necessity HEURISTIC; (QI) OPEN.)
Let g be a mate whose admissible decompositions (B_t, Omega_t) change with t on a side at all small scales (approximate resonances,
A §7.2, P1 4.1). Transport them to f' as in 3.2 (d'_t recomputed per scale). Then:
 (1) [consistency] by 3.2(i) the transported pieces represent ONE gbar only if the relative positions u_{k,m}(x')/|R_m x'|_m equal those of xi
     on the span of the differences of the block parts used at scales in [s_J, T_0], up to an l_1 error <= eps_0 s_J after multiplication by
     R_m* w'_m; equivalently, the mixed term of 3.1 must vanish for all pairs of pieces.
 (2) [depth of the window] at scale t one-sided block carriers have depth Phi <~ t or are near-threshold (P1 3.3 with P1-referee correction
     C3). Usage at depth Phi < theta moves the functional t lambda_k Omega_t(k) u_k with |t Omega_t(k)| <= 2 s(t) (box), i.e. total
     l_1 mass <= 2 s(t) sum_{Phi < theta} lambda_k = O(theta); dropping it (moving it to the base) costs at most O(theta) (kink, first order in
     the moved mass), which must be <= eps_0 t^2 at t = s_J: the replicated window must reach depth theta <~ eps_0 s_J^2. By 4.1 this means: all
     coordinates with Phi >= theta tuned or untouched robust peaks; then ||R*(w' - w)|| = O(theta).
 (3) [perturbations to undo] the masses needed for (TS) move xhat' by ~ s_1 in sup norm (through e', 3.1); by Lemma 1.1 this moves every strict
     non-peak of depth Phi >~ s_1 and every peak with margin < s_1. Undoing it requires corrections of size ~ s_1 on a window W(theta) of about
     |I_0| log2(1/theta) functionals, using costless coordinates G (free coordinates unused by the base parts at scales >= s_J, far
     coordinates), modulo resonance directions (steered as in Thm 2.1). By 4.2 this is possible iff s_1 <~ r_{W(theta)}(G), i.e.
        (QI)  along a sequence of usable small scales s -> 0:  r_{W(eps_0 s^2)}(G_s) >= c s  for some c > 0.
     (QI) is a quantitative independence property of T relative to f, g, not implied by Lemma B. Example of the difficulty: for a T built as
     in P1 2.1 (super-fast signature tails delta_l 2^{-s} on disjoint sets S_l), the restricted radii of deep windows on FAR coordinates decay
     faster than any power of s, so (QI) could only hold through near free coordinates and depends on the targets y^(i). OPEN.
 (4) [two-sided supply] (TS) needs, at J = O(kappa/delta) scales s_j <= s_1 (a FIXED number), two-sided certificates at f' within O(s_j) of gbar.
     Engineered sources: (a) contact masses for base one-sided usage (always possible; price: the consistency conditions (1));
     (b) off-peak carriers with gap: replicate finitely many ratios (Thm 2.1); (c) degenerate peaks: one tuning move each turns them into
     strict non-peaks with tiny gap (Lemma 1.1), SKETCH; (d) other one-sided block carriers (weak peaks, near-threshold coordinates,
     coordinates pushed beyond their gap, deep coordinates): only through implanted gaps on carriers k with ||u_{k,m} - v|| <~ Phi_m(k)
     (rates; one tuning move per carrier, finitely many), which lie inside the replicated window of (2), hence again (QI); (e) nothing else:
     by P1-referee R1, along C-tame NA approximants every recovered mate is a limit of certificate-span vectors, so a component carried at f
     only by one-sided BLOCK resources, without rates and without a contact representation (exact resonance), cannot be supplied by
     certificates at such approximants.

## 4.5 C's "implant scale gap" heuristic (C_part6 §9.3): verdict.
C's claim: an implanted non-peak at depth k costs eps >~ Phi(k) in p*(f' - f), so the slack covers only |t| >~ sqrt(Phi(k)), while the implant is
quadratic only for |t| <~ Phi(k); hence implants cannot bridge (Phi(k), sqrt(Phi(k))) and are never the sole support of a mate component at
intermediate scales.
 * The arithmetic is correct (PROVED: by Lemma 1.1 a gap gamma' implanted at a former peak changes w(k) by >= gamma', which contributes
   lambda_k gamma' u_k to f' - f; A Prop 8.4(b) bounds the certificate mass it can carry).
 * That the window (Phi, sqrt Phi) must be covered by structure shared by xi and x' is correct; that this obstructs engineered recovery is
   FALSE in general: Theorem 2.1 is a rigorous instance where the implanted two-sided structure (masses ~ s_1, so p*(f' - f) >~ s_1 >> s_1^2)
   serves only |t| <= s_1, while the whole window (s_1, T_0) — far beyond the slack scale sqrt(p*(f'-f)) — is covered by the EXACT transfer
   of f's one-sided decompositions. The slack is needed only for |t| >= T_0 (fixed): p*(f' - f) must be small compared with T_0^2, not s_1^2.
 * For scale-dependent mates the heuristic points at the real difficulty: the shared structure must then be replicated at all scales in
   (s_1, T_0), i.e. (QI).

## 4.6 Exact residual class (what P2 does NOT cover). OPEN.
Covered: (PROVED) two-piece switching mates with finitely supported off-peak block carriers, finite F, any contact set K and any split,
d-neutral transfer, one active block or several under (S) (Thm 2.1); (SKETCH) non-neutral transfers at block-tame active blocks (Thm 3.4),
shifted two-piece data (Rem 2.4), degenerate-peak carriers (3.5 R5).
Not covered:
 (R1) non-neutral two-piece data at active blocks with infinitely many strict non-peaks or dense near-threshold peaks (needs (QI));
 (R2) several active blocks without (S);
 (R3) two-piece data whose explicit side coefficients exceed 1/rho^2 and are not cured by shifts (Rem 2.4 is SKETCH);
 (R4) infinite base support F (near-flip coordinates as one-sided resources);
 (R5) genuinely scale-dependent switching (approximate resonances): one-sided carriers at depth ~ t (weak peaks, near-threshold coordinates,
      coordinates pushed beyond their gap) or contact splits varying with the scale on the SAME side; the scheme 4.3 reduces them to (QI) and
      implant compatibility, OPEN and T-dependent.
At P1's example every mate lies in E_u (P1 6.1); the slab and all explicit defect mates are recovered (Cor 2.3(b), PROVED); the whole fibre
would follow from Rem 2.4 (SKETCH).
