# G1 referee notes (Round 14): proofs of the verdicts and of the fixes for r14/G1_notes.md
# ("exactness only where it is needed": cushioned Hoffman lemma, strict/soft split, linear Step A, split preparation)

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Part files: r14/G1_ref_part1.md ... G1_ref_part4.md.  Scripts and
outputs: r14/G1_ref_work/.  "Mod chain" as in G1 (links cited by J1.15', J2.1, H2.A, Part III).  Notation as in G1 and Part III:
L main stage, w clean sub-window, b = b(w) < u = u(w), T = T_lo(w), T_hi = T_hi(w), B := 4 Des(L)/u, n <= 2L active variables,
p rows of the enlarged class cone, p(L) the maximum of p over patterns of level L.

## A. Verdicts
| # | G1 claim | Verdict | Fix / precision |
|---|---|---|---|
| 1 | Lemma CH (PROVED) | correct | P-CH1 (sign form on N_k), P-CH2 (sharper constant), P-CH3 (normalization) |
| 2 | Remark CH(c), Cor. CH.1 (PROVED) | correct | -- |
| 3 | Lemma 2.1 (PROVED mod chain) | correct | P-21a notation tr_j; P-21b weights among design data |
| 4 | Lemma 2.3 (PROVED) | correct | P-23: C_T fixed after C_A, C_x, C_Lip, C_r |
| 5 | Theorem G1.A (PROVED mod chain) | correct with fixable gaps | P-A1 closeness clause; P-W window count (design insertion); P-N |
| 6 | Cor. G1.B (PROVED, inspection) | correct | P-B constant in D_tol |
| 7 | Remark 2.2 (SKETCH) | label honest | size bookkeeping missing; not used |
| 8 | Lemma LE (PROVED) | correct | -- |
| 9 | Lemma 3.2, Theorem G1.C (PROVED mod chain) | correct with fixable gaps | G-T2 (bands in protected blocks; F-2 rescaling); P-A1; P-23; generalization for G-S2 |
| 10 | Lemma 3.3 (PROVED) | correct with fixable gap | P-L1: theta_pr >= 64 rho A_0 s_1/T |
| 11 | Lemma 4.2 (PROVED mod chain) | correct | P-L1; wording on (K2-d) |
| 12 | Lemma 4.4 (PROVED) | correct with fixable gap | P-44: "multiplied by 1 - dkappa/kappa"; no other ratio-dependent row |
| 13 | Lemma 5.1 (PROVED) | correct in isolation; used out of scope | G-S2 |
| 14 | Prop. 5.2, Cor. 5.3 (PROVED mod chain, first order) | correct in the restricted linear model | P-52': "iff" only there; realization needs margin |
| 15 | Cor. 5.4 (PROVED mod chain) | correct | P-54 wording ("does not make the block residual") |
| 16 | Lemma 5.5, (NT_0) (PROVED) | correct | P-55 half-radius cover; holds for every compact k-semialgebraic Z^str |
| 17 | Theorem G1.D, stages without thick-type carrier (PROVED as reduction) | correct with fixable gaps | G-S2 (proof sentence), G-T2 (band set), Q-1 (quantifiers) |
| 18 | Theorem G1.D, thick-type part (SKETCH) | label honest | transfer of H1's first-order levers to x^nat unwritten |
| 19 | Persistence (necessary condition) | correct | Q-1, H2-ref Q-2 |
| 20 | (LSC-trunc)_N for every f; density (OPEN) | OPEN | -- |

## B. Re-derivations (claims found correct)
B.1 Lemma CH.  Pigeonhole: the <= p inequality slacks miss one of [Lambda^k V, Lambda^{k+1} V), k = 0..p; N_k := E u {s_i <
rho}, rows outside have slack >= Lambda rho.  Strict basis B_s: a nonzero q x q minor of strict rows is >= u by (SE).  Maximal
robust extension B (robust sets have independent rows, so |B| <= n); for i in N_k \ B every (|B|+1)-minor of B u {i} is < u, hence
<= mu, so by Cauchy-Binet and the Gram identity dist(a_i, row A_B) <= 2^{n/2} mu/u = eta; strict rows of N_k lie in row A_{B_s}.
Projection onto ker A_B: |x' - x| <= |B|^{|B|/2} rho/u (sigma_min(A_B) >= vol/||A_B||^{|B|-1}); a_i x' = d_i x' on N_k; rows outside
N_k keep slack >= rho.  Numerics: 600/600 random instances (ref_ch_check.out).
B.2 Remark CH(c): two equality rows e_1, (e_1 + delta e_2)/|.|, data e_2: violation ~ delta, distance 1 to the exact set.
B.3 Strict/soft classification (G1 3.1).  Only target coordinates carry two coarse carriers; after the preparation every
target coordinate with a contact or (X1^F) row is an S_th support coordinate (Lemma III-prep (d)); free targets with tiny room are
closed and banked; robust support carries no row.  Strict rows: (X3), (X1-FR), single-variable rows; every strict minor without
(X3) row is a polynomial in level-L design data (incl. robust-peak and (KN) weights, P-21b): 0 or >= delta'_comb.
B.4 Lemma 2.1.  (a) banked coordinate: symmetric split of an anti-signed V' gives anti-sign parts <= delta/2 + |beta_s| <=
3|a^#_s|/t for delta <= 4|a^#_s|/t; (U3^inf) needs nothing about b^theta on supports; kappa changes by <= 4 dbar(L) theta/t << Kt.
Raised tiny support: the deep-assignment interval is nonempty iff s_j V_c(j) >= -2A_j - tr_j; A_j := 2|a^#_j|/t >= |a^r_j|/t keeps
the flip-bound estimate.  (b) kind [3]: the margin is 3 lambda gap^#/t against C_f lambda(c_{L+1} + D^C c_{L+1}^2).  (c) (X3) is
the true shift; FR violations only have (VT').
B.5 Lemma 2.3: mu_tol >= b (Des/u)^{C_T - C} (theta_T) or >= b Q(w)/Des^C (theta_0, or the g'-term) since T_hi <= 2^{-L^3}/(LQ(w)).
B.6 Theorem G1.A: the uses of the cone point in Prop. III-cushion, Lemma III-CMtr (c), (d) and Prop. III-BR (U3) are exactly:
exact (X3), exact (X1-FR), contact/tiny-support signs at S_th targets, inward rows, single-variable sign rows (orthant, class
signs, contact-likeness of Step-A banks), and the closeness bound.  Verified line by line.
B.7 Cor. G1.B (iv): cofactor polynomials are not minors of the cone matrix and were used only for A_max / the cube
normalization, which route V omits (Lemma III-nocube, III-nocubeinf, III-count).
B.8 Lemma LE: expansion along the unique (X3) row; Farkas/Cramer consistency with ||lambda||_1 <= (2L+1)Des^{3/2}; Cramer point
with |delta| <= Des^2 beta; the one-sided version by Hoffman with design rows (constant <= Des^2).  Numerics: ref_le_44_check.out.
B.9 (NT_0): |rho - 1| is a rate object, so near-threshold carriers have |rho_l(f) - 1| <= b; Lemma III-Tblock (a) gives F(r(f)) <=
1 + Des^C b; preparation and projection add <= Des^C b; b <= eps_0/Des^C (P-CHOICE).
B.10 Lemma 3.3: at the linear scale 1/gap_min <= Des^C/b <= exp(C log^3(1/T)) (log(1/b) <= C log^3(1/T), Lemma III-late), K_w and
Lambda_lev are polynomial in window quantities (cert2), so (LATE), (L2)-(L5), (W_exp)-bookkeeping and the drift bound hold:
everything is exp(-C log^3(1/T)) against s_1 ~ exp(-1/(2T)).
B.11 Lemma 4.2 (e): first-order action of a bank at a contact s is (mu_s^2/nu) theta z_s u(s) (nu changes at second order since
a_s = 0), of a raise (mu_s^2/nu) Delta a_s Dev(s); so strict minors move by <= b_bias = b T_hi (Des/u)^{C_T + C} << b.
B.12 Lemma 5.1 (isolated minor): first cofactors are minors with one (X3) row (rate objects); in case (ii) M = F^T y + G = E^T x + G on
A_x x A_y, hence constant, a ratio of design polynomials, so 0.
B.13 Prop. 5.2: Farkas for {a, e >= 0; b, c free} gives (a)-(c); the dropped term -(dkappa/kappa)M(rc) is second order.
Cor. 5.3 (iii): D_M(s) = det[[u_+(s), u_-(s)], [u_+(j), u_-(j)]]; kind-(iv) carriers have no private two-sided resource, so only
shared FR coordinates and TS generators enter.
B.14 Lemma 5.5: compactness + finite cover of Lambda = Z^str cap {F = 1} by local-step balls (H1 Lemma 2.2, J1.11 for Z^str by
the same genericity argument: Z^str and psi_d are defined over k, which contains no Phi_d, d in N_T).

## C. Findings and fixes (with proofs)

P-A1 (Theorem G1.A, closeness clause).  (E3)'s |r^# - r(f)| <= u/(4 Lip) does not give the needed data violation bound: the term
Lip |r^# - r(f)| K_X is then only <= u K_X/4, not << K T_lo.  The proof uses |r^# - r(f)| <= Des^C b.  FIX: (E3) reads
|r^# - r(f)| <= eta'(w) (J1.13 (i) and Lemma III-floorrow (b) need <= 2 eta' in (T)-blocks).  Then Lip eta' K_X <= Des^C T^4 <<
K T_lo, and V <= 2(1 + C_Gamma J A_{i(t)}) K t as claimed.  Theorem G1.C's companions satisfy |r^# - r(f)| <= Des^C b/u^3 << eta'.

P-W (Theorem G1.A, window count).  CLAIM (PROVED).  With (D-G1a) Des(L) >= p(L)^{p(L)^2} and the insertion
   (D-G1b)   omega(L) >= 8 (p(L) + 4)(L + 1) + C_K + 8,
Lemma III-count (c) holds with K_*(w) := max(K_*, 6(H_CH(C_Gamma J + 1) + 1), (K_P(w)/K)^{1/2}).
Proof.  Lambda = 2p^{p/2}/u + 1 <= 3 p^{p/2}/u, so H_CH = 2 p^{p/2} Lambda^p/u <= 2 * 3^p p^{(p^2+p)/2} u^{-p-1} <= 2*3^p Des u^{-p-1}
(p^{(p^2+p)/2} <= p^{p^2} <= Des); with the normalization P-N (u -> u/(2 Des^{1/2})) H_CH <= B^{p+3}.  Hence K_*(w) <= B^{p+4}
(C_Gamma J <= B), K_data = C K_*^{J+2} K <= B^{(p+4)(2L+2) + C_K + 1}, D_cl <= B^{L+1}, c_flat >= B^{-2}, and
log_B(D_cl K_data/c_flat) <= (p+4)(2L+2) + L + C_K + 4 <= omega(L) + L^2 + 20 - 2L by (D-G1b).  With n(w) >= L 2^{L^3}
B^{omega(L)+L^2+20}: |S| c_flat/K_data >= L 2^{L^3} and K_data T_hi(w) <= 2^{-L^3}/L.  (D-G1b) is a function of the level-L patterns
only (f-free, N-free, well founded), and enlarging omega(L) only enlarges M(L), Q(w), n(w) and lowers T_lo(w) (Lemma
III-designinf (d)).  QED.  [G1's argument "omega(L) >= 2^p because the rate scheme contains all minors" is not supported by
that reason: one p x n matrix with n <= 2L has <= 4^L (p+1)^{2L} minors.  The insertion makes the point moot.]

P-N (normalization in Lemma CH).  CLAIM (PROVED).  In natural units with every (KN)-row (X4) multiplied by lambda_l, all entries of
the class-cone rows have modulus <= 2 ((X4^0): m^2|r_l|K = lambda_l rho^0_l <= 2 lambda_l), so row norms are <= 2(2L)^{1/2};
normalizing divides a k x k minor (k <= n <= 2L) by <= (8L)^L <= Des^{1/2}.  Robust minors (>= u/2 at r^#) become >= u/(2 Des^{1/2});
tiny ones only decrease.  So Lemma CH applies with u replaced by u/(2 Des^{1/2}); eta and H_CH change by factors absorbed in
Des^{C_r + 1} (in mu_tol) and in P-W.

G-T2 (Definition 3.1 (T2), (T5) and (E3) of Theorem G1.C).  The verification of (E3) checks statuses at the TARGETS; the realized
point lies within the bands.  In a (T)-block a symmetric band of half-width beta on an active row l with r_l != 0 changes R_a(m)^2 at
first order by up to 2m^2|r_l| beta/kappa, hence the protected floor statuses by up to Des^C beta; with beta ~ beta_* ~ Des^C b/u
this is ~ Des^C b/u, against the margin mu = c Des^{C_x - 1} b.  Since u(w) = b(w^-) <= T_lo(w^-)^4 <= Des(L)^{-4 omega(L)} for every
sub-window but the first (Def. III-Tfinstage (S6)), no absolute C_x makes mu dominate.  Likewise the fixed (U)-rescaling s_m =
1 - 4 Des^{C_x} b of (T5) does not compensate first-order band effects in (U)-blocks.
FIX (PROVED).  Use the band set of Theorem H2.A / J1.15', which is what Theorem G1.D actually uses:
 (i) PROTECTED blocks (a (T)-block with N(m) nonempty, a (KN)-block with a pushed inactive near-threshold carrier): two-sided
     (kind (i)) rows realized exactly at their f_1 ratios; kind-(iv) K^- rows with shrinking overshoot bands (|r_l| decreases,
     so R_a^2 and every status of the block decrease: Lemma III-K, sigma_rob pattern-only); K^+ rows locked ((R-L)); zero-data
     rows with bands only under (J-e): mu >= C D^C m^2(beta_*/kappa)^2, which holds because (Des^C b/u)^2 << Des^{C_x} b
     (b <= T^4, u >= T^{1/20}).  In unprotected blocks bands only move robust statuses, by Des^C beta << u: harmless;
 (ii) (U)-blocks: s_m := J1-ref F-2's joint selection at the realized values, 1 - s_m <= C(Des^{C_x} b + D^C sum_l(|r_l| beta_l/kappa +
     beta_l^2/kappa^2)) <= Des^C b/u << u; Z^str is preserved (c_M = 0, minors homogeneous in r^(m), Lemma III-Uscale), soft minors
     move by << mu_tol (P-23), statuses are <= 1 - Des^{C_x} b at the realized values by construction of s_m.
Then at the realized point every protected status is <= its target status ((T)-blocks) or restored by s_m ((U)-blocks), and
(E3) holds with the margins of G1.  ((KN)-block K^+ bands: J1's (KN) SKETCH, as in H1-ref P-KN.)

G-S2 (Lemma 5.1 used out of scope; Theorem G1.D proof and Theorem G1.C/Lemma 5.5 hypotheses).  Lemma 5.1 treats one two-(X3)
minor in isolation.  When the same blocks carry single-(X3) tiny strict minors (affine sets A_m, A_{m'}), the restriction of M to
A_m x A_{m'} is bilinear with first derivatives that are design COMBINATIONS of first cofactors -- not rate objects -- and the joint
zero set can be at non-linear distance.  Model (ref_me2_system.out): M_1 = x_1 - x_2, M_1' = y_1 - y_2, M = x_1y_1 + x_2y_2 +
(x_1 - x_2)/2 + (y_1 - y_2)/2, start s = t = sqrt(b/2): every tiny minor <= b, all four first cofactors of M ~ +-1/2 (robust); Lemma
5.1 (i) zeroes M but leaves |M_1| ~ 2.3 b; dist(start, {M_1 = M_1' = M = 0}) = 1.00 sqrt(b) for b = 1e-4..1e-10.
FIX (PROVED as a restatement).  (a) Lemma 5.1 applies when M is the only tiny strict minor involving the ratios of its two blocks.
(b) (R-S2) := "some tiny strict minor contains >= 2 (X3) rows, and the strict system has no point of Z^str within Des^C b of the
start that is compatible with the one-sided constraints" (G1's notes' wording; the model above is such a stage).  (c) Lemma 5.5
holds for Z^str := {r in K_kappa : all tiny strict minors vanish} for every pattern (its proof never uses affineness: compactness,
k-semialgebraicity, genericity of Phi^T, H1 Lemma 2.2), and Theorem G1.C holds with (T1) := "a compatible exact point of Z^str
within Des^C b" in place of "a point of prod A_m": (E1) holds at that point, (NT_0) gives F <= 1 + Des^C b there, Lemma 5.5 gives the
(T3) target unless (R-S3).  With (a)-(c), Theorem G1.D's statement stands; its proof sentence "Lemma LE (and Lemma 5.1 for a
single two-(X3) minor) gives the (T1) targets" is replaced by "the negation of (R-S1), (R-S2) gives the (T1) targets".

P-44 (Lemma 4.4).  CLAIM (PROVED).  Under the move, to first order, M changes by -(dkappa_m/kappa_m) M (not by 0); if M contains
another ratio-dependent row (an (X4^0) row of a block whose values move, or a second (X3) row) the change is in general not a
multiple of M.  Proof: Delta r^(m) = (c u^(m)(j) - r^(m) dkappa)/kappa_m; on the columns of M the change of (X3)_m is
-(c/kappa)(X1)_j - (dkappa/kappa)(X3)_m, and the determinant is linear in that row.  Numerics: 1.4e-8 vs 7e1 (ref_le_44_check.out).
For STRICT minors (the use in Prop. 5.2/Cor. 5.3) no other ratio-dependent row occurs, so the consequences are unchanged: moves at
j can neither create nor destroy the vanishing of M.

P-52' (Prop. 5.2).  As H2-ref P-41: the Farkas "iff" is exact for the restricted LINEAR model; the converse direction needs strict
feasibility with margin of order rho_0^nat to survive the second-order terms (-(dkappa/kappa)M, generator side effects absorbed
by bands).  The actual residual is contained in the certificate class (necessary condition).

P-L1 (Lemma 3.3 (a), Lemma 4.2).  theta_pr := max(64 rho A_0 s_1/T, 4 Des K_DC r): Part III's (L1) is s_1 <= theta T/(64 rho A_0)
(32 rho s_1 max|b^theta| <= 32 rho s_1 A_0/T must be <= theta/2 so that no S_th coordinate enters the raise set W_F).  The
remark "the pre-row moves design-depth coordinates by <= K_w Pi << theta_0" (Lemma III-depthclean) concerns normer/room
types, not support moduli (only raised by the pre-row), so theta_pr << K_w Pi is harmless.

P-23 (Lemma 2.3, (E2)).  Fix the absolute C_T after C_A, C_x, C_Lip, C_r: C_T >= C_A + C_x + C_Lip + C_r + C + 10.  Then
Lip(W^nat + beta_band)/kappa_min + (1 + 2 Lip)b <= mu_tol/2.

P-55 (Lemma 5.5).  Cover Lambda by half-radius balls B(r_*^i, delta_i/2) and use the local step on B(r_*^i, delta_i); then
eps_0, m_0 <= (3/16) min delta_i/V keeps every curve in its validity ball.

P-54 (Cor. 5.4).  "the block is not residual" -> "this resonance does not make the block residual" (other strictly pinned or
locked rows, or G-T2's restricted band set, may still make it residual).

Q-1 (Theorem G1.D, persistence).  "the selected stage has one of ..." -> "EVERY clean sub-window w and EVERY class a with
>= n(w)/D_cl(w) scales has one of ..." (failure of (LSC-trunc) = no (w, a) realized at the stage); memory statements need
consecutive (R1) stages (H2-ref Q-2).

P-21a, P-21b, P-CH1-3, P-B: notation/constants, see the part files.

## D. Additional observation (supports G1's main obstacle; not a counterexample)
At a single stage, an Example-4.3 shape with a FREE common target j is consistent with every proved constraint: f decides which
other shared target coordinates are free (two-sided FR generators) and which are contacts (then banked: one-sided generators with
D_M(bank at s) = z_s det[[u_+(s), u_-(s)], [u_+(j), u_-(j)]], sign chosen by f's contact sign z_s).  So design genericity of target
values cannot by itself exclude (R-S1); G1's next step (1) needs an extra structural input (e.g. a second FREE shared target with
non-parallel values, which f can deny by making it a contact).  The obstruction must still be renewed at every main stage
(fresh kind-(iv) carriers, H2 Lemmas 2.6/2.7).

## E. Numerics (sanity only; r14/G1_ref_work/)
 ref_ch_check.py/.out: independent Lemma CH implementation (exhaustive maximal robust extension); 600 random instances with
   planted exact strict dependencies and tiny cushioned defects of both signs: all conclusions 600/600, |B| <= n 600/600,
   |x'-x|/V median 1.8, max 1.0e6 (the Lambda^p pigeonhole factor is really used).
 ref_me2_system.py/.out: the G-S2 model; joint exact point at distance 1.00 sqrt(b) while all first cofactors are robust.
 ref_le_44_check.py/.out: Lemma 4.4 identity dM = -(dkappa/kappa)M (1.4e-8), failure with an extra (X4^0)-type row (7e1);
   Lemma LE Cramer points exact to rounding (3000 integer design systems).
 G1's scripts re-read; outputs consistent with its notes.

## F. Most valuable idea
The strict/soft split.  Exactness on the zero set is needed only for minors built entirely from EQUALITY rows ((X3) and FR rows at
free target coordinates with robust room).  Every row at a banked S_th target coordinate (contact or raised tiny support) and every
inward row has a cushion of size theta/t (resp. lambda gap/t), and the cushioned Hoffman lemma shows that a tiny minor through such
a row only produces a violation proportional to that minor.  So contact-row resonances (H2 Example 4.3, the configuration behind
the persistent-(R1) candidates) are no longer obstructions; the residual is pushed onto FREE target coordinates, and wherever the
strict structure is single-(X3) the exactification and the near-threshold descent become LINEAR (no Lojasiewicz/Puiseux exponent).

## G. What remains open (precise)
(1) (R-S1): one-signed STRICT linear resonances -- tiny nonzero minors made of one (X3) row and FR rows at free shared target
    coordinates with robust room, annihilated by every two-sided generator, one-signed against every one-sided raise/bank, wrong-
    signed at the start; at all large main stages, at every clean sub-window and class (Q-1), with fresh kind-(iv) carriers.  By D,
    f's free/contact choice at the other shared targets can produce this at a single stage; persistence is the open question.
(2) (R-S2): strict systems with >= 2 (X3) rows -- including the shared-block case of G-S2, where exactification can require
    displacement ~ sqrt(b); closing the rate scheme under the Jacobian minors of the restricted systems (G1's suggestion) is not done.
(3) (R-S3): one-sided blocking of linear near-threshold descent; (R-L): locked K^+ rows (H2 Lemma 3.4(c) SKETCH).
(4) (R0^str): transfer of H1's lever lemmas to x^nat with strict pinning (SKETCH).
(5) Inherited: once-refereed links (H1, H2, J1, J2, Part III Section 5 chain), (KN)-block band bookkeeping (J1's SKETCH).
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) for the Martin-type p:
OPEN.  No counterexample is claimed by G1 or suggested by anything found here.
