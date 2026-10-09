# Z4 referee notes: proofs of the fixes and additions

Setting and notation as in the note paper/martin_density_note.tex (Section 8, Subsection "Toward Lemma Z") and in r5/Z4_notes.md:
canonical base, I = {1,...,N}, p = p_N, the signature-ladder operator (Definition def:SLD) or its modification SLD_G (Z4 part 2.4),
f in S_{p*} with finite base support F, forced data (xi, q_0, a, w, zhat, z, e, nu), blocks m with data (M_m, C_m, P_m, Q_m, alpha_m,
sigma_m), ladder indices l with carriers (k(l), m(l)), u_l, lambda_l = m(l) Phi_{m(l)}(k(l)) <= c_l/4, signatures v_l = delta_l h_l/n_l,
swallowed set B, signs eps_l, switching amplitudes tau_l = -eps_l Delta theta_l, weights q_l = eps_l Phi w(k(l))/(mC) (block m = m(l)).
Labels: PROVED / HEURISTIC / OPEN as indicated. Report: r5/Z4_referee.md. Part files: r5/Z4_ref_part1..6.md; scripts r5/Z4_ref_work/.

---------------------------------------------------------------------------------------------------------------------------------------
## 1. Far lowerings: a correct proof of Proposition 1.2 of Z4 (PROVED)

Let L_F be such that S_l ∩ F is empty for l > L_F; for L >= L_F let G_L be the union of the S_l with l > L, and let f^L be the first row
with forced data (a, z^L), where z^L = 0 on G_L and z^L = z elsewhere (Remark rem:lemmaZ(c)). Put eps_L := sum_{l > L} lambda_l.

**Proposition 1.2 (corrected proof).** There are L_1 and a constant K, depending only on f, N and the design, such that for L >= L_1,
  p*(f^L - f) <= q*(f^L - f) <= K eps_L <= K c_{L+1}/2.

*Proof.* Both rows have base part a, hence the same e = U*a/nu, zhat^L - zhat = -z 1_{G_L}, and f^L - f = sum_m R_m^*(w^L_m - w_m).
Fix a block m and drop its index.

