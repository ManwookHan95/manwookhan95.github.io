# cert3 report (Round 11): cluster D — transfer of refereed results to T_fin, window bookkeeping, Part I under option (a)

Referee: independent, adversarial, re-derivation from the sources.  ctx = scratchpad/ctx.  Working notes: ctx/r11/cert3_work/progress.md;
script ctx/r11/cert3_work/tu_mu_cert3.py (outputs tu_mu_cert3.out = run 1, tu_mu_cert3b.out = run 2).
Sources read: Q1_notes 0-3.6; Q1_refa_notes, Q1_refa_part3/part4, Q1_refb_notes; MTVI_graph; Part II (paper2/martin_density_note_II.tex)
Sections 3 (l.1913-3090: def:II-base ... lem:II-GW, rem:II-GWuse), 4.3-4.5 (lem:II-bankformula, lem:II-TU, def:II-companionw,
lem:II-donorraise, lem:II-compcost), 5.6 (def:II-DU1 ... thm:II-MTIV, l.6621-7545), scans of lem:II-cost/VT/donorpeak/status/transplant/
hoffman/loj/B/subset; refB R11, revision_log, refA R3; U4_notes 1-4, U4_ref_notes; U1_notes 3.4, U1_ref_notes 6-8; X2_notes 6.1;
X1_ref_notes 9; Part I (paper/martin_density_note.tex) l.91-620, 712-900, 2676-3760, 4183-4232, 4722-4760.
Verdict labels: correct / correct_with_fixable_gaps / wrong / unclear.

## 0. Bottom line and verdicts

The transfer of the refereed results to T_fin goes through, with ONE substantive defect on the tree (window count, Q1 (S6)/(E-d)),
which is fixable in two independent ways, and one substantive defect OFF the tree (route-X zero-value absorbers do not work for T_fin as
defined; this only kills Q1 2.7's "double coverage" claims, not MT VI).  Every other inspection-only link checks out once the
interface below is written down.

| # | Link (graph item) | Verdict | Fix / remark |
|---|---|---|---|
| 1 | Q1 1.7 CONCLUSION "every refereed result on the tree holds for T_fin, level read as main stage" [INSP][T] | correct_with_fixable_gaps | true for every tool on the tree EXCEPT the class/cube window count (item 5); the transfer is now written out (Sections 1-2): 18 interface properties, each verified for T_fin |
| 2a | X2 6.1 D^{X2} "PROVED (by inspection)" | correct_with_fixable_gaps | "weights enter only through upper bounds" is false as stated (absorber R, absorber least entry, cluster capacity are lower-bound uses); harmless (relative or computed-after; Q1 I2/I3/I6 + refb P-R); "survives by GW" does not cover the class/cube count (item 5) |
| 2b | X1 Lemma W'(4) (X1-ref 9 W4) | correct_with_fixable_gaps | lower-bound list incomplete (misses U1-ref 7's least-entry bound = refb P-R); otherwise correct |
| 2c | U1-ref 6.3 "lost features unused" | correct | (W5),(W6),(W7) at absorber stages and (FD) are used only by V4 / (SF*), (SF_tau), (GM) (off tree) and by lem:II-scales(e) (replaced by S2 below) |
| 2d | U4 Lemma GW / [II] lem:II-GW applied to T_fin | correct_with_fixable_gaps | (GW1)-(GW4) re-derived for T_fin at main stages; the meta-claim "every window condition survives because Q only grows" fails for the class/cube count, whose exponent C(J+2)+C_K+2(2C+1)p is not of GW's X_l form C^{l^2}(C/u)^{omega+8}Des^8 |
| 3 | Part II tools (lem:II-TU, prop:II-bank, lem:II-scales(d),(e), prop:II-transplant(iii)-(iv), prop:II-KN, def:II-Gamma, prop:II-ray, lem:II-classes, lem:II-recursion, lem:II-domfine, lem:II-SCi, lem:II-coststat, lem:II-trueshift, lem:II-firsttouch, def:II-DU1, lem:II-VT, lem:II-subset, thm:II-B, lem:II-hoffman, lem:II-loj, thm:II-clean) for T_fin | correct_with_fixable_gaps | all transfer through the interface of Section 1, with lem:II-scales(d) re-proved via B_mu and lem:II-scales(e) via fresh absorber coordinates; lem:II-classes' and prop:II-ray(d)'s bounds "<= Dbar(w)" and the count in thm:II-MTIV's proof need item 5's fix; lem:II-zerovalue (route X, off tree) does NOT transfer (Section 8) |
| 4 | mu-base Lemma TU / Lemma DR(ii) / bank efficiency (U4 C1, 4.4(a)) [1P] | correct | re-derived; numerics 90/90 at the c_T scaling; run 1 shows that c_T must contain l^{-1} 4^{-G(l)} (s'v')^2, which Design(l) provides |
| 5 | Window count (P8; refb 1.7; Q(w) without Dbar(w)^3) | Q1 as written: wrong (C_U1 "absolute" is false); refa P8: correct; refb 1.7: incomplete | fix A (P8: support-first pigeonhole + omega(L) >= 2^L - 1 or exponent +l^2) or fix B (add Dbar_fin(w)^3 to Q(w) at main stages); (E-d) re-checked under both, including K_data <= K_*^{J+2}K and C_f^p |
| 6 | P7 (patterns over the blocks of stages <= l; l_f) [1P] | correct | precision; verified (Section 6) |
| 7 | Part I with ||T|| = c_1 < 1 (prop:reduction, lem:pair, prop:smooth, prop:approximants, lem:martintail, thm:engineered + lemmas) [INSP] | correct | proofs read: every use of T is (T-b), (T-c), (T-d) or the UPPER bound q^*(Te) <= 1 (Section 7) |
| off | Q1 2.7 route X for T_fin; MT VI(b1) "alternatively 2.7(b)" | wrong as a proof (off tree); truth of the statement unclear | the cited zero-value tuning (U1 Lemma 3.3, gap refB R11; Part II lem:II-zerovalue, proved only for mu* with its p_0 rule) does not apply to T_fin's first used absorber pair after a main stage (Section 8); MT VI unaffected (route V only) |

## 1. The transfer, written once: the interface used by the Part II / Round 5-8 tools, verified for T_fin