(i) Coarse values are unchanged. For l <= L the vector u_l is supported in supp y_l ∪ S_l; S_l is disjoint from G_L, and supp y_l meets
no S_{l'} with l' >= l (allowedness (a)), in particular none with l' > L. Hence u_l(zhat^L) = u_l(zhat) for l <= L, and for l > L,
|u_l(zhat^L) - u_l(zhat)| <= ||u_l 1_{G_L}||_1 <= q*(u_l) = 1. Consequently ||R** zhat^L - R** zhat||_1 <= sum_{l > L, m(l) = m} lambda_l
<= eps_L, and since |.|_m <= ||.||_1, the block norms satisfy | |R** zhat^L| - |R** zhat| | <= eps_L. Put rho_0 := |R** zhat|/2 and
take L so large that |R** zhat^L| >= rho_0.

(ii) The common ratio. Put v_k := m|u_k(zhat)|/|R** zhat| and v^L_k := m|u_k(zhat^L)|/|R** zhat^L|. By (i), for every coarse k
(ladder index <= L), v^L_k = r v_k with the SAME number r := |R** zhat|/|R** zhat^L|, and |r - 1| <= eps_L/rho_0; moreover
sign u_k(zhat^L) = sign u_k(zhat). For fine k, v_k, v^L_k <= m/rho_0 (because |u_k(zhat)| <= q**(zhat) q*(u_k) = 1).

(iii) The constants C^L, M^L. As in the proof of Lemma lem:F1, C and C^L are roots of F(c; v) = 1 and F(c; v^L) = 1, where
F(c; v) = sum_k min(Phi_k (1-c)/c, v_k)^2. Since f^L -> f (Remark rem:lemmaZ(c)), C^L -> C (Proposition prop:continuity), so the root
localisation of the proof of Lemma lem:F1 (with a fixed peak k_natural having alpha(k_natural) != 0, which is coarse for L large) gives
|C^L - C| <= (2(1-C)/(C c_*)) sum_k Phi_k |v^L_k - v_k|. Here sum_k Phi_k |v^L_k - v_k| <= (eps_L/rho_0) sum_k Phi_k v_k
+ (2m/rho_0) sum_{fine} Phi_k <= eps_L (m/(2 rho_0^2) + 2/rho_0), using sum_k Phi_k <= 1/2, v_k <= m/(2 rho_0) and
sum_{fine} Phi_k = sum_{l > L} lambda_l/m. Hence |M^L - M| = |C^L - C| <= K_C eps_L with K_C depending only on f.

(iv) Coarse coordinates (this replaces the erroneous step). By the clamp formula, for coarse k with s_k := sign u_k(zhat),
  w(k) = s_k min(M, C v_k/Phi_k),   w^L(k) = s_k min(M^L, C^L r v_k/Phi_k).
Elementary inequality: for M > 0, x >= 0, beta > 0, |min(M, beta x) - min(M, x)| <= |beta - 1| M. (If beta >= 1: the difference is
0 when x >= M, and at most (beta - 1)x < (beta - 1)M when x < M. If beta < 1: the difference is min(M,x) - min(M, beta x) <=
min(M,x) - beta min(M,x) <= (1 - beta) M.) Also |min(M^L, y) - min(M, y)| <= |M^L - M|. With beta := C^L r/C,
  |w^L(k) - w(k)| <= |M^L - M| + |C^L r/C - 1| M <= K_C eps_L + (|C^L - C| r + C|r - 1|)/C <= K_w eps_L
for every coarse k, with K_w := K_C + (2K_C + C/rho_0)/C (for L large, r <= 2). This is a SUP-NORM bound; no summation over k is needed.

(v) Summation. sum_{coarse k} lambda_k |w^L(k) - w(k)| <= K_w eps_L sum_k lambda_k <= K_w eps_L, and sum_{fine k} lambda_k |w^L(k) - w(k)|
<= 2 sum_{fine} lambda_k <= 2 eps_L. Since ||R_m^* W||_1 <= sum_k lambda_k |W(k)| ||u_k||_1 and ||u_k||_1 <= 1,
||f^L - f||_1 <= N (K_w + 2) eps_L, and p* <= q* <= (1 + ||U||) ||.||_1. Finally eps_L <= c_{L+1}/2 by (P2). QED.

Remark 1.1 (what was wrong). The submitted step (iv) bounds sum_k lambda_k|w^L(k)-w(k)| by m eps_L sum_k (K_C(Phi_k + v_k) + v_k/rho_0) and
uses sum_k v_k <= m/(2 rho_0). This is false: v_k does not tend to 0 (the normalized block vectors are dense in S_{q*}), so sum_k v_k is
infinite. Without the multiplicative structure (ii), the clamp estimate gives only sum_k min(2 Phi_k, K eps_L) = O(eps_L log(1/eps_L)).
Numerical illustration: r5/Z4_ref_work/clamp_lowering.py.

Remark 1.2 (on Proposition 1.3 of Z4). Parts (a)-(c) are correct as stated (the box bound of Lemma lem:box only needs N_m(w + t Theta) <=
s(t), t <= 1). By (iv) the block data of coarse carriers move by O(eps_L) in sup norm, so coarse carriers with margins or gaps below
O(eps_L) may change their peak status at f^L; this does not affect (a)-(c). The sentence "hence a proof of lower semicontinuity along f^L
must ..." is an interpretation (HEURISTIC), see Section 7 below.

---------------------------------------------------------------------------------------------------------------------------------------
## 2. N-independence of the modified ladder (fix; PROVED)

In Z4 part 2.2 a configuration of level l uses U ⊂ L_N ∩ [1,l], so G*(l), and with it SLD_G, depends on N. Lemma lem:martintail needs
density for infinitely many N for ONE operator. Fix: in the definition of configurations let U range over all subsets of [1,l] (all ladder
indices, all blocks). The set of configurations of level <= l is still finite and determined by (S_{l'}, y_{l'}, v_{l'})_{l' <= l}, so
G*(l) is still a finite number computable at stage l of the recursion, it dominates the N-dependent constant for every N, and Lemma 2.2 of
Z4 holds verbatim for every N (the actual configuration kappa(f,U), U ⊂ B ⊂ L_N, is among them). Proposition 2.4 and Theorem A then hold
for the single operator SLD_G and every N. The optional clause c_l <= (delta_l ||h_l||_1)^2 must be imposed for l >= 2 only (c_1 = 1
exceeds delta_1 ||h_1||_1 <= 1/(4(1 + ||U||))); recursively c_{l+1} := min{c_l/4, T_lo(l)^3, (delta_{l+1}||h_{l+1}||_1)^2}, which is
computable because delta_{l+1} and h_{l+1} are fixed in (D0); Lemma 5.3 uses the clause only for large l. Smaller c_l only enlarges the set
of allowed targets, so (T-d) and allowedness are unaffected.

---------------------------------------------------------------------------------------------------------------------------------------
## 3. Pinning the uniform shift: a weaker hypothesis (H2'') (PROVED)

Setting of Theorem A, Steps 1-3 (Z4 part 3.2): t in a window W(l_*), a two-sided decomposition of g at scale t, the active set
U = {l in B ∩ [1, l_*] : lambda_l >= t^2} ⊃ U_fix ∩ B, the projection tau° in Z'_{kappa(f,U)} with ||tau|_U - tau°||_1 <= D :=
(1/q_0 + 2) K_1 t (this part of Step 3 does not use the shift), K* and K_1 as in Z4. Write Delta d_m := d_{+,m} - d_{-,m}
(Lemma lem:suplevel). All constants called C' below depend only on f, N and the design.

**Lemma 3.1 (every good peak gives the upper bound).** If k is a peak of block m whose carrier l = j(k,m) is good (degenerate or not),
then Delta d_m M_m <= K* t/lambda_l.
*Proof.* By eq:peakshift, |omega_{+,m}(k)| + |omega_{-,m}(k)| = -varsigma_k Delta Theta_m(k) - Delta d_m M_m >= 0, so
Delta d_m M_m <= |Delta Theta_m(k)| = |Delta theta_l|/lambda_l <= K* t/lambda_l by Step 1. QED.

**Lemma 3.2 (pinning through the d-identity).** Fix a block m.
(UP) If q_l >= 0 for every swallowed carrier l of block m, then Delta d_m M_m <= C' K_1 t.
(LO) If q_l <= 0 for every swallowed carrier l of block m, then Delta d_m M_m >= -C' K_1 t.
*Proof.* By eq:didentity and Phi_m(k(l)) w_m(k(l)) Delta theta_l/(m C_m) = -q_l tau_l for l in B,
  Delta d_m M_m = (1/(m C_m)) sum_{good l, m(l) = m} Phi w Delta theta_l - sum_{l in B, m(l) = m} q_l tau_l + r_m,  |r_m| <= 2t/sigma_m.
The good sum is at most K* t/(m C_m) in modulus (Phi |w| <= 1, Step 1). Split the swallowed sum into l in U and l notin U. For l in U,
tau°_l >= 0, so (tau_l)_- <= |tau_l - tau°_l| and sum_{l in U} (tau_l)_- <= D; with |q_l| <= 1/C_m. For swallowed l notin U the
estimate of Step 5 of Z4 gives sum |q_l tau_l| <= 6t/C_m + 6t^2/C_m. Under (UP), -sum_{l in U} q_l tau_l <= sum_{l in U} q_l (tau_l)_-
<= D/C_m; hence Delta d_m M_m <= K* t/(m C_m) + D/C_m + 12t/C_m + 2t/sigma_m <= C' K_1 t (K_1 >= K* >= 1, t <= 1). (LO) is symmetric:
-sum_{l in U} q_l tau_l = sum |q_l| tau_l >= -sum |q_l| (tau_l)_- >= -D/C_m. QED.

**Definition (H2'').** For every block m: [LOWER] there is a non-degenerate peak of block m whose carrier is good or swallowed with
swallowing sign, or q_l <= 0 for every swallowed carrier of block m; and [UPPER] there is a peak of block m whose carrier is good, or
swallowed with anti sign, or q_l >= 0 for every swallowed carrier of block m. (When a peak is used, it is included in U_fix.)

**Theorem A'' (PROVED).** Theorem A of Z4 (Theorem 3.1, for SLD_G made N-independent as in Section 2) holds with (H2') replaced by (H2'').
*Proof.* In Step 3 of Z4 the bound |Delta d_m| M_m <= K_d t, K_d = C_1 K_1, is the only use of (H2'). Under (H2'') the lower bound comes
from Step 3 of Z4 (non-degenerate good or swallowing-sign peak) or from Lemma 3.2 (LO); the upper bound from Lemma 3.1, from Step 3 of Z4
(anti-sign swallowed peak), or from Lemma 3.2 (UP). All constants are of the form C' K_1. Steps 4-9 are unchanged. QED.

**Remark 3.3 (when (H2'') fails).** The argument of Lemma 5.0 of Z4 works at every f: every block has infinitely many peaks with w = +M_m
and infinitely many with w = -M_m, all non-degenerate. If one of them is good, both halves of (H2'') hold. Otherwise all are swallowed, and
a short case analysis shows that (H2'') fails only if some block (i) has all its peaks swallowed with swallowing sign and a swallowed strict
non-peak with q_l < 0, or (ii) has all its non-degenerate peaks swallowed with anti sign and a swallowed carrier with q_l > 0 (a
swallowing-sign strict non-peak, or a degenerate swallowing-sign peak, which (H3) excludes). Example where (H2') fails and (H2'') holds:
the "self-aligned" rows z = sign(y_l(zhat)) on S_l \ F for every l (constructible recursively, since y_l(zhat) depends only on z on
supp y_l, which meets F, coarser signature sets and coordinates outside all S_l); there all q_l >= 0. Such rows are new for Theorem A only
when they have infinitely many strict non-peaks (with the clause of Section 2 and no degenerate peaks they are (BT) points otherwise), and
then (DR) needs those non-peaks to be d-neutral. Numerical sign check of the d-identity and of the (UP) bound in the finite toy model:
r5/Z4_ref_work/didentity_toy.py (residual |r|/(2t/sigma) <= 0.08, bound never violated; seeds 3, 5, 11).

---------------------------------------------------------------------------------------------------------------------------------------
## 4. One-sided d-resources (PROVED lower bound; HEURISTIC consequences)

**Lemma R.** Let block m be such that q_l >= 0 for every swallowed strict non-peak l of block m, and let l' be a swallowed strict non-peak of
block m with q_{l'} > 0 and zero cost (eps_{l'} u_{l'} 1_{F^c} is z-signed and supported in K). Then for every finite U ⊂ B containing l',
the l_1-Hoffman constant of the system defining Z_U (violation viol_{kappa(f,U)} + sum_m |delta_m|) is at least 1/q_{l'}, and
q_{l'} <= Phi_m(k(l'))/(m C_m) <= c_{l'}/(4 m C_m).
*Proof.* tau := e_{l'} has zero cost and vanishes at the peaks, so viol_{kappa(f,U)}(tau) = 0, delta_m(tau) = q_{l'} and delta_{m'}(tau) = 0
for m' != m. If tau' lies in Z_U, then tau' >= 0 (condition (Z1) of Lemma 2.1 of Z4), tau' = 0 at the peaks, and
sum_{l in U, m(l) = m} q_l tau'_l = 0 with q_l >= 0 at all strict non-peaks of block m; hence tau'_{l'} = 0 and ||tau - tau'||_1 >= 1.
Finally |w_m(k)| <= 1 and Phi_m(k) = 2^{-m-k} c_l <= c_l/4. QED.

Consequences. (PROVED) Without (DR), H^Z_f(l) >= 4 m C_m/c_{l'} for every such l' <= l, and c_{l'} <= T_lo(l'-1)^3: the constant of
Corollary 4.1 of Z4 is then of design scale, fixed after all data determining the windows below level l'. (HEURISTIC) Corollary 4.1 can
absorb it only along windows far above l', i.e. when one-sided d-resources are sparse relative to the ladder; whether a given design
leaves room for this depends on the free sets S_l. (HEURISTIC) With all q_l >= 0 the d-identity gives only sum_U q_l (tau_l)_+ = O(K_1 t),
and since |q_l| = lambda_l |w(k(l))|/(m^2 C_m), a carrier with lambda_l of order t may carry tau_l of order 1/|w(k(l))| at scale t; deleting
such switching to restore exact d-neutrality costs O(1), not O(t). So (DR) is the natural hypothesis, and (E-d) of Z4 is a genuine limit
of the exact-data method.

---------------------------------------------------------------------------------------------------------------------------------------
## 5. Corrections to Section 5 and to 6.3(d) of Z4

(a) Corollary 5.4 (maximal contact). The growth condition drops a factor l^2 from (l + M^canc/Lambda°)^2. This is harmless: Step 8 of Z4
needs only C' Xi_f(l) <= (l 2^{l^3})^6 Lambda°(l)^4 G*(l)^2 along the subsequence (and K_j T_hi -> 0, which needs less), and
Lambda°(l) >= 3^l >= l. The sentence "for the original SLD the same holds" is not justified: Lemma 5.3 needs c_l <= (delta_l ||h_l||_1)^2
for large l, and the original recursion only gives c_{l+1} <= T_lo(l)^3, which is controlled by delta°_l, not by delta°_{l+1} (the latter
depends on min S_{l+1}, left free by Definition def:SLD). For the original SLD the corollary holds with M_f in place of M^canc
(it is then just Corollary 4.1 at maximal contact, where gamma_T = 1, Lambda* <= C Lambda° and (H2') holds by Lemma 5.0).

(b) Section 6.3(d). Finitely swallowed rows are in R under (H2') (or (H2'')), (H3) and (W*) (Corollary 4.2(b) of Z4); they remain open when
(H3) or (H2'') fails OR when (W*) fails (approximate swallowing of good signature sets, (O1)(i)). The submitted text omits the last case.

(c) Remark 5.5(i) holds at every f (not only at maximal contact): if M_f(l) <= (l 2^{l^3})^3 for large l, then
sum{Phi_k : k a swallowing-sign swallowed peak, mu_k < s} <= (4/3) c_{l(s)} with l(s) := min{l : (l 2^{l^3})^{-3} < s}, and
c_{l(s)} <= T_lo(l(s) - 1)^3 <= 2^{-3(l(s)-1) 2^{(l(s)-1)^3}} = o(s).

(d) Remark 5.5(ii) of Z4 (what Corollary 5.4 does not cover) is design-dependent: the condition of Corollary 5.4 is a liminf, so super-weak
swallowing-sign peaks (margins comparable to Phi_l) are covered whenever M^canc_f(l)/Lambda°(l) stays within the ladder along a
subsequence, which can happen when Lambda°(l) exceeds 1/c_l (signature sets starting far out). "(MS) fails on the swallowing side" is
therefore not by itself outside Corollary 5.4; what is outside is M^canc/Lambda° beyond the ladder along every subsequence.

---------------------------------------------------------------------------------------------------------------------------------------
## 6. Scope of Theorem A (PROVED bookkeeping)

Definition def:BT allows any contact set. Hence the first rows that Theorem A'' adds to (BT) ∪ R_0^± ∪ R_S are those with F finite and
infinitely many swallowed carriers, not all resonant and d-neutral, satisfying (H2''), (H3), (DR), (W_inf), and violating (BT) through
infinitely many strict non-peaks, through degenerate or weak peaks that are good or anti-sign, or through weak swallowing-sign peaks whose
margins keep M_f(l)/Lambda°(l) within the ladder along a subsequence. By Section 5(c), if M_f(l) <= (l 2^{l^3})^3 for ALL large l then (MS)
holds on the swallowing-sign swallowed peaks; (W_inf) alone does not imply this, because it bounds M_f/Lambda° only along a subsequence and
Lambda°(l) can exceed 1/c_l when the sets S_l start far out (delta°_l small). The class is special (at maximal contact with F finite, f
depends only on the finitely many numbers a_j, so infinitely many near-threshold or degenerate carriers require coincidences); I make no
measure-theoretic claim.

---------------------------------------------------------------------------------------------------------------------------------------
## 7. Far lowerings and lower semicontinuity (assessment)

PROVED: B(f^L) = B(f) ∩ [1, L], every carrier l > L is good with full room at f^L, and the coarse base data on S_l, supp y_l (l <= L) are
those of f (Proposition 1.3(c)). For l > L the set S*_l (computed at f^L) is S_l itself (no swallowed carrier of f^L exceeds L), so
r*_l = delta°_l and Lambda*_{f^L}(l) <= C_L (3/2)^l Lambda°(l): (W*) holds automatically at f^L as soon as r*_l > 0 for its good l <= L.
Hence, if f^L satisfies (H2'') and (H3) (finitely many conditions, which are NOT automatic from those at f because coarse margins move by
O(eps_L)) and r*_l > 0 for its good l <= L, then f^L belongs to R by Corollary 4.2(b) of Z4. The remaining question is
dist(rho g, C(f^L)) -> 0.
HEURISTIC (agreeing with Z4 6.3): windowed averaging at f^L with target rho g works on windows lying inside the inherited band
[A t_L, 1], t_L = (6K eps_L/(1 - rho^2))^{1/2} (two-sided decompositions of rho g at f^L exist there by Proposition 1.3(a), and
Lemma lem:avgfunctionals uses only the local expansions and the bound p*(f^L + r rho g_t) <= s(rho r) + rho |r| K t). These windows are
windows l_* <= L + 1, whose coarse swallowed sets coincide at f^L and f and whose block data differ by O(eps_L) in sup norm (Section 1).
So a proof along far lowerings needs, on some window in the band, the same absorbability that (W_inf) requires at f, and then Theorem A''
applies to f directly. This is not a proof that no other approximant helps.

---------------------------------------------------------------------------------------------------------------------------------------
## 8. Verification record for Theorem A (Z4 Theorem 3.1), Steps 1-9 (all PROVED as written, given Section 2)

Step 1 (good pinning): the S*_l(l_*) remove only coarse swallowed targets; fine targets (good or swallowed) enter the box remainder <= 6t^2;
in the unrolled triangular system swallowed indices carry x_l = 0 (factor 1), so including (1 + 3/r*_l) for them only enlarges the bound.
Step 2: e_0 = -sum_{l notin U} Delta theta_l u_l 1_{F^c} (using -Delta theta_l = eps_l tau_l on B); inactive swallowed coarse carriers number
at most l_* and have |Delta theta_l| <= 6 lambda_l/t < 6t; Lemma lem:phicalc(c) and the switching budget give c_U <= t/q_0 + 2||e_0||_1.
Step 3: kappa(f,U) has level <= l_* (U ⊂ [1,l_*], max F <= l_*), its cone Z' is the zero-cost cone of f (Lemma 2.2), so Hoffman gives tau°;
eq:peakshift at an anti-sign swallowed peak bounds Delta d M above by (tau_l)_-/lambda_l, at a non-degenerate swallowing-sign swallowed peak
below by -(D + t/mu)/lambda (e_k <= t/(sigma|alpha(k)|) = t/(lambda mu), eq:margin); good non-degenerate peaks give both (Lemma badpeaks(a),
whose proof needs only Step 1). Step 4: peak rows tau_l = varsigma eps lambda (Delta d M + e_k); (H3) is needed only at swallowing-sign peaks.
Step 5: d-row identity from eq:didentity; inactive and fine swallowed carriers contribute <= 6t/C + 6t^2/C; repair by (DR) since U ⊃ U_R.
Step 6: both pairs represent g_t (R_m^* e_k = lambda_k u_k), d-neutral (tau' = 0 at peaks, d-rows exact), side conditions from Lemma split;
every discrepancy in (b), (c) is accounted for; (d) |omega^-(k(l))| <= (10 + C_dia)/t because lambda_l >= t^2 on U.
Step 7: re-derived from the proofs of Lemmas lem:uniformtransfer, lem:onesidedtransfer, lem:block(d): radius conditions gap/(2|omega|) >=
gamma_B t/(2A_2), 1/(2|d|) >= t/A_3, C/(2|d|M) >= C t/A_3; relative errors O(A_3 c_flat); t_1 constrained only by r^4-terms and by
K_3 c_flat^2 t_1^2 (2 + Lambda^varsigma) <= gamma/2, independent of A_2, gamma_B. So c_flat >= c_f gamma_f/C_dia.
Step 8: Lemma 6.1 (c_flat enters Theorem thm:windowed only through I_r and Q at fixed j); K_j/c_flat <= C G*^4 Lambda°^2 Xi_f,
n^w >= (l 2^{l^3} Lambda° G*)^6, K_j T_hi <= C G*^2 Lambda° Xi_f^{1/2} (l 2^{l^3} Lambda° G*)^{-6}; (W_inf) suffices with room to spare.
Step 9: averaging preserves all linear conditions of d-neutral two-piece data; Gamma_w convex; rho^2(1 + eta_0/2) <= 1; Corollary cor:D1.

---------------------------------------------------------------------------------------------------------------------------------------
## 9. Degenerate swallowing-sign peaks: a gap in Z4's sketch, and free steering channels

**Observation 9.1 (PROVED).** Theorem thm:engineered uses the averaged data (b^theta, omega^theta), omega^theta = (omega^+ + omega^-)/2, for
0 < |tau| <= s_1 and BOTH signs of tau. At a used degenerate peak k the two sides move inward in opposite directions
(varsigma omega^+(k) <= 0 <= varsigma omega^-(k)), so omega^theta(k) is outward for one sign of tau, and Lemma lem:block(d) at f' needs
|tau rho omega^theta(k)| <= gap'(k)/2 for |tau| <= s_1. For k notin P', the threshold Lemma at x' gives
|w'(k)| = M'|u_k(xhat')|/(theta_hat' Phi_k), hence, with mu'_k := q'_0(|u_k(xhat')| - theta_hat' Phi_k) < 0,
   gap'(k) = M' |mu'_k| / (q'_0 theta_hat' Phi_k).
So merely making k a strict non-peak of f' (Z4 part 8.1) does not suffice; one needs mu'_k <= -kappa_D s_1 with
kappa_D := 4 rho q_0 theta_hat max_{k in D} Phi_k |omega^theta(k)| / M (late stages: primed quantities within factor 2). For |tau| > s_1
the +/- data are used and the moves are inward, as Z4 says.

**Lemma 9.2 (free steering channels; PROVED).** Let (b^±, omega^±) be side-admissible (b^± = 0 off F ∪ K). Modify Definition
def:engineered by (i) z'_j := z_j + s_1 A_j at finitely many free coordinates j <= N'' (|z_j| < 1, j notin F ∪ K), s_1|A_j| <= (1-|z_j|)/2,
and/or (ii) a'' := a'' + s_1 Delta with Delta in l_1(F) fixed and s_1||Delta||_1 <= a_min/4. Then f' is still norm attaining, Lemmas
lem:approxfacts and lem:F1 hold with K_e enlarged by a constant depending only on (A_j) and Delta, and Step 3 of the proof of Theorem
thm:engineered acquires no new base excess.
*Proof.* z' remains finitely supported with |z'| <= 1 and z' = sign a' on supp a' (signs on F unchanged since s_1||Delta||_1 <= a_min/4), so
Proposition prop:smooth(c) applies as in Lemma lem:approxfacts(a). Change (i) moves xhat' by s_1 A_j e_j, so |u(xhat'_new) - u(xhat'_old)| <=
s_1|A_j| q*(u); change (ii) moves e' by at most 2 s_1 ||U|| ||Delta||_1/nu, as in (E1). Inserting these in the proofs of (E2)-(E5) and of
Lemma lem:F1 only enlarges K_e. Base: at a free coordinate j, b^±_j = 0 and a'_j = 0, so B^diamond_j = rho(beta^diamond_j - c a'_j) = 0 and
the summand of Exc' at j vanishes; on F, |a'_j| >= a_min/4 at late stages and tau rho |beta^diamond_j| <= a_min/8, so no flip occurs. QED.
The first-order effect of the channels on varsigma_k u_k(xhat') - theta_hat' Phi_k is varsigma_k [sum_j A_j u_k(j) + <P^perp U* u_k, U* Delta>/nu]
minus Phi_k times the directional derivative of theta_hat_{m(k)}; at a free target coordinate u_k(j) = y_k(j)/n_k.
CORRECTION to Z4 8.1: "steering through target coordinates meets the same cost" is FALSE at FREE target coordinates: exact zero-cost data
vanish there (Lemma 2.1 of Z4, (Z2)), so steering through them is free; the cost (push) x (switching) arises only at coordinates carrying base
switching (the carrier's own swallowed signature set, and contact coordinates where V' != 0).

**Sketch 9.3 (Corollary cor:D1 for inward degenerate-peak data; SKETCH).** Let D be the finite set of degenerate peaks used by the data and
assume (FS): the channel effects of Lemma 9.2 span a subspace of R^D containing a strictly negative vector (a linear condition; by Gordan's
theorem it fails iff a nonzero lambda >= 0 in R^D annihilates every channel effect). Choose the push so that the channel effect is
<= -(K + kappa_D) s_1 on D, where K s_1 bounds the uncontrolled change of mu'_k caused by window masses and truncation ((E2), (E3), Lemma
lem:F1). Then every k in D is a strict non-peak of f' with gap'(k) >= 2 rho s_1 |omega^theta(k)| (9.1); (E4) holds for omega supported in
Q ∪ D and vanishing on P' (at a degenerate peak of f, Phi^2 w(k)/C = zeta(k)/sigma since alpha(k) = 0); lin'_m = tau rho <omega, alpha'> = 0;
Lemma lem:block(d) holds at f' for the +/- data (inward moves: |W(k)| <= (1 - d sigma)|w'(k)|) and for the theta data (radius by 9.1);
Steps 4-6 are unchanged. (FS) holds e.g. when every k in D has a private free target coordinate. Consequence (SKETCH): Theorem A'' holds
without (H3) at rows where (FS) holds for every finite set of degenerate swallowing-sign swallowed peaks (window data: Lemma 8.1 of Z4).
OPEN: maximal contact (no free coordinates; only the |F|-dimensional channel (ii) remains, while the data may use unboundedly many degenerate
peaks), and super-weak (positive, tiny margin) swallowing-sign peaks.

---------------------------------------------------------------------------------------------------------------------------------------
## 10. Rigidity of the d-mismatch for all non-d-neutral carriers (strengthening of Z4 Prop 5.6)

**Proposition 5.6' (PROVED; strengthens Z4 Prop 5.6 from peaks to all carriers with w != 0).**
Let F be finite and let (b^±, omega^±) be two-piece data at f (Definition def:twopiece) with Delta d_m := d_m(omega^-_m) - d_m(omega^+_m)
!= 0 for some block m. Put Delta := max_{m'} |Delta d_{m'}|, let Omega be the (finite) set of carriers in the supports of the omega^±_{m'},
and T_omega the (finite) union of their target supports. Then for every carrier l of block m with l notin Omega, S_l ∩ F empty and
w_m(k(l)) != 0, every s in S_l with s > max T_omega and 2^{-s} < (2/5)|Delta d_m| |w_m(k(l))| m 2^{-m-k(l)}/(N Delta) is a contact with
  z_s = -sign(Delta d_m) sign(w_m(k(l))).
Equivalently: the far part of S_l is swallowed with a sign eps for which eps Phi w_m(k(l))/(mC_m) (the weight q_l) has sign -sign(Delta d_m).
*Proof.* As in Z4 Prop 5.6, v := b^+ - b^- = sum_{m'} R_{m'}^*(delta omega_{m'} - Delta d_{m'} w_{m'}), delta omega := omega^- - omega^+.
At s as above the delta-omega terms vanish: a carrier k in Omega has u_k(s) != 0 only if s in S_{l(k)} (impossible: l(k) != l and the S are
disjoint) or s in supp y_{l(k)} (impossible: s > max T_omega). For every block m', (R_{m'}^* w_{m'})(s) = [m' = m] lambda_l w_m(k(l)) v_l(s)
+ (targets y_{l'} with s in supp y_{l'}, which forces l' > l by allowedness (a)); by allowedness (b) and lambda_{l'} <= c_{l'}/4,
sum_{l' >= L(s)} c_{l'} <= (4/3) c_{L(s)}, the target part is at most (2/9) 2^{-2s} c_l delta_l in modulus (summed over all blocks), while
|lambda_l w_m(k(l)) v_l(s)| >= (4/5) |w_m(k(l))| m 2^{-m-k(l)} c_l delta_l 2^{-s}. Hence
|v(s) + Delta d_m lambda_l w_m(k(l)) v_l(s)| <= N Delta (2/9) 2^{-2s} c_l delta_l < |Delta d_m lambda_l w_m(k(l)) v_l(s)| by the choice of s,
so v(s) != 0 has the sign -sign(Delta d_m) sign(w_m(k(l))). Two-piece data have v = 0 off F ∪ K and z_j v(j) >= 0 on K; as s notin F,
s is a contact and z_s = sign v(s). QED.
Consequences (PROVED). (a) If block m has infinitely many carriers l with w_m(k(l)) != 0 whose signature sets have infinitely many free
points, or contain contacts of both signs arbitrarily far out, then every set of two-piece data has Delta d_m = 0. (b) Delta d_m > 0
(the option of Corollary cor:D1) requires that all but finitely many non-d-neutral carriers of block m are far-swallowed with q_l < 0;
Delta d_m < 0 (the (SC) regime of Theorem thm:engineered) requires q_l > 0 for all but finitely many of them. (c) Combined with Lemma 3.2 of
the ref notes: under the sign coherence q_l >= 0 the d-identity bounds the two-sided shift from above, and under q_l <= 0 from below; so
sign-coherent swallowing is both the only configuration where non-d-neutral two-piece data can exist and a configuration where one side of
the uniform shift is pinned for free.

---------------------------------------------------------------------------------------------------------------------------------------
## 11. Status after the referee pass

PROVED (Z4 as corrected): Theorem A'' for SLD_G (N-independent), Corollaries 4.1, 4.2, 5.4 (with Section 5), Propositions 1.2 (Section 1),
1.3, 5.1, 5.6, Lemmas 2.1-2.3, 6.1, 8.1; referee additions Lemmas 3.1, 3.2, R, 9.2, Observation 9.1 and Proposition 5.6'.
SKETCH: engineering with degenerate swallowing-sign peaks under (FS) (Sketch 9.3, which corrects and refines Z4 part 8.1).
OPEN (F finite, SLD_G): (E-a) degenerate or super-weak swallowing-sign swallowed peaks; (E-b) near-threshold swallowed strict non-peaks
beyond the ladder; (E-c) near-contacts in swallowed targets beyond the ladder; (E-d) one-sided d-resources at a non-sparse set of levels;
(E-e) approximate swallowing of good sets; failure of (H2'') (Remark 3.3). OPEN: (O4) infinite F. Lemma Z and density remain open for every
admissible operator. No counterexample is suggested.