T_fin = Q1 1.1-1.3: base mu_s = 2^{-s^2-1} (||U|| = 1/4); S_l = {2^l(2i+1)}; rounds PRE/MAIN/CLUSTER; no (FD); generic c_l in
[(1-2^{-l})c^max_l, c^max_l]; absorber R from lb_l, p_0 < ... < p_R the least odd integers > max(9, max T(l-1)); (W_exp) in c^cl(p);
(D-lev) with n_l; b(w) = min(b_U4, b_X1); Q(w) = max{(4Des/u)^{omega+20}, (Des/u)^{C_U1}}; Design(l) = [U4's Design(l)] x (main-stage
factors 4^{R_cl} 2^{k(l+R_cl)} eta_l^{-1}) x (QC factors) x ((D-lev) factor).  Part II's operator: mu*_s = 2^{-2^{2^s}} (||U|| = 1/16),
(FD) stages, fixed cluster weights c^low_{p+1}4^{1-i}, p_0 large ((mu*_{p0})^{2^{2^{p0}}-1} < 2^{-R}), Q >= Dbar(w)^3 at main stages,
Des(l) with B*(l) = 2^{s_t}/(delta_min mu*_{s_t}^2).

Reading the proofs of the tools listed in item 3 (and of the Round 5-8 originals they reproduce), the operator enters ONLY through the
following properties.  Each is verified for T_fin; "MS" = at the sub-windows of MAIN stages (the only windows used on the tree).

Base
 B1 Diagonal-base identities (lem:II-base(b), lem:II-bankformula, eq:II-bankformula, (i)-(iii)): exact for EVERY diagonal base.  T_fin: yes
    (U4 1.1).  The doubly exponential decay (lem:II-base(c),(d), rem:II-whybase, prop:II-RSwindow(c), (O10)-(O12)) is used only for
    infinite F and in lem:II-zerovalue (route X); neither is on the tree.
 B2 ||U|| <= 1/2, 0 < mu_s <= 1 decreasing, nu <= ||U||.  T_fin: ||U|| = 1/4.  Part II uses nu <= 1/16 numerically in
    lem:II-donorraise(i) (d_m <= Des^{1/3}Lambda/8); with 1/4 the bound is Des^{1/3}Lambda/2 — constants only (lem:II-compcost(a),(d)
    need N Des^{1/3}Lambda <= 1, true for l >= l_f).
 B3 Bank efficiency at the FIRST element j' = s'_{l''}(l) = min(S_{l''} ∩ (s_max(l), inf)) of every carrier l'' <= l:
      (mu_{j'})^2 v_{l''}(j') >= Des^{-1/6},   (mu_{j'} v_{l''}(j'))^{-2} <= Des^{1/3},   v_{l''}(j') >= Des^{-1/6}.
    These are the only base-dependent inputs of lem:II-TU (contraction |M'| <= C_f Des^{2/3} eps_x, kappa_T <= C_f Des eps_x^2),
    lem:II-donorraise (d_m <= Des^{1/3}Lambda), prop:II-transplant (Des^{1/3}Lambda), thm:II-B, prop:II-KN (via TU).
    T_fin (re-derived, U4 C1): j' <= sigma(l) := max_{l''<=l} s'_{l''}(l); v(j') = delta 2^{-j'}/n >= (4/5)delta_min(l)2^{-sigma(l)};
    mu decreasing gives mu_{j'}^2 v(j') >= (4/5)delta_min/B_mu(l), B_mu = 2^{sigma}/mu_sigma^2; (mu v)^{-2} <= (25/16)(B_mu/delta_min)^2;
    v(j') >= (4/5)delta_min/B_mu (B_mu >= 2^sigma).  U4's bracket contains l 2^{l^3} B_mu delta_min^{-1} with l 2^{l^3} >= 2, so
    Design^{1/6} >= 2B_mu/delta_min and all three hold.  Part II's depth s_t(l) (third element) is needed only for infinite F
    (pair tuning on support coordinates, deep raises); on the tree the depths are the first element (TU banks, peak pushes, (C3)) and
    the second (X2's lever bank j(l), (D-lev)).
 B4 Lever efficiency mu_j^2 v_l(j) >= 1/Design(L) for j <= sigma_2(L) (X2 Lemma LV, (D-lev) with n_l, X2-ref (p-LV1)).  T_fin: the
    factor max_{l''} 2^{sigma_2} n_{l''}/(mu_{sigma_2}^2 delta_{l''}) is in Design(L); no weight enters.
Signature ladder
 S1 S_l pairwise disjoint, even, bounded gaps G_l = 2^{l+1}; allowedness (a); (c) with margin for main targets; (P1) (u_{l'}(s) = 0 for
    l' < l, u_l(s) = v_l(s) on S_l).  T_fin: identical (Q1 1.1(ii), 1.2(r.1); A_fin proof; absorber targets satisfy (a): refb 1.5).
 S2 s_max(l) -> infinity, hence (eq:II-Finside) F ∪ T(l) ⊂ [1, s_max(l)] and S_{l''} \ [1, s_max(l)] ⊂ S^nat_{l''}(l) for l >= l_f.
    Part II gets this from (FD) (lem:II-scales(e), the ONLY use of (FD) on the tree).  T_fin (NEW, written proof): every main stage p is
    followed by R_cl(p) = 2|E^ch(p)| >= 2 cluster stages (E^ch(p) ⊇ T(p) ⊇ supp y_1 != {}); an absorber target at stage l has support
    {s, p_0, ..., p_R} with p_0 > max T(l-1), so s_max(l) >= p_R > s_max(l-1).  Main stages occur in every round, so s_max(l) >=
    #{absorber stages <= l} -> infinity.  u(w), b(w) -> 0 is FD-free (u(w) = b(w^-) <= T_lo(w^-)^4).
Weights
 W1 (P2) at MS: sum_{l'>L} lambda_{l'} <= c_{L+1}/3 <= b(L, M(L))^2/3 <= T_lo(w)^8 for w of level L.  T_fin: c_{L+1} <= c^cl(L) <= b(L,M(L))^2,
    later weights by c_{l+1} <= c_l/4.  (At levels that are not main stages (W2) is not imposed; their sub-windows are never used.)
 W2 (W3) Phi_k <= c_k <= (delta_k H_k)^2 for all k (used by lem:II-recursion, lem:II-SCi, U1 Lemma 4.3 for fine carriers).  T_fin: imposed
    at PRE/MAIN and p+1; implied at p+i, i >= 2 (refb 1.2: c <= b(p,M(p))^2 <= 2^{-8n(p,M(p))}, n >= p 2^{p^3} B_mu^6 >= 2^{12 s_max(p)^2}).
 W3 (W4'') with the factor T_lo(.)^3 (cluster stages: T_lo of their main stage) — lem:II-domfine(i), prop:II-absorb.  T_fin: (S4).
 W4 c_{l+1} <= c_l/4 everywhere; consecutive block-1 stages: lambda ratio >= 8 (lem:II-domfine(ii), U1-ref 7).  T_fin: (W1) and the
    cluster rule c^max_{p+i} <= c_{p+i-1}/4, k increasing.
 W5 (W_exp) c_{L+1} <= exp(-1/T_lo(L,M(L))) for main L (X2-ref (p-W)).  T_fin: in c^cl(L); inherited by all later weights (refb 1.4).
 W6 Lower-bound uses of weights (complete list after this audit): (i) absorber R (U1 3.3(i)/lem:II-zerovalue: route X only) — T_fin I3;
    (ii) absorber least entry eta_k >= mu_{p0}^2 c_k^2/64 in U1-ref 7 / lem:II-domfine(ii) — used ON the tree (route V, owners in
    absorber blocks) — T_fin: refb P-R, eta_k >= mu_{p0}^2 c_k^2/2^13, and U1-ref 7's chain n(p'-1) >= Design(p'-1) >= (B_mu D)^6 >=
    (1/(eta_k lambda_k))^6 survives (B_mu(p'-1) >= 2^{p0}/mu_{p0}^2 since sigma(p'-1) > p_0, D >= 1/Phi_k); (iii) cluster capacity
    lambda_a >= c_{L+1}/Design(L) (prop:II-absorb(c): route X only) — T_fin I2 (factor >= 1/2); (iv) design-computed bounds
    (lambda_l >= 1/D(l), Phi_min(L) >= 1/D(L), x_0) — computed after the weights.  Nothing else uses a lower bound on a weight
    (checked in lem:II-recursion/domfine/SCi/SCband/coststat/trueshift, Lemma PM, S2c^tr, Theorem UE's c_fine/c_tiny/W_pull/W_lev).
Design and windows
 D1 Design domination (lem:II-scales(c), prop:II-bank(d),(e)): l, D_r, 2^{G(l)}, 1+|T(l)|, G**(l), H_tune(l), H_conf(l) <= Des^{1/6};
    Des >= Lip, 1/delta_comb, (r c')^l, C_*, C_L, N_L, 1/delta_sh; Des >= 2^{6l^3}; Des >= Lambda°.  T_fin: U4's bracket^6 contains
    l 2^{l^3}, B_mu, 2^{s_max}, 2^{G}, delta_min^{-1}, Lambda°, 1+|T|, D(l), G*(l) (Z4: max Hoffman constant over Z4's configurations, the
    analogue of Part II's H_conf), H_comb, G**(l), H_tune, Xi^Y; times Lip, (2+1/delta_comb), (rows cols)^l, C_*, C_L, (1+1/delta_sh).
    [Part II's refA R3 deleted G*, H_comb, Xi^Y because Part II never defined them; in T_fin they are defined in Z4/Z6/Y2 and only enlarge
    Design — harmless.]  The tools on the tree use G**(l) (prop:II-transplant l.4302-4503), not H_conf itself (H_conf occurs only in Des,
    (K1) and the bound G** <= H_conf).  Dictionary: Y1 1.2's G**(l) (generalized configurations (U,P,eps,F',type), box rows |tau| <= beta
    on all of U) dominates Part II's G**(l) up to a factor 2 (the extra rows on P are redundant: viol_II <= viol_Y1 <= 2 viol_II).
 D2 Window relations at MS: Q(w) >= (4Des/u)^{omega+20}; T_hi <= 2^{-l^3}/(lQ); n >= l 2^{l^3} Q; u(w^+) = b(w) < u(w) (bands disjoint);
    b <= eta = T_lo^4/(l Des); beta := (1+Lip C_*)b <= eta, C_L beta^{2/N_L} <= eta; Des^k T_lo <= u/8 (k <= 40).  T_fin: the first
    term of Q is literally Part II's; b = min(b_U4, b_X1) <= b_U4, which is Part II's b, so every UPPER bound on b holds; no tool uses a
    lower bound on b (u(w^+) = b(w) enters Q(w^+) only as 1/u, enlarging it).  Bands disjoint: refb 1.1(d).
 D3 (GW1)-(GW4) of lem:II-GW at MS.  T_fin: (GW1) from D2 and Design >= Lambda°; (GW2) from Q >= (4Des/u)^{omega+20} and Des >=
    (l 2^{l^3} Lambda°)^6 (U4's bracket^6); (GW3) from W1 and the box bound [I, Lemma 8.10]; (GW4) by the definition of T_hi.
    lem:II-GW(b): (T-a) without the equality clause (Section 7), (T-b)-(T-d) (Q1 A_fin), (P1)-(P3) at MS.
 D4 Window COUNT for the class/cube pigeonhole: Part II assumes Q(w) >= Dbar(w)^3 (def:II-DU1), U1-ref 8 assumed Q >= D_cls^2(Des/u)^C,
    Q1 (S6) assumes D_cls <= C_{f,N}(Design/u)^{C_D} with ABSOLUTE C_D.  T_fin as written: NOT satisfied — Section 5 (fix A or B).
Absorber structure (route V uses absorbers only as fine carriers)
 A1 D^{U1'} structure: biased pairs, first touchers (lem:II-firsttouch / U1 Lemma 3.2 / U1-ref 6.4).  T_fin (re-derived): for s in
    E_c(w) and a main stage L: s in T(L) or s in S_{l''} ∩ [1, L] lies in E^ch(L), whose cluster immediately follows L; otherwise
    s in S_{l''} ∩ (L, s_far]: later carriers meeting s are pairs for s (PRE pairs of every later main target meeting s, since
    Sigma(Y_r) = supp Y_r ∩ ∪S_{l'}; cluster pairs of later main stages p >= s), absorber targets meet only fresh odd p_i > max T(l-1)
    (never an even s) and their own s, signature sets are disjoint, the fallback y^(1) lives in Z_0.  So the first two carriers after L
    meeting s are a consecutive biased pair (or none).  No (FD) target exists.
 A2 Zero-value tuning of absorbers (lem:II-zerovalue, U1 Lemma 3.3): route X ONLY.  Fails for T_fin as defined (Section 8).

## 2. Transfer table: every Part II / Round 5-8 statement on the tree of MT VI, with the interface items its proof uses
"OK" = every item used holds for T_fin (Section 1); the proof then applies verbatim with Des := Design_Tfin, mu* := mu, "level" :=
"main stage".  Graph ids in brackets.

| Statement (Round source -> Part II label) | Items used (from reading the proof) | T_fin |
|---|---|---|
| U1 Lemmas 1.1-1.5, Lemma R-kt [L2-U1a, L2-U1i] -> lem:II-cert, lem:II-kappa, lem:II-kappader, cor:II-Rkt, prop:II-Rkt | none (any T, any compact dense-range U) | OK |
| U1 Lemma 2.1 [L2-U1b] -> lem:II-shift | none | OK |
| U1 Lemma 2.4 [L2-U1c] -> lem:II-subset | none (averaging) | OK |
| U1 2.3 classes [L2-U1e] -> lem:II-classes | D1 (H(L) <= C Des^C/u, entries <= C_f Des), P7 (J <= 2L), D4 for "#classes, K_*^{J+2}, A_i <= Dbar" | OK modulo D4 (Section 5) |
| U1 2.1/2.4, Prop 2.2(a)-(d) [L2-U1f] -> def:II-Gamma, prop:II-ray | (a)-(c),(e): D1, D2, B1, lem:II-hoffman; (d): D4 | (a)-(c),(e) OK; (d) needs Section 5's fix |
| U1-ref 5 G1 release [L2-U1g] -> def:II-compclass(2) | W1 (2^{-s_far} <= c_{L+1}^2, values move <= 4c_{L+1}^2), D2 | OK |
| U1 Lemmas 4.1, 4.2 (+U1-ref 7), 4.3, 4.5, 4.6 [L2-U1h] -> lem:II-recursion, lem:II-domfine, lem:II-SCi, lem:II-coststat, lem:II-trueshift | W2 ((W3)), W3 ((W4'') with T_lo^3), W4 (ratio >= 8), W1, W6(ii) (P-R), D1 (Des(k) >= 1/(eta_k lambda_k) at main k: factor eta^{-1}D^6), D2 | OK (route-X items (c) of domfine, absorb-(c) not needed) |
| U1-ref 3.3 Prop KN [L2-U1j] -> prop:II-KN | B3 (via lem:II-TU), D1 (C_L, N_L, Lip), D2 (C_L beta^{2/N_L} <= eta), lem:II-status, lem:II-kappader | OK |
| U1 Lemma 3.2 under D^{U1'} [L2-U1d] -> lem:II-firsttouch | A1 | OK (re-derived for T_fin, Section 1 A1) |
| D^{U1'} [L2-U1d] -> def:II-DU1, lem:II-DU1 | Part II's version has mu*, fixed cluster weights, p_0 rule, Dbar | NOT transferred; replaced by T_fin's own recursion (Q-T, 2 passes) + I2/I3/I6 + P-R; lem:II-DU1(b) holds for T_fin by W1; (c) is this report |
| U4 T_final, Lemma W [L2-U4a] -> def:II-Tfinal, lem:II-W, prop:II-bank | B3 (mu-base version: U4 C1), S2 (FD-free), D1 | OK with B3 re-derived for B_mu and S2 re-proved |
| U4 Theorem 2.2 [L2-U4b] -> thm:II-lemmaB, prop:II-subwindows | S1, W1, D2; (T-a) without equality | OK (Q1 A_fin; refb 1.1(d)) |
| U4 Lemma GW [L2-U4c] -> lem:II-GW | D2, D3 | (GW1)-(GW4) OK; survival claim needs D4 (item 2d) |
| U4 4.4(a): V1 DR(ii), TU, bank efficiency, mu-base [L2-U4d] -> lem:II-TU, lem:II-bankformula, lem:II-donorraise | B1, B2, B3, D1 | OK (Section 4) |
| U3 Lemma VT [L2-U3] -> lem:II-VT | none (any T) | OK |
| V1 Theorem 2' [L3-V1a] -> thm:II-clean, cor:II-clean | D2 (M(l) = omega(l)+1 disjoint bands) | OK (T_fin's enlarged scheme: omega counts all objects) |
| V1 Lemma TU [L3-V1b] -> lem:II-TU | B1-B3, D1, S1, S2 ((T1),(T2): far parts of S_{l''} beyond s_max are outside F^2) | OK; Q1 2.2's modified use (KN-1 pull at v(j_p) >= max(correction, c_{L+1})) is cluster A |
| V1 Lemma ST [L3-V1c] -> lem:II-status | D1, D2 (threshold buffer Lambda = T_lo^3 >> beta_w), B3 | OK |
| V1 Lemma CO [L3-V1d] -> lem:II-compcost (+lem:II-cost) | B2, B3, D1, D2, W1 | OK (nu <= 1/4: constants) |
| V1 Prop TR(iii)-(iv) [L3-V1e] -> prop:II-transplant | D1 (G**(l), D_r, l), B3 (Des^{1/3}Lambda), D2 | OK for f^#_w; its use at the KN^tr companion is cluster A |
| V1 moves (C1),(C2) [L3-V1f] -> def:II-companionw | S1, S2 (z-moves on S^nat, T(l)) | OK (base-free) |
| V1 Lemma D [L3-V1g] -> lem:II-donorpeak | W1 (sum lambda <= b^2/2) | OK |
| V1 Lemma B [L3-V1h] -> lem:II-bankformula | B1 | OK (exact identity) |
| V2 Lemma H, Lemma L [L3-V2a,b] -> lem:II-hoffman, lem:II-loj | none (algebra; Lojasiewicz on a compact cube) | OK |
| V2 Theorem B [L3-V2c] -> thm:II-B | B3 (TU), D1, D2 | OK |
| Z3 Lemma 3.1 [L3-Z3] -> lem:II-cost | none (any T) | OK |
| V1 Lemma CO/lem:II-cost, Z3: cost bounds with (1+||U||) | B2 | OK |
| [not on tree] lem:II-zerovalue, prop:II-absorb(b)-(d) (route X) | p_0 rule + mu*, e_1 < 2^{-R} | FAILS for T_fin (Section 8) |

Two quantitative differences between Part II's T_final and T_fin that enter constants only: ||U|| (1/16 vs 1/4) and the bank depth
(B*(l) at s_t vs B_mu(l) at sigma).  Neither enters a window exponent.

## 3. The inspection-only survival claims

3.1 Q1 1.7 CONCLUSION [I-1].  Q1's I1-I10 are correct (two passes; re-checked here: I2/I3/I6 are W6 (i),(iii); P-R is W6 (ii); I4, I5,
I7, I9, I10 are trivial).  The conclusion sentence chains U1-ref 6.3, X1 W'(4), X2 6.1 and U4 GW.  With the interface of Section 1 it is
TRUE for every statement in Section 2 except those depending on D4.  Verdict: correct_with_fixable_gaps.  Required: (i) replace the
sentence by the table of Section 2 (or cite this report); (ii) fix D4 (Section 5); (iii) state S2 (s_max -> infinity via absorbers);
(iv) state W6 completely (including P-R).

3.2 X2 6.1, D^{X2} "PROVED (by inspection)" [I-2].  Claim: admissibility, (P1), (P2), N-freeness unaffected "(they use weights only
through upper bounds and Design only through lower bounds)"; every refereed result survives by GW.  Check: (a) (D-lev) only enlarges
Design — correct (B4: no weight).  (b) (W_exp) is one more upper bound inside c^low_p (D^{X2}) / c^cl(p) (T_fin) — correct, BUT the
parenthetical premise is false as stated: absorber R, the absorber least entry (U1-ref 7) and the cluster capacity are lower-bound uses
of weights.  They survive because (W_exp) is imposed BEFORE R is computed (R from c^low resp. lb_l, which contain it: refb 1.4, I6),
the least-entry bound is relative (eta_k vs c_k of the same stage), and capacity is a ratio inside one cluster.  (c) "survives by GW":
false for the class/cube count (D4).  Verdict: correct_with_fixable_gaps (for T_fin the gaps are closed by Q1 I2/I3/I6, refb P-R and
Section 5).

3.3 X1 Lemma W'(4) (X1-ref 9 W4) [I-3].  W1 (option (a) is Martin-type), W2 (stage 1 in block 2), W3 (R from (1-2^{-p})c^low; cluster
maxima) verified (they coincide with Q1 1.2-1.3 and I3).  W4's "complete list of lower-bound uses" omits U1-ref 7's least-entry
bound eta_k >= mu_{p0}^2 c_k^2/64 (an upper bound on R), found by refb (P-R).  With P-R the list is W6 above, and every item survives
the factor 1 - 2^{-l} >= 1/2 (P-R: eta_k >= mu_{p0}^2 c_k^2/2^13, numerics of refb min log2 ratio -12.55).  "Lemma GW applies" — D4 as
in 3.2.  Verdict: correct_with_fixable_gaps.

3.4 U1-ref 6.3 "lost features unused" [I-3].  Lost at absorber/cluster stages: (W5), (W6), (W7) (V4's (SF*), (SF_tau), (GM)-(W6)),
and in T_fin also (W2) at cluster stages p+i, i >= 2 and (FD).  Uses found by reading: (SF*), (SF_tau), (GM) are used only by V4
(U4 4.4(e); Part II rem:II-scope); (W6)/(GM) only by V4 Lemma 3.4 (U4 C7); (FD) by V4 Prop 5.8 and lem:II-scales(e) (replaced by S2);
(W2) only at main stages (W1).  None is on the tree.  [(W4) — allowedness (b), used by (T-b), (T-c) — is NOT lost: (W4'') at PRE/MAIN,
and c^cl(p) contains (W4'') for every s in E^ch(p) (Q1 A_fin, refa D2).]  (T_fin even keeps (W5), (W7) at PRE stages and at p+1: more than U1-ref says —
refb 1.2.)  Verdict: correct.

3.5 U4 Lemma GW / lem:II-GW [I-4].  lem:II-GW(a),(b) re-derived for T_fin at main stages (D3).  rem:II-GWuse ("every window argument
uses X_l = C^{l^2}(C/u)^{omega+8} Des^8 R_l") is a description of proofs; it is correct for the Round 5-7 window theorems and for
Part I Section 8 (lem:II-GW(b)), but NOT for the activity-class/cube pigeonhole of Round 8 (U1 2.3-2.4, U1-ref 8, Part II
lem:II-classes/prop:II-ray), whose window factor is D_cls^2 K_data/c_flat with exponent ~ C(J+2) + C_K + 2(2C+1)p (Section 5): Part II
handles it OUTSIDE GW, by Q >= Dbar^3.  I8/I9 ("Q only grows", "(D1), (D2) only lower b") are correct monotonicity statements (every
condition in D2/D3 is monotone in Q and Design, and no tool uses a lower bound on b or an upper bound on Q, n or Design — checked in
S2c^tr, which uses only T <= 2^{-n} and Design <= n), but monotonicity cannot create the missing factor.  Verdict:
correct_with_fixable_gaps.

## 4. mu-base Lemma TU, Lemma DR(ii), bank efficiency (U4 C1, 4.4(a)) [item 25, L2-U4d]

4.1 Re-derivation.  B3 above (U4 C1(iii)).  Lemma DR(ii) (donor bank mass): mu^D = 2 nu Lam/(lambda_c mu_s^2 v_c(s)) <= 2 (1/4) D(l)
(5/4) B_mu Lam/delta_min <= Design Lam (lambda_c >= 1/D(l), nu <= ||U||) — correct; the Part II form d_m <= Des^{1/3}Lambda/2 (with nu <= 1/4)
also holds since 1/lambda <= D_r <= Des^{1/6} and (mu^2 v)^{-1} <= Des^{1/6}.  Lemma B(ii) (second-order cross effects): exact identity
eq:II-bankformula for any diagonal base; remainder <= (||U|| ||u||_1 + sum|c_j|mu_j^2|u(j)|/nu)||X||^2/(2nu^2) — base-free.  Lemma TU:
lem:II-TU's proof uses the base only through B3 and B2 (Section 1); with them, c_T = c_f Des^{-1}, C_T = C_f Des, kappa_T <= C_f Des eps_x^2,
|M'| <= C_f Des^{2/3} eps_x <= 1/2, n_{l''} >= (Delta nu - ||U|| kappa_T)/(s'^2 v') > 0.  Verdict: correct.

4.2 Numerics (independent; tu_mu_cert3.py, 2500 bits; the proof of lem:II-TU implemented literally with mu_s = 2^{-s^2-1}, ||U|| = 1/4,
S_l = {2^l(2i+1)}, banks at the first element beyond s_max in {5,7,9,11,13} (j' up to 24, mu_{j'}^2 down to 2^{-1154}), 1-3 tuned
carriers, pulls at the largest j with v(j) >= eps_x, explicit n(y), fixed point of M on [nu_p, nu_p + kappa_T] by Illinois root-finding).
 - Run 2 (tu_mu_cert3b.out), eps_x = fac x reg/(l 4^{G}), reg := min (s'v')^2, fac in {1e-4, ..., 10}: 90/90 succeed; val^# - val^(2) = x
   to working precision (~1e-600 relative to eps_x); max |M'| on I = 0.125; all bank masses > 0; other carriers move by O(eps_x^2/reg);
   T_fin's inequalities mu_{j'}^2 v' >= (4/5)delta_min/B_mu and (mu v)^{-2} <= (25/16)(B_mu/delta_min)^2 hold in all runs.
 - Run 1 (tu_mu_cert3.out), eps_x = fac x reg without the factor 1/(l 4^G): 58/90; the failures are negative bank masses for k = 3
   (gap G = 16) even at fac = 1e-4, and loss of the bracket for fac >= 1.  Cause (re-derived): kappa_T ~ (2^G eps_x)^2/reg dominates
   Delta nu for the shallow carriers.  This is NOT a counterexample: it shows that the hypothesis eps_x <= c_T = c_f Des^{-1} must contain
   l^{-1} 4^{-G(l)} (s'v')^2, which it does because Des^{1/2} >= l 4^{G(l)} and Des^{1/3} >= (s'v')^{-2} (both true for T_fin's Design).
   U4-ref's tu_mu_hp (3000 bits, threshold eta ~ reg for 1-3 carriers) is consistent.

## 5. The window count (D4): P8 vs Dbar(w)^3 vs refb 1.7; (E-d) re-checked

5.1 The constants (re-derived from lem:II-classes, prop:II-ray, thm:II-MTIV's proof, U1 2.3-2.4).  At a clean w of a main stage
L >= l_f (N fixed), with B := 4 Design(L)/u(w) (>= 16):
 (a) classes: J := |Omega| + N <= 2L (P7: N <= L once every block <= N has a carrier <= L); thresholds A_i = K_*^i, K_* >=
     max(2 Design, 4 C_f Design J H(L)), and K_* <= (Design/u)^{C_*} <= B^{C_*} for L >= l_f (C_f J <= Design); #classes <= (J+1)3^J.
 (b) data constant: zeroing the inactive components costs <= J A_{i(t)} K t <= J K_*^{J+1} K t; the projection moves <= (1/2)A_{i(t)+1}K t;
     so p^*(g - g_t) <= K_data t with K_data := C K_*^{J+2} K <= B^{C_*(2L+2) + C_K + 2} (K = C_f(Design/u)^{C_K}).  Q1's (E-c)
     "K_j = C_f(Design/u)^C" understates this; the exponent grows linearly in L (refa H1 is right).  [Part II's thm:II-MTIV proof has the
     same understatement in words ("K of the form C_f(Des/u)^C"), harmless there because Dbar's exponent C_Gamma(P(L)+2L+2) contains the
     2L+2.]
 (c) cubes: p = number of extreme rays of Gamma^#(kappa, a) at the realized ratios.  p depends on f (through the ratio variables of (X3)),
     so the only design-level bound is combinatorial: p <= P(L) := 2^{R_Gamma(L)}, R_Gamma(L) := 2|T(L)| + 16L (rows of T_fin's cones after
     the aggregation of (X1): T(L), S_{l''} ∩ [1, L], one far sign row per l'' <= L, (X3) per block, (X4)/(X4^0) per near-threshold carrier,
     (X5); equations counted twice).  P(L) <= Design(L)^{1/2} (2^{2|T(L)|} <= 2^{2 s_max(L)} <= Design^{1/3}, 2^{16L} <= Design^{1/6}).
     Original count: (A_max/eps)^p <= (C_f N (Design/u)^{2C})^p: exponent ~ (2C+1)P(L) and the factor C_f^p.
 (d) (E-d) needs, along the main stages used: |S| c_flat/K_data -> infinity, K_data T_hi(w)/|S| -> 0, theta_w/c_flat^2 -> 0 (the last is
     fine: theta_w <= C_f T^2 log(1/T), c_flat >= c_f u, T <= 2^{-Q} <= 2^{-(4/u)^{20}}).

5.2 Q1 as written.  (S6) asserts D_cls <= C_{f,N}(Design/u)^{C_D}, K = C_f(Design/u)^{C_K} with ABSOLUTE C_D, C_K, and builds
Q = max{(4Design/u)^{omega+20}, (Design/u)^{C_U1}}, C_U1 = 2C_D + C_K + 1.  By 5.1(b),(c) the true exponent of D_cls^2 K_data/c_flat is
~ 2(2C+1)p + C_*(2L+2) + C_K + 2, which is not bounded by an absolute constant.  The first term of Q absorbs it only if
omega(L) + 20 >= 2(2C+1)p + C_*(2L+2) + ..., and no inequality omega(L) >= 2(2C+1) p_max(L) is available (counting the minors of the
cone that realizes p_max gives only omega(L) >= n p_max >= p_max; nothing in the definitions forces a larger multiple).  VERDICT on
Q1 (S6)/(E-d): wrong as written (per refa H3 the error is inherited from U1/U1-ref (A4), "(Design/u)^C" without tracking J and p),
fixable.

5.3 Fix A (refa P8, re-derived).  Support-first pigeonhole: each Delta'_pr(t) lies in R^I, |I| = N, so a basic representation uses a
support J(t) of <= N linearly independent g_j (Caratheodory; prop:II-ray(c)'s "basic solution").  Pigeonhole over J(t)
(<= (P(L)+1)^N choices), then over eps-cubes of [0, A_max]^{J(t)} (<= (A_max/eps + 1)^N), eps := c_f(u/Design)^C/N.  On a set S with one
support J and one cube with corner a^max: Delta'^* := sum_J a^max_j g_j, incr(t) := sum_J (a^max_j - a_j(t)) r_j is a nonnegative
combination of extreme rays (in the cone), Delta'_pr(t) + Delta'(incr(t)) = Delta'^*, ||incr(t)||_1 <= N eps, so sqrt(Gamma^#) grows by
<= C_f N eps and kappa_w <= 1 + eta_0/2; prop:II-ray(e) (orthant) unchanged.  Count (L >= l_f):
   D_cls <= (2L+1)9^L (P(L)+1)^N (C_f N (Design/u)^{2C} + 1)^N <= B^{1 + N(2C+3)}   [(2L+1)9^L, P(L)+1, C_f N <= B].
Hence E := log_B(D_cls^2 K_data/c_flat) <= 2 + 2N(2C+3) + C_*(2L+2) + C_K + 4 <= C_0(L+1) (N <= L), C_0 absolute.  With
Q(w) >= B^{omega(L)+l^2+20} (refa I2; or Q1's Q and the count omega(L) >= #(ray components (R5)/(O5)) >= sum_{E ⊂ [1,L]} |E| >= 2^L - 1,
using the patterns (E, {}, +, F' = T(L)) whose cones are orthants): for L >= max(l_f, L_0(C_0)),
   |S| c_flat/K_data >= (n(w)/D_cls) c_flat/K_data >= L 2^{L^3} B^{omega+l^2+20-E} >= L 2^{L^3} -> infinity,
   K_data T_hi(w)/|S| <= B^E 2^{-2L^3}/(L^2 Q(w)^2) -> 0.
The factor C_f^p does not arise (only C_f^N, absorbed for L >= l_f(f, N)).  No change of T_fin's recursion is needed except deleting
"C_U1 absolute" (the second term of Q may stay; Q only grows).  Precision to refa: "p_max(L) in Design(L)" should be the combinatorial
P(L) (the cones depend on f), and it is already <= Design^{1/2}, so nothing has to be added to Design.  VERDICT: correct.

5.4 Fix B (Part II's mechanism).  Define Dbar_fin(w) := (2L+1)3^{2L}(Design(L)/u(w))^{C_Gamma(P(L)+2L+2)} with C_Gamma >= 2C + C_* + C_K + 4,
and at main stages Q(w) := max{Q(w), Dbar_fin(w)^3} (formed from L, T(L), Design(L), u(w): well founded, N-free).  Then, with the
ORIGINAL count: (A_max/eps)^p <= (C_f N Delta_max (Design/u)^{2C})^{P(L)} <= (Design/u)^{(2C+1)P(L)} once C_f N Delta_max <= Design/u
(L >= l_f) — this is where C_f^p is absorbed — so D_cls <= Dbar_fin; K_data/c_flat <= C_f Dbar_fin (exponent C_*(2L+2) + C_K + 2 <=
C_Gamma(2L+2)); |S| >= n/Dbar^2 >= L 2^{L^3} Dbar, so |S| c_flat/K_data >= L 2^{L^3}/C_f -> infinity and K_data T_hi/|S| <= C_f 2^{-2L^3}/
(L^2 Q) -> 0.  The eps-requirement C_f p eps <= small holds since P(L) <= Design^{1/2}.  Monotonicity: Q only grows, every condition of
D2/D3 is monotone, S2c^tr uses only T <= 2^{-n} and Design <= n (both preserved).  lem:II-classes and prop:II-ray(d) then transfer
VERBATIM.  VERDICT: correct.

5.5 Reconciliation.  refa (notes 2.7, part4 H-I): correct in substance (both the L-growth of K_data and the p-growth of the cube count
are identified; the support-first pigeonhole is right); precision as in 5.3.  refa part3 E(a) alone omitted K_data's K_*^{J+2} — fixed
in part4/notes 2.7.  refb 1.7 ("f-constants with 3^N and any N-dependent exponent of the cube count are absorbed ... because
omega(l) -> infinity"): INCOMPLETE — (i) p is not N-dependent but grows with L (up to P(L)); (ii) K_data's exponent C_*(J+2) grows with L;
(iii) "omega -> infinity" without a rate does not dominate a linear-in-L exponent, and nothing dominates (2C+1)p by omega.  refb's sentence
becomes correct AFTER fix A (remaining exponent O(L + N), and omega(L) >= 2^L - 1).  Recommendation: adopt fix A (no design change) and
state the count; fix B is an equally valid alternative that makes Part II's statements verbatim.  Both keep MT VI's quantifier order
(T_fin -> N -> f -> (g, rho) -> l_f -> L -> w -> class -> Step A -> (support, cube) -> Step B -> data).
Arithmetic illustration (cert3_work/window_count.py, .out; exponents of B): with C = C_* = C_K = 3 (resp. 10), fix A's exponent
E_A(L) = O(L) is absorbed by omega(L) + 20 >= 2^L + 19 for all L >= 6..10 (resp. 8..10) for N = 1, 3, 10, and by the l^2 variant for
L >= 8..17 (resp. 23..35); the original count needs a cube exponent ~ 2(2C+1)p = 14p (resp. 42p), which "omega >= p" cannot supply.

## 6. P7 (patterns over the blocks of stages <= l; choice of l_f) [1P refa]
Re-derived.  The cone Gamma^#(kappa, a) of p_N has a shift variable Delta'_m for every block m <= N.  If some block m <= N had no carrier
<= L, its Delta'_m would be a variable not enumerated by the design's level-L patterns (which only involve the blocks m(l''), l'' <= L),
and J could exceed 2L.  For L >= l_f, every block m <= N has a coarse carrier (its natural peak of Lemma M2 is a fixed stage index, an
f-constant; T_fin serves every block in infinitely many rounds), so N <= L, J = |Omega| + N <= 2L, and the pattern of f at w is among the
enumerated ones (blocks > N: rate objects := 1, V1-ref p0).  Q1 1.4(c)'s "the patterns of p_N at level l are among those of level l" is
therefore true for L >= l_f with l_f >= the least stage after which all N blocks have carriers.  VERDICT: correct (presentational
precision; N-independence of T_fin unaffected — the condition is on l_f, which may depend on N).

## 7. Part I with ||T|| = c_1 < 1 (option (a)) [I-7]
Proofs read (not grepped): def:admissible, rem:lemmaA/lemmaB, Section 1.2 (Phi_m(k) := 2^{-m-k}q^*(Te_{k,m}) <= 2^{-m-k}; L^*w =
T(sum_m sum_k m 2^{-m-k} w_m(k) e_{k,m}) — exact for every T), lem:martintail (|R_m x|_m <= m 2^{-m} q(x) from q^*(u) = 1 and
lambda <= m 2^{-m-k}), lem:dualball, lem:threshold, lem:rigidity (coefficient d_m s_k m 2^{-m-k}: exact for every T; uses (T-b), (T-c)),
prop:forced ((T-d): theta vanishing on a dense subset; Phi(n_j) -> 0), prop:smooth (base only), prop:continuity (Phi in l_2),
prop:approximants, prop:reduction, lem:pair (its "||T|| = 1" is the operator (f, rho g) into l_2^2, not Martin's T), lem:base, lem:block,
prop:expansion, lem:slack, lem:bookkeeping, lem:TV, prop:rebalancing, lem:transferdata ((T-d) tails), lem:persistence, lem:assembly,
lem:approxfacts (sum_k lambda <= 1, |(R_m x')(k)| <= lambda c'), lem:F1 (Phi_k <= 2^{-k}, sum Phi <= 1), lem:anchor (C <= ||Phi||_2 < 1/2),
def:SC, lem:scrambling, thm:engineered (Steps 0-6), lem:suplevel (M >= 1/2), lem:phicalc, lem:switchbudget.
Every use of T is through (T-b), (T-c), (T-d) or an UPPER bound implied by q^*(Te) <= 1 (Phi <= 2^{-m-k}, lambda <= m 2^{-m-k},
||Phi_m||_1 <= 2^{-m} < 1 in Lemma A, ||Phi_m||_2 < 1/2, ||R_m|| <= m 2^{-m}).  The equality clause and lower bounds on weights occur only
in def:admissible, the admissibility verifications (l.2344-2345, 3990) and the resonance example (l.2412-2415, 3834-3841: Phi_m(1) for the
explicit operator c_l = 2^{-(l-1)^2}), none on the tree.  Under option (a) T_fin satisfies (T-b)-(T-d) (Q1 A_fin, two passes).
VERDICT: correct.  (Interpretive remark, not a proof gap: option (a) gives a Martin-TYPE norm; Martin's Lemma B literally has norm one,
and T_fin(a)/c_1 is not T_fin(b) because the norm is not homogeneous in the weights — Q1 and refb E8 say so.)

## 8. Off-tree finding: route-X zero-value absorbers are not available for T_fin as defined
lem:II-zerovalue (Part II) = U1 Lemma 3.3 repaired after refB R11 (left endpoint of the intermediate-value sweep).  The repair needs
4e_1 <= 2^{-R} for the binary-coordinate perturbations e_r := mu_{p_r}^2 theta_a/nu, obtained in Part II from the crude bound
nu >= mu*_{p0} theta_a, the doubly exponential base and the p_0 rule (mu*_{p0})^{2^{2^{p0}}-1} < 2^{-R}.  For T_fin: (a) with the crude bound,
e_1 <= mu_{p1}^2/mu_{p0} = 2^{-p0^2-8p0-9} while 2^{-R} ~ mu_{p0}^2 c^2/64 = 2^{-2p0^2-8}c^2: fails for every p_0; (b) with the true
nu (an f-constant at late stages) and theta_a >= t|gamma_a u_a(p_1)| ~ T_hi |residue(s)| (needed for "no flips" at the binary
coordinates, prop:II-absorb(d); |gamma_a| >= |residue(s)|/|u_a(s)| >= |residue(s)|): since p_1 = p_0 + 2 and 2^{-R} <= mu_{p0}^2 lb^2/32
(minimality of R), e_1 < 2^{-R} forces theta_a < (nu/32) 2^{8p0+8} lb_a^2, i.e. |residue(s)| < C nu 2^{8p0} c_{L+1}^2/T_hi.  The residues on
T(L) contain the true-shift correction, of size up to C_f Des c_{L+1} (prop:II-absorb(a)) and not small in general.  For the FIRST absorber of the cluster of
L, p_0 exceeds only the fresh coordinates of earlier absorbers, max T(L) ~ 4 log_2(1/lb_{l'}) for the last absorber stage l' < L, so
2^{8p0} ~ lb_{l'}^{-32}, while c_{L+1} <= 2^{-8 n(L,M(L))} <= 2^{-8/Phi_{l'}^6} is incomparably smaller: the requirement FAILS unless the
residue at that s is astronomically small (< C nu c_{L+1} lb_{l'}^{-32} c_{L+1}/T_hi), which nothing guarantees (later absorbers
of the same cluster are fine, since their p_0 lies beyond the ~2 log_2(1/c_{L+1}) binary coordinates of the first one; absorbers carrying
only the constant coefficient c_0(a) are fine as well).  So for the first used pair the left-end value of the sweep can be positive and
the IVT fails, exactly as in refB R11.  Consequence: Q1 2.7(a),(b) ("route X
valid for T_fin", "double coverage", MT VI(b1) "alternatively 2.7(b)") and X1's MT IV^tr for T_fin are not supported.  MT VI is NOT affected
(route V tunes no absorber; Q1 2.1).  Possible repair (not needed for MT VI): choose p_0 >= C log_2(1/lb_l) (c^low/lb_l do not depend on p_0)
and round greedily for the perturbed weights 4·2^{-r}(1+e_r) as in refB R11's fix, or simply delete the route-X claims for T_fin.

## 9. Required fixes (all fixable; none changes MT VI's statement)
 F1 (on tree; item 5) Replace Q1 (S6)'s "D_cls <= C_{f,N}(Design/u)^{C_D}, C_U1 absolute" and (E-d)'s count by fix A (5.3: support-first
    pigeonhole; Q exponent omega(l) + l^2 + 20, or the count omega(L) >= 2^L - 1) or by fix B (5.4: Q := max{Q, Dbar_fin(w)^3} at main
    stages).  State K_data = C K_*^{J+2}K in (E-c).
 F2 (on tree; item 1) Replace Q1 1.7's conclusion sentence by the interface B1-B4, S1-S2, W1-W6, D1-D4, A1 and the table of Section 2.
    In particular write S2 (s_max -> infinity via fresh absorber coordinates; lem:II-scales(e) without (FD)) and B3 (lem:II-scales(d),
    prop:II-bank(c) with B_mu at the first element beyond s_max).
 F3 (on tree; items 2a, 2b) X2 6.1 / X1-ref W4: replace "weights only through upper bounds" by the list W6 (incl. refb P-R).
 F4 (on tree; item 2d) Restrict rem:II-GWuse / U4 GW's survival claim to the Round 5-7 window theorems and Part I Section 8; the Round-8
    class/cube count is handled by F1.
 F5 (precision; items 5, 6) P(L) := 2^{R_Gamma(L)} combinatorial (cones depend on f); P7 as in Section 6.
 F6 (off tree) Delete or repair Q1 2.7(a),(b) and the "alternatively 2.7(b)" in MT VI(b1)'s proof (Section 8).

## 10. Files
 - ctx/r11/cert3_report.md (this report); ctx/r11/cert3_work/progress.md (working notes);
 - ctx/r11/cert3_work/window_count.py (+ window_count.out): log-scale exponent arithmetic of Section 5;
 - ctx/r11/cert3_work/tu_mu_cert3.py (lem:II-TU transplanted to the mu-base, 2500 bits; run 2 is the current version of the script),
   tu_mu_cert3.out (run 1: eps_x = fac·reg; 58/90, failures explained in 4.2), tu_mu_cert3b.out (run 2: eps_x = fac·reg/(l 4^G); 90/90).
